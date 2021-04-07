import wikipedia
from wikipedia import exceptions
import warnings

warnings.catch_warnings()
warnings.simplefilter("ignore")


class Wiki:
    """
    Class to find a wikipedia answer out of the parsed user input
    """
    def __init__(self, text_parsed):
        """
        Initialize :
        - the french language for the wikipedia researches
        - the parsed user input
        - an answer if no wiki has been find
        """
        wikipedia.set_lang("fr")
        self.text_parsed = text_parsed
        self.unfind = ("Ohh un papillon!? "
                       "Tu sais quand j'étais petit les champs étaient remplis de papillon!? "
                       "Il était aussi joli que celui-là. "
                       "Ah oui pardon tu disais? "
                       "Car je crois ne pas avoir de réponse à ce sujet mais regarde ce bel endroit. "
                       "Repose-moi une autre question mais soit plus précis s'il te plaît."
                       )

    def get_wiki_result(self):
        """
        Method to search a result in wikipedia
        if an answer exists then make an output of the 3 first sentences if they are existing
        otherwise send the "unfind" answer from the init
        """
        try:
            find_result = wikipedia.search(self.text_parsed)
            if not find_result:
                return self.unfind
            else:
                wik_page_name = find_result[0]
                description = wikipedia.summary(wik_page_name, sentences=3)
                resume = ("Tu sais que {}."
                          .format(description))
                return resume
        except exceptions.DisambiguationError:
            return self.unfind
        except wikipedia.exceptions.WikipediaException:
            return self.unfind
