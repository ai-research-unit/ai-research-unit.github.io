# __The Realification of the General Quaternionic Sesqualgebra__

## Introduction

The general quaternionic sesqualgebra is the structure carried by the general quaternionic sesquilinear product
$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*},
$$
the fourth of the four general products and one of the twelve structures that the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries (*The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). Over $\mathbb{C}$ it is a sesqualgebra over $(\mathbb{C},\varsigma)$, it has no unit on either side, and its scalar part is the general quaternionic sesquilinear form. This article is the **real reading** of that one product: the same product on the same eight-dimensional real space, the change of kind the passage produces, the two one-sided multiplications and the parities they take, and the realification of the form the product carries.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the doubling of the dimension, the complex structure $J$, the two rules for forms and the table of the four effects are **The Realification and the Effect of the Change of Scalars**.

## The Change of Scalars

The biquaternion space is the complex vector space of dimension four on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$; the scalars are $\mathbb{C}$, read on the scalar line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, the image of the scalar action $A\mapsto Ae_t$, which is **not** the centre here, the centre of the multiplication being trivial; and the base involution is the conjugation $\varsigma(z)=\bar z$ on it. Read over $\mathbb{R}$ the same set is the real vector space
$$
\mathbb{R}^8=\operatorname{span}_\mathbb{R}\{e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z\},
$$
with the same addition and the same product: **restriction of scalars**, no new multiplication and a smaller field. The complex structure is
$$
J:\tilde Q_1\longmapsto i\tilde Q_1,\qquad J^2=-\mathrm{id},
$$
an $\mathbb{R}$-linear endomorphism of $\mathbb{R}^8$ of square $-\mathrm{id}$; it commutes with itself, so it is $\mathbb{C}$-linear by the criterion $TJ=JT$, and it is **not** a left multiplication of this product, since $L_{ie_t}(\tilde Q_1)=(ie_t)^{\natural}\tilde Q_1^{*}=i\tilde Q_1^{*}\neq i\tilde Q_1$: the scalar action of the block is one-sided, and the complex structure belongs to the underlying space and not to the multiplication.

The product is $\mathbb{C}$-linear in its first slot and $\varsigma$-semilinear in its second. Over $\mathbb{R}$ the involution $\varsigma$ restricts to the identity — the only automorphism of $\mathbb{R}$ is the identity — and a semilinear law with the identity involution **is** a bilinear law. The passage therefore **changes the kind** of this product: a **sesqualgebra over $(\mathbb{C},\varsigma)$** over $\mathbb{C}$, an **$\mathbb{R}$-algebra** on $\mathbb{R}^8$ in the broad sense. The distinction does not vanish; it migrates from the field to the scalar line, where it is the conjugate-linearity of the second slot over $\mathbb{C}_{\mathbb{B}}$, equivalently the anticommutation $LJ=-JL$ of every left multiplication with the complex structure, proved in §*The Second Slot and the Two One-Sided Multiplications* below. This is the general effect of §*The Effect on the Twelve Algebraic Structures* of *The Realification and the Effect of the Change of Scalars*, of which the block is the instance in the quaternionic sesquilinear row.

The statements that do not move are those about the ring. The failure of associativity, of flexibility and of power associativity, the absence of a unit on either side and the triviality of the centre of the multiplication, the associator, the ternary product, the square, the idempotent family, the square-zero family, the zero divisors and the plain invertibility criterion $C(\tilde Q_2)\neq0$ are written with the addition, the product and quantification over the elements, and they are the same in the two readings, by §*The Four Effects on a Structure* of the same article. What moves is every notion that names the field: the dimension, the sesqualgebra structure, and the linear or the conjugate-linear character of a map.

## The Product Read over $\mathbb{R}$

The product is $\mathbb{R}$-bilinear, because a $\mathbb{C}$-sesquilinear law is additive in each argument and linear over the subfield $\mathbb{R}$. The block is therefore an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in the broad sense, a module with a bilinear multiplication, with no further axiom. Its list is the complex one, unchanged:

- **no unit on either side**, the two one-sided actions of $e_t$ being the two conjugations, $e_t\star\tilde Q_2=\tilde Q_2^{*}$ on the left and $\tilde Q_1\star e_t=\tilde Q_1^{\natural}$ on the right;
- neither associative nor commutative, so that no reading of the product is a commutative law;
- the values fill the whole space, the products of two basis elements being $\pm e_\mu$ and their complex span being $\mathbb{B}$;
- the left multiplications do not form a monoid.

The last entry is worth a word, because the real reading states it in the language of the next section. The composition of two left multiplications is
$$
L_{\tilde Q_4}\circ L_{\tilde Q_2}(\tilde Q_3)=\tilde Q_4^{\natural}\tilde Q_3\,\overline{\tilde Q_2},
$$
which is $\mathbb{C}$-linear in $\tilde Q_3$ — the two conjugate-linear maps compose to a linear one — so the composite is a nonzero linear map wherever $\tilde Q_4$ and $\tilde Q_2$ are nonzero, and it is then no left multiplication, every left multiplication with a nonzero parameter being conjugate-linear; the family therefore contains no identity and is not closed under composition, and the block has the element theory of the sesquilinear structures without their operator theory. Read over $\mathbb{R}$, the composite lies in the commuting part of $\operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)$ and no nonzero left multiplication does.

## The Second Slot and the Two One-Sided Multiplications

Write
$$
L_{\tilde Q_1}:\tilde Q_3\longmapsto\tilde Q_1\star\tilde Q_3,\qquad R_{\tilde Q_2}:\tilde Q_3\longmapsto\tilde Q_3\star\tilde Q_2
$$
for the left and the right multiplication.

**Theorem (the two parities).** The left multiplication is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear and the right multiplication is $\mathbb{C}_{\mathbb{B}}$-linear; equivalently, they are $\mathbb{R}$-linear on $\mathbb{R}^8$ and
$$
\boxed{\; L_{\tilde Q_1}\,J=-J\,L_{\tilde Q_1},\qquad R_{\tilde Q_2}\,J=+J\,R_{\tilde Q_2} \;}.
$$

*Proof.* The product is $\mathbb{C}$-linear in its first slot and conjugate-linear in its second, so $L_{\tilde Q_1}$ is conjugate-linear and $R_{\tilde Q_2}$ is linear in the variable, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*. A conjugate-linear $\mathbb{R}$-linear map anticommutes with the complex structure and a linear one commutes with it, by the two criteria of the same section.

**Corollary (the two block shapes).** In the real basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ the left multiplication has the matrix
$$
\begin{pmatrix}A&B\\ B&-A\end{pmatrix},
\qquad\text{and the right multiplication}\qquad
\begin{pmatrix}A&-B\\ B&A\end{pmatrix},
$$
the two shapes attached to the anticommuting and to the commuting $\mathbb{R}$-linear endomorphisms. The left multiplication is **traceless**: its two diagonal blocks are opposite, so their traces cancel and $\operatorname{Tr}_{\mathbb{R}}L_{\tilde Q_1}=0$.

**Corollary (the two summands).** By §*The Realification of a Linear Map*,
$$
\boxed{\; \operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\oplus\operatorname{Ant}_{\mathbb{C}}(\mathbb{B}) \;},
$$
the commuting and the anticommuting endomorphisms, of real dimensions $32$ and $32$ for $n=4$. The left multiplications of the block lie in the second summand and the right multiplications in the first. This is the operator form of the $A/S$ distinction: for the two bilinear general products both slots are read without a conjugation, so both families commute with $J$, while for the two sesquilinear general products, whose second slot carries the star, the left multiplications anticommute and the right multiplications commute. The parity $LJ=-JL$ against $RJ=JR$ is therefore the same statement as the linearity against the conjugate-linearity of the slots over $\mathbb{C}_{\mathbb{B}}$.

**Remark (the first slot of this block and of its sibling).** Inside the sesquilinear family the parity is carried by the second slot alone, and the insertion of the $\mathbb{C}$-linear ${}^{\natural}$ in the first slot does not move it: the left multiplications of the block and those of the general plain sesquilinear product are the same family of operators, indexed through the involution,
$$
L^{\mathrm{GQS}}_{\tilde Q_1}=L^{\mathrm{GPS}}_{\natural(\tilde Q_1)},\qquad\natural(\tilde Q_1)=\tilde Q_1^{\natural},
$$
so the two blocks differ in their elements, their tables and their forms, and not in the anticommuting family of operators they generate. The parity content of the block is carried by the star of its second slot alone, which is what *The Specificities of the General Quaternionic Sesqualgebra* records from the complex side.

## The Realified Form

The product carries the general quaternionic sesquilinear form, the Krein form
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q_1\star\tilde Q_2\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}},\qquad\varepsilon=(1,-1,-1,-1),
$$
Hermitian of complex inertia $(1,3)$ (*The Four Forms and the Four Algebraic Norms*). It is real on the diagonal, and its imaginary part, alternating and non-zero off the diagonal, is no second independent form: it is recovered from the real part by $\operatorname{Im}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=-K_{\mathbb{R}}(J\tilde Q_1,\tilde Q_2)$, so the realification is one real symmetric bilinear form and not the split pair that a bilinear form gives. By §*The Realification of a Form* of *The Realification and the Effect of the Change of Scalars* its signature is the double of the complex inertia,
$$
\boxed{\; (2p,2q)=(2,6) \;},
$$
with Gram matrix $\operatorname{diag}(\varepsilon,\varepsilon)$ in the real basis, of signs $+,-,-,-,+,-,-,-$. This is the Krein row of the table of *The Realification of the Four Forms*, §*The Four Gram Matrices*, quoted here; among the four forms of the corpus the form of the block is the only one that is **indefinite on the complex side**, so its realification is the only one that is neither definite, as $(8,0)$, nor split, as $(4,4)$.

On the realifications the complex structure **preserves** the form,
$$
K_{\mathbb{R}}(J\tilde Q_1,J\tilde Q_2)=+K_{\mathbb{R}}(\tilde Q_1,\tilde Q_2),
$$
as it does for the Hermitian form and in contrast with the two bilinear forms, whose realifications are reversed by $J$. The sign is the block structure of the Gram matrix: the two blocks of $\operatorname{diag}(\varepsilon,\varepsilon)$ are equal where those of the split matrices are opposite.

**Remark (the null set).** For the two bilinear forms the realification enlarges the null set, from a complex cone of real dimension $6$ to a real hypersurface of real dimension $7$, because the discarded imaginary part is a second real form. For the two Hermitian forms there is nothing to enlarge, their diagonals being real, so that the realified null set is the null set itself. For the Krein form the null set is therefore the complex one, the real cone $\lVert c\rVert_E=\lVert v\rVert_E$ of real dimension $7$ — the scalar coordinate against the vector part — non-singular off the apex, with its maximal isotropic real plane $\operatorname{span}_{\mathbb{R}}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$ (*The Krein Norm of the Biquaternion Algebra*, and §*The Realified Null Cones* of *The Realification of the Four Forms*).

## What Is Specific to the Real Interpretation

The passage adds three things that the complex reading does not state in this form, and their scope is not the same: the first and the third belong to the whole sesquilinear family, and only the second is particular to the form of the block.

**The parity split of the one-sided operators.** Over $\mathbb{C}$ the block is separated from the $A$ family by its scalar rules. Read over $\mathbb{R}$ the separation is read on the operators: the left multiplications lie in the anticommuting summand $\operatorname{Ant}_{\mathbb{C}}(\mathbb{B})$ and the right multiplications in the commuting one $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The split is the $S$ family's, and the block shares it with the sibling general plain sesquilinear product, whose left-multiplication family its own family reproduces through the reindexing by $\natural$. The composition of two left multiplications crosses from one summand to the other, which is the operator form of the failure of the left multiplications to be a monoid.

**The indefinite Hermitian realification.** The Krein form realifies by the doubling of its inertia, $(1,3)\mapsto(2,6)$, and this is the item particular to the block: among the four forms of the corpus its form is the only one that is indefinite on the complex side, so the realified form is the only one that is neither definite, as the $\mathrm{I}_8$ of the Hermitian form, nor split, as the $(\mathrm{D},-\mathrm{D})$ and the $(\mathrm{I}_4,-\mathrm{I}_4)$ of the two bilinear forms.

**The traceless left multiplications.** A conjugate-linear map has no intrinsic trace over $\mathbb{C}$; read over $\mathbb{R}$, the left multiplication is a real endomorphism and its trace vanishes for every $\tilde Q_1$, whereas the right multiplications have no such vanishing. The two families, already distinguished by their parities, are separated by their traces as well, and the tracelessness, like the parity split, is the whole $S$ family's.

The rest of the block's body is unchanged, and the reason is the dictionary: the unit, the associativity, the idempotents, the nilpotents, the square-zero family and the zero divisors are read from the ring alone. In particular the idempotents are those of the complex reading, $0$, $e_t$ and the family
$$
\tilde\Pi(\vec u)=-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u,\qquad(\vec u,\vec u)=1\ \text{in the real vector subspace};
$$
the square-zero family is $\lambda(\vec u+i)$, equivalently $\lambda(e_t+\tilde\Xi)$, with $\lambda\in\mathbb{C}$ and $\vec u$ a real unit vector, of which $e_t+i\vec e_x$ is the witness; and the plain invertibility criterion $C(\tilde Q_2)\neq0$ is the same in the two readings. The count of the ring-theoretic objects of the block does not change with the scalars.

## Summary

Read over $\mathbb{R}$ the general quaternionic sesqualgebra is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in the broad sense, with no unit on either side and neither associative nor commutative; the sesqualgebra structure over $(\mathbb{C},\varsigma)$ disappears with the involution of the base field and survives as the conjugate-linearity of the second slot over the scalar line $\mathbb{C}_{\mathbb{B}}$. Its left multiplications are conjugate-linear, hence anticommute with the complex structure and are traceless, with the block matrix $\left(\begin{smallmatrix}A&B\\B&-A\end{smallmatrix}\right)$, and its right multiplications are linear, commute with $J$ and have the block matrix $\left(\begin{smallmatrix}A&-B\\B&A\end{smallmatrix}\right)$: the two one-sided families lie in the two summands of $\operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)$. The form it carries is the Krein form, whose realification has signature $(2,6)$ and is preserved by $J$ — the only realified form of the corpus that is indefinite without being split — and whose null set is not enlarged by the passage, its quadratic form being already real. Everything the block states about its elements — the absence of a unit, the associator, the ternary product, the square, the idempotents, the nilpotents and the zero divisors — is a statement about the ring and is the same in the two readings.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the product of the general quaternionic sesqualgebra |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, the real basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the scalar line, the image of the scalar action $A\mapsto Ae_t$; not the centre, which is trivial |
| $J$ | the complex structure, multiplication by $i$, of square $-1$ |
| $L_{\tilde Q_1}$, $R_{\tilde Q_2}$ | the left and the right multiplications, $\mathbb{R}$-linear on $\mathbb{R}^8$ |
| $LJ=-JL$, $RJ=+JR$ | the two parities: the left anticommutes with $J$, the right commutes |
| $\left(\begin{smallmatrix}A&B\\B&-A\end{smallmatrix}\right)$, $\left(\begin{smallmatrix}A&-B\\B&A\end{smallmatrix}\right)$ | the block matrices of the left and of the right multiplication |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\oplus\operatorname{Ant}_{\mathbb{C}}(\mathbb{B})$ | the two summands of $\operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)$, of real dimensions $32$ and $32$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the Krein form, the scalar part of the product, of complex inertia $(1,3)$ |
| $(2,6)$, $\operatorname{diag}(\varepsilon,\varepsilon)$ | the signature and the Gram matrix of the realified form |
| $\tilde\Pi(\vec u)=-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$, $(\vec u,\vec u)=1$ | the nontrivial idempotents, a ring statement unchanged by the passage |

## Further Reading

- [The Realification and the Effect of the Change of Scalars](the-realification-and-the-effect-of-the-change-of-scalars.html), for the general construction, the two rules of the realification of a form, the table of the four effects and the splitting $\operatorname{End}_{\mathbb{R}}=\operatorname{End}_{\mathbb{C}}\oplus\operatorname{Ant}_{\mathbb{C}}$.
- [The Realification of the Eight Derived Structures](the-realification-of-the-eight-derived-structures.html), for the four realified Gram matrices and signatures, the Krein row $\operatorname{diag}(\varepsilon,\varepsilon)$ of signature $(2,6)$, the restrictions and the realified null cones.
- [Introduction to the General Quaternionic Sesqualgebra](introduction-to-the-general-quaternionic-sesqualgebra.html), for the product, its table, its scalar rules, the two one-sided actions of $e_t$, the associator, the ternary product and the idempotents.
- [The Specificities of the General Quaternionic Sesqualgebra](the-specificities-of-the-general-quaternionic-sesqualgebra.html), for the star identity, the factorization, the parity obstruction and the isolation of the block among the twelve.
- [Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra](square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-sesqualgebra.html), [Zero Divisors of the General Quaternionic Sesqualgebra](zero-divisors-of-the-general-quaternionic-sesqualgebra.html) and [Norm and Invertibility in the General Quaternionic Sesqualgebra](norm-and-invertibility-in-the-general-quaternionic-sesqualgebra.html), for the idempotent family $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$, the square-zero elements and the plain criterion $C\neq0$ quoted in §*What Is Specific to the Real Interpretation*.
- [The Left and Right Multiplications of the General Quaternionic Sesquilinear Product](the-left-and-right-multiplications-of-the-quaternionic-sesquilinear-product.html), for the two one-sided families over $\mathbb{C}$, which this article reads over $\mathbb{R}$.
- [The Krein Norm of the Biquaternion Algebra](the-krein-norm-of-the-biquaternion-algebra.html), for the form, its inertia, its coefficient Gram matrix and its null cone, which the passage does not move.
- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html) and [The Four General Products and Their Relations](the-four-general-products-and-their-relations.html), for the twelve structures and the four general products.
