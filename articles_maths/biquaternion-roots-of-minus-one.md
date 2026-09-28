# __Biquaternion Roots of Minus One__

## Introduction

This article determines the roots of $-1$ in the biquaternion algebra $\mathbb{B}$, that is, the elements $\xi \in \mathbb{B}$ satisfying

$$
\xi^2 = -1.
$$

It relates to *Biquaternion Idempotents and Projections* through the bijection between the roots and the idempotents established in §*The Relation to the Idempotents*. The goal here is to state the classification precisely and to prove it.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its six distinguished subspaces.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\bar{\tilde{Q}}$, the complex conjugate is denoted $\tilde{Q}^*$, and the Hermitian conjugate is denoted $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. Throughout, $\mu$ and $\nu$ denote pure real quaternions with $\mu^2 = \nu^2 = -1$, and such a pair is said to **anticommute** when $\mu\nu + \nu\mu = 0$.

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
\xi = Q_0 + \mathbf{Q}, \qquad Q_0 \in \mathbb{C}, \qquad \mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $Q_0$ is the **complex scalar part** and $\mathbf{Q}$ is the **complex vector part**.

The square of $\xi$ is given by the product formula for biquaternions:

$$
\xi^2 = \bigl(Q_0^2 - (\mathbf{Q}, \mathbf{Q})\bigr) e_0 + 2Q_0\mathbf{Q}, \qquad (\mathbf{Q}, \mathbf{Q}) = Q_1^2 + Q_2^2 + Q_3^2.
$$

The scalar part of $\xi^2$ is $(Q_0^2 - (\mathbf{Q}, \mathbf{Q})) e_0$, and the vector part is $2Q_0\mathbf{Q}$.

### Reduction to Two Cases

Equating $\xi^2$ to $-1 = -e_0$ requires

$$
2Q_0\mathbf{Q} = 0, \qquad Q_0^2 - (\mathbf{Q}, \mathbf{Q}) = -1.
$$

The first equation is a vector equation. Since $\mathbb{B}$ is a free $\mathbb{C}$-module and $\mathbb{C}$ is a field, the equation $Q_0\mathbf{Q} = 0$ holds if and only if $Q_0 = 0$ or $\mathbf{Q} = 0$. So the roots of $-1$ split into two cases.

**Case 1: $\mathbf{Q} = 0$.** Then $\xi = Q_0 e_0$ is a complex scalar, and the scalar equation becomes $Q_0^2 = -1$. So $Q_0 = \pm i$, and

$$
\xi = \pm i.
$$

These are the **trivial roots**.

**Case 2: $Q_0 = 0$.** Then $\xi = \mathbf{Q}$ is **pure** (vanishing scalar part), and the scalar equation becomes $(\mathbf{Q}, \mathbf{Q}) = 1$. The **pure roots** are the pure biquaternions whose square is $-1$.

The two cases are disjoint: the trivial roots have vanishing vector part, so they fall only in Case 1; the pure roots have vanishing scalar part, so they fall only in Case 2.

### The Pure Roots

We now solve the equation $(\mathbf{Q}, \mathbf{Q}) = 1$ for the pure biquaternion $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$.

Write each complex coefficient as $Q_k = q_k + i q'_k$ with $q_k, q'_k \in \mathbb{R}$. Then

$$
(\mathbf{Q}, \mathbf{Q}) = \sum_{k=1}^{3} Q_k^2 = \sum_{k=1}^{3} (q_k + i q'_k)^2 = \sum_{k=1}^{3} (q_k^2 - q'^2_k) + 2i \sum_{k=1}^{3} q_k q'_k.
$$

Equating the real and imaginary parts to $1$ and $0$:

$$
\sum_{k=1}^{3} q_k^2 - \sum_{k=1}^{3} q'^2_k = 1, \qquad \sum_{k=1}^{3} q_k q'_k = 0.
$$

The first equation gives $\sum_k q_k^2 = 1 + \sum_k q'^2_k \geq 1 > 0$, so the triple $(q_1, q_2, q_3)$ is nonzero.

**Sub-case 2a: $\mathbf{q}' = 0$.** Then $\sum_k q_k^2 = 1$. Let $\mu = q_1 e_1 + q_2 e_2 + q_3 e_3$, a pure real quaternion with

$$
\mu^2 = -\Bigl(\sum_{k=1}^{3} q_k^2\Bigr) e_0 = -1,
$$

and $\mathbf{Q} = \mu$, so $\xi = \mu$. These are the **real roots**. The family is invariant under $\mu \mapsto -\mu$, so it may also be written in the redundant form $\xi = \pm \mu$.

**Sub-case 2b: $\mathbf{q}' \neq 0$.** Then $\sum_k q_k^2 \geq 1 > 0$ and $\sum_k q'^2_k > 0$. Put

$$
b = \Bigl(\sum_{k=1}^{3} q_k^2\Bigr)^{1/2} > 0, \qquad d = \Bigl(\sum_{k=1}^{3} q'^2_k\Bigr)^{1/2} > 0,
$$

and define the pure real quaternions

$$
\mu = \sum_{k=1}^{3} \frac{q_k}{b} e_k, \qquad \nu = \sum_{k=1}^{3} \frac{q'_k}{d} e_k.
$$

Then $\sum_k \mu_k^2 = 1$, so $\mu^2 = -1$; likewise $\nu^2 = -1$; and the second equation gives $\sum_k \mu_k \nu_k = \frac{1}{bd} \sum_k q_k q'_k = 0$, hence

$$
\mu\nu + \nu\mu = -2\Bigl(\sum_{k=1}^{3} \mu_k \nu_k\Bigr) e_0 = 0 :
$$

the two anticommute. With $\mathbf{q} = b\mu$, $\mathbf{q}' = d\nu$ and the first equation $b^2 - d^2 = 1$,

$$
\mathbf{Q} = \mathbf{q} + i\mathbf{q}' = b\mu + d\nu i.
$$

These are the **non-trivial roots**.

### Summary of the Reduction

Every root of $-1$ falls into one of the following three families:

1. $\xi = \pm i$ (trivial roots).
2. $\xi = \pm \mu$ with $\mu$ a pure real quaternion with $\mu^2 = -1$ (real roots).
3. $\xi = b\mu + d\nu i$ with $\mu, \nu$ pure real quaternions with $\mu^2 = \nu^2 = -1$ and $\mu\nu + \nu\mu = 0$, and $b, d > 0$ satisfying $b^2 - d^2 = 1$ (non-trivial roots).

## The Classification

### Statement of the Theorem

**Theorem.** The roots of $-1$ in $\mathbb{B}$ are exactly the elements of the form

$$
\xi = \pm i, \qquad \xi = \pm\mu, \qquad \xi = b\mu + d\nu i,
$$

where $\mu$ and $\nu$ are pure real quaternions with $\mu^2 = \nu^2 = -1$ and $\mu\nu + \nu\mu = 0$, and $b, d > 0$ satisfy $b^2 - d^2 = 1$.

Equivalently:

1. **Non-trivial roots:** $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are pure real quaternions with $\mu^2 = \nu^2 = -1$ and $\mu\nu + \nu\mu = 0$, and $b, d > 0$ satisfy $b^2 - d^2 = 1$.
2. **Trivial roots:** $\xi = \pm i$.
3. **Real roots:** $\xi = \pm \mu$, where $\mu$ is a pure real quaternion with $\mu^2 = -1$.

### Verification

We verify that each of the three families consists of roots of $-1$.

**Trivial root.** $(\pm i)^2 = -1$ since $i^2 = -1$. ✓

**Real roots.** For a pure real quaternion $\mu$ with $\mu^2 = -1$, $(\pm \mu)^2 = \mu^2 = -1$. ✓

**Non-trivial roots.** Compute

$$
\xi^2 = (b\mu + d\nu i)^2 = b^2 \mu^2 + d^2 \nu^2 i^2 + bd(\mu\nu + \nu\mu) i.
$$

Now $\mu^2 = \nu^2 = -1$ and $i^2 = -1$, so the first two terms sum to $-(b^2 - d^2) e_0$. The cross term $bd(\mu\nu + \nu\mu) i$ vanishes because $\mu$ and $\nu$ anticommute. Therefore

$$
\xi^2 = -(b^2 - d^2) e_0 = -1,
$$

using the constraint $b^2 - d^2 = 1$. ✓

### Degenerate Cases

The three families are related as follows.

**The real roots as the case $d = 0$.** In the non-trivial family the constraint $b^2 - d^2 = 1$ is carried with $d > 0$. If the condition $d > 0$ is relaxed to $d \geq 0$, then $d = 0$ forces $b = 1$ and $\xi = \mu$, a real root; the element $\nu$ no longer enters. The real roots are therefore the case $d = 0$ of the non-trivial formula, and not a separate construction.

**The trivial roots as a separate family.** The trivial roots $\xi = \pm i$ have vanishing vector part. The real roots (with $\mathbf{Q} = \mu \neq 0$) and the non-trivial roots (with $\mathbf{Q} = b\mu + d\nu i$ and $b \neq 0$, hence $\mathbf{Q} \neq 0$) all have nonvanishing vector part. So the roots with vanishing vector part are exactly $\pm i$, and they form a separate family.

### Status of the Roots

The **trivial** roots are the two elements $\pm i$. The **real** roots are the elements $\pm\mu$ with $\mu$ a pure real quaternion of square $-1$; the single constraint $\sum_k \mu_k^2 = 1$ on the three real coefficients leaves two free real parameters. The **non-trivial** roots are parametrised by the pair $(\mu, \nu)$ with $\mu^2 = \nu^2 = -1$ and $\mu\nu + \nu\mu = 0$ — two free real parameters for $\mu$, and one for $\nu$, its two constraints $\sum_k \nu_k^2 = 1$ and $\sum_k \mu_k \nu_k = 0$ acting on three real coefficients — together with the pair $(b, d)$ with $b^2 - d^2 = 1$ and $b, d > 0$, one further parameter: four free real parameters in all.

All roots except the trivial ones are **pure** (their scalar part vanishes), hence lie in the six-real-dimensional vector subspace of pure biquaternions. The roots are neither idempotents ($\xi^2 = -1 \neq \xi$) nor zero divisors (§*The Roots as Invertible Elements*).

## The Relation to the Idempotents

The classification of the roots gives the classification of the idempotents of $\mathbb{B}$: the map

$$
\xi \longmapsto \tilde\Pi_+(\xi) = \tfrac{1}{2}(e_0 + \xi i)
$$

is a bijection from the set of roots of $-1$ onto the set of idempotents, under which the complementary pairs $\{\tilde\Pi, e_0 - \tilde\Pi\}$ correspond to the classes $\{\xi, -\xi\}$, and under which the three families of roots give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and the idempotents lying in none of the four four-dimensional subspaces. The construction of the idempotent, the proof of the bijection and the projection interpretation are the subject of *Biquaternion Idempotents and Projections*.

## The Relation to the Zero Divisors

### The Idempotents as Zero Divisors

Every non-trivial idempotent is a zero divisor, $\tilde\Pi(e_0 - \tilde\Pi) = 0$ with both factors nonzero (the construction of $\tilde\Pi$ is in *Biquaternion Idempotents and Projections*). The trivial idempotents $0$ and $e_0$ are not zero divisors: $0$ is excluded by the definition, and $e_0$ is a unit.

### The Roots as Invertible Elements

A root of $-1$ is a unit and **not** a zero divisor. Indeed, $\xi^2 = -1$ gives

$$
\xi\,(-\xi) = (-\xi)\,\xi = e_0,
$$

so $\xi$ is invertible, with inverse $\xi^{-1} = -\xi$. A unit is not a zero divisor: if $\xi R = 0$ for some $R$, then $R = (-\xi)(\xi R) = 0$, and the same argument applies to $R\xi = 0$. Hence the roots of $-1$ lie in the group of units $\mathbb{B}^\times$. The central scalar $\xi\bar{\xi}$ is $-1$ for the trivial roots and $+1$ for a pure root.

## The Roots of Plus One

We also record the analogous problem for $+1$. A **root of $+1$** is an element $\eta \in \mathbb{B}$ satisfying $\eta^2 = 1$.

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

- **Non-trivial roots of $+1$:** $\eta = b\mu i + d\nu i^2 = b\mu i - d\nu$, with $b^2 - d^2 = 1$ and $\mu\nu + \nu\mu = 0$.
- **Trivial roots of $+1$:** $\eta = \pm 1$ (from $\xi = \pm i$). These are the only roots of $+1$ that lie in the center $\mathbb{C}$.
- **Real roots of $+1$:** $\eta = \pm \mu i$, where $\mu$ is a pure real quaternion with $\mu^2 = -1$.

The roots of $+1$ are not used in the classification of the idempotents, but they appear in the theory of the biquaternion exponential and in the theory of the biquaternion logarithm.

## Summary

The roots of $-1$ in the biquaternion algebra are exactly:

1. **Non-trivial roots:** $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are pure real quaternions with $\mu^2 = \nu^2 = -1$ and $\mu\nu + \nu\mu = 0$, and $b, d > 0$ satisfy $b^2 - d^2 = 1$.
2. **Trivial roots:** $\xi = \pm i$.
3. **Real roots:** $\xi = \pm \mu$, where $\mu$ is a pure real quaternion with $\mu^2 = -1$.

The proof proceeds by writing $\xi = Q_0 + \mathbf{Q}$ in scalar-vector form, squaring using the biquaternion product formula, and equating to $-1$. The vector part of the square is $2Q_0\mathbf{Q}$, which forces $Q_0 = 0$ or $\mathbf{Q} = 0$; the scalar part is $Q_0^2 - (\mathbf{Q}, \mathbf{Q})$, which then determines the roots in each case. The scalar case gives the trivial roots. The pure case reduces to $(\mathbf{Q}, \mathbf{Q}) = 1$, which splits into the real and non-trivial families according to whether the imaginary part of the pure biquaternion vanishes.

The trivial roots are the two elements $\pm i$. The real roots are the family $\pm\mu$ cut out by the single constraint $\sum_k \mu_k^2 = 1$, leaving two free real parameters. The non-trivial roots carry the pair $(\mu, \nu)$ with $\mu^2 = \nu^2 = -1$ and $\mu\nu + \nu\mu = 0$ together with the pair $(b, d)$ with $b^2 - d^2 = 1$ and $b, d > 0$, four free real parameters in all. All roots except the trivial ones are pure, hence lie in the six-real-dimensional vector subspace of pure biquaternions.

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$, which are of the form $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$. The map $\xi \mapsto \tilde\Pi_+(\xi) = \tfrac{1}{2}(e_0 + \xi i)$ is a bijection from the roots of $-1$ to the idempotents; complementary pairs of idempotents correspond to roots modulo the sign identification $\xi \sim -\xi$. The non-trivial idempotents form a four-real-parameter family, and are used in the classification of the non-pure zero divisors. The roots themselves are units, and they lie in the group of units $\mathbb{B}^\times$.

The roots of $+1$ are obtained from the roots of $-1$ by multiplication by $i$: $\eta = \xi i$. They are not used in the idempotent classification, but they appear in the theory of the biquaternion exponential.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary |
| $\xi$ | Root of $-1$ |
| $\eta$ | Root of $+1$ |
| $Q_0$ | Complex scalar part of the root, $Q_0 \in \mathbb{C}$ |
| $\mathbf{Q} = Q_1e_1+Q_2e_2+Q_3e_3$ | Complex vector part of the root |
| $\mu, \nu$ | Pure real quaternions with $\mu^2 = \nu^2 = -1$ |
| $b, d$ | Real parameters with $b^2 - d^2 = 1$ |
| $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ | Idempotent |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the original classification.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the relation to the idempotents and the zero divisors.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the constraint verification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
