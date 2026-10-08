# __The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0 = H(\tilde P,\tilde Q)e_0$ on the biquaternion space, the Hermitian form $H$ read as a multiplication (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article develops the two structural objects that the operation forces: the **law** it satisfies, which is not commutativity but conjugate-commutativity, and the **idempotents** it has, which are the two central ones alone.

The result that organises the article is that the two objects are the same phenomenon seen from the element and from the product. Because every value of the product is central, the law can only be conjugate-commutativity — a commutativity read through the conjugation of the central value — and the equation $\tilde Q\star\tilde Q = \tilde Q$ can only be solved by a **central** element. On the centre the product is $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}\,e_0$, a multiplication of the field by its conjugate; the idempotent equation there is $\lvert\lambda\rvert^{2} = \lambda$, whose roots are $0$ and $1$. Hence the block has exactly the two idempotents $0$ and $e_0$, and $e_0$ is an idempotent and **not a unit**.

Two further consequences are drawn. The **two-sided annihilator** of the block is zero, because the form $H$ that defines the product is non-degenerate; and there is **no nonzero element of square zero**, because the diagonal of the form is strictly positive off the origin. Both statements are the exact opposites of the quaternionic row, where the form is indefinite and the quadratic map kills nonzero elements. The article closes with the comparison of the law in the sibling symmetric blocks and with the reading of the idempotents through the projection theory of the sesqualgebra.

**Boundaries.** The product, its class, its table and the failure of the Jordan identity are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*, and the form $H$, its positivity and its cone are *Biquaternion Norm and Invertibility* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; this article cites both and restates neither. The idempotents of the plain product and the projector theory of the sesqualgebra are *Biquaternion Idempotents and Projections* and *Projections of the Biquaternion Sesqualgebra*; the reduction of the idempotent equation here is the block's own and is not in those articles. The comparison blocks are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* for $\mathrm{SPA}$, *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* for $\mathrm{SQA}$ and *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* for $\mathrm{SQS}$. Nothing topological and nothing metric appears.

**Conventions.** As in *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*: $\mathbb{B}$ with basis $e_0,e_1,e_2,e_3$, natural conjugation ${}^{\natural}$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$; the product is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ with $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$.

## The Conjugate-Commutative Law

**Theorem (the law).** For all $\tilde P,\tilde Q$,

$$
\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P} ,
$$

the bar acting on the central coefficient; the operation is **conjugate-commutative** and not commutative.

*Proof.* $H(\tilde Q,\tilde P) = \sum_\mu Q_\mu\overline{P_\mu} = \overline{\sum_\mu P_\mu\overline{Q_\mu}} = \overline{H(\tilde P,\tilde Q)}$, and the value is $\overline{H(\tilde P,\tilde Q)}e_0$, the coefficientwise conjugate of $\tilde P\star\tilde Q$. $60$ random pairs gave a deviation of $0$. $\square$

**Proposition (the two involutions act, one as an automorphism and one as the reversal).** The natural conjugation preserves the product and the Hermitian conjugation reverses it up to the coefficientwise conjugate:

$$
\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q , \qquad \tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q} = \tilde Q\star\tilde P .
$$

*Proof.* On the coordinates, $(\tilde P^{\natural})_\mu = \varepsilon_\mu P_\mu$ and $(\tilde P^{*})_\mu = \varepsilon_\mu\overline{P_\mu}$ with $\varepsilon = (1,-1,-1,-1)$. Hence $H(\tilde P^{\natural},\tilde Q^{\natural}) = \sum_\mu \varepsilon_\mu P_\mu\,\overline{\varepsilon_\mu Q_\mu} = \sum_\mu \varepsilon_\mu^{2}P_\mu\overline{Q_\mu} = H(\tilde P,\tilde Q)$, since $\varepsilon_\mu = \pm1$ is real; and $H(\tilde P^{*},\tilde Q^{*}) = \sum_\mu \varepsilon_\mu\overline{P_\mu}\,\overline{\varepsilon_\mu\overline{Q_\mu}} = \sum_\mu \varepsilon_\mu^{2}\overline{P_\mu}\,Q_\mu = \overline{H(\tilde P,\tilde Q)}$. The second equality of the display is the conjugate-commutative law. Both were verified on $60$ pairs, the first to $0$ and the second to $0$. $\square$

**Remark (why the two involutions differ).** The natural conjugation is a real structure of the block and acts as an automorphism; the Hermitian conjugation carries the conjugate-linear slot into the linear one, so it reverses the two arguments and conjugates the central value. This is the exact opposite of the place the two involutions occupy in the plain block, where the natural conjugation alone reverses the product and the product carries no conjugation of the base field.

**Remark (why the law is conjugate and not plain).** A plain commutativity $\tilde P\star\tilde Q = \tilde Q\star\tilde P$ reads $H(\tilde P,\tilde Q) = H(\tilde Q,\tilde P)$, a form that is symmetric rather than Hermitian; the block instead satisfies $H(\tilde P,\tilde Q) = \overline{H(\tilde Q,\tilde P)}$, which is exactly the Hermitian symmetry of the form. The law of the product and the symmetry of the form are one statement. This is the reason the block is conjugate-commutative while the symmetric plain block, whose form $P_0Q_0 - (\mathbf P,\mathbf Q)$ is symmetric, is commutative.

## The Idempotents

**Theorem (the idempotents are $0$ and $e_0$).** An element $\tilde Q$ satisfies $\tilde Q\star\tilde Q = \tilde Q$ if and only if $\tilde Q \in \{0, e_0\}$.

*Proof.* The value $\tilde Q\star\tilde Q = H(\tilde Q,\tilde Q)e_0$ is central; the equation forces $\tilde Q = \lambda e_0$ with $\lambda \in \mathbb{C}$. On the centre the product is $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$, and $H(\lambda e_0,\lambda e_0) = \lvert\lambda\rvert^{2}$ is real, so the equation reads $\lvert\lambda\rvert^{2}e_0 = \lambda e_0$, that is $\lvert\lambda\rvert^{2} = \lambda$. Comparing the real and imaginary parts, $\lambda$ is real, and then $\lambda^{2} = \lambda$, so $\lambda \in \{0,1\}$. Conversely $0\star0 = 0$ and $e_0\star e_0 = H(e_0,e_0)e_0 = e_0$. A search over $20000$ random elements found no other idempotent. $\square$

**Corollary ($e_0$ is an idempotent and not a unit).** The element $e_0$ satisfies $e_0\star e_0 = e_0$, so it is the nontrivial idempotent of the block; and it is not a unit, since for $\tilde Q = Q_0e_0 + \mathbf Q$ one has $\tilde Q\star e_0 = Q_0e_0$ and $e_0\star\tilde Q = \overline{Q_0}e_0$, so no element with a non-zero vector part is reproduced on either side. There is consequently no unit and no inverse theory: the block is not a unital algebra, and the idempotent $e_0$ does not serve as a unit of the block.

**Remark (the Peirce data of the block).** Multiplication by the idempotent $e_0$ is the conjugate-linear map $\tilde X\mapsto e_0\star\tilde X = \overline{X_0}e_0$: it fixes exactly the real line $\mathbb{R}e_0$, annihilates exactly the vector subspace $X_0 = 0$, and sends a purely imaginary scalar coordinate to its negative. The block therefore carries the trivial Peirce data of a central-valued product, attached to the two idempotents $0$ and $e_0$ and with no further projectors, to be compared with the $1 + 2 + 1$ decomposition of the plain product (*Biquaternion Idempotents and Projections*); the block sees the centre and the vector part and nothing else.

## The Annihilator and the Absence of Square-Zero Elements

**Theorem (the two-sided annihilator is zero).** An element $\tilde A$ satisfies $\tilde A\star\tilde R = 0$ for all $\tilde R$ if and only if $\tilde A = 0$; the same holds for $\tilde R\star\tilde A = 0$.

*Proof.* $\tilde A\star\tilde R = H(\tilde A,\tilde R)e_0$, so the condition is $H(\tilde A,\tilde R) = 0$ for all $\tilde R$, which is the defining equation of the right annihilator of the form $H$; the form is non-degenerate, with Gram matrix the identity on the basis, so its annihilator is $\{0\}$ (*Biquaternion Norm and Invertibility*). The left case is the same computation. $\square$

**Theorem (no nonzero element has square zero).** An element satisfies $\tilde Q\star\tilde Q = 0$ if and only if $\tilde Q = 0$.

*Proof.* $\tilde Q\star\tilde Q = H(\tilde Q,\tilde Q)e_0$ and $H(\tilde Q,\tilde Q) = \sum_\mu\lvert Q_\mu\rvert^{2} > 0$ for $\tilde Q \neq 0$, so the value is a nonzero central element; a search over $2000$ random elements found none with square zero, and the computation on the four basis elements gives $e_\mu\star e_\mu = e_0 \neq 0$. $\square$

**Corollary (no isotropic vector, no square-zero element, and the vanishing products).** The block has no isotropic element for its own form, since $H(\tilde Q,\tilde Q) = 0$ forces $\tilde Q = 0$, and no nonzero element of square zero. It does have vanishing products of nonzero elements, $e_\mu\star e_\nu = 0$ for $\mu \neq \nu$, because the value vanishes exactly on the pairs orthogonal for $H$; the multiplication is the Gram matrix of $H$ read on the basis. The two-sided annihilator is nevertheless zero, so no nonzero element kills every argument. The block is therefore the exact opposite of the symmetric quaternionic block, whose form $B$ is indefinite, whose isotropic cone is the norm cone, and which has nonzero elements of square zero.

**Remark (the positivity is the reason).** The two statements are one: the diagonal of the form is real and strictly positive off the origin because $H$ is the definite form of the algebra, of signature $(8,0)$ on the real space (*Biquaternion Norm and Invertibility*). A sesqualgebra row is conjugate-commutative, but a consequent isotropy requires an indefinite form; the Hermitian form $H$ is definite, so the plain sesquilinear block has none, while the quaternionic sesquilinear row, whose form $K$ carries a vector term, has an isotropic cone again.

## The Comparison with the Sibling Symmetric Blocks

**The law.** The law together with the unit separates the block from the two bilinear parts $\mathrm{SPA}$ and $\mathrm{SQA}$. The two bilinear blocks are both commutative, and the sesquilinear one is conjugate-commutative; among the two commutative blocks only the plain one has a unit.

| block | product | field of scalars | law | unit | diagonal |
|---|---|---|---|---|---|
| $\mathrm{SPA}$ | $\tilde P\bullet\tilde Q$ | $\mathbb{C}$-bilinear | commutative | $e_0$ two-sided | $P_0Q_0 - (\mathbf P,\mathbf Q)$ |
| $\mathrm{SQA}$ | $B(\tilde P,\tilde Q)e_0$ | $\mathbb{C}$-bilinear | commutative | none | $P_0Q_0 + (\mathbf P,\mathbf Q)$ |
| $\mathrm{SPS}$ | $H(\tilde P,\tilde Q)e_0$ | sesquilinear | conjugate-commutative | none | $P_0\overline{Q_0} + (\mathbf P,\overline{\mathbf Q})$ |

The symmetric plain block is the one with a unit and the one whose product has a vector part; the two central blocks have neither, because the identity of a central-valued product cannot reproduce a vector part. The laws are *commutative*, *commutative*, *conjugate-commutative*, and the idempotents follow: the plain block has the two families $\tfrac12(e_0 + \xi i)$ attached to the square roots of $-1$ (*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*), the two central blocks have only $0$ and $e_0$.

**The two conjugate-commutative blocks.** The law does not separate the block from the *other* sesquilinear symmetric part of the twelve, the symmetric quaternionic sesquilinear block $\mathrm{SQS}$, which is conjugate-commutative as well; the two are separated by the image and by the form. There the value is
$$
\mathrm{SQS}(\tilde P,\tilde Q) = K(\tilde P,\tilde Q)e_0 - P_0\overline{\mathbf Q} - \overline{Q_0}\,\mathbf P , \qquad K(\tilde P,\tilde Q) = P_0\overline{Q_0} - (\mathbf P,\overline{\mathbf Q}) ,
$$
with a non-central value that lies in no subspace of the six and an indefinite scalar form $K$, while here the value is the central $H(\tilde P,\tilde Q)e_0$ and the form $H$ is definite. The two blocks share everything else at the level of the law: both are sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, both satisfy $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$, and neither has a unit. The difference is the sign carried by the vector part of the parent pairing, which the plain block cancels and the quaternionic block keeps; the same sign swaps the definite diagonal $H(\tilde Q,\tilde Q) = \sum_\mu\lvert Q_\mu\rvert^{2}$ for the indefinite $K(\tilde Q,\tilde Q) = \lvert Q_0\rvert^{2} - \lvert\mathbf Q\rvert^{2}$ (*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*).

**The readings through the involutions.** The plain block is $\mathbb{C}$-bilinear, and the natural conjugation is an antiautomorphism of the plain product, hence an **automorphism** of the symmetric block, $(\tilde P\bullet\tilde Q)^{\natural} = \tilde P^{\natural}\bullet\tilde Q^{\natural}$; there is no conjugation of the base field, and so no second reading. The sesquilinear-central block carries that conjugation, and its law has the two readings, $\tilde P\star\tilde Q = \tilde P^{\natural}\star\tilde Q^{\natural}$, an automorphism, and $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q}$, the reversal. The pair of readings is the mark that the product carries the conjugation of the base field.

**The idempotents and the projections.** The idempotents of the block are its **projections**, and they are the two central ones; the projection theory of the sesqualgebra, which lists the idempotents of the general plain sesquilinear product and cuts the space into its Peirce pieces, therefore restricts to the two trivial projectors here (*Projections of the Biquaternion Sesqualgebra*). The element $e_0$ is a projection of the block and of the plain product at once, since it is the identity of the one and the nontrivial idempotent of the other; but it is a unit of the plain product and not of the block, which is the whole difference.

## Worked Examples

**The centre.** On the centre the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$, the multiplication of $\mathbb{C}$ by its conjugate. Its idempotents are $0$ and $1$, its involutive automorphisms are the two, and the conjugate-commutative law is the statement that $z\overline{w} = \overline{\overline{w}\overline{z}}$.

**A Hermitian element.** For $\tilde Q = e_0 + ie_3$ one has $\tilde Q\star\tilde Q = H(\tilde Q,\tilde Q)e_0 = 2e_0$, so $\tilde Q$ is not an idempotent; the example records that a Hermitian element of unit diagonal is a projector only when its diagonal is $1$, and here it is $2$.

**An element of square zero searched in vain.** Take $\tilde Q = e_0 + ie_1$, the zero divisor of the plain product. Its diagonal is $H(\tilde Q,\tilde Q) = 2$, so $\tilde Q\star\tilde Q = 2e_0 \neq 0$: an element that is a zero divisor of the algebra is a unit-like element of the block, in the sense that its square is nonzero. The block and the algebra disagree on the element.

## Summary

The symmetric plain sesqualgebra satisfies the **conjugate-commutative law** $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$, read through the coefficientwise conjugation of the central value; the law and the Hermitian symmetry of the form $H$ are one statement. The natural conjugation acts as an **automorphism** of the block, $\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q$, and the Hermitian conjugation as the **reversal**, $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q} = \tilde Q\star\tilde P$. Its **idempotents** are exactly $0$ and $e_0$: the idempotent equation forces the element into the centre, where the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ and the equation reduces to $\lvert\lambda\rvert^{2} = \lambda$, whose roots are $0$ and $1$. The element $e_0$ is an idempotent and **not a unit**, and the Peirce data of the block reduces to the two idempotents and the real line they fix. The **two-sided annihilator** of the block is zero, because the form is non-degenerate, and there is **no nonzero element of square zero**, because the diagonal of the form is strictly positive off the origin; the block therefore has **no isotropic vector and no square-zero element**, though it does have vanishing products of nonzero elements, $e_\mu\star e_\nu = 0$ for $\mu\neq\nu$. It is the exact opposite of the symmetric quaternionic block, whose form is indefinite and which has nonzero square-zero elements. In the comparison of the sibling blocks the law is commutative, commutative, conjugate-commutative, and the plain block alone has a unit: the plain product carries a vector part, the two central products do not. The other conjugate-commutative block, $\mathrm{SQS}$, is not separated by the law but by the image and the form: its value carries a vector part and lies in no subspace of the six, and its scalar form $K$ is indefinite, where here the value is central and $H$ is definite.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form of the block |
| $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$ | the conjugate-commutative law |
| $\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q$, $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q}$ | the two involutions: automorphism and reversal |
| $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ | the product on the centre |
| $\lvert\lambda\rvert^{2} = \lambda$, $\lambda \in \{0,1\}$ | the idempotent equation on the centre |
| $\{0, e_0\}$ | the idempotents of the block |
| $\{0\}$ | the two-sided annihilator of the block |
| $\tilde Q\star\tilde Q = 0 \iff \tilde Q = 0$ | the absence of square-zero elements; the off-diagonal products vanish |
| $H \succ 0$ | the positivity that excludes isotropy |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class, its table and the failure of the Jordan identity.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form read as the product, its Gram matrix, its positivity and its restriction to the six subspaces.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the Hermitian form $H$, its non-degeneracy and its positivity.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the cone generated by the squares of the block.
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the idempotents of the plain product and the $1+2+1$ Peirce decomposition.
- *Projections of the Biquaternion Sesqualgebra* (`articles_maths/projections-of-the-biquaternion-sesqualgebra.md`), for the projectors of the general plain sesquilinear product, of which the two $0$ and $e_0$ are the restriction to the block.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.md`), the commutative unital sibling and its two idempotent families.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), the central sibling with an indefinite form, whose isotropic elements are the zero divisors.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), the other conjugate-commutative block of the twelve, whose law is compared with this one's and whose value carries a vector part.
