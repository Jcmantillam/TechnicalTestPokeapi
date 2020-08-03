# TechnicalTestPokeapi
Aplicativo que consume de la API https://pokeapi.co/ a través de un comando personalizado de Django, este guarda la información consultada en la base de datos para su posterior consulta.

Para consultar la información guardada, sólo hace falta entrar a la página de inicio(vía front) o con peticiones rpeticiones HTTP REST en los vínculos correspondientes.

# Para usar la aplicación
Los pasos de instalación son los siguientes:
```
git clone https://github.com/Jcmantillam/TechnicalTestPokeapi.git
cd PokeApi
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Para utilizar el comando personalizado:
```
python manage.py get_evo_chain(id)
```
Este id pertence a Evolution Chains de [pokeapi](https://pokeapi.co/docs/v2#evolution-section) el cual almacena los árboles evolutivos de los pokemones exitentes. Los pokemones encontrados, serán guardados en la base de datos y podrán ser consultados a través de:
```
http://localhost:8000/ si se desea usar el front
http://localhost:8000/api/pokemons/ con Rest
```
#Requerimientos
- Python 3.5+
- Django 3.0.8
- Django Rest Framework 3.11.0
Para consultar todos los requerimientos, ir a [requirements.txt](https://github.com/Jcmantillam/TechnicalTestPokeapi/blob/master/PokeApi/requirements.txt).
