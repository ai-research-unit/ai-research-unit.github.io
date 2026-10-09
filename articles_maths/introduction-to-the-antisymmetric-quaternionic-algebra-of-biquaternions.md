# __Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions__

## Introduction

The general quaternionic product of the biquaternion algebra $\mathbb{B}$ is $\tilde P^{\natural}\tilde Q$, the plain product with the first factor read through the quaternion conjugation ${}^{\natural}$; it is $\mathbb{C}$-bilinear, it has $e_0$ as a unit on the left only, and it is the quaternionic one of the four general products the $\mathbb{C}$-space carries (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *Introduction to the General Quaternionic Algebra of Biquaternions*). A bilinear product over a field in which $2$ is invertible splits canonically into the sum of a symmetric and an antisymmetric part, the splitting induced by the exchange of the two arguments of the product (*The Symmetric and Antisymmetric Parts of an Algebra Product*). The **antisymmetric quaternionic multiplication** is the antisymmetric part of this product,

$$
\tilde P \diamond \tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P\bigr) = P_0\mathbf Q - Q_0\mathbf P - \mathbf P\times\mathbf Q ,
$$

and it is the operation of the present block. It is the quaternionic product with its scalar part removed: the scalar part of its value is zero, and its vector part is the mixed term $P_0\mathbf Q-Q_0\mathbf P$ with the cross term $-\mathbf P\times\mathbf Q$ added to it. The operation is written $\diamond$, a symbol used inside this block only; the quaternionic bracket of the corpus, $[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$, is twice it.

This article introduces the block. It fixes the class of the operation and its two structural identities, alternation and the vanishing of the diagonal; the image, which is the whole vector subspace $\mathrm{Vect}(\mathbb{B})$ and nothing of the centre; the absence of a unit; the multiplication table of the basis; the identity of the operation with half the quaternionic commutator; the failure of the Jacobi identity, with the witness on which the corpus reads it; and the placement of the block among the twelve operations of the catalogue. The failure and its associator defect, the invariant forms, the six subspaces, the multiplication operators and the two matrix models are the subjects of the five following articles of the block, and none of them is developed here.

The general construction of the two parts of a product is *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the split here is the one instance of it that belongs to the quaternionic row of the catalogue. The two halves reconstruct the parent, $\tilde P^{\natural}\tilde Q = \tilde P\star\tilde Q + \tilde P\diamond\tilde Q$, with the symmetric half the operation of *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*; that article records the same split from its own side, and the two introductions are the two readings of one computation. The algebra, its basis and its conjugation are *Introduction to the General Quaternionic Algebra of Biquaternions* and *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the six distinguished subspaces named below are *Introduction to the Six Subspaces*. The article is algebraic throughout: no norm, no distance, no limit, nothing from the topology, the analysis or the geometry of the chapter.

## The Operation

**Definition.** The **antisymmetric quaternionic multiplication** of $\mathbb{B}$ is

$$
\tilde P \diamond \tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P\bigr),
$$

the antisymmetric part of the general quaternionic product for the exchange of the two arguments. The algebra $\mathbb{B}$ with this product is the **antisymmetric quaternionic algebra** of the block, written here with the same letters as its operation.

**Proposition (the explicit form).** For all $\tilde P = P_0e_0 + \mathbf P$ and $\tilde Q = Q_0e_0 + \mathbf Q$,

$$
\tilde P \diamond \tilde Q = P_0\mathbf Q - Q_0\mathbf P - \mathbf P\times\mathbf Q .
$$

In particular the scalar part of the value is zero and the value lies in the vector subspace $\mathrm{Vect}(\mathbb{B})$; the operation is $\mathbb{C}$-bilinear, alternating, and its diagonal vanishes.

*Proof.* The value of the parent product is $\tilde P^{\natural}\tilde Q = \bigl[P_0Q_0+(\mathbf P,\mathbf Q)\bigr]e_0 + P_0\mathbf Q - Q_0\mathbf P - \mathbf P\times\mathbf Q$ (*The 12 Products of the Biquaternion Complex Space*). The reverse product is obtained by exchanging the arguments, and its value is $[Q_0P_0+(\mathbf Q,\mathbf P)]e_0 + Q_0\mathbf P - P_0\mathbf Q - \mathbf Q\times\mathbf P$. The scalar part is symmetric in the pair and cancels in the difference; the vector part is antisymmetric in the pair, because the cross product reverses and the mixed terms exchange with a sign, and half the difference of the two vector parts is $\tfrac12\bigl[2(P_0\mathbf Q-Q_0\mathbf P) - 2\,\mathbf P\times\mathbf Q\bigr] = P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$, since $\mathbf Q\times\mathbf P = -\mathbf P\times\mathbf Q$. Bilinearity is inherited from the product term by term with the coefficients in $\mathbb{C}$; alternation is the antisymmetry of the definition, $\tilde Q\diamond\tilde P = -\tilde P\diamond\tilde Q$; and the diagonal vanishes at $\tilde P=\tilde Q$, where the two terms of the definition cancel. Equivalently, the scalar part of the explicit form is zero, so the value never leaves $\mathrm{Vect}(\mathbb{B})$; and at $\tilde P = \tilde Q$ the three terms of the explicit form give $P_0\mathbf P-P_0\mathbf P-\mathbf P\times\mathbf P = 0$. $\square$

**Remark (what the operation omits).** The scalar part of the parent product, the $\natural$-form $\langle\tilde P,\tilde Q\rangle_\natural=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$, is exactly the symmetric half. It carries the two terms that the exchange leaves fixed, the square terms $P_0Q_0$ and the scalar product $(\mathbf P,\mathbf Q)$ of the vectors, and the operation of this block is what remains of the parent product once that half is removed. The omission is total: the block never produces a central element, and every value has zero scalar part.

**Proposition (the two reconstructing identities).** For all $\tilde P,\tilde Q$,

$$
\tilde P^{\natural}\tilde Q = \tilde P\star\tilde Q + \tilde P\diamond\tilde Q , \qquad
[\tilde P,\tilde Q]_{\natural} = \tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P = 2\,\tilde P\diamond\tilde Q ,
$$

with $\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q + \tilde Q^{\natural}\tilde P\bigr)$ the symmetric half.

*Proof.* Adding and subtracting the two values of the parent product gives the sum and the difference; the sum is twice the symmetric half and the difference is the quaternionic bracket, twice the antisymmetric half by its definition. $\square$

The block is therefore the second of the two readings of one product: the parent product is recovered from the two halves, and the bracket of the corpus is the unhalved difference. The factor two is the only difference between the operation of this block and the quaternionic bracket, and it is recorded throughout.

## The Image and the Absence of a Unit

**Proposition (the image).** The image of the operation is the vector subspace,

$$
\mathbb{B}\diamond\mathbb{B} = \mathrm{Vect}(\mathbb{B}) = \bigl\{\tilde Q : \tilde Q^{\natural} = -\tilde Q\bigr\} ,
$$

of complex dimension three and real dimension six; the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ is disjoint from the image apart from $0$.

*Proof.* Every value has zero scalar part by the explicit form, so the image lies in $\mathrm{Vect}(\mathbb{B})$. Conversely, for a pure vector $\mathbf V$, the element $e_0$ acts as $\tilde P\mapsto\mathbf P$ from the left, $e_0\diamond\tilde Q = \mathbf Q$, so $\mathbf V = e_0\diamond\mathbf V$ is a value. The centre is the set of elements with zero vector part, and $\mathrm{Vect}(\mathbb{B})$ is the set with zero scalar part, so their intersection is $0$. $\square$

**Remark (the two sides of the identity).** The element $e_0$ is a left identity on the vector subspace, $e_0\diamond\tilde Q = \mathbf Q$, but it is not a two-sided identity there. The right multiplication by $e_0$ is the negative of the identity on the vector subspace, $\tilde P\diamond e_0 = -\mathbf P$, and the two differ by the sign. The asymmetry is the asymmetry of the parent product, which has $e_0$ as a unit on the left only, and it is the reason no element that acts on one side acts on the other. In particular $e_0\diamond\tilde Q = \mathbf Q$ recovers the vector part of $\tilde Q$ and discards the scalar part, so even on the image the left action of $e_0$ is the identity and its right action is its negative.

**Proposition (no unit).** The operation has no unit on the left and none on the right; equivalently, there is no $\tilde E$ with $\tilde E\diamond\tilde X = \tilde X$ for all $\tilde X$, and none with $\tilde X\diamond\tilde E = \tilde X$ for all $\tilde X$.

*Proof.* A left unit $\tilde E$ would give, at $\tilde X = e_0$, the value $\tilde E\diamond e_0 = -\mathbf E$, which would have to equal $e_0$; but $-\mathbf E$ is a pure vector and $e_0$ is not, so there is no left unit. A right unit would give, again at $\tilde X = e_0$, the value $e_0\diamond\tilde E = \mathbf E$, which would have to equal $e_0$, impossible for the same reason. $\square$

The absence is the one of the symmetric half as well: the parent product has a left unit and no right one, and the removal of the central part removes the left unit with it. The element $e_0$ remains the only candidate, and it fails on the side on which the parent product fails.

## The Basis and the Sixteen Brackets

**The table.** On the complex basis $e_0,e_1,e_2,e_3$ the operation reads, with the row index the left argument and the column index the right one,

| $\diamond$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $-e_1$ | $0$ | $-e_3$ | $e_2$ |
| $e_2$ | $-e_2$ | $e_3$ | $0$ | $-e_1$ |
| $e_3$ | $-e_3$ | $-e_2$ | $e_1$ | $0$ |

**Proposition.** The table is alternating, its diagonal is zero, and on the pure vectors $e_1,e_2,e_3$ the operation is the negative of the cross product, $e_j\diamond e_k = -\,e_j\times e_k$; the two mixed rows and columns, $e_0\diamond e_k = e_k$ and $e_k\diamond e_0 = -e_k$, carry the two signs of the scalar-vector terms.

*Proof.* Read the explicit form on the basis elements. For the pure vectors the scalar parts vanish and the table is the cross product with a minus sign, $e_1\diamond e_2 = -e_3$, $e_2\diamond e_3 = -e_1$ and $e_3\diamond e_1 = -e_2$ with the antisymmetric images. For the mixed pairs the cross term vanishes, $e_0\diamond e_k = e_k$ from the term $P_0\mathbf Q$ and $e_k\diamond e_0 = -e_k$ from the term $-Q_0\mathbf P$. The diagonal is zero by alternation, and the two entries $e_j\diamond e_j$ may be read on the explicit form as $0\cdot e_j - 0\cdot e_j - e_j\times e_j = 0$. $\square$

The sixteen entries are therefore of four kinds: the zero diagonal of four entries; the three mixed entries $e_0\diamond e_k$ equal to $e_k$; the three reverse mixed entries $e_k\diamond e_0$ equal to $-e_k$; and the six entries between two distinct pure vectors, the negatives of the cross products. The six pure-vector entries are the components of the table on which the operation is the plain bracket of the vector subspace, and the six mixed entries are what the block adds to it.

## The Commutator and the Two Halves

**Remark (the operation is a commutator).** The operation is half the quaternionic bracket,

$$
\tilde P\diamond\tilde Q = \tfrac12[\tilde P,\tilde Q]_{\natural}, \qquad [\tilde P,\tilde Q]_{\natural} = \tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P ,
$$

and the bracket is alternating, so it is determined by the operation and the operation by it. The block is thus the antisymmetrisation of the quaternionic product in the strict sense of *The Symmetric and Antisymmetric Parts of an Algebra Product*: it is the halved difference of the product and the product with the arguments exchanged, and half the quaternionic bracket is the same object.

The comparison with the plain row is the reason the block is worth its own article. The antisymmetric part of the plain product is the cross product, $\tilde P\wedge\tilde Q = \tfrac12(\tilde P\tilde Q - \tilde Q\tilde P) = \mathbf P\times\mathbf Q$, the operation $\mathrm{APA}$ of the catalogue; it is the one Lie product of the twelve, it is vector valued, and it vanishes whenever either argument is central. The block of this article is what becomes of that antisymmetrisation when the first factor is read through the conjugation: the cross term is reversed, $-\mathbf P\times\mathbf Q$, and the two mixed terms $P_0\mathbf Q-Q_0\mathbf P$ are added. On the pure vectors alone the two agree up to the sign, $\tilde P\diamond\tilde Q = -\,\mathbf P\times\mathbf Q$ there, but they do not agree on the whole space, and the mixed terms are exactly what destroys the Jacobi identity that the plain antisymmetrisation keeps.

## The Jacobi Identity

**Proposition (the identity fails).** The operation does not satisfy the Jacobi identity. At the triple $(e_0,e_1,e_2)$ the cyclic sum is

$$
(e_0\diamond e_1)\diamond e_2 + (e_1\diamond e_2)\diamond e_0 + (e_2\diamond e_0)\diamond e_1 = e_1\diamond e_2 + (-e_3)\diamond e_0 + (-e_2)\diamond e_1 = -e_3 + e_3 - e_3 = -e_3 ,
$$

which is not zero; so the block is not a Lie algebra, and the failure is the one the catalogue records for it.

*Proof.* The table gives $e_0\diamond e_1 = e_1$, $e_1\diamond e_2 = -e_3$, $e_2\diamond e_0 = -e_2$, and then $e_1\diamond e_2 = -e_3$, $(-e_3)\diamond e_0 = e_3$ and $(-e_2)\diamond e_1 = -\,e_2\diamond e_1$. The last is the negative of $e_2\diamond e_1 = e_3$, that is $-e_3$; the three terms sum to $-e_3+e_3-e_3 = -e_3$. $\square$

The failure is not an accident of the triple. The Jacobi sum is $\mathbb{C}$-trilinear in its three arguments and alternating, so it is determined by its values on the triples of distinct basis elements; and, as the next article of the block computes, it is nonzero exactly on the triples that carry a scalar part and two non-parallel vectors, of which $(e_0,e_1,e_2)$ and its two relatives $(e_0,e_1,e_3)$ and $(e_0,e_2,e_3)$ are the minimal witnesses. On the pure vectors the block is the cross product with a sign, and there it does satisfy the identity; the failure enters through the mixed terms, and it needs a scalar part in one argument and non-parallel vector parts in the other two.

## The Placement Among the Twelve

**Remark (the reconstruction).** The quaternionic row of the catalogue reads

$$
\mathrm{GQA} = \mathrm{SQA} + \mathrm{AQA}, \qquad
\tilde P^{\natural}\tilde Q = \tilde P\star\tilde Q + \tilde P\diamond\tilde Q ,
$$

with $\mathrm{GQA}$ the parent product, $\mathrm{SQA}$ its symmetric half and $\mathrm{AQA}$ the operation of this block, one of the four antisymmetric parts of the twelve (*The 12 Products of the Biquaternion Complex Space*). The other antisymmetric parts are $\mathrm{APA}$, the cross product of the plain row, and $\mathrm{APS}$ and $\mathrm{AQS}$, the two antisymmetric parts of the sesquilinear rows.

**Remark (what is not shared).** The operation is $\mathbb{C}$-bilinear, alternating and vector valued, and it is not one of the two operations of the catalogue that satisfy the identity of their kind, $\mathrm{APA}$ and $\mathrm{SPA}$. It is not $\mathrm{APA}$, which is the cross product on the vector subspace and which satisfies the Jacobi identity; it is not $\mathrm{AQS}$, which differs from it in the slot and in the class; and it is not $\mathrm{SQA}$, which is its symmetric counterpart and produces central values. On the real part of the space the block does not collapse into the cross product: the mixed terms $P_0\mathbf Q-Q_0\mathbf P$ are real there and do not vanish, so the operation remains distinct from $\mathrm{APA}$ and from every other of the twelve.

**Remark (the catalogue's witness).** The catalogue of the twelve records the block in one line, with the witness $(e_0,e_1,e_2)$ and the cyclic sum $-e_3$, and assigns the failure to non-associativity alone, unlike the two sesquilinear failures whose cause is the obstruction of *Lie Algebras of Sesqualgebras*. That reading is the content of the next article of the block, where the cyclic sum is expressed through the associator of the quaternionic product.

## Summary

The antisymmetric quaternionic multiplication is the antisymmetric part of the general quaternionic product, $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$, the quaternionic product with its scalar part removed; it is $\mathbb{C}$-bilinear and alternating, its diagonal vanishes, and half the quaternionic bracket $[\tilde P,\tilde Q]_{\natural}$ is the same operation. Its image is the whole vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three, and it contains no nonzero central element; the element $e_0$ is a left identity on the vector subspace and the negative of the identity on the right, and the operation has no unit on either side. On the basis the sixteen brackets split into the zero diagonal, the mixed entries $e_0\diamond e_k=e_k$ and $e_k\diamond e_0=-e_k$, and the six entries between distinct pure vectors, which are the negatives of the cross products. The operation fails the Jacobi identity, with the witness $(e_0,e_1,e_2)$ whose cyclic sum is $-e_3$, and it is one of the four antisymmetric parts of the twelve that are not Lie products; its failure enters through the mixed scalar-vector terms, since on the pure vectors alone it is the cross product up to sign, and it satisfies the identity there. The two halves reconstruct the parent, $\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$, and the failure and its associator defect, the invariant forms, the six subspaces, the operators and the matrix models are the five articles that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2=-e_0$ |
| ${}^{\natural}$ | the quaternion conjugation, $e_0\mapsto e_0$, $e_k\mapsto -e_k$ |
| $\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product (the parent product) |
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | the symmetric quaternionic multiplication, the operation $\mathrm{SQA}$ |
| $[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$ | the quaternionic bracket, twice the operation of the block |
| $\mathbf P$ | the vector part of $\tilde P$, so that $\tilde P=P_0e_0+\mathbf P$ |
| $\mathbf P\times\mathbf Q$ | the cross product of the vector parts, defined by $e_j\times e_k=e_l$ cyclically |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the image of the operation |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, disjoint from the image apart from $0$ |
| $\mathrm{GQA},\mathrm{SQA},\mathrm{AQA}$ | the three operations of the quaternionic row of the catalogue |
| $(e_0,e_1,e_2)$ | the witness of the failure of the Jacobi identity, cyclic sum $-e_3$ |

## Further Reading

- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the splitting that produces the operation and for the Lie-admissible algebras
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the other half of the split and the same reconstruction from its own side
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the parent product, its left unit and its operators
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the placement of the block among the twelve operations
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`), for the cyclic sum, its closed form and the associator criterion
- *The Associator and the Ternary Product of the Quaternionic Product* (`articles_maths/the-associator-and-the-ternary-product-of-the-quaternionic-product.md`), for the associator of the parent product, the defect of the block
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished subspaces read in the following articles of the block
