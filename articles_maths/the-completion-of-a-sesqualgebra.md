# __The Completion of a Sesqualgebra__

## Introduction

*Banach Sesqualgebras* assumes the object complete, and *Fréchet and Locally Convex Sesqualgebras* extends the assumption to the locally convex case. This article removes it for the normed object: it takes a normed sesqualgebra over $(\mathbb{K},\varsigma)$, completes the underlying normed space, and shows that the product, the twisted scalar action and, when present, the algebra involution extend uniquely to the completion, so that the completion is a Banach sesqualgebra over the same datum. It is the sesquilinear counterpart of the completion paragraph of *Topological Algebras and Banach Algebras*, §*Normed Algebras* and of *The Completion Operator*, read for the twisted product.

The one new ingredient with respect to the bilinear layer is the twisted slot. The product of a sesqualgebra is not bilinear on $A \times A$ but bilinear on the pair $(A,A^{\varsigma})$, and the extension has to be performed on that pair; this is harmless because the conjugate module is the same normed space with the same uniformity, so the completion of the conjugate module is the conjugate of the completion, $\widehat{A^{\varsigma}} = \widehat{A}^{\varsigma}$. The extension of the product is then the extension of a uniformly continuous bilinear map, and the submultiplicative estimate passes to the limit by continuity. The algebra involution, when the sesquilinear product is presented as a derived operation $x \star y = xy^{*}$, extends by *The Involution and the Completion of a Ring*, §*The Extension to the Completion*, and the derived operation of the completion is the extension of the product.

Three facts organise the article. A normed sesqualgebra has a completion which is a Banach sesqualgebra over the same datum, and the canonical map $\iota : A \to \widehat{A}$ is an isometric morphism with dense image; the product extends by uniform continuity on bounded sets, the twisted action by the extension of the scalar action, and the extension is submultiplicative, associative when the object is, and unital with the same unit. The completion is the reflection of the normed sesqualgebras into the Banach ones: every continuous morphism into a complete Hausdorff sesqualgebra factors uniquely through $\iota$, so the completion is a functor and it is idempotent, $\widehat{\widehat{A}} \cong \widehat{A}$. And at $\varsigma = \mathrm{id}$ the theorem is the completion of a normed algebra, recovering the Banach algebra completion; the closure of zero is killed by the completion, exactly as for a topological ring, so the completion of a sesqualgebra is the completion of its Hausdorff quotient.

The article completes the underlying space, extends the product and the twisted action, extends the involution and the derived operation, proves the universal property, functoriality and idempotence, and reads the examples. It cites the analytic prerequisites rather than proving them: the completion of a normed space and its universal property are *Normed and Banach Spaces*, §*Quotients, Direct Sums and Completion*, the general operator is *The Completion Operator* and *Topological Modules and Vector Spaces*, §*Completion*, the involution extension is *The Involution and the Completion of a Ring*, and the continuity of the algebra involution is *The Continuity of the Involution*. Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ its continuous involution, $A$ a normed sesqualgebra over $(\mathbb{K},\varsigma)$ in the sense of *Banach Sesqualgebras*, and $\widehat{A}$ the completion of the underlying normed space with canonical map $\iota$.

## The Completion of the Underlying Space

### The Completion

**Proposition (the completion of the normed space).** Let $A$ be a normed $\mathbb{K}$-space. Then there is a complete normed $\mathbb{K}$-space $\widehat{A}$ and a linear isometry $\iota : A \to \widehat{A}$ with dense image, unique up to isometric isomorphism; every uniformly continuous map from $A$ into a complete Hausdorff uniform space extends uniquely to $\widehat{A}$.

*Proof.* This is the construction of *Normed and Banach Spaces*, §*Quotients, Direct Sums and Completion*: the completion of the metric space $A$ with the extended vector operations, or equivalently the space of Cauchy sequences modulo the null sequences, and the universal property is that of a completion. $\square$

**Proposition (the completion is blind to the closure of zero).** Let $A$ be a topological sesqualgebra with the closure of zero $\overline{\{0\}}$ and let $q : A \to A/\overline{\{0\}}$ be the Hausdorff quotient. Then the completion of $A$ is the completion of $A/\overline{\{0\}}$, and $\iota$ factors as $q$ followed by the injective completion map of the Hausdorff quotient. In the normed case the space is already Hausdorff, $\overline{\{0\}} = \{0\}$, and the statement is the identity; it belongs to the general layer and is quoted here for completeness.

*Proof.* This is the proposition of *The Completion Operator*, §*The Completion* applied to the additive uniform structure, which the sesqualgebra carries unchanged, and to the definition of the completion of a uniform space; the quotient $A/\overline{\{0\}}$ is Hausdorff, by *Topological Sesqualgebras*, §*The Closure of Zero*. $\square$

### The Extension of the Twisted Action

**Theorem (the conjugate module commutes with completion).** Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$. Then the completion of the conjugate module is the conjugate module of the completion,

$$
\widehat{A^{\varsigma}} \;=\; \widehat{A}^{\varsigma},
$$

and the twisted action of $\mathbb{K}$ on $\widehat{A}$ is the unique continuous extension of the twisted action on $A$.

*Proof.* The conjugate module is $A$ with the twisted action, and the twisted action is isometric, $\lVert\lambda \cdot x\rVert = \lvert\varsigma(\lambda)\rvert\lVert x\rVert = \lvert\lambda\rvert\lVert x\rVert$, by *Banach Sesqualgebras*, §*The Isometric Involution*; so $A$ and $A^{\varsigma}$ are the same normed space with the same uniformity and the same Cauchy filters, and their completions are the same complete normed space. The scalar action of a normed space extends to its completion, by *Normed and Banach Spaces*, §*Quotients, Direct Sums and Completion*; the extension of the twisted action is the twisted action of the extension, because both are scalar multiplication and the scalar field is unchanged. $\square$

**Remark.** The identity $\widehat{A^{\varsigma}} = \widehat{A}^{\varsigma}$ is the reason the twisted structure does not complicate the completion: there is one completion and two actions on it, as there is one normed space and two actions before completing. The failure of the identity would occur for a base ring whose involution is not isometric, where the two twisted modules would have different uniformities; over $\mathbb{R}$ and $\mathbb{C}$ it holds always.

## The Extension of the Product

### Uniform Continuity on Bounded Sets

**Proposition (uniform continuity on bounded sets).** Let $A$ be a normed sesqualgebra. Then the product $A \times A^{\varsigma} \to A$ is uniformly continuous on sets of the form $B_1 \times B_2$ with $B_1, B_2$ bounded.

*Proof.* On the product $A \times A^{\varsigma}$ put the norm $\lVert(x,y)\rVert = \max(\lVert x\rVert,\lVert y\rVert)$. The estimate

$$
\lVert x_1y_1 - x_0y_0\rVert \leq \lVert x_1 - x_0\rVert\lVert y_1\rVert + \lVert x_0\rVert\lVert y_1 - y_0\rVert
$$

of *Banach Sesqualgebras*, §*The Submultiplicative Estimate* bounds the difference by a multiple of $\lVert(x_1,y_1) - (x_0,y_0)\rVert$ as long as $\lVert x_0\rVert$ and $\lVert y_1\rVert$ are bounded, which on $B_1 \times B_2$ they are. $\square$

### The Product on the Completion

**Theorem (the extended product).** Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$. Then the product extends to a unique continuous product

$$
\widehat{A} \times \widehat{A}^{\varsigma} \longrightarrow \widehat{A}
$$

making $\widehat{A}$ a normed sesqualgebra over $(\mathbb{K},\varsigma)$; the extension is submultiplicative, $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$, additive in each variable, $\mathbb{K}$-linear in the first and $\varsigma$-semilinear in the second.

*Proof.* A uniformly continuous map into a complete Hausdorff space extends uniquely to the completion, by the universal property of §*The Completion*, applied on bounded sets and glued because the completion is the union of the closures of the bounded sets; the extension is additive and satisfies the two scalar rules because those identities hold on the dense image $\iota(A) \times \iota(A^{\varsigma})$ and the operations are continuous, exactly as in the extension of an involution of *The Involution and the Completion of a Ring*, §*The Extension to the Completion*. Submultiplicativity passes to the limit: for $x = \lim\iota(x_n)$ and $y = \lim\iota(y_n)$,

$$
\lVert xy\rVert = \lim_n\lVert x_ny_n\rVert \leq \lim_n\lVert x_n\rVert\lVert y_n\rVert = \lVert x\rVert\lVert y\rVert ,
$$

continuity of the norm and of the product and the isometry of $\iota$. $\square$

**Corollary (the completion is a Banach sesqualgebra).** $\widehat{A}$ with the extended product and the norm of the completion is a Banach sesqualgebra over $(\mathbb{K},\varsigma)$, and $\iota : A \to \widehat{A}$ is an isometric morphism with dense image.

*Proof.* Completeness is that of the completion, and the axioms of *Banach Sesqualgebras*, §*The Definition* are those verified in the theorem; $\iota$ preserves the norm, the product and the actions by construction. $\square$

**Remark (the product is not assumed associative).** The extension theorem uses only the continuity of the object and not its associativity, so it applies to every object of the layer, associative or not. When the object carries the envelope of a sesquilinear product, the extension is the envelope of the extended product, and the associativity of the envelope passes to the limit by the same density argument.

## The Extension of the Involution

### The Algebra Involution

**Theorem (the extension of the algebra involution).** Let $A$ be a normed algebra over $\mathbb{K}$ with a continuous $\varsigma$-semilinear involution $*$, and let $\widehat{A}$ be the completion of the underlying normed space. Then $*$ extends to a unique continuous $\varsigma$-semilinear involution $\widehat{*}$ of $\widehat{A}$, and the completion is a normed algebra with a continuous involution.

*Proof.* A continuous involution of a normed algebra is uniformly continuous for the additive uniformity, being a continuous homomorphism of the additive topological group; it therefore extends uniquely to the completion by the universal property, and the extension is additive, of order two and reverses products on the dense image, hence everywhere by continuity. This is the theorem of *The Involution and the Completion of a Ring*, §*The Extension to the Completion*, read on the additive group of the normed space; when the involution is continuous but not isometric it is made isometric by the equivalent norm $\max(\lVert x\rVert,\lVert x^{*}\rVert)$ of *The Continuity of the Involution*, §*The Normal Form of a Continuous Involution*, and the normal form commutes with the completion. $\square$

### The Derived Operation

**Theorem (the derived operation of the completion is the extension).** Let $A$ be a normed involutive algebra with a continuous isometric involution $*$, and let $\star$ be its derived operation $x \star y = xy^{*}$, so that $A$ is a normed sesqualgebra over $(\mathbb{K},\varsigma)$ by *Banach Sesqualgebras*, §*The Derived Operation of an Involutive Banach Algebra*. Then $\widehat{A}$ with the algebra product, the extended involution $\widehat{*}$ and the derived operation $\widehat{x} \star \widehat{y} = \widehat{x}\,\widehat{y}^{\widehat{*}}$ is a Banach sesqualgebra, and the derived operation of the completion is the extension of the derived operation of $A$; the two descriptions of $\widehat{A}$ agree.

*Proof.* The completion of a normed algebra is a Banach algebra with the extended product, by the completion paragraph of *Topological Algebras and Banach Algebras*, §*Normed Algebras*, and the extended involution is isometric because it is the continuous extension of an isometry; so the derived operation of the completion is defined and is submultiplicative. The derived operation $\star$ of $A$ is a continuous product, so it extends by §*The Product on the Completion*, and the extension agrees with $\widehat{x}\,\widehat{y}^{\widehat{*}}$ on the dense image, hence everywhere. $\square$

**Remark (the involution is not part of the layer datum).** The base involution $\varsigma$ is fixed and its extension is the identity on $\mathbb{K}$; the algebra involution $*$ is an extra structure that some sesqualgebras carry, and it is the involution that the article extends. The distinction is the one of *Topological Sesqualgebras*, §*The Conjugate Module*: the twisted action uses $\varsigma$ and is not the algebra involution.

## The Universal Property and Functoriality

### The Universal Property

**Theorem (the universal property).** Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$ and let $T$ be a complete Hausdorff topological sesqualgebra over $(\mathbb{K},\varsigma)$. Then for every continuous morphism $g : A \to T$ there is a unique continuous morphism $h : \widehat{A} \to T$ with $h \circ \iota = g$.

*Proof.* The map $g$ is uniformly continuous for the additive uniformities, so it carries the Cauchy filter of $A$ to a Cauchy filter of $T$, which converges because $T$ is complete; the limit $h(x)$ is independent of the approximating net, and it is continuous, additive and multiplicative because those operations are continuous and compatible with limits, exactly as in the universal property of *The Completion Operator*, §*The Universal Property*. The scalar rules pass to the limit by the same density argument, so $h$ is a morphism of sesqualgebras over $(\mathbb{K},\varsigma)$. Uniqueness is the density of $\iota(A)$. $\square$

**Corollary (the completion is a reflection).** The operator $A \mapsto \widehat{A}$ with the unit $\iota$ is the reflection of the category of normed sesqualgebras over $(\mathbb{K},\varsigma)$ into the full subcategory of Banach sesqualgebras: it is left adjoint to the inclusion, and the adjunction is the bijection of the theorem.

*Proof.* The universal property is the statement that $h \mapsto h \circ \iota$ is a bijection from the continuous morphisms $\widehat{A} \to T$ to those $A \to T$, which is the defining property of a reflection. $\square$

### Idempotence

**Theorem (idempotence).** Let $A$ be a normed sesqualgebra. Then the canonical morphism $\iota : \widehat{A} \to \widehat{\widehat{A}}$ is an isomorphism of sesqualgebras over $(\mathbb{K},\varsigma)$.

*Proof.* The completion $\widehat{A}$ is complete, so its own completion is isomorphic to it by the universal property applied to the identity; the same argument as the idempotence of *The Completion Operator*, §*Idempotence*, with the product and the twist carried along because they are continuous. $\square$

## The Collapse at the Trivial Involution

### The Collapse

**Theorem (the collapse).** Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$ with $\varsigma = \mathrm{id}$. Then the product is bilinear, $A$ is a normed algebra, and $\widehat{A}$ is its Banach algebra completion in the sense of *Topological Algebras and Banach Algebras*, §*Normed Algebras*; conversely the completion of a normed algebra is the completion of the corresponding sesqualgebra over $(\mathbb{K},\mathrm{id})$.

*Proof.* With $\varsigma = \mathrm{id}$ the second scalar rule is the first, and the construction is the completion paragraph of the bilinear layer; the twisted action is the scalar action, so §*The Extension of the Twisted Action* is the extension of the scalar action of a normed space, and the extended product is the extended algebra product. $\square$

### Full Type

**Remark (full type).** As in *Banach Sesqualgebras*, §*The Objects of Full Type*, a normed sesqualgebra of full type with a nontrivial involution is neither associative nor commutative, and its completion inherits the property, because the collapse is algebraic and passes to the completion by the density argument of §*The Product on the Completion*. The completion of a full-type object is never a Banach algebra.

## Examples

### The Finite-Rank and the Compact Operators

**Example (from finite rank to compact operators, verdict: the model completion).** Let $A$ be the space of finite-rank operators on the separable Hilbert space with the operator norm, the adjoint involution and the derived operation $S \star T = ST^{*}$. Then $A$ is a normed sesqualgebra which is not complete, and its completion is the Banach sesqualgebra of compact operators with the same product and the adjoint, by the theorem of §*The Derived Operation*: the completion of the finite-rank operators is the compact operators, the adjoint extends because it is isometric, and the derived operation extends because it is continuous. The example is the standard one, and it is the completion named in *Banach Sesqualgebras*, §*The Completeness of the Model*.

### The Sequences

**Example (from finite support to $\ell^{1}$, verdict: the derived operation of a sequence algebra).** Let $A = c_{00}$ be the space of finitely supported complex sequences with the $\ell^{1}$-norm, the termwise conjugation and the product $(x \star y)_k = x_k\bar y_k$. Then

$$
\lVert x \star y\rVert_{1} = \sum_k\lvert x_k\rvert\lvert y_k\rvert \leq \lVert x\rVert_{1}\lVert y\rVert_{\infty} \leq \lVert x\rVert_{1}\lVert y\rVert_{1},
$$

so $A$ is a normed sesqualgebra over $(\mathbb{C},\varsigma)$ which is not complete, and its completion is $\ell^{1}$ with the extended termwise product and the extended termwise conjugation. The example is the discrete model of the completion, and the extended product is submultiplicative by the passage to the limit of §*The Product on the Completion*.

### The Functions

**Example (from polynomials to entire functions, verdict: an incomplete metrisable object and its completion).** Let $A = \mathbb{C}[X]$ with the topology of uniform convergence on compact subsets of $\mathbb{C}$ of *Fréchet and Locally Convex Sesqualgebras*, §*The Boundaries*, the coefficientwise conjugation and the product $f \star g = f\bar g$. The object is a metrisable locally m-convex sesqualgebra which is not complete, and its completion is the Fréchet m-sesqualgebra $\mathcal{O}(\mathbb{C})$ of entire functions with the product $f \star g = f\bar g$; the case is the locally convex analogue of the theorem, where the completion is taken in the locally convex uniformity rather than in a norm. The example shows that the extension argument is not special to the normed case, the continuity of the product being what is used and not the norm.

## Summary

Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$ and let $\widehat{A}$ be the completion of the underlying normed space with canonical map $\iota$. Then $\widehat{A}$ is a **Banach sesqualgebra** over $(\mathbb{K},\varsigma)$: the product extends uniquely by uniform continuity on bounded sets, the extension is submultiplicative, additive in each variable, linear in the first slot and $\varsigma$-semilinear in the second, associative when $A$ is, and unital with the same unit; the **twisted action** extends, and the conjugate module commutes with completion, $\widehat{A^{\varsigma}} = \widehat{A}^{\varsigma}$; a continuous algebra involution extends uniquely, and when the sesquilinear product is the **derived operation** $x \star y = xy^{*}$, the derived operation of the completion is the extension of the derived operation of $A$; a continuous but non-isometric involution is made isometric by the normal form $\max(\lVert x\rVert,\lVert x^{*}\rVert)$, which commutes with the completion. The completion has the **universal property**: every continuous morphism into a complete Hausdorff sesqualgebra factors uniquely through $\iota$, so the completion is a **reflection** of the normed sesqualgebras into the Banach ones, it is a functor, and it is **idempotent**, $\widehat{\widehat{A}} \cong \widehat{A}$; the closure of zero is killed, so the completion depends only on the Hausdorff quotient. At $\varsigma = \mathrm{id}$ the theorem is the completion of a normed algebra and $\widehat{A}$ is its Banach algebra completion, and the completion of a full-type object with a nontrivial involution is never a Banach algebra. The examples are the finite-rank operators completing to the compact operators, the finitely supported sequences completing to $\ell^{1}$, and the polynomials completing to the entire functions.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\widehat{A}$ | the completion of the normed sesqualgebra $A$ |
| $\iota : A \to \widehat{A}$ | the canonical isometric morphism with dense image |
| $\widehat{A^{\varsigma}} = \widehat{A}^{\varsigma}$ | the conjugate module commutes with completion |
| $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$ | the submultiplicative estimate, preserved by the extension |
| $\widehat{*}$ | the extended algebra involution |
| $\widehat{x} \star \widehat{y} = \widehat{x}\,\widehat{y}^{\widehat{*}}$ | the derived operation of the completion |
| $\max(\lVert x\rVert,\lVert x^{*}\rVert)$ | the normal form making a continuous involution isometric, commuting with completion |
| $h \circ \iota = g$ | the universal property: continuous morphisms into complete objects factor |
| $\widehat{\widehat{A}} \cong \widehat{A}$ | idempotence |
| $\varsigma = \mathrm{id}$ | the collapse: the completion of a normed algebra |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the completion of a normed space, its universal property and the reflection into the complete spaces.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the completion of a normed algebra and the extension of the product and the involution.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume I* (Cambridge University Press, 1994), for the extension of an involution to the completion and the normal form of a continuous involution.
- Nicolas Bourbaki, *General Topology, Chapters 1–4* (Springer, 1989), for the completion of a uniform space and the universal property that the article reads for the sesquilinear structure.
- Maria Fragoulopoulou, *Topological Algebras with Involution* (North-Holland, 2005), for the completion of locally convex and locally m-convex algebras with involution.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the completion of the ternary product and the $J^{*}$-algebra structures it defines.
