# __List of Modules__

## Introduction

This article lists the modules and the vector spaces of the corpus, with the rank, the basis, the torsion and the freeness of each. A module over a ring generalises a vector space over a field, and the list records exactly which of the four notions survives the generalisation: every vector space is free and has a basis, a module need not be free, the rank is defined for free modules and for torsion-free modules over a domain, and torsion is a phenomenon a field does not have.

Every entry points to the article that introduces the module or the vector space and states its invariant. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a module that fails to have a basis or to be torsion-free where a vector space would not, with the failure named and the article that records it.

## Vector Spaces

A **vector space** over a field $F$ is a module over $F$; because $F$ is a field, every module is free, every linearly independent set extends to a **basis**, and any two bases have the same cardinality, the **dimension**. Subspaces, quotients, direct sums, the dual and the space of linear maps are all vector spaces, and the dimension is additive in short exact sequences.

| Vector space | Rank, basis, torsion, freeness | Introduced in |
|---|---|---|
| $F^n$ | dimension $n$, the standard basis $e_1,\dots,e_n$; free, torsion-free | *Vector Spaces* |
| Arbitrary vector space $V$ | a basis exists by Zorn's lemma; dimension $\dim_F V$; free | *Vector Spaces* |
| Subspace and quotient | subspaces are direct summands; $\dim V = \dim W + \dim V/W$ for a subspace $W$ | *Vector Spaces* |
| Direct sum $\bigoplus_i V_i$ | dimension the sum of the dimensions; free | *Vector Spaces* |
| Dual space $V^* = \operatorname{Hom}_F(V,F)$ | dimension $\dim_F V$ in finite dimension; free | *Multilinear Spaces* |
| Space of linear maps $\operatorname{Hom}_F(V,W)$ | dimension $\dim_F V \cdot \dim_F W$; free | *Vector Spaces* |
| The vector space $\mathbb{H}^n$ over the division ring $\mathbb{H}$ | a free module of rank $n$, of real dimension $4n$; every $\mathbb{H}$-module is free | *Quaternionic and Biquaternionic Modules* |
| Non-example: a torsion element in a vector space | does not occur: a nonzero scalar multiple of a nonzero vector is nonzero, so $T(V) = 0$ | *Vector Spaces* |
| Non-example: a module over a field that is not free | does not occur: over a field every module is free, by the existence of bases | *Vector Spaces* |

## Free, Projective and Injective Modules

A module is **free** when it has a basis, **projective** when it is a direct summand of a free module, and **injective** when it is a direct summand of every module containing it; free implies projective, and over a principal ideal domain projective, free and torsion-free coincide for finitely generated modules. The **rank** is the cardinality of a basis of a free module, well defined by the invariant basis number property.

| Module | Rank, basis, torsion, freeness | Introduced in |
|---|---|---|
| Free module $R^{(I)}$ | basis $\{e_i\}$; free by definition, rank $|I|$ | *Modules* |
| Finitely generated free module $R^n$ | rank $n$; free, torsion-free over a domain | *Direct Sums, Free Modules and Rank* |
| Projective module $P$ | a direct summand of a free module; not necessarily free | *Projective and Injective Modules* |
| Injective module $I$ | a direct summand of every containing module; Baer's criterion tests it | *Projective and Injective Modules* |
| $\mathbb{Q}$ and $\mathbb{Q}/\mathbb{Z}$ | divisible abelian groups; injective as $\mathbb{Z}$-modules | *Projective and Injective Modules* |
| $R/(a)$ over a PID | not free for $a \neq 0$; torsion, of projective dimension $1$ | *Projective and Injective Modules* |
| $\mathbb{Z}[1/p]$ | a localisation of $\mathbb{Z}$; torsion-free, not finitely generated, not free | *Projective and Injective Modules* |
| Free resolution $L_1 \to L_0 \to M \to 0$ | exhibits $M$ as a quotient of free modules; measures the failure of freeness | *Direct Sums, Free Modules and Rank* |
| Non-example: a projective module that is not free | fails freeness over a general ring: projective is necessary but not sufficient | *Projective and Injective Modules* |
| Non-example: the invariant basis number property | fails over a general ring: the rank is well defined only when IBN holds | *Direct Sums, Free Modules and Rank* |

## Finitely Generated Modules over a Principal Ideal Domain

Over a principal ideal domain every submodule of a free module is free, every finitely generated torsion-free module is free, and every finitely generated module is a direct sum of a free module and cyclic torsion modules with unique invariants. The **torsion submodule** $M_{\mathrm{tor}}$ collects the elements annihilated by a nonzero element of the ring, the **rank** is the free rank, and the theorem specialises to the classification of finitely generated abelian groups and to the rational and Jordan forms.

| Module | Rank, basis, torsion, freeness | Introduced in |
|---|---|---|
| $M \cong R^r \oplus R/(d_1) \oplus \cdots \oplus R/(d_k)$ | free rank $r$, invariant factors $d_1 \mid \cdots \mid d_k$; torsion the second summand | *Modules over a PID* |
| Torsion submodule $M_{\mathrm{tor}}$ | the elements of nonzero annihilator; a direct summand of a finitely generated module | *Modules over a PID* |
| $p$-primary component $M_p$ | the torsion part at the prime $p$; elementary divisors $p^{e_{p,j}}$ | *Modules over a PID* |
| Cyclic module $R/(a)$ | rank $0$; torsion; free exactly when $a = 0$ | *Modules over a PID* |
| $\mathbb{Z}$-module of finite type | the case $R = \mathbb{Z}$: free part $\mathbb{Z}^r$ plus torsion | *Finitely Generated Abelian Groups* |
| $k[x]$-module | the case $R = k[x]$: the rational and Jordan forms of an operator | *Modules over $k[x]$ and the Jordan Form* |
| Torsion-free finitely generated module over a PID | free, of rank equal to the free rank | *Modules over a PID* |
| Non-example: $\mathbb{Q}$ as a $\mathbb{Z}$-module | torsion-free but not free: it is not finitely generated | *Modules* |
| Non-example: a submodule of a free module over a general ring | fails to be free: the statement needs a principal ideal domain | *Modules* |

## Torsion, Simple and Semisimple Modules

A module is **simple** when it has no proper nonzero submodule, **semisimple** when it is a direct sum of simples, and semisimple modules have no torsion in the module-theoretic sense over a division ring. The **Jacobson radical** $J(R)$ is the obstruction to semisimplicity, the **density theorem** describes the action on a semisimple module, and Schur's lemma makes the endomorphism ring of a simple module a division ring.

| Module | Rank, basis, torsion, freeness | Introduced in |
|---|---|---|
| Simple module $S$ | no proper nonzero submodule; $\operatorname{End}_A(S)$ a division ring | *Simple and Semisimple Modules* |
| Semisimple module | a direct sum of simples; every submodule a direct summand | *Simple and Semisimple Modules* |
| Isotypic component | the summands of one isomorphism class; endomorphism ring a matrix ring | *Simple and Semisimple Modules* |
| Jacobson radical $J(R)$ | the intersection of the maximal left ideals; zero exactly when $R$ is semisimple | *Simple and Semisimple Modules* |
| Modules over a semisimple algebra | all semisimple; a direct sum of copies of the simple modules | *Simple and Semisimple Modules* |
| Non-example: the module $k[x]/(x^2)$ over $k[x]/(x^2)$ | fails semisimplicity: it has a nonzero radical | *Simple and Semisimple Modules* |
| Non-example: a module of infinite length | fails the finite composition series: the length is not defined | *Simple and Semisimple Modules* |

## Modules over Division Rings and the Number Systems

Over a division ring every module is free, and the rank theory is that of vector spaces; the corpus develops this for $\mathbb{H}$ and for the biquaternions $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} \cong M_2(\mathbb{C})$, where the zero divisors of $\mathbb{B}$ prevent a basis and the module theory is governed instead by Morita equivalence with complex vector spaces.

| Module | Rank, basis, torsion, freeness | Introduced in |
|---|---|---|
| $\mathbb{H}^n$ | free of rank $n$ over the division ring $\mathbb{H}$; basis $e_1,\dots,e_n$; real dimension $4n$ | *Quaternionic and Biquaternionic Modules* |
| Finitely generated $\mathbb{B}$-module | isomorphic to $S^{\oplus k}$ for the unique simple $S = \mathbb{C}^2$; complex dimension $2k$ | *Quaternionic and Biquaternionic Modules* |
| The defining module $S$ of $\mathbb{B}$ | the unique simple $\mathbb{B}$-module; not free over $\mathbb{B}$ in the vector-space sense | *The Defining Module of the Biquaternion Algebra* |
| $\mathbb{H}$-module structure | complex structure $I$ and quaternionic structure $\mathcal{J}$; $J(\mathbb{H}) = 0$ | *Quaternionic and Biquaternionic Modules* |
| Lipschitz order $\mathbb{Z}\{e_0,e_1,e_2,e_3\}$ | a torsion-free $\mathbb{Z}$-module of rank $4$, not free over a non-commutative order | *Lattices and the Quaternion Lattice* |
| Non-example: a $\mathbb{B}$-module treated as a vector space | fails to have a basis over $\mathbb{B}$: the ring has zero divisors | *Biquaternion Algebra* |
| Non-example: a torsion element of an $\mathbb{H}$-module | does not occur: $\mathbb{H}$ is a division ring, so every nonzero module is torsion-free | *Quaternionic and Biquaternionic Modules* |

## Homomorphisms, Duals and Tensor Products

The module $\operatorname{Hom}_R(M,N)$ of homomorphisms and the dual $M^* = \operatorname{Hom}_R(M,R)$ are again modules; the tensor product $M \otimes_R N$ is a module with the universal property of bilinear maps. The list records these constructions because they are the ones that distinguish the free and projective modules from the general ones: $\operatorname{Hom}$ and the tensor product are not exact in both variables, and the derived functors $\operatorname{Ext}$ and $\operatorname{Tor}$ measure the failure.

| Construction | Rank, basis, torsion, freeness | Introduced in |
|---|---|---|
| $\operatorname{Hom}_R(M,N)$ | a module; left exact in $M$; a free module when $M$ is free of finite rank | *Modules* |
| Dual module $M^* = \operatorname{Hom}_R(M,R)$ | the linear forms; for a finitely generated projective module, $(M^*)^* \cong M$ | *Projective and Injective Modules* |
| Tensor product $M \otimes_R N$ | right exact; $R \otimes_R M \cong M$; $(R^{(I)})\otimes_R N \cong N^{(I)}$ | *Modules* |
| Tensor product of vector spaces | $\dim_F(V\otimes_F W) = \dim_F V \cdot \dim_F W$; free | *Multilinear Spaces* |
| Bilinear and multilinear maps | the universal property identifying them with maps on the tensor product | *Multilinear Spaces* |
| $\operatorname{Ext}_R^n(M,N)$ and $\operatorname{Tor}_n^R(M,N)$ | the derived functors measuring the failure of exactness | *Ext and Tor* |
| Non-example: exactness of $\operatorname{Hom}_R(M,-)$ | fails in general: it is left exact only, and $\operatorname{Ext}^1$ is the obstruction | *Ext and Tor* |
| Non-example: exactness of $-\otimes_R N$ | fails in general: it is right exact only, and $\operatorname{Tor}_1$ is the obstruction | *Ext and Tor* |

## Summary

The list gathers the modules and vector spaces of the corpus. The vector spaces over a field are free, have bases and dimensions, have no torsion, and their subspaces and quotients are again vector spaces. The modules over a general ring are the free, projective and injective modules, with the rank defined by a basis under the invariant basis number property and the free resolutions measuring the failure of freeness. Over a principal ideal domain the finitely generated modules are classified by a free rank and the torsion invariants, with the cases $\mathbb{Z}$ and $k[x]$ giving the abelian groups and the Jordan form. The simple and semisimple modules, the Jacobson radical and the density theorem describe the semisimple side. Over a division ring every module is free; over the quaternions the rank theory is that of vector spaces, and over the biquaternions the module theory is the Morita equivalence with complex vector spaces. The non-examples — a torsion element of a vector space, a non-free module over a field, a projective module that is not free, a ring without the invariant basis number property, $\mathbb{Q}$ as a torsion-free non-free $\mathbb{Z}$-module, a submodule of a free module over a general ring, the module $k[x]/(x^2)$ and a module of infinite length, a $\mathbb{B}$-module treated as a vector space and a torsion element of an $\mathbb{H}$-module — each name the property that fails.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $V$, $W$, $\dim_F V$ | vector spaces and their dimension |
| $V^*$ | dual space |
| $R^{(I)}$, $R^n$ | free module, finitely generated free module |
| $\operatorname{rk}_R L$ | rank of a free module |
| $M_{\mathrm{tor}}$, $M_p$ | torsion submodule and primary component |
| $R/(a)$ | cyclic module |
| $J(R)$ | Jacobson radical |
| $S$, $\operatorname{End}_A(S)$ | simple module and its endomorphism division ring |
| $\mathbb{H}^n$, $S^{\oplus k}$ | free $\mathbb{H}$-module, finitely generated $\mathbb{B}$-module |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | biquaternions |
| $\mathbb{Z}$, $\mathbb{Q}$ | the integers and the rationals |
| $R^r \oplus R/(d_1)\oplus\cdots$ | structure theorem over a PID |

## Further Reading

- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009), for the module theory over a general ring and over a principal ideal domain.
- Thomas Hungerford, *Algebra* (Springer, 1974), for the structure theorem for finitely generated modules over a PID and its applications.
- Frank Anderson and Kent Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for projective, injective and semisimple modules and the density theorem.
- Paul Cohn, *Free Rings and Their Relations* (Academic Press, 2nd ed. 1985), for free, projective and torsion-free modules over general rings and the invariant basis number property.
