
# __Characteristic Classes__

## Introduction

A characteristic class of a vector bundle is a cohomology class of the base that measures the twisting of the bundle: it is natural under the pullback of bundles, it vanishes on the trivial bundles in positive degree, and it is compatible with the Whitney sum. The **Chern–Weil** construction of *Fibre Bundles, Connections and Curvature* produces such classes from the curvature of a connection, and it proves the fundamental fact that the classes it produces depend only on the bundle and not on the connection; the present article completes the thread by developing the classes themselves. There are four families: the **Stiefel–Whitney** classes $w_i(E) \in H^i(B;\mathbb{Z}/2)$ of a real bundle, the **Chern** classes $c_i(E) \in H^{2i}(B;\mathbb{Z})$ of a complex bundle, the **Pontryagin** classes $p_i(E) \in H^{4i}(B;\mathbb{Z})$ of a real bundle, and the **Euler** class $e(E) \in H^n(B;\mathbb{Z})$ of an oriented real bundle of rank $n$; the Chern–Weil forms of the companion article are the images of the Chern, Pontryagin and Euler classes in the real cohomology, and the Stiefel–Whitney classes and the integral lifts of the classes are the genuinely topological part of the theory, invisible to the curvature.

The article is organised around the two ways of defining the classes and the theorem that they agree. The first way is **axiomatic**: the naturality, the vanishing on trivial bundles and the Whitney sum formula determine the classes uniquely, and the totality of the classes is the cohomology of the **classifying space**, the Grassmannian $BO(n)$ in the real case and $BU(n)$ in the complex case, whose cohomology rings are polynomial algebras on the universal classes. The second way is **geometric**: the Chern–Weil construction from the curvature, which *Fibre Bundles, Connections and Curvature*, earlier in this Part, carries out and which this article develops. The two ways meet in the equality of the Chern–Weil forms with the real images of the Chern and Pontryagin classes; the equality is the content of the normalisation by the factors of $2\pi i$, and it is the reason the Chern–Weil theory computes the topological invariants from the geometry of a connection. The article closes with the relations among the classes, the splitting principle, the characteristic numbers and the cobordism invariants, the signature theorem of Hirzebruch, and the link to the index theory of this Part, which is where the characteristic numbers of the spin manifolds, are computed.

The cohomology used is the singular cohomology with the standard coefficients, cited from the literature (Hatcher, Chapter 3), and the de Rham theory of *Differential Forms and Stokes' Theorem*; the Chern–Weil forms of *Fibre Bundles, Connections and Curvature*, earlier in this Part, are the bridge between the two. The general theory of the classifying space, its construction and the Eilenberg–MacLane spaces are those; only the Grassmannian models $BO(n)$ and $BU(n)$ of the present article are used below.

## The Axiomatic Theory and the Classifying Spaces

### Characteristic Classes and Naturality

**Definition.** Let $\mathbf{Vect}_n^{\mathbb{K}}(B)$ be the set of isomorphism classes of rank-$n$ vector bundles over the topological space $B$, over the field $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the pullback operations of *Fibre Bundles, Connections and Curvature*. A **characteristic class** of degree $i$ with coefficients in the ring $A$ is a natural transformation
$$
\kappa : \mathbf{Vect}_n^{\mathbb{K}}(-) \longrightarrow H^i(-;A),
$$
that is, an assignment to each bundle $E \to B$ of a class $\kappa(E) \in H^i(B;A)$ such that $\kappa(f^*E) = f^*\kappa(E)$ for every continuous map $f$; the class is **normalised** if it vanishes on the trivial bundles in every positive degree. A characteristic class is called **stable** if it is defined for the bundles of all ranks and is unchanged by the addition of a trivial summand.

**Definition.** The **total characteristic class** of a bundle is the class $1 + \kappa_1(E) + \kappa_2(E) + \cdots$ in the direct sum of the groups $H^i(B;A)$, written multiplicatively; a family of classes is **multiplicative** if the total class satisfies the **Whitney sum formula**
$$
\kappa(E \oplus F) = \kappa(E)\,\kappa(F)
$$
for all bundles $E$ and $F$ over the same base, the product being the cup product of the total classes.

**Theorem (classification of the characteristic classes).** For the complex bundles the graded ring of the stable characteristic classes with coefficients in $A$ is the polynomial ring $A[c_1, c_2, \ldots]$ on the **Chern classes** $c_i$ of degree $2i$; for the real bundles, the ring of the stable characteristic classes with coefficients in $\mathbb{Z}/2$ is the polynomial ring $\mathbb{Z}/2[w_1, w_2, \ldots]$ on the **Stiefel–Whitney classes** $w_i$ of degree $i$, and with coefficients in a ring in which $2$ is invertible the ring is generated by the **Pontryagin classes** $p_i$ of degree $4i$, together with the Euler class in the oriented even-rank case subject to the relation $e^2 = p_n$. The polynomial rings are the cohomology rings
$$
H^*(BO(n);\mathbb{Z}/2) = \mathbb{Z}/2[w_1, \ldots, w_n], \qquad H^*(BU(n);\mathbb{Z}) = \mathbb{Z}[c_1, \ldots, c_n],
$$
of the **classifying spaces**, and the classes are the pullbacks of the universal classes along the classifying maps of the bundles.

**Proof sketch.** A vector bundle of rank $n$ over a paracompact base is classified by a map $f : B \to BO(n)$ or $B \to BU(n)$, unique up to homotopy, and the classification is the pullback of the universal bundle; by the naturality of the characteristic classes, the characteristic classes of the bundle are exactly the pullbacks of the classes in the cohomology of the classifying space, and the degree-$i$ classes are the natural transformations $H^i(BG;A) \to H^i(-;A)$, which by the Yoneda lemma are the elements of $H^i(BG;A)$ itself. The cohomology rings of the classifying spaces are computed from the cell structures of the Grassmannians of the planes in $\mathbb{R}^\infty$ and $\mathbb{C}^\infty$, the Schubert cells giving the polynomial generators and the splitting principle of the next section giving the multiplicativity. The details are in the references. $\square$

**Remark.** The Chern–Weil construction of *Fibre Bundles, Connections and Curvature* produces, from an invariant polynomial $f$ and the curvature $\Omega$ of a connection on a principal bundle, a closed form $f(\Omega)$ whose de Rham class is independent of the connection. The comparison with the present theory is the statement that the Chern–Weil classes are the images of the integral Chern and Pontryagin classes in the real or complex cohomology under the coefficient map: the invariant polynomial $f(\xi) = \operatorname{tr}(\exp(\frac{i}{2\pi}\xi))$ gives the total Chern class, the polynomial $\det(I + \frac{R}{2\pi})$ the Chern classes of a complex bundle, the polynomials $\operatorname{tr}((\frac{R}{2\pi})^{2j})$ the Pontryagin classes up to the sign $(-1)^j$, and the Pfaffian $\operatorname{Pf}(\frac{R}{2\pi})$ the Euler class. The companion article states the Chern–Weil homomorphism and the independence of the connection, and the present article takes the comparison as the geometric realisation of the classes defined here; the proof that the Chern–Weil classes are the topological classes is the "Chern–Weil to Chern" comparison of the references.

### The Classifying Spaces and the Universal Bundles

**Definition.** The **classifying space** $BO(n)$ of the rank-$n$ real bundles is the Grassmannian of the $n$-planes in $\mathbb{R}^\infty$, the direct limit of the Grassmannians $G_n(\mathbb{R}^{n+k})$ of the $n$-planes in $\mathbb{R}^{n+k}$ under the standard inclusions, with the **universal bundle** $EO(n) \to BO(n)$ whose fibre over a plane is the plane itself; the complex case is the same with $\mathbb{C}$ in place of $\mathbb{R}$ and $BU(n)$ in place of $BO(n)$. The **universal classes** are the characteristic classes of the universal bundle,
$$
w_i = w_i(EO(n) \to BO(n)), \qquad c_i = c_i(EU(n) \to BU(n)), \qquad p_i = p_i(EO(n) \to BO(n)),
$$
and every characteristic class of a bundle $E$ over $B$ with classifying map $f$ is the pullback $f^*$ of a universal class.

**Proposition.** The cohomology of the classifying spaces is
$$
H^*(BO(n);\mathbb{Z}/2) = \mathbb{Z}/2[w_1,\ldots,w_n], \qquad H^*(BU(n);\mathbb{Z}) = \mathbb{Z}[c_1,\ldots,c_n],
$$
and in the real case with integral coefficients mod torsion the Pontryagin classes generate the polynomial ring $\mathbb{Q}[p_1, p_2, \ldots]$ in the stable range; the Euler class $e$ of the oriented universal bundle is the top class of the oriented case, and it satisfies $e^2 = p_n$ for the oriented rank-$2n$ bundles and $e = w_n$ modulo $2$ in general.

**Proof sketch.** The cohomology of the Grassmannian $G_n(\mathbb{R}^{n+k})$ is computed from its Schubert cell decomposition, whose cells are indexed by the partitions in the $n \times k$ rectangle, and the classes of the Schubert cells are the monomials of degree at most $n$ in the Stiefel–Whitney classes; passing to the limit $k \to \infty$ gives the polynomial ring. The complex case is the same with the Schubert cells of the complex Grassmannian, whose integral cohomology is the polynomial ring on the Chern classes; the relations $e^2 = p_n$ and $e = w_n \bmod 2$ are the computations of the top classes, and they are standard. The details are in the references. $\square$

## The Four Families of Classes

### The Stiefel–Whitney Classes

**Definition.** The **Stiefel–Whitney classes** of a real vector bundle $E \to B$ are the classes $w_i(E) \in H^i(B;\mathbb{Z}/2)$ defined by the pullback of the universal classes, with the total class $w(E) = 1 + w_1(E) + w_2(E) + \cdots$; they are characterised by the axioms: $w_0 = 1$; $w_1(E) = 0$ if and only if $E$ is orientable; $w(E \oplus F) = w(E)w(F)$; and the naturality $w(f^*E) = f^*w(E)$.

**Theorem.** The Stiefel–Whitney classes are determined by the axioms, and they are the unique family satisfying the normalisation $w_1(\gamma) \neq 0$ for the tautological line bundle $\gamma$ over $\mathbb{RP}^\infty$; the top class $w_n(E)$ of a rank-$n$ bundle is the mod-$2$ reduction of the Euler class in the oriented case, $w_n(E) = e(E) \bmod 2$, and $w_{n}$ is the primary obstruction to a nowhere-zero section of $E$; the first class $w_1$ is the obstruction to the orientation and the second class $w_2$ is the obstruction to the spin structure, which exists precisely when $w_2(TM) = 0$ for a Riemannian manifold.

**Example.** The total Stiefel–Whitney class of the tangent bundle of the real projective space is $w(T\mathbb{RP}^n) = (1+a)^{n+1}$ with $a$ the generator of $H^1(\mathbb{RP}^n;\mathbb{Z}/2)$; hence $w_1(T\mathbb{RP}^n) = (n+1)a$, which vanishes exactly when $n$ is odd, the orientability of the projective space, and $w_2(T\mathbb{RP}^n) = \binom{n+1}{2}a^2$, which vanishes exactly when $n \equiv 3 \pmod 4$, the spin condition. The total Stiefel–Whitney class of the tangent bundle of the sphere $S^n$ is $1$, since the sphere is stably parallelisable, and the tangent bundle of a compact surface is trivial if and only if the surface is the torus.

### The Chern Classes

**Definition.** The **Chern classes** of a complex vector bundle $E \to B$ are the classes $c_i(E) \in H^{2i}(B;\mathbb{Z})$ given by the pullback of the universal classes, with the total class $c(E) = 1 + c_1(E) + \cdots$; they are characterised by the axioms: $c_0 = 1$; $c_1(\gamma) = -x$ for the tautological line bundle over $\mathbb{CP}^\infty$ with $x$ the hyperplane class; $c(E \oplus F) = c(E)c(F)$; and the naturality. The **Chern character** is the ring homomorphism
$$
\operatorname{ch} : K^0(B) \longrightarrow H^{\mathrm{ev}}(B;\mathbb{Q}), \qquad \operatorname{ch}(E) = \sum_{i=1}^{n} e^{x_i} = \operatorname{rk}(E) + c_1(E) + \tfrac12\bigl(c_1(E)^2 - 2c_2(E)\bigr) + \cdots ,
$$
defined on the Grothendieck group of the bundles of *Topological K-Theory*, where the $x_i$ are the Chern roots of $E$; it is a homomorphism with respect to the tensor product, and after tensoring the $K$-theory with $\mathbb{Q}$ it becomes an isomorphism onto the even cohomology, the **Chern character isomorphism**.

**Theorem.** The Chern classes are determined by the axioms; for the tautological line bundles and the splitting principle of the next section the total class of a direct sum is the product, and the Chern classes of the tangent bundle of the complex projective space are
$$
c(T\mathbb{CP}^n) = (1 + x)^{n+1},
$$
with $x$ the hyperplane class, so that $c_1(T\mathbb{CP}^n) = (n+1)x$ and the top class is $c_n = (n+1)x^n$; the Chern classes of a complex manifold are the classes of its tangent bundle, and they are the topological data that the Riemann–Roch and the Atiyah–Singer theorems convert into the analytic invariants.

**Example.** For the tautological line bundle $O(-1)$ over $\mathbb{CP}^n$ one has $c_1(O(-1)) = -x$, and for the dual $O(1)$ one has $c_1 = x$; the tangent bundle of the projective space is the quotient of the trivial bundle by the tautological line bundle, and its Chern classes are $c(T\mathbb{CP}^n) = (1+x)^{n+1}$ with the identity $c_1 = (n+1)x$ consistent with the Euler sequence $0 \to O \to O(1)^{\oplus(n+1)} \to T\mathbb{CP}^n \to 0$. The Chern classes of the complex Grassmannians are computed by the same splitting, and they are the Schur polynomials in the Chern classes of the tautological bundle.

### The Pontryagin Classes and the Euler Class

**Definition.** The **Pontryagin classes** of a real vector bundle $E$ are the classes
$$
p_i(E) = (-1)^i\, c_{2i}(E \otimes_{\mathbb{R}} \mathbb{C}) \in H^{4i}(B;\mathbb{Z}),
$$
the Chern classes of the complexification, with the sign chosen so that the classes are the curvature classes of the companion article; the total class is $p(E) = 1 + p_1(E) + p_2(E) + \cdots$. The **Euler class** of an oriented real bundle $E \to B$ of rank $n$ is the class $e(E) \in H^n(B;\mathbb{Z})$ whose mod-$2$ reduction is the top Stiefel–Whitney class and whose de Rham image is the Pfaffian of the curvature, $e(E) = [\operatorname{Pf}(\frac{R}{2\pi})]$ in the Chern–Weil theory; for an oriented bundle the Euler class is the primary obstruction to a nowhere-zero section, and $e(E) = 0$ if and only if the bundle admits a nowhere-zero section when the base is a complex of dimension at most $n$.

**Theorem (the relations).** The four families satisfy the following relations:
$$
p_i(E) \equiv w_{2i}(E)^2 \pmod 2, \qquad e(E) \equiv w_n(E) \pmod 2,
$$
for a real bundle $E$, the congruence being in $H^{4i}(B;\mathbb{Z}/2)$ and $H^n(B;\mathbb{Z}/2)$; for a complex bundle $E$ with conjugate $\bar E$ the complexified real bundle satisfies
$$
p(E_{\mathbb{R}}) = c(E)\,c(\bar E),
$$
so that the Pontryagin classes of a complex bundle are the polynomials $\sum_{i+j=2k}(-1)^i c_i c_j$ in the Chern classes; and the Euler class is multiplicative, $e(E \oplus F) = e(E)e(F)$, for the oriented bundles. The Wu formula relates the Steenrod squares of the Stiefel–Whitney classes to the classes themselves, and it determines the Stiefel–Whitney classes from the cohomology ring in the presence of the operations.

**Proof sketch.** The congruences follow from the definitions and the Whitney sum: the complexification of a real bundle satisfies $E \otimes \mathbb{C} \cong E \oplus E$ as a bundle with the conjugate structure, and the Chern classes of the complexification reduce modulo $2$ to the squares of the Stiefel–Whitney classes; the Euler congruence is the comparison of the two obstructions to a nowhere-zero section, both of which live in degree $n$. The formula $p(E_{\mathbb{R}}) = c(E)c(\bar E)$ is the Whitney sum $E_{\mathbb{R}} \otimes \mathbb{C} \cong E \oplus \bar E$ together with the definition of the Pontryagin classes. The Wu formula is the algebraic computation of the Steenrod squares on the Stiefel–Whitney classes; it is standard and it is in the references. $\square$

**Theorem (Hirzebruch; the signature theorem).** Let $M$ be a closed oriented smooth manifold of dimension $4k$. Then the signature of the intersection form is a characteristic number
$$
\operatorname{sign}(M) = \langle L_k(p_1, \ldots, p_k), [M]\rangle,
$$
where $L_k$ is the **Hirzebruch $L$-polynomial**, the polynomial in the Pontryagin classes given by the generating function
$$
\sum_k L_k = \prod_j \frac{x_j}{\tanh x_j}
$$
in the Pontryagin roots of the tangent bundle; the $L$-polynomial is the characteristic class of the signature, and the theorem is the first of the applications of the characteristic classes to the topology of the manifolds.

**Example.** In dimension $4$ the signature theorem reads $\operatorname{sign}(M) = \frac13 p_1(TM)[M]$, and for the complex projective plane $\mathbb{CP}^2$ one has $p_1(T\mathbb{CP}^2) = 3x^2$ with $x^2[M] = 1$, so the signature is $1$, as it must be for the intersection form of $\mathbb{CP}^2$; for the K3 surface the signature is $-16$ and the first Pontryagin class evaluates to $-48$. The signature theorem is the prototype of the theorem of the next paragraph, and it is the source of the characteristic numbers of the manifolds.

## The Splitting Principle and the Characteristic Numbers

### The Splitting Principle

**Theorem (splitting principle).** Let $E \to B$ be a complex vector bundle of rank $n$ and let $\pi : F(E) \to B$ be the flag bundle of the complete flags of the fibres, whose fibre is the flag manifold and whose pullback $\pi^*E$ splits as a sum of line bundles,
$$
\pi^*E = L_1 \oplus \cdots \oplus L_n ;
$$
the map $\pi^* : H^*(B;\mathbb{Z}) \to H^*(F(E);\mathbb{Z})$ is injective, so an identity among the characteristic classes of $E$ holds on $B$ if and only if it holds after the splitting. The **Chern roots** $x_i = c_1(L_i)$ of the bundle satisfy
$$
c(E) = \prod_{i=1}^{n}(1 + x_i), \qquad p(E_{\mathbb{R}}) = \prod_{i=1}^{n}(1 + x_i^2),
$$
where the realification $E_{\mathbb{R}}$ has $(E_{\mathbb{R}}) \otimes \mathbb{C} = E \oplus \bar{E}$ and one root is taken from each conjugate pair, so that $p_i(E_{\mathbb{R}}) = (-1)^i c_{2i}(E \oplus \bar{E})$; and every symmetric polynomial in the roots is a polynomial in the Chern classes.

**Proof sketch.** The flag bundle is the bundle of the complete flags of the fibres, and its pullback of $E$ carries the tautological filtration whose successive quotients are line bundles; the cohomology of the flag bundle is a free module over the cohomology of the base with the Schubert cells as a basis, so the pullback is injective. The formula for the total class is the Whitney sum formula iterated over the line bundles, and the symmetric-polynomial statement is the invariant theory of the symmetric group acting on the roots. $\square$

**Corollary.** The Chern character is a ring homomorphism for the tensor product, $\operatorname{ch}(E \otimes F) = \operatorname{ch}(E)\operatorname{ch}(F)$, and it takes the values $\operatorname{ch}(L) = e^{x}$ on a line bundle of class $x$; the Chern classes and the Chern character determine each other, and the character is the natural bridge to the $K$-theory of *Topological K-Theory* and to the index theory of this Part.

### Characteristic Numbers and Cobordism

**Definition.** Let $M$ be a closed oriented smooth manifold of dimension $n$. A **characteristic number** of $M$ is the evaluation
$$
\langle \kappa(TM), [M]\rangle \in \mathbb{Z}
$$
of a characteristic class of degree $n$ of the tangent bundle on the fundamental class of $M$; the characteristic numbers of the monomials in the Pontryagin classes are the **Pontryagin numbers**, those of the Chern classes of a complex manifold are the **Chern numbers**, and the Stiefel–Whitney numbers are the evaluations of the monomials in the Stiefel–Whitney classes in $H^n(M;\mathbb{Z}/2)$.

**Theorem (Thom; the cobordism invariants).** Two closed smooth manifolds are **cobordant** if their disjoint union is the boundary of a compact manifold with boundary, and the cobordism classes form a graded ring under the disjoint union and the Cartesian product; the characteristic numbers are invariants of the cobordism class, two closed manifolds are unoriented cobordant if and only if all their Stiefel–Whitney numbers agree, and two closed oriented manifolds are oriented cobordant if and only if all their Stiefel–Whitney numbers and all their Pontryagin numbers agree; these are the theorems of Thom. The signature is a cobordism invariant, being the characteristic number of the $L$-class; the $\hat{A}$-genus is a characteristic number of the spin manifolds, and it is the topological obstruction to the positive scalar curvature.

**Remark.** The characteristic numbers are the bridge from the characteristic classes to the topology of the manifolds: the classes themselves live in the cohomology of the base, and the numbers are their evaluations on the fundamental class, which are the invariants of the bordism type of the manifold. The Atiyah–Singer index theorem of this Part computes the index of an elliptic operator as a characteristic number of the symbol, and the spin case is the case in which the characteristic number is the $\hat{A}$-genus; the characteristic classes of the present article are therefore the input of the index theory, and the Chern–Weil classes of the companion article are the differential forms by which the index is computed locally. The unoriented and oriented cobordism rings, the signature theorem and the $\hat{A}$-genus are the classical applications, and the theory of the characteristic numbers of the complex manifolds is the Riemann–Roch–Hirzebruch theorem.

**Example (the low-dimensional numbers).** For a closed oriented surface the only characteristic number of the tangent bundle in degree $2$ is the Euler number $\langle e(TM),[M]\rangle = \chi(M)$, the Euler characteristic, which is the Gauss–Bonnet theorem of the Chern–Weil theory; for a closed oriented four-manifold the characteristic numbers are the signature $\langle L_1,[M]\rangle = \frac13 p_1[M]$ and the Euler number $\langle e,[M]\rangle = \chi(M)$, subject to the integrality conditions of the Wu classes; for a closed complex surface the Chern numbers $c_1^2$ and $c_2$ are related to the signature and the Euler characteristic by the Hirzebruch and Noether formulas, and the Chern numbers are the invariants of the complex cobordism class.

## Summary

A **characteristic class** of a vector bundle $E \to B$ is a natural assignment of a cohomology class of $B$ to $E$, normalised to vanish on the trivial bundles and compatible with the Whitney sum; the classes are the pullbacks of the **universal classes** along the classifying map $B \to BO(n)$ or $B \to BU(n)$, and the rings of the classes are the cohomology rings
$$
H^*(BO(n);\mathbb{Z}/2) = \mathbb{Z}/2[w_1,\ldots,w_n], \qquad H^*(BU(n);\mathbb{Z}) = \mathbb{Z}[c_1,\ldots,c_n]
$$
of the classifying spaces. The four families are the **Stiefel–Whitney** classes $w_i(E) \in H^i(B;\mathbb{Z}/2)$, with $w_1$ the orientation obstruction and $w_2$ the spin obstruction; the **Chern** classes $c_i(E) \in H^{2i}(B;\mathbb{Z})$, with $c(E\oplus F) = c(E)c(F)$ and $c(T\mathbb{CP}^n) = (1+x)^{n+1}$; the **Pontryagin** classes $p_i(E) = (-1)^i c_{2i}(E\otimes\mathbb{C}) \in H^{4i}(B;\mathbb{Z})$, with $p_i \equiv w_{2i}^2 \bmod 2$ and $p(E_{\mathbb{R}}) = c(E)c(\bar E)$ for a complex bundle; and the **Euler** class $e(E) \in H^n(B;\mathbb{Z})$ of an oriented rank-$n$ bundle, the primary obstruction to a nowhere-zero section, with $e \equiv w_n \bmod 2$ and the de Rham image $\operatorname{Pf}(R/2\pi)$. The **splitting principle** reduces the identities among the classes to the case of the direct sums of line bundles with the Chern roots $x_i$, and the **Chern character** $\operatorname{ch}: K^0(B) \to H^{\mathrm{ev}}(B;\mathbb{Q})$ is a ring isomorphism after tensoring with $\mathbb{Q}$. The **characteristic numbers** are the evaluations of the classes of the tangent bundle on the fundamental class; they are the invariants of the cobordism classes (Thom), the signature is the characteristic number of the Hirzebruch $L$-class, $\operatorname{sign}(M) = \langle L_k(p_1,\ldots,p_k),[M]\rangle$ in dimension $4k$, and the $\hat{A}$-genus is the characteristic number of the spin manifolds. The Chern–Weil construction of *Fibre Bundles, Connections and Curvature* realises the Chern, Pontryagin and Euler classes in the real cohomology through the curvature, and the index theory of this Part computes the indices of the elliptic operators as the characteristic numbers of their symbols.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E \to B$, $F \to B$ | Vector bundles over the base $B$ |
| $\mathbb{K}$ | The scalar field $\mathbb{R}$ or $\mathbb{C}$; $\mathbf{Vect}_n^{\mathbb{K}}(B)$ |
| $\kappa(E) \in H^i(B;A)$ | Characteristic class of degree $i$ |
| $w_i(E) \in H^i(B;\mathbb{Z}/2)$ | Stiefel–Whitney classes; $w_1$ orientation, $w_2$ spin |
| $c_i(E) \in H^{2i}(B;\mathbb{Z})$ | Chern classes; $c(E\oplus F)=c(E)c(F)$ |
| $p_i(E) = (-1)^i c_{2i}(E\otimes\mathbb{C})$ | Pontryagin classes |
| $e(E) \in H^n(B;\mathbb{Z})$ | Euler class of an oriented rank-$n$ bundle |
| $BO(n)$, $BU(n)$ | Classifying spaces of the real and complex rank-$n$ bundles |
| $w_i$, $c_i$, $p_i$ | Universal classes in $H^*(BO(n))$, $H^*(BU(n))$ |
| $x_i = c_1(L_i)$ | Chern roots; $c(E) = \prod(1+x_i)$ |
| $\operatorname{ch}(E)$ | Chern character; $K^0(B)\otimes\mathbb{Q} \cong H^{\mathrm{ev}}(B;\mathbb{Q})$ |
| $p_i \equiv w_{2i}^2$, $e \equiv w_n \pmod 2$ | Relations among the classes |
| $L_k(p_1,\ldots,p_k)$ | Hirzebruch $L$-polynomial; $\sum_k L_k = \prod_j \frac{x_j}{\tanh x_j}$ |
| $\operatorname{sign}(M) = \langle L_k,[M]\rangle$ | Signature theorem for $\dim M = 4k$ |
| characteristic number | Evaluation $\langle\kappa(TM),[M]\rangle$ |



## Further Reading

- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for the axioms, the classifying spaces, the Wu formula and the cobordism invariants.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the Chern–Weil theory and the de Rham realisation of the characteristic classes.
- Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry* (Springer, 1966), for the signature theorem, the $L$-polynomial and the Riemann–Roch–Hirzebruch theorem.
- Shiing-Shen Chern, *Complex Manifolds Without Potential Theory* (Springer, 1979), for the Chern classes and the Chern character.
- René Thom, "Quelques propriétés globales des variétés différentiables", *Commentarii Mathematici Helvetici* 28 (1954), 17–86, for the cobordism classification and the characteristic numbers.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the singular cohomology, the Steenrod squares and the classifying spaces used throughout.
