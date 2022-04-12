# baseball-rollover-minutes

Do you ever wonder what it would be like if you could "bank" leftover points when you win a baseball game? Well, the Cleveland Tech Slack did and I decided to see what it would do.

If you'd like to screw around with this, create a `cache` directory, create a `season_data` directory, create a venv, install the requirements.txt and go for it. Run the `fetch_scores.py` to grab the 2021 records from baseball-reference, then run `calculate_rollovers.py` to get the details on how the season would have changed if you could bank the points.

This is very unprofessional code, thrown together for play-around time. Don't take any advice or patterns from this, please. Even publishing this borders on malpractice.
