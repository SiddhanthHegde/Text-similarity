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

According to Wikipedia, edit distance or the Levenshtein distance is "A string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other." We can directly relate this concept to text similarity. Given two sentences, if we understand how many operations on characters are needed to convert one sentence into another, we can determine their level of relatedness. For instance, if one sentence requires 100 modifications to convert it to another, and it requires just 5 operations to convert it into a third sentence, we can say that the sentence is much more similar to the third sentence.
But here are few drawbacks: 
- Consider two sentences with almost equal numbers of characters and very synonymous meanings but expressed using different words, such as "Today, it's gonna rain a lot" and "It's raining cats and dogs right now." These sentences are similar, but converting one into the other would require a substantial number of character modifications.
- If a sentence contains numerous stopwords, the distance would be high.
- When dealing with large texts, performing character-level edit distance calculations would consume a significant amount of memory.

To overcome all these drawbacks, word based or token based edit distance can be used. Instead of inserting/deleting/substituting characters we can apply the same for words. Finally, the similarity metric would be 

#### Text Similarity = 1 - (editDistance / maxLength)

## **Part 2: Extensions**

The best part of using this technique to find similarity is that we can extend this idea, tailoring it to our specific use cases to achieve improved results. The core concept of these extensions involves assigning distinct costs for various types of entities in terms of insertions, deletions, and substitutions. 
- Consider one of the extensions added in this repository, specifically addressing the handling of stopwords. Imagine a specific application where full attention to stopwords is not necessary, yet we cannot remove them entirely. In cases where an operation is needed to insert, delete, or substitute a stopword, a negative penalty is introduced, resulting in a decrease in edit distance by a certain amount.
- Another extension incorporated in this repository involves treating synonyms and antonyms differently. For instance, when comparing two sentences like "I love cake" and "I hate cake," the conventional edit distance might yield 1, but in this scenario, a larger penalty is warranted. When substituting words, if it is identified as an antonym, an additional penalty is applied to increase the edit distance. Conversely, if the word is recognized as a synonym, a negative penalty is introduced to decrease the edit distance.

We can observe that this algorithm is flexible and can be tuned to align with our specific use case. For example, if punctuations play a crucial role and are considered significant, we may treat punctuations as separate tokens and elevate the cost associated with them to better reflect their impact in the similarity measurement.

## **Part 3: Instructions on how to run and docker**

- To just run the python file, run this command:
    > python word_lev.py

    This file has sample1 and sample2 sentence hard coded and it will print the number of insertions, deletions and substitutions required to convert sample1 to sample2 and also prints the penalties and similarity

- To run this as a web service, a POST API has been exposed to which we can provide the sentences and obtain the similarity between them:
    - First run:
        > python app.py
    - Server starts running at: http://127.0.0.1:5000/
    - Set the header key as "Content-Type" and value as "application/json"
    - Create a JSON body with keys "string1" and "string2" for the sentences to be compared
    - Send a POST request to http://127.0.0.1:5000/similarity without any authorization and input type as JSON

- To run using docker:
    - Pull docker image from the Docker Hub using the following commmand:
        > docker pull stunningsid/text-similarity:text-similarity
    - Run the docker file using the following command:
        > docker run -p 5000:5000 stunningsid/text-similarity:text-similarity
    - The application will now start running on http://127.0.0.1:5000/
    - Follow the same set of instructions to use the exposed POST API