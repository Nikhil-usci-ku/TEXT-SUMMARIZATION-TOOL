# TEXT-SUMMARIZATION-TOOL

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: NIKHIL KUMAR

*INTERN ID*: CODF69

*DOMAIN*: AIML

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR


> This repository contains a Python script for advanced text summarization, by strategically combining traditional Natural Language Processing (NLP) techniques with the power of the PEGASUS Transformer model.

> Unlike traditional extractive summarization that merely picks sentences from the original text, this solution generates entirely new, concise, and fluent sentences that capture the core meaning of the input article.

## Description
This project introduces an advanced text summarization system that aims to deliver results by intelligently combining the strengths of traditional Natural Language Processing (NLP) techniques with cutting-edge Transformer models, specifically PEGASUS. The core objective is to move beyond mere extractive summarization (which simply selects and reorders existing sentences) and achieve true abstractive summarization, where the system generates entirely new, concise, and semantically accurate sentences that capture the essence of the input text.

The rationale behind this hybrid approach stems from the understanding that while large pre-trained Transformer models like PEGASUS are incredibly powerful at generating coherent text, providing them with explicit, well-structured cues from traditional NLP methods can potentially guide their attention and focus. This can lead to summaries that are not only fluent and novel but also highly relevant and factually grounded to the most critical aspects of the original content.

The system operates in two primary stages:

1. NLP-Powered Context Extraction: Before the summarization model processes the text, traditional NLP techniques are employed to identify and extract key information. This involves:

* TF-IDF for Keyword Extraction: Term Frequency-Inverse Document Frequency (TF-IDF) is used to pinpoint the most statistically significant keywords in the article. These keywords represent the core topics and important concepts, offering a concise overview of the document's content.
* spaCy for Named Entity Recognition (NER): The robust spaCy library is utilized to identify and categorize named entities (e.g., persons, organizations, locations, dates). These entities are often crucial factual anchors within a text, and explicitly highlighting them can help the summarization model maintain factual accuracy and context.

2. PEGASUS-Driven Abstractive Generation: The extracted keywords and named entities are then strategically prepended to the original article text. This augmented input is fed into the `google/pegasus-cnn_dailymail` model, a highly effective pre-trained Transformer model from Google, specifically fine-tuned for abstractive summarization on news data. PEGASUS's unique pre-training objective, known as "gap sentence generation," makes it exceptionally adept at identifying the most salient parts of a text and generating highly condensed, paraphrased summaries.


By providing PEGASUS with this "enhanced input" (e.g., "Keywords: AI, summit, climate. Entities: G7, Puglia, Meloni. Original Article: ..."), the project aims to:

* Improve Focus: Guide the model's attention towards the most important themes and entities identified by the NLP layer.
* Enhance Relevance: Ensure the generated summary remains tightly coupled to the core information.
* Maintain Factual Accuracy: Increase the likelihood that key factual elements are correctly incorporated into the abstractive output.

The result is a summarization solution that not only generates new sentences but also strives for a higher level of precision and relevance, making it particularly useful for quickly grasping the essential information from lengthy documents. The modular design also allows for easy experimentation with different NLP features or alternative Transformer models, facilitating further optimization for specific use cases.

### This project combines:
* Traditional NLP: For robust feature extraction, specifically identifying keywords (via TF-IDF) and named entities (via spaCy). These serve as explicit "hints" to the abstractive model about the article's most crucial elements.
* PEGASUS Model: A state-of-the-art Transformer model pre-trained specifically for abstractive summarization. It excels at understanding the essence of text and generating novel, coherent summaries. By providing it with NLP-extracted context, we aim to guide its powerful generation process towards the most salient points.

### Features
* Abstractive Summarization: Generates new sentences for the summary, not just extracts.
* PEGASUS Integration: Leverages google/pegasus-cnn_dailymail, a highly effective pre-trained model for summarization.
* NLP Contextualization: Uses TF-IDF for keyword extraction and spaCy for Named Entity Recognition (NER) to enrich the input provided to PEGASUS.
* Configurable Summary Length: Easily adjust max_length and min_length to control summary verbosity.
* Beam Search Decoding: Utilizes beam search for higher quality and more diverse generated summaries.

## Prerequisites
> Python 3.12

## Installation
Clone the repository (or download the Zip File):

`git clone https://github.com/Nikhil-usci-ku/TEXT-SUMMARIZATION-TOOL.git`

`cd TEXT-SUMMARIZATION-TOOL`



Install the necessary Python libraries provided in requirements.txt file:

`pip install -r requirements.txt`


The script will attempt to download NLTK and spaCy models automatically.


## Running
Run the Python script Task1.py directly. Paste The lengthy article to get summary.

## Output
* User Input
![image](https://github.com/user-attachments/assets/aadece15-6827-42ee-828d-2e4338c93d44)
![image](https://github.com/user-attachments/assets/0e6f7a85-65fa-4068-a2b9-cacb6aabb7e0)



* Summerized Output
![image](https://github.com/user-attachments/assets/df0213b5-51a3-4993-8043-e4be70275bb7)













