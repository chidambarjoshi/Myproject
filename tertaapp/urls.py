from django.urls import path
from . import views


urlpatterns = [
	path('',views.home_user,name="home-user"),
	path('home-user',views.home_user,name="home-user"),
	path('user-admin',views.home,name="user-admin"),
	path('datadisplay',views.getdata,name="datadisplay"),
	path('datadisplay1/<pid>',views.getdata1,name="datadisplay1"),
	#path('genqr/<pid>',views.gen_qrcode,name="genqr"),
	path('datadisplay_user/<pid>',views.getdata_user,name="datadisplay_user"),
	path('login', views.login, name='login'),
	path('logout', views.logout,name='logout'),
	path('about', views.about,name='about'),
	path('about_user', views.about_user,name='about_user'),
	#path('admin_dash', views.admin_dash,name='admin_dash'),
	path('search_pro',views.search_pro,name='search_pro'),

]
