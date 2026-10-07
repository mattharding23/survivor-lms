# Survivor — Week 5 (2026) — Gunner

- Win-prob sources: **odds-api:30**
- Public pick %: **survivorgrid** survivorgrid ok (https://www.survivorgrid.com/)
- Opponents tracked: **0** (0 alive)
- Teams already used by you: **KC, LV, MIN, SF**

## ✅ Recommended Week 5 pick: **ATL (Atlanta Falcons)**
- Market win probability: **63.3%**
- Public pick %: 0.3%  |  expected dupes in your pool: 41.05 (0.3% of those alive)
- EV(path) = -3.7860   EV(myopic) = -0.4506
- Implied season plan if you take ATL now:
  `W5:ATL  W6:LA  W7:HOU  W8:CIN  W9:SEA  W10:IND  W11:BUF  W12:JAX  W13:DEN  W14:DET  W15:GB  W16:BAL  W17:DAL  W18:NE`

> ℹ️ The pure win-probability path optimiser would open with **DAL** this week; **ATL** ranks #1 once the future-value guard and consensus penalty are applied. Both are shown below — adjust `future_value_penalty` / `consensus_penalty` in config.py to taste.

## Unconditional optimal season plan (pure Π win-prob)
`W5:DAL  W6:LA  W7:HOU  W8:CIN  W9:SEA  W10:IND  W11:BUF  W12:JAX  W13:DEN  W14:DET  W15:GB  W16:BAL  W17:PIT  W18:NE`
- Expected weeks survived (Π win-prob): **0.025**  (sum log wp = -3.701)

## Ranked available teams
|   rank | team   |   pick_score |   win_% |   public_% |   pool_dupes |   pool_% |   future_val |   EV_path |   rest_logwp | implied_next_picks                    |
|-------:|:-------|-------------:|--------:|-----------:|-------------:|---------:|-------------:|----------:|-------------:|:--------------------------------------|
|      1 | ATL    |        100   |    63.3 |        0.3 |        41.05 |      0.3 |        0     |   -3.786  |       -3.335 | W5:ATL  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|      2 | WAS    |         99.5 |    62.9 |        0.1 |        13.68 |      0.1 |        0     |   -3.7909 |       -3.335 | W5:WAS  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|      3 | HOU    |         92.2 |    76.3 |       12.8 |      1751.55 |     12.8 |        0.142 |   -3.8699 |       -3.48  | W5:HOU  W6:LA  W7:NYJ  W8:CIN  W9:SEA |
|      4 | PIT    |         89.7 |    57.6 |        0.3 |        41.05 |      0.3 |        0.048 |   -3.897  |       -3.335 | W5:PIT  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|      5 | NYJ    |         86.1 |    54.5 |        0.1 |        13.68 |      0.1 |        0     |   -3.9356 |       -3.335 | W5:NYJ  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|      6 | DET    |         85.5 |    69.1 |        3.2 |       437.89 |      3.2 |        0.273 |   -3.9424 |       -3.463 | W5:DET  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|      7 | CHI    |         82.8 |    54.3 |        0.4 |        54.74 |      0.4 |        0.084 |   -3.9709 |       -3.335 | W5:CHI  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|      8 | CIN    |         78.3 |    73.5 |       26.7 |      3653.63 |     26.7 |        0.219 |   -4.0194 |       -3.488 | W5:CIN  W6:LA  W7:HOU  W8:PIT  W9:SEA |
|      9 | DAL    |         77.4 |    78.3 |       45.4 |      6212.54 |     45.4 |        0.225 |   -4.0293 |       -3.457 | W5:DAL  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     10 | JAX    |         76.2 |    75.5 |        2   |       273.68 |      2   |        0.31  |   -4.0419 |       -3.648 | W5:JAX  W6:LA  W7:HOU  W8:PIT  W9:SEA |
|     11 | NE     |         75.9 |    62.9 |        1.8 |       246.31 |      1.8 |        0.237 |   -4.045  |       -3.494 | W5:NE  W6:LA  W7:NYJ  W8:CIN  W9:SEA  |
|     12 | SEA    |         69.9 |    61.1 |        0.1 |        13.68 |      0.1 |        0.277 |   -4.1096 |       -3.528 | W5:SEA  W6:LA  W7:HOU  W8:CIN  W9:PHI |
|     13 | NO     |         68.9 |    45.3 |        0.1 |        13.68 |      0.1 |        0     |   -4.1208 |       -3.335 | W5:NO  W6:LA  W7:HOU  W8:CIN  W9:SEA  |
|     14 | CLE    |         68   |    45.5 |        1.9 |       260    |      1.9 |        0     |   -4.1299 |       -3.335 | W5:CLE  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     15 | DEN    |         65.3 |    62.2 |        1.6 |       218.94 |      1.6 |        0.201 |   -4.1598 |       -3.613 | W5:DEN  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     16 | LA     |         52.1 |    59.9 |        0.1 |        13.68 |      0.1 |        0.553 |   -4.3014 |       -3.604 | W5:LA  W6:NE  W7:NYJ  W8:CIN  W9:SEA  |
|     17 | LAC    |         51.1 |    37.8 |        0   |         0    |      0   |        0.022 |   -4.3118 |       -3.335 | W5:LAC  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     18 | NYG    |         49.9 |    37.1 |        0.5 |        68.42 |      0.5 |        0     |   -4.3249 |       -3.335 | W5:NYG  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     19 | GB     |         42.9 |    45.7 |        0.1 |        13.68 |      0.1 |        0.057 |   -4.4007 |       -3.604 | W5:GB  W6:LA  W7:HOU  W8:CIN  W9:SEA  |
|     20 | BAL    |         41.4 |    36.7 |        0.7 |        95.79 |      0.7 |        0.059 |   -4.4163 |       -3.394 | W5:BAL  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     21 | IND    |         38.1 |    42.4 |        0.1 |        13.68 |      0.1 |        0.175 |   -4.4524 |       -3.538 | W5:IND  W6:NE  W7:NYJ  W8:CIN  W9:SEA |
|     22 | ARI    |         33.2 |    30.9 |        0   |         0    |      0   |        0     |   -4.5046 |       -3.335 | W5:ARI  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     23 | BUF    |         23.7 |    40.1 |        0.1 |        13.68 |      0.1 |        0.364 |   -4.6069 |       -3.57  | W5:BUF  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     24 | MIA    |         18.8 |    26.5 |        0   |         0    |      0   |        0     |   -4.6602 |       -3.335 | W5:MIA  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     25 | PHI    |         10.3 |    24.5 |        0.1 |        13.68 |      0.1 |        0.04  |   -4.7518 |       -3.335 | W5:PHI  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     26 | TEN    |          8.3 |    23.7 |        0   |         0    |      0   |        0     |   -4.7725 |       -3.335 | W5:TEN  W6:LA  W7:HOU  W8:CIN  W9:SEA |
|     27 | TB     |          0   |    21.7 |        0   |         0    |      0   |        0     |   -4.8622 |       -3.335 | W5:TB  W6:LA  W7:HOU  W8:CIN  W9:SEA  |


## Charts
- `week_05_win_probability.png`
- `week_05_pick_distribution.png`
- `week_05_best_picks.png`
- `week_05_ranked_table.png`