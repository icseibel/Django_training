# Generated by Django 2.2.7 on 2019-12-19 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lancamento', '0006_auto_20191219_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento',
            name='tipolancamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipolancamento_fk', to='lancamento.TipoLancamento'),
        ),
    ]
