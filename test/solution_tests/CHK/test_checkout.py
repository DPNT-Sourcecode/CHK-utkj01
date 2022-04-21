from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_sum(self):
        assert checkout_solution.checkout("ABCDE") == 155

    def test_fixedprice_discount(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAAA") == 260
        assert checkout_solution.checkout("BB") == 45 
        assert checkout_solution.checkout("BBB") == 75 
        assert checkout_solution.checkout("BBBB") == 90 
        assert checkout_solution.checkout("AAABB") == 175

    def test_basket_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid_product(self):
        assert checkout_solution.checkout("-") == -1 

    def test_multipriced_discount(self):
        # assert checkout_solution.checkout("EEB") == 80 
        # assert checkout_solution.checkout("EEEB") == 120 
        # assert checkout_solution.checkout("EEEE") == 160 
        # assert checkout_solution.checkout("EEEEB") == 160 
        assert checkout_solution.checkout("EEEEBB") == 160 

