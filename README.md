# 1-apocr-apoc-jn
Code and data to create a freely-available, openly-licensed, morphologically annotated edition of the _First Apocryphal
Apocalypse of John_.

For more information on this wonderful text (which uses vocabulary familiar for most readers of the Greek NT),
see the e-Clavis entry: [First Apocryphal Apocalypse of John](https://www.nasscal.com/e-clavis-christian-apocrypha/1-apocryphal-apocalypse-of-john/).

## License
This work (data) is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License
([CC-BY-SA-4.0](http://creativecommons.org/licenses/by-sa/4.0/)).

The code (python scripts) are licensed under the MIT License.

## First Apocryphal Apocalypse of John Greek Morphology

The text of the _First Apocryphal Apocalypse of John_ reflects the text used in Rick Brannan's _The First Apocryphal Apocalypse of John: 
A Greek Reader_ published by Appian Way Press in 2018. Brannan's edition uses the Greek text from Tischendorf. It has been proofread 
against Tischendorf's edition multiple times and should reflect Tischendorf's text well, even with some typo corrections found along the way.

The output currently mimicks the record style of [MorphGNT](https://github.com/MorphGNT). Note that I've also added 
a column for "language" and "source" to the record. 

The code within the repo takes a source internal to Rick, which is not in a state to be released, and prepares this edition for
public release.

## Codes and Fields

### Columns

 * book/chapter/verse
   * unlike MorphGNT, I use `1AAJn.chap.verse` where `chap` is the chapter number and `verse` is the verse number.
   * `1AAJn` has a chapter `0` which should be referred to as the `title`.
 * part of speech
 * parsing code
 * text (including punctuation)
 * word (with punctuation stripped)
 * normalized word (using Tauber's `greek_normalisation` Python library
 * lemma
 * language (`grc`)
 * source (`RWB`). This is source for both lemma and morphology string.

### Part of Speech Code (Greek)

* A- adjective  
* C- conjunction  
* D- adverb  
* I- interjection  
* N- noun
* NP noun, proper (not in Tauber)
* NU number (not in Tauber)
* P- preposition  
* RA definite article  
* RC reciprocal pronoun
* RD demonstrative pronoun  
* RF reflexive pronoun
* RI interrogative/indefinite pronoun  
* RK correlative pronoun
* RP personal pronoun  
* RR relative pronoun  
* RS possessive pronoun
* TL transliterated (not in Tauber)
* V- verb  
* X- particle  

### Parsing Code (Greek)

 * person (1=1st, 2=2nd, 3=3rd)
 * tense (P=present, I=imperfect, F=future, A=aorist, X=perfect, Y=pluperfect)
 * voice (A=active, M=middle, P=passive, U=middle/passive)
 * mood (I=indicative, D=imperative, S=subjunctive, O=optative, N=infinitive, P=participle)
 * case (N=nominative, G=genitive, D=dative, A=accusative, V=vocative)
 * number (S=singular, P=plural)
 * gender (M=masculine, F=feminine, N=neuter)
 * degree (C=comparative, S=superlative)
 
## Disclaimer
*Disclaimer:* This is _totally_ an in-my-spare-time and as-I-feel-inspired kind of project. And I don't have a lot of 
spare time. No promises about status and finishing, use at your own risk, etc.
