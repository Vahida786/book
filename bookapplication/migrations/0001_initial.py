# Generated by Django 4.2.6 on 2023-11-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=200)),
                ('prize', models.PositiveIntegerField()),
                ('Date', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
