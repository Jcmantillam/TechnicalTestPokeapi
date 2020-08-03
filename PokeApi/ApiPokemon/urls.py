from django.urls import include, path
from rest_framework import routers
from ApiPokemon.views import Evolution_chainViewSet,PokemonViewSet

router = routers.DefaultRouter()
router.register('evolutions', Evolution_chainViewSet, 'evolutions')
router.register('pokemons', PokemonViewSet, 'pokemons')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]