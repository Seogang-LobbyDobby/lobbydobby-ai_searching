from hanspell import spell_checker

class Sspell():
    def spell(self, input_text):
        results = spell_checker.check(input_text)

        result = ''
        for key, value in results.words.items():
            result += str(key) + ' '
        result = result[:-1]

        return result