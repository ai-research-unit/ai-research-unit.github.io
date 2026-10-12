# __The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra of Quaternions*. It is the specialisation of the degree-two Common Theory of *The Two General Products of an Algebra with Involution* to the real quaternions.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1^2=e_2^2=e_3^2=-e_0$. An element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; the norm is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+|\mathbf q|^2$, the generic trace is $T(\tilde q)=2q_0$, and the multiplication operator is $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$ of *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category.

## The Square Map

**Definition.** The **square map** of the block is

$$
Q:\tilde p\mapsto\tilde p\bullet\tilde p=\tilde p^2,\qquad
Q(\tilde p)=\bigl(p_0^2-|\mathbf p|^2\bigr)e_0+2p_0\mathbf p .
$$

It is the diagonal of the product; the polarisation $Q(\tilde p,\tilde q)=\tfrac12\bigl(Q(\tilde p+\tilde q)-Q(\tilde p)-Q(\tilde q)\bigr)$ is the product, $Q(\tilde p,\tilde q)=\tilde p\bullet\tilde q$.

**Proposition (the relation to the norm).** The square, the trace and the norm are tied by

$$
\mathrm{Sc}\,\tilde p^2=p_0^2-|\mathbf p|^2=2p_0^2-N(\tilde p),\qquad
N(\tilde p)=p_0^{\,2}+|\mathbf p|^{\,2},
$$

and by the quadratic identity $\tilde p^2-T(\tilde p)\tilde p+N(\tilde p)e_0=0$. The square of the block is the **plain square**; it is **not** the quaternionic square, whose value is the central element $\tilde p^{\natural}\tilde p=N(\tilde p)e_0$, and the two agree only on the scalar line.

*Proof.* The square is displayed above; the scalar part is $p_0^2-|\mathbf p|^2$, the vector part $2p_0\mathbf p$. The plain square is quoted from *Introduction to the General Plain Algebra of Quaternions* and the quaternionic square from *Introduction to the General Quaternionic Algebra of Quaternions*, below this article in this category; the quadratic identity is *Norm and Invertibility in the Symmetric Plain Algebra*.

**Remark (the two general products on one square).** The chapter carries two general products, the plain product $\tilde p\tilde q$ and the quaternionic product $\tilde p^{\natural}\tilde q$; the square of the block is the square of the first, and the symmetrisation of the second, *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, below this article in this category, has the central square $N(\tilde p)e_0$. **The division of the real chapter is between these two squares**, and the block's square is the non-central one.

## The Idempotents and Their Degeneracy

**Definition.** An **idempotent** of the block is an element with $\tilde\pi\bullet\tilde\pi=\tilde\pi$.

**Theorem.** The idempotents of the block are exactly

$$
\tilde\pi\in\{0,\ e_0\},
$$

the two trivial idempotents; there is no nontrivial one.

*Proof.* The square is the plain square, so the equation is $\tilde\pi^2=\tilde\pi$. The vector part gives $(2\pi_0-1)\boldsymbol{\pi}=0$, so either $\boldsymbol{\pi}=0$ and the scalar part gives $\pi_0^2=\pi_0$, giving $\tilde\pi\in\{0,e_0\}$, or $\pi_0=\tfrac12$ and the scalar part gives $|\boldsymbol{\pi}|^2=-\tfrac14$, with no real solution.

**Remark (the degeneracy in a division algebra).** A nontrivial idempotent is built, in a split algebra, from a pure root of $+e_0$ by $\tilde\pi=\tfrac12(e_0+\mathbf u)$, and the reason the construction fails here is that **the pure square is negative**: $\mathbf u\bullet\mathbf u=-|\mathbf u|^2e_0$, so a pure element can be a root of $-e_0$ but never a root of $+e_0$. Over a division algebra with a negative definite pure part the construction never closes, and the idempotent class collapses to the two trivial elements; the collapse is the algebraic form of the absence of the split.

**Corollary (the associated idempotents).** The only idempotents associated with the zero divisors are the trivial ones: a nonzero pure element $\mathbf u$ is a zero divisor but the element $\tfrac12(e_0+\mathbf u)$ has square $\tfrac14(1-|\mathbf u|^2)e_0+\tfrac12\mathbf u$, which is not an idempotent for any real $\mathbf u$.

## The Peirce Decomposition

**Theorem (the cubic identity).** The multiplication operator satisfies the cubic Peirce identity

$$
2\,(L^{\bullet}_{\tilde\pi})^3-3\,(L^{\bullet}_{\tilde\pi})^2+L^{\bullet}_{\tilde\pi}=0
$$

at every idempotent $\tilde\pi$, so the spectrum is contained in $\{0,\tfrac12,1\}$.

*Proof.* The identity holds in every Jordan algebra for an idempotent, by the Peirce theory of *Jordan Algebras*; in the block it is checked directly from $L^{\bullet}_{e_0}=\mathrm{id}$ and $L^{\bullet}_{0}=0$.

**Theorem (the Peirce decomposition).** For the two idempotents the decomposition is trivial:

$$
J_1(e_0)=\mathbb{H},\quad J_{1/2}(e_0)=J_0(e_0)=0;
\qquad
J_0(0)=\mathbb{H},\quad J_1(0)=J_{1/2}(0)=0,
$$

where $J_\lambda(\tilde\pi)=\{\tilde x : \tilde\pi\bullet\tilde x=\lambda\tilde x\}$.

*Proof.* $L^{\bullet}_{e_0}=\mathrm{id}$ has the single eigenvalue $1$ with multiplicity four; $L^{\bullet}_{0}=0$ has the single eigenvalue $0$ with multiplicity four.

**Remark (the would-be shape).** A nontrivial idempotent of a degree-two block of this kind would split the algebra into three Peirce spaces of dimensions $1,2,1$; since the block has only $0$ and $e_0$, **the middle space never opens and the Peirce calculus is degenerate.** This is the specific-theory reading of the degeneracy of the previous section, and it is the reason the block carries no projector calculus.

## The Jordan Inverse

**Theorem.** An element is invertible exactly when $N(\tilde p)\neq0$, that is, when $\tilde p\neq0$, and the inverse is

$$
\tilde p^{-1}=\frac{T(\tilde p)e_0-\tilde p}{N(\tilde p)}=\frac{2p_0e_0-\tilde p}{N(\tilde p)}=\frac{\tilde p^{\natural}}{N(\tilde p)} .
$$

*Proof.* This is *Norm and Invertibility in the Symmetric Plain Algebra*; the inverse satisfies $\tilde p\bullet\tilde p^{-1}=e_0$ and $\tilde p^{\bullet2}\bullet\tilde p^{-1}=\tilde p$.

**Proposition (the two-sidedness and the failure of multiplicativity).** The inverse is two-sided and involutive, $(\tilde p^{-1})^{-1}=\tilde p$; but the inversion is not a homomorphism, and the invertible elements do not form a group, since $e_1,e_2$ are invertible and $e_1\bullet e_2=0$ has no inverse.

*Proof.* The two-sidedness is commutativity and the first defining equation; the failure of multiplicativity is the pair $e_1,e_2$.

## The Quadratic Representation

**Definition.** The **quadratic representation** of the block is

$$
U_{\tilde p}=2\,(L^{\bullet}_{\tilde p})^2-L^{\bullet}_{\tilde p^{\,\bullet2}},
\qquad
U_{\tilde p}(\tilde q)=2\,\tilde p\bullet(\tilde p\bullet\tilde q)-\tilde p^{\bullet2}\bullet\tilde q .
$$

**Theorem.** The quadratic representation is the plain sandwich operator and it is multiplicative in the norm:

$$
U_{\tilde p}(\tilde q)=\tilde p\,\tilde q\,\tilde p,\qquad
N\bigl(U_{\tilde p}\tilde q\bigr)=N(\tilde p)^2N(\tilde q).
$$

*Proof.* Expanding $U_{\tilde p}(\tilde q)$ in the symmetrised plain product, $U_{\tilde p}(\tilde q)=\tfrac12\bigl(\tilde p(\tilde p\tilde q+\tilde q\tilde p)+(\tilde p\tilde q+\tilde q\tilde p)\tilde p\bigr)-\tfrac12(\tilde p^2\tilde q+\tilde q\tilde p^2)=\tilde p\tilde q\tilde p$ by the associativity of the plain product. The norm identity is the multiplicativity of $N$ applied twice, $N(\tilde p\tilde q\tilde p)=N(\tilde p)^2N(\tilde q)$.

**Remark (the effect on the norm).** For a nonzero $\tilde p$ the operator $U_{\tilde p}$ is invertible with inverse $U_{\tilde p^{-1}}$, and $U_{\tilde p^{-1}}=U_{\tilde p}^{-1}$; the norm identity is the degree-two form of the composite, and it is the quadratic representation statement of the degree-two Common Theory of *The Two General Products of an Algebra with Involution* read on the block.

## Summary

The square map of the block is the plain square, $Q(\tilde p)=(p_0^2-|\mathbf p|^2)e_0+2p_0\mathbf p$, polarising to the product, with the scalar part $2p_0^2-N(\tilde p)$ and the quadratic identity $\tilde p^2-T(\tilde p)\tilde p+N(\tilde p)e_0=0$. The idempotents are exactly $0$ and $e_0$, because a nontrivial idempotent would need a pure root of $+e_0$ and the pure square is $-|\mathbf u|^2e_0$; the Peirce decomposition is trivial, $J_1(e_0)=\mathbb{H}$ and $J_0(0)=\mathbb{H}$ with the other spaces vanishing. The Jordan inverse is $\tilde p^{-1}=(T(\tilde p)e_0-\tilde p)/N(\tilde p)=\tilde p^{\natural}/N(\tilde p)$ for $\tilde p\neq0$, two-sided and involutive but not multiplicative, and the invertible elements do not form a group. The quadratic representation is $U_{\tilde p}=2(L^{\bullet}_{\tilde p})^2-L^{\bullet}_{\tilde p^{\,\bullet2}}$, equal to the sandwich $\tilde p\tilde q\tilde p$, and $N(U_{\tilde p}\tilde q)=N(\tilde p)^2N(\tilde q)$. Everything but the idempotents and the Peirce decomposition has the same shape over $\mathbb{C}$; there the idempotents are many and the Peirce calculus opens.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q(\tilde p)=\tilde p\bullet\tilde p=\tilde p^2$ | the square map |
| $\mathbf u\bullet\mathbf u=-\lvert\mathbf u\rvert^2e_0$ | the square of a pure element |
| $\{0,e_0\}$ | the idempotents |
| $J_\lambda(\tilde\pi)$ | the Peirce spaces, trivial at $0$ and $e_0$ |
| $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$ | the Jordan inverse |
| $U_{\tilde p}=2(L^{\bullet}_{\tilde p})^2-L^{\bullet}_{\tilde p^{\,\bullet2}}$ | the quadratic representation, $=\tilde p\tilde q\tilde p$ |
| $N(U_{\tilde p}\tilde q)=N(\tilde p)^2N(\tilde q)$ | the norm identity |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product and the square.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm, the trace and the inverse.
- *The Specificities of the Symmetric Plain Algebra*, for the same objects read as the block's properties.
- *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, for the operator whose square and cube enter the representation.
- *Jordan Algebras*, for the Peirce decomposition and the cubic identity.
- *The Two General Products of an Algebra with Involution*, for the degree-two Common Theory specialised here.
