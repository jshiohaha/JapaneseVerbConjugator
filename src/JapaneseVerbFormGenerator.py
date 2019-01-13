# Local modules
from .constants.ParticleConstants import *
from .constants.VerbEndingConstants import *
from .constants.EnumeratedTypes import Formality, Polarity, Tense, VerbClass

# External Libraries
import romkan

# ---------------------------------------------------------- #
#              GENERAL VERB GENERATOR FUNCTIONS              #
# ---------------------------------------------------------- #
def splice_verb(verb, verb_class, should_return_stem=True):
    '''Split Japense verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        str: Verb stem or particle endings based on the value of should_return_stem
    '''
    num_ending_particles = 1
    if verb_class == VerbClass.IRREGULAR:
        num_ending_particles = 2
    if should_return_stem:
        return verb[:-1*num_ending_particles] 
    return verb[-1*num_ending_particles:] 

def handle_irregular_verb(verb, append_stem_particle=False, suru_ending=None, kuru_ending=None):
    ''' Handles irregular verb conjugations depending on suru or kuru verb type.
    Isolates logic of irregular verbs.
    
    Args:
        verb (str): Japanese verb in kana, might contain kanji
        append_stem_particle (bool): verb base particle depends on if the verb is a 
            suru or kuru verb. し particle is appended to suru verbs and き is appended
            to kuru verbs. Not all conjugations require these particles to be appended
            to the verb stem.
        suru_ending (:obj: str, optional): suru verb ending based on the conjugation form.
            Defaults to None.
        kuru_ending (:obj: str, optional): kuru verb ending based on the conjugation form.
            Defaults to None.

    Returns:
        str: irregular verb with appropriate particles and ending attached depending
            on verb conjugation
    '''
    particle_ending = splice_verb(verb, VerbClass.IRREGULAR, False)
    if particle_ending not in [SURU_ENDING, KURU_ENDING]:
        return None

    verb_stem = splice_verb(verb, VerbClass.IRREGULAR)
    ending = ""
    if particle_ending == SURU_ENDING:
        if append_stem_particle:
            ending = SHI_PARTICLE
        if suru_ending is not None:
            ending = "{}{}".format(ending, suru_ending)
    else:
        if append_stem_particle:
            ending = KI_PARTICLE
        if kuru_ending is not None:
            ending = "{}{}".format(ending, kuru_ending)
    return "{}{}".format(verb_stem, ending)

def generate_nai_form(verb, verb_class, is_regular_nai):
    ''' Generates the nai form of a Japanese verb

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        verb_class (enum): VerbClass Enum representing the verb class
            to which the verb belongs
        is_regular_nai (bool): indicates whether to attach nai ending directly
            to verb param or generate the explicit nai form of a verb. Some
            verb conjugations require the nai ending without calculating the 
            nai form

    Returns:
        str: nai ending attached to verb param
    '''
    verb_stem = splice_verb(verb, verb_class)
    ending = NAI_ENDING

    if not is_regular_nai:
        return "{}{}".format(verb, ending)
    if verb_class == VerbClass.IRREGULAR:
        if splice_verb(verb, verb_class, False) == SURU_ENDING:
            ending = "{}{}".format(SHI_PARTICLE, ending)
        else:
            ending = "{}{}".format(KO_PARTICLE, ending)
    else:
        if verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_a_ending(verb)
    return "{}{}".format(verb_stem, ending)

def base_te_ta_form(verb, verb_class, *endings):
    ''' Handle the formation of the -te / -ta form for verbs belonging to
    any verb class. Logic for both forms follows similar logic but differs
    between (-te, -de) and (-ta, -da) based on the last particle of a Godan 
    verb.

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        verb_class (enum): VerbClass Enum representing the verb class
            to which the verb belongs
        *endings: Variable length argument list. Must be in the form (te, de)
        or (ta, da) 
        
        TODO... reformat this logic for *endings

    Returns:
        str: The verb stem plus the -te / -ta particle depending on the 
        verb class. Defaults to None. 
    '''
    if verb_class == VerbClass.IRREGULAR:
        return handle_irregular_verb(verb, True, endings[0], endings[0])
    else:
        verb_stem = splice_verb(verb, verb_class)
        verb_ending = ""
        if verb_class == VerbClass.ICHIDAN:
            verb_ending = endings[0]
        elif verb_class == VerbClass.GODAN:
            last_kana = splice_verb(verb, verb_class, False)
            
            if last_kana in [RU_PARTICLE, TSU_PARTICLE, U_PARTICLE]:
                verb_ending = "{}{}".format(CHISAI_TSU_PARTICLE, endings[0])
            elif last_kana in [BU_PARTICLE, MU_PARTICLE, NU_PARTICLE]:
                verb_ending = "{}{}".format(N_PARTICLE, endings[1])
            elif last_kana in [KU_PARTICLE]:
                verb_ending = "{}{}".format(I_PARTICLE, endings[0])
            elif last_kana in [GU_PARTICLE]:
                verb_ending = "{}{}".format(I_PARTICLE, endings[1])
            elif last_kana in [SU_PARTICLE]:
                verb_ending = "{}{}".format(SHI_PARTICLE, endings[0])
            else:
                return None # TODO no matching particle
        return "{}{}".format(verb_stem, verb_ending)
    return None # TODO (return certain error type?)

def map_dictionary_to_a_ending(verb):
    ''' Generates Godan verb stem with corresponding -a particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -a particle attached (Godan verbs only)
    '''
    return map_dict_form_to_different_ending(verb, 'a', WA_PARTICLE, TA_PARTICLE, SA_PARTICLE)

def map_dictionary_to_e_ending(verb):
    '''Generates Godan verb stem with corresponding -e particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -e particle attached (Godan verbs only)
    '''
    return map_dict_form_to_different_ending(verb, 'e', E_PARTICLE, TE_PARTICLE, SE_PARTICLE)

def map_dictionary_to_i_ending(verb):
    '''Generates Godan verb stem with corresponding -i particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -i particle attached (Godan verbs only)
    '''
    return map_dict_form_to_different_ending(verb, 'i', I_PARTICLE, CHI_PARTICLE, SHI_PARTICLE)

def map_dictionary_to_o_ending(verb):
    '''Generates Godan verb stem with corresponding -o particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -o particle attached (Godan verbs only)
    '''
    return map_dict_form_to_different_ending(verb, 'o', O_PARTICLE, TO_PARTICLE, SO_PARTICLE)

def map_dict_form_to_different_ending(verb, romaji_ending, *special_endings):
    '''Generates Godan verb stem and computes the correct particle to attach based on the
    verb's last kana 

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        romaji_ending (str): target sound of the particle to append to the verb
        *special_endings: Variable length argument list. Based on the target Godan particle 
        class (-a, -e, -i, -o). Order of particles is -u / -tsu / -su.

    Returns:
        str: verb stem with the correct particle attached depending on the last kana particle
    of the Godan verb
    '''
    last_kana = splice_verb(verb, VerbClass.GODAN, False)
    verb_stem = splice_verb(verb, VerbClass.GODAN)

    if last_kana == U_PARTICLE:
        return "{}{}".format(verb_stem, special_endings[0])
    elif last_kana == TSU_PARTICLE:
        return "{}{}".format(verb_stem, special_endings[1])
    elif last_kana == SU_PARTICLE:
        return "{}{}".format(verb_stem, special_endings[2])
    else:
        transformed_last_kana_as_romaji = "{}{}".format(romkan.to_roma(last_kana)[:-1], romaji_ending)
        return "{}{}".format(verb_stem, romkan.to_hiragana(transformed_last_kana_as_romaji))
    return None

# ---------------------------------------------------------- #
#                       Positive Verb Forms                  #
# ---------------------------------------------------------- #
class PositiveVerbForms:
    def generate_plain_form(self, verb, verb_class, tense):
        '''Generate the positive polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb 

        Returns:
            str: positive plain form of the verb based on the tense parameter
        '''
        if tense == Tense.NONPAST:
            return verb
        return base_te_ta_form(verb, verb_class, TA_PARTICLE, DA_PARTICLE)

    def generate_polite_form(self, verb, verb_class, tense):
        '''Generate the positive polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb 

        Returns:
            str: positive polite form of the verb based on the tense parameter
        '''
        ending = MASU_POSITIVE_PAST
        if tense == Tense.NONPAST:
            ending = MASU_POSITIVE_NONPAST
    
        if verb_class == VerbClass.IRREGULAR:
            # ending is the same regardless. Any way to account for this? 
            return handle_irregular_verb(verb, True, ending, ending)
        else:
            verb_stem = splice_verb(verb, verb_class)
            if verb_class == VerbClass.GODAN:
                verb_stem = map_dictionary_to_i_ending(verb)
            # ichidan verb class check is not needed here
            return "{}{}".format(verb_stem, ending)

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
        return base_te_ta_form(verb, verb_class, TE_PARTICLE, DE_PARTICLE)

    def generate_conditional_form(self, verb, verb_class, formality):
        '''Generate the positive conditional form of the verb depending
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
        '''
        if formality == Formality.PLAIN:
            verb = base_te_ta_form(verb, verb_class, TA_PARTICLE, DA_PARTICLE)
        else:
            verb = self.generate_polite_form(verb, verb_class, Tense.PAST)
        return "{}{}".format(verb, RA_PARTICLE)

    def generate_volitional_form(self, verb, verb_class, formality):
        '''Generate the positive volitional form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(verb, suru_ending=VOLITIONAL_SURU_ENDING, kuru_ending=VOLITIONAL_KURU_ENDING)
        else:
            verb_base = ""
            ending = ""
            if verb_class == VerbClass.GODAN:
                # assuming plain formality param
                verb_base = map_dictionary_to_o_ending(verb)
                ending = U_PARTICLE
                if formality == Formality.POLITE:
                    verb_base = map_dictionary_to_i_ending(verb)
                    ending = VOLITIONAL_POLITE_ENDING
            elif verb_class == VerbClass.ICHIDAN:
                verb_base = splice_verb(verb, verb_class)
                # assuming plain formality param
                ending = VOLITIONAL_ICHIDAN_PLAIN_ENDING
                if formality == Formality.POLITE:
                    ending = VOLITIONAL_POLITE_ENDING                  
            else:
                return None # TODO: create return type failure
        return "{}{}".format(verb_base, ending)

    def generate_potential_form(self, verb, verb_class, formality):
        '''Generate the positive potential form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(verb, suru_ending=POTENTIAL_SURU_PLAIN_POSITIVE_ENDING, kuru_ending=POTENTIAL_KURU_PLAIN_POSITIVE_ENDING)
            else:
                return handle_irregular_verb(verb, suru_ending=POTENTIAL_SURU_POLITE_POSITIVE_ENDING, kuru_ending=POTENTIAL_KURU_POLITE_POSITIVE_ENDING)
        else:
            # assuming godan plain form 
            verb_base = map_dictionary_to_e_ending(verb)
            ending = RU_PARTICLE
            
            if verb_class == VerbClass.GODAN:
                if formality == Formality.POLITE:
                    verb_base = map_dictionary_to_e_ending(verb)
                    ending = MASU_POSITIVE_NONPAST
            elif verb_class == VerbClass.ICHIDAN:
                verb_base = splice_verb(verb, verb_class)
                if formality == Formality.PLAIN:
                    ending = POTENTIAL_ICHIDAN_ENDING
                else:
                    ending = POTENTIAL_POLITE_ICHIDAN_ENDING
            return "{}{}".format(verb_base, ending)

    def generate_imperative_form(self, verb, verb_class, formality):
        '''Generate the positive imperative form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(verb, suru_ending=IMPERATIVE_SURU_PLAIN_POSITIVE_ENDING, kuru_ending=IMPERATIVE_KURU_PLAIN_POSITIVE_ENDING)
            else:
                return "{}{}".format(self.generate_te_form(verb, verb_class), KUDASAI)
        else:
            verb_base = self.generate_te_form(verb, verb_class)
            ending = KUDASAI
            if formality == Formality.PLAIN:
                if verb_class == VerbClass.GODAN:
                    return map_dictionary_to_e_ending(verb)
                else:
                    verb_base = splice_verb(verb, verb_class)
                    ending = RO_PARTICLE
            return "{}{}".format(verb_base, ending)

    def generate_provisional_form(self, verb, verb_class, formality=None):
        '''Generate the positive provisional form of the verb depending
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
        '''        
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(verb, suru_ending=PROVISIONAL_SURU_PLAIN_POSITIVE_ENDING, kuru_ending=PROVISIONAL_KURU_PLAIN_POSITIVE_ENDING)
            else:
                return handle_irregular_verb(verb, suru_ending=PROVISIONAL_SURU_POLITE_POSITIVE_ENDING, kuru_ending=PROVISIONAL_KURU_POLITE_POSITIVE_ENDING)
        else:
            # assuming godan verb 
            verb_base = map_dictionary_to_e_ending(verb)
            ending = BA_PARTICLE

            if verb_class == VerbClass.ICHIDAN:
                verb_base = splice_verb(verb, verb_class)
                ending = "{}{}".format(RE_PARTICLE, BA_PARTICLE)
            return "{}{}".format(verb_base, ending)

    def generate_causative_form(self, verb, verb_class, formality):
        '''Generate the positive causative form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(verb, suru_ending=CAUSATIVE_PLAIN_SURU_ENDING, kuru_ending=CAUSATIVE_PLAIN_KURU_ENDING)
        else:
            # TODO FIX ALL THIS LOGIC... GROSS :-P
            if verb_class == VerbClass.GODAN:
                verb_with_a_ending = map_dictionary_to_a_ending(verb)
                if formality == Formality.PLAIN:
                    return "{}{}{}".format(verb_with_a_ending, SE_PARTICLE, RU_PARTICLE)
                else:
                    return "{}{}{}".format(verb_with_a_ending, SE_PARTICLE, MASU_POSITIVE_NONPAST)
            elif verb_class == VerbClass.ICHIDAN:
                verb_stem = splice_verb(verb, verb_class)
                if formality == Formality.PLAIN:
                    return "{}{}{}{}".format(verb_stem, SA_PARTICLE, SE_PARTICLE, RU_PARTICLE)
                else:
                    return "{}{}{}{}".format(verb_stem, SA_PARTICLE, SE_PARTICLE, MASU_POSITIVE_NONPAST)

# ---------------------------------------------------------- #
#                       Negative Verb Forms                  #
# ---------------------------------------------------------- #
class NegativeVerbForms:
    def generate_plain_form(self, verb, verb_class, tense):
        '''Generate the negative polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb 

        Returns:
            str: negative plain form of the verb based on the tense
        parameter
        '''
        verb = generate_nai_form(verb, verb_class, True)
        if tense == Tense.NONPAST:
            return verb
        # force a non-irregular verb class to remove ending -i particle
        return "{}{}".format(splice_verb(verb, VerbClass.NONIRREGULAR), KATTA_ENDING)

    def generate_polite_form(self, verb, verb_class, tense):
        '''Generate the negative polite form of the verb depending
        on the tense.

        Args:
            verb (str): Japanese verb in kana, might contain kanji
            verb_class (enum): VerbClass Enum representing the verb class
                to which the verb belongs
            tense (enum): Tense Enum representing the tense for the conjugated verb 

        Returns:
            str: negative polite form of the verb based on the tense
        parameter
        '''
        ending = MASU_NEGATIVE_PAST
        if tense == Tense.NONPAST:
            ending = MASU_NEGATIVE_NONPAST

        if verb_class == VerbClass.IRREGULAR:
            return handle_irregular_verb(verb, append_stem_particle=True, suru_ending=ending, kuru_ending=ending)
        else:
            verb_base = splice_verb(verb, verb_class)
            if verb_class == VerbClass.GODAN:
                verb_base = map_dictionary_to_i_ending(verb)
            # no change needed for ichidan verb
            return "{}{}".format(verb_base, ending)

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
        return base_te_ta_form(verb, verb_class, TE_PARTICLE, DE_PARTICLE)

    def generate_conditional_form(self, verb, verb_class, formality):
        '''Generate the negative polite form of the verb depending
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
        '''
        if formality == Formality.PLAIN:
            verb = self.generate_plain_form(verb, verb_class, Tense.PAST)
        else:
            verb = self.generate_polite_form(verb, verb_class, Tense.PAST)
        return "{}{}".format(verb, RA_PARTICLE)   

    def generate_volitional_form(self, verb, verb_class, formality):
        '''Generate the negative volitional form of the verb depending
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
        '''
        verb_nai_form = generate_nai_form(verb, verb_class, True)
        if formality == Formality.PLAIN:
            return "{}{}".format(verb_nai_form, VOLITIONAL_PLAIN_COPULA)
        elif formality == Formality.POLITE:
            return "{}{}".format(verb_nai_form, VOLITIONAL_POLITE_COPULA)

    def generate_potential_form(self, verb, verb_class, formality):
        '''Generate the negative potential form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(verb, suru_ending=POTENTIAL_SURU_PLAIN_NEGATIVE_ENDING, kuru_ending=POTENTIAL_KURU_PLAIN_NEGATIVE_ENDING)
            else:
                return handle_irregular_verb(verb, suru_ending=POTENTIAL_SURU_POLITE_NEGATIVE_ENDING, kuru_ending=POTENTIAL_KURU_POLITE_NEGATIVE_ENDING)
        else:
            verb_base = map_dictionary_to_e_ending(verb)

            if verb_class == VerbClass.GODAN:
                if formality == Formality.PLAIN:
                    return generate_nai_form(verb_base, verb_class, False)
                else:
                    return "{}{}".format(verb_base, MASU_NEGATIVE_NONPAST)
            elif verb_class == VerbClass.ICHIDAN:
                verb_base = splice_verb(verb, verb_class)
                verb_with_rare = "{}{}".format(verb_base, "られ")
                if formality == Formality.PLAIN:
                    return generate_nai_form(verb_with_rare, verb_class, False)
                else:
                    return "{}{}".format(verb_with_rare, MASU_NEGATIVE_NONPAST)
    
    def generate_imperative_form(self, verb, verb_class, formality):
        '''Generate the negative imperative form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                return handle_irregular_verb(verb, suru_ending="{}{}".format(SURU_ENDING, NA_PARTICLE), kuru_ending="{}{}".format(KURU_ENDING, NA_PARTICLE))
            else:
                nai_form = generate_nai_form(verb, verb_class, True)
                return "{}{}{}".format(nai_form, DE_PARTICLE, KUDASAI)
        else:
            if formality == Formality.PLAIN:
                return "{}{}".format(verb, NA_PARTICLE)
            else:
                return "{}{}{}".format(generate_nai_form(verb, verb_class, True), DE_PARTICLE, KUDASAI)
    
    def generate_provisional_form(self, verb, verb_class, formality):
        '''Generate the negative provisional form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            if formality == Formality.PLAIN:
                if splice_verb(verb, verb_class, False) == SURU_ENDING:
                    return handle_irregular_verb(verb, append_stem_particle=True, suru_ending=PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING)
                else:
                    return "{}{}".format(KO_PARTICLE, PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING)
            else:
                intermediate_verb = handle_irregular_verb(verb, append_stem_particle=True, suru_ending=MASU_NEGATIVE_NONPAST, kuru_ending=MASU_NEGATIVE_NONPAST)
                return "{}{}{}".format(intermediate_verb, NA_PARTICLE, RA_PARTICLE)
        else:
            verb_stem = splice_verb(verb, verb_class)
            if verb_class == VerbClass.GODAN:
                verb_with_a_ending = map_dictionary_to_a_ending(verb)
                return "{}{}".format(verb_with_a_ending, PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING)
            elif verb_class == VerbClass.ICHIDAN:
                return "{}{}".format(verb_stem, PROVISIONAL_ICHIDAN_PLAIN_NEGATIVE_ENDING)
        return None

    def generate_causative_form(self, verb, verb_class, formality):
        '''Generate the negative causative form of the verb depending
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
        '''
        if verb_class == VerbClass.IRREGULAR:
            if splice_verb(verb, verb_class, False) != SURU_ENDING:
                if formality == Formality.PLAIN: 
                    return generate_nai_form(CAUSATIVE_KURU_NEGATIVE_BASE, verb_class, False)
                else:
                    return "{}{}".format(CAUSATIVE_KURU_NEGATIVE_BASE, MASU_NEGATIVE_NONPAST)
        else:
            verb_stem = splice_verb(verb, verb_class)
            if verb_class == VerbClass.GODAN:
                modified_verb_stem = "{}{}".format(map_dictionary_to_a_ending(verb), SE_PARTICLE)
                if formality == Formality.PLAIN:
                    return generate_nai_form(modified_verb_stem, verb_class, False)
                else:
                    return "{}{}".format(modified_verb_stem, MASU_NEGATIVE_NONPAST)
            elif verb_class == VerbClass.ICHIDAN:
                modified_verb_stem = "{}{}{}".format(verb_stem, SA_PARTICLE, SE_PARTICLE)
                if formality == Formality.PLAIN:
                    return generate_nai_form(modified_verb_stem, verb_class, False)
                else:
                    return "{}{}".format(modified_verb_stem, MASU_NEGATIVE_NONPAST)
