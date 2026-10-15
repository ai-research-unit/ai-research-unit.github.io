# __The Specificities of the Antisymmetric Plain Sesqualgebra__

## Introduction

The antisymmetric plain sesquilinear product

$$
\tilde P\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)=-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q}
$$

is **conjugate-alternating**, vector valued and without a unit, and it fails the Jacobi identity (*Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*, *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*). As an element-theoretic object the block is poor: the origin is its only idempotent, it has no root of $-1$ or of $+1$, no unit and no inverse, every nonzero element is a zero divisor, and its nilpotents are a thin cone inside them. As an **operator-theoretic** object it has one sharp feature, and the feature is the whole of the present article.

The feature is the action of the ambient unit on the right. For the block,

$$
R^{\diamond}_{e_0}\tilde X=\tilde X\diamond e_0=\operatorname{Vect}\tilde X,
\qquad
L^{\diamond}_{e_0}\tilde X=e_0\diamond\tilde X=-\overline{\operatorname{Vect}\tilde X},
$$

so the right multiplication by $e_0$ is the **projection onto the vector subspace** along the centre. The block is the **only** one of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* in which some element multiplies on the right as that projection, and the element is necessarily $e_0$. Equivalently, the block is the only one in which the canonical splitting

$$
\mathbb{B}=\operatorname{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}
$$

is realised by the multiplication on the right by a single element, the element being the unit of the ambient algebra, which is not a unit of the block. The criterion is stated as the identity $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$, it is proved equivalent to the projector classification $R^{\diamond}_{\tilde X}{}^{2}=R^{\diamond}_{\tilde X}\Leftrightarrow\tilde X\in\{0,e_0\}$, and it isolates the block among the twelve. The model is *The Specificities of the General Plain Algebra*, which states left alternativity as its criterion; the twins are *The Specificities of the General Quaternionic Algebra*, *The Specificities of the Symmetric Quaternionic Algebra* and *The Specificities of the Symmetric Plain Algebra*.

## Placement

The article is the closing entry of the block, after the introduction, the vector part of the square and the Jacobi failure, the remarkable subspaces, the sesquilinear pairing, the adjoint operators and the two matrix models. It uses the operation and its image of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*, the operator layer of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, the $2\times2$ model of *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, the classification of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and the products of *The 12 Products of the Biquaternion Complex Space*. It reads back, as consequences of one identity, the element theory of the five Common Theory articles of the block: *Norm and Invertibility in the Antisymmetric Plain Sesqualgebra*, *Zero Divisors of the Antisymmetric Plain Sesqualgebra*, *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*, *Idempotents of the Antisymmetric Plain Sesqualgebra* and *Nilpotents of the Antisymmetric Plain Sesqualgebra*.

## Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$; an element is $\tilde Q=Q_0e_0+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_ke_k$. The **plain product** is written by juxtaposition $\tilde P\tilde Q$ and the parent sesquilinear product $\tilde P\tilde Q^{*}$; a product written $\star$ is a generic one and its identity is stated at each use, and $\diamond$ is the product of the block. The conjugations are the natural conjugation ${}^{\natural}$, $\tilde Q^{\natural}=Q_0-\vec Q$, the coefficientwise conjugations $\bar{\cdot}$ and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; the **left** and the **right multiplication** of a product $\star$ by $\tilde X$ are the maps

$$
L^{\star}_{\tilde X}:\tilde Y\mapsto\tilde X\star\tilde Y,
\qquad
R^{\star}_{\tilde X}:\tilde Y\mapsto\tilde Y\star\tilde X,
$$

and the superscript is dropped for the product in force. The **projection onto the vector subspace** is $P_{\operatorname{Vect}}$, the map $\tilde X\mapsto\operatorname{Vect}\tilde X$ removing the scalar part, and the **projection onto the centre** is $P_{\mathbb{C}_{\mathbb{B}}}$, the map $\tilde X\mapsto\operatorname{Sc}(\tilde X)e_0$ keeping it. The centre is $\mathbb{C}_{\mathbb{B}}$, the vector subspace is $\operatorname{Vect}(\mathbb{B})$, and the two meet at the origin. The **twelve** are $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Governing Identity

The criterion is an identity between two operators on the space, one attached to the product and one to the splitting.

**Definition (the splitting realised on the right).** A product $\star$ on $\mathbb{B}$ **realises the splitting on the right** when

$$
R^{\star}_{e_0}=P_{\operatorname{Vect}},
\qquad\text{that is}\qquad
\tilde X\star e_0=\operatorname{Vect}\tilde X\quad\text{for every }\tilde X .
$$

**Theorem (the identity of the block).** The product of the block realises the splitting on the right,

$$
R^{\diamond}_{e_0}\tilde X=\tilde X\diamond e_0=\operatorname{Vect}\bigl(\tilde Xe_0^{*}\bigr)=\operatorname{Vect}\tilde X ,
$$

and the left multiplication by $e_0$ is the conjugate of the projection,

$$
L^{\diamond}_{e_0}\tilde X=e_0\diamond\tilde X=\operatorname{Vect}\bigl(e_0\tilde X^{*}\bigr)=\operatorname{Vect}\tilde X^{*}=-\overline{\operatorname{Vect}\tilde X}.
$$

*Proof.* The product is $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ and $e_0^{*}=e_0$ is the unit of the plain product, so $\tilde Xe_0^{*}=\tilde X$ and $\operatorname{Vect}(\tilde X)=\operatorname{Vect}\tilde X$; the left side is $e_0\tilde X^{*}=\tilde X^{*}$, and $\operatorname{Vect}(\tilde X^{*})=-\overline{\operatorname{Vect}\tilde X}$ because the vector part carries the coefficientwise conjugation with the signs $\varepsilon=(1,-1,-1,-1)$ and the natural conjugation.

The two displays say the same thing twice: **the splitting is visible to the right multiplication and conjugate-visible to the left one.** The right multiplication by the ambient unit is the projection, so its image is the vector subspace and its kernel is the centre; the left multiplication is the projection followed by the coefficientwise conjugation, so its image is the *conjugate* vector subspace, which is the same space, and its kernel is again the centre.

**Remark (the element is forced).** The identity names the element: it is the right multiplication of $e_0$, and the isolation of §*The Isolation among the Twelve* shows that no other element of the twelve structures has $P_{\operatorname{Vect}}$ for its right multiplication. At $\tilde Y=e_0$ the identity reads $e_0\star e_0=0$, which every antisymmetrisation satisfies, so the forcing is not visible at the origin alone; it is the search over all the elements that settles it.

## The Projector Classification

The identity $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$ says that one particular right multiplication is a projector. The classification of all of them is the operator form of the criterion.

**Theorem (the projectors of the right multiplications).** For the block the right multiplication $R^{\diamond}_{\tilde X}$ is an idempotent operator,

$$
R^{\diamond}_{\tilde X}\circ R^{\diamond}_{\tilde X}=R^{\diamond}_{\tilde X},
$$

if and only if $\tilde X\in\{0,e_0\}$. The projector $R^{\diamond}_{e_0}$ is the projection onto the vector subspace and $R^{\diamond}_{0}$ is the zero operator.

*Proof.* Pass to the $2\times2$ model of *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, in which $R^{\diamond}_{\tilde X}$ is the map $Y\mapsto\operatorname{traceless}(YX^{\dagger})$ on the matrices $Y=\mathsf{M}_2(\tilde Y)$. Write $\pi(M)=M-\tfrac12\operatorname{Tr}(M)I$ for the traceless part, $B=X^{\dagger}$, and $D=\pi(YB)=\mathsf{M}_2(R^{\diamond}_{\tilde X}\tilde Y)$. Then $R^{\diamond}_{\tilde X}(D)=\pi(DB)$, and, $D$ being traceless, the identity $R^{2}=R$ is the equation
$$
\pi(DB)-D=\pi\bigl(D(B-I)\bigr)=0
$$
for every $Y$.

If $B$ is invertible, the map $Y\mapsto\pi(YB)$ is onto the traceless matrices, so $\pi(W(B-I))=0$ for every traceless $W$. Taking $W=\operatorname{diag}(1,-1)$ forces $B-I$ to be diagonal with opposite diagonal entries, and then $W=E_{12}$ forces the surviving entry to vanish; hence $B-I=0$, that is $X=e_0$.

If $B$ is singular, either $B=0$, for which $R^{\diamond}_{\tilde X}=0$ and the identity holds, or $B$ has rank one, $B=uw^{\dagger}$ with nonzero vectors $u,w$. Then $YB=(Yu)w^{\dagger}=zw^{\dagger}$ with $z=Yu$, and, with $c=w^{\dagger}u$, the equation $\pi(D(B-I))=0$ becomes
$$
\pi(D(B-I))=\bigl((c-1)z-\tfrac12(w^{\dagger}z)u\bigr)w^{\dagger}-\tfrac12\bigl(\tfrac{c}{2}-1\bigr)(w^{\dagger}z)I=0 .
$$
Choosing $Y$ with $w^{\dagger}z=0$ and $z\neq0$ gives $(c-1)zw^{\dagger}=0$, so $c=1$; choosing then $z=w$ makes the left member $\tfrac12(w^{\dagger}w)\bigl(\tfrac12 I-B\bigr)$, which vanishes only if $B=\tfrac12I$, impossible for a matrix of rank one. So no rank-one $B$ works, and the only singular solution is $B=0$.

So the identity holds exactly when $B\in\{0,I\}$, that is $X\in\{0,e_0\}$; for $X=e_0$ the operator is $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$ and for $X=0$ it is $R^{\diamond}_{0}=0$, both idempotent.

**Corollary (no other projector realises the splitting).** The projection onto the vector subspace is a right multiplication of the block for the element $e_0$ and for no other element, and the projection onto the centre is not a right multiplication of the block at all.

*Proof.* If $R^{\diamond}_{\tilde X}=P_{\operatorname{Vect}}$ then it is a projector, so $\tilde X\in\{0,e_0\}$ by the theorem, and $R^{\diamond}_{0}=0\neq P_{\operatorname{Vect}}$, leaving $\tilde X=e_0$. If instead $R^{\diamond}_{\tilde X}=P_{\mathbb{C}_{\mathbb{B}}}$, the projection onto the centre, then this operator is a projector too, so again $\tilde X\in\{0,e_0\}$, and neither $R^{\diamond}_{0}=0$ nor $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$ is the projection onto the centre.

The criterion is therefore an **operator criterion**: the splitting is realised on the right, and the projector that realises it is unique.

## The Isolation among the Twelve

The criterion is tested on each of the twelve structures by computing the right multiplication by the ambient unit.

**Theorem (the block is the only one).** Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, $\mathrm{APS}$ is the only one for which $R^{\star}_{e_0}=P_{\operatorname{Vect}}$; and it is the only one in which any element has right multiplication equal to $P_{\operatorname{Vect}}$.

*Proof.* The table computes $R^{\star}_{e_0}$ family by family. For the second statement: if $R^{\star}_{\tilde X}=P_{\operatorname{Vect}}$ then the operator is a projector, and the projector classification of §*The Projector Classification* leaves the two elements $0$ and $e_0$, of which only $e_0$ gives $P_{\operatorname{Vect}}$.

| the action of $R^{\star}_{e_0}$ | the structures |
|---|---|
| the identity | GPA, SPA, GPS |
| the natural conjugation | GQA, GQS, SQS |
| the projection onto the centre | SQA, SPS |
| the zero operator | APA, AQS |
| minus the projection onto the vector subspace | AQA |
| **the projection onto the vector subspace** | **APS** |

The rows are the three operations that generate the twelve. The general products and their symmetric parts act by the identity, by the natural conjugation or by the projection onto the centre; the antisymmetric parts act by zero or by plus or minus the projection onto the vector subspace, because the antisymmetrisation kills the scalar part of the value; and the block is the row in which the sign is $+1$ and no conjugation is applied. The block alone carries the conjugation in the second slot **and** the antisymmetrisation, so that $\tilde X\diamond e_0=\operatorname{Vect}(\tilde Xe_0^{*})=\operatorname{Vect}\tilde X$ retains the vector part of $\tilde X$; this is the exact meaning of the trailing $\mathrm S$ of the code.

## The Other Criteria Fail Here

The criteria of the twin articles are not the criterion of the block, and the block fails them all.

**Remark (the four criteria).** Left alternativity, the criterion of *The Specificities of the General Plain Algebra*, fails in the block, and its failure is the Jacobi failure of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; the block is left- and right-non-alternative. The left form $L_{e_0}=P_{\operatorname{Vect}}$, the criterion the antisymmetric quaternionic algebra carries in *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*, fails in the block, whose left multiplication by $e_0$ is $-\overline{\cdot}\circ P_{\operatorname{Vect}}$ and whose right multiplication is $P_{\operatorname{Vect}}$: **the block realises the splitting on the right where the antisymmetric quaternionic algebra realises it on the left.** The criterion of the general quaternionic algebra, the conjugated index of its left multiplications, is absent; and the criterion of the symmetric quaternionic algebra, the projector classification of the symmetric product, is absent. Each of the four criteria isolates one structure, and no structure carries two of them.

**Remark (the companion law).** The block carries a second law, and it is not unique. The product is **conjugate-alternating**,

$$
\tilde Q\diamond\tilde P=-\overline{\tilde P\diamond\tilde Q},
$$

and of the twelve structures exactly two are conjugate-alternating, the block and the quaternionic sesquilinear antisymmetrisation $\mathrm{AQS}=\vec P\times\overline{\vec Q}$. The law isolates the pair and not the block, and the criterion $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$ separates the pair: $\mathrm{AQS}$ has $R^{\mathrm{AQS}}_{e_0}=0$ while the block has $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$. **The distinction between the two conjugate-alternating structures is exactly the nonvanishing of the square**: the diagonal of the block, $\tilde X\diamond\tilde X=\operatorname{Vect}(\tilde X\tilde X^{*})$, is the Hermitian square and is generally nonzero, while the diagonal of $\mathrm{AQS}$, $\vec X\times\overline{\vec X}$, vanishes on the elements whose two real parts are linearly dependent. This is the reading of the root of $0$ in *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*.

## What the Criterion Delivers

The identity $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$, with the projector classification it carries, organises the element theory of the block. Four of its six features are consequences of the projection, and two come with it from the same two structural facts, that every value is a pure vector and that the second slot is conjugate-linear.

- **No unit.** A right unit $\tilde u$ would have $R^{\diamond}_{\tilde u}$ the identity, and the identity is a projector; by the projector classification the projectors of the right multiplications are $R^{\diamond}_{0}$ and $R^{\diamond}_{e_0}$ alone, so $\tilde u\in\{0,e_0\}$, and neither is a unit: $0$ multiplies by zero and $e_0\diamond\tilde X=-\overline{\operatorname{Vect}\tilde X}\neq\tilde X$. The absence is stated with the two one-sided actions (*Norm and Invertibility in the Antisymmetric Plain Sesqualgebra*).
- **No inverse.** The inverse is defined relative to a two-sided unit, and there is none; the group of units is void.
- **One idempotent.** The idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is solved by the parity, not by the projection: an idempotent is a pure vector, and the diagonal of a pure vector is $-\vec p\times\overline{\vec p}$, purely imaginary, so the equation has the origin alone for its solution (*Idempotents of the Antisymmetric Plain Sesqualgebra*). The projection explains why the element calculus has no other ingredient to offer here: the projector $R^{\diamond}_{e_0}$ is not the multiplication of an idempotent.
- **No root of $-1$ or $+1$.** Every value is a pure vector, being the image of the projection; the diagonal is a value, so it has zero scalar part, while $\pm e_0$ is central with scalar part $\pm1$ (*Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*).
- **Thin nilpotents.** The diagonal is $\tilde X\diamond\tilde X=\operatorname{Vect}(\tilde X\tilde X^{*})$, the Hermitian square read through the projection, and it vanishes on the cone over the real unit sphere; the index of the block is two (*Nilpotents of the Antisymmetric Plain Sesqualgebra*).
- **Every nonzero element a zero divisor.** The equation $\tilde X\diamond\tilde Y=0$ asks for $\tilde X\tilde Y^{*}\in\mathbb{C}_{\mathbb{B}}$, and the projection makes the central membership attainable from every nonzero $\tilde X$ (*Zero Divisors of the Antisymmetric Plain Sesqualgebra*).

## The Boundary of the Criterion

The criterion is sharp and it has one neighbour on each side.

**The antisymmetric quaternionic algebra.** $\mathrm{AQA}$ realises the splitting by its left multiplication, $L^{\mathrm{AQA}}_{e_0}=P_{\operatorname{Vect}}$, and by its right multiplication it acts by $-P_{\operatorname{Vect}}$; it is the left twin of the block, and its operator layer is *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* together with *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, the article of its own specificities being outside the register of the present menu. The block is the right twin, and the two together say that the splitting $\mathbb{B}=\operatorname{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$ is realised by a single element in exactly two of the twelve structures, on opposite sides.

**The conjugate-commutative structures.** $\mathrm{SPS}$ and $\mathrm{SQS}$ are conjugate-commutative, and their right multiplication by $e_0$ is the projection onto the centre for $\mathrm{SPS}$ and the natural conjugation for $\mathrm{SQS}$; the projection onto the vector subspace, which is the image of the block, and the projection onto the centre, which is the image of the symmetric plain sesquilinear product, are the two projections the pair realises, on opposite subspaces. The two are the extreme rows of the splitting: **the antisymmetrisation keeps the vector part and loses the scalar part, and the symmetrisation does the converse.**

**The open question.** Whether the identity $R^{\star}_{\tilde X}=P_{\operatorname{Vect}}$ for some element $\tilde X$ of one of the other eleven can occur after a rescaling of the product, or after a change of basis that does not preserve the involution, is a question of the classification of the twelve and is left to the author. In the basis and the products as fixed, the answer is no, and the isolation of §*The Isolation among the Twelve* is the evidence.

## Summary

The block is the product $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$, conjugate-alternating, vector valued and without a unit, and its one sharp operator property is the identity

$$
R^{\diamond}_{e_0}=P_{\operatorname{Vect}},
\qquad
\tilde X\diamond e_0=\operatorname{Vect}\tilde X,
$$

the right multiplication by the ambient unit is the projection onto the vector subspace along the centre, while the left multiplication is its conjugate. Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* the block is the only one that realises the splitting $\mathbb{B}=\operatorname{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$ on the right by a single element, and no other structure has any element whose right multiplication is $P_{\operatorname{Vect}}$; $\mathrm{AQA}$ realises the splitting on the left and is the twin.

The identity is equivalent to the projector classification of the block: a right multiplication is a projector exactly for the elements $0$ and $e_0$, the second being the projection onto the vector subspace and the first the zero operator. The companion law, conjugate-alternation, isolates the block together with $\mathrm{AQS}$, and the projection criterion separates the pair. Each Common Theory article of the block — the absence of the unit and the inverse, the unique idempotent, the absent roots of $\pm1$, the thin nilpotents and the full zero-divisor set — is a consequence of the one identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\star$, $\diamond$ | a generic product and the product of the block |
| $L^{\star}_{\tilde X}$, $R^{\star}_{\tilde X}$ | the left and the right multiplication by $\tilde X$ |
| $P_{\operatorname{Vect}}$ | the projection onto the vector subspace along the centre |
| $P_{\mathbb{C}_{\mathbb{B}}}$ | the projection onto the centre along the vector subspace |
| $R^{\diamond}_{e_0}=P_{\operatorname{Vect}}$ | the criterion, the splitting realised on the right |
| $L^{\diamond}_{e_0}=-\overline{\cdot}\circ P_{\operatorname{Vect}}$ | the left multiplication by the ambient unit |
| $\tilde Q\diamond\tilde P=-\overline{\tilde P\diamond\tilde Q}$ | the companion law, conjugate-alternation |
| $\mathrm{APS}$, $\mathrm{AQS}$, $\mathrm{AQA}$ | the block, its conjugate-alternating sibling and its left twin |

## Further Reading

- *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve structures and their laws, units and images.
- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its image and its two one-sided actions.
- *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-adjoint-operators-and-the-sandwich-of-the-antisymmetric-plain-sesqualgebra.md`), for the left and right multiplications of the block.
- *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model in which the projector classification is proved.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the model of a specificities article, and *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the left twin.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the conjugate exchange behind the split.
