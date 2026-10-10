
# __The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The left regular representation $\mathsf{M}_4$ of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* carries the algebra acting on itself, and it makes the natural conjugation ${}^{\natural}$ visible as the **transposition** of the regular matrix, $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$. This article is the companion of *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, and it reads the group *Topology on the Introduction to the General Quaternionic Algebra of Biquaternions* on the regular matrices: the quaternionic product becomes the product of the transposed regular matrix with the second factor, and the general quaternionic bilinear form becomes the trace pairing with the transposed second factor, with the factor $2$ that the dimension of the module brings.

The regular representation has one advantage over the $2\times2$ realization in this group: the characteristic operation ${}^{\natural}$ is a transposition, and the transposition is the operation that the regular matrix already carries. The general quaternionic bilinear form therefore needs no adjugate, and the determinant of the regular matrix is the square of the norm, the two factors being the two copies of the simple module.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$; the quaternionic product $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}$ with norm $N(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **left regular matrix** is the isomorphism written $\mathsf{M}_4$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: in the basis $e_0,e_1,e_2,e_3$ its $m$-th column is the coordinate column of the product $\tilde{Q}e_m$. The **right regular matrix** $\mathsf{M}_4^{R}(\tilde{Q})$ is defined the same way with the product in the opposite order, its $m$-th column being the coordinate column of $e_m\tilde{Q}$. The representation satisfies

$$
\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})=\mathsf{M}_4(\tilde{P}\tilde{Q}),\qquad \mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}},\qquad \mathsf{M}_4^{R}(\tilde{Q})=E\,\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}E ,
$$

and its two invariants are

$$
\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0,\qquad \det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2 .
$$

## The Quaternionic Product in the Regular Representation

**Theorem (the product is the transposed product of the regular matrices).** For all biquaternions,

$$
\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})^{\mathsf{T}}\,\mathsf{M}_4(\tilde{Q}) ,
$$

so the quaternionic product is read on the regular matrices by transposing the first factor and multiplying.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}$, the representation is multiplicative and $\mathsf{M}_4(\tilde{P}^{\natural})=\mathsf{M}_4(\tilde{P})^{\mathsf{T}}$.

**The square and the determinant.** The theorem at $\tilde{P}=\tilde{Q}$ gives $\mathsf{M}_4(\tilde{Q}\star\tilde{Q})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}\mathsf{M}_4(\tilde{Q})$; since $\tilde{Q}\star\tilde{Q}=N(\tilde{Q})e_0$, the transposed product is the scalar matrix $N(\tilde{Q})I_4$, and taking determinants returns $\det\mathsf{M}_4(\tilde{Q})^2=N(\tilde{Q})^4$, equivalent to the invariant $\det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2$.

**The two-sided structure.** The right multiplications $\mathsf{M}_4^{R}(\mathbb{B})$ commute with the left ones by associativity, and $\mathsf{M}_4^{R}(\tilde{Q})$ is the conjugate of the transpose of $\mathsf{M}_4(\tilde{Q})$ by the sign matrix $E$, so the natural conjugation on the left copy and the right copy are the two transpositions of the regular matrix, related by the sign matrix.

## The General Quaternionic Bilinear Form in the Regular Representation

**Theorem (the trace pairing of the transposed regular matrix).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{P})\,\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}\bigr) = 2\,\langle\tilde{P},\tilde{Q}\rangle_{\natural} ,
$$

so the trace pairing of the regular matrices with the second factor transposed is twice the general quaternionic bilinear form of the algebra.

*Proof.* $\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}=\mathsf{M}_4(\tilde{Q}^{\natural})$, so the left-hand side is $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P}\tilde{Q}^{\natural}))=2\,\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$, using $\operatorname{Tr}\mathsf{M}_4(\tilde{R})=4\,\mathrm{Sc}(\tilde{R})$.

**Theorem (the diagonal is the norm).** On the diagonal,

$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{Q})\,\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}\bigr) = 2\,N(\tilde{Q}) = 2\det\Phi(\tilde{Q}) ,
$$

so the diagonal of the pairing is twice the determinant of the element, the determinant of the regular matrix being its square.

**The Gram matrix and the signature.** In the coefficient basis the Gram matrix of the pairing is the identity $I_4$; over $\mathbb{R}$ the form is the split form of signature $(4,4)$ on the eight real coordinates, indefinite and non-degenerate.

**The null set.** The form vanishes exactly when $N(\tilde{Q})=0$, that is when $\det\mathsf{M}_4(\tilde{Q})=0$: the null set is the set of singular regular matrices, the zero divisors of the algebra, of rank two and of real dimension $6$ in $\mathbb{R}^8$. It is distinct from the isotropic cone of the general plain bilinear form and strictly smaller than the real isotropic cone of the realified form.

**The automorphisms.** The form has Gram matrix $I_4$, so its automorphism group is the complex orthogonal group $O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, and its realification is the split orthogonal group $O(4,4)$ of signature $(4,4)$. The transposition is the elementary operator of the group, and the conjugations $\mathsf{M}_4(\tilde{Q})\mapsto\mathsf{M}_4(\tilde{A})\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{A})^{-1}$ by the units are its inner part. The congruence with the general plain bilinear form is the one read on the matrices of *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $\mathsf{M}_4(e_0)=I_4$ and $\tfrac12\operatorname{Tr}(I_4\cdot I_4^{\mathsf{T}})=2=2N(e_0)$, while $\det\mathsf{M}_4(e_0)=1=N(e_0)^2$.

**A basis element.** Let $\tilde{Q}=e_1$. Then $\mathsf{M}_4(e_1)^{\mathsf{T}}=\mathsf{M}_4(e_1^{\natural})=-\mathsf{M}_4(e_1)$, so $\mathsf{M}_4(e_1)^{\mathsf{T}}\mathsf{M}_4(e_1)=-\mathsf{M}_4(e_1)^2=-\mathsf{M}_4(e_1^2)=\mathsf{M}_4(e_0)=I_4$, which is the product theorem at $\tilde{P}=\tilde{Q}=e_1$ and matches $e_1\star e_1=e_1^{\natural}e_1=-e_1^2=e_0$ with $N(e_1)=1$.

**A zero divisor.** Let $\tilde{Q}=e_0+ie_1$. Then $N(\tilde{Q})=0$, so $\det\mathsf{M}_4(\tilde{Q})=0$ and the regular matrix is singular of rank two; the diagonal of the pairing is $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{Q})^{\mathsf{T}})=2N(\tilde{Q})=0$, so the element is isotropic for the general quaternionic bilinear form, unlike its behaviour for the general plain bilinear form.

## The Matrices

**The generators.** The regular model is fixed on the basis by four matrices:

$$
\mathsf{M}_4(e_0)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

A general element is the block matrix

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A&B\\-B&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_0&-Q_1\\Q_1&Q_0\end{pmatrix},\qquad
B=\begin{pmatrix}-Q_2&-Q_3\\-Q_3&Q_2\end{pmatrix},
$$

The general element has trace $4Q_0$ and determinant $N(\tilde Q)^2$.

**The involution, entry by entry.** The transposition is the involution read on the coefficients, $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf{T}}$, and it is the trace-complement of the regular matrix,

$$
X^{\mathsf T}=\tfrac12(\operatorname{Tr}X)I_4-X,
$$

as $\operatorname{adj}X=(\operatorname{Tr}X)I-X$ is in the realization; the coefficient $\tfrac12$ is the one that carries the trace $2Q_0$ of the element to the trace $4Q_0$ of the regular matrix. At the unit $e_1$ the regular matrix and its transpose are opposite, $\mathsf{M}_4(e_1)^{\mathsf{T}}=-\mathsf{M}_4(e_1)=\mathsf{M}_4(e_1^{\natural})$.

**The product, entry by entry.** The product is the transposed product of the regular matrices, and at the pair $e_1,e_2$ it is

$$
\mathsf{M}_4(e_1\star e_2)=\mathsf{M}_4(e_1)^{\mathsf{T}}\mathsf{M}_4(e_2)=-\mathsf{M}_4(e_1)\mathsf{M}_4(e_2)=-\mathsf{M}_4(e_3),
$$

which is $e_1\star e_2=-e_3$. The square is the scalar matrix of the norm,

$$
\mathsf{M}_4(e_1)^{\mathsf{T}}\mathsf{M}_4(e_1)=(-\mathsf{M}_4(e_1))\mathsf{M}_4(e_1)=-\mathsf{M}_4(e_1)^2=I_4=N(e_1)I_4,
$$

thus $\mathsf{M}_4(e_1\star e_1)=N(e_1)I_4$, the identity $\mathsf{M}_4(e_1)^2=-I_4$ of the regular model doing the work.

**The four words.** The twelve operations of the two chapters are built from four products, and each product is a word in the two matrices $X=\mathsf{M}_4(\tilde P)$ and $Y=\mathsf{M}_4(\tilde Q)$ and in the two involutions of the model, the transposition and the conjugate transpose:

| product | first slot | second slot | the word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $X^{\mathsf T}$ | $Y$ | $X^{\mathsf T}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $X^{\mathsf T}$ | $Y^{\dagger}$ | $X^{\mathsf T}Y^{\dagger}$ |

The symmetric part of a product is the half-sum of its word and of the word with the two slots exchanged, and the antisymmetric part is the half-difference.

**The four traces.** The four products are four matrix traces, and the four forms of the algebra are read from them:

$$
\tfrac14\operatorname{Tr}(XY)=\langle\tilde P,\tilde Q\rangle,\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y)=B(\tilde P,\tilde Q),\qquad
\tfrac14\operatorname{Tr}(XY^{\dagger})=H(\tilde P,\tilde Q),\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y^{\dagger})=K(\tilde P,\tilde Q),
$$

the plain, the quaternionic, the Hermitian and the Krein form; the factor is $\tfrac14$ where the two-by-two model has $\tfrac12$, because the regular trace is four times the scalar part where the two-by-two trace is twice it.

## Summary

The left regular representation reads the natural conjugation as the transposition, $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$, and the quaternionic product as the transposed product $\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})^{\mathsf{T}}\mathsf{M}_4(\tilde{Q})$, with square the scalar matrix $N(\tilde{Q})I_4$. The general quaternionic bilinear form of the group is the trace pairing with the transposed second factor, $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})^{\mathsf{T}})=2\langle\tilde{P},\tilde{Q}\rangle_{\natural}$, whose diagonal is twice the determinant of the element, whose coefficient Gram matrix is the identity $I_4$, of real signature $(4,4)$, whose null set is the set of singular regular matrices of rank two, of real dimension $6$, and whose automorphism group is $O_4(\mathbb{C})$ on the coefficients and the split group $O(4,4)$ on the realification. The invariants of the regular matrix are the trace $4Q_0$ and the determinant $N(\tilde{Q})^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde{Q})$ | the $4\times4$ regular matrix, $\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0$, $\det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2$ |
| $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$ | the natural conjugation is the transposition |
| $\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})^{\mathsf{T}}\mathsf{M}_4(\tilde{Q})$ | the quaternionic product on the regular matrices |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})^{\mathsf{T}})=2\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form |
| $I_4$, split of signature $(4,4)$ | the coefficient Gram matrix and the real signature |
| $N(\tilde{Q})=0$ | the null set, the singular regular matrices of rank two |

## Further Reading

- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the representation and its first properties
- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/the-4x4-matrix-element-representation-of-biquaternions.md`), for the further reading of the regular representation
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the quaternionic product on the algebra
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form on the algebra
- *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-quaternionic-algebra-in-the-2x2-matrix-element-representation.md`), for the companion reading of the group
- *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the restriction theory of the form
