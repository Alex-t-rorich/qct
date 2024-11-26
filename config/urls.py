# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include(apps.get_app_config('oscar').urls[0])),
    
    path('dashboard/', include((apps.get_app_config('dashboard').urls[0], 'dashboard'))),
    path('dashboard/catalogue/', include((apps.get_app_config('catalogue_dashboard').urls[0], 'catalogue-dashboard'))),
    path('dashboard/orders/', include((apps.get_app_config('orders_dashboard').urls[0], 'orders-dashboard'))),
    path('dashboard/reports/', include((apps.get_app_config('reports_dashboard').urls[0], 'reports-dashboard'))),
    path('dashboard/users/', include((apps.get_app_config('users_dashboard').urls[0], 'users-dashboard'))),
    path('dashboard/pages/', include((apps.get_app_config('pages_dashboard').urls[0], 'pages-dashboard'))),
    path('dashboard/partners/', include((apps.get_app_config('partners_dashboard').urls[0], 'partners-dashboard'))),
    path('dashboard/offers/', include((apps.get_app_config('offers_dashboard').urls[0], 'offers-dashboard'))),
    path('dashboard/ranges/', include((apps.get_app_config('ranges_dashboard').urls[0], 'ranges-dashboard'))),
    path('dashboard/reviews/', include((apps.get_app_config('reviews_dashboard').urls[0], 'reviews-dashboard'))),
    path('dashboard/vouchers/', include((apps.get_app_config('vouchers_dashboard').urls[0], 'vouchers-dashboard'))),
    path('dashboard/comms/', include((apps.get_app_config('communications_dashboard').urls[0], 'comms-dashboard'))),
    path('dashboard/shipping/', include((apps.get_app_config('shipping_dashboard').urls[0], 'shipping-dashboard'))),
    
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)