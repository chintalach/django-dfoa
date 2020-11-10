# Generated by Django 3.1.2 on 2020-11-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner_det',
            name='user',
        ),
        migrations.AlterField(
            model_name='owner_det',
            name='owner_flatno',
            field=models.IntegerField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('201', '201'), ('202', '202'), ('203', '203'), ('204', '204'), ('205', '205'), ('206', '206'), ('207', '207'), ('208', '208'), ('301', '301'), ('302', '302'), ('303', '303'), ('304', '304'), ('305', '305'), ('306', '306'), ('307', '307'), ('308', '308'), ('401', '401'), ('402', '402'), ('403', '403'), ('404', '404'), ('405', '405'), ('406', '406'), ('407', '407'), ('408', '408'), ('501', '501'), ('502', '502'), ('503', '503'), ('504', '504'), ('505', '505'), ('506', '506'), ('507', '507'), ('508', '508')]),
        ),
        migrations.AlterField(
            model_name='tenant_det',
            name='tenant_flatno',
            field=models.IntegerField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('201', '201'), ('202', '202'), ('203', '203'), ('204', '204'), ('205', '205'), ('206', '206'), ('207', '207'), ('208', '208'), ('301', '301'), ('302', '302'), ('303', '303'), ('304', '304'), ('305', '305'), ('306', '306'), ('307', '307'), ('308', '308'), ('401', '401'), ('402', '402'), ('403', '403'), ('404', '404'), ('405', '405'), ('406', '406'), ('407', '407'), ('408', '408'), ('501', '501'), ('502', '502'), ('503', '503'), ('504', '504'), ('505', '505'), ('506', '506'), ('507', '507'), ('508', '508')]),
        ),
    ]