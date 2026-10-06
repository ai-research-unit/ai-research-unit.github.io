# __The Krein Level Sets and the Hyperbolic Structure__

## Introduction

The quaternion sesquilinear form is indefinite, so its nonzero level sets are neither spheres nor compact: they are hyperboloids, and the geometry they carry is hyperbolic rather than elliptic. This article describes the three sign level sets of the form $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ — the positive set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}$, the negative set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}$ and the null set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}$ — and the two models of hyperbolic space that the sign sets produce: the **complex hyperbolic space** of positive definite complex lines, which is the open unit ball of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^{3}$ and coincides with the symmetric space $U(1,3)/(U(1)\times U(3))$ of *The Krein Cartan Decomposition of the Operator Algebra*, and the **real hyperbolic space** $H^{3}$ of the Minkowski slice, which is the sheet of the real hyperboloid. The isotropic structure at the boundary is *The Isotropic Structure of the Krein Form*; the cone of the form is *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*.

**Conventions.** $e_0=1$, $e_k^{2}=-e_0$, central scalar imaginary $i$, $\mathrm{Sc}$ the scalar part; the quaternion sesquilinear form is $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ with $\varepsilon=(1,-1,-1,-1)$; the complex sesquilinear form is $\langle\tilde{Q}',\tilde{Q}\rangle_{*}=\sum_{\mu}\bar Q_{\mu}Q'_{\mu}$ with $\|\tilde{Q}\|_E^{2}=\langle\tilde{Q},\tilde{Q}\rangle_{*}$.

## The Three Level Sets

**Theorem (the level sets and their homotopy types).** In the splitting $\tilde{Q}=c+v$ into the centre and vector parts,

$$
\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}=\Bigl\{(c,v):\|c\|_E^{2}=1+\|v\|_E^{2}\Bigr\}\cong S^{1}\times\mathbb{R}^{6},
$$
$$
\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}=\Bigl\{(c,v):\|v\|_E^{2}=1+\|c\|_E^{2}\Bigr\}\cong S^{5}\times\mathbb{R}^{2},
$$
$$
\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}=\{(c,v):\|c\|_E=\|v\|_E\}\cong S^{1}\times S^{5}\times\mathbb{R}_{>0},
$$

all three of real dimension $7$; the first is homotopy equivalent to $S^{1}$, the second to $S^{5}$, the third to $S^{1}\times S^{5}$.

**Proof.** For the first, a pair $(c,v)$ satisfies the equation exactly when $c$ lies on the circle of radius $\sqrt{1+\|v\|_E^{2}}$ in the centre, so the map $(c,v)\mapsto(c/\|c\|_E,\ v)$ identifies the set with $S^{1}\times\mathbb{R}^{6}$: the pair $(v,c/\|c\|_E)$ is free and determines $c$. For the second, in the same way $\|v\|_E=\sqrt{1+\|c\|_E^{2}}>0$, so $v$ is determined by its direction in the five-sphere and by $c$, which is free in $\mathbb{C}$; the set is $S^{5}\times\mathbb{R}^{2}$. For the third, both norms are equal to some $t>0$, and the set is $S^{1}\times S^{5}\times\mathbb{R}_{>0}$ by the two directions and the radius.

**Remark (what is lost and what is kept).** Compared with the Euclidean sphere, the positive level set loses compactness and the sphere: it is the product of a circle with a six-dimensional Euclidean space, a hyperboloid of revolution. All three sets are connected and non-compact, as the signature $(2,6)$ over $\mathbb{R}$ requires, and the negative set has the homotopy type of $S^{5}$ alone because its vector part is forced away from the origin while its scalar part is free.

## The Positive Region and the Ball of Positive Lines

**Definition.** The **positive region** is the open cone $\mathcal{P}=\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}>0\}$, the interior of the Krein cone; the **negative region** is $\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}<0\}$; and a **positive line** is a complex line consisting of positive elements.

**Theorem (the positive region retracts onto a circle).** The positive region is $\{\|c\|_E>\|v\|_E\}$, it is a cone, and it is homotopy equivalent to $S^{1}$; the negative region is homotopy equivalent to $S^{5}$.

**Proof.** For the first, the map $\tilde{Q}\mapsto c/\|c\|_E$ is defined on the positive region, since $\|c\|_E>\|v\|_E\ge0$ forces $c\neq0$; for fixed $c$ the vector part ranges over the open ball of radius $\|c\|_E$, a contractible set, so the projection onto $\mathbb{C}\setminus\{0\}\simeq S^{1}$ is a homotopy equivalence. For the second, $\|v\|_E>\|c\|_E$ forces $v\neq0$, and the projection onto $v/\|v\|_E\in S^{5}$ has contractible fibres again.

**Theorem (the positive lines form the complex hyperbolic ball).** The positive lines are exactly the lines $\mathbb{C}(e_0+\tilde{V})$ with $\|\tilde{V}\|_E<1$; the assignment $\tilde{V}\mapsto\mathbb{C}(e_0+\tilde{V})$ is a bijection of the open unit ball of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^{3}$ onto the set of positive lines. That set is therefore a real manifold of dimension $6$, isomorphic as a homogeneous space to

$$
U(1,3)/(U(1)\times U(3)),
$$

the **complex hyperbolic space** $\mathbb{CH}^{3}$, and the isometry group $U(1,3)$ of the quaternion sesquilinear form acts on it transitively with the stabiliser $U(1)\times U(3)$ of a positive line.

**Proof.** A positive line is not contained in $\mathbb{V}_{\mathbb{B}}$, since the form is negative definite there; choosing the unique representative $e_0+\tilde{V}$ and using $\langle e_0+\tilde{V},e_0+\tilde{V}\rangle_{\natural*}=1-\|\tilde{V}\|_E^{2}$ shows that positivity is exactly $\|\tilde{V}\|_E<1$, and the assignment is bijective. The stabiliser of the line $\mathbb{C}e_0$ in $U(1,3)$ consists of the isometries preserving the canonical fundamental decomposition, which is $U(1)\times U(3)$ (*The Krein Isometry Group and Its $J$-Contractions*), whence the homogeneous description; the two realisations agree because both are the symmetric space of the same Cartan pair (*The Krein Cartan Decomposition of the Operator Algebra*).

**Remark (the boundary).** By *The Isotropic Structure of the Krein Form* the closure of the ball adds the isotropic lines, $\|\tilde{V}\|_E=1$, a copy of $S^{5}$: it is the boundary sphere of the complex hyperbolic ball, of real dimension $5$, while the ball itself has real dimension $6$.

## The Scaling and the Phase Action

**Theorem (the level sets as orbits).** The phase circle $S^{1}$ acts on $\mathbb{B}$ by $\tilde{Q}\mapsto\lambda\tilde{Q}$, $|\lambda|=1$, preserving the quaternion sesquilinear form and each level set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=t\}$, $t\in\mathbb{R}$. The action is free on $\mathbb{B}\setminus\{0\}$, and its quotient on the positive level set is the complex hyperbolic space $\mathbb{CH}^{3}$ of positive lines; more generally the scaling by $s>0$ relates the level sets $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=t\}$ and $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=s^{2}t\}$, so the positive region is the union of the positive levels over $t>0$. The positive level set is therefore a principal $S^{1}$-bundle over $\mathbb{CH}^{3}\cong\mathbb{R}^{6}$, and it is diffeomorphic to $S^{1}\times\mathbb{R}^{6}$.

**Proof.** $|\lambda|^{2}=1$ makes the value invariant, so the phase preserves every level set; the action is free because $\lambda\tilde{Q}=\tilde{Q}$ with $\tilde{Q}\neq0$ forces $\lambda=1$. The quotient of the positive level set by the phase circle is the set of positive lines, which is $\mathbb{CH}^{3}$ by §*The Positive Region and the Ball of Positive Lines*; the bundle is trivial because the projection onto the direction of $c$ is a section up to homotopy, and $S^{1}\times\mathbb{R}^{6}$ is the diffeomorphism of §*The Three Level Sets*. Real scaling acts by $t\mapsto s^{2}t$ because $\langle s\tilde{Q},s\tilde{Q}\rangle_{\natural*}=s^{2}\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}$ for real $s>0$.

## The Metric of the Ball and Its Geodesics

**Theorem (the Bergman metric).** The ball $\mathbb{B}^{3}\subset\mathbb{V}_{\mathbb{B}}=\mathbb{C}^{3}$ carries the **Bergman metric**

$$
ds^{2}=\frac{(1-\|\tilde{V}\|_E^{2})\,\|d\tilde{V}\|_E^{2}+\lvert\langle d\tilde{V},\tilde{V}\rangle_{*}\rvert^{2}}{(1-\|\tilde{V}\|_E^{2})^{2}},
$$

which is Kähler, complete, of constant negative holomorphic sectional curvature, and invariant under the isometries of the form acting on the ball; the boundary $S^{5}$ is at infinite distance.

**Proof.** The metric is the Bergman metric of the unit ball of $\mathbb{C}^{3}$, invariant under the biholomorphisms of the ball, and the isometry group of the quaternion sesquilinear form is the group of these biholomorphisms (*The Krein Isometry Group and Its $J$-Contractions*); completeness and the constant curvature are the standard properties of the ball, and the boundary is at infinite distance because the metric blows up at $\|\tilde{V}\|_E=1$.

**Theorem (the complex geodesics).** The intersection of the ball with a complex line is a copy of the unit disc, totally geodesic in $\mathbb{CH}^{3}$ and isometric to $\mathbb{CH}^{1}$; the geodesic through the origin and a point $\tilde{V}\neq0$ is the disc $\{z\,\tilde{V}/\|\tilde{V}\|_E:|z|<1\}$. The real geodesics are the curves that solve the geodesic equation; the complex ones are the images of these discs under $U(1,3)$.

**Proof.** A complex line $\mathbb{C}w$ meets the ball in the disc $\{z\,w/\|w\|_E:|z|<1\}$, which contains $0$ and the boundary point $w/\|w\|_E$; the restriction of the Bergman metric to a complex line is a multiple of the Poincaré metric of the disc, so the disc is totally geodesic, and every complex line is the image of $\mathbb{C}\tilde{V}$ under an isometry because $U(1,3)$ is transitive on the complex lines that carry positive vectors.

**Theorem (the totally real slices).** The Minkowski slice $\mathbb{H}_{\mathbb{B}}$ meets the ball in the real unit ball of $\mathbb{R}^{3}$, and the Bergman metric restricts to the Poincaré metric of the real hyperbolic space $H^{3}$; the slice is totally geodesic and totally real in $\mathbb{CH}^{3}$.

**Proof.** On the slice the form is the interval form, and the ball $\{\|\tilde{V}\|_E<1\}$ meets $\mathbb{R}^{3}$ in the real unit ball, on which the Bergman metric is the hyperbolic metric of the disc model; a real subspace of maximal dimension on which the form is real is totally real, and the standard totally geodesic submanifolds of $\mathbb{CH}^{3}$ are the complex lines and the real hyperbolic spaces.

## The Minkowski Slices

**Theorem (the real hyperboloids).** On the Hermitian subspace $\mathbb{M}_{+}$ and on the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the quaternion sesquilinear form is the interval form of Minkowski space, and with the real coordinates $q$,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=q_0^{2}-q_1^{2}-q_2^{2}-q_3^{2}.
$$

The positive level set is the two-sheeted hyperboloid, whose sheet $q_0>0$ is given by $q_0=\sqrt{1+\|\mathbf{q}\|^{2}}$ with $\mathbf{q}\in\mathbb{R}^{3}$ free, hence is $\mathbb{R}^{3}$; the negative level set is the one-sheeted hyperboloid $q_0^{2}=\|\mathbf{q}\|^{2}-1$, diffeomorphic to $S^{2}\times\mathbb{R}$; and the null set is the light cone, of two nappes.

**Proof.** The restricted form is $\sum_{\mu}\varepsilon_{\mu}q_{\mu}^{2}$ in the four real coordinates of the slice (*The Krein Gram Matrix and the Restrictions of the Form*). Solving $q_0^{2}-\|\mathbf{q}\|^{2}=1$ for $q_0$ gives the two sheets, each parametrised by $\mathbf{q}\in\mathbb{R}^{3}$. Solving $q_0^{2}-\|\mathbf{q}\|^{2}=-1$ gives $\|\mathbf{q}\|\ge1$ with $q_0$ free, so the set is $\mathbb{R}\times S^{2}$ by the direction of $\mathbf{q}$. The null equation factors as $(q_0-\|\mathbf{q}\|)(q_0+\|\mathbf{q}\|)=0$, giving the two nappes of the light cone.

**Corollary (the hyperboloid model of $H^{3}$).** The sheet $q_0=\sqrt{1+\|\mathbf{q}\|^{2}} $ carries the Riemannian metric induced by the Lorentz form and is the **hyperboloid model of the real hyperbolic space** $H^{3}$; the Lorentz boosts of *Biquaternion Rotations and Lorentz Transformations* act on it by its isometries. The complex hyperbolic ball of the preceding section is the complexification of this picture: dimension $6$ instead of $3$, the sphere $S^{5}$ instead of $S^{2}$, and the group $U(1,3)$ instead of the Lorentz group.

## The Krein Cone and the Level Sets

**Definition.** The **Krein cone** is
$$
P_K=\bigl\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}\ge0\bigr\}
=\bigl\{\tilde{Q}:\|c\|_E\ge\|v\|_E\bigr\},
$$
the closed cone of *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*.

**Theorem (the cone, its interior and its boundary).** The Krein cone is the union of the origin, the positive region and the null set; its interior is the positive region $\{\|c\|_E>\|v\|_E\}$, its boundary is the null set, and it contains the whole positive axis and no negative element. On a Minkowski slice its intersection is the full light cone, whose future nappe is the Hermitian cone $P$ of the slice.

**Proof.** The sign of an element is the sign of $\|c\|_E^{2}-\|v\|_E^{2}$ (*The Biquaternion Krein Form and Its Signature*), so the cone is exactly the set displayed, with interior the strict inequality and boundary the equality; on the slice the same form is the interval form, and the inequality $\|c\|_E\ge\|v\|_E$ becomes the light-cone condition.

**Remark (the level sets inside the cone).** The unit positive level set $\{\langle\tilde Q,\tilde Q\rangle_{\natural*}=1\}$ is a hyperboloid sheet inside the interior of $P_K$, the negative level set lies outside, and the null set is the boundary; the cone is the union of the positive level sets of all $t\ge0$, rescaled to $t=1$ by the real scaling of §*The Scaling and the Phase Action*.

## The Norm Hypersurfaces

**Theorem (the levels of the norm).** For $\lambda\neq0$ the level set $\{N(\tilde Q)=\lambda\}$ of the norm $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}$ is a complex hypersurface of $\mathbb{B}=\mathbb{C}^{4}$, of real dimension $6$, invariant under $\tilde Q\mapsto\pm\tilde Q$; the zero set $\{N=0\}$ is a complex cone, the zero-divisor cone of *Biquaternion Topology*. The level sets of the quaternion sesquilinear form are, by contrast, the real hypersurfaces of real dimension $7$ that this article describes.

**Proof.** $N$ is a complex polynomial of degree two, so a nonzero level is a complex hypersurface and the zero set is a cone; the quaternion sesquilinear form is real on the diagonal and its defining polynomial $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$ is not holomorphic, so its levels are real hypersurfaces — the same distinction as in *The Biquaternion Krein Form and Its Signature*.

**Corollary (the two pairings and the two geometries).** The two pairings of the algebra give two families of level sets: the complex hypersurfaces of the norm, whose geometry is the projective geometry of the zero-divisor cone, and the real hyperboloids of the quaternion sesquilinear form, whose geometry is the hyperbolic geometry of the ball. Their intersection is treated in *The Isotropic Structure of the Krein Form*, where it is the union of the doubly null lines.

## The Definite Companion and the Twisted Sphere

**Definition.** The **definite companion** of the quaternion sesquilinear form is the positive definite Hermitian form $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu|Q_\mu|^{2}=\|\tilde{Q}\|_E^{2}$ of *The Hermitian Form on the Biquaternion Algebra*.

**Theorem (the definite levels are spheres).** The level sets of the definite companion are the Euclidean spheres $\{\|\tilde{Q}\|_E=r\}$, of real dimension $7$ and compact; the unit sphere $S^{7}$ is the boundary of the Euclidean unit ball, the only compact member of the comparison table of §*The Level Sets Compared*, and the definite form is complete and positive definite.

**Proof.** In the coefficient basis the definite form is the standard Hermitian form of $\mathbb{C}^{4}$, so its levels are spheres; compactness and completeness are those of the Euclidean norm.

**Theorem (the indefinite levels as a twisted sphere).** The bridge $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\langle\tilde{Q},J\tilde{Q}\rangle_{*}$ of *The Fundamental Symmetry of the Biquaternion Algebra* writes the indefinite level set of level $t$ as the set of $\tilde{Q}$ with $\langle\tilde{Q},J\tilde{Q}\rangle_{*}=t$: it is the Euclidean sphere twisted by the involution $J={}^{\natural}$, and it is diffeomorphic to $S^{1}\times\mathbb{R}^{6}$ for $t>0$ and to $S^{5}\times\mathbb{R}^{2}$ for $t<0$, with the null set $t=0$ as their common boundary.

**Proof.** The bridge is the identity of the fundamental-symmetry article, and the three diffeomorphism types are those of §*The Three Level Sets*; the twist by $J$ replaces the positive definite form by the indefinite one, which is the only change from the sphere.

## The Level Sets Compared

| level set | equation in $(c,v)$ | diffeomorphism | homotopy type | compactness |
|---|---|---|---|---|
| positive | $\lVert c\rVert_E^{2}=1+\lVert v\rVert_E^{2}$ | $S^{1}\times\mathbb{R}^{6}$ | $S^{1}$ | no |
| negative | $\lVert v\rVert_E^{2}=1+\lVert c\rVert_E^{2}$ | $S^{5}\times\mathbb{R}^{2}$ | $S^{5}$ | no |
| null | $\lVert c\rVert_E=\lVert v\rVert_E$ | $S^{1}\times S^{5}\times\mathbb{R}_{>0}$ | $S^{1}\times S^{5}$ | no |
| Euclidean sphere | $\lVert c\rVert_E^{2}+\lVert v\rVert_E^{2}=1$ | $S^{7}$ | $S^{7}$ | yes |

**Remark.** The last row belongs to the definite complex sesquilinear form and is quoted for contrast: it is the sphere of *The Euclidean Topology of the Biquaternion Algebra*, the only compact member of the table, and the reason the indefinite level sets carry hyperbolic rather than elliptic geometry.

## Worked Examples

**A point of the positive level set.** $\tilde{Q}=e_0$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1$, on the positive set, the base point of the ball.

**A point of the negative level set.** $\tilde{Q}=e_1+e_2$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-2$, so $\tilde{Q}/\sqrt2$ has square $-1$.

**Two points of the null set.** $e_0+e_1$ and $(e_0+e_1)/\sqrt2$: the first has square $0$ and norm $2$, the second square $0$ and Euclidean norm $1$; the second is on the link, and both are on the boundary of the ball.

**A line inside the ball.** $\mathbb{C}(e_0+\tfrac12e_1)$: $\|\tilde{V}\|_E=\tfrac12<1$, a positive line, a point of the complex hyperbolic ball.

**A line on the boundary.** $\mathbb{C}(e_0+e_1)$: $\|\tilde{V}\|_E=1$, an isotropic line, a point of the boundary sphere $S^{5}$.

**A real timelike line.** $\tilde{Q}=e_0+\tfrac12e_1$ in $\mathbb{H}_{\mathbb{B}}$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\tfrac34>0$, a point of the Minkowski hyperboloid sheet.

**A point of a higher positive level.** $\tilde{Q}=2e_0$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=4$, in the interior of the Krein cone, on the level $t=4$; the real scaling by $s=2$ carries $e_0$ to it.

**The antipode.** $\tilde{Q}=-e_0$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1$, the same positive level as $e_0$; the two are the same positive line, and the phase by $-1$ identifies them.

**A negative element and the cone.** $\tilde{Q}=e_1$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1<0$, so it lies outside the Krein cone, on the negative level set.

**A phase orbit.** $e_0$ and $ie_0$: both on the unit positive level set, both positive, the same positive line; the phase circle acts on the level set and the orbit is the fibre of the bundle over $\mathbb{CH}^{3}$.

**A nonzero norm level.** $\{N(\tilde{Q})=1\}$ is a complex hypersurface of real dimension $6$ through the four units $e_0,e_1,e_2,e_3$, each with $N=1$; it is not a real hyperboloid, and its real points include the sphere $\sum_\mu q_\mu^{2}=1$ of the real slice.

## Summary

The sign level sets of the quaternion sesquilinear form are the hyperboloids $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}\cong S^{1}\times\mathbb{R}^{6}\simeq S^{1}$ and $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}\cong S^{5}\times\mathbb{R}^{2}\simeq S^{5}$, and the null set $S^{1}\times S^{5}\times\mathbb{R}_{>0}\simeq S^{1}\times S^{5}$; all are non-compact of real dimension $7$, in contrast with the compact Euclidean sphere $S^{7}$. The positive region $\{\|c\|_E>\|v\|_E\}$ retracts onto the circle of phases and the negative region onto $S^{5}$. The positive lines are the lines $\mathbb{C}(e_0+\tilde{V})$ with $\|\tilde{V}\|_E<1$, so they form the open unit ball of $\mathbb{C}^{3}$, of real dimension $6$, which is the complex hyperbolic space $\mathbb{CH}^{3}=U(1,3)/(U(1)\times U(3))$ with boundary the isotropic sphere $S^{5}$. On a Minkowski slice the same picture degenerates to the sheet $q_0=\sqrt{1+\|\mathbf{q}\|^{2}}$ of the real hyperboloid, the hyperboloid model of the real hyperbolic space $H^{3}$, the one-sheeted hyperboloid $S^{2}\times\mathbb{R}$, and the two nappes of the light cone. The phase circle acts freely on the positive level set with quotient $\mathbb{CH}^{3}$, and real scaling relates the positive levels; the ball carries the Bergman metric, complete and of constant negative holomorphic curvature, whose complex geodesics are the intersections with the complex lines and whose totally geodesic real slices are the Minkowski hyperboloids. The Krein cone is the union of the non-negative levels, its interior the positive region and its boundary the null set; the norm's nonzero levels, by contrast, are complex hypersurfaces of real dimension $6$, and only its zero set is a cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}\cong S^{1}\times\mathbb{R}^{6}$ | The positive level set; $\simeq S^{1}$ |
| $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1\}\cong S^{5}\times\mathbb{R}^{2}$ | The negative level set; $\simeq S^{5}$ |
| $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}\cong S^{1}\times S^{5}\times\mathbb{R}_{>0}$ | The null set |
| $\mathcal{P}=\{\lVert c\rVert_E>\lVert v\rVert_E\}$ | The positive region; $\simeq S^{1}$ |
| $\mathbb{C}(e_0+\tilde V)$, $\lVert\tilde V\rVert_E<1$ | The positive lines; the ball of $\mathbb{C}^{3}$ |
| $\mathbb{CH}^{3}=U(1,3)/(U(1)\times U(3))$ | The complex hyperbolic space of positive lines |
| $q_0^{2}-\lVert\mathbf{q}\rVert^{2}=\pm1$ | The real hyperboloids in a Minkowski slice |
| $q_0=\sqrt{1+\lVert\mathbf{q}\rVert^{2}}$ | The hyperboloid model of $H^{3}$ |
| $S^{1}$ phase and $\mathbb{R}_{>0}$ scaling | The actions on the level sets; the positive level is an $S^{1}$-bundle over $\mathbb{CH}^{3}$ |
| $ds^{2}$ of §*The Metric of the Ball and Its Geodesics* | The Bergman metric of the ball; complete, constant negative curvature |
| $P_K=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}\ge0\}$ | The Krein cone: origin, positive region, null set |
| $\{N(\tilde{Q})=\lambda\}$, $\lambda\neq0$ | The norm hypersurfaces; complex, real dimension $6$ |
| $\{\lVert\tilde{Q}\rVert_E=r\}$, $\langle\tilde{Q},J\tilde{Q}\rangle_{*}=t$ | The definite spheres and their $J$-twist |

## Further Reading

- *The Isotropic Structure of the Krein Form* (`articles_maths/the-isotropic-structure-of-the-krein-form.md`), for the boundary sphere and the null cone
- *Krein Orthogonality and the Fundamental Decomposition* (`articles_maths/krein-orthogonality-and-the-fundamental-decomposition.md`), for the parametrisation of the maximal positive definite subspaces
- *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* (`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.md`), for the cone and its interior
- *The Krein Cartan Decomposition of the Operator Algebra* (`articles_maths/the-krein-cartan-decomposition-of-the-operator-algebra.md`), for the symmetric space $U(1,3)/(U(1)\times U(3))$
- *Biquaternion Rotations and Lorentz Transformations* (`articles_maths/biquaternion-rotations-and-lorentz-transformations.md`), for the boosts acting on the Minkowski hyperboloid
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the compact sphere used here for contrast
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the definite companion and its spheres
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the bridge $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\langle\tilde{Q},J\tilde{Q}\rangle_{*}$
