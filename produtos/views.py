from django.shortcuts import render
from .services import ProdutosService
from .models import ProdutoInfo


def exibir_catalogo(request):
    service = ProdutosService(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="produtos",
    )

    # 1. Busca produtos internos e já carrega as imagens (prefetch_related) para otimizar performance
    produtos_internos = ProdutoInfo.objects.prefetch_related("imagens").all()

    # 2. Cria um mapa {codigo: objeto_produto} para busca rápida
    mapa_produtos = {p.codigo: p for p in produtos_internos}

    codigos_para_buscar = list(mapa_produtos.keys())

    # Se não houver produtos cadastrados, retorna lista vazia para evitar erro no SQL
    if not codigos_para_buscar:
        return render(request, "catalogo.html", {"produtos": []})

    # 3. Busca informações detalhadas no banco externo
    # O service retorna uma lista de dicionários (pois dictionary=True no service)
    produtos_externos = service.get_all_produtos(codigos_para_buscar)
    print(produtos_externos)

    lista_final = []

    # 4. Combina os dados
    for item_externo in produtos_externos:
        # Ajuste 'codigo_produto' conforme o nome da coluna no seu banco externo MySQL
        codigo = item_externo.get("codigo_produto")

        # Busca o objeto local correspondente
        produto_local = mapa_produtos.get(str(codigo))

        imagem_url = None
        if produto_local:
            img = produto_local.imagens.first()  # Pega a primeira imagem associada
            if img and img.imagem:
                imagem_url = img.imagem.url

        # Adiciona a URL da imagem ao dicionário de dados do produto
        item_externo.update({"imagem": imagem_url})
        lista_final.append(item_externo)
    print(lista_final)

    return render(request, "catalogo.html", {"produtos": lista_final})
