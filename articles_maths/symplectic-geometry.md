
# __Symplectic Geometry__

## Introduction

A **symplectic manifold** is a smooth manifold carrying a closed and nondegenerate $2$-form. The two conditions fight in a productive way: nondegeneracy alone is a fibrewise, linear condition that makes the form an isomorphism $TM\to T^*M$, while closedness binds the forms at nearby points together and is the exact obstruction to the manifold having any local invariants. The result is a geometry with no local curvature, in which the only invariants are global and topological in character.

This article develops the geometry of a symplectic manifold. It defines symplectic manifolds and the elementary consequences of the definition — even dimension, an orientation, a canonical volume form; it treats the standard examples, the cotangent bundle in particular; it proves the Darboux theorem by the Moser argument and draws the consequence that distinguishes symplectic geometry from Riemannian geometry; it develops Hamiltonian vector fields, the Poisson bracket of functions and the algebra of symplectomorphisms; and it treats Lagrangian submanifolds, the almost complex structures compatible with a symplectic form, and symplectic reduction. The manifold theory is not covered here; the linear algebra on which it rests is not repeated here.

The **boundary of the article** is worth stating at the outset. The linear-algebraic theory of an alternating form — nondegeneracy, the symplectic basis, the Darboux normal form for a vector space, the symplectic group, isotropic and Lagrangian subspaces, the Pfaffian, and the Poisson bracket on the polynomials of a symplectic vector space — is the subject of the companion article *Symplectic Forms and Poisson Brackets*, and is assumed throughout. What is added here is the passage from one vector space to a manifold: the form varies from point to point, and the new condition is $d\omega = 0$. The Poisson *algebra* of an abstract commutative algebra is treated in Part I, and the Poisson *manifold*, where the bracket is defined by a tensor on a manifold, is. The Hamiltonian systems and the differential equations that a Hamiltonian flow satisfies belong to Part III, where the limit and the derivative of a curve are available; this article uses a flow only as a one-parameter family of symplectomorphisms and states the differential equation in passing.

Manifolds, charts, smooth maps and their differentials are those of the companion article *Smooth Manifolds and Differential Geometry*, and transversality and the implicit-function theorem those of *Differential Topology*; both are being written in parallel in this Part and are cited rather than restated. Differential forms, the exterior derivative $d$, the de Rham complex $H^\bullet_{dR}(M)$ and the integral of a top form are those of *Differential Forms and Stokes' Theorem*. Vector fields, the Lie bracket of vector fields, bundles and the tangent and cotangent bundles are those of *Fibre Bundles, Connections and Curvature* and of the articles cited there. Lie groups and their Lie algebras are those of *Lie Groups*, *The Lie Algebra and the Exponential Map* and *The Lie Correspondence and the Adjoint Representation*. The base field is $\mathbb{R}$ and no physics is invoked.

## Symplectic Manifolds

**Definition.** A **symplectic form** on a smooth manifold $M$ is a $2$-form $\omega \in \Omega^2(M)$ that is

**(a)** **closed**, $d\omega = 0$; and

**(b)** **nondegenerate**, meaning that for every $x \in M$ the bilinear form $\omega_x$ on $T_xM$ is nondegenerate.

A **symplectic manifold** is a pair $(M, \omega)$ consisting of a smooth manifold and a symplectic form on it; a **symplectomorphism** between symplectic manifolds $(M, \omega)$ and $(N, \sigma)$ is a diffeomorphism $F : M \to N$ with $F^*\sigma = \omega$.

Nondegeneracy is exactly the condition that the bundle map

$$
\omega^{\flat} : TM \longrightarrow T^*M, \qquad X \longmapsto \omega(X, \cdot)
$$

is an isomorphism of vector bundles. Its inverse is written $\omega^{\sharp} : T^*M \to TM$, and it is what turns a $1$-form into a vector field; the Hamiltonian vector fields below are its most important application. When the form is understood, the inverse is also written by raising indices, $\omega^{\sharp}(\alpha) = \alpha^{\sharp}$.

**Proposition.** Let $\omega$ be a nondegenerate $2$-form on an $n$-manifold $M$. Then $n = 2m$ is even; the top form

$$
\mathrm{vol}_\omega = \frac{\omega^{\wedge m}}{m!}
$$

is nowhere vanishing, so $\omega$ orients $M$ and defines a volume form; and $\omega$ is nondegenerate if and only if $\omega^{\wedge m}$ is nowhere vanishing.

**Proof.** At a point $x$, the form $\omega_x$ is a nondegenerate alternating form on the vector space $T_xM$; by the symplectic-basis theorem of *Symplectic Forms and Poisson Brackets*, such a form exists only in even dimension, and in a symplectic basis it has the standard matrix. In coordinates adapted to a symplectic basis, $\omega^{\wedge m}$ is $m!$ times the coordinate volume form, which is the statement $\mathrm{vol}_\omega \neq 0$; conversely, if $\omega^{\wedge m} \neq 0$ then $\omega_x$ has maximal rank, hence is nondegenerate. The orientation is the one defined by the nowhere vanishing top form $\mathrm{vol}_\omega$. $\square$

**Remark.** The factor $m!$ is not a normalisation of convenience. If $\omega = \sum_i dx_i \wedge dy_i$, then $\omega^{\wedge m}$ is $m!$ times $dx_1\wedge dy_1\wedge\cdots\wedge dx_m\wedge dy_m$, so $\omega^{\wedge m}/m!$ is the standard volume. The form $\mathrm{vol}_\omega$ is the **symplectic volume form** of the structure, and every symplectomorphism preserves it; a symplectomorphism therefore preserves the volume, and the symplectic condition is strictly stronger than the volume condition; the rigidity that this extra strength produces — Gromov's non-squeezing theorem being the first example — is a global phenomenon and belongs.

**Example.** On $\mathbb{R}^{2m}$ with coordinates $x_1, \ldots, x_m, y_1, \ldots, y_m$ the form

$$
\omega_0 = \sum_{i=1}^{m} dx_i \wedge dy_i
$$

is closed, because its coefficients are constant, and nondegenerate, because its matrix in the coordinate basis is the invertible block matrix $\begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}$. Every open subset of $\mathbb{R}^{2m}$ is symplectic with the restricted form, and the linear algebra of $\omega_0$ is that of *Symplectic Forms and Poisson Brackets*.

**Example.** Let $Q$ be a smooth manifold and let $\pi : T^*Q \to Q$ be its cotangent bundle with the projection $\pi$. The **tautological $1$-form** $\theta \in \Omega^1(T^*Q)$ is defined at a covector $p \in T^*_qQ$ and a tangent vector $v \in T_p(T^*Q)$ by

$$
\theta_p(v) = p\,(d\pi_p\, v),
$$

so that $\theta_p$ evaluates the covector on the projection of the tangent vector. In a chart with coordinates $(q^1, \ldots, q^m)$ on $Q$ and fibre coordinates $(p_1, \ldots, p_m)$, it reads $\theta = \sum_i p_i\, dq^i$. The form

$$
\omega = -\,d\theta = \sum_{i=1}^{m} dq^i \wedge dp_i
$$

is closed because it is exact, and nondegenerate because in the coordinates $(q, p)$ it has the standard shape; so $(T^*Q, -d\theta)$ is a symplectic manifold, the **cotangent bundle** of $Q$. It is the source of the examples in mechanics and of the local model for a Lagrangian neighbourhood below.

**Example.** An oriented surface $\Sigma$ with an area form $\omega$ is symplectic: a $2$-form on a surface is automatically closed, and nondegeneracy is exactly the nowhere-vanishing condition. The symplectomorphisms are the area-preserving diffeomorphisms, and the symplectic volume is the area. In dimension two, symplectic geometry is thus the geometry of area, and the Darboux theorem says that any two area forms are locally the same; the global invariants are the total area and, more subtly, the isotopy class of the area form.

**Example.** The coadjoint orbit of a Lie group $G$ through a point $\xi \in \mathfrak{g}^*$ carries the **Kirillov–Kostant–Souriau form**, defined by

$$
\omega_\xi(X^\#, Y^\#) = \langle \xi, [X, Y]\rangle, \qquad X, Y \in \mathfrak{g},
$$

where $X^\#$ is the fundamental vector field of the coadjoint action generated by $X$. The form is well defined and nondegenerate, and it is closed; so every coadjoint orbit is a symplectic manifold. This construction, whose group-theoretic input is that of *Lie Groups*, produces a large supply of examples, and in the case of a compact Lie group it exhausts the homogeneous symplectic manifolds.

## The Darboux Theorem

The central local fact of symplectic geometry is that a symplectic form has no local invariants at all.

**Theorem (Darboux).** Let $(M, \omega)$ be a symplectic manifold of dimension $2m$. About every point $x \in M$ there is a chart $(U, x_1, \ldots, x_m, y_1, \ldots, y_m)$ centred at $x$ in which

$$
\omega = \sum_{i=1}^{m} dx_i \wedge dy_i .
$$

Consequently every symplectic manifold of dimension $2m$ is locally symplectomorphic to $(\mathbb{R}^{2m}, \omega_0)$.

**Proof.** By the linear Darboux theorem of *Symplectic Forms and Poisson Brackets* there is a basis of $T_xM$ in which $\omega_x$ is the standard form; choosing a chart in which this basis is the coordinate basis, the form $\omega_0$ with constant coefficients $\sum_i dx_i\wedge dy_i$ agrees with $\omega$ at $x$. It therefore suffices to prove that on a neighbourhood of the origin in $\mathbb{R}^{2m}$ any closed form $\omega_1$ with $\omega_1(0) = \omega_0$ is symplectomorphic to $\omega_0$ by a diffeomorphism fixing the origin. Consider the homotopy $\omega_t = \omega_0 + t(\omega_1 - \omega_0)$ from $\omega_0$ to $\omega_1$; each $\omega_t$ is closed, and each is nondegenerate near the origin because nondegeneracy is an open condition and $\omega_t(0) = \omega_0$ for every $t$. Since $\omega_1 - \omega_0$ is closed and vanishes at the origin, the Poincaré lemma of *Differential Forms and Stokes' Theorem* applied on a star-shaped chart provides a $1$-form $\sigma$ with $d\sigma = \omega_1 - \omega_0$. Because $\omega_t$ is nondegenerate, there is a unique time-dependent vector field $X_t$ with

$$
\iota_{X_t}\omega_t = -\sigma .
$$

Let $\varphi_t$ be its flow, defined near the origin for $t \in [0,1]$; then

$$
\frac{d}{dt}\bigl(\varphi_t^*\omega_t\bigr) = \varphi_t^*\Bigl(\mathcal{L}_{X_t}\omega_t + \frac{d\omega_t}{dt}\Bigr) = \varphi_t^*\bigl(d\,\iota_{X_t}\omega_t + (\omega_1-\omega_0)\bigr) = \varphi_t^*(-d\sigma + d\sigma) = 0 .
$$

Hence $\varphi_t^*\omega_t$ is constant in $t$, and evaluating at $t = 0$ gives $\varphi_t^*\omega_t = \omega_0$ for all $t$; at $t = 1$ the map $\varphi_1$ pulls $\omega_1$ back to $\omega_0$, which is the Darboux chart. $\square$

**Remark.** The argument is Moser's, and it uses only the closedness of the forms, the Poincaré lemma and the openness of nondegeneracy; it is the standard proof that a family of cohomologous nondegenerate closed forms is trivialised by an isotopy. The contrast with Riemannian geometry is the point of the theorem. A Riemannian metric has local invariants — the curvature and its covariant derivatives — and no two metrics of different curvature are locally isometric; a symplectic form has none, and two symplectic manifolds of the same dimension are always locally symplectomorphic. The sectional curvature, the Ricci tensor and the Levi-Civita connection of a Riemannian metric are those of the companion article *Riemannian Geometry*, being written in parallel.

**Corollary.** A symplectic invariant of a manifold is never local. Precisely, if $P$ is a function of the values of $\omega$ and finitely many of its derivatives at a single point which is unchanged by every symplectomorphism, then $P$ is constant: in Darboux coordinates the form is the constant form $\sum_i dx_i\wedge dy_i$, so the whole jet of $\omega$ at a point is the same for every symplectic manifold of the given dimension. Every invariant of a symplectic manifold is therefore global, and the theory is a branch of topology rather than of local differential geometry.

## Hamiltonian Vector Fields

**Definition.** Let $(M, \omega)$ be a symplectic manifold and let $f \in C^\infty(M)$. The **Hamiltonian vector field** of $f$ is the unique vector field $X_f \in \mathfrak{X}(M)$ with

$$
\iota_{X_f}\omega = df, \qquad \text{that is} \quad \omega(X_f, Y) = Y(f) \ \text{ for all } Y \in \mathfrak{X}(M).
$$

Existence and uniqueness are the nondegeneracy of $\omega$, read through the bundle isomorphism $\omega^\flat$: the vector field is $X_f = \omega^{\sharp}(df)$. A vector field $X$ is **symplectic** if $\mathcal{L}_X\omega = 0$, and **Hamiltonian** if it is $X_f$ for some function $f$.

**Definition.** The **Poisson bracket** of $f, g \in C^\infty(M)$ is

$$
\{f, g\} = \omega(X_f, X_g) = X_g(f) = -X_f(g).
$$

The equality of the three expressions is the definition of the Hamiltonian fields read in the two slots: $\omega(X_f, X_g) = df(X_g) = X_g(f)$, and the antisymmetry of $\omega$ gives $\omega(X_f,X_g) = -\omega(X_g,X_f) = -X_f(g)$.

**Proposition.** The bracket is $\mathbb{R}$-bilinear and alternating, and it is a derivation in each argument:

$$
\{f, gh\} = \{f, g\}\,h + g\,\{f, h\}.
$$

**Proof.** Bilinearity and alternation are inherited from $\omega$. For the derivation property, $X_{gh}$ is characterised by $\iota_{X_{gh}}\omega = d(gh) = g\,dh + h\,dg$, while $\iota_{gX_h + hX_g}\omega = g\,dh + h\,dg$; by uniqueness $X_{gh} = gX_h + hX_g$. Substituting into $\{f, gh\} = \omega(X_f, X_{gh})$ and using the bilinearity of $\omega$ gives the identity. $\square$

**Theorem.** The Jacobi identity for the bracket is equivalent to the closedness of $\omega$: substituting the Hamiltonian fields into the invariant formula for the differential of a $2$-form and using $[X_f, X_g] = -X_{\{f,g\}}$ gives

$$
d\omega(X_f, X_g, X_h) = -2\bigl(\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\}\bigr).
$$

Consequently, on a symplectic manifold the bracket satisfies the Jacobi identity, and the vector space $C^\infty(M)$ is a Lie algebra under it.

**Proof.** The invariant formula for the exterior derivative on a $2$-form gives

$$
d\omega(X, Y, Z) = X\,\omega(Y, Z) - Y\,\omega(X, Z) + Z\,\omega(X, Y) - \omega([X, Y], Z) + \omega([X, Z], Y) - \omega([Y, Z], X).
$$

Put $X = X_f$, $Y = X_g$, $Z = X_h$. The first three terms are $X_f\{g,h\} - X_g\{f,h\} + X_h\{f,g\} = \{\{g,h\},f\} - \{\{f,h\},g\} + \{\{f,g\},h\}$ using $\{u,v\} = X_v(u)$, and the last three require the identity

$$
[X_f, X_g] = -X_{\{f,g\}},
$$

which follows from $\iota_{[X_f,X_g]}\omega = \mathcal{L}_{X_f}\iota_{X_g}\omega - \iota_{X_g}\mathcal{L}_{X_f}\omega = d\,\iota_{X_f}\iota_{X_g}\omega + \iota_{X_f}d\,\iota_{X_g}\omega = d\,\omega(X_g, X_f) = -d\{f,g\}$, where the second equality uses $d\omega = 0$ and $\mathcal{L}_{X_f}\omega = d\,\iota_{X_f}\omega = d(df) = 0$. Substituting, the last three terms reproduce the three bracket expressions with the signs that make the total equal to twice the negative of the Jacobi sum. Hence the Jacobi sum vanishes for all $f, g, h$ exactly when $d\omega$ vanishes on all triples of Hamiltonian vector fields; since the Hamiltonian fields span the tangent space, the function $d\omega(X_f, X_g, X_h)$ vanishes identically precisely when $d\omega = 0$. $\square$

**Corollary.** On a symplectic manifold, $C^\infty(M)$ is a Lie algebra under the Poisson bracket, the map

$$
f \longmapsto X_f : C^\infty(M) \longrightarrow \mathfrak{X}(M)
$$

is a homomorphism of Lie algebras from $(C^\infty(M), -\{\cdot,\cdot\})$ onto the Lie subalgebra of Hamiltonian vector fields, with kernel the space of locally constant functions on $M$; when $M$ is connected the kernel is the constants $\mathbb{R} \cdot 1$, and the constants are the centre of the bracket.

**Proof.** The image is closed under the commutator, because $[X_f, X_g] = -X_{\{f,g\}} = X_{-\{f,g\}}$; with the bracket $-\{\cdot,\cdot\}$ on functions, the identity is the statement that $f\mapsto X_f$ preserves the bracket. The kernel consists of the functions with $df = 0$, that is, the locally constant functions. If $f$ is locally constant then $\{f,g\} = X_g(f) = 0$ for every $g$, so it is central; conversely a central $f$ has $\omega(X_f, X_g) = 0$ for all $g$ and hence $X_f = 0$, so $f$ is locally constant. $\square$

**Remark.** The identity $[X_f, X_g] = -X_{\{f,g\}}$ explains the sign that appears between the two descriptions: the map $f\mapsto X_f$ is a homomorphism for the bracket or for its negative, but not for both, and the convention chosen here is the one that makes $\iota_{X_f}\omega = df$ hold. The Hamiltonian vector field is the infinitesimal generator of a one-parameter group of symplectomorphisms, because $\mathcal{L}_{X_f}\omega = d\,\iota_{X_f}\omega + \iota_{X_f}d\omega = d^2f = 0$. The flow itself is the solution of the ordinary differential equation $\dot{x} = X_f(x)$, and that differential equation, its existence theory and its long-time behaviour are treated in Part III, where the limit and the derivative of a curve are available.

## Symplectomorphisms and the Flux

**Definition.** The **group of symplectomorphisms** of $(M, \omega)$ is

$$
\operatorname{Symp}(M, \omega) = \{F \in \operatorname{Diff}(M) : F^*\omega = \omega\},
$$

with the group structure of composition. The identity component is written $\operatorname{Symp}_0(M, \omega)$.

**Proposition.** The Lie algebra of the group of symplectomorphisms is the space of symplectic vector fields, and the Hamiltonian vector fields form the Lie subalgebra of those whose $1$-form $\iota_X\omega$ is exact. The sequence of Lie algebras

$$
0 \longrightarrow C^\infty(M)/\mathbb{R} \longrightarrow \mathfrak{X}_{\mathrm{symp}}(M) \longrightarrow H^1_{dR}(M) \longrightarrow 0
$$

is exact, the last map sending $X$ to the class $[\iota_X\omega]$.

**Proof.** A vector field $X$ generates a one-parameter group of symplectomorphisms exactly when $\mathcal{L}_X\omega = 0$, and $\mathcal{L}_X\omega = d\,\iota_X\omega + \iota_Xd\omega = d\,\iota_X\omega$; so $X$ is symplectic precisely when $\iota_X\omega$ is closed. The Hamiltonian fields are those for which $\iota_X\omega = df$ is exact, so the image of $f\mapsto X_f$ is the kernel of the class map, and the kernel of $f \mapsto X_f$ is the space of the locally constant functions. $\square$

**Remark.** The group $\operatorname{Symp}(M, \omega)$ is infinite dimensional, and it is not a Lie group in the finite-dimensional sense; for a closed manifold it carries the structure of a Fréchet Lie group modelled on the closed $1$-forms, and for the foundational material on infinite-dimensional groups the reader is referred to *Diffeomorphism Groups* and *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*, both earlier in this Part. The **flux homomorphism** of the exact sequence measures the failure of a symplectic isotopy to be Hamiltonian, and its image is the **flux group**, a discrete subgroup of $H^1_{dR}(M)$ for a closed manifold.

## Lagrangian Submanifolds

**Definition.** Let $(M, \omega)$ be a symplectic manifold of dimension $2m$ and let $L \subseteq M$ be a submanifold. Then $L$ is **isotropic** if $\omega$ restricts to zero on $L$, meaning that $\omega_x(u, v) = 0$ for all $x \in L$ and $u, v \in T_xL$; **coisotropic** if the $\omega$-orthogonal complement $TL^{\perp} \subseteq TM|_L$ is contained in $TL$; and **Lagrangian** if it is isotropic and $2\dim L = \dim M$.

**Proposition.** Let $L$ be an isotropic submanifold of a symplectic manifold of dimension $2m$. Then $\dim L \leq m$, and $L$ is Lagrangian if and only if it is isotropic of dimension $m$. If $L$ is Lagrangian then $TL = TL^{\perp}$ and $T^*L \cong TL^{\perp}$ by the bundle isomorphism $v \mapsto \omega(v, \cdot)|_{TL}$.

**Proof.** At each point the tangent space $T_xL$ is an isotropic subspace of the symplectic vector space $T_xM$, so the dimension bound and the characterisation of the Lagrangian case are those of *Symplectic Forms and Poisson Brackets*. When $\dim L = m$ the isotropic subspace is maximal isotropic, hence equals its own orthogonal complement, and $TL^{\perp}/TL \cong T^*L$. $\square$

**Example.** Let $Q$ be a manifold and let $Q_0 \subseteq T^*Q$ be the zero section, $Q_0 = \{(q, 0)\}$. Then $\theta$ restricts to zero on $Q_0$, since $p = 0$ there, so $\omega = -d\theta$ restricts to zero; hence $Q_0$ is Lagrangian. The same holds for the graph of a closed $1$-form $\beta$ on $Q$: the graph is the image of $s_\beta(q) = (q, \beta_q)$, and $s_\beta^*\omega = s_\beta^*(-d\theta) = -d(\beta) = 0$ exactly when $d\beta = 0$. Thus the closed $1$-forms on $Q$ parametrise the Lagrangian sections of $T^*Q$.

**Example.** Let $N \subseteq Q$ be a submanifold. Its **conormal bundle** $\nu^*N \subseteq T^*Q$ consists of the covectors annihilating $TN$. It is Lagrangian: in adapted coordinates with $N$ given by $q^{k+1} = \cdots = q^m = 0$, it is described by $q^{k+1} = \cdots = q^m = p_1 = \cdots = p_k = 0$, on which $\omega = \sum_i dq^i\wedge dp_i$ vanishes, and its dimension is $m$. The zero section is the case $N = Q$.

**Theorem (Lagrangian neighbourhood theorem).** Let $L$ be a closed Lagrangian submanifold of a symplectic manifold $(M, \omega)$. Then there is a neighbourhood $U$ of $L$ in $M$, a neighbourhood $V$ of the zero section of $T^*L$ and a symplectomorphism $\Phi : U \to V$ that restricts to the identity on $L$, where $T^*L$ carries the form $-d\theta$ of its tautological form.

**Proof sketch.** The bundle isomorphism $TL^{\perp} \cong T^*L$ identifies the normal bundle of $L$ with $T^*L$, and the exponential map of an auxiliary Riemannian metric provides a diffeomorphism from a neighbourhood of the zero section of $TL^{\perp}$ to a neighbourhood of $L$. Pulling $\omega$ back to $T^*L$ gives a closed form agreeing with the standard form along the zero section; the Moser argument of the Darboux theorem, applied with the linear homotopy between the two forms and the fact that they are cohomologous, produces a diffeomorphism of a possibly smaller neighbourhood correcting the difference. $\square$

**Remark.** The theorem is the local normal form for a Lagrangian submanifold and the exact analogue of the Darboux theorem for a symplectic point: a neighbourhood of a Lagrangian is modelled on a neighbourhood of the zero section of a cotangent bundle, and no further invariant survives. The global theory of Lagrangians — their intersections, their generating functions, their Floer theory — is the subject andthe companions to this article in this Part.

## Compatible Almost Complex Structures

**Definition.** Let $(M, \omega)$ be a symplectic manifold. An **almost complex structure** $J$ on $M$ is a bundle endomorphism $J : TM \to TM$ with $J^2 = -\mathrm{id}$. It is **compatible** with $\omega$ if

$$
\omega(JX, JY) = \omega(X, Y), \qquad g_J(X, Y) = \omega(X, JY) \ \text{ is positive definite}
$$

for all $X, Y \in \mathfrak{X}(M)$.

**Theorem.** Every symplectic manifold $(M, \omega)$ admits a compatible almost complex structure, and the space of compatible almost complex structures is nonempty and contractible.

**Proof sketch.** Choose an auxiliary Riemannian metric $g$ and let $A$ be the bundle endomorphism determined by $g(X, AY) = \omega(X, Y)$; the endomorphism $A$ is $g$-skew and, since $\omega$ is nondegenerate, invertible. Then $-A^2$ is $g$-symmetric and positive definite, so it has a positive-definite square root; setting $J = (-A^2)^{-1/2}A$ gives a $g$-orthogonal complex structure compatible with $\omega$. For contractibility, consider the map that assigns to a Riemannian metric the compatible complex structure produced by this construction; the space of metrics is convex, hence contractible, the fibre over a fixed $J$ is the convex set of the metrics making $J$ orthogonal, and the assignment is a fibration, so the space of compatible almost complex structures is contractible as well. $\square$

**Remark.** The pair $(g_J, J)$ makes $M$ an almost Kähler manifold: a Riemannian manifold with a compatible complex structure. The form $\omega$ is then the fundamental $2$-form of the pair, and the almost complex structure is integrable precisely when $M$ is a complex manifold and $\omega$ is its Kähler form; the integrability condition is the vanishing of the Nijenhuis tensor, and the whole circle of ideas belongs to andbeing written in this Part. Compatible almost complex structures are the technical device that turns a symplectic manifold into a complex-looking one, and they are what makes the pseudoholomorphic curves, meaningful.

## Symplectic Reduction

**Definition.** Let a Lie group $G$ act on a symplectic manifold $(M, \omega)$ by symplectomorphisms, with Lie algebra $\mathfrak{g}$. A **momentum map** for the action is a map $\mu : M \to \mathfrak{g}^*$ such that for every $X \in \mathfrak{g}$ the function $\mu_X = \langle \mu, X\rangle$ satisfies

$$
X^{\#} = X_{\mu_X},
$$

where $X^{\#}$ is the fundamental vector field of the action and $X_{\mu_X}$ is the Hamiltonian vector field of $\mu_X$. A **coadjoint-equivariant** momentum map in addition intertwines the action on $M$ with the coadjoint action on $\mathfrak{g}^*$.

**Theorem (Marsden–Weinstein).** Let $G$ act freely and properly on the symplectic manifold $(M, \omega)$ with an equivariant momentum map $\mu$, and suppose $0 \in \mathfrak{g}^*$ is a regular value of $\mu$. Then the quotient

$$
M /\!/ G = \mu^{-1}(0)/G
$$

is a smooth manifold of dimension $\dim M - 2\dim G$, and it carries a unique symplectic form $\omega_{\mathrm{red}}$ with

$$
i^*\omega = \pi^*\omega_{\mathrm{red}},
$$

where $i : \mu^{-1}(0) \hookrightarrow M$ is the inclusion and $\pi : \mu^{-1}(0) \to M/\!/G$ the quotient map. It is the **symplectic quotient** or **reduced space** of the action.

**Proof sketch.** The regular-value theorem makes $\mu^{-1}(0)$ a submanifold and the quotient a manifold; the tangent space to an orbit is the space of fundamental vector fields, which are Hamiltonian, and the $2$-form $i^*\omega$ annihilates the orbit directions because $\omega(X^{\#}, \cdot) = d\mu_X$ vanishes on $\mu^{-1}(0)$; so $i^*\omega$ descends along $\pi$ and is nondegenerate on the quotient by dimension count, the quotient being symplectic of the stated dimension. $\square$

**Example.** Take $G = U(1)$ acting on $\mathbb{C}^n$ by scalar multiplication with momentum map $\mu(z) = c - |z|^2/2$, where $c > 0$ is a constant; the level $\mu^{-1}(0)$ is the sphere $|z|^2 = 2c$, and the reduced space $\mu^{-1}(0)/U(1)$ is the complex projective space $\mathbb{CP}^{n-1}$, with the induced form the Fubini–Study form. This is the standard construction of the projective spaces as symplectic quotients, and it is the first appearance of the Kähler structures developed.

**Remark.** Reduction is the origin of most of the nontrivial examples of symplectic manifolds, and it is the exact symplectic analogue of the quotient of a manifold by a group action. Its representation-theoretic refinement, the orbit method, identifies the coadjoint orbits of a Lie group with the symplectic manifolds carrying its irreducible representations; the Lie-theoretic input is that of *Lie Groups*, and the applications to representations belong there and to *Representation Theory of Locally Compact Groups*.

## Summary

A symplectic manifold is a smooth manifold with a closed nondegenerate $2$-form $\omega$. Nondegeneracy makes $\omega^\flat : TM \to T^*M$ an isomorphism and forces the dimension to be even, and $\omega^{\wedge m}/m!$ is a nowhere vanishing volume form, so a symplectic manifold is oriented and a symplectomorphism preserves the volume. The standard examples are $\mathbb{R}^{2m}$, the cotangent bundle $T^*Q$ with $\omega = -d\theta$ for the tautological form, the oriented surfaces, and the coadjoint orbits with the Kirillov–Kostant–Souriau form.

The Darboux theorem says that about each point there are coordinates with $\omega = \sum_i dx_i\wedge dy_i$, so a symplectic form has no local invariants; the proof is the Moser argument, which uses the Poincaré lemma and the openness of nondegeneracy. The Hamiltonian vector field of a function is defined by $\iota_{X_f}\omega = df$, the Poisson bracket is $\{f,g\} = \omega(X_f, X_g)$, it is a derivation in each argument, and its Jacobi identity is equivalent to $d\omega = 0$. The map $f \mapsto X_f$ is a Lie algebra homomorphism from $C^\infty(M)$ with the bracket $-\{\cdot,\cdot\}$, with kernel the locally constant functions, and the group of symplectomorphisms has the symplectic vector fields for its Lie algebra, with the Hamiltonian fields as the exact part and the flux measuring the difference.

Lagrangian submanifolds are the isotropic submanifolds of half the dimension, and a neighbourhood of a Lagrangian is symplectomorphic to a neighbourhood of the zero section of its cotangent bundle. Every symplectic manifold carries compatible almost complex structures, forming a contractible space, and this makes every symplectic manifold almost Kähler, with the Kähler case exactly the integrable one. Finally, a free proper symplectic action with an equivariant momentum map has a symplectic quotient $\mu^{-1}(0)/G$, which produces the projective spaces and most of the concrete symplectic manifolds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M, N$ | Smooth manifolds; $T_xM$, $TM$, $T^*M$ the tangent and cotangent objects |
| $\mathfrak{X}(M)$, $\Omega^k(M)$ | Smooth vector fields and smooth $k$-forms |
| $d$, $\int_M$ | Exterior derivative; integral of a top form over an oriented manifold |
| $\omega$ | The symplectic $2$-form; closed and nondegenerate |
| $\omega_0 = \sum_i dx_i\wedge dy_i$ | Standard symplectic form on $\mathbb{R}^{2m}$ |
| $2m$ | The dimension of a symplectic manifold; $m$ half the dimension |
| $\omega^{\flat} : TM \to T^*M$, $\omega^{\sharp}$ | Bundle isomorphism $X \mapsto \omega(X,\cdot)$ and its inverse |
| $\mathrm{vol}_\omega = \omega^{\wedge m}/m!$ | Symplectic volume form; orients $M$ |
| $\theta = \sum_i p_i\,dq^i$ | Tautological $1$-form on $T^*Q$; $\omega = -d\theta$ |
| $F^*\omega = \omega$ | Symplectomorphism $F$; $\operatorname{Symp}(M,\omega)$ the group |
| $X_f$, $\iota_{X_f}\omega = df$ | Hamiltonian vector field of $f$ |
| $\{f,g\} = \omega(X_f,X_g)$ | Poisson bracket of functions on a symplectic manifold |
| $[X_f, X_g] = -X_{\{f,g\}}$ | Hamiltonian fields form a Lie algebra; sign convention |
| $\mathfrak{X}_{\mathrm{symp}}(M)$ | Symplectic vector fields, $\mathcal{L}_X\omega = 0$; Lie algebra of $\operatorname{Symp}$ |
| Isotropic, coisotropic, Lagrangian | $\omega\vert_L = 0$; $TL^{\perp}\subseteq TL$; isotropic of dimension $m$ |
| $\nu^*N$ | Conormal bundle of a submanifold; Lagrangian in $T^*Q$ |
| $J$, $\omega(JX,JY)=\omega(X,Y)$ | Compatible almost complex structure; $g_J(X,Y)=\omega(X,JY)$ |
| $\mu : M \to \mathfrak{g}^*$, $X^{\#} = X_{\mu_X}$ | Momentum map and fundamental vector field of a symplectic action |
| $M/\!/G = \mu^{-1}(0)/G$ | Symplectic quotient; $\dim M - 2\dim G$ |





## Further Reading

- Vladimir I. Arnold and Alexander B. Givental, *Symplectic Geometry*, in *Dynamical Systems IV* (Springer, 2001), for the geometry of symplectic manifolds, Hamiltonian fields and the Darboux theorem.
- Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology* (Oxford University Press, 3rd ed. 2017), for symplectic manifolds, the Moser argument, compatible almost complex structures and Lagrangian submanifolds.
- Ana Cannas da Silva, *Lectures on Symplectic Geometry* (Springer, 2008), for a complete treatment of Darboux, Moser and the symplectic group of a manifold.
- Paulette Libermann and Charles-Michel Marle, *Symplectic Geometry and Analytical Mechanics* (Reidel, 1987), for the cotangent bundle, the tautological form and symplectic reduction.
- Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics* (Cambridge University Press, 1984), for momentum maps, coadjoint orbits and the Marsden–Weinstein quotient.
- Jerrold Marsden and Tudor Ratiu, *Introduction to Mechanics and Symmetry* (Springer, 2nd ed. 1999), for the momentum map and the reduction theorem in detail.
- Jürgen Moser, "On the Volume Elements on a Manifold", *Transactions of the American Mathematical Society* 120 (1965), 286–294, for the isotopy argument that proves the Darboux theorem.
- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2nd ed. 2013), for manifolds, vector fields and the Lie bracket on which the article rests.
