# Generated by Django 3.1.4 on 2021-02-24 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=60, unique=True, verbose_name='Username')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_service_seller', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Security_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='Add security question', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.customuser')),
                ('user_answer', models.CharField(max_length=60)),
                ('user_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.security_question')),
            ],
        ),
    ]
