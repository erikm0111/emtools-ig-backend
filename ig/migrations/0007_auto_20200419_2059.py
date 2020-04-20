# Generated by Django 3.0.5 on 2020-04-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0006_auto_20200419_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computationdata',
            name='revision',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='identificationnumber',
            name='revision',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='masterlist',
            name='revision',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='revision',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='revision',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='ssn',
            name='revision',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default=None, max_length=1),
        ),
    ]
