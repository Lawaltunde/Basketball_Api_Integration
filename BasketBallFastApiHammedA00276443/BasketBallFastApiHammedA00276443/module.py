from balldontlie import BalldontlieAPI

#KEY
API_KEY = "71d00446-0de7-4d7e-9025-ad080b0bc59e"

# Creating a new instance of the BalldontlieAPI class
api = BalldontlieAPI(api_key=API_KEY)


# Fetching all teams
def get_data():
  teams = api.nba.teams.list()
  print(teams)
  return teams


# Fetching team by id
def get_team(team_id: int):
  team = api.nba.teams.get(team_id)
  return team


# Fetching just 50 players
def get_players():
  players = api.nba.players.list(per_page=50)
  return players


# fetching just player by id

def get_player(player_id: int):
  player = api.nba.players.get(player_id)
  return player

# fetching games
def get_games():
  games = api.nba.games.list()
  return games

# fetch game by id
def get_game(game_id : int):
  games = api.nba.games.get(game_id)
  return games