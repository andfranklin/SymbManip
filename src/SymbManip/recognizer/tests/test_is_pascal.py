from SymbManip.recognizer import recognizer


class TestIsPascal:
    def test_null_string(self):
        assert recognizer.is_pascal('') is False

    def test_single_lower(self):
        assert recognizer.is_pascal('a') is False

    def test_single_capital(self):
        assert recognizer.is_pascal('A') is True

    def test_single_underscore(self):
        assert recognizer.is_pascal('_') is False

    def test_underscore_single_capital(self):
        assert recognizer.is_pascal('_A') is False

    def test_underscore_single_lower(self):
        assert recognizer.is_pascal('_a') is False

    def test_single_digit(self):
        assert recognizer.is_pascal('1') is False

    def test_single_capital_underscore(self):
        assert recognizer.is_pascal('A_') is False

    def test_single_lower_underscore(self):
        assert recognizer.is_pascal('a_') is False

    def test_capital_lower(self):
        assert recognizer.is_pascal('Aa') is True

    def test_lower_lower(self):
        assert recognizer.is_pascal('aa') is False

    def test_simple_camel(self):
        assert recognizer.is_pascal('camelCase') is False

    def test_simple_snake(self):
        assert recognizer.is_pascal('snake_case') is False

    def test_simple_pascal(self):
        assert recognizer.is_pascal('PascalCase') is True

    def test_simple_kebab(self):
        assert recognizer.is_pascal('kebab-case') is False

    def test_complicated_camels(self):
        assert recognizer.is_pascal('camelCaseCamelCase') is False

    def test_complicated_snakes(self):
        assert recognizer.is_pascal('snake_case_snake_case') is False

    def test_complicated_pascals(self):
        assert recognizer.is_pascal('PascalCasePascalCase') is True

    def test_complicated_kebabs(self):
        assert recognizer.is_pascal('kebab-case-kebab-case') is False