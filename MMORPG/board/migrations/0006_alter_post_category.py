# Generated by Django 4.2.4 on 2023-09-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_category_alter_reply_comment_userssubscribed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default='', max_length=64, through='board.PostCategory', to='board.category'),
        ),
    ]