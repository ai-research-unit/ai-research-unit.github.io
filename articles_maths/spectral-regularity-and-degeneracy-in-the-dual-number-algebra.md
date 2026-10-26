# __Spectral Regularity and Degeneracy in the Dual-Number Algebra__

## Introduction

The dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ is the simplest algebra over a field in which the characteristic polynomial of every element is a square. For $Q=a+b\varepsilon$, left multiplication has characteristic polynomial $(X-a)^2$, so the spectrum is the singleton $\{a\}$: the two eigenvalues of a quadratic have coalesced before any condition is imposed. This article defines the eigenvalue problem, proves the coalescence, and separates two notions that the coalescence puts at risk of being confused. **Spectral degeneracy** is the repetition of the eigenvalue; it holds for every element. **Defect** is the absence of an eigenbasis; it holds exactly when $b\neq0$. The first is universal, the second is a proper subset of the algebra, and the whole of the spectral theory of $\mathbb{D}'_R$ is the distance between them.

**Notation and conventions.** Throughout, $R$ is a real closed field, with the geometric case $R=\mathbb{R}$; the algebra is $\mathbb{D}'_R$, and a general element is

$$
Q = a + b\varepsilon, \qquad a, b \in R,
$$

with $a = \operatorname{Re}Q$ and $b = \operatorname{Inf}Q$. In the prime notation of *Dual-Numbers Algebra* the same element is $Q = q + \varepsilon q'$, with $a = q$ and $b = q'$. The **norm** (the **dual norm**) is

$$
\langle Q\rangle = Q\bar Q = (a + b\varepsilon)(a - b\varepsilon) = a^2,
$$

where $\bar Q = a - b\varepsilon$ is dual conjugation. The norm is a degenerate quadratic form of rank one, multiplicative, with radical the maximal ideal $\mathrm{M} = (\varepsilon) = \{a = 0\}$; it vanishes exactly on $\mathrm{M}$ and is non-zero exactly on the units. These facts are those of *Dual-Numbers Norm and Invertibility*. The **characteristic polynomial** of $Q$ is the characteristic polynomial of $L_Q$; it is computed below. The matrix-element representation $\mathsf{M}_2$ of *Dual-Numbers Matrix Element Representation* is used only to compare conventions, and the eigenvalue decomposition of a general element is *The Eigenvalue Decomposition of an Element*. The companion articles *The Defective Sector of the Dual-Number Algebra* and *Relations between the Dual Norm and Spectral Degeneracy* take up the defect and the comparison with the norm.

## The Eigenvalue Problem

**An eigenvalue is a scalar for which the translate $Q-\lambda$ has a non-zero kernel, and the criterion is the invertibility criterion of the algebra.**

**Definition (eigenvalue).** A scalar $\lambda\in R$ is an **eigenvalue** of $Q$ if there is a non-zero $v\in\mathbb{D}'_R$ with

$$
Qv = \lambda v.
$$

**Definition (eigenvector, eigenspace, spectrum).** A non-zero $v$ satisfying $Qv = \lambda v$ is an **eigenvector** of $Q$ for $\lambda$. The **eigenspace** of $\lambda$ is

$$
E_\lambda(Q) = \ker L_{Q-\lambda} = \{v : (Q-\lambda)v = 0\},
$$

where $L_A(v) = Av$ is left multiplication. The **spectrum** $\sigma(Q)$ is the set of eigenvalues.

**Proposition (the eigenvalue criterion).** A scalar $\lambda$ is an eigenvalue of $Q$ if and only if $Q-\lambda$ is not a unit of $\mathbb{D}'_R$.

*Proof.* If $Q-\lambda$ is a unit and $(Q-\lambda)v = 0$, then $v = (Q-\lambda)^{-1}(Q-\lambda)v = 0$, so no non-zero eigenvector exists. Conversely, if $Q-\lambda$ is not a unit, then its real part $a-\lambda$ vanishes, because the units of $\mathbb{D}'_R$ are exactly the elements with non-zero real part. Hence $Q-\lambda = b\varepsilon$, and

$$
(Q-\lambda)\varepsilon = b\varepsilon^2 = 0
$$

with $\varepsilon\neq0$, so $\varepsilon$ is an eigenvector and $\lambda$ is an eigenvalue. If $b=0$ as well, then $Q-\lambda=0$ and the kernel is the whole algebra.

**Theorem (the spectrum is a singleton).** For every $Q = a + b\varepsilon$,

$$
\sigma(Q) = \{a\}.
$$

*Proof.* By the criterion, $\lambda$ is an eigenvalue exactly when $a-\lambda=0$, that is exactly when $\lambda=a$. The eigenvector equation at $\lambda=a$ is $b\varepsilon v = 0$, which has non-zero solutions for every $b$, as the proposition shows.

## The Characteristic Polynomial

**The operator is a scalar plus a nilpotent, and the nilpotent contributes nothing to the determinant.**

**Proposition (the operator form).** The operator $L_\varepsilon$ satisfies $L_\varepsilon^2 = 0$ and

$$
L_Q = a\,\mathrm{id} + bL_\varepsilon.
$$

*Proof.* For $v = x + y\varepsilon$,

$$
L_Q(v) = (a + b\varepsilon)(x + y\varepsilon) = ax + (ay + bx)\varepsilon,
$$

while $a v + bL_\varepsilon(v) = a(x + y\varepsilon) + b x\varepsilon = ax + (ay + bx)\varepsilon$. For the square, $L_\varepsilon^2(v) = \varepsilon(\varepsilon v) = \varepsilon^2 v = 0$.

**Theorem (the characteristic polynomial).** In the basis $(1,\varepsilon)$ and with column vectors, the matrix of $L_Q$ is

$$
[L_Q]_{(1,\varepsilon)} = \begin{pmatrix} a & 0 \\ b & a \end{pmatrix},
$$

and

$$
p_Q(X) = \det\bigl(XI - [L_Q]_{(1,\varepsilon)}\bigr) = (X-a)^2.
$$

Moreover

$$
\operatorname{tr}L_Q = 2a, \qquad \det L_Q = a^2 = \langle Q\rangle, \qquad \operatorname{disc}p_Q = 0.
$$

*Proof.* The first column is the image of $1$, namely $a + b\varepsilon$, and the second is the image of $\varepsilon$, namely $a\varepsilon$; this gives the matrix. It is upper triangular with diagonal entries $a$, so its characteristic polynomial is $(X-a)^2$. The trace is the sum of the diagonal entries, the determinant is their product, and the discriminant of $(X-a)^2$ is $4a^2 - 4a^2 = 0$.

**Corollary (the eigenspace).** For every $Q$,

$$
\dim_R E_a(Q) = \begin{cases} 2, & b = 0, \\ 1, & b\neq0. \end{cases}
$$

*Proof.* By the theorem, $E_a(Q) = \ker(bL_\varepsilon)$. If $b=0$ the kernel is everything. If $b\neq0$, then $bL_\varepsilon(x + y\varepsilon) = bx\varepsilon$, which vanishes exactly when $x=0$, so the kernel is the line $R\varepsilon = \mathrm{M}$.

**Remark (the matrix conventions).** The matrix $\begin{pmatrix}a&b\\0&a\end{pmatrix}$ often written for $L_Q$ is the matrix in the reversed basis $(\varepsilon,1)$, the matrix-element representation $\mathsf{M}_2(Q)$ of *Dual-Numbers Matrix Element Representation*, and the matrix of left multiplication on row vectors. In the column convention and the basis $(1,\varepsilon)$ it is the transpose $\begin{pmatrix}a&0\\b&a\end{pmatrix}$ of *Dual-Numbers Element Representations*. The characteristic polynomial, trace, determinant and Jordan type are the same in all readings, since the matrices are similar or transposes.

## The Theorem: Universal Spectral Degeneracy

**Spectral regularity is the separation of the two roots of the characteristic polynomial; in $\mathbb{D}'_R$ there are never two roots to separate.**

**Definition (spectrally regular, spectrally degenerate).** An element $Q$ is **spectrally regular** if its characteristic polynomial is squarefree, equivalently if it has two distinct eigenvalues in $R$. It is **spectrally degenerate** if its characteristic polynomial has a repeated root, equivalently if its discriminant vanishes.

**Theorem (every element is spectrally degenerate).** For every $Q\in\mathbb{D}'_R$, the characteristic polynomial is $(X-a)^2$, of discriminant zero. Hence every element is spectrally degenerate, and there is no spectrally regular element.

*Proof.* The characteristic polynomial was computed in the preceding section; a square has a repeated root and discriminant zero.

**Definition (the sectors).** For $i,j\in\{0,1\}$, let $\Sigma_{ij}$ be the set of elements with $\langle Q\rangle\neq0$ if $i=1$ and $\langle Q\rangle=0$ if $i=0$, and with $Q$ spectrally regular if $j=1$ and spectrally degenerate if $j=0$. Thus

$$
\Sigma_{11} = \{\langle Q\rangle\neq0,\ p_Q \text{ squarefree}\}, \qquad
\Sigma_{10} = \{\langle Q\rangle\neq0,\ p_Q \text{ not squarefree}\},
$$

and similarly for $\Sigma_{01}$ and $\Sigma_{00}$.

**Corollary (the norm/spectrum classification).** In $\mathbb{D}'_R$,

$$
\Sigma_{11} = \varnothing, \qquad
\Sigma_{01} = \varnothing, \qquad
\Sigma_{10} = \{a\neq0\} = (\mathbb{D}'_R)^\times, \qquad
\Sigma_{00} = \mathrm{M} = \{a=0\}.
$$

*Proof.* Both sets with $j=1$ are empty by the theorem. The condition $\langle Q\rangle\neq0$ is $a^2\neq0$, which over the real closed field $R$ is $a\neq0$; this is also the unit criterion. Its complement is $a=0$, namely $\mathrm{M}$.

**Remark (degenerate is not defective).** The theorem says that the eigenvalue is repeated; it does not say that the operator is not diagonalisable. The real axis $b=0$ consists of scalar operators $a\,\mathrm{id}$, which are diagonalisable, while $b\neq0$ is not. The word **degenerate** is fixed by the discriminant; **defective** is fixed by the minimal polynomial. The biquaternion cone draws the same distinction; see *Spectral Regularity and Degeneracy in the Biquaternion Algebra*.

## The Minimal Polynomial Dichotomy

**The minimal polynomial is the first invariant that sees the defect, and it takes exactly two forms.**

**Definition (minimal polynomial).** The **minimal polynomial** $m_Q$ of $Q$ is the monic polynomial of least degree in $R[X]$ with $m_Q(Q)=0$. Equivalently, it is the monic generator of the kernel of the evaluation map $R[X]\to\mathbb{D}'_R$, $X\mapsto Q$.

**Theorem (the dichotomy).** For $Q = a + b\varepsilon$,

$$
m_Q(X) = \begin{cases} X - a, & b = 0, \\ (X-a)^2, & b\neq0. \end{cases}
$$

*Proof.* Since $Q-a = b\varepsilon$, one has $(Q-a)^2 = b^2\varepsilon^2 = 0$. If $b=0$ then $Q-a=0$, so $X-a$ annihilates $Q$ and is of degree one, hence is minimal. If $b\neq0$ then $Q-a\neq0$, so no polynomial of degree one annihilates $Q$; the polynomial $(X-a)^2$ does, and it is therefore minimal.

**Corollary (semisimple and defective).** The following are equivalent:

1. $Q$ is semisimple, that is, $L_Q$ is diagonalisable over $R$;
2. $m_Q$ is squarefree;
3. $b = 0$;
4. $Q$ lies on the real axis $R\cdot1$.

The complement, $b\neq0$, is the **defective set**. It is the complement of the real axis, not the maximal ideal: the maximal ideal $\mathrm{M}\setminus\{0\}$ is the subset of the defective set on which the eigenvalue is zero. The defect is carried by the nilpotent part $Q-a = b\varepsilon$, and $\mathrm{M}\setminus\{0\}$ is the set of possible non-zero nilpotent parts.

*Proof.* The equivalence of (2) and (3) is the theorem, since $X-a$ is squarefree and $(X-a)^2$ is not. For (1) and (2), a linear operator is diagonalisable exactly when its minimal polynomial is squarefree and splits, and both polynomials here split. For (3) and (4), $b=0$ is the real axis by definition. The final description follows because $Q-a = b\varepsilon$ lies in $\mathrm{M}$ and is non-zero exactly when $b\neq0$.

## The Jordan Form

**Off the real axis the operator is a single Jordan block, and the block is visible in a basis adapted to the nilpotent part.**

**Theorem (the Jordan form).** Let $b\neq0$. In the basis $(\varepsilon,\,b^{-1})$ of $\mathbb{D}'_R$, the matrix of $L_Q$ is

$$
[L_Q]_{(\varepsilon,b^{-1})} = \begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix} = J_2(a).
$$

If $b=0$, the matrix is the scalar matrix $aI$ in every basis.

*Proof.* For $b\neq0$,

$$
L_Q(\varepsilon) = a\varepsilon, \qquad
L_Q(b^{-1}) = \frac{a + b\varepsilon}{b} = \frac{a}{b} + \varepsilon = a\,b^{-1} + \varepsilon.
$$

The first column is therefore $(a,0)$ and the second is $(1,a)$, which is the displayed matrix. For $b=0$, $L_Q = a\,\mathrm{id}$.

## The One-Term Spectral Decomposition

**A spectral decomposition separates distinct eigenvalues by orthogonal idempotents; with one eigenvalue and no non-trivial idempotent, it can have only one term.**

**Definition (spectral idempotent, spectral decomposition).** A non-zero idempotent $e\in\mathbb{D}'_R$ is a **spectral idempotent** of $Q$ if $Qe = eQ = ae$ for some scalar $a$. A **spectral decomposition** of $Q$ is a finite sum

$$
Q = \sum_{i=1}^{r}\lambda_i e_i,
$$

where the $\lambda_i$ are distinct scalars, the $e_i$ are non-zero idempotents with $e_ie_j=0$ for $i\neq j$, and $\sum_i e_i = 1$.

**Proposition (the idempotents).** Over a field, the only idempotents of $\mathbb{D}'_R$ are $0$ and $1$.

*Proof.* Let $e = x + y\varepsilon$ and impose $e^2=e$:

$$
x^2 + 2xy\varepsilon = x + y\varepsilon,
$$

so $x^2=x$ and $2xy=y$. In a field $x=0$ or $x=1$. If $x=0$ then $y=0$; if $x=1$ then $2y=y$, so $y=0$ because $2$ is invertible. Hence $e=0$ or $e=1$.

**Theorem (the one-term decomposition).** A spectral decomposition of $Q$ exists if and only if $b=0$. In that case it is the one-term decomposition

$$
Q = a\cdot1,
$$

and it is unique. No element of $\mathbb{D}'_R$ has a two-term spectral decomposition.

*Proof.* A spectral idempotent must be $1$, by the proposition, and then $Q = a\cdot1 = a$, so $b=0$. Conversely, if $b=0$ then $Q=a$ and $Q=a\cdot1$ is a one-term decomposition; it is unique because the only non-zero idempotent is $1$ and the scalar is then $Q$ itself. A two-term decomposition would require two distinct eigenvalues, which the spectrum does not contain.

**Remark (the Jordan–Chevalley decomposition).** Every element has the additive decomposition

$$
Q = a\cdot1 + b\varepsilon,
$$

with $a\cdot1$ semisimple, $b\varepsilon$ nilpotent, and the two commuting. It is the Jordan–Chevalley decomposition of *Nilpotent Elements and the Jordan–Chevalley Decomposition*, and it is unique. It is not a spectral decomposition: the nilpotent part is not separated by an idempotent, and it is non-zero exactly on the defective set. The spectral decomposition is the special case $b=0$, where the nilpotent part vanishes.

## Contrast with the Complex, Split-Complex, Quaternionic and Biquaternionic Algebras

**In the neighbouring algebras the discriminant is the norm of the pure part; in the dual algebra the pure part lies in the radical of the norm, and the discriminant vanishes with it.**

The spectral polynomial of an element is the monic quadratic whose roots are its eigenvalues. In each of the algebras below it has the form

$$
p(X) = (X-a)^2 + \langle\pi\rangle,
$$

where $a$ is the scalar part, $\pi$ is the pure part, and $\langle\pi\rangle$ is the norm of $\pi$ in that algebra. The discriminant is then

$$
\operatorname{disc}p = -4\langle\pi\rangle.
$$

The values are collected in the table; the dual row is the last.

| algebra | element | pure part $\pi$ | norm $\langle\pi\rangle$ | spectral polynomial | discriminant | eigenvalues |
|---|---|---|---|---|---|---|
| $\mathbb{C}$ | $a+bi$ | $bi$ | $b^2$ | $(X-a)^2+b^2$ | $-4b^2$ | $a\pm ib$ |
| $\mathbb{D}=\mathbb{R}[j]$ | $a+bj$ | $bj$ | $-b^2$ | $(X-a)^2-b^2$ | $4b^2$ | $a\pm b$ |
| $\mathbb{H}$ | $q_t+\vec q$ | $\vec q$ | $\lvert\vec q\rvert^2$ | $(X-q_t)^2+\lvert\vec q\rvert^2$ | $-4\lvert\vec q\rvert^2$ | $q_t\pm i\lvert\vec q\rvert$ |
| $\mathbb{B}$ | $Q_t+\vec Q$ | $\vec Q$ | $B^2$ | $(X-Q_t)^2+B^2$ | $-4B^2$ | $Q_t\pm iB$ |
| $\mathbb{D}'$ | $a+b\varepsilon$ | $b\varepsilon$ | $0$ | $(X-a)^2$ | $0$ | $a$ (double) |

Here $\mathbb{D}=\mathbb{R}[j]$ with $j^2=1$ and norm $a^2-b^2$; $\mathbb{H}$ is the quaternion algebra with norm $q_t^2+\lvert\vec q\rvert^2$; $\mathbb{B}$ is the biquaternion algebra with $B^2=Q_x^2+Q_y^2+Q_z^2$ and spectral polynomial as in *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; and $\mathbb{D}'$ is the dual algebra, where $\langle b\varepsilon\rangle = b^2\varepsilon^2 = 0$.

**Theorem (the discriminant is the norm of the pure part).** In each row of the table, the spectral polynomial is $(X-a)^2+\langle\pi\rangle$ and its discriminant is $-4\langle\pi\rangle$.

*Proof.* The complex and split-complex rows are the ordinary quadratic formulae for the matrices of multiplication by $a+bi$ and $a+bj$. The quaternion row is the spectral polynomial of *Quaternion Spectral Theory*, and the biquaternion row is that of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, with pure part $\vec q$ or $\vec Q$ and its norm. The dual row is the characteristic polynomial of the preceding section, with pure part $b\varepsilon$ and norm $\langle b\varepsilon\rangle=b^2\varepsilon^2=0$.

**Corollary (spectral regularity in the five algebras).** In $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$ and $\mathbb{B}$ the spectral-regular locus is the complement of the vanishing locus of a non-zero quadratic form in the pure part; it is non-empty and, over $\mathbb{R}$ or $\mathbb{C}$, open and dense. In $\mathbb{D}'$ the spectral-regular locus is empty.

*Proof.* The discriminant is $-4\langle\pi\rangle$, and the pure-part norm is a non-zero quadratic form in the first four algebras. A non-zero quadratic form is a non-zero polynomial function, so it takes a non-zero value at some point, and its zero set is closed with empty interior; hence its complement is non-empty, open and dense. In $\mathbb{D}'$ the pure part has norm zero, so the discriminant vanishes identically; this is the theorem of §*The Theorem: Universal Spectral Degeneracy*.

## Summary

The dual-number algebra $\mathbb{D}'_R$ has a single spectral phenomenon: every $Q=a+b\varepsilon$ has $p_Q=(X-a)^2$, discriminant zero, spectrum $\{a\}$, and eigenspace of dimension two when $b=0$ and one when $b\neq0$. Every element is spectrally degenerate, so $\Sigma_{11}=\Sigma_{01}=\varnothing$, $\Sigma_{10}=\{a\neq0\}$ and $\Sigma_{00}=\mathrm{M}$.

Spectral degeneracy is not defect. The minimal polynomial is $X-a$ on the real axis and $(X-a)^2$ off it, so the real axis is the semisimple stratum and $b\neq0$ is the defective set; the defect is carried by the nilpotent part $b\varepsilon\in\mathrm{M}$, and $\mathrm{M}\setminus\{0\}$ is the subset with eigenvalue zero, not the whole defective set. Off the real axis the operator is $J_2(a)$ in the basis $(\varepsilon,b^{-1})$, the eigenspace is $R\varepsilon$, and there is no eigenbasis. The only idempotents are $0$ and $1$, so the only spectral decomposition is the one-term $Q=a\cdot1$ of the real axis; the additive Jordan–Chevalley decomposition $Q=a\cdot1+b\varepsilon$ always exists but is not spectral.

The comparison with the neighbouring algebras is the comparison of discriminants: in $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$ and $\mathbb{B}$ the spectral polynomial is $(X-a)^2+\langle\pi\rangle$ with discriminant $-4\langle\pi\rangle$, so the spectral-regular locus is non-empty; in $\mathbb{D}'$ the pure part $b\varepsilon$ has norm zero, the discriminant vanishes identically, and the spectral-regular locus is empty.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}'_R=R[\varepsilon]/(\varepsilon^2)$ | the dual-number algebra over $R$ |
| $\mathbb{D}'=\mathbb{D}'_{\mathbb{R}}$ | the dual-number algebra over $\mathbb{R}$ |
| $Q=a+b\varepsilon$ | a general element, equal to $q+\varepsilon q'$ in the prime notation |
| $a=\operatorname{Re}Q$, $b=\operatorname{Inf}Q$ | real and infinitesimal parts |
| $\bar Q=a-b\varepsilon$ | dual conjugation |
| $\langle Q\rangle=Q\bar Q=a^2$ | the norm, the dual norm; degenerate of rank one, radical $\mathrm{M}$ |
| $\mathrm{M}=(\varepsilon)=\{a=0\}$ | the maximal ideal, the vanishing locus of the norm |
| $L_Q(v)=Qv$, $R_Q(v)=vQ$ | left and right multiplication; equal because the algebra is commutative |
| $p_Q(X)=(X-a)^2$ | the characteristic polynomial of $L_Q$ |
| $\operatorname{disc}p_Q=0$ | the discriminant; spectral degeneracy is universal |
| $m_Q$ | the minimal polynomial: $X-a$ if $b=0$, $(X-a)^2$ if $b\neq0$ |
| $E_\lambda(Q)=\ker L_{Q-\lambda}$ | the eigenspace of $\lambda$ |
| $\sigma(Q)=\{a\}$ | the spectrum |
| $J_2(a)=\begin{pmatrix}a&1\\0&a\end{pmatrix}$ | the Jordan block off the real axis |
| $R\cdot1=\{b=0\}$ | the real axis, the semisimple stratum |
| $\{b\neq0\}$ | the defective set |
| $\Sigma_{ij}$ | the norm/spectrum sectors: $i$ for the norm, $j$ for spectral regularity |
| $\mathsf{M}_2(Q)=\begin{pmatrix}a&b\\0&a\end{pmatrix}$ | the matrix-element representation, the transpose convention of the regular representation |

## Further Reading

- [Dual-Numbers Algebra](dual-numbers-algebra.html), for the algebra, the two conjugations, the maximal ideal and the group of units.
- [Dual-Numbers Norm and Invertibility](dual-numbers-norm-and-invertibility.html), for the norm, its degeneracy, the Euclidean form and the invertibility criterion.
- [Dual-Numbers Matrix Element Representation](dual-numbers-matrix-element-representation.html), for the matrix model, the characteristic polynomial and the transpose convention.
- [Dual-Numbers Element Representations](dual-numbers-element-representations.html), for the regular representation in the basis $(1,\varepsilon)$.
- [The Defective Sector of the Dual-Number Algebra](the-defective-sector-of-the-dual-number-algebra.html), for the defect, its two strata, the module picture and the polar decomposition.
- [Relations between the Dual Norm and Spectral Degeneracy](relations-between-the-dual-norm-and-spectral-degeneracy.html), for the comparison of the norm and the defect and the chain of invariants.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the same distinction on the biquaternion spectral-degenerate cone.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors in the biquaternion algebra.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the additive decomposition $Q=a\cdot1+b\varepsilon$.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block and the module picture of the defect.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the spectral decomposition in the general theory.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the characteristic polynomial, diagonalisability and the Jordan form.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (2nd edition, Prentice-Hall, 1971), for the spectral theorem over $\mathbb{C}$ and the primary decomposition.
- Michael F. Atiyah and Ian G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, Reading, 1969), for local rings and nilpotent ideals.
