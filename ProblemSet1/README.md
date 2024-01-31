# Problem 1.3: Markdown

## Aidan McDougall Submission 1.31.24
### Analysis of pseudocode in PhoneBookSearch.txt

1. The algorithm is systematically searching for the desired name in the phonebook by eliminating half of the book at a time. If 'Smith' is earlier in the book, the entire second half of the book is no longer required for our current search. The goal of the algorithm is to find the desired name `Mike Smith`

2. In the phonebook search, the algorithm is over time removing every option that isn't `Mike Smith.` This requires a simple process to be repeated over and over to get a desired result. This process would likely take a while if the desired name is slightly outside the range of the "pages" on which the name is being searched for. 

3. If the name is not found, steps for procuring a new page are enacted. Specifically, opening the book to the left half or the right half depending on where the name resides. 

4. If the name is found, as determined in step five, the process will \*Call Mike\*

### Some extra questions I had in this assignment - 
\*Does this process fail if there are an even number of names?
\*Step 2 is "Open to middle of Book". According to the else clauses, wouldn't the algorithm get stuck in a loop of opening the book to the middle?