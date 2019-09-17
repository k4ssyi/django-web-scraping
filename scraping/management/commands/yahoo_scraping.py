import logging
import traceback

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from ...models import Content


class Command(BaseCommand):
    help = 'Yahoo News Scraping'

    # はじめに実行される
    def handle(self, *args, **options):
        r = requests.get('https://news.yahoo.co.jp')

        soup = BeautifulSoup(r.content, 'html.parser')

        # ニュース一覧のテキストのみ抽出
        title = soup.find('div', 'newsFeed_item_title').text
        content = soup.find('ul', 'newsFeed_list').text

        # DBへ保存
        try:
            set_content = Content(title=title, content=content)
            set_content.save()
            print('保存完了')
        except IntegrityError:
            print('ユニーク制約')
            logging.error(traceback.format_exc())
