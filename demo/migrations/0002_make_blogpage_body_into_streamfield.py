# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailadmin.blocks
import demo.models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField(block_types=[(b'heading', wagtail.wagtailadmin.blocks.HeadingBlock()), (b'image', wagtail.wagtailadmin.blocks.ChooserBlock(label=b'Image')), (b'speaker', demo.models.ExpertSpeakerBlock([(b'another_specialist_subject', wagtail.wagtailadmin.blocks.TextInputBlock())], label=b'Featured speaker'))]),
            preserve_default=True,
        ),
    ]
