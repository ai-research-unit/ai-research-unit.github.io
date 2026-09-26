
# __Berkovich Spaces__

## Introduction

Rigid analytic geometry is built on a Grothendieck topology, and its "open sets" are not open sets of a genuine topology: the affinoid subdomains do not form a basis closed under arbitrary unions, and the points of the spectrum do not see the structure of the disc in the way that points of a topological space would. Berkovich's construction repairs this by enlarging the point set. A point of a **Berkovich space** is a bounded multiplicative seminorm on the affinoid algebra, and the whole analytic structure is recovered from the honest topology on that set of seminorms. The enlargement is exactly what is needed to make the unit disc connected, path-connected and contractible, to make the disc a tree whose branch points encode the residue classes, and to give the category of analytic spaces fibre products and a well-behaved topology, at the cost of points that are not classical — the seminorms of types 2, 3 and 4 that have no counterpart among the maximal ideals.

This article defines the Berkovich spectrum of an affinoid algebra, proves its compactness and non-emptiness, constructs the completed residue field of a point, and classifies the points of the one-dimensional disc. It then explains how the rigid analytic space of *Rigid Analytic Geometry* sits inside a Berkovich space as the subspace of classical points, how the rigid G-topology is recovered from the honest topology, and how the analytification of an algebraic variety is constructed. It closes with the structure theory — reduction, skeleta, the Shilov boundary and the coherent sheaf theory — and with a statement of the relation to the adic spaces. As with the preceding article, the constructions use the valuation theory of *Absolute Values, Valuations and Completions* and *Local Fields*; the non-Archimedean *analysis* on these spaces, integration, harmonic theory and the theory of differential equations, belongs to Part III. Throughout, $K$ is a complete non-Archimedean field with nontrivial absolute value $\lvert \cdot \rvert$, valuation ring $\mathcal{O}$, maximal ideal $\mathfrak{m}$ and residue field $k$, and $A$ is a $K$-affinoid algebra, that is, a quotient of a Tate algebra $K\langle X_1, \dots, X_n\rangle$, as in *Rigid Analytic Geometry*. For the classification of points $K$ is assumed algebraically closed , when necessary, with dense value group; the general case is obtained by base change to the completion of an algebraic closure.

---

## The Berkovich Spectrum

### Bounded Multiplicative Seminorms

**Definition.** Let $A$ be a $K$-affinoid algebra with a chosen affinoid norm $\lVert \cdot \rVert$. A **bounded multiplicative seminorm** on $A$ is a map $\lvert \cdot \rvert_x : A \to \mathbb{R}_{\geq 0}$ such that

**(BS1)** $\lvert a \rvert_x \geq 0$ for all $a$, with $\lvert 0 \rvert_x = 0$ and $\lvert 1 \rvert_x = 1$;

**(BS2)** $\lvert ab \rvert_x = \lvert a \rvert_x \lvert b \rvert_x$;

**(BS3)** $\lvert a + b \rvert_x \leq \lvert a \rvert_x + \lvert b \rvert_x$;

**(BS4)** there is a constant $C \geq 0$ with $\lvert a \rvert_x \leq C\lVert a \rVert$ for all $a \in A$.

The **Berkovich spectrum** $M(A)$ is the set of such seminorms, equipped with the weakest topology making all the evaluation maps $x \mapsto \lvert a \rvert_x$, $a \in A$, continuous.

Condition (BS4) is what makes the seminorm **bounded**; it is automatic for a seminorm on a finite-dimensional algebra over $K$, and it is needed in general to keep the spectrum compact. The multiplicative condition (BS2) is what makes the seminorm a "point": it behaves like the absolute value of $K$ at a value of a function. A multiplicative seminorm need not be a norm: its kernel $\mathfrak{p}_x = \{a : \lvert a \rvert_x = 0\}$ is a prime ideal, and $\lvert \cdot \rvert_x$ is a norm exactly when $\mathfrak{p}_x = 0$. Already on $A = K\langle X\rangle$ the seminorm $f \mapsto \lvert f(0)\rvert$ is bounded and multiplicative with kernel the maximal ideal $(X)$.

**Proposition.** The Berkovich spectrum $M(A)$ is a compact Hausdorff space.

**Proof.** The map

$$
M(A) \longrightarrow \prod_{a \in A} [0, \lVert a \rVert], \qquad x \longmapsto (\lvert a \rvert_x)_{a \in A},
$$

is injective, because the seminorm is determined by its values. Its image is closed under pointwise limits: if $x_i \to x$ pointwise along a net of elements of $M(A)$, then multiplicativity, the triangle inequality and (BS1) pass to the pointwise limit, so the limit is again a bounded multiplicative seminorm when it is finite, and the bound (BS4) is preserved. The product $\prod_a [0, \lVert a \rVert]$ is compact by Tychonoff, so its closed image is compact; the topology just defined is the subspace topology of the product, hence $M(A)$ is compact. It is Hausdorff because distinct seminorms differ at some $a \in A$, and the corresponding coordinate of the product separates them. $\square$

**Theorem (non-emptiness).** If $A \neq 0$, then $M(A) \neq \emptyset$. More precisely, for every maximal ideal $\mathfrak{m}$ of $A$ the quotient $A/\mathfrak{m}$ is a finite extension of $K$, and the unique extension of the absolute value of $K$ to that finite extension defines a point of $M(A)$; such points are the **classical points**.

**Proof.** Let $\mathfrak{m}$ be a maximal ideal. By the Nullstellensatz for affinoid algebras, $A/\mathfrak{m}$ is a finite-dimensional $K$-algebra and, $\mathfrak{m}$ being maximal, a finite field extension of $K$; a finite extension of a complete non-Archimedean field carries a unique extension of the absolute value and is complete for it, by *Absolute Values, Valuations and Completions* and *Local Fields*. Composing the quotient $A \to A/\mathfrak{m}$ with that absolute value gives a bounded multiplicative seminorm: boundedness follows from the continuity of the quotient map, equivalently from the fact that all norms on a finite-dimensional $K$-space are equivalent. Hence $M(A) \neq \emptyset$. $\square$

**Example (the point of a field).** For $A = K$ the spectrum $M(K)$ is a single point, the absolute value of $K$; this is the Berkovich analogue of a one-point space and the base of every construction below.

### The Completed Residue Field

**Definition.** Let $x \in M(A)$ be a point. Its **kernel** is the prime ideal

$$
\mathfrak{p}_x = \{a \in A : \lvert a \rvert_x = 0\} = \ker(\lvert \cdot \rvert_x),
$$

and the quotient $A/\mathfrak{p}_x$ is a domain with a multiplicative norm induced by $\lvert \cdot \rvert_x$. The **completed residue field** at $x$ is the completion

$$
\mathcal{H}(x) = \widehat{\operatorname{Frac}(A/\mathfrak{p}_x)} ,
$$

the completion of the fraction field of $A/\mathfrak{p}_x$ with respect to the norm induced by $\lvert \cdot \rvert_x$. It is a complete valued field extension of $K$, and the seminorm $\lvert \cdot \rvert_x$ is recovered as the restriction to $A$ of the absolute value of $\mathcal{H}(x)$.

**Proposition.** Let $x \in M(A)$. Then $\mathcal{H}(x)$ is a valued field extension of $K$, the residue field of $\mathcal{H}(x)$ is an extension of $k$, and $\mathcal{H}(x)$ is the smallest complete valued field through which $\lvert \cdot \rvert_x$ factors. The point $x$ is classical exactly when $\mathcal{H}(x)$ is a finite extension of $K$ and the map $A \to \mathcal{H}(x)$ is surjective.

**Proof.** The completion of a valued field is a valued field, and $\mathcal{H}(x)$ contains $K$ because $\lvert \cdot \rvert_x$ restricts to $\lvert \cdot \rvert$ on the copy of $K$ in $A$; hence it is a valued extension. The residue field statement is the standard functoriality of the residue field under completion. Minimality is the universal property of the completion. The last statement is the definition of a classical point and the theorem above. $\square$

**Definition.** The **residue field** of the point $x$ is written $\widetilde{\mathcal{H}(x)}$ and called the **residue field at $x$**; the **value group** is $\Gamma_x = \lvert \mathcal{H}(x)^\times \rvert$, a subgroup of $\mathbb{R}_{>0}$ containing $\lvert K^\times \rvert$.

**Remark.** The pair $(\widetilde{\mathcal{H}(x)}, \Gamma_x)$ is the local invariant of a Berkovich point, and the classification of the points of a curve is a classification of the possible pairs. This is the analogue for a valued field of the residue field and value group of a local field, and it is why the theory sits naturally after *Local Fields*.

### The Spectral Point

**Theorem.** The **spectral seminorm** $\lvert a \rvert_{\mathrm{sup}} = \sup_{x \in \operatorname{Sp} A} \lvert a(x) \rvert$ of *Rigid Analytic Geometry* is a bounded multiplicative seminorm on $A$ when $A$ is reduced, hence is a point of $M(A)$; it is the point at which the supremum of $\lvert a \rvert_x$ over $M(A)$ is attained for every $a \in A$.

**Proof.** On a reduced affinoid algebra the spectral seminorm is multiplicative and bounded: multiplicativity is the standard theorem that the supremum seminorm of a reduced affinoid algebra is multiplicative, which follows from the maximum modulus principle of *Rigid Analytic Geometry* (the supremum of a product is the product of the suprema), and boundedness is the inequality $\lvert a\rvert_{\mathrm{sup}} \leq \lVert a\rVert$ for any residue norm of the theorem above. It is therefore a point of $M(A)$. For the extremal property, Berkovich's maximum modulus principle states that

$$
\max_{x \in M(A)} \lvert a \rvert_x = \lim_m \lVert a^m \rVert^{1/m}
$$

for the norm of any presentation of $A$, and the right-hand side is $\lvert a \rvert_{\mathrm{sup}}$ by the theorem of *Rigid Analytic Geometry*; the maximum is attained at the spectral point. $\square$

**Corollary (Berkovich maximum modulus principle).** For every $a \in A$,

$$
\sup_{x \in M(A)} \lvert a \rvert_x = \lvert a \rvert_{\mathrm{sup}} ,
$$

and the supremum is attained, at the spectral point. In particular the supremum over the Berkovich spectrum is the spectral norm of $A$, which for a reduced affinoid algebra is a norm and is bounded by every residue norm of a presentation.

**Proof.** Both equalities are Berkovich's maximum modulus principle $\sup_{x\in M(A)}\lvert a\rvert_x = \lim_m\lVert a^m\rVert^{1/m}$ together with the identification of that limit with the spectral norm $\lvert a\rvert_{\mathrm{sup}}$ in *Rigid Analytic Geometry*, and the supremum is attained at the spectral point. $\square$

---

## The Berkovich Line

### The Unit Disc

**Definition.** For the Tate algebra $K\langle T\rangle$ the Berkovich spectrum $M(K\langle T\rangle)$ is the **closed unit disc** $\mathbb{D}^1$ of the Berkovich affine line. The **Gauss point** $\zeta \in \mathbb{D}^1$ is the point whose seminorm is the Gauss norm, $\lvert f \rvert_\zeta = \lVert f \rVert_G$.

**Theorem (classification of the points of the disc).** Let $K$ be algebraically closed and complete with dense value group. Every point $x \in M(K\langle T\rangle)$ is of exactly one of the following types.

**Type 1.** The point is classical: $\mathcal{H}(x)$ is a finite extension of $K$ and there is an $a \in K$ with $\lvert a \rvert \leq 1$ such that $\lvert f \rvert_x = \lvert f(a) \rvert$ for all $f$.

**Type 2.** There are $a \in \mathcal{O}$ and $r \in \lvert K^\times \rvert$ with $0 < r \leq 1$ such that

$$
\lvert f \rvert_x = \sup_{\lvert t - a \rvert \leq r} \lvert f(t) \rvert \qquad (f \in K\langle T\rangle),
$$

the supremum over the closed disc $D(a,r)$; the value group is $\lvert K^\times \rvert$ and the residue field $\widetilde{\mathcal{H}(x)}$ is the residue field of the disc, of transcendence degree $1$ over $k$. The Gauss point is the case $a=0$, $r=1$.

**Type 3.** The same formula with $r \notin \lvert K^\times \rvert$, $r < 1$; then $\Gamma_x$ strictly contains $\lvert K^\times \rvert$ (it is generated by it and $r$) while the residue field $\widetilde{\mathcal{H}(x)}$ is algebraic over $k$, of transcendence degree $0$.

**Type 4.** The point is a limit of a nested sequence of discs $D(a_i, r_i)$ with $D(a_{i+1}, r_{i+1}) \subseteq D(a_i, r_i)$ and $\bigcap_i D(a_i, r_i) = \emptyset$; the field $\mathcal{H}(x)$ has infinite transcendence degree over $K$ and value group equal to $\lvert K^\times \rvert$.

**Proof.** The classification is Berkovich's theorem for the disc. The essential steps are: a bounded multiplicative seminorm on $K\langle T\rangle$ is determined by its restriction to $K[T]$, and the kernel is a prime ideal corresponding to a point or to a disc; if the kernel is maximal one obtains type 1; otherwise one shows that the seminorm is the supremum over a closed disc, and the value group decides between types 2 and 3; the remaining case is a nested intersection of discs that is empty, giving type 4. Berkovich's original memoir and the standard expositions give the details. $\square$

**Remark (the tree structure).** The closed unit disc is a compact, Hausdorff, path-connected and contractible space, and it is an $\mathbb{R}$-tree: between any two points there is a unique arc, and the arc is obtained by moving along the discs containing both points. The Gauss point $\zeta$ is the branch point of infinite valence, with one branch for each residue class in $k$; the classical points are the points of type 1, and the type 4 points are the remaining points, obtained as limits of nested sequences of discs with empty intersection. The disc is thus the precise sense in which the rigid disc is connected: the extra points of types 2, 3 and 4 supply the connections between the residue classes that the classical points cannot provide.

**Example (the case of $\mathbb{C}_p$).** For $K = \mathbb{C}_p$ the value group is dense and the residue field is algebraically closed; the disc is a tree with the Gauss point of infinite valence at the centre, the points of types 2 and 3 branching off it and accumulating densely in the branches, and the type 4 points arising from nested sequences of discs with empty intersection. The disc is compact and metrisable, hence separable, so it is the closure of a countable set, while its topology is the ordinary topology of a compact metric space rather than the Grothendieck topology of the rigid disc.

### The Affine and Projective Lines

**Definition.** The **Berkovich affine line** is

$$
\mathbb{A}^{1,\mathrm{an}} = \bigcup_{n \geq 1} M(K\langle T/n\rangle),
$$

the union of the discs of radius $n$, and the **Berkovich projective line** is obtained by gluing $M(K\langle T\rangle)$ and $M(K\langle T^{-1}\rangle)$ along $M(K\langle T, T^{-1}\rangle)$.

**Theorem.** $\mathbb{A}^{1,\mathrm{an}}$ is a locally compact, Hausdorff, path-connected, contractible $\mathbb{R}$-tree, and the projective line $\mathbb{P}^{1,\mathrm{an}}$ is a compact simply-connected $\mathbb{R}$-tree. The points of types 1, 2 and 3 form a dense subset, and a point of type 4 is a limit of points of types 2 and 3, so the four types exhaust the space.

**Proof.** Local compactness and the tree structure follow from the classification theorem applied to each disc and the compatibility of the discs; contractibility of the affine line and simple connectivity of the projective line are Berkovich's theorems, proved by exhibiting the retraction onto a point and onto the interval joining the two "ends". The density of the points of types 1, 2 and 3 is the standard statement that a point of type 4 is the limit of the Gauss points of the discs in the nested sequence defining it, and conversely that a point of type 3 is a limit of points of type 2. $\square$

**Remark.** The tree structure of the projective line is the non-Archimedean analogue of the Riemann sphere, and it is the reason Berkovich's theory is suited to problems in which connectedness and the classification of analytic maps matter: a non-constant analytic map between Berkovich curves is an open map, it has a well-defined local degree, and the Hurwitz formula holds. These are analytic facts of Part III in their proofs, but their statements belong to the geometry of the valued field.

---

## The Relation to Rigid Analytic Geometry

### Classical Points and the Comparison Functor

**Definition.** A point $x \in M(A)$ is **classical** when its kernel $\mathfrak{p}_x$ is a maximal ideal of $A$; the assignment $x \mapsto \mathfrak{p}_x$ then gives a bijection between the classical points of $M(A)$ and the rigid spectrum $\operatorname{Sp} A$. For an arbitrary point $x$ the kernel $\mathfrak{p}_x$ is only prime, and its **reduction** is the nonempty closed subset of $\operatorname{Sp} A$ consisting of the maximal ideals containing $\mathfrak{p}_x$, that is, the Zariski closure of $\mathfrak{p}_x$ in $\operatorname{Sp} A$; a classical point is exactly a point whose reduction is a single point.

**Theorem (comparison of topologies).** Let $X = \operatorname{Sp} A$ be an affinoid space with its weak G-topology and let $M(A)$ be its Berkovich spectrum.

**(a)** For every affinoid subdomain $U \subseteq X$ the set

$$
U^{\mathrm{an}} = \{x \in M(A) : \lvert f \rvert_x \leq 1 \text{ for every } f \in A \text{ with } \lvert f \rvert \leq 1 \text{ on } U\}
$$

is a closed subset of $M(A)$, the assignment $U \mapsto U^{\mathrm{an}}$ preserves inclusions and finite intersections, its classical points are exactly the points of $U$, and the family of the $U^{\mathrm{an}}$ generates the topology of $M(A)$: the Berkovich topology is the coarsest topology in which all the sets $U^{\mathrm{an}}$ are closed.

**(b)** The assignment $U \mapsto U^{\mathrm{an}}$ is compatible with the structure sheaves, and the global sections of the structure sheaf of $M(A)$ are $A$.

**(c)** The coherent sheaves on the Berkovich space $M(A)$ are the sheaves associated to finitely generated $A$-modules, and their higher cohomology vanishes on affinoids, as in Kiehl's theorem.

**Proof.** (a) Each $U^{\mathrm{an}}$ is an intersection of the closed sets $\{x : \lvert f\rvert_x\leq1\}$, hence closed, and the classical points of $U^{\mathrm{an}}$ are the maximal ideals $\mathfrak{m}$ at which $\lvert f(\mathfrak{m})\rvert\leq1$ for all $f$ that are bounded by $1$ on $U$, which by the universal property of the affinoid algebra $A_U$ is exactly $U$. The generation statement is Berkovich's comparison theorem for analytic domains. (b) and (c) follow by transporting the rigid structure sheaf across the comparison, using Tate's acyclicity and Kiehl's theorem of *Rigid Analytic Geometry*. $\square$

**Remark.** The passage from rigid to Berkovich is a passage from a Grothendieck topology to a genuine topology, and the two carry the same coherent sheaf theory. The advantage of the Berkovich presentation is that connectedness, compactness and path-connectedness become properties of an ordinary topological space, and that fibre products and proper maps behave as in algebraic geometry. The rigid presentation retains the advantage that its points are exactly the classical points, so statements about the maximal spectrum are stated directly.

### Analytification

**Definition.** Let $X$ be a scheme of finite type over $K$. The **Berkovich analytification** $X^{\mathrm{an}}$ is the set of pairs $(x, \lvert \cdot \rvert)$ where $x \in X$ is a scheme point and $\lvert \cdot \rvert$ is an absolute value on the residue field $\kappa(x)$ extending the absolute value of $K$ and bounded on an affine neighbourhood with respect to a choice of coordinates, equipped with the weakest topology making the maps $x \mapsto \lvert f(x) \rvert$ continuous for local functions $f$, and with the evident structure sheaf.

**Theorem.** For a scheme $X$ of finite type over $K$ the analytification $X^{\mathrm{an}}$ is a Berkovich analytic space; the assignment is functorial, commutes with fibre products, and for a proper algebraic variety it is compact. On a projective variety the coherent sheaves on $X^{\mathrm{an}}$ are exactly the analytifications of the coherent algebraic sheaves, and the analytification functor on coherent sheaves is an equivalence of categories (GAGA).

**Proof.** The functoriality and the compatibility with fibre products are proved affine-locally from the universal property of the Berkovich spectrum; compactness in the proper case is Berkovich's theorem, using the valuative criterion, in which the points of the analytification with values in an extension play the role of the spectrum of a valuation ring. The GAGA statement is the analogue of the rigid GAGA of *Rigid Analytic Geometry* and is quoted as standard. $\square$

**Example (the projective line).** The analytification $(\mathbb{P}^1_K)^{\mathrm{an}}$ is the Berkovich projective line of the previous section. The analytification of an elliptic curve over $K$ is a compact space which is a "tate curve" quotient in the multiplicative case and is homeomorphic to a circle in the good reduction case — the two standard pictures of non-Archimedean geometry.

---

## Structure Theory

### Reduction and the Special Fibre

**Definition.** Let $A$ be a $K$-affinoid algebra with a chosen norm, and let $A^\circ = \{a : \lvert a \rvert_{\mathrm{sup}} \leq 1\}$ and $A^{\circ\circ} = \{a : \lvert a \rvert_{\mathrm{sup}} < 1\}$ be the **power-bounded** and **topologically nilpotent** subrings. The **reduction** of $A$ is the $k$-algebra

$$
\widetilde{A} = A^\circ / A^{\circ\circ} ,
$$

a reduced $k$-algebra of finite type when $A$ is reduced and $K$ has dense value group.

**Definition.** For a point $x \in M(A)$ the **reduction map** at $x$ sends $a \in A$ with $\lvert a \rvert_x \leq 1$ to the residue class of $a$ in the residue field $\widetilde{\mathcal{H}(x)}$, and the **reduction** of the point is the associated valuation-theoretic point of $\operatorname{Spec}\widetilde{A}$ in the case of the Gauss point of a polynomial algebra. The **skeleton** of a Berkovich space with a fixed polystable formal model is the union of the reductions of the strata, a finite polyhedral complex embedded in the space.

**Theorem.** Let $X$ be a quasi-compact Berkovich space with a polystable formal model. Then $X$ admits a continuous retraction onto its skeleton, and the skeleton is a finite polyhedral complex of dimension equal to the dimension of $X$; the retraction is compatible with the formal model and is invariant under admissible blow-ups.

**Pro.** The retraction is constructed disc by disc, using the reduction map and the classification of the points of a disc, and the polyhedral structure comes from the value groups of the points; the compatibility with admissible blow-ups is the statement that the skeleton depends only on the generic fibre. This is the theory of the skeleton of a Berkovich space, due to Berkovich and developed by Ducros and others; it is quoted here as standard, and the formal-model and adic formulations are not covered here. $\square$

### The Shilov Boundary

**Definition.** A **Shilov boundary** of a $K$-affinoid algebra $A$ is a minimal closed subset $\Gamma(A) \subseteq M(A)$ such that for every $a \in A$

$$
\sup_{x \in \Gamma(A)} \lvert a \rvert_x = \sup_{x \in M(A)} \lvert a \rvert_x .
$$

**Theorem.** Every $K$-affinoid algebra $A$ has a Shilov boundary $\Gamma(A)$, and it is finite; the spectral point of §The Spectral Point belongs to it.

**Proof.** The existence of a minimal closed subset with the maximum property is an application of Zorn's lemma to the family of closed subsets with the property, using the compactness of $M(A)$. Finiteness is Berkovich's theorem: the boundary is the set of points of maximal dimension in the reduction, and there are finitely many of them because the reduction is a $k$-algebra of finite type after the choice of a good model. $\square$

**Corollary (generalised maximum modulus principle).** For every $a \in A$, $\lvert a \rvert_{\mathrm{sup}} = \sup_{x \in \Gamma(A)} \lvert a \rvert_x = \max_{x \in \Gamma(A)} \lvert a \rvert_x$, the maximum over the finite Shilov boundary.

**Proof.** The first equality is the defining property of the Shilov boundary, and the second is the passage from supremum to maximum over the finite set $\Gamma(A)$. $\square$

**Remark.** The Shilov boundary is the non-Archimedean analogue of the boundary of a domain in complex analysis, but it is finite and its structure is combinatorial. This is the sharpest illustration of the difference between the Archimedean and non-Archimedean theories, and it depends only on the norm and the affine algebra, so it belongs to the geometry of the valued field.

### Coherent Sheaves and Finiteness

**Theorem (Berkovich's finiteness).** Let $X$ be a compact Berkovich analytic space and let $\mathcal{F}$ be a coherent sheaf on $X$. Then the cohomology groups $H^q(X, \mathcal{F})$ are finite-dimensional over $K$ for all $q$, and vanish above the dimension of $X$.

**Proof.** The theorem is Berkovich's finiteness theorem, proved by reducing to the affinoid case by a finite acyclic covering and applying Kiehl's theorem of *Rigid Analytic Geometry* on each piece together with a spectral sequence for the covering. It is quoted as standard; the cohomology is the standard sheaf cohomology on the Berkovich space, which agrees with the rigid cohomology on affinoid domains by the comparison theorem above. $\square$

---

## Summary

The **Berkovich spectrum** $M(A)$ of a $K$-affinoid algebra $A$ is the set of bounded multiplicative seminorms on $A$ with the topology of pointwise convergence; it is a compact Hausdorff space, non-empty when $A \neq 0$, and it contains the maximal ideals as the **classical points**, through the identification of a maximal ideal with the unique extension of the absolute value to the finite field $A/\mathfrak{m}$. Each point $x$ has a **kernel** $\mathfrak{p}_x$, a **completed residue field** $\mathcal{H}(x)$ with residue field and value group, and the local invariants $(\widetilde{\mathcal{H}(x)}, \Gamma_x)$ classify the points of a curve. The **spectral seminorm** is a point, and the **Berkovich maximum modulus principle** states that $\sup_{x \in M(A)} \lvert a \rvert_x = \lvert a \rvert_{\mathrm{sup}}$ with the supremum attained.

The **closed unit disc** $M(K\langle T\rangle)$ has points of four types: classical points, points given by the supremum over a closed disc with radius in the value group (type 2, including the **Gauss point**), points given by a disc with radius outside the value group (type 3), and limits of nested discs with empty intersection (type 4). It is a compact, path-connected, contractible $\mathbb{R}$-tree with the Gauss point as a branch point of infinite valence, and the same structure passes to the affine and projective Berkovich lines, which are trees and compact trees respectively. The affinoid subdomains of the rigid theory become a basis of the honest topology of $M(A)$, the structure sheaf and the coherent sheaf theory agree with those of rigid analytic geometry, and the **analytification** of a scheme of finite type over $K$ is a Berkovich space, functorial, compatible with fibre products and compact in the proper case, with the GAGA principle holding for projective varieties. The **reduction** $A^\circ/A^{\circ\circ}$ gives the special fibre and the relation between the analytic space and its combinatorial skeleton, the **Shilov boundary** is a finite set realising the maximum modulus principle, and Berkovich's finiteness theorem makes the coherent cohomology of a compact space finite-dimensional.

The theory is geometry over a valued field and uses only the norm and the valuation; the analysis on Berkovich spaces belongs to Part III. The formal and adic formulations of the same objects are not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Complete non-Archimedean field, algebraically closed and with dense value group for the classification |
| $A$ | A $K$-affinoid algebra |
| $M(A)$ | Berkovich spectrum, the set of bounded multiplicative seminorms |
| $\lvert \cdot \rvert_x$ | The seminorm of the point $x$ |
| $\mathfrak{p}_x = \ker \lvert \cdot \rvert_x$ | Kernel of a point |
| $\mathcal{H}(x)$ | Completed residue field at $x$ |
| $\widetilde{\mathcal{H}(x)}$ | Residue field at $x$ |
| $\Gamma_x = \lvert \mathcal{H}(x)^\times \rvert$ | Value group at $x$ |
| $\lvert \cdot \rvert_{\mathrm{sup}}$ | Spectral seminorm and spectral point |
| $\mathbb{D}^1 = M(K\langle T\rangle)$ | Closed unit disc |
| $\zeta$ | Gauss point, $\lvert f \rvert_\zeta = \lVert f \rVert_G$ |
| $D(a,r)$ | Closed disc of centre $a$ and radius $r$ |
| $\mathbb{A}^{1,\mathrm{an}}$, $\mathbb{P}^{1,\mathrm{an}}$ | Berkovich affine and projective lines |
| $\rho : M(A) \to \operatorname{Sp} A$ | Classical-point (reduction) map |
| $X^{\mathrm{an}}$ | Berkovich analytification of a scheme $X$ |
| $A^\circ$, $A^{\circ\circ}$, $\widetilde{A}$ | Power-bounded and topologically nilpotent subrings, and the reduction |
| $\Gamma(A)$ | Shilov boundary of $A$ |





## Further Reading

- Vladimir G. Berkovich, *Spectral Theory and Analytic Geometry over Non-Archimedean Fields* (American Mathematical Society, 1990), for the spectrum of seminorms, the classification of points and the foundation of the theory.
- Vladimir G. Berkovich, "Étale cohomology for non-Archimedean analytic spaces", *Publications Mathématiques de l'IHÉS* **78** (1993), 5–161, for the finiteness theorems and the coherent cohomology.
- Antoine Ducros, "La structure des courbes analytiques", lecture notes (Paris, 2012–2014), for the tree structure of analytic curves and the skeleta.
- Michael Temkin, "Introduction to Berkovich analytic spaces", in *Berkovich Spaces and Applications* (Springer, 2015), for a modern survey with proofs and examples.
- Jérôme Poineau, *Les espaces de Berkovich sont angéliques* (Société Mathématique de France, 2013), for the point-set topology of Berkovich spaces.
- Siegfried Bosch, *Lectures on Formal and Rigid Geometry* (Springer, 2014), for the rigid comparison and the affinoid background.
- Brian Conrad, "Several approaches to non-Archimedean geometry", in *$p$-adic Geometry* (American Mathematical Society, 2008), for a comparison of the rigid, Berkovich and adic approaches.
