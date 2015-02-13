# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailadmin.blocks
import demo.models
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_make_blogpage_body_into_streamfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField(block_types=[(b'heading', wagtail.wagtailadmin.blocks.CharBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(label=b'Image')), (b'speaker', demo.models.ExpertSpeakerBlock([(b'another_specialist_subject', wagtail.wagtailadmin.blocks.CharBlock(required=False))], label=b'Featured speaker')), (b'shopping_list', demo.models.ShoppingListBlock(wagtail.wagtailadmin.blocks.CharBlock())), (b'paragraph', wagtail.wagtailadmin.blocks.RichTextBlock())]),
            preserve_default=True,
        ),
    ]
