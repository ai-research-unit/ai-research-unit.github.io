# __Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

The equations $\tilde\Xi\diamond\tilde\Xi=e_0$ and $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ name a product, and the product here is the conjugate cross product

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}}
$$

of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, the operation named $\mathrm{AQS}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$ in the block, the elements $\tilde\Xi$ with $\tilde\Xi\diamond\tilde\Xi=e_0$. The second is the idempotents of the block, the elements $\tilde\Pi$ with $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$. In a unital bilateral product the two subjects are one subject, because the **halving map** $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ carries the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$. The map presupposes the unit $e_0$ and the value $\tfrac12$ of the algebra, and the block has neither a unit nor a halving of its central line; here the transfer has nothing to carry, because the roots of $+1$ are empty in any case, and the two sets are computed directly. The order is the order of the two subjects, the roots of one first and the idempotents after.

**The results.** The block has no root of $+1$: every value of the block is a pure vector, while $e_0$ is central, so the equation $\tilde\Xi\diamond\tilde\Xi=e_0$ has no solution, and neither has $\tilde\Xi\diamond\tilde\Xi=\lambda e_0$ for any nonzero $\lambda$. The failure is total and it is visible on the unit of the parent algebra, $e_0\diamond e_0=0$. The roots of $-1$ are empty as well; they are the closing paragraph of §*The Roots of One*, and they are quoted nowhere else. The idempotent set of the block is the origin alone: the equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is satisfied by the origin and by nothing else, so the block carries no nontrivial idempotent, no orthogonal family, no primitive idempotent, no Peirce decomposition, no pure state and no projection but the zero operator.

**Boundaries.** The roots of $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*; the roots of the general quadratic $\tilde\Xi\diamond\tilde\Xi=\tilde Q$ are *Square Roots of a General Element in the Antisymmetric Quaternionic Sesqualgebra*; the zero-divisor set, which contains the cone of the diagonal, is *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*; the pairing, the operators and the two matrix models are *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, *The Antisymmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* and *The Antisymmetric Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; the general definitions of a root of a central value, of a power and of an idempotent are *Definitions for the Study of the 12 Algebraic Structures*; and the law behind the vanishing of the diagonal is *The Specificities of the Antisymmetric Quaternionic Sesqualgebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, central scalar imaginary $i$ and $e_1e_2=e_3$, so that $e_k^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. A generic element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$ and $Q_k=q_k+iq'_k$, the coefficients $q_k,q'_k$ real. The natural conjugation is ${}^{\natural}$, the star is ${}^{*}={}^{\natural}\circ\bar{\cdot}$, and the bar is $\bar{\cdot}$. The product of the block is written $\diamond$, and the other eleven products are named by the three-letter codes of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The value of the block is $\mathbf{P}\times\overline{\mathbf{Q}}$, the cross product of the vector part of the first argument with the conjugate of the vector part of the second, and the square is $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}$. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\Pi$ (§*The Idempotent Convention*), and a generic element $\tilde P$ or $\tilde Q$.

## The Definition, Relative to a Product

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{B}$ and let $\lambda\in\mathbb{C}$. A **root of $\lambda$ in $\star$** is a nonzero element $\tilde P$ with

$$
\tilde P\star\tilde P=\lambda e_0 ,
$$

the definition of *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*. The roots of $-1$ are the **imaginary units** of $\star$, the roots of $+1$ its **involutions**, and the roots of $0$ its **nonzero square-zero elements**.

Throughout this article the product is the conjugate cross product $\diamond$, so that, unqualified, a root is a root of the block, the equation is read with the square $\tilde\Xi\diamond\tilde\Xi=\mathbf\Xi\times\overline{\mathbf\Xi}$ of the block, and a value is a pure vector. The origin is not a root of any product: the definition requires the element and not only the equation.

**Remark (the class of the equation).** The equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$ is not bilinear in $\tilde\Xi$ for a sesquilinear product; it is the restriction of the sesquilinear form $\tilde\Xi\star\tilde\Xi$ to the diagonal, and for the block the square is conjugate-linear in its second slot, so the equation is not complex-linear and not conjugate-linear either. The roots of one are therefore read by the shape of the value, as §*The Roots of One* does, and not by a linear criterion. The same warning applies to the idempotent equation, read in §*The Idempotents*.

## The Roots of One

**The block has no root of $+1$: for every nonzero $\lambda\in\mathbb{C}$ the equation $\tilde\Xi\diamond\tilde\Xi=\lambda e_0$ has no solution, and the failure is total because the image of the square does not meet the scalar line outside the origin.**

### The Obstruction

**Theorem.** For every nonzero $\lambda\in\mathbb{C}$ the equation $\tilde\Xi\diamond\tilde\Xi=\lambda e_0$ has no solution. In particular the block has no root of $+1$.

*Proof.* The value of the block has zero scalar part, $\mathrm{Sc}(\tilde\Xi\diamond\tilde\Xi)=0$ for every $\tilde\Xi$, because $\tilde\Xi\diamond\tilde\Xi=\mathbf\Xi\times\overline{\mathbf\Xi}$ is a pure vector. The scalar part of $\lambda e_0$ is $\lambda$, so the two sides differ in their scalar part as soon as $\lambda\neq0$.

**Corollary.** The block has no involution. Read with the code of the twelve, it is one of the blocks in which the two solution sets of $\pm1$ are empty: the emptiness is structural for the four antisymmetric parts, whose values are pure vectors. It is not the general rule of the twelve: the general plain product, the general quaternionic product and the general quaternionic sesquilinear product have roots of both $\pm1$, and they carry their imaginary units and their involutions, while the general plain sesquilinear product has a root of $+1$ and none of $-1$, because its scalar form is positive definite.

### The Failure is Total

**Remark (why the failure is total and not partial).** The obstruction is not a square that fails to reach a value; it is that the image of the square does not meet the scalar line at all outside the origin. The square map

$$
\tilde\Xi\longmapsto\tilde\Xi\diamond\tilde\Xi=\mathbf\Xi\times\overline{\mathbf\Xi}
$$

has its values in the vector subspace, and the central line meets that subspace at the origin alone, so the only central value the square can take is $0$. The witness of the failure at $+1$ is the unit itself, $\tilde\Xi=e_0$: the equation $e_0\diamond e_0=e_0$ reads $0=e_0$ and is false. The failure is thus visible on the unit of the parent algebra, which the block turns into a square-zero element, and it is recorded again at the diagonal of the block.

### The Roots of One and the Parent Row

**Remark (the contrast with the parent row).** The general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ and its symmetric half have a root of $+1$, and the block is the one member of the row for which the value is out of reach. The exceptional pair of the row is therefore inverted: in the general product the root of $+1$ generates the idempotents, and in the antisymmetric part it is missing and the cone of the diagonal takes its place.

**The roots of minus one.** The root set of $-1$ of the block is empty as well. In a bilateral product with a central scalar of square $-1$ the sign flips under multiplication by that scalar, since $(i\tilde\Xi)\star(i\tilde\Xi)=i^{2}(\tilde\Xi\star\tilde\Xi)=-\tilde\Xi\star\tilde\Xi$, and the roots of $-1$ are read off the roots of $+1$ by one map; the mechanism needs a scalar that can be moved past the two slots of the product. The block is sesquilinear and its second slot conjugates, so a scalar is moved past that slot at the price of a conjugate: scaling an element by $\lambda$ multiplies its square by $\lvert\lambda\rvert^{2}$, a non-negative real, and no scalar multiplication can turn a square into its negative. The roots of $-1$ are therefore not deduced from the roots of $+1$ by a map, and here they are empty for the same reason as the roots of $+1$: $\mathbf\Xi\times\overline{\mathbf\Xi}$ is a pure vector while $-e_0$ is central, so the equation $\tilde\Xi\diamond\tilde\Xi=-e_0$ has no solution. The set is quoted here and is used nowhere in this article.

## The Idempotents

**Every idempotent of the block is the origin: the equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is satisfied by the origin and by nothing else, so the block has no nontrivial idempotent, no orthogonal family, no Peirce decomposition and no pure state, and its only projector is the zero operator.**

The **idempotents** of the block are the elements satisfying $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$. They are the algebraic form of a projection, and in the algebra of the corpus they do four separate jobs at once: they give the direct sum decompositions into left ideals, and in particular the minimal left ideals; they classify the non-pure zero divisors; in a unital bilateral product they are in bijection with the roots of $+1$ through the halving map, so their classification is there the classification of those roots; and they drive the Peirce decomposition. The block carries none of the four: its idempotent set is trivial, its transfer from the roots of $+1$ has nothing to carry, and only the first job survives, degenerately, as a decomposition onto the whole space and the origin.

### The Definition, Relative to a Product

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The origin is an idempotent of every product, and, when the product is unital, the unit is an idempotent of it; the two are the **trivial idempotents** of the product, and the others are **nontrivial**. The set of the idempotents of $\star$ is its **idempotent set**, and the definition is the one of *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*.

The same section carries the classes that the idempotent supports in an associative product: the **orthogonal** idempotents, with $\tilde\Pi\star\tilde\Pi'=\tilde\Pi'\star\tilde\Pi=0$; the **pairwise orthogonal** families and the families whose sum is the unit; the **primitive** idempotent, which is not a sum of two nonzero orthogonal ones; and the **Peirce decomposition** attached to a pairwise orthogonal family summing to the unit. Throughout this article the product is the block $\diamond$, so that, unqualified, an idempotent is an idempotent of the block, and the trivial idempotents are the origin and, were it one, the unit; the unit of the block does not exist, so the only trivial idempotent of the block is the origin.

**Remark (the class of the equation).** For a sesquilinear product the equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is not linear in $\tilde\Pi$ and is not conjugate-linear either, since the left side is conjugate-linear in its second slot while the right side is linear; the equation is therefore read on the two coordinates separately. For the block the two readings are the scalar coordinate, which vanishes identically on the left side, and the vector coordinate, which takes its values in the three real dimensional subspace of the purely imaginary real vectors; the two readings decide the set.

### The Idempotent Set of the Block

**The idempotent set of the block is the origin alone: an element $\tilde\Pi$ satisfies $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ if and only if $\tilde\Pi=0$, and the block has no nontrivial idempotent.**

**Theorem.** The idempotent set of the block is the origin: an element $\tilde\Pi$ satisfies $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ if and only if $\tilde\Pi=0$. The block has no nontrivial idempotent.

*Proof.* Let $\tilde\Pi$ satisfy $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$. Comparing the scalar parts gives $0=\Pi_0$, since the scalar part of every value of the block is zero. Comparing the vector parts gives $\boldsymbol{\Pi}\times\overline{\boldsymbol{\Pi}}=\boldsymbol{\Pi}$, so $\boldsymbol{\Pi}$ is a value of the square and lies in $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$: write $\boldsymbol{\Pi}=i\mathbf{w}$ with $\mathbf{w}$ a real vector. Then $\overline{\boldsymbol{\Pi}}=-i\mathbf{w}$ and

$$
\boldsymbol{\Pi}\times\overline{\boldsymbol{\Pi}}=(i\mathbf{w})\times(-i\mathbf{w})=-i^{2}\,(\mathbf{w}\times\mathbf{w})=0 ,
$$

so $\boldsymbol{\Pi}=0$ and $\tilde\Pi=0$. The converse is the statement $0\diamond0=0$, which holds in every product.

**Remark (the two conditions and their witnesses).** The two conditions of the proof are both necessary and each has a witness. The first is the vanishing of the scalar coordinate, and the witness of its failure is the unit of the parent algebra: $\mathrm{Sc}(e_0\diamond e_0)=0\neq1$, so $e_0$ is not an idempotent of the block. The second is the vanishing of the vector part, once the scalar part is read, and the witness of its failure is the element $e_1+ie_2$, whose square is $-2ie_3$: the vector part of the square is nonzero, so the element is not fixed. The two witnesses are the elementary ones of the block, the unit of the parent algebra and the element of the diagonal, and they are the ones that *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* uses.

**Remark (the failure is not a near miss).** The theorem is not a statement about the equation having few solutions; it is the statement that the image of the square map and the fixed locus meet at the origin alone. The image is the three real dimensional subspace of the purely imaginary real vectors, whose intersection with the central line is the origin; the square of an element with vanishing scalar coordinate is a value of that subspace, and the equation asks that value to be the element itself, so the value is an element of that subspace equal to its own square: an element $i\mathbf{w}$ of the subspace has the square $(i\mathbf{w})\times\overline{(i\mathbf{w})}=0$, and the value is the origin. The subspace of the purely imaginary real vectors is contained in the cone of the diagonal, so it is not the cone that must be cut down but the squaring that must vanish. The failure is therefore structural: the block has no fixed point of its square outside the origin, and the whole family of candidate projectors of the parent products misses the block.

### The Witnesses of the Absence

**The parent unit $e_0$ is a square-zero element of the block, so no scalar is an idempotent of the block; the idempotents $\tfrac12(e_0+\tilde\Xi)$ of the plain product have scalar part $\tfrac12$ and are outside the idempotent set of the block; and the only projector of the block is the zero operator.**

**The parent unit is a square-zero element.** The sharpest witness is $\tilde\Pi=e_0$: the unit of the four general products and of the two algebras satisfies $e_0\diamond e_0=0$ in the block, so it is not an idempotent but a nilpotent, and the sharpest possible. The whole central line shares the reading: $\lambda e_0\diamond\lambda e_0=0$ for every complex $\lambda$, so no scalar is an idempotent of the block and the block has no idempotent in the centre other than the origin.

**The idempotents of the plain product are outside the block.** The idempotents of the plain product are the halved roots of $+1$, the elements $\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$ of the plain product, of scalar part $\tfrac12$; the family and its reading are *Square Roots of One and the Idempotents of the General Plain Algebra*. Every idempotent of the block has scalar part $0$ by the first condition of the proof, and the two sets therefore meet nowhere: evaluated with the block, the family $\tfrac12(e_0+\tilde\Xi)$ gives

$$
\tfrac12(e_0+\tilde\Xi)\diamond\tfrac12(e_0+\tilde\Xi)=\tfrac14\,\mathbf\Xi\times\overline{\mathbf\Xi},
$$

a value of the block, which is not the element and is not a fixed point of the square in general. The family is thus carried by the block onto its cone of square-zero elements when the vector part of the root is a complex multiple of a real direction, and onto nonzero values otherwise; in neither case is it an idempotent of the block.

### The Consequences of the Absence

**The block carries no nontrivial idempotent, hence no orthogonal family summing to the unit, no Peirce decomposition, no pure state and no transfer from the roots of $+1$; the block moves every nonzero element away from itself, so the word projector would name an operator onto a subspace that does not exist.**

**No nontrivial idempotent, no orthogonal family, no Peirce decomposition.** The orthogonal families of the corpus are families of idempotents, and the block has one idempotent, so every family it carries is the family of the single trivial idempotent, whose sum is not the unit; the Peirce decomposition attached to such a family degenerates, and the block has no decomposition of that kind. The block is not associative in any case, so the Peirce calculus of an associative product is out of its reach for a second reason, and the two reasons agree on the answer.

**No pure state.** A pure state of a product is read through a nontrivial idempotent, and the block has none, so the block carries no pure state; the central line of the parent products, which is where the functionals of the block are read, has no idempotent to support one, and the form-theoretic route to a state is unavailable as well, as *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra* records.

**The transfer from the roots of $+1$ is unavailable.** The definitions of the corpus carry the idempotents of the plain product from the roots of $+1$ by the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$, and the transfer presupposes a unit and a value of the algebra. The block has no unit and its roots of $+1$ are empty, so the transfer has nothing to carry; the idempotent set is computed directly, as above. The two empty sets of §*The Roots of One* are the reason the transfer has nothing to carry.

**The block is a pure deformation and not a projection.** The diagonal maps the whole space into the cone of the complex multiples of the real directions, so the block moves every nonzero element away from itself and its fixed locus collapses to the origin. The word projector, in the block, would name an operator onto a subspace that does not exist: a projector is an idempotent read as an operator, the only idempotent of the block is the origin, whose left multiplication is the zero operator, and the only projector of the block is therefore the zero operator. The left multiplications of the block are conjugate-linear and their compositions are complex-linear, so the operator calculus of the algebras of the corpus is not available to them in any case, as *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* shows.

### The Comparison with the Other Products

**Of the twelve products the four antisymmetric parts are exactly the four whose idempotent set is the origin alone; the four general products and their symmetrised halves carry idempotents, and the unit $e_0$ of the row is a square-zero element of the block.**

The idempotent sets of the four general products are known and are recorded in the corpus; the block is compared with them and with the two symmetric halves of its own row below. Every one of the four sets contains the two trivial idempotents, the origin and the unit; the table records the rest of each.

| product | the nontrivial idempotents | the source |
|---|---|---|
| $\tilde P\tilde Q$ | the plain family $\tfrac12(e_0+\tilde\Xi)$ over the roots $\tilde\Xi$ of $+1$ | *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* |
| $\tilde P^{\natural}\tilde Q$ | none beyond the trivial ones | the same |
| $\tilde P\tilde Q^{*}$ | the Hermitian family $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$ | the same |
| $\tilde P^{\natural}\tilde Q^{*}$ | the family $-\tfrac12e_0+\mu$ over the real vectors $\mu$ with $(\mu,\mu)=\tfrac34$ | the same |
| the block $\mathbf{P}\times\overline{\mathbf{Q}}$ | the origin alone | above |

Read on the twelve, the table has one more regularity: **the four antisymmetric parts are exactly the four products whose idempotent set is the origin alone.** The plain, the natural, the plain sesquilinear and the quaternionic sesquilinear products all carry idempotents, and their symmetrised halves all carry the unit $e_0$. Two of the four symmetrised halves carry the whole family of the parent: the symmetric plain algebra carries the plain family, and the symmetric quaternionic sesqualgebra carries the family $-\tfrac12e_0+\mu$. The symmetric natural algebra and the symmetric plain sesqualgebra carry the two trivial idempotents alone, their square being scalar-valued, so that an idempotent of either must be central and only the trivial pair survives. The four antisymmetrised halves (the antisymmetric plain algebra, the antisymmetric plain sesqualgebra, and the two blocks of the rows, of which the block is the quaternionic one) carry none.

**Remark (the unit of the row is a nilpotent of the block).** Within the row the inversion is sharp. The unit $e_0$ is an idempotent of the general quaternionic sesquilinear product and of its symmetric half, and it is a square-zero element of the block; the idempotents of the row are the objects the block turns into the objects of its own cone. The reading is the element-theoretic form of the antithesis between the two halves, and it is stated as such in *The 12 Products of the Biquaternion Complex Space*.

## Summary

The block has no root of $+1$: for every nonzero $\lambda\in\mathbb{C}$ the equation $\tilde\Xi\diamond\tilde\Xi=\lambda e_0$ has no solution, because every value of the block is a pure vector while $\lambda e_0$ is central. The failure is total, and the witness is the parent unit $e_0$, whose square in the block is zero. The roots of $-1$ are empty as well: the central imaginary that carries the roots of $+1$ onto them in a bilateral product is unavailable to a sesquilinear product, whose second slot conjugates and scales a square by the non-negative real $\lvert\lambda\rvert^{2}$, and the set is empty for the same structural reason.

The idempotent set of the block is the origin alone: the block has no nontrivial idempotent, and the equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is satisfied by the origin and by nothing else. The proof reads the two coordinates of the value: the scalar part of the square vanishes, so an idempotent has vanishing scalar coordinate, and its vector part is a fixed point of the square, hence a value of the square, hence lies in the three real dimensional subspace of the purely imaginary real vectors; an element $i\mathbf{w}$ of that subspace has the square $(i\mathbf{w})\times\overline{(i\mathbf{w})}=(i\mathbf{w})\times(-i\mathbf{w})=0$, so the only fixed point of the square is the origin. The witnesses of the absence are the parent unit $e_0$, which the block sends to zero, and the elements $e_1+ie_2$ and $\tfrac12(e_0+\tilde\Xi)$, whose squares are not themselves. The consequences are the absence of the projector calculus, of the orthogonal families, of the Peirce decomposition and of the pure states, and the unavailability of the halving transfer from the roots of $+1$. Among the twelve products the block is one of the four antisymmetric parts, and those four are exactly the products whose idempotent set is the origin alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ | the conjugate cross product, the product of the block |
| $\tilde\Xi\diamond\tilde\Xi=\mathbf\Xi\times\overline{\mathbf\Xi}=\mathbf{0}$ | the square of a root of $+1$ would have to be central, and every value is a pure vector |
| $\lambda e_0$ | a central value, with a root only for $\lambda=0$ |
| $\tilde\Xi=e_0$ | the parent unit, the witness against $+1$ and against $-1$ |
| $e_0\diamond e_0=0$ | the parent unit as a square-zero element of the block |
| $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ | the idempotent equation of the block |
| $\mathrm{Sc}(\tilde X\diamond\tilde X)=0$ | the first condition, forcing $\Pi_0=0$ |
| $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | the image of the square, where the vector part of an idempotent must lie |
| $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ | the halving map of a unital product, unavailable here |
| $e_1+ie_2$ | not fixed by the square, its square being $-2ie_3$ |
| $\tfrac12(e_0+\tilde\Xi)$ | the idempotents of the plain product, outside the idempotent set of the block |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots* and §*The Idempotent, the Projection and the Peirce Decomposition*, for the root of a central value, the idempotent, the orthogonal families, the primitive idempotent and the Peirce decomposition, for a general product.
- *Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the roots of $0$, the other central value of the block, and for the nilpotents.
- *Square Roots of a General Element in the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-antisymmetric-quaternionic-sesqualgebra.md`), for the roots of the general quadratic $\tilde\Xi\diamond\tilde\Xi=\tilde Q$, of which the roots of one here are one case.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra.md`), for the model block, where the idempotents are the halves of the roots of $+1$.
- *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the zero-divisor set outside which the only idempotent, the origin, lies.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the left multiplications, their conjugate-linearity and the zero projector.
- *The Specificities of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-specificities-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the law behind the vanishing of the diagonal.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve products read as the structures they define.
- *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/idempotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the idempotent sets of the four general products and of the twelve read against one another.
