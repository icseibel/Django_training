# Generated by Django 2.2.7 on 2019-12-06 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lancamento', '0002_lancamento_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipolancamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='lancamento',
            name='tipolancamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipolancamento_fk', to='lancamento.tipolancamento'),
        ),
    ]
