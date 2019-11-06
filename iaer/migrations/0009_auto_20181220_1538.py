# Generated by Django 2.0.5 on 2018-12-20 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iaer', '0008_auto_20181121_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_show_current', models.BooleanField(default=False)),
                ('home_show_this_month', models.BooleanField(default=False)),
                ('home_show_this_year', models.BooleanField(default=False)),
                ('created', models.DateField(blank=True, editable=False, null=True)),
                ('modified', models.DateField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iaer.User')),
            ],
        ),
        migrations.AlterField(
            model_name='iaer',
            name='category',
            field=models.CharField(choices=[('请选择类型', '请选择类型'), ('饮食', '饮食'), ('服饰美容', '服饰美容'), ('生活日用', '生活日用'), ('住房缴费', '住房缴费'), ('交通出行', '交通出行'), ('通讯物流', '通讯物流'), ('文教娱乐', '文教娱乐'), ('健康保险', '健康保险'), ('人情往来', '人情往来'), ('装修', '装修'), ('小孩奶粉', '小孩奶粉'), ('小孩尿布', '小孩尿布'), ('小孩玩具', '小孩玩具'), ('小孩健康', '小孩健康'), ('小孩零食', '小孩零食'), ('小孩服饰', '小孩服饰'), ('小孩文具', '小孩文具'), ('小孩生活用品', '小孩生活用品'), ('小孩其他', '小孩其他'), ('其他消费', '其他消费'), ('收入', '收入')], default=0, max_length=30),
        ),
    ]
