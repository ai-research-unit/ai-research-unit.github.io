# __Sesqualgebras__

## Introduction

A **sesqualgebra** is an algebra whose product is linear in the first variable and conjugate-linear in the second, the conjugating map being an involution $\varsigma$ of the base ring:

$$
(\lambda x)y = \lambda(xy), \qquad x(\lambda y) = \varsigma(\lambda)(xy) .
$$

The object is the algebra companion of the sesquilinear **form**, and the two must not be confused. A sesquilinear form is a two-variable map into the scalars; a sesqualgebra is an object whose product is a two-variable map into the algebra, and it is the object of this category. The difference is that the product takes its values in $A$ rather than in the scalars, so it can be composed with itself, and the questions of associativity, of unit and of the structures built on the product arise as they do for an ordinary algebra.

The datum is the pair $(R,\varsigma)$, and the object is relative to it: for the trivial involution the two scalar rules coincide and the product is bilinear, so the whole category collapses to the ordinary algebras of *Algebras* exactly when $\varsigma = \mathrm{id}$. This is the sense in which the two names are needed: the algebra is the trivial-involution case of the sesquilinear one, and the sesqualgebra is the case in which the involution is nontrivial and the product is genuinely not bilinear.

The standard example is the **derived operation** of an algebra with an involution. On an associative algebra $A$ with a $\varsigma$-semilinear involution $x \mapsto x^{*}$, the operation

$$
x \star y = xy^{*}
$$

is linear in $x$ and $\varsigma$-semilinear in $y$, so $(A,\star)$ is a sesqualgebra. For a unital $A$ it is associative exactly when the involution is trivial, so it is the model of a sesquilinear product that is not associative, and the failure forces a ternary product, $\{x,y,z\} = xy^{*}z$, which is the subject of *Algebraic J\*-Algebras*.

**Terminology.** In this article a **sesqualgebra** is an $R$-module with a product additive in each variable and satisfying the two scalar rules above; it need not be associative, need not have a unit and need not be commutative, and each of these properties is named where it is used, exactly as in *Algebras*. The base involution is written $\varsigma$, and the product is called $\varsigma$-sesquilinear; $\sigma$ is reserved for an involution of the algebra itself.

**Layout and boundaries.** The article treats the definition and the conjugate module, the collapse at the identity, the standard example with its associativity criterion and its units, the ternary product that the failure forces, and the elementary properties with the examples. It stays inside the algebra and uses no form and no distance: no norm, no length, no topology, no orthogonality, no sesquilinear or Hermitian form. The vocabulary is that of *Algebras*, *Associative Algebras* and *Unital Algebras* for the object, *Ideals and Quotients of Algebras* for the ideals, *Centre, Units, Zero Divisors and Division Algebras* for the centre and the units, *Tensor Products of Algebras* for the tensor product, *Involutive Algebras* for the involution of an algebra, and *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System* for the ternary structure. Throughout, $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and $A$ is an $R$-module carrying a product $A \times A \to A$.

---

## The Definition

### The Two Scalar Rules

**Definition.** Let $R$ be a commutative ring with $1$ and let $\varsigma$ be an involution of $R$, that is an additive map with $\varsigma(1) = 1$, $\varsigma(ab) = \varsigma(b)\varsigma(a)$ and $\varsigma^2 = \mathrm{id}$. A **sesqualgebra** is an $R$-module $A$ with a product $A \times A \to A$, written $(x,y) \mapsto xy$, additive in each variable and satisfying

$$
(\lambda x)y = \lambda(xy), \qquad x(\lambda y) = \varsigma(\lambda)(xy)
$$

for all $\lambda \in R$ and all $x, y \in A$. The first rule says the product is $R$**-linear in the first variable**; the second says it is $\varsigma$**-semilinear in the second**. When the second rule is the first, that is when $\varsigma(\lambda) = \lambda$ for every $\lambda$, the product is $R$-bilinear in both variables and $A$ is an $R$-algebra in the sense of *Algebras*.

**Remark.** The two rules are the only ones that mention the scalars. Additivity in each variable says $(x+x')y = xy + x'y$ and $x(y+y') = xy + xy'$, and the two rules fix what happens under a scalar separately on each side. No other axiom is imposed, so the notion contains the algebras that are not associative, not unital and not commutative, and an **associative sesqualgebra** is one whose product satisfies the associative law $(xy)z = x(yz)$ in addition.

**Remark (the sides are not interchangeable).** The two rules are not symmetric. Reading the product with the variables exchanged gives a product that is $\varsigma$-semilinear in the first variable and linear in the second, which is a different object unless $\varsigma = \mathrm{id}$; exchanging the two variables is therefore a construction and not an identity.

### The Conjugate Module

**Definition.** The **conjugate module** $A^{\varsigma}$ is the abelian group $A$ with the twisted scalar action

$$
\lambda \cdot x = \varsigma(\lambda)\,x .
$$

The map $x \mapsto \varsigma(\lambda)x$ is additive in $x$, and it is an action because the two sides of $\lambda \cdot (\mu \cdot x) = (\mu\lambda) \cdot x$ agree:

$$
\lambda \cdot (\mu \cdot x) = \varsigma(\lambda)\varsigma(\mu)x = \varsigma(\mu\lambda)x = (\mu\lambda) \cdot x,
$$

the last equality being the multiplicativity of $\varsigma$ read backwards. The module $A$ and its conjugate $A^{\varsigma}$ have the same additive group and the same underlying set, and they differ only in which scalars act and how.

**Theorem (the product is bilinear on the pair).** Let $A$ be a sesqualgebra. The product, read as a map

$$
A \times A^{\varsigma} \to A,
$$

is $R$-bilinear in the two variables. Conversely, an $R$-bilinear map $A \times A^{\varsigma} \to A$ is a $\varsigma$-sesquilinear product on $A$.

**Proof.** The product is additive in each variable by hypothesis, so it suffices to check the scalars. In the first slot, $(\lambda x)y = \lambda(xy)$ is the first rule. In the second slot, the scalar acts on $A^{\varsigma}$ by $\lambda \cdot y = \varsigma(\lambda)y$, and the product of $x$ with that element is $x(\varsigma(\lambda)y) = \varsigma(\varsigma(\lambda))(xy) = \lambda(xy)$, which is the second rule read backwards. The converse is the same computation in the other direction.

**Remark (conjugation is a functor).** The conjugate module of an object is again an object: reading the same product on the set $A$ with the twisted action, the first rule holds because $\varsigma$ is multiplicative and the second because $\varsigma^2 = \mathrm{id}$ returns the scalar. Conjugation is therefore an involution on the objects, $(A^{\varsigma})^{\varsigma} = A$, and it extends to an involutive functor fixing every morphism, an $R$-linear map being $R$-linear for the twisted actions on both sides. A **conjugate morphism** $A \to B$, defined below, is then exactly a morphism $A \to B^{\varsigma}$: the word names a morphism into the conjugate object, not a second kind of morphism.

**Remark.** The theorem is the reason the notion is the right one: a sesquilinear product is not a bilinear product, but it **is** a bilinear product once one of the two copies of $A$ is conjugated. Every statement of this category can therefore be read as a statement about a bilinear map $A \times A^{\varsigma} \to A$ whose two arguments live in two different modules, and the bookkeeping of which module is which is the only new ingredient.

### The Collapse at the Identity

**Theorem.** A sesqualgebra with $\varsigma = \mathrm{id}$ is an ordinary $R$-algebra, and conversely every $R$-algebra is a sesqualgebra for the trivial involution. For two involutions $\varsigma, \varsigma'$ of $R$, if a product is both $\varsigma$- and $\varsigma'$-sesquilinear then $(\varsigma(\lambda) - \varsigma'(\lambda))xy = 0$ for all $\lambda, x, y$, so the two involutions differ only on scalars that annihilate every product; when $A$ is faithful over $R$ and the products generate $A$, they coincide. The involution is part of the datum and is not determined by the product alone.

**Proof.** With $\varsigma = \mathrm{id}$ the second rule is the first and the product is $R$-bilinear. The converse is immediate. The last claim: a product that is both $\varsigma$- and $\varsigma'$-semilinear in the second slot satisfies $(\varsigma(\lambda) - \varsigma'(\lambda))xy = 0$ for every $\lambda$ and every pair $x, y$; if the products generate $A$ as an abelian group this gives $(\varsigma(\lambda) - \varsigma'(\lambda))\cdot A = 0$ for every $\lambda$, and faithfulness of $A$ then gives $\varsigma(\lambda) = \varsigma'(\lambda)$.

**Remark.** The collapse is the sense in which the sesquilinear kind **contains** the bilinear kind rather than sitting beside it, and it is the reason *Algebras* is not merely a parallel category but the case that this one collapses to. It is also the reason a statement about sesqualgebras must say what it becomes at $\varsigma = \mathrm{id}$; a proof that used only the first rule would hold in both categories and would not be a sesquilinear statement.

**Theorem (commutativity or associativity forces the trivial involution).** Let $A$ be a sesqualgebra, and for $\lambda \in R$ put $c_\lambda = \varsigma(\lambda) - \lambda$.

(i) If the product is **commutative**, then $c_\lambda \cdot (A \cdot A) = 0$ for every $\lambda$; if in addition the products generate $A$, then $c_\lambda A = 0$.
(ii) If the product is **associative**, then $c_\lambda \cdot (A \cdot A \cdot A) = 0$ for every $\lambda$; if in addition the products generate $A$ and no nonzero element of $A$ annihilates $A$ on the left, then $c_\lambda A = 0$.

In either case, if $A$ is faithful over $R$, then $c_\lambda = 0$ for every $\lambda$ and $\varsigma = \mathrm{id}$.

**Proof.** (i) The commutativity of the product turns the identity $x(\lambda y) = (\lambda y)x$ into $x(\lambda y) = \lambda(yx) = \lambda(xy)$, the first equality by the first rule and the last by commutativity; the second rule reads the same left-hand side as $\varsigma(\lambda)(xy)$. Hence $(\varsigma(\lambda) - \lambda)xy = 0$ for all $x, y$. If the products generate $A$, the scalar $c_\lambda$ annihilates a generating set and therefore all of $A$, because the scalar action is $R$-linear.

(ii) The associativity of the product turns the identity $(xy)(\lambda z) = x\bigl(y(\lambda z)\bigr)$ into $\varsigma(\lambda)((xy)z) = \lambda((xy)z)$: the left side is the second rule applied to the outer product, while the right side is the second rule applied to $y(\lambda z)$, whose scalar comes back as $\varsigma(\varsigma(\lambda)) = \lambda$ and is then reassociated. Hence $(\varsigma(\lambda) - \lambda)(xy)z = 0$ for all $x, y, z$, that is $c_\lambda(xy)$ annihilates $A$ on the left for every pair. If no nonzero element of $A$ annihilates $A$ on the left, then $c_\lambda(xy) = 0$ for all $x, y$, and if the products generate $A$ then $c_\lambda A = 0$.

In both cases $c_\lambda A = 0$, that is $c_\lambda \in \operatorname{ann}_R(A)$, and faithfulness gives $c_\lambda = 0$. $\square$

**Corollary (a sesqualgebra of full type is neither associative nor commutative).** Say that a sesqualgebra is **of full type** when it is faithful over $R$, its products generate $A$, and no nonzero element of $A$ annihilates $A$ on the left. If $A$ is of full type and $\varsigma \neq \mathrm{id}$, then $A$ is **neither associative nor commutative**. The generation and the annihilation conditions are automatic when $A$ has a unit, so a unital faithful sesqualgebra with $\varsigma \neq \mathrm{id}$ is neither associative nor commutative.

**Proof.** Were $A$ associative, (ii) would give $c_\lambda A = 0$ for every $\lambda$, hence $c_\lambda = 0$ by faithfulness, contradicting $\varsigma \neq \mathrm{id}$; were $A$ commutative the same conclusion follows from (i). $\square$

**Remark.** The hypotheses are not decorative, and each is used at a definite place. **Generation** is what turns the vanishing of $c_\lambda$ on the products into its vanishing on $A$; without it the **zero product** on a nontrivial module is commutative and associative for any $\varsigma$, with $A \cdot A = 0$ and $A \neq 0$. **Faithfulness** is what turns $c_\lambda \in \operatorname{ann}_R(A)$ into $c_\lambda = 0$; without it the honest conclusion is only that $\varsigma$ becomes the identity after the base ring is reduced by $\operatorname{ann}_R(A)$. **Absence of left annihilators** is used only in (ii), to read $c_\lambda(xy)z = 0$ for all $z$ as $c_\lambda(xy) = 0$; like generation it is automatic when $A$ has a unit. With the hypotheses in place the collapse is sharp: an algebra with a nontrivial involution is then never a disguised associative or commutative algebra, and the derived operation of the next section is the model. Dividing the base ring by $\operatorname{ann}_R(A)$ is the general reduction that turns an associative or commutative sesqualgebra into an ordinary algebra.

### Morphisms

**Definition.** A **morphism** $\varphi : A \to B$ of sesqualgebras over the same $(R,\varsigma)$ is an $R$-linear map with $\varphi(xy) = \varphi(x)\varphi(y)$; a **conjugate morphism** is a $\varsigma$-semilinear map with the same multiplicativity. The two are told apart by their behaviour on scalars, and the two notions coincide exactly when $\varsigma = \mathrm{id}$.

**Remark.** The distinction is the module-level shadow of the distinction between the two kinds of map on an involutive algebra, and it is the reason the category is not the category of algebras over a fixed ring: the scalars may be moved by $\varsigma$, and a homomorphism is allowed to move them only by the identity. The study of the maps, their kernels and images is *Ideals and Quotients of a Sesqualgebra*.

## The Standard Example

### The Derived Operation of an Involutive Algebra

**Definition.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $* : A \to A$, that is an additive map with $(xy)^{*} = y^{*}x^{*}$, $*^{2} = \mathrm{id}$ and $(\lambda x)^{*} = \varsigma(\lambda)x^{*}$ (and $1^{*} = 1$ when $A$ has a unit); the involution is the subject of *Involutive Algebras*. The **derived operation** is

$$
x \star y = xy^{*} .
$$

**Proposition.** The derived operation is a $\varsigma$-sesquilinear product on $A$.

**Proof.** The operation is additive in each variable, because the product and the involution are additive. For the first rule, $(\lambda x) \star y = (\lambda x)y^{*} = \lambda(x \star y)$. For the second,

$$
x \star (\lambda y) = x(\lambda y)^{*} = x\,\varsigma(\lambda)\,y^{*} = \varsigma(\lambda)\,xy^{*} = \varsigma(\lambda)(x \star y).
$$

**Remark.** The derived operation is the reason the category is not empty and not artificial: every algebra with a conjugate-linear involution carries one, and the algebras of the corpus — the complex matrices with the conjugate transpose, the group algebra with $f \mapsto f^{*}$, the biquaternion algebra with the star — each carry one. The operator theory of the derived operation, its left and right multiplications and its sandwich, is the operator theory of this category.

**Proposition (the units of the derived operation).** Let $A$ be a unital associative $R$-algebra with a $\varsigma$-semilinear involution $*$, and let $\star$ be the derived operation.

(i) The unit $1$ of $A$ is a right $\star$-unit: $x \star 1 = x\,1^{*} = x$ for every $x$.
(ii) $A$ has a left $\star$-unit if and only if $* = \mathrm{id}$, and then $1$ is a two-sided unit and $\star$ is the original product.

**Proof.** (i) $1^{*} = 1$, so $x \star 1 = x$. (ii) Let $e$ be a left $\star$-unit, so that $e \star x = e\,x^{*} = x$ for every $x$. At $x = 1$ this gives $e\,1^{*} = e = 1$, so $e = 1$; then $1 \star x = x^{*}$ must equal $x$ for every $x$, so $* = \mathrm{id}$. Conversely if $* = \mathrm{id}$ then $\star$ is the original product and $1$ is its unit. $\square$

**Remark.** The failure of unitality is one-sided, and it is the asymmetry of the two slots read at the level of the unit: the right unit $1$ survives the twist and the left unit does not. The derived operation of a unital algebra with a nontrivial involution therefore has a right unit and no unit at all, and it is unital exactly when it is the original product.

### The Associativity Criterion

**Proposition.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution and the derived operation $x \star y = xy^{*}$. The associator of the derived operation is

$$
(x \star y) \star z - x \star (y \star z) = x\bigl((zy)^{*} - zy^{*}\bigr) .
$$

Consequently the derived operation is associative if and only if $x\bigl((zy)^{*} - zy^{*}\bigr) = 0$ for all $x, y, z \in A$, which for an $A$ with zero left annihilator (in particular for a unital $A$) is the condition $(zy)^{*} = zy^{*}$; when $A$ has a unit this in turn holds if and only if the involution is the identity.

**Proof.** Expanding, $(x \star y) \star z = xy^{*}z^{*}$ and $x \star (y \star z) = xz y^{*}$; the difference is $x(y^{*}z^{*} - zy^{*}) = x((zy)^{*} - zy^{*})$, because $(zy)^{*} = y^{*}z^{*}$. The criterion follows. With a unit, taking $y = 1$ gives $z^{*} = z$ for every $z$, so the involution is the identity; conversely the identity involution gives the original associative product.

**Corollary.** On a commutative algebra with a unit the derived operation is associative if and only if the involution is the identity, so the commutativity of the algebra does not by itself make the derived operation associative.

**Remark.** The corollary is the point that separates the derived operation from a mere relabelling of the product. Writing $x \star y = xy^{*}$ is not a change of notation for the algebra, because the associativity that the algebra has is lost the moment the involution is nontrivial. What remains is a weaker structure, and the next section names it.

## The Ternary Product

### The Triple Product

**Definition.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution. The **triple product** attached to the derived operation is

$$
\{x,y,z\} = (x \star y) \star z^{*} = xy^{*}z .
$$

**Proposition.** The triple product is additive in each variable, $R$-linear in the first and the third variables, and $\varsigma$-semilinear in the middle variable. It satisfies the Hermitian symmetry $\{x,y,z\}^{*} = \{z^{*},y^{*},x^{*}\}$.

**Proof.** Additivity and the scalars are read from the definition: a scalar $\lambda$ in the first or the third variable is a scalar of the product, and in the middle variable it meets the involution and is sent to $\varsigma(\lambda)$. For the symmetry, $\{x,y,z\}^{*} = (xy^{*}z)^{*} = z^{*}y x^{*} = \{z^{*},y^{*},x^{*}\}$. This is the only symmetry available: the plain symmetry $\{x,y,z\} = \{z,y,x\}$ would read $xy^{*}z = zy^{*}x$, which fails as soon as $A$ is noncommutative, and it is not implied.

**Remark.** The replacement of associativity by the Hermitian symmetry is the reason the triple product rather than the binary product is the natural carrier of the identities. The binary derived operation loses associativity, so it supports no semigroup structure; the triple product retains enough symmetry to carry a Jordan triple identity, and the resulting object is the subject of *Algebraic J\*-Algebras*.

### The Jordan Triple Identity

**Theorem (the identity).** The triple product of the derived operation satisfies the Jordan triple identity

$$
\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\} .
$$

**Proof.** The verification is a finite expansion of each side in the products and the involution, using only the associativity of $A$ and $(uv)^{*} = v^{*}u^{*}$; it is carried out in *Algebraic J\*-Algebras*, where the identity is the defining axiom of the $J^{*}$-triple.

**Remark.** The identity is not an accident of the example but the algebraic content of the failure of associativity: the ternary product is what remains of the associative law after the operation is twisted by the involution. The category therefore has two layers, the binary derived operation and the ternary product, and the binary one is read as the shadow of the ternary one.

## Elementary Properties

### The Left and the Right Multiplication

**Definition.** For $a \in A$ the **left multiplication** $L_a : A \to A$ and the **right multiplication** $R_a : A \to A$ of the sesquilinear product are

$$
L_a(x) = ax, \qquad R_a(x) = xa .
$$

**Proposition.** $L_a$ is $\varsigma$-semilinear for every $a$, while $R_a$ is $R$-linear; $L_a$ is $R$-linear exactly when $\varsigma = \mathrm{id}$ or $(\lambda - \varsigma(\lambda))ax = 0$ for every $\lambda \in R$ and $x \in A$. When the product is associative — which for an algebra of full type forces $\varsigma = \mathrm{id}$, by the theorem of *The Collapse at the Identity* — the two families satisfy

$$
L_aL_b = L_{ab}, \qquad R_aR_b = R_{ba}, \qquad L_aR_b = R_bL_a,
$$

so $a \mapsto L_a$ is multiplicative but its values are $\varsigma$-semilinear, while $a \mapsto R_a$ is multiplicative up to the reversal of the order — a representation of the opposite algebra $A^{\mathrm{op}}$ — with $R$-linear values.

**Proof.** For $L_a$, $L_a(\lambda x) = a(\lambda x) = \varsigma(\lambda)(ax) = \varsigma(\lambda)L_a(x)$ by the second rule, so $L_a$ is $\varsigma$-semilinear, and it is $R$-linear exactly when $\lambda ax = \varsigma(\lambda) ax$ for every $\lambda$ and $x$. For $R_a$, $R_a(\lambda x) = (\lambda x)a = \lambda(xa) = \lambda R_a(x)$ by the first rule, so $R_a$ is $R$-linear. The composition identities are the associative law read in the three possible orders; the second shows that the right multiplications compose in the order opposite to the multiplication of the parameters, which is why $a \mapsto R_a$ is an anti-homomorphism.

**Remark.** The failure of the left multiplication to be linear is the operator-level form of the second scalar rule, and it is the reason the operator theory of this category carries two classes of operators, the linear and the conjugate-linear. That operator theory is the group *Operator Theory* of the category.

### The Opposite Algebra

**Definition.** Let $A$ be a sesqualgebra. The **opposite algebra** $A^{\mathrm{op}}$ has the same additive group and the same scalars as $A$ and the product $x \cdot y = yx$.

**Proposition.** The product of $A^{\mathrm{op}}$ is $\varsigma$-semilinear in the first variable and $R$-linear in the second: the parity of the two slots is exchanged, so $A^{\mathrm{op}}$ is the mirror of $A$ in the sense of the remark that the two sides are not interchangeable. It is a sesqualgebra in the standard sense exactly when $\varsigma = \mathrm{id}$; in general it is the $R$-bilinear map $A^{\varsigma} \times A \to A$, $(u,y) \mapsto yu$, with the conjugate module in the first factor rather than the second, just as the product of $A$ is the bilinear map $A \times A^{\varsigma} \to A$. The identity is an isomorphism $A \to A^{\mathrm{op}}$ exactly when $A$ is commutative, and the product of $A^{\mathrm{op}}$ is $R$-bilinear in both slots exactly when $\varsigma = \mathrm{id}$.

**Proof.** $(\lambda x) \cdot y = y(\lambda x) = \varsigma(\lambda)(yx) = \varsigma(\lambda)(x \cdot y)$ and $x \cdot (\lambda y) = (\lambda y)x = \lambda(yx) = \lambda(x \cdot y)$ by the two rules of the product of $A$; the same two evaluations show that $(u,y) \mapsto yu$ is additive and $R$-linear in each variable on $A^{\varsigma} \times A$. The remaining clauses are the definitions.

### Ideals and Quotients

**Definition.** An **ideal** $I$ of a sesqualgebra $A$ is an $R$-submodule with $ax \in I$ and $xa \in I$ for all $a \in A$ and $x \in I$; the quotient $A/I$ then carries an induced product.

**Proposition.** The intersection and the sum of ideals are ideals; the products $xy$ with $x \in I$, $y \in J$ generate an ideal $IJ$; and the quotient $A/I$ is a sesqualgebra whose product is the induced one whenever $I$ is an ideal.

**Proof.** The additive and multiplicative closure statements are the associativity-free part of the ring theory and hold for any product additive in each variable; the quotient inherits the two scalar rules because the scalar action descends to the quotient. The detail and the isomorphism theorems are *Ideals and Quotients of a Sesqualgebra*.

### Examples

**Example (the field itself).** Let $K$ be a field with an involution $\varsigma$, and take $A = K$ with the product $x \star y = x\,\varsigma(y)$. The product is $K$-linear in $x$ and $\varsigma$-semilinear in $y$, so $K$ is a sesqualgebra over itself. Its associator is

$$
(x \star y) \star z - x \star (y \star z) = x\,\varsigma(y)\varsigma(z) - x z\,\varsigma(y)
= x\bigl(\varsigma(zy) - z\,\varsigma(y)\bigr),
$$

which vanishes for all $x, y, z$ only when $\varsigma = \mathrm{id}$ (take $y = 1$), so the product is associative exactly when $\varsigma = \mathrm{id}$; it is commutative on the same condition.

**Example (the complex numbers).** With $K = \mathbb{C}$ and $\varsigma$ the conjugation, the product $x \star y = x\bar y$ is the standard sesquilinear product on $\mathbb{C}$. The failure of unitality is the one-sided failure of the Proposition above: $1$ is a right unit, since $z \star 1 = z\,1 = z$, and it is not a left unit, since $1 \star z = \bar z \neq z$ unless $z$ is real, so there is no two-sided unit. A sesqualgebra therefore need not be unital even when the algebra it is derived from is, and the two slots carry different unit behaviour.

**Example (the matrix algebra).** On $M_n(\mathbb{C})$ with the conjugate transpose, the derived operation $S \star T = ST^{*}$ and the triple product $\{S,T,U\} = ST^{*}U$ are the standard examples of the category over $(\mathbb{C},\varsigma)$. The Hermitian and the unitary elements, and the trace functional, are the structures that the derived operation carries.

**Example (the biquaternion algebra).** On $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the star ${}^{*}$, the derived operation $P \star Q = PQ^{*}$ and the triple product $PQ^{*}R$ are the sesquilinear structures of the corpus's own algebra; the caution that the quaternion conjugation ${}^{\natural}$ is $\mathbb{C}$-linear, so that a product whose **second** slot carries it is bilinear and not sesquilinear, while a product whose second slot carries the star is sesquilinear whatever the first slot carries, is the subject of *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*.

## Summary

A sesqualgebra is an $R$-module with a product additive in each variable, linear in the first and $\varsigma$-semilinear in the second; the datum is the pair $(R,\varsigma)$, and the object is relative to it. The product is not bilinear, but it is a bilinear map $A \times A^{\varsigma} \to A$ once the second copy of $A$ is read with the twisted scalar action of the conjugate module, and this reformulation is the working form of the definition. Conjugation is an involution on the objects, and a conjugate morphism $A \to B$ is exactly a morphism $A \to B^{\varsigma}$. At $\varsigma = \mathrm{id}$ the two scalar rules coincide, the product is $R$-bilinear and the object is an ordinary algebra, so the sesquilinear kind contains the bilinear kind as the trivial-involution case rather than sitting beside it. The inclusion is nearly an equality for an algebra of full type — faithful over $R$, with generating products and no nonzero left annihilator, the last two automatic for a unital algebra: an associative or a commutative product then forces $\varsigma = \mathrm{id}$. An algebra of full type with a nontrivial involution is therefore **neither associative nor commutative**, and the derived operation is the model of such an object.

The standard example is the derived operation $x \star y = xy^{*}$ of an associative algebra with a $\varsigma$-semilinear involution; it is sesquilinear, and its associator is $x\bigl((zy)^{*} - zy^{*}\bigr)$, so with a unit it is associative exactly when the involution is the identity, and the commutativity of the algebra does not change that. For a unital algebra the derived operation always has $1$ as a right unit and has a left unit only when the involution is trivial, so it is unital exactly when it coincides with the original product. The failure of associativity forces the triple product $\{x,y,z\} = xy^{*}z$, additive in each variable, linear in the outer variables, $\varsigma$-semilinear in the middle, and satisfying the Jordan triple identity; the binary derived operation is the shadow of the ternary product, and the ternary product is the subject of *Algebraic J\*-Algebras*. The left multiplication $L_a$ is $\varsigma$-semilinear while the right multiplication $R_a$ is linear, so the operator theory of the category carries two classes of operators; the ideals, the quotients and the opposite algebra follow the ring theory with the twisted slot carried along, and the worked examples are the field with the product $x\varsigma(y)$, the complex numbers with $x\bar y$, the complex matrices with the conjugate transpose, and the biquaternion algebra with the star.

## Summary of Notation

| symbol | meaning |
|---|---|
| $R$, $\varsigma$ | a commutative ring with $1$, and an involution of it |
| $A$ | a sesqualgebra, an $R$-module with the product below |
| $xy$ | the product, additive in each variable, $R$-linear in $x$, $\varsigma$-semilinear in $y$ |
| $A^{\varsigma}$ | the conjugate module, the scalars acting by $\lambda \cdot x = \varsigma(\lambda)x$ |
| $x \mapsto x^{*}$ | a $\varsigma$-semilinear involution of an associative $R$-algebra |
| $x \star y$ | the derived operation $xy^{*}$ |
| $\{x,y,z\}$ | the triple product $xy^{*}z$ |
| $L_a$, $R_a$ | the left and the right multiplication, $L_a(x) = ax$ and $R_a(x) = xa$ |
| $(xy)^{*}$ | the involution applied to a product, equal to $y^{*}x^{*}$ |
| $A^{\mathrm{op}}$ | the opposite algebra, $x \cdot y = yx$ |
| $A \cdot A$ | the products of pairs, whose generated submodule is assumed to be $A$ in the collapse theorems |
| $\operatorname{ann}_R(A)$ | the annihilator $\{r \in R : rA = 0\}$ of $A$ in $R$ |
| $A$ of full type | faithful over $R$, with products generating $A$ and no nonzero left annihilator |
| $I$, $A/I$ | an ideal, and the quotient by it |

## Further Reading

- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the linear and the conjugate-linear parts of an algebra with an involution and the two-sided structures they carry.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the involution of an algebra of operators, the conjugate module and the distinction between linear and conjugate-linear maps which this article takes algebraically.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the Jordan triple structure of the ternary product and the Jordan triple identity.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the $J^{*}$-algebra and the ternary product read algebraically, which is the layer of this category.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions of a central simple algebra and the semilinear case, which is the boundary this category shares with *Involutive Algebras*.
