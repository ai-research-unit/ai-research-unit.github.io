
# __Supergeometry__

## Introduction

**Supergeometry** is the geometry of manifolds whose coordinates are of two kinds, the ordinary commuting ones and the **odd** ones that anticommute and square to zero. A **supermanifold** of dimension $(p \mid q)$ is locally modelled on $p$ even coordinates and $q$ odd coordinates, in the same way that a manifold is locally modelled on Euclidean space; the odd coordinates are the generators of a Grassmann algebra, so that a function of them is a polynomial of degree at most $q$ and the whole local model is the tensor product of the smooth functions of the even variables with the exterior algebra on the odd ones. The geometry that results is the natural home of the parity-reversed objects of differential geometry: the parity-reversed tangent bundle $\Pi TM$, whose functions are the differential forms on $M$; the determinant line bundle, replaced by the **Berezinian** line bundle; and the odd vector fields, one of which, the de Rham vector field on $\Pi TM$, encodes the exterior derivative and satisfies $[Q, Q] = 0$.

Two features make the theory more than a formalism. First, the odd directions are nilpotent: an odd coordinate $\xi$ has $\xi^2 = 0$, so a supermanifold has a canonical **body** manifold, obtained by setting the odd coordinates to zero, and every supermanifold is an infinitesimal thickening of its body in the odd directions. Second, the algebraic machinery already exists: the graded algebras, the sign rule, the Lie superalgebras and the Berezinian are the subject of the companion articles *Superalgebras and Graded Structures* and *Grassmann Variables and Berezin Integration*, written in Part I, and the present article lifts that algebra to a manifold theory in the same way that *Smooth Manifolds and Differential Geometry* lifts the algebra of rings of functions to the theory of manifolds. What the geometry adds is the atlas, the partition of unity, the tangent sheaf and the cohomological constructions; what it does not add is analysis, and the integration of a section of the Berezinian line bundle is an algebraic operation — the extraction of a top coefficient — rather than a measure-theoretic one.

This article develops the theory in the concrete form, in which a supermanifold is a smooth manifold of even coordinates with an atlas whose transition functions depend polynomially on the odd coordinates. It defines the structure sheaf of functions, the body manifold and the reduction; it constructs the tangent sheaf of derivations, shows that it is locally free of rank $(p \mid q)$ — the fundamental smoothness theorem of the theory — and gives the parity of the vector fields; it treats the differential forms, the parity-reversal functor $\Pi$ and the identification of the functions on $\Pi TM$ with the differential forms on $M$, including the de Rham vector field; it defines the Berezinian line bundle and the integration over a supermanifold with the change-of-variables formula; and it gives the standard examples: the affine superspace $\mathbb{R}^{p \mid q}$, the superpoint, the odd line, the super circle $S^{1\mid 1}$, the odd tangent bundle $\Pi TM$ and the odd total space $\Pi E$ of a vector bundle. The sheaf-theoretic (Berezin–Leites) form of the definition is equivalent and is stated as such, and the concrete form used here needs no sheaf theory.

The article assumes *Superalgebras and Graded Structures* and *Grassmann Variables and Berezin Integration*, written in Part I, for the sign rule, the bicommutative algebras, the Lie superalgebras, the Berezinian and the odd calculus, which are quoted and not re-derived; *Smooth Manifolds and Differential Geometry* for manifolds, charts, atlases, the tangent bundle and the partition of unity; *Differential Forms and Stokes' Theorem* for the differential forms and the exterior derivative, whose graded version is the model of the whole theory; *Fibre Bundles, Connections and Curvature* for bundles and their associated constructions, of which the odd tangent bundle is an example; and *Dimension Theory*, written in parallel, for the ordinary dimension. The Lie superalgebras, their classification and their representation theory are the subject of *Graded Lie Algebras and Lie Superalgebras*, written in parallel, and the super versions of Teichmüller theory are not developed here. The integral over a supermanifold in the analytic sense, the measure and the functional integral are Part III's; the Berezin integral quoted here is the finite algebraic functional of Part I. No physics is invoked.

## Graded Algebra Recollected

**Definition.** A **super vector space** over a field $K$ of characteristic different from $2$ is a vector space $V = V_0 \oplus V_1$ with a decomposition into an even and an odd part; a homogeneous element $v \in V_{|v|}$ has **parity** $|v| \in \mathbb{Z}/2\mathbb{Z}$. A **superalgebra** is an algebra that is a super vector space with $A_p A_q \subseteq A_{p+q}$, and it is **supercommutative** if $ab = (-1)^{|a||b|}ba$. The **Grassmann algebra** on $q$ odd generators is

$$
\Lambda_q = \Lambda(\xi_1, \ldots, \xi_q) = K[\xi_1,\ldots,\xi_q]/(\xi_i\xi_j + \xi_j\xi_i,\ \xi_i^{\,2}) ,
$$

of dimension $2^q$ over $K$, with basis the monomials $\xi_{i_1}\cdots\xi_{i_k}$ for $i_1 < \cdots < i_k$; it is supercommutative, and $\xi_i^{\,2} = 0$. The algebra is that of *Superalgebras and Graded Structures* and *Grassmann Variables and Berezin Integration*, and its $\mathbb{Z}$-grading by the number of odd generators is the reduction to the $\mathbb{Z}/2$-grading by parity.

**Definition.** A supercommutative superalgebra $A$ is **bicommutative** (or **super-Noetherian, with body**) if it is the tensor product of a commutative algebra with a Grassmann algebra; the **body map** is the algebra homomorphism

$$
\beta : C^\infty(U)\otimes\Lambda_q \longrightarrow C^\infty(U), \qquad \beta(f)(x) = f(x)\ \text{for}\ f\ \text{even in the }\xi\text{, and}\ \beta(\xi_i) = 0 ,
$$

killing the odd generators; its kernel is the nilpotent ideal generated by the odd coordinates, and $A/\ker\beta \cong C^\infty(U)$.

**Proposition.** In a bicommutative superalgebra, every odd element is nilpotent and the ideal of nilpotents is generated by the odd generators; the even part is a commutative algebra but not a domain when $q \geq 1$, since $\xi_{i_1}\cdots\xi_{i_k}$ is a nonzero nilpotent of even parity for $k$ even and nonzero.

## Supermanifolds

### The Concrete Definition

**Definition.** A **supermanifold** of dimension $(p \mid q)$ is a topological space $M$ with an atlas of **supercharts** $(U, \varphi)$ in which $\varphi$ identifies $U$ with an open subset of the affine superspace

$$
\mathbb{R}^{p\mid q} = \mathbb{R}^p \times \mathbb{R}^{0\mid q},
$$

whose algebra of functions is $C^\infty(V) \otimes \Lambda_q$ for $V$ open in $\mathbb{R}^p$ and with an odd coordinate $\xi_j$ for each $j \leq q$; the changes of coordinates have the form

$$
x_i' = g_i(x), \qquad \xi_j' = \sum_{k} a_{jk}(x)\,\xi_k + \sum_{k_1 < k_2} a_{jk_1k_2}(x)\xi_{k_1}\xi_{k_2} + \cdots ,
$$

with the $g_i$ smooth, the coefficients smooth, and the $\xi_j'$ with no constant term; the number $p$ is the **even dimension** and $q$ the **odd dimension**. The **structure sheaf** $\mathcal{O}_M$ assigns to an open set $U$ the supercommutative algebra of functions locally of the form $f(x, \xi) = \sum_I f_I(x)\xi_I$, and the **body** of $M$ is the smooth manifold $M_{\mathrm{red}} = \beta(M)$ of dimension $p$ obtained by killing the odd coordinates; the thickening is along the odd directions, and $\mathcal{O}_M$ is a sheaf of bicommutative superalgebras with body $C^\infty_{M_{\mathrm{red}}}$.

**Remark (the sheaf-theoretic definition).** A supermanifold may equivalently be defined as a pair $(M_{\mathrm{red}}, \mathcal{O})$ of a smooth manifold and a sheaf of supercommutative algebras on it, locally isomorphic to $C^\infty(-)\otimes\Lambda_q$; a **morphism** of supermanifolds is a morphism of the underlying ringed spaces that respects the algebras, and every smooth map of the bodies lifts to a morphism exactly when it is compatible with the odd data. The two definitions are equivalent, and the concrete one is used here because it needs no sheaf theory. The equivalence is standard.

**Example (the basic supermanifolds).**

**(a)** $\mathbb{R}^{p\mid q}$, with the global coordinates $x_1, \ldots, x_p$ even and $\xi_1, \ldots, \xi_q$ odd and the algebra $C^\infty(\mathbb{R}^p)\otimes\Lambda_q$ of global functions.

**(b)** The **superpoint** $\mathbb{R}^{0\mid 1}$, whose algebra of functions is $\Lambda_1 = K[\xi]/(\xi^2)$, the dual numbers of the corpus; it is the one-point space with a nilpotent, and it is the local model of an odd direction.

**(c)** The **odd line** $\mathbb{R}^{1\mid 1}$ with one even and one odd coordinate; a function is $f(x) + g(x)\xi$.

**(d)** The **super circle** $S^{1\mid 1}$, obtained from even and odd coordinates $(t, \xi)$ with $t$ modulo $1$ and $\xi$ odd, with the transition $\xi \mapsto \pm\xi$ according to the orientation; it is the simplest closed supermanifold and the base of the standard super-Teichmüller theory of the companion article.

**(e)** Any smooth manifold $M$ of dimension $p$, read as a supermanifold of dimension $(p \mid 0)$: the supermanifolds of odd dimension zero are exactly the smooth manifolds.

**(f)** $\mathbb{R}^{p\mid q}$ with the algebra $C^\infty(\mathbb{R}^p)\otimes\Lambda_q$ is the total space of the trivial super vector bundle of rank $(0 \mid q)$ over $\mathbb{R}^p$. Such a supermanifold, whose structure sheaf is the exterior algebra of a vector bundle over the body, is called **split**; by Batchelor's theorem every smooth supermanifold is diffeomorphic to a split one, but the splitting is not canonical, so the odd data are strictly finer than the body together with a vector bundle.

### The Tangent Sheaf

**Definition.** A **vector field** on a supermanifold $M$ is a **superderivation** of the structure sheaf, that is, a $K$-linear map $X : \mathcal{O}_M \to \mathcal{O}_M$ with

$$
X(fg) = X(f)g + (-1)^{|X||f|}f\,X(g)
$$

for homogeneous $f, g$; the **tangent sheaf** $\mathcal{T}_M$ is the sheaf of vector fields, graded by parity, and the **tangent space** at a point is the graded vector space of the derivations evaluated at the point, of dimension $(p \mid q)$ as a super vector space.

**Theorem (smoothness).** The tangent sheaf of a supermanifold is locally free over the structure sheaf, of rank $(p \mid q)$; a local frame in a superchart is

$$
\partial_{x_1}, \ldots, \partial_{x_p}, \ \partial_{\xi_1}, \ldots, \partial_{\xi_q},
$$

with the $x$-derivatives even and the $\xi$-derivatives odd, and the derivatives with respect to the odd coordinates are the left derivatives of *Grassmann Variables and Berezin Integration*. Hence a supermanifold is **smooth** in the graded sense, and every vector field is locally $X = \sum_i f_i\,\partial_{x_i} + \sum_j g_j\,\partial_{\xi_j}$ with the appropriate parities.

**Proof sketch.** The chain rule in the super setting gives the transformation of the frame under a change of supercoordinates, and the invertibility of the transformation matrix on the even part (the Jacobian of the body diffeomorphism, which is invertible) together with the triangular form of the odd-odd block shows that the frame is a basis of the module of derivations; the local freeness follows. $\square$

**Theorem (the Lie superalgebra of vector fields).** The tangent sheaf with the **superbracket**

$$
[X, Y] = XY - (-1)^{|X||Y|}YX
$$

is a sheaf of Lie superalgebras: the bracket is super anticommutative, $[X,Y] = -(-1)^{|X||Y|}[Y,X]$, and satisfies the super Jacobi identity. On a supermanifold of dimension $(p \mid q)$ the bracket of two odd fields is even and may be nonzero, in contrast with the commuting case.

**Proof sketch.** The bracket of two derivations of an associative superalgebra is a derivation, and the verification of the super Jacobi identity is the graded form of the ordinary computation; the statement is that of *Superalgebras and Graded Structures* applied to the sheaf of superalgebras. $\square$

**Example (odd vector fields and the de Rham differential).** Let $M$ be a smooth manifold of dimension $p$ and let $\Pi TM$ be its **odd tangent bundle**, the supermanifold of dimension $(p \mid p)$ whose odd coordinates are the differentials $dx_i$ of the even coordinates. The functions on $\Pi TM$ are the differential forms on $M$,

$$
\mathcal{O}_{\Pi TM} \cong \Omega^\bullet(M) = C^\infty(M)\otimes\Lambda(dx_1, \ldots, dx_p) ,
$$

and the exterior derivative $d$ is the odd vector field

$$
Q = \sum_i dx_i\,\frac{\partial}{\partial x_i},
$$

which is odd because $dx_i$ and $\partial_{x_i}$ are odd and even respectively; the relation $d^2 = 0$, equivalently $[Q,Q] = 0$, is the integrability of the odd field, and the cohomology of $Q$ is the de Rham cohomology of $M$. This is the fundamental example of a supermanifold that is not a manifold, and it identifies the differential forms of *Differential Forms and Stokes' Theorem* with the functions on an odd manifold.

## Differential Forms and the Berezinian

### Forms on a Supermanifold

**Definition.** The **differential forms** on a supermanifold $M$ are the sections of the exterior algebra of the cotangent sheaf, $\Omega^\bullet(M) = \Lambda_{\mathcal{O}_M}(\Omega^1_M)$ with $\Omega^1_M = \mathcal{T}_M^\vee$ the dual of the tangent sheaf, graded by the total degree and by parity; the **super exterior derivative** is the odd derivation

$$
d : \Omega^k(M) \to \Omega^{k+1}(M), \qquad d(f\,d\alpha_1\cdots d\alpha_k) = df\, d\alpha_1\cdots d\alpha_k ,
$$

characterised by $d^2 = 0$, the super Leibniz rule and $d(f) = df$ on functions; in a superchart the coordinates $x_i$ even and $\xi_j$ odd give the forms $dx_i$ of odd total degree and $d\xi_j$ of even total degree.

**Theorem (functoriality).** The assignment $M \mapsto \Omega^\bullet(M)$ is a functor to the category of differential graded superalgebras: a morphism of supermanifolds pulls back forms, $d$ commutes with the pullback, and the super Leibniz rule holds with the Koszul sign. The degree-zero part is the structure sheaf, and the degree-one part the cotangent sheaf; the complex $(\Omega^\bullet(M), d)$ is the graded version of the de Rham complex of *Differential Forms and Stokes' Theorem*, and its cohomology is the de Rham cohomology of the supermanifold.

**Proof sketch.** The pullback of a derivation is a derivation with the opposite variance, the dual sheaf is functorial, and the compatibility of $d$ with pullback is the chain rule in the super setting; the differential graded structure is the one of *Superalgebras and Graded Structures*. $\square$

### The Berezinian and Integration

**Definition.** Let $M$ be a supermanifold of dimension $(p \mid q)$ with cotangent sheaf $\Omega^1_M$ of rank $(p \mid q)$. The **Berezinian line bundle** is the $\mathbb{Z}/2$-graded line bundle

$$
\operatorname{Ber}(M) = \Lambda^{\text{top}}\Omega^1_{M,\bar 0}\otimes \bigl(\Lambda^{\text{top}}\Omega^1_{M,\bar 1}\bigr)^{\!\vee} ,
$$

the top exterior power of the even part of the cotangent sheaf twisted by the dual of the top exterior power of the odd part, with a parity shift by $q$; its transition functions are the **Berezinian** of the Jacobian of the change of supercoordinates, the multiplicative super determinant of *Superalgebras and Graded Structures*,

$$
\operatorname{Ber}(X) = \det(A - B D^{-1} C)\,\det(D)^{-1} \quad \text{for } X = \begin{pmatrix} A & B \\ C & D \end{pmatrix},
$$

with $A$ the even-even, $B$ the even-odd, $C$ the odd-even and $D$ the odd-odd block, the formula applied when the matrices are invertible. For a smooth manifold read in odd dimension zero the Berezinian is the determinant line bundle $\Lambda^{\text{top}}T^*M$, so it is the graded generalisation of the canonical bundle.

**Theorem (integration and change of variables).** A section of the Berezinian line bundle with compact support on a supermanifold of dimension $(p \mid q)$ has a well-defined integral

$$
\int_M s = \int_{M_{\mathrm{red}}}\Bigl(\text{the coefficient of } dx_1\cdots dx_p\, d\xi_1\cdots d\xi_q \text{ in } s\Bigr),
$$

computed in a superchart and independent of the chart, where the even part is integrated over the body and the odd part is integrated by the Berezin rule. Under a change of supercoordinates, with $J = \partial(x', \xi')/\partial(x, \xi)$ the Jacobian of the change from the coordinates $(x, \xi)$ to the coordinates $(x', \xi')$, the Berezinian measures are related by

$$
dx\,d\xi = \operatorname{Ber}(J)^{-1}\,dx'\,d\xi' ,
$$

the inverse Berezinian appearing, exactly as the inverse determinant appears in the purely odd change of variables of *Grassmann Variables and Berezin Integration* and the inverse Jacobian in the ordinary change of variables of the even part. The integral is a finite algebraic operation — the extraction of a top coefficient — and agrees with the Berezin integral on each chart.

**Proof sketch.** The transformation of the odd part is the change-of-variables formula of the odd calculus, and the even part contributes the ordinary Jacobian determinant, the two combining into the Berezinian; the independence of the chart is the multiplicativity of the Berezinian, $\operatorname{Ber}(XY) = \operatorname{Ber}(X)\operatorname{Ber}(Y)$, on the overlaps of the atlas; the agreement with the Berezin integral is the computation of the top coefficient in the odd variables. $\square$

**Example (the integration of a super form).** On $\mathbb{R}^{1\mid 1}$ with the coordinates $(x, \xi)$ a section of the Berezinian is $f(x) + g(x)\xi$ times $dx\,d\xi$, and

$$
\int_{\mathbb{R}^{1\mid 1}} (f(x) + g(x)\xi)\,dx\,d\xi = \int_{\mathbb{R}} g(x)\,dx ,
$$

the even part of the coefficient; this is the shape of every superspace integral, and it shows why the odd coordinate contributes the coefficient of $\xi$ and the even coordinate the ordinary integral. The ordinary integral enters here as the classical counterpart, exactly as in *Grassmann Variables and Berezin Integration*.

## The Parity Reversal and the Examples

**Definition.** The **parity reversal** $\Pi$ associates to a super vector space $V = V_0\oplus V_1$ the super vector space $\Pi V$ with $(\Pi V)_0 = V_1$ and $(\Pi V)_1 = V_0$; on a vector bundle $E$ over a manifold the same construction gives the **odd bundle** $\Pi E$, and on a manifold the **odd tangent bundle** $\Pi TM$ and the **odd cotangent bundle** $\Pi T^*M$ are the principal examples.

**Theorem (the odd tangent bundle).** For a smooth manifold $M$ of dimension $p$, the odd tangent bundle $\Pi TM$ is a supermanifold of dimension $(p \mid p)$ whose algebra of functions is the algebra of differential forms, $\mathcal{O}_{\Pi TM} = \Omega^\bullet(M)$; each differential form on $M$ is a function on $\Pi TM$, and the exterior derivative is an odd vector field $Q$ with $[Q, Q] = 0$. The same construction for a vector bundle $E$ of rank $r$ gives a supermanifold $\Pi E$ of dimension $(p \mid r)$ whose functions are the sections of $\Lambda E^*$, and the Berezinian line bundle of $\Pi E$ is computed from the determinant lines of $E$ and of the body.

**Proof sketch.** A function on $\Pi TM$ is locally a polynomial in the odd coordinates $dx_i$ with coefficients functions on $M$, which is a differential form, and the parity of $dx_i$ is odd; the odd vector field $Q = \sum_i dx_i\,\partial_{x_i}$ realises the exterior derivative, and $Q^2 = 0$ as an operator is $d^2 = 0$, equivalently $[Q,Q] = 0$ since $Q$ is odd. For the bundle case the same computation is applied fibrewise, and the Berezinian follows from the rank count of the cotangent sheaf of $\Pi E$, of rank $(p\mid r)$. $\square$

**Example (the odd total space and the classical structure).** For $E = TM$ the manifold $\Pi E$ is $\Pi TM$ and the functions are the forms; for $E$ the trivial bundle of rank $r$ over a point, $\Pi E = \mathbb{R}^{0\mid r}$ is the odd affine space. The construction $\Pi$ is the identity on the underlying body and reverses the parity of the fibres, so $\Pi\Pi E = E$ up to the canonical identification; the odd bundles are the objects on which the odd vector fields of the theory naturally live, and the Berezinian line bundle of $\Pi E$ is the determinant line bundle of $E$ raised to the appropriate power.

**Remark (the supermanifolds that arise in the corpus).** The super circle $S^{1\mid 1}$, the odd tangent bundle $\Pi TM$, the odd total space $\Pi E$ of a vector bundle and the superspaces $\mathbb{R}^{p\mid q}$ exhaust the supermanifolds used in the corpus. The supermanifolds associated with a Lie superalgebra, on which the Lie superalgebra acts by vector fields, are the graded analogues of the homogeneous spaces of *Homogeneous Spaces* and are treated with the Lie superalgebras of *Graded Lie Algebras and Lie Superalgebras*, written in parallel; the super Riemann surfaces, which are supermanifolds of dimension $(1\mid 1)$ with a distribution, and their moduli, are not developed here.

**Remark (the bundles and the connections).** A **super vector bundle** over a supermanifold is a sheaf of locally free $\mathcal{O}_M$-modules of graded rank $(r\mid s)$; the tangent sheaf, the cotangent sheaf and the Berezinian sheaf are the basic examples, and the associated bundle constructions of *Fibre Bundles, Connections and Curvature* carry over verbatim with the Koszul sign rule inserted wherever two odd objects change places. A **connection** on a super vector bundle is a $K$-linear map $\nabla : \Gamma(E) \to \Gamma(T^*M\otimes E)$ with the super Leibniz rule, and the curvature is the commutator of the covariant derivatives; the graded Bianchi identity and the graded Chern–Weil construction follow, and the characteristic classes so obtained are the superclasses of the graded bundles. The development is that of the connection theory of *Fibre Bundles, Connections and Curvature* read with the signs of *Superalgebras and Graded Structures*, and the super characteristic classes are quoted there as the graded version of the ordinary ones.

**Remark (what is deferred).** The structures that need analysis are deferred. The integral over a supermanifold is the algebraic Berezin integral of Part I, a finite coefficient extraction; the **Berezin measure** as a measure, the distributions, the super Fourier transform, the heat kernel on a supermanifold and the functional integration are Part III's, where the measure and the integral are available, and the analytic index theorem for the graded elliptic complexes is the graded form of the index theory of *The Atiyah–Singer Index Theorem and K-Theory*. The homological algebra of the supermanifolds, the derived categories of the graded sheaves and the cohomology of the graded structures belong to the sheaf theory and the homological algebra of the corpus, and the language of sheaves is deliberately not used in this article.

## Summary

Graded algebra provides a $\mathbb{Z}/2$-grading, the Koszul sign rule and the Grassmann algebra on odd generators, with the bicommutative algebras and the Berezinian as its main structures; a supermanifold of dimension $(p\mid q)$ is a topological space with an atlas modelled on $\mathbb{R}^p$ with $q$ odd coordinates, whose structure sheaf is locally $C^\infty(U)\otimes\Lambda_q$. The odd coordinates are nilpotent, so a supermanifold has a body manifold of dimension $p$ obtained by killing the odd directions, and it is an infinitesimal thickening of its body; the sheaf-theoretic (Berezin–Leites) definition is equivalent to the concrete one and is stated but not used.

The tangent sheaf is the sheaf of superderivations of the structure sheaf, locally free of rank $(p\mid q)$ — the smoothness theorem — with an even and an odd part; the vector fields form a sheaf of Lie superalgebras under the superbracket $[X,Y] = XY - (-1)^{|X||Y|}YX$. The differential forms are the exterior algebra of the cotangent sheaf, with the super exterior derivative and the graded de Rham complex; the parity-reversal functor $\Pi$ turns the tangent bundle into the odd tangent bundle $\Pi TM$ of dimension $(p\mid p)$, whose functions are the differential forms on $M$ and whose odd vector field $Q = \sum_i dx_i\,\partial_{x_i}$ encodes the exterior derivative with $[Q,Q] = 0$. The Berezinian line bundle generalises the determinant line bundle, with transition functions the Berezinian $\operatorname{Ber}(X) = \det(A - BD^{-1}C)\det(D)^{-1}$ of the Jacobian, and the integration of a compactly supported section is a finite algebraic operation, with the measure transforming by the inverse Berezinian of the Jacobian; the super vector bundles, connections and characteristic classes are the graded versions of the ordinary theory, and the analytic aspects — the Berezin measure, the heat kernel and the functional integral — belong to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V = V_0\oplus V_1$, $\vert v\vert$ | Super vector space with even and odd parts; parity |
| $ab = (-1)^{\vert a\vert\vert b\vert}ba$ | Supercommutativity |
| $\Lambda_q = \Lambda(\xi_1,\ldots,\xi_q)$ | Grassmann algebra on $q$ odd generators; $\xi_i^2 = 0$ |
| $\beta$ | Body map; kills the odd coordinates |
| $M$, $\dim = (p\mid q)$ | Supermanifold; even and odd dimension |
| $M_{\mathrm{red}}$ | Body manifold, of dimension $p$ |
| $\mathcal{O}_M$ | Structure sheaf; locally $C^\infty(U)\otimes\Lambda_q$ |
| $\mathcal{T}_M$ | Tangent sheaf of superderivations; locally free of rank $(p\mid q)$ |
| $\partial_{x_i}$, $\partial_{\xi_j}$ | Even and odd frame of the tangent sheaf |
| $[X,Y] = XY - (-1)^{\vert X\vert\vert Y\vert}YX$ | Superbracket; Lie superalgebra of vector fields |
| $\Omega^\bullet(M)$, $d$ | Differential forms; super exterior derivative, $d^2 = 0$ |
| $\Pi E$, $\Pi TM$ | Parity reversal; odd bundle, odd tangent bundle |
| $Q = \sum_i dx_i\,\partial_{x_i}$ | de Rham odd vector field; $[Q,Q] = 0$ |
| $\operatorname{Ber}(M)$ | Berezinian line bundle; graded determinant line |
| $\operatorname{Ber}(X) = \det(A-BD^{-1}C)\det(D)^{-1}$ | Berezinian of an even supermatrix |
| $\int_M s$ | Integration of a Berezinian section; top-coefficient extraction |

## Further Reading

- F. A. Berezin, *Introduction to Superanalysis* (Reidel, 1987), for the Grassmann calculus, the Berezinian and the supermanifold.
- D. A. Leites, "Introduction to the theory of supermanifolds", *Russian Mathematical Surveys* 35 (1980), 1–64, for the sheaf-theoretic definition and the fundamental results.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, 2nd edition, 1997), for the supermanifolds, the Berezinian and the complex supergeometry.
- V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction* (American Mathematical Society, 2004), for the graded algebra, the Berezinian and the supermanifolds.
- Marjorie Batchelor, "The structure of supermanifolds", *Transactions of the American Mathematical Society* 253 (1979), 329–338, for the splitting theorem: every smooth supermanifold is diffeomorphic to a split one.
- Pierre Deligne and John Morgan, "Notes on supersymmetry (following Joseph Bernstein)", in *Quantum Fields and Strings: A Course for Mathematicians* (American Mathematical Society, 1999), for the algebro-geometric supergeometry, the odd tangent bundle and the Berezinian.
- A. Rogers, "A global theory of supermanifolds", *Journal of Mathematical Physics* 21 (1980), 1352–1365, for the concrete (Rogers) supermanifolds and their global theory.
