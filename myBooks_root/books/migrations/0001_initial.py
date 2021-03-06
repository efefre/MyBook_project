# Generated by Django 2.2.2 on 2019-06-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('averageRaiting', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('canonicalVolumeLink', models.CharField(blank=True, max_length=250)),
                ('author', models.ManyToManyField(to='books.Author')),
                ('category', models.ManyToManyField(blank=True, to='books.Category')),
            ],
        ),
    ]
