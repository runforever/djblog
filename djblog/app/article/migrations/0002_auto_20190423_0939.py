# Generated by Django 2.2 on 2019-04-23 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='分类名')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Category', verbose_name='分类'),
        ),
    ]
