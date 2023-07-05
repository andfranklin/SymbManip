from SymbManip.recognizer import recognizer


class TestIsSnake:
    def test_null_string(self):
        assert recognizer.is_kebab('') is False

    def test_single_lower(self):
        assert recognizer.is_kebab('a') is True

    def test_single_capital(self):
        assert recognizer.is_kebab('A') is False

    def test_single_underscore(self):
        assert recognizer.is_kebab('_') is False

    def test_underscore_single_capital(self):
        assert recognizer.is_kebab('_A') is False

    def test_underscore_single_lower(self):
        assert recognizer.is_kebab('_a') is False

    def test_single_digit(self):
        assert recognizer.is_kebab('1') is False

    def test_single_capital_underscore(self):
        assert recognizer.is_kebab('A_') is False

    def test_single_lower_underscore(self):
        assert recognizer.is_kebab('a_') is False

    def test_capital_lower(self):
        assert recognizer.is_kebab('Aa') is False

    def test_lower_lower(self):
        assert recognizer.is_kebab('aa') is True

    def test_simple_camel(self):
        assert recognizer.is_kebab('camelCase') is False

    def test_simple_snake(self):
        assert recognizer.is_kebab('snake_case') is False

    def test_simple_pascal(self):
        assert recognizer.is_kebab('PascalCase') is False

    def test_simple_kebab(self):
        assert recognizer.is_kebab('kebab-case') is True

    def test_complicated_camels(self):
        assert recognizer.is_kebab('camelCaseCamelCase') is False

    def test_complicated_snakes(self):
        assert recognizer.is_kebab('snake_case_snake_case') is False

    def test_complicated_pascals(self):
        assert recognizer.is_kebab('PascalCasePascalCase') is False

    def test_complicated_kebabs(self):
        assert recognizer.is_kebab('kebab-case-kebab-case') is True