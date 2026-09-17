# Survivor — Week 2 (2026) — Matt (Mattymo)

- Win-prob sources: **odds-api:32**
- Public pick %: **survivorgrid** survivorgrid ok (https://www.survivorgrid.com/)
- Opponents tracked: **0** (0 alive)
- Teams already used by you: **JAX**

## ✅ Recommended Week 2 pick: **LAC (Los Angeles Chargers)**
- Market win probability: **71.8%**
- Public pick %: 2.8%  |  expected dupes in your pool: 382.34 (2.8% of those alive)
- EV(path) = -4.8513   EV(myopic) = -0.3812
- Implied season plan if you take LAC now:
  `W2:LAC  W3:SF  W4:CHI  W5:NE  W6:LA  W7:DEN  W8:DAL  W9:SEA  W10:IND  W11:KC  W12:CIN  W13:PHI  W14:DET  W15:GB  W16:BAL  W17:BUF  W18:HOU`

> ℹ️ The pure win-probability path optimiser would open with **SF** this week; **LAC** ranks #1 once the future-value guard and consensus penalty are applied. Both are shown below — adjust `future_value_penalty` / `consensus_penalty` in config.py to taste.

## Unconditional optimal season plan (pure Π win-prob)
`W2:SF  W3:KC  W4:CHI  W5:NE  W6:LA  W7:DEN  W8:DAL  W9:SEA  W10:IND  W11:LAC  W12:CIN  W13:PHI  W14:DET  W15:GB  W16:BAL  W17:BUF  W18:HOU`
- Expected weeks survived (Π win-prob): **0.010**  (sum log wp = -4.653)

## Ranked available teams
|   rank | team   |   pick_score |   win_% |   public_% |   pool_dupes |   pool_% |   future_val |   EV_path |   rest_logwp | implied_next_picks                   |
|-------:|:-------|-------------:|--------:|-----------:|-------------:|---------:|-------------:|----------:|-------------:|:-------------------------------------|
|      1 | LAC    |        100   |    71.8 |        2.8 |       382.34 |      2.8 |        0.109 |   -4.8513 |       -4.47  | W2:LAC  W3:SF  W4:CHI  W5:NE  W6:LA  |
|      2 | TB     |         98.3 |    77.1 |       29.5 |      4028.22 |     29.5 |        0.008 |   -4.8803 |       -4.455 | W2:TB  W3:SF  W4:CHI  W5:DET  W6:LA  |
|      3 | PHI    |         95.9 |    74.3 |       12.3 |      1679.56 |     12.3 |        0.155 |   -4.9203 |       -4.501 | W2:PHI  W3:SF  W4:CHI  W5:DET  W6:LA |
|      4 | SF     |         95.9 |    87.8 |       29.4 |      4014.57 |     29.4 |        0.306 |   -4.9218 |       -4.523 | W2:SF  W3:KC  W4:CHI  W5:NE  W6:LA   |
|      5 | BAL    |         93.7 |    77.3 |        7.1 |       969.5  |      7.1 |        0.264 |   -4.9587 |       -4.57  | W2:BAL  W3:SF  W4:CHI  W5:NE  W6:LA  |
|      6 | CHI    |         92.7 |    66.1 |        1.5 |       204.82 |      1.5 |        0.155 |   -4.9762 |       -4.506 | W2:CHI  W3:SF  W4:MIN  W5:DET  W6:LA |
|      7 | KC     |         91.4 |    71.5 |        2.8 |       382.34 |      2.8 |        0.396 |   -4.9974 |       -4.511 | W2:KC  W3:SF  W4:CHI  W5:NE  W6:LA   |
|      8 | HOU    |         90.1 |    58   |        0.4 |        54.62 |      0.4 |        0.069 |   -5.0199 |       -4.455 | W2:HOU  W3:SF  W4:CHI  W5:DET  W6:LA |
|      9 | CAR    |         89.6 |    57.1 |        2.7 |       368.69 |      2.7 |        0     |   -5.0283 |       -4.455 | W2:CAR  W3:SF  W4:CHI  W5:DET  W6:LA |
|     10 | NE     |         87.2 |    67.9 |        1   |       136.55 |      1   |        0.325 |   -5.0686 |       -4.569 | W2:NE  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     11 | DAL    |         86   |    65.1 |        1.1 |       150.21 |      1.1 |        0.148 |   -5.0896 |       -4.608 | W2:DAL  W3:SF  W4:CHI  W5:DET  W6:LA |
|     12 | LA     |         84.7 |    73.8 |        1.3 |       177.52 |      1.3 |        0.4   |   -5.1114 |       -4.667 | W2:LA  W3:SF  W4:CHI  W5:DET  W6:NE  |
|     13 | DEN    |         83.9 |    58.7 |        0.2 |        27.31 |      0.2 |        0.186 |   -5.1255 |       -4.533 | W2:DEN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     14 | SEA    |         83.6 |    64.6 |        1.5 |       204.82 |      1.5 |        0.262 |   -5.1302 |       -4.599 | W2:SEA  W3:SF  W4:CHI  W5:NE  W6:LA  |
|     15 | BUF    |         83.2 |    68.2 |        1.5 |       204.82 |      1.5 |        0.303 |   -5.1382 |       -4.648 | W2:BUF  W3:SF  W4:CHI  W5:DET  W6:LA |
|     16 | GB     |         76.4 |    61.5 |        3.6 |       491.58 |      3.6 |        0.216 |   -5.2529 |       -4.672 | W2:GB  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     17 | ATL    |         73.8 |    42.9 |        0.2 |        27.31 |      0.2 |        0     |   -5.2978 |       -4.455 | W2:ATL  W3:SF  W4:CHI  W5:DET  W6:LA |
|     18 | NYJ    |         67.5 |    38.5 |        0.1 |        13.66 |      0.1 |        0     |   -5.4053 |       -4.455 | W2:NYJ  W3:SF  W4:CHI  W5:DET  W6:LA |
|     19 | CIN    |         64.5 |    42   |        0.2 |        27.31 |      0.2 |        0.153 |   -5.4556 |       -4.539 | W2:CIN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     20 | ARI    |         62.5 |    35.4 |        0.1 |        13.66 |      0.1 |        0     |   -5.4905 |       -4.455 | W2:ARI  W3:SF  W4:CHI  W5:DET  W6:LA |
|     21 | WAS    |         61.6 |    34.9 |        0.1 |        13.66 |      0.1 |        0.006 |   -5.505  |       -4.455 | W2:WAS  W3:SF  W4:CHI  W5:DET  W6:LA |
|     22 | MIN    |         58.2 |    33.9 |        0.1 |        13.66 |      0.1 |        0.08  |   -5.5628 |       -4.455 | W2:MIN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     23 | PIT    |         56   |    32.1 |        0.1 |        13.66 |      0.1 |        0.034 |   -5.6006 |       -4.455 | W2:PIT  W3:SF  W4:CHI  W5:DET  W6:LA |
|     24 | LV     |         49.1 |    28.2 |        0.1 |        13.66 |      0.1 |        0     |   -5.7184 |       -4.455 | W2:LV  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     25 | TEN    |         43.7 |    25.7 |        0   |         0    |      0   |        0     |   -5.8103 |       -4.455 | W2:TEN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     26 | IND    |         43.2 |    28.5 |        0   |         0    |      0   |        0.042 |   -5.8188 |       -4.553 | W2:IND  W3:SF  W4:CHI  W5:DET  W6:NE |
|     27 | DET    |         43   |    31.8 |        0.1 |        13.66 |      0.1 |        0.314 |   -5.823  |       -4.569 | W2:DET  W3:SF  W4:CHI  W5:NE  W6:LA  |
|     28 | NYG    |         42   |    26.2 |        0.1 |        13.66 |      0.1 |        0.134 |   -5.8389 |       -4.455 | W2:NYG  W3:SF  W4:CHI  W5:DET  W6:LA |
|     29 | CLE    |         36.9 |    22.9 |        0   |         0    |      0   |        0     |   -5.9266 |       -4.455 | W2:CLE  W3:SF  W4:CHI  W5:DET  W6:LA |
|     30 | NO     |         36.1 |    22.7 |        0   |         0    |      0   |        0.013 |   -5.9404 |       -4.455 | W2:NO  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     31 | MIA    |          0   |    12.2 |        0   |         0    |      0   |        0     |   -6.5549 |       -4.455 | W2:MIA  W3:SF  W4:CHI  W5:DET  W6:LA |


## Charts
- `week_02_win_probability.png`
- `week_02_pick_distribution.png`
- `week_02_best_picks.png`
- `week_02_ranked_table.png`