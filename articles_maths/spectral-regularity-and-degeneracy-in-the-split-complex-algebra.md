# __Spectral Regularity and Degeneracy in the Split-Complex Algebra__

## Introduction

The split-complex algebra $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ is commutative, two-dimensional and reduced. For $q=t+bj$ left multiplication has matrix $\begin{pmatrix}t&b\\b&t\end{pmatrix}$ in the basis $1,j$. Its characteristic polynomial is $p_q(X)=X^2-2tX+t^2-b^2=(X-t)^2-b^2$, of discriminant $4b^2$. The discriminant is a square: the eigenvalues $t\pm b$ are real and coincide exactly when $b=0$. This article defines the eigenvalue problem, proves the criterion, and separates $\mathbb{D}$ into the spectrally regular case $b\neq0$ and the spectrally degenerate case $b=0$, the real axis. The degenerate case is scalar, every element is semisimple, and no element is defective.

**Notation.** An element is $q=t+bj$ with $t,b\in\mathbb{R}$; $t$ is the scalar part and $b$ the split-imaginary part. The conjugation is $\bar q=t-bj$, the **split norm** is $q\bar q=t^2-b^2$, and the idempotents are $e_\pm=\tfrac12(1\pm j)$, with $e_+^2=e_+$, $e_-^2=e_-$, $e_+e_-=0$ and $e_++e_-=1$. The idempotent coordinates of $q$ are $t+b$ and $t-b$:

$$
q=(t+b)e_+ +(t-b)e_-.
$$

The corpus writes the same element $Q=q+jq'$; its $q$ and $q'$ are the $t$ and $b$ of this article, and its $\Pi_\pm$ are the $e_\pm$. The split norm is indefinite and is not a length.

## The Eigenvalue Problem

**Definition (eigenvalue).** A real number $\lambda$ is an **eigenvalue** of $q$ if $q-\lambda$ is not a unit of $\mathbb{D}$. The **spectrum** of $q$ is the set

$$
\sigma(q)=\{\lambda\in\mathbb{R}:\ q-\lambda\notin\mathbb{D}^{\times}\}.
$$

**Definition (eigenvector).** A non-zero $v\in\mathbb{D}$ is an **eigenvector** of $q$ for $\lambda$ if $qv=\lambda v$. The **eigenspace** of $\lambda$ is

$$
E_\lambda=\{v\in\mathbb{D}:\ qv=\lambda v\}=\ker L_{q-\lambda}.
$$

**Definition (spectral idempotent).** A non-zero idempotent $e$ is a **spectral idempotent** of $q$ if $qe=\lambda e$ for some $\lambda\in\mathbb{R}$.

**Proposition (eigenvalues are eigenvalues of the operator).** For $\lambda\in\mathbb{R}$, the following are equivalent:

1. $\lambda$ is an eigenvalue of $q$;
2. there is a non-zero $v$ with $(q-\lambda)v=0$;
3. $\ker L_{q-\lambda}\neq0$;
4. $L_{q-\lambda}$ is not invertible.

*Proof.* The algebra is finite-dimensional over a field. If $L_x$ is invertible, then $xy=1$ for some $y$, and commutativity gives $yx=1$, so $x$ is a unit. Conversely a unit gives an invertible $L_x$. Hence $x$ is a non-unit exactly when $L_x$ is not invertible, and for an endomorphism of a finite-dimensional space this is equivalent to a non-zero kernel.

**Definition (eigenbasis).** An **eigenbasis** of $q$ is a basis of $\mathbb{D}$ over $\mathbb{R}$ consisting of eigenvectors of $q$.

**Definition (spectral decomposition).** A **spectral decomposition** of $q$ is either the one-term writing $q=t\cdot1$ when $q$ is scalar, or a two-term writing

$$
q=\lambda_+e_+ +\lambda_-e_-,\qquad \lambda_+\neq\lambda_-,
$$

with $e_+,e_-$ non-zero orthogonal idempotents summing to $1$.

## The Characteristic Polynomial and the Discriminant

**Proposition (the matrix of left multiplication).** In the basis $1,j$,

$$
L_q=\begin{pmatrix}t&b\\b&t\end{pmatrix}.
$$

*Proof.* One has $L_q(1)=q=t+bj$ and $L_q(j)=qj=tj+b$, and the two columns are the coordinates of these images.

**Theorem (the characteristic polynomial).** For every $q=t+bj$,

$$
p_q(X)=\det(XI-L_q)=X^2-2tX+t^2-b^2=(X-t)^2-b^2.
$$

The trace is $2t$, the determinant is $t^2-b^2=q\bar q$, the discriminant is $4b^2$, and the eigenvalues are

$$
\lambda_+=t+b,\qquad \lambda_-=t-b.
$$

*Proof.* The trace and the determinant of the displayed matrix are $2t$ and $t^2-b^2$, so the characteristic polynomial is $X^2-2tX+(t^2-b^2)$. Its roots are $t\pm b$, and the discriminant is $4t^2-4(t^2-b^2)=4b^2$.

**Corollary (the spectrum is real).** For every $q$, $\sigma(q)=\{t+b,t-b\}$. The two eigenvalues coincide exactly when $b=0$.

*Proof.* The eigenvalues of a square matrix are the roots of its characteristic polynomial, and the two roots displayed above coincide exactly when $2b=0$.

**Corollary (Cayley–Hamilton and the inverse).** Every $q$ satisfies

$$
q^2-2tq+(t^2-b^2)1=0,
$$

and if $q\bar q\neq0$ then

$$
q^{-1}=\frac{\bar q}{q\bar q}=\frac{t-bj}{t^2-b^2}.
$$

*Proof.* The first identity is the characteristic polynomial evaluated at $q$, or directly $q^2=(t^2+b^2)+2tbj=2tq-(t^2-b^2)$. Multiplying $q\bar q=(t^2-b^2)1$ by $\bar q/(t^2-b^2)$ gives the inverse.

## The Spectral Criterion

**Definition (spectrally regular and degenerate).** The element $q$ is **spectrally regular** if $b\neq0$ and **spectrally degenerate** if $b=0$. The **spectral-degenerate locus** is therefore the real axis

$$
\mathcal{S}=\{q:\ b=0\}=\mathbb{R}.
$$

**Theorem (the criterion).** For $q=t+bj$, the following are equivalent:

1. $b\neq0$;
2. $\sigma(q)$ has two elements;
3. $\operatorname{disc}p_q=4b^2\neq0$;
4. $L_q$ has two distinct eigenvalues;
5. $q$ is not scalar;
6. the minimal polynomial of $q$ has degree two.

*Proof.* (1)$\iff$(2) by $\sigma(q)=\{t+b,t-b\}$; (2)$\iff$(3) by the formula for the discriminant; (3)$\iff$(4) because the eigenvalues of $L_q$ are the roots of $p_q$; (1)$\iff$(5) because $q$ is scalar exactly when $b=0$.

For (1)$\iff$(6): if $b\neq0$, the polynomial $(X-t-b)(X-t+b)$ annihilates $q$ and has two distinct roots; a degree-one annihilator would make $q$ a scalar, so the minimal polynomial has degree two. Conversely, a scalar has minimal polynomial $X-t$ of degree one.

**Remark (degenerate is not defective).** For a non-scalar biquaternion the criterion equates regularity with semisimplicity and diagonalisability. In $\mathbb{D}$ those equivalences fail: $L_q$ is diagonalisable for every $q$, because it is a real symmetric matrix, and every element is semisimple. The discriminant decides whether the diagonal form is scalar, not whether a diagonal form exists.

## Eigenspaces and the Eigenbasis

**Theorem (the eigenspaces).** Let $b\neq0$. Then

$$
E_{t+b}=\mathbb{R}e_+,\qquad E_{t-b}=\mathbb{R}e_-,
$$

and $\mathbb{D}=E_{t+b}\oplus E_{t-b}$.

*Proof.* Since $je_+=e_+$ and $je_-=-e_-$, one has $qe_+=(t+b)e_+$ and $qe_-=(t-b)e_-$. The idempotents $e_+$ and $e_-$ are non-zero and linearly independent, so each displayed eigenspace is the line through the corresponding idempotent. Their dimensions sum to $2$, hence they span $\mathbb{D}$.

**Corollary (the eigenbasis).** For $b\neq0$, the pair $(e_+,e_-)$ is an eigenbasis, and

$$
P^{-1}L_qP=\operatorname{diag}(t+b,t-b),\qquad P=\begin{pmatrix}\tfrac12&\tfrac12\\[2pt]\tfrac12&-\tfrac12\end{pmatrix},\qquad P^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

The eigenbasis is unique up to the order of its two vectors and a non-zero real multiple of each.

*Proof.* The columns of $P$ are the coordinates of $e_+,e_-$ in the basis $1,j$, and the diagonal form records the two eigenvalues. An eigenvector for $t+b$ lies in the line $E_{t+b}$, and an eigenvector for $t-b$ lies in $E_{t-b}$; a basis must take one vector from each line.

**The scalar case.** If $b=0$, then $q=t$ and $L_q=tI$. The eigenspace $E_t$ is all of $\mathbb{D}$, and every basis is an eigenbasis. Thus an eigenbasis exists for every element of $\mathbb{D}$. The discriminant decides its uniqueness, not its existence.

## The Scalar Stratum

**Proposition (the scalar stratum).** For $q=t+bj$, the following are equivalent: $b=0$; $q=t$; $q$ is a scalar; $\sigma(q)=\{t\}$; the minimal polynomial is $X-t$.

*Proof.* The first two are the definition of the scalar part, the third is the same statement, and the last two follow from the characteristic polynomial $(X-t)^2$ and the annihilation by $X-t$.

A scalar has the one-term spectral decomposition $q=t\cdot1$. The two-term writing

$$
q=te_+ +te_-
$$

has equal coefficients and is a refinement, not a spectral decomposition, which requires distinct eigenvalues. The algebra has exactly four idempotents, $0,1,e_+,e_-$ (solve $(t+bj)^2=t+bj$); hence $\{e_+,e_-\}$ is the only non-trivial complementary pair, and the refinement is unique.

## Semisimplicity and the Absence of a Defective Stratum

**Definition (semisimple element).** The **minimal polynomial** $m_q$ is the monic annihilator of $q$ of least degree. An element is **semisimple** if $m_q$ is squarefree, equivalently if the algebra it generates is a product of fields. It is **defective** if it is not semisimple.

**Theorem (every element is semisimple).** Every $q\in\mathbb{D}$ is semisimple, and $\mathbb{D}$ has no defective element.

*Proof.* If $b\neq0$, the minimal polynomial is $(X-t-b)(X-t+b)$, whose roots are distinct. If $b=0$, the minimal polynomial is $X-t$, which is squarefree. In both cases the minimal polynomial is squarefree.

**Corollary (no nilpotents).** The algebra is reduced: $q^2=0$ implies $q=0$.

*Proof.* In idempotent coordinates $q=ue_++ve_-$, so $q^2=u^2e_++v^2e_-$. This vanishes exactly when $u=v=0$, that is $q=0$. Equivalently, $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ is a product of fields.

In the biquaternion algebra the degenerate cone splits into a scalar stratum and two defective strata; in $\mathbb{D}$ the degenerate locus is scalar and semisimple. Degeneracy here is a coalescence of eigenvalues, not a defect.

## Contrast with the Complex, Split-Quaternion and Biquaternion Cases

**The complex case.** For $z=t+bi$, $L_z$ has matrix $\begin{pmatrix}t&-b\\b&t\end{pmatrix}$, characteristic polynomial $(X-t)^2+b^2$ and discriminant $-4b^2$, with eigenvalues $t\pm ib$. The criterion is again $b\neq0$, but the eigenvalues leave $\mathbb{R}$ when $b\neq0$; the sign of $j^2$ reverses the discriminant and moves the spectrum to the complex plane.

**The split-quaternion case.** The algebra $\mathbb{H}_{\mathrm{s}}\cong M_2(\mathbb{R})$ is non-commutative; its spectrum is taken over $\mathbb{C}$, and the discriminant is $-4\langle\vec v\rangle_{\natural}$ for the vector part $\vec v$. The degenerate locus is the cone $\langle\vec v\rangle_{\natural}=0$, where a non-zero null vector part is nilpotent and the element is defective. The locus has real dimension three; the locus in $\mathbb{D}$ is a line.

**The biquaternion case.** The algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has characteristic polynomial $X^2-2Q_tX+Q_t^2+B^2$, of discriminant $-4B^2$ and eigenvalues $Q_t\pm iB$. Its degenerate locus is the cone $B^2=0$, split into a scalar stratum and two defective strata. In $\mathbb{D}$ the quadratic condition has one variable, the cone collapses to the line $b=0$, and the defective strata disappear.

| algebra | discriminant | eigenvalues | degenerate locus | defective elements |
|---|---|---|---|---|
| $\mathbb{C}$ | $-4b^2$ | $t\pm ib$ | real axis | none |
| $\mathbb{D}$ | $4b^2$ | $t\pm b$ | real axis | none |
| dual numbers | $0$ | $t$ | the whole algebra | every non-scalar |
| $\mathbb{H}_{\mathrm{s}}$ | $-4\langle\vec v\rangle_{\natural}$ | $q_t\pm\sqrt{-\langle\vec v\rangle_{\natural}}$ | the cone $\langle\vec v\rangle_{\natural}=0$ | non-zero null vector part |
| $\mathbb{B}$ | $-4B^2$ | $Q_t\pm iB$ | the cone $B^2=0$ | nilpotent and unipotent strata |

The dual numbers show that a vanishing discriminant can coexist with defect: there the square of the generator is zero, so left multiplication is a Jordan block. In $\mathbb{D}$ the square is one, the algebra splits, and the eigenspaces survive.

## Summary

The split-complex algebra $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ is commutative and reduced, and $L_q$ has matrix $\begin{pmatrix}t&b\\b&t\end{pmatrix}$ in the basis $1,j$. The characteristic polynomial is $p_q(X)=X^2-2tX+t^2-b^2=(X-t)^2-b^2$, of trace $2t$, determinant $q\bar q=t^2-b^2$ and discriminant $4b^2$. The eigenvalues $t\pm b$ are always real and coincide exactly when $b=0$.

The spectral criterion is $b\neq0$: the spectrum has two elements exactly when the element is not scalar, the discriminant does not vanish, and the minimal polynomial has degree two. The regular locus is the plane minus the real axis; the degenerate locus is the real axis, and each of its elements is scalar. Every element is semisimple. The eigenbasis is $(e_+,e_-)$ for $b\neq0$, unique up to scaling and order, and every basis for $b=0$. The spectral decomposition is $q=(t+b)e_++(t-b)e_-$ for $b\neq0$ and the one-term writing $q=t\cdot1$ for $b=0$.

The comparison isolates the plane: in $\mathbb{C}$ the eigenvalues leave $\mathbb{R}$ when $b\neq0$; in $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ the degenerate locus is a cone with defective strata; in $\mathbb{D}$ it is the real axis, and its elements are scalars. The two conditions are compared in *Relations between the Split Norm and Spectral Regularity and Degeneracy*, and their four combinations are the subject of *The Four Sectors of the Split-Complex Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ | the split-complex algebra |
| $q=t+bj$ | a general element, $t,b\in\mathbb{R}$ |
| $\bar q=t-bj$ | the conjugation |
| $q\bar q=t^2-b^2$ | the split norm, the determinant of $L_q$ |
| $e_\pm=\tfrac12(1\pm j)$ | the two non-trivial idempotents |
| $t+b,\ t-b$ | the idempotent coordinates, equal to the eigenvalues |
| $L_q(v)=qv$ | left multiplication |
| $p_q(X)=X^2-2tX+t^2-b^2$ | the characteristic polynomial |
| $\operatorname{disc}p_q=4b^2$ | the discriminant |
| $\lambda_\pm=t\pm b$ | the eigenvalues |
| $\sigma(q)$ | the spectrum |
| $E_\lambda=\ker L_{q-\lambda}$ | the eigenspace |
| $\mathcal{S}=\{b=0\}=\mathbb{R}$ | the spectral-degenerate locus |
| $m_q$ | the minimal polynomial of $q$ |

## Further Reading

- [The Spectrum](the-spectrum.html), for the cone and its strata.
- [Split-Quaternion Spectral Theory](split-quaternion-spectral-theory.html), for the cone and its defects.
- [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the eigenprojections and the regimes.
- [Eigenbasis of a Split-Complex Number in Matrix Elements Representations](eigenbasis-of-a-split-complex-number-in-matrix-elements-representations.html), for the matrix models.
- [Worked Examples of Eigenbasis of a Split-Complex Number](worked-examples-of-eigenbasis-of-a-split-complex-number.html), for the eight cases.
- [Relations between the Split Norm and Spectral Regularity and Degeneracy](relations-between-the-split-norm-and-spectral-regularity-and-degeneracy.html), for the two conditions.
- [The Four Sectors of the Split-Complex Algebra](the-four-sectors-of-the-split-complex-algebra.html), for the four combinations.
- [Split-Complex Algebra](split-complex-algebra.html), for the product and the idempotents.
- [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), for the split norm.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the null lines.
