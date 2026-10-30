# __The Ball and the Bicylinder in $\mathbb{C}^2$__

## Introduction

The unit ball and the unit bicylinder are the two model bounded domains of $\mathbb{C}^2$: the ball
$$
\mathbb{B}^2=\{z:\lVert z\rVert^2=\lvert z_1\rvert^2+\lvert z_2\rvert^2<1\}
$$
and the bicylinder, also called the **polydisc**,
$$
\Delta^2=\{z:\lvert z_1\rvert<1,\ \lvert z_2\rvert<1\}.
$$
Both are bounded, convex, contractible and simply connected, both are domains of holomorphy, and both are homogeneous under a large group of biholomorphisms. They are nevertheless not biholomorphic, and the failure is the first structural difference between the analysis of one variable and the analysis of two.

This article treats the two domains, their automorphism groups, the proof that they are not biholomorphic, their boundary geometry, the failure of the Riemann mapping theorem that they exhibit, and the Reinhardt domains to which both belong. The general theory of domains of holomorphy and pseudoconvexity is *Several Complex Variables*; the Cauchy–Riemann equations and the maximum principle are *Analysis on $\mathbb{C}^2$*; the boundary integral is *The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$*. The notation is that of *Complex Two-Space*, and the Hermitian form is $H(z,w)=\sum_kz_k\overline{w_k}$.

**The ball and the bicylinder have the same topology and the same dimension, and different complex geometry.** The difference is read in three ways: the automorphism groups have dimensions $8$ and $6$, the boundary of the ball is strongly pseudoconvex everywhere while the boundary of the bicylinder is nowhere strongly pseudoconvex at its smooth points, and the Bergman metric of the ball has constant holomorphic sectional curvature while that of the bicylinder does not. The first is the classical proof of Poincaré, and it is the one given here in full.

## The Two Domains

**The ball is the unit ball of the Euclidean norm and the bicylinder is the product of two unit discs; the ball is contained in the bicylinder, and the two have different volumes and different boundaries.**

**Definition.** The **unit ball** and the **unit bicylinder** are
$$
\mathbb{B}^2=\{z:H(z,z)<1\},\qquad
\Delta^2=\Delta\times\Delta,\qquad
\Delta=\{w\in\mathbb{C}:\lvert w\rvert<1\}.
$$

**Proposition (inclusion and volume).** The ball is contained in the bicylinder, $\mathbb{B}^2\subset\Delta^2$, and the inclusion is strict. The volumes are
$$
\operatorname{vol}(\mathbb{B}^2)=\frac{\pi^2}{2},\qquad \operatorname{vol}(\Delta^2)=\pi^2,
$$
so the ball has half the volume of the bicylinder.

*Proof.* If $\lvert z_1\rvert^2+\lvert z_2\rvert^2<1$, then each summand is less than $1$, so $\lvert z_k\rvert<1$; the point $(1/\sqrt2,1/\sqrt2)$ lies in the bicylinder and on the sphere, so the inclusion is strict. The volume of the unit ball of $\mathbb{R}^4$ is $\pi^2/2$, and the volume of the bidisc is the square of the area $\pi$ of the disc.

**Proposition (convexity).** The two domains are convex, bounded, contractible and simply connected. The ball is strictly convex; the bicylinder is not.

*Proof.* The ball is a sublevel set of a strictly convex function, and the bicylinder is a product of convex sets. Convex sets are contractible, and the straight-line homotopy to the origin gives simple connectivity by *The Topology of $\mathbb{C}^2$*. The ball is strictly convex because its boundary contains no line segment; the bicylinder contains the segment $\{(1,t):-1\le t\le1\}$ in its boundary.

**Proposition (the boundaries).** The boundary of the ball is the sphere
$$
\partial\mathbb{B}^2=S^3=\{z:\lVert z\rVert=1\}.
$$
The boundary of the bicylinder is the union of two smooth pieces
$$
\partial\Delta^2=\bigl(\partial\Delta\times\overline{\Delta}\bigr)\cup\bigl(\overline{\Delta}\times\partial\Delta\bigr),
$$
which meet along the **distinguished boundary**
$$
T^2=\partial\Delta\times\partial\Delta=\{z:\lvert z_1\rvert=\lvert z_2\rvert=1\},
$$
a real two-dimensional torus. The boundary of the ball is a smooth three-manifold; the boundary of the bicylinder is not a manifold along $T^2$.

*Proof.* The boundary of the ball is the unit sphere. A point of the boundary of the bidisc has at least one coordinate of modulus $1$, which gives the two pieces; a point of both has both coordinates of modulus $1$. At a point of $T^2$ the boundary has a corner of real codimension two, so it is not locally homeomorphic to a half-space.

**Remark (the two boundaries are not interchangeable).** The boundary of the ball is a sphere and carries the Hopf fibration of *The Unit Sphere and the Hopf Fibration*; the boundary of the bicylinder is a union of two solid tori glued along their common torus boundary. **The topological difference is visible but is not by itself a biholomorphic invariant**, because a biholomorphism of bounded domains need not extend to the boundary. The invariant proof is the dimension of the automorphism group, below.

## The Automorphisms of the Ball

**Every biholomorphism of the ball is an element of the projective unitary group $\mathrm{PU}(2,1)$, a Lie group of real dimension $8$, acting transitively with isotropy $\mathrm{U}(2)$.**

**Definition.** Let $J=\operatorname{diag}(1,1,-1)$ on $\mathbb{C}^3$. The **indefinite unitary group** is
$$
\mathrm{U}(2,1)=\{A\in\mathrm{GL}_3(\mathbb{C}):A^{*}JA=J\},
$$
and the **projective unitary group** is $\mathrm{PU}(2,1)=\mathrm{U}(2,1)/\mathrm{U}(1)$, where $\mathrm{U}(1)$ is the centre of scalar matrices.

**Proposition (the action on the ball).** The group $\mathrm{PU}(2,1)$ acts on $\mathbb{CP}^2$ and preserves the ball, which is the set of classes
$$
\mathbb{B}^2=\{[Z_1:Z_2:Z_3]:\lvert Z_1\rvert^2+\lvert Z_2\rvert^2<\lvert Z_3\rvert^2\}.
$$
The action is faithful, and the group has real dimension $8$.

*Proof.* A matrix $A\in\mathrm{U}(2,1)$ preserves the Hermitian form $Z^{*}JZ$ of signature $(2,1)$, so it preserves the sign of the form on the class; the chart $Z_3\neq0$ with $z_k=Z_k/Z_3$ identifies the set with $\lVert z\rVert<1$. The centre acts trivially on classes, and the quotient acts faithfully. The Lie algebra consists of the matrices $X$ with $X^{*}J+JX=0$, a real vector space of dimension $9$; the centre has dimension $1$, so the projective group has dimension $8$.

**Theorem (the automorphisms are projective unitary).** Every biholomorphism of $\mathbb{B}^2$ is the restriction of an element of $\mathrm{PU}(2,1)$. Hence
$$
\operatorname{Aut}(\mathbb{B}^2)\cong\mathrm{PU}(2,1),
$$
a Lie group of real dimension $8$.

*Proof.* This is the theorem of Poincaré on the automorphisms of the ball; the proof uses the Schwarz lemma for the ball and the classification of the automorphisms fixing the origin, which are the unitary matrices. It is proved in *Several Complex Variables*.

**Theorem (transitivity and isotropy).** The group $\mathrm{PU}(2,1)$ acts transitively on $\mathbb{B}^2$. The isotropy group of the origin is isomorphic to $\mathrm{U}(2)$, of real dimension $4$, and
$$
\mathbb{B}^2\cong\mathrm{PU}(2,1)/\mathrm{U}(2)
$$
as a homogeneous space.

*Proof.* The transitivity is exhibited by the Möbius maps below. A projective unitary map fixing the origin fixes the complex line $[0:0:1]$, hence is represented by a block matrix $\operatorname{diag}(A,d)$ with $A\in\mathrm{U}(2)$ and $\lvert d\rvert=1$. Two such matrices represent the same projective map exactly when they differ by a scalar, and the class of $\operatorname{diag}(A,d)$ is determined by $A/d\in\mathrm{U}(2)$; hence the isotropy is $\mathrm{U}(2)$. The dimensions $8-4=4$ match the real dimension of the ball.

**Theorem (the Möbius maps).** For $a\in\mathbb{B}^2$, let $P_a$ be the orthogonal projection of $\mathbb{C}^2$ onto the complex line $\mathbb{C}a$ and define
$$
\varphi_a(z)=\frac{a-P_az-\sqrt{1-\lVert a\rVert^2}\,(I-P_a)z}{1-\langle z,a\rangle},\qquad \langle z,a\rangle=\sum_{k=1}^{2}z_k\overline{a_k}.
$$
Then $\varphi_a$ is a biholomorphism of $\mathbb{B}^2$ with
$$
\varphi_a(0)=a,\qquad \varphi_a(a)=0,\qquad \varphi_a\circ\varphi_a=\mathrm{id},
$$
and
$$
1-\lVert\varphi_a(z)\rVert^2=\frac{(1-\lVert a\rVert^2)(1-\lVert z\rVert^2)}{\lvert1-\langle z,a\rangle\rvert^2}.
$$

*Proof.* The value at $0$ is $a$ and the value at $a$ is $0$, because $P_aa=a$ and $(I-P_a)a=0$. The displayed identity is a direct computation with $\lVert P_az\rVert^2+\lVert(I-P_a)z\rVert^2=\lVert z\rVert^2$; it shows that $\lVert z\rVert<1$ implies $\lVert\varphi_a(z)\rVert<1$, and that the boundary goes to the boundary. The map is an involution, $\varphi_a\circ\varphi_a=\mathrm{id}$, by direct substitution; hence it is a biholomorphism.

**Remark (the model of the ball).** The ball is the bounded realisation of complex hyperbolic space $\mathbb{CH}^2$, and $\mathrm{PU}(2,1)$ is its group of holomorphic isometries for the Bergman metric. **The dimension $8$ is the dimension of the group, not of the space**; the space has real dimension $4$, and the isotropy has dimension $4$.

## The Automorphisms of the Bicylinder

**Every biholomorphism of the bicylinder is a permutation of the coordinates followed by a disc automorphism in each coordinate; the group is $(\mathrm{PSL}_2(\mathbb{R}))^2\rtimes S_2$, of real dimension $6$.**

**Definition.** The **disc automorphism group** is
$$
\operatorname{Aut}(\Delta)=\left\{z\longmapsto e^{i\theta}\frac{z-a}{1-\overline{a}z}:\lvert a\rvert<1,\ \theta\in\mathbb{R}\right\}.
$$
It is isomorphic to $\mathrm{PSL}_2(\mathbb{R})\cong\mathrm{PU}(1,1)$ and has real dimension $3$.

**Proposition (the disc group).** Every holomorphic bijection of the disc is of the displayed form. The group acts transitively on $\Delta$, and the isotropy of the origin is the circle $\mathrm{SO}(2)$.

*Proof.* A biholomorphism of the disc extends to the boundary circle and permutes the boundary; the Schwarz lemma applied to the automorphism and its inverse, after composing with a Möbius map sending the image of the origin to the origin, forces the form. The transitivity is the case $z=0$; the isotropy of $0$ is the rotations.

**Theorem (the automorphisms of the bicylinder).** Every biholomorphism of $\Delta^2$ is of the form
$$
(z_1,z_2)\longmapsto\bigl(\varphi_{\sigma(1)}(z_{\sigma(1)}),\varphi_{\sigma(2)}(z_{\sigma(2)})\bigr),
$$
where $\sigma\in S_2$ permutes the coordinates and $\varphi_j\in\operatorname{Aut}(\Delta)$. Hence
$$
\operatorname{Aut}(\Delta^2)\cong\bigl(\operatorname{Aut}(\Delta)\bigr)^2\rtimes S_2
\cong\bigl(\mathrm{PSL}_2(\mathbb{R})\bigr)^2\rtimes S_2,
$$
a Lie group of real dimension $6$.

*Proof.* This is the classical theorem of Poincaré on the automorphisms of the polydisc: a biholomorphism permutes the coordinate discs, and its restriction to each is a disc automorphism. It is proved in *Several Complex Variables* by the Schwarz lemma applied to the coordinate functions. The dimension is $2\cdot3=6$, the permutation being finite.

**Proposition (transitivity and isotropy).** The group $(\operatorname{Aut}(\Delta))^2$ acts transitively on $\Delta^2$, and the isotropy of the origin is $(\mathrm{SO}(2))^2\rtimes S_2$, of real dimension $2$. Hence
$$
\Delta^2\cong\bigl((\mathrm{PSL}_2(\mathbb{R}))^2\rtimes S_2\bigr)/\bigl((\mathrm{SO}(2))^2\rtimes S_2\bigr)
$$
as a homogeneous space, and the dimensions $6-2=4$ match.

*Proof.* For $a=(a_1,a_2)$, the product of the disc automorphisms sending $0$ to $a_k$ sends $0$ to $a$. A product of disc automorphisms fixing $0$ is a pair of rotations, and the permutation is the only remaining freedom.

**Remark (the two groups, side by side).** The ball has automorphism group $\mathrm{PU}(2,1)$ of dimension $8$, acting transitively with isotropy $\mathrm{U}(2)$ of dimension $4$; the bicylinder has automorphism group $(\mathrm{PSL}_2(\mathbb{R}))^2\rtimes S_2$ of dimension $6$, acting transitively with isotropy $(\mathrm{SO}(2))^2\rtimes S_2$ of dimension $2$. **The two groups have different dimensions, and the dimension is a biholomorphic invariant.** The next section turns the difference into the non-biholomorphism.

## The Non-Biholomorphism

**The ball and the bicylinder are not biholomorphic; a biholomorphism would conjugate the automorphism group of the ball onto that of the bicylinder, and the two groups have different dimensions.**

**Theorem (Poincaré).** There is no biholomorphism $\mathbb{B}^2\to\Delta^2$.

*Proof.* Suppose $F:\mathbb{B}^2\to\Delta^2$ is a biholomorphism. The map
$$
\Phi:\operatorname{Aut}(\mathbb{B}^2)\longrightarrow\operatorname{Aut}(\Delta^2),\qquad \Phi(g)=F\circ g\circ F^{-1},
$$
is an isomorphism of groups, with inverse $h\mapsto F^{-1}\circ h\circ F$. Both groups are Lie groups acting properly on the respective domains, and $\Phi$ is continuous for the compact-open topology, because composition with the fixed biholomorphisms $F$ and $F^{-1}$ is continuous; hence $\Phi$ is an isomorphism of Lie groups. An isomorphism of Lie groups preserves the dimension of the underlying manifold, so
$$
8=\dim\operatorname{Aut}(\mathbb{B}^2)=\dim\operatorname{Aut}(\Delta^2)=6,
$$
a contradiction.

**Corollary (the isotropy form).** The same contradiction is read at a point: a biholomorphism carries the isotropy group of a point of $\mathbb{B}^2$ isomorphically onto the isotropy group of its image, and these have dimensions $4$ and $2$.

*Proof.* The isotropy of the origin in $\mathrm{PU}(2,1)$ is $\mathrm{U}(2)$, of dimension $4$; the isotropy of the origin in $(\mathrm{PSL}_2(\mathbb{R}))^2\rtimes S_2$ is $(\mathrm{SO}(2))^2\rtimes S_2$, of dimension $2$. Conjugation by $F$ identifies the two.

**Remark (the dimension count is not the only proof).** The **Bergman metric** is a biholomorphic invariant, and its holomorphic sectional curvature is constant on the ball and not constant on the bicylinder: at the origin, the curvature of the bicylinder is the same in the coordinate directions and different in the diagonal direction, while the ball is homogeneous and has the same curvature in every direction. **The curvature is the analytic content of the difference**, and the dimension count is its group-theoretic shadow.

**Remark (the role of the boundary).** A second proof compares the boundaries. The boundary of the ball is strongly pseudoconvex at every point; the boundary of the bicylinder is not strongly pseudoconvex at any of its smooth points, because at $(1,0)$ the Levi form vanishes in the $z_2$ direction. **Strong pseudoconvexity is a local biholomorphic invariant of a smooth boundary point**, so a biholomorphism that extends across the boundary would carry one kind of point to the other. The boundary argument is the geometric form of the theorem, and the group argument avoids the question of the extension of $F$ to the boundary.

## The Boundary Geometry

**The boundary of the ball is a strongly pseudoconvex sphere; the boundary of the bicylinder is a union of two Levi-flat pieces glued along a torus, and its distinguished boundary is the torus.**

**Definition.** Let $\Omega=\{r<0\}$ be a domain with $C^2$ defining function $r$ and $\partial r\neq0$ on $\partial\Omega$. The **complex tangent space** at $p\in\partial\Omega$ is
$$
T_p^{\mathbb{C}}\partial\Omega=\left\{v\in\mathbb{C}^2:\sum_{k=1}^{2}v_k\frac{\partial r}{\partial z_k}(p)=0\right\},
$$
and the **Levi form** is
$$
\mathcal{L}_r(p)(v)=\sum_{j,k=1}^{2}\frac{\partial^2r}{\partial z_j\partial\bar z_k}(p)\,v_j\overline{v_k},\qquad v\in T_p^{\mathbb{C}}\partial\Omega.
$$
The boundary is **strongly pseudoconvex** at $p$ when $\mathcal{L}_r(p)$ is positive definite on $T_p^{\mathbb{C}}\partial\Omega$, and **Levi-flat** when it vanishes.

**Proposition (the ball is strongly pseudoconvex).** For the ball with $r=\lVert z\rVert^2-1$, the Levi form at every boundary point is
$$
\mathcal{L}_r(p)(v)=\lVert v\rVert^2,\qquad v\in T_p^{\mathbb{C}}\partial\Omega,
$$
which is positive definite on the complex tangent space of complex dimension $1$.

*Proof.* The mixed second derivatives are $\partial^2r/\partial z_j\partial\bar z_k=\delta_{jk}$, so the form is $\sum_k\lvert v_k\rvert^2$. The complex tangent space at $p$ is the complex line $\{v:\langle v,p\rangle=0\}$, of complex dimension $1$, and the form is positive on it.

**Proposition (the bicylinder is Levi-flat at its smooth points).** At the smooth boundary point $p=(1,0)$ of $\Delta^2$, with $r=\lvert z_1\rvert^2-1$, the complex tangent space is the $z_2$-line and the Levi form vanishes identically on it. Hence the boundary is not strongly pseudoconvex at $p$, and by symmetry at every smooth boundary point.

*Proof.* The defining function depends only on $z_1$; its mixed second derivative in $z_2$ is zero, so the Levi form is zero in the direction $v=(0,v_2)$. The point $(1,0)$ has $\lvert z_2\rvert=0<1$, so it is a smooth boundary point. The automorphisms of the bicylinder act transitively on the smooth boundary points, so the same holds everywhere.

**Remark (the shape of the two boundaries).** The boundary of the ball is a sphere $S^3$, foliated by the Hopf circles; it has no distinguished proper subset that carries the boundary values of holomorphic functions. **The boundary of the bicylinder has a distinguished boundary $T^2$**, the set where both coordinates have modulus $1$; the Cauchy formula of *Analysis on $\mathbb{C}^2$* integrates over this torus, and the other points of $\partial\Delta^2$ are not needed. The torus is the **Shilov boundary** of the bicylinder: the smallest closed set on which every continuous function holomorphic on the domain and continuous on the closure attains its maximum modulus. For the ball the Shilov boundary is the whole sphere.

**Remark (the edge is not a complex curve).** The torus $T^2$ is a real two-dimensional set, not a complex curve, and the boundary of the bicylinder is not a complex manifold. **The edge is the place where the two smooth pieces meet at a right angle**, and it is the reason the bicylinder is not strongly pseudoconvex: at the edge there is no tangent space at all, and at the smooth points the Levi form is degenerate.

## The Failure of the Riemann Mapping Theorem

**In one variable every simply connected proper domain of $\mathbb{C}$ is biholomorphic to the disc; in two variables the ball and the bicylinder are both simply connected and bounded, and they are not biholomorphic.**

**Theorem (Riemann, one variable).** Every simply connected proper domain of $\mathbb{C}$ is biholomorphic to the unit disc.

*Proof.* This is the Riemann mapping theorem of *Complex Analysis*; the proof is given there, by the normal family argument or by the Perron method.

**Theorem (the failure in two variables).** There is no biholomorphism between $\mathbb{B}^2$ and $\Delta^2$. Hence the Riemann mapping theorem fails in $\mathbb{C}^2$: two bounded simply connected domains need not be biholomorphic.

*Proof.* This is the theorem of the previous section. Both domains are bounded, convex and contractible, hence simply connected, so the hypotheses of the one-variable theorem are satisfied and the conclusion fails.

**Remark (there are infinitely many classes).** The failure is not a single exception. The **complex ellipsoids**
$$
E_m=\{z:\lvert z_1\rvert^2+\lvert z_2\rvert^{2m}<1\},\qquad m=1,2,3,\dots,
$$
are bounded, convex and simply connected. For $m=1$ the domain is the ball. For $m\ge2$ the Levi form at $(\pm1,0)$ vanishes to order $m-1$ in $\lvert z_2\rvert^2$, while the ball is strongly pseudoconvex there; the order of vanishing of the Levi form is a biholomorphic invariant of the smooth boundary point, so the domains $E_m$ are pairwise non-biholomorphic. **There are infinitely many biholomorphism classes of bounded simply connected domains in $\mathbb{C}^2$**, and no single model plays the role of the disc.

**Remark (what replaces the Riemann map).** In one variable the disc is the universal model because the uniformisation theorem reduces every simply connected domain to it. **In two variables there is no uniformisation**: the classification of bounded simply connected domains up to biholomorphism is a hard problem, and the invariants are the automorphism group, the boundary geometry and the Bergman metric, not a single normal form. The domains of holomorphy of *Several Complex Variables* are the right class, and even among them the classification is open.

## Reinhardt Domains

**A Reinhardt domain is invariant under the coordinatewise rotations of the torus $T^2$; the ball and the bicylinder are complete Reinhardt domains, and a complete Reinhardt domain is a domain of holomorphy exactly when its logarithmic image is convex.**

**Definition.** A domain $D\subset\mathbb{C}^2$ is **Reinhardt** when $(e^{i\theta_1}z_1,e^{i\theta_2}z_2)\in D$ for every $z\in D$ and every $(\theta_1,\theta_2)\in\mathbb{R}^2$. It is **complete Reinhardt** when moreover $(\lambda_1z_1,\lambda_2z_2)\in D$ for every $z\in D$ and every $\lambda_1,\lambda_2$ with $\lvert\lambda_k\rvert\le1$.

**Proposition (the two models are complete Reinhardt).** The ball and the bicylinder are complete Reinhardt domains.

*Proof.* Both are defined by conditions on $\lvert z_1\rvert$ and $\lvert z_2\rvert$ that are monotone in each modulus: $\lvert z_1\rvert^2+\lvert z_2\rvert^2<1$ and $\lvert z_k\rvert<1$. Multiplication by $e^{i\theta_k}$ leaves the moduli unchanged, and multiplication by $\lambda_k$ with $\lvert\lambda_k\rvert\le1$ decreases them.

**Definition.** The **logarithmic image** of a complete Reinhardt domain $D$ is
$$
\log D=\{(u_1,u_2)\in\mathbb{R}^2:(e^{u_1},e^{u_2})\in D\},
$$
with $u_k=\log\lvert z_k\rvert$; the domain is recovered from $\log D$ by rotation and by the completeness condition.

**Theorem (the logarithmic image and holomorphy).** A complete Reinhardt domain $D\subset\mathbb{C}^2$ is a domain of holomorphy exactly when its logarithmic image is convex.

*Proof.* This is the theorem of Hartogs on Reinhardt domains: the monomials $z^\alpha$ converge on the Reinhardt domain exactly when the logarithmic image is convex, and the convexity gives the holomorphic convexity that characterises domains of holomorphy (*Several Complex Variables*). The converse is the construction of a holomorphic function that blows up at a point outside the convex hull.

**Proposition (the two logarithmic images).** The logarithmic images are
$$
\log\mathbb{B}^2=\{(u_1,u_2):e^{2u_1}+e^{2u_2}<1\},\qquad
\log\Delta^2=\{(u_1,u_2):u_1<0,\ u_2<0\}.
$$
Both are convex, as the theorem requires.

*Proof.* The first is the sublevel set of the convex function $(u_1,u_2)\mapsto e^{2u_1}+e^{2u_2}$; the second is a quadrant. A sublevel set of a convex function is convex.

**Remark (the Reinhardt diagram).** The logarithmic image is the **Reinhardt diagram** of the domain. **The diagram of the bicylinder is a quadrant and the diagram of the ball is a curved convex region bounded by the curve $e^{2u_1}+e^{2u_2}=1$**; the two diagrams have the same dimension and different shapes, which is the combinatorial shadow of the non-biholomorphism. The Reinhardt domains are the natural testing ground for the theory of domains of holomorphy, and the ball and the bicylinder are the two simplest complete Reinhardt domains, one a product of discs and the other not.

**Remark (the Hartogs triangle).** A Reinhardt domain need not be complete: the **Hartogs triangle**
$$
H=\{z:\lvert z_1\rvert<\lvert z_2\rvert<1\}
$$
is Reinhardt and is a domain of holomorphy, but it is not complete, because the point $(0,1/2)$ lies in $H$ while $(0,0)$ does not. **The completeness is the condition that the logarithmic image contains the whole negative orthant below each of its points**, and the triangle fails it at the origin.

## Summary

The unit ball $\mathbb{B}^2$ and the unit bicylinder $\Delta^2$ are the two model bounded domains of $\mathbb{C}^2$. Both are bounded, convex, contractible, simply connected and domains of holomorphy; the ball is contained in the bicylinder, has half its volume, and has the sphere $S^3$ as boundary, while the boundary of the bicylinder is the union of two solid tori glued along the distinguished torus $T^2$.

The automorphism group of the ball is $\mathrm{PU}(2,1)$, a Lie group of real dimension $8$, acting transitively with isotropy $\mathrm{U}(2)$ of dimension $4$; the automorphism group of the bicylinder is $(\mathrm{PSL}_2(\mathbb{R}))^2\rtimes S_2$, of real dimension $6$, acting transitively with isotropy $(\mathrm{SO}(2))^2\rtimes S_2$ of dimension $2$. A biholomorphism would conjugate one group onto the other, so the dimensions would agree; they do not, and the two domains are not biholomorphic. The same contradiction is read at the isotropy groups, and the boundary gives a second proof: the ball is strongly pseudoconvex at every boundary point, the bicylinder is Levi-flat at every smooth boundary point.

The Riemann mapping theorem fails in $\mathbb{C}^2$: the ball and the bicylinder are both simply connected and not biholomorphic, and the complex ellipsoids $E_m$ give infinitely many classes. The ball and the bicylinder are complete Reinhardt domains; their logarithmic images are convex, as the theorem of Hartogs requires, and the diagrams are a quadrant and a curved convex region. The Hartogs triangle is a Reinhardt domain that is not complete, and it is a domain of holomorphy.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^2=\{z:\lVert z\rVert<1\}$ | the unit ball, a real four-dimensional domain |
| $\Delta^2=\Delta\times\Delta$ | the unit bicylinder, or polydisc |
| $T^2=\partial\Delta\times\partial\Delta$ | the distinguished boundary of the bicylinder |
| $\mathrm{U}(2,1)$ | the matrices preserving $\operatorname{diag}(1,1,-1)$ |
| $\mathrm{PU}(2,1)$ | the projective unitary group, $\operatorname{Aut}(\mathbb{B}^2)$ |
| $\mathrm{PSL}_2(\mathbb{R})$ | the disc automorphism group, $\operatorname{Aut}(\Delta)$ |
| $\varphi_a$ | the Möbius map of the ball sending $0$ to $a$ |
| $\mathcal{L}_r$ | the Levi form of the defining function $r$ |
| strongly pseudoconvex | positive definite Levi form on the complex tangent space |
| $\log D$ | the logarithmic image of a complete Reinhardt domain |
| $E_m=\{\lvert z_1\rvert^2+\lvert z_2\rvert^{2m}<1\}$ | the complex ellipsoids |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space, the norm and the Hermitian form.
- [The Topology of $\mathbb{C}^2$](the-topology-of-the-complex-two-space.html), for the ball, the sphere $S^3$ and simple connectivity.
- [Analysis on $\mathbb{C}^2$](analysis-on-the-complex-two-space.html), the previous article, for the Cauchy formula on the polydisc and the failure of the Riemann mapping theorem.
- [The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$](the-dbar-problem-and-the-bochner-martinelli-integral.html), for the boundary integral on a general domain.
- [Several Complex Variables](several-complex-variables.html), for domains of holomorphy, pseudoconvexity, the Levi form and the theorem of Poincaré on the automorphisms of the ball and the polydisc.
- [Complex Analysis](complex-analysis.html), for the Riemann mapping theorem and the automorphisms of the disc.
- [The Unit Sphere and the Hopf Fibration](the-unit-sphere-and-the-hopf-fibration.html), for the sphere $S^3$ as the boundary of the ball.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs and the typographic conventions of the corpus.
