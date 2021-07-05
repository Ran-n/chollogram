#! /usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------
#+ Autor:	Ran#
#+ Creado:	05/07/2021 17:47:50
#+ Editado:	05/07/2021 17:55:47
# --------------------------------------------
import json
# --------------------------------------------
# forma bonita de imprimir diccionarios de python
def jprint(diccionario, indent=4, sort=False):
    print(json.dumps(diccionario, indent=indent, sort_keys=sort))
# --------------------------------------------
if __name__ == '__main__':
    print('*> Probas <*')
    print('> jprint')
    print('Imprimindo {"a": 1, "b": 2}:')
    jprint({'a': 1, 'b': 2})

# --------------------------------------------
