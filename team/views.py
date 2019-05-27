from django.shortcuts import render
from team.models import Player, League, User, FantasyTeam, PlayerInstance, Season
import json

# Create your views here.
def login(request):
	return render(request, 'login.html')
  
def draft(request):
    #get all players in specified season
    player_instances = PlayerInstance.objects.filter(league=request.league)
    jsonResponse = {
        'players': [],
        'teams': []
    }
    for player_instance in player_instances:
        info = Player.objects.filter(id=player_instance.player).values().first()
        player = {}
        player['info'] = info
        player['id'] = info.id
        jsonResponse['players'].append(player)
        

    return render(request, 'base.html')