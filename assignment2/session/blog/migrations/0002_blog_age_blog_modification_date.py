# Generated by Django 4.2.11 on 2024-03-28 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='age',
            field=models.IntegerField(default=1, help_text='만나이를 입력해주세요'),
        ),
        migrations.AddField(
            model_name='blog',
            name='modification_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]