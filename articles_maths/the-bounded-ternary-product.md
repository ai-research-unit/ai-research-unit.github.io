# __The Bounded Ternary Product__

## Introduction

The failure of associativity of a sesquilinear product forces a third operation, the ternary product $\{x,y,z\} = (x \star y) \star z^{*}$, which in the standard example of an involutive algebra with the derived operation is $xy^{*}z$. This article reads that operation with a topology on the module. It shows that the ternary product is a bounded trilinear map, conjugate-linear in the middle variable and linear in the outer ones, with the norm of the product at most one, $\lVert\{x,y,z\}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$; that the pair operators $\Theta_{x,y}(z) = \{x,y,z\}$ are bounded with $\lVert\Theta_{x,y}\rVert \leq \lVert x\rVert\lVert y\rVert$ and form a bounded Lie triple system under the commutator; and that the completion of a normed sesqualgebra is a Banach $J^{*}$-triple, the triple product extending by continuity and the Jordan triple identity being preserved because both sides are continuous.

Three facts organise the article. The ternary product is bounded by one constant, the product of the three norms, and this single inequality is what makes the operation an object of the normed theory: it is the definition of a bounded triple product, and every estimate of the article is read from it. The pair operators are the ternary product with two slots promoted to parameters, they are the bounded operators that the algebraic layer of *The Ternary Product as an Operator* attaches to the pairs, and their commutators reproduce the Lie triple system of the sesqualgebra with each bracket bounded. And the completion inherits everything: the extended product and involution define an extended ternary product, the bound survives, and the Jordan triple identity survives because it is an identity between continuous functions on a dense subspace, which is the sense in which the $J^{*}$-structure of a sesqualgebra is a topological object and not only an algebraic one.

The article defines the ternary product and its parity and proves the bound, treats the pair operators and their three readings and their brackets, defines the bounded triple product and reads the completion, and works the examples. The algebraic ternary product, its parity, its Hermitian symmetry and its Jordan triple identity are *The Sesquilinear Associator and the Ternary Product*; the pair operators, their factorisation and their Lie triple system are *The Ternary Product as an Operator*; the completion and the extension of the product and the involution are *The Completion of a Sesqualgebra*; the algebraic $J^{*}$-structure is *Algebraic J\*-Algebras*; and the completed form is *The Topological J\*-Algebra*. Throughout $(\mathbb{K},\varsigma)$ is $\mathbb{R}$ or $\mathbb{C}$ with its continuous involution, $A$ is the standard example of the layer, an associative algebra with an isometric $\varsigma$-semilinear involution carrying the derived product $x \star y = xy^{*}$, normed submultiplicatively, complete where a Banach statement is made, and unital where the binary product is recovered from the ternary one.

## The Ternary Product and its Bound

### The Definition and the Parity

**Definition.** The **ternary product** attached to the sesquilinear product is

$$
\{x,y,z\} = (x \star y) \star z^{*} ,
$$

and in the standard example of a unital involutive algebra with the derived operation $x \star y = xy^{*}$ it is $\{x,y,z\} = xy^{*}z$.

**Proposition (the parities).** The ternary product is additive in each variable, $\mathbb{K}$-linear in the first and the third variables and $\varsigma$-semilinear in the middle:

$$
\{\lambda x, y, z\} = \lambda\{x,y,z\} , \qquad \{x, \lambda y, z\} = \varsigma(\lambda)\{x,y,z\} , \qquad \{x, y, \lambda z\} = \lambda\{x,y,z\} ,
$$

and it satisfies the Hermitian symmetry $\{x,y,z\}^{*} = \{z^{*},y^{*},x^{*}\}$.

*Proof.* The parities are those of *The Sesquilinear Associator and the Ternary Product*, §*Definition and Parity*; the middle slot is the one carrying the involution, and the two outer slots are the linear slots that flank it. Read as a map $A \times A^{\varsigma} \times A \to A$ the ternary product is $R$-trilinear. $\square$

### The Trilinear Bound

**Theorem (the ternary product is bounded).** Let $A$ be a normed sesqualgebra with submultiplicative norm and isometric involution. Then for all $x,y,z$,

$$
\lVert\{x,y,z\}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert ,
$$

and $\{x,y,z\}$ is continuous as a map $A \times A \times A \to A$ for the product topology.

*Proof.* By the definition and the submultiplicative estimate, $\lVert(x \star y) \star z^{*}\rVert \leq \lVert x \star y\rVert\lVert z^{*}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$, the last step by the isometry of the involution. A trilinear map bounded by a constant is continuous. $\square$

**Corollary (the triple product is a bounded trilinear form).** The ternary product factors through the projective tensor product,

$$
A \times A \times A \xrightarrow{\ \ } A \widehat{\otimes}_{\pi} A \widehat{\otimes}_{\pi} A \xrightarrow{\ T\ } A ,
$$

with $\lVert T\rVert \leq 1$, and the norm of the ternary product, $\sup\{\lVert\{x,y,z\}\rVert : \lVert x\rVert,\lVert y\rVert,\lVert z\rVert \leq 1\}$, is at most one.

*Proof.* The product is trilinear on the three modules $A$, $A^{\varsigma}$ and $A$, so it factors through the tensor product by the universal property of *Topological Tensor Products of Sesqualgebras*, §*The Projective Topology*; the bound is the theorem. $\square$

## The Pair Operators

### The Operator of a Pair

**Definition.** For $x,y \in A$ the **pair operator** is

$$
\Theta_{x,y} : A \to A , \qquad \Theta_{x,y}(z) = \{x,y,z\} .
$$

**Proposition (boundedness and the three readings).** The pair operator is $\mathbb{K}$-linear, bounded, and

$$
\lVert\Theta_{x,y}\rVert \leq \lVert x\rVert\lVert y\rVert , \qquad \Theta_{x,y} = T_{x \star y,\,1} , \qquad \Theta_{x,y}(z) = S_{x,z}(y) = T_{1,\,y^{*}z}(x) .
$$

The pair map $(x,y) \mapsto \Theta_{x,y}$ is a bounded bilinear map $A \times A^{\varsigma} \to B(A)$ of norm at most one.

*Proof.* Linearity in $z$ is the parity of the third slot; the bound is the trilinear bound read with $z$ as the variable; the three readings are the theorem of *The Ternary Product as an Operator*, §*The Three Readings*: the pair operator is the ordinary left multiplication by the derived product, $\Theta_{x,y} = T_{x \star y,1}$, and it is also the sandwich $S_{x,z}$ read in the middle slot and the right multiplication $T_{1,y^{*}z}$ read in the first. Bilinearity of the pair map is the parity of the two parameters, read on $A \times A^{\varsigma}$. $\square$

**Corollary (the middle reading is a sandwich).** With the first and the third slots fixed, the map $y \mapsto x\,y^{*}\,z$ is the sandwich $S_{x,z}$ of *The Bounded Sesquilinear Sandwich*, so the pair operator and the sandwich are the two readings of the same trilinear object, one with the middle slot promoted and one with the outer slots promoted.

*Proof.* $\{x,y,z\} = x y^{*} z = S_{x,z}(y)$, which is the corollary of *The Ternary Product as an Operator*, §*The Three Readings*. $\square$

### The Lie Triple System

**Theorem (the pair operators under the commutator).** For all $x,y,u,v,p,q$,

$$
[\Theta_{x,y}, \Theta_{u,v}] = T_{[x \star y,\,u \star v],\,1} , \qquad [[\Theta_{x,y},\Theta_{u,v}],\Theta_{p,q}] = T_{[[x \star y,\,u \star v],\,p \star q],\,1} ,
$$

where the brackets in the right-hand members are the commutators of the envelope. The operators $\Theta$ form a bounded Lie triple system: the bracket is bounded with $\lVert[\Theta_{x,y},\Theta_{u,v}]\rVert \leq 2\lVert x\rVert\lVert y\rVert\lVert u\rVert\lVert v\rVert$, and the triple commutator is again a left multiplication of the same shape, $T_{b,1}$ with $b = [[x \star y, u \star v], p \star q]$, hence a pair operator $\Theta_{b,1}$ in the unital case, of norm at most $4\lVert x\rVert\lVert y\rVert\lVert u\rVert\lVert v\rVert\lVert p\rVert\lVert q\rVert$.

*Proof.* The two identities are the theorem of *The Ternary Product as an Operator*, §*The Bracket and the Lie Triple System*: with $\Theta_{x,y} = T_{a,1}$ for $a = x \star y$ and $\Theta_{u,v} = T_{c,1}$ for $c = u \star v$ one has $T_{a,1}T_{c,1} = T_{ac,1}$, so the commutator is $T_{ac-ca,1}$, and the second identity is the first applied twice. The bounds follow from $\lVert T_{b,1}\rVert \leq \lVert b\rVert$, from $\lVert[b,c]\rVert \leq 2\lVert b\rVert\lVert c\rVert$ and from the bound of the pair operator. $\square$

**Proposition (the Lie companion).** For $x,y$ let

$$
\delta_{x,y} = \mathrm{ad}_{[x,y]} , \qquad \delta_{x,y}(z) = [[x,y],z] ,
$$

the bracket in $[x,y] = xy - yx$ being the commutator of the envelope. Then $\delta_{x,y}$ is a bounded derivation of the envelope, $\lVert\delta_{x,y}\rVert \leq 4\lVert x\rVert\lVert y\rVert$, and the family of the pairs is the family of the inner derivations of the commutator Lie algebra, which is the bounded form of *The Ternary Product as an Operator*, §*The Inner Derivation of a Pair*.

*Proof.* The element $[x,y]$ has norm at most $2\lVert x\rVert\lVert y\rVert$, and $\mathrm{ad}_a = T_{a,1} - T_{1,a}$ is bounded with norm at most $2\lVert a\rVert$ by *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*, §*The Adjoint Action* read in the ordinary product; the composition gives the bound. It is an inner derivation by the Leibniz rule. $\square$

## The Bounded Triple Product and the Completion

### The Definition of a Bounded Triple Product

**Definition.** Let $X$ be a normed space and let $\{\cdot,\cdot,\cdot\} : X \times X \times X \to X$ be additive in each variable, $\mathbb{K}$-linear in the first and third and $\varsigma$-semilinear in the middle. The triple product is **bounded** if

$$
\lVert\{x,y,z\}\rVert \leq C\lVert x\rVert\lVert y\rVert\lVert z\rVert
$$

for all $x,y,z$ and some $C \geq 0$; the least such $C$ is the **norm** of the triple product, and a normed space with a bounded triple product is a **normed triple system**.

**Theorem (the ternary product of a sesqualgebra is a bounded triple product).** Let $A$ be a normed sesqualgebra with submultiplicative norm and isometric involution. Then the ternary product is bounded with $C = 1$, so $A$ is a normed triple system with $\lVert\{\cdot,\cdot,\cdot\}\rVert \leq 1$.

*Proof.* This is the trilinear bound. $\square$

### The Completion

**Theorem (the completion is a Banach triple system).** Let $A$ be a normed sesqualgebra and let $\widehat{A}$ be its completion. Then the product and the involution extend uniquely to $\widehat{A}$, the extended ternary product $\{x,y,z\} = (x \star y) \star z^{*}$ is defined on $\widehat{A}$ and is bounded with the same constant, and $\widehat{A}$ is a Banach triple system in which $A$ is dense.

*Proof.* The product extends to a bounded bilinear map on the completion and the involution to an isometric involution by *The Completion of a Sesqualgebra*, §*The Product on the Completion* and §*The Extension of the Involution*, and the extended derived operation is the extension of the derived operation by §*The Derived Operation*. The composite of three bounded maps is bounded with the product of the constants, so the ternary product is bounded with constant one, and the completion is complete. $\square$

### The Preservation of the Jordan Triple Identity

**Theorem (the identity survives the completion).** The ternary product of $\widehat{A}$ satisfies the Jordan triple identity

$$
\{x, y, \{u, v, w\}\} = \{\{x, y, u\}, v, w\} - \{u, \{y, x, v\}, w\} + \{u, v, \{x, y, w\}\} ,
$$

so the completion of a normed sesqualgebra is a Banach $J^{*}$-triple.

*Proof.* Both sides are obtained from the extended product and involution by composition of bounded multilinear maps, hence are continuous functions of $(x,y,u,v,w)$; they agree on the dense subset $A^{5}$ by the Jordan triple identity of *The Sesquilinear Associator and the Ternary Product*, §*The Jordan Triple Identity*; and a continuous function vanishing on a dense subset vanishes everywhere in a Hausdorff space. $\square$

**Remark.** The preservation is the first place where the topological layer proves something the algebraic layer cannot even state: the identity is a polynomial identity of the algebraic object and is inherited by the completion, so the class of the $J^{*}$-triples is closed under completion. The same argument gives the bound of the pair operators on the completion and the closure of the Lie triple system, and it is the standard device for passing from a dense subalgebra to a complete one.

## The Normed J*-Triple and the Passage to the J*-Algebra

### The Normed J*-Triple

**Definition.** A **normed $J^{*}$-triple** is a normed space with a bounded triple product that is conjugate-linear in the middle and linear in the outer variables and satisfies the Jordan triple identity; a **Banach $J^{*}$-triple** is a complete normed $J^{*}$-triple. A **normed $J^{*}$-algebra** is a normed $J^{*}$-triple with a unit and a binary product recovered by $xy = \{x, y^{*}, 1\}$.

**Theorem (the sesqualgebra is a normed $J^{*}$-triple).** The standard example of a normed sesqualgebra is a normed $J^{*}$-triple, and its completion is a Banach $J^{*}$-triple; the pair operators are its bounded operators, the sandwich is its middle reading, and the triple system of the pairs is its Lie triple system.

*Proof.* The parities and the Hermitian symmetry are the proposition of §*The Definition and the Parity*, the bound is §*The Trilinear Bound*, the identity is §*The Preservation of the Jordan Triple Identity* on the completion, and the identifications are the corollaries above. $\square$

### The Passage to the J*-Algebra

**Theorem (the passage to the normed $J^{*}$-algebra).** Let $A$ be a unital normed sesqualgebra with submultiplicative norm and isometric involution. Then the ternary product determines the binary product and the involution through

$$
\{x,y,1\} = x \star y , \qquad \{1,y,1\} = y^{*} ,
$$

and on the completion $\widehat{A}$ the triple product, the binary product and the involution form a normed $J^{*}$-algebra with unit, whose norm satisfies $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$ on the binary product and $\lVert\{x,y,z\}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$ on the ternary one.

*Proof.* The two identities are those of *The Sesquilinear Associator and the Ternary Product*, §*The Passage from the Binary to the Ternary Product*, and they express the binary product as the ternary product with the unit in the third slot; the norm inequalities are the submultiplicative estimate on the completed product and the trilinear bound on the completed triple product. The completed object is the normed $J^{*}$-algebra of *The Topological J\*-Algebra*. $\square$

**Remark.** The passage is the passage from the operation with an uncontrolled associator to the operation with a controlled identity: the binary product carries at most the submultiplicative inequality, while the ternary product carries the Jordan triple identity and determines the binary product. The topological layer states this as the closure of the classes under completion, and it is the reason the ternary product, and not the binary one, is the operation whose bounded operators the next articles of the category study.

## Examples

### The Matrices

**Example (the matrices, verdict: the triple product is bounded by one).** Let $A = M_{n}(\mathbb{C})$ with the operator norm, the conjugation and the product $X \star Y = XY^{*}$. The ternary product is $\{X,Y,Z\} = XY^{*}Z$, bounded with $\lVert\{X,Y,Z\}\rVert \leq \lVert X\rVert\lVert Y\rVert\lVert Z\rVert$; the pair operator is $\Theta_{X,Y}(Z) = XY^{*}Z$, bounded with $\lVert\Theta_{X,Y}\rVert \leq \lVert X\rVert\lVert Y\rVert$; and the completion is $A$ itself, the algebra being finite-dimensional, so the Banach $J^{*}$-triple of the example is the whole matrix algebra with the triple product.

### The Field

**Example (the field, verdict: a one-dimensional triple system).** Let $A = \mathbb{C}$ with the modulus, the conjugation and the product $x \star y = x\bar y$. The ternary product is $\{x,y,z\} = x\bar y z$ with $\lvert\{x,y,z\}\rvert = \lvert x\rvert\lvert y\rvert\lvert z\rvert$, so the bound is attained and the norm of the triple product is exactly one; the pair operator is $\Theta_{x,y}(z) = x\bar y z$, of norm $\lvert x\rvert\lvert y\rvert$, and the Lie triple system of the pairs is abelian, since the field is commutative.

### The Sequences

**Example (the sequences, verdict: the completion is the Banach triple system).** Let $A = c_{00}$ be the space of finitely supported sequences with the $\ell^{1}$-norm, the termwise conjugation and the termwise product. The ternary product is the termwise map $(x,y,z) \mapsto (x_{k}\bar y_{k}z_{k})$, bounded with constant one, and the completion is $\ell^{1}$ with the extended termwise triple product; the Jordan triple identity is inherited by the completion by §*The Preservation of the Jordan Triple Identity*, and the result is a Banach $J^{*}$-triple with a dense finitely supported $J^{*}$-subtriple.

## Summary

The ternary product of a sesquilinear product is $\{x,y,z\} = (x \star y) \star z^{*}$, linear in the two outer variables and conjugate-linear in the middle, and on a normed sesqualgebra with submultiplicative norm and isometric involution it is bounded with the constant one, $\lVert\{x,y,z\}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$, so the object is a normed triple system and the product factors through the projective tensor product with a linear map of norm at most one. The pair operators $\Theta_{x,y}(z) = \{x,y,z\}$ are bounded with $\lVert\Theta_{x,y}\rVert \leq \lVert x\rVert\lVert y\rVert$, they are the left multiplications by the derived products, their middle reading is the sandwich $S_{x,z}$, the pair map is bounded bilinear on $A \times A^{\varsigma}$, and the pair operators form a bounded Lie triple system under the commutator with the Lie companion $\delta_{x,y} = \mathrm{ad}_{[x,y]}$ the bounded inner derivation of the pair. The completion $\widehat{A}$ carries the extended product, involution and triple product, the bound survives, and the Jordan triple identity survives because both of its sides are continuous and agree on the dense subset, so the completion of a normed sesqualgebra is a Banach $J^{*}$-triple. In the unital case the ternary product determines the binary product and the involution, $\{x,y,1\} = x \star y$ and $\{1,y,1\} = y^{*}$, and the completed object is the normed $J^{*}$-algebra of *The Topological J\*-Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\{x,y,z\} = (x \star y) \star z^{*} = xy^{*}z$ | the ternary product |
| $\lVert\{x,y,z\}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$ | the bound with constant one |
| $A \widehat{\otimes}_{\pi} A \widehat{\otimes}_{\pi} A \to A$ | the factorisation of the triple product |
| $\Theta_{x,y}(z) = \{x,y,z\}$ | the pair operator, linear and bounded |
| $\lVert\Theta_{x,y}\rVert \leq \lVert x\rVert\lVert y\rVert$ | the bound of the pair operator |
| $\Theta_{x,y}(z) = x\,y^{*}\,z = S_{x,z}(y)$ | the pair operator as a left multiplication and as a sandwich |
| $[\Theta_{x,y},\Theta_{u,v}]$ | the bracket of the pair operators, a Lie triple system |
| $\delta_{x,y} = \mathrm{ad}_{[x,y]}$ | the Lie companion, a bounded inner derivation |
| $\lVert\{x,y,z\}\rVert \leq C\lVert x\rVert\lVert y\rVert\lVert z\rVert$ | the defining inequality of a bounded triple product |
| $\widehat{A}$ | the completion, a Banach $J^{*}$-triple |
| $\{x,y,1\} = x \star y$, $\{1,y,1\} = y^{*}$ | the passage from the ternary to the binary product |

## Further Reading

- Lawrence A. Harris, *Bounded Symmetric Domains in Infinite-Dimensional Banach Spaces* (Lecture Notes in Mathematics 364, Springer, 1974), for the $J^{*}$-triples, their triple products and the norms that define them.
- Harald Upmeier, *Symmetric Banach Manifolds and Jordan $\mathrm{C}^{*}$-Algebras* (North-Holland, 1985), for the bounded triple products of a Banach space and the operator theory they carry.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the triple systems and the identities preserved under completion.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the Jordan triple identity as the defining axiom and its stability under completion.
- The companion articles of this series: *The Sesquilinear Associator and the Ternary Product*, *The Ternary Product as an Operator*, *The Completion of a Sesqualgebra*, *Algebraic J\*-Algebras* and *The Topological J\*-Algebra*.
