import pandas as pd
import pkg_resources
from symspellpy import SymSpell, Verbosity
from hangul_utils import split_syllable_char, split_syllables, join_jamos


# vocab = pd.read_csv("ko_50k.txt", sep=' ', names=["term", "count"])
# vocab.term = vocab.term.map(split_syllables)
# vocab.to_csv("ko_50k_decomposed.txt", sep=" ", header=None, index=None)


sym_spell = SymSpell(max_dictionary_edit_distance=3)
sym_spell.load_pickle("ko_symspell_50k.pickle")
# dictionary_path = "ko_50k_decomposed.txt"
# sym_spell.load_dictionary(dictionary_path, 0, 1, encoding='UTF8')
# sym_spell.save_pickle("ko_symspell_50k.pickle")

term = str(input())
term = split_syllables(term)

suggestions = sym_spell.lookup(term, Verbosity.ALL, max_edit_distance=3)
print("결과 총 {0}개".format(len(suggestions)))
for sugg in suggestions:
    print(sugg.term, join_jamos(sugg.term), sugg.distance, sugg.count)