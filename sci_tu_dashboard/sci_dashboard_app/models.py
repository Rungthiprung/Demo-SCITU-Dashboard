from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50)
    local_user =  models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    dob = models.DateField(null=True)
    image = models.ImageField(blank=True, upload_to='userprofile', null=True)
    Role = [
        ('Ad', 'Admin'),
        ('It', 'IT staff'),
        ('Mt', 'Maintenance'),
        ('Mg', 'Manager'),
        ('Rc', 'Room caretaker'),
        ('Sv', 'Supervisor')
    ]
    role = models.CharField(max_length=2, choices=Role)

    def __str__(self):
        return "{}-{}".format(self.firstname, self.lastname)

class Building(models.Model):
    shortname = models.CharField(max_length=30)
    fullname = models.CharField(max_length=30)

    def __str__(self):
        return self.shortname

class Room(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    level = models.IntegerField()
    caretaker = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    RoomType = [
        ('Cr', 'Class room'),
        ('Mr', 'Meeting room'),
        ('Os', 'Office space'),
        ('Oth', 'Other')
    ]
    room_type = models.CharField(max_length=30, choices=RoomType)

    def __str__(self):
        return "{}-{}".format(self.building, self.name)

class ReportType(models.Model):
    reportType = models.CharField(max_length=30)
    labels = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.reportType

class Report(models.Model):
    reportID = models.CharField(max_length=30)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.CharField(max_length=100, null=True)
    takecareBy = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    creatorname = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add= True)
    StatusReport = [
        ('S','success'),
        ('R','received'),
        ('P','pending'),
        ('St','start')
    ]
    statusReport  = models.CharField(max_length=50, choices=StatusReport)
    description = models.TextField(null=True)
    image = models.TextField(null=True)
    type = models.ForeignKey(ReportType, on_delete=models.CASCADE, null=True)
    lastModified = models.DateTimeField(auto_now= True, null=True)

    def __str__(self):
        return self.reportID

