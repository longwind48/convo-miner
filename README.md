# Automated Fictional Dialogue Corpus Extractor
Team: Traci. Ray, Rocco, LiJie, LingXiao, Joyce

---

**More specifically:**

Harvest rich human-to-human written dialogues in Project Gutenberg, to generate data for data-driven dialogue systems, aka chatbots. 

**Motivation** (need to amend):

- Spoken language in movies resembles spontaneous human spoken language (Forchini, 2009)
- Many of the linguistic and paralinguistic features contained within the dialogues are similar to natural spoken language, including dialogue acts such as turn-taking and reciprocity (e.g. returning a greeting when greeted)
- We hope that conversational corpora extracted from fiction can further stimulate research on improving chit-chat dialogue systems, and in the end crafting a more natural conversational experience for the user. (need to rephrase)

**Challenge**:

<write something>

**Definitions:**

- Utterance: 

  - text prefixed by an opening quote and postfixed by a closing quote, must be spoken by 1 speaker. 
  - E.g. ```“You used us abominably ill,” answered Mrs. Hurst, “running away without telling us that you were coming out.”``` ---> contains 1 utterance. 
- Response:
  - An utterance that is a reponse to a previous utterance.
- Speaker:

  - Person or character that voiced the utterance. 
- Narrative:

  - Text that is considered non-utterance. (receives a ‘N’ tag)
- Conversation/Dialogue:

  - A sequence of turns uninterrupted by narratives. I.e. a set of utterances

**End product of Dialogue Corpus Extractor:**

1. HTMLFiction-to-Utterance Parser

2. Model that detects conversations among utterances and extracts (utterance, reponse) pairs

  - Input: A fiction

  - Output: table containing utterance-response pairs, in the form <utterance_1, utterance_2>, where utterance_1 and utterance_2 belong in the same conversation.

**Data Preparation**

- For each utterance, Labels are now '```part```', '```response```', '```not```'.

  - '```part```': utterance is part of last utterance, or in other words, same speaker in the same conversation
  - '```response```': utterance is a response of last utterance, and they both belong in the same conversation
  - '```not```': utterance is not related to last utterance, and they both belong in different conversations

- For every paragraph, we tokenized them into one utterance, and substituted the narrative with a ```[N]```.

  - e.g. ```<p> “You used us abominably ill,” answered Mrs. Hurst, “running away without telling us that you were coming out.” </p>``` 
  -  Tokenized: ```You used us abominably ill, [N] running away without telling us that you were coming out.```

- Assumptions:

  - All utterances within a paragraph are attributed to a single speaker.  (This one-speaker-per-paragraph property is rarely violated in novels.)  (cite Hua He et. al 2013)
  - For every utterance, we form (utterance-response) pairs if it satisfies 2 conditions:
    - The speaker of the previous utterance is a different person.
    - the previous utterance is in the same conversation.

- Train-test-validation Split:

  - Training set: All utterances in chapters 1-18, 34-61
  - Validation set: All utterances in chapters 23-33
  - Training set: All utterances in chapters 19-26

  

---

## Google Docs

Tensorflow Hackathon: [Link](https://tensorflow.devpost.com/)

Project Plan in Google Docs: [Link](https://docs.google.com/document/d/153GR4_yngHeu6puHnFf-QMzcHXKFKgx94QIK6zLsQCI/edit?usp=sharing)

Pride and Prejudice html book: [Link](https://www.gutenberg.org/files/1342/1342-h/1342-h.htm)

## Progress

| Date       | Status      | Task                                                  | Comments                                                     |
| ---------- | ----------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| 26/04/2019 | Done        | Finished labeling Pride and Prejudice dataset         | ```./data/parsed-n-labeled-data/pnp-gutenberg-label-task -pride-and-prejudice-by-jane-austen.csv``` |
| 29/04/2019 | In-Progress | HTMLfiction parser script                             | - Need to write custom sentence tokenizer script,<br /> - Merged tokenized sentences with labels (HARD!!) |
| 30/04/2019 | Cancelled   | Sentence BIO-style NER                                | - Data is has to be preprocessed too many assumptions. <br /> - Preprocessed text may lose relevant information. |
| 30/04/2019 | Done        | Prepare data ready for modeling                       | - Used same preprocessing methods with [Identification of Speakers in Novels paper](https://www.aclweb.org/anthology/P13-1129). <br /> - Add new labels: '```part```', '```response```', '```not```'. <br /> - Add train test split. <br /> - Data ready for modelling in ```./data/parsed-n-labeled-data/labeled-utterance-final-300419.csv``` |
| 30/04/2019 | In-Progress | Train Sequence Labelling Models                       | Use Tensorflow 2.0 and train baseline                        |
| 01/05/2019 | Done        | Prepare data in IOB format                            | ```./data/parsed-n-labeled-data/iob-labeled-tokens-final-010519.csv``` |
| 02/05/2019 | Done        | Prepare data in utterance pair format                 | ```./data/parsed-n-labeled-data/labeled-utterance-pair-final-020519.csv``` |
| ??/05/2019 | Planned     | Script to construct (utterance, response) pairs       |                                                              |
| ??/05/2019 | Planned     | Document, refactor and test HTMLfiction parser script |                                                              |
| ??/05/2019 | Planned     | Setup a quick frontend to show how the tagging works  | Something like https://guillaumegenthial.github.io/serving.html |
| ??/05/2019 | Planned     | Manually Label more data                              | 1. One fiction from Jane Austin<br />2. One fiction from same genre, different author<br />3. One fiction from different genre, different author |
| ??/05/2019 | Planned     | Detailed writeup on project summary and results       |                                                              |
| 07/05/2019 | Planned     | Organize repo and submit                              |                                                              |

---

## Citations

