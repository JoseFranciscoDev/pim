import mysql.connector
from mysql.connector.types import RowType


class ProdutosService:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def __connectar(self):
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )

    def get_produto_por_codigo(self, codigoProduto) -> list[RowType]:
        """Retorna uma lista com linhas do resultado, cada linha é uma tupla"""
        connection = self.__connectar()
        cursor = connection.cursor()
        QUERY = "SELECT * FROM produtos where codigo_produto = %s"

        cursor.execute(
            QUERY,
            (codigoProduto,),
        )

        resultado = cursor.fetchall()
        connection.close()
        return resultado

    def get_all_produtos(self, todos_codigos_cadastrados) -> list[RowType]:
        """Retorna um dicionario com o resultado"""
        connection = self.__connectar()

        cursor = connection.cursor(dictionary=True)

        placeholders = ",".join(["%s"] * len(todos_codigos_cadastrados))
        QUERY = f"SELECT * FROM produtos where codigo_produto in ({placeholders})"

        cursor.execute(QUERY, todos_codigos_cadastrados)
        resultado = cursor.fetchall()

        connection.close()
        return resultado


class ImagemService:
    def __init__(self, image_name, path, create_at):
        self.image_name = image_name
        self.path = path
        self.create_at = create_at
