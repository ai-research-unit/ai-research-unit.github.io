
# __p-adic Lie Groups__

## Introduction

A $p$-adic Lie group is a group with a manifold structure over the field $\mathbb{Q}_p$: a topological group $G$ with an atlas of charts into $\mathbb{Q}_p^n$ whose transition maps are given by convergent power series with $p$-adic coefficients. The theory is the analogue over a non-archimedean ground field of the theory of real Lie groups, and it is a theory of *totally disconnected* groups: the underlying space of a $p$-adic manifold has a basis of clopen sets, every compact $p$-adic Lie group has the structure of a profinite group, and the connected components are points. The analogue of the exponential map and of the Lie algebra remains, and it is more rigid than in the real case: the exponential series $\sum x^n/n!$ converges on the ball $v(x) > 1/(p-1)$ of the Lie algebra, the logarithm series converges on the corresponding neighbourhood of the identity, and the **Hausdorff series** turns the coset $\mathrm{img}(\exp)$ into a subgroup whose multiplication is given by a Lie-algebraic formula. Lazard's theory makes this into an equivalence of categories between the $p$-adic analytic groups and a class of Lie algebras over $\mathbb{Z}_p$, the **saturated** ones.

The subject has two faces. The first is the **Lie theory** over $\mathbb{Q}_p$: the exponential and the logarithm, the Lie algebra, the adjoint representation, the closed-subgroup theorem, and the Lie correspondence asserting that a morphism of $p$-adic Lie groups is determined by its differential and that every finite-dimensional $\mathbb{Q}_p$-Lie algebra is the Lie algebra of a $p$-adic Lie group. The second is the **pro-$p$ theory**: every compact $p$-adic analytic group contains an open subgroup that is a **uniformly powerful** pro-$p$ group, the uniform pro-$p$ groups are precisely the groups whose Hausdorff series gives a Lie algebra over $\mathbb{Z}_p$, and a finitely generated pro-$p$ group is $p$-adic analytic exactly when it has finite rank, equivalently when its subgroup growth is polynomial — the theorems of Lazard and of Lubotzky and Mann.

The $p$-adic Lie groups are the structure theory of the $p$-adic completions of the arithmetic groups: the groups $GL_n(\mathbb{Z}_p)$ and $SL_n(\mathbb{Z}_p)$, their congruence subgroups $1+p^kM_n(\mathbb{Z}_p)$, the automorphism groups of the $p$-adic lattices, and the Galois groups of the local fields, which are pro-$p$ groups of finite rank and therefore $p$-adic analytic. The article develops the analytic functions and manifolds over $\mathbb{Q}_p$, the exponential, the logarithm and the Hausdorff series, the Lie theory with the correspondence and the closed-subgroup theorem, the pro-$p$ theory with the powerful and uniform groups and the theorems of Lazard and Lubotzky–Mann, and the examples and applications, including the $p$-adic form of Hilbert's fifth problem. The input from above is the analytic manifold theory of the real case and the Lie correspondence of *Lie Groups* and *The Lie Correspondence and the Adjoint Representation*, the profinite and pro-$p$ group theory of *Profinite Groups and the Krull Topology*, the buildings and parahorics of *Bruhat–Tits Theory*, and the fifth-problem theory of *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*. The **$p$-adic analytic function**, the **$p$-adic manifold** and the **Hausdorff series** are defined in line, since the local fields are and no earlier article introduces them.

The boundary with Part III is the one fixed for this block. What is developed here is the metric and manifold structure, the Lie algebra, the exponential and the Hausdorff series (whose convergence is a statement about the $p$-adic metric and completeness), and the group theory of the pro-$p$ groups. What is deferred is the **analytic** theory: the Haar measure on the $p$-adic Lie group, the Iwasawa algebra $\mathbb{Z}_p[[G]]$ and its use as a completed group algebra, the $L^p$-spaces, the representation theory of the $p$-adic groups and their Hecke algebras, and the $p$-adic analysis of Part III. The **differentiation** is available only formally: the derivative of a power series is defined algebraically by the termwise rule, and any statement requiring the analytic derivative, the integral or a differential equation is deferred to Part III. The **$\mathrm{CAT}(0)$ buildings** attached to the $p$-adic groups are those of *Bruhat–Tits Theory*; the **Galois theory** of the local fields is that of *Galois Cohomology* and with this article. No physics is invoked.

## Analytic Functions and Manifolds over $\mathbb{Q}_p$

### Convergent Power Series

**Definition.** Let $\mathbb{Q}_p$ be the field of $p$-adic numbers with its non-archimedean absolute value $|\cdot|_p$ and valuation $v$, and let $x \in \mathbb{Q}_p$. A series $\sum_{n\geq0}a_nx^n$ with $a_n \in \mathbb{Q}_p$ **converges** at $x$ if the sequence of partial sums converges in the metric of $\mathbb{Q}_p$; when it converges at $x$ it converges absolutely and the value depends only on $x$. A function $f : U \to \mathbb{Q}_p$ on an open set $U$ is **analytic** at $a \in U$ if it is given by a convergent power series $\sum_n a_n(x-a)^n$ on a neighbourhood of $a$; it is analytic on $U$ if analytic at every point.

**Proposition (the convergence radius).** For a series $\sum_na_nx^n$ there is a well-defined **radius of convergence**

$$
R = \frac{1}{\limsup_n |a_n|_p^{1/n}} \in [0,\infty] ,
$$

the series converging for $|x|_p < R$ and diverging for $|x|_p > R$; the value at $|x|_p = R$ depends on the series. In the non-archimedean case convergence is governed by the terms: $\sum_na_nx^n$ converges if and only if $|a_nx^n|_p \to 0$.

**Proof sketch.** The radius formula and the convergence criterion are the standard properties of the $p$-adic absolute value and its non-archimedean triangle inequality $|a+b|_p \leq \max(|a|_p,|b|_p)$, under which a series converges exactly when its terms tend to $0$; the details are in *Metric, Uniform and Complete Spaces* for the metric part and in the standard literature for the $p$-adic part. $\square$

**Definition (the formal derivative).** The **derivative** of a convergent power series $f(x) = \sum_na_nx^n$ is the series $f'(x) = \sum_nna_nx^{n-1}$, defined by the termwise rule; it has the same radius of convergence as $f$, and the product and composition of analytic functions are analytic with the formal rules $(fg)' = f'g+fg'$ and $(f\circ g)' = (f'\circ g)g'$. This is a formal-algebraic definition; the analytic theory of the derivative, the mean value theorems and the differential equations are Part III.

### The Exponential and the Logarithm

**Theorem (convergence of $\exp$ and $\log$).** Let $x,y \in \mathbb{Q}_p$ and put $r = 1/(p-1)$ for $p$ odd and $r = 1$ for $p = 2$.

**(a)** The series $\exp(x) = \sum_{n\geq0}x^n/n!$ converges if and only if $v(x) > r$ and sets up a bijection of $\{x : v(x) > r\}$ onto $1+\{y : v(y) > r\}$ with inverse $\log(1+y) = \sum_{n\geq1}(-1)^{n+1}y^n/n$.

**(b)** The maps $\exp$ and $\log$ satisfy $\log(\exp x) = x$, $\exp(\log(1+y)) = 1+y$ on their domains and are isometries: $v(\exp x - 1) = v(x)$ and $v(\log(1+y)) = v(y)$.

**(c)** For $x,y$ with $v(x),v(y) > r$, the product $\exp(x)\exp(y)$ is $\exp$ of an element of $\mathbb{Q}_p$, namely the value of the **Hausdorff series**

$$
H(X,Y) = \log(\exp X\exp Y) = X + Y + \tfrac12[X,Y] + \tfrac1{12}[X,[X,Y]] + \tfrac1{12}[Y,[Y,X]] + \cdots
$$

evaluated at $(x,y)$, a series in the noncommuting variables $X,Y$ whose terms are iterated commutators and which converges in the $p$-adic topology on the ball $v > r$.

**Proof sketch.** The convergence of the exponential is governed by the $p$-adic valuation of $n!$, which is $v(n!) = (n-s_p(n))/(p-1)$ with $s_p$ the sum of the $p$-adic digits, so that $v(x^n/n!) = nv(x) - (n-s_p(n))/(p-1) \to \infty$ exactly when $v(x) > 1/(p-1)$; the same estimate for the logarithm gives the domain of $\log$, and the inverse identity is the formal identity of power series combined with the convergence. The Hausdorff series is the formal series in the free associative algebra satisfying $\exp(X)\exp(Y) = \exp(H(X,Y))$, whose terms are the iterated commutators of $X$ and $Y$; its convergence on the ball follows from the estimates of the terms by the $p$-adic valuations of the coefficients, which is the Baker–Campbell–Hausdorff theorem in the $p$-adic setting. The statements are standard and are quoted from the literature. $\square$

**Corollary.** On the ball $v(x) > 1/(p-1)$ the exponential transfers the multiplication of $\mathbb{Q}_p^\times$ to the Lie-algebraic operation $x \cdot y = H(x,y) = x+y+\tfrac12[x,y]+\cdots$ of the abelian Lie algebra $\mathbb{Q}_p$.

### $p$-adic Analytic Manifolds

**Definition.** A **$p$-adic analytic manifold** of dimension $n$ is a topological space $M$ together with an open cover $\{U_i\}$ and homeomorphisms $\varphi_i : U_i \to V_i$ onto open subsets $V_i \subseteq \mathbb{Q}_p^n$ such that the transition maps $\varphi_j\circ\varphi_i^{-1}$ are analytic on their domains; a **morphism** of $p$-adic manifolds is a continuous map that is analytic in the charts. A **$p$-adic Lie group** is a group object in this category: a group $G$ with the structure of a $p$-adic analytic manifold for which the multiplication $G\times G\to G$ and the inversion $G\to G$ are morphisms.

**Example.** The additive group $\mathbb{Q}_p^n$ is a $p$-adic Lie group of dimension $n$ with the trivial atlas; the multiplicative group $\mathbb{Q}_p^\times$ is a $p$-adic Lie group of dimension $1$ with the atlas given by the logarithm on the ball $v(x-1) > 1/(p-1)$ and the charts $x \mapsto x/p^k$ elsewhere; the groups $GL_n(\mathbb{Q}_p)$ and $GL_n(\mathbb{Z}_p)$ are $p$-adic Lie groups of dimension $n^2$, the second one compact and of dimension $n^2$ because the congruence subgroups $1+p^kM_n(\mathbb{Z}_p)$ are clopen and the local structure at the identity is that of $M_n(\mathbb{Z}_p) \cong \mathbb{Z}_p^{n^2}$.

## The Lie Theory over $\mathbb{Q}_p$

### The Lie Algebra

**Definition.** The **Lie algebra** of a $p$-adic Lie group $G$ is the tangent space $\mathfrak{g} = T_1G$, defined as the $\mathbb{Q}_p$-vector space of derivations at the identity in the sense of the formal derivative, equivalently the space of $\mathbb{Q}_p$-linear maps $D$ on the germs of analytic functions with $D(fg) = D(f)g(1)+f(1)D(g)$; the bracket is $[X,Y](f) = X(Y(f))-Y(X(f))$, and the exponential map $\exp : \mathfrak{g} \to G$, when it converges, is the local inverse of the logarithm. For $\mathbf{G}$ an algebraic group over $\mathbb{Q}_p$, the Lie algebra of $G = \mathbf{G}(\mathbb{Q}_p)$ is $\mathfrak{g} = \mathrm{Lie}(\mathbf{G})\otimes_{\mathbb{Q}_p}\mathbb{Q}_p$; for the algebraic group $GL_n$, the Lie algebra is $M_n$ with the commutator bracket, and for $SL_n$ the traceless matrices.

**Theorem (Lie correspondence over $\mathbb{Q}_p$).** Let $G$ be a $p$-adic Lie group with Lie algebra $\mathfrak{g}$.

**(a)** There is a neighbourhood $U$ of $0$ in $\mathfrak{g}$ and a neighbourhood $V$ of $1$ in $G$ such that $\exp : U\to V$ is an analytic bijection with inverse $\log$, and the Hausdorff series makes $\exp(U)$ a subgroup of $G$ when $U$ is chosen inside the ball of convergence.

**(b)** Every morphism $f : G\to H$ of $p$-adic Lie groups is analytic, and its differential $df : \mathfrak{g}\to\mathfrak{h}$ is a homomorphism of Lie algebras; the functor $G\mapsto\mathfrak{g}$ is faithful and, on the category of simply connected $p$-adic Lie groups, an equivalence onto the category of finite-dimensional $\mathbb{Q}_p$-Lie algebras. In particular every finite-dimensional Lie algebra over $\mathbb{Q}_p$ is the Lie algebra of a $p$-adic Lie group, unique up to isomorphism among the simply connected ones.

**(c)** (closed subgroup theorem) A closed subgroup $H$ of a $p$-adic Lie group $G$ is a $p$-adic Lie group, its Lie algebra is a subalgebra of $\mathfrak{g}$, and the quotient $G/H$ is a $p$-adic analytic manifold when $H$ is closed; the connected components of $G$ are the cosets of the identity component, and the identity component is open if $G$ is locally compact.

**Proof sketch.** The exponential and the logarithm are the inverses of the previous theorem, and the Hausdorff series gives the subgroup structure on a sufficiently small ball. The functoriality of the differential is the formal chain rule, and the reconstruction of the group from the Lie algebra is the exponential of the Lie algebra of the universal enveloping algebra: the Baker–Campbell–Hausdorff series defines a group structure on a neighbourhood of $0$, and it extends to the simply connected group by the standard argument of the Lie correspondence, here entirely within the $p$-adic analytic category. The closed subgroup theorem uses the logarithm to identify the Lie algebra of $H$ with the set of directions tangent to $H$. The statements are the theorems of Lazard and are quoted from the literature. $\square$

**Corollary (linearity and compactness).** Every compact $p$-adic Lie group is isomorphic to a closed subgroup of $GL_n(\mathbb{Z}_p)$ for some $n$; every $p$-adic Lie group has an open subgroup that is compact and, after passing to a further open subgroup, uniformly powerful in the sense below. Hence a compact $p$-adic Lie group is a profinite group and has a basis of neighbourhoods of the identity consisting of open subgroups.

## Pro-$p$ Groups and the Lazard Correspondence

### Profinite and Pro-$p$ Groups of Finite Rank

**Definition.** A **profinite group** is a compact Hausdorff totally disconnected topological group, equivalently an inverse limit of finite groups, and a **pro-$p$ group** is a profinite group that is an inverse limit of finite $p$-groups; the topology is the **profinite topology** of *Profinite Groups and the Krull Topology*. A profinite group has **finite rank** if there is an integer $d$ such that every closed subgroup can be generated by $d$ elements, and it has **polynomial subgroup growth** if the number $s_n(G)$ of open subgroups of index at most $n$ grows polynomially in $n$.

**Definition (powerful and uniform).** A pro-$p$ group $G$ is **powerful** if $[G,G]\leq G^{p}$ for odd $p$, respectively $[G,G]\leq G^{4}$ for $p = 2$, where the powers denote the closures of the subgroups generated by the corresponding powers; it is **uniform** if it is powerful, finitely generated, and $|G:G^p| = p^{d(G)}$ with $d(G)$ the minimal number of generators. A uniform pro-$p$ group is torsion-free and has a **uniform power structure**: the map $x\mapsto x^{p^n}$ is injective with image $G^{p^n}$, and $|G:G^{p^n}| = p^{nd(G)}$.

**Theorem (Lazard correspondence).** Let $G$ be a uniform pro-$p$ group with a minimal generating set $g_1,\dots,g_d$. Then every element of $G$ is uniquely $g_1^{a_1}\cdots g_d^{a_d}$ with $a_i \in \mathbb{Z}_p$, and on the free $\mathbb{Z}_p$-module $L = \mathbb{Z}_pg_1\oplus\cdots\oplus\mathbb{Z}_pg_d$ the **Hausdorff operations**

$$
x +_L y := H(x,y), \qquad [x,y]_L := \text{the degree-two part of } H(x,y) = \tfrac12(xy - yx)
$$

in the coordinates $g_i$ make $L$ a **powerful** $\mathbb{Z}_p$-Lie algebra — a free $\mathbb{Z}_p$-module of finite rank with $[L,L]\leq pL$ — and the maps $\exp$ and $\log$ identify $G$ with $(L,+_L)$ as groups: the group law of $G$ in the coordinates $g_i$ is the Lie-algebraic addition $H$. The construction is an equivalence of categories between the uniform pro-$p$ groups and the powerful $\mathbb{Z}_p$-Lie algebras.

**Proof sketch.** The uniform power structure makes the coordinates well behaved: every element of $G$ is uniquely of the form $g_1^{a_1}\cdots g_d^{a_d}$ with $a_i \in \mathbb{Z}_p$, and the structure constants of the multiplication in these coordinates are the coefficients of the Hausdorff series, which are rational numbers with denominators invertible on the ball; the identities $\exp(x)\exp(y) = \exp(H(x,y))$ and $\log(xy) = H(\log x,\log y)$ identify the two structures, and the hypothesis $[L,L]\le pL$ ensures the convergence of all the series involved. The correspondence is Lazard's and is quoted from the literature. $\square$

### The Analytic Pro-$p$ Groups

**Definition.** A pro-$p$ group $G$ is **$p$-adic analytic** if it has an open subgroup that is a uniform pro-$p$ group, equivalently if it has an open subgroup isomorphic to a closed subgroup of $GL_d(\mathbb{Z}_p)$ for some $d$.

**Theorem (Lazard; Lubotzky–Mann).** Let $G$ be a finitely generated pro-$p$ group. Then the following are equivalent:

**(a)** $G$ is $p$-adic analytic;

**(b)** $G$ has finite rank;

**(c)** $G$ has polynomial subgroup growth;

**(d)** $G$ contains an open subgroup that is uniform, hence an open subgroup isomorphic to a closed subgroup of $GL_d(\mathbb{Z}_p)$;

and in that case every open subgroup of $G$ is $p$-adic analytic, the rank of $G$ is bounded by a function of the dimension, and the dimension of the Lie algebra of an open uniform subgroup is the **dimension** of $G$.

**Proof sketch.** The implication (a) $\Rightarrow$ (b) is the theory of the $\mathbb{Z}_p$-Lie algebras: a uniform pro-$p$ group of dimension $d$ has all its closed subgroups generated by at most $d$ elements because the corresponding $\mathbb{Z}_p$-lattice is a free module of rank $d$ and the subalgebras of a free $\mathbb{Z}_p$-module of rank $d$ are free of rank at most $d$. The implication (b) $\Rightarrow$ (c) is the bound on the number of subgroups of given index in a finite-rank group, and (c) $\Rightarrow$ (a) is the hard direction of Lubotzky and Mann: a finitely generated pro-$p$ group of non-linear subgroup growth has a subgroup that is not $p$-adic analytic, detected by the structure theory of the finite $p$-groups and the Wilson–Zelmanov theory. The equivalence of (a) and (d) is Lazard's theorem on the existence of the uniform open subgroup. The results are quoted from the literature. $\square$

**Theorem (the Tits alternative for the linear groups).** A finitely generated subgroup of $GL_n(K)$ over a field $K$ of characteristic zero is either virtually solvable or contains a non-abelian free group. The alternative is stated in *Infinite Groups* in Part I, and it applies to the $p$-adic Lie groups through the corollary above: a compact $p$-adic Lie group embeds in some $GL_n(\mathbb{Z}_p)$, so a finitely generated subgroup of it is either virtually solvable or contains $F_2$. Consequently a finitely generated subgroup of a $p$-adic analytic group is either virtually solvable or contains $F_2$, hence is non-amenable in the sense of *Amenable Groups*.

**Theorem (linearity and commensurability).** Every compact $p$-adic Lie group is isomorphic to a closed subgroup of $GL_n(\mathbb{Z}_p)$ for some $n$; every open subgroup of a $p$-adic Lie group $G$ is a $p$-adic Lie group of the same dimension with the same Lie algebra, and two open subgroups are commensurable. Consequently a $p$-adic Lie group is determined up to commensurability by its $\mathbb{Q}_p$-Lie algebra: two $p$-adic Lie groups with isomorphic Lie algebras have commensurable open subgroups, and for a given finite-dimensional $\mathbb{Q}_p$-Lie algebra $\mathfrak{g}$ there is, up to commensurability, a unique $p$-adic Lie group with Lie algebra $\mathfrak{g}$, namely the group generated by $\exp(\mathfrak{g})$ in the simply connected group of the correspondence.

### $p$-adic Analytic Groups and the Fifth Problem

**Theorem (Lazard's $p$-adic fifth problem).** Let $G$ be a locally compact group that is totally disconnected and has **no small subgroups** — there is a neighbourhood $U$ of $1$ containing no nontrivial subgroup. Then $G$ is a $p$-adic Lie group with finitely many connected components, and conversely a $p$-adic Lie group has no small subgroups and is locally compact and totally disconnected. Consequently the locally compact totally disconnected groups that are Lie groups over a local field are exactly those without small subgroups, which is the $p$-adic form of the solution of Hilbert's fifth problem analysed in *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*.

**Proof sketch.** The theorem of Lazard reduces the problem to the structure of the compact open subgroups: a compact totally disconnected group without small subgroups is a compact $p$-adic Lie group by the theory of the pro-$p$ groups of finite rank and the uniformisation of their Lie algebras. The converse is immediate from the exponential coordinates. The statement is Lazard's and is quoted from the literature; the real case is the theorem of Gleason, Montgomery and Zippin discussed in *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*. $\square$

## Examples and Applications

### The Classical $p$-adic Lie Groups

**Example ($\mathbb{Q}_p^\times$ and $\mathbb{Z}_p^\times$).** The group $\mathbb{Q}_p^\times$ is a $1$-dimensional $p$-adic Lie group with Lie algebra $\mathbb{Q}_p$ and trivial bracket, the exponential $\exp$ mapping the ball $v(x)>1/(p-1)$ isomorphically onto a neighbourhood of $1$. For odd $p$ the unit group decomposes as

$$
\mathbb{Z}_p^\times \cong \mu_{p-1}\times(1+p\mathbb{Z}_p) \cong \mu_{p-1}\times\mathbb{Z}_p ,
$$

the factor $\mu_{p-1}$ being the group of Teichmüller roots of unity of order prime to $p$ and the second factor being torsion-free, parametrised by the logarithm; for $p = 2$ the corresponding decomposition is $\mathbb{Z}_2^\times \cong \{\pm1\}\times(1+4\mathbb{Z}_2)\cong\{\pm1\}\times\mathbb{Z}_2$. The $p$-adic Lie structure thus makes the arithmetic of the units a statement about a free $\mathbb{Z}_p$-module of rank $1$.

**Example ($GL_n$ and $SL_n$).** The groups $GL_n(\mathbb{Z}_p)$, $SL_n(\mathbb{Z}_p)$ and their congruence subgroups are compact $p$-adic Lie groups of dimensions $n^2$ and $n^2-1$; the congruence subgroups $\Gamma_k = 1+p^kM_n(\mathbb{Z}_p)$ are open, normal and form a basis of neighbourhoods of the identity, and for $k > 1/(p-1)$ the logarithm identifies $\Gamma_k$ with the $\mathbb{Z}_p$-lattice $p^kM_n(\mathbb{Z}_p)$ of the Lie algebra. For $k$ large enough the groups $\Gamma_k$ are uniform pro-$p$ groups, so the whole local structure of $GL_n(\mathbb{Z}_p)$ at the identity is that of the $\mathbb{Z}_p$-Lie algebra $M_n(\mathbb{Z}_p)$ with the commutator. The groups $GL_n(\mathbb{Q}_p)$ and $SL_n(\mathbb{Q}_p)$ are the $p$-adic Lie groups whose buildings and parahorics are those of *Bruhat–Tits Theory*: the Iwahori and parahoric subgroups are open compact $p$-adic Lie subgroups, and the Bruhat–Tits building records their incidences.

### Galois Groups of Local Fields

**Example (Demushkin groups).** Let $k$ be a finite extension of $\mathbb{Q}_p$ and let $k(p)$ be the maximal $p$-extension of $k$; the Galois group $G_k = \mathrm{Gal}(k(p)/k)$ is a pro-$p$ group of finite rank and is $p$-adic analytic, and it is a **Demushkin group**: a finitely generated pro-$p$ group of cohomological dimension $2$ whose cup product $H^1\times H^1\to H^2$ is nondegenerate. The Demushkin groups are classified by their number of generators together with an invariant of the duality, and the classification and the structure of the local Galois groups is due to Demushk, Labute and Serre; the analysis of $G_k$ is the local input to the Galois cohomology of *Galois Cohomology* and to the arithmetic.

**Remark (the failure of the real correspondence).** In contrast with the real case, the $p$-adic Lie groups are totally disconnected and their connected components are the group-theoretic cosets of the identity component, which is open; the "infinitesimal" neighbourhoods of the identity are the open subgroups, and there is no continuous curve connecting two points of different open subgroups. This is why the theory of the $p$-adic Lie groups is, in effect, the theory of the commensurability classes of the open compact subgroups, and why the buildings of *Bruhat–Tits Theory* carry the information that the connected component of the identity carries in the real case.

## The Boundary with Analysis

The theory of this article is metric, manifold-theoretic and group-theoretic; the analysis of the $p$-adic groups is Part III.

- The **Haar measure** on the $p$-adic Lie group, the **Iwasawa algebra** $\mathbb{Z}_p[[G]]$ as the completed group algebra, its structure as a ring and its use in the theory of the $p$-adic representations, the **Mahler expansions** and the **$p$-adic integration** are Part III, where the measure and the integral are available; the Haar measure itself is constructed in *Locally Compact Groups and Haar Measure* and used here only as a set function.
- The **representation theory** of the $p$-adic groups: the smooth and admissible representations, the Hecke algebras of the parahoric and Iwahori subgroups, the **Bernstein decomposition** of the category of the smooth representations, and the local Langlands correspondence are Part III and are built on the theory of the compact open subgroups developed here.
- The **$p$-adic analysis**: the rigid analytic spaces, the $p$-adic differential equations, the $p$-adic functional analysis and the $L^p$-spaces of a $p$-adic manifold are(Part II, below) and the $p$-adic analysis of Part III.
- What is *not* deferred: the $p$-adic analytic functions and manifolds; the exponential, the logarithm and the Hausdorff series with their convergence domains; the Lie algebra and the Lie correspondence with the closed-subgroup theorem; the pro-$p$ group theory, the powerful and uniform groups and the Lazard correspondence; the theorems of Lazard and Lubotzky–Mann on the analytic pro-$p$ groups; the $p$-adic fifth problem; and the classical examples and the Demushkin groups.

## Summary

A $p$-adic analytic manifold of dimension $n$ is a space with charts into $\mathbb{Q}_p^n$ and analytic transition maps, and a $p$-adic Lie group is a group object in that category. The formal derivative of a power series is defined termwise, and the analytic derivative itself is Part III. The exponential series $\sum x^n/n!$ converges on the ball $v(x)>1/(p-1)$ and the logarithm on the corresponding ball, they are mutually inverse isometries, and the Hausdorff series $H(X,Y) = X+Y+\tfrac12[X,Y]+\cdots$ gives the multiplication in exponential coordinates; the Lie algebra $\mathfrak{g}=T_1G$ and the differential of a morphism make $G\mapsto\mathfrak{g}$ a functor, which is an equivalence on the simply connected groups, and a closed subgroup of a $p$-adic Lie group is a $p$-adic Lie group with its Lie algebra a subalgebra.

Every compact $p$-adic Lie group embeds in some $GL_n(\mathbb{Z}_p)$ and contains an open **uniform** pro-$p$ subgroup: a finitely generated powerful pro-$p$ group with $|G:G^p| = p^{d(G)}$, on which the Hausdorff series makes $G$ isomorphic to a **powerful** $\mathbb{Z}_p$-Lie algebra — the Lazard correspondence between the uniform pro-$p$ groups and the powerful $\mathbb{Z}_p$-Lie algebras. For a finitely generated pro-$p$ group $G$, the conditions of being $p$-adic analytic, of having finite rank and of having polynomial subgroup growth are equivalent (Lazard, Lubotzky–Mann), and a locally compact totally disconnected group has no small subgroups exactly when it is a $p$-adic Lie group (Lazard's $p$-adic fifth problem). The examples are $\mathbb{Q}_p^\times \cong$ the units of $\mathbb{Z}_p$ with the Teichmüller factor and a free $\mathbb{Z}_p$-module, the groups $GL_n(\mathbb{Z}_p)$ and $SL_n(\mathbb{Z}_p)$ with their congruence subgroups, and the Demushkin groups $\mathrm{Gal}(k(p)/k)$ of the local fields. The Haar measure, the Iwasawa algebra, the representation theory and the $p$-adic analysis of these groups belong to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{Q}_p$, $v$, $\vert\cdot\vert_p$ | $p$-adic field, valuation, absolute value |
| $\sum a_nx^n$, radius $R$ | Convergent power series; convergence governed by $\vert a_nx^n\vert_p\to0$ |
| $f'$ | Formal derivative of a power series (analytic derivative: Part III) |
| $\exp$, $\log$ | Exponential and logarithm, convergent for $v > 1/(p-1)$ |
| $H(X,Y)$ | Hausdorff series $=\log(\exp X\exp Y)$, a series of iterated commutators |
| $p$-adic manifold, morphism | Charts into $\mathbb{Q}_p^n$, analytic transition maps |
| $p$-adic Lie group $G$ | Group object in the analytic manifolds over $\mathbb{Q}_p$ |
| $\mathfrak{g} = T_1G$, $[\,,\,]$ | Lie algebra of $G$; commutator bracket |
| $df : \mathfrak{g}\to\mathfrak{h}$ | Differential of a morphism of $p$-adic Lie groups |
| $\dim G$ | Dimension of the $p$-adic manifold $G$; $\dim GL_n = n^2$, $\dim SL_n = n^2-1$ |
| pro-$p$ group | Inverse limit of finite $p$-groups |
| finite rank | Bound on the minimal number of generators of every closed subgroup |
| powerful | $[G,G]\leq G^p$ (odd $p$); $[G,G]\leq G^4$ for $p=2$ |
| uniform pro-$p$ group | Powerful, finitely generated, $\vert G:G^p\vert = p^{d(G)}$ |
| $d(G)$ | Minimal number of generators |
| powerful $\mathbb{Z}_p$-Lie algebra $L$ | Free of finite rank over $\mathbb{Z}_p$ with $[L,L]\leq pL$ |
| Lazard correspondence | Uniform pro-$p$ groups $\leftrightarrow$ powerful $\mathbb{Z}_p$-Lie algebras |
| $\Gamma_k = 1+p^kM_n(\mathbb{Z}_p)$ | Congruence subgroups, a basis of neighbourhoods of $1$ |
| $\mu_{p-1}$ | Teichmüller roots of unity in $\mathbb{Z}_p^\times$ |
| Demushkin group | Pro-$p$ Galois group $\mathrm{Gal}(k(p)/k)$, $p$-adic analytic of finite rank |
| Iwasawa algebra $\mathbb{Z}_p[[G]]$ | Completed group algebra (Part III) |





## Further Reading

- Michel Lazard, *Sur les groupes nilpotents et les anneaux de Lie*, Annales Scientifiques de l'École Normale Supérieure 71 (1954), 101–190, for the Hausdorff series and the correspondence between pro-$p$ groups and Lie algebras.
- Michel Lazard, *Groupes analytiques $p$-adiques*, Publications Mathématiques de l'IHÉS 26 (1965), 389–603, for the $p$-adic analytic groups, the Lie theory and the fifth problem.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Benjamin, 1965), for the $p$-adic Lie theory and the exponential and logarithm in textbook form.
- Alexander Lubotzky and Dan Segal, *Subgroup Growth* (Birkhäuser, 2003), for the subgroup growth and the analytic pro-$p$ groups.
- John D. Dixon, Marcus P. F. du Sautoy, Avinoam Mann and Dan Segal, *Analytic Pro-$p$ Groups* (Cambridge University Press, 2nd ed. 1999), for the systematic theory of the uniform and powerful pro-$p$ groups.
- Alexander Lubotzky and Avinoam Mann, *On groups of polynomial subgroup growth*, Inventiones Mathematicae 104 (1991), 521–533, for the characterisation of the analytic pro-$p$ groups.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the Galois groups of the local fields and the Demushkin groups.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 2–3 (Springer, 1989), for the analytic groups over a complete ultrametric field.
- Ephraim M. Zelmanov, *On periodic compact groups*, Israel Journal of Mathematics 77 (1992), 83–95, for the solution of the restricted Burnside problem underlying the classification.
