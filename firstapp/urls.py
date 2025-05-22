from django.urls import path
from . import views
from .kawsar import new
#from .templates import

urlpatterns=[
    path('',views.index,name='index'),
    path('data-access2',views.dataRender2,name='index'),
    path('khans',new.khan,name='khan'),
    path('html1',views.htmlPage,name='html_page2'),
    path('html2',views.htmlPage1,name='ecom'),
]