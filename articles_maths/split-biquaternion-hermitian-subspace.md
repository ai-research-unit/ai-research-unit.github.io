
# __Split-Biquaternion Hermitian Subspace__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries four linear involutions, and four of the resulting fixed spaces are its distinguished real subspaces. This article treats the **Hermitian subspace** $\mathbb{M}_+$, the fixed space of Hermitian conjugation: its definition, its basis, the failure of closure under multiplication, the symmetrized product that gives it a Jordan structure, the forms on it, its idempotents, the action of the four involutions and its intersections with the other subspaces. Its complement $\mathbb{M}_-$ under the Hermitian conjugation is treated in *Split-Biquaternion Anti-Hermitian Subspace*; the comparative tables are in *Split-Biquaternion Relations Between Subspaces* and *Split-Biquaternion Involution Lattice*.

The treatment is purely mathematical. No physics is invoked. The split biquaternion algebra is assumed from the basic algebra article, the quaternion algebra $\mathbb{H}$ from the article on quaternion algebra, and the split complex algebra $\mathbb{D}$ from the article on split complex algebra. Throughout, elements are written $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are $\bar{\cdot}$ (quaternion), ${}^{*}$ (split complex), ${}^{\dagger} = {}^{*}\circ\bar{\cdot}$ (Hermitian) and ${}^{\flat} = -{}^{\dagger}$ (anti-Hermitian). The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$, and the Hermitian form has scalar part $\sum_\mu (q_\mu^2 - q'^2_\mu)$.

## Definition and Basis

**Definition.** The **Hermitian subspace** is the fixed space of Hermitian conjugation,

$$
\mathbb{M}_+ = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^{\dagger} = \tilde{Q} \right\}, \qquad \tilde{Q}^\dagger = \bar{\tilde{Q}}^{*}.
$$

### The Condition in Coordinates

Comparing $\bar{\tilde{Q}}^{*} = \tilde{Q}$ coefficient by coefficient:

- the coefficient of $e_0$ gives $Q_0^{*} = Q_0$, so $Q_0 = q_0$ is **real**;
- the coefficient of $e_k$ gives $-Q_k^{*} = Q_k$, that is $Q_k^{*} = -Q_k$, so $Q_k = j q'_k$ is **purely split-imaginary**.

The subspace is therefore the set of elements with real scalar part and purely split-imaginary vector part,

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

### Basis and Dimension

**Proposition.** The Hermitian subspace is a real vector space of dimension $4$, with basis $e_0, je_1, je_2, je_3$.

**Proof.** The condition removes the four split-imaginary scalar parameters and the four real vector parameters, leaving the four real parameters $q_0, q'_1, q'_2, q'_3$; the four basis elements are linearly independent and span the set. $\square$

## Algebra Structure

### It Is Not a Subalgebra

**Proposition.** $\mathbb{M}_+$ is **not** closed under multiplication, and is therefore not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

**Proof.** The elements $je_1$ and $je_2$ lie in the subspace, but their product is

$$
(je_1)(je_2) = j^2 e_1 e_2 = e_3,
$$

which has real scalar part $0$ and real vector part $e_3$, and so is not in $\mathbb{M}_+$. $\square$

The obstruction is the quaternion part $\mathbf{u}\times\mathbf{v}$ of a product, which is a real vector and so leaves the subspace. When that term vanishes the product does stay in $\mathbb{M}_+$, which is the content of the reality of the square below.

### The Commutator Lands in the Anti-Hermitian Subspace

**Proposition.** For $\tilde{Q} = q_0 e_0 + j\mathbf{u}$ and $\tilde{R} = r_0 e_0 + j\mathbf{v}$ in $\mathbb{M}_+$, with $\mathbf{u}, \mathbf{v}$ real pure quaternions,

$$
[\tilde{Q}, \tilde{R}] = \tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2\,\mathbf{u} \times \mathbf{v} \in \mathbb{M}_-.
$$

**Proof.** Expanding the product and using $\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v}$ gives $\tilde{Q}\tilde{R} = q_0r_0 - \mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v} + j(q_0\mathbf{v} + r_0\mathbf{u})$ and the conjugate expression for $\tilde{R}\tilde{Q}$; the difference is $2\mathbf{u}\times\mathbf{v}$, a pure real quaternion, which lies in $\mathbb{M}_-$. $\square$

So the Hermitian subspace is **not** a Lie subalgebra; the bracket of two Hermitian elements is anti-Hermitian. This is the beginning of the Hermitian–anti-Hermitian correspondence developed in *Split-Biquaternion Anti-Hermitian Subspace*.

### It Is a Jordan Algebra

**Proposition.** The symmetrized product $\tilde{Q} \circ \tilde{R} = \tfrac{1}{2}(\tilde{Q}\tilde{R} + \tilde{R}\tilde{Q})$ closes on $\mathbb{M}_+$,

$$
\tilde{Q} \circ \tilde{R} = \left(q_0 r_0 - \mathbf{u}\cdot\mathbf{v}\right) e_0 + j\left(q_0 \mathbf{v} + r_0 \mathbf{u}\right) \in \mathbb{M}_+,
$$

and with it $\mathbb{M}_+$ is a **Jordan algebra** (commutative, with $\tilde{Q} \circ (\tilde{Q} \circ \tilde{Q}) = (\tilde{Q} \circ \tilde{Q}) \circ \tilde{Q}$).

**Proof.** The symmetrized product of the expansions is as displayed, with real scalar part and purely split-imaginary vector part; commutativity is clear, and the Jordan identity follows from the associativity of the total product and the commutativity of $\circ$. $\square$

The precedent is the Hermitian subspace of the biquaternion algebra, where the same symmetrized product gives a Jordan algebra; the general theory is the companion article *Jordan Algebras*.

### The Square and the Higher Powers

Because $\circ$ closes, every power of a Hermitian element is Hermitian. Explicitly,

$$
\tilde{Q}^2 = \left(q_0^2 - (\mathbf{u}, \mathbf{u})\right) e_0 + 2 j q_0 \mathbf{u}, \qquad \tilde{Q} = q_0 e_0 + j \mathbf{u},
$$

whose scalar part is real and whose vector part is purely split-imaginary. In particular, for a purely vector Hermitian element $j\mathbf{u}$,

$$
(j\mathbf{u})^2 = -(\mathbf{u}, \mathbf{u}) e_0 = -N(j\mathbf{u})\, e_0
$$

is a **real scalar**; the square of a Hermitian vector is central. The scalar part of the square is $q_0^2 - |\mathbf{u}|^2$, which can have either sign, so the square does not preserve positivity of the scalar part — unlike the biquaternion Hermitian subspace, where the scalar part of the square is a sum of squares.

### Stability under Multiplication

$\mathbb{M}_+$ is stable under multiplication by the centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, which acts by scalar extension. It is not stable under multiplication by the quaternion subspace on either side, since $e_1 (je_1) = e_1 j e_1 = j e_1^2 = -j \notin \mathbb{M}_+$. Its behaviour under multiplication is therefore limited to the central scalar extension, while its role as a product space is the Jordan one.

## The Norm Form and the Hermitian Form

### The Norm Form and Its Signature

**Theorem.** On the Hermitian subspace the norm form is the **positive definite** real quadratic form

$$
N(\tilde{Q}) = q_0^2 + (q'_1)^2 + (q'_2)^2 + (q'_3)^2, \qquad \tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3,
$$

of signature $(4,0)$.

**Proof.** Substituting $Q_0 = q_0$ and $Q_k = j q'_k$ in $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ gives $q_0^2 + \sum_k (q'_k)^2$, because $(j q'_k)^2 = j^2 (q'_k)^2 = +(q'_k)^2$ — the sign is positive because the split complex unit satisfies $j^2 = +1$. $\square$

This is the first structural difference from the biquaternion Hermitian subspace, where the norm form is the indefinite form $q_0^2 - \sum_k (q'_k)^2$ of signature $(1,3)$, because the central unit there satisfies $i^2 = -1$. In the split algebra the norm form is definite on the sector, and there is **no isotropic cone of the norm form**.

### The Hermitian Form and Its Isotropic Cone

The indefinite form on the sector is the **Hermitian form**, whose scalar part is $\sum_\mu (q_\mu^2 - q'^2_\mu)$. On $\mathbb{M}_+$ this is

$$
\sum_{\mu=0}^{3} (q_\mu^2 - q'^2_\mu) = q_0^2 - \left((q'_1)^2 + (q'_2)^2 + (q'_3)^2\right),
$$

of signature $(1,3)$. Its isotropic cone is the three-dimensional cone

$$
q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2,
$$

the split analogue of the biquaternion null cone, but carried by the Hermitian form rather than by the norm form.

### Units, Zero Divisors and Nilpotents

**Theorem.** For $\tilde{Q} \in \mathbb{M}_+$ the following are equivalent: $\tilde{Q}$ is a unit; $N(\tilde{Q}) \neq 0$; $\tilde{Q} \neq 0$. In particular $\mathbb{M}_+$ contains **no zero divisor** and **no nilpotent**.

**Proof.** The norm form is positive definite on the subspace, so it vanishes only at the origin and every nonzero element is a unit, with $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$. A nilpotent satisfies $\tilde{Q}^2 = 0$; by the square formula this forces $q_0^2 = |\mathbf{u}|^2$ and $q_0\mathbf{u} = 0$, hence $\mathbf{u} = 0$ and $q_0 = 0$. $\square$

So the isotropic cone of the Hermitian form is **not** the zero divisor set: every nonzero point of the cone is a unit. This is the sharpest difference from the biquaternion Hermitian subspace, where the isotropic cone and the zero divisors of the sector coincide. The absence of nilpotents holds here as it does there.

### The Idempotents

**Theorem.** The idempotents of $\mathbb{M}_+$ are exactly $0$ and $e_0$.

**Proof.** Let $\tilde{Q} = q_0 e_0 + j\mathbf{u}$ satisfy $\tilde{Q}^2 = \tilde{Q}$. Comparing with the square formula, $2 q_0 \mathbf{u} = \mathbf{u}$ and $q_0^2 - |\mathbf{u}|^2 = q_0$. If $\mathbf{u} = 0$, then $q_0 \in \{0, 1\}$. If $\mathbf{u} \neq 0$, then $q_0 = \tfrac{1}{2}$ and $q_0^2 - |\mathbf{u}|^2 = q_0$ gives $|\mathbf{u}|^2 = -\tfrac{1}{4}$, impossible. $\square$

The nontrivial idempotents $\tilde\Pi_+$ and $\tilde\Pi_-$ of $\mathbb{H}_{\mathbb{D}}$ are **not** Hermitian, since $\tilde\Pi_+^\dagger = \tilde\Pi_-$; they lie in the split complex subspace, not in $\mathbb{M}_+$. This is the opposite of the biquaternion situation, where the nontrivial idempotents are Hermitian and lie in $\mathbb{M}_+$; the reason is again that there is no central scalar imaginary here.

## The Image in the Two Halves

Under the idempotent-decomposition isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, a Hermitian element $\tilde{Q} = q_0 e_0 + j\mathbf{u}$ has components

$$
\tilde{Q}_+ = q_0 + \mathbf{u}, \qquad \tilde{Q}_- = q_0 - \mathbf{u} = \overline{\tilde{Q}_+}.
$$

The image of $\mathbb{M}_+$ is therefore the set of **conjugate pairs**

$$
\varphi(\mathbb{M}_+) = \left\{ (h, \bar{h}) : h \in \mathbb{H} \right\} \cong \mathbb{H},
$$

a real four-dimensional subspace of $\mathbb{H} \oplus \mathbb{H}$, and the map $h \mapsto (h, \bar{h})$ is an isomorphism of the underlying real vector spaces. With the Hermitian form this identifies the Hermitian sector with the graph of quaternion conjugation in $\mathbb{H} \oplus \mathbb{H}$.

## The Four Involutions on It

In the basis $e_0, je_1, je_2, je_3$ the four involutions act diagonally:

| involution | matrix | effect |
|---|---|---|
| $\bar{\cdot}$ | $\operatorname{diag}(1, -1, -1, -1)$ | negates the split-imaginary vector part |
| ${}^{*}$ | $\operatorname{diag}(1, -1, -1, -1)$ | negates the split-imaginary vector part |
| ${}^{\dagger}$ | $+\mathrm{id}$ | the identity, by definition |
| ${}^{\flat}$ | $-\mathrm{id}$ | minus the identity |

The subspace is invariant under all four. Quaternion conjugation and split complex conjugation agree on it, which is the compatibility $\dagger = {}^{*}\circ\bar{\cdot}$ read on the fixed space of $\dagger$: both send $je_k \mapsto -je_k$ and fix $e_0$. Anti-Hermitian conjugation negates the subspace, and its fixed space is $\mathbb{M}_-$.

## Relations to the Other Subspaces

The intersections of $\mathbb{M}_+$ with the other distinguished subspaces are, with dimensions:

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{M}_+ \cap \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{R}$ | $1$ |
| $\mathbb{M}_+ \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{R}$ | $1$ |
| $\mathbb{M}_+ \cap \mathbb{M}_-$ | $\{0\}$ | $0$ |
| $\mathbb{M}_+ \cap \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathrm{span}\{je_1, je_2, je_3\}$ | $3$ |

The subspace is complementary to $\mathbb{M}_-$: since $2\tilde{Q} = (\tilde{Q} + \tilde{Q}^\dagger) + (\tilde{Q} - \tilde{Q}^\dagger)$ for every element, and $\mathbb{M}_+ \cap \mathbb{M}_- = \{0\}$, one has the **Hermitian decomposition**

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-.
$$

Its decomposition along the coordinate blocks is $\mathbb{M}_+ = \mathbb{R} e_0 \oplus \mathrm{span}\{je_1, je_2, je_3\}$: the scalar line is shared with the centre and the quaternion subspaces, and the split-imaginary triple with the vector subspace. Its sum with the centre has dimension $5$ and its sum with the quaternion subspace has dimension $7$; only the pair with $\mathbb{M}_-$ spans the algebra. The full tables are in *Split-Biquaternion Relations Between Subspaces*.

## Summary

The Hermitian subspace $\mathbb{M}_+$ is the fixed space of Hermitian conjugation, the set of elements $\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3$ with real scalar part and purely split-imaginary vector part; it is a real vector space of dimension $4$ with basis $e_0, je_1, je_2, je_3$. It is **not** a subalgebra, since $(je_1)(je_2) = e_3$ leaves the subspace; but it is closed under the symmetrized product, which gives it the structure of a **Jordan algebra**, and the square of a Hermitian vector is a real scalar. The commutator of two Hermitian elements is $2\,\mathbf{u}\times\mathbf{v}$, an anti-Hermitian element, so the bracket lands in $\mathbb{M}_-$. The norm form restricts to the positive definite form $N = q_0^2 + (q'_1)^2 + (q'_2)^2 + (q'_3)^2$ of signature $(4,0)$, and consequently $\mathbb{M}_+$ contains no zero divisor and no nilpotent; the indefinite form is the Hermitian form, of signature $(1,3)$ and isotropic cone $q_0^2 = (q'_1)^2+(q'_2)^2+(q'_3)^2$, whose nonzero points are all units. The only idempotents in the subspace are $0$ and $e_0$; unlike the biquaternion case the nontrivial idempotents are not Hermitian. The image under $\varphi$ is the set of conjugate pairs $(h, \bar{h})$ in $\mathbb{H} \oplus \mathbb{H}$. Of the four involutions, Hermitian conjugation fixes the subspace pointwise, quaternion and split complex conjugations both negate its vector part, and anti-Hermitian conjugation is minus the identity; the subspace is complementary to $\mathbb{M}_-$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3$ | Element of the Hermitian subspace, coefficients real |
| $\mathbb{M}_+$ | Hermitian subspace, fixed space of ${}^{\dagger}$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, fixed space of ${}^{\flat}$ |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | The four conjugations |
| $N(\tilde{Q}) = q_0^2 + |\mathbf{u}|^2$ | Norm form on $\mathbb{M}_+$, signature $(4,0)$ |
| $\sum_\mu (q_\mu^2 - q'^2_\mu)$ | Scalar part of the Hermitian form, signature $(1,3)$ on $\mathbb{M}_+$ |
| $\tilde{Q} \circ \tilde{R} = \tfrac{1}{2}(\tilde{Q}\tilde{R} + \tilde{R}\tilde{Q})$ | Symmetrized (Jordan) product |
| $[\tilde{Q}, \tilde{R}] = 2\,\mathbf{u}\times\mathbf{v}$ | Commutator, an element of $\mathbb{M}_-$ |
| $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$ | Image in $\mathbb{H} \oplus \mathbb{H}$; $(h,\bar{h})$ on $\mathbb{M}_+$ |
| $q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2$ | Isotropic cone of the Hermitian form |

## Further Reading

- Pascual Jordan, "Über eine Klasse nichtassociativer hyperkomplexer Algebren" (1932), for the symmetrized product and the Jordan algebras it defines.
- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for the Hermitian and anti-Hermitian sectors of algebras with a conjugation.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the Hermitian decomposition of the split biquaternion algebra and the forms on its sectors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Hermitian and anti-Hermitian elements of Clifford algebras of split signature and their Jordan structure.
