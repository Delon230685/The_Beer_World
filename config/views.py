from django.shortcuts import render
from django.http import Http404
import os
from django.shortcuts import render
from django.http import HttpResponse
import traceback


def static_page(request, page_name):
    """
    Диагностическая версия
    """
    # Логируем запрос
    print(f"DEBUG: Request for page: {page_name}")

    try:
        # Пробуем рендерить
        response = render(request, f'{page_name}.html')
        print(f"DEBUG: Successfully rendered: {page_name}.html")
        return response
    except Exception as e:
        # Возвращаем детальную ошибку
        error_details = f"""
        <h1>Ошибка при рендеринге шаблона</h1>
        <p><strong>Шаблон:</strong> {page_name}.html</p>
        <p><strong>Ошибка:</strong> {e}</p>
        <pre>{traceback.format_exc()}</pre>
        """
        return HttpResponse(error_details)

def static_page(request, page_name):
    """
    Динамический view для всех статических страниц
    """
    # Базовый список разрешенных страниц - ДОБАВЬТЕ admin файлы
    allowed_pages = [
        'account', 'cart', 'checkout', 'login', 'register',
        'forgot-password', 'guides-recipes',
        # admin pages - ЭТИ ФАЙЛЫ В ПАПКЕ admin/
        'admin/add', 'admin/dashboard', 'admin/products',  # ← ИЗМЕНИТЕ ПУТИ!
        # product pages
        'product-citra-hops', 'product-maris-otter-malt',
        'product-safale-us05-yeast', 'product-cascade-hops',
        'product-caramel-malt', 'product-saaz-hops', 'product-pilsner-malt',
        'product-imperial-yeast', 'product-centennial-hops', 'product-mosaic-hops',
        'product-west-coast-ipa-kit', 'product-unmalted-wheat'
    ]

    # Проверяем существование файла
    template_path = os.path.join('templates', f'{page_name}.html')

    if not os.path.exists(template_path) and page_name not in allowed_pages:
        raise Http404(f"Страница {page_name} не найдена")

    return render(request, f'{page_name}.html')