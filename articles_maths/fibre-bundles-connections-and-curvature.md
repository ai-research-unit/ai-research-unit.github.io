
# __Fibre Bundles, Connections and Curvature__

## Introduction

A fibre bundle is a manifold that is locally a product, and a connection is a rule that differentiates sections of a bundle by identifying nearby fibres. The two notions, together with the curvature that measures the failure of the identifications to be consistent, form the differential-topological core of the theory of bundles. The companion article *Differential Forms and Stokes' Theorem* supplies the calculus: a connection on a vector bundle is a matrix of $1$-forms, its curvature is a matrix of $2$-forms, and the identities they satisfy — the structure equation and the Bianchi identity — are statements in the graded algebra of forms. The invariant polynomials in the curvature are closed forms whose de Rham classes do not depend on the connection, and this produces the characteristic classes of the bundle.

This article develops the theory from the definitions. It defines fibre bundles, vector bundles and principal bundles, with the transition functions and their cocycle condition; the vector bundles are developed in their own right — the tangent bundle of a manifold, the operations on bundles (direct sums, tensor products, exterior powers, the dual and the pullback), the metrics, the frame bundles, and the module of sections with the local frames that trivialise a bundle over a chart; it defines the covariant derivative on a vector bundle and the connection form on a principal bundle, with the gauge transformation rule and an existence proof by partition of unity; it defines the curvature by the structure equation, proves the Bianchi identity, and characterises flatness; and it states the Chern–Weil construction of characteristic classes, with the first Chern class, the Pontryagin classes and the Euler class as examples. The treatment is differential-topological throughout.

Manifolds are smooth and second countable; bundles are smooth; the structure group is a Lie group $G$ in the sense of *Lie Groups*, with Lie algebra $\mathfrak{g}$, and the associated bundle construction uses the left action of $G$ on a fibre. Exterior forms and the de Rham cohomology are those of *Differential Forms and Stokes' Theorem*, so $d$ is the exterior derivative, $\Omega^k(M)$ is the space of $k$-forms, and $H^k_{dR}(M)$ is the de Rham cohomology. Lie algebras are written in lowercase fraktur, and the adjoint representation of a Lie group on its Lie algebra is $\operatorname{Ad}$, with the conventions of *The Lie Correspondence and the Adjoint Representation*. No physics is invoked.

## Fibre Bundles

### Definitions

**Definition.** A **fibre bundle** with **total space** $E$, **base** $B$ and **fibre** $F$ is a smooth map $\pi : E \to B$ together with a cover $\{U_\alpha\}$ of $B$ by open sets and diffeomorphisms

$$
\phi_\alpha : \pi^{-1}(U_\alpha) \longrightarrow U_\alpha \times F
$$

such that $\pi = \mathrm{pr}_1 \circ \phi_\alpha$ on $\pi^{-1}(U_\alpha)$ and the maps $\phi_\alpha \circ \phi_\beta^{-1}$ are of the form $(x, v) \mapsto (x, g_{\alpha\beta}(x)v)$ for smooth maps $g_{\alpha\beta} : U_\alpha \cap U_\beta \to \operatorname{Diff}(F)$. The data $\{(U_\alpha, \phi_\alpha)\}$ are a **bundle atlas**, the maps $g_{\alpha\beta}$ are the **transition functions**, and the bundle is **trivial** if it admits an atlas with one chart, $E \cong B \times F$.

**Definition.** A **structure group** of the bundle is a Lie group $G$ acting on $F$ such that all transition functions take values in $G$; a bundle with structure group $G$ is a **$G$-bundle**. The condition that the transition functions lie in a fixed $G$ is an additional datum; the transition functions of a bundle always lie in the diffeomorphism group of the fibre.

**Proposition (cocycle condition).** The transition functions of a bundle atlas satisfy

$$
g_{\alpha\alpha} = \mathrm{id}, \qquad g_{\alpha\beta}(x)\, g_{\beta\gamma}(x) = g_{\alpha\gamma}(x)
$$

on the triple intersections; conversely, given an open cover and functions satisfying these identities, there is a bundle with those transition functions, unique up to isomorphism.

**Proof.** Comparing the three trivialisations over a triple intersection gives the relation; conversely, the disjoint union $\bigsqcup_\alpha U_\alpha \times F$ modulo the equivalence $(x, v)_\beta \sim (x, g_{\alpha\beta}(x)v)_\alpha$ on overlaps is a manifold and a bundle with the required transition functions. $\square$

### Vector Bundles and Principal Bundles

**Definition.** A **vector bundle** of rank $k$ is a fibre bundle with fibre $\mathbb{R}^k$ and structure group $GL_k(\mathbb{R})$, with transition functions acting linearly on the fibre; over $\mathbb{C}$ the fibre is $\mathbb{C}^k$ and the structure group $GL_k(\mathbb{C})$. A **section** of a bundle $\pi : E \to B$ is a smooth map $s : B \to E$ with $\pi \circ s = \mathrm{id}_B$; the space of sections of a vector bundle $E$ is written $\Gamma(E)$.

**Definition.** A **principal $G$-bundle** is a fibre bundle $\pi : P \to B$ with a free and transitive right action of $G$ on each fibre, such that the action is smooth and $B = P/G$. Its transition functions are elements of $G$, and a **section** of a principal bundle over an open set is a local trivialisation.

**Definition.** Let $P \to B$ be a principal $G$-bundle and let $F$ be a manifold with a left $G$-action. The **associated bundle** is

$$
P \times_G F = (P \times F)/G, \qquad (p \cdot g, v) \sim (p, g \cdot v),
$$

a fibre bundle over $B$ with fibre $F$. Every vector bundle of rank $k$ with structure group $G \subseteq GL_k$ is associated to a principal $G$-bundle, the **frame bundle** of the vector bundle.

**Example.** The **tangent bundle** $TM \to M$ is a vector bundle of rank $n = \dim M$, with fibre the tangent space and structure group $GL_n(\mathbb{R})$; its principal frame bundle $GL(M)$ has fibre $GL_n(\mathbb{R})$, and a point of $GL(M)$ over $x$ is a linear frame in $T_xM$. The **cotangent bundle** $T^*M$ is the dual vector bundle, and $\Lambda^kT^*M$ is the bundle of forms of *Differential Forms and Stokes' Theorem*. For a Riemannian manifold the **orthonormal frame bundle** is a principal $O(n)$-bundle associated to $TM$.

### Cocycles and Classification

**Definition.** Two cocycles $\{g_{\alpha\beta}\}$ and $\{g'_{\alpha\beta}\}$ on the same cover define isomorphic bundles if there are maps $h_\alpha : U_\alpha \to G$ with

$$
g'_{\alpha\beta} = h_\alpha^{-1}\, g_{\alpha\beta}\, h_\beta
$$

on each intersection. Such a family $\{h_\alpha\}$ is a **cochain** trivialising the difference of the cocycles.

**Remark.** The classification of principal $G$-bundles up to isomorphism is by the first Čech cohomology $\check H^1(B; \underline{G})$ with coefficients in the sheaf of smooth $G$-valued functions; for $G$ discrete this is a topological invariant, and for $G$ connected it is often computable by the homotopy classification of maps $B \to BG$, where $BG$ is the classifying space. Only the differentiable content of the cocycle is used below.

## Connections on Vector Bundles

### The Covariant Derivative

**Definition.** Let $E \to M$ be a vector bundle over a manifold $M$ with $\dim M = n$. A **connection** on $E$ is an $\mathbb{R}$-linear map

$$
\nabla : \Gamma(E) \longrightarrow \Gamma(T^*M \otimes E)
$$

satisfying the Leibniz rule

$$
\nabla(f s) = df \otimes s + f\, \nabla s
$$

for all $f \in C^\infty(M)$ and $s \in \Gamma(E)$. The operator $\nabla_X s = \langle\nabla s, X\rangle$ for $X \in \mathfrak{X}(M)$ is the **covariant derivative** along $X$, and it is $C^\infty(M)$-linear in $X$ and a derivation in $s$.

**Proposition.** A connection exists on every vector bundle, and the set of connections on $E$ is an affine space modelled on $\Omega^1(M; \operatorname{End}(E)) = \Gamma(T^*M\otimes\operatorname{End}E)$: if $\nabla$ and $\nabla'$ are connections then $\nabla' - \nabla$ is a $1$-form with values in the endomorphisms of $E$.

**Proof.** On a trivial bundle $U \times \mathbb{R}^k$ the exterior derivative $d$ on the components is a connection; on a general bundle choose a locally finite cover by trivialising charts, a partition of unity, and convex-combine the local connections with the partition of unity to obtain a global connection. The difference of two connections is $C^\infty(M)$-linear in $s$ by the Leibniz rule, hence a tensor, which is a section of $T^*M\otimes\operatorname{End}E$. $\square$

**Definition.** Let $e = (e_1, \ldots, e_k)$ be a **local frame** of $E$ over an open set $U$, so that every section over $U$ is $s = \sum_i s^i e_i$ with $s^i \in C^\infty(U)$. The **connection form** of $\nabla$ in this frame is the matrix of $1$-forms $\omega = (\omega^i_{\ j})$ defined by

$$
\nabla e_j = \sum_i \omega^i_{\ j} \otimes e_i,
$$

so that $\nabla s = \sum_i \bigl(ds^i + \sum_j \omega^i_{\ j}s^j\bigr)\otimes e_i$, and $\nabla = d + \omega$ in matrix notation.

**Proposition (change of frame).** Let $e' = e\,g$ be another frame, with $g : U \to GL_k(\mathbb{R})$ a smooth map. Then the connection forms are related by

$$
\omega' = g^{-1}\omega\, g + g^{-1} dg.
$$

**Proof.** Write $e'_j = \sum_a e_a g^a_{\ j}$ and compute $\nabla e'_j$ in both frames; the Leibniz rule produces the term $dg$ alongside the transformation of $\omega$ by $g$. $\square$

**Theorem.** The connection forms $\omega_\alpha$ of a connection on the trivialisations $U_\alpha$ satisfy $\omega_\beta = g_{\alpha\beta}^{-1}\omega_\alpha g_{\alpha\beta} + g_{\alpha\beta}^{-1}dg_{\alpha\beta}$ on overlaps; conversely, such a family defines a connection.

### Connections on Principal Bundles

**Definition.** Let $\pi : P \to M$ be a principal $G$-bundle with Lie algebra $\mathfrak{g}$. For $A \in \mathfrak{g}$ let $A^{\#}$ be the **fundamental vector field** on $P$ generated by the right action of $G$. A **connection form** on $P$ is a $\mathfrak{g}$-valued $1$-form $\omega \in \Omega^1(P; \mathfrak{g})$ such that

$$
\omega(A^{\#}) = A \ \text{ for all } A \in \mathfrak{g}, \qquad R_g^*\omega = \operatorname{Ad}(g^{-1})\,\omega \ \text{ for all } g \in G.
$$

The **horizontal subspace** at $p \in P$ is $H_pP = \ker\omega_p \subseteq T_pP$, and it is complementary to the vertical subspace $T_p(P_{\pi(p)})$.

**Proposition.** A connection form exists on every principal bundle, and the horizontal distribution $H = \ker\omega$ is a $G$-invariant distribution complementary to the vertical distribution; a distribution with these properties determines a unique connection form.

**Proof.** Existence: on a local trivialisation $U \times G$ define $\omega = \mathrm{pr}_2^*\theta$, where $\theta$ is the Maurer–Cartan form of $G$; patch the local forms with a partition of unity and correct by the $\operatorname{Ad}$-equivariance to obtain a global form satisfying both conditions. The equivalence with a $G$-invariant complement is the definition of the kernel and the existence of the fundamental vector fields. $\square$

**Definition.** Let $s : U \to P$ be a local section, so that $U \times G \to \pi^{-1}(U)$, $(x, g) \mapsto s(x)\cdot g$, is a trivialisation. The **local connection form** is $\omega_s = s^*\omega \in \Omega^1(U; \mathfrak{g})$, and for $s' = s \cdot h$ with $h : U \to G$,

$$
\omega_{s'} = h^{-1}\omega_s h + h^{-1}dh.
$$

**Remark.** This is the transformation rule of the vector bundle connection form, and the coincidence is not accidental: a connection on a vector bundle with structure group $G$ is the same thing as a connection on its frame bundle, read in a frame. The **gauge group** of the bundle is the group of bundle automorphisms covering the identity, and the transformation above is its action on connections; the affine space of connections is acted on freely, with the local form of the action displayed.

## Curvature

### The Structure Equation

**Definition.** Let $\omega$ be a connection form on a principal $G$-bundle $P \to M$. The **curvature** is

$$
\Omega = d\omega + \tfrac{1}{2}[\omega, \omega] \in \Omega^2(P; \mathfrak{g}),
$$

where $[\omega,\omega]$ combines the wedge product of forms with the bracket in $\mathfrak{g}$; since $\omega$ has degree one, $\tfrac12[\omega,\omega] = \omega\wedge\omega$. The curvature is **horizontal** ($\iota_{A^{\#}}\Omega = 0$ for all $A$) and **equivariant**, $R_g^*\Omega = \operatorname{Ad}(g^{-1})\Omega$, so it descends to a $2$-form on the base with values in the associated bundle $P\times_G\mathfrak{g}$.

**Definition.** For a vector bundle $E$ with connection $\nabla = d+\omega$ in a frame, the **curvature** is the $2$-form

$$
R = d\omega + \omega\wedge\omega \in \Omega^2(M; \operatorname{End}E),
$$

and it satisfies $R(X, Y)s = \nabla_X\nabla_Y s - \nabla_Y\nabla_X s - \nabla_{[X,Y]}s$ for vector fields $X, Y$ and a section $s$.

**Theorem (structure equation).** The curvature of a connection on a vector bundle is the obstruction to the connection being flat and it is tensorial: for a change of frame $g$,

$$
R' = g^{-1} R\, g,
$$

so the curvature is a well-defined section of $\Lambda^2 T^*M \otimes \operatorname{End}E$.

**Proof.** The formula $\nabla^2 s = R\wedge s$ follows from $R = d\omega+\omega\wedge\omega$ and the identity $d^2 = 0$; the transformation rule follows by substituting $\omega' = g^{-1}\omega g + g^{-1}dg$ into the expression for $R'$ and cancelling the terms involving $dg$, using $d(g^{-1}) = -g^{-1}dg\,g^{-1}$. $\square$

### The Bianchi Identity

**Definition.** The **exterior covariant derivative** of a $k$-form $\alpha$ with values in $E$ is $d^\nabla\alpha = d\alpha + \omega\wedge\alpha$, and for an $\operatorname{End}E$-valued form $\beta$ the operator acts as $d^\nabla\beta = d\beta + [\omega, \beta]$ with the graded bracket.

**Theorem (Bianchi identity).** For a connection $\nabla$ with curvature $R$,

$$
d^\nabla R = 0, \qquad \text{that is} \quad dR + [\omega, R] = 0.
$$

For a principal bundle, the same identity reads $d\Omega + [\omega, \Omega] = 0$.

**Proof.** Apply $d$ to $R = d\omega + \omega\wedge\omega$ and use $d^2 = 0$ and the graded Leibniz rule:

$$
dR = d(\omega\wedge\omega) = d\omega\wedge\omega - \omega\wedge d\omega.
$$

On the other hand $[\omega, R] = \omega\wedge R - R\wedge\omega$ (the sign $(-1)^{1\cdot2} = +1$ for a $1$-form and a $2$-form), and substituting $R = d\omega+\omega\wedge\omega$ gives $[\omega,R] = \omega\wedge d\omega - d\omega\wedge\omega + [\omega, \omega\wedge\omega]$. The last term vanishes by the graded Jacobi identity, so $[\omega,R] = \omega\wedge d\omega - d\omega\wedge\omega$, which is $-dR$. $\square$

**Corollary.** The curvature is a closed form when the connection is abelian, and in general the Bianchi identity says that $R$ is closed for the exterior covariant derivative $d^\nabla$.

### Flatness

**Definition.** A connection is **flat** if its curvature vanishes, $R = 0$.

**Theorem.** A connection on a vector bundle is flat if and only if it is locally trivial: about every point there is a frame in which $\omega = 0$, equivalently a family of local sections with $\nabla s = 0$ spanning the bundle. For a principal bundle the corresponding statement is that $\omega = g^{-1}dg$ locally.

**Proof.** If $\omega = 0$ in a frame then $R = d\omega+\omega\wedge\omega = 0$. Conversely, if $R = 0$ then the equation $\nabla s = 0$ is a system of linear first-order partial differential equations with zero curvature, so it is locally solvable by the Frobenius theorem, and the solution space has dimension equal to the rank; this produces the flat frame. $\square$

**Remark.** The distribution $H = \ker\omega$ on a principal bundle is integrable exactly when $\Omega = 0$, by the Frobenius theorem applied to the horizontal distribution, and the leaves are then the local trivialisations. In this sense the curvature is the obstruction to the connection being given by a foliation, and the integral of the curvature over a small loop is the infinitesimal holonomy of the connection.

## Characteristic Classes

### The Chern–Weil Homomorphism

**Definition.** Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$, and let $S^\bullet(\mathfrak{g}^*)^G$ be the algebra of $G$-invariant symmetric multilinear forms on $\mathfrak{g}$, the **invariant polynomials**. For $f \in S^k(\mathfrak{g}^*)^G$ and a connection on a principal $G$-bundle $P \to M$ with curvature $\Omega$, the **Chern–Weil form** is

$$
f(\Omega) = f(\Omega, \ldots, \Omega) \in \Omega^{2k}(P),
$$

the $k$-fold substitution of the curvature.

**Theorem (Chern–Weil).** For every invariant polynomial $f \in S^k(\mathfrak{g}^*)^G$, the form $f(\Omega)$ is closed and basic for the $G$-action (horizontal and invariant), hence descends to a closed $2k$-form $f(\Omega)$ on $M$; its de Rham class $[f(\Omega)] \in H^{2k}_{dR}(M)$ is independent of the choice of connection on $P$.

**Proof sketch.** Closedness is a consequence of the Bianchi identity: $d f(\Omega) = k\,f(d^\nabla\Omega, \Omega, \ldots, \Omega) = 0$. Basicness follows from the horizontality and equivariance of $\Omega$. Independence of the connection is proved by the transgression formula: if $\Omega_0, \Omega_1$ are the curvatures of two connections, then $f(\Omega_1) - f(\Omega_0) = d\,\tau$ for an explicit $(2k-1)$-form $\tau$ built from a linear path of connections and the identity $f$ is invariant. $\square$

**Definition.** The **Chern–Weil homomorphism** is the algebra map

$$
S^\bullet(\mathfrak{g}^*)^G \longrightarrow H^{\mathrm{ev}}_{dR}(M), \qquad f \longmapsto [f(\Omega)],
$$

taking values in the even cohomology and independent of the connection. Its image consists of **characteristic classes** of the bundle.

### Chern, Pontryagin and Euler Classes

**Example (first Chern class).** Let $L \to M$ be a complex line bundle with a connection of curvature $\mathcal{F} \in \Omega^2(M; \mathbb{C})$, a $2$-form because $\operatorname{End}(L) \cong \mathbb{C}$. The invariant polynomial $f(\xi) = \frac{i}{2\pi}\xi$ on $\mathfrak{gl}(1, \mathbb{C}) = \mathbb{C}$ gives the closed $2$-form

$$
c_1(L) = \left[\frac{i}{2\pi} \mathcal{F}\right] \in H^2_{dR}(M; \mathbb{C}),
$$

the **first Chern class** of $L$, independent of the connection. For a connection compatible with a Hermitian structure on $L$ the curvature is $\mathfrak{u}(1)$-valued and the form is real, and the class is then the image in real cohomology of an integral class in $H^2(M; \mathbb{Z})$.

**Example (Pontryagin classes).** Let $E \to M$ be a real vector bundle of rank $k$ with a connection of curvature $R$, an $\operatorname{End}E$-valued $2$-form. The invariant polynomials

$$
p_j(E) = \left[(-1)^j \operatorname{tr}\!\left(\frac{R}{2\pi}\wedge\cdots\wedge\frac{R}{2\pi}\right)\right] \in H^{4j}_{dR}(M)
$$

are the **Pontryagin classes** of $E$, the trace being taken in $\operatorname{End}E$ and the wedge product repeated $2j$ times. They vanish in odd degree, and for a complex bundle the Chern classes $c_j(E)$ are the invariant polynomials obtained from $\det(I + \frac{i}{2\pi}R)$.

**Example (Euler class).** For a real oriented vector bundle of rank $2j$ the Pfaffian of the curvature is an invariant polynomial, and its Chern–Weil form is normalised as $\operatorname{Pf}(R/2\pi)$; its class is the **Euler class** $e(E) \in H^{2j}_{dR}(M)$, the normalisation by $(2\pi)^{-j}$ being the one that makes the class integral. For the tangent bundle of a compact oriented manifold of dimension $2j$,

$$
\int_M e(TM) = \chi(M),
$$

the **Gauss–Bonnet theorem**, expressing the Euler characteristic as the integral of a curvature form.

**Remark.** The Chern–Weil construction shows that the characteristic classes are differential-geometric invariants of a bundle which are in fact topological: they depend only on the isomorphism class of the bundle, and they can be computed from any connection. If a bundle admits a flat connection then all its Chern–Weil forms vanish, so its real characteristic classes vanish; the corresponding integral classes are then torsion. This is the differential-topological counterpart of the statement that a flat connection with nontrivial holonomy can still have nontrivial topology.

## Examples

### The Tangent Bundle and the Levi-Civita Connection

**Theorem.** Let $(M, g)$ be a Riemannian manifold. Then there is a unique connection $\nabla$ on the tangent bundle $TM$ that is **metric**, $X\langle Y, Z\rangle = \langle\nabla_XY, Z\rangle + \langle Y, \nabla_XZ\rangle$, and **torsion-free**, $\nabla_XY - \nabla_YX = [X, Y]$. It is the **Levi-Civita connection**, and its curvature is the Riemann curvature tensor

$$
R(X, Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z.
$$

**Proof sketch.** The Koszul formula determines $\nabla_XY$ uniquely from $g$ and the bracket; the right-hand side is $C^\infty(M)$-linear in each slot, so it defines a connection, and the two required properties are consequences of the formula. $\square$

**Remark.** In a local frame the connection form of the Levi-Civita connection is the matrix of Christoffel symbols, $\omega^i_{\ j} = \sum_k \Gamma^i_{jk}dx^k$, and the Bianchi identity for its curvature is the differential identity satisfied by the Riemann tensor. The Chern–Weil forms of the Levi-Civita connection give the Pontryagin classes of $TM$ and, in the oriented even-dimensional case, the Euler class of the Gauss–Bonnet theorem.

### Line Bundles and Holonomy

**Example.** For a complex line bundle $L \to M$, the curvature of any connection is a closed $2$-form by the Bianchi identity (the connection being abelian), and its class is $2\pi/i$ times the first Chern class; the integral of $\frac{i}{2\pi}\mathcal{F}$ over a closed surface equals the degree of the restriction of $L$ to that surface, an integer.

**Remark (holonomy).** Parallel transport along paths with the connection defines, for each loop based at $x$, an element of the structure group; these elements form the **holonomy group** of the connection at $x$, a Lie subgroup of $G$. The Ambrose–Singer theorem identifies its Lie algebra with the span of the curvature endomorphisms $R(u, v)$ at $x$, so the curvature generates the holonomy and, in particular, a connection is flat exactly when its holonomy is discrete.

## Summary

A fibre bundle is a manifold locally isomorphic to a product $U \times F$, with transition functions satisfying the cocycle condition; a vector bundle is a bundle with linear fibres and structure group $GL_k$, a principal $G$-bundle is a bundle with a free transitive $G$-action on the fibres, and the associated bundle construction produces vector bundles from principal ones and their representations. Sections of a vector bundle form a module over the smooth functions, and a bundle is described by a local frame together with the transition data.

A connection on a vector bundle is a covariant derivative $\nabla$ satisfying the Leibniz rule; locally it is a matrix of $1$-forms $\omega$, transforming as $\omega' = g^{-1}\omega g + g^{-1}dg$ under a change of frame, and connections exist by a partition-of-unity argument. On a principal bundle a connection is a $\mathfrak{g}$-valued $1$-form with $\omega(A^\#) = A$ and $R_g^*\omega = \operatorname{Ad}(g^{-1})\omega$, equivalently a $G$-invariant horizontal distribution. The curvature is $R = d\omega + \omega\wedge\omega$, a tensorial $2$-form transforming as $R' = g^{-1}Rg$, and it satisfies the Bianchi identity $d^\nabla R = 0$; the connection is flat exactly when the horizontal distribution is integrable, equivalently when the curvature vanishes.

Invariant polynomials in the curvature are closed basic forms whose de Rham classes are independent of the connection, giving the Chern–Weil homomorphism and the characteristic classes: the first Chern class of a complex line bundle, the Pontryagin classes of a real bundle, and the Euler class, whose integral over a compact oriented even-dimensional manifold is the Euler characteristic by Gauss–Bonnet. On a Riemannian manifold the unique metric and torsion-free connection is the Levi-Civita connection, and its curvature is the Riemann tensor; the holonomy group of a connection is generated by its curvature, so flatness is exactly the discreteness of the holonomy.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi : E \to B$, fibre $F$ | Fibre bundle; locally $E \cong U \times F$ |
| $g_{\alpha\beta}$ | Transition functions; $g_{\alpha\beta}g_{\beta\gamma} = g_{\alpha\gamma}$ |
| $G$-bundle, principal $G$-bundle $P \to M$ | Structure group $G$; free transitive right $G$-action on fibres |
| $P\times_G F$ | Associated bundle; vector bundles arise from frame bundles |
| $\Gamma(E)$ | Space of smooth sections of $E$ |
| $\operatorname{Diff}(F)$ | Diffeomorphism group of the fibre; the codomain of the transition functions |
| $\nabla : \Gamma(E) \to \Gamma(T^*M\otimes E)$ | Connection; $\nabla(fs) = df\otimes s + f\nabla s$ |
| $\omega = (\omega^i_{\ j})$, $\nabla = d+\omega$ | Connection form in a frame |
| $\omega' = g^{-1}\omega g + g^{-1}dg$ | Change of frame; gauge transformation rule |
| $\omega \in \Omega^1(P;\mathfrak{g})$, $\omega(A^\#) = A$, $R_g^*\omega = \operatorname{Ad}(g^{-1})\omega$ | Connection form on a principal bundle |
| $H_pP = \ker\omega_p$ | Horizontal subspace; $G$-invariant complement to the vertical |
| $R = d\omega + \omega\wedge\omega$ | Curvature of a vector bundle connection |
| $\Omega = d\omega + \frac12[\omega,\omega]$ | Curvature of a principal connection |
| $\operatorname{End}(E)$, $\Omega^k(M;\operatorname{End}E)$ | Bundle of endomorphisms and its form-valued sections; $R$ is an $\operatorname{End}E$-valued $2$-form |
| $R(X,Y)s = \nabla_X\nabla_Ys - \nabla_Y\nabla_Xs - \nabla_{[X,Y]}s$ | Curvature as a commutator of covariant derivatives |
| $R' = g^{-1}Rg$ | Tensorial transformation of the curvature |
| $d^\nabla R = 0$, $dR + [\omega,R] = 0$ | Bianchi identity |
| Flat | $R = 0$; locally $\omega = 0$ (vector bundle) or $\omega = g^{-1}dg$ (principal bundle) |
| $f(\Omega)$, $S^\bullet(\mathfrak{g}^*)^G \to H^{\mathrm{ev}}_{dR}(M)$ | Chern–Weil form and homomorphism |
| $c_1(L) = [\frac{i}{2\pi}\mathcal{F}]$, $p_j(E)$, $e(E)$ | First Chern, Pontryagin, and Euler classes |
| $\operatorname{Pf}(R/2\pi)$ | Pfaffian form of a real oriented bundle of rank $2j$; its class is the Euler class |
| $\int_M e(TM) = \chi(M)$ | Gauss–Bonnet |
| $\nabla$ Levi-Civita, $R(X,Y)Z$ | Metric and torsion-free connection; Riemann curvature tensor |
| Holonomy group | Parallel transport around loops; its Lie algebra is spanned by the curvature |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volumes I and II* (Interscience, 1963, 1969), for fibre bundles, connections, and curvature in full.
- John M. Lee, *Introduction to Riemannian Manifolds* (Springer, 2nd ed. 2018), for the Levi-Civita connection, the Riemann tensor, and holonomy.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry, Volume II* (Publish or Perish, 3rd ed. 1999), for connections, curvature, and the structure equations.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the Chern–Weil homomorphism and characteristic classes.
- Shiing-Shen Chern, *Complex Manifolds Without Potential Theory* (Springer, 2nd ed. 1979), for connections on complex bundles and the Chern classes.
- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for characteristic classes and the Chern–Weil construction over smooth manifolds.
- Dominic Joyce, *Riemannian Holonomy Groups and Calibrated Geometry* (Oxford University Press, 2007), for holonomy groups and the Ambrose–Singer theorem.
