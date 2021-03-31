import json
import re


class Parser:
    def __init__(self, stopwords):
        self.stopwords = stopwords

    def answer_parser(self, user_input):
        with open(self.stopwords, encoding="utf-8-sig") as json_words:
            words_dict = json.load(json_words)
        recup_answer = re.sub(r'[^\w\s]', " ", str(user_input))
        make_lower = recup_answer.lower()
        sentence_list = make_lower.split()
        sentence_list = list(set(sentence_list))
        i = 0
        while i < len(sentence_list):
            if sentence_list[i] in words_dict:
                sentence_list[i] = ""
            i += 1
        final_output = " ".join(sentence_list)
        final_output = re.sub(" +", " ", final_output)
        sentence = final_output.strip()
        return sentence

# je récupère les infos du fichier 'words.json'
# je supprime les caractères spéciaux inutiles
# je mets tout en miniscule
# je créé une liste à partir de la réponse mise en minuscule
# je supprime les doublons
# si l'élément correspond à un mot interdit alors je le supprime
# je met ma liste modifiée en format string avec des espaces entre les éléments
