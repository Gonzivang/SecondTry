# Generated by Django 4.2.1 on 2023-08-08 22:49

from django.conf import settings
import django.contrib.postgres.fields
from django.db import connection, migrations, models
import django.db.models.deletion
import uuid

from llmstack.common.utils.db_models import ArrayField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiBackend',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the API', max_length=50)),
                ('slug', models.CharField(default='',
                 help_text='Slug for the API Backend', max_length=50)),
                ('description', models.CharField(blank=True, default='',
                 help_text='Description of the API backend', max_length=1000, null=True)),
                ('api_endpoint', models.CharField(
                    help_text='URL endpoint used for this API', max_length=100)),
                ('params', models.JSONField(blank=True, default=dict,
                 help_text='A JSON containing name, type, default values, help text etc., for this API. For example, things like stop, echo', null=True)),
                ('input_schema', models.JSONField(blank=True, default=dict,
                 help_text='Input fields for this backend in JSON schema format', null=True)),
                ('output_schema', models.JSONField(blank=True, default=dict,
                 help_text='Output fields for this backend in JSON schema format', null=True)),
                ('config_schema', models.JSONField(blank=True, default=dict,
                 help_text='Configuration for this backend. Values for this will be set in endpoint when it is created', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApiProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='Name of the API backend (e.g., OpenAI V2', max_length=50)),
                ('slug', models.CharField(default='',
                 help_text='Slug for the API Provider', max_length=50)),
                ('prefix', models.CharField(
                    help_text='Prefix to use with all the outbound request URLs', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='User provided name for an instance of API endpoint', max_length=100)),
                ('uuid', models.UUIDField(
                    default=uuid.uuid4, help_text='Used to run APIs')),
                ('param_values', models.JSONField(
                    default=dict, help_text='User provided param values that overrides the defaults used by the API')),
                ('post_processor', models.CharField(
                    blank=True, help_text='A regular expression that can be run on the output', max_length=100)),
                ('draft', models.BooleanField(blank=True, default=False,
                 help_text='We create draft endpoints when testing from playground')),
                ('prompt', models.TextField(
                    default='', help_text='Prompt used with this API. Use {{}} to provide variable placeholders in snake_case which will be replaced by prompt_values in tests and requests')),
                ('config', models.JSONField(blank=True, default=dict,
                 help_text='Configuration for this endpoint. Values for this will be set in endpoint when it is created')),
                ('input', models.JSONField(blank=True, default=dict,
                 help_text='Input for this endpoint. Use {{}} to provide variable placeholders in snake_case which will be replaced by template_values in tests and requests')),
                ('is_live', models.BooleanField(default=False,
                 help_text='True for the version that is currently serving production traffic')),
                ('is_app', models.BooleanField(default=False,
                 help_text='True for the version that is used by an app')),
                ('version', models.IntegerField(default=0, editable=False,
                 help_text='Version number for the endpoint')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('parent_uuid', models.UUIDField(blank=True, default=None,
                 help_text='UUID of parent endpoint', null=True)),
                ('description', models.CharField(default='',
                 help_text='Commit message for this version', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EndpointInvocationCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(default='',
                 help_text='Month for the count as MM-YY', max_length=5)),
                ('count', models.IntegerField(
                    default=0, help_text='Count for the month')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('response_quality', models.CharField(
                    help_text='Quality rating for the response', max_length=100)),
                ('expected_response', models.CharField(
                    help_text='Expected response for the response', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PromptHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(
                    default=0, help_text='Rank of the instance')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('param_values', models.JSONField(default=dict,
                 help_text='Override param values with these')),
                ('prompt_values', models.JSONField(default=dict,
                 help_text='Values for placeholders in the prompt')),
                ('input', models.JSONField(default=dict, help_text='Input to the API')),
                ('config', models.JSONField(blank=True, default=dict,
                 help_text='Configuration for this endpoint. Values for this will be set in endpoint when it is created', null=True)),
                ('template_values', models.JSONField(blank=True, default=dict,
                 help_text='Values for placeholders in the input', null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('app_session_key', models.CharField(blank=True, default=None,
                 help_text='App session this request was made for', max_length=100, null=True)),
                ('app_id', models.IntegerField(blank=True, default=None,
                 help_text='App this request was made for', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_response', models.TextField(
                    help_text='Raw response JSON from backend')),
                ('processed_response', models.TextField(
                    help_text='Output returned to the user after running the post processor')),
                ('response_code', models.IntegerField(
                    help_text='Response code from the API backend')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('request', models.ForeignKey(help_text='Request this response corresponds to',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.request')),
            ],
        ),
        migrations.CreateModel(
            name='ShareTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4,
                 help_text='Test Case Identifier')),
                ('name', models.CharField(
                    help_text='Short description for test', max_length=100)),
                ('prompt_values', models.JSONField(blank=True,
                 help_text='Values for placeholders in the prompt')),
                ('expected_output', models.CharField(
                    blank=True, help_text='Expected response for the given prompt values', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4,
                 help_text='Test Case Identifier')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('endpoint', models.ForeignKey(help_text='Endpoint this is run against', null=True,
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.endpoint')),
                ('testcase', models.ForeignKey(help_text='Test case for the run',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.testcase')),
            ],
        ),
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4,
                 help_text='Test Set Identifier')),
                ('param_values', models.JSONField(blank=True, default=dict,
                 help_text='Override the params configured in the endpoint')),
                ('endpoint', models.ForeignKey(help_text='Endpoint to run the test suite on',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='VersionedEndpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('param_values', models.JSONField(blank=True,
                 default=dict, help_text='Override param values')),
                ('prompt', models.TextField(
                    help_text='Prompt used with this API. Use {{}} to provide variable placeholders in snake_case which will be replaced by prompt_values in tests and requests')),
                ('post_processor', models.CharField(
                    blank=True, help_text='A regular expression that can be run on the output. Overrides the one defined in the parent endpoint', max_length=100)),
                ('is_live', models.BooleanField(default=False,
                 help_text='True for the version that is currently serving production traffic')),
                ('version', models.UUIDField(default=uuid.uuid4,
                 editable=False, help_text='Version string for the endpoint')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(
                    help_text='Commit message for this version', max_length=100)),
                ('endpoint', models.ForeignKey(help_text='Parent endpoint',
                 on_delete=django.db.models.deletion.PROTECT, to='apiabstractor.endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='TestSetRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Identifier')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('testruns', models.ManyToManyField(to='apiabstractor.testrun')),
                ('testset', models.ForeignKey(help_text='Test Set for the run',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.testset')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4,
                 help_text='Test Case Identifier')),
                ('request', models.ForeignKey(help_text='Request made for the test case',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.request')),
                ('response', models.ForeignKey(help_text='Response for the test run',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.response')),
                ('testrun', models.ForeignKey(help_text='Test run tied to the result',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.testrun')),
            ],
        ),
        migrations.AddField(
            model_name='testcase',
            name='testset',
            field=models.ForeignKey(help_text='Test suite this test case is part of',
                                    on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.testset'),
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(
                    default=uuid.uuid4, help_text='Share Identifier')),
                ('name', models.CharField(default='Untitled',
                 help_text='Name of the share', max_length=100)),
                ('code', models.CharField(
                    help_text='Code to share the endpoint', max_length=8)),
                ('param_values', models.JSONField(blank=True, default=None,
                 help_text='Endpoint param values', null=True)),
                ('prompt', models.TextField(blank=True, default='',
                 help_text='Endpoint prompt', null=True)),
                ('prompt_values', models.JSONField(blank=True, default=None,
                 help_text='Endpoint prompt values', null=True)),
                ('input', models.JSONField(blank=True,
                 default=dict, help_text='Endpoint input values')),
                ('output', models.JSONField(blank=True,
                 default=dict, help_text='Endpoint output values')),
                ('template_values', models.JSONField(blank=True, default=None,
                 help_text='Endpoint input template values', null=True)),
                ('config_values', models.JSONField(blank=True,
                 default=dict, help_text='Endpoint config values')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(
                    default=False, help_text='Is this share archived')),
                ('is_private', models.BooleanField(blank=True,
                 default=False, help_text='Is this share private')),
                ('api_backend', models.ForeignKey(help_text='API backend for this share',
                 on_delete=django.db.models.deletion.PROTECT, to='apiabstractor.apibackend')),
                ('owner', models.ForeignKey(help_text='Owner of the shared entity',
                 on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('response', models.ForeignKey(default=None, help_text='Response to share', null=True,
                 on_delete=django.db.models.deletion.DO_NOTHING, to='apiabstractor.response')),
                ('tags', models.ManyToManyField(to='apiabstractor.sharetag')),
            ],
        ),
        migrations.CreateModel(
            name='RunEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('request_uuid', models.CharField(default=uuid.uuid4,
                 help_text='UUID for the run', max_length=40)),
                ('app_uuid', models.CharField(default=None,
                 help_text='UUID of the app', max_length=40, null=True)),
                ('endpoint_uuid', models.CharField(default=None,
                 help_text='UUID of the endpoint', max_length=40, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True,
                 help_text='Time at which the app instance was created')),
                ('session_key', models.CharField(default=None,
                 help_text='Session key', max_length=40, null=True)),
                ('request_user_email', models.CharField(default=None,
                 help_text='User email', max_length=320, null=True)),
                ('request_ip', models.CharField(
                    help_text='Request IP', max_length=40)),
                ('request_location', models.CharField(
                    help_text='Request location', max_length=100)),
                ('request_user_agent', models.CharField(
                    help_text='Request user agent', max_length=256)),
                ('request_content_type', models.CharField(
                    default='application/json', help_text='Request Content-Type', max_length=100)),
                ('request_body', models.TextField(
                    blank=True, default='', help_text='Request body')),
                ('response_status', models.IntegerField(
                    default=0, help_text='Response status')),
                ('response_content_type', models.CharField(
                    default='application/json', help_text='Response Content-Type', max_length=100)),
                ('response_body', models.TextField(
                    blank=True, default='', help_text='Response body')),
                ('response_time', models.FloatField(
                    default=0, help_text='Response time in seconds')),
                ('response_headers', models.JSONField(
                    blank=True, default=dict, help_text='Response headers')),
                ('processor_runs', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(blank=True, default=dict), default=list, help_text='Array of processor data for each endpoint including input and output data', size=None) if connection.vendor == 'postgresql' else ArrayField(
                    null=True, help_text='Array of processor data for each endpoint including input and output data',
                )),
                ('platform_data', models.JSONField(blank=True,
                 default=dict, help_text='Platform data for the run')),
                ('owner', models.ForeignKey(help_text='Owner of the app or endpoint',
                 on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
