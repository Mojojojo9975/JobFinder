from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from .models import *
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# Create your views here.
categories = {
    "Information Technology": ["software", "developer", "network", "cybersecurity","wordpress","django", "website","internet","computer","data","software","database","information","computing", "informatics", "network", "information system", "system", "electronics", "hardware", "media", "communication", "engineering", "it", "cyber", "knowledge", "computer science", "cyberinformation", "intranet", "data path", "enterprise architecture", "update", "automation", "information theory", "web site", "cybernetics", "cyberspace", "intel", "knowbot", "networks", "create", "programmer","applications", "information science","software", "developer", "network", "cybersecurity", "programming", "coding", "software engineer", "web developer", "system administrator", "data analyst", "database administrator", "IT support", "cloud computing", "DevOps", "artificial intelligence", "machine learning", "mobile app development", "Java", "Python", "C++", "JavaScript", "SQL", "PHP", "Ruby", "HTML", "CSS", "Linux", "Windows", "Docker", "Kubernetes", "network security", "penetration testing", "ethical hacking", "data science", "software development", "front-end development", "back-end development", "full-stack development", "software architecture", "software testing", "computer science"],


    "Healthcare and Medicine": ["doctor", "nurse", "pharmacist", "medical","psychologist","healthcare", "physician", "surgeon", "dentist", "radiologist", "laboratory technician", "medical researcher", "healthcare administrator", "patient care", "medical assistant", "clinical research", "healthcare management", "pharmacy technician", "pharmaceutical", "healthcare technology", "medical imaging", "healthcare policy", "emergency medicine", "pediatrician", "geriatrics", "cardiology", "oncology", "nursing", "obstetrics", "orthopedics", "neurology", "psychiatry", "healthcare informatics", "medical ethics","patient"],

    "Business and Management": ["manager", "analyst", "marketing", "finance", "business", "management", "project manager", "business analyst", "financial analyst", "marketing manager", "sales", "human resources", "HR", "operations", "supply chain", "logistics", "business development", "entrepreneurship", "consulting", "strategy", "market research", "data analysis", "business administration", "MBA", "leadership", "accounting", "corporate finance", "budgeting", "risk management", "advertising", "public relations", "product management","advisor"],

    "Education": ["teacher", "professor", "curriculum", "education", "educator", "teaching", "instructor", "pedagogy", "e-learning", "online education", "special education", "classroom management", "school administration", "curriculum development", "education technology", "instructional design", "educational psychology", "early childhood education", "higher education", "educational leadership", "school counselor", "academic advisor", "educational research", "educational assessment", "student services"],

    "Engineering and Manufacturing": ["engineer", "manufacturing", "production", "mechanical engineer", "electrical engineer", "civil engineer", "chemical engineer", "aerospace engineer", "industrial engineer", "quality control", "manufacturing technician", "process engineer", "automotive manufacturing", "product design", "materials engineering", "automation", "robotics", "3D printing", "CAD", "CNC machining", "production planning", "lean manufacturing", "industrial automation", "continuous improvement", "product development", "aerospace manufacturing", "automotive engineering"]
}

def categorize_job(job_description):
    for category, keywords in categories.items():
        if any(keyword in job_description.lower() for keyword in keywords):
            return category
    return "-"





#-----------------------------------------------------------------------------------------------------------------------
def index(request):
    if request.method=="POST":
        Username_login=request.POST.get("Username")
        Password_login=request.POST.get("Password")
        user= authenticate(request,username=Username_login,password=Password_login)
        if user is not None:
            login(request,user)
            return redirect("home")
        
        else:
            return render(request,"index.html")
    return render(request,"index.html")

def home(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,"home.html")





from datetime import datetime, timedelta

@login_required
def dashboard(request):
    
    user = request.user
    jobs_clicked = ClickHistory.objects.filter(user=user)

    # Retrieve clicked jobs in the last week
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    clicked_jobs_past_week = ClickHistory.objects.filter(
        user=user, date_clicked__range=(start_date, end_date)
    ).select_related('job')

    # Prepare data for the graph
    categories = set(job.job.category for job in clicked_jobs_past_week)
    category_click_counts = [
        (category, ClickHistory.objects.filter(job__category=category).count())
        for category in categories
    ]

    context = {
        'categories': [category for category, _ in category_click_counts],
        'click_counts': [count for _, count in category_click_counts],
        'jobs_clicked': jobs_clicked,
    }

    return render(request, 'dashboard.html', context)

@login_required
def userLogout(request):
    logout(request)
    return redirect("/")

def userRegistration(request):
    if request.method=="POST":
        Username=request.POST.get("Username") 
        Password=request.POST.get("Password")
        ConfirmPassword=request.POST.get("ConfirmPassword")

        if Password!=ConfirmPassword:
            messages.warning(request, "Password does not match.")
            return render(request,"registration.html")
        elif len(Password)<8:
            messages.warning(request, "Password should be atleast 8 characters")
            return render(request,"registration.html")
        elif User.objects.filter(username=Username).exists():
            messages.warning(request, "Username already taken")
            return render(request,"registration.html")
    
        else:
            myUser=User.objects.create_user(Username,password=Password)
            myUser.save()
            return redirect("/")


    else:
        return render(request,"registration.html")
        
   


@login_required
def profile(request):
    if request.method == 'POST':
        
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'{request.user.username},Your account has been updated!')
            return redirect('profile') 


           
            
    else:
        
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        
        'p_form': p_form
    }

    return render(request, 'profile.html', context)


@login_required
def update_profile(request):
    if request.method=="POST":
        
        name=request.POST.get("name")
        profession=request.POST.get("profession")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        

        
        Profile.objects.filter(user_id=request.user.id).update(name=name,profession=profession,email=email,phone=phone,address=address)
        messages.success(request, "Profile details updated.")
        return render(request,"update_profile.html")
       
        
        
        

    else:
        return render(request,"update_profile.html")
    


@login_required
def save_job(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    user = request.user

    if user in job.users_saved.all():
        job.users_saved.remove(user)
    else:
        job.users_saved.add(user)

    job.save()

    return redirect('allJobs')



@login_required
def saved_jobs(request):
    saved_jobs = request.user.profile.get_saved_jobs()
    return render(request, 'saved_jobs.html', {'saved_jobs': saved_jobs})

from django.shortcuts import get_object_or_404

@login_required
def delete_saved_job(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    user = request.user

    if user in job.users_saved.all():
        job.users_saved.remove(user)
        messages.success(request, f'Job "{job.job_title}" has been removed from your saved jobs.')
    else:
        messages.error(request, f'Job "{job.job_title}" was not in your saved jobs.')

    return redirect('profile')


@login_required
def toggle_save(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    user = request.user

    if user in job.users_saved.all():
        job.users_saved.remove(user)
    else:
        job.users_saved.add(user)

    job.save()
    messages.success(request, f'Job "{job.job_title}" has been saved/unsaved.')

    return HttpResponse(status=200)


@login_required
def click_apply_now(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    user = request.user

    job.is_clicked = True
    job.save()

    ClickHistory.objects.create(user=user, job=job)

    return HttpResponse(status=200)

def allJobs(request):
    jobs=Jobs.objects.all()
    user = request.user



    if request.method == 'POST':
            action = request.POST.get('action', None)
            job_id = request.POST.get('job_id', None)

            if action and job_id:
                job = Jobs.objects.get(pk=job_id)
                user = request.user

                if action == 'save':
                    if user in job.users_saved.all():
                        job.users_saved.remove(user)
                    else:
                        job.users_saved.add(user)
                elif action == 'apply_now':
                    job.is_clicked = True
                    job.save()

                    ClickHistory.objects.create(user=user, job=job)


    for job in jobs:
        category = categorize_job(job.job_title)
        job.category = category
        job.save()


   


    for item in jobs:
        if item.salary == 0.0:
            item.salary = "-"
    params={"jobs":jobs , "user": user}
    return render(request,"allJobs.html",params)




def scholarships(request):
    scholarships=Scholarships.objects.all()
    total_scholarships= len(scholarships)
   
    params={"scholarships":scholarships ,"total_scholarships":total_scholarships, }
    return render(request,"scholarships.html",params)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@login_required
def my_jobs(request):
    user = request.user

    # Get click history for the user
    click_history = ClickHistory.objects.filter(user=user)
    clicked_job_ids = click_history.values_list('job__job_id', flat=True)
    clicked_jobs = Jobs.objects.filter(job_id__in=clicked_job_ids)

    # Print clicked_jobs for debugging
    print("Clicked Jobs:", clicked_jobs)

    # Create a DataFrame from the click history
    click_history_df = pd.DataFrame(list(click_history.values('user_id', 'job__job_title', 'job_id')))

    # Pivot the DataFrame to get a user-job title matrix
    user_title_matrix = click_history_df.pivot_table(index='user_id', columns='job__job_title', values='job_id', aggfunc=len, fill_value=0)

    # If there are no titles, return an empty list of recommended jobs
    recommended_jobs_details = []

    if not user_title_matrix.empty:
        # Initialize a CountVectorizer
        count_vectorizer = CountVectorizer(stop_words='english')

        # Fit and transform the vectorizer on the job titles
        count_matrix = count_vectorizer.fit_transform(clicked_jobs.values_list('job_title', flat=True))

        # Compute the cosine similarity between user click history and job titles
        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        # Print the cosine similarity matrix for debugging
        print("Cosine Similarity Matrix:", cosine_sim)

        # Get the user's index in the similarity matrix
        user_index = user.id

        # Ensure the user index is within bounds
        if user_index < cosine_sim.shape[0]:
            # Get the similarity scores for the user
            user_similarity_scores = cosine_sim[user_index]

            # Print the user similarity scores for debugging
            print("User Similarity Scores:", user_similarity_scores)

            # Get the indices of jobs sorted by similarity scores
            sorted_job_indices = user_similarity_scores.argsort()[::-1]

            # Get the job IDs of recommended jobs
            recommended_jobs_ids = [Jobs.objects.values_list('job_id', flat=True)[index] for index in sorted_job_indices.tolist()]

            # Get details of recommended jobs
            recommended_jobs_details = Jobs.objects.filter(job_id__in=recommended_jobs_ids)

            # Print recommended_jobs_details for debugging
            print("Recommended Jobs Details:", recommended_jobs_details)

    context = {'recommended_jobs': recommended_jobs_details}

    return render(request, 'myJobs.html', context)