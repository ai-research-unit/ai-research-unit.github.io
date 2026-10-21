# __Introduction to the Symmetric Quaternionic Algebra__

## Introduction

The biquaternion space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, and the second of them is the **general quaternionic bilinear product** $\tilde Q_1^{\natural}\tilde Q_2$, the plain product with the natural conjugation read on the first factor (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*). Every bilinear product on $\mathbb{B}$ splits into a symmetric part and an antisymmetric part, and this article is the introduction of the block that reads the symmetric part of $\tilde Q_1^{\natural}\tilde Q_2$ as a multiplication:

$$
\tilde Q_1\star\tilde Q_2 = \tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2 + \tilde Q_2^{\natural}\tilde Q_1\bigr).
$$

The general construction of the splitting is *The Symmetric and Antisymmetric Parts of an Algebra Product*; here it is cited and not restated. The article establishes the elementary theory of the operation: its rule, its coefficient, the sixteen products of the basis, its laws — commutativity, and the failure of associativity, of power-associativity, of the Jordan identity, of the Jacobi identity and of the alternating law — its image, the absence of a unit, the square and its polarisation, and the placement of the structure $\mathrm{SQA}$ among the twelve. The name $\mathrm{SQA}$ and the verb *collapse* are the two threads: the operation collapses the whole space onto its central line, and every later article of the block is a reading of the single formula $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$.

**Boundaries.** The four general products and their comparison are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *Comparison Between the Four General Products*; the catalogue of the twelve operations, whose row $\mathrm{SQA}$ is one line, is *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the general definitions of the unit, the inverse, the zero divisor, the idempotent, the nilpotent and the root are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the remarkable subspaces are *Introduction to the Remarkable Subspaces*; the norm, its polarisation and its isotropic cone are *Norm and Invertibility in the General Quaternionic Algebra* and *Zero Divisors of the Biquaternion Algebra*; the Jordan theory and the symmetrisation of an associative product are *Jordan Algebras*. The companion articles of the block read the same operation through its form (*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*), on the remarkable subspaces (*Remarkable Subspaces under the Symmetric Quaternionic Algebra*), through its multiplication operators (*The Multiplication Operators of the Symmetric Quaternionic Algebra*) and in the two matrix models.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}Q_{2,\mu} e_\mu=Q_{2t}e_t+\vec Q_2$ with $Q_{2t}\in\mathbb{C}$ and $\vec Q_2=Q_{2x}\vec e_x+Q_{2y}\vec e_y+Q_{2z}\vec e_z$, and $(\vec Q_1,\vec Q_2)=\sum_{k\in\{x,y,z\}}Q_{1,k}Q_{2,k}$ is the complex bilinear form of the two vector parts. The **natural conjugation** is $\tilde Q_2^{\natural}=Q_{2t}-\vec Q_2$, the **star** is $\tilde Q_2^{*}=\overline{Q_{2t}}-\overline{\vec Q_2}$, and the **Hermitian conjugation** is $\overline{\tilde Q_2}=\tilde Q_2^{\natural*}$; all three fix $e_t$, and the star and the Hermitian conjugation are conjugate-linear. The **centre** of the plain product is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, the **vector subspace** is $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\vec e_x+\mathbb{C}\vec e_y+\mathbb{C}\vec e_z$, and $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ are the remaining remarkable subspaces of *Introduction to the Remarkable Subspaces*. The symmetric quaternionic multiplication is denoted $\star$ throughout the Common Theory entries of the block and $\bullet$ in its Specific Theory and Operators entries; the two are the same operation.

## The Operation

**Definition.** The **symmetric quaternionic multiplication** of $\mathbb{B}$ is the operation

$$
\tilde Q_1\star\tilde Q_2 = \tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2 + \tilde Q_2^{\natural}\tilde Q_1\bigr).
$$

It is the symmetric part of the general quaternionic product $\tilde Q_1^{\natural}\tilde Q_2$ for the exchange of the two arguments (*The Symmetric and Antisymmetric Parts of an Algebra Product*), and its antisymmetric half is the quaternionic bracket

$$
[\tilde Q_1,\tilde Q_2]_{\natural} = \tilde Q_1^{\natural}\tilde Q_2 - \tilde Q_2^{\natural}\tilde Q_1
$$

of the antisymmetric quaternionic algebra (*Introduction to the Antisymmetric Quaternionic Algebra*). The two halves reconstruct the parent product,

$$
\tilde Q_1^{\natural}\tilde Q_2 = \tilde Q_1\star\tilde Q_2 + \tfrac12[\tilde Q_1,\tilde Q_2]_{\natural},
$$

and the operation is the multiplication of the structure denoted $\mathrm{SQA}$ in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Both slots are read linearly: the operation is $\mathbb{C}$-bilinear, the class of the parent product, and no conjugation is inserted in either slot of $\star$.

**Theorem (the value is central and the coefficient is the quaternion form).** For all $\tilde Q_1,\tilde Q_2\in\mathbb{B}$,

$$
\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{\natural}\,e_t,\qquad \langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2).
$$

*Proof.* Write $\tilde Q_1^{\natural}\tilde Q_2$ in scalar and vector parts (*Introduction to the General Quaternionic Algebra*): scalar part $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$, vector part $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$. The exchange $\tilde Q_2^{\natural}\tilde Q_1$ has the same scalar part and the vector part $Q_{2t}\vec Q_1-Q_{1t}\vec Q_2-\vec Q_2\times\vec Q_1$. In the half-sum the two mixed terms cancel and the two cross products cancel by $\vec Q_1\times\vec Q_2=-\vec Q_2\times\vec Q_1$.

The coefficient $\langle\cdot,\cdot\rangle_{\natural}$ is the **quaternion form**, the one of the four forms of the space that the catalogue article *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* attaches to $\mathrm{SQA}$; its comparison with the other three forms is *Comparison Between the Four General Products* and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

**Corollary (the class and the commutativity).** The operation is $\mathbb{C}$-bilinear and commutative, its value is always central, and its commutator vanishes identically,

$$
\tilde Q_1\star\tilde Q_2=\tilde Q_2\star\tilde Q_1,\qquad [\tilde Q_1,\tilde Q_2]_{\star}=\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1=0 .
$$

*Proof.* Bilinearity is read on the definition, the two slots being linear; commutativity is read on the defining half-sum; centrality is the theorem; and the commutator vanishes because the product is commutative.

**Remark (the value is central although neither summand is).** The two summands $\tilde Q_1^{\natural}\tilde Q_2$ and $\tilde Q_2^{\natural}\tilde Q_1$ are exchanged by the natural conjugation, $(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1$, and an average of two elements exchanged by an involution is fixed by it; the elements fixed by ${}^{\natural}$ are the central ones. This is the reason for the centrality, and the reason $\mathrm{SQA}$ behaves unlike the symmetric part of the plain product, which keeps a vector part. Every later statement of the block is a reading of the formula $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$; the operation is the pairing $\langle\cdot,\cdot\rangle_{\natural}$ placed on the central line.

## The Multiplication Table

The product of two basis elements is read from the definition and tabulated.

**Proposition (the basis table).** For $\mu,\nu\in\{t,x,y,z\}$,

$$
e_\mu\star e_\nu = \delta_{\mu\nu}\,e_t .
$$

*Proof.* For $\mu=\nu=t$: $e_t\star e_t=\tfrac12(e_t e_t+e_t e_t)=e_t$, and $\langle e_t,e_t\rangle_{\natural}=1$. For $\mu=\nu=k\in\{x,y,z\}$: $\vec e_k\star \vec e_k=\vec e_k^{\natural}\vec e_k=(-\vec e_k)\vec e_k=e_t$, since $\vec e_k^2=-e_t$, and $\langle \vec e_k,\vec e_k\rangle_{\natural}=1$. For $\mu\ne\nu$: if both indices are in $\{x,y,z\}$ then $e_\mu^{\natural}e_\nu=-e_\mu e_\nu$ and $e_\nu^{\natural}e_\mu=-e_\nu e_\mu$, and $e_\mu e_\nu=-e_\nu e_\mu$ for the basis, so the two summands cancel; if one index is $t$ and the other is $k\in\{x,y,z\}$ then $e_t^{\natural}\vec e_k=\vec e_k$ and $\vec e_k^{\natural}e_t=-\vec e_k$, which cancel; so the value is $0=\delta_{\mu\nu}e_t$.

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $e_t$ | $0$ | $0$ |
| $\vec e_y$ | $0$ | $0$ | $e_t$ | $0$ |
| $\vec e_z$ | $0$ | $0$ | $0$ | $e_t$ |

**Corollary (bilinearity and the determination by the table).** The sixteen products are exactly the sixteen entries of the unit matrix: the coefficient $\langle\cdot,\cdot\rangle_{\natural}$ is the standard symmetric $\mathbb{C}$-bilinear form of $\mathbb{C}^4$, with Gram matrix the identity on the basis, and the operation is determined by its table, $(\sum_\mu Q_{1,\mu} e_\mu)\star(\sum_\nu Q_{2,\nu} e_\nu)=\sum_\mu Q_{1,\mu} Q_{2,\mu}\,e_t$.

*Proof.* The table gives $e_\mu\star e_\nu=\delta_{\mu\nu}e_t$, and bilinearity extends the display to the general pair; conversely the display evaluates the definition of $\langle\cdot,\cdot\rangle_{\natural}$.

**Remark (the table is not the one of the plain product).** The plain product gives a fixed-point-free permutation table with signs (*Introduction to the Biquaternion Algebra*), and the quaternionic product one with the first column negated. The entry $e_\mu\star e_\nu$ is the symmetrisation of the second, and it is diagonal because the antisymmetric part is what carries the off-diagonal signs: the symmetric half of the quaternionic product keeps only the diagonal of the quaternionic table. The table is the smallest possible for a nonzero operation.

## The Laws of the Operation

The operation is a commutative multiplication with zero commutator, and no further law survives. The reference for the laws is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The laws of a product*, and the reading of the twelve one by one is *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### Commutativity, and the Collapse of the Derived Operation

The operation is commutative, so its **commutator** vanishes identically and the derived operation is the zero operation. The derived algebra is therefore the central line $\mathbb{C}e_t$ alone, on which the operation is the multiplication of $\mathbb{C}$: for complex $A,B$,

$$
(Ae_t)\star(Be_t)=AB\,e_t .
$$

The operation carries no Lie structure; the antisymmetric half of the parent carries it instead, and that half is $\mathrm{AQA}$.

### Associativity

**Proposition (the operation is not associative).** At $\tilde Q_1=\tilde Q_2=\vec e_x$, $\tilde Q_4=e_t$ the two bracketings differ,

$$
(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4=e_t\neq 0=\tilde Q_1\star(\tilde Q_2\star\tilde Q_4),
$$

and the general associator is

$$
(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4-\tilde Q_1\star(\tilde Q_2\star\tilde Q_4)
=\bigl(\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}R_t-Q_{1t}\langle\tilde Q_2,\tilde Q_4\rangle_{\natural}\bigr)e_t .
$$

*Proof.* $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t\star\tilde Q_4=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}R_te_t$, and $\tilde Q_1\star(\tilde Q_2\star\tilde Q_4)=\langle\tilde Q_2,\tilde Q_4\rangle_{\natural}\,Q_{1t}e_t$. At the witness the first is $\langle \vec e_x,\vec e_x\rangle_{\natural}e_t=e_t$ and the second $\langle \vec e_x,e_t\rangle_{\natural}e_t=0$.

### Power-Associativity

**Proposition (the operation is not power-associative).** The bracketings of the fourth power do not agree. At $\tilde Q_1=e_t+\vec e_x$, whose square is $\tilde Q_1\star\tilde Q_1=2e_t$,

$$
(\tilde Q_1\star\tilde Q_1)\star(\tilde Q_1\star\tilde Q_1)=4e_t\neq 2e_t=\bigl((\tilde Q_1\star\tilde Q_1)\star\tilde Q_1\bigr)\star\tilde Q_1 .
$$

*Proof.* $\tilde Q_1\star\tilde Q_1=\langle\tilde Q_1\rangle_{\natural}e_t=2e_t$. On the left the product is $2e_t\star2e_t=4e_t$. On the right, $(\tilde Q_1\star\tilde Q_1)\star\tilde Q_1=2e_t\star\tilde Q_1=2Q_{1t}e_t=2e_t$, and $2e_t\star\tilde Q_1=2e_t$ again; so the right side is $2e_t$. The two differ, and the failure is not a failure of the commutator but of the associator: the first bracketing uses the square of the square, the second the cube.

The three-element powers agree, since $\tilde Q_1\star(\tilde Q_1\star\tilde Q_1)=(\tilde Q_1\star\tilde Q_1)\star\tilde Q_1$ by commutativity; the failure appears at the fourth power, the first power at which two essentially different bracketings exist.

### The Two Classical Identities

**Proposition (the Jordan identity fails).** The commutative operation is not a Jordan product: with the parenthesisation of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the identity

$$
\tilde Q_1\star\bigl(\tilde Q_2\star(\tilde Q_1\star\tilde Q_1)\bigr)
=\bigl(\tilde Q_1\star\tilde Q_2\bigr)\star\bigl(\tilde Q_1\star\tilde Q_1\bigr)
$$

fails, and at $\tilde Q_1=\tilde Q_2=\vec e_x$ the two sides are $0$ and $e_t$.

*Proof.* At $x=\vec e_x$ the square is $x\star x=e_t$. The left side is $x\star(x\star e_t)=x\star \langle x,e_t\rangle_{\natural}e_t=x\star0=0$; the right side is $(x\star x)\star(x\star x)=e_t\star e_t=\langle e_t,e_t\rangle_{\natural}e_t=e_t$.

**Proposition (the Jacobi identity fails).** For the same product the identity

$$
\tilde Q_1\star(\tilde Q_2\star\tilde Q_3)+\tilde Q_2\star(\tilde Q_3\star\tilde Q_1)+\tilde Q_3\star(\tilde Q_1\star\tilde Q_2)=0
$$

fails, and at $\tilde Q_1=\tilde Q_2=\tilde Q_3=e_t$ its left side is $3e_t$.

*Proof.* $\tilde Q_2\star\tilde Q_3=\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}e_t$, so the first term is $Q_{1t}\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}e_t$ and the sum is $\bigl(Q_{1t}\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}+Q_{2t}\langle\tilde Q_3,\tilde Q_1\rangle_{\natural}+Q_{3t}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}\bigr)e_t$, which at the three units is $3e_t$.

**Proposition (the alternating law fails).** The operation is not alternating: $e_t\star e_t=e_t\neq0$, so there is an element whose square does not vanish.

The operation is therefore neither associative, nor power-associative, nor a Jordan product, nor a Lie bracket. It is one of the two central operations of the twelve, the other being the symmetric part of the plain sesquilinear product, and the collapse of the commutator does not imply the collapse of the associator.

## The Image and the Unit

**Proposition (the image is the central line).** The image of $\star$ is the central line $\mathbb{C}e_t=\mathbb{C}_{\mathbb{B}}$, on which the operation is the multiplication of $\mathbb{C}$.

*Proof.* Every value is central by the theorem of §*The Operation*, and every central element is a complex multiple of $e_t$.

**Proposition (there is no unit).** The operation has no unit, and no one-sided unit either. For every element $\tilde Q_5$,

$$
\tilde Q_5\star e_t=e_t\star\tilde Q_5=Q_{5t}\,e_t ,
$$

so $e_t$ is a unit for the central line alone. An element $\tilde u$ with $\tilde u\star\tilde Q=\tilde Q$ for every $\tilde Q$ would give $\tilde u\star e_t=u_te_t=e_t$, hence $u_t=1$, and then $\tilde u\star \vec e_x=u_xe_t=\vec e_x$, which is impossible because $u_xe_t$ is central and $\vec e_x$ is not.

*Proof.* The display is the theorem at $\tilde Q=e_t$: $\langle\tilde Q_5,e_t\rangle_{\natural}=Q_{5t}=\langle e_t,\tilde Q_5\rangle_{\natural}$. The unit argument is the one displayed; the same computation with the argument $\vec e_x$ excludes a right unit.

**Remark (the centre of the operation and the centre of the plain product).** Two different sets could be called central and are kept apart. Because $\star$ is commutative, its mutual commutant is the whole space: every element commutes with every other under $\star$. The centre of the *plain* product is the line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, and that is the set in which the *values* of $\star$ lie. The operation is thus commutative everywhere while producing values in the centre of the algebra, and the two statements are not merged.

**Remark (the operation acts by the scalar part).** Multiplication by the central element $Ae_t$ is the map $\tilde Q\mapsto AQ_te_t$: the scalar part of the argument, scaled and placed in the centre. The vector part of any argument is annihilated by the product with any element of the image. The operation is accordingly a representation of $\mathbb{C}$ on the central line rather than the multiplication of a unital algebra, and the first row and the first column of the table are the identity row and the identity column while the three vector rows and columns are zero.

## The Square and Its Polarisation

**Proposition (the square).** For every $\tilde Q$,

$$
\tilde Q\star\tilde Q = \langle\tilde Q\rangle_{\natural}\,e_t,\qquad \langle\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^2,
$$

and the coefficient is the polarisation of the square,

$$
\tilde Q_1\star\tilde Q_2=\tfrac12\Bigl(\langle\tilde Q_1+\tilde Q_2\rangle_{\natural}-\langle\tilde Q_1\rangle_{\natural}-\langle\tilde Q_2\rangle_{\natural}\Bigr)e_t .
$$

*Proof.* The square is the theorem of §*The Operation* at $\tilde Q_1=\tilde Q_2$, and $\langle\tilde Q_2,\tilde Q_2\rangle_{\natural}=\sum_\mu Q_{2,\mu}^2$; the polarisation identity is the expansion of the square of $\tilde Q_1+\tilde Q_2$ by bilinearity.

**Corollary (the square is the norm of the parent product).** The diagonal $\langle\cdot\rangle_{\natural}$ of the form of the block is exactly the multiplicative norm of the general plain algebra, $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ (*Norm and Invertibility in the General Quaternionic Algebra*), and the square-zero elements of the block are the elements of the isotropic cone of that norm. The two readings are kept apart in the articles of the block: $\langle\cdot\rangle_{\natural}$ is multiplicative for the parent product, while the block itself carries no unit and no multiplicative norm, and $\langle\cdot\rangle_{\natural}$ is only bilinear.

## The Placement Among the Twelve

The twelve operations are the four general products and their two parts each; $\star$ is the symmetric part of the general quaternionic product, and its antisymmetric half is the bracket $[\cdot,\cdot]_{\natural}$. The two halves reconstruct the parent,

$$
\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA},\qquad
\tilde Q_1^{\natural}\tilde Q_2=\tilde Q_1\star\tilde Q_2+\tfrac12[\tilde Q_1,\tilde Q_2]_{\natural},
$$

with $\mathrm{SQA}$ one of the two central operations and $\mathrm{AQA}$ one of the four antisymmetric ones (*The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*).

| the reading | the value | the class |
|---|---|---|
| $\mathrm{GQA}$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\mathbb{C}$-bilinear, no unit |
| $\mathrm{SQA}$ | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$ | $\mathbb{C}$-bilinear, commutative, central values, no unit |
| $\mathrm{AQA}$ | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$ | $\mathbb{C}$-bilinear, alternating, no unit |

**The two contrasts.** The operation differs from the symmetric part of the **plain** product, which is the Jordan product with the unit $e_t$, which is commutative and not central-valued, and which satisfies the Jordan identity; and it differs from the symmetric part of the **plain sesquilinear** product, which is central-valued like $\mathrm{SQA}$ but conjugate-commutative rather than commutative. On the real elements the two central operations coincide, $\mathrm{SQA}=\mathrm{SPS}$, and the catalogue records ten distinct operations on the real part against twelve on the complex space (*The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The exclusive law that singles $\mathrm{SQA}$ out among the twelve is stated in *The Specificities of the Symmetric Quaternionic Algebra*; the element theory of the block is the subject of the six later Common Theory entries.

**Remark (the name and what it does not claim).** The trailing $\mathrm A$ records that the operation is $\mathbb{C}$-bilinear and not merely sesquilinear, since the general quaternionic product from which it is taken is $\mathbb{C}$-bilinear. The word *symmetric* refers to the symmetry of the two slots, and the word *quaternionic* to the conjugation inserted in the parent product; neither word is a claim about a further structure.

## Summary

The symmetric part of the general quaternionic product $\tilde Q_1^{\natural}\tilde Q_2$ is the commutative $\mathbb{C}$-bilinear operation $\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$, whose value is always the central element $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ with $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ the quaternion form. The sixteen basis products are the entries of the unit matrix, $e_\mu\star e_\nu=\delta_{\mu\nu}e_t$, so the operation is the standard symmetric form of $\mathbb{C}^4$ read as a product and is determined by its table. The image is the central line $\mathbb{C}_{\mathbb{B}}$, on which the operation is the multiplication of $\mathbb{C}$; there is no unit and no one-sided unit, the element $e_t$ being a unit for the central line alone. The operation is commutative with vanishing commutator, and it fails associativity at $(\vec e_x,\vec e_x,e_t)$, power-associativity at $e_t+\vec e_x$, the Jordan identity at $\vec e_x$, the Jacobi identity at $e_t$ and the alternating law at $e_t$; the collapse of the commutator does not imply the collapse of the associator. The square is the norm of the parent product, $\tilde Q_2\star\tilde Q_2=\langle\tilde Q_2\rangle_{\natural}e_t$ with $\langle\tilde Q_2\rangle_{\natural}=\sum_\mu Q_{2,\mu}^2$, and its polarisation is the form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. The operation is the unique central and commutative one among the six $\mathbb{C}$-bilinear operations of the catalogue, and it collapses on the real part with the symmetric part of the plain sesquilinear product; the companion articles of the block read it through its form, its subspaces, its operators and its matrix models.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_k^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$ |
| ${}^{\natural}$, ${}^{*}$, $\overline{\cdot}$ | the natural, the star and the Hermitian conjugations, all fixing $e_t$ |
| $i$ | the central scalar imaginary, $i^2=-1$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product, the parent product |
| $\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$ | the symmetric quaternionic multiplication, the operation $\mathrm{SQA}$ |
| $[\tilde Q_1,\tilde Q_2]_{\natural}=\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1$ | the quaternionic bracket, the operation $\mathrm{AQA}$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | the quaternion form, the coefficient of the product |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the norm form, the diagonal of $\langle\cdot,\cdot\rangle_{\natural}$, the norm of the parent product |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the centre of the plain product, the image of $\star$ |
| $\mathrm{GQA},\mathrm{SQA},\mathrm{AQA}$ | the three operations of the quaternionic row of the catalogue |

## Further Reading

- [The Symmetric and Antisymmetric Parts of an Algebra Product](the-symmetric-and-antisymmetric-parts-of-an-algebra-product.html), for the splitting that produces the operation.
- [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra.html), for the parent product and its scalar–vector form.
- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html), for the row of $\mathrm{SQA}$ in the catalogue.
- [Introduction to the Antisymmetric Quaternionic Algebra](introduction-to-the-antisymmetric-quaternionic-algebra.html), for the other half of the row.
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html) and [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), for the norm form, its polarisation and its isotropic cone.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the general definitions of the unit, the inverse, the zero divisor, the idempotent, the nilpotent, the root and the laws of a product.
- [The Specificities of the Symmetric Quaternionic Algebra](the-specificities-of-the-symmetric-quaternionic-algebra.html), for the exclusive law of the block.
