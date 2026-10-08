
# __The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint__

## Introduction

The two-sided operators on a Clifford algebra form one family of five members, tabulated in *Two-Sided Operators on a Clifford Algebra*. Four of them are built from the intrinsic anti-involutions of the algebra, reversion and Clifford conjugation, and are available over every commutative base. The fifth is the **Hermitian sandwich**

$$
\Theta_x(y) = x\,y\,x^{\dagger},
$$

and it is the member that needs an involution of the base: the **dagger** $x^{\dagger} = \sigma(\alpha(x^{r}))$ is defined only when the base ring $A$ carries an involution $\sigma$, and it is introduced in *Hermitian Algebras*.

The trade between this member and the four others is exact. The four intrinsic members dress $x$ between a left factor and a right factor that are either an inverse or an intrinsic anti-involution of the algebra; the Hermitian sandwich dresses it between $x$ and the dagger of $x$. Since the dagger is defined on **every** element, $\Theta_x$ is defined for every $x$, invertible or not, and $x \mapsto \Theta_x$ is then a homomorphism of the multiplicative monoid of the algebra rather than of its group of units. In exchange the base and the coefficients enter: the operator is $A$-linear in its argument, it is $\sigma$-semilinear in its parameter up to a norm, and on the **unitary slice** $x^{\dagger}x = 1$ the dagger is the inverse, so the Hermitian sandwich there is the inner conjugation of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* and the two theories meet.

This article treats the operator itself: its domain, its linearity in the argument and in the parameter, its multiplicativity, its parity, its value at the unit, its form on the Clifford group, the elements on which it preserves the quadratic space, and two worked cases. The forms it is built from belong to *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*; the form that makes the algebra a Hilbert space is *The Blade Form and the Hermitian Structure with Hermitian Adjoint*; the slice on which the dagger is the inverse is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the adjoint of the one-sided action on a Clifford module is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; and the biquaternion case, where the sandwich $Q\,x\,Q^{\dagger}$ reproduces the Lorentz action, is *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*.

## The Operator

### Definition and Domain

**Definition.** Let $A$ be a commutative ring with involution $\sigma$, let $q$ be a quadratic form on a free $A$-module $V$, and let $\mathrm{Cl}(V,q)$ be its Clifford algebra. The **Hermitian sandwich** of an element $x \in \mathrm{Cl}(V,q)$ is the map

$$
\Theta_x : \mathrm{Cl}(V,q) \longrightarrow \mathrm{Cl}(V,q), \qquad \Theta_x(y) = x\,y\,x^{\dagger}, \qquad x^{\dagger} = \sigma(\alpha(x^{r})).
$$

The operator is defined for **every** $x \in \mathrm{Cl}(V,q)$. No invertibility is required, and no assumption is made on $x$ beyond that it is an element of the algebra.

In terms of the left and the right multiplications the definition reads

$$
\Theta_x = L_x \circ R_{x^{\dagger}} = R_{x^{\dagger}} \circ L_x,
$$

the two composites agreeing by associativity, and the right factor $x^{\dagger}$ is the **dagger**, the composite of Clifford conjugation with the coefficient involution, $\sigma$-semilinear over $A$ and of order two.

**Remark (the place of the member in the family).** The five members are indexed by the right factor, and the Hermitian sandwich is the last of them.

| member | operator | right factor | defined for |
|---|---|---|---|
| inner conjugation | $x\,y\,x^{-1}$ | $x^{-1}$ | invertible $x$ |
| signed inner conjugation | $\alpha(x)\,y\,x^{-1}$ | $x^{-1}$ | invertible $x$ |
| reversion sandwich | $x\,y\,x^{r}$ | $x^{r}$ | every $x$ |
| conjugation sandwich | $x\,y\,x^{\natural}$ | $x^{\natural}$ | every $x$ |
| Hermitian sandwich | $x\,y\,x^{\dagger}$ | $x^{\dagger}$ | every $x$, needs $\sigma$ |

The two inverse members are defined only on the group of units. The reversion and conjugation sandwiches are defined on the whole algebra and need nothing of the base beyond the algebra itself. The Hermitian sandwich is defined on the whole algebra like the last two, and is the only one of the five that needs the base to carry an involution.

### Linearity: the Argument is Linear, the Parameter is Semilinear

**Proposition.** For every central $a \in A$ and every $x, y$, $\Theta_x(ay) = a\,\Theta_x(y)$ and $\Theta_x(ya) = \Theta_x(y)\,a$. In particular $\Theta_x$ is a map of $A$-$A$-bimodules, and over a field it is $A$-linear.

**Proof.** The dagger is $\sigma$-semilinear over $A$, so $a\,y\,x^{\dagger} = y\,a\,x^{\dagger}$ since $a$ is central; hence $\Theta_x$ is the composite of the left multiplication $L_x$ and the right multiplication $R_{x^{\dagger}}$, both of which are $A$-linear.

**Proposition (the parameter rule).** For every central $a \in A$ and every $x$,

$$
\Theta_{ax} = a\,\sigma(a)\,\Theta_x .
$$

**Proof.** The dagger is $\sigma$-semilinear, so $(ax)^{\dagger} = \sigma(a)\,x^{\dagger}$. Then

$$
\Theta_{ax}(y) = a\,x\,y\,\sigma(a)\,x^{\dagger} = a\,\sigma(a)\,x\,y\,x^{\dagger} = a\,\sigma(a)\,\Theta_x(y),
$$

the middle step by centrality of $a$.

**Remark (a corrected statement of the linearity).** The operator is $A$-linear in the **argument** and picks up $\sigma$ in the **parameter**; it is not $\sigma$-semilinear in the argument. An earlier draft of *Hermitian Algebras* claimed that $\Theta_x$ is $\sigma$-semilinear in $y$, and that claim is false. Over $\mathbb{C}$ let $A = \mathbb{C}$ with complex conjugation, let $V$ be one-dimensional with $e^{2} = -1$, and put $x = 2 + ie$, $a = i$, $y = 1$. Then

$$
\Theta_x(ay) = i\,x\,x^{\dagger} = 5i - 4e, \qquad \Theta_x(y) = x\,x^{\dagger} = 5 + 4ie,
$$

so $\Theta_x(ay) = a\,\Theta_x(y)$ and the operator is $\mathbb{C}$-linear, while $\sigma$-semilinearity would require $\sigma(a)\Theta_x(y) = -5i + 4e$. The two differ, and the linear statement is the true one.

### Multiplicativity

**Proposition.** For all $x, z$,

$$
\Theta_{xz} = \Theta_x \circ \Theta_z .
$$

**Proof.** The dagger is an anti-automorphism, so $(xz)^{\dagger} = z^{\dagger}x^{\dagger}$. Then

$$
\Theta_{xz}(y) = xz\,y\,(xz)^{\dagger} = xz\,y\,z^{\dagger}x^{\dagger} = x\,(z\,y\,z^{\dagger})\,x^{\dagger} = \Theta_x\bigl(\Theta_z(y)\bigr).
$$

**Corollary.** The assignment $x \mapsto \Theta_x$ is a homomorphism from the multiplicative monoid of $\mathrm{Cl}(V,q)$ to the monoid of $A$-linear endomorphisms of $\mathrm{Cl}(V,q)$, with $\Theta_1 = \mathrm{id}$. For invertible $x$ the operator $\Theta_x$ is invertible, with inverse $\Theta_{x^{-1}}$; for non-invertible $x$ it may still be invertible as an endomorphism, but it is not for $x = 0$.

### The Parity

**Proposition.** Let $x$ be homogeneous of parity $\varepsilon = (-1)^{|x|}$ and let $y$ be homogeneous of degree $k$. Then every product $x\,y\,x^{\dagger}$ has parity $\varepsilon \cdot (-1)^{k} \cdot \varepsilon = (-1)^{k}$, so

$$
\Theta_x\bigl(\mathrm{Cl}^{k}\bigr) \subseteq \mathrm{Cl}^{\mathrm{even}} \ \text{if } k \text{ is even}, \qquad \Theta_x\bigl(\mathrm{Cl}^{k}\bigr) \subseteq \mathrm{Cl}^{\mathrm{odd}} \ \text{if } k \text{ is odd}.
$$

If in addition $x$ is even, then $\Theta_x$ preserves the degree, $\Theta_x(\mathrm{Cl}^{k}) \subseteq \mathrm{Cl}^{k}$, because the left factor and the dagger are then sums of even blades and degrees add.

**Proof.** The dagger preserves the degree, so $x^{\dagger}$ has the same parity as $x$. Each product of three homogeneous factors has parity the product of the three parities, which is $\varepsilon^{2}(-1)^{k} = (-1)^{k}$. For even $x$ and even $x^{\dagger}$ the three degrees are even, $k$, even, and they add to $k$.

**Remark.** For a mixed $x$ the operator does not preserve the grading, since the parity of a product $x_i y x_j^{\dagger}$ is $(-1)^{|x_i| + k + |x_j|}$ and the two summands with $|x_i| \neq |x_j|$ have opposite parity.

### The Value at the Unit

**Proposition.** $\Theta_x(1) = x\,x^{\dagger}$, which for $x$ in the Clifford group equals $\sigma(N(x))\,x\,\sigma(x)^{-1}$ and is in particular not a scalar unless $x$ is $\sigma$-real.

The values at the unit separate the five members of the family.

| member | value at $1$ |
|---|---|
| inner conjugation | $1$ |
| signed inner conjugation | $\alpha(x)$, that is $\pm 1$ for homogeneous $x$ |
| reversion sandwich | $x\,x^{r}$ |
| conjugation sandwich | $x\,x^{\natural} = N(x)$, the Clifford norm |
| Hermitian sandwich | $x\,x^{\dagger}$ |

The inner conjugation is the only member that fixes the unit identically; the signed inner conjugation multiplies it by the parity sign; the conjugation sandwich gives the Clifford norm; and the Hermitian sandwich gives the $\sigma$-conjugate of the norm composed with the $\sigma$-unitary part of $x$, as the next section makes precise.

## On the Clifford Group

### The Corrected Identities

**Theorem.** Let $x$ be an element of the Clifford group $\Gamma(V,q)$, with Clifford norm $N(x) = x\,x^{\natural} = x^{\natural}\,x$, a scalar of $A$. Then

$$
x^{\dagger} = \sigma\bigl(N(x)\bigr)\,\sigma(x)^{-1},
\qquad
\Theta_x(y) = \sigma\bigl(N(x)\bigr)\; x\,y\,\sigma(x)^{-1}.
$$

**Proof.** On $\Gamma$ the norm is a scalar, so $x^{\natural} = N(x)x^{-1}$. The dagger is the composite of Clifford conjugation with the ring automorphism $\sigma$, so

$$
x^{\dagger} = \sigma(x^{\natural}) = \sigma\bigl(N(x)\,x^{-1}\bigr) = \sigma\bigl(N(x)\bigr)\,\sigma(x)^{-1},
$$

using that $\sigma$ is multiplicative and that $\sigma(x^{-1}) = \sigma(x)^{-1}$. Substituting into $\Theta_x(y) = x\,y\,x^{\dagger}$ gives the second identity.

**Corollary (the $\sigma$-real case).** If $x \in \Gamma$ satisfies $\sigma(x) = x$, then $\sigma(x)^{-1} = x^{-1}$ and

$$
\Theta_x = \sigma\bigl(N(x)\bigr)\;\mathrm{Ad}_x, \qquad \mathrm{Ad}_x(y) = x\,y\,x^{-1},
$$

a scalar multiple of the inner conjugation. If in addition $x$ is even, then $\alpha(x) = x$ and $\mathrm{Ad}_x$ is the signed inner conjugation $\mathrm{Ad}^{\alpha}_x$, so $\Theta_x = \sigma(N(x))\,\mathrm{Ad}^{\alpha}_x$ there.

**Remark (an earlier error, corrected).** The identity $x^{\dagger} = \sigma(N(x))\,x^{-1}$ is false in general, and so is the identity $\Theta_x = \sigma(N(x))\,\mathrm{Ad}^{\alpha}_x$. The two sides differ by $\sigma(x)^{-1}$ against $x^{-1}$, and these agree only when $x$ is $\sigma$-real; a homogeneous but non-$\sigma$-real $x$ is a counterexample. Concretely, over $\mathbb{C}$ in the algebra with $e^{2} = -1$, let $x = 2 + ie$. Then $N(x) = 3$ and $x^{\dagger} = 2 + ie$, while the incorrect formula returns

$$
\sigma\bigl(N(x)\bigr)\,x^{-1} = 3\cdot\tfrac{1}{3}(2 - ie) = 2 - ie \neq x^{\dagger}.
$$

The corrected formula returns $3\cdot \frac{1}{3}(2 + ie) = 2 + ie = x^{\dagger}$. The same correction was recorded in *Hermitian Algebras*, where the two identities were first written.

### The Unitary Slice

**Definition.** The **unitary slice** of the algebra is

$$
U = \{\, x \in \mathrm{Cl}(V,q) : x^{\dagger}x = 1 \,\}.
$$

**Proposition.** $U$ is a subgroup of the group of units. It contains $1$; if $x \in U$ then $x$ is invertible with $x^{-1} = x^{\dagger}$, and $x^{\dagger} \in U$; if $x, y \in U$ then

$$
(xy)^{\dagger}(xy) = y^{\dagger}x^{\dagger}x\,y = y^{\dagger}y = 1 .
$$

**Proof.** The three statements are the computation displayed together with $x\,x^{\dagger} = x\,(x^{\dagger}x)\,x^{-1} = 1$ for an invertible $x$; in finite dimension a left inverse is an inverse, and $(x^{\dagger})^{\dagger} = x$ gives $x^{\dagger} \in U$.

**Corollary (where the two theories meet).** On $U$ the dagger is the inverse, so the Hermitian sandwich **is** the inner conjugation:

$$
x \in U \ \Longrightarrow \ \Theta_x(y) = x\,y\,x^{-1} = \mathrm{Ad}_x(y).
$$

This is the sense in which the Hermitian sandwich is the inverse sandwich of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* on the slice where the dagger is invertible. The slice is studied in *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*.

**Proposition (the case of the identity involution).** When $\sigma = \mathrm{id}$ the dagger is Clifford conjugation, $x^{\dagger} = x^{\natural}$, and

$$
U = \{\, x : N(x) = 1 \,\} = \mathrm{Pin}(V,q).
$$

**Proof.** If $x^{\natural}\,x = 1$ then $N(x) = x\,x^{\natural} = x\,(x^{\natural}\,x)\,x^{-1} = 1$. Conversely if $x\,x^{\natural} = 1$ then $x^{\natural} = x^{-1}$, so $x^{\natural}\,x = 1$. Hence $U = \{x : N(x) = 1\}$, the definition of the Pin group.

## Preservation of the Quadratic Space

**Proposition.** Let $x \in \Gamma(V,q)$. Then $\Theta_x$ maps the vector space $V$ to itself, and

$$
\Theta_x\big|_{V} = \sigma\bigl(N(x)\bigr)\cdot\chi(x),
$$

where $\chi(x) \in \mathrm{O}(V,q)$ is the twisted conjugation $v \mapsto \pm\,x\,v\,x^{-1}$. Consequently $\Theta_x$ is an isometry of $V$ exactly when $\sigma(N(x))^{2} = 1$, and otherwise it is a similarity of ratio $\sigma(N(x))^{2}$.

**Proof.** On $\Gamma$ the map $v \mapsto x\,v\,\alpha(x)^{-1}$ lands in $V$ and preserves $q$, by the definition of the Clifford group, and for homogeneous $x$ it differs from $v \mapsto x\,v\,x^{-1}$ by the sign $\alpha(x)x^{-1} = \pm 1$; the identity of the theorem then gives the displayed form. A scalar $\lambda$ multiplies $q$ by $\lambda^{2}$.

**Corollary.** The Hermitian sandwich produces no isometry of $V$ beyond the orthogonal group. Every isometry it yields is the inner conjugation of a $\Gamma$-element, up to a global sign, and those generate $\mathrm{O}(V,q)$ already. What the Hermitian member adds is not new isometries but the wider domain, the action of the coefficient involution, and the positivity of the next article.

**Remark (the degenerate case).** For $x \notin \Gamma$ the operator need not map $V$ to $V$; the element $x = 2 + e_2$ of the algebra with $e_2^{2} = -1$ has $\Theta_x(e_2) \notin V$. The general statement of the theorem is therefore confined to the Clifford group.

## Worked Cases

### An Odd Element with Complex Coefficients

Let $A = \mathbb{C}$ with complex conjugation, let $V = \mathbb{C}$ with $e^{2} = -1$, so that $\mathrm{Cl}(V,q)$ has basis $1, e$, and let $x = 2 + ie$. Then

$$
x^{\natural} = \alpha(2 + ie) = 2 - ie, \qquad x^{\dagger} = \sigma(x^{\natural}) = 2 + ie, \qquad N(x) = x\,x^{\natural} = 3 .
$$

The operator is $\Theta_x(y) = x\,y\,(2 + ie)$. On the two basis elements,

$$
\Theta_x(1) = (2+ie)^{2} = 5 + 4ie, \qquad \Theta_x(e) = (2+ie)\,e\,(2+ie) = -4i + 5e,
$$

and on the scalar $a = i$ it gives $\Theta_x(i) = i(5+4ie) = 5i - 4e$, the value used above to refute $\sigma$-semilinearity in the argument. On the unit, the corrected Clifford-group identity reads $x^{\dagger} = \sigma(N(x))\sigma(x)^{-1} = 3\cdot\frac{1}{3}(2+ie) = 2+ie$, while the incorrect formula $3 x^{-1}$ gives $2 - ie$.

### An Even Element and a Similarity

Let $q$ be the form on $\mathbb{R}^{2}$ with $e_1^{2} = 1$, $e_2^{2} = -1$, and let $x = 2 + 3e_1e_2$, an even element. Then $x^{\natural} = 2 - 3e_1e_2$ and, since $(e_1e_2)^{2} = 1$ in this algebra,

$$
N(x) = (2 + 3e_1e_2)(2 - 3e_1e_2) = 4 - 9 = -5 .
$$

The norm is a real scalar other than $\pm 1$, so $x \in \Gamma$ but $\Theta_x = -5\,\mathrm{Ad}^{\alpha}_x$ is a similarity and not an isometry. On the unit, $\Theta_x(1) = -5$; on the vector $e_1$, computed exactly,

$$
\Theta_x(e_1) = 13e_1 - 12e_2, \qquad \Theta_x(e_2) = -12e_1 + 13e_2,
$$

so that $q(\Theta_x(e_1)) = 13^{2} - 12^{2} = 25 = (-5)^{2}q(e_1)$: the operator scales both quadratic forms by the factor $25$ and preserves neither, exactly as the proposition requires of a similarity whose scalar is not a sign. The same computation with $x = e_1$, where $N(e_1) = -1$ and $\sigma(N)^{2} = 1$, gives $\Theta_{e_1}(e_1) = -e_1$ and $\Theta_{e_1}(e_2) = e_2$, an honest isometry of the quadratic space.

## Summary

The **Hermitian sandwich** is the fifth member of the two-sided family of *Two-Sided Operators on a Clifford Algebra*,

$$
\Theta_x(y) = x\,y\,x^{\dagger}, \qquad x^{\dagger} = \sigma(\alpha(x^{r})),
$$

the member whose right factor is the dagger and which therefore needs an involution $\sigma$ of the base, introduced in *Hermitian Algebras*. It is defined for **every** element of the algebra, invertible or not, because the dagger is. It is $A$-linear in its argument $y$, and in its parameter it obeys $\Theta_{ax} = a\sigma(a)\Theta_x$; it is **not** $\sigma$-semilinear in the argument, and the earlier claim to that effect is corrected, with the counterexample $\Theta_x(i) = 5i-4e$ over $\mathbb{C}$. It is multiplicative, $\Theta_{xz} = \Theta_x \circ \Theta_z$, so $x \mapsto \Theta_x$ is a monoid homomorphism into the endomorphisms, which is the structural gain over the inverse sandwiches: the operators are defined on all of the algebra, and the invertibility migrates to the unitary slice. For homogeneous $x$ the operator preserves the parity, and for even $x$ it preserves the degree. Its value at the unit is $\Theta_x(1) = x\,x^{\dagger}$.

On the Clifford group the identities are $x^{\dagger} = \sigma(N(x))\,\sigma(x)^{-1}$ and $\Theta_x = \sigma(N(x))\,x(\cdot)\sigma(x)^{-1}$; the simpler $x^{\dagger} = \sigma(N(x))x^{-1}$ and $\Theta_x = \sigma(N(x))\mathrm{Ad}^{\alpha}_x$ hold only for $\sigma$-real $x$, and the failure for a non-$\sigma$-real homogeneous element is worked out. On the **unitary slice** $U = \{x : x^{\dagger}x = 1\}$, which is a group and equals $\mathrm{Pin}(V,q)$ when $\sigma = \mathrm{id}$, the dagger is the inverse and the Hermitian sandwich is exactly the inner conjugation, so the two theories meet there. On the Clifford group the operator maps $V$ to $V$ as $\sigma(N(x))$ times a twisted conjugation, so it is an isometry of the quadratic space precisely when $\sigma(N(x))^{2} = 1$, and it gives no isometries of $V$ beyond the orthogonal group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\sigma$ | Commutative base ring with involution |
| $\mathrm{Cl}(V,q)$ | Clifford algebra of the quadratic space $(V,q)$ |
| $x^{r}$ | Reversion |
| $\alpha$ | Grade involution |
| $x^{\natural} = \alpha(x^{r})$ | Clifford conjugation |
| $x^{\dagger} = \sigma(\alpha(x^{r}))$ | Dagger, the right factor of the operator |
| $\Theta_x(y) = x\,y\,x^{\dagger}$ | Hermitian sandwich |
| $L_x$, $R_x$ | Left and right multiplication by $x$ |
| $\Theta_{ax} = a\sigma(a)\Theta_x$ | Parameter rule, $a$ central |
| $\Gamma(V,q)$, $N(x) = x x^{\natural}$ | Clifford group and Clifford norm |
| $\mathrm{Ad}_x(y) = x\,y\,x^{-1}$ | Inner conjugation |
| $\mathrm{Ad}^{\alpha}_x(y) = \alpha(x)\,y\,x^{-1}$ | Signed inner conjugation |
| $U = \{x : x^{\dagger}x = 1\}$ | Unitary slice |
| $\chi(x)$ | Twisted conjugation $v \mapsto \pm x\,v\,x^{-1}$ on $V$ |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for Hermitian forms over rings with involution and the unitary groups.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution, the dagger, and the anti-involutions of a Clifford algebra.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the classical theory of Hermitian forms and their isometry groups.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works 2 (Springer, 1997), for the Clifford group, the norm and the twisted conjugation on the vector space.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Clifford groups and the unitary structures over the classical division algebras.
