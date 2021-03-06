# Generated by Django 3.1.6 on 2021-02-06 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other / Rather not say')], max_length=1)),
                ('company', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=40)),
                ('lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
            ],
        ),
    ]
