# __The Six Subspaces__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four conjugations, and each of them is an involution. Each one splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and the eight spaces so obtained reduce to six distinct subspaces, the **remarkable subspaces** of $\mathbb{B}$. The conjugations themselves are not the subject of this article: their definitions are in *The Biquaternion Algebra*, the group they form is in *The Group of Involutions* and the two spaces each defines are in *The Subspaces and Their Relations*.

This article is the single article of the group for the remarkable subspaces, one to a section. Each section gives the defining condition of the subspace, the coordinate condition it amounts to, the real basis that exhibits it and its real dimension, and the algebraic role it plays. The conjugations are defined in *The Element, the Coordinates and the Conjugations*, the group they form is *The Group of Involutions*, and the relations between the subspaces are *The Subspaces and Their Relations*. What the subspaces carry beyond their linear algebra is treated where those notions are introduced. The table is the summary; the sections are the detail.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | role |
|---|---|---|---|---|
| the centre $\mathbb{C}_{\mathbb{B}}$ | $\tilde{Q}^{\natural} = \tilde{Q}$ | $e_t, ie_t$ | $2$ | the centre of the algebra, a field |
| the vector subspace $\mathrm{Vect}(\mathbb{B})$ | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $\vec e_x, \vec e_y, \vec e_z, i\vec e_x, i\vec e_y, i\vec e_z$ | $6$ | the kernel of the scalar part, a Lie algebra |
| the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ | a division algebra |
| the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = -\tilde{Q}$ | $ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $4$ | $i$ times the quaternion subspace |
| the Hermitian subspace $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $4$ | the fixed space of ${}^{*}$, not a subalgebra |
| the anti-Hermitian subspace $\mathbb{M}_-$ | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ | a Lie algebra |

The remarkable subspaces are pairwise distinct. Their relations — the coordinate blocks out of which they are built, their pairwise intersections, their sums, the action of the four conjugations and the action of the central imaginary unit — are the subject of *The Subspaces and Their Relations*, and are not treated here. The three direct-sum decompositions the conjugations cut out are *The Three Eigenspace Decompositions*. The product and its two halves, the Jordan algebra and the Lie algebra, the symmetrized product and the trace form are the business of *Remarkable Subspaces and the Four General Products, Forms and Norms* and *Symmetric and Antisymmetric Decomposition of the Four General Products*; the four forms on the remarkable subspaces are the business of the five *Remarkable Subspaces under ...* articles and of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the two matrix realizations are the business of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant* and *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*.

Nothing below is a physical statement. The elements are written $\tilde{Q}, \tilde{Q}_1, \tilde{Q}_2, \dots$, their complex coefficients $Q_t, Q_x, Q_y, Q_z$, and the real and imaginary parts of a coefficient $Q_\mu = q_\mu + i q'_\mu$; no other coordinates are used.

## The Centre Subspace

**Definition.** The **centre subspace** $\mathbb{C}_{\mathbb{B}}$ is the fixed space of quaternion conjugation,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = \tilde{Q} \right\} .
$$

**Coordinate condition.** Writing $\tilde{Q} = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ and comparing the two sides of $\tilde{Q}^{\natural} = \tilde{Q}$ coefficient by coefficient, the coefficient of $e_t$ gives no condition while the coefficient of $\vec e_k$ gives $-Q_k = Q_k$, that is $Q_k = 0$, for $k = 1, 2, 3$. The subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_te_t , \qquad Q_t \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $e_t, ie_t$ and $\dim_{\mathbb{R}}\mathbb{C}_{\mathbb{B}} = 2$. In the eight real coordinates it is the coordinate plane $q_x = q_y = q_z = q'_x = q'_y = q'_z = 0$.

**Role.** It is the centre of the algebra, the set of elements that commute with every element, and it is a commutative subalgebra isomorphic to $\mathbb{C}$; it is one of the two of the remarkable subspaces that are closed under the product. Its elements are the **central elements**, written $Ae_t$ with $A \in \mathbb{C}$.

## The Vector Subspace

**Definition.** The **vector subspace** $\mathrm{Vect}(\mathbb{B})$ is the anti-fixed space of quaternion conjugation,

$$
\mathrm{Vect}(\mathbb{B}) = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** Comparing coefficients, the condition is $Q_t = 0$: the scalar part vanishes, and the subspace is the kernel of the scalar-part functional $\operatorname{Sc}(\tilde{Q}) = Q_t = \tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$,

$$
\tilde{Q} = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z , \qquad Q_x, Q_y, Q_z \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $\vec e_x, \vec e_y, \vec e_z, i\vec e_x, i\vec e_y, i\vec e_z$ and $\dim_{\mathbb{R}}\mathrm{Vect}(\mathbb{B}) = 6$. It is the largest of the remarkable subspaces, and the only one of dimension $6$.

**Role.** It is not a subalgebra, since the product of two pure vectors has a scalar part; it is closed under the commutator, the bracket of two pure vectors being twice their cross product. It splits into the real vector triple $\operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ and the imaginary vector triple $\operatorname{span}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, and its elements are the **pure vectors**, written $\vec Q$.

## The Quaternion Subspace

**Definition.** The **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ is the fixed space of complex conjugation,

$$
\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be fixed by complex conjugation, that is, that each be real, $Q_\mu = q_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $e_t, \vec e_x, \vec e_y, \vec e_z$ and $\dim_{\mathbb{R}}\mathbb{H}_{\mathbb{B}} = 4$. It is the copy of the real quaternion algebra inside $\mathbb{B}$.

**Role.** It is a subalgebra, the second of the two of the remarkable subspaces that are closed under the product, and it is a division algebra: every non-zero element is a unit. It is the only one of the remarkable subspaces that is non-commutative, and it is the image of the structure map $\mathbb{H} \to \mathbb{B}$, $h \mapsto he_t$.

## The Anti-Quaternion Subspace

**Definition.** The **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed space of complex conjugation,

$$
i\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be negated by complex conjugation, that is, that each be purely imaginary, $Q_\mu = iq'_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ and $\dim_{\mathbb{R}}i\mathbb{H}_{\mathbb{B}} = 4$.

**Role.** Its elements are exactly the products $i\tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$, so the subspace is the image of $\mathbb{H}_{\mathbb{B}}$ under multiplication by the central imaginary unit. It is not a subalgebra — the product of two of its elements lands in the quaternion subspace — but it is stable under multiplication by $\mathbb{H}_{\mathbb{B}}$ on both sides. It splits into the imaginary scalar line $\mathbb{R}(ie_t)$ and the imaginary vector triple $\operatorname{span}\{i\vec e_x,i\vec e_y,i\vec e_z\}$.

## The Hermitian Subspace

**Definition.** The **Hermitian subspace** $\mathbb{M}_+$ is the fixed space of Hermitian conjugation,

$$
\mathbb{M}_+ = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = \tilde{Q} \right\} , \qquad \tilde{Q}^{*} = \bar{\tilde{Q}}^{\natural} .
$$

**Coordinate condition.** Since ${}^{*} = \bar{\cdot}\circ{}^{\natural}$, the condition is that the scalar coefficient be real while the three vector coefficients be purely imaginary,

$$
\tilde{Q} = q_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z , \qquad q_t, q'_x, q'_y, q'_z \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ and $\dim_{\mathbb{R}}\mathbb{M}_+ = 4$.

**Role.** It is not a subalgebra: the plain product of two of its elements need not lie in it, while the symmetrized combination $\tfrac{1}{2}(\tilde{Q}_1\tilde{Q}_2+\tilde{Q}_2\tilde{Q}_1)$ of two of its elements does. It is the set of elements with real scalar part and purely imaginary vector part.

## The Anti-Hermitian Subspace

**Definition.** The **anti-Hermitian subspace** $\mathbb{M}_-$ is the anti-fixed space of Hermitian conjugation, which is also the fixed space of the reversal $\flat = -{}^{*}$,

$$
\mathbb{M}_- = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = -\tilde{Q} \right\} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\flat} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is the reverse of the Hermitian one: the scalar coefficient is purely imaginary and the three vector coefficients are real,

$$
\tilde{Q} = iq'_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z , \qquad q'_t, q_x, q_y, q_z \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $ie_t, \vec e_x, \vec e_y, \vec e_z$ and $\dim_{\mathbb{R}}\mathbb{M}_- = 4$.

**Role.** It is not a subalgebra and it is not closed under the symmetrized product; it is closed under the commutator, and it is a real Lie algebra of dimension four whose centre is the line $\mathbb{R}(ie_t)$. It is the set of elements with purely imaginary scalar part and real vector part, and it is the anti-fixed space of ${}^{*}$ as well as the fixed space of $\flat$.

## Summary

The biquaternion algebra carries four conjugations whose fixed and anti-fixed spaces reduce to six distinct subspaces, the remarkable subspaces. The centre $\mathbb{C}_{\mathbb{B}}$, fixed by ${}^{\natural}$, is the set of elements with vanishing vector part, of real basis $e_t, ie_t$ and dimension $2$; it is the centre of the algebra and a field. The vector subspace $\mathrm{Vect}(\mathbb{B})$, anti-fixed by ${}^{\natural}$, is the kernel of the scalar part, of real basis $\vec e_x, \vec e_y, \vec e_z, i\vec e_x, i\vec e_y, i\vec e_z$ and dimension $6$; it is closed under the commutator and not under the product. The quaternion subspace $\mathbb{H}_{\mathbb{B}}$, fixed by $\bar{\cdot}$, is the set of elements with real coefficients, of real basis $e_t, \vec e_x, \vec e_y, \vec e_z$ and dimension $4$; it is a division subalgebra. The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, anti-fixed by $\bar{\cdot}$, is $i$ times the quaternion subspace, of real basis $ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ and dimension $4$; it is not a subalgebra and is stable under multiplication by $\mathbb{H}_{\mathbb{B}}$ on both sides. The Hermitian subspace $\mathbb{M}_+$, fixed by ${}^{*}$, is the set of elements with real scalar part and purely imaginary vector part, of real basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ and dimension $4$; the symmetrized combination of two of its elements stays in it. The anti-Hermitian subspace $\mathbb{M}_-$, anti-fixed by ${}^{*}$ and fixed by $\flat$, is the set of elements with purely imaginary scalar part and real vector part, of real basis $ie_t, \vec e_x, \vec e_y, \vec e_z$ and dimension $4$; it is a real Lie algebra.

Exactly two of the remarkable subspaces are closed under the product, the centre and the quaternion subspace. The six are pairwise distinct; their relations are collected in *The Subspaces and Their Relations*, and what each one carries beyond its linear algebra is treated where those notions are introduced.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | the basis, with $e_t$ the unit and $\vec e_k^2 = -e_t$ |
| $i$ | the central imaginary unit, $i^2 = -1$, commuting with every element |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a general biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | the complex coefficient of $e_\mu$, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, \flat$ | quaternion, complex, Hermitian conjugation and reversal |
| $\operatorname{Sc}(\tilde{Q})$ | the scalar part $Q_t$, equal to $\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$ |
| $\mathbb{C}_{\mathbb{B}}$ | the centre subspace, fixed by ${}^{\natural}$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, anti-fixed by ${}^{\natural}$ |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde{Q}_1 \bullet \tilde{Q}_2$ | the symmetrized product $\tfrac{1}{2}(\tilde{Q}_1\tilde{Q}_2 + \tilde{Q}_2\tilde{Q}_1)$ |
| $\vec\rho, \vec\rho'$ | the real and imaginary parts of a complex vector |

## Further Reading

- [The Subspaces and Their Relations](the-subspaces-and-their-relations.html), for the coordinate blocks, the intersections, the sums and the action of the conjugations on the remarkable subspaces
- [The Three Eigenspace Decompositions](the-three-eigenspace-decompositions.html), for the three eigenspace decompositions the conjugations cut out, one pair of subspaces to each
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the four general products brought to the remarkable subspaces together, the product of two elements of the remarkable subspaces, and the Jordan and the Lie algebra each subspace carries and with which product
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms on the remarkable subspaces side by side, the only orthogonal pair and the comparison of the two readings
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), [Remarkable Subspaces under the General Plain Sesqualgebra](remarkable-subspaces-under-the-general-plain-sesqualgebra.html), [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restrictions themselves, subspace by subspace and form by form, and for the isotropic lines and the minimal ideals the remarkable subspaces determine
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, the inverse formula and the unit group of the whole algebra
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the zero divisors of the whole algebra, the pure and the non-pure family and the bivector form of the pure ones
- [Square Roots of an Element](square-roots-of-an-element.html), for the three classifications in the whole algebra
- [Idempotents](idempotents.html), for the classification of the idempotents of the whole algebra, the bijection with the roots of minus one and the projection reading
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce decomposition in the whole algebra; simplicity and the length are *The Regular Module*, and the minimal ideals are *The Minimal Left Ideals*
- [The Category of Modules](the-category-of-modules.html), for the simple module $S$, the minimal left ideals and the Morita equivalence
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the product and its scalar–vector form
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the two parts into which the product splits
- [The Group of Involutions](the-group-of-involutions.html), for the group the four conjugations generate
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, its basis, its conjugations and its coordinate systems
