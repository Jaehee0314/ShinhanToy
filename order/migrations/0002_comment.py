# Generated by Django 4.1.5 on 2023-01-26 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='댓글내용')),
                ('tstamp', models.DateTimeField(auto_now_add=True, verbose_name='등록일시')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='주문')),
            ],
            options={
                'verbose_name': '상품 댓글',
                'verbose_name_plural': '상품 댓글',
                'db_table': 'shinhan_product_comment',
            },
        ),
    ]
