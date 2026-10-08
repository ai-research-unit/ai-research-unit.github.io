
# __The Six Subspaces under the General Quaternionic Algebra of Biquaternions__

## Introduction

The general quaternionic bilinear form $\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$, whose diagonal is the biquaternion norm, is read here on the six distinguished real subspaces of *Introduction to the Six Subspaces* – the centre, the vector subspace, the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace. On each, separating the real and imaginary parts of the coefficients turns the restriction into a real symmetric form, and this article records the six signatures, the restriction Gram matrices, the two definite rows and the maximal definite subspaces, the isotropic lines of each indefinite restriction, and the automorphism group of each restriction.

This article is the development of the restriction table stated in *The Four Pairings of the Biquaternion Algebra*; the form itself, its polarisation and its quadratic space are in *Biquaternion Norm and Invertibility*. The signatures are the ones recorded in *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*; the six subspaces are *Introduction to the Six Subspaces*; the other three forms on the same six subspaces are *The Six Subspaces under the General Plain Algebra of Biquaternions*, *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* and *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*; and the null structure of the form on the subspaces is *The Isotropic Structure of the General Quaternionic Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu$, $q_\mu,q'_\mu\in\mathbb{R}$, so that $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ on the eight real basis elements. The norm is $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$. The six subspaces are $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$, $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$, $i\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{ie_0,ie_1,ie_2,ie_3\}$, $\mathbb{M}_+=\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ and $\mathbb{M}_-=\mathbb{R}\{ie_0,e_1,e_2,e_3\}$.

## The Six Signatures and the Restriction Matrices

The restriction of the form to a subspace is the real symmetric form obtained by taking the real part on the real span; because the form is $\mathbb{C}$-bilinear and $i$ is central, the cross terms between a real direction and its imaginary companion are purely imaginary and drop out, so the restricted form is diagonal in the natural real basis.

| Subspace | Real basis | Restricted norm | Gram matrix | Signature |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_0,\,ie_0$ | $q_0^2-(q'_0)^2$ | $\operatorname{diag}(1,-1)$ | $(1,1)$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $e_k,\,ie_k$ | $\sum_k\bigl(q_k^2-(q'_k)^2\bigr)$ | $\operatorname{diag}(I_3,-I_3)$ | $(3,3)$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_0,e_1,e_2,e_3$ | $\sum_\mu q_\mu^2$ | $I_4$ | $(4,0)$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,ie_1,ie_2,ie_3$ | $-\sum_\mu(q'_\mu)^2$ | $-I_4$ | $(0,4)$ |
| Hermitian $\mathbb{M}_+$ | $e_0,ie_1,ie_2,ie_3$ | $q_0^2-\sum_k(q'_k)^2$ | $\operatorname{diag}(1,-1,-1,-1)$ | $(1,3)$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_0,e_1,e_2,e_3$ | $\sum_kq_k^2-(q'_0)^2$ | $\operatorname{diag}(-1,1,1,1)$ | $(3,1)$ |

**Proposition (the matrices).** In the natural real basis displayed, the Gram matrix of the restricted form is the one tabulated; each restriction is non-degenerate, and its determinant is $\pm1$.

*Proof.* The entries are $\langle u,v\rangle_{\natural}=\mathrm{Sc}(uv^{\natural})$ for $u,v$ among the real basis of the subspace; a real basis element is $e_\mu$ or $ie_\mu$, and $\mathrm{Sc}(e_\mu e_\nu^{\natural})=\delta_{\mu\nu}$, $\mathrm{Sc}(e_\mu(ie_\nu)^{\natural})=-i\delta_{\mu\nu}$, $\mathrm{Sc}(ie_\mu e_\nu^{\natural})=i\delta_{\mu\nu}$ and $\mathrm{Sc}(ie_\mu(ie_\nu)^{\natural})=-\delta_{\mu\nu}$. The cross entries are purely imaginary, hence zero in the real part, and the two within-block entries give the displayed diagonal. Each matrix is invertible, of determinant $\pm1$. Verified on the six real Gram matrices: their diagonals are as displayed and their eigenvalues are the stated signs.

**Remark (the index and the defect of each restriction).** The **index** of a restriction is the number of negative entries of its signature, and the **defect** or radical is the subspace orthogonal to the whole restriction. The six restrictions are non-degenerate, their Gram matrices having determinant $\pm1$, so every defect is trivial; the six indexes are $1$, $3$, $0$, $4$, $3$ and $1$, read from the signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$. The index of the whole realified form on $\mathbb{R}^8$ is $4$, of signature $(4,4)$, and its defect is trivial too; that whole-form reading is in *The Isotropic Structure of the General Quaternionic Algebra*.

**Remark (why the cross terms drop).** The vanishing of the cross block is not a numerical accident: it is the statement that a real direction and its imaginary companion are orthogonal for the realified form, while the form takes the value $i$ between them before the real part is taken. The same computation gives the realification of the whole form, $\operatorname{diag}(I_4,-I_4)$ of signature $(4,4)$, of which the six tables are the restrictions to the displayed subspaces.

**Remark (the realified matrix in the two orderings).** The realification is worth displaying once in each of its two natural orderings. In the grouped basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, the four real directions first, the matrix is the block diagonal $\operatorname{diag}(I_4,-I_4)$; in the interleaved basis $e_0,ie_0,e_1,ie_1,e_2,ie_2,e_3,ie_3$, each complex direction kept beside its companion, it is $\operatorname{diag}(1,-1,1,-1,1,-1,1,-1)$, and the two differ only by the permutation that carries one ordering to the other. The four blocks of the interleaved reading are the centre and the three vector directions, and the six subspaces of this article are cut from them in three ways: one block at a time, which gives the centre; all four blocks together, which gives the vector subspace; and the real or the imaginary half of all four, which gives the quaternion and anti-quaternion subspaces, with the two Hermitian subspaces obtained by exchanging the half of the centre block alone. Every restriction Gram matrix of the table is a submatrix of this diagonal matrix, in the order of signs displayed. Verified: the interleaved diagonal is as stated, and the grouped and interleaved matrices differ by the permutation of the four real directions.

## The Definite Rows and the Maximal Definite Subspaces

The **quaternion subspace** carries the signature $(4,0)$ and the **anti-quaternion subspace** the signature $(0,4)$: these are the definite rows, exchanged by multiplication by $i$, under which the norm changes sign,

$$
\langle i\tilde P,i\tilde Q\rangle_{\natural}=-\langle\tilde P,\tilde Q\rangle_{\natural}.
$$

The quaternion subspace is thus a **maximal positive definite** subspace of the norm, of dimension $4$, and the anti-quaternion subspace a maximal negative definite one; they are orthogonal complements for the realified form, $\mathbb{H}_{\mathbb B}\oplus i\mathbb H_{\mathbb B}=\mathbb B$, since the real part of the pairing of a real direction with its imaginary companion vanishes, while the complex pairing itself takes the value $i$ between them; and the norm is the positive form on the first and its negative on the second. This splitting is the one the norm uses to decide invertibility: on a definite subspace the restriction vanishes only at the origin, so no nonzero element of either quaternion subspace is a zero divisor, and the classical quaternion algebra $\mathbb{H}_{\mathbb B}$ is a division algebra.

**Proposition (the maximal definite dimensions).** The maximal dimension of a positive definite subspace of the realified form is $4$, attained by $\mathbb{H}_{\mathbb B}$, and the maximal dimension of a negative definite subspace is $4$, attained by $i\mathbb H_{\mathbb B}$; inside the four indefinite rows the maximal definite dimensions are $1$ on the centre, $3$ on the vector subspace, $1$ (positive) and $3$ (negative) on the Hermitian subspace and $3$ (positive) and $1$ (negative) on the anti-Hermitian one.

*Proof.* Each bound is the smaller of the two inertia indices of the restricted form, read from its signature; the bound is attained by the span of the basis elements carrying the corresponding signs, which is definite because the restricted Gram matrix is diagonal in that basis. For the whole algebra the two bounds are the two dimensions of the definite rows, which add to the total dimension $8$ and are complementary. Verified on the diagonal Gram matrices.

## The Isotropic Lines of the Indefinite Restrictions

Three of the six restrictions are indefinite with an isotropic cone; the centre is indefinite but anisotropic over $\mathbb{C}$; the two definite rows have no isotropic element.

**The vector subspace.** The restriction is the complex quadratic $\sum_kQ_k^2$ on $\mathbb{C}\{e_1,e_2,e_3\}$, the pure zero-divisor cone of *Biquaternion Zero Divisors*. Its isotropic **complex** lines are the points of the conic $\{[Q]\in\mathbb{P}^2:\sum_kQ_k^2=0\}$; the line $\mathbb{C}(e_1+ie_2)$ is one of them, and the maximal totally isotropic dimension is $1$ over $\mathbb{C}$ and $3$ over $\mathbb{R}$, the realification having signature $(3,3)$ and the real $3$-space $\mathbb{R}\{e_1+ie_1,e_2+ie_2,e_3+ie_3\}$ being totally isotropic. The cone has real dimension $4$.

**The Hermitian and anti-Hermitian subspaces.** The restrictions are the two real forms of the interval, of signatures $(1,3)$ and $(3,1)$; their null sets are the two real light cones, of real dimension $3$, and the isotropic **real** lines of a light cone are parametrised by the real unit directions. The maximal totally isotropic dimension is $1$ in each, a null line; the non-pure zero divisors are the elements of these two cones.

**The centre.** The restriction is the hyperbolic plane $q_0^2-(q'_0)^2$, so the realified restriction vanishes on the two real lines $\mathbb{R}(e_0+ie_0)$ and $\mathbb{R}(e_0-ie_0)$; the general plain bilinear form $N$ itself, however, reads $Q_0R_0$ on the complex line $\mathbb{C}e_0$, which is anisotropic, so the centre has no isotropic line for $N$ and its null set is $\{0\}$. The two statements are the two readings of the same restriction, the realified one and the complex one, and they must not be confused.

**The isotropic-line count.** Intersected with the six subspaces, the null cone has the real dimensions $0$, $4$, $0$, $0$, $3$ and $3$ in the order of the table, being empty off the origin on the two definite rows.

| Subspace | Null set of the restriction | Real dimension | Isotropic lines | Max totally isotropic |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb B}$ | $\{0\}$ for $N$; two lines for the realified form | $0$ | none for $N$ | $0$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | the complex cone $\sum_kQ_k^2=0$ | $4$ | the conic in $\mathbb{P}^2$ | $1$ over $\mathbb{C}$, $3$ over $\mathbb{R}$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $\{0\}$ | $0$ | none | $0$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $\{0\}$ | $0$ | none | $0$ |
| Hermitian $\mathbb M_+$ | the real light cone | $3$ | $S^2$ of null directions | $1$ |
| Anti-Hermitian $\mathbb M_-$ | the real light cone | $3$ | $S^2$ of null directions | $1$ |

## The Automorphism Group of Each Restriction

**Proposition.** The automorphism group of the restriction of the form to a subspace is the real orthogonal group of its signature,

$$
O(1,1),\quad O(3,3),\quad O(4),\quad O(4),\quad O(1,3),\quad O(3,1)
$$

on the centre, the vector subspace, the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace. Their real dimensions are $1$, $15$, $6$, $6$, $6$, $6$; the two definite ones are the quaternion and anti-quaternion rows, and the two real forms give the isomorphic groups $O(1,3)$ and $O(3,1)$, the two real forms of the same complex group.

*Proof.* A real-linear automorphism of a non-degenerate real symmetric form of signature $(p,q)$ is an element of $O(p,q)$; the dimension of $O(p,q)$ is $n(n-1)/2$ with $n=p+q$, giving $1$, $15$ and $6$; and the restrictions are non-degenerate by the determinant computation above. The definite rows give the groups $O(4)$; the two real forms give the isomorphic groups $O(1,3)$ and $O(3,1)$. Verified: the dimensions are the ranks of the antisymmetry conditions $X^{\mathsf T}G+GX=0$ for the six Gram matrices.

| Subspace | Restriction | Automorphism group | Real dimension | Definite |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb B}$ | $(1,1)$ | $O(1,1)$ | $1$ | no |
| Vector $\mathrm{Vect}(\mathbb B)$ | $(3,3)$ | $O(3,3)$ | $15$ | no |
| Quaternion $\mathbb H_{\mathbb B}$ | $(4,0)$ | $O(4)$ | $6$ | yes |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $(0,4)$ | $O(4)$ | $6$ | yes |
| Hermitian $\mathbb M_+$ | $(1,3)$ | $O(1,3)$ | $6$ | no |
| Anti-Hermitian $\mathbb M_-$ | $(3,1)$ | $O(3,1)$ | $6$ | no |

**Remark (the restriction group is not induced by the ambient group).** The automorphism groups of the table are the largest groups preserving the restricted form, and they are not the restrictions of the automorphism group of the ambient form: an automorphism of a subspace need not extend to the algebra, and conversely an automorphism of the whole form need not preserve a subspace. The ambient group is the complex orthogonal group $O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$ (*Biquaternion Norm and Invertibility*, §*The Polarisation and the Complex Quadratic Space*); the group of real-linear automorphisms of the realified form is the larger $O(4,4)$, of real dimension $28$, and is not the subject of this article. The two definite rows of the table are the quaternion and anti-quaternion ones, and the four rows that carry an isotropic cone have indefinite automorphism groups.

## Worked Examples

**A null element of the realified centre.** For $\tilde Q=e_0+ie_0$ the realified restriction of the centre gives $1^{2}-1^{2}=0$, while the complex form gives $N(\tilde Q)=(1+i)^{2}=2i\neq0$: the element is null for the realified form and is not a zero divisor, which is the pair of readings the centre section records.

**A pure zero divisor.** For $\tilde Q=e_1+ie_2$ the norm is $N=1+i^{2}=0$, and the element lies on the isotropic cone of the vector subspace, on the conic $\sum_kQ_k^{2}=0$ in $\mathbb{P}^{2}$; it is the line of the vector-subspace table.

**An element of a definite row.** For $\tilde Q=e_0+e_1$ in the quaternion subspace the norm is $N=2$, and for $\tilde Q=ie_0+ie_1$ in the anti-quaternion subspace it is $N=-2$: both are units, in agreement with the definiteness of the two rows, where no nonzero element is null.

**The twist on a definite row.** For $\tilde Q=e_0+e_1$ the quaternion form gives $2$ and the $\varepsilon$-twisted form gives $1-1=0$, so the same element is a unit of the first form and a null element of the second: the exchange of the definite rows is visible on a single element, and it is the sign of the second coordinate that is responsible.

**A non-pure zero divisor.** For $\tilde Q=e_0+ie_1$ the norm is $N=1+i^{2}=0$, and the element lies on the real light cone of the Hermitian subspace $\mathbb{M}_+$, of signature $(1,3)$; it is a zero divisor that is neither pure nor in the vector subspace, the two statements being the classification of *Biquaternion Zero Divisors*.

**A maximal definite subspace of an indefinite row.** In the vector subspace, of signature $(3,3)$, the span $\mathbb{R}\{e_1,e_2,e_3\}$ is a maximal positive definite subspace of dimension $3$ and the span $\mathbb{R}\{ie_1,ie_2,ie_3\}$ a maximal negative definite one; the two are orthogonal for the realified form, since the pairing of a real direction with its imaginary companion is purely imaginary, and are exchanged by multiplication by $i$, which is the local form of the exchange of the two definite rows of the whole algebra.

**An automorphism of a restriction that does not extend.** The real orthogonal group $O(4)$ of the quaternion subspace contains the reflection in the direction $e_1$, but no element of the ambient automorphism group $O_4(\mathbb{C})$ restricts to it and fixes the anti-quaternion subspace pointwise, because the two definite rows are not orthogonal for the bilinear form (the pairing of $e_1$ with $ie_1$ is $i$); a form-preserving map that fixes one row pointwise is therefore constrained on the other, and the restriction groups of the table are larger than the restrictions of the ambient group.

**The definite rows are not the real forms.** The two definite rows are $\mathbb{H}_{\mathbb B}$, on which the form is $\sum_\mu q_\mu^{2}$, all signs $+1$, and $i\mathbb{H}_{\mathbb B}$, on which it is $-\sum_\mu q_\mu^{2}$, all signs $-1$; the Hermitian and anti-Hermitian subspaces, by contrast, are indefinite of signatures $(1,3)$ and $(3,1)$. The reason is that the Hermitian subspace $\mathbb{M}_+=\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ collects the single positive direction $e_0$ with the three negative directions $ie_k$, while the anti-Hermitian subspace $\mathbb{M}_-=\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ collects the single negative direction $ie_0$ with the three positive directions $e_k$; neither is spanned by directions of a single sign, which is what definiteness requires.

**A null element of the anti-Hermitian subspace.** For $\tilde Q=ie_0+e_1$ the norm is $N=i^{2}+1=0$, on the real light cone of $\mathbb{M}_-$, of signature $(3,1)$; the sign of the null direction is the one the swapped table prescribes.

## Summary

On the six distinguished real subspaces the general quaternionic bilinear form carries the signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$, with the restriction Gram matrices $\operatorname{diag}(1,-1)$, $\operatorname{diag}(I_3,-I_3)$, $I_4$, $-I_4$, $\operatorname{diag}(1,-1,-1,-1)$ and $\operatorname{diag}(-1,1,1,1)$ in the natural real bases. The quaternion and anti-quaternion subspaces are the two definite rows, of dimension $4$ and maximal, and they are orthogonal complements for the realified form and exchanged by multiplication by $i$, which reverses the sign of the pairing; the centre and the vector subspace carry $(1,1)$ and $(3,3)$; the two real forms carry $(1,3)$ and $(3,1)$. The isotropic elements are the pure zero divisors on the vector subspace – the complex cone $\sum_kQ_k^2=0$, whose isotropic complex lines form a conic – and the non-pure zero divisors on the two real forms, whose isotropic real lines are parametrised by the real unit directions; the centre is indefinite but anisotropic over $\mathbb{C}$, and the two definite subspaces contain no isotropic element. The automorphism group of each restriction is the real orthogonal group of its signature, $O(1,1)$, $O(3,3)$, $O(4)$, $O(4)$, $O(1,3)$ and $O(3,1)$. The other three pairings on the same six subspaces are *The Six Subspaces under the General Plain Algebra of Biquaternions*, *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* and *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*, where the transposition of this table with the general plain bilinear one is read on the four real forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the six signatures of the norm |
| $\operatorname{diag}(I_3,-I_3)$, $I_4$, $-I_4$ | the restriction Gram matrices of the vector, quaternion and anti-quaternion rows |
| $\operatorname{diag}(I_4,-I_4)$ | the Gram matrix of the realified form in the grouped real basis $e_0,\dots,e_3,ie_0,\dots,ie_3$ |
| $\mathbb{R}(e_0\pm ie_0)$ | the two null lines of the realified centre |
| $\mathbb H_{\mathbb B}\oplus i\mathbb H_{\mathbb B}$ | the maximal definite splitting of the algebra |
| $\langle i\tilde P,i\tilde Q\rangle_{\natural}=-\langle\tilde P,\tilde Q\rangle_{\natural}$ | the sign change pairing the definite rows |
| $O(1,1),O(3,3),O(4),O(4),O(1,3),O(3,1)$ | the automorphism groups of the six restrictions |

## Further Reading

- *The Six Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the companion table of the same six subspaces
- *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`) and *The Six Subspaces under the Real Biquaternion Algebra* (`articles_maths/the-six-subspaces-under-the-real-biquaternion-algebra.md`), for the same six subspaces under the other readings
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms on the six subspaces, side by side
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm and its real forms
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra.md`), for the null cone on the subspaces
- *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the operators that preserve the form
