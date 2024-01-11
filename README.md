<div align="center">

# A Journey from Edit distance to Text similarity

Siddhanth U Hegde
</div>

## Info

This Repository contains the code to find text similarity between two sentences

This repository is divided into three parts:

  ***Part 1*** : Story of token based edit distance

  ***Part 2*** : Extensions

  ***Part 3*** : Instructions on how to run and docker

---

## **Part 1: Story of token based edit distance**

According to Wikipedia, edit distance or the Levenshtein distance is "A string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other." We can directly relate this concept to text similarity. Given two sentences, if we get to know how operations on characters are needed to convert one sentence into other, we can say how much they are related. For instance, if one sentence requires 100 modifications to convert another and it requires just 5 operations to convert it into third sentence, we can say the the sentence is much more similar to the third sentence. 
But here are few drawbacks: 
- Consider two sentences of almost equal characters and very synonymous but use different words. Like "Today, it's gonna rain" and "It's raining cats and dogs right now", are similar, but it will require a lot of character modifications to convert one from another. 
- If a sentence had a lot of stopwords that will add extra operations if we decide not to remove them. 
- If we had large texts, to perform character level edit distance will consume a lot of memory.

To overcome all these drawbacks, word based or token based edit distance can be used. Instead of inserting/deleting/substituting characters we can apply the same for words. Finally, the similarity metric would be 
$$
Text Similarity = 1 - \frac{editDistance}{maxLength}
$$

## **Part 2: Extensions**

The best part of using this technique in order to find similarity is we can extend this idea specific for our use cases to obtain better results. The main idea of extensions is adding different costs for different type of entities when it comes to insertions, deletions and substitutions. 
- Consider one of the extensions added in this repo about handling stopwords. Consider a specific application where we don't need full attention to stopwords, but we cannot remove them too. If an operation is required to insert/delete/substitute a stopword, we add a negative penalty so that edit distance decreases by a certain amount. 
- Another extension added in this repo is handling synonym and antonym differently. If we have two sentences, "I love cake" and "I hate cake", the edit distance will be 1, but we need a bigger penalty in this scenario. While substituting words, if we find that the word is an antonym, we add extra penalty so that edit distance increases and if the word is the synonym, we add negative penalty.
We can observe that this algorithm can be tuned so that it matches our use case. For instance, if punctuations are a deal-breaker, we might consider punctuations as a seperate token and increase cost for them. 

## **Part 3: Instructions on how to run and docker**

- To just run the python file, run this command:
    > python word_lev.py

    This file has sample1 and sample2 sentence hard coded and it will print the number of insertions, deletions and substitutions required to convert sample1 to sample2 and also prints the penalties and similarity

- To run using a web server and POST request:
    - First run:
        > python app.py
    - Server starts running at: http://127.0.0.1:5000/
    - Set the header key as "Content-Type" and value as "application/json"
    - Create a JSON dictionary with keys "string1" and "string2" for the sentences to be compared
    - Send a POST request to http://127.0.0.1:5000/similarity without any authorization and input type as JSON

- To run using docker:
    - Build docker image by downloading from the Docker Hub using this tag **stunningsid/text-similarity:text-similarity**
    - Run the docker file and send the POST request using same instructions above for the web server