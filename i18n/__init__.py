import json
import locale
import os

LOCALE_DIR = os.path.dirname(__file__)
_cache = {}

def _detect_lang():
    try:
        lang = locale.getdefaultlocale()[0]
        if lang:
            lang = lang.split('_')[0]
            if lang in ('zh', 'en'):
                return lang
    except Exception:
        pass
    return 'zh'

def load(lang=None):
    if lang is None:
        lang = _detect_lang()
    if lang in _cache:
        return _cache[lang]
    path = os.path.join(LOCALE_DIR, f'{lang}.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            _cache[lang] = json.load(f)
    except FileNotFoundError:
        path = os.path.join(LOCALE_DIR, 'zh.json')
        with open(path, 'r', encoding='utf-8') as f:
            _cache[lang] = json.load(f)
    return _cache[lang]

class T:
    def __init__(self, lang=None):
        self._data = load(lang)

    def __call__(self, key, **kwargs):
        text = self._data.get(key, key)
        if kwargs:
            text = text.format(**kwargs)
        return text

    def get(self, key, **kwargs):
        return self.__call__(key, **kwargs)


_t_instance = None

def get_t(lang=None):
    global _t_instance
    if _t_instance is None or lang is not None:
        _t_instance = T(lang)
    return _t_instance
