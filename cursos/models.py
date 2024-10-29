from django.db import models


class Base(models.Model):
    publicacao = models.DateTimeField(auto_now=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def ___str__(self):
        return self.titulo
    

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name="avaliacoes", on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default="")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together = ['email', 'curso']
        
    def __str__(self):
        return f"{self.nome} avaliou o {self.curso} com a nota {self.avaliacao}"
    
