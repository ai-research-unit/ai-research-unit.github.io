# __The Spectral Sectors and the Operators of $M_n(\mathbb{C})$__

## Introduction

**The question.** The four sectors of the previous article use one spectral predicate, "the eigenvalues are distinct". Replacing it by the full multiplicity pattern refines the partition. What are the strata, their dimensions, and which operators preserve them?

**The answer in one line.** For each partition $\mu$ of $n$ there is a stratum $S_\mu$ of matrices whose eigenvalue multiplicities are the parts of $\mu$, of dimension
$$
\dim S_\mu=n^2-\sum_i\mu_i^2+k,
$$
where $k$ is the number of parts; the regular stratum $\mu=(1,\dots,1)$ is Zariski open, and conjugation preserves every stratum.

**Why the article is needed.** The four-sector picture is the coarsest spectral partition. It is enough for the biquaternion algebra, where $n=2$ and there are two multiplicity patterns. It is not enough for $n=4$, where there are five patterns and the strata have five different dimensions. An article that speaks of "the spectrally degenerate set" as one object hides the five-fold refinement.

**Boundaries.** The coarse four sectors are *The Operators on the Four Sectors of $M_n(\mathbb{C})$*; the discriminant and the characteristic polynomial are *The Matrix Algebra $M_n(\mathbb{C})$*; the biquaternion stratification is *Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra*.

**Conventions.** A partition $\mu=(\mu_1\ge\dots\ge\mu_k)$ of $n$ records the multiplicities of the distinct eigenvalues; $k$ is the number of distinct eigenvalues. $\Delta$ is the discriminant of the previous article.

## The Discriminant

**Proposition.** $\Delta$ is homogeneous of degree $n(n-1)$, invariant under conjugation and under the transpose, and vanishes exactly on the union of the strata with $k<n$.

*Proof.* Each difference $\lambda_i-\lambda_j$ is homogeneous of degree one, and there are $n(n-1)/2$ differences, so $\Delta$ has degree $n(n-1)$. Conjugation does not change the eigenvalues, and the transpose does not either. The vanishing is the definition. $\square$

**The values.** The degree is $2,6,12,20$ for $n=2,3,4,5$.

**What the discriminant does not see.** $\Delta$ vanishes on every stratum with a repeated eigenvalue and does not distinguish them. It is one polynomial, and its zero locus is one hypersurface, which is the union of all the degenerate strata.

**The unreduced nature.** $\Delta$ is a square in the eigenvalues but not in the entries: for $n=2$ it is $\operatorname{tr}(X)^2-4\det X$, which is not the square of a polynomial in the entries. This is why the discriminant hypersurface carries the whole degenerate set and not just the deepest stratum.

## The Strata

**Theorem.** The sets $S_\mu$, over the partitions of $n$, form a partition of $M_n$. Each $S_\mu$ is a locally closed, irreducible, smooth subvariety of dimension $n^2-\sum_i\mu_i^2+k$.

*Proof.* The centraliser of a matrix with multiplicities $\mu$ has dimension $\sum_i\mu_i^2$ when the matrix is generic in its similarity class, so the similarity class has dimension $n^2-\sum_i\mu_i^2$. The eigenvalues are $k$ free parameters, and the stratum is the union of the classes over the eigenvalues, so the dimension is $n^2-\sum_i\mu_i^2+k$. The stratum is the image of the map (eigenvalues, frame, nilpotent part) and is smooth at the points where the frame is chosen generically. $\square$

**The table at $n=4$.**

| $\mu$ | $k$ | $\sum\mu_i^2$ | $\dim S_\mu$ | description |
|---|---|---|---|---|
| $1+1+1+1$ | $4$ | $4$ | $16$ | four distinct eigenvalues |
| $2+1+1$ | $3$ | $6$ | $13$ | one double eigenvalue |
| $2+2$ | $2$ | $8$ | $10$ | two double eigenvalues |
| $3+1$ | $2$ | $10$ | $8$ | one triple eigenvalue |
| $4$ | $1$ | $16$ | $1$ | scalar |

**The sum check.** The five dimensions are different, and the largest is the open stratum. There are five partitions of four, so the four-sector picture, with its two spectral classes, is a coarsening of a stratification with five strata.

**The table at $n=3$.** $1+1+1$: $9$; $2+1$: $6$; $3$: $1$. Three strata.

**The table at $n=5$.** $1^5$: $25$; $2+1+1+1$: $22$; $2+2+1$: $19$; $3+1+1$: $17$; $3+2$: $14$; $4+1$: $10$; $5$: $1$. Seven strata, one per partition of five.

## The Zariski Topology

**Proposition.** The regular stratum $S_{(1,\dots,1)}$ is Zariski open and dense, and its complement is the hypersurface $\Delta=0$.

*Proof.* The complement is the zero locus of the single polynomial $\Delta$, which is not identically zero. $\square$

**The frontier condition.** The closure of $S_\mu$ is the union of the strata whose partition refines $\mu$, that is, the strata obtained by splitting the parts of $\mu$.

*Proof.* Coalescing eigenvalues is a closed condition, and splitting them is an open condition within the closure, so the closure contains exactly the coarsenings. $\square$

**The consequence.** The stratification is a stratification in the sense of Whitney: the closures are unions of strata and the frontier condition holds. It is not the stratification by rank, which is a different partition.

## The Operators

**The inner automorphisms.** $T_{g,g^{-1}}$ preserves every stratum exactly, because conjugation preserves the multiset of eigenvalues including multiplicities.

**The transpose.** $F$ preserves every stratum, since the characteristic polynomial of $X^{\mathsf T}$ is that of $X$.

**The one-sided family.** $L_A$ preserves the stratification only when $A$ is a scalar, and otherwise it does not map strata to strata in a controlled way: the multiplicity pattern of $AX$ is not determined by those of $A$ and $X$.

*Proof.* $\operatorname{rank}(AX)\le\operatorname{rank}A$, and the eigenvalues of $AX$ are not functions of those of $A$ and $X$. The example $X=\operatorname{diag}(1,2)$, $A=\operatorname{diag}(1,\tfrac12)$ sends the regular stratum to the scalar stratum. $\square$

**The two-sided family.** $T_{A,B}$ has the same freedom, with $\operatorname{rank}(AXB)\le\min(\operatorname{rank}A,\operatorname{rank}B)$ and no control over the multiplicities.

**The group preserving everything.** The group generated by the inner automorphisms and the transpose preserves every stratum, since these are the automorphisms and the anti-automorphism of the algebra. No larger natural group does.

## The Comparison with the Biquaternion Algebra

**The two strata.** At $n=2$ the partitions are $1+1$ and $2$, with dimensions $4$ and $1$. The biquaternion algebra, being commutative and reduced, has the strata "distinct component values" and "equal component values", of dimensions $2$ and $1$.

**The extra structure.** In $M_2$ the stratum $\mu=(2)$ is the discriminant hypersurface itself: it consists of the matrices with a single eigenvalue, whose scalar part is free and whose nilpotent part is free, so it has dimension $3$. The scalar line is the sub-stratum on which the nilpotent part vanishes.

**The honest statement.** The multiplicity pattern is the same datum in both algebras; the dimensions differ because $M_2$ has nilpotents and the reduced algebra does not. The refinement by pattern survives; the dimensions do not transfer.

## The Finite Check

The homogeneity and the two invariances were checked at $n=2,3,4,5$: $\Delta(tX)/\Delta(X)/t^{n(n-1)}=1$ to $10^{-15}$ for $t=1.7$, $\Delta(X^{\mathsf T})=\Delta(X)$ to $2\times10^{-14}$, and $\Delta(gXg^{-1})=\Delta(X)$ to $10^{-13}$.

The orbit dimensions were computed from the rank of the conjugation map: at $n=3$ the ranks are $6,4,0$ for the patterns $1+1+1$, $2+1$, $3$, matching $n^2-\sum\mu_i^2=6,4,0$; at $n=4$ the ranks are $12,10,0$ for $1+1+1+1$, $2+1+1$, $4$, matching $12,10,0$. Adding $k$ gives the stratum dimensions in the table.

The two examples were computed: $\operatorname{diag}(1,2)$ lies in the regular stratum and $\operatorname{diag}(1,1)=\operatorname{diag}(1,\tfrac12)\operatorname{diag}(1,2)$ lies in the scalar stratum, so $L_A$ crosses the stratification.

## The Poset

**The refinement order.** Write $\mu\preceq\nu$ when $\mu$ is obtained from $\nu$ by merging parts. The closure of $S_\mu$ is $\bigcup_{\nu\preceq\mu}S_\nu$, and the relation is a partial order with the regular partition at the bottom and the single-part partition at the top.

**The table at $n=4$.** The regular partition $1+1+1+1$ is below all; $2+1+1$ is below $2+2$ and below $3+1$; $2+2$ and $3+1$ are both below $4$.

**The two chains.** The chain $1+1+1+1\prec2+1+1\prec3+1\prec4$ and the chain $1+1+1+1\prec2+1+1\prec2+2\prec4$ are the two maximal chains, and they meet at the top and the bottom.

**The reading.** The poset of partitions of $n$ is the poset of the spectral stratification, and it is not a chain for $n\ge4$. The four-sector picture collapses it to two levels, which is why the coarse partition cannot see the two chains.

**The incidence.** The codimension of $S_\mu$ is $n^{2}-\dim S_\mu=\sum_i\mu_i^{2}-k$, which grows as the parts merge. The frontier condition is the statement that the closure of $S_\mu$ is the union of the $S_\nu$ over the partitions $\nu$ that refine $\mu$.

## The Operators that Preserve the Discriminant

**The conjugations.** $X\mapsto gXg^{-1}$ preserve the characteristic polynomial, hence the discriminant, hence every spectral stratum.

**The transpose.** $X\mapsto X^{\mathsf T}$ preserves the characteristic polynomial and every stratum.

**The left and right multiplications.** $X\mapsto AX$ and $X\mapsto XB$ preserve the stratum exactly when $A$ or $B$ is a nonzero scalar: an arbitrary $A$ changes the characteristic polynomial.

**The reading.** The spectral stratification is preserved by the group of similarity transformations and by the transpose, and by nothing else in the two-sided family. The determinant stratification is preserved by the much larger group of the left and right multiplications with invertible parameters.

## The Closure of the Regular Set

**The statement.** The spectrally regular set is the complement of the discriminant hypersurface, hence is Zariski open and dense, and its complement is a single irreducible hypersurface for $n\ge2$.

**The consequence.** Every spectral stratum other than the regular one lies in the closure of the regular stratum, and the stratification is the one induced by the vanishing of one polynomial.

**The reading.** The discriminant is the only equation of the coarse picture, which is why the four-sector split has two levels and the four-sector picture has four.

## The Open Stratum

**The statement.** The regular stratum is open and dense, and every other stratum is a proper closed subset of its closure.

**The consequence.** A random matrix is spectrally regular with probability one, and a random one-parameter family meets the discriminant in isolated values of the parameter.

**The reading.** The spectral picture is the picture of a single hypersurface and its complement, which is why the four-sector description is coarser than the spectral one.

## Summary

The spectral partition refines the four sectors by the multiplicity pattern, with dimensions $n^2-\sum\mu_i^2+k$ and one stratum per partition of $n$. The regular stratum is Zariski open and its complement is the discriminant hypersurface. Conjugation and the transpose preserve every stratum; the one-sided and two-sided families preserve none of them in general. The refinement survives from the biquaternion algebra, and the dimensions do not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mu$ | a partition of $n$, the eigenvalue multiplicities |
| $k$ | the number of parts of $\mu$, the number of distinct eigenvalues |
| $S_\mu$ | the stratum of matrices with multiplicities $\mu$ |
| $n^2-\sum\mu_i^2+k$ | the dimension of $S_\mu$ |
| $\Delta$ | the discriminant, of degree $n(n-1)$ |

## Further Reading
- [The Operators on the Four Sectors of $M_n(\mathbb{C})$](the-operators-on-the-four-sectors-of-mnc.html), for the coarse partition.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the characteristic polynomial.
- [Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-reduced-biquaternion-algebra.html), for the case $n=2$.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-mnc.html), for the idempotent strata.
- [The Frame, the Simple Nilpotents and the Frame Group of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-frame-group-of-mnc.html), for the nilpotent orbits.
- [The Classification of the Structures of the Operators of $M_n(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-mnc.html), for where these questions sit.
