
# __The Biquaternion Algebra over $\mathbb{R}$ in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The left regular matrix of the real algebra is a real $8\times8$ matrix $\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})$ on the eight-dimensional real space $\mathbb{B}$, and the trace form of the group is built from it directly, $\tau(\tilde{P},\tilde{Q})=\operatorname{Tr}(\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q}))$. This article is the companion of *The Biquaternion Algebra over $\mathbb{R}$ in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, and it reads the group *Topology on the Biquaternions as an Algebra over $\mathbb{R}$* on the real regular representation itself, which is the representation the trace form is defined from: the form is the trace of a product of real $8\times8$ matrices, the trace of a left multiplication is eight times a real coordinate, and the determinant of a left multiplication is the fourth power of the modulus of the norm.

The regular representation adds the two facts the $2\times2$ model cannot give: the trace form is literally a matrix trace, and the determinant of the left multiplication is the modulus of $N$ to the fourth power, so the real regular matrix detects the zero divisors with multiplicity four. In the complex regular basis the same form is twice the real part of the complex trace pairing, and the two factors $8$ and $2$ measure the passage between the real and the complex reading of the same representation.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$. The real basis is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$; $\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})$ is the real $8\times8$ matrix of left multiplication in that basis, and $\mathsf{M}_4(\tilde{Q})$ the complex $4\times4$ matrix in the basis $e_0,e_1,e_2,e_3$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Real Regular Representation

**Definition.** The **real regular matrix** is the isomorphism written $\mathsf{M}_4^{\mathbb{R}}$. It converts a biquaternion into an $8 \times 8$ real matrix,

$$
\mathsf{M}_4^{\mathbb{R}}:\mathbb{B}\longrightarrow M_8(\mathbb{R}),
$$

the matrix of left multiplication $\tilde{X}\mapsto\tilde{Q}\tilde{X}$ in the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$; it is fixed by its values on that basis, the rest following by $\mathbb{R}$-linearity. It satisfies

$$
\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=\mathsf{M}_4^{\mathbb{R}}(\tilde{P}\tilde{Q}),\qquad \operatorname{Tr}\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=8\,\mathrm{Re}\,Q_0,\qquad \det\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=|N(\tilde{Q})|^4 ,
$$

the determinant being the fourth power of the modulus because the complex regular matrix has determinant $N(\tilde{Q})^2$ and the realification doubles the determinant.

## The Trace Form in the Regular Representation

**Theorem (the trace form is a matrix trace).** For all biquaternions,

$$
\tau(\tilde{P},\tilde{Q})=\operatorname{Tr}\bigl(\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})\bigr)=8\,\mathrm{Re}\langle\tilde{P},\tilde{Q}\rangle ,
$$

the trace of the product of the two real $8\times8$ regular matrices, and it satisfies

$$
\operatorname{Tr}\bigl(\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})\bigr)=2\,\mathrm{Re}\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})\bigr) ,
$$

the passage between the real and the complex regular basis.

*Proof.* $\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=\mathsf{M}_4^{\mathbb{R}}(\tilde{P}\tilde{Q})$ and $\operatorname{Tr}\mathsf{M}_4^{\mathbb{R}}(\tilde{X})=8\mathrm{Re}\,X_0$, so $\operatorname{Tr}(\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q}))=8\mathrm{Re}\,\mathrm{Sc}(\tilde{P}\tilde{Q})$, which is the trace-form theorem; and $\operatorname{Tr}(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q}))=4\mathrm{Sc}(\tilde{P}\tilde{Q})$ gives the second identity.

**The diagonal and the signature.** With $\tilde{Q}=\sum_\mu(q_\mu+iq'_\mu)e_\mu$,

$$
\tau(\tilde{Q},\tilde{Q}) = 8\sum_\mu\varepsilon_\mu\bigl(q_\mu^2-q'_\mu{}^2\bigr) ,
$$

so the trace form has signature $(4,4)$ on the eight real coordinates, the four real parts of the coefficients carrying the sign $\varepsilon_\mu$ and the four imaginary parts the opposite sign. Its Gram matrix is the block matrix of *The Realification of the Four Forms* rescaled by $8$, and its null cone is the realified cone of the general plain bilinear form.

**The determinant and the zero divisors.** The left multiplication is invertible exactly when $N(\tilde{Q})\neq0$, so the zero divisors are exactly the singular real regular matrices; the determinant $|N(\tilde{Q})|^4$ vanishes on them to the fourth order, and the real rank of $\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})$ on a non-zero zero divisor is $4$, twice the complex rank $2$ of the regular matrix $\mathsf{M}_4(\tilde{Q})$.

**Invariance.** The trace form is invariant under the automorphisms of the algebra: for every unit $\tilde{A}$ and all biquaternions, $\tau(\tilde{A}\tilde{P}\tilde{A}^{-1},\tilde{A}\tilde{Q}\tilde{A}^{-1})=\tau(\tilde{P},\tilde{Q})$, because $\mathsf{M}_4^{\mathbb{R}}(\tilde{A}\tilde{P}\tilde{A}^{-1})=\mathsf{M}_4^{\mathbb{R}}(\tilde{A})\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{A})^{-1}$ and the trace is invariant under conjugation.

## The Four Realified Forms in the Regular Representation

The real parts of the four complex pairings of the regular model are

$$
\mathrm{Re}\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})\bigr),\quad \mathrm{Re}\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}\bigr),\quad \mathrm{Re}\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q})\bigr),\quad \mathrm{Re}\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q})\bigr),
$$

the trace pairings of the plain, transposed, conjugate-transposed and adjugated conjugate-transposed products. Their signatures are the four signatures of the group, $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$; the first is the trace form of this group up to the factor $2$, and all four are recorded in *The Realification of the Four Forms*. The Lorentzian forms do not appear here: the Minkowski form of signature $(1,3)$ recorded in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*, §*A Second $4 \times 4$ Realization, and the Multiplicative Map* is a form of the second real $4\times4$ realization, on the real span of $e_0,ie_1,ie_2,ie_3$, and the two-sided action of the norm-one group is the double cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$ of the sesqualgebra group.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $L_{e_0}=I_8$, $\operatorname{Tr}I_8=8=8\operatorname{Re}Q_0$ and $\det I_8=1=|N(e_0)|^4$, while $\tau(e_0,e_0)=8$.

**A basis element.** Let $\tilde{Q}=e_1$. Then $L_{e_1}$ is a real $8\times8$ signed permutation matrix with $\operatorname{Tr}L_{e_1}=8\operatorname{Re}0=0$ and $\det L_{e_1}=|N(e_1)|^4=|{-1}|^4=1$, and $\tau(e_1,e_1)=8\varepsilon_1=-8$.

**A zero divisor and a unit.** Let $\tilde{Q}=e_0+ie_1$. Then $N(\tilde{Q})=0$, so $\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})$ is singular and $\det \mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=0$, while $\tau(\tilde{Q},\tilde{Q})=8(1-1\cdot(0-1))=8(1+1)=16$, so the zero divisor is definite for the trace form; by contrast the unit $\tilde{P}=e_0+e_1$ has $\det \mathsf{M}_4^{\mathbb{R}}(\tilde{P})=|2|^4=16$ and $\tau(\tilde{P},\tilde{P})=8(1-1)=0$, so a unit can be isotropic.

## The Matrices

**The generators.** The real regular representation is fixed on the real basis by the eight matrices $\mathsf{M}_4^{\mathbb{R}}(e_0),\dots,\mathsf{M}_4^{\mathbb{R}}(e_3),\mathsf{M}_4^{\mathbb{R}}(ie_0),\dots,\mathsf{M}_4^{\mathbb{R}}(ie_3)$, and they are read from the complex regular matrices of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* by the block rule

$$
\mathsf{M}_4^{\mathbb{R}}(\tilde Q)=\begin{pmatrix}A&-B\\B&A\end{pmatrix},\qquad
A=\operatorname{Re}\mathsf{M}_4(\tilde Q),\qquad B=\operatorname{Im}\mathsf{M}_4(\tilde Q),
$$

in the basis ordered $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. The complex generators are

$$
\mathsf{M}_4(e_0)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

On a real element $B=0$ and the real regular matrix is block diagonal, $\mathsf{M}_4^{\mathbb{R}}(\tilde Q)=\operatorname{diag}\bigl(\mathsf{M}_4(\tilde Q),\mathsf{M}_4(\tilde Q)\bigr)$, while on the central scalar $A=0$ and

$$
\mathsf{M}_4^{\mathbb{R}}(ie_k)=\begin{pmatrix}0&-\mathsf{M}_4(e_k)\\\mathsf{M}_4(e_k)&0\end{pmatrix}.
$$

**The general element, entry by entry.** Writing $\tilde Q=P+iS$ with real $P$ and $S$, the real regular matrix is

$$
\mathsf{M}_4^{\mathbb{R}}(\tilde Q)=\begin{pmatrix}\mathsf{M}_4(P)&-\mathsf{M}_4(S)\\\mathsf{M}_4(S)&\mathsf{M}_4(P)\end{pmatrix},
$$

and its first column is the column $(P_0,P_1,P_2,P_3,S_0,S_1,S_2,S_3)^{\mathsf T}$ of the eight real coordinates of $\tilde Q$ in the order of the basis.

**The trace and the determinant, entry by entry.** The trace of the real regular matrix is eight times the real scalar part and its determinant is the fourth power of the modulus of the norm,

$$
\operatorname{Tr}\mathsf{M}_4^{\mathbb{R}}(\tilde Q)=8\operatorname{Re}Q_0,\qquad
\det\mathsf{M}_4^{\mathbb{R}}(\tilde Q)=|N(\tilde Q)|^4 ,
$$

read on the identity as $\mathsf{M}_4^{\mathbb{R}}(e_0)=I_8$, of trace $8$ and determinant $1$, and on the basis element as

$$
\mathsf{M}_4^{\mathbb{R}}(e_1)=\begin{pmatrix}\mathsf{M}_4(e_1)&0\\0&\mathsf{M}_4(e_1)\end{pmatrix},\qquad
\operatorname{Tr}\mathsf{M}_4^{\mathbb{R}}(e_1)=0,\qquad
\det\mathsf{M}_4^{\mathbb{R}}(e_1)=|-1|^4=1 .
$$

**The trace form, entry by entry.** The trace form is the matrix trace, and the two signs of its diagonal are read on the two copies of a basis vector. On $\tilde Q=e_1$ the real regular matrix squares to $-\mathsf{M}_4^{\mathbb{R}}(e_0)$,

$$
\mathsf{M}_4^{\mathbb{R}}(e_1)^2=\begin{pmatrix}\mathsf{M}_4(e_1)^2&0\\0&\mathsf{M}_4(e_1)^2\end{pmatrix}=-I_8,\qquad
\operatorname{Tr}\bigl(\mathsf{M}_4^{\mathbb{R}}(e_1)^2\bigr)=-8=\tau(e_1,e_1),
$$

and on $\tilde Q=ie_1$, whose real regular matrix carries the two off-diagonal blocks, the square is the positive identity,

$$
\mathsf{M}_4^{\mathbb{R}}(ie_1)=\begin{pmatrix}0&-\mathsf{M}_4(e_1)\\\mathsf{M}_4(e_1)&0\end{pmatrix},\qquad
\mathsf{M}_4^{\mathbb{R}}(ie_1)^2=+I_8,\qquad
\operatorname{Tr}\bigl(\mathsf{M}_4^{\mathbb{R}}(ie_1)^2\bigr)=+8=\tau(ie_1,ie_1).
$$

**The Gram matrix.** In the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ the trace form is diagonal,

$$
\bigl(\tau(x_i,x_j)\bigr)_{i,j}=\operatorname{diag}(8,-8,-8,-8,-8,8,8,8),
$$

four positive and four negative entries, of signature $(4,4)$; it is the same matrix as in the $2\times2$ reading, because the form lives on the algebra and not on the carrier.

**A zero divisor and a unit, entry by entry.** On the zero divisor $\tilde Q=e_0+ie_1$ the real regular matrix is

$$
\mathsf{M}_4^{\mathbb{R}}(e_0+ie_1)=\begin{pmatrix}I_4&-\mathsf{M}_4(e_1)\\\mathsf{M}_4(e_1)&I_4\end{pmatrix},
$$

of determinant $0$ and rank $4$, twice the complex rank $2$ of $\mathsf{M}_4(e_0+ie_1)$, while $\tau(\tilde Q,\tilde Q)=16$; on the unit $\tilde P=e_0+e_1$ the matrix is $\operatorname{diag}\bigl(\mathsf{M}_4(e_0+e_1),\mathsf{M}_4(e_0+e_1)\bigr)$, of determinant $|2|^4=16$ and rank $8$, while $\tau(\tilde P,\tilde P)=0$, so a unit can be isotropic.

## Summary

The real regular matrix is the representation the trace form is defined from, and it makes the three invariants literal: $\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=\mathsf{M}_4^{\mathbb{R}}(\tilde{P}\tilde{Q})$, $\operatorname{Tr}\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=8\operatorname{Re}Q_0$, and $\det \mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=|N(\tilde{Q})|^4$, the fourth power of the modulus of the norm. The trace form of the group is the matrix trace $\operatorname{Tr}(\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q}))=8\operatorname{Re}\langle\tilde{P},\tilde{Q}\rangle$, equal to twice the real part of the complex regular trace pairing, with diagonal $8\sum_\mu\varepsilon_\mu(q_\mu^2-q'_\mu{}^2)$ of signature $(4,4)$, Gram matrix the realified block matrix rescaled by $8$, invariant under the automorphisms of the algebra, and vanishing on the zero divisors to the fourth order through the determinant. The four realified forms have the signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$, and the Minkowski form of signature $(1,3)$ and the double cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$ belong to the Lorentzian slice and the sesqualgebra group respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})$ | the real $8\times8$ left regular matrix, $\operatorname{Tr}\mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=8\operatorname{Re}Q_0$, $\det \mathsf{M}_4^{\mathbb{R}}(\tilde{Q})=\lvert N(\tilde{Q})\rvert^4$ |
| $\tau(\tilde{P},\tilde{Q})=\operatorname{Tr}(\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q}))$ | the trace form of the group |
| $\operatorname{Tr}(\mathsf{M}_4^{\mathbb{R}}(\tilde{P})\mathsf{M}_4^{\mathbb{R}}(\tilde{Q}))=2\operatorname{Re}\operatorname{Tr}(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q}))$ | the passage to the complex regular basis |
| $8\sum_\mu\varepsilon_\mu(q_\mu^2-q'_\mu{}^2)$ | the diagonal, signature $(4,4)$ |
| $(4,4),(4,4),(8,0),(2,6)$ | the signatures of the four realified forms |
| $\lvert N(\tilde{Q})\rvert^4$ | the determinant of the left multiplication, vanishing on the zero divisors |

## Further Reading

- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the regular representation and its first properties
- *The Trace Form of the Real Biquaternion Algebra* (`articles_maths/the-trace-form-of-the-real-biquaternion-algebra.md`), for the trace form on the algebra
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the signature table of the realified forms
- *Operators of the Real Biquaternion Algebra* (`articles_maths/operators-of-the-real-biquaternion-algebra.md`), for the operators of the real reading
- *The Biquaternion Algebra over $\mathbb{R}$ in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-biquaternion-algebra-over-r-in-the-2x2-matrix-element-representation.md`), for the companion reading of the group
- *Remarkable Subspaces under the Real Biquaternion Algebra* (`articles_maths/remarkable-subspaces-under-the-real-biquaternion-algebra.md`), for the restriction theory of the trace form
