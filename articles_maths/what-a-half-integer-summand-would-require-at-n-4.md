# __What a Half-Integer Summand Would Require at $n=4$__

## Introduction

**The subject.** The carriers of the algebra have the labels $0,1,2,3$. The article asks what a summand of label $\tfrac12$ or $\tfrac32$ would require, and answers that it would require a two-dimensional or a four-dimensional invariant subspace, and that no such subspace exists.

**The order of the article.** The first section fixes what a half-integer summand would be. The second lists the four requirements and shows that each fails. The third separates the two notions that the failure is often confused with, invariance and being a summand. The fourth gives the counterexample that the algebra *does* contain objects of the module's shape, namely the ideals, and the weights that distinguish them. The fifth states the boundary.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$*, *Why the Conjugation Labels Are Integer*, and *The Minimal Left Ideals of $M_4(\mathbb{C})$*. The row at order two is *What a Half-Integer Summand Would Require*.

**The result in one line.** A half-integer summand would need a carrier of dimension $2j+1$ with $2j$ odd, hence an even-dimensional invariant subspace, and every invariant subspace of the algebra has odd dimension.

**Boundaries.** The article is a negative statement with a complete proof; it does not classify the invariant subspaces of the algebra beyond the parity of their dimensions, which is *The Four Carrier Lists of One Algebra*.

## What Would Be Required

**Definition.** A **half-integer summand** would be a subspace $W\subseteq M_4(\mathbb{C})$ which is invariant under the copy and on which the copy acts by the label $j$ with $2j$ odd.

**Proposition.** Such a $W$ would have dimension $2j+1$, an even number, and would be the isotypic component of its label.

*Proof.* The dimension of the irreducible module of label $j$ is $2j+1$; for $2j$ odd this is even. An invariant subspace on which the action is irreducible of label $j$ is a copy of that module, and in a completely reducible module the copies of one label form one isotypic component.

**Corollary.** A half-integer summand would be a direct sum of copies of a module of even dimension, so its dimension would be even.

*Proof.* The proposition, and a sum of even numbers is even.

**Corollary.** It would suffice to exhibit one even-dimensional invariant subspace, since every invariant subspace is a sum of carriers.

*Proof.* The algebra is completely reducible, so an invariant subspace is a sum of isotypic components, and its dimension is a sum of the numbers $2k+1$ with multiplicities.

**The reading.** The question is finite: there are sixteen dimensions to check and four carriers, and the parity of the dimension is already an obstruction.

## The Four Requirements

**Proposition.** A half-integer summand would require (i) a carrier whose label is a half-integer, (ii) a weight string with half-integer weights, (iii) a dimension $2j+1$ with $2j$ odd, and (iv) a sum of labels in the Clebsch–Gordan rule equal to a half-integer. Each fails at $n=4$.

*Proof.* (i) The four carriers have the labels $0,1,2,3$, all integers. (ii) The algebra's weights are differences of the module's weights and are integers, so no weight string of the algebra contains a half-integer. (iii) The carrier dimensions are $1,3,5,7$, all odd. (iv) The tensor square of $V_{3/2}$ decomposes into the labels $0,\dots,2j$, which are integers.

**Corollary.** The failure is not an accident of the computation but a consequence of the parity of $2j$ and of the fact that the labels of a tensor square are differences of weights.

*Proof.* The four statements.

**Corollary.** At odd order the same four requirements are met by the module itself, which is then a carrier; the obstruction is specific to even order.

*Proof.* At odd $n$ the label $\tfrac{n-1}{2}$ is an integer, and the module is a carrier of odd dimension.

**The reading.** Four independent arguments give the same answer, and each of them is a parity statement.

## Invariance against Being a Summand

**Proposition.** The algebra contains no even-dimensional invariant subspace.

*Proof.* Every invariant subspace is a sum of isotypic components, whose dimensions are the carrier dimensions $1,3,5,7$; a sum of odd numbers is odd.

**Corollary.** No invariant subspace of the algebra has dimension two or four, so no half-integer summand exists and the module cannot be realised inside the algebra as an invariant subspace.

*Proof.* The proposition, and the dimensions two and four are even.

**Corollary.** The failure is not that the algebra lacks subspaces of dimension four: it has many. The failure is that none of them is invariant.

*Proof.* The space of all four-dimensional subspaces is a Grassmannian of positive dimension; invariance is the extra condition, and it fails by the parity of the dimension.

**The reading.** The two notions are often confused. The module has dimension four, and so do the minimal left ideals and the left ideals $M_4P$; what the algebra does not have is a four-dimensional *invariant* subspace.

## The Counterexample and the Distinction

**Proposition.** The minimal left ideal $M_4P$, of complex dimension four, is a subspace of the algebra of the module's dimension, and it is not invariant under the conjugation action; it is invariant under the left multiplication by the algebra.

*Proof.* The ideal has dimension four by the rank of $P$; conjugation carries $M_4P$ to $M_4\rho(q)P\rho(q)^{-1}$, which is a different ideal unless $q$ stabilises the line of $P$; left multiplication by $A\in M_4$ carries $M_4P$ into itself.

**Corollary.** The half-integer label is carried by the ideal under the left action, and the same subspace carries no half-integer label under the conjugation action.

*Proof.* The ideal is isomorphic to $V_{3/2}$ as a left module; the conjugation action on the algebra has integer weights, so on the ideal, as a subspace of the algebra, the conjugation weights are integers.

**Corollary.** The weight test separates the two actions: under left multiplication the weights are $\pm\tfrac32,\pm\tfrac12$, under conjugation they are differences of these and therefore integers.

*Proof.* The weights of the two actions on the same four-dimensional space.

**The reading.** The same subspace carries a half-integer label for one action and integer weights for another. A half-integer summand would require the second action to have half-integer weights, which it does not.

## The Boundary

**Against the ideal article.** That article constructs the ideals and computes their left weights; this one uses them as the counterexample that shows why a half-integer label does not give a half-integer summand.

**Against the integer labels article.** That article proves the integrality from the kernel and from the weights; this one states what would fail if the integrality failed.

**Against the odd orders.** At odd order the module is a carrier and the question does not arise; the article is about even order, and the number four is the case at hand.

## The Check of the Requirement

**The parity obstruction.** A half-integer summand inside the algebra would contribute an odd-dimensional carrier to a space whose dimension is a square of an integer; the square is even when the integer is even, and the sum of odd numbers can be even only when the number of summands is even, which is the parity obstruction.

## Summary

A half-integer summand of the algebra would be a copy of a module of even dimension $2j+1$ with $2j$ odd, hence an even-dimensional invariant subspace. Every invariant subspace of the algebra is a sum of carriers, whose dimensions are $1,3,5,7$, so every invariant subspace has odd dimension and no half-integer summand exists.

The four requirements, a half-integer label, a half-integer weight string, an even dimension and a half-integer Clebsch–Gordan label, each fail at $n=4$: the labels are $0,1,2,3$, the weights are integers, the dimensions are odd and the tensor rule gives integers.

The algebra does contain subspaces of dimension four, namely the minimal left ideals, and they are not invariant under conjugation. The distinction between a subspace of the module's dimension and an invariant subspace of the module's label is the content of the article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $W$ | a hypothetical half-integer summand |
| $2j+1$, $2j$ odd | the even dimension it would have |
| $1,3,5,7$ | the carrier dimensions |
| $M_4P$ | a minimal left ideal, dimension four, not invariant |
| $\pm\tfrac32,\pm\tfrac12$ | the weights of the ideal under left multiplication |

## Further Reading

- [Why the Conjugation Labels Are Integer: the Kernel $\{\pm\mathrm I\}$](why-the-conjugation-labels-are-integer-at-n-4.html), for the integrality.
- [The Minimal Left Ideals of $M_4(\mathbb{C})$ and the Module $V_{3/2}$](the-minimal-left-ideals-of-m4c.html), for the ideals.
- [The Four Carrier Lists of One Algebra at $n=4$](the-four-carrier-lists-of-one-algebra-at-n-4.html), for the invariant subspaces.
- [What a Half-Integer Summand Would Require](what-a-half-integer-summand-would-require.html), for the row at order two.
- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module-at-n-4.html), for the parity statements.
