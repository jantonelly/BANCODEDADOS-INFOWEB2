from models.horario import Horario
from datetime import datetime
import pyodbc

class HorarioDAO:
    def __init__(self):
        self.__conexao = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=.;Database=AppcomBD;UID=sa;PWD=senha@12345')

    def inserir(self, obj):
        cursor = self.__conexao.cursor()
        cursor.execute(
            '''
            INSERT INTO Horario (data, confirmado, Cliente_id, Servico_id)
            VALUES (?, ?, ?, ?)
        ''',
        obj.get_data(),
        obj.get_confirmado(),
        obj.get_id_cliente(),
        obj.get_id_servico()
        )
        self.__conexao.commit()

    def listar(self):                
        cursor = self.__conexao.cursor()
        cursor.execute('SELECT id, data, confirmado, Cliente_id, Servico_id FROM Horario')
        registros = cursor.fetchall()
        objetos = []
        for reg in registros:
            obj = Horario(reg[0], reg[1])
            obj.set_confirmado(reg[2])
            obj.set_id_cliente(reg[3])
            obj.set_id_servico(reg[4])
            objetos.append(obj)
        return objetos

    def listar_id(self, id):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'SELECT id, data, confirmado, Cliente_id, Servico_id FROM Horario WHERE id = {id}'
        )
        reg = cursor.fetchone()
        if reg:
            obj = Horario(reg[0], reg[1])
            obj.set_confirmado(reg[2])
            obj.set_id_cliente(reg[3])
            obj.set_id_servico(reg[4])
            return obj
        return None

    def atualizar(self, obj):
        cursor = self.__conexao.cursor()
        cursor.execute(
            '''
                UPDATE Horario
                SET data = ?, confirmado = ?,Cliente_id = ?, Servico_id = ?
                WHERE id = ?
            ''',
            obj.get_data(),
            obj.get_confirmado(),
            obj.get_id_cliente(),
            obj.get_id_servico(),
            obj.get_id()
        )
        self.__conexao.commit()

    def excluir(self, id):
        cursor = self.__conexao.cursor()
        cursor.execute(
            f'DELETE FROM Horario WHERE id = {id}',
        )
        self.__conexao.commit()