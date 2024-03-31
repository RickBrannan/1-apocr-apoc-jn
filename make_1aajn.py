'''
make_1aajn.py
Rick Brannan
2024-03-31 (Easter Sunday)
Create Tauber-style morphological annotation of the First Apocryphal Apocalypse of John.
This code uses Rick's unreleased personal morph data as the source of the Tauber-style analysis.
'''

import os
from lxml import etree
import unicodedata
import regex as re
from dataclasses import dataclass
from greek_normalisation.normalise import Normaliser
from unicodedata import normalize
from morph_maps import *


@dataclass
class MorphUnit:
    bcv: str
    pos: str
    parse_code: str
    text: str
    word: str
    normalized: str
    lemma: str
    lang: str
    source: str


local_source = "C:/temp/old-git/SecondApocalypseOfJohn/data/xml/wndb/1AAJn/"
git_dir = "C:/git/RickBrannan/1-apocr-apoc-jn/"
data_dir = f"{git_dir}data/"

book_names = {"156": "1AAJn"}
normalise = Normaliser().normalise

index_xml = etree.parse(f"{local_source}00Index.xml")
index_root = index_xml.getroot()
morph_units = []
for book_unit in index_root.xpath("*//unit[@name = 'Book']"):
    book_name = book_names[book_unit.get("ref").split('.')[1]]
    print(f"Book: {book_name}")
    for chapter_unit in book_unit.xpath("./unit[@name = 'Chapter']"):
        chapter_name = chapter_unit.get("ref")
        # print(f"Chapter: {chapter_name}")
        chapter_number = chapter_name.split('.')[2]
        if chapter_number == "title":
            chapter_number = "0"
        chapter_xml = etree.parse(f"{local_source}{chapter_name}.xml")
        chapter_root = chapter_xml.getroot()
        for verse_unit in chapter_root.xpath("*//raster-unit"):
            verse_number = verse_unit.get("ref").split('.')[3]
            print(f"Current: {book_name}.{chapter_number}.{verse_number}")
            for word in verse_unit.xpath("./word"):
                wn_element = word.xpath("./field[@name = 'WordNumber']")[0]
                surface_element = word.xpath("./field[@name = 'Surface']")[0]
                surface_text = surface_element.text
                normalized = normalise(surface_text)[0]
                lemma_element = word.xpath("./field[@name = 'Lemma']")[0]
                lemma_text = lemma_element.text.split('.')[2]
                morph_element = word.xpath("./field[@name = 'Morph']")[0]
                morph_text = morph_element.text
                if len(word.xpath("./field[@name = 'Prefix']")) > 0:
                    prefix_element = word.xpath("./field[@name = 'Prefix']")[0]
                    surface_text = prefix_element.text + surface_text
                if len(word.xpath("./field[@name = 'Suffix']")) > 0:
                    suffix_element = word.xpath("./field[@name = 'Suffix']")[0]
                    surface_text += suffix_element.text

                pos = get_pos(morph_text)
                parse_code = map_logos_morph(morph_text)
                # print(f"Word: {wn_element.text}, {surface_text}, {normalized}, {lemma_text}, {pos}, {parse_code}")

                bcv = f"{book_name}.{chapter_number}.{verse_number}"
                morph_unit = MorphUnit(bcv, pos, parse_code, surface_text.strip(), surface_element.text, normalized,
                                       lemma_text, "grc", "RWB")
                morph_units.append(morph_unit)

# write out the morph units for this book
with open(git_dir + "data/morph/1aajn.txt", "w", encoding="utf8") as f:
    for morph in morph_units:
        f.write(f"{morph.bcv} {morph.pos} {morph.parse_code} {morph.text} {morph.word} {morph.normalized} "
                f"{morph.lemma} {morph.lang} {morph.source}\n")





