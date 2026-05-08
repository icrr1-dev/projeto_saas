from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    ramo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - ({self.empresa.nome})"

class Cliente(models.Model):

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100, default="Nova Porteirinha")
    cep = models.CharField(max_length=9)

    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome