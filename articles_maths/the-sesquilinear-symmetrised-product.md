# __The Sesquilinear Symmetrised Product__

## Introduction

A sesquilinear product carries a second product, its transpose $y \star x$, and the two together carry a third, their symmetrisation. The **symmetrised sesquilinear product** is the operation

$$
x \circ y = \tfrac12\bigl(x \star y + y \star x\bigr),
$$

the companion of the symmetrised product of an algebra and the operation under which the Hermitian elements of a sesquialgebra close: the symmetrised product of a sesquialgebra is *The Sesquilinear Symmetrised Product*, and the bracket formed by the difference is *The Sesquilinear Commutator*.

The interest of the operation is that it is almost, and not quite, a Jordan product, and the whole of this article is the location of the difference. Three facts are proved. The symmetrisation is an $R^{\varsigma}$-bilinear operation and not an $R$-bilinear one, the two scalar parities of the two slots collapsing to the fixed ring. In the derived case $x \star y = xy^{*}$ it lands in the Hermitian part for arbitrary arguments, not only for Hermitian ones, which is sharper than the corresponding statement for the plain symmetrisation. And the Jordan identity, which holds on the Hermitian part through the associativity of the underlying product, fails off that part, where the symmetrised sesquilinear product is no longer the symmetrisation of the underlying product; a two-line witness in $M_2(\mathbb{C})$ is given.

The setting and the notation are those of *Sesquialgebras* and *The Sesquilinear Product*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ is an $R$-module with a $\varsigma$-sesquilinear product $\star$, and in the derived case $A$ is an associative $R$-algebra with a $\varsigma$-semilinear involution $*$ and $x \star y = xy^{*}$. The involution on $A$, the two halves $H(A)$ and $S(A)$ and the closure of $H(A)$ under the symmetrised product are *Hermitian and Skew-Hermitian Elements*; the Jordan algebra that $H(A)$ carries is *The Hermitian Jordan Algebra*; the triple product of the failure of associativity is *The Sesquilinear Associator and the Ternary Product* and *Algebraic J\*-Algebras*; and the general theory of the symmetrisation of an associative product is *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*. Throughout, $2$ is invertible in $R$, so that the halving inside $\circ$ is available.

---

## The Definition

### The Symmetrised Product

**Definition.** The **symmetrised sesquilinear product** of the product $\star$ is

$$
x \circ y := \tfrac12\bigl(x \star y + y \star x\bigr).
$$

It is additive in each variable, because $\star$ is, and it is symmetric,

$$
x \circ y = y \circ x ,
$$

by the symmetry of the sum. On the diagonal it is the square of the product, $x \circ x = x \star x$; in the derived case that square is the Hermitian square,

$$
x \circ x = x \star x = xx^{*},
$$

the element of *Hermitian Squares and the Algebraic Positive Cone*.

**Remark.** The two products $\star$ and $\circ$ are linked by the decomposition

$$
x \star y = x \circ y + \tfrac12\bigl(x \star y - y \star x\bigr),
$$

whose second summand is the difference bracket $[x,y]_{\varsigma}$ of *The Sesquilinear Product*, §*The Transposed Product*; the difference is antisymmetric and takes skew-Hermitian values, and it is read in *The Sesquilinear Commutator*. The symmetrisation is therefore the symmetric half of the pair, exactly as the Jordan product is the symmetric half of an associative product in *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*.

### The Scalar Rules

**Theorem (the symmetrisation is $R^{\varsigma}$-bilinear).** For all $\lambda \in R$ and all $x, y$,

$$
(\lambda x) \circ y = \tfrac12 \lambda\,(x \star y) + \tfrac12 \varsigma(\lambda)\,(y \star x) , \qquad x \circ (\lambda y) = \tfrac12 \varsigma(\lambda)\,(x \star y) + \tfrac12 \lambda\,(y \star x) .
$$

Consequently $\circ$ is linear in each variable over the fixed ring $R^{\varsigma} = \{\lambda : \varsigma(\lambda) = \lambda\}$, and it is linear in a variable over all of $R$ exactly in the degenerate case $(\varsigma(\lambda) - \lambda)A = 0$ for every $\lambda$, the case in which the product of $A$ is bilinear.

**Proof.** In the first slot, $(\lambda x) \star y = \lambda (x \star y)$ by the first scalar rule of *Sesquialgebras* and $y \star (\lambda x) = \varsigma(\lambda)(y \star x)$ by the second, the scalar sitting in the second slot of the transposed product; the two terms give the first display, and the second is the same computation with the slots exchanged. For $\lambda \in R^{\varsigma}$ the two displayed right-hand sides both equal $\lambda (x \circ y)$, so $\circ$ is $R^{\varsigma}$-linear in each variable. Conversely, if $(\lambda x) \circ y = \lambda (x \circ y)$ for all $x, y$ then $\bigl(\varsigma(\lambda) - \lambda\bigr)(y \star x) = 0$ for all $x, y$, which is the degeneracy condition, and the same condition arises from the second variable. $\square$

**Remark.** The symmetrisation does not average the two parities, it destroys them: each slot of $\circ$ receives one linear and one conjugate-linear contribution, so the surviving scalars are exactly the fixed ones. This is the same ring that the two halves of the algebra are modules over, and the reason is the same, that $\varsigma(\lambda) = \lambda$ is what makes a conjugate-linear slot agree with a linear one. For $\varsigma = \mathrm{id}$ the fixed ring is $R$ and the statement is the familiar bilinearity, which is the case of *The Self-Adjoint Part of an Algebra*.

### The Polarisation of the Square

**Proposition.** The symmetrised product is the polarisation of the square:

$$
x \circ y = \tfrac12\Bigl((x + y) \star (x + y) - x \star x - y \star y\Bigr).
$$

**Proof.** The product is additive in each variable, so $(x+y)\star(x+y) = x\star x + x\star y + y\star x + y\star y$; halving the difference gives the symmetrisation. $\square$

**Remark.** The square $x \mapsto x \star x$ determines the product on the diagonal and, by the proposition, the whole symmetrised product off the diagonal: two products with the same squares of all linear combinations have the same symmetrisation. The difference bracket is what the squares do not see, since it takes opposite values on $y \star x$ and $x \star y$ and cancels in every square.

---

## The Derived Operation

### The Hermitian Value

**Theorem.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$ and let $\star$ be the derived operation $x \star y = xy^{*}$. Then for all $x, y \in A$ the symmetrised product is Hermitian,

$$
(x \circ y)^{*} = x \circ y ,
$$

so that $\circ$ is an operation $A \times A \to H(A)$.

**Proof.** Conjugation reverses the derived product, $(x \star y)^{*} = y \star x$, by *The Sesquilinear Product*, §*The Conjugate of a Product*; hence $(x \circ y)^{*} = \tfrac12\bigl((x \star y)^{*} + (y \star x)^{*}\bigr) = \tfrac12\bigl(y \star x + x \star y\bigr) = x \circ y$. $\square$

**Remark.** The image of the symmetrised sesquilinear product is contained in the Hermitian elements, whatever the two arguments are: the symmetrisation is a map from the whole square $A \times A$ into one half of the algebra. The plain symmetrisation $x \bullet y = \tfrac12(xy + yx)$ has no such property, its value being Hermitian only when the two arguments lie in the right halves; this is the sharpest sense in which the sesquilinear product enters the Hermitian part more easily than the algebra product does.

### The Hermitian Part

**Theorem (the symmetrisation on the Hermitian part).** For $x, y \in H(A)$ the symmetrised sesquilinear product and the plain symmetrisation agree,

$$
x \circ y = \tfrac12\bigl(xy + yx\bigr) = x \bullet y ,
$$

and $H(A)$ is closed under both.

**Proof.** For a Hermitian $y$ the derived operation is the algebra product, $x \star y = xy^{*} = xy$, and for a Hermitian $x$ the transposed product is $y \star x = yx$. Adding and halving gives the identity; the closure of $H(A)$ under $\bullet$ is *Hermitian and Skew-Hermitian Elements*, §*The Hermitian Part is a Jordan Algebra*. $\square$

**Remark.** On the Hermitian part the two symmetrisations coincide, and off it they differ: the operation $\circ$ is the symmetrisation of the derived product, $\bullet$ the symmetrisation of the algebra product, and the two products agree only on the Hermitian slot. The next section measures the distance.

---

## The Jordan Identity

### On the Hermitian Part

**Theorem.** The symmetrised sesquilinear product restricted to $H(A)$ satisfies the Jordan identity,

$$
(x \circ y) \circ (x \circ x) = x \circ \bigl(y \circ (x \circ x)\bigr) \qquad \text{for all } x, y \in H(A) ,
$$

and with this product $H(A)$ is a commutative Jordan algebra over $R^{\varsigma}$.

**Proof.** On the Hermitian part $\circ$ is the plain symmetrisation $\bullet$, by the theorem above, and $\bullet$ is the symmetrisation $x \bullet y = \tfrac12(xy+yx)$ of the associative product of $A$; the symmetrisation of an associative product satisfies the Jordan identity, by *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*. Commutativity is built into the definition and $R^{\varsigma}$-bilinearity is the scalar theorem above. $\square$

The Jordan algebra is read in *The Hermitian Jordan Algebra*, where its idempotents, its Peirce decomposition and its degree are developed.

### Off the Hermitian Part

**Proposition (the Jordan identity fails off the Hermitian part).** In the $R$-algebra $M_{2}(\mathbb{C})$ with the conjugate transpose there are $x, y$ with

$$
(x \circ y) \circ (x \circ x) \neq x \circ \bigl(y \circ (x \circ x)\bigr).
$$

Take $x = E_{12}$ and $y = E_{22}$, writing $E_{ij}$ for the matrix units. Then

$$
x \circ x = E_{12}E_{21} = E_{11} , \qquad x \circ y = \tfrac12\bigl(E_{12}E_{22} + E_{22}E_{21}\bigr) = \tfrac12\bigl(E_{12} + E_{21}\bigr) , \qquad y \circ (x \circ x) = E_{22} \circ E_{11} = 0 ,
$$

so the two sides of the Jordan identity are

$$
(x \circ y) \circ (x \circ x) = \tfrac14\bigl(E_{12} + E_{21}\bigr) , \qquad x \circ \bigl(y \circ (x \circ x)\bigr) = x \circ 0 = 0 ,
$$

and the first is not zero.

**Proof.** The computations are the displays: $E_{12}E_{21} = E_{11}$ and $E_{12}E_{22} = E_{12}$, $E_{22}E_{21} = E_{21}$ by the multiplication of the matrix units, and $E_{22}E_{11} = E_{11}E_{22} = 0$; the symmetrisation of $E_{12}$ with $E_{11}$ is $\tfrac12(E_{12}E_{11} + E_{11}E_{21}) = \tfrac12 E_{21}$, whence $(\tfrac12(E_{12}+E_{21})) \circ E_{11} = \tfrac14(E_{12}+E_{21})$. $\square$

**Remark.** One of the two elements is Hermitian, $y = E_{22}$, and the other is not, $x = E_{12}$; a single element outside $H(A)$ is enough to break the identity. The perturbation is exactly the failure of $x$ to be Hermitian: the value $x \circ x = E_{11} = xx^{*}$ is Hermitian, as the theorem on the Hermitian value promises, but the symmetry of the derived product with one slot off $H(A)$ is the wrong one to carry the identity.

### The Obstruction

**Remark (why the Hermitian part is the right domain).** The Jordan identity for a symmetrisation holds when the two products that are being symmetrised agree, and the failure above is the failure of that agreement. On $H(A)$ the derived product coincides with the algebra product, $x \star y = xy$, and the associativity of the algebra product is inherited by the symmetrisation; off $H(A)$ the derived product is a different product, and the identity has no reason to hold, as the witness shows.

**Remark (the associator).** For a general $\varsigma$-sesquilinear product, with no involution on $A$ and no associativity, the obstruction is the non-associativity of the symmetrised pair: the criterion that makes the identity automatic is the associativity of the product being symmetrised, and the derived product $x \star y = xy^{*}$ is not associative, its associator $[x,y,z] = (x \star y) \star z - x \star (y \star z)$ being the object of *The Sesquilinear Associator and the Ternary Product*. The reason the Hermitian part survives is precisely that there the derived product is the associative one, so that the identity holds for the reason it holds for an associative algebra and not for a sesquilinear one.

---

## Worked Cases

### The Complex Matrices

For $A = M_{n}(\mathbb{C})$ with the conjugate transpose $\dagger$, the derived operation is $x \star y = xy^{\dagger}$ and the symmetrised product is

$$
x \circ y = \tfrac12\bigl(xy^{\dagger} + yx^{\dagger}\bigr),
$$

an operation from all pairs of matrices into the Hermitian matrices. The Hermitian part is the real vector space of the Hermitian matrices, the fixed ring is $R^{\varsigma} = \mathbb{R}$, and on that space, by the theorem above, the symmetrised product is the ordinary symmetrisation $\tfrac12(xy+yx)$. Off it the identity fails, with the witness of the previous section.

### The Field

For $A = \mathbb{C}$ over the datum $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation and the product $x \star y = x\bar y$, the symmetrisation is

$$
x \circ y = \tfrac12\bigl(x\bar y + y\bar x\bigr) = \mathrm{Re}\bigl(x\bar y\bigr),
$$

a real number, and every element is Hermitian exactly when it is real. Here the image is all of the Hermitian part $H(A) = \mathbb{R}$, and on that copy of $\mathbb{R}$ the symmetrised product is the ordinary multiplication; the value is the real part of the product $x\bar y$ of *The Centre and the Zero Divisors of a Sesquialgebra*, §*The Sesquilinear Field*.

### The Quaternions

For $A = \mathbb{H}$ with the quaternion conjugation over the datum $(\mathbb{R},\mathrm{id})$ the twist is invisible, so the product is the ordinary one, the symmetrised sesquilinear product is the plain symmetrisation $\tfrac12(xy+yx)$, and the Hermitian elements are the real quaternions. The case is the bilinear one, of *The Self-Adjoint Part of an Algebra*; it is recorded here for completeness, and it is the degenerate case of the scalar theorem, in which the fixed ring is all of $R$.

### The Biquaternion Case

For $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the star-involution the symmetrised star-product is the Jordan product of the biquaternion block, and the Hermitian part it fills is a Jordan algebra of degree two, read in *Biquaternion Jordan Algebras* and *The Six Subspaces and the Four Complex Products*. The biquaternion layer is the worked case in which all of the operations of this article, the product, the derived product, the symmetrisation and the difference bracket, are computed on a basis of eight elements.

## Summary

The symmetrised sesquilinear product $x \circ y = \tfrac12(x\star y + y\star x)$ is commutative, additive in each variable and equal to the square on the diagonal, $x \circ x = x\star x$, and it is the symmetric half of the product, the antisymmetric half being the difference bracket $[x,y]_{\varsigma}$. It is $R^{\varsigma}$-bilinear and no more: each slot receives one linear and one conjugate-linear contribution, so the two parities collapse to the fixed ring, and $R$-bilinearity returns exactly in the degenerate case in which the product is bilinear. It is the polarisation of the square, so the squares determine it.

In the derived case $x \star y = xy^{*}$ of an associative algebra with a $\varsigma$-semilinear involution, the symmetrised product is Hermitian-valued on all pairs, $x \circ y \in H(A)$, sharper than the plain symmetrisation, which is Hermitian only on the Hermitian part. On $H(A)$ the two symmetrisations coincide, $x \circ y = \tfrac12(xy + yx)$, and there the Jordan identity holds and $H(A)$ is a commutative Jordan algebra over $R^{\varsigma}$, by the associativity of the underlying product. Off $H(A)$ the identity fails, and the kernel of the failure is the disagreement between the derived product and the algebra product: the symmetrisation of the derived operation is a Jordan product exactly on the Hermitian part.

## Summary of Notation

| symbol | meaning |
|---|---|
| $x \circ y = \tfrac12(x \star y + y \star x)$ | the symmetrised sesquilinear product, the subject of the article |
| $x \circ x = x \star x = xx^{*}$ | its diagonal, the Hermitian square |
| $x \circ y = \tfrac12((x+y)\star(x+y) - x\star x - y\star y)$ | the polarisation of the square |
| $x \star y = x \circ y + \tfrac12\bigl(x \star y - y \star x\bigr)$ | the product split into its symmetric and antisymmetric halves |
| $[x,y]_{\varsigma} = x \star y - y \star x$ | the difference bracket, the antisymmetric half |
| $R^{\varsigma}$ | the fixed ring, the scalars over which the symmetrisation is bilinear |
| $x \bullet y = \tfrac12(xy + yx)$ | the plain symmetrisation, equal to $\circ$ on $H(A)$ |
| $H(A)$ | the Hermitian elements, the image of $\circ$ in the derived case |
| $x = E_{12},\ y = E_{22}$ | the witness pair in $M_2(\mathbb{C})$ for the failure of the Jordan identity off $H(A)$ |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetrised product of an involutive ring and the two halves of the involution.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the symmetrisation of an associative algebra and the Jordan identity it satisfies.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebras, the symmetrisation and the envelope.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of an algebra and the twisted products they carry.
- The companion articles of this series: *Sesquialgebras*, *The Sesquilinear Product*, *Hermitian and Skew-Hermitian Elements*, *The Hermitian Jordan Algebra*, *The Sesquilinear Commutator*, *The Sesquilinear Associator and the Ternary Product*, and *Algebraic J\*-Algebras*.
