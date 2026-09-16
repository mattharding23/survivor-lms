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
      <span class="abbr">${team}</span>
      <span class="bar-track"><span class="bar-fill" style="width:${(v / max) * 100}%"></span></span>
      <span class="pct">${(v * 100).toFixed(1)}%</span>
    </div>`).join("");
}

function renderLeagueTable(teams) {
  const tbody = document.querySelector("#league-table tbody");
  tbody.innerHTML = teams.slice(0, 15).map(t => `
    <tr>
      <td>${t.rank}</td>
      <td>${t.team}</td>
      <td>${(t.win_prob * 100).toFixed(1)}%</td>
      <td>${(t.pub_pick_pct * 100).toFixed(1)}%</td>
      <td>${t.pick_score.toFixed(0)}</td>
    </tr>`).join("");
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
// Personal (per-member) view
// ---------------------------------------------------------------------
async function loadMember(slug) {
  const article = document.getElementById("personal-md");
  article.innerHTML = "<p class=\"muted\">Loading…</p>";
  try {
    const md = await getText(`data/members/${slug}.md`);
    article.innerHTML = renderMarkdown(md);
  } catch (e) {
    article.innerHTML = `<p class="muted">Couldn't load this member's recommendation (${e.message}).</p>`;
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
loadMemberList().catch(e => {
  document.getElementById("personal-md").innerHTML =
    `<p class="muted">Couldn't load the member list (${e.message}).</p>`;
});
