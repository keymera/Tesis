# Generated by Django 2.2.1 on 2019-07-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]