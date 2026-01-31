from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.http import HttpResponse
import traceback

def test_template(request, template_name):
    """Тестовый view для проверки шаблонов"""
    try:
        from django.template.loader import get_template
        template = get_template(template_name)
        return HttpResponse(f"Шаблон найден: {template_name}")
    except Exception as e:
        return HttpResponse(f"ОШИБКА: {e}<br><br>{traceback.format_exc()}")
urlpatterns = [
    path('test/account/', test_template, {'template_name': 'account.html'}),
    path('test/admin-products/', test_template, {'template_name': 'admin/products.html'}),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('', include('products.urls')),

    # Статические страницы
    path('account/', views.static_page, {'page_name': 'account'}, name='account'),
    path('cart/', views.static_page, {'page_name': 'cart'}, name='cart'),
    path('checkout/', views.static_page, {'page_name': 'checkout'}, name='checkout'),
    path('login/', views.static_page, {'page_name': 'login'}, name='login'),
    path('register/', views.static_page, {'page_name': 'register'}, name='register'),
    path('forgot-password/', views.static_page, {'page_name': 'forgot-password'}, name='forgot_password'),
    path('guides-recipes/', views.static_page, {'page_name': 'guides-recipes'}, name='guides_recipes'),

    # Admin pages
    path('admin-panel/products/', views.static_page, {'page_name': 'admin/products'}, name='admin_products'),
    path('admin-panel/dashboard/', views.static_page, {'page_name': 'admin/dashboard'}, name='admin_dashboard'),
    path('admin-panel/add/', views.static_page, {'page_name': 'admin/add'}, name='admin_add'),

    # Product pages
    path('product/citra-hops/', views.static_page, {'page_name': 'product-citra-hops'}, name='product_citra'),
    path('product/maris-otter-malt/', views.static_page, {'page_name': 'product-maris-otter-malt'},
         name='product_maris'),
    path('product/safale-us05-yeast/', views.static_page, {'page_name': 'product-safale-us05-yeast'},
         name='product_safale'),
    path('product/cascade-hops/', views.static_page, {'page_name': 'product-cascade-hops'}, name='product_cascade'),
    path('product/caramel-malt/', views.static_page, {'page_name': 'product-caramel-malt'}, name='product_caramel'),
    path('product/saaz-hops/', views.static_page, {'page_name': 'product-saaz-hops'}, name='product_saaz'),
    path('product/pilsner-malt/', views.static_page, {'page_name': 'product-pilsner-malt'}, name='product_pilsner'),
    path('product/imperial-yeast/', views.static_page, {'page_name': 'product-imperial-yeast'},
         name='product_imperial'),
    path('product/centennial-hops/', views.static_page, {'page_name': 'product-centennial-hops'},
         name='product_centennial'),
    path('product/mosaic-hops/', views.static_page, {'page_name': 'product-mosaic-hops'}, name='product_mosaic'),
    path('product/west-coast-ipa-kit/', views.static_page, {'page_name': 'product-west-coast-ipa-kit'},
         name='product_west_coast'),
    path('product/unmalted-wheat/', views.static_page, {'page_name': 'product-unmalted-wheat'},
         name='product_unmalted'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)