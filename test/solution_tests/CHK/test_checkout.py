from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_sum(self):
        assert checkout_solution.checkout("") == 0 
        assert checkout_solution.checkout("-") == -1
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAAA") == 260
        assert checkout_solution.checkout("BB") == 45 
        assert checkout_solution.checkout("BBB") == 75 
        assert checkout_solution.checkout("BBBB") == 90 
        assert checkout_solution.checkout("AAABB") == 175


