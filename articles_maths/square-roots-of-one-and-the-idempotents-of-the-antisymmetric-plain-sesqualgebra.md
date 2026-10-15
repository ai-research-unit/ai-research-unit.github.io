# __Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra__

## Introduction

A root of a central value is defined by an equation in which the product occurs, so it belongs to the product (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*). The block of this article is the antisymmetric plain sesquilinear product

$$
\tilde P\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)
=-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q},
$$

the antisymmetric half of the general plain sesquilinear product, a product conjugate-linear in its second slot and without a unit (*Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*).

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi\diamond\tilde\Xi=+e_0 .
$$

The second is the idempotents of the block, the elements $\tilde\Pi$ with $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$. In a unital associative product the idempotent is the root of $+1$ in a scaled sense, through the **halving map** $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ and its inverse $\tilde\Xi=2\tilde\Pi-e_0$. The block is not associative, it has no unit, and it has no root of $+1$; the map therefore carries nothing, and the two subjects are joined negatively, by the emptiness of the family the map would produce.

The outcome is the extreme absence. The block has **no root of $+1$**, by the parity that removes the scalar part from every value; the roots of $-1$ fall to the same parity, and the paragraph closing §*The Root of One* records that their set is **empty**. The block has **one idempotent, the origin**, because its idempotent equation reduces to $\vec p=0$ on a pure vector. It therefore has no nontrivial idempotent, no orthogonal pair, no family summing to a unit, no primitive idempotent, no projection and no Peirce decomposition, and the unit $e_0$ of the ambient algebra is not an idempotent of the block.

The article is algebraic. It does not treat the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra*; the square roots of a general right side, which is *Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra*; the zero-divisor set, which is *Zero Divisors of the Antisymmetric Plain Sesqualgebra*; or the idempotent families of the general plain product, which are *Idempotents of the General Plain Algebra*.

**The results.** For the block $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ every value is a pure vector, of vanishing scalar part, and $+e_0$ is central: the root equation of $+1$ therefore fails for every element, and the block has **no root of $+1$**. The roots of $-1$ are **empty** as well, the conjugate-linear second slot denying the sign-flip of a bilateral product. The idempotent equation reduces, on a pure vector $\vec p$, to $-\vec p\times\overline{\vec p}=\vec p$, whose only solution is $\vec p=0$: the block has **one idempotent, the origin**, hence no orthogonal pair, no family summing to a unit, no primitive idempotent, no projection and no Peirce decomposition; the unit $e_0$ is not an idempotent of the block. The comparison with the parent is the comparison of the origin alone with the Hermitian idempotents of the plain sesquilinear product, which the block does not inherit.

## The Notion and Its Product

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{B}$ and let $\lambda\in\mathbb{C}$. A **root of $\lambda$ in $\star$** is a nonzero element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 .
$$

The three central values the biquaternion algebra singles out are $-1$, $+1$ and $0$: the roots of $-1$ are the imaginary units, the roots of $+1$ are the involutions, and the roots of $0$ are the nonzero nilpotents of the product (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*).

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The origin and, when the product is unital, the unit are idempotents of every product: they are the **trivial idempotents**, and the others are **nontrivial** (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Idempotent, the Projection and the Peirce Decomposition*).

Throughout this article the product is the **block** $\diamond$, and unqualified, *root* means a root of a central value in $\diamond$ and *idempotent* means an idempotent of $\diamond$; the value is fixed at $+1$ in §*The Root of One*. In a unital associative product the idempotent is the root of $+1$ in a scaled sense: the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$, because $\tilde\Xi^{2}=e_0$ exactly when the idempotent equation holds at $\tfrac12(e_0+\tilde\Xi)$. The block is not associative and carries no unit, so the map is not read on it; its root set of $+1$ is empty and its idempotents are determined directly in §*The Idempotents*.

## The Root of One

**The block has no root of $+1$: the equation $\tilde\Xi\diamond\tilde\Xi=+e_0$ has no solution.**

**Theorem (no root of $+1$).** For every $\tilde\Xi$ the value $\tilde\Xi\diamond\tilde\Xi$ is a pure vector, and no pure vector is a nonzero central element. Consequently the equation $\tilde\Xi\diamond\tilde\Xi=+e_0$ has no solution, and the block has no root of $+1$.

*Proof.* The value $\tilde\Xi\diamond\tilde\Xi$ lies in the image of the block, the vector subspace $\operatorname{Vect}(\mathbb{B})$, so its scalar part vanishes. The element $+e_0$ is central with scalar part $1$, and the centre $\mathbb{C}_{\mathbb{B}}$ meets the vector subspace at the origin; hence $\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})=+e_0$ is impossible.

The obstruction is the **centrality**, and not the non-vanishing of the diagonal. The diagonal does vanish on a set of elements, and it is nonzero elsewhere; the element $e_1+ie_2$ has the nonvanishing diagonal $2ie_3$, and no element has the central diagonal $+e_0$, the image of the block being the vector subspace. The vanishing diagonal is the root of $0$ and not of $+1$, and it is the subject of *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra*.

**The roots of minus one.** The same parity settles the central value $-1$, and the remark is recorded here and used nowhere. The block has **no root of $-1$** either, so its root set of $-1$ is **empty**: the equation $\tilde\Xi\diamond\tilde\Xi=-e_0$ reduces to $\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})=-e_0$, and $-e_0$ is central while every value is a pure vector. The mechanism that reads the roots of $-1$ off the roots of $+1$ in a bilateral product is unavailable here; there a multiplication by the central imaginary flips the sign, $(i\tilde\Xi)\star(i\tilde\Xi)=i^{2}(\tilde\Xi\star\tilde\Xi)=-\tilde\Xi\star\tilde\Xi$, because the product is bilinear, while the block is conjugate-linear in its second slot and the substitution $\tilde\Xi\mapsto i\tilde\Xi$ carries no equation to another. The remark concerns the two root sets alone, and no later section uses it.

## The Idempotents

**The idempotent equation of the block is satisfied by the origin alone, $\{\tilde\Pi:\tilde\Pi\diamond\tilde\Pi=\tilde\Pi\}=\{0\}$; the block has no nontrivial idempotent.**

### The Idempotent Equation of the Block

**Proposition (an idempotent is pure).** An idempotent of the block has vanishing scalar part: $\tilde\Pi=\vec p$, a pure vector.

*Proof.* The left member $\tilde\Pi\diamond\tilde\Pi$ is a value of the block, hence a pure vector whose scalar part is zero; the right member is $\tilde\Pi$, so the scalar part of $\tilde\Pi$ is zero.

For a pure element the diagonal is the conjugate cross product,

$$
\vec p\diamond\vec p=-\vec p\times\overline{\vec p},
$$

the value $\operatorname{Vect}(\vec p\vec p^{*})=\operatorname{Vect}(-\vec p\overline{\vec p})=-\vec p\times\overline{\vec p}$.

**Proposition (the diagonal of a pure element is purely imaginary).** For every pure $\vec p$ the value $-\vec p\times\overline{\vec p}$ is purely imaginary,

$$
-\vec p\times\overline{\vec p}=-\overline{\bigl(-\vec p\times\overline{\vec p}\bigr)} .
$$

*Proof.* Apply the coefficientwise conjugation to the value: the conjugate of $\vec p\times\overline{\vec p}$ is $\overline{\vec p}\times\vec p=-\vec p\times\overline{\vec p}$ by the anti-commutativity of the cross product over $\mathbb{C}$, so $-\vec p\times\overline{\vec p}$ equals the negative of its own conjugate.

**Theorem (the only idempotent is the origin).** The block has exactly one idempotent, the element $0$. There is no nontrivial idempotent.

*Proof.* Let $\tilde\Pi$ be an idempotent. By the first proposition it is pure, $\tilde\Pi=\vec p$, and the equation is $-\vec p\times\overline{\vec p}=\vec p$. The left member is purely imaginary by the second proposition, so the right member is purely imaginary and $\vec p=i\vec u$ with $\vec u\in\mathbb{R}^{3}$; the left member is then

$$
-(i\vec u)\times\overline{(i\vec u)}=-(i\vec u)\times(-i\vec u)=i^{2}(\vec u\times\vec u)=0 ,
$$

the cross product of a real vector with itself being zero. The equation reads $\vec p=0$, so $\tilde\Pi=0$; the origin is an idempotent of every product, and it is the only one.

The computation is the whole of the proof: the parity reduces an idempotent to a pure $\vec p$, the model computation $-\vec p\times\overline{\vec p}=\vec p$ is the equation, and its only solution is the origin. The unit $e_0$ of the ambient algebra is not an idempotent of the block, since $e_0\diamond e_0=\operatorname{Vect}(e_0)=0\neq e_0$.

### The Consequences of the Absence

**With no nontrivial idempotent the derived vocabulary is vacuous — no orthogonal pair, no family summing to a unit, no primitive idempotent, no Peirce decomposition — and the only projector among the one-sided multiplications is the zero operator.**

- **No nontrivial idempotent.** The idempotent set of the block is $\{0\}$, and the second trivial idempotent of a unital product, the unit, does not exist, the block having no unit (*Norm and Invertibility in the Antisymmetric Plain Sesqualgebra*).
- **No orthogonal pair.** The only idempotent is the origin, so the only orthogonal pair of idempotents is $(0,0)$.
- **No primitive idempotent.** A primitive idempotent is nontrivial by definition, and there is none.
- **No Peirce decomposition.** The decomposition is stated for an associative unital product, and the block is neither associative nor unital; the corner algebras and the minimal left ideals it would produce belong to the plain product (*Ideals and Peirce Decomposition of the General Plain Algebra*).

**Proposition (the only projector is the zero operator).** Let $L^{\diamond}_{\tilde P}$ be the left multiplication of the block by $\tilde P$, the map $\tilde X\mapsto\tilde P\diamond\tilde X$. It is conjugate-linear, and it is a projector if and only if $\tilde P=0$, in which case it is the zero operator.

*Proof.* The left multiplication of the block is $\mathbb{C}$-conjugate-linear in $\tilde X$, since the product is conjugate-linear in its second slot. If it were a projector, $L^{\diamond}_{\tilde P}\circ L^{\diamond}_{\tilde P}=L^{\diamond}_{\tilde P}$, the composite on the left being $\mathbb{C}$-linear while the right is conjugate-linear; a map that is both linear and conjugate-linear is zero, because $\lambda L(\tilde X)=L(\lambda\tilde X)=\overline{\lambda}L(\tilde X)$ for every $\lambda$, forcing $L(\tilde X)=0$. It remains to read $L^{\diamond}_{\tilde P}=0$: at $\tilde X=e_0$ the value is $\vec P$, so $\tilde P$ is central, $\tilde P=ce_0$; at $\tilde X=e_1$ the value is $\operatorname{Vect}(ce_0e_1^{*})=-ce_1$, so $c=0$ and $\tilde P=0$. Conversely $L^{\diamond}_0=0$ is a projector.

The two absences, the idempotent and the projector, have one source, the conjugate-linearity together with the projection, and the operator reading is the subject of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*.

### The Comparison with the Parent

**The block keeps the origin alone and loses the parent's idempotents, which are not inherited; among the twelve structures it is the row in which the idempotent set collapses to the trivial one.**

**Remark (the parent idempotents).** The parent of the block is the general plain sesquilinear product $\tilde P\tilde Q^{*}$, whose idempotents are the Hermitian idempotents, the elements $\tilde\Pi$ with $\tilde\Pi\tilde\Pi^{*}=\tilde\Pi$ and $\tilde\Pi^{*}=\tilde\Pi$; they are the two trivial idempotents $0$ and $e_0$ together with the sphere $\tfrac12e_0+i\vec u$ over the real vectors $\vec u$ with $(\vec u,\vec u)=\tfrac14$, and the block does not inherit them. The diagonal of such an element is $\operatorname{Vect}(\tilde\Pi\tilde\Pi^{*})=\operatorname{Vect}(\tilde\Pi)$, its own vector part, so a Hermitian idempotent is a block idempotent only when it equals its own vector part; and a pure Hermitian element $i\vec u$, whose block square is $0$, is a block idempotent only at the origin. The two idempotent sets therefore meet only at the origin, and the two sesquilinear blocks of the plain row have disjoint idempotent theories.

The block is one row of the table of the twelve idempotent sets, where the plain product carries the family $\tfrac12(e_0+\tilde\Xi)$ over its roots $\tilde\Xi$ of $+1$ and the natural product carries the trivial pair alone; the tabulation is *Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Twelve Idempotent Sets*, and the idempotents of the general plain product are *Idempotents of the General Plain Algebra*.

## Summary

For the block $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ every value is a pure vector, so the root equation of $+1$ reduces to $\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})=+e_0$ and has no solution: the block has **no root of $+1$**. The obstruction is the centrality of $+e_0$ and not the vanishing of the diagonal. The roots of $-1$ fall to the same parity and their set is **empty**, the conjugate-linear second slot denying the sign-flip of a bilateral product; the remark is not used later.

The idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ reduces to $-\vec p\times\overline{\vec p}=\vec p$ on a pure vector, and its only solution is $\vec p=0$: the block has **one idempotent, the origin**, and no nontrivial idempotent. The unit $e_0$ of the ambient algebra is not an idempotent of the block, the block being a bracket and not the plain product. No orthogonal pair, no family summing to a unit, no primitive idempotent and no Peirce decomposition exists, and the only projector the block carries is the zero operator, from the origin. The parent's Hermitian idempotents, $0$, $e_0$ and the sphere $\tfrac12e_0+i\vec u$, are not inherited, their diagonal being their own vector part, and the two idempotent sets meet only at the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ | the block, the operation $\mathrm{APS}$ |
| $\tilde\Xi\diamond\tilde\Xi=\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})$ | the diagonal of the block, always a pure vector |
| $\tilde\Xi\diamond\tilde\Xi=+e_0$ | the root equation of $+1$, without solution |
| $\lambda\in\{-1,+1\}$ | the two nonzero central values, both without roots; the value $0$ is *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra* |
| $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ | the idempotent equation, equivalent to $\vec p=0$ on a pure vector |
| $\{0\}$ | the idempotent set of the block, the trivial idempotent alone |
| $L^{\diamond}_{\tilde P}$ | the conjugate-linear left multiplication, a projector only at $\tilde P=0$ |
| $\tfrac12(e_0+\tilde\Xi)$ | the idempotents of the general plain product, over the roots $\tilde\Xi$ of $+1$, absent from the block |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), §*Powers, the Square and the Roots* and §*The Idempotent, the Projection and the Peirce Decomposition*, for the root of a central value, the idempotent and the halving map.
- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, its conjugate-alternation and its table.
- *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-sesqualgebra.md`), for the roots of $0$ and the other face of the projection.
- *Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-antisymmetric-plain-sesqualgebra.md`), for the square map of the block and the arbitrary right side.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), for the idempotent family of the general plain product, against which the block's origin alone is read.
- *Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), §*The Twelve Idempotent Sets*, for the idempotent sets of the twelve structures side by side.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the criterion for the vanishing of the diagonal.
