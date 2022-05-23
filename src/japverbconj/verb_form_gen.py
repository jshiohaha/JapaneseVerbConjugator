from .constants.enumerated_types import Polarity
from .copula_gen import Copula
from .decorators import validate_japanese_verb
from .negative_form_gen import NegativeVerbForms
from .positive_form_gen import PositiveVerbForms


class JapaneseVerbFormGenerator:
    positive_verb_forms = PositiveVerbForms
    negative_verb_forms = NegativeVerbForms
    copula = Copula

    @classmethod
    @validate_japanese_verb
    def generate_plain_form(cls, verb, verb_class, tense, polarity):
        """Generate the plain form of the verb depending on the tense and
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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_plain_form(verb, verb_class, tense)
        return cls.negative_verb_forms.generate_plain_form(verb, verb_class, tense)

    @classmethod
    @validate_japanese_verb
    def generate_polite_form(cls, verb, verb_class, tense, polarity):
        """Generate the polite form of the verb depending on the tense and
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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_polite_form(verb, verb_class, tense)
        return cls.negative_verb_forms.generate_polite_form(verb, verb_class, tense)

    @classmethod
    @validate_japanese_verb
    def generate_te_form(cls, verb, verb_class):
        """Utilize base_te_ta_form function to generate the -te form
        of the verb

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs

        Returns:
            str: -te form of the verb
        """
        return cls.positive_verb_forms.generate_te_form(verb, verb_class)

    @classmethod
    @validate_japanese_verb
    def generate_conditional_form(cls, verb, verb_class, formality, polarity):
        """Generate the conditional form of the verb depending on the formality.

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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_conditional_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_conditional_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_volitional_form(cls, verb, verb_class, formality, polarity):
        """Generate the volitional form of the verb depending on the formality.

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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_volitional_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_volitional_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_potential_form(cls, verb, verb_class, formality, polarity):
        """Generate the potential form of the verb depending on the formality.

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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_potential_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_potential_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_imperative_form(cls, verb, verb_class, formality, polarity):
        """Generate the imperative form of the verb depending on the formality.

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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_imperative_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_imperative_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_provisional_form(cls, verb, verb_class, formality, polarity):
        """Generate the provisional form of the verb depending on the formality.

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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_provisional_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_provisional_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_causative_form(cls, verb, verb_class, formality, polarity):
        """Generate the causative form of the verb depending on the formality.

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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_causative_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_causative_form(
            verb, verb_class, formality
        )

    @classmethod
    @validate_japanese_verb
    def generate_passive_form(cls, verb, verb_class, formality, polarity):
        """Generate the passive form of the verb depending on the formality.

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
        """
        if polarity == Polarity.POSITIVE:
            return cls.positive_verb_forms.generate_passive_form(
                verb, verb_class, formality
            )
        return cls.negative_verb_forms.generate_passive_form(
            verb, verb_class, formality
        )
