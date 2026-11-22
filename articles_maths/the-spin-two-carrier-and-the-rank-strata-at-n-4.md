# __The Spin-Two Carrier and the Rank Strata at $n=4$__

## Introduction

**The subject.** The elements of the carrier of label two have rank zero, two or four, and never one or three. The article proves it from the characteristic polynomial, exhibits the rank-two elements, and reads them as the isotropic cone of the trace form.

**The order of the article.** The first section proves the spectral rigidity. The second derives the three ranks and excludes one and three. The third exhibits the rank-two elements. The fourth computes the Jordan types and compares with the alternating square at order two. The fifth draws the boundary.

**It assumes** *The Spin-Two Carrier and the Trace Form at $n=4$* and *Introduction to the Spin-Two Carrier at $n=4$: the Alternating Square*.

**The result in one line.** The rank of an element of $V_2$ is four when $\operatorname{tr}(X^{2})\neq0$, two when the trace of the square vanishes at a nonzero element, and zero at the origin; rank one and rank three are impossible.

**Boundaries.** The article treats the rank inside the quintet; the rank law for the operators on the algebra is treated in the article on the ten ranks.

## The Spectral Rigidity

**Proposition.** Every element of $V_2$ has the characteristic polynomial $(\lambda^{2}-q/4)^{2}$ with $q=\operatorname{tr}(X^{2})$, so its spectrum is $\{\pm s,\pm s\}$ with $s^{2}=q/4$.

*Proof.* The trace and the cube trace vanish on the carrier, and the determinant equals $q^{2}/16$; the polynomial with these coefficients and a symmetric spectrum is $(\lambda^{2}-q/4)^{2}$, and the identity is verified numerically on random elements.

**Corollary.** The spectrum has at most two distinct values, each with multiplicity two.

*Proof.* The polynomial is the square of a quadratic.

**Corollary.** The element is singular exactly when $q=0$, and then it is nilpotent.

*Proof.* Singularity means a vanishing eigenvalue, and the spectrum is $\{\pm s,\pm s\}$, so $s=0$ and all eigenvalues vanish.

**The reading.** The quintet is the carrier whose spectrum is tied to a single invariant, so the rank takes only three values.

## The Three Ranks

**Proposition.** The rank of a nonzero element of $V_2$ is four if $q\neq0$ and two if $q=0$.

*Proof.* For $q\neq0$ the four eigenvalues are nonzero, so the rank is four; for $q=0$ the element is nilpotent, its square vanishes, and its image is two-dimensional, as the explicit element below shows, so its rank is two.

**Corollary.** The carrier realises exactly the ranks zero, two and four.

*Proof.* The proposition and the origin.

**Corollary.** Rank one and rank three do not occur. A rank-three element would have one zero eigenvalue and three nonzero ones, which the spectrum $\{\pm s,\pm s\}$ forbids; a rank-one element would have the spectrum $\{\mu,0,0,0\}$, so tracelessness forces $\mu=0$ and the element would be a nilpotent of type $[2,1,1]$, while the nilpotents of the carrier have square zero and type $[2,2]$.

*Proof.* The spectrum of a rank-one element is $\{\mu,0,0,0\}$ and that of a rank-three element is $\{\mu,\nu,\nu,0\}$ up to order; the second has three nonzero entries with a single zero, which the form $\{\pm s,\pm s\}$ cannot produce. For the first, $\mu=0$ by tracelessness, and the nilpotents of the carrier satisfy $X^{2}=0$, so their rank is two.

**The reading.** The middle carrier avoids the odd ranks, and its two strata are the invertible elements and the nilpotent cone.

## The Rank-Two Elements

**Proposition.** The element $E_{02}+E_{13}$ belongs to $V_2$, has rank two, and satisfies $(E_{02}+E_{13})^{2}=0$; the element $\tfrac12\operatorname{diag}(1,-1,-1,1)$ belongs to $V_2$, has rank four, and has the spectrum $\{\tfrac12,\tfrac12,-\tfrac12,-\tfrac12\}$.

*Proof.* Both are the projections onto the carrier of matrix units of the corresponding weight; the products are computed directly, since $E_{02}E_{13}=0$ and $E_{13}E_{02}=0$, and the diagonal element has the eigenvalues displayed.

**Corollary.** The rank-two elements are exactly the nonzero elements of the isotropic cone $q=0$, and they form the cone over a quadric of complex dimension three.

*Proof.* The proposition and the spectral rigidity.

**Corollary.** The rank-two stratum contains nilpotents of Jordan type $[2,2]$ and no other type, and it is not a single orbit.

*Proof.* A nilpotent of rank two with a vanishing square has two blocks of size two; the level sets of $q$ and the orbits of the copy give several orbits inside the cone.

**The reading.** The rank-two stratum is the nilpotent cone of the quintet, cut out by one quadratic equation.

## The Jordan Types

**Proposition.** The Jordan types occurring in $V_2$ are $[1,1,1,1]$ for the rank-four elements, $[2,2]$ for the rank-two nilpotents and the type of the zero matrix at the origin.

*Proof.* The rank-four elements are semisimple with two double eigenvalues; the rank-two elements have square zero and rank two.

**Corollary.** The carrier contains no element with a single Jordan block and no block of size three.

*Proof.* The multiplicity is at most two and the square of every singular element vanishes.

**Corollary.** At order two the alternating square is one-dimensional and consists of the multiples of the alternating form, of rank two or zero.

*Proof.* The alternating square of a two-dimensional space is a line spanned by the form, whose matrix is invertible of rank two.

**The reading.** The quintet's Jordan types are the two-block types, and the alternating square at order two is the degenerate case with a single block of size two.

## The Boundary

**Against the trace form article.** That article computes the form whose isotropic cone is the rank-two stratum.

**Against the rank law.** The quintet occupies the ranks two and four, so the middle carrier occupies the middle even ranks.

**Against the septet.** The septet realises rank one, because its top weight vector is a matrix unit.

## A Final Observation

**The cone and its rulings.** The rank-two elements form the isotropic cone of the trace form, a quadric cone of complex dimension four in the five-dimensional carrier; the cone is ruled by the two families of rank-one directions of the alternating square, and each ruling is a family of minimal left ideals.

**The rigidity.** The absence of rank three is the sharpest sign of the rigidity of the quintet: in the septet the intermediate ranks occur, and in the triplet the intermediate rank two does not, so each carrier has its own pattern of realised ranks.

## The Cone and Its Rulings

**The ruling by ideals.** Every rank-two element of the quintet is the sum of two rank-one bispinors, one from each family of minimal left ideals, and the decomposition is not unique; the cone is therefore ruled by the ideals, and the two rulings are the two families of lines on the quadric.

**The two orbits.** The rank-two elements split into the orbit of the nilpotent of type $[2,2]$ and the orbits obtained from it by the action of the copy; the cone is the closure of a single orbit in the space of the carrier for the smaller group, and several orbits for the larger one.

**The scale.** The cone is invariant under multiplication by scalars, so its projectivisation is a quadric surface in the projective space of dimension four; the quadric has two families of lines, and each family is a ruling by the ideals.

**The reading.** The rank-two stratum of the quintet is the projectivised quadric with its two rulings, and the two rulings are the algebraic trace of the two families of bispinors.

## The Check of the Multiplicities

**The two eigenvalues.** The spectrum is $\{\pm s,\pm s\}$ with each value of multiplicity two, so the ratio of the two nonzero eigenvalues is minus one and the projective spectrum is constant; the carrier has a single projective spectral class, and the only variable is the scale.

## Summary

Every element of the carrier of label two has the spectrum $\{\pm s,\pm s\}$ with $s^{2}=\operatorname{tr}(X^{2})/4$, so its rank is four when the trace of the square does not vanish, two when it vanishes at a nonzero element, and zero at the origin. Rank one and rank three are impossible, since each would require an eigenvalue of multiplicity one.

The rank-two elements are the nilpotents of type $[2,2]$ and form the isotropic cone; the explicit element $E_{02}+E_{13}$ is one of them, and $\tfrac12\operatorname{diag}(1,-1,-1,1)$ is an element of rank four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $q=\operatorname{tr}(X^{2})$ | the invariant parameter |
| $\{\pm s,\pm s\}$ | the spectrum |
| $0,2,4$ | the three ranks |
| $[2,2]$ | the nilpotent Jordan type |

## Further Reading

- [Introduction to the Spin-Two Carrier at $n=4$: the Alternating Square](the-spin-two-carrier-of-m4c.html), for the carrier.
- [The Spin-Two Carrier and the Trace Form at $n=4$](the-spin-two-carrier-and-the-trace-form-at-n-4.html), for the form.
- [The Spin-Three Carrier and the Rank Strata at $n=4$](the-spin-three-carrier-and-the-rank-strata-at-n-4.html), for the septet.
- [The Spin-One Carrier and the Rank Strata at $n=4$](the-spin-one-carrier-and-the-rank-strata-at-n-4.html), for the triplet.
- [The Spin-Zero Carrier and the Rank Strata at $n=4$](the-spin-zero-carrier-and-the-rank-strata-at-n-4.html), for the scalars.
