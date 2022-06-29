# Generated by Django 4.0.5 on 2022-06-22 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('joindate', models.IntegerField()),
                ('course_id', models.ForeignKey(null='TRUE', on_delete=django.db.models.deletion.CASCADE, to='appwebprojctauthen.course')),
            ],
        ),
    ]