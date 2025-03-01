from backend.infrastracture.connection_pool import MySQLPool

class PonenteRepository:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get(self, id):
        params = {'id':id}
        rv = self.mysql_pool.execute("select * from usuario where id = %(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data

    def get_all(self):
        rv = self.mysql_pool.execute("select * from usuario u inner join ponente p on p.id = u.id order by id")
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data

    def create(self, id, nombre, apellido, correo):
        params = {
            'id' : id,
            'nombre' : nombre,
            'apellido' : apellido,
            'correo' : correo,
        }
        query = "insert into usuarios(%(id)s, %(nombre)s, %(apellido)s, %(correo)s)\ninsert into ponente(%(id)s)"
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result : 1'}
        return data

        
    def delete(self, id):
        params = {'id' : id}      
        query = "delete from ponente where id = %(id)s\ndelete from usuario where id = %(id)s"    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data
