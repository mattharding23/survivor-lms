# Survivor — Week 2 (2026) — Wil (WilboBaggins)

- Win-prob sources: **survivorgrid-w%:32**
- Public pick %: **survivorgrid** survivorgrid ok (https://www.survivorgrid.com/)
- Opponents tracked: **0** (0 alive)
- Teams already used by you: **JAX**

## ✅ Recommended Week 2 pick: **TB (Tampa Bay Buccaneers)**
- Market win probability: **77.3%**
- Public pick %: 29.1%  |  expected dupes in your pool: 0.00 (0.0% of those alive)
- EV(path) = -4.7211   EV(myopic) = -0.2603
- Implied season plan if you take TB now:
  `W2:TB  W3:SF  W4:CHI  W5:DET  W6:LA  W7:DEN  W8:DAL  W9:SEA  W10:IND  W11:KC  W12:CIN  W13:PHI  W14:LAC  W15:GB  W16:BAL  W17:BUF  W18:NE`

> ℹ️ The pure win-probability path optimiser would open with **SF** this week; **TB** ranks #1 once the future-value guard and consensus penalty are applied. Both are shown below — adjust `future_value_penalty` / `consensus_penalty` in config.py to taste.

## Unconditional optimal season plan (pure Π win-prob)
`W2:SF  W3:KC  W4:CHI  W5:NE  W6:LA  W7:DEN  W8:DAL  W9:SEA  W10:IND  W11:LAC  W12:CIN  W13:PHI  W14:DET  W15:GB  W16:BAL  W17:BUF  W18:HOU`
- Expected weeks survived (Π win-prob): **0.009**  (sum log wp = -4.660)

## Ranked available teams
|   rank | team   |   pick_score |   win_% |   public_% |   pool_dupes |   pool_% |   future_val |   EV_path |   rest_logwp | implied_next_picks                   |
|-------:|:-------|-------------:|--------:|-----------:|-------------:|---------:|-------------:|----------:|-------------:|:-------------------------------------|
|      1 | TB     |        100   |    77.3 |       29.1 |            0 |        0 |        0.008 |   -4.7211 |       -4.461 | W2:TB  W3:SF  W4:CHI  W5:DET  W6:LA  |
|      2 | SF     |         97.5 |    87.2 |       29.5 |            0 |        0 |        0.302 |   -4.7652 |       -4.523 | W2:SF  W3:KC  W4:CHI  W5:NE  W6:LA   |
|      3 | LAC    |         93.2 |    71.7 |        3   |            0 |        0 |        0.109 |   -4.8433 |       -4.476 | W2:LAC  W3:SF  W4:CHI  W5:NE  W6:LA  |
|      4 | PHI    |         92.2 |    74.1 |       12.3 |            0 |        0 |        0.155 |   -4.8608 |       -4.507 | W2:PHI  W3:SF  W4:CHI  W5:DET  W6:LA |
|      5 | BAL    |         88.6 |    77.3 |        7   |            0 |        0 |        0.264 |   -4.9254 |       -4.575 | W2:BAL  W3:SF  W4:CHI  W5:NE  W6:LA  |
|      6 | CHI    |         87.6 |    68.1 |        1.5 |            0 |        0 |        0.155 |   -4.9442 |       -4.512 | W2:CHI  W3:SF  W4:MIN  W5:DET  W6:LA |
|      7 | KC     |         85.5 |    71.8 |        2.3 |            0 |        0 |        0.396 |   -4.982  |       -4.517 | W2:KC  W3:SF  W4:CHI  W5:NE  W6:LA   |
|      8 | HOU    |         82.8 |    57.6 |        0.4 |            0 |        0 |        0.069 |   -5.0299 |       -4.461 | W2:HOU  W3:SF  W4:CHI  W5:DET  W6:LA |
|      9 | CAR    |         82.7 |    56.4 |        2.7 |            0 |        0 |        0     |   -5.0316 |       -4.461 | W2:CAR  W3:SF  W4:CHI  W5:DET  W6:LA |
|     10 | NE     |         80.6 |    67.9 |        0.9 |            0 |        0 |        0.325 |   -5.0688 |       -4.575 | W2:NE  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     11 | DAL    |         79.6 |    65.2 |        1.1 |            0 |        0 |        0.148 |   -5.0869 |       -4.614 | W2:DAL  W3:SF  W4:CHI  W5:DET  W6:LA |
|     12 | LA     |         78.7 |    74.3 |        1.5 |            0 |        0 |        0.4   |   -5.1034 |       -4.673 | W2:LA  W3:SF  W4:CHI  W5:DET  W6:NE  |
|     13 | SEA    |         77.1 |    64.4 |        1.8 |            0 |        0 |        0.262 |   -5.1316 |       -4.604 | W2:SEA  W3:SF  W4:CHI  W5:NE  W6:LA  |
|     14 | DEN    |         76   |    57.4 |        0.2 |            0 |        0 |        0.186 |   -5.1517 |       -4.539 | W2:DEN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     15 | BUF    |         76   |    67   |        1.5 |            0 |        0 |        0.297 |   -5.1521 |       -4.653 | W2:BUF  W3:SF  W4:CHI  W5:DET  W6:LA |
|     16 | GB     |         72.1 |    62.6 |        3.8 |            0 |        0 |        0.216 |   -5.2211 |       -4.678 | W2:GB  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     17 | ATL    |         68.5 |    43.6 |        0.2 |            0 |        0 |        0     |   -5.2857 |       -4.461 | W2:ATL  W3:SF  W4:CHI  W5:DET  W6:LA |
|     18 | NYJ    |         59.9 |    37.4 |        0.1 |            0 |        0 |        0     |   -5.4397 |       -4.461 | W2:NYJ  W3:SF  W4:CHI  W5:DET  W6:LA |
|     19 | CIN    |         59.3 |    42.4 |        0.2 |            0 |        0 |        0.153 |   -5.4509 |       -4.545 | W2:CIN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     20 | ARI    |         57.2 |    35.6 |        0.1 |            0 |        0 |        0     |   -5.4892 |       -4.461 | W2:ARI  W3:SF  W4:CHI  W5:DET  W6:LA |
|     21 | WAS    |         55.8 |    34.8 |        0.1 |            0 |        0 |        0.006 |   -5.5141 |       -4.461 | W2:WAS  W3:SF  W4:CHI  W5:DET  W6:LA |
|     22 | PIT    |         50.7 |    32.1 |        0.1 |            0 |        0 |        0.034 |   -5.6049 |       -4.461 | W2:PIT  W3:SF  W4:CHI  W5:DET  W6:LA |
|     23 | MIN    |         49.5 |    31.9 |        0.1 |            0 |        0 |        0.08  |   -5.6276 |       -4.461 | W2:MIN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     24 | LV     |         44.3 |    28.3 |        0.1 |            0 |        0 |        0     |   -5.7196 |       -4.461 | W2:LV  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     25 | DET    |         40.4 |    33   |        0.1 |            0 |        0 |        0.314 |   -5.7893 |       -4.575 | W2:DET  W3:SF  W4:CHI  W5:NE  W6:LA  |
|     26 | TEN    |         39.4 |    25.9 |        0   |            0 |        0 |        0     |   -5.8084 |       -4.461 | W2:TEN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     27 | IND    |         37.9 |    28.2 |        0   |            0 |        0 |        0.042 |   -5.8358 |       -4.559 | W2:IND  W3:SF  W4:CHI  W5:DET  W6:NE |
|     28 | NYG    |         36.4 |    25.7 |        0.1 |            0 |        0 |        0.13  |   -5.8617 |       -4.461 | W2:NYG  W3:SF  W4:CHI  W5:DET  W6:LA |
|     29 | CLE    |         32   |    22.7 |        0   |            0 |        0 |        0     |   -5.9407 |       -4.461 | W2:CLE  W3:SF  W4:CHI  W5:DET  W6:LA |
|     30 | NO     |         31.8 |    22.7 |        0   |            0 |        0 |        0.013 |   -5.9452 |       -4.461 | W2:NO  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     31 | MIA    |          0   |    12.8 |        0   |            0 |        0 |        0     |   -6.5148 |       -4.461 | W2:MIA  W3:SF  W4:CHI  W5:DET  W6:LA |


## Charts
- `week_02_win_probability.png`
- `week_02_pick_distribution.png`
- `week_02_best_picks.png`
- `week_02_ranked_table.png`