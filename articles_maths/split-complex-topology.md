
# __Split-Complex Topology__

## Introduction

This article collects the topology of the split-complex algebra $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ as a space: its contractibility as $\mathbb{R}^2$, its Euclidean unit circle, its null cone as a pair of lines, the link of the null cone, the topology of the group of units and its four components, the deformation retract of the complement of the null cone, and the null cone as the boundary of the polar decomposition. It is the two-dimensional counterpart of *Biquaternion Topology*, and the degeneration is complete: the null cone drops from a six-dimensional real hypersurface to two lines, its link from a connected $5$-manifold to four points, and the group of units from the connected $GL(2,\mathbb{C})$ to a four-component group.

The article uses the algebra of *Split-Complex Algebra*, the norm form $N(Z)=a^2-b^2$ and the invertibility criterion of *Split-Complex Norm and Invertibility*, the zero-divisor set of *Split-Complex Zero Divisors*, the idempotents of *Split-Complex Idempotents and Projections*, and the group structure of *Split-Complex Exponential and Lie Group Structure*. No physics is invoked and no new result is claimed.

**Scope.** The topology of the **group of units** beyond its component count — the exponential, the Lie correspondence and the homotopy of the components — is treated in *Split-Complex Exponential and Lie Group Structure*; this article owns the ambient space and its distinguished subsets, and takes the component structure of $\mathbb{D}^\times$ from that article for the comparison. The null quadric of the norm form as a projective object is the subject of *Split-Complex Null Quadric and Projective Geometry*.

**Conventions.** The basis is $1$, $j$ with $j^2=+1$; $Z=a+j b$ with $a,b\in\mathbb{R}$; conjugate $\bar Z=a-j b$; idempotents $\Pi_\pm=\tfrac12(1\pm j)$; idempotent coordinates $Z_\pm=a\pm b$. The norm form is $N(Z)=a^2-b^2$, the units are $\mathbb{D}^\times=\{N\neq 0\}$, and the Euclidean norm is $\lVert Z\rVert_E=(a^2+b^2)^{1/2}$.

## The Algebra as a Topological Space

The real basis $\{1,j\}$ gives a linear isometry

$$
Z=a+j b \longmapsto (a,b)
$$

of $(\mathbb{D},\lVert\cdot\rVert_E)$ onto $\mathbb{R}^2$. So the topology of $\mathbb{D}$ is the Euclidean topology of the plane. The product is bilinear, hence continuous, so $\mathbb{D}$ is a topological algebra over $\mathbb{R}$; inversion is continuous on the units, so $\mathbb{D}^\times$ is a topological group.

**Theorem (contractibility).** The algebra is contractible, hence path-connected and simply connected, with $\pi_n(\mathbb{D})=0$ for all $n\geq 1$.

**Proof.** The straight-line homotopy $H(t,Z)=(1-t)Z$, $t\in[0,1]$, is continuous with $H(0,Z)=Z$ and $H(1,Z)=0$, so the identity of $\mathbb{D}$ is homotopic to the constant map at $0$. $\square$

Every map into $\mathbb{D}$ is therefore null-homotopic, and by the same homotopy the distinguished lines are contractible:

$$
\mathbb{R}_{\mathbb{D}}\cong\mathbb{R},\qquad j\mathbb{R}_{\mathbb{D}}\cong\mathbb{R},\qquad \mathbb{R}\Pi_1\cong\mathbb{R},\qquad \mathbb{R}\Pi_2\cong\mathbb{R}.
$$

So none of the four lines of *Split-Complex Subspaces* carries topology beyond that of a point; the geometry of the form comes from the restricted quadratic form and not from the topology.

## The Euclidean Unit Circle

**Definition.** The **Euclidean unit circle** is

$$
S^1_E=\{Z\in\mathbb{D}:\lVert Z\rVert_E=1\}=\{(a,b):a^2+b^2=1\}\cong S^1,
$$

a closed, compact, connected $1$-manifold.

The circle is the wrong object here, exactly as the sphere is for the biquaternion algebra. Multiplication does not preserve $\lVert\cdot\rVert_E$, and $S^1_E$ is not contained in the units. Indeed the null cone meets the circle where $a^2=b^2$ and $a^2+b^2=1$, that is at the four points

$$
S^1_E\cap\mathcal{N}=\Bigl\{\pm\tfrac{1}{\sqrt2}(1+j),\ \pm\tfrac{1}{\sqrt2}(1-j)\Bigr\}=\bigl\{\pm\sqrt2\,\Pi_1,\ \pm\sqrt2\,\Pi_2\bigr\},
$$

each of which has $\lVert\cdot\rVert_E=1$ and $N=0$, hence is a zero divisor. So

$$
S^1_E\not\subseteq\mathbb{D}^\times,
$$

as for $\mathbb{B}$; the field $\mathbb{C}$ is the definite exception, where $S^1\subseteq\mathbb{C}^\times$. The level set that *is* a subgroup of $\mathbb{D}^\times$ is $N=1$, not $\lVert\cdot\rVert_E=1$: the norm-one group $\mathbb{D}^{(1)}$ of *Split-Complex Exponential and Lie Group Structure*.

## The Null Cone

**Definition.** The **null cone**, or singular set, is

$$
\mathcal{N}=\{Z\in\mathbb{D}:N(Z)=0\}=\{Z:a^2=b^2\}=\{a=b\}\cup\{a=-b\},
$$

the union of the two **null lines** $\mathbb{R}(1+j)$ and $\mathbb{R}(1-j)$, equivalently the union of the two idempotent lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$.

**Theorem.** The null cone is a closed real algebraic cone with apex $0$, of real dimension $1$, with empty interior; it is the union of two distinct lines through the origin, is smooth away from the apex, and is singular at the apex. Its complement $\mathbb{D}\setminus\mathcal{N}=\mathbb{D}^\times$ is dense and open.

**Proof.** The form $N(a,b)=a^2-b^2=(a-b)(a+b)$ is homogeneous of degree $2$, so $\mathcal{N}$ is a cone; it is closed, being the zero set of a polynomial. It factors into the two linear factors $a-b=0$ and $a+b=0$, whose zero sets are the two distinct lines of slope $\pm1$, each of real dimension $1$; hence $\mathcal{N}$ has real dimension $1$ and empty interior (a finite union of lines contains no open set). Each line is a smooth $1$-manifold through $0$, but their union is not a manifold at $0$, where the two branches cross. The complement of a closed set of empty interior is open and dense. $\square$

**Remark (the zero divisors).** The null cone is exactly the zero-divisor set $\mathcal{Z}=\mathcal{N}\setminus\{0\}$ together with the origin, $\mathcal{N}=\{0\}\cup\mathcal{Z}$; on the two lines the factorisations $(a+j b)(a-j b)=N(Z)=0$ exhibit the zero divisors, and the classification of the families is the subject of *Split-Complex Zero Divisors*.

**Contractibility.** The homotopy $K(s,Z)=(1-s)Z$ maps $[0,1]\times\mathcal{N}$ into $\mathcal{N}$, since scaling preserves nullity, and contracts the pair of lines to the apex. The null cone is thus contractible, like the algebra, but is a singular subset of it.

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

**Proof.** A point of $\mathcal{N}$ with $\lVert\cdot\rVert_E=1$ satisfies $a^2=b^2$ and $a^2+b^2=1$, so $2a^2=1$, $a=\pm 1/\sqrt2$ and $b=\pm a$ with the two signs matched by $a=\pm b$; this gives the four listed points. Since the null cone is the union of two lines, its projectivisation, the set of its lines, has two elements. $\square$

**Remark (the contrast with the biquaternion link).** The link of the biquaternion null cone is a connected $5$-manifold with $\pi_2\cong\mathbb{Z}$; here the link is four points. The reduction of dimension from $6$ to $1$ and the loss of connectedness both reflect that the null cone of $\mathbb{D}$ is a union of linear subspaces rather than a nonsingular real hypersurface.

## The Group of Units and Its Components

**Definition.** The **group of units** is $\mathbb{D}^\times=\{Z:N(Z)\neq 0\}=\mathbb{D}\setminus\mathcal{N}$, with the multiplication of the algebra.

**Theorem.** The complement of the null cone in the plane is the disjoint union of the four open sectors

$$
\mathbb{D}^\times=(\mathbb{D}^\times)_0\ \sqcup\ -(\mathbb{D}^\times)_0\ \sqcup\ \Sigma_+\ \sqcup\ \Sigma_-,
$$

with

$$
(\mathbb{D}^\times)_0=\{a>\lvert b\rvert\},\qquad -(\mathbb{D}^\times)_0=\{a<-\lvert b\rvert\},\qquad \Sigma_+=\{b>\lvert a\rvert\},\qquad \Sigma_-=\{b<-\lvert a\rvert\},
$$

each homeomorphic to $\mathbb{R}^2$, hence contractible. Consequently

$$
\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times,\qquad \pi_0(\mathbb{D}^\times)\cong(\mathbb{Z}/2)^2,\qquad \pi_n(\mathbb{D}^\times)=0\ \ (n\geq 1).
$$

**Proof.** The two lines $a=\pm b$ divide $\mathbb{R}^2$ into the four open sectors above, determined by the signs of $Z_+=a+b$ and $Z_-=a-b$; each sector is a convex open cone, hence homeomorphic to $\mathbb{R}^2$ and contractible. Under the idempotent coordinates $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$, the four sectors are the four components of the product of two two-component groups, giving the component group $(\mathbb{Z}/2)^2$. A disjoint union of contractible spaces has vanishing homotopy in positive degrees. $\square$

**Remark.** This is the sharpest topological contrast with the complex field: $\mathbb{C}^\times$ is connected, with $\pi_1(\mathbb{C}^\times)\cong\mathbb{Z}$, while $\mathbb{D}^\times$ has four components and all its positive homotopy groups vanish. The four components are the analogue of the four components of the same algebra over $\mathbb{R}$ seen in *Split-Complex Exponential and Lie Group Structure*, and the identity component $(\mathbb{D}^\times)_0$ is the image of the exponential.

## The Deformation Retract of the Complement

**Definition.** The **unit-modulus set** of $\mathbb{D}$ is

$$
\mathbb{D}^{(\pm1)}=\{Z:\lvert N(Z)\rvert=1\}=\mathbb{D}^{(1)}\cup(-\mathbb{D}^{(1)}),
$$

the union of the four **hyperbola branches**

$$
\{a=\pm\cosh t,\ b=\sinh t\},\qquad \{a=\sinh t,\ b=\pm\cosh t\},\qquad t\in\mathbb{R}.
$$

**Theorem (deformation retraction).** The complement $\mathbb{D}^\times$ of the null cone deformation retracts onto the unit-modulus set $\mathbb{D}^{(\pm1)}$, by the homotopy

$$
H(s,Z)=Z\Bigl((1-s)+\frac{s}{\rho(Z)}\Bigr),\qquad \rho(Z)=\sqrt{\lvert N(Z)\rvert}>0,
$$

which is continuous on $[0,1]\times\mathbb{D}^\times$, fixes $\mathbb{D}^{(\pm1)}$ pointwise, and satisfies $H(0,Z)=Z$ and $H(1,Z)=Z/\rho(Z)\in\mathbb{D}^{(\pm1)}$.

**Proof.** For $Z\in\mathbb{D}^\times$ the modulus $\rho(Z)>0$ is continuous and nonzero, so $H$ is continuous; scaling $Z$ by the real number $(1-s)+s/\rho(Z)>0$ multiplies $N$ by its square, which is nonzero, so $H$ takes values in $\mathbb{D}^\times$. At $s=1$ the factor is $1/\rho(Z)$ and $\lvert N(Z/\rho(Z))\rvert=\lvert N(Z)\rvert/\rho(Z)^2=1$, so the image lies in $\mathbb{D}^{(\pm1)}$; at $s=0$ the factor is $1$, so $H(0,Z)=Z$, and on $\mathbb{D}^{(\pm1)}$ the factor is $1$ for every $s$, so that set is fixed pointwise throughout. $\square$

**Corollary.** Each of the four branches of $\mathbb{D}^{(\pm1)}$ is homeomorphic to $\mathbb{R}$ and contractible, so $\mathbb{D}^\times$ is homotopy equivalent to the four-point space $\pi_0(\mathbb{D}^\times)$; in particular $\pi_1(\mathbb{D}^\times)=0$, and the complement of the null cone has the homotopy type of four isolated points.

**Remark (the definite analogue).** For the complex field the same construction retracts $\mathbb{C}^\times$ onto the unit circle $S^1$, a connected $1$-manifold, so $\mathbb{C}^\times$ is homotopy equivalent to $S^1$ with $\pi_1\cong\mathbb{Z}$. Replacing the definite circle $a^2+b^2=1$ by the indefinite hyperbola pair $a^2-b^2=\pm1$ turns one circle into four lines: the transverse intersection of the quadric with a Euclidean sphere becomes the pair of asymptotic lines of the hyperbola, and the fundamental group is killed.

## The Boundary of the Polar Decomposition

The polar decomposition of a unit $Z=\rho u$, with modulus $\rho=\sqrt{\lvert N(Z)\rvert}>0$ and direction $u=Z/\rho$ of unit modulus, is defined on $\mathbb{D}^\times$ and not on $\mathbb{D}$: the modulus vanishes and the direction is undefined exactly on the null cone.

**Proposition.** The null cone is the boundary of the polar decomposition. On the components of positive norm the direction is a hyperbolic rotation $u=e^{j\theta}$, and on those of negative norm it is the boost $u=j\,e^{j\theta}$; in either case, as a point approaches the null cone from within a component, the hyperbolic angle $\theta$ tends to $\pm\infty$.

**Proof.** In the component $\{a>\lvert b\rvert\}$ the direction is $u=e^{j\theta}$ with $\theta=\operatorname{artanh}(b/a)$; as $(a,b)$ approaches the line $a=b$ from inside the sector $a>\lvert b\rvert$, the ratio $b/a\to1^{-}$ and $\theta\to+\infty$, while the line $a=-b$ gives $\theta\to-\infty$. On the components with $N<0$, where the direction is $u=j\,e^{j\theta}$ with the analogous parameter read from $\lvert N\rvert$, the same escape occurs. Hence the polar angle is unbounded toward the boundary, and the boundary is not a circle or a pair of circles but the two null lines on which the parametrisation fails entirely. $\square$

So the polar decomposition is a covering of the plane-without-the-null-cone by an open cylinder-like parameter domain, and the null cone is the asymptote at which it degenerates; this is the topological content of the two regimes of the parametrisation.

## Comparison with the Topology of the Biquaternion Algebra

| object | $\mathbb{B}$ | $\mathbb{D}$ |
|---|---|---|
| ambient space | $\mathbb{R}^8$, contractible | $\mathbb{R}^2$, contractible |
| Euclidean unit sphere | $S^7$, a compact $7$-manifold, not a group | $S^1$, a compact $1$-manifold, not a group |
| sphere inside the units? | no | no (four points of $S^1$ are null) |
| null cone | real dimension $6$ hypersurface, smooth off the apex | real dimension $1$, a pair of lines |
| projectivised null cone | $\mathbb{P}^1\times\mathbb{P}^1$ | two points |
| link of the null cone | connected $5$-manifold, $\pi_1=0$, $\pi_2\cong\mathbb{Z}$ | four points |
| group of units | $GL(2,\mathbb{C})$, connected, $\pi_1\cong\mathbb{Z}$ | $(\mathbb{R}^\times)^2$, four components, $\pi_{\geq1}=0$ |
| deformation retract of the units | $U(2)$ | the unit-modulus set, four lines |

The reduction in dimension is systematic: each object of the four-real-dimensional complex algebra drops by the real codimension of the null cone, from $6$ to $1$, and the connected manifold objects of the biquaternion theory become finite sets or finite unions of lines. The one feature that survives verbatim is the failure of the Euclidean unit sphere to lie in the units; the one that reverses is the group of units, connected and infinite-$\pi_1$ for $\mathbb{B}$ against four contractible components for $\mathbb{D}$.

## Summary

The split-complex algebra is $\mathbb{R}^2$, hence contractible, path-connected and simply connected; its product and inversion are continuous, so it is a topological algebra and $\mathbb{D}^\times$ is a topological group. The Euclidean unit circle $S^1_E$ is a compact $1$-manifold but is not contained in the units: it meets the null cone in four points, so $S^1_E\not\subseteq\mathbb{D}^\times$. The null cone $\mathcal{N}=\{N=0\}$ is the union of the two null lines $a=\pm b$, a closed real algebraic cone of real dimension $1$, smooth off the apex and singular at the apex, contractible, and with empty interior. Its link is the four-point set $\{\pm\sqrt2\,\Pi_1,\pm\sqrt2\,\Pi_2\}$, and its projectivisation is the two null directions.

The group of units $\mathbb{D}^\times=\mathbb{D}\setminus\mathcal{N}\cong(\mathbb{R}^\times)^2$ has four contractible components, the four open sectors cut out by the null lines, so $\pi_0\cong(\mathbb{Z}/2)^2$ and $\pi_n=0$ for $n\geq1$; the complement of the null cone deformation retracts onto the unit-modulus set $\mathbb{D}^{(\pm1)}$, four hyperbola branches each homeomorphic to $\mathbb{R}$, so $\mathbb{D}^\times$ has the homotopy type of four points. The null cone is the boundary of the polar decomposition, on which the modulus vanishes and the hyperbolic angle escapes to infinity. Compared with the biquaternion algebra, the null cone drops from a six-dimensional hypersurface to a pair of lines, its link from a connected $5$-manifold to four points, and the group of units from the connected $GL(2,\mathbb{C})$ with $\pi_1\cong\mathbb{Z}$ to four contractible components.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}\cong\mathbb{R}^2$ | Split complex algebra as a topological space; contractible |
| $\lVert Z\rVert_E=(a^2+b^2)^{1/2}$ | Euclidean norm; topological algebra |
| $S^1_E=\{\lVert Z\rVert_E=1\}$ | Euclidean unit circle; not contained in the units |
| $N(Z)=a^2-b^2$ | Norm form |
| $\mathcal{N}=\{N=0\}$ | Null cone; the two lines $a=\pm b$; contractible, singular at $0$ |
| $L=\mathcal{N}\cap S^1_E$ | Link of the null cone; four points |
| $\mathbb{P}(\mathcal{N})$ | Projectivised null cone; the two null directions |
| $\mathbb{D}^\times=\mathbb{D}\setminus\mathcal{N}$ | Group of units; four contractible components |
| $(\mathbb{D}^\times)_0=\{a>\lvert b\rvert\}$ | Identity component |
| $\Sigma_+=\{b>\lvert a\rvert\}$, $\Sigma_-=\{b<-\lvert a\rvert\}$ | The two components of negative norm form |
| $\rho(Z)=\sqrt{\lvert N(Z)\rvert}$ | Modulus |
| $\mathbb{D}^{(\pm1)}=\{\lvert N\rvert=1\}$ | Unit-modulus set; four hyperbola branches, the deformation retract |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Idempotents, spanning the null lines |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for contractibility, homotopy type, links of cones and the fundamental group.
- William Fulton, *Algebraic Topology: A First Course* (Springer, Graduate Texts in Mathematics 153, 1995), for the deformation retraction of quadric complements and low-dimensional examples.
- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the topology of low-dimensional matrix and abelian Lie groups.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic geometry of the split complex plane and its asymptotes.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex algebra, its isotropic lines and its unit group.
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, Graduate Texts in Mathematics 98, 1985), for the topology of matrix groups and their maximal compact subgroups.
