# -*- coding: utf-8 -*-

import calculette

def test_given_deux_nb_then_additionne():
    assert calculette.addition(1,2) == 3
    assert calculette.addition(1,-2) == -1

def test_given_deux_nb_then_soustrait():
    assert calculette.soustraction(2,1) == 1

def test_given_deux_nb_then_multiplie():
    assert calculette.multiplication(2,3) == 6

def test_given_deux_nb_then_divise():
    assert calculette.division(6,3) == 2
    assert calculette.division(4,0) == "Erreur. Impossible de diviser par 0"
