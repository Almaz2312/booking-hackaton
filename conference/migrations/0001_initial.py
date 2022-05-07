# Generated by Django 4.0.4 on 2022-04-30 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('conference_type', models.IntegerField(choices=[(1, 'Большой'), (2, 'Средний'), (3, 'Маленький')], null=True)),
                ('quantity', models.IntegerField()),
                ('projector', models.BooleanField(default=True)),
                ('conditioner', models.BooleanField(default=True)),
                ('board', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='conference')),
                ('conference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conference.conference')),
            ],
        ),
    ]