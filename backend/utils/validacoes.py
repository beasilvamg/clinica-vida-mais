#Validações do nome, idade e número de telefone
import re

def validar_nome(nome):
    nome = nome.strip().title()
    if not re.fullmatch(r"^[A-Za-zÀ-ÿ\s]{3,}$", nome):
        raise ValueError("Nome inválido: Digite apenas letras.")
    return nome

def validar_idade(idade):
    try:
        valor = int(idade)
    except (ValueError, TypeError):
        raise ValueError("A idade deve ser um número válido.")
    if not 0 < valor <= 120:
        raise ValueError("A idade deve estar entre 1 a 120.")
    return valor

def validar_telefone(telefone):
    apenas_numeros = re.sub(r"\D", "", telefone)
    if len(apenas_numeros) != 11:
        raise ValueError("O telefone deve ter 11 dígitos.")
    return f"({apenas_numeros[:2]}) {apenas_numeros[2:7]}-{apenas_numeros[7:]}"