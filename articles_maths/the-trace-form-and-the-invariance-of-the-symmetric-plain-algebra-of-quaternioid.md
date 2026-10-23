# __The Trace Form and the Invariance of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ of *Introduction to the Symmetric Plain Algebra*, and with it a bilinear form read off the scalar part. This article studies the **trace form**

$$
\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}\bigl(\tilde q_1\bullet\tilde q_2\bigr),
$$

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

## The Trace Form

### The Definition

**Definition.** The **trace form** of the block is

$$
\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}\bigl(\tilde q_1\bullet\tilde q_2\bigr).
$$

**Proposition.** The trace form is symmetric and bilinear, and coincides with the plain bilinear form of the same space:

$$
\boxed{\;\tau(\tilde q_1,\tilde q_2)=q_{1t}q_{2t}-\vec q_1\cdot\vec q_2=\mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr)\;}.
$$

*Proof.* $\tilde q_1\bullet\tilde q_2$ is symmetric and bilinear, so $\tau$ is; and $\mathrm{Sc}(\tilde q_1\bullet\tilde q_2)=\mathrm{Sc}\bigl(\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)\bigr)=\mathrm{Sc}(\tilde q_1\tilde q_2)$ because the scalar part is invariant under reversal, $\mathrm{Sc}(\tilde q_1\tilde q_2)=\mathrm{Sc}(\tilde q_2\tilde q_1)$. Expanding the plain scalar part gives $q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$.

**Corollary (the polarisation).** The trace form is the **polarisation of the quadratic trace** $\tilde q\mapsto\mathrm{Sc}(\tilde q\bullet\tilde q)=\mathrm{Sc}(\tilde q^2)=q_t^2-|\vec q|^2$:

$$
\tau(\tilde q_1,\tilde q_2)=\tfrac12\Bigl(\mathrm{Sc}(\tilde q_1+\tilde q_2)^{\bullet2}-\mathrm{Sc}\,\tilde q_1^{\bullet2}-\mathrm{Sc}\,\tilde q_2^{\bullet2}\Bigr).
$$

### The Gram Matrix and the Signature

**Proposition.** In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the Gram matrix is $\operatorname{diag}(1,-1,-1,-1)$, and the signature is $(1,3)$: the trace form is **indefinite** and **Lorentzian**.

*Proof.* $\tau(e_t,e_t)=\mathrm{Sc}(e_t)=1$ and $\tau(\vec e_\mu,\vec e_\mu)=\mathrm{Sc}(\vec e_\mu\bullet \vec e_\mu)=\mathrm{Sc}(-e_t)=-1$ for $\mu=1,2,3$; the mixed terms vanish because $\vec e_\mu\bullet \vec e_\nu$ is pure for $\mu\neq\nu$.

**Remark (the trace form is not the norm).** The trace form is indefinite and has the isotropic cone $q_t^2=|\vec q|^2$; the norm $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$ is positive definite and vanishes only at the origin. **The two forms of the block must not be confused**: the norm polarises to the quaternion form (signature $(4,0)$) and the quadratic trace polarises to the trace form (signature $(1,3)$), as *Norm and Invertibility in the Symmetric Plain Algebra* records. In particular the isotropic cone of the trace form is **not** the zero-divisor set, which is the pure set $q_t=0$ of *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### The Radical

**Proposition.** The trace form is non-degenerate and its radical is trivial:

$$
\boxed{\;\operatorname{rad}\tau=\{\tilde q_1 : \tau(\tilde q_1,\tilde q_2)=0\ \text{for all}\ \tilde q_2\}=0\;}.
$$

*Proof.* The Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ is invertible, so the form is non-degenerate.

**Corollary.** The trace form identifies the algebra with its dual and provides the pairings used by the operators of the block; **it is not a semidefinite form, so it is not the wall form of the block.** The form that is definite is the norm, of the degree-two structure.

## The Invariance

### The Associativity of the Form

**Theorem (associativity).** The trace form is **associative** and **invariant** for the product:

$$
\boxed{\;\tau(\tilde q_1\bullet\tilde q_2,\tilde q_3)=\tau(\tilde q_1,\tilde q_2\bullet\tilde q_3)=\tau(\tilde q_2,\tilde q_1\bullet\tilde q_3)\;}.
$$

*Proof.* $\tau(\tilde q_1\bullet\tilde q_2,\tilde q_3)=\mathrm{Sc}((\tilde q_1\bullet\tilde q_2)\tilde q_3)$. Writing $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ and using the associativity of the plain product and the invariance of the scalar part under reversal, $\mathrm{Sc}(\tilde q_1\tilde q_2\tilde q_3)=\mathrm{Sc}(\tilde q_3\tilde q_1\tilde q_2)=\mathrm{Sc}(\tilde q_2\tilde q_3\tilde q_1)$, gives the equalities.

**Corollary.** The trace form is a **non-degenerate associative form** on the block, the property that a Jordan algebra of degree two carries; equivalently, every multiplication operator is self-adjoint for $\tau$:

$$
\tau(L^{\bullet}_{\tilde q_1}\tilde q_2,\tilde q_3)=\tau(\tilde q_2,L^{\bullet}_{\tilde q_1}\tilde q_3).
$$

### The Invariance under the Operators

**Theorem.** Every **derivation** of the block is skew for the trace form:

$$
\boxed{\;\tau(D\tilde q_1,\tilde q_2)+\tau(\tilde q_1,D\tilde q_2)=0\;}.
$$

*Proof.* The trace form is associative, so for a derivation $D$, $0=D\,\tau(\tilde q_1\bullet\tilde q_2,\tilde q_3)=\tau(D(\tilde q_1\bullet\tilde q_2),\tilde q_3)+\tau(\tilde q_1\bullet\tilde q_2,D\tilde q_3)$; expanding the derivation rule and using the associativity of $\tau$ twice gives $\tau(D\tilde q_1,\tilde q_2)+\tau(\tilde q_1,D\tilde q_2)=0$. The derivations are *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, and the statement is the general invariance of the trace form of a Jordan algebra quoted in *Jordan Algebras*.

**Remark (the invariance is the content of the menu).** The menu comment of the block asks for "the trace form and its invariance under the operators of the Jordan product": the **operators** are the left multiplications $L^{\bullet}_{\tilde q}$ and the inner derivations they generate, and the invariance is the pair of identities $\tau(L^{\bullet}_{\tilde q_1}\tilde q_2,\tilde q_3)=\tau(\tilde q_2,L^{\bullet}_{\tilde q_1}\tilde q_3)$ and $\tau(D\tilde q_1,\tilde q_2)+\tau(\tilde q_1,D\tilde q_2)=0$. **The self-adjointness is what makes the form the trace form, and the skewness of the derivations is what makes it the invariant form of the block.**

## Summary

The trace form of the block is $\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}(\tilde q_1\bullet\tilde q_2)$, symmetric and bilinear, equal to the plain form $q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$ and polarising the quadratic trace $\mathrm{Sc}(\tilde q^2)=q_t^2-|\vec q|^2$. Its Gram matrix in the standard basis is $\operatorname{diag}(1,-1,-1,-1)$, so its signature is $(1,3)$ and it is indefinite and Lorentzian; it is non-degenerate with radical $0$, and it is the indefinite companion of the positive definite norm. It is associative, $\tau(\tilde q_1\bullet\tilde q_2,\tilde q_3)=\tau(\tilde q_1,\tilde q_2\bullet\tilde q_3)$, so every multiplication operator is self-adjoint for it, and every derivation is skew for it; these two invariances are the form content of the block. Over $\mathbb{C}$ the trace form has the same matrix shape and the same invariances, the form part of the degree-two Common Theory; the field changes only the reading of the isotropy.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}(\tilde q_1\bullet\tilde q_2)=q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$ | the trace form |
| $\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix, signature $(1,3)$ |
| $\operatorname{rad}\tau=0$ | the radical |
| $\tau(\tilde q_1\bullet\tilde q_2,\tilde q_3)=\tau(\tilde q_1,\tilde q_2\bullet\tilde q_3)$ | associativity |
| $\tau(L^{\bullet}_{\tilde q_1}\tilde q_2,\tilde q_3)=\tau(\tilde q_2,L^{\bullet}_{\tilde q_1}\tilde q_3)$ | self-adjointness of the operators |
| $\tau(D\tilde q_1,\tilde q_2)+\tau(\tilde q_1,D\tilde q_2)=0$ | skewness of the derivations |

## Further Reading

- [Introduction to the Symmetric Plain Algebra](introduction-to-the-symmetric-plain-algebra-of-quaternioid.html), for the product.
- [Norm and Invertibility in the Symmetric Plain Algebra](norm-and-invertibility-in-the-symmetric-plain-algebra.html), for the norm, the quaternion form and the contrast with the trace form.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the isotropic cone of the trace form against the zero-divisor set.
- [The Multiplication Operators of the Symmetric Plain Algebra](the-multiplication-operators-of-the-symmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the operators and the derivations that are self-adjoint and skew.
- [The 2 Forms over the Quaternioid $\mathbb{R}$ Space](the-2-forms-over-the-quaternioid-r-space.html), for the plain and quaternionic forms.
- [Jordan Algebras](jordan-algebras.html), for the trace form of a Jordan algebra and its invariance.
