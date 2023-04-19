from rest_framework import serializers
from .models import heroes


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = heroes
        fields = ['id', 'name', 'attack_type', 'damage', 'base_attack_time', 'attack_range', 'main_attribute',
                  'attribute_agi', 'attribute_str', 'attribute_int', 'mana_regen', 'hp_regen', 'armor']
