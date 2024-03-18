from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.index,name="index"),
    path("home/",views.home,name="home"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("registration/",views.userRegistration,name="userRegistration"),
    path("profile/",views.profile,name="profile"),
    path("logout/",views.userLogout,name="userLogout"),
    path("update_profile/",views.update_profile,name="update_profile"),
    path("home/allJobs",views.allJobs,name="allJobs"),
    path("home/scholarships",views.scholarships,name="scholarships"),
    path("save_job/<int:job_id>", views.save_job, name="save_job"),
    path("toggle_save/<int:job_id>", views.toggle_save, name="toggle_save"),
    path('saved_jobs/', views.saved_jobs, name='saved_jobs'),
    path('log_click/<int:job_id>/', views.click_apply_now, name='log_click'),
    path('delete_saved_job/<int:job_id>/', views.delete_saved_job, name='delete_saved_job'),
    path("home/myJobs",views.my_jobs,name="myJobs"),



]