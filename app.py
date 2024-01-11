from flask import Flask, request
from word_lev import main

app = Flask(__name__)

@app.route('/similarity', methods=['POST'])
def find_similarity():
    """
    Flask route that receives a POST request containing two strings and computes their similarity using
    the word_lev module, considering stop words and penalties for synonyms/antonyms.

    Request Body:
    - "string1" (str): The first input string.
    - "string2" (str): The second input string.

    Returns:
    - response (dict): A dictionary containing the following keys:
        - "insertions" (int): Number of insertions in the optimal alignment.
        - "deletions" (int): Number of deletions in the optimal alignment.
        - "substitutions" (int): Number of substitutions in the optimal alignment.
        - "penalty" (float): Extra penalty incurred during the alignment.
        - "similarity_score" (float): Similarity score between the two strings (1 - normalized edit distance).
    """
    # Initialize response dictionary
    response = dict()

    # Parse the request JSON
    requestBody = request.get_json()
    string1 = requestBody["string1"]
    string2 = requestBody["string2"]

    # Read stop words from file
    with open("stopwords.txt", "r") as sw:
        data = sw.read()
        stopwords = data.split("\n")

    # Sample synonym and antonym dictionary
    syn_ant_dict = {"love": [("lust", "passion"), ("hate", "dislike")]}

    # Call the main function from word_lev module
    ids, max_length = main(string1, string2, stopwords, syn_ant_dict)

    # Populate the response dictionary
    response["insertions"] = ids[0]
    response["deletions"] = ids[1]
    response["substitutions"] = ids[2]
    response["penalty"] = ids[3]
    response["similarity_score"] = 1 - sum(ids) / max_length

    return response

if __name__ == "__main__":
    app.run(debug=True)