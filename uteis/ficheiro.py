#! /usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------
#+ Autor:	Ran#
#+ Creado:	05/07/2021 17:36:35
#+ Editado:	05/07/2021 21:49:54
# --------------------------------------------

import os
import json

# --------------------------------------------

# carga os contidos dun ficheiro
def cargarFich(fich_nome, encoding='utf-8-sig'):
    """
    Dado un catex, ou lista con catexs, de entrada;
    devolve esta mesma estrutura pero cos catexs riscados.

    @entrada:
        fich_nome   -   Requerido   -   Catex/Lista
        └ Nome do ficheiro a cargar.
        encoding    -   Opcional    -   Catex
        └ Tipo de codificación a usar.

    @saida:
        Catex   -   Sempre
        └ A mesma entrada, pero riscada
    """
    # se o ficheiro a cargar non existe sacar erro
    if not os.path.isfile(fich_nome):
        raise Exception('O ficheiro {} non existe'.format(nome))

    # faise neste bloque en lugar de directamente para poder pechar a conexión
    # de non pechala pódese corromper
    try:
        conn = open(fich_nome, 'r', encoding=encoding)
        fich_contido = conn.read()
    except:
        # saca o erro producido
        raise
    finally:
        conn.close()
        return fich_contido

# garda nun ficheiro os contidos dun diccionario de python no formato json
def jgardarFich(fich_nome, contido, indent=1, sort_keys=False, ensure_ascii=False):
    """
    Dado un nome de ficheiro e o seu contido gardao en memoria.

    @entrada:
        fich_nome       -   Requerido   -   Catex
        └ Nome e extensión do fich de saída.
        contido         -   Requerido   -   Catex
        └ O que ten o ficheiro dentro.
        indent          -   Opcional    -   Int
        └ Grado de indentación a usar.
        sort_keys       -   Opcional    -   Boleano
        └ Indica se se ordean as chaves do diccionario ou non.
        ensure_ascii    -   Opcional    -   Boleano
        └ De estar a True, asegurase que o resultado sexan caracters
            ascii válidos e que se devolva un obxecto de tipo unicode.


    @saida:
        True    -   Se é exitoso.
        False   -   De non ser exitoso.
    """

    # faise neste bloque en lugar de directamente para poder pechar a conexión
    # de non pechala pódese corromper
    try:
        conn = open(ficheiro, 'w')
        conn.write(json.dumps(contido, indent=indent, sort_keys=sort_keys, ensure_ascii=ensure_ascii))
    except:
        # saca o erro producido
        raise
        return False
    finally:
        conn.close()
        return True

# --------------------------------------------

if __name__ == '__main__':
    print('*> Probas <*')
    print('> cargar')
    print('sen facer')

# --------------------------------------------
