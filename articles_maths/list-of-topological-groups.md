
# __List of Topological Groups__

## Introduction

This article lists the topological groups of Parts I to III, grouped by the topology they carry and by the class the corpus attaches to them: the general topological groups, whose topology is determined at the identity; the locally compact groups, on which the Haar measure exists; the profinite groups, which are compact and totally disconnected; and the $p$-adic and adelic groups, which carry the topology of a valued field or of a restricted product. A Lie group is a topological group as well, and the Lie groups are indexed separately in *List of Lie Groups*; the entry here records the topological structure that the group theory uses.

Every entry points to the article that introduces the group. The article introduces nothing and proves nothing: it records the topology that the introducing article gives each group, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the groups that are locally compact it lists the topological groups that are not — the additive group of an infinite-dimensional Banach space, the loop group, the diffeomorphism group; beside the groups that are Hausdorff it lists the quotients by a non-closed subgroup; beside the groups that are unimodular it lists the affine group, whose left and right Haar measures differ — each with the failure named and the article that records it.

## The General Topological Groups

A topological group is a group $G$ with a topology for which the multiplication and the inversion are continuous. The topology is then determined by a neighbourhood base at the identity, the group is homogeneous, and there are two natural uniformities, the left and the right.

| Group | The topology it carries | Completion and uniformity | Introduced in |
|---|---|---|---|
| a topological group $G$ | the topology determined by a neighbourhood base at $e$; $L_g$ and $R_g$ are homeomorphisms | the left $\mathcal{U}_L$ and right $\mathcal{U}_R$ uniformities; completion $\hat G$ in the two-sided (Raĭkov) uniformity | *Topological Groups* |
| a discrete group | the discrete topology; every map is continuous | complete; a subgroup is open if and only if it is closed | *Groups*; *Topological Groups* |
| $\mathbb{R}^n$, $\mathbb{C}^n$ | the Euclidean topology under addition; locally compact, connected | complete; the uniformity is the additive one | *Topological Groups*; *Euclidean Geometry* |
| $S^1 = \mathbb{R}/\mathbb{Z}$, $T^n$ | the quotient topology of $\mathbb{R}$ and $\mathbb{R}^n$; compact, connected | complete; the unique compact-group uniformity | *Topological Groups*; *Pontryagin Duality* |
| $\mathbb{R}^\times$, $\mathbb{C}^\times$ | the subspace topology of the field; not connected ($\mathbb{R}^\times$ has two components) | complete for the multiplicative metric; Haar measure $dx/\lvert x\rvert$ | *Locally Compact Groups and Haar Measure* |
| $\mathbb{Q}$ | the subspace topology of $\mathbb{R}$; the $p$-adic topology is a different refinement | neither topology is complete; completions $\mathbb{R}$ and $\mathbb{Q}_p$ | *Topological Groups*; *Absolute Values, Valuations and Completions* |
| $GL_n(\mathbb{R})$, $GL_n(\mathbb{C})$ | the subspace topology of matrices; locally compact | complete metrisable; two components for $\mathbb{R}$, connected for $\mathbb{C}$ | *The General Linear Group*; *Lie Groups* |
| $\operatorname{Sym}(X)$ | the pointwise-convergence topology on $X^X$; a topological group, not locally compact for infinite $X$ | not complete for infinite $X$; the completion is strictly larger than $\operatorname{Sym}(X)$ | *Group Actions and Structure*; *Topological Groups* |
| $\operatorname{Homeo}(X)$ | the compact-open topology; a topological group when $X$ is compact | not locally compact for a manifold of positive dimension | *Group Actions and Structure* |
| a quotient $G/H$ | the quotient topology; a topological group when $H$ is normal | Hausdorff exactly when $H$ is closed | *Topological Groups* |
| the identity component $G_0$ | the connected component of $e$, closed and normal, and the intersection of the open subgroups | $G/G_0$ is totally disconnected | *Topological Groups* |
| $\operatorname{GL}_n(\mathbb{Q}_p)$ | the $p$-adic manifold topology; locally compact, totally disconnected | complete; the congruence subgroups form a neighbourhood base | *$p$-adic Lie Groups*; *Adeles and Ideles* |

## The Locally Compact Groups

A locally compact group is a Hausdorff topological group in which every point has a compact neighbourhood. It is exactly the class on which the Haar measure exists, and it contains the discrete groups, the compact groups, the Lie groups and the additive groups of the local fields.

| Group | The topology and the invariant measure | Unimodular? | Introduced in |
|---|---|---|---|
| a locally compact group $G$ | Hausdorff, locally compact; a left Haar measure $\mu$, unique up to a positive scalar | $\Delta \equiv 1$ for the abelian, compact, discrete, nilpotent and semisimple groups, classes that overlap and none of which contains the others | *Locally Compact Groups and Haar Measure* |
| a discrete group | the discrete topology; counting measure | yes, trivially | *Locally Compact Groups and Haar Measure* |
| a compact group $K$ | compact Hausdorff; the Haar measure normalised to a probability | yes | *Analysis on Compact Groups* |
| $\mathbb{R}^n$ | the Euclidean topology; Lebesgue measure | yes | *Locally Compact Groups and Haar Measure* |
| $\mathbb{Q}_p^n$, $\mathbb{Z}_p^n$ | the $p$-adic topology; Haar measure normalised by $\mu(\mathbb{Z}_p) = 1$ | yes, the group is abelian | *The $p$-adic Numbers* |
| $GL_n(\mathbb{R})$, $SL_n(\mathbb{R})$, $O(n)$, $U(n)$ | the matrix topology; $GL_n$ with the measure $\lvert\det A\rvert^{-n}dA$ | yes for all of them | *Locally Compact Groups and Haar Measure*; *The General Linear Group* |
| the affine group $\mathbb{R} \rtimes \mathbb{R}_{>0}$ | the topology of $\mathbb{R}^2$; left Haar measure $a^{-2}da\,db$ and right Haar measure $a^{-1}da\,db$ | **no**; $\Delta(a,b) = a^{-1}$ | *Locally Compact Groups and Haar Measure*; *Affine Spaces and Translations* |
| the Heisenberg group | the topology of $\mathbb{R}^3$; Lebesgue measure | yes | *Lie Groups*; *Locally Compact Groups and Haar Measure* |
| the adeles $\mathbb{A}_K$, the ideles $\mathbb{I}_K$ | the restricted-product topology; locally compact and totally disconnected away from the archimedean places | yes, the groups are abelian | *Adeles and Ideles* |
| a lattice $\Gamma \subseteq G$ | the discrete topology, with $G/\Gamma$ of finite invariant volume | inherits unimodularity from $G$ when $G$ is unimodular | *Lattices in Lie Groups* |

The structure theory of the locally compact abelian groups belongs here: an open subgroup is of the form $\mathbb{R}^n \times K$ with $K$ compact, and a compactly generated locally compact abelian group is $\mathbb{R}^n \times \mathbb{Z}^m \times K$ with $K$ compact. This is the input to Pontryagin duality, which exchanges compactness with discreteness and identifies the category with its own opposite.

## The Profinite and Pro-$p$ Groups

A profinite group is the inverse limit of an inverse system of finite groups with the discrete topology; equivalently it is a compact Hausdorff totally disconnected topological group. The topology is generated by the open normal subgroups, which are exactly the finite-index subgroups that are open.

| Group | The topology it carries | Its role | Introduced in |
|---|---|---|---|
| $\varprojlim_i G_i$ | the inverse-limit topology, with the subgroups $\ker(G \to G_i)$ as a base at $e$; compact totally disconnected | the definition of a profinite group | *Profinite Groups and the Krull Topology* |
| $\mathbb{Z}_p = \varprojlim_n \mathbb{Z}/p^n$ | the $p$-adic topology; compact, totally disconnected, metrisable | the additive group of the $p$-adic integers | *The $p$-adic Numbers*; *Profinite Groups and the Krull Topology* |
| $\hat{\mathbb{Z}} = \varprojlim_n \mathbb{Z}/n\mathbb{Z}$ | the inverse-limit topology; $\hat{\mathbb{Z}} \cong \prod_p \mathbb{Z}_p$ | the profinite completion of $\mathbb{Z}$ | *Profinite Groups and the Krull Topology* |
| $\operatorname{Gal}(L/K)$ | the Krull topology, with the subgroups $\operatorname{Gal}(L/M)$ for $M/K$ finite Galois as a base | the Galois correspondence holds for the closed subgroups | *Galois Theory*; *Profinite Groups and the Krull Topology* |
| $\operatorname{Gal}(\overline{\mathbb{F}}_p/\mathbb{F}_p)$ | the Krull topology; $\hat{\mathbb{Z}}$, with the Frobenius as topological generator | the absolute Galois group of a finite field | *Galois Theory*; *Galois Cohomology* |
| the profinite completion $\hat G^{\mathrm{pf}}$ | the inverse limit over the finite-index normal subgroups; $G$ embeds exactly when $G$ is residually finite | the profinite completion of an abstract group | *Profinite Groups and the Krull Topology* |
| a pro-$p$ group | the inverse limit of finite $p$-groups; compact, totally disconnected | the Sylow $p$-subgroups of a profinite group | *Profinite Groups and the Krull Topology*; *Combinatorial Group Theory* |
| a compact $p$-adic analytic group | the $p$-adic manifold topology; contains a uniformly powerful open pro-$p$ subgroup | the $p$-adic Lie groups of the next table | *$p$-adic Lie Groups* |
| the Galois group of a local field | the Krull topology; a Demushkin pro-$p$ group of finite rank, hence $p$-adic analytic | the input to local class field theory | *Galois Cohomology*; *$p$-adic Lie Groups* |

A profinite group is metrisable exactly when its inverse system has a countable cofinal subsystem, equivalently when there are countably many open normal subgroups; the Krull topology of a Galois group is metrisable exactly when the field has countably many finite Galois subextensions, and it is not induced by any distance otherwise. The abelian profinite groups are the Pontryagin duals of the discrete torsion groups, by *Pontryagin Duality*, and this is how their structure is read off.

## The $p$-adic and Adelic Groups

The $p$-adic Lie groups carry the manifold topology of a non-archimedean field, and the adelic groups carry the restricted-product topology; both are totally disconnected away from finitely many places, and both are the topological home of the arithmetic of a global field.

| Group | The topology it carries | Introduced in |
|---|---|---|
| $\mathbb{Q}_p$, $\mathbb{Q}_p^n$ | the $p$-adic topology; locally compact, complete, totally disconnected | *The $p$-adic Numbers* |
| a $p$-adic Lie group $G$ | an analytic manifold over $\mathbb{Q}_p$; the connected components are points and the compact open subgroups form a base | *$p$-adic Lie Groups* |
| $GL_n(\mathbb{Z}_p)$, $SL_n(\mathbb{Z}_p)$ | the subspace topology of $M_n(\mathbb{Z}_p)$; compact and totally disconnected | *$p$-adic Lie Groups*; *The General Linear Group* |
| the congruence subgroups $\Gamma_k = 1 + p^kM_n(\mathbb{Z}_p)$ | a basis of open neighbourhoods of the identity; each is a normal pro-$p$ subgroup | *$p$-adic Lie Groups* |
| the adeles $\mathbb{A}_K$ | the restricted product of the completions $K_v$ with respect to the valuation rings $\mathcal{O}_v$; locally compact, with the adelic topology | *Adeles and Ideles* |
| the ideles $\mathbb{I}_K = \mathbb{A}_K^\times$ | the topology of the adele ring restricted to the units, which is **not** the subspace topology | *Adeles and Ideles* |
| the adelic group $G(\mathbb{A}_K)$ | the restricted product of the groups $G(K_v)$ over the places, locally compact | *Adeles and Ideles* |
| $K \subseteq \mathbb{A}_K$, discrete | the image of $K$ is discrete and cocompact in the trace-zero part | *Adeles and Ideles* |
| the loop group $LG = C^\infty(S^1,G)$ | the Fréchet manifold topology; not locally compact | *Loop Groups* |
| a maximal Kac–Moody group | the topology of Tits, Moody and Teo, in which the root groups are topological groups; in the affine case the locally compact group of the loop or $p$-adic description | *Kac–Moody Groups* |

## The Compact and Connected Groups, and the Failure of Both

The compactness and the connectedness of a topological group are properties of the group, and the corpus records the groups that have them and those that do not.

| Group | The property it has, and the one it fails | Introduced in |
|---|---|---|
| the Sorgenfrey line as an additive group | the half-open interval topology makes $\mathbb{R}$ a group with a topology, and addition is **not** continuous; hence it is not a topological group | *Metrisation and Separation Axioms*; *Topological Groups* |
| a group with the indiscrete topology | a topological group that is not $T_0$ and not Hausdorff; the quotient $G/H$ is Hausdorff exactly when $H$ is closed | *Topological Groups* |
| $\mathbb{R}^n$ | connected, locally compact, $\sigma$-compact; not compact | *Topological Groups* |
| $GL_n(\mathbb{R})$ | locally compact, two components; not compact and not connected | *The General Linear Group* |
| $GL_n(\mathbb{Q}_p)$ | locally compact, totally disconnected; not compact, not connected in the archimedean sense | *$p$-adic Lie Groups* |
| the loop group $LG$ | a topological group and a Fréchet manifold; not locally compact | *Loop Groups* |
| the diffeomorphism group $\operatorname{Diff}(M)$ | a topological group and a Fréchet manifold; not locally compact | *Diffeomorphism Groups* |
| the affine group | locally compact; **not** unimodular, so the left and right Haar measures differ | *Locally Compact Groups and Haar Measure* |
| an uncountable product $\prod_{i \in I} \mathbb{Z}/2$ | compact totally disconnected, hence profinite; not metrisable and not second countable | *Profinite Groups and the Krull Topology* |
| a locally compact quantum group | an operator-algebraic object with a comultiplication and a Haar weight; not a topological group with a point set | *Locally Compact Quantum Groups* |

## Warnings

Objects that a reader may expect to find in a list of topological groups, and does not.

| Object | Why it is not listed as a topological group of this article | Introduced in |
|---|---|---|
| the orthogonal group $O(n)$ and the other classical groups | compact Lie groups, hence topological groups, indexed with their Lie structure in *List of Lie Groups* and with their forms in *List of Classical Geometric Groups* | *Lie Groups*; *Isometries and Orthogonal Transformations* |
| the affine group $\operatorname{Aff}(n)$ | a locally compact non-unimodular group, indexed with the affine geometry in *List of Affine and Euclidean Groups* | *Affine Spaces and Translations* |
| the quantum groups of Part I | Hopf algebras and their deformations, without a topology on a point set | *Quantum Groups*; *Hopf Algebras* |
| the Weil group $W_K$ | a topological group that is not profinite, treated with the Galois cohomology of the local fields | *Galois Cohomology* |
| the group of adelic points of a non-abelian group | a restricted product of locally compact groups, recorded with the arithmetic and not in the structure table | *Adeles and Ideles* |

## Summary

This article has listed the topological groups of the corpus: the general topological groups, whose topology is determined at the identity and which carry the left and right uniformities; the locally compact groups, with the Haar measure, the modular function and the structure theorem for the abelian case; the profinite and pro-$p$ groups, with the inverse-limit topology and the Krull topology of the Galois groups; and the $p$-adic and adelic groups, with the manifold topology of a non-archimedean field and the restricted-product topology of the places. The non-examples stand beside them: the Sorgenfrey line, whose half-open topology does not make addition continuous; the quotients by a non-closed subgroup, which fail to be Hausdorff; the affine group, which is not unimodular; the loop group and the diffeomorphism group, which are not locally compact; and the uncountable products, which are profinite and not metrisable. The list introduces and proves nothing; it is the index of the topological groups of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $G$, $H$, $e$ | a topological group, a subgroup, the identity |
| $L_g$, $R_g$, $\operatorname{Ad}_g$ | left and right translations and the inner automorphism |
| $\mathcal{N}$, $\mathcal{U}_L$, $\mathcal{U}_R$ | a neighbourhood base at $e$; the left and right uniformities |
| $\hat G$, $\hat G^{\mathrm{pf}}$ | the completion in the two-sided uniformity; the profinite completion |
| $G_0$, $G/H$ | the identity component; a coset space with the quotient topology |
| $\mu$, $\Delta$, $\mu_R$ | a left Haar measure; the modular function; the right Haar measure $\Delta^{-1}\mu$ |
| unimodular | $\Delta \equiv 1$ |
| $S^1 = \mathbb{R}/\mathbb{Z}$, $T^n$ | the circle group and the $n$-torus |
| $G^\vee$ | the Pontryagin dual, not to be confused with the completion $\hat G$ |
| $\mathbb{Z}_p$, $\hat{\mathbb{Z}}$, $\mathbb{Q}_p$ | the $p$-adic integers, the profinite completion of $\mathbb{Z}$, the $p$-adic field |
| $\mathbb{A}_K$, $\mathbb{I}_K$, $G(\mathbb{A}_K)$ | the adeles, the ideles and the adelic points of $G$ |
| $LG$, $\operatorname{Homeo}(X)$, $\operatorname{Diff}(M)$ | the loop group, the homeomorphism group, the diffeomorphism group |
| $\Gamma_k = 1 + p^kM_n(\mathbb{Z}_p)$ | the congruence subgroups |

## Further Reading

- Nicolas Bourbaki, *General Topology*, Chapters III–IV (Springer, 1989), for the topological groups, the uniformities and the completion.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis*, Vol. I (Springer, 2nd ed. 1979), for the structure of locally compact abelian groups, the Haar measure and the duality.
- Lynn A. Steen and J. Arthur Seebach, *Counterexamples in Topology* (Springer, 2nd ed. 1978), for the Sorgenfrey line and the other counterexamples.
- John S. Wilson, *Profinite Groups* (Oxford University Press, 1998), for the inverse-limit topology, the pro-$p$ groups and the Frattini theory.
