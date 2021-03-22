# Generated by Django 3.1.7 on 2021-03-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('Born', models.CharField(default='No data available', max_length=50)),
                ('About', models.CharField(default='No data Available', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=120, unique=True)),
                ('price', models.IntegerField()),
                ('pub_year', models.IntegerField()),
                ('summary', models.CharField(max_length=500)),
                ('author_name', models.ManyToManyField(related_name='maps', to='bookapi.Authors')),
            ],
        ),
    ]
