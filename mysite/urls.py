"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path #必須要用re_path才能使用regex
from django.contrib.auth import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('blog.urls')),  #這行是我加的，為了把blog資料夾中的urls導入到這邊的主url裡
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/',views.LogoutView.as_view(), name='logout'), #這行必須加，但還不知道如何運作
    
] 
'''
注意上面的blog.urls要在blog資料夾中建一個相符的urls檔名的.py檔
不能用path要用re_path才能用regex包含所有url符合上面1.2行指定的規則(不然會有"Django tried these URL patterns, in this order:
login/
admin/
The empty path didn’t match any of these."的bug)
'''