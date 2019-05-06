# Mining Conversations from Novels

![python](https://img.shields.io/badge/python%20-3.7.1-brightgreen.svg) ![tensorflow](https://img.shields.io/badge/tensorflow-2.0.0--alpha0-orange.svg)

insert Image

Abstract: xxxxx

## Table of contents
* [Introduction](#general-info)
  - [Quick Summary](#Quick-Summary)
  - [Motivation](#motivation)
  - [Why Is this a challenge?](#why-is-the-a-challenge)
* [Identifying Conversations](#identifying-conversations)
  - [Data](#data)
  - [Preprocessing](#preprocessing)
  - [Methodology](#Methodology)
    1. [Heuristic](#Heuristic)
    2. [Sentence-pair Classification](#Sentence-pair-Classification)
    3. [Sequence Labeling](#Sequence-Labeling)
  - [Results](#results)
  - [Examples](#examples)
  - [Conclusion](#conclusion)
* [Quick Start](#quick-start)
  - [Requirements](#requirements)
  - [Access NER visualizer](#requirements)
  - [NER Starter Code]()
* [Resources](#resources)
  - [Embeddings](#embeddings)
  - [References](#references)
* [Contact](#contact)

---

# Introduction

#### Quick Summary

The objective of this project is to compare methods for mining **conversations** from **narrative fiction**.

#### Motivation

Firstly, non-goal-driven (NGD) chatbots need natural language data. A lot of it, and the richer the better. Exciting advances in NGD chatbots such as Google Duplex and Microsoft Xiaoice have been powered by deep learning models trained on rich and diverse types of conversations. For instance, XiaoIce is trained to be able to switch between 230 conversational modes or 'skills', ranging from comforting and storytelling to recommending movies after being trained on examples of conversations from each category.

Such data sources are hard to come by. Existing methods include mining reddit and twitter for conversational pairs and sequences. These methods face limitations because of the linguistic and content differences between online communication and regular human conversation, not to mention the negativity bias of internet content. Some teams have resorted to collecting human-generated conversational data through crowd-sourcing tools such as Amazon Mechanical Turk. Unfortunately, these methods are expensive, slow, and do not scale well.

There is another way. A treasure trove of varied and life-like conversational data lie unexplored within the  pages of narrative fiction. Conversation in literary fiction is rich and varied in ways that existing corpora are not. Research has found that many of the linguistic and paralinguistic features that drive 

Furthermore, this project is also valuable for digital humanities researchers. Humanities researchers are increasingly seeing the value of obtaining large corpora to test general hypotheses. 

#### Solution Approach

Identifying conversations in narrative fiction is tricky. Where does one conversation end, and another begins? Stylistic and lexical features vary greatly across literary works and time periods. For instance, in some works, speaker attribution is clear, i.e. "The car is red," she said. In others, it is not, i.e. "The car is red". "Indeed it is". More crucially, if you say . 

Simply looking at consecutive utterances enclosed in quotation marks "…", "…" will not work, because some conversations are interspersed with additional narration.

Basically, there isn't a simple set of rules one can use to extract conversations. The task would also involve being able to detect very subtle and complex correlations between the narrative text and sequences of dialogue.



#### 

# Identifying Conversations

#### Data

Our data consist of three novels: *Pride and Prejudice*  and *Emma* by Jane Austen, and *Jane Eyre* by Charlotte Bronte. We use *Pride and Prejudice* as our training set, and *Emma* and *Jane Eyre* as our validation and test sets respectively.

We used *Pride and Prejudice* as our training set because it contains several appealing qualities. Firstly, it is a novel that is particularly rich in dialogue. Not only does it contain many utterance, it is a *comedy of manners*, which in litspeak basically means a novel that makes fun of social norms by playing them out in social interactions. This means that the dialogue inhabited   



#### Preprocessing

#### Methodology

##### Heuristic 

##### Sentence-pair Classification

Shifting to deep learning approach, the team first explored to solve the issue as a multi-class classification problem.
 
 The dataset was prepared in the format of utterance pairs which labeled classes (i.e. "not_pair", "part" and "response"). As the key part of training preparation, the team adopted pre-trained GloVe embedding to form the vector representation of the paired utterances which are then fed into two bidirectional LSTM models end with 3 classes Dense layer with 'softmax' as activation function.

##### Sequence Labeling

As the alternative approach thought of, the team considered treating the issue as sentence level Named Entity Recognition problem and constructed BERT embedding+LSTM architecture. 

Being one of the latest state-of-art algorithm, BERT applies bidirectional transformer training on the language model which gives one of the best pre-trained embedding available across many NLP tasks. To achieve good results, the team selected BERT pre-trained embedding due to the need of understanding the context.

The team also explored LDA, TF-IDF word2vec approach to which BERT embedding outperforms on the NER task.


#### Results


| Model                            | Recall B-START | Precision B-START | comments                           |
| -------------------------------- | -------------- | ----------------- | ---------------------------------- |
| Convo miner heuristic            | 0.5            | 0.909             | Non-ML                             |
| fiction_bert_lstm_train_v1.ipynb | 0.079          | 0.500             | 1 paragraph as input, batchsize=4  |
| fiction_bert_lstm_train_v2.ipynb | 0.55           | 0.478             | 3 paragraph as input, batchsize=4  |
| fiction_bert_lstm_train_v3.ipynb | 0.6            | 0.429             | 4 paragraph as input, batchsize=4  |
| fiction_bert_lstm_train_v4.ipynb | 0.611          | 0.611             | 4 paragraph as input, batchsize=16 |

#### Examples

# Quick Start

#### Requirements

#### Access NER Visualizer

#### NER Starter Code

# Resources

#### Embeddings

#### References

# Contact