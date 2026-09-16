# Survivor — Week 2 (2026) — Matt (Mattymo)

- Win-prob sources: **odds-api:32**
- Public pick %: **survivorgrid** survivorgrid ok (https://www.survivorgrid.com/)
- Opponents tracked: **0** (0 alive)
- Teams already used by you: **JAX**

## ✅ Recommended Week 2 pick: **TB (Tampa Bay Buccaneers)**
- Market win probability: **77.1%**
- Public pick %: 29.1%  |  expected dupes in your pool: 0.00 (0.0% of those alive)
- EV(path) = -4.7236   EV(myopic) = -0.2628
- Implied season plan if you take TB now:
  `W2:TB  W3:SF  W4:CHI  W5:DET  W6:LA  W7:DEN  W8:DAL  W9:SEA  W10:IND  W11:KC  W12:CIN  W13:PHI  W14:LAC  W15:GB  W16:BAL  W17:BUF  W18:NE`

> ℹ️ The pure win-probability path optimiser would open with **SF** this week; **TB** ranks #1 once the future-value guard and consensus penalty are applied. Both are shown below — adjust `future_value_penalty` / `consensus_penalty` in config.py to taste.

## Unconditional optimal season plan (pure Π win-prob)
`W2:SF  W3:KC  W4:CHI  W5:NE  W6:LA  W7:DEN  W8:DAL  W9:SEA  W10:IND  W11:LAC  W12:CIN  W13:PHI  W14:DET  W15:GB  W16:BAL  W17:BUF  W18:HOU`
- Expected weeks survived (Π win-prob): **0.009**  (sum log wp = -4.658)

## Ranked available teams
|   rank | team   |   pick_score |   win_% |   public_% |   pool_dupes |   pool_% |   future_val |   EV_path |   rest_logwp | implied_next_picks                   |
|-------:|:-------|-------------:|--------:|-----------:|-------------:|---------:|-------------:|----------:|-------------:|:-------------------------------------|
|      1 | TB     |        100   |    77.1 |       29.1 |            0 |        0 |        0.008 |   -4.7236 |       -4.461 | W2:TB  W3:SF  W4:CHI  W5:DET  W6:LA  |
|      2 | SF     |         97.8 |    87.4 |       29.4 |            0 |        0 |        0.302 |   -4.7632 |       -4.523 | W2:SF  W3:KC  W4:CHI  W5:NE  W6:LA   |
|      3 | LAC    |         93.2 |    71.5 |        3   |            0 |        0 |        0.109 |   -4.8465 |       -4.476 | W2:LAC  W3:SF  W4:CHI  W5:NE  W6:LA  |
|      4 | PHI    |         92.5 |    74.3 |       12.4 |            0 |        0 |        0.155 |   -4.8582 |       -4.507 | W2:PHI  W3:SF  W4:CHI  W5:DET  W6:LA |
|      5 | BAL    |         88.8 |    77.3 |        7   |            0 |        0 |        0.264 |   -4.9252 |       -4.575 | W2:BAL  W3:SF  W4:CHI  W5:NE  W6:LA  |
|      6 | CHI    |         87.2 |    67.4 |        1.5 |            0 |        0 |        0.155 |   -4.9543 |       -4.512 | W2:CHI  W3:SF  W4:MIN  W5:DET  W6:LA |
|      7 | KC     |         85.4 |    71.5 |        2.4 |            0 |        0 |        0.396 |   -4.9867 |       -4.517 | W2:KC  W3:SF  W4:CHI  W5:NE  W6:LA   |
|      8 | CAR    |         83.6 |    57.1 |        2.7 |            0 |        0 |        0     |   -5.019  |       -4.461 | W2:CAR  W3:SF  W4:CHI  W5:DET  W6:LA |
|      9 | HOU    |         83.1 |    57.6 |        0.4 |            0 |        0 |        0.069 |   -5.0293 |       -4.461 | W2:HOU  W3:SF  W4:CHI  W5:DET  W6:LA |
|     10 | NE     |         80.9 |    67.9 |        0.9 |            0 |        0 |        0.325 |   -5.0684 |       -4.575 | W2:NE  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     11 | DAL    |         80.1 |    65.5 |        1.1 |            0 |        0 |        0.148 |   -5.0826 |       -4.614 | W2:DAL  W3:SF  W4:CHI  W5:DET  W6:LA |
|     12 | LA     |         79.3 |    74.7 |        1.5 |            0 |        0 |        0.4   |   -5.0977 |       -4.673 | W2:LA  W3:SF  W4:CHI  W5:DET  W6:NE  |
|     13 | DEN    |         77.3 |    58.5 |        0.2 |            0 |        0 |        0.186 |   -5.1328 |       -4.539 | W2:DEN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     14 | SEA    |         77.1 |    64.1 |        1.8 |            0 |        0 |        0.262 |   -5.1364 |       -4.604 | W2:SEA  W3:SF  W4:CHI  W5:NE  W6:LA  |
|     15 | BUF    |         76.2 |    67.1 |        1.5 |            0 |        0 |        0.303 |   -5.1533 |       -4.653 | W2:BUF  W3:SF  W4:CHI  W5:DET  W6:LA |
|     16 | GB     |         71.6 |    61.7 |        3.8 |            0 |        0 |        0.216 |   -5.236  |       -4.678 | W2:GB  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     17 | ATL    |         67.9 |    42.9 |        0.2 |            0 |        0 |        0     |   -5.3022 |       -4.461 | W2:ATL  W3:SF  W4:CHI  W5:DET  W6:LA |
|     18 | NYJ    |         61.7 |    38.3 |        0.1 |            0 |        0 |        0     |   -5.4154 |       -4.461 | W2:NYJ  W3:SF  W4:CHI  W5:DET  W6:LA |
|     19 | CIN    |         59.6 |    42.4 |        0.2 |            0 |        0 |        0.153 |   -5.4519 |       -4.545 | W2:CIN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     20 | ARI    |         58.1 |    35.9 |        0.1 |            0 |        0 |        0     |   -5.4805 |       -4.461 | W2:ARI  W3:SF  W4:CHI  W5:DET  W6:LA |
|     21 | WAS    |         55.7 |    34.5 |        0.1 |            0 |        0 |        0.006 |   -5.5222 |       -4.461 | W2:WAS  W3:SF  W4:CHI  W5:DET  W6:LA |
|     22 | PIT    |         51.1 |    32.1 |        0.1 |            0 |        0 |        0.034 |   -5.6057 |       -4.461 | W2:PIT  W3:SF  W4:CHI  W5:DET  W6:LA |
|     23 | MIN    |         51.1 |    32.6 |        0.1 |            0 |        0 |        0.08  |   -5.6064 |       -4.461 | W2:MIN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     24 | LV     |         45.2 |    28.5 |        0.1 |            0 |        0 |        0     |   -5.7118 |       -4.461 | W2:LV  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     25 | DET    |         40.9 |    32.9 |        0.1 |            0 |        0 |        0.314 |   -5.7909 |       -4.575 | W2:DET  W3:SF  W4:CHI  W5:NE  W6:LA  |
|     26 | TEN    |         39.5 |    25.7 |        0   |            0 |        0 |        0     |   -5.8159 |       -4.461 | W2:TEN  W3:SF  W4:CHI  W5:DET  W6:LA |
|     27 | IND    |         39   |    28.5 |        0   |            0 |        0 |        0.042 |   -5.8244 |       -4.559 | W2:IND  W3:SF  W4:CHI  W5:DET  W6:NE |
|     28 | NYG    |         36   |    25.3 |        0.1 |            0 |        0 |        0.13  |   -5.8782 |       -4.461 | W2:NYG  W3:SF  W4:CHI  W5:DET  W6:LA |
|     29 | CLE    |         33   |    22.9 |        0   |            0 |        0 |        0     |   -5.9322 |       -4.461 | W2:CLE  W3:SF  W4:CHI  W5:DET  W6:LA |
|     30 | NO     |         32.3 |    22.7 |        0   |            0 |        0 |        0.013 |   -5.9459 |       -4.461 | W2:NO  W3:SF  W4:CHI  W5:DET  W6:LA  |
|     31 | MIA    |          0   |    12.6 |        0   |            0 |        0 |        0     |   -6.5283 |       -4.461 | W2:MIA  W3:SF  W4:CHI  W5:DET  W6:LA |


## Charts
- `week_02_win_probability.png`
- `week_02_pick_distribution.png`
- `week_02_best_picks.png`
- `week_02_ranked_table.png`