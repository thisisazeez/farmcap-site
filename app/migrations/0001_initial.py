# Generated by Django 3.1.7 on 2021-11-16 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('membership_type', models.CharField(choices=[('Premium', 'pre'), ('Free', 'free')], default='Free', max_length=30)),
                ('price', models.DecimalField(decimal_places=90000, default=0, max_digits=9999999999999)),
            ],
        ),
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_membership', to='app.membership')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('user_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='app.usermembership')),
            ],
        ),
    ]
