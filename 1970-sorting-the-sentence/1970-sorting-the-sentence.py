class Solution:
    def sortSentence(self, s: str) -> str:
        sentence_list = s.split(" ")
        
        ordered_sentence_list = [" "] * len(sentence_list)
        for word in sentence_list:
            ordered_sentence_list[int(word[-1]) -1] = word[:-1]
        return " ".join(ordered_sentence_list)

        