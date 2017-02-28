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


#**HOW TO RUN THE DULUTH SYSTEM**
The system is written in Python 2.7

You can download the training data and Evaluation script from the SemEval website (http://alt.qcri.org/semeval2017/task6/)

Step 1: Run `pip install https://github.com/kpu/kenlm/archive/master.zip` to install kenlm

Step 2: Run `python avocado.py` to generate training corpus (plain txt file which contains tweets) for the language model

Step 3: Under kenlm directory Run `/build/bin/lmplz -o 3 -S 70% </path/to/the/plain/text/file/plain.txt >text.arpa` to train the language model (specific usage refers to KenLM: https://kheafield.com/code/kenlm/)

Step 4: Run `python beets.py` to generate scores for each tweet based on the languge model

Step 5: Run `python cilantro_a.py` / `python cilantro_b.py` to generate Task A / Task B result

Step 6: Run `python TaskA_Eval/TaskA_Eval_Script.py predict_test/ gold_test/` / `py TaskB_Eval/TaskB_Eval_Script.py predict_test/ gold_test/` to evaluate Task A / Task B result

# METHOD
The system uses language models (bigram and trigram) to train the corpus. Sepeficially, the system uses KenLM Language Model Toolkit.

# REFERENCE
SemEval:  http://alt.qcri.org/semeval2017/task6/

KenLM Language Model Toolkit:  https://github.com/kpu/kenlm
                               http://kheafield.com/code/kenlm/

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


    



        

        



