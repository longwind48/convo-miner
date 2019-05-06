short_desc: "Mining conversational data from fiction"

### Story

#### Summary

The objective of this project is to train a model that can identify and extract conversations from narrative fiction.

#### Problem Statement

Identifying conversations in narrative fiction is tricky. Where does one conversation end, and another begins? Stylistic and lexical features vary greatly across literary works and time periods. For instance, in some works, speaker attribution is clear, i.e. "The car is red," she said. In others, it is not, i.e. "The car is red". "Indeed it is". More crucially, 

Simply looking at consecutive utterances enclosed in quotation marks "…", "…" will not work, because some conversations are interspersed with additional narration

#### Approach

Our data consist of three novels: *Pride and Prejudice*  and *Emma* by Jane Austen, and *Jane Eyre* by Charlotte Bronte. We use *Pride and Prejudice* as our training set, and *Emma* and *Jane Eyre* as our validation and test sets respectively.

#### Use-Cases

Our model aims to be a scalable method for generating data used to train chatbots. Lack of data is a typical bottleneck in any chatbot development project in general, and for non-goal-seeking chatbots in particular (paper). 

On the one hand, corpora-based methods of training are the predominant means of training chatbots. On the other, natural human conversation contain a richer set of linguistic features than can be typically found in existing corpora. Fiction, conveniently, is a form of textual that can be easily added to digital corpora and which also contains rich conversational information.

The project also has important uses for Digital Humanities researchers who want to conduct large-scale studies of dialogue in fiction.

#### 

