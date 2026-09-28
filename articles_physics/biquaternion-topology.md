# __Biquaternion Topology__

## Introduction

This article describes the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ as a topological space, together with the two subsets of it that the framework singles out: the Euclidean unit sphere and the null cone. It uses the algebra and the six distinguished subspaces of *Biquaternion Algebra*, the coordinates, the $ict$ assignment and the sector split of *Conventions in the Biquaternion Universe*, and the biquaternion norm $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ and the invertibility criterion of *Biquaternion Norm and Invertibility*. The form itself is not re-derived here.

**Scope.** The topology of the **group of units** $\mathbb{B}^\times$ — the polar decomposition, the retractions onto the compact subgroups, the homotopy groups, the universal cover and the connected components — belongs to the Lie theory of the algebra and is treated in *The Biquaternion Unit Group as a Topological Group*. The differentiability statement that the null cone is smooth away from the apex belongs to *Biquaternion Analysis*, where the derivative is available. This article owns the ambient space and its distinguished subsets.

**Conventions.** The units are $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, the central scalar imaginary is $i$, and $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\sum_\mu Q_\mu^2$, and the Euclidean norm is $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$, which is the square root of the scalar part of the Hermitian form $\tilde{Q}\tilde{Q}^\dagger$.

## The Underlying Space and its Contractibility

As a real vector space, $\mathbb{B}\cong\mathbb{C}^4\cong\mathbb{R}^8$. The linear isometry that exhibits it is the coefficient map

$$
\tilde{Q}=\sum_\mu Q_\mu e_\mu \;\longmapsto\; (\operatorname{Re}Q_0,\operatorname{Im}Q_0,\operatorname{Re}Q_1,\operatorname{Im}Q_1,\operatorname{Re}Q_2,\operatorname{Im}Q_2,\operatorname{Re}Q_3,\operatorname{Im}Q_3)\in\mathbb{R}^8 ,
$$

and the Euclidean norm $\|\cdot\|_E$ is the pull-back of the standard norm of $\mathbb{R}^8$ along it. Because $\mathbb{B}$ is a real vector space, it is contractible: the straight-line homotopy $\tilde{Q}\mapsto t\tilde{Q}$ contracts it to the origin, and consequently

$$
\pi_n(\mathbb{B})=0 \quad\text{for every } n\ge 1 .
$$

**Physical reading.** The ambient algebra carries no topology of its own. There is no non-contractible loop inside $\mathbb{B}$, and therefore no topological invariant that can be lodged in the algebra itself. Every topological charge the framework produces — the winding of a Skyrme field, the instanton number of a gauge configuration, the linking of a field configuration — must come from a *map* into $\mathbb{B}$ or into one of its groups, never from the carrier. This is also why the complex structure of the framework cannot be a topological property of the space it is written on: $\mathbb{B}$ is as flat as $\mathbb{R}^8$.

## The Euclidean Unit Sphere

The **Euclidean unit sphere** is the set

$$
S^7_E=\{\tilde{Q}\in\mathbb{B} : \|\tilde{Q}\|_E=1\} ,
$$

which the isometry above carries to the standard unit sphere of $\mathbb{R}^8$. It is a compact, connected, simply connected seven-dimensional manifold, with

$$
\pi_0(S^7_E)=0,\qquad \pi_1(S^7_E)=\dots=\pi_6(S^7_E)=0,\qquad \pi_7(S^7_E)=\mathbb{Z}.
$$

Two subsets of it are used later. The **unit quaternions** $S^3=\{\tilde{q}\in\mathbb{H} : N(\tilde{q})=1\}$ sit inside it as the real quaternion slice, and the **unit-norm slice** $\{\tilde{Q} : N(\tilde{Q})=1\}$ meets it in the elements that are simultaneously of unit biquaternion norm and unit Euclidean norm, a set that carries the rotor group and is treated in *Biquaternion Rotations and Lorentz Transformations*.

**Physical reading.** The Euclidean sphere is the sphere the Hermitian form defines, not the one the biquaternion norm defines, and the distinction matters physically: a normalised quantum state lies on the Hermitian sphere, an interval lies on the biquaternion norm. The two agree only on the subset where the element is unitary, which is the rotor group.

## The Null Cone

The **null cone** is the zero locus of the biquaternion norm,

$$
\mathcal{N}=\{\tilde{Q}\in\mathbb{B} : N(\tilde{Q})=0\} .
$$

It is a real algebraic variety of real dimension $6$, since it is the common zero set of the real and the imaginary parts of the single complex equation $\sum_\mu Q_\mu^2=0$, two independent real equations in eight real unknowns. It is a cone: $\tilde{Q}\in\mathcal{N}$ implies $z\tilde{Q}\in\mathcal{N}$ for every $z\in\mathbb{C}$.

The cone is smooth away from the apex. The complex gradient of the norm at $\tilde{Q}$ is $2\sum_\mu Q_\mu e_\mu$, and it is never zero except at $\tilde{Q}=0$, since the coefficient vector $Q\in\mathbb{C}^4$ is nonzero away from the apex. Its real and imaginary parts are the two real gradients of the two real equations, and they fail to be independent exactly when the coefficient vector $Q$ lies on a real complex line, $Q=\lambda u$ with $\lambda\in\mathbb{C}$ and $u\in\mathbb{R}^4$ real. Such a $Q$ satisfies $N(Q)=\lambda^2\sum_\mu u_\mu^2=0$ only when $\lambda=0$ or $\sum_\mu u_\mu^2=0$; the second is impossible for real nonzero $u$, because the level-1 form is positive definite on the real vectors. Hence, **away from the apex the two real gradients are independent at every point of $\mathcal{N}$**, and the cone is a real $6$-dimensional manifold there.

**The link.** The intersection

$$
L=\mathcal{N}\cap S^7_E
$$

is a compact five-dimensional manifold, the **link** of the cone, and the cone is the cone over it: $\mathcal{N}\setminus\{0\}\cong L\times\mathbb{R}_{>0}$ under $\tilde{Q}\mapsto(\tilde{Q}/\|\tilde{Q}\|_E,\|\tilde{Q}\|_E)$. Multiplication by a unit complex number preserves both $N=0$ and $\|\cdot\|_E=1$, so the circle $U(1)$ acts on $L$ freely, and the quotient is

$$
L/U(1)\cong S^2\times S^2 ,
$$

so that $L$ is an $S^1$-bundle over $S^2\times S^2$. The four-dimensional quotient is the projectivised null quadric, and its two sphere factors are its two rulings, treated as geometry in *Biquaternion Null Quadric and Projective Geometry*.

**Physical reading.** On the material sector, where the four-position is $\tilde{Q}=ict\,e_0+\mathbf{x}$, the norm is $N(\tilde{Q})=-c^2t^2+\mathbf{x}^2$, so the null cone is exactly the **light cone** of Minkowski space in the $ict$ coordinate. On the informational sector, where the coordinate is $ct'\,e_0+i\mathbf{x}'$, the norm is $N=c^2t'^2-\mathbf{x}'^2$, and the same cone appears as the null cone of the informational coordinates. The two readings are mirror images through the sector exchange $i\mathbb{M}_+=\mathbb{M}_-$.

The physics of the link is the physics of the massless particle. A null momentum $\tilde{P}$ has a direction on the light cone, and the directions of null momenta form the **celestial sphere** $S^2$. The framework's link carries a further circle, the phase of the null spinor, and the second $S^2$ factor is the celestial sphere read on the other chirality. The pair of rulings is the pair of Weyl spinor lines, so the $S^1$-bundle over $S^2\times S^2$ is the statement that a null momentum is carried by a pair of spinors up to a phase, which is the spinor-helicity description of a massless particle.

## Pure Biquaternions and the Roots of Minus One

A **pure** biquaternion has vanishing scalar part, $\tilde{Q}=\sum_{k=1}^{3}Q_k e_k$. Its square is central,

$$
\tilde{Q}^2=-\Big(\sum_{k=1}^{3}Q_k^2\Big)e_0=-N(\tilde{Q})e_0 ,
$$

so a pure element is null exactly when it squares to zero. The **real** roots of $-1$, the elements $\xi$ with $\xi^2=-1$ that lie in the real quaternion slice, are the unit pure quaternions

$$
\xi=xe_1+ye_2+ze_3,\qquad x^2+y^2+z^2=1 ,
$$

which is the sphere $S^2$ of imaginary units of $\mathbb{H}$. The full set of roots of $-1$ in $\mathbb{B}$ is a complex cone over it and is classified in *Biquaternion Roots of Minus One*.

**Physical reading.** The sphere $S^2$ of real roots of $-1$ is the sphere of the spatial rotation axes, and a general root of $-1$ generates a one-parameter subgroup that is a rotation when the generator is real and a mixture of rotation and boost when it is not. The null pure elements are the parabolic directions, the nilpotents, whose one-parameter group is a translation rather than a rotation.

## The Null Cone as the Boundary of the Group of Units

The group of units is the complement of the null cone,

$$
\mathbb{B}^\times=\{\tilde{Q} : N(\tilde{Q})\ne 0\}=\mathbb{B}\setminus\mathcal{N},
$$

because the inverse formula $\tilde{Q}^{-1}=\bar{\tilde{Q}}/N(\tilde{Q})$ requires exactly $N(\tilde{Q})\ne0$. Since $N$ is a continuous complex-valued function, $\mathbb{B}^\times$ is open, and $\mathcal{N}$ is closed. The null cone has empty interior, because it is a proper real algebraic subvariety of an eight-dimensional space, so the group of units is dense in $\mathbb{B}$. Therefore

$$
\partial\,\mathbb{B}^\times=\overline{\mathbb{B}^\times}\cap\overline{\mathcal{N}}=\mathbb{B}\cap\mathcal{N}=\mathcal{N},
$$

and the **null cone is the topological boundary of the group of units**.

**Physical reading.** The invertible elements are the generic elements, and the non-invertible ones are confined to the light cone. The dense openness is what makes the group of units a good arena for the Lorentz action: a small perturbation of an invertible element stays invertible, and the only way to leave the group is to land exactly on the cone. It is also why the group of units of the *real* sectors is disconnected into three pieces separated by the cone, whereas the full group is connected — the statement belongs to *The Biquaternion Unit Group as a Topological Group*.

## Summary

As a real vector space $\mathbb{B}$ is $\mathbb{R}^8$ and is therefore contractible, with $\pi_n(\mathbb{B})=0$ for every $n\ge1$; the algebra carries no topological invariant of its own. The Euclidean unit sphere is $S^7$, with $\pi_7=\mathbb{Z}$ and all lower homotopy groups trivial. The null cone $\{N(\tilde{Q})=0\}$ is a real $6$-dimensional cone with two independent real gradients away from the apex, hence a manifold there, and its link is an $S^1$-bundle over $S^2\times S^2$. On the material sector the null cone is the light cone of the $ict$ coordinate and on the informational sector the null cone of the informational coordinate, and the two are exchanged by multiplication by $i$. The null cone is the topological boundary of the group of units, which is open and dense.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, $Q_\mu\in\mathbb{C}$ | Biquaternion and its four complex coefficients |
| $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$ | Euclidean norm, the level of the Hermitian form |
| $S^7_E=\{\tilde{Q} : \|\tilde{Q}\|_E=1\}$ | Euclidean unit sphere |
| $\mathcal{N}=\{\tilde{Q} : N(\tilde{Q})=0\}$ | Null cone; the light cone of the material sector |
| $L=\mathcal{N}\cap S^7_E$ | Link of the null cone |
| $L/U(1)\cong S^2\times S^2$ | Projectivised null quadric, the two rulings |
| $\mathbb{B}^\times=\mathbb{B}\setminus\mathcal{N}$ | Group of units, open and dense |
| $\partial\mathbb{B}^\times=\mathcal{N}$ | The null cone as the boundary of the units |
| $ict\,e_0+\mathbf{x}$, $ct'\,e_0+i\mathbf{x}'$ | Material and informational coordinates |

## Further Reading

- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the null cone, the zero divisors and the geometry of the complexified quaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the isotropic cones of a complex quadratic space and their rulings.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, vol. 1 (Cambridge, 1984), for the celestial sphere, the null directions and the spinor-helicity description of a massless particle.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the semi-norm, its vanishing locus and the invertibility criterion.
- Charles W. Misner, Kip S. Thorne and John A. Wheeler, *Gravitation* (Freeman, 1973), for the light cone, its generators and the causal structure it carries.
