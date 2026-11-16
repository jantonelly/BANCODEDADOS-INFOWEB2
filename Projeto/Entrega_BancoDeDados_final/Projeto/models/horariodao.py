from database import connect
from models.horario import Horario


class HorarioDAO:
    def inserir(self, obj):
        with connect() as cn:
            cur = cn.cursor()
            cur.execute("""INSERT INTO dbo.Horario (data_hora, confirmado, id_cliente, id_servico)
                OUTPUT INSERTED.id_horario VALUES (?, ?, ?, ?)""",
                obj.get_data(), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico())
            obj.set_id(cur.fetchone()[0])

    def listar(self):
        with connect() as cn:
            rows = cn.cursor().execute("SELECT id_horario, data_hora, confirmado, id_cliente, id_servico FROM dbo.Horario ORDER BY data_hora").fetchall()
        return [self._obj(r) for r in rows]

    def listar_id(self, id):
        with connect() as cn:
            r = cn.cursor().execute("SELECT id_horario, data_hora, confirmado, id_cliente, id_servico FROM dbo.Horario WHERE id_horario = ?", id).fetchone()
        return self._obj(r) if r else None

    @staticmethod
    def _obj(r):
        obj = Horario(r.id_horario, r.data_hora)
        obj.set_confirmado(bool(r.confirmado))
        obj.set_id_cliente(r.id_cliente)
        obj.set_id_servico(r.id_servico)
        return obj

    def atualizar(self, obj):
        with connect() as cn:
            cn.cursor().execute("""UPDATE dbo.Horario SET data_hora = ?, confirmado = ?, id_cliente = ?, id_servico = ?
                WHERE id_horario = ?""", obj.get_data(), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id())

    def excluir(self, id):
        with connect() as cn:
            cn.cursor().execute("DELETE FROM dbo.Horario WHERE id_horario = ?", id)
