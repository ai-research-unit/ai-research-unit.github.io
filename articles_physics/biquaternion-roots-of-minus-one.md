# __Biquaternion Roots of Minus One__

## Introduction

This article determines the roots of $-1$ in the biquaternion algebra $\mathbb{B}$, that is, the elements $\xi\in\mathbb{B}$ satisfying $\xi^2 = -1$; it also records the roots of $+1$ and the relation between the two. It follows *Biquaternion Idempotents and Projections*, where the idempotents are classified by the roots, and *Biquaternion Norm and Invertibility*, where the norm form and the invertibility criterion are established.

Physically, a root of $-1$ is an **imaginary unit** of the algebra, and the imaginary units are what the framework's transformations are generated from. Each root generates a one-parameter circle subgroup, $\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi$, and the three families of roots are three physically distinct kinds of generator:

- the **trivial roots** $\pm i$ generate the central phase, the abelian gauge group the framework supplies canonically;
- the **real roots** $\pm\mu$, with $\mu$ a unit pure real quaternion, generate the spatial rotations: $\mu$ is a rotation axis, the sphere of real roots is the sphere of axes, and the associated idempotents are the pure states;
- the **non-trivial roots** $b\mu+d\nu i$ generate the mixed transformations, an elliptic combination of a rotation about $\mu$ and a boost along $\nu$, with $b$ and $d$ the hyperbolic functions of a rapidity.

The roots of $+1$ are the **involutions**: the reflections and the parity-type operators, of which the fermion parity $(-1)^F = ie_3$ is an example, and each of which splits the algebra into a complementary pair of projectors. Generators whose square is neither $-1$ nor $+1$ but $0$ — the **parabolic** generators — are exactly the null elements, and they are treated in *Biquaternion Zero Divisors*.

**Conventions.** The quaternion basis is $e_0 = 1,e_1,e_2,e_3$ and the scalar imaginary is $i$, so that it does not collide with the quaternion units; a general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The conjugations are $\bar{\tilde{Q}}$, $\tilde{Q}^*$ and $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. The material coordinate is $ict\,e_0+\mathbf{x}$ and the informational coordinate is $ct'\,e_0+i\mathbf{x}'$.

## The Problem and Its Reduction

### Statement

A **root of $-1$** in $\mathbb{B}$ is an element $\xi$ with $\xi^2 = -1$.

### Vector-Part Decomposition

Write $\xi$ in scalar-vector form,

$$
\xi = Q_0+\mathbf{Q}, \qquad Q_0\in\mathbb{C}, \qquad \mathbf{Q} = Q_1e_1+Q_2e_2+Q_3e_3 ,
$$

with $Q_0$ the complex scalar part and $\mathbf{Q}$ the complex vector part. The square is given by the product formula,

$$
\xi^2 = \left(Q_0^2-(\mathbf{Q},\mathbf{Q})\right)e_0+2Q_0\mathbf{Q}, \qquad (\mathbf{Q},\mathbf{Q}) = Q_1^2+Q_2^2+Q_3^2 ,
$$

so the scalar part of $\xi^2$ is $(Q_0^2-(\mathbf{Q},\mathbf{Q}))e_0$ and the vector part is $2Q_0\mathbf{Q}$.

### Reduction to Two Cases

Equating $\xi^2$ to $-e_0$ requires

$$
2Q_0\mathbf{Q} = 0, \qquad Q_0^2-(\mathbf{Q},\mathbf{Q}) = -1 .
$$

Since $\mathbb{C}$ is a field, $Q_0\mathbf{Q} = 0$ holds if and only if $Q_0 = 0$ or $\mathbf{Q} = 0$, so the roots split into two cases.

**Case 1: $\mathbf{Q} = 0$.** Then $\xi = Q_0e_0$ is a complex scalar and $Q_0^2 = -1$, so $Q_0 = \pm i$:

$$
\xi = \pm i ,
$$

the **trivial roots**.

**Case 2: $Q_0 = 0$.** Then $\xi = \mathbf{Q}$ is **pure** and $(\mathbf{Q},\mathbf{Q}) = 1$. The **pure roots** are the pure biquaternions whose square is $-1$.

The cases are disjoint: the trivial roots have vanishing vector part, the pure roots vanishing scalar part.

### The Pure Roots

Write $Q_k = q_k+iq'_k$ with $q_k,q'_k\in\mathbb{R}$. Then

$$
(\mathbf{Q},\mathbf{Q}) = \sum_{k=1}^{3}(q_k^2-q'^2_k)+2i\sum_{k=1}^{3}q_kq'_k ,
$$

so equating real and imaginary parts to $1$ and $0$ gives, with $\mathbf{q} = (q_1,q_2,q_3)$ and $\mathbf{q}' = (q'_1,q'_2,q'_3)$,

$$
|\mathbf{q}|^2-|\mathbf{q}'|^2 = 1, \qquad \mathbf{q}\cdot\mathbf{q}' = 0 .
$$

The first condition gives $|\mathbf{q}|^2 = 1+|\mathbf{q}'|^2\geq1>0$, so $\mathbf{q}\neq0$.

**Sub-case 2a: $\mathbf{q}' = 0$.** Then $|\mathbf{q}| = 1$: $\mathbf{q}$ is a unit vector in $\mathbb{R}^3$, and $\xi = \mu$ with $\mu$ a unit pure real quaternion, for which $\mu^2 = -1$ by the standard quaternion fact. These are the **real roots**; $\mu$ ranges over the whole unit sphere $S^2\subset\mathbb{R}^3$, and since $S^2$ is invariant under $\mu\mapsto-\mu$ the family may also be written in the redundant form $\xi = \pm\mu$.

**Sub-case 2b: $\mathbf{q}'\neq0$.** Normalise: $\mu = \mathbf{q}/|\mathbf{q}|$ and $\nu = \mathbf{q}'/|\mathbf{q}'|$ are unit pure real quaternions, and $\mathbf{q}\cdot\mathbf{q}' = 0$ becomes $\mu\perp\nu$. With $b = |\mathbf{q}|>0$ and $d = |\mathbf{q}'|>0$,

$$
\mathbf{Q} = \mathbf{q}+i\mathbf{q}' = b\mu+d\nu i, \qquad b^2-d^2 = 1 .
$$

These are the **non-trivial roots**.

### Summary of the Reduction

Every root of $-1$ falls into one of three families:

1. $\xi = \pm i$ (trivial roots);
2. $\xi = \pm\mu$ with $\mu$ a unit pure real quaternion (real roots);
3. $\xi = b\mu+d\nu i$ with $\mu,\nu$ perpendicular unit pure real quaternions and $b,d>0$ satisfying $b^2-d^2 = 1$ (non-trivial roots).

## The Classification

### Statement of the Theorem

**Theorem.** The roots of $-1$ in $\mathbb{B}$ are exactly the elements

$$
\xi = \pm i, \qquad \xi = \pm\mu, \qquad \xi = b\mu+d\nu i ,
$$

with $\mu,\nu$ perpendicular unit pure real quaternions and $b,d>0$ satisfying $b^2-d^2 = 1$.

### Verification

**Trivial root.** $(\pm i)^2 = -1$ since $i^2 = -1$. ✓

**Real roots.** For a unit pure real quaternion $\mu$, $\mu^2 = -1$ (the unit pure real quaternions are the unit sphere in $\mathbb{R}^3$, and every such element squares to $-1$); so $(\pm\mu)^2 = \mu^2 = -1$. ✓

**Non-trivial roots.** Compute

$$
\xi^2 = (b\mu+d\nu i)^2 = b^2\mu^2+d^2\nu^2i^2+bd(\mu\nu+\nu\mu)i .
$$

Here $\mu^2 = \nu^2 = -1$ and $i^2 = -1$, so the first two terms sum to $-(b^2-d^2)e_0$. For the cross term, use the product formula for pure quaternions, $\mu\nu = -\mu\cdot\nu+\mu\times\nu$ and $\nu\mu = -\mu\cdot\nu-\mu\times\nu$, whence $\mu\nu+\nu\mu = -2(\mu\cdot\nu)e_0$, which vanishes because $\mu\perp\nu$. Therefore

$$
\xi^2 = -(b^2-d^2)e_0 = -1 ,
$$

using the constraint. ✓

### Degenerate Cases

**The real roots are the boundary of the non-trivial family.** If $d\to0$ in the non-trivial family then $b^2\to1$ and $\xi = b\mu+d\nu i\to\mu$, a real root; the direction $\nu$ becomes undetermined in the limit. So the real roots (the sphere $S^2$) form the boundary of the non-trivial family.

**The trivial roots are separate.** The trivial roots have vanishing vector part, and neither the real nor the non-trivial roots (both with $\mathbf{Q}\neq0$) include or approach them, so they are two isolated points.

### The Roots as Generators

Because $\xi^2 = -1$, the exponential of $\xi$ closes on a circle:

$$
\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi, \qquad \theta\in\mathbb{R},
$$

so **each root generates a one-parameter subgroup** of the group of units. For a pure generator $\xi$ the square is a scalar, $\xi^2 = -(\xi,\xi)e_0$, and the three cases physics distinguishes are:

- $\xi^2 = -1$: a root of $-1$, an **elliptic** generator, whose exponential $\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi$ is a compact circle subgroup;
- $\xi^2 = +1$: a root of $+1$, a **hyperbolic** generator, whose exponential $\exp(\theta\xi) = \cosh\theta\,e_0+\sinh\theta\,\xi$ is a non-compact one-parameter subgroup;
- $\xi^2 = 0$: a **parabolic** (null) generator: it is nilpotent, its exponential is the polynomial subgroup $\exp(\theta\xi) = e_0+\theta\xi$, and $\xi$ itself is a zero divisor rather than a unit.

Every pure element with $(\xi,\xi)\neq0$ is a complex scale multiple of a root of $-1$, and a pure element is nilpotent exactly when $(\xi,\xi) = 0$. Up to scale, therefore, the pure generators are the two root families together with the nilpotent cone.

**Physical reading.** The elliptic generators are the rotations: a real root $\mu$ is a rotation axis, and the rotation through an angle is conjugation by $\exp(\tfrac{\theta}{2}\mu)$, which sends a vector $\mathbf{v}$ to its rotation about $\mu$ by $\theta$. The hyperbolic generators are the boosts: a pure boost is generated by $i\nu$, whose square is $+\nu^2 = +1$, a root of $+1$ and not of $-1$. The parabolic generators are the null directions, and they are the zero divisors. So the trichotomy elliptic/hyperbolic/parabolic of Lorentz-type generators is, in this algebra, exactly the trichotomy of the square of a pure element: $-1$, $+1$, $0$.

### Parametrization by Hyperbolic Functions

The constraint $b^2-d^2 = 1$ is a hyperbola; on the branch $b>0$,

$$
b = \cosh t, \qquad d = \sinh t, \qquad t\in\mathbb{R},
$$

giving

$$
\xi = \cosh t\,\mu+\sinh t\,\nu i, \qquad \mu\perp\nu, \quad |\mu| = |\nu| = 1 .
$$

The parameter $t$ is the **rapidity** of the root, by analogy with the rapidity of a hyperbolic rotation.

**Physical reading.** The rapidity is not an analogy but the same parameter: the pair $(b,d) = (\cosh t,\sinh t)$ is the standard hyperbolic parametrisation of a boost, and the mixed root is the generator of a transformation that is a rotation about $\mu$ composed with a boost along $\nu$. The real roots are the case $t = 0$; the trace of the asymptotic value $\nu$ in the degenerate limit $d\to0$ is the reason the boundary of the non-trivial family is the sphere of rotation axes. A mixed root is therefore the algebra's normalised way of writing "a rotation and a boost taken together, with the generator squaring to $-1$".

### Status of the Roots

The **non-trivial** roots form a **four-real-dimensional** family, parametrised by

- $\mu\in S^2$ (two real parameters);
- $\nu$ on the unit circle in the plane perpendicular to $\mu$ (one parameter);
- $(b,d)$ on the branch $b^2-d^2 = 1$ with $b,d>0$ (one parameter);

giving $2+1+1 = 4$ real dimensions. The **real** roots form a two-dimensional submanifold, the sphere $S^2$, the boundary of the non-trivial family. The **trivial** roots are two isolated points. So the set of roots of $-1$ is a stratified space whose largest stratum is four-dimensional.

All roots except the trivial ones are **pure**, hence sit in the six-real-dimensional space of pure biquaternions. The roots are neither idempotents ($\xi^2 = -1\neq\xi$) nor zero divisors ($N(\xi)\neq0$ in every case): they lie in the group of units $\mathbb{B}^\times$. **Physically: an imaginary unit is a group element, never a state and never a null direction.**

## The Relation to the Idempotents

The classification of the roots gives the classification of the idempotents: the map

$$
\xi\longmapsto P_+(\xi) = \tfrac{1}{2}(e_0+\xi i)
$$

is a bijection from the roots of $-1$ onto the idempotents, under which the complementary pairs $\{\tilde{P},e_0-\tilde{P}\}$ correspond to the classes $\{\xi,-\xi\}$, and under which the three families of roots give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and the idempotents lying in none of the four four-dimensional subspaces. The construction of the idempotent, the proof of the bijection and the projection interpretation are the subject of *Biquaternion Idempotents and Projections*.

**Physical reading.** The correspondence is why the framework can speak of a state direction as an algebraic datum of the same kind as a generator: a root $\xi$ is an imaginary unit, its associated projector $P_+(\xi)$ is a pure state, and the sphere of real roots is the sphere of pure states. The rotation axis and the state direction are the same direction.

## The Relation to the Zero Divisors

### The Idempotents as Zero Divisors

Every non-trivial idempotent is a zero divisor, $\tilde{P}(e_0-\tilde{P}) = 0$ with both factors nonzero, so the non-trivial idempotents form a subset of the zero divisor set studied in *Biquaternion Zero Divisors*. The trivial idempotents $0$ and $e_0$ are not zero divisors: $0$ is excluded by the definition and $N(e_0) = 1\neq0$.

### The Roots as Invertible Elements

A root of $-1$ is **not** a zero divisor. Its norm form is

$$
N(\xi) = \xi\bar{\xi} = \begin{cases}-1 & \text{for the trivial roots } \xi = \pm i,\\ +1 & \text{for a pure root},\end{cases}
$$

so $N(\xi)\neq0$ and $\xi$ is invertible. For a pure root the inverse is explicit: $\xi^{-1} = \bar{\xi}/N(\xi) = -\xi$, so **a pure imaginary unit is its own negative inverse**. The roots therefore lie in the group of units, as *Biquaternion Norm and Invertibility* records.

### Dimensions

The set of roots of $-1$ is a stratified space of real dimension 4 (the non-trivial family) with a two-dimensional boundary stratum (the real roots, $S^2$) and two isolated points (the trivial roots, $\pm i$). By the bijection, the idempotents inherit this size: the non-trivial idempotents form a set of real dimension 4 with a two-dimensional boundary stratum, no isolated points, sitting inside the six-real-dimensional zero divisor set — which, as *Biquaternion Idempotents and Projections* records, is the sphere of pure states on its boundary stratum.

The non-trivial roots sit inside the six-real-dimensional space of pure biquaternions; the trivial roots are isolated points outside it. The parabolic (null) pure elements are the remaining part of that six-dimensional space, and they are the pure zero divisors of *Biquaternion Zero Divisors*.

## The Roots of Plus One

For completeness, the analogous problem for $+1$: an element $\eta$ with $\eta^2 = 1$. The roots of $+1$ are related to those of $-1$ by

$$
\eta = \xi i ,
$$

which squares to $1$ since $\xi^2i^2 = (-1)(-1) = 1$. The map $\xi\mapsto\xi i$ is a bijection: it is injective since $i$ is invertible, and if $\eta^2 = 1$ then $\xi = -\eta i$ satisfies $\xi^2 = -1$ and $\xi i = \eta$. Applying the classification:

- **Non-trivial roots of $+1$:** $\eta = b\mu i+d\nu i^2 = b\mu i-d\nu$ with $b^2-d^2 = 1$ and $\mu\perp\nu$;
- **Trivial roots of $+1$:** $\eta = \pm1$ (from $\xi = \pm i$), the only roots of $+1$ lying in the centre $\mathbb{C}$;
- **Real roots of $+1$:** $\eta = \pm\mu i$ with $\mu$ a unit pure real quaternion.

A root of $+1$ is an **involution**, and every involution splits the algebra: if $\eta^2 = 1$ then $\eta\neq1$ gives the idempotents $\tfrac12(e_0\pm\eta)$ with $\tfrac12(e_0+\eta)+\tfrac12(e_0-\eta) = e_0$ and $\tfrac12(e_0+\eta)\cdot\tfrac12(e_0-\eta) = 0$, which is the bijection above read in the other direction.

**Physical reading: the reflections and the parities.** The roots of $+1$ are the algebra's reflections. The real roots $\pm\mu i$ are the Hermitian ones — $(\mu i)^\dagger = \mu i$ — so they are exactly the involutions that split the algebra into **orthogonal** projectors, and they are the parity-type operators of the framework. The fermion parity of the field-theory articles is an instance: $(-1)^F = ie_3$ is a real root of $+1$ (with $\mu = e_3$), Hermitian, and its associated projectors are $\tfrac12(e_0\pm ie_3)$, the vacuum projector $P_+(e_3)$ and its complement. The trivial roots $\pm1$ are the two central involutions (the identity and the total sign), and the non-trivial roots are the non-Hermitian involutions, which split the algebra into complementary projectors that are not orthogonal. See *The Biquaternion Vacuum as a Minimal Idempotent* and *Bogoliubov Transformations in Biquaternionic Form* for the parity and vacuum instances. Beyond the framework, the roots of $+1$ generate the hyperbolic subgroups, which is where the boosts of *The Lorentz Group as Biquaternion Norm-Form Automorphisms* come from.

## Summary

The roots of $-1$ in the biquaternion algebra are exactly:

1. **Non-trivial roots:** $\xi = b\mu+d\nu i$, with $\mu,\nu$ perpendicular unit pure real quaternions and $b,d>0$ satisfying $b^2-d^2 = 1$;
2. **Trivial roots:** $\xi = \pm i$;
3. **Real roots:** $\xi = \pm\mu$ with $\mu$ a unit pure real quaternion.

The proof writes $\xi = Q_0+\mathbf{Q}$, squares using the biquaternion product formula and equates to $-1$: the vector part $2Q_0\mathbf{Q}$ forces $Q_0 = 0$ or $\mathbf{Q} = 0$; the scalar part $Q_0^2-(\mathbf{Q},\mathbf{Q})$ then gives the trivial root in the scalar case and, in the pure case, reduces to $(\mathbf{Q},\mathbf{Q}) = 1$, which splits into the real and non-trivial families according to whether the imaginary part of the pure element vanishes.

The non-trivial roots form a four-real-dimensional family with the real roots (a sphere $S^2$) as boundary, and the trivial roots are two isolated points. All roots except the trivial ones are pure, and they lie in the group of units: a pure root has norm form $+1$ and inverse $-\xi$, the trivial roots have norm form $-1$. Physically, the roots are the imaginary units of the algebra and generate its circle subgroups: $\pm i$ the central phase, the sphere of real roots the rotations about the spatial axes, the non-trivial roots the mixed rotation–boost generators with rapidity $t$ in $b = \cosh t$, $d = \sinh t$. The three families of roots classify the idempotents through $\xi\mapsto\tfrac12(e_0+\xi i)$; the associated projectors are the pure states for the real roots and non-orthogonal projectors for the non-trivial ones. The parabolic generators, whose square is $0$ rather than $\pm1$, are the null elements and belong to the zero-divisor theory.

The roots of $+1$ are the involutions, obtained from the roots of $-1$ by multiplication by $i$; the real ones are the Hermitian reflections, of which the fermion parity $ie_3$ is an instance, and each splits the algebra into a complementary pair of projectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1,e_1,e_2,e_3$ | Quaternion basis |
| $i$ | Central scalar imaginary |
| $\xi$ | Root of $-1$: an imaginary unit, an elliptic generator |
| $\eta$ | Root of $+1$: an involution, a hyperbolic generator |
| $Q_0$ | Complex scalar part of the root |
| $\mathbf{Q} = Q_1e_1+Q_2e_2+Q_3e_3$ | Complex vector part of the root |
| $\mu,\nu$ | Unit pure real quaternions (spatial directions) |
| $b,d$ | Real parameters with $b^2-d^2 = 1$ |
| $t$ | Rapidity: $b = \cosh t$, $d = \sinh t$ |
| $\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi$ | The circle subgroup generated by a root |
| $\tilde{P} = \tfrac12e_0\pm\tfrac12\xi i$ | The idempotent of the root |
| $(-1)^F = ie_3$ | Fermion parity: a Hermitian root of $+1$ |
| $ict\,e_0+\mathbf{x}$, $ct'\,e_0+i\mathbf{x}'$ | Material and informational coordinates |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the original classification.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the relation to the idempotents and the zero divisors.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the representation theory and the constraint verification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
