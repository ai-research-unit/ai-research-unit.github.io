# __The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ is alternating and vector valued, it has no unit, and it fails the Jacobi identity (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*, *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*). A Lie algebra carries its invariant bilinear forms, the symmetric $\beta$ with $\beta([x,y],z)+\beta(y,[x,z])=0$, whose prototype is the Killing form, and the block of this article is an antisymmetrisation for which the Jacobi identity fails; the question of the block's own invariant forms is therefore well posed even though the classical theory does not apply, and this article answers it.

The answer has three parts. The space of forms invariant under the block is **one-dimensional**, spanned by the form $\varphi(\tilde P,\tilde Q)=P_0Q_0$ that reads the two scalar parts; the invariant form is symmetric, its radical is the whole vector subspace, and there is no nonzero alternating invariant form. The **trace form vanishes**, the block being of scalar part zero, so the coefficient form of the block is zero and cannot serve as the invariant form. And the substitution that suggests itself in the absence of a Jacobi identity, the trace form of the multiplication operators $\operatorname{Tr}(L_{\tilde A}L_{\tilde B})$, is computed, is non-degenerate, and is **not invariant**: its failure is the same obstruction as the Jacobi failure. The article closes with the restriction of the forms to the remarkable subspaces and with the comparison with the adjacent Lie case $\mathrm{APA}$, which does carry a Killing form (*The Killing Form of the Antisymmetric Plain Algebra*).

The forms of the parent quaternionic algebra are *Comparison Between the Four General Products* and *The Four Pairings of the Biquaternion Algebra*; the forms of the associative algebra $\mathbb{B}$ are the same four, read in the coefficient basis. None of those is a form of the block, and the form $\varphi$ below is not the $\natural$-form $\langle\tilde P,\tilde Q\rangle_\natural=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ of the parent product, which also reads the vector parts.

## The Invariance Condition

**Definition.** A $\mathbb{C}$-bilinear form $\beta:\mathbb{B}\times\mathbb{B}\to\mathbb{C}$ is **invariant under the block** if

$$
\beta(\tilde P\diamond\tilde Q,\tilde R) + \beta(\tilde Q,\tilde P\diamond\tilde R) = 0
$$

for all $\tilde P,\tilde Q,\tilde R$; equivalently, for a symmetric $\beta$, if $\beta(\tilde P\diamond\tilde Q,\tilde R)=\beta(\tilde P,\tilde Q\diamond\tilde R)$ for all triples. This is the classical invariance condition of a Lie algebra, $\beta([x,y],z)+\beta(y,[x,z])=0$, read for the operation of the block.

**Proposition.** For a symmetric $\beta$ the second condition implies the first, for any alternating operation, and for the block of this article the two conditions are equivalent, both returning the same one-dimensional space. The condition is $\mathbb{C}$-linear in $\beta$, so the invariant forms of the block form a vector space.

*Proof.* If (II) holds then $\beta(\tilde Y,\tilde X\diamond\tilde Z)=\beta(\tilde Y\diamond\tilde X,\tilde Z)=-\beta(\tilde X\diamond\tilde Y,\tilde Z)$, where the first equality is (II) with the first two arguments exchanged and the second is the antisymmetry of the operation; that is (I). For the converse, write $G$ for the Gram matrix of $\beta$ and $M_{\tilde A}$ for the matrix of the operator of $\tilde A$; then (I) is the matrix condition $M_{\tilde A}^{\mathsf T}G+GM_{\tilde A}=0$ and (II) is $M_{\tilde A}^{\mathsf T}G-GM_{\tilde A}=0$, and solving either over the four basis operators gives the same solution, $G_{00}$ free and the other entries zero. So for the block the two are equivalent, and both single out the multiples of $\varphi$. Linearity in $\beta$ is immediate from the definition, the two terms being linear in $\beta$. $\square$

## The Space of Invariant Forms

**Theorem (the invariant forms).** The space of $\mathbb{C}$-bilinear forms invariant under the block is one-dimensional, spanned by

$$
\varphi(\tilde P,\tilde Q) = P_0Q_0 ,
$$

the product of the two scalar parts. Every invariant form is a multiple of $\varphi$.

*Proof.* Let $G$ be the Gram matrix of $\beta$ in the coefficient basis, $G_{\mu\nu}=\beta(e_\mu,e_\nu)$, and let $M_{\tilde A}$ be the matrix of the left multiplication operator $L_{\tilde A}$, so that the coordinate vector of $\tilde A\diamond e_\nu$ is the $\nu$-th column of $M_{\tilde A}$, determined by the table of the block. Writing $\beta(\tilde X,\tilde Y)=X^{\mathsf T}G\,Y$ for the coordinate columns, the condition at $\tilde P=e_\mu$, $\tilde Q=e_\nu$, $\tilde R=e_\rho$ reads $M_{\tilde A}^{\mathsf T}G+GM_{\tilde A}=0$ for every $\tilde A$, and the four basis elements $\tilde A=e_0,e_1,e_2,e_3$ generate it. Solving the sixty-four equations $\beta(e_\mu\diamond e_\nu,e_\rho)+\beta(e_\nu,e_\mu\diamond e_\rho)=0$ over the sixteen entries of $G$ gives $G_{00}=g$ free and $G_{\mu\nu}=0$ otherwise; the solution space is one-dimensional, with basis $\varphi$. $\square$

**Remark (why the scalar form survives).** The operation has zero scalar part, so $\varphi(\tilde P\diamond\tilde Q,\tilde R)=(\tilde P\diamond\tilde Q)_0R_0=0$ and the first term of the condition vanishes for every triple; and $\varphi(\tilde Q,\tilde P\diamond\tilde R)=Q_0(\tilde P\diamond\tilde R)_0=0$ likewise. The form $\varphi$ is invariant for the trivial reason that both of its terms vanish, and it is the only form for which that happens on the scalar slot. A form that reads a vector slot, such as the quaternion form $B$, is not invariant, because the block moves the scalar part into the vector part and the mixed terms then survive in the condition.

**Proposition (the Gram matrix and the rank).** The Gram matrix of $\varphi$ in the coefficient basis $e_0,e_1,e_2,e_3$ is $\operatorname{diag}(1,0,0,0)$, of rank $1$.

*Proof.* $\varphi(e_\mu,e_\nu)=\delta_{\mu0}\delta_{\nu0}$, by the definition of the scalar part. $\square$

## The Trace Form Vanishes

**Proposition.** The coefficient form of the block vanishes identically,

$$
\mathrm{Sc}\,(\tilde P\diamond\tilde Q) = 0 \qquad \text{for all } \tilde P,\tilde Q ,
$$

so the trace form of the block, the bilinear form that reads the scalar part of the product, is the zero form and is not an invariant form of the block.

*Proof.* The scalar part of the value is zero by the explicit form, the value being a pure vector. The trace form of the block is therefore zero as a bilinear form, and the zero form is invariant but carries no information; it is a multiple of $\varphi$, so it is not a second invariant form. $\square$

The vanishing is the structural difference from the plain row. The plain product has the trace form $\mathrm{Sc}(\tilde P\tilde Q)$ and its symmetrisation; the block removes the scalar part, and with it the trace form. There is no coefficient attached to the block's values, because the values have no coefficient to read.

## The Symmetric and the Alternating Parts

**Proposition.** The single invariant form $\varphi$ is symmetric, and there is no nonzero alternating invariant form; the space of invariant forms splits as one dimension symmetric and zero alternating, and the two parts are invariant subspaces of the condition.

*Proof.* $\varphi(\tilde P,\tilde Q)=P_0Q_0=\varphi(\tilde Q,\tilde P)$, so $\varphi$ is symmetric. The solution of the same linear system with the added antisymmetry $G^{\mathsf T}=-G$ is $G=0$: the solution space of the system without the added symmetry is one-dimensional and its basis is symmetric, so its only antisymmetric element is zero. The condition is preserved by the transposition of $\beta$, so the symmetric and the alternating forms may be searched for separately, and the search returns one dimension and zero. $\square$

## The Radical

**Proposition (the radical).** The radical of $\varphi$, the set of $\tilde X$ with $\varphi(\tilde X,\tilde Y)=0$ for all $\tilde Y$, is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three; the isotropic elements of $\varphi$, those with $\varphi(\tilde X,\tilde X)=0$, are the same set.

*Proof.* $\varphi(\tilde X,\tilde Y)=X_0Y_0$ vanishes for all $\tilde Y$ exactly when $X_0=0$, that is when $\tilde X$ is a pure vector; and $\varphi(\tilde X,\tilde X)=X_0^2$ vanishes exactly when $X_0=0$. The radical and the isotropic cone therefore coincide with the kernel of the scalar part. $\square$

The form is thus as degenerate as it can be without being zero: its rank is one, its radical is the three-dimensional image of the block, and the isotropic elements are exactly the elements the block produces. The form reads only the one-dimensional quotient $\mathbb{B}/\mathrm{Vect}(\mathbb{B})$ and is non-degenerate there, so it is the pull-back of a one-dimensional form along the scalar-part map.

## The Adjoint of the Operator with Respect to a Form

**Proposition (the adjoint is undetermined).** With respect to the invariant form $\varphi$ the adjoint of a multiplication operator is not determined: $\varphi(L_{\tilde A}\tilde X,\tilde Y)=0$ for all $\tilde X,\tilde Y$, so every operator is adjoint to $0$ modulo the radical, and the form is too degenerate to define the adjoint uniquely.

*Proof.* $L_{\tilde A}\tilde X=\tilde A\diamond\tilde X$ is a pure vector, so its scalar part is zero, and $\varphi(L_{\tilde A}\tilde X,\tilde Y)=(L_{\tilde A}\tilde X)_0Y_0=0$. The adjoint $(L_{\tilde A})^*$ is defined by $\varphi(L_{\tilde A}\tilde X,\tilde Y)=\varphi(\tilde X,(L_{\tilde A})^*\tilde Y)$; the left side vanishes for all $\tilde X$, so $(L_{\tilde A})^*\tilde Y$ lies in the radical for every $\tilde Y$, and the freedom in the adjoint is the freedom of the radical. $\square$

The degeneracy is the reason the invariant form is not the form to adjoint against, and the next section supplies the substitution: a non-degenerate form on the operators, on which the adjoint is determined.

## The Operator Trace Form and Its Failure of Invariance

**Definition.** The **operator trace form** of the block is

$$
K(\tilde A,\tilde B) = \operatorname{Tr}\bigl(L_{\tilde A}L_{\tilde B}\bigr) ,
$$

the trace of the composition of the two left multiplication operators.

**Proposition (the operator trace form is non-degenerate).** For all $\tilde A,\tilde B$,

$$
K(\tilde A,\tilde B) = 3A_0B_0 - 2\sum_{k=1}^{3}A_kB_k ,
$$

its Gram matrix in the coefficient basis is $\operatorname{diag}(3,-2,-2,-2)$, of rank $4$, and the form is non-degenerate.

*Proof.* The matrix of $L_{\tilde A}$ is read off the table, and the trace of the product is computed entry by entry; the diagonal entries of $L_{\tilde A}$ are $0,A_0,A_0,A_0$ on the scalar line and the three vector lines, and the off-diagonal contributions of the two factors give the cross terms. The determinant of $\operatorname{diag}(3,-2,-2,-2)$ is $3\cdot(-2)^3=-24$, nonzero. $\square$

**Proposition (it is not invariant).** The operator trace form is not invariant under the block. The failure

$$
F(\tilde A,\tilde B,\tilde C) = K(\tilde A\diamond\tilde B,\tilde C)+K(\tilde B,\tilde A\diamond\tilde C) = -4A_0(\mathbf B,\mathbf C)+2B_0(\mathbf A,\mathbf C)+2C_0(\mathbf A,\mathbf B)
$$

does not vanish identically; at $(\tilde A,\tilde B,\tilde C)=(e_0,e_1,e_1)$ it is $K(e_1,e_1)+K(e_1,e_1)=-2-2=-4$.

*Proof.* Insert the explicit form into the two terms and collect. Each term is twice a scalar product of the vector part of the first argument with the third, since the first factor of $K$ is a scalar product on the vector lines; at the displayed triple the two terms are each $K(e_1,e_1)=-2$, and the sum is $-4$. The general expression is the one displayed, and it is nonzero for a general triple. $\square$

The operator trace form is thus the natural substitution for the Killing form and it does not serve. It is symmetric, non-degenerate and canonical, and it fails the one property the theory needs. This is the expected outcome of the absence of a Jacobi identity: the Killing form of a Lie algebra is invariant because the Jacobi identity makes the adjoint representation a representation, and here the adjoint map is not a representation, so the trace form of the operators is not invariant either. The substitute computed here is therefore a form of the *operators* and not an invariant form of the *block*, and the only invariant form of the block remains the degenerate $\varphi$.

## The Restriction to the Remarkable Subspaces

**Proposition (the restrictions of $\varphi$).** On the remarkable subspaces the form $\varphi$ restricts as follows, with the scalar coordinate the one indicated,

| subspace | the scalar coordinate | $\varphi$ | signature on the real basis | radical |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $A_0\in\mathbb{C}$ | $A_0B_0$ | $(1,1)$ | $0$ |
| $\mathrm{Vect}(\mathbb{B})$ | none | $0$ | $(0,0)$ | all |
| $\mathbb{H}_{\mathbb{B}}$ | $a_0\in\mathbb{R}$ | $a_0b_0$ | $(1,0)$ | $\mathbb{R}\{e_1,e_2,e_3\}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ia_0$, $a_0\in\mathbb{R}$ | $-a_0b_0$ | $(0,1)$ | $\mathbb{R}\{ie_1,ie_2,ie_3\}$ |
| $\mathbb{M}_{+}$ | $a_0\in\mathbb{R}$ | $a_0b_0$ | $(1,0)$ | $\mathbb{R}\{ie_1,ie_2,ie_3\}$ |
| $\mathbb{M}_{-}$ | $ia_0$, $a_0\in\mathbb{R}$ | $-a_0b_0$ | $(0,1)$ | $\mathbb{R}\{e_1,e_2,e_3\}$ |

*Proof.* The form reads the two scalar parts; the remarkable subspaces are distinguished by their scalar and vector lines (*Introduction to the Remarkable Subspaces*). The centre has the scalar line $e_0,ie_0$ and no vector line, so the form is the complex product $A_0B_0$ there, non-degenerate over $\mathbb{C}$, of real rank two and real signature $(1,1)$ as the realification of the complex form prescribes; the vector subspace has no scalar line, so the form is zero there. The four four-dimensional subspaces have a scalar line of real dimension one and a vector part; on the scalar line the form is $\pm a_0b_0$, positive for $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_{+}$, whose scalar line is real, and negative for $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_{-}$, whose scalar line is the imaginary one, and the vector part lies in the radical. The signatures of the four are those of the real form $\pm a_0b_0$ on the one-dimensional scalar line. $\square$

The restriction is therefore definite wherever it is not zero, and the two negative cases are the two subspaces on which the scalar line is imaginary. The radical of the restriction is the vector part of the subspace in every case in which the subspace has a vector part, and the whole subspace in the case of $\mathrm{Vect}(\mathbb{B})$.

## The Comparison with the Lie Case

**Remark.** The adjacent block $\mathrm{APA}$ is the antisymmetrisation of the plain product, $\tilde P\wedge\tilde Q=\mathbf P\times\mathbf Q$, and it is a Lie algebra; it carries the Killing form $K_{\mathrm{A}}(\tilde P,\tilde Q)=\operatorname{Tr}(\operatorname{ad}_{\tilde P}\operatorname{ad}_{\tilde Q})$, computed on the cross product and non-degenerate on the vector subspace (*The Killing Form of the Antisymmetric Plain Algebra*). The block of this article has no such form. Its only invariant form is the degenerate $\varphi$, its coefficient form vanishes, and the trace form of its operators, $K(\tilde A,\tilde B)=3A_0B_0-2(\mathbf A,\mathbf B)$, is non-degenerate but not invariant. The comparison is the exact measure of the loss: the Killing form exists in $\mathrm{APA}$ because the Jacobi identity holds, and it fails to have an analogue here because the Jacobi identity does not. On the vector subspace, where the block is the cross product up to sign, both $K_{\mathrm A}$ and the operator trace form restrict to multiples of the same complex bilinear form $(\mathbf A,\mathbf B)$ — for $K$ the multiple is $-2$ — so the two differ only in the scalar factor, and neither is an invariant form of the block.

**Remark (the two form theories).** The block is thus the first of the twelve operations for which the invariant-form theory is degenerate and the Killing construction is unavailable. The plain antisymmetrisation is a Lie algebra and has its invariant forms; the block of this article is a deformation of it in which the two mixed terms $P_0\mathbf Q-Q_0\mathbf P$ survive, and the deformation destroys both the Jacobi identity and the invariance of the trace form. What survives is the one-dimensional form $\varphi$ on the scalar line, and it survives for the trivial reason that the block never leaves the vector subspace.

## Summary

The invariant bilinear forms of the block, the $\beta$ with $\beta(\tilde P\diamond\tilde Q,\tilde R)+\beta(\tilde Q,\tilde P\diamond\tilde R)=0$, form a one-dimensional space spanned by $\varphi(\tilde P,\tilde Q)=P_0Q_0$, the product of the two scalar parts; the form is symmetric, its Gram matrix in the coefficient basis is $\operatorname{diag}(1,0,0,0)$, its rank is $1$, its radical is the whole vector subspace, and its isotropic elements are the same vector subspace. There is no nonzero alternating invariant form. The trace form of the block vanishes identically, the values having zero scalar part, so the coefficient form of the block is the zero form. The substitution in the absence of a Jacobi identity, the operator trace form $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=3A_0B_0-2\sum_kA_kB_k$, is symmetric and non-degenerate with Gram matrix $\operatorname{diag}(3,-2,-2,-2)$, and it is **not** invariant, its failure being the scalar trilinear form $-4A_0(\mathbf B,\mathbf C)+2B_0(\mathbf A,\mathbf C)+2C_0(\mathbf A,\mathbf B)$, built from the same scalar and vector data as the cyclic sum of the block; the adjoint of a multiplication operator with respect to the invariant form is undetermined, the form being too degenerate to define it. On the remarkable subspaces the form restricts to the signed square of the scalar coordinate, non-degenerate on the centre, zero on the vector subspace, and of signature $(1,0)$ or $(0,1)$ on the four four-dimensional subspaces according to the reality of their scalar line. The adjacent Lie case $\mathrm{APA}$ carries a non-degenerate Killing form, and the block of this article has no analogue of it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\varphi(\tilde P,\tilde Q)=P_0Q_0$ | the unique invariant bilinear form of the block, up to a factor |
| $\beta(\tilde P\diamond\tilde Q,\tilde R)+\beta(\tilde Q,\tilde P\diamond\tilde R)=0$ | the invariance condition of the block |
| $\operatorname{diag}(1,0,0,0)$ | the Gram matrix of $\varphi$ in the coefficient basis |
| $\mathrm{Vect}(\mathbb{B})$ | the radical and the isotropic cone of $\varphi$ |
| $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$ | the vanishing of the trace form of the block |
| $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$ | the left multiplication operator of the block |
| $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=3A_0B_0-2\sum_kA_kB_k$ | the operator trace form, non-degenerate and not invariant |
| $\langle\tilde P,\tilde Q\rangle_\natural=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, the $\natural$-form | the form of the parent product, $P_0Q_0+(\mathbf P,\mathbf Q)$, and not a form of the block |
| $K_{\mathrm{A}}$ | the Killing form of the adjacent Lie case $\mathrm{APA}$ |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and its image
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`), for the cyclic sum whose multiples are the failure of the operator trace form
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the matrix of the operator, its trace and the derivation of the operator trace form
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the quaternion form $B$ and the forms of the parent algebra
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the forms of the associative algebra $\mathbb{B}$
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form that the adjacent Lie case carries and this block does not
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the scalar and vector lines of the remarkable subspaces
