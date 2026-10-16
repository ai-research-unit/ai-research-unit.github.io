# __The Euclidean Topology of the Reduced Biquaternion Algebra__

## Introduction

The Euclidean topology of the reduced biquaternion algebra is the topology of the norm $\lVert T\rVert=\sqrt{\langle T\rangle_{\natural*}}$, and this article develops it: the isometry onto $\mathbb{R}^{4}$, the algebra read as a normed algebra, the contractibility, the unit group as a topological group, the Euclidean unit sphere and the topology of the zero-divisor set. The algebra is **commutative**, and the two facts that shape the topology are that the multiplication **has zero divisors** — so the norm is not submultiplicative with constant one, and the unit group is the complement of the zero-divisor set — and that the algebra is **not a division algebra**. The Euclidean topology is the subject; the algebraic norm $\langle\cdot\rangle_{\natural*}$ is only the tool, and the four algebraic norms are distinguished from it throughout.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $T=A+Bj$ with $A=a+ia'$, $\langle\cdot\rangle=b+ib'$; the idempotent coordinates are $q_1=A+B$, $q_2=A-B$. The Euclidean norm is $\lVert T\rVert=\sqrt{\langle T\rangle_{\natural*}}=\sqrt{a^{2}+a'^{2}+b^{2}+b'^{2}}$, from the positive definite form $\langle\cdot,\cdot\rangle_{\natural*}$ of *The Four Products, Their Forms and Their Algebraic Norms*. The element glyph is $T$, without a tilde.

**Boundaries.** The topology and the metric are set up in *Topology in the Space of Reduced Biquaternions*; the metric of each product is *Topology and Metric for Each of the Operations*; the zero divisors are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the unit group and its complement are *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*; and the forms are *The Forms of the General Plain Algebra of the Reduced Biquaternions*. The biquaternion counterpart is *The Euclidean Topology of the Biquaternion Algebra*.

## The Euclidean Norm and the Isometry onto $\mathbb{R}^{4}$

**The norm is the Euclidean norm of the coordinate quadruple, and the coordinate map is an isometry onto $\mathbb{R}^{4}$.**

**Theorem (the isometry).** The map
$$
T=A+Bj\mapsto(a,a',b,b')
$$
is an isometry of $\mathbb{B}_{\mathrm{r}}$ with the norm $\lVert\cdot\rVert$ onto $\mathbb{R}^{4}$ with its standard Euclidean norm, and it is an isomorphism of real vector spaces.

*Proof.* $\lVert T\rVert^{2}=a^{2}+a'^{2}+b^{2}+b'^{2}$ is the sum of the squares of the four coordinates, which is the square of the standard Euclidean norm of the quadruple; the map is a bijective real-linear map by *The Four-Vector Element Representation of the Reduced Biquaternions*, and it preserves the norm by the display.

**Corollary (the geometry is the standard one).** Every topological property of the space is the corresponding property of $\mathbb{R}^{4}$: the space is complete, separable, locally compact, second-countable, finite-dimensional and non-compact, and its one-point compactification is $S^{4}$.

*Proof.* The isometry is a homeomorphism and all the listed properties are invariant under homeomorphism and hold for $\mathbb{R}^{4}$.

## The Algebra as a Normed Algebra

**The norm is not submultiplicative with constant one, and the sharp constant is $\sqrt2$.**

**Theorem (the multiplication inequality).** For all $T,W$,
$$
\lVert TW\rVert\le\sqrt2\,\lVert T\rVert\lVert W\rVert,
$$
and the constant $\sqrt2$ is sharp; more precisely
$$
\frac{\lVert TW\rVert^{2}}{\lVert T\rVert^{2}\lVert W\rVert^{2}}
=1+\frac{\bigl(\lvert q_{1,T}\rvert^{2}-\lvert q_{2,T}\rvert^{2}\bigr)\bigl(\lvert q_{1,W}\rvert^{2}-\lvert q_{2,W}\rvert^{2}\bigr)}{\bigl(\lvert q_{1,T}\rvert^{2}+\lvert q_{2,T}\rvert^{2}\bigr)\bigl(\lvert q_{1,W}\rvert^{2}+\lvert q_{2,W}\rvert^{2}\bigr)},
$$
a ratio in $[0,2]$.

*Proof.* In the idempotent coordinates $\lVert T\rVert^{2}=\tfrac12(\lvert q_{1,T}\rvert^{2}+\lvert q_{2,T}\rvert^{2})$ and $\lVert TW\rVert^{2}=\tfrac12(\lvert q_{1,T}q_{1,W}\rvert^{2}+\lvert q_{2,T}q_{2,W}\rvert^{2})$. Writing $a=\lvert q_{1,T}\rvert^{2}$, $b=\lvert q_{2,T}\rvert^{2}$, $c=\lvert q_{1,W}\rvert^{2}$, $d=\lvert q_{2,W}\rvert^{2}$, the ratio is
$$
\frac{2(ac+bd)}{(a+b)(c+d)}=\frac{ac+bd+ac+bd}{(a+b)(c+d)}=1+\frac{ac+bd-ad-bc}{(a+b)(c+d)}=1+\frac{(a-b)(c-d)}{(a+b)(c+d)},
$$
which lies in $[0,2]$ because $\lvert(a-b)/(a+b)\rvert\le1$ and $\lvert(c-d)/(c+d)\rvert\le1$ for non-negative $a,b,c,d$. The two extremes are attained, $2$ when $a\gg b$ and $c\gg d$, $0$ when the two products $TW$ vanish, that is at the zero divisors.

**Corollary (the failure of submultiplicativity and the absence of a lower bound).** The algebra is a normed algebra only up to the constant $\sqrt2$; it is not a Banach algebra in the strict sense. There is no positive constant $c$ with $\lVert TW\rVert\ge c\lVert T\rVert\lVert W\rVert$: taking $T$ on the first idempotent line and $W$ on the second gives $TW=0$ with $\lVert T\rVert\lVert W\rVert>0$. The failure is exactly the presence of the zero divisors.

*Proof.* The ratio reaches $2$, so the constant $\sqrt2$ cannot be lowered; the ratio reaches $0$ on the pairs $q_{1,T}q_{2,W}=0$ and $q_{2,T}q_{1,W}=0$, which are the products of the two idempotent lines, the zero divisors of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*.

**Corollary (the submultiplicativity up to powers).** For every positive integer $n$,
$$
\lVert T^{n}\rVert\le(\sqrt2)^{\,n-1}\lVert T\rVert^{n}.
$$

*Proof.* Iterate the inequality $\lVert T^{k+1}\rVert\le\sqrt2\lVert T^{k}\rVert\lVert T\rVert$ and use $\lVert T\rVert^{n}$.

## The Contractibility of the Algebra

**The algebra is contractible, being a real vector space.**

**Theorem.** The homotopy $\langle T,s\rangle_{*}=(1-s)T$ for $s\in[0,1]$ contracts $\mathbb{B}_{\mathrm{r}}$ to the origin, and it is continuous in $(T,s)$; hence the space is contractible, and its homotopy groups vanish.

*Proof.* The map is the multiplication by a real scalar and is jointly continuous in the element and the parameter; at $s=0$ it is the identity and at $s=1$ it is the constant map to $0$.

**Corollary (the unit sphere is the only spherical object, and it is not a group).** The only interesting topological object in the space is the Euclidean sphere of §*The Euclidean Unit Sphere*; the algebra itself has no non-trivial homotopy, and no sphere of the algebra is a group under the multiplication unless the multiplication is restricted to the units. The one-point compactification of the algebra is $S^{4}$, but the algebra is not the sphere; the sphere is a level set, not the whole space.

*Proof.* The contraction collapses every loop and every sphere in the algebra; the sphere $S^{3}$ is a compact level set, and its group structure is examined in the next section and fails.

## The Unit Group as a Topological Group

**The unit group is an open dense subset, and with the multiplication and the inversion it is a topological group homeomorphic to the torus times a plane.**

**Theorem (the unit group).** The unit group
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\{T:\langle T\rangle_{\natural}\neq0\}=\{T:q_1\neq0,\ q_2\neq0\}
$$
is open and dense, and it is a topological group: the multiplication and the inversion are continuous.

*Proof.* The unit group is the complement of the closed zero-divisor set, hence open, and the set has empty interior, hence the unit group is dense, by *Topology in the Space of Reduced Biquaternions*. The multiplication is continuous as a product in a topological algebra, and the inversion is continuous because it is given by $T^{-1}=(A-Bj)/\langle T\rangle_{\natural}$ with $\langle T\rangle_{\natural}$ a continuous non-vanishing function, hence a continuous map.

**Theorem (the homeomorphism).** The unit group is homeomorphic to
$$
\mathbb{C}^{\times}\times\mathbb{C}^{\times}\cong(S^{1}\times S^{1})\times(\mathbb{R}_{>0}\times\mathbb{R}_{>0}),
$$
through the two idempotent coordinates; it is connected, abelian, non-compact, and its fundamental group is $\mathbb{Z}^{2}$.

*Proof.* The map $T\mapsto(q_1,q_2)$ is a homeomorphism of the unit group onto $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, an isomorphism of groups by *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; each $\mathbb{C}^{\times}$ is homeomorphic to $S^{1}\times\mathbb{R}_{>0}$ by modulus and argument, so the group is homeomorphic to the display. It is connected as a product of connected sets, abelian as a product of abelian groups, non-compact because $\mathbb{R}_{>0}$ is not compact, and its fundamental group is $\pi_{1}(S^{1})^{2}=\mathbb{Z}^{2}$, the two positive factors being contractible.

**Corollary (the unit group is not the whole space and not compact).** The unit group is a proper open subset, homotopy equivalent to the two-torus, and its complement, the zero-divisor set, is its boundary. The unit group deformation-retracts onto its torus factor, and no retraction of the space onto the unit group exists, the space being contractible and the unit group not.

*Proof.* The complement is the zero-divisor set of the next section; a retraction of the contractible space onto the non-contractible unit group would make the unit group contractible, which it is not since $\pi_{1}=\mathbb{Z}^{2}\neq0$.

## The Euclidean Unit Sphere

**The Euclidean sphere is not a group and is not closed under the multiplication; it contains the two circles of zero divisors.**

**Definition.** The **Euclidean unit sphere** is the level set
$$
S^{3}=\{T:\lVert T\rVert=1\}=\{T:\langle T\rangle_{\natural*}=1\},
$$
a compact three-dimensional manifold without boundary.

**Theorem (the sphere is not closed under the multiplication).** The product of two elements of $S^{3}$ need not be in $S^{3}$; equivalently the norm is not multiplicative, and $S^{3}$ is not a subgroup of the unit group.

*Proof.* $\langle TW\rangle_{\natural*}=\langle T\rangle_{\natural*}\langle W\rangle_{\natural*}$ fails: for $T=W=\tfrac{1}{\sqrt2}(1+j)$ one has $\langle T\rangle_{\natural*}=\tfrac12(2)=1$ and $T^{2}=\tfrac12(1+j)^{2}=\tfrac12(2+2j)=1+j$ with $\langle T^{2}\rangle_{\natural*}=1+1=2\neq1$. So the product of two norm-one elements has norm $\sqrt2$ and is not unit.

**Theorem (the zero divisors on the sphere).** The sphere meets the zero-divisor set in the two circles
$$
\{q_1=0,\ \lvert q_2\rvert=\sqrt2\}\qquad\text{and}\qquad\{q_2=0,\ \lvert q_1\rvert=\sqrt2\},
$$
which are disjoint; the complement of the two circles in $S^{3}$ is the set of **norm-one units**, homeomorphic to $S^{1}\times S^{1}\times(-1,1)$.

*Proof.* On $\langle\cdot\rangle_{\natural*}=1$, the condition $q_1=0$ gives $\tfrac12\lvert q_2\rvert^{2}=1$, that is $\lvert q_2\rvert=\sqrt2$, a circle because $q_2\in\mathbb{C}$; symmetrically for $q_2=0$; the two circles are disjoint because $q_1=q_2=0$ gives $T=0\notin S^{3}$. Removing the two circles and reading $(\rho_{1},\rho_{2})$ with $\rho_{1}^{2}+\rho_{2}^{2}=2$ gives the display.

**Corollary (the contrast with the quaternions).** For the quaternions the unit sphere is the group $Sp(1)$; here the unit sphere is not a group, its norm-one units are the sphere minus two circles, and the group structure lives on the unit group of the previous section. The difference is the zero divisors, absent in the quaternions and present here.

*Proof.* The quaternion norm is multiplicative, so its sphere is closed under the multiplication and is a group; here the norm is not multiplicative, by the first theorem of this section, and the zero divisors, absent in the quaternions, cut two circles out of the sphere.

## The Topology of the Zero-Divisor Set

**The zero-divisor set is the union of two real planes meeting at the origin; it is closed, connected, of empty interior and minute, and it is not a manifold at the origin.**

**Theorem (the shape).** The zero-divisor set is
$$
\mathcal Z=\{\langle T\rangle_{\natural}=0\}=\{q_1=0\}\cup\{q_2=0\}=P_{1}\cup P_{2},
$$
where $P_{1}$ and $P_{2}$ are the two real two-dimensional subspaces $\{A+B=0\}$ and $\{A-B=0\}$, each a copy of $\mathbb{C}$, meeting only at the origin.

*Proof.* $\langle T\rangle_{\natural}=q_1q_2$ and a product of complex numbers vanishes exactly when one factor does; $\{q_1=0\}$ is $\{A=-B\}$, the set of $T=\langle 1-j\rangle$ for $B\in\mathbb{C}$, a real two-dimensional subspace; similarly $\{q_2=0\}=\{T=\langle 1+j\rangle\}$; their intersection is $\{\langle 1-j\rangle=B'(1+j)\}$, which forces $\langle\cdot\rangle=B'=0$.

**Theorem (the topological properties).** The set $\mathcal Z$ is closed, connected, path-connected, of empty interior and of Lebesgue measure zero; it is not compact; it is the boundary of the unit group; and it is not a topological manifold at the origin, where it is a crossing of two planes.

*Proof.* Closed as the vanishing set of the continuous functions $q_1,q_2$; connected because the two planes meet at the origin, and path-connected because each point of one plane reaches the origin by a straight line; empty interior and measure zero because each plane is a proper subspace; not compact because a subspace through the origin of positive dimension is unbounded; the boundary because it is the complement and the closure of the unit group, the unit group being dense. At the origin a neighbourhood of $\mathcal Z$ is the union of two planes meeting at that single point, which is not locally Euclidean of a single dimension, so $\mathcal Z$ is not a manifold there.

**Corollary (the difference from the companion).** In the biquaternion algebra the zero-divisor set is an irreducible cone of real dimension three; here it is the union of two planes of real dimension two, the factoring $\langle\cdot\rangle_{\natural}=(A+B)(A-B)$ being the idempotent splitting read on the norm, as *The Group of Units of the General Plain Algebra of the Reduced Biquaternions* records.

*Proof.* The complex-valued reduced norm of the reduced algebra factors and its zero set splits; the biquaternion reduced norm is an irreducible quadratic, whose zero set does not split, so its zero-divisor set is an irreducible cone.

## The Euclidean Space and the Duality

**The form $\langle\cdot,\cdot\rangle_{\natural*}$ identifies the space with its dual, and the isometry makes the dual a copy of the space.**

**Theorem (the Riesz identification).** The map
$$
T\mapsto \langle T,\cdot\rangle_{\natural*},\qquad W\mapsto \langle T,W\rangle_{\natural*},
$$
is a conjugate-linear isomorphism of $\mathbb{B}_{\mathrm{r}}$ onto its dual; through it each element is a linear functional and each functional is an element.

*Proof.* $\langle\cdot,\cdot\rangle_{\natural*}$ is positive definite and sesquilinear, hence non-degenerate; the map sends $T$ to the functional $W\mapsto \langle T,W\rangle_{\natural*}$, and non-degeneracy makes it injective, while equal finite dimensions make it bijective.

**Corollary (the Euclidean structure and the four products).** The four products are read on the dual through the four forms; the form $\langle\cdot,\cdot\rangle_{\natural*}$ gives the Euclidean identification and the form $\langle\cdot,\cdot\rangle_{*}$ the indefinite one, and the positive definite case is the one that gives a Hilbert-space structure on the four-dimensional real space, the complex-valued algebraic norms $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ giving no real inner product.

*Proof.* Each form is the scalar part of its product; only $\langle\cdot,\cdot\rangle_{\natural*}$ is an inner product, and an inner product on a finite-dimensional real space is a complete inner product, hence a Hilbert structure; $\langle\cdot,\cdot\rangle_{*}$ is indefinite, and the complex-valued $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ give no real inner product.

## Summary

The Euclidean topology of the reduced biquaternion algebra is the topology of the norm $\lVert T\rVert=\sqrt{\langle T\rangle_{\natural*}}$, and the coordinate map is an isometry onto $\mathbb{R}^{4}$, which makes the space complete, locally compact and non-compact, contractible, with one-point compactification $S^{4}$. The multiplication satisfies $\lVert TW\rVert\le\sqrt2\lVert T\rVert\lVert W\rVert$ with the sharp constant $\sqrt2$, and the algebra is a normed algebra only up to that constant; there is no positive lower bound, the failure being exactly the zero divisors. The unit group is open and dense, a topological group homeomorphic to the torus times a plane, connected and abelian with fundamental group $\mathbb{Z}^{2}$, not compact. The Euclidean unit sphere $S^{3}$ is not a group: the product of two norm-one elements can leave it, the norm not being multiplicative, and the sphere meets the zero-divisor set in two disjoint circles, whose complement is the set of norm-one units. The zero-divisor set is the union of two real planes meeting at the origin, closed, connected, of empty interior and measure zero, not a manifold at the origin, and it is the boundary of the unit group. The form $\langle\cdot,\cdot\rangle_{\natural*}$ identifies the space with its dual, and the algebra is **not a division algebra**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lVert T\rVert=\sqrt{\langle T\rangle_{\natural*}}$ | the Euclidean norm |
| $\mathcal Z=P_{1}\cup P_{2}$ | the zero-divisor set, the union of the two planes $q_1=0$ and $q_2=0$ |
| $S^{3}=\{\langle T\rangle_{\natural*}=1\}$ | the Euclidean unit sphere |
| $\{q_1=0,\lvert q_2\rvert=\sqrt2\}\cup\{q_2=0,\lvert q_1\rvert=\sqrt2\}$ | the two circles of zero divisors on the sphere |
| $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | the unit group, a topological group |

## Further Reading

- *Topology in the Space of Reduced Biquaternions* (`articles_maths/topology-in-the-space-of-reduced-biquaternions.md`), for the norm, the topology and the continuity of the products.
- *Topology and Metric for Each of the Operations* (`articles_maths/topology-and-metric-for-each-of-the-operations-of-the-reduced-biquaternions.md`), for the metric of each product.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the two lines.
- *The Group of Units of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the unit group.
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the non-commutative companion and its zero-divisor cone.
