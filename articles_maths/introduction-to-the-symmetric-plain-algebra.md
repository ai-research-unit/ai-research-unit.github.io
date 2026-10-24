# __Introduction to the Symmetric Plain Algebra__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries the general plain bilinear product $\tilde Q_1\tilde Q_2$, the multiplication of *The Biquaternion Algebra and Its Vector Spaces*. Its exchange of the two arguments splits it into a symmetric and an antisymmetric part, and each of the two parts is again a $\mathbb{C}$-bilinear product of the space. This article reads the **symmetric part** as a multiplication in its own right:

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr)
=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1.
$$

The operation is the plain product with the cross term dropped, and the space it makes of $\mathbb{B}$ is a commutative unital Jordan algebra over $\mathbb{C}$. The reading is one of the twelve operations of *Symmetric and Antisymmetric Decomposition of the Four General Products*, where the operation is named $\mathrm{SPA}$ and is one of the two members of the twelve that satisfies the identity of a classical nonassociative algebra.

The split that produces the operation, its two projections and the two admissibility conditions are *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the order-symmetry reading of the same split, with the worked examples on the four general products, is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. This article owns the operation as a multiplication: the rule, the class, the laws, the sixteen products of the basis, the square and its polarisation, the reconstruction, and the placement of the block among the twelve. The algebra it builds is read further in the companions of the block: the Common Theory articles *Norm and Invertibility in the Symmetric Plain Algebra*, *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, which close with *The Specificities of the Symmetric Plain Algebra*; the Specific Theory article *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*; and, in the other sections of the block, *The Trace Form and the Invariance of the Symmetric Plain Algebra*, *Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions*, *The Multiplication Operators of the Symmetric Plain Algebra* and the two articles *Introduction to the Symmetric Plain Algebra*.

## The Symmetrisation of the Plain Product

### The Rule

**Definition.** The **symmetric plain product** of two biquaternions is

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr).
$$

It is the **symmetrisation** of the general plain bilinear product $\tilde Q_1\tilde Q_2$, the operation called the symmetric part of the product in *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the operation named $\mathrm{SPA}$ in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The space $\mathbb{B}$ with the product $\bullet$ is written $\mathbb{B}^{\bullet}$ and is the **symmetric plain algebra** of the block.

The rule needs no more than the plain product, and *The Symmetric and Antisymmetric Parts of an Algebra Product* proves that the split is canonical: if a product is written as a sum of a symmetric and an antisymmetric operation, the two are forced to be the two halves. The symmetric half is therefore fixed by the plain product alone and not by a choice of notation.

### The Coordinate and Scalar–Vector Forms

The plain product reads, in the scalar–vector form of *The Biquaternion Algebra and Its Vector Spaces*,

$$
\tilde Q_1\tilde Q_2=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2,
$$

and its exchange $\tilde Q_2\tilde Q_1$ differs from it only in the sign of the cross term. Adding the two and halving gives the rule that names the block:

$$
\tilde Q_1\bullet\tilde Q_2=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1.
$$

**Remark (the cross term is what the symmetrisation removes).** The scalar part $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ is symmetric by itself, since $(\vec Q_1,\vec Q_2)=(\vec Q_2,\vec Q_1)$, and the mixed vector part $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ is symmetric as well; the only asymmetric piece of the plain product is the cross product $\vec Q_1\times\vec Q_2$, which changes sign under the exchange. **The symmetric plain product is therefore exactly the plain product with the cross term dropped**, and the vector part of the value is $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$.

Read on the coordinates, the same rule is the plain coordinate rule of *The Biquaternion Algebra and Its Vector Spaces* with the cross terms deleted:

$$
\tilde Q_1\bullet\tilde Q_2=\bigl(Q_{1t}Q_{2t}-Q_{1x}Q_{2x}-Q_{1y}Q_{2y}-Q_{1z}Q_{2z}\bigr)
+\bigl(Q_{1t}Q_{2x}+Q_{1x}Q_{2t}\bigr)\vec e_x
+\bigl(Q_{1t}Q_{2y}+Q_{1y}Q_{2t}\bigr)\vec e_y
+\bigl(Q_{1t}Q_{2z}+Q_{1z}Q_{2t}\bigr)\vec e_z.
$$

The two forms are one rule, and each is used where it is shorter.

### Bilinearity and the Class

**Proposition.** The symmetric plain product is $\mathbb{C}$-**bilinear**:

$$
(\tilde Q_1+\tilde Q_3)\bullet\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_3\bullet\tilde Q_2,\qquad
\tilde Q_2\bullet(\tilde Q_1+\tilde Q_3)=\tilde Q_2\bullet\tilde Q_1+\tilde Q_2\bullet\tilde Q_3,\qquad
(A\tilde Q_1)\bullet\tilde Q_2=A(\tilde Q_1\bullet\tilde Q_2)=\tilde Q_1\bullet(A\tilde Q_2)
$$

for every $A\in\mathbb{C}$.

*Proof.* The plain product is $\mathbb{C}$-bilinear, and the sum of two $\mathbb{C}$-bilinear maps and the halving keep the class; equivalently, the displayed coordinate rule is additive and homogeneous in the coordinates of each argument separately.

**Remark (why the class survives the split).** The plain product has two $\mathbb{C}$-linear slots, so its two slots have the same type and the bare interchange of the arguments is an exchange that keeps the class; the two halves are $\mathbb{C}$-bilinear again. This is the **algebra case** of the general split, and it is contrasted in *The Symmetric and Antisymmetric Parts of an Algebra Product* with the case of a product one of whose slots is conjugate-linear, where the bare interchange returns a product of the opposite class and the exchange must be adapted. **The symmetric plain product is $\mathbb{C}$-bilinear, and the obstruction of the class does not arise in this block.**

## The Algebra the Symmetrisation Defines

### Commutativity

**Proposition.** The symmetric plain product is **commutative**:

$$
\boxed{\; \tilde Q_1\bullet\tilde Q_2=\tilde Q_2\bullet\tilde Q_1 \;}.
$$

*Proof.* The half-sum of the plain product and its exchange is unchanged when the two arguments are interchanged; equivalently, the scalar part is the symmetric bilinear form $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ and the vector part $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ is symmetric in the two elements.

Commutativity is the defining departure from the plain product, which is not commutative, since $\vec e_x \vec e_y=\vec e_z$ and $\vec e_y \vec e_x=-\vec e_z$. The commutator of the plain product is carried entirely by the antisymmetric part, $[\tilde Q_1,\tilde Q_2]=\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1=2(\vec Q_1\times\vec Q_2)$, which is the operation of the companion block *Introduction to the Antisymmetric Plain Algebra*.

### The Unit

**Proposition.** The element $e_t$ is a **two-sided identity** of the symmetric plain product:

$$
e_t\bullet\tilde Q=\tilde Q\bullet e_t=\tilde Q .
$$

*Proof.* $e_t$ is the identity of the plain product, so $\tfrac12(e_t\tilde Q+\tilde Qe_t)=\tfrac12(\tilde Q+\tilde Q)=\tilde Q$.

The identity is unique, and $e_t$ is the only element that serves, as it is for the plain product. The operation is therefore **unital**, and the unit is two-sided because the product is commutative.

**Remark (the only part with a unit).** Of the twelve operations of *Symmetric and Antisymmetric Decomposition of the Four General Products*, $\mathrm{SPA}$ is the only part — the only operation other than the four general products — that carries a unit, and both $\mathrm{APA}$ and the six parts of the other rows fail to have one. **The symmetric plain product is the unique two-sidedly unital operation of the eight parts of the twelve.**

### The Jordan Identity

**Definition.** A commutative product is a **Jordan product** when it satisfies the **Jordan identity**

$$
(x\bullet y)\bullet(x\bullet x)=x\bullet\bigl(y\bullet(x\bullet x)\bigr),
$$

and a commutative algebra with a Jordan product is a **Jordan algebra**. The identity is the one named in *The Symmetric and Antisymmetric Parts of an Algebra Product* and in *Jordan Algebras*.

**Theorem.** The symmetric plain product satisfies the Jordan identity: for all $\tilde Q_1,\tilde Q_2\in\mathbb{B}$,

$$
\boxed{\; (\tilde Q_1\bullet\tilde Q_2)\bullet(\tilde Q_1\bullet\tilde Q_1)=\tilde Q_1\bullet\bigl(\tilde Q_2\bullet(\tilde Q_1\bullet\tilde Q_1)\bigr) \;}.
$$

*Proof.* The symmetrisation of an associative product always satisfies the Jordan identity: for an associative algebra $A$, the algebra $A^{\bullet}$ with the product $\tfrac12(xy+yx)$ is the classical special Jordan algebra, and the identity is the theorem of *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*, that $A^{+}$ is a Jordan algebra, proved there by the direct expansion with the product $xy+yx$ (the halved product satisfies it as well, every coefficient being halved). Expanding both sides in the associative product of $\mathbb{B}$ and using its associativity verifies the identity directly.

**Remark (the identity is what singles out the block).** Of the four symmetric parts of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, exactly one satisfies the Jordan identity, and of the four antisymmetric parts exactly one satisfies the Jacobi identity; both sit in the plain row, $\mathrm{SPA}$ being the Jordan product and $\mathrm{APA}$ being the Lie product. Read without the restriction to the parts, the Jordan identity also holds at every element of the associative general plain product, at every element of the general quaternionic product, whose square is central, and vacuously for the two alternating antisymmetrisations, so the identity by itself does not isolate the block; the restriction to the parts of their kind is the corpus's convention and it is *The Specificities of the Symmetric Plain Algebra* that states the exact criterion, commutativity together with the Jordan identity. **Read with the product $\bullet$, the biquaternion space is a commutative unital Jordan algebra over $\mathbb{C}$**, and it is a *special* Jordan algebra, because it is the symmetrisation of an associative algebra. Its degree and its norm are *Norm and Invertibility in the Symmetric Plain Algebra*, its idempotents are *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and its nilpotents *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The relation of the associativity of the plain product to the Jordan identity is the general one: associativity implies both the Jacobi and the Jordan identities of the two halves, while neither identity implies the other, and the block is the instance of the Jordan side. The generic theory, with the two inadmissibility witnesses and the criterion read off the associator, is *The Symmetric and Antisymmetric Parts of an Algebra Product*.

### The Associativity of the Block

**Proposition.** The symmetric plain product is **not associative**.

*Proof.* The witness is the pair $\tilde Q_1=\tilde Q_2=\vec e_x$ read against $\tilde Q_3=\vec e_y$:

$$
(\vec e_x\bullet \vec e_x)\bullet \vec e_y=(-e_t)\bullet \vec e_y=-\vec e_y,\qquad
\vec e_x\bullet(\vec e_x\bullet \vec e_y)=\vec e_x\bullet 0=0,
$$

and the two values differ.

The failure is the reason the block is a Jordan algebra and not an associative one; the Jordan identity is the substitute for associativity that the symmetrisation keeps, and it is weaker, as the witness shows.

### The Sixteen Products of the Basis

The product is $\mathbb{C}$-bilinear, so it is fixed by its values on the sixteen pairs of basis elements.

**Proposition.** The products of the basis elements are

| $\bullet$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $0$ | $0$ |
| $\vec e_y$ | $\vec e_y$ | $0$ | $-e_t$ | $0$ |
| $\vec e_z$ | $\vec e_z$ | $0$ | $0$ | $-e_t$ |

*Proof.* Each entry is $\tfrac12(e_\mu e_\nu+e_\nu e_\mu)$ read from the multiplication table of *The Biquaternion Algebra and Its Vector Spaces*. For $\mu=\nu=t$ the entry is $e_t$; for $\mu=\nu=k$ it is $\vec e_k^2=-e_t$; for one index $t$ it is the other basis element, the unit acting trivially; and for two distinct vector indices the quaternion units anticommute, $\vec e_j \vec e_k=-\vec e_k \vec e_j$, so the two terms cancel and the entry is $0$. The table is symmetric, as commutativity requires, and its diagonal is $e_t,-e_t,-e_t,-e_t$.

**Remark (the table against the plain one).** The table of the block is the quaternion table of *The Biquaternion Algebra and Its Vector Spaces* with the six signed off-diagonal vector entries $\vec e_z,-\vec e_z,\vec e_y,-\vec e_y,\vec e_x,-\vec e_x$ replaced by $0$, and it keeps the diagonal $e_t,-e_t,-e_t,-e_t$ and the first row and column. **The two tables differ only where the plain product is skew, which is off the diagonal in the vector block.**

### The Square and Its Polarisation

**Proposition.** The square of an element in the block is the plain square,

$$
\tilde Q\bullet\tilde Q=\tilde Q^2=\bigl[Q_t^2-(\vec Q,\vec Q)\bigr]+2Q_t\vec Q,
$$

so the diagonal of $\bullet$ and the diagonal of the plain product agree.

*Proof.* $\tilde Q_2\bullet\tilde Q_2=\tfrac12(\tilde Q_2^2+\tilde Q_2^2)=\tilde Q_2^2$, and the plain square is the displayed form by the scalar–vector rule with $\tilde Q_1=\tilde Q_2$.

The square is the symmetric part of the plain square, and the antisymmetric part vanishes on the diagonal because it is alternating; this is the general fact that the antisymmetric part of a product has zero diagonal and the square carries the symmetric part alone.

**Proposition (polarisation).** The product off the diagonal is recovered from the square by polarisation:

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl((\tilde Q_1+\tilde Q_2)\bullet(\tilde Q_1+\tilde Q_2)-\tilde Q_1\bullet\tilde Q_1-\tilde Q_2\bullet\tilde Q_2\bigr).
$$

*Proof.* The product is $\mathbb{C}$-bilinear and commutative, so expanding the square of the sum gives $(\tilde Q_1+\tilde Q_2)\bullet(\tilde Q_1+\tilde Q_2)=\tilde Q_1\bullet\tilde Q_1+2\tilde Q_1\bullet\tilde Q_2+\tilde Q_2\bullet\tilde Q_2$, and the displayed identity follows by subtraction and halving.

So the square map $\tilde Q\mapsto\tilde Q\bullet\tilde Q$ determines the whole product, and the block is generated by its square and its linear structure. The square is the quadratic map whose study, with the norm, the idempotents and the nilpotents, is *Norm and Invertibility in the Symmetric Plain Algebra*, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the fuller theory is the Specific Theory article *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

## The Reconstruction and the Twelve

### The Reconstruction $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$

**Theorem.** The plain product is the sum of its two parts:

$$
\boxed{\; \tilde Q_1\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_1\wedge\tilde Q_2,\qquad
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr)=\vec Q_1\times\vec Q_2 \;},
$$

and the symmetric part is $\mathrm{SPA}$ and the antisymmetric part $\mathrm{APA}$.

*Proof.* Adding the two halves restores the product, and the antisymmetric half of the plain product is the cross product of the two vector parts, as *Introduction to the Antisymmetric Plain Algebra* develops. The identity is one of the four row reconstructions $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, $\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$, $\mathrm{GPS}=\mathrm{SPS}+\mathrm{APS}$, $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$ of *Symmetric and Antisymmetric Decomposition of the Four General Products*.

The two halves have opposite symmetry, so either determines the other from the product, and the pair is the unique such decomposition. The plain row is the one whose symmetric part is the Jordan product and whose antisymmetric part is the Lie product; the two companion blocks that read the halves are *Introduction to the Antisymmetric Plain Algebra* and the present one.

### The Placement among the Twelve

The name $\mathrm{SPA}$ is read with the code of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*: the first letter $\mathrm S$ says that the operation is the symmetric part of the row; the second letter $\mathrm P$ says that it comes from the plain product, whose first slot is read as it stands; and the third letter $\mathrm A$ says that it belongs to the family of algebras over $\mathbb{C}$, whose second slot is read as it stands.

| the row | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

**Remark (the place of the block).** The block $\mathrm{SPA}$ is the symmetrisation of the associative product $\mathrm{GPA}$, and the other seven parts are the symmetrisations and antisymmetrisations of the three further products. Two of the eight parts pass the identity of a classical nonassociative algebra, both in the plain row: $\mathrm{APA}$ is the Lie product and $\mathrm{SPA}$ the Jordan product. **Of the twelve operations, $\mathrm{SPA}$ is the one commutative unital Jordan product, and it is the only one of the four symmetric parts that satisfies the Jordan identity** — the four general products are neither symmetrisations nor antisymmetrisations, and the identity is not put to them, so the twelve reduce to the four symmetric parts for this identity and to the four antisymmetric parts for the Jacobi identity of the block $\mathrm{APA}$. The class of the operation is that of the plain product, $\mathbb{C}$-bilinear, the eight parts are described in *Symmetric and Antisymmetric Decomposition of the Four General Products*, which owns the laws, and named in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the order-symmetry reading is in *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

## Summary

The symmetric part of the general plain bilinear product of $\mathbb{B}$ is the operation

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr)
=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1,
$$

the plain product with the cross term dropped. It is $\mathbb{C}$-bilinear and commutative, $e_t$ is a two-sided unit, it satisfies the Jordan identity, and it is not associative, with the witness $(\vec e_x\bullet \vec e_x)\bullet \vec e_y=-\vec e_y$ against $\vec e_x\bullet(\vec e_x\bullet \vec e_y)=0$. Read with the product, the space is a commutative unital special Jordan algebra over $\mathbb{C}$, and it is the only part of the twelve operations that has a unit and the only one that is a Jordan product. The sixteen products of the basis are the quaternion table with the six off-diagonal vector entries set to $0$; the square is the plain square, $\tilde Q\bullet\tilde Q=Q_t^2-(\vec Q,\vec Q)+2Q_t\vec Q$, and the product is the polarisation of the square. The plain product reconstructs as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, the symmetrisation of an associative product in the plain row of *Symmetric and Antisymmetric Decomposition of the Four General Products*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | the symmetrised (Jordan) product, the multiplication of the block |
| $\mathbb{B}^{\bullet}$ | the biquaternion space with the symmetric plain product |
| $\mathrm{SPA}$ | the name of the operation among the twelve |
| $\tilde Q_1\wedge\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)=\vec Q_1\times\vec Q_2$ | the antisymmetric part, $\mathrm{APA}$ |
| $\tilde Q\bullet\tilde Q=\tilde Q^2$ | the square of the block = the plain square |
| $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ | the reconstruction of the plain product |
| $(\vec Q_1,\vec Q_2)$ | the complex bilinear dot product of the vector parts |

## Further Reading

- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the names, the laws and the table of the twelve operations.
- [The Symmetric and Antisymmetric Parts of an Algebra Product](the-symmetric-and-antisymmetric-parts-of-an-algebra-product.html), for the split, its uniqueness and the two admissibility conditions.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the same split read from the side of the order symmetry.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the product the block splits and its multiplication table.
- [Introduction to the Antisymmetric Plain Algebra](introduction-to-the-antisymmetric-plain-algebra.html), for the companion half, the cross product and the Lie structure.
- [Norm and Invertibility in the Symmetric Plain Algebra](norm-and-invertibility-in-the-symmetric-plain-algebra.html), [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.html) and [The Specificities of the Symmetric Plain Algebra](the-specificities-of-the-symmetric-plain-algebra.html), for the Common Theory of the block.
- [The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra](the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.html), [The Trace Form and the Invariance of the Symmetric Plain Algebra](the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra.html), *Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions*, [The Multiplication Operators of the Symmetric Plain Algebra](the-multiplication-operators-of-the-symmetric-plain-algebra.html), [Introduction to the Symmetric Plain Algebra](introduction-to-the-symmetric-plain-algebra.html), for the remainder of the block.
