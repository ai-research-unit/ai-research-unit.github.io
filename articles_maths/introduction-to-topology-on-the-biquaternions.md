# __Introduction to Topology on the Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is an eight-dimensional real space that carries a product, and the corpus reads it through four distinguished forms. Each form is the scalar part of one of the four products of *The Four Biquaternion Complex Products*, each is a non-degenerate pairing of the algebra with itself, and each carries a layer of structure: a signature, a zero set, a family of level sets and a group of isometries. The topology region is divided into the sub-categories *Topology Induced by the Bilinear Form*, *Topology Induced by the Hermitian Form* and *Topology Induced by the Krein Form*; those three develop three of the four forms, and this article is their common entry point and presents the fourth beside them.

It introduces no theorem. The four forms are defined and compared, as forms, in *The Four Biquaternion Complex Products*, *Relations Between the Four Biquaternion Products* and *The Three Pairings of the Biquaternion Algebra*; every result quoted below is proved in the article that owns it, and each section names the articles of its layer. What this article states is the situation the layers share — one algebra, four forms, four readings that do not coincide — and the sense in which each form induces a topology. It assumes the algebra and its conjugations from *Biquaternions as a Vector Space over $\mathbb{C}$* and the group they generate from *The Group of Involutions*, the four products from *The Four Biquaternion Complex Products*, and the two functions $N$ and $\lVert\cdot\rVert_E$ from *Biquaternion Norm and Invertibility*. No physics is invoked.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$ satisfying $e_k^{2}=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and with central scalar imaginary $i$, $i^{2}=-1$. A general element and its three conjugates are

$$
\tilde{Q}=Q_0+Q_1e_1+Q_2e_2+Q_3e_3,\qquad Q_0,Q_1,Q_2,Q_3\in\mathbb{C},
$$

$$
\tilde{Q}^{\natural}=Q_0-Q_1e_1-Q_2e_2-Q_3e_3,\qquad
\tilde{Q}^{*}=\bar{Q}_0-\bar{Q}_1e_1-\bar{Q}_2e_2-\bar{Q}_3e_3,\qquad
\bar{\tilde{Q}}=\bar{Q}_0+\bar{Q}_1e_1+\bar{Q}_2e_2+\bar{Q}_3e_3,
$$

so that ${}^{*}={}^{\natural}\circ\bar{\cdot}$, and $\mathrm{Sc}(\tilde{Q})=Q_0$ is the scalar part. The region reads **four forms**, the scalar parts of the four products of *The Four Biquaternion Complex Products*, and it writes them with **one bracket** $\langle\cdot,\cdot\rangle$ only. The subscript of the bracket records which conjugation enters each argument: the natural conjugation ${}^{\natural}$, when it appears, is applied to the first argument, and the complex conjugation $\bar{\cdot}$, when it appears, to the second argument.

$$
\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}).
$$

They are the **complex bilinear form**, the **quaternion bilinear form**, the **complex sesquilinear form** and the **quaternion sesquilinear form**. In coordinates, with $\varepsilon=(1,-1,-1,-1)$,

$$
\langle\tilde{P},\tilde{Q}\rangle=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_{\mu=0}^{3}P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu\overline{Q_\mu}.
$$

The two bilinear forms are linear in each argument; the two sesquilinear forms are linear in the first argument and conjugate-linear in the second. On the diagonal $\tilde{P}=\tilde{Q}$ they give the four quadratic readings

$$
\langle\tilde{Q},\tilde{Q}\rangle=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},\qquad
\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2},
$$

$$
\langle\tilde{Q},\tilde{Q}\rangle_{*}=\lvert Q_0\rvert^{2}+\lvert Q_1\rvert^{2}+\lvert Q_2\rvert^{2}+\lvert Q_3\rvert^{2}=\lVert\tilde{Q}\rVert_E^{2},\qquad
\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2}.
$$

The prefixes name the conjugation the form is built from and not a signature or a base field: *complex* marks a form in which no natural conjugation enters and *quaternion* one in which it enters in the first argument, while *bilinear* marks linearity in both arguments and *sesquilinear* the entry of the complex conjugation in the second. This naming is the only one used in this region. The words *Minkowski*, *Hermitian* and *Krein* are not used as names here, the first because it is available only over the reals and the other two because they name a symmetry and a signature rather than the algebraic structure the form is built from.

## The Four Forms

The four forms are one family cut out by two independent choices: whether the natural conjugation ${}^{\natural}$ is inserted in the first argument, and whether the complex conjugation ${}^{*}$ is inserted in the second. The four products of *The Four Biquaternion Complex Products* are exactly the four products that result, and the four forms are their scalar parts. They are collected here with the data each is read from.

| form | product | bracket | in coordinates | diagonal | linearity |
|---|---|---|---|---|---|
| complex bilinear | $\tilde{P}\tilde{Q}$ | $\langle\tilde{P},\tilde{Q}\rangle$ | $\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | $\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | linear in both arguments |
| quaternion bilinear | $\tilde{P}^{\natural}\tilde{Q}$ | $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | $\sum_\mu P_\mu Q_\mu$ | $\sum_\mu Q_\mu^{2}=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | linear in both arguments |
| complex sesquilinear | $\tilde{P}\tilde{Q}^{*}$ | $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\sum_\mu P_\mu\overline{Q_\mu}$ | $\sum_\mu\lvert Q_\mu\rvert^{2}=\lVert\tilde{Q}\rVert_E^{2}$ | linear in the first, conjugate-linear in the second |
| quaternion sesquilinear | $\tilde{P}^{\natural}\tilde{Q}^{*}$ | $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$ | $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | linear in the first, conjugate-linear in the second |

The four are mutually determined, and the passage from the plain forms to the quaternion ones is the insertion of the natural conjugation in the first argument,

$$
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\langle\tilde{P}^{\natural},\tilde{Q}\rangle,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\langle\tilde{P}^{\natural},\tilde{Q}\rangle_{*},
$$

while the passage from a bilinear form to its sesquilinear companion is the insertion of the complex conjugation in the second, $\langle\tilde{P},\bar{\tilde{Q}}\rangle=\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$ and $\langle\tilde{P},\bar{\tilde{Q}}\rangle_{\natural}=\langle\tilde{P},\tilde{Q}\rangle_{*}$. Each form is symmetric or conjugate-symmetric in the two arguments, and each is non-degenerate; they are nevertheless pairwise distinct, and no one of them is a deformation of another.

## What a Pairing Induces

A non-degenerate pairing determines four objects, and they are the objects each layer of this region is built from.

- the **real form on the diagonal**, $\tilde{Q}\mapsto\langle\tilde{Q},\tilde{Q}\rangle$ or its real part, together with its signature, which decides whether the pairing is definite or indefinite;
- the **null set** $\{\tilde{Q}:\Phi(\tilde{Q},\tilde{Q})=0\}$ and the **level sets** $\{\tilde{Q}:\Phi(\tilde{Q},\tilde{Q})=c\}$;
- the **isometry group**, of the linear maps preserving the pairing; and
- the **subgroups cut out by the diagonal**, wherever the level set of a multiplicative form is a group.

Each layer reads these four objects from its own form, and the objects do not agree. The disagreement is the content of the region, and it begins with the meaning of the word *topology*.

**Remark (every non-degenerate pairing yields a distance, and the four distances coincide).** A real-valued form gives a norm through its diagonal only when the diagonal is positive definite, and among the four only the complex sesquilinear form is. But no non-degenerate form is without a distance: a **symmetry** of the form $\Phi$ — an involution $J$ with $\Phi(J\tilde{P},J\tilde{Q})=\Phi(\tilde{P},\tilde{Q})$ and $\Phi(\tilde{Q},J\tilde{Q})>0$ off zero — makes $\mathrm{Re}\,\Phi(\tilde{P},J\tilde{Q})$ an inner product, and every non-degenerate form has one, by Sylvester. For the four forms the symmetries are the four involutions $\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}$, and each returns the complex sesquilinear form: all four forms produce the **same** distance, the Euclidean one, and the complex sesquilinear form is merely the one that needs no symmetry. The three sub-categories are named for the structure each form induces beyond that common distance — its signature, its null set, its level sets, its isometry group — and not for three inequivalent topologies on one set. The full argument is *Four Forms but One Topology on the Biquaternion Algebra*; the quaternion bilinear norm $N$ decides the units and the complex sesquilinear form the topology (*The Biquaternion Unit Group as a Topological Group*, §*The Topology of the Group*).

## The Complex Bilinear Form

The complex bilinear form $\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q})=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ is the polarisation of the quadratic form $\sum_\mu\varepsilon_\mu Q_\mu^{2}$. It is $\mathbb{C}$-bilinear, symmetric and non-degenerate, and it is the one form of the four that carries no conjugation at all. Its Gram matrix is $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, of complex signature $(1,3)$, and its realification is the split form of signature $(4,4)$ — the signature of the quaternion bilinear form, which it shares. Its diagonal vanishes on the non-zero $\tilde{Q}=e_0+e_1$, so it is indefinite; its null set $\{\sum_\mu\varepsilon_\mu Q_\mu^{2}=0\}$ is a complex cone of real dimension $6$; and its isometry group is the complex orthogonal group $O_4(\mathbb{C})$, the same abstract group as that of the quaternion bilinear form, the two forms being equivalent over $\mathbb{C}$.

The form has no sub-category of its own in the region. It is the second bilinear reading, the partner of the quaternion bilinear form in the pair of two, and it is the scalar bilinear form of *Association and the Transpose on the Biquaternion Algebra*, where its Gram matrix $\mathrm{E}$, its signature and its association law are developed. Its distance comes from the symmetry ${}^{*}$, which returns the complex sesquilinear form, $\langle\tilde{P},\tilde{Q}^{*}\rangle=\langle\tilde{P},\tilde{Q}\rangle_{*}$ (§*What a Pairing Induces*).

## The Quaternion Bilinear Form

The quaternion bilinear form is the polarisation of the biquaternion norm, $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$. It is $\mathbb{C}$-bilinear, symmetric and non-degenerate, and it takes complex values, as does the complex bilinear form; its realification is the split form of signature $(4,4)$. Its restriction to the six distinguished real subspaces carries the signatures $(1,1)$ on the centre, $(3,3)$ on the vector subspace, $(4,0)$ on the quaternion subspace, $(0,4)$ on the anti-quaternion subspace, and $(1,3)$ and $(3,1)$ on the Hermitian and anti-Hermitian subspaces.

Its diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ is complex-valued and multiplicative, so it is not itself a norm; the distance of this layer comes from the symmetry $c=\bar{\cdot}$, which returns the complex sesquilinear form, $\langle\tilde{P},\bar{\tilde{Q}}\rangle_{\natural}=\langle\tilde{P},\tilde{Q}\rangle_{*}$ (§*What a Pairing Induces*). It decides invertibility — an element is a unit exactly when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ — and its vanishing defines the **null cone**

$$
\mathcal{N}=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}=\{0\}\cup\mathcal{Z},
$$

where $\mathcal{Z}$ is the zero-divisor set. The cone is a complex hypersurface in $\mathbb{B}\cong\mathbb{C}^{4}$, of real dimension $6$, and the origin is its only singular point; away from the apex it is a smooth complex $3$-manifold, and it is the set on which the algebra fails to be a division algebra. Its complement is the group of units $\mathbb{B}^\times=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0\}$, open and dense. The level set $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1$ is the **norm-one group** $\mathbb{B}^\times_1$, a closed non-compact subgroup of real dimension $6$: in this layer the *unit sphere* is a group, and it is not bounded.

Three further structures belong to the layer. The **Clifford algebra** of the quadratic form $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, with its spinors and its Fierz–Kofink identities. The **projective geometry** of the null cone: its link, the quadric $Q^{2}$ and the Klein–Plücker geometry of the lines of $\mathbb{P}^{3}$. And the **isometry group** $O_4(\mathbb{C})$, of real dimension $12$. The layer is developed in *Biquaternion Norm and Invertibility*, *The Clifford Structure of the Biquaternion Algebra*, *Biquaternion Topology*, *The Biquaternion Unit Group as a Topological Group* and *Biquaternion Orders and Finite Groups of Units*; the sub-category also gathers the coordinate realizations of the element — *Biquaternion Four-Vector Element Representation*, *Biquaternion Polar Element Representation* and *Biquaternion Partial Polar Element Representations* — whose content is algebraic and is not read here.

## The Complex Sesquilinear Form

The complex sesquilinear form is the one definite form of the four, and it is the canonical source of the ambient topology: it is the one form that is already an inner product in the bracket convention of this region, so its distance needs no symmetry to be read (§*What a Pairing Induces*). Its diagonal is $\sum_\mu\lvert Q_\mu\rvert^{2}$, positive definite, and its real part

$$
(\tilde{P},\tilde{Q})_{\mathbb{R}}=\mathrm{Re}\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_{\mu=0}^{3}\bigl(p_\mu q_\mu+p'_\mu q'_\mu\bigr)
$$

is a Euclidean inner product on $\mathbb{B}\cong\mathbb{R}^{8}$. The associated **Euclidean norm** $\lVert\cdot\rVert_E$ gives the metric, the balls, the completeness and the **Euclidean topology** in which every topological statement of the corpus is made; the coefficient map is a linear isometry onto $\mathbb{R}^{8}$.

Two level sets of this layer are distinguished. The **Euclidean unit sphere** $S^{7}_{E}=\{\lVert\tilde{Q}\rVert_E=1\}$ is a genuine $S^{7}$, compact and connected, but it is not a group: $\lVert\cdot\rVert_E$ is not multiplicative, and $S^{7}_{E}$ contains zero divisors, its intersection with the null cone being the link of that cone. The other is the **unitary group**

$$
U(\mathbb{B})=\{\tilde{Q}:\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)\cong S^{1}\times S^{3},
$$

a compact Lie group, and it is the maximal compact subgroup onto which the group of units deformation retracts. Unlike the sphere $S^{7}_{E}$, it lies inside the units.

The layer owns the Euclidean structure and the contractibility of the algebra and of the six distinguished subspaces; the unitary group and the polar decomposition; the retraction of the group of units and its homotopy, with $\pi_1\cong\mathbb{Z}$, $\pi_2=0$, $\pi_3\cong\mathbb{Z}$ and universal cover $\mathbb{R}\times S^{3}$; and the Hermitian modules, the positivity cone and the unitary Witt group. Its articles are *The Hermitian Form on the Biquaternion Algebra*, *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*, *The Euclidean Topology of the Biquaternion Algebra*, *The Unitary Group of the Biquaternion Algebra*, *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* and their companions.

## The Quaternion Sesquilinear Form

The quaternion sesquilinear form $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ is conjugate-symmetric and indefinite, of signature $(2,6)$ over $\mathbb{R}$ and $(1,3)$ over $\mathbb{C}$. Its positive part is the centre $\mathbb{C}_{\mathbb{B}}$ and its negative part the vector subspace $\mathbb{V}_{\mathbb{B}}$; the two are orthogonal in the form and complementary,

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}},
$$

the **fundamental decomposition**. The natural conjugation ${}^{\natural}$ is a self-adjoint involution of the form, and it plays the role of the **fundamental symmetry** $J$: it turns the quaternion sesquilinear form into the positive definite complex sesquilinear one by the bridge identity

$$
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\langle\tilde{P}^{\natural},\tilde{Q}\rangle_{*}.
$$

The algebra is thereby a Krein space of complex dimension four and negative index three, a Pontryagin space $\Pi_6$ over $\mathbb{R}$.

The **null set** $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}$ is a real cone of real dimension $7$, and it is a different object from the null cone: it contains $\tilde{Q}=e_0+e_1$, which is no zero divisor, and it omits $\tilde{Q}=e_1+ie_2$, which is one; the two cones cross on elements such as $\tilde{Q}=e_0+ie_1$. The level set $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1$ is a hyperboloid, and the maximal totally isotropic subspace has real dimension $2$, so the Witt index is $2$ over $\mathbb{R}$ and $1$ over $\mathbb{C}$.

The layer owns the signature and the fundamental decomposition; the isotropic and totally isotropic subspaces; the level sets and the hyperbolic structure; and the operators the form defines — the $J$-self-adjoint, the $J$-unitary and the $J$-normal operators and the indefinite spectral theorem. Its articles are *The Biquaternion Krein Form and Its Signature*, *The Fundamental Symmetry of the Biquaternion Algebra*, *The Three Pairings of the Biquaternion Algebra*, *The Krein Gram Matrix and the Restrictions of the Form*, *Krein Orthogonality and the Fundamental Decomposition*, *The Isotropic Structure of the Krein Form* and *The Krein Level Sets and the Hyperbolic Structure*, with their operator companions.

## The Four Forms Compared

The four forms are collected in one table. Each row is a pairing; the entries are the objects of §*What a Pairing Induces*, read from that pairing; the signatures are those of the underlying real form.

| form | bracket | Gram matrix | signature over $\mathbb{R}$ | definiteness | null set | level set $\Phi=1$ | isometry group |
|---|---|---|---|---|---|---|---|
| complex bilinear | $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | $\mathrm{E}$ | $(4,4)$ | indefinite | $\{\sum_\mu\varepsilon_\mu Q_\mu^{2}=0\}$, real dimension $6$ | the complex quadric $\sum_\mu\varepsilon_\mu Q_\mu^{2}=1$ | $O_4(\mathbb{C})$ |
| quaternion bilinear | $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$ | $\mathrm{I}_4$ | $(4,4)$ | indefinite | the null cone $\mathcal{N}$, real dimension $6$ | the group $\mathbb{B}^\times_1$ | $O_4(\mathbb{C})$ |
| complex sesquilinear | $\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu}$ | $\mathrm{I}_4$ | $(8,0)$ | positive definite | $\{0\}$ | the sphere $S^{7}_{E}$, not a group | $U(4)$ |
| quaternion sesquilinear | $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | $\mathrm{E}$ | $(2,6)$ | indefinite | the null set of the form, real dimension $7$ | a hyperboloid | $U(1,3)$ |

**Remark (the four are pairwise distinct and mutually determined).** No two of the four forms agree: the two bilinear forms are complex-valued while the two sesquilinear forms are conjugate-linear in the second argument, and the Gram matrices $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$ and the signatures $(4,4),(4,4),(8,0),(2,6)$ separate the rows. They are nevertheless one family, related by the identities of §*The Four Forms*, and they carry the four involutions $\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}$ as their symmetries. **The layers are four readings of one algebra, and none is a deformation of another.**

**Remark (the four rows give one distance, four level sets).** Each row yields a distance, and the four distances coincide, so the table carries one metric and not four; what differs from row to row is the *level set* the diagonal singles out. The complex sesquilinear row has a positive definite diagonal and its level set is the genuine $S^{7}_{E}$; the other three rows have indefinite diagonals whose *level sets* are a complex quadric, the group $\mathbb{B}^\times_1$ and a hyperboloid rather than a sphere. This is the table form of the caution of §*What a Pairing Induces*.

## The Matrix Picture

The $2\times2$ realization $\Phi$ of *Biquaternion 2×2 Matrix Element Representation* carries the four forms to four pairings of matrices, with the trace in place of the scalar part and the adjugate and the conjugate transpose marking the two non-plain cases. Since $\Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q})$ and $\Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger}$, the four readings are the plain trace product with either matrix conjugation in the first slot and either in the second,

$$
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\Phi(\tilde{Q})\bigr),\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})\,\Phi(\tilde{Q})\bigr),\qquad
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\,\Phi(\tilde{Q})^{\dagger}\bigr),\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})\,\Phi(\tilde{Q})^{\dagger}\bigr),
$$

and they reproduce the complex bilinear, the quaternion bilinear, the complex sesquilinear and the quaternion sesquilinear form respectively. The realization converts the Euclidean norm into the Frobenius norm, $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$, and converts the level set of the quaternion bilinear form into the determinant locus: $\mathbb{B}^\times\cong GL_2(\mathbb{C})$ and $\mathbb{B}^\times_1=\{N=1\}\cong SL_2(\mathbb{C})$. The four readings of the six distinguished subspaces are *The Centre Subspace under the Three Topologies* and its five companions, and the four readings of the two realizations are *The 2×2 Matrix Representation under the Three Topologies* and *The 4×4 Regular Matrix Representation under the Three Topologies*; the matrix form of the four forms themselves is *The Forms in the Matrix Representation of the Biquaternion Algebra*.

## Summary

The biquaternion algebra is one algebra with four distinguished forms, the scalar parts of the four products of *The Four Biquaternion Complex Products*. The complex bilinear form $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ carries no conjugation, with Gram matrix $\mathrm{E}$ and realification of signature $(4,4)$; its diagonal is the quadratic form $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, its null set is the complex cone $\{\sum_\mu\varepsilon_\mu Q_\mu^{2}=0\}$ of real dimension $6$, and its isometry group is $O_4(\mathbb{C})$. The quaternion bilinear form $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$ is the polarisation of the norm $N$, with Gram matrix $\mathrm{I}_4$ and realification of signature $(4,4)$; its null set is the null cone, of real dimension $6$, whose punctured part is the zero-divisor set, and its *level set* $N=1$ is the norm-one group $\mathbb{B}^\times_1$. The complex sesquilinear form $\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu}$ is positive definite, with Gram matrix $\mathrm{I}_4$ and signature $(8,0)$; it supplies the Euclidean norm, the ambient topology, the sphere $S^{7}_{E}$, which is not a group, and the unitary group $U(\mathbb{B})\cong U(2)$. The quaternion sesquilinear form $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ is indefinite, with Gram matrix $\mathrm{E}$ and signature $(2,6)$; it carries the fundamental decomposition, the fundamental symmetry $J={}^{\natural}$, a null set of real dimension $7$ distinct from the null cone, and the isometry group $U(1,3)$. The four forms are mutually determined and their four symmetries $\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}$ return the complex sesquilinear form. Each of the four gives a distance and the four distances coincide, so the algebra carries one topology; what the three indefinite forms add is the geometry their signatures single out, read in that topology. Each layer is developed by the articles named in its section.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q})=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the complex bilinear form; Gram $\mathrm{E}$; signature $(4,4)$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})=\sum_\mu P_\mu Q_\mu$ | the quaternion bilinear form; diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$; signature $(4,4)$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ | the complex sesquilinear form; diagonal $\lVert\tilde{Q}\rVert_E^{2}$; signature $(8,0)$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the quaternion sesquilinear form; signature $(2,6)$ |
| $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, $\mathrm{I}_4$ | the two Gram matrices |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\langle\tilde{P}^{\natural},\tilde{Q}\rangle$, $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\langle\tilde{P}^{\natural},\tilde{Q}\rangle_{*}$ | the quaternion forms vs the plain ones |
| $\mathcal{N}=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}$ | the null cone; real dimension $6$; the zero-divisor set |
| $\mathbb{B}^\times_1=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1\}$ | the norm-one group; the quaternion bilinear level set |
| $S^{7}_{E}=\{\lVert\tilde{Q}\rVert_E=1\}$ | the Euclidean unit sphere; not a group |
| $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)$ | the unitary group; the complex sesquilinear level set |
| $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}$ | the null set of the quaternion sesquilinear form; real dimension $7$ |
| $J={}^{\natural}$, $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\langle J\tilde{P},\tilde{Q}\rangle_{*}$ | the fundamental symmetry of the quaternion sesquilinear form |
| $O_4(\mathbb{C}),\ U(4),\ U(1,3)$ | the three isometry groups |

## Further Reading

- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the four products whose scalar parts are the four forms
- *Relations Between the Four Biquaternion Products* (`articles_maths/relations-between-the-four-biquaternion-products.md`), for the identities that link the four products and the four forms
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for three of the forms, their adjoints and their isometry groups
- *Four Forms but One Topology on the Biquaternion Algebra* (`articles_maths/four-forms-but-one-topology-on-the-biquaternion-algebra.md`), for the argument behind the caution of §*What a Pairing Induces*
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`) and *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for three of the forms in full
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the complex bilinear form, its Gram matrix $\mathrm{E}$ and its association law
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, its polarisation and the real forms
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the ambient topology the complex sesquilinear form induces
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the map that turns the quaternion sesquilinear form into the complex sesquilinear one
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the forms in the $2\times2$ realization
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations and their group
