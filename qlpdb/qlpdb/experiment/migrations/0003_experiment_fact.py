# Generated by Django 3.0.3 on 2020-02-21 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0002_auto_20200218_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='fact',
            field=models.FloatField(default=0, help_text='Manual scaling coefficient'),
            preserve_default=False,
        ),
    ]