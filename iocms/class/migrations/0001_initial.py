# Generated by Django 3.0.8 on 2020-08-27 17:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=150)),
                ('class_description', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_class_code_enabled', models.BooleanField(default=True)),
                ('class_code', models.CharField(max_length=8)),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
        migrations.CreateModel(
            name='ClassroomStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='class.Classroom')),
            ],
        ),
    ]
