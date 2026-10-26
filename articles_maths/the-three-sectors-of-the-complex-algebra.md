# __The Three Sectors of the Complex Algebra__

## Introduction

The complex algebra carries two predicates on an element $z$: the **modulus predicate** $M(z)=|z|^2\neq0$, which decides invertibility, and the **spectral predicate** $B(z)=b^2\neq0$, which decides whether the two eigenvalues are distinct. The pair of truth values cuts the algebra into four cells, the **sectors** $\Sigma_{ij}$. In $\mathbb{C}$ three of them are non-empty and the fourth is empty:

$$
\Sigma_{11}=\mathbb{C}\setminus\mathbb{R},\qquad
\Sigma_{10}=\mathbb{R}^\times,\qquad
\Sigma_{01}=\varnothing,\qquad
\Sigma_{00}=\{0\}.
$$

The missing cell would consist of non-zero elements of vanishing modulus, and the complex algebra has none.

This article defines the sectors, proves the partition and the identifications, describes each cell, computes the closures and the dimensions, and records the absence of a defective stratum. It accompanies *Spectral Regularity and Degeneracy in the Complex Algebra* and *Relations between the Modulus and Spectral Regularity and Degeneracy*.

**Conventions.** The algebra is $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$; the element is $z=t+bi$ with $t,b\in\mathbb{R}$, the conjugation is $\bar z=t-bi$, the modulus squared is $|z|^2=z\bar z=t^2+b^2$, and $b^2$ is the square of the imaginary part. The companion articles write $Q=q+iq'$ and $\langle Q\rangle_*=Q\bar Q$; the translation is $t=q$, $b=q'$, $|z|^2=\langle Q\rangle_*$. The eigenvalue criterion and the characteristic polynomial are those of *Spectral Regularity and Degeneracy in the Complex Algebra*; the comparison of the predicates is *Relations between the Modulus and Spectral Regularity and Degeneracy*.

## The Definition and the Partition

**Definition (the sectors).** For $i,j\in\{0,1\}$, let $\Sigma_{ij}$ be the set of elements that are modulus-regular if $i=1$ and modulus-degenerate if $i=0$, and spectrally regular if $j=1$ and spectrally degenerate if $j=0$. Explicitly,

$$
\Sigma_{11}=\{M\neq0,\ B\neq0\},\quad
\Sigma_{10}=\{M\neq0,\ B=0\},\quad
\Sigma_{01}=\{M=0,\ B\neq0\},\quad
\Sigma_{00}=\{M=0,\ B=0\}.
$$

**Theorem (the partition).** The algebra is the disjoint union

$$
\mathbb{C}=\Sigma_{11}\sqcup\Sigma_{10}\sqcup\Sigma_{01}\sqcup\Sigma_{00}.
$$

*Proof.* Each element has exactly one truth value for $M\neq0$ and exactly one for $B\neq0$, hence lies in exactly one of the four combinations.

**Remark (the index).** The first index is the modulus and the second the spectrum, as in the biquaternion articles of the corpus. The cells are read in the order $\Sigma_{11},\Sigma_{10},\Sigma_{01},\Sigma_{00}$: the doubly regular first, the doubly degenerate last.

## The Identification of the Cells

**Theorem (the three non-empty cells).**

$$
\Sigma_{11}=\{b\neq0\}=\mathbb{C}\setminus\mathbb{R},\qquad
\Sigma_{10}=\mathbb{R}^\times,\qquad
\Sigma_{00}=\{0\},\qquad
\Sigma_{01}=\varnothing.
$$

*Proof.* For $\Sigma_{11}$: $B=b^2\neq0$ is $b\neq0$, and it implies $M=t^2+b^2\geq b^2>0$; hence the condition $M\neq0$ is automatic and the cell is the complement of the real axis. For $\Sigma_{10}$: $B=0$ is $b=0$, so $z=t$, and $M\neq0$ is $t^2\neq0$, that is $t\neq0$. For $\Sigma_{00}$: $M=0$ forces $t=b=0$, so $z=0$, and $B(0)=0$. For $\Sigma_{01}$: $M=0$ again forces $z=0$, and then $B=0$, so no element satisfies $M=0$ and $B\neq0$.

**Corollary (three non-empty, one empty).** The cells $\Sigma_{11}$, $\Sigma_{10}$ and $\Sigma_{00}$ are non-empty, with representatives $i$, $1$ and $0$; the cell $\Sigma_{01}$ is empty.

*Proof.* $M(i)=1$ and $B(i)=1$; $M(1)=1$ and $B(1)=0$; $M(0)=B(0)=0$. The emptiness of $\Sigma_{01}$ is the theorem.

**Remark (the names).** $\Sigma_{11}$ is the **doubly regular** cell, $\Sigma_{10}$ is the **modulus-regular, spectrally degenerate** cell, and $\Sigma_{00}$ is the **doubly degenerate** cell. The empty cell would be the modulus-degenerate, spectrally regular cell, the combination forbidden by definiteness.

## The Doubly Regular Cell

**Proposition (the description).** $\Sigma_{11}=\mathbb{C}\setminus\mathbb{R}$ is the union of the upper half-plane $b>0$ and the lower half-plane $b<0$. It is open, dense, and disconnected, with exactly two connected components, each homeomorphic to an open disc. Its real dimension is $2$.

*Proof.* The complement of the real axis is the two open half-planes; each is open and homeomorphic to $\mathbb{R}^2$. The real axis is closed with empty interior, so its complement is open and dense. The two half-planes are separated by the real axis, so they are the two components.

**Proposition (the properties of its elements).** Every element of $\Sigma_{11}$ is a unit, has two distinct eigenvalues, and has a distinguished complex eigenbasis, the pair $(1,-i),(1,i)$.

*Proof.* $M\neq0$ gives invertibility, and $B\neq0$ gives distinct eigenvalues. The eigenbasis is that of *Eigenvalue Decomposition and Eigenbasis of a Complex Number*.

## The Modulus-Regular, Spectrally Degenerate Cell

**Proposition (the description).** $\Sigma_{10}=\mathbb{R}^\times=(-\infty,0)\cup(0,\infty)$ is the punctured real axis. It is the union of two open rays, it has real dimension $1$, and it is not open in $\mathbb{C}$; it is open in the real axis and locally closed in the plane.

*Proof.* The set is the real axis with the origin removed. In the subspace topology of $\mathbb{R}$ it is open, and in $\mathbb{C}$ every neighbourhood of a point of $\Sigma_{10}$ meets $\Sigma_{11}$, so it is not open in the plane. It is the intersection of the closed real axis with the open set $\mathbb{C}\setminus\{0\}$, hence locally closed. Its dimension is one because it is an open subset of the line.

**Proposition (the properties of its elements).** Every element of $\Sigma_{10}$ is a unit and is real. Its spectrum is the singleton $\{t\}$, its minimal polynomial is $X-t$, and every basis of the complexified plane is an eigenbasis.

*Proof.* $M\neq0$ gives invertibility, and $B=0$ gives $b=0$, so $z=t\neq0$. The regular matrix is $tI$, so the spectrum is $\{t\}$, the minimal polynomial is $X-t$, and every vector is an eigenvector.

**Remark (the scalar stratum).** $\Sigma_{10}$ is the real axis minus the origin, the analogue of the scalar stratum of the biquaternion algebra: real scalars, central and semisimple. It differs from that stratum in one point, the origin, which is here the doubly degenerate cell. The spectral decomposition of an element of $\Sigma_{10}$ is the one-term writing $z=t\cdot1$.

## The Doubly Degenerate Cell

**Proposition (the description).** $\Sigma_{00}=\{0\}$ is a single point. It has real dimension $0$ and is closed. Its element is the only non-unit of the algebra, the only modulus-degenerate element, and the only element at which both predicates fail.

*Proof.* $M=0$ forces $z=0$; $B(0)=0$; every non-zero element has $M>0$ and is a unit.

**Proposition (the spectral data at the origin).** The regular matrix is the zero matrix, the spectrum is $\{0\}$, the minimal polynomial is $X$, and every basis of the complexified plane is an eigenbasis.

*Proof.* $L_0=0$, so every vector is an eigenvector with eigenvalue $0$, and $X$ is the minimal annihilating polynomial.

**Remark (the closure).** The origin lies in the closure of both other cells: it is the limit of the real sequence $1/n$ in $\Sigma_{10}$ and of the non-real sequence $i/n$ in $\Sigma_{11}$. It is the only point of the algebra with this property.

## The Empty Cell

**Proposition (the emptiness).** $\Sigma_{01}=\varnothing$.

*Proof.* $M=0$ forces $z=0$, and $B(0)=0$; hence no element has $M=0$ and $B\neq0$.

**Remark (what the empty cell would be).** The cell would consist of non-zero elements whose modulus vanishes and whose imaginary part does not. In the split-complex algebra such elements exist: the two null lines $t=\pm b$ away from the origin have $M=t^2-b^2=0$ and $B=b^2\neq0$. In the biquaternion algebra they also exist; see *The N-Degenerate, Spectrally Regular Sector*. The emptiness of $\Sigma_{01}$ is therefore the exact expression of the definiteness of the complex modulus.

## The Absence of a Defective Stratum

**Theorem (no defective element).** Every element of $\mathbb{C}$ is semisimple. The minimal polynomial over $\mathbb{R}$ is $X-t$ on the real axis and $X^2-2tX+M$ off it, and it is squarefree in both cases.

*Proof.* This is the theorem of *Spectral Regularity and Degeneracy in the Complex Algebra*, §*Eigenspaces and Semisimplicity*.

**Corollary (no defective stratum).** The spectral-degenerate set $\Sigma_{10}\cup\Sigma_{00}=\mathbb{R}$ contains no defective element and no non-zero nilpotent element. The partition into sectors is not refined by the Jordan type.

*Proof.* Every element of the real axis is a scalar $tI$; its minimal polynomial is $X-t$ or $X$, of degree one, hence semisimple. A nilpotent element of a field is zero, so there is no non-zero nilpotent element.

**Remark (the contrast).** In the biquaternion algebra the spectral-degenerate cone splits into three strata, the scalar, the nilpotent and the unipotent, and the last two are defective. The complex case has no such splitting: the spectral-degenerate set is the real axis, all of it is scalar, and all of it is semisimple. This is why the complex algebra has three sectors and no defectivity refinement, while the biquaternion algebra has four sectors and six strata.

## Closure and Dimension

**Theorem (the closures).**

$$
\overline{\Sigma_{11}}=\mathbb{C},\qquad
\overline{\Sigma_{10}}=\mathbb{R},\qquad
\overline{\Sigma_{00}}=\{0\},\qquad
\overline{\Sigma_{01}}=\varnothing.
$$

*Proof.* Every real number $t$ is the limit of $t+i/n\in\Sigma_{11}$, so the closure of $\Sigma_{11}$ contains $\mathbb{R}$ and hence all of $\mathbb{C}$. The closure of $\Sigma_{10}$ is $\mathbb{R}^\times\cup\{0\}=\mathbb{R}$. The closure of a point is itself. The empty set is closed.

**Corollary (the frontier condition).** The closures are ordered by inclusion,

$$
\overline{\Sigma_{00}}=\{0\}\subset\overline{\Sigma_{10}}=\mathbb{R}\subset\overline{\Sigma_{11}}=\mathbb{C},
$$

and each difference of consecutive closures is the union of the lower cells. The partition is a stratification of $\mathbb{C}$ into a two-dimensional open cell, a one-dimensional locally closed cell, and a zero-dimensional closed cell.

*Proof.* The inclusions are the theorem. The frontier condition is $\overline{\Sigma_{10}}\setminus\Sigma_{10}=\{0\}=\Sigma_{00}$ and $\overline{\Sigma_{11}}\setminus\Sigma_{11}=\mathbb{R}=\Sigma_{10}\cup\Sigma_{00}$.

**Theorem (the dimensions).** The real dimensions are $2$ for $\Sigma_{11}$, $1$ for $\Sigma_{10}$, $0$ for $\Sigma_{00}$; the empty cell has no dimension.

*Proof.* $\Sigma_{11}$ is open in $\mathbb{C}\cong\mathbb{R}^2$; $\Sigma_{10}$ is open in $\mathbb{R}$; $\Sigma_{00}$ is a point.

## Summary Table

| sector | condition | description | dimension |
|---|---|---|---|
| $\Sigma_{11}$ | $M\neq0$, $B\neq0$ | $\mathbb{C}\setminus\mathbb{R}$: the two open half-planes $b>0$ and $b<0$ | $2$ |
| $\Sigma_{10}$ | $M\neq0$, $B=0$ | $\mathbb{R}^\times$: the two open rays $t<0$ and $t>0$ | $1$ |
| $\Sigma_{01}$ | $M=0$, $B\neq0$ | empty | none |
| $\Sigma_{00}$ | $M=0$, $B=0$ | the origin $\{0\}$ | $0$ |

## Summary

The two predicates $M\neq0$ and $B\neq0$ cut the complex algebra into four sectors. Three are non-empty: $\Sigma_{11}=\mathbb{C}\setminus\mathbb{R}$, the doubly regular cell; $\Sigma_{10}=\mathbb{R}^\times$, the modulus-regular and spectrally degenerate cell; and $\Sigma_{00}=\{0\}$, the doubly degenerate cell. The fourth, $\Sigma_{01}$, is empty, because $M=0$ forces $z=0$ and $B(0)=0$.

The doubly regular cell is the complement of the real axis, open and dense, with two connected components, the upper and lower half-planes. Every element is a unit with two distinct eigenvalues and the distinguished eigenbasis $(1,-i),(1,i)$. The cell $\Sigma_{10}$ is the punctured real axis, two open rays; every element is a real unit, its spectrum is a singleton, its minimal polynomial is $X-t$, and every basis is an eigenbasis. The cell $\Sigma_{00}$ is the origin, the only non-unit, the only modulus-degenerate element and the only point at which both predicates fail.

The closures are $\overline{\Sigma_{11}}=\mathbb{C}$, $\overline{\Sigma_{10}}=\mathbb{R}$ and $\overline{\Sigma_{00}}=\{0\}$, and they are ordered by inclusion; the partition is a stratification of dimensions $2$, $1$ and $0$. There is no defective stratum: every element is semisimple, and the spectral-degenerate set, the real axis, consists of scalar semisimple elements. The absence of nilpotent and unipotent strata is the field property of $\mathbb{C}$, and it is the structural difference between this three-sector case and the four-sector biquaternion case.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$ | the complex algebra |
| $z=t+bi$ | a complex number |
| $M(z)=\lvert z\rvert^2=t^2+b^2$ | the modulus squared, the first predicate |
| $B(z)=b^2$ | the square of the imaginary part, the second predicate |
| $\Sigma_{ij}$ | the cell with $M\neq0$ iff $i=1$ and $B\neq0$ iff $j=1$ |
| $\Sigma_{11}$ | doubly regular: $\mathbb{C}\setminus\mathbb{R}$ |
| $\Sigma_{10}$ | modulus-regular, spectrally degenerate: $\mathbb{R}^\times$ |
| $\Sigma_{01}$ | modulus-degenerate, spectrally regular: empty |
| $\Sigma_{00}$ | doubly degenerate: $\{0\}$ |

## Further Reading

- [Spectral Regularity and Degeneracy in the Complex Algebra](spectral-regularity-and-degeneracy-in-the-complex-algebra.html), for the spectral criterion, the discriminant and semisimplicity.
- [Eigenvalue Decomposition and Eigenbasis of a Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-complex-number.html), for the eigenbasis and the spectral idempotents of the first cell.
- [Relations between the Modulus and Spectral Regularity and Degeneracy](relations-between-the-modulus-and-spectral-regularity-and-degeneracy.html), for the nesting of the two predicates and the comparison of the invariants.
- [Complex Norm and Invertibility](complex-norm-and-invertibility.html), for the modulus, the units and the three-way classification.
- [Complex Algebra](complex-algebra.html), for the algebra and the real and imaginary subspaces.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the analogue of $\Sigma_{11}$ in the biquaternion algebra.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the analogue of $\Sigma_{10}$ and its unipotent stratum.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the analogue of $\Sigma_{00}$ and its nilpotent stratum.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the non-empty analogue of the empty cell $\Sigma_{01}$.
