# -*- coding: utf-8 -*-
from datetime import datetime


DATE_FMT = "%Y-%m-%d"
TIME_FMT = "%H:%M:%S"
DATETIME_FMT = "%Y-%m-%d %H:%M:%S"


def cur_date(fmt=DATE_FMT):
    return datetime.now().strftime(fmt)


def cur_time(fmt=TIME_FMT):
    return datetime.now().strftime(fmt)


def cur_date_time(fmt=DATETIME_FMT):
    return datetime.now().strftime(fmt)

