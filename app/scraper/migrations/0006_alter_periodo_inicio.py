# Generated by Django 4.0.3 on 2022-03-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_alter_caracterizacaodecurso_periodos_de_oferta_do_curso_nos_proximos_5_anos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='inicio',
            field=models.DateField(null=True),
        ),
    ]
