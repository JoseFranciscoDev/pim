from django.db import models

class TimeStampModel(models.Model):
    # create_at = models.DateField(auto_now_add=True, default=timezone.now())
    # update_at = models.DateField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True


class ProdutoInfo(TimeStampModel):
    class Meta:
        db_table = "produtos_cod"
        verbose_name = "produto_cod"
        verbose_name_plural = "produtos_cod"

    codigo = models.CharField(null=False)

    def __str__(self):
        return self.codigo


class ProdutoImagem(TimeStampModel):
    class Meta:
        db_table = "produto_imagens"
        verbose_name = "produto_imagem"
        verbose_name_plural = "produto_imagens"

    produto = models.ForeignKey(
        ProdutoInfo, on_delete=models.CASCADE, related_name="imagens"
    )
    imagem = models.ImageField(upload_to="produtos")

    def __str__(self):
        return f"{self.produto.codigo} - imagem"
    
    
    

"""Descrição, preço de venda, se está na promoção"""
