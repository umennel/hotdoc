import os
from urllib.request import pathname2url
from bs4 import BeautifulSoup
import cssutils


def inline_css(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('link'):
        if "stylesheet" not in link.get('rel'):
            continue

        href = link.get('href')
        if not href.startswith('http'):
            href = 'file://' + pathname2url(os.path.abspath(href))

        sheet = cssutils.parseUrl(href, validate=False)
            
        style_tag = soup.new_tag("style", type="text/css")

        style_tag.string = sheet.cssText.decode(sheet.encoding)
        link.replace_with(style_tag)

    return str(soup)