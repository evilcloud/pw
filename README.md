# pw

A very basic password generator:

generates a password on the fly and pushes it to the clipboard.

**Optional:** a lenght of the password (_0 < int < whatever your system or reason may allow_)

**Default lenght:** 40 charachters

Current generator's MO:
* picks random words from [1-1000.txt](https://gist.github.com/dmitryTsatsarin/e6b8b43f2a9a265b98a7) -- a short dictionary of most popular clean words in English language
* capitalizes each word
* strings all words together
* at the end of the string are added:
    * One single digit from 0 to 9
    * One single special charachter

Made it just because couldn't find a decent pass generator with no drama attached.

There is also a profanity mode with `--fuck`. Dictionary is taken directly, with no modifications, from Luis von Ahn's [Offensive/Profane Word List](https://www.cs.cmu.edu/~biglou/resources/bad-words.txt)