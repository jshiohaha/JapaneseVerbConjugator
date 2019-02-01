# Local modules
from .constants.EnumeratedTypes import Polarity

from .PositiveVerbFormGenerator import PositiveVerbForms
from .NegativeVerbFormGenerator import NegativeVerbForms


class JapaneseVerbFormGenerator():
    def __init__(self):
        self.positiveVerbForms = PositiveVerbForms()
        self.negativeVerbForms = NegativeVerbForms()

    def generate_plain_form(self, verb, verb_class, tense, polarity):
        '''Generate the plain form of the verb depending on the tense and 
        polarity.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: plain form of the verb based on the tense and polarity
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_plain_form(verb, verb_class, tense)
        return self.negativeVerbForms.generate_plain_form(verb, verb_class, tense)

    def generate_polite_form(self, verb, verb_class, tense, polarity):
        '''Generate the polite form of the verb depending on the tense and 
        polarity.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: polite form of the verb based on the tense and polarity
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_polite_form(verb, verb_class, tense)
        return self.negativeVerbForms.generate_polite_form(verb, verb_class, tense)

    def generate_te_form(self, verb, verb_class):
        '''Utilize base_te_ta_form function to generate the -te form 
        of the verb

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs

        Returns:
            str: -te form of the verb
        '''
        return self.positiveVerbForms.generate_te_form(verb, verb_class)

    def generate_conditional_form(self, verb, verb_class, formality, polarity):
        '''Generate the conditional form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: conditional form of the verb based on the formality and polarity 
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_conditional_form(verb, verb_class, formality)
        return self.negativeVerbForms.generate_conditional_form(verb, verb_class, formality)

    def generate_volitional_form(self, verb, verb_class, formality, polarity):
        '''Generate the volitional form of the verb depending on the formality. 

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: volitional form of the verb based on the formality and polarity 
        parameters
        '''        
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_volitional_form(verb, verb_class, formality)
        return self.negativeVerbForms.generate_volitional_form(verb, verb_class, formality)

    def generate_potential_form(self, verb, verb_class, formality, polarity):
        '''Generate the potential form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: potential form of the verb based on the formality and polarity 
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_potential_form(verb, verb_class, formality)
        return self.negativeVerbForms.generate_potential_form(verb, verb_class, formality)

    def generate_imperative_form(self, verb, verb_class, formality, polarity):
        '''Generate the imperative form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: imperative form of the verb based on the formality and polarity 
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_imperative_form(verb, verb_class, formality)
        return self.negativeVerbForms.generate_imperative_form(verb, verb_class, formality)

    def generate_provisional_form(self, verb, verb_class, formality, polarity):
        '''Generate the provisional form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: provisional form of the verb based on the formality and polarity 
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_provisional_form(verb, verb_class, formality)
        return self.negativeVerbForms.generate_provisional_form(verb, verb_class, formality)

    def generate_causative_form(self, verb, verb_class, formality, polarity):
        '''Generate the causative form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: causative form of the verb based on the formality and polarity 
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_causative_form(verb, verb_class, formality)
        return self.negativeVerbForms.generate_causative_form(verb, verb_class, formality)

    def generate_passive_form(self, verb, verb_class, formality, polarity):
        '''Generate the passive form of the verb depending on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb 
            polarity (enum): Polarity Enum representing the polarity for the 
                conjugated verb

        Returns:
            str: passive form of the verb based on the formality and polarity 
        parameters
        '''
        if polarity == Polarity.POSITIVE:
            return self.positiveVerbForms.generate_passive_form(verb, verb_class, formality)
        return self.negativeVerbForms.generate_passive_form(verb, verb_class, formality)
