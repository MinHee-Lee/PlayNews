# Generated by Django 4.1.3 on 2022-12-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('newsid', models.AutoField(primary_key=True, serialize=False)),
                ('cnt', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('date_first', models.CharField(blank=True, max_length=45, null=True)),
                ('date_mod', models.CharField(blank=True, max_length=45, null=True)),
                ('newspaper', models.CharField(blank=True, max_length=45, null=True)),
                ('writer', models.CharField(blank=True, max_length=45, null=True)),
                ('context', models.TextField(blank=True, null=True)),
                ('img_link', models.CharField(blank=True, max_length=200, null=True)),
                ('img_alt', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'newsinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('userpw', models.CharField(max_length=20)),
                ('useremail', models.CharField(max_length=30)),
                ('userAddress', models.CharField(max_length=50)),
                ('userPhone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
