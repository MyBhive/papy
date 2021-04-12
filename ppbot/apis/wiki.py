import wikipedia
from wikipedia import exceptions
import warnings

warnings.catch_warnings()
warnings.simplefilter("ignore")


class Wiki:
    """
    Class to find a wikipedia answer out of the parsed user input
    """
    def __init__(self, text_parsed, address, geocode):
        """
        Initialize :
        - the french language for the wikipedia researches
        - the parsed user input
        - an answer if no wiki has been find
        """
        wikipedia.set_lang("fr")
        self.text_parsed = text_parsed
        self.address = address
        self.geocode = geocode
        self.unfind = ("Ohh un papillon!? "
                       "Tu sais quand j'étais petit les champs étaient remplis de papillon!? "
                       "Il était aussi joli que celui-là. "
                       "Ah oui pardon tu disais? "
                       "tu voulais voir : {} ou je me trompe? Je ne sais que te dire.. "
                       "Repose-moi une autre question mais soit plus précis s'il te plaît."
                       .format(address)
                       )

    def get_wiki_result(self):
        """
        Method to search a result in wikipedia
        if an answer exists then make an output of the 2 first sentences if they are existing
        otherwise send the "unfind" answer from the init
        """
        try:
            find_result = wikipedia.search(self.text_parsed)
            print(find_result)
            if not find_result:
                return self.unfind
            else:
                wik_page_name = find_result[0]
                description = wikipedia.summary(wik_page_name, sentences=2)
                resume = ("Alors alors! A ce que je comprends, "
                          "tu veux l'endroit à cette adresse: {}? "
                          "Non mais tu sais que {}."
                          .format(self.address, description))
                return resume
        except exceptions.DisambiguationError:
            use_coordinate = self.geocode
            description = wikipedia.geosearch(use_coordinate['lat'], use_coordinate['lng'])
            alternative_result = wikipedia.summary(description)
            alternative_answer = "{} Si ce n'est pas la réponse que tu attendais " \
                                 "alors soit plus précis. Tu vois, si je te dis par exemple: 'Paris'. " \
                                 "Ca veut dire quoi? La célébrité? la ville? le défis? " \
                                 "Allons mon petiot tu peux le faire!".format(alternative_result)
            return alternative_answer
        except wikipedia.exceptions.WikipediaException:
            return self.unfind
