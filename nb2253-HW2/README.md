Nesma Belkhodja
HW 2:

Create 2 Programs using regular expressions to identify the following in a corpus

Program 1 should identify dollar amounts

Cover as many cases as possible

including those with words like million or billion

include numbers and decimals

include dollar signs, the words “dollar”, “dollars”, “cent” and “cents.

include US dollars and optionally other types of dollars

do not include currencies that are not stated in terms of dollars and cents (e.g., ignore yen, franc, etc.)

The program should return each match of your regular expression into an output file, one match per line.

For example, if the program matched exactly 3 cases, than it would be a short file consisting of 3 lines like:

$500 million

$6.57

1 dollar and 7 cents

Program 2 should identify telephone numbers

Attempt to handle as many cases as possible: with and without area codes, different punctuation, etc.

Design and test the programs using all-OANC.txt, the training corpus you downloaded and any other corpora if you choose (but not the test corpus). 

Then run the program for one last time on the test corpus you downloaded: test_dollar_phone_corpus.txt

These are the results you should submit for grading (see below)

You should not use this corpus to develop your system -- you should only run on the test corpus when you are done writing the program