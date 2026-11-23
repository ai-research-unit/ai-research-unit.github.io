# __The Parity Rule at $n=4$: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$__

## Introduction

**The subject.** The symmetric square of the module has dimension ten and the alternating square has dimension six, and each decomposes into two carriers. The symmetric square keeps the labels of the parity of $2j$ and the alternating square keeps the others; that is the whole content of the rule.

**The order of the article.** The first section states the two decompositions and counts dimensions. The second computes the weights of the two squares and matches them with the carriers. The third proves the parity criterion. The fourth compares with the tensor square and with the algebra. The fifth treats the row at order two and draws the boundary.

**It assumes** *The Four Weights of the Module and the Half Angle at $n=4$* for the weights and *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the labels. The row at order two is *The Parity Rule: the Two Squares of the Module*.

**The result in one line.** $\operatorname{Sym}^{2}V_{3/2}=V_3\oplus V_1$ with $10=7+3$, and $\Lambda^{2}V_{3/2}=V_2\oplus V_0$ with $6=5+1$.

**Boundaries.** The article treats the two squares as modules; it does not treat the symmetric and alternating *halves of the algebra*, which are cut by the transpose and are the subject of *Neither Half Is Invariant*. It does not treat the products of carriers, which is *The Truncated Rule*.

## The Two Decompositions

**Theorem.** $\operatorname{Sym}^{2}V\cong V_3\oplus V_1$ and $\Lambda^{2}V\cong V_2\oplus V_0$, with complex dimensions $10=7+3$ and $6=5+1$.

*Proof.* The Clebsch–Gordan rule gives $V\otimes V=\bigoplus_{k=0}^{3}V_k$. The symmetric part of the tensor square of an irreducible module of label $j$ contains the labels $k$ with $2j-k$ even, and the alternating part the labels with $2j-k$ odd; with $2j=3$ the even case gives $k=3,1$ and the odd case $k=2,0$. The dimensions add up: $\dim\operatorname{Sym}^{2}V=10$ and $\dim\Lambda^{2}V=6$, and $7+3=10$, $5+1=6$.

**Corollary.** The four labels are split two and two between the squares, and no label occurs in both.

*Proof.* The parities of $2j-k$ for the four labels are $0,1,0,1$.

**Corollary.** Each square is a sum of exactly two carriers, and each carrier occurs in exactly one square.

*Proof.* The theorem, and the four labels are distinct.

**The check on dimensions.** $\dim\operatorname{Sym}^{2}V=4\cdot5/2=10$ and $\dim\Lambda^{2}V=4\cdot3/2=6$, and the sums of the carrier dimensions agree.

*Proof.* The two binomial counts.

## The Weights of the Two Squares

**Proposition.** The weights of $\operatorname{Sym}^{2}V$ are the ten sums $m+m'$ with $m\le m'$, namely $3,2,1,0,-1,-2,-3$ together with $1,0,-1$; the weights of $\Lambda^{2}V$ are the six sums with $m<m'$, namely $2,1,0,-1,-2$ together with $0$.

*Proof.* The weights of the symmetric square are the sums over unordered pairs with repetition and the weights of the alternating square the sums over unordered pairs without repetition; with the weights $\pm\tfrac32,\pm\tfrac12$ the sums are as displayed.

**Corollary.** The multiset of $\operatorname{Sym}^{2}V$ is $3,2,1,1,0,0,-1,-1,-2,-3$, which is the union of the strings $3,2,1,0,-1,-2,-3$ and $1,0,-1$.

*Proof.* The proposition, read as a multiset.

**Corollary.** The multiset of $\Lambda^{2}V$ is $2,1,0,0,-1,-2$, which is the union of the strings $2,1,0,-1,-2$ and $0$.

*Proof.* The same reading.

**The check against the tensor square.** The union of the two multisets is the multiset of $V\otimes V$, of sixteen weights, with each symmetric weight once and each alternating weight once; the two squares are complementary inside the tensor square.

*Proof.* The sums with repetition and without partition the sixteen ordered sums.

## The Parity Criterion

**Proposition.** In the tensor square of $V_j$, the label $k$ occurs in $\operatorname{Sym}^{2}$ exactly when $2j-k$ is even, and in $\Lambda^{2}$ exactly when $2j-k$ is odd.

*Proof.* In the tensor square, the flip of the two factors acts on the summand of label $k$ by the sign $(-1)^{2j-k}$; that is the standard computation with the highest weight vector, since the flip exchanges the two factors and the summand of label $2j$ is the symmetric one. A summand with sign $+1$ lies in the symmetric square and one with sign $-1$ in the alternating square.

**Corollary.** At $2j=3$ the symmetric square carries $k=3$ and $k=1$ and the alternating square carries $k=2$ and $k=0$.

*Proof.* $3-k$ is even for $k=3,1$ and odd for $k=2,0$.

**Corollary.** The parity of $k$ relative to $2j$ is the only thing the two squares select: the sizes $2k+1$ are not involved in the criterion.

*Proof.* The sign $(-1)^{2j-k}$ depends only on the parity of $2j-k$.

**The reading.** The symmetric square keeps the labels of the same parity as the top label and the alternating square the others. At half-integer $j$ the top label is a half-integer, and so the integer labels split by their own parity; at integer $j$ the top label is an integer and the rule keeps the even labels symmetric.

*Proof.* The criterion with $2j$ odd and with $2j$ even.

## The Comparison with the Other Squares

**Against the tensor square.** The tensor square is the sum of the two squares, and its eight labels, counted with multiplicity, are the four carriers with multiplicities: $V_3$ and $V_1$ once each from the symmetric square, $V_2$ and $V_0$ once each from the alternating square.

**Against the algebra.** The algebra is the tensor square of the module, and its four carriers are the same four labels; the squares of the module are not subspaces of the algebra in a natural way, since the module is not a subspace of its own tensor square.

**Against the carriers of the algebra.** The carrier $V_2$ of the algebra is the alternating square of the module minus the centre, and the carrier $V_3$ is the symmetric square minus the triplet; the two readings of the same label are different spaces.

## The Row at Order Two

**Proposition.** At $n=2$ the module is $V_{1/2}$ and $\operatorname{Sym}^{2}V_{1/2}=V_1$, $\Lambda^{2}V_{1/2}=V_0$, with dimensions $3$ and $1$.

*Proof.* The weights are $\pm\tfrac12$; the symmetric square has the sums $1,0,-1$ and dimension three, the alternating square has the sum $0$ and dimension one; the criterion gives $2j-k$ even for $k=1$ and odd for $k=0$.

**Corollary.** The mechanism is the same at the two rows: the symmetric square keeps the labels of the parity of $2j$ and the alternating square the others.

*Proof.* The criterion does not depend on the order.

**The reading.** At $n=2$ the alternating square is one-dimensional, the scalars, and the symmetric square is the triplet; at $n=4$ the alternating square has two pieces and the symmetric square two. The parity rule is the same rule and the sizes differ.

## The Check of the Signs

**The symmetry.** The tensor square of the module splits into the symmetric and the alternating parts, and the two parts are the eigenspaces of the exchange operator with eigenvalues $+1$ and $-1$; the highest weight of the symmetric part is the sum of the two highest weights and that of the alternating part is the sum minus one, which is the origin of the parity rule.

**The labels.** The symmetric part carries the labels of the same parity as twice the label of the module, and the alternating part the others; the module has twice the label equal to three, an odd number, so the symmetric part carries the even labels and the alternating part the odd ones, read in the other convention.

**The dimensions.** The two parts have dimensions ten and six, and the four carriers are distributed as seven plus three and five plus one; the check is that the two sums add to the dimension of the tensor square, which is the square of the dimension of the module.

## Summary

The symmetric square of the module is $V_3\oplus V_1$, of dimension $10=7+3$, and the alternating square is $V_2\oplus V_0$, of dimension $6=5+1$. The weights confirm the decomposition: the symmetric square has $3,2,1,0,-1,-2,-3$ together with $1,0,-1$, and the alternating square has $2,1,0,-1,-2$ together with $0$.

The criterion is the parity of $2j-k$: the flip of the two factors acts on the summand of label $k$ by $(-1)^{2j-k}$, so the symmetric square keeps the labels of the parity of $2j$ and the alternating square the others. At $2j=3$ that gives $3,1$ and $2,0$.

At order two the same criterion gives $\operatorname{Sym}^{2}V_{1/2}=V_1$ and $\Lambda^{2}V_{1/2}=V_0$; the sizes change with the order and the rule does not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=V_{3/2}$ | the module |
| $\operatorname{Sym}^{2}V$ | the symmetric square, dimension ten |
| $\Lambda^{2}V$ | the alternating square, dimension six |
| $(-1)^{2j-k}$ | the sign of the flip on the summand of label $k$ |
| $2j=3$ | the top label |

## Further Reading

- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the labels of the tensor square.
- [Neither Half Is Invariant: the Cartan Element Carries $\operatorname{Sym}$ into $\Lambda$](neither-half-is-invariant-the-cartan-element-at-n-4.html), for the halves of the algebra.
- [The Truncated Rule: the Product of Two Carriers Is Not a Carrier](the-truncated-rule-the-product-of-two-carriers-at-n-4.html), for the products.
- [The Parity Rule: the Two Squares of the Module](the-parity-rule-the-two-squares-of-the-module.html), for the row at order two.
- [The Spin-Two Carrier of $M_4(\mathbb{C})$](introduction-to-the-spin-two-carrier-of-m4c.html), for the carrier $V_2$ as the alternating square.
