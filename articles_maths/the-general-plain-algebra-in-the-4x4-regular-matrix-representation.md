
# __The General Plain Algebra in the $4\times4$ Regular Matrix Representation__

## Introduction

The left regular representation $\rho_L$ of *Introduction to the $4\times4$ Regular Matrix Representation of Biquaternions* realises the algebra on the coefficient space $\mathbb{C}^4$ by left multiplication, so that the regular matrix $\rho_L(\tilde{Q})$ is the carrier of the element acting on the algebra itself. This article is the companion of *The General Plain Algebra in the $2\times2$ Matrix Representation*, and it reads the same reading group *Topology on the Introduction to the General Plain Algebra of Biquaternions* on the regular matrices instead of on the $2\times2$ matrices: the plain product becomes the product of the regular matrices, and the general plain bilinear form $\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q})$ becomes the plain trace pairing of the regular matrices, with the factor $2$ that the dimension of the module brings.

The regular representation is the more faithful of the two carrier spaces, because it sees the algebra act and not only the algebra: it carries the left and right multiplications as two commuting copies, the natural conjugation as the transposition, and the two blocks of the fundamental decomposition as invariant subspaces. The trace pairing of the regular matrices is twice the general plain bilinear form, and the determinant of the regular matrix is the square of the determinant of the element, the two factors being the two copies of the simple module in $\mathbb{B}$.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **left regular representation** is the algebra homomorphism

$$
\rho_L:\mathbb{B}\longrightarrow M_4(\mathbb{C}),\qquad \rho_L(\tilde{Q})(\tilde{R})=\tilde{Q}\tilde{R},
$$

with $\rho_L(\tilde{Q})$ the $4\times4$ matrix of left multiplication in the basis $e_0,e_1,e_2,e_3$; the **right regular representation** is $\rho_R(\tilde{Q})(\tilde{R})=\tilde{R}\tilde{Q}$. The two representation matrices satisfy

$$
\rho_L(\tilde{P})\rho_L(\tilde{Q})=\rho_L(\tilde{P}\tilde{Q}),\qquad \rho_R(\tilde{Q})=E\,\rho_L(\tilde{Q})^{\mathsf{T}}E,\qquad \rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}},
$$

and the two invariants of the regular matrix are

$$
\operatorname{Tr}\rho_L(\tilde{Q})=4Q_0,\qquad \det\rho_L(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2 .
$$

## The Plain Product in the Representation

**Theorem (the product is the product of the regular matrices).** For all biquaternions,

$$
\rho_L(\tilde{P})\rho_L(\tilde{Q})=\rho_L(\tilde{P}\tilde{Q}),
$$

so the plain product of the algebra is the product of the regular matrices, and the composition of the two one-sided operators is the operator of the product, $\rho_L(\tilde{P})\circ\rho_L(\tilde{Q})=\rho_L(\tilde{P}\tilde{Q})$.

*Proof.* The representation is defined by $\rho_L(\tilde{Q})(\tilde{R})=\tilde{Q}\tilde{R}$ and the associativity of the algebra: $\rho_L(\tilde{P})\rho_L(\tilde{Q})(\tilde{R})=\tilde{P}(\tilde{Q}\tilde{R})=(\tilde{P}\tilde{Q})\tilde{R}$.

**The two-sided structure.** The right multiplications act on the same space and commute with the left ones, so the regular module carries the two commuting copies $\rho_L(\mathbb{B})$ and $\rho_R(\mathbb{B})$; the double centralizer theorem identifies each with the full commutant of the other, and the algebra decomposes as the direct sum $I_1\oplus I_2$ of two minimal left ideals. The elements of $\rho_R(\mathbb{B})$ are exactly the conjugates of the transposes of $\rho_L(\mathbb{B})$ by the sign matrix, by the second identity above.

## The General Plain Bilinear Form in the Representation

**Theorem (the trace pairing of the regular matrices).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\rho_L(\tilde{P})\rho_L(\tilde{Q})\bigr) = 2\,\langle\tilde{P},\tilde{Q}\rangle ,
$$

so the plain trace pairing of the regular matrices is twice the general plain bilinear form of the algebra.

*Proof.* The representation is a homomorphism, so $\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q}))=\operatorname{Tr}\rho_L(\tilde{P}\tilde{Q})=4\,\mathrm{Sc}(\tilde{P}\tilde{Q})$, and the factor $2$ follows.

**Theorem (the diagonal).** On the diagonal,

$$
\tfrac12\operatorname{Tr}\bigl(\rho_L(\tilde{Q})^2\bigr) = 2\sum_\mu\varepsilon_\mu Q_\mu^2 ,
$$

the general plain bilinear invariant of the regular matrix.

**The Gram matrix, the congruence and the signature.** In the coefficient basis the Gram matrix of the pairing is the sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$, and a change of basis with matrix $S$ replaces it by $S^{\mathsf T}ES$; over $\mathbb{C}$ the form is determined up to congruence by its rank alone. Over $\mathbb{R}$ the form has signature $(4,4)$ on the eight real coordinates of the coefficient space, and it is indefinite.

**The null set.** The pairing vanishes on the cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of real dimension $6$, the same cone as in the $2\times2$ representation; the two representations carry the same null set, because the form is transported by the two realizations of the same element.

**The automorphisms.** A matrix preserves the trace pairing exactly when $T^{\mathsf T}ET=E$, so the automorphism group on the coefficient space is $\{T\in GL_4(\mathbb{C}):T^{\mathsf T}ET=E\}=O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, its Lie algebra $\{X:X^{\mathsf T}E+EX=0\}$ being of real dimension $12$; its real forms $O(4)$ and $O(1,3)$ are cut out by the Hermitian and the complex conjugation on the Hermitian and the quaternion subspace. The group of real-linear automorphisms of the realified form is the larger $O(4,4)$, not the group the form defines over $\mathbb{C}$. Two operators act on the regular matrix from the algebra: the transposition $\rho_L(\tilde{Q})\mapsto\rho_L(\tilde{Q}^{\natural})$ carries the natural conjugation, and the conjugation $\rho_L(\tilde{Q})\mapsto\rho_L(\tilde{A})\rho_L(\tilde{Q})\rho_L(\tilde{A})^{-1}$ carries the inner automorphism of a unit; both are automorphisms of the pairing.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $\rho_L(e_0)=I_4$, $\operatorname{Tr}\rho_L(e_0)=4$ and $\det\rho_L(e_0)=1$, while $\langle e_0,e_0\rangle=1$ and $\tfrac12\operatorname{Tr}(I_4^2)=2=2\langle e_0,e_0\rangle$.

**A basis element.** Let $\tilde{Q}=e_1$. Then $\rho_L(e_1)$ is the matrix of left multiplication by $e_1$, a signed permutation matrix of trace $0$ and determinant $1$; since $\langle e_1,e_1\rangle=-1$, the diagonal identity reads $\tfrac12\operatorname{Tr}(\rho_L(e_1)^2)=-2=2\langle e_1,e_1\rangle$.

**A zero divisor.** Let $\tilde{Q}=e_0+ie_1$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$, so $\det\rho_L(\tilde{Q})=0$ and the regular matrix is singular of rank two; the diagonal of the plain pairing is $\tfrac12\operatorname{Tr}(\rho_L(\tilde{Q})^2)=2\langle\tilde{Q},\tilde{Q}\rangle=4$, so the singular matrix is not isotropic for the general plain bilinear form.

## Summary

The left regular representation turns the plain product of the algebra into the product of the regular matrices, $\rho_L(\tilde{P})\rho_L(\tilde{Q})=\rho_L(\tilde{P}\tilde{Q})$, and carries the two commuting copies $\rho_L(\mathbb{B})$ and $\rho_R(\mathbb{B})$ of the algebra, related by the transposition identities $\rho_R(\tilde{Q})=E\rho_L(\tilde{Q})^{\mathsf{T}}E$ and $\rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}}$. The general plain bilinear form of the group is the plain trace pairing $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$, with the coefficient Gram matrix $E$, of real signature $(4,4)$, with the isotropic cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of real dimension $6$ as null set, and with automorphism group $O_4(\mathbb{C})$ on the coefficients and $O(4,4)$ on the realification. The invariants of the regular matrix are the trace $4Q_0$ and the determinant $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$, the square of the determinant of the element because the regular module is the direct sum of two copies of the simple module.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_L(\tilde{Q})$ | the $4\times4$ regular matrix of left multiplication, $\operatorname{Tr}\rho_L(\tilde{Q})=4Q_0$ |
| $\rho_R(\tilde{Q})=E\rho_L(\tilde{Q})^{\mathsf{T}}E$ | the right regular matrix, the transpose of the left one conjugated by the sign matrix $E$ |
| $\rho_L(\tilde{P})\rho_L(\tilde{Q})=\rho_L(\tilde{P}\tilde{Q})$ | the plain product is the product of the regular matrices |
| $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form as the trace pairing of the regular matrices |
| $\det\rho_L(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$ | the determinant of the regular matrix |
| $O_4(\mathbb{C})$, $O(4,4)$ | the automorphism group and its realification |

## Further Reading

- *Introduction to the $4\times4$ Regular Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-4x4-regular-matrix-representation-of-biquaternions.md`), for the representation and its first properties
- *Biquaternion 4×4 Regular Matrix Element Representation* (`articles_maths/biquaternion-4x4-regular-matrix-element-representation.md`), for the further reading of the regular representation
- *The General Plain Algebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the restriction theory of the form
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms read side by side
