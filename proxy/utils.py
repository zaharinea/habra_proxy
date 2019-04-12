from typing import List

from bs4 import BeautifulSoup, element

from .common import UrlReplace

WORD_LEN = 6


def convert_words(data: str) -> str:
    words = []
    for word in data.split(" "):
        if len(word) == WORD_LEN and word.isalpha():
            words.append(f"{word}™")
        else:
            words.append(word)

    return " ".join(words)


def html_dom_walker(soup: BeautifulSoup) -> None:
    if soup.name is None:
        return
    for child in soup.children:
        if all(
            [
                isinstance(child, element.NavigableString),
                not isinstance(child, element.Comment),
            ]
        ):
            child.replace_with(convert_words(child.string))
        html_dom_walker(child)


def processing_text(data: str, urls: List[UrlReplace]) -> str:
    for url in urls:
        data = data.replace(url.src, url.dst)

    soup = BeautifulSoup(data, "html.parser")
    html_dom_walker(soup.body)

    return str(soup)
