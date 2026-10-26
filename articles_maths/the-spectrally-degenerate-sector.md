# __The Spectrally Degenerate Sector__

## Introduction

The biquaternion algebra carries two quadratic conditions. The first is the quaternionic norm $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$, whose zero set is the null cone and whose two halves are *The N-Regular Sector* and *The N-Degenerate Sector*. The second is the square of the vector part,

$$
B^2=Q_x^2+Q_y^2+Q_z^2,
$$

whose zero set is the **spectrally degenerate sector**

$$
\mathcal S=\{B^2=0\}.
$$

This article studies that sector as a set. It is the complement of the sector on which the eigenbasis is constructed: *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion* treats $B^2\neq0$, where the two eigenvalues are distinct and the Peirce basis exists; the present article treats $B^2=0$, where they coincide and no such basis exists.

The sector is the union of two cells of the four-cell arrangement,

$$
\mathcal S=\Sigma_{10}\sqcup\Sigma_{00},
$$

and each cell has its own article: *The N-Regular, Spectrally Degenerate Sector* for $\Sigma_{10}$ and *The N-Degenerate, Spectrally Degenerate Sector* for $\Sigma_{00}$. The cell articles compute the Peirce data, the generators and the comparison with the other cells. This article treats what the two cells have in common: the equation, the strata, the geometry, the matrix form, the multiplicative behaviour, and the way the sector sits inside the polar decomposition and inside the norm partition.

**The word degenerate refers to the spectrum only.** It says that the two eigenvalues coincide, not that the element is a zero divisor and not that the element fails to be diagonalisable. Two warnings fix the reading. The scalar line $\mathbb C e_t$ lies in the sector, and its points are central, hence semisimple; the origin is diagonalisable as well. The defective elements form the **Jordan part** $\mathcal S^{\mathrm n}\cup\mathcal S^{\mathrm u}$ of the sector, a proper subset. Conversely, an element outside the sector can be a zero divisor: the Hermitian idempotent $\tfrac12(e_t+i\vec u)$ with $\vec u\cdot\vec u=1$ has $B^2=-\tfrac14$ and $N=0$. Spectral degeneracy and degeneracy of the product are independent conditions.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, of complex dimension four and real dimension eight, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$, and central scalar imaginary $i$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$ and the Hermitian conjugation is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$; the product is the plain product, with unit $e_t$. The **quaternionic norm** is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$, written $N$ when no ambiguity arises. A **sector** is one of the two halves selected by one condition; a **cell** is one of the four intersections $\Sigma_{ij}$, with $i=1$ for $N\neq0$ and $i=0$ for $N=0$, and $j=1$ for $B^2\neq0$ and $j=0$ for $B^2=0$.

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

*Proof.* The identity $\vec Q^2=-B^2e_t$ gives (i)$\iff$(ii). The characteristic polynomial of *Spectral Regularity and Degeneracy in the Biquaternion Algebra* is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2,
$$

of discriminant $-4B^2$ and roots $Q_t\pm iB$; hence (i), (iii), (iv) and (v) are the same equation read in four ways. ∎

**Corollary (the spectral data).** On the sector the eigenvalue is $Q_t$, the trace is $2Q_t$, the determinant and the norm are

$$
\det\mathsf{M}_2(\tilde Q)=N=Q_t^2,
$$

and the spectrum is the single point $\{Q_t\}$: the two roots have merged, so no symmetric function of them can separate them.

**Remark (three readings of one equation).** The equation is **geometric** — the vector part is isotropic, $(\vec Q,\vec Q)=0$ for the complex bilinear form of the vector subspace; **algebraic** — the vector part is square-zero, hence nilpotent of index two when it is non-zero; and **spectral** — the discriminant vanishes. The three readings are those of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral-Degenerate Cone*, where the proofs and the stratification are given in full.

**Remark (a closed cone, not a subspace).** The sector is a complex cone: it is closed under multiplication by scalars, since $B^2$ is homogeneous of degree two. It is not closed under addition, since $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ both lie in it while their sum $2\vec e_x$ does not. It is a proper algebraic subset, of empty interior in $\mathbb{B}$.

## The Norm inside the Sector

**The norm is not an independent condition on the sector: it is the square of the scalar part.**

**Theorem (the norm on the sector).** For $\tilde Q\in\mathcal S$,

$$
N=Q_t^2.
$$

*Proof.* The definition gives $N=Q_t^2+B^2$, and $B^2=0$ on the sector. ∎

**Corollary (the sector splits by the scalar part).** The norm cuts $\mathcal S$ into exactly two halves,

$$
\Sigma_{10}=\mathcal S\setminus\mathcal N=\{Q_t\neq0\},\qquad
\Sigma_{00}=\mathcal S\cap\mathcal N=\{Q_t=0\},
$$

and on the sector the three conditions "$N\neq0$", "$Q_t\neq0$" and "$\tilde Q$ is a unit with repeated eigenvalue" are equivalent.

*Proof.* By the theorem, $N=Q_t^2$. A complex square vanishes exactly when its argument does. The last equivalence is the criterion of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, which identifies $N\neq0$ with invertibility. ∎

**Corollary (both kinds of element).** The sector contains units and zero divisors. Its unit half is $\Sigma_{10}$; its zero-divisor half is $\Sigma_{00}\setminus\{0\}$, the nilpotent stratum. Hence spectral degeneracy is not a form of non-invertibility: every element of $\Sigma_{10}$ is invertible, with inverse

$$
\tilde Q^{-1}=Q_t^{-1}\left(e_t-\frac{\vec Q}{Q_t}\right).
$$

**Remark (the norm as the squared eigenvalue).** The norm is the product of the eigenvalues. On the sector the two eigenvalues are equal to $Q_t$, so the product is $Q_t^2$; the identity of the theorem is the spectral reading of that product, not a new constraint.

## The Three Strata

**Definition (the strata).** On $\mathcal S$ put

$$
\mathcal S^{\mathrm{s}}=\{\vec Q=0\},\qquad
\mathcal S^{\mathrm{n}}=\{Q_t=0,\ \vec Q\neq0\},\qquad
\mathcal S^{\mathrm{u}}=\{Q_t\neq0,\ \vec Q\neq0\},
$$

the **scalar**, **nilpotent** and **unipotent** strata. The union $\mathcal S^{\mathrm{n}}\cup\mathcal S^{\mathrm{u}}$ is the **Jordan part** of the sector; its complement, the scalar stratum, is the common vertex.

**Theorem (a disjoint union).** $\mathcal S=\mathcal S^{\mathrm{s}}\sqcup\mathcal S^{\mathrm{n}}\sqcup\mathcal S^{\mathrm{u}}$.

*Proof.* Either $\vec Q=0$, or $\vec Q\neq0$; in the second case either $Q_t=0$ or $Q_t\neq0$. The three conditions are exclusive and exhaustive. ∎

**Theorem (the normal forms).** The three strata have the following normal forms and invariants; $m_{\tilde Q}$ is the minimal polynomial and $L_{\tilde Q}$ is left multiplication.

| stratum | condition | normal form | $m_{\tilde Q}$ | $\operatorname{rank}L_{\tilde Q}$ | centraliser | $N$ |
|---|---|---|---|---|---|---|
| **scalar** | $\vec Q=0$ | $Q_te_t$ | $X-Q_t$ | $4$, or $0$ at the origin | $\mathbb{B}$ | $Q_t^2$ |
| **nilpotent** | $Q_t=0$, $\vec Q\neq0$ | $\vec Q$, with $\vec Q^2=0$ | $X^2$ | $2$ | $\mathbb{C}[\vec Q]$ | $0$ |
| **unipotent** | $Q_t\neq0$, $\vec Q\neq0$ | $Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon=\vec Q/Q_t$ | $(X-Q_t)^2$ | $4$ | $\mathbb{C}[\vec Q]$ | $Q_t^2$ |

*Proof.* The scalar stratum is immediate: the element is central, with the stated minimal polynomial, and left multiplication is $Q_t\,\mathrm{id}$, of rank $4$, or zero at the origin. On the other two strata $\vec Q^2=0$ and $\vec Q\neq0$, so $\tilde Q-Q_te_t$ is non-zero with square zero; the minimal polynomial is $(X-Q_t)^2$ and the centraliser is that of $\vec Q$, the dual numbers $\mathbb{C}[\vec Q]=\{ae_t+b\vec Q\}$, of complex dimension two. On the nilpotent stratum the element is a non-zero square-zero element, not a unit, and its minimal polynomial is $X^2$; on the unipotent stratum $u=e_t+\vec\Upsilon$ is unipotent, so $\tilde Q=Q_tu$ is a unit with inverse $Q_t^{-1}(e_t-\vec\Upsilon)$. Left multiplication by a non-zero square-zero element has image contained in its kernel, and both spaces have complex dimension two, so the rank is two; on the units the rank is four. ∎

**Corollary (the spectral behaviour).** The spectral data are collected in the table.

| stratum | spectrum | spectral decomposition | eigenspace | eigenbasis |
|---|---|---|---|---|
| **scalar** | $\{Q_t\}$ | one term, unique | $\mathbb{B}$, of dimension $4$ | every basis |
| **nilpotent** | $\{0\}$ | none | $\ker L_{\vec Q}$, of dimension $2$ | none |
| **unipotent** | $\{Q_t\}$ | none | $\ker L_{\vec Q}$, of dimension $2$ | none |

*Proof.* A two-term spectral decomposition needs two non-trivial orthogonal idempotents commuting with $\tilde Q$. On the two defective strata the centraliser is the dual numbers, whose only idempotents are $0$ and $e_t$; on the scalar stratum the element is central, and the canonical one-term writing is the only decomposition. The eigenspace is $\ker L_{\tilde Q}=\ker L_{\vec Q}$, which is all of $\mathbb{B}$ on the scalar stratum and has dimension two on the other two, by the rank computation of the preceding theorem. ∎

**Proposition (similarity).** Under the inner automorphisms of $\mathbb{B}$ each stratum is a union of orbits indexed by the scalar part: the scalar stratum has one orbit for each $Q_t\in\mathbb{C}$, the unipotent stratum has one orbit for each $Q_t\in\mathbb{C}^\times$, and the nilpotent stratum is a single orbit. The origin is its own orbit.

*Proof.* The scalar part is invariant under every automorphism, since automorphisms fix the centre. On the scalar stratum the element is central, so its orbit is a point. On the unipotent stratum, $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$; the group $\mathrm{PGL}_2(\mathbb{C})$ acts transitively on the non-zero square-zero elements, by the matrix picture below, so all unipotents with the same $Q_t$ are conjugate. The same argument applies to the nilpotent stratum with $Q_t=0$; the origin is fixed. ∎

**Remark (three strata, two halves).** The norm split and the stratum split do not agree on the sector. The scalar stratum straddles the two halves: the origin lies in $\Sigma_{00}$, while every other point $Q_te_t$, $Q_t\neq0$, lies in $\Sigma_{10}$. The unipotent stratum is exactly $\Sigma_{10}\setminus\mathbb{C}^\times e_t$, and the nilpotent stratum is exactly $\Sigma_{00}\setminus\{0\}$. Thus

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

A Jordan basis of $L_{\vec Q}$ needs two vectors outside the kernel whose images span it; the quotient $\mathbb{B}/\ker L_{\vec Q}$ is two-dimensional, but no splitting of it is determined by $\vec Q$. This is the structural reason the eigenbasis fails on the sector: the isotropic line admits no canonical complement, so there is no canonical second spectral direction.

## The Matrix Picture

Under $\mathsf{M}_2$ of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure* the sector becomes the set of matrices whose two eigenvalues coincide. The characteristic polynomial is $(X-Q_t)^2$, the trace is $2Q_t$ and the determinant is $Q_t^2$. The Jordan form is determined by the minimal polynomial:

| stratum | $\mathsf{M}_2(\tilde Q)$ | Jordan form | rank |
|---|---|---|---|
| **scalar**, $Q_t\neq0$ | $Q_t\mathrm{I}_2$ | $Q_t\mathrm{I}_2$ | $2$ |
| **scalar**, origin | $0$ | $0$ | $0$ |
| **nilpotent** | a non-zero matrix of square zero | $J_2(0)$ | $1$ |
| **unipotent** | $Q_t(\mathrm{I}_2+N)$, $N^2=0$, $N\neq0$ | $J_2(Q_t)$ | $2$ |

**Proposition (diagonalisability).** An element of the sector is diagonalisable exactly when it lies on the scalar line. Off that line the minimal polynomial is $(X-Q_t)^2$, of degree two, while the characteristic polynomial has the same two roots; the matrix is a single Jordan block.

**Remark (not a determinantal variety).** The null cone is the determinantal variety of rank at most one, so the rank is a complete invariant of it. The spectral-degenerate sector is not of that kind: it contains matrices of rank two (the units of $\Sigma_{10}$), of rank one (the nilpotents) and of rank zero (the origin). Its defining equation is the discriminant, not a rank condition, and its strata are distinguished by the minimal polynomial and the scalar part rather than by the rank alone.

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

which has $B^2=1$ and $N=1$: it lies in the doubly regular cell $\Sigma_{11}$, outside the sector. ∎

**Remark (the unit half is not a group).** The product of two unipotents need not be unipotent, as the proposition shows. The unit half $\Sigma_{10}$ is therefore a union of similarity orbits closed under inversion, not a subgroup of $\mathbb{B}^\times$. The scalar line minus the origin is a subgroup, and the unipotent stratum is a single orbit for each scalar part, but the two do not compose within the sector.

**Proposition (the truncated exponential).** Let $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$. Then, for every complex $\theta$,

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\left(e_t+\theta\vec Q\right).
$$

*Proof.* The scalar part commutes with $\vec Q$ and $\vec Q^2=0$, so the exponential series truncates after the linear term. ∎

**Corollary (the exponential lands in the unit half).** For every $\tilde Q\in\mathcal S$ and every $\theta$, the exponential $e^{\theta\tilde Q}$ lies in $\Sigma_{10}$. In particular the exponential of a nilpotent is the unipotent $e_t+\theta\vec Q$, and the exponential of the origin is $e_t$.

*Proof.* The vector part of $e^{\theta\tilde Q}$ is $e^{\theta Q_t}\theta\vec Q$, whose square is zero; its scalar part is $e^{\theta Q_t}$, which is never zero. ∎

**Remark (no oscillation).** On the sector the exponential is polynomial in $\theta$: there is no frequency and no periodic term. The root-parametrised form $e^{\theta Q_t}(\cos(B\theta)e_t+\sin(B\theta)\rho)$ of the regular sector does not extend to $B=0$ as a formula in $\rho$, because the root $\rho=\vec Q/B$ does not exist; the entire form in $B$ does extend, and its value is the truncated expression above.

## The Polar Decomposition on the Sector

The sector straddles the two regimes of the polar decomposition, and the split is exactly the norm split of §*The Norm inside the Sector*.

**On $\Sigma_{10}$.** The element is a unit, $N=Q_t^2\neq0$, and the modulus $\Rho$ with $\Rho^2=N$ is non-zero. The modulus–unit form $\tilde Q=\Rho\tilde U$ and the four-factor word $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ exist, with $\tilde U$ unitary. The sector contributes to this regime the scalar line minus the origin and the unipotent stratum; the amplitudes and the phases are those of *The Polar Decomposition of a N-Regular Biquaternion*, read with the two eigenvalues equal.

**On $\Sigma_{00}$.** The element is a zero divisor, $N=Q_t^2=0$, and the modulus vanishes. The modulus–unit form and the four-factor word do not exist, because both divide by $\Rho$. What survives is the two-factor decomposition $\tilde Q=\tilde Q_H\tilde Q_0$ of *The Polar Decomposition of a Biquaternion*: the Hermitian factor $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}$ is positive semidefinite of rank at most one, and $\tilde Q_0$ is a partial isometry that is not unitary. The two cases, with the closed forms of the factors, are *The Polar Decomposition of a N-Degenerate Biquaternion*, §*The Two Sectors*.

**Remark (the determinant of the modulus).** In the matrix model $\det(\tilde Q\tilde Q^{*})=\lvert N\rvert^2=\lvert Q_t\rvert^4$, so the Hermitian factor is singular exactly on $\Sigma_{00}$. This is the polar form of the same split: invertibility of the modulus is invertibility of the element, and on the sector both are decided by $Q_t$.

## Relation to the Spectrally Regular Sector

The spectrally regular sector is the complement $\mathbb{B}\setminus\mathcal S=\{B^2\neq0\}$. It is open and dense, and it splits into the two cells

$$
\Sigma_{11}=\{N\neq0,\ B^2\neq0\},\qquad
\Sigma_{01}=\{N=0,\ B^2\neq0\}.
$$

On it the eigenvalues are distinct, the discriminant is non-zero, the root $\vec\Xi=-i\vec Q/B$ exists, and the eigenbasis of *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion* is constructed. None of these objects exists on $\mathcal S$: the two constructions are separated by the single equation $B^2=0$, and the passage from one to the other is the collapse of the two eigenvalues.

The four cells are collected in the table.

| cell | $N$ | $B^2$ | complex dimension | description |
|---|---|---|---|---|
| $\Sigma_{11}$ | $\neq0$ | $\neq0$ | $4$ | the generic unit, with distinct non-zero eigenvalues |
| $\Sigma_{10}$ | $\neq0$ | $=0$ | $3$ | the unit of the sector: $\mathbb{C}^\times e_t$ and the unipotents |
| $\Sigma_{01}$ | $=0$ | $\neq0$ | $3$ | the zero divisor with distinct eigenvalues, one of them zero |
| $\Sigma_{00}$ | $=0$ | $=0$ | $2$ | the nilpotents, with the origin adjoined |

**Remark (density and boundary).** The sector is closed with empty interior, so every point of it is a limit of points of the spectrally regular sector; it is the boundary of the open set on which the eigenbasis exists. The two conditions are independent, and the cells $\Sigma_{10}$ and $\Sigma_{01}$ are the witnesses: each is a non-empty open part of one cone on which the other condition is non-zero. The comparison of the two cones is *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*.

## Consequences

- **No splitting, no root, no frequency.** The two eigenvalues coincide at $Q_t$; the discriminant $-4B^2$ vanishes; the root $\vec\Xi=-i\vec Q/B$ and the frequency $B$ are undefined; the spectral projectors and the two-term spectral decomposition do not exist.
- **No eigenbasis off the scalar line.** The eigenspace has complex dimension two, the minimal polynomial is $(X-Q_t)^2$, and the isotropic line admits no canonical complement. Only the scalar line carries an eigenbasis, and there it is every basis.
- **A flag survives where a splitting fails.** The canonical objects are the line $\mathbb{C}\vec Q$, the plane $\vec Q^{\perp}$, the kernel–image space $\ker L_{\vec Q}=\operatorname{im}L_{\vec Q}$, and the two flags they form. A Jordan basis exists, but it is not canonical.
- **The truncated exponential survives.** On the sector the exponential is polynomial, $e^{\theta\tilde Q}=e^{\theta Q_t}(e_t+\theta\vec Q)$, and it maps the whole sector into its unit half $\Sigma_{10}$.
- **The norm is the square of the eigenvalue.** On the sector $N=Q_t^2$, so the norm partition restricted to the sector is the partition by the scalar part, and the sector is split into a unit half and a zero-divisor half by one complex number.
- **Spectral degeneracy is not non-invertibility.** $\Sigma_{10}$ consists of units; the scalar line is semisimple; only the Jordan part is defective. The sector is the discriminant locus, not the zero-divisor set and not the set of non-diagonalisable elements.
- **The sector is not a subalgebra.** It is a cone closed under scalars and, on its unit half, under inversion; it is closed under neither addition nor multiplication, and the exponential of a nilpotent is a unipotent outside the zero-divisor half.

## Summary

The spectrally degenerate sector is the set $\mathcal S=\{B^2=0\}$ on which the two eigenvalues of a biquaternion coincide. It is a complex cone of complex dimension three and real dimension six, the product of the scalar line and the isotropic cone of the vector subspace, singular exactly along the scalar line and smooth off it. It is connected, closed, of empty interior, and it is the boundary of the sector on which the eigenbasis exists.

The norm restricted to the sector is the square of the scalar part, $N=Q_t^2$. This one identity splits the sector into the unit half $\Sigma_{10}=\{Q_t\neq0\}$ and the zero-divisor half $\Sigma_{00}=\{Q_t=0\}$, and it shows that spectral degeneracy and degeneracy of the product are independent: the unipotent stratum consists of units with a repeated eigenvalue, while the idempotent $\tfrac12(e_t+i\vec u)$ is a zero divisor with distinct eigenvalues.

The sector has three strata. The scalar line is central and semisimple; the nilpotent stratum is the single similarity class of $J_2(0)$; the unipotent stratum is, for each scalar part, the single similarity class of $J_2(Q_t)$. On the two defective strata the minimal polynomial is $(X-Q_t)^2$, the eigenspace has dimension two, there is no spectral decomposition and no eigenbasis, and the canonical objects are the isotropic line and the flag. The exponential truncates, the polar decomposition keeps its two factors and loses its modulus, and the sector is closed under neither addition nor multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, complex dimension four, real dimension eight |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part |
| $\langle\tilde Q\rangle_{\natural}=N=Q_t^2+B^2$ | the quaternionic norm |
| $\mathcal S=\{B^2=0\}$ | the spectrally degenerate sector |
| $\mathbb{B}\setminus\mathcal S=\{B^2\neq0\}$ | the spectrally regular sector |
| $\mathcal N=\{N=0\}$ | the null cone, the $N$-degenerate sector |
| $\Sigma_{ij}$ | the cell with $N\neq0$ for $i=1$ and $B^2\neq0$ for $j=1$ |
| $\Sigma_{10}=\mathcal S\setminus\mathcal N$ | the unit half of the sector |
| $\Sigma_{00}=\mathcal S\cap\mathcal N$ | the zero-divisor half of the sector |
| $\mathcal S^{\mathrm{s}}=\{\vec Q=0\}$ | the scalar stratum, the vertex |
| $\mathcal S^{\mathrm{n}}=\{Q_t=0,\ \vec Q\neq0\}$ | the nilpotent stratum |
| $\mathcal S^{\mathrm{u}}=\{Q_t\neq0,\ \vec Q\neq0\}$ | the unipotent stratum |
| $p_{\tilde Q}(X)=(X-Q_t)^2$ | the characteristic polynomial on the sector |
| $\mathsf{M}_2(\tilde Q)$ | the $2\times2$ matrix model, with $\det=N$ |
| $J_2(Q_t)$ | the Jordan block of the defective strata |
| $\mathbb{C}[\vec Q]=\{ae_t+b\vec Q\}$ | the dual numbers, the centraliser of a defective element |
| $\vec\Xi=-i\vec Q/B$ | the root of the regular sector, undefined on $\mathcal S$ |
| $\Rho^2=N$ | the modulus, vanishing on $\Sigma_{00}$ |

## Further Reading

- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the cone, the three strata and the similarity classification
- [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the complementary sector and the construction that fails here
- [The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations](the-spectrally-regular-sector-and-eigenbasis-of-a-biquaternion-in-matrix-element-representations.html), for the matrix reading of the eigenbasis
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the unit half as a cell
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the nilpotent half as a cell
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm and its partition
- [The N-Regular Sector](the-n-regular-sector.html) and [The N-Degenerate Sector](the-n-degenerate-sector.html), for the two halves of the norm partition
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the vanishing modulus and the partial isometry
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four cells and the independence of the two cones
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, its coordinates and its conjugations
- [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](m2c-representation-the-matrix-product-and-the-algebra-structure.html), for the matrix model, the determinant and the trace
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential and its truncated form
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
