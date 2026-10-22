
# __Split-Complex Topology__

## Introduction

This article collects the topology of the split-complex algebra $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ as a space: its contractibility as $\mathbb{R}^2$, its Euclidean unit circle, its null cone as a pair of lines, the link of the null cone, the topology of the group of units and its four components, the deformation retract of the complement of the null cone, and the null cone as the frontier of the four sign classes of $\mathbb{D}^\times$. It is the two-dimensional counterpart of the higher-dimensional zero-divisor cones, and the degeneration is complete: the null cone drops from a real hypersurface to two lines, its link from a connected manifold to four points, and the group of units from connected to four components.

The article uses the algebra of *Split-Complex Algebra*, the norm $\langle Q\rangle_{*}=q^2-q'^2$ and the invertibility criterion of *Split-Complex Norm and Invertibility*, the zero-divisor set of *Split-Complex Zero Divisors*, the idempotents of *Split-Complex Idempotents and Projections*, and the group structure of *Split-Complex Exponential and Lie Group Structure*. No physics is invoked and no new result is claimed.

**Scope.** The topology of the **group of units** beyond its component count — the exponential, the Lie correspondence and the homotopy of the components — is treated in *Split-Complex Exponential and Lie Group Structure*; the component count of $\mathbb{D}^\times$ is in *Split-Complex Norm and Invertibility*; this article owns the ambient space and its distinguished subsets, and takes the component structure of $\mathbb{D}^\times$ from those articles for the comparison. The null quadric of the norm as a projective object is the subject of *Split-Complex Null Quadric and Projective Geometry*.

**Conventions.** The basis is $1$, $j$ with $j^2=+1$; $Q=q+jq'$ with $q,q'\in\mathbb{R}$; conjugate $\bar Q=q-jq'$; idempotents $\Pi_\pm=\tfrac12(1\pm j)$; idempotent coordinates $Q_\pm=q\pm q'$. The norm is $\langle Q\rangle_{*}=q^2-q'^2$, the units are $\mathbb{D}^\times=\{\langle Q\rangle_{*}\neq 0\}$, and the Euclidean norm is $\lVert Q\rVert_E=(q^2+q'^2)^{1/2}$.

## The Algebra as a Topological Space

The real basis $\{1,j\}$ gives a linear isometry

$$
Q=q+jq' \longmapsto (q,q')
$$

of $(\mathbb{D},\lVert\cdot\rVert_E)$ onto $\mathbb{R}^2$. So the topology of $\mathbb{D}$ is the Euclidean topology of the plane. The product is bilinear, hence continuous, so $\mathbb{D}$ is a topological algebra over $\mathbb{R}$; inversion is continuous on the units, so $\mathbb{D}^\times$ is a topological group.

**Theorem (contractibility).** The algebra is contractible, hence path-connected and simply connected, with $\pi_n(\mathbb{D})=0$ for all $n\geq 1$.

**Proof.** The straight-line homotopy $H(t,Q)=(1-t)Q$, $t\in[0,1]$, is continuous with $H(0,Q)=Q$ and $H(1,Q)=0$, so the identity of $\mathbb{D}$ is homotopic to the constant map at $0$.

Every map into $\mathbb{D}$ is therefore null-homotopic, and by the same homotopy the distinguished lines are contractible:

$$
\mathbb{R}_{\mathbb{D}}\cong\mathbb{R},\qquad j\mathbb{R}_{\mathbb{D}}\cong\mathbb{R},\qquad \mathbb{R}\Pi_+\cong\mathbb{R},\qquad \mathbb{R}\Pi_-\cong\mathbb{R}.
$$

So none of the four lines of *Split-Complexoid Subspaces* carries topology beyond that of a point; the geometry of the form comes from the restricted quadratic form and not from the topology.

## The Euclidean Unit Circle

**Definition.** The **Euclidean unit circle** is

$$
S^1_E=\{Q\in\mathbb{D}:\lVert Q\rVert_E=1\}=\{(q,q'):q^2+q'^2=1\}\cong S^1,
$$

a closed, compact, connected $1$-manifold.

The circle is the wrong object here. Multiplication does not preserve $\lVert\cdot\rVert_E$, and $S^1_E$ is not contained in the units. Indeed the null cone meets the circle where $q^2=q'^2$ and $q^2+q'^2=1$, that is at the four points

$$
S^1_E\cap\mathcal{N}=\Bigl\{\pm\tfrac{1}{\sqrt2}(1+j),\ \pm\tfrac{1}{\sqrt2}(1-j)\Bigr\}=\bigl\{\pm\sqrt2\,\Pi_+,\ \pm\sqrt2\,\Pi_-\bigr\},
$$

each of which has $\lVert\cdot\rVert_E=1$ and $\langle Q\rangle_{*}=0$, hence is a zero divisor. So

$$
S^1_E\not\subseteq\mathbb{D}^\times,
$$

the field $\mathbb{C}$ is the definite exception, where $S^1\subseteq\mathbb{C}^\times$. The level set that *is* a subgroup of $\mathbb{D}^\times$ is $\langle Q\rangle_{*}=1$, not $\lVert\cdot\rVert_E=1$: the norm-one group $\mathbb{D}^{(1)}$ of *Split-Complex Exponential and Lie Group Structure*.

## The Null Cone

**Definition.** The **null cone**, or singular set, is

$$
\mathcal{N}=\{Q\in\mathbb{D}:\langle Q\rangle_{*}=0\}=\{Q:q^2=q'^2\}=\{q=q'\}\cup\{q=-q'\},
$$

the union of the two **null lines** $\mathbb{R}(1+j)$ and $\mathbb{R}(1-j)$, equivalently the union of the two idempotent lines $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$.

**Theorem.** The null cone is a closed real algebraic cone with apex $0$, of real dimension $1$, with empty interior; it is the union of two distinct lines through the origin, is a real $1$-manifold away from the apex, and is singular at the apex. Its complement $\mathbb{D}\setminus\mathcal{N}=\mathbb{D}^\times$ is dense and open.

**Proof.** The form $\langle q,q'\rangle_{*}=q^2-q'^2=(q-q')(q+q')$ is homogeneous of degree $2$, so $\mathcal{N}$ is a cone; it is closed, being the zero set of a polynomial. It factors into the two linear factors $q-q'=0$ and $q+q'=0$, whose zero sets are the two distinct lines of slope $\pm1$, each of real dimension $1$; hence $\mathcal{N}$ has real dimension $1$ and empty interior (a finite union of lines contains no open set). Each line is a real $1$-manifold through $0$, but their union is not a manifold at $0$, where the two branches cross. The complement of a closed set of empty interior is open and dense.

The differentiability statement that each line is smooth at its non-apex points, equivalently that the cone is smooth away from the apex, is analytic and is in *Split-Complex Analysis*.

**Remark (the zero divisors).** The null cone is exactly the zero-divisor set $\mathcal{Z}=\mathcal{N}\setminus\{0\}$ together with the origin, $\mathcal{N}=\{0\}\cup\mathcal{Z}$; on the two lines the factorisations $(q+j q')(q-j q')=\langle Q\rangle_{*}=0$ exhibit the zero divisors, and the classification of the families is the subject of *Split-Complex Zero Divisors*.

**Contractibility.** The homotopy $K(s,Q)=(1-s)Q$ maps $[0,1]\times\mathcal{N}$ into $\mathcal{N}$, since scaling preserves nullity, and contracts the pair of lines to the apex. The null cone is thus contractible, like the algebra, but is a singular subset of it.

## The Link of the Null Cone

**Definition.** The **link** of the null cone is $L=\mathcal{N}\cap S^1_E$.

**Theorem.** The link is the four-point set

$$
L=\Bigl\{\pm\tfrac1{\sqrt2}(1+j),\ \pm\tfrac1{\sqrt2}(1-j)\Bigr\}\cong 4\ \text{points},
$$

a closed, compact $0$-manifold with $\pi_0(L)$ of order $4$ and $\pi_n(L)=0$ for all $n\geq 1$. The null cone is the cone on $L$, and the projectivised null cone is the two-point set

$$
\mathbb{P}(\mathcal{N})=\{\mathbb{R}(1+j),\ \mathbb{R}(1-j)\}\cong 2\ \text{points},
$$

the two null directions.

**Proof.** A point of $\mathcal{N}$ with $\lVert\cdot\rVert_E=1$ satisfies $q^2=q'^2$ and $q^2+q'^2=1$, so $2q^2=1$, $q=\pm 1/\sqrt2$ and $q'=\pm q$ with the two signs matched by $q=\pm q'$; this gives the four listed points. Since the null cone is the union of two lines, its projectivisation, the set of its lines, has two elements.

**Remark (the link).** Here the link of the null cone is four points, and the null cone of $\mathbb{D}$ is a union of linear subspaces rather than a nonsingular real hypersurface.

## The Group of Units and Its Components

**Definition.** The **group of units** is $\mathbb{D}^\times=\{Q:\langle Q\rangle_{*}\neq 0\}=\mathbb{D}\setminus\mathcal{N}$, with the multiplication of the algebra.

**Theorem.** The complement of the null cone in the plane is the disjoint union of the four open sectors

$$
\mathbb{D}^\times=(\mathbb{D}^\times)_0\ \sqcup\ -(\mathbb{D}^\times)_0\ \sqcup\ \Sigma_+\ \sqcup\ \Sigma_-,
$$

with

$$
(\mathbb{D}^\times)_0=\{q>\lvert q'\rvert\},\qquad -(\mathbb{D}^\times)_0=\{q<-\lvert q'\rvert\},\qquad \Sigma_+=\{q'>\lvert q\rvert\},\qquad \Sigma_-=\{q'<-\lvert q\rvert\},
$$

each homeomorphic to $\mathbb{R}^2$, hence contractible. Consequently

$$
\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times,\qquad \pi_0(\mathbb{D}^\times)\cong(\mathbb{Z}/2)^2,\qquad \pi_n(\mathbb{D}^\times)=0\ \ (n\geq 1).
$$

**Proof.** The two lines $q=\pm q'$ divide $\mathbb{R}^2$ into the four open sectors above, determined by the signs of $Q_+=q+q'$ and $Q_-=q-q'$; each sector is a convex open cone, hence homeomorphic to $\mathbb{R}^2$ and contractible. Under the idempotent coordinates $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$, the four sectors are the four components of the product of two two-component groups, giving the component group $(\mathbb{Z}/2)^2$. A disjoint union of contractible spaces has vanishing homotopy in positive degrees.

**Remark.** This is the sharpest topological contrast with the complex field: $\mathbb{C}^\times$ is connected, with $\pi_1(\mathbb{C}^\times)\cong\mathbb{Z}$, while $\mathbb{D}^\times$ has four components and all its positive homotopy groups vanish. The four components are the analogue of the four components of the same algebra over $\mathbb{R}$ seen in *Split-Complex Exponential and Lie Group Structure*, and the identity component $(\mathbb{D}^\times)_0$ is the image of the exponential.

## The Deformation Retract of the Complement

**Definition.** The **unit-modulus set** of $\mathbb{D}$ is

$$
\mathbb{D}^{(\pm1)}=\{Q:\lvert \langle Q\rangle_{*}\rvert=1\}=\mathbb{D}^{(1)}\cup(-\mathbb{D}^{(1)}),
$$

the union of the four **hyperbola branches**

$$
\{q=\pm\cosh t,\ q'=\sinh t\},\qquad \{q=\sinh t,\ q'=\pm\cosh t\},\qquad t\in\mathbb{R}.
$$

**Theorem (deformation retraction).** The complement $\mathbb{D}^\times$ of the null cone deformation retracts onto the unit-modulus set $\mathbb{D}^{(\pm1)}$, by the homotopy

$$
H(s,Q)=Q\Bigl((1-s)+\frac{s}{\rho(Q)}\Bigr),\qquad \rho(Q)=\sqrt{\lvert \langle Q\rangle_{*}\rvert}>0,
$$

which is continuous on $[0,1]\times\mathbb{D}^\times$, fixes $\mathbb{D}^{(\pm1)}$ pointwise, and satisfies $H(0,Q)=Q$ and $H(1,Q)=Q/\rho(Q)\in\mathbb{D}^{(\pm1)}$.

**Proof.** For $Q\in\mathbb{D}^\times$ the modulus $\rho(Q)>0$ is continuous and nonzero, so $H$ is continuous; scaling $Q$ by the real number $(1-s)+s/\rho(Q)>0$ multiplies $\langle\cdot\rangle_{*}$ by its square, which is nonzero, so $H$ takes values in $\mathbb{D}^\times$. At $s=1$ the factor is $1/\rho(Q)$ and $\lvert \langle Q/\rho(Q)\rangle_{*}\rvert=\lvert \langle Q\rangle_{*}\rvert/\rho(Q)^2=1$, so the image lies in $\mathbb{D}^{(\pm1)}$; at $s=0$ the factor is $1$, so $H(0,Q)=Q$, and on $\mathbb{D}^{(\pm1)}$ the factor is $1$ for every $s$, so that set is fixed pointwise throughout.

**Corollary.** Each of the four branches of $\mathbb{D}^{(\pm1)}$ is homeomorphic to $\mathbb{R}$ and contractible, so $\mathbb{D}^\times$ is homotopy equivalent to the four-point space $\pi_0(\mathbb{D}^\times)$; in particular $\pi_1(\mathbb{D}^\times)=0$, and the complement of the null cone has the homotopy type of four isolated points.

**Remark (the definite analogue).** For the complex field the same construction retracts $\mathbb{C}^\times$ onto the unit circle $S^1$, a connected $1$-manifold, so $\mathbb{C}^\times$ is homotopy equivalent to $S^1$ with $\pi_1\cong\mathbb{Z}$. Replacing the definite level set $q^2+q'^2=1$ by the indefinite level set $q^2-q'^2=\pm1$ turns one circle into four lines: the transverse intersection of the level set with a Euclidean sphere becomes the pair of null lines, and the fundamental group is killed.

## The Null Cone as a Frontier

The null cone is the frontier of each of the four sign classes of $\mathbb{D}^\times$: every neighbourhood of a point of $\mathcal{N}$ meets exactly two of the four components, and $\mathcal{N}$ contains no point of any component, so the cone is a closed set of empty interior that separates them. In the idempotent coordinates a point approaches the cone exactly when one of its two coordinates tends to zero, and the two coordinates are the two independent real parameters of *Split-Complex Algebra*.

The polar parametrisation of a unit, $Q=\rho u$ with modulus $\rho=\lvert \langle Q\rangle_{*}\rvert^{1/2}>0$ and direction $u=Q/\rho$ of unit modulus, is defined on $\mathbb{D}^\times$ and degenerates on $\mathcal{N}$: the modulus vanishes there and the direction is undefined. That parametrisation, its two regimes and the behaviour of its angle as the cone is approached are the subject of *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*; the cone read geometrically, as a pair of asymptotic directions, is in *Hyperbolic Rotations*.

## Summary

The split-complex algebra is $\mathbb{R}^2$, hence contractible, path-connected and simply connected; its product and inversion are continuous, so it is a topological algebra and $\mathbb{D}^\times$ is a topological group. The Euclidean unit circle $S^1_E$ is a compact $1$-manifold but is not contained in the units: it meets the null cone in four points, so $S^1_E\not\subseteq\mathbb{D}^\times$. The null cone $\mathcal{N}=\{\langle Q\rangle_{*}=0\}$ is the union of the two null lines $q=\pm q'$, a closed real algebraic cone of real dimension $1$, a real $1$-manifold off the apex and singular at the apex, contractible, and with empty interior. Its link is the four-point set $\{\pm\sqrt2\,\Pi_+,\pm\sqrt2\,\Pi_-\}$, and its projectivisation is the two null directions.

The group of units $\mathbb{D}^\times=\mathbb{D}\setminus\mathcal{N}\cong(\mathbb{R}^\times)^2$ has four contractible components, the four open sectors cut out by the null lines, so $\pi_0\cong(\mathbb{Z}/2)^2$ and $\pi_n=0$ for $n\geq1$; the complement of the null cone deformation retracts onto the unit-modulus set $\mathbb{D}^{(\pm1)}$, four hyperbola branches each homeomorphic to $\mathbb{R}$, so $\mathbb{D}^\times$ has the homotopy type of four points. The null cone is the frontier of the four components of $\mathbb{D}^\times$: every neighbourhood of a point of $\mathcal{N}$ meets exactly two of them. The null cone is a pair of lines, its link is four points, and the group of units has four contractible components.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}\cong\mathbb{R}^2$ | Split complex algebra as a topological space; contractible |
| $\lVert Q\rVert_E=(q^2+q'^2)^{1/2}$ | Euclidean norm; topological algebra |
| $S^1_E=\{\lVert Q\rVert_E=1\}$ | Euclidean unit circle; not contained in the units |
| $\langle Q\rangle_{*}=q^2-q'^2$ | Norm |
| $\mathcal{N}=\{\langle Q\rangle_{*}=0\}$ | Null cone; the two lines $q=\pm q'$; contractible, singular at $0$ |
| $L=\mathcal{N}\cap S^1_E$ | Link of the null cone; four points |
| $\mathbb{P}(\mathcal{N})$ | Projectivised null cone; the two null directions |
| $\mathbb{D}^\times=\mathbb{D}\setminus\mathcal{N}$ | Group of units; four contractible components |
| $(\mathbb{D}^\times)_0=\{q>\lvert q'\rvert\}$ | Identity component |
| $\Sigma_+=\{q'>\lvert q\rvert\}$, $\Sigma_-=\{q'<-\lvert q\rvert\}$ | The two components of negative norm |
| $\rho(Q)=\sqrt{\lvert \langle Q\rangle_{*}\rvert}$ | Modulus |
| $\mathbb{D}^{(\pm1)}=\{\lvert \langle Q\rangle_{*}\rvert=1\}$ | Unit-modulus set; four hyperbola branches, the deformation retract |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Idempotents, spanning the null lines |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for contractibility, homotopy type, links of cones and the fundamental group.
- William Fulton, *Algebraic Topology: A First Course* (Springer, Graduate Texts in Mathematics 153, 1995), for the deformation retraction of quadric complements and low-dimensional examples.
- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the topology of low-dimensional matrix and abelian Lie groups.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic geometry of the split complex plane and its asymptotes.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex algebra, its isotropic lines and its unit group.
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, Graduate Texts in Mathematics 98, 1985), for the topology of matrix groups and their maximal compact subgroups.
