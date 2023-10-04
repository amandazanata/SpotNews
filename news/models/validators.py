from django.core.exceptions import ValidationError


# notícia com um título com uma única palavra é gerada a resp
# Req 3
def validate_title(title):
    words = title.split()
    if len(words) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
