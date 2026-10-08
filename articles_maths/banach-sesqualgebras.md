# __Banach Sesqualgebras__

## Introduction

The entry of the category, *Topological Sesqualgebras*, takes the base an involutive topological ring, the module a topological module and the product separately continuous, and it records that joint continuity is in general stronger and that in the complete normed case the two agree. This article develops that case, the sesquilinear counterpart of the normed and complete section of *Topological Algebras and Banach Algebras*: the base is a complete valued field with a continuous involution, the module is a normed space, the product is submultiplicative, and the object is complete.

The one new ingredient with respect to the bilinear layer is the norm on the conjugate module. The norm is a norm on the twisted module exactly when the involution $\varsigma$ of the base is isometric, and over $\mathbb{R}$ and $\mathbb{C}$ every continuous involution is isometric, so the hypothesis is free in the cases the layer uses. With it, the second slot of the product is an honest normed slot: the product is a jointly continuous bilinear map $A \times A^{\varsigma} \to A$ of normed spaces, and the separately continuous hypothesis of the layer is seen to cost nothing. Submultiplicativity is the axiom that makes this work, and it is the analogue of the axiom of *Topological Algebras and Banach Algebras*, §*Normed Algebras*.

Three facts organise the article. A normed sesqualgebra is a normed space with a submultiplicative product, $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$, linear in the first slot and $\varsigma$-semilinear in the second, and submultiplicativity gives the joint continuity of the product, hence the separate continuity, so every normed sesqualgebra is an object of the layer and the layer's general hypothesis is automatic here. The standard model is the derived operation $x \star y = xy^{*}$ of an involutive Banach algebra whose involution is isometric, where submultiplicativity of $\star$ is the submultiplicativity of the algebra product read through the isometry; the unit is a right unit of $\star$ and not a left one, because $x \star 1 = x$ while $1 \star x = x^{*}$. And at $\varsigma = \mathrm{id}$ the object is a normed or Banach algebra, so a Banach sesqualgebra of full type with a nontrivial involution is never a Banach algebra, the obstruction being the scalar rule and not the norm.

The article defines the normed and the Banach objects, proves the submultiplicative estimate and its consequences, reads the norm on the conjugate module, treats the derived operation of an involutive Banach algebra, reads the unit, and proves the collapse. It names no form and says nothing about the norms that a form defines: the completion of the normed object is *The Completion of a Sesqualgebra*, the locally convex weakening is *Fréchet and Locally Convex Sesqualgebras*, the operator theory of the bounded one-sided multiplications is *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*, and the continuity of the two involutions is *The Continuity of the Involution*. Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ with its usual absolute value, $\varsigma$ a continuous involution of $\mathbb{K}$, $A$ a normed $\mathbb{K}$-space, and the norms are submultiplicative and normalised by $\lVert 1\rVert = 1$ when there is a unit.

## The Normed Object

### The Definition

**Definition.** Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $\varsigma$ be a continuous involution of $\mathbb{K}$. A **normed sesqualgebra** over $(\mathbb{K},\varsigma)$ is a normed $\mathbb{K}$-space $A$ with a product, additive in each variable, such that

$$
\lVert xy\rVert \leq \lVert x\rVert\,\lVert y\rVert, \qquad (\lambda x)y = \lambda(xy), \qquad x(\lambda y) = \varsigma(\lambda)(xy)
$$

for all $x, y \in A$ and $\lambda \in \mathbb{K}$. A **Banach sesqualgebra** is a normed sesqualgebra which is complete for the norm.

The definition is *Topological Sesqualgebras*, §*The Definition* with the topology specialised to the norm topology, and the three displayed demands are the axioms of *Topological Algebras and Banach Algebras*, §*Normed Algebras* with the second scalar rule twisted. The product is not assumed associative, commutative or unital, and no form is named.

**Remark (the norm is not a form).** The article uses **norm** in the analytic sense alone. The quadratic form $h(x,x)$ that a Hermitian form defines is a different object, it need not be positive definite, and where it is positive definite the analytic norm it defines is the subject of *The Norm Defined by a Form*, in the form category. A sesqualgebra of this article may carry no form, and the selection of the examples below is made on the algebra and the norm and not on a pairing.

### The Submultiplicative Estimate

**Theorem (the product is jointly continuous).** Let $A$ be a normed sesqualgebra. Then the product is jointly continuous: if $x_n \to x_0$ and $y_n \to y_0$ then $x_ny_n \to x_0y_0$.

*Proof.* Additivity in each variable gives

$$
\lVert x_ny_n - x_0y_0\rVert = \lVert x_n(y_n - y_0) + (x_n - x_0)y_0\rVert \leq \lVert x_n - x_0\rVert\lVert y_n\rVert + \lVert x_0\rVert\lVert y_n - y_0\rVert ,
$$

by submultiplicativity and the triangle inequality; the sequence $(y_n)$ is bounded and the two differences tend to $0$, so the sum tends to $0$. $\square$

**Corollary (the two notions of continuity coincide).** Every normed sesqualgebra is an object of the layer *Topological Sesqualgebras*, with the separately continuous product required there, and the separate and the joint hypotheses of the layer are the same hypothesis. In particular the left and the right multiplication $L_a(x) = ax$ and $R_a(x) = xa$ are continuous for every $a$.

*Proof.* Joint continuity implies separate continuity, so $A$ satisfies the definition of the layer, whose topology is the norm topology and whose base involution is continuous by hypothesis. The two hypotheses of the layer coincide because the stronger one is automatic, which is the ambiguity recorded in *Topological Sesqualgebras*, §*Joint Continuity*. The continuity of $L_a$ and $R_a$ is the separate continuity, and it is the statement of *Topological Sesqualgebras*, §*The One-Sided Multiplications*. $\square$

**Remark (submultiplicativity is an axiom).** The estimate is not a theorem about a product that happens to satisfy the scalar rules; a product on a normed space may satisfy the two scalar rules and still be discontinuous, and then the object is a normed space with a product that is not an object of the layer. The axiom $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$ is the compatibility of the norm with the product, and it is exactly what passes to the completion.

## The Norm on the Conjugate Module

### The Isometric Involution

**Theorem (the twisted action is isometric).** Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $\varsigma$ be a continuous involution of $\mathbb{K}$. Then $\varsigma$ is isometric, $\lvert\varsigma(\lambda)\rvert = \lvert\lambda\rvert$ for every $\lambda$, and the twisted action $\lambda \cdot x = \varsigma(\lambda)x$ of *Topological Sesqualgebras*, §*The Conjugate Module* satisfies

$$
\lVert \lambda \cdot x\rVert = \lvert\varsigma(\lambda)\rvert\,\lVert x\rVert = \lvert\lambda\rvert\,\lVert x\rVert .
$$

Consequently the conjugate module $A^{\varsigma}$ is a normed $\mathbb{K}$-space with the norm of $A$, the identity $A \to A^{\varsigma}$ is an isometry, and it is $\mathbb{K}$-linear exactly when $\varsigma = \mathrm{id}$.

*Proof.* Over $\mathbb{R}$ the identity is the only involution, and it is isometric. Over $\mathbb{C}$ a continuous involution of the field is either the identity or the conjugation: an involution of $\mathbb{C}$ is a field automorphism of order two, its fixed field is $\mathbb{R}$ when it is not the identity, by *Involutive Topological Rings and Fields*, §*Topological Fields with Involution*, and a continuous automorphism of $\mathbb{C}$ fixing $\mathbb{R}$ is the identity or the conjugation. The identity is isometric, and the conjugation satisfies $\lvert\bar\lambda\rvert = \lvert\lambda\rvert$ by the definition of the modulus of a complex number. The homogeneity of the norm of the conjugate module is the displayed computation, and the identity is a linear isometry onto its image in all cases; it is $\mathbb{K}$-linear exactly when $\varsigma(\lambda)x = \lambda x$ for every $\lambda$ and $x$, which for $x \neq 0$ is $\varsigma = \mathrm{id}$. $\square$

**Remark.** The theorem is the reason a normed sesqualgebra carries a norm on both of its two modules: $A$ and $A^{\varsigma}$ are the same normed space with two actions, and the identity between them is an isometry that is semilinear and not linear. Without the isometry of $\varsigma$ the twisted action would have a bound but not a norm, and the normed theory of the second slot would require a modification of the norm of $A$; over $\mathbb{R}$ and $\mathbb{C}$ this never happens.

### The Second Slot

**Theorem (the product is bilinear and jointly continuous on the pair).** Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$. Read as a map $A \times A^{\varsigma} \to A$, the product is $\mathbb{K}$-bilinear and satisfies

$$
\lVert xy\rVert \leq \lVert x\rVert\,\lVert y\rVert
$$

with the norm of $A$ on the first factor and the norm of $A^{\varsigma}$ on the second; it is jointly continuous.

*Proof.* The bilinearity is *Topological Sesqualgebras*, §*The Two Slots*, and the estimate is the submultiplicative axiom, the norm of $A^{\varsigma}$ being the norm of $A$ and the twisted scalar multiplying by $\varsigma(\lambda)$ of the same modulus. Joint continuity is the corollary above. $\square$

**Corollary (the left and the right multiplication are bounded).** Let $a \in A$. Then $L_a$ is a bounded $\varsigma$-semilinear operator with $\lVert L_a\rVert \leq \lVert a\rVert$, and $R_a$ is a bounded $\mathbb{K}$-linear operator with $\lVert R_a\rVert \leq \lVert a\rVert$.

*Proof.* The parities are *Topological Sesqualgebras*, §*The One-Sided Multiplications*, and the bounds are the submultiplicative estimate applied to $\lVert ax\rVert$ and $\lVert xa\rVert$, the operator norm being the supremum over $\lVert x\rVert \leq 1$. $\square$

## The Banach Object

### Completeness

**Theorem (the Banach object).** Let $A$ be a Banach sesqualgebra. Then $A$ is a complete object of the layer *Topological Sesqualgebras*, its conjugate module $A^{\varsigma}$ is a Banach space with the norm of $A$, and the product on the pair, the two one-sided multiplications and the twisted action are continuous.

*Proof.* Completeness is the hypothesis, and the normed $\mathbb{K}$-space $A^{\varsigma}$ is complete because it is $A$ with the same norm and the same additive uniformity, the twisted action differing only in the scalars. The continuity statements are the theorems of the two preceding sections. $\square$

**Remark (the norm is unique only up to equivalence).** Two submultiplicative norms on the same sesqualgebra that define the same topology define the same layer, because the layer sees the topology and not the norm; for a finite-dimensional object over a complete valued field all norms are equivalent, by *Normed and Banach Spaces*, §*Equivalence of Norms*, so the normed layer on a finite-dimensional sesqualgebra is unique. The non-uniqueness is real in infinite dimension: the operator norm and the normalised submultiplicative norm of *Topological Algebras and Banach Algebras*, §*Normed Algebras* define the same topology on a unital algebra and differ by a constant.

### The Derived Operation of an Involutive Banach Algebra

**Theorem (the standard model).** Let $B$ be a Banach algebra over $\mathbb{K}$ with an isometric $\varsigma$-semilinear involution $*$, and put $x \star y = xy^{*}$. Then $B$ with the product $\star$ and the norm of $B$ is a Banach sesqualgebra over $(\mathbb{K},\varsigma)$, the algebra product being the **envelope** of the sesquilinear product.

*Proof.* The product $\star$ is additive in each variable, and

$$
\lVert x \star y\rVert = \lVert xy^{*}\rVert \leq \lVert x\rVert\,\lVert y^{*}\rVert = \lVert x\rVert\,\lVert y\rVert,
$$

submultiplicativity of the algebra product and the isometry of the involution. The first scalar rule is $(\lambda x) \star y = (\lambda x)y^{*} = \lambda(xy^{*})$, and the second is $x \star (\lambda y) = x(\lambda y)^{*} = \varsigma(\lambda)xy^{*} = \varsigma(\lambda)(x \star y)$ by the semilinearity of $*$. Completeness is the hypothesis on $B$. $\square$

**Corollary (the model covers every involutive Banach algebra).** Every Banach algebra with an isometric involution is a Banach sesqualgebra under its derived operation, and the involution of the layer is the involution of the algebra. The derived operation $x \star y = xy^{*}$ and the algebra product $xy$ coincide exactly when the involution is trivial, $* = \mathrm{id}$; then also $\varsigma = \mathrm{id}$ and the object has collapsed to a Banach algebra.

**Remark (the normal form removes the hypothesis on the algebra involution).** A continuous involution that is not isometric is replaced by the isometric one for the equivalent norm $\lVert x\rVert_{*} = \max(\lVert x\rVert,\lVert x^{*}\rVert)$ of *The Continuity of the Involution*, §*The Normal Form of a Continuous Involution*; the norm is submultiplicative and defines the same topology, so the hypothesis of the theorem costs nothing beyond the continuity of the involution, which is the standing hypothesis of the layer.

### The Unit

**Proposition (the unit is a right unit of the derived operation).** Let $B$ be a unital Banach algebra with an isometric involution $*$ and let $\star$ be its derived operation. Then

$$
x \star 1 = x, \qquad 1 \star x = x^{*},
$$

so $1$ is a right unit and not a left unit of $\star$ unless $* = \mathrm{id}$, and $\lVert 1\rVert = 1$ if the norm is normalised.

*Proof.* By definition $x \star 1 = x1^{*} = x$ and $1 \star x = 1x^{*} = x^{*}$. The two agree for every $x$ exactly when $* = \mathrm{id}$, and the norm is normalised by the standing convention. $\square$

**Remark.** The asymmetry is the algebraic one of *Units and the Unitary Elements*: the unit of the algebra is a right unit of the sesquilinear product and the left multiplication by the unit is the involution. It is the smallest instance of the failure of associativity of the layer, and it is the reason the derived operation has no two-sided unit when the involution is nontrivial.

## The Collapse at the Trivial Involution

### The Collapse

**Theorem (the collapse of the normed layer).** Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$ with $\varsigma = \mathrm{id}$. Then the two scalar rules coincide, the product is $\mathbb{K}$-bilinear, $A^{\varsigma} = A$ as a normed space with the same action, and $A$ is a normed algebra over $\mathbb{K}$ in the sense of *Topological Algebras and Banach Algebras*, §*Normed Algebras*; if $A$ is complete it is a Banach algebra. Conversely every normed algebra is a normed sesqualgebra over $(\mathbb{K},\mathrm{id})$, so the two categories are the same.

*Proof.* With $\varsigma = \mathrm{id}$ the second rule reads $x(\lambda y) = \lambda(xy)$ and is the first; the twisted action is the ordinary action, so the conjugate module is the module and the identity is linear. The submultiplicative axiom and the completeness are those of a normed or Banach algebra. Conversely a normed algebra satisfies all the axioms of a normed sesqualgebra over $(\mathbb{K},\mathrm{id})$. $\square$

### The Objects of Full Type

**Theorem (objects of full type).** Let $A$ be a Banach sesqualgebra of **full type** in the sense of *Sesqualgebras*, §*The Collapse at the Identity*: faithful over $\mathbb{K}$, with products generating $A$ and no nonzero element annihilating $A$ on the left. If $\varsigma \neq \mathrm{id}$ then $A$ is neither associative nor commutative, and in particular it is not a Banach algebra.

*Proof.* The algebraic collapse theorem of *Sesqualgebras*, §*The Collapse at the Identity* applies to the scalars and the product alone and is unchanged by the norm, exactly as *Topological Sesqualgebras*, §*The Objects of Full Type* records for the topological layer; its conclusion is that the associativity or the commutativity of the product forces $\varsigma = \mathrm{id}$. $\square$

**Remark.** The theorem is the reason the normed layer is not a reparametrisation of the normed algebras: the obstruction to being an algebra is a scalar rule, it is present whether the norm is complete or not, and it is what the derived operation of an involutive Banach algebra exhibits. The norm contributes the convergence of the power series, which the later entries of the category read.

## Examples

### The Field and the Matrices

**Example (the field, verdict: a Banach sesqualgebra with a multiplicative norm).** Let $A = \mathbb{C}$ with the modulus, $\varsigma$ the conjugation and the product $z \star w = z\bar w$. Then $\lvert z \star w\rvert = \lvert z\rvert\lvert w\rvert$, the two scalar rules hold, and $\mathbb{C}$ is a Banach sesqualgebra whose norm is multiplicative and whose product is neither associative nor commutative. It is the field example of *Examples of Sesqualgebras*, §*The Field with Its Involution*, read with the modulus.

**Example (the complex matrices, verdict: the operator norm and the dagger).** Let $A = M_n(\mathbb{C})$ with the operator norm, $\varsigma$ the conjugation and the product $S \star T = ST^{*}$. Then $A$ is a unital Banach algebra with the isometric involution the conjugate transpose, so the theorem of §*The Derived Operation of an Involutive Banach Algebra* makes it a Banach sesqualgebra; it satisfies the $\mathrm{C}^{*}$-identity $\lVert S^{*}S\rVert = \lVert S\rVert^{2}$, so the involution is isometric with no normal form needed. The product is not associative for $n \geq 2$: the matrix-unit witness of *Matrix Sesqualgebras*, §*The Two Products* is $(E_{22} \star E_{12}) \star E_{11} = E_{21} \neq 0 = E_{22} \star (E_{12} \star E_{11})$. The verdict: the standard finite-dimensional model, with every hypothesis automatic.

**Example (the non-isometric involution, verdict: the normal form is needed).** Let $A = M_n(\mathbb{R})$ with the transpose and the norm $\lVert X\rVert_{T} = \lVert TXT^{-1}\rVert$ of *The Continuity of the Involution*, §*Examples*, for an invertible $T$. The involution is continuous, being linear in finite dimension, and isometric only when $T$ is orthogonal up to a scalar; for the equivalent submultiplicative norm $\max(\lVert X\rVert_{T},\lVert X^{\mathsf{T}}\rVert_{T})$ it is isometric and the derived operation $X \star Y = XY^{\mathsf{T}}$ is submultiplicative. The example is the witness that the isometry in the theorem on the derived operation is a real hypothesis on the chosen norm and not a formal one, and that the normal form removes it.

### The Function Algebras

**Example (the continuous functions, verdict: a Banach sesqualgebra of functions).** Let $X$ be a compact Hausdorff space and let $A = C(X,\mathbb{C})$ with the supremum norm, the involution $\sigma(f) = \bar f$ relative to the conjugation of the scalars, and the product $f \star g = f\,\sigma(g)$. Then $\lVert f \star g\rVert_{\infty} \leq \lVert f\rVert_{\infty}\lVert g\rVert_{\infty}$, the involution is isometric; the object is a Banach sesqualgebra which is neither associative nor commutative, and its envelope is the Banach algebra $C(X,\mathbb{C})$. This is the analytic model of the field example, and it is the infinite-dimensional case of the layer.

**Example (the group algebra, verdict: isometric involution without the $\mathrm{C}^{*}$-identity).** Let $G$ be a locally compact group and let $A = L^{1}(G)$ with the convolution product, the involution $f^{*}(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the $L^{1}$-norm. The involution is isometric, $\lVert f^{*}\rVert_{1} = \lVert f\rVert_{1}$, hence continuous, so $A$ is a Banach algebra with an isometric involution and the derived operation $f \star g = f * g^{*}$ makes it a Banach sesqualgebra; for $G = \mathbb{R}$ the norm is not a $\mathrm{C}^{*}$-norm, the $\mathrm{C}^{*}$-identity failing, as recorded in *The Involution and the Spectral Radius*, §*Examples*. The verdict: the continuity of the involution may come from an isometry which is not a $\mathrm{C}^{*}$-identity, so the layer's hypothesis is strictly weaker than the $\mathrm{C}^{*}$-case.

### The Completeness of the Model

**Example (a normed sesqualgebra that is not complete, verdict: the completion is needed).** Let $A$ be the space of finite-rank operators on the separable Hilbert space with the operator norm, the involution the adjoint and the product $S \star T = ST^{*}$. The submultiplicative estimate holds, by the estimate of the derived operation and the isometry of the adjoint, and $A$ is a normed sesqualgebra which is not complete; its completion is the Banach sesqualgebra of compact operators with the same product, by *The Completion of a Sesqualgebra*, §*Examples*. The example is the witness that completeness is a genuine hypothesis and that it is recovered by completion.

## Summary

A **normed sesqualgebra** over $(\mathbb{K},\varsigma)$ is a normed $\mathbb{K}$-space with a product additive in each variable, submultiplicative, $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$, linear in the first slot and $\varsigma$-semilinear in the second; a **Banach sesqualgebra** is one that is complete. Submultiplicativity gives the joint continuity of the product, hence the separate continuity, so every normed sesqualgebra is an object of the layer *Topological Sesqualgebras* and the layer's separate hypothesis is automatic here; the one-sided multiplications are bounded with $\lVert L_a\rVert, \lVert R_a\rVert \leq \lVert a\rVert$. The involution $\varsigma$ of $\mathbb{K}$ is isometric, being the identity over $\mathbb{R}$ and the identity or the conjugation over $\mathbb{C}$, so the **conjugate module** $A^{\varsigma}$ is a normed space with the norm of $A$ and the product is a jointly continuous bilinear map $A \times A^{\varsigma} \to A$. The standard model is the **derived operation** $x \star y = xy^{*}$ of an involutive Banach algebra with an isometric involution: submultiplicativity of $\star$ is the estimate $\lVert xy^{*}\rVert \leq \lVert x\rVert\lVert y\rVert$ read through the isometry, and where the involution is continuous but not isometric it is made isometric by the equivalent norm $\max(\lVert x\rVert,\lVert x^{*}\rVert)$. The unit of the algebra is a **right unit** of the derived operation, $x \star 1 = x$, and the left multiplication by the unit is the involution, $1 \star x = x^{*}$, so the derived operation has no two-sided unit when the involution is nontrivial. At $\varsigma = \mathrm{id}$ the product is bilinear and the object is a normed or Banach algebra, so the category **collapses**, and a Banach sesqualgebra of **full type** with a nontrivial involution is neither associative nor commutative, hence not a Banach algebra; the examples are the field with the modulus, the complex matrices with the operator norm and the dagger, the non-isometric involution that needs the normal form, the continuous functions and the group algebra, and the finite-rank operators, whose completion is the compact operators.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$ with its usual absolute value |
| $\varsigma$ | the continuous involution of $\mathbb{K}$: the identity, or the conjugation over $\mathbb{C}$ |
| $A$ | a normed or Banach sesqualgebra over $(\mathbb{K},\varsigma)$ |
| $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$ | the submultiplicative axiom, which gives joint continuity |
| $A^{\varsigma}$ | the conjugate module, a normed space with the norm of $A$ via the isometry of $\varsigma$ |
| $L_a$, $R_a$ | the one-sided multiplications, bounded with norm at most $\lVert a\rVert$ |
| $x \star y = xy^{*}$ | the derived operation of an involutive Banach algebra |
| $\lVert x\rVert_{*} = \max(\lVert x\rVert,\lVert x^{*}\rVert)$ | the normal form making a continuous involution isometric |
| $\lVert x^{*}x\rVert = \lVert x\rVert^{2}$ | the $\mathrm{C}^{*}$-identity, which makes both slots isometric with no normal form |
| full type | faithful over $\mathbb{K}$, products generating $A$, no nonzero left annihilator |
| $\varsigma = \mathrm{id}$ | the collapse: the object is a normed or Banach algebra |

## Further Reading

- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the normed and complete algebras, the submultiplicative axiom and the involutions that the derived operation uses.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume I* (Cambridge University Press, 1994), for the standard examples of Banach algebras with an isometric involution.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume II* (Cambridge University Press, 2001), for the $\mathrm{C}^{*}$-identity, the uniqueness of the $\mathrm{C}^{*}$-norm and the group algebras.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the operator norm, the norm on the conjugate module and the finite-dimensional models.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the normed spaces, their completions and the duality that the conjugate dual of the layer uses.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the ternary product and the normed $J^{*}$-structures that the derived operation forces.
