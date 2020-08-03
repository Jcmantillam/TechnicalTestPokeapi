from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Evolution_chain(models.Model):
    tree_id = models.IntegerField(null=False, blank=False, unique=True)
    base_pokemon = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.tree_id)
    


class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    #Stats
    hp = models.IntegerField(null=False, blank=False)
    attack = models.IntegerField(null=False, blank=False)
    defense = models.IntegerField(null=False, blank=False)
    sp_attack = models.IntegerField(null=False, blank=False)
    sp_defense = models.IntegerField(null=False, blank=False)
    speed = models.IntegerField(null=False, blank=False)

    height = models.IntegerField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    p_id = models.IntegerField(null=False, blank=False)

    level = models.IntegerField(null=False, blank=False)

    #LLave foránea a la cadena de evolución
    evol_tree = models.ForeignKey(Evolution_chain, 
                                  on_delete=models.CASCADE, 
                                  null=False, blank=False)

    pre_evolve = models.TextField(blank=True, null=True)
    evolves = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
   