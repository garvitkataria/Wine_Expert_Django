# Generated by Django 2.1.2 on 2019-02-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('designation', models.CharField(blank=True, max_length=250, null=True)),
                ('points', models.FloatField(default=-1.0)),
                ('price', models.FloatField(default=-1.0)),
                ('province', models.CharField(blank=True, max_length=250, null=True)),
                ('region_1', models.CharField(blank=True, max_length=250, null=True)),
                ('region_2', models.CharField(blank=True, max_length=250, null=True)),
                ('variety', models.CharField(blank=True, max_length=250, null=True)),
                ('winery', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
