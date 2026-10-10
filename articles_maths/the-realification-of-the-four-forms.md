
# __The Realification of the Four Forms__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four distinguished complex forms — the two bilinear and the two sesquilinear of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* — and each of them is complex-valued. Read over the real scalars, the algebra is the vector space $\mathbb{R}^{8}$, and the **real part** of each form is a real symmetric bilinear form on that space. This article is the entry point of the group that reads the four forms over $\mathbb{R}$: it fixes the real basis, computes the four realified Gram matrices and their signatures, reads the remarkable real subspaces through all four forms at once, describes the four realified null cones, and separates the realified forms from the complex forms they come from.

The article is organised around one caution. **The realified form is not the complex form.** The realification keeps the real part and discards the imaginary part, so the object computed here is a real symmetric form on a space of dimension eight and not the complex form it comes from. In particular the null set of the realified form is a real hypersurface of real dimension $7$, strictly larger than the complex null cone of the same form, which is the common zero set of the real and the imaginary parts and has real dimension $6$. The notation must therefore always say which object is meant: the symmetric bilinear form on $\mathbb{R}^{8}$, or the complex form on $\mathbb{C}^{4}$ whose real part it is.

The result that fixes the group is the signature table. The four realified signatures are $(4,4)$ for the general plain bilinear form, $(4,4)$ for the general quaternionic bilinear form, $(8,0)$ for the Hermitian form and $(2,6)$ for the Krein form. This article is their common source: the table is stated once, here, and quoted elsewhere. All four realified forms are diagonal in the eight real basis elements, with sign patterns $+,-,-,-,-,+,+,+$; $+,+,+,+,-,-,-,-$; $+,+,+,+,+,+,+,+$; and $+,-,-,-,+,-,-,-$, and everything below is read from those four strings.

**Boundary.** The four forms themselves, their polarisations, their adjoints and their automorphism groups belong to *The Four Pairings of the Biquaternion Algebra* and to the $2\times2$ and $4\times4$ representation articles of the four layers, and their comparison on the remarkable subspaces is the sequence *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*, *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions* and *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*. The comparison of the four forms as complex objects is the Synthesis group and is not repeated here.

## The Real Basis and the Realification

**Definition (the real basis).** Recall from *Biquaternions as a Vector Space over $\mathbb{R}$* that the eight elements

$$
e_{0},\ e_{1},\ e_{2},\ e_{3},\ ie_{0},\ ie_{1},\ ie_{2},\ ie_{3}
$$

are a basis of $\mathbb{B}$ over $\mathbb{R}$, with $e_{0}$ the identity, $e_{k}^{2}=-e_{0}$ for $k=1,2,3$, and $i$ the central scalar imaginary. A general element is written

$$
\tilde Q=\sum_{\mu=0}^{3}q_{\mu}e_{\mu}+\sum_{\mu=0}^{3}q'_{\mu}\,ie_{\mu},\qquad q_{\mu},q'_{\mu}\in\mathbb{R},
$$

and the coordinates $(q_{0},q_{1},q_{2},q_{3},q'_{0},q'_{1},q'_{2},q'_{3})$ identify $\mathbb{B}$ with $\mathbb{R}^{8}$. Throughout, $\varepsilon=(1,-1,-1,-1)$, $\mathrm{D}=\operatorname{diag}(1,-1,-1,-1)$, and $\mathrm{I}_{4}$, $\mathrm{I}_{8}$ are the identities of orders four and eight.

**Definition (the realification of a form).** Let $\Phi$ be a complex-valued form on $\mathbb{B}$. Its **realification** is the real-valued form $\Phi_{\mathbb{R}}(\tilde P,\tilde Q)=\mathrm{Re}\,\Phi(\tilde P,\tilde Q)$.

**Proposition (the four realifications are real symmetric bilinear forms).** The real parts of the four forms

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),\quad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q),\quad
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*}),\quad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*}),
$$

are real symmetric bilinear forms on $\mathbb{R}^{8}$.

*Proof.* The scalar part is $\mathbb{R}$-linear in each argument up to the conjugation it carries: the two bilinear forms are $\mathbb{C}$-bilinear and symmetric, and the two sesquilinear forms are conjugate-linear in the second argument and Hermitian; in both cases taking the real part leaves a real form that is symmetric. Both the value set and the symmetry are unaffected by the passage to the real part.

**Proposition (the central scalar is an form reversal for the bilinear forms and a form-preserving map for the sesquilinear ones).** Multiplication by $i$, written $J$, satisfies

$$
\langle J\tilde P,J\tilde Q\rangle_{\mathbb{R}}=-\langle\tilde P,\tilde Q\rangle_{\mathbb{R}},\qquad
\langle J\tilde P,J\tilde Q\rangle_{\natural\mathbb{R}}=-\langle\tilde P,\tilde Q\rangle_{\natural\mathbb{R}},
$$

and

$$
\langle J\tilde P,J\tilde Q\rangle_{*\mathbb{R}}=\langle\tilde P,\tilde Q\rangle_{*\mathbb{R}},\qquad
\langle J\tilde P,J\tilde Q\rangle_{\natural*\mathbb{R}}=\langle\tilde P,\tilde Q\rangle_{\natural*\mathbb{R}}.
$$

*Proof.* The general plain bilinear forms satisfy $\langle iP,iQ\rangle=-\langle P,Q\rangle$ by the $\mathbb{C}$-bilinearity, and the sesquilinear forms satisfy $\langle iP,iQ\rangle_{*}=\langle P,Q\rangle_{*}$ because the conjugate-linear argument contributes $\overline{i}=-i$; taking real parts gives the four identities.

**Remark (the dictionary between the complex and the real reading).** The realification discards the imaginary part of the complex form. For the two bilinear forms the discarded part is a second real symmetric bilinear form; for the two sesquilinear forms it is an alternating form, the Kähler form of the Hermitian structure. This group uses the real part only, and the propositions above are the whole dictionary: the complex form is recovered from its realification together with the complex structure $J$, and $J$ is an form reversal of the bilinear realifications and an automorphism of the sesquilinear ones. The sign flip of the two bilinear realifications, and its absence for the two sesquilinear ones, is exactly the block structure of the Gram matrices below.

## The Four Gram Matrices

**Theorem (the Gram matrices in the real basis).** In the real basis $(e_{0},e_{1},e_{2},e_{3},ie_{0},ie_{1},ie_{2},ie_{3})$ the four realified forms have the Gram matrices

| form | Gram matrix | diagonal signs | signature |
|---|---|---|---|
| general plain bilinear | $\operatorname{diag}(\mathrm{D},-\mathrm{D})$ | $+,-,-,-,-,+,+,+$ | $(4,4)$ |
| general quaternionic bilinear | $\operatorname{diag}(\mathrm{I}_{4},-\mathrm{I}_{4})$ | $+,+,+,+,-,-,-,-$ | $(4,4)$ |
| Hermitian | $\mathrm{I}_{8}$ | $+,+,+,+,+,+,+,+$ | $(8,0)$ |
| Krein | $\operatorname{diag}(\varepsilon,\varepsilon)$ | $+,-,-,-,+,-,-,-$ | $(2,6)$ |

*Proof.* Write $\tilde P=\sum_\mu p_\mu e_\mu+\sum_\mu p'_\mu ie_\mu$ and $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu ie_\mu$. For the general plain bilinear form, $\mathrm{Re}\,\varepsilon_\mu P_\mu Q_\mu=\varepsilon_\mu(p_\mu q_\mu-p'_\mu q'_\mu)$, giving the two blocks $\mathrm{D}$ and $-\mathrm{D}$. For the general quaternionic bilinear form the same computation with $\varepsilon_\mu=1$ gives the two blocks $\mathrm{I}_{4}$ and $-\mathrm{I}_{4}$. For the Hermitian form, $\mathrm{Re}\,P_\mu\overline{Q_\mu}=p_\mu q_\mu+p'_\mu q'_\mu$, giving $\mathrm{I}_{8}$. For the Krein form, $\mathrm{Re}\,\varepsilon_\mu P_\mu\overline{Q_\mu}=\varepsilon_\mu(p_\mu q_\mu+p'_\mu q'_\mu)$, giving the two equal blocks $\operatorname{diag}(\varepsilon)$. The signatures are the counts of signs, $4+4$, $4+4$, $8+0$ and $2+6$.

**Corollary (the four signatures).** The realified signatures, in the order general plain bilinear, general quaternionic bilinear, Hermitian, Krein, are

$$
(4,4),\qquad (4,4),\qquad (8,0),\qquad (2,6).
$$

**Remark (why two blocks, and why the sign repeats).** The two-block structure of the bilinear Gram matrices is the form reversal $J$: it exchanges the block $\mathrm{D}$ with the block $-\mathrm{D}$, hence the split signature $(4,4)$ of a form whose complex inertia is $(1,3)$. The repeated block of the sesquilinear Gram matrices is the $J$ of the proposition above, which preserves the form; the Krein form therefore repeats the sign string $\varepsilon$ where the general plain bilinear form reverses it, and this is the only difference between the two matrices $\operatorname{diag}(\mathrm{D},-\mathrm{D})$ and $\operatorname{diag}(\varepsilon,\varepsilon)$.

**Remark (the Hermitian realification is the definite form).** The Hermitian realification is positive definite, $\langle\tilde Q,\tilde Q\rangle_{*\mathbb{R}}=\sum_\mu(q_\mu^{2}+{q'_\mu}^{2})$, and it is the ordinary inner product of $\mathbb{R}^{8}$. It is the one form of the four with no null vector but $0$, and it is the form the next sections use.

## Remarkable Subspaces under the Four Realified Forms

The algebra has remarkable real subspaces: the centre $\mathbb{C}_{\mathbb{B}}$ and the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_{+},\mathbb{M}_{-}$ (*Introduction to the Remarkable Subspaces*). Their real dimensions are $2,6,4,4,4,4$. The four realified forms restrict to them as follows.

**Theorem (the four restriction tables).** In the natural real basis of each subspace the signatures are

| subspace | general plain bilinear | general quaternionic bilinear | Hermitian | Krein |
|---|---|---|---|---|
| centre $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $(1,1)$ | $(2,0)$ | $(2,0)$ |
| vector $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $(3,3)$ | $(6,0)$ | $(0,6)$ |
| quaternion $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| Hermitian $\mathbb{M}_{+}$ | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |
| anti-Hermitian $\mathbb{M}_{-}$ | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |

Every entry is the inertia of the restricted form in the natural real basis of the subspace, that is the diagonal of the restriction. It agrees row by row with the complex readings of *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* and *The Krein Gram Matrix and the Restrictions of the Form*, and with the Hermitian table of *Biquaternion Norm and Invertibility*.

**Remark (the definite rows).** Each form has its own definite rows, and the four are different. The **Hermitian** form is positive definite on all remarkable subspaces and is the definite structure. The **general plain bilinear** form is definite on $\mathbb{M}_{+}$, of signature $(4,0)$, and on $\mathbb{M}_{-}$, of signature $(0,4)$. The **general quaternionic bilinear** form is definite on $\mathbb{H}_{\mathbb{B}}$, $(4,0)$, and on $i\mathbb{H}_{\mathbb{B}}$, $(0,4)$. The **Krein** form is definite on the two complex subspaces, positive on the centre $(2,0)$ and negative on the vector subspace $(0,6)$. The passage from the Hermitian form to the Krein form moves the definite rows from the four real forms to the two complex subspaces; the passage to the two bilinear forms moves them to the pairs $(\mathbb{M}_{+},\mathbb{M}_{-})$ and $(\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}})$.

**Proposition (the maximal totally isotropic dimensions).** A real form of signature $(p,q)$ has maximal totally isotropic subspaces of dimension $\min(p,q)$ (*Witt's Theorems*). Hence the maximal totally isotropic dimensions of the four realified forms are

$$
4\ \text{(general plain bilinear)},\qquad 4\ \text{(general quaternionic bilinear)},\qquad 0\ \text{(Hermitian)},\qquad 2\ \text{(Krein)}.
$$

*Proof.* The signatures are those of the theorem above, and $\min(4,4)=4$, $\min(4,4)=4$, $\min(8,0)=0$ and $\min(2,6)=2$. Isotropic subspaces of those dimensions are exhibited by $\operatorname{span}_{\mathbb{R}}\{e_{\mu}+ie_{\mu}\}_{\mu=0}^{3}$ for the general quaternionic bilinear form, $\operatorname{span}_{\mathbb{R}}\{e_{0}+ie_{0},e_{1}+ie_{1},e_{2}+ie_{2},e_{3}+ie_{3}\}$ for the general plain bilinear form, and the plane $\operatorname{span}_{\mathbb{R}}\{e_{0}+e_{1},ie_{0}+ie_{1}\}$ for the Krein form; the Hermitian form has no nonzero isotropic vector.

## The Realified Null Cones

**Theorem (the four null sets).** With $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu ie_\mu$, the null sets of the four realified forms are

| form | equation | null set | real dimension |
|---|---|---|---|
| general plain bilinear | $q_{0}^{2}-q_{1}^{2}-q_{2}^{2}-q_{3}^{2}-q_{0}'^{2}+q_{1}'^{2}+q_{2}'^{2}+q_{3}'^{2}=0$ | hypersurface | $7$ |
| general quaternionic bilinear | $\sum_{\mu}\bigl(q_{\mu}^{2}-q_{\mu}'^{2}\bigr)=0$ | hypersurface | $7$ |
| Hermitian | $\sum_{\mu}\bigl(q_{\mu}^{2}+q_{\mu}'^{2}\bigr)=0$ | $\{0\}$ | — |
| Krein | $q_{0}^{2}+q_{0}'^{2}-\sum_{k=1}^{3}\bigl(q_{k}^{2}+q_{k}'^{2}\bigr)=0$ | hypersurface | $7$ |

*Proof.* The equations are the diagonals of the Gram matrices, that is the restricted quadratic forms read on $\tilde Q=\tilde P$. The Hermitian diagonal is a sum of squares, hence vanishes only at the origin. Each of the other three diagonals is a nonconstant homogeneous polynomial of degree two with nonzero gradient away from the origin, so its zero set is a real hypersurface of $\mathbb{R}^{8}$, of real dimension $7$, non-singular off the apex.

**Proposition (the realified cone and the complex cone).** Let $\Phi$ be one of the two general plain bilinear forms. Its **complex** null cone is

$$
\{\Phi(\tilde Q,\tilde Q)=0\}=\{\mathrm{Re}\,\Phi(\tilde Q,\tilde Q)=0\}\cap\{\mathrm{Im}\,\Phi(\tilde Q,\tilde Q)=0\},
$$

a complex cone of real dimension $6$, and it sits inside the **realified** cone $\{\mathrm{Re}\,\Phi(\tilde Q,\tilde Q)=0\}$, a real hypersurface of dimension $7$, as a real codimension-one subcone:

$$
\{\mathrm{Re}=0\}\cap\{\mathrm{Im}=0\}\ \subsetneq\ \{\mathrm{Re}=0\}.
$$

*Proof.* The identity is the definition of the complex null cone as the common zero set of the real and the imaginary parts. The two real equations are independent at a generic null point, so the common zero set has real codimension two and real dimension $6$, while the single equation $\{\mathrm{Re}=0\}$ has real codimension one and real dimension $7$; the inclusion is strict because a realified null vector with nonzero imaginary part lies in the larger set and not in the smaller.

**Remark (the realified cone and the complex cone are different objects).** The complex null cone of the general plain bilinear form is the quadric of *The Four Pairings of the Biquaternion Algebra*, and the complex null cone of the general quaternionic bilinear form is the null cone of *The Isotropic Structure of the General Quaternionic Algebra*; the realified cones tabulated above are the objects of this group, and they must not be called the null cones of the complex forms. The distinction between the realified cone and the complex cone is a feature of the two **bilinear** forms: it needs the imaginary part to be independent of the real part, which happens because a symmetric bilinear form has a complex diagonal. The two **sesquilinear** forms are Hermitian, so their diagonals are real-valued, and there the realified null set is the null set; in particular the Krein form, whose diagonal is $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$, has the real null set of real dimension $7$ described in *The Isotropic Structure of the General Quaternionic Sesqualgebra*, with no separate complex cone.

## Worked Examples

**A null vector of each indefinite realified form.** For the general plain bilinear realification the element $e_{1}+ie_{2}$ is null, since $-1+i^{2}(-1)=-1+1=0$; for the general quaternionic bilinear realification $e_{0}+ie_{0}$ is null, since $1-1=0$; for the Krein realification $e_{0}+e_{1}$ is null, since $1-1=0$. For the Hermitian realification no nonzero element is null, the diagonal being a sum of squares.

**A maximal totally isotropic subspace of each bilinear realification.** For the general quaternionic bilinear form the four vectors $e_{\mu}+ie_{\mu}$, $\mu=0,1,2,3$, span a totally isotropic real four-plane: each has square $1-1=0$ and distinct pairs are orthogonal. For the general plain bilinear form the four vectors $e_{0}+ie_{0}$, $e_{1}+ie_{1}$, $e_{2}+ie_{2}$, $e_{3}+ie_{3}$ also span a totally isotropic real four-plane, because the positive directions $e_{0},ie_{1},ie_{2},ie_{3}$ of $\operatorname{diag}(\mathrm{D},-\mathrm{D})$ may be paired with the negative directions $ie_{0},e_{1},e_{2},e_{3}$.

**A maximally isotropic plane of the Krein form.** The vectors $e_{0}+e_{1}$ and $ie_{0}+ie_{1}$ are null and Krein-orthogonal, so they span a totally isotropic real two-plane; it is maximal, since $\min(2,6)=2$.

**The three indefinite cones are pairwise distinct.** The element $e_{0}+e_{1}$ is null for the general plain bilinear and the Krein realifications but not for the general quaternionic bilinear one ($1-1=0$ against $1+1=2$); the element $e_{1}+ie_{2}$ is null for the general plain bilinear and the general quaternionic bilinear realifications but not for the Krein one ($-1+1=0$ against $-1-1=-2$). The two witnesses separate every pair of the three indefinite cones, so the general plain bilinear, general quaternionic bilinear and Krein cones are three different cones of $\mathbb{R}^{8}$ although three of them have the same dimension $7$, and the Hermitian cone is the single point $\{0\}$.

## Summary

The realification of the four complex forms of the biquaternion algebra is the family of real symmetric bilinear forms on $\mathbb{B}=\mathbb{R}^{8}$ obtained by taking real parts: the general plain bilinear form with Gram matrix $\operatorname{diag}(\mathrm{D},-\mathrm{D})$ and signature $(4,4)$, the general quaternionic bilinear form with $\operatorname{diag}(\mathrm{I}_{4},-\mathrm{I}_{4})$ and signature $(4,4)$, the Hermitian form with $\mathrm{I}_{8}$ and signature $(8,0)$, and the Krein form with $\operatorname{diag}(\varepsilon,\varepsilon)$ and signature $(2,6)$. The four signatures $(4,4),(4,4),(8,0),(2,6)$ are stated here once and quoted elsewhere. The realified form is not the complex form: the realification drops the imaginary part, the central scalar $J$ reverses the two bilinear forms and preserves the two sesquilinear ones, and for the two bilinear forms the realified null cone, a hypersurface of dimension $7$, strictly contains the complex null cone of dimension $6$, while for the two Hermitian forms the null set is one real equation. Restricted to the remarkable real subspaces — centre, vector, quaternion, anti-quaternion, Hermitian, anti-Hermitian — the four forms give the four signature tables above, with the definite rows on the Hermitian and anti-Hermitian subspaces for the general plain bilinear form, on the quaternion and anti-quaternion subspaces for the general quaternionic bilinear form, always for the Hermitian form, and on the centre and the vector subspace for the Krein form; the maximal totally isotropic dimensions are $4,4,0,2$ in the same order. The trace form $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$ of the real algebra is developed in the companion article and is $8$ times the realified general plain bilinear form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_{0},e_{1},e_{2},e_{3},ie_{0},ie_{1},ie_{2},ie_{3}$ | the real basis of $\mathbb{B}\cong\mathbb{R}^{8}$ |
| $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu ie_\mu$ | the real coordinates $q_\mu,q'_\mu\in\mathbb{R}$ |
| $\varepsilon=(1,-1,-1,-1)$, $\mathrm{D}=\operatorname{diag}(1,-1,-1,-1)$ | the sign vector and sign matrix |
| $\operatorname{diag}(\mathrm{D},-\mathrm{D})$ | realified general plain bilinear form; signature $(4,4)$ |
| $\operatorname{diag}(\mathrm{I}_{4},-\mathrm{I}_{4})$ | realified general quaternionic bilinear form; signature $(4,4)$ |
| $\mathrm{I}_{8}$ | realified Hermitian form; signature $(8,0)$ |
| $\operatorname{diag}(\varepsilon,\varepsilon)$ | realified Krein form; signature $(2,6)$ |
| $(4,4),(4,4),(8,0),(2,6)$ | the four realified signatures, in the order bilinear, bilinear, Hermitian, Krein |
| $4,4,0,2$ | the maximal totally isotropic dimensions in the same order |
| $\{\mathrm{Re}=0\}\supsetneq\{\mathrm{Re}=0\}\cap\{\mathrm{Im}=0\}$ | the realified cone of dimension $7$ and the complex cone of dimension $6$ |
| $\lVert\tilde Q\rVert_{E}^{2}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the definite norm of the real reading |

## Further Reading

- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general products whose scalar parts are the four forms
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the first form in full and its complex null quadric
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`) and *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the complex readings of the two tables
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the fourth form, its fundamental decomposition and the restriction table of the Krein form
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the definite norm and the unit group treated in full
- *The Null Quadric and Its Projective Geometry* (`articles_maths/the-null-quadric-and-its-projective-geometry.md`), for the projective geometry of the null cone in the same ambient space, and *The Topology of the Zero-Divisor Cone* (`articles_maths/the-topology-of-the-zero-divisor-cone.md`) for the cone itself
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the unit group
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, the invertibility criterion, the group of units, the definite form that supplies the definite structure and the inner product
- *Biquaternions as a Vector Space over $\mathbb{R}$* (`articles_maths/biquaternions-as-a-vector-space-over-r.md`) and *The Change of Scalars from $\mathbb{C}$ to $\mathbb{R}$* (`articles_maths/the-change-of-scalars-from-c-to-r.md`), for the real basis and the passage between the two scalar systems
- *Bilinear Forms* (`articles_maths/bilinear-forms.md`), *Quadratic Forms and Polarisation* (`articles_maths/quadratic-forms-and-polarisation.md`) and *Witt's Theorems* (`articles_maths/witts-theorems.md`), for Gram matrices, inertia, Sylvester's law and the totally isotropic dimensions
- *Normed Division Algebras and the Hurwitz Theorem* (`articles_maths/normed-division-algebras-and-the-hurwitz-theorem.md`), *The Low-Dimensional Classification* (`articles_maths/the-low-dimensional-classification.md`) and *Bott Periodicity and the Classification* (`articles_maths/bott-periodicity-and-the-classification.md`), for the normed division algebras and the real classification behind the signature table
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for bilinear forms, their Gram matrices, their inertia and their automorphism groups.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the real forms and the signature conventions.
