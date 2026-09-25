# __List of Representations__

## Introduction

This article lists the representations the corpus meets. A representation is a module with an action: of a finite group, over its group algebra; of a Lie group, on a topological vector space; of a Lie algebra, on a vector space with a bracket action; of an associative algebra, as a module over it; of a quiver, as a diagram of vector spaces; and of an algebra over one of the number systems, over the real, complex, split-complex, quaternion or biquaternion scalars. Beside each family the list records its characters, its weights and the theorem — Maschke's, Schur's or Weyl's — that governs it.

Every entry points to the article that introduces the representation and names the invariant recorded there. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a representation that fails complete reducibility or a module that fails to be simple, with the failure named and the article that records it.

## Representations of Finite Groups

A representation of a finite group $G$ over a field $F$ is a module over the group algebra $F[G]$. **Maschke's theorem** states that the category of representations is semisimple when the characteristic of $F$ does not divide $|G|$, so every representation is a direct sum of irreducibles; the **character** $\chi_V(g) = \operatorname{Tr}\rho(g)$ is a class function, the irreducible characters satisfy the orthogonality relations, and the number of irreducible complex characters equals the number of conjugacy classes.

| Representation | The property it has | Introduced in |
|---|---|---|
| $F[G]$-module, equivalently $\rho : G \to GL_F(V)$ | the definition of a representation of a finite group | *Representations of Groups* |
| Irreducible representation | a simple $F[G]$-module; the atoms of the semisimple case | *Representations of Groups* |
| Maschke's theorem | complete reducibility when $\operatorname{char} F \nmid |G|$ | *Representations of Groups* |
| Regular representation | the action of $G$ on $F[G]$ by left multiplication; its character is $|G|$ at the identity | *Group Algebras* |
| Permutation representation | the linearisation of a $G$-set; the character counts fixed points | *Representations of Groups* |
| Character $\chi_V$ | the trace of the representation; a class function constant on conjugacy classes | *Character Theory* |
| Orthogonality relations | the inner product of irreducible characters is $\delta_{ij}$ | *Character Theory* |
| Character table | the table of irreducible characters against conjugacy classes | *Character Theory* |
| Clebsch–Gordan decomposition | the tensor product of representations decomposed into irreducibles | *Representations of Groups* |
| Induction and restriction $\operatorname{Ind}_H^G$, $\operatorname{Res}_H^G$ | the representations built from a subgroup and restricted to it | *Representations of Groups* |
| Representation ring $R(G)$ | the Grothendieck ring of representations, with tensor product multiplication | *Representations of Groups* |
| Representations of the symmetric group | the irreducibles indexed by Young diagrams, with the Specht modules and the hook length formula | *Representation Theory of Symmetric Groups* |
| Schur–Weyl decomposition of $V^{\otimes n}$ | the decomposition under $S_n \times GL(V)$ into Schur functors | *Schur–Weyl Duality* |
| Hecke algebra representation | the deformation of the symmetric group's representation theory | *Hecke Algebras* |
| Non-example: a modular representation with $\operatorname{char} F \mid |G|$ | fails complete reducibility: Maschke's hypothesis is defeated, and the Jacobson radical of $F[G]$ is nonzero | *Representations of Groups* |
| Non-example: a non-split extension of two irreducibles | fails semisimplicity: the representation is reducible but not decomposable | *Representations of Groups* |

## Representations of Lie Groups and Lie Algebras

A representation of a Lie algebra $\mathfrak{g}$ is a vector space with a linear map $\mathfrak{g} \to \mathfrak{gl}(V)$ preserving the bracket; a representation of a Lie group is a smooth or continuous action on a vector space, whose differential is a representation of the Lie algebra. **Weyl's theorem** states that every finite-dimensional representation of a semisimple Lie algebra is completely reducible; the irreducible ones are classified by their highest weight, computed from the weights and the roots of a Cartan subalgebra.

| Representation | The property it has | Introduced in |
|---|---|---|
| Representation of a Lie algebra | a module over $\mathfrak{g}$, with the bracket action | *Representations of Lie Algebras* |
| Universal enveloping algebra $U(\mathfrak{g})$ | the associative algebra whose modules are the representations, by the PBW theorem | *Representations of Lie Algebras* |
| Weight and weight space | the generalised eigenspaces of a Cartan subalgebra | *Representations of Lie Algebras* |
| Highest weight representation | the irreducible representation determined by a dominant weight | *Representations of Lie Algebras* |
| Weyl's theorem | complete reducibility for a semisimple Lie algebra | *Representations of Lie Algebras* |
| Weyl character formula | the character of the highest weight representation | *Representations of Lie Algebras* |
| Adjoint representation | the action of $\mathfrak{g}$ on itself by the bracket | *Lie Algebras* |
| Root system and Cartan matrix | the discrete data classifying the semisimple Lie algebras and their representations | *Lie Algebras* |
| Peter–Weyl decomposition | the decomposition of $L^2(G)$ for a compact group into irreducibles | *The Peter–Weyl Theorem* (Part III) |
| Unitary representation of a locally compact group | a continuous action on a Hilbert space, with the imprimitivity theorem | *Representation Theory of Locally Compact Groups* (Part II) |
| Non-example: a representation of a non-semisimple Lie algebra | fails Weyl's theorem: the solvable algebra $\mathfrak{b}$ has non-split extensions | *Representations of Lie Algebras* |
| Non-example: an infinite-dimensional representation of a compact Lie group | fails the finite-dimensional weight classification: the highest weight theory needs finite dimension | *The Peter–Weyl Theorem* (Part III) |

## Representations of Associative Algebras

A representation of an associative algebra $A$ is a left $A$-module, and the structure theory of modules applies directly: the simple modules, the semisimple modules, the radical and the density theorem. **Schur's lemma** states that $\operatorname{End}_A(S)$ is a division ring for a simple module $S$; for a finite-dimensional semisimple algebra over an algebraically closed field, the Wedderburn–Artin structure theorem makes every representation a direct sum of matrix-algebra modules.

| Representation | The property it has | Introduced in |
|---|---|---|
| $A$-module | the definition of a representation of an associative algebra | *Modules over an Algebra* |
| Simple and semisimple module | a module with no proper nonzero submodule; a direct sum of simples | *Simple and Semisimple Modules* |
| Schur's lemma | $\operatorname{End}_A(S)$ is a division ring for a simple $S$ | *Automorphisms of Modules over an Algebra* |
| Density theorem | the image of $A$ in $\operatorname{End}_F(M)$ is dense for a semisimple module | *Automorphisms of Modules over an Algebra* |
| Wedderburn–Artin theorem | a semisimple algebra is a product $\prod_i M_{n_i}(D_i)$ of matrix algebras over division rings | *Simple and Semisimple Modules* |
| Representations of a matrix algebra | the modules over $M_n(k)$, all of the form $k^n \otimes W$ | *Representations of Algebras* |
| Semisimple algebra | an algebra whose every module is semisimple; a product of matrix algebras | *Simple and Semisimple Modules* |
| Group algebra representation | the case $A = F[G]$, reducing to group representations | *Representations of Algebras* |
| Non-example: a representation of the dual numbers $\mathbb{D}'$ | fails semisimplicity: the module $k[x]/x^2$ is not a direct sum of simples | *Simple and Semisimple Modules* |
| Non-example: a module over a non-semisimple algebra | fails to be a direct sum of simples: the radical is nonzero | *Simple and Semisimple Modules* |

## Representations over the Number Systems

The corpus also develops the representation theory of the real, complex, split-complex, quaternion and biquaternion scalars, where the scalars themselves are not a field and the division-ring and zero-divisor cases must be separated. These are the representations of Part V, and they show how the extra structure of the scalar algebra changes the module theory.

| Representation | The property it has | Introduced in |
|---|---|---|
| Real representation | a representation over $\mathbb{R}$, with the real character theory | *Real Representations* |
| Complex representation | a representation over $\mathbb{C}$, the algebraically closed case | *Complex Representations* |
| Split-complex representation | a module over the ring with zero divisors $\mathbb{D}$ | *Split-Complex Representations* |
| Quaternion representation | a module over the division ring $\mathbb{H}$ | *Quaternion Representations* |
| Biquaternion representation | a module over $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with the complex-linear and biquaternion-linear cases separated | *Biquaternion Representation Theory* |
| Non-example: a biquaternion module treated as a vector space | fails to have a basis: $\mathbb{B}$ has zero divisors, so a $\mathbb{B}$-module need not be free | *Biquaternion Representation Theory* |

## Representations of Quivers

A **quiver** is a directed graph, and a representation assigns a vector space to each vertex and a linear map to each arrow; equivalently it is a module over the path algebra. **Gabriel's theorem** classifies the quivers of finite representation type by the simply-laced Dynkin diagrams, and the tame and wild dichotomy of Drozd separates the remaining cases.

| Representation | The property it has | Introduced in |
|---|---|---|
| Representation of a quiver | a diagram of vector spaces and linear maps, equivalently a module over the path algebra | *Quiver Representations and Representation Type* |
| Path algebra | the algebra whose modules are the quiver representations | *Quiver Representations and Representation Type* |
| Gabriel's theorem | a quiver is of finite representation type exactly when its underlying graph is a simply-laced Dynkin diagram | *Quiver Representations and Representation Type* |
| Tame and wild representation type | the dichotomy of Drozd; the tame cases classified by one-parameter families | *Quiver Representations and Representation Type* |
| Auslander–Reiten quiver | the quiver of almost split sequences, encoding the representation type | *Auslander–Reiten Theory* |
| Almost split sequence | the short exact sequence, ending in a given indecomposable, that is universal | *Auslander–Reiten Theory* |
| Non-example: a quiver containing the double source | fails finite representation type: it is of wild type | *Quiver Representations and Representation Type* |
| Non-example: an indecomposable of infinite length | fails Gabriel's finiteness: the module is not finite-dimensional | *Quiver Representations and Representation Type* |

## Summary

The list gathers the representations of the corpus. The representations of a finite group are the $F[G]$-modules, the irreducibles, the regular and permutation representations, the characters with their orthogonality relations and character table, the Clebsch–Gordan decomposition, induction and restriction, the representation ring, the Specht modules of the symmetric group and the Schur–Weyl decomposition, with Maschke's theorem the governing result. The representations of a Lie group and a Lie algebra are the $\mathfrak{g}$-modules, the universal enveloping algebra, the weights and the highest weight classification, the adjoint representation, the root system, Weyl's theorem and character formula, and the Peter–Weyl and unitary representation theories. The representations of an associative algebra are the modules, the simple and semisimple modules, Schur's lemma and the density theorem, the matrix-algebra and group-algebra cases; over the number systems they are the real, complex, split-complex, quaternion and biquaternion representations. The representations of a quiver are the diagrams of vector spaces, the path-algebra modules, Gabriel's classification, the tame–wild dichotomy and the Auslander–Reiten theory. The non-examples — a modular representation, a non-split extension, a representation of a non-semisimple Lie algebra, an infinite-dimensional compact-group representation, a module over the dual numbers or a non-semisimple algebra, a biquaternion module treated as a vector space, a wild quiver and an infinite-length indecomposable — each name the property that fails.

## Summary of Notation

The article denotes its representations by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $F[G]$, $k[G]$ | group algebra |
| $\rho : G \to GL_F(V)$ | representation of a group |
| $\chi_V$, $\operatorname{Res}$, $\operatorname{Ind}$, $R(G)$ | character, restriction, induction, representation ring |
| $\mathfrak{g}$, $\mathfrak{gl}(V)$, $U(\mathfrak{g})$ | Lie algebra, endomorphism algebra, universal enveloping algebra |
| $\operatorname{ad}$ | adjoint representation |
| $M_n(k)$ | matrix algebra |
| $\operatorname{End}_A(S)$, $\operatorname{End}_A(M)$ | endomorphism ring of a simple module, of a module |
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}$, $\mathbb{B}$ | real, complex, split-complex, dual, quaternion and biquaternion scalars |
| $\operatorname{Rep}_F(G)$, $\operatorname{Mod}(A)$ | categories of representations and modules |

## Further Reading

- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for Maschke's theorem, the character orthogonality relations and the finite group case.
- James Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for weights, highest weight theory, Weyl's theorem and the character formula.
- Charles Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the module-theoretic treatment of representations of associative algebras and Schur's lemma.
- Ibrahim Assem, Daniel Simson and Andrzej Skowroński, *Elements of the Representation Theory of Associative Algebras*, Vol. 1 (Cambridge University Press, 2006), for quiver representations, Gabriel's theorem and the Auslander–Reiten theory.
