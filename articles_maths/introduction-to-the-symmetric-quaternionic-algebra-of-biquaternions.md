# __Introduction to the Symmetric Quaternionic Algebra of Biquaternions__

## Introduction

The biquaternion space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, and the second of them is the **general quaternionic bilinear product** $\tilde P^{\natural}\tilde Q$, the plain product with the natural conjugation read on the first factor (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*). Every bilinear product on $\mathbb{B}$ splits into a symmetric part and an antisymmetric part, and this article is the introduction of the block that reads the symmetric part of $\tilde P^{\natural}\tilde Q$ as a multiplication:

$$
\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q + \tilde Q^{\natural}\tilde P\bigr).
$$

The general construction of the splitting is *The Symmetric and Antisymmetric Parts of an Algebra Product*; here it is cited and not restated. The article establishes the elementary theory of the operation: its rule, its coefficient, the sixteen products of the basis, its laws — commutativity, and the failure of associativity, of power-associativity, of the Jordan identity, of the Jacobi identity and of the alternating law — its image, the absence of a unit, the square and its polarisation, and the placement of the structure $\mathrm{SQA}$ among the twelve. The name $\mathrm{SQA}$ and the verb *collapse* are the two threads: the operation collapses the whole space onto its central line, and every later article of the block is a reading of the single formula $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$.

**Boundaries.** The four general products and their comparison are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *Comparison Between the Four General Products*; the catalogue of the twelve operations, whose row $\mathrm{SQA}$ is one line, is *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the general definitions of the unit, the inverse, the zero divisor, the idempotent, the nilpotent and the root are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the remarkable subspaces are *Introduction to the Remarkable Subspaces*; the norm, its polarisation and its isotropic cone are *Norm and Invertibility in the General Quaternionic Algebra* and *Zero Divisors of the General Plain Algebra*; the Jordan theory and the symmetrisation of an associative product are *Jordan Algebras*. The companion articles of the block read the same operation through its form (*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*), on the remarkable subspaces (*Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*), through its multiplication operators (*The Multiplication Operators of the Symmetric Quaternionic Algebra*) and in the two matrix models.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\vec Q$ with $Q_0\in\mathbb{C}$ and $\vec Q=Q_1e_1+Q_2e_2+Q_3e_3$, and $(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k$ is the complex bilinear form of the two vector parts. The **natural conjugation** is $\tilde Q^{\natural}=Q_0-\vec Q$, the **star** is $\tilde Q^{*}=\overline{Q_0}-\overline{\vec Q}$, and the **Hermitian conjugation** is $\overline{\tilde Q}=\tilde Q^{\natural*}$; all three fix $e_0$, and the star and the Hermitian conjugation are conjugate-linear. The **centre** of the plain product is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the **vector subspace** is $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$, and $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ are the remaining remarkable subspaces of *Introduction to the Remarkable Subspaces*. The symmetric quaternionic multiplication is denoted $\star$ throughout the Common Theory entries of the block and $\bullet$ in its Specific Theory and Operators entries; the two are the same operation.

## The Operation

**Definition.** The **symmetric quaternionic multiplication** of $\mathbb{B}$ is the operation

$$
\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q + \tilde Q^{\natural}\tilde P\bigr).
$$

It is the symmetric part of the general quaternionic product $\tilde P^{\natural}\tilde Q$ for the exchange of the two arguments (*The Symmetric and Antisymmetric Parts of an Algebra Product*), and its antisymmetric half is the quaternionic bracket

$$
[\tilde P,\tilde Q]_{\natural} = \tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P
$$

of the antisymmetric quaternionic algebra (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*). The two halves reconstruct the parent product,

$$
\tilde P^{\natural}\tilde Q = \tilde P\star\tilde Q + \tfrac12[\tilde P,\tilde Q]_{\natural},
$$

and the operation is the multiplication of the structure denoted $\mathrm{SQA}$ in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Both slots are read linearly: the operation is $\mathbb{C}$-bilinear, the class of the parent product, and no conjugation is inserted in either slot of $\star$.

**Theorem (the value is central and the coefficient is the quaternion form).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
\tilde P\star\tilde Q = N(\tilde P,\tilde Q)\,e_0,\qquad N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q).
$$

*Proof.* Write $\tilde P^{\natural}\tilde Q$ in scalar and vector parts (*Introduction to the General Quaternionic Algebra of Biquaternions*): scalar part $P_0Q_0+(\vec P,\vec Q)$, vector part $P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$. The exchange $\tilde Q^{\natural}\tilde P$ has the same scalar part and the vector part $Q_0\vec P-P_0\vec Q-\vec Q\times\vec P$. In the half-sum the two mixed terms cancel and the two cross products cancel by $\vec P\times\vec Q=-\vec Q\times\vec P$.

The coefficient $N$ is the **quaternion form**, the one of the four forms of the space that the catalogue article *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* attaches to $\mathrm{SQA}$; its comparison with the other three forms is *Comparison Between the Four General Products* and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

**Corollary (the class and the commutativity).** The operation is $\mathbb{C}$-bilinear and commutative, its value is always central, and its commutator vanishes identically,

$$
\tilde P\star\tilde Q=\tilde Q\star\tilde P,\qquad [\tilde P,\tilde Q]_{\star}=\tilde P\star\tilde Q-\tilde Q\star\tilde P=0 .
$$

*Proof.* Bilinearity is read on the definition, the two slots being linear; commutativity is read on the defining half-sum; centrality is the theorem; and the commutator vanishes because the product is commutative.

**Remark (the value is central although neither summand is).** The two summands $\tilde P^{\natural}\tilde Q$ and $\tilde Q^{\natural}\tilde P$ are exchanged by the natural conjugation, $(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P$, and an average of two elements exchanged by an involution is fixed by it; the elements fixed by ${}^{\natural}$ are the central ones. This is the reason for the centrality, and the reason $\mathrm{SQA}$ behaves unlike the symmetric part of the plain product, which keeps a vector part. Every later statement of the block is a reading of the formula $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$; the operation is the pairing $N$ placed on the central line.

## The Multiplication Table

The product of two basis elements is read from the definition and tabulated.

**Proposition (the basis table).** For $\mu,\nu\in\{0,1,2,3\}$,

$$
e_\mu\star e_\nu = \delta_{\mu\nu}\,e_0 .
$$

*Proof.* For $\mu=\nu=0$: $e_0\star e_0=\tfrac12(e_0e_0+e_0e_0)=e_0$, and $N(e_0,e_0)=1$. For $\mu=\nu=k\ne0$: $e_k\star e_k=e_k^{\natural}e_k=(-e_k)e_k=e_0$, since $e_k^2=-e_0$, and $N(e_k,e_k)=1$. For $\mu\ne\nu$: if both indices are nonzero then $e_\mu^{\natural}e_\nu=-e_\mu e_\nu$ and $e_\nu^{\natural}e_\mu=-e_\nu e_\mu$, and $e_\mu e_\nu=-e_\nu e_\mu$ for the basis, so the two summands cancel; if one index is $0$ and the other is $k\ne0$ then $e_0^{\natural}e_k=e_k$ and $e_k^{\natural}e_0=-e_k$, which cancel; so the value is $0=\delta_{\mu\nu}e_0$.

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $e_0$ | $0$ | $0$ |
| $e_2$ | $0$ | $0$ | $e_0$ | $0$ |
| $e_3$ | $0$ | $0$ | $0$ | $e_0$ |

**Corollary (bilinearity and the determination by the table).** The sixteen products are exactly the sixteen entries of the unit matrix: the coefficient $N$ is the standard symmetric $\mathbb{C}$-bilinear form of $\mathbb{C}^4$, with Gram matrix the identity on the basis, and the operation is determined by its table, $(\sum_\mu P_\mu e_\mu)\star(\sum_\nu Q_\nu e_\nu)=\sum_\mu P_\mu Q_\mu\,e_0$.

*Proof.* The table gives $e_\mu\star e_\nu=\delta_{\mu\nu}e_0$, and bilinearity extends the display to the general pair; conversely the display evaluates the definition of $N$.

**Remark (the table is not the one of the plain product).** The plain product gives a fixed-point-free permutation table with signs (*Introduction to the General Plain Algebra of Biquaternions*), and the quaternionic product one with the first column negated. The entry $e_\mu\star e_\nu$ is the symmetrisation of the second, and it is diagonal because the antisymmetric part is what carries the off-diagonal signs: the symmetric half of the quaternionic product keeps only the diagonal of the quaternionic table. The table is the smallest possible for a nonzero operation.

## The Laws of the Operation

The operation is a commutative multiplication with zero commutator, and no further law survives. The reference for the laws is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The laws of a product*, and the reading of the twelve one by one is *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### Commutativity, and the Collapse of the Derived Operation

The operation is commutative, so its **commutator** vanishes identically and the derived operation is the zero operation. The derived algebra is therefore the central line $\mathbb{C}e_0$ alone, on which the operation is the multiplication of $\mathbb{C}$: for complex $A,B$,

$$
(Ae_0)\star(Be_0)=AB\,e_0 .
$$

The operation carries no Lie structure; the antisymmetric half of the parent carries it instead, and that half is $\mathrm{AQA}$.

### Associativity

**Proposition (the operation is not associative).** At $\tilde P=\tilde Q=e_1$, $\tilde R=e_0$ the two bracketings differ,

$$
(\tilde P\star\tilde Q)\star\tilde R=e_0\neq 0=\tilde P\star(\tilde Q\star\tilde R),
$$

and the general associator is

$$
(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R)
=\bigl(N(\tilde P,\tilde Q)R_0-P_0N(\tilde Q,\tilde R)\bigr)e_0 .
$$

*Proof.* $(\tilde P\star\tilde Q)\star\tilde R=N(\tilde P,\tilde Q)e_0\star\tilde R=N(\tilde P,\tilde Q)R_0e_0$, and $\tilde P\star(\tilde Q\star\tilde R)=N(\tilde Q,\tilde R)\,P_0e_0$. At the witness the first is $N(e_1,e_1)e_0=e_0$ and the second $N(e_1,e_0)e_0=0$.

### Power-Associativity

**Proposition (the operation is not power-associative).** The bracketings of the fourth power do not agree. At $\tilde X=e_0+e_1$, whose square is $\tilde X\star\tilde X=2e_0$,

$$
(\tilde X\star\tilde X)\star(\tilde X\star\tilde X)=4e_0\neq 2e_0=\bigl((\tilde X\star\tilde X)\star\tilde X\bigr)\star\tilde X .
$$

*Proof.* $\tilde X\star\tilde X=N(\tilde X)e_0=2e_0$. On the left the product is $2e_0\star2e_0=4e_0$. On the right, $(\tilde X\star\tilde X)\star\tilde X=2e_0\star\tilde X=2X_0e_0=2e_0$, and $2e_0\star\tilde X=2e_0$ again; so the right side is $2e_0$. The two differ, and the failure is not a failure of the commutator but of the associator: the first bracketing uses the square of the square, the second the cube.

The three-element powers agree, since $\tilde X\star(\tilde X\star\tilde X)=(\tilde X\star\tilde X)\star\tilde X$ by commutativity; the failure appears at the fourth power, the first power at which two essentially different bracketings exist.

### The Two Classical Identities

**Proposition (the Jordan identity fails).** The commutative operation is not a Jordan product: with the parenthesisation of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the identity

$$
\tilde P\star\bigl(\tilde Q\star(\tilde P\star\tilde P)\bigr)
=\bigl(\tilde P\star\tilde Q\bigr)\star\bigl(\tilde P\star\tilde P\bigr)
$$

fails, and at $\tilde P=\tilde Q=e_1$ the two sides are $0$ and $e_0$.

*Proof.* At $x=e_1$ the square is $x\star x=e_0$. The left side is $x\star(x\star e_0)=x\star N(x,e_0)e_0=x\star0=0$; the right side is $(x\star x)\star(x\star x)=e_0\star e_0=N(e_0,e_0)e_0=e_0$.

**Proposition (the Jacobi identity fails).** For the same product the identity

$$
\tilde X\star(\tilde Y\star\tilde Z)+\tilde Y\star(\tilde Z\star\tilde X)+\tilde Z\star(\tilde X\star\tilde Y)=0
$$

fails, and at $\tilde X=\tilde Y=\tilde Z=e_0$ its left side is $3e_0$.

*Proof.* $\tilde Y\star\tilde Z=N(\tilde Y,\tilde Z)e_0$, so the first term is $X_0N(\tilde Y,\tilde Z)e_0$ and the sum is $\bigl(X_0N(\tilde Y,\tilde Z)+Y_0N(\tilde Z,\tilde X)+Z_0N(\tilde X,\tilde Y)\bigr)e_0$, which at the three units is $3e_0$.

**Proposition (the alternating law fails).** The operation is not alternating: $e_0\star e_0=e_0\neq0$, so there is an element whose square does not vanish.

The operation is therefore neither associative, nor power-associative, nor a Jordan product, nor a Lie bracket. It is one of the two central operations of the twelve, the other being the symmetric part of the plain sesquilinear product, and the collapse of the commutator does not imply the collapse of the associator.

## The Image and the Unit

**Proposition (the image is the central line).** The image of $\star$ is the central line $\mathbb{C}e_0=\mathbb{C}_{\mathbb{B}}$, on which the operation is the multiplication of $\mathbb{C}$.

*Proof.* Every value is central by the theorem of §*The Operation*, and every central element is a complex multiple of $e_0$.

**Proposition (there is no unit).** The operation has no unit, and no one-sided unit either. For every element $\tilde A$,

$$
\tilde A\star e_0=e_0\star\tilde A=A_0\,e_0 ,
$$

so $e_0$ is a unit for the central line alone. An element $u$ with $u\star\tilde Q=\tilde Q$ for every $\tilde Q$ would give $u\star e_0=u_0e_0=e_0$, hence $u_0=1$, and then $u\star e_1=u_1e_0=e_1$, which is impossible because $u_1e_0$ is central and $e_1$ is not.

*Proof.* The display is the theorem at $\tilde Q=e_0$: $N(\tilde A,e_0)=A_0=N(e_0,\tilde A)$. The unit argument is the one displayed; the same computation with the argument $e_1$ excludes a right unit.

**Remark (the centre of the operation and the centre of the plain product).** Two different sets could be called central and are kept apart. Because $\star$ is commutative, its mutual commutant is the whole space: every element commutes with every other under $\star$. The centre of the *plain* product is the line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, and that is the set in which the *values* of $\star$ lie. The operation is thus commutative everywhere while producing values in the centre of the algebra, and the two statements are not merged.

**Remark (the operation acts by the scalar part).** Multiplication by the central element $Ae_0$ is the map $\tilde Q\mapsto AQ_0e_0$: the scalar part of the argument, scaled and placed in the centre. The vector part of any argument is annihilated by the product with any element of the image. The operation is accordingly a representation of $\mathbb{C}$ on the central line rather than the multiplication of a unital algebra, and the first row and the first column of the table are the identity row and the identity column while the three vector rows and columns are zero.

## The Square and Its Polarisation

**Proposition (the square).** For every $\tilde Q$,

$$
\tilde Q\star\tilde Q = N(\tilde Q)\,e_0,\qquad N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2,
$$

and the coefficient is the polarisation of the square,

$$
\tilde P\star\tilde Q=\tfrac12\Bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\Bigr)e_0 .
$$

*Proof.* The square is the theorem of §*The Operation* at $\tilde P=\tilde Q$, and $N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$; the polarisation identity is the expansion of the square of $\tilde P+\tilde Q$ by bilinearity.

**Corollary (the square is the norm of the parent product).** The diagonal $N$ of the form of the block is exactly the multiplicative norm of the general plain algebra, $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ (*Norm and Invertibility in the General Quaternionic Algebra*), and the square-zero elements of the block are the elements of the isotropic cone of that norm. The two readings are kept apart in the articles of the block: $N$ is multiplicative for the parent product, while the block itself carries no unit and no multiplicative norm, and $N$ is only bilinear.

## The Placement Among the Twelve

The twelve operations are the four general products and their two parts each; $\star$ is the symmetric part of the general quaternionic product, and its antisymmetric half is the bracket $[\cdot,\cdot]_{\natural}$. The two halves reconstruct the parent,

$$
\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA},\qquad
\tilde P^{\natural}\tilde Q=\tilde P\star\tilde Q+\tfrac12[\tilde P,\tilde Q]_{\natural},
$$

with $\mathrm{SQA}$ one of the two central operations and $\mathrm{AQA}$ one of the four antisymmetric ones (*The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*).

| the reading | the value | the class |
|---|---|---|
| $\mathrm{GQA}$ | $\tilde P^{\natural}\tilde Q$ | $\mathbb{C}$-bilinear, no unit |
| $\mathrm{SQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\mathbb{C}$-bilinear, commutative, central values, no unit |
| $\mathrm{AQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $\mathbb{C}$-bilinear, alternating, no unit |

**The two contrasts.** The operation differs from the symmetric part of the **plain** product, which is the Jordan product with the unit $e_0$, which is commutative and not central-valued, and which satisfies the Jordan identity; and it differs from the symmetric part of the **plain sesquilinear** product, which is central-valued like $\mathrm{SQA}$ but conjugate-commutative rather than commutative. On the real elements the two central operations coincide, $\mathrm{SQA}=\mathrm{SPS}$, and the catalogue records ten distinct operations on the real part against twelve on the complex space (*The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The exclusive law that singles $\mathrm{SQA}$ out among the twelve is stated in *The Specificities of the Symmetric Quaternionic Algebra*; the element theory of the block is the subject of the six later Common Theory entries.

**Remark (the name and what it does not claim).** The trailing $\mathrm A$ records that the operation is $\mathbb{C}$-bilinear and not merely sesquilinear, since the general quaternionic product from which it is taken is $\mathbb{C}$-bilinear. The word *symmetric* refers to the symmetry of the two slots, and the word *quaternionic* to the conjugation inserted in the parent product; neither word is a claim about a further structure.

## Summary

The symmetric part of the general quaternionic product $\tilde P^{\natural}\tilde Q$ is the commutative $\mathbb{C}$-bilinear operation $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$, whose value is always the central element $N(\tilde P,\tilde Q)e_0$ with $N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$ the quaternion form. The sixteen basis products are the entries of the unit matrix, $e_\mu\star e_\nu=\delta_{\mu\nu}e_0$, so the operation is the standard symmetric form of $\mathbb{C}^4$ read as a product and is determined by its table. The image is the central line $\mathbb{C}_{\mathbb{B}}$, on which the operation is the multiplication of $\mathbb{C}$; there is no unit and no one-sided unit, the element $e_0$ being a unit for the central line alone. The operation is commutative with vanishing commutator, and it fails associativity at $(e_1,e_1,e_0)$, power-associativity at $e_0+e_1$, the Jordan identity at $e_1$, the Jacobi identity at $e_0$ and the alternating law at $e_0$; the collapse of the commutator does not imply the collapse of the associator. The square is the norm of the parent product, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ with $N(\tilde Q)=\sum_\mu Q_\mu^2$, and its polarisation is the form $N(\tilde P,\tilde Q)$. The operation is the unique central and commutative one among the six $\mathbb{C}$-bilinear operations of the catalogue, and it collapses on the real part with the symmetric part of the plain sesquilinear product; the companion articles of the block read it through its form, its subspaces, its operators and its matrix models.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2=-e_0$, $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$ |
| ${}^{\natural}$, ${}^{*}$, $\overline{\cdot}$ | the natural, the star and the Hermitian conjugations, all fixing $e_0$ |
| $i$ | the central scalar imaginary, $i^2=-1$ |
| $\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product, the parent product |
| $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | the symmetric quaternionic multiplication, the operation $\mathrm{SQA}$ |
| $[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$ | the quaternionic bracket, the operation $\mathrm{AQA}$ |
| $N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$ | the quaternion form, the coefficient of the product |
| $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ | the norm form, the diagonal of $N$, the norm of the parent product |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre of the plain product, the image of $\star$ |
| $\mathrm{GQA},\mathrm{SQA},\mathrm{AQA}$ | the three operations of the quaternionic row of the catalogue |

## Further Reading

- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the splitting that produces the operation.
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the parent product and its scalar–vector form.
- *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.md`), for the row of $\mathrm{SQA}$ in the catalogue.
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the other half of the row.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`) and *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the norm form, its polarisation and its isotropic cone.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the general definitions of the unit, the inverse, the zero divisor, the idempotent, the nilpotent, the root and the laws of a product.
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the exclusive law of the block.
