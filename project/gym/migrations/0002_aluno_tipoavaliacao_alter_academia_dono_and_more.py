# Generated by Django 4.2 on 2023-04-08 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=150)),
                ('E_mail', models.EmailField(max_length=254)),
                ('Data_Nascimento', models.DateField()),
                ('Data_pagamento', models.DateField(auto_now_add=True)),
                ('Valor_pagamento', models.FloatField()),
                ('Situacao', models.BooleanField(default=True)),
                ('Data_inscricao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='academia',
            name='Dono',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='academia',
            name='E_mail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='academia',
            name='Endereco',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='academia',
            name='Nome_academia',
            field=models.CharField(max_length=254),
        ),
        migrations.CreateModel(
            name='Risco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Problema', models.CharField(max_length=300)),
                ('Recomendacao', models.CharField(max_length=300)),
                ('academia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.academia')),
                ('aluno', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=100)),
                ('E_mail', models.EmailField(max_length=254)),
                ('academia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.academia')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_avaliacao', models.TimeField(auto_now_add=True)),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('Dobra_tripical', models.FloatField()),
                ('Dobra_abdominal', models.FloatField()),
                ('Dobra_subescapular', models.FloatField()),
                ('Dobra_axilar_media', models.FloatField()),
                ('Dobra_coxa', models.FloatField()),
                ('Dobra_toracica', models.FloatField()),
                ('Dobra_suprailiaca', models.FloatField()),
                ('Circoferencia_pescoco', models.FloatField()),
                ('Circoferencia_torax', models.FloatField()),
                ('Circoferencia_ombro', models.FloatField()),
                ('Circoferencia_cintura', models.FloatField()),
                ('Circoferencia_quadril', models.FloatField()),
                ('Circoferencia_abdomen', models.FloatField()),
                ('Circoferencia_braco_relaxado', models.FloatField()),
                ('Circoferencia_braco_contraido', models.FloatField()),
                ('Circoferencia_antebraco', models.FloatField()),
                ('Circoferencia_prox_coxa', models.FloatField()),
                ('Circoferencia_medial_coxa', models.FloatField()),
                ('Circoferencia_distal_coxa', models.FloatField()),
                ('Circoferencia_panturilha_coxa', models.FloatField()),
                ('TipoAvaliacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.tipoavaliacao')),
                ('academia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.academia')),
                ('aluno', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.aluno')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='academia',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.academia'),
        ),
    ]