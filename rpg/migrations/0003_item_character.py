# Generated by Django 4.2.10 on 2024-02-25 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='rpg.character'),
            preserve_default=False,
        ),
    ]
