import json
import re


class Parser:
    """
    Class for parsing the user input before we can find an address and a wiki answer.
    """
    def __init__(self, stopwords):
        """
        Initializing the "stopwords" list
        """
        self.stopwords = stopwords

    def answer_parser(self, user_input):
        """
        Method to:
        - open the "stop words" file
        - From the user input : delete de useless character and make everything lower
        - make a loop to check one by one the words (from user input)
        if they are in the "stop words" list or not. If yes we delete them.
        - delete the useless blank and return the parsed answer
        """
        with open(self.stopwords, encoding="utf-8-sig") as json_words:
            words_dict = json.load(json_words)
        recup_answer = re.sub(r'[^\w\s]', " ", str(user_input))
        make_lower = recup_answer.lower()
        sentence_list = make_lower.split()
        i = 0
        while i < len(sentence_list):
            if sentence_list[i] in words_dict:
                sentence_list[i] = ""
            i += 1
        final_output = " ".join(sentence_list)
        final_output = re.sub(" +", " ", final_output)
        sentence = final_output.strip()
        return sentence

