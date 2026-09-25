
# __List of Metric and Uniform Spaces__

## Introduction

This article lists the distances and the uniformities of Parts I to III, with the completion that each admits and with the metrisation theorem that decides which topological spaces receive a distance. The metric side is the geometric side: a distance gives balls, diameter, Lipschitz maps, geodesics and the Hausdorff and Gromov–Hausdorff distances between spaces. The uniform side is the topological side: a uniformity is the family of entourages "closer than $\epsilon$", and it is the structure that survives a homeomorphism, the structure carried by every topological group, and the structure whose completion exists in full generality. The entry bridges the two, since every metric space carries a uniformity and the passage from the uniformity to the topology loses exactly the uniform data that the completion uses.

Every entry points to the article that introduces the distance, the uniformity or the theorem. The article introduces nothing and proves nothing: it records the completion and the metrisation statement that the introducing article establishes, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the distances that are complete it lists the metrics that are not — the usual metric on $(0,1)$ and on $\mathbb{Q}$, whose completions are $[0,1]$ and $\mathbb{R}$; beside the spaces that are metrisable it lists the Sorgenfrey line, which is perfectly normal, separable, Lindelöf and paracompact and admits no distance; and beside the uniformities with a countable base it lists the unique uniformity of $\beta\mathbb{N}$, which has none — each with the failure named and the article that records it.

## The Distances of the Corpus

The distances are grouped by the structure that supplies them: the order or absolute value of a field, the inner product or metric of a linear space, the metric of a manifold, and the graph or distance structure of a discrete object.

| Metric space | The distance it carries | Completion | Introduced in |
|---|---|---|---|
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{R}^n$ | $d(x,y) = \lvert x - y\rvert$, the Euclidean distance | already complete | *Metric, Uniform and Complete Spaces*; *Euclidean Geometry* |
| $\mathbb{Q}$ | the restriction of the usual distance | $\mathbb{R}$, and no other for the usual absolute value | *Metric, Uniform and Complete Spaces*; *Absolute Values, Valuations and Completions* |
| $[0,1]$, $(0,1)$ | the restriction of the usual distance | $[0,1]$ for both; $(0,1)$ is not complete | *Metric, Uniform and Complete Spaces* |
| $\mathbb{Q}_p$ | the ultrametric $d(x,y) = \lvert x - y\rvert_p$ | already complete; the completion of $\mathbb{Q}$ for the $p$-adic absolute value | *The $p$-adic Numbers*; *Absolute Values, Valuations and Completions* |
| $\mathbb{Z}_p$ | the restriction of the $p$-adic distance | compact, hence complete; its completion is itself | *The $p$-adic Numbers* |
| $S^n$ | the chordal and the geodesic (round) distances, which induce the same topology | compact, hence complete | *Spherical Geometry* |
| $\mathbf{H}^n$ | the hyperbolic distance $d_{\mathbf{H}}$ | complete, and the completion adds no point | *Hyperbolic Geometry* |
| a Riemannian manifold $(M,g)$ | the Riemannian distance, the infimum of the lengths of the curves | complete if and only if $(M,g)$ is geodesically complete (Hopf–Rinow) | *Riemannian Geometry*; *Curvature and Geodesics* |
| $\mathbb{CP}^n$ | the Fubini–Study metric | compact, hence complete | *Kähler Geometry* |
| $C([0,1])$, $B(X,Y)$ | the sup metric $d_\infty(f,g) = \sup_x d(f(x),g(x))$ | complete when the target is complete | *Metric, Uniform and Complete Spaces* |
| a normed space, a Banach space | $d(x,y) = \lVert x - y\rVert$ | the completion is the Banach space completion, built as classes of Cauchy sequences | *Banach and Hilbert Spaces*; *Normed and Banach Spaces* |
| a Hilbert space | the distance of the inner product | complete by definition, and every inner product space embeds in its completion | *Banach and Hilbert Spaces* |
| a finitely generated group $G$ | the word metric $d_S(g,h) = \lvert g^{-1}h\rvert_S$ of a Cayley graph | the completion is the group; the metric depends on $S$ only up to quasi-isometry | *Geometric Group Theory* |
| a real tree, a $0$-hyperbolic length space | the intrinsic distance, with the four-point condition | complete when the tree is | *Metric Geometry* |
| $\mathcal{K}(Z)$, the compact subsets of a metric space | the Hausdorff distance $d_H$ | complete when $Z$ is complete | *Gromov–Hausdorff Convergence*; *Metric Geometry* |
| the isometry classes of compact metric spaces | the Gromov–Hausdorff distance $d_{GH}$ | the class is not complete; the limits include singular spaces | *Gromov–Hausdorff Convergence* |
| a metric space with the discrete metric | $d(x,y) = 1$ for $x \neq y$ | complete; it induces the discrete topology | *Metric, Uniform and Complete Spaces* |
| a compact Hausdorff space | any metric inducing its topology, and the unique uniformity | complete for that unique uniformity, and complete in every metric | *Metric, Uniform and Complete Spaces* |

The order of the rows is the order in which the corpus builds the distances: the order and absolute value distances of the real and $p$-adic lines, then the distances of normed and inner-product spaces, then the geometric distances of manifolds, then the coarse distances of graphs and the distances between spaces themselves. The **intrinsic metric** of a length space is the supremum of the lengths of the curves, and a length space is one in which the intrinsic metric recovers $d$; the metric geometry of these distinctions is *Metric Geometry*.

## The Completion of a Metric Space

Every metric space $(X,d)$ embeds isometrically as a dense subspace of a complete metric space $(\hat X,\hat d)$, unique up to isometry fixing $X$; the construction is by equivalence classes of Cauchy sequences, and it is the same construction that produces $\mathbb{R}$ from $\mathbb{Q}$ and $\mathbb{Q}_p$ from $\mathbb{Q}$ with the $p$-adic distance.

| Completion | The space completed, and the result | Introduced in |
|---|---|---|
| $\mathbb{R}$ | the completion of $\mathbb{Q}$ for the usual absolute value | *The Real Numbers*; *Absolute Values, Valuations and Completions* |
| $\mathbb{Q}_p$, $\mathbb{Z}_p$ | the completions of $\mathbb{Q}$ and $\mathbb{Z}$ for the $p$-adic absolute value; $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$ | *The $p$-adic Numbers*; *Topological Rings and Fields* |
| $\mathbb{C}_p$ | the completion of the algebraic closure of $\mathbb{Q}_p$; it is not complete, and its own completion is needed for the analytic theory | *Absolute Values, Valuations and Completions* |
| $k[[t]]$, $k((t))$ | the $(t)$-adic completions of $k[t]$ and $k(t)$, the second being the fraction field of the first | *Topological Rings and Fields*; *Formal Power Series and Completion* |
| $\hat X$ | the completion of a metric space, unique up to an isometry fixing $X$ | *Metric, Uniform and Complete Spaces* |
| the Banach space completion | the completion of a normed space, a Banach space | *Normed and Banach Spaces* |
| the Hilbert space completion | the completion of an inner product space, a Hilbert space | *Banach and Hilbert Spaces* |
| the $I$-adic completion $\hat R$ | the completion of a ring for the $I$-adic topology, an inverse limit of quotients | *Topological Rings and Fields* |

Completeness is not a topological property, and the standard witness is the interval: $(0,1)$ and $\mathbb{R}$ are homeomorphic, the first is not complete for its usual metric and the second is. A metrisable space admits a complete metric exactly when it is completely metrisable, that is, a $G_\delta$ in its completion, and this is the topological form of the property that the completion detects. The completion is idempotent, and it is an isometry-invariant functor on the category of metric spaces with uniformly continuous maps.

## The Uniform Structures of the Corpus

A uniform structure on a set is a filter of entourages on $X \times X$ containing the diagonal, closed under inversion and under composition; it generates a topology, and it remembers exactly the data that the Cauchy condition and uniform continuity need.

| Uniform space | The uniformity it carries | Its completion | Introduced in |
|---|---|---|---|
| a metric space | the metric uniformity, with entourages $\{(x,y) : d(x,y) < \epsilon\}$ | the metric completion $\hat X$ | *Metric, Uniform and Complete Spaces* |
| a topological group $G$ | the left, the right and the two-sided uniformities, generated by the neighbourhoods of the identity | the completion of the group, a topological group when $G$ is Hausdorff | *Topological Groups*; *Abelian Topological Groups* |
| a compact Hausdorff space | a unique uniformity, compatible with the topology | already complete; the completion adds no point | *Metric, Uniform and Complete Spaces* |
| a metrisable uniform space | a uniformity with a countable base, equivalently generated by countably many pseudometrics | the metric completion for any metric of a countable base | *Metric, Uniform and Complete Spaces* |
| a topological vector space | the uniformity generated by the neighbourhoods of $0$, additive and linear | the completion, a topological vector space | *Topological Modules and Vector Spaces*; *Locally Convex Spaces* |
| a proximity space $(X,\delta)$ | the proximal uniformity, whose entourages are the sets far from the diagonal | the Samuel compactification, whose points are the minimal Cauchy filters | *Proximity Spaces* |
| a uniform space in general | a filter of entourages, with no metric assumed | the separated completion, built from minimal Cauchy filters | *Metric, Uniform and Complete Spaces* |
| an inverse system of groups | the inverse-limit uniformity, with the subgroups of the system as a base at the identity | the profinite completion $\hat G^{\mathrm{pf}}$, compact and totally disconnected | *Profinite Groups and the Krull Topology* |

The completion of a uniform space always exists, is unique up to a uniform isomorphism fixing $X$, and is the separated completion when the original space is not Hausdorff; the passage to the completion is a functor on the category of uniform spaces and uniformly continuous maps. The uniformity is finer information than the topology and coarser than the metric: a topological space that carries a uniformity at all is completely regular, and the proximities of *Proximity Spaces* sit between the two, since every uniformity induces a proximity and every proximity induces a topology.

## The Metrisation Theorems

The metrisation theorems decide which topological and which uniform spaces receive a distance. They are stated here together because they are the reason the two sides of this list meet.

| Theorem | The statement | Introduced in |
|---|---|---|
| Urysohn's metrisation theorem | a regular second-countable $T_1$ space is metrisable; the proof embeds it in the Hilbert cube | *Metrisation and Separation Axioms* |
| Nagata–Smirnov theorem | a regular space with a $\sigma$-locally finite base is metrisable, and the condition is necessary as well as sufficient | *Metrisation and Separation Axioms* |
| Bing's metrisation theorem | a regular space with a $\sigma$-discrete base is metrisable | *Metrisation and Separation Axioms* |
| Smirnov's metrisation theorem | a paracompact and locally metrisable space is metrisable | *Paracompactness and Partitions of Unity* |
| Stone's theorem | every metrisable space is paracompact | *Paracompactness and Partitions of Unity* |
| the uniform metrisation theorem | a uniform space is metrisable exactly when its uniformity has a countable base, equivalently is generated by countably many pseudometrics | *Metric, Uniform and Complete Spaces* |
| the group metrisation theorem | a Hausdorff topological group is metrisable exactly when it is first countable, and then a left-invariant metric may be chosen | *Topological Groups* |
| the metric characterisation of compactness | a metrisable space is compact exactly when it is complete and totally bounded, equivalently sequentially compact | *Metric, Uniform and Complete Spaces*; *Topological Spaces* |

## The Spaces That Fail Metrisability or Completeness

The non-examples are recorded with the property that fails, since their role is to show that neither a separation axiom nor a covering property supplies a distance, and that completeness is not a topological invariant.

| Space | The property it has, and the one it fails | Introduced in |
|---|---|---|
| $(0,1)$ | metrisable and connected, homeomorphic to $\mathbb{R}$; not complete for its usual metric, so completeness is not topological | *Metric, Uniform and Complete Spaces* |
| $\mathbb{Q}$ | countable, metrisable and $\sigma$-compact; not complete, and not completely metrisable, since it is meagre in itself | *Metric, Uniform and Complete Spaces*; *Baire Spaces and Category* |
| the map $x \mapsto 1/x$ on $(0,1)$ | a homeomorphism onto $(1,\infty)$ that is not uniformly continuous; the uniformity is not a topological invariant | *Metric, Uniform and Complete Spaces* |
| the Sorgenfrey line $\mathbb{R}_S$ | perfectly normal, separable, Lindelöf and paracompact; not metrisable, and not locally metrisable | *Metrisation and Separation Axioms*; *Paracompactness and Partitions of Unity* |
| the long line $L$ | locally metrisable, connected, normal; not metrisable and not paracompact | *Paracompactness and Partitions of Unity* |
| $\beta\mathbb{N}$ | compact Hausdorff, with its unique uniformity; not metrisable, so its uniformity has no countable base | *Metrisation and Separation Axioms* |
| an uncountable discrete space | carries the fine uniformity; not metrisable, and the discrete metric is not equivalent to it with respect to the topology alone | *Metric, Uniform and Complete Spaces* |
| $\mathbb{Q}$ with the $p$-adic distance | a metric space that is not complete and whose completion is $\mathbb{Q}_p$; unlike the usual completion, it is totally disconnected | *The $p$-adic Numbers*; *Absolute Values, Valuations and Completions* |

## Warnings

Objects that a reader may expect to find among the metric and uniform spaces, and does not.

| Object | Why it is not listed | Introduced in |
|---|---|---|
| the fine uniformity on an uncountable set | a uniformity with no countable base, hence not metrisable; it is a uniformity and not a distance, and it is recorded only through the discrete space | *Metric, Uniform and Complete Spaces* |
| the asymptotic cone of a metric space | a construction that requires the limits of Part III, and not a metric space of this Part | *Geometric Group Theory* |
| the measured Gromov–Hausdorff distance | a construction that remembers a measure on each space and belongs to Part III | *Gromov–Hausdorff Convergence* |
| the Lipschitz distance | a distance between metric spaces coarser than the Gromov–Hausdorff distance and recorded with the Lipschitz maps, not as a metric structure of the corpus | *Gromov–Hausdorff Convergence* |
| a norm on a vector space over a non-Archimedean field | the non-Archimedean norms and their unit balls, which belong to the non-Archimedean analysis and are not distances of this list | *Non-Archimedean Functional Analysis* |

## Summary

This article has listed the distances of the corpus with their completions — the Euclidean, $p$-adic, hyperbolic, Riemannian, word and Gromov–Hausdorff distances among them — and the uniformities of the corpus with their completions — the metric uniformity, the uniformities of a topological group, the unique uniformity of a compact Hausdorff space, the proximal uniformity and the inverse-limit uniformity. The completion of a metric space and of a uniform space is unique up to an isomorphism fixing the space, and it produces $\mathbb{R}$ from $\mathbb{Q}$, $\mathbb{Q}_p$ from $\mathbb{Q}$ and the profinite completion from a group. The metrisation theorems — Urysohn, Nagata–Smirnov, Bing, Smirnov, the countable-base theorem for uniformities and the first-countability theorem for groups — decide which spaces receive a distance. Beside the examples stand the non-examples: the incomplete interval, the rationals, the Sorgenfrey line and the long line, each with the failure named. The list introduces and proves nothing; it is the index of the distance structures of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $d(x,y)$, $d_\infty$ | a distance; the sup metric on bounded functions |
| $B(x,r)$, $\overline B(x,r)$ | open and closed balls |
| $\lvert x\rvert_p$, $\lvert x\rvert$ | the $p$-adic and the usual absolute values |
| $d_H$, $d_{GH}$ | the Hausdorff and Gromov–Hausdorff distances |
| $\hat X$, $\hat d$, $\iota$ | the completion of a metric space and its isometric embedding |
| $\mathcal{U}$, $E$, $E[x]$ | a uniform structure, an entourage, and the points $E$-close to $x$ |
| $\Delta_X$ | the diagonal of $X \times X$ |
| $G/H$ | a homogeneous space, with the uniformity induced from $G$ |
| $\hat G^{\mathrm{pf}}$ | the profinite completion |
| $\mathbb{R}_S$ | the Sorgenfrey line |
| $\mathcal{K}(Z)$ | the hyperspace of nonempty compact subsets with the Hausdorff metric |
| $\lvert g\rvert_S$, $d_S$ | word length and word metric of a finitely generated group |
| $M^2_k$, CAT($k$) | the model surface and the triangle comparison condition of metric geometry |

## Further Reading

- Nicolas Bourbaki, *General Topology*, Chapters I–IV (Springer, 1989), for the uniform structures, the entourages and the completion of a uniform space in their standard form.
- John R. Isbell, *Uniform Spaces* (American Mathematical Society, 1964), for the uniform spaces, the proximities and the Samuel compactification.
- Dmitri Burago, Yuri Burago and Sergei Ivanov, *A Course in Metric Geometry* (American Mathematical Society, 2001), for the distances, the length spaces and the Gromov–Hausdorff convergence.
- Ryszard Engelking, *General Topology* (Heldermann, rev. ed. 1989), for the metrisation theorems and the uniform spaces, including the uniform metrisation theorem.
