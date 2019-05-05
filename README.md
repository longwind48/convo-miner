# Mining Conversations from Novels

[python](https://img.shields.io/badge/python%20-3.7.1-brightgreen.svg)

[tensorflow](https://img.shields.io/badge/tensorflow-2.0.0--alpha0-orange.svg)

insert Image

Text

## Table of contents
* [Introduction](#general-info)
  - [TL;DR](#tl;dr)
  - [Motivation](####motivation)
  - [Why Is this a challenge?](#why-is-the-a-challenge)
  - [What's the point of mining conversations?]()
* [Identifying Conversations](#identifying-conversations)
  - [Data](#data)
  - [Preprocessing](#preprocessing)
  - [Methodology](#Methodology)
    1. [Heuristic](#heuristic)
    2. [Sentence-pair Classification](#sentence-pair-classification)
    3. [Sequence Labeling](#sequence-labeling)
  - [Results](#results)
  - [Examples](##examples)
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

#### TL;DR

#### Motivation

#### Why is this a challenge?

# Identifying Conversations

#### Data

#### Preprocessing

#### Methodology

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