from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
    
class owner_det(models.Model):
    FLATNO =(
             ('101','101'),
             ('102','102'),
             ('103','103'),
             ('104','104'),
             ('105','105'),
             ('106','106'),
             ('107','107'),
             ('108','108'),
             ('201','201'),
             ('202','202'),
             ('203','203'),
             ('204','204'),
             ('205','205'),
             ('206','206'),
             ('207','207'),
             ('208','208'),
             ('301','301'),
             ('302','302'),
             ('303','303'),
             ('304','304'),
             ('305','305'),
             ('306','306'),
             ('307','307'),
             ('308','308'),
             ('401','401'),
             ('402','402'),
             ('403','403'),
             ('404','404'),
             ('405','405'),
             ('406','406'),
             ('407','407'),
             ('408','408'),
             ('501','501'),
             ('502','502'),
             ('503','503'),
             ('504','504'),
             ('505','505'),
             ('506','506'),
             ('507','507'),
             ('508','508'),
             
            )
    owner_flatno = models.CharField(max_length=3,choices=FLATNO)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=100)
    owner_dob = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    owner_email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+911234567890'. Up to 15 digits allowed.")
    owner_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    owner_comm_addr1 = models.CharField(max_length=100)
    owner_comm_addr2 = models.CharField(max_length=100)
    owner_comm_city = models.CharField(max_length=100)
    owner_comm_state = models.CharField(max_length=100)
    owner_comm_country = models.CharField(max_length=100)
    owner_comm_pincode = models.IntegerField()
    tenant_occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.owner_flatno
    
class tenant_det(models.Model):
    FLATNO =(
             ('101','101'),
             ('102','102'),
             ('103','103'),
             ('104','104'),
             ('105','105'),
             ('106','106'),
             ('107','107'),
             ('108','108'),
             ('201','201'),
             ('202','202'),
             ('203','203'),
             ('204','204'),
             ('205','205'),
             ('206','206'),
             ('207','207'),
             ('208','208'),
             ('301','301'),
             ('302','302'),
             ('303','303'),
             ('304','304'),
             ('305','305'),
             ('306','306'),
             ('307','307'),
             ('308','308'),
             ('401','401'),
             ('402','402'),
             ('403','403'),
             ('404','404'),
             ('405','405'),
             ('406','406'),
             ('407','407'),
             ('408','408'),
             ('501','501'),
             ('502','502'),
             ('503','503'),
             ('504','504'),
             ('505','505'),
             ('506','506'),
             ('507','507'),
             ('508','508'),
             
            )
    tenant_flatno = models.CharField(max_length=3,choices=FLATNO)
    tenant_first_name = models.CharField(max_length=100)
    tenant_last_name = models.CharField(max_length=100)
    tenant_dob =  models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    tenant_email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+911234567890'. Up to 15 digits allowed.")
    tenant_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    tenant_permnt_addr1 = models.CharField(max_length=100)
    tenant_permnt_addr2 = models.CharField(max_length=100)
    tenant_permnt_city = models.CharField(max_length=100)
    tenant_permnt_state = models.CharField(max_length=100)
    tenant_permnt_country = models.CharField(max_length=100)
    tenant_permnt_pincode = models.IntegerField()
    tenant_police_verification = models.BooleanField(default=False)
    tenant_occupy_date =  models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    tenant_vacate_date =  models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    
    def __str__(self):
        return self.tenant_flatno
    