# Generated by Django 4.2.1 on 2023-05-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_checklist_chore_alter_checklist_rest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drill', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='progress',
            name='recommendations',
            field=models.ManyToManyField(to='main_app.recommendation'),
        ),
    ]
