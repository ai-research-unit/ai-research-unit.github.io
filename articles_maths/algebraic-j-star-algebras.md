# __Algebraic J\*-Algebras__

## Introduction

A $\varsigma$-sesquilinear product produces a ternary operation, and the ternary operation carries the identities that the binary product cannot: the associator of the binary product is uncontrolled, while the ternary product satisfies the Jordan triple identity, by *The Sesquilinear Associator and the Ternary Product*. This article takes the ternary operation as the primitive datum and writes the identities it satisfies, with no binary product assumed. The result is the **algebraic $J^{*}$-algebra**, the norm-free and topology-free form of the $J^{*}$-algebra of Harris; the Banach version is *The Topological J\*-Algebra*.

What is recalled and what is added: the model $\{x,y,z\} = xy^{*}z$ of an associative algebra with a $\varsigma$-semilinear involution, its Jordan triple identity, and the recovery of the binary product by inserting a unit are in *The Sesquilinear Associator and the Ternary Product*; what is added is the abstract axiom system, its parity read as a triple system, the witness that the axioms determine no binary product, and the comparison with the Jordan triple systems of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*.

Throughout, $R$ is a commutative ring with $1$ and $\varsigma$ is an involution of $R$; the classical case is $R = \mathbb{C}$ with $\varsigma(z) = \bar z$, and a module over a ring is written $V$ to leave $A$ for the algebras.

## The Axioms

### Definition

**Definition.** An **algebraic $J^{*}$-algebra** on an $R$-module $V$ is a map $\{\cdot,\cdot,\cdot\} : V \times V \times V \to V$ that is additive in each variable, $R$-linear in the first and the third variables, $\varsigma$-semilinear in the second,

$$
\{\lambda x, y, z\} = \lambda \{x,y,z\}, \qquad \{x, \lambda y, z\} = \varsigma(\lambda) \{x,y,z\}, \qquad \{x, y, \lambda z\} = \lambda \{x,y,z\},
$$

and satisfies the Jordan triple identity

$$
\{x, y, \{u, v, w\}\} = \{\{x, y, u\}, v, w\} - \{u, \{y, x, v\}, w\} + \{u, v, \{x, y, w\}\} .
$$

**Remark.** The axioms are equational and norm-free: no norm, no completeness and no topology appears, and the adjectives of the title name exactly this absence. For $\varsigma = \mathrm{id}$ the definition is that of a Jordan triple system without the symmetry axiom, and for $R = \mathbb{C}$, $\varsigma(z) = \bar z$ it is the classical algebraic $J^{*}$-algebra. Nothing in the definition names a binary product, and the rest of the article is largely about what that omission costs and what it buys.

### The Parity

**Proposition.** The parities of the ternary product are linear, $\varsigma$-semilinear, linear; read on the conjugate module of *Conjugate-Linear Maps and the Conjugate Dual*, the ternary product is an $R$-trilinear map

$$
V \times V^{\varsigma} \times V \longrightarrow V .
$$

**Proof.** The middle slot carries the single conjugation and the outer slots carry none, which is the definition; reading the middle variable on $V^{\varsigma}$ converts its $\varsigma$-semilinearity into linearity. $\square$

**Remark.** The parity (linear, conjugate, linear) is the ternary form of the parity rule of the block: one slot is conjugated and the two others are not, and the bookkeeping "one conjugation for each conjugate slot" is the same one that governs the conjugate dual, the transpose and the transport of *Conjugate-Linear Maps and the Conjugate Dual*. The operator form of the defining identity,

$$
[L(x,y), L(u,v)] = L(\{x,y,u\}, v) - L(u, \{y,x,v\}), \qquad L(x,y)z = \{x,y,z\},
$$

turns the identity into a commutation relation of the operators $L(x,y)$, which are taken up in *The Ternary Product as an Operator*.

## The Model and the Shadow

### The Derived Model

**Theorem.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, and put $\{x,y,z\} = xy^{*}z$. Then $A$ with this ternary product is an algebraic $J^{*}$-algebra.

**Proof.** The ternary product is additive in each variable, and it is linear in $x$ and in $z$ because the multiplication of $A$ is bilinear. In the middle variable, $(\lambda y)^{*} = \varsigma(\lambda) y^{*}$ and the scalar $\varsigma(\lambda)$ is central, so $\{x, \lambda y, z\} = x\,\varsigma(\lambda)\, y^{*} z = \varsigma(\lambda)\, x y^{*} z = \varsigma(\lambda)\{x,y,z\}$; the conjugation comes from the involution alone, the outer slots meeting no conjugation. The Jordan triple identity is the identity theorem of *The Sesquilinear Associator and the Ternary Product*. $\square$

**Remark.** This is the model of the theory. The classical instance is the space $\mathcal{L}(H,K)$ of bounded operators between two Hilbert spaces, with $\{x,y,z\} = xy^{*}z$ and the adjoint as the involution; the norm appears only to define the adjoint, which is the datum the ternary product needs. When $H \neq K$ the space is closed under the ternary product but not under the binary one, because two maps $H \to K$ cannot be composed, and this is the classical instance of the gap that the next theorem exhibits in finite dimensions. The finite-dimensional model is $A = M_n(\mathbb{C})$ with the conjugate transpose, worked in *Matrix Sesqualgebras*, and the model over the biquaternion algebra is worked in *Introduction to the General Plain Sesqualgebra of Biquaternions*.

### The Binary Product as a Shadow

**Proposition (the unital reading).** Let $A$ be a unital associative $R$-algebra with a $\varsigma$-semilinear involution and the ternary product $\{x,y,z\} = xy^{*}z$. Then $\{x,y,1\} = x \star y$ and $\{1,y,1\} = y^{*}$, so the binary derived operation and the involution are read from the ternary product by inserting the unit, and the original product is recovered as $xy = x \star y^{*}$.

**Proof.** The theorem of *The Sesquilinear Associator and the Ternary Product*: $\{x,y,1\} = (x \star y) \star 1 = xy^{*}$ and $\{1,y,1\} = y^{*}$, and $x \star y^{*} = x (y^{*})^{*} = xy$. $\square$

**Remark.** In the unital case the binary product is the shadow of the ternary one, and not the reverse: the ternary product determines the derived operation, the involution and the original product, while the derived operation alone determines neither the involution nor the unit. But the unit is not part of the axioms, and the recovery is a property of the unital examples rather than a consequence of the axioms. The next theorem exhibits an algebraic $J^{*}$-algebra that is not an algebra, closed under the ternary product and not under the product; this is the reason the axioms name the ternary operation, which is the operation that survives when the binary one is not available.

### A $J^{*}$-Algebra that is Not an Algebra

**Theorem (a $J^{*}$-algebra that is not an algebra).** Let $W$ be the subspace of $M_2(\mathbb{C})$ of the matrices with zero diagonal,

$$
W = \left\{ \begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix} : a, b \in \mathbb{C} \right\},
$$

with $\varsigma(z) = \bar z$ and the ternary product $\{x,y,z\} = xy^{*}z$ inherited from $M_2(\mathbb{C})$. Then $W$ is a $*$-invariant algebraic $J^{*}$-algebra, and $W$ is not closed under the binary product of $M_2(\mathbb{C})$.

**Proof.** Let $x = \begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix}$, $y = \begin{pmatrix} 0 & p \\ q & 0 \end{pmatrix}$ and $z = \begin{pmatrix} 0 & c \\ d & 0 \end{pmatrix}$, so that $y^{*} = \begin{pmatrix} 0 & \bar q \\ \bar p & 0 \end{pmatrix} \in W$. Then

$$
xy^{*} = \begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix}\begin{pmatrix} 0 & \bar q \\ \bar p & 0 \end{pmatrix} = \begin{pmatrix} a\bar p & 0 \\ 0 & b\bar q \end{pmatrix},
\qquad
xy^{*}z = \begin{pmatrix} a\bar p & 0 \\ 0 & b\bar q \end{pmatrix}\begin{pmatrix} 0 & c \\ d & 0 \end{pmatrix} = \begin{pmatrix} 0 & a\bar p c \\ b\bar q d & 0 \end{pmatrix} \in W ,
$$

so $W$ is closed under the ternary product, and it is $*$-invariant because $y^{*} \in W$. Being the restriction of the ternary product of $M_2(\mathbb{C})$, it is additive, linear in the outer slots, conjugate-linear in the middle, and satisfies the Jordan triple identity, which is an identity of $M_2(\mathbb{C})$. The binary product, however, is

$$
xz = \begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix}\begin{pmatrix} 0 & c \\ d & 0 \end{pmatrix} = \begin{pmatrix} ad & 0 \\ 0 & bc \end{pmatrix},
$$

which is diagonal and hence outside $W$ as soon as $ad \neq 0$ or $bc \neq 0$; so $W$ is not closed under the product. $\square$

**Remark.** The witness shows that a $J^{*}$-algebra need not be an algebra. $W$ is a subtriple of $M_2(\mathbb{C})$ — it is closed under the ternary product — but it is not a subalgebra, since the product of two of its elements is diagonal; the ternary structure therefore exists on a space that carries no binary product, and the axioms are those of a space closed under the ternary operation rather than of an algebra. The involution is an operation of $W$, which is $*$-invariant, so the failure is not a matter of the involution but of the product alone: $W$ is even a $*$-subspace, and still not a subalgebra. The binary product is what the axioms decline to require, and it is present in the model only because the model begins with an algebra. This is Harris's definition of a $J^{*}$-algebra: a space closed under $xy^{*}z$, not assumed closed under $xy$.

## The Relation to the Jordan Triple Systems

### The Outer Symmetry

**Proposition (the outer symmetry is not an axiom).** The defining axioms do not include the outer symmetry $\{x,y,z\} = \{z,y,x\}$, and it is not a consequence: on $M_2(\mathbb{C})$ with $\varsigma(z) = \bar z$,

$$
\{E_{12}, E_{11}, E_{11}\} = 0 \neq E_{12} = \{E_{11}, E_{11}, E_{12}\} .
$$

**Proof.** $\{E_{12}, E_{11}, E_{11}\} = E_{12}E_{11}E_{11} = (E_{12}E_{11})E_{11} = 0$, since $E_{12}E_{11} = 0$; and $\{E_{11}, E_{11}, E_{12}\} = E_{11}E_{11}E_{12} = E_{11}E_{12} = E_{12}$. $\square$

**Remark.** The Hermitian symmetry of the derived ternary product, $\{x,y,z\}^{*} = \{z^{*},y^{*},x^{*}\}$ of *The Sesquilinear Associator and the Ternary Product*, is not the outer symmetry and does not imply it. The outer symmetry is a genuinely extra axiom, and it fails for the noncommutative model, as the example above shows.

### The Comparison with the Jordan Triple Systems

**Proposition.** Impose $\varsigma = \mathrm{id}$ and let the model algebra be commutative. Then $\varsigma = \mathrm{id}$ makes the involution $*$ $R$-linear, so $\{x,y,z\} = xy^{*}z$ is $R$-trilinear in all three slots; commutativity gives $xy^{*}z = zy^{*}x$, the outer symmetry; and the Jordan triple identity holds by the model theorem. The model is therefore a Jordan triple system of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*.

**Proof.** With $\varsigma = \mathrm{id}$, $(\lambda y)^{*} = \lambda y^{*}$, so the middle slot is linear like the outer two and the product is trilinear. Commutativity gives $xy^{*}z = zy^{*}x$, the outer symmetry. The Jordan triple identity is the model theorem. $\square$

**Remark.** With the base ring and its involution fixed, the two axiom systems differ in exactly two places: the parity of the middle slot, which is $\varsigma$-semilinear for the $J^{*}$-algebra and linear for the Jordan triple system, and the outer symmetry, which the $J^{*}$-algebra omits and the Jordan triple system requires. Note that $\varsigma = \mathrm{id}$ does **not** make the involution the identity map: $*$ remains an $R$-linear order-two map, and the product remains $xy^{*}z$, which equals $xyz$ only when $* = \mathrm{id}$ as well. What $\varsigma = \mathrm{id}$ supplies is the linearity of the middle slot and, with commutativity, the outer symmetry; the involution itself is still carried, and dropping it is the further specialisation $* = \mathrm{id}$. The Jordan triple system is therefore the commutative specialization of the algebraic $J^{*}$-algebra at $\varsigma = \mathrm{id}$, and the $J^{*}$-algebra is its sesquilinear generalisation. The two reductions are independent: the conjugation is a matter of the base involution, and the symmetry is a matter of the commutativity of the model. The classical $J^{*}$-algebra of operators drops both, being neither commutative nor identity-involutive.

## Summary

An algebraic $J^{*}$-algebra is an $R$-module $V$ with a ternary product that is additive in each variable, $R$-linear in the first and third variables, $\varsigma$-semilinear in the second, and satisfies the Jordan triple identity; the axioms are equational and norm-free, and they name no binary product. The parities are (linear, conjugate, linear), so the product is $R$-trilinear as a map $V \times V^{\varsigma} \times V \to V$, in the same parity bookkeeping as the conjugate dual. The model is the derived operation $\{x,y,z\} = xy^{*}z$ of an associative algebra with a $\varsigma$-semilinear involution, whose Jordan triple identity is inherited from the associativity of the algebra. The binary product is the shadow of the ternary one in the unital case, where $\{x,y,1\} = x \star y$ and $\{1,y,1\} = y^{*}$ recover the derived operation, the involution and the product $xy = x \star y^{*}$, but the axioms carry no unit and no binary product, and the subspace of $M_2(\mathbb{C})$ of the matrices with zero diagonal is a $*$-invariant $J^{*}$-algebra closed under the triple product and not under the product. The outer symmetry $\{x,y,z\} = \{z,y,x\}$ is not an axiom and fails for the noncommutative model, while the Jordan triple system of the bilinear layer adds it and removes the conjugation, so the model specialises to a Jordan triple system when the algebra is commutative and $\varsigma = \mathrm{id}$. The ternary product, and not the binary one, is the natural home of the identities because it is the operation that survives where the binary one is absent, and because the identity it carries is the one the binary product cannot.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\{x,y,z\}$ | the ternary product of the $J^{*}$-algebra |
| $V \times V^{\varsigma} \times V \to V$ | the ternary product as an $R$-trilinear map, the middle slot conjugated |
| $L(x,y)z = \{x,y,z\}$ | the operator attached to a pair, taken up in *The Ternary Product as an Operator* |
| $\{x,y,z\} = xy^{*}z$ | the derived model of an associative algebra with an involution |
| $\{x,y,1\} = x \star y$, $\{1,y,1\} = y^{*}$ | the unital reading, which recovers the binary product and the involution |
| $\{x,y,z\} = \{z,y,x\}$ | the outer symmetry, absent from the axioms and present in the Jordan triple system |

## Further Reading

- L. A. Harris, *Bounded Symmetric Homogeneous Domains in Infinite Dimensional Spaces* (Lecture Notes in Mathematics 364, Springer, 1974), for the origin of the $J^{*}$-algebra: a space of operators closed under $xy^{*}z$ and not assumed closed under $xy$, which is exactly the gap of this article.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the Jordan triple systems and the ternary product as a primary object, of which the binary product is a derived notion.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the ternary product of a $J^{*}$-algebra read algebraically, without the norm.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the algebra-free theory of the $J^{*}$-triple and the ternary product as the carrier of the identities, which is the layer of this category.
- Bernard Russo, *Structure of JB\*-Triples* (in *Jordan Algebras*, Oberwolfach 1992, de Gruyter, 1994), for the classification of the triple systems that the axioms generate when a norm is added, the boundary with the next category.
