
# __Calabi–Yau Manifolds__

## Introduction

A **Calabi–Yau manifold** is a compact Kähler manifold whose first Chern class vanishes. The definition is cohomological, but it is equivalent to a geometric statement about the canonical bundle, to a statement about holonomy — the holonomy group lies in the special unitary group $SU(n)$ — and to a statement about differential forms: there is a nowhere vanishing holomorphic $n$-form, and Yau's theorem endows the manifold with a Ricci-flat Kähler metric. The four descriptions are the reason Calabi–Yau manifolds occupy the centre of modern geometry: they are the compact Ricci-flat Kähler manifolds, the irreducible ones among them are the manifolds of exceptional holonomy $SU(n)$ in Berger's classification, and the existence of the metric is the solution of a complex Monge–Ampère equation.

This article develops the condition, its equivalent forms, the holomorphic volume form and the Hodge-theoretic consequences that the holonomy restriction forces, and the two standard families of examples: the hypersurfaces of degree $n+1$ in $\mathbb{CP}^n$, among them the elliptic curves, the quartic $K3$ surfaces and the quintic threefolds, and the torus and orbifold constructions. It states Yau's theorem as the source of the metrics and the Bogomolov decomposition as the structure theorem for the whole class of manifolds with $c_1=0$. It closes with the period map and the mirror phenomenon, which exchanges the two Hodge numbers $h^{1,1}$ and $h^{2,1}$ of a Calabi–Yau threefold.

**The boundaries of the article.** The Riemannian metric, the Levi-Civita connection, holonomy and Berger's classification are those of *Riemannian Geometry*. The complex structure, the Chern connection and the fundamental form are those of *Hermitian Geometry and Almost Complex Structures*; the Kähler condition, the Hodge decomposition, the Lefschetz theorems and the Ricci form are those of *Kähler Geometry*, and Yau's theorem is stated there and used here. The quaternionic and hyperkähler structures are those of *Quaternionic Geometry* and *Hyperkähler Geometry*; a Calabi–Yau manifold of even complex dimension whose holonomy is smaller than $SU(2n)$ is hyperkähler, and the hyperkähler manifolds are treated separately. The exceptional holonomy cases $G_2$ and $\mathrm{Spin}(7)$, which occur in real dimensions seven and eight and are the relatives of the Calabi–Yau condition, are not covered here. The characteristic classes of a complex manifold are those of *Characteristic Classes*, earlier in this Part. The Hodge theory of a compact Kähler manifold, the finiteness of the cohomology and the existence theory of the Monge–Ampère equation require the analysis of Part III, where the measure and the limit are available; the results are stated here and their proofs cited. The period map, the Torelli problem, mirror symmetry and the enumeration of rational curves belong to algebraic geometry and to the enumerative theory, and are mentioned only as consequences of the geometry. The base field is $\mathbb{C}$ for the manifolds and $\mathbb{R}$ for the metrics; no physics is invoked.

## The Calabi–Yau Condition

**Definition.** A **Calabi–Yau manifold** is a compact Kähler manifold $M$ of complex dimension $n$ with $c_1(M) = 0$ in $H^2(M;\mathbb{R})$.

**Theorem (equivalent forms of the Calabi–Yau condition).** Let $M$ be a compact Kähler manifold of complex dimension $n$. The following are equivalent:

**(a)** $c_1(M) = 0$;

**(b)** the canonical bundle $K_M = \Lambda^n(T^{1,0}M)^*$ is torsion, $K_M^{\otimes m}\cong\mathcal{O}_M$ for some $m\geq1$; equivalently, a finite étale cover of $M$ has trivial canonical bundle and carries a nowhere vanishing holomorphic $n$-form $\Omega$;

**(c)** $M$ carries a Kähler metric with vanishing Ricci form, and therefore a Ricci-flat Kähler metric;

**(d)** the reduced holonomy group of some Kähler metric on $M$ is contained in $SU(n)$.

**Proof sketch.** (a)$\Leftrightarrow$(c) is Yau's theorem, stated below: the Ricci form represents $2\pi c_1(M)$, so a Kähler class is the class of a Ricci-flat metric exactly when $c_1=0$. (c)$\Rightarrow$(d): a Ricci-flat Kähler metric has reduced holonomy in $SU(n)$, the subgroup of $U(n)$ fixing the complex volume form. (d)$\Rightarrow$(b): a metric of holonomy in $SU(n)$ has a parallel complex volume form, which is a nowhere vanishing holomorphic $n$-form on the finite étale cover that makes the holonomy connected, so that the canonical bundle is trivial there and torsion in general. (b)$\Rightarrow$(a): a torsion canonical bundle has $c_1(K_M)=0$ in $H^2(M;\mathbb{R})$, and $c_1(M) = -c_1(K_M)$. The passage from the vanishing of $c_1$ in real cohomology to the torsion of the canonical bundle is the theorem of Bogomolov and Beauville; it is the step that makes the equivalence a statement about compact Kähler manifolds. $\square$

**Theorem (Yau, on the Calabi conjecture).** Let $M$ be a compact Kähler manifold with $c_1(M)=0$. Then every Kähler class on $M$ contains exactly one Ricci-flat Kähler metric. The metric is obtained by solving the complex Monge–Ampère equation

$$
\det\Bigl(g_{i\bar j} + \partial_i\partial_{\bar j}\varphi\Bigr) = \det(g_{i\bar j})
$$

for the potential $\varphi$, where $g$ is any Kähler metric in the given class.

**Proof sketch.** The statement is that of *Kähler Geometry*; the proof is the continuity method for the Monge–Ampère equation, with the a priori estimates of Yau and the openness from the implicit function theorem. The analysis is that of Part III, where the measure and the limit are available. $\square$

**Definition.** A Calabi–Yau manifold is **strict**, or has **holonomy exactly $SU(n)$**, if the holonomy of its Ricci-flat Kähler metric is not a proper subgroup of $SU(n)$. The cases with smaller holonomy are the flat tori (trivial holonomy), the hyperkähler manifolds (holonomy in $Sp(k)\subseteq SU(2k)$, treated in *Hyperkähler Geometry*), and their products.

**Remark.** The condition is a single cohomological equation, but its content is a parallel form: the holonomy reduction to $SU(n)$ means that the bundle of exterior forms acquires an extra invariant $\Omega$, and with it the Hodge numbers of $M$ become constrained. The Ricci-flat metric of Yau's theorem is the geometry behind the algebra: a Calabi–Yau manifold is the pair of a complex structure and a Kähler class, together with the metric that the Monge–Ampère equation assigns to them, and the moduli problem of complex structures is the moduli problem of the underlying manifolds.

## The Holomorphic Volume Form and the Hodge Numbers

**Definition.** Let $M$ be a Calabi–Yau manifold. A **holomorphic volume form** is a nowhere vanishing holomorphic section

$$
\Omega \in H^0(M, K_M) = H^0(M,\Lambda^n(T^{1,0}M)^*),
$$

unique up to a nonzero complex constant when $M$ is connected. In local holomorphic coordinates it is $\Omega = f(z)\,dz^1\wedge\cdots\wedge dz^n$ with $f$ holomorphic and nowhere zero.

**Proposition.** Let $M$ be Calabi–Yau with holomorphic volume form $\Omega$ and Ricci-flat Kähler metric $g$. Then:

**(a)** $\Omega$ is parallel for the Levi-Civita connection, $\nabla\Omega = 0$;

**(b)** the Riemannian volume form is $\Omega\wedge\bar\Omega$ up to a positive constant, and $|\Omega|_g$ is constant;

**(c)** $h^{n,0}(M) = 1$, and $h^{p,0}(M) = 0$ for $0 < p < n$ when the holonomy is exactly $SU(n)$;

**(d)** the Hodge numbers satisfy the symmetry $h^{p,q} = h^{n-p,n-q}$ and, when the holonomy is exactly $SU(n)$, also $h^{p,0}=0$ and $b_1(M)=0$.

**Proof.** (a) Since $c_1(M)=0$, the Ricci form is exact and the metric can be chosen Ricci-flat; a holomorphic $n$-form has constant norm with respect to a Ricci-flat Kähler metric, and the parallel transport preserves it, so it is parallel. (b) $\Omega$ is a generator of the top exterior power and is parallel, so $\Omega\wedge\bar\Omega$ is a parallel top form, hence a constant multiple of the volume; the constancy of $|\Omega|_g$ is the same statement. (c) and (d) follow from the holonomy principle: a harmonic form that is invariant under the holonomy group is parallel, and the invariants of $SU(n)$ acting on exterior powers vanish on the type-$(p,0)$ parts for $0<p<n$; in particular the only holomorphic $p$-forms for $0<p<n$ are zero. $\square$

**Remark.** The symmetry $h^{p,q} = h^{n-p,n-q}$ is Serre duality combined with the triviality of the canonical bundle, and the vanishing of $h^{p,0}$ is the statement that a strict Calabi–Yau manifold has no holomorphic $1$-forms; the Bochner argument shows that a compact Ricci-flat Kähler manifold with $b_1\neq0$ splits off a flat torus factor, and the vanishing of $b_1$ together with the splitting theory for Ricci-flat Kähler metrics gives the finiteness of the fundamental group of a strict Calabi–Yau manifold — a standard consequence of the holonomy reduction. This is the sharpest single consequence of the holonomy reduction, and it is why the Calabi–Yau condition sits at the boundary between the flat and the hyperbolic ends of Kähler geometry.

**Proposition.** Let $M$ be a Calabi–Yau manifold of complex dimension $n$. When $n$ is even and the holonomy is $Sp(n/2)$, the manifold carries a holomorphic symplectic $2$-form $\sigma$ whose top power $\sigma^{\wedge n/2}$ is the holomorphic volume form; in general, $\Omega$ trivialises the canonical bundle and the Hodge structure on $H^n(M;\mathbb{Q})$ is a polarised Hodge structure of weight $n$ with $h^{n,0}=1$.

**Proof.** If the holonomy is $Sp(k)\subseteq SU(2k)$ then the parallel holomorphic volume form is a power of the holomorphic symplectic form of *Hyperkähler Geometry*; in the general case, $\Omega$ spans $H^{n,0}$ and the Hodge–Riemann bilinear relations of *Kähler Geometry* polarise the primitive part. $\square$

## Examples

**Example (complex dimension one).** A compact Riemann surface of genus one is Calabi–Yau: $c_1=0$ for the torus, the holomorphic volume form is the holomorphic $1$-form $dz$ in a uniformisation $\mathbb{C}/\Lambda$, and the flat metric is Ricci-flat. Genus $g\neq1$ is not Calabi–Yau, since $c_1\neq0$; the sphere has $c_1\neq0$. In complex dimension one the Calabi–Yau manifolds are exactly the elliptic curves.

**Example (complex dimension two).** Among compact Kähler surfaces with $c_1=0$, every one is finitely covered by a complex torus, a $K3$ surface, or a product of two elliptic curves; the surfaces with torsion canonical bundle — the Enriques and the bielliptic surfaces — are finite quotients of these, and the non-Kähler examples with $c_1=0$, the Kodaira surfaces, are excluded by the Kähler hypothesis. The $K3$ surface is simply connected, has $b_2=22$ and Hodge numbers $h^{2,0}=h^{0,2}=1$, $h^{1,1}=20$, and Euler characteristic $\chi = 24$. Its Ricci-flat Kähler metrics are the Yau metrics, the moduli space of its complex structures is twenty-dimensional, and by the classification of surfaces it is a hyperkähler four-manifold in the sense of *Hyperkähler Geometry*. The quartic surface of degree four in $\mathbb{CP}^3$ is the classical $K3$ example:

$$
X_4 = \{F_4(z_0,z_1,z_2,z_3)=0\} \subseteq \mathbb{CP}^3,
$$

and the Chern class computation gives $c_1(X_4)=0$ and $\chi(X_4)=24$.

**Example (the quintic threefold).** The **quintic threefold** is the smooth hypersurface

$$
X_5 = \{F_5(z_0,\ldots,z_4)=0\} \subseteq \mathbb{CP}^4,
$$

of degree five. Its Chern classes are those of the adjunction

$$
c(TX_5) = \frac{(1+H)^5}{1+5H}\Big|_{X_5} = 1 + 10H^2 - 40H^3 + 205H^4,
$$

so that $c_1(X_5)=0$ and the Euler characteristic is

$$
\chi(X_5) = \int_{X_5}c_3(TX_5) = -40\cdot 5 = -200 .
$$

By the Lefschetz hyperplane theorem $h^{1,1}(X_5)=1$, and from $\chi = 2(h^{1,1}-h^{2,1})$ one obtains $h^{2,1}(X_5)=101$. The quintic is the model Calabi–Yau threefold, and the Fermat quintic $z_0^5+\cdots+z_4^5=0$ is its most symmetric member, with a large group of projective automorphisms.

**Example (hypersurfaces and complete intersections).** Let $X_d\subseteq\mathbb{CP}^n$ be a smooth hypersurface of degree $d$. By the adjunction formula $c_1(X_d) = (n+1-d)H$, so $X_d$ is Calabi–Yau exactly when $d = n+1$. This gives the elliptic curve $X_3\subseteq\mathbb{CP}^2$, the quartic $K3$ surface $X_4\subseteq\mathbb{CP}^3$, the quintic threefold $X_5\subseteq\mathbb{CP}^4$, and the four-, five- and sixfolds $X_6\subseteq\mathbb{CP}^5$, $X_7\subseteq\mathbb{CP}^6$, $X_8\subseteq\mathbb{CP}^7$. Complete intersections of multidegree $(d_1,\ldots,d_k)$ in $\mathbb{CP}^n$ are Calabi–Yau when $\sum_i d_i = n+1$, and this gives the threefolds of bidegree $(3,3)$, $(2,4)$ and $(2,2,3)$ in the appropriate projective spaces.

**Example (tori, orbifolds and their resolutions).** The complex torus $T^6 = \mathbb{C}^3/\Lambda$ is Calabi–Yau with the flat metric and trivial holonomy. The quotient of $T^6$ by the order-three automorphism acting as a rotation of order three on each elliptic factor is a Calabi–Yau orbifold with $27$ isolated fixed points; each is resolved by an exceptional divisor, and the crepant resolution is a smooth Calabi–Yau threefold with $h^{1,1}=36 = 9+27$ — the nine invariant classes of the torus and one divisor per fixed point — with $h^{2,1}=0$ and Euler characteristic $\chi = 2(36-0) = 72$. This is the standard construction of the **rigid** Calabi–Yau threefolds, those with $h^{2,1}=0$ and hence no deformations of the complex structure.

**Example (weights and quotients).** Hypersurfaces in weighted projective spaces, and the resolutions of their quotient singularities, produce large families of Calabi–Yau threefolds with prescribed Hodge numbers; the Greene–Plesser construction realises them as quotients of Fermat-type hypersurfaces, and the mirrors of a family arise from a different resolution of the same orbifold. The construction is algebraic and the results are the Hodge numbers of the resulting smooth manifolds.

**Example (products and factors of smaller dimension).** A product of Calabi–Yau manifolds is Calabi–Yau with the product metric, but its holonomy is a product and its structure is reducible; the Bogomolov decomposition expresses every compact Kähler manifold with $c_1=0$ as a product of a torus, irreducible Calabi–Yau factors and irreducible hyperkähler factors up to finite étale cover. A Calabi–Yau manifold that is neither a torus nor a product nor hyperkähler is **irreducible** of holonomy $SU(n)$.

## The Moduli Space and the Period Map

**Remark (deformations).** The complex structures on a Calabi–Yau manifold $M$ near a given one are governed by the Kodaira–Spencer theory: the first-order deformations are $H^1(M, T^{1,0}M)$, and for a Calabi–Yau manifold with holonomy $SU(n)$ one has the isomorphism

$$
H^1(M,T^{1,0}M) \cong H^{n-1,1}(M) \cong H^{2,1}(M)
$$

for $n=3$, so that $h^{2,1}$ counts the complex-structure moduli and $h^{1,1}$ counts the Kähler moduli. The moduli space of the complex structures is a complex manifold of dimension $h^{2,1}$ locally, and the Kähler moduli sit in the complexification of the Kähler cone, a domain of dimension $h^{1,1}$; the sum $h^{1,1}+h^{2,1}$ is the dimension of the extended moduli in which the mirror correspondence is stated.

**Theorem (local Torelli for Calabi–Yau manifolds; Griffiths, Voisin).** Let $M$ be a Calabi–Yau manifold. The **period map** that assigns to a complex structure the Hodge filtration of $H^n(M;\mathbb{C})$,

$$
\mathcal{M} \longrightarrow \mathcal{D}, \qquad M_t \longmapsto \bigl(F^n_t \subset F^{n-1}_t \subset \cdots \subset H^n(M;\mathbb{C})\bigr),
$$

is a local isomorphism onto its image in the cases $n=1,2,3$ — the elliptic curves, the $K3$ surfaces and the Calabi–Yau threefolds — where the infinitesimal Torelli theorem holds; for the higher dimensions the infinitesimal and the global statements are the subject of the Torelli problem, which is open in general, and the global question — whether the period point determines the manifold — is answered affirmatively for the elliptic curves and the $K3$ surfaces, while for Calabi–Yau threefolds it is known to fail for some families.

**Proof sketch.** The differential of the period map is the cup product with the Kodaira–Spencer class, and its injectivity is the infinitesimal Torelli theorem; the global statement is the theory of the period domain $D$ of polarised Hodge structures of weight $n$ and the horizontality of the period map. The analytic input is the finite-dimensionality of the Hodge theory again; the proofs are those of the Hodge-theoretic literature cited below. $\square$

**Remark (Bogomolov decomposition and the classification scheme).** The Bogomolov decomposition, stated in *Hyperkähler Geometry*, reduces the classification of compact Kähler manifolds with $c_1=0$ to the classification of the irreducible Calabi–Yau and hyperkähler factors. The Calabi–Yau factors of dimension three are the playground of mirror symmetry, and the enumeration of their rational curves — which requires the Gromov–Witten invariants and the analysis of the corresponding moduli spaces of stable maps — is where the enumerative theory of algebraic geometry meets the Hodge theory of this article.

**Remark (mirror symmetry as a Hodge-theoretic statement).** For a Calabi–Yau threefold $X$ with Hodge numbers $h^{1,1}$ and $h^{2,1}$ there is a mirror partner $\check X$ with

$$
h^{1,1}(\check X) = h^{2,1}(X), \qquad h^{2,1}(\check X) = h^{1,1}(X), \qquad \chi(\check X) = -\chi(X),
$$

and with the complex-structure moduli of $X$ identified with the Kähler moduli of $\check X$. The statement is a statement about the Hodge numbers and the period maps, verified for the constructed families of hypersurfaces and complete intersections by the Greene–Plesser and Batyrev constructions, and it explains the symmetry of the Hodge-number tables of the known families. The quantum or enumerative content — the relation between the periods of $\check X$ and the numbers of rational curves on $X$ — lies outside this corpus.

## Summary

A Calabi–Yau manifold is a compact Kähler manifold with $c_1(M)=0$; equivalently its canonical bundle $K_M$ is torsion, trivial on a finite étale cover, so that the cover carries a nowhere vanishing holomorphic $n$-form $\Omega$; equivalently it carries a Ricci-flat Kähler metric, whose reduced holonomy is then contained in $SU(n)$. The equivalence of the first and third is Yau's solution of the Calabi conjecture: in each Kähler class on a compact Kähler manifold with $c_1=0$ there is exactly one Ricci-flat Kähler metric, obtained from the complex Monge–Ampère equation for the potential.

The holomorphic volume form $\Omega$ is parallel, its modulus $|\Omega|_g$ is constant and $\Omega\wedge\bar\Omega$ is a constant multiple of the volume; the holonomy principle gives $h^{n,0}=1$, and for strict holonomy $SU(n)$ also $h^{p,0}=0$ for $0<p<n$ and $b_1=0$, with the Hodge symmetry $h^{p,q}=h^{n-p,n-q}$.

The standard examples are the elliptic curves in dimension one, the tori and $K3$ surfaces in dimension two and the quintic threefold $X_5\subseteq\mathbb{CP}^4$ in dimension three, with $c_1=0$, $\chi=-200$, $h^{1,1}=1$ and $h^{2,1}=101$; the hypersurfaces of degree $n+1$ in $\mathbb{CP}^n$ and the complete intersections with $\sum d_i=n+1$ form the classical families, and torus quotients resolved produce the rigid threefolds with $h^{2,1}=0$. The period map is a local isomorphism in the low-dimensional cases in which the infinitesimal Torelli theorem holds, and mirror symmetry exchanges the Hodge numbers $h^{1,1}$ and $h^{2,1}$ of a Calabi–Yau threefold and its partner. The even-dimensional Calabi–Yau manifolds whose holonomy is the subgroup $Sp(k)$ are the hyperkähler manifolds of *Hyperkähler Geometry*; the rigid analytic cases of $G_2$ and $\mathrm{Spin}(7)$ holonomy are not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$ | Compact Kähler manifold of complex dimension $n$ |
| $c_1(M)=0$ | The Calabi–Yau condition; equivalently $K_M$ torsion, equivalently reduced holonomy in $SU(n)$ |
| $K_M = \Lambda^n(T^{1,0}M)^*$ | Canonical bundle; $c_1(M) = -c_1(K_M)$ |
| $\Omega \in H^0(M,K_M)$ | Holomorphic volume form; $\nabla\Omega=0$, $|\Omega|_g$ constant |
| $g_{i\bar j}$, $\varphi$ | Kähler metric and potential; Monge–Ampère $\det(g_{i\bar j}+\partial_i\partial_{\bar j}\varphi)=\det(g_{i\bar j})$ |
| $h^{p,q}$, $\chi$ | Hodge numbers; $\chi = \sum(-1)^{p+q}h^{p,q}$, $h^{p,q}=h^{n-p,n-q}$ |
| Strict Calabi–Yau | Holonomy exactly $SU(n)$; $h^{p,0}=0$ ($0<p<n$), $b_1=0$ |
| $X_d\subseteq\mathbb{CP}^n$ | Hypersurface of degree $d$; Calabi–Yau iff $d=n+1$; $c_1=(n+1-d)H$ |
| Quintic | $X_5\subseteq\mathbb{CP}^4$: $h^{1,1}=1$, $h^{2,1}=101$, $\chi=-200$ |
| $K3$ | Surface with $c_1=0$, $b_2=22$, $h^{1,1}=20$, $h^{2,0}=1$, $\chi=24$ |
| $T^6/\mathbb{Z}_3$ | Rigid Calabi–Yau threefold from a resolved orbifold: $h^{1,1}=36$, $h^{2,1}=0$, $\chi=72$ |
| Period map | $\mathcal{M}\to\mathcal{D}$, $M_t\mapsto$ Hodge filtration of $H^n(M;\mathbb{C})$ |
| Mirror | $h^{1,1}(\check X)=h^{2,1}(X)$, $h^{2,1}(\check X)=h^{1,1}(X)$, $\chi(\check X)=-\chi(X)$ |





## Further Reading

- Shing-Tung Yau, "On the Ricci Curvature of a Compact Kähler Manifold and the Complex Monge–Ampère Equation, I", *Communications on Pure and Applied Mathematics* 31 (1978), 339–411, for the Ricci-flat Kähler metric in each Kähler class.
- Eugenio Calabi, "On Kähler Manifolds with Vanishing Canonical Class", in *Algebraic Geometry and Topology: A Symposium in Honor of S. Lefschetz* (Princeton University Press, 1957), 78–89, for the conjecture and the structure of the holonomy reduction.
- Fedor A. Bogomolov, "On the Decomposition of Kähler Manifolds with Trivial Canonical Class", *Mathematics of the USSR-Izvestiya* 8 (1974), 55–80, for the decomposition theorem.
- Arnaud Beauville, "Variétés Kähleriennes dont la première classe de Chern est nulle", *Journal of Differential Geometry* 18 (1983), 755–782, for the refined decomposition and the hyperkähler factors.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the adjunction formula, the Hodge numbers of hypersurfaces and the period map.
- Claire Voisin, *Hodge Theory and Complex Algebraic Geometry, I–II* (Cambridge University Press, 2002), for the period map, the local Torelli theorem and the Hodge structures of Calabi–Yau manifolds.
- Tristan Hübsch, *Calabi–Yau Manifolds: A Bestiary for Physicists* (World Scientific, 1992), for the tables of Hodge numbers of hypersurfaces, complete intersections and weighted projective constructions.
- Brian Greene and M. Ronen Plesser, "Duality in Calabi–Yau Moduli Space", *Nuclear Physics B* 338 (1990), 15–37, for the mirror construction by quotients and resolutions.
- Victor Batyrev, "Dual Polyhedra and Mirror Symmetry for Calabi–Yau Hypersurfaces in Toric Varieties", *Journal of Algebraic Geometry* 3 (1994), 493–535, for the toric construction of mirror pairs and the combinatorial computation of Hodge numbers.
