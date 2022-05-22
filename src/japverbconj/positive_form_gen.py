# Local modules
from .constants.enumerated_types import Formality, Tense, VerbClass
from .constants.particle_constants import *
from .constants.verb_ending_constants import *
from .utils import (
    base_te_ta_form,
    get_verb_stem,
    handle_irregular_verb,
    map_dictionary_to_a_ending,
    map_dictionary_to_e_ending,
    map_dictionary_to_i_ending,
    map_dictionary_to_o_ending,
)


# ---------------------------------------------------------- #
#                       Positive Verb Forms                  #
# ---------------------------------------------------------- #
class PositiveVerbForms:
    @classmethod
    def generate_plain_form(cls, verb, verb_class, tense):
        """Generate the positive polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb

        Returns:
            str: positive plain form of the verb based on the tense parameter
        """
        if tense == Tense.NONPAST:
            return verb
        return base_te_ta_form(verb, verb_class, TA_PARTICLE, DA_PARTICLE)

    @classmethod
    def generate_polite_form(cls, verb, verb_class, tense):
        """Generate the positive polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb

        Returns:
            str: positive polite form of the verb based on the tense parameter
        """
        if tense == Tense.NONPAST:
            ending = MASU_POSITIVE_NONPAST
        else:
            ending = MASU_POSITIVE_PAST

        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(verb, True, ending, ending, ending)
        else:
            if verb_class == VerbClass.GODAN:
                verb_stem = map_dictionary_to_i_ending(verb)
            else:
                verb_stem = get_verb_stem(verb, verb_class)
            return f"{verb_stem}{ending}"

    @classmethod
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
        return base_te_ta_form(verb, verb_class, TE_PARTICLE, DE_PARTICLE)

    @classmethod
    def generate_conditional_form(cls, verb, verb_class, formality):
        """Generate the positive conditional form of the verb depending
        on the level of formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: positive conditional form of the verb based on the formality
        parameter
        """
        if formality == Formality.PLAIN:
            verb_stem = base_te_ta_form(verb, verb_class, TA_PARTICLE, DA_PARTICLE)
        else:
            verb_stem = cls.generate_polite_form(verb, verb_class, Tense.PAST)
        return f"{verb_stem}{RA_PARTICLE}"

    @classmethod
    def generate_volitional_form(cls, verb, verb_class, formality):
        """Generate the positive volitional form of the verb depending
        on the level of formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: positive volitional form of the verb based on the formality
            parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb,
                suru_ending=VOLITIONAL_SURU_ENDING,
                kuru_ending=VOLITIONAL_KURU_ENDING,
                kuru_kanji_ending=VOLITIONAL_KURU_KANJI_ENDING,
            )
        elif verb_class == VerbClass.GODAN:
            if formality == Formality.PLAIN:
                verb_stem = map_dictionary_to_o_ending(verb)
                ending = U_PARTICLE
            else:
                verb_stem = map_dictionary_to_i_ending(verb)
                ending = VOLITIONAL_POLITE_ENDING
        else:
            verb_stem = get_verb_stem(verb, verb_class)
            if formality == Formality.PLAIN:
                ending = VOLITIONAL_ICHIDAN_PLAIN_ENDING
            else:
                ending = VOLITIONAL_POLITE_ENDING
        return f"{verb_stem}{ending}"

    @classmethod
    def generate_potential_form(cls, verb, verb_class, formality):
        """Generate the positive potential form of the verb depending
        on the level of formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: positive potential form of the verb based on the specified formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                suru_ending = POTENTIAL_SURU_PLAIN_POSITIVE_ENDING
                kuru_ending = POTENTIAL_KURU_PLAIN_POSITIVE_ENDING
                kuru_kanji_ending = POTENTIAL_KURU_KANJI_PLAIN_POSITIVE_ENDING
            else:
                suru_ending = POTENTIAL_SURU_POLITE_POSITIVE_ENDING
                kuru_ending = POTENTIAL_KURU_POLITE_POSITIVE_ENDING
                kuru_kanji_ending = POTENTIAL_KURU_KANJI_POLITE_POSITIVE_ENDING
            return handle_irregular_verb(
                verb, False, suru_ending, kuru_ending, kuru_kanji_ending
            )
        if verb_class == VerbClass.GODAN:
            if formality == Formality.PLAIN:
                verb_stem = map_dictionary_to_e_ending(verb)
                ending = RU_PARTICLE
            else:
                verb_stem = map_dictionary_to_e_ending(verb)
                ending = MASU_POSITIVE_NONPAST
        else:
            verb_stem = get_verb_stem(verb, verb_class)
            if formality == Formality.PLAIN:
                ending = POTENTIAL_ICHIDAN_ENDING
            else:
                ending = POTENTIAL_POLITE_ICHIDAN_ENDING
        return f"{verb_stem}{ending}"

    @classmethod
    def generate_imperative_form(cls, verb, verb_class, formality):
        """Generate the positive imperative form of the verb depending
        on the level of formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: positive imperative form based on the specified formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(
                    verb,
                    suru_ending=IMPERATIVE_SURU_PLAIN_POSITIVE_ENDING,
                    kuru_ending=IMPERATIVE_KURU_PLAIN_POSITIVE_ENDING,
                    kuru_kanji_ending=IMPERATIVE_KURU_KANJI_PLAIN_POSITIVE_ENDING,
                )
            else:
                return f"{cls.generate_te_form(verb, verb_class)}{KUDASAI}"
        if formality == Formality.PLAIN:
            if verb_class == VerbClass.GODAN:
                verb_stem = map_dictionary_to_e_ending(verb)
                ending = ""
            else:
                verb_stem = get_verb_stem(verb, verb_class)
                ending = RO_PARTICLE
        else:
            verb_stem = cls.generate_te_form(verb, verb_class)
            ending = KUDASAI
        return f"{verb_stem}{ending}"

    @classmethod
    def generate_provisional_form(cls, verb, verb_class, formality=None):
        """Generate the positive provisional form of the verb depending
        on the level of formality. No formality parameter required for
        non-irregular verbs.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (:obj: enum, optional): Formality Enum representing the formality class
                for the conjugated verb. Defaults to None.

        Returns:
            str: positive provisional form based on the specified formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                suru_ending = PROVISIONAL_SURU_PLAIN_POSITIVE_ENDING
                kuru_ending = PROVISIONAL_KURU_PLAIN_POSITIVE_ENDING
                kuru_kanji_ending = PROVISIONAL_KURU_KANJI_PLAIN_POSITIVE_ENDING
            else:
                suru_ending = PROVISIONAL_SURU_POLITE_POSITIVE_ENDING
                kuru_ending = PROVISIONAL_KURU_POLITE_POSITIVE_ENDING
                kuru_kanji_ending = PROVISIONAL_KURU_KANJI_POLITE_POSITIVE_ENDING
            return handle_irregular_verb(
                verb, False, suru_ending, kuru_ending, kuru_kanji_ending
            )
        # assuming godan verb
        if verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_e_ending(verb)
            ending = BA_PARTICLE
        else:
            verb_stem = get_verb_stem(verb, verb_class)
            ending = f"{RE_PARTICLE}{BA_PARTICLE}"
        return f"{verb_stem}{ending}"

    @classmethod
    def generate_causative_form(cls, verb, verb_class, formality):
        """Generate the positive causative form of the verb depending
        on the level of formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: positive causative form based on the specified formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb,
                suru_ending=CAUSATIVE_PLAIN_SURU_ENDING,
                kuru_ending=CAUSATIVE_PLAIN_KURU_ENDING,
                kuru_kanji_ending=CAUSATIVE_PLAIN_KURU_KANJI_ENDING,
            )

        if verb_class == VerbClass.GODAN:
            verb_stem = f"{map_dictionary_to_a_ending(verb)}{SE_PARTICLE}"
        else:
            verb_stem = f"{get_verb_stem(verb, verb_class)}{SA_PARTICLE}{SE_PARTICLE}"

        if formality == Formality.PLAIN:
            ending = RU_PARTICLE
        else:
            ending = MASU_POSITIVE_NONPAST
        return f"{verb_stem}{ending}"

    @classmethod
    def generate_passive_form(cls, verb, verb_class, formality):
        """Generate the positive passive form of the verb depending
        on the level of formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: positive passive form based on the specified formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb,
                suru_ending=PASSIVE_SURU_PLAIN_POSITIVE_ENDING,
                kuru_ending=PASSIVE_KURU_PLAIN_POSITIVE_ENDING,
                kuru_kanji_ending=PASSIVE_KURU_KANJI_PLAIN_POSITIVE_ENDING,
            )
        if verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_a_ending(verb)
            if formality == Formality.PLAIN:
                ending = f"{RE_PARTICLE}{RU_PARTICLE}"
            else:
                ending = f"{RE_PARTICLE}{MASU_POSITIVE_NONPAST}"
        else:
            verb_stem = get_verb_stem(verb, verb_class)
            if formality == Formality.PLAIN:
                ending = PASSIVE_ICHIDAN_PLAIN_POSITIVE_ENDING
            else:
                ending = PASSIVE_ICHIDAN_POLITE_POSITIVE_ENDING
        return f"{verb_stem}{ending}"
