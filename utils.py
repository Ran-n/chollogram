#! /usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	12/05/2021 17:49:06
#+ Editado:	05/07/2021 20:21:36
# -----------------------------------------------------------------------------------------
from uteis.ficheiro import cargar
import sys
# -----------------------------------------------------------------------------------------
# cargar as variables de configuración
def cargarConfig(nome_ficheiro='.config', elemento=0):
    config = {'id_afiliado': '',
            'token_bot': '',
            'nome_canle1': ''
            }
    try:
        for dato in cargar(nome_ficheiro).split('\n')[:-1]:
            try:
                if (not dato.startswith('#')) and dato != '':
                    dato1, dato2 = dato.strip().split('=')
                    config[dato1.strip()] = dato2.strip()
            except:
                sys.exit('ERRO: Pon o identificador e un igual (=) e o seu valor')
    except:
        sys.exit('ERRO: Pon cada elemento da configuración na súa linha')

    # 0 == Tódolos
    if elemento == 0:
        return config
    # 1 == 1º
    elif elemento == 1:
        return config['id_afiliado']
    elif elemento == -1:
        return config['token_bot'], config['nome_canle1']
    # 2 == 2º
    elif elemento == 2:
        return config['token_bot']
    # 3 == 3º
    elif elemento == 3:
        return config['nome_canle1']
# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Por exemplo carga do ficheiro .config: ', cargarConfig())
# -----------------------------------------------------------------------------------------
