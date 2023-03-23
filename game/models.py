from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField()

    forward1 = models.CharField(verbose_name='Forward 1:', max_length=2, blank=True, null=True)
    forward2 = models.CharField(verbose_name='Forward 2:', max_length=2, blank=True, null=True)
    forward3 = models.CharField(verbose_name='Forward 3:', max_length=2, blank=True, null=True)
    defense1 = models.CharField(verbose_name='Defense 1:', max_length=2, blank=True, null=True)
    defense2 = models.CharField(verbose_name='Defense 2:', max_length=2, blank=True, null=True)
    goalie = models.CharField(verbose_name='Goalie:', max_length=2, blank=True, null=True)
    extra_attacker = models.CharField(verbose_name='Ext:', max_length=2, blank=True, null=True)
    
    powerplay = models.BooleanField(verbose_name='Powerplay:', default=False)
    penaltykill = models.BooleanField(verbose_name='Penalty Kill:', default=False)
    extra_for = models.BooleanField(verbose_name='Extra Attacker For:', default=False)
    extra_against = models.BooleanField(verbose_name='Extra Attacker Against:', default=False)

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


    event_type = models.CharField(verbose_name='Event type', max_length=5, choices=EVENT_TYPE)
    id = models.AutoField(primary_key=True)