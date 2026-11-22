# __The Spin-Zero Carrier and the Rank Strata at $n=4$__

## Introduction

**The subject.** The rank of an element of the carrier of label zero is zero or four. The article computes the two strata, compares them with the rank strata of the other carriers, and separates the rank from the spectrum.

**The order of the article.** The first section fixes the rank of a scalar. The second computes the two strata and their closures. The third places the carrier in the full list of rank strata of the algebra. The fourth separates the rank from the spectrum and from the determinant. The fifth draws the boundary.

**It assumes** *The Spin-Zero Carrier of $M_4(\mathbb{C})$: the Scalars* and *The Spin-Zero Carrier and the Spectral Strata at $n=4$*. The row at order two is *The Spin-Zero Carrier and the Rank Strata*.

**The result in one line.** The rank of an element of $V_0$ is $0$ or $4$, the invertible stratum is the complement of the origin, and the two strata are the two extremes of the rank stratification of the algebra.

**Boundaries.** The article treats the rank as a function on the carrier and its comparison with the other carriers; it does not compute the rank strata of the septet, which is a later article.

## The Rank of a Scalar

**Proposition.** The rank of $\lambda\mathrm I$ is $4$ for $\lambda\neq0$ and $0$ for $\lambda=0$.

*Proof.* The image of $\lambda\mathrm I$ is the whole space for $\lambda\neq0$ and the zero space for $\lambda=0$.

**Corollary.** The rank function on the carrier takes exactly the two values $0$ and $4$.

*Proof.* The proposition.

**Corollary.** The carrier meets every intermediate rank stratum in the empty set: there is no element of rank $1$, $2$ or $3$ in $V_0$.

*Proof.* A scalar is either invertible or zero.

**The reading.** The carrier is the simplest rank stratification of the algebra: two strata, one point and one open set.

## The Two Strata

**Proposition.** The stratum of rank zero is the origin, the stratum of rank four is the carrier minus the origin, and the second is open and dense in the carrier.

*Proof.* The rank is lower semicontinuous, so the set of elements of rank at least four is open; the origin is closed; the complement of a point in a line is dense.

**Corollary.** The closure of the invertible stratum is the whole carrier, and the origin lies in that closure.

*Proof.* The density and the closedness.

**Corollary.** The carrier is the only one whose rank stratification has two strata and whose rank-zero stratum is a single point.

*Proof.* The other carriers contain elements of intermediate rank and their rank-zero strata contain more than one point.

**The reading.** The two strata are the two ends of the rank scale: the most degenerate element and the generic element.

## The Carrier in the Full Stratification

**Proposition.** The ranks occurring in the four carriers are $0,4$ in $V_0$; $3,4$ in $V_1$; $2,3,4$ in $V_2$; and $1,2,3,4$ in $V_3$.

*Proof.* $V_0$ consists of scalars; $V_1$ is the copy's Lie algebra in the spin-$\tfrac32$ representation, so its elements are $aJ_x+bJ_y+cJ_z$ with eigenvalues $\pm3\lambda/2,\pm\lambda/2$ and rank four when $\lambda\neq0$, and a nonzero nilpotent conjugate to $J_+$, of rank three, when $\lambda=0$; $V_2$ contains a nilpotent of rank two, found numerically, an element of rank three, and generic elements of rank four; $V_3$ contains $E_{03}$ of rank one, $E_{03}+E_{30}$ of rank two, an element of rank three, and generic elements of rank four.

**Corollary.** The minimal rank decreases from four to one as the label increases from zero to three.

*Proof.* The four lists.

**Corollary.** The union of the four carriers is the whole algebra, so every rank from zero to four occurs somewhere, and the extreme ranks occur in the extreme carriers.

*Proof.* The algebra is the sum of the carriers, and the ranks zero and four occur in $V_0$.

**The reading.** The carrier of label zero supplies the two extreme ranks; the other carriers supply the intermediate ones, and the top carrier supplies all four.

## Rank, Spectrum and Determinant

**Proposition.** The rank does not determine the spectrum and the spectrum does not determine the rank.

*Proof.* The zero element and a nilpotent of rank two both have the spectrum $\{0,0,0,0\}$ and different ranks; the scalars $\mathrm I$ and $-\mathrm I$ have the same rank and different spectra.

**Corollary.** The rank is not a function of the invariants of the conjugation action: it is not invariant, since conjugation preserves the rank but the carriers contain elements of different ranks.

*Proof.* The rank is preserved by conjugation, so it is constant on orbits, but a carrier is a union of orbits of different ranks.

**Corollary.** The determinant detects the maximal stratum only: it is nonzero exactly on the elements of rank four, and it vanishes on every other stratum.

*Proof.* The determinant is nonzero exactly for invertible matrices.

**The reading.** The rank refines the determinant: the vanishing of the determinant is one condition, and the rank records how far the element is from invertibility.

## The Boundary

**Against the spectral article.** That article computes the spectrum; this one computes the rank, and the two invariants are independent.

**Against the later rank articles.** The rank strata of the triplet, the quintet and the septet are computed in their own articles; this one gives the list and the extreme case.

**Against the ideal.** The minimal left ideals are the opposite extreme: all their elements have rank at most one.

## A Final Observation

**The two points.** The scalar carrier is a line, and the rank function on it takes the value four at every nonzero point and zero at the origin; the stratum of rank four is the affine line minus the origin, and the stratum of rank zero is the origin itself.

**The separation of the invariants.** The trace and the determinant separate the two points: the trace is nonzero exactly off the origin, and the determinant is nonzero exactly off the origin, so the two invariants vanish together and the carrier has no other rank.

## The Rank Under the Projection

**The projection onto the scalars.** The projector $P_0(X)=\tfrac14\operatorname{tr}(X)\mathrm I$ sends the algebra onto the scalar carrier, and it has rank four for every matrix of nonzero trace and rank zero on the traceless hyperplane of dimension fifteen.

**The fibres.** The fibre of the projection over a nonzero scalar is an affine hyperplane, and the fibre over zero is the traceless hyperplane; the rank of the projection therefore jumps on a single hyperplane, which is the two-stratum picture of the carrier read from the side of the algebra.

**The comparison with the rank strata.** The rank strata of the carrier are the image under the projection of the trace strata of the algebra, and the four strata of the other carriers are the images of the finer decompositions of the traceless part.

**The reading.** The scalar carrier is the image of the trace map, and its two points record the two behaviours of the trace on the algebra.

## Summary

On the carrier of label zero the rank is zero at the origin and four elsewhere, so the carrier has two rank strata, one point and one open dense set. It meets no intermediate stratum.

In the full algebra the ranks occurring in the carriers are $0,4$; $3,4$; $2,3,4$; and $1,2,3,4$, so the minimal rank decreases as the label increases and the extreme ranks belong to the extreme carriers.

The rank is independent of the spectrum and refines the determinant: the determinant vanishes exactly off the maximal stratum.


**The place in the corpus.** The scalar carrier is the smallest of the four and the only one whose rank function is constant off the origin; its rank stratum of dimension one and its origin are the image under the projection onto the centre of the rank strata of the other carriers, which is the reason the list of carriers always ends with the term one.
## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{rank}$ | the rank of a matrix |
| $0,4$ | the ranks in $V_0$ |
| $3,4$; $2,3,4$; $1,2,3,4$ | the ranks in $V_1,V_2,V_3$ |
| $\det\neq0$ | the maximal stratum |

## Further Reading

- [The Spin-Zero Carrier of $M_4(\mathbb{C})$: the Scalars](the-spin-zero-carrier-of-m4c.html), for the carrier.
- [The Spin-Zero Carrier and the Spectral Strata at $n=4$](the-spin-zero-carrier-and-the-spectral-strata-at-n-4.html), for the spectrum.
- [The Spin-Three Carrier and the Rank Strata at $n=4$](the-spin-three-carrier-and-the-rank-strata-at-n-4.html), for the top carrier.
- [The Spin-Zero Carrier and the Rank Strata](the-spin-zero-carrier-and-the-rank-strata.html), for the row at order two.
- [The Left Ideals and the Image of a Left Multiplication at $n=4$](the-left-ideals-and-the-image-of-a-left-multiplication-at-n-4.html), for the rank law.
