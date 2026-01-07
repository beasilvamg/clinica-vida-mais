from backend.models.paciente import Paciente

def gerar_relatoio_estatistico(pacientes):
    if not pacientes:
            # Caso não tenha pacientes o valor volta padrão
            return {"total_pacientes": 0, "media_idade": 0.0, "mais_novo_idade": 0, "mais_velho_idade": 0}
        
    # Lógica de calculo
    idades = [paciente.idade for paciente in pacientes]
    total_pacientes = len(idades)
    media_idade = sum(idades) / total_pacientes
    mais_novo_idade = min(idades)
    mais_velho_idade = max(idades)

    # Retorna os dados
    return {
         "total_pacientes": total_pacientes,
         "media_idade": round(media_idade),
         "mais_novo_idade": mais_novo_idade,
         "mais_velho_idade": mais_velho_idade 
    }