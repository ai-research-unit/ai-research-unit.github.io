# __Examples of Sesqualgebras__

## Introduction

The preceding articles developed the general theory of the sesqualgebras: the two scalar rules and the conjugate module, the associator and the ternary product, the Hermitian and skew-Hermitian elements, the ideals and the quotients, the units, the centre and the zero divisors, the simplicity, the tensor and direct products, the real forms and the involutions. This article collects the standard examples and records, for each, the data the theory associates with it: the **datum** $(R,\varsigma)$, the involution, the product, whether the product is associative, commutative or unital, and whether the object is of **full type** — faithful over $R$, with products generating $A$ and no nonzero element annihilating $A$ on the left. It is a reference article: each example is treated in its own article, and the purpose here is to make the data comparable at a glance and to separate the examples that are genuinely sesquilinear from those that are the bilinear case in disguise.

The distinction the whole tabulation is built on is the collapse of *Sesqualgebras*, §*The Collapse at the Identity*: a sesqualgebra with $\varsigma = \mathrm{id}$ **is** an ordinary algebra, and every ordinary algebra is a sesqualgebra for the trivial involution. An example is therefore genuinely sesquilinear exactly when its datum has $\varsigma \neq \mathrm{id}$, and an example read over the trivial involution is a bilinear example, however sesquilinear the product looks in coordinates. The same algebra appears twice in the list when it carries both readings, and the two entries are different objects of the category, because the involution is part of the datum. The collapse also supplies the sharp test of the list: by the theorem of that section an object of full type with $\varsigma \neq \mathrm{id}$ is **neither associative nor commutative**, so every associative entry of the table below is either a collapsed one or fails full type.

Throughout, $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and an involution of an algebra is written ${}^{*}$; the product of a sesqualgebra is the **derived operation** $x\star y = xy^{*}$ of an associative algebra with an involution wherever the example is of that standard form, and the product by juxtaposition is the algebra product. The number systems are those of the shared conventions: $\mathbb{C}$ over $\mathbb{R}$ with the conjugation, the split complex numbers $\mathbb{D}$ with unit $j$, $j^2 = +1$, the dual numbers $\mathbb{D}'$ with unit $\varepsilon$, $\varepsilon^2 = 0$, the quaternions $\mathbb{H}$ with conjugation ${}^{\natural}$, and the biquaternions $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the star ${}^{*} = \bar{\cdot}\circ{}^{\natural}$. The definition and the collapse are *Sesqualgebras*; the derived operation and its parities are *The Sesquilinear Product*; the involutions of the object are *The Involutions of a Sesqualgebra*; the matrix example is *Matrix Sesqualgebras*; the biquaternion example is *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*; the endomorphism example is *The Sesquilinear Structure of the Endomorphism Algebra*; and the products are *Tensor Products of Sesqualgebras* and *Direct Products of Sesqualgebras*. The field, the complex numbers, the matrices and the biquaternion algebra are the four examples of *Sesqualgebras*, §*Examples*, read here with the data of the table; the split complex numbers, the dual numbers and the quaternions are *Examples of Algebras*, §*The Split Complex Numbers*, §*The Dual Numbers* and §*The Quaternions*. The article stays inside the algebra: no distance and no continuity occurs.

## The Data Table

The table is the summary; each row is justified in the sections below.

| Example | datum $(R,\varsigma)$ | involution / twist | product $\star$ | associative | commutative | unit | full type |
|---|---|---|---|---|---|---|---|
| a field $K$ | $(K,\varsigma)$ | second slot $\varsigma$ | $x\,\varsigma(y)$ | iff $\varsigma = \mathrm{id}$ | iff $\varsigma = \mathrm{id}$ | right | yes |
| $\mathbb{C}$ | $(\mathbb{C},\text{conj})$ | second slot conjugation | $x\bar y$ | no | no | right | yes |
| $\mathbb{C}$ | $(\mathbb{R},\mathrm{id})$ | second slot conjugation | $x\bar y$ | no | no | right | yes |
| $\mathbb{D}$, $\mathbb{D}'$ | $(\mathbb{R},\mathrm{id})$ | second slot ${}^{*}$ | $xy^{*}$ | iff $* = \mathrm{id}$ | iff $* = \mathrm{id}$ | right | yes |
| $\mathbb{H}$ | $(\mathbb{R},\mathrm{id})$ | second slot ${}^{\natural}$ | $x\,{}^{\natural}y$ | no | no | right | yes |
| $M_n(\mathbb{C})$, $n \geq 2$ | $(\mathbb{C},\text{conj})$ | second slot ${}^{*} = \overline{X}^{T}$ | $ST^{*}$ | no | no | right | yes |
| $\operatorname{End}_R(M)$, $M$ free of rank at least two | $(R,\varsigma)$ | second slot ${}^{\dagger}$ | $ST^{\dagger}$ | iff ${}^{\dagger} = \mathrm{id}$ | no | right | yes |
| $\mathbb{B}$ | $(\mathbb{C},\text{conj})$ | second slot $*$ | $PQ^{*}$ | no | no | right | yes |
| $\mathbb{B}$ | $(\mathbb{C},\mathrm{id})$ | trivial | $PQ$ | yes | no | two-sided | yes |
| $\mathbb{B}$ | $(\mathbb{C},\mathrm{id})$ | first slot ${}^{\natural}$ | ${}^{\natural}PQ$ | no | no | left | yes |
| $\mathbb{B}$ | $(\mathbb{C},\text{conj})$ | first slot ${}^{\natural}$, second slot $*$ | ${}^{\natural}PQ^{*}$ | no | no | none | yes |
| $R[G]$ | $(R,\varsigma)$ | second slot $g \mapsto g^{-1}$ | $xy^{*}$ | only $\varsigma = \mathrm{id}$, $G$ of exponent two | same | right | yes |
| any nonzero $R$-module | any $(R,\varsigma)$ | any | $0$ | yes | yes | none | no |

In the column **involution / twist** the involution named is the one carried by the second slot in the derived form $x\star y = xy^{*}$, and "first slot ${}^{\natural}$" records that the product is not of the derived form but twists its first slot by the $\mathbb{C}$-linear ${}^{\natural}$, as the biquaternion entries below explain. In the column **unit**, the entry is the behaviour of the unit when the involution displayed is not the identity: "right" means that the unit is a right unit and not a left one, "left" that it is a left unit and not a right one, "none" that there is no unit of either kind, and "two-sided" that it is a unit on both sides. The trivial involution gives the two-sided unit, and the only row whose displayed twist is trivial is the algebra product $PQ$ of $\mathbb{B}$.

## The Field with Its Involution

**Example.** Let $K$ be a field with an involution $\varsigma$ and let $A = K$ with the product $x\star y = x\,\varsigma(y)$, the smallest of the four examples of *Sesqualgebras*, §*Examples*. The product is $K$-linear in the first slot and $\varsigma$-semilinear in the second, so $K$ is a sesqualgebra over $(K,\varsigma)$, and its associator is

$$
(x\star y)\star z - x\star(y\star z) = x\bigl(\varsigma(zy) - z\,\varsigma(y)\bigr) = x\,\varsigma(y)\bigl(\varsigma(z) - z\bigr) .
$$

The associator vanishes for all $x, y, z$ exactly when $\varsigma = \mathrm{id}$ (take $y = 1$), and the same test with the commutator shows that the product is commutative on the same condition. The element $1$ is a right unit, $z\star1 = z$, and it is not a left unit when $\varsigma \neq \mathrm{id}$, since $1\star z = \varsigma(z)$. This is the smallest genuinely sesquilinear example, and it is the one the collapse theorem is read on: the field is faithful over itself with generating products, so it is of full type, and it is neither associative nor commutative as soon as the involution is nontrivial.

**Example (the complex numbers).** With $K = \mathbb{C}$ and $\varsigma$ the conjugation the product is $x\star y = x\bar y$, the standard sesquilinear product on the plane, not associative and not commutative, with $1$ a right unit and no two-sided one. This is the case $n = 1$ of the matrix example below, and the simplest instance of the collapse: read over $(\mathbb{C},\varsigma)$ it is genuinely sesquilinear, while read over $(\mathbb{R},\mathrm{id})$ the same product is $\mathbb{R}$-bilinear and the object is an ordinary, non-associative real algebra of rank two. The two readings are *Real Forms of a Sesqualgebra*.

## The Real Algebras and the Collapse

### The Split Complex and the Dual Numbers

**Example.** Let $A$ be $\mathbb{D}$, $\mathbb{D}'$ or any real algebra, with an $\mathbb{R}$-linear involution ${}^{*}$ and the derived product $x\star y = xy^{*}$. The datum is $(\mathbb{R},\mathrm{id})$, the second scalar rule is the first, the product is $\mathbb{R}$-bilinear, and the object is an ordinary real algebra: this is the collapse of the category, and every statement about it is a statement about algebras. The derived operation is associative exactly when $xy^{*}$ is the algebra product, that is exactly when ${}^{*} = \mathrm{id}$ for a unital algebra, by the associator proposition of *Sesqualgebras*; for the involution $j\mapsto -j$ of $\mathbb{D}$ it is not, and the failure is the same one as over the complex numbers. The products of the split complex numbers are the prototypes of the rank-two entries, and the idempotents $e_{\pm} = \tfrac12(1\pm j)$ are exchanged by the involution $j\mapsto -j$, $e_{\pm}^{*} = e_{\mp}$, so the Hermitian elements of $\mathbb{D}$ for that involution are the line $\mathbb{R}\cdot1$. The underlying algebras are *Examples of Algebras*, §*The Split Complex Numbers* and §*The Dual Numbers*.

### The Quaternions

**Example.** Let $A = \mathbb{H}$ with the quaternion conjugation ${}^{\natural}$ over $(\mathbb{R},\mathrm{id})$ and the derived product $x\star y = x\,{}^{\natural}y$. The involution is $\mathbb{R}$-linear and anti-multiplicative, the product is $\mathbb{R}$-bilinear, and the object is the collapsed one: an ordinary, non-associative real algebra. It is not associative, on the witness $(1\star1)\star e_1 = -e_1 \neq e_1 = 1\star(1\star e_1)$, and it is not commutative, since $1\star e_1 = -e_1$ while $e_1\star1 = e_1$; both failures are read on the unit $1$ against the nontrivial involution, which is the criterion of the associator proposition of *Sesqualgebras* read on this algebra. The Hermitian elements are the real line, $H(\mathbb{H}) = \mathbb{R}\cdot1$, and $\mathbb{H}$ is a division algebra for its own product, so this is also the division example of the list: an object of full type whose underlying algebra is a division algebra, in contrast with the matrix example below, whose underlying algebra has zero divisors. The underlying algebra is *Examples of Algebras*, §*The Quaternions*.

## The Matrix Algebra

### The Complex Matrices

**Example.** Let $A = M_n(\mathbb{C})$ with the conjugate transpose $X^{*} = \overline{X}^{T}$, over $(\mathbb{C},\varsigma)$ with the conjugation, and the derived product $S\star T = ST^{*}$. The product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second; it is not associative, on the witness

$$
\bigl(E_{22}\star E_{12}\bigr)\star E_{11} = E_{21} \neq 0 = E_{22}\star\bigl(E_{12}\star E_{11}\bigr) ,
$$

and it is not commutative, on the witness $E_{12}\star I = E_{12}$ against $I\star E_{12} = E_{21}$. The unit $I$ is a right unit and not a left one, $I\star S = S^{*}$. The object is of full type — it is unital and faithful — and it is neither associative nor commutative in agreement with the collapse theorem, $\varsigma$ being nontrivial. The Hermitian elements are the Hermitian matrices and the unitary elements the unitary group $U(n)$; the ideal theory of the example is the case $n \geq 2$ in which the object is simple and has zero divisors at the same time, both notions being those of *Simple Sesqualgebras and Minimal Ideals* and *The Centre and the Zero Divisors of a Sesqualgebra*, and the tabulation of the elements is *Matrix Sesqualgebras*.

### The Endomorphism Algebra

**Example.** Let $M$ be an $R$-module with an involution of its endomorphism ring, so that $S^{\dagger}$ is defined, and let $A = \operatorname{End}_R(M)$ with the product $S\star T = S T^{\dagger}$. This is the general form of which the matrices are the case $M = \mathbb{C}^n$, and it is the example the operator theory of the category is computed on; the structure, the involutions it admits and the worked cases $M_n(\mathbb{C})$, $M_n(\mathbb{H})$ and the biquaternion algebra are *The Sesquilinear Structure of the Endomorphism Algebra*, and the product is read here only to place it in the table.

## The Biquaternion Algebra

### The Star and the Derived Operation

**Example.** Let $A = \mathbb{B}$ over $(\mathbb{C},\varsigma)$ with the star ${}^{*} = \bar{\cdot}\circ{}^{\natural}$, the conjugate-linear involution that conjugates the coefficients and negates the quaternion units, and the derived product $P\star Q = PQ^{*}$. The product is conjugate-linear in the second slot, not associative and not commutative, with $e_0$ a right unit and no two-sided one, and the object is of full type. It is the corpus's own algebra, and through the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ of *Matrix Sesqualgebras* it is the case $n = 2$ of the matrix example, the star being the conjugate transpose: so it is simple, it has zero divisors, and its Hermitian elements are the matrices that the model sends to the Hermitian ones.

### The Linear Conjugation and the Bilinear Twist

**Example.** Let $A = \mathbb{B}$ over $(\mathbb{C},\mathrm{id})$ with the quaternion conjugation ${}^{\natural}$ carried by the **first** slot, and the product ${}^{\natural}PQ$. This is the caution of *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$* read as an entry of the table: ${}^{\natural}$ is $\mathbb{C}$-**linear**, since it fixes the complex scalars, so a slot read through it is still $\mathbb{C}$-linear, the product is $\mathbb{C}$-bilinear, and the datum is $(\mathbb{C},\mathrm{id})$. The product is not associative, and it has a left unit and no right one: the product with $P = e_0$ is $Q$, while the product with $Q = e_0$ is ${}^{\natural}P$, so $e_0$ acts on the left and not on the right. The entry is in the list because it fixes the shape of the definition: the conjugation that makes a product sesquilinear is the conjugate-linear ${}^{*}$, a product whose **second** slot carried ${}^{\natural}$ in its place would be bilinear, and a product whose second slot carries ${}^{*}$ is sesquilinear whatever its first slot carries.

### The Four Products

**Example.** The four products of *The Four Biquaternion Complex Products* are read in the table as four entries on one algebra: the algebra product $PQ$, the linear twist ${}^{\natural}PQ$, the derived operation $PQ^{*}$, and the mixed product ${}^{\natural}PQ^{*}$. The first two are $\mathbb{C}$-bilinear and belong to $(\mathbb{C},\mathrm{id})$, the second two are conjugate-linear in the second slot and belong to $(\mathbb{C},\varsigma)$. Each of the four makes $\mathbb{B}$ a sesqualgebra for its own datum — associativity is not one of the axioms, and the two scalar rules alone do not separate the four — and exactly one of them, $PQ^{*}$, is the derived operation of the algebra with a conjugate-linear involution; the two conditions that single it out are those of *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*. This is the sharpest warning of the list against identifying an object with its product: the algebra is one, the products are four, and the datum and the derived form are the data that tell them apart.

## The Group Algebra

### The Involution $g \mapsto g^{-1}$

**Example.** Let $A = R[G]$ be the group algebra of a group $G$ over $R$, with the involution

$$
\Bigl(\sum_g a_g\,g\Bigr)^{*} = \sum_g \varsigma(a_g)\,g^{-1} ,
$$

which is $\varsigma$-semilinear, of order two, and anti-multiplicative because $(gh)^{-1} = h^{-1}g^{-1}$. With the derived product $x\star y = xy^{*}$ the group algebra is a sesqualgebra over $(R,\varsigma)$, unital with unit the identity of $G$ and faithful over $R$, hence of full type. The associator is $x((zy)^{*} - z\,y^{*})$ by *Sesqualgebras*, so the product is associative exactly when $(zy)^{*} = z\,y^{*}$ for all $z, y$.

### Why the Group Elements Do Not Decide

**Proposition.** On the basis elements the identity $(zy)^{*} = z\,y^{*}$ reads $h^{-1}g^{-1} = gh^{-1}$ for all $g, h$, which holds exactly when $g^{-1} = g$ for every $g$ — a group of exponent two is automatically abelian, so this is exactly the elementary abelian two-group case; but the identity must hold on all of $R[G]$, and with $z = \lambda g$ and $y = h$ it reads

$$
\varsigma(\lambda)\,h^{-1}g^{-1} = \lambda\, gh^{-1} \qquad \text{for all } \lambda\in R , \quad g, h\in G .
$$

*Proof.* The two sides are the two coefficientwise products of the basis computation. For the second display, $zy = \lambda\mu gh$ when $y = \mu h$, so $(zy)^{*} = \varsigma(\lambda\mu)(gh)^{-1} = \varsigma(\lambda)\varsigma(\mu)h^{-1}g^{-1}$, while $z\,y^{*} = (\lambda g)(\varsigma(\mu)h^{-1}) = \lambda\varsigma(\mu)gh^{-1}$; putting $\mu = 1$ gives the display. $\square$

**Corollary.** If $\varsigma \neq \mathrm{id}$ the product $x\star y = xy^{*}$ of the group algebra is **never** associative, because the display with $g = h = 1$ reads $\varsigma(\lambda) = \lambda$, which must hold for every $\lambda$. If $\varsigma = \mathrm{id}$ the involution is $g\mapsto g^{-1}$ and the product is the ordinary group-algebra product exactly when $g = g^{-1}$ for every $g$, that is when $G$ is an elementary abelian two-group, and otherwise it is a non-associative $R$-algebra. Testing the identity on the group elements alone would find the exponent-two condition and miss the scalar obstruction altogether, which is the reason the corollary is stated on the whole algebra.

## The Degenerate Examples

### The Zero Product

**Example.** On a nonzero $R$-module $A$ with the product $xy = 0$, every pair $(R,\varsigma)$ and every involution is a datum: both scalar rules hold, the product is associative and commutative, and the object is not of full type because its products do not generate it. It is the example that shows the hypotheses of the collapse theorem to be necessary — the theorem concludes $\varsigma = \mathrm{id}$ from associativity only through generation and faithfulness — and it is the boundary of the category in the other direction as well: it is a sesqualgebra whose involution may be nontrivial while the product is as degenerate as a product can be. On a ring with a nontrivial product the same construction shows that a datum can be changed on the annihilator, by the second clause of the theorem of *Sesqualgebras*, §*The Collapse at the Identity*.

### The Direct Products

**Example.** If $A$ and $B$ are sesqualgebras over the same datum, the module $A\times B$ with the componentwise product and the componentwise involution, $(a,b)^{*} = (a^{*}, b^{*})$, is a sesqualgebra over that datum; it is associative, commutative or unital exactly when both factors are, and its Hermitian, skew-Hermitian and unitary elements are the pairs of such elements. The construction, its idempotents and its decomposition by a central idempotent are *Direct Products of Sesqualgebras*, and it is recorded here because it is the operation that produces new examples from the ones of the list: the product of two collapsed examples is collapsed, and the product of a genuinely sesquilinear example with another is genuinely sesquilinear.

## Genuinely Sesquilinear and Collapsed

### The Criterion

**Proposition.** Let $A$ be a sesqualgebra over $(R,\varsigma)$ that is faithful over $R$ and whose products generate $A$. If $A$ is also a sesqualgebra over $(R,\varsigma')$ with the same product, then $\varsigma = \varsigma'$; in particular a product that is $\varsigma$-sesquilinear in the second slot and $\varsigma'$-sesquilinear in the same slot with $\varsigma\neq\varsigma'$ is possible only through the annihilation of the difference, and the datum of an example of full type is determined by its product.

*Proof.* The two scalar rules of *Sesqualgebras*, §*The Two Scalar Rules*, read with the two data give $(\varsigma(\lambda) - \varsigma'(\lambda))xy = 0$ for all $\lambda, x, y$: the first rule is the same for both data, and the second reads the same left-hand side $x(\lambda y)$ as $\varsigma(\lambda)(xy)$ and as $\varsigma'(\lambda)(xy)$. The products generate $A$, so $(\varsigma(\lambda) - \varsigma'(\lambda))A = 0$, and faithfulness over $R$ makes the scalar zero, which is the collapse criterion of §*The Collapse at the Identity*. $\square$

### The Two Lists

**The genuinely sesquilinear examples**, with $\varsigma \neq \mathrm{id}$, are the field $K$ with $x\,\varsigma(y)$; the complex numbers over $(\mathbb{C},\text{conj})$; the complex matrices with the conjugate transpose; the endomorphism algebra with the adjoint of its involution; the biquaternion algebra with the star and with the mixed product $P\,{}^{\natural}Q^{*}$; and the group algebra with $g\mapsto g^{-1}$ over a base with a nontrivial involution. By the collapse theorem each of them of full type is neither associative nor commutative, which is the test that no entry of this list is an ordinary algebra in disguise.

**The collapsed examples**, with $\varsigma = \mathrm{id}$, are the real algebras $\mathbb{R}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{H}$ with the derived operation of an $\mathbb{R}$-linear involution; the complex numbers read over $(\mathbb{R},\mathrm{id})$; the biquaternion algebra with the products $PQ$ and $P\,{}^{\natural}Q$; the group algebra over the trivial involution, which is the ordinary group algebra when $G$ is an elementary abelian two-group; and the zero product over any datum. Each of them is an ordinary algebra and belongs to the list only to mark the boundary: the sesquilinear kind contains the bilinear kind as the case $\varsigma = \mathrm{id}$, and an example is genuinely of the new kind exactly when its datum is nontrivial.

**Remark (the same algebra in two rows).** $\mathbb{C}$, $\mathbb{B}$ and $R[G]$ each appear twice, once in each list, and the two rows are different objects of the category with the same underlying algebra. The reason is stated in §*The Collapse at the Identity*: the involution is part of the datum, so one module with two data gives two sesqualgebras, and the object of the category is the pair (algebra, involution) and not the algebra. This is why the table has a column for the datum and not only a column for the product. The repetition is not a redundancy: by the criterion above a full-type object has its datum determined by its product on a fixed base, so the second row of an algebra repeated over one base always carries a different product, the difference being carried by the involution that built it.

## Summary

The standard examples of the sesqualgebras are the field with its involution and the product $x\,\varsigma(y)$, the complex numbers with $x\bar y$, the split complex numbers and the dual numbers with the derived operation of an $\mathbb{R}$-linear involution, the quaternions with the derived operation of ${}^{\natural}$, the complex matrices with $ST^{*}$, the endomorphism algebra with $ST^{\dagger}$, the biquaternion algebra with the four products $PQ$, $P\,{}^{\natural}Q$, $PQ^{*}$ and $P\,{}^{\natural}Q^{*}$, the group algebra with $g\mapsto g^{-1}$, the zero product and the direct products. The datum $(R,\varsigma)$, the involution, the product, associativity, commutativity, the unit and full type are the data the theory assigns to each, and they are collected in the table of §*The Data Table*.

The governing fact is the **collapse**: with $\varsigma = \mathrm{id}$ the object is an ordinary algebra, and an object of full type with $\varsigma \neq \mathrm{id}$ is neither associative nor commutative. The genuinely sesquilinear examples are those with a nontrivial datum, the complex numbers, the complex matrices, the endomorphism algebra, the biquaternion algebra with the star and the group algebra over an involutive base; the collapsed ones are the real algebras, the complex numbers and the group algebra read over the trivial datum, the quaternion example, the two bilinear products of the biquaternion algebra and the zero product. The same algebra appears in both lists when it carries an involution that is semilinear for one datum and a product that is bilinear for the other, $\mathbb{C}$, $\mathbb{B}$ and $R[G]$ being the cases that do, because the involution is part of the datum and not an accident of the product. The definition and the collapse are *Sesqualgebras*; the product is *The Sesquilinear Product*; the involutions of the object are *The Involutions of a Sesqualgebra*; the matrices are *Matrix Sesqualgebras*; the biquaternions are *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*; and the products are *Tensor Products of Sesqualgebras* and *Direct Products of Sesqualgebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\varsigma$ | the base ring and its involution |
| $A$, $(R,\varsigma)$ | a sesqualgebra and its datum |
| $x\star y = xy^{*}$ | the derived operation of an algebra with an involution |
| $H(A)$, $S(A)$ | the Hermitian and the skew-Hermitian elements |
| full type | faithful over $R$, generating products, no nonzero left annihilator |
| $\mathbb{C},\mathbb{D},\mathbb{D}',\mathbb{H},\mathbb{B}$ | the complex, split complex, dual, quaternion and biquaternion algebras |
| ${}^{\natural}$, ${}^{*}$ | the quaternion conjugation and the biquaternion star |
| $M_n(\mathbb{C})$, $\operatorname{End}_R(M)$ | the matrix and endomorphism examples |
| ${}^{\dagger}$ | the adjoint of the endomorphism algebra |
| $R[G]$ | the group algebra with $g\mapsto g^{-1}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the classification and the examples of the algebras that the collapsed entries are read on.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions of the classical algebras and their semilinear counterparts.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group algebras, their units and their zero divisors.
