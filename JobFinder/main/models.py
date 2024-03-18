from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db import IntegrityError
# Create your models here.


class Jobs(models.Model):
    users_saved = models.ManyToManyField(User, related_name='saved_jobs', blank=True)
    users_clicked = models.ManyToManyField(User, related_name='clicked_jobs', blank=True)
    is_clicked = models.BooleanField(default=False)

    job_id = models.BigAutoField(primary_key=True)
    job_title=models.CharField(max_length=70)
    job_description=models.TextField()
    company=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=8, decimal_places=2)
    publish_date=models.CharField(max_length=20)
    location=models.CharField(max_length=150)
    category=models.CharField(default="-",max_length=150)
    url=models.CharField( max_length=400)

    @property
    def click_count_last_week(self):
        return self.click_history.filter(date_clicked__gte=timezone.now() - timedelta(days=7)).count()

    @property
    def is_saved_by_user(self, user):
        return user in self.users_saved.all()

    @property
    def click_history(self):
        return ClickHistory.objects.filter(job=self)

    def save(self, *args, **kwargs):
        if self.is_clicked:
            for user in self.users_saved.all():
                try:
                    ClickHistory.objects.create(user=user, job=self)
                except IntegrityError:
                    # This exception will be raised if the entry already exists
                    pass
        super(Jobs, self).save(*args, **kwargs)

    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ['-publish_date']
        verbose_name_plural = "Jobs"

#User Profile
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profession=models.CharField(default="xyz",max_length=50)
    name=models.CharField(default="xyz",max_length=30)
    email=models.CharField(default="xyz@abc.com",max_length=70)
    phone=models.CharField(default="12345678",max_length=13)
    address=models.CharField(default="xyz",max_length=100)
    profileImage=models.ImageField(default="default.jpg",upload_to='profilePics',null=True,blank=True)
    
    
    def get_saved_jobs(self):
        return Jobs.objects.filter(users_saved=self.user)

    def get_clicked_jobs(self):
        return Jobs.objects.filter(users_clicked=self.user, is_clicked=True)

    def __str__(self):
        return self.user.username


class ClickHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey('Jobs', on_delete=models.CASCADE)
    date_clicked = models.DateTimeField(auto_now_add=True)

class Scholarships(models.Model):
    scholarship_id = models.BigAutoField(primary_key=True)
    university=models.CharField(max_length=70)
    scholarship_title=models.CharField(max_length=70)
    deadline=models.CharField(max_length=70)
    country=models.CharField(max_length=50)
    degree=models.CharField(max_length=30)
    course_start=models.CharField(max_length=70)
    url=models.CharField( max_length=400)








