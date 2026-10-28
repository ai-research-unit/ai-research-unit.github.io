# __Topology in the Space of Biquaternions__

## Introduction

This article builds the topology of the space of biquaternions, and its only input is the linear structure of that space. The space is a real vector space of dimension eight; a **norm** is defined on it; because the dimension is finite, all its norms are equivalent, so the space carries exactly **one topological norm** and **one topology**; that topology is then built explicitly and it is the **Euclidean topology of $\mathbb{R}^{8}$**; and in it the product of biquaternions is continuous, so that the space is a topological algebra as well as a topological vector space. The article uses the linear structure and the product, and nothing else.

## Notation

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_t=1,\vec e_x,\vec e_y,\vec e_z$ satisfying $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$. The central imaginary is written $i$, so that it does not collide with the quaternion units. A general element and its real coordinates are

$$
\tilde{Q}=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu=q_\mu+iq'_\mu,\qquad q_\mu,q'_\mu\in\mathbb{R},
$$

so that, as a real vector space,

$$
\mathbb{B}=\mathbb{R}\text{-span}\{e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z\},\qquad \dim_{\mathbb{R}}\mathbb{B}=8,
$$

with $\mathrm{Sc}(\tilde{Q})=Q_t$ the scalar part and the product of the algebra as in *The Realification and the Effect of the Change of Scalars*.

## 1. The Norm

**Definition (norm).** Let $V$ be a real vector space. A **norm** on $V$ is a function $\lVert\cdot\rVert:V\to[Normed and Banach Spaces](normed-and-banach-spaces.html), the norm, the equivalence of norms and the uniqueness of the topology in finite dimension; [Comparison of Norms and Invertibility](comparison-of-norms-and-invertibility.html).
- [Metric, Uniform and Complete Spaces](metric-uniform-and-complete-spaces.html), the metric, the completeness and the compactness properties of §3; [Banach and Hilbert Spaces](banach-and-hilbert-spaces.html).
- [Topological Algebras and Banach Algebras](topological-algebras-and-banach-algebras.html), the continuity of the product and the openness of the group of units.
- [The Matrix Element Representation and the Biquaternion Dynamics](the-matrix-element-representation-and-the-biquaternion-dynamics.html), the realization $\mathsf{M}_2$ and $\lVert\mathsf{M}_2(\tilde{Q})\rVert_F=\sqrt2\lVert\tilde{Q}\rVert$.
