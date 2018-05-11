# -*- coding: utf-8 -*-
from apistar import types, validators
from utils.time_util import cur_date_time


class CallBack(types.Type):
    """
    回调表
    """
    name = validators.String(max_length=255, title=u'接口名称', description=u'接口名称')
    url = validators.String(title=u'回调url', description=u'回调url')
    create_time = validators.DateTime(default=cur_date_time(), title=u'创建时间', description=u'创建时间')

    def __str__(self):
        return self.name


class Case(types.Type):
    """
    # 条件表
    """
    name = validators.String(max_length=255, title=u"条件名称")
    desc = validators.String(allow_null=True, title=u'条件描述')
    sql = validators.String(title=u'条件sql')
    no_data_pass = validators.Boolean(default=True, title=u'无数据满足')


