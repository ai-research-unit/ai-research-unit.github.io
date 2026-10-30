# __The General Plain Sesqualgebra in the $4\times4$ Left Regular Representation__

## Introduction

The left regular representation is built from the multiplication and carries the Hermitian conjugation as the **conjugate transpose**, $\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger}$, so it is a $*$-representation of the sesqualgebra. In the canonical frame of *Conventions of the Representations*, §*The Matrix Models*, the matrix is block diagonal, $I_2\otimes\mathsf M_2(\tilde Q)$, and the two blocks are the $2\times2$ matrix of the element. This article is the companion of *$M_2(\mathbb C)$ Representation : The General Plain Sesqualgebra of Biquaternions*, and it reads the group on the regular matrices: the sesquilinear product becomes the product with the conjugate-transposed second factor, and the general plain sesquilinear form becomes the Hilbert–Schmidt pairing, positive definite.

The canonical frame changes no formula of this group. The two operations used here, the matrix product and the dagger, act blockwise on $I_2\otimes A$, so the passage from the coefficient basis only changes the displayed generators and the block form. The positive definite form makes the Hermitian subspace a definite space on which the norm-one group acts, and that action is the two-to-one cover $SL_2(\mathbb C)\to SO^{+}(1,3)$.

**Conventions.** The algebra is $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$, with $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, $\mathsf M_2(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}$, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The Hermitian form is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$.

**Boundaries.** The representation is *$M_4(\mathbb C)_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*; the operator reading is *Two-Sided Operators on the Biquaternion Algebra*. The $2\times2$ companion is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation*; the form is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## The Representation

**Definition.** The left regular matrix is fixed by the multiplication in the canonical Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$:
$$
\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)
=\begin{pmatrix}A&0\\0&A\end{pmatrix},\qquad A=\mathsf M_2(\tilde Q),
$$
and the right regular matrix is $\mathsf M_4^{R}(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$. It satisfies
$$
\mathsf M_4^{L}(\tilde Q)\mathsf M_4^{L}(\tilde Q_2)=\mathsf M_4^{L}(\tilde Q\tilde Q_2),\qquad
\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger},
$$
$$
\operatorname{Tr}\mathsf M_4^{L}(\tilde Q)=4Q_t,\qquad
\det\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}.
$$
The star property holds blockwise and needs no carrier: the Hermitian conjugation of the element is the conjugate transpose of each block.

**The units.** The units of the algebra are the elements of non-zero norm, so their images form the group $\mathsf M_4^{L}(\mathbb B^{\times})\cong GL_2(\mathbb C)$ inside $GL_4(\mathbb C)$. The norm-one group $\{\tilde A:\langle\tilde A\rangle_{\natural}=1\}$ is $SL_2(\mathbb C)$, and its regular matrices have determinant one.

## The Sesquilinear Product in the Regular Representation

**Theorem (the conjugate-transposed product).** For all biquaternions,
$$
\boxed{\;\mathsf M_4^{L}(\tilde Q\star\tilde Q_2)=\mathsf M_4^{L}(\tilde Q)\,\mathsf M_4^{L}(\tilde Q_2)^{\dagger}\;}
$$
where $\tilde Q\star\tilde Q_2=\tilde Q\tilde Q_2^{*}$.

*Proof.* The representation is multiplicative and carries ${}^{*}$ to the dagger, so the image of $\tilde Q\tilde Q_2^{*}$ is $XY^{\dagger}$. $\square$

**The square and the unit.** At $\tilde Q_2=\tilde Q$ the theorem gives $XY^{\dagger}=\mathsf M_4^{L}(\tilde Q\tilde Q^{*})$, a positive semidefinite matrix whatever $\tilde Q$ is, because $I_2\otimes A$ is positive semidefinite exactly when $A$ is. The identity matrix $I_4=\mathsf M_4^{L}(e_t)$ is a **right unit alone**: $Y\star I_4=Y$, while $I_4\star Y=Y^{\dagger}$.

## The General Plain Sesquilinear Form in the Regular Representation

**Theorem (the Hilbert–Schmidt pairing).** For all biquaternions,
$$
\boxed{\;\tfrac12\operatorname{Tr}\bigl(\mathsf M_4^{L}(\tilde Q_1)^{\dagger}\mathsf M_4^{L}(\tilde Q_2)\bigr)
=2\,\langle\tilde Q_2,\tilde Q_1\rangle_{*}\;}
$$
so the Hilbert–Schmidt pairing of the regular matrices is twice the general plain sesquilinear form of the algebra, with the slots exchanged.

*Proof.* The dagger gives $\mathsf M_4^{L}(\tilde Q_1^{*})$, so the left-hand side is $\tfrac12\operatorname{Tr}\mathsf M_4^{L}(\tilde Q_1^{*}\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1^{*}\tilde Q_2)$. The scalar part is invariant under cyclic permutation, so $\mathrm{Sc}(\tilde Q_1^{*}\tilde Q_2)=\mathrm{Sc}(\tilde Q_2\tilde Q_1^{*})=\langle\tilde Q_2,\tilde Q_1\rangle_{*}$. $\square$

**Theorem (the Frobenius norm).** On the diagonal,
$$
\boxed{\;\lVert\mathsf M_4^{L}(\tilde Q)\rVert_F^{2}
=\operatorname{Tr}\bigl(\mathsf M_4^{L}(\tilde Q)^{\dagger}\mathsf M_4^{L}(\tilde Q)\bigr)
=4\sum_\mu|Q_\mu|^{2}=4\lVert\tilde Q\rVert_E^{2}\;}
$$
so the Frobenius norm of the regular matrix is twice the definite norm of the element.

**The signature and the null set.** The pairing is positive definite: on the four complex coordinates of the left copy it has signature $(8,0)$, and its null set is $\{0\}$ alone. The form is the restriction to $\mathbb B_L$ of the Hilbert–Schmidt form of $M_4(\mathbb C)$, not the whole of it.

**The isometry group.** The Hilbert–Schmidt form on the left copy has isometry group the unitary group $\mathrm U(4)$. The algebra automorphisms that are isometries are the inner maps $X\mapsto UXU^{\dagger}$ with $U\in\mathrm U(2)$, forming $PU(2)$. The larger family $X\mapsto UXV^{\dagger}$ with $U,V\in\mathrm U(2)$, forming $\mathrm U(2)\times\mathrm U(2)$ modulo the common centre, preserves the two-sided module structure but not the product.

**The two-sided action and the double cover.** The positive definite form makes the Hermitian subspace $\mathbb M_+$ a definite space of real dimension $4$, and the norm-one group $G=SL_2(\mathbb C)$ acts on it by $\tilde Q\mapsto\tilde A\tilde Q\tilde A^{*}$, preserving the norm:
$$
\langle\tilde A\tilde Q\tilde A^{*},\tilde A\tilde Q\tilde A^{*}\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural},\qquad \tilde A\in G.
$$
The action defines the surjective homomorphism $SL_2(\mathbb C)\to SO^{+}(1,3)$ with kernel $\{\pm e_t\}$, the two-to-one cover of the identity component of the orthogonal group of the restricted form. The statement is *Biquaternion Rotations and Lorentz Transformations*; the module reading is *The Category of Modules*.

## Worked Examples

**The identity.** For $\tilde Q=e_t$, $\mathsf M_4^{L}(e_t)=I_4$, $\lVert\mathsf M_4^{L}(e_t)\rVert_F^{2}=4=4\lVert e_t\rVert_E^{2}$, and $\tfrac12\operatorname{Tr}(I_4)=2=2\langle e_t,e_t\rangle_{*}$.

**A Hermitian element.** For $\tilde Q=e_t+i\vec e_z$ the element is Hermitian, $\tilde Q^{*}=\tilde Q$, so the regular matrix is Hermitian. Its square is $\tilde Q\star\tilde Q=\tilde Q^{2}=2e_t+2i\vec e_z=2\tilde Q$, a positive semidefinite element, and the pairing at the two equal arguments is $4\lVert\tilde Q\rVert_E^{2}=8$.

**A zero divisor.** For $\tilde Q=e_t+i\vec e_x$ the norm is $\langle\tilde Q\rangle_{\natural}=1+i^{2}=0$, so $\mathsf M_2(\tilde Q)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is singular and the regular matrix has rank two, while $\lVert\mathsf M_4^{L}(\tilde Q)\rVert_F^{2}=4\lVert\tilde Q\rVert_E^{2}=8$. The element is a zero divisor and a definite one for the general plain sesquilinear form.

## The Matrices

**The generators.** In the canonical frame the four units go to
$$
\mathsf M_4^{L}(e_t)=I_4,\qquad
\mathsf M_4^{L}(\vec e_x)=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
\mathsf M_4^{L}(\vec e_y)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
\mathsf M_4^{L}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}.
$$
A general element is the block matrix
$$
\mathsf M_4^{L}(\tilde Q)=\begin{pmatrix}A&0\\0&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix},
$$
with trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^{2}$, and the Hermitian conjugation carried to the conjugate transpose.

**The product, entry by entry.** A vector unit is anti-Hermitian, $\mathsf M_4^{L}(\vec e_y)^{\dagger}=-\mathsf M_4^{L}(\vec e_y)$, and the product at the pair $\vec e_x,\vec e_y$ is
$$
\mathsf M_4^{L}(\vec e_x)\mathsf M_4^{L}(\vec e_y)^{\dagger}
=-\mathsf M_4^{L}(\vec e_x)\mathsf M_4^{L}(\vec e_y)=-\mathsf M_4^{L}(\vec e_z),
$$
which is $\vec e_x\star\vec e_y=\vec e_x\vec e_y^{*}=-\vec e_z$.

**The right unit, entry by entry.** The identity matrix is a right unit and not a left one,
$$
I_4\star Y=Y^{\dagger},\qquad Y\star I_4=Y,
$$
and at $Y=\mathsf M_4^{L}(\vec e_x)$ the left action returns the negative, $Y^{\dagger}=-Y\neq Y$.

**The Frobenius norm, entry by entry.** The regular matrix of a vector unit has four entries of modulus one and the remaining twelve zero, so $\lVert\mathsf M_4^{L}(\vec e_x)\rVert_F^{2}=4$, in agreement with $4\sum_\mu|Q_\mu|^{2}$. The square of the product is the positive semidefinite matrix $\mathsf M_4^{L}(\tilde Q)\mathsf M_4^{L}(\tilde Q)^{\dagger}=I_2\otimes AA^{\dagger}$.

## Summary

In the canonical frame the left regular representation is a $*$-representation, $\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger}$, and it reads the sesquilinear product as $\mathsf M_4^{L}(\tilde Q\star\tilde Q_2)=\mathsf M_4^{L}(\tilde Q)\mathsf M_4^{L}(\tilde Q_2)^{\dagger}$, whose square is always positive semidefinite. The general plain sesquilinear form is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\mathsf M_4^{L}(\tilde Q_1)^{\dagger}\mathsf M_4^{L}(\tilde Q_2))=2\langle\tilde Q_2,\tilde Q_1\rangle_{*}$, positive definite of signature $(8,0)$ on the left copy, with Frobenius norm $\lVert\mathsf M_4^{L}(\tilde Q)\rVert_F=2\lVert\tilde Q\rVert_E$ and null set $\{0\}$; its isometry group is $\mathrm U(4)$, with isometric algebra automorphisms $PU(2)$. The two-sided action of the norm-one group $SL_2(\mathbb C)$ on the Hermitian subspace gives the double cover $SL_2(\mathbb C)\to SO^{+}(1,3)$, and the units of the algebra appear as the matrices of $GL_2(\mathbb C)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$ | the $4\times4$ left regular matrix, $\operatorname{Tr}=4Q_t$ |
| $\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger}$ | the Hermitian conjugation is the conjugate transpose |
| $\mathsf M_4^{L}(\tilde Q\star\tilde Q_2)=\mathsf M_4^{L}(\tilde Q)\mathsf M_4^{L}(\tilde Q_2)^{\dagger}$ | the sesquilinear product on the regular matrices |
| $\tfrac12\operatorname{Tr}(\mathsf M_4^{L}(\tilde Q_1)^{\dagger}\mathsf M_4^{L}(\tilde Q_2))=2\langle\tilde Q_2,\tilde Q_1\rangle_{*}$ | the general plain sesquilinear form as the Hilbert–Schmidt pairing |
| $\lVert\mathsf M_4^{L}(\tilde Q)\rVert_F=2\lVert\tilde Q\rVert_E$ | the Frobenius norm of the regular matrix |
| $SL_2(\mathbb C)\to SO^{+}(1,3)$ | the double cover of the two-sided action on the Hermitian subspace |

## Further Reading

- [$M_4(\mathbb C)_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the representation and its first properties
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the operator reading
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the sesquilinear product on the algebra
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form on the algebra
- [$M_2(\mathbb C)$ Representation : The General Plain Sesqualgebra of Biquaternions](the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the companion reading of the group
- [Remarkable Subspaces under the General Plain Sesqualgebra](remarkable-subspaces-under-the-general-plain-sesqualgebra.html), for the restriction theory of the form
