# Generated by Django 2.2.6 on 2019-12-11 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_auto_20191206_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='playlist',
            name='video_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.Video'),
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
