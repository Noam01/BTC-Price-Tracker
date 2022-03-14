from email import message
import requests
import smtplib
import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from time import sleep
import time



def send_logs():

	fromAddr = config.fromAddr
	fromPswd = config.fromPswd
	toAddr = fromAddr

	subject = f'BTC Kurs'

	msg = MIMEMultipart()
	msg['From'] = fromAddr
	msg['To'] = toAddr
	msg['Subject'] = subject
	body = f'Ihr gewünschter BTC Kurs von {goal_rate} oder weniger wurde erreicht'
	msg.attach(MIMEText(body,'plain'))

	text = msg.as_string()

	s = smtplib.SMTP('smtp.gmail.com',587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(fromAddr,fromPswd)
	s.sendmail(fromAddr,toAddr,text)
	s.close()



def get_current_rate():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : 'A9A8B6A8-D255-4AF7-B26A-9F79F876C82D'}
    response = requests.get(url, headers=headers)

    current = response.json()['rate']

    current_rate = str(current)
    
    return(current_rate)

def get_current_rate1():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : 'A9A8B6A8-D255-4AF7-B26A-9F79F876C82D'}
    response = requests.get(url, headers=headers)

    current = response.json()['rate']

    current_rate = str(current)
    
    print(current_rate)



def compare_current_rate():
    current_rate = get_current_rate()

    if current_rate <= goal_rate:

        send_logs()

        print(f'Der Kurs entspricht deiner Vorstellung von {goal_rate} oder weniger USD')

        print(f'Aktueller Kurs: {current_rate} USD')
    else:
        print(f'Der Kurs entspricht nicht deiner Vorstellung von {goal_rate} USD')
        print(f'Aktueller Kurs: {current_rate} USD')


def track_rate():

    while True:
        print('\ntracke den BTC Kurs')
        compare_current_rate()
        sleep(5)


if __name__ == "__main__":
    programm = input("Möchten Sie den aktuellen Kurs von BTC in USD ausgeben, mit ihrem Wunschkurs vergleichen oder den Kurs von BTC in USD tracken ? (1/2/3)")
    if programm == "1":
        print("Der aktuelle Kurs von BTC in USD beträgt: ")
        get_current_rate1()
    elif programm == "2":
        goal = input(" Bitte geben sie ihren Gewünschten Kurs von BTC in USD an ")

        goal_rate = str(goal)

        ueberpruefung = input(f'{goal_rate} ist ihr gewünschter Kurs? ')

        if ueberpruefung == "ja":
            compare_current_rate()
        else:
            quit()
    elif programm == "3":
        goal = input(" Bitte geben sie ihren Gewünschten Kurs von BTC in USD an ")

        goal_rate = str(goal)

        ueberpruefung = input(f'{goal_rate} ist ihr gewünschter Kurs? ')

        if ueberpruefung == "ja":
            track_rate()
        else:
            quit()
