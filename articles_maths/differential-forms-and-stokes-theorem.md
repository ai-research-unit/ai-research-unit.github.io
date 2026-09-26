
# __Differential Forms and Stokes' Theorem__

## Introduction

A differential form on a smooth manifold is a smoothly varying alternating form on the tangent spaces, and the companion article *The Determinant and Alternating Forms* shows that the algebra of alternating forms on a single vector space is the exterior algebra of its dual. The global theory assembles these algebras into a bundle, forms the module of smooth sections, and adds one new operation, the **exterior derivative** $d$, a degree-one derivation with $d^2 = 0$. The resulting complex of forms is the de Rham complex, whose cohomology is a topological invariant of the manifold; the exterior derivative is also the object that makes integration local, because it is the operator for which **Stokes' theorem** holds: the integral of $d\omega$ over an oriented manifold with boundary equals the integral of $\omega$ over the boundary.

This article develops the calculus of differential forms. It defines the bundle of forms, the exterior derivative in coordinates and invariantly, the de Rham complex and its cohomology, the Poincaré lemma, the integration of top-degree forms on oriented manifolds with the change-of-variables formula, and Stokes' theorem with its classical specialisations — the fundamental theorem of calculus, Green's theorem, the divergence theorem and the classical Stokes theorem of vector calculus. It closes with the Hodge star and the Laplace–de Rham operator, and with the theorem of de Rham identifying the de Rham cohomology with singular cohomology with real coefficients.

The treatment is differential-topological throughout. Manifolds are smooth, second countable and Hausdorff; they may have boundary, and the orientation conventions for the boundary are fixed below. The base field is $\mathbb{R}$. The exterior algebra is written $\Lambda^k$ with the notation of *Exterior Powers* and *The Exterior Algebra*, so the wedge product is $\wedge$, the degree of a form is its exterior degree, and the Koszul sign rule is $\alpha \wedge \beta = (-1)^{pq}\beta \wedge \alpha$ for forms of degrees $p$ and $q$. The determinant is that of *The Determinant and Alternating Forms*. No physics is invoked.

## Differential Forms on a Manifold

### The Cotangent Bundle and the Bundle of Forms

Let $M$ be a smooth manifold of dimension $n$. The **cotangent bundle** $T^*M$ is the dual of the tangent bundle, and for each $x \in M$ the fibre $T^*_xM$ is the dual space of the tangent space $T_xM$.

**Definition.** The **bundle of $k$-forms** on $M$ is the exterior power bundle

$$
\Lambda^k T^*M = \bigsqcup_{x \in M} \Lambda^k(T^*_xM),
$$

with the vector space structure on each fibre inherited from the exterior power, endowed with the smooth structure induced from that of $T^*M$.

**Definition.** A **differential $k$-form** on $M$ is a smooth section of $\Lambda^k T^*M$. The space of such sections is written $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$; elements of $\Omega^0(M)$ are the smooth functions, $\Omega^0(M) = C^\infty(M)$, and $\Omega^1(M)$ is the space of smooth $1$-forms, the smooth sections of the cotangent bundle. The **degree** of an element of $\Omega^k(M)$ is $k$, and

$$
\Omega^\bullet(M) = \bigoplus_{k=0}^{n} \Omega^k(M)
$$

is the **algebra of differential forms**, a graded-commutative algebra under the wedge product.

**Proposition.** In a chart $(U, x^1, \ldots, x^n)$, every $k$-form on $U$ has a unique expression

$$
\omega = \sum_{i_1 < i_2 < \cdots < i_k} \omega_{i_1\cdots i_k}\, dx^{i_1} \wedge \cdots \wedge dx^{i_k}
$$

with coefficients $\omega_{i_1\cdots i_k} \in C^\infty(U)$, and the $dx^{i_1}\wedge\cdots\wedge dx^{i_k}$ give a basis of $\Lambda^k(T^*_xM)$ at each point of $U$. Consequently $\Omega^k(M) = 0$ for $k > n$ and $\Omega^n(M)$ is the module of **top forms**.

**Proof.** The cotangent bundle is locally trivial with fibre $\mathbb{R}^n$, and the exterior power of a free module of rank $n$ has the stated basis; the sections are smooth precisely when the coefficients are. $\square$

### Smooth Sections and the Module Structure

**Proposition.** $\Omega^\bullet(M)$ is a module over $C^\infty(M)$ and a graded-commutative algebra over $\mathbb{R}$; the wedge product is associative, unital, and satisfies $\alpha \wedge \beta = (-1)^{pq}\beta\wedge\alpha$ for $\alpha$ of degree $p$ and $\beta$ of degree $q$.

**Proof.** Multiplication of a form by a function is defined pointwise and preserves smoothness, giving the module structure; the wedge product is defined fibrewise from the exterior algebra, so it inherits associativity, the unit, and the sign rule of *The Exterior Algebra*. $\square$

### The Pullback

**Definition.** Let $F : M \to N$ be a smooth map. The **pullback** of a form $\omega \in \Omega^k(N)$ is the form $F^*\omega \in \Omega^k(M)$ defined by

$$
(F^*\omega)_x(v_1, \ldots, v_k) = \omega_{F(x)}(dF_x v_1, \ldots, dF_x v_k), \qquad v_j \in T_xM.
$$

**Theorem.** The pullback is an algebra homomorphism $F^* : \Omega^\bullet(N) \to \Omega^\bullet(M)$ that preserves the grading, and it is contravariantly functorial: $(G \circ F)^* = F^* \circ G^*$ and $\mathrm{id}^* = \mathrm{id}$. It commutes with the exterior derivative defined below, $F^* \circ d = d \circ F^*$.

**Proof.** At each point the pullback is the transpose of $dF_x$ applied to an alternating form, and pulling back an alternating form along a linear map preserves the wedge product, by the functoriality of the exterior algebra; the module structure is preserved because $F^*$ pulls functions back by composition. Contravariant functoriality is the chain rule. The commutation with $d$ is proved after the exterior derivative is defined. $\square$

## The Exterior Derivative

### Definition in Coordinates

**Definition.** The **exterior derivative** is the $\mathbb{R}$-linear map $d : \Omega^k(M) \to \Omega^{k+1}(M)$ defined in a chart $(U, x^1, \ldots, x^n)$ by

$$
d\Bigl(\sum_{I} \omega_I\, dx^I\Bigr) = \sum_{I}\sum_{j=1}^{n} \frac{\partial \omega_I}{\partial x^j}\, dx^j \wedge dx^I,
$$

where $dx^I = dx^{i_1}\wedge\cdots\wedge dx^{i_k}$ for $I = (i_1 < \cdots < i_k)$.

**Theorem.** The operator $d$ is well defined, that is, the expression above is independent of the choice of chart, and it is characterised on $\Omega^k(M)$ by

**(a)** $d(\alpha + \beta) = d\alpha + d\beta$ and $d(c\alpha) = c\, d\alpha$ for $c \in \mathbb{R}$;

**(b)** $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^{k}\, \alpha \wedge d\beta$ for $\alpha \in \Omega^k(M)$;

**(c)** for a function $f$, $df$ is the differential of $f$; and

**(d)** $d \circ d = 0$.

It is the unique operator with properties (a), (b), (c) and (d).

**Proof sketch.** One checks the coordinate expression transforms correctly under a change of chart: the chain rule and the antisymmetry of the wedge product produce the two terms that cancel when the transformation is applied to $d\omega$. For the characterisation, property (b) with the $dx^{i}$ and property (c) with the coordinate functions reconstruct the displayed formula term by term, so any two operators with the listed properties agree; conversely the displayed operator has them, and $d^2 = 0$ follows from the equality of mixed partial derivatives, $\frac{\partial^2 f}{\partial x^i \partial x^j} = \frac{\partial^2 f}{\partial x^j \partial x^i}$, together with $dx^i\wedge dx^j = -dx^j\wedge dx^i$. $\square$

**Remark.** Property (b) is the graded Leibniz rule, and it says that $d$ is an odd derivation of the graded-commutative algebra of forms; the sign $(-1)^k$ is the Koszul sign of the exterior algebra. The exterior derivative is not a tensor: the value of $d\omega$ at a point depends on the first derivatives of the coefficients, which is why the differential structure is needed and why the purely algebraic theory of *The Determinant and Alternating Forms* does not contain $d$.

### The Coordinate-Free Characterisation

**Definition.** A **derivation** of $\Omega^\bullet(M)$ is an $\mathbb{R}$-linear map $D : \Omega^\bullet(M) \to \Omega^\bullet(M)$ of degree one satisfying $D(\alpha\wedge\beta) = D\alpha\wedge\beta + (-1)^{|\alpha|}\alpha\wedge D\beta$; a derivation is **algebraic** if it is $C^\infty(M)$-linear, that is, if $D(f\alpha) = f D(\alpha)$.

**Proposition.** An algebraic derivation of $\Omega^\bullet(M)$ of degree one is the same thing as a section of $\Lambda^2 T^*M$, and $d$ is not algebraic. The exterior derivative is characterised among degree-one derivations by the values it takes on functions.

**Proof.** An algebraic derivation is determined by its values on $\Omega^0(M) = C^\infty(M)$ and $\Omega^1(M)$, and sending a function to zero and a $1$-form to a $2$-form defines a tensor in $\Lambda^2T^*M$. The failure of $d$ to be algebraic is the Leibniz rule for a product by a function, $d(f\alpha) = df\wedge\alpha + f\,d\alpha$, which has a term involving $df$. $\square$

### The Exterior Derivative and the Pullback

**Proposition.** For every smooth map $F : M \to N$ and every form $\omega$ on $N$ one has $F^*(d\omega) = d(F^*\omega)$.

**Proof.** Both sides are derivations of the graded algebra to which $F^*$ applies, and it suffices to check the identity on functions and on exact $1$-forms. For a function $f$ on $N$, $F^*(df) = d(f\circ F) = d(F^*f)$. Additivity and the graded Leibniz rule extend the identity to all forms. $\square$

## The de Rham Complex

### The Complex

**Definition.** The **de Rham complex** of $M$ is the sequence

$$
0 \longrightarrow \Omega^0(M) \xrightarrow{\ d\ } \Omega^1(M) \xrightarrow{\ d\ } \Omega^2(M) \xrightarrow{\ d\ } \cdots \xrightarrow{\ d\ } \Omega^n(M) \longrightarrow 0,
$$

with $d^2 = 0$. A form with $d\omega = 0$ is **closed**; a form with $\omega = d\eta$ is **exact**. Every exact form is closed.

**Definition.** The **de Rham cohomology** of $M$ is

$$
H^k_{dR}(M) = \frac{\ker\bigl(d : \Omega^k(M) \to \Omega^{k+1}(M)\bigr)}{\operatorname{im}\bigl(d : \Omega^{k-1}(M) \to \Omega^k(M)\bigr)},
$$

the space of closed $k$-forms modulo exact ones. It is a real vector space, and $H^0_{dR}(M)$ is the space of locally constant functions.

### Functoriality and the Mayer–Vietoris Sequence

**Theorem.** The pullback along a smooth map $F : M \to N$ induces a linear map $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ on cohomology, and this assignment is contravariantly functorial; homotopic maps induce the same map on cohomology.

**Proof.** The commutation $F^* d = d F^*$ shows that $F^*$ preserves closed and exact forms, so it descends. Functoriality is the functoriality of the pullback. The homotopy invariance follows from the construction of a chain homotopy between the pullbacks of homotopic maps, the **prism operator**, which is built from the integral of the pullback along the homotopy. $\square$

**Theorem (Mayer–Vietoris).** Let $M = U \cup V$ be an open cover. Then there is a long exact sequence

$$
\cdots \longrightarrow H^k_{dR}(M) \longrightarrow H^k_{dR}(U) \oplus H^k_{dR}(V) \longrightarrow H^k_{dR}(U \cap V) \xrightarrow{\ \delta\ } H^{k+1}_{dR}(M) \longrightarrow \cdots,
$$

where the connecting map $\delta$ is the boundary operator of the short exact sequence of complexes $0 \to \Omega^\bullet(M) \to \Omega^\bullet(U)\oplus\Omega^\bullet(V) \to \Omega^\bullet(U\cap V) \to 0$ built from a partition of unity.

**Proof sketch.** The restriction maps fit into a short exact sequence of complexes; the existence of a partition of unity subordinate to the cover shows that the third map is surjective, and the snake lemma produces the long exact sequence. $\square$

### The Poincaré Lemma

**Definition.** An open set $U \subseteq \mathbb{R}^n$ is **star-shaped** with respect to a point $p$ if for every $x \in U$ the segment from $p$ to $x$ lies in $U$; a manifold is **contractible** if it is homotopy equivalent to a point.

**Theorem (Poincaré lemma).** If $U \subseteq \mathbb{R}^n$ is star-shaped (in particular if $U$ is an open ball or all of $\mathbb{R}^n$), then every closed form of positive degree is exact:

$$
H^k_{dR}(U) = 0 \quad \text{for } k \geq 1, \qquad H^0_{dR}(U) = \mathbb{R}.
$$

**Proof.** Let $U$ be star-shaped with respect to $0$. Define a **homotopy operator** $h : \Omega^k(U) \to \Omega^{k-1}(U)$ by

$$
h(\omega) = \int_0^1 t^{k-1}\, \iota_{x}\, \omega(tx)\, dt,
$$

where $\iota_x$ is the contraction with the radial vector field $x = \sum_j x^j \partial_{x^j}$. One checks the homotopy identity $d\,h + h\,d = \mathrm{id}$ on $\Omega^k(U)$ for $k \geq 1$; a closed form of positive degree therefore satisfies $\omega = d(h\omega)$ and is exact. $\square$

**Corollary.** The de Rham cohomology of a contractible manifold is $\mathbb{R}$ in degree $0$ and zero in positive degrees. In particular the de Rham complex computes a homotopy invariant of the manifold, not merely a differential-geometric one.

## Integration of Forms

### Orientation and the Integral of a Top Form

**Definition.** An **orientation** of an $n$-manifold $M$ is a nowhere vanishing top form $\mathrm{vol} \in \Omega^n(M)$, or an equivalence class of atlases whose transition functions have positive Jacobian determinant; an oriented manifold is a manifold with a chosen orientation. The orientation induces an orientation on each tangent space by declaring a basis $(v_1, \ldots, v_n)$ to be positively oriented when $\mathrm{vol}(v_1, \ldots, v_n) > 0$.

**Definition.** Let $M$ be an oriented $n$-manifold and $\omega \in \Omega^n(M)$ a top form with compact support. Write $\omega = f\, dx^1\wedge\cdots\wedge dx^n$ in a positively oriented chart $(U, x)$, and define the **integral** of $\omega$ over $U$ to be the ordinary integral $\int_{x(U)} f\, dx^1\cdots dx^n$ of the coefficient function. For a general compactly supported $\omega$ choose a finite cover by positively oriented charts subordinate to a partition of unity and sum the local integrals.

**Theorem (change of variables).** The integral is well defined, and if $F : N \to M$ is an orientation-preserving diffeomorphism between oriented $n$-manifolds, then

$$
\int_N F^*\omega = \int_M \omega
$$

for every compactly supported $\omega \in \Omega^n(M)$; if $F$ reverses orientation the two sides differ by a sign.

**Proof.** The local definition is independent of the chart because of the ordinary change-of-variables formula in $\mathbb{R}^n$: the Jacobian determinant of the transition function multiplies both the coefficient function and the coordinate volume form, and the two factors cancel, the sign being positive precisely for orientation-preserving transitions. The global statement follows by covering and summing. $\square$

### Stokes' Theorem

To state the theorem one needs the induced orientation on the boundary. If $M$ is an oriented $n$-manifold with boundary and $\mathrm{vol}$ is the orientation, the **boundary orientation** on $\partial M$ is defined by the rule that a basis $(v_2, \ldots, v_n)$ of $T_x\partial M$ at a boundary point is positively oriented when $(\nu, v_2, \ldots, v_n)$ is positively oriented in $T_xM$, where $\nu$ is an outward-pointing normal vector; equivalently, the orientation form of the boundary is the contraction of $\mathrm{vol}$ with the outward normal.

**Theorem (Stokes).** Let $M$ be an oriented smooth $n$-manifold with boundary, and let $\omega \in \Omega^{n-1}(M)$ be a form with compact support. Then

$$
\int_M d\omega = \int_{\partial M} \omega,
$$

the boundary carrying the induced orientation.

**Proof.** By a partition of unity it suffices to prove the statement for a form supported in a single chart. In a chart mapping an open set of $M$ to an open set of the half-space $\mathbb{R}^n_+ = \{x^n \geq 0\}$ with the standard orientation, a compactly supported $(n-1)$-form can be written as

$$
\omega = \sum_{j=1}^{n} (-1)^{j-1} f_j\, dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n,
$$

and

$$
d\omega = \sum_{j=1}^{n} \frac{\partial f_j}{\partial x^j}\, dx^1\wedge\cdots\wedge dx^n.
$$

Integrating the $j$-th term over $\mathbb{R}^n_+$ and applying the fundamental theorem of calculus in the $x^j$ variable, the integrals cancel except for the term $j = n$ on the boundary hyperplane $x^n = 0$, where the fundamental theorem gives

$$
\int_{\mathbb{R}^n_+} \frac{\partial f_n}{\partial x^n}\, dx^1\cdots dx^n = -\int_{\mathbb{R}^{n-1}} f_n(x^1, \ldots, x^{n-1}, 0)\, dx^1\cdots dx^{n-1}.
$$

The remaining boundary integral is exactly $\int_{\partial M}\omega$ with the induced orientation: the contraction with the outward normal picks out the $j = n$ term with the sign displayed. Summing over the charts gives the theorem. $\square$

**Remark.** The reason the boundary orientation is fixed to be the one making the fundamental theorem of calculus the source of the theorem is that the sign of $\int_{\partial M}\omega$ must agree with the sign that the calculation produces. With the opposite convention, Stokes' theorem acquires a minus sign.

### The Classical Specialisations

**Theorem (fundamental theorem of calculus).** For $M = [a, b]$ with the standard orientation and a function $f$,

$$
\int_a^b f'(x)\, dx = f(b) - f(a),
$$

which is Stokes' theorem for the $0$-form $f$ and the oriented boundary $\{b\} - \{a\}$.

**Theorem (Green).** Let $D \subseteq \mathbb{R}^2$ be a compact region with smooth positively oriented boundary and let $P, Q \in C^\infty(D)$. Then

$$
\oint_{\partial D} (P\, dx + Q\, dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx\, dy,
$$

which is Stokes' theorem for the $1$-form $\omega = P\,dx + Q\,dy$.

**Theorem (divergence).** Let $D \subseteq \mathbb{R}^3$ be a compact region with smooth boundary and let $X$ be a smooth vector field. Then

$$
\iint_{\partial D} X \cdot \nu\, dS = \iiint_D \operatorname{div} X\, dV,
$$

where $\nu$ is the outward unit normal, which is Stokes' theorem for the $2$-form $\omega = \iota_X(dx\wedge dy\wedge dz)$.

**Theorem (classical Stokes).** Let $S \subseteq \mathbb{R}^3$ be an oriented surface with boundary and let $X$ be a smooth vector field. Then

$$
\oint_{\partial S} X \cdot dr = \iint_S \operatorname{curl} X \cdot \nu\, dS,
$$

which is Stokes' theorem for the $1$-form $\omega = X_1\,dx + X_2\,dy + X_3\,dz$.

## The Hodge Star and the Laplacian

### The Hodge Star

**Definition.** Let $M$ be an oriented Riemannian $n$-manifold with metric $g$ and volume form $\mathrm{vol}_g$, the unique top form of unit length in the orientation. The **Hodge star** is the bundle map $\star : \Lambda^kT^*M \to \Lambda^{n-k}T^*M$ defined by

$$
\alpha \wedge \star\beta = \langle \alpha, \beta\rangle_g\, \mathrm{vol}_g,
$$

where $\langle\cdot,\cdot\rangle_g$ is the metric induced on exterior powers by $g$.

**Proposition.** The Hodge star is an isomorphism of vector bundles, and on $k$-forms

$$
\star\star \alpha = (-1)^{k(n-k)}\, \alpha.
$$

**Proof.** The pairing $\Lambda^k \times \Lambda^{n-k} \to \Lambda^n \cong \mathbb{R}$ is perfect and the metric is positive definite, so the defining relation determines $\star$ uniquely and it is invertible. Evaluating both sides of the defining relation on an oriented orthonormal frame shows that $\star$ sends an orthonormal basis of $\Lambda^k$ to the corresponding orthonormal basis of $\Lambda^{n-k}$ up to the sign of the permutation that reverses the complementary index sets, and iterating gives $(-1)^{k(n-k)}$. $\square$

### The Codifferential and the Laplace–de Rham Operator

**Definition.** The **codifferential** is $\delta = (-1)^{n(k+1)+1}\, \star\, d\, \star$ on $\Omega^k(M)$ (with the sign convention fixed by the requirement that $\delta$ be the formal adjoint of $d$ with respect to the $L^2$ inner product on a compact manifold); the **Laplace–de Rham operator** is

$$
\Delta = d\,\delta + \delta\, d.
$$

**Proposition.** $\delta$ lowers the degree by one, $\delta^2 = 0$, and $\delta$ is the formal adjoint of $d$ for the $L^2$ inner product

$$
\langle\alpha, \beta\rangle_{L^2} = \int_M \langle\alpha, \beta\rangle_g\, \mathrm{vol}_g
$$

on a compact oriented Riemannian manifold. The operator $\Delta$ preserves degree, is self-adjoint, and commutes with $d$ and $\delta$.

**Proof.** The adjoint property is reduced by the definition of $\star$ to the divergence theorem applied to a top form: $\int_M d(\alpha\wedge\star\beta) = \int_{\partial M}\alpha\wedge\star\beta = 0$ for a closed manifold, and the integrand is $\langle d\alpha,\beta\rangle_g - \langle\alpha,\delta\beta\rangle_g$ up to sign. The remaining statements follow by computation from $d^2 = 0$ and the adjointness. $\square$

**Theorem (Hodge).** On a compact oriented Riemannian manifold, every de Rham cohomology class has a unique representative that is harmonic, $\Delta\alpha = 0$, so that

$$
H^k_{dR}(M) \cong \mathcal{H}^k(M) = \{\alpha \in \Omega^k(M) : \Delta\alpha = 0\}.
$$

**Proof sketch.** The Laplace–de Rham operator is elliptic, hence has finite-dimensional kernel on the compact manifold and closed range with an $L^2$-orthogonal decomposition of forms into the harmonic part and the image of $\Delta$; a form is harmonic exactly when it is closed and coclosed, so the harmonic forms represent the cohomology classes, and the ellipticity gives the uniqueness. $\square$

## The Theorem of de Rham

**Theorem (de Rham).** Let $M$ be a smooth manifold. Then there is a natural isomorphism

$$
H^k_{dR}(M) \longrightarrow H^k(M; \mathbb{R})
$$

between the $k$-th de Rham cohomology and the $k$-th singular cohomology of $M$ with real coefficients, natural with respect to smooth maps. Consequently the de Rham cohomology is a homotopy invariant, its dimension is the $k$-th Betti number of $M$ when finite, and a closed form is exact if and only if all its periods over singular cycles vanish.

**Proof sketch.** Integration of a closed $k$-form over a smooth singular $k$-simplex, $\sigma \mapsto \int_\sigma \omega$, is unchanged by a boundary by Stokes' theorem, so it induces a pairing $H^k_{dR}(M) \times H_k(M;\mathbb{R}) \to \mathbb{R}$ and hence a map $H^k_{dR}(M) \to H^k(M;\mathbb{R})$ by the universal coefficient theorem. The map is an isomorphism; the proof uses the Poincaré lemma and the Mayer–Vietoris sequences on both sides, which are isomorphic as functors, and a comparison on contractible open sets. $\square$

**Corollary.** For a compact oriented $n$-manifold the integration pairing $H^k_{dR}(M) \times H^{n-k}_{dR}(M) \to \mathbb{R}$, $([\alpha], [\beta]) \mapsto \int_M \alpha\wedge\beta$, is nondegenerate (Poincaré duality).

## Summary

A differential form of degree $k$ is a smooth section of $\Lambda^k T^*M$; the forms form a graded-commutative algebra under the wedge product, and the pullback along a smooth map is a contravariant algebra homomorphism. The exterior derivative $d$ is the unique degree-one derivation of this algebra with $d^2 = 0$ that agrees with the differential on functions; in coordinates it differentiates the coefficients and wedges with $dx^j$.

The de Rham complex $0 \to \Omega^0 \to \Omega^1 \to \cdots \to \Omega^n \to 0$ has cohomology $H^\bullet_{dR}(M)$, which is contravariantly functorial, homotopy invariant, and satisfies the Mayer–Vietoris sequence; the Poincaré lemma says that on a star-shaped open set the cohomology vanishes in positive degrees.

The integral of a top form on an oriented manifold is defined locally by the ordinary integral of the coefficient function in a positively oriented chart, and it is well defined by the change-of-variables formula. Stokes' theorem, $\int_M d\omega = \int_{\partial M}\omega$, holds for the induced boundary orientation and contains the fundamental theorem of calculus, Green's theorem, the divergence theorem and the classical Stokes theorem as special cases. On an oriented Riemannian manifold the Hodge star, the codifferential $\delta$ and the Laplace–de Rham operator $\Delta = d\delta + \delta d$ give a harmonic representative for each cohomology class, and the theorem of de Rham identifies the de Rham cohomology with the singular cohomology with real coefficients.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M, N$ | Smooth manifolds, possibly with boundary; $n = \dim M$ |
| $T^*M$, $\Lambda^k T^*M$ | Cotangent bundle and its $k$-th exterior power bundle |
| $\Omega^k(M) = \Gamma(\Lambda^kT^*M)$ | Differential $k$-forms; $\Omega^0(M) = C^\infty(M)$ |
| $\Omega^\bullet(M) = \bigoplus_k\Omega^k(M)$ | Graded-commutative algebra of forms; $\Omega^k = 0$ for $k > n$ |
| $\alpha \wedge \beta = (-1)^{pq}\beta\wedge\alpha$ | Wedge product of forms of degrees $p, q$ |
| $F : M \to N$, $F^*\omega$ | Smooth map and the pullback of a form along it; $F^*(d\omega) = d(F^*\omega)$ |
| $d$, $d^2 = 0$ | Exterior derivative; $d(\alpha\wedge\beta) = d\alpha\wedge\beta + (-1)^k\alpha\wedge d\beta$ |
| Closed, exact | $d\omega = 0$; $\omega = d\eta$; exact implies closed |
| $H^k_{dR}(M) = \ker d/\operatorname{im} d$ | de Rham cohomology |
| Poincaré lemma | $H^k_{dR}(U) = 0$ for $k \geq 1$ on a star-shaped open set |
| $\mathrm{vol}$, orientation | Nowhere vanishing top form defining an orientation |
| $\mathbb{R}^n_+ = \{x^n \geq 0\}$ | Closed upper half-space; the local model for a manifold with boundary |
| $\int_M\omega$ | Integral of a compactly supported top form on an oriented manifold |
| $\int_M d\omega = \int_{\partial M}\omega$ | Stokes' theorem; boundary carries the induced orientation |
| $\star$, $\langle\alpha,\beta\rangle_g\mathrm{vol}_g = \alpha\wedge\star\beta$ | Hodge star on an oriented Riemannian manifold |
| $\delta = (-1)^{n(k+1)+1}\star d\star$ | Codifferential; formal adjoint of $d$ |
| $\Delta = d\delta + \delta d$ | Laplace–de Rham operator; harmonic forms represent cohomology |
| $\operatorname{div}$, $\operatorname{curl}$ | Divergence and curl; the classical operators read off from $d$ and $\delta$ |
| $\mathcal{H}^k(M) = \{\alpha : \Delta\alpha = 0\}$ | Harmonic $k$-forms; $\mathcal{H}^k(M) \cong H^k_{dR}(M)$ |
| $H^k_{dR}(M) \cong H^k(M;\mathbb{R})$ | Theorem of de Rham; natural isomorphism with singular cohomology |

## Further Reading

- Michael Spivak, *Calculus on Manifolds* (Benjamin, 1965), for differential forms, the exterior derivative, and Stokes' theorem.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for the de Rham complex, the Poincaré lemma, and the theorem of de Rham.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the de Rham cohomology, Mayer–Vietoris, and the relation to singular cohomology.
- Vladimir A. Zorich, *Mathematical Analysis II* (Springer, 2nd ed. 2016), for Green's theorem, the divergence theorem, and the classical Stokes theorem.
- Georges de Rham, *Differentiable Manifolds: Forms, Currents, Harmonic Forms* (Springer, 1984), for the original development of the de Rham theorems.
- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2nd ed. 2013), for the integration of forms, orientations, and Stokes' theorem with complete proofs.
- Steven Rosenberg, *The Laplacian on a Riemannian Manifold* (Cambridge University Press, 1997), for the Laplace–de Rham operator, the Hodge theorem, and harmonic forms.
