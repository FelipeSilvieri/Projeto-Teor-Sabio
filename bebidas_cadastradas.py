import mysql.connector

class BebidasCadastradas:
    
    conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='teorsabio'
        )
    cursor = conn.cursor()
        
        
    @classmethod
    def get_bebidas(cls):
        try:
            # Execute uma consulta para recuperar as bebidas do banco de dados
            cls.cursor.execute("SELECT nome, volume, teor FROM bebidas")
            bebidas = []
            for (nome, volume, teor) in cls.cursor:
                bebidas.append({"nome": nome, "volume": volume, "teor": teor})
            return bebidas
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            cls.cursor.close()
            cls.conn.close()

    @classmethod
    def cadastrar_bebida(cls, nome, volume, teor):
        # Conecte-se ao servidor MySQL (certifique-se de ter o MySQL Connector Python instalado)
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="teorsabio"
        )
        
        cursor = db.cursor()

        # Insira a nova bebida na tabela
        sql = "INSERT INTO bebidas (nome, volume, teor) VALUES (%s, %s, %s)"
        val = (nome, volume, teor)

        try:
            cursor.execute(sql, val)
            db.commit()
            return f"Bebida {nome} cadastrada com sucesso!\nRode o programa novamente para atualizar..."
        except mysql.connector.Error as err:
            db.rollback()
            return f"Erro ao cadastrar bebida: {err}"

        finally:
            cursor.close()
            db.close()
