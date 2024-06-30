#!/usr/bin/env python3

example_text = "Lorem ipsum dolor sit amet"

words_len = [x for x in example_text.split() if len(x) >= 4]
print(words_len)