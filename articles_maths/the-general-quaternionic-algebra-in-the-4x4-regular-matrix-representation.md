
# __The General Quaternionic Algebra in the $4\times4$ Matrix Representation__

## Introduction

The left regular representation $\rho_L$ of *Introduction to the $4\times4$ Regular Matrix Representation of Biquaternions* carries the algebra acting on itself, and it makes the natural conjugation ${}^{\natural}$ visible as the **transposition** of the regular matrix, $\rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}}$. This article is the companion of *The General Quaternionic Algebra in the $2\times2$ Matrix Representation*, and it reads the group *Topology on the Introduction to the General Quaternionic Algebra of Biquaternions* on the regular matrices: the quaternionic product becomes the product of the transposed regular matrix with the second factor, and the general quaternionic bilinear form becomes the trace pairing with the transposed second factor, with the factor $2$ that the dimension of the module brings.

The regular representation has one advantage over the $2\times2$ realization in this group: the characteristic operation ${}^{\natural}$ is a transposition, and the transposition is the operation that the regular matrix already carries. The general quaternionic bilinear form therefore needs no adjugate, and the determinant of the regular matrix is the square of the norm, the two factors being the two copies of the simple module.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$; the quaternionic product $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}$ with norm $N(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **left regular representation** is the algebra homomorphism

$$
\rho_L:\mathbb{B}\longrightarrow M_4(\mathbb{C}),\qquad \rho_L(\tilde{Q})(\tilde{R})=\tilde{Q}\tilde{R},
$$

with $\rho_L(\tilde{Q})$ the $4\times4$ matrix of left multiplication in the basis $e_0,e_1,e_2,e_3$; the right regular representation is $\rho_R(\tilde{Q})(\tilde{R})=\tilde{R}\tilde{Q}$. The representation satisfies

$$
\rho_L(\tilde{P})\rho_L(\tilde{Q})=\rho_L(\tilde{P}\tilde{Q}),\qquad \rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}},\qquad \rho_R(\tilde{Q})=E\,\rho_L(\tilde{Q})^{\mathsf{T}}E ,
$$

and its two invariants are

$$
\operatorname{Tr}\rho_L(\tilde{Q})=4Q_0,\qquad \det\rho_L(\tilde{Q})=N(\tilde{Q})^2 .
$$

## The Quaternionic Product in the Regular Representation

**Theorem (the product is the transposed product of the regular matrices).** For all biquaternions,

$$
\rho_L(\tilde{P}\star\tilde{Q})=\rho_L(\tilde{P})^{\mathsf{T}}\,\rho_L(\tilde{Q}) ,
$$

so the quaternionic product is read on the regular matrices by transposing the first factor and multiplying.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}$, the representation is multiplicative and $\rho_L(\tilde{P}^{\natural})=\rho_L(\tilde{P})^{\mathsf{T}}$.

**The square and the determinant.** The theorem at $\tilde{P}=\tilde{Q}$ gives $\rho_L(\tilde{Q}\star\tilde{Q})=\rho_L(\tilde{Q})^{\mathsf{T}}\rho_L(\tilde{Q})$; since $\tilde{Q}\star\tilde{Q}=N(\tilde{Q})e_0$, the transposed product is the scalar matrix $N(\tilde{Q})I_4$, and taking determinants returns $\det\rho_L(\tilde{Q})^2=N(\tilde{Q})^4$, equivalent to the invariant $\det\rho_L(\tilde{Q})=N(\tilde{Q})^2$.

**The two-sided structure.** The right multiplications $\rho_R(\mathbb{B})$ commute with the left ones by associativity, and $\rho_R(\tilde{Q})$ is the conjugate of the transpose of $\rho_L(\tilde{Q})$ by the sign matrix $E$, so the natural conjugation on the left copy and the right copy are the two transpositions of the regular matrix, related by the sign matrix.

## The General Quaternionic Bilinear Form in the Regular Representation

**Theorem (the trace pairing of the transposed regular matrix).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\rho_L(\tilde{P})\,\rho_L(\tilde{Q})^{\mathsf{T}}\bigr) = 2\,\langle\tilde{P},\tilde{Q}\rangle_{\natural} ,
$$

so the trace pairing of the regular matrices with the second factor transposed is twice the general quaternionic bilinear form of the algebra.

*Proof.* $\rho_L(\tilde{Q})^{\mathsf{T}}=\rho_L(\tilde{Q}^{\natural})$, so the left-hand side is $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P}\tilde{Q}^{\natural}))=2\,\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$, using $\operatorname{Tr}\rho_L(\tilde{R})=4\,\mathrm{Sc}(\tilde{R})$.

**Theorem (the diagonal is the norm).** On the diagonal,

$$
\tfrac12\operatorname{Tr}\bigl(\rho_L(\tilde{Q})\,\rho_L(\tilde{Q})^{\mathsf{T}}\bigr) = 2\,N(\tilde{Q}) = 2\det\Phi(\tilde{Q}) ,
$$

so the diagonal of the pairing is twice the determinant of the element, the determinant of the regular matrix being its square.

**The Gram matrix and the signature.** In the coefficient basis the Gram matrix of the pairing is the identity $I_4$; over $\mathbb{R}$ the form is the split form of signature $(4,4)$ on the eight real coordinates, indefinite and non-degenerate.

**The null set.** The form vanishes exactly when $N(\tilde{Q})=0$, that is when $\det\rho_L(\tilde{Q})=0$: the null set is the set of singular regular matrices, the zero divisors of the algebra, of rank two and of real dimension $6$ in $\mathbb{R}^8$. It is distinct from the isotropic cone of the general plain bilinear form and strictly smaller than the real isotropic cone of the realified form.

**The automorphisms.** The form has Gram matrix $I_4$, so its automorphism group is the complex orthogonal group $O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, and its realification is the split orthogonal group $O(4,4)$ of signature $(4,4)$. The transposition is the elementary operator of the group, and the conjugations $\rho_L(\tilde{Q})\mapsto\rho_L(\tilde{A})\rho_L(\tilde{Q})\rho_L(\tilde{A})^{-1}$ by the units are its inner part. The congruence with the general plain bilinear form is the one read on the matrices of *The General Plain Algebra in the $4\times4$ Matrix Representation*.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $\rho_L(e_0)=I_4$ and $\tfrac12\operatorname{Tr}(I_4\cdot I_4^{\mathsf{T}})=2=2N(e_0)$, while $\det\rho_L(e_0)=1=N(e_0)^2$.

**A basis element.** Let $\tilde{Q}=e_1$. Then $\rho_L(e_1)^{\mathsf{T}}=\rho_L(e_1^{\natural})=-\rho_L(e_1)$, so $\rho_L(e_1)^{\mathsf{T}}\rho_L(e_1)=-\rho_L(e_1)^2=-\rho_L(e_1^2)=\rho_L(e_0)=I_4$, which is the product theorem at $\tilde{P}=\tilde{Q}=e_1$ and matches $e_1\star e_1=e_1^{\natural}e_1=-e_1^2=e_0$ with $N(e_1)=1$.

**A zero divisor.** Let $\tilde{Q}=e_0+ie_1$. Then $N(\tilde{Q})=0$, so $\det\rho_L(\tilde{Q})=0$ and the regular matrix is singular of rank two; the diagonal of the pairing is $\tfrac12\operatorname{Tr}(\rho_L(\tilde{Q})\rho_L(\tilde{Q})^{\mathsf{T}})=2N(\tilde{Q})=0$, so the element is isotropic for the general quaternionic bilinear form, unlike its behaviour for the general plain bilinear form.

## Summary

The left regular representation reads the natural conjugation as the transposition, $\rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}}$, and the quaternionic product as the transposed product $\rho_L(\tilde{P}\star\tilde{Q})=\rho_L(\tilde{P})^{\mathsf{T}}\rho_L(\tilde{Q})$, with square the scalar matrix $N(\tilde{Q})I_4$. The general quaternionic bilinear form of the group is the trace pairing with the transposed second factor, $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q})^{\mathsf{T}})=2\langle\tilde{P},\tilde{Q}\rangle_{\natural}$, whose diagonal is twice the determinant of the element, whose coefficient Gram matrix is the identity $I_4$, of real signature $(4,4)$, whose null set is the set of singular regular matrices of rank two, of real dimension $6$, and whose automorphism group is $O_4(\mathbb{C})$ on the coefficients and the split group $O(4,4)$ on the realification. The invariants of the regular matrix are the trace $4Q_0$ and the determinant $N(\tilde{Q})^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_L(\tilde{Q})$ | the $4\times4$ regular matrix, $\operatorname{Tr}\rho_L(\tilde{Q})=4Q_0$, $\det\rho_L(\tilde{Q})=N(\tilde{Q})^2$ |
| $\rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}}$ | the natural conjugation is the transposition |
| $\rho_L(\tilde{P}\star\tilde{Q})=\rho_L(\tilde{P})^{\mathsf{T}}\rho_L(\tilde{Q})$ | the quaternionic product on the regular matrices |
| $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q})^{\mathsf{T}})=2\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form |
| $I_4$, split of signature $(4,4)$ | the coefficient Gram matrix and the real signature |
| $N(\tilde{Q})=0$ | the null set, the singular regular matrices of rank two |

## Further Reading

- *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-representation-of-biquaternions.md`), for the representation and its first properties
- *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/biquaternion-4x4-matrix-element-representation.md`), for the further reading of the regular representation
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the quaternionic product on the algebra
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form on the algebra
- *The General Quaternionic Algebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-quaternionic-algebra-in-the-2x2-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the restriction theory of the form
