# from django.urls import path, include

# from django.contrib import admin
# from django.conf.urls import url, include
# admin.autodiscover()

# import hello

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

# urlpatterns = [
#      path("", hello.views.index, name="index"),
#     #  path("db/", hello.views.db, name="db"),
#     # path("admin/", admin.site.urls),
#     url(r'^admin/', admin.site.urls),
#     # url('', include('django_mako_plus.urls')),
# ]

# original Django 
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
#ifat = __import__(infinite-atoll-72014)
from tutorial import views

admin.autodiscover()

import hello.views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
