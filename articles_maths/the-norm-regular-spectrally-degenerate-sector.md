# __The Norm-Regular, Spectrally Degenerate Sector__

## Introduction

This is cell $10$ of the four-sector arrangement of the two quadratic conditions

$$
N(\tilde Q)=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

the sector on which the quaternionic norm does not vanish and the vector square does. It is the difference of the spectral-degenerate cone and the null cone,

$$
\Sigma_{10}=\mathcal S\setminus\mathcal N,
$$

and it is one of the two **mixed** sectors: the two cells on which the norm problem and the spectral problem give different answers. Its partner is $\Sigma_{01}=\mathcal N\setminus\mathcal S$; the two together are the witness that the problems are independent. The vocabulary, the two cones and the naming convention are those of *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra* and *Spectral Regularity and Degeneracy in the Biquaternion Algebra*. The opposite corner $\Sigma_{00}$ is treated in *The Norm-Degenerate, Spectrally Degenerate Sector* and $\Sigma_{01}$ in *The Norm-Degenerate, Spectrally Regular Sector*.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and $\tilde Q=Q_te_t+\vec Q$; the conjugation is ${}^{\natural}$; the quaternionic norm is $N(\tilde Q)=\tilde Q^{\natural}\tilde Q$, central; and the product is the plain product unless stated otherwise. The null cone is $\mathcal N=\{N=0\}$; the spectral-degenerate cone is $\mathcal S=\{B^2=0\}$; **spectrally degenerate** means $B^2=0$, and it is a statement about the spectrum, not about diagonalisability.

## Definition and Characterisation

**Definition.** The sector $\Sigma_{10}$ is

$$
\Sigma_{10}=\{N\neq0,\ B^2=0\}=\{Q_t^2+B^2\neq0,\ B^2=0\}.
$$

**Theorem (five descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\tilde Q\in\Sigma_{10}$;

(ii) $B^2=0$ and $Q_t\neq0$;

(iii) $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $Q_t\in\mathbb{C}^\times$ and $\vec\Upsilon$ a pure nilpotent, $\vec\Upsilon^2=0$;

(iv) $\tilde Q=Q_tu$ with $Q_t\in\mathbb{C}^\times$ and $u$ a unipotent element, $(u-e_t)^2=0$;

(v) $\tilde Q$ is a unit whose two eigenvalues coincide at $Q_t$.

*Proof.* (i) $\iff$ (ii): on $B^2=0$ one has $N=Q_t^2$, so $N\neq0$ exactly when $Q_t\neq0$. (ii) $\iff$ (iii): the vector part is pure, and $\vec Q^2=-B^2e_t=0$, so $\vec\Upsilon=\vec Q$ is nilpotent; conversely $B^2=0$ follows from $\vec\Upsilon^2=0$. (iii) $\iff$ (iv): $u=e_t+\vec\Upsilon$ has $u-e_t$ nilpotent, and conversely. (ii) $\iff$ (v): with $B^2=0$ the characteristic polynomial is $X^2-2Q_tX+Q_t^2=(X-Q_t)^2$, so both eigenvalues are $Q_t$; and $N=Q_t^2\neq0$ makes $\tilde Q$ a unit.

**Corollary (positive characterisation).** The sector is the non-zero complex cone over the unipotent variety:

$$
\Sigma_{10}=\{Q_tu\ :\ Q_t\in\mathbb{C}^\times,\ (u-e_t)^2=0\}.
$$

The pair $(Q_t,u)$ is determined by $\tilde Q$: the scalar part gives $Q_t$, and $u=\tilde Q/Q_t$. So the description is a bijection.

**Corollary (automatic scalar part).** Every element of the sector has $Q_t\neq0$. The non-vanishing of the scalar part is not an extra condition: on $\mathcal S$ it is exactly the norm-regularity condition. The sector is the part of $\mathcal S$ on which the scalar part survives.

**Remark (two orbits).** The unipotent variety is $\{e_t\}$ together with a single orbit of the unit group: a non-zero pure nilpotent generates a minimal left ideal, and the unit group is transitive on the minimal left ideals. The sector is the union of the corresponding two orbits of $\mathbb{C}^\times\times\mathbb{B}^\times$ acting by scaling and inner automorphisms: the scalar line, and the cone over the non-trivial unipotents.

## Geometry

**Theorem (the cone and its vertex).** $\mathcal S=\{B^2=0\}$ is the cone in $\mathbb{C}^4$ over the smooth conic $\{Q_x^2+Q_y^2+Q_z^2=0\}\subset\mathbb{P}^2$, with vertex the scalar line $\mathbb{C}e_t$. Its singular locus is exactly that line. The sector $\Sigma_{10}=\mathcal S\setminus\Sigma_{00}\subset\mathcal S$ is Zariski-open, of complex dimension $3$ and real dimension $6$, connected, and it contains the singular locus of $\mathcal S$ with the origin removed.

*Proof.* The gradient of $B^2$ is $2(0,\vec Q)$, which vanishes exactly on $\vec Q=0$, the scalar line; off that line the cone is smooth, and the projection to $\mathbb{P}^2$ exhibits it as the cone over the conic. In $\mathcal S$ one has $N=Q_t^2$, so $\mathcal N\cap\mathcal S=\{Q_t=0,\ B^2=0\}=\Sigma_{00}$, and $\Sigma_{10}=\{Q_t\neq0\}$ is Zariski-open in $\mathcal S$. Its dimension is that of $\mathcal S$, namely $4-1=3$ over $\mathbb{C}$ and $6$ over $\mathbb{R}$. It is connected because it is $\mathbb{C}^\times$ times the punctured nilpotent cone, both factors connected.

**Parametrisation.** The map

$$
\mathbb{C}^\times\times\{\vec\Upsilon\in\mathbb{C}^3:\vec\Upsilon^2=0\}\longrightarrow\Sigma_{10},\qquad (Q_t,\vec\Upsilon)\mapsto Q_t(e_t+\vec\Upsilon)
$$

is a bijection. The pure nilpotent cone is the cone over a smooth conic in $\mathbb{P}^2$, of complex dimension $2$ and real dimension $4$; the $\mathbb{C}^\times$ factor adds $2$ real dimensions. The count is $2+4=6$, in agreement with the theorem.

**Remark (a cone with the apex removed).** The sector is stable under every non-zero complex scalar and under no zero scalar: $0\cdot\tilde Q=0$ lies in $\Sigma_{00}$. It is a cone with its apex deleted, and the apex belongs to its closure.

**Remark (two pieces, one of them singular).** The scalar line $\{\vec Q=0\}\cap\Sigma_{10}$ is the vertex of $\mathcal S$ minus its apex; it lies in the sector and is part of its singular locus. The Jordan part $\{\vec Q\neq0\}$ is the smooth part of $\mathcal S$. This is the geometric origin of the split in the next section.

## The Two Regimes

The sector is not homogeneous in its spectral behaviour, although it is homogeneous under the unit group. It splits by the vector part:

$$
\Sigma_{10}=\Sigma_{10}^{\mathrm{s}}\sqcup\Sigma_{10}^{\mathrm{J}}.
$$

This split is the spectral refinement of the sector, and it is exactly the pair of zones called scalar and Jordan in the five-zone classification.

### The scalar line

**Definition.** $\Sigma_{10}^{\mathrm{s}}=\{\tilde Q=Q_te_t\ :\ Q_t\in\mathbb{C}^\times\}$.

**Properties.** These elements are central and semisimple, with minimal polynomial $X-Q_t$, not $(X-Q_t)^2$: the eigenvalue is repeated but the element is diagonalisable. The centraliser is all of $\mathbb{B}$, and every idempotent commutes with $\tilde Q$. The spectral idempotent is $e_t$ itself, and it is unique; what is **not unique** is its refinement: every orthogonal pair $\tilde\Pi_1+\tilde\Pi_2=e_t$ gives

$$
\tilde Q=Q_t\tilde\Pi_1+Q_t\tilde\Pi_2
$$

with the same coefficient on both terms, and the pair is not determined by $\tilde Q$. The adapted Peirce decomposition exists only in the **one-term** form $\tilde Q=Q_te_t$; every two-term refinement is non-unique.

This is the sharpest warning in the arrangement: $\mathcal S$ is not the locus of non-diagonalisable elements. The identity $e_t$ lies here, with $Q_t=1$, spectrum $\{1\}$ and a repeated eigenvalue, and it is a unit. The punctured scalar line is the only place in the algebra where a non-zero element admits several two-term Peirce decompositions with commuting idempotents.

### The Jordan part

**Definition.** $\Sigma_{10}^{\mathrm{J}}=\{\tilde Q=Q_te_t+\vec\Upsilon\ :\ Q_t\in\mathbb{C}^\times,\ \vec\Upsilon\neq0,\ \vec\Upsilon^2=0\}$.

**Properties.** These elements are defective. From $(\tilde Q-Q_te_t)^2=\vec\Upsilon^2=0$ and $\tilde Q\neq Q_te_t$, the minimal polynomial is $(X-Q_t)^2$: a single Jordan block of size two with eigenvalue $Q_t$.

**Centraliser.** An element $X=x_0e_t+\vec x$ commutes with $\tilde Q$ exactly when $\vec x\times\vec\Upsilon=0$, that is, exactly when $\vec x$ is a multiple of $\vec\Upsilon$. The centraliser is therefore the plane

$$
\mathbb{C}[\tilde Q]=\{a e_t+b\vec\Upsilon\ :\ a,b\in\mathbb{C}\}\cong\mathbb{C}[\varepsilon]/(\varepsilon^2),
$$

the dual numbers. Its only idempotents are $0$ and $e_t$: from $a^2=a$ and $2ab=b$ one obtains $(a,b)=(0,0)$ or $(1,0)$. Hence **no non-trivial idempotent commutes with $\tilde Q$**, and $\tilde Q$ admits **no adapted Peirce decomposition**.

**Peirce form.** A non-zero nilpotent generates a minimal left ideal, so there is an idempotent $e$ with $\vec\Upsilon=e\vec\Upsilon(e_t-e)$. Relative to that $e$ the Peirce form of $\tilde Q$ is diagonal plus off-diagonal:

$$
e\tilde Qe=Q_te,\qquad
e\tilde Q(e_t-e)=\vec\Upsilon,\qquad
(e_t-e)\tilde Qe=0,\qquad
(e_t-e)\tilde Q(e_t-e)=Q_t(e_t-e).
$$

The semisimple part $Q_te_t$ is diagonal and the nilpotent part sits wholly in one mixed corner. This is the closest available structure to a spectral decomposition, and it is not one: the off-diagonal component does not vanish.

**The spectral decomposition.** It exists only on the scalar line, and only in the one-term form $\tilde Q=Q_te_t$; the two-projector refinement is non-unique. On the Jordan part it fails: the only idempotents in the centraliser are $0$ and $e_t$, so no pair of non-trivial orthogonal idempotents summing to $e_t$ is adapted to $\tilde Q$. There is no eigenbasis either: the eigenspace of $L_{\tilde Q}$ for $Q_t$ is the left annihilator of $\vec\Upsilon$, a complex plane of dimension $2$, and a basis of eigenvectors would need four independent vectors in it.

**Powers and inverse.** From $(\tilde Q-Q_te_t)^2=\vec\Upsilon^2=0$, for $n\geq1$,
$$
\tilde Q^n=Q_t^ne_t+nQ_t^{n-1}\vec\Upsilon,\qquad
\tilde Q^{-1}=\frac{1}{Q_t}e_t-\frac{1}{Q_t^2}\vec\Upsilon.
$$

### The split

$\Sigma_{10}^{\mathrm{s}}$ is a closed complex submanifold of the sector, of complex dimension $1$; its complement $\Sigma_{10}^{\mathrm{J}}$ is open and dense, of complex dimension $3$. The scalar part is central and semisimple, the Jordan part is regular in the sense $\vec Q\neq0$ and defective. The union is the whole sector, and the two pieces meet only in the limit: a sequence of Jordan elements with $\vec\Upsilon\to0$ converges to a point of the scalar line.

## Peirce Data

**The sector contains two Peirce behaviours. On the scalar line every idempotent is adapted and the Peirce matrix is $Q_tI$. On the Jordan part no non-trivial idempotent commutes with $\tilde Q$, and the Peirce matrix relative to a nilpotent-generated idempotent is a single Jordan block.**

### Peirce data on the scalar line

Let $\tilde Q=Q_te_t$ with $Q_t\neq0$. Every idempotent commutes with $\tilde Q$, so every idempotent is adapted. Relative to any complete pair $(e,f)$,

$$
e\tilde Qe=Q_te,\qquad
e\tilde Qf=0,\qquad
f\tilde Qe=0,\qquad
f\tilde Qf=Q_tf,
$$

and the Peirce matrix is $Q_tI$ in every Peirce basis. The spectral decomposition has one term, $\tilde Q=Q_te_t$; a two-term refinement $Q_t\tilde\Pi_1+Q_t\tilde\Pi_2$ exists for every orthogonal pair summing to $e_t$ and is not determined by $\tilde Q$. The Peirce data therefore see a repeated eigenvalue as a repeated diagonal entry, and the freedom of the refinement as the freedom of the Peirce pair.

### Peirce data on the Jordan part

Let $\tilde Q=Q_te_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ and $Q_t\neq0$. Its centraliser is $\mathbb{C}[\tilde Q]=\{ae_t+b\vec\Upsilon\}$, the dual numbers, whose only idempotents are $0$ and $e_t$. Hence no non-trivial idempotent commutes with $\tilde Q$ and there is no adapted Peirce decomposition.

A non-zero nilpotent generates a minimal left ideal, so there is an idempotent $e$ with $\vec\Upsilon=e\vec\Upsilon(e_t-e)$. With $f=e_t-e$ the Peirce form is

$$
e\tilde Qe=Q_te,\qquad
e\tilde Qf=\vec\Upsilon,\qquad
f\tilde Qe=0,\qquad
f\tilde Qf=Q_tf.
$$

The semisimple part is diagonal and the nilpotent part lies in one mixed corner; in the corner coordinates fixed by $(e,\vec\Upsilon)$ and $(f,\vec X)$, where $\vec X$ spans $f\mathbb{B}e$, the Peirce matrix of $\tilde Q$ is the single block

$$
\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}=J_2(Q_t).
$$

**No Q-adapted basis.** The construction needs a root $\vec\Xi=-i\vec Q/B$, and here $B=0$. The root is undefined, no Peirce pair is attached to $\tilde Q$, and there is no Q-adapted Peirce basis. This is the spectral particularity of the sector: the norm is non-zero, so the element is a unit, and still no Peirce basis is attached to it.

## Multiplication and Inversion

**Products stay off the null cone.** The norm is multiplicative, so for $\tilde P,\tilde Q\in\Sigma_{10}$,

$$
N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)\neq0,
$$

and the product lies in the unit group $\mathbb{B}^\times=\Sigma_{10}\sqcup\Sigma_{11}$. All three outcomes inside the unit group occur.

**Theorem (what products do).**

$$
\Sigma_{10}\cdot\Sigma_{10}\subseteq\Sigma_{10}\cup\Sigma_{11},
$$

and the product of two elements of the sector can lie in $\Sigma_{10}^{\mathrm{s}}$, can lie in $\Sigma_{10}^{\mathrm{J}}$, and can lie in $\Sigma_{11}$.

*Witnesses.* Write $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$. Then

$$
\tilde Q^2=Q_t^2(e_t+2\vec\Upsilon+\vec\Upsilon^2)=Q_t^2(e_t+2\vec\Upsilon),
$$

whose vector part squares to $4Q_t^2\vec\Upsilon^2=0$ and whose norm is $Q_t^4\neq0$: the square lies in $\Sigma_{10}$, and in $\Sigma_{10}^{\mathrm{J}}$ when $\vec\Upsilon\neq0$. For the scalar line, $Q_te_t\cdot Q'_te_t=QQ'_te_t\in\Sigma_{10}^{\mathrm{s}}$. For the exit to $\Sigma_{11}$, take

$$
\tilde P=e_t+\vec e_x+i\vec e_y,\qquad \tilde Q=e_t+i\vec e_x+\vec e_y,
$$

both in $\Sigma_{10}^{\mathrm{J}}$ since $1+i^2=0$ and $i^2+1=0$. Their product is

$$
\tilde P\tilde Q=(1-2i)e_t+(1+i)\vec e_x+(1+i)\vec e_y+2\vec e_z,
$$

with $B^2=4+4i\neq0$ and $N=1$. So the product lies in $\Sigma_{11}$.

**Inversion stays inside the sector.** Since $N(\tilde Q)=Q_t^2\neq0$, every element of the sector is a unit, with

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)}
=\frac{Q_t-\vec\Upsilon}{Q_t^2}
=\frac{1}{Q_t}(e_t-\vec\Upsilon).
$$

The element $-\vec\Upsilon$ is again nilpotent, so $\tilde Q^{-1}\in\Sigma_{10}$; it lies in the scalar line exactly when $\tilde Q$ does.

**Consequence.** The sector is **closed under inversion and not closed under multiplication**. It is a symmetric subset of the unit group, not a subgroup. The only part of it closed under both is the punctured scalar line $\Sigma_{10}^{\mathrm{s}}$, a subgroup isomorphic to $\mathbb{C}^\times$.

## Relation to the Two Cones

**The sector is the complement of one cone inside the other.** As point sets,

$$
\Sigma_{10}=\mathcal S\setminus\mathcal N,\qquad
\mathcal S=\Sigma_{00}\sqcup\Sigma_{10}.
$$

The closure of $\Sigma_{10}$ is $\mathcal S$; the boundary it loses is exactly $\Sigma_{00}$, the nilpotent stratum.

**Transversality, and where it fails.** The gradients are

$$
\nabla N=2(Q_t,\vec Q),\qquad \nabla B^2=2(0,\vec Q).
$$

On the Jordan part both are non-zero and they are proportional only if $Q_t=0$; since $Q_t\neq0$ there, the two hypersurfaces meet transversally along $\Sigma_{10}^{\mathrm{J}}$. On the scalar line $\nabla B^2=0$: the spectral cone is singular there, so transversality is not defined, and the sector runs along the vertex of $\mathcal S$. The tangency of the two cones is confined to $\Sigma_{00}$, where the two gradients coincide.

**Independence witness.** Every element of the sector is a **unit with a repeated eigenvalue**. The standard examples are

$$
\tilde Q=e_t+\vec e_x+i\vec e_y,\qquad N=1,\qquad B^2=0,\qquad (\tilde Q-e_t)^2=0,
$$

a single Jordan block with eigenvalue $1$, and the identity $e_t$ itself, a semisimple unit with a repeated eigenvalue and no defect at all. Neither is a zero divisor; both lie on the spectral-degenerate cone. This is the half of the independence proof that the null cone cannot supply.

**Vertex warning.** The singular locus of $\mathcal S$ is the scalar line, and $\Sigma_{10}$ contains all of it except the origin. The scalar part is semisimple. So $\mathcal S$, and this sector in particular, is **not** the set of non-diagonalisable elements; that set is the union of the Jordan part and the nilpotent stratum. Spectral degeneracy is the vanishing of the discriminant, not the failure of diagonalisability.

## Comparison with the Other Three Sectors

| sector | conditions | elements | spectrum | adapted Peirce | product |
|---|---|---|---|---|---|
| **doubly regular** $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | units with distinct eigenvalues | $\{\lambda_+,\lambda_-\}$, distinct, non-zero | exists, unique | stays in $\mathbb{B}^\times$; can land in $\Sigma_{10}$ |
| **norm-degenerate, spectrally regular** $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | $c\tilde\Pi$, $\tilde\Pi$ a non-trivial idempotent | $\{c,0\}$ | exists, unique | stays on $\mathcal N$; all three outcomes |
| **norm-regular, spectrally degenerate** $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | $Q_tu$, $u$ unipotent | $\{Q_t\}$, repeated | fails on $\Sigma_{10}^{\mathrm{J}}$; one-term and non-unique on $\Sigma_{10}^{\mathrm{s}}$ | stays in $\mathbb{B}^\times$; can land in $\Sigma_{11}$ |
| **doubly degenerate** $\Sigma_{00}$ | $N=0$, $B^2=0$ | non-zero nilpotents of index two, plus the origin | $\{0\}$ | fails off the origin | $0$ or $\Sigma_{01}$ |

**The two mixed sectors.** $\Sigma_{01}$ and $\Sigma_{10}$ are the independence witnesses: $\Sigma_{01}$ is a zero divisor with a full eigenbasis, $\Sigma_{10}$ is a unit with none. Neither cone contains the other, and these are the cells that show it.

**Position in the five-zone refinement.** The five zones of *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*, §*The Five Zones*, sit with respect to the sectors as follows.

| zone | condition | sector |
|---|---|---|
| **distinct** | $B^2\neq0$, $N\neq0$ | $\Sigma_{11}$ |
| **zero divisor** | $B^2\neq0$, $N=0$ | $\Sigma_{01}$ |
| **scalar** | $\vec Q=0$ | $\Sigma_{10}^{\mathrm{s}}\cup\{0\}$ |
| **Jordan** | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\Sigma_{10}^{\mathrm{J}}$ |
| **nilpotent** | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\Sigma_{00}\setminus\{0\}$ |

Sector $10$ is therefore not a zone: it is the Jordan zone together with the scalar zone **minus the origin**, and the missing point of the scalar zone belongs to $\Sigma_{00}$. This is why the four-sector table and the five-zone table cannot be merged: the finer spectral split cuts through one sector and moves a point of another.

## Consequences

**Eigenbasis.** It fails on the Jordan part, where the element is a single Jordan block; it exists trivially on the scalar line, where the one-term decomposition into eigenspaces is all there is and any two-term refinement is non-unique. There is no genuine two-term spectral decomposition anywhere in the sector.

**Polar decomposition.** It exists throughout the sector, because $N\neq0$ and the modulus $\Rho=\sqrt{N(\tilde Q)}\neq0$ is defined; the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Biquaternions* applies. This is the sector's positive feature and its sharpest contrast with $\Sigma_{01}$: there the eigenbasis exists and the polar decomposition does not; here the polar decomposition exists and the eigenbasis does not.

**One-sided operators.** Since $\tilde Q$ is a unit, $L_{\tilde Q}$ and $R_{\tilde Q}$ are bijections of complex rank $4$, with zero kernel, and both annihilators are $\{0\}$. The spectral defectivity is invisible to the one-sided structure: on $\Sigma_{10}$ and on $\Sigma_{11}$ alike, both multiplications are invertible. No ideal-theoretic condition can detect a repeated eigenvalue.

**The degenerate half of the unit group.** The unit group splits as $\mathbb{B}^\times=\Sigma_{10}\sqcup\Sigma_{11}$. The sector $\Sigma_{10}$ is the degenerate half: closed under inversion, not under multiplication, and made of the units whose two eigenvalues have merged.

## Summary

| question | answer |
|---|---|
| definition | $\Sigma_{10}=\{N\neq0,\ B^2=0\}$ |
| descriptions | $\mathcal S\setminus\mathcal N$; $Q_t\neq0$ on $\mathcal S$; $Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$; $Q_tu$ with $u$ unipotent; unit with spectrum $\{Q_t\}$ |
| geometry | Zariski-open in $\mathcal S$; complex cone of complex dimension $3$ and real dimension $6$; connected; contains the punctured scalar line, the singular locus of $\mathcal S$ |
| regimes | $\Sigma_{10}^{\mathrm{s}}$: scalar, semisimple, non-unique spectral idempotents, dimension $1$, closed; $\Sigma_{10}^{\mathrm{J}}$: Jordan, defective, dual-number centraliser, dimension $3$, open dense |
| adapted Peirce | fails on the Jordan part; one-term and non-unique on the scalar line |
| annihilators | both zero: the element is a unit |
| multiplication | $\Sigma_{10}\cdot\Sigma_{10}\subseteq\Sigma_{10}\cup\Sigma_{11}$, with all three outcomes; inverse-closed, not product-closed |
| relation to the cones | $\Sigma_{10}=\mathcal S\setminus\mathcal N$; transverse on the Jordan part; singular on the scalar line; tangency only on $\Sigma_{00}$ |
| place in the arrangement | the Jordan zone plus the punctured scalar zone: units with a repeated eigenvalue |

The sector is the unipotent sector. It is the non-zero scalar cone over the unipotent elements, the complement of the nilpotent stratum inside the spectral-degenerate cone, and the degenerate half of the unit group. Its elements are exactly the units whose two eigenvalues are equal: invertibility survives, the spectral separation fails. It contains, in its scalar line, the identity and the whole singular locus of the spectral cone, and it is the sharpest reminder that spectral degeneracy and non-diagonalisability are not the same property.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{ij}$ | the sector with $i=1$ iff $N\neq0$, $j=1$ iff $B^2\neq0$ |
| $\Sigma_{10}$ | the norm-regular, spectrally degenerate sector, this article |
| $\mathcal N=\{N=0\}$ | the null cone of the quaternionic norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{10}^{\mathrm{s}}=\mathbb{C}^\times e_t$ | the scalar line |
| $\Sigma_{10}^{\mathrm{J}}$ | the Jordan part, $\vec\Upsilon\neq0$ |
| $\vec\Upsilon$ | a pure nilpotent, $\vec\Upsilon^2=0$ |
| $u=e_t+\vec\Upsilon$ | a unipotent element, $(u-e_t)^2=0$ |
| $Q_t$ | the scalar part, non-zero on the sector |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication, both invertible on the sector |

## Further Reading

- [The Norm-Degenerate, Spectrally Degenerate Sector](the-norm-degenerate-spectrally-degenerate-sector.html), for $\Sigma_{00}$, the nilpotents and the origin.
- [The Norm-Degenerate, Spectrally Regular Sector](the-norm-degenerate-spectrally-regular-sector.html), for the partner mixed sector $\Sigma_{01}$, the scaled idempotents.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the null cone, its two strata and the unit group.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the discriminant and the spectral-degenerate cone.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the five zones and the comparison of the two cones.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the Peirce corners and the minimal left ideals.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus $\Rho=\sqrt N$ and the unit factor.
