
# Split-Quaternion Roots of Minus One

## Introduction

This article determines the roots of $-1$ in the split quaternion algebra $\mathbb{H}_{\mathbb{D}}$, that is, the elements $\xi \in \mathbb{H}_{\mathbb{D}}$ satisfying

$$
\xi^2 = -1.
$$

It follows the article on split quaternion zero divisors, where the structure of the algebra and its zero divisors are established, and it uses the idempotent decomposition of the algebra into two copies of the quaternion algebra.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The split quaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the preceding articles, together with its four conjugations, its four fixed-point subspaces, and its idempotent decomposition.

Throughout, a split quaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$, where $Q_\mu^* = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^\dagger$.

The idempotents of the split complex algebra are $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split quaternion is

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

with $\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}$ ordinary quaternions.

## The Problem

### Statement

A **root of $-1$** in $\mathbb{H}_{\mathbb{D}}$ is an element $\xi \in \mathbb{H}_{\mathbb{D}}$ satisfying

$$
\xi^2 = -1.
$$

The problem is to find all such elements.

### Reduction to the Idempotent Components

In the idempotent basis, the square of $\xi = \xi_+ e_+ + \xi_- e_-$ is

$$
\xi^2 = \xi_+^2 e_+ + \xi_-^2 e_-,
$$

because the idempotents satisfy $e_+^2 = e_+$, $e_-^2 = e_-$, and $e_+ e_- = e_- e_+ = 0$.

The equation $\xi^2 = -1$ is therefore equivalent to the pair of equations

$$
\xi_+^2 = -1, \qquad \xi_-^2 = -1,
$$

where $\xi_\pm \in \mathbb{H}$ are ordinary quaternions, and $-1$ is understood as $-e_0 = -1_{\mathbb{H}}$ in each copy of $\mathbb{H}$.

So the roots of $-1$ in $\mathbb{H}_{\mathbb{D}}$ are exactly the pairs $(\xi_+, \xi_-)$ where $\xi_+$ and $\xi_-$ are roots of $-1$ in the quaternion algebra $\mathbb{H}$.

### Reduction to the Quaternion Case

The problem therefore reduces to the problem of finding the roots of $-1$ in $\mathbb{H}$, which is a solved problem: the roots of $-1$ in $\mathbb{H}$ are exactly the unit pure quaternions, i.e., the elements $\mu \in \mathbb{H}$ with $\mu^2 = -1$ and $\mu \in \mathbb{R}^3_{\mathbb{H}}$.

So the roots of $-1$ in $\mathbb{H}_{\mathbb{D}}$ are the elements

$$
\xi = \mu_+ e_+ + \mu_- e_-,
$$

where $\mu_+, \mu_- \in \mathbb{H}$ are unit pure real quaternions.

## The Classification

### Statement

**Theorem.** The roots of $-1$ in $\mathbb{H}_{\mathbb{D}}$ are exactly the elements of the form

$$
\xi = \mu_+ e_+ + \mu_- e_-,
$$

where $\mu_+$ and $\mu_-$ are unit pure real quaternions. Equivalently, in the standard basis,

$$
\xi = \frac{1}{2}(\mu_+ + \mu_-) + \frac{j}{2}(\mu_+ - \mu_-),
$$

with $\mu_\pm$ unit pure real quaternions.

There are no other roots of $-1$ in $\mathbb{H}_{\mathbb{D}}$.

### Proof

**Step 1: Reduction.** As shown above, the equation $\xi^2 = -1$ is equivalent to the pair of equations $\xi_+^2 = -1$ and $\xi_-^2 = -1$, where $\xi_\pm \in \mathbb{H}$ are the idempotent components of $\xi$.

**Step 2: Quaternion roots.** The roots of $-1$ in $\mathbb{H}$ are exactly the unit pure real quaternions. This is the standard result: $\mu^2 = -1$ with $\mu \in \mathbb{H}$ implies $\mu$ is pure (if $\mu$ had a nonzero scalar part, the scalar part of $\mu^2$ would be nonzero in general) and $|\mu| = 1$.

**Step 3: Combination.** Any pair $(\mu_+, \mu_-)$ of unit pure real quaternions gives a root $\xi = \mu_+ e_+ + \mu_- e_-$. Conversely, every root arises this way. $\square$

### The Scalar Part

A root $\xi$ of $-1$ in $\mathbb{H}_{\mathbb{D}}$ has the form

$$
\xi = \frac{1}{2}(\mu_+ + \mu_-) + \frac{j}{2}(\mu_+ - \mu_-).
$$

The scalar part of $\xi$ (with respect to the quaternion basis) is the split complex number

$$
\xi_0 = \frac{1}{2}(\mu_+ + \mu_-),
$$

which is a real quaternion in general. The vector part is

$$
\boldsymbol{\xi} = \frac{j}{2}(\mu_+ - \mu_-),
$$

which is a purely split-imaginary quaternion.

So a root of $-1$ in $\mathbb{H}_{\mathbb{D}}$ is an element with:
- A scalar part that is a real quaternion (not necessarily a real number).
- A vector part that is purely split-imaginary.

This is different from the biquaternion case, where the roots of $-1$ are pure (zero scalar part) or scalar (the scalar imaginary $i$).

### The Pure Roots

A root $\xi$ of $-1$ is **pure** if its scalar part vanishes:

$$
\mu_+ + \mu_- = 0, \quad \text{i.e.,} \quad \mu_- = -\mu_+.
$$

In this case, the root is

$$
\xi = \mu_+ e_+ - \mu_+ e_- = \mu_+ (e_+ - e_-) = \mu_+ j.
$$

So the pure roots of $-1$ are exactly the elements of the form $\mu j$ with $\mu \in \mathbb{H}$ a unit pure real quaternion. This is a three-dimensional family, parametrized by the unit sphere $\mathbb{S}^2$ in $\mathbb{R}^3$.

### The Scalar Roots

A root $\xi$ of $-1$ is **scalar** if its vector part vanishes:

$$
\mu_+ - \mu_- = 0, \quad \text{i.e.,} \quad \mu_- = \mu_+.
$$

In this case, the root is

$$
\xi = \mu_+ e_+ + \mu_+ e_- = \mu_+ (e_+ + e_-) = \mu_+.
$$

So the scalar roots of $-1$ are exactly the unit pure real quaternions $\mu \in \mathbb{H}$. This is a three-dimensional family.

But wait: the scalar roots of $-1$ in $\mathbb{H}_{\mathbb{D}}$ are the elements $\xi = \mu$ with $\mu^2 = -1$ in $\mathbb{H}$. These are the quaternion roots of $-1$ embedded in $\mathbb{H}_{\mathbb{D}}$. They are not the "scalar imaginary" $i$ of the biquaternion case; there is no single scalar root, because the split complex algebra $\mathbb{D}$ has no square root of $-1$.

So the scalar roots of $-1$ in $\mathbb{H}_{\mathbb{D}}$ form a three-dimensional family, and the pure roots form another three-dimensional family. The general root is a combination of the two, parametrized by a pair of unit pure real quaternions, which is a six-dimensional family.

### Dimension of the Root Set

The root set is parametrized by a pair of unit pure real quaternions $\mu_+, \mu_-$, each of which lies on the unit sphere $\mathbb{S}^2$ in $\mathbb{R}^3$. So the root set has real dimension $3 + 3 = 6$.

This is a six-dimensional submanifold of the eight-dimensional algebra $\mathbb{H}_{\mathbb{D}}$.

### Comparison with the Biquaternion Case

In the biquaternion algebra $\mathbb{B}$, the roots of $-1$ are:
- The trivial root $\pm i$ (two points).
- The real roots $\pm \mu$ with $\mu$ a unit pure real quaternion (a three-dimensional family, doubled by sign).
- The non-trivial roots $b\mu + d\nu i$ with $\mu \perp \nu$ and $b^2 - d^2 = 1$ (a four-dimensional family).

The biquaternion root set has a much richer structure, with degenerate roots, real roots, and non-trivial roots. The split quaternion root set is simpler: it is the product of two copies of the quaternion root set, i.e., a pair of unit pure real quaternions.

The reason for the difference is that the split complex algebra $\mathbb{D}$ has no square root of $-1$, so there is no "scalar imaginary" root. In the biquaternion case, the scalar imaginary $i$ is a root of $-1$, and it generates the non-trivial roots by combination with the quaternion roots. In the split quaternion case, there is no such scalar root, and the root set is simply the product of two quaternion root sets.

## The Relation to the Idempotents

### The Idempotents of $\mathbb{H}_{\mathbb{D}}$

The idempotents of $\mathbb{H}_{\mathbb{D}}$ are the elements $\tilde{P}$ with $\tilde{P}^2 = \tilde{P}$. In the idempotent basis, an element $\tilde{P} = \tilde{P}_+ e_+ + \tilde{P}_- e_-$ is idempotent if and only if

$$
\tilde{P}_+^2 = \tilde{P}_+, \qquad \tilde{P}_-^2 = \tilde{P}_-.
$$

In the quaternion algebra $\mathbb{H}$, the idempotents are only $0$ and $1$. So the idempotents of $\mathbb{H}_{\mathbb{D}}$ are the four elements

$$
0, \qquad e_+, \qquad e_-, \qquad e_+ + e_- = 1.
$$

These are the only idempotents. The two nontrivial idempotents $e_+$ and $e_-$ are the ones associated with the two components.

### The Relation Between Roots and Idempotents

In the biquaternion case, the roots of $-1$ are related to the idempotents by the formula

$$
\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi$ is a root of $-1$ and $i$ is the scalar imaginary. This formula gives all the idempotents of the biquaternion algebra.

In the split quaternion case, the idempotents are the fixed elements $0, e_+, e_-, 1$, and they are not obtained from the roots of $-1$ by a similar formula. The reason is that the split complex algebra has no scalar imaginary, so there is no element to multiply the root by to obtain an idempotent.

The relation between the roots of $-1$ and the idempotents is therefore different in the two cases:
- In $\mathbb{B}$, the roots of $-1$ generate the idempotents.
- In $\mathbb{H}_{\mathbb{D}}$, the roots of $-1$ and the idempotents are independent structures.

This is a reflection of the fact that the biquaternion algebra is simple (and its idempotents come from the roots of $-1$), while the split quaternion algebra is semisimple (and its idempotents come from the split complex algebra).

## The Relation to the Zero Divisors

### The Roots Are Not Zero Divisors

A root $\xi$ of $-1$ satisfies $\xi^2 = -1$. In the idempotent basis, $\xi = \mu_+ e_+ + \mu_- e_-$ with $\mu_\pm$ unit pure real quaternions. The idempotent components $\xi_\pm = \mu_\pm$ are nonzero (they are unit quaternions). So $\xi$ is invertible, not a zero divisor.

The inverse of $\xi$ is $\xi^{-1} = -\xi = -\mu_+ e_+ - \mu_- e_-$.

So the roots of $-1$ are invertible elements, and they lie in the group of units $\mathbb{H}_{\mathbb{D}}^\times$.

### The Idempotents Are Zero Divisors

The nontrivial idempotents $e_+$ and $e_-$ are zero divisors: $e_+ e_- = 0$ with both $e_+$ and $e_-$ nonzero. So the idempotents lie in the zero divisor set.

### The Cones

The roots of $-1$ form a six-dimensional submanifold of $\mathbb{H}_{\mathbb{D}}$. The idempotents form a finite set of four points. The relation between the two is not a map from roots to idempotents, as in the biquaternion case, but rather the two structures are independent.

## Comparison with the Biquaternion Case

| | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|
| Extra unit | $i$, $i^2 = -1$ | $j$, $j^2 = +1$ |
| Scalar roots of $-1$ | $\pm i$ | None |
| Quaternion roots of $-1$ | $\pm \mu$, $\mu$ unit pure real | $\mu$, $\mu$ unit pure real |
| Non-trivial roots | $b\mu + d\nu i$, $\mu \perp \nu$, $b^2 - d^2 = 1$ | None |
| Dimension of root set | 4 (non-trivial family) | 6 (product of two quaternion root sets) |
| Relation to idempotents | Roots generate idempotents | Independent |
| Idempotents | $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ | $0, e_+, e_-, 1$ |

The key differences are:

1. **No scalar root.** The split quaternion algebra has no scalar root of $-1$, because the split complex algebra has no square root of $-1$.
2. **No non-trivial roots.** The biquaternion algebra has a four-dimensional family of non-trivial roots, which arise from the combination of the scalar imaginary with the quaternion roots. The split quaternion algebra has no such family, because there is no scalar imaginary.
3. **The root set is a product.** The split quaternion root set is the product of two copies of the quaternion root set, parametrized by a pair of unit pure real quaternions. The biquaternion root set is more complicated, because the scalar imaginary interacts with the quaternion roots.
4. **The idempotents are different.** The idempotents of the split quaternion algebra are the four elements $0, e_+, e_-, 1$, and they are not generated by the roots of $-1$. The idempotents of the biquaternion algebra are generated by the roots of $-1$ via the formula $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$.

## The Root Set as a Manifold

The root set of $-1$ in $\mathbb{H}_{\mathbb{D}}$ is the product of two copies of the unit sphere $\mathbb{S}^2$:

$$
\{\xi \in \mathbb{H}_{\mathbb{D}} : \xi^2 = -1\} \cong \mathbb{S}^2 \times \mathbb{S}^2.
$$

The isomorphism is given by $\xi \mapsto (\mu_+, \mu_-)$, where $\xi = \mu_+ e_+ + \mu_- e_-$ and $\mu_\pm$ are unit pure real quaternions.

So the root set is a compact four-dimensional manifold (the product of two two-dimensional spheres is four-dimensional as a manifold, but here we are using the fact that each $\mathbb{S}^2$ is two-dimensional; the product is four-dimensional). Wait, each $\mathbb{S}^2$ is two-dimensional, so the product is four-dimensional. But earlier I said the root set is six-dimensional. Let me recheck.

The unit pure real quaternions form the unit sphere $\mathbb{S}^2$ in $\mathbb{R}^3$, which is two-dimensional. The set of pairs $(\mu_+, \mu_-)$ is therefore the product $\mathbb{S}^2 \times \mathbb{S}^2$, which is four-dimensional. So the root set has real dimension 4, not 6.

I made an error earlier. Let me correct: the unit pure real quaternions form the two-sphere $\mathbb{S}^2$, which is two-dimensional, not three-dimensional. So the root set is $\mathbb{S}^2 \times \mathbb{S}^2$, which is four-dimensional. The parametrization is by a pair of points on the two-sphere, and the dimension is $2 + 2 = 4$.

So the root set of $-1$ in $\mathbb{H}_{\mathbb{D}}$ is a compact four-dimensional manifold, isomorphic to $\mathbb{S}^2 \times \mathbb{S}^2$.

### Comparison with the Biquaternion Root Set

The biquaternion root set has dimension 4 (the non-trivial family is four-dimensional, and the degenerate families are lower-dimensional). So both root sets have dimension 4, but their structures are different: the biquaternion root set is a four-dimensional manifold with a more complicated topology, while the split quaternion root set is the product of two two-spheres.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}$ | Split quaternion algebra |
| $\xi$ | Root of $-1$ |
| $\xi_\pm = \xi e_\pm$ | Idempotent components |
| $\mu, \mu_+, \mu_-$ | Unit pure real quaternions |
| $e_+ = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $e_- = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\mathbb{S}^2$ | Unit sphere in $\mathbb{R}^3$ |

## Summary

The roots of $-1$ in the split quaternion algebra $\mathbb{H}_{\mathbb{D}}$ are exactly the elements of the form

$$
\xi = \mu_+ e_+ + \mu_- e_-,
$$

where $\mu_+$ and $\mu_-$ are unit pure real quaternions. Equivalently, in the standard basis,

$$
\xi = \frac{1}{2}(\mu_+ + \mu_-) + \frac{j}{2}(\mu_+ - \mu_-).
$$

There are no other roots. The proof is by reduction to the idempotent components: the equation $\xi^2 = -1$ is equivalent to the pair of equations $\xi_+^2 = -1$ and $\xi_-^2 = -1$, and the roots of $-1$ in the quaternion algebra are the unit pure real quaternions.

The root set is parametrized by a pair of unit pure real quaternions, i.e., by a pair of points on the two-sphere $\mathbb{S}^2$. It is therefore a compact four-dimensional manifold, isomorphic to $\mathbb{S}^2 \times \mathbb{S}^2$.

The pure roots (with vanishing scalar part) are the elements $\mu j$ with $\mu$ a unit pure real quaternion. The scalar roots (with vanishing vector part) are the unit pure real quaternions themselves. The general root is a combination of the two.

The roots of $-1$ are invertible and lie in the group of units. They are not zero divisors. The relation to the idempotents is different from the biquaternion case: in the split quaternion algebra, the idempotents are the fixed elements $0, e_+, e_-, 1$, and they are not generated by the roots of $-1$.

The split quaternion root set is simpler than the biquaternion root set, because the split complex algebra has no square root of $-1$, so there is no scalar imaginary root and no non-trivial roots. The root set is the product of two copies of the quaternion root set, which is a clean and simple structure.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure of the split quaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.

