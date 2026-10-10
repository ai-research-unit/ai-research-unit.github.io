# __Introduction to the Remarkable Subspaces__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four conjugations, and each of them is an involution. Each one splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and the eight spaces so obtained reduce to six distinct subspaces, the **remarkable subspaces** of $\mathbb{B}$. The conjugations themselves are not the subject of this article: their definitions are in *Biquaternions as a Vector Space over $\mathbb{C}$*, the group they form is in *The Group of Involutions* and the two spaces each defines are in *Comparison of the Remarkable Subspaces*.

This article is the single article of the group for the remarkable subspaces, one to a section. Each section gives the defining condition of the subspace, the coordinate condition it amounts to, the real basis that exhibits it and its real dimension; the elements of the subspace — which of them are units, which are zero divisors, which roots of the three central values lie in it; and the structure it carries — the idempotents that lie in it and the minimal one-sided ideals it determines. The idempotents and the ideals of the algebra are classified once, in §*The Idempotents and the Ideals in the Remarkable Subspaces*, and read on the remarkable subspaces there. The table is the summary; the sections are the detail.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | role |
|---|---|---|---|---|
| the centre $\mathbb{C}_{\mathbb{B}}$ | $\tilde{Q}^{\natural} = \tilde{Q}$ | $e_0, ie_0$ | $2$ | the centre of the algebra, a field |
| the vector subspace $\mathrm{Vect}(\mathbb{B})$ | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $e_1, e_2, e_3, ie_1, ie_2, ie_3$ | $6$ | the kernel of the scalar part, a Lie algebra |
| the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0, e_1, e_2, e_3$ | $4$ | a division algebra |
| the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = -\tilde{Q}$ | $ie_0, ie_1, ie_2, ie_3$ | $4$ | a module over $\mathbb{H}_{\mathbb{B}}$ |
| the Hermitian subspace $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | $e_0, ie_1, ie_2, ie_3$ | $4$ | a Jordan algebra |
| the anti-Hermitian subspace $\mathbb{M}_-$ | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_0, e_1, e_2, e_3$ | $4$ | a Lie algebra |

The remarkable subspaces are pairwise distinct. Their relations — the coordinate blocks out of which they are built, their pairwise intersections, their sums, the action of the four conjugations and the action of the central imaginary unit — are the subject of *Comparison of the Remarkable Subspaces*, and are not treated here. The three eigenspace decompositions the conjugations cut out are *Decompositions Along the Remarkable Subspaces*. The product and its two halves, the Jordan algebra and the Lie algebra, the symmetrized product and the trace form are the business of *Remarkable Subspaces and the Four General Products* and *The 12 Products of the Biquaternion Complex Space*; the four forms on the remarkable subspaces are the business of the five *Remarkable Subspaces under ...* articles and of *The Four Pairings of the Biquaternion Algebra*; the two matrix realizations are the business of *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* and *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*.

Nothing below is a physical statement. The elements are written $\tilde{Q}, \tilde{R}, \tilde{P}, \dots$, their complex coefficients $Q_0, Q_1, Q_2, Q_3$, and the real and imaginary parts of a coefficient $Q_\mu = q_\mu + i q'_\mu$; no other coordinates are used.

## The Centre Subspace

**Definition.** The **centre subspace** $\mathbb{C}_{\mathbb{B}}$ is the fixed space of quaternion conjugation,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = \tilde{Q} \right\} .
$$

**Coordinate condition.** Writing $\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ and comparing the two sides of $\tilde{Q}^{\natural} = \tilde{Q}$ coefficient by coefficient, the coefficient of $e_0$ gives no condition while the coefficient of $e_k$ gives $-Q_k = Q_k$, that is $Q_k = 0$, for $k = 1, 2, 3$. The subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_0e_0 , \qquad Q_0 \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $e_0, ie_0$ and $\dim_{\mathbb{R}}\mathbb{C}_{\mathbb{B}} = 2$. In the eight real coordinates it is the coordinate plane $q_1 = q_2 = q_3 = q'_1 = q'_2 = q'_3 = 0$.

**Role.** It is the centre of the algebra, the set of elements that commute with every element, and it is a commutative subalgebra isomorphic to $\mathbb{C}$; it is one of the two of the remarkable subspaces that are closed under the product. Its elements are the **central elements**, written $Ae_0$ with $A \in \mathbb{C}$.

**The norm and the non-units.** The norm of a central element is the square of its complex coordinate:

$$
N(Ae_0) = A^2 , \qquad (Ae_0)^{-1} = A^{-1}e_0 \quad (A \neq 0) .
$$

Every nonzero central element is a unit, so the centre has no nonzero zero divisor, and it is the field $\mathbb{C}_{\mathbb{B}}$; its only non-unit is $0$. The zero divisors of the algebra avoid the centre entirely.

**The idempotents and the ideals.** A central element $Ae_0$ satisfies $A^2 = A$ only for $A \in \{0,1\}$, so the centre carries the trivial pair $0, e_0$ and no nontrivial idempotent. A nonzero central element is invertible, so the centre determines no minimal ideal and generates the two-sided ideal $\mathbb{B}$, since $e_0 \in \mathbb{C}_{\mathbb{B}}$. A central idempotent $e$ gives the Peirce decomposition $\mathbb{B} = \mathbb{B}e \oplus \mathbb{B}(e_0-e)$, which for a central $e$ is a product of algebras, $\mathbb{B} = \mathbb{B}e \times \mathbb{B}(e_0-e)$; for the simple algebra $\mathbb{B}$ that is possible only when one factor is zero, so the Peirce decomposition relative to a central idempotent is trivial, which is the same fact as simplicity read through the centre.

**The roots.** A central element is $\tilde\Xi = Q_0e_0$ with $Q_0 \in \mathbb{C}$, and $\tilde\Xi^2 = Q_0^2e_0 = -e_0$ holds exactly when $Q_0^2 = -1$, that is $Q_0 = \pm i$. The centre contains the two trivial roots and nothing else,

$$
\tilde\Xi = \pm ie_0 = \pm i .
$$

These are the only roots of $-1$ with a nonvanishing scalar part, and so the only ones that are not pure and the only ones that lie outside the vector subspace.

## The Vector Subspace

**Definition.** The **vector subspace** $\mathrm{Vect}(\mathbb{B})$ is the anti-fixed space of quaternion conjugation,

$$
\mathrm{Vect}(\mathbb{B}) = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** Comparing coefficients, the condition is $Q_0 = 0$: the scalar part vanishes, and the subspace is the kernel of the scalar-part functional $\operatorname{Sc}(\tilde{Q}) = Q_0 = \tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$,

$$
\tilde{Q} = Q_1e_1 + Q_2e_2 + Q_3e_3 , \qquad Q_1, Q_2, Q_3 \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $e_1, e_2, e_3, ie_1, ie_2, ie_3$ and $\dim_{\mathbb{R}}\mathrm{Vect}(\mathbb{B}) = 6$. It is the largest of the remarkable subspaces, and the only one of dimension $6$.

**Role.** It is not a subalgebra, since the product of two pure vectors has a scalar part; it is closed under the commutator, the bracket of two pure vectors being twice their cross product. It splits into the real vector triple $\operatorname{span}\{e_1,e_2,e_3\}$ and the imaginary vector triple $\operatorname{span}\{ie_1,ie_2,ie_3\}$, and its elements are the **pure vectors**, written $\mathbf{Q}$.

**The norm and the zero divisors.** The norm of a pure vector is the complex dot product of the vector with itself:

$$
N(\mathbf{P}) = (\mathbf{P},\mathbf{P}) = P_1^2 + P_2^2 + P_3^2 .
$$

A pure vector is a unit exactly when $(\mathbf{P},\mathbf{P}) \neq 0$. Since a pure vector satisfies $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$, the nonzero non-units of the vector subspace are exactly its **square-zero** elements:

$$
(\mathbf{P},\mathbf{P}) = 0 \iff \mathbf{P}^2 = 0 .
$$

An explicit example is $\mathbf{P} = e_1 + ie_2$, whose square vanishes: $(e_1 + ie_2)^2 = -e_0 + ie_3 - ie_3 + e_0 = 0$. Writing the complex vector as $\boldsymbol{\rho} + i\boldsymbol{\rho}'$ with $\boldsymbol{\rho}, \boldsymbol{\rho}'$ real,

$$
(\mathbf{P},\mathbf{P}) = (\boldsymbol{\rho},\boldsymbol{\rho}) - (\boldsymbol{\rho}',\boldsymbol{\rho}') + 2i(\boldsymbol{\rho},\boldsymbol{\rho}') ,
$$

so that the condition is the pair of real equations $(\boldsymbol{\rho},\boldsymbol{\rho}) = (\boldsymbol{\rho}',\boldsymbol{\rho}')$ and $(\boldsymbol{\rho},\boldsymbol{\rho}') = 0$. **A pure vector is a zero divisor exactly when its two real parts are orthogonal and of equal length.** Writing $\boldsymbol{\rho} = r\hat{u}$ and $\boldsymbol{\rho}' = r\hat{v}$ with $r > 0$ and $\hat{u}, \hat{v}$ an orthonormal pair of directions, the zero divisors of the vector subspace are the elements $r(\hat{u} + i\hat{v})$: a four-parameter family, cut out by two real equations in the six real coordinates. The conjugation $\mathbf{P}^{\natural} = -\mathbf{P}$ is nonzero whenever $\mathbf{P}$ is, so for a square-zero $\mathbf{P}$ the pair $\mathbf{P}, -\mathbf{P}$ is a pair of nonzero elements with vanishing product: **every zero divisor of the vector subspace is its own annihilating partner**. This is the property that the two Hermitian subspaces do not share, and the reason the pure and the non-pure family are kept apart throughout.

**The idempotents and the ideals.** The vector subspace has one idempotent, $0$. A pure vector with $\mathbf{P}^2 = \mathbf{P}$ would have $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$ central and equal to the pure vector $\mathbf{P}$, so $\mathbf{P} \in \mathbb{C}_{\mathbb{B}} \cap \mathrm{Vect}(\mathbb{B}) = 0$. It therefore has square-zero elements and no idempotent; an element that is a projection never has a pure vector part without a scalar part. Through a nonzero nilpotent $\mathbf{P}$ the subspace determines the minimal ideal $\mathbb{B}\mathbf{P}$ and the annihilator $I_{\mathbf{P}}$, and for a nilpotent the two coincide, $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ and $\mathbf{P}\mathbb{B} = J_{\mathbf{P}}$, by §*The Idempotents and the Ideals in the Remarkable Subspaces*. An explicit case is $\mathbf{P} = e_1 + ie_2$, with

$$
\mathbb{B}\mathbf{P} = I_{\mathbf{P}} = \operatorname{span}_{\mathbb{R}}\left\{e_1 + ie_2,\; e_2 - ie_1,\; e_0 - ie_3,\; e_3 + ie_0\right\},
$$

the first two elements being further nilpotents of the vector subspace and the last two a Hermitian element and $i$ times it. This minimal ideal is the sum of a complex line of the vector subspace, a real line of $\mathbb{M}_+$ and a real line of $\mathbb{M}_-$; it contains no basis element of the algebra, so it is not a sum of coordinate blocks and it is not one of the remarkable subspaces.

**The roots.** A pure element is $\tilde\Xi = \mathbf{P} = P_1e_1 + P_2e_2 + P_3e_3$ with complex coefficients, and $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$, so $\tilde\Xi^2 = -e_0$ is the single complex equation

$$
(\mathbf{P},\mathbf{P}) = P_1^2 + P_2^2 + P_3^2 = 1 .
$$

Its solutions are the **pure roots**, and the whole of them, of both kinds, lies here: the vector subspace contains every root of $-1$ that is not one of the trivial pair. In the real and imaginary parts the equation is the pair $(\boldsymbol{\rho},\boldsymbol{\rho}) - (\boldsymbol{\rho}',\boldsymbol{\rho}') = 1$ and $(\boldsymbol{\rho},\boldsymbol{\rho}') = 0$, whose solutions with $\boldsymbol{\rho}' = 0$ are the **real roots**, the vectors $\boldsymbol{\rho}$ of length one, a two-parameter family, and whose solutions with $\boldsymbol{\rho}' \neq 0$ are the **non-trivial roots**, a four-parameter family, the two real parts orthogonal and their squared lengths differing by one,

$$
(\boldsymbol{\rho},\boldsymbol{\rho}) = (\boldsymbol{\rho}',\boldsymbol{\rho}') + 1 , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}') = 0 .
$$

The vector subspace is the only one of the remarkable subspaces in which all three central equations have solutions: the roots of $-1$ as units, the nilpotents $\mathbf{P}^2 = 0$ as the pure solutions of $(\mathbf{P},\mathbf{P}) = 0$, and the roots of $+1$ as the pure solutions of $(\mathbf{P},\mathbf{P}) = -1$. So $\mathrm{Vect}(\mathbb{B})$ carries roots of $-1$ as units and roots of $0$ as zero divisors at the same time, the two opposite kinds of element of the algebra meeting in this one subspace.

## The Quaternion Subspace

**Definition.** The **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ is the fixed space of complex conjugation,

$$
\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be fixed by complex conjugation, that is, that each be real, $Q_\mu = q_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $e_0, e_1, e_2, e_3$ and $\dim_{\mathbb{R}}\mathbb{H}_{\mathbb{B}} = 4$. It is the copy of the real quaternion algebra inside $\mathbb{B}$.

**Role.** It is a subalgebra, the second of the two of the remarkable subspaces that are closed under the product, and it is a division algebra: every non-zero element is a unit. It is the only one of the remarkable subspaces that is non-commutative, and it is the image of the structure map $\mathbb{H} \to \mathbb{B}$, $h \mapsto he_0$.

**The norm and the non-units.** On the quaternion subspace the coefficients are real, so the norm is a sum of four squares:

$$
N(h) = h_0^2 + h_1^2 + h_2^2 + h_3^2 , \qquad N(h) = 0 \iff h = 0 .
$$

Every nonzero element of the quaternion subspace is therefore a unit, and the subspace is a **division algebra**, as it must be: it is the image of the real quaternion algebra, which is a division algebra, under $h \mapsto he_0$. The inverse of $h$ is $h^{\natural}/N(h)$ with $N(h) > 0$ real, the classical formula. The quaternion subspace is one of the three without a nonzero zero divisor, and the only one of them that is not commutative; among the subspaces of the remarkable subspaces it is the one whose non-units are the fewest: only $0$.

**The idempotents and the ideals.** The quaternion subspace has the two trivial idempotents and no others:

$$
0 , \qquad e_0 .
$$

For $h \in \mathbb{H}_{\mathbb{B}}$, the equation $h^2 = h$ reads $h(h - e_0) = 0$, and the quaternion subspace is a division algebra, so $h = 0$ or $h = e_0$. This is the argument that the anti-quaternion subspace cannot use — it is not a division algebra, nor even closed under the product — and it is the reason the two quaternion subspaces reach the same trivial answer by different routes. On the ideal side the quaternion subspace is the sharpest of the three negative cases: not merely the subspace as a whole, but **every single nonzero element** of $\mathbb{H}_{\mathbb{B}}$ is a unit, so every one of them generates the whole algebra on both sides, and the ideal theory sees nothing of the subspace beyond the identity element it shares with the centre and with $\mathbb{M}_+$. The subspace is closed under the product — one of the two of the remarkable subspaces that are, the centre being the other — but it is not an ideal: $ie_1 \in \mathbb{B}$ and $e_1 \in \mathbb{H}_{\mathbb{B}}$ give $ie_1e_1 = -i \notin \mathbb{H}_{\mathbb{B}}$.

**The roots.** A real quaternion is $\tilde\Xi = h_0e_0 + \boldsymbol{\rho}$ with $h_0 \in \mathbb{R}$ and $\boldsymbol{\rho}$ a **real** vector, and its square is $(h_0^2 - (\boldsymbol{\rho},\boldsymbol{\rho}))e_0 + 2h_0\boldsymbol{\rho}$. Setting this equal to $-e_0$ gives the pair $2h_0\boldsymbol{\rho} = 0$ and $h_0^2 - (\boldsymbol{\rho},\boldsymbol{\rho}) = -1$. The first equation gives $\boldsymbol{\rho} = 0$ or $h_0 = 0$. With $\boldsymbol{\rho} = 0$ the second reads $h_0^2 = -1$, impossible for a real $h_0$; with $h_0 = 0$ it reads $(\boldsymbol{\rho},\boldsymbol{\rho}) = 1$. So the roots of $-1$ in the quaternion subspace are

$$
\tilde\Xi = \boldsymbol{\rho} , \qquad \boldsymbol{\rho} \in \mathbb{R}^3 , \quad (\boldsymbol{\rho},\boldsymbol{\rho}) = 1 ,
$$

the **real unit vectors** and nothing else. These are the classical imaginary units of the quaternions, and their absence of a scalar part is what excludes the trivial roots: $\pm i$ has vanishing vector part and is not a real quaternion.

## The Anti-Quaternion Subspace

**Definition.** The **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed space of complex conjugation,

$$
i\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be negated by complex conjugation, that is, that each be purely imaginary, $Q_\mu = iq'_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $ie_0, ie_1, ie_2, ie_3$ and $\dim_{\mathbb{R}}i\mathbb{H}_{\mathbb{B}} = 4$.

**Role.** Its elements are exactly the products $i\tilde{P}$ with $\tilde{P} \in \mathbb{H}_{\mathbb{B}}$, so the subspace is the image of $\mathbb{H}_{\mathbb{B}}$ under multiplication by the central imaginary unit. It is not a subalgebra — the product of two of its elements lands in the quaternion subspace — but it is a two-sided module over $\mathbb{H}_{\mathbb{B}}$. It splits into the imaginary scalar line $\mathbb{R}(ie_0)$ and the imaginary vector triple $\operatorname{span}\{ie_1,ie_2,ie_3\}$.

**The norm and the non-units.** An element of the anti-quaternion subspace is $i$ times a real quaternion, and the norm is the negative of a sum of four squares:

$$
N(ih) = -N(h) = -(h_0^2 + h_1^2 + h_2^2 + h_3^2) , \qquad N(ih) = 0 \iff h = 0 .
$$

Every nonzero element is therefore a unit, with inverse $(ih)^{-1} = -(i h^{\natural})/N(h)$; the subspace has no nonzero zero divisor although it is not closed under the product. Its elements are the negatives, up to the central unit, of the elements of the quaternion subspace, which is the reason the criterion is the same apart from the sign.

**The idempotents and the ideals.** The anti-quaternion subspace has one idempotent, $0$. An element of it is $ih$ with $h$ real, and $(ih)^2 = -h^2$ is a real quaternion; an idempotent there would satisfy $\tilde\Pi = \tilde\Pi^2 \in \mathbb{H}_{\mathbb{B}}$ and therefore lie in $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} = 0$. The subspace consists of units and zero, so it contributes nothing to the idempotent theory of the algebra. For the ideals, multiplication by the central unit $i$ carries $\mathbb{H}_{\mathbb{B}}$ bijectively to $i\mathbb{H}_{\mathbb{B}}$ and preserves products and linear combinations, so everything said of the quaternion subspace holds of it verbatim: every nonzero element is a unit, no zero divisor lies in it, and every nonzero element generates $\mathbb{B}$ on both sides. It is not an ideal: $e_1 \in \mathbb{B}$ and $ie_1 \in i\mathbb{H}_{\mathbb{B}}$ give $e_1 \cdot ie_1 = -i \notin i\mathbb{H}_{\mathbb{B}}$.

**The roots.** An element of $i\mathbb{H}_{\mathbb{B}}$ is $\tilde\Xi = ih$ with $h = h_0e_0 + \boldsymbol{\rho}$ a real quaternion, and $\tilde\Xi^2 = -h^2 = ((\boldsymbol{\rho},\boldsymbol{\rho}) - h_0^2)e_0 - 2h_0\boldsymbol{\rho}$. Setting this equal to $-e_0$ gives $2h_0\boldsymbol{\rho} = 0$ and $(\boldsymbol{\rho},\boldsymbol{\rho}) - h_0^2 = -1$. The first equation again forces $\boldsymbol{\rho} = 0$ or $h_0 = 0$. With $h_0 = 0$ the second reads $(\boldsymbol{\rho},\boldsymbol{\rho}) = -1$, impossible for a real vector; with $\boldsymbol{\rho} = 0$ it reads $h_0^2 = 1$, so $h_0 = \pm 1$ and

$$
\tilde\Xi = \pm i .
$$

**The anti-quaternion subspace contains the two trivial roots and no others.** The sign is the opposite of the quaternion subspace's, and it is exactly the sign that admits $\pm i$ here and excludes the real unit vectors: the imaginary unit $i = ie_0$ lies in $i\mathbb{H}_{\mathbb{B}}$, while it does not lie in $\mathbb{H}_{\mathbb{B}}$.

## The Hermitian Subspace

**Definition.** The **Hermitian subspace** $\mathbb{M}_+$ is the fixed space of Hermitian conjugation,

$$
\mathbb{M}_+ = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = \tilde{Q} \right\} , \qquad \tilde{Q}^{*} = \bar{\tilde{Q}}^{\natural} .
$$

**Coordinate condition.** Since ${}^{*} = \bar{\cdot}\circ{}^{\natural}$, the condition is that the scalar coefficient be real while the three vector coefficients be purely imaginary,

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 , \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $e_0, ie_1, ie_2, ie_3$ and $\dim_{\mathbb{R}}\mathbb{M}_+ = 4$.

**Role.** It is not a subalgebra, but it is closed under the symmetrized product $\tilde{P} \bullet \tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$, which makes it a Jordan algebra. It is the set of elements with real scalar part and purely imaginary vector part.

**The idempotents.** The Hermitian subspace is the one of the remarkable subspaces that carries a nontrivial family of idempotents. Besides $0$ and $e_0$,

$$
\tilde\Pi = \tfrac{1}{2}\left(e_0 + i\mathbf{u}\right) , \qquad \mathbf{u} \in \mathbb{R}^3 , \quad (\mathbf{u},\mathbf{u}) = 1 .
$$

The parameter $\mathbf{u}$ runs over the real unit vectors, so the nontrivial idempotents of the Hermitian subspace form a two-parameter family; each is a Hermitian idempotent of the algebra and a projection. Three properties hold for every member, and they are the ones the projection theory uses. **First, the norm vanishes, so every nontrivial idempotent of the Hermitian subspace is a zero divisor.** The norm of $\tfrac{1}{2}(e_0 + i\mathbf{u})$ is $\tfrac{1}{4}(1 - (\mathbf{u},\mathbf{u})) = 0$, and the nontrivial idempotents are exactly the zero divisors of the Hermitian subspace with scalar part $\tfrac{1}{2}$, every other zero divisor of the subspace being a real multiple of one of them. **Second, the complement and the orthogonality.** The complement $e_0 - \tilde\Pi = \tfrac{1}{2}(e_0 - i\mathbf{u})$ is again a nontrivial idempotent of the subspace, and

$$
\tilde\Pi\left(e_0 - \tilde\Pi\right) = \left(e_0 - \tilde\Pi\right)\tilde\Pi = 0 , \qquad \tilde\Pi + \left(e_0 - \tilde\Pi\right) = e_0 :
$$

the pair is a complete orthogonal pair of idempotents, a **frame**, and each member is primitive and generates a minimal right ideal. The frame cuts the algebra into the four pieces $\tilde\Pi\mathbb{B}\tilde\Pi$, $\tilde\Pi\mathbb{B}(e_0-\tilde\Pi)$, $(e_0-\tilde\Pi)\mathbb{B}\tilde\Pi$ and $(e_0-\tilde\Pi)\mathbb{B}(e_0-\tilde\Pi)$, each of real dimension $2$, so that the eight-dimensional algebra splits into four pieces of dimension two; none of the four is a sum of coordinate blocks, in contrast with the remarkable subspaces, every one of which is a sum of blocks. **Third, the projection.** The idempotent is the projection onto $\mathbb{B}\tilde\Pi$ along $\mathbb{B}(e_0 - \tilde\Pi)$:

$$
\tilde\Pi\tilde{X}\tilde\Pi = \tilde{X}\tilde\Pi \quad (\tilde{X} \in \mathbb{B}\tilde\Pi) , \qquad \tilde\Pi\tilde{Y}\tilde\Pi = 0 \quad (\tilde{Y} \in \mathbb{B}(e_0 - \tilde\Pi)) .
$$

**The ideals.** Let $\tilde\Pi = \tfrac{1}{2}(e_0 + i\mathbf{u})$ be a Hermitian idempotent and $f = e_0 - \tilde\Pi = \tfrac{1}{2}(e_0 - i\mathbf{u})$ its complement. The annihilators are the complement ideals themselves,

$$
I_{\tilde\Pi} = \left\{\tilde X : \tilde X\tilde\Pi = 0\right\} = \left\{\tilde X\,f : \tilde X \in \mathbb{B}\right\} = \mathbb{B}f , \qquad J_{\tilde\Pi} = f\mathbb{B} ,
$$

the first because $\tilde X\tilde\Pi = 0$ leaves $\tilde X = \tilde X(\tilde\Pi + f) = \tilde X f$, and conversely $(\tilde X f)\tilde\Pi = \tilde X f\tilde\Pi = 0$. Here $\tilde\Pi$ is not nilpotent, so the second alternative of the theorem applies and

$$
\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}f = \tilde\Pi\mathbb{B} \oplus f\mathbb{B} ,
$$

four nonzero proper one-sided ideals, all minimal, all of real dimension $4$, arranged in two complementary pairs. The four are the halves of the Peirce decomposition. Expanding $\tilde X$ as $\tilde\Pi\tilde X\tilde\Pi + \tilde\Pi\tilde X f + f\tilde X\tilde\Pi + f\tilde X f$ gives

$$
\mathbb{B} = \tilde\Pi\mathbb{B}\tilde\Pi \oplus \tilde\Pi\mathbb{B}f \oplus f\mathbb{B}\tilde\Pi \oplus f\mathbb{B}f ,
$$

and each of the four Peirce spaces is a complex line, so that the decomposition is $\mathbb{B} = \mathbb{C}\tilde\Pi \oplus \mathbb{C}\tilde R \oplus \mathbb{C}\tilde T \oplus \mathbb{C}f$ with $\mathbb{C}\tilde R = \tilde\Pi\mathbb{B}f$ and $\mathbb{C}\tilde T = f\mathbb{B}\tilde\Pi$. For $\tilde\Pi = \tfrac{1}{2}(e_0 + ie_1)$ the lines are spanned by $\tilde\Pi$, $e_3 - ie_2$, $e_3 + ie_2$ and $f$, and grouped in pairs they are the four minimal one-sided ideals

$$
\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi \oplus \mathbb{C}(e_3 + ie_2) , \quad \mathbb{B}f = \mathbb{C}f \oplus \mathbb{C}(e_3 - ie_2) , \quad \tilde\Pi\mathbb{B} = \mathbb{C}\tilde\Pi \oplus \mathbb{C}(e_3 - ie_2) , \quad f\mathbb{B} = \mathbb{C}f \oplus \mathbb{C}(e_3 + ie_2) .
$$

Two of the four lines are the **idempotent lines** $\mathbb{C}\tilde\Pi$ and $\mathbb{C}f$, each meeting $\mathbb{M}_+$ and $\mathbb{M}_-$ in one real dimension, and two are the **nilpotent lines** $\mathbb{C}(e_3 \mp ie_2)$, lying wholly in the vector subspace.

**The norm and the non-units.** A Hermitian element is $a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector, and its norm is the difference

$$
N(a_0e_0 + i\mathbf{p}) = a_0^2 + i^2(p_1^2 + p_2^2 + p_3^2) = a_0^2 - (\mathbf{p},\mathbf{p}) .
$$

A Hermitian element is a unit exactly when $a_0^2 \neq (\mathbf{p},\mathbf{p})$, so the nonzero non-units of the Hermitian subspace are the nonzero solutions of the single equation $a_0^2 = (\mathbf{p},\mathbf{p})$. Since $(\mathbf{p},\mathbf{p})$ is a sum of real squares, a nonzero solution has $a_0 \neq 0$; indeed $\mathbf{p} = 0$ would give $a_0 = 0$. So every zero divisor of the Hermitian subspace can be written with $a_0$ divided out,

$$
a_0e_0 + i\mathbf{p} = 2a_0 \cdot \tfrac{1}{2}\left(e_0 + i\,\frac{\mathbf{p}}{a_0}\right) , \qquad \left(\frac{\mathbf{p}}{a_0}, \frac{\mathbf{p}}{a_0}\right) = 1 ,
$$

and the second factor is a **Hermitian idempotent**. **The zero divisors of the Hermitian subspace are exactly the nonzero real multiples of the Hermitian idempotents**, and the set of them is a cone of two pieces, the two signs of $a_0$ over the same $\mathbf{p}$. An explicit pair is $(e_0 + ie_1)(e_0 - ie_1) = e_0 - e_0 = 0$, since $(ie_1)^2 = e_0$ and $e_0$ is central; here $e_0 \pm ie_1$ are the two zero divisors, each the other's annihilating partner, and they are $2$ times the idempotents $\tfrac{1}{2}(e_0 \pm ie_1)$. Their squares are $2(e_0 \pm ie_1) \neq 0$, so the vector subspace's square-zero elements are not typical of the algebra's zero divisors but peculiar to it.

**The roots.** A Hermitian element is $\tilde\Xi = a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector, and its square is $(a_0^2 + (\mathbf{p},\mathbf{p}))e_0 + 2ia_0\mathbf{p}$. Setting this equal to $-e_0$ gives $2a_0\mathbf{p} = 0$ and $a_0^2 + (\mathbf{p},\mathbf{p}) = -1$. The second equation is a sum of two real squares equal to $-1$, impossible: **the Hermitian subspace contains no root of $-1$.** This is the sharpest of the two negative cases, because the Hermitian subspace is where the idempotents live: the idempotents are built from the roots, $\tilde\Pi = \tfrac{1}{2}(e_0 + \tilde\Xi i)$, and it is $\tilde\Xi i$, not $\tilde\Xi$, that lies in $\mathbb{M}_+$ when $\tilde\Xi$ is a real root. The roots of $+1$ in $\mathbb{M}_+$ are $\pm e_0$ and the imaginary unit vectors $i\mathbf{p}$ with $\mathbf{p}$ of length one, which is exactly the statement that the idempotents of $\mathbb{M}_+$ are $0$, $e_0$ and $\tfrac{1}{2}(e_0 + i\mathbf{u})$ over real unit vectors. So the roots of $-1$ do not touch $\mathbb{M}_+$; their images under multiplication by $i$ are what $\mathbb{M}_+$ is made of.

## The Anti-Hermitian Subspace

**Definition.** The **anti-Hermitian subspace** $\mathbb{M}_-$ is the anti-fixed space of Hermitian conjugation, which is also the fixed space of the reversal $\flat = -{}^{*}$,

$$
\mathbb{M}_- = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = -\tilde{Q} \right\} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\flat} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is the reverse of the Hermitian one: the scalar coefficient is purely imaginary and the three vector coefficients are real,

$$
\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 , \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $ie_0, e_1, e_2, e_3$ and $\dim_{\mathbb{R}}\mathbb{M}_- = 4$.

**Role.** It is not a subalgebra and it is not closed under the symmetrized product; it is closed under the commutator, and it is a real Lie algebra of dimension four whose centre is the line $\mathbb{R}(ie_0)$. It is the set of elements with purely imaginary scalar part and real vector part, and it is the anti-fixed space of ${}^{*}$ as well as the fixed space of $\flat$.

**The norm and the non-units.** An anti-Hermitian element is $ib_0e_0 + \mathbf{q}$ with $b_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector, and its norm is

$$
N(ib_0e_0 + \mathbf{q}) = (ib_0)^2 + q_1^2 + q_2^2 + q_3^2 = -b_0^2 + (\mathbf{q},\mathbf{q}) .
$$

An anti-Hermitian element is a unit exactly when $(\mathbf{q},\mathbf{q}) \neq b_0^2$, and the nonzero non-units are the nonzero solutions of $(\mathbf{q},\mathbf{q}) = b_0^2$. A nonzero solution has $b_0 \neq 0$, and dividing it out,

$$
ib_0e_0 + \mathbf{q} = 2ib_0 \cdot \tfrac{1}{2}\left(e_0 - i\,\frac{\mathbf{q}}{b_0}\right) , \qquad \left(\frac{\mathbf{q}}{b_0}, \frac{\mathbf{q}}{b_0}\right) = 1 ,
$$

so that **the zero divisors of the anti-Hermitian subspace are exactly the nonzero purely imaginary multiples of the Hermitian idempotents**; the idempotent is the one of the Hermitian subspace, and only the multiplier is imaginary. This is the precise sense in which the two Hermitian subspaces share their zero divisors: the same family of idempotents, multiplied by a real number in the one case and by a purely imaginary number in the other, with the result in $\mathbb{M}_+$ and in $\mathbb{M}_-$ respectively. An explicit pair is $(ie_0 + e_1)(ie_0 - e_1) = -e_0 - ie_1 + ie_1 + e_0 = 0$, with $ie_0 \pm e_1$ the two zero divisors, of square $-2e_0 \pm 2ie_1$, neither zero. The subspace is the mirror image of the Hermitian one, the sign of the norm reversed, and its non-units are correspondingly not square-zero: the square of $ib_0e_0 + \mathbf{q}$ is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, which vanishes only at the zero element. So the Hermitian and the anti-Hermitian non-units alike have nonzero square, and among the remarkable subspaces the only subspace with a nonzero square-zero element is the vector subspace.

**The idempotents and the ideals.** The anti-Hermitian subspace has one idempotent, $0$. The **square** of every element of it lies in the Hermitian subspace, though the product of two different elements need not — $e_1e_2 = e_3$ stays in $\mathbb{M}_-$: for $\tilde{Q} = ib_0e_0 + \mathbf{q}$ with $b_0$ real and $\mathbf{q}$ real, the square is $\tilde{Q}^2 = -(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, real in its scalar part and imaginary in its vector part, which is the shape of $\mathbb{M}_+$. So an idempotent there would satisfy $\tilde\Pi = \tilde\Pi^2 \in \mathbb{M}_+$ and lie in $\mathbb{M}_+ \cap \mathbb{M}_- = 0$. Its nonzero elements are the purely imaginary multiples of the Hermitian subspace's idempotents, and a central multiple $c\tilde\Pi$ of an idempotent is an idempotent only when $c(c-1) = 0$, that is when $c = 0$ or $c = 1$. For the ideals the subspace is $i\mathbb{M}_+$: multiplication by the central unit $i$ is a bijection of $\mathbb{M}_+$ onto $\mathbb{M}_-$ that preserves products and linear combinations and therefore preserves ideals. So the zero divisors of $\mathbb{M}_-$ are the purely imaginary multiples of the Hermitian idempotents, and the minimal ideals they determine are the very same four, $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$ and $f\mathbb{B}$, with the same elements. **The subspace $\mathbb{M}_-$ adds no ideal to those already determined by $\mathbb{M}_+$**, and the same relation holds between $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$, and between the centre and itself, so that up to the central unit $i$ the ideal theory of the remarkable subspaces is carried by the three subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ and $\mathbb{M}_+$.

**The roots.** An anti-Hermitian element is $\tilde\Xi = ib_0e_0 + \mathbf{q}$ with $b_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector, and its square is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$. Setting this equal to $-e_0$ gives $2b_0\mathbf{q} = 0$ and $b_0^2 + (\mathbf{q},\mathbf{q}) = 1$. The first equation gives $\mathbf{q} = 0$ or $b_0 = 0$, and both alternatives are now possible. With $\mathbf{q} = 0$ the second reads $b_0^2 = 1$, giving the trivial roots $\pm i$; with $b_0 = 0$ it reads $(\mathbf{q},\mathbf{q}) = 1$, giving the real unit vectors. So the anti-Hermitian subspace contains

$$
\tilde\Xi = \pm i \qquad \text{and} \qquad \tilde\Xi = \mathbf{q} , \quad \mathbf{q} \in \mathbb{R}^3 , \quad (\mathbf{q},\mathbf{q}) = 1 ,
$$

both families at once. It is the only one of the remarkable subspaces besides the vector subspace to contain roots of $-1$ of both the trivial and the pure kind, and it is the meeting place of the two: the trivial roots lie in $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and the real roots in $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$.

## The Roots of Zero and Plus One

The same computation can be read at the other two central values, and the result is a companion table.

**The roots of $0$** are $0$ and the **nilpotent cone**, by *Biquaternion Square Roots of Minus One, Zero and Plus One*; the nonzero ones are the pure solutions of $(\mathbf{P},\mathbf{P}) = 0$, so they lie in the vector subspace and nowhere else. Each of the remarkable subspaces contains $0$, and only the vector subspace contains any other root of $0$.

**The roots of $+1$** are the images $\tilde\Xi i$ of the roots of $-1$, the map $\tilde\Xi \mapsto \tilde\Xi i$ being a bijection. Multiplication by $i$ carries the remarkable subspaces to the remarkable subspaces — it fixes the centre and the vector subspace and interchanges $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$, and $\mathbb{M}_+$ with $\mathbb{M}_-$ — so the table for $+1$ is the table for $-1$ transported by that interchange:

| subspace | the roots of $+1$ in it |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\pm 1$ |
| $\mathrm{Vect}(\mathbb{B})$ | the images of the pure roots |
| $\mathbb{H}_{\mathbb{B}}$ | $\pm 1$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the imaginary unit quaternions $i\mathbf{p}$ with $(\mathbf{p},\mathbf{p}) = 1$ |
| $\mathbb{M}_+$ | $\pm 1$ and the imaginary unit quaternions |
| $\mathbb{M}_-$ | none |

So of the four four-dimensional subspaces, $\mathbb{M}_-$ is the one that carries roots of $-1$ and no root of $+1$, $\mathbb{M}_+$ is the one that carries roots of $+1$ and no root of $-1$, and $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are exchanged by the multiplication by $i$ that trades the two values. The centre carries the trivial roots of both.

## The Idempotents and the Ideals in the Remarkable Subspaces

An element of $\mathbb{B}$ is an **idempotent** if $\tilde\Pi^2 = \tilde\Pi$, a **left ideal** is a $\mathbb{C}$-subspace $I$ with $\mathbb{B}I \subseteq I$, a **right ideal** a subspace $J$ with $J\mathbb{B} \subseteq J$, and a **two-sided ideal** one that is both. An idempotent splits the algebra as

$$
\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}(e_0 - \tilde\Pi) ,
$$

its complement $e_0 - \tilde\Pi$ is the complementary projection, and when the idempotent is primitive the two summands are minimal one-sided ideals. The classifications themselves are the business of *Biquaternion Idempotents and Projections* and *Biquaternion Ideals and Peirce Decomposition*; what is recorded here is their restriction to the remarkable subspaces.

**The idempotents of the algebra.** Every idempotent of $\mathbb{B}$ is $0$, or $e_0$, or of the form

$$
\tilde\Pi = \tfrac{1}{2}\left(e_0 + \xi i\right) , \qquad \xi^2 = -1 ,
$$

with $\xi$ a root of minus one; there are no others. Writing the idempotent as $\tilde\Pi = \Pi_0e_0 + \mathbf{q}$, with $\Pi_0$ the scalar part and $\mathbf{q}$ the vector part, and using $\mathbf{q}^2 = -(\mathbf{q},\mathbf{q})e_0$, the equation $\tilde\Pi^2 = \tilde\Pi$ is the pair

$$
\Pi_0^2 - (\mathbf{q},\mathbf{q}) = \Pi_0 , \qquad 2\Pi_0\mathbf{q} = \mathbf{q} .
$$

**Theorem (the idempotents of the remarkable subspaces).** The idempotents of $\mathbb{C}_{\mathbb{B}}$ are $0$ and $e_0$; those of $\mathbb{H}_{\mathbb{B}}$ are $0$ and $e_0$; those of $\mathbb{M}_+$ are $0$, $e_0$ and the family of elements $\tfrac{1}{2}(e_0 + i\mathbf{u})$ with $\mathbf{u}$ a real vector of $(\mathbf{u},\mathbf{u}) = 1$; and $0$ is the only idempotent of $\mathrm{Vect}(\mathbb{B})$, of $i\mathbb{H}_{\mathbb{B}}$ and of $\mathbb{M}_-$.

**Proof.** Read the two equations of the display above on each subspace, whose elements are enumerated in the sections. The second equation is the one that does the work: it forces $\mathbf{q} = 0$ unless the scalar part is exactly $\tfrac{1}{2}$, and the scalar part is real only on the centre and in the Hermitian subspace. *Centre:* $\mathbf{q} = 0$ and $\Pi_0^2 = \Pi_0$, so $\Pi_0 \in \{0,1\}$. *Vector:* $\Pi_0 = 0$, and $2\Pi_0\mathbf{q} = \mathbf{q}$ gives $\mathbf{q} = 0$ directly. *Quaternion:* $\Pi_0 = h_0$ real and $\mathbf{q}$ a real vector; $2h_0\mathbf{q} = \mathbf{q}$ gives $\mathbf{q} = 0$ or $h_0 = \tfrac{1}{2}$, and $h_0 = \tfrac{1}{2}$ in the first equation gives $(\mathbf{q},\mathbf{q}) = -\tfrac{1}{4}$, impossible for a real vector, so $\mathbf{q} = 0$ and $h_0 \in \{0,1\}$. *Anti-quaternion:* $\Pi_0$ is purely imaginary and $\mathbf{q}$ is real; $2\Pi_0\mathbf{q} = \mathbf{q}$ forces $\mathbf{q} = 0$ since $2\Pi_0 \neq 1$, and the first equation then gives $\Pi_0^2 = \Pi_0$ with $\Pi_0$ purely imaginary, so $\Pi_0 = 0$. *Hermitian:* $\Pi_0 = a_0$ real and $\mathbf{q} = i\mathbf{p}$ with $\mathbf{p}$ real, so $(\mathbf{q},\mathbf{q}) = -(\mathbf{p},\mathbf{p})$; the second equation gives $\mathbf{p} = 0$ or $a_0 = \tfrac{1}{2}$, and with $\mathbf{p} = 0$ the first gives $a_0 \in \{0,1\}$ while with $a_0 = \tfrac{1}{2}$ it gives $(\mathbf{p},\mathbf{p}) = \tfrac{1}{4}$. *Anti-Hermitian:* $\Pi_0$ is purely imaginary and $\mathbf{q}$ is real; the second equation forces $\mathbf{q} = 0$, and the first gives $\Pi_0 = 0$. $\square$

**Corollary.** The nontrivial idempotents present in the remarkable subspaces are exactly the **Hermitian idempotents** $\tfrac{1}{2}(e_0 + i\mathbf{u})$, and they all lie in the Hermitian subspace. Each is a zero divisor, since its norm is $\tfrac{1}{4}(1 - (\mathbf{u},\mathbf{u})) = 0$; so is its complement, and the two are orthogonal and sum to $e_0$. Every idempotent of the algebra not of this form — every idempotent built on a non-Hermitian root of minus one — lies in none of the remarkable subspaces, its vector part mixing a real and an imaginary direction. So the remarkable subspaces see exactly one nontrivial family of idempotents, in exactly one subspace.

**The ideals.** $\mathbb{B}$ is **simple**, its only two-sided ideals being $0$ and $\mathbb{B}$, and it has **length two** as a left module over itself, so that every nonzero proper left ideal is **minimal**, of real dimension $4$, and dually every nonzero proper right ideal is a minimal right ideal of real dimension $4$. Two consequences are immediate. Since the only two-sided ideals are $0$ and $\mathbb{B}$, **no subspace of the remarkable subspaces is a two-sided ideal**. And each of the remarkable subspaces **generates the whole algebra on both sides**,

$$
\mathbb{B}\mathbb{S} = \mathbb{S}\mathbb{B} = \mathbb{B} \qquad \text{for each of the remarkable subspaces } \mathbb{S} ,
$$

because a left ideal containing a unit is everything, and each of the remarkable subspaces contains a unit: $e_0$ is in the centre, in the quaternion subspace and in $\mathbb{M}_+$, the element $e_1$ is in the vector subspace and in $\mathbb{M}_-$, and $ie_0$ is in the anti-quaternion subspace.

**Theorem (the annihilators of the zero divisors).** Let $\tilde Q \neq 0$ be a zero divisor of $\mathbb{B}$, so that $N(\tilde Q) = 0$. Write $I_{\tilde Q}$ for the set of $\tilde X$ with $\tilde X\tilde Q = 0$ and $J_{\tilde Q}$ for the set of $\tilde X$ with $\tilde Q\tilde X = 0$. Then $I_{\tilde Q}$ is a minimal left ideal, $J_{\tilde Q}$ is a minimal right ideal, and each has real dimension $4$.

**Theorem (the ideal generated against the annihilator).** For a nonzero **nilpotent** of the vector subspace, $\mathbf{P}^2 = 0$, the ideal generated and the annihilator coincide, $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ and $\mathbf{P}\mathbb{B} = J_{\mathbf{P}}$; for every other zero divisor $\tilde Q$ the two are distinct and therefore complementary,

$$
\mathbb{B} = \mathbb{B}\tilde Q \oplus I_{\tilde Q} = \tilde Q\mathbb{B} \oplus J_{\tilde Q} .
$$

**Proof of the nilpotent case.** If $\mathbf{P}^2 = 0$ then $(\tilde X\mathbf{P})\mathbf{P} = \tilde X\mathbf{P}^2 = 0$ for every $\tilde X$, so $\mathbb{B}\mathbf{P} \subseteq I_{\mathbf{P}}$, and $\mathbb{B}\mathbf{P}$ contains $\mathbf{P} \neq 0$ while $I_{\mathbf{P}}$ is proper, so both are nonzero proper left ideals; by the length-two statement they are both minimal of real dimension $4$, hence equal. The right-hand statement is the mirror image, using $(\mathbf{P}\tilde X)\mathbf{P} = 0$ on the left instead. $\square$

The subspaces of the remarkable subspaces that carry a zero divisor are the vector subspace, $\mathbb{M}_+$ and $\mathbb{M}_-$, by the sections above; the other three — the centre, the quaternion subspace and the anti-quaternion subspace — consist of $0$ and units, and determine no minimal ideal at all. So the ideal content of the remarkable subspaces is carried by three of them:

| subspace | left ideal generated | units in it | minimal one-sided ideals determined |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{B}$ | all $Ae_0$ with $A \neq 0$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $e_1$ | $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ and $\mathbf{P}\mathbb{B} = J_{\mathbf{P}}$, $\mathbf{P}$ a nonzero nilpotent |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $e_0$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $ie_0$ | none |
| $\mathbb{M}_+$ | $\mathbb{B}$ | $e_0$ | $\mathbb{B}\tilde\Pi$, $I_{\tilde\Pi} = \mathbb{B}(e_0-\tilde\Pi)$ and their right-hand twins, $\tilde\Pi$ a Hermitian idempotent |
| $\mathbb{M}_-$ | $\mathbb{B}$ | $e_1$ | the same four, unchanged |

Every one of the minimal ideals determined by the remarkable subspaces meets the remarkable subspaces in the same way, two real dimensions in the vector subspace, one in $\mathbb{M}_+$ and one in $\mathbb{M}_-$:

| minimal ideal | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| each $\mathbb{B}\mathbf{P}$, $\mathbf{P}\mathbb{B}$, $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$, $f\mathbb{B}$ | $0$ | $2$ | $0$ | $0$ | $1$ | $1$ |

the entries being real dimensions; so the minimal ideals meet exactly the three subspaces that carry zero divisors, and avoid the other three entirely.

## Summary

The biquaternion algebra carries four conjugations whose fixed and anti-fixed spaces reduce to six distinct subspaces, the remarkable subspaces. The centre $\mathbb{C}_{\mathbb{B}}$, the fixed space of quaternion conjugation, is the set of elements with vanishing vector part, of real basis $e_0, ie_0$ and dimension $2$; it is the centre of the algebra and a field, its nonzero elements are all units, it carries the trivial idempotent pair $0, e_0$ and no minimal ideal, and it contains the two trivial roots of $-1$ and nothing else. The vector subspace $\mathrm{Vect}(\mathbb{B})$, the anti-fixed space of quaternion conjugation, is the kernel of the scalar part, of real basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$ and dimension $6$; it is a Lie algebra and not a subalgebra, its nonzero non-units are the square-zero pure vectors $r(\hat u + i\hat v)$ over an orthonormal pair of directions, a four-parameter family, each its own annihilating partner, and it carries the minimal ideal $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ of any nonzero nilpotent; it is the only subspace in which all three central equations have solutions, and it contains every root of $-1$ that is not one of the trivial pair, the real unit vectors and the four-parameter non-trivial family. The quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the fixed space of complex conjugation, is the set of elements with real coefficients, of real basis $e_0, e_1, e_2, e_3$ and dimension $4$; it is a division subalgebra, every nonzero element a unit, it carries the trivial idempotent pair and no minimal ideal, and its roots of $-1$ are the real unit vectors.

The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the anti-fixed space of complex conjugation, is the set of elements with purely imaginary coefficients, of real basis $ie_0, ie_1, ie_2, ie_3$ and dimension $4$; it is a module over the quaternion subspace and not a subalgebra, every nonzero element a unit, it carries only the idempotent $0$ and no minimal ideal, and its roots of $-1$ are the trivial pair. The Hermitian subspace $\mathbb{M}_+$, the fixed space of Hermitian conjugation, is the set of elements with real scalar part and purely imaginary vector part, of real basis $e_0, ie_1, ie_2, ie_3$ and dimension $4$; it is a Jordan algebra under the symmetrized product, it carries the nontrivial family of idempotents $\tfrac{1}{2}(e_0 + i\mathbf{u})$ over real unit vectors, which are also exactly the zero divisors of the subspace, each with the orthogonal complement $e_0 - \tilde\Pi$ and the four minimal ideals $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$, $f\mathbb{B}$, and it contains no root of $-1$. The anti-Hermitian subspace $\mathbb{M}_-$, the anti-fixed space of Hermitian conjugation and the fixed space of the reversal, is the set of elements with purely imaginary scalar part and real vector part, of real basis $ie_0, e_1, e_2, e_3$ and dimension $4$; it is a real Lie algebra, its zero divisors are the purely imaginary multiples of the Hermitian idempotents and determine the same four minimal ideals, and its roots of $-1$ are the trivial pair and the real unit vectors.

Exactly two of the remarkable subspaces are closed under the product, the centre and the quaternion subspace, and both are division algebras; no subspace of the remarkable subspaces is a two-sided ideal and each generates $\mathbb{B}$ on both sides. Of the remarkable subspaces, only three contain a nonzero idempotent and only three carry a zero divisor, and up to the central unit $i$ the ideal theory is carried by the centre, the vector subspace and the Hermitian subspace. The remarkable subspaces are pairwise distinct; their relations are collected in *Comparison of the Remarkable Subspaces*, and the algebra each one carries belongs to the thematic articles.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0, e_1, e_2, e_3$ | the basis, with $e_0$ the unit and $e_k^2 = -e_0$ |
| $i$ | the central imaginary unit, $i^2 = -1$, commuting with every element |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a general biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | the complex coefficient of $e_\mu$, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, \flat$ | quaternion, complex, Hermitian conjugation and reversal |
| $\operatorname{Sc}(\tilde{Q})$ | the scalar part $Q_0$, equal to $\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$ |
| $\mathbb{C}_{\mathbb{B}}$ | the centre subspace, fixed by ${}^{\natural}$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, anti-fixed by ${}^{\natural}$ |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $N(\tilde{Q})$ | the norm $\tilde{Q}\tilde{Q}^{\natural}$, central |
| $\tilde{P} \bullet \tilde{Q}$ | the symmetrized product $\tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$ |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi^2 = \tilde\Pi$ |
| $e_0 - \tilde\Pi, f$ | the complementary idempotent |
| $\mathbf{u}$ | a real unit vector, the parameter of the Hermitian idempotents |
| $I_{\tilde Q}, J_{\tilde Q}$ | the sets of $\tilde X$ with $\tilde X\tilde Q = 0$ and with $\tilde Q\tilde X = 0$ |
| $\mathbf{P}$ | a pure vector, and a nonzero nilpotent in the ideal theory |
| $\tilde\Xi$ | a root of a central value |
| $A, \mathbf{p}, \mathbf{q}$ | a complex scalar and the real vectors of a Hermitian or anti-Hermitian element |
| $h$ | a real quaternion, $h_0e_0 + \boldsymbol{\rho}$ with $\boldsymbol{\rho}$ real |
| $\boldsymbol{\rho}, \boldsymbol{\rho}'$ | the real and imaginary parts of a complex vector |

## Further Reading

- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the coordinate blocks, the intersections, the sums and the action of the conjugations on the remarkable subspaces
- *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces.md`), for the three eigenspace decompositions the conjugations cut out, one pair of subspaces to each
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the four general products brought to the remarkable subspaces together, the product of two elements of the remarkable subspaces, and the Jordan and the Lie algebra each subspace carries and with which product
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms on the remarkable subspaces side by side, the only orthogonal pair and the comparison of the two readings
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`) and *Remarkable Subspaces under the Real Biquaternion Algebra* (`articles_maths/remarkable-subspaces-under-the-real-biquaternion-algebra.md`), for the restrictions themselves, subspace by subspace and form by form, and for the isotropic lines and the minimal ideals the remarkable subspaces determine
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, the inverse formula and the unit group of the whole algebra
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the zero divisors of the whole algebra, the pure and the non-pure family and the bivector form of the pure ones
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the three classifications in the whole algebra
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the classification of the idempotents of the whole algebra, the bijection with the roots of minus one and the projection reading
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for simplicity, the length, the minimal ideals and the Peirce decomposition in the whole algebra
- *Modules over the General Plain Algebra of Biquaternions* (`articles_maths/modules-over-the-general-plain-algebra-of-biquaternions.md`), for the simple module $S$, the minimal left ideals and the Morita equivalence
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the product and its scalar–vector form
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the two parts into which the product splits
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the group the four conjugations generate
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, its basis, its conjugations and its coordinate systems
