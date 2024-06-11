# Generated by Django 5.0.3 on 2024-06-11 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_contractor_id_alter_document_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentitem',
            options={'verbose_name': 'Инвентарь в документе', 'verbose_name_plural': 'Инвентарь в документе'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title'], 'verbose_name': 'Инвентарь', 'verbose_name_plural': 'Инвентарь'},
        ),
        migrations.AlterModelOptions(
            name='storageitem',
            options={'verbose_name': 'Инвентарь на складе', 'verbose_name_plural': 'Инвентарь на складе'},
        ),
        migrations.AlterField(
            model_name='documentitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product', verbose_name='Инвентарь'),
        ),
        migrations.AlterField(
            model_name='storageitem',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='main.product', verbose_name='Инвентарь'),
        ),
    ]