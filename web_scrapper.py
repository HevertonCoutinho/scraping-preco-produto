import requests
from bs4 import BeautifulSoup 
import smtplib
import email.message

#arquivo = open('testes.csv', encoding='utf-8')
#ler_arquivo = pd.read_csv(arquivo)

URL = "https://www.siteexemplo.com.br/produto"
#URL.append(ler_arquivo)
print(URL)
#gravando as linhas
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=headers) #buscar e guardar minhas informações

soup = BeautifulSoup(site.content, 'html.parser')   #guardar todo o meu html da página
##print(soup.prettify()) #trazer todo o html da página

title = soup.find('h1', class_ = 'product-main__name').get_text()#utiliza claas com _ para palavra reservada.
print(title)

price = soup.find('strong', class_ = 'skuPrice').get_text()#buscando preço do produto
print(price)


num_price = price[3:7] #mantendo numeros
num_price = num_price.replace(',','')#retirando ponto e virgula
num_price = num_price.replace('.','')#retirando ponto e virgula
num_price = float(num_price)
print(num_price)

def send_email():#dados da mensagem
    email_content = 'mensagem' #Mensagem que vai no corpo do email
    msg = email.message.Message()
    msg['subject'] = 'O preço de alguns produtos baixaram!!!'#Assunto do email

    msg ['From'] = 'remetente@gmail.com'
    msg ['To'] = 'Destinatario@gmail.com'
    password = '' #senha do email ou senha de aplicativo(desenvolvedor)
    msg.add_header('Content_Tipe', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print('Sucesso ao enviar a mensagem!')
if (num_price < 400):
    send_email()
