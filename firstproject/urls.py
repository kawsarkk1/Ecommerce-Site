from django.contrib import admin
from django.urls import path,include

from firstproject import simpleviews

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('firstapp/',include('firstapp.urls')),
    path('product/',include('product.urls')),
    path('crudapp/', include('crudapp.urls')),
    path('category/',include('category.urls')),
    path('',simpleviews.htmlPage,name='html_page2'),
]
