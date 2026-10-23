# __Introduction to Topology on the Quaternions__

## Introduction

This article opens the topological half of the chapter. The quaternion algebra is a real vector space of dimension four, so it carries the Euclidean topology of that space; its multiplicative structure cuts out three objects, the whole space, the unit sphere, and the complement of the origin, and the article names them and maps the articles that study them. It states the topology and does not develop it: the algebra of the block is the article before it, and the metric statements are the concern of the articles below.

## The Space and Its Norm

**Proposition (the space).** The identification $\tilde q\mapsto(q_t,q_x,q_y,q_z)$ is a vector-space isomorphism $\mathbb{H}\cong\mathbb{R}^4$, and $\mathbb{H}$ carries the Euclidean topology of $\mathbb{R}^4$: the product and the addition and the scalar multiplication are continuous, and the topology is induced by the norm $\lvert\tilde q\rvert=\sqrt{q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}}$.

*Proof.* The coordinates are linear, so the two vector spaces are the same space with a chosen basis; the norm is the square root of the positive definite quadratic form $\langle\cdot\rangle_{\natural}$, and the product is given by polynomial formulas in the coordinates, hence continuous.

**Proposition (the norm is multiplicative and the inverse is continuous).** $\lvert\tilde q_2\tilde q_1\rvert=\lvert\tilde q_2\rvert\lvert\tilde q_1\rvert$, and the inversion map $\tilde q\mapsto\tilde q^{-1}=\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$ is continuous on the complement of the origin.

*Proof.* Multiplicativity of $\langle\cdot\rangle_{\natural}$ is the multiplicativity of the quaternion product, $\langle\tilde q_2\tilde q_1\rangle_{\natural}=\langle\tilde q_2\rangle_{\natural}\langle\tilde q_1\rangle_{\natural}$; the inverse formula is *Norm and Invertibility in the Quaternion Algebra*, and its coordinates are rational with denominator $\langle\tilde q\rangle_{\natural}\neq0$.

## The Three Objects

**Definition (the three objects).** On the quaternion space this topology distinguishes

$$
\mathbb{H}\quad(\text{the whole space}),\qquad
S^3=\{\tilde q:\langle\tilde q\rangle_{\natural}=1\}\quad(\text{the unit sphere}),\qquad
\mathbb{H}^\times=\{\tilde q\neq0\}\quad(\text{the punctured space}).
$$

**Theorem (the algebra is contractible).** The space $\mathbb{H}$ is contractible; it is connected, simply connected, and locally compact, and no homotopy group of it detects the multiplication.

*Proof.* $\mathbb{H}$ is a real vector space; the straight-line homotopy $\tilde q\mapsto t\tilde q$ retracts it to the origin, so it is contractible, and a contractible space is connected and has trivial homotopy groups. The vector space is locally compact.

**Theorem (the unit sphere).** The unit sphere $S^3$ is a compact connected subspace of $\mathbb{H}$, homeomorphic to the Euclidean three-sphere, and it is the group of unit quaternions $Sp(1)$ under the quaternion product; the group operations are continuous, so $S^3$ is a compact topological group.

*Proof.* $S^3=\{N=1\}$ is the zero set of a continuous function on the closed unit ball, hence compact, and it is the sphere of the norm; the quaternion product of two unit quaternions is a unit quaternion by multiplicativity of $\langle\cdot\rangle_{\natural}$, and the operations are restrictions of the continuous product and inverse.

**Remark (the punctured space is a product).** The map

$$ \boxed{\; \mathbb{H}^\times\longrightarrow\mathbb{R}_{>0}\times S^3,\qquad
\tilde q\longmapsto\bigl(\lvert\tilde q\rvert,\ \tilde q/\lvert\tilde q\rvert\bigr) \;} ,$$

is a homeomorphism, and an isomorphism of topological groups when the first factor is given its multiplicative structure; the display is the decomposition of the group of units, and its proof, together with the topology of the group, is *The Quaternion Unit Group as a Topological Group*, below this article in this category. The homeomorphism is named here because it is the bridge between the punctured space and the sphere, and it is not reproved here.

## The Map of the Topological Articles

| object | article |
|---|---|
| the topology of the algebra, connectedness, compactness, the structure of the space | *Quaternion Topology* |
| the group of units, its decomposition, its exponential | *The Quaternion Unit Group as a Topological Group* |
| the orders and the finite subgroups of the unit sphere | *Quaternion Orders and Finite Groups of Units* |
| the metric of the quaternion space and its subspaces | *Quaternion Metrics* |

## Summary

The quaternion algebra is $\mathbb{R}^4$ with its Euclidean topology, the norm $\lvert\tilde q\rvert=\sqrt{\langle\tilde q\rangle_{\natural}}$ multiplicative and the inverse continuous off the origin. Three objects carry the topology: the whole space $\mathbb{H}$, which is contractible and simply connected; the unit sphere $S^3=\{N=1\}$, which is the compact connected topological group $Sp(1)$ of the unit quaternions; and the punctured space $\mathbb{H}^\times$, which is homeomorphic and group-isomorphic to $\mathbb{R}_{>0}\times S^3$. The topological articles of the chapter read the space, the unit group, the finite subgroups of the sphere through the orders, and the metrics of the quaternion space.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lvert\tilde q\rvert=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the norm, multiplicative on the algebra |
| $\mathbb{H}^\times=\mathbb{H}\setminus\{0\}$ | the punctured space, the group of units |
| $S^3=\{N=1\}=Sp(1)$ | the unit sphere, the compact group of unit quaternions |
| $\mathbb{H}^\times\cong\mathbb{R}_{>0}\times S^3$ | the product decomposition of the units |
| $\mathcal N=\{N=0\}$ | the null cone; a point $\{0\}$ over $\mathbb{R}$, a cone of real dimension $6$ over $\mathbb{C}$ |

## Further Reading

- [Quaternion Topology](quaternion-topology.html), for the space and its structure
- [The Quaternion Unit Group as a Topological Group](the-quaternion-unit-group-as-a-topological-group.html) and [Quaternion Orders and Finite Groups of Units](quaternion-orders-and-finite-groups-of-units.html), for the units
