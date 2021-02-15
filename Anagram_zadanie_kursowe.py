s_1 = 'alal'
s_2 = 'AbAL'
s_3 = 'lala'


def are_anagrams(s_1, s_2, s_3):
    # Tworzymy listę z obu słów, usuwamy ewentualne spacje gdyż anagram może powstać z imion i nazwisk, zamieniamy litery na małe, ponieważ wielkość w tym przypadku ma znaczenie ;)#
    # Sortujemy aby móc porównać zawartość obu nowopowstałych list, te same litery oznaczać będą ten sam zestaw z których zostały stworzone wyrazy#

    s_1_lista = list(s_1.replace(' ', '').lower())
    s_1_lista.sort()

    s_2_lista = list(s_2.replace(' ', '').lower())
    s_2_lista.sort()

    s_3_lista = list(s_3.replace(' ', '').lower())
    s_3_lista.sort()

    return s_1_lista
    return s_2_lista
    return s_3_lista


if (sorted(s_1.replace(' ', '').lower()) == sorted(s_2.replace(' ', '').lower()) == sorted(
        s_3.replace(' ', '').lower())):
    print ('True, Jesteś zwycięzcą')
else:
    print ('False, ***** ***')
