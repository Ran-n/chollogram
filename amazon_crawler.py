#!/usr/bin/python3
#+ Autor:	Ran#
#+ Creado:	11/05/2021 13:31:33
#+ Editado:	12/05/2021 18:16:26

import utils as u

import requests as r
import sys
from bs4 import BeautifulSoup as bs
import os

# coller as opcións dadas na entrada
def getOpcions():
    args = sys.argv[1:]

    if any(['-a' in args, '-h' in args, '?' in args]):
        print('Axuda ------------------')
        print('-a/?/-h\t\t-> Esta mensaxe')
        print('-u catex\t-> Ligazón a utilizar')
        sys.exit()


    if '-u' in args:
        ligazon = args[args.index('-u')+1]
    else:
        sys.exit("ERRO: Non me diches ligazón.")

    return ligazon 

# print da info
def printInfo(tit, prezo_antes, prezo, lig_imaxe, ref_lig):
    print('Artigo:\t\t{}\nPrezo Anterior:\t{}\nPrezo Actual:\t{}\nImaxe:\t\t{}\nLigazón:\t{}'.format(tit, prezo_antes, prezo, lig_imaxe, ref_lig))

# dada unha ligazón simplificaa e devolve a de referal
def tratarLigazon(ligazon, ref_code):
    cachos_ligazon = ligazon.split('?')[0].split('/')

    amazon = [ama for ama in cachos_ligazon if 'www.amazon' in ama][0]

    pais = amazon.split('.')[2]
    if pais == 'es':
        idioma = 'es_ES' 
    elif pais == 'com':
        idioma = 'en_US'

    try:
        ligazon = 'https://'+amazon+'/dp/'+cachos_ligazon[cachos_ligazon.index('dp')+1]
    except:
        ligazon = 'https://'+amazon+'/dp/'+cachos_ligazon[cachos_ligazon.index('gp')+2]

    ref_lig = ligazon+'?&linkCode=ll1&tag='+ref_code+'&language='+idioma+'&ref_=as_li_ss_tl'
    #&aod=1

    return ligazon, ref_lig

# print info produto
def getInfo(ligazon):
    # variables precisas para poder facer os scrapping en amazon
    cabeceira = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/90.0.4430.93 Safari/537.36'
            }
    bolacha = {'from-my': 'browser'}

    # request á url
    pax = r.get(ligazon, headers=cabeceira, cookies=bolacha)
    # parseado
    soup = bs(pax.content, 'html.parser')

    # sacar o título
    tit = soup.find(id='productTitle').get_text().strip()
    # sacar o prezo
    try:
        prezo = soup.find(id='priceblock_ourprice').get_text().strip()
    except NameError:
        prezo = soup.find(id='priceblock_saleprice').get_text().strip()
    except:
        prezo = 'Non Disponhible'

    # sacar o prezo anterior se o ten
    prezo_antes = soup.find(class_='priceBlockStrikePriceString a-text-strike')
    if prezo_antes:
        prezo_antes = u.tachar(prezo_antes.get_text().strip())
    else:
        prezo_antes = u.tachar('Non Disponhible')

    # sacar ligazón da imaxe
    lig_imaxe = soup.find(class_='a-dynamic-image')['data-a-dynamic-image'].split('"')[1]
    
    return tit, prezo_antes, prezo, lig_imaxe

if __name__ == '__main__':
    print()
    id_afiliado = u.cargarConfig('.config', 1)

    ligazon = getOpcions()
    ligazon, ref_lig = tratarLigazon(ligazon, id_afiliado)

    tit, prezo_antes, prezo, lig_imaxe = getInfo(ligazon)
    printInfo(tit, prezo_antes, prezo, lig_imaxe, ref_lig)
    print()
