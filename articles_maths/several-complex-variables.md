
# __Several Complex Variables__

## Introduction

This is the seventh article of the Complex Numbers system in Part V, and it occupies the **analysis slot** of that system. The system is the field $\mathbb{C}$ of *The Complex Numbers*, and the object of study is the theory of holomorphic functions of several complex variables: the functions of $n$ complex variables that are complex differentiable in each variable, the domains on which they live, the domains of holomorphy, pseudoconvexity, the inhomogeneous Cauchy–Riemann equation, the Cousin problems and the Stein manifolds on which the theory is at its cleanest.

The one-variable theory is from *Complex Analysis*, which constructs holomorphic functions, the Cauchy integral, the power series and the singularities; the present article assumes that theory and develops what is genuinely new from two variables upward. The new phenomena are not technical refinements but structural changes: a function holomorphic on a domain minus a compact set extends across the removed set (the Hartogs phenomenon), so there are no isolated singularities in dimension $\geq 2$; the Riemann mapping theorem fails, so there is no biholomorphic classification of domains; and the natural home of the theory is not the domain of the one-variable theory but the *domain of holomorphy*, characterised by holomorphic convexity and by pseudoconvexity. The formal apparatus of differential forms and the $\bar\partial$ operator is from *Differential Forms and Stokes' Theorem*, and the cohomological method by which the global problems are solved is from *Sheaf Cohomology*.

Throughout, $n \geq 2$ unless stated, $z = (z_1, \dots, z_n) \in \mathbb{C}^n$ with $z_j = x_j + iy_j$, and a **domain** is a connected open subset of $\mathbb{C}^n$. The **polydisc** of multiradius $r = (r_1, \dots, r_n)$ about $a$ is

$$
\Delta(a, r) = \{z : \lvert z_j - a_j\rvert < r_j,\ j = 1, \dots, n\},
$$

the unit ball is $B^n = \{z : \lvert z_1\rvert^2 + \cdots + \lvert z_n\rvert^2 < 1\}$, and the **Wirtinger operators** are $\partial/\partial z_j = \tfrac12(\partial/\partial x_j - i\partial/\partial y_j)$ and $\partial/\partial \bar z_j = \tfrac12(\partial/\partial x_j + i\partial/\partial y_j)$. The **Cauchy–Riemann operator** is $\bar\partial = \sum_j (\partial/\partial \bar z_j)\,d\bar z_j$, the sheaf of holomorphic functions is $\mathcal{O}$, the sheaf of nowhere-vanishing holomorphic functions is $\mathcal{O}^*$, the structure sheaf of a complex manifold is written $\mathcal{O}_X$, and $\Omega^p$ is the sheaf of holomorphic $p$-forms. The unit disc in $\mathbb{C}$ is $\Delta$.

## Holomorphic Functions of Several Variables

### Holomorphy and the Cauchy–Riemann Equations

**Definition.** Let $U \subseteq \mathbb{C}^n$ be open. A function $f : U \to \mathbb{C}$ is **holomorphic** if it is complex differentiable at every point, that is, real differentiable with a $\mathbb{C}$-linear differential; equivalently, if it is locally the sum of a convergent power series. The first condition is expressed by the system of Cauchy–Riemann equations

$$
\frac{\partial f}{\partial \bar z_j} = 0, \qquad j = 1, \dots, n ,
$$

which for $f = u + iv$ reads $\partial u/\partial x_j = \partial v/\partial y_j$ and $\partial u/\partial y_j = -\partial v/\partial x_j$ for every $j$.

**Theorem.** A function $f$ on a polydisc $\Delta(a,r)$ is holomorphic if and only if it is represented there by a convergent power series

$$
f(z) = \sum_{\alpha \in \mathbb{N}^n} c_\alpha (z-a)^\alpha, \qquad c_\alpha = \frac{1}{\alpha!}\,\frac{\partial^{\lvert\alpha\rvert} f}{\partial z^\alpha}(a),
$$

the series converging absolutely and uniformly on every compact subset of the polydisc.

**Proof.** If $f$ is holomorphic, iterating the one-variable Cauchy integral formula of *Complex Analysis* over the $n$ variables gives, for $z$ in a smaller polydisc,

$$
f(z) = \frac{1}{(2\pi i)^n}\int_{\lvert \zeta_j - a_j\rvert = r_j} \frac{f(\zeta)}{(\zeta_1 - z_1)\cdots(\zeta_n - z_n)}\,d\zeta_1\cdots d\zeta_n ,
$$

and expanding each factor $(\zeta_j - z_j)^{-1}$ as a geometric series gives the power series with the stated coefficients and the stated convergence. Conversely a convergent power series is continuous and holomorphic in each variable, so it is holomorphic. $\square$

**Theorem (Cauchy estimates and the identity theorem).** If $f$ is holomorphic on $\Delta(a,r)$ with $\lvert f\rvert \leq M$ then $\lvert c_\alpha\rvert \leq M r^{-\alpha}$. If $f$ vanishes on a nonempty open subset of a domain $D$, then $f \equiv 0$ on $D$.

**Proof.** The estimates follow from the integral formula by bounding the integrand. The identity theorem follows by applying the one-variable identity theorem successively in each variable along polydiscs, using that a domain in $\mathbb{C}^n$ is connected and the vanishing set is open and closed in it. $\square$

**Theorem (Weierstrass convergence theorem; Montel).** A sequence of holomorphic functions on a domain $D$ that converges uniformly on every compact subset of $D$ has a holomorphic limit, and the same is true of every derivative of the sequence. A locally bounded family of holomorphic functions on $D$ is normal: every sequence in it has a subsequence converging uniformly on compact subsets.

**Proof.** The first statement is a diagonal application of the one-variable Weierstrass theorem, or an application of Morera's theorem in each variable using the continuity of the limit; the second is Montel's theorem, obtained from the Cauchy estimates and the Arzelà–Ascoli theorem. $\square$

### Separate and Joint Holomorphy: Hartogs' Theorem

**Theorem (Hartogs).** Let $D \subseteq \mathbb{C}^n$ be a domain and let $f : D \to \mathbb{C}$ be holomorphic in each variable separately. Then $f$ is holomorphic.

**Proof.** The proof has two steps. First, Osgood's lemma: a separately holomorphic function is continuous, because the Cauchy integral formula in each variable expresses $f$ near a point as an integral of $f$ over a polydisc boundary, and the integrand is continuous in the parameter. Second, continuity together with separate holomorphy allows the iterated Cauchy integral over a polydisc, which produces the power series expansion, so $f$ is jointly holomorphic. Both steps use the one-variable Cauchy theory of *Complex Analysis*. $\square$

**Remark.** In one variable there is nothing to prove, since separate and joint holomorphy coincide by definition; in two and more variables the theorem is a genuine regularity statement. The power series expansion obtained in the proof shows that continuity is a consequence of separate holomorphy, and it is the first indication of the rigidity that governs the whole theory.

### The Hartogs Phenomenon

**Theorem (Hartogs extension).** Let $D \subseteq \mathbb{C}^n$ with $n \geq 2$ be a domain and let $K \subset D$ be compact with $D \setminus K$ connected. Then every holomorphic function on $D \setminus K$ extends holomorphically to $D$.

**Proof.** The classical proof uses a Hartogs figure: a suitable domain $H \subset D$, the union of a polydisc and a "chimney", such that every function holomorphic on $H$ extends to the ordinary polydisc containing it, by iterating the one-variable Cauchy formula along the chimney. Covering $D \setminus K$ by finitely many such figures and using the connectedness of $D \setminus K$ to propagate the extensions gives the theorem. The argument is Hartogs' and is in the references. $\square$

**Corollary.** In $n \geq 2$ variables there are no isolated singularities of holomorphic functions: a function holomorphic on a punctured polydisc $\Delta(a,r) \setminus \{a\}$ extends holomorphically over $a$.

**Proof.** Take $K = \{a\}$, a compact subset whose complement in the polydisc is connected. $\square$

**Remark.** The corollary is the sharpest contrast with the one-variable theory, in which a function holomorphic on a punctured disc may have an essential singularity and no extension. The phenomenon is caused by the abundance of directions: the singularity is surrounded, and the one-variable Cauchy formula applied in a ring, together with the connectedness of the complement, forces the Laurent expansion to have no negative part.

## Domains of Holomorphy

### The Envelope of Holomorphy

**Definition.** A domain $D \subseteq \mathbb{C}^n$ is a **domain of holomorphy** if there is a holomorphic function on $D$ that does not extend holomorphically to any larger domain; equivalently, if there is no pair of domains $D \subsetneq D'$ with every holomorphic function on $D$ extending to $D'$. The **envelope of holomorphy** of a domain $D$ is the largest domain to which every holomorphic function on $D$ extends.

**Theorem (existence of the envelope).** Every domain $D \subseteq \mathbb{C}^n$ has an envelope of holomorphy, and it is a domain of holomorphy.

**Proof.** The envelope is constructed as the space of germs of holomorphic functions on $D$ that are continuable along paths, with the natural projection to $\mathbb{C}^n$; the connectedness and the existence of a maximal spread domain are due to Cartan–Thullen and Oka. The construction is in the references. $\square$

**Example.** The domain $D = \Delta(0,1)^2 \setminus \overline{\Delta(0, 1/2)^2}$ in $\mathbb{C}^2$ has envelope the full bidisc $\Delta(0,1)^2$, by the Hartogs extension theorem; it is therefore not a domain of holomorphy, and it shows that the envelope may be strictly larger than the domain.

### Holomorphic Convexity

**Definition.** For a compact set $K$ in a domain $D \subseteq \mathbb{C}^n$, the **holomorphic hull** of $K$ in $D$ is

$$
\hat K_D = \left\{ z \in D : \lvert f(z)\rvert \leq \sup_K \lvert f\rvert \ \text{ for every } f \text{ holomorphic on } D \right\}.
$$

The domain $D$ is **holomorphically convex** if $\hat K_D$ is compact in $D$ for every compact $K \subset D$.

**Theorem (Cartan–Thullen).** A domain $D \subseteq \mathbb{C}^n$ is a domain of holomorphy if and only if it is holomorphically convex.

**Proof.** A point outside the hull of a compact set can be separated from it by a holomorphic function, and a sequence of such separations produces a holomorphic function on $D$ blowing up on any sequence approaching the boundary, which prevents extension; the converse uses the existence of the envelope and the compactness of the hulls. The theorem is Cartan and Thullen's; the details are in the references. $\square$

**Theorem (the hulls determine the envelope).** If $D$ is not holomorphically convex, then the envelope of holomorphy of $D$ contains $\hat K_D$ for a compact $K$ with noncompact hull, and every holomorphic function on $D$ extends across the added part.

**Proof.** The functions of $D$ are bounded on $\hat K_D$ by their supremum on $K$, so their power series at points of $K$ converge on an open set containing $\hat K_D$; the continuation gives the extension. $\square$

## Pseudoconvexity and the Levi Problem

### Plurisubharmonic Functions

**Definition.** An upper semicontinuous function $\varphi : U \to [-\infty, \infty)$ on an open $U \subseteq \mathbb{C}^n$ is **plurisubharmonic** if for every $z \in U$ and $w \in \mathbb{C}^n$ the function $\zeta \mapsto \varphi(z + \zeta w)$ of the complex variable $\zeta$ is subharmonic on its domain. A $\mathcal{C}^2$ function $\varphi$ is plurisubharmonic if and only if its **Levi form**

$$
L\varphi(z; w) = \sum_{j,k=1}^{n} \frac{\partial^2 \varphi}{\partial z_j \partial \bar z_k}(z)\, w_j \bar w_k
$$

is positive semidefinite for every $z$ and every $w$.

**Theorem.** A function $\varphi$ is plurisubharmonic if and only if it is locally the upper semicontinuous regularisation of the supremum of a family of functions of the form $c\log\lvert f\rvert$ with $f$ holomorphic and $c > 0$. In particular $\log\lvert f\rvert$ is plurisubharmonic for every holomorphic $f$, and plurisubharmonicity is invariant under biholomorphic maps.

**Proof.** The characterisation of plurisubharmonicity by holomorphic discs gives one direction: composing with a holomorphic map preserves plurisubharmonicity, and $\log\lvert\zeta\rvert$ is subharmonic in one variable. The converse is the standard approximation by $\log\lvert f\rvert$ in the definition of the pluricomplex Green function; the details are in the references. $\square$

**Definition.** A domain $D \subseteq \mathbb{C}^n$ is **pseudoconvex** if it has a continuous plurisubharmonic exhaustion function $\varphi : D \to \mathbb{R}$, that is, a plurisubharmonic $\varphi$ such that $\{z \in D : \varphi(z) < c\}$ is relatively compact in $D$ for every $c$. A domain with $\mathcal{C}^2$ boundary is pseudoconvex if and only if the Levi form of a defining function is positive semidefinite on the complex tangent space at every boundary point.

**Remark.** Pseudoconvexity is the local form of holomorphic convexity: the plurisubharmonic exhaustion measures the failure of the domain to extend across its boundary, and the Levi form is the second-order test for that failure. In one variable every domain is pseudoconvex, so the notion is new from two variables upward.

### The Levi Problem

**Theorem (Levi problem; Oka, Bremermann, Norguet).** A domain $D \subseteq \mathbb{C}^n$ is pseudoconvex if and only if it is a domain of holomorphy; equivalently, every pseudoconvex domain carries a holomorphic function that does not extend across any boundary point.

**Proof.** The implication from a domain of holomorphy to pseudoconvexity is a consequence of the Cartan–Thullen theorem together with the construction of a plurisubharmonic exhaustion from the holomorphically convex hulls. The converse, which is the substance of the theorem, is the solution of the Levi problem by Oka and independently by Bremermann and Norguet in the years 1942–1954: one solves the inhomogeneous Cauchy–Riemann equation with a plurisubharmonic barrier to construct the extending function. The proof is in the references. $\square$

**Corollary.** For domains in $\mathbb{C}^n$ the three conditions — domain of holomorphy, holomorphic convexity, pseudoconvexity — are equivalent.

**Proof.** The Cartan–Thullen theorem gives the first equivalence and the Levi problem the second. $\square$

## The $\bar\partial$-Equation and the Cohomological Method

### The Dolbeault Complex

**Definition.** For a domain $D \subseteq \mathbb{C}^n$, the **Dolbeault complex** is the sequence of sheaves and maps

$$
0 \to \mathcal{O} \to \Omega^0 \xrightarrow{\ \bar\partial\ } \Omega^{0,1} \xrightarrow{\ \bar\partial\ } \Omega^{0,2} \xrightarrow{\ \bar\partial\ } \cdots ,
$$

where $\Omega^{0,q}$ is the sheaf of $(0,q)$-forms and $\bar\partial$ is the Cauchy–Riemann operator; the complex is exact, so that the kernel of $\bar\partial$ on $\Omega^{0,q}$ is the image of $\bar\partial$ on $\Omega^{0,q-1}$.

**Theorem (Dolbeault).** For a domain $D \subseteq \mathbb{C}^n$ and $p, q \geq 0$ there is a natural isomorphism

$$
H^{p,q}_{\bar\partial}(D) \cong H^q(D, \Omega^p),
$$

where the left-hand side is the cohomology of the Dolbeault complex of $(p,q)$-forms and the right-hand side is the sheaf cohomology of the holomorphic $p$-forms.

**Proof.** The Dolbeault complex is a fine resolution of the sheaf $\Omega^p$, and the comparison theorem for resolutions by fine sheaves identifies its cohomology with the sheaf cohomology; the construction is in *Sheaf Cohomology*. $\square$

**Theorem (solvability of the $\bar\partial$-equation; Hörmander).** Let $D \subseteq \mathbb{C}^n$ be a pseudoconvex domain and let $f$ be a $\bar\partial$-closed $(0,q)$-form with $q \geq 1$ and square-integrable coefficients. Then there is a $(0,q-1)$-form $u$ with $L^2$ coefficients solving $\bar\partial u = f$, and the solution can be chosen with the estimate

$$
\int_D \lvert u\rvert^2 e^{-\varphi}\,dV \leq \int_D \lvert f\rvert^2 e^{-\varphi}\,dV
$$

for a suitable plurisubharmonic weight $\varphi$. For $q = 1$ the equation $\bar\partial u = f$ is solvable for every $\bar\partial$-closed $(0,1)$-form, and this is the technical heart of the theory of domains of holomorphy.

**Proof.** The theorem is Hörmander's, obtained by the $L^2$ estimates for the $\bar\partial$-Neumann problem and the weighted Hilbert space method; the pseudoconvexity supplies the plurisubharmonic weight. The proof is in the references. $\square$

**Corollary.** On a pseudoconvex domain $D$, $H^q(D, \mathcal{O}) = 0$ for every $q \geq 1$. In particular, for $n \geq 2$, if $K \subset D$ is compact and $D \setminus K$ is connected, then every holomorphic function on $D \setminus K$ extends holomorphically to $D$.

**Proof.** The vanishing is the Dolbeault isomorphism with the solvability of $\bar\partial$ in degree $(0,q)$ for $q \geq 1$, using $p = 0$; the extension statement is the combination with the Hartogs phenomenon and the Levi problem. $\square$

### The Cousin Problems

**Definition.** The **first Cousin problem** (additive) asks, given a domain $D$ and an open cover $\{U_i\}$ with holomorphic functions $f_{ij}$ on $U_i \cap U_j$ satisfying the cocycle conditions, for holomorphic $f_i$ on $U_i$ with $f_i - f_j = f_{ij}$. The **second Cousin problem** (multiplicative) asks the same question with the additive cocycle replaced by a nowhere-vanishing multiplicative one, $f_i/f_j = f_{ij}$.

**Theorem.** On a domain of holomorphy the first Cousin problem is always solvable. The second Cousin problem is solvable if and only if the class of the cocycle in $H^1(D, \mathcal{O}^*)$ vanishes, and in the equivalence-class form the obstruction is the image of the class under the connecting map

$$
H^1(D, \mathcal{O}^*) \longrightarrow H^2(D, \mathbb{Z})
$$

of the exponential sheaf sequence $0 \to \mathbb{Z} \to \mathcal{O} \xrightarrow{\exp} \mathcal{O}^* \to 0$.

**Proof.** The first problem is solved by the vanishing $H^1(D,\mathcal{O}) = 0$ of Cartan's theorem B below, which trivialises the cocycle. For the second, the long exact cohomology sequence of the exponential sequence gives $H^1(D, \mathcal{O}^*)/\operatorname{im} H^1(D,\mathcal{O}) \cong \ker(H^2(D,\mathbb{Z}) \to H^2(D,\mathcal{O}))$; since $H^1(D, \mathcal{O}) = 0$ and $H^2(D, \mathcal{O}) = 0$ on a domain of holomorphy by Cartan's theorem B, the Cousin class vanishes exactly when its image in $H^2(D,\mathbb{Z})$ does. The argument is in *Sheaf Cohomology*. $\square$

### Cartan's Theorems

**Theorem (Cartan's Theorem A).** Let $X$ be a Stein manifold and let $\mathcal{F}$ be a coherent analytic sheaf on $X$. Then the global sections of $\mathcal{F}$ generate every stalk: for every $x \in X$ the evaluation $H^0(X, \mathcal{F}) \to \mathcal{F}_x$ is surjective.

**Theorem (Cartan's Theorem B).** Let $X$ be a Stein manifold and let $\mathcal{F}$ be a coherent analytic sheaf on $X$. Then

$$
H^q(X, \mathcal{F}) = 0 \qquad \text{for all } q \geq 1 .
$$

**Proof.** The theorems are Cartan's, proved from Oka's coherence theorem and the solution of the $\bar\partial$-equation; the sheaf-theoretic proof is in *Sheaf Cohomology*. $\square$

**Corollary.** On a Stein manifold, $H^1(X, \mathcal{O}) = 0$, the first Cousin problem is always solvable, and $H^1(X, \mathcal{O}^*) \cong H^2(X, \mathbb{Z})$, so the second Cousin problem is obstructed exactly by an integral cohomology class.

**Proof.** The first two statements are Theorem B for $\mathcal{F} = \mathcal{O}$; the last is the exponential sequence together with $H^1(X,\mathcal{O}) = H^2(X,\mathcal{O}) = 0$. $\square$

## Stein Manifolds

### Definition and Characterisation

**Definition.** A **Stein manifold** is a complex manifold $X$ such that (i) $X$ is holomorphically convex, (ii) the holomorphic functions on $X$ separate the points of $X$, and (iii) the holomorphic functions give local coordinates at every point. A **Stein domain** is a domain of holomorphy in $\mathbb{C}^n$, and every domain of holomorphy is a Stein manifold.

**Theorem.** A connected complex manifold $X$ is Stein if and only if it is holomorphically convex and the holomorphic functions separate points and give local coordinates; equivalently, if and only if $X$ admits a strictly plurisubharmonic exhaustion function. Every closed complex submanifold of $\mathbb{C}^n$ is Stein, and every closed complex submanifold of a Stein manifold is Stein.

**Proof.** The equivalence of the two characterisations is the Levi problem on manifolds, solved by the same $\bar\partial$ methods; the heredity of the Stein property to closed submanifolds follows because the restrictions of the ambient holomorphic functions separate points and give coordinates, and the exhaustion restricts. $\square$

### Embedding and the Oka Principle

**Theorem (Remmert, Bishop, Narasimhan).** Every Stein manifold of dimension $n$ admits a proper holomorphic embedding into $\mathbb{C}^N$ for some $N$; in fact $N = 2n+1$ suffices.

**Proof.** The theorem is the embedding theorem for Stein manifolds, obtained from Cartan's Theorem A and the approximation results of Oka; the details are in the references. $\square$

**Theorem (Oka principle; Oka–Grauert).** Let $X$ be a Stein manifold and let $Y$ be a complex manifold that is the total space of a holomorphic fibre bundle with a complex Lie group as structure group. Then every continuous map $X \to Y$ is homotopic to a holomorphic map, and every continuous section of the bundle over $X$ is homotopic to a holomorphic section; more generally, for such bundles the holomorphic classification and the topological classification agree.

**Proof.** The principle is Oka's for the case of a complex Lie group and Grauert's for the general fibre bundle; the proof reduces the existence of holomorphic sections to the vanishing of the relevant cohomology by Cartan's theorems and a homotopy-theoretic induction. It is quoted from the literature. $\square$

**Remark.** The Oka principle is the global form of the rigidity of the theory: on Stein manifolds there is no obstruction to solving a holomorphic problem that cannot already be detected topologically, and the cohomological vanishing of Cartan's Theorem B is the algebraic content of that statement.

## Rigidity: How $n \geq 2$ Differs from $n = 1$

### The Failure of the Riemann Mapping Theorem

**Theorem (Poincaré).** The unit ball $B^n$ and the unit polydisc $\Delta^n$ are not biholomorphic for $n \geq 2$, although both are simply connected domains in $\mathbb{C}^n$.

**Proof.** The automorphism group of the ball is the projective unitary group $\operatorname{PU}(n,1)$, of real dimension $n^2 + 2n$: the stabiliser of the origin is the unitary group $U(n)$ and the group acts transitively on $B^n$. The automorphism group of the polydisc is $(\operatorname{Aut}\Delta)^n \rtimes S_n$, of real dimension $3n$, since each factor is the Möbius group $\operatorname{PU}(1,1) \cong \operatorname{PSL}(2,\mathbb{R})$, of dimension $3$. The two dimensions $n^2+2n$ and $3n$ agree only for $n = 1$, so the groups are not isomorphic as Lie groups and the domains are not biholomorphic. The computation of the automorphism groups is Poincaré's. $\square$

**Corollary.** In $n \geq 2$ variables there is no biholomorphic classification of simply connected domains: the Riemann mapping theorem of *Complex Analysis* is a strictly one-dimensional phenomenon, and the biholomorphic equivalence problem in $\mathbb{C}^n$ is a moduli problem without a discrete answer.

**Theorem (Fefferman).** A biholomorphism between smoothly bounded strictly pseudoconvex domains in $\mathbb{C}^n$ extends to a smooth diffeomorphism of the closures.

**Proof.** The theorem is Fefferman's; the extension is obtained from the boundary behaviour of the Bergman kernel and the asymptotic expansion of the Bergman metric near the boundary. It is quoted from the literature. $\square$

**Remark.** In one variable the boundary of a smoothly bounded domain is a curve and a conformal map need not extend smoothly, while in several variables the strong pseudoconvexity forces the boundary to be rigid enough that biholomorphisms extend. The rigidity is the geometric counterpart of the Hartogs phenomenon: the functions and the maps of the several-variable theory cannot behave locally as freely as in one variable.

## Analytic Varieties and the Local Structure

### The Weierstrass Preparation Theorem

**Definition.** A **Weierstrass polynomial** of degree $k$ in $z_n$ over the ring $\mathcal{O}_{\mathbb{C}^{n-1},0}$ is a polynomial $w(z') = z_n^k + a_1(z')z_n^{k-1} + \cdots + a_k(z')$ with coefficients $a_i$ holomorphic near $0$ and vanishing at $z' = 0$. A germ $f \in \mathcal{O}_{\mathbb{C}^n,0}$ is **regular of order $k$ in $z_n$** if $f(0, z_n)$ has a zero of order $k$ at $z_n = 0$.

**Theorem (Weierstrass preparation and division).** Let $f \in \mathcal{O}_{\mathbb{C}^n,0}$ be regular of order $k$ in $z_n$. Then $f$ factors uniquely as

$$
f = u \cdot w ,
$$

where $u$ is a unit in the local ring and $w$ is a Weierstrass polynomial of degree $k$ in $z_n$. Moreover, for every $g \in \mathcal{O}_{\mathbb{C}^n,0}$ there are unique $q$ and $r$ with $g = qf + r$, where $r$ is a polynomial in $z_n$ of degree less than $k$ over $\mathcal{O}_{\mathbb{C}^{n-1},0}$.

**Proof.** The division theorem is proved by the one-variable Weierstrass division applied to the holomorphic functions of $z_n$ with parameters $z'$, using the regularity to divide the polynomial part; the preparation theorem is the special case $g = z_n^k$. The details are in the references. $\square$

**Corollary.** The local ring $\mathcal{O}_{\mathbb{C}^n,0}$ is a unique factorization domain and a regular local ring of dimension $n$; hence the germ of a hypersurface is the zero set of a Weierstrass polynomial and has a local branched covering structure over $\mathbb{C}^{n-1}$.

**Proof.** Unique factorization follows from the preparation theorem by induction on $n$, beginning with the one-variable case, and the regular local ring statement is the computation of the maximal ideal of $\mathcal{O}_{\mathbb{C}^n,0}$, which is generated by $z_1, \dots, z_n$, together with the dimension. $\square$

### Coherence and the Nullstellensatz

**Theorem (Oka's coherence theorem).** The sheaf $\mathcal{O}$ of holomorphic functions on $\mathbb{C}^n$ is coherent, and the sheaf of ideals generated by finitely many holomorphic functions is coherent. Consequently every analytic set is locally the common zero set of finitely many holomorphic functions with coherent ideal sheaf.

**Proof.** The theorem is Oka's; the proof uses the Weierstrass preparation theorem to reduce the coherence of the ideal sheaf to the coherence of the structure sheaf, and it is the foundation of Cartan's theorems. It is quoted from the literature. $\square$

**Theorem (analytic Nullstellensatz).** Let $X$ be the germ of an analytic set at the origin of $\mathbb{C}^n$ and let $\mathcal{I}(X)$ be the ideal of germs vanishing on $X$. Then $\mathcal{I}(X)$ is the radical of the ideal generated by any set of local defining functions of $X$, and the local ring $\mathcal{O}_{X,0}$ is a reduced analytic algebra of finite dimension.

**Proof.** The statement is Rückert's and Oka's; the radical property is proved from the Weierstrass preparation theorem and the local parametrisation of $X$ as a branched covering of a polydisc in $\mathbb{C}^k$. $\square$

**Theorem (singular locus).** The set of singular points of an analytic set $X$ of pure dimension $k$ is a proper analytic subset of $X$; consequently the regular points form a dense open subset which is a complex manifold of dimension $k$.

**Proof.** The singular locus is locally the common zero set of the $(k \times k)$ minors of the Jacobian matrix of a set of defining functions, hence is analytic; it is proper because the regular points are dense in the local branched covering. This is the theorem of Oka and Remmert. $\square$

## Summary

Holomorphic functions of several complex variables are the functions satisfying the Cauchy–Riemann equations $\partial f/\partial\bar z_j = 0$ in each variable; by Hartogs' theorem separate holomorphy implies joint holomorphy, and holomorphic functions are exactly the locally convergent power series, with the Cauchy integral formula taken over polydiscs supplying the coefficients and the Cauchy estimates. The decisive novelty is the Hartogs extension theorem: in $n \geq 2$ variables a function holomorphic on a domain minus a compact set with connected complement extends across the removed set, so there are no isolated singularities and no compact singularities. The natural domains are the domains of holomorphy, equivalently by Cartan–Thullen the holomorphically convex domains, and equivalently by the solution of the Levi problem of Oka, Bremermann and Norguet the pseudoconvex domains, those carrying a plurisubharmonic exhaustion function.

The local and global problems of the theory are governed by the $\bar\partial$-equation and by sheaf cohomology: the Dolbeault isomorphism identifies the cohomology of the $\bar\partial$-complex with the sheaf cohomology of the holomorphic forms, Hörmander's $L^2$ estimates solve $\bar\partial u = f$ on pseudoconvex domains, and Cartan's Theorems A and B give the vanishing $H^q(X,\mathcal{F}) = 0$ for $q \geq 1$ on Stein manifolds, which solves the first Cousin problem and identifies the obstruction to the second with a class in $H^2(X,\mathbb{Z})$ via the exponential sheaf sequence. Stein manifolds are the holomorphically convex manifolds with enough holomorphic functions; they embed properly in some $\mathbb{C}^N$, and on them the Oka principle makes the holomorphic existence problems agree with the topological ones. The one-variable phenomena do not persist: the Riemann mapping theorem fails, as Poincaré's comparison of the ball and the polydisc shows, and Fefferman's boundary extension theorem replaces the flexible conformal theory by a rigid one. The analysis slot of the system $\mathbb{C}$ is thus enlarged from the one-variable theory of *Complex Analysis* to the several-variable theory, in which the Cauchy–Riemann operator, the plurisubharmonic functions and the cohomology of the structure sheaf take over the role of the Cauchy integral and the residue calculus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}^n$ | Complex $n$-space, $n \geq 2$ |
| $z_j = x_j + iy_j$ | Coordinates |
| $\Delta(a,r)$ | Polydisc of multiradius $r$ about $a$ |
| $\Delta^n$, $B^n$ | Unit polydisc and unit ball |
| $\partial/\partial z_j$, $\partial/\partial \bar z_j$ | Wirtinger operators |
| $\bar\partial$ | Cauchy–Riemann operator $\sum_j (\partial/\partial\bar z_j)\,d\bar z_j$ |
| $\mathcal{O}$, $\mathcal{O}^*$ | Sheaves of holomorphic and nowhere-vanishing holomorphic functions |
| $\mathcal{O}_X$ | Structure sheaf of a complex manifold $X$ |
| $\Omega^p$, $\Omega^{0,q}$ | Sheaves of holomorphic $p$-forms and of $(0,q)$-forms |
| $\hat K_D$ | Holomorphic hull of $K$ in $D$ |
| $L\varphi$ | Levi form of $\varphi$ |
| $H^{p,q}_{\bar\partial}(D)$ | Dolbeault cohomology |
| $H^q(X, \mathcal{F})$ | Sheaf cohomology |
| $U_i \cap U_j$, $f_{ij}$ | Cousin data, additive or multiplicative |
| $\operatorname{PU}(n,1)$ | Automorphism group of the ball |

## Further Reading

- Lars Hörmander, *An Introduction to Complex Analysis in Several Variables* (North-Holland, 3rd ed. 1990), for the $\bar\partial$-equation, the $L^2$ estimates and the Levi problem.
- Robert C. Gunning and Hugo Rossi, *Analytic Functions of Several Complex Variables* (Prentice–Hall, 1965), for domains of holomorphy, holomorphic convexity and the Cartan–Thullen theory.
- Hans Grauert and Reinhold Remmert, *Theory of Stein Spaces* (Springer, 1979), for Stein spaces, Cartan's Theorems A and B and the Oka principle.
- Kiyoshi Oka, *Sur les fonctions analytiques de plusieurs variables* (Iwanami, 1961), for the coherence theorem, the Levi problem and the origins of the subject.
- Hugo Rossi, "On envelopes of holomorphy", *Communications on Pure and Applied Mathematics* 16 (1963), for the existence and structure of the envelope of holomorphy.
- Steven G. Krantz, *Function Theory of Several Complex Variables* (American Mathematical Society, 2nd ed. 2001), for a general introduction to the geometry and function theory of domains in $\mathbb{C}^n$.
- Charles Fefferman, "The Bergman kernel and biholomorphic mappings of pseudoconvex domains", *Inventiones Mathematicae* 26 (1974), for the boundary extension of biholomorphisms.
