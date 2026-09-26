
# __Split-Biquaternion Geometry__

## Introduction

This article is the geometry slot of the split biquaternion system. It describes the geometric structures that the algebra $\mathbb{H}_{\mathbb{D}}$ carries in its own right: the two quadratic forms attached to it, the unit sphere and its metric, the zero divisor cone and its two ruling ideals, the quadric defined by the Hermitian form, and the incidence geometry of the neutral planes. The article is the geometric companion of the written algebraic articles of the same system and the split-biquaternion entry of the ladder that Part V traverses one number system at a time.

The article assumes the split biquaternion algebra from *Split-Biquaternion Algebra*: the tensor product $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$, the basis $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the central split complex unit $j$ with $j^2 = +e_0$, the four conjugations $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger} = \bar{\cdot}\,{}^{*}$ and ${}^{\flat} = -{}^{\dagger}$, the idempotents $e_{\pm} = \tfrac{1}{2}(1\pm j)$ and the isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$. It assumes the norm form $N(\tilde Q) = \tilde Q\bar{\tilde Q}$, its non-invertibility exactly on the zero divisors, and the idempotent description of invertibility, from *Split-Biquaternion Norm and Invertibility*; the description of the zero divisors as the union of the two ideals from *Split-Biquaternion Zero Divisors*; the classification of the roots of $-e_0$ from *Split-Biquaternion Roots of Minus One*; and the polar representation of the units from *Split-Biquaternion Polar Representation*, whose algebraic content is used here only as the input to a geometric statement and is not restated. The Hermitian scalar form and its two Lorentzian and neutral restrictions are established in *Split-Biquaternion Rotations and the Lorentz Group*, and are used here as the metric datum. The general theory of quadrics, of isotropic subspaces and of the isometry groups of forms is the subject of the Part II companion *Pseudo-Riemannian and Lorentzian Geometry* and of the Part I companions *Quadratic Forms and Polarisation*, *Bilinear Forms* and *Isometries and Orthogonal Transformations*, written in parallel; the present article treats only the structures of this one algebra.

Throughout, $\tilde Q = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu = q_\mu + jq'_\mu$ and $q_\mu, q'_\mu\in\mathbb{R}$, and the real coordinates of $\tilde Q$ are $(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)$. Two quadratic forms are used: the **Euclidean form**

$$
\lvert\tilde Q\rvert^2 = \sum_{\mu=0}^{3}\left(q_\mu^2 + (q'_\mu)^2\right),
$$

which is positive definite of signature $(8,0)$ and is the norm form of $\mathbb{H}_{\mathbb{D}}$ as a real vector space, and the **Hermitian scalar form**

$$
g(\tilde P,\tilde Q) = \operatorname{Sc}\!\left(\tilde P\tilde Q^{\dagger}\right),
$$

which is non-degenerate of signature $(4,4)$. The involution ${}^{\dagger}$ and its two eigenspaces $\mathbb{M}_{\pm}$ are those of *Split-Biquaternion Rotations and the Lorentz Group*.

## The Norm Form and Its Zero Set

### The Norm Form as a Quadratic Map

**Definition.** The **norm form** is the map

$$
N : \mathbb{H}_{\mathbb{D}}\longrightarrow\mathbb{D}, \qquad N(\tilde Q) = \tilde Q\bar{\tilde Q}.
$$

**Proposition.** The norm form is multiplicative, $N(\tilde P\tilde Q) = N(\tilde P)N(\tilde Q)$, and quadratic over $\mathbb{R}$: for real $\lambda$ one has $N(\lambda\tilde Q) = \lambda^2N(\tilde Q)$, and the polarisation

$$
N(\tilde P + \tilde Q) - N(\tilde P) - N(\tilde Q) = \tilde P\bar{\tilde Q} + \tilde Q\bar{\tilde P}
$$

is $\mathbb{R}$-bilinear. In coordinates,

$$
N(\tilde Q) = \sum_{\mu=0}^{3}Q_\mu^2
= \left(\sum_{\mu=0}^{3}\left(q_\mu^2 + (q'_\mu)^2\right)\right) + 2j\left(\sum_{\mu=0}^{3}q_\mu q'_\mu\right).
$$

*Proof.* Multiplicativity is the multiplicativity of the quaternion norm extended $\mathbb{D}$-linearly, established in *Split-Biquaternion Algebra*; quadraticity follows by expanding the product. The coordinate formula is the expansion of $\sum_\mu(q_\mu + jq'_\mu)^2$ using $j^2 = +e_0$. $\square$

The norm form is therefore the sum of a positive definite real quadratic form and a second real quadratic form multiplied by $j$. The two are

$$
R(\tilde Q) = \lvert\tilde Q\rvert^2 = \sum_{\mu=0}^{3}\left(q_\mu^2 + (q'_\mu)^2\right), \qquad
I(\tilde Q) = 2\sum_{\mu=0}^{3}q_\mu q'_\mu,
$$

so that $N = R + jI$. The form $R$ is the Euclidean form of the introduction; the form $I$ is the polarisation of the product of each real coordinate with its split partner.

### The Zero Set

**Definition.** The **null set** of the norm form, also called the **zero divisor cone**, is

$$
Z = \{\tilde Q\in\mathbb{H}_{\mathbb{D}} : N(\tilde Q) = 0\}.
$$

**Theorem.** The zero divisor cone has the following description. The norm form vanishes at $\tilde Q$ if and only if the split complex number $N(\tilde Q)$ is a zero divisor of $\mathbb{D}$, that is, if and only if the idempotent component $\tilde Q_+$ or the idempotent component $\tilde Q_-$ is the quaternion zero. Equivalently,

$$
Z = \mathbb{H}e_+\cup\mathbb{H}e_- = \{\tilde Q : \tilde Q_+ = 0\}\cup\{\tilde Q : \tilde Q_- = 0\},
$$

the union of the two ideals, and each of the two sets is a real four-dimensional subspace; the two meet only at the origin, and $Z$ is the union of two four-dimensional subspaces of the eight-dimensional real space $\mathbb{H}_{\mathbb{D}}$. In terms of the decomposition $N = R + jI$ the cone is the locus $\lvert I(\tilde Q)\rvert = R(\tilde Q)$, which for the two real forms $R$ and $I$ is the equality case of the Cauchy–Schwarz inequality.

*Proof.* In the split complex algebra an element $u = c + js$ is a zero divisor if and only if $c^2 = s^2$, that is, if and only if $u$ has the form $\lambda(1\pm j)$ with $\lambda\in\mathbb{R}$; equivalently $uu^{*} = 0$ (see *Split Complex Algebra*). Since $N(\tilde Q) = N(\tilde Q_+)e_+ + N(\tilde Q_-)e_-$ under the idempotent decomposition, the norm form is a zero divisor of $\mathbb{D}$ exactly when one of the two quaternion norms vanishes, and a quaternion norm vanishes only at the quaternion zero. This gives the two ideals, and each ideal is four-dimensional over $\mathbb{R}$ because it is a copy of $\mathbb{H}$. They meet only at the origin because $\tilde Q_+ = 0$ and $\tilde Q_- = 0$ together give $\tilde Q = 0$. For the last statement, $N(\tilde Q) = R + jI$ with $R = \sum_\mu(q_\mu^2 + (q'_\mu)^2)$ and $I = 2\sum_\mu q_\mu q'_\mu$, so the idempotent components of $N(\tilde Q)$ are $R \pm I = \sum_\mu(q_\mu\pm q'_\mu)^2$, which vanish exactly when $q'_\mu = \mp q_\mu$ for all $\mu$; this is the equality case of $\lvert\sum_\mu q_\mu q'_\mu\rvert \leq \sqrt{\sum_\mu q_\mu^2}\sqrt{\sum_\mu (q'_\mu)^2}$. $\square$

The description of the zero divisor set is the geometric counterpart of the algebraic statement of *Split-Biquaternion Zero Divisors*: the set of non-invertible elements is a union of two subspaces, not a hypersurface, and it is not a cone in the sense of a single quadratic cone but the union of the two ruling subspaces.

**Proposition.** Both ideals $\mathbb{H}e_+$ and $\mathbb{H}e_-$ are totally isotropic for the Hermitian scalar form $g$: $g(\tilde P,\tilde Q) = 0$ for all $\tilde P,\tilde Q$ in the same ideal. They are four-dimensional and maximal with this property, since the maximal totally isotropic subspaces of a neutral form of signature $(4,4)$ are four-dimensional.

*Proof.* If $\tilde Q = \tilde Q_-e_-$ then $\tilde Q^{\dagger} = \bar{\tilde Q}_-e_+$, so $\tilde Q\tilde Q^{\dagger} = \tilde Q_-\bar{\tilde Q}_-e_-e_+ = 0$ and hence $g(\tilde Q,\tilde Q) = 0$; polarisation gives $g(\tilde P,\tilde Q) = 0$ within the ideal, since $\tilde P\tilde Q^{\dagger}$ has the same form with $\tilde P_-,\tilde Q_-$ and $\operatorname{Sc}(\tilde P_-\bar{\tilde Q}_-e_-e_+) = 0$ because every element of the form $\tilde R e_+$ has scalar part $\tfrac{1}{2}\operatorname{Sc}(\tilde R)$ and $\tilde P_-\bar{\tilde Q}_-e_-e_+ = 0$. By Witt's theorem the maximal totally isotropic subspaces of a non-degenerate form of signature $(4,4)$ have dimension the minimum of the two indices, which is four. $\square$

## The Unit Sphere and Its Metric

### The Unit Sphere

**Definition.** The **unit sphere** of the split biquaternion algebra is

$$
S(\mathbb{H}_{\mathbb{D}}) = \{\tilde Q\in\mathbb{H}_{\mathbb{D}} : N(\tilde Q) = e_0\}.
$$

**Theorem.** The unit sphere is the product $S^3\times S^3$ of two round three-spheres, exhibited by the idempotent decomposition: an element $\tilde Q$ has norm form $e_0$ if and only if $\lvert\tilde Q_+\rvert = \lvert\tilde Q_-\rvert = 1$, and the map

$$
\mathbb{H}e_+\oplus\mathbb{H}e_-\longrightarrow\mathbb{H}\oplus\mathbb{H}, \qquad
\tilde Q = \tilde Q_+e_+ + \tilde Q_-e_-\longmapsto(\tilde Q_+,\tilde Q_-)
$$

is a ring isomorphism carrying $S(\mathbb{H}_{\mathbb{D}})$ onto $S^3\times S^3$. In particular $S(\mathbb{H}_{\mathbb{D}})$ is a compact six-dimensional manifold, and it is a group under multiplication.

*Proof.* The norm form of $\tilde Q = \tilde Q_+e_+ + \tilde Q_-e_-$ is $N(\tilde Q_+)e_+ + N(\tilde Q_-)e_-$ because $e_{\pm}$ are orthogonal idempotents, and this equals $e_0 = e_+ + e_-$ exactly when both quaternion norms equal $1$. The identification $S^3\times S^3$ is then immediate. $\square$

The unit sphere is thus a compact Lie group of dimension six. It is not a hyperboloid and not a symmetric space of non-compact type; the hyperboloids of this system are described, and are level sets of the Hermitian form rather than of the norm form.

### The Product Metric

**Definition.** The **product metric** on $S(\mathbb{H}_{\mathbb{D}})\cong S^3\times S^3$ is

$$
d\left((u_+,u_-),(v_+,v_-)\right)^2 = d_{S^3}(u_+,v_+)^2 + d_{S^3}(u_-,v_-)^2,
$$

where $d_{S^3}$ is the geodesic distance of the quaternion sphere, $d_{S^3}(u,v) = \arccos\operatorname{Sc}(u\bar v)$.

**Proposition.** The product metric is a bi-invariant metric on the group $S^3\times S^3$, it is the metric induced by the Euclidean form restricted to the unit sphere in the directions tangent to it, and its geodesics are the products of great circles. Its diameter is $\pi$ in each coordinate, the cut locus of a point is the product of the two antipodes, and the volume of the unit sphere with respect to the induced Riemannian volume is

$$
\operatorname{vol}(S^3\times S^3) = (2\pi^2)^2 = 4\pi^4 .
$$

*Proof.* The group $S^3\times S^3$ is a direct product of compact Lie groups, and the product of bi-invariant metrics is bi-invariant, since translations act coordinatewise. The product of the tangent spaces at the identity is $\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}$, on which the product of the quaternion invariant inner products is invariant under the adjoint action. The geodesics of a Riemannian product are the products of geodesics, and the cut locus and diameter statements follow. The volume of $S^3$ with the round metric of radius one is $2\pi^2$, and volumes multiply in a Riemannian product. $\square$

The unit sphere therefore carries the geometry of a product of two round spheres; its curvature is not of constant sign but non-negative, and its fundamental group is trivial. The two-sided action of the unit sphere on itself, giving left and right translations, is the geometric expression of the group structure, and it extends to the whole algebra by multiplication.

### The Quotients

The unit sphere contains two distinguished compact subgroups, the two factors $S^3\times\{1\}$ and $\{1\}\times S^3$, and the diagonal $\Delta S^3$. Their geometric quotients are the following.

**Proposition.** The quotients

$$
(S^3\times S^3)/\Delta S^3\cong S^3, \qquad (S^3\times S^3)/(S^3\times\{1\})\cong S^3, \qquad (S^3\times S^3)/\{\pm(1,1)\}
$$

are respectively the quaternion sphere, the quaternion sphere again, and a compact six-dimensional group covered two-to-one by the unit sphere. The first two identifications show that the split biquaternion unit sphere fibres over the quaternion unit sphere, with a fibre the diagonal copy of $S^3$ in the first case and a right coset in the second.

*Proof.* The diagonal acts freely by $(u,v)\mapsto(uw,vw)$, and the map $(u,v)\mapsto uw$ for $w = v^{-1}$ exhibits the orbit space as the set of ratios $uv^{-1}$, which is all of $S^3$ because $S^3$ is a group; the stabiliser is the diagonal. The quotient by the first factor is the set of second coordinates. The last quotient is the quotient by the centre, computed from the centre of the product. $\square$

These quotients are the split-biquaternion counterpart of the projective quotient $\mathbb{H}P^1 = S^4$ of the quaternion theory; the difference is that here the quotients are again three-spheres rather than a four-sphere, because the split biquaternion unit group is a product and its quotients by the factors are the factors themselves.

## The Projective and Incidence Geometry

### The Quadric of the Hermitian Form

The Hermitian scalar form defines a quadric, and its isotropic subspaces carry an incidence geometry.

**Definition.** Let $\mathbb{P}(\mathbb{H}_{\mathbb{D}})$ be the real projective space of seven dimensions on the real vector space $\mathbb{H}_{\mathbb{D}}$. The **Hermitian quadric** is

$$
Q(g) = \left\{[\tilde Q]\in\mathbb{P}(\mathbb{H}_{\mathbb{D}}) : g(\tilde Q,\tilde Q) = 0\right\},
$$

the projectivisation of the null cone of $g$; it is a non-degenerate quadric of dimension six and of signature $(4,4)$, called a quadric of Kleinian type.

**Proposition.** The quadric $Q(g)$ contains two families of four-dimensional totally isotropic subspaces, namely the projectivisations of the maximal totally isotropic subspaces of $g$; through each point of $Q(g)$ there passes at least one member of each family, and the two families are interchanged by the symmetries of the quaternion index set. The ideals $\mathbb{H}e_+$ and $\mathbb{H}e_-$ project to two members of these families, so the zero divisor set of the algebra is a union of two ruling subspaces of the quadric.

*Proof.* The zero divisor ideals are totally isotropic of dimension four by the proposition above, so their projectivisations are three-dimensional projective subspaces contained in $Q(g)$; in the projective space $\mathbb{P}^7$ the maximal projective subspaces of a $(4,4)$ quadric have dimension three, since the maximal totally isotropic vector subspaces have dimension four. The incidence statement is the standard description of the maximal isotropic subspaces of a form of signature $(4,4)$, whose two families are parametrised by the choice of a maximal positive subspace of dimension four and its orthogonal complement; the identification with the quaternion index set is made through the pairing $\mu\leftrightarrow$ the coordinate $e_\mu$ and the split partner. $\square$

The zero divisor set therefore has a projective interpretation: it is not a hypersurface but a union of two families of maximal linear spaces on the quadric. This is the sense in which the split biquaternion geometry has two rulings, and it is the geometric content of the algebraic decomposition into two ideals.

### The Neutral Planes and Their Incidence

**Definition.** A **neutral plane** in $\mathbb{H}_{\mathbb{D}}$ is a four-dimensional real subspace on which $g$ has signature $(2,2)$. A neutral plane is **totally isotropic** if the restriction of $g$ to it is zero, which with dimension four is the maximal isotropic case.

**Proposition.** Let $\mu\neq\nu$ be distinct elements of $\{0,1,2,3\}$. The $\mathbb{D}$-span $\mathbb{D}e_\mu\oplus\mathbb{D}e_\nu$ is a neutral plane with $g$-orthonormal basis $(e_\mu, je_\mu, e_\nu, je_\nu)$ and signature $(+1,-1,+1,-1)$; the group $O(2,2)$ is its isometry group. Two such planes intersect in the two-dimensional split complex line $\mathbb{D}e_\mu$ when they share exactly one index, and in the origin otherwise.

*Proof.* The orthogonality and the diagonal values are the computation of *Split-Biquaternion Rotations and the Lorentz Group*; the intersection statement is immediate from the direct sum decomposition of $\mathbb{H}_{\mathbb{D}}$ into the four split complex lines $\mathbb{D}e_\mu$. $\square$

The neutral planes are the geometric home of the hyperbolic rotations of the system: by the results of *Split-Biquaternion Rotations and the Lorentz Group*, left multiplication by a unit $e^{\theta j}$ of the split complex part acts on each neutral plane as a simultaneous hyperbolic rotation in the two coordinate planes, giving a two-dimensional subgroup of $SO^{+}(2,2)$.

## The Isometry Group and the Homogeneous Description

### The Group Preserving the Hermitian Form

The geometry of the Hermitian form is governed by its isometry group.

**Definition.** The **isometry group** of $g$ is

$$
O(4,4) = \{T\in GL_8(\mathbb{R}) : g(T\tilde P,T\tilde Q) = g(\tilde P,\tilde Q)\ \text{for all }\tilde P,\tilde Q\},
$$

with identity component $SO^{+}(4,4)$ and maximal compact subgroup $O(4)\times O(4)$.

**Proposition.** $\dim O(4,4) = 28$, the maximal compact subgroup of $SO^{+}(4,4)$ is $SO(4)\times SO(4)$, and the quadric $Q(g)$ is the compact dual of the symmetric space $SO^{+}(4,4)/(SO(4)\times SO(4))$, which is of dimension sixteen and rank four.

*Proof.* The dimension of $O(p,q)$ is $\tfrac{1}{2}(p+q)(p+q-1) = \tfrac{1}{2}\cdot 8\cdot 7 = 28$. The maximal compact subgroup is $O(p)\times O(q)$ for a form of signature $(p,q)$ with $p,q > 0$, giving $O(4)\times O(4)$; its identity component is $SO(4)\times SO(4)$. The symmetric space $SO^{+}(p,q)/(SO(p)\times SO(q))$ is the Grassmannian of maximal positive subspaces, of dimension $pq = 16$ and rank $\min(p,q) = 4$, and the quadric is its compact dual, the standard duality of the symmetric space and the quadric associated to a form of signature $(p,q)$ with $p = q$. $\square$

**Proposition.** The subgroup of $GL_8(\mathbb{R})$ preserving the algebra structure of $\mathbb{H}_{\mathbb{D}}$ and the Hermitian form $g$ is a closed subgroup of $O(4,4)$; it contains the compact group $Sp(1)\times Sp(1)$ of two-sided multiplication by unit quaternions, acting on the quaternion subspace and inducing $SO(4)$, and the split complex unit group $e^{\theta j}$ of the neutral planes.

*Proof.* The algebra automorphisms and the two-sided multiplications preserve the algebra structure, and the claim is that those among them preserve $g$. The two-sided multiplication by $\tilde S_+,\tilde S_-\in Sp(1)$ acts on the quaternion part by $SO(4)$, which preserves the definite form on the quaternion subspace of the algebra; combined with the identity action on the split partners it preserves $g$. The split complex units preserve $g$ on each neutral plane by the proposition of the previous article. $\square$

### The Algebra as a Normed Space

The Euclidean form $\lvert\cdot\rvert^2$ gives $\mathbb{H}_{\mathbb{D}}$ the structure of a normed real vector space of dimension eight, and the multiplication is continuous in that norm but not norm-multiplicative. The sharp inequality is

$$
\lvert\tilde P\tilde Q\rvert \leq \sqrt{2}\,\lvert\tilde P\rvert\lvert\tilde Q\rvert,
$$

and the constant $\sqrt{2}$ is attained, for instance at $\tilde P = \tilde Q = (1+j)e_0$. This follows from multiplicativity of $N = R + jI$: writing $R_{\tilde P} = \lvert\tilde P\rvert^2$ and $I_{\tilde P}$ for the second form, one has $R_{\tilde P\tilde Q} = R_{\tilde P}R_{\tilde Q} + I_{\tilde P}I_{\tilde Q}$, and $\lvert I_{\tilde P}I_{\tilde Q}\rvert \leq R_{\tilde P}R_{\tilde Q}$ by the inequality $\lvert I(\tilde X)\rvert\leq R(\tilde X)$ established above, so $R_{\tilde P\tilde Q}\leq 2R_{\tilde P}R_{\tilde Q}$; equality holds exactly when both $\tilde P$ and $\tilde Q$ lie on the zero divisor cone with $I_{\tilde P}I_{\tilde Q} > 0$, as for the displayed example, where $R = 2$, $I = 2$ and $\lvert\tilde P^2\rvert = \sqrt{8} = \sqrt2\,\lvert\tilde P\rvert^2$. The polar decomposition of a non-zero element is

$$
\tilde Q = \lvert\tilde Q\rvert\,\frac{\tilde Q}{\lvert\tilde Q\rvert},
$$

with the second factor a point of the Euclidean unit sphere of $\mathbb{H}_{\mathbb{D}}$, not of the unit sphere $S(\mathbb{H}_{\mathbb{D}})$; the two spheres are different, and the geometric content of the difference is exactly that the Euclidean sphere meets both the zero divisor cone and the algebraic unit sphere in lower-dimensional sets. The polar representation of the units of the algebra, established in *Split-Biquaternion Polar Representation*, describes which units occur; the geometric statement kept here is that the set of units is not the Euclidean unit sphere and not the algebraic unit sphere, but the complement of the zero divisor cone.

## Comparison with the Neighbouring Systems

The geometry of the split biquaternions is best read against the two geometries it generalises and against the quaternion geometry it doubles.

| Feature | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{H}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|
| Real dimension | $2$ | $2$ | $4$ | $8$ |
| Norm form | $z\bar z > 0$ | $c^2 - s^2$ indefinite | $q\bar q > 0$ | $N = R + jI$ split complex |
| Zero divisors | none | two lines | none | two four-dimensional ideals |
| Unit sphere | $S^1$ | two hyperbola branches | $S^3$ | $S^3\times S^3$ |
| Unit sphere compact | yes | no | yes | yes |
| Isometry group of the form | $O(2)$ | $O(1,1)$ | $O(4)$ | $O(4,4)$ |
| Signature of the ambient form | $(2,0)$ | $(1,1)$ | $(4,0)$ | $(4,4)$ |
| Projective line | $\mathbb{C}P^1=S^2$ | — | $\mathbb{H}P^1 = S^4$ | quotient $S^3$ |

Two features separate the split biquaternion system from both the complex and the quaternion systems. First, the norm form is not real-valued but split complex valued, so it does not define a distance; the metric that $\mathbb{H}_{\mathbb{D}}$ carries is the Euclidean metric $\lvert\cdot\rvert^2$, and the norm form instead defines the zero divisor cone. Second, the zero divisor cone is not a hypersurface but a union of two linear subspaces; the geometry of the system is therefore affine and incidence-theoretic rather than conformal. Against the split complex system, the split biquaternion system replaces the two-branched hyperbola of units by the compact group $S^3\times S^3$: naively passing from $\mathbb{D}$ to $\mathbb{D}\otimes\mathbb{H}$ restores compactness, because the quaternion factor is definite even though the split complex factor is not.

## Summary

The split biquaternion algebra carries two quadratic forms. The Euclidean form $\lvert\tilde Q\rvert^2 = \sum_\mu(q_\mu^2 + (q'_\mu)^2)$ is positive definite of signature $(8,0)$ and gives the metric of the underlying real vector space. The norm form $N(\tilde Q) = \tilde Q\bar{\tilde Q}$ is split complex valued, equal to $R + jI$ with $R = \lvert\tilde Q\rvert^2$ and $I = 2\sum_\mu q_\mu q'_\mu$, and multiplicative. Its zero set is the union of the two ideals $\mathbb{H}e_+$ and $\mathbb{H}e_-$, each a real four-dimensional subspace, meeting only at the origin; the zero divisors are therefore a union of two ruling subspaces rather than a hypersurface.

The unit sphere $\{\tilde Q : N(\tilde Q) = e_0\}$ is the product $S^3\times S^3$, a compact six-dimensional group with the product of the round metrics, of volume $4\pi^4$, bi-invariant, with geodesics the products of great circles. Its quotients by the diagonal and by either factor are three-spheres. The Hermitian scalar form $g(\tilde P,\tilde Q) = \operatorname{Sc}(\tilde P\tilde Q^{\dagger})$ is non-degenerate of signature $(4,4)$; its projectivised null cone is a Kleinian quadric of dimension six, on which the two zero divisor ideals project to two maximal totally isotropic subspaces; the $\mathbb{D}$-span of two quaternion coordinates is a neutral plane of signature $(2,2)$ with isometry group $O(2,2)$. The isometry group of $g$ is $O(4,4)$, of dimension twenty-eight, with maximal compact subgroup $O(4)\times O(4)$, and the quadric is the compact dual of the Hermitian symmetric space $SO^{+}(4,4)/(SO(4)\times SO(4))$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | The split biquaternion algebra, real dimension $8$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $j$ | Split complex unit, $j^2 = +e_0$, central |
| $Q_\mu = q_\mu + jq'_\mu$ | Split complex coefficients, $q_\mu, q'_\mu\in\mathbb{R}$ |
| $e_{\pm} = \tfrac{1}{2}(1\pm j)$ | Idempotents, $e_+e_- = 0$ |
| $\bar{\cdot},\ {}^{*},\ {}^{\dagger},\ {}^{\flat}$ | Quaternion, split complex, Hermitian and anti-Hermitian conjugations |
| $N(\tilde Q) = \tilde Q\bar{\tilde Q} = R + jI$ | Norm form, split complex valued |
| $R = \lvert\tilde Q\rvert^2 = \sum_\mu(q_\mu^2 + (q'_\mu)^2)$ | Euclidean form, signature $(8,0)$ |
| $I = 2\sum_\mu q_\mu q'_\mu$ | Split part of the norm form |
| $Z = \mathbb{H}e_+\cup\mathbb{H}e_-$ | Zero divisor cone, the two ideals |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $g(\tilde P,\tilde Q) = \operatorname{Sc}(\tilde P\tilde Q^{\dagger})$ | Hermitian scalar form, signature $(4,4)$ |
| $S(\mathbb{H}_{\mathbb{D}}) = \{\tilde Q : N(\tilde Q) = e_0\}\cong S^3\times S^3$ | Unit sphere, compact group |
| $d_{S^3}(u,v) = \arccos\operatorname{Sc}(u\bar v)$ | Geodesic distance on $S^3$ |
| $\Delta S^3$ | Diagonal subgroup of $S^3\times S^3$ |
| $Q(g)$ | Hermitian quadric in $\mathbb{P}^7$, Kleinian type $(4,4)$ |
| $\mathbb{D}e_\mu\oplus\mathbb{D}e_\nu$ | Neutral four-plane, signature $(2,2)$ |
| $O(4,4)$, $SO^{+}(4,4)$, $O(2,2)$ | Isometry groups of $g$ and of the neutral planes |
| $e^{\theta j} = \cosh\theta + j\sinh\theta$ | Split complex unit, hyperbolic one-parameter group |



## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for symmetric spaces, their compact duals and the maximal compact subgroups of the orthogonal groups.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Clarendon Press, 1994), for the geometry of positive cones and the Jordan-theoretic description of the associated symmetric spaces.
- Dirk J. Struik, *Lectures on Classical Differential Geometry* (Dover, 1988), for the classification of ruled quadrics and their two families of rulings.
- Walter Benz, *Classical Geometries in Modern Contexts* (Birkhäuser, 2005), for the incidence geometry of quadrics of arbitrary signature.
- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the null cone, the totally isotropic subspaces and the classification of forms of signature $(p,q)$.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the product of compact Lie groups and the quotient geometry of $S^3\times S^3$.
