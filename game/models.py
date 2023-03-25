from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    opponent = models.CharField(max_length=50)

    # Probably will need to add two things:
    # an event list or something like that
    # something for time on ice

    def __str__(self):
        return f"Date: {self.date}, Opponent: {self.opponent}"



class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField()

    forward1 = models.CharField(verbose_name='Forward 1:', max_length=2, blank=True, null=True)
    forward2 = models.CharField(verbose_name='Forward 2:', max_length=2, blank=True, null=True)
    forward3 = models.CharField(verbose_name='Forward 3:', max_length=2, blank=True, null=True)
    defense1 = models.CharField(verbose_name='Defense 1:', max_length=2, blank=True, null=True)
    defense2 = models.CharField(verbose_name='Defense 2:', max_length=2, blank=True, null=True)
    goalie = models.CharField(verbose_name='Goalie:', max_length=2, blank=True, null=True)
    ext_attacker = models.CharField(verbose_name='Ext:', max_length=2, blank=True, null=True)
    
    special_teams = models.CharField(max_length=20)
    
    extra_attacker = models.CharField(max_length=20)
    

    HDGF = "HDGF"
    LDGF = "LDGF"
    HDGA = "HDGA"
    LDGA = "LDGA"

    HDSF = "HDSF"
    LDSF = "LDSF"
    HDSA = "HDSA"
    LDSA = "LDSA"

    MHDSF = "MHDSF"
    MLDSF = "MLDSF"
    MHDSA = "MHDSA"
    MLDSA = "MLDSA"

    EVENT_TYPE = [
        (HDGF, "High Danger Goal For"),
        (LDGF, "Low Danger Goal For"),
        (HDGA, "High Danger Goal Against"),
        (LDGA, "Low Danger Goal Against"),
        (HDSF, "High Danger Shot For"),
        (LDSF, "Low Danger Shot For"),
        (HDSA, "High Danger Shot Against"),
        (LDSA, "Low Danger Shot Against"),
        (MHDSF, "Missed High Danger Shot For"),
        (MLDSF, "Missed Low Danger Shot For"),
        (MHDSA, "Missed High Danger Shot Against"),
        (MLDSA, "Missed Low Danger Shot Against"),
    ]

    event_type = models.CharField(max_length=5)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Date: {self.date}, User: {self.user}\nEvent: {self.event_type}\nSpecial: {self.special_teams}, Extra: {self.extra_attacker}\nPlayers: {self.forward1}, {self.forward2}, {self.forward3}, {self.defense1}, {self.defense2}, {self.goalie}, {self.ext_attacker}"