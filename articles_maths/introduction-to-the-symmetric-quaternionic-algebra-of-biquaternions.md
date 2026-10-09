# __Introduction to the Symmetric Quaternionic Algebra of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four general products, and the second of them is the **general
quaternionic bilinear product** $\tilde P^{\natural}\tilde Q$, the plain product with the quaternion
conjugation read on the first factor (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*). Every bilinear product on
$\mathbb{B}$ splits into a symmetric part and an antisymmetric part, and this article is the introduction
of the block that reads the symmetric part of $\tilde P^{\natural}\tilde Q$:

$$
\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q + \tilde Q^{\natural}\tilde P\bigr).
$$

The general construction of the splitting is *The Symmetric and Antisymmetric Parts of an Algebra Product*,
and the operation itself, with its centrality, its coefficient and its failure of the Jordan identity, is the
subject of *The Symmetrised Quaternionic Product and the Hermitian Subspace*. The present article does not
restate either: it takes the operation as given, names it $\star$, and reads it as the multiplication of a
named structure, the **symmetric quaternionic algebra** $\mathrm{SQA}$, whose row in the catalogue is
*The 12 Products of the Biquaternion Complex Space*. The five companion articles of the
block read the same operation through the form it carries (*The Quaternion Form as a Product on the Symmetric
Quaternionic Algebra*), on the six distinguished subspaces (*The Six Subspaces under the Symmetric
Quaternionic Algebra of Biquaternions*), through its multiplication operators (*The Multiplication Operators
of the Symmetric Quaternionic Algebra*), and in the two matrix models (*The Symmetric Quaternionic Algebra in
the Matrix Representations*).

The article establishes the elementary theory of the operation: its class, its commutativity, its image, the
sixteen products of the basis, the square and its polarisation, its lack of a unit, the failure of the Jordan
identity, and the placement of $\mathrm{SQA}$ among the twelve operations. The operation is $\mathbb{C}$-bilinear
and commutative; its value is always a central element, a complex multiple of $e_0$; it has no unit; and the
algebra it makes is far from the associative one and far from a Jordan one. The name $\mathrm{SQA}$ and the
verb *collapse* are the two threads: the operation collapses the whole algebra onto its central line.

**Boundaries.** The product $\tilde P^{\natural}\tilde Q$ and the four general products are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, their comparison is *Comparison Between the Four General Products*, their relations are
*Relations Between the Four General Products*; the six subspaces are *Introduction to the Six Subspaces*;
the norm and the isotropy are *Biquaternion Norm and Invertibility* and *Biquaternion Zero Divisors*; the Jordan
theory is *Jordan Algebras*; the general splitting is the two parts articles. Nothing of the enriched layer of Part II is used here.

## The Operation

**Definition.** The **symmetric quaternionic multiplication** of $\mathbb{B}$ is the operation

$$
\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q + \tilde Q^{\natural}\tilde P\bigr).
$$

It is the symmetric part of the general quaternionic product $\tilde P^{\natural}\tilde Q$ for the exchange
of the two arguments (*The Symmetric and Antisymmetric Parts of an Algebra Product*), and its antisymmetric
half is the quaternionic bracket

$$
[\tilde P,\tilde Q]_{\natural} = \tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P
$$

of the antisymmetric quaternionic algebra
(*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*). The two halves reconstruct the
parent product,

$$
\tilde P^{\natural}\tilde Q = \tilde P\star\tilde Q + \tfrac12[\tilde P,\tilde Q]_{\natural},
$$

and the multiplication is the multiplication of the algebra denoted $\mathrm{SQA}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Theorem (the value is central and the coefficient is the quaternion form).** For all
$\tilde P,\tilde Q \in \mathbb{B}$,

$$
\tilde P\star\tilde Q = B(\tilde P,\tilde Q)\,e_0, \qquad
B(\tilde P,\tilde Q) = P_0Q_0 + (\mathbf P,\mathbf Q).
$$

*Proof.* Write $\tilde P^{\natural}\tilde Q$ in scalar and vector parts (*Introduction to the General
Quaternionic Algebra of Biquaternions*): scalar part $P_0Q_0+(\mathbf P,\mathbf Q)$, vector part
$P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$. The exchange $\tilde Q^{\natural}\tilde P$ has the same
scalar part and the vector part $Q_0\mathbf P-P_0\mathbf Q-\mathbf Q\times\mathbf P$. In the half-sum the two
mixed terms cancel and the two cross products cancel by $\mathbf P\times\mathbf Q=-\mathbf Q\times\mathbf P$.
$\square$

The theorem is the centrality statement of *The Symmetrised Quaternionic Product and the Hermitian Subspace*,
where the coefficient $B(\tilde P,\tilde Q)$ is called $\beta$ and is identified with the polarisation of the
norm. This article keeps the name $B$, the one the form carries in the catalogue article *The 12 Products of the Biquaternion Complex Space*; the form, with its comparison with the other three, is
*Comparison Between the Four General Products* and *The Four Pairings of the Biquaternion Algebra*.

**Corollary (the class and the commutativity).** The operation $\star$ is $\mathbb{C}$-bilinear and
commutative, and its image is the central line $\mathbb{C}e_0 = \mathbb{C}_{\mathbb{B}}$, the centre of
$\mathbb{B}$. It is a commutative multiplication with **zero commutator**, $[\tilde P,\tilde Q]_\star =\tilde P\star\tilde Q-\tilde Q\star\tilde P=0$ for every pair.

*Proof.* Bilinearity is read on the definition, the two slots being linear. Commutativity is read on the
defining half-sum. The image is central by the theorem, and the commutator vanishes because the product is
commutative. $\square$

**Remark (the value is central although neither summand is).** The two summands $\tilde P^{\natural}\tilde Q$
and $\tilde Q^{\natural}\tilde P$ are exchanged by the conjugation, $(\tilde P^{\natural}\tilde Q)^{\natural}= \tilde Q^{\natural}\tilde P$, and an average of two elements exchanged by an involution is fixed by it; the
elements fixed by ${}^{\natural}$ are the central ones. This is the reason for the centrality, and it is the
structural reason that $\mathrm{SQA}$ behaves unlike the symmetric part of the plain product, which keeps a
vector part. The point is the one *The Symmetrised Quaternionic Product and the Hermitian Subspace* develops;
it is quoted here because every later statement of the block is a reading of the single formula
$\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$.

## The Sixteen Products of the Basis

The basis is $e_0=1,e_1,e_2,e_3$, with $e_k^2=-e_0$ and the cyclic products $e_1e_2=e_3$,
$e_2e_3=e_1$, $e_3e_1=e_2$; the conjugation reads $e_0^{\natural}=e_0$ and $e_k^{\natural}=-e_k$. The product of
two basis elements is read from the definition, and it is computed before it is tabulated.

**Proposition (the basis table).** For $\mu,\nu\in\{0,1,2,3\}$,

$$
e_\mu\star e_\nu = \delta_{\mu\nu}\,e_0 .
$$

*Proof.* For $\mu=\nu=0$: $e_0\star e_0=\tfrac12(e_0e_0+e_0e_0)=e_0$, and $B(e_0,e_0)=1$. For
$\mu=\nu=k\ne0$: $e_k\star e_k=\tfrac12(e_k^{\natural}e_k+e_k^{\natural}e_k)=e_k^{\natural}e_k=(-e_k)e_k=e_0$,
since $e_k^2=-e_0$, and $B(e_k,e_k)=1$. For $\mu\ne\nu$: if both indices are nonzero then
$e_\mu^{\natural}e_\nu=-e_\mu e_\nu$ and $e_\nu^{\natural}e_\mu=-e_\nu e_\mu$, and $e_\mu e_\nu=-e_\nu e_\mu$,
so the two summands cancel; if one index is $0$ and the other is $k\ne0$ then $e_0^{\natural}e_k=e_k$ and
$e_k^{\natural}e_0=-e_k$, which cancel; so the value is $0=\delta_{\mu\nu}e_0$. $\square$

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $e_0$ | $0$ | $0$ |
| $e_2$ | $0$ | $0$ | $e_0$ | $0$ |
| $e_3$ | $0$ | $0$ | $0$ | $e_0$ |

**Corollary (the table is the identity matrix read in the basis).** The sixteen products are exactly the
sixteen entries of $I_4$, and the multiplication is the one whose Gram matrix relative to the basis is the
unit matrix: the coefficient $B$ is the standard symmetric $\mathbb{C}$-bilinear form of $\mathbb{C}^4$. The
table is the smallest possible for a nonzero operation, every basis element squaring to the unit and every
two distinct basis elements multiplying to $0$.

**Remark (the table is not the one of the plain product).** The plain product gives a fixed-point-free
permutation table with signs (*Introduction to the General Plain Algebra of Biquaternions*), and the
quaternionic product one with the first column negated (*Introduction to the General Quaternionic Algebra of
Biquaternions*). The entry $e_\mu\star e_\nu$ is the symmetrisation of the second, and it is diagonal because
the antisymmetric part is what carries the off-diagonal signs: the symmetric half of the quaternionic product
keeps only the diagonal of the quaternionic table.

## The Image, the Unit, and the Absence of One

**Proposition (the image is the central line).** The image of $\star$ is the central line
$\mathbb{C}e_0=\mathbb{C}_{\mathbb{B}}$. Restricted to that line the operation is the multiplication of
$\mathbb{C}$: for complex $A,B$,

$$
(Ae_0)\star(Be_0) = AB\,e_0 .
$$

*Proof.* The image is central by the theorem of the first section, and every central element is a complex
multiple of $e_0$. On the line $B(Ae_0,Be_0)=AB$, so the two readings agree. $\square$

**Proposition (no unit).** The operation has no unit. More precisely, for every element $\tilde A$,

$$
\tilde A\star e_0 = e_0\star\tilde A = A_0\,e_0 ,
$$

so the element $e_0$ is a unit for the central line alone: an element $u$ with $u\star\tilde Q=\tilde Q$ for
every $\tilde Q$ would need $u\star e_0=u_0e_0=e_0$, giving $u_0=1$, and then $u\star e_1=u_1e_0=e_1$, which
is impossible because $u_1e_0$ is central and $e_1$ is not. The element $e_0$ is the only idempotent besides
$0$.

*Proof.* The display is the theorem at $\tilde Q=e_0$: $B(\tilde A,e_0)=A_0$ and $B(e_0,\tilde A)=A_0$. A unit
$u$ would satisfy $u\star\tilde Q=\tilde Q$ for every $\tilde Q$: at $\tilde Q=e_0$ this gives $u_0e_0=e_0$,
hence $u_0=1$, and at $\tilde Q=e_1$ it gives $u_1e_0=e_1$, whose left side is a complex multiple of $e_0$
while the right side is not, so no $u$ exists. The idempotents are computed in *The Radical and the Isotropic
Elements of the Symmetric Quaternionic Algebra*, where $0$ and $e_0$ are the two. $\square$

**Remark (the centre acts by the projection of the scalar part).** The formula says that multiplication by
the central element $Ae_0$ is the map $\tilde Q\mapsto AQ_0e_0$: the scalar part of the second argument,
scaled and placed in the centre. The operation is accordingly a **representation of $\mathbb{C}$** on the
central line rather than the multiplication of an algebra with unit — every element acts through its scalar
part, and the vector part of an argument is annihilated by the product with any element of the image. The
first row and the first column of the table are the identity row and the identity column, and the three
vector rows and columns are zero.

## The Square, Its Polarisation, and the Elements It Kills

**Proposition (the square).** For every $\tilde Q$,

$$
\tilde Q\star\tilde Q = N(\tilde Q)\,e_0, \qquad N(\tilde Q) = \sum_{\mu=0}^3 Q_\mu^2,
$$

and the square is the norm form of *Biquaternion Norm and Invertibility* read as a product. The polarisation
of the square is the coefficient,

$$
\tilde P\star\tilde Q = \tfrac12\Bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\Bigr)e_0,
$$

so that $B$ is the polarisation of $N$.

*Proof.* The square is the theorem at $\tilde P=\tilde Q$, and $B(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2=N(\tilde Q)$.
The polarisation identity is the expansion of the square of $\tilde P+\tilde Q$ by the bilinearity of $\star$.
$\square$

**Corollary (the square-zero set is the isotropic cone).** The elements with $\tilde Q\star\tilde Q=0$ are
exactly the **isotropic** elements $N(\tilde Q)=0$, that is the zero divisors of *Biquaternion Zero
Divisors*. The cone is the affine cone over the quadric
$\{[Q_0:Q_1:Q_2:Q_3]:\sum_\mu Q_\mu^2=0\}$ of $\mathbb{P}^3(\mathbb{C})$, of complex dimension $2$ in the
projective space and $3$ in the algebra. Its study on the six subspaces is *The Six Subspaces under the
Symmetric Quaternionic Algebra of Biquaternions*, and the elements of the cone with a vanishing scalar part are the
pure zero divisors.

**Remark (why the square is central and the associator is not zero).** The square is central for the reason
the general value is, and the two-sided collapse of the operation is what makes its element theory poor: the
idempotents reduce to $0$ and $e_0$, the square-zero set is the whole isotropic cone, and the group of units
of the operation is empty since there is no unit. The operation nevertheless keeps a nonzero **associator**:
at $\tilde P=\tilde Q=e_1$ and $\tilde R=e_0$ the two bracketings are

$$
(\tilde P\star\tilde Q)\star\tilde R = e_0, \qquad
\tilde P\star(\tilde Q\star\tilde R) = 0,
$$

because $B(\tilde P,\tilde Q)R_0e_0=e_0$ while $P_0B(\tilde Q,\tilde R)e_0=0$. The multiplication is therefore
neither associative nor power-associative, and the cancellation of the commutator does not imply the
cancellation of the associator.

## The Failure of the Jordan Identity

**Theorem (the Jordan identity fails).** The commutative operation $\star$ is not a Jordan product: the
identity

$$
\tilde P\star\bigl(\tilde Q\star(\tilde P\star\tilde P)\bigr)
= \bigl(\tilde P\star\tilde Q\bigr)\star\bigl(\tilde P\star\tilde P\bigr)
$$

fails, and at $\tilde P=\tilde Q=e_1$ the two sides are $0$ and $e_0$.

*Proof.* At $x=e_1$ the square is $x\star x=e_0$. The left side is $x\star(x\star e_0)=x\star 0=0$, since
$x\star e_0=B(x,e_0)e_0=0$; the right side is $(x\star x)\star(x\star x)=e_0\star e_0=B(e_0,e_0)e_0=e_0$. The
two sides differ, so the identity fails. $\square$

**Remark (why the identity fails).** The failure is not an accident of the witness but a consequence of the
centrality. The value of every product is a complex multiple of $e_0$, so the two bracketings of the fourth
power are computed from scalar data that the identity does not compare: the left side collapses to $0$ as
soon as the scalar part of one argument vanishes, while the right side collapses only when the coefficient of
the central value vanishes. The identity of a commutative algebra whose values are central is not imposed by
an associative parent, and the general theory of the symmetrisation of an **associative** product — which is
what forces the Jordan identity in the classical case — does not apply (*Jordan Algebras*, and *The
Symmetrised Quaternionic Product and the Hermitian Subspace* for the contrast with the plain symmetrisation).

**Remark (the operation is not a Lie or a Jordan product).** With the commutator identically zero and the
Jordan identity failing, the operation is neither a Lie bracket nor a Jordan product on the whole space. It
is one of the two central operations of the twelve (*The 12 Products of the Biquaternion Complex Space*), the other being the symmetric part of the plain sesquilinear product; and it is the
unique central and commutative operation among the six $\mathbb{C}$-bilinear ones.

## The Placement Among the Twelve

The twelve operations of the catalogue are the four general products and their two parts each; $\star$ is the
symmetric part of the general quaternionic product and its antisymmetric half is the bracket
$[\cdot,\cdot]_{\natural}$. The two halves reconstruct the parent,

$$
\mathrm{GQA} = \mathrm{SQA} + \mathrm{AQA}, \qquad
\tilde P^{\natural}\tilde Q = \tilde P\star\tilde Q + \tfrac12[\tilde P,\tilde Q]_{\natural},
$$

with $\mathrm{SQA}$ one of the two central operations and $\mathrm{AQA}$ one of the four antisymmetric ones
(*The 12 Products of the Biquaternion Complex Space*).

| the reading | the value | the class |
|---|---|---|
| $\mathrm{GQA}$ | $\tilde P^{\natural}\tilde Q$ | $\mathbb{C}$-bilinear, no unit on the right |
| $\mathrm{SQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\mathbb{C}$-bilinear, commutative, central, no unit |
| $\mathrm{AQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $\mathbb{C}$-bilinear, alternating, no unit |

**The three contrasts.** The operation differs from the symmetric part of the **plain** product, which is the
Jordan product $\tilde P\bullet\tilde Q$ with the unit $e_0$ and satisfying the Jordan identity, and from the
symmetric part of the **plain sesquilinear** product, which is $\bar{\cdot}$-conjugate-commutative rather than
commutative. On the real elements the operation coincides with that of the symmetric part of the plain
sesquilinear product, and the two names collapse to one: the catalogue records ten distinct operations on the
real part, where $\mathrm{SQA}=\mathrm{SPS}$, and twelve on the complex space.

**Remark (the name and what it does not claim).** The trailing $\mathrm A$ records that the operation is
$\mathbb{C}$-bilinear and not merely sesquilinear, since the general quaternionic product from which it is
taken is $\mathbb{C}$-bilinear (*The 12 Products of the Biquaternion Complex Space*). The
name *symmetric* refers to the symmetry of the two slots, and the name *quaternionic* to the conjugation
inserted in the parent product; neither word is a claim about a further structure.

## Summary

The symmetric part of the general quaternionic product $\tilde P^{\natural}\tilde Q$ is the commutative
$\mathbb{C}$-bilinear operation $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$,
whose value is always the central element $B(\tilde P,\tilde Q)e_0$ with $B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$
the quaternion form. The sixteen basis products are the entries of the identity matrix, $e_\mu\star e_\nu=\delta_{\mu\nu}e_0$,
so the operation is the standard symmetric form of $\mathbb{C}^4$ read as a product. The image is the central
line $\mathbb{C}_{\mathbb{B}}$, on which the operation is the multiplication of $\mathbb{C}$; there is no
unit; the element $e_0$ and $0$ are the only idempotents; the square is the norm form, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$,
and its polarisation is $B$; the square-zero elements are exactly the isotropic elements, the zero divisors;
the Jordan identity fails, at $e_1$ with sides $0$ and $e_0$; and the operation is the unique central and
commutative one among the six $\mathbb{C}$-bilinear operations of the catalogue, collapsing on the real part
with the symmetric part of the plain sesquilinear product. The five companion articles of the block read the
same operation through its form, its subspaces, its operators and its matrix models.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2=-e_0$ |
| ${}^{\natural}$ | the quaternion conjugation, $e_0\mapsto e_0$, $e_k\mapsto -e_k$ |
| $\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product (the parent product) |
| $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | the symmetric quaternionic multiplication, the operation $\mathrm{SQA}$ |
| $[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$ | the quaternionic bracket, the operation $\mathrm{AQA}$ |
| $B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the quaternion form, the coefficient of the product |
| $N(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ | the norm form |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the image of $\star$ |
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | the Jordan product of the associative multiplication |
| $\mathrm{GQA},\mathrm{SQA},\mathrm{AQA}$ | the three operations of the quaternionic row of the catalogue |

## Further Reading

- *The Symmetrised Quaternionic Product and the Hermitian Subspace* (`articles_maths/the-symmetrised-quaternionic-product-and-the-hermitian-subspace.md`), for the centrality, the coefficient and the failure of the Jordan identity in full
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the row of $\mathrm{SQA}$ in the catalogue of the twelve
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the splitting that produces the operation
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the parent product
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`) and *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the norm form and its isotropic cone
- *Jordan Algebras* (`articles_maths/jordan-algebras.md`), for the symmetrisation of an associative product and the identity it inherits
