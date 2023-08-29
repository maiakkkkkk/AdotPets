# Generated by Django 4.2.4 on 2023-08-29 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.CharField(max_length=8)),
                ('desc', models.CharField(max_length=200)),
                ('pref', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=10)),
                ('imagem', models.FileField(upload_to='media/imgPet')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
