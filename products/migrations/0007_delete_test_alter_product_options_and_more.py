# Generated by Django 5.0.1 on 2024-05-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_test_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='categoty',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
