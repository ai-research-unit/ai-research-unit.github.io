# __List of Group Actions__

## Introduction

This article lists the actions by which the corpus realises an abstract group as transformations of a set, an order, a vector space, an algebra or a field. For each action the list records the orbit, the stabiliser and the representation the action furnishes — the permutation representation, the defining representation, the regular representation, the Galois action or the action on a lattice of subgroups — together with the article that introduces it.

Every entry points to the article that introduces the action. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being an action that fails faithfulness or transitivity where its neighbour has it, with the failure named and the article that records it.

## Actions on Sets

An **action** of $G$ on a set $X$ is a homomorphism $\rho : G \to \operatorname{Sym}(X)$; the **orbit** of a point is its equivalence class under the action, the **stabiliser** is the subgroup fixing it, and the orbit–stabiliser theorem relates the two to the order of the group. The action is **faithful** when the kernel of $\rho$ is trivial; the left regular action shows every group embeds in a symmetric group, which is Cayley's theorem.

| Action | Orbit, stabiliser and representation | Introduced in |
|---|---|---|
| Left regular action of $G$ on itself | one orbit $G$; stabiliser trivial; the regular permutation representation, giving Cayley's embedding $G \hookrightarrow \operatorname{Sym}(G)$ | *Transformation Groups* |
| Conjugation action of $G$ on itself | orbits the conjugacy classes; stabiliser $C_G(g)$, the centraliser; the permutation representation on conjugacy classes | *Group Actions and Structure* |
| Action of $G$ on the cosets $G/H$ | one orbit; stabiliser a conjugate of $H$; a transitive $G$-set | *Transformation Groups* |
| Action of $G$ on its subgroups by conjugation | orbits the conjugacy classes of subgroups; stabiliser the normaliser $N_G(H)$ | *Group Actions and Structure* |
| Action of $G$ on the power set of a $G$-set | orbits the sets of $k$-subsets; the induced permutation representation | *Transformation Groups* |
| Action of $G$ on itself by left multiplication, a monoid action | the monoid of endomorphisms; $\operatorname{Aut}(X) = \operatorname{End}(X)^\times$ for a structure $X$ | *Transformation Groups* |
| Permutation representation | the homomorphism $\rho : G \to \operatorname{Sym}(X)$; faithful exactly when $\ker\rho = 1$ | *Transformation Groups* |
| Non-example: the trivial action of a nontrivial group | fails faithfulness: the kernel is the whole group | *Transformation Groups* |
| Non-example: the action of $S_n$ on $\{1,\dots,n\}$ for $n \geq 3$ | fails to be regular: the stabiliser of a point has order $(n-1)!$, not $1$ | *Transformation Groups* |

## Actions on Lattices of Subgroups

The action-theoretic proofs of finite group theory use carefully chosen sets: the Sylow theorems apply the orbit–stabiliser theorem to the conjugation action on the Sylow subgroups, and the class equation counts the orbits of the conjugation action on the group itself. These actions act on a lattice of subgroups, ordered by inclusion, which is where the corpus meets the action of a group on an order.

| Action | Orbit, stabiliser and representation | Introduced in |
|---|---|---|
| Conjugation action on $\operatorname{Syl}_p(G)$ | the number of orbits $n_p$ divides the index; stabiliser the normaliser of a Sylow subgroup | *Group Actions and Structure* |
| Action of $G$ on the cosets of a Sylow subgroup | the representation $G \to S_{n_p}$ whose kernel controls the normal Sylow subgroup | *Group Actions and Structure* |
| Class equation | the orbit decomposition of conjugation; the fixed points are the centre $Z(G)$ | *Group Actions and Structure* |
| Action of $G$ on its subgroups, ordered by inclusion | the lattice of subgroups is a $G$-poset; the orbits are the conjugacy classes of subgroups | *Group Actions and Structure* |
| Double-coset action of $H \times K$ on $G$ | orbits the double cosets $HaK$; stabilisers the intersections $H \cap aKa^{-1}$ | *Group Actions and Structure* |
| Burnside's lemma | the number of orbits as the average of the fixed-point counts | *Group Actions and Structure* |
| Non-example: the conjugation action of an abelian group | fails to be interesting only: every orbit is a point, since $C_G(g) = G$ | *Group Actions and Structure* |

## Actions on Vector Spaces and Modules: the Representations

An action of $G$ on a vector space by linear maps is a **representation** of $G$, equivalently a module over the group algebra $F[G]$. The corpus meets the permutation representation of a group action, the defining representation of $GL(V)$, the regular representation of $G$ on $F[G]$, the dual and tensor representations, the symmetric and exterior powers, and the adjoint representation of a Lie algebra.

| Action | Orbit, stabiliser and representation | Introduced in |
|---|---|---|
| Linear action of $GL(V)$ on $V$ | the defining representation; the orbit of a vector is its nonzero scalar multiples, and the stabiliser the stabiliser of a line | *The General Linear Group* |
| Action of $GL(V)$ on the lines and Grassmannians | the orbits are the Grassmannians; the stabilisers the parabolic subgroups | *The General Linear Group* |
| Regular representation of $G$ on $F[G]$ | $G$ acts on the group algebra; the character is $\chi_{\mathrm{reg}}(e) = |G|$ | *Group Algebras* |
| Permutation representation of a $G$-set | the linearisation of an action on a set; the character counts fixed points | *Representations of Groups* |
| Tensor, dual, symmetric and exterior powers | the representations $V \otimes W$, $V^*$, $\operatorname{Sym}^n V$ and $\Lambda^n V$ | *Representations of Groups* |
| Adjoint action of a Lie algebra on itself | orbits the coadjoint orbits; the representation $\operatorname{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ | *Lie Algebras* |
| Weight decomposition | the action of a Cartan subalgebra; the weights and the highest weight | *Representations of Lie Algebras* |
| Schur–Weyl action of $S_n \times GL(V)$ on $V^{\otimes n}$ | orbits and stabilisers described by Young diagrams; the decomposition into Schur functors | *Schur–Weyl Duality* |
| Non-example: a non-faithful representation | fails faithfulness: the kernel is a nontrivial normal subgroup | *Representations of Groups* |
| Non-example: a reducible representation in characteristic dividing $|G|$ | fails complete reducibility: Maschke's hypothesis is defeated | *Representations of Groups* |

## Actions on Algebras and Fields

A group acts on an algebra by **automorphisms**, and the subalgebra it fixes is the **ring of invariants**; a group acts on a field extension as its **Galois group**, and the fixed field is the subject of the fundamental theorem. The action of a group on an algebra also builds new algebras, the crossed products, and the infinitesimal version of an automorphism is a derivation.

| Action | Orbit, stabiliser and representation | Introduced in |
|---|---|---|
| Action of $\operatorname{Aut}(R)$ on a ring $R$ | the fixed subring and the invariant centre; the transformation group of the ring | *Ring and Field Automorphisms* |
| Inner action $x \mapsto uxu^{-1}$ by a unit | the orbit is the conjugacy class; the action is by an inner automorphism | *Ring and Field Automorphisms* |
| Galois action of $\operatorname{Gal}(L/K)$ on $L$ | the fixed field is $K$; the orbit of an element has size the degree of its minimal polynomial | *Galois Theory* |
| Action of $G$ on a polynomial ring by graded automorphisms | the invariant ring $R^G$; the Molien series computes the graded dimensions | *Invariant Theory* |
| Crossed product $A \# G$ | the algebra built from a group action, with the action as twisted multiplication | *Crossed Products* |
| Action of $G$ on an algebra by automorphisms | the orbits of the automorphism group; the fixed subalgebra | *Automorphisms and Derivations of Algebras* |
| Derivation as the infinitesimal action | a derivation $\delta$ with the Leibniz rule; the inner derivations $\operatorname{ad}_a$ | *Automorphisms and Derivations of Algebras* |
| Frobenius action on a finite field | the automorphism $x \mapsto x^p$, of order the degree over $\mathbb{F}_p$ | *Ring and Field Automorphisms* |
| Non-example: an infinite Galois group of a finite extension | fails the finite-orbit description: the action is trivial on a finite Galois extension | *Galois Theory* |
| Non-example: an action of $\operatorname{Aut}(R)$ that fails to preserve the centre | does not occur: an automorphism preserves the centre, so the centre is a stabilised subring | *Ring and Field Automorphisms* |

## Actions on Spaces

Once a distance is available, a group acts on a topological space by homeomorphisms or by isometries, and the orbit–stabiliser theorem acquires the orbit map as a quotient map. The corpus treats these actions in Part II and Part III, and the algebraic layer records only the algebraic shadow of them.

| Action | Orbit, stabiliser and representation | Introduced in |
|---|---|---|
| Action of a topological group on a space | orbits are the homogeneous spaces; the orbit map is continuous | *Topological Groups* (Part II) |
| Action of a discrete group on a space by deck transformations | the orbits are the fibres of a covering; the stabilisers are the deck group | *The Fundamental Group and Covering Spaces* (Part II) |
| Isometric action on a metric space | orbits are the equidistant sets; stabilisers are the isometry subgroups | *Metric, Uniform and Complete Spaces* (Part II) |
| Linear action of a Lie group on a manifold | the orbits are the homogeneous spaces $G/H$; the representation of the Lie algebra | *Lie Groups* (Part II) |
| Non-example: an action by homeomorphisms that is not by isometries | fails to preserve the distance: the orbit map is continuous but not Lipschitz | *Metric, Uniform and Complete Spaces* (Part II) |

## The Three Properties of an Action

Every action in the list is separated by three properties — whether it is faithful, whether it is transitive, and whether it is regular — and the table reads them side by side so that the same group appears with different properties on different sets.

| Action | Faithful? | Transitive? | Introduced in |
|---|---|---|---|
| Left regular action of $G$ on itself | yes: the kernel is trivial | yes: one orbit | *Transformation Groups* |
| Action of $G$ on the cosets $G/H$ | exactly when $H$ contains no nontrivial normal subgroup of $G$ | yes, by construction | *Transformation Groups* |
| Conjugation action of $G$ on itself | exactly when the centre is trivial | exactly when $G$ is abelian | *Group Actions and Structure* |
| Trivial action of a nontrivial group | no: the kernel is the whole group | yes: one orbit | *Transformation Groups* |
| Action of $S_n$ on $\{1,\dots,n\}$, $n \geq 3$ | yes | yes | *Transformation Groups* |

## Summary

The list gathers the group actions of the corpus. The actions on sets are the left regular action and Cayley's embedding, the conjugation action with the conjugacy classes and centralisers, the action on cosets, on subgroups, on power sets and the permutation representation. The actions on a lattice of subgroups are the conjugation action on the Sylow subgroups, the coset action on a Sylow subgroup, the class equation, the double-coset action and Burnside's lemma. The actions on vector spaces are the defining representation of $GL(V)$, its action on lines and Grassmannians, the regular representation on the group algebra, the permutation representation, the tensor, dual, symmetric and exterior power representations, the adjoint representation of a Lie algebra, the weight decomposition and the Schur–Weyl action on tensor powers. The actions on algebras and fields are the automorphism action on a ring, the inner action, the Galois action, the graded action on a polynomial ring with its invariant ring, the crossed product, the derivation as infinitesimal action and the Frobenius. The actions on spaces are the topological, covering, isometric and Lie-group actions of Parts II and III. The non-examples — the trivial action, the non-regular action on a finite set, the conjugation action of an abelian group, a non-faithful representation, a reducible representation in the modular case, an action failing to preserve the centre, and an action by homeomorphisms that is not isometric — each name the property that fails.

## Summary of Notation

The article denotes its actions by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}(X)$, $S_n$ | symmetric group on a set, on $n$ letters |
| $\rho : G \to \operatorname{Sym}(X)$ | permutation representation of an action |
| $\operatorname{Orb}(x)$, $\operatorname{Stab}(x)$ | orbit and stabiliser |
| $C_G(g)$, $Z(G)$, $N_G(H)$ | centraliser, centre, normaliser |
| $\operatorname{Syl}_p(G)$, $n_p$ | Sylow $p$-subgroups and their number |
| $F[G]$, $\chi_V$, $\operatorname{Rep}_F(G)$ | group algebra, character, representation category |
| $V \otimes W$, $V^*$, $\operatorname{Sym}^n V$, $\Lambda^n V$ | tensor, dual, symmetric and exterior power representations |
| $\operatorname{ad}$ | adjoint representation of a Lie algebra |
| $R^G$ | ring of invariants |
| $\operatorname{Gal}(L/K)$ | Galois group of a field extension |
| $\operatorname{Aut}(R)$, $\operatorname{Inn}(G)$ | automorphism group; inner automorphisms |
| $\mathbb{F}_p$, $\mathbb{F}_q$ | finite fields |

## Further Reading

- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, 4th ed. 1995), for the conjugation, coset and Sylow actions and the class equation.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the permutation, regular, tensor and symmetric-power representations.
- Igor Shafarevich, *Basic Algebraic Geometry 1* (Springer, 3rd ed. 2013), for the actions on Grassmannians, the invariant ring and the quotient by a group action.
- Kenneth Brown, *Cohomology of Groups* (Springer, 1982), for the crossed-product and derivation constructions attached to group actions.
