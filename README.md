# JLPT Nx 単語帳

List of words for making japanese flashcards

The data is licensed as CC-BY by Jonathan Waller.

You can find the words and a lot of other cool stuff at his website:

http://www.tanos.co.uk/jlpt/

## Setup

To set up, install the requirements (you might want to set up a venv first)

```cmd
$ python -m pip install -r requirements.txt
```

Ensure that you have a proper installation of TeXlive installed, including XeLaTeX, and the [Noto Sans CJK fonts][google-noto]

Then generate all the cards by running

```cmd
$ make all
```

The resulting pdfs can be found in the `pdf` directory.

## Printing

These booklets are meant to be printed as greyscale double sided A4 papers. As standalone pdfs, they tend to be somewhat useless (for the time being at least)

## Intended use case

First of all, get some kind of flashcard solution.
This might be a mobile app, it might be a bunch of paper slices.
Personally, I would recommend getting a [pack of premade paper cards (image)][tangocho-link]

[![Memorization cards][tangocho-img]][tangocho-link]

Secondly, get one of these bad bois:

![Highlighter/text marker][highlighter-img]

Although not strictly required, keeping track of which of the words you've put into your memorization cards will help you avoid duplicates.

[google-noto]: https://github.com/googlefonts/noto-cjk
[tangocho-link]: https://www.amazon.com/Copies-Books-Each-Yellow-Assortment/dp/B0012OV700/133-2864506-7558164
[tangocho-img]: https://m.media-amazon.com/images/I/71CrpXAXmML._AC_SL1000_.jpg
[highlighter-img]: https://static2.jetpens.com/images/a/000/178/178843.jpg?auto=format&ba=middle%2Ccenter&balph=3&blend64=aHR0cDovL3d3dy5qZXRwZW5zLmNvbS9pbWFnZXMvYXNzZXRzL3dhdGVybWFyazIucG5n&bm=difference&bs=inherit&chromasub=444&fm=jpg&h=400&mark64=aHR0cDovL3d3dy5qZXRwZW5zLmNvbS9pbWFnZXMvYXNzZXRzL3dhdGVybWFyazEucG5n&markalign=top%2Cright&markalpha=30&markscale=16&q=90&usm=20&w=600&s=78167e64fe93cce86b3e07da0f53578c