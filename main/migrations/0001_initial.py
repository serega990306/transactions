# Generated by Django 3.0.2 on 2020-01-27 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_dttm', models.DateTimeField(auto_now_add=True)),
                ('user_get', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_get', to='main.Account')),
                ('user_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to='main.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Currency'),
        ),
    ]
