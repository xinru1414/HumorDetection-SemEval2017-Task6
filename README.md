# **OVERVIEW**
This github contains the Master's Thesis work from Xinru. It is associated with the SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor" (http://alt.qcri.org/semeval2017/task6/). There are two stages involved:

## NgramLM
stage 1, Ngram Language Model, part of the SemEval2017 Task6 competition
## DLLM
stage 2, Deep Learning Language Model

# Warning
site is under construction

# **THE TASK**
## HashtagWars
In each episode the host comes up with a topic in the form of a hashtag. For example, “#BadInventions” is one of the topics in the hashtag format. In order to respond to the topic, the guests must provide a funny tweet including the hashtag. The home audience is also encouraged to participate this game in a certain amount of time by posting their own tweet using the hashtag and @ing the show “@midnight”. In the next episode, the show chooses top 10 funny tweets from the audience’s posts and selects a single winning tweet which is the funniest from the show’s point of view. The SemEval task collects tweets to conduct the dataset. Note that there are three buckets for the tweets: the winning tweet, top 10 but not winning, and not 10. Data is available here: http://alt.qcri.org/semeval2017/task6/index.php?id=data-and-tools

## Goal 
There are two subtasks -- Subtask A: Pairwise Comparison; Subtask B: Semi-Ranking
For Subtask A, the system should be able to correctly predict which tweet is funnier given two tweets, based on the gold label. For Subtask B, the system should produce a ranking of tweets from the funniest to the least funny given an input file of tweets for a specific hashtag.

# **STRUCTURE**
**NgramLM**: This directory contains stage 1 work.

**DLLM**: This directory contains stage 2 work.

**Evaluation**: This directory contains evaluation script released by SemEval and evaluation source code.

**data**:This directory contains all the training data and evaluation data.

# **HOW TO RUN THE DULUTH SYSTEM**
The system is written in Python 2.7 for NgramLM and Python3.5 for DLLM

The **script** folder under each stage contains various scripts to set up and run the system.

# **AUTHORS**
Xinru Yan, University of Minnesota Duluth yanxx418@d.umn.edu

Ted Pedersen, University of Minnesota Duluth tpederse@d.umn.edu

# **COPYRIGHT AND LICENCE**
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

# **RELEASE**
First release on March 15th,  2017
TBC
