from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
class TeamLocation(models.Model):
    home_city = models.CharField(max_length=50)
    home_state = models.CharField(max_length=50)
    home_city_abbr = models.CharField(max_length=5)
    home_state_abbr = models.CharField(max_length=5)
    
    def __unicode__(self):
        return self.home_city
    
class Team(models.Model):
    name = models.CharField(max_length=25)
    home_location = models.ForeignKey(TeamLocation)
    division = models.CharField(max_length=2)
    
