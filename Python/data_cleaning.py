import json
import pandas as pd
file_path = r"C:\Users\Ayeshath Shaima\OneDrive\ドキュメント\Football_Analytics\open-data-master\open-data-master\data\matches\9\27.json"
with open(file_path,"r",encoding="utf-8") as file:
    matches = json.load(file)
print("Total matches:",len(matches))
print("First match:",matches[0])

# inspect the data
first_match = matches[0]
print(first_match.keys())

#check if there are nested data
for key,value in first_match.items():
    print(key,"-->",type(value))

home = first_match["home_team"]["home_team_name"]
away = first_match["away_team"]["away_team_name"]
home_score = first_match["home_score"]
away_score = first_match["away_score"]
print(f"{home} {home_score} {away_score} {away}")

for match in matches:
    home = match["home_team"]["home_team_name"]
    away = match["away_team"]["away_team_name"]
    home_score = match["home_score"]
    away_score = match["away_score"]
    print(f"{home} {home_score} {away_score} {away}")

home_wins = 0 
for match in matches:
    if match["home_score"] > match["away_score"]:
        home_wins += 1
print("Home-team wins:",home_wins)

away_wins = 0 
for match in matches:
    if match["away_score"] > match["home_score"]:
        away_wins += 1
print("Away-team wins:",away_wins)

draw = 0 
for match in matches:
    if match["home_score"] == match["away_score"]:
        draw += 1
print("Draws:",draw)

total_goals = 0
for match in matches:
    total_goals += match["home_score"]
    total_goals += match["away_score"]
print("Total Goals :",total_goals)


average_goals_per_match = total_goals / len(matches)
print("Average goals per match:",round(average_goals_per_match,2))


team_goals = {}
for match in matches :
    home = match["home_team"]["home_team_name"]
    away = match["away_team"]["away_team_name"]

    home_score = match["home_score"]
    away_score = match["away_score"]

    if home not in team_goals:
        team_goals[home] = 0
    team_goals[home] += home_score

    if away not in team_goals:
        team_goals[away] = 0
    team_goals[away] += away_score
print(team_goals)

top_team = max(team_goals , key = team_goals.get)
print("Top-scoring team:",top_team)
print("Goals scored:",team_goals[top_team])

team_conceded = {}
for match in matches :
    home = match["home_team"]["home_team_name"]
    away = match["away_team"]["away_team_name"]

    home_score = match["home_score"]
    away_score = match["away_score"]

    if home not in team_conceded:
        team_conceded[home] = 0
    team_conceded[home] += away_score

    if away not in team_conceded:
        team_conceded[away] = 0
    team_conceded[away] += home_score
print(team_conceded)

worst_defence = max(team_conceded , key = team_conceded.get)
print("Most goals conceded:",worst_defence)
print("goals conceded:",team_conceded[worst_defence])

goal_difference = {}
for team in team_goals:
    scored = team_goals[team]
    conceded = team_conceded[team]
    goal_difference[team] = scored - conceded
print("Goal difference for each team")
print(goal_difference)

#create a function to get goal difference value
def get_goal_difference(item):
    return item[1]

#sort team from highest to lowest
sorted_team = sorted(
    goal_difference.items(),key=get_goal_difference,reverse = True)

#display the ranking
print("Teams ranked by goal difference:")
for team,difference in sorted_team:
    print(team,":",difference)

team_wins = {}
team_draws = {}
team_losses = {}
team_points = {}
#team name entry for each dictionary
for team in team_goals:
    team_wins[team] = 0
    team_draws[team] = 0
    team_losses[team] = 0
    team_points[team] = 0

for match in matches:
    home = match["home_team"]["home_team_name"]
    away = match["away_team"]["away_team_name"]
    home_score = match["home_score"]
    away_score = match["away_score"]

    if home_score > away_score:
        team_wins[home] += 1
        team_losses[away] += 1
        team_points[home] += 3

    elif away_score > home_score:
        team_wins[away] += 1
        team_losses[home] += 1
        team_points[away] += 3

    else:
        team_draws[home] += 1
        team_draws[away] += 1
        team_points[home] += 1
        team_points[away] += 1

print("\nTeam performance:")
for team in team_wins:
    print(
        team,
        "| Wins:",team_wins[team],
        "| losses:",team_losses[team],
        "| draws:",team_draws[team],
         "| points:",team_points[team],
    )
#ranking team by points
#sort by points first if poitns are equal then go for goal difference

def get_team_ranking(item):
    team = item[0]
    points = team_points[team]
    difference = goal_difference[team]
    return points , difference

#sort
sorted_teams = sorted(
    team_points.items(),
    key = get_team_ranking,
    reverse = True
)
print("\nTeam Ranking:")
rank = 1
for team ,points in sorted_teams:
    print(
        rank,
        team,
        "| Points:", points,
        "|GD:" , goal_difference[team]
    )
    rank += 1

df = pd.DataFrame(matches)
print(df.columns.tolist())

print("\nFirst 5 matches:")
print(df.head())

print("\nFirst 5 match IDs:")
print(df["match_id"].head())

print("\nReferee information:")
print(df["referee"].head())

print("\nFirst referee country:")
print(df["referee"].iloc[0]["country"])

first_referee = df["referee"].iloc[0]
print("Referee:", first_referee["name"])
print("Country:", first_referee["country"]["name"])

print("\nFirst home team information :")
first_home_team = df["home_team"].iloc[0]
print(first_home_team)

print("\nAway team names:")
first_away_team = df["away_team"].iloc[0]
print(first_away_team["away_team_name"])

def get_home_team_name(team):
    return team["home_team_name"]

def get_team_id(team):
    if isinstance(team , dict):
        if "home_team_id" in team:
            return team.get("home_team_id")
        elif "away_team_id" in team:
            return team.get("away_team_id")
    return None

def get_away_team_name(team):
    return team["away_team_name"]

print("\nFirst match stadium:")
print(df["stadium"].iloc[0])
print("\nFirst match referee:")
print(df["referee"].iloc[0])

first_stadium = df["stadium"].iloc[0]
print("\nStadium name:",first_stadium["name"])

first_referee = df["referee"].iloc[0]
print("Referee name:",first_referee["name"])

print("\nFirst match competition:")
print(df["competition"].iloc[0])

print("\nFirst match season:")
print(df["season"].iloc[0])

def get_competition_name(competition):
    return competition["competition_name"]


def get_country_name(competition):
    return competition["country_name"]


def get_season_name(season):
    return season["season_name"]


def get_stadium_name(stadium):
    return stadium["name"]


def get_referee_name(referee):
    return referee["name"]

clean_matches = pd.DataFrame({
    "match_id": df["match_id"],
    "match_date": df["match_date"],
    "kick_off": df["kick_off"],
    "home_team_id": df["home_team"].apply(get_team_id),
    "home_team": df["home_team"].apply(get_home_team_name),
    "away_team_id": df["away_team"].apply(get_team_id),
    "away_team": df["away_team"].apply(get_away_team_name),
    "home_score": df["home_score"],
    "away_score": df["away_score"],
    "competition": df["competition"].apply(get_competition_name),
    "country": df["competition"].apply(get_country_name),
    "season": df["season"].apply(get_season_name),
    "stadium": df["stadium"].apply(get_stadium_name),
    "referee": df["referee"].apply(get_referee_name)
})

print("\nClean match table:")
print(clean_matches.head())

print("\nTable shape:", clean_matches.shape)

print("\nFirst home team id:")
print(first_home_team["home_team_id"])
print("\nFirst home team country:")
print(first_home_team["country"]["name"])

#create team table
def get_home_team_id(team):
    return team["home_team_id"]

def get_home_team_country(team):
    return team["country"]["name"]

def get_away_team_id(team):
    return team["away_team_id"]

def get_away_team_country(team):
    return team["country"]["name"]

home_teams = pd.DataFrame({
    "team_ID" : df["home_team"].apply(get_home_team_id),
    "team_name" : df["home_team"].apply(get_home_team_name),
    "country" : df["home_team"].apply(get_home_team_country)
    })

away_teams = pd.DataFrame({
    "team_ID" : df["away_team"].apply(get_away_team_id),
    "team_name" : df["away_team"].apply(get_away_team_name),
    "country" : df["away_team"].apply(get_away_team_country)
})

team_details = pd.concat(
    [home_teams , away_teams],ignore_index=True).drop_duplicates(subset = "team_ID").reset_index(drop = True)

print("\nTeam details:")
print(team_details.head())
print("\nTeam table shape:",team_details.shape)

print("\nUnique teams:")
print(len(team_details))

print("\nManagers of First home team :")
print(first_home_team["managers"])

print("\nFirst away teams manager:")
print(df["away_team"].iloc[0]["managers"])


def get_managers(team):
    managers =  team.get("managers")
    if not managers:
        return []
    return managers

def get_manager_details(manager):
    return {
        "manager_id": manager["id"],
        "manager_name": manager["name"],
        "nickname": manager["nickname"],
        "date_of_birth": manager["dob"],
        "country": manager["country"]["name"]
    }

home_manager_lists = df["home_team"].apply(get_managers)
print("\nManagers list:")
print(home_manager_lists.head())
    
away_manager_lists = df["away_team"].apply(get_managers)
print("\nManagers list:")
print(away_manager_lists.head())

all_manager_lists = pd.concat(
    [home_manager_lists , away_manager_lists], ignore_index = True
)
print("\nTotal manager lists:",len(all_manager_lists))
print("\nFirst combined manager lits:")
print(all_manager_lists.head())

all_managers = []

for manager_list in all_manager_lists:
    for manager in manager_list:
        all_managers.append(manager)

print("\nTotal manager records:", len(all_managers))
print("\nFirst manager record:")
print(all_managers[0])

manager_details = pd.DataFrame(
    [get_manager_details(manager) for manager in all_managers]
)

print("\nManager details before removing duplicates:")
print(manager_details.head())

print("\nManager table shape:", manager_details.shape)

manager_details = manager_details.drop_duplicates(
    subset="manager_id"
).reset_index(drop=True)

print("\nManager details after removing duplicates:")
print(manager_details.head())

print("\nManager table shape:", manager_details.shape)

print("\nFinal table summary")
print("clean matches:",clean_matches.shape)
print("team details:",team_details.shape)
print("manager details:",manager_details.shape)

print("\nMissing values in clean matches table:")
print(clean_matches.isnull().sum())
print("\nMissing values in team details table:")
print(team_details.isnull().sum())
print("\nMissing values in manager details table:")
print(manager_details.isnull().sum())

print("\nChecking Roger Schmidt records:")

print(
    manager_details[
        manager_details["manager_name"] == "Roger Schmidt"
    ]
)

print("\nChecking duplicate team IDs:")

print(
    team_details[
        team_details.duplicated(
            subset="team_ID",
            keep=False
        )
    ]
)

print("\nHome team IDs in clean_matches:")
print(clean_matches["home_team"].head())

print("\nAway team IDs in clean_matches:")
print(clean_matches["away_team"].head())

print("\nTeam IDs in team_details:")
print(team_details["team_ID"].head())

print(clean_matches.head())

print("\nMissing team IDs after correction:")

print(clean_matches[["home_team_id", "away_team_id"]].isnull().sum())

print("\nFirst 5 matches with team IDs:")
print(clean_matches[["home_team_id", "home_team", "away_team_id", "away_team"]].head())

#check for missing ids
all_team_ids = set(team_details["team_ID"])
home_team_ids = set(clean_matches["home_team_id"])
away_team_ids = set(clean_matches["away_team_id"])
missing_home_ids = home_team_ids - all_team_ids
missing_away_ids = away_team_ids - all_team_ids
print("\nMissing home team IDs:", missing_home_ids)
print("\nMissing away team IDs:", missing_away_ids)

#find duplicate team ids
print("\nDuplicate team ids:")
print(team_details["team_ID"].duplicated().sum())

#find duplicate manager ids
print("\nDuplicate manager ids:")
print(manager_details["manager_id"].duplicated().sum())

#check duplicate match id 
print(clean_matches["match_id"].duplicated().sum())

match_team_manager_records = []

for index, row in df.iterrows():

    # Extract home team managers
    home_team = row["home_team"]

    for manager in home_team.get("managers", []) or []:
        match_team_manager_records.append({
            "match_id": row["match_id"],
            "team_id": home_team["home_team_id"],
            "manager_id": manager["id"]
        })

    # Extract away team managers
    away_team = row["away_team"]

    for manager in away_team.get("managers", []) or []:
        match_team_manager_records.append({
            "match_id": row["match_id"],
            "team_id": away_team["away_team_id"],
            "manager_id": manager["id"]
        })

print(match_team_manager_records[:5])

match_team_managers = pd.DataFrame(match_team_manager_records)
print(match_team_managers.head())
print(match_team_managers.shape)

print(match_team_managers.isnull().sum())
print(match_team_managers.duplicated().sum())


#referential integrity
all_manager_ids = set(manager_details["manager_id"])
relationship_manager_ids = set(match_team_managers["manager_id"])
missing_manager_ids = relationship_manager_ids - all_manager_ids
print(missing_manager_ids)

all_team_ids = set(team_details["team_ID"])
relationship_team_ids = set(match_team_managers["team_id"])
missing_team_ids = relationship_team_ids - all_team_ids
print(missing_team_ids)

#export the tables 
clean_matches.to_csv("clean_matches.csv", index = False)
team_details.to_csv("team_details.csv" , index = False)
manager_details.to_csv("manager_details.csv", index = False)
match_team_managers.to_csv("match_team_managers.csv", index = False)

import os
print(os.getcwd())
