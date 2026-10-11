# __The Quaternion Unit Group as a Topological Group__

## Introduction

The quaternions form a division algebra, so the units of the plain product are exactly the nonzero elements and the punctured space is the group of units. This article reads that group as a topological group: its decomposition into a positive real factor and the unit sphere, the compact subgroup of the unit quaternions, the connectedness, the exponential map, and the comparison with the biquaternion group of units. The space is the article before it; the discrete subgroups of the sphere are the article after it.

**Boundaries.** The space and its topology are *Introduction to Topology on the Quaternions*, above this article in this category; the norm and the inverse formula are *Norm and Invertibility in the General Plain Algebra*, above this article in this category; the finite subgroups of the unit sphere are *Quaternion Orders and Finite Groups of Units*, below this article in this category; the exponential and the Lie structure are *Quaternion Exponential and Lie Group Structure*, below this article in this category; the rotations are *Quaternion Rotations and Reflections*, in `### Geometry`. The biquaternion parallel is *The Biquaternion Unit Group as a Topological Group*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$; an element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_kq_ke_k$. The **quaternion form** is $N(\tilde q)=q_0^{2}+|\mathbf q|^{2}$ and the **norm** is $\lvert\tilde q\rvert=\sqrt{N(\tilde q)}$; the **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\mathbf q$, the bar is the identity. The **unit sphere** is $S^3=\{\tilde q:N(\tilde q)=1\}$, the **group of units** is $\mathbb{H}^\times=\{\tilde q\neq0\}$.

## The Group of Units

**Proposition (the units are the nonzero elements).** The group of units of the plain product is

$$
\mathbb{H}^\times=\mathrm{GL}_1(\mathbb{H})=\{\tilde q:\tilde q\neq0\},
$$

of real dimension $4$, open and dense in the algebra; its centre is $\mathbb{R}^\times e_0\cong\mathbb{R}^\times$, of real dimension one.

*Proof.* The algebra is a division algebra, so every nonzero element is invertible, with inverse $\tilde q^{\natural}/N(\tilde q)$ (*Norm and Invertibility in the General Plain Algebra*); the origin is a closed proper algebraic subset, so its complement is open and dense; an element commutes with all of $\mathbb{H}$ exactly when it is a real scalar multiple of $e_0$, and the central units are the nonzero ones.

**Proposition (the subspace is a topological group).** With the topology of $\mathbb{H}$ the multiplication $\mathbb{H}^\times\times\mathbb{H}^\times\to\mathbb{H}^\times$ and the inversion $\mathbb{H}^\times\to\mathbb{H}^\times$ are continuous, so $\mathbb{H}^\times$ is a topological group.

*Proof.* The product is polynomial in the coordinates, and the inverse has coordinates rational with denominator $N(\tilde q)\neq0$; both are continuous on the punctured space.

## The Decomposition with the Sphere

**Theorem (the units are a product).** The map

$$
\mathbb{H}^\times\longrightarrow\mathbb{R}_{>0}\times S^3,\qquad
\tilde q\longmapsto\bigl(\lvert\tilde q\rvert,\ \tilde q/\lvert\tilde q\rvert\bigr),
$$

is an isomorphism of topological groups, the second factor being the group of unit quaternions and the first the multiplicative group of the positive reals.

*Proof.* The map is well defined and continuous; the inverse is $(t,\tilde u)\mapsto t\tilde u$, continuous, and satisfies $\lvert t\tilde u\rvert=t$ because $\lvert\tilde u\rvert=1$; multiplicativity of the norm gives $\lvert\tilde p\tilde q\rvert=\lvert\tilde p\rvert\lvert\tilde q\rvert$, so the map is a group homomorphism, and its kernel and image are as displayed.

**Corollary (the units are connected and their topology is the sphere's).** The group $\mathbb{H}^\times$ is connected, path-connected and not compact; it is homotopy equivalent to $S^3$, so it is simply connected, $\pi_1(\mathbb{H}^\times)=0$ and $\pi_3(\mathbb{H}^\times)\cong\mathbb{Z}$.

*Proof.* The product $\mathbb{R}_{>0}\times S^3$ is connected and path-connected because both factors are; the factor $\mathbb{R}_{>0}$ admits the retraction $t\mapsto1$ and is contractible, so the product deformation retracts onto $S^3$; the fundamental group of $S^3$ is trivial and its third homotopy group is infinite cyclic, and these are homotopy invariants. The group is not compact because $\mathbb{R}_{>0}$ is unbounded.

## The Compact Subgroup of the Unit Quaternions

**Proposition (the maximal compact subgroup).** The unit quaternions

$$
Sp(1)=S^3=\{\tilde u:\tilde u^{\natural}\tilde u=e_0\}
$$

are a compact Lie group of real dimension $3$, the maximal compact subgroup of $\mathbb{H}^\times$; the decomposition $\mathbb{H}^\times=\mathbb{R}_{>0}\cdot Sp(1)$ holds, and the centre of $Sp(1)$ is $\{\pm e_0\}$.

*Proof.* The set $S^3$ is closed and bounded in $\mathbb{H}$, hence compact; it is closed under the product and the inverse, so it is a subgroup; it is a differentiable submanifold of dimension three cut by $N=1$ with nonzero gradient, so it is a Lie group. Every unit $\tilde q$ is $\lvert\tilde q\rvert\cdot\tilde u$ with $\tilde u$ a unit quaternion, which is the displayed decomposition and shows maximality, a compact subgroup lying in $S^3$ by the norm bound. An element of $S^3$ commuting with all of $\mathbb{H}$ is a real scalar unit, that is $\pm e_0$.

**Remark (the quotient by the centre).** The centre $\{\pm e_0\}$ is a discrete normal subgroup, and the quotient $Sp(1)/\{\pm e_0\}$ is the group of the rotations of three-dimensional space; it is the two-to-one cover read as a group quotient, and it is *Quaternion Rotations and Reflections*.

## The Exponential Map

**Theorem (the exponential and its homeomorphism property).** The series

$$
\exp(\tilde q)=\sum_{n\geq0}\frac{\tilde q^{n}}{n!}
$$

converges everywhere, takes values in $\mathbb{H}^\times$, is continuous, and is surjective onto $\mathbb{H}^\times$; on the pure quaternions it is $\exp(\mathbf v)=\cos\lvert\mathbf v\rvert+\dfrac{\mathbf v}{\lvert\mathbf v\rvert}\sin\lvert\mathbf v\rvert$, a unit quaternion. Restricted to the open band $\{\tilde q:\lvert\mathbf q\rvert<\pi\}$ the map $\exp$ is a homeomorphism onto $\mathbb{H}^\times$ with the negative scalar ray removed.

*Proof.* The series converges by comparison with the real exponential, gives $\lvert\exp(\tilde q)\rvert=e^{q_0}\neq0$, so the values are units; the pure formula is the splitting of the series into its even and odd parts. Writing $\tilde q=q_0e_0+\mathbf v$, $\exp(\tilde q)=e^{q_0}\exp(\mathbf v)$, and $\exp(\mathbf v)=\cos\lvert\mathbf v\rvert+\widehat{\mathbf v}\sin\lvert\mathbf v\rvert$ with $\widehat{\mathbf v}=\mathbf v/\lvert\mathbf v\rvert$; every unit quaternion is uniquely $(\cos\theta,\widehat{\mathbf v}\sin\theta)$ with $\theta\in[0,\pi)$ and a unit imaginary direction, except the value $\theta=\pi$, which is $-e_0$, so the unit part of the image misses exactly $-e_0$ and the positive factor misses nothing; the inverse assigns to a unit quaternion its angle $\theta\in[0,\pi)$ and direction. Continuity and openness of the inverse are the continuity of the arccosine and the direction, and the excluded set is the negative scalar ray $-\mathbb{R}_{>0}e_0$.

**Corollary (the exponential generates the unit group).** Every unit is $\exp(\tilde q)$ for some $\tilde q$, and every unit quaternion is $\exp(\mathbf v)$ for a pure $\mathbf v$ with $\lvert\mathbf v\rvert\in[0,\pi]$; the exponential is a local homeomorphism at the origin, with local inverse the quaternion logarithm of *Quaternion Exponential and Lie Group Structure*.

*Proof.* The surjectivity onto $\mathbb{H}^\times$ is the theorem; the unit statement is the restriction to the pure part, allowing the value $\lvert\mathbf v\rvert=\pi$ for $-e_0$; the local statement is the inverse function theorem applied on the band, where the differential at the origin is the identity.

## The Comparison with the Biquaternion Group of Units

| object | $\mathbb{H}^\times$ | $\mathbb{B}^\times$ |
|---|---|---|
| description | all nonzero elements (division algebra) | the non-zero-divisors, complement of the singular cone |
| real dimension | $4$ | $8$ |
| decomposition | $\mathbb{R}_{>0}\times S^3$ | $\bigl(\mathbb{C}^\times\times SL_2(\mathbb{C})\bigr)/\{\pm I\}\cong GL_2(\mathbb{C})$ |
| compact part | $Sp(1)=S^3$ | $U(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\}$ |
| connected | yes, simply connected | yes, $\pi_1\cong\mathbb{Z}$ |
| exponential | onto, a homeomorphism on the band $\lvert\mathbf q\rvert<\pi$ minus the negative ray | onto, a local homeomorphism, with the singular cone absent |

**Proposition (the definite case is one dimension shorter and simply connected).** Over $\mathbb{R}$ the group of units is the product of a line and a three-sphere, hence simply connected; over $\mathbb{C}$ the singular cone cuts the units down to the complement of a cone and the group retracts onto $U(\mathbb{B})$, whose centre contributes a circle and a fundamental group $\mathbb{Z}$.

*Proof.* The decomposition over $\mathbb{R}$ is the theorem; over $\mathbb{C}$ the units are the complement of the singular cone and the retraction onto the maximal compact subgroup is *The Biquaternion Unit Group as a Topological Group*, whose fundamental group is $\mathbb{Z}$.

## Summary

The group of units of the quaternion algebra is the punctured space $\mathbb{H}^\times=\mathbb{H}\setminus\{0\}$, open, dense, of real dimension four, with centre $\mathbb{R}^\times e_0$. It is a topological group, and the map $\tilde q\mapsto(\lvert\tilde q\rvert,\tilde q/\lvert\tilde q\rvert)$ is an isomorphism onto $\mathbb{R}_{>0}\times S^3$; consequently it is connected, simply connected, homotopy equivalent to $S^3$ and not compact. The unit quaternions $Sp(1)=S^3$ form the compact maximal subgroup, of dimension three, with centre $\{\pm e_0\}$ and quotient the rotation group. The exponential is surjective onto the units, is a unit quaternion on the pure part, and is a homeomorphism from the band of pure norm less than $\pi$ onto the units with the negative scalar ray removed. The biquaternion group of units is the complement of a cone of real dimension eight and retracts onto a circle times a three-sphere with fundamental group $\mathbb{Z}$; the quaternion case is one rung shorter and simply connected.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}^\times=\mathbb{H}\setminus\{0\}$ | the group of units |
| $\mathbb{H}^\times\cong\mathbb{R}_{>0}\times S^3$ | the product decomposition |
| $Sp(1)=S^3=\{N=1\}$ | the compact maximal subgroup |
| $\{\pm e_0\}$, $Sp(1)/\{\pm e_0\}$ | the centre and the rotation quotient |
| $\exp(\tilde q)=e^{q_0}\bigl(\cos\lvert\mathbf q\rvert+\widehat{\mathbf q}\sin\lvert\mathbf q\rvert\bigr)$ | the exponential, onto $\mathbb{H}^\times$ |
| $\lvert\mathbf q\rvert<\pi$ | the band on which $\exp$ is a homeomorphism onto its image |

## Further Reading

- *Introduction to Topology on the Quaternions* (`articles_maths/introduction-to-topology-on-the-quaternions.md`), for the space and the three objects
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), for the inverse formula
- *Quaternion Orders and Finite Groups of Units* (`articles_maths/quaternion-orders-and-finite-groups-of-units.md`), for the discrete subgroups of $S^3$
- *Quaternion Exponential and Lie Group Structure* (`articles_maths/quaternion-exponential-and-lie-group-structure.md`), for the logarithm and the Lie structure
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the biquaternion parallel
