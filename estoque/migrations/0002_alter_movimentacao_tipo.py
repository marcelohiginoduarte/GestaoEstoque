# Generated by Django 5.1.1 on 2024-09-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='tipo',
            field=models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1),
        ),
    ]
