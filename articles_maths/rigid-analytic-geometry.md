
# __Rigid Analytic Geometry__

## Introduction

Over a non-Archimedean field the naive notion of an analytic function fails in a way that has no Archimedean analogue: the unit disc admits functions that are bounded but not locally constant, yet the classical identity theorem and the maximum principle of complex analysis have no direct transcription, because there is no integration against a contour and because the ground field is totally disconnected. Tate's remedy, and the beginning of non-Archimedean geometry, was to abandon the pointwise notion of an open set and to replace it by a *Grothendieck topology* on the spectrum of an algebra of convergent power series. The resulting objects — **affinoid algebras**, **affinoid spaces**, and **rigid analytic spaces** glued from them — carry a structure sheaf for which the analogues of the theorems of analytic geometry hold, with the Weierstrass preparation theorem and the maximum modulus principle replacing the tools of complex analysis.

This article develops the affine theory — the Tate algebra, affinoid algebras, the Weierstrass theorems and the maximum modulus principle — then the rigid topology, the affinoid subdomains and Tate's acyclicity theorem, then rigid spaces, coherent sheaves and Kiehl's theorems, and finally the GAGA principle and the relation to formal models. It is the first of the articles of this Part devoted to the geometry of a valued field, and it is deliberately written as geometry: the valuation theory that the constructions use is that of *Absolute Values, Valuations and Completions* and of *Local Fields*, and the reader is referred to those articles rather than given a re-derivation. The non-Archimedean *analysis* — power series on domains, analytic continuation, the theory of the integral and of differential equations over a valued field — belongs to Part III, where the limit and the measure are available; only the algebraic and topological content of the rings of convergent series is used here.

Throughout, $K$ is a complete non-Archimedean field with a nontrivial absolute value $\lvert \cdot \rvert$, valuation ring $\mathcal{O} = \{x: \lvert x \rvert \leq 1\}$, maximal ideal $\mathfrak{m}$ and residue field $k = \mathcal{O}/\mathfrak{m}$, as in *Local Fields*; for the geometric statements $K$ is assumed algebraically closed, so that the points of the spectra below are $K$-valued, and the general case is recovered by allowing points with values in finite extensions of $K$. Multi-indices are written $\alpha = (\alpha_1, \dots, \alpha_n) \in \mathbb{N}^n$ and $X^\alpha = X_1^{\alpha_1}\cdots X_n^{\alpha_n}$. A **$K$-Banach algebra** is a $K$-algebra complete for a submultiplicative norm (standard); the general topological- and Banach-algebra theory is developed.

---

## Non-Archimedean Phenomena

### The Failure of the Complex Picture

Over $K$ the closed unit disc is a totally disconnected compact space, and this has immediate analytic consequences. If a power series $\sum_\alpha a_\alpha X^\alpha$ with coefficients in $K$ is to converge at every point of the closed unit polydisc of $K^n$ in the sense that the terms tend to zero, a condition weaker than absolute convergence is forced by the non-Archimedean absolute value: the sequence $(a_\alpha)$ must tend to $0$ in the sense that for every $\varepsilon > 0$ there are only finitely many $\alpha$ with $\lvert a_\alpha \rvert > \varepsilon$. There is no intermediate notion of conditional convergence, because the ultrametric inequality makes a series converge exactly when its general term tends to $0$. The natural ring of functions on the unit disc is therefore the ring of power series whose coefficients tend to $0$, and this ring is the object with which the theory starts.

Two further features distinguish the situation from the Archimedean one. First, a series with coefficients tending to $0$ converges uniformly, and its supremum over the disc is attained at a coefficient; there is no boundary phenomenon. Second, the disc decomposes into disjoint residue classes, each of which is simultaneously open and closed, so that a function which is "locally constant modulo $\mathfrak{m}$" is a natural object. These two features — the sup-norm and the residue decomposition — are what Tate's theory systematises.

### The Tate Algebra

**Definition.** Let $n \geq 1$. The **Tate algebra** in $n$ variables over $K$ is

$$
K\langle X_1, \dots, X_n\rangle = \Bigl\{ f = \sum_{\alpha \in \mathbb{N}^n} a_\alpha X^\alpha : a_\alpha \in K \text{ and } \lvert a_\alpha \rvert \to 0 \Bigr\},
$$

with addition, scalar multiplication and multiplication defined termwise, and with the **Gauss norm**

$$
\lVert f \rVert_G = \max_{\alpha \in \mathbb{N}^n} \lvert a_\alpha \rvert ,
$$

the maximum existing because the coefficients tend to $0$ and the absolute value is non-Archimedean. A series is **convergent on the closed unit polydisc** when its coefficients tend to $0$.

**Theorem.** The Tate algebra $K\langle X_1, \dots, X_n\rangle$ is a commutative $K$-Banach algebra with unit $1$, the Gauss norm is a multiplicative norm, and its unit ball is the subring $\mathcal{O}\langle X_1, \dots, X_n\rangle$ of series with coefficients in $\mathcal{O}$.

**Proof.** The coefficient space is the direct sum $\bigoplus_\alpha K$ together with the sup norm, and it is complete because a Cauchy sequence of coefficient families with the sup norm is Cauchy coefficientwise and the limit family still tends to $0$: given $\varepsilon$, all but finitely many coefficients of each element of the sequence beyond some index are $\leq \varepsilon$, and a diagonal argument gives the same for the limit. Multiplicativity of the Gauss norm is the ultrametric maximum principle applied to the convolution coefficients: the maximum of the absolute values of the convolution is the product of the two maxima, because a term achieving the maximum is unique up to units in the leading coefficients of the factors and all other terms have strictly smaller absolute value. The unit ball is closed under multiplication by multiplicativity of the norm and under addition because the norm is non-Archimedean, and it is a subring. $\square$

**Remark.** The multiplicativity of the Gauss norm is a genuinely non-Archimedean phenomenon. For the Archimedean analogue the norm would be the $L^\infty$ norm on the disc, and it would not be multiplicative on the ring of convergent series.

---

## Affinoid Algebras

### Definition and Basic Properties

**Definition.** An **affinoid algebra** over $K$ is a $K$-algebra of the form

$$
A = K\langle X_1, \dots, X_n\rangle / \mathfrak{a}
$$

for some $n$ and some ideal $\mathfrak{a}$ of the Tate algebra. The **residue norm** of an element $f \in A$ is

$$
\lVert f \rVert = \inf_{g \mapsto f} \lVert g \rVert_G ,
$$

the infimum over the representatives $g$ of $f$ in $K\langle X_1, \dots, X_n\rangle$; the **spectral seminorm** is

$$
\lvert f \rvert_{\mathrm{sup}} = \sup_{x \in \operatorname{Sp} A} \lvert f(x) \rvert ,
$$

where $\operatorname{Sp} A$ is the set of maximal ideals of $A$, identified with the set of continuous $K$-algebra homomorphisms $A \to K$ because $K$ is algebraically closed.

**Theorem.** Let $A$ be an affinoid algebra with a chosen presentation. Then $A$ is a $K$-Banach algebra for the residue norm, the residue norm is submultiplicative and satisfies $\lVert f \rVert \geq \lvert f \rvert_{\mathrm{sup}}$, the spectral seminorm is a power-multiplicative seminorm with $\lvert f \rvert_{\mathrm{sup}} = \lim_m \lVert f^m \rVert^{1/m}$, and $\lvert f \rvert_{\mathrm{sup}} = 0$ if and only if $f$ is nilpotent. In particular, $A$ is reduced exactly when the spectral seminorm is a norm.

**Proof.** The residue norm is well defined and submultiplicative because the Gauss norm is, and completeness of the quotient follows from the open mapping theorem for Banach spaces: every ideal of the Tate algebra is closed — a standard consequence of the Weierstrass division theorems, the Tate algebra being noetherian — so the quotient of a Banach space by a closed subspace is complete. The inequalities are the standard comparison of the residue and spectral norms, and the limit formula is the Gelfand spectral radius formula $r(x) = \lim_n\lVert x^n\rVert^{1/n}$, which holds in every Banach algebra (standard). The final statement is the standard fact that the spectral radius vanishes exactly on the nilradical. $\square$

**Example (the disc and the polydisc).** $\operatorname{Sp} K\langle X\rangle$ is the **closed unit disc**, the set of $x \in K$ with $\lvert x \rvert \leq 1$; more generally $\operatorname{Sp} K\langle X_1, \dots, X_n\rangle$ is the closed unit polydisc, and $\lvert f \rvert_{\mathrm{sup}} = \lVert f \rVert_G$ there. The algebra of the disc is the fundamental building block, and the general affinoid algebra is a quotient of the algebra of a polydisc, so the geometry of the polydisc controls the general affine theory.

### The Weierstrass Theorems

**Definition.** Let $f = \sum_{i \geq 0} f_i(X_1, \dots, X_{n-1}) X_n^i \in K\langle X_1, \dots, X_n\rangle$. Then $f$ is **distinguished of order $d$ in $X_n$** if $f_d$ is a unit of $K\langle X_1, \dots, X_{n-1}\rangle$ and

$$
\lvert f_d \rvert > \lvert f_i \rvert \quad \text{for all } i \neq d .
$$

**Theorem (Weierstrass division).** Let $f \in K\langle X_1, \dots, X_n\rangle$ be distinguished of order $d$ in $X_n$, and let $g \in K\langle X_1, \dots, X_n\rangle$. Then there are a unique $q \in K\langle X_1, \dots, X_n\rangle$ and a unique $r \in K\langle X_1, \dots, X_{n-1}\rangle[X_n]$ of degree $< d$ in $X_n$ with

$$
g = qf + r,
$$

and $\lVert q \rVert_G \leq \lVert f \rVert_G^{-1}\lVert g \rVert_G$.

**Proof.** Divide the expansions of $f$ and $g$ as series in $X_n$ with coefficients in $K\langle X_1, \dots, X_{n-1}\rangle$; the division algorithm over the coefficient ring terminates in the limit because the coefficients of $f$ beyond the $d$-th are dominated by $f_d$, which is a unit; convergence follows from the norm estimate displayed, and uniqueness follows because a nonzero remainder of degree $< d$ cannot be a multiple of $f$, the leading coefficient of $f$ being a unit. $\square$

**Theorem (Weierstrass preparation).** Let $f \in K\langle X_1, \dots, X_n\rangle$ be distinguished of order $d$ in $X_n$. Then $f$ has a unique factorisation

$$
f = u \cdot g
$$

with $u \in K\langle X_1, \dots, X_n\rangle^\times$ a unit and $g \in K\langle X_1, \dots, X_{n-1}\rangle[X_n]$ a monic polynomial of degree $d$ whose non-leading coefficients have Gauss norm strictly less than $1$.

**Proof.** Apply Weierstrass division to $g = X_n^d$ and to $f$; the remainder is a polynomial $g$ of degree $d$ with leading coefficient $1$, and the quotient $u$ is a unit because its residue modulo the maximal ideal is the invertible constant $f_d \bmod \mathfrak{m}$; this is the standard argument of the preparation theorem. $\square$

**Corollary.** $K\langle X_1, \dots, X_n\rangle$ is a Noetherian unique factorisation domain, and every ideal is closed.

**Proof.** Noetherianity is by induction on $n$ using Weierstrass division: an ideal $\mathfrak{a}$ of $K\langle X\rangle$ is generated by a distinguished element $f$ of minimal order together with generators of the intersection $\mathfrak{a} \cap K\langle X_1,\dots,X_{n-1}\rangle$ of $\mathfrak{a}$ with the coefficient ring, the division of an arbitrary element of $\mathfrak{a}$ by $f$ leaving a remainder of degree $< d$ in $X_n$ that already lies in the coefficient ring. The factoriality is Tate's theorem, proved by the same division argument together with Gauss's lemma for the coefficient ring; closedness of ideals is the standard companion statement, proved by the same division argument together with the open mapping theorem. $\square$

### The Maximum Modulus Principle

**Theorem (maximum modulus principle).** Let $f \in K\langle X_1, \dots, X_n\rangle$. Then

$$
\sup_{x \in \operatorname{Sp} K\langle X_1, \dots, X_n\rangle} \lvert f(x) \rvert = \lVert f \rVert_G ,
$$

and the supremum is attained.

**Proof.** It suffices to treat the case $\lVert f \rVert_G = 1$, since scaling $f$ by a scalar scales both sides. Then $f \in \mathcal{O}\langle X\rangle$, some coefficient of $f$ is a unit, and the reduction $\bar f \in k[X_1, \dots, X_n]$ is a nonzero polynomial over the residue field $k$, which is infinite because $K$ is algebraically closed. Choose $\bar x = (\bar x_1, \dots, \bar x_n) \in k^n$ with $\bar f(\bar x) \neq 0$, possible since a nonzero polynomial over an infinite field does not vanish identically; lift each $\bar x_i$ to $x_i \in \mathcal{O}$, and let $x = (x_i)$. Evaluation at $x$ reduces the coefficients modulo $\mathfrak{m}$, so $\lvert f(x) \rvert = \lvert \bar f(\bar x) \rvert = 1 = \lVert f \rVert_G$. On the other hand $\lvert f(x) \rvert \leq \lVert f \rVert_G$ for every $x$ of the polydisc, by the multiplicativity of the Gauss norm and the inequality $\lvert x_i \rvert \leq 1$. Hence the supremum equals the Gauss norm and is attained. $\square$

**Corollary.** For a reduced affinoid algebra $A$ the spectral seminorm is a norm, and for each presentation the residue norm is a submultiplicative Banach norm on $A$ satisfying $\lVert f\rVert \geq \lvert f\rvert_{\mathrm{sup}}$ for every $f$. The spectrum $\operatorname{Sp} A$ is a compact Hausdorff space.

**Proof.** The maximum modulus principle identifies the spectral seminorm with the Gauss norm for the Tate algebra, and the spectral seminorm passes to a quotient of the Tate algebra, where it is a norm because the nilradical of the quotient is $0$; the inequality is the theorem above, the residue norm being the quotient norm of a complete norm. Compactness of the spectrum is the standard compactness of the Gelfand spectrum of a commutative Banach algebra, with the Zariski topology inherited from the residue norm (standard). The two norms are not equal in general: for $A = K\langle X\rangle/(X^2-t)$ with $0 < \lvert t\rvert < 1$ and $\operatorname{char} K \neq 2$, so that $A$ is reduced, the class of $X$ has residue norm $1$ and spectral norm $\lvert t\rvert^{1/2}$. $\square$

**Remark.** The maximum modulus principle is the exact replacement for the Cauchy integral formula in the non-Archimedean theory: it turns the algebraic Gauss norm into a geometric supremum, and it is the reason the affine theory can be developed from the algebras alone. The corresponding *analytic* statements — the behaviour of the supremum under restriction to subdomains, and the theory of the boundary — are statements about convergence and belong to the non-Archimedean analysis of Part III.

---

## The Rigid Topology

### Affinoid Subdomains

**Definition.** Let $A$ be an affinoid algebra and $X = \operatorname{Sp} A$. A subset $U \subseteq X$ is an **affinoid subdomain** if there are an affinoid algebra $A_U$ and a morphism of affinoid algebras $A \to A_U$ such that the induced map $\operatorname{Sp} A_U \to \operatorname{Sp} A$ is a bijection onto $U$ and is **universal** for this property: every morphism $A \to B$ of affinoid algebras whose induced map $\operatorname{Sp} B \to \operatorname{Sp} A$ lands in $U$ factors uniquely through $A \to A_U$. The three basic classes, all of which are affinoid subdomains, are:

**(a)** the **Weierstrass domain** $X(f_1, \dots, f_r) = \{x : \lvert f_i(x) \rvert \leq 1\}$, with algebra $A\langle f_1, \dots, f_r\rangle$ obtained by adjoining the $f_i$;

**(b)** the **Laurent domain** $X(f_1, \dots, f_r; g_1, \dots, g_s) = \{x : \lvert f_i(x) \rvert \leq 1, \lvert g_j(x) \rvert \geq 1\}$;

**(c)** the **rational domain** $X(f_1, \dots, f_r / g) = \{x : g(x) \neq 0 \text{ and } \lvert f_i(x) \rvert \leq \lvert g(x) \rvert \text{ for all } i\}$.

**Theorem (Gerritzen–Grauert).** Every affinoid subdomain of $X = \operatorname{Sp} A$ is a finite union of rational subdomains, and the affinoid subdomains form a basis of a topology on $X$ closed under finite intersections.

**Proof.** The Gerritzen–Grauert theorem is the standard characterisation: an affinoid subdomain is a finite union of rational subdomains, and conversely each of the three classes above is an affinoid subdomain, the universal property being verified by the corresponding algebra. Closedness under finite intersections follows from the explicit formulas for the algebras of Weierstrass, Laurent and rational domains, which are themselves affinoid. $\square$

### The G-Topology

**Definition.** Let $X = \operatorname{Sp} A$. The **weak G-topology** on $X$ is the Grothendieck topology (in the sense of *Sheaves on Sites*) whose

- **admissible open sets** are the finite unions of rational subdomains,
- **admissible coverings** are the finite coverings by rational subdomains $U_i$ that satisfy **Tate's condition**: there are finitely many $f_1, \dots, f_n \in A$ with $\lvert f_j(x) \rvert \leq 1$ for all $x \in U$ and $\sup_j \lvert f_j(x) \rvert = 1$ for every $x \in U$, such that each of the sets $\{x \in U : \lvert f_j(x) \rvert = 1\}$ is contained in one of the covering sets $U_i$.

The **strong G-topology** is the Grothendieck topology whose admissible open sets are the unions of affinoid subdomains that admit an admissible covering, and whose admissible coverings are those that refine to finite affinoid coverings. The weak G-topology generates the strong one, and both give the same sheaf theory on affinoid spaces.

**Remark.** The interest of the Grothendieck topology is that the naive Zariski topology on $\operatorname{Sp} A$ is too coarse: a finite union of affinoid subdomains need not be affinoid, and the collection of "open" sets in the naive sense does not support the sheaf property for the structure presheaf. The Tate condition on coverings restores exactly enough to make the sheaf axiom and the acyclicity theorem true. This is the conceptual step that separates rigid analytic geometry from a mere theory of maximal spectra.

### Tate's Acyclicity Theorem

**Definition.** The **structure presheaf** on $X = \operatorname{Sp} A$ assigns to an affinoid subdomain $U \subseteq X$ the algebra $A_U$ of the definition, and to an inclusion $V \subseteq U$ the canonical restriction homomorphism $A_U \to A_V$.

**Theorem (Tate's acyclicity).** Let $X = \operatorname{Sp} A$ be an affinoid space. Then the structure presheaf is a sheaf for the weak G-topology: for every admissible covering $\{U_i\}$ of an admissible open $U$ and every family $f_i \in A_{U_i}$ with $f_i = f_j$ on $U_i \cap U_j$, there is a unique $f \in A_U$ restricting to each $f_i$. Moreover the higher cohomology of the structure sheaf vanishes on affinoid spaces: $H^q(U, O_X) = 0$ for all $q > 0$ and all affinoid subdomains $U$.

**Proof.** The statement is Tate's theorem; the sheaf property is proved from the algebra of the covering, using the Weierstrass division theorem to compare the algebras of different affine pieces and the Tate condition to control the intersections, and the vanishing of higher cohomology follows from the sheaf property together with the finite acyclicity of the covering. The proofs are standard and are given in full in the references; the vanishing statement is quoted here as the foundational theorem of the subject. $\square$

**Corollary.** The pair $(X, O_X)$, with $X = \operatorname{Sp} A$ carrying the weak G-topology and $O_X$ the sheaf associated to the structure presheaf, is a locally ringed space for the Grothendieck topology, and its global sections are $A$.

**Proof.** Local rings: the stalk at a point $x$ is the local ring $O_{X,x}$ whose maximal ideal consists of the functions vanishing at $x$, which is a local ring by the standard argument that the kernel of evaluation $A \to K$ is maximal. Global sections: the sheaf axiom on the covering by all of $X$ gives $O_X(X) = A$. $\square$

---

## Rigid Analytic Spaces

### Definition and Morphisms

**Definition.** A **rigid analytic space** over $K$ is a triple $(X, \mathcal{T}_X, O_X)$ consisting of a set $X$, a Grothendieck topology $\mathcal{T}_X$ on it, and a sheaf of $K$-algebras $O_X$ on the site, such that there is an admissible covering of $X$ by admissible open sets $U_i$ with $(U_i, O_X\vert_{U_i})$ isomorphic to an affinoid space $(\operatorname{Sp} A_i, O_{\operatorname{Sp} A_i})$. A **morphism** of rigid spaces is a morphism of the underlying G-ringed spaces, that is, a map $f : X \to Y$ which pulls admissible opens back to admissible opens and which is a morphism of sheaves $f^{-1}O_Y \to O_X$; equivalently, a morphism is a family of morphisms of affinoid algebras compatible with the local identifications.

**Proposition.** The rigid analytic spaces over $K$ form a category with fibre products, and the affinoid spaces form a full subcategory.

**Proof.** Fibre products are constructed affine-locally: for affinoid algebras the tensor product $A\otimes_K B$ is not in general affinoid, but the completed tensor product $\widehat{\otimes}_K$ with respect to the residue norms is, and the completion is the correct coproduct in the category of affinoid algebras; the general case is glued from the affine pieces. The full embedding of affinoid spaces is immediate from the definition. $\square$

### Examples

**Example (the closed disc and its subdomains).** The closed unit disc $D^1 = \operatorname{Sp} K\langle X\rangle$ has as affinoid subdomains the discs $\lvert x \rvert \leq r$ for $r \in \lvert K^\times \rvert$ with $r \leq 1$, with algebra $K\langle X/r\rangle$. The intersection of two such discs is the smaller one, and the union of two proper discs is admissible but not affinoid. The maximum modulus principle identifies the norm on each algebra with the supremum on the corresponding disc.

**Example (the rigid affine line).** The **rigid affine line** is $\mathbb{A}^{1,\mathrm{rig}} = \bigcup_{n \geq 1} \operatorname{Sp} K\langle X/n\rangle$, the increasing union of the closed discs of radius growing without bound. The covering by the discs is admissible, and $\mathbb{A}^{1,\mathrm{rig}}$ is a rigid space which is not affinoid. Similarly $\mathbb{A}^{n,\mathrm{rig}}$ is the union of the polydiscs of all radii.

**Example (the open disc).** The **open unit disc** $D^1_< = \{x : \lvert x \rvert < 1\} = \bigcup_{r < 1} \operatorname{Sp} K\langle X/r\rangle$, the union over $r \in \lvert K^\times \rvert$ with $r < 1$, is an admissible open subset of the closed disc and is not quasi-compact. It is a rigid space, and it is not affinoid. The contrast with the Archimedean disc is one of the standard illustrations of the theory.

**Example (annuli).** For $t \in K^\times$ with $\lvert t \rvert < 1$ the algebra $K\langle X, Y\rangle/(XY - t)$ is affinoid, and its spectrum is the **annulus** $\lvert t \rvert \leq \lvert x \rvert \leq 1$. Annuli are the building blocks of the theory of curves over $K$, and they also exhibit the failure of the "disc is simply connected" picture: an annulus is not the union of its two boundary discs, and its structure sheaf has the expected restrictions.

**Example (the rigid projective line).** $\mathbb{P}^{1,\mathrm{rig}}$ is obtained by gluing $\operatorname{Sp} K\langle X\rangle$ and $\operatorname{Sp} K\langle Y\rangle$ along the Laurent domain $\operatorname{Sp} K\langle X, Y\rangle/(XY - 1)$, which is the annulus $\lvert x \rvert = 1$. The result is a proper rigid space, and it contains the affine line together with the point at infinity.

### Coherent Sheaves and Kiehl's Theorem

**Definition.** Let $X$ be a rigid space. An $O_X$-module $\mathcal{F}$ is **coherent** if it is a sheaf for the G-topology and if there is an admissible covering by affinoids $\operatorname{Sp} A_i$ on which $\mathcal{F}$ is the sheaf associated to a finitely generated $A_i$-module.

**Theorem (Kiehl).** Let $X = \operatorname{Sp} A$ be an affinoid space. The functor $\mathcal{F} \mapsto \mathcal{F}(X)$ is an equivalence between the category of coherent $O_X$-modules and the category of finitely generated $A$-modules. Moreover $H^q(X, \mathcal{F}) = 0$ for every coherent $\mathcal{F}$ and every $q > 0$, and the cohomology of a coherent sheaf on an admissible open $U$ is that of the corresponding module over the affinoid algebra of $U$.

**Proof.** The statement is Kiehl's theorem; the sheaf-theoretic part is Tate's acyclicity theorem applied to the associated modules, and the equivalence is by the same division arguments that prove the structure theorem for affinoid algebras. The higher cohomology vanishes because the coverings in the weak G-topology are finite and acyclic and the associated module is finitely presented; the proofs are standard. $\square$

**Corollary.** On a rigid space the coherent sheaves form an abelian category, kernels, images and cokernels of morphisms of coherent sheaves are coherent, and the support of a coherent sheaf is a closed analytic subset.

**Proof.** The equivalence of Kiehl's theorem transfers the abelian category structure from finitely generated modules over the affinoid algebras, and closedness of supports is the corresponding algebraic statement. $\square$

---

## GAGA and Formal Models

### The GAGA Principle

**Theorem (GAGA; Kiehl, Köpf).** Let $X$ be a projective algebraic variety over $K$ and let $X^{\mathrm{an}}$ be its **analytification**, obtained by gluing the affinoid spaces associated to an affine cover of $X$. Then analytification induces an equivalence of categories

$$
\operatorname{Coh}(X) \xrightarrow{\ \sim\ } \operatorname{Coh}(X^{\mathrm{an}}),
$$

and for projective $X$ the analytification functor is fully faithful, $\operatorname{Hom}(X, Y) \cong \operatorname{Hom}(X^{\mathrm{an}}, Y^{\mathrm{an}})$ for projective $X$ and $Y$. In particular the coherent sheaves on $X^{\mathrm{an}}$, its closed analytic subsets and its finite étale covers are all algebraic.

**Proof.** The theorem is Kiehl's GAGA for rigid analytic spaces, proved first in the projective case and extended by Köpf to proper rigid spaces and proper families. It is proved by reduction to the affine statements: on an affine variety the analytification of a coherent sheaf is the completion of the algebraic module, and the comparison is an equivalence by the flatness of the completion; the global statement follows by the theory of coherent sheaves on the projective space and a descending induction on the dimension, exactly parallel to the algebraic GAGA of Serre. It is quoted here as a standard theorem of rigid analytic geometry. $\square$

**Remark.** GAGA is the first of the comparison theorems that relate the non-Archimedean analytic geometry to algebraic geometry, and it belongs to this Part because it is a statement about the topology of the analytification, not about any analytic operation. The corresponding statements for the étale fundamental group and for higher direct images are also standard.

### Formal Models

**Theorem (Raynaud).** Let $R$ be the valuation ring of $K$, viewed as a formal scheme with the $\mathfrak{m}$-adic topology, and write $\mathfrak{X}$ for a formal $R$-scheme of finite type. Then the category of quasi-compact and quasi-separated rigid analytic spaces over $K$ is equivalent to the category of formal $R$-schemes of finite type localised at the admissible blow-ups: the rigid space is the **generic fibre** $\mathfrak{X}_K$ of the formal scheme, and two formal schemes with the same generic fibre differ by an admissible blow-up.

**Pro.** Raynaud's theorem identifies a rigid space with its formal model and shows that the passage to the generic fibre is a localisation; the proof proceeds by constructing a formal model from an admissible affinoid covering and checking that admissible blow-ups do not change the generic fibre. It is quoted here as the standard comparison; the theory of formal schemes itself is the subject, where the completion and the $I$-adic topology of *Topological Rings and Fields* supply the foundations. $\square$

**Remark.** Raynaud's theorem explains why the rigid topology is the natural one: the admissible blow-ups of a formal model are the formal counterpart of the admissible coverings of the rigid space. The Berkovich approach to the same geometry, which replaces the Grothendieck topology by an honest topological space of seminorms, is treated; the adic approach that unifies both is not covered here.

---

## Summary

Tate's **rigid analytic geometry** is the geometry of a complete non-Archimedean field built from the **Tate algebra** $K\langle X_1, \dots, X_n\rangle$ of power series whose coefficients tend to $0$, with the **Gauss norm** $\lVert f \rVert_G = \max_\alpha \lvert a_\alpha \rvert$. This algebra is a commutative $K$-Banach algebra with a multiplicative norm, its unit ball is the subring $\mathcal{O}\langle X\rangle$, and it is Noetherian and factorial; the two structural results are the Weierstrass division and preparation theorems, which reduce questions about series to questions about monic polynomials over the coefficient algebra. An **affinoid algebra** is a quotient of a Tate algebra, its **spectrum** $\operatorname{Sp} A$ is the space of its maximal ideals, and the **maximum modulus principle** identifies the spectral norm with the Gauss norm and asserts that the supremum is attained; this is the replacement for the Cauchy integral formula.

The rigid structure on $\operatorname{Sp} A$ is a **Grothendieck topology**: the admissible opens are the finite unions of rational subdomains, the admissible covers satisfy the Tate condition, and the affinoid subdomains — Weierstrass, Laurent and rational domains — are the basic pieces. **Tate's acyclicity theorem** says that the structure presheaf is a sheaf on this site and that the higher cohomology of the structure sheaf vanishes on affinoids. A **rigid analytic space** is a G-ringed space locally isomorphic to an affinoid space; the closed disc, the rigid affine line as the increasing union of its discs, the open disc, the annuli and the rigid projective line are the standard examples. **Kiehl's theorem** identifies coherent sheaves on an affinoid with finitely generated modules and gives their acyclicity, and **GAGA** identifies the coherent sheaves on the analytification of a projective variety with the algebraic ones.

The constructions above are geometric: they use the valuation only through the norm and the residue field, and the valuation theory is that of *Absolute Values, Valuations and Completions* and *Local Fields*. The non-Archimedean analysis on the resulting spaces, the theory of the integral and of differential equations, belongs to Part III; the formal models of rigid spaces are treated elsewhere, as are the seminorm-theoretic approach and the unified theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | A complete non-Archimedean field, algebraically closed for the geometric statements |
| $\lvert \cdot \rvert$ | The absolute value of $K$ |
| $\mathcal{O}$, $\mathfrak{m}$, $k$ | Valuation ring, maximal ideal and residue field of $K$ |
| $K\langle X_1, \dots, X_n\rangle$ | The Tate algebra of series with coefficients tending to $0$ |
| $\lVert f \rVert_G$ | The Gauss norm, $\max_\alpha \lvert a_\alpha \rvert$ |
| $\mathcal{O}\langle X_1, \dots, X_n\rangle$ | The unit ball of the Tate algebra |
| $A$ | An affinoid algebra, a quotient of a Tate algebra |
| $\lVert f \rVert$ | The residue norm on an affinoid algebra |
| $\lvert f \rvert_{\mathrm{sup}}$ | The spectral seminorm, $\sup_{x \in \operatorname{Sp} A} \lvert f(x) \rvert$ |
| $\operatorname{Sp} A$ | The affinoid space of maximal ideals (spectrum) of $A$ |
| $X(f_1, \dots, f_r)$ | Weierstrass domain $\{\lvert f_i \rvert \leq 1\}$ |
| $X(f_1, \dots, f_r; g_1, \dots, g_s)$ | Laurent domain $\{\lvert f_i \rvert \leq 1, \lvert g_j \rvert \geq 1\}$ |
| $X(f_1, \dots, f_r/g)$ | Rational domain $\{\lvert f_i \rvert \leq \lvert g \rvert\}$ |
| $O_X$ | The structure sheaf for the rigid (G-)topology |
| $H^q(U, O_X)$ | Higher cohomology of the structure sheaf, vanishing on affinoids |
| $\mathbb{A}^{n,\mathrm{rig}}$, $\mathbb{P}^{1,\mathrm{rig}}$ | The rigid affine and projective spaces |
| $X^{\mathrm{an}}$ | Analytification of an algebraic variety |
| $\operatorname{Coh}(X)$ | The category of coherent sheaves on $X$ |
| $\mathfrak{X}$, $\mathfrak{X}_K$ | A formal $R$-model and its generic fibre (Raynaud) |





## Further Reading

- John Tate, "Rigid analytic spaces", *Inventiones Mathematicae* **12** (1971), 257–289, for the original construction, the Tate algebra and the acyclicity theorem.
- Siegfried Bosch, *Lectures on Formal and Rigid Geometry* (Springer, 2014), for a systematic development of affinoid algebras, the rigid topology and rigid spaces.
- Siegfried Bosch, Ulrich Güntzer and Reinhold Remmert, *Non-Archimedean Analysis* (Springer, 1984), for the foundations of the Tate algebra, the Weierstrass theorems and the maximum modulus principle.
- Jean Fresnel and Marius van der Put, *Rigid Analytic Geometry and its Applications* (Birkhäuser, 2004), for rigid spaces, coherent sheaves and the comparison theorems.
- Reinhardt Kiehl, "Theorem A und Theorem B in der nichtarchimedischen Funktionentheorie", *Inventiones Mathematicae* **2** (1967), 256–273, for the coherent sheaf theory on rigid spaces.
- Michel Raynaud, "Géométrie analytique rigide d'après Tate, Kiehl, …", *Mémoires de la Société Mathématique de France* **39–40** (1974), 319–327, for the formal-model point of view.
- Ulrich Köpf, "Über eigentliche Familien algebraischer Varietäten über affinoiden Räumen", *Schriftenreihe des Mathematischen Instituts der Universität Münster* **7** (1974), for the rigid GAGA theorem.
- Hans Grauert and Reinhold Remmert, *Coherent Analytic Sheaves* (Springer, 1984), for the classical comparison theorems that the rigid GAGA parallels.
