"""statistic_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from dashboard.views import ChartData, company_article_list, dash, dash_ajax

urlpatterns = [
    path("admin/", admin.site.urls),
    # dashboard
    path('companies/', company_article_list, name='companies'),
    path('api/chart/data/', ChartData.as_view(), name='api-chart-data'),
    path('dash/', dash),
    path('_dash', dash_ajax),
    # path to djoser and points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("api/account/", include("account.urls")),
]
