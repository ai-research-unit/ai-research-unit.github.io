# __Introduction to the Symmetric Plain Algebra of Biquaternions__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries the general plain bilinear product $\tilde P\tilde Q$, the multiplication of *Introduction to the General Plain Algebra of Biquaternions*. Its exchange of the two arguments splits it into a symmetric and an antisymmetric part, and each of the two parts is again a $\mathbb{C}$-bilinear product of the space. This article reads the **symmetric part** as a multiplication in its own right:

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)
=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}.
$$

The operation is the plain product with the cross term dropped, and the space it makes of $\mathbb{B}$ is a commutative unital Jordan algebra over $\mathbb{C}$. The reading is one of the twelve operations of *The 12 Products of the Biquaternion Complex Space*, where the operation is named $\mathrm{SPA}$ and is one of the two members of the twelve that satisfies the identity of a classical nonassociative algebra.

The split that produces the operation, its two projections and the two admissibility conditions are *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the order-symmetry reading of the same split, with the worked examples on the four general products, is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. This article owns the operation as a multiplication: the rule, the class, the laws, the sixteen products of the basis, the square and its polarisation, the reconstruction, and the placement of the block among the twelve. The algebra it builds is read further in five companions of the block: *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, *The Trace Form and the Invariance of the Symmetric Plain Algebra*, *Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions*, *The Multiplication Operators of the Symmetric Plain Algebra* and *The Symmetric Plain Algebra in the $2\times2$ and $4\times4$ Matrix Element Representations*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, central scalar imaginary $i$ and $e_1e_2=e_3$, so that $e_1^2=e_2^2=e_3^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. A generic element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$; $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ is the complex bilinear dot product of the vector parts. The product $\tilde P\tilde Q$ is the general plain bilinear one throughout. The inner product $(\cdot,\cdot)$ and the general plain product are as in *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *The Four Pairings of the Biquaternion Algebra*; the remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Introduction to the Remarkable Subspaces*.

## The Symmetrisation of the Plain Product

### The Rule

**Definition.** The **symmetric plain product** of two biquaternions is

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr).
$$

It is the **symmetrisation** of the general plain bilinear product $\tilde P\tilde Q$, the operation called the symmetric part of the product in *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the operation named $\mathrm{SPA}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The space $\mathbb{B}$ with the product $\bullet$ is written $\mathbb{B}^{\bullet}$ and is the **symmetric plain algebra** of the block.

The rule needs no more than the plain product, and *The Symmetric and Antisymmetric Parts of an Algebra Product* proves that the split is canonical: if a product is written as a sum of a symmetric and an antisymmetric operation, the two are forced to be the two halves. The symmetric half is therefore fixed by the plain product alone and not by a choice of notation.

### The Coordinate and Scalar–Vector Forms

The plain product reads, in the scalar–vector form of *Introduction to the General Plain Algebra of Biquaternions*,

$$
\tilde P\tilde Q=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q},
$$

and its exchange $\tilde Q\tilde P$ differs from it only in the sign of the cross term. Adding the two and halving gives the rule that names the block:

$$
\tilde P\bullet\tilde Q=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}.
$$

**Remark (the cross term is what the symmetrisation removes).** The scalar part $P_0Q_0-(\mathbf{P},\mathbf{Q})$ is symmetric by itself, since $(\mathbf{P},\mathbf{Q})=(\mathbf{Q},\mathbf{P})$, and the mixed vector part $P_0\mathbf{Q}+Q_0\mathbf{P}$ is symmetric as well; the only asymmetric piece of the plain product is the cross product $\mathbf{P}\times\mathbf{Q}$, which changes sign under the exchange. **The symmetric plain product is therefore exactly the plain product with the cross term dropped**, and the vector part of the value is $P_0\mathbf{Q}+Q_0\mathbf{P}$.

Read on the coordinates, the same rule is the plain coordinate rule of *Introduction to the General Plain Algebra of Biquaternions* with the cross terms deleted:

$$
\tilde P\bullet\tilde Q=\bigl(P_0Q_0-P_1Q_1-P_2Q_2-P_3Q_3\bigr)
+\bigl(P_0Q_1+P_1Q_0\bigr)e_1
+\bigl(P_0Q_2+P_2Q_0\bigr)e_2
+\bigl(P_0Q_3+P_3Q_0\bigr)e_3.
$$

The two forms are one rule, and each is used where it is shorter.

### Bilinearity and the Class

**Proposition.** The symmetric plain product is $\mathbb{C}$-**bilinear**:

$$
(\tilde P+\tilde R)\bullet\tilde Q=\tilde P\bullet\tilde Q+\tilde R\bullet\tilde Q,\qquad
\tilde Q\bullet(\tilde P+\tilde R)=\tilde Q\bullet\tilde P+\tilde Q\bullet\tilde R,\qquad
(A\tilde P)\bullet\tilde Q=A(\tilde P\bullet\tilde Q)=\tilde P\bullet(A\tilde Q)
$$

for every $A\in\mathbb{C}$.

*Proof.* The plain product is $\mathbb{C}$-bilinear, and the sum of two $\mathbb{C}$-bilinear maps and the halving keep the class; equivalently, the displayed coordinate rule is additive and homogeneous in the coordinates of each argument separately. Verified on the coordinate rule.

**Remark (why the class survives the split).** The plain product has two $\mathbb{C}$-linear slots, so its two slots have the same type and the bare interchange of the arguments is an exchange that keeps the class; the two halves are $\mathbb{C}$-bilinear again. This is the **algebra case** of the general split, and it is contrasted in *The Symmetric and Antisymmetric Parts of an Algebra Product* with the case of a product one of whose slots is conjugate-linear, where the bare interchange returns a product of the opposite class and the exchange must be adapted. **The symmetric plain product is $\mathbb{C}$-bilinear, and the obstruction of the class does not arise in this block.**

## The Algebra the Symmetrisation Defines

### Commutativity

**Proposition.** The symmetric plain product is **commutative**:

$$
\tilde P\bullet\tilde Q=\tilde Q\bullet\tilde P .
$$

*Proof.* The half-sum of the plain product and its exchange is unchanged when the two arguments are interchanged; equivalently, the scalar part is the symmetric bilinear form $P_0Q_0-(\mathbf{P},\mathbf{Q})$ and the vector part $P_0\mathbf{Q}+Q_0\mathbf{P}$ is symmetric in the two elements. Verified on the coordinate rule.

Commutativity is the defining departure from the plain product, which is not commutative, since $e_1e_2=e_3$ and $e_2e_1=-e_3$. The commutator of the plain product is carried entirely by the antisymmetric part, $[\tilde P,\tilde Q]=\tilde P\tilde Q-\tilde Q\tilde P=2(\mathbf{P}\times\mathbf{Q})$, which is the operation of the companion block *Introduction to the Antisymmetric Plain Algebra of Biquaternions*.

### The Unit

**Proposition.** The element $e_0$ is a **two-sided identity** of the symmetric plain product:

$$
e_0\bullet\tilde Q=\tilde Q\bullet e_0=\tilde Q .
$$

*Proof.* $e_0$ is the identity of the plain product, so $\tfrac12(e_0\tilde Q+\tilde Qe_0)=\tfrac12(\tilde Q+\tilde Q)=\tilde Q$. Verified on the coordinate rule.

The identity is unique, and $e_0$ is the only element that serves, as it is for the plain product. The operation is therefore **unital**, and the unit is two-sided because the product is commutative.

**Remark (the only part with a unit).** Of the twelve operations of *The 12 Products of the Biquaternion Complex Space*, $\mathrm{SPA}$ is the only part — the only operation other than the four general products — that carries a unit, and both $\mathrm{APA}$ and the six parts of the other rows fail to have one. **The symmetric plain product is the unique two-sidedly unital operation of the eight parts of the twelve.**

### The Jordan Identity

**Definition.** A commutative product is a **Jordan product** when it satisfies the **Jordan identity**

$$
(x\bullet y)\bullet(x\bullet x)=x\bullet\bigl(y\bullet(x\bullet x)\bigr),
$$

and a commutative algebra with a Jordan product is a **Jordan algebra**. The identity is the one named in *The Symmetric and Antisymmetric Parts of an Algebra Product* and in *Jordan Algebras*.

**Theorem.** The symmetric plain product satisfies the Jordan identity: for all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
(\tilde P\bullet\tilde Q)\bullet(\tilde P\bullet\tilde P)=\tilde P\bullet\bigl(\tilde Q\bullet(\tilde P\bullet\tilde P)\bigr).
$$

*Proof.* The symmetrisation of an associative product always satisfies the Jordan identity: for an associative algebra $A$, the algebra $A^{\bullet}$ with the product $\tfrac12(xy+yx)$ is the classical special Jordan algebra, and the identity is the theorem of *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*, that $A^{+}$ is a Jordan algebra, proved there by the direct expansion with the product $xy+yx$ (the halved product satisfies it as well, every coefficient being halved). Expanding both sides in the associative product of $\mathbb{B}$ and using its associativity verifies the identity directly. The identity was recomputed on the coordinate rule of this block and checked on random pairs.

**Remark (the identity is what singles out the block).** Of the twelve operations of *The 12 Products of the Biquaternion Complex Space*, exactly one satisfies the Jordan identity and exactly one satisfies the Jacobi identity, and both sit in the plain row: $\mathrm{SPA}$ is the Jordan product and $\mathrm{APA}$ is the Lie product. The other six parts fail the identity of their kind. **Read with the product $\bullet$, the biquaternion space is a commutative unital Jordan algebra over $\mathbb{C}$**, and it is a *special* Jordan algebra, because it is the symmetrisation of an associative algebra. Its degree, its idempotents, its inverse and its norm are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

The relation of the associativity of the plain product to the Jordan identity is the general one: associativity implies both the Jacobi and the Jordan identities of the two halves, while neither identity implies the other, and the block is the instance of the Jordan side. The generic theory, with the two inadmissibility witnesses and the criterion read off the associator, is *The Symmetric and Antisymmetric Parts of an Algebra Product*.

### The Associativity of the Block

**Proposition.** The symmetric plain product is **not associative**.

*Proof.* The witness is the pair $\tilde P=\tilde Q=e_1$ read against $\tilde R=e_2$:

$$
(e_1\bullet e_1)\bullet e_2=(-e_0)\bullet e_2=-e_2,\qquad
e_1\bullet(e_1\bullet e_2)=e_1\bullet 0=0,
$$

and the two values differ. Verified on the basis.

The failure is the reason the block is a Jordan algebra and not an associative one; the Jordan identity is the substitute for associativity that the symmetrisation keeps, and it is weaker, as the witness shows.

### The Sixteen Products of the Basis

The product is $\mathbb{C}$-bilinear, so it is fixed by its values on the sixteen pairs of basis elements.

**Proposition.** The products of the basis elements are

| $\bullet$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $0$ | $0$ |
| $e_2$ | $e_2$ | $0$ | $-e_0$ | $0$ |
| $e_3$ | $e_3$ | $0$ | $0$ | $-e_0$ |

*Proof.* Each entry is $\tfrac12(e_\mu e_\nu+e_\nu e_\mu)$ read from the multiplication table of *Introduction to the General Plain Algebra of Biquaternions*. For $\mu=\nu=0$ the entry is $e_0$; for $\mu=\nu=k$ it is $e_k^2=-e_0$; for one index $0$ it is the other basis element, the unit acting trivially; and for two distinct vector indices the quaternion units anticommute, $e_je_k=-e_ke_j$, so the two terms cancel and the entry is $0$. The table is symmetric, as commutativity requires, and its diagonal is $e_0,-e_0,-e_0,-e_0$. Verified on the table.

**Remark (the table against the plain one).** The table of the block is the quaternion table of *Introduction to the General Plain Algebra of Biquaternions* with the six signed off-diagonal vector entries $e_3,-e_3,e_2,-e_2,e_1,-e_1$ replaced by $0$, and it keeps the diagonal $e_0,-e_0,-e_0,-e_0$ and the first row and column. **The two tables differ only where the plain product is skew, which is off the diagonal in the vector block.**

### The Square and Its Polarisation

**Proposition.** The square of an element in the block is the plain square,

$$
\tilde Q\bullet\tilde Q=\tilde Q^2=\bigl[Q_0^2-(\mathbf{Q},\mathbf{Q})\bigr]+2Q_0\mathbf{Q},
$$

so the diagonal of $\bullet$ and the diagonal of the plain product agree.

*Proof.* $\tilde Q\bullet\tilde Q=\tfrac12(\tilde Q^2+\tilde Q^2)=\tilde Q^2$, and the plain square is the displayed form by the scalar–vector rule with $\tilde P=\tilde Q$. Verified on the coordinate rule.

The square is the symmetric part of the plain square, and the antisymmetric part vanishes on the diagonal because it is alternating; this is the general fact that the antisymmetric part of a product has zero diagonal and the square carries the symmetric part alone.

**Proposition (polarisation).** The product off the diagonal is recovered from the square by polarisation:

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl((\tilde P+\tilde Q)\bullet(\tilde P+\tilde Q)-\tilde P\bullet\tilde P-\tilde Q\bullet\tilde Q\bigr).
$$

*Proof.* The product is $\mathbb{C}$-bilinear and commutative, so expanding the square of the sum gives $(\tilde P+\tilde Q)\bullet(\tilde P+\tilde Q)=\tilde P\bullet\tilde P+2\tilde P\bullet\tilde Q+\tilde Q\bullet\tilde Q$, and the displayed identity follows by subtraction and halving. Verified on the coordinate rule.

So the square map $\tilde Q\mapsto\tilde Q\bullet\tilde Q$ determines the whole product, and the block is generated by its square and its linear structure. The square is the quadratic map whose study, with the idempotents and the norm, is *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

## The Reconstruction and the Twelve

### The Reconstruction $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$

**Theorem.** The plain product is the sum of its two parts:

$$
\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q,\qquad
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$

and the symmetric part is $\mathrm{SPA}$ and the antisymmetric part $\mathrm{APA}$.

*Proof.* Adding the two halves restores the product, and the antisymmetric half of the plain product is the cross product of the two vector parts, as *Introduction to the Antisymmetric Plain Algebra of Biquaternions* develops. The identity is one of the four row reconstructions $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, $\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$, $\mathrm{GPS}=\mathrm{SPS}+\mathrm{APS}$, $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$ of *The 12 Products of the Biquaternion Complex Space*. Verified on the coordinate rule.

The two halves have opposite symmetry, so either determines the other from the product, and the pair is the unique such decomposition. The plain row is the one whose symmetric part is the Jordan product and whose antisymmetric part is the Lie product; the two companion blocks that read the halves are *Introduction to the Antisymmetric Plain Algebra of Biquaternions* and the present one.

### The Placement among the Twelve

The name $\mathrm{SPA}$ is read with the code of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*: the first letter $\mathrm S$ says that the operation is the symmetric part of the row; the second letter $\mathrm P$ says that it comes from the plain product, whose first slot is read as it stands; and the third letter $\mathrm A$ says that it belongs to the family of algebras over $\mathbb{C}$, whose second slot is read as it stands.

| the row | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

**Remark (the place of the block).** The block $\mathrm{SPA}$ is the symmetrisation of the associative product $\mathrm{GPA}$, and the other seven parts are the symmetrisations and antisymmetrisations of the three further products. Two of the eight parts pass the identity of a classical nonassociative algebra, both in the plain row: $\mathrm{APA}$ is the Lie product and $\mathrm{SPA}$ the Jordan product. **Of the twelve operations, $\mathrm{SPA}$ is the one commutative unital Jordan product, and it is the only one of the four symmetric parts that satisfies the Jordan identity** — the four general products are neither symmetrisations nor antisymmetrisations, and the identity is not put to them, so the twelve reduce to the four symmetric parts for this identity and to the four antisymmetric parts for the Jacobi identity of the block $\mathrm{APA}$. The class of the operation is that of the plain product, $\mathbb{C}$-bilinear, the eight parts are described in *The 12 Products of the Biquaternion Complex Space*, which owns the laws, and named in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the order-symmetry reading is in *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

## Summary

The symmetric part of the general plain bilinear product of $\mathbb{B}$ is the operation

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)
=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P},
$$

the plain product with the cross term dropped. It is $\mathbb{C}$-bilinear and commutative, $e_0$ is a two-sided unit, it satisfies the Jordan identity, and it is not associative, with the witness $(e_1\bullet e_1)\bullet e_2=-e_2$ against $e_1\bullet(e_1\bullet e_2)=0$. Read with the product, the space is a commutative unital special Jordan algebra over $\mathbb{C}$, and it is the only part of the twelve operations that has a unit and the only one that is a Jordan product. The sixteen products of the basis are the quaternion table with the six off-diagonal vector entries set to $0$; the square is the plain square, $\tilde Q\bullet\tilde Q=Q_0^2-(\mathbf{Q},\mathbf{Q})+2Q_0\mathbf{Q}$, and the product is the polarisation of the square. The plain product reconstructs as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, the symmetrisation of an associative product in the plain row of *The 12 Products of the Biquaternion Complex Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | the symmetrised (Jordan) product, the multiplication of the block |
| $\mathbb{B}^{\bullet}$ | the biquaternion space with the symmetric plain product |
| $\mathrm{SPA}$ | the name of the operation among the twelve |
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | the antisymmetric part, $\mathrm{APA}$ |
| $\tilde Q\bullet\tilde Q=\tilde Q^2$ | the square of the block = the plain square |
| $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ | the reconstruction of the plain product |
| $(\mathbf{P},\mathbf{Q})$ | the complex bilinear dot product of the vector parts |

## Further Reading

- *The 12 Products of the Biquaternion Complex Space*, for the names, the laws and the table of the twelve operations.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the split, its uniqueness and the two admissibility conditions.
- *The 12 Products of the Biquaternion Complex Space*, for the same split read from the side of the order symmetry.
- *Introduction to the General Plain Algebra of Biquaternions*, for the product the block splits and its multiplication table.
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, for the companion half, the cross product and the Lie structure.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, *The Trace Form and the Invariance of the Symmetric Plain Algebra*, *Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions*, *The Multiplication Operators of the Symmetric Plain Algebra* and *The Symmetric Plain Algebra in the $2\times2$ and $4\times4$ Matrix Element Representations*, for the remainder of the block.
