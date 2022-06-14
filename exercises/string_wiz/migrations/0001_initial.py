# Generated by Django 4.0.5 on 2022-06-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_question_text', models.CharField(max_length=4000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
