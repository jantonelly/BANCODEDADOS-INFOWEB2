from database import connect
from models.servico import Servico


class ServicoDAO:
    def inserir(self, obj):
        with connect() as cn:
            cur = cn.cursor()
            cur.execute("INSERT INTO dbo.Servico (descricao, valor) OUTPUT INSERTED.id_servico VALUES (?, ?)", obj.get_descricao(), obj.get_valor())
            obj.set_id(cur.fetchone()[0])

    def listar(self):
        with connect() as cn:
            rows = cn.cursor().execute("SELECT id_servico, descricao, valor FROM dbo.Servico ORDER BY descricao").fetchall()
        return [Servico(r.id_servico, r.descricao, float(r.valor)) for r in rows]

    def listar_id(self, id):
        with connect() as cn:
            r = cn.cursor().execute("SELECT id_servico, descricao, valor FROM dbo.Servico WHERE id_servico = ?", id).fetchone()
        return Servico(r.id_servico, r.descricao, float(r.valor)) if r else None

    def atualizar(self, obj):
        with connect() as cn:
            cn.cursor().execute("UPDATE dbo.Servico SET descricao = ?, valor = ? WHERE id_servico = ?", obj.get_descricao(), obj.get_valor(), obj.get_id())

    def excluir(self, id):
        with connect() as cn:
            cn.cursor().execute("DELETE FROM dbo.Servico WHERE id_servico = ?", id)
