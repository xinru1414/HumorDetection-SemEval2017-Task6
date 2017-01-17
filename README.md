# PROJECT OVERVIEW
This project corresponds to the SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor" (http://alt.qcri.org/semeval2017/task6/). The goal of this project is to develop a system that learns the sense of humor represented in the comedy show @midnight (http://www.cc.com/shows/-midnight). 

## HashtagWars
In each episode the host comes up with a topic in the form of a hashtag. For example, “#BadInventions” is one of the topics in the hashtag format. In order to respond to the topic, the guests must provide a funny tweet including the hashtag. The home audience is also encouraged to participate this game in a certain amount of time by posting their own tweet using the hashtag and @ing the show “@midnight”. In the next episode, the show chooses top 10 funny tweets from the audience’s posts and selects a single winning tweet which is the funniest from the show’s point of view. The SemEval task collects tweets to conduct the dataset. Note that there are three buckets for the tweets: the winning tweet, top 10 but not winning, and not 10. Data is available here: http://alt.qcri.org/semeval2017/task6/index.php?id=data-and-tools

## Goal 
There are two subtasks -- Subtask A: Pairwise Comparison; Subtask B: Semi-Ranking
For Subtask A, the system should be able to correctly predict which tweet is funnier given two tweets, based on the gold label. For Subtask B, the system should produce a ranking of tweets from funniest to least funny given an input file of tweets for a specific hashtag.

# HOW TO RUN THE SYSTEM
The system is written in Python 2.7

	Step 1: Download the training data from the SemEval website (http://alt.qcri.org/semeval2017/task6/)
	Step 2: Run install.sh for dependencies (kenlm)
	STep 3: Run python avocado.py to generate
