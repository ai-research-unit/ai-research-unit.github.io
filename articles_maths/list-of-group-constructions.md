# __List of Group Constructions__

## Introduction

This article lists the constructions by which the corpus builds a group from smaller groups: the direct products and direct sums, the semidirect and wreath products, the extensions, the free products, the free products with amalgamation, the HNN extensions and the quotients by normal subgroups. For each construction the list records what it preserves — whether the factors remain as subgroups, whether the result is finite when the factors are, whether the factors commute — and the article that introduces it.

Every entry points to the article that introduces the construction. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a construction that fails to have a property its neighbour has, with the failure named and the article that records it.

## Direct Products and Direct Sums

The **direct product** of a family of groups is the group of functions into the family with pointwise multiplication; the **direct sum** is the subgroup of finitely supported functions, and for finitely many factors the two agree. The product is the categorical product with its projections, the sum the coproduct with its injections, and a group is the **internal direct product** of two subgroups when they commute and generate it.

| Construction | What it preserves | Introduced in |
|---|---|---|
| Direct product $\prod_i G_i$ | the projections; the factors embed and commute elementwise | *Infinite Abelian Groups* |
| Direct sum $\bigoplus_i G_i$ | the injections; the finitely supported subgroup of the product | *Infinite Abelian Groups* |
| Direct power $G^I$ | the product of $|I|$ copies of one group | *Generators, Presentations and Free Products* |
| Internal direct product | two commuting subgroups generating the group | *Groups* |
| Direct product of finitely many factors | finite when the factors are finite, of order the product of the orders | *Groups* |
| Non-example: $S_3 \times \mathbb{Z}/2\mathbb{Z}$ | the direct product is not the semidirect product: the factors commute, and $S_3 \times \mathbb{Z}/2\mathbb{Z}$ has no normal $S_3$ complement | *Groups* |

## Semidirect and Wreath Products

The **semidirect product** $N \rtimes_\varphi H$ is built from a homomorphism $\varphi : H \to \operatorname{Aut}(N)$, so that $H$ acts on $N$ and the product law is twisted by $\varphi$; it is the split extension of $H$ by $N$. The **wreath product** $A \wr H$ is the semidirect product of a direct sum of copies of $A$ indexed by $H$ with $H$ acting by permutation of the summands.

| Construction | What it preserves | Introduced in |
|---|---|---|
| Semidirect product $N \rtimes_\varphi H$ | both factors as subgroups; $N$ normal, $H$ a complement | *Generators, Presentations and Free Products* |
| Split extension $1 \to N \to G \to H \to 1$ with section $s$ | the short exact sequence splits; $G$ is a semidirect product | *Generators, Presentations and Free Products* |
| Dihedral group as $C_n \rtimes C_2$ | the reflection action on the rotation group | *Finite Groups and Symmetry* |
| Affine group $\operatorname{Aff}(V) = V \rtimes GL(V)$ | the translations normal, the linear group a complement | *Affine Spaces and Translations* |
| Wreath product $A \wr H = A^{(H)} \rtimes H$ | the base group $A^{(H)}$ normal, $H$ permuting coordinates | *Infinite Groups* |
| Lamplighter group $(\mathbb{Z}/2\mathbb{Z}) \wr \mathbb{Z}$ | a finitely generated metabelian group that is not Noetherian | *Infinite Groups* |
| Hyperoctahedral group $W(B_n) = S_n \ltimes (\mathbb{Z}/2\mathbb{Z})^n$ | a wreath product realised as a reflection group | *Symplectic Reflection Algebras* (Part II) |
| Non-example: $N \rtimes_\varphi H$ with $\varphi$ nontrivial | fails to be the direct product: the factors do not commute | *Generators, Presentations and Free Products* |
| Non-example: $A \wr H$ for infinite $H$ | fails to be finitely generated in general: the base group is an infinite direct sum | *Infinite Groups* |

## Extensions and Cohomological Constructions

An **extension** of $H$ by $N$ is a short exact sequence $1 \to N \to E \to H \to 1$; it is **split** when a section exists, so that $E$ is a semidirect product, and **central** when $N$ lies in the centre. The extensions inducing a fixed action of $H$ on $N$ are classified by the second cohomology $H^2(H,N)$, with the split extension as the zero class and the Baer sum as the addition; the third cohomology classifies the crossed modules and $2$-fold extensions.

| Construction | What it preserves | Introduced in |
|---|---|---|
| Extension $1 \to N \to E \to H \to 1$ | $N$ normal in $E$; the quotient isomorphic to $H$ | *Generators, Presentations and Free Products* |
| Classification by $H^2(H,N)$ | the action of $H$ on $N$ and the equivalence classes of extensions | *Group Cohomology* |
| Split extension | the extension has a section; equivalently the class is zero | *Group Cohomology* |
| Central extension | $N$ central in $E$; classified by $H^2(H,N)$ with trivial action | *Group Cohomology* |
| Universal central extension | through which every central extension of a perfect group factors uniquely | *Group Cohomology* |
| Schur multiplier $M(G) = H_2(G,\mathbb{Z})$ | the kernel of the universal central extension | *Group Cohomology* |
| Schur–Zassenhaus splitting | the extension splits when $\gcd(|M|,|G|)=1$ | *Group Cohomology* |
| Non-example: a nonsplit extension of coprime order | does not exist: Schur–Zassenhaus forces a splitting | *Group Cohomology* |
| Non-example: an extension of $H$ by $N$ with a nonabelian kernel | fails the $H^2$ classification: the kernel must be abelian for the cohomological classification | *Group Cohomology* |

## Free, Amalgamated and HNN Constructions

The **free product** $G_1 * G_2$ is the coproduct of groups, the universal group receiving both factors with no relation between them; it is infinite whenever one factor is nontrivial and has more than one element. The **free product with amalgamation** $G_1 *_H G_2$ identifies a common subgroup, and the **HNN extension** adjoins a stable letter conjugating one subgroup onto another; both are the group-theoretic pushout and its relative.

| Construction | What it preserves | Introduced in |
|---|---|---|
| Free product $G_1 * G_2$ | both factors as subgroups; no relation between them | *Generators, Presentations and Free Products* |
| Infinite dihedral group $D_\infty = C_2 * C_2$ | a free product that is virtually cyclic | *Generators, Presentations and Free Products* |
| Free product with amalgamation $G_1 *_H G_2$ | the common subgroup $H$; the pushout over it | *Combinatorial Group Theory* |
| HNN extension | a subgroup identified with its image under an isomorphism via a stable letter | *Combinatorial Group Theory* |
| Kurosh subgroup theorem | the subgroups of a free product are free products of copies of subgroups of the factors and a free group | *Combinatorial Group Theory* |
| Nielsen–Schreier theorem | every subgroup of a free group is free | *Combinatorial Group Theory* |
| Presentation $\langle X \mid R\rangle$ | the quotient of the free group by the normal closure of $R$ | *Generators, Presentations and Free Products* |
| Non-example: $G_1 * G_2$ for nontrivial $G_1, G_2$ | fails to be finite unless both factors have order $2$: the free product is infinite | *Generators, Presentations and Free Products* |
| Non-example: $G_1 *_H G_2$ with $H$ not normal in either factor | fails the pushout description when the maps do not identify $H$ | *Combinatorial Group Theory* |

## Quotients, Series and Presentations

A **quotient** $G/N$ is formed by a normal subgroup, and the quotient of a group by the normal closure of a set of relations is a **presentation**. The derived and lower central series are iterated quotients, and their termination defines the solvable and the nilpotent groups; the abelianisation is the universal abelian quotient.

| Construction | What it preserves | Introduced in |
|---|---|---|
| Quotient $G/N$ | the group law on the cosets; exists exactly for normal $N$ | *Groups* |
| Normal closure $\langle\langle R\rangle\rangle$ | the smallest normal subgroup containing a set of relations | *Generators, Presentations and Free Products* |
| Abelianisation $G^{\mathrm{ab}} = G/[G,G]$ | the largest abelian quotient of $G$ | *Groups* |
| Derived series | the iterated commutator subgroups; terminates for solvable groups | *Solvable and Nilpotent Groups* |
| Lower central series | the iterated commutators with $G$; terminates for nilpotent groups | *Solvable and Nilpotent Groups* |
| Subgroup generated by $S$ | the smallest subgroup containing $S$ | *Groups* |
| Non-example: $G/N$ for a non-normal $N$ | fails to be a group: the coset multiplication is not well defined | *Groups* |

## What Each Construction Preserves

The constructions differ in the properties they preserve; the table collects the comparison that the scope line asks for.

| Construction | Preserves finiteness | Preserves freeness | Keeps factors as subgroups |
|---|---|---|---|
| Direct product | yes, for finitely many factors | yes | yes |
| Direct sum | yes, for finitely many factors | yes | yes |
| Semidirect product | yes, for finite factors | only when the action is trivial | yes |
| Wreath product | yes, for finite factors | no | yes |
| Extension | yes, for finite kernel and quotient | no | the kernel only |
| Free product | no, unless both factors have order $2$ | yes | yes |
| Free product with amalgamation | no, in general | no | the factors, modulo $H$ |
| HNN extension | no, in general | no | the base group |
| Quotient | yes | no | no |

## Summary

The list gathers the group constructions of the corpus. The products are the direct product, the direct sum, the direct power and the internal direct product; the twisted products are the semidirect product, the wreath product, the lamplighter group, the dihedral group and the affine group; the extensions are the general extension, its classification by the second cohomology, the split and central extensions, the universal central extension with the Schur multiplier as kernel, and the Schur–Zassenhaus splitting; the free constructions are the free product, the free product with amalgamation, the HNN extension and the presentations, with the Kurosh and Nielsen–Schreier theorems; the quotients are the quotient by a normal subgroup, the abelianisation, the normal closure and the derived and lower central series. The final table compares what each construction preserves, and the non-examples — the direct product that is not a semidirect product, the semidirect product with a nontrivial action, the infinite wreath product, the coprimal-order nonsplit extension, the extension with a nonabelian kernel, the infinite free product, the free product with a non-identified subgroup and the quotient by a non-normal subgroup — name the property that fails.

## Summary of Notation

The article denotes its constructions by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $\prod_i G_i$, $\bigoplus_i G_i$, $G^I$ | direct product, direct sum, direct power |
| $N \rtimes_\varphi H$ | semidirect product with action $\varphi$ |
| $A \wr H$ | wreath product |
| $1 \to N \to E \to H \to 1$ | short exact sequence, an extension |
| $H^n(G,M)$, $H_2(G,\mathbb{Z})$ | group cohomology; Schur multiplier |
| $G_1 * G_2$ | free product |
| $G_1 *_H G_2$ | free product with amalgamation |
| $\langle X \mid R\rangle$, $\langle\langle R\rangle\rangle$ | presentation and normal closure |
| $G^{\mathrm{ab}} = G/[G,G]$ | abelianisation |
| $[G,G]$ | commutator subgroup |

## Further Reading

- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, 4th ed. 1995), for direct and semidirect products and the extension theory.
- Roger Lyndon and Paul Schupp, *Combinatorial Group Theory* (Springer, 1977), for free products, amalgamated products, HNN extensions and the Kurosh and Nielsen–Schreier theorems.
- Kenneth Brown, *Cohomology of Groups* (Springer, 1982), for the classification of extensions by $H^2$, the Schur multiplier and the universal central extension.
- John Conway, Robert Curtis, Simon Norton, Richard Parker and Robert Wilson, *Atlas of Finite Groups* (Oxford University Press, 1985), for the explicit extensions and wreath-product constructions among the finite groups.
