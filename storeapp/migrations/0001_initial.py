# Generated by Django 4.0.1 on 2022-01-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=5)),
                ('slug', models.SlugField(unique=True)),
                ('like', models.PositiveIntegerField(blank=True, null=True)),
                ('disponible_date', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=6)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]