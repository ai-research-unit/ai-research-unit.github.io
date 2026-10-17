# __The Krein Form and Its Physical Interpretation__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four forms, one to each of its four general
products, and the fourth is the **Krein form**

$$
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu P_\mu\overline{Q_\mu}=P_t\overline{Q_t}-P_x\overline{Q_x}-P_y\overline{Q_y}-P_z\overline{Q_z},
$$

the gauge form of the framework: Hermitian, indefinite, of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over
$\mathbb{R}$, real at its two equal arguments, and unable to normalise a state. The four forms and their
readings are *The Four Forms, the Four Algebraic Norms and the Change of Scalars*; the general product
whose scalar part it is belongs to *The Products, Their Forms
and Their Norms*; and the band whose product is the form read on a pair is *The Biquaternioid Symmetric Quaternionic Sesqualgebra
(SQS) over $\mathbb{C}$*.

The form carries a whole indefinite structure, grouped in the mathematics menu under *The Krein Form*: the **fundamental
symmetry** that makes it a definite form in disguise, its **Gram matrix** and the signatures of its restrictions, its **isotropic
structure**, its **orthogonality** and the fundamental decomposition, and the **two cones** of its positivity. This article
collects those results, each with the mathematics article that owns it, and gives the physical interpretation of each. It proves
nothing; every result is owned on the mathematics side, and every reading is labelled as a reading.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$,
$e_t=1$, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$, and central imaginary $i$. An element is
$\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The conjugations are the natural one $\tilde Q^{\natural}$, the
coefficientwise one $\bar{\tilde Q}$ and the star $\tilde Q^{*}=\bar{\tilde Q}^{\natural}$; the sign vector is
$\varepsilon=(1,-1,-1,-1)$; the sectors are $\mathbb{M}_+=\{Q^{*}=Q\}$ and $\mathbb{M}_-=\{Q^{\flat}=Q\}$ with $\flat=-{}^{*}$;
$\|\tilde Q\|_E^{2}=\langle\tilde Q,\tilde Q\rangle_{*}$ is the Euclidean square; and $c,v$ are the centre and vector parts of an
element. All conventions are those of *Conventions in the Biquaternion Universe*.

## The Results

### The Form and Its Fundamental Symmetry

- **The fundamental symmetry.** The natural conjugation $J={}^{\natural}$ is a fundamental symmetry of the form: it is
$\mathbb{C}$-**linear**, $J^{2}=\mathrm{id}$, self-adjoint for the Krein form, and it carries the bridge identity
$\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,J\tilde Q\rangle_{*}$ from the indefinite form to the positive
definite Hermitian one. Owner: *The Fundamental Symmetry of the Biquaternioid Algebra*.
- **The eigenspaces and the family.** The eigenspaces of $J$ are the centre and the vector subspace, and they are the
**fundamental decomposition** of the algebra; all the other fundamental symmetries are parametrised by the open unit ball
$\lVert\tilde V\rVert_E<1$ of the vector subspace. Among them ${}^{\natural}$ alone is an **anti-automorphism** of the
algebra. Owner: *The Fundamental Symmetry of the Biquaternioid Algebra*.
- **The Pontryagin data.** The inertia of the form is $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, with negative
index $3$ and $6$ and Pontryagin index $1$ and $2$, so the algebra is a $\Pi_3$ space over $\mathbb{C}$ and a $\Pi_6$ one over
$\mathbb{R}$. Owner: *The Fundamental Symmetry of the Biquaternioid Algebra*.

### The Gram Matrix and the Restrictions

- **The Gram matrix.** In the coefficient basis the Gram matrix is the sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$ of
determinant $-1$, and in the real basis it is $\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$ of signature $(2,6)$; in the $2\times2$
model the form is the Hilbert–Schmidt pairing
$\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde P))$.
Owner: *The Krein Gram Matrix and the Restrictions of the Form*.
- **The restrictions.** By Sylvester's law the inertia is $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$; on the
remarkable subspaces the restriction is $(2,0)$ on the centre, $(0,6)$ on the vector subspace, and $(1,3)$ on each of the
quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces. Owner: *The Krein Gram Matrix and the Restrictions of the
Form*.
- **The complementarity.** The centre and the vector subspace are mutual Krein-orthogonal complements, and the discriminant is of
class $-1$ over $\mathbb{R}$. Owner: *The Krein Gram Matrix and the Restrictions of the Form*.

### The Isotropic Structure

- **The null set.** The **Krein null set** is
$\mathcal{K}=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural*}=0\}=\{\lVert c\rVert_E=\lVert v\rVert_E\}$, a real cone of
dimension $7$, non-singular off the apex. Owner: *The Isotropic Structure of the General Quaternionic Sesqualgebra*.
- **The comparison with the zero-divisor cone.** The zero-divisor cone of the algebraic norm is a real cone of dimension $6$,
and it meets the Krein null set in the union of the **doubly-null lines** $\mathbb{C}(e_t\pm i\hat\mu)$ over the real unit
directions $\hat\mu$, a cone of real dimension $4$; those lines are exactly the Peirce lines of the rank-one Hermitian idempotents.
Owner: *The Isotropic Structure of the General Quaternionic Sesqualgebra*.
- **The totally isotropic subspaces.** The Witt index is $\min(1,3)=1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; the maximal
isotropic complex line is $\mathbb{C}(e_t+\vec e_x)$ and the maximal isotropic real plane is
$\mathrm{span}_\mathbb{R}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$. Owner: *The Isotropic Structure of the General Quaternionic Sesqualgebra*.

### The Krein Orthogonality and the Fundamental Decomposition

- **The complement.** Two elements are Krein-orthogonal when their form vanishes, and a subspace and its Krein-orthogonal
complement satisfy $\dim\mathbb{W}+\dim\mathbb{W}^{\perp_K}=4$ over $\mathbb{C}$, with non-degeneracy exactly when
$\mathbb{W}\cap\mathbb{W}^{\perp_K}=\{0\}$. Owner: *Krein Orthogonality and the Fundamental Decomposition*.
- **The classification.** A subspace is definite, neutral, degenerate or totally isotropic according to the inertia of the
restricted form; the neutral plane is $\mathrm{span}_\mathbb{R}\{e_t+\vec e_x,e_t-\vec e_x\}$ and the complex dimension bounds are
$1$ and $3$. Owner: *Krein Orthogonality and the Fundamental Decomposition*.
- **The fundamental decomposition and the projections.** The maximal positive definite subspaces are the lines
$\mathbb{C}(e_t+\tilde V)$ with $\lVert\tilde V\rVert_E<1$; the decomposition $\mathbb{W}\perp_K\mathbb{W}^{\perp_K}$ carries its
fundamental symmetry $J_{\mathbb{W}}$, and the $J$-self-adjoint idempotents are exactly the Krein-orthogonal projections onto
the non-degenerate subspaces, a class strictly larger than the definite-orthogonal projections that commute with $J$.
Owner: *Krein Orthogonality and the Fundamental Decomposition*.

### The Indefinite Positivity and the Krein Cone

- **The Krein cone.** On the elements the set of non-negative Krein square,
$P_K=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural*}\ge0\}=\{\lVert c\rVert_E\ge\lVert v\rVert_E\}$, is a cone whose
boundary is the Krein null set; it is closed but neither convex nor pointed. Owner: *Indefinite Positivity and the Krein Cone of
the Biquaternioid Algebra*.
- **The Hermitian cone inside it.** The intersection of $P_K$ with the Hermitian subspace is the full light cone of the interval
form, and its future nappe is the Hermitian cone $P=\{\tilde Q^{*}\tilde Q\}$ of the dagger; hence $P\subseteq P_K$. Owner:
*Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*.
- **The operator cone.** On the operators the $J$-positive cone
$\mathcal{P}_J=\{T=T^{\dagger}:\langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0\}=J\cdot\{S\ge0\}$ is closed and convex, stable
under sums and $J$-adjoints, and contains $J$ but not the identity;
the $J$-projections are exactly the Krein-orthogonal projections onto the non-degenerate subspaces, and the
$J$-Cartan involution $\theta_J(T)=(T^{\dagger})^{-1}$ has the fixed group $U_J(\mathbb{B})\cong \mathrm{U}(1,3)$. Owner:
*Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*.

## Physical Interpretation

- **The gauge form pairs two frames and never ranks them.** It is indefinite — positive on the centre directions and negative
on the vector ones — so it fixes no overall sign and ranks nothing. It normalises nothing: its real value at equal arguments
carries a signature and is not a weight. The definite companion that carries a weight is the Hermitian form
$\langle\tilde P,\tilde Q\rangle_{*}$, the Born pairing, and the two are the invariant pair of the frame — the same pair the
gauge band reads as a product.
- **On matter, the gauge form and the interval are one form read with a sign.** On the material sector the Krein form is minus
the interval, $\langle\cdot,\cdot\rangle_{\natural*}=-\langle\cdot,\cdot\rangle_{\natural}$, so the gauge calibration of matter
is minus the spacetime interval; the light cone of the interval is the Krein null cone of the gauge form, and the level sets of
one are the level sets of the other up to sign. The framework reads this as the statement that the metric of the material sector
and the form of the frame are the same algebra object, the sign being the whole of their difference; on the informational sector
the two coincide.
- **The fundamental symmetry is the frame's own parity.** The gauge form is the definite Hermitian form transported by
$J={}^{\natural}$, the natural conjugation that fixes the scale and reverses every direction. Physically this is the parity of
the frame: the split of the algebra into the clock direction (the centre) and the spatial directions (the vector subspace). That
${}^{\natural}$ alone is an anti-automorphism of the algebra is the statement that the gauge's parity is not an extra choice but
the algebra's own involution, the one that respects the multiplication.
- **The sign vector is the gauge itself and not an index.** The metric of the series is the sign vector $\varepsilon$ inside the
product, so no index is raised and none is lowered, and the gauge is a permanent $(1,3)$: one sense of scale and three of
direction. The framework reads the Minkowski-type sign pattern as carried by the algebra and not imposed from outside — it is
the natural conjugation of the first slot that installs the sign, exactly as the star of the second slot installs the bar.
- **The gauge null cone is not the zero-divisor cone.** Over the complex space the Krein null cone (dimension $7$) and the
zero-divisor cone (real dimension $6$) are two different sets and neither contains the other: $e_t+\vec e_x$ is gauge-null
with interval $2$, and $\vec e_x+i\vec e_y$ has interval $0$ with gauge square $-2$. They meet exactly on the doubly-null
lines $\mathbb{C}(e_t\pm i\hat\mu)$, the Peirce lines of the rank-one Hermitian idempotents, which generate the minimal
ideals. On the material sector, where the gauge form is minus the interval, the two null sets coincide with the light cone,
so the distinction is a property of the complex space and not of a sector.
- **Orthogonality is indefinite, so a projection is a frame and not a metric.** Two subspaces can be gauge-orthogonal and still
meet, and a projection is Krein-orthogonal — self-adjoint for the form — exactly when it projects onto a non-degenerate
subspace. The maximal positive definite subspaces are the lines $\mathbb{C}(e_t+\tilde V)$ with
$\lVert\tilde V\rVert_E<1$, the time axes of observers. Physically: a gauge projection is fixed by the form together with the chosen time line, so two observers with
different time lines project differently, and the Krein Gram–Schmidt is the frame-dependent form of the orthogonalisation.
- **The positivity of the gauge is twofold, and its identity is the frame reflection.** The Krein cone is a causal structure and
not a state space: it is closed but not convex and not pointed, and it carries the interval's light cone on the informational
sector. The operator cone $J\cdot\{S\ge0\}$ contains $J$ and not the algebra unit, so the "identity" of the gauge is the frame
reflection. Physically: the gauge's positivity is transported by the reflection of the vector directions, which is why the gauge
compares frames and never counts states — the counting is the Hermitian form's work.

## Summary

The Krein form $\langle\tilde P,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ is the fourth form of
the biquaternion algebra, the indefinite Hermitian gauge form of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over
$\mathbb{R}$. Its structure is fivefold and is owned on the mathematics side: the fundamental symmetry $J={}^{\natural}$ with the
bridge to the definite form, the Gram matrix and the signatures of the restrictions, the isotropic structure with the doubly-null
lines, the Krein orthogonality and the fundamental decomposition with the Krein-orthogonal projections, and the two cones of the
indefinite positivity. On the material sector the form is minus the interval, so the metric and the gauge form are one object read
with a sign; the readings above are the framework's, each labelled, and none of them is a proof.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, the gauge form; signature $(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector, the gauge inside the product |
| $E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of the form in the coefficient basis |
| $J={}^{\natural}$ | the fundamental symmetry, $\mathbb{C}$-linear, $J^{2}=\mathrm{id}$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,J\tilde Q\rangle_{*}$ | the bridge from the indefinite form to the definite one |
| $\mathcal{K}=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ | the Krein null set, of real dimension $7$ |
| $\mathbb{C}(e_t\pm i\hat\mu)$ | the doubly-null lines, crossing of the Krein and the zero-divisor cones |
| $\mathbb{C}(e_t+\tilde V)$, $\lVert\tilde V\rVert_E<1$ | the maximal positive definite subspaces, the time axes |
| $P_K=\{\lVert c\rVert_E\ge\lVert v\rVert_E\}$ | the Krein cone; closed, not convex, not pointed |
| $\mathcal{P}_J=J\cdot\{S\ge0\}$ | the $J$-positive operator cone, containing $J$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | the informational and material sectors; $K=\langle\cdot,\cdot\rangle_{\natural}$ on $\mathbb{M}_+$ and $K=-\langle\cdot,\cdot\rangle_{\natural}$ on $\mathbb{M}_-$ |
| $\mathrm{U}(1,3)$ | the fixed group of the $J$-Cartan involution |

## Further Reading

- The mathematics group *The Krein Form* (`maths.md`), for the five articles whose results are listed above: *The Fundamental
Symmetry of the Biquaternioid Algebra*, *The Krein Gram Matrix and the Restrictions of the Form*, *The Isotropic Structure of the
General Quaternionic Sesqualgebra*, *Krein Orthogonality and the Fundamental Decomposition* and *Indefinite Positivity and the
Krein Cone of the Biquaternioid Algebra*.
- Mathematics article *The Fundamental Symmetry of the Biquaternioid Algebra*
(`articles_maths/the-fundamental-symmetry-of-the-biquaternioid-algebra.md`), for the symmetry $J={}^{\natural}$, the bridge and
the Pontryagin data.
- Mathematics article *The Krein Gram Matrix and the Restrictions of the Form*
(`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Gram matrix, the inertia and the
restrictions.
- Mathematics article *The Isotropic Structure of the General Quaternionic Sesqualgebra*
(`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the null set, the Witt index and
the doubly-null lines.
- Mathematics article *Krein Orthogonality and the Fundamental Decomposition*
(`articles_maths/krein-orthogonality-and-the-fundamental-decomposition.md`), for the complement, the classification and the
projections.
- Mathematics article *Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*
(`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternioid-algebra.md`), for the two cones and the $J$-Cartan
involution.
- Companion article *The Four Forms, the Four Algebraic Norms and the Change of Scalars*, for the four forms, their signatures and
their readings.
- Companion article *The Biquaternion Mathematics Corpus*, for the mathematics corpus as a whole and for the principle that no
result is owned on the physics side.
