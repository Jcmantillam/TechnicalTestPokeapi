from GetPokemon.models import Evolution_chain,Pokemon
from rest_framework import serializers


class Evolution_chainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evolution_chain
        fields = "__all__"


class PokemonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pokemon
        fields = ('name', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 
                  'speed', 'height', 'weight', 'p_id', 'evolves')