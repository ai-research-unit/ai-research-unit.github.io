# __The Topology of $\mathbb{C}^2$__

## Introduction

This article treats the topology of the complex two-space as a real four-dimensional space: the Euclidean topology, the norm as a proper map, the unit ball and the unit sphere, the complement of the origin, and the homotopy type of the general linear group. It is the first of the three topological articles of the category; the compactifications are *The Compactifications of $\mathbb{C}^2$* and the unit sphere read as a bundle is *The Unit Sphere and the Hopf Fibration*.

The article treats the space and its subsets only. The complex structure, the three canonical forms and the holomorphic structure are not topological data, and the point of the article is to say exactly what the topology does and does not see. The general theory of the fundamental group and of covering spaces is *The Fundamental Group and Covering Spaces*; the homology is *Simplicial and Singular Homology*; the homotopy groups and the fibrations are *Homotopy Groups and Fibrations*; and the topology of the real space $\mathbb{R}^4$ is *Real Topology*. None of these is restated here.

**The topology of $\mathbb{C}^2$ is the topology of $\mathbb{R}^4$.** The complex structure is an extra operator, invisible to every topological invariant. The article makes that statement precise: the space is contractible, the punctured space is homotopy equivalent to the sphere $S^3$, and the general linear group is homotopy equivalent to $S^1\times S^3$.

## The Euclidean Topology

**The norm and the distance make $\mathbb{C}^2$ a metric space isometric to $\mathbb{R}^4$, and the topology is the product topology of the four real coordinates.**

**Definition.** The **norm** of $z=(z_1,z_2)$ is
$$
\lVert z\rVert=\sqrt{\lvert z_1\rvert^2+\lvert z_2\rvert^2},
$$
the **distance** is $d(z,w)=\lVert z-w\rVert$, and the **topology** is the metric topology of $d$.

**Proposition (the linear isometry).** The map
$$
\Phi:\mathbb{C}^2\longrightarrow\mathbb{R}^4,\qquad (z_1,z_2)\longmapsto(x_1,y_1,x_2,y_2),
$$
with $z_k=x_k+iy_k$, is a linear isometry onto $\mathbb{R}^4$ with the Euclidean norm. Hence the topology of $\mathbb{C}^2$ is the Euclidean topology of $\mathbb{R}^4$, equivalently the product of the two Euclidean topologies of the coordinate planes.

*Proof.* The map is bijective and real-linear, and
$$
\lVert z\rVert^2=\lvert z_1\rvert^2+\lvert z_2\rvert^2=x_1^2+y_1^2+x_2^2+y_2^2=\lVert\Phi(z)\rVert^2.
$$
A linear isometry is a homeomorphism, and the Euclidean topology of $\mathbb{R}^4$ is the product topology of the four coordinates.

**Proposition (the independence of the norm).** Any two norms on $\mathbb{C}^2$ are equivalent, so the topology does not depend on the choice of the norm.

*Proof.* This is the finite-dimensional statement that all norms on $\mathbb{R}^n$ are equivalent, applied through the linear isomorphism $\Phi$.

**Theorem (contractibility).** The space $\mathbb{C}^2$ is contractible.

*Proof.* The straight-line homotopy
$$
H:[0,1]\times\mathbb{C}^2\longrightarrow\mathbb{C}^2,\qquad H(t,z)=(1-t)z,
$$
is continuous, with $H(0,z)=z$ and $H(1,z)=0$.

**Corollary (the invariants).** The space $\mathbb{C}^2$ is path-connected and simply connected, its homotopy groups vanish in every degree,
$$
\pi_n(\mathbb{C}^2)=0\qquad(n\ge1),
$$
and its homology is that of a point, $H_0(\mathbb{C}^2;\mathbb{Z})=\mathbb{Z}$ and $H_k(\mathbb{C}^2;\mathbb{Z})=0$ for $k\ge1$.

*Proof.* A contractible space is homotopy equivalent to a point, and the homotopy and homology groups are homotopy invariants.

**Proposition (the global properties).** The space $\mathbb{C}^2$ is not compact, it is complete, it is $\sigma$-compact, and it is second countable.

*Proof.* The sequence $(n,0)$ has no convergent subsequence, so the space is not compact. A Cauchy sequence in $\mathbb{C}^2$ has Cauchy coordinate sequences in $\mathbb{C}\cong\mathbb{R}^2$, which converge, so the space is complete. It is the countable union of the closed balls of integer radius, and it has a countable base of products of rational balls.

The invariants are collected below.

| Property | Value |
|---|---|
| underlying space | $\mathbb{R}^4$ |
| real dimension | $4$ |
| compact | no |
| connected | yes |
| simply connected | yes |
| contractible | yes |
| homotopy groups | $\pi_n=0$ for $n\ge1$ |
| homology | $H_0=\mathbb{Z}$, $H_k=0$ for $k\ge1$ |
| complete | yes |
| $\sigma$-compact | yes |
| second countable | yes |

## The Norm as a Proper Map

**The norm is a proper map: the preimage of a compact set is compact. This is the metric form of the finite dimension of the space, and it is what makes the closed balls compact.**

**Definition.** A continuous map $f:X\to Y$ of locally compact spaces is **proper** when $f^{-1}(K)$ is compact for every compact $K\subset Y$.

**Theorem (properness of the norm).** The norm
$$
\lVert\cdot\rVert:\mathbb{C}^2\longrightarrow[0,\infty)
$$
is continuous, surjective and proper.

*Proof.* Continuity is the triangle inequality. Surjectivity is the existence of the vector $(r,0)$ for $r\ge0$. For properness, let $K\subset[0,\infty)$ be compact; then $K\subset[0,R]$ for some $R$, and
$$
\lVert\cdot\rVert^{-1}(K)\subset\{z:\lVert z\rVert\le R\},
$$
the closed ball of radius $R$. That ball is closed and bounded in $\mathbb{R}^4$, hence compact by Heine–Borel, and a closed subset of a compact set is compact.

**Corollary (Heine–Borel).** A subset of $\mathbb{C}^2$ is compact exactly when it is closed and bounded.

*Proof.* This is Heine–Borel in $\mathbb{R}^4$ read through the isometry $\Phi$. The direct half is the theorem above: a bounded set lies in a closed ball, and a closed subset of a compact set is compact.

**Corollary (closed balls are compact).** For every $R\ge0$, the closed ball
$$
\overline{B}^4_R=\{z:\lVert z\rVert\le R\}
$$
is compact, and the sphere $S^3_R=\{z:\lVert z\rVert=R\}$ is compact.

*Proof.* The ball is closed and bounded, hence compact; the sphere is a closed subset of the ball.

**Remark (properness is a finite-dimensional phenomenon).** The unit ball of an infinite-dimensional normed space is not compact, so the norm there is not proper. **Properness is exactly the property that fails in infinite dimensions and holds here because the space is $\mathbb{R}^4$.** It is the reason every closed bounded subset is compact, and it is used below to compactify the space by one point.

## The Unit Ball and the Unit Sphere

**The open unit ball is homeomorphic to the whole space, the closed unit ball is a compact manifold with boundary the unit sphere, and the unit sphere is compact, connected and simply connected but not contractible.**

**Definition.** The **open unit ball**, the **closed unit ball** and the **unit sphere** are
$$
B^4=\{z:\lVert z\rVert<1\},\qquad \overline{B}^4=\{z:\lVert z\rVert\le1\},\qquad S^3=\{z:\lVert z\rVert=1\}.
$$

**Proposition (the open ball is the space).** The map
$$
B^4\longrightarrow\mathbb{C}^2,\qquad w\longmapsto\frac{w}{1-\lVert w\rVert},
$$
is a homeomorphism with inverse $z\mapsto z/(1+\lVert z\rVert)$.

*Proof.* For $\lVert w\rVert<1$ the denominator is positive; for $z\in\mathbb{C}^2$, the point $z/(1+\lVert z\rVert)$ has norm $\lVert z\rVert/(1+\lVert z\rVert)<1$. The two formulas are inverse by direct computation, and both are continuous.

**Proposition (the closed ball).** The closed ball $\overline{B}^4$ is compact, contractible and a topological manifold with boundary $S^3$.

*Proof.* It is closed and bounded, hence compact; it is convex, hence contractible by the straight-line homotopy to the origin; and it is the standard closed ball of $\mathbb{R}^4$, whose boundary is the unit sphere.

**Theorem (the sphere).** The sphere $S^3$ is compact, connected, path-connected and simply connected. Its homology is
$$
H_0(S^3;\mathbb{Z})=\mathbb{Z},\qquad H_3(S^3;\mathbb{Z})=\mathbb{Z},\qquad H_k(S^3;\mathbb{Z})=0\quad(k\neq0,3),
$$
and its homotopy groups begin with $\pi_1(S^3)=\pi_2(S^3)=0$ and $\pi_3(S^3)=\mathbb{Z}$.

*Proof.* The sphere is closed and bounded, hence compact; it is connected and path-connected for every $n\ge1$; it is simply connected for $n\ge2$ (*The Fundamental Group and Covering Spaces*); its homology is computed by the standard cell decomposition $S^n=e^0\cup e^n$ (*Simplicial and Singular Homology*); and the Hurewicz theorem gives $\pi_3(S^3)\cong H_3(S^3)=\mathbb{Z}$ because the sphere is simply connected (*Homotopy Groups and Fibrations*).

**Theorem (not contractible).** The sphere $S^3$ is not contractible, and there is no retraction of the closed ball $\overline{B}^4$ onto $S^3$.

*Proof.* If $S^3$ were contractible, its homology would be that of a point, contradicting $H_3(S^3)=\mathbb{Z}$. If $r:\overline{B}^4\to S^3$ were a retraction and $i:S^3\to\overline{B}^4$ the inclusion, then $r\circ i=\mathrm{id}$ on $S^3$, so on homology $r_*\circ i_*=\mathrm{id}$ on $H_3(S^3)=\mathbb{Z}$. But $H_3(\overline{B}^4)=0$ because the ball is contractible, and $i_*:H_3(S^3)\to H_3(\overline{B}^4)$ is therefore the zero map, a contradiction.

**Remark (the Brouwer theorem).** The non-existence of a retraction is equivalent to the Brouwer fixed point theorem for the closed ball: a fixed-point-free continuous map $f:\overline{B}^4\to\overline{B}^4$ produces a retraction by following the ray from $f(x)$ through $x$ to the boundary. **The topology of the sphere is therefore the topological content of the fixed point theorem**, and the fixed point theorem is the reason the sphere cannot be contracted inside the ball (*Real Topology* and *Differential Topology*).

The three spaces are compared below.

| Space | Definition | Compact | Contractible | Boundary |
|---|---|---|---|---|
| open ball $B^4$ | $\lVert z\rVert<1$ | no | yes | $S^3$ in the closure |
| closed ball $\overline{B}^4$ | $\lVert z\rVert\le1$ | yes | yes | $S^3$ |
| sphere $S^3$ | $\lVert z\rVert=1$ | yes | no | empty |

## The Complement of the Origin

**The complement of the origin is homeomorphic to $S^3\times(0,\infty)$ and deformation retracts onto the unit sphere; it is therefore homotopy equivalent to $S^3$.**

**Theorem (polar coordinates).** The map
$$
\mathbb{C}^2\setminus\{0\}\longrightarrow S^3\times(0,\infty),\qquad z\longmapsto\left(\frac{z}{\lVert z\rVert},\lVert z\rVert\right),
$$
is a homeomorphism, with inverse $(\theta,r)\mapsto r\theta$.

*Proof.* The map is continuous, and so is the inverse. It is bijective: every nonzero $z$ is $r\theta$ with $r=\lVert z\rVert>0$ and $\theta=z/\lVert z\rVert\in S^3$, and the pair is unique.

**Corollary (the deformation retraction).** The map
$$
r:\mathbb{C}^2\setminus\{0\}\longrightarrow S^3,\qquad r(z)=\frac{z}{\lVert z\rVert},
$$
is a deformation retraction, with homotopy
$$
H(t,z)=\bigl((1-t)+t/\lVert z\rVert\bigr)z.
$$

*Proof.* At $t=0$ the map is the identity; at $t=1$ it is $r$; the formula is continuous on $\mathbb{C}^2\setminus\{0\}$ because $\lVert z\rVert>0$; and $r$ restricted to $S^3$ is the identity.

**Corollary (the invariants).** The punctured space is path-connected and simply connected, and
$$
\pi_1=\pi_2=0,\qquad \pi_3=\mathbb{Z},\qquad H_0=\mathbb{Z},\qquad H_3=\mathbb{Z},
$$
with all other reduced homology groups zero.

*Proof.* It is homotopy equivalent to $S^3$, whose invariants are those of the theorem above.

**Proposition (not the space).** The punctured space $\mathbb{C}^2\setminus\{0\}$ is not homeomorphic to $\mathbb{C}^2$.

*Proof.* The space $\mathbb{C}^2$ has $H_3=0$ because it is contractible, while the punctured space has $H_3=\mathbb{Z}$.

**Remark (the link of the origin).** The sphere $S^3$ is the **link** of the origin in $\mathbb{C}^2$: it is the intersection of a small sphere around the origin with the space, and its topology records the local structure of the space at the origin. **In real dimension four the link of a point is a three-dimensional sphere**, and the complement of the point is a cylinder over that link. The same picture in the plane gives a circle: $\mathbb{C}\setminus\{0\}\cong S^1\times(0,\infty)$, which is the punctured plane of *Complex Topology*.

**Remark (the fundamental group of a punctured space).** Removing a point from $\mathbb{R}^n$ does not change the fundamental group when $n\ge3$, because the complement deformation retracts onto $S^{n-1}$, which is simply connected. **The plane is the exception**: $\mathbb{R}^2\setminus\{0\}\simeq S^1$ has fundamental group $\mathbb{Z}$. The space $\mathbb{C}^2$ is on the simply connected side of that divide.

## The Group $\mathrm{GL}_2(\mathbb{C})$

**The general linear group is an open dense complex Lie group of real dimension eight; it deformation retracts onto the unitary group, and its homotopy type is that of $S^1\times S^3$.**

**Definition.** The **general linear group** is
$$
\mathrm{GL}_2(\mathbb{C})=\{A\in M_2(\mathbb{C}):\det A\neq0\},
$$
with the topology of $M_2(\mathbb{C})\cong\mathbb{C}^4\cong\mathbb{R}^8$.

**Proposition (open, dense and connected).** The group $\mathrm{GL}_2(\mathbb{C})$ is open and dense in $M_2(\mathbb{C})$, it is a complex Lie group of complex dimension $4$ and real dimension $8$, it is connected, and it is not compact.

*Proof.* The complement is the zero set of the determinant, a closed set with empty interior, so the group is open and dense. Multiplication and inversion are polynomial and rational, hence holomorphic. For connectedness, the polar decomposition below retracts the group onto the connected group $\mathrm{U}(2)$. The sequence $nI$ has no convergent subsequence, so the group is not compact.

**Theorem (polar decomposition).** Every $A\in\mathrm{GL}_2(\mathbb{C})$ is uniquely
$$
A=UP,\qquad U\in\mathrm{U}(2),\qquad P=P^{*}>0,
$$
with $P$ positive definite Hermitian. The map $A\mapsto U$ is continuous, and the homotopy
$$
H(t,A)=U\,P^{t},\qquad P^{t}=\exp(t\log P),
$$
is a deformation retraction of $\mathrm{GL}_2(\mathbb{C})$ onto $\mathrm{U}(2)$.

*Proof.* The matrix $A^{*}A$ is positive definite Hermitian, so it has a unique positive definite Hermitian square root $P=(A^{*}A)^{1/2}$; then $U=AP^{-1}$ satisfies $U^{*}U=P^{-1}A^{*}AP^{-1}=I$, so $U$ is unitary. The uniqueness follows from the uniqueness of the square root. The functional calculus makes $P^{t}$ continuous in $(t,P)$, and $P^{0}=I$, $P^{1}=P$, so the homotopy runs from $A$ to $U$.

**Proposition (the unitary group).** The unitary group is compact, connected and of real dimension $4$, and there is a diffeomorphism of manifolds
$$
\mathrm{U}(2)\longrightarrow\mathrm{SU}(2)\times\mathrm{U}(1),\qquad A\longmapsto\bigl(A\operatorname{diag}(\det(A)^{-1},1),\det A\bigr).
$$
Moreover $\mathrm{SU}(2)$ is homeomorphic to $S^3$.

*Proof.* The unitary group is closed and bounded in $M_2(\mathbb{C})$, hence compact, and it is the image of the connected space $\mathrm{SU}(2)\times\mathrm{U}(1)$ under the multiplication map, hence connected. The displayed map has inverse $(B,d)\mapsto B\operatorname{diag}(d,1)$: the first component has determinant $1$ and is unitary, and the two maps are smooth and inverse. Finally,
$$
\mathrm{SU}(2)=\left\{\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}:\alpha,\beta\in\mathbb{C},\ \lvert\alpha\rvert^2+\lvert\beta\rvert^2=1\right\},
$$
and the map to $S^3$, $\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}\mapsto(\alpha,\beta)$, is a homeomorphism.

**Corollary (the homotopy type).** There are homotopy equivalences
$$
\mathrm{GL}_2(\mathbb{C})\simeq\mathrm{U}(2)\simeq S^1\times S^3.
$$
Hence
$$
\pi_1(\mathrm{GL}_2(\mathbb{C}))=\mathbb{Z},\qquad \pi_2(\mathrm{GL}_2(\mathbb{C}))=0,\qquad \pi_3(\mathrm{GL}_2(\mathbb{C}))=\mathbb{Z}.
$$

*Proof.* The polar decomposition is a deformation retraction onto $\mathrm{U}(2)$; the diffeomorphism $\mathrm{U}(2)\cong\mathrm{SU}(2)\times\mathrm{U}(1)\cong S^3\times S^1$ gives the second equivalence; and the homotopy groups of a product are the products of the homotopy groups, with $\pi_1(S^1)=\mathbb{Z}$, $\pi_2(S^1)=0$, $\pi_3(S^1)=0$ and $\pi_1(S^3)=\pi_2(S^3)=0$, $\pi_3(S^3)=\mathbb{Z}$.

**Proposition (not simply connected).** The group $\mathrm{GL}_2(\mathbb{C})$ is not simply connected. The loop $t\mapsto\operatorname{diag}(e^{2\pi it},1)$ is not nullhomotopic.

*Proof.* The determinant sends the loop to $t\mapsto e^{2\pi it}$, a generator of $\pi_1(\mathbb{C}^{\times})=\mathbb{Z}$. A nullhomotopy of the loop would give a nullhomotopy of its determinant, which does not exist.

**Proposition (the special linear group).** The special linear group $\mathrm{SL}_2(\mathbb{C})=\{A:\det A=1\}$ is a complex Lie group of real dimension $6$, and the polar decomposition retracts it onto $\mathrm{SU}(2)\cong S^3$. In particular $\mathrm{SL}_2(\mathbb{C})$ is simply connected and $\pi_3(\mathrm{SL}_2(\mathbb{C}))=\mathbb{Z}$.

*Proof.* For $A\in\mathrm{SL}_2(\mathbb{C})$, the polar decomposition $A=UP$ has $1=\det A=\det U\det P=\det P$ with $\det P>0$ real, so $\det P=1$ and $\det U=1$; hence $U\in\mathrm{SU}(2)$. The retraction is the same homotopy as above.

**Proposition (the determinant fibration).** The determinant
$$
\det:\mathrm{GL}_2(\mathbb{C})\longrightarrow\mathbb{C}^{\times}
$$
is a surjective submersion with fibre $\mathrm{SL}_2(\mathbb{C})$, and its long exact sequence gives
$$
\pi_1(\mathrm{GL}_2(\mathbb{C}))\cong\mathbb{Z},\qquad \pi_2(\mathrm{GL}_2(\mathbb{C}))=0,\qquad \pi_3(\mathrm{GL}_2(\mathbb{C}))\cong\mathbb{Z}.
$$

*Proof.* The determinant is a surjective Lie group homomorphism with kernel $\mathrm{SL}_2(\mathbb{C})$; a surjective homomorphism of Lie groups with closed kernel is a principal bundle over its image, hence a fibration. It is surjective because $\operatorname{diag}(d,1)$ has determinant $d$, and its derivative is surjective at every point. The relevant part of the exact sequence is
$$
0=\pi_4(\mathbb{C}^{\times})\to\pi_3(\mathrm{SL}_2)\to\pi_3(\mathrm{GL}_2)\to\pi_3(\mathbb{C}^{\times})=0,
$$
$$
0=\pi_2(\mathrm{SL}_2)\to\pi_2(\mathrm{GL}_2)\to\pi_2(\mathbb{C}^{\times})=0,
$$
$$
0=\pi_1(\mathrm{SL}_2)\to\pi_1(\mathrm{GL}_2)\to\pi_1(\mathbb{C}^{\times})=\mathbb{Z}\to\pi_0(\mathrm{SL}_2)=0,
$$
using $\mathrm{SL}_2\simeq S^3$ and $\mathbb{C}^{\times}\simeq S^1$.

The groups are compared below. The column *homotopy type* records a space to which the group is homotopy equivalent.

| Group | Definition | Real dimension | Homotopy type | $\pi_1$ | $\pi_3$ |
|---|---|---|---|---|---|
| $\mathrm{GL}_2(\mathbb{C})$ | $\det A\neq0$ | $8$ | $S^1\times S^3$ | $\mathbb{Z}$ | $\mathbb{Z}$ |
| $\mathrm{SL}_2(\mathbb{C})$ | $\det A=1$ | $6$ | $S^3$ | $0$ | $\mathbb{Z}$ |
| $\mathrm{U}(2)$ | $A^{*}A=I$ | $4$ | $S^1\times S^3$ | $\mathbb{Z}$ | $\mathbb{Z}$ |
| $\mathrm{SU}(2)$ | $A^{*}A=I$, $\det A=1$ | $3$ | $S^3$ | $0$ | $\mathbb{Z}$ |
| $\mathbb{C}^{\times}$ | $z\neq0$ | $2$ | $S^1$ | $\mathbb{Z}$ | $0$ |

**Remark (the maximal compact subgroup).** The unitary group $\mathrm{U}(2)$ is a maximal compact subgroup of $\mathrm{GL}_2(\mathbb{C})$, and the polar decomposition is the Cartan decomposition of the group. **The group is an open eight-dimensional manifold homotopy equivalent to a compact four-dimensional manifold**, which is why its low-dimensional topology is that of $S^1\times S^3$ and not that of a point. The general theory of the classical groups is *The Classical Groups of $\mathbb{C}^2$*, and the matrix computations are the $M_2(\mathbb{C})$ Model articles of the biquaternion category.

## What the Topology Does Not See

**The topology sees the real dimension and nothing else; the complex structure, the Hermitian form and the holomorphic structure are extra data that no topological invariant records.**

The space $\mathbb{C}^2$ is homeomorphic to $\mathbb{R}^4$ and to the quaternions $\mathbb{H}$ read as a real vector space. Every real-linear isomorphism $\mathbb{C}^2\to\mathbb{R}^4$ is a homeomorphism, and it need not send the complex structure $J$ to the standard complex structure of $\mathbb{R}^4$; indeed $\mathbb{R}^4$ carries a whole family of complex structures, all with the same underlying topological space.

**Remark (the topology of the space and the topology of the structure).** The complex structure is visible in the **sheaf of holomorphic functions**, in the **Hermitian metric**, and in the **operator $J$**, but not in the underlying topological space. **Two complex structures on $\mathbb{R}^4$ give the same topological space and different complex geometry.** This is why the topology of $\mathbb{C}^2$ is exhausted by the statements above, and why the analysis and the geometry of the space are separate articles.

**Remark (the compactifications).** The one-point compactification of $\mathbb{C}^2$ is the sphere $S^4$, which admits no complex structure at all; the projective compactification is $\mathbb{CP}^2$, which is a complex manifold. **The choice of compactification is a choice of how much structure is added at infinity**, and it is the subject of the next article. The topology of the space alone does not select either.

## Summary

The complex two-space is isometric to $\mathbb{R}^4$ with the Euclidean norm, and its topology is the Euclidean topology of $\mathbb{R}^4$. It is contractible, path-connected and simply connected, with $\pi_n=0$ for all $n\ge1$ and the homology of a point; it is complete, $\sigma$-compact and second countable, and it is not compact. The norm is a proper map, so closed balls are compact and Heine–Borel holds. The open unit ball is homeomorphic to the whole space, the closed unit ball is a compact contractible manifold with boundary $S^3$, and the sphere $S^3$ is compact, connected, simply connected, of homology $\mathbb{Z}$ in degrees $0$ and $3$, and not contractible; there is no retraction of the ball onto its boundary.

The complement of the origin is homeomorphic to $S^3\times(0,\infty)$ and deformation retracts onto $S^3$, so it is simply connected with $\pi_3=\mathbb{Z}$ and $H_3=\mathbb{Z}$; it is not homeomorphic to the whole space. The general linear group $\mathrm{GL}_2(\mathbb{C})$ is an open dense complex Lie group of real dimension $8$; the polar decomposition retracts it onto the compact unitary group $\mathrm{U}(2)\cong\mathrm{SU}(2)\times\mathrm{U}(1)\cong S^3\times S^1$, so it has the homotopy type of $S^1\times S^3$, with $\pi_1=\mathbb{Z}$, $\pi_2=0$ and $\pi_3=\mathbb{Z}$, and it is not simply connected. The special linear group $\mathrm{SL}_2(\mathbb{C})$ retracts onto $\mathrm{SU}(2)\cong S^3$ and is simply connected. The topology sees the real dimension only; the complex structure is extra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lVert z\rVert=\sqrt{\lvert z_1\rvert^2+\lvert z_2\rvert^2}$ | the Euclidean norm |
| $d(z,w)=\lVert z-w\rVert$ | the distance |
| $B^4$ | the open unit ball, homeomorphic to $\mathbb{C}^2$ |
| $\overline{B}^4$ | the closed unit ball, compact with boundary $S^3$ |
| $S^3$ | the unit sphere, $\lVert z\rVert=1$ |
| $\mathbb{C}^2\setminus\{0\}\cong S^3\times(0,\infty)$ | the punctured space and its polar coordinates |
| $\mathrm{GL}_2(\mathbb{C})$ | the invertible matrices, homotopy equivalent to $S^1\times S^3$ |
| $\mathrm{SL}_2(\mathbb{C})$ | the matrices of determinant $1$, homotopy equivalent to $S^3$ |
| $\mathrm{U}(2)$, $\mathrm{SU}(2)$ | the unitary and special unitary groups |
| proper map | a map whose preimage of every compact set is compact |

## Further Reading

- [Real Topology](real-topology.html), for the topology of $\mathbb{R}^4$, compactness, Heine–Borel and the Brouwer theorem.
- [Complex Topology](complex-topology.html), for the one-dimensional analogue, the punctured plane and the circle.
- [The Fundamental Group and Covering Spaces](the-fundamental-group-and-covering-spaces.html), for simple connectivity and the fundamental group.
- [Simplicial and Singular Homology](simplicial-and-singular-homology.html), for the homology of the spheres and the cell decomposition.
- [Homotopy Groups and Fibrations](homotopy-groups-and-fibrations.html), for the homotopy groups, the Hurewicz theorem and the long exact sequence.
- [The Compactifications of $\mathbb{C}^2$](the-compactifications-of-the-complex-two-space.html), the next article, for the one-point and the projective compactifications.
- [The Unit Sphere and the Hopf Fibration](the-unit-sphere-and-the-hopf-fibration.html), the next article, for the bundle structure of $S^3$.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-the-complex-two-space.html), for the groups $\mathrm{GL}_2$, $\mathrm{SL}_2$, $\mathrm{U}(2)$ and $\mathrm{SU}(2)$ and their actions.
