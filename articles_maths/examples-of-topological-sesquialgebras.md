# __Examples of Topological Sesquialgebras__

## Introduction

The layer has three definitions — a complex sesquialgebra, a topological one, and the normed and complete one — and the examples are what fix the sense in which a sesquialgebra is more than an algebra. Every one of the examples below except the degenerate zero product is an associative algebra with an isometric involution, read through the derived product $x \star y = xy^{*}$; what separates them is the involution, which may be trivial, in which case the derived product is the algebra product and the object is a Banach algebra of the bilinear layer, or nontrivial, in which case the derived product is a genuinely new operation and the object is neither associative nor commutative — by the theorem of full type when the base involution $\varsigma$ is nontrivial, and by direct witness for the real matrices and the quaternions, whose base is collapsed.

Three facts organise the article. The **field, the matrices, the group algebra and the function algebra** are the four standard models: all are complete with an isometric involution, all have the derived product submultiplicative with norm exactly one, and all are of full type with the conjugation of the scalars as the base involution, so none of them is associative or commutative as a sesquialgebra and each is an object of the genuinely sesquilinear layer. The **collapsed objects** are those in which at least one of the two involutions is trivial: a Banach algebra with the identity involution, where $* = \mathrm{id}$ and the derived product is the algebra product, the zero product, which is degenerate, and — with only the base collapsed — the real division algebras and the real matrices, where $\varsigma = \mathrm{id}$ but $*$ is nontrivial. And the **base involution** is the finer invariant: an object with $\varsigma = \mathrm{id}$ but $*$ nontrivial, such as the quaternions over $\mathbb{R}$ or the real matrices with the transpose, has a conjugate module equal to its module and a derived product different from its product, so it sits in the layer with a collapsed base and a nontrivial sesquilinear structure.

The article reads the four standard models, treats the collapsed objects and the degenerate zero product, tabulates the invariants — completeness, the isometry of the involution, the $\mathrm{C}^{*}$-identity, the norm of the sesquilinear product, full type, associativity and commutativity of the derived product, and the two collapses — and closes with the collapse at $\varsigma = \mathrm{id}$. The definitions and the full-type theorem are *Sesquialgebras*; the algebra examples are *Examples of Sesquialgebras*; the normed layer is *Banach Sesquialgebras*; the collapse is *Topological Sesquialgebras*, §*The Collapse*; the involution and the $\mathrm{C}^{*}$-identity are *The Continuity of the Involution*; and the group algebra is *Group Algebras*. Throughout, $(\mathbb{K},\varsigma)$ is $\mathbb{R}$ or $\mathbb{C}$ with its continuous involution, an object is a Banach sesquialgebra of the standard model, that is a Banach algebra over $\mathbb{K}$ with an isometric $\varsigma$-semilinear involution $*$ and the derived product $x \star y = xy^{*}$; the algebra is unital in every named example except the group algebra $L^{1}(G)$ for non-discrete $G$, where an approximate identity replaces the unit — the degenerate zero product of §*The Degenerate Product*, whose product is not of that shape, is the one example kept outside the standard model — and the **norm of the sesquilinear product** is

$$
\lVert\star\rVert = \sup\{\lVert x \star y\rVert : \lVert x\rVert \leq 1, \ \lVert y\rVert \leq 1\} .
$$

## The Four Standard Models

### The Field

**Example (the complex numbers, verdict: the smallest nontrivial object).** Let $A = \mathbb{C}$ with the modulus, $\varsigma$ the conjugation and $* = \varsigma$. Then $A$ is a Banach algebra, $\lvert zw^{*}\rvert = \lvert z\rvert\lvert w\rvert$, the involution is isometric and satisfies the $\mathrm{C}^{*}$-identity $\lvert z^{*}z\rvert = \lvert z\rvert^{2}$, and the derived product is $z \star w = z\bar w$ with $\lVert\star\rVert = 1$. The object is faithful, its products generate it and it has no nonzero left annihilator, so it is of full type; by the theorem of *Sesquialgebras*, §*The Collapse at the Identity*, it is neither associative nor commutative, the witnesses being $1 \star i = -i$ against $i \star 1 = i$ for the failure of commutativity and $(1 \star 1) \star i = -i$ against $1 \star (1 \star i) = i$ for the failure of associativity.

### The Matrices

**Example (the complex matrices, verdict: the model with the $\mathrm{C}^{*}$-identity).** Let $A = M_{n}(\mathbb{C})$ with the operator norm, the conjugation, the conjugate transpose and $X \star Y = XY^{*}$. Then the operator norm is submultiplicative, the adjoint is isometric, the $\mathrm{C}^{*}$-identity $\lVert X^{*}X\rVert = \lVert X\rVert^{2}$ holds, and $\lVert X \star Y\rVert \leq \lVert X\rVert\lVert Y\rVert$ with $\lVert\star\rVert = 1$, attained at $X = Y = E_{11}$. The object is of full type for $n \geq 2$, so it is neither associative nor commutative: the associativity witness is $X = E_{11} + E_{21} + E_{22}$, for which $(X \star X) \star X \neq X \star (X \star X)$ by *The Exponential Map on a Banach Sesquialgebra*, §*Why the Derived Operation Has No Exponential*, and the commutativity witness is $E_{12} \star E_{22} = E_{12}$ against $E_{22} \star E_{12} = E_{21}$. The example is the finite-dimensional model in which the operator theory of the category is read, and it is the one whose conjugate dual is the trace class, by *The Conjugate Dual of a Sesquialgebra*, §*Examples*.

**Example (the real matrices, verdict: a collapsed base with a nontrivial involution).** Let $A = M_{n}(\mathbb{R})$ with the operator norm, $\varsigma = \mathrm{id}$ and $*$ the transpose. Then the derived product is $X \star Y = XY^{\mathsf{T}}$, which is not the ordinary product and is neither associative nor commutative, while the base involution is trivial and the conjugate module is the module. The object is of full type for $n \geq 2$, and the verdict is that the collapse of the layer at $\varsigma = \mathrm{id}$ does not make the object a Banach algebra: it makes the conjugate module the module and the scalar rules coincide, and the derived product remains a genuinely sesquilinear operation. The real matrices are the model of a *bilinear* base with a *sesquilinear* involution, and the example separates the two collapses.

### The Group Algebra

**Example (the group algebra, verdict: isometric involution without the $\mathrm{C}^{*}$-identity).** Let $G$ be a locally compact group, $A = L^{1}(G)$ with the convolution product, the involution $f^{*}(x) = \overline{f(x^{-1})}\,\Delta(x)^{-1}$ and the $L^{1}$-norm, over $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation. Then the norm is submultiplicative by Young's inequality, the involution is isometric, $\lVert f^{*}\rVert_{1} = \lVert f\rVert_{1}$, and $A$ is a Banach sesquialgebra; for $G = \mathbb{R}$ the norm is not a $\mathrm{C}^{*}$-norm, by *The Continuity of the Involution*, §*Examples*. The object is faithful with generating products and no nonzero left annihilator for $G \neq \{1\}$, since the algebra has an approximate identity, so it is of full type and neither associative nor commutative; and $\lVert\star\rVert = 1$, attained at the unit mass when $G$ is discrete. The example is the model in which the layer contains objects that are complete and isometrically involutive but not $\mathrm{C}^{*}$-algebras, and it is *The Continuity of the Involution*, §*Examples*.

### The Function Algebra

**Example (the function algebra, verdict: the commutative model of a noncommutative derived product).** Let $X$ be a compact Hausdorff space and let $A = C(X,\mathbb{C})$ with the supremum norm, $\varsigma$ the conjugation and $\sigma(f) = \bar f$. Then $A$ is a commutative $\mathrm{C}^{*}$-algebra, the involution is isometric with the $\mathrm{C}^{*}$-identity, and the derived product is $f \star g = f\bar g$ with $\lVert f \star g\rVert_{\infty} = \lVert f\rVert_{\infty}\lVert g\rVert_{\infty}$, so $\lVert\star\rVert = 1$. The underlying algebra is commutative and the derived product is not: the constant function $g = i$ has $\bar g = -g \neq g$, so $1 \star g = \bar g = -g$ against $g \star 1 = g$ exhibits the failure of commutativity, and $(1 \star 1) \star g = \bar g = -g$ against $1 \star (1 \star g) = g$ the failure of associativity; the object is of full type, hence neither associative nor commutative. The example is the infinite-dimensional model, and it is the commutative-algebra analogue of the field.

## The Collapsed Objects

### The Banach Algebras with the Identity Involution

**Proposition (the trivial involution).** Let $A$ be a unital Banach algebra over $\mathbb{K}$ with the identity involution, $* = \mathrm{id}$, and $\varsigma = \mathrm{id}$. Then $A$ is a unital Banach sesquialgebra whose derived product is the product of $A$, the conjugate module is the module, and the object is exactly a Banach algebra of *Topological Algebras and Banach Algebras*, §*Topological Algebras*.

*Proof.* The identity map is a $\varsigma$-semilinear involution for $\varsigma = \mathrm{id}$, and it is isometric, so $A$ is a Banach sesquialgebra of the standard model; the derived product is $x \star y = xy^{*} = xy$, the product of the algebra, and the conjugate module is the module because the twisted action is the scalar action. $\square$

**Remark.** The proposition is the sense in which the sesquilinear layer contains the bilinear one: the objects with $* = \mathrm{id}$ are the Banach algebras, and the inclusion is not a coincidence but the collapse of the two scalar rules into one. Note that $* = \mathrm{id}$ forces $\varsigma = \mathrm{id}$, because $\varsigma$-semilinearity at the unit reads $*(\lambda 1) = \varsigma(\lambda)1 = \lambda1$; so the full collapse is the case of the trivial algebra involution, and the two collapses at $\varsigma = \mathrm{id}$ and at $* = \mathrm{id}$ are distinct.

### The Real Division Algebras

**Example (the quaternions, verdict: a collapsed base, a nontrivial involution).** Let $A = \mathbb{H}$ over $\mathbb{R}$ with the Euclidean norm and $*$ the quaternion conjugation, so $\varsigma = \mathrm{id}$. Then $A$ is a normed division algebra, the conjugation is isometric, and the derived product is $p \star q = p\bar q$, whose norm is one and which is neither associative nor commutative: the same computation that fails in the field fails here, $p\bar q \neq q\bar p$ for $p = 1$, $q = j$, and $(1 \star i) \star i = -1 \neq 1 = 1 \star (i \star i)$ for the associativity. The object is of full type, the base is collapsed, and the verdict is the one of the real matrices: the collapse of the base does not collapse the derived operation.

### The Degenerate Product

**Example (the zero product, verdict: a degenerate object).** Let $A$ be a unital Banach algebra with $\varsigma = \mathrm{id}$ and the involution $* = \mathrm{id}$, and put $x \star y = 0$. This is the one example of the article that is not the derived operation of the algebra, so it is outside the standard model of the standing hypotheses and the tabulation flags it; the product $x \star y = 0$ does satisfy the two scalar rules and submultiplicativity, so $A$ is a Banach sesquialgebra; it is faithful but its products generate only $\{0\}$ and every element annihilates $A$ on both sides, so it is not of full type, and the full-type theorem does not apply. The example is the witness that the conditions of full type are not automatic and that the collapse conclusion needs them: a sesquialgebra may be associative and commutative when it is degenerate, and the hypothesis of full type is what rules this out.

## The Tabulation

### The Table

**Remark (the invariants of the examples).** The tabulation records, for each of the standard models, the completeness, the isometry of the involution, the $\mathrm{C}^{*}$-identity, the base involution, the norm of the sesquilinear product, and the three structural verdicts. The symbol $\checkmark$ is a yes and $\times$ a no. The $\mathrm{C}^{*}$-identity is the algebraic condition $\lVert x^{*}x\rVert = \lVert x\rVert^{2}$ of the norm: it holds for the complex $\mathrm{C}^{*}$-algebras of the table and also for the real $\mathrm{C}^{*}$-algebras $M_{n}(\mathbb{R})$ and $\mathbb{H}$, and it fails for $L^{1}(G)$, whose involution is isometric without it.

| object | complete | $*$ isometric | $\mathrm{C}^{*}$-identity | $\varsigma$ | $\lVert\star\rVert$ | full type | $\star$ assoc. | $\star$ comm. |
|---|---|---|---|---|---|---|---|---|
| $\mathbb{C}$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | conj | $1$ | $\checkmark$ | $\times$ | $\times$ |
| $M_{n}(\mathbb{C})$, $n \geq 2$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | conj | $1$ | $\checkmark$ | $\times$ | $\times$ |
| $L^{1}(G)$ | $\checkmark$ | $\checkmark$ | $\times$ | conj | $1$ | $\checkmark$ | $\times$ | $\times$ |
| $C(X,\mathbb{C})$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | conj | $1$ | $\checkmark$ | $\times$ | $\times$ |
| $M_{n}(\mathbb{R})$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\mathrm{id}$ | $1$ | $\checkmark$ | $\times$ | $\times$ |
| $\mathbb{H}$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\mathrm{id}$ | $1$ | $\checkmark$ | $\times$ | $\times$ |
| Banach algebra, $* = \mathrm{id}$ | $\checkmark$ | $\checkmark$ | depends | $\mathrm{id}$ | $1$ | depends | $\checkmark$ | depends |
| zero product | $\checkmark$ | $\checkmark$ | depends | $\mathrm{id}$ | $0$ | $\times$ | $\checkmark$ | $\checkmark$ |

**Remark (the reading of the table).** The four standard models and the two base-collapsed models are of full type with a nontrivial algebra involution, and in every one of them the derived product is neither associative nor commutative — by the theorem of *Sesquialgebras*, §*The Collapse at the Identity* for the four standard models, whose base involution is the conjugation, and by direct computation for the two base-collapsed models, where that theorem's hypothesis $\varsigma \neq \mathrm{id}$ fails; the two rows of the table that are associative are the collapsed algebra, whose involution is trivial, and the degenerate product, which is not of full type. The norm of the sesquilinear product is one in every nondegenerate example, which is the statement that the submultiplicative estimate is sharp; it is zero exactly for the degenerate product, and the estimates of the layer are trivial there.

### The Collapse at the Identity

**Theorem (the collapse of the layer).** Let $A$ be an object with $\varsigma = \mathrm{id}$. Then the twisted action is the ordinary action, the conjugate module is the module, the derived operation is the algebra product read through the algebra involution, and the layer of the objects is the layer of *Topological Algebras and Banach Algebras* with a continuous involution. If in addition $* = \mathrm{id}$ then the derived operation is the algebra product and the object is a Banach algebra.

*Proof.* This is the collapse theorem of *Topological Sesquialgebras*, §*The Collapse*, together with the proposition of §*The Banach Algebras with the Identity Involution* for the second clause. $\square$

**Remark.** The table exhibits both collapses: the objects with $\varsigma = \mathrm{id}$ are those in which the conjugate module is the module, so the base has collapsed, and among them the objects with $* = \mathrm{id}$ are those in which also the derived operation is the product, so the object has collapsed to a Banach algebra. The standard models have neither collapse, and they are the objects the operator theory of the category studies.

## Summary

The **four standard models** of a unital Banach sesquialgebra are the field $\mathbb{C}$ with the modulus and the derived product $z \star w = z\bar w$, the matrices $M_{n}(\mathbb{C})$ with the operator norm and the conjugate transpose, the group algebra $L^{1}(G)$ with the convolution and the isometric involution, and the function algebra $C(X,\mathbb{C})$ with the supremum norm and the pointwise product; each is complete with an isometric involution, each has $\lVert\star\rVert = 1$, and each is of **full type** with the conjugation of the scalars as the base involution, so each is **neither associative nor commutative** as a sesquialgebra. The objects with a trivial algebra involution — a Banach algebra with $* = \mathrm{id}$ — **collapse** to the layer of the bilinear algebras, the derived product being the algebra product and the conjugate module being the module; the objects with $\varsigma = \mathrm{id}$ but $*$ nontrivial, such as the real matrices with the transpose and the quaternions with the conjugation, have a **collapsed base** and a nontrivial derived product, and they are the witness that the collapse of the base does not collapse the operation; and the **degenerate zero product** is the witness that the conditions of full type are not automatic, being associative and commutative and of no use to the layer. The tabulation records the completeness, the isometry, the $\mathrm{C}^{*}$-identity, the base involution, the norm of the sesquilinear product and the three structural verdicts for each object, and the collapse theorem of the layer is the statement that both collapses are read from the two involutions $\varsigma$ and $*$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $x \star y = xy^{*}$ | the derived product, the object of every example |
| $\lVert\star\rVert = \sup\{\lVert x \star y\rVert\}$ | the norm of the sesquilinear product |
| $z \star w = z\bar w$ on $\mathbb{C}$ | the field, norm one, of full type |
| $X \star Y = XY^{*}$ on $M_{n}(\mathbb{C})$ | the matrices, the $\mathrm{C}^{*}$-identity, of full type |
| $X \star Y = XY^{\mathsf{T}}$ on $M_{n}(\mathbb{R})$ | the real matrices, collapsed base, of full type |
| $f \star g = f\,g^{*}$ on $L^{1}(G)$ | the group algebra, isometric involution without the $\mathrm{C}^{*}$-identity |
| $f \star g = f\bar g$ on $C(X,\mathbb{C})$ | the function algebra, commutative algebra, noncommutative derived product |
| $p \star q = p\bar q$ on $\mathbb{H}$ | the quaternions, collapsed base, of full type |
| $* = \mathrm{id}$ | the full collapse to a Banach algebra |
| $\varsigma = \mathrm{id}$ | the collapse of the base, the conjugate module being the module |
| $x \star y = 0$ | the degenerate product, not of full type |

## Further Reading

- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the Banach algebras, the involutions and the examples that the article reads through the derived product.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume I* (Cambridge University Press, 1994), for the group algebras, the $\mathrm{C}^{*}$-algebras and the isometric involutions.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the commutative $\mathrm{C}^{*}$-algebras and the function algebras.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the matrix algebras, the operator norms and the trace duality of the examples.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953), for the convolution algebra $L^{1}(G)$, its involution and the approximate identity.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involutions, the full-type conditions and the examples over an arbitrary commutative ring.
