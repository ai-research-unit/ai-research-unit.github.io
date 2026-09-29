# __Biquaternion Topology__

## Introduction

This article describes the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ as a topological space, together with the two subsets of it that the framework singles out: the Euclidean unit sphere and the null cone. It then reads the projective geometry of that cone: the Segre embedding, the two rulings of null planes, the projective null quadric $Q^2$ with its tangency and its polarity, the Klein–Plücker geometry of the lines of $\mathbb{P}^3$, and the automorphisms of the quadric. It uses the algebra and the six distinguished subspaces of *Biquaternion Algebra*, the coordinates, the $ict$ assignment and the sector split of *Conventions in the Biquaternion Universe*, and the biquaternion norm $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ and the invertibility criterion of *Biquaternion Norm and Invertibility*. The form itself is not re-derived here.

The norm vanishes exactly on the zero divisors together with the origin (*Biquaternion Norm and Invertibility*, *Biquaternion Zero Divisors*); the algebraic treatment is in those two articles, and the geometric treatment, as the equation of a quadric, is the second half of this article. Physically the null quadric is the celestial sphere of the light cone: a null direction of the material sector $\mathbb{M}_-$ is a point of $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, and the two rulings of the quadric are the left- and right-handed Weyl spinors; its polarity is the Hodge duality of the field strengths, the map that exchanges the electric and magnetic fields.

**Scope.** The topology of the **group of units** $\mathbb{B}^\times$ — the polar decomposition, the retractions onto the compact subgroups, the homotopy groups, the universal cover and the connected components — belongs to the Lie theory of the algebra and is treated in *The Biquaternion Unit Group as a Topological Group*. The differentiability statement that the null cone is smooth away from the apex belongs to *Biquaternion Analysis*, where the derivative is available. This article owns the ambient space, its distinguished subsets and the projective geometry of the null cone.

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

The cone is smooth away from the apex. The complex gradient of the norm at $\tilde{Q}$ is $2\sum_\mu Q_\mu e_\mu$, and it is never zero except at $\tilde{Q}=0$, since the coefficient vector $Q\in\mathbb{C}^4$ is nonzero away from the apex. Its real and imaginary parts are the two real gradients of the two real equations, and they fail to be independent exactly when the coefficient vector $Q$ lies on a real complex line, $Q=\lambda u$ with $\lambda\in\mathbb{C}$ and $u\in\mathbb{R}^4$ real. Such a $Q$ satisfies $N(Q)=\lambda^2\sum_\mu u_\mu^2=0$ only when $\lambda=0$ or $\sum_\mu u_\mu^2=0$; the second is impossible for real nonzero $u$, because the level-1 form is positive definite on the real vectors. Hence, **away from the apex the two real gradients are independent at every point of $\mathcal{N}$**, and the cone is a real $6$-dimensional manifold there. Punctured, it is exactly the zero-divisor set of *Biquaternion Zero Divisors*, $\mathcal{N}\setminus\{0\}=\mathcal{Z}$, and $\mathcal{N}=\{0\}\cup\mathcal{Z}$.

**The link.** The intersection

$$
L=\mathcal{N}\cap S^7_E
$$

is a compact five-dimensional manifold, the **link** of the cone, and the cone is the cone over it: $\mathcal{N}\setminus\{0\}\cong L\times\mathbb{R}_{>0}$ under $\tilde{Q}\mapsto(\tilde{Q}/\|\tilde{Q}\|_E,\|\tilde{Q}\|_E)$. Multiplication by a unit complex number preserves both $N=0$ and $\|\cdot\|_E=1$, so the circle $U(1)$ acts on $L$ freely, and the quotient is

$$
L/U(1)\cong S^2\times S^2 ,
$$

so that $L$ is an $S^1$-bundle over $S^2\times S^2$. The four-dimensional quotient is the projectivised null quadric, and its two sphere factors are its two rulings, treated as geometry in §*The projective null quadric $Q^2$*.

**Physical reading.** On the material sector, where the four-position is $\tilde{Q}=ict\,e_0+\mathbf{x}$, the norm is $N(\tilde{Q})=-c^2t^2+\mathbf{x}^2$, so the null cone is exactly the **light cone** of Minkowski space in the $ict$ coordinate. On the informational sector, where the coordinate is $ct'\,e_0+i\mathbf{x}'$, the norm is $N=c^2(t')^2-(\mathbf{x}')^2$, and the same cone appears as the null cone of the informational coordinates. The two readings are mirror images through the sector exchange $i\mathbb{M}_+=\mathbb{M}_-$.

The physics of the link is the physics of the massless particle. A null momentum $\tilde{P}$ has a direction on the light cone, and the directions of null momenta form the **celestial sphere** $S^2$. The framework's link carries a further circle, the phase of the null spinor, and the second $S^2$ factor is the celestial sphere read on the other chirality. The pair of rulings is the pair of Weyl spinor lines, so the $S^1$-bundle over $S^2\times S^2$ is the statement that a null momentum is carried by a pair of spinors up to a phase, which is the spinor-helicity description of a massless particle.

## The Segre embedding

Choose on $\mathbb{B}$ the linear coordinates
$$
X_0=Q_0-iQ_3,\qquad X_1=-iQ_1-Q_2,\qquad X_2=-iQ_1+Q_2,\qquad X_3=Q_0+iQ_3,
$$
an invertible $\mathbb{C}$-linear change of the coordinates $Q_0,\dots,Q_3$. In them the norm is a split form,
$$
N(\tilde{Q})=\sum_{\mu=0}^{3}Q_\mu^2=X_0X_3-X_1X_2,
$$
since $X_0X_3=(Q_0-iQ_3)(Q_0+iQ_3)=Q_0^2+Q_3^2$ and $X_1X_2=(-iQ_1-Q_2)(-iQ_1+Q_2)=-Q_1^2-Q_2^2$. The null cone is therefore the affine hypersurface $X_0X_3=X_1X_2$, and each of its nonzero points is a pair of one-dimensional subspaces of $\mathbb{C}^2$. Indeed, for nonzero $u=(\alpha,\beta)$ and $v=(\gamma,\delta)$ the point
$$
(X_0,X_1,X_2,X_3)=(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)
$$
lies on the null cone, since $\alpha\gamma\cdot\beta\delta=\alpha\delta\cdot\beta\gamma$, and conversely every null point is of this form: if $X_0\neq0$ the pair $u=(1,X_2/X_0)$, $v=(X_0,X_1)$ reproduces it, and the other cases are the same argument applied to a coordinate that is nonzero. The pair is determined only up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$. Projectivising gives the **Segre embedding**
$$
s:\mathbb{P}^1\times\mathbb{P}^1\longrightarrow\mathbb{P}^3,\qquad ([u],[v])\mapsto[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta],
$$
whose image is exactly the projective null quadric
$$
\mathbb{P}(\mathcal{N})=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}.
$$
The affine null cone is the cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$, and the zero-divisor set is that cone with its apex removed.

## The two rulings of null planes

In the coordinates above the polar form of $N$ is
$$
B(X,Y)=\tfrac12\bigl(X_0Y_3+X_3Y_0-X_1Y_2-X_2Y_1\bigr),
$$
the polarisation of $X_0X_3-X_1X_2$, with $B(X,X)=N(X)$. For each $[u]=[\alpha:\beta]\in\mathbb{P}^1$ the two-dimensional subspace
$$
W_{[u]}=\operatorname{span}\{(\alpha,0,\beta,0),\,(0,\alpha,0,\beta)\}=\{(\alpha\sigma,\alpha\tau,\beta\sigma,\beta\tau):\sigma,\tau\in\mathbb{C}\}
$$
is totally isotropic: for $X$ built from $\sigma,\tau$ and $Y$ from $\sigma',\tau'$ the form above gives $B(X,Y)=\tfrac12\alpha\beta(\sigma\tau'+\tau\sigma'-\tau\sigma'-\sigma\tau')=0$. Since $\dim W_{[u]}=2$ is the maximal isotropic dimension for a non-degenerate form in dimension $4$, $W_{[u]}$ is a **null plane**, and the same holds for
$$
W^{[v]}=\operatorname{span}\{(\gamma,\delta,0,0),\,(0,0,\gamma,\delta)\},\qquad [v]=[\gamma:\delta].
$$
Their projectivisations $\ell_{[u]}=\mathbb{P}(W_{[u]})$ and $m_{[v]}=\mathbb{P}(W^{[v]})$ are the **two rulings**: each family is a $\mathbb{P}^1$ of lines; every quadric point lies on exactly one line of each family; lines of the same family are disjoint, while lines of different families meet in exactly one point, the point $[(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)]$ that the pair $([u],[v])$ determines.


## The projective null quadric $Q^2$

The projectivised null cone
$$
Q^2=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}
$$
is a smooth irreducible quadric surface, isomorphic to $\mathbb{P}^1\times\mathbb{P}^1$; it is the classical **Segre quadric**. Non-degeneracy of $B$ gives smoothness, and over $\mathbb{C}$ all smooth quadric surfaces in $\mathbb{P}^3$ are projectively equivalent.

Its real points depend on the real form of *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*: empty for the definite form on $\mathbb{H}_{\mathbb{B}}$; the sphere $S^2$ for the Lorentzian form on $\mathbb{M}_+$ (or $\mathbb{M}_-$); the torus $S^1\times S^1$ for the split form of signature $(2,2)$. Only in the split case does the real quadric contain real lines.

## Lines in $\mathbb{P}^3$, the Klein quadric, and the Plücker embedding

A line in $\mathbb{P}^3$ is $\mathbb{P}(U)$ for a two-dimensional subspace $U\subset\mathbb{C}^4$. With a basis $x,y$ of $U$, the **Plücker coordinates** are the six minors
$$
p_{ij}=x_iy_j-x_jy_i,\qquad 0\le i < j\le3,
$$
the coordinates of the decomposable bivector $x\wedge y\in\Lambda^2\mathbb{C}^4$, defined up to an overall scalar. This gives the **Plücker embedding**
$$
\mathrm{Gr}(2,4)\hookrightarrow\mathbb{P}(\Lambda^2\mathbb{C}^4)=\mathbb{P}^5,
$$
whose image is the **Klein quadric**, the quadric hypersurface of dimension $4$ cut out by the Plücker relation
$$
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0 .
$$
Over $\mathbb{R}$ the Plücker form has signature $(3,3)$. This Klein quadric in $\mathbb{P}^5$ is distinct from the null quadric $Q^2$ in $\mathbb{P}^3$: it is the variety of lines of the projective space in which $Q^2$ sits.

The rulings of $Q^2$ appear in this picture as follows. A line of $Q^2$ is a maximal isotropic two-plane, and its Plücker point lies on the Klein quadric. The lines on $Q^2$ form two components, the two rulings, each a $\mathbb{P}^1$; their Plücker images are two conics on the Klein quadric. (The maximal isotropic subspaces of the Klein quadric itself are two families of projective planes $\mathbb{P}^2$: the stars of lines through a fixed point and the plane fields of lines in a fixed plane.)

## Tangency and polarity

The form $B$ defines a **polarity**, the correlation
$$
[\tilde{P}]\longmapsto[\tilde{P}]^{\perp}=\{[\tilde{Q}]:B(\tilde{P},\tilde{Q})=0\},
$$
well defined by bilinearity and bijective by non-degeneracy. The quadric is the locus of self-polar points, $[\tilde{P}]\in Q^2\iff B(\tilde{P},\tilde{P})=0$. For $[\tilde{P}]\in Q^2$, since the differential of $N$ at $\tilde{P}$ is $2B(\tilde{P},\cdot\,)$, the polar hyperplane is the **tangent hyperplane**, and its intersection with the quadric is the pair of ruling lines through $[\tilde{P}]$,
$$
Q^2\cap[\tilde{P}]^{\perp}=\ell_{[u]}\cup m_{[v]},
$$
one line from each family. For two distinct null points $[\tilde{P}],[\tilde{Q}]$, the biquaternion norm on the line $\tilde{P}+t\tilde{Q}$ is $2t\,B(\tilde{P},\tilde{Q})$, so
$$
[\tilde{P}][\tilde{Q}]\subset Q^2\iff B(\tilde{P},\tilde{Q})=0,
$$
in which case the two points lie on a common ruling line. A line through $[\tilde{P}]\in Q^2$ is therefore tangent exactly when its direction lies in the tangent hyperplane; the two ruling lines are tangent, and every other tangent line meets the quadric only at $[\tilde{P}]$.


## Automorphisms of the complex quadric

The projective automorphisms of $Q^2$ are induced by the complex orthogonal group of $N$:
$$
\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})=O_4(\mathbb{C})/\{\pm I\},
$$
acting on $\mathbb{P}^1\times\mathbb{P}^1$ by $([u],[v])\mapsto([Au],[Bv])$, with the $\mathbb{Z}/2$ exchanging the rulings. Its identity component $PSO_4(\mathbb{C})$ preserves each ruling; the outer component swaps them.
**Physical reading: the celestial sphere and the Hodge duality.** The projective null quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$ is the celestial sphere of the light cone: a null direction of the material sector $\mathbb{M}_-$ is a point of $Q^2$, and the two rulings are the two chiralities of the massless field, one family of spinor lines for each. The tangency and polarity of the quadric are then the Hodge duality $\star$: on a bivector it is the map that exchanges the electric and magnetic fields, so the self-dual and anti-self-dual parts of a field strength are the two rulings read on the field, the Riemann–Silberstein combination of *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form* and the free-field content of *Biquaternion Electromagnetism*.


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

The projectivised null cone is the smooth quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, the Segre quadric; the null cone is the affine cone over it, and its two rulings are the two families of maximal isotropic null planes, each a $\mathbb{P}^1$. In the coordinates of §*The Segre embedding* the norm is $X_0X_3-X_1X_2$ and the polar form is $B$; the quadric is the locus of self-polar points, and the polarity gives the tangency. The quadric sits in the Plücker–Klein geometry of the lines of $\mathbb{P}^3$, and $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})$, while $SO^+(1,3)$ is the conformal group of the projective null cone $S^2$, not the automorphism group of the complex quadric. Physically $Q^2$ is the celestial sphere of the light cone, its two rulings are the two Weyl chiralities, and its polarity is the Hodge duality of the electromagnetic field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, $Q_\mu\in\mathbb{C}$ | Biquaternion and its four complex coefficients |
| $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$ | Euclidean norm, the level of the Hermitian form |
| $S^7_E=\{\tilde{Q} : \|\tilde{Q}\|_E=1\}$ | Euclidean unit sphere |
| $\mathcal{N}=\{\tilde{Q} : N(\tilde{Q})=0\}$ | Null cone; the light cone of the material sector |
| $L=\mathcal{N}\cap S^7_E$ | Link of the null cone |
| $L/U(1)\cong S^2\times S^2$ | Projectivised null quadric, the two rulings |
| $Q^2 = \mathbb{P}(\mathcal{N}) \cong \mathbb{P}^1 \times \mathbb{P}^1$ | Projective null quadric, the Segre quadric; the celestial sphere |
| $B(\tilde{P},\tilde{Q}) = \sum_\mu P_\mu Q_\mu$ | Polar form of $N$, the complex bilinear dot product |
| $X_0,\dots,X_3$ | Linear coordinates on $\mathbb{B}$ in which $N = X_0X_3 - X_1X_2$; see §*The Segre embedding* |
| $[u] = [\alpha:\beta]$, $[v] = [\gamma:\delta]$ | The two factors of a null point, up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ |
| $\ell_{[u]}, m_{[v]}$ | The two rulings of $Q^2$; the two chiralities |
| $p_{ij} = x_i y_j - x_j y_i$ | Plücker coordinates; the Klein quadric in $\mathbb{P}^5$ is their Plücker locus |
| $\operatorname{Aut}(Q^2) \cong PO_4(\mathbb{C})$ | Projective automorphisms of the quadric |
| $\mathbb{B}^\times=\mathbb{B}\setminus\mathcal{N}$ | Group of units, open and dense |
| $\partial\mathbb{B}^\times=\mathcal{N}$ | The null cone as the boundary of the units |
| $ict\,e_0+\mathbf{x}$, $ct'\,e_0+i\mathbf{x}'$ | Material and informational coordinates |

## Further Reading

- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the null cone, the zero divisors and the geometry of the complexified quaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the isotropic cones of a complex quadratic space and their rulings.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, vol. 1 (Cambridge, 1984), for the celestial sphere, the null directions and the spinor-helicity description of a massless particle.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the semi-norm, its vanishing locus and the invertibility criterion.
- Charles W. Misner, Kip S. Thorne and John A. Wheeler, *Gravitation* (Freeman, 1973), for the light cone, its generators and the causal structure it carries.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992).
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978).
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Igor R. Shafarevich, *Basic Algebraic Geometry 1: Varieties in Projective Space* (Springer, 3rd ed., 2013).
