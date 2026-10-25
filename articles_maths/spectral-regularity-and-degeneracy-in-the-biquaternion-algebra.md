# __Spectral Regularity and Degeneracy in the Biquaternion Algebra__

## Introduction

This article treats the eigenvalue problem of an element of the biquaternion algebra. For $\tilde Q=Q_te_t+\vec Q$ and a scalar $\lambda$, the question is whether the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, equivalently whether $\tilde Q-\lambda e_t$ is a non-unit. The answer is read from the characteristic polynomial: its discriminant $-4R^2$, with $R^2=Q_x^2+Q_y^2+Q_z^2$, vanishes exactly when the two eigenvalues $Q_t\pm iR$ coalesce. The locus $\mathcal S=\{R^2=0\}$ is the **spectral-degenerate cone**. The article describes the cone, its three regimes and the spectral decomposition on each side. The comparison with the invertibility problem is left to *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*.

The article states the eigenvalue problem without a module or an acting operator. An eigenvalue is a scalar for which a left ideal is proper, an eigenvector is an element of a left annihilator, and a spectral idempotent is an idempotent commuting with the element. On that vocabulary the spectral criterion is proved: $\lambda$ is an eigenvalue of $\tilde Q$ exactly when $\det\mathsf{M}_2(\tilde Q-\lambda e_t)=0$, that is exactly when $(\lambda-Q_t)^2+R^2=0$. The characteristic polynomial follows, $p_{\tilde Q}(X)=(X-Q_t)^2+R^2$, with discriminant $-4R^2$, and the degenerate side $\mathcal S$ is stratified into three regimes: scalar, Jordan and nilpotent. A two-term spectral decomposition is shown to exist exactly on the non-scalar side where $R^2\neq0$, and to fail on the Jordan and nilpotent regimes.

**Scope and naming.** The subject is the eigenvalue problem of a single element: the spectrum, the characteristic polynomial, the discriminant, the eigenspaces, the spectral idempotents and the existence of a spectral decomposition. The degeneration locus is $\mathcal S=\{R^2=0\}$, the **spectral-degenerate cone**; it is the discriminant locus of the characteristic polynomial. Unqualified **regular** means **spectrally regular**, that is $R^2\neq0$, and **degenerate** means spectrally degenerate, $R^2=0$. The invertibility problem of the algebra is not treated here; its comparison with the spectral problem is *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$, and with complex coefficients. The natural conjugation is the $\mathbb{C}$-linear quaternion conjugation $\tilde Q^{\natural}=Q_t-\vec Q$, an anti-involution of order two fixing the centre. The vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and

$$
R^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-R^2e_t.
$$

The number $R$ is a fixed complex square root of $Q_x^2+Q_y^2+Q_z^2$; the other root only exchanges the two eigenvalues. The comparison article *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy* and the sector articles write $B^2$ for the same square and $B$ for the same root. The matrix realization $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* is used only to test invertibility, through the determinant $\det\mathsf{M}_2(\tilde Q)=Q_t^2+R^2$. The algebra and its conventions are *The Biquaternion Algebra and Its Vector Spaces*; the eigenvalue decomposition, the normality criterion and the spectral theorem are *The Biquaternion Eigenvalue Decomposition*.

## The Spectral Criterion

**Definition (eigenvalue).** A scalar $\lambda\in\mathbb{C}$ is an **eigenvalue** of $\tilde Q$ if the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, that is $\mathbb{B}(\tilde Q-\lambda e_t)\neq\mathbb{B}$.

**Definition (eigenvector).** A non-zero $v\in\mathbb{B}$ is an **eigenvector** of $\tilde Q$ for $\lambda$ if $(\tilde Q-\lambda e_t)v=0$. The eigenvectors for $\lambda$, with the origin, are the left annihilator

$$
\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)=\{v:\ (\tilde Q-\lambda e_t)v=0\},
$$

which is a right ideal of $\mathbb{B}$.

**Definition (spectral idempotent).** A non-zero idempotent $e$ is a **spectral idempotent** of $\tilde Q$ if $e\tilde Q=\tilde Qe=\lambda e$ for some scalar $\lambda$.

**Definition (spectral decomposition).** A **spectral decomposition** of $\tilde Q$ is a pair of orthogonal idempotents $e_+,e_-$ with

$$
e_++e_-=e_t,\qquad e_+e_-=0,\qquad \tilde Qe_\pm=\lambda_\pm e_\pm,\qquad \lambda_+\neq\lambda_-.
$$

No module and no acting operator enters the definitions: the primitives are the left ideal, the left annihilator and the idempotent.

**Theorem (the spectral criterion).** For $\tilde Q\in\mathbb{B}$ and $\lambda\in\mathbb{C}$, the following are equivalent:

1. $\lambda$ is an eigenvalue of $\tilde Q$;
2. $\tilde Q-\lambda e_t$ is not a unit of the plain product;
3. $\det\mathsf{M}_2(\tilde Q-\lambda e_t)=0$;
4. $(\lambda-Q_t)^2+R^2=0$.

*Proof.* Write $a=\tilde Q-\lambda e_t$.

*(1)$\iff$(2).* If $a$ is a unit then $\mathbb{B}a=\mathbb{B}$, and the left ideal is not proper. Conversely, if $\mathbb{B}a=\mathbb{B}$, then $e_t=xa$ for some $x$, so $x$ is a left inverse of $a$. The left multiplication by $a$ is then injective: $ay=0$ gives $y=xay=0$. In finite dimension an injective endomorphism is bijective, so there is $b$ with $ab=e_t$; then

$$
x=x e_t=x(ab)=(xa)b=e_tb=b,
$$

and $a$ has the two-sided inverse $b$. Hence a proper left ideal forces a non-unit.

*(2)$\iff$(3).* The algebra isomorphism $\mathsf{M}_2$ turns the plain product into the matrix product, so $a$ is a unit exactly when $\mathsf{M}_2(a)$ is an invertible matrix, and a square matrix over a field is invertible exactly when its determinant is non-zero.

*(3)$\iff$(4).* For $a=a_te_t+\vec a$ the matrix is

$$
\mathsf{M}_2(a)=\begin{pmatrix} a_t-ia_z & -ia_x-a_y\\ -ia_x+a_y & a_t+ia_z\end{pmatrix},
$$

whose determinant is $a_t^2+a_x^2+a_y^2+a_z^2$. With $a_t=Q_t-\lambda$ and $\vec a=\vec Q$ this is $(\lambda-Q_t)^2+R^2$.

**Corollary (the characteristic polynomial).** For every $\lambda$,

$$
\det\mathsf{M}_2(\tilde Q-\lambda e_t)=(\lambda-Q_t)^2+R^2,
$$

so the characteristic polynomial is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+R^2,
$$

of discriminant

$$
\operatorname{disc}p_{\tilde Q}=4Q_t^2-4(Q_t^2+R^2)=-4R^2.
$$

The eigenvalues are

$$
\lambda_\pm=Q_t\pm iR,
$$

and they coincide exactly when $R=0$, that is exactly when $R^2=0$.

**Corollary (the eigenspaces).** For a non-scalar $\tilde Q$ and each eigenvalue $\lambda$, the eigenspace $\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)$ is a right ideal of complex dimension $2$. For $\tilde Q=Q_te_t$ the only eigenvalue is $Q_t$, and its eigenspace is all of $\mathbb{B}$.

*Proof.* A non-zero non-unit in $\mathbb{B}$ has left multiplication of complex rank $2$, by *The Four General Products and Their Relations over the Biquaternion Algebra*, §*The Annihilators*; at the scalar the difference $\tilde Q-Q_te_t$ is zero.

**Corollary (Cayley–Hamilton and the inverse).** Every $\tilde Q$ satisfies

$$
\tilde Q^2-2Q_t\tilde Q+(Q_t^2+R^2)e_t=0 ,
$$

and if $Q_t^2+R^2\neq0$ then $\tilde Q^{-1}=(2Q_te_t-\tilde Q)/(Q_t^2+R^2)=\tilde Q^{\natural}/(Q_t^2+R^2)$.

*Proof.* With $\tilde Q=Q_te_t+\vec Q$ and $\vec Q^2=-R^2e_t$, $\tilde Q^2=Q_t^2e_t+2Q_t\vec Q-R^2e_t=2Q_t\tilde Q-(Q_t^2+R^2)e_t$. Multiplying by $2Q_te_t-\tilde Q=\tilde Q^{\natural}$ on either side gives $(Q_t^2+R^2)e_t$.

**Remark (left and right eigenvalues).** The centre of $\mathbb{B}$ is $\mathbb{C}$, so complex scalars commute with every element. A left eigenvalue, $\tilde Qv=\lambda v$, and a right eigenvalue, $\tilde Qv=v\lambda$, therefore define the same set when the scalar is required to lie in $\mathbb{C}$, and that set is $\sigma(\tilde Q)$. The distinction between the two eigenvalue problems, which is genuine over a noncommutative division ring (*Quaternion Spectral Theory*, §*The Spectrum of a Quaternion*), collapses here.

## Similarity Classes and the Eigenvalue Dichotomy

**Definition.** Two biquaternions $\tilde Q_1,\tilde Q_2$ are **similar** if $\tilde Q_2=S\tilde Q_1S^{-1}$ for some unit $S\in\mathbb{B}$.

**Theorem (the classification).** Let $T=2Q_t$ and $D=Q_t^2+R^2$, and let $\Delta=T^2-4D=-4R^2$.

1. If $R\neq0$, the eigenvalues $Q_t\pm iR$ are distinct, and the similarity class is determined by the unordered pair of eigenvalues, equivalently by $(T,D)$.
2. If $R=0$, the only eigenvalue is $Q_t$, and exactly two similarity classes share $(T,D)=(2Q_t,Q_t^2)$: the **central class** $\tilde Q=Q_te_t$, and the **non-semisimple class** $\vec Q\neq0$ with $\vec Q^2=0$, which is similar to the Jordan block with diagonal $Q_t$.

*Proof.* (1) $p_{\tilde Q}$ has two distinct roots, so $\tilde Q$ is diagonalisable with those roots; any two such elements are conjugate in $\mathbb{B}\cong M_2(\mathbb{C})$. (2) $R=0$ gives $\vec Q^2=0$. If $\vec Q=0$ the element is central. If $\vec Q\neq0$, then $\tilde Q-Q_te_t$ is nonzero with square $0$, so the minimal polynomial is $(X-Q_t)^2$ and the Jordan form is a single block of size $2$; all such elements are conjugate.

**Corollary.** In the non-semisimple class the element is a zero divisor exactly when $Q_t=0$, since $Q_t^2+R^2=Q_t^2$ on that class.

## The Spectral-Degenerate Cone

**Definition.** The **spectral-degenerate cone** is

$$
\mathcal S=\{R^2=0\}=\{\vec Q^2=0\}=\{\operatorname{disc}p_{\tilde Q}=0\}.
$$

**Theorem (three readings of one equation).** The equation $R^2=0$ is simultaneously:

- **geometric:** the vector part is isotropic, $Q_x^2+Q_y^2+Q_z^2=0$;
- **algebraic:** the vector part is square-zero, $\vec Q^2=0$, hence nilpotent of index two when it is non-zero;
- **spectral:** the discriminant vanishes, and the two eigenvalues coalesce at $Q_t$.

**Theorem (the geometry).** The cone is the product of the scalar line and the isotropic cone of the vector subspace,

$$
\mathcal S=\mathbb{C}e_t\times\{\vec Q\in\operatorname{Vect}(\mathbb{B}):\vec Q^2=0\}.
$$

It is a complex cone of complex dimension $3$ and real dimension $6$. Its singular locus is the **vertex** $\{\vec Q=0\}$, the whole scalar line; off the vertex it is a smooth hypersurface.

*Proof.* The equation $R^2=0$ is one complex equation in the four complex coefficients, homogeneous of degree two. Its gradient with respect to $(Q_t,Q_x,Q_y,Q_z)$ is

$$
(0,\,2Q_x,\,2Q_y,\,2Q_z),
$$

which vanishes exactly when $\vec Q=0$. Off the vertex the gradient is non-zero and the equation cuts a smooth hypersurface, of complex dimension $4-1=3$ and real dimension $8-2=6$. On the vertex the cone is $\mathbb{C}e_t\times C$, with $C$ the isotropic cone of $\mathbb{C}^3$, which is singular at its apex; the product is singular along the whole line.

**The cone is not a subspace.** The elements $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ lie on $\mathcal S$, since their vector squares are $1+i^2=0$, but their sum $2\vec e_x$ has $R^2=4$ and lies off it.

**Warning (the vertex is not defective).** A point of the vertex is a scalar $\tilde Q=Q_te_t$. Its only eigenvalue is $Q_t$, repeated, and its minimal polynomial is $X-Q_t$: it is semisimple and diagonalisable. The cone $\mathcal S$ is therefore the set of elements with a repeated eigenvalue, not the set of non-diagonalisable elements. The defective elements of $\mathcal S$ are the Jordan and nilpotent regimes of §*The Degenerate Case $Q_x^2+Q_y^2+Q_z^2=0$*. This distinction is invisible in the equation $R^2=0$.

**Warning (the name).** $R^2$ is the square of the vector part: as a quadratic form on $\mathbb{B}$ it is degenerate, since it does not involve $Q_t$. The cone $\mathcal S$ is the discriminant locus of the characteristic polynomial. It is not the set of zero divisors either: the vertex consists of units when $Q_t\neq0$.

## The Spectral Decomposition

**A non-scalar element has a spectral decomposition exactly when $R^2\neq0$, and then it is unique; the two idempotents are the Lagrange idempotents of the two eigenvalues.**

**Definition.** A **spectral decomposition** of $\tilde Q$ is a writing

$$
\tilde Q=\lambda_+e_++\lambda_-e_-,
$$

where $\lambda_\pm\in\mathbb{C}$ and $e_+,e_-$ are non-zero idempotents with

$$
e_+^2=e_+,\qquad e_-^2=e_-,\qquad e_+e_-=e_-e_+=0,\qquad e_++e_-=e_t.
$$

The scalars $\lambda_\pm$ are the eigenvalues and the idempotents $e_\pm$ are the **spectral idempotents**. A scalar element has the one-term decomposition $\tilde Q=Q_te_t$.

**Theorem (existence).** Let $\tilde Q$ be non-scalar. The following are equivalent:

1. $R^2\neq0$;
2. $\tilde Q$ has a spectral decomposition;
3. $\tilde Q$ is semisimple;
4. $L_{\tilde Q}$ is diagonalisable.

*Proof.* (1)$\Rightarrow$(2). When the eigenvalues are distinct, the Lagrange idempotents

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}
$$

are defined. The algebra identities give

$$
e_\pm^2=e_\pm,\qquad e_+e_-=0,\qquad e_++e_-=e_t,\qquad \tilde Qe_\pm=\lambda_\pm e_\pm,
$$

so they form a spectral decomposition.

(2)$\Rightarrow$(3). The minimal polynomial divides $(X-\lambda_+)(X-\lambda_-)$ and is not of degree one, since $\tilde Q$ is not scalar. It is therefore $(X-\lambda_+)(X-\lambda_-)$, and $\lambda_+\neq\lambda_-$, since otherwise $\tilde Q=\lambda_+e_t$ would be scalar. Hence the minimal polynomial has distinct roots and $\tilde Q$ is semisimple.

(3)$\iff$(1). For a non-scalar element the minimal polynomial is the characteristic polynomial $p_{\tilde Q}(X)=(X-Q_t)^2+R^2$, of degree two. It is squarefree exactly when the two roots are distinct, that is exactly when $R^2\neq0$.

(3)$\iff$(4). The left regular representation is faithful and carries $\mathbb{C}[\tilde Q]$ isomorphically onto $\mathbb{C}[L_{\tilde Q}]$, so $\tilde Q$ and $L_{\tilde Q}$ have the same minimal polynomial. An operator is diagonalisable exactly when its minimal polynomial is squarefree.

**Corollary (uniqueness).** If $R^2\neq0$, the spectral decomposition is unique. The centraliser of $\tilde Q$ is $\mathbb{C}[\tilde Q]\cong\mathbb{C}\times\mathbb{C}$, whose only idempotents are $0,e_t,e_+,e_-$, and every spectral decomposition of $\tilde Q$ uses the pair $e_+,e_-$.

*Proof.* The minimal polynomial has two distinct roots, so the Chinese remainder theorem gives $\mathbb{C}[X]/((X-\lambda_+)(X-\lambda_-))\cong\mathbb{C}\times\mathbb{C}$, and the idempotents of the product are the four listed. A spectral idempotent lies in the centraliser and is therefore one of them.

**The scalar exception.** The theorem excludes the scalar elements, and it must: if $\tilde Q=Q_te_t$ is central, every idempotent commutes with it, and the two-term writing $Q_t\tilde\Pi+Q_t(e_t-\tilde\Pi)$ exists for every non-trivial idempotent $\tilde\Pi$ while $R^2=0$. That writing is not the spectral decomposition of a non-scalar element: the coefficients coincide and the pair is not determined by $\tilde Q$. The scalar regime is treated below.

## The Two Cases

**The discriminant of $p_{\tilde Q}=X^2-2Q_tX+Q_t^2+R^2$ is $-4R^2$. The vanishing of $R^2$ therefore cuts the algebra into two spectral cases.**

| case | condition | spectrum | spectral decomposition | eigenbasis |
|---|---|---|---|---|
| **non-degenerate** | $R^2\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | two terms, unique | exists |
| **degenerate** | $R^2=0$ | one eigenvalue | one term at the vertex, none off it | every basis at the vertex, none off it |

The non-degenerate case is the complement of the cone $\mathcal S$: it is the spectral-regular case, treated in §*The Spectral Decomposition* and §*The Eigenbasis of Left Multiplication*. The degenerate case is the cone itself, and its points are classified in §*The Degenerate Case*. The zero element is degenerate, and it is the one point of the cone that is neither a unit nor a zero divisor: it is treated in §*The Zero Element*.

## The Eigenbasis of Left Multiplication

**For $R^2\neq0$ the operator $L_{\tilde Q}$ is diagonalisable, with the two eigenvalues $\lambda_+,\lambda_-$ each of multiplicity two; the eigenspaces are the right ideals $\tilde\Pi_\pm\mathbb{B}$, each minimal of complex dimension two. For $R^2=0$ and $\vec Q\neq0$ there is no eigenbasis, and for $\vec Q=0$ every basis is an eigenbasis.**

Let
$$
\vec\Xi=-\frac{i\vec Q}{R},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm iR,
$$
so that $\vec\Xi^2=e_t$, $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_+\tilde\Pi_-=0$, $\tilde\Pi_++\tilde\Pi_-=e_t$, and
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,\qquad
\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm.
$$
The right ideals
$$
\tilde\Pi_+\mathbb{B},\qquad \tilde\Pi_-\mathbb{B}
$$
are the eigenspaces:
$$
\ker(L_{\tilde Q}-\lambda_\pm)=\tilde\Pi_\pm\mathbb{B},
$$
each of complex dimension two, and $\tilde\Pi_\pm$ lies in its own eigenspace.

**Eigenbasis.** A basis of $\mathbb{B}$ is an eigenbasis of $L_{\tilde Q}$ when each of its vectors $b$ satisfies $\tilde Qb=\mu b$ for some scalar $\mu$. When $R^2\neq0$ such a basis exists: it is any pair of bases of the two eigenspaces, for instance $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ for non-zero $\vec\Upsilon_-\in\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ and $\vec\Upsilon_+\in\tilde\Pi_-\mathbb{B}\tilde\Pi_+$. The eigenbasis is not unique: it is determined only up to an invertible change of basis on each eigenspace.

**The two sides.** The minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$ are the eigenspaces of the right multiplication $R_{\tilde Q}$, with eigenvalues $\lambda_\pm$. They are not eigenspaces of $L_{\tilde Q}$: when $R^2\neq0$ each contains one eigenvector for $\lambda_+$ and one for $\lambda_-$.

**Eigenprojection.** The idempotent $\tilde\Pi_+$ is the spectral idempotent of $\lambda_+$, and $L_{\tilde\Pi_+}$ is the spectral projector onto the $\lambda_+$-eigenspace: it sends $X$ to $\tilde\Pi_+X$, with image $\tilde\Pi_+\mathbb{B}$.

**The degenerate side.** If $R^2=0$ and $\vec Q\neq0$, the minimal polynomial is $(X-Q_t)^2$, so $L_{\tilde Q}$ is not diagonalisable and no eigenbasis exists. If $\vec Q=0$ the element is scalar and $L_{\tilde Q}=Q_t\,\mathrm{id}$; every basis is then an eigenbasis.

## The Degenerate Case $Q_x^2+Q_y^2+Q_z^2=0$

**On the cone $R^2=0$ the two eigenvalues have coalesced. Two further questions decide the geometry of a point: whether the scalar part vanishes, and whether the vector part vanishes.**

| regime | condition | spectrum | minimal polynomial | spectral decomposition | the element is |
|---|---|---|---|---|---|
| **scalar** | $\vec Q=0$ | $\{Q_t\}$ | $X-Q_t$ | one term, every idempotent | central, semisimple; a unit iff $Q_t\neq0$ |
| **Jordan** | $R^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\{Q_t\}$ | $(X-Q_t)^2$ | none | a unit, defective, one Jordan block |
| **nilpotent** | $R^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\{0\}$ | $X^2$ | none | a non-unit, $\tilde Q^2=0$ |

### The Scalar Regime and the Vertex

Let $\tilde Q=Q_te_t$. The element is central, its minimal polynomial is $X-Q_t$, and it is semisimple with the single eigenvalue $Q_t$. Every idempotent commutes with it, so every idempotent is available as a spectral idempotent. The spectral decomposition in the sense of the general theory has one term, $\tilde Q=Q_te_t$, and it is unique; a two-term writing with two orthogonal idempotents summing to $e_t$ has the equal coefficient $Q_t$ on both terms and is not determined by $\tilde Q$. This is the only regime in which a two-term writing exists without being a spectral decomposition.

The vertex is the singular locus of $\mathcal S$: it is the line of elements of $\mathcal S$ with the mildest spectral degeneration, where the eigenvalue is repeated but the element still has a spectral decomposition, with one term.

### The Zero Element

**The zero element is degenerate, and it is the one point of the cone that is neither a unit nor a zero divisor.**

At $\tilde Q=0$ one has $R^2=0$ and $Q_t=0$, so $0$ lies in the degenerate case and is the apex of $\mathcal S$: it is the only point at which both the scalar and the vector part vanish. Its spectrum is $\{0\}$, its minimal polynomial is $X$, every idempotent commutes with it, and its spectral decomposition is the one-term writing $0=0\cdot e_t$. Both translations $L_0$ and $R_0$ are the zero map, so both annihilators are all of $\mathbb{B}$ and both ranks are $0$.

### The Jordan Regime

Let $\tilde Q=Q_te_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$, and let $Q_t\neq0$. The minimal polynomial is $(X-Q_t)^2$, the spectrum is the single eigenvalue $Q_t$, and the element is a unit, since $Q_t^2+R^2=Q_t^2\neq0$. Its centraliser is $\mathbb{C}[\tilde Q]=\{ae_t+b\vec\Upsilon\}$, whose only idempotents are $0$ and $e_t$, so no non-trivial idempotent commutes with it and no two-term spectral decomposition exists. The element is a single Jordan block: it is defective, and the two eigenvalues of the non-degenerate side have coalesced at $Q_t$ without the element becoming scalar.

### The Nilpotent Regime

Let $\tilde Q=\vec\Upsilon$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$. The spectrum is $\{0\}$, the minimal polynomial is $X^2$, and the element is not a unit, since $Q_t^2+R^2=0$. The centraliser and the absence of a two-term spectral decomposition are the same as in the Jordan regime.

This regime is the set of non-zero elements with vanishing scalar part and square, with the origin removed.

## Summary

The eigenvalue problem of $\tilde Q$ is governed by the characteristic polynomial $p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+R^2=(X-Q_t)^2+R^2$, whose discriminant is $-4R^2$. The eigenvalues are $Q_t\pm iR$; they are distinct exactly when $R^2\neq0$ and coalesce on the spectral-degenerate cone $\mathcal S$. The cone is the discriminant locus of the problem: it is cut out by the degenerate quadratic form $R^2$, which does not involve $Q_t$.

The spectral problem is stated without a module or an acting operator. An eigenvalue is a scalar for which the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, equivalently for which $\tilde Q-\lambda e_t$ is a non-unit, equivalently for which $(\lambda-Q_t)^2+R^2=0$. The eigenspace is the left annihilator, a right ideal of complex dimension $2$ for a non-scalar element. A spectral idempotent is an idempotent commuting with the element, and on the regular side the spectral decomposition is the pair of Lagrange idempotents. Cayley–Hamilton gives the inverse whenever $Q_t^2+R^2\neq0$, and the unordered spectrum determines the similarity class except at $R=0$, where the scalar class and the non-semisimple class share it, the Jordan class when $Q_t\neq0$ and the nilpotent class when $Q_t=0$.

The cone $\mathcal S$ is $\mathbb{C}e_t$ times the isotropic cone of the vector subspace, of complex dimension $3$ and real dimension $6$. It is smooth off the scalar vertex and singular along it. It is not a subspace, and it is not the set of defective elements: the vertex is semisimple.

On the non-scalar side, a two-term spectral decomposition exists exactly when $R^2\neq0$, and then it is unique. The degenerate side is stratified into the scalar regime, where every idempotent is available and the spectral decomposition has one term; the Jordan regime, where the element is a unit, defective and without a non-trivial commuting idempotent; and the nilpotent regime, where the element is a zero divisor and a nilpotent of index two. The vertex is the scalar line.

The comparison with the invertibility problem is *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*, which also supplies the operator readings. This article has treated the eigenvalue problem alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part |
| $R^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+R^2$ | the characteristic polynomial, equal to $(X-Q_t)^2+R^2$ |
| $\det\mathsf{M}_2(a)=a_t^2+\vec a^2$, for $a=a_te_t+\vec a$ | the determinant of the matrix realization, the invertibility test |
| $\operatorname{disc}p_{\tilde Q}=-4R^2$ | the discriminant |
| $\lambda_\pm=Q_t\pm iR$ | the eigenvalues |
| $\mathcal S=\{R^2=0\}$ | the spectral-degenerate cone |
| $\operatorname{Ann}_{\ell}(a)=\{v:av=0\}$ | the left annihilator, a right ideal |
| $e_\pm=(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$ | the spectral idempotents |
| $\vec\Upsilon$ | a non-zero vector with $\vec\Upsilon^2=0$ |

## Further Reading

- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of the two cones, the five zones, the two decompositions and the two operator loci.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition, the eigenprojections, the degenerate regimes, the Hermitian case and the spectral theorem.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the existence and uniqueness of the spectral decomposition in the general theory.
- [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), for the interpolating idempotents.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block behind the Jordan regime.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the semisimple and nilpotent parts.
