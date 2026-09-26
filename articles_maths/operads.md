
# __Operads__

## Introduction

An operad is the algebraic structure that governs operations of several variables and their compositions. A single associative algebra has a binary product and the product is associative; a Lie algebra has a bracket and the bracket satisfies the Jacobi identity; a commutative algebra has a commutative and associative product. In each case the operations and their relations are the same for every algebra of the species, and an operad is the object that records them: it consists of a module of $n$-ary operations for each $n$, an action of the symmetric group permuting the arguments, a unit, and composition maps that substitute operations into one another. An algebra over an operad is then an object on which the operations act, and the theorems of the subject describe the resulting species of algebras, their free objects, their homology and their deformation theory.

This article develops symmetric sequences and the substitution product, the definition of an operad and of an algebra over it, the free operad and the operads of the fundamental species, modules and the bar and cobar constructions, the Koszul duality of operads with the associative and Poisson examples, and the relation to the Hochschild and deformation theories of the previous articles. It follows *Hochschild Homology*, *Cyclic Homology*, *Deformation Theory*, and it prepares the representation-theoretic articles of the category.

Two boundaries are fixed. The **homotopy-theoretic side** of the theory — the model category of operads, the cofibrant replacements, the homotopy coherent structures and the higher algebra of $\infty$-operads — belongs to Part II, where it is treated in ; this article works with the strict algebraic objects and cites those articles for the homotopy theory. The **topological side** — the little discs operads, the recognition principles and the operads of loop spaces — is likewise Part II's, and the little intervals and little discs operads are named only where the algebra requires them. Throughout, $k$ is a commutative ring with $1\neq0$, modules are $k$-modules, and the symmetric groups act from the right unless stated.

## Symmetric Sequences and the Substitution Product

### Symmetric Sequences

**Definition.** A **symmetric sequence** (or $\Sigma$-module) is a collection $M=\{M(n)\}_{n\ge0}$ of $k$-modules, each equipped with a right action of the symmetric group $\Sigma_n$, with $M(0)$ a module for the trivial group. A **morphism** of symmetric sequences is a collection of $\Sigma_n$-equivariant maps. The **degreewise tensor product** and the **direct sum** are defined componentwise, and the category of symmetric sequences is abelian.

**Definition.** The **substitution product** (or composition product) $M\circ N$ of two symmetric sequences is the symmetric sequence with

$$
(M\circ N)(n)=\bigoplus_{p\ge0}M(p)\otimes_{\Sigma_p}\Bigl(\bigoplus_{n_1+\cdots+n_p=n}\operatorname{Ind}_{\Sigma_{n_1}\times\cdots\times\Sigma_{n_p}}^{\Sigma_n}N(n_1)\otimes\cdots\otimes N(n_p)\Bigr),
$$

where the outer tensor product is the coinvariant quotient of the diagonal action and the inner sum runs over the compositions of $n$.

**Proposition.** The substitution product is associative up to the canonical isomorphisms and has the unit $I$ with $I(1)=k$ and $I(n)=0$ for $n\neq1$; hence the category of symmetric sequences is a monoidal category under $\circ$, with the symmetric sequence $I$ as unit.

*Proof.* The associativity is the identification of two ways of nesting the sums over compositions of $n$; each corresponds to a planar forest with $n$ leaves and internal vertices labelled by the components of the sequences, and the two nestings give the same forest. The unit axioms follow from $\Sigma_1$ being trivial and from $N(0)$ occurring only in the positions fixed by the composition. $\square$

**Example.** If $M$ is concentrated in degree $0$ with $M(0)=k$ and $N$ is arbitrary, then $(M\circ N)(0)=k$ and $(M\circ N)(n)=0$ for $n\ge1$, so $M$ is a left zero for the composition on the positive degrees.

### Operads

**Definition.** An **operad** $\mathcal{O}$ is a monoid in the monoidal category of symmetric sequences, that is, a symmetric sequence with morphisms $\gamma:\mathcal{O}\circ\mathcal{O}\to\mathcal{O}$ and $\eta:I\to\mathcal{O}$ satisfying the associativity and unit axioms. Explicitly, for each $n$ and each composition $n=n_1+\cdots+n_p$ there are **composition maps**

$$
\gamma:\mathcal{O}(p)\otimes\mathcal{O}(n_1)\otimes\cdots\otimes\mathcal{O}(n_p)\to\mathcal{O}(n),
$$

equivariant for the symmetric groups, together with a **unit** $1\in\mathcal{O}(1)$, and the compositions are associative and unital in the evident sense. An operad is **augmented** if it carries a morphism $\mathcal{O}\to I$ of operads, that is, a splitting of the unit. Without the $\Sigma_n$-actions the same data define a **non-symmetric operad**.

**Example.** The **endomorphism operad** $\operatorname{End}_V$ of a $k$-module $V$ has $\operatorname{End}_V(n)=\operatorname{Hom}_k(V^{\otimes n},V)$, with the symmetric group acting by permuting the tensor factors, the unit the identity of $V$, and composition given by substitution of maps. Every operad acts on some modules through a morphism to an endomorphism operad; this is the origin of the definition.

**Example.** The **associative operad** $\mathcal{A}ss$ has $\mathcal{A}ss(n)=k[\Sigma_n]$ the regular representation, with composition induced by the block inclusions of symmetric groups. The **commutative operad** $\mathcal{C}om$ has $\mathcal{C}om(n)=k$ with the trivial action. The **Lie operad** $\mathcal{L}ie$ has $\mathcal{L}ie(n)$ the $k$-module with basis the left-normed bracket monomials modulo the Jacobi and antisymmetry relations, of rank $(n-1)!$ over a field; it is the operad whose algebras are the Lie algebras. The **Poisson operad** $\mathcal{P}ois$ is generated by a commutative product in arity two and a bracket in arity two subject to the associativity, commutativity, Jacobi and Leibniz relations.

**Definition.** A **morphism of operads** $\mathcal{O}\to\mathcal{O}'$ is a morphism of monoids in symmetric sequences, that is, a collection of $\Sigma_n$-equivariant maps compatible with composition and unit.

**Definition.** An **algebra over an operad** $\mathcal{O}$, or $\mathcal{O}$-algebra, is a $k$-module $A$ together with a morphism of operads $\mathcal{O}\to\operatorname{End}_A$. Equivalently, it is a $k$-module with maps $\mathcal{O}(n)\otimes_{\Sigma_n}A^{\otimes n}\to A$ for all $n$ that are compatible with the composition and unit of $\mathcal{O}$. The **free $\mathcal{O}$-algebra** on a module $V$ is $\mathcal{O}(V)=\bigoplus_n\mathcal{O}(n)\otimes_{\Sigma_n}V^{\otimes n}$, with the action induced by the composition.

**Theorem (the species of algebras).** An algebra over $\mathcal{A}ss$ is an associative $k$-algebra; an algebra over $\mathcal{C}om$ is a commutative associative $k$-algebra; an algebra over $\mathcal{L}ie$ is a Lie $k$-algebra; an algebra over $\mathcal{P}ois$ is a Poisson $k$-algebra. The free algebra statements are the corresponding free objects: $\mathcal{A}ss(V)$ is the tensor algebra $T(V)$, $\mathcal{C}om(V)$ is the symmetric algebra $S(V)$, and $\mathcal{L}ie(V)$ is the free Lie algebra.

*Proof.* A morphism $\mathcal{A}ss\to\operatorname{End}_A$ assembles the $\Sigma_n$-equivariant maps $k[\Sigma_n]\to\operatorname{Hom}_k(A^{\otimes n},A)$, and the equivariance forces the value on the identity permutation to determine all the others; the value on a transposition in arity two is a binary product, and the composition axiom in $\mathcal{A}ss$ is exactly associativity. The cases of $\mathcal{C}om$ and $\mathcal{L}ie$ are the same computation with the quotient relations imposed on arity two, which are commutativity and antisymmetry with the Jacobi identity. The identifications of the free algebras follow from the definition of the free $\mathcal{O}$-algebra and the known descriptions of $T(V)$, $S(V)$ and the free Lie algebra. $\square$

**Example.** For a one-dimensional $k$-module $V$ the free associative algebra $T(V)$ and the free commutative algebra $S(V)$ both identify with the polynomial algebra $k[x]$; the free objects differ as soon as $V$ has dimension at least two, where $T(V)$ is the noncommutative polynomial algebra and $S(V)$ is its commutative quotient.

## The Free Operad and Modules

### The Free Operad

**Definition.** The **free operad** $\mathcal{F}(M)$ on a symmetric sequence $M$ is the operad with

$$
\mathcal{F}(M)(n)=\bigoplus_{\text{planar trees }T\text{ with }n\text{ leaves}}\ \bigotimes_{\text{vertices }v\text{ of }T}M(\operatorname{in}(v)),
$$

where the sum runs over the isomorphism classes of planar trees and the symmetric groups act by permuting the leaves. It is the left adjoint to the forgetful functor from operads to symmetric sequences.

**Proposition.** The free operad is the free monoid on $M$ in the monoidal category of symmetric sequences: $\mathcal{F}(M)=\bigoplus_{j\ge0}M^{\circ j}$, where $M^{\circ j}$ is the $j$-fold substitution product, and the components are the trees with $j$ internal vertices.

*Proof.* The monoidal structure on symmetric sequences computed above identifies the iterated substitution with the sum over planar forests; a forest with $j$ internal vertices is a tree of trees, and the leaves are the inputs. The unit and associativity axioms of the free monoid are then automatic, and the universal property is the universal property of the free monoid. $\square$

**Example.** If $M$ is concentrated in arity two, $M(2)=k$ with the trivial action and $M(n)=0$ otherwise, then $\mathcal{F}(M)(n)$ has dimension the Catalan number $\frac{1}{n}\binom{2n-2}{n-1}$ when $k$ is a field of characteristic zero, one basis element for each binary tree with $n$ leaves: $1,1,2,5,14$ for $n=1,\dots,5$.

### Modules over an Operad

**Definition.** A **module** over an operad $\mathcal{O}$ is a symmetric sequence $M$ with an action of the monoid $\mathcal{O}$, that is, morphisms $\mathcal{O}\circ M\to M$ and $M\circ\mathcal{O}\to M$ satisfying the associativity and unit axioms; a **left module** uses only the first and a **right module** only the second. The **generating function** of an operad is the formal power series $\sum_{n\ge0}\dim_k\mathcal{O}(n)\,t^n/n!$ when the dimensions are finite.

**Theorem (generating function of the free operad).** Let $M$ be a symmetric sequence with $M(0)=M(1)=0$ and finite-dimensional components, and let

$$
G(u)=\sum_{n\ge1}\dim_k\mathcal{F}(M)(n)\,u^n
$$

be the ordinary generating function of the free operad. Then $G$ satisfies the functional equation

$$
G(u)=u+\sum_{p\ge2}\dim_kM(p)\,G(u)^p,
$$

the term of arity $p$ recording a root operation of arity $p$ with its $p$ subtrees. If $M$ is concentrated in arity two with $\dim_kM(2)=1$, this is $G=u+G^2$, so

$$
G(u)=\frac{1-\sqrt{1-4u}}{2}=\sum_{n\ge1}C_{n-1}u^n, \qquad C_{n-1}=\frac{1}{n}\binom{2n-2}{n-1},
$$

and the dimensions of the components are the Catalan numbers $1,1,2,5,14$ for $n=1,\dots,5$. The functional equation is a relation between **ordinary** generating functions, because the planar decomposition orders the $p$ subtrees at a vertex; passing to the exponential generating function $F(u)=\sum_n\dim_k\mathcal{F}(M)(n)\,u^n/n!$ therefore does not amount to replacing $\dim_kM(p)$ by $\dim_kM(p)/p!$. In the binary case

$$
F(u)=\sum_{n\ge1}C_{n-1}\frac{u^n}{n!}=u+\frac{u^2}{2}+\frac{u^3}{3}+\frac{5u^4}{24}+\cdots,
$$

which is not the solution $1-\sqrt{1-2u}$ of the substitution equation $F=u+\tfrac12F^2$: that solution has coefficients $u+\frac12u^2+\frac12u^3+\frac58u^4+\cdots$, with $n!$-multiples $1,1,3,15,\dots$, the odd double factorials, and not the Catalan dimensions of the free operad.

*Proof.* A tree of the free operad has a root operation of some arity $p$, and the $p$ subtrees hanging from it are themselves trees; grouping by the root gives the functional equation, each vertex contributing its dimension and each arity $p$ vertex attached to $p$ subtrees. For the binary case $G=u+G^2$ is the defining equation of the Catalan numbers, whose explicit form is the standard solution by the quadratic formula and by the Lagrange inversion. The subtrees at a vertex are ordered in this decomposition, so each arity-$p$ vertex contributes $\dim_kM(p)$ and no factor $1/p!$ is present; the components are spanned by planar trees, whose leaves carry the symmetric-group action, and it is the ordinary generating function that the tree decomposition computes. $\square$

**Example.** For $\mathcal{A}ss$ the generating function is $\sum_{n\ge0}n!\,t^n/n!=\frac{1}{1-t}$, and for $\mathcal{C}om$ it is $\sum_{n\ge0}t^n/n!=e^t$, reflecting the fact that $\mathcal{A}ss(n)=k[\Sigma_n]$ has dimension $n!$ while $\mathcal{C}om(n)=k$ has dimension $1$.

## Bar and Cobar Constructions

### The Bar Construction

**Definition.** Let $\mathcal{O}$ be an augmented operad with augmentation ideal $\bar{\mathcal{O}}$, and let $\mathcal{O}^{!}$ be the **Koszul dual**, the operad with the same arity-two generating operations dualised and with relations the annihilators of the relations of $\mathcal{O}$. The **bar construction** $B\mathcal{O}$ is the symmetric sequence with
$$
B\mathcal{O}(n)=\bigoplus_{j\ge1}\ \bigoplus_{\text{trees with }n\text{ leaves and }j\text{ internal vertices}}\bigotimes_{v}\bar{\mathcal{O}}(\operatorname{in}(v)),
$$
with the signs of the tree differential, and the **cobar construction** $\Omega(M)$ on a symmetric sequence $M$ is the free operad with a differential, $\Omega(M)=(\mathcal{F}(M),d)$, where $d$ contracts the edges of the trees. The bar and cobar constructions are adjoint, and for an operad $\mathcal{O}$ the **operadic homology** of an $\mathcal{O}$-algebra $A$ is
$$
H^{\mathcal{O}}_{\bullet}(A)=\operatorname{Tor}^{\mathcal{O}}_{\bullet}(k,A),
$$
computed by the bar resolution of $k$ over $\mathcal{O}$.

**Theorem (Koszul duality).** There is a duality $\mathcal{O}\mapsto\mathcal{O}^{!}$ on augmented operads generated by operations in arity two, with $\mathcal{O}^{!}(n)$ the linear dual of a suitable space of indecomposables, such that:
- $\mathcal{A}ss^{!}=\mathcal{A}ss$, $\mathcal{C}om^{!}=\mathcal{L}ie$ and $\mathcal{L}ie^{!}=\mathcal{C}om$, with the Lie operad dualised up to the suspension of the bracket;
- $\mathcal{O}$ is **Koszul** if the natural map $\Omega(\mathcal{O}^{!})\to\mathcal{O}$ is a quasi-isomorphism, equivalently if the bar construction $B\mathcal{O}$ has homology concentrated in the **weight** degree $n$, where the weight of a tree is its number of internal vertices;
- if $\mathcal{O}$ is Koszul then for every $\mathcal{O}$-algebra $A$ the operadic homology $H^{\mathcal{O}}_{\bullet}(A)$ can be computed by the **Koszul complex** $A\otimes\mathcal{O}^{!\,\vee}$, the dual of the Koszul dual, and the two spectral sequences of the bicomplex converge to the same answer.

*Proof (in outline).* The duality is defined by linear algebra on the space of generating operations, and the identifications $\mathcal{C}om^{!}=\mathcal{L}ie$ and $\mathcal{L}ie^{!}=\mathcal{C}om$ are the classical statement that the Lie operad is the Koszul dual of the commutative one, computed by comparing the generating functions of the two operads, which are related by the Koszul inversion. The Koszul criterion and the Koszul complex are proved by comparing the bar construction with the cobar construction; the weight filtration gives the two spectral sequences, and their degeneracy at the $E^1$-term is the Koszul condition. $\square$

**Example.** The associative operad is Koszul, and $H^{\mathcal{A}ss}_{\bullet}(A)=HH_{\bullet}(A,A)$ is the Hochschild homology of *Hochschild Homology*; the commutative operad is Koszul, and $H^{\mathcal{C}om}_{\bullet}(A)$ is the Andr\'e–Quillen homology of the commutative algebra $A$; the Lie operad is Koszul, and $H^{\mathcal{L}ie}_{\bullet}(\mathfrak{g})$ is the Chevalley–Eilenberg homology of the Lie algebra $\mathfrak{g}$ with trivial coefficients.

**Example (Poisson).** The Poisson operad is Koszul over a field of characteristic zero — a standard result, established by comparing the generating functions of the Poisson and Gerstenhaber operads — and the operadic homology of a Poisson algebra is computed by the corresponding Koszul complex. This is the algebraic input to the formality and deformation statements of *Deformation Theory*.

### Operads and Deformation Theory

**Theorem.** Let $\mathcal{O}$ be an operad and $A$ an $\mathcal{O}$-algebra. Then the deformation theory of $A$ as an $\mathcal{O}$-algebra is controlled by the **operadic cohomology** $\operatorname{Ext}^{\bullet}_{\mathcal{O}}(A,A)$, which is the $\mathcal{O}$-analogue of the Hochschild cohomology; for $\mathcal{O}=\mathcal{A}ss$ it is the Hochschild cohomology of *Hochschild Homology*, and the Maurer–Cartan and obstruction formalism of *Deformation Theory* applies verbatim with the differential graded Lie algebra of $\mathcal{O}$-cochains.

*Proof (in outline).* The operadic cohomology is the Ext over the operad of the algebra with itself, and the deformation functor is the Maurer–Cartan functor of the endomorphism operad; restricting to the arity-two operations recovers the binary operations of the algebra and hence the Hochschild complex in the associative case. The general statement is the same obstruction calculus, with the operadic composition in place of the cup product. $\square$

**Example.** For the commutative operad the operadic cohomology of a commutative algebra is the Andr\'e–Quillen cohomology, and the first-order deformations of the algebra in the commutative world are the square-zero extensions; for a smooth algebra these agree with the Kähler differentials and the exterior powers, which is the algebraic statement used throughout *Deformation Theory*.

## Summary

A symmetric sequence is a graded collection of modules with symmetric-group actions, and the substitution product makes the symmetric sequences into a monoidal category with unit $I$. An operad is a monoid in this category; it consists of $n$-ary operations, a unit in arity one, and composition maps that substitute operations into one another, and its algebras are the modules on which the operations act compatibly. The fundamental examples are the endomorphism operad, the associative operad $\mathcal{A}ss$, the commutative operad $\mathcal{C}om$, the Lie operad $\mathcal{L}ie$ and the Poisson operad, whose algebras are the associative, commutative, Lie and Poisson algebras respectively, with free objects the tensor algebra, the symmetric algebra and the free Lie algebra.

The free operad on a symmetric sequence is the free monoid under substitution, and its components are the planar trees weighted by the sequence; the generating functions satisfy a functional equation solved by the Lagrange inversion, and the specialisations recover the Catalan numbers for a binary generator. Modules over an operad, the bar and cobar constructions, and the Koszul duality give the computation of the operadic homology; the associative, commutative and Lie operads are Koszul, and their homologies are the Hochschild, Andr\'e–Quillen and Chevalley–Eilenberg homologies. For an $\mathcal{O}$-algebra the deformation theory is controlled by the operadic cohomology, which specialises to the Hochschild cohomology of *Hochschild Homology* and to the obstruction calculus of *Deformation Theory*. The homotopy-coherent and model-categorical refinements of all of this belong to Part II andand are cited rather than used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma_n$ | symmetric group on $n$ letters |
| $M(n)$, $\mathcal{O}(n)$ | the $n$-ary operations, with right $\Sigma_n$-action |
| $M\circ N$ | substitution product of symmetric sequences |
| $I$ | unit symmetric sequence, $I(1)=k$ |
| $\gamma$, $\eta$ | composition and unit of an operad |
| $\operatorname{End}_V$ | endomorphism operad of a module $V$ |
| $\mathcal{A}ss$, $\mathcal{C}om$, $\mathcal{L}ie$, $\mathcal{P}ois$ | associative, commutative, Lie, Poisson operads |
| $\mathcal{O}(V)$, $\mathcal{F}(M)$ | free algebra, free operad |
| $B\mathcal{O}$, $\Omega(M)$ | bar and cobar constructions |
| $\mathcal{O}^{!}$ | Koszul dual operad |
| $H^{\mathcal{O}}_{\bullet}(A)$ | operadic homology $\operatorname{Tor}^{\mathcal{O}}_{\bullet}(k,A)$ |
| $C_{n-1}=\frac{1}{n}\binom{2n-2}{n-1}$ | Catalan number; the dimension $\dim_k\mathcal{F}(M)(n)$ for a generator concentrated in arity two |
| $G(u)=\sum_n\dim_k\mathcal{F}(M)(n)u^n$ | ordinary generating function of the free operad |
| $F(u)=\sum_n\dim_k\mathcal{F}(M)(n)u^n/n!$ | exponential generating function, the Borel transform of $G$ |
| $\mathfrak{g}$ | a Lie algebra, an algebra for $\mathcal{L}ie$ |



## Further Reading

- J. Michael Boardman and Rainer M. Vogt, *Homotopy Invariant Algebraic Structures on Topological Spaces* (Springer Lecture Notes in Mathematics 347, 1973), for the origin of the operadic axioms and the composition of operations.
- Benoit Fresse, *Modules over Operads and Functors* (Springer Lecture Notes in Mathematics 1964, 2009), for the systematic theory of operadic modules and the bar construction.
- Ezra Getzler and John D. S. Jones, "Operads, homotopy algebra and iterated integrals for double loop spaces", *preprint* (1994), for the operadic bar construction and the algebraic models.
- Victor Ginzburg and Mikhail Kapranov, "Koszul duality for operads", *Duke Mathematical Journal* 76 (1994), 203–272, for the Koszul duality, the Koszul complex and the criterion used here.
- Maxim Kontsevich, "Operads and motives in deformation quantization", *Letters in Mathematical Physics* 48 (1999), 35–72, for the formality and the deformation-theoretic applications.
- Jean-Louis Loday and Bruno Vallette, *Algebraic Operads* (Springer, 2012), for the systematic treatment of symmetric sequences, the free operad and the Koszul duality.
- Peter May, *The Geometry of Iterated Loop Spaces* (Springer Lecture Notes in Mathematics 271, 1972), for the origin of the definition and the operads of loop spaces.
- Martin Markl, Steve Shnider and Jim Stasheff, *Operads in Algebra, Topology and Physics* (American Mathematical Society, 2002), for the survey of the algebraic and homotopical theory.
