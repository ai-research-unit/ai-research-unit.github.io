# __Four Integer Labels and One Half-Integer Module: $\tfrac32$ Is a Weight, Not a Label__

## Introduction

**The subject.** The algebra has four labels, all integers, and its module has one label, $\tfrac32$, which is not among them. The half-integer does not disappear: it goes into the weights of the module and of its minimal left ideals, into the eigenvalues of the elements of the algebra, and into the corners of the block display.

**The order of the article.** The first section lists the labels of the algebra and of the module. The second explains why the algebra's labels cannot be half-integers. The third shows where the half-integers reappear as weights. The fourth shows where they reappear as eigenvalues, with the pair $(\tfrac12,\tfrac12)$ and the corners. The fifth draws the lesson and the boundary.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the labels, *The Minimal Left Ideals of $M_4(\mathbb{C})$ and the Module $V_{3/2}$* for the ideal. The row at order two is *Half-Integer Weights Cancel in the Differences*.

**The result in one line.** The algebra carries the integer labels $0,1,2,3$, the module carries $\tfrac32$, and a half-integer eigenvalue of an algebra element is not a half-integer label.

**Boundaries.** The article does not re-prove the decomposition or the ideal structure; it locates the half-integer in each of the four places where it occurs and separates the label from the eigenvalue.

## The Two Lists

**Proposition.** The carriers of the algebra have labels $0,1,2,3$ and dimensions $1,3,5,7$; the module has label $\tfrac32$ and dimension $4$.

*Proof.* The tensor square of $V_{3/2}$ decomposes into the labels $0,1,2,3$, and the module's dimension is $2\cdot\tfrac32+1=4$.

**Corollary.** The label $\tfrac32$ is not a carrier label, and no carrier has dimension $4$.

*Proof.* The labels are integers and the dimensions $2k+1$ are odd, while $4$ is even.

**Corollary.** The weights of the algebra are integers and the weights of the module are half-integers.

*Proof.* The algebra's weights are differences of module weights, and the difference of two half-integers is an integer.

**The reading.** The two lists are the two halves of the same statement: the module has the half-integer label and the algebra the integer ones, and neither list can be deduced from the other without the tensor rule.

## Why the Labels Are Integers

**Proposition.** If a label $j$ occurs in the decomposition of the algebra, then $j$ is an integer, because $j$ is a difference of two weights of the module and the module's weights are all congruent to $\tfrac32$ modulo $1$.

*Proof.* The weights of $V_{3/2}$ are $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$; each is congruent to $\tfrac12$ modulo $1$, so the difference of two of them is congruent to $0$.

**Corollary.** The four labels $3,2,1,0$ are the integers between $0$ and $2j$, and the half-integer $2j-1=2$ is not among them because it is not a label at all: the labels are integers and the values $2j-k$ are the integers $0,\dots,3$.

*Proof.* The labels are integers and their values run from $0$ to $2j=3$.

**Corollary.** At half-integer $j$ the ring of labels is the integers and the module is the only object with a half-integer label; at integer $j$ the module itself has an integer label and appears as a carrier.

*Proof.* The two cases $2j$ odd and $2j$ even.

**The reading.** The half-integer does not disappear from the algebra; it is pushed into the weights. The next section follows it there.

## The Half-Integers as Weights

**Proposition.** The module has the four weights $\pm\tfrac32,\pm\tfrac12$, and every minimal left ideal, being isomorphic to the module, has the same four weights under the left action of the diagonal generator.

*Proof.* The module's weight string is the ladder from $\tfrac32$ down to $-\tfrac32$; a left ideal is isomorphic to the module as a left module, and the diagonal generator acts by the same weights.

**Corollary.** The weights $\tfrac32$ and $\tfrac12$ occur in the ideal and in no carrier of the algebra; the algebra's weight spaces have integer weights only.

*Proof.* The algebra's weights are differences of module weights, hence integers; the ideal's weights are the module's.

**Corollary.** The raising operator moves the weight $\tfrac12$ to $\tfrac32$ inside the ideal, and the lowering operator moves $\tfrac32$ to $\tfrac12$; both stay inside the ideal.

*Proof.* The ideal is invariant under the left action, which contains the two operators.

**The numerical check.** The diagonal generator in the weight basis is diagonal with the entries $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, and the raising operator has nonzero entries only between consecutive weights, of the values $\sqrt3,2,\sqrt3$.

*Proof.* The ladder relations $J_+v_m=\sqrt{(j-m)(j+m+1)}\,v_{m+1}$ with $j=\tfrac32$.

## The Half-Integers as Eigenvalues

**Proposition.** The algebra contains the element with eigenvalues $\tfrac12,\tfrac12,-\tfrac12,-\tfrac12$, namely the diagonal matrix with those entries in the weight basis, and this element decomposes as a sum of a vector in $V_1$ and a vector in $V_3$ with squared norms in the ratio $4:1$.

*Proof.* The element is diagonal, hence an algebra element; projecting it on the four carriers gives norms $0.894$ and $0.447$ on $V_1$ and $V_3$ and zero on the other two, whose squares are in the ratio $4:1$ and sum to one.

**Corollary.** A half-integer eigenvalue does not make the element a half-integer object: its weights are differences of weights and its label is an integer.

*Proof.* The element lies in $V_1\oplus V_3$, and its eigenvalues are the diagonal entries, not the weights.

**Proposition.** In the block display of the module by the two halves $\{v_{3/2},v_{1/2}\}$ and $\{v_{-1/2},v_{-3/2}\}$, the diagonal blocks carry the weights $\tfrac32,\tfrac12$ and $-\tfrac12,-\tfrac32$, and the off-diagonal corners carry the entries that connect a weight of one half with a weight of the other.

*Proof.* The weight basis orders the four vectors by decreasing weight, and the matrix of an operator in that basis has the block structure of the two halves.

**Corollary.** The extreme eigenvalues $\pm\tfrac32$ occur on the diagonal of the display, and the corners connect them to the weights $\mp\tfrac12$, so a corner element has eigenvalues differing by integers.

*Proof.* The corner entries have weights $\pm1$ and $\pm2$, being differences of a weight of the first half and a weight of the second; the eigenvalues of a corner element are computed from its $2\times2$ blocks and differ by integer amounts.

**The reading.** Half-integers occur in three places: as the module's label, as the module's weights, and as eigenvalues of algebra elements. Only the first two are representation-theoretic; the third is a statement about a chosen basis.

## The Lesson

**Proposition.** The label of an object under the copy is a half-integer exactly when the object is a module and not a carrier; the algebra is a carrier sum and its labels are integers.

*Proof.* The carriers are the isotypic pieces of the algebra, whose labels are differences of module weights.

**Corollary.** The rule "the algebra has integer labels, the module has the half-integer label" holds at every even order, and at odd orders the module's label is an integer and the distinction disappears.

*Proof.* The label of the module is $\tfrac{n-1}{2}$, an integer exactly for odd $n$.

**The boundary.** The article does not claim that the half-integer is absent from the algebra: it is present as a weight of the ideal and as an eigenvalue. What is absent from the algebra is a *carrier* with a half-integer label.

## Summary

The algebra has the labels $0,1,2,3$ and the module has $\tfrac32$. The algebra's labels are integers because they are differences of the module's weights, which are all congruent to $\tfrac12$ modulo one.

The half-integer survives in three places: as the label of the module and of every minimal left ideal, as the weights $\pm\tfrac32,\pm\tfrac12$ of that ideal, and as the eigenvalues of algebra elements such as the diagonal element with entries $\tfrac12,\tfrac12,-\tfrac12,-\tfrac12$, which lies in $V_1\oplus V_3$ with squared norms in the ratio $4:1$.

A half-integer eigenvalue is not a half-integer label. The distinction is the content of the article, and it is the reason the algebra has four integer labels while its module has one half-integer label.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $0,1,2,3$ | the labels of the carriers |
| $\tfrac32$ | the label of the module |
| $\pm\tfrac32,\pm\tfrac12$ | the weights of the module and of the ideal |
| $\operatorname{diag}(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12)$ | an algebra element with half-integer eigenvalues |
| $2j=n-1$ | the identity fixing the slot |

## Further Reading

- [The Slot and the Summand at $n=4$](the-slot-and-the-summand-at-n-4.html), for the identity $2j=n-1$.
- [The Minimal Left Ideals of $M_4(\mathbb{C})$ and the Module $V_{3/2}$](the-minimal-left-ideals-of-m4c.html), for the ideal.
- [The Four Weights of the Module and the Half Angle at $n=4$](the-four-weights-of-the-module-and-the-half-angle-at-n-4.html), for the weights.
- [Four Integer Labels and One Half-Integer Module](four-integer-labels-and-one-half-integer-module.html), for the row at order two.
- [The Conjugation Labels at $n=4$](the-conjugation-labels-at-n-4.html), for the argument from the difference of weights.
