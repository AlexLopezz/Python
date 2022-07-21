'''Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.'''
'''
list = ['a','b','c']
list2 = ['a','b','c']

print(list  == list2) '''

def palindromo(listWords):
    reverseWords = listWords.copy()
    reverseWords.reverse()
    return listWords == reverseWords

listWords = ['a','l','l','a']
print(f"La palabra {listWords} es palindromo? \nRespuesta: {palindromo(listWords)}")