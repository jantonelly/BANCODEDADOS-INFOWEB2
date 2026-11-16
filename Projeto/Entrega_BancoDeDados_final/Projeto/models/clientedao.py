from database import connect
from models.cliente import Cliente


class ClienteDAO:
    def inserir(self, obj):
        with connect() as cn:
            cur = cn.cursor()
            cur.execute("INSERT INTO dbo.Cliente (nome, email, telefone) OUTPUT INSERTED.id_cliente VALUES (?, ?, ?)", obj.get_nome(), obj.get_email(), obj.get_fone())
            obj.set_id(cur.fetchone()[0])

    def listar(self):
        with connect() as cn:
            rows = cn.cursor().execute("SELECT id_cliente, nome, email, telefone FROM dbo.Cliente ORDER BY nome").fetchall()
        return [Cliente(r.id_cliente, r.nome, r.email, r.telefone) for r in rows]

    def listar_id(self, id):
        with connect() as cn:
            r = cn.cursor().execute("SELECT id_cliente, nome, email, telefone FROM dbo.Cliente WHERE id_cliente = ?", id).fetchone()
        return Cliente(r.id_cliente, r.nome, r.email, r.telefone) if r else None

    def atualizar(self, obj):
        with connect() as cn:
            cn.cursor().execute("UPDATE dbo.Cliente SET nome = ?, email = ?, telefone = ? WHERE id_cliente = ?", obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_id())

    def excluir(self, id):
        with connect() as cn:
            cn.cursor().execute("DELETE FROM dbo.Cliente WHERE id_cliente = ?", id)
