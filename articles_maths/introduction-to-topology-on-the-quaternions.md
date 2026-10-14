# __Introduction to Topology on the Quaternions__

## Introduction

This article opens the topological half of the chapter. The quaternion algebra is a real vector space of dimension four, so it carries the Euclidean topology of that space; its multiplicative structure cuts out three objects, the whole space, the unit sphere, and the complement of the origin, and the article names them and maps the articles that study them. It states the topology and does not develop it: the algebra of the block is the article before it, and the metric statements are the concern of the articles below.

**Boundaries.** This is the entry of the topological half. The algebra is *Introduction to the Symmetric Quaternionic Algebra of Quaternions* and its block, above this article in this category; the topology of the algebra is *Quaternion Topology*, below this article in this category; the group of units is *The Quaternion Unit Group as a Topological Group* and the arithmetic of its finite subgroups is *Quaternion Orders and Finite Groups of Units*, both below this article in this category; the metrics are *Quaternion Metrics* and *Topology and Metric for Each of the Six Operations*, below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_kq_ke_k$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$, the **quadratic form** is $N(\tilde q)=q_0^{2}+|\vec q|^{2}$, and the **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\vec q$; the bar is the identity. Metric words are used in this half of the chapter only, and the *norm* here is the function $\lvert\tilde q\rvert=\sqrt{N(\tilde q)}$.

## The Space and Its Norm

**Proposition (the space).** The identification $\tilde q\mapsto(q_0,q_1,q_2,q_3)$ is a vector-space isomorphism $\mathbb{H}\cong\mathbb{R}^4$, and $\mathbb{H}$ carries the Euclidean topology of $\mathbb{R}^4$: the product and the addition and the scalar multiplication are continuous, and the topology is induced by the norm $\lvert\tilde q\rvert=\sqrt{q_0^{2}+q_1^{2}+q_2^{2}+q_3^{2}}$.

*Proof.* The coordinates are linear, so the two vector spaces are the same space with a chosen basis; the norm is the square root of the positive definite quadratic form $N$, and the product is given by polynomial formulas in the coordinates, hence continuous.

**Proposition (the norm is multiplicative and the inverse is continuous).** $\lvert\tilde p\tilde q\rvert=\lvert\tilde p\rvert\lvert\tilde q\rvert$, and the inversion map $\tilde q\mapsto\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$ is continuous on the complement of the origin.

*Proof.* Multiplicativity of $N$ is the multiplicativity of the plain product, $N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$; the inverse formula is *Norm and Invertibility in the General Plain Algebra*, and its coordinates are rational with denominator $N(\tilde q)\neq0$.

## The Three Objects

**Definition (the three objects).** On the quaternion space this topology distinguishes

$$
\mathbb{H}\quad(\text{the whole space}),\qquad
S^3=\{\tilde q:N(\tilde q)=1\}\quad(\text{the unit sphere}),\qquad
\mathbb{H}^\times=\{\tilde q\neq0\}\quad(\text{the punctured space}).
$$

**Theorem (the algebra is contractible).** The space $\mathbb{H}$ is contractible; it is connected, simply connected, and locally compact, and no homotopy group of it detects the multiplication.

*Proof.* $\mathbb{H}$ is a real vector space; the straight-line homotopy $\tilde q\mapsto t\tilde q$ retracts it to the origin, so it is contractible, and a contractible space is connected and has trivial homotopy groups. The vector space is locally compact.

**Theorem (the unit sphere).** The unit sphere $S^3$ is a compact connected subspace of $\mathbb{H}$, homeomorphic to the Euclidean three-sphere, and it is the group of unit quaternions $Sp(1)$ under the plain product; the group operations are continuous, so $S^3$ is a compact topological group.

*Proof.* $S^3=\{N=1\}$ is the zero set of a continuous function on the closed unit ball, hence compact, and it is the sphere of the norm; the plain product of two unit quaternions is a unit quaternion by multiplicativity of $N$, and the operations are restrictions of the continuous product and inverse.

**Remark (the punctured space is a product).** The map

$$
\mathbb{H}^\times\longrightarrow\mathbb{R}_{>0}\times S^3,\qquad
\tilde q\longmapsto\bigl(\lvert\tilde q\rvert,\ \tilde q/\lvert\tilde q\rvert\bigr),
$$

is a homeomorphism, and an isomorphism of topological groups when the first factor is given its multiplicative structure; the display is the decomposition of the group of units, and its proof, together with the topology of the group, is *The Quaternion Unit Group as a Topological Group*, below this article in this category. The homeomorphism is named here because it is the bridge between the punctured space and the sphere, and it is not reproved here.

## The Map of the Topological Articles

| object | article |
|---|---|
| the topology of the algebra, connectedness, compactness, the structure of the space | *Quaternion Topology* |
| the group of units, its decomposition, its exponential | *The Quaternion Unit Group as a Topological Group* |
| the orders and the finite subgroups of the unit sphere | *Quaternion Orders and Finite Groups of Units* |
| the metric of the quaternion space and its subspaces | *Quaternion Metrics* |
| the metric read for each of the six products | *Topology and Metric for Each of the Six Operations* |

## Summary

The quaternion algebra is $\mathbb{R}^4$ with its Euclidean topology, the norm $\lvert\tilde q\rvert=\sqrt{N(\tilde q)}$ multiplicative and the inverse continuous off the origin. Three objects carry the topology: the whole space $\mathbb{H}$, which is contractible and simply connected; the unit sphere $S^3=\{N=1\}$, which is the compact connected topological group $Sp(1)$ of the unit quaternions; and the punctured space $\mathbb{H}^\times$, which is homeomorphic and group-isomorphic to $\mathbb{R}_{>0}\times S^3$. The topological articles of the chapter read the space, the unit group, the finite subgroups of the sphere through the orders, and the metrics of the quaternion space and of the six products.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lvert\tilde q\rvert=\sqrt{N(\tilde q)}$ | the norm, multiplicative on the algebra |
| $\mathbb{H}^\times=\mathbb{H}\setminus\{0\}$ | the punctured space, the group of units |
| $S^3=\{N=1\}=Sp(1)$ | the unit sphere, the compact group of unit quaternions |
| $\mathbb{H}^\times\cong\mathbb{R}_{>0}\times S^3$ | the product decomposition of the units |
| $\mathcal N=\{N=0\}$ | the null cone; a point $\{0\}$ over $\mathbb{R}$, a cone of real dimension $6$ over $\mathbb{C}$ |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the algebra and its norm
- *Quaternion Topology* (`articles_maths/quaternion-topology.md`), for the space and its structure
- *The Quaternion Unit Group as a Topological Group* (`articles_maths/the-quaternion-unit-group-as-a-topological-group.md`) and *Quaternion Orders and Finite Groups of Units* (`articles_maths/quaternion-orders-and-finite-groups-of-units.md`), for the units
- *Topology and Metric for Each of the Six Operations* (`articles_maths/topology-and-metric-for-each-of-the-six-operations.md`), for the metric reading of the six products
