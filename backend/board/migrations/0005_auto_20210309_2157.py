# Generated by Django 3.1.7 on 2021-03-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20210303_1638'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='Board',
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, verbose_name='링크'),
        ),
    ]