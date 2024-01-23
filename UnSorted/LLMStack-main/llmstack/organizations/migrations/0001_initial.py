# Generated by Django 4.2.1 on 2023-08-08 22:49

import django.contrib.postgres.fields
from django.db import connection, migrations, models
import django.db.models.deletion

from llmstack.common.utils.db_models import ArrayField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apiabstractor', '0001_initial'),
    ]

    if connection.vendor == 'postgresql':
        domains_field = ('domains', django.contrib.postgres.fields.ArrayField(
            base_field=models.CharField(max_length=100),
            default=list,
            help_text='List of allowed domains of the organization',
            size=None,
        ))
    else:
        domains_field = ('domains', ArrayField(
            null=True,
            help_text='List of allowed domains of the organization',
            blank=True,
        ))

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='Name of the organization', max_length=100)),
                ('slug', models.SlugField(blank=True, default=None,
                 help_text='Unique identifier for the organization', max_length=100, null=True, unique=True)),
                domains_field,
                ('admin_email', models.EmailField(
                    help_text='Email of the admin of the organization', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default=None,
                 null=True, upload_to='organizations/logos/')),
                ('default_app_visibility', models.PositiveSmallIntegerField(choices=[(0, 'Private'), (1, 'Organization'), (
                    2, 'Unlisted'), (3, 'Public')], default=3, help_text='Default app visibility for the organization')),
                ('max_app_visibility', models.PositiveSmallIntegerField(choices=[(0, 'Private'), (1, 'Organization'), (
                    2, 'Unlisted'), (3, 'Public')], default=3, help_text='Maximum app visibility for the organization')),
                ('allow_user_keys', models.BooleanField(
                    default=True, help_text='Whether to allow users to provide their own API keys or not')),
                ('azure_openai_api_key', models.CharField(blank=True, default=None,
                 help_text='Azure OpenAI key to use with Azure backend', max_length=256, null=True)),
                ('openai_key', models.CharField(blank=True, default=None,
                 help_text='OpenAI key to use with OpenAI backend', max_length=256, null=True)),
                ('stabilityai_key', models.CharField(blank=True, default=None,
                 help_text='StabilityAI key to use with StabilityAI backend', max_length=256, null=True)),
                ('cohere_key', models.CharField(blank=True, default=None,
                 help_text='Cohere API key to use with Cohere backend', max_length=256, null=True)),
                ('forefrontai_key', models.CharField(blank=True, default=None,
                 help_text='ForefrontAI API key to use with ForefrontAI backend', max_length=256, null=True)),
                ('elevenlabs_key', models.CharField(blank=True, default=None,
                 help_text='Elevenlabs API key to use with Elevenlabs backend', max_length=256, null=True)),
                ('azure_openai_endpoint', models.CharField(blank=True, default=None,
                 help_text='Azure OpenAI endpoint to use with Azure openai processor', max_length=256, null=True)),
                ('aws_access_key_id', models.CharField(blank=True, default=None,
                 help_text='AWS access key id to use with AWS backend', max_length=256, null=True)),
                ('aws_secret_access_key', models.CharField(blank=True, default=None,
                 help_text='AWS access key secret to use with AWS backend', max_length=256, null=True)),
                ('aws_default_region', models.CharField(blank=True, default=None,
                 help_text='AWS default region to use with AWS backend', max_length=64, null=True)),
                ('vectorstore_weaviate_url', models.CharField(blank=True, default=None,
                 help_text='Vectorstore URL to use with Vectorstore backend', max_length=256, null=True)),
                ('vectorstore_weaviate_api_key', models.CharField(blank=True, default=None,
                 help_text='Vectorstore API key to use with Vectorstore backend', max_length=256, null=True)),
                ('vectorstore_weaviate_text2vec_openai_module_config', models.JSONField(blank=True, default=None,
                 help_text='Text2Vec OpenAI module config to use with Vectorstore backend', null=True)),
                ('use_own_vectorstore', models.BooleanField(default=False,
                 help_text='Whether to use own Vectorstore instance or not')),
                ('use_azure_openai_embeddings', models.BooleanField(
                    default=False, help_text='Whether to use Azure OpenAI embeddings or not')),
                ('embeddings_api_rate_limit', models.PositiveIntegerField(
                    default=300, help_text='Rate limit for embeddings requests in requests/min')),
                ('embeddings_batch_size', models.PositiveIntegerField(
                    default=20, help_text='Batch size for embeddings requests')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('default_api_backend', models.ForeignKey(blank=True, help_text='Default API backend to use for the organization', null=True,
                 on_delete=django.db.models.deletion.SET_NULL, related_name='default_api_backend', to='apiabstractor.apibackend')),
                ('disabled_api_backends', models.ManyToManyField(
                    blank=True, related_name='disabled_api_backends', to='apiabstractor.apibackend')),
                ('organization', models.OneToOneField(
                    on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.organization')),
            ],
        ),
    ]
