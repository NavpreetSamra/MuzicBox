# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 15:34
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import imagekit.models.fields
import reactmusic.utils.models_helpers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sex', models.IntegerField(blank=True, choices=[(1, 'man'), (0, 'woman'), (None, "don't show")], null=True, verbose_name='gender')),
                ('slug', models.SlugField(help_text="automatically generated, don't change manually !", max_length=100, unique=True)),
                ('address_line1', models.CharField(blank=True, max_length=200, null=True, verbose_name='address line1')),
                ('address_line2', models.CharField(blank=True, max_length=200, null=True, verbose_name='address line2')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='city')),
                ('state', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('postal', models.CharField(blank=True, max_length=200, null=True, verbose_name='postal')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='phone')),
                ('cell', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='cell number')),
                ('profile_image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=reactmusic.utils.models_helpers.UploadToPathAndRename('profile_images'))),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
