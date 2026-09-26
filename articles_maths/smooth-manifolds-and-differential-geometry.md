
# __Smooth Manifolds and Differential Geometry__

## Introduction

A **smooth manifold** is a topological space that is locally modelled on $\mathbb{R}^n$, with the local models glued by smooth maps. The definition is the meeting point of the two structures of this Part: the topology supplies the open sets and the continuity, the smooth atlas supplies the calculus, and the whole of differential geometry is built by doing linear algebra in the tangent space at each point and letting the answer vary smoothly from point to point. The passage from the linear algebra of one tangent space to the geometry of the whole manifold is the subject of this article and the frame for the bundles and the curvature that follow.

This article develops the theory from its definitions. It defines topological and smooth manifolds, atlases and smooth structures, smooth maps and diffeomorphisms, and gives the standard examples — the Euclidean spaces, the spheres, the real projective spaces and the matrix groups. It defines the tangent space at a point both by derivations and by curves and proves the two definitions agree, defines the differential of a smooth map and proves the chain rule, and defines vector fields, their Lie bracket and the Lie algebra of a manifold. It treats submanifolds through the rank theorem and the implicit function theorem, obtains the spheres, the projective spaces and the classical groups as submanifolds of Euclidean or matrix space, and closes with the Riemannian metric, the length of a curve and the distance it induces, which recovers the topology of the manifold.

The article assumes the topological background of *Topological Spaces* and *Metric, Uniform and Complete Spaces*, including second countability, Hausdorffness, compactness and paracompactness; the partitions of unity it uses are those of *Paracompactness and Partitions of Unity*. From Part I it uses the exterior algebra of *The Exterior Algebra*, the determinant of *The Determinant and Alternating Forms*, and the general linear group of *The General Linear Group*. From the quadratic-forms category of this Part it uses the inner product and the orthogonal group of *Bilinear Forms* and *Isometries and Orthogonal Transformations*. The calculus of differential forms, the theory of bundles and connections, and the curvature and the geodesics of a metric are deferred. The existence and uniqueness theory of the ordinary differential equations that a vector field or a geodesic defines is deferred to Part III, where the limit and the differential equations are available. No physics is invoked.

## Charts, Atlases and Smooth Structures

### Topological Manifolds

**Definition.** A **topological manifold** of dimension $n$ is a topological space $M$ such that

**(a)** $M$ is Hausdorff;

**(b)** $M$ is second countable, that is, it has a countable base for its topology;

**(c)** every point of $M$ has a neighbourhood homeomorphic to an open subset of $\mathbb{R}^n$.

The three conditions are not redundant. Hausdorffness makes limits unique and prevents the line with two origins; second countability excludes the long line and makes partitions of unity available; the local Euclidean condition makes the space locally compact and locally path connected. The number $n$ is well defined, by the invariance of dimension, which is a theorem of algebraic topology and is quoted as standard.

**Definition.** A **chart** on $M$ is a pair $(U, \varphi)$ where $U \subseteq M$ is open and $\varphi : U \to \varphi(U) \subseteq \mathbb{R}^n$ is a homeomorphism onto an open set. The functions $x^i = \operatorname{pr}_i \circ \varphi$ are the **coordinate functions** of the chart. Two charts $(U, \varphi)$ and $(V, \psi)$ are **smoothly compatible** if either $U \cap V = \emptyset$ or the **transition map**

$$
\psi \circ \varphi^{-1} : \varphi(U \cap V) \longrightarrow \psi(U \cap V)
$$

is a diffeomorphism of open subsets of $\mathbb{R}^n$, that is, a bijection that is smooth with smooth inverse.

**Definition.** A **smooth atlas** on $M$ is a family of pairwise smoothly compatible charts whose domains cover $M$. Two atlases are **equivalent** if their union is again an atlas, and a **smooth structure** on $M$ is an equivalence class of atlases, equivalently a maximal atlas. A **smooth manifold** is a topological manifold together with a smooth structure.

**Remark.** A smooth structure is a genuine additional datum on a topological manifold. Milnor's examples of exotic smooth structures on the seven-sphere show that two smooth manifolds may be homeomorphic and not diffeomorphic; the topological and the smooth classifications are therefore different problems. Smooth structures exist on every topological manifold of dimension at most three, and the higher-dimensional existence question is the domain of surgery theory.

### Smooth Maps and Diffeomorphisms

**Definition.** Let $M$ and $N$ be smooth manifolds of dimensions $m$ and $n$. A continuous map $F : M \to N$ is **smooth** if for every pair of charts $(U, \varphi)$ on $M$ and $(V, \psi)$ on $N$ the composition

$$
\psi \circ F \circ \varphi^{-1} : \varphi(U \cap F^{-1}(V)) \longrightarrow \mathbb{R}^n
$$

is smooth as a map of open subsets of Euclidean spaces. The property is local, so it suffices to check it on a cover by charts, and it is independent of the atlases chosen in the equivalence classes.

**Definition.** A smooth map $F : M \to N$ is a **diffeomorphism** if it is bijective and its inverse is smooth. The set of diffeomorphisms $M \to M$ is a group under composition, written $\operatorname{Diff}(M)$.

**Definition.** The **rank** of a smooth map $F$ at a point $p$ is the rank of the linear map $dF_p : T_pM \to T_{F(p)}N$ defined below. A smooth map is an **immersion** if its rank equals $\dim M$ at every point, a **submersion** if its rank equals $\dim N$ at every point, and an **embedding** if it is an immersion that is a homeomorphism onto its image.

**Example (the Euclidean spaces).** The space $\mathbb{R}^n$ is a smooth manifold with the single chart $(\mathbb{R}^n, \mathrm{id})$, and every open subset of $\mathbb{R}^n$ is a smooth manifold with the restricted atlas. The sphere $S^{n-1}$ and the torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ are smooth manifolds; the torus carries the quotient smooth structure described in *Topological Spaces*, whose charts are the local inverses of the quotient map.

### Partitions of Unity

**Definition.** Let $\{U_\alpha\}$ be an open cover of a smooth manifold $M$. A **partition of unity subordinate** to the cover is a family $\{\rho_\alpha\}$ of smooth functions $\rho_\alpha : M \to [0, 1]$ such that

**(a)** the support of $\rho_\alpha$, the closure of $\{x : \rho_\alpha(x) \neq 0\}$, is contained in $U_\alpha$;

**(b)** every point has a neighbourhood on which only finitely many $\rho_\alpha$ are nonzero (the family is **locally finite**);

**(c)** $\sum_\alpha \rho_\alpha(x) = 1$ for every $x \in M$.

**Theorem.** Every smooth manifold admits a smooth partition of unity subordinate to any given open cover.

**Proof sketch.** Since $M$ is second countable and locally compact, it is paracompact; *Paracompactness and Partitions of Unity* supplies a locally finite refinement of the given cover and a subordinate partition of unity by continuous functions. Choosing a chart in each member of the refinement and smoothing the functions with a bump function produces smooth functions with the same supports, and normalising by their sum gives the stated partition. $\square$

**Remark.** The existence of smooth partitions of unity is what distinguishes the smooth category from the topological and the analytic categories: it is the mechanism by which local constructions are glued into global ones, and every global object constructed below by patching — a smooth function, a Riemannian metric, a vector field, a connection — uses it. The construction requires the local finiteness, which is why second countability and paracompactness are imposed in the definition of a manifold.

## The Tangent Space and the Differential

### Curves and Their Velocities

Let $M$ be a smooth manifold and $p \in M$. A **smooth curve** through $p$ is a smooth map $\gamma : (-\epsilon, \epsilon) \to M$ with $\gamma(0) = p$. In a chart $(U, \varphi)$ with $\varphi(p) = 0$, the curve has a coordinate expression $\varphi \circ \gamma$, and the velocity of the curve in this chart is the vector $(\varphi \circ \gamma)'(0) \in \mathbb{R}^n$.

**Definition.** Two smooth curves $\gamma_1, \gamma_2$ through $p$ are **tangent at $p$** if for one, hence every, chart $(U, \varphi)$ about $p$ one has $(\varphi \circ \gamma_1)'(0) = (\varphi \circ \gamma_2)'(0)$. Tangency at $p$ is an equivalence relation, and a **tangent vector** at $p$ is an equivalence class of smooth curves through $p$.

**Definition.** The set of tangent vectors at $p$ is the **tangent space** $T_pM$. It is a real vector space of dimension $n = \dim M$; the vector space structure is defined in a chart by the vector space structure of $\mathbb{R}^n$, and it is independent of the chart because the transition map is a diffeomorphism, so its derivative is a linear isomorphism.

A chart $(U, \varphi)$ with coordinates $x^1, \ldots, x^n$ determines a basis of $T_pM$ for $p \in U$: the class of the $i$-th coordinate curve $t \mapsto \varphi^{-1}(\varphi(p) + t e_i)$, written $\partial/\partial x^i|_p$ or $\partial_{x^i}|_p$. Every tangent vector is uniquely $v = \sum_i v^i \partial_{x^i}|_p$ with $v^i \in \mathbb{R}$, and under a change of chart the coefficients transform by the Jacobian of the transition map, the **chain rule** for tangent vectors.

### Derivations

**Definition.** A **derivation** at $p$ is an $\mathbb{R}$-linear map $D : C^\infty(M) \to \mathbb{R}$ satisfying the Leibniz rule

$$
D(fh) = D(f)\,h(p) + f(p)\,D(h)
$$

for all $f, h \in C^\infty(M)$. The set of derivations at $p$ is a real vector space, written $\operatorname{Der}_p(C^\infty(M))$.

**Theorem.** For every $p \in M$ the map from tangent vectors to derivations that sends the class of a curve $\gamma$ to $D_\gamma(f) = (f \circ \gamma)'(0)$ is a vector space isomorphism

$$
T_pM \longrightarrow \operatorname{Der}_p(C^\infty(M)).
$$

**Proof sketch.** The map is well defined because tangent curves give the same derivative of $f \circ \gamma$ by the chain rule, and it is linear. For injectivity, a derivation that kills every function has vanishing pairing with every coordinate function, hence the corresponding coordinate velocity vanishes. For surjectivity, let $D$ be a derivation and choose a chart with coordinates $x^i$ around $p$, which we may suppose is the origin. Writing $f$ in the chart and subtracting its Taylor expansion to first order expresses $f - f(p) - \sum_i (\partial f/\partial x^i)(0) x^i$ as a sum of products of functions vanishing at $0$; the Leibniz rule applied to those products shows that $D(f) = \sum_i D(x^i)\,(\partial f/\partial x^i)(0)$, so $D$ is the derivation of the vector $\sum_i D(x^i)\partial_{x^i}|_p$. $\square$

The theorem identifies the two definitions, and one writes a tangent vector as a derivation $v = \sum_i v^i \partial_{x^i}|_p$ acting on functions by $v(f) = \sum_i v^i \partial f/\partial x^i(p)$. This is the **directional derivative**.

### The Differential

**Definition.** Let $F : M \to N$ be a smooth map. The **differential** (or **tangent map** or **pushforward**) of $F$ at $p$ is the linear map

$$
dF_p : T_pM \longrightarrow T_{F(p)}N, \qquad dF_p(v)(f) = v(f \circ F),
$$

the tangent vector at $F(p)$ whose action on a function on $N$ is the action of $v$ on the pullback of that function.

**Theorem (chain rule).** For smooth maps $F : M \to N$ and $G : N \to P$ and a point $p \in M$,

$$
d(G \circ F)_p = dG_{F(p)} \circ dF_p,
$$

and $d(\mathrm{id}_M)_p = \mathrm{id}_{T_pM}$. Consequently, if $F$ is a diffeomorphism then $dF_p$ is invertible with inverse $d(F^{-1})_{F(p)}$.

**Proof.** For $v \in T_pM$ and $g \in C^\infty(P)$,

$$
d(G \circ F)_p(v)(g) = v\bigl(g \circ G \circ F\bigr) = dF_p(v)(g \circ G) = dG_{F(p)}\bigl(dF_p(v)\bigr)(g),
$$

which is the claim; the identity statement is immediate, and the inverse statement follows because $d(F^{-1})_{F(p)} \circ dF_p = d(\mathrm{id})_p = \mathrm{id}$. $\square$

In coordinates $x^1, \ldots, x^m$ on $M$ and $y^1, \ldots, y^n$ on $N$, the matrix of $dF_p$ in the bases $\partial_{x^i}$ and $\partial_{y^j}$ is the Jacobian matrix with entries $\partial F^j/\partial x^i(p)$, so the differential is the intrinsic form of the Jacobian.

**Definition.** The **tangent bundle** is the disjoint union

$$
TM = \bigsqcup_{p \in M} T_pM,
$$

with the projection $\pi : TM \to M$ sending $T_pM$ to $p$. The charts of $M$ induce charts of $TM$ making it a smooth manifold of dimension $2n$: over a chart $(U, \varphi)$ with coordinates $x^i$, the map $(p, \sum_i v^i \partial_{x^i}|_p) \mapsto (\varphi(p), v^1, \ldots, v^n)$ is a chart. The **cotangent bundle** $T^*M$ is defined dually.

The bundle structure of $TM$, its sections and its transition functions are the first example of the theory, and the tangent bundle is the model on which that theory is built.

## Vector Fields and the Lie Bracket

**Definition.** A **vector field** on $M$ is a smooth section of the tangent bundle, that is, a smooth map $X : M \to TM$ with $\pi \circ X = \mathrm{id}_M$. The space of vector fields is written $\mathfrak{X}(M)$; it is a module over the ring $C^\infty(M)$ and a real vector space. In a chart, $X = \sum_i X^i \partial_{x^i}$ with $X^i \in C^\infty(U)$, and $X$ acts on functions by $X(f) = \sum_i X^i \partial f/\partial x^i$.

**Definition.** The **Lie bracket** of vector fields $X$ and $Y$ is the vector field

$$
[X, Y](f) = X(Y(f)) - Y(X(f)), \qquad f \in C^\infty(M).
$$

**Proposition.** The bracket is well defined by the displayed expression, is skew-symmetric and bilinear over $\mathbb{R}$, satisfies the **Jacobi identity**

$$
[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0,
$$

and the **Leibniz rule**

$$
[X, fY] = X(f)\,Y + f\,[X, Y]
$$

for $f \in C^\infty(M)$. It is not a tensor: the value of $[X, Y]$ at $p$ depends on the first derivatives of the coefficients of $X$ and $Y$, not merely on their values at $p$.

**Proof.** The expression $X(Y(f)) - Y(X(f))$ is a derivation of $C^\infty(M)$ in $f$: the second-order terms cancel, because $XY(f) - YX(f)$ is the commutator of two first-order differential operators and its symbol is symmetric. Hence it defines a smooth vector field. Skew-symmetry is immediate; the Jacobi identity is the associativity of composition of the operators $X, Y, Z$ arranged cyclically; the Leibniz rule follows by expanding $X(fY)(h) - fY(X(h))$. $\square$

**Theorem.** The pair $(\mathfrak{X}(M), [\cdot, \cdot])$ is a real Lie algebra, the **Lie algebra of the manifold** $M$. For a Lie group, the left-invariant vector fields form a subalgebra isomorphic to the Lie algebra of the group, and the two notions agree; this is developed in *Lie Groups* and *The Lie Algebra and the Exponential Map*.

**Proof.** The module $\mathfrak{X}(M)$ is a real vector space and the bracket is bilinear, alternating and satisfies the Jacobi identity, which is the definition of a Lie algebra. $\square$

**Definition.** Vector fields $X$ and $Y$ **commute** if $[X, Y] = 0$. In a chart with coordinates $x^i$, the coordinate vector fields satisfy $[\partial_{x^i}, \partial_{x^j}] = 0$, and this is exactly the symmetry of the mixed partial derivatives.

**Remark (integral curves and flows).** An **integral curve** of a vector field $X$ is a smooth curve $\gamma$ with $\gamma'(t) = X(\gamma(t))$ for all $t$, where $\gamma'(t) = d\gamma_t(1)$ is the tangent vector of the curve. The standard existence and uniqueness theorem states that every smooth vector field has, about each point, a unique maximal integral curve through that point, and that the resulting local flow $\Phi_t$ is a local one-parameter group of local diffeomorphisms; the theorem is a statement in the theory of ordinary differential equations, and its proof, together with the analytic properties of the flow, belongs to Part III, where the differential equations are treated. What differential geometry uses is the geometric consequence: two vector fields commute exactly when their local flows commute, and the bracket $[X, Y]$ measures the failure of the infinitesimal parallelograms spanned by $X$ and $Y$ to close.

## Submanifolds, the Rank Theorem and Implicit Function Theorems

### Immersions, Submersions and Submanifolds

**Definition.** A subset $S$ of a smooth manifold $M$ is a **regular submanifold** of dimension $k$ if for every $p \in S$ there is a chart $(U, \varphi)$ of $M$ about $p$ with $\varphi(p) = 0$ such that

$$
\varphi(U \cap S) = \{x \in \varphi(U) : x^{k+1} = \cdots = x^n = 0\}.
$$

Such a chart is **adapted** to $S$. The subspace $S$ then carries a smooth structure of dimension $k$, with charts the restrictions of the adapted charts, and the inclusion $S \hookrightarrow M$ is an embedding.

**Theorem (rank theorem).** Let $F : M \to N$ be a smooth map of constant rank $r$ near $p$. Then there are charts $(U, \varphi)$ about $p$ and $(V, \psi)$ about $F(p)$ with $F(U) \subseteq V$ such that

$$
\psi \circ F \circ \varphi^{-1}(x^1, \ldots, x^m) = (x^1, \ldots, x^r, 0, \ldots, 0).
$$

Consequently, about a point of constant rank $r$, the map $F$ looks like the projection of the first $r$ coordinates followed by the inclusion of the first $r$ coordinates.

**Proof sketch.** The statement is local, so one may work in Euclidean spaces. Composing with linear isomorphisms reduces the derivative at $p$ to the standard form, and the inverse function theorem applied to the map $x \mapsto (F_1(x), \ldots, F_r(x), x^{r+1}, \ldots, x^m)$ produces a change of coordinates in which the first $r$ components of $F$ are the first $r$ coordinates and the remaining components have vanishing derivative; a further argument, using the constancy of the rank, shows the remaining components are independent of the first $r$ variables and then eliminates them by a second change of coordinates in the target. $\square$

**Theorem (implicit function theorem, manifold form).** Let $F : M \to N$ be a smooth map and let $c \in N$ be a **regular value**, meaning that $dF_p$ is surjective for every $p \in F^{-1}(c)$. Then $F^{-1}(c)$ is a regular submanifold of $M$ of dimension $\dim M - \dim N$, and its tangent space at $p$ is $\ker dF_p$.

**Proof sketch.** Regularity is open, so $F$ has rank $\dim N$ on a neighbourhood of each point of the preimage; the rank theorem then provides adapted coordinates in which the preimage is the common zero set of the last $\dim N$ coordinates, which is exactly the local model of a regular submanifold. The tangent space statement follows by differentiating $F \circ \iota = c$ for the inclusion $\iota$. $\square$

**Corollary.** A smooth map $F : M \to N$ with $\dim M = \dim N$ whose differential is invertible at $p$ is a local diffeomorphism near $p$; in particular, if in addition $F$ is bijective then $F$ is a diffeomorphism. This is the **inverse function theorem** in its manifold form.

### The Sard Theorem

**Definition.** A point $p \in M$ is a **critical point** of a smooth map $F : M \to N$ if $dF_p$ is not surjective, and a **critical value** is the image of a critical point. A point of $N$ that is not a critical value is a **regular value**.

**Theorem (Sard).** The set of critical values of a smooth map $F : M \to N$ has empty interior in $N$, equivalently the set of regular values is dense in $N$. The sharper statement, that the critical values form a null set, is proved in Part III, where the measure is available.

The theorem is stated here for completeness, because it guarantees that regular values are dense and hence that the regular-value constructions of topology are always available; its proof uses the measure and the covering arguments of Part III, where the measure is introduced, and it is quoted as standard. The differential-topological consequences — transversality, degree theory, the Whitney embedding theorem — are developed.

## The Manifold Structure of the Spheres and Classical Groups

### The Spheres

**Definition.** For $n \geq 1$ the **unit sphere** is

$$
S^{n-1} = \{x \in \mathbb{R}^n : \langle x, x\rangle = 1\},
$$

where $\langle\cdot,\cdot\rangle$ is the standard positive definite inner product of *Bilinear Forms*.

**Theorem.** The sphere $S^{n-1}$ is a smooth manifold of dimension $n-1$.

**Proof.** Define $f : \mathbb{R}^n \to \mathbb{R}$ by $f(x) = \langle x, x\rangle$. Its differential at $x$ is $df_x(v) = 2\langle x, v\rangle$, which is surjective whenever $x \neq 0$, since $df_x(x) = 2\langle x, x\rangle \neq 0$. Hence $1$ is a regular value of $f$, and $S^{n-1} = f^{-1}(1)$ is a regular submanifold of dimension $n-1$ by the implicit function theorem. $\square$

**Example.** The manifold structure is also visible in charts: the two hemispheres $x^n > 0$ and $x^n < 0$ are graphs over the ball, with coordinates $x^1, \ldots, x^{n-1}$ and the last coordinate recovered as $\pm(1 - |x'|^2)^{1/2}$; on the overlap $|x'| < 1$, the transition map is a diffeomorphism of the open ball. The smooth structure obtained from the implicit function theorem agrees with this one.

**Theorem.** The sphere $S^{n-1}$ is compact and connected, and for $n = 2$ it is the circle $S^1$.

**Proof.** It is closed and bounded in $\mathbb{R}^n$, hence compact; it is path connected for $n \geq 2$, since any two points are joined by an arc of a great circle, and connected. $\square$

### The Real Projective Spaces

**Definition.** The **real projective space** $\mathbb{RP}^n$ is the quotient of $\mathbb{R}^{n+1} \setminus \{0\}$ by the equivalence relation $x \sim \lambda x$ for $\lambda \in \mathbb{R}^\times$, equivalently the set of lines through the origin in $\mathbb{R}^{n+1}$. It is written also as the quotient $S^n/\{\pm 1\}$ of the sphere by the antipodal action.

**Theorem.** The space $\mathbb{RP}^n$ is a compact smooth manifold of dimension $n$.

**Proof sketch.** For $i = 0, \ldots, n$ let $U_i$ be the set of lines not contained in the hyperplane $x^i = 0$; the map sending a line to the affine coordinates $(x^0/x^i, \ldots, \widehat{x^i/x^i}, \ldots, x^n/x^i)$ is a homeomorphism onto $\mathbb{R}^n$, and the transition maps are smooth rational functions, so the $U_i$ form a smooth atlas with $n+1$ charts. Compactness is the compactness of $S^n$ under the quotient map. $\square$

### The Classical Matrix Groups

**Theorem.** The general linear group $GL_n(\mathbb{R})$ is an open submanifold of the space $M_n(\mathbb{R}) \cong \mathbb{R}^{n^2}$ of dimension $n^2$, because it is the preimage of the open set $\mathbb{R}^\times$ under the continuous determinant.

**Theorem.** The orthogonal group

$$
O(n) = \{A \in GL_n(\mathbb{R}) : A^T A = I\}
$$

is a compact smooth submanifold of $M_n(\mathbb{R})$ of dimension $n(n-1)/2$, and the special orthogonal group $SO(n) = \{A \in O(n) : \det A = 1\}$ is a submanifold of the same dimension.

**Proof.** Consider $F : M_n(\mathbb{R}) \to \operatorname{Sym}_n(\mathbb{R})$, $F(A) = A^T A$, where $\operatorname{Sym}_n$ is the space of symmetric matrices, of dimension $n(n+1)/2$. Its differential at $A$ is $dF_A(H) = A^T H + H^T A$. For $A \in O(n)$, this map is surjective: given a symmetric $S$, take $H = \frac{1}{2} A S$, then $A^T H + H^T A = \frac{1}{2}S + \frac{1}{2}S = S$. Hence $I$ is a regular value, and $O(n) = F^{-1}(I)$ is a submanifold of dimension $n^2 - n(n+1)/2 = n(n-1)/2$. It is bounded in $M_n(\mathbb{R})$ and closed, hence compact; $SO(n)$ is a union of components, cut out by the condition $\det = 1$. $\square$

**Theorem.** The unitary group $U(n)$ is a smooth submanifold of $M_n(\mathbb{C}) \cong \mathbb{R}^{2n^2}$ of real dimension $n^2$, and the special unitary group $SU(n)$ has real dimension $n^2 - 1$.

**Proof.** The same argument applied to $F(A) = A^* A$ with values in the real vector space of Hermitian matrices, of real dimension $n^2$, gives $\dim U(n) = 2n^2 - n^2 = n^2$; the determinant maps $U(n)$ onto the unit circle with kernel $SU(n)$, and the derivative of the determinant is surjective, so $SU(n)$ is a submanifold of dimension $n^2 - 1$. $\square$

These groups are the classical groups of *Matrix Groups and Classical Groups*, and they are Lie groups in the sense of *Lie Groups*: the group operations are smooth because they are given by polynomial and rational expressions in the matrix entries, and the manifold structure is the one produced here.

**Example (the three-sphere as the unit quaternions).** The unit sphere $S^3$, viewed as the set of unit quaternions, is a Lie group of dimension $3$ under quaternion multiplication, and the map $S^3 \to SO(3)$ sending a unit quaternion $q$ to conjugation $p \mapsto qpq^{-1}$ on the imaginary subspace is a two-to-one covering homomorphism, as in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*. This identifies $S^3$ with $SU(2)$ and realises the double cover $SU(2) \to SO(3)$ of *Matrix Groups and Classical Groups*.

## Riemannian Metrics and the Associated Distance

### Riemannian Metrics

**Definition.** A **Riemannian metric** on a smooth manifold $M$ is a smooth assignment to each $p \in M$ of a positive definite inner product $g_p$ on the tangent space $T_pM$, in the sense that for every chart $(U, \varphi)$ with coordinates $x^i$ the functions

$$
g_{ij}(p) = g_p\!\left(\frac{\partial}{\partial x^i}\Big|_p, \frac{\partial}{\partial x^j}\Big|_p\right)
$$

are smooth on $U$, and the matrix $(g_{ij}(p))$ is symmetric and positive definite at every $p$. A **Riemannian manifold** is a pair $(M, g)$.

**Theorem.** Every smooth manifold carries a Riemannian metric.

**Proof.** Choose an atlas $\{U_\alpha\}$ and a subordinate smooth partition of unity $\{\rho_\alpha\}$. On each chart domain pull back the standard inner product of $\mathbb{R}^n$ along the coordinate map to obtain a positive semidefinite symmetric form $g_\alpha$ on $U_\alpha$, definite on $U_\alpha$; put

$$
g = \sum_\alpha \rho_\alpha\, g_\alpha.
$$

The sum is finite near each point by local finiteness, its coefficients are smooth, and it is positive definite because at each point at least one $\rho_\alpha$ is positive and the corresponding $g_\alpha$ is definite there. $\square$

**Example (the Euclidean metric).** On $\mathbb{R}^n$ the standard metric is $g_{ij} = \delta_{ij}$, whose value at $x$ is the standard inner product on the tangent space $\mathbb{R}^n$.

**Example (the round sphere).** The inclusion $S^{n-1} \hookrightarrow \mathbb{R}^n$ restricts the standard inner product to the tangent spaces of the sphere, giving the **round metric** of constant curvature; the induced distance is the great-circle distance treated.

**Example (the hyperbolic metric).** On the upper half-space with coordinates $y > 0$ in $\mathbb{R}^n$ the metric $g = (dx_1^2 + \cdots + dx_n^2)/y^2$ is positive definite, and it is the **hyperbolic metric** whose geometry is developed.

### Length and the Induced Distance

**Definition.** The **speed** of a smooth curve $\gamma : [a, b] \to M$ at $t$ is the nonnegative real number

$$
|\gamma'(t)|_g = \sqrt{g_{\gamma(t)}\bigl(\gamma'(t), \gamma'(t)\bigr)},
$$

where $\gamma'(t) = d\gamma_t(1)$. The **length** of $\gamma$ is

$$
L_g(\gamma) = \int_a^b |\gamma'(t)|_g\, dt,
$$

the integral being the elementary Riemann integral of the continuous function $t \mapsto |\gamma'(t)|_g$ in any chart covering the image; the value is independent of the chart by the change-of-variables formula. The integral here is one-dimensional and is the integral read on a curve; the measure-theoretic theory of the length of merely rectifiable curves, and the existence of minimisers in general, belong to Part III, where the measure and the limit are available.

**Theorem.** The length is invariant under reparametrisation: if $\sigma : [c, d] \to [a, b]$ is a smooth increasing surjection and $\gamma$ a smooth curve, then $L_g(\gamma \circ \sigma) = L_g(\gamma)$. Consequently the length of a piecewise smooth curve depends only on its image and its orientation.

**Proof.** The chain rule gives $(\gamma \circ \sigma)'(t) = \sigma'(t)\,\gamma'(\sigma(t))$, hence $|(\gamma \circ \sigma)'(t)|_g = \sigma'(t)\,|\gamma'(\sigma(t))|_g$, and the change-of-variables formula in one variable gives the result. $\square$

**Definition.** For $p, q \in M$ the **Riemannian distance** is

$$
d_g(p, q) = \inf \{ L_g(\gamma) : \gamma \text{ piecewise smooth from } p \text{ to } q \},
$$

the infimum being taken over all piecewise smooth curves joining the two points; the infimum is finite because $M$ is connected, and $d_g(p, q) = 0$ if and only if $p = q$, since any two distinct points have disjoint neighbourhoods and a curve joining them has length bounded below by the distance between the neighbourhoods in a chart.

**Theorem.** The function $d_g$ is a metric on $M$, and its metric topology is the given topology of $M$.

**Proof sketch.** Symmetry and the triangle inequality follow from reversing and concatenating curves; positivity and separation were noted. For the topology, one shows that a point and the complement of a small geodesically convex ball of radius $r$ are at distance at least $r$ from each other, using the fact that the exponential map of the metric provides a coordinate system in which the metric is close to Euclidean; hence the metric balls generate the given topology. $\square$

The metric $d_g$ is the distance that this Part places on the manifold, and it is the object that allows all the topological and metric notions of *Metric, Uniform and Complete Spaces* to be applied to $M$. The finer metric theory — geodesics, completeness, curvature and the comparison theorems — is the subject of the two articles.

**Remark (metric versus topological invariants).** Two Riemannian metrics on the same manifold may induce the same topology and different distances, as the metrics $|x - y|$ and $|\arctan x - \arctan y|$ on $\mathbb{R}$ do in *Metric, Uniform and Complete Spaces*. The distance therefore retains information — completeness, boundedness, the growth of balls — that the topology alone discards, and that information is what the geometry of the manifold is about.

## Summary

A topological manifold is a second-countable Hausdorff space locally homeomorphic to $\mathbb{R}^n$; a smooth structure is a maximal atlas of smoothly compatible charts, and a smooth manifold is the pair. Smooth maps are those whose coordinate expressions are smooth, diffeomorphisms are the isomorphisms of the category, and smooth partitions of unity subordinate to any open cover are the gluing device that the rest of the theory uses.

The tangent space $T_pM$ may be defined by equivalence classes of curves through $p$ or as the derivations of the algebra of smooth functions at $p$, and the two definitions agree; it is a vector space of dimension $n$ with a basis of coordinate derivations $\partial_{x^i}$ in each chart. The differential $dF_p : T_pM \to T_{F(p)}N$ is the intrinsic form of the Jacobian and satisfies the chain rule, so it is the functorial part of the theory. Vector fields are sections of the tangent bundle, they form the real Lie algebra $\mathfrak{X}(M)$ under the bracket $[X, Y](f) = X(Y(f)) - Y(X(f))$, and the bracket measures the failure of the flows of the fields to commute; the existence of the flows is a differential-equation statement deferred to Part III.

A regular submanifold is one that looks locally like a coordinate subspace, the rank theorem puts every constant-rank map into a normal form, and the implicit function theorem identifies the preimage of a regular value as a submanifold whose tangent space is the kernel of the differential. The spheres, the real projective spaces, and the general linear, orthogonal, unitary and special unitary groups are manifolds by these results, the last three being the classical groups of this Part.

A Riemannian metric is a smooth positive definite inner product on each tangent space, every manifold carries one by a partition-of-unity construction, and it assigns to each piecewise smooth curve a length and to each pair of points the infimum of lengths joining them. That infimum is a metric whose topology is the given one, so the manifold becomes a metric space and the whole of *Metric, Uniform and Complete Spaces* applies. The metric is the structure that anddevelop.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M, N$ | Smooth manifolds; $n = \dim M$ |
| $(U, \varphi)$, $x^i$ | Chart and its coordinate functions |
| $\psi \circ \varphi^{-1}$ | Transition map of two charts; smooth for compatible charts |
| $C^\infty(M)$ | Smooth real-valued functions on $M$ |
| $\operatorname{Diff}(M)$ | Group of diffeomorphisms of $M$ onto itself |
| $T_pM$, $TM$, $T^*M$ | Tangent space at $p$, tangent bundle, cotangent bundle |
| $\partial_{x^i}\big|_p$ | Coordinate basis vector of $T_pM$ |
| $dF_p : T_pM \to T_{F(p)}N$ | Differential (tangent map, pushforward) of a smooth map |
| $\mathfrak{X}(M)$ | Lie algebra of smooth vector fields on $M$ |
| $[X, Y](f) = X(Y(f)) - Y(X(f))$ | Lie bracket of vector fields; $[X,Y] = -[Y,X]$, Jacobi identity |
| $X(f) = df(X)$ | Action of a vector field on a function; the directional derivative |
| Regular submanifold | Locally a coordinate subspace; preimage of a regular value |
| $S^{n-1} = \{x : \langle x,x\rangle = 1\}$ | Unit sphere, a manifold of dimension $n-1$ |
| $\mathbb{RP}^n = S^n/\{\pm 1\}$ | Real projective space, a compact manifold of dimension $n$ |
| $GL_n(\mathbb{R})$, $SL_n(\mathbb{R})$ | General and special linear groups, open submanifolds of $M_n(\mathbb{R})$ |
| $O(n)$, $SO(n)$, $U(n)$, $SU(n)$ | Orthogonal, special orthogonal, unitary and special unitary groups; $\dim O(n) = n(n-1)/2$, $\dim U(n) = n^2$ |
| $g$, $g_{ij}$ | Riemannian metric and its coefficients in a chart |
| $|\gamma'(t)|_g$, $L_g(\gamma)$ | Speed and length of a curve |
| $d_g(p,q) = \inf_\gamma L_g(\gamma)$ | Riemannian distance; its metric topology is the topology of $M$ |
| $\operatorname{rank} dF_p$ | Rank of a smooth map at a point; immersion, submersion, embedding |
| Partition of unity $\{\rho_\alpha\}$ | Smooth functions with locally finite supports summing to $1$ |



## Further Reading

- John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed. (Springer, 2013), for charts, tangent spaces, vector fields, submanifolds and partitions of unity in full.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry, Volume I* (Publish or Perish, 3rd ed. 1999), for the classical treatment of manifolds and the tangent bundle.
- William M. Boothby, *An Introduction to Differentiable Manifolds and Riemannian Geometry* (Academic Press, 2nd ed. 1986), for a compact development from manifolds to curvature.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for the manifold and Lie-group material treated together.
- John W. Milnor, *Topology from the Differentiable Viewpoint* (University Press of Virginia, 1965), for the regular-value arguments and their topological consequences.
- Serge Lang, *Fundamentals of Differential Geometry* (Springer, 1999), for manifolds and bundles in the modern formulation.
- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the manifold theory with a view to the indefinite metrics of this Part.
