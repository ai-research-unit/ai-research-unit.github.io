
# __List of Topological Spaces by Separation and Compactness__

## Introduction

This article lists the separation axioms and the compactness conditions that Parts I to III of the corpus use, and tabulates which of the spaces of the corpus satisfies which. The separation axioms record how far a space separates points from points, points from closed sets, and closed sets from closed sets; the compactness conditions record how far the open covers of a space can be reduced to a finite, a countable or a locally finite family. The two families are the ones that decide which theorems apply to a space, and the article collects them in one place so that the same space can be read down a column.

Every entry points to the article that introduces the space, the axiom or the condition, and every space tabulated appears in Parts I to III. The article introduces nothing and proves nothing: it records the implications that the corpus establishes and the examples that show the implications do not reverse, and it does not restate a definition or give a proof.

The article records examples and non-examples side by side. Beside the spaces that satisfy an axiom or a compactness condition it lists the spaces that fail it — the cofinite topology on an infinite set, which is $T_1$ and not Hausdorff; the Sorgenfrey plane, which is Tychonoff and not normal; Mysior's example, which is regular and not completely regular; the long line, which is countably compact and not compact and not paracompact — each with the failure named and the article that records it.

## The Separation Axioms

The axioms are those of *Topological Spaces* and *Metrisation and Separation Axioms*, where the hierarchy, its permanence and the metrisation theorems are proved. The convention of the corpus is that $T_3$, $T_{3\frac12}$ and $T_4$ denote the corresponding condition together with $T_1$.

| Axiom | What it separates | Introduced in |
|---|---|---|
| $T_0$ | any two distinct points, by an open set containing exactly one of them | *Topological Spaces* |
| $T_1$ | any two distinct points, by open sets each avoiding the other; equivalently points are closed | *Topological Spaces* |
| Hausdorff ($T_2$) | any two distinct points, by disjoint open sets; equivalently limits of nets are unique | *Topological Spaces* |
| regular ($T_3$) | a point from a closed set not containing it, by disjoint open sets; with $T_1$, the regular Hausdorff spaces | *Metrisation and Separation Axioms* |
| completely regular ($T_{3\frac12}$) | a point from a closed set not containing it, by a continuous function to $[0,1]$; with $T_1$, the Tychonoff spaces | *Metrisation and Separation Axioms* |
| normal ($T_4$) | two disjoint closed sets, by disjoint open sets; with $T_1$, the normal Hausdorff spaces | *Metrisation and Separation Axioms* |
| perfectly normal | two disjoint closed sets, by a continuous function; every closed set a countable intersection of open sets | *Metrisation and Separation Axioms* |
| collectionwise normal | a discrete family of closed sets, by a discrete family of open sets | *Paracompactness and Partitions of Unity* |

The implications run one way only:

| Implication | The condition that strengthens it | Introduced in |
|---|---|---|
| $T_4 \Rightarrow T_{3\frac12} \Rightarrow T_3 \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0$ | each condition implies the one to its right; no arrow reverses | *Metrisation and Separation Axioms* |
| compact Hausdorff $\Rightarrow$ normal | every compact Hausdorff space is normal, hence satisfies Urysohn and Tietze | *Topological Spaces* |
| metric $\Rightarrow$ perfectly normal, collectionwise normal | every metrisable space is perfectly normal and collectionwise normal | *Metrisation and Separation Axioms* |
| paracompact Hausdorff $\Rightarrow$ normal | paracompactness supplies the shrinkings from which the separation is built | *Paracompactness and Partitions of Unity* |
| normal $\Rightarrow$ Tietze, Urysohn | the extension and separation theorems hold in every normal space | *Metrisation and Separation Axioms* |

## The Spaces That Separate the Axioms

The axioms do not collapse, and each collapse is prevented by a space of the corpus. The failures are recorded beside the spaces that satisfy the axiom, in the same table.

| Space | $T_0$ | $T_1$ | Hausdorff | regular | completely regular | normal | metrisable |
|---|---|---|---|---|---|---|---|
| $\mathbb{R}$, $\mathbb{R}^n$, $\mathbb{Q}$ | yes | yes | yes | yes | yes | yes | yes |
| $\mathbb{C}$, $\mathbb{C}^n$ | yes | yes | yes | yes | yes | yes | yes |
| $S^n$, $T^n$, $\mathbb{RP}^n$, $\mathbb{CP}^n$ | yes | yes | yes | yes | yes | yes | yes |
| the Cantor set, $\mathbb{Z}_p$, a compact metric space | yes | yes | yes | yes | yes | yes | yes |
| a compact Hausdorff space | yes | yes | yes | yes | yes | yes | not always |
| a paracompact Hausdorff space | yes | yes | yes | yes | yes | yes | not always |
| a metric space | yes | yes | yes | yes | yes | yes | yes |
| $\beta\mathbb{N}$ | yes | yes | yes | yes | yes | yes | no |
| the long line $L$, $[0,\omega_1)$, $[0,\omega_1]$ | yes | yes | yes | yes | yes | yes | no |
| the Sorgenfrey line $\mathbb{R}_S$ | yes | yes | yes | yes | yes | yes | no |
| the Sorgenfrey plane $\mathbb{R}_S^2$ | yes | yes | yes | yes | yes | **no** | no |
| the Niemytzki plane | yes | yes | yes | yes | yes | **no** | no |
| Mysior's example | yes | yes | yes | yes | **no** | **no** | no |
| the cofinite topology on an infinite set | yes | yes | **no** | **no** | **no** | **no** | no |
| the indiscrete topology on two points | **no** | **no** | **no** | yes | yes | yes | no |
| $[0,1]^{I}$ for uncountable $I$ | yes | yes | yes | yes | yes | **no** | no |
| $\operatorname{Spec} R$ with the Zariski topology | yes | **no** | **no** | — | — | — | no |

The rows are read as follows. The cofinite topology is $T_1$ and not Hausdorff, and since $T_1$ together with normality implies Hausdorff, it is neither regular nor normal; this is the counterexample of *Topological Spaces*. The Sorgenfrey plane and the Niemytzki plane are Tychonoff and not normal, so $T_{3\frac12}$ does not imply $T_4$, and the Sorgenfrey plane is a finite product of normal spaces that is not normal. Mysior's example is regular and not completely regular, so $T_3$ does not imply $T_{3\frac12}$. The indiscrete topology is regular, completely regular and normal and not $T_1$, which is why the corpus defines $T_3$, $T_{3\frac12}$ and $T_4$ with the $T_1$ clause. The product of uncountably many intervals is compact Hausdorff and not normal, so normality is not productive. The prime spectrum is $T_0$ and not $T_1$ whenever a nonzero prime is contained in another, so it is not metrisable, and this failure is one of separation and not of countability.

## The Compactness and Countability Conditions

| Condition | Its definition | Introduced in |
|---|---|---|
| compact | every open cover has a finite subcover; equivalently every ultrafilter converges | *Topological Spaces* |
| countably compact | every countable open cover has a finite subcover; equivalently every sequence has a cluster point | *Paracompactness and Partitions of Unity* |
| sequentially compact | every sequence has a convergent subsequence; equivalent to compactness in a metric space | *Topological Spaces* |
| Lindelöf | every open cover has a countable subcover | *Paracompactness and Partitions of Unity* |
| $\sigma$-compact | a countable union of compact subsets | *Topological Spaces* |
| locally compact | every point has a neighbourhood base of compact neighbourhoods | *Topological Spaces* |
| paracompact | every open cover has a locally finite open refinement | *Paracompactness and Partitions of Unity* |
| fully normal | every open cover has an open star refinement; equivalent to paracompactness for Hausdorff spaces | *Paracompactness and Partitions of Unity* |
| totally bounded | for every $\varepsilon$ a finite cover by sets of diameter less than $\varepsilon$ | *Metric, Uniform and Complete Spaces* |

The implications among the conditions are these, and each is recorded with the article that proves it:

| Implication | The statement | Introduced in |
|---|---|---|
| compact $\Rightarrow$ countably compact | a finite subcover is a finite subcover of every countable subfamily | *Topological Spaces* |
| compact $\Rightarrow$ Lindelöf | a finite subcover is countable | *Paracompactness and Partitions of Unity* |
| compact $\Rightarrow$ $\sigma$-compact | the space itself is the single compact set | *Topological Spaces* |
| compact Hausdorff $\Rightarrow$ paracompact | a finite subcover is locally finite | *Paracompactness and Partitions of Unity* |
| paracompact + countably compact $\Rightarrow$ compact | a locally finite family of nonempty sets is finite in a countably compact space | *Paracompactness and Partitions of Unity* |
| countably compact + Lindelöf $\Rightarrow$ compact | the countable subcover has a finite subcover | *Paracompactness and Partitions of Unity* |
| metric: compact $\Leftrightarrow$ sequentially compact $\Leftrightarrow$ complete + totally bounded | the metric characterisation of compactness | *Topological Spaces*; *Metric, Uniform and Complete Spaces* |
| metric $\Rightarrow$ paracompact (Stone) | every metrisable space is paracompact | *Paracompactness and Partitions of Unity* |
| Lindelöf + regular $\Rightarrow$ paracompact | the countable refinement is locally finite | *Paracompactness and Partitions of Unity* |

## The Matrix of the Standard Spaces

The following table records the compactness and countability conditions satisfied by the spaces of the corpus. A blank cell is not a claim of failure; it records that the corpus does not establish the condition for that space.

| Space | compact | countably compact | Lindelöf | $\sigma$-compact | locally compact | paracompact |
|---|---|---|---|---|---|---|
| $\mathbb{R}$, $\mathbb{R}^n$, $\mathbb{C}^n$ | no | no | yes | yes | yes | yes |
| $[0,1]$, $S^n$, $T^n$, $\mathbb{RP}^n$ | yes | yes | yes | yes | yes | yes |
| the Cantor set, $\mathbb{Z}_p$ | yes | yes | yes | yes | yes | yes |
| $\mathbb{Q}$ | no | no | yes | yes | no | yes |
| $\mathbb{Z}$, $\mathbb{N}$ | no | no | yes | yes | yes | yes |
| the long line $L$ | no | yes | no | no | yes | no |
| $[0,\omega_1)$ | no | yes | no | no | yes | no |
| $[0,\omega_1]$ | yes | yes | yes | yes | yes | yes |
| $\beta\mathbb{N}$ | yes | yes | yes | yes | yes | yes |
| the Sorgenfrey line $\mathbb{R}_S$ | no | no | yes | no | no | yes |
| the Sorgenfrey plane $\mathbb{R}_S^2$ | no | — | no | no | no | no |
| the Niemytzki plane | no | — | no | no | no | no |
| a metric space | not always | not always | not always | not always | not always | yes |
| a compact Hausdorff space | yes | yes | yes | yes | yes | yes |

The three standard separations of the table are the long line, the Sorgenfrey line and the Sorgenfrey plane. The long line is countably compact and not compact, and it is locally metrisable and not paracompact: the cover by its initial segments has no locally finite refinement. The Sorgenfrey line is Lindelöf, hence paracompact and normal, and it is not $\sigma$-compact, not locally compact and not metrisable; it shows that Lindelöf and paracompact do not give a distance. The Sorgenfrey plane is the product of two paracompact spaces and is not paracompact, and it is not Lindelöf; it shows that paracompactness is not finitely productive.

## Warnings

Objects that a reader may expect to find among the spaces classified here, and does not.

| Object | Why it is not tabulated | Introduced in |
|---|---|---|
| the Zariski topology alone | a topology that is $T_0$ and not $T_1$; it is recorded through $\operatorname{Spec} R$ and the real Zariski topology, and it carries no metric | *Schemes*; *Real Algebraic Geometry* |
| pseudocompactness | the corpus does not introduce pseudocompact or limit-point compact spaces, and no entry relies on them | — |
| countable compactness of a general non-Hausdorff space | the corpus records countable compactness only where the paracompactness theory uses it, and not for the pathological spaces | *Paracompactness and Partitions of Unity* |
| the axiom $T_5$ | the corpus uses the separation hierarchy only up to $T_4$ and perfect normality | *Metrisation and Separation Axioms* |

## Summary

This article has listed the separation axioms $T_0$ to $T_4$, the complete regularity and perfect normality that sit beside them, and the compactness and countability conditions of the corpus, and has tabulated which spaces satisfy which. The implications run $T_4 \Rightarrow T_{3\frac12} \Rightarrow T_3 \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0$ with no arrow reversing, compactness implies countable compactness, the Lindelöf property and $\sigma$-compactness, and countable compactness together with the Lindelöf property gives compactness. Each non-implication is witnessed by a space of the corpus: the cofinite topology for $T_1$ without Hausdorff, Mysior's example for regularity without complete regularity, the Sorgenfrey plane and the Niemytzki plane for Tychonoff without normal, the indiscrete space for normal without $T_1$, and the long line and the Sorgenfrey line for the independence of compactness, paracompactness and metrisability. The tables introduce and prove nothing; they record the properties that the introducing articles establish.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $T_0$, $T_1$, $T_2$, $T_3$, $T_{3\frac12}$, $T_4$ | the separation axioms; $T_2$ is Hausdorff, $T_3$ regular, $T_{3\frac12}$ Tychonoff, $T_4$ normal, each with the $T_1$ clause |
| $T_3$, $T_{3\frac12}$ | the corpus's numbering, in which complete regularity is stronger than regularity |
| regular, completely regular, normal, paracompact | the conditions as in *Metrisation and Separation Axioms* and *Paracompactness and Partitions of Unity* |
| $\mathbb{R}_S$, $\mathbb{R}_S^2$ | the Sorgenfrey line and its square |
| $\beta\mathbb{N}$ | the Stone–Čech compactification of $\mathbb{N}$ |
| $L$, $[0,\omega_1)$, $[0,\omega_1]$ | the long line and the two ordinal spaces |
| $\operatorname{Spec} R$ | the prime spectrum with the Zariski topology |
| $[0,1]^{I}$ | a product of intervals, compact Hausdorff for every $I$ |
| $\sigma$-compact, Lindelöf | countable union of compact sets; every open cover has a countable subcover |

## Further Reading

- Ryszard Engelking, *General Topology* (Heldermann, rev. ed. 1989), for the separation axioms, the compactness conditions and the counterexamples in their standard form.
- Lynn A. Steen and J. Arthur Seebach, *Counterexamples in Topology* (Springer, 2nd ed. 1978), for the Sorgenfrey line and plane, the Niemytzki plane, Mysior's example, the long line and the ordinal spaces.
- K. P. Hart, Jun-iti Nagata and Jerry E. Vaughan (eds.), *Encyclopedia of General Topology* (Elsevier, 2004), for the charts of implications among the covering and separation properties.
- James R. Munkres, *Topology* (Pearson, 2nd ed. 2000), for the separation axioms, compactness and local compactness in their textbook order.
