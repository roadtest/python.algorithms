#!/usr/bin/env python3
def reverse_words(sentence):
    if not sentence:
        return False

    str_len = len(sentence)
    return " ".join(sentence.split()[::-1])

if __name__ == '__main__': 
  assert reverse_words("We love Python") == "Python love We", "wrong output"
