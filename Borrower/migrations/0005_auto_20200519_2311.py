# Generated by Django 3.0.5 on 2020-05-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Borrower', '0004_fairtradeborrower_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fairtradeborrower',
            name='credit_debt',
        ),
        migrations.RemoveField(
            model_name='fairtradeborrower',
            name='cur_adr_years',
        ),
        migrations.RemoveField(
            model_name='fairtradeborrower',
            name='cur_emp_years',
        ),
        migrations.RemoveField(
            model_name='fairtradeborrower',
            name='d_to_i',
        ),
        migrations.AddField(
            model_name='fairtradeborrower',
            name='capital',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='fairtradeborrower',
            name='credit_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fairtradeborrower',
            name='debt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='fairtradeborrower',
            name='interest',
            field=models.FloatField(default=3),
        ),
        migrations.AddField(
            model_name='fairtradeborrower',
            name='repayment_score',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='fairtradeborrower',
            name='education',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='fairtradeborrower',
            name='income',
            field=models.FloatField(default=0),
        ),
    ]
