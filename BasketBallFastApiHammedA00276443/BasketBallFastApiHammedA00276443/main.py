from os import name
from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
import matplotlib.pyplot as plt
import io
from module import get_data, get_team, get_players, get_player, get_games, get_game
from statistics import stat, statistics

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
  message = " Welcome to Hammed fast API endpoint on data from Balldontlie  and a dashboard on analysis carried out on the data. use below link to access the dashboard"
  toDo = "https://c82022af-268f-456e-98ce-08b12c4672ba-00-onsyf6g2xboi.worf.replit.dev/hammed/v1/metadata"
  return {"message": message, "toDo": toDo}


# fetching all teams
@app.get("/hammed/v1/metadata")
async def metal_data():
  result = get_data()
  toDo = "https://c82022af-268f-456e-98ce-08b12c4672ba-00-onsyf6g2xboi.worf.replit.dev/hammed/v1/team/{team_id}"
  return [result, {"Get team details by id": toDo}]


# fetching team by id
@app.get("/hammed/v1/team/{team_id}")
async def team_data(team_id: int):
  teamDetails = get_team(team_id)
  return teamDetails


# fetching just 50 players
@app.get("/hammed/v1/players")
async def players():
  players = get_players()
  return players


# fetching player by id
@app.get("/hammed/v1/player/{player_id}")
async def player(player_id: int):
  player = get_player(player_id)
  return player


# games
@app.get("/hammed/v1/games")
async def games():
  games = get_games()
  return games


# game
@app.get("/hammed/v1/game/{game_id}")
async def game(game_id: int):
  game = get_game(game_id)
  return game

# mean, median and mode for weigths
@app.get("/hammed/stat")
async def statisticalAnalysis(request: Request):
  mean, median = statistics()
  values = [mean, median]
  return templates.TemplateResponse("index.html", {"request": request, "value": values[0], "value2": values[1]})

@app.get("/hammed/v1/dashboard")
async def dashboard(request: Request):
  """Render the HTML dashboard page."""
  return templates.TemplateResponse("index.html", {"request": request})

  # Web based Dashboard display

def generate_plot(plot_id):
  """Generate a different Matplotlib plot based on the ID."""

  fig, ax = plt.subplots()

  weights, heights, names = stat()
  if plot_id == 1:
    ax.bar(names, heights)
    ax.set_title("Height vs. Name")

  elif plot_id == 2:
    ax.bar(names, weights)
    ax.set_title("Bar Chart")

  elif plot_id == 3:
    ax.scatter(weights, heights)
    ax.set_title("Scatter Plot, Weight vs Height")

  elif plot_id == 4:
    ax.hist(weights, bins=5, color="green")
    ax.set_title("Weight Histogram")

  elif plot_id == 5:
    ax.hist(heights, bins=5, color="red")
    ax.set_title("Height Histogram")

  img = io.BytesIO()
  plt.savefig(img, format="png")
  img.seek(0)
  return img.getvalue()


@app.get("/plot/{plot_id}")
async def get_plot(plot_id: int):

  return Response(content=generate_plot(plot_id), media_type="image/png")


uvicorn.run(app, host='0.0.0.0', port=8080)
