# Generated by Django 2.1.5 on 2022-12-31 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EMapp', '0004_auto_20221231_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense_management',
            name='Sign_In',
        ),
        migrations.AddField(
            model_name='expense_management',
            name='Sign_In',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EMapp.Sign_In'),
        ),
    ]