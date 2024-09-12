from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Shift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class Staff(models.Model):
    l_name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)


class StaffShift(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staff}, {self.position}, {self.shift}"
    
    
    

    def __str__(self):
        return f"{self.l_name}, {self.f_name}"

class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE , related_name='attendance')
    date = models.DateTimeField(auto_now_add=True)
    isinstance = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.staff.l_name} - {self.staff.f_name}"
    
    class Meta:
        verbose_name_plural = "StaffAttendance"

class Admins(models.Model):
    img=models.ImageField()
    name=models.CharField(max_length=50)
    
    


  



