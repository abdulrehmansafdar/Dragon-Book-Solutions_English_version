# Chapter 3 Key Points

### 1. Conversion from NFA, DFA to regular expressions

http://courses.engr.illinois.edu/cs373/sp2009/lectures/lect_08.pdf

### 2. KMP and its extended algorithm (p87)

Refer to matrix's blog post [Detailed explanation of KMP algorithm](http://www.matrix67.com/blog/archives/115).Examples are provided in the article to make it easier to understand.

### 3. Efficiency of string processing algorithm (p103)

For each constructed DFA state, we must construct at most 4|r| new states

### 4. Time and space trade-offs in DFA simulation (p116)

The algorithm shown in Figure 3-66

### 5. Minimize the number of states of a DFA (p115)

Note line 4 of Figure 3-64: "Transitions on a from states s and t both arrive at the same group in Π", not at the same state.If it is determined by whether they reach the same state, then if s and t transition to two different but indistinguishable states on a, s and t will be considered to be distinguishable.