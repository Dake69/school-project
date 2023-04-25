from rest_framework import serializers
from .models import heroes
from .models import items
from .models import neutral_items


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = heroes
        fields = ['id', 'name', 'attack_type', 'damage', 'base_attack_time', 'attack_range', 'main_attribute',
                  'attribute_agi', 'attribute_str', 'attribute_int', 'mana_regen', 'hp_regen', 'armor']

    class Items:
        model = items
        fields = ['id', 'item_name', 'active', 'passive', 'stats', 'price']

    class Neutral_items:
        model = neutral_items
        fields = ['id', 'name', 'active', 'passive', 'stats', 'tier']


