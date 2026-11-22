# __The Slot and the Summand: $\tfrac12$ in $\mathbb{B}$ and $\tfrac32$ in $M_4(\mathbb{C})$__

## Introduction

**The subject.** At every order there is a slot: the label of the module, fixed by the dimension through $2j=n-1$. At even orders the slot is a half-integer and is not a summand label; at odd orders it is an integer and is one. At order four the slot is $\tfrac32$ and the summands are $0,1,2,3$; at order two the slot is $\tfrac12$ and the summands are $0,1$.

**The order of the article.** The first section states the identity $2j=n-1$ and derives the three invariants of the slot. The second lists the two rows side by side. The third proves the parallel and identifies what differs. The fourth treats the odd orders, where the slot is a summand. The fifth draws the boundary.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* and *Where the Half-Integers Go in $M_4(\mathbb{C})$*. The row at order two is *The Slot and the Summand*.

**The result in one line.** The slot is $\tfrac{n-1}{2}$, its module has dimension $n$ and $n$ weights, and its top weight is $\tfrac{n-1}{2}$; at $n=4$ the slot is $\tfrac32$ and the summands are $0,1,2,3$.

**Boundaries.** The article fixes the vocabulary of slot, module and summand; it does not re-derive the decomposition, and it does not treat the ideals except to name the object that carries the slot.

## The Slot and Its Invariants

**Definition.** The **slot** of the row of order $n$ is the number $j=\tfrac{n-1}{2}$; the **summands** are the integer labels $k$ occurring in the decomposition of the algebra.

**Proposition.** The dimension of the module is $2j+1=n$, the number of its weights is $n$, and its maximal weight is $j=\tfrac{n-1}{2}$.

*Proof.* The module is the symmetric power $\operatorname{Sym}^{2j}$ of the two-dimensional module, of dimension $2j+1=n$; an irreducible module of highest weight $j$ has the weights $j,j-1,\dots,-j$, of which there are $2j+1=n$.

**Corollary.** The three invariants of the slot are $n$, $n$ and $\tfrac{n-1}{2}$: the dimension, the number of weights and the maximal weight.

*Proof.* The proposition.

**Corollary.** The sum of the dimensions of the summands is $n^{2}$, the square of the dimension of the module.

*Proof.* $\sum_{k=0}^{n-1}(2k+1)=n^{2}$.

**The reading.** The identity $2j=n-1$ ties the slot to the size of the algebra: the module's top weight is half the distance from $0$ to $n-1$, and the summands are the integers of that interval.

## The Two Rows Side by Side

**Proposition.** At $n=2$ the algebra is $M_2(\mathbb{C})$, of dimension four, with the summands $0,1$ of dimensions $1,3$; the slot is $\tfrac12$, the module has dimension two and the weights $\pm\tfrac12$.

*Proof.* The tensor square of $V_{1/2}$ is $V_1\oplus V_0$, of dimensions $3+1=4$; the module has the two weights $\pm\tfrac12$.

**Proposition.** At $n=4$ the algebra is $M_4(\mathbb{C})$, of dimension sixteen, with the summands $0,1,2,3$ of dimensions $1,3,5,7$; the slot is $\tfrac32$, the module has dimension four and the weights $\pm\tfrac32,\pm\tfrac12$.

*Proof.* The tensor square of $V_{3/2}$ is $V_3\oplus V_2\oplus V_1\oplus V_0$, of dimensions $7+5+3+1=16$; the module has the four weights $\pm\tfrac32,\pm\tfrac12$.

**Corollary.** The two rows are the cases $n=2$ and $n=4$ of one formula: $n$ summands $0,\dots,n-1$, total dimension $n^{2}$, module of dimension $n$ with the slot $\tfrac{n-1}{2}$.

*Proof.* The two propositions and the identity $2j=n-1$.

**Corollary.** In both rows the slot is a half-integer and is not a summand.

*Proof.* $\tfrac12$ is not among $0,1$, and $\tfrac32$ is not among $0,1,2,3$.

**Proposition.** At $n=2$ the same computation inside the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ gives the slot $\tfrac12$, the module $V_{1/2}$ of dimension two, and the summands $0,1$; the row of the biquaternion algebra is the row of order two.

*Proof.* The biquaternion algebra is $M_2(\mathbb{C})$ as a complex algebra, and the conjugation action of its copy $SU(2)$ has the module $V_{1/2}$ and the two carriers $V_1,V_0$.

**The reading.** The two rows agree in structure and differ in the value of the slot. The structure is the formula; the value is the order.

## What Differs

**Proposition.** The differences between the rows are the size of the algebra, $4$ against $16$; the number of summands, $2$ against $4$; the dimension of the module, $2$ against $4$; and the value of the slot, $\tfrac12$ against $\tfrac32$.

*Proof.* The two lists above.

**Corollary.** The dimension of the algebra is the square of the dimension of the module, and the number of summands is the dimension of the module.

*Proof.* $n^{2}$ and $n$ with $n=\dim V$.

**Corollary.** Nothing else differs: the weight strings, the parity rule, the intersection table and the rank stratification are the same statements at the two orders with the numbers changed.

*Proof.* Each of these statements is a function of $j$ and $n$ only.

**The reading.** The row at order four is the row at order two with the slot raised from $\tfrac12$ to $\tfrac32$; the mechanism is the same and the sizes are larger.

## The Odd Orders

**Proposition.** At odd $n$ the slot $\tfrac{n-1}{2}$ is an integer and is one of the summands; at $n=3$ the summands are $0,1,2$, the slot is $1$, and the module of dimension three is the carrier $V_1$.

*Proof.* $2j=n-1$ is even for odd $n$, so $j$ is an integer, and the summands $0,\dots,n-1$ contain $j$; the dimension $2j+1=n$ is odd, as the dimensions of the carriers are.

**Corollary.** At odd $n$ the module is a subspace of the algebra, namely one of its carriers; at even $n$ it is not, and it occurs only as a minimal left ideal.

*Proof.* A carrier is a subspace of the algebra, and at even $n$ its label is not an integer, so no carrier has the module's label.

**Corollary.** The distinction between the slot and the summand is a property of even order; at odd order the slot is a summand and the vocabulary collapses.

*Proof.* The two cases of the parity of $2j$.

**The reading.** The phrase "the module is not a subspace of the algebra" is true at even order and false at odd order; the article states it only where it holds.

## The Boundary

**Against the half-integer article.** That article follows the half-integer into the weights and the eigenvalues; this one fixes the slot as an object and compares the two rows. Both use the identity $2j=n-1$.

**Against the ideal.** At even $n$ the module is realised as a minimal left ideal $M_nP$, and the slot is the label of that ideal; the ideal is not a summand, and the summands are the carriers.

**Against the general order.** The statements are stated for $n=2$ and $n=4$; the extension is the identity $2j=n-1$ and the sum $\sum(2k+1)=n^{2}$.

## The Check of the Distinction

**The slot.** A slot is a position in the tensor square, that is a pair of weights whose difference is the weight of the slot; the slots are the $4\times4=16$ positions, and each carries a single matrix unit.

**The summand.** A summand is a carrier, and it collects the slots whose differences lie in the same weight string; the summand therefore groups several slots, and the grouping is the Clebsch–Gordan decomposition.

**The count.** The number of slots is sixteen and the number of summands is four; the number of slots in a summand is the square of the dimension of its label, and the squares $16,9,4,1$ are the multiplicities with which the labels appear in the tensor square, each label occurring as many times as its dimension.

## Summary

The slot of the row of order $n$ is $j=\tfrac{n-1}{2}$, and its three invariants are the dimension $2j+1=n$, the number $n$ of weights and the maximal weight $j$. The summands are the integers $0,\dots,n-1$, of total dimension $n^{2}$, which is the square of the module's dimension.

At $n=2$ the algebra is $M_2(\mathbb{C})$ with the summands $0,1$ of dimensions $1,3$ and the slot $\tfrac12$; at $n=4$ the algebra is $M_4(\mathbb{C})$ with the summands $0,1,2,3$ of dimensions $1,3,5,7$ and the slot $\tfrac32$. In both rows the slot is a half-integer and not a summand.

At odd order the slot is an integer and is a summand, and the module is a carrier; the distinction between slot and summand is a property of even order.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $j=\tfrac{n-1}{2}$ | the slot |
| $2j+1=n$ | the dimension of the module |
| $0,\dots,n-1$ | the summand labels |
| $n^{2}$ | the total dimension of the summands |

## Further Reading

- [Where the Half-Integers Go in $M_4(\mathbb{C})$](where-the-half-integers-go-in-m4c.html), for the half-integer.
- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the summands.
- [Why the Conjugation Labels Are Integer at $n=4$](why-the-conjugation-labels-are-integer-at-n-4.html), for the parity argument.
- [The Slot and the Summand](the-slot-and-the-summand.html), for the row at order two.
- [The Law of the Module and the Chain of Carriers](the-law-of-the-module-and-the-chain-of-carriers.html), for the general order.
