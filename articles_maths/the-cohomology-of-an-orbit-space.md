# __The Cohomology of an Orbit Space__

## Introduction

The orbit space $Q = X/\sigma$ of a space with an involution is the quotient that identifies each point with its image, and its cohomology is governed by two comparisons: the pullback $\pi^*$ from the quotient to the space, which lands in the invariant classes, and the map from the quotient into the homotopy quotient, which compares the orbit space with the equivariant cohomology. The two comparisons coincide exactly for a free action, where the quotient is a double cover; away from that case they separate, and the difference is precisely the fixed set. The orbit space is therefore the object on which the general theory of the involution is read off: the invariants of the cohomology of the space compute the quotient when the coefficient field has characteristic different from two, the mod 2 quotient is computed by the **Cartan–Leray spectral sequence** with coefficients in the cohomology of the space as a module over the group, and the kernel of the pullback measures the classes that the quotient cannot see.

The article develops the cohomology of the orbit space. It defines the orbit space and the projection and records the functoriality, states the two comparisons and the transfer identities that relate the pullback to the invariants, proves Grothendieck's theorem that over a field in which two is invertible the quotient cohomology is the invariant cohomology, gives the Cartan–Leray spectral sequence for the mod 2 quotient and identifies the comparison with the equivariant cohomology as an isomorphism exactly for the free action, describes the kernel of the pullback and its relation to the fixed set, and closes with the examples of the spheres, the projective spaces and the interval. The orbit space and the double cover are those of *Two-Fold Coverings and the Borel Construction*; the transfer and its identities are those of *The Transfer and the Involution* and *The Gysin Sequence of a Two-Fold Covering*; the equivariant cohomology and the Borel construction are those of *Equivariant Cohomology*; the fixed set and the Smith theory are those of *The Mod 2 Cohomology of an Involution* and *Smith Theory and the Fixed Sets of Periodic Maps*; and the spectral sequence is that of *The Leray–Serre Spectral Sequence*. Nothing analytic and nothing geometric is used.

Throughout, $(X,\sigma)$ is a space with an involution, $Q = X/\sigma$ is its **orbit space**, and $\pi : X\to Q$ is the quotient, a continuous, open, surjective map with $\pi\sigma = \pi$; the fixed set is $F = X^{\sigma}$, on which $\pi$ is a homeomorphism onto its image. The coefficient field is written $k$, most often $k = \mathbb{F}_2 = \mathbb{Z}/2$ or a field of characteristic not two, and all cohomology is singular cohomology of the indicated space with coefficients in $k$. The invariants of the action on cohomology are written $H^*(X;k)^{\sigma}$, and the norm is $1+\sigma^*$. The homotopy quotient $X_{\mathbb{Z}/2}$ and the equivariant cohomology $H_{\mathbb{Z}/2}^*(X)$ are those of *Equivariant Cohomology*.

## The Orbit Space and the Projection

### The Quotient Map

**Definition.** The **orbit space** of the involution is the quotient $Q = X/\sigma$ of $X$ by the equivalence relation $x\sim\sigma x$, with the quotient topology, and the **projection** is the quotient map $\pi : X\to Q$.

**Proposition.** The projection is continuous, open and surjective, and it is a homeomorphism from the fixed set $F$ onto its image; the pair $(\pi,Q)$ is characterised by the universal property that a continuous map $f : X\to Y$ with $f\sigma = f$ factors uniquely as $f = \bar f\circ\pi$ for a continuous $\bar f : Q\to Y$. The construction is functorial: an equivariant map $X\to X'$ induces a continuous map $Q\to Q'$, and an equivariant homotopy induces a homotopy.

*Proof.* The quotient map of a group action is open and continuous by the definition of the quotient topology; on the fixed set the projection is a bijection onto its image with continuous inverse because the intersection of the fixed set with a saturated open set is open; the universal property and the functoriality are the standard ones for a quotient. $\square$

### The Free Part

**Theorem.** The involution restricts to a free involution of the complement $X\setminus F$, on which the projection is a two-fold covering, and the quotient $Q$ is the union of the double cover $\pi : X\setminus F\to Q\setminus \pi(F)$ and the closed copy of the fixed set; the projection is a double cover over exactly the complement of $\pi(F)$, and it is a homeomorphism over $\pi(F)$. The quotient is a topological manifold when $X$ is one and the action is free, and at the fixed set the quotient is the orbit space of the linear isotropy action on the normal directions.

*Proof.* A point is fixed exactly when its orbit is a single point, so on the complement every orbit has two points and the projection is a double cover there; the fixed set maps homeomorphically, and the local structure at a fixed point is the quotient of a neighbourhood by the linear involution, by the slice theorem of *Equivariant Homotopy Theory*. $\square$

## The Two Comparisons

### The Pullback from the Quotient

**Theorem.** The pullback of the projection is a ring homomorphism

$$
\pi^* : H^*(Q;k) \longrightarrow H^*(X;k), \qquad \pi^*(\bar\alpha) = \bar\alpha\circ\pi ,
$$

whose image is contained in the invariants, $\sigma^*\pi^* = \pi^*$; on the fixed set the pullback is the restriction, and the pullback is natural for equivariant maps.

*Proof.* The pullback is the map on cohomology induced by the continuous map $\pi$, hence a ring homomorphism, and $\pi\sigma=\pi$ gives $\sigma^*\pi^*=\pi^*$; the restriction statement is that $\pi$ is a homeomorphism on the fixed set. $\square$

### The Transfer and the Invariants

**Theorem.** When the action is free, so that $\pi$ is a double cover, the transfer $\tau : H^*(X;k)\to H^*(Q;k)$ satisfies

$$
\tau\circ\pi^* = 2, \qquad \pi^*\circ\tau = 1+\sigma^* = N,
$$

so that $\pi^*\tau$ is the norm of the involution on $H^*(X;k)$ and its image is the invariant submodule; over a field in which two is invertible the map $\tfrac12\pi^*\tau$ is the projection onto the invariants and $\tau$ is an isomorphism onto the invariants up to the scalar, while over $\mathbb{F}_2$ the first identity is $\tau\pi^*=0$. These are the cohomological forms of the identities of *The Transfer and the Involution*.

*Proof.* The chain identities $p_\#\tau=2$ and $\tau p_\#=N$ of *The Transfer and the Involution* dualise to the stated identities, the norm has image the invariants because $N = 1+\sigma^*$ and $\sigma^*N = N$, and over a field where two is invertible the idempotent $\tfrac12N$ realises the projection. $\square$

### The Comparison with the Homotopy Quotient

**Theorem.** The map of quotients

$$
\pi_G : X_{\mathbb{Z}/2} = EG\times_{\mathbb{Z}/2}X \longrightarrow Q = \mathrm{pt}\times_{\mathbb{Z}/2}X
$$

induced by the projection $EG\to\mathrm{pt}$ is continuous, and it induces the comparison map on cohomology

$$
\pi_G^* : H^*(Q;k) \longrightarrow H_{\mathbb{Z}/2}^*(X;k) ,
$$

which is the identity on the quotient when the action is free: for a free involution $X_{\mathbb{Z}/2}\simeq Q$ and the comparison is an isomorphism, so the orbit-space cohomology and the equivariant cohomology coincide. For a non-free action the comparison is not an isomorphism; the difference between the two is the contribution of the fixed set, and the map factors the pullback $\pi^*$ through the restriction to the fibre of the Borel fibration.

*Proof.* The Borel construction is natural in the space with action, so the map $\mathrm{pt}\to EG$ (the inclusion of a point) induces a map of homotopy quotients in the stated direction; for a free action the projection $EG\times_{\mathbb{Z}/2}X\to X/\sigma$ is a homotopy equivalence by *Two-Fold Coverings and the Borel Construction*; the non-free case is the statement of the localisation of *Equivariant Cohomology*. $\square$

## Grothendieck's Theorem in Inverted Characteristic

### The Statement

**Theorem (Grothendieck).** Let $k$ be a field in which two is invertible. Then the pullback

$$
\pi^* : H^*(Q;k) \longrightarrow H^*(X;k)^\sigma
$$

is an isomorphism onto the invariants, and it is injective with image the invariant subalgebra. Equivalently, the cohomology of the orbit space is the invariant cohomology of the space, and the transfer realises the inverse: $\pi^*\circ\tfrac12\tau = \mathrm{id}$ and $\tfrac12\tau\circ\pi^*=\mathrm{id}$ on the invariants.

*Proof.* By the second comparison theorem the action is effectively free over $k$ modulo the fixed set, and the transfer argument of *The Transfer and the Involution* applies: $\tfrac12 N$ is the projection onto the invariants and it factors through $\pi^*$ because $\pi^*\tau=N$, while $\tau\pi^*=2$ shows that $\tfrac12\tau$ is a left inverse; the two together give the isomorphism. $\square$

### The Consequences

**Corollary.** Over a field in which two is invertible, the invariant classes are exactly the classes pulled back from the quotient, the quotient map is injective on cohomology, and the cohomology of the orbit space is computed by taking invariants: $H^*(Q;k)\cong H^*(X;k)^\sigma$. In particular the Betti numbers of the quotient are the dimensions of the invariant cohomology, and the Euler characteristics are related by $\chi(Q) = \tfrac12(\chi(X)+\chi(F))$ over the rationals.

*Proof.* The isomorphism is the theorem; the Euler-characteristic formula follows from the additivity on the free part and the fixed part, the free part contributing half its Euler characteristic and the fixed set contributing its own. $\square$

## The Mod 2 Case and the Cartan–Leray Sequence

### The Spectral Sequence

**Theorem (Cartan–Leray).** Let the involution act, and consider the two-fold covering $\pi : X\to Q$ of the free part; then the cohomology of the quotient is the abutment of the spectral sequence

$$
E_2^{p,q} = H^p(\mathbb{Z}/2; H^q(X;\mathbb{F}_2)) \ \Longrightarrow \ H^{p+q}(Q;\mathbb{F}_2),
$$

with coefficients in the cohomology of $X$ regarded as a module over the group ring $\mathbb{F}_2[\mathbb{Z}/2]$ through the action $\sigma^*$; the sequence is natural for equivariant maps, and for the free action it converges to the quotient cohomology from the group cohomology of the coefficient module.

*Proof.* The Cartan–Leray spectral sequence of the covering with group $\mathbb{Z}/2$, obtained from the filtration of the singular complex of $Q$ by the cover; the identification of the $E_2$ page with the group cohomology of the coefficient module is the standard one for the covering, and the convergence is to the cohomology of the total space of the cover. $\square$

### The Kernel of the Pullback

**Theorem.** Over $\mathbb{F}_2$ the pullback of the quotient is not in general injective; its kernel is the ideal of the quotient cohomology consisting of the classes whose restriction to the free part of the cover vanishes, and it is annihilated by the Euler class in the free case. When the involution acts trivially on $H^*(X;\mathbb{F}_2)$ the pullback is an isomorphism onto the invariants if and only if the action is free and the cover is trivial in cohomology; otherwise the quotient has extra classes and the pullback has a kernel, of which the antipodal covering $S^n\to\mathbb{RP}^n$ is the model, whose pullback kills every power of the generator except the zeroth and the top of the quotient ring.

*Proof.* The kernel is by definition the classes restricting to zero; in the free case the Gysin sequence of *The Gysin Sequence of a Two-Fold Covering* identifies the kernel of $\pi^*$ with the image of $\smile e$, hence annihilated by $e$; the model is computed from the cohomology of the projective space. $\square$

### The Comparison with the Equivariant Cohomology

**Remark.** For the free action the quotient cohomology and the equivariant cohomology agree, $H^*(Q;\mathbb{F}_2)\cong H_{\mathbb{Z}/2}^*(X)$, and the Cartan–Leray sequence and the Borel spectral sequence coincide; for a non-free action the two differ by the fixed-set contribution, and the comparison map $\pi_G^*$ fits into the localisation of *Equivariant Cohomology*: after inverting the generator of $H^*(B\mathbb{Z}/2;\mathbb{F}_2)$, the equivariant cohomology becomes the cohomology of the fixed set with a free module adjoined, while the orbit space sees the fixed set as a closed subspace and has no such algebraic free part. The refined statement uses the Bredon cohomology of the orbit category, which is the subject of *Equivariant Obstruction Theory*.

## The Relation to the Fixed Set

### The Fixed Set as the Singular Locus of the Quotient

**Theorem.** The image $\pi(F)$ of the fixed set is the singular locus of the projection: over the complement of $\pi(F)$ the projection is a double cover, so the quotient there has the cohomology of the invariants, and at $\pi(F)$ the projection is a homeomorphism, so the fixed set survives to the quotient. The cohomology of $Q$ is therefore computed from the cohomology of the free part and the cohomology of $F$ by the Mayer–Vietoris sequence of the decomposition $Q = (Q\setminus\pi(F))\cup\pi(F)$, and the mixed terms are the invariant classes of the free part.

*Proof.* The projection is a double cover over $Q\setminus\pi(F)$ and a homeomorphism over $\pi(F)$, so the Mayer–Vietoris sequence of *Exact Sequences* applies to the two closed pieces; the free part contributes its invariant cohomology and the fixed part its own cohomology, with the connecting map the restriction. $\square$

**Corollary.** For a free involution the quotient has no singular locus, $H^*(Q;k)\cong H^*(X;k)^\sigma$ over a field in which two is invertible, and over $\mathbb{F}_2$ the quotient cohomology is computed by the Cartan–Leray sequence; for an involution with a fixed set the quotient cohomology is the invariant cohomology of the free part glued to the cohomology of the fixed set along the restriction.

*Proof.* The two cases are the two extremes of the decomposition; the free case is Grothendieck's theorem and the fixed case is the Mayer–Vietoris computation. $\square$

## The Invariants and the Sign Decomposition

### The Two Idempotents

**Definition.** Over a field $k$ in which two is invertible, the **invariant** and the **anti-invariant** projections of the involution are

$$
p_+ = \tfrac12(1+\sigma^*) , \qquad p_- = \tfrac12(1-\sigma^*) ,
$$

acting on $H^*(X;k)$.

**Theorem.** The two projections are idempotents with $p_+ + p_- = \mathrm{id}$, $p_+p_-=0$, $p_\pm^2=p_\pm$, and they decompose the cohomology into the invariant and the anti-invariant parts,

$$
H^*(X;k) = H^*(X;k)^+ \oplus H^*(X;k)^- , \qquad H^*(X;k)^\pm = p_\pm H^*(X;k) ,
$$

with $H^*(X;k)^+ = H^*(X;k)^\sigma$; the quotient cohomology is the invariant part, $H^*(Q;k)\cong H^*(X;k)^+$, and the coinvariants are canonically isomorphic to the invariants through the averaging, the quotient of $H^*(X;k)$ by the anti-invariant part being the invariant part.

*Proof.* The idempotent algebra is the computation $p_\pm^2=p_\pm$ and $p_+p_-=0$ from $\sigma^{*2}=\mathrm{id}$; the fixed part is the image of $p_+$ because $p_+a=a$ exactly when $\sigma^*a=a$, and the coinvariant statement follows from the decomposition. $\square$

### The Transfer as the Section

**Theorem.** In the sign decomposition the pullback is the inclusion of the invariant part up to the identification and the transfer is twice it: $\tau\pi^*=2$ and $\pi^*\tau=1+\sigma^*=2p_+$, so $\tfrac12\tau$ is the inverse of $\pi^*$ on the invariants and the norm is $2p_+$. The transfer is therefore the section that splits the pullback, and the quotient cohomology is the image of the idempotent $p_+$ applied to the cohomology of the space.

*Proof.* The identities are those of the section on the transfer and the invariance, and the idempotent form is $1+\sigma^*=2p_+$. $\square$

## The Local Structure at the Fixed Set

### The Slice and the Linear Model

**Theorem.** At a fixed point the slice theorem of *Equivariant Homotopy Theory* gives an equivariant neighbourhood of the point of the form $D(V)$ for a finite-dimensional real vector space $V$ with a linear involution, and the quotient near the image of the point is the quotient $D(V)/\pm$; every linear involution of $V$ is diagonalisable with eigenvalues $\pm1$ and fixed subspace $V^+$ and complement $V^-$, so

$$
D(V)/\pm \;\cong\; D(V^+)\times\bigl(D(V^-)/\pm\bigr), \qquad D(V^-)/\pm \cong \text{the cone on } \mathbb{RP}^{\dim V^- - 1} ,
$$

and the quotient is a topological manifold only when $V^-=0$ or $V^+=0$, that is when the involution is trivial or free; otherwise the image of the fixed set is a singular stratum.

*Proof.* An involution of a real vector space has the minimal polynomial dividing $t^2-1$, hence is diagonalisable with eigenvalues $\pm1$; the quotient of the complement by the antipodal identification is the cone on the projective space of $V^-$, which is the quotient of the unit sphere, and the product decomposition is the diagonalisation. $\square$

### The Local Cohomology

**Theorem.** The local cohomology of the quotient at the image of a fixed point is computed by the Gysin sequence of the double cover of the punctured disk, and for the linear model it is the cohomology of the cone on $\mathbb{RP}^{\dim V^- - 1}$, which is that of a point in degree zero together with the reduced cohomology of the projective space shifted up by one, the top class contributing in degree $\dim V^-$; the singular stratum therefore contributes the mod 2 classes of the projective space of the normal directions, in accordance with the fixed-set contribution of the Smith theory.

*Proof.* The punctured disk is homotopy equivalent to the sphere and the double cover there is the antipodal covering, whose cohomology is computed by the Gysin sequence of *The Gysin Sequence of a Two-Fold Covering*; the cone on a space raises the reduced cohomology by one degree, so the top class of $\mathbb{RP}^{\dim V^- - 1}$ contributes in degree $\dim V^-$, and the cone adds the point in degree zero. $\square$

## Examples

**Example (the spheres and the projective spaces).** For the antipodal involution of $S^n$, $n \geq 1$, the quotient is $\mathbb{RP}^n$ and the fixed set is empty; over the rationals the antipodal map acts on $H^n(S^n;\mathbb{Q})$ by $(-1)^{n+1}$, so the invariant cohomology is $\mathbb{Q}$ in degree $0$ and, when $n$ is odd, in degree $n$, with Euler characteristic $1$ for $n$ even and $0$ for $n$ odd, in agreement with $\chi(\mathbb{RP}^n)=\tfrac12(\chi(S^n)+\chi(F))=\tfrac12\chi(S^n)$; over $\mathbb{F}_2$ the Cartan–Leray sequence computes $H^*(\mathbb{RP}^n;\mathbb{F}_2)=\mathbb{F}_2[x]/(x^{n+1})$ from $H^*(S^n;\mathbb{F}_2)$ and the group cohomology, and the pullback kills every positive-degree class, its kernel being the augmentation ideal generated by $x$ and its image the unit: the projection has degree two, so the pullback on the top class is the multiplication by two, which vanishes over $\mathbb{F}_2$, and the top class of $S^n$ lies instead in the image of the transfer.

**Example (the interval).** For the reflection of $S^1$ with fixed set two points, the quotient is an interval; over a field in which two is invertible the cohomology of the quotient is the invariant cohomology of $S^1$, which is the cohomology of a point; over $\mathbb{F}_2$ the mod 2 cohomology of the interval is one-dimensional, and the fixed set contributes the two points whose classes are identified in the quotient. The example exhibits the Euler-characteristic formula of the corollary in the smallest case.

**Example (the torus).** For the involution of the torus inverting one circle, the fixed set is the complementary torus and the quotient is the product of an interval with the circle; over the rationals the invariant cohomology of the torus is the cohomology of the quotient, and the fixed set contributes the classes of the invariant circle. The example shows the gluing of the free part and the fixed part in a case where both are non-trivial.

## Summary

The orbit space $Q = X/\sigma$ of an involution is the quotient of the space by the equivalence $x\sim\sigma x$, with projection $\pi$ that is a double cover over the complement of the fixed set and a homeomorphism on the fixed set. Two comparisons govern its cohomology: the pullback $\pi^* : H^*(Q;k)\to H^*(X;k)$, whose image lies in the invariants and which satisfies the transfer identities $\tau\pi^*=2$ and $\pi^*\tau=1+\sigma^*$, and the comparison map $\pi_G^* : H^*(Q;k)\to H_{\mathbb{Z}/2}^*(X;k)$ from the orbit space to the homotopy quotient, which is an isomorphism exactly for the free action. Over a field in which two is invertible Grothendieck's theorem gives $H^*(Q;k)\cong H^*(X;k)^\sigma$, so the quotient cohomology is the invariant cohomology and the Euler characteristics are related by $\chi(Q)=\tfrac12(\chi(X)+\chi(F))$; over $\mathbb{F}_2$ the quotient is computed by the Cartan–Leray spectral sequence $E_2^{p,q}=H^p(\mathbb{Z}/2;H^q(X;\mathbb{F}_2))\Rightarrow H^{p+q}(Q;\mathbb{F}_2)$, the pullback has a kernel that vanishes on the free part and is annihilated by the Euler class, and the fixed set is the singular locus of the quotient, glued to the free part by Mayer–Vietoris. The transfer and the Gysin sequence are those of *The Transfer and the Involution* and *The Gysin Sequence of a Two-Fold Covering*, the equivariant cohomology and its localisation are those of *Equivariant Cohomology*, and the fixed-set theory is that of *The Mod 2 Cohomology of an Involution*. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,\sigma)$, $F = X^{\sigma}$ | Space with an involution and its fixed set |
| $Q = X/\sigma$, $\pi : X\to Q$ | Orbit space and projection |
| $\pi^* : H^*(Q;k)\to H^*(X;k)$ | Pullback; image in the invariants $H^*(X;k)^\sigma$ |
| $N = 1+\sigma^*$ | Norm of the involution on cohomology |
| $\tau : H^*(X;k)\to H^*(Q;k)$ | Transfer (free case); $\tau\pi^*=2$, $\pi^*\tau=N$ |
| $H^*(Q;k)\cong H^*(X;k)^\sigma$ | Grothendieck's theorem, two invertible in $k$ |
| $\chi(Q)=\tfrac12(\chi(X)+\chi(F))$ | Euler characteristics over $\mathbb{Q}$ |
| $E_2^{p,q}=H^p(\mathbb{Z}/2;H^q(X;\mathbb{F}_2))\Rightarrow H^{p+q}(Q;\mathbb{F}_2)$ | Cartan–Leray spectral sequence of the quotient |
| $\pi_G : X_{\mathbb{Z}/2}\to Q$, $\pi_G^*$ | Comparison map to the homotopy quotient and on cohomology |
| $\pi_G^* : H^*(Q;k)\cong H_{\mathbb{Z}/2}^*(X;k)$ | Isomorphism exactly for the free action |
| $\pi(F)$ | Image of the fixed set; the singular locus of the projection |

## Further Reading

- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the transfer argument and the invariants of the quotient.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the cohomology of an orbit space, the Cartan–Leray sequence and the fixed-set decomposition.
- Armand Borel, *Seminar on Transformation Groups* (Annals of Mathematics Studies 46, 1960), for the equivariant cohomology and its comparison with the orbit space.
- John McCleary, *A User's Guide to Spectral Sequences* (Cambridge University Press, 2nd ed. 2001), for the Cartan–Leray spectral sequence of a covering.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the quotient maps, the transfer and the cohomology of the projective spaces.
- Wu-yi Hsiang, *Cohomology Theory of Topological Transformation Groups* (Springer, 1975), for the orbit-space computations and the fixed-set contributions.
