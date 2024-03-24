import psycopg2 as pg
import streamlit as st


def conectar_banco(visualizacao_youtube, inscricao_youtube, visualizacao_youtube_28dias, visualizacao_youtube_48horas, seguidores_linkedin, impressoes_28dias, impressores_90dias):
    try:
        conexao = pg.connect(
            dbname='mydatabase',
            user='user',
            password='password',
            host='postgres'
        )
        cursor = conexao.cursor()

        cursor.execute("""
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
            """)
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
                impressores_90dias
            ))
        
        conexao.commit()
        st.success("Dados Salvos Com Sucesso!!!!")
        cursor.close()
        conexao.close()


    except Exception as e:
        st.error(f'Error ao se conectar com o banco {e}')
        cursor.close()
        conexao.close()

        
if __name__ == '__main__':
    print(conectar_banco())