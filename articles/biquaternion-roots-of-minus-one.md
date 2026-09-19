
# Biquaternion Roots of Minus One

## Introduction

This article determines the roots of $-1$ in the biquaternion algebra $\mathbb{B}$, that is, the elements $\xi \in \mathbb{B}$ satisfying

$$
\xi^2 = -1.
$$

It follows the article on biquaternion zero divisors, where the classification of the roots is used to classify the idempotents, and it follows the article on biquaternion norm and invertibility, where the norm form and the invertibility criterion are established. The goal here is to state the classification precisely and to prove it.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its four fixed-point subspaces.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\bar{\tilde{Q}}$, the complex conjugate is denoted $\tilde{Q}^*$, and the Hermitian conjugate is denoted $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$.

## The Problem and Its Reduction

### Statement

A **root of $-1$** in $\mathbb{B}$ is an element $\xi \in \mathbb{B}$ satisfying

$$
\xi^2 = -1.
$$

The problem is to find all such elements.

### Vector-Part Decomposition

Write $\xi$ in the scalar-vector form

$$
\xi = A + \mathbf{X}, \qquad A = Q_0 \in \mathbb{C}, \qquad \mathbf{X} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $A$ is the **complex scalar part** and $\mathbf{X}$ is the **complex vector part**.

The square of $\xi$ is given by the product formula for biquaternions:

$$
\xi^2 = \bigl(A^2 - (\mathbf{X}, \mathbf{X})\bigr) e_0 + 2A\mathbf{X}, \qquad (\mathbf{X}, \mathbf{X}) = Q_1^2 + Q_2^2 + Q_3^2.
$$

The scalar part of $\xi^2$ is $(A^2 - (\mathbf{X}, \mathbf{X})) e_0$, and the vector part is $2A\mathbf{X}$.

### Reduction to Two Cases

Equating $\xi^2$ to $-1 = -e_0$ requires

$$
2A\mathbf{X} = 0, \qquad A^2 - (\mathbf{X}, \mathbf{X}) = -1.
$$

The first equation is a vector equation. Since $\mathbb{B}$ is a free $\mathbb{C}$-module and $\mathbb{C}$ is a field, the equation $A\mathbf{X} = 0$ holds if and only if $A = 0$ or $\mathbf{X} = 0$. So the roots of $-1$ split into two cases.

**Case 1: $\mathbf{X} = 0$.** Then $\xi = A e_0$ is a complex scalar, and the scalar equation becomes $A^2 = -1$. So $A = \pm i$, and

$$
\xi = \pm i.
$$

These are the **trivial roots**.

**Case 2: $A = 0$.** Then $\xi = \mathbf{X}$ is **pure** (vanishing scalar part), and the scalar equation becomes $(\mathbf{X}, \mathbf{X}) = 1$. The **pure roots** are the pure biquaternions whose square is $-1$.

The two cases are disjoint: the trivial roots have vanishing vector part, so they fall only in Case 1; the pure roots have vanishing scalar part, so they fall only in Case 2.

### The Pure Roots

We now solve the equation $(\mathbf{X}, \mathbf{X}) = 1$ for the pure biquaternion $\mathbf{X} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$.

Write each complex coefficient as $Q_k = q_k + i q'_k$ with $q_k, q'_k \in \mathbb{R}$. Then

$$
(\mathbf{X}, \mathbf{X}) = \sum_{k=1}^{3} Q_k^2 = \sum_{k=1}^{3} (q_k + i q'_k)^2 = \sum_{k=1}^{3} (q_k^2 - q'^2_k) + 2i \sum_{k=1}^{3} q_k q'_k.
$$

Equating the real and imaginary parts to $1$ and $0$:

$$
\sum_{k=1}^{3} q_k^2 - \sum_{k=1}^{3} q'^2_k = 1, \qquad \sum_{k=1}^{3} q_k q'_k = 0.
$$

Let $\mathbf{q} = (q_1, q_2, q_3)$ and $\mathbf{q}' = (q'_1, q'_2, q'_3)$ be the vectors of real and imaginary parts in $\mathbb{R}^3$. The conditions become

$$
|\mathbf{q}|^2 - |\mathbf{q}'|^2 = 1, \qquad \mathbf{q} \cdot \mathbf{q}' = 0.
$$

From the first condition, $|\mathbf{q}|^2 = 1 + |\mathbf{q}'|^2 \geq 1 > 0$, so $\mathbf{q} \neq 0$.

**Sub-case 2a: $\mathbf{q}' = 0$.** Then $|\mathbf{q}|^2 = 1$, so $\mathbf{q}$ is a unit vector in $\mathbb{R}^3$. Let $\mu = \mathbf{q}$, which is a unit pure real quaternion. Then $\mathbf{X} = \mu$, and $\xi = \mu$. Since $\mu$ is a unit pure real quaternion, $\mu^2 = -1$ (a standard fact from the quaternion algebra). These are the **real roots**. Since $\mu$ ranges over the whole unit sphere $S^2 \subset \mathbb{R}^3$, and $S^2$ is invariant under $\mu \mapsto -\mu$, the family can also be written in the redundant form $\xi = \pm \mu$.

**Sub-case 2b: $\mathbf{q}' \neq 0$.** Then $|\mathbf{q}| \geq 1 > 0$ and $|\mathbf{q}'| > 0$, so we can normalize both. Let

$$
\mu = \frac{\mathbf{q}}{|\mathbf{q}|}, \qquad \nu = \frac{\mathbf{q}'}{|\mathbf{q}'|},
$$

which are both unit pure real quaternions. The condition $\mathbf{q} \cdot \mathbf{q}' = 0$ becomes $\mu \cdot \nu = 0$, i.e. $\mu \perp \nu$. Set

$$
b = |\mathbf{q}| > 0, \qquad d = |\mathbf{q}'| > 0.
$$

Then $\mathbf{q} = b\mu$, $\mathbf{q}' = d\nu$, and $\mathbf{X} = \mathbf{q} + i\mathbf{q}' = b\mu + d\nu i$. The condition $|\mathbf{q}|^2 - |\mathbf{q}'|^2 = 1$ becomes

$$
b^2 - d^2 = 1.
$$

These are the **non-trivial roots**.

### Summary of the Reduction

Every root of $-1$ falls into one of the following three families:

1. $\xi = \pm i$ (trivial roots).
2. $\xi = \pm \mu$ with $\mu$ a unit pure real quaternion (real roots).
3. $\xi = b\mu + d\nu i$ with $\mu, \nu$ perpendicular unit pure real quaternions and $b, d > 0$ satisfying $b^2 - d^2 = 1$ (non-trivial roots).

## The Classification

### Statement of the Theorem

**Theorem.** The roots of $-1$ in $\mathbb{B}$ are exactly the elements of the form

$$
\xi = \pm i, \qquad \xi = \pm\mu, \qquad \xi = b\mu + d\nu i,
$$

where $\mu$ and $\nu$ are perpendicular unit pure real quaternions and $b, d > 0$ satisfy $b^2 - d^2 = 1$.

Equivalently:

1. **Non-trivial roots:** $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions, and $b, d > 0$ satisfy $b^2 - d^2 = 1$.
2. **Trivial root:** $\xi = \pm i$.
3. **Real roots:** $\xi = \pm\mu$, where $\mu$ is a unit pure real quaternion.

### Verification

We verify that each of the three families consists of roots of $-1$.

**Trivial root.** $(\pm i)^2 = -1$ since $i^2 = -1$. ✓

**Real roots.** For a unit pure real quaternion $\mu$, $\mu^2 = -1$ (a standard quaternion fact: the unit pure real quaternions form the unit sphere $S^2$ in $\mathbb{R}^3$, and every such element squares to $-1$). So $(\pm \mu)^2 = \mu^2 = -1$. ✓

**Non-trivial roots.** Compute

$$
\xi^2 = (b\mu + d\nu i)^2 = b^2 \mu^2 + d^2 \nu^2 i^2 + bd(\mu\nu + \nu\mu) i.
$$

Now $\mu^2 = \nu^2 = -1$ and $i^2 = -1$, so the first two terms sum to $-(b^2 - d^2) e_0$. For the cross term, use the quaternion product formula for pure quaternions:

$$
\mu\nu = -\mu \cdot \nu + \mu \times \nu, \qquad \nu\mu = -\nu \cdot \mu + \nu \times \mu = -\mu \cdot \nu - \mu \times \nu.
$$

Adding: $\mu\nu + \nu\mu = -2(\mu \cdot \nu) e_0$. Since $\mu \perp \nu$, we have $\mu \cdot \nu = 0$, so the cross term vanishes. Therefore

$$
\xi^2 = -(b^2 - d^2) e_0 = -1,
$$

using the constraint $b^2 - d^2 = 1$. ✓

### Degenerate Cases

The three families are related as follows.

**Real roots as the boundary of the non-trivial family.** If $d \to 0$ in the non-trivial family, then $b^2 \to 1$ (by the constraint $b^2 - d^2 = 1$), and $\xi = b\mu + d\nu i$ tends to $\mu$, a real root. The unit pure quaternion $\nu$ becomes undetermined in the limit. So the real roots (the unit sphere $S^2$) form the boundary of the non-trivial family.

**Trivial roots as a separate family.** The trivial roots $\xi = \pm i$ have vanishing vector part. Neither the real roots (which are pure, hence have $\mathbf{X} = \mu \neq 0$) nor the non-trivial roots (which have $\mathbf{X} = b\mu + d\nu i$ with $b \neq 0$, hence $\mathbf{X} \neq 0$) include or approach the trivial roots. So the trivial roots form a separate family, consisting of two isolated points.

### Parametrization by Hyperbolic Functions

The constraint $b^2 - d^2 = 1$ is the equation of a hyperbola in the $(b, d)$-plane. If we take $b > 0$, we can parametrize the constraint by

$$
b = \cosh t, \qquad d = \sinh t, \qquad t \in \mathbb{R},
$$

using the identity $\cosh^2 t - \sinh^2 t = 1$. Substituting:

$$
\xi = \cosh t \, \mu + \sinh t \, \nu i, \qquad \mu \perp \nu, \quad |\mu| = |\nu| = 1, \quad t \in \mathbb{R}.
$$

The parameter $t$ is the **rapidity** of the root, by analogy with the rapidity of a Lorentz boost.

### Status of the Roots

The **non-trivial** roots form a **four-real-dimensional** family, parametrized by:

- the choice of $\mu$ on the unit sphere $S^2 \subset \mathbb{R}^3$ (two real parameters);
- the choice of $\nu$ on the unit circle in the plane perpendicular to $\mu$ (one real parameter);
- the choice of $(b, d)$ on the branch of the hyperbola $b^2 - d^2 = 1$ with $b, d > 0$ (one real parameter).

Together: $2 + 1 + 1 = 4$ real dimensions.

The **real** roots form a **two-real-dimensional** submanifold, the unit sphere $S^2$, which is the boundary of the non-trivial family. The **trivial** roots are two isolated points. So the set of roots of $-1$ is a stratified space whose largest stratum (the non-trivial family) is four-dimensional.

All roots except the trivial ones are **pure** (their scalar part vanishes). The pure roots (real and non-trivial) sit inside the six-real-dimensional space of pure biquaternions.

The roots are neither idempotents ($\xi^2 = -1 \neq \xi$) nor zero divisors ($N(\xi) \neq 0$ in every case). They therefore lie in the group of units $\mathbb{B}^\times$ studied in the article on biquaternion norm and invertibility.

## The Relation to the Idempotents

### The Idempotent Construction

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$. Recall from the article on biquaternion zero divisors that every idempotent is of the form

$$
\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi$ is a root of $-1$.

**Theorem.** The idempotents of $\mathbb{B}$ are exactly the elements of the form

$$
\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi$ is a root of $-1$. Every such element satisfies $\tilde{P}^2 = \tilde{P}$, and conversely every idempotent of $\mathbb{B}$ has this form.

**Proof.** If $\xi^2 = -1$, then

$$
\tilde{P}^2 = \tfrac{1}{4}(e_0 \pm \xi i)^2 = \tfrac{1}{4}(e_0 \pm 2\xi i + \xi^2 i^2) = \tfrac{1}{4}(e_0 \pm 2\xi i + 1) = \tfrac{1}{2}(e_0 \pm \xi i) = \tilde{P},
$$

where we have used $\xi^2 i^2 = (-1)(-1) = 1$ and the fact that $e_0$ commutes with $\xi i$. The converse is proved in the article on biquaternion zero divisors. $\square$

Substituting the classification of $\xi$:

- For the trivial root $\xi = \pm i$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} i \cdot i = \tfrac{1}{2} e_0 \mp \tfrac{1}{2} e_0$, giving $\tilde{P} = 0$ or $\tilde{P} = e_0$. These are the **trivial idempotents**.
- For the real root $\xi = \pm \mu$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \mu i$. These are the idempotents that involve the real scalar part together with the imaginary vector direction $\mu i$.
- For the non-trivial root $\xi = b\mu + d\nu i$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu + d\nu i) i = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu i - d\nu)$. These idempotents combine a real scalar part, a real vector part in the direction of $\nu$, and an imaginary vector part in the direction of $\mu$.

### The Correspondence

The map

$$
\xi \longmapsto P_+(\xi), \qquad P_+(\xi) = \tfrac{1}{2}(e_0 + \xi i),
$$

is a **bijection** from the set of roots of $-1$ to the set of idempotents of $\mathbb{B}$. Indeed:

- It is well-defined: the verification that $P_+(\xi)$ is idempotent whenever $\xi^2 = -1$ is the computation above.
- It is injective: $P_+(\xi) = P_+(\xi')$ gives $\xi i = \xi' i$, hence $\xi = \xi'$.
- It is surjective onto the set of idempotents of the stated form, since $P_-(\xi) = \tfrac{1}{2}(e_0 - \xi i) = P_+(-\xi)$ and $-\xi$ is again a root of $-1$.

Consequently, the **complementary pairs** $\{P, e_0 - P\}$ of idempotents are in bijection with the roots of $-1$ modulo the sign identification $\xi \sim -\xi$, since

$$
P_+(-\xi) = \tfrac{1}{2}(e_0 - \xi i) = e_0 - P_+(\xi).
$$

Thus $P_+(\xi)$ and $P_+(-\xi)$ are the two members of a complementary pair, and the pair itself corresponds to the class $\{\xi, -\xi\}$.

### The Idempotent as a Projection

An idempotent $\tilde{P}$ satisfies $\tilde{P}^2 = \tilde{P}$. Its **complement** $e_0 - \tilde{P}$ is also an idempotent, and $\tilde{P}(e_0 - \tilde{P}) = 0$, so the pair $\{\tilde{P}, e_0 - \tilde{P}\}$ gives a **direct sum decomposition** of the underlying $\mathbb{C}$-module:

$$
\mathbb{B} = \tilde{P}\mathbb{B} \oplus (e_0 - \tilde{P})\mathbb{B}.
$$

This is the algebraic content of the statement that idempotents correspond to projections.

## The Relation to the Zero Divisors

### The Idempotents as Zero Divisors

Every non-trivial idempotent is a zero divisor, because

$$
\tilde{P}(e_0 - \tilde{P}) = \tilde{P} - \tilde{P}^2 = 0,
$$

and both $\tilde{P}$ and $e_0 - \tilde{P}$ are nonzero unless $\tilde{P}$ is $0$ or $e_0$. So the non-trivial idempotents form a subset of the zero divisor set $\mathcal{Z}$ studied in the article on biquaternion zero divisors. The trivial idempotents $0$ and $e_0$ are not zero divisors: $0$ is excluded by the definition, and $e_0$ has nonzero norm form.

### The Roots as Invertible Elements

A root of $-1$ is **not** a zero divisor. Indeed, the norm form of a root satisfies

$$
N(\xi) = \xi\bar{\xi} = \begin{cases} -1 & \text{for the trivial root } \xi = \pm i, \\ +1 & \text{for a pure root.} \end{cases}
$$

In either case $N(\xi) \neq 0$, so by the invertibility criterion, $\xi$ is invertible. The roots of $-1$ therefore lie in the group of units $\mathbb{B}^\times$.

### Dimensions

The set of roots of $-1$ is a stratified space of real dimension $4$ (the non-trivial family) with a two-dimensional boundary stratum (the real roots, $S^2$) and two isolated points (the trivial roots, $\pm i$).

The idempotents correspond bijectively to the roots of -1, so the non-trivial idempotents (that is, the idempotents other than 0 and e₀) also form a set of real dimension 4, with a two-dimensional boundary stratum inherited from the real roots. The trivial roots $\pm i$ map to the trivial idempotents $0$ and $e_0$, which are excluded from the non-trivial idempotents, so there are no isolated points among the non-trivial idempotents.

The non-trivial roots sit inside the six-real-dimensional space of pure biquaternions. The non-trivial idempotents sit inside the six-real-dimensional zero divisor set. The trivial roots ($\pm i$) and trivial idempotents ($0, e_0$) are isolated points outside these families.

## The Roots of Plus One

For completeness, we note the analogous problem for $+1$. A **root of $+1$** is an element $\eta \in \mathbb{B}$ satisfying $\eta^2 = 1$.

The roots of $+1$ are related to the roots of $-1$ by

$$
\eta = \xi i,
$$

where $\xi$ is a root of $-1$. Indeed,

$$
(\xi i)^2 = \xi^2 i^2 = (-1)(-1) = 1.
$$

The map $\xi \mapsto \xi i$ is a bijection from the roots of $-1$ to the roots of $+1$: it is injective since $i$ is invertible, and if $\eta^2 = 1$ then $\xi = -\eta i$ satisfies $\xi^2 = -1$ and $\xi i = \eta$.

Applying the classification of the roots of $-1$:

- **Non-trivial roots of $+1$:** $\eta = b\mu i + d\nu i^2 = b\mu i - d\nu$, with $b^2 - d^2 = 1$ and $\mu \perp \nu$.
- **Trivial roots of $+1$:** $\eta = \pm 1$ (from $\xi = \pm i$). These are the only roots of $+1$ that lie in the center $\mathbb{C}$.
- **Real roots of $+1$:** $\eta = \pm \mu i$, where $\mu$ is a unit pure real quaternion.

The roots of $+1$ are not used in the classification of the idempotents, but they appear in the theory of the biquaternion exponential and in the theory of the biquaternion logarithm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary |
| $\xi$ | Root of $-1$ |
| $\eta$ | Root of $+1$ |
| $\mu, \nu$ | Unit pure real quaternions |
| $b, d$ | Real parameters with $b^2 - d^2 = 1$ |
| $t$ | Rapidity parameter |
| $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ | Idempotent |

## Summary

The roots of $-1$ in the biquaternion algebra are exactly:

1. **Non-trivial roots:** $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions and $b, d > 0$ satisfy $b^2 - d^2 = 1$.
2. **Trivial root:** $\xi = \pm i$.
3. **Real roots:** $\xi = \pm \mu$, where $\mu$ is a unit pure real quaternion.

The proof proceeds by writing $\xi = A + \mathbf{X}$ in scalar-vector form, squaring using the biquaternion product formula, and equating to $-1$. The vector part of the square is $2A\mathbf{X}$, which forces $A = 0$ or $\mathbf{X} = 0$; the scalar part is $A^2 - (\mathbf{X}, \mathbf{X})$, which then determines the roots in each case. The scalar case gives the trivial root. The pure case reduces to $(\mathbf{X}, \mathbf{X}) = 1$, which splits into the real and non-trivial families according to whether the imaginary part of the pure biquaternion vanishes.

The non-trivial roots form a four-real-dimensional family, with the real roots (a two-dimensional sphere) as their boundary. The trivial roots are two isolated points. All roots except the trivial ones are pure, and they lie in the six-dimensional space of pure biquaternions.

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$, which are of the form $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$. The map $\xi \mapsto P_+(\xi) = \tfrac{1}{2}(e_0 + \xi i)$ is a bijection from the roots of $-1$ to the idempotents; complementary pairs of idempotents correspond to roots modulo the sign identification $\xi \sim -\xi$. The non-trivial idempotents form a four-dimensional family in the six-dimensional zero divisor set, and are used in the classification of the non-pure zero divisors in the article on biquaternion zero divisors. The roots themselves are invertible, and they lie in the group of units studied in the article on biquaternion norm and invertibility.

The roots of $+1$ are obtained from the roots of $-1$ by multiplication by $i$: $\eta = \xi i$. They are not used in the idempotent classification, but they appear in the theory of the biquaternion exponential.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the original classification.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the relation to the idempotents and the zero divisors.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the representation theory and the constraint verification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.

