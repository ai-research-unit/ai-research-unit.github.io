# __Jordan Algebras of Sesquialgebras__

## Introduction

A bilinear product carries a Jordan algebra in its symmetrisation: the product $x \bullet y = \tfrac12(xy + yx)$ is commutative and satisfies the Jordan identity, and that is the general source of the special Jordan algebras of *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*, and the symmetric half of the decomposition of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*. A sesquilinear product is bilinear in one slot and conjugate-linear in the other, and the question of this article is what becomes of that construction. The answer has four parts.

The symmetrisation of a sesquilinear product is commutative and additive, and it is linear over the fixed ring rather than over $R$, so it too is a *bilinear* product and the object it defines is an algebra and not a sesquialgebra; it is a Jordan product on the Hermitian part of the algebra and not off it, since off the Hermitian part the product being symmetrised is not the associative one, and the Jordan identity fails there with a witness in $M_{2}(\mathbb{C})$. This is §*The Symmetrisation and Its Obstruction*. On the Hermitian part the symmetrisation is a Jordan algebra over the fixed ring, $J(A) = \bigl(H(A), \circ\bigr)$, the object of *The Hermitian Jordan Algebra*, and it is functorial in the involutive algebra. This is §*The Hermitian Jordan Algebra*. What exists on the whole space, when the binary product does not, is the ternary one: the algebraic $J^{*}$-algebra $\{x,y,z\} = xy^{*}z$ of *Algebraic J\*-Algebras*, whose binary product is a shadow recovered only at a unit. This is §*The Ternary Structure*. And the Jordan algebras that arise this way are all special, so the exceptional ones are outside the class. This is §*The Boundary*.

The companion article is *Lie Algebras of Sesquialgebras*. The two are the sesquilinear counterparts of the two halves of the bilinear decomposition, they share the framing of the binary structure on one half of the algebra over the fixed ring, and they are read together; the parallel is sharp, since the Lie structure is carried by the *skew*-Hermitian half under the commutator and the Jordan structure by the *Hermitian* half under the symmetrisation, and each half carries the action of its own structure, $\mathrm{ad}$ on the one and the quadratic representation on the other. The setting is that of *Sesquialgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ is an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, the derived sesquilinear operation is $x \star y = xy^{*}$, and $H(A)$ and $S(A)$ are the two halves of *Hermitian and Skew-Hermitian Elements*. Throughout, $2$ is invertible in $R$.

---

## The Symmetrisation and Its Obstruction

### The Symmetrisation

**Definition.** The **symmetrisation** of the sesquilinear product is

$$
x \circ y = \tfrac12\bigl(x \star y + y \star x\bigr) .
$$

**Proposition.** The symmetrisation is commutative, $x \circ y = y \circ x$, additive in each variable, equal to the square on the diagonal, $x \circ x = x \star x = xx^{*}$, and it is the polarisation of the square, $x \circ y = \tfrac12\bigl((x+y)\star(x+y) - x\star x - y\star y\bigr)$. For $\lambda \in R$,

$$
(\lambda x) \circ y = \tfrac12 \lambda\,(x \star y) + \tfrac12 \varsigma(\lambda)\,(y \star x) ,
$$

so that $\circ$ is linear over the fixed ring $R^{\varsigma}$ in each variable, and linear over all of $R$ exactly in the degenerate case $(\varsigma(\lambda) - \lambda)A = 0$ for every $\lambda$. Its image lies in the Hermitian part, $(x \circ y)^{*} = x \circ y$ for all $x, y$.

**Proof.** All but the last statement are the proposition and the theorem of *The Sesquilinear Symmetrised Product*, where the scalar rules, the polarisation and the Hermitian value are proved; the image statement uses the reversal of the derived product under conjugation, $(x \star y)^{*} = y \star x$, which gives $(x \circ y)^{*} = \tfrac12(y \star x + x \star y) = x \circ y$. $\square$

**Remark.** The pair $\bigl(x \circ y, \tfrac12(x \star y - y \star x)\bigr)$ splits the sesquilinear product into a symmetric and an antisymmetric part, exactly as the bilinear theory splits a product into its symmetrisation and its commutator. The two halves of that split behave very differently here, and the difference is the subject of this article and of its companion: the symmetric part is a Jordan product on the Hermitian half, while the antisymmetric part is a Lie bracket on no half at all, its Lie theory being carried by the commutator instead.

**Remark (a Jordan algebra over the fixed ring, not a Jordan sesquialgebra).** The scalar rule above is two rules, and that is the obstruction. Under $\lambda$ the two terms of the symmetrisation carry different scalars, $\lambda$ on the first and $\varsigma(\lambda)$ on the second,

$$
(\lambda x) \circ y = \tfrac12 \lambda\,(x \star y) + \tfrac12 \varsigma(\lambda)\,(y \star x) .
$$

A scalar can be taken out of a sum only when it multiplies every term of it, so $\circ$ is linear at $\lambda$ only if $\varsigma(\lambda) = \lambda$, and it is $\varsigma$-semilinear there under the same condition; over a scalar that the involution moves it obeys no rule at all. Over the fixed ring the two scalars coincide and the product is bilinear, so what the symmetrisation defines there is a **Jordan algebra over $R^{\varsigma}$**. It is never a Jordan sesquialgebra. The title says this exactly: the symmetrisation of a sesquialgebra returns an algebra.

### The Failure off the Hermitian Part

**Theorem.** The Jordan identity for the symmetrisation of the derived sesquilinear product fails off the Hermitian part. In $A = M_{2}(\mathbb{C})$ with the conjugate transpose, for $x = E_{12}$ and $y = E_{22}$,

$$
(x \circ y) \circ (x \circ x) = \tfrac14\bigl(E_{12} + E_{21}\bigr) \neq 0 = x \circ \bigl(y \circ (x \circ x)\bigr) .
$$

**Proof.** With the matrix-unit rule $E_{ab}E_{cd} = \delta_{bc}E_{ad}$: $x \circ x = E_{12}E_{21} = E_{11}$, and $y \circ (x \circ x) = E_{22} \circ E_{11} = \tfrac12(E_{22}E_{11} + E_{11}E_{22}) = 0$, so the right-hand side is $x \circ 0 = 0$. On the left, $x \circ y = \tfrac12(E_{12}E_{22} + E_{22}E_{21}) = \tfrac12(E_{12} + E_{21})$, whose symmetrisation with $E_{11}$ is $\tfrac12\bigl(\tfrac12(E_{12}+E_{21})E_{11} + E_{11}\tfrac12(E_{12}+E_{21})\bigr) = \tfrac14\bigl(E_{12}+E_{21}\bigr)$, and the two sides differ. $\square$

**Remark.** One of the two elements is Hermitian, $y = E_{22}$, and one is not; a single element off $H(A)$ breaks the identity. The mechanism is the one identified in *The Sesquilinear Symmetrised Product*: the identity for a symmetrisation is inherited from the associativity of the product being symmetrised, and off the Hermitian part the product being symmetrised is the derived operation $x \star y = xy^{*}$, which is not associative. On $H(A)$ the derived operation coincides with the associative product, and there the identity holds — this is the theorem of the next section.

### When the Symmetrisation Is a Jordan Product

**Theorem (the criterion, and its collapse).** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution, and let $\star$ be the derived operation.

(i) If $\star$ is associative, then $\circ$ satisfies the Jordan identity on all of $A$, and it is a Jordan product over $R$ exactly when the product is $R$-bilinear.

(ii) If $A$ is of full type and $\varsigma \neq \mathrm{id}$, then $\star$ is not associative, so the hypothesis of (i) is unavailable, the Jordan identity fails off the Hermitian part by the witness above, and it holds on $H(A)$.

**Proof.** (i) The symmetrisation of an associative product satisfies the Jordan identity, by *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*, and the scalar statement is the scalar rule of the proposition above. (ii) The associativity of $\star$ of full type forces $\varsigma = \mathrm{id}$ by the collapse theorem of *Sesquialgebras*, §*The Collapse at the Identity*, so for a genuinely sesquilinear product the hypothesis of (i) is unavailable and the failure of the theorem above applies; on $H(A)$ the derived operation is the associative product, $x \star y = xy$ for $y \in H(A)$, so the symmetrisation restricted there is the symmetrisation of the associative product and the identity holds. $\square$

**Remark.** Both constructions of the bilinear theory therefore require associativity, and for a full-type product associativity forces the twist to be invisible: the difference is that the Lie construction loses the associativity at the level of the *bracket* and has to migrate to the commutator on the skew half, whereas the Jordan construction loses it only off the Hermitian part and keeps it on the Hermitian half. The Jordan case is the sharper of the two, since the identity survives on half of the algebra instead of being replaced altogether.

---

## The Hermitian Jordan Algebra

### The Theorem

**Theorem.** The Hermitian part with the symmetrisation,

$$
J(A) = \bigl(H(A), \circ\bigr) , \qquad x \circ y = \tfrac12\bigl(xy + yx\bigr) \text{ for } x, y \in H(A) ,
$$

is a commutative Jordan algebra over the fixed ring $R^{\varsigma}$: the product is commutative and $R^{\varsigma}$-bilinear, and it satisfies the Jordan identity.

**Proof.** On $H(A)$ the derived operation is the associative product, so $\circ$ is the symmetrisation $\tfrac12(xy + yx)$ of that product, and the Jordan identity is inherited from the associativity of $A$; commutativity is by construction and the $R^{\varsigma}$-bilinearity is the scalar rule above. The development of the algebra, its axioms, its envelope, its trace form, its idempotents, its Peirce decomposition, its degree and its quadratic representation is *The Hermitian Jordan Algebra*. $\square$

**Remark.** The Jordan algebra is special, its envelope being the associative algebra $A$ with its involution, and every statement about $J(A)$ is an associative computation followed by a symmetrisation. The unit $1$ of $A$ is Hermitian and is the unit of $J(A)$, and the powers of a Hermitian element are its ordinary powers, $x^{\circ n} = x^{n}$.

### The Fixed Ring

**Theorem.** $H(A)$ is a module over the fixed ring $R^{\varsigma}$ and not over $R$ in general, and $J(A)$ is an algebra over $R^{\varsigma}$. A scalar with $\varsigma(\lambda) = -\lambda$ carries $H(A)$ onto $S(A)$, so it is not a scalar of the Jordan algebra.

**Proof.** For $\lambda \in R^{\varsigma}$ and $h \in H(A)$, $(\lambda h)^{*} = \varsigma(\lambda)h^{*} = \lambda h$, so $\lambda h \in H(A)$; for $\varsigma(\lambda) = -\lambda$ the same computation gives $(\lambda h)^{*} = -\lambda h \in S(A)$. The scalars preserving $H(A)$ are those with $(\varsigma(\lambda) - \lambda)H(A) = 0$, the fixed ring when $H(A)$ has zero annihilator in $R$ and possibly larger over a ring with zero divisors; this is *Hermitian and Skew-Hermitian Elements*, §*The Scalar Action*, and *The Unitary Lie Algebra*, §*The Scalars*, carries the counterexample. $\square$

**Remark.** This is the one structural difference between the sesquilinear Jordan theory and the bilinear one: over a field the self-adjoint part of *The Self-Adjoint Part of an Algebra* is a vector space over that field, whereas here the two halves are modules over the fixed ring and the Jordan algebra is an algebra over $R^{\varsigma}$. In the matrix model the fixed ring is $\mathbb{R}$, the Jordan algebra is a real Jordan algebra while the ambient algebra is a complex one, and the scalar $i$ is exactly the element that exchanges the two halves.

### The Action and the Functor

**Definition.** For $x \in H(A)$ the **quadratic representation** is

$$
U_{x}(y) = 2\,x \circ (x \circ y) - (x \circ x) \circ y ,
$$

which on the Hermitian part is $U_{x}(y) = xyx$; the identification and its properties are *The Hermitian Jordan Algebra*, §*The Quadratic Representation*.

**Proposition.** The assignments $A \mapsto H(A)$ and $A \mapsto J(A)$ are functorial: a morphism $\varphi$ of involutive $R$-algebras, $\varphi(xy) = \varphi(x)\varphi(y)$ and $\varphi(x^{*}) = \varphi(x)^{*}$, carries $H(A)$ into $H(B)$, and it is a homomorphism of Jordan algebras,

$$
\varphi(x \circ y) = \varphi(x) \circ \varphi(y) .
$$

**Proof.** $\varphi(x)^{*} = \varphi(x^{*}) = \varphi(x)$ for $x \in H(A)$, so $\varphi$ preserves the Hermitian elements; then $\varphi(x \circ y) = \tfrac12\varphi(xy + yx) = \tfrac12\bigl(\varphi(x)\varphi(y) + \varphi(y)\varphi(x)\bigr) = \varphi(x) \circ \varphi(y)$ by multiplicativity and additivity, and the scalars are respected because a morphism is $R$-linear and the fixed ring is contained in $R$. $\square$

**Remark.** The functor is the Jordan counterpart of the functor $A \mapsto S(A)$ of *Lie Algebras of Sesquialgebras*, which carries the same morphisms to homomorphisms of Lie algebras. The two functors are the two halves of the pair, and the scalar action is where their functoriality is anchored: both go to algebras over the fixed ring, and a *conjugate* morphism, which is $\varsigma$-semilinear rather than linear, respects the fixed ring too, since $\varsigma$ fixes it pointwise.

---

## The Ternary Structure

### The $J^{*}$-Algebra

**Definition.** An **algebraic $J^{*}$-algebra** is an $R$-module $V$ with a ternary product that is additive in each variable, $R$-linear in the first and the third, $\varsigma$-semilinear in the second, and satisfies the Jordan triple identity

$$
\{x, y, \{u, v, w\}\} = \{\{x,y,u\}, v, w\} - \{u, \{y,x,v\}, w\} + \{u, v, \{x,y,w\}\} .
$$

**Theorem (recalled).** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution and put $\{x,y,z\} = xy^{*}z$. Then $A$ with this ternary product is an algebraic $J^{*}$-algebra.

**Proof.** The parity statement and the Jordan triple identity are the theorem of *Algebraic J\*-Algebras*, §*The Derived Model*, where the identity is inherited from the associativity of $A$; the axioms are equational and name no binary product. $\square$

**Remark.** This is the structure that a sesquialgebra carries on its whole underlying module and with no involution fixed: the ternary product exists wherever the product and the involution do, and its identities are the ones the binary product cannot supply. It is the Jordan counterpart of the Lie triple system $[[x,y],z]$ of *Lie Algebras of Sesquialgebras*, and the two are the ternary layer of the sesquilinear kind.

### The Binary Product as a Shadow

**Theorem (recalled, the unital reading).** In the unital case the ternary product determines the binary one and the involution,

$$
\{x,y,1\} = x \star y , \qquad \{1,y,1\} = y^{*} , \qquad xy = x \star y^{*} ,
$$

so the derived operation, the involution and the associative product are recovered from the ternary product by inserting the unit.

**Proof.** $\{x,y,1\} = xy^{*}1 = x \star y$ and $\{1,y,1\} = y^{*}$; then $x \star y^{*} = x(y^{*})^{*} = xy$. This is *Algebraic J\*-Algebras*, §*The Binary Product as a Shadow*. $\square$

**Remark.** The recovery is a property of the unital examples and not a consequence of the axioms: the axioms carry no unit, and *Algebraic J\*-Algebras* exhibits a subspace of $M_{2}(\mathbb{C})$, the matrices with zero diagonal, closed under the ternary product and not under the binary one. The Jordan algebra of the previous section is recovered from the ternary structure in the same way, by restricting to the Hermitian elements at the unit: $H(A) = \{x : \{1,x,1\} = x\}$, and there the symmetrisation is read from the ternary product at the unit, $x \circ y = \tfrac12\bigl(\{x,y,1\} + \{y,x,1\}\bigr)$.

### The Jordan Triple System

**Remark.** Impose $\varsigma = \mathrm{id}$ and let the algebra be commutative. Then the middle slot of the ternary product is linear, and the model acquires the outer symmetry $\{x,y,z\} = \{z,y,x\}$: the algebraic $J^{*}$-algebra specialises to a **Jordan triple system** in the sense of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*. The two reductions are independent — the linearity of the middle slot is a matter of the base involution and the symmetry a matter of the commutativity — and neither makes the involution the identity. The Jordan triple system is therefore the commutative bilinear specialisation of the $J^{*}$-algebra, and the $J^{*}$-algebra is its sesquilinear generalisation, which is the direction this article reads.

---

## The Boundary

### Specialness

**Theorem.** $J(A)$ is a special Jordan algebra, with envelope the associative algebra $A$ and its involution, and it is a Jordan subalgebra of the symmetrisation $A^{+}$ of $A$.

**Proof.** $H(A)$ is closed under $\circ$, so $J(A)$ is a subalgebra of $A^{+}$, which is the definition of specialness, the envelope being $A$; *Special and Exceptional Jordan Algebras*. $\square$

**Remark.** The envelope is the whole associative algebra and not the Hermitian part, and this is why every computation in $J(A)$ is an associative one. Nothing in the construction can leave the special class: an involution can cut a piece out of an associative algebra, and every piece so obtained is special.

### The Exceptional Case

**Theorem (the exceptional algebras are outside the class).** The Albert algebra is an exceptional Jordan algebra, so it is not isomorphic to $J(A) = \bigl(H(A), \circ\bigr)$ for any associative $R$-algebra $A$ with a $\varsigma$-semilinear involution.

**Proof.** $J(A)$ is special by the theorem above, and the Albert algebra is exceptional, that is not special, by *Special and Exceptional Jordan Algebras*; a Jordan algebra isomorphic to a special one would be special. $\square$

**Remark.** This is the sharpest boundary of the article, and it is a boundary of principle rather than of computation: the sesquilinear construction produces exactly the special Jordan algebras, and the exceptional ones are reached only by a construction that does not pass through an associative envelope, as the octonion and Cayley–Dickson routes of *Special and Exceptional Jordan Algebras* do. In the sesquilinear layer the obstruction is the algebra structure itself: the ternary product is defined by the associative product and the involution, and no involution on an associative algebra produces the Albert algebra.

---

## The Scalars and the Bilinear Case

**Theorem (the degeneration).** Put $\varsigma = \mathrm{id}$. Then the derived operation is $R$-bilinear, the fixed ring is all of $R$, $H(A)$ is the self-adjoint part of an involutive $R$-algebra, and $J(A)$ is the self-adjoint part of *The Self-Adjoint Part of an Algebra* together with its Jordan structure; the ternary structure is the Jordan triple system when $A$ is commutative, and the algebraic $J^{*}$-algebra otherwise.

**Proof.** With $\varsigma = \mathrm{id}$ the second scalar rule is the first, so $x\star y = xy^{*}$ is $R$-bilinear, $H(A)$ is an $R$-submodule, and the statements are the definitions read at $\varsigma = \mathrm{id}$; the ternary statement is the comparison of *Algebraic J\*-Algebras*, §*The Comparison with the Jordan Triple Systems*. $\square$

**Remark.** As in the Lie case the degeneration has two independent steps: $\varsigma = \mathrm{id}$ makes the product bilinear and the scalars all of $R$, and $* = \mathrm{id}$ makes the derived operation the product, in which case $H(A)$ is all of $A$ and the Jordan algebra is the symmetrisation of $A$ itself.

The two cases are collected in the table.

| | bilinear, $\varsigma = \mathrm{id}$ | sesquilinear, $\varsigma \neq \mathrm{id}$ |
|---|---|---|
| the symmetrisation | a Jordan product on all of $A$ when $* = \mathrm{id}$ | a Jordan product on $H(A)$, and only there |
| the Jordan identity | inherited from the associativity of the product | holds on $H(A)$, fails off it |
| the scalars | $R$ | $R^{\varsigma}$ |
| the fixed scalar $i$ | a scalar | exchanges $H(A)$ and $S(A)$ |
| the image of $\circ$ | $A$ | $H(A)$, for all pairs of arguments |
| the ternary companion | the Jordan triple system of the commutative case | the algebraic $J^{*}$-algebra |
| the boundary | the special algebras | the special algebras, the exceptional ones excluded |

## Examples

### The Complex Matrices

For $A = M_{n}(\mathbb{C})$ with the conjugate transpose, $H(A)$ is the space of the Hermitian matrices and $J(A)$ is that space with the symmetrised product $\tfrac12(xy + yx)$, a Jordan algebra over $\mathbb{R}$; its degree is $n$, its idempotents are the orthogonal projections, and at $E_{11}$ its Peirce spaces are $\mathbb{R}E_{11}$, the Hermitian off-diagonal matrices and $\mathbb{R}E_{22}$, with the eigenvalues $1, \tfrac12, 0$. Off $H(A)$ the symmetrisation is Hermitian-valued but not Jordan, with the witness of $M_{2}(\mathbb{C})$ above.

### The Field

For $A = \mathbb{C}$ over $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation and $x \star y = x\bar y$, the Hermitian elements are the reals, so $J(A) = \mathbb{R}$ with the ordinary multiplication, the smallest case in which the fixed ring is a proper subring of $R$ and the Jordan algebra a real form of the algebra. The symmetrisation is $x \circ y = \mathrm{Re}(x\bar y)$, which lands in $\mathbb{R}$ for all pairs.

### The Quaternions

For $A = \mathbb{H}$ with the quaternion conjugation over $(\mathbb{R},\mathrm{id})$ the twist is invisible, the case is bilinear, the Hermitian elements are the real quaternions, and $J(A) = \mathbb{R}$; it is the case in which the sesquilinear Jordan theory and the bilinear one coincide, recorded to mark the boundary.

### The Biquaternion Algebra

For $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the star-involution the Hermitian subspace is a Jordan algebra of degree two, isomorphic to $H_{2}(\mathbb{C})$, with two orthogonal idempotents and the Peirce spaces read in *Biquaternion Jordan Algebras* and *The Six Subspaces and the Jordan Algebra*. That layer is the worked case of the whole article, the ternary structure being the $J^{*}$-algebra of the biquaternion algebra and the binary one the Hermitian Jordan algebra of degree two.

## Summary

A sesquialgebra carries its Jordan structure on the Hermitian half and its ternary structure on the whole module. The symmetrisation $x \circ y = \tfrac12(x \star y + y \star x)$ is commutative and additive, it is linear over the fixed ring $R^{\varsigma}$ and not over $R$, and its image is contained in $H(A)$ for all pairs of arguments. It is a Jordan product exactly where the product being symmetrised is associative: on $H(A)$, where the derived operation coincides with the associative product, the Jordan identity holds and $J(A) = (H(A), \circ)$ is a commutative Jordan algebra over $R^{\varsigma}$, functorially in the involutive algebra and special with envelope $A$; off $H(A)$ the identity fails, with the witness $E_{12}, E_{22}$ in $M_{2}(\mathbb{C})$, and the criterion that would repair it is associativity of the derived product, which for an algebra of full type forces the twist to be invisible, so the genuinely sesquilinear case is exactly the case where the failure occurs.

What exists on the whole module is the ternary product $\{x,y,z\} = xy^{*}z$ of an algebraic $J^{*}$-algebra, whose Jordan triple identity is inherited from the associativity of the enveloping product and whose binary product is recovered only by inserting a unit. That ternary structure is the Jordan counterpart of the Lie triple system of the companion article, and it specialises to a Jordan triple system when the base involution is trivial and the algebra is commutative. The class of Jordan algebras obtained this way is the class of the special algebras, and the exceptional Jordan algebras, the Albert algebra among them, are outside it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $x \circ y = \tfrac12(x \star y + y \star x)$ | the symmetrisation of the sesquilinear product |
| $x \circ x = xx^{*}$ | the square, the polarised diagonal |
| $J(A) = (H(A), \circ)$ | the Hermitian Jordan algebra, an algebra over $R^{\varsigma}$ |
| $H(A) = \{x : x^{*} = x\}$ | the Hermitian elements, the underlying module of $J(A)$ |
| $R^{\varsigma}$ | the fixed ring, the scalars of $J(A)$ |
| $\{x,y,z\} = xy^{*}z$ | the ternary product of the algebraic $J^{*}$-algebra |
| $\{x,y,1\} = x \star y$, $\{1,y,1\} = y^{*}$ | the unital reading, recovering the binary product |
| $\{x,y,z\} = \{z,y,x\}$ | the outer symmetry, present in the Jordan triple system only |
| $U_{x}(y) = 2\,x\circ(x\circ y) - (x\circ x)\circ y = xyx$ | the quadratic representation |
| $A^{+}$ | the symmetrisation of $A$, the envelope of $J(A)$ |
| $E_{12}, E_{22}$ | the witness pair in $M_2(\mathbb{C})$ for the failure off $H(A)$ |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the symmetrisation of an associative algebra, the special algebras, their envelopes and the Jordan identity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebras, the quadratic representation and the Peirce decomposition.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the Jordan triple systems and the ternary product as a primary object.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), and Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the ternary product of a $J^{*}$-algebra read algebraically.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions and the two halves they cut.
- The companion articles of this series: *Sesquialgebras*, *The Sesquilinear Product*, *Hermitian and Skew-Hermitian Elements*, *The Sesquilinear Symmetrised Product*, *The Hermitian Jordan Algebra*, *Algebraic J\*-Algebras*, *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*, and *Lie Algebras of Sesquialgebras*.
