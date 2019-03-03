import calculette

def test_given_deux_nb_then_additionne():
    assert calculette.addition(1,2) == 3
    assert calculette.addition(1,-2) == -1
