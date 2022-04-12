# baseball-rollover-minutes

Do you ever wonder what it would be like if you could "bank" leftover points when you win a baseball game? Well, the Cleveland Tech Slack did and I decided to see what it would do.

If you'd like to screw around with this, create a `cache` directory, create a `season_data` directory, create a venv, install the requirements.txt and go for it. Run the `fetch_scores.py` to grab the 2021 records from baseball-reference, then run `calculate_rollovers.py` to get the details on how the season would have changed if you could bank the points.

This is very unprofessional code, thrown together for play-around time. Don't take any advice or patterns from this, please. Even publishing this borders on malpractice.

Example output:

```Under the old rules of baseball, these are the 2021 W/L records
Rank	Team                     	Wins	Losses	PCT
---------------------------------------------------------------------------------------------------------
1	     San Francisco Giants	107	55	0.66
2	      Los Angeles Dodgers	106	56	0.654
3	           Tampa Bay Rays	100	62	0.617
4	        Milwaukee Brewers	95	67	0.586
5	           Houston Astros	95	67	0.586
6	        Chicago White Sox	93	69	0.574
7	         New York Yankees	92	70	0.568
8	           Boston Red Sox	92	70	0.568
9	        Toronto Blue Jays	91	71	0.562
10	      St. Louis Cardinals	90	72	0.556
11	         Seattle Mariners	90	72	0.556
12	           Atlanta Braves	88	73	0.547
13	        Oakland Athletics	86	76	0.531
14	          Cincinnati Reds	83	79	0.512
15	    Philadelphia Phillies	82	80	0.506
16	        Cleveland Indians	80	82	0.494
17	         San Diego Padres	79	83	0.488
18	       Los Angeles Angels	77	85	0.475
19	           Detroit Tigers	77	85	0.475
20	            New York Mets	77	85	0.475
21	         Colorado Rockies	74	87	0.46
22	       Kansas City Royals	74	88	0.457
23	          Minnesota Twins	73	89	0.451
24	             Chicago Cubs	71	91	0.438
25	            Miami Marlins	67	95	0.414
26	     Washington Nationals	65	97	0.401
27	       Pittsburgh Pirates	61	101	0.377
28	            Texas Rangers	60	102	0.37
29	          Arizona D'Backs	52	110	0.321
30	        Baltimore Orioles	52	110	0.321



Under the new t-mobile rules of baseball, these are the 2021 W/L records
Rank	Team                     	Wins	Losses	PCT	Points Left in the Bank
---------------------------------------------------------------------------------------------------------
1	      Los Angeles Dodgers	109	53	0.673	19
2	          Cincinnati Reds	106	56	0.654	0
3	           Tampa Bay Rays	104	58	0.642	19
4	        Toronto Blue Jays	103	59	0.636	16
5	           Houston Astros	102	60	0.63	11
6	           Boston Red Sox	101	61	0.623	0
7	        Milwaukee Brewers	99	63	0.611	0
8	           Atlanta Braves	91	70	0.565	0
9	        Oakland Athletics	90	72	0.556	0
10	        Chicago White Sox	88	74	0.543	4
11	            New York Mets	86	76	0.531	3
12	        Cleveland Indians	85	77	0.525	0
13	         San Diego Padres	84	78	0.519	0
14	         Colorado Rockies	82	79	0.509	0
15	     San Francisco Giants	82	80	0.506	12
16	      St. Louis Cardinals	81	81	0.5	5
17	     Washington Nationals	77	85	0.475	2
18	    Philadelphia Phillies	76	86	0.469	0
19	       Los Angeles Angels	75	87	0.463	0
20	           Detroit Tigers	73	89	0.451	0
21	         New York Yankees	73	89	0.451	0
22	          Minnesota Twins	71	91	0.438	0
23	         Seattle Mariners	69	93	0.426	4
24	       Pittsburgh Pirates	66	96	0.407	7
25	          Arizona D'Backs	65	97	0.401	4
26	             Chicago Cubs	62	100	0.383	0
27	       Kansas City Royals	61	101	0.377	1
28	            Miami Marlins	61	101	0.377	8
29	        Baltimore Orioles	56	106	0.346	0
30	            Texas Rangers	51	111	0.315	0
```
