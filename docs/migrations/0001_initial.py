# Generated by Django 2.0.2 on 2018-03-07 18:12

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.URL')),
            ],
        ),
    ]