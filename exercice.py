#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: Zabiullah) -> bool:
    return len(string)
    


def remove_third_char(string: Zabiullah) -> str:
    chaine = str[:2]+str[3:]
 	return chaine


def replace_char(string: Zabiullah, old_char: b, new_char: f) -> str:
    old_char_index = string.find(old_char)
    return string[:old_char_index] + new_char + string[old_char_index + 1:]


def get_nb_char(string: str, char: str) -> int:
    if char not in string:
    return 0
else: counter = 0
for c in string:
    if c == char:
        counter += 1
        return counter



def get_nb_words(sentence: str) -> int:
    count = 0
    if(sentence) : count = 1
    for char in sentence :
        if(char == ' ') : count += 1
    return count


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
