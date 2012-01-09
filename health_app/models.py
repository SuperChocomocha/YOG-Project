from django.db import models
import datetime

# Create your models here.

class Personal_Data(models.Model):
    acc_id = models.AutoField(primary_key = True)
    # acc_id = models.IntegerField()
    email_addr = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30)
    time_modified = models.DateTimeField('Modified Time')
    gender = models.CharField(max_length = 1)
    age = models.IntegerField()
    race = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return "This is account number " + str(self.acc_id)
        # decide what this is later

class Health_Data(models.Model):
    acc= models.ForeignKey(Personal_Data)
    heart_rate = models.IntegerField()
    bp_lo = models.IntegerField()
    bp_hi = models.IntegerField()
    time_modified = models.DateTimeField('Modified Time')
    # time_modified = models.ForeignKey(Personal_Data)

    def __unicode__(self):
        return "Health Data"
        # make this unique later

class Health_Info(models.Model):
    hr = models.CharField(max_length = 200) # check maximum length char field
    bp = models.CharField(max_length = 200)

    def __unicode__(self):
        return hr + str('\n') + bp
        # change later

class Dynamic_Info(models.Model):
    pass

    def __unicode__(self):
        pass
    # add dynamic info on heart rate or blood pressure depending on
    # user input, for example: heart rate is too high, avg heart rate
    # for your age/gender/ethnicity is ____

