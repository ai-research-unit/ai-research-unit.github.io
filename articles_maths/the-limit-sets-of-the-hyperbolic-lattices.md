# __The Limit Sets of the Hyperbolic Lattices__

## Introduction

The units of the split-quaternion algebra act on the three-dimensional vector subspace $V$ by the adjoint action, preserving the indefinite form $N$ of signature $(2,1)$ of *Split-Quaternion Rotations and the Lorentz Group*; the norm-one timelike locus is a sheet of a **hyperboloid** in $V$, and that sheet is the **hyperbolic plane**, with the metric $-B$ of constant curvature $-1$ and the isometry group $\operatorname{PSL}_2(\mathbb{R})\cong\operatorname{SO}^{+}(2,1)$, by *Split-Quaternions and Hyperbolic Geometry*. A discrete subgroup $\Gamma$ of the isometry group then acts on the sheet and on its boundary, the **isotropic lines** of the form, which form the **circle at infinity**. The **limit set** $\Lambda(\Gamma)$ is the set of the accumulation points of the $\Gamma$-orbit of a point, and it is a fractal on that circle: the whole circle for a lattice, a Cantor set of dimension strictly between $0$ and $1$ for a convex-cocompact group of the second kind. Its Hausdorff dimension is the **critical exponent** of the group, the Patterson–Sullivan exponent, and its measure is the Patterson–Sullivan measure; these are the objects of the article.

The article is careful about one thing from the outset. The hyperboloid lives in the three-dimensional space $V$, but the hyperbolic space it models is **two-dimensional**, and its boundary is the **circle** at infinity and not a two-sphere. The limit sets on the two-sphere, and the Kleinian groups that produce them, require the faithful linear action lost by the split-quaternion adjoint map, and they belong to the definite quaternion and to the biquaternion algebras, where the boundary of the hyperbolic three-space is a sphere; the comparison is drawn at the end and the difference is stated. The Apollonian gasket, which is the standard example on the sphere, is the Kleinian sibling of the Fuchsian objects of this article, and is cited rather than reproduced.

The model, the hyperboloid, the sheet and the boundary are from *Split-Quaternions and Hyperbolic Geometry*; the units, the adjoint action and the Lorentz group are from *Split-Quaternion Rotations and the Lorentz Group*; the group theory of the discrete groups, the limit set and the critical exponent are from *Kleinian and Fuchsian Groups*; the hyperbolic geometry of Part IV is *Hyperbolic Geometry*; the dimension of the limit set of a hyperbolic group is *The Dimension of the Boundary of a Hyperbolic Group*; the Apollonian gasket and the inversions are from *Möbius and Lie Sphere Geometry*; and the dimension itself is *Fractal Geometry*'s. No physics is invoked.

Throughout, $V=\operatorname{span}\{e_1,e_2,e_3\}$, $N$ is the form of signature $(2,1)$ on $V$, $B$ its polar form, $\mathbb{H}^{+}$ the timelike sheet $\{v\in V: N(v)=1\}$ of *Split-Quaternions and Hyperbolic Geometry*, and $\partial\mathbb{H}^{+}$ is the boundary, the set of isotropic directions. The group is $\Gamma\subset\operatorname{PSL}_2(\mathbb{R})\cong\operatorname{SO}^{+}(2,1)$.

## The Hyperboloid and the Boundary

**Theorem (the model and the boundary).** The norm-one timelike sheet $\mathbb{H}^{+}=\{v\in V:N(v)=1\}$ with the metric $-B$ is a complete simply connected Riemannian surface of constant curvature $-1$, that is the hyperbolic plane; the isometry group is $\operatorname{PSL}_2(\mathbb{R})$, acting by the adjoint action; and the boundary is the set of the isotropic lines of $N$, which is the circle at infinity.

*Proof.* This is the content of *Split-Quaternions and Hyperbolic Geometry*: the sheet is the homogeneous space $\operatorname{PSL}_2(\mathbb{R})/SO(2)$, the metric $-B$ restricted to the tangent planes is positive definite and of constant curvature $-1$, the geodesics are the central sections of the sheet by the planes through the origin of $V$, and the ideal points are the isotropic lines, that is the points of the null cone modulo the positive scalars, which form a circle. The statements are quoted and not reproved. $\square$

**Remark (the word "hyperbolic three-space").** The menu says that the model is the hyperbolic three-space, where the unit sphere is a hyperboloid. The correct reading, and the one used here, is that the hyperboloid is a **surface in the three-dimensional space $V$** and the hyperbolic space it carries is two-dimensional. Its boundary is therefore a **circle**, and the "sphere at infinity" of the menu is the circle at infinity. The genuinely three-dimensional hyperbolic space, with the two-sphere at infinity and the Kleinian groups acting on it, is not realised by the split-quaternion adjoint action: the adjoint map $\operatorname{PSL}_2(\mathbb{R})\to\operatorname{SO}^{+}(2,1)$ is the isometry group of a surface, and a group of isometries of a three-dimensional hyperbolic space needs the four-dimensional quaternion unit group or the biquaternion group of the sibling categories. The article states the difference and does not confuse the two.

## The Discrete Groups and Their Limit Sets

**Definition.** Let $\Gamma\subset\operatorname{PSL}_2(\mathbb{R})$ be discrete and let $\xi\in\mathbb{H}^{+}$. The **limit set** is

$$
\Lambda(\Gamma)=\overline{\Gamma\xi}\cap\partial\mathbb{H}^{+} ,
$$

the set of the accumulation points on the circle at infinity of the orbit; the complement $\Omega(\Gamma)=\partial\mathbb{H}^{+}\setminus\Lambda(\Gamma)$ is the **discontinuity domain**, on which $\Gamma$ acts properly discontinuously.

**Proposition (the limit set is independent of the point).** For a nonelementary discrete group the set $\Lambda(\Gamma)$ does not depend on the choice of $\xi$, it is the smallest nonempty closed $\Gamma$-invariant subset of the circle, and the quotient $(\mathbb{H}^{+}\cup\Omega)/\Gamma$ is a hyperbolic surface.

*Proof.* If $\xi,\eta\in\mathbb{H}^{+}$ then the hyperbolic distance is $\Gamma$-invariant and the orbit of $\eta$ stays within a bounded distance of the orbit of $\xi$ along the geodesic joining them, so the two sets of accumulation points agree; invariance and minimality are standard, and the quotient statement is the definition of the discontinuity domain. The propositions are *Kleinian and Fuchsian Groups*'s and are quoted. $\square$

**Remark (the elementary case).** If $\Gamma$ is elementary — cyclic, or generated by a hyperbolic element and an elliptic one — the limit set has at most two points and is not a fractal; the definition still applies, and the article restricts the fractal statements to the nonelementary case.

## The Limit Set as a Fractal

**Theorem (two regimes).** Let $\Gamma$ be a nonelementary discrete subgroup of $\operatorname{PSL}_2(\mathbb{R})$ acting on the hyperbolic plane.

1. If $\Gamma$ is of the **first kind**, that is if $\Lambda(\Gamma)=\partial\mathbb{H}^{+}$, the limit set is the whole circle and its dimension is $1$.
2. If $\Gamma$ is of the **second kind**, the limit set is a perfect, totally disconnected, uncountable compact subset of the circle — a **Cantor set** — and its dimension lies strictly between $0$ and $1$; the discontinuity domain is nonempty, and the quotient is a hyperbolic surface with boundary.

*Proof.* The dichotomy is the standard one of the Fuchsian groups: a nonelementary discrete group of the first kind acts ergodically on the circle and its limit set is the whole circle; a group of the second kind has a nonempty discontinuity domain, and its limit set, being closed, invariant, perfect and not the whole circle, is a Cantor set. The dimension statements are the Patterson–Sullivan theory of the next section; the group theory is *Kleinian and Fuchsian Groups*'s. $\square$

**Remark (the lattices).** A **lattice** is a discrete subgroup of finite covolume, and a lattice of $\operatorname{PSL}_2(\mathbb{R})$ is of the first kind: its limit set is the whole circle. The limit set of a lattice is therefore **not a fractal**, and the fractal limit sets of the article are those of the convex-cocompact groups of the second kind, the Schottky groups and their relatives. This is the honest limit of the comparison with the Apollonian gasket, which is a fractal and a Kleinian and not a Fuchsian object.

## The Dimension and the Measure

**Definition.** The **Poincaré series** of $\Gamma$ is $\sum_{\gamma\in\Gamma}e^{-s\,d(\xi,\gamma\xi)}$, and its abscissa of convergence $\delta(\Gamma)$ is the **critical exponent**. The **Patterson–Sullivan measure** is the $\Gamma$-invariant conformal measure on $\Lambda(\Gamma)$ of dimension $\delta$ whose existence and uniqueness come from the divergence of the Poincaré series at $s=\delta$.

**Theorem (the dimension is the critical exponent, quoted).** For a nonelementary discrete group $\Gamma$ the Hausdorff dimension of the limit set is the critical exponent,

$$
\dim_H\Lambda(\Gamma)=\delta(\Gamma) ,
$$

the Patterson–Sullivan exponent; for a convex-cocompact group $\delta\in(0,1)$ and the limit set has Lebesgue measure zero on the circle, while for a lattice of finite covolume $\delta=1$ and the limit set is the whole circle with the Patterson–Sullivan measure proportional to the circle measure. The dimension of the limit set of a hyperbolic group in the general theory is the subject of *The Dimension of the Boundary of a Hyperbolic Group*, and the dimension itself is *Fractal Geometry*'s.

*Proof (quoted).* The equality of the Hausdorff dimension and the critical exponent is the Patterson–Sullivan theorem, and the dichotomy of the measure is the standard consequence of the divergence of the Poincaré series at the exponent; both belong to *Kleinian and Fuchsian Groups* and are cited rather than reproved. $\square$

**Remark (the measure).** For a group of the second kind the limit set is a Cantor set of vanishing Lebesgue measure, and the Patterson–Sullivan measure is supported on it, is finite, and is the natural self-similar-like measure of dimension $\delta$; for a lattice the limit set is the circle and the measure is the circle measure. **The dimension and the measure are the two invariants of the limit set**, and the pair of the dimension and the measure is the content of the article.

## The Apollonian Gasket and the Comparison

**Remark (the Apollonian gasket is one dimension higher).** The **Apollonian gasket** is the residual set of the iterative removal of the interstices between three mutually tangent circles of the plane; it is the limit set of the **Kleinian group** generated by the inversions in the circles, acting on the boundary sphere of the hyperbolic three-space, and its dimension is the critical exponent of that group. The Apollonian gasket is thus the Kleinian sibling of the limit sets of this article, and not their instance: the split-quaternion model gives the hyperbolic **plane** and the **circle** at infinity, its limit sets are the Fuchsian ones, and the gasket lives on the **sphere** at infinity of the hyperbolic three-space. The construction, the inversions and the group are *Möbius and Lie Sphere Geometry*'s and *Hyperbolic Geometry*'s, and the comparison of the two kinds of limit sets is the comparison of the Fuchsian groups of this article with the Kleinian groups of *Kleinian and Fuchsian Groups*. **The two are compared and not identified**, and the article records the difference.

**Remark (the role of the Lorentz group).** The isometry group $\operatorname{SO}^{+}(2,1)$ of the Lorentz form $N$ is the group that acts on the sheet and on the circle at infinity, and the limit set is invariant under it in the sense that it is a limit set of the subgroup: the conjugation of $\Gamma$ by an element of $\operatorname{SO}^{+}(2,1)$ carries the limit set to the limit set of the conjugate group, and the critical exponent is unchanged because the hyperbolic distance is invariant. The Lorentz group of *Split-Quaternion Rotations and the Lorentz Group* is therefore the ambient group of the construction, and the discrete subgroups are its lattices and their convex-cocompact relatives. The hyperbolic three-space of the neighbouring quaternion and biquaternion categories has the larger group, and the split-quaternion one has this group.

## Worked Example

**Example (two groups).**

**(a) A lattice.** The modular group $\operatorname{PSL}_2(\mathbb{Z})$ is a lattice of $\operatorname{PSL}_2(\mathbb{R})$; it is of the first kind, its limit set is the whole circle at infinity, $\delta=1$, and the Patterson–Sullivan measure is the circle measure. The split-quaternion sheet with this group is the modular hyperbolic surface, and the limit set is not a fractal: the example fixes the boundary of the fractal regime.

**(b) A Schottky group.** Choose four disjoint closed discs in the circle's interior and the two Möbius transformations pairing the boundary circles of the first disc with the second and of the third with the fourth; the group they generate is free, discrete, convex-cocompact of the second kind, and its limit set is a Cantor set on the circle, with $\delta(\Gamma)\in(0,1)$ and vanishing Lebesgue measure. The limit set is the fractal of the article, the Cantor set is constructed by the same pairing as the Schottky groups of *Kleinian and Fuchsian Groups*, and the dimension is the Patterson–Sullivan exponent; the specific numerical value of $\delta$ is **not** asserted here, since it is not recomputed in this pass.

## Summary

The split-quaternion units act on the hyperboloid of the three-dimensional vector subspace $V$ and realise the hyperbolic **plane** with the circle at infinity, the isometry group being $\operatorname{PSL}_2(\mathbb{R})\cong\operatorname{SO}^{+}(2,1)$. The limit set of a discrete group is the set of the accumulation points on the circle, independent of the base point and the smallest nonempty closed invariant subset. For a lattice of finite covolume the limit set is the whole circle, of dimension $1$, with the circle measure; for a convex-cocompact group of the second kind it is a Cantor set of dimension the critical exponent $\delta\in(0,1)$ and of vanishing Lebesgue measure, carrying the Patterson–Sullivan measure. The dimension is the Patterson–Sullivan exponent, quoted from *Kleinian and Fuchsian Groups* and comparable to the general theory of *The Dimension of the Boundary of a Hyperbolic Group*; the dimension itself is *Fractal Geometry*'s. The Apollonian gasket is the Kleinian sibling one dimension higher, on the sphere at infinity of the hyperbolic three-space, and is compared with these Fuchsian limit sets and not identified with them; the hyperbolic three-space with its sphere belongs to the quaternion and biquaternion categories. The model is *Split-Quaternions and Hyperbolic Geometry*'s and the group is *Split-Quaternion Rotations and the Lorentz Group*'s.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\operatorname{span}\{e_1,e_2,e_3\}$ | The three-dimensional vector subspace |
| $N$, $B$ | The form of signature $(2,1)$ and its polar form |
| $\mathbb{H}^{+}=\{v\in V:N(v)=1\}$ | The timelike sheet, the hyperbolic plane |
| $\partial\mathbb{H}^{+}$ | The circle at infinity, the isotropic directions |
| $\Gamma\subset\operatorname{PSL}_2(\mathbb{R})$ | The discrete group, a Fuchsian group |
| $\Lambda(\Gamma)$, $\Omega(\Gamma)$ | The limit set; the discontinuity domain |
| $\delta(\Gamma)$ | The critical exponent; $\dim_H\Lambda=\delta$ |
| Patterson–Sullivan measure | The conformal measure on $\Lambda$ of dimension $\delta$ |

## Further Reading

- S. J. Patterson, "The limit set of a Fuchsian group", *Acta Mathematica* 136 (1976), 241–273. The critical exponent and the conformal measure.
- Dennis Sullivan, "The density at infinity of a discrete group of hyperbolic motions", *Publications Mathématiques de l'IHÉS* 50 (1979), 171–202. The Patterson–Sullivan theory and the dimension, cited to *Kleinian and Fuchsian Groups*.
- David Mumford, Caroline Series and David Wright, *Indra's Pearls: The Vision of Felix Klein* (Cambridge, 2002). The limit sets of the Schottky groups and the Kleinian constructions.
- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983). The Fuchsian groups, the limit set and the dichotomy of the kinds.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd ed. (Wiley, 2014). The Hausdorff dimension and its computation, cited to *Fractal Geometry*.
