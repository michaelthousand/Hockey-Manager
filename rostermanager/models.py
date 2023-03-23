from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Season(models.Model):
    year = models.CharField(max_length=9)

    def __str__(self):
        return self.year


class Player(models.Model):
    CENTER = "C"
    LEFT_WING = "LW"
    RIGHT_WING = "RW"
    LEFT_DEFENSE = "LD"
    RIGHT_DEFENSE = "RD"
    GOALIE = "G"

    POSITIONS = [
        (CENTER, "Center"),
        (LEFT_WING, "Left Wing"),
        (RIGHT_WING, "Right Wing"),
        (LEFT_DEFENSE, "Left Defense"),
        (RIGHT_DEFENSE, "Right Defense"),
        (GOALIE, "Goalie")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    player_num = models.PositiveIntegerField()
    position = models.CharField(max_length=2, choices=POSITIONS)
    on_roster = models.BooleanField(default=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    id = str(player_num) + str(last_name) + str(season) + str(user)

    def __str__(self):
        return f"#{self.player_num} - {self.first_name} {self.last_name} - {self.position}\nOn roster: {self.on_roster}"

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    note = models.TextField(max_length=300)
    id = str(user) + str(date)