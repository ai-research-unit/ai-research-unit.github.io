# __List of Universal Properties__

## Introduction

This article lists the objects of the corpus that are defined by a universal property, that is, by the maps into or out of them rather than by a construction. The pattern is the same in every case: an object is required, together with a map satisfying a condition, such that every other candidate factors through it uniquely. The corpus meets the pattern in the free objects, in the quotients, in the tensor products, in the localizations, in the completions and in the products and coproducts.

Every entry points to the article that introduces the object and states the property that fixes it. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a candidate for which the required factorisation fails, with the failure named and the article that records it.

## Free Objects

A **free object** is the solution of a universal arrow from a set to a forgetful functor: the free monoid on a set is the universal monoid the set maps into, the free group and the free module are its analogues for groups and for modules, and the free algebra is the universal algebra containing a given module. In each case the universal map is the insertion of the generators, and a homomorphism out of the free object is determined by its values on them.

| Object | The property it has | Introduced in |
|---|---|---|
| Free monoid $X^*$ | the universal monoid on a set, with words as elements | *Universal Properties and Categories* |
| Free group $F(X)$ | the universal group on a set, with reduced words as elements | *Generators, Presentations and Free Products* |
| Free abelian group | the universal abelian group on a set, with rank as its invariant | *Infinite Abelian Groups* |
| Free module $R^{(I)}$ | the universal $R$-module on a set, with basis the inserted elements | *Direct Sums, Free Modules and Rank* |
| Free algebra $T(V)$ | the universal associative algebra on a module, the tensor algebra | *Tensor Powers and the Free Algebra* |
| Free commutative algebra $\operatorname{Sym}(V)$ | the universal commutative algebra on a module, the symmetric algebra | *The Symmetric Algebra* |
| Polynomial algebra $R[x_1,\dots,x_n]$ | the free commutative $R$-algebra on $n$ generators | *Polynomial Rings and Rational Functions* |
| Free product $G_1 * G_2$ | the coproduct of groups, the universal group receiving both factors | *Generators, Presentations and Free Products* |
| Free product of algebras $A \sqcup B$ | the coproduct of associative algebras | *Tensor Products of Algebras* |
| Free operad | the free monoid in symmetric sequences, with trees as components | *Operads* |
| Non-example: $\mathbb{Z}/n\mathbb{Z}$ as a $\mathbb{Z}$-module | a module that fails to be free: it has no basis | *Direct Sums, Free Modules and Rank* |
| Non-example: a group with a presentation $\langle X \mid R \rangle$, $R \neq 1$ | a quotient of the free group that fails freeness | *Generators, Presentations and Free Products* |

## Products, Coproducts and Limits

The **product** and the **coproduct** are the universal objects receiving the projections and carrying the injections; the **initial** and **terminal** objects are their empty cases, the **equaliser** and the **coequaliser** their diagrammatic forms, and the **limit** and the **colimit** the general construction. In the module-theoretic articles the coproduct is the direct sum and the product the direct product, and the two differ for infinite families. The **pushout** is the coproduct under a common base, which for commutative algebras is the tensor product.

| Object | The property it has | Introduced in |
|---|---|---|
| Initial and terminal objects | the universal objects mapping out of and into every object | *Universal Properties and Categories* |
| Product $A \times B$ | the universal object with two projections | *Universal Properties and Categories* |
| Coproduct $A + B$ | the universal object with two injections | *Universal Properties and Categories* |
| Equaliser and coequaliser | the universal object equalising or coequalising a parallel pair | *Universal Properties and Categories* |
| Limit and colimit | the universal cone and cocone over a diagram | *Universal Properties and Categories* |
| Direct sum $\bigoplus_i M_i$ | the coproduct of modules, the finitely supported submodule of the product | *Direct Sums, Free Modules and Rank* |
| Direct product $\prod_i M_i$ | the product of modules, with its coordinate projections | *Direct Sums, Free Modules and Rank* |
| Pushout of commutative algebras | the coproduct under a common base, given by $\otimes_C$ | *Tensor Products of Algebras* |
| Non-example: $\prod_i M_i$ for infinite $I$ | the product is not the coproduct: its elements need not be finitely supported | *Direct Sums, Free Modules and Rank* |
| Non-example: a set with two elements | the coproduct in $\mathbf{Set}$ is the disjoint union, not the union | *Sets, Functions and Relations* |

## Quotients

A **quotient** is a coequaliser: the quotient of a set by an equivalence relation, of a group by a normal subgroup, of a ring by a two-sided ideal, of a module by a submodule and of an algebra by a two-sided ideal are the universal objects in which the collapsed elements become equal. The **normal closure** of a set of relations is the kernel of the corresponding quotient of the free group, and a **presentation** records the quotient in the language of generators and relations.

| Object | The property it has | Introduced in |
|---|---|---|
| Quotient set $X/{\sim}$ | the universal set in which equivalent elements coincide | *Sets, Functions and Relations* |
| Quotient group $G/N$ | the universal group killing a normal subgroup | *Groups* |
| Abelianisation $G^{\mathrm{ab}}$ | the universal abelian quotient of a group | *Groups* |
| Quotient ring $R/I$ | the universal ring killing a two-sided ideal | *Rings* |
| Quotient module $M/N$ | the universal module killing a submodule | *Modules* |
| Quotient algebra $A/I$ | the universal algebra killing a two-sided ideal | *Ideals and Quotients of Algebras* |
| Normal closure $\langle\langle R \rangle\rangle$ | the kernel of the quotient of $F(X)$ by the relations $R$ | *Generators, Presentations and Free Products* |
| Non-example: the quotient of a group by a non-normal subgroup | the candidate fails: only normal subgroups carry a group structure on the cosets | *Groups* |
| Non-example: the quotient of a ring by a one-sided ideal | the candidate fails: the multiplication is not well defined on the cosets | *Rings* |

## Tensor Products

The **tensor product** is the universal object representing the bilinear maps; over a commutative ring it is the balanced product, and it is the underlying construction of the tensor, symmetric, exterior and Clifford algebras alike. The **tensor power**, the **symmetric power** and the **exterior power** are its quotients or its graded pieces, and each of them has the universal property of the multilinear maps it represents.

| Object | The property it has | Introduced in |
|---|---|---|
| Balanced product $M \otimes_R N$ | the universal object representing the $R$-bilinear maps | *The Balanced Product* |
| Tensor product of algebras $A \otimes_R B$ | the universal algebra receiving two commuting images | *Tensor Products of Algebras* |
| Bimodule tensor $M_A \otimes_A {}_A N$ | the balanced product over a non-commutative ring, forcing centrality | *The Balanced Product over an Algebra* |
| Tensor power $V^{\otimes n}$ | the universal object for the $n$-multilinear maps | *Tensor Powers and the Free Algebra* |
| Symmetric power $\operatorname{Sym}^n M$ | the universal object for the symmetric $n$-multilinear maps | *Symmetric Powers* |
| Symmetric algebra $\operatorname{Sym}(M)$ | the quotient of the tensor algebra by $x \otimes y - y \otimes x$ | *The Symmetric Algebra* |
| Exterior power $\Lambda^n M$ | the universal object for the alternating $n$-multilinear maps | *Exterior Powers* |
| Exterior algebra $\Lambda(M)$ | the quotient of the tensor algebra by $x \otimes x$ | *The Exterior Algebra* |
| Clifford algebra $\mathrm{Cl}(V,Q)$ | the quotient of $T(V)$ by $x \otimes x - Q(x)$ | *The Clifford Algebra* |
| Non-example: the tensor product over a non-commutative ring without a bimodule structure | the candidate fails: $M \otimes_R N$ requires one side left and one right | *The Balanced Product over an Algebra* |

## Localizations and Fraction Objects

A **localization** inverts a chosen set of elements and is universal among rings in which they become units. Its two extreme cases are the **fraction field** of an integral domain, the initial field in which the domain embeds, and the **local ring** at a prime ideal; for modules the same construction is the localisation of a module. The non-commutative analogue is the division ring of fractions of an Ore domain.

| Object | The property it has | Introduced in |
|---|---|---|
| Localization $S^{-1}R$ | the universal ring in which every element of $S$ becomes a unit | *Localization and the Fraction Field* |
| Fraction field $\operatorname{Frac}(R)$ | the initial field in which an integral domain embeds | *Localization and the Fraction Field* |
| Local ring $R_\mathfrak{p}$ | the localization at a prime ideal, with a single maximal ideal | *Localization and the Fraction Field* |
| Localization of a module $S^{-1}M$ | the universal module over $S^{-1}R$ receiving $M$ | *Localization and Completion of Modules* |
| Total ring of fractions | the localization inverting the nonzero non-zero-divisors | *Localization and the Fraction Field* |
| Division ring of fractions of an Ore domain | the non-commutative analogue of the fraction field | *Ore Domains and Division Rings of Fractions* |
| Non-example: $\operatorname{Frac}(R)$ for a ring with zero divisors | the candidate fails: the fraction field exists only for a domain | *Localization and the Fraction Field* |
| Non-example: a division ring of fractions for the free algebra | the candidate fails: the free algebra is not an Ore domain | *Ore Domains and Division Rings of Fractions* |

## Completions

A **completion** is the universal complete object into which the given object embeds densely. The corpus meets the algebraic $I$-adic completion — of a ring, of a module and, for $I = (x_1,\dots,x_n)$, of the polynomial algebra as the formal power series algebra — and, once a distance is available, the metric completion, the profinite completion and the Dedekind completion.

| Object | The property it has | Introduced in |
|---|---|---|
| $I$-adic completion $\hat A = \varprojlim A/I^k$ | the universal complete ring receiving $A$ | *Localization and Completion of Modules* |
| Formal power series algebra $R[[x_1,\dots,x_n]]$ | the $I$-adic completion of the polynomial algebra | *Formal Power Series and Completion* |
| Associated graded algebra $\operatorname{gr}_{\mathfrak m} A$ | the graded object attached to an $I$-adic filtration | *Formal Power Series and Completion* |
| Metric completion | the universal complete metric space receiving a metric space | *Metric, Uniform and Complete Spaces* |
| Profinite completion | the inverse limit of the finite quotients, universal among profinite groups | *Profinite Groups and the Krull Topology* |
| Dedekind completion | the universal complete ordered field extension of an ordered field | *Real-Closed and Complete Ordered Fields* |
| Non-example: the category of fields | the coproduct fails to exist there: $\mathbb{C} \otimes_\mathbb{R} \mathbb{C}$ is a ring but not a field | *Tensor Products of Algebras* |

## Summary

The list gathers the objects of the corpus that are defined by a universal property. The free objects are the free monoid, the free group, the free abelian group, the free module, the free algebra, the free commutative algebra, the polynomial algebra, the free product and the free operad; the products and coproducts are the initial and terminal objects, the product, the coproduct, the equaliser and coequaliser, the limit and colimit, the direct sum and product and the pushout; the quotients are the quotient set, group, ring, module and algebra, with the abelianisation and the normal closure; the tensor constructions are the balanced product, the tensor product of algebras, the bimodule tensor, the tensor, symmetric and exterior powers and algebras and the Clifford algebra; the localizations are the localization of a ring, the fraction field, the local ring, the localization of a module, the total ring of fractions and the division ring of fractions of an Ore domain; and the completions are the $I$-adic completion, the formal power series algebra, the metric completion, the profinite completion and the Dedekind completion. The non-examples — the non-free module, the non-free presented group, the infinite direct product, the quotient by a non-normal subgroup, the quotient by a one-sided ideal, the tensor product over a non-commutative ring without a bimodule structure, the fraction field of a ring with zero divisors, the division ring of fractions of the free algebra and the missing coproduct in the category of fields — name the hypothesis that each fails.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $X^*$ | free monoid on a set $X$ |
| $F(X)$ | free group on a set $X$ |
| $R^{(I)}$, $R^n$ | free module on the index set $I$ |
| $\mathbb{Z}$, $\mathbb{R}$, $\mathbb{C}$ | the integers, the reals, the complex numbers |
| $T(V)$, $\operatorname{Sym}(V)$, $\Lambda(V)$, $\mathrm{Cl}(V,Q)$ | tensor, symmetric, exterior and Clifford algebras |
| $V^{\otimes n}$, $\operatorname{Sym}^n M$, $\Lambda^n M$ | tensor, symmetric and exterior powers |
| $M \otimes_R N$ | balanced product over $R$ |
| $A \sqcup B$, $A \otimes_C B$ | free product and pushout of algebras |
| $S^{-1}R$, $S^{-1}M$ | localizations of a ring and of a module |
| $\operatorname{Frac}(R)$ | fraction field |
| $R_\mathfrak{p}$ | localization at a prime ideal |
| $\hat A = \varprojlim A/I^k$ | $I$-adic completion |
| $R[[x_1,\dots,x_n]]$ | formal power series algebra |
| $\bigoplus_i M_i$, $\prod_i M_i$ | direct sum and direct product |
| $G_1 * G_2$, $G_1 *_H G_2$ | free product and free product with amalgamation |
| $\langle X \mid R\rangle$, $\langle\langle R\rangle\rangle$ | presentation; normal closure of the relations |

## Further Reading

- Saunders Mac Lane, *Categories for the Working Mathematician* (Springer, 2nd ed. 1998), for universal arrows, adjunctions and the limit and colimit constructions in their general form.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the universal properties of the free objects, the tensor product and the symmetric and exterior algebras.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the tensor, symmetric and exterior algebras and the localization and fraction field constructions.
- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (Addison–Wesley, 1969), for localization, the $I$-adic completion and the formal power series ring.
