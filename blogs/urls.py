from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='starting_page'),
    path('posts',views.post,name='post_page'),
    path('posts/<slug:slug>',views.single_post,name='page_detail'),
    path('product/',views.list_product),
    path('<slug:slug>', views.details_product)
]