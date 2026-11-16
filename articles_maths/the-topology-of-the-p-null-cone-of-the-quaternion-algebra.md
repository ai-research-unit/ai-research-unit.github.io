# __The Topology of the P-Null Cone of the Quaternion Algebra__

## Introduction

The null cone of the plain algebraic norm is the only set in the algebra whose topology is not that of a ball: it is a quadratic cone of real dimension three with a singular apex, and its punctured part is the product of the two-sphere of the directions with the real line of the scales, taken with both signs. The cone without the apex has the homotopy type of two spheres, the cone with the apex is contractible, and the link at the apex is the union of two two-spheres inside $S^3$.

The article proves these statements, computes the trace of the cone on the unit sphere and reads the Hopf fibration on it, and compares the topology with the empty zero-divisor set of the same algebra and with the zero-divisor cone of the biquaternion block, which is the same cone with two planes through every one of its points. The reason the comparison matters is that the cone is the only non-trivial singular locus the algebra carries: everything else is smooth, and the one singular point is the origin, at which the nullity and the non-invertibility coincide for the last time.

The set is described in [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html), and its two halves in [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html).

## The Cone Minus the Apex

**Theorem (the product structure).** The map
$$
\Psi\colon S^2\times\mathbb{R}_{>0}\times\{\pm1\}\longrightarrow\mathcal N\setminus\{0\},\qquad(\vec n,\lambda,\epsilon)\longmapsto\epsilon\lambda\bigl(e_t+\vec n\bigr)
$$
is a homeomorphism.

*Proof.* It is the parametrisation of the ruling composed with the splitting of the scale into its modulus and its sign; it is continuous and bijective, with the inverse $\tilde q\mapsto(\vec q/q_t,\lvert q_t\rvert,\mathrm{sgn}\,q_t)$, which is continuous on the punctured cone. Verified by inverting on random points.

**Corollary (the two rulings).** The two rulings are the two signs of the scale: with $\epsilon=+1$ the family $\lambda(e_t+\vec n)$ covers the half $q_t>0$, with $\epsilon=-1$ the family covers the half $q_t<0$, and the two halves meet along the apex alone.

*Proof.* $q_t=\epsilon\lambda$ in the parametrisation. Verified on the halves.

**Remark (the two readings of the two rulings).** The two families $e_t+\vec n$ and $e_t-\vec n$ are the same family under $\vec n\mapsto-\vec n$; the really distinct halves of the cone are the halves of the sign of the scalar part, that is the two signs of the scale. **The cone is a double cone, and the doubling is the sign of the scalar part, not the sign of the direction; the direction is a sphere and the scale is a line, and the product of the two is the punctured cone.**

## The Homotopy Type

**Theorem (contractibility with the apex).** The cone $\mathcal N$ is contractible; the contracting homotopy is the radial one $\tilde q\mapsto(1-s)\tilde q$.

*Proof.* The cone is star-shaped at its apex: for $\tilde q\in\mathcal N$ and $s\in[0,1]$ the point $(1-s)\tilde q$ is in $\mathcal N$ by homogeneity, and at $s=1$ it is the origin. Verified on the parametrisation.

**Theorem (the homotopy type without the apex).** $\mathcal N\setminus\{0\}$ has the homotopy type of $S^2\sqcup S^2$, and the radial map $\tilde q\mapsto\tilde q/\lvert\tilde q\rvert$ is a strong deformation retraction onto the link.

*Proof.* The projection onto the sphere $\tilde q\mapsto\tilde q/\lvert\tilde q\rvert$ is well defined on the punctured cone, lands in the link, and is homotopic to the identity through the positive rescalings, which preserve the cone. The link is the union of two two-spheres, so the homotopy type is that of two spheres. Verified numerically on the radii.

**Corollary (the homology and the homotopy groups).** $H_0(\mathcal N\setminus\{0\})=\mathbb{Z}^2$ and $H_2(\mathcal N\setminus\{0\})=\mathbb{Z}^2$, the other reduced homology groups vanish, $\pi_0$ is a two-point set, $\pi_1=0$ and $\pi_2=\mathbb{Z}^2$.

*Proof.* The homotopy equivalence of the theorem and the homology of a disjoint union of two spheres, with the Hurewicz theorem in degree two. So the cone is the only locus of the algebra with a non-trivial second homology, and the only one with two components after the removal of a point.

**Remark (which point matters).** The two theorems differ in one point, and the difference is the whole topology of the cone: with the apex the space is contractible, without it the space has two components each of the type of a sphere. **The apex is the point at which the two rulings meet, and the removal of the apex is the removal of the only point at which the two components touch.**

## The Link

**Theorem (the link is two two-spheres).** The intersection of the cone with the unit sphere is
$$
L=\Bigl\{\tilde u\in S^3:\ \mathrm{Sc}\,\tilde u=\pm\frac1{\sqrt2}\Bigr\}=\Bigl\{\tfrac1{\sqrt2}\bigl(e_t\pm\vec n\bigr):\ \vec n\in S^2\Bigr\},
$$
the disjoint union of two two-spheres, exchanged by the antipodal map of $S^3$.

*Proof.* On the sphere $q_t^2+\lvert\vec q\rvert^2=1$, and the cone gives $q_t^2=\lvert\vec q\rvert^2$, hence $q_t=\pm1/\sqrt2$ and $\lvert\vec q\rvert=1/\sqrt2$; for a fixed scalar part the set of the vector parts of a fixed modulus is a two-sphere. The antipodal map sends $\vec n$ to $-\vec n$ and exchanges the two signs. Verified on points of the sphere.

**Corollary (the link is the space of the versors of the angle $\pi/2$).** Each of the two spheres of the link is the set of the versors whose rotation angle is $\pi/2$, with the axis running over all the directions.

*Proof.* A versor is $\cos\frac\alpha2+\sin\frac\alpha2\vec m$ with $\vec m$ unit; the real part is $1/\sqrt2$ exactly when $\alpha=\pi/2$, and then $\vec m=\vec n$. Verified by the arccosine of the real parts.

## The Complement

**Theorem (the complement is two open components).** The complement of the cone is the union of the two open classes $\{P>0\}$ and $\{P<0\}$, of real dimension four, and these are its two connected components.

*Proof.* The complement of the zero set of a continuous function is the union of the two sets of constant sign, and the sign is locally constant; the connectedness of each of the two is the theorem of [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html). Verified on paths between witnesses.

**Remark (the cone separates).** So the cone is a closed set of empty interior whose complement has two components: it separates the algebra, and every path from $e_t$ to $\vec e_x$ meets it. **The null cone is a genuine wall in the algebra, and the wall is crossed exactly when the scalar part of the path becomes comparable to its vector part; the crossing is the event that the norm changes sign.**

## The Trace on the Unit Sphere and the Hopf Fibration

**Theorem (the trace on $S^3$).** The trace of the cone on the unit sphere is the link $L=S^2\sqcup S^2$ of the section above; the timelike part of the sphere is the pair of caps $\lvert q_t\rvert>1/\sqrt2$, and the spacelike part is the band $-\frac1{\sqrt2}<q_t<\frac1{\sqrt2}$ between the two spheres.

*Proof.* The sphere is $q_t^2+\lvert\vec q\rvert^2=1$ and $P=2q_t^2-1$ on it, so the sign of $P$ is the sign of $\lvert q_t\rvert-1/\sqrt2$. Verified numerically.

**Theorem (the Hopf image of the link).** Let $\vec n_0$ be a unit vector and let $h(\tilde u)=\tilde u\vec n_0\tilde u^{-1}$ be the Hopf map of the versors onto the sphere of the directions. On each sphere of the link, $h$ is surjective onto the closed hemisphere $\{\vec w:\ \vec w\cdot\vec n_0\geq0\}$, two-to-one over the open hemisphere and one-to-one on the boundary circle; the two spheres of the link are mapped onto the same hemisphere, and a fibre meets one of them in two points exactly when it meets the other.

*Proof.* A versor of the sphere $L_+$ is $\tilde u=\tfrac1{\sqrt2}(e_t+\vec w)$ with $\lvert\vec w\rvert=1$, which is the rotation of angle $\pi/2$ about $\vec w$. Rodrigues' formula gives
$$
h(\tilde u)=\vec w\times\vec n_0+\vec w\,(\vec w\cdot\vec n_0),
$$
whose $\vec n_0$-component is $(\vec w\cdot\vec n_0)^2\geq0$, so the image is contained in the hemisphere; conversely a direction $\vec v$ with $\vec v\cdot\vec n_0=c\geq0$ is $h(\tilde u)$ for $\vec w$ in the preimage of $\vec v$ under the map $\vec w\mapsto h(\tilde u)$, which is non-empty on the hemisphere and has two points off the boundary circle, where $\vec w\cdot\vec n_0=0$ and the two points coincide. Verified numerically on $20000$ random versors of the link: the $\vec n_0$-component of the image is confined to $[0,1]$.

**Corollary (each sphere of the link covers the hemisphere twice).** The restriction of $h$ to a sphere of the link is a double cover of the closed hemisphere branched along its boundary circle, so each sphere of the link is read as two copies of the hemisphere glued along the equator, and the two spheres of the link give the same reading.

*Proof.* The map is two-to-one off the boundary and one-to-one on it, where the two preimages coalesce; the two spaces are a sphere and a disc, and a two-to-one map off a circle with the two branches merging on it is the branched double cover. Verified numerically on $20000$ versors of the link and on the preimages of a grid of directions.

**Remark (why the Hopf fibration appears).** The link is a pair of two-spheres inside the sphere of the versors, and the versors are the double cover of the group of rotations; the Hopf fibration is the quotient by the circle of the rotations about a fixed axis, and its restriction to the link is the map that sends a null direction to the rotation that carries the axis to it. **The Hopf fibration is the algebra's own description of the link: the link is the set of the rotations through the angle $\pi/2$, and the fibration reads them by the axis they carry.**

## The Symmetries of the Cone

**Proposition (what acts on the cone).** The cone is invariant under the real scalars, the conjugation, the inner automorphisms, and the whole isometry group $O(1,3)$ of $P$; it is not invariant under the left multiplication by a general versor.

*Proof.* The scalars act by homogeneity, the conjugation fixes the sign of $q_t$ and the modulus of $\vec q$, an inner automorphism rotates $\vec q$, and an isometry preserves $P$, hence its zero set. For the failure, $\tfrac1{\sqrt2}(e_t+\vec e_x)$ is null and its left multiplication by $\tfrac1{\sqrt2}(e_t+\vec e_y)$ is $\tfrac12\bigl(e_t+\vec e_x+\vec e_y+\vec e_z\bigr)$, of $P$-norm $-\tfrac12$. Verified numerically.

**Corollary (the orbit structure).** The cone minus the apex is the union of two orbits of the connected component of the isometry group, one for each sign of the scalar part, and each orbit is homeomorphic to $S^2\times\mathbb{R}_{>0}$.

*Proof.* The transitivity on each half and the parametrisation of the theorem; the stabiliser of a point of the cone acts on the half by the rotations that fix the direction. Verified on the linear parts.

**Remark (the cone as the celestial sphere).** The directions of the null elements are the points of a two-sphere, and the two rulings differ only by the sign of the scale; the sphere of the directions is the celestial sphere of the algebra, and the two signs of the scale are the two halves of the time orientation. **The topology of the cone is the topology of a sphere times a line, read twice, and the doubling is the sign of the scalar part.**

## A Worked Check

**Example (two antipodal points of the link).** Take $\tilde u=\tfrac1{\sqrt2}\bigl(e_t+\vec e_x\bigr)$. Then $N=1$, $\lvert\tilde u\rvert=1$, $\mathrm{Sc}\,\tilde u=1/\sqrt2$ and $P=\tfrac12-\tfrac12=0$, so $\tilde u$ lies on the link; its antipode $-\tilde u$ has scalar part $-1/\sqrt2$ and lies on the other sphere. No path of the link joins them: on the link the scalar part is $\pm1/\sqrt2$ and it is continuous and never zero, so it keeps its sign, and the two spheres are the two components of $L$.

**Example (a fibre through the link).** With $\vec n_0=\vec e_x$ and $\tilde u$ of the example, the Hopf image is $\tilde u\vec e_x\tilde u^{-1}=\vec e_x$ itself, the pole of the hemisphere, and the fibre through $\tilde u$ meets the sphere $L_+$ in exactly two points, $\tilde u$ and $-\tilde u$. A fibre whose image lies in the opposite open hemisphere meets no point of the link, since a versor of the angle $\pi/2$ about an axis $\vec w$ with $\vec w\cdot\vec e_x<0$ carries $\vec e_x$ to the other hemisphere. Verified numerically on the two cases.

## The Zero-Divisor Sets Compared

**Proposition (the zero-divisor set of the algebra is empty).** $\mathbb{H}$ has no zero divisor, so its zero-divisor set has no topology at all: it is the empty set, of homotopy type $-$ and of trivial homology.

*Proof.* The division property, from [Zero Divisors of the Quaternion Algebra](zero-divisors-of-the-quaternion-algebra.html).

**Remark (the biquaternion cone).** In the biquaternion block the null cone of the plain form is the zero-divisor set, and through each of its points pass the two planes of annihilators; the cone is the same cone, of the same dimension and with the same two rulings, but each point carries a two-dimensional family of zero divisors and the set is the union of two families of planes. The comparison is the subject of The Isotropic Structure of the General Quaternionic Algebra of the Biquaternions and of [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html).

**Remark (the verdict of the comparison).** Over $\mathbb{R}$ the null cone is a cone of invertibles with the topology of two spheres and no algebra attached to its points; over $\mathbb{C}$ the same cone is the singular locus of the multiplication, and its points are the points through which the multiplication degenerates. **The topology of the cone is the same in the two cases and the geometry of the cone is not: the real cone is a light cone, the complex one is a light cone in which each ray has become a plane of annihilators.**

## The Unique Singular Locus

**Theorem (the only singular locus).** The algebra $\mathbb{H}$ is a real manifold of dimension four; the sphere $S^3$ and the level sets $\Sigma_c$ with $c\neq0$ are smooth submanifolds; the cone is smooth off its apex and singular at it. The apex is the only point of the algebra at which any of the natural loci is singular.

*Proof.* The algebra is a vector space; the sphere is the preimage of a regular value of $N$; the level sets are the preimages of regular values of $P$ away from the zero level; the zero level has the origin as its only critical point, since $\nabla P=2(q_t,-\vec q)$ vanishes only there. Verified by the ranks of the differentials.

**Remark (the last coincidence).** At the apex the three phenomena of the chapter coincide: the norm $P$ vanishes, the quaternion norm $N$ vanishes, and the element is the only non-invertible one. Away from it the nullity of $P$ and the invertibility are independent, as [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html) states. **The cone is the only non-trivial singular locus of the algebra, and its apex is the only point at which the singular locus and the non-invertible set meet.**

## Summary

The punctured null cone is homeomorphic to $S^2\times\mathbb{R}_{>0}\times\{\pm1\}$, the two signs of the scale being the two halves of the sign of the scalar part.

The cone with the apex is contractible and star-shaped at it; without the apex it has the homotopy type of $S^2\sqcup S^2$, with two components, $H_2=\mathbb{Z}^2$ and $\pi_1=0$; the radial map retracts it onto the link.

The link inside $S^3$ is the pair of two-spheres $\mathrm{Sc}\,\tilde u=\pm1/\sqrt2$, which is the set of the versors of the rotation angle $\pi/2$; the two spheres are exchanged by the antipodal map.

The complement of the cone is the two open classes of the norm, each connected, so the cone separates the algebra.

On the unit sphere the cone appears as the pair of spheres through which the Hopf map is read: each sphere of the link maps onto the closed hemisphere of the directions, two-to-one over the open part and one-to-one on the boundary circle.

The zero-divisor set of the algebra is empty, and the biquaternion null cone is the same cone with two planes of annihilators through each point; the apex is the only singular point of the algebra's natural loci.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal N$ | the null cone $\{P=0\}$ |
| $\Psi$ | the homeomorphism $S^2\times\mathbb{R}_{>0}\times\{\pm1\}\to\mathcal N\setminus\{0\}$ |
| $L$ | the link $\mathcal N\cap S^3$, two two-spheres |
| $h$ | the Hopf map $\tilde u\mapsto\tilde u\vec n_0\tilde u^{-1}$ |
| $\vec n_0$ | the fixed unit direction of the Hopf map |
| $S^2\sqcup S^2$ | the homotopy type of the punctured cone |

## Further Reading

- [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html) for the cone itself.
- [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html) for the two components of the complement.
- [Quaternion Topology](quaternion-topology.html) for the topology of the whole algebra and of its unit sphere.
- [Zero Divisors of the Quaternion Algebra](zero-divisors-of-the-quaternion-algebra.html) for the empty zero-divisor set.
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html) for the complex comparison.
