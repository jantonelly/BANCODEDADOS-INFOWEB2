from models.cliente import Cliente
import pyodbc

class ClienteDAO:
    def __init__(self):
        self.__conexao = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=AppcomBD;UID=sa;PWD=senha@12345')

    def inserir(self, obj):
        cursor = self.__conexao.cursor()
        sql = f'''
                        INSERT INTO Cliente(nome, email, fone) 
                        VALUES ('{obj.get_nome()}', '{obj.get_email()}', '{obj.get_fone()}')
                    '''
        print(sql)
        cursor.execute(sql
        )
        self.__conexao.commit()

    def listar(self):                
        cursor = self.__conexao.cursor()
        cursor.execute('SELECT id, nome, email, fone FROM Cliente')
        registros = cursor.fetchall()
        objetos = []
        for reg in registros:
            obj = Cliente(reg[0], reg[1], reg[2], reg[3])
            objetos.append(obj)
        return objetos

    def listar_id(self, id):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'SELECT id, nome, email, fone FROM Cliente WHERE id = {id}',
        )
        reg = cursor.fetchone()
        if reg:
            obj = Cliente(reg[0], reg[1], reg[2], reg[3])
            return obj
        return None

    def atualizar(self, obj):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f"UPDATE Cliente SET nome = '{obj.get_nome()}', email = '{obj.get_email()}', fone = '{obj.get_fone()}' WHERE id = {obj.get_id()}"
        )
        self.__conexao.commit()

    def excluir(self, id):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'DELETE FROM Cliente WHERE id = {id}'
        )
        self.__conexao.commit()