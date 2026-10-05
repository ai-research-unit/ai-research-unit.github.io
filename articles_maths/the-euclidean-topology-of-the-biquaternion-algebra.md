# __The Euclidean Topology of the Biquaternion Algebra__

## Introduction

The complex sesquilinear form of the biquaternion algebra $\mathbb{B}$ — the sesquilinear inner product $\langle\tilde{Q},\tilde{P}\rangle_{*}=\sum_\mu P_{\bar\mu}Q_\mu$ built on the antilinear conjugation ${}^{*}$ — makes $\mathbb{B}$ into a complex Hilbert space whose real part is a Euclidean inner product, and the topology it defines is the topology in which every topological statement of the corpus is made. This article reads the topology of $\mathbb{B}$ **from the complex sesquilinear form**: the Euclidean norm, the linear isometry onto $\mathbb{R}^{8}$, the Hilbert-space structure and the Riemannian metric; the normed-algebra inequality with its sharp constant; the contractibility of the algebra and of its six distinguished subspaces; and the Euclidean unit sphere $S^{7}_{E}$, which — unlike the level sets of the biquaternion norm — is a genuine sphere but is not a group and contains zero divisors.

The readings collected here are the Hermitian half of the former joint treatment of the ambient topology. The bilinear half — the null cone, its link and the projective geometry of the norm — is *Biquaternion Topology*, which quotes this article for the Euclidean structure and the contractibility. The two forms are compared in *The Hermitian Form on the Biquaternion Algebra* and *The Bilinear Form on the Biquaternion Algebra*; the matrix reading of the Euclidean norm is *The Unit Group and the Frobenius Norm in the Matrix Representation*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with units $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, central scalar imaginary $i$, and a general element $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The Hermitian conjugation is ${}^{*}={}^{\natural}\circ\bar{\cdot}$, the inner product is $\langle\tilde{Q},\tilde{P}\rangle_{*}=\sum_\mu P_{\bar\mu}Q_\mu$, the Euclidean norm is $\|\tilde{Q}\|_E=\bigl(\sum_\mu|Q_\mu|^{2}\bigr)^{1/2}=\bigl(\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})\bigr)^{1/2}$, and the biquaternion norm is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^{2}$.

## The Euclidean Norm and the Isometry onto $\mathbb{R}^{8}$

The real part of the inner product is a genuine inner product. Write $\tilde{Q}=\sum_\mu(q_\mu+iq'_\mu)e_\mu$ and introduce the real inner product

$$
(\tilde{P},\tilde{Q})_{\mathbb{R}}=\mathrm{Re}\,\langle\tilde{Q},\tilde{P}\rangle_{*}=\sum_{\mu=0}^{3}\bigl(p_\mu q_\mu+p'_\mu q'_\mu\bigr).
$$

**Proposition.** $(\cdot,\cdot)_{\mathbb{R}}$ is a positive definite real inner product on $\mathbb{B}$, of the form $\mathrm{Re}\langle\tilde{Q},\tilde{P}\rangle_{*}$, and its associated norm is $\|\tilde{Q}\|_E$.

**Proof.** Bilinearity over $\mathbb{R}$ is immediate from the definition; symmetry follows from $\langle\tilde{Q},\tilde{P}\rangle_{*}^{*}=\langle\tilde{P},\tilde{Q}\rangle_{*}$; and $(\tilde{Q},\tilde{Q})_{\mathbb{R}}=\sum_\mu(q_\mu^{2}+q'_\mu{}^{2})$ is positive off zero, since a vanishing sum of squares forces $q_\mu=q'_\mu=0$. The associated norm is the square root of $(\tilde{Q},\tilde{Q})_{\mathbb{R}}=\sum_\mu|Q_\mu|^{2}=\|\tilde{Q}\|_E^{2}$.

**Theorem (the isometry).** The coefficient map

$$
\iota:\mathbb{B}\longrightarrow\mathbb{R}^{8},\qquad \tilde{Q}=\sum_\mu(q_\mu+iq'_\mu)e_\mu\longmapsto(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3),
$$

is a linear isometry of $(\mathbb{B},(\cdot,\cdot)_{\mathbb{R}})$ onto $\mathbb{R}^{8}$ with the standard inner product. Equivalently, $\mathbb{B}\cong\mathbb{C}^{4}$ as a complex Hilbert space with orthonormal basis $e_0,e_1,e_2,e_3$.

**Proof.** The map is bijective and $\mathbb{R}$-linear because $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ is a real basis; it preserves the inner product by the displayed formula. The complex structure is the central multiplication by $i$, which acts as $i$ on each coefficient, so the $\mathbb{C}$-span of the same four vectors is $\mathbb{B}$ and the complex inner product is $\langle\cdot,\cdot\rangle_{*}$.

Two consequences are used throughout. First, $\mathbb{B}$ is **complete** in $\|\cdot\|_E$: it is finite-dimensional, and a finite-dimensional inner product space is a Hilbert space. Second, $\|\cdot\|_E$ defines the unique Hausdorff vector-space topology on $\mathbb{B}$, the **Euclidean topology**, and this is the topology of the corpus. The metric is $d(\tilde{P},\tilde{Q})=\|\tilde{P}-\tilde{Q}\|_E$.

**Remark (distinct from the quaternion bilinear norm).** The corpus carries a second quadratic function, the biquaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, complex-valued and indefinite; it is not a norm and defines no topology. The two agree on the quaternion subspace and differ by a sign on the anti-quaternion subspace (*Biquaternion Norm and Invertibility*, §*The Euclidean Norm and the Hermitian Form*). Everything topological uses $\|\cdot\|_E$, never $N$.

## The Algebra as a Normed Algebra

The multiplication is continuous, and the estimate is sharp.

**Theorem (the normed-algebra inequality).** For all $\tilde{Q},\tilde{R}\in\mathbb{B}$,

$$
\|\tilde{Q}\tilde{R}\|_E\leq\sqrt{2}\,\|\tilde{Q}\|_E\|\tilde{R}\|_E,
$$

and the constant $\sqrt{2}$ cannot be lowered.

**Proof.** Under the algebra isomorphism $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation*, which is a linear isometry up to the factor $\sqrt2$, one has $\|\Phi(\tilde{T})\|_F=\sqrt2\|\tilde{T}\|_E$, where $\|\cdot\|_F$ is the Frobenius norm (*The Forms in the Matrix Representation of the Biquaternion Algebra*, §*The Inner Product as the Hilbert–Schmidt Pairing*). The Frobenius norm is submultiplicative, so
$$
\sqrt2\,\|\tilde{Q}\tilde{R}\|_E=\|\Phi(\tilde{Q})\Phi(\tilde{R})\|_F\leq\|\Phi(\tilde{Q})\|_F\|\Phi(\tilde{R})\|_F=2\|\tilde{Q}\|_E\|\tilde{R}\|_E,
$$
which is the inequality. For sharpness take $\tilde{Q}=\tilde{R}=e_0+ie_1$: then $\tilde{Q}^{2}=2e_0+2ie_1$ and $\|\tilde{Q}\|_E^{2}=2$, $\|\tilde{Q}^{2}\|_E=2\sqrt2$, so $\|\tilde{Q}^{2}\|_E=\sqrt2\,\|\tilde{Q}\|_E^{2}$.

**Corollary.** Multiplication $\mathbb{B}\times\mathbb{B}\to\mathbb{B}$ is continuous, inversion is continuous on the units, and $\mathbb{B}$ is a topological algebra over $\mathbb{R}$ with $\mathbb{B}^{\times}$ a topological group.

**Proof.** The inequality bounds the product in terms of the factors; inversion is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^{-1}\tilde{Q}^{\natural}$-based and $N^{-1}$ is continuous off the closed null cone, so the standard arguments apply; the group axioms with continuous operations give a topological group.

**Proposition (the isometries that the algebra supplies).** Multiplication by a central element and the conjugations are orthogonal:

$$
\|(A e_0)\tilde{Q}\|_E=|A|\,\|\tilde{Q}\|_E,\qquad
\|\tilde{Q}^{\natural}\|_E=\|\bar{\tilde{Q}}\|_E=\|\tilde{Q}^{*}\|_E=\|\tilde{Q}\|_E .
$$

Moreover, for every unitary biquaternion $\tilde{U}$ the inner conjugation $\Theta_{\tilde{U}}(\tilde{T})=\tilde{U}\tilde{T}\tilde{U}^{*}$ is a Euclidean isometry.

**Proof.** A central multiplier scales every coefficient by $A$, and the three conjugations $\natural$, $\bar{\cdot}$, ${}^{*}$ (together with the reversal $\flat=-{}^{*}$) permute the coefficients among $\pm Q_\mu$ and $\pm\bar Q_\mu$, preserving $\sum_\mu|Q_\mu|^{2}$. For the last statement, $\Phi$ carries $\Theta_{\tilde{U}}$ to $M\mapsto M_{\tilde{U}}XM_{\tilde{U}}^{\dagger}$ with $M_{\tilde{U}}$ unitary, and the Frobenius norm is invariant under unitary similarity.

## The Contractibility of the Algebra

**Theorem.** $\mathbb{B}$ is contractible; hence it is path-connected and simply connected, with $\pi_n(\mathbb{B})=0$ for every $n\geq1$.

**Proof.** The straight-line homotopy $H(t,\tilde{Q})=(1-t)\tilde{Q}$, $t\in[0,1]$, is jointly continuous with $H(0,\cdot)=\mathrm{id}$ and $H(1,\cdot)\equiv0$, so the identity is homotopic to a constant map.

**Corollary (the fixed subspaces).** The centre, the vector subspace, the Hermitian subspace, the anti-Hermitian subspace, the quaternion subspace and the anti-quaternion subspace are each contractible, the homotopy above preserving every linear subspace, so each is a point as far as homotopy is concerned:

$$
\mathbb{C}_{\mathbb{B}}\cong\mathbb{R}^{2},\qquad
\mathbb{V}_{\mathbb{B}}\cong\mathbb{R}^{6},\qquad
\mathbb{H}_{\mathbb{B}}\cong i\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^{4},\qquad
\mathbb{M}_{+}\cong\mathbb{M}_{-}\cong\mathbb{R}^{4}.
$$

**Proof.** Each is a linear subspace of $\mathbb{B}$, and the homotopy above preserves it. The dimensions are those of *Comparison of the Six Subspaces*.

**Corollary.** Every map into $\mathbb{B}$ is null-homotopic, and $\mathbb{B}$ carries no topological obstruction of its own; the topology of the algebra is entirely the topology of its distinguished subsets — the unit group, the null cone and the spheres.

**Proof.** Immediate from the theorem.

The complement of the null cone is dense in $\mathbb{B}$, because the null cone is a proper algebraic subset of real codimension two — a complex hypersurface of $\mathbb{B}\cong\mathbb{C}^{4}$ — with empty interior (*Biquaternion Topology*, §*The null cone*); this is what makes the group of units, an open dense subset, carry the topology it does.

## The Euclidean Unit Sphere

$$
S^{7}_{E}=\{\tilde{Q}\in\mathbb{B}:\|\tilde{Q}\|_E=1\}\cong S^{7}
$$

is, by the isometry of §*The Euclidean Norm and the Isometry onto $\mathbb{R}^{8}$*, the standard unit sphere of $\mathbb{R}^{8}$: closed, compact, connected, and a smooth $7$-manifold. It is nevertheless the **wrong** sphere for the algebra, and the reason is that $\|\cdot\|_E$ is not multiplicative: for $\tilde{Q}=e_1+ie_2$ one has $\tilde{Q}^{2}=0$ while $\|\tilde{Q}\|_E=\sqrt2$, so

$$
\tilde{Q}_0=\frac{e_1+ie_2}{\sqrt2}\in S^{7}_{E},\qquad \langle\tilde{Q}_0,\tilde{Q}_0\rangle_{\natural}=0,
$$

and $\tilde{Q}_0$ is a zero divisor. Hence $S^{7}_{E}\not\subseteq\mathbb{B}^{\times}$ and $S^{7}_{E}$ is not a subgroup of $\mathbb{B}^{\times}$.

**Proposition (the sphere meets the null cone in a compact $5$-manifold).** The intersection $S^{7}_{E}\cap\mathcal{N}$, with $\mathcal{N}=\{N=0\}$, is a compact real $5$-manifold without boundary, homeomorphic to the link of the null cone.

**Proof.** The null cone is a real algebraic cone of real dimension $6$ with its only singular point at the origin (*Biquaternion Topology*, §*The null cone*); intersecting the smooth part with the transverse unit sphere and removing the origin gives a compact smooth manifold of dimension $6-1=5$, and it is the link by definition (*Biquaternion Topology*, §*The link of the null cone*).

**Remark (the three spherical level sets).** The algebra carries three level sets that look like unit spheres, and they are genuinely different objects; only the group-theoretic ones are developed in *The Unitary Group of the Biquaternion Algebra*.

| Level set | Geometry | Algebra |
|---|---|---|
| $\|\tilde{Q}\|_E=1$ | $S^{7}$, compact $7$-manifold | no group structure; contains zero divisors |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1$ | non-compact real $6$-manifold, homotopy equivalent to $S^{3}$ | closed subgroup $\mathbb{B}^{\times}_1$ |
| $\tilde{Q}^{*}\tilde{Q}=e_0$ | $\cong S^{1}\times S^{3}$ | closed subgroup $U(\mathbb{B})\cong U(2)$ |

The middle row is *The Biquaternion Unit Group as a Topological Group*; the bottom row is *The Unitary Group of the Biquaternion Algebra*, where the retraction of the group of units onto it is proved.

## The Hilbert Space and the Duality

The inner product $\langle\cdot,\cdot\rangle_{*}$ makes $\mathbb{B}$ a Hilbert space of complex dimension four, and the real inner product $(\cdot,\cdot)_{\mathbb{R}}$ a Euclidean space of dimension eight. Two structures follow and are recorded here because later articles use them.

**The Riesz duality.** Every $\mathbb{C}$-linear functional on $\mathbb{B}$ is $\tilde{Q}\mapsto\langle\tilde{Q},\tilde{P}\rangle_{*}$ for a unique $\tilde{P}$; every $\mathbb{R}$-linear functional is $(\tilde{P},\cdot)_{\mathbb{R}}$ for a unique $\tilde{P}$. This is the finite-dimensional Riesz representation theorem, and it is what makes the adjoint operations of the operator articles well defined.

**The Riemannian metric.** $(\cdot,\cdot)_{\mathbb{R}}$ is the flat Riemannian metric of $\mathbb{B}\cong\mathbb{R}^{8}$; the orthogonal group $O(8)$ is its isometry group, and the $\mathbb{C}$-linear isometries that preserve the algebra structure are exactly the inner automorphisms by the unitary biquaternions, of group $PU(2)\cong SO(3)$ (*Biquaternion Automorphisms and Derivations*). Over $\mathbb{R}$ the coefficient conjugation adds one more coset, since it is an $\mathbb{R}$-algebra automorphism of unit Euclidean norm, so the real-linear automorphisms that are Euclidean isometries form $PU(2)\rtimes\mathbb{Z}/2$.

## Summary

The complex sesquilinear form equips $\mathbb{B}$ with the real inner product $(\tilde{P},\tilde{Q})_{\mathbb{R}}=\mathrm{Re}\sum_\mu P_{\bar\mu}Q_\mu$ and the Euclidean norm $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^{2})^{1/2}$, and the coefficient map is a linear isometry $\mathbb{B}\cong\mathbb{R}^{8}$, equivalently $\mathbb{B}\cong\mathbb{C}^{4}$ as a complex Hilbert space. Multiplication satisfies the sharp inequality $\|\tilde{Q}\tilde{R}\|_E\leq\sqrt2\|\tilde{Q}\|_E\|\tilde{R}\|_E$, and central multipliers, the conjugations and inner conjugations by unitary elements are Euclidean isometries. The algebra is contractible, as is each of its six distinguished subspaces, so every map into $\mathbb{B}$ is null-homotopic. The Euclidean unit sphere $S^{7}_{E}$ is a genuine $S^{7}$ but is not a group and contains zero divisors; its intersection with the null cone is a compact $5$-manifold, the link. The three spherical level sets — Euclidean, norm-one and unitary — are distinct, and only the last two are groups.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde{P},\tilde{Q})_{\mathbb{R}}=\mathrm{Re}\,\langle\tilde{Q},\tilde{P}\rangle_{*}$ | Real inner product; positive definite |
| $\|\tilde{Q}\|_E=(\sum_\mu\lvert Q_\mu\rvert^{2})^{1/2}$ | Euclidean norm |
| $\iota:\mathbb{B}\to\mathbb{R}^{8}$ | Linear isometry onto $\mathbb{R}^{8}$ |
| $\|\tilde{Q}\tilde{R}\|_E\leq\sqrt2\|\tilde{Q}\|_E\|\tilde{R}\|_E$ | Normed-algebra inequality, sharp |
| $H(t,\tilde{Q})=(1-t)\tilde{Q}$ | Contraction of $\mathbb{B}$ to $0$ |
| $S^{7}_{E}=\{\|\tilde{Q}\|_E=1\}$ | Euclidean unit sphere; not a group |
| $S^{7}_{E}\cap\mathcal{N}$ | Compact $5$-manifold; the link of the null cone |
| $O(8)$ | Isometry group of the Euclidean structure |

## Further Reading

- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the form whose topology this article reads
- *Biquaternion Topology* (`articles_maths/biquaternion-topology.md`), for the null cone and its projective geometry, and the link used here
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the group of the unitary level set
- *The Unit Group and the Frobenius Norm in the Matrix Representation* (`articles_maths/the-unit-group-and-the-frobenius-norm-in-the-matrix-representation.md`), for the matrix reading of $\|\cdot\|_E$
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the comparison of $\|\cdot\|_E$ with $N$
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the finite-dimensional Hilbert-space facts used here
