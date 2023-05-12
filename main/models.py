from django.db import models

class heroes(models.Model):
    name = models.CharField(max_length=50)
    attack_type = models.CharField(max_length=50)
    damage = models.IntegerField((""))
    base_attack_time = models.FloatField((""))
    attack_range = models.IntegerField((""))
    main_attribute = models.TextField(max_length=15)
    attribute_agi = models.CharField(max_length=50)
    attribute_str = models.CharField(max_length=50)
    attribute_int = models.CharField(max_length=50)
    mana_regen = models.FloatField((""))
    hp_regen = models.FloatField((""))
    armor = models.IntegerField((""))
    img = models.ImageField()


# Create your models here.

class items(models.Model):
    item_name = models.TextField(max_length=50)
    active = models.CharField(max_length=200)
    passive = models.CharField(max_length=200)
    stats = models.CharField(max_length=100)
    price = models.IntegerField((""))
    img = models.ImageField()


class neutral_items(models.Model):
    name = models.TextField(max_length=50)
    active = models.CharField(max_length=200)
    passive = models.CharField(max_length=200)
    stats = models.CharField(max_length=100)
    tier = models.IntegerField((""))
    img = models.ImageField()


class structures(models.Model):
    name = models.TextField(max_length=20)
    health = models.IntegerField((""))
    health_regen = models.FloatField((""))
    gold_bounty = models.CharField(max_length=10)
    armor = models.FloatField((""))
    magic_resist = models.CharField(max_length=10)
    attack_speed = models.FloatField((""))
    damage = models.IntegerField((""))
    img = models.ImageField()


class line_creeps(models.Model):
    name = models.CharField(max_length=30)
    attack_type = models.CharField(max_length=50)
    damage = models.IntegerField((""))
    attack_time = models.FloatField((""))
    attack_range = models.IntegerField((""))
    move_speed = models.IntegerField((""))
    armor = models.FloatField((""))
    magic_resist = models.CharField(max_length=10)
    health = models.IntegerField((""))
    mana = models.IntegerField((""))
    health_regen = models.FloatField((""))
    mana_regen = models.FloatField((""))
    gold_bounty = models.CharField(max_length=10)
    XP_bounty = models.CharField(max_length=10)
    img = models.ImageField()


class small_neutral_camps(models.Model):
    name = models.CharField(max_length=30)
    health = models.IntegerField((""))
    health_regen = models.FloatField((""))
    mana = models.IntegerField((""))
    mana_regen = models.FloatField((""))
    gold_bounty = models.CharField(max_length=10)
    XP_bounty = models.CharField(max_length=10)
    armor = models.FloatField((""))
    magic_resist = models.CharField(max_length=10)
    attack_speed = models.FloatField((""))
    attack_range = models.IntegerField((""))
    damage = models.IntegerField((""))
    img = models.ImageField()


class big_neutral_camps(models.Model):
    name = models.CharField(max_length=30)
    health = models.IntegerField((""))
    health_regen = models.FloatField((""))
    mana = models.IntegerField((""))
    mana_regen = models.FloatField((""))
    gold_bounty = models.CharField(max_length=10)
    XP_bounty = models.CharField(max_length=10)
    armor = models.FloatField((""))
    magic_resist = models.CharField(max_length=10)
    attack_speed = models.FloatField((""))
    attack_range = models.IntegerField((""))
    damage = models.IntegerField((""))
    img = models.ImageField()


class ancient_neutral_camps(models.Model):
    name = models.CharField(max_length=30)
    health = models.IntegerField((""))
    health_regen = models.FloatField((""))
    mana = models.IntegerField((""))
    mana_regen = models.FloatField((""))
    gold_bounty = models.CharField(max_length=10)
    XP_bounty = models.CharField(max_length=10)
    armor = models.FloatField((""))
    magic_resist = models.CharField(max_length=10)
    attack_speed = models.FloatField((""))
    attack_range = models.IntegerField((""))
    damage = models.IntegerField((""))
    img = models.ImageField(upload_to='')
