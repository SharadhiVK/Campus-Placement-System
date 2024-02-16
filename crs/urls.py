
from django.contrib import admin
from django.urls import path ,include
#from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', include('campus.urls')),
    # path('student/student_register/', include('campus.urls')),
    # path('student/student_login/',include('campus.urls')),
    # path('dept/dept_register/', include('campus.urls')),
    # path('dept/dept_login/',include('campus.urls')),
    # path('student/student_login/usd/',include('campus.urls')),
    # path('logout/',include('campus.urls')),
    # path('student/student_login/dispstu/', include('campus.urls')),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='campus/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="campus/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='campus/password/password_reset_complete.html'), name='password_reset_complete'),      
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)