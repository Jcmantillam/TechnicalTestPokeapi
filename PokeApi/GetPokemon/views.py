from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, Evolution_chain

#Para el front de la página de búsqueda
def index(request):
    if request.method == "POST":
        pokemon_name = request.POST.get("search")
        pokemon_name = pokemon_name.lower()
        pokemon_name = pokemon_name.strip()
        try:
            pokemon = Pokemon.objects.get(name=pokemon_name.strip())#Se obtienen todos los datos disponibles
        except:
            pokemon = False
        if pokemon:
            #Buscando la imagen de pokemon
            image_url = getURL(pokemon)

            #Se obtiene el árbol de evolución completo
            prev = []#Si el pokemon es evolución de otro
            variant = []#Si es una variación
            evolve = []#Si tiene evolución
            pokemons = Pokemon.objects.filter(evol_tree=pokemon.evol_tree)
            
            for p in pokemons:
                if pokemon.level > p.level:
                    node = [p.name,getURL(p)]
                    prev.append(node)
                if pokemon.level == p.level and pokemon.name!=p.name:
                    node = [p.name,getURL(p)]
                    variant.append(node)
                if pokemon.level < p.level:
                    node = [p.name,getURL(p)]
                    evolve.append(node)
            b_prev = False
            b_variant = False
            b_evolve = False
            if len(prev)>0:
                b_prev = True
            if len(variant)>0:
                b_variant = True
            if len(evolve)>0:
                b_evolve = True

            return render(request,
                    'index.html',
                    {
                        'Nombre': pokemon_name.upper(),
                        'pokemon': pokemon,
                        'image_url': image_url,
                        'prev': prev,
                        'variant': variant,
                        'evolve': evolve,
                        'b_prev': b_prev,
                        'b_variant': b_variant,
                        'b_evolve': b_evolve,
                    })
        else:
            print("404")
            return render(request,
                        'index.html',
                        {
                            'notfound': True,
                        })
    else:
        print("iniciando")
        return render(request,
                    'index.html')

def getURL(pokemon):
    image_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/"
    if pokemon.p_id<10:
        image_url = image_url + "00" + str(pokemon.p_id) + ".png"
    if pokemon.p_id>=10 and pokemon.p_id<100:
        image_url = image_url + "0" + str(pokemon.p_id) + ".png"
    if pokemon.p_id>=100:
        image_url = image_url + str(pokemon.p_id) + ".png"
    
    return image_url