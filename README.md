# muevy-api-sandbox-pyclient
Exemplos em Python para o consumo da Muevy API Sandbox

# Instruções

## Faça o clone do repositório.

```
git clone https://github.com/Muevy/muevy-api-sandbox-pyclient
```

## Crie o ambiente Python local dentro do diretório muevy-api-sandbox-pyclient

```
python -m venv venv
source venv/bin/activate
```

## Instale as bibliotecas necessárias

```
pip install -r requirements.txt
```

## Configure o config.cfg

```
cp config.cfg.example config.cfg

export MUEVY_API_CONTEXT="SANDBOX"

Observação: Caso seja alterado o nome do bloco dentro do arquivo config.cfg modificar o valor da variável.

Edite o arquivo e altere as variáveis com as informações que foram enviadas pela equipe Muevy Onboarding. 

CONTEXT
VERSION
API_KEY
```

## Realize a primeira chamada de teste

```
./01-check.py
```


## Conheça todas as chamadas Muevy API 

```
Utilize os casos de uso com o payload de requisição e o payload de resposta.
```

# ESTAMOS VERDADEIRAMENTE FELIZES DE TER VOCÊ COMO CLIENTE! SEJA BEM-VINDO!
