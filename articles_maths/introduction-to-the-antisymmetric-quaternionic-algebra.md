# __Introduction to the Antisymmetric Quaternionic Algebra__

## Introduction

The general quaternionic product of the biquaternion algebra $\mathbb{B}$ is $\tilde Q_1^{\natural}\tilde Q_2$, the plain product with the first factor read through the quaternion conjugation ${}^{\natural}$; it is $\mathbb{C}$-bilinear, it has $e_t$ as a unit on the left only, and it is the quaternionic one of the four general products the $\mathbb{C}$-space carries (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *Introduction to the General Quaternionic Algebra*). A bilinear product over a field in which $2$ is invertible splits canonically into the sum of a symmetric and an antisymmetric part, the splitting induced by the exchange of the two arguments of the product (*The Symmetric and Antisymmetric Parts of an Algebra Product*). The **antisymmetric quaternionic multiplication** is the antisymmetric part of this product,

$$
\tilde Q_1 \diamond \tilde Q_2 = \tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2 - \tilde Q_2^{\natural}\tilde Q_1\bigr) = Q_{1t}\vec Q_2 - Q_{2t}\vec Q_1 - \vec Q_1\times\vec Q_2 ,
$$

and it is the operation of the present block. It is the quaternionic product with its scalar part removed: the scalar part of its value is zero, and its vector part is the mixed term $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ with the cross term $-\vec Q_1\times\vec Q_2$ added to it. The operation is written $\diamond$, a symbol used inside this block only; the quaternionic bracket of the corpus, $[\tilde Q_1,\tilde Q_2]_{\natural}=\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1$, is twice it.

This article introduces the block. It fixes the class of the operation, which is the bilinear class
$(\mathrm{id},\mathrm{id})$ and not the class of the parent; its two structural identities,
alternation and the vanishing of the diagonal; the image, which is the whole vector subspace
$\mathrm{Vect}(\mathbb{B})$ and nothing of the centre; the absence of a unit; the multiplication
table of the basis; the square, which vanishes identically, and its polarisation, which carries no
information about the operation; the identity of the operation with half the quaternionic
commutator; the failure of the Jacobi identity, with the witness on which the corpus reads it;
and the placement of the block among the twelve operations of the catalogue. The element theory
that the vanishing square forces — the nilpotents, the zero divisors, the idempotents and the
roots — is the subject of five companion articles of the Common Theory, and the failure, the
invariant forms, the remarkable subspaces, the operators and the two matrix models are the
subjects of the articles that follow; none of them is developed here.

The general construction of the two parts of a product is *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the split here is the one instance of it that belongs to the quaternionic row of the catalogue. The two halves reconstruct the parent, $\tilde Q_1^{\natural}\tilde Q_2 = \tilde Q_1\star\tilde Q_2 + \tilde Q_1\diamond\tilde Q_2$, with the symmetric half the operation of *Introduction to the Symmetric Quaternionic Algebra*; that article records the same split from its own side, and the two introductions are the two readings of one computation. The algebra, its basis and its conjugation are *Introduction to the General Quaternionic Algebra* and *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the remarkable subspaces named below are *Introduction to the Remarkable Subspaces*. The article is algebraic throughout: no notion of the analysis or of the geometry of the chapter is used.

## The Operation

**Definition.** The **antisymmetric quaternionic multiplication** of $\mathbb{B}$ is

$$
\tilde Q_1 \diamond \tilde Q_2 = \tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2 - \tilde Q_2^{\natural}\tilde Q_1\bigr),
$$

the antisymmetric part of the general quaternionic product for the exchange of the two arguments. The algebra $\mathbb{B}$ with this product is the **antisymmetric quaternionic algebra** of the block, written here with the same letters as its operation.

The parent product reads the first slot through ${}^{\natural}$ and the second slot as it
stands, so its class is $(\natural,\mathrm{id})$; the antisymmetrisation exchanges the two
slots, so each slot of the block carries the conjugation exactly once across the two terms of
the definition and the two conjugations cancel: the operation is $\mathbb{C}$-bilinear, of class
$(\mathrm{id},\mathrm{id})$, the class of *Definitions for the Study of the 12 Algebraic
Structures*, §*The Product, its Slots and its Class*.

**Proposition (the explicit form).** For all $\tilde Q_1 = Q_{1t}e_t + \vec Q_1$ and $\tilde Q_2 = Q_{2t}e_t + \vec Q_2$,

$$ \boxed{\; \tilde Q_1 \diamond \tilde Q_2 = Q_{1t}\vec Q_2 - Q_{2t}\vec Q_1 - \vec Q_1\times\vec Q_2 \;}. $$

In particular the scalar part of the value is zero and the value lies in the vector subspace $\mathrm{Vect}(\mathbb{B})$; the operation is $\mathbb{C}$-bilinear, alternating, and its diagonal vanishes.

*Proof.* The value of the parent product is $\tilde Q_1^{\natural}\tilde Q_2 = \bigl[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr]e_t + Q_{1t}\vec Q_2 - Q_{2t}\vec Q_1 - \vec Q_1\times\vec Q_2$ (*The 12 Products of the Biquaternion Complex Space*). The reverse product is obtained by exchanging the arguments, and its value is $[Q_{2t}Q_{1t}+(\vec Q_2,\vec Q_1)]e_t + Q_{2t}\vec Q_1 - Q_{1t}\vec Q_2 - \vec Q_2\times\vec Q_1$. The scalar part is symmetric in the pair and cancels in the difference; the vector part is antisymmetric in the pair, because the cross product reverses and the mixed terms exchange with a sign, and half the difference of the two vector parts is $\tfrac12\bigl[2(Q_{1t}\vec Q_2-Q_{2t}\vec Q_1) - 2\,\vec Q_1\times\vec Q_2\bigr] = Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, since $\vec Q_2\times\vec Q_1 = -\vec Q_1\times\vec Q_2$. Bilinearity is inherited from the product term by term with the coefficients in $\mathbb{C}$; alternation is the antisymmetry of the definition, $\tilde Q_2\diamond\tilde Q_1 = -\tilde Q_1\diamond\tilde Q_2$; and the diagonal vanishes at $\tilde Q_1=\tilde Q_2$, where the two terms of the definition cancel. Equivalently, the scalar part of the explicit form is zero, so the value never leaves $\mathrm{Vect}(\mathbb{B})$; and at $\tilde Q_1 = \tilde Q_2$ the three terms of the explicit form give $Q_{1t}\vec Q_1-Q_{1t}\vec Q_1-\vec Q_1\times\vec Q_1 = 0$.

**Remark (what the operation omits).** The scalar part of the parent product, the quaternionic form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$, is exactly the symmetric half. It carries the two terms that the exchange leaves fixed, the square terms $Q_{1t}Q_{2t}$ and the scalar product $(\vec Q_1,\vec Q_2)$ of the vectors, and the operation of this block is what remains of the parent product once that half is removed. The omission is total: the block never produces a central element, and every value has zero scalar part.

**Proposition (the two reconstructing identities).** For all $\tilde Q_1,\tilde Q_2$,

$$
\tilde Q_1^{\natural}\tilde Q_2 = \tilde Q_1\star\tilde Q_2 + \tilde Q_1\diamond\tilde Q_2 , \qquad
[\tilde Q_1,\tilde Q_2]_{\natural} = \tilde Q_1^{\natural}\tilde Q_2 - \tilde Q_2^{\natural}\tilde Q_1 = 2\,\tilde Q_1\diamond\tilde Q_2 ,
$$

with $\tilde Q_1\star\tilde Q_2 = \tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2 + \tilde Q_2^{\natural}\tilde Q_1\bigr)$ the symmetric half.

*Proof.* Adding and subtracting the two values of the parent product gives the sum and the difference; the sum is twice the symmetric half and the difference is the quaternionic bracket, twice the antisymmetric half by its definition.

The block is therefore the second of the two readings of one product: the parent product is recovered from the two halves, and the bracket of the corpus is the unhalved difference. The factor two is the only difference between the operation of this block and the quaternionic bracket, and it is recorded throughout.

## The Image and the Absence of a Unit

**Proposition (the image).** The image of the operation is the vector subspace,

$$ \boxed{\; \mathbb{B}\diamond\mathbb{B} = \mathrm{Vect}(\mathbb{B}) = \bigl\{\tilde Q : \tilde Q^{\natural} = -\tilde Q\bigr\} \;}, $$

of complex dimension three and real dimension six; the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ is disjoint from the image apart from $0$.

*Proof.* Every value has zero scalar part by the explicit form, so the image lies in $\mathrm{Vect}(\mathbb{B})$. Conversely, for a pure vector $\vec V$, the element $e_t$ acts as $\tilde Q_1\mapsto\vec Q_1$ from the left, $e_t\diamond\tilde Q_2 = \vec Q_2$, so $\vec V = e_t\diamond\vec V$ is a value. The centre is the set of elements with zero vector part, and $\mathrm{Vect}(\mathbb{B})$ is the set with zero scalar part, so their intersection is $0$.

**Remark (the two sides of the identity).** The element $e_t$ is a left identity on the vector subspace, $e_t\diamond\tilde Q_2 = \vec Q_2$, but it is not a two-sided identity there. The right multiplication by $e_t$ is the negative of the identity on the vector subspace, $\tilde Q_1\diamond e_t = -\vec Q_1$, and the two differ by the sign. The asymmetry is the asymmetry of the parent product, which has $e_t$ as a unit on the left only, and it is the reason no element that acts on one side acts on the other. In particular $e_t\diamond\tilde Q_2 = \vec Q_2$ recovers the vector part of $\tilde Q_2$ and discards the scalar part, so even on the image the left action of $e_t$ is the identity and its right action is its negative.

**Proposition (no unit).** The operation has no unit on the left and none on the right; equivalently, there is no $\tilde E$ with $\tilde E\diamond\tilde Q_1 = \tilde Q_1$ for all $\tilde Q_1$, and none with $\tilde Q_1\diamond\tilde E = \tilde Q_1$ for all $\tilde Q_1$.

*Proof.* A left unit $\tilde E$ would give, at $\tilde Q_1 = e_t$, the value $\tilde E\diamond e_t = -\vec E$, which would have to equal $e_t$; but $-\vec E$ is a pure vector and $e_t$ is not, so there is no left unit. A right unit would give, again at $\tilde Q_1 = e_t$, the value $e_t\diamond\tilde E = \vec E$, which would have to equal $e_t$, impossible for the same reason.

The absence is the one of the symmetric half as well: the parent product has a left unit and no right one, and the removal of the central part removes the left unit with it. The element $e_t$ remains the only candidate, and it fails on the side on which the parent product fails.

## The Basis and the Sixteen Brackets

**The table.** On the complex basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the operation reads, with the row index the left argument and the column index the right one,

| $\diamond$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $0$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $\vec e_z$ | $0$ | $-\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $0$ |

**Proposition.** The table is alternating, its diagonal is zero, and on the pure vectors $\vec e_x,\vec e_y,\vec e_z$ the operation is the negative of the cross product, $\vec e_\mu\diamond \vec e_\nu = -\,\vec e_\mu\times \vec e_\nu$; the two mixed rows and columns, $e_t\diamond \vec e_\nu = \vec e_\nu$ and $\vec e_\nu\diamond e_t = -\vec e_\nu$, carry the two signs of the scalar-vector terms.

*Proof.* Read the explicit form on the basis elements. For the pure vectors the scalar parts vanish and the table is the cross product with a minus sign, $\vec e_x\diamond \vec e_y = -\vec e_z$, $\vec e_y\diamond \vec e_z = -\vec e_x$ and $\vec e_z\diamond \vec e_x = -\vec e_y$ with the antisymmetric images. For the mixed pairs the cross term vanishes, $e_t\diamond \vec e_\nu = \vec e_\nu$ from the term $Q_{1t}\vec Q_2$ and $\vec e_\nu\diamond e_t = -\vec e_\nu$ from the term $-Q_{2t}\vec Q_1$. The diagonal is zero by alternation, and the two entries $\vec e_\mu\diamond \vec e_\mu$ may be read on the explicit form as $0\cdot \vec e_\mu - 0\cdot \vec e_\mu - \vec e_\mu\times \vec e_\mu = 0$.

The sixteen entries are therefore of four kinds: the zero diagonal of four entries; the three mixed entries $e_t\diamond \vec e_\nu$ equal to $\vec e_\nu$; the three reverse mixed entries $\vec e_\nu\diamond e_t$ equal to $-\vec e_\nu$; and the six entries between two distinct pure vectors, the negatives of the cross products. The six pure-vector entries are the components of the table on which the operation is the plain bracket of the vector subspace, and the six mixed entries are what the block adds to it.

## The Square and Its Polarisation

**Proposition (the square vanishes identically).** For every element $\tilde Q_1$,
$$ \boxed{\; \mathfrak{Q}(\tilde Q_1)=\tilde Q_1\diamond\tilde Q_1=0 \;}, $$
and the polarisation of the square vanishes as well,
$$
\beta(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(\mathfrak{Q}(\tilde Q_1+\tilde Q_2)-\mathfrak{Q}(\tilde Q_1)-\mathfrak{Q}(\tilde Q_2)\bigr)=0 ,
\qquad\text{equivalently}\qquad
\tilde Q_1\diamond\tilde Q_2+\tilde Q_2\diamond\tilde Q_1=0 .
$$
The operation is an alternating bilinear form, its quadratic form $\mathfrak{Q}$ is the zero form, and it is
not recovered from its square.

*Proof.* The vanishing of the square is the alternation of the proposition on the explicit form,
$\tilde Q_1\diamond\tilde Q_1=Q_{1t}\vec Q_1-Q_{1t}\vec Q_1-\vec Q_1\times\vec Q_1=0$. The polarised
expression is the sum of the two values $\tilde Q_1\diamond\tilde Q_2$ and $\tilde Q_2\diamond\tilde Q_1$,
which cancel by alternation; equivalently, the polarisation of a quadratic form that is
identically zero is the zero bilinear form. Since the operation is alternating, the values at
equal arguments carry no information about it, and the operation is read from the bilinear form
itself and not from its square.

**Remark (the contrast with the symmetric half).** The square of the symmetric half is the
quaternion form, $\tilde Q_1\star\tilde Q_1=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}e_t$, and its polarisation recovers
the operation, $2\tilde Q_1\star\tilde Q_2=2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$; the square of the block is
zero and its polarisation is zero, so that half carries its quadratic form and this half carries
none. The two readings are the two sides of the same split: the parent product's square is the
central value $\langle\tilde Q_1\rangle_{\natural}e_t$, the symmetric half keeps the scalar part and the block keeps the
rest, and with the scalar part removed the square is lost.

**Remark (the element theory that follows).** The vanishing square is the single fact on which
the element theory of the block rests, and the five companion articles of the form read it. Every
element is a nilpotent, of index two away from the origin (*Square Roots of Zero and the
Nilpotents of the Antisymmetric Quaternionic Algebra*); every nonzero element is a two-sided zero
divisor, with itself as the annihilating partner (*Zero Divisors of the Antisymmetric
Quaternionic Algebra*); the origin is the only idempotent (*Square Roots of One and the
Idempotents of the Antisymmetric Quaternionic Algebra*); and the block has no root of $-1$ and no
root of $+1$, while its roots of $0$ are all the nonzero elements
(*Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
*Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and
*Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). Each of the five
is a reading of the display $\tilde Q_1\diamond\tilde Q_1=0$.

## The Commutator and the Two Halves

**Remark (the operation is a commutator).** The operation is half the quaternionic bracket,

$$
\tilde Q_1\diamond\tilde Q_2 = \tfrac12[\tilde Q_1,\tilde Q_2]_{\natural}, \qquad [\tilde Q_1,\tilde Q_2]_{\natural} = \tilde Q_1^{\natural}\tilde Q_2 - \tilde Q_2^{\natural}\tilde Q_1 ,
$$

and the bracket is alternating, so it is determined by the operation and the operation by it. The block is thus the antisymmetrisation of the quaternionic product in the strict sense of *The Symmetric and Antisymmetric Parts of an Algebra Product*: it is the halved difference of the product and the product with the arguments exchanged, and half the quaternionic bracket is the same object.

The comparison with the plain row is the reason the block is worth its own article. The antisymmetric part of the plain product is the cross product, $\tilde Q_1\wedge\tilde Q_2 = \tfrac12(\tilde Q_1\tilde Q_2 - \tilde Q_2\tilde Q_1) = \vec Q_1\times\vec Q_2$, the operation $\mathrm{APA}$ of the catalogue; it is the one Lie product of the twelve, it is vector valued, and it vanishes whenever either argument is central. The block of this article is what becomes of that antisymmetrisation when the first factor is read through the conjugation: the cross term is reversed, $-\vec Q_1\times\vec Q_2$, and the two mixed terms $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ are added. On the pure vectors alone the two agree up to the sign, $\tilde Q_1\diamond\tilde Q_2 = -\,\vec Q_1\times\vec Q_2$ there, but they do not agree on the whole space, and the mixed terms are exactly what destroys the Jacobi identity that the plain antisymmetrisation keeps.

## The Jacobi Identity

**Proposition (the identity fails).** The operation does not satisfy the Jacobi identity. At the triple $(e_t,\vec e_x,\vec e_y)$ the cyclic sum is

$$
(e_t\diamond \vec e_x)\diamond \vec e_y + (\vec e_x\diamond \vec e_y)\diamond e_t + (\vec e_y\diamond e_t)\diamond \vec e_x = \vec e_x\diamond \vec e_y + (-\vec e_z)\diamond e_t + (-\vec e_y)\diamond \vec e_x = -\vec e_z + \vec e_z - \vec e_z = -\vec e_z ,
$$

which is not zero; so the block is not a Lie algebra, and the failure is the one the catalogue records for it.

*Proof.* The table gives $e_t\diamond \vec e_x = \vec e_x$, $\vec e_x\diamond \vec e_y = -\vec e_z$, $\vec e_y\diamond e_t = -\vec e_y$, and then $\vec e_x\diamond \vec e_y = -\vec e_z$, $(-\vec e_z)\diamond e_t = \vec e_z$ and $(-\vec e_y)\diamond \vec e_x = -\,\vec e_y\diamond \vec e_x$. The last is the negative of $\vec e_y\diamond \vec e_x = \vec e_z$, that is $-\vec e_z$; the three terms sum to $-\vec e_z+\vec e_z-\vec e_z = -\vec e_z$.

The failure is not an accident of the triple. The Jacobi sum is $\mathbb{C}$-trilinear in its three arguments and alternating, so it is determined by its values on the triples of distinct basis elements; and, as the next article of the block computes, it is nonzero exactly on the triples that carry a scalar part and two non-parallel vectors, of which $(e_t,\vec e_x,\vec e_y)$ and its two relatives $(e_t,\vec e_x,\vec e_z)$ and $(e_t,\vec e_y,\vec e_z)$ are the minimal witnesses. On the pure vectors the block is the cross product with a sign, and there it does satisfy the identity; the failure enters through the mixed terms, and it needs a scalar part in one argument and non-parallel vector parts in the other two.

## The Placement Among the Twelve

**Remark (the reconstruction).** The quaternionic row of the catalogue reads

$$
\mathrm{GQA} = \mathrm{SQA} + \mathrm{AQA}, \qquad
\tilde Q_1^{\natural}\tilde Q_2 = \tilde Q_1\star\tilde Q_2 + \tilde Q_1\diamond\tilde Q_2 ,
$$

with $\mathrm{GQA}$ the parent product, $\mathrm{SQA}$ its symmetric half and $\mathrm{AQA}$ the operation of this block, one of the four antisymmetric parts of the twelve (*The 12 Products of the Biquaternion Complex Space*). The other antisymmetric parts are $\mathrm{APA}$, the cross product of the plain row, and $\mathrm{APS}$ and $\mathrm{AQS}$, the two antisymmetric parts of the sesquilinear rows.

**Remark (what is not shared).** The operation is $\mathbb{C}$-bilinear, alternating and vector valued, and it is not one of the two operations of the catalogue that satisfy the identity of their kind, $\mathrm{APA}$ and $\mathrm{SPA}$. It is not $\mathrm{APA}$, which is the cross product on the vector subspace and which satisfies the Jacobi identity; it is not $\mathrm{AQS}$, which differs from it in the slot and in the class; and it is not $\mathrm{SQA}$, which is its symmetric counterpart and produces central values. On the real part of the space the block does not collapse into the cross product: the mixed terms $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ are real there and do not vanish, so the operation remains distinct from $\mathrm{APA}$ and from every other of the twelve.

**Remark (the catalogue's witness).** The catalogue of the twelve records the block in one line, with the witness $(e_t,\vec e_x,\vec e_y)$ and the cyclic sum $-\vec e_z$, and assigns the failure to non-associativity alone, unlike the two sesquilinear failures whose cause is the obstruction of *Lie Algebras of Sesqualgebras*. That reading is the content of the next article of the block, where the cyclic sum is expressed through the associator of the quaternionic product.

## Summary

The antisymmetric quaternionic multiplication is the antisymmetric part of the general quaternionic product, $\tilde Q_1\diamond\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, the quaternionic product with its scalar part removed; it is $\mathbb{C}$-bilinear and alternating, its diagonal vanishes, and half the quaternionic bracket $[\tilde Q_1,\tilde Q_2]_{\natural}$ is the same operation. Its image is the whole vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three, and it contains no nonzero central element; the element $e_t$ is a left identity on the vector subspace and the negative of the identity on the right, and the operation has no unit on either side. On the basis the sixteen brackets split into the zero diagonal, the mixed entries $e_t\diamond \vec e_\nu=\vec e_\nu$ and $\vec e_\nu\diamond e_t=-\vec e_\nu$, and the six entries between distinct pure vectors, which are the negatives of the cross products. The operation fails the Jacobi identity, with the witness $(e_t,\vec e_x,\vec e_y)$ whose cyclic sum is $-\vec e_z$, and it is one of the four antisymmetric parts of the twelve that are not Lie products; its failure enters through the mixed scalar-vector terms, since on the pure vectors alone it is the cross product up to sign, and it satisfies the identity there. The square $\tilde Q_1\diamond\tilde Q_1$ vanishes identically, so the quadratic form of the operation is the zero form, its polarisation carries no information, and the whole element theory of the block follows: every element is a nilpotent, the origin is the only idempotent, every nonzero element is a two-sided zero divisor, and the block has no root of $-1$ and none of $+1$ while its roots of $0$ are all the nonzero elements. The two halves reconstruct the parent, $\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$, and the failure and its associator defect, the invariant forms, the remarkable subspaces, the operators and the matrix models are the articles that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_\mu^2=-e_t$ |
| ${}^{\natural}$ | the quaternion conjugation, $e_t\mapsto e_t$, $\vec e_\mu\mapsto -\vec e_\mu$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product (the parent product) |
| $\tilde Q_1\diamond\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$ | the symmetric quaternionic multiplication, the operation $\mathrm{SQA}$ |
| $[\tilde Q_1,\tilde Q_2]_{\natural}=\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1$ | the quaternionic bracket, twice the operation of the block |
| $\vec Q_1$ | the vector part of $\tilde Q_1$, so that $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ |
| $\vec Q_1\times\vec Q_2$ | the cross product of the vector parts, defined by $\vec e_\mu\times \vec e_\nu=\vec e_\lambda$ cyclically |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the image of the operation |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the centre, disjoint from the image apart from $0$ |
| $\mathrm{GQA},\mathrm{SQA},\mathrm{AQA}$ | the three operations of the quaternionic row of the catalogue |
| $(e_t,\vec e_x,\vec e_y)$ | the witness of the failure of the Jacobi identity, cyclic sum $-\vec e_z$ |

## Further Reading

- [The Symmetric and Antisymmetric Parts of an Algebra Product](the-symmetric-and-antisymmetric-parts-of-an-algebra-product.html), for the splitting that produces the operation and for the Lie-admissible algebras
- [Introduction to the Symmetric Quaternionic Algebra](introduction-to-the-symmetric-quaternionic-algebra.html), for the other half of the split and the same reconstruction from its own side
- [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra.html), for the parent product, its left unit and its operators
- [The 12 Products of the Biquaternion Complex Space](the-12-products-of-the-biquaternion-complex-space.html), for the placement of the block among the twelve operations
- [Norm and Invertibility in the Antisymmetric Quaternionic Algebra](norm-and-invertibility-in-the-antisymmetric-quaternionic-algebra.html), [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html) and [Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the element theory that the vanishing square forces
- [The Specificities of the Antisymmetric Quaternionic Algebra](the-specificities-of-the-antisymmetric-quaternionic-algebra.html), for the criterion of the block, the projector class and the comparison of the twelve in one table
- [The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra](the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.html), for the cyclic sum, its explicit formula and the associator criterion
- [The Associator and the Ternary Product of the Quaternionic Product](the-associator-and-the-ternary-product-of-the-quaternionic-product.html), for the associator of the parent product, the defect of the block
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the remarkable subspaces read in the following articles of the block
