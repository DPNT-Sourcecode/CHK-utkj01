from solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        skus = "ABC"
        assert checkout_solution.checkout(skus) == 3
