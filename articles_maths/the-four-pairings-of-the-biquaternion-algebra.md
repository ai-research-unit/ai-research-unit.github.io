# __The Four Pairings of the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries not one but four distinguished pairings of its elements, one for each of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*: the scalar part of each product is a pairing of the pair. They are the four degree-2 forms of the algebra: the general plain bilinear form, the general quaternionic bilinear form, the general plain sesquilinear form and the general quaternionic sesquilinear form.

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

the plain product, the product with the natural conjugation on the first argument, the product with the Hermitian conjugation on the second, and the product with both. This article sets them side by side: their conjugation, their linearity, their symmetry, their Gram matrix in the coefficient basis, their signature and the automorphism group each one defines. The comparison is the natural entry into the category, because it shows exactly what each pairing shares with the other three and where it differs. Their null sets, their value-one sets and their restrictions to the remarkable real subspaces belong to the comparison too, since those are the objects the four layers differ in most visibly; the subspace comparison is §*Remarkable Subspaces in Comparison* and §*The Two Readings*.

The four conjugations of the algebra generate the Klein four-group $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$; they index the four pairings, the identity and the natural conjugation on the first argument and the identity and the Hermitian conjugation on the second. The fifth involution, the reversal $\flat=-{}^{*}$, gives the negative of the general plain sesquilinear form and is the only other pairing the four conjugations produce.

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

each being the scalar part of one of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. The table records which conjugation enters each product and which argument carries it.

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

**Proof.** Substituting the four general products and using $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ gives each identity; the diagonal values follow. The diagonal of the second is the biquaternion norm of *Biquaternion Norm and Invertibility*, and the diagonal of the third is the Euclidean square of the coefficient space. $\square$

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

each identity being a rearrangement of the conjugations entering the four general products. The natural conjugation $J={}^{\natural}$ preserves all four pairings, $\langle J\tilde P,J\tilde Q\rangle=\langle\tilde P,\tilde Q\rangle$ and likewise for the other three, so $J$ is an automorphism of each; it is the *fundamental symmetry* of *The Fundamental Symmetry of the Biquaternion Algebra*.

**Proof.** Each identity is checked coefficientwise, and the invariance of $J$ is $\varepsilon_\mu^{2}=1$ in the bilinear cases and $\lvert\varepsilon_\mu\rvert^{2}=1$ in the sesquilinear cases. $\square$

## The Forms in Comparison

The four forms are collected in one table; each entry is defined before it is used, and the signatures are those of the underlying real quadratic or general plain sesquilinear form.

| form | conjugation | in the first argument | symmetry | Gram matrix | signature over $\mathbb{R}$ | diagonal object |
|---|---|---|---|---|---|---|
| $\langle\cdot,\cdot\rangle$ general plain bilinear | none | $\mathbb{C}$-linear | symmetric, $\mathbb{C}$-bilinear | $\mathrm{E}$ | $(4,4)$ | $\sum_\mu\varepsilon_\mu Q_\mu^{2}$ |
| $\langle\cdot,\cdot\rangle_{\natural}$ general quaternionic bilinear | ${}^{\natural}$ | $\mathbb{C}$-linear | symmetric, $\mathbb{C}$-bilinear | $\mathrm{I}_4$ | $(4,4)$ | the norm $\sum_\mu Q_\mu^{2}$ |
| $\langle\cdot,\cdot\rangle_{*}$ general plain sesquilinear | ${}^{*}$ | conjugate-linear | Hermitian, positive definite | $\mathrm{I}_4$ | $(8,0)$ | $\lVert\tilde Q\rVert_E^{2}$ |
| $\langle\cdot,\cdot\rangle_{\natural*}$ general quaternionic sesquilinear | ${}^{\natural}\circ\bar{\cdot}$ | conjugate-linear | Hermitian, indefinite | $\mathrm{E}$ | $(2,6)$ | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ |

The two bilinear forms are complex-valued; their real parts have signature $(4,4)$ on the eight real coordinates. The general plain sesquilinear form is positive definite and the general quaternionic sesquilinear form is indefinite, of signature $(2,6)$.

The four prefixes of the table name the conjugation the form is built from, and they are not a signature and not a base field: *complex* marks a form in which no natural conjugation enters, *quaternion* one in which it enters in the first argument, *bilinear* marks a form linear in both arguments, *sesquilinear* one conjugate-linear in the second. Each is recovered from the others by the conjugations of the arguments (§*The Four Pairings*), so the prefixes organise the table without carrying metric content.

**Theorem (the four automorphism groups).** The $\mathbb{C}$-linear operators preserving each form are, in the coefficient basis,

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

with real dimensions $12$, $12$, $16$ and $16$. The two orthogonal groups are the complex groups of the symmetric pairing, the unitary group is the definite one, and the indefinite unitary group is the real form of $GL_4(\mathbb{C})$ attached to the sign matrix.

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

The transpose $R_{\tilde Q}$ belongs to the general plain bilinear form, the two anti-automorphic conjugations ${}^{\natural}$ and ${}^{*}$ keep left multiplication on the left, and the automorphic conjugation $\bar{\cdot}$ moves it to the right — the dichotomy that organises *Association and the Transpose on the Biquaternion Algebra* and *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*.

**Proof.** Each identity is checked on the units and extended by $\mathbb{R}$-linearity; equivalently, each is $\mathrm{Sc}$-cyclicity applied to the product. $\square$

## Remarkable Subspaces in Comparison

The comparison extends from the algebra to the remarkable real subspaces of *Introduction to the Remarkable Subspaces*, and the remarkable subspaces are where the four forms differ most visibly. Because all four are diagonal in the coefficient basis, each restriction is read off the real sign strings, and the signatures on the remarkable subspaces are

| subspace | $\dim_{\mathbb{R}}$ | $\langle\cdot,\cdot\rangle$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $\langle\cdot,\cdot\rangle_{*}$ | $\langle\cdot,\cdot\rangle_{\natural*}$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $(1,1)$ | $(1,1)$ | $(2,0)$ | $(2,0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $(3,3)$ | $(3,3)$ | $(6,0)$ | $(0,6)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_+$ | $4$ | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_-$ | $4$ | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |

Four features of the table are worth naming. The general plain sesquilinear form is **positive definite on every one of the remarkable subspaces**, so it distinguishes nothing among them. The general plain bilinear and the general quaternionic bilinear form **agree in signature on the centre and the vector subspace** and part company on the four four-dimensional subspaces, where the general plain bilinear form is indefinite and the general quaternionic bilinear form is definite or anti-definite. The general quaternionic sesquilinear form has the **same** signature $(1,3)$ on each of the four four-dimensional subspaces, which is the form statement of their common real dimension. And each of the two indefinite bilinear forms is **definite on exactly one pair** of the four-dimensional subspaces: the general quaternionic bilinear form is positive definite on $\mathbb{H}_{\mathbb{B}}$ and negative definite on $i\mathbb{H}_{\mathbb{B}}$, while the general plain bilinear form is positive definite on $\mathbb{M}_+$ and negative definite on $\mathbb{M}_-$.

The four diagonal values are read in the same way, and they locate each subspace in the four layers.

| subspace | element | $\langle\tilde Q,\tilde Q\rangle$ | $\langle\tilde Q,\tilde Q\rangle_{\natural}$ | $\langle\tilde Q,\tilde Q\rangle_{*}$ | $\langle\tilde Q,\tilde Q\rangle_{\natural*}$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q=Ae_0$, $A=q_0+iq'_0$ | $A^{2}$ | $A^{2}$ | $\lvert A\rvert^{2}$ | $\lvert A\rvert^{2}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q=\mathbf{P}=\sum_kP_ke_k$ | $-\sum_kP_k^{2}$ | $\sum_kP_k^{2}$ | $\sum_k\lvert P_k\rvert^{2}$ | $-\sum_k\lvert P_k\rvert^{2}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde Q=h=\sum_\mu h_\mu e_\mu$, $h_\mu\in\mathbb{R}$ | $h_0^{2}-\sum_kh_k^{2}$ | $\sum_\mu h_\mu^{2}$ | $\sum_\mu h_\mu^{2}$ | $h_0^{2}-\sum_kh_k^{2}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\tilde Q=ih$ | $-h_0^{2}+\sum_kh_k^{2}$ | $-\sum_\mu h_\mu^{2}$ | $\sum_\mu h_\mu^{2}$ | $h_0^{2}-\sum_kh_k^{2}$ |
| $\mathbb{M}_+$ | $\tilde Q=a_0e_0+i\mathbf{p}$, $a_0\in\mathbb{R}$ | $a_0^{2}+(\mathbf{p},\mathbf{p})$ | $a_0^{2}-(\mathbf{p},\mathbf{p})$ | $a_0^{2}+(\mathbf{p},\mathbf{p})$ | $a_0^{2}-(\mathbf{p},\mathbf{p})$ |
| $\mathbb{M}_-$ | $\tilde Q=ib_0e_0+\mathbf{q}$, $b_0\in\mathbb{R}$ | $-b_0^{2}-(\mathbf{q},\mathbf{q})$ | $-b_0^{2}+(\mathbf{q},\mathbf{q})$ | $b_0^{2}+(\mathbf{q},\mathbf{q})$ | $b_0^{2}-(\mathbf{q},\mathbf{q})$ |

The two bilinear forms are **complex-valued** on the centre and the vector subspace, and it is their real parts that carry the signatures $(1,1)$ and $(3,3)$; the two sesquilinear forms are positive definite there. On the four real subspaces all four forms are real-valued, and the identities of the table organise the layer: on the quaternion and anti-quaternion subspaces the general plain sesquilinear form, the general quaternionic bilinear form and the general quaternionic sesquilinear form pair off against the general plain bilinear form; on the two Hermitian subspaces the general quaternionic sesquilinear form is the general quaternionic bilinear form up to the sign $+$ on $\mathbb{M}_+$ and $-$ on $\mathbb{M}_-$, while the general plain bilinear form is definite with the opposite signs on the two. The two exchanges, "$i$ swaps the definite rows of the norm" and "$i$ swaps the definite rows of the general plain bilinear form", are the two readings of one substitution, and the remarkable subspaces are the fixed points of the four conjugations that generate them.

The null sets are read from the same diagonals. On the centre all four vanish only at $0$. On the vector subspace the complex and the general quaternionic bilinear forms share the **complex null cone** $\sum_kP_k^{2}=0$ – the cone whose projective geometry is *The Null Quadric and Its Projective Geometry* – while both sesquilinear forms are definite there and vanish only at $0$. On the quaternion and anti-quaternion subspaces the general plain bilinear form and the general quaternionic sesquilinear form share the **real cone** $h_0^{2}=h_1^{2}+h_2^{2}+h_3^{2}$, while the general quaternionic bilinear form is definite there. On the two Hermitian subspaces the general quaternionic bilinear form and the general quaternionic sesquilinear form coincide up to sign and share the same cone, $a_0^{2}=(\mathbf{p},\mathbf{p})$ on $\mathbb{M}_+$ and $b_0^{2}=(\mathbf{q},\mathbf{q})$ on $\mathbb{M}_-$, while the general plain bilinear form is definite there.

**Proposition (the two complex cones of the vector subspace).** On the vector subspace the general plain bilinear and the general quaternionic bilinear forms share the complex cone $\sum_kP_k^{2}=0$: an element lies on both $\sum_\mu Q_\mu^{2}=0$ and $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$ only when $Q_0=0$ and $\sum_kQ_k^{2}=0$.

*Proof.* Adding the two equations gives $2Q_0^{2}=0$, so $Q_0=0$, and either equation then gives $\sum_kQ_k^{2}=0$. $\square$

The three cones are separated by explicit elements: $e_1+ie_2$ lies on both general plain bilinear cones, $e_0+ie_1$ on the $\natural$-cone alone, and $e_0+e_1$ on the general plain bilinear cone alone.

The **orthogonal pairs** are the same for all four forms: because each form is diagonal in the coefficient basis, two subspaces are orthogonal exactly when their coefficient supports are disjoint, the supports are $\{0\}$ for the centre, $\{1,2,3\}$ for the vector subspace and $\{0,1,2,3\}$ for the other four, and therefore **the centre and the vector subspace are orthogonal for all four pairings, and they are the only pair of the remarkable subspaces that is**. Every other pair shares a coefficient, and the corresponding entry of the pairing does not vanish identically; since each diagonal entry is nonzero, the decomposition is one of non-degenerate summands and the signatures add:

$$
(1,1)+(3,3)=(4,4),\qquad (1,1)+(3,3)=(4,4),\qquad (2,0)+(6,0)=(8,0),\qquad (2,0)+(0,6)=(2,6),
$$

the last being the fundamental decomposition of the Krein space of *The Krein Gram Matrix and the Restrictions of the Form*.

No **isotropic subspace beyond a line** lies inside a single one of the remarkable subspaces, since each restriction is non-degenerate. A complex line is totally isotropic for a bilinear form exactly when it is spanned by a null element; the two complex subspaces are the centre, of complex dimension $1$, and the vector subspace, of complex dimension $3$, and by non-degeneracy a totally isotropic complex subspace of a non-degenerate form on a complex space of dimension $d$ has dimension at most $d/2$, so at most $0$ in the centre and at most $1$ in the vector subspace; the four four-dimensional subspaces are **totally real**, in the sense that $i\tilde Q$ lies in none of them when $\tilde Q\ne0$ is in one, so they contain no complex subspace at all. Each of the vector subspace, the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace therefore contains isotropic lines for some of the forms and no isotropic plane, and the remaining restrictions are anisotropic. The isotropic lines of the general quaternionic bilinear form inside the remarkable subspaces are its zero-divisor lines, and the ideals it carries are *The Isotropic Structure of the General Quaternionic Algebra*, §*The Minimal Ideals and the Hyperbolic Peirce Basis*.

The restrictions themselves, subspace by subspace and form by form, are the subject of the five companion articles: *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*, *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*, *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* and *Remarkable Subspaces under the Real Biquaternion Algebra*, one for each reading group.

## The Two Readings

The remarkable subspaces are one set of subspaces carrying two form readings, and the comparison of the readings is the point of this section. The **algebra reading** is the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ of *Biquaternion Norm and Invertibility*, positive definite on all of $\mathbb{B}$; the **form reading** is the general quaternionic sesquilinear form $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ of *The Krein Gram Matrix and the Restrictions of the Form*, of signature $(2,6)$.

**Theorem (the comparison of the readings).** The general plain sesquilinear form restricts to every one of the remarkable subspaces as a positive definite form, of signature the real dimension of the subspace, because it is positive definite on all of $\mathbb{B}$. The general quaternionic sesquilinear form restricts to the same remarkable subspaces with the patterns of the table above: it is positive definite on the centre $(2,0)$, negative definite on the vector subspace $(0,6)$, and indefinite of signature $(1,3)$ on each of the quaternion subspace, the anti-quaternion subspace and the two sectors. A subspace definite for one form need not be definite for the other, and the two readings share the remarkable subspaces while they differ on four of them.

**Proof.** $\langle\tilde P,\tilde P\rangle_{*}=\sum_\mu|P_\mu|^{2}>0$ off zero, so the restriction to a real subspace is positive definite of signature its real dimension. The columns of the table above give the quaternion-sesquilinear patterns; the divergence is explicit on $\mathbb{H}_{\mathbb{B}}$, where $\langle e_1,e_1\rangle_{*}=1$ while $\langle e_1,e_1\rangle_{\natural*}=-1$. $\square$

**Remark (the two readings do not change the orthogonal pairs).** The remarkable subspaces have the same orthogonal pairs under every pairing, namely the centre with the vector subspace, as §*Remarkable Subspaces in Comparison* records; the reading is a change of form on one common set of subspaces, not a change of the lattice.

**Remark (where the four forms sit in the split of the products).** Each of the four forms is the scalar form of one of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, that is the scalar part of the product read as a value; and each is the **scalar part of the symmetric half** of that product taken under the exchange that keeps its class — the plain transposition for the two bilinear products, whose base involution is trivial, and the transposition followed by the coefficientwise conjugation for the two sesquilinear products — by the scalar theorem of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product* and its §*The Biquaternion Products*. For the plain sesquilinear product and $c=\overline{\cdot}$ the coincidence is exact and not only scalar: the conjugate-symmetric half is the central element
$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+(\tilde{P}\tilde{Q}^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})\,e_0=\bigl(P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr)e_0,
$$
which is the form $\langle\tilde{P},\tilde{Q}\rangle_{*}$ of the algebra reading above read in the centre. So the exchange that keeps the class is the one under which the form is a product: the symmetric half carries the form in its scalar part, and for the plain sesquilinear product the half is the form itself in the centre, while for a product whose value is not central the half is the form in its scalar part and carries a vector part as well. The four forms of this article are the four scalar parts, and the four scalar parts of the four general products are the four forms (*Relations Between the Four General Products*, §*The Four Scalar Parts*). The other reading of the four, under the plain exchange, is *The 12 Products of the Biquaternion Complex Space*.

## The Null Sets Compared

The forms share one space and one basis, and the comparison is not complete with the table of §*The Forms in Comparison*: the set on which each diagonal vanishes, and the value-one set each diagonal singles out, are also objects of the comparison, and they are the objects the four layers differ in. The definite form has no null element beyond the origin; the three indefinite ones have cones, of two different kinds.

**Definition.** The **null set** of a form $\Phi$ is the set $\{\tilde Q:\Phi(\tilde Q,\tilde Q)=0\}$.

**Theorem (the four null sets).** In the coefficient basis,

| form | null set |
|---|---|
| general plain bilinear $\langle\cdot,\cdot\rangle$ | $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$ |
| general quaternionic bilinear $\langle\cdot,\cdot\rangle_{\natural}$ | $\sum_\mu Q_\mu^{2}=0$ |
| general plain sesquilinear $\langle\cdot,\cdot\rangle_{*}$ | $\{0\}$ |
| general quaternionic sesquilinear $\langle\cdot,\cdot\rangle_{\natural*}$ | $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}=0$ |

The three indefinite null sets are cones; only the general plain sesquilinear form has no null element beyond the origin. The dimension and the shape of each cone are *The Euclidean Topology of the Biquaternion Algebra*, *The Krein Level Sets and the Hyperbolic Structure* and *The Topology of the Zero-Divisor Cone*.

**The quadric of the general plain bilinear form.** Its null set is the complex quadric $\mathcal{Q}=\{\tilde Q:\sum_\mu\varepsilon_\mu Q_\mu^{2}=0\}$, homogeneous of degree two: a complex cone with apex the origin, of real dimension $6$ in $\mathbb{R}^8$. It carries two families of **isotropic planes**, each of complex dimension $2$ and real dimension $4$, on which the form vanishes identically, for instance $W_{+}=\mathrm{span}_{\mathbb{C}}\{e_0+e_1,\;e_2+ie_3\}$ and $W_{-}=\mathrm{span}_{\mathbb{C}}\{e_0-e_1,\;e_2-ie_3\}$; the two families meet in the lines $\mathbb{C}(e_0\pm e_1)$. The maximal dimension of a totally isotropic subspace is $2$ over $\mathbb{C}$, that is $4$ over $\mathbb{R}$.

**Proposition (the form is an orthogonal sum of two hyperbolic planes).** The four elements
$$
h_1=e_0+e_1,\qquad h_2=\tfrac12(e_0-e_1),\qquad h_3=e_2+ie_3,\qquad h_4=\tfrac12(ie_3-e_2)
$$
are isotropic, the only non-zero pairings among them are $\langle h_1,h_2\rangle=1$ and $\langle h_3,h_4\rangle=1$, and the Gram matrix in this basis is $\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$. The form is therefore the orthogonal sum of the two hyperbolic planes $\mathrm{span}\{e_0,e_1\}$ and $\mathrm{span}\{e_2,e_3\}$, of index $1+1=2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$.

**Remark (the three elements that separate the two cones).** The quadric of the general plain bilinear form is not the zero-divisor cone: $e_1+ie_2$ lies on both, $e_0+e_1$ lies on the quadric and not on the zero-divisor cone, and $e_0+ie_1$ lies on the zero-divisor cone and not on the quadric, so neither cone contains the other.

**Theorem (the Krein null set and the norm cone).** The **Krein null set** $\mathcal{K}$, the null set of the general quaternionic sesquilinear form, and the **norm cone** $\mathcal{N}$, the null set of the general quaternionic bilinear form, are distinct: neither is contained in the other. Their intersection $\mathcal{K}\cap\mathcal{N}$ is the union of the **doubly null lines** $\mathbb{C}(e_0+i\hat\mu)$, $\hat\mu$ a real unit vector, a real algebraic cone; in particular it contains the two complex lines $\mathbb{C}(e_0\pm ie_1)$.

**Proof.** $e_0+e_1$ lies in $\mathcal{K}$ and not in $\mathcal{N}$, since $\langle e_0+e_1,e_0+e_1\rangle_{\natural*}=1-1=0$ while $\langle e_0+e_1,e_0+e_1\rangle_{\natural}=2$; $e_1+ie_2$ lies in $\mathcal{N}$ and not in $\mathcal{K}$, since $\langle e_1+ie_2,e_1+ie_2\rangle_{\natural}=1+i^{2}=0$ while $\langle e_1+ie_2,e_1+ie_2\rangle_{\natural*}=-2$. Neither inclusion holds. For the intersection, $\mathcal{K}\cap\mathcal{N}$ is invariant under complex scaling, so compute it in the affine chart $Q_0=1$: writing the vector part as $v=U+iW$ with $U,W$ real, the two conditions $\|v\|_E=1$ and $\langle v,v\rangle_{\natural}=-1$ read

$$
\|U\|_E^{2}+\|W\|_E^{2}=1,\qquad
\|U\|_E^{2}-\|W\|_E^{2}=-1,\qquad
\langle U,W\rangle=0,
$$

which force $U=0$ and $W=\hat\mu$ a real unit vector. The chart therefore meets the intersection in the copy $\{1\}\times iS^{2}$ of $S^{2}$: the intersection is the union of the doubly null lines $\mathbb{C}(e_0+i\hat\mu)$. The two lines of the statement are null for both forms, $\langle e_0\pm ie_1,e_0\pm ie_1\rangle_{\natural}=1+(i)^{2}=0$ and $\langle e_0\pm ie_1,e_0\pm ie_1\rangle_{\natural*}=1-1=0$. The doubly null lines are also the **Peirce lines** $\mathbb{C}\tilde\Pi_{1,2}(\hat\mu)$ of the rank-one Hermitian idempotents $\tilde\Pi_{1,2}(\hat\mu)=\tfrac12(e_0\pm i\hat\mu)$, which is the description of *The Isotropic Structure of the General Quaternionic Sesqualgebra*, §*The Index in Two Ways*. $\square$

**Remark (the two cones agree on a real slice).** On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the general quaternionic sesquilinear form is the Krein form and the norm is the definite form, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=q_0^{2}-\sum_kq_k^{2}$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu}q_{\mu}^{2}$; the Krein null set is the light cone of the slice, the norm cone meets the real slice only at the origin, and the two agree nowhere except at $0$.

## The Value-One Sets Compared

Each form singles out the value-one set of its diagonal, and the three sign levels of the general quaternionic sesquilinear form are read in the splitting $\tilde Q=c+v$ of the algebra into its centre part $c\in\mathbb{C}_{\mathbb{B}}$ and its vector part $v\in\mathbb{V}_{\mathbb{B}}$: the **positive value-one set** $\{\langle\tilde Q,\tilde Q\rangle_{\natural*}=1\}$, the **negative value-one set** $\{\langle\tilde Q,\tilde Q\rangle_{\natural*}=-1\}$ and the **null set** $\{\langle\tilde Q,\tilde Q\rangle_{\natural*}=0\}$.

**Proposition (the value-one sets in the splitting).** With $\tilde Q=c+v$, $c\in\mathbb{C}_{\mathbb{B}}$, $v\in\mathbb{V}_{\mathbb{B}}$, the three levels are read by the identity $\langle\tilde Q,\tilde Q\rangle_{\natural*}=\|c\|_E^{2}-\|v\|_E^{2}$:

| value-one set | equation in $(c,v)$ |
|---|---|
| positive | $\|c\|_E^{2}=1+\|v\|_E^{2}$ |
| negative | $\|v\|_E^{2}=1+\|c\|_E^{2}$ |
| null | $\|c\|_E=\|v\|_E$ |

*Proof.* The centre and the vector subspace are $\varepsilon$-orthogonal, so the diagonal splits as the difference of the two squared norms, and each row is the rearrangement of the corresponding sign.

**The value-one set of the general plain bilinear form.** Its value-one set is
$$
\mathcal{L}=\Bigl\{\tilde Q:\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=1\Bigr\},
$$
the affine complex quadric of the same polynomial, of complex dimension $3$. The curve $\tilde Q(t)=\cosh t\,e_0+\sinh t\,e_1$ lies on $\mathcal{L}$ for every real $t$, since $\cosh^{2}t-\sinh^{2}t=1$. The set is not a group: $\langle\tilde Q(t),\tilde Q(t)\rangle=1$ while $\tilde Q(t)^{2}=e_0+\sinh2t\,e_1$, of diagonal value $1-\sinh^{2}2t$, which differs from $1$ for $t\neq0$, so $\mathcal{L}$ is not closed under the product. This separates it from the value-one set of the general quaternionic bilinear form, which is the norm-one group $G_1$ of *Biquaternion Norm and Invertibility*. Over $\mathbb{C}$ every non-degenerate quadratic form of rank $4$ is equivalent to every other, so $\mathcal{L}$ is the standard complex quadric.

## The Two Senses of Norm

The four pairings separate the two senses of the word *norm*, and the separation is why the algebra carries no single norm. The **algebraic norm** is the diagonal of the general quaternionic bilinear form,
$$
N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_{\mu=0}^{3}Q_\mu^{2}\in\mathbb{C},
$$
complex-valued and multiplicative; the **Hermitian norm** is the square root of the diagonal of the general plain sesquilinear form, $\lVert\tilde Q\rVert_E^{2}=\langle\tilde Q,\tilde Q\rangle_{*}$, real and definite. Multiplicativity belongs to the first and definiteness to the second, and no third function holds the two together.

**Proposition (no function is both definite and multiplicative).** There is no function on $\mathbb{B}$ that is both definite and multiplicative.

*Proof.* The algebra has zero divisors: for example
$$
(e_0+ie_1)(e_0-ie_1)=e_0-i^{2}e_1^{2}=e_0-(-1)(-1)e_0=0,
$$
with $e_0\pm ie_1\neq0$ and $N(e_0\pm ie_1)=1+i^{2}=0$. Suppose $\lVert\cdot\rVert$ were definite and multiplicative. Then $\lVert e_0+ie_1\rVert$ and $\lVert e_0-ie_1\rVert$ are nonzero, since the factors are nonzero, whereas
$$
\lVert e_0+ie_1\rVert\lVert e_0-ie_1\rVert=\lVert (e_0+ie_1)(e_0-ie_1)\rVert=\lVert 0\rVert=0,
$$
which is impossible in the real numbers. $\square$

**Corollary.** $N$ is multiplicative and not definite; the diagonal of the general plain sesquilinear form is definite and not multiplicative; and no third function repairs the split.

**Remark (the coincidence that fails here).** For $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and the octonions the multiplicative form is real and positive on the nonzero elements and equal to the square of the definite norm, so the two senses of *norm* are one function; by the Hurwitz theorem these four are the only normed division algebras (*Normed Division Algebras and the Hurwitz Theorem*). The biquaternions are excluded by their zero divisors, exactly as the proposition shows. The coincidence is recovered on the parts of $\mathbb{B}$ where $N$ does not vanish: on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where $N$ is real of signature $(4,0)$ and $N(\tilde Q)=\lVert\tilde Q\rVert^{2}$; on the imaginary translate $i\mathbb{H}_{\mathbb{B}}$, where $N$ is real of signature $(0,4)$ and $N(\tilde Q)=-\lVert\tilde Q\rVert^{2}$; and on the two sectors, where $N$ is indefinite and the norm and the interval differ by a sign on one of the two halves. It is the whole algebra, taken at once, that no single function norms. The two senses carry the two readings of the framework: restricted to the material sector the algebraic norm is the interval of signature $(3,1)$, whose zero set is the light cone, and the Hermitian norm is the length of the state space on the informational sector.

**Remark (the four degree-two functions).** Each of the four products carries its own quadratic diagonal, $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\sum_\mu Q_\mu^{2}$, $\sum_\mu\lvert Q_\mu\rvert^{2}$ and $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$, and the four rows of the table above separate them; only the second is multiplicative and only the third is definite. The algebraic norm, its polarisation, the two norms and the unit group are *Biquaternion Norm and Invertibility*, and the four products as one two-slot construction are *The Four General Products and Their Two Slots: the Two Algebras and the Two Sesqualgebras*.

## Worked Examples

**The units.** $\langle e_0,e_0\rangle=\langle e_0,e_0\rangle_{\natural}=\langle e_0,e_0\rangle_{*}=\langle e_0,e_0\rangle_{\natural*}=1$: the identity is positive for all four pairings.

**The vector units.** $\langle e_1,e_1\rangle=-1$ and $\langle e_1,e_1\rangle_{\natural}=1$ while $\langle e_1,e_1\rangle_{*}=1$ and $\langle e_1,e_1\rangle_{\natural*}=-1$: the vector direction is negative for the general plain bilinear and the general quaternionic sesquilinear pairings and positive for the general quaternionic bilinear and the general plain sesquilinear ones. This single contrast is the origin of the sign matrix $\mathrm{E}$.

**A null element.** $\tilde Q=e_1+ie_2$: $\langle\tilde Q,\tilde Q\rangle_{\natural}=1+i^{2}=0$, so it is null for the general quaternionic bilinear pairing and a zero divisor, while $\langle\tilde Q,\tilde Q\rangle=-2$, $\langle\tilde Q,\tilde Q\rangle_{*}=2$ and $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-2$: null for one pairing and not for the others.

**An isotropic element for the general quaternionic sesquilinear pairing only.** $\tilde Q=e_0+e_1$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1-1=0$, while $\langle\tilde Q,\tilde Q\rangle_{\natural}=2$ and $\langle\tilde Q,\tilde Q\rangle_{*}=2$.

**A zero divisor that is positive for the general plain sesquilinear pairing.** $\tilde Q=e_0+ie_1$: $\langle\tilde Q,\tilde Q\rangle_{\natural}=1+i^{2}=0$ at once with $\langle\tilde Q,\tilde Q\rangle_{*}=1+1=2$, while $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1+(-1)=0$: null for the general quaternionic bilinear and the general quaternionic sesquilinear pairings and positive for the general plain sesquilinear one.

**An automorphism of one form only.** A hyperbolic boost, $e_0\mapsto\cosh t\,e_0+\sinh t\,e_1$ and $e_1\mapsto\sinh t\,e_0+\cosh t\,e_1$ with $e_2,e_3$ fixed, preserves the general quaternionic sesquilinear form and not the other three: it is in $U(1,3)$ and in no unitary group of the definite form (*The Krein Isometry Group and Its $J$-Contractions*).

## Summary

The biquaternion algebra carries four pairings, the scalar parts of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. In the author's convention $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$, $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_\mu P_\mu Q_\mu$, $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$. Their Gram matrices are $\mathrm{E}$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$, and their signatures over $\mathbb{R}$ are $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$. The four forms determine one another by $\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P^{\natural},\tilde Q\rangle$, $\langle\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,\bar{\tilde Q}\rangle_{\natural}$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,\bar{\tilde Q}\rangle$, and the natural conjugation $J={}^{\natural}$ is an automorphism of all four. The adjoint of a left multiplication is a left multiplication for the two anti-automorphic involutions and a right multiplication for the identity and the automorphic conjugation, so $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle}=R_{\tilde Q}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural}}=L_{\tilde Q^{\natural}}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{*}}=L_{\tilde Q^{*}}$ and $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural*}}=R_{\bar{\tilde Q}}$. The automorphism groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $U(4)$ and $U(1,3)$. The four pairings separate the two senses of *norm*: the algebraic norm $\langle\tilde Q,\tilde Q\rangle_{\natural}$ is multiplicative and not definite, the Hermitian norm $\langle\tilde Q,\tilde Q\rangle_{*}$ is definite and not multiplicative, and no function is both, because the algebra has zero divisors.

Their null sets separate them as sharply as their signatures. The general plain sesquilinear form has no null element beyond the origin. The general plain bilinear form has the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$, and the general quaternionic bilinear form the complex norm cone $\mathcal{N}=\{\sum_\mu Q_\mu^{2}=0\}$, the zero-divisor cone. The general quaternionic sesquilinear form has the real cone $\mathcal{K}=\{\|c\|_E=\|v\|_E\}$; the two cones $\mathcal{K}$ and $\mathcal{N}$ are distinct, and their intersection is the union of the doubly null lines $\mathbb{C}(e_0+i\hat\mu)$. The sign value-one sets of the general quaternionic sesquilinear form are the three levels of the proposition above; their restrictions to the remarkable real subspaces are the signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$ of the companion articles, and the centre and the vector subspace are the only pair of the six orthogonal for all four forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the general plain bilinear form, the scalar part of $\tilde P\tilde Q$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$ | the general quaternionic bilinear form; $\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ |
| $\langle\tilde P,\tilde Q\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu}$ | the general plain sesquilinear form; $\langle\tilde Q,\tilde Q\rangle_{*}=\lVert\tilde Q\rVert_E^{2}$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the general quaternionic sesquilinear form |
| $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ | the sign matrix, the Gram matrix of the first and the fourth pairings |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the four signatures over $\mathbb{R}$ |
| $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle}=R_{\tilde Q}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural}}=L_{\tilde Q^{\natural}}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{*}}=L_{\tilde Q^{*}}$, $(L_{\tilde Q})^{\langle\cdot,\cdot\rangle_{\natural*}}=R_{\bar{\tilde Q}}$ | the four adjoints |
| $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $U(4)$, $U(1,3)$ | the four automorphism groups |
| $\mathcal{K}=\{\|c\|_E=\|v\|_E\}$ | the Krein null set, the null set of the general quaternionic sesquilinear form |
| $\mathcal{N}=\{\sum_\mu Q_\mu^{2}=0\}$ | the norm cone, the null set of the general quaternionic bilinear form, the zero divisors |
| $\mathbb{C}(e_0\pm i\hat\mu)$ | the doubly null lines, $\mathcal{K}\cap\mathcal{N}$, the Peirce lines |
| $S^{1}\times\mathbb{R}^{6}$, $S^{5}\times\mathbb{R}^{2}$, $S^{7}$ | the value-one sets of the general quaternionic sesquilinear form and of the general plain sesquilinear form |
| $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$, $(3,1)$ | the signatures of the four forms on the remarkable subspaces |

## Further Reading

- *The Four General Products and Operators* (`articles_maths/the-four-general-products-and-operators.md`), for the reading of the four pairings as the scalar parts of the four general products and the answer to the question whether a product decides a rotation or a reflection
- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the four adjoints of the notation table worked out on explicit operators, the four adjoint matrices of one two-sided operator, and the reading of the suffixes of the operator families as those adjoints
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations and their group
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general products whose scalar parts are the four pairings
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the general plain sesquilinear form and its inner product
- *Normed Division Algebras and the Hurwitz Theorem* (`articles_maths/normed-division-algebras-and-the-hurwitz-theorem.md`), for the normed division algebras where the two senses of *norm* are one function, the coincidence that §*The Two Senses of Norm* shows fails here
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the general quaternionic sesquilinear form and its signature
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable real subspaces and their bases
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`) and *Remarkable Subspaces under the Real Biquaternion Algebra* (`articles_maths/remarkable-subspaces-under-the-real-biquaternion-algebra.md`), for the restrictions, subspace by subspace and form by form
- *The Isotropic Structure of the General Quaternionic Sesqualgebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the null set of the general quaternionic sesquilinear form and the doubly null lines
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the sign levels and the hyperbolic structure
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the sphere $S^{7}$ used here for contrast
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-element-representation.md`), for the same four forms read in the two matrix representations
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the transpose that belongs to the general plain bilinear pairing
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for bilinear and sesquilinear forms, their Gram matrices and their automorphism groups
