# __The Topological J\*-Algebra__

## Introduction

An **algebraic $J^{*}$-algebra** is a module with a ternary product that is additive in each variable, linear in the outer ones and $\varsigma$-semilinear in the middle, and satisfies the Jordan triple identity; the axioms are equational and norm-free, and the binary product is not among them, since the model $\{x,y,z\} = xy^{*}z$ is closed under the triple product while a subspace such as the matrices with zero diagonal is not closed under the product. *The Bounded Ternary Product* reads the same structure with a norm: the triple product of a normed sesquialgebra is bounded with constant one, the Jordan triple identity survives the completion, and the completion of a normed sesquialgebra is a Banach $J^{*}$-triple. This article takes the passage one step further and defines the object in which the triple product *and* the recovered binary product are both present: the **topological $J^{*}$-algebra**.

Three facts organise the article. The inequality $\lVert\{x,y,z\}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$ is the definition of a **normed $J^{*}$-algebra**, and it is not an extra axiom on top of the triple product: it is what makes the object an object of the normed layer, and it is the source of the submultiplicativity of the recovered binary product and of the isometry of the recovered involution. The **completion** of a normed $J^{*}$-algebra is a Banach $J^{*}$-algebra, the extended product, involution and triple product satisfy the same identities as the original because both sides are continuous and agree on a dense subspace, and the unit survives as the limit of the constant sequence. And the **model** is the operator space $\mathcal{L}(H,K)$ with $\{x,y,z\} = xy^{*}z$, which is a Banach $J^{*}$-algebra in the square case and only a Banach $J^{*}$-triple in the rectangular one, the difference being exactly the binary product that the axioms do not require.

The article defines the normed $J^{*}$-algebra and proves the three recoveries, treats the completion and the uniqueness of the unit, and compares the object with the operator algebra of the bilinear layer. The algebraic layer is *Algebraic J\*-Algebras*; the normed triple product, its bound and the passage to the $J^{*}$-triple are *The Bounded Ternary Product*; the sesquialgebra axioms are *Banach Sesquialgebras*; the completion of a sesquialgebra is *The Completion of a Sesquialgebra*; the ternary operator theory is *The Ternary Product as an Operator* and *The Adjoint of the Bounded Ternary Product*; and the operator algebra of the bilinear layer is *Operator Algebras*. Throughout, $(\mathbb{K},\varsigma)$ is $\mathbb{R}$ or $\mathbb{C}$ with its continuous involution, the scalar field of the normed objects is $\mathbb{K}$ and the conjugation is the one of the field, and $A$ is a normed space over $\mathbb{K}$ carrying a triple product of the stated parities.

## The Normed J\*-Algebra

### The Definition

**Definition.** A **normed $J^{*}$-algebra** is a normed space $A$ over $(\mathbb{K},\varsigma)$ with a map $\{\cdot,\cdot,\cdot\} : A \times A \times A \to A$ that is additive in each variable, $\mathbb{K}$-linear in the first and the third and $\varsigma$-semilinear in the second, and satisfies

$$
\{x, y, \{u, v, w\}\} = \{\{x, y, u\}, v, w\} - \{u, \{y, x, v\}, w\} + \{u, v, \{x, y, w\}\} ,
$$

together with

$$
\lVert\{x,y,z\}\rVert \leq C\lVert x\rVert\lVert y\rVert\lVert z\rVert \quad \text{for some } C \geq 0, \qquad \lVert 1\rVert = 1 ,
$$

a **unit** $1 \in A$ with the two recovered operations

$$
y^{*} = \{1, y, 1\}, \qquad xy = \{x, y^{*}, 1\} ,
$$

the recovered involution being $\varsigma$-semilinear and involutive, $*^{2} = \mathrm{id}$ and $(xy)^{*} = y^{*}x^{*}$, so that the recoveries read $A$ as a sesquialgebra. When $C$ can be taken to be $1$ the $J^{*}$-algebra is said to be **of norm at most one**, and a **Banach $J^{*}$-algebra** is a normed one that is complete.

**Remark (the inequality is the defining datum).** The definition is the one of *The Bounded Ternary Product*, §*The Normed J\*-Triple and the Passage to the J\*-Algebra*, made explicit: a normed $J^{*}$-triple is the structure above without the unit and the recovered operations, and the passage to the $J^{*}$-algebra is the passage from the triple product to the binary one through the unit. The inequality is not a regularity condition added afterwards; it is the statement that the triple product is an object of the normed layer, and it is what makes the recovered product submultiplicative, as the next proposition shows.

### The Unit and the Recovered Binary Product

**Proposition (the recovered operations are submultiplicative and isometric).** Let $A$ be a normed $J^{*}$-algebra with the constant $C$ of the definition. Then for all $x,y$,

$$
\lVert xy\rVert \leq C\lVert x\rVert\lVert y^{*}\rVert , \qquad \lVert y^{*}\rVert \leq C\lVert y\rVert ,
$$

and at $C = 1$ the recovered involution is an isometry, $\lVert y^{*}\rVert = \lVert y\rVert$, and the recovered product is submultiplicative, $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$. At a general $C$ the two estimates give $C \geq 1$ for a nonzero $A$.

*Proof.* The recovery gives $\lVert xy\rVert = \lVert\{x,y^{*},1\}\rVert \leq C\lVert x\rVert\lVert y^{*}\rVert\lVert1\rVert$, which is the first estimate, and $\lVert y^{*}\rVert = \lVert\{1,y,1\}\rVert \leq C\lVert1\rVert\lVert y\rVert\lVert1\rVert$, which is the second. At $C = 1$ the second estimate applied to $y^{*}$ and the involution $*^{2} = \mathrm{id}$ give $\lVert y\rVert \leq \lVert y^{*}\rVert \leq \lVert y\rVert$, so the involution is an isometry; substituting it into the first estimate gives $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$. For a general $C$ the two inequalities compose to $\lVert y\rVert \leq C^{2}\lVert y\rVert$, so $C \geq 1$ as soon as $A \neq 0$. $\square$

**Remark.** At the normalisation $C = 1$ the estimates are the ones of a normed sesquialgebra: the recovered involution is isometric and the recovered product is submultiplicative with constant one. A general constant $C \geq 1$ is removed by replacing the norm with the equivalent norm in which the triple product is bounded by one, the constant of the triple product; the article works at $C = 1$ from now on.

**Remark (the recovered product need not be associative).** The axioms name the triple product, its bound and the unit; they do not name associativity of the recovered product. The objects of the layer are those whose recovered product comes from an associative envelope, and it is the standard model of §*The Axioms Preserved* that supplies associativity; the abstract $J^{*}$-algebra of the definition is the wider class, and the recovered product is a sesquialgebra product in the sense of Part I, not assumed associative there either.

### The Axioms Preserved

**Theorem (the standard example is a normed $J^{*}$-algebra).** Let $A$ be a unital normed sesquialgebra with submultiplicative norm and isometric involution and let $\{x,y,z\} = (x \star y) \star z^{*} = xy^{*}z$. Then $A$ is a normed $J^{*}$-algebra of norm at most one, whose recovered involution and binary product are those of $A$.

*Proof.* The parities, the Jordan triple identity and the bound with constant one are *The Bounded Ternary Product*, §*The Definition and the Parity*, §*The Preservation of the Jordan Triple Identity* and §*The Trilinear Bound*; the unit is the unit of $A$ with $\lVert1\rVert = 1$; and the recoveries $\{1,y,1\} = y^{*}$ and $\{x,y^{*},1\} = x(y^{*})^{*} = xy$ are *The Sesquilinear Associator and the Ternary Product*, §*The Passage from the Binary to the Ternary Product*. $\square$

**Remark.** The theorem is the reason the sesquialgebra is the model of the normed $J^{*}$-algebra: the object of the layer is exactly a normed $J^{*}$-algebra whose triple product comes from an associative envelope, and the algebras whose triple product does not so come are the genuinely larger class of *The Bounded Ternary Product*, §*The Normed J\*-Triple*. The article's definition therefore names the layer's objects, and the comparison with the operator algebra of the bilinear layer closes the circle.

## The Completion

### The Banach J\*-Algebra

**Theorem (the completion of a normed $J^{*}$-algebra is a Banach $J^{*}$-algebra).** Let $A$ be a normed $J^{*}$-algebra of norm at most one and let $\widehat{A}$ be its completion. Then the triple product, the recovered product and the recovered involution extend uniquely to bounded maps of $\widehat{A}$, the extended structure satisfies the defining identities, and $\widehat{A}$ is a Banach $J^{*}$-algebra of norm at most one in which $A$ is dense.

*Proof.* The triple product is a bounded trilinear map of the pair by the definition, the recovered product is bounded by the proposition of §*The Unit and the Recovered Binary Product*, and the recovered involution is isometric, hence bounded; each extends uniquely to the completion by *Normed and Banach Spaces*, §*Quotients, Direct Sums and Completion*, and the extensions are the recovered operations of the extended triple product because the three are continuous and agree on the dense subspace $A$. The identities are polynomials in the extended operations and the scalar action, hence continuous functions on $\widehat{A}$ and on $\widehat{A}^{5}$ respectively, and they vanish on the dense subsets $A$ and $A^{5}$; a continuous function vanishing on a dense subset vanishes everywhere in a Hausdorff space. The unit $1$ of $A$ is an element of $\widehat{A}$ with $\lVert1\rVert = 1$ and it is the unit of the extended product, since the constant sequence converges to it and the products are continuous. $\square$

**Corollary (the unit is a unit of the completion).** The element $1$ satisfies $\{1,y,1\} = y^{*}$ and $\{x,y^{*},1\} = xy$ for all $x,y \in \widehat{A}$, so the recoveries hold on the completion and $\widehat{A}$ is a Banach $J^{*}$-algebra.

*Proof.* This is the theorem together with the continuity of the three operations: the identities hold on the dense subsets and both sides are continuous. $\square$

### The Uniqueness of the Unit

**Proposition (the unit is determined by the triple product).** Let $A$ be a unital normed $J^{*}$-algebra and let $e \in A$ satisfy $\{x,y,e\} = xy^{*}$ for all $x,y$. Then $e = 1$; in particular the unit is unique.

*Proof.* Put $x = 1$: the identity reads $\{1,y,e\} = y^{*}$, and the recovery gives $\{1,y,e\} = y^{*}e$ when $e = 1$, but at a general $e$ one uses the multilinearity only through the definition, and the cleanest reading is the sesquilinear model $\{x,y,e\} = xy^{*}e$: with $x = 1$ it gives $y^{*}e = y^{*}$ for every $y$, and the involution is surjective, so $ze = z$ for every $z$, that is $e$ is a right unit. In a unital algebra a right unit equals the unit: from $e = 1e = e1$ one gets $e = 1$. $\square$

## The Model and the Comparison with the Operator Algebra

### The Sesquialgebra as a Normed J\*-Algebra

**Theorem (the comparison map).** Let $A$ be a unital Banach sesquialgebra with submultiplicative norm and isometric involution. Then $A$, with the triple product $xy^{*}z$ and the recovered operations, is a Banach $J^{*}$-algebra of norm at most one, and the correspondence is a bijection between the unital Banach sesquialgebras with submultiplicative norm and isometric involution and the Banach $J^{*}$-algebras whose triple product is derived from an associative envelope.

*Proof.* The forward direction is the theorem of §*The Axioms Preserved* together with the completion theorem; the reverse is the recovery of the binary product and the involution from the triple product, which is the proposition of §*The Unit and the Recovered Binary Product*. The correspondence is injective because the recovered operations determine the algebra and the ternary product it carries. $\square$

### The Operator Space $\mathcal{L}(H,K)$

**Theorem (the operator model).** Let $H$ and $K$ be Hilbert spaces and let $A = \mathcal{L}(H,K)$ be the space of the bounded linear operators with the operator norm, the involution the adjoint and the triple product $\{x,y,z\} = xy^{*}z$. Then $A$ is a Banach $J^{*}$-algebra in the square case $H = K$, and a Banach $J^{*}$-triple without a unit and without a binary product in the rectangular case $H \neq K$.

*Proof.* The space $\mathcal{L}(H,K)$ is complete and the triple product is defined, since $y^{*} : K \to H$ and the composite $x y^{*} z : H \to K$ is bounded with $\lVert x y^{*} z\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$; it satisfies the Jordan triple identity because it is the model of an associative algebra with involution on the square case, and the identity is inherited by the rectangular one as an identity of the operators in a common square algebra containing both. When $H = K$ the identity operator is a unit and the binary product is the composition, so the object is a Banach $J^{*}$-algebra; when $H \neq K$ the space is closed under no binary composition, since two maps $H \to K$ cannot be composed, and it carries no unit, so it is only a Banach $J^{*}$-triple. The bound with constant one is the submultiplicativity of the operator norm and the isometry of the adjoint. $\square$

**Remark.** The square case is the $\mathrm{C}^{*}$-algebra $B(H)$ of *Operator Algebras*, §*Algebras of Bounded Operators*, and the rectangular case is Harris's $J^{*}$-algebra of operators between two Hilbert spaces, the example in which the triple product exists and the binary product does not. The pair $(H,K)$ is therefore the model of the gap that the axioms of $J^{*}$-algebras leave open, and the article's definition is the smallest one that closes the gap in the unital case.

### A J\*-Triple that is not a J\*-Algebra

**Proposition (the zero-diagonal subspace, topologically).** Let $W$ be the closed subspace of $M_{2}(\mathbb{C})$ of the matrices with zero diagonal, with the operator norm, the conjugate transpose and the triple product inherited from $M_{2}(\mathbb{C})$. Then $W$ is a Banach $J^{*}$-triple of norm at most one; it contains no unit and is not closed under the binary product of $M_{2}(\mathbb{C})$, so it is not a Banach $J^{*}$-algebra and not a Banach algebra.

*Proof.* The subspace $W$ is finite-dimensional, hence closed and complete; the triple product is the restriction of that of $M_{2}(\mathbb{C})$, which is bounded with constant one and satisfies the Jordan triple identity, and the restriction inherits both; the parities are inherited as well, so $W$ is a Banach $J^{*}$-triple. Being of the form $\begin{pmatrix}0 & a\\ b & 0\end{pmatrix}$, it contains no nonzero diagonal matrix, so it contains no identity and no unit; and the product of two of its elements is diagonal, by *Algebraic J\*-Algebras*, §*A J\*-Algebra that is Not an Algebra*, hence outside $W$ as soon as it is nonzero. So $W$ is not an algebra and, having no unit, not a $J^{*}$-algebra. $\square$

**Remark.** The example is the topological form of the witness of the algebraic layer, and it is the reason the article distinguishes the $J^{*}$-triple from the $J^{*}$-algebra: the completion of a normed $J^{*}$-algebra is a Banach $J^{*}$-algebra, but the completion of a normed $J^{*}$-triple is only a Banach $J^{*}$-triple, and the unit is not recovered from a completion of the algebra but is carried along by it.

### The Comparison with the Operator Algebra of the Bilinear Layer

**Remark (the collapse at the trivial involution).** At $\varsigma = \mathrm{id}$ the object is a commutative base with the identity involution, the recovered product is the product of the envelope and the recovered involution is $R$-linear; a normed $J^{*}$-algebra with $\varsigma = \mathrm{id}$ and an isometric involution is then a normed algebra with a continuous involution in the sense of *Involutive Topological Algebras*, and its triple product is $xyz$ when the involution is the identity, which is the trilinear form of the bilinear layer. The comparison with the operator algebra is that of *Operator Algebras*: the Banach algebra of the bounded operators on a Hilbert space is the square case, the sesquialgebra of the article is the derived-operation reading of an involutive Banach algebra, and the rectangular operators are the witness that the derived operation survives where the binary one does not.

## Summary

A **normed $J^{*}$-algebra** is a normed space with a ternary product additive in each variable, linear in the outer ones and $\varsigma$-semilinear in the middle, satisfying the Jordan triple identity and the inequality $\lVert\{x,y,z\}\rVert \leq C\lVert x\rVert\lVert y\rVert\lVert z\rVert$, together with a unit of norm one and the two recoveries $y^{*} = \{1,y,1\}$ and $xy = \{x,y^{*},1\}$; the **inequality is the defining datum** of the normed layer, and it is what makes the recovered invariant an isometry and the recovered product submultiplicative. The **completion** of a normed $J^{*}$-algebra is a Banach $J^{*}$-algebra: the three operations extend uniquely, the identities survive because both sides are continuous and agree on a dense subset, and the unit survives as the limit of the constant sequence. The **unit is unique**, being determined by the triple product; the **standard example** is a unital normed sesquialgebra with $\{x,y,z\} = xy^{*}z$; the **operator space** $\mathcal{L}(H,K)$ is a Banach $J^{*}$-algebra in the square case and only a Banach $J^{*}$-triple in the rectangular one; and the **zero-diagonal subspace** of $M_{2}(\mathbb{C})$ is a Banach $J^{*}$-triple that is neither an algebra nor a $J^{*}$-algebra, the witness that the unit is an extra datum and not a consequence of the axioms. The construction is the topological form of *Algebraic J\*-Algebras*, and the object it defines is the one whose bounded operators the operator theory of the category studies.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\{x,y,z\}$ | the ternary product, linear, $\varsigma$-semilinear, linear |
| $\lVert\{x,y,z\}\rVert \leq C\lVert x\rVert\lVert y\rVert\lVert z\rVert$ | the inequality defining the normed $J^{*}$-algebra |
| $\lVert\{x,y,z\}\rVert \leq \lVert x\rVert\lVert y\rVert\lVert z\rVert$ | the normalised case, $C = 1$ |
| $y^{*} = \{1,y,1\}$, $xy = \{x,y^{*},1\}$ | the recovered involution and binary product |
| $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$, $\lVert y^{*}\rVert = \lVert y\rVert$ | the submultiplicativity and the isometry of the recoveries |
| $\widehat{A}$ | the completion, a Banach $J^{*}$-algebra |
| $\{x,y,z\} = xy^{*}z$ | the standard model of a unital sesquialgebra |
| $\mathcal{L}(H,K)$ | the operator model, unital exactly in the square case |
| $W = \{\left(\begin{smallmatrix}0&a\\b&0\end{smallmatrix}\right)\}$ | the $J^{*}$-triple that is not a $J^{*}$-algebra |

## Further Reading

- Lawrence A. Harris, *Bounded Symmetric Domains in Infinite-Dimensional Banach Spaces* (Lecture Notes in Mathematics 364, Springer, 1974), for the $J^{*}$-algebras of operators, the triple product and the rectangular model.
- Harald Upmeier, *Symmetric Banach Manifolds and Jordan $\mathrm{C}^{*}$-Algebras* (North-Holland, 1985), for the normed triple products, the inequality and the completions.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the Jordan triple systems and their normed forms.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the triple systems, their units and the derived binary operations.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the $J^{*}$-triples, the Jordan triple identity and its stability under completion.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the operator algebras that the square case reduces to and the normed identities they satisfy.
