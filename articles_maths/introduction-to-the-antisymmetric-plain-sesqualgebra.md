# __Introduction to the Antisymmetric Plain Sesqualgebra__

## Introduction

The general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ splits into two halves, and the split is the **adapted** one of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*: the exchange is not the bare interchange of the two arguments but the interchange followed by the coefficientwise conjugation of the value, and its two parts are the conjugate-symmetric half $\mathrm{SPS}(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})e_t$ and the **skew-conjugate-symmetric** half developed here,

$$
\tilde Q_1\diamond\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)
=\mathrm{Vect}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)
=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} .
$$

The first half is *Introduction to the Symmetric Plain Sesqualgebra*; the two together reconstruct the product, $\tilde Q_1\tilde Q_2^{*}=\mathrm{SPS}(\tilde Q_1,\tilde Q_2)+\tilde Q_1\diamond\tilde Q_2$, and this article introduces the second. It is the **antisymmetric plain sesqualgebra** (APS) of the block: the antisymmetric part of the general plain sesquilinear product under the conjugate transpose.

The insertion of the conjugation into the exchange changes the whole vocabulary. A bilinear antisymmetrisation is *alternating*, it vanishes on the diagonal, and for such an operation the exchange of the arguments alone reverses the sign. Here the conjugation is part of the operation, and the symmetry that survives is the **conjugate-alternation**

$$
\tilde Q_1\diamond\tilde Q_2=-\overline{\tilde Q_2\diamond\tilde Q_1},
$$

a statement about the two arguments and the coefficientwise conjugate of the value at once, and not the alternating sign of the bilinear rows. The diagonal is consequently **not** zero: it is the vector part of the square of the row, $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$, which is $2i\vec e_z$ at the element $\vec e_x+i\vec e_y$. The operation is therefore neither alternating nor anti-commutative; it is conjugate-alternating, and this article fixes that vocabulary before anything else.

Three boundaries are stated at once. The product that is split, its two-sided operators and its two models are *Introduction to the General Plain Sesqualgebra*, *The Left and Right Multiplications of the Biquaternioid Sesqualgebra* and the two articles *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* and *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*, and none of the three is repeated here. The product itself, the four general products as a family and the row table are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *Comparison Between the Four General Products*. The general construction of the parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and its long development, with the conjugation, the projections and the structure constants, is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*; both are cited and not restated. The **other** antisymmetrisation of the same product, the sesquilinear commutator of *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternioid*, is the half of the **bare** interchange and is a different operation; §*The Adapted Exchange* of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* sets the two side by side, and the exact defect between them is computed in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, below in this block.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the unit, $\vec e_k^2=-e_t$, and central scalar imaginary $i$; a general element is $\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=\sum_{k\in\{x,y,z\}}Q_k\vec e_k$ and $\overline{\vec Q}$ the coefficientwise conjugate of the vector part. The natural conjugation ${}^{\natural}$ negates the vector part, the coefficientwise conjugation $\bar{\cdot}$ conjugates the coefficients, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, with coordinates $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$. The dot and cross products of vector parts are the complex bilinear ones of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the Hermitian form is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ of *Introduction to the Remarkable Subspaces*. Throughout, $\diamond$ is the operation of this block.

## The Operation

### The Definition and the Coordinate Rule

**Definition.** The **antisymmetric plain sesqualgebra** is the operation

$$
\diamond\;:\;\mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{B},\qquad
(\tilde Q_1,\tilde Q_2)\longmapsto \tilde Q_1\diamond\tilde Q_2=\mathrm{Vect}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr),
$$

the vector part of the general plain sesquilinear product. Equivalently, it is the **skew-conjugate-symmetric part** of that product under the exchange $\tilde Q_1\tilde Q_2^{*}\mapsto\overline{\tilde Q_2\tilde Q_1^{*}}$,

$$
\tilde Q_1\diamond\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr),
$$

which is the general definition of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Two Parts Under Their Own Names*, read on the biquaternion product with the conjugation $\bar{\cdot}$.

The equivalence of the two displays is the definition of the vector part. Indeed $\overline{\tilde Q_2\tilde Q_1^{*}}=(\tilde Q_1\tilde Q_2^{*})^{\natural}$ for the biquaternion product, since $\natural(\overline{\tilde Q_3})=\tilde Q_3^{*}$ and $\natural$ is an anti-automorphism, so that $\tfrac12\bigl(\tilde Q_3-\tilde Q_3^{\natural}\bigr)=\mathrm{Vect}(\tilde Q_3)$ at $\tilde Q_3=\tilde Q_1\tilde Q_2^{*}$. That identity is the reason the two sesqualgebra rows of the row table admit the exchange *read on the value*: the conjugate transpose of the value is the natural conjugate of the same value, and the two halves of the same element fall out.

Written on the coordinates, collecting the scalar and the vector parts and conjugating the second one,

$$
\tilde Q_1\diamond\tilde Q_2=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2},
$$

so the scalar part vanishes identically, $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$, and the vector part is the antisymmetrisation of the scalar–vector formula of the product. The first two terms mix the scalar parts with the vector parts, and the last is the cross product of the vector part of the first argument with the conjugate of the vector part of the second.

### The Class

**Proposition.** The operation $\diamond$ is additive in each variable and **sesquilinear** over $(\mathbb{C},\bar{\cdot})$: $\mathbb{C}$-linear in the first argument and conjugate-linear in the second,

$$
(\lambda\tilde Q_1)\diamond\tilde Q_2=\lambda\,(\tilde Q_1\diamond\tilde Q_2),\qquad
\tilde Q_1\diamond(\lambda \tilde Q_2)=\overline{\lambda}\,(\tilde Q_1\diamond\tilde Q_2)\qquad(\lambda\in\mathbb{C}).
$$

*Proof.* The values lie in the vector subspace and the two rules are the two scalar rules of the sesquilinear product read through the vector part: $\mathrm{Vect}(\lambda\tilde Q_1\,\tilde Q_2^{*})=\lambda\,\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$ and $\mathrm{Vect}(\tilde Q_1(\lambda\tilde Q_2)^{*})=\mathrm{Vect}(\overline{\lambda}\,\tilde Q_1\tilde Q_2^{*})=\overline{\lambda}\,\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$.

**Remark.** The operation therefore belongs to the same class as the product it splits, and not to the class of the six $\mathbb{C}$-bilinear parts of the two algebra rows. In the row table of *The 12 Products of the Biquaternion Complex Space* it is the entry $\mathrm{APS}$, in the plain sesqualgebra row, between $\mathrm{GPS}$ and $\mathrm{SPS}$. The distinction is the one the two rows of the table exhibit: the six operations of the algebra rows are $\mathbb{C}$-bilinear, the six of the sesqualgebra rows are sesquilinear over $(\mathbb{C},\bar{\cdot})$, and the count twelve is the count over the complex space alone.

### Conjugate-Alternation

**Theorem (the operation is conjugate-alternating).** For all biquaternions,

$$
\tilde Q_1\diamond\tilde Q_2=-\overline{\tilde Q_2\diamond\tilde Q_1}.
$$

*Proof.* $\tilde Q_1\diamond\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)$ and $\tilde Q_2\diamond\tilde Q_1=\tfrac12\bigl(\tilde Q_2\tilde Q_1^{*}-\overline{\tilde Q_1\tilde Q_2^{*}}\bigr)$; conjugating the second and negating, $-\overline{\tilde Q_2\diamond\tilde Q_1}=\tfrac12\bigl(\overline{\tilde Q_2\tilde Q_1^{*}}-\tilde Q_1\tilde Q_2^{*}\bigr)=\tilde Q_1\diamond\tilde Q_2$.

**Remark (the vocabulary).** Three words have to be separated, because the operation satisfies none of the bilinear ones. It is **not alternating**, since its diagonal is not zero; it is **not anti-commutative**, since $\tilde Q_1\diamond\tilde Q_2\ne-\tilde Q_2\diamond\tilde Q_1$ off the real part; and it is **not a Lie bracket**, since the cyclic sum fails at the triple $(e_t,\vec e_x,\vec e_y)$ of the next section. It is conjugate-alternating and nothing else, and what replaces the vanishing diagonal is not a sign but the conjugation: the diagonal is **purely imaginary**, $\tilde Q\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde Q}$, and the pair of statements that the exchange yields is $\tilde Q_1\diamond\tilde Q_2=-\overline{\tilde Q_2\diamond\tilde Q_1}$ and $\overline{\tilde Q_1\diamond\tilde Q_2}=\overline{\tilde Q}_1\diamond\overline{\tilde Q}_2$.

**Proposition (the coefficientwise conjugation is an automorphism).** For all biquaternions,

$$
\overline{\tilde Q_1\diamond\tilde Q_2}=\overline{\tilde Q}_1\diamond\overline{\tilde Q}_2.
$$

*Proof.* $\overline{\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})}=\mathrm{Vect}(\overline{\tilde Q_1\tilde Q_2^{*}})=\mathrm{Vect}(\overline{\tilde Q}_1\,\overline{\tilde Q_2^{*}})$ and $\overline{\tilde Q^{*}}=\tilde Q^{\natural}$, so the value is $\mathrm{Vect}(\overline{\tilde Q}_1\,\tilde Q_2^{\natural})=(\overline{\tilde Q}_1)\diamond(\overline{\tilde Q}_2)$, since $(\overline{\tilde Q})^{*}=\tilde Q^{\natural}$.

**Remark.** The proposition is the conjugation-symmetry of the block, and it is the reason the block is stable under the conjugation of the space: the conjugation is a conjugate-linear automorphism of $\diamond$, in the same way that the interchange is an automorphism of a commutative product and its negative one of a Lie product. It is also the shape the exchange takes in this row, and it is what makes the two halves $\mathrm{SPS}$ and $\diamond$ read the same value $\tilde Q_1\tilde Q_2^{*}$ through the two conjugations ${}^{\natural}$ and $\bar{\cdot}$.

## The Image and the Absence of a Unit

**Proposition (the image is the vector subspace; the centre is not in it).** The image of $\diamond$ is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three over $\mathbb{C}$; the operation is central-free, so no value lies in the centre $\mathbb{C}_{\mathbb{B}}$ except $0$. The two one-sided actions of the unit are

$$
\tilde Q_1\diamond e_t=\vec Q_1,\qquad e_t\diamond\tilde Q=-\overline{\vec Q} .
$$

*Proof.* Every value is a vector part, so the image is contained in $\mathrm{Vect}(\mathbb{B})$. The first display gives the whole vector subspace, since $\vec Q_1$ is an arbitrary vector part, and it is the computation of $\mathrm{Vect}(\tilde Q_1 e_t^{*})=\mathrm{Vect}(\tilde Q_1)$. The second is $\mathrm{Vect}(\tilde Q^{*})=\mathrm{Vect}(-\overline{\vec Q})=-\overline{\vec Q}$. The scalar part vanishing with a nonzero vector part is not central, and the zero value is central.

**Remark (the unit is not a unit of the block).** The sesqualgebra has a unit on the right alone, by *Introduction to the General Plain Sesqualgebra*, and the block inherits neither side. A left unit $\tilde u$ would give $\tilde u\diamond e_t=e_t$, but $\tilde u\diamond e_t=\vec q$ has zero scalar part while $e_t$ has scalar part $1$: no left unit. A right unit $\tilde u$ would give $\tilde Q_6\diamond\tilde u=\tilde Q_6$ for all $\tilde Q_6$; the left member is a value of the block and so has zero scalar part, while the right member $e_t$ has scalar part $1$, so the condition already fails at $\tilde Q_6=e_t$. So the block has no unit on either side, and the two displays of the proposition are the two one-sided actions that replace it.

### The Sixteen Values of the Basis

Because the operation is sesquilinear, its values on the basis determine it. On the four real basis elements,

| $\diamond$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $0$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $\vec e_z$ | $0$ | $-\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $0$ |

and the remaining values follow from the conjugate-linearity in the second slot, $e_I\diamond (i e_J)=-i\,(e_I\diamond e_J)$. The table exhibits the two features of the block at once: the row and the column of $e_t$ are the vector parts $-\mathbf{e}_J$ and $\mathbf{e}_I$, which is the image computation above, and the diagonal is zero **on the real basis alone**,

$$
e_t\diamond e_t=\vec e_x\diamond \vec e_x=\vec e_y\diamond \vec e_y=\vec e_z\diamond \vec e_z=0,
$$

while off the real basis it is not, by the next section. The real basis therefore sees a bracket that looks alternating, and the complex space sees the conjugated one; the difference is the coefficientwise conjugation, which acts trivially on the real span.

## The Diagonal, and the Failure of the Jacobi Identity

**Proposition (the diagonal is the vector part of the square).** For every biquaternion,

$$
\tilde Q\diamond\tilde Q=\mathrm{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr),
$$

the vector part of the square of the row. It does not vanish in general: at $\tilde Q=\vec e_x+i\vec e_y$ it is

$$
(\vec e_x+i\vec e_y)\diamond(\vec e_x+i\vec e_y)=2i\vec e_z\neq0 .
$$

The formula, the criterion for the vanishing and the cone that the diagonal traces are the subject of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, below in this block, where they are computed; here the non-vanishing alone is recorded, because it is what forbids reading the block as a Lie product.

**Theorem (the Jacobi identity fails).** Write, for an operation $b$, the **cyclic sum** at a triple $(\tilde Q_3,\tilde Q_4,\tilde Q_5)$ as

$$
\mathrm{cyc}\,\mathfrak{b}(\tilde Q_3,\tilde Q_4,\tilde Q_5)=b\bigl(\mathfrak{b}(\tilde Q_3,\tilde Q_4),\tilde Q_5\bigr)+b\bigl(\mathfrak{b}(\tilde Q_4,\tilde Q_5),\tilde Q_3\bigr)+b\bigl(\mathfrak{b}(\tilde Q_5,\tilde Q_3),\tilde Q_4\bigr),
$$

the outer form of *The Symmetric and Antisymmetric Parts of an Algebra Product*, §*Lie-Admissible Algebras*, with the factor $\tfrac12$ carried by $b$ itself. Then

$$
\mathrm{cyc}\,\diamond\,(e_t,\vec e_x,\vec e_y)=\vec e_z\neq0 ,
$$

so $\diamond$ is not a Lie bracket. The value is the one tabulated for $\mathrm{APS}$ in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Twelve Structures, One by One*, recomputed here as the article declares its cyclic sum.

**Remark (the reason).** For $\mathrm{AQA}$ the failure comes from the non-associativity of the quaternionic bilinear product that is antisymmetrised; here the antisymmetrised product is the plain sesquilinear one, whose two involutions — the coefficientwise conjugation of the base and the star of the second slot — are both non-trivial, so that product is **not** associative and the obstruction of *Lie Algebras of Sesqualgebras* applies. There the antisymmetrisation $x\star y-y\star x$ of a sesquilinear product is $R^{\varsigma}$-bilinear and antisymmetric, and it is a Lie bracket exactly when the product $\star$ is associative; for a unital faithful sesqualgebra that associativity would force both involutions to collapse, $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$, which a genuine sesqualgebra over $(\mathbb{C},\bar{\cdot})$ forbids. The plain sesquilinear product is such a genuine sesqualgebra, so its antisymmetrisation fails. The failure is developed, with the obstruction and the comparison with the two siblings $\mathrm{AQA}$ and $\mathrm{AQS}$, in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

**Remark (a second witness, and its coincidence with $\mathrm{AQS}$).** The block also fails at the complex triple $(\vec e_x,\vec e_x,i\vec e_y)$, where the cyclic sum is $-2i\vec e_y$. That is the witness of the quaternionic sesquilinear sibling $\mathrm{AQS}$ of *Introduction to the Symmetric Quaternionic Sesqualgebra*, and the coincidence is not an accident: both blocks are conjugate-alternating, and a conjugate-alternating operation fails the Jacobi identity as soon as a conjugate-linear slot meets a non-real coefficient. The failure at the real triple $(e_t,\vec e_x,\vec e_y)$ is of the other kind, shared with the bilinear sibling $\mathrm{AQA}$, and it is visible on the real span; both failures, and their two reasons, are developed in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, below in this block.

## The Reconstruction and the Placement among the Twelve

**Theorem (the reconstruction).** The general plain sesquilinear product is the sum of its two adapted parts,

$$
\tilde Q_1\tilde Q_2^{*}=\mathrm{SPS}(\tilde Q_1,\tilde Q_2)+\tilde Q_1\diamond\tilde Q_2
=\bigl[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr]e_t+\bigl(-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}\bigr),
$$

the symmetric half being central-valued and the antisymmetric half pure-vector. Each half of the sum is a sesquilinear product of the class, by the independence theorem of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and neither is recoverable from the other; together they are the product.

**Remark (the placement).** In the table of *The 12 Products of the Biquaternion Complex Space* the block occupies the row

| name | the product | scalar part | vector part | law | unit | image |
|---|---|---|---|---|---|---|
| $\mathrm{APS}$ | $\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)$ | $\bigl[0\bigr]$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |

and it is the plain-sesqualgebra sibling of three other antisymmetrisations: $\mathrm{APA}=\vec Q_1\times\vec Q_2$, which is the one Lie product of the twelve, $\mathrm{AQA}=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, which fails on the associator, and $\mathrm{AQS}=\vec Q_1\times\overline{\vec Q_2}$, which fails as the block does. On the **real** part of the space the block is its own operation: it is $\tilde Q_1\diamond\tilde Q_2=-Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$, which coincides with no other of the twelve, while on the real **vectors** alone it is the cross product up to sign, $\vec Q_1\diamond\vec Q_2=-\vec Q_1\times\vec Q_2$. The ten operations of the real part, and the two coincidences $\mathrm{APA}=\mathrm{AQS}$ and $\mathrm{SQA}=\mathrm{SPS}$ that reduce the twelve to ten there, are tabulated in *The 12 Products of the Biquaternion Complex Space*; the block is not one of the coincidences.

## The Interpretation in the Physics Band

The block is the **phase** of the pairing. Its diagonal does not vanish: it is the vector part of the square, $\tilde Q\diamond\tilde Q = \mathrm{Vect}(\tilde Q\tilde Q^{*})$, and it is purely imaginary, so its direction is a real axis. Its law is conjugate-alternation, $\tilde Q_1\diamond\tilde Q_2 = -\overline{\tilde Q_2\diamond\tilde Q_1}$, so an exchange of the two arguments both reverses and conjugates the value. Its Jacobi identity fails, so this phase structure is not a Lie algebra.

The readings are these, and each belongs to the physics article named; this article stops at the algebra. The diagonal, as $i$ times a real vector, is read as the axis of the relative phase of two amplitudes in *The Biquaternioid Antisymmetric Plain Sesqualgebra (APS) over $\mathbb{C}$*. The failure of the Jacobi identity, and the absence of a Lie algebra of the phase on the state space, are read in *The Biquaternioid Antisymmetric Plain Sesqualgebra (APS) over $\mathbb{C}$*.

## Summary

The antisymmetric part of the general plain sesquilinear product is $\tilde Q_1\diamond\tilde Q_2=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$, a sesquilinear operation over $(\mathbb{C},\bar{\cdot})$ that is **conjugate-alternating**, $\tilde Q_1\diamond\tilde Q_2=-\overline{\tilde Q_2\diamond\tilde Q_1}$, and neither alternating nor anti-commutative. Its values are pure vector and fill the vector subspace, its scalar part vanishes, it has no unit on either side, and the coefficientwise conjugation is an automorphism of it. The diagonal is the vector part of the square, $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$, which is $2i\vec e_z$ at $\vec e_x+i\vec e_y$ and zero on the real basis; the Jacobi identity fails, at the real triple $(e_t,\vec e_x,\vec e_y)$ with the cyclic sum $\vec e_z$ and at the conjugated witness $(\vec e_x,\vec e_x,i\vec e_y)$ with $-2i\vec e_y$, the first failure being the bilinear face shared with $\mathrm{AQA}$ and the second the obstruction of *Lie Algebras of Sesqualgebras*, and the block is the plain-sesqualgebra sibling of $\mathrm{AQS}$ among the two failures of that kind. With the symmetric half it reconstructs the product, $\tilde Q_1\tilde Q_2^{*}=\mathrm{SPS}(\tilde Q_1,\tilde Q_2)+\tilde Q_1\diamond\tilde Q_2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, read here with the sesquilinear product split |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis; $e_t$ the unit, $\vec e_k$ the quaternion units; $i$ the central scalar imaginary |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion and its scalar–vector split, $Q_\mu\in\mathbb{C}$ |
| $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the coefficientwise, the natural and the Hermitian conjugations, $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ |
| $\tilde Q_1\diamond\tilde Q_2=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$ | the operation of the block, the antisymmetric plain sesqualgebra $\mathrm{APS}$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hermitian form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* |
| $\mathrm{Vect}(\mathbb{B}),\mathbb{C}_{\mathbb{B}}$ | the vector subspace and the centre of the remarkable subspaces |
| $\tilde Q_1\diamond\tilde Q_2=-\overline{\tilde Q_2\diamond\tilde Q_1}$ | conjugate-alternation, the law the block satisfies |
| $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$ | the diagonal, the vector part of the square |
| $\mathrm{cyc}\,b$ | the cyclic sum $b(\mathfrak{b}(\tilde Q_3,\tilde Q_4),\tilde Q_5)+b(\mathfrak{b}(\tilde Q_4,\tilde Q_5),\tilde Q_3)+b(\mathfrak{b}(\tilde Q_5,\tilde Q_3),\tilde Q_4)$ |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra.md`), for the symmetric half that with this one reconstructs the product
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the diagonal, its criterion and the failure with its obstruction
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the adapted exchange, its two parts and the independence of the halves
- *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product* (`articles_maths/the-conjugate-symmetric-and-skew-conjugate-symmetric-parts-of-a-sesquilinear-product.md`), for the long development of the same split, the projections and the structure constants
- *Introduction to the General Plain Sesqualgebra* (`articles_maths/introduction-to-the-general-plain-sesqualgebra.md`), for the product that is split and its one-sided unit
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the coordinate rule of the product and of the conjugations
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the row table, the three Jacobi failures and the ten operations of the real part
- *Lie Algebras of Sesqualgebras* (`articles_maths/lie-algebras-of-sesqualgebras.md`), for the obstruction that forbids the antisymmetrisation of a genuine sesquilinear product
- *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternioid* (`articles_maths/the-sesquilinear-commutator-and-the-symmetrised-product-on-the-biquaternioid.md`), for the other, bare, antisymmetrisation of the same product
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces and their bases
