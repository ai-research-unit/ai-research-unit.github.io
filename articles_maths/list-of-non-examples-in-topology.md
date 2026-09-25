
# __List of Non-Examples in Topology__

## Introduction

This article lists the standard counterexamples of the corpus, each with the topological property it breaks and the article that records the failure. Every entry points to the article that introduces the space, and the article introduces nothing and proves nothing.

The list gathers the spaces that are counterexamples to a natural implication: the topologist's sine curve, which is connected but not path connected; the Warsaw circle and the comb space, which are continua but not Peano continua; the pseudo-arc, which is arc-like and contains no arc; the long line, which is locally Euclidean and not metrisable; the Sorgenfrey line and plane and the Niemytzki plane, which show that separability, first countability and normality do not imply metrisability; and the Alexander horned sphere and the wild knot, which are embeddings that fail tameness. The spaces are grouped by the layer of the theory whose implication they break: connectedness, local connectedness, indecomposability, metrisability and countability, the separation axioms, compactness and category, and wildness.

The article records examples and non-examples side by side. The typical row names a space and the property it *fails*, so that the space can be read as the boundary of the implication it is usually taken to refute; where the corpus also states the positive property the space retains, both are named.

## Connectedness and Path Connectedness

The first group breaks the converse of the implication that a path connected space is connected.

| Space | The property it breaks | Introduced in |
|---|---|---|
| the topologist's sine curve | connected but not path connected: a path from the graph cannot reach the limiting segment | *Topological Spaces*, §Connectedness |
| the topologist's sine curve, as a continuum | connected and compact but not locally connected at the limiting segment | *Continuum Theory*, §Peano Continua |
| the rationals $\mathbb{Q}$ | not a Baire space: meagre in themselves | *Baire Spaces and Category*, §The Rationals and the Irrationals |
| the rationals $\mathbb{Q}$ | not completely metrisable, and not a $G_\delta$ in a complete space | *Baire Spaces and Category*, §The Rationals and the Irrationals |

The sine curve is the classical witness that connectedness is strictly weaker than path connectedness, and it is also the simplest continuum that is not a Peano continuum. The rationals show the same phenomenon in the category-theoretic direction: a space may be countable and dense and still fail the Baire property that every complete metric space has.

## Local Connectedness and Peano Continua

The second group breaks the converse of the Hahn–Mazurkiewicz theorem, which says that the Peano continua are exactly the continuous images of the interval.

| Space | The property it breaks | Introduced in |
|---|---|---|
| the Warsaw circle | a continuum that is not locally connected; it has the Čech cohomology of a circle but is not homotopy equivalent to one | *Continuum Theory*, §Peano Continua |
| the comb space | a continuum that is not locally connected; it is contractible, so it is not detected by homotopy | *Continuum Theory*, §Peano Continua |
| the bucket-handle continuum | indecomposable, hence not locally connected and not a Peano continuum | *Continuum Theory*, §The Standard Indecomposable Continua |
| the solenoid | an indecomposable continuum arising as an inverse limit of circles; not locally connected | *Continuum Theory*, §The Standard Indecomposable Continua |

The Warsaw circle and the comb space are the two standard continua that are not Peano continua, and both are planar; the solenoid is the inverse-limit example, the attractor of a dynamical system that is not a finite graph. Each shows that the continuous-image characterisation of the Peano continua cannot be weakened to compactness and connectedness alone.

## Indecomposable and Hereditarily Indecomposable Continua

The third group consists of the continua that are not the union of two proper subcontinua, where the intuition drawn from the interval fails.

| Space | The property it breaks | Introduced in |
|---|---|---|
| the pseudo-arc | a continuum that contains no arc, although it is arc-like | *Continuum Theory*, §Hereditarily Indecomposable Continua |
| the pseudo-arc | homogeneous, and homeomorphic to each of its nondegenerate subcontinua | *Continuum Theory*, §Hereditarily Indecomposable Continua |
| the bucket-handle continuum | its proper subcontinua have empty interior, and it is partitioned into pairwise disjoint dense composants | *Continuum Theory*, §Decompositions and Composants |
| the circle $S^1$ as a continuum | not unicoherent: it contains a simple closed curve, unlike the interval | *Continuum Theory*, §Unicoherent Continua |

The pseudo-arc is the extremal example: it is arc-like, homogeneous and hereditarily indecomposable, and yet it is not an arc and contains none, so that the inverse-limit construction and the local structure point in opposite directions. The bucket-handle continuum shows the same failure of intuition in the decomposable-looking picture: the composants are dense and disjoint, so no decomposition into simpler pieces exists.

## Metrisability, Countability and Paracompactness

The fourth group breaks the implications between the countability and metrisability properties, and shows that separable plus first countable plus perfectly normal does not suffice.

| Space | The property it breaks | Introduced in |
|---|---|---|
| the long line | locally metrisable but not metrisable, and not paracompact; it is countably compact and not compact | *Paracompactness and Partitions of Unity*, §The Smirnov Metrisation Theorem |
| the Sorgenfrey line $\mathbb{R}_S$ | separable, first countable and perfectly normal, but not second countable and not metrisable | *Metrisation and Separation Axioms*, §Comparing the Axioms: Counterexamples |
| the Sorgenfrey line $\mathbb{R}_S$ | Lindelöf and paracompact, but not locally metrisable | *Paracompactness and Partitions of Unity*, §The Smirnov Metrisation Theorem |
| the Sorgenfrey line $\mathbb{R}_S$ | a Moore space that is not metrisable, and not Čech-complete | *Baire Spaces and Category* |
| the Sorgenfrey plane $\mathbb{R}_S^2$ | the square of a paracompact space that is not paracompact, and a product of normal spaces that is not normal | *Metrisation and Separation Axioms*, §Comparing the Axioms: Counterexamples |
| the Niemytzki plane | a Moore space that is Tychonoff and not normal, and not metrisable | *Metrisation and Separation Axioms*, §Comparing the Axioms: Counterexamples |
| the one-point compactification of an uncountable discrete space | compact Hausdorff and not metrisable | *Metrisation and Separation Axioms* |
| the product $[0,1]^{I}$ for uncountable $I$ | compact Hausdorff and not first countable, hence not metrisable | *Metrisation and Separation Axioms* |

The long line is the standard proof that local metrisability is strictly weaker than metrisability, and the Sorgenfrey line is the standard proof that separability, first countability and perfect normality together do not give a metric. The Sorgenfrey plane and the Niemytzki plane show that normality is not preserved by products and is not implied by the Moore-space axioms, and the uncountable products show that compactness does not supply the countable base.

## Separation Axioms

The fifth group consists of the spaces on which one of the separation axioms fails, with the failure named.

| Space | The property it breaks | Introduced in |
|---|---|---|
| the trivial topology on two points | regular, completely regular and normal, but not $T_1$ | *Metrisation and Separation Axioms* |
| Mysior's example | a regular $T_1$ space that is not completely regular | *Metrisation and Separation Axioms* |
| the Sorgenfrey plane | Tychonoff and not normal | *Metrisation and Separation Axioms* |
| the Niemytzki plane | Tychonoff and not normal | *Metrisation and Separation Axioms* |
| the Zariski topology on a variety | not Hausdorff, and not metrisable | *Algebraic Geometry* |
| the cofinite topology on an infinite set | $T_1$ and not Hausdorff | *Topological Spaces*, §Separation Axioms |

The separation hierarchy does not reverse: the trivial topology has all the separation properties except $T_1$, Mysior's example separates a regular $T_1$ space from a completely regular one, and the Zariski topology is the geometric instance of a natural topology that is not Hausdorff and in which the closed sets carry the information.

## Compactness and Category

A compact space need not satisfy the countability or the category properties that the metric case suggests.

| Space | The property it breaks | Introduced in |
|---|---|---|
| the long line as an ordered set | countably compact but not compact, since the initial segments have no finite subcover | *Paracompactness and Partitions of Unity*, §The Smirnov Metrisation Theorem |
| the product $[0,1]^{I}$ for uncountable $I$ | compact Hausdorff but not normal | *Metrisation and Separation Axioms* |
| the rationals inside $\mathbb{R}$ | meagre but dense, so a dense subset of a Baire space need not be Baire | *Baire Spaces and Category* |
| a discrete space in its own topology | locally compact and metrisable but not compact when infinite | *Topological Spaces*, §Compactness |

The long line is countably compact and not compact, the uncountable Tychonoff cube is compact and not normal, and the rationals show the asymmetry of the Baire property under the passage to a dense subspace. These are the failures of compactness to imply the further properties that hold in the compact metric case.

## Wild Embeddings

The last group consists of the embedded objects whose embedding is not tame, so that the intrinsic homeomorphism type does not determine their position.

| Space | The property it breaks | Introduced in |
|---|---|---|
| the Alexander horned sphere | a topological 2-sphere in $\mathbb{R}^3$ whose complement is not simply connected: a wild embedding | *Wild and Exotic Manifolds* (planned) |
| a wild knot | a knot in $S^3$ that is not isotopic to a polygonal one, and is excluded from the theory | *Knot Theory* |

The horned sphere is the standard wild embedding of a sphere, and its complement has a non-trivial fundamental group in contrast to the tame case; the wild knot is the corresponding one-dimensional phenomenon, excluded from the theory of the tame knots.

## Summary

This article has listed the standard counterexamples of the corpus, each with the property it breaks. The topologist's sine curve is connected and not path connected; the Warsaw circle and the comb space are continua and not Peano continua; the pseudo-arc is arc-like and contains no arc; the long line is locally metrisable and not metrisable; the Sorgenfrey line and plane and the Niemytzki plane show that separability, first countability and normality do not give a metric; the trivial topology and Mysior's example break the separation hierarchy; and the Alexander horned sphere and the wild knot are wild embeddings. The spaces are grouped by the layer whose implication they refute, and the positive property each retains is named beside the failure.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\mathbb{R}_S$, $\mathbb{R}_S^2$ | Sorgenfrey line and Sorgenfrey plane |
| $[0,1]^{I}$ | Tychonoff cube over an index set $I$ |
| $T_0$, $T_1$, $T_2$, $T_3$, $T_{3\frac12}$, $T_4$ | Separation axioms: $T_0$, $T_1$, Hausdorff, regular, completely regular, normal |
| $S^1$, $\mathbb{R}^3$, $S^3$ | Circle, space, sphere of the wild embeddings |
| $L$ | Long line, ordered set $\omega_1\times[0,1)$ |
| $\mathbb{Q}$, $\mathbb{R}$ | The standard number systems of the corpus |

## Further Reading

- Lynn A. Steen and J. Arthur Seebach, *Counterexamples in Topology* (Springer, 2nd ed. 1978), for the standard list of the counterexamples and the properties they break.
- Ryszard Engelking, *General Topology* (Heldermann, 2nd ed. 1989), for the separation, metrisation and paracompactness theorems and their sharpness.
- Sam B. Nadler, *Continuum Theory: An Introduction* (Marcel Dekker, 1992), for the sine curve, the Warsaw circle, the comb space and the pseudo-arc.
- R. H. Bing, "Concerning Hereditarily Indecomposable Continua", *Transactions of the American Mathematical Society* 71 (1951), for the pseudo-arc and its uniqueness.
