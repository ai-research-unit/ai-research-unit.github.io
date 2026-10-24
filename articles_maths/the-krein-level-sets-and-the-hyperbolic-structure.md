# __The Krein Level Sets and the Hyperbolic Structure__

## Introduction

The general quaternionic sesquilinear form is indefinite, so its nonzero level sets are neither spheres nor compact: they are hyperboloids, and the geometry they carry is hyperbolic rather than elliptic. This article describes the three sign level sets of the form $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\lvert Q_{\mu}\rvert^{2}$ — the positive set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}$, the negative set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}$ and the null set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}$ — and the hyperbolic structures they carry: the positive region, the complex hyperbolic space of positive lines, the Bergman ball and its geodesics, and the real hyperbolic space of the Lorentzian slice.

The form, its symmetry, its null set, its cone and its positive lines are *The Krein Norm of the Biquaternion Algebra*; the isometry group $\mathrm{U}(1,3)$, its maximal compact part, its Cartan involution and the identification of the symmetric space are *The Krein Isometry Group and Its Cartan Decomposition*; the general ball, its Bergman metric and its geodesics are *Hermitian Symmetric Spaces and the Bergman Metric*; the real hyperboloid model is *Hyperbolic Geometry*; and the comparison with the definite sphere is *The Four Forms and the Four Algebraic Norms*. This article owns the topology of the level sets, the phase and scaling actions on them, and the reading of the ball and of the real slices as hyperbolic spaces.

## The Three Level Sets

**Theorem (the level sets and their homotopy types).** In the splitting $\tilde{Q}=c+v$ into the centre and vector parts,

$$
\boxed{\;\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}=\Bigl\{(c,v):\|c\|_E^{2}=1+\|v\|_E^{2}\Bigr\}\cong S^{1}\times\mathbb{R}^{6}\;},
$$
$$
\boxed{\;\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}=\Bigl\{(c,v):\|v\|_E^{2}=1+\|c\|_E^{2}\Bigr\}\cong S^{5}\times\mathbb{R}^{2}\;},
$$
$$ \{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}=\{(c,v):\|c\|_E=\|v\|_E\}=C(S^{1}\times S^{5}), $$

the cone on $S^{1}\times S^{5}$ with apex at the origin; all three are of real dimension $7$, the first is homotopy equivalent to $S^{1}$, the second to $S^{5}$, and the third is contractible, its complement of the apex being $S^{1}\times S^{5}\times\mathbb{R}_{>0}\simeq S^{1}\times S^{5}$.

*Proof.* For the first, a pair $(c,v)$ satisfies the equation exactly when $c$ lies on the circle of radius $\sqrt{1+\|v\|_E^{2}}$ in the centre, so the map $(c,v)\mapsto(c/\|c\|_E,\ v)$ identifies the set with $S^{1}\times\mathbb{R}^{6}$: the pair $(v,c/\|c\|_E)$ is free and determines $c$. For the second, in the same way $\|v\|_E=\sqrt{1+\|c\|_E^{2}}>0$, so $v$ is determined by its direction in the five-sphere and by $c$, which is free in $\mathbb{C}$; the set is $S^{5}\times\mathbb{R}^{2}$. For the third, both norms are equal to some $t\ge0$; the set is the cone over $S^{1}\times S^{5}$, the pair of directions with the radius, with the apex at $t=0$.

**Remark (what is lost and what is kept).** Compared with the Euclidean sphere $S^{7}$ of *The Euclidean Topology of the Biquaternion Algebra*, the positive level set loses compactness and the sphere: it is the product of a circle with a six-dimensional Euclidean space, a hyperboloid of revolution. All three sets are connected and non-compact, as the signature $(2,6)$ over $\mathbb{R}$ requires, and the negative set has the homotopy type of $S^{5}$ alone because its vector part is forced away from the origin while its scalar part is free.

## The Positive Region and the Positive Lines

**Definition.** The **positive region** is the open cone $\mathcal{P}=\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}>0\}$, the interior of the Krein cone; the **negative region** is $\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}<0\}$; and a **positive line** is a complex line consisting of positive elements.

**Theorem (the positive region retracts onto a circle).** The positive region is $\{\|c\|_E>\|v\|_E\}$, it is a cone, and it is homotopy equivalent to $S^{1}$; the negative region is homotopy equivalent to $S^{5}$.

*Proof.* For the first, the map $\tilde{Q}\mapsto c/\|c\|_E$ is defined on the positive region, since $\|c\|_E>\|v\|_E\ge0$ forces $c\neq0$; for fixed $c$ the vector part ranges over the open ball of radius $\|c\|_E$, a contractible set, so the projection onto $\mathbb{C}\setminus\{0\}\simeq S^{1}$ is a homotopy equivalence. For the second, $\|v\|_E>\|c\|_E$ forces $v\neq0$, and the projection onto $v/\|v\|_E\in S^{5}$ has contractible fibres again.

**Theorem (the positive lines form the complex hyperbolic ball).** The positive lines are exactly the lines $\mathbb{C}(e_t+\tilde Q_1)$ with $\|\tilde Q_1\|_E<1$; the assignment $\tilde Q_1\mapsto\mathbb{C}(e_t+\tilde Q_1)$ is a bijection of the open unit ball of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^{3}$ onto the set of positive lines. That set is therefore a real manifold of dimension $6$, isomorphic as a homogeneous space to

$$
\mathrm{U}(1,3)\,/\,\bigl(\mathrm{U}(1)\times \mathrm{U}(3)\bigr),
$$

the **complex hyperbolic space** $\mathbb{CH}^{3}$.

*Proof.* A positive line is not contained in $\mathbb{V}_{\mathbb{B}}$, since the form is negative definite there; choosing the unique representative $e_t+\tilde Q_1$ and using $\langle e_t+\tilde Q_1,e_t+\tilde Q_1\rangle_{\natural*}=1-\|\tilde Q_1\|_E^{2}$ shows that positivity is exactly $\|\tilde Q_1\|_E<1$, and the assignment is bijective. The stabiliser of the line $\mathbb{C}e_t$ in $\mathrm{U}(1,3)$ is the group preserving the canonical fundamental decomposition, which is $\mathrm{U}(1)\times \mathrm{U}(3)$, and the action is transitive on the positive lines (*The Krein Isometry Group and Its Cartan Decomposition*, §*The Actions of the Group*); the two realisations agree because both are the symmetric space of the same Cartan pair.

**Theorem (the phase action and the real scaling).** The phase circle $S^{1}$ acts on $\mathbb{B}$ by $\tilde{Q}\mapsto\lambda\tilde{Q}$, $\lvert\lambda\rvert=1$, preserving the form and each level set; the action is free on $\mathbb{B}\setminus\{0\}$, and its quotient on the positive level set is the complex hyperbolic space $\mathbb{CH}^{3}$ of positive lines. Real scaling by $s>0$ relates the levels $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=t\}$ and $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=s^{2}t\}$, so the positive region is the union of the positive levels over $t>0$. The positive level set is a principal $S^{1}$-bundle over $\mathbb{CH}^{3}\cong\mathbb{R}^{6}$, hence diffeomorphic to $S^{1}\times\mathbb{R}^{6}$.

*Proof.* $\lvert\lambda\rvert^{2}=1$ makes the value invariant, so the phase preserves every level set; the action is free because $\lambda\tilde{Q}=\tilde{Q}$ with $\tilde{Q}\neq0$ forces $\lambda=1$. The quotient of the positive level set by the phase circle is the set of positive lines, which is $\mathbb{CH}^{3}$ by the preceding theorem. A principal circle bundle over the contractible space $\mathbb{CH}^{3}\cong\mathbb{R}^{6}$ is trivial, and the diffeomorphism with $S^{1}\times\mathbb{R}^{6}$ is the one of §*The Three Level Sets*. Real scaling acts by $t\mapsto s^{2}t$ because $\langle s\tilde{Q},s\tilde{Q}\rangle_{\natural*}=s^{2}\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}$ for real $s>0$.

**Remark (the boundary).** The closure of the ball adds the isotropic lines, $\|\tilde Q_1\|_E=1$, a copy of $S^{5}$: the boundary sphere of the complex hyperbolic ball, of real dimension $5$, while the ball itself has real dimension $6$ (§*The Isotropic Boundary*).

## The Metric and the Geodesics of the Ball

**Theorem (the Bergman metric).** The unit ball $B^{3}\subset\mathbb{V}_{\mathbb{B}}=\mathbb{C}^{3}$ carries the **Bergman metric**

$$
\boxed{\;ds^{2}=\frac{(1-\|\tilde Q_1\|_E^{2})\,\|d\tilde Q_1\|_E^{2}+\lvert\langle d\tilde Q_1,\tilde Q_1\rangle_{*}\rvert^{2}}{(1-\|\tilde Q_1\|_E^{2})^{2}}\;},
$$

which is Kähler, complete, of constant negative holomorphic sectional curvature, and invariant under the action of $\mathrm{U}(1,3)$; the boundary $S^{5}$ is at infinite distance.

*Proof.* This is the Bergman metric of the unit ball of $\mathbb{C}^{3}$ (*Hermitian Symmetric Spaces and the Bergman Metric*), invariant under the biholomorphisms of the ball; the isometry group of the form acts on the ball through $PU(1,3)$, which is its full biholomorphism group, so the metric is invariant under $\mathrm{U}(1,3)$. Completeness and constant curvature are the standard properties of the ball, and the boundary is at infinite distance because the metric blows up at $\|\tilde Q_1\|_E=1$.

**Theorem (the complex geodesics and the real slices).** The intersection of the ball with a complex line is a copy of the unit disc, totally geodesic in $\mathbb{CH}^{3}$ and isometric to $\mathbb{CH}^{1}$; the geodesic through the origin and a point $\tilde Q_1\neq0$ is the disc $\{z\,\tilde Q_1/\|\tilde Q_1\|_E:\lvert z\rvert<1\}$. The Lorentzian slice $\mathbb{H}_{\mathbb{B}}$ meets the ball in the real unit ball of $\mathbb{R}^{3}$, on which the Bergman metric restricts to the Poincaré metric of $H^{3}$; the slice is totally geodesic and totally real in $\mathbb{CH}^{3}$.

*Proof.* A complex line $\mathbb{C}w$ meets the ball in the disc $\{z\,w/\|w\|_E:\lvert z\rvert<1\}$, which contains $0$ and the boundary point $w/\|w\|_E$; the restriction of the Bergman metric to a complex line is a multiple of the Poincaré metric of the disc, so the disc is totally geodesic, and every complex line is the image of $\mathbb{C}\tilde Q_1$ under an isometry because $\mathrm{U}(1,3)$ is transitive on the complex lines that carry positive vectors. On the slice the form is the interval form, and the ball meets $\mathbb{R}^{3}$ in the real unit ball, on which the Bergman metric is the hyperbolic metric of the disc model; a real subspace of maximal dimension on which the form is real is totally real, and the standard totally geodesic submanifolds of $\mathbb{CH}^{3}$ are the complex lines and the real hyperbolic spaces (*Hermitian Symmetric Spaces and the Bergman Metric*).

## The Lorentzian Slices

**Theorem (the real hyperboloids).** On the Hermitian subspace $\mathbb{M}_{+}$ and on the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the general quaternionic sesquilinear form is the interval form of Lorentzian space, and with the real coordinates $q$,

$$ \langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=q_t^{2}-q_x^{2}-q_y^{2}-q_z^{2}. $$

The positive level set is the two-sheeted hyperboloid, whose sheet $q_t>0$ is given by $q_t=\sqrt{1+\|\vec q\|^{2}}$ with $\vec q\in\mathbb{R}^{3}$ free, hence is $\mathbb{R}^{3}$; the negative level set is the one-sheeted hyperboloid $q_t^{2}=\|\vec q\|^{2}-1$, diffeomorphic to $S^{2}\times\mathbb{R}$; and the null set is the null cone, of two nappes.

*Proof.* The restricted form is $\sum_{\mu}\varepsilon_{\mu}q_{\mu}^{2}$ in the four real coordinates of the slice (*The Krein Norm of the Biquaternion Algebra*). Solving $q_t^{2}-\|\vec q\|^{2}=1$ for $q_t$ gives the two sheets, each parametrised by $\vec q\in\mathbb{R}^{3}$. Solving $q_t^{2}-\|\vec q\|^{2}=-1$ gives $\|\vec q\|\ge1$ with $q_t$ free, so the set is $\mathbb{R}\times S^{2}$ by the direction of $\vec q$. The null equation factors as $(q_t-\|\vec q\|)(q_t+\|\vec q\|)=0$, giving the two nappes of the null cone.

**Corollary (the hyperboloid model of $H^{3}$).** The sheet $q_t=\sqrt{1+\|\vec q\|^{2}}$ carries the Riemannian metric induced by the Lorentz form and is the **hyperboloid model of the real hyperbolic space** $H^{3}$ (*Hyperbolic Geometry*, §*The Hyperboloid and Beltrami–Klein Models*); the Lorentz boosts of *Biquaternion Rotations and Lorentz Transformations* act on it by its isometries. The complex hyperbolic ball is the complexification of this picture: dimension $6$ instead of $3$, the sphere $S^{5}$ instead of $S^{2}$, and the group $\mathrm{U}(1,3)$ instead of the Lorentz group.

## The Cone and the Other Levels

**Remark (the cone is the union of the levels).** The Krein cone $P_K=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}\ge0\}=\{\|c\|_E\ge\|v\|_E\}$ is the union of the origin, the positive region and the null set; its interior is the positive region, its boundary is the null set, and it contains the whole positive axis and no negative element (*The Krein Norm of the Biquaternion Algebra*, §*The Krein Cone*). The unit positive level set is a hyperboloid sheet inside the interior, the negative level set lies outside, and the cone is the union of the positive levels over $t\ge0$, rescaled to $t=1$ by the real scaling above; on a Lorentzian slice the intersection is the full null cone, whose future nappe is the Hermitian cone.

**Remark (the norm levels and the definite sphere).** The algebraic norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ is holomorphic, so its nonzero levels are complex hypersurfaces of real dimension $6$, and its zero set is the zero-divisor cone (*The Topology of the Zero-Divisor Cone*); the general quaternionic sesquilinear form is real on the diagonal and its levels are the real hypersurfaces of dimension $7$ described here (*The Four Forms and the Four Algebraic Norms*). The definite companion is the Euclidean norm, whose levels are the spheres $S^{7}$; the bridge $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\langle\tilde{Q},J\tilde{Q}\rangle_{*}$ writes the indefinite level as the sphere twisted by $J$, which is the whole difference between $S^{7}$ and the three hyperboloids.

## The Isotropic Boundary

**Theorem (the isotropic lines form $S^{5}$).** The isotropic complex lines of the general quaternionic sesquilinear form are exactly the lines $\mathbb{C}(e_t+\tilde Q_1)$ with $\|\tilde Q_1\|_E=1$, so the assignment $\tilde Q_1\mapsto\mathbb{C}(e_t+\tilde Q_1)$ is a bijection from the unit sphere of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^{3}$ — a copy of $S^{5}$ — onto the set of isotropic lines. This is the boundary of the ball of positive lines.

*Proof.* An isotropic line $\mathbb{C}\tilde{Q}$ has $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$, hence $\|c\|_E=\|v\|_E$, so it is not contained in $\mathbb{V}_{\mathbb{B}}$ and admits a representative with nonzero scalar part; scaling it gives exactly one representative of the form $e_t+\tilde Q_1$. For that representative $\langle e_t+\tilde Q_1,e_t+\tilde Q_1\rangle_{\natural*}=1-\|\tilde Q_1\|_E^{2}$, so the line is isotropic exactly for $\|\tilde Q_1\|_E=1$; and distinct points $\tilde Q_1$ of the unit sphere give distinct lines, since $e_t+\tilde Q_1$ and $e_t+\tilde Q_1'$ span the same line only if $\tilde Q_1=\tilde Q_1'$. This is the boundary case of the parametrisation of the maximal positive definite subspaces in *The Krein Norm of the Biquaternion Algebra*, which uses the open ball $\|\tilde Q_1\|_E<1$.

## Worked Examples

**A point of the positive level set.** $\tilde{Q}=e_t$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1$, the base point of the ball.

**A point of the negative level set.** $\tilde{Q}=\vec e_x+\vec e_y$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-2$, so $\tilde{Q}/\sqrt2$ has square $-1$.

**Two points of the null set.** $e_t+\vec e_x$ and $(e_t+\vec e_x)/\sqrt2$: the first has square $0$ and Euclidean norm $\sqrt2$, the second square $0$ and Euclidean norm $1$; the second is on the link, and both are on the boundary of the ball.

**A line inside the ball and a line on its boundary.** $\mathbb{C}(e_t+\tfrac12\vec e_x)$ has $\|\tilde Q_1\|_E=\tfrac12<1$ and is a point of the ball; $\mathbb{C}(e_t+\vec e_x)$ has $\|\tilde Q_1\|_E=1$ and is a point of the boundary sphere $S^{5}$.

**A real timelike point.** $\tilde{Q}=e_t+\tfrac12\vec e_x$ in $\mathbb{H}_{\mathbb{B}}$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\tfrac34>0$, a point of the Lorentzian hyperboloid sheet.

**A phase orbit.** $e_t$ and $ie_t$ are both on the unit positive level set and on the same positive line; the phase circle acts on the level set with the orbit as the fibre of the bundle over $\mathbb{CH}^{3}$.

## Summary

The sign level sets of the general quaternionic sesquilinear form are the hyperboloids $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}\cong S^{1}\times\mathbb{R}^{6}\simeq S^{1}$ and $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}\cong S^{5}\times\mathbb{R}^{2}\simeq S^{5}$, and the null set is the cone on $S^{1}\times S^{5}$, contractible, its complement of the apex being $S^{1}\times S^{5}\times\mathbb{R}_{>0}\simeq S^{1}\times S^{5}$; all are non-compact of real dimension $7$, in contrast with the compact Euclidean sphere $S^{7}$. The positive region $\{\|c\|_E>\|v\|_E\}$ retracts onto the circle of phases and the negative region onto $S^{5}$. The positive lines are the lines $\mathbb{C}(e_t+\tilde Q_1)$ with $\|\tilde Q_1\|_E<1$, so they form the open unit ball of $\mathbb{C}^{3}$, of real dimension $6$, the complex hyperbolic space $\mathbb{CH}^{3}=\mathrm{U}(1,3)/(\mathrm{U}(1)\times \mathrm{U}(3))$, with boundary the isotropic sphere $S^{5}$. On a Lorentzian slice the same picture degenerates to the sheet $q_t=\sqrt{1+\|\vec q\|^{2}}$ of the real hyperboloid, the hyperboloid model of $H^{3}$, the one-sheeted hyperboloid $S^{2}\times\mathbb{R}$ and the two nappes of the null cone. The phase circle acts freely on the positive level set with quotient $\mathbb{CH}^{3}$, real scaling relates the positive levels, and the ball carries the Bergman metric, complete and of constant negative holomorphic curvature, whose complex geodesics are the intersections with the complex lines and whose totally geodesic real slices are the Lorentzian hyperboloids.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}\cong S^{1}\times\mathbb{R}^{6}$ | The positive level set; $\simeq S^{1}$ |
| $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}\cong S^{5}\times\mathbb{R}^{2}$ | The negative level set; $\simeq S^{5}$ |
| $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}=C(S^{1}\times S^{5})$ | The null set, contractible |
| $\mathcal{P}=\{\lVert c\rVert_E>\lVert v\rVert_E\}$ | The positive region; $\simeq S^{1}$ |
| $\mathbb{C}(e_t+\tilde Q_1)$, $\lVert\tilde Q_1\rVert_E<1$ | The positive lines; the ball of $\mathbb{C}^{3}$ |
| $\mathbb{CH}^{3}=\mathrm{U}(1,3)/(\mathrm{U}(1)\times \mathrm{U}(3))$ | The complex hyperbolic space of positive lines |
| $q_t^{2}-\lVert\vec q\rVert^{2}=\pm1$ | The real hyperboloids in a Lorentzian slice |
| $q_t=\sqrt{1+\lVert\vec q\rVert^{2}}$ | The hyperboloid model of $H^{3}$ |
| $S^{1}$ phase and $\mathbb{R}_{>0}$ scaling | The actions on the level sets; the positive level is an $S^{1}$-bundle over $\mathbb{CH}^{3}$ |
| $ds^{2}$ of §*The Metric and the Geodesics of the Ball* | The Bergman metric; complete, constant negative curvature |
| $P_K=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}\ge0\}$ | The Krein cone: origin, positive region, null set |
| $\{\langle\tilde{Q}\rangle_{\natural}=\lambda\}$, $\lambda\neq0$ | The norm hypersurfaces; complex, real dimension $6$ |

## Further Reading

- [The Krein Norm of the Biquaternion Algebra](the-krein-norm-of-the-biquaternion-algebra.html), for the form, the null set, the cone, the positive lines and the bridge $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\langle\tilde{Q},J\tilde{Q}\rangle_{*}$
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the group $\mathrm{U}(1,3)$, its maximal compact part, its transitive actions and the symmetric space
- [Hermitian Symmetric Spaces and the Bergman Metric](hermitian-symmetric-spaces-and-the-bergman-metric.html), for the general ball, its metric, its geodesics and its totally real slices
- [Hyperbolic Geometry](hyperbolic-geometry.html), for the hyperboloid model of $H^{3}$ and its isometries
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the boosts acting on the Lorentzian hyperboloid
- [The Euclidean Topology of the Biquaternion Algebra](the-euclidean-topology-of-the-biquaternion-algebra.html), for the compact sphere used here for contrast
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the four forms, their four null sets and the definite companion
