# __Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions__

## Introduction

The general plain sesquilinear product $\tilde P\tilde Q^{*}$ splits into two halves, and the split is the **adapted** one of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*: the exchange is not the bare interchange of the two arguments but the interchange followed by the coefficientwise conjugation of the value, and its two parts are the conjugate-symmetric half $\mathrm{SPS}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})e_0$ and the **skew-conjugate-symmetric** half developed here,

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}\bigr)
=\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)
=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}} .
$$

The first half is *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the two together reconstruct the product, $\tilde P\tilde Q^{*}=\mathrm{SPS}(\tilde P,\tilde Q)+\tilde P\diamond\tilde Q$, and this article introduces the second. It is the **antisymmetric plain sesqualgebra** (APS) of the block: the antisymmetric part of the general plain sesquilinear product under the conjugate transpose.

The insertion of the conjugation into the exchange changes the whole vocabulary. A bilinear antisymmetrisation is *alternating*, it vanishes on the diagonal, and for such an operation the exchange of the arguments alone reverses the sign. Here the conjugation is part of the operation, and the symmetry that survives is the **conjugate-alternation**

$$
\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P},
$$

a statement about the two arguments and the coefficientwise conjugate of the value at once, and not the alternating sign of the bilinear rows. The diagonal is consequently **not** zero: it is the vector part of the square of the row, $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$, which is $2ie_3$ at the element $e_1+ie_2$. The operation is therefore neither alternating nor anti-commutative; it is conjugate-alternating, and this article fixes that vocabulary before anything else.

Three boundaries are stated at once. The product that is split, its two-sided operators and its two models are *Introduction to the General Plain Sesqualgebra of Biquaternions*, *The Left and Right Multiplications of the Biquaternion Sesqualgebra* and the two articles *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation* and *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation*, and none of the three is repeated here. The product itself, the four general products as a family and the row table are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *Comparison Between the Four General Products*. The general construction of the parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and its long development, with the conjugation, the projections and the structure constants, is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*; both are cited and not restated. The **other** antisymmetrisation of the same product, the sesquilinear commutator of *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions*, is the half of the **bare** interchange and is a different operation; §*The Adapted Exchange* of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* sets the two side by side, and the exact defect between them is computed in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, below in this block.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, $e_k^2=-e_0$, and central scalar imaginary $i$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$ and $\overline{\mathbf{Q}}$ the coefficientwise conjugate of the vector part. The natural conjugation ${}^{\natural}$ negates the vector part, the coefficientwise conjugation $\bar{\cdot}$ conjugates the coefficients, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, with coordinates $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$. The dot and cross products of vector parts are the complex bilinear ones of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the Hermitian form is $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ of *Biquaternion Norm and Invertibility*. The six distinguished subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ of *Introduction to the Six Subspaces*. Throughout, $\diamond$ is the operation of this block.

## The Operation

### The Definition and the Coordinate Rule

**Definition.** The **antisymmetric plain sesqualgebra** is the operation

$$
\diamond\;:\;\mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{B},\qquad
(\tilde P,\tilde Q)\longmapsto \tilde P\diamond\tilde Q=\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr),
$$

the vector part of the general plain sesquilinear product. Equivalently, it is the **skew-conjugate-symmetric part** of that product under the exchange $\tilde P\tilde Q^{*}\mapsto\overline{\tilde Q\tilde P^{*}}$,

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}\bigr),
$$

which is the general definition of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Two Parts Under Their Own Names*, read on the biquaternion product with the conjugation $\bar{\cdot}$.

The equivalence of the two displays is the definition of the vector part. Indeed $\overline{\tilde Q\tilde P^{*}}=(\tilde P\tilde Q^{*})^{\natural}$ for the biquaternion product, since $\natural(\overline{X})=X^{*}$ and $\natural$ is an anti-automorphism, so that $\tfrac12\bigl(X-X^{\natural}\bigr)=\mathrm{Vect}(X)$ at $X=\tilde P\tilde Q^{*}$. That identity is the reason the two sesqualgebra rows of the row table admit the exchange *read on the value*: the conjugate transpose of the value is the natural conjugate of the same value, and the two halves of the same element fall out.

Written on the coordinates, collecting the scalar and the vector parts and conjugating the second one,

$$
\tilde P\diamond\tilde Q=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}},
$$

so the scalar part vanishes identically, $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$, and the vector part is the antisymmetrisation of the scalar–vector formula of the product. The first two terms mix the scalar parts with the vector parts, and the last is the cross product of the vector part of the first argument with the conjugate of the vector part of the second.

### The Class

**Proposition.** The operation $\diamond$ is additive in each variable and **sesquilinear** over $(\mathbb{C},\bar{\cdot})$: $\mathbb{C}$-linear in the first argument and conjugate-linear in the second,

$$
(\lambda\tilde P)\diamond\tilde Q=\lambda\,(\tilde P\diamond\tilde Q),\qquad
\tilde P\diamond(\lambda \tilde Q)=\overline{\lambda}\,(\tilde P\diamond\tilde Q)\qquad(\lambda\in\mathbb{C}).
$$

*Proof.* The values lie in the vector subspace and the two rules are the two scalar rules of the sesquilinear product read through the vector part: $\mathrm{Vect}(\lambda\tilde P\,\tilde Q^{*})=\lambda\,\mathrm{Vect}(\tilde P\tilde Q^{*})$ and $\mathrm{Vect}(\tilde P(\lambda\tilde Q)^{*})=\mathrm{Vect}(\overline{\lambda}\,\tilde P\tilde Q^{*})=\overline{\lambda}\,\mathrm{Vect}(\tilde P\tilde Q^{*})$. $\square$

**Remark.** The operation therefore belongs to the same class as the product it splits, and not to the class of the six $\mathbb{C}$-bilinear parts of the two algebra rows. In the row table of *The 12 Products of the Biquaternion Complex Space* it is the entry $\mathrm{APS}$, in the plain sesqualgebra row, between $\mathrm{GPS}$ and $\mathrm{SPS}$. The distinction is the one the two rows of the table exhibit: the six operations of the algebra rows are $\mathbb{C}$-bilinear, the six of the sesqualgebra rows are sesquilinear over $(\mathbb{C},\bar{\cdot})$, and the count twelve is the count over the complex space alone.

### Conjugate-Alternation

**Theorem (the operation is conjugate-alternating).** For all biquaternions,

$$
\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}.
$$

*Proof.* $\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}\bigr)$ and $\tilde Q\diamond\tilde P=\tfrac12\bigl(\tilde Q\tilde P^{*}-\overline{\tilde P\tilde Q^{*}}\bigr)$; conjugating the second and negating, $-\overline{\tilde Q\diamond\tilde P}=\tfrac12\bigl(\overline{\tilde Q\tilde P^{*}}-\tilde P\tilde Q^{*}\bigr)=\tilde P\diamond\tilde Q$. $\square$

**Remark (the vocabulary).** Three words have to be separated, because the operation satisfies none of the bilinear ones. It is **not alternating**, since its diagonal is not zero; it is **not anti-commutative**, since $\tilde P\diamond\tilde Q\ne-\tilde Q\diamond\tilde P$ off the real part; and it is **not a Lie bracket**, since the cyclic sum fails at the triple $(e_0,e_1,e_2)$ of the next section. It is conjugate-alternating and nothing else, and what replaces the vanishing diagonal is not a sign but the conjugation: the diagonal is **purely imaginary**, $\tilde Q\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde Q}$, and the pair of statements that the exchange yields is $\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}$ and $\overline{\tilde P\diamond\tilde Q}=\overline{\tilde P}\diamond\overline{\tilde Q}$.

**Proposition (the coefficientwise conjugation is an automorphism).** For all biquaternions,

$$
\overline{\tilde P\diamond\tilde Q}=\overline{\tilde P}\diamond\overline{\tilde Q}.
$$

*Proof.* $\overline{\mathrm{Vect}(\tilde P\tilde Q^{*})}=\mathrm{Vect}(\overline{\tilde P\tilde Q^{*}})=\mathrm{Vect}(\overline{\tilde P}\,\overline{\tilde Q^{*}})$ and $\overline{\tilde Q^{*}}=\tilde Q^{\natural}$, so the value is $\mathrm{Vect}(\overline{\tilde P}\,\tilde Q^{\natural})=(\overline{\tilde P})\diamond(\overline{\tilde Q})$, since $(\overline{\tilde Q})^{*}=\tilde Q^{\natural}$. $\square$

**Remark.** The proposition is the conjugation-symmetry of the block, and it is the reason the block is stable under the conjugation of the space: the conjugation is a conjugate-linear automorphism of $\diamond$, in the same way that the interchange is an automorphism of a commutative product and its negative one of a Lie product. It is also the shape the exchange takes in this row, and it is what makes the two halves $\mathrm{SPS}$ and $\diamond$ read the same value $\tilde P\tilde Q^{*}$ through the two conjugations ${}^{\natural}$ and $\bar{\cdot}$.

## The Image and the Absence of a Unit

**Proposition (the image is the vector subspace; the centre is not in it).** The image of $\diamond$ is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three over $\mathbb{C}$; the operation is central-free, so no value lies in the centre $\mathbb{C}_{\mathbb{B}}$ except $0$. The two one-sided actions of the unit are

$$
\tilde P\diamond e_0=\mathbf{P},\qquad e_0\diamond\tilde Q=-\overline{\mathbf{Q}} .
$$

*Proof.* Every value is a vector part, so the image is contained in $\mathrm{Vect}(\mathbb{B})$. The first display gives the whole vector subspace, since $\mathbf{P}$ is an arbitrary vector part, and it is the computation of $\mathrm{Vect}(\tilde P e_0^{*})=\mathrm{Vect}(\tilde P)$. The second is $\mathrm{Vect}(\tilde Q^{*})=\mathrm{Vect}(-\overline{\mathbf{Q}})=-\overline{\mathbf{Q}}$. The scalar part vanishing with a nonzero vector part is not central, and the zero value is central. $\square$

**Remark (the unit is not a unit of the block).** The sesqualgebra has a unit on the right alone, by *Introduction to the General Plain Sesqualgebra of Biquaternions*, and the block inherits neither side. A left unit $\tilde u$ would give $\tilde u\diamond e_0=e_0$, but $\tilde u\diamond e_0=\mathbf{u}$ has zero scalar part while $e_0$ has scalar part $1$: no left unit. A right unit $\tilde u$ would give $\tilde R\diamond\tilde u=\tilde R$ for all $\tilde R$; the left member is a value of the block and so has zero scalar part, while the right member $e_0$ has scalar part $1$, so the condition already fails at $\tilde R=e_0$. So the block has no unit on either side, and the two displays of the proposition are the two one-sided actions that replace it.

### The Sixteen Values of the Basis

Because the operation is sesquilinear, its values on the basis determine it. On the four real basis elements,

| $\diamond$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $0$ | $-e_1$ | $-e_2$ | $-e_3$ |
| $e_1$ | $e_1$ | $0$ | $-e_3$ | $e_2$ |
| $e_2$ | $e_2$ | $e_3$ | $0$ | $-e_1$ |
| $e_3$ | $e_3$ | $-e_2$ | $e_1$ | $0$ |

and the remaining values follow from the conjugate-linearity in the second slot, $e_I\diamond (i e_J)=-i\,(e_I\diamond e_J)$. The table exhibits the two features of the block at once: the row and the column of $e_0$ are the vector parts $-\mathbf{e}_J$ and $\mathbf{e}_I$, which is the image computation above, and the diagonal is zero **on the real basis alone**,

$$
e_0\diamond e_0=e_1\diamond e_1=e_2\diamond e_2=e_3\diamond e_3=0,
$$

while off the real basis it is not, by the next section. The real basis therefore sees a bracket that looks alternating, and the complex space sees the conjugated one; the difference is the coefficientwise conjugation, which acts trivially on the real span.

## The Diagonal, and the Failure of the Jacobi Identity

**Proposition (the diagonal is the vector part of the square).** For every biquaternion,

$$
\tilde Q\diamond\tilde Q=\mathrm{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr),
$$

the vector part of the square of the row. It does not vanish in general: at $\tilde Q=e_1+ie_2$ it is

$$
(e_1+ie_2)\diamond(e_1+ie_2)=2ie_3\neq0 .
$$

The formula, the criterion for the vanishing and the cone that the diagonal traces are the subject of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, below in this block, where they are computed; here the non-vanishing alone is recorded, because it is what forbids reading the block as a Lie product.

**Theorem (the Jacobi identity fails).** Write, for an operation $b$, the **cyclic sum** at a triple $(\tilde X,\tilde Y,\tilde Z)$ as

$$
\mathrm{cyc}\,b(\tilde X,\tilde Y,\tilde Z)=b\bigl(b(\tilde X,\tilde Y),\tilde Z\bigr)+b\bigl(b(\tilde Y,\tilde Z),\tilde X\bigr)+b\bigl(b(\tilde Z,\tilde X),\tilde Y\bigr),
$$

the outer form of *The Symmetric and Antisymmetric Parts of an Algebra Product*, §*Lie-Admissible Algebras*, with the factor $\tfrac12$ carried by $b$ itself. Then

$$
\mathrm{cyc}\,\diamond\,(e_0,e_1,e_2)=e_3\neq0 ,
$$

so $\diamond$ is not a Lie bracket. The value is the one tabulated for $\mathrm{APS}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Twelve Structures, One by One*, recomputed here as the article declares its cyclic sum.

**Remark (the reason).** For $\mathrm{AQA}$ the failure comes from the non-associativity of the quaternionic bilinear product that is antisymmetrised; here the antisymmetrised product is the plain sesquilinear one, whose two involutions — the coefficientwise conjugation of the base and the star of the second slot — are both non-trivial, so that product is **not** associative and the obstruction of *Lie Algebras of Sesqualgebras* applies. There the antisymmetrisation $x\star y-y\star x$ of a sesquilinear product is $R^{\varsigma}$-bilinear and antisymmetric, and it is a Lie bracket exactly when the product $\star$ is associative; for a unital faithful sesqualgebra that associativity would force both involutions to collapse, $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$, which a genuine sesqualgebra over $(\mathbb{C},\bar{\cdot})$ forbids. The plain sesquilinear product is such a genuine sesqualgebra, so its antisymmetrisation fails. The failure is developed, with the obstruction and the comparison with the two siblings $\mathrm{AQA}$ and $\mathrm{AQS}$, in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

**Remark (a second witness, and its coincidence with $\mathrm{AQS}$).** The block also fails at the complex triple $(e_1,e_1,ie_2)$, where the cyclic sum is $-2ie_2$. That is the witness of the quaternionic sesquilinear sibling $\mathrm{AQS}$ of *The Antisymmetric Quaternionic Sesqualgebra in the Matrix Representations*, and the coincidence is not an accident: both blocks are conjugate-alternating, and a conjugate-alternating operation fails the Jacobi identity as soon as a conjugate-linear slot meets a non-real coefficient. The failure at the real triple $(e_0,e_1,e_2)$ is of the other kind, shared with the bilinear sibling $\mathrm{AQA}$, and it is visible on the real span; both failures, and their two reasons, are developed in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, below in this block.

## The Reconstruction and the Placement among the Twelve

**Theorem (the reconstruction).** The general plain sesquilinear product is the sum of its two adapted parts,

$$
\tilde P\tilde Q^{*}=\mathrm{SPS}(\tilde P,\tilde Q)+\tilde P\diamond\tilde Q
=\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]e_0+\bigl(-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}\bigr),
$$

the symmetric half being central-valued and the antisymmetric half pure-vector. Each half of the sum is a sesquilinear product of the class, by the independence theorem of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and neither is recoverable from the other; together they are the product.

**Remark (the placement).** In the table of *The 12 Products of the Biquaternion Complex Space* the block occupies the row

| name | the product | scalar part | vector part | law | unit | image |
|---|---|---|---|---|---|---|
| $\mathrm{APS}$ | $\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}\bigr)$ | $\bigl[0\bigr]$ | $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |

and it is the plain-sesqualgebra sibling of three other antisymmetrisations: $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$, which is the one Lie product of the twelve, $\mathrm{AQA}=P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$, which fails on the associator, and $\mathrm{AQS}=\mathbf{P}\times\overline{\mathbf{Q}}$, which fails as the block does. On the **real** part of the space the block is its own operation: it is $\tilde P\diamond\tilde Q=-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$, which coincides with no other of the twelve, while on the real **vectors** alone it is the cross product up to sign, $\mathbf{P}\diamond\mathbf{Q}=-\mathbf{P}\times\mathbf{Q}$. The ten operations of the real part, and the two coincidences $\mathrm{APA}=\mathrm{AQS}$ and $\mathrm{SQA}=\mathrm{SPS}$ that reduce the twelve to ten there, are tabulated in *The 12 Products of the Biquaternion Complex Space*; the block is not one of the coincidences.

## The Reading in the Physics Band

The block is the **phase** of the pairing. Its diagonal does not vanish: it is the vector part of the square, $\tilde Q\diamond\tilde Q = \mathrm{Vect}(\tilde Q\tilde Q^{*})$, and it is purely imaginary, so its direction is a real axis. Its law is conjugate-alternation, $\tilde P\diamond\tilde Q = -\overline{\tilde Q\diamond\tilde P}$, so an exchange of the two arguments both reverses and conjugates the value. Its Jacobi identity fails, so this phase structure is not a Lie algebra.

The readings are these, and each belongs to the physics article named; this article stops at the algebra. The diagonal, as $i$ times a real vector, is read as the axis of the relative phase of two amplitudes in *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*. The failure of the Jacobi identity, and the absence of a Lie algebra of the phase on the state space, are read in *Interference without a Lie Algebra: the Jacobi Failure in the State Space*.

## Summary

The antisymmetric part of the general plain sesquilinear product is $\tilde P\diamond\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$, a sesquilinear operation over $(\mathbb{C},\bar{\cdot})$ that is **conjugate-alternating**, $\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}$, and neither alternating nor anti-commutative. Its values are pure vector and fill the vector subspace, its scalar part vanishes, it has no unit on either side, and the coefficientwise conjugation is an automorphism of it. The diagonal is the vector part of the square, $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$, which is $2ie_3$ at $e_1+ie_2$ and zero on the real basis; the Jacobi identity fails with the cyclic sum $e_3$ at $(e_0,e_1,e_2)$, by the obstruction of *Lie Algebras of Sesqualgebras* and not by an associator, and the block is the plain-sesqualgebra sibling of $\mathrm{AQS}$ among the two failures of that kind. With the symmetric half it reconstructs the product, $\tilde P\tilde Q^{*}=\mathrm{SPS}(\tilde P,\tilde Q)+\tilde P\diamond\tilde Q$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, read here with the sesquilinear product split |
| $e_0,e_1,e_2,e_3$ | the basis; $e_0$ the unit, $e_k$ the quaternion units; $i$ the central scalar imaginary |
| $\tilde Q=Q_0e_0+\mathbf{Q}$ | a biquaternion and its scalar–vector split, $Q_\mu\in\mathbb{C}$ |
| $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the coefficientwise, the natural and the Hermitian conjugations, $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ |
| $\tilde P\diamond\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | the operation of the block, the antisymmetric plain sesqualgebra $\mathrm{APS}$ |
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | the Hermitian form of *Biquaternion Norm and Invertibility* |
| $\mathrm{Vect}(\mathbb{B}),\mathbb{C}_{\mathbb{B}}$ | the vector subspace and the centre of the six distinguished subspaces |
| $\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}$ | conjugate-alternation, the law the block satisfies |
| $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$ | the diagonal, the vector part of the square |
| $\mathrm{cyc}\,b$ | the cyclic sum $b(b(\tilde X,\tilde Y),\tilde Z)+b(b(\tilde Y,\tilde Z),\tilde X)+b(b(\tilde Z,\tilde X),\tilde Y)$ |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the symmetric half that with this one reconstructs the product
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the diagonal, its criterion and the failure with its obstruction
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the adapted exchange, its two parts and the independence of the halves
- *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product* (`articles_maths/the-conjugate-symmetric-and-skew-conjugate-symmetric-parts-of-a-sesquilinear-product.md`), for the long development of the same split, the projections and the structure constants
- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product that is split and its one-sided unit
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the coordinate rule of the product and of the conjugations
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the row table, the three Jacobi failures and the ten operations of the real part
- *Lie Algebras of Sesqualgebras* (`articles_maths/lie-algebras-of-sesqualgebras.md`), for the obstruction that forbids the antisymmetrisation of a genuine sesquilinear product
- *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions* (`articles_maths/the-sesquilinear-commutator-and-the-symmetrised-product-on-the-biquaternions.md`), for the other, bare, antisymmetrisation of the same product
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished subspaces and their bases
