import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from getpass import getpass
import socket 
from cProfile import label
from cgitb import text
from dataclasses import replace
from multiprocessing.sharedctypes import Value
from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import billboard


def send_msg(text):
    token=''#YOUR TOKEN (TELEGRAM)
    chat_id=""#THE CHAT ID OF THE PERSON YOU WANT TO SEND THE MESSAGE TO
    results=url_req="https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="+text
    requests.get(url_req)


infos_foot365="https://www.footmercato.net/"
infos_binance="https://coinmarketcap.com/fr/"
infos_billboard="https://www.billboard.com/charts/hot-100/"
infos_meteo="https://weather.com/fr-CI/temps/aujour/l/IVXX3721:1:IV?Goto=Redirected"

r_infos_foot_mercato=requests.get(infos_foot365)
response_r_infos_foot_mercato=BeautifulSoup(r_infos_foot_mercato.text,"html.parser")
tableau_infos_foot_mercato=response_r_infos_foot_mercato.find_all(class_="articleFlash__title")





r_infos_binance=requests.get(infos_binance)
response_r_infos_binance=BeautifulSoup(r_infos_binance.text,"html.parser")
tableau_infos_binance=response_r_infos_binance.find_all(class_="sc-1eb5slv-0 iworPT")

r_infos_binance_price=requests.get(infos_binance)
response_r_infos_binance_price=BeautifulSoup(r_infos_binance_price.text,"html.parser")
tableau_infos_binance_price=response_r_infos_binance_price.find_all(class_="sc-1ow4cwt-1 ieFnWP")


TOP_CRYPTO_CUMUL=tableau_infos_binance[9].text+" Is in the top 5 cryptocurrency on CoinMarketCap  "+"and is cap market is : "+tableau_infos_binance_price[0].text+"\n"+"\n"+tableau_infos_binance[10].text+"\n"+" Is in the top 5 cryptocurrency on CoinMarketCap "+"and is cap market is : "+tableau_infos_binance_price[1].text+"\n"+"\n"+tableau_infos_binance[11].text+"\n"+" Is in the top 5 cryptocurrency on CoinMarketCap "+"and is cap market is : "+tableau_infos_binance_price[2].text+"\n"+"\n"+tableau_infos_binance[12].text+" Is in the top 5 cryptocurrency on CoinMarketCap "+"\n"+"and is cap market is : "+tableau_infos_binance_price[3].text+"\n"+"\n"+tableau_infos_binance[13].text+"\n"+" Is in the top 5 cryptocurrency on CoinMarketCap "+"and is cap market is : "+tableau_infos_binance_price[4].text



chart=billboard.ChartData('hot-100')
song1=chart[0]
song2=chart[1]
song3=chart[2]
song4=chart[3]
song5=chart[4]


final_song=song1.title+" by : "+song1.artist+"\n"+song2.title+" by : "+song2.artist+"\n"+song3.title+" by : "+song3.artist+"\n"+song4.title+" by : "+song4.artist+"\n"+song5.title+" by : "+song5.artist


r_infos_meteo=requests.get(infos_meteo)
response_r_infos_meteo=BeautifulSoup(r_infos_meteo.text,"html.parser")
tableau_infos_meteo=response_r_infos_meteo.find_all(class_="CurrentConditions--tempValue--3a50n")

final_meteo="Il fait :  " ,tableau_infos_meteo[0].text,"à Abidjan"
final_meteo=str(final_meteo)



    

send_msg("LE FOOTBALL")
send_msg(tableau_infos_foot_mercato[0].text)
send_msg(tableau_infos_foot_mercato[1].text)
send_msg(tableau_infos_foot_mercato[2].text)
send_msg(tableau_infos_foot_mercato[3].text)
send_msg(tableau_infos_foot_mercato[4].text)
send_msg(tableau_infos_foot_mercato[5].text)
send_msg(tableau_infos_foot_mercato[6].text)
send_msg(tableau_infos_foot_mercato[7].text)
send_msg(tableau_infos_foot_mercato[8].text)
send_msg(tableau_infos_foot_mercato[9].text)
send_msg("CRTYPTOCURRENCY")
send_msg(TOP_CRYPTO_CUMUL)
send_msg("BILLBOARD")
send_msg(final_song)
send_msg("METEO")
send_msg(final_meteo)
