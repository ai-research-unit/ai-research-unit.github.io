# __The Trace Form and the Invariance of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{B}$ carries the product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra*, and a commutative algebra carries a form with it: the **trace form**

$$
\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_tQ_t-(\vec P,\vec Q),
$$

the scalar part of the product of the two elements. This article reads the form, its identity with the scalar part of the plain product, its Gram matrix, its **invariance** $\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)$, the operator traces built from it, and its restriction to the remarkable subspaces.

The form is not new to the algebra: it is the **general plain bilinear form** $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, which the associativity of the plain product makes invariant, and its operator theory is *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* and *Two-Sided Operators on the Biquaternion Algebra*. What this article adds is the same form read as the **trace form of the Jordan algebra**: the invariance becomes the associativity of the Jordan product read on the form, the polarisation of the form recovers the product, and the operator traces are the Jordan-algebra reading of the plain operators. The restrictions of the form to the remarkable subspaces are the subject of *Remarkable Subspaces and the Four Forms*; the form is used here with the product and not re-derived.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central scalar imaginary $i$. An element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_k\vec e_k$ and $Q_\mu\in\mathbb{C}$, and $(\vec P,\vec Q)=\sum_kP_kQ_k$. The scalar part is $\mathrm{Sc}(\tilde Q)=Q_t$; the general plain bilinear form is $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ with $\varepsilon=(1,-1,-1,-1)$, and $\tau$ denotes it read as the trace form of the block. The multiplication operator of the block is $L^{\bullet}_{\tilde P}\tilde Q=\tilde P\bullet\tilde Q$, and $L_{\tilde P},R_{\tilde P}$ are the left and right operators of the plain product, still with the halved product and the unhalved ones distinguished as in *The Multiplication Operators of the Symmetric Plain Algebra*.

## The Trace Form

### The Definition

**Definition.** The **trace form** of the symmetric plain algebra is

$$
\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q).
$$

**Proposition.** The form is $\mathbb{C}$-bilinear and **symmetric**:

$$
\tau(\tilde P,\tilde Q)=P_tQ_t-(\vec P,\vec Q)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu P_\mu Q_\mu,\qquad
\tau(\tilde P,\tilde Q)=\tau(\tilde Q,\tilde P).
$$

*Proof.* The scalar part of the product is $\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_tQ_t-(\vec P,\vec Q)$ by the scalar–vector rule of *Introduction to the Symmetric Plain Algebra*; the expression is symmetric in the two elements because the dot product is. Bilinearity is inherited from the product.

**Proposition (non-degeneracy).** The form is **non-degenerate**, and its Gram matrix on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is

$$
\operatorname{diag}(1,-1,-1,-1),
$$

the coefficient matrix $D$ of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, of complex rank four.

*Proof.* $\tau(e_\mu,e_\nu)=\mathrm{Sc}(e_\mu\bullet e_\nu)$; on the basis table of *Introduction to the Symmetric Plain Algebra* the values are $\varepsilon_\mu\delta_{\mu\nu}=(1,-1,-1,-1)$ on the diagonal and $0$ off it. The matrix is invertible, so the form is non-degenerate.

### The Identity with the Scalar Part of the Plain Product

**Theorem.** The trace form of the block is the scalar part of the **plain** product:

$$
\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=\langle\tilde P,\tilde Q\rangle .
$$

*Proof.* $\mathrm{Sc}(\tilde P\bullet\tilde Q)=\tfrac12\bigl(\mathrm{Sc}(\tilde P\tilde Q)+\mathrm{Sc}(\tilde Q\tilde P)\bigr)$, and the scalar part of a plain product is symmetric, $\mathrm{Sc}(\tilde P\tilde Q)=\mathrm{Sc}(\tilde Q\tilde P)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$. The half-sum is therefore the common value.

**Remark (the two readings are one form).** **The trace form of the Jordan algebra and the general plain bilinear form are the same form**, because the scalar part cannot see the cross term that distinguishes the plain product from its symmetrisation. The form is a form of the algebra and of the block at once, and the two readings differ only in what is put on the other side of it: the plain product in the algebra theory, the Jordan product here.

### The Gram Matrix on the Real Basis

The form is complex bilinear, and on the real basis of the algebra, $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$, its realification is the diagonal matrix

$$
\operatorname{diag}(1,-1,-1,-1,-1,1,1,1),
$$

of signature $(4,4)$.

*Proof.* On the four real directions the values are $\varepsilon_\mu$; on the four imaginary directions they are $\mathrm{Re}\,\tau(ie_\mu,ie_\nu)=\mathrm{Re}(i^2\varepsilon_\mu\delta_{\mu\nu})=-\varepsilon_\mu\delta_{\mu\nu}$, that is $-1,1,1,1$ on the diagonal; and the mixed values $\mathrm{Re}\,\tau(e_\mu,ie_\nu)$ vanish. The realified signature is $(4,4)$, the signature of the realified form of *The Realification and the Effect of the Change of Scalars*.

## The Invariance

### The Invariance Identity

**Theorem.** The trace form is **invariant** under the product:

$$
\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)
$$

for all $\tilde P,\tilde Q,\tilde R\in\mathbb{B}$.

*Proof.* By the definition of the form and the product,

$$
\tau(\tilde P\bullet\tilde Q,\tilde R)=\mathrm{Sc}\bigl((\tilde P\bullet\tilde Q)\tilde R\bigr)=\tfrac12\bigl(\mathrm{Sc}(\tilde P\tilde Q\tilde R)+\mathrm{Sc}(\tilde Q\tilde P\tilde R)\bigr),
$$

$$
\tau(\tilde P,\tilde Q\bullet\tilde R)=\mathrm{Sc}\bigl(\tilde P(\tilde Q\bullet\tilde R)\bigr)=\tfrac12\bigl(\mathrm{Sc}(\tilde P\tilde Q\tilde R)+\mathrm{Sc}(\tilde P\tilde R\tilde Q)\bigr).
$$

The first terms agree, and the second terms agree because $\mathrm{Sc}$ is invariant under the cyclic permutation of its factors, $\mathrm{Sc}(\tilde Q\tilde P\tilde R)=\mathrm{Sc}(\tilde P\tilde R\tilde Q)$; equivalently $\mathrm{Sc}(\tilde X\tilde Y\tilde Z)=\mathrm{Sc}(\tilde Z\tilde X\tilde Y)$, the associativity of the plain product read on the scalar part.

**Remark (invariance is associativity on the Jordan product).** The plain product is associative, so the scalar part of a triple product is invariant under cyclic permutation; the invariance of the trace form is exactly that statement written with the symmetrised product. **The form is associative in the Jordan sense**, and it is the trace form that the general theory of Jordan algebras attaches to a special Jordan algebra. The plain operator theory of the same form, the association and the transpose relative to the plain product, is *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*.

### The Polarisation That Recovers the Product

**Theorem.** The trace form and the unit recover the product. From

$$
T(\tilde P)=2\tau(\tilde P,e_t)=2P_t,\qquad
\langle\tilde P\rangle_{\natural}=2\tau(\tilde P,e_t)^2-\tau(\tilde P,\tilde P)=P_t^2+(\vec P,\vec P),
$$

the square is $\tilde P\bullet\tilde P=T(\tilde P)\tilde P-\langle\tilde P\rangle_{\natural}e_t$, and the product is its polarisation,

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl((\tilde P+\tilde Q)\bullet(\tilde P+\tilde Q)-\tilde P\bullet\tilde P-\tilde Q\bullet\tilde Q\bigr).
$$

*Proof.* The generic trace is $T(\tilde P)=2P_t=2\tau(\tilde P,e_t)$, and the generic norm of *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* is $\langle\tilde P\rangle_{\natural}=P_t^2+(\vec P,\vec P)=2P_t^2-\bigl(P_t^2-(\vec P,\vec P)\bigr)=2\tau(\tilde P,e_t)^2-\tau(\tilde P,\tilde P)$. The quadratic identity of the block gives $\tilde P\bullet\tilde P=T(\tilde P)\tilde P-\langle\tilde P\rangle_{\natural}e_t$, and the polarisation of the square gives the product.

**Remark (the form is a polar form).** The form is also the polar form of the **quadratic trace** $\tilde P\mapsto\mathrm{Sc}(\tilde P\bullet\tilde P)=\mathrm{Sc}(\tilde P^2)=\tau(\tilde P,\tilde P)$:

$$
\tau(\tilde P,\tilde Q)=\tfrac12\bigl(\tau(\tilde P+\tilde Q,\tilde P+\tilde Q)-\tau(\tilde P,\tilde P)-\tau(\tilde Q,\tilde Q)\bigr).
$$

**The same form is the polarisation of the quadratic trace and the datum from which the generic trace and the generic norm, and hence the product, are recovered**; this double role is what makes it the trace form of the block.

## The Operator Traces

### The Trace of a Multiplication Operator

**Proposition.** The multiplication operator of the block is $L^{\bullet}_{\tilde P}=\tfrac12(L_{\tilde P}+R_{\tilde P})$, and

$$
\operatorname{Tr}\bigl(L^{\bullet}_{\tilde P}\bigr)=4P_t=2T(\tilde P),\qquad
\det\bigl(L^{\bullet}_{\tilde P}\bigr)=P_t^2\,\langle\tilde P\rangle_{\natural}.
$$

*Proof.* $L^{\bullet}_{\tilde P}\tilde Q=\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)=\tfrac12(L_{\tilde P}+R_{\tilde P})\tilde Q$, so the two operators differ by the factor $\tfrac12$ and not by the sum alone; the trace of a plain operator is $\operatorname{Tr}(L_{\tilde P})=\operatorname{Tr}(R_{\tilde P})=4P_t$, so the trace of the half-sum is $4P_t=2T(\tilde P)$. The determinant is computed on the matrix of the operator; in the $2\times2$ model the operator is $M\mapsto\tfrac12(\mathsf{M}_2(\tilde P)M+M\mathsf{M}_2(\tilde P))$, whose eigenvalues are $\tfrac12(\lambda_i+\lambda_j)$ over the eigenvalues $\lambda_1,\lambda_2$ of $\mathsf{M}_2(\tilde P)$, giving $\det= P_t^2\langle\tilde P\rangle_{\natural}$.

**Remark (the factor of the operator identity).** The operator identity is

$$
L_{\tilde P}+R_{\tilde P}=2L^{\bullet}_{\tilde P},
$$

so the sum of the two plain operators is **twice** the multiplication operator of the block, and not the operator itself. **The multiplication operator of the symmetric plain algebra is half the sum of the left and right operators of the plain product**; the sum is the operator of the doubled product $\tilde P\tilde Q+\tilde Q\tilde P$.

### The Operator Trace and Its Relation to the Form

**Theorem.** For all $\tilde P,\tilde Q$,

$$
\operatorname{Tr}\bigl(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q}\bigr)=4P_tQ_t-2(\vec P,\vec Q)=2\tau(\tilde P,\tilde Q)+\tfrac12T(\tilde P)T(\tilde Q).
$$

*Proof.* With $L^{\bullet}=\tfrac12(L+R)$, the product expands as

$$
L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q}=\tfrac14\bigl(L_{\tilde P}L_{\tilde Q}+L_{\tilde P}R_{\tilde Q}+R_{\tilde P}L_{\tilde Q}+R_{\tilde P}R_{\tilde Q}\bigr),
$$

and the four plain traces are $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=4\tau(\tilde P,\tilde Q)$, $\operatorname{Tr}(R_{\tilde P}R_{\tilde Q})=4\tau(\tilde P,\tilde Q)$, and $\operatorname{Tr}(L_{\tilde P}R_{\tilde Q})=\operatorname{Tr}(R_{\tilde P}L_{\tilde Q})=4P_tQ_t$, computed on the bases of the left and right operators. Summing gives $\tfrac14\bigl(8\tau(\tilde P,\tilde Q)+8P_tQ_t\bigr)=2\tau(\tilde P,\tilde Q)+2P_tQ_t$, and $2P_tQ_t=\tfrac12T(\tilde P)T(\tilde Q)$.

**Remark (the trace is not the form).** The operator trace is **not** the trace form, and not a multiple of it either: the two coefficient pairs $(4,-2)$ and $(1,-1)$ are not proportional. Its excess over twice the form is exactly the term $\tfrac12T(\tilde P)T(\tilde Q)$ built from the generic trace, so the operator trace and $2\tau(\tilde P,\tilde Q)$ agree exactly on the elements of generic trace zero, that is on the hyperplane $P_t=0$ or $Q_t=0$; against four times the form, $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=4\tau(\tilde P,\tilde Q)$, the agreement is exactly on the pairs with $(\vec P,\vec Q)=0$. **The trace form is the polarisation of the quadratic trace, while the operator trace is a second, larger invariant**, and the two are related by the generic trace functional.

### The Trace Functional

**Definition.** The **trace functional** of the block is

$$
\tilde Q\longmapsto T(\tilde Q)=2Q_t=2\tau(\tilde Q,e_t).
$$

It is the linear form $\operatorname{Tr}\bigl(L^{\bullet}_{\tilde Q}\bigr)/2$, and it is the generic trace of *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*. The **generic norm** is $\langle\tilde Q\rangle_{\natural}=2\tau(\tilde Q,e_t)^2-\tau(\tilde Q,\tilde Q)$, the quadratic companion of the trace, and the ambient identity of the block is $\tilde Q\bullet\tilde Q-T(\tilde Q)\tilde Q+\langle\tilde Q\rangle_{\natural}e_t=0$.

**Remark (the two symmetric functions).** The trace functional and the generic norm are the two coefficients of the quadratic identity, and they are recovered from the trace form and the unit: $T(\tilde Q)=2\tau(\tilde Q,e_t)$ and $\langle\tilde Q\rangle_{\natural}=2\tau(\tilde Q,e_t)^2-\tau(\tilde Q,\tilde Q)$. **The trace form, the unit and the polarisation carry the whole degree-two structure of the block.**

## The Restriction to the Remarkable Subspaces

### The Restriction Matrices

The trace form is the general plain bilinear form, so its restrictions to the remarkable subspaces of *Introduction to the Remarkable Subspaces* are those of *Remarkable Subspaces and the Four Forms*, read here as the restrictions of the trace form of the block:

| Subspace | Natural real basis | Restriction matrix | Signature | Rank |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_t,\,ie_t$ | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | $(1,1)$ | $2$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $\vec e_x,\vec e_y,\vec e_z,\,i\vec e_x,i\vec e_y,i\vec e_z$ | $\operatorname{diag}(-1,-1,-1,1,1,1)$ | $(3,3)$ | $6$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_t,\vec e_x,\vec e_y,\vec e_z$ | $D=\operatorname{diag}(1,-1,-1,-1)$ | $(1,3)$ | $4$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $-D=\operatorname{diag}(-1,1,1,1)$ | $(3,1)$ | $4$ |
| Hermitian $\mathbb{M}_+$ | $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $\mathrm{I}_4=\operatorname{diag}(1,1,1,1)$ | $(4,0)$ | $4$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_t,\vec e_x,\vec e_y,\vec e_z$ | $-\mathrm{I}_4=\operatorname{diag}(-1,-1,-1,-1)$ | $(0,4)$ | $4$ |

The matrices are the same six as in *Remarkable Subspaces and the Four Forms*, because the trace form is the general plain bilinear form; the table is reproduced here with the reading of the block.

### The Isotropic Cones of the Restrictions

**Remark (the restriction and the cone of the block).** The restricted form is **non-degenerate on each of the remarkable subspaces**, of ranks $2,6,4,4,4,4$, and the four indefinite rows carry isotropic cones of real dimensions $1,5,3,3$ with the null elements $e_t+ie_t$, $\vec e_x+i\vec e_x$, $e_t+\vec e_x$ and $ie_t+i\vec e_x$. The two definite rows, the Hermitian and the anti-Hermitian, carry no isotropic vector. **The isotropic cone of the restriction is the intersection of the subspace with the cone of the form**, and it must not be confused with the isotropic cone of the generic norm: on the quaternion subspace, for instance, the trace form has the cone of signature $(1,3)$ computed here, while the generic norm $\sum_\mu Q_\mu^2$ vanishes on that subspace only at the origin.

## Summary

The trace form of the symmetric plain algebra is $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_tQ_t-(\vec P,\vec Q)$, which is the scalar part of the plain product and the general plain bilinear form. It is $\mathbb{C}$-bilinear, symmetric and non-degenerate, with Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ on the basis and realified signature $(4,4)$; it is invariant, $\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)$, which is the associativity of the plain product read on the Jordan product, and its polarisation recovers the quadratic trace, the generic trace $T(\tilde Q)=2\tau(\tilde Q,e_t)$ and the generic norm $\langle\tilde Q\rangle_{\natural}=2\tau(\tilde Q,e_t)^2-\tau(\tilde Q,\tilde Q)$, hence the product. The multiplication operator is $L^{\bullet}_{\tilde P}=\tfrac12(L_{\tilde P}+R_{\tilde P})$, of trace $4P_t=2T(\tilde P)$ and determinant $P_t^2\langle\tilde P\rangle_{\natural}$, and the operator trace is $\operatorname{Tr}(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q})=4P_tQ_t-2(\vec P,\vec Q)=2\tau(\tilde P,\tilde Q)+\tfrac12T(\tilde P)T(\tilde Q)$. On the remarkable subspaces the restrictions are those of the general plain bilinear form, of ranks $2,6,4,4,4,4$ and signatures $(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_tQ_t-(\vec P,\vec Q)$ | the trace form of the block |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)$ | the invariance of the form |
| $T(\tilde Q)=2\tau(\tilde Q,e_t)=2Q_t$ | the trace functional, the generic trace |
| $\langle\tilde Q\rangle_{\natural}=2\tau(\tilde Q,e_t)^2-\tau(\tilde Q,\tilde Q)$ | the generic norm |
| $L^{\bullet}_{\tilde P}=\tfrac12(L_{\tilde P}+R_{\tilde P})$ | the multiplication operator of the block |
| $\operatorname{Tr}(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q})=4P_tQ_t-2(\vec P,\vec Q)$ | the operator trace |
| $(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$ | the signatures of the restrictions |

## Further Reading

- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, for the general plain bilinear form, its coefficient matrix $D$ and its comparison with the other three forms.
- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*, for the associativity of the plain form and its operator theory.
- *Two-Sided Operators on the Biquaternion Algebra*, for the left and right operators whose half-sum is the multiplication operator of the block.
- *Remarkable Subspaces and the Four Forms*, for the restrictions of the form to the remarkable subspaces.
- *The Realification and the Effect of the Change of Scalars*, for the realified signature $(4,4)$.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, for the generic trace, the generic norm and the quadratic identity.
