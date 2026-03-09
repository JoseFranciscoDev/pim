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

    produtos_externos = service.get_all_produtos()
    
    produtos = []

    for produto in produtos_externos:
        codigo = produto[0]

        try:
            produto_local = ProdutoInfo.objects.get(codigo=codigo)
            imagens = produto_local.imagens.all()
        except ProdutoInfo.DoesNotExist:
            imagens = []

        produtos.append({"dados": produto, "imagens": imagens})
        # produtos.append({"dados": produto})

    return render(request, "produtos.html", {"produtos": produtos})
