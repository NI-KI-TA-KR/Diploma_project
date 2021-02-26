from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:resume_id>/', views.detail_resume, name='detail_resume'),
    path('<int:resume_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)