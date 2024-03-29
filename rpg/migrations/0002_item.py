# Generated by Django 4.2.10 on 2024-02-25 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('boosted_stat', models.CharField(choices=[('health', 'Health'), ('mana', 'Mana'), ('strength', 'Strength'), ('intelligence', 'Intelligence'), ('agility', 'Agility')], max_length=20)),
                ('value', models.IntegerField()),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='rpg.rarity')),
            ],
        ),
    ]
