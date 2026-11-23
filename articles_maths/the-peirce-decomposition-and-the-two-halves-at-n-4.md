# __The Peirce Decomposition and the Two Halves at $n=4$__

## Introduction

**Each Peirce space of $M_4(\mathbb{C})$ at a Hermitian idempotent is invariant under the transpose, so each splits into a symmetric and an antisymmetric part; the six pieces of the split carry the trace pairing with the inertias $(3,1)$, $(3,1)$ and $(4,4)$ at rank two, and these add up to the inertia $(10,6)$ of the whole algebra.**

The article writes the associative Peirce decomposition at a Hermitian idempotent, proves that the transpose preserves each Peirce space, computes the two halves of each space for every rank, works the case of rank two explicitly, computes the trace pairing on each of the six pieces, checks that the inertias add to $(10,6)$, and concludes that the Peirce decomposition and the symmetric decomposition are transverse: neither refines the other.

It assumes *The Two Halves as Orthogonal Complements at $n=4$* and *The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$*. The Jordan version is *The Peirce Decomposition of $\operatorname{Sym}_4$ as a Jordan Algebra*; the corner recursion is *The Peirce Decomposition and the Corner Recursion of $M_4(\mathbb{C})$*.

## The Peirce Spaces of the Whole Algebra

**Definition.** For an idempotent $E$ the **associative Peirce spaces** are
$$
V_{11}=EME,\quad V_{00}=(1-E)M(1-E),\quad V_{10}=EM(1-E),\quad V_{01}=(1-E)ME.
$$

**Theorem.** $M_4=V_{11}\oplus V_{10}\oplus V_{01}\oplus V_{00}$, with the dimensions $k^{2}$, $k(4-k)$, $k(4-k)$ and $(4-k)^{2}$ at rank $k$, summing to $16$.

**Proof.** In blocks at $E=\operatorname{diag}(1,\dots,1,0,\dots,0)$ the four spaces are the four blocks of the block decomposition, and a block of size $k\times(4-k)$ has $k(4-k)$ entries.

**Corollary.** At $k=2$ the four dimensions are $4,4,4,4$; at $k=1$ they are $1,3,3,9$.

**Proof.** Substitution.

**The multiplication table.** $V_{ij}V_{kl}\subseteq\delta_{jk}V_{il}$, and all the products not of that form vanish.

**Proof.** $EME\cdot EME\subseteq EME$ because $E^{2}=E$, and $EME\cdot EM(1-E)\subseteq EM(1-E)$ for the same reason; a product carrying a wrong pair of adjacent idempotents vanishes because $E(1-E)=0$.

**Corollary.** The two mixed spaces $V_{10}$ and $V_{01}$ are one-sided ideals in the Peirce algebra, and their sum is the space on which $E$ acts by different eigenvalues on the left and on the right.

**Proof.** $V_{10}=EM(1-E)$ is annihilated on the right by $E$ and on the left by $1-E$.

## Transpose Invariance and the Split

**Proposition.** For a Hermitian idempotent $E$ the transpose preserves each Peirce space: $V_{ij}^{\mathsf T}=V_{ji}$.

**Proof.** $E^{\mathsf T}=E$ because $E$ is symmetric, so $(EME)^{\mathsf T}=EME$ and $(EM(1-E))^{\mathsf T}=(1-E)ME$.

**Corollary.** $V_{11}$ and $V_{00}$ are transpose-invariant, and the transpose swaps $V_{10}$ and $V_{01}$.

**Proof.** The proposition with $i=j$ and with $i\neq j$.

**Definition.** On a transpose-invariant space $W$ the **symmetric part** is $W^{+}=\{X\in W:X^{\mathsf T}=X\}$ and the **antisymmetric part** is $W^{-}=\{X\in W:X^{\mathsf T}=-X\}$.

**Theorem.** $V_{11}=V_{11}^{+}\oplus V_{11}^{-}$ with the dimensions $\tfrac{k(k+1)}{2}$ and $\tfrac{k(k-1)}{2}$; the same for $V_{00}$ with $4-k$ in place of $k$; and $V_{10}\oplus V_{01}$ splits into the two spaces
$$
W^{+}=\{(B,B^{\mathsf T})\},\qquad W^{-}=\{(B,-B^{\mathsf T})\},
$$
each of dimension $k(4-k)$.

**Proof.** The first two are the symmetric and antisymmetric matrices of the size, whose dimensions are the counts of the entries on and off the diagonal. For the mixed space an element is a pair $(B,C)$ with $B\in V_{10}$ and $C\in V_{01}$, and the transpose sends it to $(C^{\mathsf T},B^{\mathsf T})$, so the fixed pairs are those with $C=B^{\mathsf T}$ and the anti-fixed pairs those with $C=-B^{\mathsf T}$, each determined freely by $B$.

**Corollary.** Each Peirce space is the direct sum of a symmetric and an antisymmetric space, and the two halves of the algebra are the sums of the six pieces.

**Proof.** Sum the splits over the four Peirce spaces.

## The Counts at Rank $k$

**Theorem.** At rank $k$ the symmetric part has dimension
$$
\frac{k(k+1)}{2}+\frac{(4-k)(5-k)}{2}+k(4-k)=10,
$$
and the antisymmetric part has dimension
$$
\frac{k(k-1)}{2}+\frac{(4-k)(3-k)}{2}+k(4-k)=6.
$$

**Proof.** Sum the dimensions of the theorem above and use the identity for the first and the corresponding one for the second.

**Corollary.** The three ranks give
$$
k=1:\ 1+6+3=10\ \text{and}\ 0+3+3=6,\qquad k=2:\ 3+3+4=10\ \text{and}\ 1+1+4=6,
$$
and $k=3$ is the mirror of $k=1$.

**Proof.** Substitution.

**The reading.** The symmetric half is spread over all three Peirce spaces, so no Peirce space is contained in one half; the antisymmetric half is likewise spread, and at rank two it has one dimension in each corner and four in the mixed space.

**Proof.** The counts above are all nonzero at $k=2$.

## The Case of Rank Two, Worked

**Proposition.** At $E=\operatorname{diag}(1,1,0,0)$ the decomposition is
$$
M_4=M_2\oplus M_2\oplus M_{2\times2}\oplus M_{2\times2},
$$
of dimensions $4,4,4,4$, and each of the four pieces splits as $3+1$, $3+1$, $4+0$ and $4+0$ for the transpose.

**Proof.** The corners are two copies of $M_2$, each splitting into $\operatorname{Sym}_2$ of dimension $3$ and $\operatorname{Skew}_2$ of dimension $1$; the mixed space of dimension $8$ splits into the pairs $(B,B^{\mathsf T})$ and $(B,-B^{\mathsf T})$, each of dimension $4$ and each entirely symmetric or entirely antisymmetric.

**Corollary.** The symmetric half of dimension $10$ splits as $\operatorname{Sym}_2\oplus\operatorname{Sym}_2\oplus W^{+}$ with the dimensions $3+3+4$, and the antisymmetric half as $\operatorname{Skew}_2\oplus\operatorname{Skew}_2\oplus W^{-}$ with the dimensions $1+1+4$.

**Proof.** Sum the pieces of each parity.

**The explicit mixed split.** With $B=E_{13}+2E_{24}$ the symmetric element is $(B,B^{\mathsf T})$ and the antisymmetric element is $(B,-B^{\mathsf T})$, and the two are independent and span a two-dimensional piece of the mixed space.

**Proof.** The two pairs differ in the sign of the second block.

**What the split is not.** The mixed symmetric space $W^{+}$ is not the symmetric half of the corner, and the mixed antisymmetric space $W^{-}$ is not the antisymmetric half of anything: both are copies of the rectangular block $M_{2\times2}$.

**Proof.** $W^{\pm}$ is parametrised by an arbitrary $2\times2$ matrix $B$, with no symmetry condition on $B$ itself.

## The Trace Pairing on Each Piece

**Theorem.** The trace pairing is diagonal with respect to the Peirce decomposition and the split:
$$
\beta(V_{11},V_{10}\oplus V_{01}\oplus V_{00})=0,\qquad \beta(V_{10},V_{01})=2\operatorname{tr}(BC'),
$$
and on $V_{11}$ and $V_{00}$ it is the trace pairing of the corner.

**Proof.** The trace of a block matrix with only off-diagonal blocks in the product is zero unless the blocks match, which gives the vanishing; for an element $(B,C)$ and an element $(B',C')$ of the mixed space, the product is $\operatorname{diag}(BC',CB')$ and its trace is $2\operatorname{tr}(BC')$. On the corner the product of two elements of $V_{11}$ is again in $V_{11}$ and its trace is the corner trace.

**Corollary.** At rank two the inertias on the corner, the complement and the mixed space are $(3,1)$, $(3,1)$ and $(4,4)$, and they add to $(10,6)$.

**Proof.** On the corner the form is the trace pairing of $M_2$, of inertia $(3,1)$; on the mixed space it is $2\operatorname{tr}(BC')$, positive definite on $W^{+}$ and negative definite on $W^{-}$, hence neutral of type $(4,4)$.

**Corollary.** The Peirce decomposition diagonalises the trace pairing into three blocks whose inertias add to the inertia of the whole algebra, and the mixed block is the hyperbolic one.

**Proof.** The inertia of a direct sum is the sum of the inertias.

**The general rank.** At rank $k$ the three inertias are
$$
\Bigl(\tfrac{k(k+1)}{2},\tfrac{k(k-1)}{2}\Bigr),\qquad \bigl(k(4-k),\,k(4-k)\bigr),\qquad \Bigl(\tfrac{(4-k)(5-k)}{2},\tfrac{(4-k)(3-k)}{2}\Bigr),
$$
and the first components add to $10$ while the second add to $6$.

**Proof.** The three computations of the theorem, with the mixed space split into its two definite halves.

## The Two Decompositions Are Transverse

**Proposition.** Neither decomposition refines the other: $V_{11}$ is not contained in $\operatorname{Sym}_4$ or in $\operatorname{Skew}_4$, and $\operatorname{Sym}_4$ is not contained in a Peirce space.

**Proof.** $V_{11}$ contains both a symmetric and an antisymmetric element, and $\operatorname{Sym}_4$ contains elements with entries in every block.

**Corollary.** The joint refinement of the two decompositions is the six-piece decomposition of this article, and it is strictly finer than either.

**Proof.** Each piece is the intersection of a Peirce space with a half, and the intersections are proper subspaces of both.

**The two planes.** At rank two the corners contribute the two copies of $\operatorname{Sym}_2$ and the two copies of $\operatorname{Skew}_2$, and the mixed space contributes two copies of $M_{2\times2}$; the six pieces are the atoms of the joint decomposition.

**Proof.** The counts $3,1,3,1,4,4$ summing to $16$.

**Corollary.** The joint decomposition has six pieces and the two separate ones have four and two, and the refinement is the reading of the algebra in the Peirce frame and the transpose frame at once.

**Proof.** $6=4+2$ is a coincidence of counts and not a refinement relation; the six pieces are the nonzero intersections.

**The moral.** The Peirce decomposition is adapted to the idempotent and the symmetric decomposition is adapted to the involution; the two structures are independent, and the intersection pattern is the joint refinement, whose inertias add to the inertia of the algebra in either grouping.

**Proof.** The two decompositions are defined by different operators, $L_E$ and the transpose, which do not commute in general.

## Summary

Each associative Peirce space at a Hermitian idempotent is invariant under the transpose, and the two mixed spaces are swapped by it. So every Peirce space splits into a symmetric and an antisymmetric part, and at rank $k$ the six pieces have dimensions $\tfrac{k(k+1)}{2}$, $\tfrac{k(k-1)}{2}$, $k(4-k)$, $k(4-k)$, $\tfrac{(4-k)(5-k)}{2}$ and $\tfrac{(4-k)(3-k)}{2}$.

At rank two the pieces are $3,1,4,4,3,1$. The trace pairing is diagonal with respect to the Peirce decomposition: it restricts to the corner form of inertia $(3,1)$, to the complement form of inertia $(3,1)$, and to the mixed form $2\operatorname{tr}(BC')$, positive on $W^{+}$ and negative on $W^{-}$, hence of type $(4,4)$. The three inertias add to $(10,6)$.

The two decompositions are transverse. Neither refines the other, their joint refinement has six pieces, and the Peirce decomposition is adapted to the idempotent while the symmetric decomposition is adapted to the involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_{11},V_{10},V_{01},V_{00}$ | the four associative Peirce spaces |
| $V_{11}^{+},V_{11}^{-}$ | their symmetric and antisymmetric parts |
| $W^{+},W^{-}$ | the symmetric and antisymmetric halves of the mixed space |
| $\beta(X,Y)=\operatorname{tr}(XY)$ | the trace pairing |
| $(3,1),(3,1),(4,4)$ | the inertias at rank two |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Peirce decomposition and its relation to the involution.
- [The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m4c.html), for the inertia $(10,6)$ that the pieces add to.
- [The Peirce Decomposition of $\operatorname{Sym}_4$ as a Jordan Algebra](the-peirce-decomposition-of-sym-4-as-a-jordan-algebra.html), for the Jordan version of the split.
- [The Two Halves as Orthogonal Complements at $n=4$](the-two-halves-as-orthogonal-complements-at-n-4.html), for the transpose and the orthogonality.
- [The Peirce Decomposition and the Corner Recursion of $M_4(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-m4c.html), for the recursion that the corner starts.
