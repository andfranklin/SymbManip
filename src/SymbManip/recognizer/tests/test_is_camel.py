from SymbManip.recognizer import recognizer


class TestIsCamel:
    def test_null_string(self):
        assert recognizer.is_camel('') is False

    def test_single_lower(self):
        assert recognizer.is_camel('a') is True

    def test_single_capital(self):
        assert recognizer.is_camel('A') is False

    def test_single_underscore(self):
        assert recognizer.is_camel('_') is False

    def test_underscore_single_capital(self):
        assert recognizer.is_camel('_A') is False

    def test_underscore_single_lower(self):
        assert recognizer.is_camel('_a') is False

    def test_single_digit(self):
        assert recognizer.is_camel('1') is False

    def test_single_capital(self):
        assert recognizer.is_camel('A') is False

    def test_single_lower(self):
        assert recognizer.is_camel('a') is True

    def test_single_capital_underscore(self):
        assert recognizer.is_camel('A_') is False

    def test_single_lower_underscore(self):
        assert recognizer.is_camel('a_') is False

    def test_capital_lower(self):
        assert recognizer.is_camel('Aa') is False

    def test_lower_lower(self):
        assert recognizer.is_camel('aa') is True

    def test_simple_camel(self):
        assert recognizer.is_camel('camelCase') is True

    def test_simple_snake(self):
        assert recognizer.is_camel('snake_case') is False

    def test_simple_pascal(self):
        assert recognizer.is_camel('PascalCase') is False

    def test_simple_kebab(self):
        assert recognizer.is_camel('kebab-case') is False

    def test_complicated_camels(self):
        assert recognizer.is_camel('camelCaseCamelCase') is True

    def test_complicated_snakes(self):
        assert recognizer.is_camel('snake_case_snake_case') is False

    def test_complicated_pascals(self):
        assert recognizer.is_camel('PascalCasePascalCase') is False

    def test_complicated_kebabs(self):
        assert recognizer.is_camel('kebab-case-kebab-case') is False