"""
FDC API data fetching module.
"""


from typing import Any
from httpx import (
    AsyncClient,
    ConnectError,
    ConnectTimeout,
)

from .configuration import get_fdc_config


def get_link_from_url_text(url, search_text):
    """
    Находит ссылку по тексту на странице
    """
    try:
        # Отправляем запрос к странице
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        
        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем все ссылки с нужным текстом
        links = soup.find_all('a', string=lambda text: text and search_text in text)
        
        if not links:
            print(f"Ссылка с текстом '{search_text}' не найдена")
            return None
        
        # Берем первую найденную ссылку
        first_link = links[0]
        href = first_link.get('href')
        
        # Если ссылка относительная, преобразуем в абсолютную
        if href and href.startswith('/'):
            from urllib.parse import urljoin
            href = urljoin(url, href)
        
        print(f"Найдена ссылка: {href}")
        return href
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return None