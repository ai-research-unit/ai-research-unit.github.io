# __The Spin Decomposition: Four Carriers and the Weight Multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$__

## Introduction

**The subject.** The sixteen weights of the Cartan generator on the operator space are the sixteen differences of the four weights of the module, and as a multiset they read $0$ four times, $\pm1$ three times, $\pm2$ twice and $\pm3$ once. The article computes the multiset, checks it twice, once by the differences and once by the carrier strings, and separates the multiplicity of a weight from the dimension of a carrier.

**The order of the article.** The differences and the multiset come first; the check by the carriers second. The meeting of the four carriers at weight zero follows, then the symmetry, and the two counts close the article.

**It assumes** *The Clebsch–Gordan Decomposition of the Operators*, *The Four Weights of the Module and the Half Angle* and *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*. **The row of the elements is** where the corresponding multiset has four entries, $\pm1$ and $0$ twice; here the doubled string gives sixteen.

**The result in one line.** The multiset of the sixteen weights is $0^{4},(\pm1)^{3},(\pm2)^{2},(\pm3)^{1}$, its multiplicities sum to sixteen, and each weight occurs once in every carrier whose label dominates it.

**Boundaries.** The decomposition into carriers is *The Clebsch–Gordan Decomposition of the Operators*; the action of the copy is *The Copy Acting on Sixteen Dimensions*; the squares of the module are *The Parity Rule*.

## The Differences

**Theorem.** The weights of the operator space are the sixteen differences $m-m'$ of the four weights of the module, and their multiplicities are
$$
0^{4},\quad(\pm1)^{3},\quad(\pm2)^{2},\quad(\pm3)^{1}.
$$

*Proof.* The weights of the tensor square are the sums of a weight and the negative of a weight, which is the difference of two weights of the module; counting the pairs that give each difference gives the multiplicities displayed.

**Corollary.** The multiplicities sum to $4+3+3+2+2+1+1=16$.

*Proof.* The count of the pairs, or the sum of the multiplicities.

**Corollary.** The weights are symmetric, and the multiplicity of a weight equals the multiplicity of its negative.

*Proof.* The differences are exchanged by the reflection of the string.

**The reading.** The multiset is computed from the module alone, by subtracting weights. This is the cheapest way to see the dimension sixteen: the sixteen differences are the sixteen coordinates of the operator space in the weight basis.

## The Check by the Carriers

**Theorem.** The same multiset is the union of the four carrier strings,
$$
V_3:3,2,1,0,-1,-2,-3;\quad V_2:2,1,0,-1,-2;\quad V_1:1,0,-1;\quad V_0:0,
$$
and the union reproduces the multiplicities.

*Proof.* Each carrier of label $k$ has the string from $k$ down to $-k$ in steps of one; the number of carriers whose string contains a weight $w$ is $4-|w|$ for $|w|\le3$, which gives $4,3,2,1$.

**Corollary.** The dimension check reads $7+5+3+1=16$ on one side and $4+6+4+2=16$ on the other.

*Proof.* The sum of the carrier dimensions, and the sum of the multiplicities counted once per occurrence.

**Corollary.** A weight of large modulus occurs in few carriers, and the extreme weights occur once each.

*Proof.* The count $4-|w|$ decreases with the modulus.

**The reading.** The two counts are the same count: the multiplicity of a weight is the number of carriers containing it, and the dimension of a carrier is the number of weights it contains. The multiset and the decomposition are two readings of one table.

## The Four Carriers at Weight Zero

**Proposition.** Weight zero occurs once in each of the four carriers, so the kernel of the Cartan generator meets all four.

*Proof.* Every carrier of integer label $k$ has the string from $k$ to $-k$, which contains zero; the carrier of label zero is the zero weight alone.

**Corollary.** The intersection of the kernel with the operator space is four-dimensional, and it is the direct sum of four lines.

*Proof.* One line from each carrier, and the carriers are independent.

**Corollary.** No carrier is contained in the kernel, and no carrier avoids it.

*Proof.* Each carrier has one zero weight and at least one nonzero weight.

**The reading.** The kernel of the Cartan generator is the diagonal of the four carriers, one line each. This is why a spectral statement about the operators has to say which carrier it refers to: the zero weight alone does not distinguish them.

## The Symmetry

**Theorem.** The weight multiset is symmetric under the reflection $w\mapsto-w$, and the reflection is realised by an operator of the space that exchanges the two factors of the tensor square.

*Proof.* The multiplicities are symmetric by the corollary on differences; the exchange of the two factors of $V\otimes V$ carries a difference $m-m'$ to its negative.

**Corollary.** The reflection commutes with the Cartan generator up to sign, and it is an involution of the sixteen.

*Proof.* The exchange of factors has the stated effect on the weights.

**Corollary.** The trace of the Cartan generator on the operator space is zero.

*Proof.* The weights come in opposite pairs, so their sum vanishes.

**The reading.** The symmetry of the multiset is a symmetry of the space and not only of the list. It is the reflection that makes the module self-dual, read on the operator space.

## The Two Counts

**Proposition.** The multiplicity of a weight and the dimension of a carrier are different numbers, and neither determines the other.

*Proof.* The weight three has multiplicity one and lies in a carrier of dimension seven; the weight zero has multiplicity four and lies in four carriers, of dimensions seven, five, three and one.

**Corollary.** The dimension sixteen is the sum of the carrier dimensions and also the sum of the multiplicities of the weights, but the two sums are over different index sets.

*Proof.* The carrier dimensions sum over four labels, the multiplicities over seven weights.

**Corollary.** A statement about the number of coordinates of a given weight is a statement about the multiset, and a statement about the size of an invariant subspace is a statement about a carrier.

*Proof.* The two numbers count different things.

**The reading.** The multiset answers how many coordinates carry a given weight; the decomposition answers which invariant subspaces exist. Both are needed, and the two must be kept apart, since a reader who confuses them will assign the dimension seven to the weight zero.

## The Staircase

**Definition.** The **multiplicity** of a weight is the number of independent vectors of the space with that weight; the **staircase** is the graph of the multiplicity against the weight.

**Proposition.** The multiplicities rise from one at the top weight to four at weight zero and fall back symmetrically, and the rise is by one at each step.

*Proof.* The top weight $3$ occurs once, in the carrier of label three. At weight $2$ the vectors are the lowering of the top vector and the highest weight vector of the carrier of label two, so there are two. At weight $1$ there are the second lowering of the top vector, the lowering of the label-two vector and the top vector of the carrier of label one, so three. At weight zero there are one more, the top vector of the label-zero carrier, so four; and the argument mirrors below zero because the weights are symmetric.

**Corollary.** The total is $1+2+3+4+3+2+1=16$, in agreement with the multiset $0^{4},(\pm1)^{3},(\pm2)^{2},(\pm3)^{1}$.

*Proof.* The staircase, summed.

**Corollary.** A carrier of label $k$ contributes one vector to each weight from $k$ down to $-k$, so the multiplicity of a weight is the number of carriers whose label dominates it.

*Proof.* The weights of the carrier of label $k$ are $k,k-1,\dots,-k$, one vector each.

**The reading.** The multiset is not a coincidence of dimensions but a staircase, and the staircase is the statement that the four carriers are nested by their labels. Anyone who knows the multiplicities can redraw the carriers, and anyone who knows the carriers can read off the multiplicities.

## The Two Bases and the Count

**The products.** The sixteen products $\lvert\tfrac32,m_1\rangle\otimes\lvert\tfrac32,m_2\rangle$ are a basis of the tensor square, and the weight of a product is the sum $m_1+m_2$.

**The coupled states.** The sixteen states $\lvert J,M\rangle$ are the second basis, one string of length $2J+1$ in each carrier.

**Proposition.** At each weight $M$ the number of products equals the number of coupled states, $4-\lvert M\rvert$.

*Proof.* The products of weight $M$ are the pairs with $m_1+m_2=M$, of which there are $4-\lvert M\rvert$; the coupled states of weight $M$ are those of the labels $J\ge\lvert M\rvert$, also $4-\lvert M\rvert$ in number.

**The reading.** The multiset $0^{4},\pm1^{3},\pm2^{2},\pm3^{1}$ is that count read at every weight. The staircase of this article is the equality of two bases read weight by weight, and the four carriers of the decomposition are the four strings of the second basis.

## Further Reading

- [The Clebsch–Gordan Decomposition of the Operators](the-clebsch-gordan-decomposition-of-the-operators.html), for the four carriers.
- [The Four Weights of the Module and the Half Angle](the-four-weights-of-the-module-and-the-half-angle.html), for the four weights of the module.
- [The Copy Acting on Sixteen Dimensions](the-copy-acting-on-sixteen-dimensions.html), for the action that produces the multiset.
- [The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$](the-intersection-table-of-the-carriers-with-the-two-halves.html), for the same carriers against the two squares.
