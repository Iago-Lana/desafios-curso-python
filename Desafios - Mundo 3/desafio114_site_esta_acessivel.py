"""
Desafio 114: Crie um código em
Python que testa se o
site Pudim está
acessível pelo
computador usado.
"""
import requests
from requests import RequestException

url = "https://www.pudim.com.br/"

try:
    n = requests.get(url, timeout=5)
except RequestException:
    print('\033[31mO site "Pudim" não está acessível no momento\033[0m')
else:
    print('\033[32mConsegui acessar com sucesso o site "Pudim"\033[0m')