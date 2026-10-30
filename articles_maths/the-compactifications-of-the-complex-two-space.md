# __The Compactifications of $\mathbb{C}^2$__

## Introduction

A compactification of $\mathbb{C}^2$ is a compact Hausdorff space containing a dense copy of $\mathbb{C}^2$. There are many, and this article treats the two standard ones: the **one-point compactification**, which adds a single point at infinity and is the sphere $S^4$, and the **projective compactification**, which adds a complex projective line at infinity and is the projective plane $\mathbb{CP}^2$. The closed unit ball is the common model from which both are read: the ball keeps the sphere at infinity, the one-point compactification collapses it to a point, and the projective compactification attaches it to a two-sphere by the Hopf map.

The article treats the constructions, the cell decompositions, the homology, the Euler characteristic, the line at infinity and the proof that the two compactifications are not homeomorphic. It does not treat the topology of $\mathbb{C}^2$ itself, which is *The Topology of $\mathbb{C}^2$*; it does not treat the Hopf fibration in detail, which is *The Unit Sphere and the Hopf Fibration*; and it does not treat projective geometry in general, which is *Projective Geometry* and *Grassmannians and Stiefel Manifolds*. The characteristic classes used in one remark are *Characteristic Classes*.

**The two compactifications are both compact four-dimensional manifolds containing $\mathbb{C}^2$ densely, and they are not homeomorphic.** The reason is visible in the boundary: the one-point compactification adds a point, the projective one adds a two-sphere, and the two-sphere carries a non-trivial two-dimensional homology class.

## The Sphere at Infinity

**The open unit ball is $\mathbb{C}^2$, its boundary is the sphere $S^3$, and the three compactifications are three ways of treating that boundary.**

The open ball $B^4$ is homeomorphic to $\mathbb{C}^2$ by *The Topology of $\mathbb{C}^2$*, and its closure $\overline{B}^4$ is a compact manifold with boundary
$$
\partial\overline{B}^4=S^3.
$$
The boundary is the **sphere at infinity**: a sequence in $\mathbb{C}^2$ tends to infinity exactly when its radial coordinate tends to infinity, and the angular coordinate records the direction. The three treatments are collected below.

| Space | Treatment of the boundary $S^3$ | Boundary of the compactification | Compact | Manifold |
|---|---|---|---|---|
| closed ball $\overline{B}^4$ | kept | $S^3$ | yes | with boundary |
| one-point compactification $S^4$ | collapsed to a point | a point | yes | without boundary |
| projective compactification $\mathbb{CP}^2$ | attached to $\mathbb{CP}^1$ by the Hopf map | $\mathbb{CP}^1=S^2$ | yes | without boundary |

**Remark (the boundary is a choice).** The space $\mathbb{C}^2$ alone does not determine a boundary at infinity: the sphere $S^3$ is a choice of radial compactification, and the three compactifications are three quotients of that choice. **The one-point compactification forgets the direction, the projective compactification records the complex direction, and the closed ball records the real direction.** This is the organising idea of the article.

## The One-Point Compactification

**The one-point compactification adds a single point to $\mathbb{C}^2$ and is homeomorphic to the sphere $S^4$.**

**Definition.** Let $X$ be a locally compact Hausdorff space. The **one-point compactification** is the set $X^{+}=X\cup\{\infty\}$ with the topology whose open sets are the open sets of $X$ together with the sets $U$ containing $\infty$ such that $X\setminus U$ is compact in $X$.

**Proposition (the axioms).** For a locally compact, non-compact Hausdorff space $X$, the space $X^{+}$ is compact and Hausdorff, and $X$ is an open dense subset of $X^{+}$.

*Proof.* The open sets of $X$ are open in $X^{+}$; a set containing $\infty$ is open exactly when its complement in $X$ is compact. The space is compact: an open cover of $X^{+}$ contains a member $U$ with $\infty\in U$, whose complement $K=X\setminus U$ is compact, and finitely many members cover $K$. It is Hausdorff: two points of $X$ are separated by open sets of $X$, and a point $x\in X$ and $\infty$ are separated by a compact neighborhood of $x$ and its complement. The set $X$ is open, since $\{\infty\}$ is closed; it is dense, since a neighborhood of $\infty$ has compact complement, which is not all of $X$ because $X$ is not compact, so it meets $X$.

**Theorem (the one-point compactification of $\mathbb{C}^2$ is $S^4$).** There is a homeomorphism
$$
(\mathbb{C}^2)^{+}\longrightarrow S^4
$$
that is the inverse of the stereographic projection on $\mathbb{C}^2$ and sends $\infty$ to the north pole.

*Proof.* Identify $\mathbb{C}^2$ with $\mathbb{R}^4$. The inverse stereographic projection from the north pole $N=(0,0,0,0,1)$ is
$$
\sigma^{-1}(u)=\left(\frac{2u}{1+\lVert u\rVert^2},\frac{\lVert u\rVert^2-1}{1+\lVert u\rVert^2}\right)\in S^4\subset\mathbb{R}^5,
$$
a homeomorphism $\mathbb{R}^4\to S^4\setminus\{N\}$. As $\lVert u\rVert\to\infty$, the image tends to $N$. Extending by $\infty\mapsto N$ gives a continuous bijection from the one-point compactification onto the compact Hausdorff space $S^4$, hence a homeomorphism.

**Proposition (uniqueness and minimality).** The one-point compactification is unique up to homeomorphism. For every compactification $Y$ of a locally compact, non-compact Hausdorff space $X$, the identity of $X$ extends to a continuous surjection $Y\to X^{+}$ sending $Y\setminus X$ to $\infty$.

*Proof.* Two one-point compactifications are homeomorphic by the identity on $X$ extended by $\infty\mapsto\infty$. For the second statement, define $f:Y\to X^{+}$ by $f(y)=y$ for $y\in X$ and $f(y)=\infty$ otherwise. A locally compact dense subset of a compact Hausdorff space is open, so the preimage of an open set of $X$ is open in $Y$; the preimage of a neighborhood of $\infty$ is the complement in $Y$ of a compact subset of $X$, which is closed in the Hausdorff space $Y$, hence open. The map is surjective and continuous.

**Corollary (the smallest compactification).** The one-point compactification is the smallest compactification of $\mathbb{C}^2$: every other compactification maps onto $S^4$ by a continuous surjection that is the identity on $\mathbb{C}^2$.

*Proof.* This is the proposition applied to $X=\mathbb{C}^2$ and $X^{+}=S^4$.

**Proposition (the topological invariants).** The sphere $S^4$ is compact, connected, simply connected and of dimension $4$, with
$$
H_0(S^4;\mathbb{Z})=H_4(S^4;\mathbb{Z})=\mathbb{Z},\qquad H_k(S^4;\mathbb{Z})=0\quad(k=1,2,3),
$$
and Euler characteristic $2$. Its homotopy groups begin with $\pi_1(S^4)=\pi_2(S^4)=\pi_3(S^4)=0$.

*Proof.* The sphere is the boundary of the closed ball of $\mathbb{R}^5$, hence compact; it is connected and simply connected for dimension at least $2$; its cell decomposition $S^4=e^0\cup e^4$ gives the homology; and the low homotopy groups vanish because $S^4$ is $3$-connected (*Homotopy Groups and Fibrations*).

**Remark (the point at infinity).** In $S^4$ all directions of escape are identified: every sequence with $\lVert z_n\rVert\to\infty$, whatever the angular behaviour, converges to the same point $\infty$. **The one-point compactification is direction-blind.** This is exactly what the projective compactification refines.

**Remark (no complex structure).** The sphere $S^4$ admits no almost complex structure, so the one-point compactification cannot be made a complex manifold compatible with $\mathbb{C}^2$. The obstruction is read on the Chern classes: a closed almost complex $4$-manifold satisfies $c_1^2=2\chi+3\sigma$, which for $S^4$ gives $4$, while $H^2(S^4;\mathbb{Z})=0$ forces $c_1=0$ and $c_1^2=0$ (*Characteristic Classes*). **The one-point compactification is the compactification of the real space, not of the complex one.**

## The Projective Compactification

**The projective compactification adds a complex projective line at infinity, and the result is the complex projective plane $\mathbb{CP}^2$, a compact complex manifold of complex dimension two.**

**Definition.** The **complex projective plane** is the set of complex lines through the origin of $\mathbb{C}^3$,
$$
\mathbb{CP}^2=\bigl(\mathbb{C}^3\setminus\{0\}\bigr)/\mathbb{C}^{\times},
$$
with homogeneous coordinates $[Z_0:Z_1:Z_2]$, the class of $(Z_0,Z_1,Z_2)$.

**Proposition (the affine chart).** The map
$$
\mathbb{C}^2\longrightarrow\mathbb{CP}^2,\qquad(z_1,z_2)\longmapsto[1:z_1:z_2]
$$
is a homeomorphism onto the open set $U_0=\{Z_0\neq0\}$, whose complement is the **line at infinity**
$$
L_\infty=\{[0:Z_1:Z_2]\}\cong\mathbb{CP}^1.
$$
Hence $\mathbb{CP}^2=\mathbb{C}^2\sqcup\mathbb{CP}^1$ as a set, with $\mathbb{C}^2$ open and dense.

*Proof.* The map is injective, and its image is exactly $U_0$, since $[Z_0:Z_1:Z_2]=[1:Z_1/Z_0:Z_2/Z_0]$ for $Z_0\neq0$. The complement is the set $Z_0=0$, which is the projectivisation of the plane $Z_0=0\cong\mathbb{C}^2$, hence a projective line. The map is continuous with continuous inverse $[Z_0:Z_1:Z_2]\mapsto(Z_1/Z_0,Z_2/Z_0)$ on $U_0$.

**Proposition (the manifold structure).** The space $\mathbb{CP}^2$ is compact, Hausdorff, connected and second countable, and it is a complex manifold of complex dimension $2$ and real dimension $4$. The three charts $U_i=\{Z_i\neq0\}$ are copies of $\mathbb{C}^2$, with holomorphic transition maps.

*Proof.* The space is the quotient of the compact sphere $S^5\subset\mathbb{C}^3$ by the compact group $\mathrm{U}(1)$ acting by scalar multiplication, hence compact, Hausdorff and second countable; it is the continuous image of the connected sphere, hence connected. On $U_i$ the coordinates $Z_j/Z_i$ give a chart to $\mathbb{C}^2$, and the transition $Z_k/Z_i=(Z_k/Z_j)(Z_j/Z_i)$ is holomorphic on the overlap.

**Proposition (the line at infinity is a sphere).** The line at infinity $L_\infty$ is homeomorphic to $\mathbb{CP}^1$, hence to $S^2$. It is the set of complex directions of $\mathbb{C}^2$, and it has real codimension $2$ in $\mathbb{CP}^2$.

*Proof.* The line $L_\infty=\{[0:Z_1:Z_2]\}$ is the projective line of the plane $Z_0=0$, and $\mathbb{CP}^1$ is homeomorphic to $S^2$ (*The Subspaces of $\mathbb{C}^2$*). Its real dimension is $2$, against the real dimension $4$ of $\mathbb{CP}^2$.

**Theorem (the attaching map is the Hopf map).** The projective compactification is obtained from the closed ball by attaching its boundary sphere $S^3$ to $\mathbb{CP}^1$ along the Hopf map
$$
h:S^3\longrightarrow\mathbb{CP}^1,\qquad h(z_1,z_2)=[z_1:z_2].
$$
Equivalently, $\mathbb{CP}^2$ is the quotient of the disjoint union $\overline{B}^4\sqcup\mathbb{CP}^1$ that identifies each boundary point $z\in S^3$ with $h(z)$.

*Proof.* The open ball is $\mathbb{C}^2$, the boundary is $S^3$, and the inclusion $\mathbb{C}^2\to\mathbb{CP}^2$ has the complement $L_\infty=\mathbb{CP}^1$. A sequence $z_n\in\mathbb{C}^2$ with $\lVert z_n\rVert\to\infty$ converges in $\mathbb{CP}^2$ to $[0:w]$ exactly when the classes $[z_n]\in\mathbb{CP}^1$ converge to $[0:w]$, that is when the directions $z_n/\lVert z_n\rVert$ approach the fibre of $h$ over $[0:w]$. Hence the boundary is attached by $h$.

**Remark (the two boundaries).** The closed ball keeps the real directions $S^3$; the projective compactification collapses each circle of real directions inside a complex line to the single complex direction, which is a point of $\mathbb{CP}^1=S^2$. **The Hopf map is exactly the map from real directions to complex directions**, and it is the attaching map of the projective compactification. Its fibres are the circles of real directions that differ by a complex scalar.

## The Cell Decomposition

**The projective plane has one cell in each even dimension, which gives its homology, its Euler characteristic and its signature; the sphere $S^4$ has one cell in dimensions zero and four.**

**Theorem (the cells of $\mathbb{CP}^2$).** The projective plane decomposes as
$$
\mathbb{CP}^2=e^0\sqcup e^2\sqcup e^4,
$$
where
$$
e^0=\{[0:0:1]\},\qquad e^2=\{[0:1:Z_2]\},\qquad e^4=\{[1:Z_1:Z_2]\},
$$
so that $e^{2k}\cong\mathbb{C}^k\cong\mathbb{R}^{2k}$. The closure of $e^{2k}$ is $\mathbb{CP}^k$.

*Proof.* A point of $\mathbb{CP}^2$ has a first nonzero coordinate; the three possibilities $Z_0\neq0$, $Z_0=0$ and $Z_1\neq0$, and $Z_0=Z_1=0$ and $Z_2\neq0$ give the three cells. The cell $e^{2k}$ is parametrized by the $k$ free coordinates after the first nonzero one, hence is a copy of $\mathbb{C}^k$. The closure of $e^{2k}$ is the set of points whose first $2-k$ coordinates vanish, which is $\mathbb{CP}^k$.

**Corollary (the Euler characteristic).** The Euler characteristic of $\mathbb{CP}^2$ is
$$
\chi(\mathbb{CP}^2)=1+1+1=3.
$$

*Proof.* The Euler characteristic is the alternating sum of the number of cells in each dimension; there is one cell in dimensions $0$, $2$ and $4$, and none in odd dimensions.

**Theorem (the homology).** The homology of $\mathbb{CP}^2$ with integer coefficients is
$$
H_0=\mathbb{Z},\qquad H_1=0,\qquad H_2=\mathbb{Z},\qquad H_3=0,\qquad H_4=\mathbb{Z}.
$$
The group $H_2$ is generated by the class of the line at infinity, and $H_4$ by the fundamental class.

*Proof.* The cellular chain complex has one generator in dimensions $0$, $2$ and $4$, and all boundary maps vanish because there are no cells in odd dimensions. The generator of $H_2$ is the 2-cell, whose closure is $\mathbb{CP}^1=L_\infty$.

**Theorem (the cohomology ring and the signature).** The cohomology ring of $\mathbb{CP}^2$ is
$$
H^{*}(\mathbb{CP}^2;\mathbb{Z})=\mathbb{Z}[\alpha]/(\alpha^3),\qquad \deg\alpha=2,
$$
where $\alpha$ is the class dual to a line. Its square is the class of a point, evaluated by $\alpha^2([\mathbb{CP}^2])=1$. The intersection form on $H^2(\mathbb{CP}^2;\mathbb{R})$ is the $1\times1$ matrix $(1)$, and the signature of $\mathbb{CP}^2$ is $1$.

*Proof.* The ring is generated by the hyperplane class $\alpha$, and $\alpha^3=0$ because there is no cohomology in degree $6$. The product $\alpha^2$ is dual to the intersection of two generic lines, which is one point; hence $\alpha^2([\mathbb{CP}^2])=1$. The intersection form is therefore $(1)$, of signature $1$.

**Theorem (the sphere).** The sphere $S^4$ has the cell decomposition $S^4=e^0\cup e^4$, homology
$$
H_0=\mathbb{Z},\qquad H_1=H_2=H_3=0,\qquad H_4=\mathbb{Z},
$$
Euler characteristic $2$, and signature $0$.

*Proof.* The sphere is the boundary of a 5-ball, with one 0-cell and one 4-cell; the boundary maps vanish; the intersection form on $H^2(S^4;\mathbb{R})=0$ is trivial.

The two decompositions are compared below.

| Invariant | $S^4$ | $\mathbb{CP}^2$ |
|---|---|---|
| cells | $e^0\cup e^4$ | $e^0\cup e^2\cup e^4$ |
| $H_0$ | $\mathbb{Z}$ | $\mathbb{Z}$ |
| $H_1$ | $0$ | $0$ |
| $H_2$ | $0$ | $\mathbb{Z}$ |
| $H_3$ | $0$ | $0$ |
| $H_4$ | $\mathbb{Z}$ | $\mathbb{Z}$ |
| Euler characteristic | $2$ | $3$ |
| signature | $0$ | $1$ |

**Remark (the two attaching maps).** Both spaces are built from a 4-cell. In $S^4$ the boundary $S^3$ of the 4-cell is collapsed to a point, so the attaching map is constant. In $\mathbb{CP}^2$ the boundary is attached to the 2-cell $L_\infty$ by the Hopf map, and the Hopf map is essential. **The 2-cell is what gives $H_2=\mathbb{Z}$; the Hopf attaching map is what makes $\alpha^2=1$ and the signature $1$.** The next article computes the Hopf map and its Hopf invariant.

## The Line at Infinity

**The line at infinity is a complex projective line, hence a two-sphere; it records the complex directions of $\mathbb{C}^2$, and it is the boundary that the one-point compactification replaces by a point.**

Each point $[0:Z_1:Z_2]$ of $L_\infty$ is the complex line $\mathbb{C}(Z_1,Z_2)\subset\mathbb{C}^2$, that is a complex direction. The affine line
$$
a z_1+b z_2=c,\qquad (a,b)\neq(0,0),
$$
has closure
$$
aZ_1+bZ_2=cZ_0
$$
in $\mathbb{CP}^2$, and its point at infinity is $[0:b:-a]$, the direction of the line. Two affine lines are parallel exactly when their points at infinity coincide, so **parallel lines meet at infinity, and every two distinct projective lines meet in exactly one point.**

**Proposition (directions: real against complex).** The set of real rays of $\mathbb{C}^2$ is $S^3$; the set of complex lines is $\mathbb{CP}^1=S^2$; and the map between them is the Hopf map $h(z)=[z_1:z_2]$. Its fibre over a complex line is the circle of real rays contained in that line.

*Proof.* A real ray is a point of $S^3$. A complex line is a point of $\mathbb{CP}^1$. The map $h$ sends a real ray to the complex line it spans, and the fibre is the set of real rays in that complex line, a circle.

**Remark (what the two compactifications add).** The one-point compactification adds one point, which is the common limit of all directions; the projective compactification adds one point for each complex direction, that is a two-sphere. **The boundary of the projective compactification is the space of complex directions, and the boundary of the one-point compactification is the space of no direction at all.** This is the precise sense in which the projective compactification is finer.

**Remark (the line at infinity is not a boundary in the manifold sense).** The set $L_\infty$ is a complex submanifold of real codimension $2$, not the boundary of a manifold with boundary. **The compactification is a closed manifold; the line at infinity is a submanifold inside it**, and the complement $\mathbb{CP}^2\setminus L_\infty=\mathbb{C}^2$ is open and dense. The closed ball is the only one of the three spaces that has a genuine boundary.

## Why the Two Are Not Homeomorphic

**The sphere $S^4$ and the projective plane $\mathbb{CP}^2$ are both compact four-dimensional manifolds containing $\mathbb{C}^2$ densely, and they are not homeomorphic: their second homology groups differ.**

**Theorem (the obstruction).** The groups $H_2(S^4;\mathbb{Z})=0$ and $H_2(\mathbb{CP}^2;\mathbb{Z})=\mathbb{Z}$ are not isomorphic, so there is no homeomorphism $S^4\to\mathbb{CP}^2$.

*Proof.* A homeomorphism induces an isomorphism on homology; the two groups differ.

**Corollary (the other invariants).** The two spaces also differ in Euler characteristic, $2$ against $3$, in signature, $0$ against $1$, and in the second homotopy group, $0$ against $\mathbb{Z}$. Any one of these separates them.

*Proof.* These are homotopy invariants, computed above.

**Theorem (the identity extends one way only).** The identity of $\mathbb{C}^2$ extends to a continuous surjection
$$
\pi:\mathbb{CP}^2\longrightarrow S^4
$$
that collapses the line at infinity to the point at infinity. It does not extend to a continuous map $S^4\to\mathbb{CP}^2$.

*Proof.* Define $\pi([1:z_1:z_2])=(z_1,z_2)$ and $\pi([0:Z_1:Z_2])=\infty$. On the affine chart $\pi$ is the identity, hence continuous. At a point of $L_\infty$, a sequence $[1:z_1^n:z_2^n]$ converging to $[0:Z_1:Z_2]$ has $\lVert(z_1^n,z_2^n)\rVert\to\infty$, so $\pi$ sends the sequence to $\infty$; hence $\pi$ is continuous. For the second statement, suppose $F:S^4\to\mathbb{CP}^2$ extends the identity. The sequences $(n,0)$ and $(0,n)$ in $\mathbb{C}^2$ both tend to $\infty$ in $S^4$, so
$$
F(\infty)=\lim_{n\to\infty}[1:n:0]=[0:1:0],\qquad F(\infty)=\lim_{n\to\infty}[1:0:n]=[0:0:1],
$$
which is impossible.

**Remark (the meaning of the asymmetry).** The projective compactification is finer than the one-point compactification: it separates the directions that the one-point compactification identifies. **The collapse map $\pi$ is the statement that $S^4$ is a quotient of $\mathbb{CP}^2$**, and the failure of the reverse extension is the statement that the directions cannot be recovered from the one-point compactification.

**Remark (the complex structures).** The projective plane is a complex manifold, and the one-point compactification is not even almost complex. **The complex structure of $\mathbb{C}^2$ extends to $\mathbb{CP}^2$ and does not extend to $S^4$.** This is the deepest difference between the two compactifications: the projective one is the holomorphic compactification, the one-point one is the real compactification.

The two spaces are compared below.

| Property | $S^4$ | $\mathbb{CP}^2$ |
|---|---|---|
| real dimension | $4$ | $4$ |
| compact | yes | yes |
| connected | yes | yes |
| simply connected | yes | yes |
| $\pi_2$ | $0$ | $\mathbb{Z}$ |
| $H_2$ | $0$ | $\mathbb{Z}$ |
| Euler characteristic | $2$ | $3$ |
| signature | $0$ | $1$ |
| almost complex | no | yes |
| added boundary | a point | $\mathbb{CP}^1=S^2$ |

## Summary

The one-point compactification of $\mathbb{C}^2$ adds a single point and is the sphere $S^4$; it is the smallest compactification, and every compactification maps onto it. The projective compactification adds a complex projective line and is the projective plane $\mathbb{CP}^2$; it is a compact complex manifold of real dimension $4$, with $\mathbb{CP}^2=\mathbb{C}^2\sqcup\mathbb{CP}^1$ and the line at infinity a two-sphere of complex directions. The closed ball is the common model: it keeps the real-direction sphere $S^3$, the one-point compactification collapses it to a point, and the projective compactification attaches it to $\mathbb{CP}^1$ by the Hopf map.

The cell decompositions are $\mathbb{CP}^2=e^0\cup e^2\cup e^4$ and $S^4=e^0\cup e^4$. Hence $\mathbb{CP}^2$ has homology $\mathbb{Z}$ in degrees $0$, $2$ and $4$, Euler characteristic $3$, cohomology ring $\mathbb{Z}[\alpha]/(\alpha^3)$ and signature $1$; the sphere has homology $\mathbb{Z}$ in degrees $0$ and $4$, Euler characteristic $2$ and signature $0$. The two are not homeomorphic, because $H_2$ is $\mathbb{Z}$ against $0$; the same separation is read on $\pi_2$, on the Euler characteristic and on the signature. The identity of $\mathbb{C}^2$ extends to a continuous surjection $\mathbb{CP}^2\to S^4$ collapsing the line at infinity, but not to a map $S^4\to\mathbb{CP}^2$, because the limit at infinity in the projective plane depends on the direction. The projective compactification is holomorphic, the one-point compactification is not even almost complex.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X^{+}=X\cup\{\infty\}$ | the one-point compactification |
| $S^4$ | the one-point compactification of $\mathbb{C}^2$ |
| $\mathbb{CP}^2$ | the projective plane, the space of complex lines in $\mathbb{C}^3$ |
| $[Z_0:Z_1:Z_2]$ | homogeneous coordinates on $\mathbb{CP}^2$ |
| $U_0=\{Z_0\neq0\}$ | the affine chart, a copy of $\mathbb{C}^2$ |
| $L_\infty=\{[0:Z_1:Z_2]\}$ | the line at infinity, a copy of $\mathbb{CP}^1=S^2$ |
| $e^{2k}$ | the cell of real dimension $2k$, a copy of $\mathbb{C}^k$ |
| $\chi$ | the Euler characteristic |
| $\alpha\in H^2(\mathbb{CP}^2;\mathbb{Z})$ | the hyperplane class, with $\alpha^3=0$ and $\alpha^2=1$ |

## Further Reading

- [The Topology of $\mathbb{C}^2$](the-topology-of-the-complex-two-space.html), the previous article, for the space, the ball and the sphere.
- [The Unit Sphere and the Hopf Fibration](the-unit-sphere-and-the-hopf-fibration.html), the next article, for the Hopf map that attaches the boundary of the projective compactification.
- [The Subspaces of $\mathbb{C}^2$](the-subspaces-of-the-complex-two-space.html), for the projective line and the complex directions.
- [Projective Geometry](projective-geometry.html), for the projective plane, duality and the line at infinity in general.
- [Grassmannians and Stiefel Manifolds](grassmannians-and-stiefel-manifolds.html), for the Grassmannians and the cell decompositions of the projective spaces.
- [Simplicial and Singular Homology](simplicial-and-singular-homology.html), for the cellular homology used in the computations.
- [Characteristic Classes](characteristic-classes.html), for the Chern classes and the identity $c_1^2=2\chi+3\sigma$ used in the remark on $S^4$.
- [Real Topology](real-topology.html), for the one-point compactification of $\mathbb{R}^n$ and stereographic projection.
