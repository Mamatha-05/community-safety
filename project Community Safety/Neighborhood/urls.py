from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('Admin',views.admin_login_view,name='Admin'),
    path('dashboard',views.dashboard_view,name='dashboard'),
    path('Register',views.Register_view,name='register'),
    path('instruction-pass',views.instruction,name='Instruction'),
    path('Add-instruction',views.New_instruction,name='Add_Instruction'),
    path('Raising-report',views.report,name='Report'),
    path('delete-report/<int:pk>/',views.delete_report,name="Delete_report")
]