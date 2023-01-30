from django.urls import path

from home import views


urlpatterns = [
    path('', views.index,name='index'),
    path('student_registration',views.student_registration,name='student_registration'),
    path('admin_registration',views.admin_registration,name='admin_registration'),
    path('login_user',views.login_user,name='login_user'),
    path('admin_profile',views.admin_profile,name='admin_profile'),
    path('admin_view_students',views.admin_view_students,name='admin_view_students'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('student_viewprofile',views.student_viewprofile,name='student_viewprofile'),
    path('student_updateprofile',views.student_updateprofile,name='student_updateprofile'),
    path('delete_profile_student',views.delete_profile_student,name='delete_profile_student'),
    path('admin_add_marks',views.admin_add_marks,name='admin_add_marks'),
    path('admin_view_marks',views.admin_view_marks,name='admin_view_marks'),
    path('student_view_marks',views.student_view_marks,name='student_view_marks'),
    path('admin_edit_marks/<int:id>/', views.admin_edit_marks, name='admin_edit_marks'),

]
