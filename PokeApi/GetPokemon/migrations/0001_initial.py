# Generated by Django 3.0.8 on 2020-08-01 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evolution_chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_id', models.IntegerField(unique=True)),
                ('base_pokemon', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('sp_attack', models.IntegerField()),
                ('sp_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('p_id', models.IntegerField()),
                ('level', models.IntegerField()),
                ('evol_tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GetPokemon.Evolution_chain')),
            ],
        ),
    ]
