# Local modules
from .constants.enumerated_types import Formality, Tense, VerbClass
from .constants.particle_constants import *
from .constants.verb_ending_constants import *
from .utils import (
    generate_nai_form,
    get_ending_particle,
    get_verb_stem,
    handle_irregular_verb,
    map_dictionary_to_a_ending,
    map_dictionary_to_e_ending,
    map_dictionary_to_i_ending,
)


# ---------------------------------------------------------- #
#                       Negative Verb Forms                  #
# ---------------------------------------------------------- #
class NegativeVerbForms:
    @classmethod
    def generate_plain_form(cls, verb, verb_class, tense):
        """Generate the negative plain form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb

        Returns:
            str: negative plain form of the verb based on the tense
        parameter
        """
        nai_form = generate_nai_form(verb, verb_class, True)
        if tense == Tense.NONPAST:
            return nai_form
        else:
            return f"{nai_form[:-1]}{KATTA_ENDING}"

    @classmethod
    def generate_polite_form(cls, verb, verb_class, tense):
        """Generate the negative polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb

        Returns:
            str: negative polite form of the verb based on the tense
        parameter
        """
        if tense == Tense.NONPAST:
            ending = MASU_NEGATIVE_NONPAST
        else:
            ending = MASU_NEGATIVE_PAST

        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(
                verb,
                append_stem_particle=True,
                suru_ending=ending,
                kuru_ending=ending,
                kuru_kanji_ending=ending,
            )
        elif verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_i_ending(verb)
        else:
            verb_stem = get_verb_stem(verb, verb_class)
        return f"{verb_stem}{ending}"

    @classmethod
    def generate_conditional_form(cls, verb, verb_class, formality):
        """Generate the negative conditional form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative conditional form of the verb based on the formality
        parameter
        """
        if formality == Formality.PLAIN:
            verb = cls.generate_plain_form(verb, verb_class, Tense.PAST)
        else:
            verb = cls.generate_polite_form(verb, verb_class, Tense.PAST)
        return f"{verb}{RA_PARTICLE}"

    @classmethod
    def generate_volitional_form(cls, verb, verb_class, formality):
        """Generate the negative volitional form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative volitional form of the verb based on the formality
        parameter
        """
        verb_nai_form = generate_nai_form(verb, verb_class, True)
        if formality == Formality.PLAIN:
            return f"{verb_nai_form}{VOLITIONAL_PLAIN_COPULA}"
        else:
            return f"{verb_nai_form}{VOLITIONAL_POLITE_COPULA}"

    @classmethod
    def generate_potential_form(cls, verb, verb_class, formality):
        """Generate the negative potential form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative potential form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(
                    verb,
                    suru_ending=POTENTIAL_SURU_PLAIN_NEGATIVE_ENDING,
                    kuru_ending=POTENTIAL_KURU_PLAIN_NEGATIVE_ENDING,
                    kuru_kanji_ending=POTENTIAL_KURU_KANJI_PLAIN_NEGATIVE_ENDING,
                )
            else:
                return handle_irregular_verb(
                    verb,
                    suru_ending=POTENTIAL_SURU_POLITE_NEGATIVE_ENDING,
                    kuru_ending=POTENTIAL_KURU_POLITE_NEGATIVE_ENDING,
                    kuru_kanji_ending=POTENTIAL_KURU_KANJI_POLITE_NEGATIVE_ENDING,
                )
        elif verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_e_ending(verb)
        else:
            verb_stem = f"{get_verb_stem(verb, verb_class)}{RA_PARTICLE}{RE_PARTICLE}"
        if formality == Formality.PLAIN:
            return generate_nai_form(verb_stem, verb_class, False)
        else:
            return f"{verb_stem}{MASU_NEGATIVE_NONPAST}"

    @classmethod
    def generate_imperative_form(cls, verb, verb_class, formality):
        """Generate the negative imperative form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative imperative form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(
                    verb,
                    suru_ending=f"{SURU_ENDING}{NA_PARTICLE}",
                    kuru_ending=f"{KURU_ENDING}{NA_PARTICLE}",
                    kuru_kanji_ending=f"{KURU_KANJI_ENDING}{NA_PARTICLE}",
                )
            else:
                nai_form = generate_nai_form(verb, verb_class, True)
                return f"{nai_form}{DE_PARTICLE}{KUDASAI}"
        else:
            if formality == Formality.PLAIN:
                return f"{verb}{NA_PARTICLE}"
            else:
                return (
                    f"{generate_nai_form(verb, verb_class, True)}{DE_PARTICLE}{KUDASAI}"
                )

    @classmethod
    def generate_provisional_form(cls, verb, verb_class, formality):
        """Generate the negative provisional form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative provisional form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                ending_particle = get_ending_particle(verb, verb_class)
                if ending_particle == KURU_ENDING:
                    return f"{KO_PARTICLE}{PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING}"
                else:
                    return handle_irregular_verb(
                        verb,
                        append_stem_particle=True,
                        suru_ending=PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING,
                        kuru_kanji_ending=PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING,
                    )

            else:
                intermediate_verb = handle_irregular_verb(
                    verb,
                    append_stem_particle=True,
                    suru_ending=MASU_NEGATIVE_NONPAST,
                    kuru_ending=MASU_NEGATIVE_NONPAST,
                    kuru_kanji_ending=MASU_NEGATIVE_NONPAST,
                )
                return f"{intermediate_verb}{NA_PARTICLE}{RA_PARTICLE}"
        elif verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_a_ending(verb)
        else:
            verb_stem = get_verb_stem(verb, verb_class)
        return f"{verb_stem}{PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING}"

    @classmethod
    def generate_causative_form(cls, verb, verb_class, formality):
        """Generate the negative causative form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative causative form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.IRREGULAR:
            if get_ending_particle(verb, verb_class) == KURU_ENDING:
                verb_stem = CAUSATIVE_KURU_NEGATIVE_BASE
            else:
                verb_stem = CAUSATIVE_KURU_KANJI_NEGATIVE_BASE
        elif verb_class == VerbClass.GODAN:
            verb_stem = f"{map_dictionary_to_a_ending(verb)}{SE_PARTICLE}"
        else:
            verb_stem = f"{get_verb_stem(verb, verb_class)}{SA_PARTICLE}{SE_PARTICLE}"
        if formality == Formality.PLAIN:
            return generate_nai_form(verb_stem, verb_class, False)
        else:
            return f"{verb_stem}{MASU_NEGATIVE_NONPAST}"

    @classmethod
    def generate_passive_form(cls, verb, verb_class, formality):
        """Generate the negative passive form of the verb depending
        on the formality.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            formality (enum): Formality Enum representing the formality class
                for the conjugated verb

        Returns:
            str: negative passive form of the verb based on the formality
        parameter
        """
        if verb_class == VerbClass.GODAN:
            verb_stem = f"{map_dictionary_to_a_ending(verb)}{RE_PARTICLE}"
        else:
            verb_stem = f"{get_verb_stem(verb, verb_class)}{RA_PARTICLE}{RE_PARTICLE}"
        if formality == Formality.PLAIN:
            return generate_nai_form(verb_stem, verb_class, False)
        else:
            return f"{verb_stem}{MASU_NEGATIVE_NONPAST}"
