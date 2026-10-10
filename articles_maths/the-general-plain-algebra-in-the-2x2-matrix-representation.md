
# __The General Plain Algebra in the $2\times2$ Matrix Representation__

## Introduction

The reading group *Topology on the Introduction to the General Plain Algebra of Biquaternions* reads the algebra through one pairing, the general plain bilinear form $\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q})=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$, through the plain product it polarises, and through the two-sided operators that product defines. This article reads that same group through the $2\times2$ matrix realization $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and it is the first of the two representation articles of the group: the companion *The General Plain Algebra in the $4\times4$ Matrix Representation* repeats the reading on the left regular representation.

The plain product becomes the matrix product under $\mathsf{M}_2$, and the general plain bilinear form becomes the plain trace pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q}))$. The two facts are the whole content of the group law on the matrices: the product transports because $\mathsf{M}_2$ is an algebra isomorphism, and the trace carries the scalar part because $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{R})\mathsf{M}_2(\tilde{S}))$.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; a generic element is $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the scalar part is $\mathrm{Sc}$, the sign vector is $\varepsilon=(1,-1,-1,-1)$, the natural conjugation ${}^{\natural}$ negates $e_1,e_2,e_3$, and the Hermitian conjugation is ${}^{*}={}^{\natural}\circ\bar{\cdot}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **matrix realization** is the isomorphism written $\mathsf{M}_2$. It converts a biquaternion into a $2 \times 2$ complex matrix,

$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: $\mathsf{M}_2(e_0)=I$ on the identity and $\mathsf{M}_2(e_k)=-i\sigma_k$ on the three vector units. The matrices $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices, and on a general element

$$
\mathsf{M}_2(\tilde{Q}) = \begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3 \end{pmatrix} .
$$

The realization is an isomorphism of algebras, and the three basic invariants are the trace, the determinant and the two conjugations,

$$
\operatorname{Tr}\mathsf{M}_2(\tilde{Q})=2Q_0,\qquad \det \mathsf{M}_2(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2,\qquad \mathsf{M}_2(\tilde{Q}^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde{Q}),\qquad \mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger} .
$$

## The Plain Product in the Representation

**Theorem (the product is the matrix product).** For all biquaternions,

$$
\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})=\mathsf{M}_2(\tilde{P}\tilde{Q}),
$$

so the plain product of the algebra is the product of the matrices.

*Proof.* $\mathsf{M}_2$ is the algebra isomorphism $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ defined on the generators by $\mathsf{M}_2(e_k)=-i\sigma_k$, and the Pauli matrices realise the quaternion relations $\sigma_k\sigma_l=\delta_{kl}I+i\sum_m\epsilon_{klm}\sigma_m$.

**The dictionary of the product.** The theorem transports every product-theoretic notion of the group into the matrix algebra:

- the centre of $\mathbb{B}$ is the scalar matrices $\mathbb{C} I$, so a biquaternion is central exactly when its matrix is a scalar;
- the group of units $\mathbb{B}^\times$ is $GL_2(\mathbb{C})$, and the unit group is the complement of the singular matrices;
- the zero divisors are the singular matrices, equivalently the rank-one matrices $\mathsf{M}_2(\tilde{Q})=uv^{\mathsf{T}}$;
- the two-sided operator $X\mapsto \tilde{Q}X\tilde{Q}^{-1}$ is the conjugation $M\mapsto \mathsf{M}_2(\tilde{Q})M\mathsf{M}_2(\tilde{Q})^{-1}$ of the matrix algebra.

## The General Plain Bilinear Form in the Representation

**Theorem (the trace pairing).** For all biquaternions,

$$
\langle\tilde{P},\tilde{Q}\rangle = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})\bigr),
$$

and the matrix trace is the carrier of the scalar part, $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{R})\mathsf{M}_2(\tilde{S}))$.

*Proof.* The trace identity gives the right-hand side at once; it holds on the basis, where $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\operatorname{Tr}(\mathsf{M}_2(e_\mu)\mathsf{M}_2(e_\nu))=2\varepsilon_\mu\delta_{\mu\nu}$.

**Theorem (the diagonal).** On the diagonal the pairing is the general plain bilinear form of the element,

$$
\langle\tilde{Q},\tilde{Q}\rangle = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde{Q})^2\bigr) = \sum_\mu\varepsilon_\mu Q_\mu^2 .
$$

**The Gram matrix, the congruence and the signature.** In the coefficient basis the Gram matrix of the pairing is the sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$, and a change of basis with matrix $S$ replaces it by $S^{\mathsf T}ES$; over $\mathbb{C}$ the form is therefore determined up to congruence by its rank alone, every non-degenerate complex quadratic form of rank $4$ being equivalent to this one. The plain product is what puts the sign matrix $E$, and not $\mathrm{I}_4$, in the coefficient basis. Over $\mathbb{R}$ the form has signature $(4,4)$ on the eight real coordinates, and it is indefinite.

**The null set.** The pairing vanishes on the isotropic cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$, a complex cone of real dimension $6$ in $\mathbb{R}^8$, with two families of isotropic planes; it is the null set of neither the determinant nor the general quaternionic bilinear form. The quadric, its isotropic planes, the hyperbolic splitting and the index are *The Four Pairings of the Biquaternion Algebra*.

**The automorphisms.** A matrix preserves the trace pairing exactly when $T^{\mathsf T}ET=E$, so on the coefficients the automorphism group is $\{T\in GL_4(\mathbb{C}):T^{\mathsf T}ET=E\}=O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, its Lie algebra $\{X:X^{\mathsf T}E+EX=0\}$ being of real dimension $12$. The real structures exhibit the real forms: the Hermitian conjugation is an antilinear form reversal with fixed space the Hermitian subspace of restriction signature $(4,0)$, so the automorphisms commuting with it form the real orthogonal group $O(4)$; the complex conjugation has fixed space the quaternion subspace of signature $(1,3)$, exhibited by $O(1,3)$. The group of real-linear automorphisms of the realified form is the larger $O(4,4)$, which is not the group the form defines over $\mathbb{C}$. On the matrices the conjugation $M\mapsto UMU^{-1}$ by a unit and the transposition $M\mapsto M^{\mathsf{T}}$ are automorphisms, since $\operatorname{Tr}(UMU^{-1}\cdot UNU^{-1})=\operatorname{Tr}(MN)$ and $\operatorname{Tr}(M^{\mathsf{T}}N^{\mathsf{T}})=\operatorname{Tr}(MN)$; the inner automorphisms and the transposition together form a proper subgroup of the full group $O_4(\mathbb{C})$.

## Worked Examples

**A zero divisor that is not isotropic.** Let $\tilde{Q}=e_0+ie_1$. Then $N(\tilde{Q})=1+i^2=0$, so $\tilde{Q}$ is a zero divisor, and $\mathsf{M}_2(\tilde{Q})=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is singular of rank one; but $\langle\tilde{Q},\tilde{Q}\rangle=Q_0^2-Q_1^2=1-i^2=2$, so $\tilde{Q}$ is not isotropic for the general plain bilinear form.

**An isotropic pair.** Let $\tilde{P}=e_0+ie_1$ and $\tilde{Q}=e_0-ie_1$. Then $\langle\tilde{P},\tilde{Q}\rangle=1+(-1)(i)(-i)=1-1=0$, so the two are isotropic to each other while both matrices are singular.

**A central element.** Let $\tilde{Q}=\lambda e_0$. Then $\mathsf{M}_2(\tilde{Q})=\lambda I$ and $\langle\tilde{Q},\tilde{Q}\rangle=\lambda^2$, while $\det \mathsf{M}_2(\tilde{Q})=\lambda^2$; the two invariants agree on the centre and separate off it.

## Summary

The matrix realization $\mathsf{M}_2$ turns the plain product of the algebra into the matrix product, by the isomorphism theorem $\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})=\mathsf{M}_2(\tilde{P}\tilde{Q})$, and the scalar part into the half trace, $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{R})\mathsf{M}_2(\tilde{S}))$. The general plain bilinear form of the group is therefore the plain trace pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q}))$, whose diagonal is the general plain bilinear form $\sum_\mu\varepsilon_\mu Q_\mu^2$ of the element, whose coefficient Gram matrix is the sign matrix $E$, of real signature $(4,4)$, whose null set is the isotropic cone of real dimension $6$, and whose automorphism group is $O_4(\mathbb{C})$ on the coefficients and $O(4,4)$ on the realification. The units are $GL_2(\mathbb{C})$, the zero divisors are the singular matrices, and the trace and determinant are the two invariants $2Q_0$ and $\sum_\mu Q_\mu^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\mathsf{M}_2(e_0)=I$, $\mathsf{M}_2(e_k)=-i\sigma_k$ |
| $\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})=\mathsf{M}_2(\tilde{P}\tilde{Q})$ | the plain product is the matrix product |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q}))=\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form as the plain trace pairing |
| $E=\operatorname{diag}(1,-1,-1,-1)$ | the coefficient Gram matrix, real signature $(4,4)$ |
| $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ | the isotropic cone, of real dimension $6$ |
| $O_4(\mathbb{C})$, $O(4,4)$ | the automorphism group and its realification |

## Further Reading

- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and its first properties
- *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/biquaternion-2x2-matrix-element-representation-m2c.md`), for the further reading of the isomorphism
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the general plain bilinear form and its comparison with the other three
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the operators of this group
- *The General Plain Algebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-plain-algebra-in-the-4x4-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the restriction theory of the form
