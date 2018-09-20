# -*- encoding: utf-8 -*-

import os

import django


def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()
