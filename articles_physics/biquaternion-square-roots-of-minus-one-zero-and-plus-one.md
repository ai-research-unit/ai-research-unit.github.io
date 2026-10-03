# __Biquaternion Square Roots of Minus One, Zero and Plus One__

## Introduction

This article determines the square roots of the three central values $-1$, $0$ and $+1$ in the biquaternion algebra $\mathbb{B}$ — the elements $\xi\in\mathbb{B}$ satisfying $\xi^2 = -1$, $\xi^2 = 0$ and $\xi^2 = +1$ — and the relations among the three sets. It relates to *Biquaternion Idempotents and Projections* through the bijection between the roots of $-1$ and the idempotents. The square roots of an arbitrary element $Q$, and the Clifford-algebra algorithm that computes them, are *Biquaternion Square Roots of a General Element*; the three sets found here are the degenerate data of that classification, and the algorithm is deliberately not reproduced.

Physically, a root of $-1$ is an **imaginary unit** of the algebra, and the imaginary units are what the framework's transformations are generated from. Each root generates a one-parameter subgroup, $\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi$, and the three families of roots are three physically distinct kinds of generator:

- the **trivial roots** $\pm i$ generate the central phase, the abelian gauge group the framework supplies canonically;
- the **real roots** $\pm\mu$, with $\mu$ a pure real quaternion with $\mu^2 = -1$, generate the spatial rotations: $\mu$ is a rotation axis, and the associated idempotents are the pure states;
- the **non-trivial roots** $b\mu+d\nu i$ generate the mixed transformations, an elliptic combination of a rotation about $\mu$ and a boost along $\nu$, with $b$ and $d$ the hyperbolic functions of a rapidity.

The roots of $+1$ are the **involutions**: the reflections and the parity-type operators, of which the fermion parity $(-1)^F = ie_3$ is an example, and each of which splits the algebra into a complementary pair of projectors. Generators whose square is neither $-1$ nor $+1$ but $0$ — the **parabolic** generators — are exactly the null elements.

**Conventions.** The quaternion basis is $e_0 = 1,e_1,e_2,e_3$ and the scalar imaginary is $i$, so that it does not collide with the quaternion units; a general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The conjugations are $\tilde{Q}^{\natural}$, $\bar{\tilde{Q}}$ and $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The material coordinate is $ict\,e_0+\mathbf{x}$ and the informational coordinate is $ct'\,e_0+i\mathbf{x}'$. Throughout, $\mu$ and $\nu$ denote pure real quaternions with $\mu^2 = \nu^2 = -1$, and such a pair **anticommutes** when $\mu\nu + \nu\mu = 0$.

## The Problem and Its Reduction

The three problems of this article — the equations $\xi^2 = -1$, $\xi^2 = 0$ and $\xi^2 = +1$ — share one reduction, carried out once here and applied three times. Write $\xi$ in scalar-vector form,

$$
\xi = Q_0+\mathbf{Q}, \qquad Q_0\in\mathbb{C}, \qquad \mathbf{Q} = Q_1e_1+Q_2e_2+Q_3e_3 ,
$$

with $Q_0$ the complex scalar part and $\mathbf{Q}$ the complex vector part. The square is given by the product formula,

$$
\xi^2 = \left(Q_0^2-(\mathbf{Q},\mathbf{Q})\right)e_0+2Q_0\mathbf{Q}, \qquad (\mathbf{Q},\mathbf{Q}) = Q_1^2+Q_2^2+Q_3^2 ,
$$

so the scalar part of $\xi^2$ is $(Q_0^2-(\mathbf{Q},\mathbf{Q}))e_0$ and the vector part is $2Q_0\mathbf{Q}$, so that equating $\xi^2$ to a central value splits the equation into a vector part and a scalar part.

## The Roots of Minus One

### Statement

A **root of $-1$** in $\mathbb{B}$ is an element $\xi$ with $\xi^2 = -1$.

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
(\mathbf{Q},\mathbf{Q}) = \sum_{k=1}^{3}(q_k^2-(q'_k)^2)+2i\sum_{k=1}^{3}q_kq'_k ,
$$

so equating real and imaginary parts to $1$ and $0$ gives

$$
\sum_{k=1}^{3} q_k^2-\sum_{k=1}^{3} (q'_k)^2 = 1, \qquad \sum_{k=1}^{3} q_k q'_k = 0 .
$$

The first condition gives $\sum_k q_k^2 = 1+\sum_k (q'_k)^2\geq1>0$, so the triple $(q_1,q_2,q_3)$ is nonzero.

**Sub-case 2a: $\mathbf{q}' = 0$.** Then $\sum_k q_k^2 = 1$. Let $\mu = q_1e_1+q_2e_2+q_3e_3$, a pure real quaternion with $\mu^2 = -\bigl(\sum_k q_k^2\bigr)e_0 = -1$, so $\xi = \mu$. These are the **real roots**; the family is invariant under $\mu\mapsto-\mu$, and it may also be written in the redundant form $\xi = \pm\mu$.

**Sub-case 2b: $\mathbf{q}'\neq0$.** Put $b = \bigl(\sum_k q_k^2\bigr)^{1/2}>0$ and $d = \bigl(\sum_k (q'_k)^2\bigr)^{1/2}>0$, and define the pure real quaternions $\mu = \sum_k (q_k/b)e_k$ and $\nu = \sum_k (q'_k/d)e_k$. Then $\mu^2 = \nu^2 = -1$, and $\sum_k\mu_k\nu_k = \frac{1}{bd}\sum_k q_kq'_k = 0$, so $\mu\nu+\nu\mu = -2\bigl(\sum_k\mu_k\nu_k\bigr)e_0 = 0$: the two anticommute. With $\mathbf{q} = b\mu$, $\mathbf{q}' = d\nu$ and $b^2-d^2 = 1$,

$$
\mathbf{Q} = \mathbf{q}+i\mathbf{q}' = b\mu+d\nu i .
$$

These are the **non-trivial roots**.

### Statement of the Theorem

**Theorem.** The roots of $-1$ in $\mathbb{B}$ are exactly the elements

$$
\xi = \pm i, \qquad \xi = \pm\mu, \qquad \xi = b\mu+d\nu i ,
$$

with $\mu,\nu$ pure real quaternions with $\mu^2 = \nu^2 = -1$ and $\mu\nu+\nu\mu = 0$, and $b,d>0$ satisfying $b^2-d^2 = 1$.

### Verification

**Trivial root.** $(\pm i)^2 = -1$ since $i^2 = -1$. ✓

**Real roots.** For a pure real quaternion $\mu$ with $\mu^2 = -1$, $(\pm\mu)^2 = \mu^2 = -1$. ✓

**Non-trivial roots.** Compute

$$
\xi^2 = (b\mu+d\nu i)^2 = b^2\mu^2+d^2\nu^2i^2+bd(\mu\nu+\nu\mu)i .
$$

Here $\mu^2 = \nu^2 = -1$ and $i^2 = -1$, so the first two terms sum to $-(b^2-d^2)e_0$. The cross term $bd(\mu\nu+\nu\mu)i$ vanishes because $\mu$ and $\nu$ anticommute. Therefore

$$
\xi^2 = -(b^2-d^2)e_0 = -1 ,
$$

using the constraint. ✓

### Degenerate Cases

**The real roots as the case $d = 0$.** In the non-trivial family the constraint $b^2-d^2 = 1$ is carried with $d>0$. If the condition $d>0$ is relaxed to $d\geq0$, then $d = 0$ forces $b = 1$ and $\xi = \mu$, a real root; the element $\nu$ no longer enters. So the real roots are the case $d = 0$ of the non-trivial formula, not a separate construction.

**The trivial roots are separate.** The trivial roots have vanishing vector part, and the real and non-trivial roots all have $\mathbf{Q}\neq0$. So the roots with vanishing vector part are exactly $\pm i$, which form a separate family.

### The Roots as Generators

Because $\xi^2 = -1$, the exponential of $\xi$ closes:

$$
\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi, \qquad \theta\in\mathbb{R},
$$

so **each root generates a one-parameter subgroup** of the group of units. For a pure generator $\xi$ the square is a scalar, $\xi^2 = -(\xi,\xi)e_0$, and the three cases physics distinguishes are:

- $\xi^2 = -1$: a root of $-1$, an **elliptic** generator, whose exponential $\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi$ is a one-parameter subgroup;
- $\xi^2 = +1$: a root of $+1$, a **hyperbolic** generator, whose exponential $\exp(\theta\xi) = \cosh\theta\,e_0+\sinh\theta\,\xi$ is a one-parameter subgroup;
- $\xi^2 = 0$: a **parabolic** (null) generator: it is nilpotent, its exponential is the polynomial subgroup $\exp(\theta\xi) = e_0+\theta\xi$, and $\xi$ itself is a zero divisor rather than a unit.

Every pure element with $(\xi,\xi)\neq0$ is a complex scale multiple of a root of $-1$, and a pure element is nilpotent exactly when $(\xi,\xi) = 0$. Up to scale, therefore, the pure generators are the two root families together with the nilpotent cone.

**Physical reading.** The elliptic generators are the rotations: a real root $\mu$ is a rotation axis, and the rotation through an angle is conjugation by $\exp(\tfrac{\theta}{2}\mu)$, which sends a vector $\mathbf{v}$ to its rotation about $\mu$ by $\theta$. The hyperbolic generators are the boosts: a pure boost is generated by $i\nu$, whose square is $+\nu^2 = +1$, a root of $+1$ and not of $-1$. The parabolic generators are the null directions, and they are the zero divisors. So the trichotomy elliptic/hyperbolic/parabolic of Lorentz-type generators is, in this algebra, exactly the trichotomy of the square of a pure element: $-1$, $+1$, $0$.

### Parametrization by Hyperbolic Functions

The constraint $b^2-d^2 = 1$ with $b>0$ is parametrised by

$$
b = \cosh t, \qquad d = \sinh t, \qquad t\in\mathbb{R},
$$

giving

$$
\xi = \cosh t\,\mu+\sinh t\,\nu i, \qquad \mu^2 = \nu^2 = -1, \quad \mu\nu+\nu\mu = 0 .
$$

The parameter $t$ is the **rapidity** of the root, by analogy with the rapidity of a hyperbolic rotation.

**Physical reading.** The rapidity is not an analogy but the same parameter: the pair $(b,d) = (\cosh t,\sinh t)$ is the standard hyperbolic parametrisation of a boost, and the mixed root is the generator of a transformation that is a rotation about $\mu$ composed with a boost along $\nu$. The real roots are the case $t = 0$; at $d = 0$ the element $\nu$ drops out and the root is $\mu$. A mixed root is therefore the algebra's way of writing "a rotation and a boost taken together, with the generator squaring to $-1$".

### Status of the Roots

The **trivial** roots are the two elements $\pm i$. The **real** roots are the elements $\pm\mu$ with $\mu$ a pure real quaternion of square $-1$; the single constraint $\sum_k\mu_k^2 = 1$ on the three real coefficients leaves two free real parameters. The **non-trivial** roots are parametrised by the pair $(\mu,\nu)$ with $\mu^2 = \nu^2 = -1$ and $\mu\nu+\nu\mu = 0$ — two free real parameters for $\mu$, and one for $\nu$, its two constraints $\sum_k\nu_k^2 = 1$ and $\sum_k\mu_k\nu_k = 0$ acting on three real coefficients — together with the pair $(b,d)$ with $b^2-d^2 = 1$ and $b,d>0$, one further parameter: four free real parameters in all.

All roots except the trivial ones are **pure**, hence lie in the six-real-dimensional vector subspace of pure biquaternions. The roots are neither idempotents ($\xi^2 = -1\neq\xi$) nor zero divisors (§*The Roots as Invertible Elements*): they lie in the group of units $\mathbb{B}^\times$. **Physically: an imaginary unit is a group element, never a state and never a null direction.**

## The Roots of Zero

### Reduction to Two Cases

A root of $0$ is an element with $\xi^2 = 0$. With $\xi = Q_0+\mathbf{Q}$ the square is $(Q_0^2-(\mathbf{Q},\mathbf{Q}))e_0+2Q_0\mathbf{Q}$, and equating it to $0$ forces the same choice $Q_0 = 0$ or $\mathbf{Q} = 0$ as for the roots of $-1$.

- **Case $\mathbf{Q} = 0$.** Then $\xi = Q_0e_0$ and $Q_0^2 = 0$; since $\mathbb{C}$ is a field, $Q_0 = 0$. This gives the single element $\xi = 0$.
- **Case $Q_0 = 0$.** Then $\xi = \mathbf{Q}$ is pure with $(\mathbf{Q},\mathbf{Q}) = 0$, that is $Q_1^2+Q_2^2+Q_3^2 = 0$.

### Statement of the Theorem

**Theorem.** The roots of $0$ in $\mathbb{B}$ are $\xi = 0$ together with the pure elements $\xi = Q_1e_1+Q_2e_2+Q_3e_3$ with $Q_1^2+Q_2^2+Q_3^2 = 0$.

### Verification

For such a pure element both the scalar part $-(\mathbf{Q},\mathbf{Q})$ and the vector part $2Q_0\mathbf{Q}$ of the square vanish. ✓

The nonzero roots of $0$ are the **nilpotents** of the algebra, and they form the **nilpotent cone** of the pure subspace; the instance $\xi = e_1+ie_2$ gives $\xi^2 = e_1^2+i^2e_2^2+i(e_1e_2+e_2e_1) = -1+1+0 = 0$. The set is the zero-divisor set of the algebra, whose structure, its two families and the criterion in terms of the scalar part, is *Biquaternion Zero Divisors*; it is named here only to complete the list of the three central values and not developed.

**Physical reading: the parabolic generators and the null momenta.** A root of $0$ is a **parabolic** generator: its exponential is the polynomial subgroup $\exp(\theta\xi) = e_0+\theta\xi$, and the element itself is a zero divisor rather than a unit. The three central values are therefore the three kinds of one-parameter generator the framework uses: $-1$ the elliptic generators (the central phase and the rotations), $+1$ the hyperbolic ones (the boosts and the parities), and $0$ the parabolic ones (the null translations). The physical instance is the **photon**: a null momentum $p$ with $p^2 = 0$ is a parabolic generator, and the pure null elements such as $e_1+ie_2$ are the two sectors' null directions. The parabolic generators sit at the boundary of the group of units, which is the light cone of the material and informational sectors; the null readings are developed in *Biquaternion Zero Divisors*.

## The Roots of Plus One

### Statement of the Theorem

The analogous problem for $+1$, an element $\eta$ with $\eta^2 = 1$, is also recorded. The roots of $+1$ are related to those of $-1$ by

$$
\eta = \xi i ,
$$

where $\xi$ is a root of $-1$. Applying the classification:

- **Non-trivial roots of $+1$:** $\eta = b\mu i+d\nu i^2 = b\mu i-d\nu$ with $b^2-d^2 = 1$ and $\mu\nu+\nu\mu = 0$;
- **Trivial roots of $+1$:** $\eta = \pm1$ (from $\xi = \pm i$), the only roots of $+1$ lying in the centre $\mathbb{C}$;
- **Real roots of $+1$:** $\eta = \pm\mu i$ with $\mu$ a pure real quaternion with $\mu^2 = -1$.

### Verification

That $\eta = \xi i$ satisfies $\eta^2 = 1$ follows since $\xi^2i^2 = (-1)(-1) = 1$. The map $\xi\mapsto\xi i$ is a bijection: it is injective since $i$ is invertible, and if $\eta^2 = 1$ then $\xi = -\eta i$ satisfies $\xi^2 = -1$ and $\xi i = \eta$. ✓

A root of $+1$ is an **involution**, and every involution splits the algebra: if $\eta^2 = 1$ then $\eta\neq1$ gives the idempotents $\tfrac12(e_0\pm\eta)$ with $\tfrac12(e_0+\eta)+\tfrac12(e_0-\eta) = e_0$ and $\tfrac12(e_0+\eta)\cdot\tfrac12(e_0-\eta) = 0$, which is the bijection above read in the other direction.

**Physical reading: the reflections and the parities.** The roots of $+1$ are the algebra's reflections. The real roots $\pm\mu i$ are the Hermitian ones — $(\mu i)^{*} = \mu i$ — so they are exactly the involutions that split the algebra into **orthogonal** projectors, and they are the parity-type operators of the framework. The fermion parity of the field-theory articles is an instance: $(-1)^F = ie_3$ is a real root of $+1$ (with $\mu = e_3$), Hermitian, and its associated projectors are $\tfrac12(e_0\pm ie_3)$, the vacuum projector $\tilde\Pi_1$ and its complement. The trivial roots $\pm1$ are the two central involutions (the identity and the total sign), and the non-trivial roots are the non-Hermitian involutions, which split the algebra into complementary projectors that are not orthogonal. Beyond the framework, the roots of $+1$ generate the hyperbolic one-parameter subgroups that carry the boosts.

## The Three Sets Compared

The three root sets are related by their invertibility. The roots of $-1$ and of $+1$ are **units**: a root $\xi$ of $\pm1$ satisfies $\xi^{-1} = \pm\xi$, in $\mathbb{B}^\times$. The nonzero roots of $0$ are the exception: they are nilpotents, hence zero divisors and not units. So of the three central values only $0$ has non-unit roots.

The three sets also differ in kind. The roots of $-1$ are two isolated elements together with a two-parameter family and a four-parameter family; the roots of $+1$ are the bijective image of that set under $\xi\mapsto\xi i$; and the roots of $0$ are the single element $0$ together with one four-parameter family, the nilpotent cone. In particular the roots of $0$ contain no unit, and the only non-pure roots of the three values are the trivial ones, $\pm i$ for $-1$ and $\pm1$ for $+1$.

**Physical reading.** The three sets are the three kinds of one-parameter generator: the elliptic ones from $-1$, the hyperbolic ones from $+1$, and the parabolic ones from $0$. Only the first two lie in the group of units, and only the third lies on the light cone of the two sectors; a generator is therefore classified by the sign of its square.

## The Relation to the Idempotents

The classification of the roots of $-1$ gives the classification of the idempotents: the map

$$
\xi\longmapsto \tilde\Pi(\xi) = \tfrac{1}{2}(e_0+\xi i)
$$

is a bijection from the roots of $-1$ onto the idempotents, under which the complementary pairs $\{\tilde\Pi,e_0-\tilde\Pi\}$ correspond to the classes $\{\xi,-\xi\}$, and under which the three families of roots give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and the idempotents lying in none of the four four-dimensional subspaces. The construction of the idempotent, the proof of the bijection and the projection interpretation are the subject of *Biquaternion Idempotents and Projections*.

**Physical reading.** The correspondence is why the framework can speak of a state direction as an algebraic datum of the same kind as a generator: a root $\xi$ is an imaginary unit, its associated projector $\tilde\Pi(\xi)$ is a pure state, and the family of real roots is the family of pure states. The rotation axis and the state direction are the same direction.

## The Relation to the Zero Divisors

### The Idempotents as Zero Divisors

Every non-trivial idempotent is a zero divisor, $\tilde\Pi(e_0-\tilde\Pi) = 0$ with both factors nonzero (the construction of $\tilde\Pi$ is in *Biquaternion Idempotents and Projections*). The trivial idempotents $0$ and $e_0$ are not zero divisors: $0$ is excluded by the definition, and $e_0$ is a unit.

### The Roots as Invertible Elements

A root of $-1$ is a unit and **not** a zero divisor. Indeed, $\xi^2 = -1$ gives

$$
\xi\,(-\xi) = (-\xi)\,\xi = e_0,
$$

so $\xi$ is invertible, with inverse $\xi^{-1} = -\xi$; in particular **a pure imaginary unit is its own negative inverse**. A unit is not a zero divisor: if $\xi R = 0$ then $R = (-\xi)(\xi R) = 0$, and likewise $R\xi = 0$ forces $R = 0$. The roots therefore lie in the group of units $\mathbb{B}^\times$. The central scalar $\xi\bar{\xi}$ is $-1$ for the trivial roots and $+1$ for a pure root.

### The Remaining Pure Elements

The non-trivial roots lie in the six-real-dimensional vector subspace of pure biquaternions; the trivial roots $\pm i$ do not. The remaining pure elements, those with $(\xi,\xi) = 0$, are the parabolic (null) elements.

## Summary

This article determines the square roots of the three central values $-1$, $0$ and $+1$ in the biquaternion algebra, by one reduction applied three times, and compares the three sets in §*The Three Sets Compared*.

The roots of $-1$ in the biquaternion algebra are exactly:

1. **Non-trivial roots:** $\xi = b\mu+d\nu i$, with $\mu,\nu$ pure real quaternions with $\mu^2 = \nu^2 = -1$ and $\mu\nu+\nu\mu = 0$, and $b,d>0$ satisfying $b^2-d^2 = 1$;
2. **Trivial roots:** $\xi = \pm i$;
3. **Real roots:** $\xi = \pm\mu$ with $\mu$ a pure real quaternion with $\mu^2 = -1$.

The proof writes $\xi = Q_0+\mathbf{Q}$, squares using the biquaternion product formula and equates to $-1$: the vector part $2Q_0\mathbf{Q}$ forces $Q_0 = 0$ or $\mathbf{Q} = 0$; the scalar part $Q_0^2-(\mathbf{Q},\mathbf{Q})$ then gives the trivial root in the scalar case and, in the pure case, reduces to $(\mathbf{Q},\mathbf{Q}) = 1$, which splits into the real and non-trivial families according to whether the imaginary part of the pure element vanishes.

The trivial roots are the two elements $\pm i$; the real roots are the family $\pm\mu$ cut out by $\sum_k\mu_k^2 = 1$; the non-trivial roots carry the pairs $(\mu,\nu)$ and $(b,d)$ as above, four free real parameters in all. All roots except the trivial ones are pure, hence lie in the six-real-dimensional vector subspace of pure biquaternions. Physically, the roots are the imaginary units of the algebra and generate its one-parameter subgroups: $\pm i$ the central phase, the real roots the rotations about the spatial axes, the non-trivial roots the mixed rotation–boost generators with rapidity $t$ in $b = \cosh t$, $d = \sinh t$. The three families of roots classify the idempotents through $\xi\mapsto\tfrac12(e_0+\xi i)$; the associated projectors are the pure states for the real roots and non-orthogonal projectors for the non-trivial ones. The parabolic generators, whose square is $0$ rather than $\pm1$, are the null elements and belong to the zero-divisor theory.

The roots of $0$ are $\xi = 0$ together with the pure elements $Q_1e_1+Q_2e_2+Q_3e_3$ with $Q_1^2+Q_2^2+Q_3^2 = 0$; the nonzero ones are the nilpotents, instance $e_1+ie_2$. Physically they are the parabolic generators, whose exponential is the polynomial subgroup $e_0+\theta\xi$ and whose physical instance is the photon's null momentum; they lie at the boundary of the group of units, unlike the roots of $\pm1$, which are units. The classification of $\xi^2 = Q$ for a general $Q$ is *Biquaternion Square Roots of a General Element*, and the structure of the zero-divisor set they belong to is *Biquaternion Zero Divisors*.

The roots of $+1$ are the involutions, obtained from the roots of $-1$ by multiplication by $i$; the real ones are the Hermitian reflections, of which the fermion parity $ie_3$ is an instance, and each splits the algebra into a complementary pair of projectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1,e_1,e_2,e_3$ | Quaternion basis |
| $i$ | Central scalar imaginary |
| $\xi$ | Root of $-1$ (an elliptic generator) or of $0$ (a parabolic generator) |
| $\eta$ | Root of $+1$: an involution, a hyperbolic generator |
| $Q_0$ | Complex scalar part of the root |
| $\mathbf{Q} = Q_1e_1+Q_2e_2+Q_3e_3$ | Complex vector part of the root |
| $\mu,\nu$ | Pure real quaternions with $\mu^2 = \nu^2 = -1$ (spatial directions) |
| $b,d$ | Real parameters with $b^2-d^2 = 1$ |
| $t$ | Rapidity: $b = \cosh t$, $d = \sinh t$ |
| $\exp(\theta\xi) = \cos\theta\,e_0+\sin\theta\,\xi$ | The one-parameter subgroup generated by a root |
| $\exp(\theta\xi) = e_0+\theta\xi$ | The polynomial subgroup generated by a root of $0$ |
| $\tilde\Pi = \tfrac12e_0\pm\tfrac12\xi i$ | The idempotent of the root |
| $(-1)^F = ie_3$ | Fermion parity: a Hermitian root of $+1$ |
| $ict\,e_0+\mathbf{x}$, $ct'\,e_0+i\mathbf{x}'$ | Material and informational coordinates |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the original classification.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the relation to the idempotents and the zero divisors.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the representation theory and the constraint verification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- A. Acus and A. Dargys, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square roots of an arbitrary complexified quaternion and the Clifford-algebra algorithm treated in *Biquaternion Square Roots of a General Element*.
