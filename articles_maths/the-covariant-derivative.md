# __The Covariant Derivative__

## Introduction

A **covariant derivative** on a vector bundle is the operator that differentiates its sections by comparing the fibres over neighbouring points through a **connection**; the connection is the horizontal distribution, the covariant derivative is its action on sections, and the two are the same datum read in two ways. The definition, the local connection form and the transformation rule are those of *Fibre Bundles, Connections and Curvature*; this article reads that datum as an **operator** and develops the operator calculus it generates, which is what the rest of the Part and the geometry above it use.

The article develops the covariant derivative from the definition, not repeating the definition itself. It fixes the operator $\nabla_X$ along a vector field, its $C^\infty(M)$-linearity in $X$ and its Leibniz rule in the section, and its extension $d^\nabla$ to the forms with values in the bundle, the operator of degree one whose square is the multiplication by the curvature. It proves that the curvature is the failure of the covariant derivatives to commute, that it is tensorial, and that the Bianchi identity is the operator statement $d^\nabla R = 0$. It then develops **parallel transport**, the flow of the equation $\nabla_{\dot\gamma}V = 0$ along a curve, which turns the curvature into the infinitesimal non-commutativity of translation around a small loop and recovers the holonomy group. It treats the metric-compatible and torsion-free case, the Levi–Civita connection of a metric, and the autoparallel curves it defines.

The article assumes the vector bundles, their sections and frames, the connection, the connection form, the curvature, the structure equation, the Bianchi identity and the holonomy group of *Fibre Bundles, Connections and Curvature*; the vector fields, the Lie bracket and the tangent bundle of *Smooth Manifolds and Differential Geometry*; and the differential forms and the exterior derivative of *Differential Forms and Stokes' Theorem*. The existence and uniqueness of the solution of the parallel-transport equation is the theorem of *Ordinary Differential Equations*, later in this Part, and is quoted where it is used. The geodesics, the exponential map of a metric and the curvature as a geometric object are Part IV's, and are named here only as forward references. No physics is invoked.

## The Covariant Derivative as an Operator

### The Operator Along a Vector Field

Let $E \to M$ be a vector bundle over a smooth manifold $M$ and let $\nabla$ be a connection on $E$, so that $\nabla : \Gamma(E) \to \Gamma(T^*M \otimes E)$ is $\mathbb{R}$-linear and satisfies $\nabla(fs) = df \otimes s + f\,\nabla s$ for $f \in C^\infty(M)$ and $s \in \Gamma(E)$, as in *Fibre Bundles, Connections and Curvature*. For a vector field $X \in \mathrm{X}(M)$ the **covariant derivative along $X$** is the operator

$$
\nabla_X : \Gamma(E) \longrightarrow \Gamma(E), \qquad \nabla_X s = \langle \nabla s, X\rangle .
$$

**Proposition.** The assignment $X \mapsto \nabla_X$ is $C^\infty(M)$-linear, $\nabla_{fX+gY} = f\nabla_X + g\nabla_Y$, and for each $X$ the operator $\nabla_X$ is a first-order differential operator on the sections of $E$ in the sense of *Differential Operators on a Manifold*, with the Leibniz rule

$$
\nabla_X(fs) = (Xf)\,s + f\,\nabla_X s, \qquad f \in C^\infty(M),\ s \in \Gamma(E).
$$

Its principal symbol is $\sigma_1(\nabla_X)(x,\xi) = \langle \xi, X_x\rangle\, \mathrm{id}_{E_x}$.

*Proof.* The $C^\infty(M)$-linearity in $X$ is the pairing of the $1$-form $\nabla s$ with $X$; the Leibniz rule is the defining Leibniz rule of the connection evaluated on $X$. In a chart with a frame $(e_a)$ the operator reads $(\nabla_X s)^a = X(s^a) + \sum_b \omega^a_{\ b}(X)\,s^b$ with smooth coefficients, which is a first-order operator whose top-order part is $X(s^a)$ on each component; the symbol follows.

### Local Expression and the Affine Space of Connections

In a local frame $e = (e_1, \ldots, e_r)$ over an open set $U$, the connection form $\omega = (\omega^a_{\ b})$ is the matrix of $1$-forms defined by $\nabla e_b = \sum_a \omega^a_{\ b}\otimes e_a$, and a section $s = \sum_b s^b e_b$ has

$$
\nabla_X s = \sum_a \Bigl(X(s^a) + \sum_b \omega^a_{\ b}(X)\,s^b\Bigr) e_a, \qquad \text{equivalently} \quad \nabla = d + \omega
$$

on the components, where $d$ is the exterior derivative of the coefficient functions. Under a change of frame $e' = eg$ the form transforms as $\omega' = g^{-1}\omega g + g^{-1}dg$.

**Proposition.** The operators $\nabla_X$ arising from the connections on $E$ form an affine space: if $\nabla$ and $\nabla'$ are connections, then $\nabla' - \nabla$ is a $C^\infty(M)$-linear map $\Gamma(E) \to \Gamma(T^*M \otimes E)$, that is, a section of $T^*M \otimes \operatorname{End}(E)$, and every such section arises.

*Proof.* Both operators satisfy the Leibniz rule with the same $df \otimes s$ term, so the difference annihilates the multiplication by a function; a map that is linear over $C^\infty(M)$ is a bundle map, here a section of $T^*M \otimes \operatorname{End}E$. Conversely, adding such a section to a connection preserves the Leibniz rule. In a frame the statement is that $\omega' - \omega$ is a matrix of $1$-forms, which is the affine statement of the transformation rule.

### The Extension to Bundle-Valued Forms

**Definition.** The **exterior covariant derivative** is the unique $\mathbb{R}$-linear operator

$$
d^\nabla : \Omega^p(M; E) \longrightarrow \Omega^{p+1}(M; E)
$$

that agrees with $\nabla$ on $\Omega^0(M;E) = \Gamma(E)$ and satisfies the graded Leibniz rule

$$
d^\nabla(\alpha \wedge s) = d\alpha \wedge s + (-1)^p\, \alpha \wedge \nabla s
$$

for $\alpha \in \Omega^p(M)$ and $s \in \Gamma(E)$; on $\alpha \otimes s$ the two rules combine to $d^\nabla(\alpha \otimes s) = d\alpha \otimes s + (-1)^p\alpha \wedge \nabla s$. When $E = \operatorname{End}(F)$ and $\nabla$ is the connection induced on the endomorphisms, the same operator acts on an $\operatorname{End}(F)$-valued form $\beta$ by

$$
d^\nabla\beta = d\beta + [\omega, \beta],
$$

the bracket being the graded commutator of the matrix of forms with the matrix of $\beta$.

**Proposition.** The operator $d^\nabla$ is well defined by these requirements and is the operator of degree one, locally $d + \omega \wedge \cdot$, on the graded module $\Omega^\bullet(M;E)$ of $E$-valued forms. It is not a derivation of a graded-commutative algebra unless $E$ is the trivial line bundle, because the product of two $E$-valued forms is not defined; it is a degree-one operator on a graded module over the graded-commutative algebra of scalar forms, and it satisfies the graded Leibniz rule over that module structure.

*Proof.* The requirements determine the operator on the generators $\alpha\otimes s$ and hence, by additivity, everywhere; the local expression $d + \omega\wedge\cdot$ is obtained by writing $s$ in a frame, and it is the unique operator with the two stated properties.

## The Curvature as the Square of the Covariant Derivative

### The Operator Identity

**Theorem.** For every connection $\nabla$ on $E$ there is a unique section $R$ of $\Lambda^2T^*M \otimes \operatorname{End}(E)$, the **curvature**, such that for every pair of vector fields $X, Y$ and every section $s$,

$$
R(X, Y)s = \nabla_X\nabla_Y s - \nabla_Y\nabla_X s - \nabla_{[X,Y]}s .
$$

Equivalently, $R \wedge \cdot = (d^\nabla)^2$ on the $E$-valued forms, and in a frame $R = d\omega + \omega \wedge \omega$. The contraction $R(X,Y)$ is $C^\infty(M)$-linear in $X$ and $Y$ and in $s$, so it is a tensor; and it is the obstruction to the operators $\nabla_X$ forming a representation of the Lie algebra of vector fields, the failure being measured by the bracket $[X,Y]$.

*Proof.* The difference of the three terms is $C^\infty(M)$-linear in $s$: the terms involving derivatives of $f$ in $\nabla_X\nabla_Y(fs) - \nabla_Y\nabla_X(fs)$ cancel against those of $\nabla_{[X,Y]}(fs)$, by the Leibniz rule and the identity $XYf - YXf = [X,Y]f$. It is also $C^\infty(M)$-linear in $X$ and $Y$, because $\nabla_X$ depends on $X$ through its value pointwise and the bracket is skew. Hence the expression defines a bundle map $\Lambda^2T^*M \to \operatorname{End}(E)$, which is the section $R$. The identification with $(d^\nabla)^2$ and with $d\omega + \omega\wedge\omega$ is the computation of *Fibre Bundles, Connections and Curvature*, where the structure equation is proved.

**Corollary.** $\nabla_X\nabla_Y - \nabla_Y\nabla_X = \nabla_{[X,Y]} + R(X,Y)$, so the curvature is exactly the failure of the operators $\nabla_X$ to commute with the Lie bracket of the fields; the connection is **flat**, $R = 0$, if and only if $X \mapsto \nabla_X$ is a representation of the Lie algebra $\mathrm{X}(M)$.

**Corollary (the Bianchi identity).** $d^\nabla R = 0$; in a frame, $dR + [\omega, R] = 0$. Consequently $R$ is a closed form for the operator $d^\nabla$, and its class is the first obstruction to the flatness of the connection beyond the vanishing of $R$ itself.

### Flatness and the Local Frame

**Theorem.** A connection is flat if and only if it is locally trivial: about every point there is a frame in which $\omega = 0$, equivalently a family of local sections with $\nabla s = 0$ that spans the bundle. For a principal bundle the corresponding statement is that $\omega = g^{-1}dg$ locally, and the horizontal distribution is integrable.

*Proof.* That a flat frame gives $R = d\omega + \omega\wedge\omega = 0$ is immediate. Conversely, if $R = 0$ the equation $\nabla s = 0$ is a system of linear first-order partial differential equations whose integrability condition is the vanishing of the curvature, so it is locally solvable by the Frobenius theorem with a solution space of the rank of $E$; this produces the flat frame. The principal statement is the same argument read in the connection form, and the integrability of the horizontal distribution is the Frobenius theorem applied to $\ker\omega$.

The local frame in which the connection is trivial is the flat case of the parallel transport of the next section: a global flat frame exists exactly when the holonomy of the connection is trivial, and it exists locally always.

## Parallel Transport

### The Parallel Transport Equation

Let $\gamma : [a,b] \to M$ be a smooth curve and let $V$ be a section of $E$ along $\gamma$, that is, a smooth family $V(t) \in E_{\gamma(t)}$. The section is **parallel along $\gamma$** if

$$
\nabla_{\dot\gamma}V = 0,
$$

an equation whose local form in a frame pulled back to $[a,b]$ is the linear system of ordinary differential equations

$$
\dot V^a(t) + \sum_b \omega^a_{\ b}(\dot\gamma(t))\, V^b(t) = 0, \qquad a = 1, \ldots, r .
$$

**Theorem (existence and uniqueness).** For every curve $\gamma$ and every initial value $v \in E_{\gamma(a)}$ there is a unique parallel section $V$ along $\gamma$ with $V(a) = v$.

*Proof.* Locally the equation is a linear system of ordinary differential equations with continuous coefficients, so the theorem of *Ordinary Differential Equations*, later in this Part, gives a unique local solution for each initial value; the solutions on the overlaps of a cover of the compact interval agree by uniqueness, and a finite cover glued by the composition of the flows gives the global solution on $[a,b]$. The solution depends smoothly on the initial value because the flow of a linear system is linear in the initial condition.

### The Parallel Transport Map and Holonomy

**Definition.** The **parallel transport** along $\gamma$ is the map

$$
P_\gamma : E_{\gamma(a)} \longrightarrow E_{\gamma(b)}, \qquad P_\gamma(v) = V(b),
$$

where $V$ is the parallel section with $V(a) = v$.

**Theorem.** The map $P_\gamma$ is a linear isomorphism; it depends only on the curve up to reparametrisation preserving the endpoints; it is functorial under concatenation, $P_{\gamma_2 * \gamma_1} = P_{\gamma_2}\circ P_{\gamma_1}$, and $P_{\gamma^{-1}} = P_\gamma^{-1}$. For closed curves based at $x$ the maps $P_\gamma$ form a subgroup of $GL(E_x)$, the **holonomy group**, and its identity component is the holonomy group of the connection.

*Proof.* Linearity and invertibility are the linearity of the equation and the reversibility of the curve. Reparametrisation invariance is the chain rule, which replaces $\dot\gamma$ by a positive multiple and leaves the equation's solution set unchanged. The concatenation and inverse laws are the uniqueness of the solution of the initial-value problem applied to the two subintervals and to the reversed curve. The group laws follow, and the closed curves at a fixed base give a subgroup of the linear group of the fibre, which is a Lie subgroup because the transport depends smoothly on the curve.

**Theorem (curvature as the infinitesimal holonomy).** Let $X, Y$ be vector fields on a neighbourhood of $x$, let $\square_\epsilon$ be the coordinate rectangle spanned by $\epsilon X$ and $\epsilon Y$ and traversed in the order $X, Y, -X, -Y$, and let $P_\epsilon$ be the parallel transport around it. Then

$$
P_\epsilon = \mathrm{id} - \epsilon^2\, R(X, Y)(x) + O(\epsilon^3)
$$

as $\epsilon \to 0$. Consequently the curvature endomorphisms $R(X,Y)(x)$ span the Lie algebra of the holonomy group, and the connection is flat if and only if the parallel transport around every contractible loop is the identity.

*Proof sketch.* Write the parallel transport as the flow of the linear system $\dot V = -\omega(\dot\gamma)V$ and expand the ordered product of the four flows in powers of $\epsilon$ by the Lie–Trotter product formula; the first-order terms cancel by the opposite traversals, and the second-order term is the commutator $d\omega + \omega\wedge\omega$ evaluated on $X\wedge Y$, which is $R(X,Y)$. The span statement is the theorem of Ambrose and Singer, quoted from *Fibre Bundles, Connections and Curvature*; the flatness criterion follows because a flat connection has a flat local frame, in which $P_\epsilon = \mathrm{id}$.

### The Autoparallel Curves

**Definition.** A smooth curve $\gamma$ in $M$ is **autoparallel** for a connection $\nabla$ on $TM$ if $\nabla_{\dot\gamma}\dot\gamma = 0$; in a chart with Christoffel symbols $\Gamma^i_{jk}$ the equation reads $\ddot\gamma^i + \sum_{j,k}\Gamma^i_{jk}\dot\gamma^j\dot\gamma^k = 0$.

The autoparallel curves are the straight lines of the connection: they are the curves whose velocity is parallel along themselves, and in a flat frame they are the linear curves. For the Levi–Civita connection of a Riemannian metric they are the geodesics, and the metric geometry of those curves — the exponential map, the length-minimising property, the completeness — is *Riemannian Geometry* and *Curvature and Geodesics* in Part IV; what belongs to the present article is the differential equation, its existence and uniqueness by *Ordinary Differential Equations*, and the fact that the equation is the same for every connection on the tangent bundle.

## The Metric-Compatible and Torsion-Free Case

**Definition.** Let $E$ carry a metric $h$, a smooth family of inner products on the fibres. A connection $\nabla$ on $E$ is **metric-compatible** (or **metric**) if

$$
X\,h(s, t) = h(\nabla_X s, t) + h(s, \nabla_X t) \qquad \text{for all } X \in \mathrm{X}(M),\ s, t \in \Gamma(E).
$$

The **torsion** of a connection $\nabla$ on the tangent bundle $TM$ is the tensor $T(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$, a section of $\Lambda^2T^*M \otimes TM$; the connection is **torsion-free** if $T = 0$.

**Theorem (fundamental theorem of Riemannian geometry).** On a Riemannian manifold $(M,g)$ there is exactly one connection on $TM$ that is metric-compatible and torsion-free, the **Levi–Civita connection**. It is determined by the Koszul formula

$$
2g(\nabla_XY, Z) = X\,g(Y,Z) + Y\,g(X,Z) - Z\,g(X,Y) - g(X,[Y,Z]) - g(Y,[X,Z]) + g(Z,[X,Y]),
$$

which expresses its covariant derivative in terms of the metric and the Lie bracket alone.

*Proof.* The right-hand side is $C^\infty(M)$-linear in $X$, $Y$ and $Z$, so it defines the three contractions with the Levi–Civita symbol, hence a connection; substituting the formula into the metric and the torsion conditions verifies them. Uniqueness follows because the difference of two metric and torsion-free connections is a tensor $S(X,Y)$ that is skew in $X,Y$ and satisfies $g(S(X,Y),Z) + g(S(X,Z),Y) = 0$, a tensor that polarises to zero; the Koszul formula computes the covariant derivative from the data, so there is nothing left free.

**Proposition.** For a metric-compatible connection the parallel transport preserves the metric, $h(P_\gamma u, P_\gamma v) = h(u,v)$ for every curve $\gamma$; conversely, if the parallel transport preserves the metric for every curve, the connection is metric-compatible.

*Proof.* If $u, v$ are parallel along $\gamma$, then $\frac{d}{dt}h(u,v) = \dot\gamma\,h(u,v) = h(\nabla_{\dot\gamma}u, v) + h(u,\nabla_{\dot\gamma}v) = 0$; the converse differentiates the constancy of $h$ along the parallel sections with the given initial values.

The two conditions of the theorem are the ones that single out the Levi–Civita connection from the affine space of the connections, and the metric refinement of it — the metric as an object, its curvature and its geodesics — is the subject of *Riemannian Geometry* in Part IV; the metric-compatibility condition on an arbitrary bundle, its reading as adjointness, and its interaction with an involution are the subject of *Hermitian Connections and the Adjoint* and *Hermitian Vector Bundles and the Chern Connection* in this category.

## Summary

A covariant derivative is a connection read as an operator: $\nabla_X$ is first-order, $C^\infty(M)$-linear in $X$ and a derivation in the section; in a frame it is $d + \omega$ on the components, and the connections on a bundle form an affine space modelled on the $1$-forms with values in the endomorphisms. Extending to the bundle-valued forms gives the operator $d^\nabla$ of degree one, locally $d + \omega\wedge\cdot$, whose square is the multiplication by the curvature. The curvature $R(X,Y) = \nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X,Y]}$ is a tensorial $2$-form with values in the endomorphisms; it is the failure of the covariant derivatives to represent the Lie algebra of vector fields, it satisfies the Bianchi identity $d^\nabla R = 0$, and it vanishes exactly when the connection is locally trivial.

Parallel transport solves the equation $\nabla_{\dot\gamma}V = 0$ along a curve; the solution exists and is unique, and it defines a linear isomorphism $P_\gamma$ between the fibres that is functorial under concatenation and inversion. The maps around the closed curves form the holonomy group; the parallel transport around a small rectangle is $\mathrm{id} - \epsilon^2R(X,Y) + O(\epsilon^3)$, so the curvature spans the Lie algebra of the holonomy, and flatness is the triviality of the transport around the contractible loops. The autoparallel curves are the curves with $\nabla_{\dot\gamma}\dot\gamma = 0$, the straight lines of the connection. The metric-compatible and torsion-free condition singles out the Levi–Civita connection of a metric, expressed by the Koszul formula, and for it the parallel transport is an isometry; the metric geometry of geodesics and curvature is Part IV's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\nabla$, $\nabla_X s = \langle\nabla s, X\rangle$ | Connection and covariant derivative along a vector field |
| $\nabla_X(fs) = (Xf)s + f\nabla_Xs$ | Leibniz rule; $\nabla_{fX+gY} = f\nabla_X + g\nabla_Y$ |
| $\omega = (\omega^a_{\ b})$, $\nabla = d + \omega$ | Connection form in a frame; local components |
| $\omega' = g^{-1}\omega g + g^{-1}dg$ | Change of frame |
| $\Omega^p(M;E)$, $d^\nabla$ | $E$-valued forms and the exterior covariant derivative $d + \omega\wedge\cdot$ |
| $d^\nabla\beta = d\beta + [\omega,\beta]$ | Action on $\operatorname{End}(E)$-valued forms |
| $R(X,Y) = \nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X,Y]}$ | Curvature; $(d^\nabla)^2 = R\wedge\cdot$ |
| $R = d\omega + \omega\wedge\omega$ | Local curvature; the structure equation |
| $d^\nabla R = 0$, $dR + [\omega,R] = 0$ | Bianchi identity |
| Flat | $R = 0$; locally $\omega = 0$ and the horizontal distribution is integrable |
| $\nabla_{\dot\gamma}V = 0$ | Parallel transport equation along a curve |
| $P_\gamma : E_{\gamma(a)} \to E_{\gamma(b)}$ | Parallel transport, a linear isomorphism |
| Holonomy group | $\{P_\gamma\}$ over the closed curves based at $x$; a subgroup of $GL(E_x)$ |
| $R(X,Y)(x)$ | Spans the Lie algebra of the holonomy (Ambrose–Singer) |
| $\nabla_{\dot\gamma}\dot\gamma = 0$ | Autoparallel curves; the geodesics for the Levi–Civita connection |
| $T(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$ | Torsion of a connection on $TM$ |
| Metric-compatible, $Xh(s,t) = h(\nabla_Xs,t) + h(s,\nabla_Xt)$ | The connection preserves the metric |
| Koszul formula, Levi–Civita | The unique metric and torsion-free connection of a metric |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. I (Interscience, 1963), for connections, the covariant derivative, the structure equation and the holonomy.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. (Springer, 2018), for the covariant derivative, the Koszul formula, the Levi–Civita connection and parallel transport.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry*, vol. II (Publish or Perish, 3rd ed. 1999), for the operator viewpoint on connections and curvature.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the exterior covariant derivative and the curvature identities in the holomorphic case, cited for the forward reference.
- Michael E. Taylor, *Partial Differential Equations*, vol. I (Springer, 2nd ed. 2011), for the parallel-transport equation as a linear system and the regularity of its flow.
