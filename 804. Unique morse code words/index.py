from string import ascii_lowercase


class Solution:
    def uniqueMorseRepresentations(self, words):
        dict1 = {}
        result = {}
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        for i, c in enumerate(ascii_lowercase):
            dict1[c] = morse[i]
        temp = ""
        for w in words:
            for j in w:
                temp += dict1[j]
            result[temp] = 0
            temp = ""
        return len(result)
