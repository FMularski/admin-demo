# Generated by Django 3.2 on 2024-02-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0007_statistics_depleted_mana'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='items/'),
        ),
    ]
