# __Zero Divisors Across the Twelve Structures__

## Introduction

A zero divisor is a nonzero element that annihilates a nonzero partner. It is an operation that cannot be inverted, and the set of such operations is the wall of the reversible region. The twelve products of the biquaternion complex space give twelve zero-divisor sets. They are not twelve unrelated sets: the cone of the quaternion norm lies in all twelve, and the differences between the sets are the differences between the products off that common core.

This article reads the twelve sets, compares them, and gives the physical content of each. It owns no theorem. The mathematics is *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the physical interpretations are gathered from the structure drafts of this category. The companion articles of the block are *Annihilators Across the Twelve Structures* and *Roots Across the Twelve Structures*.

The result that organizes the comparison is a coincidence and a contrast. The four general products have **one** zero-divisor set, because the four products read the same norm; their root sets, by contrast, are four different sets. Degeneracy is universal across the bands, while factorisation is band-specific.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The twelve products and their multiplication tables | [The 12 Products of the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-12-products-of-the-biquaternion-complex-space.html) |
| The twelve structures, their values, units and inverse equations | [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The zero-divisor cone, the units and the twelve sets | [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The norm, its vanishing and the inverse formula | [Norm and Invertibility in the Biquaternion Algebra](../articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.html) |
| The two one-sided actions and the absence of a unit | [The Two One-Sided Actions and the Absence of a Unit](../articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.html) |
| The square-zero sets and the nilpotents | [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |

## The Zero-Divisor Set

### Left, Right and Two-Sided

Let $\star$ be one of the twelve products. A nonzero element $\tilde Q$ is a **left zero divisor** when there is a nonzero $\tilde Q_1$ with $\tilde Q\star\tilde Q_1=0$, a **right zero divisor** when there is a nonzero $\tilde Q_2$ with $\tilde Q_2\star\tilde Q=0$, and a two-sided zero divisor when it is both. The origin is excluded, and it is never a zero divisor. In a commutative or conjugate-commutative structure the two sides coincide, and in an alternating structure every element is a zero divisor of both sides.

A zero divisor need not be nilpotent. The element $e_t+i\vec e_x$ has vanishing norm, $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$, yet its square is $2e_t+2i\vec e_x$ and not zero. The zero-divisor set, the nilpotent set and the square-zero set are three different sets, and the companion *Roots Across the Twelve Structures* reads the third.

### The Three Sets Kept Apart

Three sets are easy to exchange and must not be. The **zero-divisor set** of a product is the set of elements with a nonzero annihilating partner. The **cone** is the common zero set of the quaternion norm, $\mathcal{C}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\}$, a complex cone of complex dimension three and real dimension six. The **nilpotent cone** is the pure part of the cone, of real dimension four.

The relations are strict. The cone lies in every one of the twelve zero-divisor sets. The nilpotent cone lies in the cone and in the vector subspace, and in no other remarkable subspace. A nonzero nilpotent is a zero divisor, but a zero divisor is not necessarily nilpotent, and the cone is strictly larger than the nilpotent cone. The state $\tfrac12(e_t+i\vec u)$, with $\vec u$ a real unit vector, is a zero divisor of the plain product and is not nilpotent.

## The Four General Products

The general plain algebra, the general plain sesqualgebra, the general quaternionic algebra and the general quaternionic sesqualgebra all have the same zero-divisor set, the punctured cone

$$
\mathcal{C}\setminus\{0\}=\{\tilde Q\neq0:\ \langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0\}.
$$

The reason is that each of the four products is the plain product with a conjugation in one or both slots, and a conjugation is a bijection that does not move the norm. The four sets coincide, and the theorem is stated as *the four general products coincide* in the mathematics companion. It is the first of the three coincidences of the twelve; the other two are the symmetric pair $\mathrm{SPA}$ and $\mathrm{SQS}$ and the six structures with the total set.

Physically the cone is the **complexified light cone**, the locus of lightlike propagation; its cut by the material sector is the physical light cone and the boundary between the reversible and the irreversible. Off the cone the multiplication is invertible: in the plain product the inverse is $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, and the other three products have the one-sided inverse solutions recorded in the companion. On the cone the map drops rank and destroys its argument. The four bands read the same wall with four different names: composition degenerates there, the probability square has rank one there, the interval vanishes there, and the gauge multiplication drops rank there. One set, four readings.

The cone splits into two families, and the split is physical. The **pure null family**, $Q_t=0$ and $(\vec Q,\vec Q)=0$, is the nilpotent family of lightlike displacements. The **non-pure family** is the multiples of the idempotents, that is, the states. A state is a zero divisor because a measurement cannot be undone, not because its square vanishes. The distinction is the difference between the lightlike displacement and the pure state: both lie on the cone, and only the first is square-zero.

## The Two Symmetric Structures

The symmetric plain algebra $\mathrm{SPA}$ and the symmetric quaternionic sesqualgebra $\mathrm{SQS}$ have a larger set,

$$
\bigl(\{Q_t=0\}\cup\mathcal{C}\bigr)\setminus\{0\}.
$$

A nonzero element is a zero divisor exactly when it is pure or lies on the cone. The enlargement is physical. A pure element, one with $Q_t=0$, kills the plane of operations orthogonal to it, and it does so whether or not it is lightlike. The cleanest witness is a unit: $\vec e_x$ has norm $1$ and is invertible in the algebra, yet for the Jordan product $\vec e_x\bullet\vec e_y=\tfrac12(\vec e_x\vec e_y+\vec e_y\vec e_x)=0$. The same holds for the symmetric quaternionic sesquilinear product, $\vec e_x\star\vec e_y=0$.

The consequence is that the classical equivalence *zero divisor if and only if not a unit* fails. The symmetric coupling also annihilates on the pure elements, and an invertible unit can fail to compose symmetrically. The complement of the enlarged set is not the invertible set: it is $\{Q_t\neq0,\ \langle\tilde Q\rangle_{\natural}\neq0\}\cup\{0\}$, and the pure elements off the cone are the gap, being zero divisors of the coupling and invertible at once.

## The Two Scalar-Valued Structures

The symmetric plain sesqualgebra $\mathrm{SPS}$ and the symmetric quaternionic algebra $\mathrm{SQA}$ have the largest zero-divisor set, the whole punctured space $\mathbb{B}\setminus\{0\}$. Their products are scalar-valued: $\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$. For a nonzero $\tilde Q$ the equation $\tilde Q\star\tilde Q_1=0$ is one linear equation in the components of the partner, and its solutions fill a complex hyperplane.

A scalar coupling of two operations returns a number, and a number has no inverse. Neither structure has a unit, so neither has an invertible element. Every nonzero element is a zero divisor, and the only element of the complement is the origin, which is not invertible either. The whole band is irreversible in the algebraic sense, and that is the correct interpretation of a measurement: a probability and a coupling are not operations to be undone.

## The Four Antisymmetric Structures

The four antisymmetric structures also have the whole punctured space as their zero-divisor set, but for a different reason. Their products are antisymmetrisations or conjugate-antisymmetrisations, and their values lie in the three-dimensional vector subspace. Multiplication by a nonzero element is therefore a map of rank at most three, so its kernel is nonzero: every nonzero element has an annihilating partner. In the two alternating structures the element itself is a witness, $\tilde Q\star\tilde Q=0$; in the two conjugate-alternating ones the partner is another element in general. No element of a bracket has an inverse, because a bracket is not a composition.

The algebra of the four is the algebra of generators. The antisymmetric plain algebra is the rotation bracket, the antisymmetric plain sesqualgebra is the phase, the antisymmetric quaternionic algebra is the obstruction, and the antisymmetric quaternionic sesqualgebra is the polarisation. In each case the product returns a direction and not an operation, and the zero-divisor set being total is the algebraic form of the statement that a generator is an infinitesimal transformation, not something to be undone.

## The Comparison Table

| the structure | the product | the zero-divisor set | the complement | the word |
| --- | --- | --- | --- | --- |
| $\mathrm{GPA}$ | $\tilde Q_1\tilde Q_2$ | $\mathcal{C}\setminus\{0\}$ | the units off the cone, and $0$ | composition |
| $\mathrm{GPS}$ | $\tilde Q_1\tilde Q_2^{*}$ | $\mathcal{C}\setminus\{0\}$ | the invertible elements off the cone, and $0$ | probability |
| $\mathrm{GQA}$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\mathcal{C}\setminus\{0\}$ | the invertible elements off the cone, and $0$ | causality |
| $\mathrm{GQS}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $\mathcal{C}\setminus\{0\}$ | the invertible elements off the cone, and $0$ | gauge |
| $\mathrm{SPA}$ | $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | $(\{Q_t=0\}\cup\mathcal{C})\setminus\{0\}$ | $\{Q_t\neq0,\ \langle\tilde Q\rangle_{\natural}\neq0\}\cup\{0\}$ | commutativity |
| $\mathrm{SPS}$ | $\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ | $\mathbb{B}\setminus\{0\}$ | $\{0\}$ | positivity |
| $\mathrm{SQA}$ | $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ | $\mathbb{B}\setminus\{0\}$ | $\{0\}$ | coupling |
| $\mathrm{SQS}$ | the symmetrisation of the fourth product | $(\{Q_t=0\}\cup\mathcal{C})\setminus\{0\}$ | $\{Q_t\neq0,\ \langle\tilde Q\rangle_{\natural}\neq0\}\cup\{0\}$ | metric |
| $\mathrm{APA}$ | $\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)$ | $\mathbb{B}\setminus\{0\}$ | $\{0\}$ | rotation |
| $\mathrm{APS}$ | the antisymmetrisation of the second product | $\mathbb{B}\setminus\{0\}$ | $\{0\}$ | phase |
| $\mathrm{AQA}$ | the antisymmetrisation of the third product | $\mathbb{B}\setminus\{0\}$ | $\{0\}$ | obstruction |
| $\mathrm{AQS}$ | the antisymmetrisation of the fourth product | $\mathbb{B}\setminus\{0\}$ | $\{0\}$ | polarisation |

Three groups appear in the table, and each group has one statement. The four general products degenerate on the cone alone. The two symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ also degenerate on the pure family. The six scalar-valued or antisymmetric structures degenerate everywhere. **No row is empty**: the cone lies in all twelve sets, so the algebra is never a division algebra and no band is free of degeneracy.

## The Wall of Invertibility

### The Unit Group

The elements off the cone are the invertible elements of the plain product, and they form the group $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ with $\pi_1\cong\mathbb{Z}$. The cone is the complement of that group, so the reversible operations are exactly the off-cone ones and the light cone is the wall of the reversible region. Of the twelve structures only the general plain algebra and its symmetric part $\mathrm{SPA}$ have a two-sided unit, and only the general plain algebra is associative, so only it has a genuine group of units with the classical equivalence between zero divisors, non-units and a vanishing norm.

The other structures keep the wall and lose the group. An element off the cone is invertible in the four general products, but the products are not associative, so the invertible elements form no group. $\mathrm{SPA}$ keeps its invertible elements and its unit, but its symmetrised product is not associative either, so they form no group. The other symmetric structures and the four brackets destroy invertibility or have no unit, and the scalar-valued structures have no unit at all. The wall is the same wall; what changes behind it is how much of a group survives.

### The Two Families of the Cone

The cone has two physical layers. The pure null family, $Q_t=0$ and $(\vec Q,\vec Q)=0$, is the nilpotent family of lightlike displacements. The non-pure family is the family of states, the multiples of the idempotents. A state is a zero divisor of the composition because it is a measurement outcome and cannot be undone; a lightlike displacement is a zero divisor because its square vanishes. The two are different physical objects on the same algebraic wall.

The cone is the **information barrier**. A reset memory lands on a pure state, which is a zero divisor, and the reset costs $k_BT\log2$: that is Landauer's price. The barrier is not an erasure by itself. A gauge kernel hides a description that a gauge choice can recover; a confinement kernel destroys a description that the observable algebra no longer contains, and that loss is an absent label rather than an erased memory, so it carries no Landauer price. The algebraic wall is one; the information readings on its two sides are not the same.

The cone is a **cone over its own directions**. On the material sector those directions form a sphere: two nonzero null elements define the same direction when they differ by a scale, and the projectivisation of the real null cone is a two-dimensional sphere, the **celestial sphere** along which a photon's momentum points. The proper orthochronous Lorentz group acts transitively on the future directions; the past directions are a second copy, and time reversal exchanges the two. The projectivisation identifies them, so the sphere, not the cone, is the Lorentz-homogeneous object. Complexified, the projectivisation is the **Segre quadric**, whose two rulings are the two chiral celestial spheres, and the real sphere is their diagonal, the fixed set of the conjugation.

The cone also carries the state-space metric. The biquaternion norm vanishes on the pure states, and the Fubini–Study metric is its second variation at a null direction. The cone is where the algebra's quadratic form stops measuring length at first order and measures it at second order, so the geometry of the state space is read off the cone rather than blocked by it. In the velocity space the lightlike elements are the ideal points of a hyperbolic geometry, and the unboundedness of rapidity is the geometric form of their non-invertibility.

## Limits

The cone is not yet the light cone. It is a complex cone of real dimension six, while the physical light cone is its cut by the material sector $\mathbb{M}_{-}$, where the element is $\tilde R=ict'\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$ and the norm is $-c^{2}{t'}^{2}+x^{2}+y^{2}+z^{2}$. The metric enters only when the sector is cut out.

The cone is pointwise. Every statement above is a statement about one fixed algebra at one point; in a curved background the single cone becomes a field of local cones, and the metric, now a field, selects the directions and the surfaces. A black-hole horizon is a null surface and shares the algebra's notion of nullity, but it is not a piece of the cone: the cone is a fibrewise set of null directions, the horizon a hypersurface selected by one solution and its metric. The cone supplies the criterion, the metric supplies the surface.

The cone is a kinematic boundary, not the boundary of a dynamics. It has three images: the massless shell in momentum space, the WKB turning surface in configuration space, and the boundary and origin of the state space, because the module is generated by a null element. It is not the mass gap: the Klein step is set by the gap, and the cone enters only in the massless limit where the gap closes. Nor is it a topological obstruction: a configuration with no global potential is invertible wherever it is smooth, and the failure is in the patching, not in the norm.

## Summary

The four general products share one zero-divisor set, the punctured cone $\mathcal{C}\setminus\{0\}$, because all four read the same quaternion norm. The two symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ enlarge the set to the pure elements together with the cone. The two scalar-valued structures $\mathrm{SPS}$ and $\mathrm{SQA}$ and the four antisymmetric structures have the whole punctured space. The cone lies in all twelve sets, and no row of the table is empty. The cone is the wall of invertibility; its complement is the unit group of the plain product and only a set of invertible elements for the other general products. The cone splits into the nilpotent lightlike displacements and the state family, and the two are different reasons for being a zero divisor. The physical light cone is the cut of the complex cone by the material sector, and the cone becomes a field of cones on a curved background.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathcal{C}$ | the zero-divisor cone $\{\langle\tilde Q\rangle_{\natural}=0\}$ |
| $\langle\tilde Q\rangle_{\natural}$ | the quaternion algebraic norm $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $\mathbb{B}^{\times}$ | the unit group of the plain product, $\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| $Q_t$, $\vec Q$ | the scalar part and the vector part of $\tilde Q$ |
| $\mathbb{M}_{-}$ | the anti-Hermitian material sector, the cut that gives the physical light cone |

## Further Reading

- *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve sets and the proofs.
- *Norm and Invertibility in the Biquaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.md`), for the unit group and the inverse formula.
- *Annihilators Across the Twelve Structures* (`articles_physics/annihilators-across-the-twelve-structures.md`) and *Roots Across the Twelve Structures* (`articles_physics/roots-across-the-twelve-structures.md`), the two companions of this block.
- *The Eight Derived Structures: Symmetric and Antisymmetric* (`articles_physics/the-eight-derived-structures-symmetric-and-antisymmetric.md`), for the products compared here.
