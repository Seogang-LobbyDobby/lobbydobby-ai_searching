from symspellpy import SymSpell, Verbosity
from hangul_utils import split_syllable_char, split_syllables, join_jamos


class Spell():
    def __init__(self):
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2)
        self.sym_spell.load_pickle("ko_symspell_50k.pickle")

    def spell(self, term):
        ssterm = split_syllables(term)
        suggestions = self.sym_spell.lookup(ssterm, Verbosity.ALL, max_edit_distance=2)

        try:
            if suggestions[0].distance >= 2:
                return term
            return join_jamos(suggestions[0].term)
        except:
            return term