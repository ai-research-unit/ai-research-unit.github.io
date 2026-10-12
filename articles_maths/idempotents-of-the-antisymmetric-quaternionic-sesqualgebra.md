# __Idempotents of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

An idempotent of a product is an element that the product leaves fixed, $\tilde\Pi\star\tilde\Pi=\tilde\Pi$, and the notion is relative to the product in the same way as the unit, the inverse and the zero divisor: it is the equation and not the element that names the class. For the conjugate cross product

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}}
$$

of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* the equation is decided by two readings of one element. The value has zero scalar part and vanishes on the elements whose vector part is a complex multiple of a real vector, so an idempotent must have a vanishing scalar coordinate and must be a fixed point of a map whose values lie in the three real dimensional subspace of the purely imaginary real vectors; the intersection is trivial, and the conclusion is that **the block has no nontrivial idempotent**: its idempotent set is the origin alone.

The consequence is the absence of the whole projector calculus of the corpus. The idempotent is the carrier of the orthogonal families, of the primitive idempotents and of the Peirce decomposition, of the pure states and of the sandwich; the block carries none of them, and it carries none of them for one reason, which is the vanishing of the diagonal on the centre and its concentration on a cone. The absence is not an accident of the class either: among the twelve, the idempotent set is reduced to the origin for exactly the four antisymmetric parts, and the block is one of the four.

The article states the definition for a general product, then the idempotent set of the block with its proof, then the witnesses of the absence, then the consequences and the comparison. The definition and the classes it carries are *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*; the idempotent sets of the four general products are *The Zero Divisors and the Twelve Structures*, §*The Square, the Idempotents and the Units*; the transfer from the roots of $+1$ that is unavailable here is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Sesqualgebra*; the operators that would carry a projector are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*; and the law that governs the vanishing of the diagonal is the criterion of *The Specificities of the Antisymmetric Quaternionic Sesqualgebra*.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$ and $e_k^2=-e_0$, a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$, and the product $\diamond$ for the block. The value of the block is written $\mathbf{P}\times\overline{\mathbf{Q}}$ and the square $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}$; the subspace of the purely imaginary real vectors is $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$, of real dimension three.

## The Definition, Relative to a Product

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The origin is an idempotent of every product, and, when the product is unital, the unit is an idempotent of it; the two are the **trivial idempotents** of the product, and the others are **nontrivial**. The set of the idempotents of $\star$ is its **idempotent set**, and the definition is the one of *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*.

The same section carries the classes that the idempotent supports in an associative product: the **orthogonal** idempotents, with $\tilde\Pi\star\tilde\Pi'=\tilde\Pi'\star\tilde\Pi=0$; the **pairwise orthogonal** families and the families whose sum is the unit; the **primitive** idempotent, which is not a sum of two nonzero orthogonal ones; and the **Peirce decomposition** attached to a pairwise orthogonal family summing to the unit. Throughout this article the product is the block $\diamond$, so that, unqualified, an idempotent is an idempotent of the block, and the trivial idempotents are the origin and, were it one, the unit; the unit of the block does not exist, so the only trivial idempotent of the block is the origin.

**Remark (the class of the equation).** For a sesquilinear product the equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is not linear in $\tilde\Pi$ and is not conjugate-linear either, since the left side is conjugate-linear in its second slot while the right side is linear; the equation is therefore read on the two coordinates separately. For the block the two readings are the scalar coordinate, which vanishes identically on the left side, and the vector coordinate, which takes its values in the three real dimensional subspace of the purely imaginary real vectors; the two readings decide the set.

## The Idempotent Set of the Block

**Theorem.** The idempotent set of the block is the origin: an element $\tilde\Pi$ satisfies $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ if and only if $\tilde\Pi=0$. The block has no nontrivial idempotent.

*Proof.* Let $\tilde\Pi$ satisfy $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$. Comparing the scalar parts gives $0=\Pi_0$, since the scalar part of every value of the block is zero. Comparing the vector parts gives $\boldsymbol{\Pi}\times\overline{\boldsymbol{\Pi}}=\boldsymbol{\Pi}$, so $\boldsymbol{\Pi}$ is a value of the square and lies in $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$: write $\boldsymbol{\Pi}=i\mathbf{w}$ with $\mathbf{w}$ a real vector. Then $\overline{\boldsymbol{\Pi}}=-i\mathbf{w}$ and

$$
\boldsymbol{\Pi}\times\overline{\boldsymbol{\Pi}}=(i\mathbf{w})\times(-i\mathbf{w})=-i^{2}\,(\mathbf{w}\times\mathbf{w})=0 ,
$$

so $\boldsymbol{\Pi}=0$ and $\tilde\Pi=0$. The converse is the statement $0\diamond0=0$, which holds in every product.

**Remark (the two conditions and their witnesses).** The two conditions of the proof are both necessary and each has a witness. The first is the vanishing of the scalar coordinate, and the witness of its failure is the unit of the parent algebra: $\mathrm{Sc}(e_0\diamond e_0)=0\neq1$, so $e_0$ is not an idempotent of the block. The second is the vanishing of the vector part, once the scalar part is read, and the witness of its failure is the element $e_1+ie_2$, whose square is $-2ie_3$: the vector part of the square is nonzero, so the element is not fixed. The two witnesses are the two elementary ones of the diagonal, and they are the ones *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* uses.

**Remark (the failure is not a near miss).** The theorem is not a statement about the equation having few solutions; it is the statement that the image of the square map and the fixed locus meet at the origin alone. The image is the three real dimensional subspace of the purely imaginary real vectors, whose intersection with the central line is the origin; the square of an element with vanishing scalar coordinate is a value of that subspace, and the equation asks that value to be the element itself, so the value is an element of that subspace equal to its own square: an element $i\mathbf{w}$ of the subspace has the square $(i\mathbf{w})\times\overline{(i\mathbf{w})}=0$, and the value is the origin. The subspace of the purely imaginary real vectors is contained in the cone of the diagonal, so it is not the cone that must be cut down but the squaring that must vanish. The failure is therefore structural: the block has no fixed point of its square outside the origin, and the whole family of candidate projectors of the parent products misses the block.

## The Witnesses of the Absence

**The parent unit is a square-zero element.** The sharpest witness is $\tilde\Pi=e_0$: the unit of the four general products and of the two algebras satisfies $e_0\diamond e_0=0$ in the block, so it is not an idempotent but a nilpotent, and the sharpest possible. The whole central line shares the reading: $\lambda e_0\diamond\lambda e_0=0$ for every complex $\lambda$, so no scalar is an idempotent of the block and the block has no idempotent in the centre other than the origin.

**The idempotents of the plain product are outside the block.** The idempotents of the plain product are the halved roots of $+1$, the elements $\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$, of scalar part $\tfrac12$; equivalently they are the elements $\tfrac12(e_0+\tilde\Xi i)$ with $\tilde\Xi$ a root of $-1$, the form of the corpus. Every idempotent of the block has scalar part $0$ by the first condition of the proof, and the two sets therefore meet nowhere: evaluated with the block, the family $\tfrac12(e_0+\tilde\Xi)$ gives

$$
\tfrac12(e_0+\tilde\Xi)\diamond\tfrac12(e_0+\tilde\Xi)=\tfrac14\,\boldsymbol{\tilde\Xi}\times\overline{\boldsymbol{\tilde\Xi}},
$$

a value of the block, which is not the element and is not even a fixed point of the square in general. The family is thus carried by the block onto its cone of square-zero elements when the vector part of the root is a complex multiple of a real direction, and onto nonzero values otherwise; in neither case is it an idempotent of the block.

**The operator reading.** A projector is an idempotent read as an operator, and the left multiplication of the block by an idempotent would be its own square. The only idempotent is the origin, whose left multiplication is the zero operator, so the only projector of the block is the zero operator, and the block projects onto nothing. The left multiplications of the block are conjugate-linear and their compositions are complex-linear, so the operator calculus of the algebras of the corpus is not available to them in any case, as *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* shows.

## The Consequences of the Absence

**No nontrivial idempotent, no orthogonal family, no Peirce decomposition.** The orthogonal families of the corpus are families of idempotents, and the block has one idempotent, so every family it carries is the family of the single trivial idempotent, whose sum is not the unit; the Peirce decomposition attached to such a family degenerates, and the block has no decomposition of that kind. The block is not associative in any case, so the Peirce calculus of an associative product is out of its reach for a second reason, and the two reasons agree on the answer.

**No pure state.** A pure state of a product is read through a nontrivial idempotent, and the block has none, so the block carries no pure state; the central line of the parent products, which is where the functionals of the block are read, has no idempotent to support one, and the trace form of the block vanishes identically, so the form-theoretic route to a state is unavailable as well, as *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra* records.

**The transfer from the roots of $+1$ is unavailable.** The definitions of the corpus carry the idempotents of the plain product from the roots of $+1$ by the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$, and the transfer presupposes a unit and a value of the algebra. The block has no unit and its roots of $+1$ are empty, so the transfer has nothing to carry; the idempotent set is computed directly, as above, and the reading of the three central values is the one of *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Sesqualgebra*.

**The block is a pure deformation and not a projection.** The element theory of the block sits on one side of the split only: the diagonal maps the whole space into the cone of the complex multiples of the real directions and the value part lies in the vector subspace, so the block moves every nonzero element away from itself and the fixed locus collapses. The word projector, in the block, would name an operator onto a subspace that does not exist.

## The Comparison with the Other Products

The idempotent sets of the four general products are known and are recorded in the corpus; the block is compared with them and with the two symmetric halves of its own row below.

| product | idempotent set | the source |
|---|---|---|
| $\tilde P\tilde Q$ | the plain family $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$, and the trivial ones | *The Zero Divisors and the Twelve Structures* |
| $\tilde P^{\natural}\tilde Q$ | the trivial idempotents alone | the same |
| $\tilde P\tilde Q^{*}$ | the Hermitian idempotents | the same |
| $\tilde P^{\natural}\tilde Q^{*}$ | the family $-\tfrac12e_0+\mu$ | the same |
| the block $\mathbf{P}\times\overline{\mathbf{Q}}$ | the origin alone | above |

Read on the twelve, the table has one more regularity: **the four antisymmetric parts are exactly the four products whose idempotent set is the origin alone.** The plain, the natural, the plain sesquilinear and the quaternionic sesquilinear products all carry idempotents, and their symmetrised halves all carry the unit $e_0$; two of the four symmetrised halves carry the whole family of the parent — the symmetric plain algebra carries the plain family, and the symmetric quaternionic sesqualgebra carries the family $-\tfrac12e_0+\mu$ — while the symmetric natural algebra and the symmetric plain sesqualgebra carry the two trivial idempotents alone, the Hermitian idempotents of the plain sesquilinear product being moved off themselves by the antisymmetrisation; the four antisymmetrised halves — the antisymmetric plain algebra, the antisymmetric plain sesqualgebra, and the two blocks of the rows, of which the block is the quaternionic one — carry none.

**Remark (the unit of the row is a nilpotent of the block).** Within the row the inversion is sharp. The unit $e_0$ is an idempotent of the general quaternionic sesquilinear product and of its symmetric half, and it is a square-zero element of the block; the idempotents of the row are the objects the block turns into the objects of its own cone. The reading is the element-theoretic form of the antithesis between the two halves, and it is stated as such in *The 12 Products of the Biquaternion Complex Space*.

## Summary

The idempotent set of the block is the origin alone: the block has no nontrivial idempotent, and the equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is satisfied by the origin and by nothing else. The proof reads the two coordinates of the value: the scalar part of the square vanishes, so an idempotent has vanishing scalar coordinate, and its vector part is a fixed point of the square, hence a value of the square, hence lies in the three real dimensional subspace of the purely imaginary real vectors; an element $i\mathbf{w}$ of that subspace has the square $(i\mathbf{w})\times\overline{(i\mathbf{w})}=(i\mathbf{w})\times(-i\mathbf{w})=0$, so the only fixed point of the square is the origin, and the subspace contains no nontrivial idempotent of the block. The witnesses of the absence are the parent unit $e_0$, which the block sends to zero, and the elements $e_1+ie_2$ and $\tfrac12(e_0+\tilde\Xi)$, whose squares are not themselves. The consequences are the absence of the projector calculus, of the orthogonal families, of the Peirce decomposition and of the pure states, and the unavailability of the halving transfer from the roots of $+1$. Among the twelve products the block is one of the four antisymmetric parts, and those four are exactly the products whose idempotent set is the origin alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ | the idempotent equation of the block |
| $\mathrm{Sc}(\tilde X\diamond\tilde X)=0$ | the first condition, forcing $\Pi_0=0$ |
| $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | the image of the square, where the vector part of an idempotent must lie |
| $\mathbf{X}$ a complex multiple of a real vector | the cone of the diagonal, on which the square vanishes |
| $e_0$ | an idempotent of the parent products, a square-zero element of the block |
| $e_1+ie_2$ | not fixed by the square, its square being $-2ie_3$ |
| $\tfrac12(e_0+\tilde\Xi)$ | the idempotents of the plain product, outside the idempotent set of the block |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*, for the idempotent, the orthogonal families, the primitive idempotent and the Peirce decomposition, for a general product.
- *Idempotents of the General Plain Algebra*, for the model block, where the idempotents are the halves of the roots of $+1$.
- *The Zero Divisors and the Twelve Structures*, for the idempotent sets of the four general products and their comparison.
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Sesqualgebra*, for the absent halving map and the empty roots of $+1$.
- *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*, for the cone on which the square vanishes and for the parent unit as a nilpotent.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, for the left multiplications and their conjugate-linearity.
- *The 12 Products of the Biquaternion Complex Space*, for the twelve products read as the structures they define.
