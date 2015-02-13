# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailadmin.blocks
import demo.models
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20150213_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField(block_types=[(b'heading', wagtail.wagtailadmin.blocks.CharBlock()), (b'pullquote', demo.models.PullQuoteBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(label=b'Image')), (b'speaker', demo.models.ExpertSpeakerBlock([(b'another_specialist_subject', wagtail.wagtailadmin.blocks.CharBlock(required=False))], label=b'Featured speaker')), (b'shopping_list', demo.models.ShoppingListBlock(wagtail.wagtailadmin.blocks.CharBlock())), (b'paragraph', wagtail.wagtailadmin.blocks.RichTextBlock())]),
            preserve_default=True,
        ),
    ]
