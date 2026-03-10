from django.shortcuts import render
from .services import ProdutosService
from .models import ProdutoInfo, ProdutoImagem


def listar_produtos(request):
    service = ProdutosService(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="produtos",
    )

    produtos_internos = ProdutoInfo.objects.values_list("codigo", flat=True)
    produtos_externos = service.get_all_produtos(
        list(produtos_internos),
    )
    # imagens = ProdutoImagem.objects.filter(, "imagens": produtos_internos.imagens,)
    return render(
        request,
        "produtos.html",
        {
            "produtos": produtos_externos,
            "imagens": produtos_internos.imagens,
        },
    )

    # # def listar_produtos(request):
    # service = ProdutosService(
    #     host="localhost",
    #     port=3306,
    #     user="root",
    #     password="1234",
    #     database="produtos",
    # )

    # produtos_internos = ProdutoInfo.objects.prefetch_related("imagens")

    # mapa_produtos = {p.codigo: p for p in produtos_internos}

    # produtos_externos = service.get_all_produtos(list(mapa_produtos.keys()))

    # produtos = []

    # for p in produtos_externos:
    #     codigo = p[0]
    #     descricao = p[1]

    #     produto_local = mapa_produtos.get(codigo)

    #     imagem = None
    #     if produto_local:
    #         img = produto_local.imagens.first()
    #         if img:
    #             imagem = img.imagem

    #     produtos.append(
    #         {
    #             "codigo_produto": codigo,
    #             "descricao_produto": descricao,
    #             "imagem": imagem,
    #         }
    #     )

    # return render(request, "produtos.html", {"produtos": produtos})
