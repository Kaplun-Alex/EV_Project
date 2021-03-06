# Generated by Django 3.2.9 on 2021-11-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ev_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='NewsModel',
        ),
    ]
