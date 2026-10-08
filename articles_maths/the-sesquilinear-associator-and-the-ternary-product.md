# __The Sesquilinear Associator and the Ternary Product__

## Introduction

The product of a sesqualgebra is linear in the first slot and $\varsigma$-semilinear in the second, and this asymmetry makes associativity an unstable condition: for an algebra of full type with a nontrivial involution the product is **never** associative, by the collapse of *Sesqualgebras*. What measures the failure is the **associator** $[x,y,z] = (x \star y) \star z - x \star (y \star z)$, and what the failure forces is the **ternary product**, the three-variable operation on which the identities that the binary product cannot carry are read.

This article computes the associator of a general sesquilinear product and records the **twist** it carries: the two groupings of the variables are trilinear on two **different** modules, so the associator is a difference of two trilinear maps and not a trilinear map itself. It then describes the passage to the ternary product, whose parity is the ternary form of the binary one and which determines the binary product in return. The associator of the derived operation $x \star y = xy^{*}$, its value $x\bigl((zy)^{*} - zy^{*}\bigr)$ and the associativity criterion are proved in *Sesqualgebras* and are recalled here in the associator notation; the ternary product and its Jordan triple identity are in the same article, and what is added here is the parity of the associator, the twisted-trilinear form of the two groupings, and the recovery of the binary product from the ternary one.

Throughout, $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and $A$ is an $R$-module with a $\varsigma$-sesquilinear product $\star$; the conjugate module $A^{\varsigma}$ and the convention that the product is the bilinear map $A \times A^{\varsigma} \to A$ are those of *Sesqualgebras* and *The Sesquilinear Product*.

## The Associator

### Definition and Parity

**Definition.** The **associator** of $x, y, z \in A$ is

$$
[x, y, z] = (x \star y) \star z - x \star (y \star z) .
$$

**Proposition.** The associator is additive in each variable, $R$-linear in the first variable, and $\varsigma$-semilinear in the second; it vanishes identically if and only if the product is associative.

**Proof.** Both groupings are additive in each variable, because the product is, so the difference is; in the first variable, both groupings are linear, so $[\lambda x, y, z] = \lambda [x, y, z]$; in the second variable, both groupings are $\varsigma$-semilinear, so $[x, \lambda y, z] = \varsigma(\lambda)[x, y, z]$. The product is associative exactly when the two groupings agree for all $x, y, z$, which is the vanishing of the difference. $\square$

**Remark.** With the third variable fixed the associator is $R$-bilinear as a map $A \times A^{\varsigma} \to A$ in its first two variables, and the vanishing criterion is the sense in which the associator measures associativity without deciding it: associativity is an identity of two products, and the associator is the difference of those two products, so "associative" is exactly "$[\,,\,,\,] = 0$".

### The Twist in the Third Slot

**Theorem (the two groupings live on two different modules).** Put $A(x,y,z) = (x \star y) \star z$ and $B(x,y,z) = x \star (y \star z)$, so that $[x, y, z] = A(x,y,z) - B(x,y,z)$. Then $A$ is $R$-trilinear as a map $A \times A^{\varsigma} \times A^{\varsigma} \to A$, and $B$ is $R$-trilinear as a map $A \times A^{\varsigma} \times A \to A$. In particular

$$
A(x, y, \lambda z) = \varsigma(\lambda) A(x,y,z), \qquad B(x, y, \lambda z) = \lambda B(x,y,z),
$$

so

$$
[x, y, \lambda z] = \varsigma(\lambda) A(x,y,z) - \lambda B(x,y,z),
$$

which is neither $\lambda [x,y,z]$ nor $\varsigma(\lambda)[x,y,z]$ unless $[x,y,z] = 0$.

**Proof.** For $A$: it is linear in $x$ because it is a product in the first slot of an outer product; its second variable passes through the inner product as a second slot and then through the outer product as a first slot, so it is $\varsigma$-semilinear in $y$; its third variable is the second slot of the outer product, so $A(x,y,\lambda z) = \varsigma(\lambda) A(x,y,z)$. Reading the second variable on $A^{\varsigma}$ and the third on $A^{\varsigma}$ makes $A$ trilinear. For $B$: it is linear in $x$; its second variable is the first slot of the inner product and then the second slot of the outer product, hence $\varsigma$-semilinear in $y$; its third variable is the second slot of the inner product and then the second slot of the outer product, and the two conjugations cancel, so $B(x,y,\lambda z) = \lambda B(x,y,z)$. Reading the second variable on $A^{\varsigma}$ makes $B$ trilinear on $A \times A^{\varsigma} \times A$. The last display is the two scalar rules subtracted. $\square$

**Remark.** The two groupings are not two trilinear maps on the same module: the third slot is on $A^{\varsigma}$ for $A$ and on $A$ for $B$, and no single module makes both linear in that slot. The associator is therefore the difference of a trilinear map and a trilinear map of the other parity in the third slot, and it is not homogeneous in that slot. This is the twist the associator carries, and it is why the associator is not itself a trilinear object: it carries one definite parity in each of the first two slots and a difference of parities in the third.

**Corollary.** An algebra of full type with a nontrivial involution is not associative; its associator is not identically zero, and the two trilinear groupings $A$ and $B$, which live on two different modules, are distinct maps.

**Proof.** The collapse theorem of *Sesqualgebras*: associativity forces $\varsigma = \mathrm{id}$ for an algebra of full type. So with $\varsigma \neq \mathrm{id}$ the product is not associative, and by the proposition above the associator does not vanish identically, which is $A \neq B$ somewhere. $\square$

### The Associator of the Derived Product

**Proposition.** For the derived operation $x \star y = xy^{*}$ of an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, the associator is

$$
[x, y, z] = x\bigl((zy)^{*} - zy^{*}\bigr),
$$

which is $R$-linear in $x$ and $\varsigma$-semilinear in $y$, in agreement with the general theorem.

**Proof.** This is the associator proposition of *Sesqualgebras*, read in the present notation: $(x \star y) \star z = xy^{*}z^{*}$ and $x \star (y \star z) = xz y^{*}$, whose difference is $x(y^{*}z^{*} - zy^{*}) = x((zy)^{*} - zy^{*})$. $\square$

**Corollary.** The derived operation is associative if and only if $x\bigl((zy)^{*} - zy^{*}\bigr) = 0$ for all $x, y, z$. For an $A$ with zero left annihilator this is the condition $(zy)^{*} = zy^{*}$ for all $y, z$, and for a unital $A$ it holds if and only if the involution is the identity; the proof is in *Sesqualgebras*.

**Remark.** Two readings of the same proposition: the derived operation of a unital algebra with a nontrivial involution is never associative, and its associator is $R$-linear in the first variable, $\varsigma$-semilinear in the second and of mixed parity in the third, exactly as the general theorem prescribes.

## The Ternary Product

### Definition and Parity

**Definition.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution. The **ternary product** attached to the derived operation is

$$
\{x, y, z\} = (x \star y) \star z^{*} = xy^{*}z .
$$

**Proposition.** The ternary product is additive in each variable, $R$-linear in the first and the third variables, and $\varsigma$-semilinear in the middle variable; it satisfies the Hermitian symmetry $\{x,y,z\}^{*} = \{z^{*}, y^{*}, x^{*}\}$, and the plain symmetry $\{x,y,z\} = \{z,y,x\}$ fails as soon as the algebra is noncommutative.

**Proof.** The parity is read from $xy^{*}z$: a scalar in $x$ or in $z$ is a scalar of one of the products, and a scalar in $y$ meets the involution and is sent to $\varsigma(\lambda)$. The symmetry is $(xy^{*}z)^{*} = z^{*}yx^{*} = \{z^{*}, y^{*}, x^{*}\}$; the plain symmetry would read $xy^{*}z = zy^{*}x$. $\square$

**Remark.** The parity of the ternary product is the parity of the binary product with one slot promoted: the binary product is linear in the first slot and $\varsigma$-semilinear in the second, and the ternary product is linear in the two outer slots and $\varsigma$-semilinear in the middle. The middle slot is where the conjugation sits, and the two outer slots are the linear slots that flank it; the ternary product is not a linearisation of the binary one — the two do not even have the same number of arguments — but the parity of the middle slot is the parity of the second slot of the binary product, and the outer slots carry no conjugation.

### The Jordan Triple Identity

**Theorem.** The ternary product satisfies the Jordan triple identity

$$
\{x, y, \{u, v, w\}\} = \{\{x, y, u\}, v, w\} - \{u, \{y, x, v\}, w\} + \{u, v, \{x, y, w\}\} ,
$$

the proof being a finite expansion in the products and the involution, using only the associativity of $A$ and $(uv)^{*} = v^{*}u^{*}$. The verification is in *Algebraic J\*-Algebras*, where the identity is the defining axiom of the $J^{*}$-triple.

**Remark.** The ternary product satisfies a three-variable identity while the binary product carries no associativity identity of its own: the associator of the binary product is a three-variable map with no identity attached to it, and the ternary product is the operation that carries the identity instead. The Jordan triple identity is what remains of the associative law after the operation is twisted by the involution, and it is the reason the ternary product, and not the binary one, is the natural carrier of the structure; the general theory of the triple systems that carry it is *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System* and *Jordan Algebras*.

### The Passage from the Binary to the Ternary Product

**Theorem (the binary product is the shadow of the ternary one).** Let $A$ be unital with unit $1$. Then

$$
\{x, y, 1\} = x \star y, \qquad \{1, y, 1\} = y^{*},
$$

so the ternary product determines the binary derived operation and the involution; since the original product is $xy = x \star y^{*}$, with $y^{*} = \{1,y,1\}$, the ternary product determines the algebra as well.

**Proof.** $\{x,y,1\} = (x \star y) \star 1^{*} = (x \star y) \star 1 = xy^{*}1 = xy^{*} = x \star y$, and $\{1,y,1\} = (1 \star y) \star 1^{*} = y^{*} \star 1 = y^{*}$. The original product is then $xy = x \star y^{*}$, because $(y^{*})^{*} = y$. $\square$

**Remark.** The ternary product carries strictly more than the binary one: from $\{x,y,1\}$ one recovers the derived operation, and from $\{1,y,1\}$ the involution, while the derived operation alone does not determine the involution, which is part of the datum by *Sesqualgebras*. This is the precise sense in which the binary product is read as the **shadow** of the ternary one: the binary operation is the ternary operation with the unit in the third slot, and the whole ternary operation is what the failure of associativity forces one to consider.

**Remark (the passage in one line).** The binary product has an uncontrolled associator and carries no associativity identity, and the ternary product has a controlled associator — the Jordan triple identity — and it determines the binary product; the passage from the binary to the ternary operation is therefore the passage from a product whose associator is a defect to a triple product whose identity is a structure. The operator theory of the ternary product, its quadratic representation $z \mapsto \{x,y,z\}$ and the adjoint it carries, is *The Adjoint of the Ternary Product*.

## Summary

The associator $[x,y,z] = (x \star y) \star z - x \star (y \star z)$ measures the failure of associativity of a sesquilinear product; it vanishes identically exactly when the product is associative, it is $R$-linear in the first variable and $\varsigma$-semilinear in the second, and it carries a twist in the third: the two groupings are $R$-trilinear on $A \times A^{\varsigma} \times A^{\varsigma}$ and on $A \times A^{\varsigma} \times A$ respectively, so the associator is the difference of two trilinear maps on two different modules and is not homogeneous in its third variable. For the derived operation $x \star y = xy^{*}$ the associator is $x\bigl((zy)^{*} - zy^{*}\bigr)$, and an algebra of full type with a nontrivial involution is never associative. What the failure forces is the ternary product $\{x,y,z\} = xy^{*}z$, which is linear in the outer slots and $\varsigma$-semilinear in the middle, satisfies the Hermitian symmetry $\{x,y,z\}^{*} = \{z^{*},y^{*},x^{*}\}$, satisfies the Jordan triple identity, and determines the binary product and the involution through $\{x,y,1\} = x \star y$ and $\{1,y,1\} = y^{*}$; the binary product is the shadow of the ternary one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $[x,y,z]$ | the associator $(x \star y) \star z - x \star (y \star z)$ |
| $A(x,y,z)$, $B(x,y,z)$ | the two groupings $(x \star y) \star z$ and $x \star (y \star z)$ |
| $A \times A^{\varsigma} \times A^{\varsigma} \to A$ | the module of $A(x,y,z)$, the third slot conjugated |
| $A \times A^{\varsigma} \times A \to A$ | the module of $B(x,y,z)$, the third slot plain |
| $\{x,y,z\}$ | the ternary product $(x \star y) \star z^{*} = xy^{*}z$ |
| $\{x,y,z\}^{*} = \{z^{*},y^{*},x^{*}\}$ | the Hermitian symmetry of the ternary product |
| $\{x,y,1\} = x \star y$ | the binary product as the ternary product with the unit in the third slot |
| $xy = x \star y^{*}$ | the original product recovered from the derived operation |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan algebras and the associative ones they are built from, the setting in which the symmetrised product and its identity are read.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the Jordan triple systems and the ternary product as the primary object, of which the binary product is a derived notion.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the ternary product of a $J^{*}$-algebra, its quadratic representation and the Jordan triple identity, taken here algebraically.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the algebra-free theory of the $J^{*}$-triple and the ternary product as the carrier of the identities, which is the layer of this category.
