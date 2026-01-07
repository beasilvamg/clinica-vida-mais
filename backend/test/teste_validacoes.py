from backend.utils.validacoes import validar_nome, validar_idade, validar_telefone

def executar_testes_completos():
    print("\nValidação de NOME:")
    casos_nome = [
        ("Ana Silva", True),   # Sucesso
        ("A", False),           # Erro: Muito curto
        ("João123", False),     # Erro: Contém números
        ("", False),             # Erro: Vazio
        ("  MARIA socorro  ", True), #Sucesso: Ajuste de nome na lista
    ]
    for entrada, esperado in casos_nome:
        try:
            resultado = validar_nome(entrada)
            sucesso_real = True if resultado else False 
        except ValueError:
            sucesso_real = False 
    
        status = "PASSOU" if sucesso_real == esperado else "FALHOU"
        print(f"Entrada: '{entrada}' | Esperado: {esperado} | Resultado: {status}")


    print("\nValidação de IDADE:")
    casos_idade = [
        (25, True),    # Sucesso
        (150, False),  # Erro: Idade impossível
        (-5, False),   # Erro: Idade negativa
        ("vinte", False), # Erro: Não é número
        (42, True),     # Sucesso
        (150, False),   # Erro: Idade fora do limite
    ]
    for entrada, esperado in casos_idade:
        try:
            resultado = validar_idade(entrada)
            sucesso_real = True if isinstance(resultado, int) else False
        except ValueError:
            sucesso_real = False

        status = "PASSOU" if sucesso_real == esperado else "FALHOU"
        print(f"Entrada: '{entrada}' | Esperado: {esperado} | Resultado: {status}")


    print("\nValidação de TELEFONE:")
    casos_tel = [
        ("(11) 99999-9999", True), # Sucesso
        ("11988887777", True),     # Sucesso, sem máscara
        ("12345", False),          # Erro: Muito curto
        ("abc-defg", False),       # Erro: Letras no telefone
        ("(11) 99a99-76j5", False), # Erro: Lestras entre números
        ("11 9 1234 5678", True),  # Sucesso: Espaços corrigidos na lista
    ]
    for entrada, esperado in casos_tel:       
        try:
            resultado = validar_telefone(entrada)
            sucesso_real = True if resultado else False
        except ValueError:
            sucesso_real = False
            
        status = "PASSOU" if sucesso_real == esperado else "FALHOU"
        print(f"Entrada: '{entrada}' | Esperado: {esperado} | Resultado: {status}")


if __name__ == "__main__":
    executar_testes_completos()