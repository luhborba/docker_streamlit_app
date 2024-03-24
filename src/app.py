"""Arquivo Principal do FrontEnd."""

import pandas as pd
import streamlit as st

from database import conectar_banco, listar_dados


def main():
    """Função Principal de FrontEnd."""
    st.set_page_config(
        page_title="App de Metas",
        page_icon=":bar_chart:",
        layout="wide",
    )
    st.title("Aplicativo de Acompanhamento de Meta")

    with st.expander("Cadastro de Acompanhamento: "):
        st.markdown("## Cadastro de Metas")
        st.write("Indicadores do Youtube")
        visualizacao_youtube = st.number_input(
            "Nº de Visualização Youtube", min_value=0, step=1
        )
        inscricao_youtube = st.number_input(
            "Nº de Inscrição Youtube", min_value=0, step=1
        )
        visualizacao_youtube_28dias = st.number_input(
            "Nº de Visualização Youtube 28 dias", min_value=0, step=1
        )
        visualizacao_youtube_48horas = st.number_input(
            "Nº de Visualização Youtube 48 horas", min_value=0, step=1
        )
        st.divider()
        st.write("Indicadores do LinkedIn")
        seguidores_linkedin = st.number_input(
            "Nº de Seguidores Linkedin", min_value=0, step=1
        )
        impressoes_28dias = st.number_input(
            "Nº de Impressões 28 dias", min_value=0, step=1
        )
        impressores_90dias = st.number_input(
            "Nº de Impressores 90 dias", min_value=0, step=1
        )
        enviar = st.button("Enviar Dados")

        if enviar:
            try:
                resposta = conectar_banco(
                    visualizacao_youtube=visualizacao_youtube,
                    inscricao_youtube=inscricao_youtube,
                    visualizacao_youtube_28dias=visualizacao_youtube_28dias,
                    visualizacao_youtube_48horas=visualizacao_youtube_48horas,
                    seguidores_linkedin=seguidores_linkedin,
                    impressoes_28dias=impressoes_28dias,
                    impressores_90dias=impressores_90dias,
                )
            except Exception as e:
                st.error(f"Erro ao enviar dados: {e}")

    with st.expander("Lista de Dados Cadastrados:"):
        dados = listar_dados()
        if dados:
            nomes_colunas = [
                "ID",
                "Visualizações no Youtube",
                "Inscritos no Youtube",
                "Visualizações no Youtube 28 dias",
                "Visualizações no Youtube 48 horas",
                "Seguidores no Linkedin",
                "Impressões no 28 dias",
                "Impressores no 90 dias",
                "Data de Envio",
            ]
            df = pd.DataFrame(dados[1:], columns=nomes_colunas)
            st.write(
                df
            )  # Exibe o DataFrame pandasbe os dados em formato de tabela com os nomes das colunas
        else:
            st.write("Nenhum dado cadastrado ainda.")


if __name__ == "__main__":
    main()
