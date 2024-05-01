# Generated by Django 3.2.3 on 2021-09-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.FloatField()),
                ('authors', models.CharField(max_length=300)),
                ('publisher', models.CharField(max_length=300)),
                ('pubdate', models.DateField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]