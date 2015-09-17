# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoImage',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('wagtailimages.image',),
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='audience',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=255),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateField(verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_to',
            field=models.DateField(blank=True, verbose_name='End date', null=True, help_text='Not required if event is on a single day'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_from',
            field=models.TimeField(blank=True, verbose_name='Start time', null=True),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_to',
            field=models.TimeField(blank=True, verbose_name='End time', null=True),
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='first_name',
            field=models.CharField(blank=True, verbose_name='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='last_name',
            field=models.CharField(blank=True, verbose_name='Surname', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.CharField(blank=True, verbose_name='Choices', max_length=512, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='default_value',
            field=models.CharField(blank=True, verbose_name='Default value', max_length=255, help_text='Default value. Comma separated values supported for checkboxes.'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(verbose_name='Field type', choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='help_text',
            field=models.CharField(blank=True, verbose_name='Help text', max_length=255),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='label',
            field=models.CharField(verbose_name='Label', max_length=255, help_text='The label of the form field'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='required',
            field=models.BooleanField(verbose_name='Required', default=True),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='from_address',
            field=models.CharField(blank=True, verbose_name='From address', max_length=255),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='subject',
            field=models.CharField(blank=True, verbose_name='Subject', max_length=255),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='to_address',
            field=models.CharField(blank=True, verbose_name='To address', max_length=255, help_text='Optional - form submissions will be emailed to this address'),
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
        migrations.AlterField(
            model_name='personpage',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
        ),
    ]
