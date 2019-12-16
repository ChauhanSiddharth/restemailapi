# Generated by Django 2.1.5 on 2019-12-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.EmailField(max_length=100)),
                ('receiver_email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('message_delete', models.BooleanField(default=False)),
                ('message_archive', models.BooleanField(default=False)),
                ('message_sent', models.BooleanField(default=False)),
            ],
        ),
    ]