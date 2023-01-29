# Generated by Django 3.2.16 on 2023-01-27 22:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('produto', '0002_rename_categoria_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data_cadastro',
            field=models.DateField(default=datetime.date(2023, 1, 27)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtos', to='categoria.categoria'),
        ),
    ]
