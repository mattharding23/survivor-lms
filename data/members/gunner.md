# Survivor — Week 6 (2026) — Gunner

- Win-prob sources: **odds-api:28**
- Public pick %: **survivorgrid** survivorgrid ok (https://www.survivorgrid.com/)
- Opponents tracked: **0** (0 alive)
- Teams already used by you: **CIN, KC, LV, MIN, SF**

## ✅ Recommended Week 6 pick: **IND (Indianapolis Colts)**
- Market win probability: **73.5%**
- Public pick %: 17.6%  |  expected dupes in your pool: 2408.74 (17.6% of those alive)
- EV(path) = -3.4675   EV(myopic) = -0.4341
- Implied season plan if you take IND now:
  `W6:IND  W7:HOU  W8:PIT  W9:SEA  W10:LA  W11:BUF  W12:JAX  W13:DEN  W14:DET  W15:GB  W16:BAL  W17:DAL  W18:NE`

> ℹ️ The pure win-probability path optimiser would open with **LA** this week; **IND** ranks #1 once the future-value guard and consensus penalty are applied. Both are shown below — adjust `future_value_penalty` / `consensus_penalty` in config.py to taste.

## Unconditional optimal season plan (pure Π win-prob)
`W6:LA  W7:HOU  W8:PIT  W9:SEA  W10:IND  W11:BUF  W12:JAX  W13:DEN  W14:DET  W15:GB  W16:BAL  W17:DAL  W18:NE`
- Expected weeks survived (Π win-prob): **0.039**  (sum log wp = -3.254)

## Ranked available teams
|   rank | team   |   pick_score |   win_% |   public_% |   pool_dupes |   pool_% |   future_val |   EV_path |   rest_logwp | implied_next_picks                     |
|-------:|:-------|-------------:|--------:|-----------:|-------------:|---------:|-------------:|----------:|-------------:|:---------------------------------------|
|      1 | IND    |        100   |    73.5 |       17.6 |      2408.74 |     17.6 |        0.085 |   -3.4675 |       -3.033 | W6:IND  W7:HOU  W8:PIT  W9:SEA  W10:LA |
|      2 | NE     |         91.8 |    73.8 |       19.4 |      2655.08 |     19.4 |        0.131 |   -3.591  |       -3.135 | W6:NE  W7:LA  W8:PIT  W9:SEA  W10:IND  |
|      3 | CHI    |         91.3 |    57.1 |        0.1 |        13.69 |      0.1 |        0.064 |   -3.5988 |       -3.025 | W6:CHI  W7:HOU  W8:LA  W9:SEA  W10:IND |
|      4 | PIT    |         90.5 |    56.8 |        1.3 |       177.92 |      1.3 |        0.052 |   -3.61   |       -3.025 | W6:PIT  W7:HOU  W8:LA  W9:SEA  W10:IND |
|      5 | BAL    |         90.1 |    68.7 |        0.9 |       123.17 |      0.9 |        0.174 |   -3.6169 |       -3.185 | W6:BAL  W7:HOU  W8:LA  W9:SEA  W10:IND |
|      6 | LA     |         90   |    85.7 |       38.4 |      5255.42 |     38.4 |        0.438 |   -3.618  |       -3.1   | W6:LA  W7:HOU  W8:PIT  W9:SEA  W10:IND |
|      7 | NO     |         85.1 |    51.1 |        0.1 |        13.69 |      0.1 |        0.006 |   -3.691  |       -3.025 | W6:NO  W7:HOU  W8:LA  W9:SEA  W10:IND  |
|      8 | CAR    |         83.8 |    50   |        0.1 |        13.69 |      0.1 |        0     |   -3.7106 |       -3.025 | W6:CAR  W7:HOU  W8:LA  W9:SEA  W10:IND |
|      9 | PHI    |         82.8 |    50   |        0.2 |        27.37 |      0.2 |        0.043 |   -3.7264 |       -3.025 | W6:PHI  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     10 | NYG    |         82   |    48.9 |        0.9 |       123.17 |      0.9 |        0     |   -3.7387 |       -3.025 | W6:NYG  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     11 | BUF    |         78.2 |    67.1 |        3   |       410.58 |      3   |        0.355 |   -3.7945 |       -3.259 | W6:BUF  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     12 | TB     |         74.1 |    43.2 |        0   |         0    |      0   |        0     |   -3.856  |       -3.025 | W6:TB  W7:HOU  W8:LA  W9:SEA  W10:IND  |
|     13 | ATL    |         73.5 |    42.9 |        0.1 |        13.69 |      0.1 |        0     |   -3.8652 |       -3.025 | W6:ATL  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     14 | SEA    |         72.2 |    56.6 |        0.4 |        54.74 |      0.4 |        0.301 |   -3.8857 |       -3.217 | W6:SEA  W7:HOU  W8:LA  W9:PHI  W10:IND |
|     15 | GB     |         70.7 |    53.2 |        0.3 |        41.06 |      0.3 |        0.073 |   -3.9083 |       -3.259 | W6:GB  W7:HOU  W8:PIT  W9:SEA  W10:IND |
|     16 | JAX    |         66.4 |    57.1 |        3   |       410.58 |      3   |        0.375 |   -3.972  |       -3.267 | W6:JAX  W7:HOU  W8:PIT  W9:SEA  W10:LA |
|     17 | DAL    |         66.1 |    46.8 |        0   |         0    |      0   |        0.224 |   -3.9772 |       -3.146 | W6:DAL  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     18 | HOU    |         61.2 |    42.9 |        0   |         0    |      0   |        0.217 |   -4.0501 |       -3.135 | W6:HOU  W7:LA  W8:PIT  W9:SEA  W10:IND |
|     19 | CLE    |         52.5 |    31.3 |        0   |         0    |      0   |        0     |   -4.1807 |       -3.025 | W6:CLE  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     20 | DEN    |         49.4 |    43.4 |        0   |         0    |      0   |        0.247 |   -4.2284 |       -3.315 | W6:DEN  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     21 | TEN    |         41.3 |    26.5 |        0   |         0    |      0   |        0     |   -4.3492 |       -3.025 | W6:TEN  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     22 | NYJ    |         39.8 |    26.2 |        0   |         0    |      0   |        0.034 |   -4.372  |       -3.025 | W6:NYJ  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     23 | WAS    |         34.4 |    23.9 |        0   |         0    |      0   |        0     |   -4.4538 |       -3.025 | W6:WAS  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     24 | LAC    |         29.4 |    22.2 |        0   |         0    |      0   |        0     |   -4.5283 |       -3.025 | W6:LAC  W7:HOU  W8:LA  W9:SEA  W10:IND |
|     25 | ARI    |          0   |    14.3 |        0   |         0    |      0   |        0     |   -4.9701 |       -3.025 | W6:ARI  W7:HOU  W8:LA  W9:SEA  W10:IND |


## Charts
- `week_06_win_probability.png`
- `week_06_pick_distribution.png`
- `week_06_best_picks.png`
- `week_06_ranked_table.png`