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
                  'attribute_agi', 'attribute_str', 'attribute_int', 'mana_regen', 'hp_regen', 'armor', 'img']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ['id', 'item_name', 'active', 'passive', 'stats', 'price', 'img']


class NeutralItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = neutral_items
        fields = ['id', 'name', 'active', 'passive', 'stats', 'tier', 'img']


class StructuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = structures
        fields = ['id', 'name', 'health', 'health_regen', 'gold_bounty', 'armor', 'magic_resist', 'attack_speed',
                  'damage', 'img']


class LineCreepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = line_creeps
        fields = ['id', 'name', 'attack_type', 'damage', 'attack_time', 'attack_range', 'move_speed', 'armor',
                  'magic_resist', 'health', 'mana', 'health_regen', 'mana_regen', 'gold_bounty', 'XP_bounty', 'img']


class SmallCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = small_neutral_camps
        fields = ['id', 'name', 'health', 'health_regen', 'mana', 'mana_regen', 'gold_bounty', 'XP_bounty', 'armor',
                  'magic_resist', 'attack_speed', 'attack_range', 'damage', 'img']


class BigCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = big_neutral_camps
        fields = ['id', 'name', 'health', 'health_regen', 'mana', 'mana_regen', 'gold_bounty', 'XP_bounty', 'armor',
                  'magic_resist', 'attack_speed', 'attack_range', 'damage', 'img']


class AncientCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = ancient_neutral_camps
        fields = ['id', 'name', 'health', 'health_regen', 'mana', 'mana_regen', 'gold_bounty', 'XP_bounty', 'armor',
                  'magic_resist', 'attack_speed', 'attack_range', 'damage', 'img']
