
# __The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation__

## Introduction

The reading group *Topology on the Introduction to the General Quaternionic Sesqualgebra of Biquaternions* reads the algebra through the **general quaternionic sesquilinear form** $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{P}^{\natural*}\tilde{Q})=\sum_\mu\varepsilon_\mu\overline{P_\mu}Q_\mu$, the Krein form of *The Krein Gram Matrix and the Restrictions of the Form*, and through the **general quaternionic sesquilinear product** $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}^{*}$ that it polarises. This article reads that group through the $2\times2$ matrix realization $\mathsf{M}_2$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and it is the first of the two representation articles of the group; the companion *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Representation* repeats the reading on the left regular representation.

The two conjugations of the algebra are the two matrix operations of the model: the natural conjugation is the **adjugate** and the Hermitian conjugation is the **conjugate transpose**. The form of the group is therefore the adjugated conjugate-transpose pairing of the matrices, the **Krein form** of signature $(2,6)$ over $\mathbb{R}$ and $(1,3)$ over $\mathbb{C}$, and the product is the matrix product with the adjugate in the first slot and the conjugate transpose in the second. The natural conjugation $J={}^{\natural}$ is the fundamental symmetry of the form, and in the model it is the adjugation.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; product $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}^{*}$, form $\langle\cdot,\cdot\rangle_{\natural*}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **matrix realization** is the isomorphism written $\mathsf{M}_2$. It converts a biquaternion into a $2 \times 2$ complex matrix,

$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: $\mathsf{M}_2(e_0)=I$ on the identity and $\mathsf{M}_2(e_k)=-i\sigma_k$ on the three vector units.

The invariants and the two conjugations are

$$
\operatorname{Tr}\mathsf{M}_2(\tilde{Q})=2Q_0,\qquad \det \mathsf{M}_2(\tilde{Q})=\sum_\mu Q_\mu^2,\qquad \mathsf{M}_2(\tilde{Q}^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde{Q}),\qquad \mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger} .
$$

Both conjugations are needed here, and the model keeps them apart: the adjugate is the conjugate of the transpose by the fixed matrix $\mathsf{M}_2(-e_2)$ of determinant one, and the conjugate transpose is the other.

**The three conjugations.** The two conjugations of the group are joined by the coefficientwise complex conjugation, which in the model is neither the adjugate nor the conjugate transpose but their composite,

$$
\mathsf{M}_2(\overline{\tilde{Q}})=\operatorname{adj}\bigl(\mathsf{M}_2(\tilde{Q})^{\dagger}\bigr)=\varepsilon\,\overline{\mathsf{M}_2(\tilde{Q})}\,\varepsilon^{-1},\qquad \varepsilon=\mathsf{M}_2(-e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$

The adjugate is $\mathbb{C}$-linear and anti-multiplicative, the conjugate transpose is conjugate-linear and anti-multiplicative, and their composite is conjugate-linear and multiplicative.

## The General Quaternionic Sesquilinear Product in the Model

**Theorem (the product is the adjugated conjugate-transposed matrix product).** For all biquaternions,

$$
\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\operatorname{adj}\mathsf{M}_2(\tilde{P})\,\mathsf{M}_2(\tilde{Q})^{\dagger} ,
$$

the ordinary matrix product with the adjugate in the first slot and the conjugate transpose in the second.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}^{*}$, the realization is multiplicative, and it carries the two conjugations to the adjugate and the conjugate transpose.

**The square.** At $\tilde{P}=\tilde{Q}$ the theorem gives $\mathsf{M}_2(\tilde{Q}\star\tilde{Q})=\operatorname{adj}\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^{\dagger}$, which is neither positive semidefinite nor scalar in general; the element theory of the product is that of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, whose matrix reading is the product of the adjugate with the conjugate transpose.

**The fundamental symmetry.** The natural conjugation $J={}^{\natural}$ is an involution commuting with the complex coefficients, and in the model it is the adjugation; it is self-adjoint for the Krein form and it splits the algebra into its $+1$ and $-1$ eigenspaces, the Hermitian and anti-Hermitian subspaces.

## The Four General Products in Matrices

**Theorem (the four matrix forms).** Under $\mathsf{M}_2$ the four general products of the algebra read

| product | rule on $\mathbb{B}$ | matrix form |
|---|---|---|
| plain | $\tilde{P}\tilde{Q}$ | $M(P)M(Q)$ |
| natural-bilinear | $\tilde{P}^{\natural}\tilde{Q}$ | $\operatorname{adj}M(P)\,M(Q)$ |
| general plain sesquilinear (sibling) | $\tilde{P}\tilde{Q}^{*}$ | $M(P)M(Q)^{\dagger}$ |
| general quaternionic sesquilinear | $\tilde{P}^{\natural}\tilde{Q}^{*}$ | $\operatorname{adj}M(P)\,M(Q)^{\dagger}$ |

where $M(\tilde{X})=\mathsf{M}_2(\tilde{X})$. The four general products are the four ways of inserting the two conjugations into the two slots of the matrix product, and the fourth carries one adjugate and one conjugate transpose. It is the sesquilinear one: the first factor enters linearly and the second conjugate-linearly,

$$
\mathsf{M}_2\bigl((\lambda\tilde{P})\star\tilde{Q}\bigr)=\lambda\,\mathsf{M}_2(\tilde{P}\star\tilde{Q}),\qquad \mathsf{M}_2\bigl(\tilde{P}\star(\lambda\tilde{Q})\bigr)=\bar\lambda\,\mathsf{M}_2(\tilde{P}\star\tilde{Q}),
$$

a product with two adjugates being $\mathbb{C}$-bilinear and one with two daggers conjugate-bilinear. Substituting the transpose form of the adjugate, $\operatorname{adj}(X)=\varepsilon X^{\mathsf{T}}\varepsilon^{-1}$, the product is

$$
\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\varepsilon\,\mathsf{M}_2(\tilde{P})^{\mathsf{T}}\,\varepsilon^{-1}\,\mathsf{M}_2(\tilde{Q})^{\dagger},
$$

the plain **transpose** inserted in the first factor and the **conjugate transpose** in the second.

**The trace and the determinant of a value.** For $Z=\mathsf{M}_2(\tilde{P}\star\tilde{Q})$,

$$
\operatorname{Tr}Z=2\mathrm{Sc}(\tilde{P}\star\tilde{Q})=2\bigl(P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr),\qquad \det Z=\langle\tilde{P},\tilde{P}\rangle_{\natural}\overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}},
$$

so the determinant of a value is the norm of the first factor times the conjugate of the norm of the second. On the norm-one elements the adjugate is the inverse, so the product of two norm-one matrices computed by the twisted rule again has determinant one, which is the matrix form of the closure of the units under the product.

## The Idempotents in Matrices

**Theorem (the matrix idempotent equation).** An element $\tilde{\Pi}$ is idempotent for the multiplication if and only if its matrix $M=\mathsf{M}_2(\tilde{\Pi})$ satisfies

$$
\operatorname{adj}(M)\,M^{\dagger}=M .
$$

For an invertible idempotent this is equivalent to $\det(M)M^{\dagger}=M^{2}$, and for an idempotent of norm one to $M^{\dagger}=M^{2}$. The matrix of an idempotent is therefore not a projection in general, nor is the matrix of a projection an idempotent: $\operatorname{diag}(1,\omega)$ satisfies $M^{2}=M^{\dagger}$ but not the idempotent equation, so the adjugate is essential.

**Theorem (the family of idempotents as a unitary orbit).** The nontrivial idempotents of the multiplication are exactly the elements whose matrices are the unitary conjugates of the diagonal matrix $\operatorname{diag}(\omega,\omega^{2})$, where $\omega=e^{2\pi i/3}$:

$$
\tilde{\Pi}\longleftrightarrow M=U\operatorname{diag}(\omega,\omega^{2})U^{\dagger},\qquad U\in U(2).
$$

*Proof.* A norm-one idempotent satisfies $M^{\dagger}=M^{2}$; applying the dagger gives $(M^{\dagger})^{2}=M$, and substituting yields $M^{4}=M$, so $M^{3}=I$ for the invertible $M$. Then $MM^{\dagger}=MM^{2}=M^{3}=I$ and $M^{\dagger}M=I$, so $M$ is unitary of determinant one, and a unitary matrix with $M^{3}=I$ and $\det M=1$ has spectrum $\{1,1\}$ or $\{\omega,\omega^{2}\}$; the first case is $M=I$, the identity $\tilde{\Pi}=e_0$, and the second, by the spectral theorem, is the displayed unitary conjugacy class. Conversely each matrix of the class satisfies $M^{\dagger}=M^{2}$, $M^{3}=I$ and $\det M=1$, hence $\operatorname{adj}(M)M^{\dagger}=\det(M)M^{-1}M^{2}=M$. The trace of $\operatorname{diag}(\omega,\omega^{2})$ is $\omega+\omega^{2}=-1$, so $Q_0=-\tfrac12$; $\operatorname{adj}(M^{\dagger})=\operatorname{adj}(M^{2})=\operatorname{adj}(M)^{2}=M^{-2}=M$ gives $\mathsf{M}_2(\overline{\tilde{\Pi}})=\mathsf{M}_2(\tilde{\Pi})$, so the three vector coordinates are real; and unitarity gives $\sum_\mu|Q_\mu|^{2}=1$, so $|Q_1|^{2}+|Q_2|^{2}+|Q_3|^{2}=\tfrac34$. The class is connected of real dimension two, the family of the idempotents. $\square$

**Corollary (the order-three matrices).** The matrix of a nontrivial idempotent satisfies $M^{3}=I$, $M^{\dagger}=M^{2}=M^{-1}$ and $\det M=1$; consequently $\operatorname{Tr}M=-1$ and the characteristic polynomial is $\lambda^{2}+\lambda+1$. The nontrivial idempotents are therefore units, and they are disjoint from the zero divisors: in the model they are unitary matrices of order three, while the zero divisors are the singular matrices, $N(\tilde{Q})=\det \mathsf{M}_2(\tilde{Q})=0$. This is the sharpest contrast with the sibling general plain sesquilinear product, where the nontrivial idempotents are the rank-one Hermitian projections and are singular.

## The Associator and the Operators in Matrices

**Theorem (the associator).** With $M(\tilde{X})=\mathsf{M}_2(\tilde{X})$, the associator of the product has the matrix form

$$
\mathsf{M}_2\bigl([\tilde{P},\tilde{Q},\tilde{R}]\bigr)=\operatorname{adj}\bigl(M(Q)^{\dagger}\bigr)M(P)M(R)^{\dagger}-\operatorname{adj}M(P)\,M(R)\,\operatorname{adj}\bigl(M(Q)^{\dagger}\bigr),
$$

using $\mathsf{M}_2(\overline{\tilde{Q}})=\operatorname{adj}(M(Q)^{\dagger})$, $\mathsf{M}_2(\tilde{P}^{\natural})=\operatorname{adj}M(P)$ and $\mathsf{M}_2(\tilde{R}^{*})=M(R)^{\dagger}$; the associator vanishes exactly when the two products agree. It is the difference of two products of three matrices, each mixing the adjugate and the dagger and reading the factors in a different order, $Q,P,R$ against $P,R,Q$, so it is not the commutator of any single pair.

**Theorem (the multiplication operators).** For every $\tilde{A}$ and $\tilde{X}$,

$$
\mathsf{M}_2\bigl(L_{\tilde{A}}(\tilde{X})\bigr)=\operatorname{adj}M(A)\,M(X)^{\dagger},\qquad \mathsf{M}_2\bigl(R_{\tilde{A}}(\tilde{X})\bigr)=\operatorname{adj}M(X)\,M(A)^{\dagger},
$$

and the composition of two left multiplications is

$$
\mathsf{M}_2\bigl(L_{\tilde{A}}L_{\tilde{B}}(\tilde{X})\bigr)=\operatorname{adj}M(A)\,M(X)\,\bigl(\operatorname{adj}M(B)\bigr)^{\dagger},
$$

a matrix product with $M(X)$ in the middle, which is the matrix form of the two-sided multiplication and the reason the composition leaves the class of the multiplication operators: the left multiplication carries a dagger on $M(X)$ and the composition does not. Since $\bigl(\operatorname{adj}M(B)\bigr)^{\dagger}=M(\overline{\tilde{B}})$, this agrees with the value $\operatorname{adj}M(A)\,M(X)\,M(\overline{\tilde{B}})$ predicted by the composition law of the group.

## The General Quaternionic Sesquilinear Form in the Model

**Theorem (the adjugated conjugate-transpose pairing).** For all biquaternions,

$$
\langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde{P})^{\dagger}\mathsf{M}_2(\tilde{Q})\bigr),
$$

the pairing in which the conjugate transpose of the first argument is adjugated.

*Proof.* $\operatorname{adj}\mathsf{M}_2(\tilde{P})^{\dagger}=\mathsf{M}_2(\tilde{P}^{\natural})^{\dagger}=\mathsf{M}_2((\tilde{P}^{\natural})^{*})=\mathsf{M}_2(\bar{\tilde{P}})$, since $(\tilde{P}^{\natural})^{*}=\bar{\tilde{P}}$ is the coefficient conjugate; the right-hand side is then $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\bar{\tilde{P}})\mathsf{M}_2(\tilde{Q}))=\mathrm{Sc}(\bar{\tilde{P}}\tilde{Q})=\sum_\mu\varepsilon_\mu\overline{P_\mu}Q_\mu$.

**Theorem (the diagonal).** On the diagonal,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural*} = \sum_\mu\varepsilon_\mu|Q_\mu|^2 = |Q_0|^2-\sum_{k=1}^{3}|Q_k|^2 ,
$$

the Krein invariant of the element; it is positive on the centre, negative on the vector subspace, and the two subspaces are orthogonal for the form, which is the fundamental decomposition of the algebra.

**The signature and the null set.** The form has complex inertia $(1,3)$ and real signature $(2,6)$; the positive part is the centre, of real dimension $2$, and the negative part the vector subspace, of real dimension $6$. The null set is the real cone $\sum_\mu\varepsilon_\mu|Q_\mu|^2=0$, of real dimension $7$, which is not the complex null cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of the general plain bilinear form and is not the determinant null set of the general quaternionic bilinear form.

**The automorphism group.** The form is the general quaternionic sesquilinear form of signature $(1,3)$ on the four complex coordinates, so its automorphism group is the indefinite unitary group $U(1,3)$, of real dimension $16$; on the matrix side it is the group preserving the adjugated conjugate-transpose pairing, and its realification has automorphism group $O(2,6)$, of real dimension $28$. The adjugation is a form-preserving map, because it is the fundamental symmetry $J$.

## Worked Examples

**An isotropic element that is not a zero divisor.** Let $\tilde{Q}=e_0+ie_1$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=|1|^2-|i|^2=0$, so the element is isotropic for the Krein form, while $N(\tilde{Q})=1+i^2=0$ as well: the element is a zero divisor of the general quaternionic bilinear form. By contrast the element $\tilde{Q}=e_0+e_1$ has $N(\tilde{Q})=2$ and is still Krein-isotropic, so the two notions are independent.

**A positive and a negative element.** Let $\tilde{P}=2e_0+e_1$ and $\tilde{Q}=e_0+2e_1$. Then $\langle\tilde{P},\tilde{P}\rangle_{\natural*}=4-1=3>0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1-4=-3<0$, so the form is indefinite and the two types occur on the axis elements alone.

**A basis element.** Let $\tilde{P}=e_1$ and $\tilde{Q}=e_0$. Then $\tilde{P}\star\tilde{Q}=e_1^{\natural}e_0^{*}=-e_1$, and in the model $\operatorname{adj}\mathsf{M}_2(e_1)\mathsf{M}_2(e_0)^{\dagger}=-\mathsf{M}_2(e_1)$, as the product theorem requires; the diagonal of the form is $\langle e_1,e_1\rangle_{\natural*}=-1$.

## Summary

The $2\times2$ realization keeps the two conjugations apart, the natural conjugation as the adjugate and the Hermitian conjugation as the conjugate transpose, with the coefficientwise conjugation as the adjugate of the dagger; so the general quaternionic sesquilinear product is the adjugated conjugate-transposed matrix product, $\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\operatorname{adj}\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})^{\dagger}=\varepsilon \mathsf{M}_2(\tilde{P})^{\mathsf{T}}\varepsilon^{-1}\mathsf{M}_2(\tilde{Q})^{\dagger}$, the fourth of the four general products and the only sesquilinear one. Its idempotents satisfy $\operatorname{adj}(M)M^{\dagger}=M$; the nontrivial ones have norm one and satisfy $M^{3}=I$, $M^{\dagger}=M^{2}=M^{-1}$, $\operatorname{Tr}M=-1$, and they are exactly the unitary conjugates of $\operatorname{diag}(\omega,\omega^{2})$, the family of the group, disjoint from the zero divisors, which are the singular matrices. The associator is $\operatorname{adj}(M(Q)^{\dagger})M(P)M(R)^{\dagger}-\operatorname{adj}M(P)M(R)\operatorname{adj}(M(Q)^{\dagger})$, and the left and right multiplications are $\operatorname{adj}M(A)M(X)^{\dagger}$ and $\operatorname{adj}M(X)M(A)^{\dagger}$. The general quaternionic sesquilinear form of the group is the adjugated conjugate-transpose pairing $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde{P})^{\dagger}\mathsf{M}_2(\tilde{Q}))=\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$, whose diagonal is $\sum_\mu\varepsilon_\mu|Q_\mu|^2$, positive on the centre and negative on the vector subspace, of complex inertia $(1,3)$ and real signature $(2,6)$, with the real cone of real dimension $7$ as null set and the indefinite unitary group $U(1,3)$ as automorphism group, of realification $O(2,6)$. The natural conjugation is the fundamental symmetry, and in the model it is the adjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\operatorname{Tr}\mathsf{M}_2(\tilde{Q})=2Q_0$ |
| $\mathsf{M}_2(\tilde{Q}^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde{Q})$, $\mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger}$ | the natural conjugation is the adjugate, the Hermitian conjugation the conjugate transpose |
| $\mathsf{M}_2(\overline{\tilde{Q}})=\operatorname{adj}(\mathsf{M}_2(\tilde{Q})^{\dagger})=\varepsilon\overline{\mathsf{M}_2(\tilde{Q})}\varepsilon^{-1}$ | the coefficientwise conjugation is the adjugate of the dagger |
| $\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\operatorname{adj}\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})^{\dagger}$ | the general quaternionic sesquilinear product, the fourth of the four general products |
| $\operatorname{adj}(M)M^{\dagger}=M$ | the matrix idempotent equation |
| $U\operatorname{diag}(\omega,\omega^{2})U^{\dagger}$ | the family of idempotents as a unitary orbit |
| $\operatorname{adj}(M(Q)^{\dagger})M(P)M(R)^{\dagger}-\operatorname{adj}M(P)M(R)\operatorname{adj}(M(Q)^{\dagger})$ | the associator in matrices |
| $\operatorname{adj}M(A)M(X)^{\dagger}$, $\operatorname{adj}M(X)M(A)^{\dagger}$ | the left and the right multiplication |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde{P})^{\dagger}\mathsf{M}_2(\tilde{Q}))=\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$ | the general quaternionic sesquilinear form |
| $(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | the inertia and the real signature |
| $U(1,3)$, $O(2,6)$ | the automorphism group and its realification |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the adjugate, the determinant and the unitary group.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the structure of $M_2(\mathbb{C})$ and its involutions.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the classification of the involutions of a matrix algebra and the orthosymplectic forms.
- Barry Simon, *Representations of Finite and Compact Groups* (American Mathematical Society, 1996), for the conjugacy classes of $U(2)$ and the orbits of the unitary group.
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and its first properties
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the further reading of the isomorphism
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form on the algebra
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the fundamental symmetry $J={}^{\natural}$
- *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-4x4-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the restriction theory of the form
