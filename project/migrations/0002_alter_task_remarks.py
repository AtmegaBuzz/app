# Generated by Django 3.2.7 on 2021-10-07 08:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='remarks',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
