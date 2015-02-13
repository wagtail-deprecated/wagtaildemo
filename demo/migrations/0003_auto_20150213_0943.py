# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
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
            field=wagtail.wagtailcore.fields.StreamField(block_types=[(b'heading', wagtail.wagtailcore.blocks.CharBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(label=b'Image')), (b'speaker', demo.models.ExpertSpeakerBlock([(b'another_specialist_subject', wagtail.wagtailcore.blocks.CharBlock(required=False))], label=b'Featured speaker')), (b'shopping_list', demo.models.ShoppingListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock())]),
            preserve_default=True,
        ),
    ]
