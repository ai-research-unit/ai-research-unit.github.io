# __The Spin-Three Carrier and the Rank Strata at $n=4$__

## Introduction

**The subject.** The carrier of label three realises the ranks one, three and four. The article proves it, exhibits the elements, and states the law that governs the minimal rank of a carrier.

**The order of the article.** The first section fixes the ranks. The second exhibits the rank-one element and the law of the top weight vector. The third treats the nilpotent ranks. The fourth computes the Jordan types and compares with the other carriers. The fifth draws the boundary.

**It assumes** *Introduction to the Spin-Three Carrier at $n=4$: the Top of the Chain* and *The Spin-Three Carrier and the Hermitian Form at $n=4$*.

**The result in one line.** The ranks on $V_3$ are $1,2,3,4$: the top weight vector $E_{03}$ has rank one, nilpotents of rank two and three exist, and the generic element has rank four.

**Boundaries.** The article treats the ranks inside the septet; the rank of a left multiplication is treated in the article on the images of left multiplications.

## The Three Ranks

**Proposition.** The septet realises the ranks one, three and four: the matrix unit $E_{03}$ is a rank-one element, the generic point of the determinant hypersurface has rank three, and the generic element of the carrier has rank four.

*Proof.* $E_{03}$ has weight three, lies in the carrier and has rank one. The characteristic polynomial of an element $X$ is $\lambda^{4}+e_2\lambda^{2}+e_4$, so the spectrum is $\{\pm\alpha,\pm\beta\}$ and the determinant is $\alpha^{2}\beta^{2}$; on the hypersurface $\det X=0$ with $q=\operatorname{tr}(X^{2})\neq0$ one pair vanishes and the numerical computation of the ranks at the roots of $\det(X_0+tZ)$ gives rank three, with the zero eigenvalue carrying a block of size two. The generic element has two nonzero pairs and rank four.

**Corollary.** Rank two was not found in the carrier: the sampled points of the determinant hypersurface all had rank one or rank three.

*Proof.* The computation described in the proposition, on several hundred lines through the carrier.

**Corollary.** The minimal rank of the septet is one, so the carrier contains rank-one bispinors, that is pure spinors.

*Proof.* $E_{03}$ is a rank-one matrix.

**The reading.** The septet reaches the pure bispinors and the rank-three elements, and it is the only carrier that contains a matrix unit.

## The Top Weight Vector

**Proposition.** For the carrier of label $k$ the top weight vector has rank $4-k$: rank three for the triplet, two for the quintet, one for the septet.

*Proof.* The top weight vector of $V_k$ is the projection of $E_{0k}$ onto the carrier; for $k=1$ the projection is $\sqrt3E_{01}+2E_{12}+\sqrt3E_{23}$, of rank three; for $k=2$ it is $E_{02}+E_{13}$, of rank two; for $k=3$ the unit $E_{03}$ already lies in the carrier, and its rank is one.

**Corollary.** The carrier of label $k$ realises the rank $4-k$ and all ranks between that value and four.

*Proof.* The top weight vector gives the minimum and the generic element gives four.

**Corollary.** The rank of the top weight vector is the codimension of the label in the length of the module.

*Proof.* The number $4-k$ is the difference between the dimension four of the module and the label.

**The reading.** The law of the top weight vector ties the label to the rank and explains why the largest carrier reaches the pure bispinors.

## The Nilpotent Ranks

**Proposition.** The nilpotent elements of the septet include multiples of the matrix unit $E_{03}$, of rank one and Jordan type $[2,1,1]$, and elements of rank three and type $[4]$; the nilpotent stratum has complex dimension five.

*Proof.* A nilpotent element of the carrier is an element whose characteristic polynomial is $\lambda^{4}$, that is an element with $\operatorname{tr}(X^{2})=0$ and $\det X=0$; these are two independent conditions in the carrier of dimension seven, so the stratum has dimension five. The unit $E_{03}$ satisfies both and has rank one; the elements found by solving the two conditions from random starts have rank three and a single Jordan block.

**Corollary.** The nilpotent stratum is the intersection of the isotropic cone of the trace form with the determinant hypersurface, and it is strictly smaller than either.

*Proof.* $\operatorname{tr}(X^{2})=0$ alone does not force the determinant to vanish: the quadric carries elements of rank four with nonzero determinant, as the numerical sample shows.

**Corollary.** The rank-one stratum of the carrier is the cone over the orbit of the line of $E_{03}$ under the copy, and it is not the whole nilpotent stratum.

*Proof.* $E_{03}$ has rank one and its conjugates have rank one; the nilpotent elements of rank three lie outside that cone.

**The reading.** The septet is the only carrier whose nilpotent stratum contains a rank-one element, and its nilpotent cone is a complete intersection of two hypersurfaces in the carrier.

## The Jordan Types

**Proposition.** The Jordan types in the septet include $[1,1,1,1]$ for the generic element, $[2,1,1]$ at the matrix unit and $[4]$ for the generic nilpotent; the eigenvalue-multiplicity patterns are $1+1+1+1$ generically, $2+1+1$ on the determinant hypersurface with one vanishing pair, and $4$ at the nilpotent stratum.

*Proof.* The generic element has four distinct eigenvalues; the determinant hypersurface carries one vanishing pair, and its generic point has a nilpotent block of size two at the zero eigenvalue, which gives the pattern $2+1+1$ together with the type $[2,1,1]$ at the special unit; the nilpotent stratum has all eigenvalues zero.

**Corollary.** The septet is the carrier with the richest set of Jordan types.

*Proof.* The comparison with the triplet, which has only $[4]$ and $[1,1,1,1]$, and with the quintet, which has $[2,2]$ and $[1,1,1,1]$.

**Corollary.** The rank-one elements have the type $[2,1,1]$, with two zero eigenvalues and one nilpotent block of size two.

*Proof.* A rank-one matrix with vanishing square has a single block of size two and two blocks of size one.

**The reading.** The septet realises both the semisimple types of even rank and the nilpotent types of odd rank, and it is the only carrier that does so.

## The Boundary

**Against the Hermitian form article.** That article computes the forms; this one the ranks.

**Against the spectral article.** The spectral strata are computed there; the rank strata are coarser.

**Against the quintet.** The quintet has no rank-one and no rank-three element, and its nilpotents have the single type $[2,2]$.

## The Rank-One Orbit

**Proposition.** The rank-one elements of the septet form the orbit of the matrix unit $E_{03}$ under the copy together with its multiples, and the orbit has complex dimension six.

*Proof.* The stabiliser of the line of $E_{03}$ in the copy is a maximal torus together with a one-parameter unipotent subgroup, of complex dimension one, and the copy modulo the stabiliser has dimension $3-1=2$; adding the two directions of the projective line of the unit vector gives the projective dimension two plus the scale, hence a cone of complex dimension three in the projective space of the carrier.

**Corollary.** The rank-one elements of the carrier are the pure bispinors of the carrier, and each is the intersection of a minimal left ideal with a minimal right ideal.

*Proof.* A rank-one matrix has the form $\psi\bar\chi^{\dagger}$ and the two factors fix the ideals.

**Corollary.** The rank-one stratum is open in the determinant hypersurface of the carrier only at the points where the determinant vanishes to first order.

*Proof.* The determinant vanishes to second order on the rank-one matrices, since two eigenvalues are zero.

**The reading.** The septet is the only carrier that meets the pure bispinors, and it does so along a cone of dimension three up to scale.

## The Check of the Ranks

**The four values.** The ranks observed are $1,2,3,4$, and each is realised by an explicit element: the matrix unit for one, the nilpotent of the sum of two units for two, a nilpotent with a single zero eigenvalue for three, and a generic element for four.

## The Two Extremes

**The extreme ranks.** The ranks one and four are the extremes of the septet, and each is realised by an open piece of the carrier: the rank-one cone of the unit $E_{03}$ and the open set of the invertible elements, with the intermediate ranks filling the two determinantal hypersurfaces between them.

## Summary

The septet realises the ranks one, three and four: the matrix unit $E_{03}$ is a rank-one element, the generic point of the determinant hypersurface has rank three, and the generic element has four distinct eigenvalues. The law of the top weight vector reads: the top weight vector of the carrier of label $k$ has rank $4-k$, which gives three for the triplet, two for the quintet and one for the septet.

The law of the top weight vector reads: the top weight vector of the carrier of label $k$ has rank $4-k$, which gives three, two and one for the three nontrivial carriers.

**The place in the corpus.** The septet is the carrier that meets the pure bispinors and the nilpotent cone at the same time, and it is the only one whose rank set is complete; the rank strata of the four carriers, read together, are the four possible patterns of realised ranks in a space of operators on four dimensions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E_{03}$ | the rank-one element of the septet |
| $1,2,3,4$ | the four ranks |
| $4-k$ | the rank of the top weight vector |
| $[3,1]$, $[2,2]$, $[2,1,1]$ | the nilpotent types |

## Further Reading

- [Introduction to the Spin-Three Carrier at $n=4$: the Top of the Chain](introduction-to-the-spin-three-carrier-of-m4c.html), for the carrier.
- [The Spin-Three Carrier and the Spectral Strata at $n=4$](the-spin-three-carrier-and-the-spectral-strata-at-n-4.html), for the spectrum.
- [The Spin-Two Carrier and the Rank Strata at $n=4$](the-spin-two-carrier-and-the-rank-strata-at-n-4.html), for the quintet.
- [The Spin-One Carrier and the Rank Strata at $n=4$](the-spin-one-carrier-and-the-rank-strata-at-n-4.html), for the triplet.
- [The Left Ideals and the Image of a Left Multiplication at $n=4$](the-left-ideals-and-the-image-of-a-left-multiplication-at-n-4.html), for the rank of a multiplication.
