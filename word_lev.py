from backtrace import backtrace

def minDistance(string1, string2):
    """
    Calculates the minimum edit distance (Levenshtein distance) between two input strings.

    Parameters:
    - string1 (str): The first input string.
    - string2 (str): The second input string.

    Returns:
    - dp (list): A 2D list representing the dynamic programming table used to compute the minimum edit distance.
    - max_len (int): The maximum length between the two input strings (max(len(string1), len(string2))).
    """

    # Tokenize the input strings into lists of words
    string1 = string1.split()
    string2 = string2.split()

    # Get the lengths of the tokenized strings
    m = len(string1)
    n = len(string2)

    # Initialize a 2D list for dynamic programming
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Populate the dynamic programming table
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                # Determine the cost based on whether the current characters are equal
                cost = 0 if string1[i - 1] == string2[j - 1] else 1

                # Update the dynamic programming table with the minimum of three operations
                dp[i][j] = min(
                    dp[i - 1][j] + 1,     # Deletion
                    dp[i][j - 1] + 1,     # Insertion
                    dp[i - 1][j - 1] + cost  # Substitution
                )

    # Return the dynamic programming table and the maximum length of the input strings
    return dp, max(m, n)

def main(string1, string2, stopwords, syn_ant_dict):

    matrix, max_length = minDistance(string1, string2)
    _, ids = backtrace(string1, string2, matrix, stopwords, syn_ant_dict)

    return ids, max_length

if __name__ == "__main__":

    sample1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    sample2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
    sample3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

    matrix1 = minDistance(sample1, sample2)
    matrix2 = minDistance(sample1, sample3)

    with open("stopwords.txt", "r") as sw:
        data = sw.read()
        stopwords = data.split("\n") 

    syn_ant_dict = {"love":[("lust", "passion"), ("hate","dislike")]}

    ids, max_length = main(sample1, sample2, stopwords, syn_ant_dict)

    response = {}
    response["insertions"] = ids[0]
    response["deletions"] = ids[1]
    response["substitutions"] = ids[2]
    response["penalty"] = ids[3]
    response["similarity_score"] = 1 - sum(ids) / max_length

    print(response)