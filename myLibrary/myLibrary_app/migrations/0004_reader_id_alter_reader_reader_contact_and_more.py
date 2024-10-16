# Generated by Django 4.2.7 on 2023-11-27 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myLibrary_app', '0003_remove_reader_id_alter_reader_reader_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='id',
            field=models.BigAutoField(auto_created=True, default= 1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reader',
            name='reader_contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reader',
            name='reference_id',
            field=models.CharField(max_length=200),
        ),
    ]
