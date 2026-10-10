# __The Euclidean Topology of the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}$ is a real vector space of dimension eight, and its topology is the one its linear structure forces; every topological statement of the corpus is made in that topology. This article develops the Euclidean structure of that space: the linear isometry onto $\mathbb{R}^{8}$ and the flat Riemannian metric; the norm, which is the one that defines the topology; the normed-algebra inequality with its sharp constant; the contractibility of the algebra and of its remarkable subspaces; and the Euclidean unit sphere $S^{7}_{E}$, which is a genuine sphere but is not a group and contains zero divisors.

The topology itself — the definitions, the equivalence of norms and the uniqueness of the topology in finite dimension — is built in *Topology in the Space of Biquaternions*. The group of units as a topological group is *The Biquaternion Unit Group as a Topological Group*; the zero divisors, the singular cone and its projective geometry are *The Null Quadric and Its Projective Geometry*; and the matrix reading of the Euclidean norm is *The Matrix Element Representation and the Biquaternion Dynamics*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with units $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, central scalar imaginary $i$, and a general element $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The Euclidean norm is the coordinate norm $\|\tilde{Q}\|_E=\bigl(\sum_\mu|Q_\mu|^{2}\bigr)^{1/2}$.

## The Euclidean Norm and the Isometry onto $\mathbb{R}^{8}$

The Euclidean structure is read from the coefficients. Write $\tilde{Q}=\sum_\mu(q_\mu+iq'_\mu)e_\mu$ and introduce the real inner product

$$
(\tilde{P},\tilde{Q})_{\mathbb{R}}=\sum_{\mu=0}^{3}\bigl(p_\mu q_\mu+p'_\mu q'_\mu\bigr).
$$

**Proposition.** $(\cdot,\cdot)_{\mathbb{R}}$ is a positive definite real inner product on $\mathbb{B}$, and its associated norm is $\|\tilde{Q}\|_E$.

**Proof.** Linearity in each argument and symmetry over $\mathbb{R}$ are immediate from the definition; and $(\tilde{Q},\tilde{Q})_{\mathbb{R}}=\sum_\mu(q_\mu^{2}+q'_\mu{}^{2})$ is positive off zero, since a vanishing sum of squares forces $q_\mu=q'_\mu=0$. The associated norm is the square root of $(\tilde{Q},\tilde{Q})_{\mathbb{R}}=\sum_\mu|Q_\mu|^{2}=\|\tilde{Q}\|_E^{2}$.

**Theorem (the isometry).** The coefficient map

$$
\iota:\mathbb{B}\longrightarrow\mathbb{R}^{8},\qquad \tilde{Q}=\sum_\mu(q_\mu+iq'_\mu)e_\mu\longmapsto(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3),
$$

is a linear isometry of $(\mathbb{B},(\cdot,\cdot)_{\mathbb{R}})$ onto $\mathbb{R}^{8}$ with the standard inner product.

**Proof.** The map is bijective and $\mathbb{R}$-linear because $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ is a real basis, and it preserves the inner product by the displayed formula.

Two consequences are used throughout. First, $\mathbb{B}$ is **complete** in $\|\cdot\|_E$: it is finite-dimensional, and a finite-dimensional inner product space is a Hilbert space. Second, $\|\cdot\|_E$ defines the unique Hausdorff vector-space topology on $\mathbb{B}$, the **Euclidean topology**, and this is the topology of the corpus. The metric is $d(\tilde{P},\tilde{Q})=\|\tilde{P}-\tilde{Q}\|_E$.

## The Algebra as a Normed Algebra

The multiplication is continuous, and the estimate is sharp.

**Theorem (the normed-algebra inequality).** For all $\tilde{Q},\tilde{R}\in\mathbb{B}$,

$$
\|\tilde{Q}\tilde{R}\|_E\leq\sqrt{2}\,\|\tilde{Q}\|_E\|\tilde{R}\|_E,
$$

and the constant $\sqrt{2}$ cannot be lowered.

**Proof.** Under the algebra isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, which is a linear isometry up to the factor $\sqrt2$, one has $\|\mathsf{M}_2(\tilde{T})\|_F=\sqrt2\|\tilde{T}\|_E$, where $\|\cdot\|_F$ is the Frobenius norm. The Frobenius norm is submultiplicative, so
$$
\sqrt2\,\|\tilde{Q}\tilde{R}\|_E=\|\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{R})\|_F\leq\|\mathsf{M}_2(\tilde{Q})\|_F\|\mathsf{M}_2(\tilde{R})\|_F=2\|\tilde{Q}\|_E\|\tilde{R}\|_E,
$$
which is the inequality. For sharpness take $\tilde{Q}=\tilde{R}=e_0+ie_1$: then $\tilde{Q}^{2}=2e_0+2ie_1$ and $\|\tilde{Q}\|_E^{2}=2$, $\|\tilde{Q}^{2}\|_E=2\sqrt2$, so $\|\tilde{Q}^{2}\|_E=\sqrt2\,\|\tilde{Q}\|_E^{2}$.

**Corollary.** Multiplication $\mathbb{B}\times\mathbb{B}\to\mathbb{B}$ is continuous, inversion is continuous on the units, and $\mathbb{B}$ is a topological algebra over $\mathbb{R}$ with $\mathbb{B}^{\times}$ a topological group.

**Proof.** The inequality bounds the product in terms of the factors; inversion is a rational function of the coefficients, hence continuous on the set of invertible elements, and the group axioms hold there, so the operations are continuous.

**Proposition (the isometries that the algebra supplies).** Multiplication by a central element and the conjugations are orthogonal:

$$
\|(A e_0)\tilde{Q}\|_E=|A|\,\|\tilde{Q}\|_E,\qquad
\|\tilde{Q}^{\natural}\|_E=\|\bar{\tilde{Q}}\|_E=\|\tilde{Q}^{*}\|_E=\|\tilde{Q}\|_E .
$$

Moreover, for every unitary biquaternion $\tilde{U}$ the inner conjugation $\Theta_{\tilde{U}}(\tilde{T})=\tilde{U}\tilde{T}\tilde{U}^{*}$ is a Euclidean isometry.

**Proof.** A central multiplier scales every coefficient by $A$, and the three conjugations $\natural$, $\bar{\cdot}$, ${}^{*}$ (together with the reversal $\flat=-{}^{*}$) permute the coefficients among $\pm Q_\mu$ and $\pm\bar Q_\mu$, preserving $\sum_\mu|Q_\mu|^{2}$. For the last statement, $\mathsf{M}_2$ carries $\Theta_{\tilde{U}}$ to $M\mapsto M_{\tilde{U}}XM_{\tilde{U}}^{\dagger}$ with $M_{\tilde{U}}$ unitary, and the Frobenius norm is invariant under unitary similarity.

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

**Proof.** Each is a linear subspace of $\mathbb{B}$, and the homotopy above preserves it. The dimensions are those of *Comparison of the Remarkable Subspaces*.

**Corollary.** Every map into $\mathbb{B}$ is null-homotopic, and $\mathbb{B}$ carries no topological obstruction of its own; the topology of the algebra is entirely the topology of its distinguished subsets — the unit group, the singular cone and the spheres.

**Proof.** Immediate from the theorem.

The complement of the set of zero divisors is dense in $\mathbb{B}$, because that set is a proper algebraic subset of real codimension two — a complex hypersurface of $\mathbb{B}\cong\mathbb{C}^{4}$ — with empty interior (*Topology in the Space of Biquaternions*); this is what makes the group of units, an open dense subset, carry the topology it does.

## The Euclidean Unit Sphere

$$
S^{7}_{E}=\{\tilde{Q}\in\mathbb{B}:\|\tilde{Q}\|_E=1\}\cong S^{7}
$$

is, by the isometry of §*The Euclidean Norm and the Isometry onto $\mathbb{R}^{8}$*, the standard unit sphere of $\mathbb{R}^{8}$: closed, compact, connected, and a smooth $7$-manifold. It is nevertheless the **wrong** sphere for the algebra, and the reason is that $\|\cdot\|_E$ is not multiplicative: for $\tilde{Q}=e_1+ie_2$ one has $\tilde{Q}^{2}=0$ while $\|\tilde{Q}\|_E=\sqrt2$, so

$$
\tilde{Q}_0=\frac{e_1+ie_2}{\sqrt2}\in S^{7}_{E},\qquad \tilde{Q}_0^{2}=0,
$$

and $\tilde{Q}_0$ is a zero divisor. Hence $S^{7}_{E}\not\subseteq\mathbb{B}^{\times}$ and $S^{7}_{E}$ is not a subgroup of $\mathbb{B}^{\times}$.

**Proposition (the sphere meets the singular cone in a compact $5$-manifold).** The intersection $S^{7}_{E}\cap\mathcal{N}$, with $\mathcal{N}$ the set of zero divisors, is a compact real $5$-manifold without boundary, homeomorphic to the link of that cone.

**Proof.** The set of zero divisors is a real algebraic cone of real dimension $6$ with its only singular point at the origin (*The Topology of the Zero-Divisor Cone*); intersecting the smooth part with the transverse unit sphere and removing the origin gives a compact smooth manifold of dimension $6-1=5$, and it is the link by definition (*The Topology of the Zero-Divisor Cone*).

**Remark (the one sphere the topological norm defines).** The Euclidean sphere $S^{7}_{E}$ is the only sphere the topological norm of the space defines. The level sets of the algebra that carry a group structure — the compact subgroup $U(\mathbb{B})\cong U(2)$ of the unitary elements and the group developed in *The Biquaternion Unit Group as a Topological Group* — are not level sets of the topological norm, and their topology is proved in *The Unitary Group of the Biquaternion Algebra*.

## The Euclidean Space and the Duality

The real inner product $(\cdot,\cdot)_{\mathbb{R}}$ makes $\mathbb{B}$ a Euclidean space of dimension eight. Two structures follow and are recorded here because later articles use them.

**The Riesz duality.** Every $\mathbb{R}$-linear functional on $\mathbb{B}$ is $(\tilde{P},\cdot)_{\mathbb{R}}$ for a unique $\tilde{P}$. This is the finite-dimensional Riesz representation theorem, and it is what makes the adjoint operations of the operator articles well defined.

**The Riemannian metric.** $(\cdot,\cdot)_{\mathbb{R}}$ is the flat Riemannian metric of $\mathbb{B}\cong\mathbb{R}^{8}$; the orthogonal group $O(8)$ is its isometry group, and the $\mathbb{C}$-linear isometries that preserve the algebra structure are exactly the inner automorphisms by the unitary biquaternions, of group $PU(2)\cong SO(3)$ (*Biquaternion Automorphisms and Derivations*). Over $\mathbb{R}$ the coefficient conjugation adds one more coset, since it is an $\mathbb{R}$-algebra automorphism of unit Euclidean norm, so the real-linear automorphisms that are Euclidean isometries form $PU(2)\rtimes\mathbb{Z}/2$.

## Summary

The Euclidean norm is $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^{2})^{1/2}$, and the coefficient map is a linear isometry $\mathbb{B}\cong\mathbb{R}^{8}$. Multiplication satisfies the sharp inequality $\|\tilde{Q}\tilde{R}\|_E\leq\sqrt2\|\tilde{Q}\|_E\|\tilde{R}\|_E$, and central multipliers, the conjugations and inner conjugations by unitary elements are Euclidean isometries. The algebra is contractible, as is each of its remarkable subspaces, so every map into $\mathbb{B}$ is null-homotopic. The Euclidean unit sphere $S^{7}_{E}$ is a genuine $S^{7}$ but is not a group and contains zero divisors; its intersection with the singular cone is a compact $5$-manifold, the link. The level sets of the algebra that carry a group structure are treated in *The Biquaternion Unit Group as a Topological Group* and *The Unitary Group of the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde{P},\tilde{Q})_{\mathbb{R}}=\sum_\mu(p_\mu q_\mu+p'_\mu q'_\mu)$ | Real inner product; positive definite |
| $\|\tilde{Q}\|_E=(\sum_\mu\lvert Q_\mu\rvert^{2})^{1/2}$ | Euclidean norm |
| $\iota:\mathbb{B}\to\mathbb{R}^{8}$ | Linear isometry onto $\mathbb{R}^{8}$ |
| $\|\tilde{Q}\tilde{R}\|_E\leq\sqrt2\|\tilde{Q}\|_E\|\tilde{R}\|_E$ | Normed-algebra inequality, sharp |
| $H(t,\tilde{Q})=(1-t)\tilde{Q}$ | Contraction of $\mathbb{B}$ to $0$ |
| $S^{7}_{E}=\{\|\tilde{Q}\|_E=1\}$ | Euclidean unit sphere; not a group |
| $S^{7}_{E}\cap\mathcal{N}$ | Compact $5$-manifold; the link of the singular cone |
| $O(8)$ | Isometry group of the Euclidean structure |

## Further Reading

- *Topology in the Space of Biquaternions* (`articles_maths/topology-in-the-space-of-biquaternions.md`), for the definitions, the equivalence of norms and the uniqueness of the topology used here
- *The Topology of the Zero-Divisor Cone* (`articles_maths/the-topology-of-the-zero-divisor-cone.md`), for the zero divisors, their cone and the link used here
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the group of the unitary elements and the retraction of the group of units onto it
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the matrix reading of $\|\cdot\|_E$
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the invertibility criterion and the group of units
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the finite-dimensional inner-product-space facts used here
