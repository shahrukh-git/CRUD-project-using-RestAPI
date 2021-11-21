from django import urls
from django.contrib import admin
from django.urls import path, include
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAddShowView.as_view(), name="addandshow"),
    path('<int:id>/', views.UserUpdateDelete.as_view(), name="updatedata"),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name="deletedata"),
    path('api/', include('enroll.api.urls'))
]