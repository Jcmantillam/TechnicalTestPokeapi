from django.core.management.base import BaseCommand, CommandError
from GetPokemon.services import get_evolution_chain, search_save_pokemon

#from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('chain_id', nargs=1, type=int)

    def handle(self, *args, **options):
        chain_id = options.get('chain_id', None)

        if chain_id:
            arg_id = chain_id[0]
            try:
                evol_tree = get_evolution_chain(arg_id)
                self.stdout.write(self.style.SUCCESS("Objetos encontrados: "))
                print(evol_tree)
                for node in evol_tree:
                    search_save_pokemon(node[0],node[1],evol_tree,chain_id)
            except:
                raise CommandError('El id "%s" no existe en pokeapi' % arg_id)
            self.stdout.write(self.style.SUCCESS("Proceso terminado"))