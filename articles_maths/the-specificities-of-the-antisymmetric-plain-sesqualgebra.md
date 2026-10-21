# __The Specificities of the Antisymmetric Plain Sesqualgebra__

## Introduction

The antisymmetric plain sesquilinear product

$$
\tilde Q_1\diamond\tilde Q_2=\operatorname{Vect}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}
$$

is **conjugate-alternating**, vector valued and without a unit, and it fails the Jacobi identity (*Introduction to the Antisymmetric Plain Sesqualgebra*, *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*). As an element-theoretic object the block is poor: the origin is its only idempotent, it has no root of $-1$ or of $+1$, no unit and no inverse, every nonzero element is a zero divisor, and its nilpotents are a thin cone inside them. As an **operator-theoretic** object it has one sharp feature, and the feature is the whole of the present article.

The feature is the action of the ambient unit on the right. For the block,

$$
R^{\diamond}_{e_t}\tilde Q_1=\tilde Q_1\diamond e_t=\operatorname{Vect}\tilde Q_1,
\qquad
L^{\diamond}_{e_t}\tilde Q_1=e_t\diamond\tilde Q_1=-\overline{\operatorname{Vect}\tilde Q_1},
$$

so the right multiplication by $e_t$ is the **projection onto the vector subspace** along the centre. The block is the **only** one of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* in which some element multiplies on the right as that projection, and the element is necessarily $e_t$. Equivalently, the block is the only one in which the canonical splitting

$$
\mathbb{B}=\operatorname{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}
$$

is realised by the multiplication on the right by a single element, the element being the unit of the ambient algebra, which is not a unit of the block. The criterion is stated as the identity $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$, it is proved equivalent to the projector classification $R^{\diamond}_{\tilde Q_1}{}^{2}=R^{\diamond}_{\tilde Q_1}\Leftrightarrow\tilde Q_1\in\{0,e_t\}$, and it isolates the block among the twelve. The model is *The Specificities of the Biquaternion Algebra*, which states left alternativity as its criterion; the twins are *The Specificities of the General Quaternionic Algebra*, *The Specificities of the Symmetric Quaternionic Algebra* and *The Specificities of the Symmetric Plain Algebra*.

## Placement

The article is the closing entry of the block, after the introduction, the vector part of the square and the Jacobi failure, the remarkable subspaces, the sesquilinear pairing, the adjoint operators and the two matrix models. It uses the operation and its image of *Introduction to the Antisymmetric Plain Sesqualgebra*, the operator layer of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, the $2\times2$ model of *Introduction to the Symmetric Plain Sesqualgebra*, the classification of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and the products of *The 12 Products of the Biquaternion Complex Space*. It reads back, as consequences of one identity, the element theory of the five Common Theory articles of the block: *Norm and Invertibility in the Antisymmetric Plain Sesqualgebra*, *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*, *Idempotents of the Antisymmetric Plain Sesqualgebra* and *Nilpotents of the Antisymmetric Plain Sesqualgebra*.

## Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x\vec e_y=\vec e_z$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$; an element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The **plain product** is written by juxtaposition $\tilde Q_1\tilde Q_2$ and the parent sesquilinear product $\tilde Q_1\tilde Q_2^{*}$; a product written $\star$ is a generic one and its identity is stated at each use, and $\diamond$ is the product of the block. The conjugations are the natural conjugation ${}^{\natural}$, $\tilde Q^{\natural}=Q_t-\vec Q$, the coefficientwise conjugations $\bar{\cdot}$ and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; the **left** and the **right multiplication** of a product $\star$ by $\tilde Q_1$ are the maps

$$
L^{\star}_{\tilde Q_1}:\tilde Q_2\mapsto\tilde Q_1\star\tilde Q_2,
\qquad
R^{\star}_{\tilde Q_1}:\tilde Q_2\mapsto\tilde Q_2\star\tilde Q_1,
$$

and the superscript is dropped for the product in force. The **projection onto the vector subspace** is $P_{\operatorname{Vect}}$, the map $\tilde Q_1\mapsto\operatorname{Vect}\tilde Q_1$ removing the scalar part, and the **projection onto the centre** is $P_{\mathbb{C}_{\mathbb{B}}}$, the map $\tilde Q_1\mapsto\operatorname{Sc}(\tilde Q_1)e_t$ keeping it. The centre is $\mathbb{C}_{\mathbb{B}}$, the vector subspace is $\operatorname{Vect}(\mathbb{B})$, and the two meet at the origin. The **twelve** are $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Governing Identity

The criterion is an identity between two operators on the space, one attached to the product and one to the splitting.

**Definition (the splitting realised on the right).** A product $\star$ on $\mathbb{B}$ **realises the splitting on the right** when

$$
R^{\star}_{e_t}=P_{\operatorname{Vect}},
\qquad\text{that is}\qquad
\tilde Q_1\star e_t=\operatorname{Vect}\tilde Q_1\quad\text{for every }\tilde Q_1 .
$$

**Theorem (the identity of the block).** The product of the block realises the splitting on the right,

$$
R^{\diamond}_{e_t}\tilde Q_1=\tilde Q_1\diamond e_t=\operatorname{Vect}\bigl(\tilde Q_1e_t^{*}\bigr)=\operatorname{Vect}\tilde Q_1 ,
$$

and the left multiplication by $e_t$ is the conjugate of the projection,

$$
L^{\diamond}_{e_t}\tilde Q_1=e_t\diamond\tilde Q_1=\operatorname{Vect}\bigl(e_t\tilde Q_1^{*}\bigr)=\operatorname{Vect}\tilde Q_1^{*}=-\overline{\operatorname{Vect}\tilde Q_1}.
$$

*Proof.* The product is $\tilde Q_1\diamond\tilde Q_2=\operatorname{Vect}(\tilde Q_1\tilde Q_2^{*})$ and $e_t^{*}=e_t$ is the unit of the plain product, so $\tilde Q_1e_t^{*}=\tilde Q_1$ and $\operatorname{Vect}(\tilde Q_1)=\operatorname{Vect}\tilde Q_1$; the left side is $e_t\tilde Q_1^{*}=\tilde Q_1^{*}$, and $\operatorname{Vect}(\tilde Q_1^{*})=-\overline{\operatorname{Vect}\tilde Q_1}$ because the vector part carries the coefficientwise conjugation with the signs $\varepsilon=(1,-1,-1,-1)$ and the natural conjugation.

The two displays say the same thing twice: **the splitting is visible to the right multiplication and conjugate-visible to the left one.** The right multiplication by the ambient unit is the projection, so its image is the vector subspace and its kernel is the centre; the left multiplication is the projection followed by the coefficientwise conjugation, so its image is the *conjugate* vector subspace, which is the same space, and its kernel is again the centre.

**Remark (the element is forced).** The identity names the element: it is the right multiplication of $e_t$, and the isolation of §*The Isolation among the Twelve* shows that no other element of the twelve structures has $P_{\operatorname{Vect}}$ for its right multiplication. At $\tilde Q_2=e_t$ the identity reads $e_t\star e_t=0$, which every antisymmetrisation satisfies, so the forcing is not visible at the origin alone; it is the search over all the elements that settles it.

## The Projector Classification

The identity $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$ says that one particular right multiplication is a projector. The classification of all of them is the operator form of the criterion.

**Theorem (the projectors of the right multiplications).** For the block the right multiplication $R^{\diamond}_{\tilde Q_1}$ is an idempotent operator,

$$
R^{\diamond}_{\tilde Q_1}\circ R^{\diamond}_{\tilde Q_1}=R^{\diamond}_{\tilde Q_1},
$$

if and only if $\tilde Q_1\in\{0,e_t\}$. The projector $R^{\diamond}_{e_t}$ is the projection onto the vector subspace and $R^{\diamond}_{0}$ is the zero operator.

*Proof.* Pass to the $2\times2$ model of *Introduction to the Symmetric Plain Sesqualgebra*, in which $R^{\diamond}_{\tilde Q_1}$ is the map $Y\mapsto\operatorname{traceless}(YX^{\dagger})$ on the matrices $Y=\mathsf{M}_2(\tilde Q_2)$. Write $\pi(M)=M-\tfrac12\operatorname{Tr}(M)I$ for the traceless part, $B=X^{\dagger}$, and $D=\pi(YB)=\mathsf{M}_2(R^{\diamond}_{\tilde Q_1}\tilde Q_2)$. Then $R^{\diamond}_{\tilde Q_1}(D)=\pi(DB)$, and, $D$ being traceless, the identity $R^{2}=R$ is the equation
$$
\pi(DB)-D=\pi\bigl(D(B-I)\bigr)=0
$$
for every $Y$.

If $B$ is invertible, the map $Y\mapsto\pi(YB)$ is onto the traceless matrices, so $\pi(W(B-I))=0$ for every traceless $W$. Taking $W=\operatorname{diag}(1,-1)$ forces $B-I$ to be diagonal with opposite diagonal entries, and then $W=E_{12}$ forces the surviving entry to vanish; hence $B-I=0$, that is $\tilde Q_1=e_t$.

If $B$ is singular, either $B=0$, for which $R^{\diamond}_{\tilde Q_1}=0$ and the identity holds, or $B$ has rank one, $B=uw^{\dagger}$ with nonzero vectors $u,w$. Then $YB=(Yu)w^{\dagger}=zw^{\dagger}$ with $z=Yu$, and, with $c=w^{\dagger}u$, the equation $\pi(D(B-I))=0$ becomes
$$
\pi(D(B-I))=\bigl((c-1)z-\tfrac12(w^{\dagger}z)u\bigr)w^{\dagger}-\tfrac12\bigl(\tfrac{c}{2}-1\bigr)(w^{\dagger}z)I=0 .
$$
Choosing $Y$ with $w^{\dagger}z=0$ and $z\neq0$ gives $(c-1)zw^{\dagger}=0$, so $c=1$; choosing then $z=w$ makes the left member $\tfrac12(w^{\dagger}w)\bigl(\tfrac12 I-B\bigr)$, which vanishes only if $B=\tfrac12I$, impossible for a matrix of rank one. So no rank-one $B$ works, and the only singular solution is $B=0$.

So the identity holds exactly when $B\in\{0,I\}$, that is $\tilde Q_1\in\{0,e_t\}$; for $\tilde Q_1=e_t$ the operator is $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$ and for $\tilde Q_1=0$ it is $R^{\diamond}_{0}=0$, both idempotent.

**Corollary (no other projector realises the splitting).** The projection onto the vector subspace is a right multiplication of the block for the element $e_t$ and for no other element, and the projection onto the centre is not a right multiplication of the block at all.

*Proof.* If $R^{\diamond}_{\tilde Q_1}=P_{\operatorname{Vect}}$ then it is a projector, so $\tilde Q_1\in\{0,e_t\}$ by the theorem, and $R^{\diamond}_{0}=0\neq P_{\operatorname{Vect}}$, leaving $\tilde Q_1=e_t$. If instead $R^{\diamond}_{\tilde Q_1}=P_{\mathbb{C}_{\mathbb{B}}}$, the projection onto the centre, then this operator is a projector too, so again $\tilde Q_1\in\{0,e_t\}$, and neither $R^{\diamond}_{0}=0$ nor $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$ is the projection onto the centre.

The criterion is therefore an **operator criterion**: the splitting is realised on the right, and the projector that realises it is unique.

## The Isolation among the Twelve

The criterion is tested on each of the twelve structures by computing the right multiplication by the ambient unit.

**Theorem (the block is the only one).** Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, $\mathrm{APS}$ is the only one for which $R^{\star}_{e_t}=P_{\operatorname{Vect}}$; and it is the only one in which any element has right multiplication equal to $P_{\operatorname{Vect}}$.

*Proof.* The table computes $R^{\star}_{e_t}$ family by family. For the second statement: if $R^{\star}_{\tilde Q_1}=P_{\operatorname{Vect}}$ then the operator is a projector, and the projector classification of §*The Projector Classification* leaves the two elements $0$ and $e_t$, of which only $e_t$ gives $P_{\operatorname{Vect}}$.

| the action of $R^{\star}_{e_t}$ | the structures |
|---|---|
| the identity | GPA, SPA, GPS |
| the natural conjugation | GQA, GQS, SQS |
| the projection onto the centre | SQA, SPS |
| the zero operator | APA, AQS |
| minus the projection onto the vector subspace | AQA |
| **the projection onto the vector subspace** | **APS** |

The rows are the three operations that generate the twelve. The general products and their symmetric parts act by the identity, by the natural conjugation or by the projection onto the centre; the antisymmetric parts act by zero or by plus or minus the projection onto the vector subspace, because the antisymmetrisation kills the scalar part of the value; and the block is the row in which the sign is $+1$ and no conjugation is applied. The block alone carries the conjugation in the second slot **and** the antisymmetrisation, so that $\tilde Q_1\diamond e_t=\operatorname{Vect}(\tilde Q_1e_t^{*})=\operatorname{Vect}\tilde Q_1$ retains the vector part of $\tilde Q_1$; this is the exact meaning of the trailing $\mathrm S$ of the code.

## The Other Criteria Fail Here

The criteria of the twin articles are not the criterion of the block, and the block fails them all.

**Remark (the four criteria).** Left alternativity, the criterion of *The Specificities of the Biquaternion Algebra*, fails in the block, and its failure is the Jacobi failure of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; the block is left- and right-non-alternative. The left form $L_{e_t}=P_{\operatorname{Vect}}$, the criterion the antisymmetric quaternionic algebra carries in *Introduction to the Antisymmetric Quaternionic Algebra*, fails in the block, whose left multiplication by $e_t$ is $-\overline{\cdot}\circ P_{\operatorname{Vect}}$ and whose right multiplication is $P_{\operatorname{Vect}}$: **the block realises the splitting on the right where the antisymmetric quaternionic algebra realises it on the left.** The criterion of the general quaternionic algebra, the conjugated index of its left multiplications, is absent; and the criterion of the symmetric quaternionic algebra, the projector classification of the symmetric product, is absent. Each of the four criteria isolates one structure, and no structure carries two of them.

**Remark (the companion law).** The block carries a second law, and it is not unique. The product is **conjugate-alternating**,

$$
\tilde Q_2\diamond\tilde Q_1=-\overline{\tilde Q_1\diamond\tilde Q_2},
$$

and of the twelve structures exactly two are conjugate-alternating, the block and the quaternionic sesquilinear antisymmetrisation $\mathrm{AQS}=\vec Q_1\times\overline{\vec Q_2}$. The law isolates the pair and not the block, and the criterion $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$ separates the pair: $\mathrm{AQS}$ has $R^{\mathrm{AQS}}_{e_t}=0$ while the block has $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$. **The distinction between the two conjugate-alternating structures is exactly the nonvanishing of the square**: the diagonal of the block, $\tilde Q_1\diamond\tilde Q_1=\operatorname{Vect}(\tilde Q_1\tilde Q_1^{*})$, is the Hermitian square and is generally nonzero, while the diagonal of $\mathrm{AQS}$, $\vec Q_1\times\overline{\vec Q_1}$, vanishes on the elements whose two real parts are linearly dependent. This is the reading of the root of $0$ in *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*.

## What the Criterion Delivers

The identity $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$, with the projector classification it carries, organises the element theory of the block. Four of its six features are consequences of the projection, and two come with it from the same two structural facts, that every value is a pure vector and that the second slot is conjugate-linear.

- **No unit.** A right unit $\tilde u$ would have $R^{\diamond}_{\tilde u}$ the identity, and the identity is a projector; by the projector classification the projectors of the right multiplications are $R^{\diamond}_{0}$ and $R^{\diamond}_{e_t}$ alone, so $\tilde u\in\{0,e_t\}$, and neither is a unit: $0$ multiplies by zero and $e_t\diamond\tilde Q_1=-\overline{\operatorname{Vect}\tilde Q_1}\neq\tilde Q_1$. The absence is stated with the two one-sided actions (*Norm and Invertibility in the Antisymmetric Plain Sesqualgebra*).
- **No inverse.** The inverse is defined relative to a two-sided unit, and there is none; the group of units is void.
- **One idempotent.** The idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is solved by the parity, not by the projection: an idempotent is a pure vector, and the diagonal of a pure vector is $-\vec p\times\overline{\vec p}$, purely imaginary, so the equation has the origin alone for its solution (*Idempotents of the Antisymmetric Plain Sesqualgebra*). The projection explains why the element calculus has no other ingredient to offer here: the projector $R^{\diamond}_{e_t}$ is not the multiplication of an idempotent.
- **No root of $-1$ or $+1$.** Every value is a pure vector, being the image of the projection; the diagonal is a value, so it has zero scalar part, while $\pm e_t$ is central with scalar part $\pm1$ (*Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*).
- **Thin nilpotents.** The diagonal is $\tilde Q_1\diamond\tilde Q_1=\operatorname{Vect}(\tilde Q_1\tilde Q_1^{*})$, the Hermitian square read through the projection, and it vanishes on the cone over the real unit sphere; the index of the block is two (*Nilpotents of the Antisymmetric Plain Sesqualgebra*).
- **Every nonzero element a zero divisor.** The equation $\tilde Q_1\diamond\tilde Q_2=0$ asks for $\tilde Q_1\tilde Q_2^{*}\in\mathbb{C}_{\mathbb{B}}$, and the projection makes the central membership attainable from every nonzero $\tilde Q_1$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*).

## The Boundary of the Criterion

The criterion is sharp and it has one neighbour on each side.

**The antisymmetric quaternionic algebra.** $\mathrm{AQA}$ realises the splitting by its left multiplication, $L^{\mathrm{AQA}}_{e_t}=P_{\operatorname{Vect}}$, and by its right multiplication it acts by $-P_{\operatorname{Vect}}$; it is the left twin of the block, and its operator layer is *Introduction to the Antisymmetric Quaternionic Algebra* together with *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, the article of its own specificities being outside the register of the present menu. The block is the right twin, and the two together say that the splitting $\mathbb{B}=\operatorname{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$ is realised by a single element in exactly two of the twelve structures, on opposite sides.

**The conjugate-commutative structures.** $\mathrm{SPS}$ and $\mathrm{SQS}$ are conjugate-commutative, and their right multiplication by $e_t$ is the projection onto the centre for $\mathrm{SPS}$ and the natural conjugation for $\mathrm{SQS}$; the projection onto the vector subspace, which is the image of the block, and the projection onto the centre, which is the image of the symmetric plain sesquilinear product, are the two projections the pair realises, on opposite subspaces. The two are the extreme rows of the splitting: **the antisymmetrisation keeps the vector part and loses the scalar part, and the symmetrisation does the converse.**

**The open question.** Whether the identity $R^{\star}_{\tilde Q_1}=P_{\operatorname{Vect}}$ for some element $\tilde Q_1$ of one of the other eleven can occur after a rescaling of the product, or after a change of basis that does not preserve the involution, is a question of the classification of the twelve and is left to the author. In the basis and the products as fixed, the answer is no, and the isolation of §*The Isolation among the Twelve* is the evidence.

## Summary

The block is the product $\tilde Q_1\diamond\tilde Q_2=\operatorname{Vect}(\tilde Q_1\tilde Q_2^{*})$, conjugate-alternating, vector valued and without a unit, and its one sharp operator property is the identity

$$
R^{\diamond}_{e_t}=P_{\operatorname{Vect}},
\qquad
\tilde Q_1\diamond e_t=\operatorname{Vect}\tilde Q_1,
$$

the right multiplication by the ambient unit is the projection onto the vector subspace along the centre, while the left multiplication is its conjugate. Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* the block is the only one that realises the splitting $\mathbb{B}=\operatorname{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$ on the right by a single element, and no other structure has any element whose right multiplication is $P_{\operatorname{Vect}}$; $\mathrm{AQA}$ realises the splitting on the left and is the twin.

The identity is equivalent to the projector classification of the block: a right multiplication is a projector exactly for the elements $0$ and $e_t$, the second being the projection onto the vector subspace and the first the zero operator. The companion law, conjugate-alternation, isolates the block together with $\mathrm{AQS}$, and the projection criterion separates the pair. Each Common Theory article of the block — the absence of the unit and the inverse, the unique idempotent, the absent roots of $\pm1$, the thin nilpotents and the full zero-divisor set — is a consequence of the one identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\star$, $\diamond$ | a generic product and the product of the block |
| $L^{\star}_{\tilde Q_1}$, $R^{\star}_{\tilde Q_1}$ | the left and the right multiplication by $\tilde Q_1$ |
| $P_{\operatorname{Vect}}$ | the projection onto the vector subspace along the centre |
| $P_{\mathbb{C}_{\mathbb{B}}}$ | the projection onto the centre along the vector subspace |
| $R^{\diamond}_{e_t}=P_{\operatorname{Vect}}$ | the criterion, the splitting realised on the right |
| $L^{\diamond}_{e_t}=-\overline{\cdot}\circ P_{\operatorname{Vect}}$ | the left multiplication by the ambient unit |
| $\tilde Q_2\diamond\tilde Q_1=-\overline{\tilde Q_1\diamond\tilde Q_2}$ | the companion law, conjugate-alternation |
| $\mathrm{APS}$, $\mathrm{AQS}$, $\mathrm{AQA}$ | the block, its conjugate-alternating sibling and its left twin |

## Further Reading

- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html), for the twelve structures and their laws, units and images.
- [Introduction to the Antisymmetric Plain Sesqualgebra](introduction-to-the-antisymmetric-plain-sesqualgebra.html), for the product, its image and its two one-sided actions.
- [The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra](the-adjoint-operators-and-the-sandwich-of-the-antisymmetric-plain-sesqualgebra.html), for the left and right multiplications of the block.
- [Introduction to the Symmetric Plain Sesqualgebra](introduction-to-the-symmetric-plain-sesqualgebra.html), for the model in which the projector classification is proved.
- [The Specificities of the Biquaternion Algebra](the-specificities-of-the-biquaternion-algebra.html), for the model of a specificities article, and [Introduction to the Antisymmetric Quaternionic Algebra](introduction-to-the-antisymmetric-quaternionic-algebra.html), for the left twin.
- [The Symmetric and Antisymmetric Parts of a Sesqualgebra Product](the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.html), for the conjugate exchange behind the split.
