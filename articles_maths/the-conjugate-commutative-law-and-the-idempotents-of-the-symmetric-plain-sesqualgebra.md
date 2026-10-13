# __The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0 = H(\tilde P,\tilde Q)e_0$ on the biquaternion space, the Hermitian form $H$ read as a multiplication (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article develops the **law** that the operation forces, which is not commutativity but **conjugate-commutativity**, and it reads the law through the two involutions of the sesqualgebra and against the law of the sibling symmetric blocks. The objects the law determines — the idempotents, the annihilator and the square-zero elements — are stated here only as consequences and are proved in their own articles of the block: *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, *Zero Divisors of the Symmetric Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra*.

The result that organises the article is that the law and the symmetry of the form are one statement. Because every value of the product is central, the law can only be conjugate-commutativity — a commutativity read through the conjugation of the central value — and it reads on the form as the Hermitian symmetry $H(\tilde P,\tilde Q) = \overline{H(\tilde Q,\tilde P)}$. On the centre the product is $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$, the multiplication of the field by its conjugate, and the idempotent equation there is $\lvert\lambda\rvert^{2} = \lambda$, whose roots are $0$ and $1$; the reduction is *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*.

Two further consequences are drawn, both of them consequences of the definiteness of the form. The **two-sided annihilator** of the block is zero, because $H$ is non-degenerate; and there is **no nonzero element of square zero**, because the form is strictly positive at the two equal arguments off the origin. Both statements are the exact opposites of the quaternionic row, where the form is indefinite and the quadratic map kills nonzero elements. They are proved in *Zero Divisors of the Symmetric Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra*. The article closes with the comparison of the law in the sibling symmetric blocks and with the criterion that comparison feeds, in *The Specificities of the Symmetric Plain Sesqualgebra*.

**Boundaries.** The product, its class, its table and the failure of the Jordan identity are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*, and the form $H$, its positivity and its cone are *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; this article cites both and restates neither. The **idempotents** of the block are *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, its **zero divisors and annihilators** are *Zero Divisors of the Symmetric Plain Sesqualgebra*, and its **nilpotents** are *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra*; this article cites them and does not restate them. The comparison blocks are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* for $\mathrm{SPA}$, *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* for $\mathrm{SQA}$ and *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* for $\mathrm{SQS}$, and the criterion they feed is *The Specificities of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** As in *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*: $\mathbb{B}$ with basis $e_0,e_1,e_2,e_3$, natural conjugation ${}^{\natural}$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$; the product is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ with $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$.

## The Conjugate-Commutative Law

**Theorem (the law).** For all $\tilde P,\tilde Q$,

$$
\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P} ,
$$

the bar acting on the central coefficient; the operation is **conjugate-commutative** and not commutative.

*Proof.* $H(\tilde Q,\tilde P) = \sum_\mu Q_\mu\overline{P_\mu} = \overline{\sum_\mu P_\mu\overline{Q_\mu}} = \overline{H(\tilde P,\tilde Q)}$, and the value is $\overline{H(\tilde P,\tilde Q)}e_0$, the coefficientwise conjugate of $\tilde P\star\tilde Q$.

**Proposition (the two involutions act, one as an automorphism and one as the reversal).** The natural conjugation preserves the product and the Hermitian conjugation reverses it up to the coefficientwise conjugate:

$$
\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q , \qquad \tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q} = \tilde Q\star\tilde P .
$$

*Proof.* On the coordinates, $(\tilde P^{\natural})_\mu = \varepsilon_\mu P_\mu$ and $(\tilde P^{*})_\mu = \varepsilon_\mu\overline{P_\mu}$ with $\varepsilon = (1,-1,-1,-1)$. Hence $H(\tilde P^{\natural},\tilde Q^{\natural}) = \sum_\mu \varepsilon_\mu P_\mu\,\overline{\varepsilon_\mu Q_\mu} = \sum_\mu \varepsilon_\mu^{2}P_\mu\overline{Q_\mu} = H(\tilde P,\tilde Q)$, since $\varepsilon_\mu = \pm1$ is real; and $H(\tilde P^{*},\tilde Q^{*}) = \sum_\mu \varepsilon_\mu\overline{P_\mu}\,\overline{\varepsilon_\mu\overline{Q_\mu}} = \sum_\mu \varepsilon_\mu^{2}\overline{P_\mu}\,Q_\mu = \overline{H(\tilde P,\tilde Q)}$. The second equality of the display is the conjugate-commutative law.

**Remark (why the two involutions differ).** The natural conjugation is $\mathbb{C}$-linear and acts as an automorphism of the block; the Hermitian conjugation carries the conjugate-linear slot into the linear one, so it reverses the two arguments and conjugates the central value. In the plain bilinear product the roles are the other way round: there the natural conjugation alone is the antiautomorphism, and the product carries no conjugation of the base field.

**Remark (why the law is conjugate and not plain).** A plain commutativity $\tilde P\star\tilde Q = \tilde Q\star\tilde P$ reads $H(\tilde P,\tilde Q) = H(\tilde Q,\tilde P)$, a form that is symmetric rather than Hermitian; the block instead satisfies $H(\tilde P,\tilde Q) = \overline{H(\tilde Q,\tilde P)}$, which is exactly the Hermitian symmetry of the form. The law of the product and the symmetry of the form are one statement. This is the reason the block is conjugate-commutative while the symmetric plain block, whose form $P_0Q_0 - (\mathbf P,\mathbf Q)$ is symmetric, is commutative.

## The Idempotents

The idempotents of the block, the elements with $\tilde Q\star\tilde Q = \tilde Q$, are exactly $0$ and $e_0$, and the reduction is the one the law forces. The square is central, so an idempotent lies in the centre, where the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$; the equation there reads $\lvert\lambda\rvert^{2} = \lambda$, whose roots are $0$ and $1$, and $e_0$ is an idempotent and not a unit, since $\tilde Q\star e_0 = Q_0e_0$ and $e_0\star\tilde Q = \overline{Q_0}e_0$ reproduce no element with a vector part. The classification, its proof and the comparison with the two central siblings are *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*; the present article records the reduction because the law is read through the field rule of the centre, and cites the rest.

## The Annihilator and the Square-Zero Elements

The two-sided annihilator of the block is $\{0\}$, because the form $H$ is non-degenerate, and the block has no nonzero square-zero element, because the diagonal of $H$ is strictly positive off the origin; it does have vanishing products of nonzero elements, $e_\mu\star e_\nu = 0$ for $\mu\neq\nu$, the value vanishing exactly on the orthogonal pairs. The two statements are proved in *Zero Divisors of the Symmetric Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra*, where the index-three nilpotents are also read; this article cites them and does not restate them, and it records only that both are consequences of the definiteness of $H$, the property the law shares with the form.

## The Comparison with the Sibling Symmetric Blocks

**The law.** The law together with the unit separates the block from the two bilinear parts $\mathrm{SPA}$ and $\mathrm{SQA}$. The two bilinear blocks are both commutative, and the sesquilinear one is conjugate-commutative; among the two commutative blocks only the plain one has a unit.

| block | product | field of scalars | law | unit | form |
|---|---|---|---|---|---|
| $\mathrm{SPA}$ | $\tilde P\bullet\tilde Q$ | $\mathbb{C}$-bilinear | commutative | $e_0$ two-sided | $P_0Q_0 - (\mathbf P,\mathbf Q)$ |
| $\mathrm{SQA}$ | $N(\tilde P,\tilde Q)e_0$ | $\mathbb{C}$-bilinear | commutative | none | $P_0Q_0 + (\mathbf P,\mathbf Q)$ |
| $\mathrm{SPS}$ | $H(\tilde P,\tilde Q)e_0$ | sesquilinear | conjugate-commutative | none | $P_0\overline{Q_0} + (\mathbf P,\overline{\mathbf Q})$ |

The symmetric plain block is the one with a unit and the one whose product has a vector part; the two central blocks have neither, because the identity of a central-valued product cannot reproduce a vector part. The laws are *commutative*, *commutative*, *conjugate-commutative*, and the idempotents follow: the plain block has the two families $\tfrac12(e_0 + \tilde\Xi i)$ attached to the square roots of $-1$ (*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*), the two central blocks have only $0$ and $e_0$ (*Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

**The two conjugate-commutative blocks.** The law does not separate the block from the *other* sesquilinear symmetric part of the twelve, the symmetric quaternionic sesquilinear block $\mathrm{SQS}$, which is conjugate-commutative as well; the two are separated by the image and by the form. There the value is
$$
\mathrm{SQS}(\tilde P,\tilde Q) = K(\tilde P,\tilde Q)e_0 - P_0\overline{\mathbf Q} - \overline{Q_0}\,\mathbf P , \qquad K(\tilde P,\tilde Q) = P_0\overline{Q_0} - (\mathbf P,\overline{\mathbf Q}) ,
$$
with a non-central value that lies in no subspace of the remarkable subspaces and an indefinite scalar form $K$, while here the value is the central $H(\tilde P,\tilde Q)e_0$ and the form $H$ is definite. The two blocks share everything else at the level of the law: both are sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, both satisfy $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$, and neither has a unit. The difference is the sign carried by the vector part of the parent pairing, which the plain block cancels and the quaternionic block keeps; the same sign swaps the definite diagonal $H(\tilde Q,\tilde Q) = \sum_\mu\lvert Q_\mu\rvert^{2}$ for the indefinite $K(\tilde Q,\tilde Q) = \lvert Q_0\rvert^{2} - \lvert\mathbf Q\rvert^{2}$ (*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*).

**The readings through the involutions.** The plain block is $\mathbb{C}$-bilinear, and the natural conjugation is an antiautomorphism of the plain product, hence an **automorphism** of the symmetric block, $(\tilde P\bullet\tilde Q)^{\natural} = \tilde P^{\natural}\bullet\tilde Q^{\natural}$; there is no conjugation of the base field, and so no second reading. The sesquilinear-central block carries that conjugation, and its law has the two readings, $\tilde P\star\tilde Q = \tilde P^{\natural}\star\tilde Q^{\natural}$, an automorphism, and $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q}$, the reversal. The pair of readings is the mark that the product carries the conjugation of the base field.

**The idempotents and the projections.** The idempotents of the block are the two central ones and they are also its projections; the classification, the failure of the bijection with the roots of $-1$ and the comparison with the sibling blocks are *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, and the idempotent theory of the general plain sesquilinear product, of which the two are the restriction, is *Idempotents of the General Plain Sesqualgebra*. The element $e_0$ is a projection of the block and of the plain product at once, being the nontrivial idempotent of the one and the identity of the other, and it is a unit of the plain product and not of the block, which is the whole difference.

## Worked Examples

**The centre.** On the centre the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$, the multiplication of $\mathbb{C}$ by its conjugate. Its idempotents are $0$ and $1$, its involutive automorphisms are the two, and the conjugate-commutative law is the statement that $z\overline{w} = \overline{w\overline{z}}$.

**A Hermitian element.** For $\tilde Q = e_0 + ie_3$ one has $\tilde Q\star\tilde Q = H(\tilde Q,\tilde Q)e_0 = 2e_0$, so $\tilde Q$ is not an idempotent: the square is central while $\tilde Q$ is not, and idempotence in the block is a condition on the central elements alone.

**An element of square zero searched in vain.** Take $\tilde Q = e_0 + ie_1$, the zero divisor of the plain product. Its diagonal is $H(\tilde Q,\tilde Q) = 2$, so $\tilde Q\star\tilde Q = 2e_0 \neq 0$: an element that is a zero divisor of the algebra is a unit-like element of the block, in the sense that its square is nonzero. The block and the algebra disagree on the element.

## Summary

The symmetric plain sesqualgebra satisfies the **conjugate-commutative law** $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$, read through the coefficientwise conjugation of the central value; the law and the Hermitian symmetry of the form $H$ are one statement. The natural conjugation acts as an **automorphism** of the block, $\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q$, and the Hermitian conjugation as the **reversal**, $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q} = \tilde Q\star\tilde P$. On the centre the law is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$, the multiplication of $\mathbb{C}$ by its conjugate. In the comparison of the sibling blocks the law is commutative, commutative, conjugate-commutative, and the plain block alone has a unit: the plain product carries a vector part, the two central products do not. The other conjugate-commutative block, $\mathrm{SQS}$, is not separated by the law but by the image and the form: its value carries a vector part and its scalar form $K$ is indefinite, where here the value is central and $H$ is definite, and the separation of the twelve by the law and the image is the criterion of *The Specificities of the Symmetric Plain Sesqualgebra*. The idempotents, the annihilator and the square-zero elements that the law forces, and the index-three nilpotents beyond the square, are *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, *Zero Divisors of the Symmetric Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form of the block |
| $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$ | the conjugate-commutative law |
| $\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q$, $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q}$ | the two involutions: automorphism and reversal |
| $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ | the product on the centre, the field rule the law is read through |
| $\{0, e_0\}$ | the idempotents, read in *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra* |
| $\{0\}$ | the two-sided annihilator, read in *Zero Divisors of the Symmetric Plain Sesqualgebra* |
| $\mathrm{Vect}(\mathbb{B})$ | the index-three nilpotents, read in *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra* |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class, its table and the failure of the Jordan identity.
- *The Specificities of the Symmetric Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-symmetric-plain-sesqualgebra.md`), for the criterion of the law and the centrality against which the eleven other structures are tested.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form read as the product, its Gram matrix, its positivity and its restriction to the remarkable subspaces.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the norm, the definiteness and the absence of a unit.
- *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the idempotents $0$ and $e_0$, the field rule of the centre and the halving map from the roots of one.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`), for the punctured-space zero-divisor set and the annihilators.
- *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-sesqualgebra.md`), for the index-three nilpotents of the vector subspace and the absence of square-zero elements.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the cone generated by the squares of the block.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.md`), the commutative unital sibling and its two idempotent families.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), the central sibling with an indefinite form, whose isotropic elements are the zero divisors.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), the other conjugate-commutative block of the twelve, whose law is compared with this one's and whose value carries a vector part.
