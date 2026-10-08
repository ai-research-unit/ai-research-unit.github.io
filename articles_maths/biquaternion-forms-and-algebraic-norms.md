# __Biquaternion Forms and Algebraic Norms__

## Introduction

The biquaternion algebra carries four products, and the scalar part of each of them is a form on one and the same space. This article is the synthesis of those four forms: it states them with one bracket, compares their diagonals and their types, reads from them the norm-like objects the literature calls norms, and separates the objects that are norms in the sense of algebra from the objects that are norms in the sense of analysis.

Three norm-like objects come out of the four forms, and they are of different kinds. The **algebraic norm**, or multiplicative norm form, is complex-valued, multiplicative and vanishes on the zero divisors. The **Hermitian norm** is real, definite and not multiplicative. The **distances** read from the forms through their symmetries are four, and they coincide. The article states which of the four forms carries which object, proves the proposition that no single function can be of both kinds at once, and records the geometry the forms determine: the null cones, the level sets and the isometry groups.

The topology of the space is not among these objects. It is fixed by the linear structure alone and is built, without any form entering, in *Topology in the Space of Biquaternions*; every form of this article is read inside that one topology and adds nothing to it.

## Notation

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$ satisfying $e_k^{2}=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and with the central imaginary written $i$, so that it does not collide with the quaternion units. A general element is

$$
\tilde{Q}=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3,\qquad Q_\mu=q_\mu+iq'_\mu,\qquad q_\mu,q'_\mu\in\mathbb{R},
$$

with $\mathrm{Sc}(\tilde{Q})=Q_0$ the scalar part. The three conjugations are

$$
\tilde{Q}^{\natural}=Q_0-Q_1e_1-Q_2e_2-Q_3e_3,\qquad
\bar{\tilde{Q}}=\bar{Q}_0+\bar{Q}_1e_1+\bar{Q}_2e_2+\bar{Q}_3e_3,\qquad
\tilde{Q}^{*}=\bar{\tilde{Q}}^{\natural},
$$

and the four involutions $\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}$ are the four symmetries used below. The four forms are quoted from *The Four Biquaternion Complex Products* and *The Four Pairings of the Biquaternion Algebra*, and their restrictions to the six distinguished subspaces from *The Six Subspaces under the Complex Bilinear Form*.

## 1. The Four Forms

The four forms are the scalar parts of the four products, written with **one bracket** $\langle\cdot,\cdot\rangle$ and a subscript recording the conjugation entering each argument:

$$
\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}).
$$

| form | product | in coordinates | diagonal | linearity |
|---|---|---|---|---|
| complex bilinear | $\tilde{P}\tilde{Q}$ | $\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | $Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2}$ | linear in both arguments |
| quaternion bilinear | $\tilde{P}^{\natural}\tilde{Q}$ | $\sum_\mu P_\mu Q_\mu$ | $Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$ | linear in both arguments |
| complex sesquilinear | $\tilde{P}\tilde{Q}^{*}$ | $\sum_\mu P_\mu\overline{Q_\mu}$ | $\lvert Q_0\rvert^{2}+\lvert Q_1\rvert^{2}+\lvert Q_2\rvert^{2}+\lvert Q_3\rvert^{2}$ | conjugate-linear in the second |
| quaternion sesquilinear | $\tilde{P}^{\natural}\tilde{Q}^{*}$ | $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | $\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2}$ | conjugate-linear in the second |

with $\varepsilon=(1,-1,-1,-1)$. The prefixes name the conjugation the form is built from and not a signature or a base field: *complex* marks a form in which no natural conjugation enters, *quaternion* one in which it enters in the first argument; *bilinear* marks a form linear in both arguments, *sesquilinear* one conjugate-linear in the second.

## 2. The Four Diagonals and Their Types

The two bilinear forms have **quadratic** diagonals and the two sesquilinear forms have **Hermitian** diagonals, and the distinction matters because the two kinds behave differently under the conjugations and over the real numbers.

**Over $\mathbb{C}$.** A symmetric bilinear form on $\mathbb{C}^{n}$ has no inertia: every non-degenerate one is congruent to the identity, and the only invariant left is the rank, here $4$. A Hermitian form, by contrast, keeps its signature: the complex sesquilinear form has signature $(4,0)$, positive definite, and the quaternion sesquilinear form has signature $(1,3)$.

**Over $\mathbb{R}$.** Reading the four forms on the real coordinates, the four realifications have signatures

$$
\begin{array}{c|c}
\text{form} & \text{signature of the realification on }\mathbb{R}^{8}\\ \hline
\text{complex bilinear} & (4,4)\\
\text{quaternion bilinear} & (4,4)\\
\text{complex sesquilinear} & (8,0)\\
\text{quaternion sesquilinear} & (2,6)
\end{array}
$$

and only the third is definite. The indefinite ones are metric tensors of split signature and not norms.

**On the six distinguished subspaces.** The three involutions are diagonal, in the quaternion basis, on the four-dimensional real subspace $\mathbb{H}_{\mathbb{B}}$, on its imaginary translate $i\mathbb{H}_{\mathbb{B}}$, on the centre $\mathbb{C}_{\mathbb{B}}$, on the vector subspace $\mathrm{Vect}(\mathbb{B})$ and on the two sectors $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$, and the restrictions carry the signatures

$$
\begin{array}{c|cccccc}
\text{subspace} & \mathbb{C}_{\mathbb{B}} & \mathrm{Vect}(\mathbb{B}) & \mathbb{H}_{\mathbb{B}} & i\mathbb{H}_{\mathbb{B}} & \mathbb{M}_{+} & \mathbb{M}_{-}\\ \hline
\text{signature of } N & (1,1) & (3,3) & (4,0) & (0,4) & (1,3) & (3,1)
\end{array}
$$

with $N$ the algebraic norm of §3. The six signatures are the quantitative form of the statement that one algebra carries six real forms, and they are the reason the two sectors of the framework have their names: $\mathbb{H}_{\mathbb{B}}$ is positive definite, $i\mathbb{H}_{\mathbb{B}}$ negative definite, and the sectors indefinite with opposite conventions.

## 3. The Algebraic Norm

**Definition.** The **algebraic norm**, or **multiplicative norm form**, of a biquaternion is

$$
N(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_{\mu=0}^{3}Q_\mu^{2}\in\mathbb{C}.
$$

It is the diagonal of the **quaternion bilinear form**, and its polar form is that form itself, $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$.

**Properties.**

- **Multiplicativity.** $N(\tilde{P}\tilde{Q})=N(\tilde{P})N(\tilde{Q})$, because $N$ is central and $(\tilde{P}\tilde{Q})^{\natural}=\tilde{Q}^{\natural}\tilde{P}^{\natural}$. This is the defining property of the norm of an algebra, and it is why this object is *the* norm of the biquaternion algebra.
- **Reduced norm.** $N(\tilde{Q})=\det\Phi(\tilde{Q})$ under the realization $\Phi$, so the algebra is read as a quadratic space with a reduced norm.
- **Vanishing set.** $N(\tilde{Q})=0$ for a nonzero $\tilde{Q}$ exactly when $\tilde{Q}$ is a zero divisor; the zero set of $N$ is the union of the zero divisors with the origin, and it is the **null cone** of the form.
- **Invertibility.** $\tilde{Q}$ is invertible if and only if $N(\tilde{Q})\neq0$, with $\tilde{Q}^{-1}=\tilde{Q}^{\natural}/N(\tilde{Q})$.
- **The multiplicative real norm.** $\lvert N\rvert$ and $\sqrt{\lvert N\rvert}$ are not norms of the space, but $r(\tilde{Q})=\sqrt{\lvert N(\tilde{Q})\rvert}$ is the **unique** multiplicative real norm on the group of units normalised by $r(\lambda e_0)=\lvert\lambda\rvert$ for real $\lambda$.

The detail is in *Biquaternion Norm and Invertibility*, and the vanishing set in *Biquaternion Zero Divisors*.

**The second algebraic norm.** The **quaternionic product** (the product whose slots are conjugated in the first argument) carries the polynomial $Q_0^{2}-Q_1^{2}-Q_2^{2}+Q_3^{2}$, and the four products carry four such degree-two functions; the four-products synthesis is *The Four Products and Their Two Slots: the Two Algebras and the Two Sesqualgebras* and *The Realification of the Four Forms*.

## 4. No Function Is Both

**Proposition.** There is no function on $\mathbb{B}$ that is both definite and multiplicative.

**Proof.** The algebra has zero divisors: for example

$$
(e_0+ie_1)(e_0-ie_1)=e_0-i^{2}e_1^{2}=e_0-(-1)(-1)e_0=0,
$$

with $e_0\pm ie_1\neq0$, and $N(e_0\pm ie_1)=1+i^{2}=0$. Suppose $\lVert\cdot\rVert$ were definite and multiplicative. Then $\lVert e_0+ie_1\rVert$ and $\lVert e_0-ie_1\rVert$ are nonzero, since the factors are nonzero, whereas

$$
\lVert e_0+ie_1\rVert\lVert e_0-ie_1\rVert=\lVert (e_0+ie_1)(e_0-ie_1)\rVert=\lVert 0\rVert=0,
$$

which is impossible in the real numbers. $\square$

**Corollary.** $N$ is multiplicative and not definite; the norm of the complex sesquilinear diagonal is definite and not multiplicative; and no third function repairs the split.

The coincidence that fails here is the one that holds for the normed division algebras. For $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and the octonions the multiplicative form is real and positive on the nonzero elements and equal to the square of the Euclidean norm, so the two senses of *norm* are one function; by the Hurwitz theorem these four are the only normed division algebras (*Normed Division Algebras and the Hurwitz Theorem*). The biquaternions are excluded by their zero divisors, exactly as the proposition shows.

The coincidence is recovered on the parts of $\mathbb{B}$ where $N$ does not vanish: on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where $N$ is real of signature $(4,0)$ and $N(\tilde{Q})=\lVert\tilde{Q}\rVert^{2}$; on the imaginary translate $i\mathbb{H}_{\mathbb{B}}$, where $N$ is real of signature $(0,4)$ and $N(\tilde{Q})=-\lVert\tilde{Q}\rVert^{2}$; and on the two sectors, where $N$ is indefinite and the norm and the interval differ by a sign on one of the two halves. It is the whole algebra, taken at once, that no single function norms.

## 5. Distances Read from the Forms

Each of the four forms is non-degenerate, so each admits a **symmetry**: an involution $J$ with $\Phi(\tilde{P},J\tilde{Q})$ a definite form, from which a distance is read as

$$
d_J(\tilde{P},\tilde{Q})^{2}=\mathrm{Re}\,\Phi(\tilde{P}-\tilde{Q},\,J(\tilde{P}-\tilde{Q})),\qquad
\Phi\in\{\langle\cdot,\cdot\rangle,\ \langle\cdot,\cdot\rangle_{\natural},\ \langle\cdot,\cdot\rangle_{*},\ \langle\cdot,\cdot\rangle_{\natural*}\}.
$$

The four symmetries are the four involutions, and each of them carries its form to the complex sesquilinear form, whose diagonal is definite:

| form | symmetry $J$ | the distance it yields |
|---|---|---|
| complex bilinear | ${}^{*}$ | $d(\tilde{P},\tilde{Q})=\lVert\tilde{P}-\tilde{Q}\rVert$ |
| quaternion bilinear | $\bar{\cdot}$ | $d(\tilde{P},\tilde{Q})=\lVert\tilde{P}-\tilde{Q}\rVert$ |
| complex sesquilinear | $\mathrm{id}$ | $d(\tilde{P},\tilde{Q})=\lVert\tilde{P}-\tilde{Q}\rVert$ |
| quaternion sesquilinear | ${}^{\natural}$ | $d(\tilde{P},\tilde{Q})=\lVert\tilde{P}-\tilde{Q}\rVert$ |

So the four forms give **one** distance, through four different symmetries; the diagonal route reaches it for the third form alone, and the symmetry route for all four. The four symmetries are moreover isometries of that distance. This is a statement about the forms and their geometry; the topology in which the distance is read is fixed independently of them in *Topology in the Space of Biquaternions*.

## 6. The Geometry: Null Sets, Level Sets and Isometry Groups

What distinguishes the four forms is not a topology but a geometry, and each form has its own.

- **Null sets.** The null set of $N$ is the zero-divisor cone of §3. The null set of the quaternion sesquilinear form is the Krein null cone, of signature $(2,6)$ in the realification, and the fundamental decomposition of that form splits the algebra into the informational and the material sector. The complex sesquilinear form is definite and has no nonzero null vector; it is the only one of the four with that property.
- **Level sets.** $\{N(\tilde{Q})=1\}$ is a non-compact real $6$-manifold homotopy equivalent to $S^{3}$, and it is the only level set of the four forms that is a group, the norm-one group $\mathbb{B}^{\times}_{1}$; the level set of the complex sesquilinear diagonal is the sphere $S^{7}=\{\lVert\tilde{Q}\rVert=1\}$; the level set of the complex bilinear form is a hyperquadric of signature $(4,4)$; and the level set of the quaternion sesquilinear form is the Krein sphere of signature $(2,6)$.
- **Isometry groups.** Each form has a complex-linear isometry group and a real one, and they are different groups:

$$
\begin{array}{c|cc}
\text{form} & \text{complex-linear isometry group} & \text{real isometry group}\\ \hline
\text{complex bilinear} & O_4(\mathbb{C}) & O(4,4)\\
\text{quaternion bilinear} & O_4(\mathbb{C}) & O(4,4)\\
\text{complex sesquilinear} & U(4) & O(8)\\
\text{quaternion sesquilinear} & U(1,3) & O(2,6)
\end{array}
$$

The two bilinear forms are congruent over $\mathbb{C}$ and therefore have the same complex-linear isometry group $O_4(\mathbb{C})$; the complex-linear isometries of the alternating form of the plain product are $U(4)$; and the real group is the larger group read in real coordinates. Each is a closed subgroup of $GL_8(\mathbb{R})$ and each is the symmetry group of the corresponding level set. The full tables are in *Topology and Metric for Each of the Twelve Operations*.

## 7. The Two Categories in the Framework

The two senses of *norm* are not a pedantic distinction in the biquaternion framework, because the framework uses both objects and assigns them different roles.

- The **algebraic norm** restricted to the material sector $\mathbb{M}_{-}$ is the interval of signature $(3,1)$,
  $$N|_{\mathbb{M}_{-}}(\tilde{Q})=-x_0^{2}+x_1^{2}+x_2^{2}+x_3^{2},$$
  whose zero set is the light cone; its vanishing at a nonzero four-vector is the algebraic statement that the four-vector is null. This is the object of *The Anti-Hermitian Subspace $\mathbb{M}_{-}$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`).
- The **Hermitian norm**, the square root of the diagonal of the complex sesquilinear form, is the length of the state space: it is the norm of the informational sector $\mathbb{M}_{+}$, where the form is positive definite and the pairing is the trace pairing from which the Born rule is read. This is the object of *The Hermitian Subspace $\mathbb{M}_{+}$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`).

The two cannot be interchanged: the interval must be indefinite for the light cone to exist, and the state-space norm must be definite for positivity to exist. The proposition of §4 is the reason the framework cannot have a single object doing both.

## Summary

The four products of the algebra have four scalar parts, and the four forms they define carry three norm-like objects of two different kinds. The **algebraic norm** $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^{2}$ is complex-valued, multiplicative, equal to $\det\Phi(\tilde{Q})$ and zero exactly on the zero divisors; it is the norm of the algebra and it is the interval of signature $(3,1)$ on the material sector. The **Hermitian norm** read from the complex sesquilinear form is real, definite, equal to the Euclidean norm of $\mathbb{R}^{8}$ and not multiplicative; it is the norm of the state space. The two **cannot** be one function, because the algebra has zero divisors, as $(e_0+ie_1)(e_0-ie_1)=0$ shows; the coincidence of the two senses that holds for the normed division algebras of the Hurwitz theorem fails here, and it is recovered only on the parts of the algebra where $N$ does not vanish. The four **distances** read from the four forms through their four symmetries coincide. And what the forms distinguish is a geometry — four null sets, four level sets, two complex-linear and four real isometry groups — read inside the one topology built from the linear structure in *Topology in the Space of Biquaternions*.

## Further Reading

- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`) and *Comparison between the Four Biquaternion Products* (`articles_maths/comparison-between-the-four-biquaternion-products.md`), the four products and their scalar parts.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), the algebraic norm, its polarisation, the six real forms and the group of units; *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), its vanishing set.
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), the complex sesquilinear form and its diagonal.
- *The Six Subspaces under the Complex Bilinear Form* (`articles_maths/the-six-subspaces-under-the-complex-bilinear-form.md`) and *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), the restrictions and the signatures of §2.
- *The Four Products and Their Two Slots: the Two Algebras and the Two Sesqualgebras* (`articles_maths/the-four-products-and-their-two-slots-the-two-algebras-and-the-two-sesqualgebras.md`), the four products as one two-slot construction.
- *Topology and Metric for Each of the Twelve Operations* (`articles_maths/topology-and-metric-for-each-of-the-twelve-operations.md`), the same objects for the twelve operations, with the full isometry tables.
- *Normed Division Algebras and the Hurwitz Theorem* (`articles_maths/normed-division-algebras-and-the-hurwitz-theorem.md`), the coincidence that fails for the biquaternions; *List of Norms and Seminorms* (`articles_maths/list-of-norms-and-seminorms.md`) and *Quadratic Forms over Algebras and Norms* (`articles_maths/quadratic-forms-over-algebras-and-norms.md`).
- *Topology in the Space of Biquaternions* (`articles_maths/topology-in-the-space-of-biquaternions.md`), the topology, built from the linear structure alone.
