from GetPokemon.models import Evolution_chain, Pokemon
import requests
import queue


def generate_request(url):#Genera la petición GET y guarda Json
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

def get_evolution_chain(id):#Pide el recurso a evolution-chain
    chain_request = 'https://pokeapi.co/api/v2/evolution-chain/' + str(id)
    response = generate_request(chain_request)

    if response:
        return __BFS(response)
       #user = response.get('name')
       #return user.get('name').get('first')

    

def search_save_pokemon(level, name, evol_list, chain_id):#Pide el recurso a evolution-chain y guarda los datos en la BD de la app
    chain_request = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    response = generate_request(chain_request)
    
    if response:

        #Creando cadena evolutiva
        evol_chain,created_chain = Evolution_chain.objects.get_or_create(tree_id=chain_id[0],
                                                            base_pokemon=evol_list[0][1])
        evol_chain.save()
        #Creando Pokemon
        hp = response["stats"][0]["base_stat"]
        attack = response["stats"][1]["base_stat"]
        defense = response["stats"][2]["base_stat"]
        sp_attack = response["stats"][3]["base_stat"]
        sp_defense = response["stats"][4]["base_stat"]
        speed = response["stats"][5]["base_stat"]
        height = response["height"]
        weight = response["weight"]
        p_id = response["id"]
        level = level
        pokemon,created_pokemon = Pokemon.objects.get_or_create(name=name,
                                                hp=hp,attack=attack,defense=defense,
                                                sp_attack=sp_attack,sp_defense=sp_defense,
                                                speed=speed,height=height,weight=weight,
                                                p_id=p_id,level=level,
                                                evol_tree=Evolution_chain.objects.get(tree_id=evol_chain.tree_id)
                                                )
        evolves = ""

        for item in evol_list:
            aux_request = 'https://pokeapi.co/api/v2/pokemon/' + str(item[1])
            aux_response = generate_request(aux_request)
            aux_id = aux_response["id"]
            if item[0] < level:
                aux_evol = "Preevolution"
            if item[0] > level:
                aux_evol = "Evolution"
            if item[0] == level  and item[0]!=name:
                aux_evol = "Varaint" 
            evolves = evolves + "Name: " + str(item[1]) + '\n'
            evolves = evolves + "Id: " + str(aux_id) + '\n'
            evolves = evolves + "Evolution type: " + aux_evol + '\n\n'

        pokemon.evolves = evolves
        pokemon.save()


#BFS para recorrer el arbol de evolución
def __BFS(respose_tree):
    output= []

    bfs_queue = queue.Queue()#Cola de recorrido
    visited = []#Arreglo que guarda los nodos visitados

    #Se guarda el nodo raíz
    name= respose_tree["chain"]["species"]["name"]
    output.append((1,name))

    bfs_queue.put((respose_tree["chain"],1))

    visited.append(respose_tree["chain"]["species"]["name"])#El nodo visitado(pokemon contado)

    
    try:
        if len(respose_tree["chain"]["evolves_to"]) > 0:

            #Recorriendo el arbol despues de la raiz
            while(not bfs_queue.empty()):
                node = bfs_queue.get()

                #Vecinos del nodo
                try:
                    chain = node[0]
                    level = node[1]
                    neighborhoods = chain["evolves_to"]
                    if len(neighborhoods) > 0:
                        #Recorrer vecinos
                        for item in neighborhoods:
                            pokemon = item["species"]["name"]
                            #Si el nodo no fue visitado
                            if pokemon not in visited:
                                bfs_queue.put((item,level+1))
                                visited.append(pokemon)
                                #Se añade al nodo
                                output.append((level+1,pokemon))
                except:
                    pass


    except:
       return output
    
    return output
  
