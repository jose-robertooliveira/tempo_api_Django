from django.db import models

LEITURAS = (
    (0, "Ensolarado"),
    (1, "Chuvoso"),
    (2, "Nublado"), 
    (3, "Neve")
)

class Leitura(models.Model):
    tempo_leitura = models.IntegerField(choices=LEITURAS, default=0)
    temperatura = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return str(self.created_on) 