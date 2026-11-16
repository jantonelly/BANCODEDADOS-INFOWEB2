from models.servico import Servico
import pyodbc

class ServicoDAO:
    def __init__(self):
        self.__conexao = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=.;Database=Matheus;UID=sa;PWD=senha@12345')

    def inserir(self, obj):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'''
                INSERT INTO Servico (descricao, valor) 
                VALUES ({obj.get_descricao()}, {obj.get_valor()})
            '''
        )
        self.__conexao.commit()

    def listar(self):                
        cursor = self.__conexao.cursor()
        cursor.execute('SELECT id, descricao, valor FROM Servico')
        registros = cursor.fetchall()
        objetos = []
        for reg in registros:
            obj = Servico(reg[0], reg[1], reg[2])
            objetos.append(obj)
        return objetos

    def listar_id(self, id):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'SELECT id, descricao, valor FROM Servico WHERE id = {id}'
        )
        reg = cursor.fetchone()
        if reg:
            obj = Servico(reg[0], reg[1], reg[2])
            return obj
        return None


    def atualizar(self, obj):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'UPDATE Servico SET descricao = {obj.get_descricao()}, valor = {obj.get_valor()} WHERE id = {obj.get_id()}'
        )
        self.__conexao.commit()

    def excluir(self, id):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'DELETE FROM Servico WHERE id = {id}',
        )
        self.__conexao.commit()
        