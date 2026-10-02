
# __Real Algebraic Varieties__

## Introduction

A **real algebraic variety** is a variety of finite type over $\mathbb{R}$, and it is the real form of its complexification: the complex variety $X_{\mathbb{C}} = X\times_{\mathbb{R}}\mathbb{C}$ carries the conjugation over $\mathbb{R}$, and $X$ is the fixed locus. The real points $X(\mathbb{R})$ are the $\mathbb{R}$-points, they form a **semialgebraic** set with the topology of the real line, and their orders are recorded by a second spectrum built from the orderings rather than from the prime ideals: the **real spectrum** $\operatorname{Spec}_r$, whose points are the orderings of the residue fields. Between the two lies the **semialgebraic structure**, the Boolean algebra of the sets defined by polynomial inequalities, and above it the **Nash structure**, the same sets with the smooth structure that Part III supplies. This article fixes the real variety, the real points and their topology, the real spectrum with the real Nullstellensatz, and the semialgebraic structure, and it names and defers the Nash structure. It is the third article of the `- * Theory` group.

The article reads the real structure of *Real Structures on Varieties and Galois Descent* at the level of the real points, and it is the foundational article for *Real Structures on a Curve*, later in this group, where the number of the connected components of the real points is classified by the genus. The orderings it uses are Part I's *Ordered Fields* and *Real-Closed and Complete Ordered Fields*, with the quantifier elimination of the latter; the topology of the real points is the written *Real Topology* of this Part, with its connectedness and compactness; the bilinear and quadratic forms of *The Weil Restriction and the Trace Form* and of the written *Quadratic Forms and Polarisation* supply the positivity that the orderings express. The **smooth** structure — the real manifold of the regular real points and the Nash refinement of the semialgebraic sheaf — is Part III, and it is named here with an explicit deferral in the terms the boundary of this Part allows.

Throughout $X$ is a variety of finite type over $\mathbb{R}$, $A = \Gamma(X,\mathcal{O}_X)$ its coordinate ring when affine, $X(\mathbb{R})$ its set of real points, and $X_{\mathbb{C}}$ its complexification. The real spectrum is $\operatorname{Spec}_r A$; the support of a point is its prime ideal.

## Real Algebraic Varieties and the Real Points

### Real Forms and the Complexification

**Definition.** A **real algebraic variety** is a variety $X$ of finite type over $\mathbb{R}$. Its **complexification** is $X_{\mathbb{C}} = X\times_{\mathbb{R}}\mathbb{C}$, carrying the real structure — the conjugation — that is the descent datum of *Real Structures on Varieties and Galois Descent*, and $X$ is the fixed locus of the conjugation: $X = (X_{\mathbb{C}})^\sigma$. Two real varieties are **real forms** of the same complex variety when their complexifications are isomorphic over $\mathbb{C}$.

**Proposition (the real points are the fixed points).** The real points are the fixed locus of the conjugation on the complex points,
$$
X(\mathbb{R}) = X_{\mathbb{C}}(\mathbb{C})^{\sigma},
$$
and the fixed-point theorem of *The Galois Action as an Operator* identifies them with the $\mathbb{R}$-points of the descended variety.

*Proof.* This is the real-points theorem of *Real Structures on Varieties and Galois Descent* applied to the conjugation of $\mathbb{C}/\mathbb{R}$, with the fixed locus of the real structure.

**Example (real forms of the affine line and of the conic).** The complexification of $\mathbb{A}^1_{\mathbb{R}}$ is $\mathbb{A}^1_{\mathbb{C}}$ with the conjugation, and $\mathbb{A}^1_{\mathbb{R}}$ has the real points $\mathbb{R}$. The conic $x^2+y^2+z^2 = 0$ over $\mathbb{R}$ has the same complexification $\mathbb{P}^1_{\mathbb{C}}$ as $\mathbb{P}^1_{\mathbb{R}}$ but no real point, so the two are nonisomorphic real forms of the projective line; real points can be empty for a nonempty real variety.

### The Real Topology of the Real Points

**Definition.** The set $X(\mathbb{R})$ carries the **real topology** (also the **strong topology**), the topology it inherits from the metric topology of $\mathbb{R}$ through the coordinates: it is the coarsest topology that makes every regular function $X(\mathbb{R})\to\mathbb{R}$ continuous, and on an affine chart it is the topology induced from the metric topology of $\mathbb{R}^m$ by the coordinate functions.

**Theorem (the real points as a topological space).** For $X$ of finite type over $\mathbb{R}$ the real points $X(\mathbb{R})$ are a locally compact, locally closed and locally path-connected topological space; for $X$ affine they are a closed subspace of some $\mathbb{R}^m$, and for $X$ projective they are compact. The set $X(\mathbb{R})$ is a finite union of connected components, and the number of components of a semialgebraic set is finite.

*Proof.* On an affine chart $X\subseteq\mathbb{A}^m_{\mathbb{R}}$ the set $X(\mathbb{R})$ is the zero locus of the defining polynomials, closed in $\mathbb{R}^m$ by continuity, and locally compact because $\mathbb{R}^m$ is; a projective $X$ is a closed subspace of some $\mathbb{P}^m(\mathbb{R})$, which is compact, so $X(\mathbb{R})$ is compact. The finiteness of the number of the connected components is the semialgebraic finiteness theorem: a semialgebraic set of $\mathbb{R}^m$ has finitely many connected components, each semialgebraic, by the argument of the next section and the connectedness of *Real Topology*.

**Remark (the topology at a regular point, and the deferral).** At a real point of $X$ at which the local ring is regular, the real points of a neighbourhood form a real manifold of dimension $\dim X$: the coordinate functions give local coordinates. The **smooth** structure of the real algebraic variety — the atlas, the tangent space and the differentiable functions — is Part III's *Smooth Manifolds and Differential Topology*; this article records the topology of the real points and defers the differentiable structure to that article.

## The Real Spectrum

### Orderings and the Real Spectrum

**Definition.** Let $A$ be a commutative ring. The **real spectrum** $\operatorname{Spec}_r A$ is the set of pairs $\alpha = (\mathfrak{p},\leq)$, where $\mathfrak{p}$ is a prime ideal of $A$ and $\leq$ is an ordering of the residue field $\kappa(\mathfrak{p}) = \operatorname{Frac}(A/\mathfrak{p})$ that makes it an ordered field. Equivalently, a point of the real spectrum is a ring homomorphism $A\to R$ into a real-closed field $R$, up to the equivalence of ordered extensions; the **support** of $\alpha$ is the prime $\mathfrak{p} = \operatorname{supp}\alpha$, and $\kappa(\alpha) = \kappa(\mathfrak{p})$ is its residue field.

**Definition (the topology).** The **real spectrum** carries the topology generated by the sets
$$
[f>0] = \{\alpha : f(\alpha)>0\}, \qquad f\in A ,
$$
where $f(\alpha)$ is the image of $f$ in the real closure of $\kappa(\alpha)$; the sets $[f>0]$ and $[f=0] = \{\alpha : f(\alpha)=0\}$ are the **constructible** and **Zariski** sets of the real spectrum, and the topology they generate is the **spectral topology** of $\operatorname{Spec}_r A$.

**Theorem (the real spectrum is a spectral space).** The real spectrum of a ring is a spectral space: it is compact, sober and has a basis of compact open sets that is closed under finite intersections. The **support map**
$$
\operatorname{supp} : \operatorname{Spec}_r A\longrightarrow\operatorname{Spec}A, \qquad (\mathfrak{p},\leq)\longmapsto\mathfrak{p},
$$
is continuous, and its image is the set of the primes with a real residue field at a suitable place, that is, the primes whose residue field admits an ordering. The support map is spectral, and the real spectrum is the **real** companion of the prime spectrum, with the orderings in place of the primes alone.

*Proof.* The sets $[f_1>0,\ldots,f_k>0]$ form a basis closed under finite intersections by construction, and the compactness is the theorem that every open cover by such basic opens is refined by a finite subcover, which rests on the real-closed field properties of Part I's *Real-Closed and Complete Ordered Fields*. The support of a point is a prime by definition, so the support map is well defined and continuous for the two spectral topologies; a prime lies in its image exactly when its residue field is formally real, since a formally real field has an ordering and the residue field of a point of the real spectrum is ordered. The soberness and the basis of compact opens are the standard properties of a spectral space, the same as for $\operatorname{Spec}A$ in *Schemes*.

**Example (the real spectrum of a polynomial ring).** For $A = \mathbb{R}[x]$ the real spectrum consists of the orderings of $\mathbb{R}[x]/(x-a)\cong\mathbb{R}$, one for each $a\in\mathbb{R}$ and each ordering of $\mathbb{R}$ — there is only one — and the orderings of the fraction field $\mathbb{R}(x)$ of the whole ring. The support of the first class is the maximal ideal $(x-a)$ and of the second the zero ideal; the first class is the closed and open copy of the real points, and the second class is the "generic point" of the real spectrum, whose orderings record whether the polynomial is positive near $+\infty$ or near $-\infty$.

### The Real Nullstellensatz

**Definition.** For a real algebraic variety $X$ with real coordinate ring $A$, the **real points** embed in the real spectrum, $X(\mathbb{R})\hookrightarrow\operatorname{Spec}_r A$, by sending a point $P$ to the ordering of $\mathbb{R}$ through the evaluation at $P$. The image is the set of the **real-closed points** of the real spectrum, the points whose residue field is $\mathbb{R}$ itself.

**Theorem (the real Nullstellensatz).** Let $X$ be affine over $\mathbb{R}$ with coordinate ring $A$. An ideal $I\subseteq A$ vanishes on $X(\mathbb{R})$ if and only if $I$ is **real**, that is, if and only if every sum of squares in $A/I$ is nonzero; equivalently, the real ideals are exactly the ideals cut out by their real points. In particular the coordinate ring of the real points is the quotient of $A$ by the real radical $I_{\mathrm r}$, and the real spectra agree, $\operatorname{Spec}_r A = \operatorname{Spec}_r(A/I_{\mathrm r})$.

*Proof.* The statement is the real Nullstellensatz of Krivine and Dubois, the real analogue of the Nullstellensatz of *Algebraic Geometry* and *Schemes*, with the orderings of the real spectrum replacing the points with values in an algebraically closed field and the sums of squares replacing the vanishing of the powers. Its proof uses the real-closed field properties of Part I and the Positivstellensatz below; it is cited rather than reproduced.

**Theorem (the Positivstellensatz).** For a finitely generated ring $A$ over $\mathbb{R}$ and functions $f_1,\ldots,f_m,g_1,\ldots,g_r\in A$, the following are equivalent: the system $g_i\geq0$, $g_i\neq0$ has a solution in the real spectrum; and every $f_j$ is not of the form $-(\text{sum of squares})$ modulo the cone generated by the $g_i$. Equivalently, a polynomial is nonnegative on $X(\mathbb{R})$ if and only if it is a sum of products of the defining inequalities with sums of squares — the sharp statement that the orderings detect positivity.

*Proof.* The equivalence is Stengle's Positivstellensatz, the ordered-ring form of the real Nullstellensatz and the statement that the real spectrum is the right object for the real solutions of inequalities: the absence of a solution forces an algebraic certificate of nonnegativity, and the presence of one exhibits a point of the real spectrum. The proof is by the induction on the number of the inequalities with the resolution of the orderings, and it is cited.

## The Semialgebraic and Nash Structures

### Semialgebraic Sets

**Definition.** A subset $S\subseteq X(\mathbb{R})$ is **semialgebraic** if it is a finite Boolean combination of the sets $\{f = 0\}$ and $\{f > 0\}$ for regular functions $f\in A$; equivalently, it is a finite union of the sets $\{x : f_1(x)=\cdots=f_k(x)=0,\ g_1(x)>0,\ldots,g_l(x)>0\}$. The **semialgebraic structure** of the real variety is the Boolean algebra of its semialgebraic subsets.

**Theorem (Tarski–Seidenberg).** The image of a semialgebraic set under a polynomial map is semialgebraic, and the closure and the boundary of a semialgebraic set are semialgebraic. Consequently the semialgebraic sets of the powers $\mathbb{R}^n$ form a structure closed under the polynomial maps and their projections.

*Proof.* The image is the projection of a set defined by polynomial equalities and inequalities, and the elimination of a variable from such a system is the quantifier elimination of the theory of real-closed fields, Part I's *Real-Closed and Complete Ordered Fields*: an existential formula is equivalent to a quantifier-free one, which is a finite Boolean combination of polynomial inequalities. The closure and the boundary are projections of semialgebraic sets, hence semialgebraic.

**Corollary (the finiteness of the components).** Every semialgebraic set has finitely many connected components, each of them semialgebraic, and the semialgebraic sets form an **o-minimal** structure: the semialgebraic subsets of $\mathbb{R}$ itself are exactly the finite unions of points and intervals.

*Proof.* The semialgebraic subsets of the line are the finite Boolean combinations of points and intervals by the definition, so the structure is o-minimal; the finiteness of the components in every dimension is the theorem of the o-minimal structures, proved by the cell decomposition of a semialgebraic set, which is the induction on the number of variables with the quantifier elimination above.

### The Transfer Principle

**Theorem (the completeness of the real-closed fields).** The theory of real-closed ordered fields in the language of ordered rings is complete and admits the elimination of quantifiers, and every real-closed field is elementarily equivalent to $\mathbb{R}$; consequently an embedding of real-closed fields is elementary, $k\preceq R$.

*Proof.* The completeness and the quantifier elimination are Tarski's theorem, proved for $\mathbb{R}$ and transferred to every real-closed field by the axioms of Part I's *Real-Closed and Complete Ordered Fields*; a complete theory with one model per cardinal has the elementary-embedding property for its models, so the inclusion $k\subseteq R$ of real-closed fields is elementary.

**Corollary (the transfer for the inequalities).** Let $k$ be a real-closed field, $R\supseteq k$ a real-closed extension, and let a system of polynomial equalities and inequalities have coefficients in $k$. The system has a solution in $k$ if and only if it has a solution in $R$; equivalently, the real points of a variety over $k$ are the $k$-points of the base change to $R$, $X(k) = (X\times_kR)(R)$.

*Proof.* The solvability is the truth of an existential formula with parameters in $k$, and $k\preceq R$, so the existential formula holds in $k$ exactly when it holds in $R$; the equality of the real points then follows from the definition of the $k$-points of the base change. This is the sense in which the real points are governed by the ordering of the base field, and it is the transfer principle of *Real-Closed and Complete Ordered Fields*.

### The Nash Structure

**Definition (named, and deferred).** A **Nash function** on an open semialgebraic set $U\subseteq\mathbb{R}^n$ is a semialgebraic function that is also smooth, in the differentiable sense of Part III; the **Nash structure** of a real algebraic variety is the sheaf of the Nash functions, and a **Nash manifold** is a real algebraic variety whose real points carry the Nash structure of a manifold. The Nash functions contain the regular functions and are contained in the continuous semialgebraic functions.

**Remark (the deferral).** The construction of the Nash sheaf and the theory of the Nash manifolds need the smooth structure — the atlas, the tangent space and the derivatives — which is Part III's *Smooth Manifolds and Differential Topology*, and they are not constructed here. What this article supplies for them is the underlying semialgebraic structure: a Nash manifold is a real algebraic variety whose semialgebraic structure is that of a manifold, and the connected components, the compactness and the finiteness of the previous sections are the set-theoretic and topological skeleton on which the smooth Nash structure is placed. The reader meets the Nash structure when Part III reaches the smooth manifolds over the reals.

## Examples

**Example (the real points of quadrics).** The real points of the affine quadric $x_1^2+\cdots+x_n^2 = 1$ form a compact subset of $\mathbb{R}^n$ with the real topology, connected for $n\geq2$ and consisting of two points for $n=1$; the real points of $x_2^2 = x_1^2-1$ in the affine plane have two connected components, each semialgebraic and an interval unbounded on one side. The examples are recorded for the finiteness of the components and the compactness.

**Example (the real spectrum of the line and the orderings).** For $A=\mathbb{R}[x]$ the real spectrum consists of the closed points over the real points and of the orderings of $\mathbb{R}(x)$, and the real points of the affine line are the subset of the real-closed points. The polynomial $f = x^2-1$ is positive on the two unbounded intervals of the real points and negative in the middle interval; the points of the real spectrum at which $f>0$ are the constructible set $[f>0]$, whose intersection with $X(\mathbb{R})$ is the two intervals. This is the sense in which the real spectrum organizes the inequalities.

**Example (a real variety with no real points).** The projective conic $x^2+y^2+z^2=0$ has no real point, while its real spectrum is nonempty: the orderings of the function field supply points, and the Positivstellensatz certifies the absence of a real point by the certificate $x^2+y^2+z^2 = 0$ with the sum of squares. The real spectrum is thus strictly larger than the real points, and it detects the real solutions of the inequalities even when there is none.

## Summary

A **real algebraic variety** is a variety of finite type over $\mathbb{R}$, the fixed locus of the conjugation on its complexification $X_{\mathbb{C}} = X\times_{\mathbb{R}}\mathbb{C}$; its **real points** $X(\mathbb{R}) = X_{\mathbb{C}}(\mathbb{C})^\sigma$ carry the **real topology**, are locally compact, and are compact when $X$ is projective, and they have finitely many connected components. The **real spectrum** $\operatorname{Spec}_r A$ consists of the pairs of a prime ideal and an ordering of its residue field, equivalently of the homomorphisms into real-closed fields; it carries the spectral topology generated by the sets $[f>0]$ and $[f=0]$, it is a spectral space, and the support map $\operatorname{supp} : \operatorname{Spec}_r A\to\operatorname{Spec}A$ is continuous and spectral. The real Nullstellensatz identifies the ideals vanishing on the real points with the real ideals, the two real spectra of a ring and of its real radical agreeing; the Positivstellensatz certifies the nonnegativity on $X(\mathbb{R})$ by the sums of squares and the inequalities.

The **semialgebraic structure** is the Boolean algebra generated by the sets $\{f=0\}$ and $\{f>0\}$; it is closed under the polynomial maps by Tarski–Seidenberg, which is the quantifier elimination of the real-closed fields, and it is o-minimal, so every semialgebraic set has finitely many semialgebraic connected components. The **Nash structure** refines the semialgebraic structure by the smooth structure of Part III — the Nash functions are the smooth semialgebraic functions, and a Nash manifold is a real algebraic variety whose semialgebraic structure is that of a manifold — and it is named here and deferred to that Part. The real variety, its real points, the real spectrum and the semialgebraic structure are the objects of the article, and the smooth refinement is the object of the next Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $X_{\mathbb{C}}=X\times_{\mathbb{R}}\mathbb{C}$ | real variety and its complexification with the conjugation |
| $X(\mathbb{R})=X_{\mathbb{C}}(\mathbb{C})^\sigma$ | the real points; the fixed points of the conjugation |
| real topology (strong topology) | the topology of $X(\mathbb{R})$ from the metric topology of $\mathbb{R}$ |
| $X(\mathbb{R})\subseteq\mathbb{R}^m$, $\mathbb{P}^m(\mathbb{R})$ | closed for affine $X$; compact for projective $X$ |
| $\operatorname{Spec}_r A$ | the real spectrum: pairs (prime, ordering), or maps into real-closed fields |
| $\operatorname{supp}\alpha$, $\kappa(\alpha)$ | the prime ideal of a point of the real spectrum; its residue field |
| $[f>0]$, $[f=0]$ | constructible and Zariski basic sets of the real spectrum |
| $\operatorname{supp}:\operatorname{Spec}_r A\to\operatorname{Spec}A$ | the support map, continuous and spectral |
| real ideal, real radical | ideals vanishing on the real points; the real Nullstellensatz |
| Positivstellensatz | nonnegativity certified by sums of squares and the inequalities |
| semialgebraic set | finite Boolean combination of $\{f=0\}$, $\{f>0\}$ |
| Tarski–Seidenberg | the image of a semialgebraic set under a polynomial map is semialgebraic |
| o-minimal structure | the semialgebraic subsets of the line are the finite unions of points and intervals |
| $k\preceq R$, real-closed | elementary extension of real-closed fields; the transfer principle |
| $X(k)=(X\times_kR)(R)$ | the real points are the $k$-points of the base change |
| Nash function, Nash manifold | smooth semialgebraic functions; deferred to Part III |

## Further Reading

- Eberhard Becker, *On the real spectrum of a ring and its application to semialgebraic geometry* (Bulletin of the American Mathematical Society 83, 1977), for the real spectrum and its topology.
- Jacek Bochnak, Michel Coste and Marie-Françoise Roy, *Real Algebraic Geometry* (Springer, Ergebnisse der Mathematik 36, 1998), for the real algebraic varieties, the real points and the Nash structure.
- Ludwig Bröcker, *On the real spectrum of a ring* (Manuscripta Mathematica 24, 1978), for the comparison of the real spectrum with the prime spectrum.
- Alexander Prestel and Charles N. Delzell, *Positive Polynomials* (Springer Monographs in Mathematics, 2001), for the Positivstellensatz and its certificates.
- Michel Coste, *An Introduction to O-minimal Geometry* (Dip. Mat. Univ. Pisa, 2000), for the o-minimal structures and the finiteness of the connected components.
- John Nash, *Real algebraic manifolds* (Annals of Mathematics 56, 1952), for the Nash structure and the Nash functions.
