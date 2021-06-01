from django.urls import include, path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
	path('',views.home, name='home'),
	path('index',views.index, name='index'),
	path('all_appo',views.all_appo, name='all_appo'),
	path('all_contact',views.all_contact, name='all_contact'),
	path('count_appo',views.count_appo, name='count_appo'),
	path('email_count',views.email_count, name='email_count'),
	path('department_doc',views.department_doc, name='department_doc'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('post_collection/', views.post_collection,name='post_collection'),
    path('post_element/<int:pk>', views.post_element,),

]