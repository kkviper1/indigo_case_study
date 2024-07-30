# Case Study for Indigo Hack2Hire

In today’s world, LLMs and other NLP models are around us everywhere,
from the text predictor of our phone’s keyboard to the
GPT models taking over the internet. As Machine Learning and
NLP has become an important part of our lives, there is no denying
the importance of it.
In this Report, we shall see how 3 Transformer models, namely
BERT, T5 and GPT2 stack up against a question answering problem
provided by the Toughdata Quora dataset.

# Results

| Models | Loss   | BLEU   | ROUGE  | Perplexity |
|--------|--------|--------|--------|------------|
| GPT    | 2.9588 |        |        | 19.276     |
| BERT   | 3.3579 |        |        | 28.729     |
| T5     | 3.7446 | 0.1138 | 0.1287 |            |


## Tech Stack:
- Programming Language: Python
- Dataset: Toughdata Quora Q&A
- Libraries: Torch, Transformers, NLTK, Seaborn, Matplotlib

Front End: Gradio, Huggingface Spaces


## Link to Demo:

[Huggingface Demo](https://huggingface.co/spaces/karanzrk/Unified_Quora_QA)



