# Generated by Django 3.1.14 on 2023-01-22 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_agent', models.CharField(max_length=1024)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('worker_id', models.UUIDField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=256)),
                ('fqdn', models.CharField(max_length=1024)),
                ('ip_address', models.CharField(max_length=32)),
                ('mac_address', models.CharField(max_length=17)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='worker',
            index=models.Index(fields=['mac_address'], name='cinfo_worke_mac_add_aeae62_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='worker',
            unique_together={('worker_id', 'mac_address')},
        ),
        migrations.AddField(
            model_name='request',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinfo.worker'),
        ),
        migrations.AddIndex(
            model_name='request',
            index=models.Index(fields=['timestamp'], name='cinfo_reque_timesta_5a8712_idx'),
        ),
        migrations.AddIndex(
            model_name='request',
            index=models.Index(fields=['worker'], name='cinfo_reque_worker__95957e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together={('worker', 'user_agent', 'timestamp')},
        ),
    ]