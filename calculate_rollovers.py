import os
import csv

season_to_get = '2021'
season_data_path = f'season_data{os.path.sep}' 
season_data_file_path = f'{season_data_path}{season_to_get}.csv'

ALLOW_SAVING_POINTS_IN_A_LOST_CAUSE = True
old_wins_losses = {}
new_wins_losses = {}
points_bank = {}


def sort_the_wins(dic):
    
    records = []
    for team in dic:
        records.append([
                team.rjust(25), 
                dic[team]["wins"], 
                dic[team]["losses"], 
                round(dic[team]["wins"] / (dic[team]["wins"] + dic[team]["losses"]), 3)
            ])
            
    records.sort(key = lambda x: x[1], reverse=True)
    
    for idx, record in enumerate(records):
        record.insert(0, str(idx + 1))
        records[idx] = record
    
    return records

def get_or_create_team_points_bank(team):
    if team in points_bank:
        team_score = points_bank[team]
    else:
        team_score = 0
    
    return team_score

    
def add_to_points_bank(team, points):

    team_score = get_or_create_team_points_bank(team)
    
    team_score = team_score + points
    
    points_bank[team] = team_score

    
def withdraw_from_points_bank(team, proposed_amount):
    
    team_score = get_or_create_team_points_bank(team)
    
    if team_score >= proposed_amount:
        team_score = team_score - proposed_amount
        points_bank[team] = team_score
        return proposed_amount
    else:
        if ALLOW_SAVING_POINTS_IN_A_LOST_CAUSE:
            return 0
        else:
            points_bank[team] = 0
            return team_score
 

def get_or_create_team_record(dic, team):
    
    if team in dic:
        return dic[team]
    else:
        dic[team] = {
            'wins':0,
            'losses':0
        }
        return dic[team]
        
def add_team_win(dic, team):
    
    team_record = get_or_create_team_record(dic, team)
    team_record["wins"] = team_record["wins"] + 1
    
    dic[team] = team_record

def add_team_loss(dic, team):
    
    team_record = get_or_create_team_record(dic, team)
    team_record["losses"] = team_record["losses"] + 1
    
    dic[team] = team_record
    
with open(season_data_file_path, 'r') as infile:
    gamereader = csv.reader(infile, delimiter=',', quotechar='"')
    
    for row in gamereader:
        
        away_team = row[1]
        away_team_score = int(row[2])
        home_team = row[3]
        home_team_score = int(row[4])
    
        # Old-fashioned, boring baseball
        if home_team_score > away_team_score:
            add_team_win(old_wins_losses, home_team)
            add_team_loss(old_wins_losses, away_team)
        else:
            add_team_win(old_wins_losses, away_team)
            add_team_loss(old_wins_losses, home_team)
        
        # Radioshack Sprint Wireless Rollover Baseball
        if home_team_score > away_team_score:
            #allow the away_team to try to buy their way to a win
            
            proposed_amount = (home_team_score - away_team_score) + 1
            
            received_points = withdraw_from_points_bank(away_team, proposed_amount)
            
            if received_points >= proposed_amount:
                add_team_win(new_wins_losses, away_team)
                add_team_loss(new_wins_losses, home_team)
            else:
                add_to_points_bank(home_team, home_team_score - away_team_score - received_points)
                add_team_win(new_wins_losses, home_team)
                add_team_loss(new_wins_losses, away_team)
        
        else:
            #allow the home_team to try to buy their way to a win
            proposed_amount = (away_team_score - home_team_score) + 1
            
            received_points = withdraw_from_points_bank(home_team, proposed_amount)
            
            if received_points >= proposed_amount:
                add_team_win(new_wins_losses, home_team)
                add_team_loss(new_wins_losses, away_team)
            else:
                add_to_points_bank(home_team, away_team_score - home_team_score - received_points)
                add_team_win(new_wins_losses, away_team)
                add_team_loss(new_wins_losses, home_team)
            

print(f"Under the old rules of baseball, these are the {season_to_get} W/L records")
print("Rank\tTeam                     \tWins\tLosses\tPCT")
print("---------------------------------------------------------------------------------------------------------")
old_wins = sort_the_wins(old_wins_losses)
for team in old_wins:
    print("\t".join([str(x) for x in team]))


print("\n\n")
print(f"Under the new t-mobile rules of baseball, these are the {season_to_get} W/L records")
print("Rank\tTeam                     \tWins\tLosses\tPCT\tPoints Left in the Bank")
print("---------------------------------------------------------------------------------------------------------")
new_wins = sort_the_wins(new_wins_losses)
for team in new_wins:
    print("\t".join([str(x) for x in team]) + "\t" + str(points_bank[team[1].strip()]))    

    