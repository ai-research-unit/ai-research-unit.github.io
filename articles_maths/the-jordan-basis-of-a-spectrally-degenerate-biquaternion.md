# __The Jordan Basis of a Spectrally Degenerate Biquaternion__

## Introduction

The biquaternion algebra carries many quadratic conditions. Two of them organise this article. The first is the determinant $\det\tilde Q=Q_t^2+B^2$, whose zero set is the null cone. The second is the square of the vector part,

$$
B^2=Q_x^2+Q_y^2+Q_z^2,
$$

whose zero set is the **spectrally degenerate sector**

$$
\mathcal S=\{B^2=0\}.
$$

This article studies that sector and the spectral basis it carries. On the complement $B^2\neq0$ the two eigenvalues are distinct, and *The Eigenbasis of a Spectrally Regular Biquaternion* builds an eigenbasis. On $\mathcal S$ they coincide; on its defective part no eigenbasis exists, because the eigenspace has complex dimension two and four eigenvectors cannot be found. The root $\vec\Xi=-i\vec Q/B$ of the regular construction diverges at $B=0$, and the two spectral idempotents have no limit.

The sector is not without a basis. Off the scalar line the element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$ and $\vec Q\neq0$, and the **flag** replaces the root. It selects a complete orthogonal pair of idempotents $\tilde\Pi_\pm$, and with them the two corner generators $\vec\Upsilon_\pm$; the pair is chosen, and the Jordan form does not depend on the choice. The quadruple

$$
\mathcal{J}(\tilde Q)=(\vec\Upsilon_-,\ \tilde\Pi_-,\ \tilde\Pi_+,\ \vec\Upsilon_+),
$$

listed chain by chain, is then a basis of the algebra, a **Jordan basis**, in which left multiplication by $\tilde Q$ is $\operatorname{diag}(J_2(Q_t),J_2(Q_t))$ and right multiplication is the same two blocks with the other pairing. Every biquaternion has a unique expansion in it, and the coordinate model sends $\tilde Q$ to the single block $J_2(Q_t)$. The construction is the degenerate twin of the eigenbasis: it covers the two defective strata at once, and it does not depend on the scalar part.

**Place among the Peirce decompositions.** This article is the degenerate particular case of *The Peirce Decomposition of the Biquaternion Algebra*. That article attaches a Peirce basis to any complete orthogonal pair of idempotents, and shows that the four basis vectors split into the two couples $\mathcal{C}_+=(\tilde\Pi_+,\vec\Upsilon_+)$ and $\mathcal{C}_-=(\vec\Upsilon_-,\tilde\Pi_-)$, on which left multiplication acts by the same Peirce matrix. Here the pair is an adapted frame of §*The Frame on the Sector*: complete, orthogonal and primitive, so the four corners and the basis are the general Peirce data. What is special is the matrix of the element: $\mathsf M_{\tilde\Pi}(\tilde Q)=J_2(Q_t)$, so each couple is a Jordan chain rather than a pair of eigenvectors. The reciprocal $\mathbb{C}^\times$ of the general theory is fixed here by $\vec\Upsilon_-=\vec Q$, not by a normalisation convention.

The sector is the union of two cells of the four-cell arrangement,

$$
\mathcal S=\Sigma_{10}\sqcup\Sigma_{00},
$$

and each cell has its own article: *The N-Regular, Spectrally Degenerate Sector* for $\Sigma_{10}$ and *The N-Degenerate, Spectrally Degenerate Sector* for $\Sigma_{00}$. The cell articles compute the Peirce data, the generators and the comparison with the other cells. This article treats what the two cells have in common: the equation, the strata, the geometry, the matrix form, the construction of the Jordan basis, the multiplicative behaviour, and the way the sector sits inside the spectral partition.

**The word degenerate refers to the spectrum only.** It says that the two eigenvalues coincide, not that the element is a zero divisor and not that the element fails to be diagonalisable. Two warnings fix the reading. The scalar line $\mathbb C e_t$ lies in the sector, and its points are central, hence semisimple; the origin is diagonalisable as well. The defective elements form the **Jordan part** $\mathcal S^{\mathrm n}\cup\mathcal S^{\mathrm u}$ of the sector, a proper subset. Conversely, an element outside the sector can be a zero divisor: the Hermitian idempotent $\tfrac12(e_t+i\vec u)$ with $\vec u\cdot\vec u=1$ has $B^2=-\tfrac14$ and $\det\tilde Q=0$. Spectral degeneracy and degeneracy of the product are independent conditions.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, of complex dimension four and real dimension eight, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$, and central scalar imaginary $i$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$ and the Hermitian conjugation is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$; the product is the plain product, with unit $e_t$. The **determinant** is $\det\tilde Q=Q_t^2+B^2$. A **sector** is one of the two halves selected by one condition; a **cell** is one of the four intersections $\Sigma_{ij}$, with $i=1$ for $\det\tilde Q\neq0$ and $i=0$ for $\det\tilde Q=0$, and $j=1$ for $B^2\neq0$ and $j=0$ for $B^2=0$.

## Definition and Characterisation

**Definition.** The **spectrally degenerate sector** is

$$
\mathcal S=\{\tilde Q\in\mathbb{B}:B^2=0\}=\{\tilde Q\in\mathbb{B}:\vec Q^2=0\},
$$

the zero set of the square of the vector part. Its complement $\mathbb{B}\setminus\mathcal S=\{B^2\neq0\}$ is the **spectrally regular sector**.

**Theorem (five descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $B^2=0$;

(ii) $\vec Q^2=0$;

(iii) the discriminant of the characteristic polynomial vanishes, $\operatorname{disc}p_{\tilde Q}=0$;

(iv) the two eigenvalues of $\tilde Q$ coincide, $\lambda_+=\lambda_-=Q_t$;

(v) the characteristic polynomial is a square, $p_{\tilde Q}(X)=(X-Q_t)^2$.

*Proof.* The identity $\vec Q^2=-B^2e_t$ gives (i)$\iff$(ii). The characteristic polynomial of *The Spectrum* is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2,
$$

of discriminant $-4B^2$ and roots $Q_t\pm iB$; hence (i), (iii), (iv) and (v) are the same equation read in four ways. ∎

**Corollary (the spectral data).** On the sector the eigenvalue is $Q_t$, the trace is $2Q_t$, the determinant is

$$
\det\mathsf{M}_2(\tilde Q)=Q_t^2,
$$

and the spectrum is the single point $\{Q_t\}$: the two roots have merged, so no symmetric function of them can separate them.

**Remark (three readings of one equation).** The equation is **geometric** — the vector part is isotropic, $\vec Q\cdot\vec Q=0$ for the complex dot product of the vector subspace; **algebraic** — the vector part is square-zero, hence nilpotent of index two when it is non-zero; and **spectral** — the discriminant vanishes. The three readings are those of *The Spectrum*, §*The Spectral-Degenerate Cone*, where the proofs are given; the stratification is §*The Three Strata* below.

**Remark (a closed cone, not a subspace).** The sector is a complex cone: it is closed under multiplication by scalars, since $B^2$ is homogeneous of degree two. It is not closed under addition, since $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ both lie in it while their sum $2\vec e_x$ does not. It is a proper algebraic subset, of empty interior in $\mathbb{B}$.

## The Determinant inside the Sector

**The determinant is not an independent condition on the sector: it is the square of the scalar part.**

**Theorem (the determinant on the sector).** For $\tilde Q\in\mathcal S$,

$$
\det\tilde Q=Q_t^2.
$$

*Proof.* The determinant is $Q_t^2+B^2$, and $B^2=0$ on the sector. ∎

**Corollary (the sector splits by the scalar part).** The scalar part cuts $\mathcal S$ into exactly two halves,

$$
\Sigma_{10}=\mathcal S\setminus\mathcal N=\{Q_t\neq0\},\qquad
\Sigma_{00}=\mathcal S\cap\mathcal N=\{Q_t=0\},
$$

and on the sector the three conditions "$\det\tilde Q\neq0$", "$Q_t\neq0$" and "$\tilde Q$ is a unit with repeated eigenvalue" are equivalent.

*Proof.* By the theorem, $\det\tilde Q=Q_t^2$. A complex square vanishes exactly when its argument does. The last equivalence is the criterion of *Zero Divisors and Units*, which identifies $\det\tilde Q\neq0$ with invertibility. ∎

**Corollary (both kinds of element).** The sector contains units and zero divisors. Its unit half is $\Sigma_{10}$; its zero-divisor half is $\Sigma_{00}\setminus\{0\}$, the nilpotent stratum. Hence spectral degeneracy is not a form of non-invertibility: every element of $\Sigma_{10}$ is invertible, with inverse

$$
\tilde Q^{-1}=Q_t^{-1}\left(e_t-\frac{\vec Q}{Q_t}\right).
$$

**Remark (the determinant as the squared eigenvalue).** The determinant is the product of the eigenvalues. On the sector the two eigenvalues are equal to $Q_t$, so the product is $Q_t^2$; the identity of the theorem is the spectral reading of that product, not a new constraint.

## The Three Strata

**Definition (the strata).** On $\mathcal S$ put

$$
\mathcal S^{\mathrm{s}}=\{\vec Q=0\},\qquad
\mathcal S^{\mathrm{n}}=\{\vec Q\neq0,\ Q_t=0\},\qquad
\mathcal S^{\mathrm{u}}=\{\vec Q\neq0,\ Q_t\neq0\},
$$

the **scalar**, **nilpotent** and **unipotent** strata. The union $\mathcal S^{\mathrm{n}}\cup\mathcal S^{\mathrm{u}}$ is the **Jordan part** of the sector; its complement, the scalar stratum, is the common vertex.

**Theorem (a disjoint union).** $\mathcal S=\mathcal S^{\mathrm{s}}\sqcup\mathcal S^{\mathrm{n}}\sqcup\mathcal S^{\mathrm{u}}$.

*Proof.* Either $\vec Q=0$, or $\vec Q\neq0$; in the second case either $Q_t=0$ or $Q_t\neq0$. The three conditions are exclusive and exhaustive. ∎

**Theorem (the normal forms).** The three strata have the following normal forms and invariants; $m_{\tilde Q}$ is the minimal polynomial and $L_{\tilde Q}$ is left multiplication.

| stratum | condition | normal form | $m_{\tilde Q}$ | $\operatorname{rank}L_{\tilde Q}$ | centraliser | $\det$ |
|---|---|---|---|---|---|---|
| **scalar** | $\vec Q=0$ | $Q_te_t$ | $X-Q_t$ | $4$, or $0$ at the origin | $\mathbb{B}$ | $Q_t^2$ |
| **nilpotent** | $\vec Q\neq0$, $Q_t=0$ | $\vec Q$, with $\vec Q^2=0$ | $X^2$ | $2$ | $\mathbb{C}[\vec Q]$ | $0$ |
| **unipotent** | $\vec Q\neq0$, $Q_t\neq0$ | $Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon=\vec Q/Q_t$ | $(X-Q_t)^2$ | $4$ | $\mathbb{C}[\vec Q]$ | $Q_t^2$ |

*Proof.* The scalar stratum is immediate: the element is central, with the stated minimal polynomial, and left multiplication is $Q_t\,\mathrm{id}$, of rank $4$, or zero at the origin. On the other two strata $\vec Q^2=0$ and $\vec Q\neq0$, so $\tilde Q-Q_te_t$ is non-zero with square zero; the minimal polynomial is $(X-Q_t)^2$ and the centraliser is that of $\vec Q$, the dual numbers $\mathbb{C}[\vec Q]=\{ae_t+b\vec Q\}$, of complex dimension two. On the nilpotent stratum the element is a non-zero square-zero element, not a unit, and its minimal polynomial is $X^2$; on the unipotent stratum $u=e_t+\vec\Upsilon$ is unipotent, so $\tilde Q=Q_tu$ is a unit with inverse $Q_t^{-1}(e_t-\vec\Upsilon)$. Left multiplication by a non-zero square-zero element has image contained in its kernel, and both spaces have complex dimension two, so the rank is two; on the units the rank is four. ∎

**Corollary (the spectral behaviour).** The spectral data are collected in the table.

| stratum | spectrum | spectral decomposition | eigenspace | eigenbasis | Jordan basis |
|---|---|---|---|---|---|
| **scalar** | $\{Q_t\}$ | one term, unique | $\mathbb{B}$, of dimension $4$ | every basis | every basis, four blocks $J_1(Q_t)$ |
| **nilpotent** | $\{0\}$ | none | $\ker L_{\vec Q}$, of dimension $2$ | none | chosen, two blocks $J_2(0)$ |
| **unipotent** | $\{Q_t\}$ | none | $\ker L_{\vec Q}$, of dimension $2$ | none | chosen, two blocks $J_2(Q_t)$ |

*Proof.* A two-term spectral decomposition needs two non-trivial orthogonal idempotents commuting with $\tilde Q$. On the two defective strata the centraliser is the dual numbers, whose only idempotents are $0$ and $e_t$; on the scalar stratum the element is central, and the canonical one-term writing is the only decomposition. The eigenspace is $\ker L_{\tilde Q}=\ker L_{\vec Q}$, which is all of $\mathbb{B}$ on the scalar stratum and has dimension two on the other two, by the rank computation of the preceding theorem. The Jordan column is the construction of §*The Jordan Basis* on the defective strata, and the trivial case on the scalar line. ∎

**Proposition (similarity).** Under the inner automorphisms of $\mathbb{B}$ each stratum is a union of orbits indexed by the scalar part: the scalar stratum has one orbit for each $Q_t\in\mathbb{C}$, the unipotent stratum has one orbit for each $Q_t\in\mathbb{C}^\times$, and the nilpotent stratum is a single orbit. The origin is its own orbit.

*Proof.* The scalar part is invariant under every automorphism, since automorphisms fix the centre. On the scalar stratum the element is central, so its orbit is a point. On the unipotent stratum, $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$; the group $\mathrm{PGL}_2(\mathbb{C})$ acts transitively on the non-zero square-zero elements, by the matrix picture below, so all unipotents with the same $Q_t$ are conjugate. The same argument applies to the nilpotent stratum with $Q_t=0$; the origin is fixed. ∎

**Remark (three strata, two halves).** The determinant split and the stratum split do not agree on the sector. The scalar stratum straddles the two halves: the origin lies in $\Sigma_{00}$, while every other point $Q_te_t$, $Q_t\neq0$, lies in $\Sigma_{10}$. The unipotent stratum is exactly $\Sigma_{10}\setminus\mathbb{C}^\times e_t$, and the nilpotent stratum is exactly $\Sigma_{00}\setminus\{0\}$. Thus

$$
\Sigma_{10}=\mathbb{C}^\times e_t\sqcup\mathcal S^{\mathrm{u}},\qquad
\Sigma_{00}=\{0\}\sqcup\mathcal S^{\mathrm{n}}.
$$

## Geometry

**Theorem (the sector as a product).** Let $C=\{\vec Q\in\operatorname{Vect}(\mathbb{B}):\vec Q^2=0\}$ be the isotropic cone of the vector subspace. Then

$$
\mathcal S=\mathbb{C}e_t\times C.
$$

The sector is a complex algebraic cone of complex dimension $3$ and real dimension $6$. Its singular locus is the whole scalar line $\mathbb{C}e_t$; off that line it is a smooth hypersurface of $\mathbb{B}$.

*Proof.* The equation $B^2=0$ involves no $Q_t$, so the sector is the product of the scalar line and $C$. It is one complex equation in four complex variables, homogeneous of degree two, so its complex dimension is $3$ and its real dimension is $6$, away from the locus where the equation is singular. The gradient of $B^2$ with respect to $(Q_t,Q_x,Q_y,Q_z)$ is

$$
(0,\,2Q_x,\,2Q_y,\,2Q_z),
$$

which vanishes exactly when $\vec Q=0$. Off the scalar line the gradient is non-zero, and the sector is a smooth hypersurface; on the line the cone is $\mathbb{C}e_t\times C$ with $C$ singular at its apex, and the product is singular along the whole line. ∎

**Proposition (connectedness).** The sector is connected and path-connected. So are its two halves $\Sigma_{10}$ and $\Sigma_{00}$.

*Proof.* The isotropic cone $C$ of $\mathbb{C}^3$ is the affine cone over the smooth conic $Q_x^2+Q_y^2+Q_z^2=0$ of $\mathbb{P}^2$, which is isomorphic to $\mathbb{P}^1$; a cone over a connected projective variety, with the apex adjoined, is connected and path-connected. A product of connected sets is connected, and $\Sigma_{10}=\{Q_t\neq0\}\times C$ and $\Sigma_{00}=\{0\}\times C$ are connected for the same reason. ∎

**The isotropic line and the flag.** Let $(\vec X,\vec Y)=X_xY_x+X_yY_y+X_zY_z$ be the symmetric form of the vector subspace, so that $(\vec Q,\vec Q)=B^2$. Off the sector the line $\mathbb{C}\vec Q$ is non-isotropic and $\mathbb{C}^3=\mathbb{C}\vec Q\oplus\vec Q^{\perp}$ is a direct sum of non-degenerate summands. On the sector, for $\vec Q\neq0$, the line is isotropic and $\vec Q\in\vec Q^{\perp}$, so $\mathbb{C}\vec Q+\vec Q^{\perp}=\vec Q^{\perp}$ and the sum is not direct. No complement of the line is determined by $\vec Q$: the canonical objects are the line, the plane $\vec Q^{\perp}$ that contains it, and the flag

$$
0\subset\mathbb{C}\vec Q\subset\vec Q^{\perp}\subset\mathbb{C}^3.
$$

On the algebra the same failure appears as $\operatorname{im}L_{\vec Q}\subseteq\ker L_{\vec Q}$ with equal dimensions, hence equality, and the canonical flag

$$
0\subset\mathbb{C}\vec Q\subset\ker L_{\vec Q}=\operatorname{im}L_{\vec Q}\subset\mathbb{B}.
$$

A Jordan basis of $L_{\vec Q}$ needs two vectors outside the kernel whose images span it; the quotient $\mathbb{B}/\ker L_{\vec Q}$ is two-dimensional, but no splitting of it is determined by $\vec Q$ alone. This is the structural reason the eigenbasis fails on the defective part: the isotropic line admits no canonical complement, so there is no spectral second direction. The obstruction is not removed by the product; §*The Frame on the Sector* records the choice that replaces it.

## The Matrix Picture

Under $\mathsf{M}_2$ of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant* the sector becomes the set of matrices whose two eigenvalues coincide. The characteristic polynomial is $(X-Q_t)^2$, the trace is $2Q_t$ and the determinant is $Q_t^2$. The Jordan form is determined by the minimal polynomial:

| stratum | $\mathsf{M}_2(\tilde Q)$ | Jordan form | rank |
|---|---|---|---|
| **scalar**, $Q_t\neq0$ | $Q_t\mathrm{I}_2$ | $Q_t\mathrm{I}_2$ | $2$ |
| **scalar**, origin | $0$ | $0$ | $0$ |
| **nilpotent** | a non-zero matrix of square zero | $J_2(0)$ | $1$ |
| **unipotent** | $Q_t(\mathrm{I}_2+N)$, $N^2=0$, $N\neq0$ | $J_2(Q_t)$ | $2$ |

**Proposition (diagonalisability).** An element of the sector is diagonalisable exactly when it lies on the scalar line. Off that line the minimal polynomial is $(X-Q_t)^2$, of degree two, while the characteristic polynomial has the same two roots; the matrix is a single Jordan block.

**Remark (not a determinantal variety).** The null cone is the determinantal variety of rank at most one, so the rank is a complete invariant of it. The spectral-degenerate sector is not of that kind: it contains matrices of rank two (the units of $\Sigma_{10}$), of rank one (the nilpotents) and of rank zero (the origin). Its defining equation is the discriminant, not a rank condition, and its strata are distinguished by the minimal polynomial and the scalar part rather than by the rank alone.

## The Frame on the Sector

**The flag is canonical; the frame is not. The idempotents that split the flag are chosen, and the Jordan form does not depend on the choice.**

### The Obstruction

The vector part is isotropic, $(\vec Q,\vec Q)=B^2=0$, so $\vec Q\in\vec Q^{\perp}$ and the line $\mathbb{C}\vec Q$ lies in its own orthogonal plane. On the algebra,

$$
\operatorname{im}L_{\vec Q}=\ker L_{\vec Q}=\vec Q\mathbb{B},
$$

of complex dimension two: the image is the kernel, and the quotient $\mathbb{B}/\ker L_{\vec Q}$ has no canonical splitting. The regular construction escapes this by the root, a pure square root of $e_t$; the root does not exist at $B=0$.

### The Chosen Frame

A **frame adapted to $\vec Q$** is a complete orthogonal pair $\tilde\Pi_+,\tilde\Pi_-$ with

$$
\tilde\Pi_+\vec Q=\vec Q,\qquad \vec Q\tilde\Pi_-=\vec Q,\qquad \tilde\Pi_-\vec Q=\vec Q\tilde\Pi_+=0.
$$

Such a pair exists: choose a complement of $\mathbb{C}\vec Q$ in $\ker L_{\vec Q}$, let $\tilde\Pi_+$ be the projection onto $\mathbb{C}\vec Q$ along that complement, and put $\tilde\Pi_-=e_t-\tilde\Pi_+$.

**Proposition.** Every adapted pair is complete and orthogonal, and $\vec Q\in\mathbb{B}_{+-}$.

*Proof.* The identities give $\tilde\Pi_+\vec Q=\vec Q$ and $\tilde\Pi_-\vec Q=0$, so $\vec Q=\tilde\Pi_+\vec Q\tilde\Pi_-$ lies in the corner $\mathbb{B}_{+-}$; completeness and orthogonality are the definition of the pair. ∎

**Remark (the choice is real).** The complement is not determined by $\vec Q$: two complements differ by a linear map from $\mathbb{C}\vec Q$ to the complement, and the idempotents differ by the affine family $\tilde\Pi_+(b)=\tilde\Pi_+ + b\vec Q$, $b\in\mathbb{C}$, with $\tilde\Pi_-(b)=e_t-\tilde\Pi_+(b)$. The Jordan form below is independent of $b$; the frame is not. No canonical value of $b$ is claimed for the product alone. The definite Hermitian form selects one, and it is constructed in the next subsection.

**Remark (not a limit).** The idempotents are not the limits of the regular spectral idempotents $(e_t\pm\vec\Xi)/2$, which diverge as $B\to0$. They are a new pair, attached to the flag of $\vec Q$ and to the chosen complement.

### The Canonical Frame

**The definite Hermitian form selects one value of $b$.** The form is $\langle X,Y\rangle_*=\operatorname{Sc}(XY^*)$ of *Conventions in Mathematics*, §*The Form Convention, the Norm Convention and the Unitary Convention*, and $\langle\vec Q\rangle_*=\sum\lvert Q_k\rvert^2>0$ on the sector off the scalar line.

**Theorem (the canonical pair).** Put $\vec\Upsilon_-=\vec Q$ and

$$
\tilde\Pi_+=\frac{\vec Q\vec Q^*}{2\langle\vec Q\rangle_*},\qquad
\tilde\Pi_-=\frac{\vec Q^*\vec Q}{2\langle\vec Q\rangle_*},\qquad
\vec\Upsilon_+=\frac{\vec Q^*}{2\langle\vec Q\rangle_*}.
$$

Then $\tilde\Pi_\pm$ are the **support idempotents**: Hermitian idempotents with $\tilde\Pi_+\tilde\Pi_-=0$, $\tilde\Pi_++\tilde\Pi_-=e_t$, and

$$
\tilde\Pi_+\vec Q=\vec Q,\qquad
\vec Q\tilde\Pi_-=\vec Q,\qquad
\vec Q\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+\vec Q=\tilde\Pi_-.
$$

*Proof.* In the fixed model $Q=\mathsf M_2(\vec Q)$ is a rank-one nilpotent with singular value $s=\sqrt{2\langle\vec Q\rangle_*}$, so $Q=suv^\dagger$ with $u,v$ orthonormal. The Frobenius norm gives $s^2=\operatorname{Tr}(Q^\dagger Q)=2\langle\vec Q\rangle_*$. The four elements are the images of $uu^\dagger$, $suv^\dagger$, $s^{-1}vu^\dagger$ and $vv^\dagger$, and the identities are the matrix-unit identities. ∎

**Corollary (uniqueness).** The canonical pair is the value $b=0$ of the affine family. Every adapted pair is $\tilde\Pi_+(b)=\tilde\Pi_+ + b\vec Q$ with $\tilde\Pi_-(b)=\tilde\Pi_- - b\vec Q$, and the pair is Hermitian exactly when $b=0$.

*Proof.* If $\tilde\Pi_+(b)$ is Hermitian, then $\bar b\vec Q^*=b\vec Q$. If $b\neq0$, then $\vec Q^*=\mu\vec Q$ with $\lvert\mu\rvert=1$, hence $\vec Q^*\vec Q=\mu\vec Q^2=0$, contrary to $\vec Q^*\vec Q$ being a nonzero projection. Hence $b=0$. ∎

**Remark (the matrix form).** The pair is the SVD frame of the nilpotent. The Jordanising matrix, its determinant and its freedom are in *$M_2(\mathbb{C})$ Model : The Jordan Basis and the Jordanising Matrix*.

## The Corners and the Jordan Pair

**The two idempotents split the algebra into four one-dimensional corners, as in the regular case. The mixed corners carry the two generators of the chain.**

### The Peirce Corners

**Definition (corners).** For $s,t\in\{+,-\}$ put

$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t=\{\tilde Q_2:\ \tilde\Pi_s\tilde Q_2=\tilde Q_2,\ \tilde Q_2\tilde\Pi_t=\tilde Q_2\}.
$$

The corner rule is

$$
\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}.
$$

Each corner is a complex line (*The Peirce Decomposition of the Biquaternion Algebra*), and the direct sum is the algebra:

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}.
$$

The diagonal corners are spanned by the idempotents,

$$
\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_+,\qquad
\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_-,
$$

and the mixed corners by the generators of the next subsection,

$$
\mathbb{B}_{+-}=\mathbb{C}\vec\Upsilon_-,\qquad
\mathbb{B}_{-+}=\mathbb{C}\vec\Upsilon_+.
$$

The proposition of the preceding section places the vector part in the first mixed corner: $\tilde\Pi_+\vec Q=\vec Q$ and $\vec Q\tilde\Pi_-=\vec Q$, so $\vec Q\in\mathbb{B}_{+-}$.

### The Jordan Pair

**Definition (the pair).** Put $\vec\Upsilon_-=\vec Q$. Left multiplication by $\vec Q$ is an isomorphism from $\mathbb{B}_{-+}$ onto $\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_+$, so there is a unique $\vec\Upsilon_+\in\mathbb{B}_{-+}$ with $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**Theorem (the pair).** The two elements satisfy

$$
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_\pm^2=0,
$$

and they are the unique pair with these properties and with $\vec\Upsilon_-=\vec Q$.

*Proof.* The products are the proposition, and the square of $\vec\Upsilon_-$ is $\vec Q^2=0$. The square of $\vec\Upsilon_+$ vanishes because the star preserves the cone. For uniqueness, let $\vec\Upsilon$ lie in $\mathbb{B}_{-+}$ with $\vec Q\vec\Upsilon=\tilde\Pi_+$. Then $\vec Q(\vec\Upsilon-\vec\Upsilon_+)=0$, and the difference lies in the corner. Left multiplication by $\vec Q$ is injective on $\mathbb{B}_{-+}$: it sends the generator $\vec\Upsilon_+$ to $\tilde\Pi_+\neq0$, and a non-zero linear map between lines is injective. Hence $\vec\Upsilon=\vec\Upsilon_+$. ∎

**Remark (the scale is fixed by the element).** In the regular case the admissible pair is determined only up to the reciprocal rescaling $\vec\Upsilon_+\mapsto\mu\vec\Upsilon_+$, $\vec\Upsilon_-\mapsto\mu^{-1}\vec\Upsilon_-$. The rescaling is still an automorphism of the pair here, but only one representative has $\vec\Upsilon_-=\vec Q$. The condition that the element itself be a basis vector, $\tilde Q=Q_te_t+1\cdot\vec\Upsilon_-$, fixes $\mu=1$. The normalisation is the one of the Jordan block: the superdiagonal entry is one.

## The Jordan Basis

**With the pair fixed, the four vectors are a basis, and the two multiplications are Jordan blocks.**

### The Basis and the Left Action

**Definition (the Jordan basis).** For a spectrally degenerate $\tilde Q$ with $\vec Q\neq0$, the **Jordan basis** is

$$
\mathcal{J}(\tilde Q)=(\vec\Upsilon_-,\ \tilde\Pi_-,\ \tilde\Pi_+,\ \vec\Upsilon_+).
$$

The vectors are listed chain by chain. The corner order, used for the multiplication table and for the coordinate model, is the same four vectors in the order $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. The four vectors are determined by the frame; their corner labels are canonical, and the order of the two chains is a convention.

**Theorem (basis and Jordan form).** The four vectors are non-zero and lie in the four corners, in the corner order $\mathbb{B}_{++},\mathbb{B}_{+-},\mathbb{B}_{-+},\mathbb{B}_{--}$ respectively. They form a basis of $\mathbb{B}$. Put

$$
J_2(Q_t)=\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}.
$$

In the order of the definition,

$$
L_{\tilde Q}=\operatorname{diag}\bigl(J_2(Q_t),J_2(Q_t)\bigr).
$$

In the corner order the matrix is

$$
L_{\tilde Q}=
\begin{pmatrix}
Q_t&0&1&0\\
0&Q_t&0&1\\
0&0&Q_t&0\\
0&0&0&Q_t
\end{pmatrix}.
$$

*Proof.* The corners are lines and their direct sum is $\mathbb{B}$, so one non-zero vector in each forms a basis. The actions are

$$
\tilde Q\tilde\Pi_+=Q_t\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=Q_t\vec\Upsilon_-,
$$

$$
\tilde Q\tilde\Pi_-=Q_t\tilde\Pi_-+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=Q_t\vec\Upsilon_++\tilde\Pi_+.
$$

The first pair is diagonal, and the second pair gives the superdiagonal entry one in each chain. ∎

The multiplication of the four basis vectors is the table. The row is the left factor and the column is the right factor.

| product | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |
|---|---|---|---|---|
| $\tilde\Pi_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $0$ | $0$ |
| $\vec\Upsilon_-$ | $0$ | $0$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ |
| $\vec\Upsilon_+$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ | $0$ | $0$ |
| $\tilde\Pi_-$ | $0$ | $0$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |

The table is the one of the eigenbasis, unchanged: in both cases the four vectors are the matrix units. What changes is the element expanded in the basis, not the multiplication of the basis.

### The Right Action

**Theorem (the right action).** In the order of the definition,

$$
R_{\tilde Q}=
\begin{pmatrix}
Q_t&0&1&0\\
0&Q_t&0&1\\
0&0&Q_t&0\\
0&0&0&Q_t
\end{pmatrix}.
$$

In the order $(\vec\Upsilon_-,\tilde\Pi_+,\tilde\Pi_-,\vec\Upsilon_+)$ it is $\operatorname{diag}(J_2(Q_t),J_2(Q_t))$.

*Proof.* The actions are

$$
\tilde\Pi_+\tilde Q=Q_t\tilde\Pi_++\vec\Upsilon_-,\qquad
\vec\Upsilon_-\tilde Q=Q_t\vec\Upsilon_-,
$$

$$
\vec\Upsilon_+\tilde Q=Q_t\vec\Upsilon_++\tilde\Pi_-,\qquad
\tilde\Pi_-\tilde Q=Q_t\tilde\Pi_-.
$$

The two chains are $(\vec\Upsilon_-,\tilde\Pi_+)$ and $(\tilde\Pi_-,\vec\Upsilon_+)$. ∎

**Remark (no simultaneous Jordan basis).** If one basis put both $L_{\tilde Q}$ and $R_{\tilde Q}$ in Jordan form, both would be $\operatorname{diag}(J_2(Q_t),J_2(Q_t))$, since the Jordan form of a single eigenvalue with two blocks of size two is unique, hence $L_{\tilde Q}=R_{\tilde Q}$. But $L_{\tilde Q}\tilde\Pi_+=Q_t\tilde\Pi_+$ while $R_{\tilde Q}\tilde\Pi_+=Q_t\tilde\Pi_++\vec\Upsilon_-$. The two actions have different chain pairings and no common Jordan form.

### The Matrix Model

Assign the four vectors, in the corner order, to the matrix units by

$$
\mathsf M_2^{\tilde Q}(\tilde\Pi_+)=E_{11},\quad
\mathsf M_2^{\tilde Q}(\vec\Upsilon_-)=E_{12},\quad
\mathsf M_2^{\tilde Q}(\vec\Upsilon_+)=E_{21},\quad
\mathsf M_2^{\tilde Q}(\tilde\Pi_-)=E_{22}.
$$

The assignment is an algebra isomorphism onto $M_2(\mathbb{C})$, because the table above is the matrix-unit table. In it,

$$
\mathsf M_2^{\tilde Q}(\tilde Q)=J_2(Q_t),
$$

and left and right multiplication by $\tilde Q$ become left and right multiplication by $J_2(Q_t)$ on $2\times2$ matrices. The coordinate matrix of a general element is

$$
\mathsf M_2^{\tilde Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$

## Expansion of Every Biquaternion

**The Jordan basis is a coordinate system: every element has one expansion, and the coordinates multiply as matrices.**

**Theorem (expansion).** Every $\tilde X\in\mathbb{B}$ has a unique expansion

$$
\tilde X=X_{11}\tilde\Pi_++X_{12}\vec\Upsilon_-+X_{21}\vec\Upsilon_++X_{22}\tilde\Pi_-,
$$

and the map $\tilde X\mapsto\mathsf M_2^{\tilde Q}(\tilde X)$ is an algebra isomorphism onto $M_2(\mathbb{C})$.

*Proof.* The four vectors are a basis, and the products are the table of $\mathsf M_2^{\tilde Q}$. ∎

**Corollary (the centraliser).** The matrices commuting with $J_2(Q_t)$ are the upper triangular Toeplitz matrices $\begin{pmatrix}a&b\\0&a\end{pmatrix}$. Hence the centraliser of $\tilde Q$ is $\mathbb{C}[\tilde Q]=\{ae_t+b\vec Q\}$, the dual numbers, of complex dimension two, with maximal ideal $\mathbb{C}\vec Q$ and only the idempotents $0$ and $e_t$.

*Proof.* A direct computation gives $c=0$ and $d=a$ for a matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ commuting with $J_2(Q_t)$. The coordinate matrix of $ae_t+b\vec Q$ is $aI+bE_{12}$. ∎

**Corollary (the trace).** $\operatorname{Tr}\tilde X=X_{11}+X_{22}$.

*Proof.* The trace is twice the scalar part, and the scalar part of the expansion is $(X_{11}+X_{22})/2$. ∎

### A Worked Example

Take

$$
\tilde Q=e_t+\vec e_x+i\vec e_y.
$$

Then $Q_t=1$, $\vec Q=\vec e_x+i\vec e_y$, $\vec Q^2=0$. The adapted frame is

$$
\tilde\Pi_+=\frac12(e_t+i\vec e_z),\qquad
\tilde\Pi_-=\frac12(e_t-i\vec e_z),
$$

$$
\vec\Upsilon_-=\vec e_x+i\vec e_y,\qquad
\vec\Upsilon_+=\frac14(-\vec e_x+i\vec e_y).
$$

The checks are

$$
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
$$

and

$$
\tilde Q=\tilde\Pi_++\vec\Upsilon_-+\tilde\Pi_-.
$$

In the chain order $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$,

$$
L_{\tilde Q}=\operatorname{diag}\left(\begin{pmatrix}1&1\\0&1\end{pmatrix},\begin{pmatrix}1&1\\0&1\end{pmatrix}\right),
$$

and in the coordinate model $\mathsf M_2^{\tilde Q}(\tilde Q)=\begin{pmatrix}1&1\\0&1\end{pmatrix}$.

### Change of Element

**Proposition (the affine family).** Let $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$ and $\vec Q\neq0$, let $b\in\mathbb{C}$ and $a\in\mathbb{C}^\times$.

1. $\tilde Q+be_t$ has the same vector part, hence the same basis $\mathcal{J}(\tilde Q)$, and $\mathsf M_2^{\tilde Q}(\tilde Q+be_t)=J_2(Q_t+b)$.
2. The Jordan basis of $a\tilde Q$ is obtained from $\mathcal{J}(\tilde Q)$ by

$$
\tilde\Pi_\pm\longmapsto\tilde\Pi_\pm,\qquad
\vec\Upsilon_-\longmapsto a\vec\Upsilon_-,\qquad
\vec\Upsilon_+\longmapsto a^{-1}\vec\Upsilon_+,
$$

and $\mathsf M_2^{\tilde Q}(a\tilde Q)=J_2(aQ_t)$.

*Proof.* The vector part of $\tilde Q+be_t$ is $\vec Q$. For $a\tilde Q$ the vector part is $a\vec Q$; the flag is unchanged, so the idempotents are unchanged and the generators scale as stated. In the rescaled basis the element is $aQ_te_t+a\Upsilon_-$, whose coefficient on $\vec\Upsilon_-'$ is one, so its matrix is $J_2(aQ_t)$. ∎

## The Frame Attached to the Vector Part

**The idempotents see the complex line of the vector part. The chain vectors see the vector itself, with the scale fixed by the normal form.**

**Proposition (dependence).** Let $\lambda\in\mathbb{C}^\times$.

1. The idempotents are unchanged under $\vec Q\mapsto\lambda\vec Q$: $\tilde\Pi_\pm(\lambda\vec Q)=\tilde\Pi_\pm(\vec Q)$.
2. The generators are homogeneous of degrees $\pm1$:

$$
\vec\Upsilon_-(\lambda\vec Q)=\lambda\vec\Upsilon_-(\vec Q),\qquad
\vec\Upsilon_+(\lambda\vec Q)=\lambda^{-1}\vec\Upsilon_+(\vec Q).
$$

*Proof.* The line $\mathbb{C}\vec Q$ and the chosen complement are unchanged, so the idempotents are unchanged. The generator $\vec\Upsilon_-=\vec Q$ scales by $\lambda$, and the relation $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ forces $\vec\Upsilon_+$ to scale by $\lambda^{-1}$. ∎

**Remark (comparison with the eigenbasis).** The eigenbasis of the regular case is attached to the direction $[\vec Q]\in\mathbb{P}^2$; the eigenvalues move affinely with the element and the basis does not move. Here the idempotents are attached to the direction, and the two chain vectors are not: the chain carries the scale of the vector part. The price of the normal form $J_2$ is that its superdiagonal entry one is a scale, and that scale is the scale of $\vec Q$.

**Proposition (equivariance).** Let $S\in\mathbb{B}^\times$ with $S^*=S^{-1}$. Then

$$
\mathcal{J}(S\tilde QS^{-1})=S\,\mathcal{J}(\tilde Q)\,S^{-1}.
$$

A general inner automorphism need not preserve the chosen frame, and the image of a Jordan basis is then a Jordan basis, but not the same one.

*Proof.* The conjugation preserves the product, the unit, the trace and the star, hence the flag and the formulas of the construction. ∎

**Remark (the boundary).** The construction is defined on $\mathcal S\setminus\mathbb{C}e_t$; on the scalar line the vector part vanishes, the flag collapses, and no adapted frame is distinguished. On that line $\tilde Q=Q_te_t$ and every basis is an eigenbasis; the Jordan type is four blocks $J_1(Q_t)$, and at the origin $L_{\tilde Q}=0$.

## Spinors and Chirality

**The two minimal left ideals are the two Jordan blocks of the left action, and the right action distinguishes them only partly.**

The general statement is in *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*, §*The Left Action on a Couple*: the four Peirce vectors split into the couples, and left multiplication acts on each couple by the same matrix. Here that matrix is $J_2(Q_t)$, so each couple is a single Jordan chain. The eigenline in $\mathcal{C}_+$ is $\mathbb{C}\tilde\Pi_+$ and the eigenline in $\mathcal{C}_-$ is $\mathbb{C}\vec\Upsilon_-=\mathbb{C}\vec Q$; the two lines span the two-dimensional eigenspace.

**Definition (the spinor spaces).** Put $S_\pm=\mathbb{B}\tilde\Pi_\pm$, the two Peirce carriers, here the two minimal left ideals.

**Proposition (the splitting).** $S_+=\operatorname{span}\{\tilde\Pi_+,\vec\Upsilon_+\}$ and $S_-=\operatorname{span}\{\vec\Upsilon_-,\tilde\Pi_-\}$, and $\mathbb{B}=S_+\oplus S_-$.

*Proof.* The products of the table give $\tilde\Pi_+\tilde\Pi_+=\tilde\Pi_+$, $\vec\Upsilon_+\tilde\Pi_+=\vec\Upsilon_+$, and $\vec\Upsilon_-\tilde\Pi_+=\tilde\Pi_-\tilde\Pi_+=0$; the other side is the same. ∎

**Theorem (the actions on the spinor spaces).** Each $S_\pm$ is invariant under $L_{\tilde Q}$, and $L_{\tilde Q}$ acts on each as one Jordan block $J_2(Q_t)$. The right action preserves $S_-$ and is scalar there, $R_{\tilde Q}|_{S_-}=Q_t\,\mathrm{id}$, but it does not preserve $S_+$:

$$
R_{\tilde Q}(\tilde\Pi_+)=Q_t\tilde\Pi_++\vec\Upsilon_-,\qquad
R_{\tilde Q}(\vec\Upsilon_+)=Q_t\vec\Upsilon_++\tilde\Pi_-.
$$

In particular the two Peirce copies are the two blocks of the left action, and the right action mixes $S_+$ into $S_++S_-$.

*Proof.* The left action is the theorem of §*The Basis and the Left Action* read on the two chains $(\tilde\Pi_+,\vec\Upsilon_+)$ and $(\vec\Upsilon_-,\tilde\Pi_-)$. The right action is computed in the table. ∎

The four labels are collected in the table.

| vector | corner | left ideal | $L_{\tilde Q}$ | $R_{\tilde Q}$ |
|---|---|---|---|---|
| $\tilde\Pi_+$ | $\mathbb{B}_{++}$ | $S_+$ | $Q_t\tilde\Pi_+$ | $Q_t\tilde\Pi_++\vec\Upsilon_-$ |
| $\vec\Upsilon_-$ | $\mathbb{B}_{+-}$ | $S_-$ | $Q_t\vec\Upsilon_-$ | $Q_t\vec\Upsilon_-$ |
| $\vec\Upsilon_+$ | $\mathbb{B}_{-+}$ | $S_+$ | $Q_t\vec\Upsilon_++\tilde\Pi_+$ | $Q_t\vec\Upsilon_++\tilde\Pi_-$ |
| $\tilde\Pi_-$ | $\mathbb{B}_{--}$ | $S_-$ | $Q_t\tilde\Pi_-+\vec\Upsilon_-$ | $Q_t\tilde\Pi_-$ |

**Remark (the Peirce index).** In the regular case right multiplication is scalar on each $S_\pm$, and the Peirce index is a right-multiplication label. Here it is not: $S_-$ is an eigenspace of $R_{\tilde Q}$, but $S_+$ is not invariant, and its image carries a $Q_t$ part in $S_+$ and a nilpotent part in $S_-$. The Peirce index survives as the label of the two minimal left ideals and of the two blocks of the left action.

## Multiplication, Inversion, and the Exponential

**The sector is a cone, but it is not a subalgebra.**

**Proposition (scalars and inverses).** The sector is closed under multiplication by complex scalars. Its unit half $\Sigma_{10}$ is closed under inversion, with the inverse of the corollary of §*The Norm inside the Sector*, and the inverse of a unipotent is unipotent.

*Proof.* $B^2(\lambda\tilde Q)=\lambda^2B^2(\tilde Q)$, so the cone is closed under scalar multiplication. For $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $Q_t\neq0$ and $\vec\Upsilon^2=0$, the inverse is $Q_t^{-1}(e_t-\vec\Upsilon)$, whose vector part $-\vec\Upsilon$ is again square-zero and whose scalar part is non-zero. ∎

**Proposition (the two failures of closure).** The sector is closed under neither addition nor multiplication.

*Proof.* For addition, $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ lie in $\mathcal S$, because each has square zero, and their sum $2\vec e_x$ has $B^2=4\neq0$. For multiplication, put

$$
u_1=e_t+\vec e_x+i\vec e_y,\qquad u_2=e_t+\vec e_x+i\vec e_z .
$$

Both lie in $\Sigma_{10}$: their vector parts $\vec e_x+i\vec e_y$ and $\vec e_x+i\vec e_z$ are square-zero, and their scalar parts are $1$. Their product is computed from the multiplication table as

$$
u_1u_2=e_t+\bigl(2\vec e_x+i\vec e_y+i\vec e_z\bigr)+\bigl(-e_t-\vec e_x-i\vec e_y-i\vec e_z\bigr)=\vec e_x,
$$

which has $B^2=1$ and $\det\tilde Q=1$: it lies in the doubly regular cell $\Sigma_{11}$, outside the sector. ∎

**Remark (the unit half is not a group).** The product of two unipotents need not be unipotent, as the proposition shows. The unit half $\Sigma_{10}$ is therefore a union of similarity orbits closed under inversion, not a subgroup of $\mathbb{B}^\times$. The scalar line minus the origin is a subgroup, and the unipotent stratum is a single orbit for each scalar part, but the two do not compose within the sector.

**Proposition (the truncated exponential).** Let $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$. Then, for every complex $\theta$,

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\left(e_t+\theta\vec Q\right).
$$

*Proof.* The scalar part commutes with $\vec Q$ and $\vec Q^2=0$, so the exponential series truncates after the linear term. ∎

**Corollary (the exponential lands in the unit half).** For every $\tilde Q\in\mathcal S$ and every $\theta$, the exponential $e^{\theta\tilde Q}$ lies in $\Sigma_{10}$. In particular the exponential of a nilpotent is the unipotent $e_t+\theta\vec Q$, and the exponential of the origin is $e_t$.

*Proof.* The vector part of $e^{\theta\tilde Q}$ is $e^{\theta Q_t}\theta\vec Q$, whose square is zero; its scalar part is $e^{\theta Q_t}$, which is never zero. ∎

**Remark (no oscillation).** On the sector the exponential is polynomial in $\theta$: there is no frequency and no periodic term. The root-parametrised form $e^{\theta Q_t}(\cos(B\theta)e_t+\sin(B\theta)\rho)$ of the regular sector does not extend to $B=0$ as a formula in $\rho$, because the root $\rho=\vec Q/B$ does not exist; the entire form in $B$ does extend, and its value is the truncated expression above.

## Relation to the Spectrally Regular Sector

The spectrally regular sector is the complement $\mathbb{B}\setminus\mathcal S=\{B^2\neq0\}$. It is open and dense, and it splits into the two cells

$$
\Sigma_{11}=\{\det\tilde Q\neq0,\ B^2\neq0\},\qquad
\Sigma_{01}=\{\det\tilde Q=0,\ B^2\neq0\}.
$$

On it the eigenvalues are distinct, the discriminant is non-zero, the root $\vec\Xi=-i\vec Q/B$ exists, and the eigenbasis of *The Eigenbasis of a Spectrally Regular Biquaternion* is constructed. The root and the eigenbasis do not cross the boundary; the defective part of the sector has the Jordan basis instead, selected by an adapted frame. The two constructions are separated by the single equation $B^2=0$, and the passage from one to the other is the collapse of the two eigenvalues.

The regular article reads its basis in a root-adapted Fourier form. There is no such reading here: the Fourier form needs the pure root $\rho=i\vec\Xi$ with $\rho^2=-1$, and the degenerate vector part is nilpotent. The counterpart is the truncated exponential, $e^{\theta\tilde Q}=e^{\theta Q_t}(e_t+\theta\vec Q)$, of §*Multiplication, Inversion, and the Exponential*.

The four cells are collected in the table.

| cell | $\det$ | $B^2$ | complex dimension | description |
|---|---|---|---|---|
| $\Sigma_{11}$ | $\neq0$ | $\neq0$ | $4$ | the generic unit, with distinct non-zero eigenvalues |
| $\Sigma_{10}$ | $\neq0$ | $=0$ | $3$ | the unit of the sector: $\mathbb{C}^\times e_t$ and the unipotents |
| $\Sigma_{01}$ | $=0$ | $\neq0$ | $3$ | the zero divisor with distinct eigenvalues, one of them zero |
| $\Sigma_{00}$ | $=0$ | $=0$ | $2$ | the nilpotents, with the origin adjoined |

**Remark (density and boundary).** The sector is closed with empty interior, so every point of it is a limit of points of the spectrally regular sector; it is the boundary of the open set on which the eigenbasis exists. The two conditions are independent, and the cells $\Sigma_{10}$ and $\Sigma_{01}$ are the witnesses: each is a non-empty open part of one cone on which the other condition is non-zero. The comparison of the two cones is *Relations between the N Norm and Spectral Regularity and Degeneracy*.

## Consequences

- **No splitting, no root, no frequency.** The two eigenvalues coincide at $Q_t$; the discriminant $-4B^2$ vanishes; the root $\vec\Xi=-i\vec Q/B$ and the frequency $B$ are undefined; the spectral projectors and the two-term spectral decomposition do not exist.
- **No eigenbasis off the scalar line.** The eigenspace has complex dimension two, the minimal polynomial is $(X-Q_t)^2$, and the isotropic line admits no canonical complement. Only the scalar line carries an eigenbasis, and there it is every basis.
- **A flag survives, and a complement is chosen.** The canonical objects are the line $\mathbb{C}\vec Q$, the plane $\vec Q^{\perp}$, the kernel–image space $\ker L_{\vec Q}=\operatorname{im}L_{\vec Q}$, and the two flags they form. A complement of the line inside the kernel is not canonical; an adapted frame supplies one.
- **A Jordan basis replaces the eigenbasis.** An adapted frame supplies two idempotents and two generators, and the quadruple $\mathcal{J}(\tilde Q)$ is determined by the frame. In it the left and the right actions are each two Jordan blocks $J_2(Q_t)$, with different pairings, and every biquaternion has a unique expansion.
- **The truncated exponential survives.** On the sector the exponential is polynomial, $e^{\theta\tilde Q}=e^{\theta Q_t}(e_t+\theta\vec Q)$, and it maps the whole sector into its unit half $\Sigma_{10}$.
- **The determinant is the square of the eigenvalue.** On the sector $\det\tilde Q=Q_t^2$, so the determinant restricted to the sector is the partition by the scalar part, and the sector is split into a unit half and a zero-divisor half by one complex number.
- **Spectral degeneracy is not non-invertibility.** $\Sigma_{10}$ consists of units; the scalar line is semisimple; only the Jordan part is defective. The sector is the discriminant locus, not the zero-divisor set and not the set of non-diagonalisable elements.
- **The sector is not a subalgebra.** It is a cone closed under scalars and, on its unit half, under inversion; it is closed under neither addition nor multiplication, and the exponential of a nilpotent is a unipotent outside the zero-divisor half.

## The Two Sector Articles as Specialisations

**The Peirce construction needs a complete orthogonal pair and nothing else. The two companion articles obtain the pair from one element, and the Peirce matrix of that element records the difference.**

Fix a complete orthogonal pair $\tilde\Pi_+,\tilde\Pi_-$ and normalised generators $\vec\Upsilon_-\in\mathbb{B}_{+-}$ and $\vec\Upsilon_+\in\mathbb{B}_{-+}$, with $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ (§*The Peirce Decompositions*). The four vectors

$$
\mathcal{P}=(\tilde\Pi_+,\ \vec\Upsilon_-,\ \vec\Upsilon_+,\ \tilde\Pi_-)
$$

are a basis of $\mathbb{B}$, unique up to the reciprocal rescaling $(\mu,\mu^{-1})$ of the two mixed generators. For $\tilde P\in\mathbb{B}$, let $\mathsf M_{\tilde\Pi}(\tilde P)=(p_{ij})$ be its Peirce matrix in this basis, so that $\tilde P=p_{11}\tilde\Pi_++p_{12}\vec\Upsilon_-+p_{21}\vec\Upsilon_++p_{22}\tilde\Pi_-$. For the standard pair $\mathsf M_{\tilde\Pi}$ is the model $\mathsf M_2$ of §*The Peirce Coordinates and the Matrix Model*.

Both sector articles use a basis of this shape. They differ only in the pair, and the pair is visible in the matrix of the element. Write $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and put $B^2=Q_x^2+Q_y^2+Q_z^2$. Write $S_\pm=\mathbb{B}\tilde\Pi_\pm$ for the two minimal left ideals, and split the four basis vectors into the couples $\mathcal{C}_+=(\tilde\Pi_+,\vec\Upsilon_+)$ and $\mathcal{C}_-=(\vec\Upsilon_-,\tilde\Pi_-)$.

| | general Peirce | spectrally regular, $B^2\neq0$ | spectrally degenerate, $B^2=0$, $\vec Q\neq0$ |
|---|---|---|---|
| pair | any complete orthogonal pair | the spectral pair $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$, $\vec\Xi=-i\vec Q/B$ | a chosen adapted pair $\tilde\Pi_+,\tilde\Pi_-$ |
| relation to $\tilde Q$ | none required | $[\tilde\Pi_\pm,\tilde Q]=0$ | $\tilde Q\tilde\Pi_+=Q_t\tilde\Pi_+$, $\tilde\Pi_+\tilde Q=Q_t\tilde\Pi_++\vec\Upsilon_-$ |
| Peirce matrix $\mathsf M_{\tilde\Pi}(\tilde Q)$ | any matrix, with trace $2Q_t$ | $\operatorname{diag}(\lambda_+,\lambda_-)$ | $J_2(Q_t)$ |
| each couple | two spinors | two eigenvectors | a Jordan chain |
| right action | mixes the couples in general | scalar on $S_+$ and on $S_-$ | scalar on $S_-$, mixes $S_+$ |
| basis | a normalised Peirce basis | the eigenbasis $\mathcal{B}(\tilde Q)$ | the Jordan basis $\mathcal{J}(\tilde Q)$ |
| scale | reciprocal $\mathbb{C}^\times$ | fixed by the normalisation | fixed by $\vec\Upsilon_-=\vec Q$ |

Here $\lambda_\pm=Q_t\pm iB$ are the two eigenvalues, $J_2(Q_t)=\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}$ is the Jordan block of the repeated eigenvalue.

**The rigidity applies to all three columns.** By §*Systems of Matrix Units*, every pair of primitive orthogonal idempotents summing to $e_t$ is the image of the standard pair under an inner automorphism. The pairs are therefore conjugate, and the three columns are not three decompositions of different kinds: what changes from one column to the next is the position of the element in the decomposition, not the decomposition itself. The regular pair commutes with $\tilde Q$; the support pair does not; on the scalar line every pair commutes.

**The regular case.** For $B^2\neq0$ the pair is the spectral pair of $\tilde Q$. It satisfies $[\tilde\Pi_\pm,\tilde Q]=0$, so $\mathsf M_{\tilde\Pi}(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$ and each couple is a pair of eigenvectors. The basis $\mathcal{P}$ is the eigenbasis $\mathcal{B}(\tilde Q)$ of *The Eigenbasis of a Spectrally Regular Biquaternion*; the reciprocal freedom is fixed there by the normalisation of the mixed generators.

**The degenerate case.** For $B^2=0$ and $\vec Q\neq0$ the root is gone, and an adapted frame supplies the pair. The pair is still complete, orthogonal and primitive, so the four corners and the basis are the general Peirce data. What changes is the Peirce matrix: $\mathsf M_{\tilde\Pi}(\tilde Q)=J_2(Q_t)$, with $\tilde Q\tilde\Pi_+=Q_t\tilde\Pi_+$ and $\tilde\Pi_+\tilde Q=Q_t\tilde\Pi_++\vec\Upsilon_-$. Each couple is a single Jordan chain rather than a pair of eigenvectors. The basis is the Jordan basis $\mathcal{J}(\tilde Q)$ of §*The Jordan Basis*; the reciprocal freedom is fixed there by $\vec\Upsilon_-=\vec Q$.

**The scalar line.** For $\vec Q=0$ the element is $\tilde Q=Q_te_t$ and central. Every pair commutes with it, $\mathsf M_{\tilde\Pi}(\tilde Q)=Q_tI$, and every couple is a pair of eigenvectors. No pair is distinguished and no basis is canonical: every basis of $\mathbb{B}$ is an eigenbasis.


## Summary

The spectrally degenerate sector is the set $\mathcal S=\{B^2=0\}$ on which the two eigenvalues of a biquaternion coincide. It is a complex cone of complex dimension three and real dimension six, the product of the scalar line and the isotropic cone of the vector subspace, singular exactly along the scalar line and smooth off it. It is connected, closed, of empty interior, and it is the boundary of the sector on which the eigenbasis exists; it is also the domain of the Jordan basis.

The determinant restricted to the sector is the square of the scalar part, $\det\tilde Q=Q_t^2$. This one identity splits the sector into the unit half $\Sigma_{10}=\{Q_t\neq0\}$ and the zero-divisor half $\Sigma_{00}=\{Q_t=0\}$, and it shows that spectral degeneracy and degeneracy of the product are independent: the unipotent stratum consists of units with a repeated eigenvalue, while the idempotent $\tfrac12(e_t+i\vec u)$ is a zero divisor with distinct eigenvalues.

The sector has three strata. The scalar line is central and semisimple; the nilpotent stratum is the single similarity class of $J_2(0)$; the unipotent stratum is, for each scalar part, the single similarity class of $J_2(Q_t)$. On the two defective strata the minimal polynomial is $(X-Q_t)^2$, the eigenspace has dimension two, and there is no spectral decomposition and no eigenbasis. An adapted frame supplies a pair of idempotents and a pair of generators, and the quadruple $\mathcal{J}(\tilde Q)$ is a Jordan basis: the left and the right actions are each two blocks $J_2(Q_t)$, with different pairings, the four vectors are the matrix units of the coordinate model, and every biquaternion has a unique expansion. The exponential truncates, and the sector is closed under neither addition nor multiplication.

The two constructions are compared in the table.

| | regular, $B^2\neq0$ | degenerate, $B^2=0$, $\vec Q\neq0$ |
|---|---|---|
| root | $\vec\Xi=-i\vec Q/B$, with $\vec\Xi^2=e_t$ | none |
| idempotents | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the canonical pair of §*The Canonical Frame* |
| generators | a pair, up to reciprocal rescaling, then one normalisation | $\vec\Upsilon_-=\vec Q$, and $\vec\Upsilon_+$ is the unique element with $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ |
| left action | $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ | $J_2(Q_t)\oplus J_2(Q_t)$ |
| right action | $\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$ | $J_2(Q_t)\oplus J_2(Q_t)$, other pairing |
| coordinate matrix | $\operatorname{diag}(\lambda_+,\lambda_-)$ | $J_2(Q_t)$ |
| spectrum | two distinct eigenvalues | one eigenvalue, minimal polynomial $(X-Q_t)^2$ |
| dependence | the direction $[\vec Q]\in\mathbb{P}^2$ | the vector $\vec Q$ |

The Jordan basis is not the limit of the eigenbasis. The spectral idempotents diverge as $B\to0$; the new pair is selected by the definite Hermitian form, and the two constructions meet through the flag of the isotropic line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, complex dimension four, real dimension eight |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part |
| $\det\tilde Q=Q_t^2+B^2$ | the determinant |
| $\mathcal S=\{B^2=0\}$ | the spectrally degenerate sector |
| $\mathbb{B}\setminus\mathcal S=\{B^2\neq0\}$ | the spectrally regular sector |
| $\mathcal N=\{\det\tilde Q=0\}$ | the null cone, the zero-divisor set |
| $\Sigma_{ij}$ | the cell with $\det\tilde Q\neq0$ for $i=1$ and $B^2\neq0$ for $j=1$ |
| $\Sigma_{10}=\{Q_t\neq0\}$ | the unit half of the sector |
| $\Sigma_{00}=\{Q_t=0\}$ | the zero-divisor half of the sector |
| $\mathcal S^{\mathrm{s}}=\{\vec Q=0\}$ | the scalar stratum, the vertex |
| $\mathcal S^{\mathrm{n}}=\{\vec Q\neq0,\ Q_t=0\}$ | the nilpotent stratum |
| $\mathcal S^{\mathrm{u}}=\{\vec Q\neq0,\ Q_t\neq0\}$ | the unipotent stratum |
| $p_{\tilde Q}(X)=(X-Q_t)^2$ | the characteristic polynomial on the sector |
| $\mathsf{M}_2(\tilde Q)$ | the $2\times2$ matrix model, with $\det\tilde Q=Q_t^2+B^2$ |
| $J_2(Q_t)$ | the Jordan block of the defective strata |
| $\mathbb{C}[\vec Q]=\{ae_t+b\vec Q\}$ | the dual numbers, the centraliser of a defective element |
| $\tilde\Pi_\pm$ | the idempotents of an adapted frame; the canonical pair is $\vec Q\vec Q^*/(2\langle\vec Q\rangle_*)$ and $\vec Q^*\vec Q/(2\langle\vec Q\rangle_*)$ |
| $\vec\Upsilon_-=\vec Q$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ | the generators of the mixed corners, unique given the frame |
| $\mathcal{J}(\tilde Q)=(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$ | the Jordan basis, chain by chain; the corner order is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ |
| $\mathsf M_2^{\tilde Q}$ | the coordinate model of the Jordan basis, with $\mathsf M_2^{\tilde Q}(\tilde Q)=J_2(Q_t)$ |
| $\vec\Xi=-i\vec Q/B$ | the root of the regular sector, undefined on $\mathcal S$ |

## Further Reading

- [$M_2(\mathbb{C})$ Model : The Jordan Basis and the Jordanising Matrix](m2c-model-the-jordan-basis-and-the-jordanising-matrix.html), for the matrix form, the Jordanising matrix and the defect
- [$M_4(\mathbb{C})_L$ Model : The Jordan Basis and the Jordanising Matrix](m4c-model-the-jordan-basis-and-the-jordanising-matrix.html), for the $4\times4$ model
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the general Peirce construction and the Jordan basis as a particular Peirce matrix
- [The Spectrum](the-spectrum.html), for the spectral criterion, the cone, the three strata and the similarity classification
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the complementary sector and the eigenbasis construction
- [$M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix](m4c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the matrix reading of the eigenbasis
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the unit half as a cell, with the Peirce data and the degenerate limits of the eigenbasis
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the nilpotent half as a cell, with the same Peirce data
- [Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Degenerate Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the chain as the limit of a rescaled eigenbasis
- [Worked Examples of an Eigenbasis of a Biquaternion](worked-examples-of-an-eigenbasis-of-a-biquaternion.html), for the explicit constructions in coordinates
- [The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion](the-one-sided-operators-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the degenerate operator on the two-sided module
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm and its partition
- [The N-Regular Sector](the-n-regular-sector.html) and [The N-Degenerate Sector](the-n-degenerate-sector.html), for the two halves of the norm partition
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the vanishing modulus and the partial isometry
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four cells and the independence of the two cones
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, its coordinates and its conjugations
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the matrix model, the determinant and the trace
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential and its truncated form
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
