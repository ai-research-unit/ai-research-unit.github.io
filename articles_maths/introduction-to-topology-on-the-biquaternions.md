# __Introduction to Topology on the Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is an eight-dimensional real space that carries a product, and the corpus reads it through three distinguished pairings of its elements. Each pairing is a non-degenerate form, and each form carries a layer of structure: a signature, a zero set, a family of level sets and a group of isometries. The three layers are the sub-categories *Topology Induced by the Bilinear Form*, *Topology Induced by the Hermitian Form* and *Topology Induced by the Krein Form*, and this article is their common entry point.

It introduces no theorem. The three pairings are defined and compared, as forms, in *The Three Pairings of the Biquaternion Algebra*; every result quoted below is proved in the article that owns it, and each section names the articles of its layer. What this article states is the situation the three layers share — one algebra, three forms, three readings that do not coincide — and the sense in which each form induces a topology. It assumes the algebra and its conjugations from *Biquaternion Algebra* and *Biquaternion Involution Lattice*, the pairing map and the three forms from *The Three Pairings of the Biquaternion Algebra*, and the two functions $N$ and $\lVert\cdot\rVert_E$ from *Biquaternion Norm and Invertibility*. No physics is invoked.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, central scalar imaginary $i$, and a general element $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The conjugations are the natural conjugation ${}^{\natural}$, the complex conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; $\mathrm{Sc}$ is the scalar part; the sign vector is $\varepsilon=(1,-1,-1,-1)$ and $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ is its diagonal matrix. The biquaternion norm is $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$ and the Euclidean norm is $\lVert\tilde{Q}\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$.

## The Situation

The algebra has one product and four conjugations, and the conjugations generate the pairings. They form the Klein four-group $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ of *Biquaternion Involution Lattice*, and to each involution $\sigma$ the **pairing map** assigns

$$
\Phi_{\sigma}(\tilde{P},\tilde{Q})=\mathrm{Sc}\bigl(\sigma(\tilde{P})\,\tilde{Q}\bigr).
$$

The identity gives the unsymmetric product form $\mathrm{Sc}(\tilde{P}\tilde{Q})$ and the reversal $\flat=-{}^{*}$ gives the negative of the Hermitian pairing; the three non-identity involutions of the group give the three forms of the corpus,

$$
B(\tilde{P},\tilde{Q})=\sum_{\mu=0}^{3}P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle=\sum_{\mu=0}^{3}\overline{P_\mu}\,Q_\mu,\qquad
[\tilde{P},\tilde{Q}]=\sum_{\mu=0}^{3}\varepsilon_\mu\overline{P_\mu}\,Q_\mu .
$$

They are the **bilinear form** $B$, built on the linear conjugation ${}^{\natural}$; the **Hermitian form** $\langle\cdot,\cdot\rangle$, built on the antilinear conjugation ${}^{*}$; and the **Krein form** $[\cdot,\cdot]$, built on the antilinear conjugation $\bar{\cdot}$. Their diagonals are the three real or complex quadratic functions of the algebra,

$$
B(\tilde{Q},\tilde{Q})=N(\tilde{Q}),\qquad
\langle\tilde{Q},\tilde{Q}\rangle=\lVert\tilde{Q}\rVert_E^{2},\qquad
[\tilde{Q},\tilde{Q}]=\sum_{\mu=0}^{3}\varepsilon_\mu\lvert Q_\mu\rvert^{2},
$$

and the second is positive definite while the first and the third are not. The three are collected in the table with the data each layer is built from.

| form | conjugation | first argument | Gram matrix | signature over $\mathbb{R}$ | diagonal value |
|---|---|---|---|---|---|
| bilinear $B$ | ${}^{\natural}$, linear | linear | $\mathrm{I}_4$ | $(4,4)$ | $N(\tilde{Q})$ |
| Hermitian $\langle\cdot,\cdot\rangle$ | ${}^{*}$, antilinear | conjugate-linear | $\mathrm{I}_4$ | $(8,0)$ | $\lVert\tilde{Q}\rVert_E^{2}$ |
| Krein $[\cdot,\cdot]$ | $\bar{\cdot}$, antilinear | conjugate-linear | $\mathrm{E}$ | $(2,6)$ | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ |

The Gram matrices are $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$, and the signatures over the eight real coordinates are $(4,4)$, $(8,0)$ and $(2,6)$. The three forms are mutually non-degenerate and pairwise distinct, and they nevertheless determine one another by the identities

$$
[\tilde{P},\tilde{Q}]=\langle\tilde{P}^{\natural},\tilde{Q}\rangle,\qquad
B(\bar{\tilde{P}},\tilde{Q})=\langle\tilde{P},\tilde{Q}\rangle,\qquad
[\tilde{P},\tilde{Q}]=B\bigl(\overline{\tilde{P}^{\natural}},\tilde{Q}\bigr),
$$

so the three readings are three coefficient expressions of one pairing map and not three independent structures. The natural conjugation ${}^{\natural}$ preserves all three, and it is the map that ties the layers together: it is an isometry of each form and, in the Krein layer, the fundamental symmetry (*The Fundamental Symmetry of the Biquaternion Algebra*).

## What a Pairing Induces

A non-degenerate pairing determines four objects, and they are the objects each layer of this region is built from.

- the **real form on the diagonal**, $\tilde{Q}\mapsto\Phi(\tilde{Q},\tilde{Q})$, together with its signature, which decides whether the pairing is definite or indefinite;
- the **null set** $\{\tilde{Q}:\Phi(\tilde{Q},\tilde{Q})=0\}$ and the **level sets** $\{\tilde{Q}:\Phi(\tilde{Q},\tilde{Q})=c\}$;
- the **isometry group**, of the linear maps preserving the pairing; and
- the **subgroups cut out by the diagonal**, wherever the level set of a multiplicative form is a group.

Each layer reads these four objects from its own form, and the objects do not agree. The disagreement is the content of the region, and it begins with the meaning of the word *topology*.

**Remark (every non-degenerate pairing yields a distance, and the three distances coincide).** A real-valued form gives a norm through its diagonal only when the diagonal is positive definite, and among the three only the Hermitian form is. But no non-degenerate form is without a distance: a **symmetry** of the form $\Phi$ — an involution $J$ with $\Phi(J\tilde{P},J\tilde{Q})=\Phi(\tilde{P},\tilde{Q})$ and $\Phi(J\tilde{Q},\tilde{Q})>0$ off zero — makes $\mathrm{Re}\,\Phi(J\tilde{P},\tilde{Q})$ an inner product, and every non-degenerate form has one, by Sylvester. For the three pairings the symmetries are the complex conjugation and the natural conjugation, which give the identities of §*The Situation*: all three forms produce the **same** distance, the Euclidean one, and the Hermitian form is merely the one that needs no symmetry. The three sub-categories are named for the structure each form induces beyond that common distance — its signature, its null set, its level sets, its isometry group — and not for three inequivalent topologies on one set. The full argument is *The Three Topologies of the Biquaternion Algebra*; the bilinear norm $N$ decides the units and the Hermitian form the topology (*The Biquaternion Unit Group as a Topological Group*, §*The Topology of the Group*).

## The Bilinear Layer

The bilinear form is the polarisation of the biquaternion norm, $B(\tilde{P},\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$. It is $\mathbb{C}$-bilinear, symmetric and non-degenerate, and it is the only one of the three that takes complex values; its realification is the split form of signature $(4,4)$. Its restriction to the six distinguished real subspaces carries the signatures $(1,1)$ on the centre, $(3,3)$ on the vector subspace, $(4,0)$ on the quaternion subspace, $(0,4)$ on the anti-quaternion subspace, and $(1,3)$ and $(3,1)$ on the Hermitian and anti-Hermitian subspaces.

Its diagonal $N$ is complex-valued and multiplicative, so it is not itself a norm; the distance of this layer comes from the symmetry $c=\bar{\cdot}$, which returns the Hermitian form, $B(\bar{\tilde{P}},\tilde{Q})=\langle\tilde{P},\tilde{Q}\rangle$ (§*What a Pairing Induces*). It decides invertibility — an element is a unit exactly when $N(\tilde{Q})\neq0$ — and its vanishing defines the **null cone**

$$
\mathcal{N}=\{N(\tilde{Q})=0\}=\{0\}\cup\mathcal{Z},
$$

where $\mathcal{Z}$ is the zero-divisor set. The cone is a complex hypersurface in $\mathbb{B}\cong\mathbb{C}^{4}$, of real dimension $6$, and the origin is its only singular point; away from the apex it is a smooth complex $3$-manifold, and it is the set on which the algebra fails to be a division algebra. Its complement is the group of units $\mathbb{B}^\times=\{N\neq0\}$, open and dense. The level set $N(\tilde{Q})=1$ is the **norm-one group** $\mathbb{B}^\times_1$, a closed non-compact subgroup of real dimension $6$: in this layer the *unit sphere* is a group, and it is not bounded.

Three further structures belong to the layer. The **Clifford algebra** of the quadratic form $N$, with its spinors and its Fierz–Kofink identities. The **projective geometry** of the null cone: its link, the quadric $Q^{2}$ and the Klein–Plücker geometry of the lines of $\mathbb{P}^{3}$. And the **isometry group** $O_4(\mathbb{C})$, of real dimension $12$. The layer is developed in *Biquaternion Norm and Invertibility*, *The Clifford Structure of the Biquaternion Algebra*, *Biquaternion Topology*, *The Biquaternion Unit Group as a Topological Group* and *Biquaternion Orders and Finite Groups of Units*; the sub-category also gathers the coordinate realizations of the element — *Biquaternion Four-Vector Element Representation*, *Biquaternion Polar Element Representation* and *Biquaternion Partial Polar Element Representations* — whose content is algebraic and is not read here.

## The Hermitian Layer

The Hermitian form is the one definite pairing, and it is the canonical source of the ambient topology: it is the one form that is already an inner product, so its distance needs no symmetry to be read (§*What a Pairing Induces*). Its scalar part is $\sum_\mu\lvert Q_\mu\rvert^{2}$, positive definite, and its real part

$$
(\tilde{P},\tilde{Q})_{\mathbb{R}}=\mathrm{Re}\langle\tilde{P},\tilde{Q}\rangle=\sum_{\mu=0}^{3}\bigl(p_\mu q_\mu+p'_\mu q'_\mu\bigr)
$$

is a Euclidean inner product on $\mathbb{B}\cong\mathbb{R}^{8}$. The associated **Euclidean norm** $\lVert\cdot\rVert_E$ gives the metric, the balls, the completeness and the **Euclidean topology** in which every topological statement of the corpus is made; the coefficient map is a linear isometry onto $\mathbb{R}^{8}$.

Two level sets of this layer are distinguished. The **Euclidean unit sphere** $S^{7}_{E}=\{\lVert\tilde{Q}\rVert_E=1\}$ is a genuine $S^{7}$, compact and connected, but it is not a group: $\lVert\cdot\rVert_E$ is not multiplicative, and $S^{7}_{E}$ contains zero divisors, its intersection with the null cone being the link of that cone. The other is the **unitary group**

$$
U(\mathbb{B})=\{\tilde{Q}:\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)\cong S^{1}\times S^{3},
$$

a compact Lie group, and it is the maximal compact subgroup onto which the group of units deformation retracts. Unlike the sphere $S^{7}_{E}$, it lies inside the units.

The layer owns the Euclidean structure and the contractibility of the algebra and of the six distinguished subspaces; the unitary group and the polar decomposition; the retraction of the group of units and its homotopy, with $\pi_1\cong\mathbb{Z}$, $\pi_2=0$, $\pi_3\cong\mathbb{Z}$ and universal cover $\mathbb{R}\times S^{3}$; and the Hermitian modules, the positivity cone and the unitary Witt group. Its articles are *The Hermitian Form on the Biquaternion Algebra*, *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*, *The Euclidean Topology of the Biquaternion Algebra*, *The Unitary Group of the Biquaternion Algebra*, *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* and their companions.

## The Krein Layer

The Krein form is Hermitian and indefinite, of signature $(2,6)$ over $\mathbb{R}$ and $(1,3)$ over $\mathbb{C}$. Its positive part is the centre $\mathbb{C}_{\mathbb{B}}$ and its negative part the vector subspace $\mathbb{V}_{\mathbb{B}}$; the two are orthogonal in the form and complementary,

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}},
$$

the **fundamental decomposition**. The natural conjugation ${}^{\natural}$ is a self-adjoint involution of the form, and it plays the role of the **fundamental symmetry** $J$: it turns the Krein form into the positive definite Hermitian one by the bridge identity $[\tilde{P},\tilde{Q}]=\langle\tilde{P}^{\natural},\tilde{Q}\rangle$. The algebra is thereby a Krein space of complex dimension four and negative index three, a Pontryagin space $\Pi_6$ over $\mathbb{R}$.

The **null set** $\{[\tilde{Q},\tilde{Q}]=0\}$ is a real cone of real dimension $7$, and it is a different object from the null cone: it contains $\tilde{Q}=e_0+e_1$, which is no zero divisor, and it omits $\tilde{Q}=e_1+ie_2$, which is one; the two cones cross on elements such as $\tilde{Q}=e_0+ie_1$. The level set $[\tilde{Q},\tilde{Q}]=1$ is a hyperboloid, and the maximal totally isotropic subspace has real dimension $2$, so the Witt index is $2$ over $\mathbb{R}$ and $1$ over $\mathbb{C}$.

The layer owns the signature and the fundamental decomposition; the isotropic and totally isotropic subspaces; the level sets and the hyperbolic structure; and the operators the form defines — the $J$-self-adjoint, the $J$-unitary and the $J$-normal operators and the indefinite spectral theorem. Its articles are *The Biquaternion Krein Form and Its Signature*, *The Fundamental Symmetry of the Biquaternion Algebra*, *The Three Pairings of the Biquaternion Algebra*, *The Krein Gram Matrix and the Restrictions of the Form*, *Krein Orthogonality and the Fundamental Decomposition*, *The Isotropic Structure of the Krein Form* and *The Krein Level Sets and the Hyperbolic Structure*, with their operator companions.

## The Three Topologies Compared

The three layers are collected in one table. Each row is a pairing; the entries are the objects of §*What a Pairing Induces*, read from that pairing; the signatures are those of the underlying real form.

| topology | form | Gram matrix | signature over $\mathbb{R}$ | definiteness | null set | level set $\Phi=1$ | isometry group |
|---|---|---|---|---|---|---|---|
| bilinear | $B(\tilde{P},\tilde{Q})=\sum_\mu P_\mu Q_\mu$ | $\mathrm{I}_4$ | $(4,4)$ | indefinite | the null cone $\mathcal{N}$, real dimension $6$ | the group $\mathbb{B}^\times_1$ | $O_4(\mathbb{C})$ |
| Hermitian | $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\overline{P_\mu}Q_\mu$ | $\mathrm{I}_4$ | $(8,0)$ | positive definite | $\{0\}$ | the sphere $S^{7}_{E}$, not a group | $U(4)$ |
| Krein | $[\tilde{P},\tilde{Q}]=\sum_\mu\varepsilon_\mu\overline{P_\mu}Q_\mu$ | $\mathrm{E}$ | $(2,6)$ | indefinite | the Krein null set, real dimension $7$ | a hyperboloid | $U(1,3)$ |

**Remark (the three are pairwise distinct and mutually determined).** No two of the three forms agree: the bilinear form is not sesquilinear and is complex-valued, the Hermitian form is definite and the Krein form is not, and the Gram matrices $\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$ are not all equal. They are nevertheless one family, related by the identities of §*The Situation*, and they carry the same natural conjugation as a common isometry. **The layers are three readings of one algebra, and none is a deformation of another.**

**Remark (the three rows give one distance, three unit spheres).** Each row yields a distance, and the three distances coincide, so the table carries one metric and not three; what differs from row to row is the *unit sphere* the diagonal singles out. The Hermitian row has a positive definite diagonal and its sphere is the genuine $S^{7}_{E}$; the other two rows have indefinite diagonals whose *unit spheres* are the group $\mathbb{B}^\times_1$ and a hyperboloid rather than a sphere. This is the table form of the caution of §*What a Pairing Induces*.

## The Matrix Picture

The $2\times2$ realization $\Phi$ of *Biquaternion 2×2 Matrix Element Representation* carries the three pairings to three pairings of matrices, with the trace in place of the scalar part and adjugation and the conjugate transpose marking the two non-bilinear cases:

$$
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr),\qquad
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

and they reproduce the bilinear, the Hermitian and the Krein form respectively. The realization converts the Euclidean norm into the Frobenius norm, $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$, and converts the level set of the bilinear layer into the determinant locus: $\mathbb{B}^\times\cong GL_2(\mathbb{C})$ and $\mathbb{B}^\times_1=\{N=1\}\cong SL_2(\mathbb{C})$. The three readings of the six distinguished subspaces are *The Centre Subspace under the Three Topologies* and its five companions, and the three readings of the two realizations are *The 2×2 Matrix Representation under the Three Topologies* and *The 4×4 Regular Matrix Representation under the Three Topologies*; the matrix form of the three forms themselves is *The Forms in the Matrix Representation of the Biquaternion Algebra*.

## Summary

The biquaternion algebra is one algebra with three distinguished pairings, generated by the three non-identity involutions of the Klein four-group $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ through the pairing map $\Phi_{\sigma}$. The bilinear form $B=\sum_\mu P_\mu Q_\mu$ is $\mathbb{C}$-bilinear, with Gram matrix $\mathrm{I}_4$ and realification of signature $(4,4)$; its diagonal is the multiplicative complex norm $N$, its null set is the null cone, of real dimension $6$, whose punctured part is the zero-divisor set, and its *unit sphere* is the norm-one group. The Hermitian form $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\overline{P_\mu}Q_\mu$ is positive definite, with Gram matrix $\mathrm{I}_4$ and signature $(8,0)$; it supplies the Euclidean norm, the ambient topology, the sphere $S^{7}_{E}$, which is not a group, and the unitary group $U(\mathbb{B})\cong U(2)$. The Krein form $[\tilde{P},\tilde{Q}]=\sum_\mu\varepsilon_\mu\overline{P_\mu}Q_\mu$ is indefinite, with Gram matrix $\mathrm{E}$ and signature $(2,6)$; it carries the fundamental decomposition, the fundamental symmetry $J={}^{\natural}$, a null set of real dimension $7$ distinct from the null cone, and the isometry group $U(1,3)$. The three forms determine one another and $J$ is a common isometry. Each of the three gives a distance and the three distances coincide, so the algebra carries one topology; what the bilinear and the Krein layers add is the geometry their signatures single out, read in that topology. Each layer is developed by the articles named in its section.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi_{\sigma}(\tilde{P},\tilde{Q})=\mathrm{Sc}(\sigma(\tilde{P})\tilde{Q})$ | the pairing map of the involution $\sigma$ |
| $B(\tilde{P},\tilde{Q})=\sum_\mu P_\mu Q_\mu$ | the bilinear form; diagonal $N$; signature $(4,4)$ |
| $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\overline{P_\mu}Q_\mu$ | the Hermitian form; diagonal $\lVert\tilde{Q}\rVert_E^{2}$; signature $(8,0)$ |
| $[\tilde{P},\tilde{Q}]=\sum_\mu\varepsilon_\mu\overline{P_\mu}Q_\mu$ | the Krein form; signature $(2,6)$ |
| $\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ | the three Gram matrices |
| $\mathcal{N}=\{N=0\}$ | the null cone; real dimension $6$; the zero-divisor set |
| $\mathbb{B}^\times_1=\{N=1\}$ | the norm-one group; the bilinear unit sphere |
| $S^{7}_{E}=\{\lVert\tilde{Q}\rVert_E=1\}$ | the Euclidean unit sphere; not a group |
| $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)$ | the unitary group; the Hermitian unit sphere |
| $\{[\tilde{Q},\tilde{Q}]=0\}$ | the Krein null set; real dimension $7$ |
| $J={}^{\natural}$, $[\tilde{P},\tilde{Q}]=\langle J\tilde{P},\tilde{Q}\rangle$ | the fundamental symmetry of the Krein form |
| $O_4(\mathbb{C}),\ U(4),\ U(1,3)$ | the three isometry groups |

## Further Reading

- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms, their adjoints and their isometry groups
- *The Three Topologies of the Biquaternion Algebra* (`articles_maths/the-three-topologies-of-the-biquaternion-algebra.md`), for the argument behind the caution of §*What a Pairing Induces*
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`) and *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the three forms in full
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, its polarisation and the real forms
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the ambient topology the Hermitian form induces
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the map that turns the Krein form into the Hermitian one
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the three forms in the $2\times2$ realization
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four conjugations and their group
