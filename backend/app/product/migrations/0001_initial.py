# Generated by Django 2.2.9 on 2020-01-24 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'bunches',
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'flowers',
            },
        ),
        migrations.CreateModel(
            name='BunchContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_quantity', models.IntegerField(null=True)),
                ('bunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Flower')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Bunch')),
            ],
            options={
                'db_table': 'bunch_content',
            },
        ),
        migrations.AddField(
            model_name='bunch',
            name='flower',
            field=models.ManyToManyField(through='product.BunchContent', to='product.Flower'),
        ),
    ]
