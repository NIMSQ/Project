# Generated by Django 5.0.1 on 2024-05-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['content']},
        ),
        migrations.AddField(
            model_name='product',
            name='categoty',
            field=models.CharField(blank=True, choices=[('phone', 'phone'), ('computer', 'computer')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='desception'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='photos/4/16/desert.jpeg', upload_to='photos/%y/%m/%d', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='name', max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=5),
        ),
    ]
