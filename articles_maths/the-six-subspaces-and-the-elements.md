# __The Six Subspaces and the Elements__

## Introduction

An element of the biquaternion algebra is a **unit** if it has a two-sided inverse in the algebra, and a **zero divisor** if some nonzero element multiplies it to zero on one side or the other. One central element decides both. Write $Q^{\natural} = Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ for quaternion conjugation, and

$$
N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 ,
$$

so that $N(\tilde{Q})$ is central, is the sum of the squares of the four complex coefficients, and is the norm of the algebra. Then

$$
\tilde{Q} \tilde{Q}^{\natural} = \tilde{Q}^{\natural}\tilde{Q} = N(\tilde{Q})e_0 , \qquad \tilde{Q}^{-1} = \frac{\tilde{Q}^{\natural}}{N(\tilde{Q})} \quad \text{when } N(\tilde{Q}) \neq 0 .
$$

**Theorem (invertibility).** An element $\tilde{Q}$ is a unit if and only if $N(\tilde{Q}) \neq 0$; if $N(\tilde{Q}) = 0$ and $\tilde{Q} \neq 0$, then $\tilde{Q}$ is a zero divisor, since $\tilde{Q}\tilde{Q}^{\natural} = 0$ exhibits a nonzero element multiplied by $\tilde{Q}$ into zero.

The norm is multiplicative, $N(\tilde{P}\tilde{Q}) = N(\tilde{P})N(\tilde{Q})$, so the units are closed under the product and form a group with the identity $e_0$. The algebra's own treatment is in *Biquaternion Norm and Invertibility*, for the norm, the inverse formula and the unit group, and in *Biquaternion Zero Divisors*, for the elements of vanishing norm in the whole algebra.

The other question one asks of an element is which central values its square takes. A **root of $-1$** is an element $\tilde\Xi$ with $\tilde\Xi^2 = -e_0$, the element $-1$ being understood as $-e_0$. The classification is in *Biquaternion Square Roots of Minus One, Zero and Plus One*, and it has three families: the two **trivial roots** $\pm i$, the **real roots**, which are the pure real quaternions of unit length, a two-parameter family, and the **non-trivial roots**, a four-parameter family of pure elements whose two real vector parts are orthogonal and whose squared lengths differ by one.

This article reads both questions inside the six distinguished subspaces of *Introduction to the Six Subspaces*: which elements of each are units, which are zero divisors, and which roots of the three central values the subspace contains. The answers are collected in one table. Here $A \in \mathbb{C}$ is a complex number and $\mathbf{p}, \mathbf{q} \in \mathbb{R}^3$ are **real** vectors, for which $(\mathbf{p},\mathbf{p})$ is the sum of the squares of the three real coordinates; for a complex vector $\mathbf{P}$ the symbol $(\mathbf{P},\mathbf{P})$ is the complex dot product, the sum of the squares of the three complex coordinates without conjugation.

| subspace | element | $N$ | roots of $-1$ | unit exactly when | zero divisors |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_0$ | $A^2$ | $\pm i$ | $A \neq 0$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf{P}$ | $(\mathbf{P},\mathbf{P})$ | the pure roots | $(\mathbf{P},\mathbf{P}) \neq 0$ | $\mathbf{P} \neq 0$ with $(\mathbf{P},\mathbf{P}) = 0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $h$ | $h_0^2 + h_1^2 + h_2^2 + h_3^2$ | the unit real sphere | $h \neq 0$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$ | $-(h_0^2 + h_1^2 + h_2^2 + h_3^2)$ | $\pm i$ | $h \neq 0$ | none |
| $\mathbb{M}_+$ | $a_0e_0 + i\mathbf{p}$ | $a_0^2 - (\mathbf{p},\mathbf{p})$ | none | $a_0^2 \neq (\mathbf{p},\mathbf{p})$ | $a_0^2 = (\mathbf{p},\mathbf{p})$ |
| $\mathbb{M}_-$ | $ib_0e_0 + \mathbf{q}$ | $(\mathbf{q},\mathbf{q}) - b_0^2$ | $\pm i$ and the unit real sphere | $(\mathbf{q},\mathbf{q}) \neq b_0^2$ | $(\mathbf{q},\mathbf{q}) = b_0^2$ |

Three theorems stand over the table, and the rest of the article is their reading one subspace at a time.

**Theorem (the three without a zero divisor).** The centre, the quaternion subspace and the anti-quaternion subspace contain no nonzero zero divisor: every nonzero element of any of the three is a unit. The vector subspace, the Hermitian subspace and the anti-Hermitian subspace each contain nonzero zero divisors.

**Proof.** In the first three the norm vanishes only at the zero element: $A^2 = 0$ forces $A = 0$ in the centre, and the real sum of squares $h_0^2 + h_1^2 + h_2^2 + h_3^2$, with its negative, forces $h = 0$ in the quaternion and the anti-quaternion subspaces. In the last three the norm is a difference, so it vanishes on nonzero elements: $e_1 + ie_2$ in the vector subspace, $e_0 + ie_1$ in the Hermitian subspace and $ie_0 + e_1$ in the anti-Hermitian subspace, each computed below. $\square$

**Theorem (where the roots live).** Every root of $-1$ lies in the centre or in the vector subspace, and no root lies outside their union; every root except the trivial pair is pure. The centre contains the two trivial roots and nothing else; the vector subspace contains every pure root, hence the whole of the unit real sphere and the whole of the non-trivial family; the quaternion subspace contains the unit real sphere and no other root; the anti-quaternion subspace contains the trivial roots and no other; the Hermitian subspace contains no root of $-1$ at all; and the anti-Hermitian subspace contains both the trivial roots and the unit real sphere.

**Theorem (the two families of zero divisors).** The zero divisors of the algebra are of exactly two kinds. Those in the vector subspace are **pure**, they are the nonzero solutions of $(\mathbf{P},\mathbf{P}) = 0$, and every one of them is **square-zero**: $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0 = 0$. Those in the Hermitian and the anti-Hermitian subspaces are **non-pure**, and none of them is square-zero: the square of $a_0e_0 + i\mathbf{p}$ in $\mathbb{M}_+$ is $(a_0^2 + (\mathbf{p},\mathbf{p}))e_0 + 2ia_0\mathbf{p}$, which is nonzero whenever the element is, and the square of $ib_0e_0 + \mathbf{q}$ in $\mathbb{M}_-$ is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, likewise nonzero.

**Proof.** The square of a pure vector is $-\mathbf{P}^2$ evaluated in the scalar–vector formula, and $(\mathbf{P},\mathbf{P}) = 0$ makes it vanish. For the two non-pure families the displayed squares are computed from the product formula, and each vanishes only if both its scalar part and its vector part vanish: in $\mathbb{M}_+$ the vector part $2ia_0\mathbf{p}$ vanishes only for $\mathbf{p} = 0$ or $a_0 = 0$, the first giving $a_0 = 0$ and the second $(\mathbf{p},\mathbf{p}) = 0$, that is $\mathbf{p} = 0$; in $\mathbb{M}_-$ the vector part $2ib_0\mathbf{q}$ likewise forces $\mathbf{q} = 0$ or $b_0 = 0$, hence the zero element. So no nonzero zero divisor of $\mathbb{M}_+$ or $\mathbb{M}_-$ is square-zero, and every nonzero zero divisor of the vector subspace is. $\square$

The same distinction appears in the relation to the idempotents of the algebra, whose classification is in *The Six Subspaces and the Structure*: **the zero divisors of the two Hermitian subspaces are exactly the nonzero complex multiples of the Hermitian idempotents**, those of $\mathbb{M}_+$ being the real multiples and those of $\mathbb{M}_-$ the purely imaginary ones, while the zero divisors of the vector subspace are multiples of no idempotent. The bilinearity of the product settles at once how the zero divisors sit among the elements: as $\tilde{Q}$ runs over the zero divisors and $\tilde{X}$ over the whole algebra, the product $\tilde{Q}\tilde{X}$ has norm $N(\tilde{Q})N(\tilde{X}) = 0$ and the same for $\tilde{X}\tilde{Q}$. **The union of the zero divisors with the zero element is closed under multiplication and is carried into itself by multiplication by any element on either side.** The zero divisors are the singular set of the algebra, in the usual sense of that word.

## The Centre Subspace

The norm of a central element is the square of its complex coordinate:

$$
N(Ae_0) = A^2 , \qquad (Ae_0)^{-1} = A^{-1}e_0 \ (A \neq 0) .
$$

Every nonzero central element is a unit, so the centre has no nonzero zero divisor, and it is the field $\mathbb{C}_{\mathbb{B}}$. Its only non-unit is $0$. It is the first of the three subspaces of the theorem, and the smallest: the zero divisors of the algebra avoid the centre entirely.

For the roots, a central element is $\tilde\Xi = Q_0e_0$ with $Q_0 \in \mathbb{C}$, and $\tilde\Xi^2 = Q_0^2e_0 = -e_0$ holds exactly when $Q_0^2 = -1$, that is $Q_0 = \pm i$. So the centre contains the two trivial roots and nothing else:

$$
\tilde\Xi = \pm ie_0 = \pm i .
$$

These are the only roots of $-1$ with a nonvanishing scalar part, and so the only ones that are not pure. They are also the only roots that are not in the vector subspace.

## The Vector Subspace

The norm of a pure vector is the complex dot product of the vector with itself:

$$
N(\mathbf{P}) = (\mathbf{P},\mathbf{P}) = P_1^2 + P_2^2 + P_3^2 .
$$

A pure vector is a unit exactly when $(\mathbf{P},\mathbf{P}) \neq 0$. Since a pure vector satisfies $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$, the nonzero non-units of the vector subspace are exactly its **square-zero** elements:

$$
(\mathbf{P},\mathbf{P}) = 0 \iff \mathbf{P}^2 = 0 .
$$

An explicit example is $\mathbf{P} = e_1 + ie_2$, whose square vanishes:

$$
(e_1 + ie_2)^2 = e_1^2 + e_1(ie_2) + (ie_2)e_1 + (ie_2)^2 = -e_0 + ie_3 - ie_3 + e_0 = 0 .
$$

Writing the complex vector as $\boldsymbol{\rho} + i\boldsymbol{\rho}'$ with $\boldsymbol{\rho}, \boldsymbol{\rho}'$ real,

$$
(\mathbf{P},\mathbf{P}) = (\boldsymbol{\rho},\boldsymbol{\rho}) - (\boldsymbol{\rho}',\boldsymbol{\rho}') + 2i(\boldsymbol{\rho},\boldsymbol{\rho}') ,
$$

so that the condition is the pair of real equations

$$
(\boldsymbol{\rho},\boldsymbol{\rho}) = (\boldsymbol{\rho}',\boldsymbol{\rho}') , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}') = 0 .
$$

**A pure vector is a zero divisor exactly when its two real parts are orthogonal and of equal length.** Writing $\boldsymbol{\rho} = r\hat{u}$ and $\boldsymbol{\rho}' = r\hat{v}$ with $r > 0$ and $\hat{u}, \hat{v}$ an orthonormal pair of directions, the zero divisors of the vector subspace are the elements $r(\hat{u} + i\hat{v})$: a four-parameter family, cut out by two real equations in the six real coordinates. The conjugation $\mathbf{P}^{\natural} = -\mathbf{P}$ is nonzero whenever $\mathbf{P}$ is, so for a square-zero $\mathbf{P}$ the pair $\mathbf{P}, -\mathbf{P}$ is a pair of nonzero elements of the vector subspace with vanishing product: **every zero divisor of the vector subspace is its own annihilating partner**, since $\mathbf{P}^2 = 0$. This is the property that the two Hermitian subspaces do not share, and the reason the pure and the non-pure family are kept apart throughout.

For the roots, a pure element is $\tilde\Xi = \mathbf{P} = P_1e_1 + P_2e_2 + P_3e_3$ with complex coefficients, and $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$, so $\tilde\Xi^2 = -e_0$ is the single complex equation

$$
(\mathbf{P},\mathbf{P}) = P_1^2 + P_2^2 + P_3^2 = 1 .
$$

This is the equation whose solutions are the **pure roots**, and the whole of them, of both kinds, lies here: the vector subspace contains every root of $-1$ that is not one of the trivial pair. In the real and imaginary parts the equation is the pair

$$
(\boldsymbol{\rho},\boldsymbol{\rho}) - (\boldsymbol{\rho}',\boldsymbol{\rho}') = 1 , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}') = 0 ,
$$

whose solutions with $\boldsymbol{\rho}' = 0$ are the **real roots**, the vectors $\boldsymbol{\rho}$ of length one, a two-parameter family, and whose solutions with $\boldsymbol{\rho}' \neq 0$ are the **non-trivial roots**, a four-parameter family, the two real parts orthogonal and their squared lengths differing by one,

$$
(\boldsymbol{\rho},\boldsymbol{\rho}) = (\boldsymbol{\rho}',\boldsymbol{\rho}') + 1 , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}') = 0 .
$$

The vector subspace is the only one of the six in which all three central equations have solutions: roots of $-1$ as units, the nilpotents $\mathbf{P}^2 = 0$ as the pure solutions of $(\mathbf{P},\mathbf{P}) = 0$, and roots of $+1$ as the pure solutions of $(\mathbf{P},\mathbf{P}) = -1$. So $\mathrm{Vect}(\mathbb{B})$ carries roots of $-1$ as units and roots of $0$ as zero divisors at the same time, the two opposite kinds of element of the algebra meeting in this one subspace.

## The Quaternion Subspace

On the quaternion subspace the coefficients are real, so the norm is a sum of four squares:

$$
N(h) = h_0^2 + h_1^2 + h_2^2 + h_3^2 , \qquad N(h) = 0 \iff h = 0 .
$$

Every nonzero element of the quaternion subspace is therefore a unit, and the subspace is a **division algebra**, as it must be: it is the image of the real quaternion algebra, which is a division algebra, under $h \mapsto he_0$. The inverse of $h$ is $h^{\natural}/N(h)$ with $N(h) > 0$ real, which is the classical formula. The quaternion subspace is one of the three without a nonzero zero divisor, and the only one of them that is not commutative; among the subspaces closed under the product or under the symmetrized product it is the one whose non-units are the fewest: only $0$.

For the roots, a real quaternion is $\tilde\Xi = h_0e_0 + \boldsymbol{\rho}$ with $h_0 \in \mathbb{R}$ and $\boldsymbol{\rho}$ a **real** vector, and its square is $(h_0^2 - (\boldsymbol{\rho},\boldsymbol{\rho}))e_0 + 2h_0\boldsymbol{\rho}$. Setting this equal to $-e_0$ gives the pair

$$
2h_0\boldsymbol{\rho} = 0 , \qquad h_0^2 - (\boldsymbol{\rho},\boldsymbol{\rho}) = -1 .
$$

The first equation gives $\boldsymbol{\rho} = 0$ or $h_0 = 0$. With $\boldsymbol{\rho} = 0$ the second reads $h_0^2 = -1$, impossible for a real $h_0$; with $h_0 = 0$ it reads $(\boldsymbol{\rho},\boldsymbol{\rho}) = 1$. So the roots of $-1$ in the quaternion subspace are

$$
\tilde\Xi = \boldsymbol{\rho} , \qquad \boldsymbol{\rho} \in \mathbb{R}^3 , \quad (\boldsymbol{\rho},\boldsymbol{\rho}) = 1 ,
$$

the **unit real sphere** and nothing else. These are the classical imaginary units of the quaternions, and their absence of a scalar part is what excludes the trivial roots: $\pm i$ has vanishing vector part and is not a real quaternion.

## The Anti-Quaternion Subspace

An element of the anti-quaternion subspace is $i$ times a real quaternion, and the norm is the negative of a sum of four squares:

$$
N(ih) = -N(h) = -(h_0^2 + h_1^2 + h_2^2 + h_3^2) , \qquad N(ih) = 0 \iff h = 0 .
$$

Every nonzero element of the anti-quaternion subspace is therefore a unit, with inverse $(ih)^{-1} = -(i h^{\natural})/N(h)$; the subspace has no nonzero zero divisor although it is not closed under the product. Its elements are the negatives, up to the central unit, of the elements of the quaternion subspace, which is the reason the criterion is the same apart from the sign.

For the roots, an element of $i\mathbb{H}_{\mathbb{B}}$ is $\tilde\Xi = ih$ with $h = h_0e_0 + \boldsymbol{\rho}$ a real quaternion, and $\tilde\Xi^2 = -h^2 = ((\boldsymbol{\rho},\boldsymbol{\rho}) - h_0^2)e_0 - 2h_0\boldsymbol{\rho}$. Setting this equal to $-e_0$ gives

$$
2h_0\boldsymbol{\rho} = 0 , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}) - h_0^2 = -1 .
$$

The first equation again forces $\boldsymbol{\rho} = 0$ or $h_0 = 0$. With $h_0 = 0$ the second reads $(\boldsymbol{\rho},\boldsymbol{\rho}) = -1$, impossible for a real vector; with $\boldsymbol{\rho} = 0$ it reads $h_0^2 = 1$, so $h_0 = \pm 1$ and

$$
\tilde\Xi = \pm i .
$$

**The anti-quaternion subspace contains the two trivial roots and no others.** The sign is the opposite of the quaternion subspace's, and it is exactly the sign that admits $\pm i$ here and excludes the unit real sphere: the imaginary unit $i = ie_0$ lies in $i\mathbb{H}_{\mathbb{B}}$, while it does not lie in $\mathbb{H}_{\mathbb{B}}$.

## The Hermitian Subspace

A Hermitian element is $a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector, and its norm is the difference

$$
N(a_0e_0 + i\mathbf{p}) = a_0^2 + i^2(p_1^2 + p_2^2 + p_3^2) = a_0^2 - (\mathbf{p},\mathbf{p}) .
$$

A Hermitian element is a unit exactly when $a_0^2 \neq (\mathbf{p},\mathbf{p})$, so the nonzero non-units of the Hermitian subspace are the nonzero solutions of the single equation

$$
a_0^2 = (\mathbf{p},\mathbf{p}) .
$$

Since $(\mathbf{p},\mathbf{p})$ is a sum of real squares, a nonzero solution has $a_0 \neq 0$; indeed $\mathbf{p} = 0$ would give $a_0 = 0$. So every zero divisor of the Hermitian subspace can be written with $a_0$ divided out,

$$
a_0e_0 + i\mathbf{p} = 2a_0 \cdot \tfrac{1}{2}\left(e_0 + i\,\frac{\mathbf{p}}{a_0}\right) , \qquad \left(\frac{\mathbf{p}}{a_0}, \frac{\mathbf{p}}{a_0}\right) = 1 ,
$$

and the second factor is a **Hermitian idempotent**, by *The Six Subspaces and the Structure*. **The zero divisors of the Hermitian subspace are exactly the nonzero real multiples of the Hermitian idempotents**, and the set of them is a cone of two pieces, the two signs of $a_0$ over the same $\mathbf{p}$. An explicit pair is

$$
(e_0 + ie_1)(e_0 - ie_1) = e_0^2 - (ie_1)^2 = e_0 - e_0 = 0 ,
$$

since $(ie_1)^2 = i^2e_1^2 = -(-e_0) = e_0$ and $e_0$ is central, so that the two middle terms cancel. Here $e_0 \pm ie_1$ are the two zero divisors and each is the other's annihilating partner; they are $2$ times the idempotents $\tfrac{1}{2}(e_0 \pm ie_1)$. The squares are not zero, by the theorem of the Introduction: $e_0 + ie_1$ has square $2(e_0 + ie_1)$, so it is a zero divisor of square nonzero, and the vector subspace's square-zero elements are not typical of the algebra's zero divisors but peculiar to it.

For the roots, a Hermitian element is $\tilde\Xi = a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector, and its square is $(a_0^2 + (\mathbf{p},\mathbf{p}))e_0 + 2ia_0\mathbf{p}$. Setting this equal to $-e_0$ gives

$$
2a_0\mathbf{p} = 0 , \qquad a_0^2 + (\mathbf{p},\mathbf{p}) = -1 .
$$

The second equation is a sum of two real squares equal to $-1$ unless both terms vanish, and then it reads $0 = -1$. **The Hermitian subspace contains no root of $-1$.** No separate discussion of the two cases is needed: $a_0^2 + (\mathbf{p},\mathbf{p})$ is a sum of squares of real numbers, hence nonnegative, and $-1$ is not.

This is the sharpest of the two negative cases, because the Hermitian subspace is where the idempotents live. The idempotents are built from the roots, $\tilde\Pi = \tfrac{1}{2}(e_0 + \tilde\Xi i)$, but it is $\tilde\Xi i$, not $\tilde\Xi$, that lies in $\mathbb{M}_+$ when $\tilde\Xi$ is a real root: $\tilde\Xi i$ is then a root of $+1$ of the Hermitian subspace, and the roots of $+1$ in $\mathbb{M}_+$ are $\pm e_0$ and the imaginary unit vectors $i\mathbf{p}$ with $\mathbf{p}$ of length one, which is exactly the statement that the idempotents of $\mathbb{M}_+$ are $0$, $e_0$ and $\tfrac{1}{2}(e_0 + i\mathbf{u})$ over real unit vectors. So the roots of $-1$ do not touch $\mathbb{M}_+$; their images under multiplication by $i$ are what $\mathbb{M}_+$ is made of.

## The Anti-Hermitian Subspace

An anti-Hermitian element is $ib_0e_0 + \mathbf{q}$ with $b_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector, and its norm is

$$
N(ib_0e_0 + \mathbf{q}) = (ib_0)^2 + q_1^2 + q_2^2 + q_3^2 = -b_0^2 + (\mathbf{q},\mathbf{q}) .
$$

An anti-Hermitian element is a unit exactly when $(\mathbf{q},\mathbf{q}) \neq b_0^2$, and the nonzero non-units are the nonzero solutions of $(\mathbf{q},\mathbf{q}) = b_0^2$. A nonzero solution has $b_0 \neq 0$, and dividing it out,

$$
ib_0e_0 + \mathbf{q} = 2ib_0 \cdot \tfrac{1}{2}\left(e_0 - i\,\frac{\mathbf{q}}{b_0}\right) , \qquad \left(\frac{\mathbf{q}}{b_0}, \frac{\mathbf{q}}{b_0}\right) = 1 ,
$$

so that **the zero divisors of the anti-Hermitian subspace are exactly the nonzero purely imaginary multiples of the Hermitian idempotents**; the idempotent is the one of the Hermitian subspace, and only the multiplier is imaginary. This is the precise sense in which the two Hermitian subspaces share their zero divisors: the same family of idempotents, multiplied by a real number in the one case and by a purely imaginary number in the other, with the result in $\mathbb{M}_+$ and in $\mathbb{M}_-$ respectively. An explicit pair is

$$
(ie_0 + e_1)(ie_0 - e_1) = (ie_0)^2 - (ie_0)e_1 + e_1(ie_0) - e_1^2 = -e_0 - ie_1 + ie_1 + e_0 = 0 ,
$$

with $ie_0 \pm e_1$ the two zero divisors, of square $-2e_0 + 2ie_1$ and $-2e_0 - 2ie_1$, neither zero. The subspace is the mirror image of the Hermitian one, the sign of the norm reversed, and its non-units are correspondingly not square-zero: the square of $ib_0e_0 + \mathbf{q}$ is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, which vanishes only at the zero element, since $\mathbf{q} \neq 0$ and $b_0 \neq 0$ together force $2ib_0\mathbf{q} \neq 0$. So the Hermitian and the anti-Hermitian non-units alike have nonzero square, and among the six the only subspace with a nonzero square-zero element is the vector subspace.

For the roots, an anti-Hermitian element is $\tilde\Xi = ib_0e_0 + \mathbf{q}$ with $b_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector, and its square is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$. Setting this equal to $-e_0$ gives

$$
2b_0\mathbf{q} = 0 , \qquad b_0^2 + (\mathbf{q},\mathbf{q}) = 1 .
$$

The first equation gives $\mathbf{q} = 0$ or $b_0 = 0$, and both alternatives are now possible. With $\mathbf{q} = 0$ the second reads $b_0^2 = 1$, giving the trivial roots $\pm i$; with $b_0 = 0$ it reads $(\mathbf{q},\mathbf{q}) = 1$, giving the unit real sphere. So the anti-Hermitian subspace contains

$$
\tilde\Xi = \pm i \qquad \text{and} \qquad \tilde\Xi = \mathbf{q} , \quad \mathbf{q} \in \mathbb{R}^3 , \quad (\mathbf{q},\mathbf{q}) = 1 ,
$$

both families at once. It is the only one of the six besides the vector subspace to contain roots of $-1$ of both the trivial and the pure kind, and it is the meeting place of the two: the trivial roots lie in $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and the real roots in $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$.

## The Roots of Zero and Plus One

The same computation can be read at the other two central values, and the result is a companion table.

**The roots of $0$** are $0$ and the **nilpotent cone**, by *Biquaternion Square Roots of Minus One, Zero and Plus One*; the nonzero ones are the pure solutions of $(\mathbf{P},\mathbf{P}) = 0$, so they lie in the vector subspace and nowhere else. Each of the six contains $0$, and only the vector subspace contains any other root of $0$.

**The roots of $+1$** are the images $\tilde\Xi i$ of the roots of $-1$, the map $\tilde\Xi \mapsto \tilde\Xi i$ being a bijection. Multiplication by $i$ carries the six to the six — it fixes the centre and the vector subspace and interchanges $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$, and $\mathbb{M}_+$ with $\mathbb{M}_-$ — so the table for $+1$ is the table for $-1$ transported by that interchange:

| subspace | the roots of $+1$ in it |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\pm 1$ |
| $\mathrm{Vect}(\mathbb{B})$ | the images of the pure roots |
| $\mathbb{H}_{\mathbb{B}}$ | $\pm 1$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the imaginary unit quaternions $i\mathbf{p}$ with $(\mathbf{p},\mathbf{p}) = 1$ |
| $\mathbb{M}_+$ | $\pm 1$ and the imaginary unit quaternions |
| $\mathbb{M}_-$ | none |

So of the four four-dimensional subspaces, $\mathbb{M}_-$ is the one that carries roots of $-1$ and no root of $+1$, $\mathbb{M}_+$ is the one that carries roots of $+1$ and no root of $-1$, and $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are exchanged by the multiplication by $i$ that trades the two values. The centre carries the trivial roots of both.

## Summary

An element of the biquaternion algebra is a unit exactly when the central norm $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ is nonzero, and then its inverse is $\tilde{Q}^{\natural}/N(\tilde{Q})$; it is a zero divisor exactly when $N(\tilde{Q}) = 0$ and $\tilde{Q} \neq 0$. Restricted to the six distinguished subspaces, the criterion is $A \neq 0$ on the centre, $(\mathbf{P},\mathbf{P}) \neq 0$ on the vector subspace, $h \neq 0$ on the quaternion subspace, $h \neq 0$ on the anti-quaternion subspace, $a_0^2 \neq (\mathbf{p},\mathbf{p})$ on the Hermitian subspace and $(\mathbf{q},\mathbf{q}) \neq b_0^2$ on the anti-Hermitian subspace. Three of the six — the centre, the quaternion subspace and the anti-quaternion subspace — contain no nonzero zero divisor, because on each of them the coefficients are real and the norm is a sum of squares of a single sign; the quaternion subspace is a division algebra and the centre a field. The other three — the vector subspace, the Hermitian subspace and the anti-Hermitian subspace — each contain a nonzero element whose norm vanishes. The zero divisors of the vector subspace are the nonzero solutions of $(\mathbf{P},\mathbf{P}) = 0$, equivalently the pure vectors whose two real parts are orthogonal and of equal length; every one of them is square-zero, and they form a four-parameter family. The zero divisors of the Hermitian subspace are the nonzero solutions of $a_0^2 = (\mathbf{p},\mathbf{p})$, exactly the nonzero real multiples of the Hermitian idempotents; those of the anti-Hermitian subspace are the nonzero solutions of $(\mathbf{q},\mathbf{q}) = b_0^2$, exactly the nonzero purely imaginary multiples of the same idempotents. So the zero divisors of the algebra are of two kinds, the pure ones of the vector subspace, which are square-zero, and the non-pure ones of the two Hermitian subspaces, which are not, and the non-pure ones are the complex multiples of the idempotents. The units form a group under the product, the norm being multiplicative on the algebra.

For the roots, a root of $-1$ is an element of square $-e_0$, of which the algebra has three families: the two trivial roots $\pm i$, the unit real sphere, and the four-parameter non-trivial family of pure elements whose real vector parts are orthogonal and whose squared lengths differ by one. Every root of $-1$ lies in the centre or in the vector subspace, and every root except the trivial pair is pure. The centre contains the two trivial roots and no others; the vector subspace contains every pure root, hence the whole of the unit real sphere and the whole of the non-trivial family, and it is the only subspace in which the roots of $-1$ meet the nilpotents, the roots of $0$; the quaternion subspace contains the unit real sphere and no other root, the trivial roots being excluded for want of a vector part; the anti-quaternion subspace contains the trivial roots and no other, the sphere being excluded by the sign; the Hermitian subspace contains no root of $-1$ at all, because its elements square to a sum of real squares; and the anti-Hermitian subspace contains both the trivial roots and the unit real sphere. The unit real sphere lies in the triple intersection $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$, which is the real vector triple, and the trivial roots lie in $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$, which is the imaginary axis. Every root of $-1$ is a unit, and none is a zero divisor; the idempotents are built from the roots by $\tilde\Pi = \tfrac{1}{2}(e_0 + \tilde\Xi i)$, the trivial roots giving the trivial idempotents, the real roots the Hermitian idempotents of $\mathbb{M}_+$, and the non-trivial roots the idempotents lying in none of the four four-dimensional subspaces. The classification itself, and the parallel treatment of the roots of $0$ and of $+1$, are the business of *Biquaternion Square Roots of Minus One, Zero and Plus One*; the classifications of the idempotents and of the ideals are the business of *The Six Subspaces and the Structure*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde{Q}^{\natural}$ | quaternion conjugation $Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ |
| $N(\tilde{Q})$ | the norm $\tilde{Q}\tilde{Q}^{\natural}$, central |
| $\tilde\Xi$ | a root of a central value |
| $A, \mathbf{P}$ | a complex scalar and a complex vector |
| $h$ | a real quaternion, $h_0e_0 + \boldsymbol{\rho}$ with $\boldsymbol{\rho}$ real |
| $\boldsymbol{\rho}, \boldsymbol{\rho}'$ | the real and imaginary parts of a complex vector |
| $\mathbf{p}, \mathbf{q}, a_0, b_0$ | the real vectors and real scalar parts of $\mathbb{M}_\pm$ |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, the inverse formula and the unit group of the whole algebra
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the zero divisors of the whole algebra, the pure and the non-pure family and the bivector form of the pure ones
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the three classifications in the whole algebra
- *The Six Subspaces and the Structure* (`articles_maths/the-six-subspaces-and-the-structure.md`), for the idempotents that the non-pure zero divisors are multiples of, and for the minimal ideals the annihilators determine
- *The Isotropic Structure of the Quaternion Bilinear Form* (`articles_maths/the-isotropic-structure-of-the-quaternion-bilinear-form.md`), for the isotropic lines, which are exactly the lines spanned by the zero divisors of the vector, Hermitian and anti-Hermitian subspaces
- *The Six Subspaces and the Analysis* (`articles_maths/the-six-subspaces-and-the-analysis.md`), for the null cone as the set on which the second-order operator of the subspace is not elliptic
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the product formula
- *Scalar / Vector decomposition of the Biquaternion Complex Products* (`articles_maths/scalar-over-vector-decomposition-of-the-biquaternion-complex-products.md`), for the square of a pure vector
