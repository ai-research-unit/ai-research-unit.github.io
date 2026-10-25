# __Spectral Regularity and Degeneracy in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries a second quadratic condition, the square of the vector part,

$$
B^2=Q_x^2+Q_y^2+Q_z^2,
$$

which involves no scalar term. It alone decides whether the two eigenvalues of an element can be told apart: the characteristic polynomial is $X^2-2Q_tX+Q_t^2+B^2$, and its discriminant is $-4B^2$. This article defines the eigenvalue problem, proves the spectral criterion, and separates the elements of $\mathbb{B}$ into the two cases of the value of $B^2$: the regular case $B^2\neq0$, where the two eigenvalues are distinct and the element has a unique spectral decomposition, and the degeneracy case $B^2=0$, the spectral-degenerate cone, on which the two eigenvalues coalesce. This article is the study of this one condition and of its two cases.

**Notation.** An element is $\tilde Q=Q_te_t+\vec Q$, its natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, and the product is the plain product of the algebra, associative with the two-sided unit $e_t$. The vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t.
$$

The number $B$ is a fixed complex square root of $B^2$; the other root only exchanges the two eigenvalues. The companion article *N-Regularity and Degeneracy in the Biquaternion Algebra* studies the multiplicative norm and its two cases; this article studies $B^2$ and does not use that norm. The matrix realization $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* is used only to compute the determinant $\det\mathsf{M}_2(\tilde Q)=Q_t^2+B^2$. The algebra and its conventions are *The Biquaternion Algebra and Its Vector Spaces*; the eigenvalue decomposition, the normality criterion and the spectral theorem are *The Biquaternion Eigenvalue Decomposition*.

## The Spectral Criterion

**An eigenvalue is a scalar for which a left ideal is proper, and the criterion turns that definition into a single polynomial equation.**

**Definition (eigenvalue).** A scalar $\lambda\in\mathbb{C}$ is an **eigenvalue** of $\tilde Q$ if the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, that is $\mathbb{B}(\tilde Q-\lambda e_t)\neq\mathbb{B}$.

**Definition (eigenvector).** A non-zero $v\in\mathbb{B}$ is an **eigenvector** of $\tilde Q$ for $\lambda$ if $(\tilde Q-\lambda e_t)v=0$. The eigenvectors for $\lambda$, with the origin, are the left annihilator

$$
\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)=\{v:\ (\tilde Q-\lambda e_t)v=0\},
$$

which is a right ideal of $\mathbb{B}$.

**Definition (spectral idempotent).** A non-zero idempotent $e$ is a **spectral idempotent** of $\tilde Q$ if $e\tilde Q=\tilde Qe=\lambda e$ for some scalar $\lambda$.

**Theorem (the spectral criterion).** For $\tilde Q\in\mathbb{B}$ and $\lambda\in\mathbb{C}$, the following are equivalent:

1. $\lambda$ is an eigenvalue of $\tilde Q$;
2. $\tilde Q-\lambda e_t$ is not a unit of the plain product;
3. $\det\mathsf{M}_2(\tilde Q-\lambda e_t)=0$;
4. $(\lambda-Q_t)^2+B^2=0$.

*Proof.* Write $a=\tilde Q-\lambda e_t$.

*(1)$\iff$(2).* If $a$ is a unit then $\mathbb{B}a=\mathbb{B}$, so the left ideal is not proper. Conversely, if $\mathbb{B}a=\mathbb{B}$ then $e_t=xa$ for some $x$. Left multiplication by $a$ is injective, since $ay=0$ gives $y=xay=0$. In finite dimension an injective endomorphism is bijective, so there is $b$ with $ab=e_t$. Then $a(ba-e_t)=0$, hence $ba=e_t$ by injectivity, and $b$ is a two-sided inverse.

*(2)$\iff$(3).* The isomorphism $\mathsf{M}_2$ turns the plain product into the matrix product, so $a$ is a unit exactly when $\mathsf{M}_2(a)$ is invertible, and a square matrix over a field is invertible exactly when its determinant is non-zero.

*(3)$\iff$(4).* For $a=a_te_t+\vec a$ the matrix is

$$
\mathsf{M}_2(a)=\begin{pmatrix} a_t-ia_z & -ia_x-a_y\\ -ia_x+a_y & a_t+ia_z\end{pmatrix},
$$

whose determinant is $a_t^2+a_x^2+a_y^2+a_z^2$. With $a_t=Q_t-\lambda$ and $\vec a=\vec Q$ this is $(\lambda-Q_t)^2+B^2$.

**Corollary (the characteristic polynomial).** For every $\lambda$,

$$
\det\mathsf{M}_2(\tilde Q-\lambda e_t)=(\lambda-Q_t)^2+B^2,
$$

so the characteristic polynomial is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2,
$$

of discriminant

$$
\operatorname{disc}p_{\tilde Q}=4Q_t^2-4(Q_t^2+B^2)=-4B^2.
$$

The eigenvalues are

$$
\lambda_\pm=Q_t\pm iB,
$$

and they coincide exactly when $B=0$, that is exactly when $B^2=0$.

**Corollary (the eigenspaces).** For a non-scalar $\tilde Q$ and each eigenvalue $\lambda$, the eigenspace $\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)$ is a right ideal of complex dimension $2$. For $\tilde Q=Q_te_t$ the only eigenvalue is $Q_t$, and its eigenspace is all of $\mathbb{B}$.

*Proof.* A non-zero non-unit of $\mathbb{B}$ is a matrix of rank one in $\mathsf{M}_2$, and left multiplication by a rank-one matrix has rank $2$; hence the kernel has complex dimension $4-2=2$. At the scalar the difference $\tilde Q-Q_te_t$ is zero.

**Corollary (Cayley–Hamilton and the inverse).** Every $\tilde Q$ satisfies

$$
\tilde Q^2-2Q_t\tilde Q+(Q_t^2+B^2)e_t=0,
$$

and if $Q_t^2+B^2\neq0$ then $\tilde Q^{-1}=(2Q_te_t-\tilde Q)/(Q_t^2+B^2)=\tilde Q^{\natural}/(Q_t^2+B^2)$.

*Proof.* With $\tilde Q=Q_te_t+\vec Q$ and $\vec Q^2=-B^2e_t$, $\tilde Q^2=Q_t^2e_t+2Q_t\vec Q-B^2e_t=2Q_t\tilde Q-(Q_t^2+B^2)e_t$. Multiplying by $2Q_te_t-\tilde Q=\tilde Q^{\natural}$ on either side gives $(Q_t^2+B^2)e_t$.

**Remark (left and right eigenvalues).** The centre of $\mathbb{B}$ is $\mathbb{C}$, so complex scalars commute with every element. A left eigenvalue, $\tilde Qv=\lambda v$, and a right eigenvalue, $\tilde Qv=v\lambda$, therefore define the same set when the scalar is required to lie in $\mathbb{C}$, and that set is $\sigma(\tilde Q)$. The distinction between the two eigenvalue problems, which is genuine over a noncommutative division ring (*Quaternion Spectral Theory*, §*The Spectrum of a Quaternion*), collapses here.

## The Two Cases

**The discriminant of the characteristic polynomial is $-4B^2$, and its vanishing, and nothing else, separates the algebra into two spectral cases.**

**Definition (spectral decomposition).** A **spectral decomposition** of $\tilde Q$ is either the one-term writing $\tilde Q=Q_te_t$ when $\tilde Q$ is scalar, or a two-term writing

$$
\tilde Q=\lambda_+e_++\lambda_-e_-,
$$

where $\lambda_+\neq\lambda_-$ and $e_+,e_-$ are non-zero idempotents with

$$
e_+^2=e_+,\qquad e_-^2=e_-,\qquad e_+e_-=e_-e_+=0,\qquad e_++e_-=e_t.
$$

The scalars $\lambda_\pm$ are the eigenvalues and the idempotents $e_\pm$ are the **spectral idempotents**.

**Criterion (four descriptions).** For a non-scalar $\tilde Q$ the following are equivalent:

1. $B^2\neq0$;
2. the eigenvalues are distinct;
3. $\tilde Q$ is semisimple;
4. $L_{\tilde Q}$ is diagonalisable.

*Proof.* (1)$\iff$(2): the eigenvalues are $Q_t\pm iB$, and they are distinct exactly when $B\neq0$. (2)$\iff$(3): for a non-scalar element the minimal polynomial is the characteristic polynomial $(X-Q_t)^2+B^2$, of degree two, since a degree-one minimal polynomial would make the element scalar; it is squarefree exactly when its two roots are distinct. (3)$\iff$(4): the left regular representation is faithful and carries $\mathbb{C}[\tilde Q]$ isomorphically onto $\mathbb{C}[L_{\tilde Q}]$, so $\tilde Q$ and $L_{\tilde Q}$ have the same minimal polynomial, and an operator is diagonalisable exactly when that polynomial is squarefree.

The two cases are collected in the table; the last two columns are proved in §*The Spectral Decomposition* and §*The Eigenbasis of Left Multiplication*.

| case | condition | spectrum | spectral decomposition | eigenbasis |
|---|---|---|---|---|
| **regular** | $B^2\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | two terms, unique | exists |
| **degenerate** | $B^2=0$ | $\{Q_t\}$ | one term iff $\vec Q=0$, none otherwise | every basis iff $\vec Q=0$, none otherwise |

**Remark (the words).** Unqualified **regular** means **spectrally regular**, $B^2\neq0$, and **degenerate** means **spectrally degenerate**, $B^2=0$; both words are fixed by the discriminant, as **norm-regular** and **norm-degenerate** are fixed by the value of the norm in the companion article. Degenerate here does not mean defective: the vertex is semisimple. The comparison with the norm is *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*.

**Remark (the condition is not multiplicative).** Neither case is stable under the product. Two elements of $B^2=0$ can multiply to an element of $B^2\neq0$: both factors of

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2i\vec e_z
$$

have $B^2=0$, and the product has $B^2=-4$. Two elements of $B^2\neq0$ can multiply to an element of $B^2=0$: both factors of

$$
(e_t+\vec e_x)(e_t-\vec e_x)=2e_t
$$

have $B^2=1$, and the product has $B^2=0$. So the regular case is not a subgroup, and the spectral condition is not preserved by multiplication in either direction.

## The Regular Case: Distinct Eigenvalues

**When $B^2\neq0$ the two eigenvalues are distinct, the spectral idempotents are the Lagrange idempotents, and the decomposition is unique.**

### The Spectral Decomposition

**Theorem (existence).** Let $B^2\neq0$ and put

$$
\vec\Xi=-\frac{i\vec Q}{B},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm iB.
$$

Then $\tilde\Pi_\pm$ are non-zero idempotents with $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$, and

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,\qquad
\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm.
$$

*Proof.* Since $\vec Q^2=-B^2e_t$, one has $\vec\Xi^2=e_t$ and $\vec Q=iB\vec\Xi$. Hence $\tilde\Pi_\pm^2=(e_t\pm2\vec\Xi+e_t)/4=\tilde\Pi_\pm$ and $\tilde\Pi_+\tilde\Pi_-=(e_t-\vec\Xi^2)/4=0$, and the sum is $e_t$. The idempotents are non-zero because $\vec\Xi$ has zero scalar part, so $\vec\Xi\neq\pm e_t$. For the action, $\vec Q\vec\Xi=(-i/B)\vec Q^2=iBe_t$, hence

$$
\tilde Q\tilde\Pi_+=\frac{(Q_t e_t+\vec Q)(e_t+\vec\Xi)}{2}
=\frac{(Q_t+iB)(e_t+\vec\Xi)}{2}=\lambda_+\tilde\Pi_+,
$$

and $\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-$ the same way. Adding the two identities multiplied by the eigenvalues gives the decomposition.

**Corollary (Lagrange form).** The idempotents are the Lagrange idempotents,

$$
\tilde\Pi_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},
$$

and the spectral decomposition is unique.

*Proof.* The first identity is the computation $\tilde Q-\lambda_-=iB(e_t+\vec\Xi)$, and its analogue with the signs exchanged. For uniqueness, the minimal polynomial $(X-\lambda_+)(X-\lambda_-)$ has distinct roots, so the Chinese remainder theorem gives $\mathbb{C}[\tilde Q]\cong\mathbb{C}[X]/((X-\lambda_+)(X-\lambda_-))\cong\mathbb{C}\times\mathbb{C}$; the idempotents of that product are $0,e_t,\tilde\Pi_+,\tilde\Pi_-$, and every spectral idempotent lies in the centraliser $\mathbb{C}[\tilde Q]$.

**Corollary (spectral projectors).** $L_{\tilde\Pi_+}$ is the projector onto the $\lambda_+$-eigenspace: it sends $X$ to $\tilde\Pi_+X$, with image $\tilde\Pi_+\mathbb{B}$ and kernel $\tilde\Pi_-\mathbb{B}$. The same statement holds with the two signs exchanged.

### The Eigenbasis of Left Multiplication

**Theorem (the eigenspaces).** For $B^2\neq0$ and each sign,

$$
\ker(L_{\tilde Q}-\lambda_\pm)=\tilde\Pi_\pm\mathbb{B},
$$

a right ideal of complex dimension $2$. Each eigenvalue therefore has multiplicity two.

*Proof.* Since $\tilde Q-\lambda_+=iB(\vec\Xi-e_t)=-2iB\tilde\Pi_-$, the equation $(\tilde Q-\lambda_+)X=0$ is $\tilde\Pi_-X=0$, that is $X=\tilde\Pi_+X$, that is $X\in\tilde\Pi_+\mathbb{B}$. In a basis in which $\tilde\Pi_+=\operatorname{diag}(1,0)$, the ideal $\tilde\Pi_+\mathbb{B}$ is the set of matrices whose second row vanishes, of complex dimension $2$.

**Corollary (eigenbasis).** Choose non-zero $\vec\Upsilon_-\in\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ and $\vec\Upsilon_+\in\tilde\Pi_-\mathbb{B}\tilde\Pi_+$. Then

$$
(\tilde\Pi_+,\ \vec\Upsilon_-,\ \vec\Upsilon_+,\ \tilde\Pi_-)
$$

is an eigenbasis of $L_{\tilde Q}$, with diagonal values $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$. An eigenbasis is any pair of bases of the two eigenspaces, so it is determined only up to an invertible change of basis on each.

*Proof.* The mixed corners are one-dimensional, and $\vec\Upsilon_-\in\tilde\Pi_+\mathbb{B}$ while $\vec\Upsilon_+\in\tilde\Pi_-\mathbb{B}$, so the four vectors form a basis of the two eigenspaces and hence of $\mathbb{B}$.

**Remark (the two sides).** The minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$ are the eigenspaces of the right multiplication $R_{\tilde Q}$, with eigenvalues $\lambda_\pm$. They are not eigenspaces of $L_{\tilde Q}$: $S_+$ contains $\tilde\Pi_+$ and $\vec\Upsilon_+$, with eigenvalues $\lambda_+$ and $\lambda_-$, and $S_-$ contains $\tilde\Pi_-$ and $\vec\Upsilon_-$, with eigenvalues $\lambda_-$ and $\lambda_+$. The eigenbasis above is an eigenbasis of left multiplication, not of right multiplication.

**Remark (the degenerate side).** If $B^2=0$ and $\vec Q\neq0$, the minimal polynomial is $(X-Q_t)^2$, the eigenspace has dimension $2$, and no eigenbasis exists. If $\vec Q=0$ the element is scalar and $L_{\tilde Q}=Q_t\,\mathrm{id}$; every basis is then an eigenbasis.

## The Degenerate Case: The Cone

**On the cone $B^2=0$ the eigenvalues have coalesced, and one further question decides the spectral behaviour of a point: whether the vector part vanishes.**

### The Spectral-Degenerate Cone

**Definition.** The **spectral-degenerate cone** is

$$
\mathcal S=\{B^2=0\}=\{\vec Q^2=0\}=\{\operatorname{disc}p_{\tilde Q}=0\}.
$$

**Theorem (three readings of one equation).** The equation $B^2=0$ is simultaneously:

- **geometric:** the vector part is isotropic, $Q_x^2+Q_y^2+Q_z^2=0$;
- **algebraic:** the vector part is square-zero, $\vec Q^2=0$, hence nilpotent of index two when it is non-zero;
- **spectral:** the discriminant vanishes, and the two eigenvalues coalesce at $Q_t$.

**Theorem (the geometry).** The cone is the product of the scalar line and the isotropic cone of the vector subspace,

$$
\mathcal S=\mathbb{C}e_t\times\{\vec Q\in\operatorname{Vect}(\mathbb{B}):\vec Q^2=0\}.
$$

It is a complex cone of complex dimension $3$ and real dimension $6$. Its singular locus is the **vertex** $\{\vec Q=0\}$, the whole scalar line; off the vertex it is a smooth hypersurface.

*Proof.* The equation $B^2=0$ is one complex equation in the four complex coefficients, homogeneous of degree two. Its gradient with respect to $(Q_t,Q_x,Q_y,Q_z)$ is

$$
(0,\,2Q_x,\,2Q_y,\,2Q_z),
$$

which vanishes exactly when $\vec Q=0$. Off the vertex the gradient is non-zero and the equation cuts a smooth hypersurface, of complex dimension $4-1=3$ and real dimension $8-2=6$. On the vertex the cone is $\mathbb{C}e_t\times C$, with $C$ the isotropic cone of $\mathbb{C}^3$, which is singular at its apex; the product is singular along the whole line.

**Warning (what the cone is not).** The equation involves only $\vec Q$: the cone is blind to the scalar part, and the whole scalar line lies on it. It is not a subspace, since $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ lie on it while their sum $2\vec e_x$ does not. It is not the set of defective elements: a point of the vertex is semisimple with minimal polynomial $X-Q_t$. The cone is exactly the set of elements with a repeated eigenvalue.

### The Behaviour on the Cone

**Theorem (the vertex and its complement).** Let $\tilde Q=Q_te_t+\vec Q\in\mathcal S$.

- **At the vertex**, $\vec Q=0$: the element is the scalar $Q_te_t$, its minimal polynomial is $X-Q_t$, its spectrum is $\{Q_t\}$ and it is semisimple. Every idempotent commutes with it, the spectral decomposition is the one-term writing $\tilde Q=Q_te_t$, and every basis is an eigenbasis.
- **Off the vertex**, $\vec Q\neq0$: the vector part is square-zero, the minimal polynomial is $(X-Q_t)^2$, the spectrum is $\{Q_t\}$ and the element is defective. Its eigenspace is $\ker(L_{\vec Q})$, of complex dimension $2$, and no two-term spectral decomposition or eigenbasis exists.

*Proof.* At the vertex the difference $\tilde Q-Q_te_t$ vanishes. Off it, $\vec Q^2=0$ and $\vec Q\neq0$, so $(\tilde Q-Q_te_t)^2=0$ while $\tilde Q-Q_te_t\neq0$; the minimal polynomial therefore divides $(X-Q_t)^2$ and is not $X-Q_t$, hence equals $(X-Q_t)^2$. A minimal polynomial with a repeated root is not squarefree, so the element is defective. Since $Q_te_t$ is central, the centraliser of $\tilde Q$ is the centraliser of $\vec Q$, namely the dual numbers $\mathbb{C}[\vec Q]=\{ae_t+b\vec Q\}$, whose only idempotents are $0$ and $e_t$; hence there is no non-trivial spectral idempotent and no two-term spectral decomposition. The eigenspace is $\ker(L_{\vec Q})$, and left multiplication by a non-zero square-zero element has rank $2$, so the kernel has complex dimension $2$; since $2<4$, no eigenbasis exists.

The two behaviours are collected in the table.

| point of the cone | condition | spectrum | minimal polynomial | spectral decomposition | eigenspace |
|---|---|---|---|---|---|
| **vertex** | $B^2=0$, $\vec Q=0$ | $\{Q_t\}$ | $X-Q_t$ | one term | all of $\mathbb{B}$, every basis |
| **off the vertex** | $B^2=0$, $\vec Q\neq0$ | $\{Q_t\}$ | $(X-Q_t)^2$ | none | $\ker(L_{\vec Q})$, complex dimension $2$, no eigenbasis |

**Remark (no further spectral split).** The distinguishing condition of the table is $\vec Q$, not $Q_t$: the vertex is the whole scalar line, and every point of it has the same spectral behaviour whatever the value of $Q_t$; off the vertex the minimal polynomial is $(X-Q_t)^2$ for every $Q_t$. The type of the minimal polynomial distinguishes the vertex from its complement and nothing finer.

## The Similarity Classification

**Definition.** Two biquaternions $\tilde Q_1,\tilde Q_2$ are **similar** if $\tilde Q_2=S\tilde Q_1S^{-1}$ for some unit $S\in\mathbb{B}$.

**Theorem (the classification).**

1. If $B^2\neq0$, the similarity class is determined by the unordered pair of eigenvalues $\{\lambda_+,\lambda_-\}$.
2. If $B^2=0$, the spectrum is the singleton $\{Q_t\}$, and exactly two similarity classes share it: the **central class** $\tilde Q=Q_te_t$, and the **non-semisimple class** $\vec Q\neq0$ with $\vec Q^2=0$, which is similar to the Jordan block $J_2(Q_t)$.

*Proof.* (1) The characteristic polynomial has two distinct roots, so $\tilde Q$ is diagonalisable with those roots; two diagonalisable matrices with the same spectrum are conjugate in $M_2(\mathbb{C})\cong\mathbb{B}$, and the spectrum is unordered because the two eigenvalues are exchanged by the choice of $B$. (2) On the cone $\vec Q^2=0$. If $\vec Q=0$ the element is central. If $\vec Q\neq0$, then $\tilde Q-Q_te_t$ is non-zero with square $0$, so the minimal polynomial is $(X-Q_t)^2$ and the Jordan form is a single block of size $2$; all non-zero square-zero elements are rank-one nilpotents, hence conjugate.

The unordered spectrum therefore determines the similarity class off the cone, and carries no information on it beyond $Q_t$: the discriminant is what separates the central class from the non-semisimple one.

## The Two Cases on the Remarkable Subspaces

**The condition $B^2$ depends only on the vector part, so its restriction to a remarkable subspace is read from the vector coordinates of that subspace.**

| remarkable subspace | real basis | restriction of $B^2$ | elements with $B^2=0$ |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $e_t,\,ie_t$ | $0$ | the whole centre |
| $\operatorname{Vect}(\mathbb{B})$, the vector subspace | $\vec e_k,\,i\vec e_k$ | $\sum_kQ_k^2$, realified signature $(3,3)$ | the isotropic cone, complex dimension $2$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $e_t,\vec e_x,\vec e_y,\vec e_z$ | $q_x^2+q_y^2+q_z^2$ | $\mathbb{R}e_t$ |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $-(q_x^2+q_y^2+q_z^2)$ | $\mathbb{R}ie_t$ |
| $\mathbb{M}_{+}$, the Hermitian subspace | $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $-(a_x^2+a_y^2+a_z^2)$ | $\mathbb{R}e_t$ |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $ie_t,\vec e_x,\vec e_y,\vec e_z$ | $a_x^2+a_y^2+a_z^2$ | $\mathbb{R}ie_t$ |

**Corollary.** Every element of the centre is spectrally degenerate, and the centre is the only remarkable subspace contained in $\mathcal S$. On the quaternion and anti-Hermitian subspaces the condition is positive semidefinite, on the anti-quaternion and Hermitian subspaces negative semidefinite; in each case the zero set is the real or the imaginary scalar line. Only on the vector subspace is the condition a genuine cone, the isotropic cone of complex dimension $2$ and real dimension $4$.

*Proof.* The values are read from the displayed real bases: on the centre all three vector coefficients vanish; on $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ the coefficients $Q_k$ are real or purely imaginary; on $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ the scalar coefficient is real or purely imaginary and the vector coefficients are purely imaginary or real. Each non-central restriction is a sum of three squares with a sign, so its zero set is the scalar line of the subspace.

## Summary

The biquaternion algebra carries a second quadratic condition, the square of the vector part, $B^2=Q_x^2+Q_y^2+Q_z^2$, which involves no scalar term. It decides whether the two eigenvalues of an element can be told apart: the characteristic polynomial is $X^2-2Q_tX+Q_t^2+B^2$, of discriminant $-4B^2$, with eigenvalues $Q_t\pm iB$.

The eigenvalue problem is stated without a module and without an acting operator: an eigenvalue is a scalar for which the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, an eigenvector lies in the left annihilator, and a spectral idempotent is an idempotent commuting with the element. The criterion proves that $\lambda$ is an eigenvalue exactly when $\tilde Q-\lambda e_t$ is a non-unit, exactly when $\det\mathsf{M}_2(\tilde Q-\lambda e_t)=0$, exactly when $(\lambda-Q_t)^2+B^2=0$. The eigenspace of a non-scalar element has complex dimension $2$; Cayley–Hamilton gives the inverse whenever the determinant does not vanish.

The regular case is $B^2\neq0$. The eigenvalues are distinct, the element is semisimple, and its left multiplication is diagonalisable. The spectral idempotents are the Lagrange idempotents $\tilde\Pi_\pm=(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$, which coincide with $(e_t\pm\vec\Xi)/2$ for $\vec\Xi=-i\vec Q/B$; the decomposition is unique, and an eigenbasis exists with diagonal values $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$.

The degeneracy case is the cone $B^2=0$, of complex dimension $3$ and real dimension $6$, the product of the scalar line and the isotropic cone of the vector subspace, smooth off the scalar vertex. On it the two eigenvalues have coalesced at $Q_t$. The spectral behaviour is uniform along the whole vertex: the element is scalar and semisimple, every idempotent commutes with it, and the decomposition has one term. Off the vertex the minimal polynomial is $(X-Q_t)^2$, the element is defective, the eigenspace has complex dimension $2$, and no two-term spectral decomposition or eigenbasis exists. The unordered spectrum determines the similarity class off the cone; on the cone it distinguishes only the central class from the non-semisimple one. The condition is blind to the scalar part, so the whole centre is degenerate, and no case is stable under multiplication. The comparison with the norm is *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2$ | the characteristic polynomial, equal to $(X-Q_t)^2+B^2$ |
| $\det\mathsf{M}_2(a)=a_t^2+a_x^2+a_y^2+a_z^2$, for $a=a_te_t+\vec a$ | the determinant of the matrix realization, the invertibility test |
| $\operatorname{disc}p_{\tilde Q}=-4B^2$ | the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\operatorname{Ann}_{\ell}(a)=\{v:av=0\}$ | the left annihilator, a right ideal |
| $\vec\Xi=-i\vec Q/B$ | the pure root, with $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$ | the spectral idempotents, equal to $(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$ |

## Further Reading

- [Spectral Regularity and Construction of the Eigenbasis of a Biquaternion](spectral-regularity-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the construction, the normalisation, the expansion of every biquaternion and the spinor reading.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of the two cones, the four sectors, the two decompositions and the two operator loci.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition, the eigenprojections, the degenerate regimes, the Hermitian case and the spectral theorem.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the existence and uniqueness of the spectral decomposition in the general theory.
- [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), for the interpolating idempotents.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block behind the non-semisimple class.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the semisimple and nilpotent parts.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the characteristic polynomial, diagonalisability and the Jordan form.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (2nd edition, Prentice-Hall, 1971), for the spectral theorem over $\mathbb{C}$ and the primary decomposition.
