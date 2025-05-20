# TEXT-SUMMARIZATION-TOOL




This repository contains a Python script for advanced text summarization, by strategically combining traditional Natural Language Processing (NLP) techniques with the power of the PEGASUS Transformer model.

Unlike traditional extractive summarization that merely picks sentences from the original text, this solution generates entirely new, concise, and fluent sentences that capture the core meaning of the input article.

Why This Approach?
Modern abstractive summarization, powered by large language models (LLMs), has revolutionized how we condense information. While models like PEGASUS are incredibly powerful on their own, integrating targeted traditional NLP steps can sometimes provide them with explicit signals, potentially leading to even more focused and relevant summaries.

This project combines:

Traditional NLP: For robust feature extraction, specifically identifying keywords (via TF-IDF) and named entities (via spaCy). These serve as explicit "hints" to the abstractive model about the article's most crucial elements.
PEGASUS Model: A state-of-the-art Transformer model pre-trained specifically for abstractive summarization. It excels at understanding the essence of text and generating novel, coherent summaries. By providing it with NLP-extracted context, we aim to guide its powerful generation process towards the most salient points.
Features
Abstractive Summarization: Generates new sentences for the summary, not just extracts.
PEGASUS Integration: Leverages google/pegasus-cnn_dailymail, a highly effective pre-trained model for summarization.
NLP Contextualization: Uses TF-IDF for keyword extraction and spaCy for Named Entity Recognition (NER) to enrich the input provided to PEGASUS.
Configurable Summary Length: Easily adjust max_length and min_length to control summary verbosity.
Beam Search Decoding: Utilizes beam search for higher quality and more diverse generated summaries.
Getting Started
Follow these steps to set up and run the summarization script.

Prerequisites
> Python 3.12

Installation
Clone the repository (or download the Zip File):
`git clone https://github.com/your-username/advanced-abstractive-summarization.git`
`cd advanced-abstractive-summarization`

Install the necessary Python libraries provided in requirements.txt file:

`pip install -r requirements.txt`

The script will attempt to download NLTK and spaCy models automatically.

##Running
Run the Python script directly.
