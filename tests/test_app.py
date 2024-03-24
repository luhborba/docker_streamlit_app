"""Arquivo de Test."""
import subprocess
from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """
    Função de Teste para iniciar o navegador.
    """
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Utilizando Web Driver
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(10)
    yield driver

    # Encerra o navegador
    driver.quit()
    process.kill()


def test_app_open(driver):
    """Função de Teste para verificar se a aplicação está aberta."""
    driver.get("http://127.0.0.1:8501")
    sleep(3)


def test_app_title(driver):
    """Função de Teste para verificar o título da aplicação."""
    driver.get("http://localhost:8501")
    sleep(5)
    # Capturando Título
    page_title = driver.title
    # Verificando se o título confere
    title = "App de Metas"
    assert page_title == title
