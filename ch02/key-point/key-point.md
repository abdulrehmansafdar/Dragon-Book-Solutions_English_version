# Chapter 2 Key Points

### 1. Grammar, grammar-guided translation solutions, grammar-guided translators

Take an expression that only supports single-digit addition and subtraction as an example.

1. Grammar

list -> list + digit | list - digit | digit

digit -> 0 | 1 | … | 9

2. Syntax-guided translation scheme (eliminating left recursion)

expr -> term rest

rest -> + term { print('+') } rest | - term { print('+') } rest | ε

term -> 0 { print('0') } | 1 { print('1') } | … | 9 { print('9') }

4. Grammar-guided translator

See p46 for java code

### 2. Syntax tree, syntax analysis tree

Take 2 + 5 - 9 as an example

![Syntax tree and parse tree](https://raw.github.com/fool2fish/dragon-book-practice-answer/master/ch02/key-point/assets/dragonbook-keypoint-2.2-2.png)

### 3. Regular grammar, context-free grammar, context-sensitive grammar?

Grammatical abbreviation:

- RG: [Regular Grammar](http://en.wikipedia.org/wiki/Regular_grammar)
- CFG: [Context-free Grammar](http://en.wikipedia.org/wiki/Context-free_grammar)
- CSG: [Context-sensitive Grammar](http://en.wikipedia.org/wiki/Context-sensitive_grammar)

#### Regular grammar

[wiki](http://en.wikipedia.org/wiki/Regular_grammar)

All productions of regular grammar after the standard should satisfy one of the following three situations:

B->a
B -> a C
B ->epsilon

The key points are:

1. The left-hand side of the production must be a non-terminal symbol.
2. The right hand side of a production can have nothing, a terminal symbol, or a terminal symbol plus a non-terminal symbol.

From the perspective of production, such a provision makes it possible to produce zero or one terminal symbol every time a production rule is applied, until the string we want is finally produced.

From a matching point of view, this provision makes it possible to consume one non-terminal symbol each time a rule is applied until the entire string is matched.

The automaton corresponding to the language defined in this way has one property: a finite state automaton.

To put it simply, you only need to record the current state and get the next input symbol to determine the next state transition.

#### Regular grammar and context-free grammar

The biggest difference between CFG and RG is that there can be zero or more terminal symbols or non-terminal symbols on the right hand side of the production, and there is no limit on the order or number.

Consider a classic example of pairwise matching of parentheses:

expr -> '(' expr ')' | epsilon

In this production (just look at the first sub-production), there is a non-terminal expr on the right-hand side, but there are terminal symbols on both sides of it. This production cannot be normalized to strict RG.This is an example of CFG.

Its corresponding automaton not only needs to record the current state, but also records the history of reaching the current position, so that it can determine the state transition based on the next input symbol.The so-called "history" here is the stack that stores matching rules.

The automaton corresponding to CFG is PDA (pushdown automaton).

The rules of RG are strict, and the advantage is that the automaton it corresponds to is very simple, so it can be implemented in a very efficient and simple way.

#### Context-sensitive grammar

CSG further relaxes restrictions on the basis of CFG.

There can also be terminal and non-terminal symbols on the left hand side of a production.The left-hand terminator is where the "context" comes from.That is to say, when matching, you can't just look at where the current match is, but also look at what is on the left and right of the current position (that is, what the context is). The context will not be consumed when this rule is applied, it is just a "look".

The next layer above CSG is PSG, phrase structure grammar.

Basically, all restrictions on CSG are lifted.

There can be any number of terminal symbols and non-terminal symbols in any order on the left and right sides.

Anyway, if you don’t do natural language processing, you won’t encounter this kind of grammar, so I won’t go into details.

### 4. Why do the priorities of n operators correspond to n+1 productions?

Priority processing can be solved at the pure grammar level, or it can be handled in other ways in the parser implementation.

From the purely grammatical level, there are as many priorities as there are plus one production.

The grammar of the four arithmetic operations introduced in the book will make addition and subtraction closer to the root, and multiplication and division farther from the root.

The shape of the syntax tree determines the calculation order of nodes. Nodes far from the root will be processed first, so it seems that multiplication and division are calculated first, that is, multiplication and division have higher priority.

Reference: http://rednaxelafx.iteye.com/blog/492667

### 5. What are the effective principles for avoiding ambiguous grammar?

The ambiguity problem is mainly related to the characteristics of CFG.

CFG's selection structure ("|") has no specified order or priority.
At the same time, multiple rules may have a common prefix,
This will cause ambiguity problems.

PEG is something similar to CFG, and its language expression is similar to CFG.
But there is no ambiguity at the grammatical level, because its selection structure ("|") has an order or priority.

### 6. Avoid infinite loops caused by left-recursive grammar in the predictive analyzer

Production:

A -> A x |and

Syntax-guided translation pseudocode snippet:

void A(){
switch(lookahead){
case x:
A();match(x);break;
case y:
match(y):break;
default:
report("syntax error")
}
}

When the statement conforms to the form A x, the A() operation will fall into an infinite loop, which can be avoided by changing the production to the equivalent non-left recursive form:

B -> y C

C -> x C | ε

### 7. Why is it difficult to translate expressions containing left associative operators in right-recursive grammars?

### 8. Lvalue and rvalue issues when generating intermediate code.

After reading the pseudocode of lvalue() and rvalue() in the book, I feel that lvalue() can be used to handle both lvalues ​​and rvalues. For rvalues, you either have to handle them yourself. For rvalues ​​that can be used as lvalues, lvalue() is called.

Why not just use value() and be done with it?