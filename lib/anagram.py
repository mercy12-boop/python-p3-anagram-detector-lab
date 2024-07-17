# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = []
        sorted_word = sorted(self.word)
        for i in word_list:
            if sorted(i) == sorted_word:
                anagrams.append(i)
        return anagrams

listen = Anagram("listen")

print(listen.match(['enlists', 'google', 'inlets', 'banana']))
