# -*- coding: utf-8 -*-
"""
所有用到的常量
"""
import os

_author_ = 'luwt'
_date_ = '2020/10/27 10:50'

# 模板文档文件路径
TEMPLATE_DOCX_PATH = os.path.join(os.path.abspath('.'), 'static\\template_docx\\default.docx')
# 查询数据库列表
QUERY_DB_SQL = 'show databases;'

# 查询数据库中的表名sql
QUERY_TABLES_SQL = 'show tables;'

# 查询系统表sql
QUERY_SYS_TB = 'select column_name, data_type, column_key, column_comment from information_schema.columns'
# 查询系统表和列sql
QUERY_SYS_TB_COL = 'select column_name, table_name from information_schema.columns'
# 从系统库查询tables表
SCHEMA_TABLES_SQL = "SELECT table_name, table_comment from information_schema.`TABLES`"
# 从系统库查询column表
SCHEMA_COLS_SQL = "select column_name, column_type, is_nullable, column_key, column_default, column_comment " \
                  "from information_schema.`COLUMNS` "

"""菜单栏"""
FILE_MENU = '文件'
EXIT_MENU = '退出'

"""关于连接的右键菜单"""
# 打开连接
OPEN_CONN_MENU = '打开连接'
# 关闭连接
CLOSE_CONN_MENU = '关闭连接'
# 测试连接
TEST_CONN_MENU = '测试连接'
# 添加连接
ADD_CONN_MENU = '添加连接'
# 编辑连接
EDIT_CONN_MENU = '编辑连接'
# 删除连接
DEL_CONN_MENU = '删除连接'

"""关于数据库的右键菜单"""
# 打开数据库
OPEN_DB_MENU = '打开数据库'
# 关闭数据库
CLOSE_DB_MENU = '关闭数据库'
# 全选所有表
SELECT_ALL_TB_MENU = '全选所有表'
# 取消选择表
UNSELECT_TB_MENU = '取消选择表'

"""关于表的右键菜单"""
# 打开表
OPEN_TABLE_MENU = '打开表'
# 关闭表
CLOSE_TABLE_MENU = '关闭表'
# 全选表中所有字段
SELECT_ALL_FIELD_MENU = '全选表中所有字段'
# 取消选择字段
UNSELECT_FIELD_MENU = '取消选择字段'
# 生成
GENERATE_MENU = '生成'
""""消息弹窗"""
WARNING_OK = '确认无误'
WARNING_RESELECT = '重新选择'
WRONG_TITLE = '错误'
WRONG_UNSELECT_DATA = '当前未选中数据，请选择后再执行！'
WRONG_PATH = "路径不正确！"

"""消息框按钮文字"""
OK_BUTTON = '确定'
ACCEPT_BUTTON = '是'
REJECT_BUTTON = '否'

"""按钮文字"""
NEXT_GENERATE_BUTTON = '下一步'
PRE_STEP_BUTTON = '上一步'
CANCEL_BUTTON = '取消'
EXPAND_BUTTON = '一键展开所有项'
COLLAPSE_BUTTON = '一键折叠所有项'
GENERATE_BUTTON = '开始生成'
CHOOSE_File = '请选择文件'

"""操作连接时提示语"""
# 编辑连接时的提示语
EDIT_CONN_PROMPT = '编辑连接需要先关闭连接，是否继续？'
# 编辑连接关闭时如有选择字段
EDIT_CONN_WITH_FIELD_PROMPT = '编辑连接需要先关闭连接，此连接下有已选的字段，' \
                              '如果继续将清空此连接下已选字段并关闭连接，是否继续？'
# 删除连接时的提示语
DEL_CONN_PROMPT = '是否要删除连接？'
# 删除连接时如有选择字段
DEL_CONN_WITH_FIELD_PROMPT = '此连接下有已选字段，如果继续将清空此连接下已选字段并删除连接，是否继续？'
# 保存连接成功提示语
SAVE_CONN_SUCCESS_PROMPT = '保存成功！'
# 测试连接成功提示语
TEST_CONN_SUCCESS_PROMPT = '连接成功！'
# 测试连接失败提示语
TEST_CONN_FAIL_PROMPT = '无法连接到数据库'
# 选择数据库表数据时，无法连接到数据库
SELECT_TABLE_FAIL_PROMPT = '选择数据库表失败'
# 选择字段失败
SELECT_FIELD_FAIL_PROMPT = '选择数据库字段失败'
# 检查系统库中连接名字存在提示语
CONN_NAME_EXISTS = '当前名称不可用，{}已存在！'
CONN_NAME_AVAILABLE = '连接名称{}可用'
# 关闭连接时的提示语
CLOSE_CONN_PROMPT = '该连接下有已选的字段，强行关闭将清空连接下所选字段，是否继续'

"""操作数据库时提示语"""
# 关闭数据库时提示语
CLOSE_DB_PROMPT = '该数据库下有已选的字段，强行关闭将清空库下所选字段，是否继续？'

"""表格列头"""
TABLE_HEADER_LABELS = ["全选", "字段名", "数据类型", "备注"]

"""主页面树部件头标题"""
TREE_HEADER_LABELS = 'mysql连接列表'

"""生成弹窗确认页树部件头标题"""
CONFIRM_TREE_HEADER_LABELS = '已选择的表字段列表'

"""生成器配置页"""
GENERATOR_SETTING_TITLE = '数据词典生成器路径配置'
GENERATOR_PATH = '生成路径'

"""生成器实现部分"""
# 表头列名信息
COL_NAMES = ['字段名', '数据类型', '允许为空', '是否为主键', '默认值', '注释']
