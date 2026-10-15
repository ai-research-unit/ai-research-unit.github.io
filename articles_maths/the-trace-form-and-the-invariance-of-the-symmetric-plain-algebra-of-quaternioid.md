# __The Trace Form and the Invariance of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra of Quaternions*, and with it a bilinear form read off the scalar part. This article studies the **trace form**

$$
\tau(\tilde p,\tilde q)=\mathrm{Sc}\bigl(\tilde p\bullet\tilde q\bigr),
$$

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1^2=e_2^2=e_3^2=-e_0$. An element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; the scalar part is $\mathrm{Sc}$, the vector subspace is $\mathrm{Vect}(\mathbb{H})$, the norm is $N(\tilde q)=q_0^2+|\vec q|^2$, and the multiplication operator is $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$ of *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category. The plain bilinear form $(\tilde p,\tilde q)\mapsto\mathrm{Sc}(\tilde p\tilde q)$ is *The 2 Forms over the Quaternion $\mathbb{R}$ Space*.

## The Trace Form

### The Definition

**Definition.** The **trace form** of the block is

$$
\tau(\tilde p,\tilde q)=\mathrm{Sc}\bigl(\tilde p\bullet\tilde q\bigr).
$$

**Proposition.** The trace form is symmetric and bilinear, and coincides with the plain bilinear form of the same space:

$$
\tau(\tilde p,\tilde q)=p_0q_0-\vec p\cdot\vec q=\mathrm{Sc}\bigl(\tilde p\tilde q\bigr).
$$

*Proof.* $\tilde p\bullet\tilde q$ is symmetric and bilinear, so $\tau$ is; and $\mathrm{Sc}(\tilde p\bullet\tilde q)=\mathrm{Sc}\bigl(\tfrac12(\tilde p\tilde q+\tilde q\tilde p)\bigr)=\mathrm{Sc}(\tilde p\tilde q)$ because the scalar part is invariant under reversal, $\mathrm{Sc}(\tilde p\tilde q)=\mathrm{Sc}(\tilde q\tilde p)$. Expanding the plain scalar part gives $p_0q_0-\vec p\cdot\vec q$.

**Corollary (the polarisation).** The trace form is the **polarisation of the quadratic trace** $\tilde p\mapsto\mathrm{Sc}(\tilde p\bullet\tilde p)=\mathrm{Sc}(\tilde p^2)=p_0^2-|\vec p|^2$:

$$
\tau(\tilde p,\tilde q)=\tfrac12\Bigl(\mathrm{Sc}(\tilde p+\tilde q)^{\bullet2}-\mathrm{Sc}\,\tilde p^{\bullet2}-\mathrm{Sc}\,\tilde q^{\bullet2}\Bigr).
$$

### The Gram Matrix and the Signature

**Proposition.** In the basis $(e_0,e_1,e_2,e_3)$ the Gram matrix is $\operatorname{diag}(1,-1,-1,-1)$, and the signature is $(1,3)$: the trace form is **indefinite** and **Lorentzian**.

*Proof.* $\tau(e_0,e_0)=\mathrm{Sc}(e_0)=1$ and $\tau(e_j,e_j)=\mathrm{Sc}(e_j\bullet e_j)=\mathrm{Sc}(-e_0)=-1$ for $j=1,2,3$; the mixed terms vanish because $e_j\bullet e_k$ is pure for $j\neq k$.

**Remark (the trace form is not the norm).** The trace form is indefinite and has the isotropic cone $p_0^2=|\vec p|^2$; the norm $N(\tilde p)=p_0^2+|\vec p|^2$ is positive definite and vanishes only at the origin. **The two forms of the block must not be confused**: the norm polarises to the quaternion form (signature $(4,0)$) and the quadratic trace polarises to the trace form (signature $(1,3)$), as *Norm and Invertibility in the Symmetric Plain Algebra* records. In particular the isotropic cone of the trace form is **not** the zero-divisor set, which is the pure set $p_0=0$ of *Zero Divisors of the Symmetric Plain Algebra*.

### The Radical

**Proposition.** The trace form is non-degenerate and its radical is trivial:

$$
\operatorname{rad}\tau=\{\tilde p : \tau(\tilde p,\tilde q)=0\ \text{for all}\ \tilde q\}=0 .
$$

*Proof.* The Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ is invertible, so the form is non-degenerate.

**Corollary.** The trace form identifies the algebra with its dual and provides the pairings used by the operators of the block; **it is not a semidefinite form, so it is not the wall form of the block.** The form that is definite is the norm, of the degree-two structure.

## The Invariance

### The Associativity of the Form

**Theorem (associativity).** The trace form is **associative** and **invariant** for the product:

$$
\tau(\tilde p\bullet\tilde q,\tilde r)=\tau(\tilde p,\tilde q\bullet\tilde r)=\tau(\tilde q,\tilde p\bullet\tilde r).
$$

*Proof.* $\tau(\tilde p\bullet\tilde q,\tilde r)=\mathrm{Sc}((\tilde p\bullet\tilde q)\tilde r)$. Writing $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ and using the associativity of the plain product and the invariance of the scalar part under reversal, $\mathrm{Sc}(\tilde p\tilde q\tilde r)=\mathrm{Sc}(\tilde r\tilde p\tilde q)=\mathrm{Sc}(\tilde q\tilde r\tilde p)$, gives the equalities.

**Corollary.** The trace form is a **non-degenerate associative form** on the block, the property that a Jordan algebra of degree two carries; equivalently, every multiplication operator is self-adjoint for $\tau$:

$$
\tau(L^{\bullet}_{\tilde p}\tilde q,\tilde r)=\tau(\tilde q,L^{\bullet}_{\tilde p}\tilde r).
$$

### The Invariance under the Operators

**Theorem.** Every **derivation** of the block is skew for the trace form:

$$
\tau(D\tilde p,\tilde q)+\tau(\tilde p,D\tilde q)=0 .
$$

*Proof.* The trace form is associative, so for a derivation $D$, $0=D\,\tau(\tilde p\bullet\tilde q,\tilde r)=\tau(D(\tilde p\bullet\tilde q),\tilde r)+\tau(\tilde p\bullet\tilde q,D\tilde r)$; expanding the derivation rule and using the associativity of $\tau$ twice gives $\tau(D\tilde p,\tilde q)+\tau(\tilde p,D\tilde q)=0$. The derivations are *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, and the statement is the general invariance of the trace form of a Jordan algebra quoted in *Jordan Algebras*.

**Remark (the invariance is the content of the menu).** The menu comment of the block asks for "the trace form and its invariance under the operators of the Jordan product": the **operators** are the left multiplications $L^{\bullet}_{\tilde p}$ and the inner derivations they generate, and the invariance is the pair of identities $\tau(L^{\bullet}_{\tilde p}\tilde q,\tilde r)=\tau(\tilde q,L^{\bullet}_{\tilde p}\tilde r)$ and $\tau(D\tilde p,\tilde q)+\tau(\tilde p,D\tilde q)=0$. **The self-adjointness is what makes the form the trace form, and the skewness of the derivations is what makes it the invariant form of the block.**

## Summary

The trace form of the block is $\tau(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\bullet\tilde q)$, symmetric and bilinear, equal to the plain form $p_0q_0-\vec p\cdot\vec q$ and polarising the quadratic trace $\mathrm{Sc}(\tilde p^2)=p_0^2-|\vec p|^2$. Its Gram matrix in the standard basis is $\operatorname{diag}(1,-1,-1,-1)$, so its signature is $(1,3)$ and it is indefinite and Lorentzian; it is non-degenerate with radical $0$, and it is the indefinite companion of the positive definite norm. It is associative, $\tau(\tilde p\bullet\tilde q,\tilde r)=\tau(\tilde p,\tilde q\bullet\tilde r)$, so every multiplication operator is self-adjoint for it, and every derivation is skew for it; these two invariances are the form content of the block. Over $\mathbb{C}$ the trace form has the same matrix shape and the same invariances, the form part of the degree-two Common Theory; the field changes only the reading of the isotropy.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\bullet\tilde q)=p_0q_0-\vec p\cdot\vec q$ | the trace form |
| $\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix, signature $(1,3)$ |
| $\operatorname{rad}\tau=0$ | the radical |
| $\tau(\tilde p\bullet\tilde q,\tilde r)=\tau(\tilde p,\tilde q\bullet\tilde r)$ | associativity |
| $\tau(L^{\bullet}_{\tilde p}\tilde q,\tilde r)=\tau(\tilde q,L^{\bullet}_{\tilde p}\tilde r)$ | self-adjointness of the operators |
| $\tau(D\tilde p,\tilde q)+\tau(\tilde p,D\tilde q)=0$ | skewness of the derivations |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm, the quaternion form and the contrast with the trace form.
- *Zero Divisors of the Symmetric Plain Algebra*, for the isotropic cone of the trace form against the zero-divisor set.
- *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, for the operators and the derivations that are self-adjoint and skew.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, for the plain and quaternionic forms.
- *Jordan Algebras*, for the trace form of a Jordan algebra and its invariance.
