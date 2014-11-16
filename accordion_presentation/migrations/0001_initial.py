# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import paintstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldPresentation',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to=b'icons')),
                ('color', paintstore.fields.ColorPickerField(max_length=7)),
                ('align', models.CharField(default=b'h', max_length=1, choices=[(b'v', 'Vertical'), (b'h', 'Horizontal')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PresentationAccordion',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
                ('custom_height', models.IntegerField(help_text='It is a number between 0 and 100', null=True, verbose_name='custom height porcentaje', blank=True)),
                ('custom_width', models.IntegerField(help_text='It is a number between 0 and 100', null=True, verbose_name='custom width porcentaje', blank=True)),
                ('custom_duration', models.IntegerField(help_text='Jquery Animation duration in milliseconds,ignore if not set', null=True, verbose_name='custom duration in milliseconds', blank=True)),
                ('background_color', paintstore.fields.ColorPickerField(max_length=7, null=True, blank=True)),
                ('cycle_fx', models.CharField(default=b'none', max_length=200, verbose_name='Type of transition', choices=[(b'none', b'None'), (b'fade', b'Fade'), (b'fadeout', b'Fadeout'), (b'scrollHorz', b'Scroll Horizontal'), (b'tileBlind', b'Tile Blind')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PresentationModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=500, null=True, blank=True)),
                ('icon', models.ImageField(upload_to=b'icons')),
                ('photo', models.ImageField(upload_to=b'photos')),
                ('color', paintstore.fields.ColorPickerField(max_length=7)),
                ('page_link', models.ForeignKey(blank=True, to='cms.Page', help_text='If present image will be clickable', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
