import wikipedia
from wikipedia import exceptions
import warnings

warnings.catch_warnings()
warnings.simplefilter("ignore")


class Wikipedia:
    """
    Class to find an wikipedia answer attached to the address found in the class Map
    """
    def __init__(self, address_found):
        """ Initialize the french language for the wikipedia researches and the address coming from the class Map """
        wikipedia.set_lang("fr")
        self.address_found = address_found

    def get_wiki_result(self):
        """ Method to search a result on wikipedia and make an output of the 3 first sentences if they are existing"""
        try:
            find_result = wikipedia.search(self.address_found)
            if not find_result:
                return "Désolé mon petit, je sais où s'est mais je ne connais pas son histoire"
            else:
                wik_page_name = find_result[0]
                description = wikipedia.summary(wik_page_name, sentences=3)
                link_search = wikipedia.page(wik_page_name)
                connect_link = link_search.url
                resume = ("Tu sais que {}. Si cela t'intéresse, voici le lien pour avoir plus de détail: {}"
                          .format(description, connect_link))
                return resume
        except exceptions.DisambiguationError:
            unfind = ("Ohh un papillon!? "
                      "Tu sais quand j'étais petit les champs étaient remplis de papillon!? "
                      "Il était aussi joli que celui-là. "
                      "Tu viens on va manger une pomme. "
                      "Ah oui pardon tu disais? "
                      "Car je crois ne pas avoir de réponse à ce sujet. "
                      "Reposes moi une autre question mais soit plus précis s'il te plait.")
            return unfind



