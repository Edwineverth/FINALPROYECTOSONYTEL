# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulossegunda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('art_nombre', models.CharField(max_length=30, verbose_name='Nombre:')),
                ('art_precio', models.FloatField(verbose_name='Precio:')),
                ('art_cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('art_serie', models.CharField(max_length=50, verbose_name='Serie')),
                ('art_estado', models.CharField(default='D', verbose_name='Estado', max_length=1, editable=False)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mar_nombre', models.CharField(max_length=30, verbose_name='Nombre:')),
                ('mar_descripcion', models.CharField(max_length=75, verbose_name='Descripci\xf3n:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ciu_nombre', models.CharField(max_length=30, verbose_name='Nombre:')),
                ('ciu_descripcion', models.CharField(max_length=70, verbose_name='Descripci\xf3n:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cli_cedula', models.CharField(max_length=10, verbose_name='Cedula:')),
                ('cli_nombre', models.CharField(max_length=30, verbose_name='Nombre:')),
                ('cli_apellido', models.CharField(max_length=30, verbose_name='Apellido:')),
                ('cli_telefono', models.CharField(max_length=10, verbose_name='Telefono:', blank=True)),
                ('cli_direccion', models.CharField(max_length=75, verbose_name='Direcci\xf3n:')),
                ('cli_email', models.CharField(max_length=75, verbose_name='Email:')),
                ('cli_estado', models.CharField(max_length=1, verbose_name='Estado:')),
                ('ciu', models.ForeignKey(blank=True, to='sistema.Ciudad', null=True)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_fac', models.AutoField(serialize=False, primary_key=True)),
                ('fac_subtotal', models.FloatField()),
                ('fac_iva', models.FloatField()),
                ('fac_descuento', models.FloatField(verbose_name='Ingrese descuento')),
                ('fac_total', models.FloatField()),
                ('fac_fecha', models.DateField()),
                ('fac_estado', models.CharField(max_length=1)),
                ('serializador', models.IntegerField()),
                ('cli', models.ForeignKey(blank=True, to='sistema.Clientes', null=True)),
            ],
            options={
                'ordering': ['id_fac'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facturadetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('det_cantiadd', models.IntegerField()),
                ('det_preciou', models.FloatField()),
                ('det_preciot', models.FloatField()),
                ('fac', models.ForeignKey(blank=True, to='sistema.Factura', null=True)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facturadetallemantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fad_preciou', models.FloatField()),
                ('fad_preciot', models.FloatField()),
                ('fac', models.ForeignKey(to='sistema.Factura')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('man_fecha', models.DateField()),
                ('man_garantia', models.IntegerField()),
                ('man_informe', models.TextField(max_length=300)),
                ('man_fechaentrega', models.DateField()),
                ('man_estado', models.CharField(max_length=1, blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mensajeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('men_asunto', models.CharField(max_length=30, verbose_name='Nombre:')),
                ('men_descripcion', models.CharField(max_length=500, verbose_name='Descripci\xf3n:')),
                ('cli', models.ForeignKey(to='sistema.Clientes')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mod_nombre', models.CharField(max_length=30, verbose_name='Nombre:')),
                ('mod_descripcion', models.CharField(max_length=75, verbose_name='Descripci\xf3n:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ord_subtotal', models.FloatField()),
                ('ord_iva', models.FloatField()),
                ('ord_descuento', models.FloatField()),
                ('ord_total', models.FloatField()),
                ('ord_fecha', models.DateField()),
                ('ord_estado', models.CharField(max_length=1)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_nombre', models.CharField(max_length=30, verbose_name='Nombre:')),
                ('pro_cantidad', models.IntegerField(verbose_name='Cantidad:')),
                ('pro_precio', models.FloatField(verbose_name='Precio:')),
                ('pro_ecg', models.CharField(max_length=75, verbose_name='ECG:', blank=True)),
                ('pro_tarifa_iva', models.FloatField(verbose_name='IVA:')),
                ('pro_ex', models.IntegerField(verbose_name='Cant Min:')),
                ('pro_pvp', models.FloatField(verbose_name='Precio Venta Publico:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detalleproveedor',
            fields=[
                ('pro', models.ForeignKey(primary_key=True, serialize=False, to='sistema.Productos')),
                ('kar_precio_proveedor', models.FloatField(db_column='kar_Precio_proveedor')),
                ('kar_entra', models.IntegerField()),
                ('kar_sald', models.IntegerField()),
                ('kar_fecha', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prov_ruc', models.CharField(max_length=13, verbose_name='RUC')),
                ('prov_cedula', models.CharField(max_length=10, verbose_name='CEDULA')),
                ('prov_nombre', models.CharField(max_length=30, verbose_name='NOMBRE')),
                ('prov_representante', models.CharField(max_length=50, verbose_name='REPRESENTANTE')),
                ('prov_direccion', models.CharField(max_length=80, verbose_name='DIRECCI\xd3N')),
                ('prov_telefono', models.CharField(max_length=10, verbose_name='TELEFONO', blank=True)),
                ('prov_estado', models.CharField(max_length=1, verbose_name='ESTADO', blank=True)),
                ('ciu', models.ForeignKey(verbose_name='CIUDAD', blank=True, to='sistema.Ciudad', null=True)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Repuestos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rep_cantidad', models.IntegerField()),
                ('man', models.ForeignKey(to='sistema.Mantenimiento')),
                ('pro', models.ForeignKey(to='sistema.Productos')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicitudmantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solm_fecha', models.DateField(verbose_name='Fecha')),
                ('solm_falla', models.CharField(max_length=100, verbose_name='Falla')),
                ('solm_observaciones', models.CharField(max_length=100, verbose_name='Observacion', blank=True)),
                ('solm_abono', models.FloatField(verbose_name='Abono')),
                ('solm_saldo', models.FloatField(verbose_name='Saldo')),
                ('solm_total', models.FloatField(verbose_name='Total')),
                ('solm_estado', models.CharField(max_length=1, verbose_name='Estado', blank=True)),
                ('art', models.ForeignKey(to='sistema.Articulossegunda')),
                ('cli', models.ForeignKey(blank=True, to='sistema.Clientes', null=True)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productos',
            name='mar',
            field=models.ForeignKey(verbose_name='TIPO:', blank=True, to='sistema.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='prov',
            field=models.ForeignKey(to='sistema.Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='solm',
            field=models.ForeignKey(to='sistema.Solicitudmantenimiento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facturadetallemantenimiento',
            name='solm',
            field=models.ForeignKey(to='sistema.Solicitudmantenimiento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facturadetalle',
            name='pro',
            field=models.ForeignKey(blank=True, to='sistema.Productos', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalleproveedor',
            name='ord',
            field=models.ForeignKey(blank=True, to='sistema.OrdenDeCompra', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulossegunda',
            name='mar',
            field=models.ForeignKey(verbose_name='Marca', blank=True, to='sistema.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulossegunda',
            name='mod',
            field=models.ForeignKey(verbose_name='Modelo', blank=True, to='sistema.Modelo', null=True),
            preserve_default=True,
        ),
    ]
