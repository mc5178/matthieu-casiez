class FrenchStemmer:

    def __init__(self):

        # Liste des suffixes personnalisés

        self.custom_suffixes = sorted([
            'able', 'ace', 'age', 'aie', 'ain', 'aine', 'aire', 'ais', 'aise', 'ard', 'asse', 'ation',
            'eau', 'elle', 'ement', 'er', 'erie', 'eron', 'eronne', 'esse', 'et', 'ette', 'eté', 'eur', 'euse',
            'ible', 'ien', 'ienne', 'ier', 'isation', 'iser', 'isme', 'iste', 'ière',
            'ment',
            'ois', 'oise', 'on',
            'teur', 'tion', 'trice', 'té',
            'âtre',
            'é', 'ée', 'éen', 'éenne'
        ], key=lambda x: -len(x))

        # Liste des terminaisons verbales

        self.verb_endings = sorted([
            # Présent
            'e', 'es', 'eons', 'ez', 'ent', 'is', 'it', 'issons', 'issez', 'issent', 's', 't', 'ons', 'ez', 'ent',
            # Imparfait
            'ais', 'ait', 'ions', 'iez', 'aient', 'issais', 'issait', 'issions', 'issiez', 'issaient',
            # Futur
            'erai', 'eras', 'era', 'erons', 'erez', 'eront', 'irai', 'iras', 'ira', 'irons', 'irez', 'iront',
            # Conditionnel
            'erais', 'erait', 'erions', 'eriez', 'eraient', 'irais', 'irait', 'irions', 'iriez', 'iraient',
            # Passé Simple
            'ai', 'as', 'a', 'âmes', 'âtes', 'èrent', 'is', 'it', 'îmes', 'îtes', 'irent',
            # Participes
            'ant', 'é', 'ée', 'és', 'ées', 'issant', 'i'
        ], key=lambda x: -len(x))

    def stem(self, word):
        """
        Applique un stemming basique à un mot français.
        """
        word = word.lower()

        # Suppression du 's' final, sauf exceptions
        if word.endswith('s'):
            word = word[:-1]
        elif word.endswith('oux'):
            word = word[:-1]

        # Suppression des suffixes personnalisés
        for suffix in self.custom_suffixes:
            if word.endswith(suffix) and len(word) - len(suffix) >= 4:
                word = word[:-len(suffix)]

        # Suppression des terminaisons verbales
        for ending in self.verb_endings:
            if word.endswith(ending) and len(word) - len(ending) >= 4:
                word = word[:-len(ending)]

        return word

# Exemple d'utilisation

stemmer = FrenchStemmer()
words = ["nationalisation", "boulangère", "parlent", "mangeaient", "jolie", "mangeais", "chanteuse", "chanteur", "fabrication", "déstandardisation"]