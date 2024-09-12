from main import models

def create_datas():
    staff_1 = models.Staff.objects.create(l_name='Axliddin', f_name='Boboyev', phone='998907772233', age=30, address='Qoqon')
    staff_2 = models.Staff.objects.create(l_name='SHHHSD', f_name='vghjvhvj', phone='998903337711', age=25, address='Quva')
    staff_3 = models.Staff.objects.create(l_name='csdmcsd', f_name='scdbnk', phone='998906661122', age=28, address='Rishton')
    staff_4 = models.Staff.objects.create(l_name='csd,mcsdn,', f_name='Dadajonov', phone='998337772233', age=19, address='Namangan')
    staff_5 = models.Staff.objects.create(l_name='', f_name='csd ncsd', phone='998911112233', age=32, address='Andijon')

    
    print(f"Created: {staff_1}, {staff_2}, {staff_3}, {staff_4, {staff_5}}")
