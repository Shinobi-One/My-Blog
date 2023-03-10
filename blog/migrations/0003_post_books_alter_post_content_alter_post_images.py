# Generated by Django 4.1.2 on 2023-02-20 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_remove_tag_tag_post_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Books',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='legacy', to='blog.author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(upload_to='blog/static/images'),
        ),
    ]
