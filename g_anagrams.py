def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key] = anagrams.get(key,[]) + [word]
    return anagrams

if __name__ == "__main__":
    words = [word.strip() for word in raw_input("Enter all the words:").split(',')]
    print group_anagrams(words)
