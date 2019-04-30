# Automated Fictional Dialogue Corpus Extractor
Team: Traci. Ray, Rocco, LiJie, LingXiao, Joyce

---

**More specifically:**

Harvest rich human-to-human written dialogues in Project Gutenberg, to generate data for data-driven dialogue systems, aka chatbots. 

**Motivation**:

- Spoken language in movies resembles spontaneous human spoken language (Forchini, 2009)
- Many of the linguistic and paralinguistic features contained within the dialogues are similar to natural spoken language, including dialogue acts such as turn-taking and reciprocity (e.g. returning a greeting when greeted)
- We hope that conversational corpora extracted from fiction can further stimulate research on improving chit-chat dialogue systems, and in the end crafting a more natural conversational experience for the user. (need to rephrase)

**Challenge**:

<write something>

**Definitions:**

- Utterance: 

  - text prefixed by an opening quote and postfixed by a closing quote, must be spoken by 1 speaker. 
  - E.g. “You used us abominably ill,” answered Mrs. Hurst, “running away without telling us that you were coming out.” ---> contains 1 utterance. 

- Speaker:

  - Person or character that voiced the utterance. 

- Narrative:

  - Text that is considered non-utterance. (receives a ‘N’ tag)

- Conversation/Dialogue:

  - A sequence of turns uninterrupted by narratives. I.e. a set of utterances

**End product of Dialogue Corpus Extractor:**

1. HTMLFiction-to-Utterance Parser

2. Model that detects conversations among utterances and extracts (utterance, reponse) pairs

3. - Input: A fiction

   - Output: table containing utterance-response pairs, in the form <utterance_1, utterance_2>, where utterance_1 and utterance_2 belong in the same conversation.

     

---

## Google Docs

Tensorflow Hackathon: [Link](https://tensorflow.devpost.com/)

Project Plan in Google Docs: [Link](https://docs.google.com/document/d/153GR4_yngHeu6puHnFf-QMzcHXKFKgx94QIK6zLsQCI/edit?usp=sharing)

Pride and Prejudice html book: [Link](https://www.gutenberg.org/files/1342/1342-h/1342-h.htm)

## Progress

| Date       | Status      | Task                                          | Comments                                                     |
| ---------- | ----------- | --------------------------------------------- | ------------------------------------------------------------ |
| 26/04/2019 | Done        | Finished labeling Pride and Prejudice Dataset | ```./data/parsed-n-labeled-data/pnp-gutenberg-label-task -pride-and-prejudice-by-jane-austen.csv``` |
| 29/04/2019 | In-Progress | HTMLfiction parser script                     | 1. Need to write custom sentence tokenizer script, 2. Merged tokenized sentences with labels (HARD!!) |
| 30/04/2019 | Cancelled   | Sentence-level NER                            | Data is has to be preprocessed too many assumptions. Preprocessed text may lose relevant information. |
| 30/04/2019 | Done        | Prepare data ready for modeling               | Used same preprocessing methods with [Identification of Speakers in Novels paper](https://www.aclweb.org/anthology/P13-1129). Add new labels: '```part```', '```response```', '```not```'. Add train test split. Latest working data ready for modelling in ```./data/parsed-n-labeled-data/labeled-utterance-final-300419.csv``` |
| 30/04/2019 | Planned     | Train Sequence Labelling Model                | Use Tensorflow 2.0 and train baseline                        |



---

## Citations

