import wikipedia
from wikipedia import exceptions
import warnings

warnings.catch_warnings()
warnings.simplefilter("ignore")


class Wiki:
    """
    Class to find an wikipedia answer attached to the address found in the class Map
    """
    def __init__(self, text_parsed):
        """ Initialize the french language for the wikipedia researches and the address coming from the class Map """
        wikipedia.set_lang("fr")
        self.text_parsed = text_parsed
        self.unfind = ("Ohh un papillon!? "
                       "Tu sais quand j'étais petit les champs étaient remplis de papillon!? "
                       "Il était aussi joli que celui-là. "
                       "Tu viens on va manger une pomme. "
                       "Ah oui pardon tu disais? "
                       "Car je crois ne pas avoir de réponse à ce sujet. "
                       "Reposes moi une autre question mais soit plus précis s'il te plait.")

    def get_wiki_result(self):
        """ Method to search a result on wikipedia and make an output of the 3 first sentences if they are existing"""
        try:
            find_result = wikipedia.search(self.text_parsed)
            if not find_result:
                return "C'est rigolo ce que tu demandes! Tu sais que je suis un peu gâteux. Oh regarde ce belle endroit"
            else:
                wik_page_name = find_result[0]
                description = wikipedia.summary(wik_page_name, sentences=3)
                link_search = wikipedia.page(wik_page_name)
                connect_link = link_search.url
                resume = ("Tu sais que {}. Si cela t'intéresse, voici le lien pour avoir plus de détail: {}"
                          .format(description, connect_link))
                return resume
        except exceptions.DisambiguationError:
            return self.unfind
        except wikipedia.exceptions.WikipediaException:
            return self.unfind
