# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailadmin.blocks
import demo.models
import wagtail.wagtailcore.fields
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField(block_types=[(b'heading', wagtail.wagtailadmin.blocks.FieldBlock(django.forms.fields.CharField)), (b'image', wagtail.wagtailadmin.blocks.ChooserBlock(label=b'Image')), (b'speaker', demo.models.ExpertSpeakerBlock([(b'another_specialist_subject', wagtail.wagtailadmin.blocks.TextInputBlock())], label=b'Featured speaker'))]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='default_value',
            field=models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
