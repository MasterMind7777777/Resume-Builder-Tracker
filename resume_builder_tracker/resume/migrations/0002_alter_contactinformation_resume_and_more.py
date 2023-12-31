# Generated by Django 4.2.2 on 2023-06-22 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='resume',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume'),
        ),
        migrations.AlterField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume'),
        ),
    ]
