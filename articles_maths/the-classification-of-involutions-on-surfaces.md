
# __The Classification of Involutions on Surfaces__

## Introduction

An involution of a closed orientable surface is classified by very little: whether it preserves or reverses the orientation, and then a single integer — the number of fixed points in the preserving case, the number of fixed circles in the reversing case. This article gives the classification, the Riemann–Hurwitz relation that constrains the integer in terms of the genus, the construction of the quotient orbifold, and the Nielsen theory of the fixed points.

The classification is the surface case of *Involutions on Manifolds and Equivariant Surgery*, where the fixed set and the equivariant neighbourhood are developed in general, and it is the simplest case in which the equivariant classification is complete: in dimension two the surgery obstruction vanishes and the invariants are the combinatorial data of the quotient. The quotients are the **$2$-orbifolds**, and the Riemann–Hurwitz relation between the genus, the number of branch points and the genus of the quotient is the numerical spine of the classification.

**The article assumes** the mapping class group and the Dehn twist of *Mapping Class Groups* and *The Dehn Twist as an Operator*, the structure theory of *Involutions on Manifolds and Equivariant Surgery*, the Euler characteristic and the classification of surfaces, and the elementary Nielsen fixed-point theory of *Degree Theory and the Brouwer Fixed Point Theorem*.

**The boundaries of the article.** The general involution of a manifold of dimension at least three, its equivariant surgery and its classification are *Involutions on Manifolds and Equivariant Surgery*; the free involutions and their quotients are *Free Involutions and Lens Spaces*; the fixed sets of periodic maps of prime order are *Periodic Maps and the Smith Theory*. The hyperbolic metrics realising the involutions as isometries are *Hyperbolic Geometry* and *Teichmüller Theory*; the higher-dimensional orbifolds and their fundamental groups are modelled on the two-dimensional case treated here. The analytic Teichmüller theory is Part III, and no physics is invoked.

## Local Models on a Surface

**Proposition (fixed sets of involutions of surfaces).** Let $T$ be a locally linear involution of a surface $S$.

**(a)** If $T$ preserves the orientation, then either $T$ is the identity or its fixed points are isolated. At an isolated fixed point there are coordinates $(u,v)$ in which $T(u,v) = (-u,-v)$.

**(b)** If $T$ reverses the orientation, then its fixed set is a disjoint union of simple closed curves, possibly empty. At a fixed point there are coordinates $(u,v)$ in which $T(u,v) = (-u,v)$ (or $(u,-v)$).

**Proof.** A locally linear involution of the plane is a linear involution, diagonalisable with eigenvalues $\pm1$. If it preserves the orientation its determinant is $+1$, so the number of $-1$ eigenvalues is even, hence $0$ or $2$: the identity, or $-I$, whose only fixed point is the origin. If it reverses the orientation the determinant is $-1$, so the number of $-1$ eigenvalues is odd, hence $1$: the model is a reflection with a fixed line. The local statements glue along the surface, and the fixed set of a reflection is one-dimensional, hence in a closed surface a union of circles.

**Corollary (the two kinds of involution).** An orientation-preserving involution of a closed surface is determined, up to conjugacy, by the finite set of its fixed points and its local model; an orientation-reversing involution is determined, up to conjugacy, by the family of circles it fixes. In particular an orientation-reversing involution has no isolated fixed point, and an orientation-preserving involution with more than one fixed point has all of them isolated.

## Orientation-Preserving Involutions

Let $S = S_g$ be the closed orientable surface of genus $g$, and let $T$ be an orientation-preserving involution different from the identity.

**Definition.** The **quotient orbifold** $O = S/T$ is the orbit space, a surface with finitely many **cone points** of order $2$, the images of the fixed points; its underlying surface is orientable of some genus $\gamma$, and the number of cone points is the number $r$ of fixed points of $T$. The **orbifold Euler characteristic** is
$$
\chi_{\mathrm{orb}}(O) = 2 - 2\gamma - \tfrac{r}{2},
$$
and the quotient map is a $2$-fold cover branched at the cone points.

**Theorem (Riemann–Hurwitz).** The Euler characteristics of $S$ and of the quotient orbifold are related by $\chi(S) = 2\,\chi_{\mathrm{orb}}(O)$, that is,
$$
2 - 2g = 2\Bigl(2 - 2\gamma - \tfrac{r}{2}\Bigr) = 4 - 4\gamma - r,
$$
so that
$$
r = 2 + 2g - 4\gamma .
$$

**Proof.** Take a triangulation of $O$ with the cone points as vertices and lift it to $S$. Every cell not supported on a cone point has two preimages, and each cone point has one preimage; the alternating count gives $\chi(S) = 2\chi(O) - r_{\mathrm{corr}}$ with the correction $r$ from the $r$ cone points, and $\chi(O) = 2-2\gamma$ for the underlying surface. The displayed formula follows.

**Corollary (the possible numbers of fixed points).** For an orientation-preserving involution of $S_g$ the number of fixed points is
$$
r = 2 + 2g - 4\gamma \qquad (\gamma = 0,1,\dots), \qquad r\geq0, \qquad r \equiv 2g+2 \pmod 4 .
$$
The involution is free exactly when $g$ is odd, the quotient then being a closed orientable surface of genus $\gamma = (g+1)/2$; and the involution is **hyperelliptic** exactly when $\gamma = 0$, in which case $r = 2g+2$ and the quotient is the sphere.

**Proof.** The formula is the Riemann–Hurwitz relation; the congruence is $2+2g-4\gamma\equiv2g+2\pmod4$; the vanishing of $r$ forces $2+2g = 4\gamma$, that is, $g = 2\gamma-1$ odd, and then the quotient is a closed orientable surface of genus $\gamma$; the largest $r$ occurs at $\gamma = 0$. The hyperelliptic involution is the one with the sphere quotient.

**Theorem (classification; orientation-preserving).** Two orientation-preserving involutions of $S_g$ are conjugate in the homeomorphism group if and only if they have the same number $r$ of fixed points; every value $r = 2+2g-4\gamma$ with $\gamma\geq0$ and $r\geq0$ occurs. The number of conjugacy classes is therefore the number of admissible values of $\gamma$, namely $\lfloor g/2\rfloor + 1$.

**Proof sketch.** Sufficiency is the classification of the $2$-fold branched covers of the sphere and of the surfaces with the prescribed branch data, which depends only on the genus and the number of branch points; the conjugacy is realised by a homeomorphism of the quotient extended to the cover, together with the choices of the local models, which are all equivalent. The full statements for the surfaces with boundary and punctures are in the literature; the case of $S_g$ is the one used here.

**Example (the torus).** For $g = 1$ the values are $r = 4-4\gamma$, so $r = 4$ (the quotient a sphere, the involution $-I$) or $r = 0$ (the quotient a torus, the free involution $(x,y)\mapsto(x+\tfrac12,y)$). Both occur, and the two classes are the whole list; the elliptic involution $-I$ has the four two-torsion points as fixed set.

**Example (the genus-two surface).** For $g = 2$ the values are $r = 6-4\gamma$, so $r = 6$ (the hyperelliptic involution, quotient the sphere) or $r = 2$ (quotient an elliptic curve). The hyperelliptic involution is central in $\mathrm{Mod}(S_2)$ modulo the centre, and its six fixed points are the Weierstrass points; the example is the standard one for the small genera.

**Example (the genus-three surface).** For $g = 3$ the values are $r = 8-4\gamma$, so $r = 8,4,0$: the hyperelliptic involution with eight fixed points, the involution with four, and the free involution with the quotient a surface of genus two. The three classes illustrate the congruence $r\equiv0\pmod4$ for $g$ odd.

## Orientation-Reversing Involutions

Let $\tau$ be an orientation-reversing involution of $S_g$.

**Theorem (classification; orientation-reversing, nonempty fixed set).** Suppose $\tau$ has a fixed point. Then its fixed set is a disjoint union of $k$ simple closed curves, where
$$
1 \leq k \leq g+1, \qquad k \equiv g+1 \pmod 2 ,
$$
and $\tau$ is determined up to conjugacy by $k$. Conversely every such $k$ occurs.

**Construction (the double of a surface with boundary).** Let $\Sigma$ be a compact connected orientable surface of genus $\gamma$ with $k$ boundary components, and let $S = \Sigma \cup_{\partial\Sigma} \Sigma$ be its **double** along the boundary. Then $S$ is closed orientable of genus
$$
g = 2\gamma + k - 1,
$$
the reflection swapping the two copies is an orientation-reversing involution, and its fixed set is exactly the boundary, a union of $k$ circles. The resulting $k$ satisfies $k = g - 2\gamma + 1$, so $1\leq k\leq g+1$ and $k\equiv g+1\pmod2$, and every admissible pair $(g,k)$ arises this way.

**Proof sketch of the theorem.** The construction realises the admissible values. For the converse, cut $S$ along the $k$ fixed circles: the result is a compact surface with $2k$ boundary circles on which $\tau$ acts freely, swapping the two copies of each circle; the quotient is a compact surface with $k$ boundary circles, and the computation of the Euler characteristics gives the relation $k = g-2\gamma+1$ between the number of fixed circles and the genus of the quotient, with the parity following from the integrality of $\gamma$. The classification up to conjugacy is that of the quotients with their boundary data, which is determined by $k$.

**Theorem (the free case).** If $\tau$ is free, its quotient is a closed non-orientable surface, of Euler characteristic $\chi(S_g)/2 = 1-g$ and hence of non-orientable genus $g+1$; such an involution exists for every $g$, and it is determined up to conjugacy by the quotient. The free case is not covered by the parity condition of the nonempty case, which is a statement about the fixed set alone.

**Proof sketch.** A free involution has a quotient which is a closed surface with $\chi = \chi(S_g)/2 = 1-g$; since $\tau$ reverses the orientation and $S_g$ is connected, the quotient is non-orientable, so it is $N_{g+1}$, the connected sum of $g+1$ projective planes; conversely $S_g$ is the orientation double cover of $N_{g+1}$, with the deck transformation the free orientation-reversing involution. The uniqueness is the uniqueness of the orientation double cover. (The orientability of the quotient is the one place where connectivity is used: a free orientation-reversing involution on a connected orientable manifold has a non-orientable quotient.)

**Example (the torus).** For $g = 1$ the nonempty case has $k\equiv0\pmod2$ and $1\leq k\leq2$, so $k = 2$: the reflection $\tau(x,y) = (-x,y)$ with the two circles $\{x=0\}$ and $\{x=\tfrac12\}$ fixed, the example of *The Involution on the Homology*. The free case is $k=0$, the quotient the Klein bottle, with the involution $(x,y)\mapsto(x+\tfrac12,-y)$.

**Example (the genus-two surface).** For $g = 2$ the values are $k\equiv1\pmod2$, $1\leq k\leq3$, so $k = 1$ (the double of the once-punctured torus, the fixed set one separating circle) or $k = 3$ (the double of a pair of pants, the fixed set three circles); the free case is excluded by the parity of the nonempty classification but nevertheless exists, with the quotient the closed non-orientable surface of genus three.

**Example (the sphere).** For $g = 0$ the values are $k\equiv1\pmod2$ and $1\leq k\leq1$, so $k = 1$: a reflection of the sphere in a great circle, the quotient the disc, the sphere being the double of the disc. The free orientation-reversing involution is the antipodal map, with quotient $\mathbb{RP}^2$.

## The Quotient Orbifold and its Fundamental Group

**Definition.** A **$2$-orbifold** is a surface together with a finite set of marked points, each with a cyclic group of orders $\geq2$ ("cone points"), and a finite set of marked boundary circles, each with a cyclic group acting by reflection ("mirror circles"); the orbifold fundamental group $\pi_1^{\mathrm{orb}}(O)$ is the fundamental group of the complement of the singular locus to which the local groups are adjoined, so that a loop around a cone point of order $n$ contributes a generator of order $n$ and a loop running to a mirror circle contributes an involution.

**Proposition (the orbifold fundamental group of the quotient).** Let $T$ be an orientation-preserving involution of $S_g$ with $r$ fixed points; then there is an extension
$$
1\longrightarrow \pi_1(S_g)\longrightarrow \pi_1^{\mathrm{orb}}(O)\longrightarrow \mathbb{Z}/2\longrightarrow 1,
$$
and $\pi_1^{\mathrm{orb}}(O)$ has a presentation with the $r$ generators of order two for the cone points; the extension is the one describing the branched cover. For an orientation-reversing involution the analogous extension describes the cover branched along the mirror circles, with the mirror circles contributing involutions.

**Proof sketch.** The quotient map away from the singular locus is a covering, giving the first map; the local group at a cone point provides the element of order two over it, and the composition onto $\mathbb{Z}/2$ records the sheet. The presentations are read off a triangulation of the orbifold. The orbifold groups are developed in the hyperbolic-geometry and low-dimensional articles, and the statement here is the bookkeeping needed for the classification.

**Remark (why the two-dimensional classification is complete).** In dimension two the surgery obstruction of the equivariant theory vanishes for the relevant groups and the quotient orbifold, with its genus, its cone points and its mirror circles, is a complete invariant of the involution up to conjugacy; this is the reason the classification is a finite combinatorial list rather than a surgery-theoretic computation. In higher dimensions the normal representations of the fixed components are additional invariants, as in *Involutions on Manifolds and Equivariant Surgery*.

## Nielsen Theory

**Theorem (Nielsen realisation, quoted).** Let $S$ be a closed orientable surface of genus $g\geq2$. Every finite subgroup of the mapping class group $\mathrm{Mod}(S)$ is realised by a group of homeomorphisms of $S$; equivalently, every involution of $S$ is conjugate to an isometry of some hyperbolic metric on $S$. The realisation of the finite-order mapping classes as geometric automorphisms is the content of the theorem, and the metric is the corresponding point of Teichmüller space.

**Proof sketch.** The theorem is Nielsen's, with a complete proof by Kerckhoff using the Teichmüller metric; the surface is given the hyperbolic metric for which the given finite-order homeomorphism has minimal displacement, and the action of the finite group is by isometries. The Teichmüller theory is *Teichmüller Theory* and Part III, and the hyperbolic metric is *Hyperbolic Geometry*; the statement is quoted here for the classification.

**Definition.** For a self-map $f$ of a compact surface the fixed points are grouped into **Nielsen classes** by paths between them, and the **Nielsen number** $N(f)$ is the number of classes of nonzero **fixed point index**; it is a homotopy invariant and satisfies $N(f)\leq\#\mathrm{Fix}(g)$ for every $g$ homotopic to $f$.

**Proposition (the Nielsen number of an involution).** Let $T$ be a non-identity involution of a closed surface with isolated fixed points. Then every fixed point is its own Nielsen class, of index $+1$, and
$$
N(T) = \#\mathrm{Fix}(T) = r ,
$$
so that the number of fixed points is the minimum in the homotopy class and the classification above is the classification of the Nielsen data.

**Proof.** Two distinct isolated fixed points of a finite-order map are joined by a path whose image under $t\mapsto T(x(t))$ is not homotopic to $x(t)$ unless the points are equal, because the map has finite order and no nontrivial path can be fixed up to homotopy; hence the classes are singletons. The index of each is the degree of $I - T$ at the point, which is $+1$ for the isolated model $z\mapsto -z$. The Lefschetz number $L(T) = r$ then agrees with the count, as in *Degree Theory and the Brouwer Fixed Point Theorem*.

**Remark (the realisation and the conjugacy classification).** Two involutions of $S_g$ are conjugate in $\mathrm{Mod}(S_g)$ exactly when they are conjugate in the homeomorphism group, by the Nielsen realisation; the classification by the single integer is therefore the classification both up to isotopy and up to conjugacy. For the orientation-reversing involutions the conjugacy is in the full group $\mathrm{Mod}^{\pm}(S_g)$.

## Summary

An involution of a closed orientable surface either preserves the orientation, in which case it is the identity or has isolated fixed points with the local model $z\mapsto-z$, or reverses it, in which case its fixed set is a union of simple closed curves with the local model a reflection. An orientation-preserving involution has $r = 2+2g-4\gamma$ fixed points, where $\gamma$ is the genus of the quotient orbifold, so that $r\equiv2g+2\pmod4$ and $r\geq0$; it is classified up to conjugacy by $r$, is free exactly when $g$ is odd, and is hyperelliptic exactly when the quotient is the sphere, with $2g+2$ fixed points. An orientation-reversing involution with nonempty fixed set fixes $k$ circles with $1\leq k\leq g+1$ and $k\equiv g+1\pmod2$, is classified by $k$, and is realised as the reflection of the double of a compact surface of genus $\gamma$ with $k$ boundary components, where $g = 2\gamma+k-1$; the free case has a non-orientable quotient of genus $g+1$ and exists for every $g$. The quotient is a $2$-orbifold whose fundamental group is an extension of $\pi_1(S_g)$ by the local groups, and in dimension two the quotient data are a complete invariant. Nielsen's realisation theorem identifies the conjugacy classes in the mapping class group with the geometric ones, and the Nielsen number of an involution is its number of fixed points.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_g$ | the closed orientable surface of genus $g$ |
| $T$ | an involution of $S_g$; orientation-preserving or reversing |
| isolated fixed point, $z\mapsto-z$ | the local model of an orientation-preserving involution |
| fixed circle, $z\mapsto\bar z$ | the local model of an orientation-reversing involution |
| $O = S/T$, $\gamma$ | the quotient orbifold and the genus of its underlying surface |
| $r = 2+2g-4\gamma$ | the number of fixed points; $r\equiv2g+2\pmod4$ |
| hyperelliptic involution | the orientation-preserving involution with $\gamma=0$, $r=2g+2$ |
| $k$ | the number of fixed circles of an orientation-reversing involution |
| $k\leq g+1$, $k\equiv g+1\pmod2$ | the range and parity of $k$ in the nonempty case |
| $\Sigma\cup_{\partial\Sigma}\Sigma$, $g=2\gamma+k-1$ | the double construction realising the reversing involutions |
| $\chi_{\mathrm{orb}} = 2-2\gamma-r/2$ | the orbifold Euler characteristic; Riemann–Hurwitz $\chi(S)=2\chi_{\mathrm{orb}}$ |
| $N(T) = \#\mathrm{Fix}(T)$ | the Nielsen number of an involution with isolated fixed points |
| $N_{g+1}$ | the non-orientable closed surface, $\chi = 1-g$, the quotient in the free case |

## Further Reading

- Jakob Nielsen, "Die Struktur periodischer Transformationen von Flächen", *Matematisk-fysiske Meddelelser* 15 (1937), 1–77, for the classification of periodic surface homeomorphisms.
- Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups* (Princeton University Press, 2012), for the classification of involutions, the hyperelliptic involution and the Nielsen realisation.
- Steven Kerckhoff, "The Nielsen Realization Problem", *Annals of Mathematics* 117 (1983), 235–265, for the realisation of finite subgroups of the mapping class group.
- William Thurston, "On the Geometry and Dynamics of Diffeomorphisms of Surfaces", *Bulletin of the American Mathematical Society* 19 (1988), 417–431, for the classification of surface homeomorphisms and its finite-order case.
- Emilio Bujalance, José Etayo, José Gamboa and Grzegorz Gromadzki, *Automorphisms of Compact Non-Orientable Riemann Surfaces* (Pitman, 1990), for the orientation-reversing involutions, the ovals and the parity conditions.
- Bo Ju Jiang, *Lectures on Nielsen Fixed Point Theory* (Contemporary Mathematics 14, American Mathematical Society, 1983), for the Nielsen classes, the Nielsen number and the index.
- John Stillwell, *Classical Topology and Combinatorial Group Theory* (Springer, 1993), for the classification of surfaces, the double constructions and the orbifold groups.
