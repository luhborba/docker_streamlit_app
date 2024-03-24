"""Arquivo de config do banco de dados."""
import psycopg2 as pg
import streamlit as st


def conectar_banco(
    visualizacao_youtube,
    inscricao_youtube,
    visualizacao_youtube_28dias,
    visualizacao_youtube_48horas,
    seguidores_linkedin,
    impressoes_28dias,
    impressores_90dias,
):
    """
    Função de acesso e inserção no banco de dados.

    Args:
        visualizacao_youtube (int): Número de Visualização Youtube.
        inscricao_youtube (int): Número de Inscrição Youtube.
        visualacao_youtube_28dias (int): Número de Visualização Youtube 28 dias.
        visualizacao_youtube_48horas (int): Número de Visualização Youtube 48 horas.
        seguidores_linkedin (int): Número de Seguidores Linkedin.
        impressoes_28dias (int): Número de Impressoes 28 dias.
        impressores_90dias (int): Número de Impressores 90 dias.
    """
    try:
        conexao = pg.connect(
            dbname="mydatabase", user="user", password="password", host="postgres"
        )
        cursor = conexao.cursor()

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS dados_redes_sociais (
                    id SERIAL PRIMARY KEY,
                    visualizacao_youtube INTEGER,
                    inscricao_youtube INTEGER,
                    visualizacao_youtube_28dias INTEGER,
                    visualizacao_youtube_48horas INTEGER,
                    seguidores_linkedin INTEGER,
                    impressoes_28dias INTEGER,
                    impressores_90dias INTEGER,
                    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
        )
        conexao.commit()
        cursor.execute(
            """
            INSERT INTO dados_redes_sociais (
                visualizacao_youtube,
                inscricao_youtube,
                visualizacao_youtube_28dias,
                visualizacao_youtube_48horas,
                seguidores_linkedin,
                impressoes_28dias,
                impressores_90dias
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                visualizacao_youtube,
                inscricao_youtube,
                visualizacao_youtube_28dias,
                visualizacao_youtube_48horas,
                seguidores_linkedin,
                impressoes_28dias,
                impressores_90dias,
            ),
        )

        conexao.commit()
        st.success("Dados Salvos Com Sucesso!!!!")
        cursor.close()
        conexao.close()

    except Exception as e:
        st.error(f"Error ao se conectar com o banco {e}")
        cursor.close()
        conexao.close()


def listar_dados():
    """Função de consulta no banco de dados."""
    try:
        conexao = pg.connect(
            dbname="mydatabase", user="user", password="password", host="postgres"
        )
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM dados_redes_sociais")
        dados = cursor.fetchall()
        return dados

    except Exception as e:
        st.error(f"Error ao se conectar com o banco {e}")

    finally:
        if "conexao" in locals():
            conexao.close()
        if "cursor" in locals():
            cursor.close()


if __name__ == "__main__":
    print(conectar_banco())
