# __Hermitian Algebras__

## Introduction

A **Hermitian algebra** is an associative algebra carrying an involution and a Hermitian form that the involution turns into the adjoint of multiplication. The data are a product, an involution and a form, and one axiom ties them together:

$$
\langle xy, z \rangle = \langle y, x^{\dagger} z \rangle .
$$

The axiom says that the involution computes the adjoint of every multiplication operator. It is the algebraic content of the whole layer, and it needs nothing else: no positivity of the form, no completeness of the algebra, no norm and no convergence.

This article is the base of the four operator groups of `Sesqualgebras with a degree-2 form`: the two-sided operators with the Hermitian sandwich $\Theta_x(y) = xyx^{\dagger}$, the one-sided operators, and their signed variants all take the dagger fixed here as their involution. It is the Part I companion of *Hilbert Algebras*, which adds the two hypotheses this article removes — the positive definiteness of the form and the completion of the algebra. Positivity, the cone, Cauchy–Schwarz, the completion and the modular theory are *Hilbert Algebras* and the later articles of Part II; the adjoint, the radical, the isometry group and the unitary slice are here.

The base is a commutative ring $F$ with an involution $\sigma$, and the collapse at $\sigma = \mathrm{id}$ returns the bilinear theory of *Algebras with a degree-2 form*.

## The Axioms

### Definition

Let $A$ be a unital associative algebra over a commutative ring $F$ carrying an involution $\sigma$, and let $x \mapsto x^{\dagger}$ be an involution of $A$, $\sigma$-semilinear over $F$:

$$
(xy)^{\dagger} = y^{\dagger}x^{\dagger}, \qquad (x^{\dagger})^{\dagger} = x, \qquad 1^{\dagger} = 1, \qquad (ax)^{\dagger} = \sigma(a)x^{\dagger} .
$$

A **Hermitian form** on $A$ is a map $\langle \cdot, \cdot \rangle : A \times A \to F$ that is

- additive in each argument, with $\langle ax, y \rangle = a\langle x, y\rangle$ and $\langle x, ay \rangle = \sigma(a)\langle x, y\rangle$ for $a \in F$;
- Hermitian: $\langle x, y \rangle = \sigma(\langle y, x \rangle)$, so that the diagonal $q(x) = \langle x, x\rangle$ lies in the fixed ring $F^\sigma$;
- non-degenerate: $\langle x, y \rangle = 0$ for every $y$ forces $x = 0$.

A **Hermitian algebra** is the triple $(A, \bar{\cdot}, \langle \cdot, \cdot \rangle)$ with the form tied to the involution by the **adjoint axiom**

$$
\langle xy, z \rangle = \langle y, x^{\dagger} z \rangle \qquad \text{for all } x, y, z \in A .
$$

Two of the three data are constitutive of the algebra — the product and the involution — and the third is constitutive of the *Hermitian* structure. The axiom is what forbids an arbitrary pairing: it is the statement that the involution is the adjoint operation of the algebra for the form. A **Hilbert algebra** is the case in which the form is, in addition, positive definite; that hypothesis is not made here.

### The Adjoint Axiom

**Proposition.** The adjoint axiom is equivalent to

$$
\langle x^{\dagger}y, z \rangle = \langle y, xz \rangle .
$$

**Proof.** Apply the axiom to the pair $(y^{\dagger}, x^{\dagger})$ and use $y^{\dagger}x^{\dagger} = (xy)^{\dagger}$, obtaining $\langle (xy)^{\dagger}, z\rangle = \langle x^{\dagger}, yz\rangle$; reading the axiom on the pair $(x^{\dagger},y)$ gives the displayed relation. The non-degeneracy of the form is what makes the adjoint unique.

**Remark (a third identity is not equivalent).** The identity $\langle xy,z\rangle = \langle x, zy^{\dagger}\rangle$ is sometimes listed as a third equivalent form of the axiom. It is not a consequence of it, even for a non-degenerate form: the compatible form $\tau(xGy^{\dagger})$ with $G = \operatorname{diag}(1,-1)$ on $M_2$ fails it on $307\,008$ of the $531\,441$ triples of matrices with entries in $\{-1,0,1\}$, while the trace form $\tau(xy^{\dagger})$ satisfies it because $(zy^{\dagger})^{\dagger} = yz^{\dagger}$ and the trace is cyclic. The identity is an extra hypothesis, and it is discussed in *Sesqualgebras with a Form*.

**Proposition.** Let $L_x : A \to A$ be the left multiplication $L_x(y) = xy$ and let $R_x(y) = yx$ be the right multiplication. Then

$$
L_{x^{\dagger}} = L_x^{*},
$$

the adjoint being taken with respect to $\langle \cdot, \cdot \rangle$.

**Proof.** $\langle L_xy, z\rangle = \langle xy, z\rangle = \langle y, x^{\dagger}z\rangle = \langle y, L_{x^{\dagger}}z\rangle$ for all $y, z$, which is the defining relation of the adjoint, and non-degeneracy makes the adjoint unique. The right multiplication is subtler: the identity $R_{x^{\dagger}} = R_x^{*}$ is the third identity $\langle yx,z\rangle = \langle y,zx^{\dagger}\rangle$ refused above, it holds for the trace form $\langle x,y\rangle = \tau(x^{\dagger}y)$ because $\tau$ is cyclic, and in general the adjoint of $R_x$ is the right multiplication by the **transpose** $x^{t}$, defined by $\langle yx,z\rangle = \langle y,zx^{t}\rangle$ and equal to $x^{\dagger}$ only for the trace form; the computation is in *The Form-Adjoint of the Multiplications*.

The two identities are the adjoint axiom in operator form, and they are the origin of the operator theory of the layer. They hold for a form of any signature and over any commutative base with an involution.

### The Correspondence

**Proposition.** The form and the involution determine each other through the functional $\varphi = \langle \cdot, 1\rangle$:

$$
\langle x, y \rangle = \langle x^{\dagger}y, 1 \rangle .
$$

**Proof.** Apply the adjoint axiom with $y$ replaced by $x^{\dagger}y$ and $z = 1$, and use $(x^{\dagger}y)^{\dagger} = y^{\dagger}x$. Conversely, a $\sigma$-linear functional $\varphi$ on $A$ produces the Hermitian form $h_\varphi(x, y) = \varphi(y^{\dagger}x)$, and the two constructions are inverse. This is the correspondence of *The Sesquilinear Form and the Conjugation*, stated here for the involution of the algebra; it uses neither positivity nor completeness.

## The Dagger of a Clifford Algebra

The algebras of the category carry their involution intrinsically. With the $\mathbb{Z}/2$-grading $A = A^0 \oplus A^1$ and the grade involution $\alpha$ acting by $\alpha(x) = (-1)^k x$ on the degree-$k$ part, two anti-involutions are defined on every coefficient ring:

- **reversion** $x^{r}$, the anti-automorphism fixing each vector;
- the **conjugate** $x^{\natural} = \alpha(x^{r})$, which negates each vector.

They agree on the even part and differ on the odd part, their signs on a $k$-blade being $(-1)^{k(k-1)/2}$ and $(-1)^{k(k+1)/2}$. The involution $\sigma$ of the base acts on the coefficients and commutes with both. The **dagger** is the composite

$$
x^{\dagger} = \sigma(\alpha(x^{r})) = \sigma(x^{\natural}),
$$

an anti-automorphism of order two, and the **conjugate reversion** $x^{r,\sigma} = \sigma(x^{r})$ is the other anti-involution of order two, the two being related by $x^{\dagger} = \alpha(x^{r,\sigma})$. The construction, the table of signs, the Klein four-group on the biquaternions and the trace form $\tau(x^{\dagger}y)$ are *Hilbert Algebras*; the point taken here is that they are available over every commutative base and use no positivity.

**Example.** For the biquaternions $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} \cong M_2(\mathbb{C})$ the conjugations ${}^{\natural}$, $\sigma$ and $\bar{\cdot}$ commute and $\bar{\cdot} = \sigma\circ{}^{\natural}$ is the dagger; the form $\operatorname{Trd}(\tilde P\bar{\tilde Q})$ is the Hermitian one, while $\operatorname{Trd}(\tilde P\tilde Q)$ is the symmetric form of the ordinary trace. The difference between the two is exactly the dagger, and it is stated in *Hilbert Algebras*.

## The Self-Adjoint and Skew Elements

The involution cuts the algebra in two. An element is **self-adjoint** when $x^{\dagger} = x$ and **skew-adjoint** when $x^{\dagger} = -x$, and the involution is $F$-semilinear, so the self-adjoint elements form a module over the fixed ring $F^\sigma$ and the skew-adjoint elements another. When $2$ is invertible in $F$ every element decomposes uniquely,

$$
x = \tfrac{1}{2}\bigl(x + x^{\dagger}\bigr) + \tfrac{1}{2}\bigl(x - x^{\dagger}\bigr),
$$

into a self-adjoint part and a skew-adjoint part. The decomposition is the algebraic substitute for the splitting of a complex number into a real part and an imaginary part, and it carries no order.

For every $x$ the products $x^{\dagger}x$ and $xx^{\dagger}$ are self-adjoint, $(x^{\dagger}x)^{\dagger} = x^{\dagger}x$, and the diagonal of the form reads $q(x) = \langle x^{\dagger}x, 1\rangle$ by the correspondence. These elements are the **Hermitian squares** of the algebra, and the set of their finite sums is the algebraic positive cone of *Hermitian Squares and the Algebraic Positive Cone*. Whether that cone meets its negative only at $0$ is the question of the positivity of the involution, and it is the question that decides whether the algebra is a *Hilbert Algebra*; it is Part II's.

## The Radical and Non-Degeneracy

**Definition.** The **left radical** and the **right radical** of the form are

$$
\operatorname{rad}_l = \{x : \langle x, y\rangle = 0 \ \text{for all } y\}, \qquad \operatorname{rad}_r = \{x : \langle y, x\rangle = 0 \ \text{for all } y\},
$$

and the form is **non-degenerate** when the common radical vanishes.

**Proposition.** For a Hermitian form the two radicals coincide, $\operatorname{rad}_l = \operatorname{rad}_r = \operatorname{rad}$, and the common radical is a left ideal and a right ideal. If the form is associative, in the sense that $\langle xy, z\rangle = \langle x, yz\rangle$ for all $x, y, z$, then the radical is a two-sided ideal.

**Proof.** Since the form is Hermitian, $\langle x, y\rangle = \sigma(\langle y, x\rangle)$ with $\sigma$ an involution, so $\langle x, y\rangle = 0$ is equivalent to $\langle y, x\rangle = 0$ and the two radicals coincide. If $x \in \operatorname{rad}$ and $a \in A$ then $\langle ax, y\rangle = \langle x, a^{\dagger}y\rangle = 0$ for every $y$, so $ax \in \operatorname{rad}$ and the radical is a left ideal; if the form is associative then also $\langle xa, y\rangle = \langle x, ay\rangle = 0$, so it is a right ideal as well.

When the radical is a two-sided ideal the form descends to the quotient $A/\operatorname{rad}$, and the descended form is non-degenerate; this is the algebraic reduction that the definite theory never needs, because a positive definite form has a zero radical. The reduction is the companion, on a single algebra, of the passage from an indefinite space to its definite quotient, and the indefinite case is *The Indefinite Case and the Signature*.

## The Isometry Group and the Unitary Slice

**Definition.** An $F$-linear map $T : A \to A$ is an **isometry** of the form when

$$
\langle Tx, Ty \rangle = \langle x, y \rangle \qquad \text{for all } x, y \in A ,
$$

and the isometries form the **isometry group** $\operatorname{Iso}(A, q)$.

The isometry of a form is the solution set of a system of polynomial equations over $F$, so the group is algebraic: it is defined by an equation and not by a distance. Its determinant-one part is written $\operatorname{SIso}(A, q)$, and it is the group of the layer.

**Definition.** The **unitary slice** is the set of elements whose dagger is their inverse,

$$
U = \{x \in A : x^{\dagger}x = xx^{\dagger} = 1\}.
$$

It is a subgroup of the group of units: it is closed under the product because $(xy)^{\dagger}(xy) = y^{\dagger}x^{\dagger}xy = 1$, it contains $1$, and it is closed under inversion because the two defining relations are exchanged by the dagger. On the slice the dagger is the inverse, $x^{\dagger} = x^{-1}$, so the Hermitian sandwich and the inner conjugation agree there and only there; this is the identity that the four operator groups below exploit. The slice, its relation to the compact real form and the definite case are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*.

**Proposition.** An element of the unitary slice acts by an isometry of the algebra under both the inner conjugation and the Hermitian sandwich.

**Proof.** For $u \in U$ and the inner conjugation, $\langle uxu^{-1}, uyu^{-1}\rangle = \langle x, y\rangle$ is the statement that the form is invariant under the automorphism; for the Hermitian sandwich $\Theta_u(z) = uzu^{\dagger}$ the same computation with $u^{\dagger} = u^{-1}$ gives the identity. The two actions therefore agree on the slice, which is the reason the slice is the meeting point of the involutive structure and the orthogonal structure.

## What Belongs Elsewhere

- The **general theory of $\sigma$-sesquilinear and Hermitian forms** over an involution ring — the Gram matrix, congruence, the unitary Witt group and the Wall group — belongs to *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and to *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*.
- The **symmetric and antisymmetric decomposition of a form**, its dictionary of Hermitian, skew-Hermitian and alternating kinds, and the collapse at the trivial involution belong to *The Sesquilinear Form and the Conjugation*.
- The **positivity of the form**, the **positive cone** $\{\sum_i x_i^{\dagger}x_i\}$, **Cauchy–Schwarz**, the **completion** and the **modular theory** are *Hilbert Algebras*, *Self-Adjoint Elements and the Positive Cone* and *The Modular Structure of a Hermitian Algebra* in Part II; nothing of that layer is used here.
- The **operators built from the dagger** — the blade form, the Hermitian sandwich $\Theta_x(y) = xyx^{\dagger}$, the one-sided operators and their signed variants — are the four groups of this category that follow.
- The **Clifford algebra**, its grading, its intrinsic anti-involutions and the trace form are *Clifford Algebras*, *The Grading of the Clifford Algebra with Signed Inner Conjugation* and *Hilbert Algebras*.

## Summary

- A **Hermitian algebra** is an associative algebra with an involution $\bar{\cdot}$ and a non-degenerate Hermitian form tied by the adjoint axiom $\langle xy, z\rangle = \langle y, x^{\dagger}z\rangle$.
- The axiom is $\langle xy, z\rangle = \langle y, x^{\dagger}z\rangle$, equivalently $\langle x^{\dagger}y, z\rangle = \langle y, xz\rangle$; it says that $L_{x^{\dagger}} = L_x^{*}$. The third identity $\langle xy, z\rangle = \langle x, zy^{\dagger}\rangle$, equivalently $R_{x^{\dagger}} = R_x^{*}$, is not a consequence: it is the cyclicity of the functional of the form, and it holds for the trace form.
- The form and the involution determine each other through $\varphi = \langle \cdot, 1\rangle$, with $\langle x, y\rangle = \langle x^{\dagger}y, 1\rangle$.
- The dagger of a Clifford algebra is the composite $x^{\dagger} = \sigma(\alpha(x^{r}))$ of reversion and the involution of the base, available with no positivity.
- Every element splits as $x = \tfrac12(x + x^{\dagger}) + \tfrac12(x - x^{\dagger})$ into a self-adjoint and a skew-adjoint part, and the Hermitian squares $x^{\dagger}x$ generate the algebraic positive cone.
- The left and the right radicals are a left and a right ideal, and they coincide and are two-sided when the form is associative; the form descends to a non-degenerate form on the quotient.
- The isometry group is algebraic, and the unitary slice $U = \{x : x^{\dagger}x = xx^{\dagger} = 1\}$ is the subgroup on which the dagger is the inverse and the Hermitian sandwich is the inner conjugation.
- Positivity, the cone, the completion and the modular theory are *Hilbert Algebras* and Part II; the operator groups of this category are the four that follow.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A$ | a unital associative algebra |
| $F$, $\sigma$ | the commutative base ring and its involution |
| $x^{\dagger}$ | the involution of $A$, $\sigma$-semilinear over $F$ |
| $x^{r}$, $x^{\natural}$ | reversion and the conjugate $\alpha(x^{r})$ |
| $x^{r,\sigma}$ | the conjugate reversion $\sigma(x^{r})$ |
| $\alpha$ | the grade involution of the $\mathbb{Z}/2$-grading |
| $\langle \cdot, \cdot \rangle$ | the Hermitian form of the algebra |
| $q(x)$ | the diagonal $\langle x, x\rangle$, valued in $F^\sigma$ |
| $\varphi$ | the functional $\langle \cdot, 1\rangle$ of the correspondence |
| $L_x$, $R_x$ | the left and the right multiplication by $x$ |
| $T^{*}$ | the adjoint of $T$ for the form |
| $\operatorname{rad}_l$, $\operatorname{rad}_r$ | the left and the right radical |
| $\operatorname{Iso}(A, q)$ | the isometry group of the form |
| $U$ | the unitary slice $\{x : x^{\dagger}x = xx^{\dagger} = 1\}$ |
| $\Theta_x$ | the Hermitian sandwich $y \mapsto xyx^{\dagger}$ |
| $F^\sigma$ | the fixed ring of the base involution |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for Hermitian forms over a ring with an involution, the adjoint involution and the unitary group.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the non-degenerate case, the radical and the isometry group.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reversion, Clifford conjugation and the dagger on a Clifford algebra.
