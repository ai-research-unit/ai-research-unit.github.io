# __The Spin-$\tfrac32$ Bispinors and the Rank Strata at $n=4$__

## Introduction

**The subject.** The rank of a bispinor is the rank of the corresponding matrix, and the five possible values define five strata of the bispinor space. The article computes the strata, identifies the pure bispinors with the rank-one stratum, and locates the strata of the ideals.

**The order of the article.** The first section fixes the rank of a bispinor. The second describes the five strata and their dimensions. The third treats the pure stratum and the Segre cone. The fourth locates the strata of the ideals and of the carriers. The fifth draws the boundary.

**It assumes** *The Fierz–Kofink Identities and the Classification of Spinors at $n=4$* and *The Left Ideals and the Image of a Left Multiplication at $n=4$*. The row at order two is *The Spin-$\tfrac12$ Bispinors and the Rank Strata*.

**The result in one line.** The bispinor space has five rank strata, of ranks $0,1,2,3,4$, and the rank-one stratum is the Segre cone of the pair of spinor spaces, of dimension seven.

**Boundaries.** The article treats the rank stratification of the whole bispinor space; the rank strata inside a single carrier are the subjects of the carrier articles.

## The Rank of a Bispinor

**Proposition.** The rank of the bispinor $X$ is the dimension of its image, and it is invariant under the conjugation action and unchanged by multiplying $X$ on either side by invertible bispinors.

*Proof.* The rank of a matrix is the dimension of its image; conjugation by invertible matrices preserves the dimension of the image.

**Corollary.** The rank takes the five values $0,1,2,3,4$, and the value four is an open condition.

*Proof.* The rank is at most four; the invertible matrices form an open set.

**Corollary.** The rank of a rank-one bispinor $\psi\bar\chi^{\dagger}$ is one for nonzero factors and zero otherwise.

*Proof.* A nonzero product of a column and a row has a one-dimensional image.

**The reading.** The rank is the first invariant of a bispinor, coarser than the Jordan type and finer than the vanishing of the determinant.

## The Five Strata

**Proposition.** The stratum of rank $r$ has dimension $16-(4-r)^{2}$: the values are $0$, $7$, $12$, $15$ and $16$ for $r=0,1,2,3,4$.

*Proof.* A matrix of rank $r$ is the product of a $4\times r$ matrix of full column rank and an $r\times4$ matrix of full row rank, which gives $4r+r4-r^{2}=8r-r^{2}$ parameters; $8-1=7$, $16-4=12$, $24-9=15$, $32-16=16$.

**Corollary.** The strata have dimensions $0,7,12,15,16$, and each stratum is the closure of the next.

*Proof.* The dimension formula and the semicontinuity of the rank.

**Corollary.** The stratum of rank at most one has dimension seven, and it is the determinantal variety of the algebra.

*Proof.* The rank-one stratum has dimension seven and its closure adds the origin.

**The reading.** The dimensions $0,7,12,15,16$ are the sizes of the determinantal varieties, and the rank-one variety is the smallest nontrivial one.

## The Pure Stratum

**Proposition.** The rank-one stratum is the image of the Segre map $\mathbb{P}^{3}\times\mathbb{P}^{3}\to\mathbb{P}^{15}$, of dimension six in projective space, and it is the union of the minimal left ideals.

*Proof.* A rank-one matrix is $\psi\bar\chi^{\dagger}$ with both factors nonzero, and the pair is determined up to a common scalar; the image of the Segre map has dimension $3+3=6$.

**Corollary.** The pure bispinors are the intersections of a minimal left ideal with a minimal right ideal, and each is a single point of the Segre variety.

*Proof.* The intersection of the ideal and the coideal is the line spanned by the bispinor.

**Corollary.** The rank-one stratum is not invariant under the copy, but it is a union of orbits.

*Proof.* The group acts on both factors, so it preserves the Segre variety and moves points along it.

**The reading.** The pure bispinors form the smallest stratum and the one closest to the spinor description.

## The Ideals and the Carriers

**Proposition.** Every minimal left ideal consists of bispinors of rank at most one, so it lies in the closure of the pure stratum.

*Proof.* The elements of the ideal are $\psi\bar\chi^{\dagger}$ for fixed $\bar\chi$, of rank one or zero.

**Corollary.** The intersection of a carrier with the rank-one stratum is nonempty for $V_3$ and empty for $V_0$.

*Proof.* $V_0$ consists of scalars, of rank four or zero; $V_3$ contains a rank-one matrix, as the weight basis shows.

**Corollary.** The rank strata cut each carrier into pieces, and the pieces are not invariant.

*Proof.* The rank is preserved by conjugation, so the pieces are unions of orbits, and a carrier is a union of orbits of different ranks.

**The reading.** The rank stratification and the carrier decomposition are transverse: the ideals are fibres of the first, the carriers are pieces of the second.

## The Boundary

**Against the classification article.** That article gives the five types; this one gives their dimensions and their geometry.

**Against the carrier rank articles.** Those articles compute the ranks inside a single carrier; this one treats the whole space.

**Against the ideal article.** The ideals are entirely inside the rank-one closure, which is why they are the natural home of the pure bispinors.

## The Rank and the Squaring

**Proposition.** The rank of a bispinor is one and its square is a nonzero multiple of itself, so the rank-one bispinors are exactly the nonzero elements whose square lies in their own line.

*Proof.* A bispinor is $\psi\bar\chi^{\dagger}$; its square is $\psi(\bar\chi^{\dagger}\psi)\bar\chi^{\dagger}$, which is the pairing times the bispinor, and the pairing is nonzero for a pair of nonzero spinors.

**Corollary.** The nonzero bispinors form a single orbit under the product of the two special linear actions, and the orbit is the complement of the zero bispinor.

*Proof.* The two spinors may be brought to any prescribed pair of vectors by the two actions.

**Corollary.** The zero bispinor is the only bispinor of rank zero, and it is the only one whose square vanishes.

*Proof.* The square of a nonzero bispinor does not vanish.

**The reading.** The bispinor space is the set of rank-one matrices, and the rank strata of the whole algebra meet it only in the ranks zero and one; the elements of the intermediate ranks are sums of several bispinors.

## The Rank and the Fierz Identity

**The identity for the square.** The square of a rank-one bispinor is the bispinor times the pairing of its factors, and the identity is the Fierz identity at this order; it shows that the rank-one elements are the idempotents up to scale, and that the scale is the pairing.

**The trace of the square.** The trace of the square of a rank-one bispinor is the square of the pairing, and the trace is also the sum of the squared eigenvalues, which are the pairing and three zeros; the two computations agree, and the agreement is a check of the Fierz identity.

**The rank and the pairing.** A bispinor is zero exactly when one of its factors is zero, because the factors are nonzero spinors and their product cannot vanish; the rank therefore drops to zero only at the origin, and the pairing vanishes exactly when the two factors are orthogonal.

**The reading.** The Fierz identity is the algebraic form of the rank-one condition, and the pairing is the scalar that the identity produces.

## Summary

The rank of a bispinor takes the five values zero to four, and the stratum of rank $r$ has dimension $16-(4-r)^{2}$, that is $0,7,12,15,16$. The stratum of rank at most one is the determinantal variety, of dimension seven, and the pure stratum is the Segre variety of dimension six in projective space.

The minimal left ideals consist of rank-one bispinors and lie in the closure of the pure stratum; the carriers meet the strata in pieces that are not invariant.


**The place in the corpus.** The rank-one elements of the bispinor space are the meeting point of the left and right structures: they are the pure bispinors of the module, the rank-one matrices of the algebra, and the elements of the minimal left ideals, and the three descriptions coincide exactly at rank one.
## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{rank}X$ | the rank of a bispinor |
| $16-(4-r)^{2}$ | the dimension of the stratum of rank $r$ |
| $\mathbb{P}^{3}\times\mathbb{P}^{3}$ | the Segre parametrisation |
| $7$ | the dimension of the rank-one variety |

## Further Reading

- [The Fierz–Kofink Identities and the Classification of Spinors at $n=4$](the-fierz-kofink-identities-at-n-4.html), for the classification.
- [The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals](the-spin-three-halves-bispinors-and-the-minimal-left-ideals-at-n-4.html), for the ideals.
- [The Spin-$\tfrac32$ Bispinors and the Spectral Strata at $n=4$](the-spin-three-halves-bispinors-and-the-spectral-strata-at-n-4.html), for the spectrum.
- [The Spin-$\tfrac12$ Bispinors and the Rank Strata](the-spin-half-bispinors-and-the-rank-strata.html), for the row at order two.
- [The Left Ideals and the Image of a Left Multiplication at $n=4$](the-left-ideals-and-the-image-of-a-left-multiplication-at-n-4.html), for the rank law.
