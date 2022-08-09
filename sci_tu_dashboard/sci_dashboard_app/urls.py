from django.urls import path, include, re_path
from . import views, view_staff, view_chief, view_admin
from sci_dashboard_app.dash_apps import simpleexsample
from django.conf.urls import url


urlpatterns = [  

    path('admin_home/', view_admin.home, name = 'admin_home'),
    path('staff_home/', view_staff.home, name = 'staff_home'),
    path('chief_home/', view_chief.home, name = 'chief_home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    # path('dashboard/(?P<start_date>[0-9][\w-]+)/(?P<end_date>[0-9][\w-]+)/$', views.dashboard, name = 'dashboard'),
    url(r'^dashboard/(?P<start_date>[0-9][\w-]+)/(?P<end_date>[0-9][\w-]+)/$', views.dashboard, name = 'dashboard'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('report/by-status/', views.reportbystatus, name = 'reportbystatus'),
    path('report/by-status/start', views.start, name = 'start'),
    path('report/by-status/success', views.success, name = 'success'),
    path('report/by-status/pending', views.pending, name = 'pending'),
    path('report/by-status/received', views.received, name = 'received'),
    path('report/by-location/', views.reportbylocation, name = 'reportbylocation'),
    path('report/by-location/<int:building_id>/', views.location, name = 'location'),
    path('report/by-location/<int:building_id>/type-<int:type_id>', views.locationtype, name = 'locationtype'),
    path('detailofficer/<int:pk>', views.detailofficer, name = 'detailofficer'),
    path('roomcaretaker/', views.roomcaretaker, name = 'roomcaretaker'),
    path('ITstaff/', views.ITstaff, name = 'ITstaff'),
    path('maintenance/', views.maintenance, name = 'maintenance'),
    path('supervisor/', views.supervisor, name = 'supervisor'),
    path('manager-view/', views.managerview, name = 'manager-view'),
    path('detailofficer/edit-profile/<str:pk>', views.editProfile, name = 'edit-profile'),
    path('board-manager-view/', views.boardmanager, name = 'boardmanager'),
   
]