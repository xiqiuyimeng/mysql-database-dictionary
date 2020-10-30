# -*- coding: utf-8 -*-
from src.func.connection_function import open_connection
from src.generator.table_info import TableInfo
from src.sys.sys_info_storage.conn_sqlite import ConnSqlite

_author_ = 'luwt'
_date_ = '2020/10/27 10:50'


def get_params(gui, selected_data, output_path, consumer):
    """
    拼接生成器需要的参数。
    """
    params = list()
    tb_count = 0
    for conn_name, db_dict in selected_data.items():
        conn_id = ConnSqlite().get_id_by_name(conn_name)
        db_executor = open_connection(gui, conn_id, conn_name)
        for db_name, tb_dict in db_dict.items():
            table_cols = list()
            current_param_dict = {
                'conn_name': conn_name,
                'db_executor': db_executor,
                'table_schema': db_name,
                'table_cols': table_cols,
                'path': output_path,
                'consumer': consumer
            }
            for tb_name, cols in tb_dict.items():
                if isinstance(cols, list):
                    table_cols.append({tb_name: list(map(lambda x: x[1], cols))})
                else:
                    table_cols.append(tb_name)
            params.append(current_param_dict)
            tb_count += len(tb_dict)
    gui.tb_count = tb_count
    return params


def do_generate(gui, output_path, selected_data, consumer):
    params = get_params(gui, selected_data, output_path, consumer)
    for param in params:
        TableInfo(**param).main()
