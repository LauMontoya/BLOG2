from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEntrega1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessages',
            new_name='ContactMessage',
        ),
        migrations.RenameModel(
            old_name='TeamMembers',
            new_name='TeamMember',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]