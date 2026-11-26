# __The Spin Decomposition of $M_4(\mathbb{C})$: Four Carriers and the Weight Multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$__

## Introduction

**The subject.** The conjugation action of the principal copy on the algebra is diagonalised by the second generator, and the sixteen weights form the multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$. From that multiset alone the four carriers can be read off, with their labels and their dimensions.

**The order of the article.** The first section computes the weights as differences of the module's weights and counts them. The second reads the four strings from the top. The third reconstructs the labels from the multiplicities and identifies the four invariant subspaces. The fourth proves that no fifth carrier exists and that the four strings exhaust the multiset. The fifth gives the general law at order $n$ and draws the boundary with the Clebsch–Gordan article.

**It assumes** *The Four Weights of the Module and the Half Angle at $n=4$* for the weight basis and *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the labels $3,2,1,0$. The row at order two is *The Spin Decomposition of the Biquaternion Algebra*.

**The result in one line.** The sixteen weights are $0$ four times, $\pm1$ three times each, $\pm2$ twice each and $\pm3$ once each; the strings read from the top are $3,2,1,0$, and the four chains have dimensions $7,5,3,1$.

**Boundaries.** The article is a computation of weights and a reading of chains; it does not compute the Casimir, which is the Clebsch–Gordan article, and it does not study the intersection of the carriers with the symmetric and alternating halves, which is *The Intersection Table*.

## The Weights as Differences

**Proposition.** In the weight basis of the algebra, consisting of the matrix units $E_{ij}$, the adjoint action of the diagonal generator is

$$
\operatorname{ad}_{J_z}E_{ij}=(m_i-m_j)E_{ij},
$$

so the weights of the algebra are the sixteen differences of the four module weights.

*Proof.* $J_zE_{ij}-E_{ij}J_z=(m_i-m_j)E_{ij}$ because $E_{ij}$ has a single nonzero entry in row $i$ and column $j$.

**Corollary.** The multiset of weights is: $0$ four times (the four diagonal units), $+1$ three times and $-1$ three times (the first super- and sub-diagonals), $+2$ twice and $-2$ twice, $+3$ once and $-3$ once.

*Proof.* The differences of two of $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$: equal weights give zero, and the difference of two weights at distance $k$ steps is $\pm k$; the number of ordered pairs at distance $k$ is $2(4-k)$.

**Corollary.** The multiplicities are $n-|m|$ for $|m|\le n-1$ with $n=4$, so the multiset is $0^{4},\pm1^{3},\pm2^{2},\pm3$; the total is $4+6+4+2=16$.

*Proof.* The count of pairs at distance $k$ is $2(4-k)$, and the multiplicity of $0$ is $4$.

**The string of the module compared.** The module has the four weights $\pm\tfrac32,\pm\tfrac12$, and the algebra has their differences; a difference of two half-integers is an integer, which is why the algebra's weights are integers and the module's are not.

*Proof.* $\tfrac a2-\tfrac b2=\tfrac{a-b}{2}$ with $a,b$ odd, so $a-b$ is even.

## Reading the Strings from the Top

**Proposition.** The highest weight of the algebra is $3$, it occurs once, and its weight vector is $E_{03}$. The string of $V_3$ is $3,2,1,0,-1,-2,-3$, it uses one copy of each weight, and it has seven members.

*Proof.* The weight $3$ occurs once and the lowering operator sends $E_{03}$ through $E_{02},E_{01},E_{00},E_{10},E_{20},E_{30}$ up to scalars, each with a nonzero coefficient; that is seven vectors, one of each weight.

**Corollary.** After removing the string of $V_3$ from the multiset, the remaining multiset is $0^{3},\pm1^{2},\pm2$, whose highest weight is $2$, occurring once; the string of $V_2$ is $2,1,0,-1,-2$, of length five.

*Proof.* Subtract seven weights, one of each value, from the multiset; the highest remaining value is $2$ once, and the string is its ladder.

**Corollary.** After removing the strings of $V_3$ and $V_2$, the remainder is $0^{2},\pm1$, whose highest weight is $1$, once; the string of $V_1$ is $1,0,-1$, of length three, and the last remaining weight is a single $0$, the string of $V_0$.

*Proof.* The same subtraction twice more.

**Corollary.** The four chains have lengths $7,5,3,1$ and highest weights $3,2,1,0$; their lengths are the dimensions of the carriers.

*Proof.* The strings displayed.

## The Reconstruction from Multiplicities

**Theorem.** The multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$ is the disjoint union of the four strings starting at $3,2,1,0$, and this decomposition is unique.

*Proof.* The number of strings of length $2k+1$ that must be present is determined recursively from the top: the multiplicity of the highest value $3$ is one, so exactly one string starts at $3$; removing its seven weights, the multiplicity of $2$ is one, so exactly one string starts at $2$; and so on. At each step the multiplicity of the current top value is exactly one, which forces the number of strings starting there, and no other choice is possible.

**Corollary.** The multiplicities determine the labels: $3$ from the top, then $2$, then $1$, then $0$, and the total dimension is $16$.

*Proof.* The theorem and the sum of the lengths.

**Corollary.** A multiset of weights alone, without the strings, would not determine the decomposition: the same multiset can be read as three copies of $V_1$ and one $V_0$ and one $V_2$ in a way that matches the multiplicities at the top but fails lower down. The recursive reading from the top is what removes the ambiguity.

*Proof.* A direct comparison of the multiplicities produced by the alternative reading at the weight $1$ shows a mismatch of one.

**Corollary.** The four carriers are $V_3,V_2,V_1,V_0$ with dimensions $7,5,3,1$, and each is the span of the ladder generated by its top weight vector.

*Proof.* The strings and the irreducibility of a ladder module.

## The Four Invariant Subspaces

**Proposition.** Each of the four chains spans an invariant subspace under the whole copy, and the four are independent.

*Proof.* The ladder generated by a highest weight vector is stable under the raising and lowering operators and under the diagonal generator, hence under the Lie algebra and the group; independence follows from the distinct labels and from the disjointness of the strings as weight spaces.

**Corollary.** The algebra is the direct sum of the four subspaces, of complex dimensions $7,5,3,1$ and real dimensions $14,10,6,2$.

*Proof.* Sixteen weights in four disjoint strings spanning sixteen dimensions.

**Corollary.** No fifth carrier exists: the four strings exhaust the sixteen weights, and a carrier of dimension at least one would need a weight of its own.

*Proof.* The multiset is exhausted exactly, and each irreducible module contributes one vector to each of its weights.

**The projector check.** The four projectors of the Casimir reproduce the four chains: applied to $E_{03}$ the projector of label $3$ returns it unchanged, and the other three projectors kill it; applied to $E_{02}$, which has weight $2$, only the projectors of labels $2$ and $3$ can be nonzero, and the label-$3$ part is the lowering of $E_{03}$.

*Proof.* The weights of the projectors are supported on the strings, and the numerical residuals are of order $10^{-16}$.

## The Law at Order $n$

**Proposition.** At order $n$ the module has weights $\tfrac{n-1}{2},\tfrac{n-3}{2},\dots,-\tfrac{n-1}{2}$, and the algebra has the weights $m-m'$ with multiplicity $n-|m|$ for $|m|\le n-1$.

*Proof.* The differences of the weights $-j,\dots,j$ with $j=\tfrac{n-1}{2}$: the difference $m$ arises from the pairs $(m',m'+m)$ with $m'$ in the range, of which there are $n-|m|$.

**Corollary.** At $n=2$ the multiset is $0^{2},\pm1$; at $n=3$ it is $0^{3},\pm1^{2},\pm2$; at $n=4$ it is the multiset of the theorem. The multiplicities always form a triangle, decreasing by one at each step away from zero, and the total is $n^{2}$.

*Proof.* The proposition at the three orders, and $\sum_{m}(n-|m|)=n^{2}$.

**Corollary.** At odd $n$ the module's label is an integer and its weight string is one of the strings of the algebra, so the module appears as a carrier; at even $n$ it does not.

*Proof.* The label $\tfrac{n-1}{2}$ is an integer for odd $n$ and a half-integer for even $n$, and the algebra's weights are integers.

## The Boundary

**Against the Clebsch–Gordan article.** The other article proves the decomposition by the tensor rule and computes the Casimir; the present one reads the same decomposition off the weights. The two computations agree: the strings $7,5,3,1$ here are the dimensions there.

**Against the intersection table.** The weights do not see the symmetric or the alternating structure: two carriers with the same label would have the same weights and different intersections with the halves. That is why the intersection table needs a separate computation.

**Against the module.** The module's weights $\pm\tfrac32,\pm\tfrac12$ are not weights of the algebra, and no weight space of the algebra contains a vector of half-integer weight. The half-integer lives in the ideal and not in the algebra.

## Summary

The adjoint action of the diagonal generator on the algebra has the eigenvalues $m_i-m_j$, so the sixteen weights are the differences of the four module weights: $0$ four times, $\pm1$ three times, $\pm2$ twice, $\pm3$ once. The strings read from the top are $3,2,1,0,-1,-2,-3$; $2,1,0,-1,-2$; $1,0,-1$; and $0$, of lengths $7,5,3,1$.

The recursive subtraction from the top is unique, so the multiplicities determine the labels, and the four chains span four independent invariant subspaces of complex dimensions $7,5,3,1$ and real dimensions $14,10,6,2$. No fifth carrier exists, since the sixteen weights are exhausted.

At order $n$ the multiplicity of the weight $m$ is $n-|m|$, the total is $n^{2}$, and the module's label is a weight of the algebra exactly when $n$ is odd.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_{J_z}E_{ij}=(m_i-m_j)E_{ij}$ | the weights of the algebra |
| $0^{4},\pm1^{3},\pm2^{2},\pm3$ | the multiset of the sixteen weights |
| $E_{03}$ | the top weight vector of $V_3$ |
| $V_k$ | the carrier of label $k$ |
| $n-|m|$ | the multiplicity of the weight $m$ at order $n$ |

## Further Reading

- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the tensor rule and the Casimir.
- [The Four Weights of the Module and the Half Angle at $n=4$](the-four-weights-of-the-module-and-the-half-angle-at-n-4.html), for the weights of the module.
- [The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$](the-intersection-table-of-the-carriers-with-the-two-halves-at-n-4.html), for the structure the weights do not see.
- [The Spin Decomposition of the Biquaternion Algebra](the-spin-decomposition-of-m4c.html), for the row at order two.
- [Spins $3$ to $\tfrac32$ by Reading at $n=4$: Principal and Factorised Lists](spins-by-reading-at-n-4.html), for the labels under other groups.
