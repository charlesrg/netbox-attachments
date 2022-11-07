# Generated by Django 4.0.7 on 2022-11-07 11:58

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import netbox_attachments.utils
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0077_customlink_extend_text_and_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetBoxAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('object_id', models.PositiveBigIntegerField()),
                ('file', models.FileField(upload_to=netbox_attachments.utils.attachment_upload)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name', 'pk'),
            },
        ),
    ]