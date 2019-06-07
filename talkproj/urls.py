"""talkproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import talk.api_views

urlpatterns = [
  path('api/v1/talks/', talk.api_views.TalkList.as_view()),
  path('api/v1/talks/new', talk.api_views.TalkCreate.as_view()),
  path('api/v1/talks/<int:id>/',
       talk.api_views.TalkRetrieveUpdateDestroy.as_view()
       ),
  # path('api/v1/talks/<int:id>/stats',
  #      talk.api_views.TalkStats.as_view(),
  #      ),

  path('admin/', admin.site.urls),
  # path('products/<int:id>/', talk.views.show, name='show-product'),
  # path('cart/', talk.views.cart, name='shopping-cart'),
  # path('', talk.views.index, name='list-products'),
]
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
