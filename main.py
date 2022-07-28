# Desafio: fazer cotação em dolar, euro e ouro, atualizar os valores do banco de dados



#passo 1: pegar cotação dolar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#abrir navegador
navegador = webdriver.Chrome()
#entrar google
navegador.get("https://www.google.com.br/")
#pegar cotação dolar
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print (cotacao_dolar)


#passo 2: pegar cotação euro
#abrir navegador
navegador = webdriver.Chrome()
#entrar google
navegador.get("https://www.google.com.br/")
#pegar cotação euro
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print (cotacao_euro)

#passo 3: pegar cotação ouro
#abrir navegador
navegador = webdriver.Chrome()
#entrar google
navegador.get("https://www.melhorcambio.com/ouro-hoje")
#pegar cotação euro
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print (cotacao_ouro)
navegador.quit()


#passo 4: atualizar base de dados
import pandas as pd
tabela = pd.read_excel("Produtos.xlsx")
print(tabela)


#passo 5: recalcular os preços
    #atualizar cotações
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
#display(tabela)
    #atualizar preço de compra
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
    #atualizar preço de venda
tabela["Preco de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]


print(tabela)

#passo 6: exportar base de dados atualizada
tabela.to_excel("Produtos_Novos.xlsx", index = False)
