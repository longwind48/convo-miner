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

'Begin at the beginning,' the King said gravely, 'and go on till you come to the end: then stop.' 

​													- King of Hearts, Alice in Wonderland (1865)

#### Quick Summary

The objective of this project is to compare methods for mining **conversations** from **narrative fiction**.

#### Motivation

Firstly, dialogue systems need natural language data. A lot of it, and the richer the better. Exciting advances in dialogue systems such as Google Duplex and Microsoft Xiaoice have been powered by deep learning models trained on rich and diverse types of conversations. For instance, XiaoIce is trained to be able to switch between 230 conversational modes or 'skills', ranging from comforting and storytelling to recommending movies after being trained on examples of conversations from each category.

Such data sources are hard to come by. Existing methods include mining reddit and twitter for conversational pairs and sequences. These methods face limitations because of the linguistic and content differences between online communication and regular human conversation, not to mention the negativity bias of internet content, seen in the infamous Microsoft "Tay" bot. Some teams have resorted to collecting human-generated conversational data through crowd-sourcing tools such as Amazon Mechanical Turk. Unfortunately, these methods are expensive, slow, and do not scale well.

There is another way.

A treasure trove of varied and life-like conversational data lies within the pages of narrative fiction. Conversation in narrative fiction is rich and varied in ways that existing corpora are not. Research has found that many of the linguistic and paralinguistic features of dialogue in fiction  are similar to natural spoken language. They also contain different actors with different intentions and relationships to one another, which could potentially allow a data-driven dialogue system to learn to personalize itself to different users by making use of different interaction patterns. Additionally, real-life dialogue is a role-playing 'language game' of sorts between turn-taking strategic agents, and we would like data that can capture this.

Furthermore, this project is also valuable for digital humanities researchers who want to conduct large-scale studies of dialogue in fiction.

#### Solution Approach

Identifying conversations in narrative fiction is tricky. Where does one conversation end, and another begins? Stylistic and lexical features vary greatly across literary works and time periods. For instance, in some works, speaker attribution is clear, i.e. "The car is red," she said. In others, it is not, i.e. "The car is red". "Indeed it is". 

Simply picking out consecutive words enclosed in quotation marks "…", "…" will not work, because some conversations are interspersed with additional narration.

Finally, and most importantly, a lot of the information about conversation in fiction is contained not in dialogue text itself, but in the exposition `{O}`. Narrative exposition may add context to the ongoing conversation. It may also signal a change in conversational or situational context and thus the beginning of a new narrative sequence. Thus, any method that looks purely at the conversational utterances is likely to fall short.

In sum, we suspect that there isn't a simple set of rules one can use to extract conversations. We propose that solving this task would  require a model that can detect very subtle and complex correlations between the narrative text and dialogue. It would also need to readily identify sequences of text. Thus, we decided to approach this problem using a sequence-labelling **Deep Learning** model constructed using a custom-built **BERT**+ **LSTM** architecture implemented in **tensorflow 2.0**. We compare it against a heuristic method.

# Identifying Conversations

#### Data

Our data consists of all the text in *Pride and Prejudice* by Jane Austen. We chose the novel as our data because it contains several appealing qualities. 

Firstly, it is a novel that is particularly rich in the relationship between dialogue and plot. A leading Austen scholar characterises her novels as "Conversational Machines", in which words are traded in a "complex role-playing game" (Morini 2009). 

Secondly, it comes from a period in the history of the English language novel in which authors attempted to recreate dialogue as realistically as possible instead of the more abstract, experimental means used in later periods  (Ibid). 

Thirdly, it is easily and legally accessible as in HTML from the open-source website **Project Gutenberg** as its copyright has expired. This also means that our entire development pipeline will be directly applicable to the other ~58,000 texts hosted on Project Gutenberg.

#### Preprocessing

We input html files containing the complete text of narrative fiction hosted on [Project Gutenberg](<https://www.gutenberg.org/>). 

Then, a Python parser extracts text within ```<p>``` tags and ``<h2>`` tags and outputs a csv file with each paragraph as a row. Utterances and non-utterances are also tagged as such using a collection of simple rules.

Inspired by the sequence-labelling scheme typically used in Named-Entity-Recognition, we use the following schema to assign labels to our text paragraphs:

 For each utterance, we assign

- `B-START` to first utterance in the conversation
- `I-START` if it the utterance following `B-START` is by the same speaker
- `B-OTHER ` if a speaker other than the one making the preceding utterance enters the conversation
- `I-OTHER` if the next utterance following an utterance assigned a `B-OTHER` tag belongs to the very same speaker

Note that we our approach does not track identities of speakers, only changes of speakers.

If, on the other hand, a paragraph is not an utterance and is instead exposition, we assign:

- `O`, which stands for "Outside"

For example, the first few paragraphs of our text will be tagged as such:

```
It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. {O}

However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters. {O}

“My dear Mr. Bennet,” said his lady to him one day, “have you heard that Netherfield Park is let at last?” {B-START}

Mr. Bennet replied that he had not. {O}

“But it is,” returned she; “for Mrs. Long has just been here, and she told me all about it.” {B-OTHER}

“Do you not want to know who has taken it?” cried his wife impatiently. {I-OTHER}
```



#### Methodology

We evaluate our models using two types of metrics. Firstly, we compare the true and predicted labels of `B-START`. We then also construct utterance pairs from the predicted labels using XXX and

##### Heuristic 



##### Sequence Labeling

As the alternative approach thought of, the team considered treating the issue as sentence level Named Entity Recognition problem and constructed BERT embedding+LSTM architecture. The model takes paragraphs as input and analyzes the conversation entities (as listed above) at sentence level.

Being one of the latest state-of-art algorithm, BERT applies bidirectional transformer training on the language model which gives one of the best pre-trained embedding available across many NLP tasks.The team selected BERT pre-trained embedding with average operator to achieve sentence level embedding on the extracted paragraphs.

The team also explored LDA, TF-IDF word2vec approach to which BERT embedding outperforms on the NER task.


#### Results


| Model                            | Recall B-START | Precision (Utterance-Pair) | comments                                     |
| -------------------------------- | -------------- | -------------------------- | -------------------------------------------- |
| Convo miner heuristic            | 0.50           | 0.89                       | Non-ML                                       |
| fiction_bert_lstm_train_v4.ipynb | **0.70**       | **0.93**                   | BERT + LSTM, 4 paragraph input, batchsize=16 |

The table above compares the results of the 3 types of solutions we built. The NER model with the BERT + LSTM architecture is best-performing one in absolute terms across 2 metrics.

The **Recall** of B-Start is the measures the percentage of total relevant results correctly classified by the algorithm. It is calculated by taking the ratio of true labels that are correctly predicted . This means that 50% of all true labels were predicted correctly by the heuristic method. On the other hand, our sequence-labelling model correctly predicts 74% of all true labels.

The **Precision** of the utterance pairs is the proportion of predictions that are relevant. It is calculated by the proportion of true predictions over all predictions (either correct or incorrect). The precision of the sequence-labelling model, at 93%, beats the precision of the heuristic method, which stands at only 89%.

In conclusion, our theoretical motivations were validated by the results. Our NER-inspired sequence-labelling model was able to far better mine conversations from text. We suggest, in line with our theoretical convictions, that it could do so because it can take account the sequential nature of conversations in fiction as well as the highly complex correlations between narration and dialogue in the text.

#### Examples

# Quick Start

#### Requirements

#### Access NER Visualizer

#### NER Starter Code

# Resources

#### Embeddings

#### References

[A large annotated corpus for learning natural language inference,](https://nlp.stanford.edu/pubs/snli_paper.pdf)

[Keras SNLI baseline example](https://github.com/Smerity/keras_snli)

[GloVe: Global Vectors for Word Representation,](https://nlp.stanford.edu/pubs/glove.pdf)

[A Survey of Available Corpora for Building Data-Driven Dialogue Systems](https://arxiv.org/pdf/1512.05742.pdf)

[10 innovative chatbots](https://www.wordstream.com/blog/ws/2017/10/04/chatbots)

[Google Duplex](https://ai.googleblog.com/2018/05/duplex-ai-system-for-natural-conversation.html)

[The Design and Implementation of XiaoIce,an Empathetic Social Chatbot](https://arxiv.org/pdf/1812.08989.pdf)

[The Ubuntu Dialogue Corpus: A Large Dataset for Research in Unstructured Multi-Turn Dialogue Systems](https://arxiv.org/pdf/1506.08909.pdf)

[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://arxiv.org/abs/1801.07243)

[Training Millions of Personalized Dialogue Agents](https://www.topbots.com/most-important-conversational-ai-research/#ai-chat-paper-2018-4)

[I Know The Feeling: Learning To converse with Empathy](https://arxiv.org/pdf/1811.00207.pdf)

[Psychological, Relational, and Emotional Effects of Self-Disclosure After Conversations With a Chatbot](https://academic.oup.com/joc/article-abstract/68/4/712/5025583)

[Creating an Emotion Responsive Dialogue System](https://uwspace.uwaterloo.ca/bitstream/handle/10012/14026/Vadehra_Ankit.pdf?sequence=1&isAllowed=y)

[Learning Personas from Dialogue with Attentive Memory Networks](https://arxiv.org/pdf/1810.08717.pdf) 

# Contact