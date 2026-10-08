# __The Sesquilinear Product__

## Introduction

A **sesquilinear product** on an $R$-module $A$ is a two-variable map $\star : A \times A \to A$ that is additive in each variable, $R$-linear in the first variable and $\varsigma$-semilinear in the second, where $\varsigma$ is an involution of $R$ (an additive map with $\varsigma(1) = 1$, $\varsigma(ab) = \varsigma(b)\varsigma(a)$ and $\varsigma^{2} = \mathrm{id}$, as in *Sesqualgebras*). Beyond additivity the whole definition is the pair of scalar rules

$$
(\lambda x) \star y = \lambda (x \star y), \qquad x \star (\lambda y) = \varsigma(\lambda) (x \star y) .
$$

This article is the calculus of the product itself: what the two rules force for a product of combinations, how the product becomes an ordinary bilinear map once one copy of the module is conjugated, what the conjugate of a product is, how the transposed product $y \star x$ compares with $x \star y$, and how the one-sided products $a \star x$ and $x \star a$ move the scalars. The module carrying the product, its ideals, its units and its examples are the subject of *Sesqualgebras*; here the module is fixed and only the product is computed with.

Throughout, $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and the product is written $\star$. When the product is the **derived operation** $x \star y = xy^{*}$ of an associative algebra with a $\varsigma$-semilinear involution $*$, the algebra's own product is written by juxtaposition, $xy$, so that the two products are told apart; that case is the standard one and supplies the examples.

## The Axioms of the Product

### Additivity and the Two Rules

**Definition.** The product is **additive in each variable** when $(x + y) \star z = x \star z + y \star z$ and $x \star (y + z) = x \star y + x \star z$ for all $x, y, z$, and it satisfies the two scalar rules above. A product that is additive in each variable and satisfies the two rules is a **$\varsigma$-sesquilinear product**.

**Proposition.** The product vanishes on a zero argument and is homogeneous of degree one in each argument: for all $x, y$,

$$
0 \star x = x \star 0 = 0, \qquad (-x) \star y = x \star (-y) = -(x \star y),
$$

and additivity in each variable extends to finite sums.

**Proof.** Put $x = 0$ and $y = 0$ in the two distributive laws and use the uniqueness of the neutral element; then put $y = -x$ in $(x + y) \star z = x \star z + y \star z$ and use $0 \star z = 0$. The finite-sum form is induction on the number of terms. $\square$

**Remark.** Nothing beyond additivity and the two rules is assumed. The product need not be associative, commutative or unital, and there need not be an involution on $A$ itself; those further data are named where they are used, and the associativity-free part of the theory is exactly the part computed in this article.

### The Rule of the Scalars of a Product

**Proposition (the scalars of a product).** For all $\lambda, \mu \in R$ and all $x, y \in A$,

$$
(\lambda x) \star (\mu y) = \lambda \, \varsigma(\mu) \, (x \star y) .
$$

More generally, for finite families,

$$
\Bigl( \sum_i \lambda_i x_i \Bigr) \star \Bigl( \sum_j \mu_j y_j \Bigr) = \sum_{i,j} \lambda_i \, \varsigma(\mu_j) \, (x_i \star y_j) .
$$

**Proof.** $(\lambda x) \star (\mu y) = \lambda \bigl( x \star (\mu y) \bigr) = \lambda \, \varsigma(\mu) (x \star y)$, by the first and then the second rule. The general form is this formula applied term by term, additivity carrying the sums through. $\square$

**Corollary (structure constants).** Suppose $A$ is free with basis $(e_i)_{i \in I}$. Writing $e_i \star e_j = \sum_k c_{ij}^{k} e_k$, the product of two elements $x = \sum_i \lambda_i e_i$ and $y = \sum_j \mu_j e_j$ is

$$
x \star y = \sum_{i,j,k} \lambda_i \, \varsigma(\mu_j) \, c_{ij}^{k} \, e_k .
$$

Conversely, for any family of scalars $c_{ij}^{k}$ the last formula defines a $\varsigma$-sesquilinear product on $A$. So on a free module with a finite basis of $n$ elements the $\varsigma$-sesquilinear products are exactly the $n^{3}$-tuples of scalars, with no condition on the tuple; associativity is not assumed, and it would impose conditions on the tuple.

**Proof.** The first statement is the general scalar rule. For the converse, the formula is additive in each of $\lambda_i$ and $\mu_j$, and reading off the two rules gives $(\lambda x) \star y = \lambda (x \star y)$ from the left slot and $x \star (\mu y) = \varsigma(\mu)(x \star y)$ from the right slot; so the axioms hold without any constraint among the $c_{ij}^{k}$. $\square$

**Remark.** The scalars of the left factor pass through unchanged and the scalars of the right factor come out conjugated. This is the precise sense in which the product is not bilinear: a bilinear product would give $\lambda \mu$, and the rule $\lambda \, \varsigma(\mu)$ is what replaces it.

### The Product as a Bilinear Map on the Pair

**Definition.** The **conjugate module** $A^{\varsigma}$ is the additive group $A$ with the twisted scalar action $\lambda \cdot x = \varsigma(\lambda) x$; the definition and its properties are in *Sesqualgebras*.

**Theorem (the product is bilinear on the pair).** The product, read as a map $A \times A^{\varsigma} \to A$, is $R$-bilinear in the two variables.

**Proof.** In the first variable, $(\lambda x) \star y = \lambda (x \star y)$ is the first rule, and the scalar $\lambda$ acts on the output in $A$. In the second variable, $x \star (\lambda \cdot y) = x \star (\varsigma(\lambda) y) = \varsigma(\varsigma(\lambda)) (x \star y) = \lambda (x \star y)$, the second rule being used once and $\varsigma^{2} = \mathrm{id}$ once. Additivity in each variable is the definition of the product. $\square$

**Remark.** The theorem looks like a tautology and is not. The output lies in $A$ with the **original** scalar action, not the twisted one, so the scalar that the second rule conjugates is returned unconjugated only because $\varsigma$ has order two. Conjugation is a functorial involution on the objects, $(A^{\varsigma})^{\varsigma} = A$, and this reformulation — a $\varsigma$-sesquilinear product is the same thing as an $R$-bilinear map $A \times A^{\varsigma} \to A$ — is the working definition of the category.

## The Conjugate of a Product

### The Conjugate Module

**Proposition.** $A^{\varsigma}$ is an $R$-module, the identity $A \to A^{\varsigma}$ is $\varsigma$-semilinear, and $A^{\varsigma\varsigma} = A$.

**Proof.** The action is additive in $x$ and $\lambda \cdot (\mu \cdot x) = (\mu \lambda) \cdot x$ because $\varsigma$ is multiplicative and $\varsigma^{2} = \mathrm{id}$; the remaining clauses are the definition. $\square$

### The Conjugate of a Product

**Proposition (conjugation reverses the star-product).** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, and let $x \star y = xy^{*}$ be the derived operation. Then

$$
(x \star y)^{*} = y \star x .
$$

**Proof.** $(x \star y)^{*} = (xy^{*})^{*} = (y^{*})^{*} x^{*} = y x^{*} = y \star x$, using $(uv)^{*} = v^{*} u^{*}$ and $*^{2} = \mathrm{id}$. $\square$

**Corollary.** The involution carries the star-product to the same star-product with the two factors exchanged, so conjugating a product and transposing it are the same operation.

**Remark.** The plain product obeys the anti-automorphism rule $(xy)^{*} = y^{*} x^{*}$; the star-product obeys the same rule with $\star$ in place of the product, $(x \star y)^{*} = y \star x$. So the same involution $*$ is an anti-automorphism for the star-product as well as for the plain product: the star-product is not a second kind of object but the plain product read through $*$.

**Remark (the boundary).** A general $\varsigma$-sesquilinear product carries no involution on $A$, so there is no conjugate $x^{*}$ and hence no conjugate of a product: the conjugate **module** $A^{\varsigma}$ always exists, the conjugate of a product exists only for the derived operation of an involutive algebra. The distinction is the reason *Anti-Automorphisms Twisted by the Base Involution* treats the involution as extra data.

## The Transposed Product

### The Transposed Product and the Difference

**Definition.** The **transposed product** of $x$ and $y$ is $y \star x$, and the **difference** is the bracket

$$
[x, y]_{\varsigma} = x \star y - y \star x .
$$

**Proposition (the transposed product has the opposite parity).** The map $(x, y) \mapsto y \star x$ is $\varsigma$-semilinear in the first variable and $R$-linear in the second, so it is $R$-bilinear as a map $A^{\varsigma} \times A \to A$, with the conjugate module in the first factor. It is a $\varsigma$-sesquilinear product of the original parity only when the twist is invisible, that is when $\varsigma = \mathrm{id}$ or $\bigl(\varsigma(\lambda) - \lambda\bigr)(y \star x) = 0$ for all $\lambda, y, x$, the degenerate case of *Sesqualgebras* again.

**Proof.** In the first slot, $y \star (\lambda x) = \varsigma(\lambda)(y \star x)$, which is semilinearity; in the second slot, $(\lambda y) \star x = \lambda(y \star x)$, which is linearity. Reading the first slot with the twisted action of $A^{\varsigma}$ makes the map $R$-bilinear, exactly as the theorem that the product is bilinear on the pair. Semilinearity and linearity in the first slot agree only when $\varsigma = \mathrm{id}$. $\square$

**Remark.** The parity of the transposed product is the reverse of the parity of the product: the product is the bilinear map $A \times A^{\varsigma} \to A$, the transposed product the bilinear map $A^{\varsigma} \times A \to A$. The reversal is the product-level form of the asymmetry of the opposite algebra of *Sesqualgebras*, where the conjugate module comes into the first factor rather than the second.

**Proposition.** $[x, y]_{\varsigma} = -[y, x]_{\varsigma}$ and $[x, x]_{\varsigma} = 0$.

**Proof.** Both statements are the antisymmetry of the subtraction. $\square$

**Theorem (when transposition changes nothing).** Let $A$ be a unital associative $R$-algebra with a $\varsigma$-semilinear involution $*$, and let $\star$ be the derived operation. Then $x \star y = y \star x$ for all $x, y$ if and only if $* = \mathrm{id}$ and the product of $A$ is commutative.

**Proof.** If $x \star y = y \star x$ for all $x, y$, put $y = 1$ and use $1^{*} = 1$: then $x = x \star 1 = 1 \star x = x^{*}$ for every $x$, so $*$ is the identity; the product is then the original one, and $x \star y = y \star x$ is its commutativity. Conversely, if $* = \mathrm{id}$ then $\star$ is the original product, which is transposition-invariant exactly when $A$ is commutative. $\square$

**Corollary (the faithful case).** If $A$ is faithful over $R$, then $* = \mathrm{id}$ forces $\varsigma = \mathrm{id}$: the compatibility $(\lambda x)^{*} = \varsigma(\lambda) x^{*}$ with $* = \mathrm{id}$ gives $(\lambda - \varsigma(\lambda)) x = 0$ for every $\lambda$ and every $x$, and faithfulness gives $\lambda = \varsigma(\lambda)$. So for an algebra of full type with $\varsigma \neq \mathrm{id}$ the involution $*$ on $A$ is nontrivial, and the transposed product always differs from the product. The converse does not hold: $\varsigma = \mathrm{id}$ does not force $* = \mathrm{id}$, and on the commutative algebra $\mathbb{C} \times \mathbb{C}$ the swap $(z, w) \mapsto (w, z)$ is a $\mathbb{C}$-linear involution of order two whose derived operation $x \star y = xy^{*}$ is not transposition-invariant. The sharp criterion stays $* = \mathrm{id}$ and $A$ commutative.

**Remark (faithfulness cannot be dropped).** Without faithfulness the involution on $A$ can be the identity while the base involution is not. Take $R = \mathbb{Q}[\varepsilon]/(\varepsilon^{2})$ with $\varsigma(\varepsilon) = -\varepsilon$ and $A = R/(\varepsilon) = \mathbb{Q}$ with its usual multiplication and $* = \mathrm{id}$. Then $*$ is $\varsigma$-semilinear, because $\varepsilon$ acts as $0$ on $A$ and $\varepsilon$ is the only place where $\varsigma$ differs from the identity; the product is commutative, hence transposition-invariant, and $\varsigma \neq \mathrm{id}$. The involution is the identity only modulo $\operatorname{ann}_{R}(A)$, which is the honest conclusion in the absence of faithfulness, in agreement with *The Collapse at the Identity*. For an algebra of full type with $\varsigma \neq \mathrm{id}$ the transposed product therefore always differs from the product, and a genuine sesquilinear product is never symmetric.

### The Hermitian and the Skew-Hermitian Parts

**Proposition.** Let $\star$ be the derived operation of an algebra with a $\varsigma$-semilinear involution $*$, and suppose $2$ is invertible in $R$. Then the product splits as

$$
x \star y = \tfrac{1}{2}\bigl( x \star y + y \star x \bigr) + \tfrac{1}{2}\bigl( x \star y - y \star x \bigr),
$$

the symmetrised part $x \star y + y \star x$ is **Hermitian**, $(x \star y + y \star x)^{*} = x \star y + y \star x$, and the difference $x \star y - y \star x$ is **skew-Hermitian**, $(x \star y - y \star x)^{*} = -(x \star y - y \star x)$.

**Proof.** By the conjugate-of-a-product identity, $(x \star y)^{*} = y \star x$, so the conjugate of the symmetrised part is itself and the conjugate of the difference is its negative; the factor $\tfrac{1}{2}$ exists because $2$ is invertible. $\square$

**Remark.** The identity is the whole of the symmetry it states: the symmetrised part of the product is Hermitian and the difference is skew-Hermitian. It does not say more. In particular the difference $[x, y]_{\varsigma} = x \star y - y \star x$ is antisymmetric and takes skew-Hermitian values, but it satisfies no Jacobi identity in general, so it is not itself a Lie bracket; the bracket under which the skew-Hermitian elements form a Lie algebra is the ordinary commutator $xy - yx$, a different operation, treated in *The Sesquilinear Commutator* and *The Unitary Lie Algebra*. Likewise the symmetrised product $x \star y + y \star x = xy^{*} + yx^{*}$ is not the Jordan product $xy + yx$ of the algebra.

## The One-Sided Products

### The Left and the Right Product

**Definition.** For $a \in A$ the **left product** and the **right product** by $a$ are the maps

$$
L_{a}(x) = a \star x, \qquad R_{a}(x) = x \star a .
$$

**Proposition.** $L_{a}$ is $\varsigma$-semilinear and $R_{a}$ is $R$-linear. Equivalently, $L_{a}$ is $R$-linear as a map $A^{\varsigma} \to A$, and $R_{a}$ is $R$-linear as a map $A \to A$ and as a map $A^{\varsigma} \to A^{\varsigma}$.

**Proof.** $L_{a}(\lambda x) = a \star (\lambda x) = \varsigma(\lambda)(a \star x) = \varsigma(\lambda) L_{a}(x)$, so $L_{a}$ is $\varsigma$-semilinear; then $L_{a}(\lambda \cdot x) = L_{a}(\varsigma(\lambda) x) = \varsigma(\varsigma(\lambda)) L_{a}(x) = \lambda L_{a}(x)$, so $L_{a}$ is linear on the conjugate module. For $R_{a}$, $R_{a}(\lambda x) = (\lambda x) \star a = \lambda (x \star a) = \lambda R_{a}(x)$ by the first rule, and the same computation with $\lambda \cdot x$ shows that $R_{a}$ is linear for the twisted action as well. $\square$

**Remark.** The two one-sided products are two families of operators of opposite parity: the left products are conjugate-linear on $A$ and linear on $A^{\varsigma}$, the right products are linear on both. When the product is associative the left products turn $A$ into a left $A$-module and the right products into a right $A$-module, and these are the two module structures that the asymmetry of the slots produces; without associativity the two families are only families of operators, since $L_{a} \circ L_{b} = L_{a \star b}$ is the associative law. The operator theory is in *The Left and Right Multiplication Operators of a Sesqualgebra*.

### The Twisted Composition

**Proposition.** The composites $L_{a} \circ L_{b}$ and $R_{a} \circ R_{b}$ are $R$-linear: they are composites of two $\varsigma$-semilinear maps and of two linear maps respectively. When the product is associative, $L_{a} \circ R_{b} = R_{b} \circ L_{a}$.

**Proof.** For the composites, apply the parity twice: $\varsigma^{2} = \mathrm{id}$ returns a linear map from a composite of two conjugate-linear ones, and a composite of two linear ones is linear. The commutation of the two families is the associative law $(a \star x) \star b = a \star (x \star b)$, which is exactly the equality of $L_{a}R_{b}$ and $R_{b}L_{a}$ at every $x$. $\square$

**Remark.** A composite of two left products is linear while a single left product is conjugate-linear, so the left products form a representation of $A$ by linear operators only when the twist is invisible: $L_{a}$ is $R$-linear exactly when $\varsigma = \mathrm{id}$ or $(\lambda - \varsigma(\lambda)) a \star x = 0$ for all $\lambda$ and $x$, the condition of *Sesqualgebras*. The composition laws and the representation are read in *The Left and Right Multiplication Operators of a Sesqualgebra*, to which the present parity statement is the first input.

## Summary

A $\varsigma$-sesquilinear product is additive in each variable with $(\lambda x) \star y = \lambda(x \star y)$ and $x \star (\lambda y) = \varsigma(\lambda)(x \star y)$. The two rules force $(\lambda x) \star (\mu y) = \lambda \, \varsigma(\mu) (x \star y)$, so on a free module with a finite basis of $n$ elements the product is an $n^{3}$-tuple of structure constants with no condition among them, and the only difference from a bilinear product is the conjugated scalar of the right factor. Read on the conjugate module $A^{\varsigma}$, the product is an ordinary $R$-bilinear map $A \times A^{\varsigma} \to A$, the output keeping the original action; this is the working form of the definition. For the derived operation $x \star y = xy^{*}$ of an involutive algebra, conjugation reverses the product, $(x \star y)^{*} = y \star x$, so the symmetrised product is Hermitian and the difference skew-Hermitian. The transposed product $y \star x$ is of the opposite parity, bilinear on $A^{\varsigma} \times A$, and it equals the product exactly when the involution on $A$ is the identity and $A$ is commutative; for an algebra of full type with $\varsigma \neq \mathrm{id}$ it therefore always differs from the product. The left products are conjugate-linear and the right products linear, and when the product is associative they make $A$ a left and a right module; the composite of two left products is linear through the square $\varsigma^{2} = \mathrm{id}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $R$, $\varsigma$ | a commutative ring with $1$, and an involution of it |
| $A$, $\star$ | an $R$-module, and a $\varsigma$-sesquilinear product on it |
| $xy$ | the product of an associative algebra, written by juxtaposition when the derived operation is in play |
| $x \mapsto x^{*}$ | a $\varsigma$-semilinear involution, the extra datum of the standard case |
| $x \star y = xy^{*}$ | the derived operation, the standard sesquilinear product |
| $A^{\varsigma}$ | the conjugate module, the scalars acting by $\lambda \cdot x = \varsigma(\lambda) x$ |
| $(\lambda x) \star (\mu y) = \lambda \varsigma(\mu)(x \star y)$ | the rule of the scalars of a product |
| $c_{ij}^{k}$ | the structure constants, $e_i \star e_j = \sum_k c_{ij}^{k} e_k$ |
| $[x, y]_{\varsigma}$ | the difference $x \star y - y \star x$ |
| $L_{a}$, $R_{a}$ | the left and the right product, $L_{a}(x) = a \star x$ and $R_{a}(x) = x \star a$ |

## Further Reading

- N. Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1989), for the semilinear algebra of a module over a ring with an involution, the setting in which a sesquilinear map is read as an ordinary bilinear map.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the involution of a ring and the conjugate-linear maps it produces, which is the datum that makes a sesquilinear product different from a bilinear one.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the linear and the conjugate-linear kinds of anti-automorphism and the constraint the twist puts on them.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the conjugate-linear operators, taken here algebraically and without the topology.
