# Generated by Django 5.1.2 on 2024-10-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_rename_timestamp_todo_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.SmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='todo',
            name='tg_id',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='tg_name',
            field=models.CharField(max_length=180, null=True),
        ),
    ]
