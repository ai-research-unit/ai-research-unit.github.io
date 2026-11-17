# __The P-Regular Sector of the Quaternion Algebra__

## Introduction

The set on which the plain algebraic norm does not vanish,
$$
\{P\neq0\}=\{q_t^2\neq\lvert\vec q\rvert^2\},
$$
is the complement of the null cone. It is open, dense, of full measure, and it falls into exactly two connected components, the timelike one and the spacelike one, of real dimension four. Each component carries the hyperbolic reading of its own sign, the level sets $P=\pm1$ are the two hyperboloids, and the trivial radial retraction carries the sector onto the two of them.

The article proves the two-component statement from the convexity of the two kinds of cone, gives the hyperbolic reading and the action of the isometry group, and compares the sector with the N-regular sector, which is the complement of a point. The partition itself is stated in [The P-Norm Partition of the Quaternion Algebra](the-p-norm-partition-of-the-quaternion-algebra.html); the cone that is its complement is [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html).

## The Two Components

**Theorem (the decomposition).** Put
$$
\mathcal T^+=\{q_t>\lvert\vec q\rvert\},\qquad \mathcal T^-=\{q_t<-\lvert\vec q\rvert\},\qquad \mathcal S=\{P<0\}.
$$
Then
$$
\{P\neq0\}=\mathcal T^+\uplus\mathcal T^-\uplus\mathcal S,
$$
the three sets are open and non-empty, $\mathcal T^+$ and $\mathcal T^-$ are convex, $\mathcal S$ is connected, and the sector has exactly two components, $\mathcal T=\mathcal T^+\cup\mathcal T^-$ and $\mathcal S$.

*Proof.* $P>0$ is $q_t^2>\lvert\vec q\rvert^2$, which splits into the two alternatives $q_t>\lvert\vec q\rvert$ and $q_t<-\lvert\vec q\rvert$. Each of $\mathcal T^\pm$ is a superlevel set of the concave function $q_t-\lvert\vec q\rvert$, hence convex, hence connected. The function $q_t$ does not vanish on $\mathcal T$, so a path in $\mathcal T$ keeps a constant sign of $q_t$ and cannot join $\mathcal T^+$ to $\mathcal T^-$; the two are the components of $\mathcal T$. For $\mathcal S$: on it $\vec q\neq0$, so $\vec q=s\vec m$ with $s=\lvert\vec q\rvert>0$ and $\vec m\in S^2$, and the condition is $\lvert q_t\rvert<s$; the map $(\vec m,s,q_t)\mapsto s\vec m+q_te_t$ is a homeomorphism of $S^2\times\{(s,q_t):s>\lvert q_t\rvert\}$ onto $\mathcal S$, and the second factor is a convex set, hence connected. Verified on random samples of each set and on paths between the witnesses $e_t$ and $-e_t$, which leave $\mathcal T$ at the origin of the segment.

**Corollary (open, dense, full measure).** The sector is open, its complement is the null cone of empty interior and of Lebesgue measure zero, and the sector is of real dimension four.

*Proof.* Openness is the continuity of $P$; density is the emptiness of the interior of $\{P=0\}$, since a non-zero polynomial cannot vanish on an open set; the measure is zero because the cone is a quadratic hypersurface; the dimension is that of a non-empty open set of $\mathbb{H}$.

**Remark (the shape of the two pieces).** $\mathcal T$ is the union of the two sheets, each convex and homeomorphic to $\mathbb{R}^4$, the positive one being the region $q_t>\lvert\vec q\rvert$ above the graph of $\lvert\vec q\rvert$ over $\mathbb{R}^3$; $\mathcal S$ is a thickening of the sphere $S^2$, of the homotopy type of $S^2$. **The two components of the sector have different topology, and the difference is already visible in the sign: the positive one is a pair of convex cones, the negative one is a tube around the sphere of the directions.**

## The Hyperbolic Reading

**Definition.** On $\mathcal T$ the form $-P$ is positive definite; on $\mathcal S$ the form $P$ is negative definite. The **hyperbolic reading** of $\mathcal T$ is the Riemannian metric $-P$, and the **hyperbolic reading** of $\mathcal S$ is the Riemannian metric $-P$ restricted to it.

*Proof of definiteness.* On $\mathcal T$, $-P=\lvert\vec q\rvert^2-q_t^2>0$; on $\mathcal S$, $P<0$ so $-P>0$; both are quadratic forms positive on their sets, and the radical of $P$ is zero, so the restrictions are Riemannian metrics.

**Remark (the constant curvature).** The ambient form $P$ is flat, of inertia $(1,3)$, and the level sets $P=c$ carry the metrics of constant curvature: the sheet $P=1$, $q_t>0$, is a model of the hyperbolic space $H^3$ of curvature $-1$; the sheet $P=-1$ is a model of the de Sitter space $dS_3$, of inertia $(2,1)$. The two readings are two models of the same ambient form, one elliptic and one hyperbolic in the sense of the sign of the curvature. The details are in [The P Level Sets and the Hyperbolic Structure of the Quaternion Algebra](the-p-level-sets-and-the-hyperbolic-structure-of-the-quaternion-algebra.html).

**Theorem (the level sets and the retraction).** The radial map
$$
\rho(\tilde q)=\frac{\tilde q}{\sqrt{\lvert P(\tilde q)\rvert}}
$$
is a strong deformation retraction of $\mathcal T$ onto the two-sheeted hyperboloid $\{P=1\}$ and of $\mathcal S$ onto the one-sheeted hyperboloid $\{P=-1\}$.

*Proof.* $P(\rho(\tilde q))=\mathrm{sgn}(P(\tilde q))$, so $\rho$ lands on the level set of the sign. The homotopy $\tilde q\mapsto(1-t)\tilde q+t\rho(\tilde q)$ is the positive rescaling by the factor $1-t+t\lvert P\rvert^{-1/2}>0$ of $\tilde q$, which preserves both the sign of $P$ and the component. So the retraction is continuous, fixes the level set, and is homotopic to the identity through maps of the sector into itself. Verified on the four basis elements.

**Corollary (the homotopy types).** $\mathcal T$ has the homotopy type of two points, and $\mathcal S$ that of $S^2$.

*Proof.* By the theorem and the topology of the two hyperboloids: the sheet $P=1,q_t>0$ is contractible, the sheet $P=-1$ is homeomorphic to $\mathbb{R}\times S^2$.

## The Group Acting

**Proposition (the group of the sector).** The isometry group of $P$ is $O(1,3)$; it preserves the sector and its components, acts transitively on each sheet of $P=1$ and on $P=-1$, and the stabiliser of a point of the positive sheet is a copy of $O(3)$.

*Proof.* The isometries of a form of inertia $(1,3)$ form $O(1,3)$; they preserve the level sets of the quadratic form, hence the sector and the sign of $P$ up to the sign of the isometry, and they preserve $q_t$ up to that sign. Transitivity on the positive sheet is the Witt extension theorem applied to the two timelike vectors $e_t$ and a given point of the sheet; the stabiliser of $e_t$ is the group of the vector subspace, that is $O(3)$. Verified on the linear parts of the four sign patterns.

**Corollary (the hyperbolic space as a quotient).** The positive sheet of $P=1$ is $O(1,3)^{+}/O(3)$ up to the two components, that is the hyperbolic space $H^3$ as a homogeneous space.

*Proof.* The transitivity and the stabiliser of the proposition, with the connected component of the identity. The comparison of the two realisations, by the versors and by the boosts, is the subject of [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html).

## The Intersection with the Group of Invertibles

**Theorem (the sector is a subset of the invertibles).** $\{P\neq0\}\subset\mathbb{H}^{\times}$, and every element of the sector is invertible with
$$
N(\tilde q)\geq\lvert P(\tilde q)\rvert>0 .
$$

*Proof.* $P(\tilde q)\neq0$ forces $\tilde q\neq0$, and every non-zero quaternion is invertible by the division property. For the inequality, $N=q_t^2+\lvert\vec q\rvert^2\geq\lvert q_t^2-\lvert\vec q\rvert^2\rvert=\lvert P\rvert$. Verified on random elements.

**Remark (the intersection is the whole sector).** The intersection of the sector with the group of invertibles is the sector itself, so the so-called intersection carries no information. What carries information is the shape of the P-partition inside the group: the group of invertibles is the sector plus the punctured cone, and the cone is the boundary. **The regular sector does not select the invertibles; the invertibles are everything but the origin, and the sector is that same set with a cone removed.** The cone itself lies inside the invertibles, as [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html) proves.

**Theorem (the intersection with the spectral strata).** The real axis minus the origin is contained in $\mathcal T^+$. The non-real quaternions meet both components. The origin is in neither.

*Proof.* On the real axis $P=\lambda^2>0$ and $q_t=\lambda$; a real $\lambda>0$ is in $\mathcal T^+$ and a real $\lambda<0$ in $\mathcal T^-$. The non-real witnesses $e_t+\tfrac12\vec e_x$ and $\vec e_x$ lie in the two components. The origin has $P=0$. Verified numerically. So the sector contains two of the three spectral strata whole and cuts the third in two: **the spectral cut restricts to the sector as the cut of the non-real stratum by the sign of $P$, and it says nothing about the real axis, which is entirely timelike.**

## Worked Checks on the Components

**Example (a path that leaves and a pair that does not).** The segment from $e_t$ to $-e_t$ is $\lambda e_t$ with $\lambda\in[-1,1]$; its $P$-value is $\lambda^2$, which vanishes at $\lambda=0$, so the segment leaves the sector at the origin and the two points lie in different components. The same two points are joined inside $\mathcal S$ only by a detour: the path $\sigma\mapsto\cos(\pi\sigma)(e_t+\vec e_x)+\sin(\pi\sigma)(\vec e_y+\vec e_z)$ has $P=\cos^2(\pi\sigma)-\sin^2(\pi\sigma)\cdot2$, which vanishes at $\sigma$ with $\tan^2(\pi\sigma)=\tfrac12$, so this path also crosses the cone and is not a path in the sector either. A path inside $\mathcal T$ from $e_t$ to an element of the negative sheet does not exist, by the theorem on the components. Verified numerically on both paths.

**Example (the radial retraction).** Take $\tilde q=2e_t+\vec e_x$. Then $P=4-1=3$, $\lvert P\rvert^{1/2}=\sqrt3$ and $\rho(\tilde q)=\tfrac1{\sqrt3}(2e_t+\vec e_x)$, with $P=1$ and $N=\tfrac53$. Take $\tilde q=e_t+2\vec e_x$; then $P=1-4=-3$, and $\rho(\tilde q)=\tfrac1{\sqrt3}(e_t+2\vec e_x)$ has $P=-1$, $N=\tfrac53$. So the two elements of the same $N$-sphere and of opposite $P$-sign lie on the two different hyperboloids, and the radial retraction separates them as the two components require.

**Proposition (the boundary).** The boundary of $\mathcal T$ and the boundary of $\mathcal S$ are both the null cone; the closure of each component of $\mathcal T$ adds the origin.

*Proof.* The cone is closed and of empty interior, and its complement is the union of the two open sets; so each of them is a union of components of the complement and the frontier of each is contained in the cone. Every point of the cone is a limit of timelike points, since $\tilde q+\varepsilon e_t$ has $P(\tilde q)+2\varepsilon q_t+\varepsilon^2$, positive for $\varepsilon$ small with the sign of $q_t$; and it is a limit of spacelike points, since $\tilde q+\varepsilon\vec e_x$ has $P(\tilde q)-2\varepsilon q_x-\varepsilon^2$, negative for small $\varepsilon$ on one side. Verified numerically on the cone.

**Remark (the sector as a manifold with corners).** Neither component is a manifold with boundary: each is an open subset of $\mathbb{H}$ whose frontier is the cone, and the cone is not smooth at the apex. **The sector is open and the cone is the wall; the wall has a singular point, and the two components share it in their closure and in nothing else.**

## The Symmetries of the Sector

**Proposition (what preserves the cut).** The sector is invariant under the conjugation, under the negation, and under every inner automorphism $\tilde q\mapsto\tilde u\tilde q\tilde u^{-1}$ with $\tilde u$ a versor; it is not invariant under the left multiplication by a general versor.

*Proof.* The conjugation reverses the sign of $\vec q$ and fixes $q_t$, so it preserves $P$; the negation multiplies $P$ by the square of the scalar; an inner automorphism fixes $q_t$ and rotates $\vec q$, preserving its modulus, hence $P$. For the failure, take $\tilde u=\tfrac1{\sqrt2}(e_t+\vec e_x)$ and $\tilde q=e_t$: then $\tilde u\tilde q=\tilde u$ has $P=0$, so the timelike element is sent to the cone. Verified numerically.

**Corollary (the compact part of the isometry group is inside the invertibles).** The inner automorphisms of the algebra, that is the group of the versors modulo $\{\pm e_t\}$, act on the sector as rotations of the vector subspace and are the compact part of $O(1,3)$.

*Proof.* The proposition and the identification of the inner automorphism group with $SO(3)$, which is [Quaternion Automorphisms and Derivations](quaternion-automorphisms-and-derivations.html). **The versors act on the sector by rotations around the scalar axis and by nothing else; the boosts are not inner, and this is the whole content of the Cartan decomposition of the group of the form.**

## The Comparison with the N-Regular Sector

| | $\{P\neq0\}$ | $\{N\neq0\}$ |
|---|---|---|
| complement | the null cone | the origin |
| components | two | one |
| dimensions | $4+4$ | $4$ |
| topology | two points $\uplus$ $S^2$ | contractible |
| retraction | radial, onto $P=\pm1$ | radial, onto $N=1$ |
| level set | two hyperboloids | one sphere |
| group | $O(1,3)$ | $O(4)$ |

**Remark (the comparison).** The N-regular sector is the complement of a point: it is connected, its retraction is the normalisation onto the unit sphere $S^3$, and its isometry group is the compact $O(4)$. The P-regular sector is the complement of a cone: it has two components, its retraction is the normalisation onto two hyperboloids, and its isometry group is the non-compact $O(1,3)$. **The passage from the definite to the indefinite cut is the passage from one sphere to two hyperboloids, from a connected sector to a disconnected one, and from a compact group to a non-compact one; the algebra is the same and the geometry is not.**

**Remark (the measure).** The cone is the zero set of a non-zero quadratic form, of Lebesgue measure zero, so the sector is of full measure: a random element of the algebra lies in the sector with probability one, and the classification of its sign is decided by the sign of $q_t$ against $\lvert\vec q\rvert$ alone. The null set, the object the following article is about, is large in dimension and null in measure, and this is the reason it is read by topology and not by counting.

## Summary

The P-regular sector is the complement of the null cone, open, dense, of full measure and of real dimension four.

It has exactly two components: the timelike component, the union of the two convex sheets $q_t>\lvert\vec q\rvert$ and $q_t<-\lvert\vec q\rvert$, and the spacelike component $\lvert q_t\rvert<\lvert\vec q\rvert$, homeomorphic to $S^2\times\mathbb{R}^2$.

Each component carries the hyperbolic reading of its sign: the positive sheet of $P=1$ is a model of $H^3$, the negative level $P=-1$ a model of $dS_3$, and the radial map $\tilde q\mapsto\tilde q/\sqrt{\lvert P\rvert}$ is a strong deformation retraction onto the level set of the sign.

The isometry group is $O(1,3)$, transitive on each sheet with stabiliser $O(3)$ on the positive one; the sector is contained in the group of invertibles with $N\geq\lvert P\rvert>0$; the real axis minus the origin is entirely timelike and the non-real stratum meets both components.

The N-regular sector is the complement of a point, connected, contractible, with the compact group $O(4)$; the comparison isolates the difference between a definite cut and an indefinite one.

The inner automorphisms, that is the rotations of the vector subspace, act on the sector; the boosts do not, and the two together are the Cartan decomposition of the isometry group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P(\tilde q)$ | $\mathrm{Sc}(\tilde q^2)=q_t^2-\lvert\vec q\rvert^2$ |
| $\mathcal T^+,\mathcal T^-$ | the two sheets $q_t>\lvert\vec q\rvert$ and $q_t<-\lvert\vec q\rvert$ |
| $\mathcal T$ | the timelike component, $\mathcal T^+\cup\mathcal T^-$ |
| $\mathcal S$ | the spacelike component $\{P<0\}$ |
| $\rho$ | the radial retraction onto $\{P=\pm1\}$ |
| $O(1,3)$ | the isometry group of $P$ |
| $dS_3$ | the de Sitter space $\{P=-1\}$ |

## Further Reading

- [The P-Norm Partition of the Quaternion Algebra](the-p-norm-partition-of-the-quaternion-algebra.html) for the partition this sector is the regular half of.
- [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html) for the cone that is the complement.
- [The P Level Sets and the Hyperbolic Structure of the Quaternion Algebra](the-p-level-sets-and-the-hyperbolic-structure-of-the-quaternion-algebra.html) for the metrics of the two hyperboloids.
- [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html) for the group acting.
- [Quaternion Metrics](quaternion-metrics.html) for the family of forms the norm belongs to.
- [Quaternion Automorphisms and Derivations](quaternion-automorphisms-and-derivations.html) for the inner automorphisms that act on the sector by rotations.
- [The Topology of the P-Null Cone of the Quaternion Algebra](the-topology-of-the-p-null-cone-of-the-quaternion-algebra.html) for the wall of the sector.
