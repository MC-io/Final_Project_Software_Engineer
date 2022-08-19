from backend.infrastracture.connection_pool import MySQLPool

class EventoRepository:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("select * from evento where evento.id = %(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'id_ponente': result[1], 'nombre': result[2], 'detalles': result[3], 'link': result[4]}
            data.append(content)
            content = {}
        return data

    def get_all(self):
        rv = self.mysql_pool.execute("select * from assitente order by id")
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'id_ponente': result[1], 'nombre': result[2], 'detalles': result[3], 'link': result[4]}
            data.append(content)
            content = {}
        return data

    def create(self, id, id_ponente, nombre, detalles, link):
        params = {
            'id' : id,
            'id_ponente' : id_ponente,
            'nombre' : nombre,
            'detalles' : detalles,
            'link' : link
        }
        query = "insert into evento(%(id)s, %(id_ponente)s, %(nombre)s, %(detalles)s, %(link)s)"
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result : 1'}
        return data
        
    def delete(self, id):
        params = {'id' : id}      
        query = "delete from evento where id = %(id)s"    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data
