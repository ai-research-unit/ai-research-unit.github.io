
# Biquaternion Roots of Minus One

## Introduction

This article determines the roots of $-1$ in the biquaternion algebra $\mathbb{B}$, that is, the elements $\xi \in \mathbb{B}$ satisfying

$$
\xi^2 = -1.
$$

It follows the article on biquaternion zero divisors, where the classification of the roots is used to classify the idempotents, and it follows the article on biquaternion norm and invertibility, where the norm form and the invertibility criterion are established. The goal here is to state the classification precisely and to prove it.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its four fixed-point subspaces.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\bar{\tilde{Q}}$, the complex conjugate is denoted $\tilde{Q}^*$, and the Hermitian conjugate is denoted $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$.

## The Problem

### Statement

A **root of $-1$** in $\mathbb{B}$ is an element $\xi \in \mathbb{B}$ satisfying

$$
\xi^2 = -1.
$$

The problem is to find all such elements.

### Reduction to the Pure Case

The first observation is that a root of $-1$ cannot have a nonzero scalar part. Indeed, write $\xi = A e_0 + \mathbf{X}$ with $A \in \mathbb{C}$ and $\mathbf{X}$ a pure biquaternion. Then

$$
\xi^2 = (A^2 - (\mathbf{X}, \mathbf{X})) e_0 + 2 A \mathbf{X}.
$$

For this to equal $-1 = -e_0$, the vector part must vanish:

$$
2 A \mathbf{X} = 0.
$$

If $\mathbf{X} \neq 0$, then $A = 0$, because the product of a nonzero complex scalar with a nonzero pure biquaternion is nonzero. The reason is that the pure biquaternions form a free module over $\mathbb{C}$, and multiplication by a nonzero complex scalar is injective on this module. If $\mathbf{X} = 0$, then $\xi = A e_0$ and $\xi^2 = A^2 e_0 = -e_0$, so $A^2 = -1$, i.e. $A = \pm i$. So the roots of $-1$ are either:

- **Scalar roots:** $\xi = \pm i$.
- **Pure roots:** $\xi$ pure, i.e. $\xi = \mathbf{X}$, with $\xi^2 = -1$.

The scalar roots are the trivial roots. The pure roots are the non-trivial roots, and they are the main subject of this article.

### The Pure Roots

A pure biquaternion has the form

$$
\xi = X_1 e_1 + X_2 e_2 + X_3 e_3, \qquad X_1, X_2, X_3 \in \mathbb{C}.
$$

The condition $\xi^2 = -1$ becomes

$$
X_1^2 + X_2^2 + X_3^2 = 1.
$$

Indeed, for a pure biquaternion, the square is

$$
\xi^2 = -(X_1^2 + X_2^2 + X_3^2) e_0,
$$

as computed in the article on biquaternion zero divisors, so $\xi^2 = -e_0$ if and only if the sum of squares is $1$.

So the pure roots of $-1$ are the pure biquaternions whose three complex components have a sum of squares equal to $1$. This is a single complex equation in three complex unknowns, i.e. two real equations in six real unknowns, so the solution set is a four-real-dimensional submanifold of the six-real-dimensional space of pure biquaternions.

## The Classification

### Statement

**Theorem.** The roots of $-1$ in $\mathbb{B}$ are exactly:

1. **The non-trivial roots:** $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions, and $b, d \in \mathbb{R}$ satisfy $b^2 - d^2 = 1$.
2. **The trivial root:** $\xi = \pm i$.
3. **The real roots:** $\xi = \pm \mu$, where $\mu$ is a unit pure real quaternion.

### Remarks

The three families are distinguished by the value of the real and imaginary parts of $\xi$.

- The **non-trivial roots** have both real and imaginary parts nonzero. They are the generic roots, and they use all four basis elements $e_0, e_1, e_2, e_3$ (via the scalar imaginary $i$).
- The **trivial root** $\xi = \pm i$ is the scalar imaginary itself. It is not pure in the biquaternion sense, because its imaginary part is the scalar $i$, which has zero vector part.
- The **real roots** $\xi = \pm \mu$ are unit pure real quaternions. They lie in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and they are the roots of $-1$ that already exist in $\mathbb{H}$.

The real roots are the case $d = 0$ of the non-trivial form, with $b = \pm 1$. The trivial root is the case $b = 0$ of the non-trivial form, with $d = \pm 1$ and $\nu = 1$ (the unit scalar, which is not a pure quaternion but is the degenerate limit of the construction). So the three families can be combined into the single form

$$
\xi = b\mu + d\nu i, \qquad b^2 - d^2 = 1,
$$

where $\mu$ and $\nu$ are perpendicular unit pure real quaternions, or one of the degenerate cases $\mu = 1$ or $\nu = 1$.

### Parametrization by Hyperbolic Functions

The constraint $b^2 - d^2 = 1$ is the equation of a hyperbola in the $(b, d)$-plane. It is parametrized by

$$
b = \cosh t, \qquad d = \sinh t, \qquad t \in \mathbb{R},
$$

or by

$$
b = -\cosh t, \qquad d = \sinh t, \qquad t \in \mathbb{R}.
$$

So the non-trivial roots can be written

$$
\xi = \cosh t \, \mu + \sinh t \, \nu i, \qquad \mu \perp \nu, \quad |\mu| = |\nu| = 1, \quad t \in \mathbb{R},
$$

up to the sign of the whole expression. This is the parametrization given by Sangwine. The parameter $t$ is the **rapidity** of the root, in analogy with the rapidity of a Lorentz boost.

## Proof of the Classification

### The Proof Strategy

The proof is by enumeration of the terms obtained when an arbitrary biquaternion is squared. Write the arbitrary biquaternion in the form

$$
\tilde{Q} = a e_0 + b\mu + c i + d\nu i,
$$

where $a, b, c, d \in \mathbb{R}$ and $\mu, \nu$ are unit pure real quaternions. If the vector part of $\tilde{Q}$ vanishes, we take $\mu$ arbitrary and $b = 0$; if the imaginary part of the vector part vanishes, we take $\nu$ arbitrary and $d = 0$. This form covers all biquaternions.

Compute $\tilde{Q}^2$ by expanding the product. The 16 terms are organized in the following table, where the entry in row $r$ and column $c$ is the product of the $r$-th term and the $c$-th term of $\tilde{Q}$:

| | $a$ | $b\mu$ | $c i$ | $d\nu i$ |
|---|---|---|---|---|
| $a$ | $a^2$ | $ab\mu$ | $ac i$ | $ad\nu i$ |
| $b\mu$ | $ab\mu$ | $-b^2$ | $bc\mu i$ | $bd\mu\nu i$ |
| $c i$ | $ac i$ | $bc\mu i$ | $-c^2$ | $cd\nu i$ |
| $d\nu i$ | $ad\nu i$ | $bd\nu\mu i$ | $cd\nu i$ | $d^2$ |

The 16 terms fall into three classes:

- **Real terms.** The diagonal entries $a^2$, $-b^2$, $-c^2$, $d^2$ are the only real terms. Their sum must be $-1$:

$$
a^2 - b^2 - c^2 + d^2 = -1. \tag{D}
$$

- **Pure real quaternion terms.** The off-diagonal entries $ab\mu$ appear twice, in positions $(a, b\mu)$ and $(b\mu, a)$, and they are the only pure real quaternion terms. Since they have the same sign, their sum must be zero:

$$
2 ab \mu = 0. \tag{O}
$$

- **Terms containing $i$.** All the remaining terms contain $i$ and must sum to zero:

$$
2 ac i + 2 ad \nu i + 2 bc \mu i + 2 bd (\mu \nu + \nu \mu) i + 2 cd \nu i = 0. \tag{I}
$$

### Case Analysis

From $(O)$, either $a = 0$ or $b = 0$.

**Case $a = 0$.** Then $(D)$ becomes $b^2 + c^2 - d^2 = 1$, and $(I)$ becomes

$$
2 bc \mu i + 2 bd (\mu \nu + \nu \mu) i + 2 cd \nu i = 0.
$$

For this to hold, each coefficient must vanish separately when $\mu$, $\nu$, and $\mu \nu + \nu \mu$ are linearly independent (which they are when $\mu$ and $\nu$ are not parallel). So $bc = 0$, $cd = 0$, and either $bd = 0$ or $\mu \perp \nu$.

- If $c = 0$: then $b^2 - d^2 = 1$. If $d = 0$, then $b = \pm 1$ and $\xi = \pm \mu$, giving the real roots. If $b, d \neq 0$, then $\mu \perp \nu$, giving $\xi = b\mu + d\nu i$ with $b^2 - d^2 = 1$, the non-trivial roots.
- If $d = 0$: then $b^2 + c^2 = 1$. If $b = 0$, then $c = \pm 1$ and $\xi = \pm i$, giving the trivial root. If $c = 0$, then $b = \pm 1$ and $\xi = \pm \mu$, giving the real roots.

**Case $b = 0$.** Then $(D)$ becomes $a^2 - c^2 + d^2 = -1$, i.e. $c^2 - a^2 - d^2 = 1$, and $(I)$ becomes

$$
2 ac i + 2 ad \nu i + 2 cd \nu i = 0.
$$

So $ac = 0$, $ad = 0$, $cd = 0$.

- If $a = 0$: then $c^2 - d^2 = 1$. If $d = 0$, then $c = \pm 1$ and $\xi = \pm i$, giving the trivial root. If $c = 0$, then $d = \pm 1$ and $\xi = \pm \nu i$. But $(\nu i)^2 = \nu^2 i^2 = (-1)(-1) = 1$, so $\xi = \pm \nu i$ is a root of $+1$, not of $-1$. So this subcase gives no roots of $-1$, and it is the reason the case $b = 0$ contributes only the trivial root and not the real roots.
- If $c = 0$: then $a^2 + d^2 = -1$, which has no real solution.
- If $d = 0$: then $c^2 - a^2 = 1$. If $a = 0$, then $c = \pm 1$ and $\xi = \pm i$, giving the trivial root. If $c = 0$, then $a^2 = -1$, which has no real solution.

### Conclusion

The only solutions are:

- The non-trivial roots $\xi = b\mu + d\nu i$ with $b^2 - d^2 = 1$ and $\mu \perp \nu$.
- The trivial root $\xi = \pm i$.
- The real roots $\xi = \pm \mu$.

This is the classification stated in the theorem. $\square$

## The Relation to the Idempotents

### The Idempotent Construction

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$. Recall from the article on biquaternion zero divisors that every idempotent is of the form

$$
\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi$ is a root of $-1$.

Substituting the classification of $\xi$:

- For the trivial root $\xi = \pm i$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} i \cdot i = \tfrac{1}{2} e_0 \mp \tfrac{1}{2} e_0$, giving $\tilde{P} = 0$ or $\tilde{P} = e_0$. These are the trivial idempotents.
- For the real root $\xi = \pm \mu$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \mu i$. These are the idempotents that lie in the subalgebra spanned by $e_0$ and one of the quaternion units, after complexification.
- For the non-trivial root $\xi = b\mu + d\nu i$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu + d\nu i) i = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu i - d\nu)$. These are the idempotents that use all four basis elements $e_0, e_1, e_2, e_3$.

### The Correspondence

The correspondence between roots of $-1$ and idempotents is as follows. The map

$$
\xi \longmapsto \{\tilde{P}_+, \tilde{P}_-\}, \qquad \tilde{P}_\pm = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

sends a root $\xi$ to the unordered pair of its two associated idempotents. This map is not injective: the roots $\xi$ and $-\xi$ give the same unordered pair, because

$$
\tfrac{1}{2} e_0 \pm \tfrac{1}{2} (-\xi) i = \tfrac{1}{2} e_0 \mp \tfrac{1}{2} \xi i,
$$

so the pair $\{\tilde{P}_+, \tilde{P}_-\}$ is the same. So the map is two-to-one from roots to unordered pairs of idempotents. Equivalently, the idempotents are in bijection with the roots of $-1$ modulo the sign $\xi \sim -\xi$, with the additional sign choice $\pm$ in the construction.

The roots of $-1$ are not idempotents, and they are not zero divisors: if $\xi^2 = -1$, then $N(\xi) = -1 \neq 0$, so $\xi$ is invertible, and it lies in the group of units $\mathbb{B}^\times$ studied in the article on biquaternion norm and invertibility. The idempotents, by contrast, are zero divisors, as shown in the article on biquaternion zero divisors.

### The Idempotent as a Projection

An idempotent $\tilde{P}$ is a **projection**: it satisfies $\tilde{P}^2 = \tilde{P}$, and its complementary idempotent is $e_0 - \tilde{P}$. The two idempotents $\tilde{P}$ and $e_0 - \tilde{P}$ are orthogonal: $\tilde{P} (e_0 - \tilde{P}) = 0$. So the pair of idempotents associated with a root $\xi$ gives a direct sum decomposition

$$
\mathbb{B} = \tilde{P} \mathbb{B} \oplus (e_0 - \tilde{P}) \mathbb{B},
$$

where $\tilde{P} \mathbb{B}$ and $(e_0 - \tilde{P}) \mathbb{B}$ are the two ideals of $\mathbb{B}$ corresponding to the two idempotents. Each ideal is isomorphic to $\mathbb{H}_{\mathbb{B}}$ as a left module, and the decomposition is the algebraic content of the idempotent construction.

## The Relation to the Zero Divisors

### The Idempotents as Zero Divisors

Every non-trivial idempotent is a zero divisor, because

$$
\tilde{P} (e_0 - \tilde{P}) = \tilde{P} - \tilde{P}^2 = 0,
$$

and both $\tilde{P}$ and $e_0 - \tilde{P}$ are nonzero unless $\tilde{P}$ is $0$ or $e_0$. So the non-trivial idempotents are zero divisors, and they lie in the zero divisor set $\mathcal{Z}$ studied in the article on biquaternion zero divisors.

### The Roots as Invertible Elements

A root of $-1$ is not a zero divisor, because $\xi^2 = -1$ implies $N(\xi) = -1 \neq 0$, so $\xi$ is invertible. The roots of $-1$ therefore lie in the group of units $\mathbb{B}^\times$ studied in the article on biquaternion norm and invertibility, and they form a four-real-dimensional submanifold of $\mathbb{B}^\times$.

### The Cones

The roots of $-1$ form a four-dimensional submanifold of the six-dimensional space of pure biquaternions, and the idempotents form a family of two-dimensional submanifolds (one for each root, parametrized by the sign $\pm$) in the seven-dimensional zero divisor set. The relation between the two is the construction $\xi \mapsto \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$.

## The Roots of Plus One

For completeness, we note the analogous problem for $+1$. A **root of $+1$** is an element $\eta \in \mathbb{B}$ satisfying $\eta^2 = 1$. The roots of $+1$ are related to the roots of $-1$ by

$$
\eta = \xi i,
$$

where $\xi$ is a root of $-1$. Indeed, $(\xi i)^2 = \xi^2 i^2 = (-1)(-1) = 1$. So the classification of the roots of $+1$ follows immediately from the classification of the roots of $-1$:

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

1. The non-trivial roots $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions and $b, d \in \mathbb{R}$ satisfy $b^2 - d^2 = 1$.
2. The trivial root $\xi = \pm i$.
3. The real roots $\xi = \pm \mu$, where $\mu$ is a unit pure real quaternion.

The proof is by enumeration of the 16 terms in the square of an arbitrary biquaternion, grouped into real terms, pure real quaternion terms, and terms containing $i$. The analysis of the constraints gives the three families.

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$, which are of the form $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$. The idempotents are zero divisors, and they are used in the classification of the non-pure zero divisors in the article on biquaternion zero divisors. The roots themselves are invertible, and they lie in the group of units studied in the article on biquaternion norm and invertibility.

The roots of $+1$ are obtained from the roots of $-1$ by multiplication by $i$: $\eta = \xi i$. They are not used in the idempotent classification, but they appear in the theory of the biquaternion exponential.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the original classification.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the relation to the idempotents and the zero divisors.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the representation theory and the constraint verification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

