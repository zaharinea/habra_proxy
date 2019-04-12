from proxy.common import UrlReplace
from proxy.utils import convert_words, processing_text


def test_convert_text():
    text = """Сейчас на фоне уязвимости Logjam все в индустрии в очередной раз обсуждают
проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы
поговорить об одной из них, а именно — о настройке ciphersiutes. Вот ниже его позвали, ждемс."""

    expected = """Сейчас™ на фоне уязвимости Logjam™ все в индустрии в очередной раз обсуждают
проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы
поговорить об одной из них, а именно™ — о настройке ciphersiutes. Вот ниже его позвали, ждемс."""

    assert convert_words(text) == expected


def test_processing_text(html, get_expected_soup):
    expected_soup, _ = get_expected_soup
    urls = [
        UrlReplace("https://habr.com/", "http://localhost:8000/"),
        UrlReplace("http://habrahabr.ru/", "http://localhost:8000/"),
        UrlReplace("https://habrahabr.ru/", "http://localhost:8000/"),
    ]

    result = processing_text(data=html, urls=urls)
    assert result == str(expected_soup)
