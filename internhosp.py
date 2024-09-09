import os
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser

# Função para ler as credenciais do arquivo config.ini
def ler_credenciais():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    usuario_ghosp = config['G-HOSP']['usuario']
    senha_ghosp = config['G-HOSP']['senha']
    
    return usuario_ghosp, senha_ghosp

# Exemplo de uso no script internhosp.py
usuario, senha = ler_credenciais()

# Caminho para o ChromeDriver
chrome_driver_path = "chromedriver.exe"
# Caminho para a pasta de Downloads (ajuste conforme necessário)
from pathlib import Path

# Obtém o caminho da pasta de Downloads do usuário
pasta_downloads = str(Path.home() / "Downloads")

print(f"Pasta de Downloads: {pasta_downloads}")


# Função para encontrar o arquivo mais recente na pasta de Downloads
def encontrar_arquivo_recente(diretorio):
    arquivos = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    arquivos.sort(key=os.path.getmtime, reverse=True)  # Ordena por data de modificação (mais recente primeiro)
    if arquivos:
        return arquivos[0]  # Retorna o arquivo mais recente
    return None

# Função para verificar se a linha segue o padrão desejado
def linha_valida(linha):
    try:
        # Verifica se o primeiro campo é numérico e se o nome está na segunda posição
        return linha[0].isdigit() and len(linha) > 2
    except:
        return False

# Função principal para extrair os nomes
def extrair_nomes():
    # Encontra o arquivo CSV mais recente na pasta de Downloads
    arquivo_recente = encontrar_arquivo_recente(pasta_downloads)

    if not arquivo_recente:
        print("Nenhum arquivo encontrado na pasta de Downloads.")
        return

    print(f"Arquivo mais recente encontrado: {arquivo_recente}")

    # Caminho para salvar o novo arquivo com os nomes extraídos no mesmo local do script
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_novo_arquivo = os.path.join(caminho_atual, 'internados_ghosp.csv')

    # Lista para armazenar os nomes extraídos
    nomes_extraidos = []

    # Abrindo o arquivo CSV original e filtrando as linhas desejadas
    with open(arquivo_recente, newline='', encoding='utf-8') as csvfile:
        leitor_csv = csv.reader(csvfile)
        for linha in leitor_csv:
            if linha_valida(linha):
                # Extrai o nome que está na segunda posição da linha (índice 1)
                nome = linha[1].strip()
                if nome:  # Se o nome não estiver vazio, adiciona à lista
                    nomes_extraidos.append(nome)

    # Salvando o novo arquivo com os nomes extraídos
    with open(caminho_novo_arquivo, 'w', newline='', encoding='utf-8') as novo_csvfile:
        escritor_csv = csv.writer(novo_csvfile)
        for nome in nomes_extraidos:
            escritor_csv.writerow([nome])

    print(f"Nomes extraídos e salvos em {caminho_novo_arquivo}.")

# Inicializa o navegador (Chrome neste caso) usando o serviço
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Maximiza a janela para garantir que todos os elementos estejam visíveis
driver.maximize_window()

# Acesse a página de login do G-HOSP
driver.get('http://10.16.9.43:4001/users/sign_in')

try:
    # Ajustar o zoom para 50% antes do login
    print("Ajustando o zoom para 50%...")
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)  # Aguarda um pouco após ajustar o zoom

    # Realiza o login
    print("Tentando localizar o campo de e-mail...")
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.send_keys(usuario)

    print("Tentando localizar o campo de senha...")
    senha_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_password"))
    )
    senha_field.send_keys(senha)

    print("Tentando localizar o botão de login...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Entrar']"))
    )
    login_button.click()

    time.sleep(5)
    print("Login realizado com sucesso!")

    # Acessar a página de relatórios
    print("Acessando a página de relatórios...")
    driver.get('http://10.16.9.43:4001/relatorios/rc001s')

    # Ajustar o zoom para 60% após acessar a página de relatórios
    print("Ajustando o zoom para 60% na página de relatórios...")
    driver.execute_script("document.body.style.zoom='60%'")
    time.sleep(2)  # Aguarda um pouco após ajustar o zoom

    # Selecionar todas as opções no dropdown "Setor"
    print("Selecionando todos os setores...")
    setor_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "setor_id1"))
    ))
    for option in setor_select.options:
        setor_select.select_by_value(option.get_attribute('value'))

    print("Todos os setores selecionados!")

    # Selecionar o formato CSV
    print("Rolando até o dropdown de formato CSV...")
    formato_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tipo_arquivo"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", formato_dropdown)
    time.sleep(2)

    print("Selecionando o formato CSV...")
    formato_select = Select(formato_dropdown)
    formato_select.select_by_value("csv")

    print("Formato CSV selecionado!")

    # Clicar no botão "Imprimir"
    print("Tentando clicar no botão 'IMPRIMIR'...")
    imprimir_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "enviar_relatorio"))
    )
    imprimir_button.click()

    print("Relatório sendo gerado!")

    # Aguardar alguns segundos para o download ser concluído
    time.sleep(10)  # Ajuste conforme necessário para garantir que o download seja concluído

    # Chamar a função para extrair os nomes do CSV recém-baixado
    extrair_nomes()

except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    driver.quit()
