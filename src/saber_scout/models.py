from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name