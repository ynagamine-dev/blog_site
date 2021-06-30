from django.test import TestCase

from ..models import Article, Tag


# 値が正しいかどうか is_valid()
# 日時が現在時刻になっているかどうか
# titleの文字数を超えるとエラーになるかどうか