# __The Carriers of Dimension 4 and Spectral Regularity__

## Introduction

The carriers of real dimension $4$ are the four halves cut out by the Hermitian conjugation and by the conjugation of the coefficients. This article computes on them the second predicate: whether the two eigenvalues separate. The answer is uniform for all four halves and much simpler than the norm. On each half,

$$
B^{2}=\pm\lvert\vec v\rvert^{2},
$$

with the sign positive on $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$ and negative on $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{iH}$. So $B^{2}$ vanishes exactly when the triple coordinate vanishes, and the spectral-degenerate locus of each half is its central line: the line $\mathbb{R}e_t$ in two of them and $\mathbb{R}(ie_t)$ in the other two.

Three consequences follow. The degenerate locus is of real codimension three, so a half is spectrally regular at almost every point. Being spectrally degenerate in a half is the same as being central, and the halves contain no non-zero nilpotent. And the two triples inside the halves are spectrally regular at every non-zero point, so the carriers proper avoid the degenerate locus entirely, while the ambient halves do not.

The companion article is *The Carriers of Dimension 4 and Norm Regularity*. The halves are constructed in *Introduction to the Carriers of Dimension 4 over R*.

Nothing below is a statement of physics. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the units $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the unit, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$. An element is $\tilde Q=Q_t+\vec Q$. The triples are $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z}\}$ and $\mathfrak{p}=i\mathfrak{k}$, and $\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$ for $\vec v\in\mathfrak{k}$.

## The Predicate in the Four Halves

**Definition (the characteristic polynomial and the predicate).** For $\tilde Q=Q_t+\vec Q$,

$$
p_{\tilde Q}(X)=X^{2}-2Q_tX+N(\tilde Q),\qquad N=Q_t^{2}+B^{2},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

with roots $\lambda_{\pm}=Q_t\pm iB$ and discriminant $-4B^{2}$. The element is **spectrally regular** when $B^{2}\neq0$ and **spectrally degenerate** when $B^{2}=0$; the zero locus is the cone $\mathcal S$.

**Theorem (the four restrictions).** With the coordinates of the four halves,

$$
B^{2}(i\lambda+\vec v)=\lvert\vec v\rvert^{2},\quad
B^{2}(\lambda+\vec v)=\lvert\vec v\rvert^{2},\quad
B^{2}(\lambda+i\vec v)=-\lvert\vec v\rvert^{2},\quad
B^{2}(i\lambda+i\vec v)=-\lvert\vec v\rvert^{2}.
$$

*Proof.* The vector part of $i\lambda+\vec v$ is $\vec v$, and its coordinates are real, so $B^{2}=\lvert\vec v\rvert^{2}$; the vector part of $\lambda+\vec v$ is the same. For $\lambda+i\vec v$ the vector coordinates are $iv_x,iv_y,iv_z$, so each square changes sign, and the same happens for $i\lambda+i\vec v$.

**Theorem (the degenerate locus is the central line).** For $X$ in any of the four halves,

$$
B^{2}(X)=0\iff\vec v=0\iff X\in\mathbb{R}e_t\ \text{or}\ X\in\mathbb{R}(ie_t)\ \text{according to the half}.
$$

*Proof.* A sum of three squares of real numbers vanishes only when the three vanish; the remaining coordinate is the central one.

**Corollary (codimension three).** In each half the spectral-degenerate locus has real dimension $1$ and the regular locus has real dimension $4$ minus one line; the degenerate set is closed, of empty interior, and of real codimension $3$.

## The Spectrum

**Theorem (the four spectra).** Let $X$ be an element of a half with coordinates $\lambda$ and $\vec v$, and let $\lvert\vec v\rvert$ be the non-negative square root.

$$
\begin{aligned}
X=i\lambda+\vec v\in\mathbb{B}_{\Phi}:&\qquad \operatorname{spec}X=\{\,i(\lambda+\lvert\vec v\rvert),\ i(\lambda-\lvert\vec v\rvert)\,\},\\
X=\lambda+\vec v\in\mathbb{B}_{H}:&\qquad \operatorname{spec}X=\{\,\lambda+i\lvert\vec v\rvert,\ \lambda-i\lvert\vec v\rvert\,\},\\
X=\lambda+i\vec v\in\mathbb{B}_{\Psi}:&\qquad \operatorname{spec}X=\{\,\lambda+\lvert\vec v\rvert,\ \lambda-\lvert\vec v\rvert\,\},\\
X=i\lambda+i\vec v\in\mathbb{B}_{iH}:&\qquad \operatorname{spec}X=\{\,i\lambda+\lvert\vec v\rvert,\ i\lambda-\lvert\vec v\rvert\,\}.
\end{aligned}
$$

*Proof.* Substitute $Q_t$ and $B$ in $\lambda_{\pm}=Q_t\pm iB$. In $\mathbb{B}_{\Phi}$ one has $Q_t=i\lambda$ and $B=\lvert\vec v\rvert$, so the roots are $i\lambda\pm i\lvert\vec v\rvert$. In $\mathbb{B}_{H}$, $Q_t=\lambda$ and the roots are $\lambda\pm i\lvert\vec v\rvert$. In $\mathbb{B}_{\Psi}$, $Q_t=\lambda$ and $B^{2}=-\lvert\vec v\rvert^{2}$, so $B=i\lvert\vec v\rvert$ and the roots are $\lambda\mp\lvert\vec v\rvert$. In $\mathbb{B}_{iH}$, $Q_t=i\lambda$ and $B=i\lvert\vec v\rvert$, so the roots are $i\lambda\mp\lvert\vec v\rvert$.

**Corollary (where the spectrum lies).** In $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{iH}$ the spectrum lies on a line parallel to the imaginary axis; in $\mathbb{B}_{\Psi}$ it lies on a line parallel to the real axis; in $\mathbb{B}_{H}$ it is a complex conjugate pair symmetric about the real point $\lambda$.

**Corollary (the two eigenvalues differ by $2iB$).** The separation of the eigenvalues is $2i\lvert\vec v\rvert$ up to sign, so it is a function of the triple coordinate alone and is independent of the central coordinate.

## No Nilpotents in a Half

**Theorem (the only spectrally degenerate elements are the scalars).** In each half the set of spectrally degenerate elements is the central line, and the elements of that line are scalar: $\lambda e_t$ in $\mathbb{B}_{H}$ and $\mathbb{B}_{\Psi}$, and $i\lambda e_t$ in $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{iH}$.

*Proof.* The degenerate locus is $\{\vec v=0\}$, which is the central line by the definition of the coordinates, and the elements of the central line are the scalar multiples of the unit or of $i$ times the unit.

**Theorem (the halves contain no non-zero nilpotent).** If $X$ lies in a half and $X^{n}=0$ for some $n$, then $X=0$.

*Proof.* A nilpotent element has the single eigenvalue $0$, so $B^{2}=0$ and $Q_t=0$. By the theorem above $B^{2}=0$ forces $\vec v=0$, and then $X$ is a central element $c e_t$ with $c$ real or purely imaginary; the condition $Q_t=0$ forces $c=0$.

**Corollary (the nilpotents lie outside the halves).** The companion nilpotents $\nu=\tfrac12(i\vec e_x+\vec e_y)$ and $\nu'=\tfrac12(i\vec e_x-\vec e_y)$ have a vanishing scalar part and a vector part with $\lvert\vec v\rvert^{2}=0$, and they belong to no half of this group.

**Remark (degeneracy without a Jordan defect).** Every spectrally degenerate element of a half is semisimple, with a minimal polynomial of degree one. The degenerate locus and the nilpotent variety are disjoint in a half, so the predicate there reads the coincidence of two eigenvalues and never a failure of diagonalisability.

## The Carriers Inside the Halves

**Theorem (the triples are spectrally regular).** For $\vec v\neq0$ in $\mathfrak{k}$ or in $\mathfrak{p}$,

$$
B^{2}(\vec v)=\lvert\vec v\rvert^{2}\neq0,\qquad B^{2}(i\vec v)=-\lvert\vec v\rvert^{2}\neq0 .
$$

*Proof.* Set $\lambda=0$ in the restrictions above.

**Corollary (the carriers avoid the degenerate locus).** The carriers $\mathfrak{k}$ and $\mathfrak{p}$ meet the spectral-degenerate locus of their halves only at the origin. Every non-zero element of a carrier of dimension $4$ is spectrally regular.

**Remark (the three carriers side by side).** The three carriers sit in three different positions relative to the two predicates. The centre has $B^{2}=0$ at every point and $N=\lambda^{2}$, so it lies inside the degenerate cone and is norm-regular away from the origin. A column has $N=0$ at every point and $B^{2}=-\tfrac{a^{2}}4$, so it lies inside the null cone and is spectrally regular away from its nilpotent line. A triple has both $N$ and $B^{2}$ non-zero at every non-zero point, so it lies in the doubly regular sector. Of the three, only the carrier of dimension $4$ is regular in both senses.

## The Carrier in the Sector Partition

**Theorem (the sectors on the four halves).** In $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ all four sectors are non-empty; in $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ the sector $\Sigma_{01}$ is empty.

*Proof.* In $\mathbb{B}_{\Phi}$ the element $i\lambda+\vec v$ with $\lvert\vec v\rvert=\lvert\lambda\rvert\neq0$ has $N=0$ and $B^{2}\neq0$, so it lies in $\Sigma_{01}$; the central line away from $0$ lies in $\Sigma_{10}$; the general element lies in $\Sigma_{11}$; the origin lies in $\Sigma_{00}$. In $\mathbb{B}_{H}$ the norm $\lambda^{2}+\lvert\vec v\rvert^{2}$ vanishes only at the origin, so no element has $N=0$ and $B^{2}\neq0$.

| half | $B^{2}$ | degenerate locus | spectrum | $\Sigma_{01}$ |
|---|---|---|---|---|
| $\mathbb{B}_{\Phi}$ | $\lvert\vec v\rvert^{2}$ | $\mathbb{R}(ie_t)$ | $i(\lambda\pm\lvert\vec v\rvert)$ | non-empty |
| $\mathbb{B}_{H}$ | $\lvert\vec v\rvert^{2}$ | $\mathbb{R}e_t$ | $\lambda\pm i\lvert\vec v\rvert$ | empty |
| $\mathbb{B}_{\Psi}$ | $-\lvert\vec v\rvert^{2}$ | $\mathbb{R}e_t$ | $\lambda\pm\lvert\vec v\rvert$ | non-empty |
| $\mathbb{B}_{iH}$ | $-\lvert\vec v\rvert^{2}$ | $\mathbb{R}(ie_t)$ | $i\lambda\pm\lvert\vec v\rvert$ | empty |

## Summary

On the four halves of real dimension $4$ the predicate is determined by the triple coordinate alone: $B^{2}=\lvert\vec v\rvert^{2}$ on $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$, and $B^{2}=-\lvert\vec v\rvert^{2}$ on $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{iH}$.

The spectral-degenerate locus of each half is therefore its central line, of real codimension three, and the elements of that line are scalar. Being spectrally degenerate in a half is the same as being central, and the halves contain no non-zero nilpotent, so the predicate never records a Jordan defect here.

The spectra lie on lines parallel to the imaginary axis in $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{iH}$, on a line parallel to the real axis in $\mathbb{B}_{\Psi}$, and form a conjugate pair in $\mathbb{B}_{H}$; the separation of the two eigenvalues is $2i\lvert\vec v\rvert$ up to sign. The triples $\mathfrak{k}$ and $\mathfrak{p}$ are spectrally regular at every non-zero point, so the carriers proper avoid the degenerate locus of their halves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda+\vec v$, $i\lambda+\vec v$, $\lambda+i\vec v$, $i\lambda+i\vec v$ | the coordinates of an element of each half |
| $\mathfrak{k},\mathfrak{p}=i\mathfrak{k}$ | the real and imaginary triples, the carriers |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part |
| $\lambda_{\pm}=Q_t\pm iB$ | the two roots, of separation $2iB$ |
| $\mathcal S=\{B^{2}=0\}$ | the spectral-degenerate cone |
| $\Sigma_{ij}$ | the sector with the $N$ predicate $i$ and the $B^{2}$ predicate $j$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{H},\mathbb{B}_{\Psi},\mathbb{B}_{iH}$ | the four halves of real dimension $4$ |

## Further Reading

- [Introduction to the Carriers of Dimension 4 over R](the-carriers-of-dimension-4.html), for the four halves, the two involutions and the two tests.
- [The Carriers of Dimension 4 and Norm Regularity](the-carriers-of-dimension-4-and-norm-regularity.html), for the other predicate on the same halves.
- [The Spectrum](the-spectrum.html), for the roots, the discriminant and the characteristic polynomial.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the doubly regular sector containing the triples.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the punctured central lines of the halves.
- [Derivations and the Peirce Decomposition](derivations-and-the-peirce-decomposition.html), for the traceless parts and the central lines of the halves.
