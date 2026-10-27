# __The Spectrum__

## Introduction

The biquaternion algebra carries many quadratic conditions; this article studies one of them, the square of the vector part,

$$
B^2=Q_x^2+Q_y^2+Q_z^2,
$$

which involves no scalar term. This condition decides whether the two eigenvalues of an element can be told apart: the characteristic polynomial is $X^2-2Q_tX+Q_t^2+B^2$, and its discriminant is $-4B^2$. This article defines the eigenvalue problem, proves the spectral criterion, and separates the elements of $\mathbb{B}$ into the two cases of the value of $B^2$: the regular case $B^2\neq0$, where the two eigenvalues are distinct and the element has a unique spectral decomposition, and the degeneracy case $B^2=0$, the spectral-degenerate cone, on which the two eigenvalues coalesce. This article is the study of this one condition and of its two cases.

**Notation.** An element is $\tilde Q=Q_te_t+\vec Q$, its natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, and the product is the plain product of the algebra, associative with the two-sided unit $e_t$. The vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t.
$$

The number $B$ is a fixed complex square root of $B^2$; the other root only exchanges the two eigenvalues. The companion article *N-Regularity and N-Degeneracy in the Biquaternion Algebra* studies the zero-divisor set; this article studies $B^2$ and the spectral cases it defines. The matrix realization $\mathsf{M}_2$ of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure* appears only as a check, through the identity $\det\mathsf{M}_2(\tilde Q)=Q_t^2+B^2$; the criterion is proved without it. The algebra and its conventions are *The Biquaternion Algebra*; the eigenvalue decomposition, the normality criterion and the spectral theorem are *The Biquaternion Eigenvalue Decomposition*.

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
3. $(\lambda-Q_t)^2+B^2=0$.

*Proof.* Write $a=\tilde Q-\lambda e_t=a_te_t+\vec a$, with $a_t=Q_t-\lambda$ and $\vec a=\vec Q$.

*(1)$\iff$(2).* If $a$ is a unit then $\mathbb{B}a=\mathbb{B}$, so the left ideal is not proper. Conversely, if $\mathbb{B}a=\mathbb{B}$ then $e_t=xa$ for some $x$. Left multiplication by $a$ is injective, since $ay=0$ gives $y=xay=0$. In finite dimension an injective endomorphism is bijective, so there is $b$ with $ab=e_t$. Then $a(ba-e_t)=0$, hence $ba=e_t$ by injectivity, and $b$ is a two-sided inverse.

*(2)$\iff$(3).* The conjugate product is

$$
aa^{\natural}=a_t^2-\vec a^2=(a_t^2+B^2)e_t=((\lambda-Q_t)^2+B^2)e_t .
$$

If the scalar is non-zero, then $a^{-1}=a^{\natural}/(a_t^2+B^2)$, so $a$ is a unit. If the scalar is zero, then $aa^{\natural}=0$; for $a\neq0$ this exhibits $a$ as a zero divisor, since $a^{\natural}\neq0$, and $a=0$ is not a unit. So $a$ is a unit exactly when the scalar is non-zero.

**Remark (the determinant in the model).** Under $\mathsf{M}_2$ the element $a=a_te_t+\vec a$ is

$$
\mathsf{M}_2(a)=\begin{pmatrix} a_t-ia_z & -ia_x-a_y\\ -ia_x+a_y & a_t+ia_z\end{pmatrix},
$$

whose determinant is $a_t^2+a_x^2+a_y^2+a_z^2$, the same scalar as above. The determinant is therefore a reading of $(\lambda-Q_t)^2+B^2$ in the model, not the proof of the criterion; the criterion holds without the model.

**Corollary (the characteristic polynomial).** For every scalar $X$,

$$
(X-\tilde Q)(X-\tilde Q^{\natural})=((X-Q_t)^2+B^2)e_t,
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

and they coincide exactly when $B=0$, that is exactly when $B^2=0$. In the model the same polynomial is $\det(\mathsf{M}_2(\tilde Q)-X\mathrm I_2)$.

**Corollary (the eigenspaces).** For a non-scalar $\tilde Q$ and each eigenvalue $\lambda$, the eigenspace $\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)$ is a right ideal of complex dimension $2$. For $\tilde Q=Q_te_t$ the only eigenvalue is $Q_t$, and its eigenspace is all of $\mathbb{B}$.

*Proof.* For $a=\tilde Q-\lambda e_t\neq0$, the eigenspace is the left annihilator of $a$, a right ideal. It is non-zero because $a$ is a zero divisor, and it is proper because $a\neq0$. Every non-zero proper right ideal of $\mathbb{B}$ is minimal of complex dimension $2$, by the ideal theory of *The Minimal Left Ideals*, §*The Two Minimal Left Ideals*. At the scalar the difference $\tilde Q-Q_te_t$ is zero, and its annihilator is all of $\mathbb{B}$.

**Corollary (Cayley–Hamilton and the inverse).** Every $\tilde Q$ satisfies

$$
\tilde Q^2-2Q_t\tilde Q+(Q_t^2+B^2)e_t=0,
$$

and if $Q_t^2+B^2\neq0$ then $\tilde Q^{-1}=(2Q_te_t-\tilde Q)/(Q_t^2+B^2)=\tilde Q^{\natural}/(Q_t^2+B^2)$.

*Proof.* With $\tilde Q=Q_te_t+\vec Q$ and $\vec Q^2=-B^2e_t$, $\tilde Q^2=Q_t^2e_t+2Q_t\vec Q-B^2e_t=2Q_t\tilde Q-(Q_t^2+B^2)e_t$. Multiplying by $2Q_te_t-\tilde Q=\tilde Q^{\natural}$ on either side gives $(Q_t^2+B^2)e_t$.

### The Operator Form of the Criterion

**The discriminant also reads on left multiplication: it decides whether the directional part of the operator is a complex structure or a nilpotent.**

**Proposition (the directional part).** Write $\tilde Q=Q_te_t+\vec Q$. Then

$$
L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec Q},\qquad
R_{\tilde Q}=Q_t\,\mathrm{id}+R_{\vec Q},
$$

and

$$
L_{\vec Q}^{\,2}=R_{\vec Q}^{\,2}=-B^{2}\,\mathrm{id}.
$$

*Proof.* For $X\in\mathbb{B}$, $L_{\vec Q}^{\,2}(X)=\vec Q(\vec QX)=\vec Q^{2}X=-B^{2}X$, because $\vec Q^{2}=-B^{2}e_t$, and $R_{\vec Q}^{\,2}(X)=(X\vec Q)\vec Q=X\vec Q^{2}=-B^{2}X$. The scalar part is central.

**Corollary (the minimal polynomial of the directional part).** The two directional operators have the same minimal polynomial,

$$
m_{L_{\vec Q}}=m_{R_{\vec Q}}=
\begin{cases}
X^{2}+B^{2}, & B^{2}\neq0,\\
X^{2}, & B^{2}=0,\ \vec Q\neq0,\\
X, & \vec Q=0.
\end{cases}
$$

*Proof.* If $B^{2}\neq0$, the polynomial $X^{2}+B^{2}=(X-iB)(X+iB)$ annihilates the operator and is squarefree, because $B\neq0$; a degree-one annihilator would make the operator scalar, which it is not when $\vec Q\neq0$. If $B^{2}=0$ and $\vec Q\neq0$, the square annihilates and the operator is not zero. If $\vec Q=0$, the operator is zero.

**Corollary (the complex structure and the defect).** If $B^{2}\neq0$, then $J=L_{\vec Q}/B$ satisfies $J^{2}=-\mathrm{id}$, and the eigenvalues of $L_{\vec Q}$ are $\pm iB$: the directional part is a complex structure. If $B^{2}=0$ and $\vec Q\neq0$, $L_{\vec Q}$ is nilpotent of index two. Consequently $L_{\tilde Q}$ is semisimple except on $\mathcal S\setminus\{\vec Q=0\}$, where it is defective with minimal polynomial $(X-Q_t)^{2}$ and Jordan type $(2,2)$.

*Proof.* The square of $J$ is $-B^{2}\mathrm{id}/B^{2}=-\mathrm{id}$; the eigenvalues of $L_{\vec Q}$ are the roots $\pm iB$ of $X^{2}+B^{2}$. Translation by $Q_t\mathrm{id}$ preserves semisimplicity and defectivity, and it preserves the Jordan type. In the defective case the minimal polynomial becomes $(X-Q_t)^{2}$; on the scalar stratum it is $X-Q_t$.

**Remark (the commutator form).** The same computation on commutators, $\mathrm{ad}_{\vec Q}^{\,3}=-4B^{2}\mathrm{ad}_{\vec Q}$, is the inner derivation of *Relations between the N Norm and Spectral Regularity and Degeneracy*, §*The Two Operator Loci*, where it is nilpotent exactly on $\mathcal S$.

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

The two cases are collected in the table; the regular row is proved in §*The Spectral Decomposition* and §*The Eigenbasis of Left Multiplication*, the degenerate row in *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Three Strata*.

| case | condition | spectrum | spectral decomposition | eigenbasis |
|---|---|---|---|---|
| **regular** | $B^2\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | two terms, unique | exists |
| **degenerate** | $B^2=0$ | $\{Q_t\}$ | one term iff $\vec Q=0$, none otherwise | every basis iff $\vec Q=0$, none otherwise |

### The Four Minimal Polynomials

**The characteristic polynomial has two coefficients, and the minimal polynomial separates what the characteristic polynomial does not.**

| type | condition | $p_{\tilde Q}$ | $m_{\tilde Q}$ |
|---|---|---|---|
| semisimple, non-scalar | $B^2\neq0$ | $(X-Q_t)^2+B^2$ | $(X-Q_t)^2+B^2$ |
| scalar | $B^2=0$, $\vec Q=0$ | $(X-Q_t)^2$ | $X-Q_t$ |
| Jordan | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $(X-Q_t)^2$ | $(X-Q_t)^2$ |
| nilpotent | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $X^2$ | $X^2$ |

The first row is the spectrally regular case. The second row is the central part of the spectral-degenerate cone, $\vec Q=0$: it is semisimple too, but its semisimplicity comes from the degree-one minimal polynomial, not from distinct roots. The last two rows form the non-central part of the cone, split by the scalar part. The table says what the two-case split does not. The characteristic polynomial cannot separate the scalar case from the Jordan case: both have $(X-Q_t)^2$, and only the minimal polynomial distinguishes them. It also cannot separate the nilpotent case from the origin: both have $X^2$. The two-case split of this article is the coarser reading by $B^2$: the regular case is the non-scalar semisimple row, and the degenerate case contains the scalar, Jordan and nilpotent rows. The classification is the one used in *The Semisimple–Nilpotent Split*.

**Remark (the words).** Unqualified **regular** means **spectrally regular**, $B^2\neq0$, and **degenerate** means **spectrally degenerate**, $B^2=0$; both words are fixed by the discriminant. Degenerate here does not mean defective: the vertex is semisimple, while the other two strata of the spectral-degenerate cone are defective.

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

## The Degenerate Case: The Spectral-Degenerate Cone

**On the spectral-degenerate cone $B^2=0$ the eigenvalues have coalesced, and two questions decide the spectral behaviour of a point: whether the vector part vanishes, and whether the scalar part vanishes.**

### The Spectral-Degenerate Cone

**Definition.** The **spectral-degenerate cone** is

$$
\mathcal S=\{B^2=0\}=\{\vec Q^2=0\}=\{\operatorname{disc}p_{\tilde Q}=0\}.
$$

**Theorem (three readings of one equation).** The equation $B^2=0$ is simultaneously:

- **geometric:** the vector part is isotropic, $Q_x^2+Q_y^2+Q_z^2=0$;
- **algebraic:** the vector part is square-zero, $\vec Q^2=0$, hence nilpotent of index two when it is non-zero;
- **spectral:** the discriminant vanishes, and the two eigenvalues coalesce at $Q_t$.

**Theorem (the geometry).** The spectral-degenerate cone is the product of the scalar line and the isotropic cone of the vector subspace,

$$
\mathcal S=\mathbb{C}e_t\times\{\vec Q\in\operatorname{Vect}(\mathbb{B}):\vec Q^2=0\}.
$$

It is a complex cone of complex dimension $3$ and real dimension $6$. Its singular locus is the **vertex** $\{\vec Q=0\}$, the whole scalar line; off the vertex it is a smooth hypersurface.

*Proof.* The equation $B^2=0$ is one complex equation in the four complex coefficients, homogeneous of degree two. Its gradient with respect to $(Q_t,Q_x,Q_y,Q_z)$ is

$$
(0,\,2Q_x,\,2Q_y,\,2Q_z),
$$

which vanishes exactly when $\vec Q=0$. Off the vertex the gradient is non-zero and the equation cuts a smooth hypersurface, of complex dimension $4-1=3$ and real dimension $8-2=6$. On the vertex the spectral-degenerate cone is $\mathbb{C}e_t\times C$, with $C$ the isotropic cone of $\mathbb{C}^3$, which is singular at its apex; the product is singular along the whole line.

**The strata of the spectral-degenerate cone.** The spectral-degenerate cone has three pieces: the **scalar stratum** $\mathcal S^{\mathrm{s}}=\{\vec Q=0\}$, the vertex; the **nilpotent stratum** $\mathcal S^{\mathrm{n}}=\{\vec Q\neq0,\ Q_t=0\}$; and the **unipotent stratum** $\mathcal S^{\mathrm{u}}=\{\vec Q\neq0,\ Q_t\neq0\}$, with $\mathcal S=\mathcal S^{\mathrm{s}}\sqcup\mathcal S^{\mathrm{n}}\sqcup\mathcal S^{\mathrm{u}}$. The last two form the **Jordan part**, the defective part of the spectral-degenerate cone. Their normal forms, minimal polynomials, ranks, centralisers and spectral data are in *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Three Strata*; how the strata sit inside the four norm–spectrum sectors is in *Relations between the N Norm and Spectral Regularity and Degeneracy*, §*The Four Sectors Compared* and §*The Two Decompositions*.

**Warning (what the spectral-degenerate cone is not).** The equation involves only $\vec Q$: the spectral-degenerate cone is blind to the scalar part, and the whole scalar line lies on it. It is not a subspace, since $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ lie on it while their sum $2\vec e_x$ does not. It is not the set of defective elements: a point of the vertex is semisimple with minimal polynomial $X-Q_t$. The spectral-degenerate cone is exactly the set of elements with a repeated eigenvalue.

**Remark (a zero divisor with a simple spectrum).** The spectral condition is independent of the zero-divisor condition, and the witness is the Hermitian idempotent. Let $\vec u$ be a vector with $\vec u\cdot\vec u=1$, so that $\vec u^{2}=-e_t$, and put

$$
\tilde\Pi=\frac12(e_t+i\vec u).
$$

Then $\tilde\Pi^{2}=\tilde\Pi$, and

$$
\tilde\Pi\tilde\Pi^{\natural}=\Bigl(\frac14+B^{2}(\tilde\Pi)\Bigr)e_t=\Bigl(\frac14-\frac14\Bigr)e_t=0,\qquad
B^{2}(\tilde\Pi)=\frac{i^{2}}{4}(\vec u\cdot\vec u)=-\frac14.
$$

The spectrum is $\{1,0\}$ and the minimal polynomial is $X(X-1)$, which is squarefree: $\tilde\Pi$ is a zero divisor and is spectrally regular. The comparison of the null cone and the spectral-degenerate cone is *Relations between the N Norm and Spectral Regularity and Degeneracy*, §*Independence of the Two Cones*.

### The Isotropic Line and the Flag

**A non-isotropic line splits the space; an isotropic line only flags it.**

Let $(\vec X,\vec Y)=X_xY_x+X_yY_y+X_zY_z$ be the symmetric form on the vector subspace, so that $(\vec Q,\vec Q)=B^{2}$. If $B^{2}\neq0$, the line $\mathbb{C}\vec Q$ is non-isotropic and

$$
\mathbb{C}^{3}=\mathbb{C}\vec Q\oplus\vec Q^{\perp}
$$

is a direct sum of non-degenerate summands, canonical in $\vec Q$. If $B^{2}=0$ and $\vec Q\neq0$, the line is isotropic and $\vec Q\in\vec Q^{\perp}$, so $\mathbb{C}\vec Q+\vec Q^{\perp}=\vec Q^{\perp}$ and the sum is not direct. No complement is determined by $\vec Q$: the canonical objects are the line, the plane $\vec Q^{\perp}$ that contains it, and the flag

$$
0\subset\mathbb{C}\vec Q\subset\vec Q^{\perp}\subset\mathbb{C}^{3}.
$$

On the algebra, $\vec Q^{2}=0$ gives $\operatorname{im}L_{\vec Q}\subseteq\ker L_{\vec Q}$, and both spaces have complex dimension $2$, so they coincide. The canonical flag is

$$
0\subset\mathbb{C}\vec Q\subset\ker L_{\vec Q}=\operatorname{im}L_{\vec Q}\subset\mathbb{B}.
$$

A Jordan basis of $L_{\vec Q}$ needs two vectors outside $\ker L_{\vec Q}$ whose images span the kernel. The quotient $\mathbb{B}/\ker L_{\vec Q}$ is two-dimensional, but no splitting of it is determined by $\vec Q$ alone. The eigenbasis fails on the spectral-degenerate cone for this reason: the isotropic line admits no canonical complement. A canonical complement requires extra data, and the resulting Jordan basis is constructed in *The Jordan Basis of a Spectrally Degenerate Biquaternion*.

## The Similarity Classification

**Definition.** Two biquaternions $\tilde Q_1,\tilde Q_2$ are **similar** if $\tilde Q_2=S\tilde Q_1S^{-1}$ for some unit $S\in\mathbb{B}$.

**Theorem (the classification).**

1. If $B^2\neq0$, the similarity class is determined by the unordered pair of eigenvalues $\{\lambda_+,\lambda_-\}$.
2. If $B^2=0$, the spectrum is the singleton $\{Q_t\}$, and exactly two similarity classes share it: the **central class** $\tilde Q=Q_te_t$, and the **non-semisimple class** $\vec Q\neq0$ with $\vec Q^2=0$, which is similar to the Jordan block $J_2(Q_t)$. At $Q_t=0$ the second class is that of the non-zero nilpotents, $J_2(0)$; at $Q_t\neq0$ it is that of the unipotent scalings $Q_tu$, $J_2(Q_t)$.

*Proof.* (1) The characteristic polynomial has two distinct roots, so $\tilde Q$ is diagonalisable with those roots; two diagonalisable matrices with the same spectrum are conjugate in $M_2(\mathbb{C})\cong\mathbb{B}$, and the spectrum is unordered because the two eigenvalues are exchanged by the choice of $B$. (2) On the spectral-degenerate cone $\vec Q^2=0$. If $\vec Q=0$ the element is central. If $\vec Q\neq0$, then $\tilde Q-Q_te_t$ is non-zero with square $0$, so the minimal polynomial is $(X-Q_t)^2$ and the Jordan form is a single block of size $2$; all non-zero square-zero elements are rank-one nilpotents, hence conjugate.

The unordered spectrum therefore determines the similarity class off the spectral-degenerate cone, and carries no information on it beyond $Q_t$: the discriminant is what separates the central class from the non-semisimple one.

## The Two Cases on the Remarkable Subspaces

**The condition $B^2$ depends only on the vector part, so its restriction to a remarkable subspace is read from the vector coordinates of that subspace.**

| remarkable subspace | real basis | restriction of $B^2$ | elements with $B^2=0$ |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $e_t,\,ie_t$ | $0$ | the whole centre |
| $\operatorname{Vect}(\mathbb{B})$, the vector subspace | $\vec e_k,\,i\vec e_k$ | $\sum_kQ_k^2$ | the isotropic cone, complex dimension $2$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $e_t,\vec e_x,\vec e_y,\vec e_z$ | $q_x^2+q_y^2+q_z^2$ | $\mathbb{R}e_t$ |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $-(q_x^2+q_y^2+q_z^2)$ | $\mathbb{R}ie_t$ |
| $\mathbb{M}_{+}$, the Hermitian subspace | $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $-(a_x^2+a_y^2+a_z^2)$ | $\mathbb{R}e_t$ |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $ie_t,\vec e_x,\vec e_y,\vec e_z$ | $a_x^2+a_y^2+a_z^2$ | $\mathbb{R}ie_t$ |

**Corollary.** Every element of the centre is spectrally degenerate, and the centre is the only remarkable subspace contained in $\mathcal S$. On the quaternion and anti-Hermitian subspaces $B^2$ is a sum of squares, on the anti-quaternion and Hermitian subspaces it is the negative of a sum of squares; in each case the zero set is the real or the imaginary scalar line. Only on the vector subspace is the condition a genuine cone, the isotropic cone of complex dimension $2$ and real dimension $4$.

*Proof.* The values are read from the displayed real bases: on the centre all three vector coefficients vanish; on $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ the coefficients $Q_k$ are real or purely imaginary; on $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ the scalar coefficient is real or purely imaginary and the vector coefficients are purely imaginary or real. Each non-central restriction is a sum of three squares with a sign, so its zero set is the scalar line of the subspace.

**Corollary (the strata on the remarkable subspaces).** The centre and the four real-type subspaces meet only the scalar stratum; the vector subspace meets the scalar stratum at the origin and the nilpotent stratum elsewhere; the unipotent stratum meets none of the remarkable subspaces.

*Proof.* On the centre and on the four real-type subspaces, $B^2=0$ forces $\vec Q=0$, so the point is scalar. On the vector subspace $Q_t=0$ by construction, so a point of $\mathcal S$ there is the origin or a nilpotent. The unipotent stratum requires $Q_t\neq0$ and $\vec Q\neq0$ together, and no remarkable subspace carries both coordinates.

## Summary

The biquaternion algebra carries many quadratic conditions; the one studied here is the square of the vector part, $B^2=Q_x^2+Q_y^2+Q_z^2$, which involves no scalar term. It decides whether the two eigenvalues of an element can be told apart: the characteristic polynomial is $X^2-2Q_tX+Q_t^2+B^2$, of discriminant $-4B^2$, with eigenvalues $Q_t\pm iB$.

The eigenvalue problem is stated without a module and without an acting operator: an eigenvalue is a scalar for which the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, an eigenvector lies in the left annihilator, and a spectral idempotent is an idempotent commuting with the element. The criterion proves that $\lambda$ is an eigenvalue exactly when $\tilde Q-\lambda e_t$ is a non-unit, exactly when $(\lambda-Q_t)^2+B^2=0$. The determinant of the matrix model is the same scalar, not the proof; the proof is the conjugate product $a a^{\natural}=(a_t^2+B^2)e_t$. The eigenspace of a non-scalar element has complex dimension $2$; Cayley–Hamilton gives the inverse whenever the determinant does not vanish. The same condition reads on the operators: $L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec Q}$ and $R_{\tilde Q}=Q_t\,\mathrm{id}+R_{\vec Q}$, with $L_{\vec Q}^{\,2}=R_{\vec Q}^{\,2}=-B^2\,\mathrm{id}$. Off the spectral-degenerate cone the directional part is a complex structure; on the spectral-degenerate cone it is nilpotent.

The regular case is $B^2\neq0$. The eigenvalues are distinct, the element is semisimple, and its left multiplication is diagonalisable. The spectral idempotents are the Lagrange idempotents $\tilde\Pi_\pm=(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$, which coincide with $(e_t\pm\vec\Xi)/2$ for $\vec\Xi=-i\vec Q/B$; the decomposition is unique, and an eigenbasis exists with diagonal values $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$.

The degeneracy case is the spectral-degenerate cone $B^2=0$, of complex dimension $3$ and real dimension $6$, the product of the scalar line and the isotropic cone of the vector subspace, smooth off the scalar vertex. On it the two eigenvalues have coalesced at $Q_t$. The spectral-degenerate cone splits into the scalar vertex and the Jordan part, the latter carrying the nilpotent and unipotent strata; their normal forms, minimal polynomials, ranks, centralisers and spectral data are in *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Three Strata*. The condition is blind to the scalar part, so the whole centre is degenerate, and no case is stable under multiplication. The spectral condition and the zero-divisor condition are independent: a Hermitian idempotent has $B^2=-\tfrac14$ and is a zero divisor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2$ | the characteristic polynomial, equal to $(X-Q_t)^2+B^2$ |
| $m_{\tilde Q}$ | the minimal polynomial of $\tilde Q$ |
| $a a^{\natural}=(a_t^2+B_a^2)e_t$ | the conjugate product, the intrinsic invertibility test |
| $\det\mathsf{M}_2(a)=a_t^2+a_x^2+a_y^2+a_z^2$ | the same scalar in the matrix model |
| $\operatorname{disc}p_{\tilde Q}=-4B^2$ | the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathcal S^{\mathrm{s}},\ \mathcal S^{\mathrm{n}},\ \mathcal S^{\mathrm{u}}$ | the scalar, nilpotent and unipotent strata of $\mathcal S$ |
| $L_{\tilde Q}(X)=\tilde QX,\ R_{\tilde Q}(X)=X\tilde Q$ | left and right multiplication |
| $\operatorname{Ann}_{\ell}(a)=\{v:av=0\}$ | the left annihilator, a right ideal |
| $\vec\Xi=-i\vec Q/B$ | the pure root, with $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$ | the spectral idempotents, equal to $(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$ |

## Further Reading

- [The Jordan–Chevalley Decomposition of a Biquaternion](the-jordan-chevalley-decomposition-of-a-biquaternion.html), for the four types as the semisimple and nilpotent split, the Peirce corner pattern and the multiplicative form.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the construction, the normalisation, the expansion of every biquaternion and the spinor reading.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of the null cone and the spectral-degenerate cone, the four sectors, the two decompositions and the two operator loci.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the unipotent stratum inside the unit group.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the nilpotent stratum and the origin.
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), for the sector as a whole: the equation, the three strata, the geometry and the Jordan basis.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition, the eigenprojections, the degenerate regimes, the Hermitian case and the spectral theorem.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the existence and uniqueness of the spectral decomposition in the general theory.
- [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), for the interpolating idempotents.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block behind the non-semisimple class.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the semisimple and nilpotent parts.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the characteristic polynomial, diagonalisability and the Jordan form.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (2nd edition, Prentice-Hall, 1971), for the spectral theorem over $\mathbb{C}$ and the primary decomposition.
