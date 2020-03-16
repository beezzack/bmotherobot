# Generated by Django 3.0.3 on 2020-03-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageId', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('imagehashcode', models.CharField(max_length=100)),
            ],
        ),
    ]
