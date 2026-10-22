
# __Split-Biquaternion Hermitian Subspace__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries four linear involutions, and four of the resulting fixed spaces are its distinguished real subspaces. This article treats the **Hermitian subspace** $\mathbb{M}_+$, the fixed space of Hermitian conjugation: its definition, its basis, the failure of closure under multiplication, the symmetrized product that gives it a Jordan structure, the forms on it, its idempotents, the action of the four involutions and its intersections with the other subspaces. Its complement $\mathbb{M}_-$ under the Hermitian conjugation is treated in *Split-Biquaternion Anti-Hermitian Subspace*; the comparative tables are in *Split-Biquaternion Relations Between Subspaces* and *Split-Biquaternion Involution Lattice*.

The treatment is purely mathematical. No physics is invoked. The split biquaternion algebra is assumed from the basic algebra article, the quaternion algebra $\mathbb{H}$ from the article on quaternion algebra, and the split complex algebra $\mathbb{D}$ from the article on split complex algebra. Throughout, elements are written $\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (split complex), ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (Hermitian) and ${}^{\flat} = -{}^{*}$ (anti-Hermitian). The split-biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$, and the Hermitian norm is $\langle\tilde{Q}\rangle_{*} = \sum_\mu (q_\mu^2 - q'^2_\mu)$.

## Definition and Basis

**Definition.** The **Hermitian subspace** is the fixed space of Hermitian conjugation,

$$
\mathbb{M}_+ = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^{*} = \tilde{Q} \right\}, \qquad \tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}.
$$

### The Condition in Coordinates

Comparing $\overline{\tilde{Q}^{\natural}} = \tilde{Q}$ coefficient by coefficient:

- the coefficient of $e_t$ gives $\bar{Q_t} = Q_t$, so $Q_t = q_t$ is **real**;
- the coefficient of $\vec e_k$ gives $-\bar{Q_k} = Q_k$, that is $\bar{Q_k} = -Q_k$, so $Q_k = j q'_k$ is **purely split-imaginary**.

The subspace is therefore the set of elements with real scalar part and purely split-imaginary vector part,

$$
\tilde{Q} = q_t e_t + j q'_x \vec e_x + j q'_y \vec e_y + j q'_z \vec e_z, \qquad q_t, q'_x, q'_y, q'_z \in \mathbb{R}.
$$

### Basis and Dimension

**Proposition.** The Hermitian subspace is a real vector space of dimension $4$, with basis $e_t, j\vec e_x, j\vec e_y, j\vec e_z$.

**Proof.** The condition removes the four split-imaginary scalar parameters and the four real vector parameters, leaving the four real parameters $q_t, q'_x, q'_y, q'_z$; the four basis elements are linearly independent and span the set.

## Algebra Structure

### It Is Not a Subalgebra

**Proposition.** $\mathbb{M}_+$ is **not** closed under multiplication, and is therefore not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

**Proof.** The elements $j\vec e_x$ and $j\vec e_y$ lie in the subspace, but their product is

$$
(j\vec e_x)(j\vec e_y) = j^2 \vec e_x \vec e_y = \vec e_z,
$$

which has real scalar part $0$ and real vector part $\vec e_z$, and so is not in $\mathbb{M}_+$.

The obstruction is the quaternion part $\vec q_1\times\vec q_2$ of a product, which is a real vector and so leaves the subspace. When that term vanishes the product does stay in $\mathbb{M}_+$, which is the content of the reality of the square below.

### The Commutator Lands in the Anti-Hermitian Subspace

**Proposition.** For $\tilde{Q}_1 = q_{1t} e_t + j\vec q_1$ and $\tilde{Q}_2 = q_{2t} e_t + j\vec q_2$ in $\mathbb{M}_+$, with $\vec q_1, \vec q_2$ real pure quaternions,

$$
[\tilde{Q}_1, \tilde{Q}_2] = \tilde{Q}_1\tilde{Q}_2 - \tilde{Q}_2\tilde{Q}_1 = 2\,\vec q_1 \times \vec q_2 \in \mathbb{M}_-.
$$

**Proof.** Expanding the product and using $\vec q_1\vec q_2 = -\vec q_1\cdot\vec q_2 + \vec q_1\times\vec q_2$ gives $\tilde{Q}_1\tilde{Q}_2 = q_{1t}q_{2t} - \vec q_1\cdot\vec q_2 + \vec q_1\times\vec q_2 + j(q_{1t}\vec q_2 + q_{2t}\vec q_1)$ and the conjugate expression for $\tilde{Q}_2\tilde{Q}_1$; the difference is $2\vec q_1\times\vec q_2$, a pure real quaternion, which lies in $\mathbb{M}_-$.

So the Hermitian subspace is **not** a Lie subalgebra; the bracket of two Hermitian elements is anti-Hermitian. This is the beginning of the Hermitian–anti-Hermitian correspondence developed in *Split-Biquaternion Anti-Hermitian Subspace*.

### It Is a Jordan Algebra

**Proposition.** The symmetrized product $\tilde{Q}_1 \bullet \tilde{Q}_2 = \tfrac{1}{2}(\tilde{Q}_1\tilde{Q}_2 + \tilde{Q}_2\tilde{Q}_1)$ closes on $\mathbb{M}_+$,

$$
\tilde{Q}_1 \bullet \tilde{Q}_2 = \left(q_{1t} q_{2t} - \vec q_1\cdot\vec q_2\right) e_t + j\left(q_{1t} \vec q_2 + q_{2t} \vec q_1\right) \in \mathbb{M}_+,
$$

and with it $\mathbb{M}_+$ is a **Jordan algebra** (commutative, with $\tilde{Q}_1 \bullet (\tilde{Q}_1 \bullet \tilde{Q}_1) = (\tilde{Q}_1 \bullet \tilde{Q}_1) \bullet \tilde{Q}_1$).

**Proof.** The symmetrized product of the expansions is as displayed, with real scalar part and purely split-imaginary vector part; commutativity is clear, and the Jordan identity follows from the associativity of the total product and the commutativity of $\bullet$.

The precedent is the Hermitian subspace of the biquaternion algebra, where the same symmetrized product gives a Jordan algebra; the general theory is the companion article *Jordan Algebras*.

### The Square and the Higher Powers

Because $\bullet$ closes, every power of a Hermitian element is Hermitian. Explicitly,

$$
\tilde{Q}^2 = \left(q_t^2 - (\vec q, \vec q)\right) e_t + 2 j q_t \vec q, \qquad \tilde{Q} = q_t e_t + j \vec q,
$$

whose scalar part is real and whose vector part is purely split-imaginary. In particular, for a purely vector Hermitian element $j\vec q$,

$$
(j\vec q)^2 = -(\vec q, \vec q) e_t = -\langle j\vec q\rangle_{\natural}\, e_t
$$

is a **real scalar**; the square of a Hermitian vector is central. The scalar part of the square is $q_t^2 - |\vec q|^2$, which can have either sign, so the square does not preserve positivity of the scalar part — unlike the biquaternion Hermitian subspace, where the scalar part of the square is a sum of squares.

### Stability under Multiplication

$\mathbb{M}_+$ is stable under multiplication by the centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, which acts by scalar extension. It is not stable under multiplication by the quaternion subspace on either side, since $\vec e_x (j\vec e_x) = \vec e_x j \vec e_x = j \vec e_x^2 = -j \notin \mathbb{M}_+$. Its behaviour under multiplication is therefore limited to the central scalar extension, while its role as a product space is the Jordan one.

## The Split-Biquaternion Norm and the Hermitian Form

### The Split-Biquaternion Norm and Its Signature

**Theorem.** On the Hermitian subspace the split-biquaternion norm is the **positive definite** real quadratic form

$$
\langle\tilde{Q}\rangle_{\natural} = q_t^2 + (q'_x)^2 + (q'_y)^2 + (q'_z)^2, \qquad \tilde{Q} = q_t e_t + j q'_x \vec e_x + j q'_y \vec e_y + j q'_z \vec e_z,
$$

of signature $(4,0)$.

**Proof.** Substituting $Q_t = q_t$ and $Q_k = j q'_k$ in $\langle\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2$ gives $q_t^2 + \sum_k (q'_k)^2$, because $(j q'_k)^2 = j^2 (q'_k)^2 = +(q'_k)^2$ — the sign is positive because the split complex unit satisfies $j^2 = +1$.

This is the first structural difference from the biquaternion Hermitian subspace, where the split-biquaternion norm is the indefinite form $q_t^2 - \sum_k (q'_k)^2$ of signature $(1,3)$, because the central unit there satisfies $i^2 = -1$. In the split algebra the split-biquaternion norm is definite on the sector, and there is **no isotropic cone of the split-biquaternion norm**.

### The Hermitian Norm and Its Isotropic Cone

The indefinite form on the sector is the **Hermitian norm** $\langle\tilde Q\rangle_{*} = \sum_\mu (q_\mu^2 - q'^2_\mu)$. On $\mathbb{M}_+$ this is

$$
\sum_{\mu\in\{t,x,y,z\}} (q_\mu^2 - q'^2_\mu) = q_t^2 - \left((q'_x)^2 + (q'_y)^2 + (q'_z)^2\right),
$$

of signature $(1,3)$. Its isotropic cone is the three-dimensional cone

$$
q_t^2 = (q'_x)^2 + (q'_y)^2 + (q'_z)^2,
$$

the split analogue of the biquaternion null cone, but carried by the Hermitian form rather than by the split-biquaternion norm.

### Units, Zero Divisors and Nilpotents

**Theorem.** For $\tilde{Q} \in \mathbb{M}_+$ the following are equivalent: $\tilde{Q}$ is a unit; $\langle\tilde{Q}\rangle_{\natural} \neq 0$; $\tilde{Q} \neq 0$. In particular $\mathbb{M}_+$ contains **no zero divisor** and **no nilpotent**.

**Proof.** The split-biquaternion norm is positive definite on the subspace, so it vanishes only at the origin and every nonzero element is a unit, with $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$. A nilpotent satisfies $\tilde{Q}^2 = 0$; by the square formula this forces $q_t^2 = |\vec q|^2$ and $q_t\vec q = 0$, hence $\vec q = 0$ and $q_t = 0$.

So the isotropic cone of the Hermitian form is **not** the zero divisor set: every nonzero point of the cone is a unit. This is the sharpest difference from the biquaternion Hermitian subspace, where the isotropic cone and the zero divisors of the sector coincide. The absence of nilpotents holds here as it does there.

### The Idempotents

**Theorem.** The idempotents of $\mathbb{M}_+$ are exactly $0$ and $e_t$.

**Proof.** Let $\tilde{Q} = q_t e_t + j\vec q$ satisfy $\tilde{Q}^2 = \tilde{Q}$. Comparing with the square formula, $2 q_t \vec q = \vec q$ and $q_t^2 - |\vec q|^2 = q_t$. If $\vec q = 0$, then $q_t \in \{0, 1\}$. If $\vec q \neq 0$, then $q_t = \tfrac{1}{2}$ and $q_t^2 - |\vec q|^2 = q_t$ gives $|\vec q|^2 = -\tfrac{1}{4}$, impossible.

The nontrivial idempotents $\tilde\Pi_1$ and $\tilde\Pi_2$ of $\mathbb{H}_{\mathbb{D}}$ are **not** Hermitian, since $\tilde\Pi_1^{*} = \tilde\Pi_2$; they lie in the split complex subspace, not in $\mathbb{M}_+$. This is the opposite of the biquaternion situation, where the nontrivial idempotents are Hermitian and lie in $\mathbb{M}_+$; the reason is again that there is no central scalar imaginary here.

## The Image in the Two Halves

Under the idempotent-decomposition isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, a Hermitian element $\tilde{Q} = q_t e_t + j\vec q$ has components

$$
\tilde{Q}_+ = q_t + \vec q, \qquad \tilde{Q}_- = q_t - \vec q = (\tilde{Q}_+)^{\natural}.
$$

The image of $\mathbb{M}_+$ is therefore the set of **conjugate pairs**

$$
\varphi(\mathbb{M}_+) = \left\{ (h, h^{\natural}) : h \in \mathbb{H} \right\} \cong \mathbb{H},
$$

a real four-dimensional subspace of $\mathbb{H} \oplus \mathbb{H}$, and the map $h \mapsto (h, h^{\natural})$ is an isomorphism of the underlying real vector spaces. With the Hermitian form this identifies the Hermitian sector with the graph of quaternion conjugation in $\mathbb{H} \oplus \mathbb{H}$.

## The Four Involutions on It

In the basis $e_t, j\vec e_x, j\vec e_y, j\vec e_z$ the four involutions act diagonally:

| involution | matrix | effect |
|---|---|---|
| ${}^{\natural}$ | $\operatorname{diag}(1, -1, -1, -1)$ | negates the split-imaginary vector part |
| $\bar{\cdot}$ | $\operatorname{diag}(1, -1, -1, -1)$ | negates the split-imaginary vector part |
| ${}^{*}$ | $+\mathrm{id}$ | the identity, by definition |
| ${}^{\flat}$ | $-\mathrm{id}$ | minus the identity |

The subspace is invariant under all four. Quaternion conjugation and split complex conjugation agree on it, which is the compatibility ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ read on the fixed space of ${}^{*}$: both send $j\vec e_k \mapsto -j\vec e_k$ and fix $e_t$. Anti-Hermitian conjugation negates the subspace, and its fixed space is $\mathbb{M}_-$.

## Relations to the Other Subspaces

The intersections of $\mathbb{M}_+$ with the other distinguished subspaces are, with dimensions:

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{M}_+ \cap \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{R}$ | $1$ |
| $\mathbb{M}_+ \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{R}$ | $1$ |
| $\mathbb{M}_+ \cap \mathbb{M}_-$ | $\{0\}$ | $0$ |
| $\mathbb{M}_+ \cap \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathrm{span}\{j\vec e_x, j\vec e_y, j\vec e_z\}$ | $3$ |

The subspace is complementary to $\mathbb{M}_-$: since $2\tilde{Q} = (\tilde{Q} + \tilde{Q}^{*}) + (\tilde{Q} - \tilde{Q}^{*})$ for every element, and $\mathbb{M}_+ \cap \mathbb{M}_- = \{0\}$, one has the **Hermitian decomposition**

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-.
$$

Its decomposition along the coordinate blocks is $\mathbb{M}_+ = \mathbb{R} e_t \oplus \mathrm{span}\{j\vec e_x, j\vec e_y, j\vec e_z\}$: the scalar line is shared with the centre and the quaternion subspaces, and the split-imaginary triple with the vector subspace. Its sum with the centre has dimension $5$ and its sum with the quaternion subspace has dimension $7$; only the pair with $\mathbb{M}_-$ spans the algebra. The full tables are in *Split-Biquaternion Relations Between Subspaces*.

## The Analysis on the Hermitian Subspace

The Hermitian subspace is not a subalgebra, so it carries no intrinsic multiplicative function theory; the analysis on it is the restriction of the ambient analysis of *Split-Biquaternion Analysis* to a four-dimensional subspace, together with the differential operators built from the Hermitian form. The ambient Cauchy–Riemann operator of *Split-Biquaternion Analysis* restricted to $\mathbb{M}_+$ splits into the Hermitian and anti-Hermitian pieces, and the second-order operator obtained is the wave operator of the restricted Lorentzian form $q_t^2 - \sum_k q'^2_k$ of signature $(1,3)$ rather than a Laplacian. A general function on $\mathbb{M}_+$ alone has no product rule, because a product of two elements of $\mathbb{M}_+$ leaves the subspace; only the functions that extend to regular functions on the algebra have an intrinsic theory.

## The Geometry of the Hermitian Subspace

The Hermitian subspace is the fixed space of Hermitian conjugation, the positive eigenspace of the involution ${}^{*}$ of the algebra, and geometrically the invariant four-plane of the corresponding linear involution of $\mathbb{R}^8$. It is a Lorentzian subspace for the Hermitian scalar form: $g$ restricts to the real form $q_t^2 - \sum_k q'^2_k$ of signature $(1,3)$ of *Split-Biquaternion Rotations and the Lorentz Group*, while the split-biquaternion norm restricts to the positive definite form $q_t^2 + \sum_k q'^2_k$ of signature $(4,0)$ recorded in the notation table above. The null cone of $g$ is the cone $q_t^2 = \sum_k q'^2_k$; the restricted form being indefinite of signature $(1,3)$, it has isotropic lines, and their projectivisation in $\mathbb{P}(\mathbb{M}_+)$ is a two-sphere. The motions it carries are the Lorentz group $SO(1,3)$ induced by the algebra units, the hyperbolic rotations of *Split-Biquaternions and Hyperbolic Geometry*.

## Summary

The Hermitian subspace $\mathbb{M}_+$ is the fixed space of Hermitian conjugation, the set of elements $\tilde{Q} = q_t e_t + j q'_x \vec e_x + j q'_y \vec e_y + j q'_z \vec e_z$ with real scalar part and purely split-imaginary vector part; it is a real vector space of dimension $4$ with basis $e_t, j\vec e_x, j\vec e_y, j\vec e_z$. It is **not** a subalgebra, since $(j\vec e_x)(j\vec e_y) = \vec e_z$ leaves the subspace; but it is closed under the symmetrized product, which gives it the structure of a **Jordan algebra**, and the square of a Hermitian vector is a real scalar. The commutator of two Hermitian elements is $2\,\vec q_1\times\vec q_2$, an anti-Hermitian element, so the bracket lands in $\mathbb{M}_-$. The split-biquaternion norm restricts to the positive definite form $N = q_t^2 + (q'_x)^2 + (q'_y)^2 + (q'_z)^2$ of signature $(4,0)$, and consequently $\mathbb{M}_+$ contains no zero divisor and no nilpotent; the indefinite form is the Hermitian form, of signature $(1,3)$ and isotropic cone $q_t^2 = (q'_x)^2+(q'_y)^2+(q'_z)^2$, whose nonzero points are all units. The only idempotents in the subspace are $0$ and $e_t$; unlike the biquaternion case the nontrivial idempotents are not Hermitian. The image under $\varphi$ is the set of conjugate pairs $(h, h^{\natural})$ in $\mathbb{H} \oplus \mathbb{H}$. Of the four involutions, Hermitian conjugation fixes the subspace pointwise, quaternion and split complex conjugations both negate its vector part, and anti-Hermitian conjugation is minus the identity; the subspace is complementary to $\mathbb{M}_-$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = q_t e_t + j q'_x \vec e_x + j q'_y \vec e_y + j q'_z \vec e_z$ | Element of the Hermitian subspace, coefficients real |
| $\mathbb{M}_+$ | Hermitian subspace, fixed space of ${}^{*}$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, fixed space of ${}^{\flat}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations |
| $\langle\tilde{Q}\rangle_{\natural} = q_t^2 + (q'_x)^2 + (q'_y)^2 + (q'_z)^2$ | Norm on $\mathbb{M}_+$, signature $(4,0)$ |
| $\langle\tilde Q\rangle_{*} = \sum_\mu (q_\mu^2 - q'^2_\mu)$ | Hermitian norm, signature $(1,3)$ on $\mathbb{M}_+$ |
| $\tilde{Q}_1 \bullet \tilde{Q}_2 = \tfrac{1}{2}(\tilde{Q}_1\tilde{Q}_2 + \tilde{Q}_2\tilde{Q}_1)$ | Symmetrized (Jordan) product |
| $[\tilde{Q}_1, \tilde{Q}_2] = 2\,\vec q_1\times\vec q_2$ | Commutator, an element of $\mathbb{M}_-$ |
| $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$ | Image in $\mathbb{H} \oplus \mathbb{H}$; $(h,h^{\natural})$ on $\mathbb{M}_+$ |
| $q_t^2 = (q'_x)^2 + (q'_y)^2 + (q'_z)^2$ | Isotropic cone of the Hermitian norm |
| $SO(1,3)$ | Lorentz group acting on the Hermitian subspace |

## Further Reading

- Pascual Jordan, "Über eine Klasse nichtassociativer hyperkomplexer Algebren" (1932), for the symmetrized product and the Jordan algebras it defines.
- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for the Hermitian and anti-Hermitian sectors of algebras with a conjugation.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the Hermitian decomposition of the split biquaternion algebra and the forms on its sectors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Hermitian and anti-Hermitian elements of Clifford algebras of split signature and their Jordan structure.
