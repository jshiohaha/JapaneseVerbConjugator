# Local modules
from .constants.ParticleConstants import *
from .constants.VerbEndingConstants import *
from .constants.EnumeratedTypes import Formality, Polarity, Tense, VerbClass

# External Libraries
import romkan

# ---------------------------------------------------------- #
#              GENERAL VERB GENERATOR FUNCTIONS              #
# ---------------------------------------------------------- #
def get_verb_stem(verb, verb_class):
    ''' Parse Japense verb stem from entire verb 

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        str: Main verb stem, which varies depending on verb class
    '''
    num_ending_particles = 1
    if verb_class == VerbClass.IRREGULAR:
        num_ending_particles = 2
    return verb[:-1*num_ending_particles]

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
    particle_ending = verb[-2:]
    if particle_ending not in [SURU_ENDING, KURU_ENDING]:
        return None

    verb_stem = get_verb_stem(verb, VerbClass.IRREGULAR)
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
    last_kana = verb[-1:]
    verb_stem = get_verb_stem(verb, VerbClass.GODAN)

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