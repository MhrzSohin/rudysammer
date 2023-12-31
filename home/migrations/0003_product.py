# Generated by Django 4.2.6 on 2023-10-30 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_services_number_services_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('slug', models.TextField(unique=True)),
                ('labels', models.CharField(choices=[('organic', 'organic'), ('fresh', 'fresh'), ('best', 'best')], max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
