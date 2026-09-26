
# __Descriptive Set Theory__

## Introduction

Descriptive set theory studies the sets that occur in analysis — the sets generated from the open sets by the operations of countable union, countable intersection and complement, and the sets obtained by further projection and complementation — and classifies them by the number of these operations needed. The theory begins with the observation that in a complete separable metric space the sets that are analytically respectable form a hierarchy of exact complexity: open, closed, countable intersections of opens, and so on through the countable ordinals, followed by the analytic sets, which are the continuous images of the whole space and are the sets that arise as the solution sets of equations with a quantifier, and then the coanalytic sets, their complements. Two of the theorems are the reason the subject exists. Souslin's theorem of 1917 states that a set is Borel exactly when it is both analytic and coanalytic, so that the projection operation destroys Borelness and the hierarchy continues strictly; and the same year's work of Suslin and the following work of Lusin and Sierpiński show that every analytic set is universally measurable, has the Baire property and, if uncountable, contains a perfect subset, so that the pathologies of the axiom of choice cannot be analytic. In a complete metric space the analytic sets are thus the sets of analysis.

This article develops the classical theory in the separable complete metric setting and in the light of the measure and convergence theory of the previous articles. The Polish spaces and their basic structure come first, with the Baire space and the Cantor space as the universal objects into which every other Polish space maps continuously and thereby reduces the general theory to one space. The Borel hierarchy is then defined and shown to be strictly increasing at every level, by the universal-set method, and the Borel isomorphism theorem reduces the uncountable case to the real line. The analytic sets are introduced through the Souslin operation, their closure properties and their relation to continuous images, and the separation theorems and their reductions are stated: two disjoint analytic sets are separated by a Borel set, and every analytic set is the continuous injective image of a closed subset of the Baire space, which is the source of the perfect set property. Suslin's theorem is proved by the separation technique. The regularisation of the analytic sets follows: universal measurability with respect to every $\sigma$-finite Borel measure, the Baire property, and hence — since the analytic sets are the projections of the closed sets — the failure of the classical construction of a non-measurable set inside this class. The projective hierarchy closes the article, with the determinacy hypothesis that regulates it and the independence phenomena, and with the ranking of well-founded relations, which is the point at which descriptive set theory meets the theory of ordinals and the invariant descriptive theory.

The prerequisites are *Metric, Uniform and Complete Spaces* and *Topological Spaces* of Part II for completeness, separability, compactness and the Baire category theorem; *Measure Theory and Integration* for $\sigma$-algebras, Borel measures, measurability and completeness of measure; and *Modes of Convergence* for the vocabulary of pointwise convergence of sequences of functions on which the Baire classification rests. The cardinal arithmetic — the continuum hypothesis, the cardinality of $\mathbb{R}$, König's theorem, the role of the axiom of choice — belongs to *Cardinality and the Axiom of Choice*, and is used here only through the concrete countability statements stated in line. The descriptive topology of Part II supplies the topological space and the metrisation criteria; the theory here adds the countable operations. The measure-theoretic content of the harmonic analysis of Part III is deferred:written below, uses the measurability of analytic sets, and the reader meets there the applications, not the proofs.

## Polish Spaces

### Definitions and the Standard Examples

**Definition.** A topological space is **Polish** if it is separable and its topology is induced by a complete metric.

**Theorem.** The following are Polish: $\mathbb{R}^n$ and $\mathbb{C}^n$; a closed subset of a Polish space with the induced topology; an open subset of a Polish space, with the induced topology; a countable product of Polish spaces, with the product topology; and a countable disjoint union of Polish spaces, with the obvious metric.

**Proof.** For the product, the metric $d(x,y) = \sum_n2^{-n}\min(d_n(x_n,y_n),1)$ is complete and the product of countable dense sets is countable dense. For an open $U\subseteq X$ the metric $d_U(x,y) = d(x,y)+\lvert 1/\operatorname{dist}(x,X\setminus U)-1/\operatorname{dist}(y,X\setminus U)\rvert$ is complete on $U$, and completeness of the restriction to a closed set is inherited. $\square$

**Definition.** The **Baire space** is $\mathcal{N} = \mathbb{N}^{\mathbb{N}}$ with the product of the discrete topologies, and the **Cantor space** is $\mathcal{C} = 2^{\mathbb{N}}$ with the product topology. Both are Polish and zero-dimensional. For $s\in\mathbb{N}^{<\mathbb{N}}$ the **cylinder** is $N_s = \{x : x\restriction\lvert s\rvert = s\}$, and the cylinders form a countable base of clopen sets.

**Theorem (universality).** Every nonempty Polish space is a continuous image of the Baire space; every nonempty compact metrisable space is a continuous image of the Cantor space; every nonempty perfect zero-dimensional compact metrisable space is homeomorphic to the Cantor space; and every nonempty perfect Polish space has cardinality $2^{\aleph_0}$.

**Proof sketch.** For the first, choose a compatible complete metric, well-order a countable dense subset and define a surjection by the "tent" construction: to $x\in\mathcal{N}$ assign the limit of the points selected by $x$ from the successive refinements of a countable base by shrinking radii at each level; completeness makes the limit exist and density makes it exhaust the space. For the second and third, embed the space into $2^{\mathbb{N}}$ by separating points with a countable clopen basis, and use the Cantor–Bendixson analysis to remove the countable part. $\square$

**Definition.** For a topological space $X$ the space $F(X)$ of closed subsets carries the **Fell topology**, generated by the sets $\{F : F\cap K = \emptyset\}$ for $K$ compact and $\{F : F\cap U\neq\emptyset\}$ for $U$ open; the space $\mathcal{P}(X)$ of Borel probability measures carries the **weak topology**, generated by $\mu\mapsto\int f\,d\mu$ for $f$ bounded continuous.

**Theorem.** If $X$ is a locally compact Polish space then $F(X)$ with the Fell topology is Polish; for every Polish $X$, $\mathcal{P}(X)$ with the weak topology is Polish. The Borel $\sigma$-algebras these topologies generate agree with the $\sigma$-algebras generated by the sets $\{F : F\cap U\neq\emptyset\}$ and by the evaluation maps $\mu\mapsto\mu(B)$, respectively.

**Proof sketch.** For $F(X)$ the Fell topology is compact and metrisable, and the compact metric spaces are Polish; for $\mathcal{P}(X)$ use the embedding into the dual of the space of bounded continuous functions with the sup norm, whose weak-$\ast$ topology is induced by a complete metric on the unit ball, or the equivalent description by the Lévy–Prokhorov metric. $\square$

### The Borel Hierarchy

**Definition.** Let $X$ be Polish. The **Borel hierarchy** is defined by transfinite recursion on the countable ordinals:
$$
\Sigma^0_1 = \text{open sets}, \qquad \Pi^0_\alpha = \{\,X\setminus A : A\in\Sigma^0_\alpha\,\}, \qquad \Sigma^0_\alpha = \Bigl\{\bigcup_{n}A_n : A_n\in\bigcup_{\beta<\alpha}\Pi^0_\beta\Bigr\}\ \ (\alpha>1),
$$
and $\Delta^0_\alpha = \Sigma^0_\alpha\cap\Pi^0_\alpha$. The **Borel sets** are $\bigcup_{\alpha<\omega_1}\Sigma^0_\alpha$.

**Theorem.** Each $\Sigma^0_\alpha$ is closed under finite intersections and countable unions, each $\Pi^0_\alpha$ under finite unions and countable intersections, each $\Delta^0_\alpha$ under complementation and finite Boolean operations; the classes increase with $\alpha$, and the Borel sets $\bigcup_{\alpha<\omega_1}\Sigma^0_\alpha$ are the smallest $\sigma$-algebra containing the open sets.

**Proof sketch.** Monotonicity is immediate from the definitions. For the closure under countable unions, write a countable union of countable unions over a common index; the remaining statements follow from the closure of the preceding classes under the dual operations, which is proved by taking complements of the defining unions. $\square$

**Theorem (strictness).** For every $\alpha<\omega_1$ and every uncountable Polish space $X$, $\Sigma^0_\alpha\neq\Pi^0_\alpha$ and $\Sigma^0_\alpha\subsetneq\Sigma^0_{\alpha+1}$.

**Proof sketch.** One constructs a $\Sigma^0_\alpha$-universal set $U_\alpha\subseteq\mathcal{N}\times X$, a set whose sections exhaust $\Sigma^0_\alpha(X)$, by recursion on $\alpha$ using a coding of the countable sequences of codes of lower levels, and then applies the diagonal argument to the diagonal set $\{x : (x,x)\notin U_\alpha\}\in\Pi^0_\alpha\setminus\Sigma^0_\alpha$. The existence of the parameterisation by real numbers also gives the strictness at each level. $\square$

**Theorem (Borel isomorphism).** Every uncountable Polish space is Borel isomorphic to $\mathbb{R}$; more precisely there is a bijection carrying the Borel sets of one onto the Borel sets of the other. Consequently the cardinality of the Borel sets of an uncountable Polish space is $2^{\aleph_0}$, and the Borel hierarchy is exhausted at the countable ordinals.

**Proof sketch.** The Cantor–Bendixson theorem decomposes a Polish space into a countable part and a perfect part; a perfect Polish space is Borel isomorphic to the Cantor space by the existence of a countable separating family of clopen sets, and the Cantor space is Borel isomorphic to $\mathbb{R}$. The classification follows. $\square$

### The Baire Category Theorem and the Baire Property

**Definition.** A set is **nowhere dense** if the closure of its interior is empty, **meager** (of the first category) if it is a countable union of nowhere dense sets, and **comeager** if its complement is meager. A set $A\subseteq X$ has the **Baire property** if $A = U\triangle M$ for some open $U$ and meager $M$.

**Theorem (Baire category theorem).** A complete metric space is not the union of countably many nowhere dense sets; equivalently, a countable intersection of dense open subsets of a complete metric space is dense.

**Proof.** This is the theorem of *Metric, Uniform and Complete Spaces*; it is quoted here because the descriptive theory uses it in place of measure: a countable intersection of dense open sets is nonempty in every open ball, hence large in the topological sense, while its complement is meager. $\square$

**Theorem (Banach–Mazur game).** Let $A\subseteq X$ with $X$ complete and let the players choose nested nonempty open sets alternately. If $A$ is meager then the first player has a strategy ensuring that the unique point of the intersection lies outside $A$; if $A$ is comeager in a nonempty open set then the second player has a strategy ensuring that the point lies in $A$. The game characterises the Baire property in the sense that both conjuncts can be reversed when the play is restricted to balls of a fixed countable basis, and this is the classical criterion of Banach, Mazur and Oxtoby.

**Remark (measure and category).** The two notions of smallness — measure zero and meagerness — are independent: $\mathbb{R}$ is the union of a meager set and a null set, and there are meager sets of full measure and comeager null sets, obtained by the classical constructions with the rationals and the Cantor set. The descriptive theory of this article holds for both: the analytic sets are well behaved with respect to each.

## Analytic Sets

### The Souslin Operation

**Definition.** Let $\{A_s\}$ be a family of subsets of $X$ indexed by the finite sequences of natural numbers. The **Souslin operation** applied to the family is
$$
\mathcal{A}\{A_s\} = \bigcup_{x\in\mathcal{N}}\bigcap_{n\in\mathbb{N}}A_{x\restriction n},
$$
and a set is **analytic** ($\Sigma^1_1$) if it is of this form with each $A_s$ closed; a set is **coanalytic** ($\Pi^1_1$) if its complement is analytic.

**Theorem.** The analytic sets are exactly the continuous images of the Baire space, exactly the continuous images of closed subsets of the Baire space, and exactly the sets of the form $\{x : \exists y\ (x,y)\in F\}$ with $F$ closed in $X\times\mathcal{N}$. They are closed under countable unions and countable intersections and contain all the Borel sets.

**Proof sketch.** A closed set $F\subseteq X\times\mathcal{N}$ gives an analytic set by projection, with the projection exhibited as a Souslin operation applied to a basis at the closed set; conversely a Souslin operation on closed sets is the projection of the closed set $\{(x,y) : x\in A_{y\restriction n}\ \text{for all } n\}$, closed because each $A_s$ is closed and the conditions are finitely testable; and a continuous image is a projection by definition of the graph. The closure under countable unions and intersections is the standard "merging" of the Souslin schemes — the union of the sets $\mathcal{A}\{A_s^{(n)}\}$ is $\mathcal{A}\{B_s\}$ with $B_s$ indexed by pairing the first coordinate with $n$ — and the Borel sets are analytic by recursion on the hierarchy, since the sets $A_s$ may be chosen open and the operation reproduces the countable unions and intersections of Borel sets. $\square$

**Theorem (the analytic sets are not closed under complement).** There is a coanalytic set that is not analytic; the set $\mathrm{WF}$ of codes in $\mathcal{N}$ of well-founded relations on $\mathbb{N}$ is $\Pi^1_1$-complete, that is coanalytic but not analytic.

**Proof sketch.** A tree $T\subseteq\mathbb{N}^{<\mathbb{N}}$ is well-founded iff it has no infinite branch, so $\mathrm{WF} = \{T : \forall x\,\exists n\ (x\restriction n\notin T)\}$ is coanalytic; the completeness is proved by assigning to every analytic set a continuous reduction to $\mathrm{WF}$, using the tree of attempts to enter the set, and the failure of $\mathrm{WF}$ to be analytic follows from the strictness of the Borel hierarchy together with Souslin's theorem below. $\square$

### Separation and Souslin's Theorem

**Theorem (Lusin's separation theorem).** Two disjoint analytic subsets of a Polish space can be separated by a Borel set: there is a Borel $B$ with $A_1\subseteq B$ and $A_2\cap B = \emptyset$. Consequently a set is analytic and coanalytic at once if and only if it is Borel.

**Proof sketch.** For the separation, one uses the characterisation of disjoint analytic sets by the ranks of the trees: if the scheme of $A_1$ and that of $A_2$ had a common branch the sets would meet, so the tree of pairs admits a ranking by countable ordinals, and the sets of pairs below each rank produce a Borel separating set by transfinite induction on the rank. The second statement, **Souslin's theorem**, is the two-sided case: a Borel set is analytic and coanalytic by the previous subsection, and conversely a set that is both is separated from its complement, which is analytic, by a Borel set, whence the set itself is Borel. $\square$

**Theorem (the reduction theorem).** Every two coanalytic sets $C_1,C_2$ can be **reduced** by coanalytic sets: there are disjoint coanalytic $D_1\subseteq C_1$, $D_2\subseteq C_2$ with $D_1\cup D_2 = C_1\cup C_2$. Dually, every two analytic sets can be separated by analytic sets in the same sense.

**Proof sketch.** The dual statement for analytic sets follows from the separation theorem applied in the product with a parameter and the uniformity of the separating construction; the reduction is the dualisation of the separation, obtained by complementing and interchanging the two coordinates in the product. $\square$

**Theorem (Lusin–Sierpiński; the perfect set property).** Every uncountable analytic subset of a Polish space contains a perfect subset homeomorphic to the Cantor space, and hence has cardinality $2^{\aleph_0}$. Every analytic set has the Baire property and is universally measurable: it is measurable with respect to the completion of every $\sigma$-finite Borel measure on the space.

**Proof sketch.** For the perfect set property, write the set as the image of the Baire space under a continuous map and pull back the branching of the tree: an uncountable analytic set has a subtree with infinitely many branches, from which a perfect subset is built by the standard construction of a Cantor scheme of nested compact sets. For universality of measurability, write the analytic set as a Souslin operation on a closed family and use the fact that a closed set with a given finite approximation can be replaced by a compact set of almost the same measure, the outer measure being regular; one obtains that for every $\epsilon$ there is a compact subset of the analytic set whose complement in the set has measure less than $\epsilon$, which is measurability together with inner regularity. $\square$

**Remark (the limit of the method).** The three regularity properties — the perfect set property, the Baire property and measurability — hold for the analytic sets, and the passage to the coanalytic sets already requires a new axiom: the statement that every coanalytic set has the perfect set property is not provable in the standard axioms, and the hypothesis of **projective determinacy**, that every projective game is determined, implies the three properties for all projective sets. Gale and Stewart proved that the games of length $\omega$ on a Polish space with open payoff are determined; the determinacy of the higher classes is a hypothesis, and it is the organising principle of the subject at the levels above the analytic sets.

## The Projective Hierarchy and the Rank Theory

### The Projective Hierarchy

**Definition.** The **projective hierarchy** is defined by
$$
\Sigma^1_1 = \text{analytic sets}, \qquad \Pi^1_n = \{\,X\setminus A : A\in\Sigma^1_n\,\}, \qquad \Sigma^1_{n+1} = \{\,p(A) : A\subseteq X\times\mathcal{N},\ A\in\Pi^1_n\,\},
$$
with $\Delta^1_n = \Sigma^1_n\cap\Pi^1_n$; the sets in the union are the **projective sets**. The first levels satisfy $\Delta^1_1 = $ Borel, $\Sigma^1_1$ = analytic, $\Pi^1_1$ = coanalytic; and the classes are strictly increasing, by the same universal-set and diagonal argument as for the Borel hierarchy.

**Theorem (the regularity dichotomy).** Every analytic set is universally measurable and has the Baire property and the perfect set property. The corresponding statements at the level $\Sigma^1_2$ are independent of the standard axioms: if every set is constructible then there is a $\Delta^1_2$ well-ordering of the reals, whence a $\Sigma^1_2$ set that is not Lebesgue measurable and has no perfect subset; and, on the other hand, the hypothesis of projective determinacy implies the three properties for every projective set.

**Proof sketch.** The first statement is the theorem above. For the independence, the constructible well-ordering gives a $\Sigma^1_2$ well-ordering of $\mathbb{R}$, and a well-ordering of a perfect Polish space has an initial segment that is not measurable and has no perfect subset by the classical argument with the countable ordinals and the Fubini theorem; conversely, the determinacy of the projective games yields the properties through the game-theoretic characterisations of measure and category — the **Banach–Mazur game** for the Baire property and its measure analogue for measurability. $\square$

**Remark (what the hierarchy is for).** The value of the classification is that it assigns to each set of analysis the exact number of projections and complements needed to define it, and that a large part of the classical theory of point sets — the Baire property, measurability, the existence of perfect subsets, the existence of selections — can be settled by the level alone. This is the sense in which the analytic sets are, as stated in the introduction, the sets of analysis: they are exactly the sets defined with one existential quantifier over a complete separable space, and the theory shows that this class is closed under all the operations of analysis except complementation.

### Well-Founded Relations and Ranks

**Definition.** A relation $R\subseteq X\times X$ is **well-founded** if it has no infinite descending sequence; then every nonempty subset has a minimal element, and the **rank** $\rho(x)$ of a point is the ordinal defined by $\rho(x) = \sup\{\rho(y)+1 : yRx\}$, with $\rho(x) = 0$ if $x$ has no predecessor. The **rank** of a well-founded relation is $\sup_x\rho(x)$.

**Theorem (the boundedness theorem; Luzin–Sierpiński).** Let $R$ be a coanalytic well-founded relation whose domain is analytic. Then there is a countable ordinal $\alpha$ with $\rho(x)<\alpha$ for every $x$ in the domain. In particular the ranks of the well-founded trees in $\mathrm{WF}$ are unbounded in $\omega_1$, the domain of the extension relation there being coanalytic and not analytic; the bound applies exactly when the domain is analytic, and this asymmetry between an analytic and a merely coanalytic domain is what the next theorem sharpens.

**Proof sketch.** The rank function is $\Pi^1_1$ in the parameter; the boundedness follows because the statement "$\rho(x)\geq\alpha$" is analytic in $\alpha$ and the coanalytic well-foundedness prevents the class of ranks attained from having an analytic description closed upwards; the standard proof constructs, from a ranking whose ranks are unbounded in $\omega_1$, an infinite descending sequence, contradicting well-foundedness. $\square$

**Theorem (Kunen–Martin).** Let $R$ be a well-founded relation on a Polish space whose vertical sections are countable. If $R$ is analytic, then $R$ has bounded rank: $\rho(R)<\omega_1$. Consequently, if $S$ is a coanalytic well-founded relation on a Polish space and there is an analytic $R\subseteq S$ with countable sections and the same domain as $S$, then $S$ also has bounded rank.

**Proof sketch.** The statement "$\rho(x)\geq\alpha$" is analytic in the ordinal parameter $\alpha$ and the well-foundedness of $R$ forbids the ranks from exhausting $\omega_1$: an unbounded analytic family of ranks would yield, by the countable sections and a diagonal argument on the codes, an infinite descending sequence. $\square$

**Corollary.** The ranks of the well-founded trees are unbounded in $\omega_1$: for each countable $\alpha$ there is a well-founded tree of rank $\alpha$. On the well-founded trees consider the relation $R_0$ that holds of a pair of nodes $(v,u)$ of a common tree when $v$ is a proper initial segment of $u$; restricted to the well-founded trees it is coanalytic, well-founded, with finite — hence countable — sections, and its ranks are unbounded. Were $\mathrm{WF}$ analytic, $R_0$ restricted to it would be an analytic well-founded relation with countable sections of unbounded rank, contradicting the Kunen–Martin theorem. Hence $\mathrm{WF}$ is not analytic, and consequently $\Pi^1_1\not\subseteq\Sigma^1_1$.

**Remark (the invariant theory).** The ranking of coanalytic sets is the entry point of the invariant descriptive set theory, in which complete coanalytic sets are classified up to Borel isomorphism by the ranks and by the complexity of the reductions; the theory of the trees, the $\Pi^1_1$ ranks and the Kunen–Martin theorem is the machinery that makes "complete" a precise notion, and it is what the applications of the classification use.

## Summary

A Polish space is a separable space whose topology comes from a complete metric; $\mathbb{R}^n$, the closed and open subsets, the countable products and the standard spaces $F(X)$ of closed sets and $\mathcal{P}(X)$ of measures are Polish, and every nonempty Polish space is a continuous image of the Baire space $\mathcal{N} = \mathbb{N}^{\mathbb{N}}$, every compact metrisable space a continuous image of the Cantor space $2^{\mathbb{N}}$. The Borel hierarchy $\Sigma^0_\alpha$, $\Pi^0_\alpha$, $\Delta^0_\alpha$ is generated from the open sets by complementation and countable unions along the countable ordinals; it is strictly increasing at every level, by the universal-set and diagonal argument, and its union is the $\sigma$-algebra of Borel sets, of cardinality $2^{\aleph_0}$ in the uncountable case, every uncountable Polish space being Borel isomorphic to $\mathbb{R}$. The analytic sets are the continuous images of the Baire space, equivalently the projections of closed subsets of $X\times\mathcal{N}$, equivalently the sets obtained from closed sets by the Souslin operation; they are closed under countable unions and intersections, contain the Borel sets and are strictly larger. Two disjoint analytic sets are separated by a Borel set, by Lusin's separation theorem, and a set is Borel exactly when it is both analytic and coanalytic, by Souslin's theorem; the coanalytic sets are reducible, and $\mathrm{WF}$, the set of codes of well-founded trees, is coanalytic and complete for the class. Every uncountable analytic set contains a perfect subset and so has cardinality $2^{\aleph_0}$, and every analytic set has the Baire property and is universally measurable with respect to every $\sigma$-finite Borel measure, these being the sense in which the analytic sets are the well-behaved sets of analysis. The projective hierarchy continues by alternating projection and complement, the sets at the level $\Sigma^1_2$ and above have their regularity properties decided only under additional hypotheses — projective determinacy implies all three properties for all projective sets, while in the constructible universe there is a $\Sigma^1_2$ well-ordering of the reals and hence a non-measurable $\Sigma^1_2$ set — and the ranks of well-founded relations are bounded for analytic relations on analytic domains, which is the boundedness theorem and the origin of the invariant classification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{N} = \mathbb{N}^{\mathbb{N}}$ | Baire space |
| $\mathcal{C} = 2^{\mathbb{N}}$ | Cantor space |
| $N_s$ | Cylinder of the finite sequence $s$ |
| $F(X)$ | Closed subsets of $X$, with the Fell topology |
| $\mathcal{P}(X)$ | Borel probability measures on $X$, with the weak topology |
| $\Sigma^0_\alpha$, $\Pi^0_\alpha$, $\Delta^0_\alpha$ | Borel hierarchy at the level $\alpha<\omega_1$ |
| $\mathcal{A}\{A_s\}$ | Souslin operation on the family $\{A_s\}$ |
| $\Sigma^1_1$, $\Pi^1_1$ | Analytic, coanalytic sets |
| $\Sigma^1_n$, $\Pi^1_n$, $\Delta^1_n$ | Projective hierarchy |
| $\mathrm{WF}$ | Coanalytic complete set of codes of well-founded trees |
| $\rho(x)$, $\rho(R)$ | Rank of a point, rank of a well-founded relation |
| PD | Projective determinacy |



## Further Reading

- Mikhail Suslin, *Sur une définition des ensembles mesurables B sans nombres transfinis* (Comptes Rendus de l'Académie des Sciences 164, 1917), for the analytic sets and the theorem that Borel $=$ analytic $\cap$ coanalytic.
- Nikolai Lusin and Wacław Sierpiński, *Sur quelques propriétés des ensembles (A)* (Bulletin de l'Académie des Sciences de Cracovie, 1918), for the measurability and the Baire property of the analytic sets.
- Nikolai Lusin, *Leçons sur les ensembles analytiques et leurs applications* (Gauthier-Villars, 1930), for the separation and reduction theorems and the classical development.
- Wacław Sierpiński, *Hypothèse du continu* (Warsaw, 1934), for the continuum hypothesis and the classical descriptive theory.
- Yiannis N. Moschovakis, *Descriptive Set Theory* (2nd ed., American Mathematical Society, 2009), for the hierarchy, the ranks, the separation theorems and the determinacy hypotheses.
- Alexander S. Kechris, *Classical Descriptive Set Theory* (Springer, 1995), for the standard graduate account used throughout this article.
- Donald L. Cohn, *Measure Theory* (Birkhäuser, 1980), for the measurability of analytic sets and the regularity of Borel measures used in the proof.
- John C. Oxtoby, *Measure and Category* (2nd ed., Springer, 1980), for the Baire category theorem, the Banach–Mazur game and the independence of measure and category.
- Donald A. Martin, *Descriptive set theory: projective sets*, in *Handbook of Set-Theoretic Topology* (North-Holland, 1984), for projective determinacy and its consequences.
