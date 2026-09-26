
# __Poisson and Gerstenhaber Algebras__

## Introduction

A **Poisson algebra** is a commutative associative algebra $A$ over a field $k$ equipped with a Lie bracket $\{\,,\,\}$ on the underlying $k$-module that is a **derivation** in each variable,

$$
\{f,gh\} = \{f,g\}h+g\{f,h\},
$$

so that the two structures — the commutative multiplication and the bracket — are tied by the Leibniz rule. A **Gerstenhaber algebra** is the graded form of the same data: a graded-commutative algebra $A^\bullet$ with a bracket of degree $-1$ that is graded antisymmetric, satisfies the graded Jacobi identity, and is a graded derivation of the product in each variable. The two notions are the same structure read in degree zero and in arbitrary degree, and both arise from the same source: the **Hochschild cohomology** of an associative algebra carries a graded-commutative product and a bracket of degree $-1$, and a Poisson structure on an algebra $A$ is a class in the second Hochschild cohomology of $A$ with square zero under that bracket.

The article is the twentieth of the corpus, in the category *Anti-symmetric Linear Algebras*, and it closes the Lie-theoretic development of the category. It follows *Graded Lie Algebras and Lie Superalgebras* and it uses the Lie algebras of the category for its principal examples: the bracket of a Poisson algebra is a Lie algebra structure on an associative algebra, the bracket of a Gerstenhaber algebra is a Lie-algebra-like structure of degree $-1$, and the **Poisson cohomology** is the cohomology of the complex of derivations with the differential given by the bracket with the Poisson bivector, in the form of *Lie Algebra Cohomology*. The article develops the definition and the examples of a Poisson algebra, the description of a Poisson structure by a bivector with the **Schouten–Nijenhuis bracket** and the condition of vanishing square, the Poisson cohomology with the interpretations of its low degrees, the **Gerstenhaber algebra** of the Hochschild cohomology with the cup product and the Gerstenhaber bracket, the **deformation** theory of an associative algebra and the sense in which a Poisson bracket is the semi-classical limit of a formal deformation, the **Batalin–Vilkovisky** algebras and the cyclic structures relating the bracket to an operator of square zero, and the **Poisson vertex algebras** in which the bracket is parametrised by a formal variable in the sense of *Vertex Algebras*.

The article keeps to the algebraic side. The Poisson bracket attached to a **symplectic form**, the symplectic and Poisson manifolds, the Darboux normal form, the Poisson geometry of a manifold and the classification of the Poisson structures by the forms are the subject of Part II, where the form and the manifold are available; the bracket on the algebra of functions of a symplectic space, its derivation properties and the Jacobi identity are developed there and are only referred to here, and the deformation quantisation of a Poisson manifold, the formality theorem on the polynomial algebra over the real numbers and the analytic convergence of the star products are deferred to Parts II and III. What is developed here is the algebraic theory of the structures themselves, together with the Lie–Poisson example on the symmetric algebra of a Lie algebra, which uses no form and no manifold.

Throughout, $A$ is a commutative associative $k$-algebra with unit, $\{\,,\,\}$ is a Poisson bracket, $\pi$ is a Poisson bivector, $\Lambda^\bullet\operatorname{Der}(A)$ is the graded algebra of the alternating polyderivations with the **Schouten–Nijenhuis bracket** $[\,,\,]_{SN}$ of degree $-1$, $H^\bullet_\pi(A)$ is the Poisson cohomology, $HH^\bullet(A,A)$ is the Hochschild cohomology with the cup product $\smile$ and the **Gerstenhaber bracket** $[\,,\,]_G$ of degree $-1$, $A[[t]]$ is the algebra of formal power series with the deformation parameter $t$, and $\Delta$ is the Batalin–Vilkovisky operator.

## Poisson Algebras

**Definition.** A **Poisson algebra** over $k$ is a $k$-algebra $A$ with a commutative associative multiplication, a unit $1$, and a $k$-bilinear map $\{\,,\,\}:A\times A\to A$ such that:

1. $\{\,,\,\}$ is a Lie bracket: it is alternating, $\{f,f\} = 0$, and satisfies the Jacobi identity $\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\} = 0$;
2. the **Leibniz rule** $\{f,gh\} = \{f,g\}h+g\{f,h\}$ holds for all $f,g,h\in A$;
3. $\{f,1\} = 0$ for all $f$, which follows from the Leibniz rule when the bracket is alternating.

A **morphism of Poisson algebras** is an algebra homomorphism preserving the bracket, and a **Poisson subalgebra** is a subalgebra closed under the bracket.

**Example (the polynomial algebra).** Let $A = k[x_1,\dots,x_n]$ with the bracket determined by the values $\{x_i,x_j\} = \pi_{ij}(x)$ and extended by the Leibniz rule,

$$
\{f,g\} = \sum_{i,j}\pi_{ij}\,\frac{\partial f}{\partial x_i}\frac{\partial g}{\partial x_j},
$$

where the $\pi_{ij}$ are the entries of a skew-symmetric matrix of elements of $A$. The Jacobi identity for the bracket is equivalent to the single condition

$$
\sum_{i,j,l}\Bigl(\pi_{il}\frac{\partial\pi_{jk}}{\partial x_l}+\pi_{jl}\frac{\partial\pi_{ki}}{\partial x_l}+\pi_{kl}\frac{\partial\pi_{ij}}{\partial x_l}\Bigr) = 0
$$

for all $i,j,k$, which is the vanishing of the **Schouten–Nijenhuis bracket** $[\pi,\pi]_{SN} = 0$ of the next section; the bracket is thus determined by the bivector $\pi = \sum_{i<j}\pi_{ij}\partial_i\wedge\partial_j$, and the condition is a system of quadratic differential equations on the coefficients.

**Example (the Lie–Poisson structure).** Let $\mathfrak{g}$ be a finite-dimensional Lie algebra over $k$ with basis $x_1,\dots,x_n$ and structure constants $[x_i,x_j] = \sum_kc^k_{ij}x_k$, and let $A = \operatorname{Sym}(\mathfrak{g}) = k[\xi_1,\dots,\xi_n]$ be the symmetric algebra of *The Symmetric Algebra* on the underlying space, the variables $\xi_i$ being the images of the basis. Define

$$
\{\xi_i,\xi_j\} = \sum_kc^k_{ij}\xi_k, \qquad \{f,g\} = \sum_{i,j,k}c^k_{ij}\,\xi_k\,\frac{\partial f}{\partial\xi_i}\frac{\partial g}{\partial\xi_j},
$$

the second display being the extension of the first by the Leibniz rule. Then $A$ is a Poisson algebra, the **Lie–Poisson** or Kirillov–Kostant–Souriau structure on $\operatorname{Sym}(\mathfrak{g})$: the Leibniz rule holds by construction, the alternating property holds because the $c^k_{ij}$ are alternating, and the Jacobi identity for the bracket is a consequence of the Jacobi identity for the structure constants. For the Heisenberg algebra with basis $p,q,z$ and $[p,q] = z$ the bracket $\{F,G\} = \xi_z(\partial_pF\partial_qG-\partial_qF\partial_pG)$ satisfies the Jacobi identity and the Leibniz rule; this was verified by explicit computation of the bracket of monomials, for all triples of the monomials $p,q,z,1$ and for products of them, with the exact rational arithmetic of the coefficients, together with $\{p,q\} = z$ and the alternating property. The Poisson structure depends on the Lie algebra structure only: no form, no dual space and no manifold enters, and the bracket is the algebraic source of the Kac–Moody and the affine structures of *Vertex Algebras*.

**Example (the trivial structure).** Every commutative associative algebra is a Poisson algebra with $\{f,g\} = 0$. In particular the Poisson bracket is not symmetric in its arguments: the structures of interest are exactly those in which the bracket is non-trivial, and the Poisson algebras form a full subcategory of the algebras with an additional Lie structure.

**Proposition.** Let $A$ be a Poisson algebra. Then the bracket is a derivation in each variable, and the **Hamiltonian** assignment $f\mapsto \mathrm{ad}_f = \{f,-\}$ is a Lie algebra homomorphism from $(A,\{\,,\,\})$ to the Lie algebra $\operatorname{Der}(A)$ of derivations of the commutative algebra $A$; the **Casimir** or central elements of the Poisson structure are the elements $f$ with $\{f,g\} = 0$ for all $g$, and they form a Poisson subalgebra of $A$.

*Proof.* The Leibniz rule in the second variable and the alternating property give it in the first; the Jacobi identity says that $\mathrm{ad}_f$ is a derivation of the bracket and the Leibniz rule says that it is a derivation of the product, so that $\mathrm{ad}_f\in\operatorname{Der}(A)$, and the Jacobi identity also says that $f\mapsto\mathrm{ad}_f$ is a Lie algebra homomorphism. The central elements are the kernel of this homomorphism and are closed under the product and the bracket. $\square$

**Remark (the relation to the Lie algebras of the category).** A Poisson algebra is a Lie algebra object in the category of commutative algebras: the bracket is a Lie bracket (the antisymmetric structure of the category) and the Leibniz rule says that it is compatible with the commutative multiplication. The Poisson algebras therefore sit in the present category exactly as the Lie algebras of *Lie Algebras* sit in it, and the two structures are related by the forgetful functor: from a Poisson algebra one recovers a Lie algebra by forgetting the multiplication, and from a Lie algebra $\mathfrak{g}$ one recovers a Poisson algebra by passing to $\operatorname{Sym}(\mathfrak{g})$, the construction of the previous example. The symmetric algebra is thus the free commutative algebra carrying a Poisson structure compatible with the bracket of $\mathfrak{g}$.

## Poisson Bivectors and the Schouten–Nijenhuis Bracket

**Definition.** Let $A$ be a commutative $k$-algebra. A **polyderivation** of degree $p$ is a $k$-multilinear map $A^{\times p}\to A$ that is a derivation in each variable; the polyderivations form a graded algebra

$$
\Lambda^\bullet\operatorname{Der}(A) = \bigoplus_{p\geq0}\Lambda^p_A\operatorname{Der}(A),
$$

the **alternating** polyderivations, and for $A = k[x_1,\dots,x_n]$ this is the exterior algebra over $A$ on the derivations $\partial_i$, with $\Lambda^0 = A$ and $\Lambda^1 = \operatorname{Der}(A)$.

**Definition.** The **Schouten–Nijenhuis bracket** on $\Lambda^\bullet\operatorname{Der}(A)$ is the unique graded bracket of degree $-1$

$$
[\,,\,]_{SN}:\Lambda^p\operatorname{Der}(A)\times\Lambda^q\operatorname{Der}(A)\longrightarrow\Lambda^{p+q-1}\operatorname{Der}(A)
$$

that is graded antisymmetric, graded derivation in each variable with respect to the exterior product, and that extends the commutator of derivations for $p = q = 1$ and the action on $A$ for $p = 1$, $q = 0$; it satisfies the graded Jacobi identity, so that $\Lambda^\bullet\operatorname{Der}(A)$ is a **Gerstenhaber algebra** in the sense of the next-but-one section.

**Theorem.** Let $A$ be a commutative $k$-algebra and $\pi\in\Lambda^2\operatorname{Der}(A)$ a bivector. The formula

$$
\{f,g\} = \pi(df\wedge dg)
$$

defines a Poisson bracket on $A$ if and only if $[\pi,\pi]_{SN} = 0$; the bracket is the skew-symmetrisation of a biderivation and the condition is the Jacobi identity, which for the bracket of the displayed form is equivalent to the vanishing of the Schouten–Nijenhuis square of the bivector.

*Proof.* The Leibniz rule is automatic from the definition of a polyderivation, since $\pi(df\wedge d(g h)) = \pi(df\wedge g\,dh)+\pi(df\wedge h\,dg)$ gives $\{f,gh\} = \{f,g\}h+g\{f,h\}$. For the Jacobi identity, the sum $\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}$ is a trilinear alternating expression in the differentials, hence a trivector, and its vanishing for all $f,g,h$ is exactly the vanishing of $[\pi,\pi]_{SN}$, computed in the coordinates of the previous section as the displayed quadratic condition. $\square$

**Corollary.** A Poisson structure on $A$ with $A = k[x_1,\dots,x_n]$ is a bivector $\pi = \sum_{i<j}\pi_{ij}\partial_i\wedge\partial_j$ with $[\pi,\pi]_{SN} = 0$; the linear bivectors $\pi_{ij}\in k$ correspond to the Lie–Poisson structures of nilpotent type and give the constant Poisson structures, the structures with the $\pi_{ij}$ constant on the algebra; the non-linear bivectors give the genuinely curved Poisson structures, whose study through the forms of Part II is the subject of the Poisson geometry deferred there.

## Poisson Cohomology

**Definition.** Let $A$ be a Poisson algebra with bracket defined by the bivector $\pi\in\Lambda^2\operatorname{Der}(A)$. The **Poisson complex** is the complex of graded $k$-modules

$$
\cdots\longrightarrow\Lambda^{p}\operatorname{Der}(A)\xrightarrow{\ d_\pi\ }\Lambda^{p+1}\operatorname{Der}(A)\longrightarrow\cdots, \qquad d_\pi = [\pi,-\;]_{SN},
$$

and the **Poisson cohomology** is $H^\bullet_\pi(A) = \ker d_\pi/\operatorname{im}d_\pi$; the differential satisfies $d_\pi^2 = 0$ by the graded Jacobi identity of the Schouten–Nijenhuis bracket and the condition $[\pi,\pi]_{SN} = 0$.

**Proposition.** The low degrees of the Poisson cohomology have the following interpretations:

1. $H^0_\pi(A)$ is the algebra of **Casimir** elements, the elements $f\in A$ with $\{f,-\} = 0$;
2. $H^1_\pi(A)$ is the space of the **Poisson derivations** of $A$ modulo the Hamiltonian ones, that is the derivations $D$ of the commutative algebra with $D\{f,g\} = \{Df,g\}+\{f,Dg\}$ modulo the derivations $\mathrm{ad}_f$;
3. $H^2_\pi(A)$ classifies the **infinitesimal deformations** of the Poisson structure $\pi$, that is the bivectors $\pi+t\pi_1$ over $k[t]/(t^2)$ whose Schouten–Nijenhuis square vanishes modulo $t^2$;
4. $H^3_\pi(A)$ carries the obstructions to extending such an infinitesimal deformation to higher order.

*Proof.* The complex is the Schouten–Nijenhuis complex twisted by the bivector, and the identifications are the standard ones of deformation theory: a one-cochain is a derivation, a cocycle is a Poisson derivation and a coboundary is Hamiltonian; a two-cochain is a bivector, a cocycle is the first-order condition for the deformation $\pi+t\pi_1$ to be Poisson, and a coboundary is the change of $\pi_1$ produced by a change of the coordinates. $\square$

**Remark (the relation to Lie algebra cohomology).** For the linear Lie–Poisson structure on $\operatorname{Sym}(\mathfrak{g})$ the Poisson complex is the complex computing the cohomology of the Lie algebra $\mathfrak{g}$ with coefficients in the symmetric algebra with its induced module structure, and the Poisson cohomology of the linear structure coincides with that Lie algebra cohomology; this is the precise sense in which the cohomology of *Lie Algebra Cohomology* is the linear case of the Poisson cohomology, and it is the algebraic statement whose geometric form, the identification of the Poisson cohomology with the de Rham cohomology of the symplectic leaves, belongs to Part II.

## Gerstenhaber Algebras and the Hochschild Complex

**Definition.** A **Gerstenhaber algebra** over $k$ is a graded $k$-module $G^\bullet = \bigoplus_{n\geq0}G^n$ with:

1. a **graded-commutative product** $G^p\times G^q\to G^{p+q}$, $ab = (-1)^{pq}ba$, with unit in degree zero;
2. a **bracket** $[\,,\,]:G^p\times G^q\to G^{p+q-1}$ of degree $-1$ that is graded antisymmetric, $[a,b] = -(-1)^{(p-1)(q-1)}[b,a]$;
3. the **graded Jacobi identity** $(-1)^{(p-1)(r-1)}[a,[b,c]]+(-1)^{(q-1)(p-1)}[b,[c,a]]+(-1)^{(r-1)(q-1)}[c,[a,b]] = 0$;
4. the **graded Leibniz rule** $[a,bc] = [a,b]c+(-1)^{(p-1)q}b[a,c]$.

A Gerstenhaber algebra of degree zero, that is one concentrated in degrees $0$ and with the bracket on $G^0$, is a Poisson algebra; the shift of degree by one therefore exhibits the Poisson algebras as the degree-zero case and the Gerstenhaber algebras as the general one.

**Definition.** Let $A$ be an associative $k$-algebra with unit and $M$ an $A$-bimodule. The **Hochschild complex** has

$$
C^n(A,M) = \operatorname{Hom}_k(A^{\otimes n},M), \qquad (df)(a_1,\dots,a_{n+1}) = a_1f(a_2,\dots,a_{n+1})+\sum_{i=1}^{n}(-1)^if(a_1,\dots,a_ia_{i+1},\dots,a_{n+1})+(-1)^{n+1}f(a_1,\dots,a_n)a_{n+1},
$$

and its cohomology $HH^\bullet(A,M)$ is the **Hochschild cohomology**; the complex and its homology are the subject of the article *Hochschild Homology* of this Part, written in parallel, and the standard references are cited below.

**Theorem (Gerstenhaber, standard).** Let $A$ be an associative $k$-algebra. Then:

1. the cup product of Hochschild cochains makes $HH^\bullet(A,A)$ a graded-commutative algebra, $f\smile g = (-1)^{pq}g\smile f$, with unit the class of the multiplication;
2. the **Gerstenhaber bracket** — the graded bracket of degree $-1$ on the cochains defined by the graded commutator of the composition products of cochains — descends to a bracket of degree $-1$ on $HH^\bullet(A,A)$;
3. the descended bracket satisfies the graded Jacobi identity and the graded Leibniz rule with respect to the cup product,

so that $HH^\bullet(A,A)$ is a **Gerstenhaber algebra**; the bracket of two one-cocycles, that is of two derivations, is the commutator of the derivations, and the bracket of a one-cochain with a zero-cochain is the action of the derivation on the algebra.

**Example (the Hochschild–Kostant–Rosenberg identification).** For a polynomial algebra $A = k[x_1,\dots,x_n]$ over a field of characteristic zero the **Hochschild–Kostant–Rosenberg theorem** gives

$$
HH^\bullet(A,A)\cong\Lambda^\bullet\operatorname{Der}(A) = \Lambda^\bullet_A\bigl(\bigoplus_iA\,\partial_i\bigr),
$$

an isomorphism of Gerstenhaber algebras, the cup product corresponding to the exterior product and the Gerstenhaber bracket to the Schouten–Nijenhuis bracket; the isomorphism is the algebraic source of the identification of the Poisson cohomology of the previous section with the cohomology of the Hochschild-type complex, and it explains why the two brackets — the Schouten–Nijenhuis bracket of polyderivations and the Gerstenhaber bracket of Hochschild cochains — are the same bracket in the commutative case.

**Corollary.** Let $A$ be an associative algebra and $HH^2(A,A)$ its second Hochschild cohomology. An element $\pi\in HH^2(A,A)$ with $[\pi,\pi]_G = 0$, where $[\,,\,]_G$ is the Gerstenhaber bracket, is a **Poisson structure** on $A$ in the generalised sense of the theory: for a commutative $A$ these are the Poisson brackets of the first section, and for a noncommutative $A$ they are the structures whose double bracket vanishing is the condition for the associated deformation of the next section to exist.

## Deformations and the Semi-Classical Limit

**Definition.** A **formal deformation** of an associative $k$-algebra $A$ is a $k[[t]]$-bilinear product on $A[[t]]$ of the form

$$
a*b = ab+\sum_{n\geq1}t^n\mu_n(a,b), \qquad \mu_n:A\times A\to A,
$$

which is associative, with $\mu_0$ the given product; two deformations are **equivalent** if they are related by a $k[[t]]$-linear automorphism of $A[[t]]$ reducing to the identity modulo $t$. Suppose $A$ commutative; the **semi-classical bracket** of a deformation is

$$
\{a,b\} = \mu_1(a,b)-\mu_1(b,a),
$$

and the deformation is a **quantisation** of a Poisson structure when this bracket is a Poisson bracket on $A$.

**Theorem (Gerstenhaber, standard).** Let $A$ be an associative $k$-algebra and let $\mu_1$ be the first-order term of a formal deformation. Then the Hochschild differential applied to $\mu_1$ vanishes — the first-order associativity of the deformed product is exactly the condition that $\mu_1$ be a Hochschild two-cocycle — and if the deformation is a quantisation, its semi-classical bracket $\{a,b\} = \mu_1(a,b)-\mu_1(b,a)$ is a Poisson bracket; conversely, if a Poisson bracket $\{\,\,\}$ on a commutative $A$ is the semi-classical bracket of a deformation, the deformation is called a **deformation quantisation** of the bracket, and the obstruction to the existence of the deformation lies in the third Hochschild cohomology, in the sense of the deformation theory and of the article *Deformation Theory* in this corpus.

*Proof (outline).* Associativity of $*$ to first order in $t$ reads $a\mu_1(b,c)-\mu_1(ab,c)+\mu_1(a,bc)-\mu_1(a,b)c = 0$, which is the Hochschild cocycle condition for $\mu_1$; taking the alternating part of the identity and using the cocycle condition, the semi-classical bracket is seen to satisfy the Leibniz rule and the Jacobi identity, the latter being a restatement of the degree-three part of associativity: the associator of the deformed product is the Gerstenhaber bracket of $\mu_1$ with itself, and its vanishing to second order is the condition that the class of $\mu_1$ has square zero and extends. The obstructions to the extension to higher order are the successive products $[\mu_1,\mu_n]_G$, whose classes lie in $HH^3$, and the theory is the standard deformation theory of Gerstenhaber. $\square$

**Theorem (Kontsevich, standard).** Let $A = \mathbb{R}[x_1,\dots,x_n]$ be the polynomial algebra and let $\pi$ be a Poisson bivector with $[\pi,\pi]_{SN} = 0$. Then the Poisson structure defined by $\pi$ admits a deformation quantisation: a formal deformation of $A$ over $\mathbb{R}[[t]]$ whose semi-classical bracket is the bracket of $\pi$. The construction is given by an explicit formula, the formality quasi-isomorphism of the operad of little discs to the operad of the Poisson structures, and it produces the star products of the theory; the extension to a general Poisson manifold, and the analytic and convergence properties of the products, belong to Parts II and III, where the manifold and the limit are available, and the algebraic formality statement itself belongs to the homotopy theory of the operads, the subject of *Operads* and of *A-Infinity and L-Infinity Algebras* in this corpus.

**Example.** The antisymmetric part of the first-order term of the deformation of the symmetric algebra of a Lie algebra $\mathfrak{g}$ is the Lie–Poisson bracket of the first section; the deformation is the **universal enveloping algebra** $U(\mathfrak{g})$ itself, read as the quantisation of $\operatorname{Sym}(\mathfrak{g})$ along the Lie–Poisson structure: the Rees algebra of the degree filtration of $U(\mathfrak{g})$ is a deformation of $\operatorname{Sym}(\mathfrak{g})$ over $k[t]$, the associated graded is $\operatorname{Sym}(\mathfrak{g})$ by the Poincaré–Birkhoff–Witt theorem of *Universal Enveloping Algebras*, and the semi-classical bracket is the Lie–Poisson bracket, since the commutator $xy-yx$ in $U(\mathfrak{g})$ has order one and its leading term is $[x,y]$. This is the classical example of a quantisation, and its quantised product is the one whose commutator closes on $\mathfrak{g}$.

## Batalin–Vilkovisky Algebras and Cyclic Structures

**Definition.** A **Batalin–Vilkovisky algebra** over $k$ is a Gerstenhaber algebra $G^\bullet$ with an operator $\Delta:G^\bullet\to G^{\bullet-1}$ of degree $-1$ such that $\Delta^2 = 0$ and the bracket is recovered from $\Delta$ and the product by

$$
[a,b] = (-1)^{\lvert a\rvert}\bigl(\Delta(ab)-\Delta(a)b-(-1)^{\lvert a\rvert}a\,\Delta(b)\bigr);
$$

an operator with these properties is a **BV operator**, and it is a derivation of the bracket, $\Delta[a,b] = [\Delta a,b]+(-1)^{\lvert a\rvert}[a,\Delta b]$.

**Theorem (standard).** Let $A$ be a **Calabi–Yau algebra** of dimension $d$ in the sense of *Calabi–Yau Algebras*, that is an algebra with a non-degenerate trace on its Hochschild homology of degree $d$. Then the Hochschild cohomology $HH^\bullet(A,A)$ carries a Batalin–Vilkovisky algebra structure whose BV operator is the Connes operator transplanted through the Calabi–Yau structure, the product and the bracket being the cup product and the Gerstenhaber bracket; the BV operator pairs the Hochschild cohomology with the Hochschild homology, and in the commutative case $A = k[x_1,\dots,x_n]$ the operator is the divergence with respect to the volume form, so that the bracket is the Schouten bracket of the polyderivations. The cyclic structures relating the Hochschild and the cyclic homology of the same algebra, and the cyclic bicomplex, are the subject of the article *Cyclic Homology* of this Part, written in parallel.

*Proof (outline).* The Connes operator $B$ on the Hochschild complex is a degree $-1$ operator with $B^2 = 0$; the cyclic structure of the algebra, that is the invariance of the trace under cyclic permutations, identifies the Hochschild complex with its dual up to a shift, and the Calabi–Yau condition makes the identification compatible with the products, so that $B$ transcribed becomes an operator $\Delta$ on the Hochschild cohomology satisfying the BV identity. The divergence computation in the commutative case is the standard one and identifies the bracket with the Schouten–Nijenhuis bracket of the polyderivations, which is the Gerstenhaber bracket under the Hochschild–Kostant–Rosenberg isomorphism. $\square$

## Poisson Structures in the Parametrised Setting

**Definition.** A **Poisson vertex algebra** is a commutative vertex algebra $V$ in the sense of *Vertex Algebras*, with the multiplication $a_{(-1)}b$ commutative and associative, together with a $\lambda$-bracket $[a_\lambda b] = \sum_{n\geq0}\frac{\lambda^n}{n!}a_{(n)}b$ such that:

1. $[a_\lambda b]$ is a derivation of the commutative product in each variable, $[a_\lambda bc] = [a_\lambda b]c+b[a_\lambda c]$;
2. the bracket is skew-symmetric, $[a_\lambda b] = -[b_{-\lambda-T}a]$;
3. the **Jacobi identity** $[a_\lambda[b_\mu c]]-[b_\mu[a_\lambda c]] = [[a_\lambda b]_{\lambda+\mu}c]$ holds, an identity of formal series in $\lambda,\mu$;

so that the bracket is a Lie bracket in the parametrised sense with the derivation property, exactly as the bracket of a Poisson algebra is a Lie bracket with the derivation property in the unparametrised case.

**Proposition.** A Poisson vertex algebra is the parametrised form of a Poisson algebra: putting $\lambda = 0$ and taking the degree-zero part recovers a Poisson algebra, the bracket $[a_0b]$ reducing to the Poisson bracket of the zero-mode algebra, and the Jacobi identity reduces to the ordinary Poisson Jacobi identity; conversely, the symmetric algebra $\operatorname{Sym}(\mathfrak{g})$ with the Lie–Poisson structure is the zero-mode algebra of a Poisson vertex algebra whose $\lambda$-bracket is the constant bracket $[a_\lambda b] = \{a,b\}$, in which the higher modes vanish.

*Proof.* Setting $\lambda = 0$ kills the terms of positive degree in $\lambda$, and the three axioms reduce to the alternating property, the derivation rule and the Jacobi identity of a Poisson bracket; the converse is checked directly from the axioms, the higher modes being zero and the axiom 3 reducing to the Jacobi identity of the Lie–Poisson bracket. $\square$

**Remark (the place of the parametrised structures).** The parametrised bracket of the vertex algebras and the degree-$(-1)$ bracket of the Gerstenhaber algebras are two faces of one structure: a bracket whose identity is a Jacobi identity in a parameter. In the vertex case the parameter is the formal variable of the state-field correspondence and the product is the commutative product $a_{(-1)}b$; in the Gerstenhaber case the parameter is absent and the grading supplies the degree shift. The general framework of structures of this kind, in which the bracket is an operation of a given arity and the identities are assembled from the operations and their compositions, is the operadic framework of *Operads*, written in parallel; and the objects with a bracket of degree $1-d$ satisfying the Jacobi identity, which arise from the shifts of the present structures, are the **L-infinity** algebras of *A-Infinity and L-Infinity Algebras*, whose Maurer–Cartan equation is the condition of square zero that appeared here as $[\pi,\pi] = 0$.

## Summary

A **Poisson algebra** is a commutative associative algebra with a Lie bracket that is a derivation in each variable; a **Gerstenhaber algebra** is the same structure with a graded-commutative product and a bracket of degree $-1$, satisfying the graded Jacobi identity and the graded Leibniz rule, and a Poisson algebra is the degree-zero case. The principal algebraic example of a Poisson structure is the **Lie–Poisson** structure on the symmetric algebra $\operatorname{Sym}(\mathfrak{g})$ of a Lie algebra, $\{\xi_i,\xi_j\} = \sum_kc^k_{ij}\xi_k$ extended by the Leibniz rule, whose Jacobi identity and Leibniz rule were verified by explicit computation of the brackets of monomials for the Heisenberg algebra with basis $p,q,z$ and $[p,q] = z$. A Poisson structure on $A$ is a bivector $\pi\in\Lambda^2\operatorname{Der}(A)$ with $[\pi,\pi]_{SN} = 0$ under the **Schouten–Nijenhuis bracket**, the bracket being $\{f,g\} = \pi(df\wedge dg)$ and the condition being the Jacobi identity; the **Poisson cohomology** $H^\bullet_\pi(A)$ of the complex $(\Lambda^\bullet\operatorname{Der}(A),[\,\pi,-\;]_{SN})$ has $H^0$ the Casimirs, $H^1$ the Poisson derivations modulo the Hamiltonian ones, $H^2$ the infinitesimal deformations of the Poisson structure and $H^3$ the obstructions, and it reduces to the Lie algebra cohomology of *Lie Algebra Cohomology* for the linear structures. The **Hochschild cohomology** $HH^\bullet(A,A)$ of an associative algebra is a Gerstenhaber algebra, with the cup product, the **Gerstenhaber bracket** of degree $-1$, and the identification $HH^\bullet(k[x_1,\dots,x_n],k[x_1,\dots,x_n])\cong\Lambda^\bullet\operatorname{Der}(A)$ of the Hochschild–Kostant–Rosenberg theorem, under which the two brackets agree; a formal deformation $a*b = ab+\sum_nt^n\mu_n(a,b)$ has its first-order term a Hochschild two-cocycle, its **semi-classical bracket** $\mu_1(a,b)-\mu_1(b,a)$ a Poisson bracket, and its obstructions in $HH^3$, and the theorem of Kontsevich asserts that every Poisson structure on a polynomial algebra over the real numbers admits a **deformation quantisation**, the algebraic example being the passage from $\operatorname{Sym}(\mathfrak{g})$ to $U(\mathfrak{g})$. A **Batalin–Vilkovisky algebra** is a Gerstenhaber algebra with an operator $\Delta$ of degree $-1$, $\Delta^2 = 0$, whose failure to be a derivation measures the bracket; the Hochschild cohomology of a Calabi–Yau algebra of *Calabi–Yau Algebras* carries such a structure with the Connes operator as $\Delta$, and the commutative case gives the divergence. Finally, a **Poisson vertex algebra** is the parametrised form of the theory, with the commutative vertex algebra product, the $\lambda$-bracket and the Jacobi identity in the parameter, and it is the general framework referred to by *Vertex Algebras*. The symplectic and Poisson forms of Part II, the Poisson manifolds and the Poisson geometry, and the analytic theory of the star products of Part III, are deferred.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | commutative associative algebra carrying the structures |
| $\{\,,\,\}$ | Poisson bracket, a Lie bracket and a derivation in each variable |
| $\pi\in\Lambda^2\operatorname{Der}(A)$ | Poisson bivector, $\{f,g\} = \pi(df\wedge dg)$ |
| $[\,,\,]_{SN}$ | Schouten–Nijenhuis bracket of polyderivations, degree $-1$ |
| $c^k_{ij}$ | structure constants, Lie–Poisson structure on $\operatorname{Sym}(\mathfrak{g})$ |
| $H^\bullet_\pi(A)$, $d_\pi = [\pi,-\;]_{SN}$ | Poisson cohomology and its differential |
| $C^n(A,M)$, $HH^\bullet(A,A)$ | Hochschild complex and cohomology |
| $\smile$, $[\,,\,]_G$ | cup product and Gerstenhaber bracket, degree $-1$ |
| $HH^\bullet(k[x],k[x])\cong\Lambda^\bullet\operatorname{Der}(A)$ | Hochschild–Kostant–Rosenberg |
| $a*b = ab+\sum_nt^n\mu_n(a,b)$ | formal deformation |
| $\{a,b\} = \mu_1(a,b)-\mu_1(b,a)$ | semi-classical bracket of a deformation |
| $\Delta$, $\Delta^2 = 0$ | Batalin–Vilkovisky operator |
| $[a_\lambda b]$ | $\lambda$-bracket of a Poisson vertex algebra |



## Further Reading

- André Lichnerowicz, "Les variétés de Poisson et leurs algèbres de Lie associées", *Journal of Differential Geometry* **12** (1977), 253–300, for the Poisson cohomology and the Schouten–Nijenhuis complex.
- Murray Gerstenhaber, "The cohomology structure of an associative ring", *Annals of Mathematics* **78** (1963), 267–288, and "On the deformation of rings and algebras", *Annals of Mathematics* **79** (1964), 59–103, for the Hochschild complex, the Gerstenhaber bracket and the deformation theory.
- Maxim Kontsevich, "Deformation quantization of Poisson manifolds", *Letters in Mathematical Physics* **66** (2003), 157–216, for the formality theorem and the quantisation of the Poisson structures on the polynomial algebra.
- James D. Stasheff, "The intrinsic bracket on the deformation complex of an associative algebra", *Journal of Pure and Applied Algebra* **89** (1993), 231–235, for the operadic form of the Gerstenhaber bracket.
- Alexandre A. Kirillov, *Lectures on the Orbit Method* (American Mathematical Society, 2004), for the Lie–Poisson structure on the symmetric algebra and its cohomology.
- Mikhail Alexandrov, Albert Schwarz, Oleg Zaboronsky and Maxim Kontsevich, "The geometry of the master equation and topological quantum field theory", *International Journal of Modern Physics A* **12** (1997), 1405–1429, for the Batalin–Vilkovisky algebra and the operator of square zero.
- Bojko Bakalov and Victor G. Kac, "Field algebras", *International Mathematics Research Notices* **2003**, 123–159, for the Poisson vertex algebras and the parametrised Jacobi identity.
