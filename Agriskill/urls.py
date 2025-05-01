from django.template.context_processors import static
from django.urls import path
from numpy.f2py.crackfortran import namepattern
from . import views  # Import views from the current app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('role-selection/', views.role_selection, name='role_selection'),  # Role Selection
    path('signup/skilled-professional/', views.skilled_professional_signup, name='skilled_professional_signup'),  # Skilled Professional Signup
    path('signup/landowner/', views.landowner_signup, name='landowner_signup'),  # Landowner Signup
    path('skilled-professional/', views.skilled_professional_home, name='skilled_professional_home'),  # Skilled Professional Home
    path('job-listings/', views.job_listings, name='job_listings'),  # Job Listings
    path('user-messages/', views.user_messages, name='user_messages'),  # User Messages
    path('settings/', views.settings, name='settings'),  # User Settings
    path('landowner-home/', views.landowner_home, name='landowner_home'),  # Landowner Home
    path('select-professional/<int:id>/', views.select_professional, name='select_professional'),  # Select Professional
    path('update-work-location/', views.update_work_location, name='update_work_location'),  # Update Work Location
    path('logout/', views.custom_logout, name='logout'),  # Logout
    path('profile/', views.profile, name='profile'),
    path('matched_professionals/', views.matched_professionals, name='matched_professionals'),
    path('professional/<str:professional_name>/', views.landowner_results, name='landowner_results'),
    path('matched_landowners/', views.matched_landowners, name='matched_landowners'),
    path('skillshare/', views.skillshare_view, name='skillshare_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)