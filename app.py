# Importação streamlit interface gráfica rápida
import streamlit as st
from backend.controllers.paciente_controllers import PacienteController
from backend.services.estatisticas import gerar_relatoio_estatistico

# Configuração da página
st.set_page_config(page_title="Sistema Vida +", layout="wide", page_icon="🏥")

# Session State para não sumir os dados do paciente
if 'controller' not in st.session_state:
    st.session_state.controller = PacienteController()

controller = st.session_state.controller

# Menu
st.sidebar.title("🏥 Vida +")
st.sidebar.markdown("---")
aba = st.sidebar.radio("Navegação:", ["Início", "Cadastrar Paciente",
"Lista de Pacientes", "Buscar Paciente", "Estatísticas da Clínica"])

if aba == "Início":
    st.title("Bem-Vindo(a) ao Sistema da Clínica Vida+")
    st.write("Selecione uma opção no menu lateral para começar.")


elif aba == "Cadastrar Paciente":
    st.title("Cadastrar Paciente")

    with st.form("from_cadastro", clear_on_submit=True):
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
        telefone = st.text_input("Telefone Ex: (99) 98765-4321")
        btn_enviar = st.form_submit_button("Salvar Cadastro")
        if btn_enviar:
            paciente = controller.cadastrar_paciente(nome, idade, telefone)

            if paciente:
                st.success(f" Paciente {paciente.nome} cadastrado com sucesso!")
            else:
                st.error(f" Erro ao cadastrar. Verifique se os dados estão corretos.")


elif aba == "Lista de Pacientes":
    st.title("Lista de Pacientes")
    pacientes = controller.listar_pacientes()
    if pacientes:
        dados = [{"Nome": p.nome, "Idade": p.idade, "Telefone": p.telefone} for i, p in enumerate(pacientes)]
        st.table(dados)
    else:
        st.info("Nenhum paciente cadastrado no sistema.")


elif aba == "Buscar Paciente":
    st.title("Buscar Paciente")
    nome_busca = st.text_input("Digite o nome completo ou parte dele:")
    if nome_busca:
        resultados = controller.buscar_paciente(nome_busca)
        if resultados:
            st.success(f"Encontrado(s) {len(resultados)} paciente(s):")
            dados_busca = [{"Nome": p.nome, "Idade": p.idade, "Telefone": p.telefone} for p in resultados]
            st.table(dados_busca)
        else:
            st.error("Paciente não econtrado no sistema.")


elif aba == "Estatísticas da Clínica":
    st.title("Estatísticas da Clínica")
    pacientes_para_stats = controller.listar_pacientes()
    
    if pacientes_para_stats:
        stats = gerar_relatoio_estatistico(pacientes_para_stats)
        
        dados_grafico = {
            "Idade Médica": round(stats['media_idade'], 1),
            "Paciente Mais Novo": stats['mais_novo_idade'],
            "Paciente Mais Velho": stats['mais_velho_idade'],
            "Total de Pacientes": stats['total_pacientes']
        }
        
        st.subheader("Dados gerais da Clínica Vida+")
        st.bar_chart(dados_grafico)

        st.markdown("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Média", f"{stats['media_idade']:.1f}")
        c2.metric("Mais Novo", f"{stats['mais_novo_idade']} anos")
        c3.metric("Mais Velho", f"{stats['mais_velho_idade']} anos")
        c4.metric("Total de Pacientes", stats["total_pacientes"])

    else:
        st.info("Nenhum paciente cadastrado para gerar estatísticas.")