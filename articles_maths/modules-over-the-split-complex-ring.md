# __Modules over the Split-Complex Ring__

## Introduction

The split-complex ring is a product of two copies of the real field, and its modules are therefore pairs of real vector spaces. That one sentence carries the whole classification, and it also explains what fails. This article writes the equivalence of categories, computes the simple modules, shows that one of the two simple modules is projective and not free, and separates what the vector-space picture keeps from what it loses.

The claim is that the linear algebra over $\mathbb{C}_{\mathrm{spl}}$ is the linear algebra over $\mathbb{R}$ read twice, with one addition and one subtraction. **The addition:** every module is a direct sum of simple modules, so there is no torsion and no pathology of the kind $\mathbb{Z}$ has. **The subtraction:** the notion of a free module no longer covers every module, because a one-dimensional summand sits inside a free module without being free. Both statements have the same proof, the decomposition over the two idempotents.

The ring is *Split-Complex Algebra*, its idempotents are *Ideals and Peirce Decomposition of the Split-Complex Algebra*, and its zero divisors are *Zero Divisors of the Split-Complex Algebra*; the forms on the modules are *The Hermitian Modules and the Hyperbolic Witt Group over the Split-Complex Ring*, next. The comparison with the field case is against *Modules over an Algebra*.

## The Ring Is Not a Field

### The Two Idempotents

The ring carries the two idempotents

$$
\Pi_+=\tfrac12(1+j), \qquad \Pi_-=\tfrac12(1-j),
$$

orthogonal, $\Pi_+\Pi_-=0$, and summing to $1$. The idempotent $\Pi_+$ is not $0$ and not $1$, so the ring has a nontrivial direct sum decomposition, and that is the whole difference from a field: a field has no idempotent other than $0$ and $1$, which is why every module over a field is free.

### The Decomposition of the Ring

**Theorem.** $\mathbb{C}_{\mathrm{spl}}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ as a direct sum of two ideals, and each ideal is isomorphic to $\mathbb{R}$ as a ring, with $\Pi_\pm$ as its unit.

**Proof.** Every element is $Q=Q_+\Pi_++Q_-\Pi_-$ with $Q_\pm\in\mathbb{R}$, uniquely, and the product is componentwise, $QR=(Q_+R_+)\Pi_++(Q_-R_-)\Pi_-$. The map $Q\mapsto Q_+$ is a ring homomorphism onto $\mathbb{R}$, and the map $Q\mapsto(Q_+,Q_-)$ is an isomorphism onto $\mathbb{R}\times\mathbb{R}$.

### The Two Homomorphisms

The two projections are the two ring homomorphisms of $\mathbb{C}_{\mathrm{spl}}$ onto a field, and there are no others: the kernel of such a homomorphism is a maximal ideal, and the maximal ideals of the ring are the two null lines (*Ideals and Peirce Decomposition of the Split-Complex Algebra*). Each projection has for kernel one of the two ideals.

## The Finitely Generated Modules

### The Structure Theorem

**Theorem.** A finitely generated module over $\mathbb{C}_{\mathrm{spl}}$ is a pair $(V_+,V_-)$ of real vector spaces, and the module structure is

$$
Q\cdot(x_+,x_-)=(Q_+x_+,Q_-x_-) .
$$

**Proof.** Evaluation at $\Pi_+$ and at $\Pi_-$ gives two real vector spaces $V_\pm=\Pi_\pm M$, and $M=V_+\oplus V_-$ because $\Pi_++\Pi_-=1$ and $\Pi_+\Pi_-=0$. The action of $Q$ on $V_+$ is the multiplication by the scalar $Q_+$, and on $V_-$ by $Q_-$.

### The Equivalence of Categories

**Corollary.** The category of modules over $\mathbb{C}_{\mathrm{spl}}$ is equivalent to the category of pairs of real vector spaces, by $M\mapsto(V_+,V_-)$, and a homomorphism is a pair of linear maps.

**Proof.** A module map commutes with the action of $\Pi_\pm$, so it preserves each summand, and conversely a pair of linear maps gives a module map because the action is diagonal.

### The Count of the Invariants

The classification is therefore by the pair of dimensions $(\dim V_+,\dim V_-)$, and the dimension of the module as a real vector space is their sum. Over a field the classification is by one number; here it is by two, and the two are the two evaluations of the dimension at the two projections.

## The Simple Modules

### The Two Simple Modules

**Definition.** $S_+=\mathbb{R}\Pi_+$ and $S_-=\mathbb{R}\Pi_-$, each a module of real dimension one.

**Theorem.** $S_+$ and $S_-$ are simple, and they are not isomorphic.

**Proof.** A submodule of $S_+$ is an $\mathbb{R}$-subspace stable under $\mathbb{C}_{\mathrm{spl}}$, and $S_+$ is one-dimensional, so the only submodules are $0$ and $S_+$. A module map $S_+\to S_-$ sends $\Pi_+$ to $\lambda\Pi_-$, and then $\lambda\Pi_-=f(\Pi_+)=f(\Pi_+^2)=\Pi_+f(\Pi_+)=\Pi_+\lambda\Pi_-=0$, so $\lambda=0$ and every such map is zero.

### The Exhaustion

**Theorem.** Every simple module is isomorphic to $S_+$ or to $S_-$.

**Proof.** A simple module is a pair $(V_+,V_-)$ with no nontrivial subpair, so one of the two spaces is $0$ and the other is one-dimensional; the two cases are $S_+$ and $S_-$.

There are exactly two simple modules, up to isomorphism, and they are the two halves of the regular module. Over a field there is one.

### The Regular Module

The regular module is $S_+\oplus S_-$, and this is the Peirce decomposition of *Ideals and Peirce Decomposition of the Split-Complex Algebra* read as a module decomposition. The two summands are the two simple modules, each an ideal, and the ring is their direct sum as a module.

## Projective and Free

### The Projectivity of $S_+$

**Theorem.** $S_+$ is projective and not free.

**Proof.** The regular module is free of rank one and it is $S_+\oplus S_-$, so $S_+$ is a direct summand of a free module, which is the definition of projective. It is not free: a free module of rank $n$ has real dimension $2n$, and $S_+$ has real dimension $1$; the free module of rank $0$ is the zero module, so no rank fits.

The idempotent is the witness. The projector $\Pi_+$ is an endomorphism of the free module of rank one with $\Pi_+^2=\Pi_+$, and the image of a projector is always a direct summand of the source and never, in general, free. Over a field the same argument produces nothing, because the only idempotents there are $0$ and $1$ and their images are the zero module and the whole module, both free.

### What the Failure Costs

The failure of freeness is not a failure of the module theory. Every module is still projective, since every pair $(V_+,V_-)$ is a direct sum of copies of $S_+$ and $S_-$; every module is a direct summand of a free module; and every module is injective. The ring is semisimple, and the linear algebra over it is as clean as the linear algebra over a field, with one change of vocabulary: the word "free" must be replaced by the word "projective".

## What Carries Over

### The Basis and the Rank

A free module has a basis, and a finitely generated module has a **rank pair** $(\dim V_+,\dim V_-)$. The rank is a pair of integers, additive under direct sums, and the free modules are the modules of rank pair $(n,n)$; the projective modules are all the modules, of any rank pair.

### Linear Maps and Matrices

A homomorphism of free modules of rank $m$ and $n$ is a matrix over the ring, and it is a pair of real matrices by the equivalence of categories. The matrix of a map is a pair $(T_+,T_-)$, the two real matrices acting on the two components.

### Injectivity, Surjectivity and Dimension

**Proposition.** A homomorphism is injective, surjective or bijective exactly when both of its components are, and for endomorphisms of a finitely generated module the three conditions are equivalent.

**Proof.** The components are separated by the decomposition, so each property holds for the map exactly when it holds for both components, and over a field each component of a square matrix is injective, surjective or bijective under any one of the three.

### The Sums and the Kernels

Kernels, images and cokernels are computed componentwise, and the module of homomorphisms is $\mathrm{Hom}(M,N)=\mathrm{Hom}(V_+,W_+)\oplus\mathrm{Hom}(V_-,W_-)$. The additive structure of the category is untouched.

## What Does Not Carry Over

### The Single Dimension

A module has no single dimension. The dimension is a pair, and the two entries are independent: for every pair $(p,q)$ of non-negative integers there is a module, and two modules of the same real dimension can be non-isomorphic. The real dimension is the sum of the pair and loses the information.

### The Submodules Need Not Be Free

The free module of rank one has exactly four submodules: $0$, $S_+$, $S_-$ and itself, and two of the four are not free. Over a field every submodule of a free module is free; here the exchange property fails with it, since the single element $1$ spans the free module of rank one and no subset of $\{1\}$ is a basis.

### The Composition Series

Every module has a composition series, of length $\dim V_++\dim V_-$, with the two simple modules as factors, and the length is the sum of the rank pair. The Jordan-Hölder theorem holds, since the ring is semisimple; what fails is only the correspondence between the length and a single dimension.

### The Idempotents of the Endomorphism Ring

The endomorphism ring of $S_+$ is $\mathbb{R}$, and the endomorphism ring of the regular module is the ring itself, which is not a matrix ring over a division ring in the sense of the field case but is $\mathbb{R}\times\mathbb{R}$; the two Wedderburn components are the two simple modules.

## The Comparison with the Field Case

### Every Module Is Free There

Over a field every module is free, so every module is a direct sum of copies of one simple module, and the dimension is one number. Here every module is projective but not every module is free, there are two simple modules, and the dimension is a pair. The change is the change of $\mathbb{R}$ into $\mathbb{R}\times\mathbb{R}$: a product of rings has the modules of the product, and a product of two fields is not a field.

### The Two Types

Over $\mathbb{C}_{\mathrm{spl}}$ the module $S_+$ is the type of the modules that are not free, and it has no counterpart over a field. It is one-dimensional over $\mathbb{R}$, it is the image of an idempotent, and it is the module of the projection $Q\mapsto Q_+$. The theory of the ring is the theory of these modules: what the Peirce decomposition does to the algebra, the same decomposition does to the modules.

## Summary

The split-complex ring is $\mathbb{R}\times\mathbb{R}$, and a finitely generated module over it is a pair of real vector spaces with the diagonal action. The classification is by the pair of dimensions, the two simple modules are $S_+=\mathbb{R}\Pi_+$ and $S_-=\mathbb{R}\Pi_-$, and the regular module is their direct sum.

$S_+$ is projective and not free: it is a direct summand of the free module of rank one, and its real dimension one is not twice a rank. Every module is projective and injective, the ring is semisimple, and the exchange property of bases fails while the Jordan-Hölder theorem holds.

The linear algebra that carries over is the linear algebra of pairs: matrices are pairs of real matrices, kernels and images are componentwise, and injectivity, surjectivity and bijectivity agree for endomorphisms. What does not carry over is the single dimension, the freeness of submodules and the free generation of every module. Over a field there is one simple module and every module is free; here there are two and freeness is a special case of projectivity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_\pm=\tfrac12(1\pm j)$ | The two orthogonal idempotents |
| $\mathbb{C}_{\mathrm{spl}}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ | The decomposition of the ring |
| $S_\pm=\mathbb{R}\Pi_\pm$ | The two simple modules |
| $(V_+,V_-)$ | A finitely generated module, a pair of real spaces |
| $(\dim V_+,\dim V_-)$ | The rank pair, the complete invariant |
| $Q\cdot(x_+,x_-)=(Q_+x_+,Q_-x_-)$ | The action, diagonal |
| $\mathrm{rank}(n,n)$ | The free modules |
| $\mathrm{projective}$ | All modules, by semisimplicity |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, Graduate Texts in Mathematics 13, 2nd ed. 1992), for semisimple rings, projective modules and the Peirce decomposition.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for the structure of semisimple rings and their simple modules.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the Peirce decomposition and the modules over a product of algebras.
- N. Bourbaki, *Algebra I*, Chapters 1-3 (Springer, 1989), for modules, free modules and the failure of the exchange property over a general ring.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, Universitext, 2nd ed. 2009), for projective and injective modules and the exactness of the componentwise constructions.
