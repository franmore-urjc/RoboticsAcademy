# Generated by Django 4.2.1 on 2023-09-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0016_merge_20230116_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='visualization',
            field=models.CharField(choices=[('gazebo_gra', 'Gazebo GRA'), ('INACTIVE', 'INACTIVE'), ('PROTOTYPE', 'PROTOTYPE')], default='INACTIVE', max_length=20),
        ),
    ]