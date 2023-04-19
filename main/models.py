from django.db import models
import json

class heroes(models.Model):
    name = models.CharField(max_length=50)
    attack_type = models.CharField(max_length=50)
    damage = models.IntegerField((""))
    base_attack_time = models.FloatField((""))
    attack_range = models.ImageField((""))
    main_attribute = models.TextField(max_length=15)
    attribute_agi = models.CharField(max_length=50)
    attribute_str = models.CharField(max_length=50)
    attribute_int = models.CharField(max_length=50)
    mana_regen = models.FloatField((""))
    hp_regen = models.FloatField((""))
    armor = models.IntegerField((""))
# Create your models here.
