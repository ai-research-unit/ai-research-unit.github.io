# __The Trace Form and the Invariance of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{B}$ carries the product $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ of *Introduction to the Symmetric Plain Algebra*, and a commutative algebra carries a form with it: the **trace form**

$$
\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2),
$$

the scalar part of the product of the two elements. This article reads the form, its identity with the scalar part of the plain product, its Gram matrix, its **invariance** $\tau(\tilde Q_1\bullet\tilde Q_2,\tilde Q_4)=\tau(\tilde Q_1,\tilde Q_2\bullet\tilde Q_4)$, the operator traces built from it, and its restriction to the remarkable subspaces.

The form is not new to the algebra: it is the **general plain bilinear form** $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, which the associativity of the plain product makes invariant, and its operator theory is *The Four Adjoints of the Biquaternion Algebra in Examples* and *Two-Sided Operators on the Biquaternion Algebra*. What this article adds is the same form read as the **trace form of the Jordan algebra**: the invariance becomes the associativity of the Jordan product read on the form, the polarisation of the form recovers the product, and the operator traces are the Jordan-algebra reading of the plain operators. The restrictions of the form to the remarkable subspaces are the subject of *Remarkable Subspaces and the Four General Products, Forms and Norms*; the form is used here with the product and not re-derived.

## The Trace Form

### The Definition

**Definition.** The **trace form** of the symmetric plain algebra is

$$
\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2).
$$

**Proposition.** The form is $\mathbb{C}$-bilinear and **symmetric**:

$$
\tau(\tilde Q_1,\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu} Q_{2\mu},\qquad
\tau(\tilde Q_1,\tilde Q_2)=\tau(\tilde Q_2,\tilde Q_1).
$$

*Proof.* The scalar part of the product is $\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ by the scalar–vector rule of *Introduction to the Symmetric Plain Algebra*; the expression is symmetric in the two elements because the dot product is. Bilinearity is inherited from the product.

**Proposition (non-degeneracy).** The form is **non-degenerate**, and its Gram matrix on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is

$$
\operatorname{diag}(1,-1,-1,-1),
$$

the coefficient matrix $D$ of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, of complex rank four.

*Proof.* $\tau(e_\mu,e_\nu)=\mathrm{Sc}(e_\mu\bullet e_\nu)$; on the basis table of *Introduction to the Symmetric Plain Algebra* the values are $\varepsilon_\mu\delta_{\mu\nu}=(1,-1,-1,-1)$ on the diagonal and $0$ off it. The matrix is invertible, so the form is non-degenerate.

### The Identity with the Scalar Part of the Plain Product

**Theorem.** The trace form of the block is the scalar part of the **plain** product:

$$
\boxed{\; \tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle \;}.
$$

*Proof.* $\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2)=\tfrac12\bigl(\mathrm{Sc}(\tilde Q_1\tilde Q_2)+\mathrm{Sc}(\tilde Q_2\tilde Q_1)\bigr)$, and the scalar part of a plain product is symmetric, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\mathrm{Sc}(\tilde Q_2\tilde Q_1)=\sum_\mu\varepsilon_\mu Q_{1\mu} Q_{2\mu}$. The half-sum is therefore the common value.

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
\boxed{\; \tau(\tilde Q_1\bullet\tilde Q_2,\tilde Q_4)=\tau(\tilde Q_1,\tilde Q_2\bullet\tilde Q_4) \;}
$$

for all $\tilde Q_1,\tilde Q_2,\tilde Q_4\in\mathbb{B}$.

*Proof.* By the definition of the form and the product,

$$
\tau(\tilde Q_1\bullet\tilde Q_2,\tilde Q_4)=\mathrm{Sc}\bigl((\tilde Q_1\bullet\tilde Q_2)\tilde Q_4\bigr)=\tfrac12\bigl(\mathrm{Sc}(\tilde Q_1\tilde Q_2\tilde Q_4)+\mathrm{Sc}(\tilde Q_2\tilde Q_1\tilde Q_4)\bigr),
$$

$$
\tau(\tilde Q_1,\tilde Q_2\bullet\tilde Q_4)=\mathrm{Sc}\bigl(\tilde Q_1(\tilde Q_2\bullet\tilde Q_4)\bigr)=\tfrac12\bigl(\mathrm{Sc}(\tilde Q_1\tilde Q_2\tilde Q_4)+\mathrm{Sc}(\tilde Q_1\tilde Q_4\tilde Q_2)\bigr).
$$

The first terms agree, and the second terms agree because $\mathrm{Sc}$ is invariant under the cyclic permutation of its factors, $\mathrm{Sc}(\tilde Q_2\tilde Q_1\tilde Q_4)=\mathrm{Sc}(\tilde Q_1\tilde Q_4\tilde Q_2)$; equivalently $\mathrm{Sc}(\tilde Q_1\tilde Q_2\tilde Q_3)=\mathrm{Sc}(\tilde Q_3\tilde Q_1\tilde Q_2)$, the associativity of the plain product read on the scalar part.

**Remark (invariance is associativity on the Jordan product).** The plain product is associative, so the scalar part of a triple product is invariant under cyclic permutation; the invariance of the trace form is exactly that statement written with the symmetrised product. **The form is associative in the Jordan sense**, and it is the trace form that the general theory of Jordan algebras attaches to a special Jordan algebra. The plain operator theory of the same form, the association and the transpose relative to the plain product, is *The Four Adjoints of the Biquaternion Algebra in Examples*.

### The Polarisation That Recovers the Product

**Theorem.** The trace form and the unit recover the product. From

$$
T(\tilde Q_1)=2\tau(\tilde Q_1,e_t)=2Q_{1t},\qquad
\langle\tilde Q_1\rangle_{\natural}=2\tau(\tilde Q_1,e_t)^2-\tau(\tilde Q_1,\tilde Q_1)=Q_{1t}^2+(\vec Q_1,\vec Q_1),
$$

the square is $\tilde Q_1\bullet\tilde Q_1=T(\tilde Q_1)\tilde Q_1-\langle\tilde Q_1\rangle_{\natural}e_t$, and the product is its polarisation,

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl((\tilde Q_1+\tilde Q_2)\bullet(\tilde Q_1+\tilde Q_2)-\tilde Q_1\bullet\tilde Q_1-\tilde Q_2\bullet\tilde Q_2\bigr).
$$

*Proof.* The generic trace is $T(\tilde Q_1)=2Q_{1t}=2\tau(\tilde Q_1,e_t)$, and the generic norm of *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* is $\langle\tilde Q_1\rangle_{\natural}=Q_{1t}^2+(\vec Q_1,\vec Q_1)=2Q_{1t}^2-\bigl(Q_{1t}^2-(\vec Q_1,\vec Q_1)\bigr)=2\tau(\tilde Q_1,e_t)^2-\tau(\tilde Q_1,\tilde Q_1)$. The quadratic identity of the block gives $\tilde Q_1\bullet\tilde Q_1=T(\tilde Q_1)\tilde Q_1-\langle\tilde Q_1\rangle_{\natural}e_t$, and the polarisation of the square gives the product.

**Remark (the form is a polar form).** The form is also the polar form of the **quadratic trace** $\tilde Q_1\mapsto\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_1)=\mathrm{Sc}(\tilde Q_1^2)=\tau(\tilde Q_1,\tilde Q_1)$:

$$
\tau(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(\tau(\tilde Q_1+\tilde Q_2,\tilde Q_1+\tilde Q_2)-\tau(\tilde Q_1,\tilde Q_1)-\tau(\tilde Q_2,\tilde Q_2)\bigr).
$$

**The same form is the polarisation of the quadratic trace and the datum from which the generic trace and the generic norm, and hence the product, are recovered**; this double role is what makes it the trace form of the block.

## The Operator Traces

### The Trace of a Multiplication Operator

**Proposition.** The multiplication operator of the block is $L^{\bullet}_{\tilde Q_1}=\tfrac12(L_{\tilde Q_1}+R_{\tilde Q_1})$, and

$$
\operatorname{Tr}\bigl(L^{\bullet}_{\tilde Q_1}\bigr)=4Q_{1t}=2T(\tilde Q_1),\qquad
\det\bigl(L^{\bullet}_{\tilde Q_1}\bigr)=Q_{1t}^2\,\langle\tilde Q_1\rangle_{\natural}.
$$

*Proof.* $L^{\bullet}_{\tilde Q_1}\tilde Q_2=\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)=\tfrac12(L_{\tilde Q_1}+R_{\tilde Q_1})\tilde Q_2$, so the two operators differ by the factor $\tfrac12$ and not by the sum alone; the trace of a plain operator is $\operatorname{Tr}(L_{\tilde Q_1})=\operatorname{Tr}(R_{\tilde Q_1})=4Q_{1t}$, so the trace of the half-sum is $4Q_{1t}=2T(\tilde Q_1)$. The determinant is computed on the matrix of the operator; in the $2\times2$ model the operator is $M\mapsto\tfrac12(\mathsf{M}_2(\tilde Q_1)M+M\mathsf{M}_2(\tilde Q_1))$, whose eigenvalues are $\tfrac12(\lambda_i+\lambda_j)$ over the eigenvalues $\lambda_1,\lambda_2$ of $\mathsf{M}_2(\tilde Q_1)$, giving $\det= Q_{1t}^2\langle\tilde Q_1\rangle_{\natural}$.

**Remark (the factor of the operator identity).** The operator identity is

$$
L_{\tilde Q_1}+R_{\tilde Q_1}=2L^{\bullet}_{\tilde Q_1},
$$

so the sum of the two plain operators is **twice** the multiplication operator of the block, and not the operator itself. **The multiplication operator of the symmetric plain algebra is half the sum of the left and right operators of the plain product**; the sum is the operator of the doubled product $\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1$.

### The Operator Trace and Its Relation to the Form

**Theorem.** For all $\tilde Q_1,\tilde Q_2$,

$$
\boxed{\; \operatorname{Tr}\bigl(L^{\bullet}_{\tilde Q_1}L^{\bullet}_{\tilde Q_2}\bigr)=4Q_{1t}Q_{2t}-2(\vec Q_1,\vec Q_2)=2\tau(\tilde Q_1,\tilde Q_2)+\tfrac12T(\tilde Q_1)T(\tilde Q_2) \;}.
$$

*Proof.* With $L^{\bullet}=\tfrac12(L+R)$, the product expands as

$$
L^{\bullet}_{\tilde Q_1}L^{\bullet}_{\tilde Q_2}=\tfrac14\bigl(L_{\tilde Q_1}L_{\tilde Q_2}+L_{\tilde Q_1}R_{\tilde Q_2}+R_{\tilde Q_1}L_{\tilde Q_2}+R_{\tilde Q_1}R_{\tilde Q_2}\bigr),
$$

and the four plain traces are $\operatorname{Tr}(L_{\tilde Q_1}L_{\tilde Q_2})=4\tau(\tilde Q_1,\tilde Q_2)$, $\operatorname{Tr}(R_{\tilde Q_1}R_{\tilde Q_2})=4\tau(\tilde Q_1,\tilde Q_2)$, and $\operatorname{Tr}(L_{\tilde Q_1}R_{\tilde Q_2})=\operatorname{Tr}(R_{\tilde Q_1}L_{\tilde Q_2})=4Q_{1t}Q_{2t}$, computed on the bases of the left and right operators. Summing gives $\tfrac14\bigl(8\tau(\tilde Q_1,\tilde Q_2)+8Q_{1t}Q_{2t}\bigr)=2\tau(\tilde Q_1,\tilde Q_2)+2Q_{1t}Q_{2t}$, and $2Q_{1t}Q_{2t}=\tfrac12T(\tilde Q_1)T(\tilde Q_2)$.

**Remark (the trace is not the form).** The operator trace is **not** the trace form, and not a multiple of it either: the two coefficient pairs $(4,-2)$ and $(1,-1)$ are not proportional. Its excess over twice the form is exactly the term $\tfrac12T(\tilde Q_1)T(\tilde Q_2)$ built from the generic trace, so the operator trace and $2\tau(\tilde Q_1,\tilde Q_2)$ agree exactly on the elements of generic trace zero, that is on the hyperplane $Q_{1t}=0$ or $Q_{2t}=0$; against four times the form, $\operatorname{Tr}(L_{\tilde Q_1}L_{\tilde Q_2})=4\tau(\tilde Q_1,\tilde Q_2)$, the agreement is exactly on the pairs with $(\vec Q_1,\vec Q_2)=0$. **The trace form is the polarisation of the quadratic trace, while the operator trace is a second, larger invariant**, and the two are related by the generic trace functional.

### The Trace Functional

**Definition.** The **trace functional** of the block is

$$
\tilde Q\longmapsto T(\tilde Q)=2Q_t=2\tau(\tilde Q,e_t).
$$

It is the linear form $\operatorname{Tr}\bigl(L^{\bullet}_{\tilde Q}\bigr)/2$, and it is the generic trace of *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*. The **generic norm** is $\langle\tilde Q\rangle_{\natural}=2\tau(\tilde Q,e_t)^2-\tau(\tilde Q,\tilde Q)$, the quadratic companion of the trace, and the ambient identity of the block is $\tilde Q\bullet\tilde Q-T(\tilde Q)\tilde Q+\langle\tilde Q\rangle_{\natural}e_t=0$.

**Remark (the two symmetric functions).** The trace functional and the generic norm are the two coefficients of the quadratic identity, and they are recovered from the trace form and the unit: $T(\tilde Q)=2\tau(\tilde Q,e_t)$ and $\langle\tilde Q\rangle_{\natural}=2\tau(\tilde Q,e_t)^2-\tau(\tilde Q,\tilde Q)$. **The trace form, the unit and the polarisation carry the whole degree-two structure of the block.**

## The Restriction to the Remarkable Subspaces

### The Restriction Matrices

The trace form is the general plain bilinear form, so its restrictions to the remarkable subspaces of *The Six Subspaces* are those of *Remarkable Subspaces and the Four General Products, Forms and Norms*, read here as the restrictions of the trace form of the block:

| Subspace | Natural real basis | Restriction matrix | Signature | Rank |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_t,\,ie_t$ | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | $(1,1)$ | $2$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $\vec e_x,\vec e_y,\vec e_z,\,i\vec e_x,i\vec e_y,i\vec e_z$ | $\operatorname{diag}(-1,-1,-1,1,1,1)$ | $(3,3)$ | $6$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_t,\vec e_x,\vec e_y,\vec e_z$ | $D=\operatorname{diag}(1,-1,-1,-1)$ | $(1,3)$ | $4$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $-D=\operatorname{diag}(-1,1,1,1)$ | $(3,1)$ | $4$ |
| Hermitian $\mathbb{M}_+$ | $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $\mathrm{I}_4=\operatorname{diag}(1,1,1,1)$ | $(4,0)$ | $4$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_t,\vec e_x,\vec e_y,\vec e_z$ | $-\mathrm{I}_4=\operatorname{diag}(-1,-1,-1,-1)$ | $(0,4)$ | $4$ |

The matrices are the same six as in *Remarkable Subspaces and the Four General Products, Forms and Norms*, because the trace form is the general plain bilinear form; the table is reproduced here with the reading of the block.

### The Isotropic Cones of the Restrictions

**Remark (the restriction and the cone of the block).** The restricted form is **non-degenerate on each of the remarkable subspaces**, of ranks $2,6,4,4,4,4$, and the four indefinite rows carry isotropic cones of real dimensions $1,5,3,3$ with the null elements $e_t+ie_t$, $\vec e_x+i\vec e_x$, $e_t+\vec e_x$ and $ie_t+i\vec e_x$. The two definite rows, the Hermitian and the anti-Hermitian, carry no isotropic vector. **The isotropic cone of the restriction is the intersection of the subspace with the cone of the form**, and it must not be confused with the isotropic cone of the generic norm: on the quaternion subspace, for instance, the trace form has the cone of signature $(1,3)$ computed here, while the generic norm $\sum_\mu Q_\mu^2$ vanishes on that subspace only at the origin.

## Summary

The trace form of the symmetric plain algebra is $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$, which is the scalar part of the plain product and the general plain bilinear form. It is $\mathbb{C}$-bilinear, symmetric and non-degenerate, with Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ on the basis and realified signature $(4,4)$; it is invariant, $\tau(\tilde Q_1\bullet\tilde Q_2,\tilde Q_4)=\tau(\tilde Q_1,\tilde Q_2\bullet\tilde Q_4)$, which is the associativity of the plain product read on the Jordan product, and its polarisation recovers the quadratic trace, the generic trace $T(\tilde Q_2)=2\tau(\tilde Q_2,e_t)$ and the generic norm $\langle\tilde Q_2\rangle_{\natural}=2\tau(\tilde Q_2,e_t)^2-\tau(\tilde Q_2,\tilde Q_2)$, hence the product. The multiplication operator is $L^{\bullet}_{\tilde Q_1}=\tfrac12(L_{\tilde Q_1}+R_{\tilde Q_1})$, of trace $4Q_{1t}=2T(\tilde Q_1)$ and determinant $Q_{1t}^2\langle\tilde Q_1\rangle_{\natural}$, and the operator trace is $\operatorname{Tr}(L^{\bullet}_{\tilde Q_1}L^{\bullet}_{\tilde Q_2})=4Q_{1t}Q_{2t}-2(\vec Q_1,\vec Q_2)=2\tau(\tilde Q_1,\tilde Q_2)+\tfrac12T(\tilde Q_1)T(\tilde Q_2)$. On the remarkable subspaces the restrictions are those of the general plain bilinear form, of ranks $2,6,4,4,4,4$ and signatures $(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ | the trace form of the block |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\tau(\tilde Q_1\bullet\tilde Q_2,\tilde Q_4)=\tau(\tilde Q_1,\tilde Q_2\bullet\tilde Q_4)$ | the invariance of the form |
| $T(\tilde Q)=2\tau(\tilde Q,e_t)=2Q_t$ | the trace functional, the generic trace |
| $\langle\tilde Q\rangle_{\natural}=2\tau(\tilde Q,e_t)^2-\tau(\tilde Q,\tilde Q)$ | the generic norm |
| $L^{\bullet}_{\tilde Q_1}=\tfrac12(L_{\tilde Q_1}+R_{\tilde Q_1})$ | the multiplication operator of the block |
| $\operatorname{Tr}(L^{\bullet}_{\tilde Q_1}L^{\bullet}_{\tilde Q_2})=4Q_{1t}Q_{2t}-2(\vec Q_1,\vec Q_2)$ | the operator trace |
| $(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$ | the signatures of the restrictions |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the general plain bilinear form, its coefficient matrix $D$ and its comparison with the other three forms.
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the associativity of the plain form and its operator theory.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the left and right operators whose half-sum is the multiplication operator of the block.
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the restrictions of the form to the remarkable subspaces.
- [The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra](the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.html), for the generic trace, the generic norm and the quadratic identity.
