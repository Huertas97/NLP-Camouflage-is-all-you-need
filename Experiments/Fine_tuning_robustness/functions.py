from typing import Callable, Iterator, Dict, List, Tuple, TYPE_CHECKING
from pyleetspeak.pyleetspeak import WordCamouflage_Augmenter
# from pyleetspeak import WordCamouflage_Augmenter

import spacy
import random
from spacy.training import Example

import warnings

warnings.filterwarnings("ignore")

# Keep in mind that the augmenter should yield all examples you want to use in your corpus, not only the augmented examples (unless you want to augment all examples).
# The augmenter should yield the original example as well as the augmented example. [preferred]
# Or you can yield the original example or the augmented example, but not both.


@spacy.registry.augmenters("wordcamouflage_augmenter.v1")
def wordcamouflage_augmenter(
    level: float,  # level (float): The percentage of texts that will be augmented.
    extractor_type: str,  # "yake" or "keybert"
    # leet_mode: str,
    method: List[str] = None, 
    max_top_n: int = 5,  # Number of keywords to extract
    seed: int = None,  # Seed for random number generator
    lang: str = "en",  # Language of the text
    leet_change_prb: float = 0.8,  # Probability of applying leetspeak
    leet_change_frq: float = 0.5,  # Frequency of applying leetspeak
    leet_uniform_change: float = 0.6,  # Probability of applying uniform change in leetspeak
    punt_hyphenate_prb: float = 0.5,  # Probability of hyphenating words
    punt_uniform_change_prb: float = 0.6,  # Probability of applying uniform change in punctuation
    punt_word_splitting_prb: float = 0.5,  # Probability of splitting words
    inv_max_dist: int = 4,  # Maximum distance between words to be inverted
    inv_only_max_dist_prb: float = 0.5,  # Probability of inverting only words with maximum distance
    leet_punt_prb: float = 0.9,  # Probability of applying leetspeak and punctuation
    leet_prb: float = 0.45,  # Probability of applying leetspeak
    punct_prb: float = 0.25,  # Probability of applying punctuation
    leet_basic_punt_prb: float = 0.15,  # Probability of applying basic punctuation
    leet_covid_basic_punt_prb: float = 0.15,  # Probability of applying basic punctuation
):
    def augment(nlp, example):
        # print("---> Example:")
        # No augmentation
        if random.random() >= level:
            # print("---> Original text:")
            # print(type(example), example)
            # print()
            yield example

        # Augment
        else:
            # print("---> Modified text:")
            augmenter = WordCamouflage_Augmenter.augmenter(
                extractor_type=extractor_type,
                max_top_n=max_top_n,
                method = method,
                # leet_mode = leet_mode,
                # seed=seed,
                lang=lang,
                leet_change_prb=leet_change_prb,
                leet_change_frq=leet_change_frq,
                leet_uniform_change=leet_uniform_change,
                punt_hyphenate_prb=punt_hyphenate_prb,
                punt_uniform_change_prb=punt_uniform_change_prb,
                punt_word_splitting_prb=punt_word_splitting_prb,
                inv_max_dist=inv_max_dist,
                inv_only_max_dist_prb=inv_only_max_dist_prb,
                leet_punt_prb=leet_punt_prb,
                leet_prb=leet_prb,
                punct_prb=punct_prb,
                leet_basic_punt_prb=leet_basic_punt_prb,
                leet_covid_basic_punt_prb=leet_covid_basic_punt_prb,
            )
            text = example.text
            augmented_text = augmenter.transform(text)
            # augmented_text = "augmented text"

            # Create augmented training example
            # Create doc from augmented text
            augmented_doc = nlp.make_doc(augmented_text)

            # Extract label from original example
            original_example_dict = example.to_dict()
            gold_dict = {}
            gold_dict["cats"] = original_example_dict["doc_annotation"]["cats"]

            # print("Augmented Doc:", augmented_doc)
            # print("Gold dict:", gold_dict)
            # Create augmented example using augmented doc and original label
            aug_example = Example.from_dict(augmented_doc, gold_dict)
            # print(type(aug_example), aug_example)
            # print("Original example:", example)
            # print()

            # Original example followed by augmented example
            # This way the corpus will have the original example and the augmented example
            # yield example
            yield aug_example

    return augment


@spacy.registry.augmenters("spongebob_augmenter.v1")
def create_augmenter(level: float = 0.7):
    def augment(nlp, example):

        if random.random() >= level:
            # print("---> Original text:")
            # print(type(example), example)
            # print()
            yield example
        else:
            print("---> Modified text:")
            # Uppercase followed by lowercase
            text = example.text
            chars = [c.lower() if i % 2 else c.upper() for i, c in enumerate(text)]
            # Create augmented training example
            example_dict = example.to_dict()
            print("Example dict:", example_dict)
            # doc = nlp.make_doc("".join(chars))
            doc = nlp.make_doc("augmented text")
            gold_dict = {}
            gold_dict["cats"] = example_dict["doc_annotation"]["cats"]
            # gold_dict["token_annotation"]["ORTH"] = [t.text for t in doc]

            # Original example followed by augmented example
            # yield example

            print("Doc:", doc)
            print("Gold dict:", gold_dict)
            aug_example = Example.from_dict(doc, gold_dict)
            print(type(aug_example), aug_example)
            print()
            yield aug_example

    return augment

    def lower_casing_augmenter(nlp, example):
        if random.random() >= level:
            yield example
        else:
            example_dict = example.to_dict()
            doc = nlp.make_doc(example.text.lower())
            example_dict["token_annotation"]["ORTH"] = [
                t.lower_ for t in example.reference
            ]
            # Original example followed by augmented example
            yield example
            yield example.from_dict(doc, example_dict)

    return lower_casing_augmenter
