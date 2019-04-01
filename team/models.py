from django.db import models
import json

# Create your models here.

class Player(models.Model):

	full_name = models.CharField(max_length=100, help_text='Enter full name')

	short_name = models.CharField(max_length=40, help_text='Enter shortened version of name')

	team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)

	position = models.CharField(max_length=2, help_text='Enter player position')

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
		self.rushing_yards = jsom.dumps(rushing_yards)
	
	def get_rushing_yards(self):
		return json.loads(self.rushing_yards)

	#passing methods
	def set_num_passes(self, num_passes):
		self.num_passes = json.dumps(num_passes)

	def get_num_passes(self):
		return json.loads(self.num_passes)

	def set_passing_yards(self, rushing_yards):
		self.passing_yards = jsom.dumps(passing_yards)
	
	def get_passing_yards(self):
		return json.loads(self.passing_yards)
	"""
	week1_points = models.DecimalField(max_digits=5, decimal_places=2)
	week2_points = models.DecimalField(max_digits=5, decimal_places=2)
	week3_points = models.DecimalField(max_digits=5, decimal_places=2)
	week4_points = models.DecimalField(max_digits=5, decimal_places=2)
	week5_points = models.DecimalField(max_digits=5, decimal_places=2)
	week6_points = models.DecimalField(max_digits=5, decimal_places=2)
	week7_points = models.DecimalField(max_digits=5, decimal_places=2)
	week8_points = models.DecimalField(max_digits=5, decimal_places=2)
	week9_points = models.DecimalField(max_digits=5, decimal_places=2)
	week10_points = models.DecimalField(max_digits=5, decimal_places=2)
	week11_points = models.DecimalField(max_digits=5, decimal_places=2)
	week12_points = models.DecimalField(max_digits=5, decimal_places=2)
	week13_points = models.DecimalField(max_digits=5, decimal_places=2)
	wee14_points = models.DecimalField(max_digits=5, decimal_places=2)
	week15_points = models.DecimalField(max_digits=5, decimal_places=2)
	week16_points = models.DecimalField(max_digits=5, decimal_places=2)

	week1_catches_amount = models.IntegerField(max_digits=3)
	week2_catches_amount = models.IntegerField(max_digits=3)
	week3_catches_amount = models.IntegerField(max_digits=3)
	week4_catches_amount = models.IntegerField(max_digits=3)
	week5_catches_amount = models.IntegerField(max_digits=3)
	week6_catches_amount = models.IntegerField(max_digits=3)
	week7_catches_amount = models.IntegerField(max_digits=3)
	week8_catches_amount = models.IntegerField(max_digits=3)
	week9_catches_amount = models.IntegerField(max_digits=3)
	week10_catches_amount = models.IntegerField(max_digits=3)
	week11_catches_amount = models.IntegerField(max_digits=3)
	week12_catches_amount = models.IntegerField(max_digits=3)
	week13_catches_amount = models.IntegerField(max_digits=3)
	week14_catches_amount = models.IntegerField(max_digits=3)
	week15_catches_amount = models.IntegerField(max_digits=3)
	week16_catches_amount = models.IntegerField(max_digits=3)

	week1_catches_yards = models.IntegerField(max_digits=3)
	week2_catches_yards = models.IntegerField(max_digits=3)
	week3_catches_yards = models.IntegerField(max_digits=3)
	week4_catches_yards = models.IntegerField(max_digits=3)
	week5_catches_yards = models.IntegerField(max_digits=3)
	week6_catches_yards = models.IntegerField(max_digits=3)
	week7_catches_yards = models.IntegerField(max_digits=3)
	week8_catches_yards = models.IntegerField(max_digits=3)
	week9_catches_yards = models.IntegerField(max_digits=3)
	week10_catches_yards = models.IntegerField(max_digits=3)
	week11_catches_yards = models.IntegerField(max_digits=3)
	week12_catches_yards = models.IntegerField(max_digits=3)
	week13_catches_yards = models.IntegerField(max_digits=3)
	week14_catches_yards = models.IntegerField(max_digits=3)
	week15_catches_yards = models.IntegerField(max_digits=3)
	week16_catches_yards = models.IntegerField(max_digits=3)

	week1_rushes_amount = models.IntegerField(max_digits=3)
	week2_rushes_amount = models.IntegerField(max_digits=3)
	week3_rushes_amount = models.IntegerField(max_digits=3)
	week4_rushes_amount = models.IntegerField(max_digits=3)
	week5_rushes_amount = models.IntegerField(max_digits=3)
	week6_rushes_amount = models.IntegerField(max_digits=3)
	week7_rushes_amount = models.IntegerField(max_digits=3)
	week8_rushes_amount = models.IntegerField(max_digits=3)
	week9_rushes_amount = models.IntegerField(max_digits=3)
	week10_rushes_amount = models.IntegerField(max_digits=3)
	week11_rushes_amount = models.IntegerField(max_digits=3)
	week12_rushes_amount = models.IntegerField(max_digits=3)
	week13_rushes_amount = models.IntegerField(max_digits=3)
	week14_rushes_amount = models.IntegerField(max_digits=3)
	week15_rushes_amount = models.IntegerField(max_digits=3)
	week16_rushes_amount = models.IntegerField(max_digits=3)

	week1_rushes_yards = models.IntegerField(max_digits=3)
	week2_rushes_yards = models.IntegerField(max_digits=3)
	week3_rushes_yards = models.IntegerField(max_digits=3)
	week4_rushes_yards = models.IntegerField(max_digits=3)
	week5_rushes_yards = models.IntegerField(max_digits=3)
	week6_rushes_yards = models.IntegerField(max_digits=3)
	week7_rushes_yards = models.IntegerField(max_digits=3)
	week8_rushes_yards = models.IntegerField(max_digits=3)
	week9_rushes_yards = models.IntegerField(max_digits=3)
	week10_rushes_yards = models.IntegerField(max_digits=3)
	week11_rushes_yards = models.IntegerField(max_digits=3)
	week12_rushes_yards = models.IntegerField(max_digits=3)
	week13_rushes_yards = models.IntegerField(max_digits=3)
	week14_rushes_yards = models.IntegerField(max_digits=3)
	week15_rushes_yards = models.IntegerField(max_digits=3)
	week16_rushes_yards = models.IntegerField(max_digits=3)

	week1_passing_amounts = models.IntegerField(max_digits=3)
	week2_passing_amounts = models.IntegerField(max_digits=3)
	week3_passing_amounts = models.IntegerField(max_digits=3)
	week4_passing_amounts = models.IntegerField(max_digits=3)
	week5_passing_amounts = models.IntegerField(max_digits=3)
	week6_passing_amounts = models.IntegerField(max_digits=3)
	week7_passing_amounts = models.IntegerField(max_digits=3)
	week8_passing_amounts = models.IntegerField(max_digits=3)
	week9_passing_amounts = models.IntegerField(max_digits=3)
	week10_passing_amounts = models.IntegerField(max_digits=3)
	week11_passing_amounts = models.IntegerField(max_digits=3)
	week12_passing_amounts = models.IntegerField(max_digits=3)
	week13_passing_amounts = models.IntegerField(max_digits=3)
	week14_passing_amounts = models.IntegerField(max_digits=3)
	week15_passing_amounts = models.IntegerField(max_digits=3)
	week16_passing_amounts = models.IntegerField(max_digits=3)

	week1_passing_yards = models.IntegerField(max_digits=3)
	week2_passing_yards = models.IntegerField(max_digits=3)
	week3_passing_yards = models.IntegerField(max_digits=3)
	week4_passing_yards = models.IntegerField(max_digits=3)
	week5_passing_yards = models.IntegerField(max_digits=3)
	week6_passing_yards = models.IntegerField(max_digits=3)
	week7_passing_yards = models.IntegerField(max_digits=3)
	week8_passing_yards = models.IntegerField(max_digits=3)
	week9_passing_yards = models.IntegerField(max_digits=3)
	week10_passing_yards = models.IntegerField(max_digits=3)
	week11_passing_yards = models.IntegerField(max_digits=3)
	week12_passing_yards = models.IntegerField(max_digits=3)
	week13_passing_yards = models.IntegerField(max_digits=3)
	week14_passing_yards = models.IntegerField(max_digits=3)
	week15_passing_yards = models.IntegerField(max_digits=3)
	week16_passing_yards = models.IntegerField(max_digits=3)
	"""
class League(models.Model):
	league_name = models.CharField(max_length=30, help_text='Enter a league name')

	league_type = models.CharField(max_length=10, help_text='Enter a league scoring type')

class User(models.Model):
	user_name = models.CharField(max_length=50, help_text='Enter full name of user')

class FantasyTeam(models.Model):
	team_name = models.CharField(max_length=30, help_text='Enter a team name')

	league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	division = models.CharField(max_length=4, help_text='Enter division of team')

class PlayerInstance(models.Model):
	player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)

	fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.SET_NULL, null=True)

	is_on_waivers = models.BooleanField(default=True)








	