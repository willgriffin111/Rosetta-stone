
# Rosetta Stone Decoder

The Rosetta stone is an ancient decree written into stone that was used by archeologists to translate between Greek and Ancient Egyptian languages.

## Objective

Write a program to decode messages using a Rosetta for translation. The "Rosetta" will be a series of character sets paired with English words or characters. If you translate the encrypted message correctly, you will find the hidden message.

**HINT:** Spaces that are not part of a fragment must be preserved.

## Input

Multiple lines of input will be given. The first line of input will be the message to translate to English.

All other lines of input will be the Rosetta needed to translate. The fragments of each pair will be separated by a pipe character, one pair per line of input.

For example:

```
Hola Mundo
Mundo|World
Lunes|Monday
Hola|Hello
```

Translates: Hola Mundo

into: Hello World

## Output

The translated text, which will be a real English phrase.

### Test 1 Test Input

```
Hola Mundo
Mundo|World
Lunes|Monday
Hola|Hello
```

**Expected Output:** Hello World

### Test 2 Test Input

```
mieux vaut prévenir que guérir
merci|thank you
que|than
malade|sick
mieux|better
guérir|to heal
chien|dog
vaut prévenir|to prevent
beurre|butter
s'il vous plaît|please
```

**Expected Output:** better to prevent than to heal

### Test 3 Test Input

```
5748494348 574159 544845 57494E44 424C4F5753
41|A
42|B
43|C
44|D
45|E
46|F
47|G
48|H
49|I
4A|J
4B|K
4C|L
4D|M
4E|N
4F|O
50|P
51|Q
52|R
53|S
54|T
55|U
56|V
57|W
58|X
59|Y
5A|Z
```

**Expected Output:** WHICH WAY THE WIND BLOWS
