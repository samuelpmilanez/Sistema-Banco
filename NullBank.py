""" coding: utf-8"""

import MySQLdb as Bd


class ConnectionBd:
    connect = None
    cursor = None

    def __init__(self, **kwargs):
        super(ConnectionBd, self).__init__(**kwargs)

    def connect_bd(self, user, senha):

        host = "localhost"
        data = 'null_bank'
        port = 3306

        self.connect = Bd.connect(host, user, senha, data, port)
        """
        Definir q as tuplas do banco serao transformadas em dicionarios o objetivo 
        das funçoes e sempre o msm :formar a string que  seja igual ao comando em sql relativo a funcao
        """
        self.cursor = self.connect.cursor(Bd.cursors.DictCursor)
        print("Conexão OK")

    """ values e uma lista com o valores para inserir table e a tabela onde vai ser inserido  
        e fields os atributos da tabela """

    def select(self, fields, tables, where=None):
        """#fields recebe as strings com o nome das colunas
                                         # table=o nome das tabelas,pode ser mais de uma,
                                         # where é opcional,mas ai e so adicionar o predicado"""
        query = 'select ' + fields + " from  " + tables
        if where:
            query = query + ' WHERE ' + where
        self.cursor.execute(query)
        return self.cursor.fetchall()

    """
        sets e um dicionario onde a chave é o atributo e ele recebe o novo valor tables e where 
        msm jeito q no select
    """

    def insert(self, values, table, fields=None):

        query = "insert into " + table
        if fields:
            query = query + ' (' + fields + ')'

        query = query + ' values ' + ','.join(['(' + v + ')' for v in values])

        self.cursor.execute(query)
        self.connect.commit()

    def update(self, sets, tables, where=None):

        query = "update " + tables + " set "
        query = query + ','.join([fields + '=' + "'" + values + "'" for fields, values in sets.items()])
        if where:
            query = query + " where " + where

        self.cursor.execute(query)
        self.connect.commit()

    def delete(self, table, where):  # do msm jeito q no select

        query = " delete from  " + table + ' where ' + where

        self.cursor.execute(query)
        self.connect.commit()


def func_insert():

    colunas_s = input("\n\n\n\nSELECT ")
    tablela_s = input("FROM ")
    where_s = input("WHERE ")
    if colunas_s == "" or colunas_s == " ":
        colunas_s = "*"
    if where_s == "":
        for tupla_s in ConnectionBd.select(ConnectionBd, colunas_s, tablela_s):
            print(tupla_s)
    elif where_s != "":
        for tupla_s in ConnectionBd.select(ConnectionBd, colunas_s, tablela_s, where_s):
            print(tupla_s)


def func_update():
    tabela_u = input("\n\n\n\nUPDATE ")
    set_u = input("Set ")
    where_u = input("WHERE ")

    set_u = set_u.split(',')
    for i in list(range(len(set_u))):
        set_u[i] = set_u[i].split('=')
    set_u = dict(set_u)
    print(set_u)
    if where_u == "":
        ConnectionBd.update(ConnectionBd, set_u, tabela_u)
    else:
        ConnectionBd.update(ConnectionBd, set_u, tabela_u, where_u)


def func_delete():
    print("\n\n\n\nDELETE")
    table_d = input("")


if __name__ == '__main__':
    print("Logar no Mysql-Server")
    my_sql_usr = str(input("Usuário do Mysql-server :"))
    my_sql_pass = str(input("Senha do Mysql-server :"))
    ConnectionBd.connect_bd(ConnectionBd, my_sql_usr, my_sql_pass)
    while True:
        print("\nNullBank\n")
        print("Digite | 1 | para fazer um select")
        print("Digite | 2 | para fazer um update")
        print("Digite | 3 | para fazer um delete")
        print("Digite | 4 | para SAIR\n")
        escolha = input("O que deseja fazer ? \nEscolha : ")
        if escolha == "4":
            exit(1)
        elif escolha == "1":
            func_insert()
        elif escolha == "2":
            func_update()
        elif escolha == "3":
            func_delete()
