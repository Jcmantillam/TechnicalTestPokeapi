from django.contrib import admin
from django.urls import include,path
from GetPokemon.views import index

urlpatterns = [
    path('', include('ApiPokemon.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
