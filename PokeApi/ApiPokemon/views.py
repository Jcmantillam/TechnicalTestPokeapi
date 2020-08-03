from GetPokemon.models import Evolution_chain,Pokemon
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import Evolution_chainSerializer, PokemonSerializer

class Evolution_chainViewSet(viewsets.ModelViewSet):
    queryset = Evolution_chain.objects.all()
    serializer_class = Evolution_chainSerializer
    permission_classes = [permissions.AllowAny]

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PokemonSerializer
    lookup_field = 'name'