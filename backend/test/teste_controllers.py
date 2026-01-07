# Teste do módulo controllers
from backend.controllers.paciente_controllers import PacienteController

# Importando o módulo Paciente para checar o tipo de objeto retornado
from backend.models.paciente import Paciente 

def rodar_teste_de_cadastro():
    print("--- 🧪 INICIANDO TESTE RÁPIDO DO CONTROLLER ---")
    
    controller = PacienteController()

    # == TESTE 1: CADASTRO COM SUCESSO ==
    try:
        print("\n[AÇÃO] Tentando cadastrar paciente válido...")
        
        
        nome_valido = "Ana Silva"
        idade_str_valida = "30"
        telefone_valido = "(11) 98765-4321"

        paciente_cadastrado = controller.cadastrar_paciente(
            nome_valido, idade_str_valida, telefone_valido
        )
        
        # Verificação de sucesso
        if isinstance(paciente_cadastrado, Paciente) and paciente_cadastrado.nome == nome_valido:
            print("✅ TESTE DE CADASTRO SUCESSO: Objeto Paciente criado e retornado.")
        else:
            print("❌ TESTE DE CADASTRO FALHOU: Não retornou o objeto esperado.")

    except Exception as e:
        print(f"❌ TESTE DE CADASTRO FALHOU (Inesperado): {e}")


    # == TESTE 2: VALIDAÇÃO COM ERRO (Utils) ==
    try:
        print("\n[AÇÃO] Tentando cadastrar paciente com idade inválida ('abc')...")
        controller.cadastrar_paciente("Pedro", "abc", "(11) 98765-4321")
        
        # Se chegar aqui, significa que o erro não foi lançado
        print("❌ TESTE DE VALIDAÇÃO FALHOU: Não lançou ValueError.")
    
    except ValueError as e:
        # Se entrar no except, significa que a validação do Utils funcionou
        print(f"✅ TESTE DE VALIDAÇÃO SUCESSO: Lançou o erro esperado: {e}")
    
    
    # == TESTE 3: LISTAGEM DOS DADOS ==
    print("\n[AÇÃO] Listando pacientes após os testes...")
    pacientes_na_lista = controller.listar_pacientes()
    
    if len(pacientes_na_lista) == 1 and pacientes_na_lista[0].nome == nome_valido:
        print("✅ TESTE DE LISTAGEM SUCESSO: Encontrado 1 paciente na lista.")
        print(f"Detalhe: {pacientes_na_lista[0]}")
    else:
        print(f"❌ TESTE DE LISTAGEM FALHOU: Esperava 1 paciente, encontrou {len(pacientes_na_lista)}.")
    
    print("\n--- TESTE CONCLUÍDO ---")


if __name__ == '__main__':
    rodar_teste_de_cadastro()