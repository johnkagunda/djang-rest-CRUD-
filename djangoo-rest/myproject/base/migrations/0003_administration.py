# Generated by Django 5.0.6 on 2024-06-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField()),
                ('admin_name', models.CharField(max_length=100)),
            ],
        ),
    ]
