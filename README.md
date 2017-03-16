#**OVERVIEW**
This project describes the **Duluth** system that participated in the SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor" (http://alt.qcri.org/semeval2017/task6/). The goal of the task is to develop a system that learns the sense of humor represented in the comedy show @midnight (http://www.cc.com/shows/-midnight). The Duluth system completed Subtask A and Subtask B using N-gram language models, ranking well during evaluation.

## HashtagWars
In each episode the host comes up with a topic in the form of a hashtag. For example, “#BadInventions” is one of the topics in the hashtag format. In order to respond to the topic, the guests must provide a funny tweet including the hashtag. The home audience is also encouraged to participate this game in a certain amount of time by posting their own tweet using the hashtag and @ing the show “@midnight”. In the next episode, the show chooses top 10 funny tweets from the audience’s posts and selects a single winning tweet which is the funniest from the show’s point of view. The SemEval task collects tweets to conduct the dataset. Note that there are three buckets for the tweets: the winning tweet, top 10 but not winning, and not 10. Data is available here: http://alt.qcri.org/semeval2017/task6/index.php?id=data-and-tools

## Goal 
There are two subtasks -- Subtask A: Pairwise Comparison; Subtask B: Semi-Ranking
For Subtask A, the system should be able to correctly predict which tweet is funnier given two tweets, based on the gold label. For Subtask B, the system should produce a ranking of tweets from the funniest to the least funny given an input file of tweets for a specific hashtag.

#**STRUCTURE**
**code**: This directory contains all the third party code including KenLM and the Evaluation script for both subtasks provided by SemEval.

**data**: This directory contains all the tweets training data and evaluation data provided by SemEval task.

**mydata**:This directory contains the result of running the system.

**src**: This directory contains source code for the system.

**script**: This directory contains the install script and various run scripts of the system.

**Xinru_Poster**: A poster that briefly examplains the system and how it worked during SemEval evaluation.


#**HOW TO RUN THE DULUTH SYSTEM**
The system is written in Python 2.7

The **script** folder contains various scripts to set up and run the system.


#**METHOD**
The system uses language models (bigram and trigram) to train the corpus. Sepeficially, the system uses KenLM Language Model Toolkit.

Training Language models (LMs) is a straightforward way to collect set of rules by utilizing the fact that words do not appear in an arbitrary order, which means we can gain useful information from a word and its neighbors. A statistical language model is a model that computes the probability of a sequence of words or an upcoming word. Below are two examples of language modeling:

To compute the probability of a sequence of words $W$ given the sequence w1, w2, w3, we have:

P(W) = P(w1) * P(w2) * P(w3)


To compute the probability of an upcoming word W3 given the sequence W1,W2, we have:

P(w3|w1,w2)


The idea of word prediction with probabilistic models is called the N-gram model, which predicts the upcoming word from the previous N-1 words. An N-gram is a contiguous sequence of N words: a unigram is a single word, a bigram is a two-word sequence of words and a trigram is a three-word sequence of words. For example, in tweet "tears in Ramen #SingleLifeIn3Words", "tears", "in", "Ramen" and "#SingleLifeIn3Words" are unigrams; "tears in", "in Ramen" and "Ramen SingleLifeIn3Words" are bigrams and "tears in Ramen" and "in Ramen #SingleLifeIn3Words" are trigrams.

When we use for example, a trigram LM, to predict the conditional probability of the next word, we are thus making the assumption that the probability of a word depends only on a small number of previous words is called the Markov assumption.


# REFERENCE
SemEval:  http://alt.qcri.org/semeval2017/task6/

KenLM Language Model Toolkit:  https://github.com/kpu/kenlm
                               http://kheafield.com/code/kenlm/
                            
News training data: http://www.statmt.org/wmt11/translation-task.html


#**AUTHORS**
Xinru Yan, University of Minnesota Duluth yanxx418@d.umn.edu

Ted Pedersen, University of Minnesota Duluth tpederse@d.umn.edu

#**COPYRIGHT AND LICENCE**
Copyright (C) 2017, Xinru Yan, Ted Pedersen

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.

#**RELEASE**
First release on March 15th,  2017


    



        

        



