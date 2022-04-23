from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_item_price(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("G") == 20
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("I") == 35
        assert checkout_solution.checkout("J") == 60
        assert checkout_solution.checkout("K") == 80
        assert checkout_solution.checkout("L") == 90
        assert checkout_solution.checkout("M") == 15
        assert checkout_solution.checkout("N") == 40
        assert checkout_solution.checkout("O") == 10
        assert checkout_solution.checkout("P") == 50
        assert checkout_solution.checkout("Q") == 30
        assert checkout_solution.checkout("R") == 50
        assert checkout_solution.checkout("S") == 30
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("U") == 40
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 90
        assert checkout_solution.checkout("Y") == 10
        assert checkout_solution.checkout("Z") == 50

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
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40

        assert checkout_solution.checkout("NNNM") == 120 
        assert checkout_solution.checkout("UUUU") == 120 
        assert checkout_solution.checkout("RRRQ") == 150 

    def test_stacked_discount(self):
        assert checkout_solution.checkout("AAABBBEE") == 255 
        assert checkout_solution.checkout("AAABBEE") == 240





