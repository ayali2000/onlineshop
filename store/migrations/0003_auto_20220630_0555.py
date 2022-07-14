# Generated by Django 3.2 on 2022-06-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220626_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='items',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default='2022-6-30'),
            preserve_default=False,
        ),
    ]