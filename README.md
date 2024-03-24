# Home

Bem vindo ao projeto de **Acompanhando Indicadores** utilizando Streamlit e Docker para Deploy, a ideia geral deste projeto é criar uma aplicação Streamlit onde podemos registrar os indicadores do Youtube e LinkedIn, assim poder monitorar a movimentação nestas redes e realizar o deploy utilizando Docker.

Acesse a Documentação deste projeto [Documentação feita em MkDocs](https://luhborba.github.io/docker_streamlit_app/)
## Stack Utilizada

- Python
- Pyenv
- Poetry
- Pandas
- Pytest
- Black
- Isort
- Pre-Commit
- MkDocs
- Pip-Audit
- Pydocstyle
- Taskipy
- Docker
- Streamlit

## Clonando o Projeto com Docker

- Nesta etapa você precisa conter o Docker Instalado na sua maquina.


### Clone o repositório:
```bash
git clone https://github.com/luhborba/docker_streamlit_app.git
cd docker_streamlit_app
```

### Subindo Container:
```bash
docker compose up -d
```

### Acessando Aplicação:

```
Acesse seu navegador 'localhost:8502'
```
## Clonando o Projeto com Python

- Caso não tenha `Pyenv e Proetry` instalado é está usando ambiente Linux acesse [Instalando Pyenv e Poetry (WSL/Linux)](https://github.com/luhborba/Wsl-Pyenv-Poetry)
- Caso o ambiente seja Windows, assista este vídeo [Como instalar Python em 2024 + Pyenv, PIP, VENV, PIPX e Poetry](https://www.youtube.com/watch?v=9LYqtLuD7z4&t)

### Clone o repositório:
```bash
git clone https://github.com/luhborba/docker_streamlit_app.git
cd docker_streamlit_app
```

### Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.11.7
pyenv local 3.11.7
```

### Ativando Poetry
```bash
poetry env use 3.11.7
poetry shell
```

### Insatalando dependências
```bash
poetry install
```

### Rodando Streamlit
```bash
task run
```

### Rodando Testes
```bash
task test
```

### Rodando Documentação
```bash
task docs
```

<h3 align="left">Se conecte comigo:</h3>
<p align="left">
<a href="https://linkedin.com/in/luhborba" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="luhborba" height="30" width="40" /></a>
<a href="https://www.youtube.com/@luhborba" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="luciano borba" height="30" width="40" /></a>
</p>