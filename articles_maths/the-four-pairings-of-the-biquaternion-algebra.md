# __The Four Pairings of the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries not one but four distinguished pairings of its elements, one for each of the four products of *The Four Biquaternion Complex Products*: the scalar part of each product is a pairing of the pair. The whole topology region of this category is built on them: the complex bilinear form, the quaternion bilinear form, the complex sesquilinear form and the quaternion sesquilinear form.

The four pairings are written

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q),
$$
$$
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*}),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*}),
$$

the plain product, the product with the natural conjugation on the first argument, the product with the Hermitian conjugation on the second, and the product with both. This article sets them side by side: their conjugation, their linearity, their symmetry, their Gram matrix in the coefficient basis, their signature and the isometry group each one defines. The comparison is the natural entry into the category, because it shows exactly what each pairing shares with the other three and where it differs.

The four conjugations of the algebra generate the Klein four-group $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$; they index the four pairings, the identity and the natural conjugation on the first argument and the identity and the Hermitian conjugation on the second. The fifth involution, the reversal $\flat=-{}^{*}$, gives the negative of the complex sesquilinear form and is the only other pairing the four conjugations produce.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}\in\mathbb{C}$, units $e_0=1$ and $e_k^{2}=-e_0$, central scalar imaginary $i$, and $\mathrm{Sc}$ the scalar part. The sign vector is $\varepsilon=(1,-1,-1,-1)$ and $\mathbb{B}$ is identified with $\mathbb{C}^{4}$ by $\tilde{Q}\mapsto(Q_0,Q_1,Q_2,Q_3)$.

## The Involution Group and the Four Pairings

**Definition.** An **involution** of $\mathbb{B}$ is a $\mathbb{R}$-linear map $\sigma$ with $\sigma^{2}=\mathrm{id}$. It is **linear** if $\sigma(\lambda\tilde{Q})=\lambda\sigma(\tilde{Q})$ for $\lambda\in\mathbb{C}$ and **antilinear** if $\sigma(\lambda\tilde{Q})=\bar\lambda\sigma(\tilde{Q})$; it is an **anti-automorphism** if $\sigma(\tilde{Q}\tilde{R})=\sigma(\tilde{R})\sigma(\tilde{Q})$.

**Theorem (the four conjugations).** $\mathbb{B}$ has four distinguished involutions:

| name | notation | formula | linearity | product |
|---|---|---|---|---|
| identity | $\mathrm{id}$ | $\tilde{Q}$ | linear | automorphism |
| natural conjugation | ${}^{\natural}$ | $\tilde{Q}^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$ | linear | anti-automorphism |
| complex conjugation | $\bar{\cdot}$ | $\bar{\tilde{Q}}=\bar Q_0e_0+\bar Q_1e_1+\bar Q_2e_2+\bar Q_3e_3$ | antilinear | automorphism |
| Hermitian conjugation | ${}^{*}$ | $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$ | antilinear | anti-automorphism |
| reversal | $\flat$ | $\tilde{Q}^{\flat}=-\tilde{Q}^{*}$ | antilinear | anti-automorphism up to sign |

They satisfy ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ and $\flat=-{}^{*}$, and $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ is the Klein four-group of pairwise commuting involutions.

**Proof.** These are the definitions and composition rules of *The Group of Involutions*, where the four conjugations, their real coordinates and the two composition rules are recorded.

**Definition (the four pairings).** The four pairings are the scalar parts

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q),
$$
$$
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*}),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*}),
$$

each being the scalar part of one of the four products of *The Four Biquaternion Complex Products*. The table records which conjugation enters each product and which argument carries it.

| pairing | product | first argument | second argument | scalar part |
|---|---|---|---|---|
| $\langle\cdot,\cdot\rangle$ | $\tilde P\tilde Q$ | as it stands | as it stands | $\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ |
| $\langle\cdot,\cdot\rangle_{\natural}$ | $\tilde P^{\natural}\tilde Q$ | ${}^{\natural}$ | as it stands | $\sum_\mu P_\mu Q_\mu$ |
| $\langle\cdot,\cdot\rangle_{*}$ | $\tilde P\tilde Q^{*}$ | as it stands | ${}^{*}$ | $\sum_\mu P_\mu\overline{Q_\mu}$ |
| $\langle\cdot,\cdot\rangle_{\natural*}$ | $\tilde P^{\natural}\tilde Q^{*}$ | ${}^{\natural}$ | ${}^{*}$ | $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ |

**Proposition (standard properties of the pairings).** Each pairing is $\mathbb{R}$-bilinear, is $\mathbb{C}$-linear in the second argument, and is $\mathbb{C}$-linear in the first exactly for the two bilinear pairings. Its Gram matrix in the basis $e_{\mu}$ is diagonal,
$$
G_{\mu\nu}=\langle e_\mu,e_\nu\rangle\,\delta_{\mu\nu},
\qquad
G=\mathrm{E},\ \mathrm{I}_4,\ \mathrm{I}_4,\ \mathrm{E},
$$
for the four pairings in order, with $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$.

**Proof.** $\mathbb{R}$-bilinearity is immediate. In the first argument, the natural conjugation is $\mathbb{C}$-linear, so the first two pairings carry a complex scalar out without conjugating it, while the star conjugates it, so the last two are conjugate-linear there. The Gram matrices follow from $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$; the entries are $\varepsilon_\mu$ for the first and the fourth pairing and $1$ for the second and the third. $\square$

## The Four Pairings

**Theorem (the four pairings and their diagonals).** The four pairings and their diagonal values are

$$
\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2},
\qquad
\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2},
$$
$$
\langle\tilde Q,\tilde Q\rangle_{*}=\lVert\tilde Q\rVert_E^{2}=\sum_\mu\lvert Q_\mu\rvert^{2},
\qquad
\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}.
$$

**Proof.** Substituting the four products and using $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ gives each identity; the diagonal values follow. The diagonal of the second is the biquaternion norm of *Biquaternion Norm and Invertibility*, and the diagonal of the third is the Euclidean square of the coefficient space. $\square$

**Proposition (the four Gram matrices).** In the coefficient basis the Gram matrices are

$$
G_{\langle\cdot,\cdot\rangle}=\mathrm{E},\qquad
G_{\langle\cdot,\cdot\rangle_{\natural}}=\mathrm{I}_4,\qquad
G_{\langle\cdot,\cdot\rangle_{*}}=\mathrm{I}_4,\qquad
G_{\langle\cdot,\cdot\rangle_{\natural*}}=\mathrm{E}.
$$

**Proof.** The Gram entries are the diagonal values evaluated on the units, which is the theorem above. $\square$

**Corollary (non-degeneracy and mutual distinction).** The four pairings are non-degenerate, and no two of them agree.

**Proof.** The Gram matrices $\mathrm{E}$ and $\mathrm{I}_4$ are invertible, so each pairing is non-degenerate. For the distinction, the four diagonal forms $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\sum_\mu Q_\mu^{2}$, $\sum_\mu\lvert Q_\mu\rvert^{2}$ and $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ separate on the units: $\langle e_1,e_1\rangle=-1$ while $\langle e_1,e_1\rangle_{\natural}=1=\langle e_1,e_1\rangle_{*}$ while $\langle e_1,e_1\rangle_{\natural*}=-1$, and the first two separate at $e_1+ie_2$. $\square$

**Remark (the relations among the four).** Any two of the four are recovered from the others by the natural and the complex conjugations of the arguments:

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P^{\natural},\tilde Q\rangle,
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,\bar{\tilde Q}\rangle_{\natural},
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,\bar{\tilde Q}\rangle=\langle\tilde P^{\natural},\tilde Q\rangle_{*},
$$

each identity being a rearrangement of the conjugations entering the four products. The natural conjugation $J={}^{\natural}$ preserves all four pairings, $\langle J\tilde P,J\tilde Q\rangle=\langle\tilde P,\tilde Q\rangle$ and likewise for the other three, so $J$ is an isometry of each; it is the *fundamental symmetry* of *The Fundamental Symmetry of the Biquaternion Algebra*.

**Proof.** Each identity is checked coefficientwise, and the invariance of $J$ is $\varepsilon_\mu^{2}=1$ in the bilinear cases and $\lvert\varepsilon_\mu\rvert^{2}=1$ in the sesquilinear cases. $\square$

## The Forms in Comparison

The four forms are collected in one table; each entry is defined before it is used, and the signatures are those of the underlying real quadratic or complex sesquilinear form.

| form | conjugation | in the first argument | symmetry | Gram matrix | signature over $\mathbb{R}$ | diagonal object |
|---|---|---|---|---|---|---|
| $\langle\cdot,\cdot\rangle$ complex bilinear | none | $\mathbb{C}$-linear | symmetric, $\mathbb{C}$-bilinear | $\mathrm{E}$ | $(4,4)$ | $\sum_\mu\varepsilon_\mu Q_\mu^{2}$ |
| $\langle\cdot,\cdot\rangle_{\natural}$ quaternion bilinear | ${}^{\natural}$ | $\mathbb{C}$-linear | symmetric, $\mathbb{C}$-bilinear | $\mathrm{I}_4$ | $(4,4)$ | the norm $\sum_\mu Q_\mu^{2}$ |
| $\langle\cdot,\cdot\rangle_{*}$ complex sesquilinear | ${}^{*}$ | conjugate-linear | Hermitian, positive definite | $\mathrm{I}_4$ | $(8,0)$ | $\lVert\tilde Q\rVert_E^{2}$ |
| $\langle\cdot,\cdot\rangle_{\natural*}$ quaternion sesquilinear | ${}^{\natural}\circ\bar{\cdot}$ | conjugate-linear | Hermitian, indefinite | $\mathrm{E}$ | $(2,6)$ | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ |

The two bilinear forms are complex-valued; their real parts have signature $(4,4)$ on the eight real coordinates. The complex sesquilinear form is positive definite and the quaternion sesquilinear form is indefinite, of signature $(2,6)$.

**Theorem (the four isometry groups).** The $\mathbb{C}$-linear operators preserving each form are, in the coefficient basis,

$$
\mathrm{Isom}\bigl(\langle\cdot,\cdot\rangle\bigr)=\{T:T^{\mathsf T}\mathrm{E}T=\mathrm{E}\}=O_4(\mathbb{C}),
\qquad
\mathrm{Isom}\bigl(\langle\cdot,\cdot\rangle_{\natural}\bigr)=\{T:T^{\mathsf T}T=\mathrm{I}_4\}=O_4(\mathbb{C}),
$$
$$
\mathrm{Isom}\bigl(\langle\cdot,\cdot\rangle_{*}\bigr)=\{T:T^{*}T=\mathrm{I}_4\}=U(4),
\qquad
\mathrm{Isom}\bigl(\langle\cdot,\cdot\rangle_{\natural*}\bigr)=\{T:T^{*}\mathrm{E}T=\mathrm{E}\}=U(1,3),
$$

with real dimensions $12$, $12$, $16$ and $16$. The two complex orthogonal groups are non-compact and complex, the unitary group is compact, and the indefinite unitary group is the non-compact real form of $GL_4(\mathbb{C})$ attached to the sign matrix.

**Proof.** A pairing with Gram matrix $G$ is preserved by a $\mathbb{C}$-linear $T$ exactly when $T^{\mathsf T}GT=G$ in the bilinear case and $T^{*}GT=G$ in the Hermitian case, where $T^{\mathsf T}$ is the transpose and $T^{*}$ the conjugate transpose. With $G=\mathrm{I}_4$ or $\mathrm{E}$ this gives the four groups. The dimensions are the classical ones: $\dim_{\mathbb{R}}O_4(\mathbb{C})=2\cdot6=12$, $\dim_{\mathbb{R}}U(4)=16$, $\dim_{\mathbb{R}}U(1,3)=16$. $\square$

**Remark (the adjoints of the left multiplications).** The four pairings give four adjoints to left multiplication, and the identity conjugation is the only one that changes the side:

$$
(L_{\tilde Q})^{\langle\cdot,\cdot\rangle}=R_{\tilde Q},
\qquad
(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural}}=L_{\tilde Q^{\natural}},
\qquad
(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{*}}=L_{\tilde Q^{*}},
\qquad
(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural*}}=R_{\bar{\tilde Q}}.
$$

The transpose $R_{\tilde Q}$ belongs to the complex bilinear form, the two anti-automorphic conjugations ${}^{\natural}$ and ${}^{*}$ keep left multiplication on the left, and the automorphic conjugation $\bar{\cdot}$ moves it to the right — the dichotomy that organises *Association and the Transpose on the Biquaternion Algebra* and *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*.

**Proof.** Each identity is checked on the units and extended by $\mathbb{R}$-linearity; equivalently, each is $\mathrm{Sc}$-cyclicity applied to the product. $\square$

## Worked Examples

**The units.** $\langle e_0,e_0\rangle=\langle e_0,e_0\rangle_{\natural}=\langle e_0,e_0\rangle_{*}=\langle e_0,e_0\rangle_{\natural*}=1$: the identity is positive for all four pairings.

**The vector units.** $\langle e_1,e_1\rangle=-1$ and $\langle e_1,e_1\rangle_{\natural}=1$ while $\langle e_1,e_1\rangle_{*}=1$ and $\langle e_1,e_1\rangle_{\natural*}=-1$: the vector direction is negative for the complex bilinear and the quaternion sesquilinear pairings and positive for the quaternion bilinear and the complex sesquilinear ones. This single contrast is the origin of the sign matrix $\mathrm{E}$.

**A null element.** $\tilde Q=e_1+ie_2$: $\langle\tilde Q,\tilde Q\rangle_{\natural}=1+i^{2}=0$, so it is null for the quaternion bilinear pairing and a zero divisor, while $\langle\tilde Q,\tilde Q\rangle=-2$, $\langle\tilde Q,\tilde Q\rangle_{*}=2$ and $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-2$: null for one pairing and not for the others.

**An isotropic element for the quaternion sesquilinear pairing only.** $\tilde Q=e_0+e_1$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1-1=0$, while $\langle\tilde Q,\tilde Q\rangle_{\natural}=2$ and $\langle\tilde Q,\tilde Q\rangle_{*}=2$.

**A zero divisor that is positive for the complex sesquilinear pairing.** $\tilde Q=e_0+ie_1$: $\langle\tilde Q,\tilde Q\rangle_{\natural}=1+i^{2}=0$ at once with $\langle\tilde Q,\tilde Q\rangle_{*}=1+1=2$, while $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1+(-1)=0$: null for the quaternion bilinear and the quaternion sesquilinear pairings and positive for the complex sesquilinear one.

**An isometry of one form only.** A hyperbolic boost, $e_0\mapsto\cosh t\,e_0+\sinh t\,e_1$ and $e_1\mapsto\sinh t\,e_0+\cosh t\,e_1$ with $e_2,e_3$ fixed, preserves the quaternion sesquilinear form and not the other three: it is in $U(1,3)$ and in no unitary group of the definite form (*The Krein Isometry Group and Its $J$-Contractions*).

## Summary

The biquaternion algebra carries four pairings, the scalar parts of the four products of *The Four Biquaternion Complex Products*. In the author's convention $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$, $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_\mu P_\mu Q_\mu$, $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$. Their Gram matrices are $\mathrm{E}$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$, and their signatures over $\mathbb{R}$ are $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$. The four forms determine one another by $\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P^{\natural},\tilde Q\rangle$, $\langle\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,\bar{\tilde Q}\rangle_{\natural}$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,\bar{\tilde Q}\rangle$, and the natural conjugation $J={}^{\natural}$ is an isometry of all four. The adjoint of a left multiplication is a left multiplication for the two anti-automorphic involutions and a right multiplication for the identity and the automorphic conjugation, so $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle}=R_{\tilde Q}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural}}=L_{\tilde Q^{\natural}}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{*}}=L_{\tilde Q^{*}}$ and $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural*}}=R_{\bar{\tilde Q}}$. The isometry groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $U(4)$ and $U(1,3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the complex bilinear form, the scalar part of $\tilde P\tilde Q$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$ | the quaternion bilinear form; $\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ |
| $\langle\tilde P,\tilde Q\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu}$ | the complex sesquilinear form; $\langle\tilde Q,\tilde Q\rangle_{*}=\lVert\tilde Q\rVert_E^{2}$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the quaternion sesquilinear form |
| $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ | the sign matrix, the Gram matrix of the first and the fourth pairings |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the four signatures over $\mathbb{R}$ |
| $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle}=R_{\tilde Q}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural}}=L_{\tilde Q^{\natural}}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{*}}=L_{\tilde Q^{*}}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural*}}=R_{\bar{\tilde Q}}$ | the four adjoints |
| $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $U(4)$, $U(1,3)$ | the four isometry groups |

## Further Reading

- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations and their group
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the four products whose scalar parts are the four pairings
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the first pairing in full
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the quaternion bilinear form and the norm
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the complex sesquilinear form and its inner product
- *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the quaternion sesquilinear form and its signature
- *The Gram Matrices of the Four Forms* (`articles_maths/the-gram-matrices-of-the-four-forms.md`), for the four Gram matrices in one place
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the same four forms in the $2\times2$ matrix model
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the transpose that belongs to the complex bilinear pairing
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for bilinear and sesquilinear forms, their Gram matrices and their isometry groups
