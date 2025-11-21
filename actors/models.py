from django.db import models

NATIONALITY_CHOICES = (
    ("AFEGANISTÃO", "Afghanistan"),
    ("ÁFRICA DO SUL", "South Africa"),
    ("ALEMANHA", "Germany"),
    ("ARGENTINA", "Argentina"),
    ("AUSTRÁLIA", "Australia"),
    ("ÁUSTRIA", "Austria"),
    ("BÉLGICA", "Belgium"),
    ("BOLÍVIA", "Bolivia"),
    ("BRASIL", "Brazil"),
    ("CANADÁ", "Canada"),
    ("CHILE", "Chile"),
    ("CHINA", "China"),
    ("COLÔMBIA", "Colombia"),
    ("COREIA DO SUL", "South Korea"),
    ("CUBA", "Cuba"),
    ("DINAMARCA", "Denmark"),
    ("EGITO", "Egypt"),
    ("EMIRADOS ÁRABES UNIDOS", "United Arab Emirates"),
    ("ESPANHA", "Spain"),
    ("ESTADOS UNIDOS", "United States"),
    ("FILIPINAS", "Philippines"),
    ("FINLÂNDIA", "Finland"),
    ("FRANÇA", "France"),
    ("GRÉCIA", "Greece"),
    ("HOLANDA", "Netherlands"),
    ("HONG KONG", "Hong Kong"),
    ("HUNGRIA", "Hungary"),
    ("ÍNDIA", "India"),
    ("INDONÉSIA", "Indonesia"),
    ("INGLATERRA", "England"),
    ("IRÃ", "Iran"),
    ("IRAQUE", "Iraq"),
    ("IRLANDA", "Ireland"),
    ("ISLÂNDIA", "Iceland"),
    ("ISRAEL", "Israel"),
    ("ITÁLIA", "Italy"),
    ("JAPÃO", "Japan"),
    ("LÍBANO", "Lebanon"),
    ("MÉXICO", "Mexico"),
    ("MARROCOS", "Morocco"),
    ("NIGÉRIA", "Nigeria"),
    ("NORUEGA", "Norway"),
    ("NOVA ZELÂNDIA", "New Zealand"),
    ("PAQUISTÃO", "Pakistan"),
    ("PERU", "Peru"),
    ("POLÔNIA", "Poland"),
    ("PORTUGAL", "Portugal"),
    ("REINO UNIDO", "United Kingdom"),
    ("REPÚBLICA TCHECA", "Czech Republic"),
    ("RÚSSIA", "Russia"),
    ("SUÉCIA", "Sweden"),
    ("TAILÂNDIA", "Thailand"),
    ("TURQUIA", "Turkey"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
