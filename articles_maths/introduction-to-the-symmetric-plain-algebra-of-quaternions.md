# __Introduction to the Symmetric Plain Algebra of Quaternions__

## Introduction

The underlying real vector space of the quaternion algebra $\mathbb{H}$ carries the general plain bilinear product $\tilde p\tilde q$, the multiplication of *Introduction to the General Plain Algebra of Quaternions*. The exchange of the two arguments splits that product into a symmetric and an antisymmetric part, and each of the two parts is again a real bilinear product of the same space. This article reads the **symmetric part** as a multiplication in its own right:

$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr)
=\bigl(p_0q_0-\mathbf p\cdot\mathbf q\bigr)e_0+p_0\mathbf q+q_0\mathbf p.
$$

The operation is the plain product with the cross term dropped, and the space it makes of $\mathbb{H}$ is a commutative unital Jordan algebra over $\mathbb{R}$.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication from the plain product $\tilde p\tilde q$: it is commutative where the plain product is not, and its scalar part $p_0q_0-\mathbf p\cdot\mathbf q$ is not the product of the scalar parts, so **the projection onto the scalar line is not multiplicative**. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

The reading is one of the six operations of *The 6 Products of the Quaternion Real Space*, where the operation is named $\mathrm{SPA}$; it is the one commutative unital Jordan product of the six, and its structure among them is *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The split that produces it, with its two projections and its two admissibility conditions, is the general material of *The Symmetric and Antisymmetric Parts of an Algebra Product*. This article owns the operation as a multiplication: the rule, the class, the laws, the sixteen products of the basis, the square and its polarisation, the reconstruction, and the placement of the block among the six. The algebra it builds is read further in the companions of the block: the Common Theory articles *Norm and Invertibility in the Symmetric Plain Algebra*, below this article in this category, *Zero Divisors of the Symmetric Plain Algebra*, below this article in this category, *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*, below this article in this category, *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*, below this article in this category, *Square Roots of a General Element in the Symmetric Plain Algebra*, below this article in this category and *The Specificities of the Symmetric Plain Algebra*, below this article in this category, which owns the reduction of the idempotents and of the nilpotents; the Specific Theory article *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category; and, in the other sections of the block, *The Trace Form and the Invariance of the Symmetric Plain Algebra*, below this article in this category, *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, *The Symmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, below this article in this category and *The Symmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, so that $e_1^2=e_2^2=e_3^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. A generic element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $\mathbf p\cdot\mathbf q=\sum_kp_kq_k$ is the Euclidean dot product of the vector parts, and $\mathbf p\times\mathbf q$ their vector product. The plain product is $\tilde p\tilde q$ throughout; its scalar and vector forms, its table and its rules are those of *Introduction to the General Plain Algebra of Quaternions* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*, and the plain bilinear form is *The 2 Forms over the Quaternion $\mathbb{R}$ Space*.

## The Symmetrisation of the Plain Product

### The Rule

**Definition.** The **symmetric plain product** of two quaternions is

$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr).
$$

It is the **symmetrisation** of the general plain bilinear product $\tilde p\tilde q$, the operation called the symmetric part of the product in *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the operation named $\mathrm{SPA}$ in *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The space $\mathbb{H}$ with the product $\bullet$ is written $\mathbb{H}^{\bullet}$ and is the **symmetric plain algebra** of the block.

The rule needs no more than the plain product, and *The Symmetric and Antisymmetric Parts of an Algebra Product* proves that the split is canonical: if a product is written as a sum of a symmetric and an antisymmetric operation, the two are forced to be the two halves. The symmetric half is fixed by the plain product alone and not by a choice of notation.

### The Coordinate and Scalar–Vector Forms

The plain product reads, in the scalar–vector form of *Introduction to the General Plain Algebra of Quaternions*,

$$
\tilde p\tilde q=\bigl(p_0q_0-\mathbf p\cdot\mathbf q\bigr)+p_0\mathbf q+q_0\mathbf p+\mathbf p\times\mathbf q,
$$

and its exchange $\tilde q\tilde p$ differs from it only in the sign of the cross term. Adding the two and halving gives the rule that names the block:

$$
\tilde p\bullet\tilde q=\bigl(p_0q_0-\mathbf p\cdot\mathbf q\bigr)+p_0\mathbf q+q_0\mathbf p.
$$

**Remark (the cross term is what the symmetrisation removes).** The scalar part $p_0q_0-\mathbf p\cdot\mathbf q$ is symmetric by itself, since $\mathbf p\cdot\mathbf q=\mathbf q\cdot\mathbf p$, and the mixed vector part $p_0\mathbf q+q_0\mathbf p$ is symmetric as well; the only asymmetric piece of the plain product is the cross product $\mathbf p\times\mathbf q$, which changes sign under the exchange. **The symmetric plain product is exactly the plain product with the cross term dropped**, and the vector part of the value is $p_0\mathbf q+q_0\mathbf p$.

Read on the coordinates, the same rule is the plain coordinate rule with the cross terms deleted:

$$
\tilde p\bullet\tilde q=\bigl(p_0q_0-p_1q_1-p_2q_2-p_3q_3\bigr)+\bigl(p_0q_1+p_1q_0\bigr)e_1+\bigl(p_0q_2+p_2q_0\bigr)e_2+\bigl(p_0q_3+p_3q_0\bigr)e_3.
$$

The two forms are one rule, and each is used where it is shorter.

### Bilinearity and the Class

**Proposition.** The symmetric plain product is $\mathbb{R}$-**bilinear**:

$$
(\tilde p+\tilde r)\bullet\tilde q=\tilde p\bullet\tilde q+\tilde r\bullet\tilde q,\qquad
\tilde q\bullet(\tilde p+\tilde r)=\tilde q\bullet\tilde p+\tilde q\bullet\tilde r,\qquad
(a\tilde p)\bullet\tilde q=a(\tilde p\bullet\tilde q)=\tilde p\bullet(a\tilde q)
$$

for every $a\in\mathbb{R}$.

*Proof.* The plain product is $\mathbb{R}$-bilinear, and the sum of two $\mathbb{R}$-bilinear maps and the halving keep the class; equivalently, the displayed coordinate rule is additive and homogeneous in the coordinates of each argument separately.

**Remark (why the class survives the split).** The plain product has two $\mathbb{R}$-linear slots, so its two slots have the same type and the bare interchange of the arguments is an exchange that keeps the class; the two halves are $\mathbb{R}$-bilinear again. This is the **algebra case** of the general split. **The symmetric plain product is $\mathbb{R}$-bilinear, and the obstruction of the class does not arise in this block.**

## The Algebra the Symmetrisation Defines

### Commutativity

**Proposition.** The symmetric plain product is **commutative**:

$$
\tilde p\bullet\tilde q=\tilde q\bullet\tilde p.
$$

*Proof.* The half-sum of the plain product and its exchange is unchanged when the two arguments are interchanged; equivalently, the scalar part is the symmetric bilinear form $p_0q_0-\mathbf p\cdot\mathbf q$ and the vector part $p_0\mathbf q+q_0\mathbf p$ is symmetric in the two elements.

Commutativity is the defining departure from the plain product, which is not commutative, since $e_1e_2=e_3$ and $e_2e_1=-e_3$. The commutator of the plain product is carried entirely by the antisymmetric part,

$$
[\tilde p,\tilde q]=\tilde p\tilde q-\tilde q\tilde p=2\,\mathbf p\times\mathbf q,
$$

which is the operation of the companion block *Introduction to the Antisymmetric Plain Algebra of Quaternions*, below this article in this category.

### The Unit

**Proposition.** The element $e_0$ is a **two-sided identity** of the symmetric plain product:

$$
e_0\bullet\tilde q=\tilde q\bullet e_0=\tilde q.
$$

*Proof.* $e_0$ is the identity of the plain product, so $\tfrac12(e_0\tilde q+\tilde qe_0)=\tfrac12(\tilde q+\tilde q)=\tilde q$.

The identity is unique, and $e_0$ is the only element that serves, as it is for the plain product. The operation is therefore **unital**, and the unit is two-sided because the product is commutative.

**Remark (the block has a unit).** The claim that a Jordan product has no unit is not true of this one: $e_0$ is a two-sided unit of $\bullet$, and it is the unit of the ambient algebra as well. The menu comment of the block says "the unit $e_0$ on both sides", and the reading above agrees with it; the brief of the block describing the operation as having "no unit" is the contrary statement, and the computation $e_0\bullet\tilde q=\tilde q$ settles it in favour of the unit.

### The Jordan Identity

**Definition.** A commutative product is a **Jordan product** when it satisfies the **Jordan identity**

$$
(x\bullet y)\bullet(x\bullet x)=x\bullet\bigl(y\bullet(x\bullet x)\bigr),
$$

and a commutative algebra with a Jordan product is a **Jordan algebra**.

**Theorem.** The symmetric plain product satisfies the Jordan identity: for all $\tilde p,\tilde q\in\mathbb{H}$,

$$
(\tilde p\bullet\tilde q)\bullet(\tilde p\bullet\tilde p)=\tilde p\bullet\bigl(\tilde q\bullet(\tilde p\bullet\tilde p)\bigr).
$$

*Proof.* The symmetrisation of an associative product always satisfies the Jordan identity: for an associative algebra $A$, the algebra $A^{+}$ with the product $\tfrac12(xy+yx)$ is the classical special Jordan algebra, and it is the theorem of *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*, that $A^{+}$ is a Jordan algebra, proved there by a direct expansion with the product $xy+yx$ (the halved product satisfies the identity as well, every coefficient being halved). Expanding both sides in the associative product of $\mathbb{H}$ and using associativity verifies the identity directly.

**Remark (the identity is what singles out the block).** Of the two symmetric parts of the six operations of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, exactly one satisfies the Jordan identity, and of the two antisymmetric parts exactly one satisfies the Jacobi identity; both sit in the plain row, $\mathrm{SPA}$ being the Jordan product and $\mathrm{APA}$ the Lie product. The symmetric quaternionic product is commutative but fails the Jordan identity, with the witness $x=(-3,-3,3,2)$, $y=(2,-3,1,2)$, where the two sides are $310e_0$ and $-186e_0$; it is scalar valued and has no unit, so the two symmetric parts are separated by the identity. Read without the restriction to the parts, the Jordan identity also holds at every element of the associative general plain product and, vacuously, for the two alternating antisymmetrisations, so the identity by itself does not isolate the block; the restriction to the parts of their kind is the corpus's convention, and it is *The Specificities of the Symmetric Plain Algebra*, below this article in this category, that states the exact criterion, commutativity together with the Jordan identity. **Read with the product $\bullet$, the quaternion space is a commutative unital Jordan algebra over $\mathbb{R}$**, and it is a *special* Jordan algebra, because it is the symmetrisation of an associative algebra. Its degree and its norm are *Norm and Invertibility in the Symmetric Plain Algebra*, below this article in this category, and its idempotents and nilpotents, which reduce to the trivial ones, are *The Specificities of the Symmetric Plain Algebra*, below this article in this category.

### The Failure of Associativity

**Proposition.** The symmetric plain product is **not associative**.

*Proof.* The witness is the pair $\tilde p=\tilde q=e_1$ read against $\tilde r=e_2$:

$$
(e_1\bullet e_1)\bullet e_2=(-e_0)\bullet e_2=-e_2,\qquad
e_1\bullet(e_1\bullet e_2)=e_1\bullet 0=0,
$$

and the two values differ.

The failure is the reason the block is a Jordan algebra and not an associative one; the Jordan identity is the substitute for associativity that the symmetrisation keeps, and it is weaker, as the witness shows. The block is nevertheless **power-associative**, all bracketings of a power of one element agreeing, because the subalgebra generated by a single element is associative; the non-trivial failure is the associator of three distinct elements.

### The Sixteen Products of the Basis

The product is $\mathbb{R}$-bilinear, so it is fixed by its values on the sixteen pairs of basis elements.

**Proposition.** The products of the basis elements are

| $\bullet$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $0$ | $0$ |
| $e_2$ | $e_2$ | $0$ | $-e_0$ | $0$ |
| $e_3$ | $e_3$ | $0$ | $0$ | $-e_0$ |

*Proof.* Each entry is $\tfrac12(e_\mu e_\nu+e_\nu e_\mu)$ read from the multiplication table of *Introduction to the General Plain Algebra of Quaternions*. For $\mu=\nu=0$ the entry is $e_0$; for $\mu=\nu=k$ it is $e_k^2=-e_0$; for one index $0$ it is the other basis element, the unit acting trivially; and for two distinct vector indices the quaternion units anticommute, $e_je_k=-e_ke_j$, so the two terms cancel and the entry is $0$. The table is symmetric, as commutativity requires, and its diagonal is $e_0,-e_0,-e_0,-e_0$.

**Remark (the table against the plain one).** The table of the block is the quaternion table with the six signed off-diagonal vector entries replaced by $0$; it keeps the diagonal $e_0,-e_0,-e_0,-e_0$ and the first row and column. **The two tables differ only where the plain product is skew, which is off the diagonal in the vector block.**

### The Square and Its Polarisation

**Proposition.** The square of an element in the block is the plain square,

$$
\tilde q\bullet\tilde q=\tilde q^2=\bigl(q_0^2-|\mathbf q|^2\bigr)e_0+2q_0\mathbf q,
$$

so the diagonal of $\bullet$ and the diagonal of the plain product agree.

*Proof.* $\tilde q\bullet\tilde q=\tfrac12(\tilde q^2+\tilde q^2)=\tilde q^2$, and the plain square is the displayed form by the scalar–vector rule with $\tilde p=\tilde q$.

**Proposition (polarisation).** The product off the diagonal is recovered from the square by polarisation:

$$
\tilde p\bullet\tilde q=\tfrac12\bigl((\tilde p+\tilde q)\bullet(\tilde p+\tilde q)-\tilde p\bullet\tilde p-\tilde q\bullet\tilde q\bigr).
$$

*Proof.* The product is $\mathbb{R}$-bilinear and commutative, so expanding the square of the sum gives $(\tilde p+\tilde q)\bullet(\tilde p+\tilde q)=\tilde p\bullet\tilde p+2\tilde p\bullet\tilde q+\tilde q\bullet\tilde q$, and the displayed identity follows by subtraction and halving.

So the square map $\tilde q\mapsto\tilde q\bullet\tilde q$ determines the whole product. The square, its idempotents and its inverse are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category.

## The Reconstruction and the Six

### The Reconstruction $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$

**Theorem.** The plain product is the sum of its two parts:

$$
\tilde p\tilde q=\tilde p\bullet\tilde q+\tilde p\times\tilde q,\qquad
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\mathbf p\times\mathbf q,
$$

and the symmetric part is $\mathrm{SPA}$ and the antisymmetric part $\mathrm{APA}$.

*Proof.* Adding the two halves restores the product, and the antisymmetric half of the plain product is the cross product of the two vector parts, as *Introduction to the Antisymmetric Plain Algebra of Quaternions*, below this article in this category, develops. The identity is one of the two row reconstructions $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ and $\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$ of *The 6 Products of the Quaternion Real Space*.

The two halves have opposite symmetry, so either determines the other from the product, and the pair is the unique such decomposition. The plain row is the one whose symmetric part is the Jordan product and whose antisymmetric part is the Lie product; the companion block that reads the antisymmetric half is *Introduction to the Antisymmetric Plain Algebra of Quaternions*, below this article in this category.

### The Placement among the Six

The name $\mathrm{SPA}$ is read with the code of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*: the first letter $\mathrm{S}$ says that the operation is the symmetric part of the row, the second letter $\mathrm{P}$ that it comes from the plain product, and the third letter $\mathrm{A}$ that it is a real bilinear algebra product.

| the row | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |

**Remark (the place of the block).** The block $\mathrm{SPA}$ is the symmetrisation of the associative product $\mathrm{GPA}$, and the companion block $\mathrm{SQA}$ is the symmetrisation of the quaternionic product $\mathrm{GQA}$; the antisymmetric parts $\mathrm{APA}$ and $\mathrm{AQA}$ are the two Lie candidates. Two of the six operations pass the identity of a classical nonassociative algebra, both in the plain row: $\mathrm{APA}$ is the Lie product and $\mathrm{SPA}$ the Jordan product. **Of the six operations, $\mathrm{SPA}$ is the commutative unital Jordan product; it is the only one of the two symmetric parts that satisfies the Jordan identity, and it is the block whose generic norm is positive definite** — the symmetric quaternionic product is commutative, scalar valued and without a unit, and its square of $e_1$ is $+e_0$, not $-e_0$. The laws are owned by *The 6 Products of the Quaternion Real Space* and the names by *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

## Summary

The symmetric part of the general plain bilinear product of $\mathbb{H}$ is the operation

$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr)
=\bigl(p_0q_0-\mathbf p\cdot\mathbf q\bigr)e_0+p_0\mathbf q+q_0\mathbf p,
$$

the plain product with the cross term dropped. It is $\mathbb{R}$-bilinear and commutative, $e_0$ is a two-sided unit, it satisfies the Jordan identity, and it is not associative, with the witness $(e_1\bullet e_1)\bullet e_2=-e_2$ against $e_1\bullet(e_1\bullet e_2)=0$. Read with the product, the space is a commutative unital special Jordan algebra over $\mathbb{R}$, and it is the one Jordan product of the six operations. The sixteen products of the basis are the quaternion table with the six off-diagonal vector entries set to $0$; the square is the plain square, $\tilde q\bullet\tilde q=(q_0^2-|\mathbf q|^2)e_0+2q_0\mathbf q$, and the product is the polarisation of the square. The plain product reconstructs as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, the symmetrisation of an associative product in the plain row of *The 6 Products of the Quaternion Real Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ | the symmetrised (Jordan) product, the multiplication of the block |
| $\mathbb{H}^{\bullet}$ | the quaternion space with the symmetric plain product |
| $\mathrm{SPA}$ | the name of the operation among the six |
| $\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\mathbf p\times\mathbf q$ | the antisymmetric part, $\mathrm{APA}$ |
| $\tilde q\bullet\tilde q=\tilde q^2$ | the square of the block, the plain square |
| $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ | the reconstruction of the plain product |
| $\tilde q^{\natural}=q_0e_0-\mathbf q$ | the quaternion conjugation, the natural sign |
| $\mathbf p\cdot\mathbf q$, $\mathbf p\times\mathbf q$ | the dot and the vector products of the vector parts |

## Further Reading

- *The 6 Products of the Quaternion Real Space*, for the six operations, their names and their table.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, for the structures the six define and the two laws that separate them.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the split, its uniqueness and the two admissibility conditions.
- *Introduction to the General Plain Algebra of Quaternions*, for the product the block splits and its multiplication table.
- *Introduction to the Antisymmetric Plain Algebra of Quaternions*, below this article in this category, for the companion half, the cross product and the Lie structure.
- *Norm and Invertibility in the Symmetric Plain Algebra*, below this article in this category, *Zero Divisors of the Symmetric Plain Algebra*, below this article in this category, *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*, below this article in this category, *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*, below this article in this category, *Square Roots of a General Element in the Symmetric Plain Algebra*, below this article in this category and *The Specificities of the Symmetric Plain Algebra*, below this article in this category, for the Common Theory of the block.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category, *The Trace Form and the Invariance of the Symmetric Plain Algebra*, below this article in this category, *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category and the two matrix-representation articles, for the remainder of the block.
