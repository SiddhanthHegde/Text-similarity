def backtrace(string1, string2, matrix, stopwords, syn_ant_dict):
    """
    Performs backtracking on a dynamic programming matrix to identify the optimal alignment
    between two input strings, considering stop word penalties and synonyms/antonyms penalties.

    Parameters:
    - string1 (str): The first input string.
    - string2 (str): The second input string.
    - matrix (list): The dynamic programming matrix computed using the minDistance function.
    - stopwords (set): A set of stop words that incur penalties during alignment.
    - syn_ant_dict (dict): A dictionary containing synonyms and antonyms for words.

    Returns:
    - trace (list): A list of indices representing the optimal alignment path in the matrix.
    - operation_counts (list): A list containing the count of insertions, deletions, substitutions,
                               and extra penalties incurred during the alignment.
    """
    # Tokenize the input strings into lists of words
    string1 = string1.split()
    string2 = string2.split()

    # Initialize variables for row and column indices, and trace list
    row = len(string1)
    col = len(string2)
    trace = [[row, col]]

    # Initialize counts for insertions, deletions, substitutions, and extras
    insertions, deletions, substitutions = 0, 0, 0
    extras = 0

    # Set penalty values for stop words, synonyms, and antonyms
    stop_word_penalty = -0.25
    syn_penalty = -0.8
    ant_penalty = 2

    # Perform backtracking until reaching the top or left boundary of the matrix
    while True:
        word1 = string1[row - 1]
        word2 = string2[col - 1]

        # Check if the current words are equal
        if word1 == word2:
            cost = 0
        else:
            cost = 1
            # Apply stop word penalty if either word is a stop word
            if word1 in stopwords or word2 in stopwords:
                extras += stop_word_penalty

        # Retrieve values for the current, diagonal, above, and left cells in the matrix
        cur = matrix[row][col]
        up = matrix[row - 1][col]
        diag = matrix[row - 1][col - 1]
        left = matrix[row][col - 1]

        # Check the optimal alignment operation and update trace accordingly
        if cur == diag + cost:
            # Substitution
            trace.append([row - 1, col - 1])
            row, col = row - 1, col - 1

            # Increment substitution count and check for synonyms/antonyms penalties
            if cost == 1:
                substitutions += 1
                
                if syn_ant_dict.get(word1) is not None:
                    syns = syn_ant_dict[word1][0]
                    ants = syn_ant_dict[word1][1]

                    if word2 in syns:
                        extras += syn_penalty
                    
                    if word2 in ants:
                        extras += ant_penalty
                
        else:
            if cur == up + 1:
                # Insertion
                trace.append([row - 1, col])
                insertions += 1
                row, col = row - 1, col

            elif cur == left + 1:
                # Deletion
                trace.append([row, col - 1])
                deletions += 1
                row, col = row, col - 1

        # Check if reached the top or left boundary of the matrix
        if row == 0 or col == 0:
            return trace, [insertions, deletions, substitutions, extras]