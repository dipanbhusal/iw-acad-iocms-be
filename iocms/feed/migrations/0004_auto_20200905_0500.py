# Generated by Django 3.1 on 2020-09-05 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20200904_0613'),
        ('feed', '0003_auto_20200905_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroomfeed',
            name='assignment_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.assignment'),
        ),
    ]
