#Validações do nome, idade e número de telefone
import re

def validar_nome(nome):
    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
        raise ValueError("O nome deve conter apenas letras e espaços.")
    return True

def validar_idade(idade):
    if not isinstance(idade, int):
        raise ValueError("A idade deve ser em números.")
    if idade <= 0 or idade > 120:
        raise ValueError("A idade deve estar entre 1 e 120.")
    return int(idade)

def validar_telefone(telefone):
    if not re.match(r"^\(\d{2}\)\s9\d{4}-\d{4}$", telefone):
        raise ValueError("Telefone inválido! Use o formato (99) 98765-4321.")
    return True