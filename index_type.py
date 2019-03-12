# -*- coding: utf-8 -*-
from enum import Enum
_author_ = 'luwt'
_date_ = '2019/2/15 18:26'


class IndexType(Enum):
    PRI = '主键'
    MUL = '复合索引'
    UNI = '唯一索引'
    FUL = '全文索引'
