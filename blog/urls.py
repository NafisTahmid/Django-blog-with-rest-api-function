from django.urls import path, include
from . import views
# FOR api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.BlogCategoryViewSet, basename='category')
router.register(r'blogs', views.BlogViewSet, basename='blogs')
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name="home"),
    path('category/<str:category_slug>', views.category_page, name="category_page"),
    path('<str:blog_slug>', views.blog_details, name="blog_details")
]
