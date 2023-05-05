from rest_framework import serializers
from .models import heroes
from .models import items
from .models import neutral_items
from .models import structures
from .models import line_creeps
from .models import small_neutral_camps
from .models import big_neutral_camps
from .models import ancient_neutral_camps


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = heroes
        fields = ['id', 'name', 'attack_type', 'damage', 'base_attack_time', 'attack_range', 'main_attribute',
                  'attribute_agi', 'attribute_str', 'attribute_int', 'mana_regen', 'hp_regen', 'armor']


class ItemSerializer(serializers.ModelSerializer):
    class Items:
        model = items
        fields = ['id', 'item_name', 'active', 'passive', 'stats', 'price']


class NeutralItemsSerializer(serializers.ModelSerializer):
    class Neutral_items:
        model = neutral_items
        fields = ['id', 'name', 'active', 'passive', 'stats', 'tier']


class StructuresSerializer(serializers.ModelSerializer):
    class Structures:
        model = structures
        fields = ['id', 'name', 'health', 'health_regen', 'gold_bounty', 'armor', 'magic_resist', 'attack_speed',
                  'damage']


class LineCreepsSerializer(serializers.ModelSerializer):
    class Line_creeps:
        model = line_creeps
        fields = ['id', 'name', 'attack_type', 'damage', 'attack_time', 'attack_range', 'move_speed', 'armor',
                  'magic_resist', 'health', 'mana', 'health_regen', 'mana_regen', 'gold_bounty', 'XP_bounty']


class SmallCampSerializer(serializers.ModelSerializer):
    class Small_neutral_camps:
        model = small_neutral_camps
        fields = ['id', 'name', 'health', 'health_regen', 'mana', 'mana_regen', 'gold_bounty', 'XP_bounty', 'armor',
                  'magic_resist', 'attack_speed', 'attack_range', 'damage']


class BigCampSerializer(serializers.ModelSerializer):
    class Big_neutral_camps:
        model = big_neutral_camps
        fields = ['id', 'name', 'health', 'health_regen', 'mana', 'mana_regen', 'gold_bounty', 'XP_bounty', 'armor',
                  'magic_resist', 'attack_speed', 'attack_range', 'damage']


class AncientCampSerializer(serializers.ModelSerializer):
    class Ancient_neutral_camps:
        model = ancient_neutral_camps
        fields = ['id', 'name', 'health', 'health_regen', 'mana', 'mana_regen', 'gold_bounty', 'XP_bounty', 'armor',
                  'magic_resist', 'attack_speed', 'attack_range', 'damage']
