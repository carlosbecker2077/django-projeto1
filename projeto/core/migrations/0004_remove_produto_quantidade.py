# Generated by Django 3.2.3 on 2021-06-02 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_produto_quantidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='quantidade',
        ),
    ]
