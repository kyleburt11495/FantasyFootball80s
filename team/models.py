from django.db import models
import json

# Create your models here.

class Player(models.Model):
	id = models.CharField(primary_key=True, max_length=100)

	full_name = models.CharField(max_length=100, help_text='Enter full name')

	short_name = models.CharField(max_length=40, help_text='Enter shortened version of name')

	team = models.ForeignKey('FantasyTeam', on_delete=models.SET_NULL, null=True)

	season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)

	position = models.CharField(max_length=2, help_text='Enter player position')

	bye_week = models.IntegerField(max_length=2, help_text="Enter player's bye week")

	num_catches = models.CharField(max_length=500)

	receiving_yards = models.CharField(max_length=500)

	num_rushes = models.CharField(max_length=500)

	rushing_yards = models.CharField(max_length=500)

	num_passes = models.CharField(max_length=500)

	passing_yards = models.CharField(max_length=500)


	#receiving methods
	def set_num_catches(self, num_catches):
		self.num_catches = json.dumps(num_catches)

	def get_num_catches(self):
		return json.loads(self.num_catches)

	def set_receiving_yards(self, receiving_yards):
		self.receiving_yards = json.dumps(receiving_yards)

	def get_receiving_yards(self):
		return json.loads(self.receiving_yards)

	#rushing methods
	def set_num_rushes(self, num_rushes):
		self.num_rushes = json.dumps(num_rushes)

	def get_num_rushes(self):
		return json.loads(self.num_catches)

	def set_rushing_yards(self, rushing_yards):
		self.rushing_yards = json.dumps(rushing_yards)
	
	def get_rushing_yards(self):
		return json.loads(self.rushing_yards)

	#passing methods
	def set_num_passes(self, num_passes):
		self.num_passes = json.dumps(num_passes)

	def get_num_passes(self):
		return json.loads(self.num_passes)

	def set_passing_yards(self, passing_yards):
		self.passing_yards = json.dumps(passing_yards)
	
	def get_passing_yards(self):
		return json.loads(self.passing_yards)
	
class League(models.Model):
	league_name = models.CharField(max_length=30, help_text='Enter a league name')

	league_type = models.CharField(max_length=10, help_text='Enter a league scoring type')

	season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)

class User(models.Model):
	user_name = models.CharField(max_length=50, help_text='Enter full name of user')

class FantasyTeam(models.Model):
	team_name = models.CharField(max_length=30, help_text='Enter a team name')

	league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	division = models.CharField(max_length=4, help_text='Enter division of team')

class PlayerInstance(models.Model):
	player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)

	league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

	fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.SET_NULL, null=True)

	is_on_waivers = models.BooleanField(default=True)

class Season(models.Model):
	year = models.IntegerField(primary_key=True, max_length=4)








	