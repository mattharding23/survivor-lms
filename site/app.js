// Survivor LMS static site. No build step, no backend -- fetches the JSON/
// markdown the weekly Action writes to data/ (relative paths only: this is
// served from a GitHub Pages *project* site, i.e. a subpath, so absolute
// paths like "/data/..." would 404).

async function getJSON(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error(`${path}: ${r.status}`);
  return r.json();
}

async function getText(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error(`${path}: ${r.status}`);
  return r.text();
}

// ---------------------------------------------------------------------
// Branding -- same palette/sources as the pipeline's chart PNGs
// (survivor_core/branding.py's fallback colors + ESPN logo CDN), so the
// site reads as one system with the exported images.
// ---------------------------------------------------------------------
const TEAM_COLORS = {
  ARI: "#97233F", ATL: "#A71930", BAL: "#241773", BUF: "#00338D",
  CAR: "#0085CA", CHI: "#0B162A", CIN: "#FB4F14", CLE: "#311D00",
  DAL: "#003594", DEN: "#FB4F14", DET: "#0076B6", GB: "#203731",
  HOU: "#03202F", IND: "#002C5F", JAX: "#006778", KC: "#E31837",
  LA: "#003594", LAC: "#0080C6", LV: "#000000", MIA: "#008E97",
  MIN: "#4F2683", NE: "#002244", NO: "#D3BC8D", NYG: "#0B2265",
  NYJ: "#125740", PHI: "#004C54", PIT: "#FFB612", SEA: "#002244",
  SF: "#AA0000", TB: "#D50A0A", TEN: "#0C2340", WAS: "#5A1414",
};
const teamColor = (abbr) => TEAM_COLORS[abbr] || "#444444";
const teamLogo = (abbr) => `https://a.espncdn.com/i/teamlogos/nfl/500/${abbr.toLowerCase()}.png`;
const logoImg = (abbr) => `<img class="logo" src="${teamLogo(abbr)}" alt="" loading="lazy" onerror="this.style.visibility='hidden'">`;

// Same 3-stop red -> amber -> green scale as the ranked_table chart's win%
// column (viz.py's _RGGRAD), clamped over the same [0.30, 0.88] win-prob
// range so a given win% reads as the same color on the site as in the PNG.
function winProbColor(p) {
  const t = Math.max(0, Math.min(1, (p - 0.30) / (0.88 - 0.30)));
  const stops = [[0.75, 0.06, 0.16], [0.85, 0.64, 0.25], [0.25, 0.56, 0.16]]; // red, amber, green
  const seg = t < 0.5 ? [stops[0], stops[1], t * 2] : [stops[1], stops[2], (t - 0.5) * 2];
  const [a, b, f] = seg;
  const mix = (i) => Math.round((a[i] + (b[i] - a[i]) * f) * 255);
  return `rgb(${mix(0)}, ${mix(1)}, ${mix(2)})`;
}
function textOn(rgbStr) {
  const [r, g, b] = rgbStr.match(/\d+/g).map(Number);
  const lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
  return lum < 0.55 ? "#fff" : "#1a1a1a";
}

// ---------------------------------------------------------------------
// Tiny markdown renderer. The only input this ever sees is our own
// report.py's output -- a fixed, predictable dialect (# / ## headers,
// **bold**, `code`, "- " bullets, "> " blockquotes, and pandas
// .to_markdown() GFM pipe tables) -- so a hand-rolled line-based pass
// covers it without pulling in a library.
// ---------------------------------------------------------------------
function renderMarkdown(md) {
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const inline = (s) => esc(s)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");

  const lines = md.replace(/\r\n/g, "\n").split("\n");
  const out = [];
  let i = 0;
  let inList = false;

  const closeList = () => { if (inList) { out.push("</ul>"); inList = false; } };

  while (i < lines.length) {
    const line = lines[i];

    // GFM pipe table: a "| a | b |" header line immediately followed by a
    // "|---|---|" (with optional :-- alignment) separator line.
    if (/^\s*\|.*\|\s*$/.test(line) && i + 1 < lines.length &&
        /^\s*\|[\s:|-]+\|\s*$/.test(lines[i + 1])) {
      closeList();
      const splitRow = (r) => r.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map(c => c.trim());
      const header = splitRow(line);
      let j = i + 2;
      const rows = [];
      while (j < lines.length && /^\s*\|.*\|\s*$/.test(lines[j])) {
        rows.push(splitRow(lines[j]));
        j++;
      }
      out.push("<table><thead><tr>" + header.map(h => `<th>${inline(h)}</th>`).join("") + "</tr></thead><tbody>");
      for (const row of rows) {
        out.push("<tr>" + row.map(c => `<td>${inline(c)}</td>`).join("") + "</tr>");
      }
      out.push("</tbody></table>");
      i = j;
      continue;
    }

    if (/^#{1,3}\s+/.test(line)) {
      closeList();
      const m = line.match(/^(#{1,3})\s+(.*)$/);
      const level = Math.min(m[1].length + 1, 4); // keep site h1 as the page title
      out.push(`<h${level}>${inline(m[2])}</h${level}>`);
    } else if (/^>\s?/.test(line)) {
      closeList();
      out.push(`<blockquote>${inline(line.replace(/^>\s?/, ""))}</blockquote>`);
    } else if (/^-\s+/.test(line)) {
      if (!inList) { out.push("<ul>"); inList = true; }
      out.push(`<li>${inline(line.replace(/^-\s+/, ""))}</li>`);
    } else if (line.trim() === "") {
      closeList();
    } else {
      closeList();
      out.push(`<p>${inline(line)}</p>`);
    }
    i++;
  }
  closeList();
  return out.join("\n");
}

// ---------------------------------------------------------------------
// Shared (league-wide) view
// ---------------------------------------------------------------------
function renderPctBars(pct, source) {
  const el = document.getElementById("pct-bars");
  const src = document.getElementById("pct-source");
  src.textContent = source ? `(${source})` : "";
  const entries = Object.entries(pct)
    .filter(([, v]) => v != null && v > 0)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 12);
  const max = entries.length ? entries[0][1] : 1;
  el.innerHTML = entries.map(([team, v]) => `
    <div class="bar-row">
      ${logoImg(team)}
      <span class="abbr">${team}</span>
      <span class="bar-track"><span class="bar-fill" style="width:${(v / max) * 100}%;background:${teamColor(team)}"></span></span>
      <span class="pct">${(v * 100).toFixed(1)}%</span>
    </div>`).join("");
}

function renderLeagueTable(teams) {
  const tbody = document.querySelector("#league-table tbody");
  tbody.innerHTML = teams.slice(0, 15).map(t => {
    const wc = winProbColor(t.win_prob);
    return `
    <tr class="${t.rank === 1 ? "is-rec" : ""}">
      <td>${t.rank}</td>
      <td class="team-cell">${logoImg(t.team)}<span>${t.team}</span></td>
      <td class="scale-cell" style="background:${wc};color:${textOn(wc)}">${(t.win_prob * 100).toFixed(1)}%</td>
      <td>${(t.pub_pick_pct * 100).toFixed(1)}%</td>
      <td>${t.pick_score.toFixed(0)}</td>
    </tr>`;
  }).join("");
}

async function loadShared() {
  const [pct, ev] = await Promise.all([
    getJSON("data/public_pct.json"),
    getJSON("data/league_ev.json"),
  ]);
  document.getElementById("week-line").textContent =
    `Week ${ev.week} — generated ${new Date(ev.generated_at).toLocaleString()}`;
  renderPctBars(pct.pct, pct.source);
  renderLeagueTable(ev.teams);
}

// ---------------------------------------------------------------------
// Chart viewer -- a dropdown + <img> pair, fed by the actual branded PNGs
// report.py already generates (win probability, pick distribution, best
// picks, ranked table, and -- shared only -- teams remaining pool-wide).
// Same pair of elements is reused for the shared section and swapped per
// member in the personal section.
// ---------------------------------------------------------------------
function wireChartViewer(selectEl, imgEl, basePath, charts) {
  selectEl.innerHTML = "";
  if (!charts || !charts.length) {
    selectEl.disabled = true;
    imgEl.removeAttribute("src");
    imgEl.alt = "No charts available yet";
    return;
  }
  selectEl.disabled = false;
  charts.forEach(c => selectEl.add(new Option(c.label, c.file)));
  const show = (file) => {
    const c = charts.find(c => c.file === file) || charts[0];
    imgEl.src = basePath + c.file;
    imgEl.alt = c.label;
  };
  selectEl.onchange = () => show(selectEl.value);
  show(charts[0].file);
}

const chartManifestPromise = getJSON("data/charts/manifest.json").catch(() => ({ shared: [], members: {} }));

async function loadSharedCharts() {
  const manifest = await chartManifestPromise;
  wireChartViewer(
    document.getElementById("shared-chart-select"),
    document.getElementById("shared-chart-img"),
    "data/charts/shared/",
    manifest.shared,
  );
}

// ---------------------------------------------------------------------
// Personal (per-member) view
// ---------------------------------------------------------------------
async function loadMember(slug) {
  const article = document.getElementById("personal-md");
  article.innerHTML = "<p class=\"muted\">Loading…</p>";
  const [mdResult, manifest] = await Promise.allSettled([getText(`data/members/${slug}.md`), chartManifestPromise]);

  if (manifest.status === "fulfilled") {
    wireChartViewer(
      document.getElementById("personal-chart-select"),
      document.getElementById("personal-chart-img"),
      `data/charts/${slug}/`,
      manifest.value.members ? manifest.value.members[slug] : null,
    );
  }

  if (mdResult.status === "fulfilled") {
    article.innerHTML = renderMarkdown(mdResult.value);
  } else {
    article.innerHTML = `<p class="muted">Couldn't load this member's recommendation (${mdResult.reason.message}).</p>`;
  }
}

async function loadMemberList() {
  const idx = await getJSON("data/members/index.json");
  const select = document.getElementById("member-select");
  select.innerHTML = "";
  idx.members.forEach(m => select.add(new Option(m.name, m.slug)));
  select.addEventListener("change", () => loadMember(select.value));
  if (idx.members.length) loadMember(select.value);
}

loadShared().catch(e => {
  document.getElementById("week-line").textContent = `Couldn't load league-wide data (${e.message}).`;
});
loadSharedCharts().catch(() => {});
loadMemberList().catch(e => {
  document.getElementById("personal-md").innerHTML =
    `<p class="muted">Couldn't load the member list (${e.message}).</p>`;
});
