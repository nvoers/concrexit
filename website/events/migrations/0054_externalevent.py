# Generated by Django 3.2.8 on 2021-10-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0053_auto_20220112_2049_squashed_0054_auto_20220126_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organiser', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('alumni', 'Alumni'), ('education', 'Education'), ('career', 'Career'), ('leisure', 'Leisure'), ('association', 'Association Affairs'), ('other', 'Other')], help_text='Alumni: Events organised for alumni, Education: Education focused events, Career: Career focused events, Leisure: borrels, parties, game activities etc., Association Affairs: general meetings or any other board related events, Other: anything else.', max_length=40, verbose_name='category')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('location', models.CharField(max_length=255, verbose_name='location')),
                ('start', models.DateTimeField(verbose_name='start time')),
                ('end', models.DateTimeField(verbose_name='end time')),
                ('url', models.URLField(verbose_name='website')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
            ],
        ),
    ]