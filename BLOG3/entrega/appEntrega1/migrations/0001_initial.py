from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(max_length=900)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('githubaccount', models.CharField(max_length=30)),
            ],
        ),

    ]
