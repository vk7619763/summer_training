import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'job_info.settings')
import django
django.setup()

from app1.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_elements(elements=('project_manager','senior','junior'))
        feligibility=fake.random_elements(elements=('yes','no'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        jaipur_jobs=jaipurjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

populate(2)
