# __Introduction to the Symmetric Plain Algebra__

## Introduction

The underlying real vector space of the quaternion algebra $\mathbb{H}$ carries the general plain bilinear product $\tilde q_1\tilde q_2$, the multiplication of *Introduction to the Quaternion Algebra*. The exchange of the two arguments splits that product into a symmetric and an antisymmetric part, and each of the two parts is again a real bilinear product of the same space. This article reads the **symmetric part** as a multiplication in its own right:

$$
\tilde q_1\bullet\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1\bigr)
=\bigl(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\bigr)e_t+q_{1t}\vec q_2+q_{2t}\vec q_1.
$$

The operation is the plain product with the cross term dropped, and the space it makes of $\mathbb{H}$ is a commutative unital Jordan algebra over $\mathbb{R}$.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication from the plain product $\tilde q_1\tilde q_2$: it is commutative where the plain product is not, and its scalar part $q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$ is not the product of the scalar parts, so **the projection onto the scalar line is not multiplicative**. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

The reading is one of the companion products of *The 6 Products of the Quaternioid Real Space*, where the operation is named $\mathrm{SPA}$; it is the one commutative unital Jordan product among them, and its structure is *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The split that produces it, with its two projections and its two admissibility conditions, is the general material of *The Symmetric and Antisymmetric Parts of an Algebra Product*. This article owns the operation as a multiplication: the rule, the class, the laws, the sixteen products of the basis, the square and its polarisation, the reconstruction, and the placement of the block among the companion products. The algebra it builds is read further in the companions of the block: the Common Theory articles *Norm and Invertibility in the Symmetric Plain Algebra*, below this article in this category, *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category, *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category, *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category and *The Specificities of the Symmetric Plain Algebra*, below this article in this category, which owns the reduction of the idempotents and of the nilpotents; the Specific Theory article *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category; and, in the other sections of the block, *The Trace Form and the Invariance of the Symmetric Plain Algebra*, below this article in this category, *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, *Introduction to the Symmetric Plain Algebra*, below this article in this category and *The Symmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x \vec e_y=\vec e_z$, so that $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_\mu \vec e_\nu=-\vec e_\nu \vec e_\mu$ for $\mu\neq\nu$. A generic element is $\tilde q=q_te_t+\vec q$ with $\vec q=\sum_{k=1}^{3}q_k\vec e_k$ and $q_\mu\in\mathbb{R}$; $\vec q_1\cdot\vec q_2=\sum_kq_{1k}q_{2k}$ is the Euclidean dot product of the vector parts, and $\vec q_1\times\vec q_2$ their vector product. The plain product is $\tilde q_1\tilde q_2$ throughout; its scalar and vector forms, its table and its rules are those of *Introduction to the Quaternion Algebra* and *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, and the plain bilinear form is *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*.

## The Symmetrisation of the Plain Product

### The Rule

**Definition.** The **symmetric plain product** of two quaternions is

$$
\tilde q_1\bullet\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1\bigr).
$$

It is the **symmetrisation** of the general plain bilinear product $\tilde q_1\tilde q_2$, the operation called the symmetric part of the product in *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the operation named $\mathrm{SPA}$ in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The space $\mathbb{H}$ with the product $\bullet$ is written $\mathbb{H}^{\bullet}$ and is the **symmetric plain algebra** of the block.

The rule needs no more than the plain product, and *The Symmetric and Antisymmetric Parts of an Algebra Product* proves that the split is canonical: if a product is written as a sum of a symmetric and an antisymmetric operation, the two are forced to be the two halves. The symmetric half is fixed by the plain product alone and not by a choice of notation.

### The Coordinate and Scalar–Vector Forms

The plain product reads, in the scalar–vector form of *Introduction to the Quaternion Algebra*,

$$
\tilde q_1\tilde q_2=\bigl(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\bigr)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2,
$$

and its exchange $\tilde q_2\tilde q_1$ differs from it only in the sign of the cross term. Adding the two and halving gives the rule that names the block:

$$
\tilde q_1\bullet\tilde q_2=\bigl(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\bigr)+q_{1t}\vec q_2+q_{2t}\vec q_1.
$$

**Remark (the cross term is what the symmetrisation removes).** The scalar part $q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$ is symmetric by itself, since $\vec q_1\cdot\vec q_2=\vec q_2\cdot\vec q_1$, and the mixed vector part $q_{1t}\vec q_2+q_{2t}\vec q_1$ is symmetric as well; the only asymmetric piece of the plain product is the cross product $\vec q_1\times\vec q_2$, which changes sign under the exchange. **The symmetric plain product is exactly the plain product with the cross term dropped**, and the vector part of the value is $q_{1t}\vec q_2+q_{2t}\vec q_1$.

Read on the coordinates, the same rule is the plain coordinate rule with the cross terms deleted:

$$
\tilde q_1\bullet\tilde q_2=\bigl(q_{1t}q_{2t}-q_{1x}q_{2x}-q_{1y}q_{2y}-q_{1z}q_{2z}\bigr)+\bigl(q_{1t}q_{2x}+q_{1x}q_{2t}\bigr)\vec e_x+\bigl(q_{1t}q_{2y}+q_{1y}q_{2t}\bigr)\vec e_y+\bigl(q_{1t}q_{2z}+q_{1z}q_{2t}\bigr)\vec e_z.
$$

The two forms are one rule, and each is used where it is shorter.

### Bilinearity and the Class

**Proposition.** The symmetric plain product is $\mathbb{R}$-**bilinear**:

$$
(\tilde q_1+\tilde q_2)\bullet\tilde q_3=\tilde q_1\bullet\tilde q_3+\tilde q_2\bullet\tilde q_3,\qquad
\tilde q_3\bullet(\tilde q_1+\tilde q_2)=\tilde q_3\bullet\tilde q_1+\tilde q_3\bullet\tilde q_2,\qquad
(a\tilde q_1)\bullet\tilde q_3=a(\tilde q_1\bullet\tilde q_3)=\tilde q_1\bullet(a\tilde q_3)
$$

for every $a\in\mathbb{R}$.

*Proof.* The plain product is $\mathbb{R}$-bilinear, and the sum of two $\mathbb{R}$-bilinear maps and the halving keep the class; equivalently, the displayed coordinate rule is additive and homogeneous in the coordinates of each argument separately.

**Remark (why the class survives the split).** The plain product has two $\mathbb{R}$-linear slots, so its two slots have the same type and the bare interchange of the arguments is an exchange that keeps the class; the two halves are $\mathbb{R}$-bilinear again. This is the **algebra case** of the general split. **The symmetric plain product is $\mathbb{R}$-bilinear, and the obstruction of the class does not arise in this block.**

## The Algebra the Symmetrisation Defines

### Commutativity

**Proposition.** The symmetric plain product is **commutative**:

$$
\tilde q_1\bullet\tilde q_2=\tilde q_2\bullet\tilde q_1.
$$

*Proof.* The half-sum of the plain product and its exchange is unchanged when the two arguments are interchanged; equivalently, the scalar part is the symmetric bilinear form $q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$ and the vector part $q_{1t}\vec q_2+q_{2t}\vec q_1$ is symmetric in the two elements.

Commutativity is the defining departure from the plain product, which is not commutative, since $\vec e_x \vec e_y=\vec e_z$ and $\vec e_y \vec e_x=-\vec e_z$. The commutator of the plain product is carried entirely by the antisymmetric part,

$$
[\tilde q_1,\tilde q_2]=\tilde q_1\tilde q_2-\tilde q_2\tilde q_1=2\,\vec q_1\times\vec q_2,
$$

which is the operation of the companion block *Introduction to the Antisymmetric Plain Algebra*, below this article in this category.

### The Unit

**Proposition.** The element $e_t$ is a **two-sided identity** of the symmetric plain product:

$$
e_t\bullet\tilde q=\tilde q\bullet e_t=\tilde q.
$$

*Proof.* $e_t$ is the identity of the plain product, so $\tfrac12(e_t\tilde q+\tilde qe_t)=\tfrac12(\tilde q+\tilde q)=\tilde q$.

The identity is unique, and $e_t$ is the only element that serves, as it is for the plain product. The operation is therefore **unital**, and the unit is two-sided because the product is commutative.

**Remark (the block has a unit).** The claim that a Jordan product has no unit is not true of this one: $e_t$ is a two-sided unit of $\bullet$, and it is the unit of the ambient algebra as well. The menu comment of the block says "the unit $e_t$ on both sides", and the reading above agrees with it; the brief of the block describing the operation as having "no unit" is the contrary statement, and the computation $e_t\bullet\tilde q=\tilde q$ settles it in favour of the unit.

### The Jordan Identity

**Definition.** A commutative product is a **Jordan product** when it satisfies the **Jordan identity**

$$
(x\bullet y)\bullet(x\bullet x)=x\bullet\bigl(y\bullet(x\bullet x)\bigr),
$$

and a commutative algebra with a Jordan product is a **Jordan algebra**.

**Theorem.** The symmetric plain product satisfies the Jordan identity: for all $\tilde q_1,\tilde q_2\in\mathbb{H}$,

$$
(\tilde q_1\bullet\tilde q_2)\bullet(\tilde q_1\bullet\tilde q_1)=\tilde q_1\bullet\bigl(\tilde q_2\bullet(\tilde q_1\bullet\tilde q_1)\bigr).
$$

*Proof.* The symmetrisation of an associative product always satisfies the Jordan identity: for an associative algebra $A$, the algebra $A^{+}$ with the product $\tfrac12(xy+yx)$ is the classical special Jordan algebra, and it is the theorem of *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*, that $A^{+}$ is a Jordan algebra, proved there by a direct expansion with the product $xy+yx$ (the halved product satisfies the identity as well, every coefficient being halved). Expanding both sides in the associative product of $\mathbb{H}$ and using associativity verifies the identity directly.

**Remark (the identity is what singles out the block).** Of the two symmetrisations the space carries, exactly one satisfies the Jordan identity, and of the two antisymmetrisations exactly one satisfies the Jacobi identity; both sit in the plain row, $\mathrm{SPA}$ being the Jordan product and $\mathrm{APA}$ the Lie product. The scalar-valued symmetrisation of the quaternionic product is commutative but fails the Jordan identity; it is scalar valued and has no unit, so the two symmetric parts are separated by the identity. Read without the restriction to the parts, the Jordan identity also holds at every element of the associative general plain product and, vacuously, for the two alternating antisymmetrisations, so the identity by itself does not isolate the block; the restriction to the parts of their kind is the corpus's convention, and it is *The Specificities of the Symmetric Plain Algebra*, below this article in this category, that states the exact criterion, commutativity together with the Jordan identity. **Read with the product $\bullet$, the quaternion space is a commutative unital Jordan algebra over $\mathbb{R}$**, and it is a *special* Jordan algebra, because it is the symmetrisation of an associative algebra. Its degree and its norm are *Norm and Invertibility in the Symmetric Plain Algebra*, below this article in this category, and its idempotents and nilpotents, which reduce to the trivial ones, are *The Specificities of the Symmetric Plain Algebra*, below this article in this category.

### The Failure of Associativity

**Proposition.** The symmetric plain product is **not associative**.

*Proof.* The witness is the pair $\tilde q_1=\tilde q_2=\vec e_x$ read against $\tilde q_3=\vec e_y$:

$$
(\vec e_x\bullet \vec e_x)\bullet \vec e_y=(-e_t)\bullet \vec e_y=-\vec e_y,\qquad
\vec e_x\bullet(\vec e_x\bullet \vec e_y)=\vec e_x\bullet 0=0,
$$

and the two values differ.

The failure is the reason the block is a Jordan algebra and not an associative one; the Jordan identity is the substitute for associativity that the symmetrisation keeps, and it is weaker, as the witness shows. The block is nevertheless **power-associative**, all bracketings of a power of one element agreeing, because the subalgebra generated by a single element is associative; the non-trivial failure is the associator of three distinct elements.

### The Sixteen Products of the Basis

The product is $\mathbb{R}$-bilinear, so it is fixed by its values on the sixteen pairs of basis elements.

**Proposition.** The products of the basis elements are

| $\bullet$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $0$ | $0$ |
| $\vec e_y$ | $\vec e_y$ | $0$ | $-e_t$ | $0$ |
| $\vec e_z$ | $\vec e_z$ | $0$ | $0$ | $-e_t$ |

*Proof.* Each entry is $\tfrac12(e_\mu e_\nu+e_\nu e_\mu)$ read from the multiplication table of *Introduction to the Quaternion Algebra*. For $\mu=\nu=t$ the entry is $e_t$; for $\mu=\nu\in\{x,y,z\}$ it is $\vec e_\mu^2=-e_t$; for one index $t$ it is the other basis element, the unit acting trivially; and for two distinct vector indices the quaternion units anticommute, $\vec e_\mu \vec e_\nu=-\vec e_\nu \vec e_\mu$, so the two terms cancel and the entry is $0$. The table is symmetric, as commutativity requires, and its diagonal is $e_t,-e_t,-e_t,-e_t$.

**Remark (the table against the plain one).** The table of the block is the quaternion table with the six signed off-diagonal vector entries replaced by $0$; it keeps the diagonal $e_t,-e_t,-e_t,-e_t$ and the first row and column. **The two tables differ only where the plain product is skew, which is off the diagonal in the vector block.**

### The Square and Its Polarisation

**Proposition.** The square of an element in the block is the plain square,

$$
\tilde q\bullet\tilde q=\tilde q^2=\bigl(q_t^2-|\vec q|^2\bigr)e_t+2q_t\vec q,
$$

so the diagonal of $\bullet$ and the diagonal of the plain product agree.

*Proof.* $\tilde q\bullet\tilde q=\tfrac12(\tilde q^2+\tilde q^2)=\tilde q^2$, and the plain square is the displayed form by the scalar–vector rule with $\tilde q_1=\tilde q_2$.

**Proposition (polarisation).** The product off the diagonal is recovered from the square by polarisation:

$$
\tilde q_1\bullet\tilde q_2=\tfrac12\bigl((\tilde q_1+\tilde q_2)\bullet(\tilde q_1+\tilde q_2)-\tilde q_1\bullet\tilde q_1-\tilde q_2\bullet\tilde q_2\bigr).
$$

*Proof.* The product is $\mathbb{R}$-bilinear and commutative, so expanding the square of the sum gives $(\tilde q_1+\tilde q_2)\bullet(\tilde q_1+\tilde q_2)=\tilde q_1\bullet\tilde q_1+2\tilde q_1\bullet\tilde q_2+\tilde q_2\bullet\tilde q_2$, and the displayed identity follows by subtraction and halving.

So the square map $\tilde q\mapsto\tilde q\bullet\tilde q$ determines the whole product. The square, its idempotents and its inverse are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category.

## The Reconstruction

### The Reconstruction of the Algebra Product

**Theorem.** The plain product is the sum of its two parts:

$$
\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\times\tilde q_2,\qquad
\tilde q_1\times\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1\bigr)=\vec q_1\times\vec q_2,
$$

and the symmetric part is $\mathrm{SPA}$ and the antisymmetric part $\mathrm{APA}$.

*Proof.* Adding the two halves restores the product, and the antisymmetric half of the algebra product is the cross product of the two vector parts, as *Introduction to the Antisymmetric Plain Algebra*, below this article in this category, develops. The identity is the plain row reconstruction $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ of *The 6 Products of the Quaternioid Real Space*.

The two halves have opposite symmetry, so either determines the other from the product, and the pair is the unique such decomposition. The algebra product is the one whose symmetric part is the Jordan product and whose antisymmetric part is the Lie product; the block that reads the antisymmetric half is *Introduction to the Antisymmetric Plain Algebra*, below this article in this category.

### The Placement among the Companion Products

The name $\mathrm{SPA}$ is read with the code of *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*: the first letter $\mathrm{S}$ says that the operation is a symmetric part, the second letter $\mathrm{P}$ that it comes from the plain product, and the third letter $\mathrm{A}$ that it is a real bilinear algebra product.

| the algebra product | symmetric half | antisymmetric half |
|---|---|---|
| $\tilde q_1\tilde q_2$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |

**Remark (the place of the block).** The block $\mathrm{SPA}$ is the symmetrisation of the algebra product $\tilde q_1\tilde q_2$, whose antisymmetrisation is $\mathrm{APA}$; the two halves carry the two classical nonassociative laws, $\mathrm{SPA}$ the Jordan product and $\mathrm{APA}$ the Lie product. **$\mathrm{SPA}$ is the commutative unital Jordan product of the space**, and it is the block whose generic norm is positive definite. The laws are owned by *The 6 Products of the Quaternioid Real Space* and the names by *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

## Summary

The symmetric part of the general plain bilinear product of $\mathbb{H}$ is the operation

$$
\tilde q_1\bullet\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1\bigr)
=\bigl(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\bigr)e_t+q_{1t}\vec q_2+q_{2t}\vec q_1,
$$

the plain product with the cross term dropped. It is $\mathbb{R}$-bilinear and commutative, $e_t$ is a two-sided unit, it satisfies the Jordan identity, and it is not associative, with the witness $(\vec e_x\bullet \vec e_x)\bullet \vec e_y=-\vec e_y$ against $\vec e_x\bullet(\vec e_x\bullet \vec e_y)=0$. Read with the product, the space is a commutative unital special Jordan algebra over $\mathbb{R}$, and it is the one Jordan product among the companion products. The sixteen products of the basis are the quaternion table with the six off-diagonal vector entries set to $0$; the square is the plain square, $\tilde q\bullet\tilde q=(q_t^2-|\vec q|^2)e_t+2q_t\vec q$, and the product is the polarisation of the square. The algebra product reconstructs as $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$, the symmetrisation of an associative product, read in *The 6 Products of the Quaternioid Real Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ | the symmetrised (Jordan) product, the multiplication of the block |
| $\mathbb{H}^{\bullet}$ | the quaternion space with the symmetric plain product |
| $\mathrm{SPA}$ | the name of the operation among the companion products |
| $\tilde q_1\times\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$ | the antisymmetric part, $\mathrm{APA}$ |
| $\tilde q\bullet\tilde q=\tilde q^2$ | the square of the block, the plain square |
| $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ | the reconstruction of the algebra product |
| $\tilde q^{\natural}=q_te_t-\vec q$ | the quaternion conjugation, the natural sign |
| $\vec q_1\cdot\vec q_2$, $\vec q_1\times\vec q_2$ | the dot and the vector products of the vector parts |

## Further Reading

- *The 6 Products of the Quaternioid Real Space*, for the companion products, their names and their table.
- *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, for the structures the companion products define and the two laws that separate them.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the split, its uniqueness and the two admissibility conditions.
- *Introduction to the Quaternion Algebra*, for the product the block splits and its multiplication table.
- *Introduction to the Antisymmetric Plain Algebra*, below this article in this category, for the companion half, the cross product and the Lie structure.
- *Norm and Invertibility in the Symmetric Plain Algebra*, below this article in this category, *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category, *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category, *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, below this article in this category and *The Specificities of the Symmetric Plain Algebra*, below this article in this category, for the Common Theory of the block.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category, *The Trace Form and the Invariance of the Symmetric Plain Algebra*, below this article in this category, *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category and the two matrix-representation articles, for the remainder of the block.
