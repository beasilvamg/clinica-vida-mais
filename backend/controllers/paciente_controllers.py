# Importação dos módulos criados
from backend.models.paciente import Paciente
from backend.utils.validacoes import validar_nome, validar_idade, validar_telefone
from backend.database.conexao import db_inserir

class PacienteController:
    # Função para cadastrar paciente
    def cadastrar_paciente(self, nome, idade, telefone):
        #Impedir e interromper cadastros incompletos
        try:
        #Chamando as funções do módulo utils
            nome_final = validar_nome(nome)
            idade_validada = validar_idade(idade)
            telefone_final = validar_telefone(telefone)

            novo_paciente = Paciente(nome_final, idade_validada, telefone_final)
            db_inserir(novo_paciente)
            return novo_paciente
        except Exception as e:
            return None

    # Lista de todos os pacientes cadastrados
    #def listar_pacientes(self):
        #return dados_pacientes

    # Buscar paciente pelo nome
    #def buscar_paciente(self, nome):
        #resultado = list(filter(lambda paciente: nome.lower() in paciente.nome.lower(), dados_pacientes))
        #return resultado