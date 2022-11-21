from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('country/', views.country, name='country'),
    path('country/create_country/', views.create_country, name='create_country'),
    path('country/update_country/<str:cname>/', views.upd_country, name='update_country'),
    path('country/delete_country/<str:cname>/', views.delete_country, name='delete_country'),

    path('diseaseType/', views.dType, name='diseaseType'),
    path('diseaseType/create_dType/', views.create_dType, name='create_dType'),
    path('diseaseType/update_dType/<int:diseasetype_id>/', views.upd_dType, name='update_dType'),
    path('diseaseType/delete_dType/<int:diseasetype_id>/', views.delete_dType, name='delete_dType'),

    path('disease/', views.disease, name='disease'),
    path('disease/create_disease/', views.create_disease, name='create_disease'),
    path('disease/update_disease/<str:disease_code>/', views.upd_disease, name='update_disease'),
    path('disease/delete_disease/<str:disease_code>/', views.delete_disease, name='delete_disease'),

    path('discover/', views.discover, name='discover'),
    path('discover/create_discover/', views.create_discover, name='create_discover'),
    path('discover/update_discover/<str:cname>,<str:disease_code>/', views.upd_discover, name='update_discover'),
    path('discover/delete_discover/<str:cname>,<str:disease_code>/', views.delete_discover, name='delete_discover'),

    path('users/', views.users, name='users'),
    path('users/create_users/', views.create_users, name='create_users'),
    path('users/update_users/<str:email>/', views.upd_users, name='update_users'),
    path('users/delete_users/<str:email>/', views.delete_users, name='delete_users'),

    path('publicservant/', views.publicservant, name='publicservant'),
    path('publicservant/create_publicservant/', views.create_publicservant, name='create_publicservant'),
    path('publicservant/update_publicservant/<str:email>/', views.upd_publicservant, name='update_publicservant'),
    path('publicservant/delete_publicservant/<str:email>/', views.delete_publicservant, name='delete_publicservant'),

    path('doctor/', views.doctor, name='doctor'),
    path('doctor/create_doctor/', views.create_doctor, name='create_doctor'),
    path('doctor/update_doctor/<str:email>/', views.upd_doctor, name='update_doctor'),
    path('doctor/delete_doctor/<str:email>/', views.delete_doctor, name='delete_doctor'),

    path('specialize/', views.specialize, name='specialize'),
    path('specialize/create_specialize/', views.create_specialize, name='create_specialize'),
    path('specialize/delete_specialize/<int:id>/', views.delete_specialize, name='delete_specialize'),

    path('record/', views.record, name='record'),
    path('record/create_record/', views.create_record, name='create_record'),
    path('record/update_record/<int:id>/', views.upd_record, name='update_record'),
    path('record/delete_record/<int:id>/', views.delete_record, name='delete_record')
]
