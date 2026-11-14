# __The Carriers of Dimension 4 and Norm Regularity__

## Introduction

The carriers of real dimension $4$ are the four halves of the algebra cut out by the Hermitian conjugation and by the conjugation of the coefficients. This article computes the $N$ norm on each of them. The four answers are four different quadratic forms:

$$
\mathbb{B}_{\Phi}:\ \lvert\vec v\rvert^{2}-\lambda^{2},\qquad
\mathbb{B}_{H}:\ \lambda^{2}+\lvert\vec v\rvert^{2},\qquad
\mathbb{B}_{\Psi}:\ \lambda^{2}-\lvert\vec v\rvert^{2},\qquad
\mathbb{B}_{iH}:\ -\bigl(\lambda^{2}+\lvert\vec v\rvert^{2}\bigr).
$$

So two of the halves carry an indefinite form, and their norm-degenerate locus is a genuine cone of real dimension $3$; two carry a definite form, and their norm-degenerate locus is the origin alone. On the first pair the norm separates the half into two open pieces; on the second it separates nothing.

The result is the sharpest contrast in the group of articles. On the centre the norm vanishes at one point of the carrier. On the columns it vanishes at every point. On the halves it vanishes on a cone that is neither: three-dimensional, with two nappes, and a curved set rather than a subspace. The two triples inside the halves are the exception: they are entirely norm-regular away from the origin.

The companion article is *The Carriers of Dimension 4 and Spectral Regularity*. The halves are constructed in *Introduction to the Carriers of Dimension 4 over R*.

Nothing below is a statement of physics. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the units $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the unit, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$. An element is $\tilde Q=Q_t+\vec Q$. The real pure quaternions are $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and their imaginary partners are $\mathfrak{p}=i\mathfrak{k}$; an element of $\mathfrak{k}$ is written $\vec v$ with $\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$.

## The Four Halves and Their Coordinates

**Definition (the halves).**

$$
\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k},\quad
\mathbb{B}_{H}=\mathbb{R}e_t\oplus\mathfrak{k},\quad
\mathbb{B}_{\Psi}=\mathbb{R}e_t\oplus\mathfrak{p},\quad
\mathbb{B}_{iH}=\mathbb{R}(ie_t)\oplus\mathfrak{p},
$$

each of real dimension $4$. An element is written in the corresponding coordinates:

$$
\mathbb{B}_{\Phi}:i\lambda+\vec v,\qquad
\mathbb{B}_{H}:\lambda+\vec v,\qquad
\mathbb{B}_{\Psi}:\lambda+i\vec v,\qquad
\mathbb{B}_{iH}:i\lambda+i\vec v,
$$

with $\lambda\in\mathbb{R}$ and $\vec v\in\mathfrak{k}$.

**Definition (the norm).** $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, the determinant in the $M_2(\mathbb{C})$ representation, and $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$.

**Theorem (the four restrictions).**

$$
N|_{\mathbb{B}_{\Phi}}=\lvert\vec v\rvert^{2}-\lambda^{2},\qquad
N|_{\mathbb{B}_{H}}=\lambda^{2}+\lvert\vec v\rvert^{2},\qquad
N|_{\mathbb{B}_{\Psi}}=\lambda^{2}-\lvert\vec v\rvert^{2},\qquad
N|_{\mathbb{B}_{iH}}=-\lambda^{2}-\lvert\vec v\rvert^{2}.
$$

*Proof.* For $i\lambda+\vec v$ the scalar part is $i\lambda$ and the vector part is $\vec v$, so $Q_t^{2}=-\lambda^{2}$ and $B^{2}=\lvert\vec v\rvert^{2}$. For $\lambda+\vec v$, $Q_t^{2}=\lambda^{2}$ and $B^{2}=\lvert\vec v\rvert^{2}$. For $\lambda+i\vec v$, $B^{2}=-\lvert\vec v\rvert^{2}$. For $i\lambda+i\vec v$, both terms change sign. Each expression is real, because the coordinates are real.

**Corollary (the four forms are two forms up to sign).** Multiplication by $i$ carries each half to another and multiplies the norm by $-1$:

$$
N(iX)=-N(X),\qquad N|_{i\cdot\mathbb{B}_{\bullet}}=-N|_{\mathbb{B}_{\bullet}}.
$$

## The Signatures

**Theorem (the signatures).** In the four real coordinates $(\lambda,v_x,v_y,v_z)$ the forms have the signatures

$$
\mathbb{B}_{\Phi}:(3,1),\qquad \mathbb{B}_{H}:(4,0),\qquad \mathbb{B}_{\Psi}:(1,3),\qquad \mathbb{B}_{iH}:(0,4).
$$

*Proof.* In these coordinates each form is diagonal with entries $\pm1$ on the $\lambda$ axis and $\pm1$ on each of the three components of $\vec v$: the triple contributes $+1,+1,+1$ in $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$, and $-1,-1,-1$ in $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{iH}$; the central coordinate contributes $-1$ in $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{iH}$, $+1$ in $\mathbb{B}_{H}$ and $\mathbb{B}_{\Psi}$.

**Corollary (definite and indefinite halves).** $\mathbb{B}_{H}$ carries a positive definite form and $\mathbb{B}_{iH}$ a negative definite one; $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ carry forms of signature $(3,1)$ and $(1,3)$.

**Corollary (division halves).** On $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ the norm vanishes only at the origin, so every non-zero element is norm-regular. On $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ there are non-zero null elements.

**Remark (the reason).** $\mathbb{B}_{H}$ is the real quaternion algebra, a division algebra, and its norm is the quaternion norm; $\mathbb{B}_{\Phi}$ is not an algebra at all, since the product of two anti-Hermitian elements need not be anti-Hermitian, and its form is the same form with the sign of one coordinate changed.

## The Null Locus

**Theorem (the null locus of the indefinite halves).** In $\mathbb{B}_{\Phi}$ and in $\mathbb{B}_{\Psi}$,

$$
N(X)=0\iff\lvert\vec v\rvert=\lvert\lambda\rvert,
$$

a real cone of dimension $3$ with vertex $0$ and two nappes, $\lambda>0$ and $\lambda<0$. In $\mathbb{B}_{H}$ and in $\mathbb{B}_{iH}$ the null locus is $\{0\}$.

*Proof.* The equations $\lvert\vec v\rvert^{2}=\lambda^{2}$ and $\lambda^{2}=\lvert\vec v\rvert^{2}$ are the same equation, and its solution set is the cone over the sphere in the $\vec v$ coordinates, doubled along the sign of $\lambda$. The definite cases vanish only at $0$.

**Corollary (the complement has two components).** In $\mathbb{B}_{\Phi}$ the norm is positive on $\lvert\vec v\rvert>\lvert\lambda\rvert$ and negative on $\lvert\vec v\rvert<\lvert\lambda\rvert$; the two sets are open, connected, and separated by the cone. In $\mathbb{B}_{H}$ the punctured half is connected and the norm is positive throughout.

**Remark (the null locus is not a subspace).** On the centre the null locus in the carrier is a point, and on a column it is the whole carrier; both are linear. Here it is a cone: closed under multiplication by real scalars and not closed under addition. The sum of two null elements of a half is in general not null, and the null locus therefore carries no linear structure beyond its vertex.

## The Triples Inside the Halves

**Theorem (the triples are definite).** On $\mathfrak{k}\subset\mathbb{B}_{H}$ and on $\mathfrak{p}\subset\mathbb{B}_{iH}$,

$$
N|_{\mathfrak{k}}=\lvert\vec v\rvert^{2}\geq0,\qquad N|_{\mathfrak{p}}=-\lvert\vec v\rvert^{2}\leq0,
$$

with equality only at $\vec v=0$.

*Proof.* Set $\lambda=0$ in the restrictions above.

**Corollary (the carriers are norm-regular).** Every non-zero element of $\mathfrak{k}$ and of $\mathfrak{p}$ is norm-regular. The null elements of the halves are exactly those with $\lvert\vec v\rvert=\lvert\lambda\rvert\neq0$, which lie in neither triple.

**Remark (where the degeneracy lives).** The null cone of a half is a set of elements that mix the central coordinate and the triple. The two carriers contained in the half are the triples, and they avoid the cone except at the origin. In this sense the ambient half is degenerate and the carrier is not.

## The Carrier in the Sector Partition

**Theorem (the sectors on the four halves).** In $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ all four sectors are non-empty. In $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ the sector $\Sigma_{01}$ is empty.

*Proof.* A null element with $\lvert\vec v\rvert=\lvert\lambda\rvert\neq0$ lies in $\Sigma_{01}$, since its vector part is non-zero; such an element exists exactly in the indefinite halves. In the definite halves the only null element is $0$, which has $B^{2}=0$ as well and lies in $\Sigma_{00}$.

**Corollary (the definite halves meet three sectors).** On $\mathbb{B}_{H}$: $\Sigma_{11}$ is everything except the origin and the punctured central line; $\Sigma_{10}$ is the punctured central line; $\Sigma_{00}$ is the origin; $\Sigma_{01}$ is empty. On $\mathbb{B}_{iH}$ the same with $\mathbb{R}(ie_t)$ in place of $\mathbb{R}e_t$.

| half | signature of $N$ | null locus | $\Sigma_{01}$ | null elements in the carrier |
|---|---|---|---|---|
| $\mathbb{B}_{\Phi}$ | $(3,1)$ | cone, dim $3$, two nappes | non-empty | none |
| $\mathbb{B}_{H}$ | $(4,0)$ | $\{0\}$ | empty | none |
| $\mathbb{B}_{\Psi}$ | $(1,3)$ | cone, dim $3$, two nappes | non-empty | none |
| $\mathbb{B}_{iH}$ | $(0,4)$ | $\{0\}$ | empty | none |

## Summary

On the four halves of real dimension $4$ the $N$ norm takes four forms: $\lvert\vec v\rvert^{2}-\lambda^{2}$ on $\mathbb{B}_{\Phi}$, $\lambda^{2}+\lvert\vec v\rvert^{2}$ on $\mathbb{B}_{H}$, $\lambda^{2}-\lvert\vec v\rvert^{2}$ on $\mathbb{B}_{\Psi}$ and $-\lambda^{2}-\lvert\vec v\rvert^{2}$ on $\mathbb{B}_{iH}$, with signatures $(3,1)$, $(4,0)$, $(1,3)$ and $(0,4)$.

The indefinite halves have a null locus that is a genuine cone of real dimension $3$ with two nappes; the definite halves have the origin alone, and every non-zero element of those halves is norm-regular. Multiplication by $i$ exchanges the two sign patterns, since $N(iX)=-N(X)$.

The triples inside the halves are definite, so the carriers themselves are entirely norm-regular and the degeneracy of the half belongs to the elements that mix the central coordinate with the triple.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda+\vec v$, $i\lambda+\vec v$, $\lambda+i\vec v$, $i\lambda+i\vec v$ | the coordinates of an element of each half |
| $\mathfrak{k},\mathfrak{p}=i\mathfrak{k}$ | the real and imaginary triples |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the $N$ norm, the determinant |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part |
| $\mathcal N=\{N=0\}$ | the null cone |
| $\Sigma_{ij}$ | the sector with the $N$ predicate $i$ and the $B^{2}$ predicate $j$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{H},\mathbb{B}_{\Psi},\mathbb{B}_{iH}$ | the four halves of real dimension $4$ |

## Further Reading

- [Introduction to the Carriers of Dimension 4 over R](the-carriers-of-dimension-4.html), for the four halves, the two involutions and the two tests.
- [The Carriers of Dimension 4 and Spectral Regularity](the-carriers-of-dimension-4-and-spectral-regularity.html), for the other predicate on the same halves.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm and its vanishing set.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the geometry of their boundaries.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the null elements of the indefinite halves.
- [The N-Regular Sector](the-n-regular-sector.html), for the two open pieces cut by the cone.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the conventions of the units and the products.
