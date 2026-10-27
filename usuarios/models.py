
from django.db import models
from django.core.validators import MinValueValidator


class Material(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField(default=1)
    localizacao = models.CharField(max_length=150, blank=True)
    permanente = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return self.nome

    @property
    def estoque_critico(self):
        return self.quantidade <= self.estoque_minimo


class Movimentacao(models.Model):
    class Tipo(models.TextChoices):
        ENTRADA = 'ENTRADA', 'Entrada'
        RETIRADA = 'RETIRADA', 'Retirada'
        EMPRESTIMO = 'EMPRESTIMO', 'Empréstimo'
        DEVOLUCAO = 'DEVOLUCAO', 'Devolução'

    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        related_name='movimentacoes'
    )
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    requisitante = models.CharField(max_length=150, blank=True)
    matricula = models.CharField(max_length=50, blank=True)
    setor = models.CharField(max_length=100, blank=True)
    observacao = models.TextField(blank=True)
    usuario_registro = models.CharField(max_length=150, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_hora']
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.material.nome}'


class Emprestimo(models.Model):
    class Status(models.TextChoices):
        ATIVO = 'ATIVO', 'Em andamento'
        DEVOLVIDO = 'DEVOLVIDO', 'Devolvido'

    codigo = models.CharField(max_length=30, unique=True)
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        related_name='emprestimos'
    )
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    requisitante = models.CharField(max_length=150)
    matricula = models.CharField(max_length=50, blank=True)
    setor = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ATIVO
    )
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-data_emprestimo']
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    def __str__(self):
        return f'{self.codigo} - {self.material.nome}'
