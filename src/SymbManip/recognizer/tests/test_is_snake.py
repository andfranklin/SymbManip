from SymbManip.recognizer import recognizer


class TestIsSnake:
    def test_null_string(self):
        assert recognizer.is_snake('') is False

    def test_single_lower(self):
        assert recognizer.is_snake('a') is True

    def test_single_capital(self):
        assert recognizer.is_snake('A') is False

    def test_single_underscore(self):
        assert recognizer.is_snake('_') is False

    def test_underscore_single_capital(self):
        assert recognizer.is_snake('_A') is False

    def test_underscore_single_lower(self):
        assert recognizer.is_snake('_a') is False

    def test_single_digit(self):
        assert recognizer.is_snake('1') is False

    def test_single_capital_underscore(self):
        assert recognizer.is_snake('A_') is False

    def test_single_lower_underscore(self):
        assert recognizer.is_snake('a_') is False

    def test_capital_lower(self):
        assert recognizer.is_snake('Aa') is False

    def test_lower_lower(self):
        assert recognizer.is_snake('aa') is True

    def test_simple_camel(self):
        assert recognizer.is_snake('camelCase') is False

    def test_simple_snake(self):
        assert recognizer.is_snake('snake_case') is True

    def test_simple_pascal(self):
        assert recognizer.is_snake('PascalCase') is False

    def test_simple_kebab(self):
        assert recognizer.is_snake('kebab-case') is False

    def test_complicated_camels(self):
        assert recognizer.is_snake('camelCaseCamelCase') is False

    def test_complicated_snakes(self):
        assert recognizer.is_snake('snake_case_snake_case') is True

    def test_complicated_pascals(self):
        assert recognizer.is_snake('PascalCasePascalCase') is False

    def test_complicated_kebabs(self):
        assert recognizer.is_snake('kebab-case-kebab-case') is False