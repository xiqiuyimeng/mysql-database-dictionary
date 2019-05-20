# -*- coding: utf-8 -*-
from db_opt import getcursor
from docx_demo import index_type
import docx
import os
import time
_author_ = 'luwt'
_date_ = '2018/12/17 13:42'


class TableInfo:

    def __init__(self, table_schema, path):
        default_docx = 'default.docx' if os.path.exists(
            os.path.join(os.path.abspath('.'), 'default.docx')) else None
        self.doc = docx.Document(docx=default_docx)
        self.cursor = TableInfo.get_cur()
        self.schema = table_schema
        self.path = path

    @staticmethod
    def get_cur():
        get_cursor = getcursor.GetCursor()
        return get_cursor.get_native_conn().cursor()

    def get_data(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def generate_table_title(self, table_comment, table_name):
        """生成表格标题，标题为表注释 + 表名，标题样式为有序数字"""
        self.doc.add_paragraph('\n')
        self.doc.add_paragraph('{} {}'.format(table_comment, table_name), style='List Number')

    def generate_table(self, data):
        # Table Grid可以实现表格线框为实线
        table = self.doc.add_table(1, 6, style='Table Grid')
        # 建立表格，生成表头
        cells = table.rows[0].cells
        cells[0].text = '字段名'
        cells[1].text = '数据类型'
        cells[2].text = '允许为空'
        cells[3].text = '是否为主键'
        cells[4].text = '默认值'
        cells[5].text = '注释'
        # data为查出的每个数据库表字段信息，一个字段为一个元祖
        for column_info in data:
            row_cells = table.add_row().cells
            # 处理索引
            index = column_info[4]
            if column_info[4] is not None and column_info[4] is not '':
                index = eval('index_type.IndexType.{}.value'.format(column_info[4]))
            values = (column_info[0], column_info[1], column_info[3],
                      index, column_info[5], column_info[8]
                      )
            # 将当前字段的各个属性填充相应表格
            for ix, v in enumerate(row_cells):
                if values[ix]:
                    v.text = values[ix]

    def main(self):
        # 查表名加表注释
        table_names_sql = 'SELECT table_name, table_comment from information_schema.`TABLES` ' \
                          'where table_schema = "{}" and table_comment != "";'.format(self.schema)
        # 查出所有表名
        table_names = self.get_data(table_names_sql)
        for table_name in table_names:
            table_comment = table_name[1].split('，')[0]
            table_name = table_name[0]
            # 查出表对象信息
            table_infos_sql = 'show full fields from {};'.format(table_name)
            data = self.get_data(table_infos_sql)
            self.generate_table_title(table_comment, table_name)
            self.generate_table(data)
        self.doc.save(self.path)
        print('执行完毕，输出为{}，三秒后退出！'.format(path))
        time.sleep(3)

    @staticmethod
    def get_schema(schema):
        cur = getcursor.GetCursor().get_native_schema_conn().cursor()
        cur.execute('SELECT SCHEMA_NAME FROM `SCHEMATA`;')
        data = cur.fetchall()
        data = list(map(lambda x: str(x[0]), data))
        print('正确的数据库名为：{}'.format(data))
        if schema in data:
            return True
        return False


if __name__ == '__main__':
    while True:
        name = input('请输入数据库名称：')
        flag = TableInfo.get_schema(name)
        if flag:
            break
        continue_ = input('请输入正确的数据库名称，继续？y/n')
        if continue_ is 'n':
            exit()
    path = 'D:\\数据词典demo.docx'
    table_info = TableInfo('test', path)
    table_info.main()

