from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_item_price(self):
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
        assert checkout_solution.checkout("A") == 50
    A = 50
    B = 30
    C = 20
    D = 15
    E = 40
    F = 10
    G = 20
    H = 10
    I = 35
    J = 60
    K = 80
    L = 90
    M = 15
    N = 40
    O = 10
    P = 50
    Q = 30
    R = 50
    S = 30
    T = 20
    U = 40
    V = 50
    W = 20
    X = 90
    Y = 10
    Z = 50

    def test_basket_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid_product(self):
        assert checkout_solution.checkout("-") == -1 


    def test_multiprice_discount(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("BB") == 45 
        assert checkout_solution.checkout("BBB") == 75 
        assert checkout_solution.checkout("BBBB") == 90 
        assert checkout_solution.checkout("AAABB") == 175
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("KK") == 150
        assert checkout_solution.checkout("PPPPP") == 200
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("VV") == 90
        assert checkout_solution.checkout("VVV") == 130

    def test_getfree_discount(self):
        assert checkout_solution.checkout("EEB") == 80 
        assert checkout_solution.checkout("EEBB") == 110 
        assert checkout_solution.checkout("EEEB") == 120 
        assert checkout_solution.checkout("EEEE") == 160 
        assert checkout_solution.checkout("EEEEB") == 160 
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFFF") == 40

        assert checkout_solution.checkout("NNNM") == 120 
        assert checkout_solution.checkout("UUUU") == 120 
        assert checkout_solution.checkout("RRRQ") == 150 

    def test_stacked_discount(self):
        assert checkout_solution.checkout("AAABBBEE") == 255 
        assert checkout_solution.checkout("AAABBEE") == 240




