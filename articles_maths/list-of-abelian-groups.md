# __List of Abelian Groups__

## Introduction

This article lists the abelian groups the corpus meets, grouped by the structure theorem that classifies each family: the finitely generated groups, classified by a free rank and a torsion part; the torsion and the torsion-free groups, split by the torsion subgroup and the rank; the divisible groups, classified by their rank; and the profinite abelian groups, which carry a topology as well as a group law. Beside each family the list names the theorem that classifies it.

Every entry points to the article that introduces the group and names the invariant recorded there. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being an abelian group that fails one property of its family, with the failure named and the article that records it.

## Finitely Generated Abelian Groups

A finitely generated abelian group is a direct sum of a free abelian group of finite rank and a finite abelian group, and the finite part is a direct sum of cyclic groups. The invariants are unique in two normal forms, the **invariant factors** $d_1 \mid \cdots \mid d_k$ and the **elementary divisors** $p_i^{e_i}$, and the theorem is the case $R = \mathbb{Z}$ of the structure theorem for finitely generated modules over a principal ideal domain.

| Group | The property it has | Introduced in |
|---|---|---|
| $\mathbb{Z}^r$ | free abelian of rank $r$; the free part of a finitely generated group | *Finitely Generated Abelian Groups* |
| $\mathbb{Z}/n\mathbb{Z}$ | cyclic of order $n$, with $n$ decomposed into prime powers | *Finitely Generated Abelian Groups* |
| Finite abelian group | a direct sum of cyclic groups of prime-power order, uniquely | *Finitely Generated Abelian Groups* |
| $\mathbb{Z}/p^{e_1}\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/p^{e_k}\mathbb{Z}$ | the elementary-divisor form of the $p$-primary part | *Finitely Generated Abelian Groups* |
| Group with invariant factors $d_1 \mid \cdots \mid d_k$ | the divisibility-ordered form of the torsion part | *Finitely Generated Abelian Groups* |
| Relations matrix and Smith normal form | the algorithm computing the invariants from a presentation | *Finitely Generated Abelian Groups* |
| $(\mathbb{Z},+)$ | free abelian of rank $1$; its torsion subgroup is trivial | *Infinite Abelian Groups* |
| Non-example: $\mathbb{Z}^r$ with $r \geq 1$ | fails to be torsion: it has no nonzero element of finite order | *Infinite Abelian Groups* |
| Non-example: $\mathbb{Z}/n\mathbb{Z}$ with $n \geq 2$ | fails to be torsion-free: every element has finite order | *Infinite Abelian Groups* |
| Non-example: the free abelian group of rank $\geq 2$ | fails to be a free group: it satisfies $[a,b]=1$ | *Generators, Presentations and Free Products* |

## Torsion and Torsion-Free Groups

The **torsion subgroup** $T(A)$ collects the elements of finite order, and $A$ is torsion, torsion-free or mixed according to what $T(A)$ is. The torsion groups decompose into their **primary components** $A_p$, and the countable primary groups are classified by the **Ulm invariants**; the torsion-free groups are classified by their rank only in the free case, the countable torsion-free groups admitting no comparably simple description.

| Group | The property it has | Introduced in |
|---|---|---|
| Torsion subgroup $T(A)$ | the elements of finite order; a subgroup | *Infinite Abelian Groups* |
| $A[p]$ | the elements of order dividing $p$ | *Infinite Abelian Groups* |
| Primary component $A_p$ | the $p$-primary summand of a torsion group | *Infinite Abelian Groups* |
| Torsion group | a group with $T(A)=A$; a direct sum of its primary components | *Infinite Abelian Groups* |
| Torsion-free group | a group with $T(A)=0$; contains a free subgroup of the same rank | *Infinite Abelian Groups* |
| Rank $\operatorname{rk}(A)$ | the cardinality of a maximal linearly independent set | *Infinite Abelian Groups* |
| Prüfer $p$-group $\mathbb{Z}[p^\infty]$ | the $p$-primary torsion group of the $p^n$-th roots of unity | *Infinite Abelian Groups* |
| Ulm invariants $U(k,G)$ | the complete invariants of a countable primary group | *Infinite Abelian Groups* |
| Non-example: a countable torsion-free group of rank $\geq 2$ | fails to be classified by rank alone: the torsion-free classification is intractable | *Infinite Abelian Groups* |
| Non-example: $\mathbb{Q}$ | fails to be free: it is torsion-free but has no basis over $\mathbb{Z}$ | *Infinite Abelian Groups* |

## Divisible Groups

A **divisible** group is one in which every element is divisible by every positive integer; the divisible groups are classified by their rank as direct sums of copies of $\mathbb{Q}$ and of the Prüfer groups $\mathbb{Z}[p^\infty]$. Every group embeds in a divisible group, its **divisible hull**, which is unique up to isomorphism.

| Group | The property it has | Introduced in |
|---|---|---|
| Divisible group $D$ | every element is $n$-divisible for every $n$ | *Infinite Abelian Groups* |
| $\mathbb{Q}$ | the divisible torsion-free group of rank $1$; the divisible hull of $\mathbb{Z}$ | *Infinite Abelian Groups* |
| $\mathbb{Q}/\mathbb{Z}$ | the torsion divisible group, the direct sum of the Prüfer groups | *Modules over a PID* |
| $\mathbb{Z}[p^\infty]$ | the Prüfer $p$-group; divisible and torsion | *Infinite Abelian Groups* |
| $D^{(I)}$ | the direct sum of $|I|$ copies of the fixed rank-one divisible group $D$; the general divisible torsion-free group | *Infinite Abelian Groups* |
| Divisible hull | the smallest divisible group containing a given group; unique | *Infinite Abelian Groups* |
| Non-example: $\mathbb{Z}$ | fails divisibility: $1$ is not divisible by $2$ | *Infinite Abelian Groups* |
| Non-example: a finite abelian group | fails divisibility: no nonzero element is infinitely divisible | *Infinite Abelian Groups* |

## Profinite and Topological Abelian Groups

A **profinite abelian group** is an inverse limit of finite abelian groups, equivalently a compact totally disconnected abelian group; the group carries a topology as well as a group law, and the topological theory, including Pontryagin duality, belongs to Part II. The additive groups $\mathbb{Z}_p$ and the profinite completion $\hat{\mathbb{Z}}$ are the standard examples, and the Galois groups of the arithmetic articles are their non-abelian relatives.

| Group | The property it has | Introduced in |
|---|---|---|
| $\mathbb{Z}_p$ | the additive group of $p$-adic integers; profinite, torsion-free and not divisible | *Profinite Groups and the Krull Topology* |
| $\hat{\mathbb{Z}}$ | the profinite completion of $\mathbb{Z}$, isomorphic to $\prod_p \mathbb{Z}_p$ | *Profinite Groups and the Krull Topology* |
| Profinite completion $\hat{A}$ | the inverse limit of the finite quotients of $A$ | *Profinite Groups and the Krull Topology* |
| Inverse limit of finite abelian groups | a compact totally disconnected abelian group | *Profinite Groups and the Krull Topology* |
| $\mathbb{Q}_p$ | the additive group of $p$-adic numbers; locally compact, not compact | *The $p$-adic Numbers* |
| Pontryagin dual $\hat{A} = \operatorname{Hom}(A,\mathbb{R}/\mathbb{Z})$ | the dual of a locally compact abelian group; an exact contravariant equivalence | *Pontryagin Duality* (Part II) |
| Non-example: $\mathbb{Z}_p$ | fails divisibility: $p$ does not divide $1$ in $\mathbb{Z}_p$ | *The $p$-adic Numbers* |
| Non-example: $\mathbb{Q}$ with the discrete topology | fails compactness: its Pontryagin dual is not compact | *Pontryagin Duality* (Part II) |

## Abelian Groups as Modules and as Coefficients

Because an abelian group is exactly a module over $\mathbb{Z}$, the module theory of the corpus is the abelian theory in a general ring: the structure theorem over a principal ideal domain applies to $\mathbb{Z}$, the rank is the free rank, and the annihilator of an element is the ideal generated by its order. Abelian groups also serve as the coefficient objects of group cohomology and homology.

| Object | The property it has | Introduced in |
|---|---|---|
| Abelian group as a $\mathbb{Z}$-module | the scalar action $na$ is the integer multiple | *Modules* |
| Structure theorem over a PID | the classification of finitely generated modules, hence of finitely generated abelian groups | *Modules over a PID* |
| Torsion submodule $M_{\mathrm{tor}}$ | the module form of the torsion subgroup | *Modules over a PID* |
| Annihilator $\operatorname{Ann}(m)$ | the ideal of scalars killing $m$, generated by $\operatorname{ord}(m)$ over $\mathbb{Z}$ | *Modules over a PID* |
| Coefficient group of group cohomology | the abelian group $M$ in $H^n(G,M)$ | *Group Cohomology* |
| Schur multiplier $H_2(G,\mathbb{Z})$ | the second homology with abelian coefficients | *Group Cohomology* |
| Non-example: a non-free finitely generated torsion-free module over a general ring | fails the PID structure theorem: over a general ring it need not be free | *Modules* |

## The Classification in Each Family

Each family is pinned by one invariant, and the table gathers the four statements so that the family and its classifying theorem stand together.

| Family | The classifying invariant | The theorem | Introduced in |
|---|---|---|---|
| Finitely generated | the rank and the invariant factors $d_1 \mid \cdots \mid d_k$ | the structure theorem for finitely generated modules over a PID | *Finitely Generated Abelian Groups* |
| Torsion | the primary components, and the Ulm invariants within a countable primary group | Ulm's theorem | *Infinite Abelian Groups* |
| Torsion-free | the rank | rank classifies the free and the divisible cases, and fails in general | *Infinite Abelian Groups* |
| Divisible | the rank, with one copy of $\mathbb{Q}$ or $\mathbb{Z}[p^\infty]$ per rank | the structure theorem for divisible groups | *Infinite Abelian Groups* |
| Profinite | the Pontryagin dual, a discrete torsion group | Pontryagin duality | *Pontryagin Duality* (Part II) |

## Summary

The list gathers the abelian groups of the corpus. The finitely generated groups are the free abelian groups and the finite abelian groups, classified by the invariant factors and the elementary divisors; the torsion and torsion-free groups are separated by the torsion subgroup, the torsion groups decomposing into primary components and the countable primary groups classified by the Ulm invariants; the divisible groups are the direct sums of copies of $\mathbb{Q}$ and of the Prüfer groups, classified by their rank, with the divisible hull as the universal embedding; and the profinite abelian groups are the inverse limits of finite abelian groups, with $\mathbb{Z}_p$ and $\hat{\mathbb{Z}}$ as the standard examples and Pontryagin duality as their topological theory. The abelian groups are also the modules over $\mathbb{Z}$ and the coefficients of group cohomology. The non-examples — $\mathbb{Z}^r$, $\mathbb{Z}/n\mathbb{Z}$, the free abelian group of rank at least two, the countable torsion-free group of rank at least two, $\mathbb{Q}$ as a non-free group, $\mathbb{Z}$ and a finite group as non-divisible groups, $\mathbb{Z}_p$, and $\mathbb{Q}$ with the discrete topology — name the property that each fails.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$, $\mathbb{Z}^r$, $\mathbb{Z}/n\mathbb{Z}$ | integers, free abelian of rank $r$, cyclic group |
| $T(A)$, $A_p$, $A[p]$ | torsion subgroup, primary component, $p$-torsion |
| $\operatorname{rk}(A)$ | rank of an abelian group |
| $U(k,G)$ | Ulm invariant of a countable primary group |
| $\mathbb{Q}$, $\mathbb{Q}/\mathbb{Z}$ | rationals and the torsion divisible group |
| $\mathbb{Z}[p^\infty]$ | Prüfer $p$-group |
| $D$, $D^{(I)}$ | rank-one divisible group and its direct sum |
| $\mathbb{Z}_p$, $\hat{\mathbb{Z}}$, $\mathbb{Q}_p$ | $p$-adic integers, profinite integers, $p$-adic numbers |
| $\operatorname{Hom}(A,\mathbb{R}/\mathbb{Z})$ | Pontryagin dual |
| $\bigoplus_i A_i$, $\prod_i A_i$ | direct sum and direct product |
| $d_1 \mid \cdots \mid d_k$, $p_i^{e_i}$ | invariant factors and elementary divisors |

## Further Reading

- László Fuchs, *Infinite Abelian Groups*, Vols. I–II (Academic Press, 1970–1973), for the torsion, torsion-free, divisible and primary classifications and the Ulm invariants.
- Irving Kaplansky, *Infinite Abelian Groups* (University of Michigan Press, 1954), for the structure theory and the divisible and reduced decompositions.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, 4th ed. 1995), for the finitely generated structure theorem and the invariant-factor and elementary-divisor forms.
- Sidney A. Morris, *Pontryagin Duality and the Structure of Locally Compact Abelian Groups* (Cambridge University Press, 1977), for the profinite and topological abelian groups and their duality.
