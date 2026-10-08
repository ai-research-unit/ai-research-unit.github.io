
# __Split-Quaternion Topology__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ is a four-dimensional real vector space with an indefinite norm $N(\tilde q) = q_0^2 + q_1^2 - q_2^2 - q_3^2$. Its topology is therefore simple wherever it is the topology of the underlying vector space, and interesting only where the split-quaternion norm cuts out the group of units, the norm-one group and the null cone. This article collects those topological facts: the contractibility of the algebra, the two components of the group of units, the circle that the norm-one group retracts onto, the torus that is the link of the null cone, the two families of isotropic lines, and the radial structure of the algebra near the null cone.

The article owns the topological statements of the category. It relies on *Split-Quaternion Norm and Invertibility* for the group of units, on *Split-Quaternion Exponential and Lie Group Structure* for the norm-one group and the Lorentz double cover, and on *Split-Quaternion Null Quadric and Projective Geometry* for the ruling of the null quadric. All the invariants below are standard; the signs of the indefinite form and the reality of the algebra are what distinguish the picture from the biquaternion one. No physics is invoked.

**Conventions.** The algebra is $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ with the coordinates $q_0, q_1, q_2, q_3$; the split-quaternion norm is $N = q_0^2 + q_1^2 - q_2^2 - q_3^2$ of signature $(2,2)$; the group of units is $\mathbb{H}_{\mathrm{s}}^\times = \{N \neq 0\}$; the norm-one group is $U = \{N = 1\} = \mathrm{SL}_2(\mathbb{R})$; the null cone is $\mathcal{N} = \{N = 0\}$; the vector subspace is $V = \operatorname{span}\{e_1,e_2,e_3\}$ with $N|_V = q_1^2 - q_2^2 - q_3^2$ of signature $(2,1)$. The Euclidean norm of $(q_0,q_1,q_2,q_3)$ is $|\tilde q|_E = (q_0^2+q_1^2+q_2^2+q_3^2)^{1/2}$, and $\Sigma^3$ denotes the Euclidean unit sphere.

## The Underlying Space and Its Contractibility

**Theorem.** As a topological space, $\mathbb{H}_{\mathrm{s}}$ is homeomorphic to $\mathbb{R}^4$ and is therefore **contractible**: $\pi_0(\mathbb{H}_{\mathrm{s}})$ is a point and $\pi_k(\mathbb{H}_{\mathrm{s}}) = 0$ for every $k \geq 1$.

**Proof.** The coordinate map $\tilde q \mapsto (q_0,q_1,q_2,q_3)$ is a homeomorphism onto $\mathbb{R}^4$, and the straight-line homotopy $H(\tilde q,t) = (1-t)\tilde q$ contracts the algebra to the origin.

Consequently every interesting invariant of the article comes from a *deleted* set or a *level set* of $N$, not from the algebra itself. The punctured algebra $\mathbb{H}_{\mathrm{s}} \setminus \{0\}$ has the homotopy type of the Euclidean sphere $\Sigma^3$, by the radial deformation retraction $\tilde q \mapsto \tilde q/|\tilde q|_E$.

## The Group of Units and Its Components

**Theorem.** The group of units $\mathbb{H}_{\mathrm{s}}^\times = \{N \neq 0\}$ has exactly two connected components, $\{N > 0\}$ and $\{N < 0\}$. Each component deformation retracts onto its intersection with $\Sigma^3$, and each is homotopy equivalent to a circle:

$$
\{N > 0\} \simeq SO(2), \qquad \{N < 0\} \simeq SO(2).
$$

Hence $\pi_0(\mathbb{H}_{\mathrm{s}}^\times) = \mathbb{Z}/2$ and $\pi_1(\mathbb{H}_{\mathrm{s}}^\times) = \mathbb{Z}$ on each component, so $\pi_1$ of the group is free abelian of rank two.

**Proof.** The map $\tilde q \mapsto \tilde q/|\tilde q|_E$ retracts $\{N \neq 0\}$ onto the set $\{N = \pm 1\} \cap \Sigma^3$ without changing the sign of $N$, componentwise. The component $\{N>0\}$ retracts onto its maximal compact subgroup $SO(2)$ by the Gram–Schmidt process, and the component $\{N<0\}$ is the coset $e_2\{N>0\}$, homeomorphic to the first. A circle has $\pi_0$ a point and $\pi_1 = \mathbb{Z}$.

## The Norm-One Group

**Theorem.** The norm-one group $U = \{N = 1\} = \mathrm{SL}_2(\mathbb{R})$ is a connected three-dimensional submanifold of $\mathbb{H}_{\mathrm{s}}$, diffeomorphic to $S^1 \times \mathbb{R}^2$; it deformation retracts onto its maximal compact subgroup $SO(2)$,

$$
U \simeq S^1, \qquad \pi_1(U) = \mathbb{Z}.
$$

**Proof.** The set $U$ is the level set of the regular value $1$ of $N$, so it is a smooth three-manifold; it is connected, retracting onto its intersection with $\Sigma^3$, which is the set $\{N=1\} \cap \Sigma^3 = \{q_0^2+q_1^2 = 1, q_2=q_3=0\}$, a circle. The KAN (Iwasawa) decomposition $\mathrm{SL}_2(\mathbb{R}) = SO(2)\cdot A \cdot N$ with $A \cong \mathbb{R}$ and $N \cong \mathbb{R}$ gives the diffeomorphism $U \cong S^1 \times \mathbb{R}^2$.

By *Split-Quaternion Exponential and Lie Group Structure* the group $U$ double-covers the identity component $\mathrm{SO}^{+}(2,1)$ of the Lorentz group. The double cover is **not** the universal cover: $\pi_1(U) = \mathbb{Z}$ is infinite, so the universal cover of $\mathrm{SO}^{+}(2,1)$ is an infinite cyclic cover of $U$ and not $U$ itself. This is a structural difference from the quaternion case, where the unit sphere is the simply connected three-sphere and its double cover of $SO(3)$ is universal.

## The Null Cone and Its Link

**Definition.** The **null cone** is

$$
\mathcal{N} = \{\, \tilde q : N(\tilde q) = 0 \,\} = \{\, q_0^2 + q_1^2 = q_2^2 + q_3^2 \,\},
$$

the set of zero divisors together with the origin; the **link** of the cone is $\mathcal{N} \cap \Sigma^3$.

**Theorem.** The null cone is a cone on its link: $\mathcal{N} = \{\, t\, \tilde p : t \geq 0,\ \tilde p \in \mathcal{N}\cap\Sigma^3 \,\}$, and the link is a **torus**,

$$
\mathcal{N} \cap \Sigma^3 \;\cong\; S^1 \times S^1 = T^2 .
$$

Hence $\mathcal{N}\setminus\{0\}$ is homotopy equivalent to $T^2$, with $\pi_1(\mathcal{N}\setminus\{0\}) = \mathbb{Z}^2$.

**Proof.** A null point $\tilde q \neq 0$ is $t \tilde p$ with $t = |\tilde q|_E > 0$ and $\tilde p$ on the sphere; the cone property is homogeneity of $N$. On the sphere the equations $q_0^2+q_1^2 = q_2^2+q_3^2$ and $q_0^2+q_1^2+q_2^2+q_3^2 = 1$ give $q_0^2+q_1^2 = q_2^2+q_3^2 = \tfrac12$, so $(q_0,q_1)$ lies on the circle of radius $1/\sqrt2$ and $(q_2,q_3)$ on the circle of radius $1/\sqrt2$, independently: the link is the product of the two circles, a torus. The radial retraction makes $\mathcal{N}\setminus\{0\}$ homotopy equivalent to the link.

The cone is singular at the origin, and the singularity is the vertex of the cone on the torus; away from the origin the cone is a smooth three-manifold.

## The Two Families of Isotropic Lines

Inside the null cone sit the **maximal isotropic subspaces** of the form, of dimension $2$. They fall into two families, each parametrised by a projective line.

**Theorem.** The maximal isotropic subspaces of $N$ are the two families of two-dimensional planes

$$
\mathcal{L} = \{\, L_\lambda \,\}, \qquad \mathcal{M} = \{\, M_\mu \,\},
$$

each parametrised by a projective line and each consisting of totally isotropic planes; the two families are disjoint, their union fills the null cone, and each maximal isotropic plane belongs to exactly one of them. In the projective space $\mathbb{P}^3$ the two families are the two rulings of the smooth quadric surface $Q = \{N = 0\}$, which is $\cong \mathbb{P}^1 \times \mathbb{P}^1$.

**Proof.** The form has signature $(2,2)$, so a maximal isotropic subspace has dimension $2$ and the Witt index is $2$. A concrete maximal isotropic plane is

$$
L = \operatorname{span}\Bigl\{ \tfrac12(1+e_2),\; e_1 + e_3 \Bigr\},
$$

whose generators are null — $N\bigl(\tfrac12(1+e_2)\bigr) = \tfrac14 N(1+e_2) = 0$ and $N(e_1+e_3) = 1 - 1 = 0$ — and mutually $B$-orthogonal, $B\bigl(\tfrac12(1+e_2), e_1+e_3\bigr) = 0$; it is therefore totally isotropic. The isometry group $O(2,2)$ acts transitively on each family, and the two families are exchanged by the reflection $e_2 \mapsto -e_2$; each family is the set of images of $L$ under the two connected components of $O(2,2)$, a copy of $\mathrm{SO}^{+}(2,2)/P$ for a maximal parabolic $P$, hence a projective line. The identification of the projectivised cone with $\mathbb{P}^1\times\mathbb{P}^1$ and its two rulings is the standard description of a smooth quadric surface, developed in *Split-Quaternion Null Quadric and Projective Geometry*.

The link of the null cone and the two rulings are the same object seen twice: the two families of lines of the quadric pull back to the two families of circles of the torus $T^2 = S^1 \times S^1$, one circle of each factor for each ruling.

## The Radial Structure and the Null Cone

Every nonzero split-quaternion has the radial decomposition $\tilde q = \rho\, u$ with $\rho = \sqrt{|N(\tilde q)|} > 0$ and $u$ a unit of norm $\pm 1$. The map

$$
\mathbb{H}_{\mathrm{s}} \setminus \{0\} \longrightarrow \mathbb{R}_{>0} \times \{\, u : N(u) = \pm 1 \,\}, \qquad \tilde q \mapsto (\rho, \tilde q/\rho),
$$

is a homeomorphism, and the second factor is the two-sheeted unit slice of *Split-Quaternion Norm and Invertibility*.

**Theorem.** The **boundary of the radial decomposition** is the null cone. As $N(\tilde q) \to 0$ with $\tilde q$ fixed and nonzero, the modulus $\rho \to 0$ while the unit part $\tilde q/\rho$ leaves every compact set of the unit slice; the radial map does not extend continuously to $\mathcal{N}$, and its image is an open dense subset whose complement is $\mathcal{N}$.

**Proof.** The modulus is continuous and vanishes exactly on the null cone, where the normalisation $\tilde q/\rho$ is undefined. Along a path to a nonzero null point the unit part is unbounded because $\rho \to 0$ with $|\tilde q|_E$ bounded below. The identity above shows the polar map is a homeomorphism onto its image, which is the complement of the cone.

The unit slice of the second factor has two connected components, $\{N=1\} \cong S^1\times\mathbb{R}^2$ and $\{N=-1\}$, corresponding to the two components of the group of units; the radial decomposition separates the scale $\rho \in \mathbb{R}_{>0}$ from the direction, itself split into the two component types.

## Comparison with the Topology of $\mathbb{B}$

The biquaternion article *The Topology of the Zero-Divisor Cone* treats the eight-dimensional algebra $\mathbb{B}$, its Euclidean unit sphere $S^7$, the null cone of the complex quadratic form and the reality conditions on the pure biquaternions. The split-quaternion picture is the four-dimensional real analogue. The algebra is $\mathbb{R}^4$ in place of $\mathbb{R}^8$, with Euclidean sphere $\Sigma^3 = S^3$ in place of $S^7$; the group of units $\{N \neq 0\}$ has **two** components (retracting onto two circles) where the biquaternion unit group is connected; the norm-one group retracts onto the circle $SO(2)$ with infinite cyclic fundamental group, where the biquaternion norm-one group retracts onto the simply connected $SU(2)$; and the link of the null cone is the torus $T^2$, of the same type as the biquaternion link because both come from a quadric of split type, but realised in one real dimension less. The two rulings and the two-component structure of the units are the topological shadow of the indefinite form; nothing biquaternion-specific — no complex structure, no Hermitian reality condition, no $S^7$ — is imported.

## Summary

The split-quaternion algebra is $\mathbb{R}^4$ and is contractible, so its only interesting topology is that of the level sets of the split-quaternion norm. The group of units $\{N \neq 0\}$ has two components, $\{N>0\}$ and $\{N<0\}$, each homotopy equivalent to a circle; the norm-one group $U = \mathrm{SL}_2(\mathbb{R})$ is connected, diffeomorphic to $S^1 \times \mathbb{R}^2$ and homotopy equivalent to $S^1$, with $\pi_1 = \mathbb{Z}$, so the double cover $U \to \mathrm{SO}^{+}(2,1)$ is not the universal cover. The null cone $\mathcal{N} = \{q_0^2+q_1^2=q_2^2+q_3^2\}$ is a cone on its link, which is the torus $T^2 = S^1\times S^1$, and its maximal isotropic subspaces are the two families of planes, each parametrised by a circle and each corresponding to one ruling of the smooth projective quadric. The radial decomposition $\tilde q = \rho u$ is a homeomorphism from the punctured algebra onto $\mathbb{R}_{>0}$ times the two-sheeted unit slice, and its boundary is the null cone, where the modulus vanishes and the unit part escapes to infinity. Compared with the biquaternion topology the dimension drops by four, the group of units splits into two components, the norm-one group acquires infinite cyclic fundamental group, and the Euclidean sphere is $S^3$ in place of $S^7$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ | the split-quaternion algebra, contractible | *Split-Quaternion Algebra* |
| $N = q_0^2+q_1^2-q_2^2-q_3^2$ | the split-quaternion norm, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |
| $\mathbb{H}_{\mathrm{s}}^\times = \{N \neq 0\}$ | the group of units, two components | this article |
| $U = \{N = 1\} = \mathrm{SL}_2(\mathbb{R})$ | the norm-one group, $\simeq S^1$ | *Split-Quaternion Exponential and Lie Group Structure* |
| $\mathcal{N} = \{N=0\}$ | the null cone / zero-divisor set | *Split-Quaternion Zero Divisors* |
| $\mathcal{N} \cap \Sigma^3 = T^2$ | the link of the null cone, a torus | this article |
| $\Sigma^3$, $|\tilde q|_E$ | the Euclidean unit sphere and norm of $\mathbb{R}^4$ | this article |
| $L_{(s:t)}, M_{(u:v)}$ | the two families of maximal isotropic planes | *Split-Quaternion Null Quadric and Projective Geometry* |
| $Q \subset \mathbb{P}^3$ | the projective null quadric, $\cong \mathbb{P}^1\times\mathbb{P}^1$ | *Split-Quaternion Null Quadric and Projective Geometry* |
| $\rho u$ | the radial decomposition; boundary the null cone | this article |
| $\mathrm{SO}^{+}(2,1)$ | the Lorentz group double-covered by $U$ | *Split-Quaternion Rotations and the Lorentz Group* |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the homotopy type of matrix groups and the homotopy groups of spheres.
- Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33 (Springer, 1976), for level sets of regular values and the link of a cone singularity.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the deformation retractions of the classical matrix groups onto their maximal compact subgroups.
- Joe Harris, *Algebraic Geometry: A First Course*, Graduate Texts in Mathematics 133 (Springer, 1992), for the two rulings of a smooth quadric surface and the Segre embedding.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the isotropic subspaces and the quadric of an indefinite form.
