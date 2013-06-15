Parrott
=======
By [Francis Tseng](http://supermedes.com)

[Parrott](http://supermedes.com/labs/parrott/) is intended to be a pseudo-intelligent retweeter. It will learn
from your retweeting habits, and optionally the retweeting habits of
others, and try to retweet things on your behalf.

If I can get it to work well enough, and if the Twitter API allows it
(so far it looks like it doesn't), you could in theory collect
tweets/retweets from several tastemaking accounts, and train Parrott to
be a tastemaker.

Parrott runs off a simple bag-of-words Naive Bayes classifier, which is
a slightly modified, [python-ported
version](https://github.com/ftzeng/naivebayes) of [Edwin Chen's Naive Bayes
classifier](http://goo.gl/uLmBf). Though Parrott uses unigrams, the
classifier supports any ngram, so you could modify the program to use
bigrams and so on.

Parrott is licensed under the [MIT
license](https://github.com/ftzeng/parrott/blob/master/LICENSE.txt).

## Setup
To get Parrott up and running, you need to start the Jetty/Solr server:
``` bash
    $ cd solr
    $ java -jar start.jar -Dsolr.solr.home=memory
```
Then access at `http://localhost:8983/solr/#/`.

Why Parrott?
I'm lazy and want a computer to do my social media for me.


## To Do
* Make the damn thing more accurate

## Nice-To-Haves (Advanced Features)
* Follow links, pass through
	[Readability](https://github.com/buriy/python-readability), consider
	that content as part of the document (i.e. tweet)?