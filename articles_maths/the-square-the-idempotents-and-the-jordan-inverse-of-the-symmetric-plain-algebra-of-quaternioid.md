# __The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ of *Introduction to the Symmetric Plain Algebra*. It is the specialisation of the degree-two Common Theory of *The Two General Products of an Algebra with Involution* to the real quaternions.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

## The Square Map

**Definition.** The **square map** of the block is

$$
Q:\tilde q\mapsto\tilde q\bullet\tilde q=\tilde q^2,\qquad
\mathfrak{Q}(\tilde q)=\bigl(q_t^2-|\vec q|^2\bigr)e_t+2q_t\vec q .
$$

It is the diagonal of the product; the polarisation $\mathfrak{Q}(\tilde q_1,\tilde q_2)=\tfrac12\bigl(\mathfrak{Q}(\tilde q_1+\tilde q_2)-\mathfrak{Q}(\tilde q_1)-\mathfrak{Q}(\tilde q_2)\bigr)$ is the product, $\mathfrak{Q}(\tilde q_1,\tilde q_2)=\tilde q_1\bullet\tilde q_2$.

**Proposition (the relation to the norm).** The square, the trace and the norm are tied by

$$
\mathrm{Sc}\,\tilde q^2=q_t^2-|\vec q|^2=2q_t^2-\langle\tilde q\rangle_{\natural},\qquad
\langle\tilde q\rangle_{\natural}=q_t^{\,2}+|\vec q|^{\,2},
$$

and by the quadratic identity $\tilde q^2-T(\tilde q)\tilde q+\langle\tilde q\rangle_{\natural}e_t=0$. The square of the block is the **plain square**; it is **not** the quaternionic square, whose value is the central element $\tilde q^{\natural}\tilde q=\langle\tilde q\rangle_{\natural}e_t$, and the two agree only on the scalar line.

*Proof.* The square is displayed above; the scalar part is $q_t^2-|\vec q|^2$, the vector part $2q_t\vec q$. The plain square is quoted from *Introduction to the Quaternion Algebra* and the quaternionic square from *Introduction to the General Quaternionic Algebra*, below this article in this category; the quadratic identity is *Norm and Invertibility in the Symmetric Plain Algebra*.

**Remark (the two general products on one square).** The chapter carries two general products, the plain product $\tilde q_1\tilde q_2$ and the quaternionic product $\tilde q_1^{\natural}\tilde q_2$; the square of the block is the square of the first, and the symmetrisation of the second, *The Symmetrised Quaternionic Product and the Hermitian Subspace*, below this article in this category, has the central square $\langle\tilde q\rangle_{\natural}e_t$. **The division of the real chapter is between these two squares**, and the block's square is the non-central one.

## The Idempotents and Their Degeneracy

**Definition.** An **idempotent** of the block is an element with $\tilde\pi\bullet\tilde\pi=\tilde\pi$.

**Theorem.** The idempotents of the block are exactly

$$
\boxed{\;\tilde\pi\in\{0,\ e_t\}\;},
$$

the two trivial idempotents; there is no nontrivial one.

*Proof.* The square is the plain square, so the equation is $\tilde\pi^2=\tilde\pi$. The vector part gives $(2\pi_t-1)\vec\pi=0$, so either $\vec\pi=0$ and the scalar part gives $\pi_t^2=\pi_t$, giving $\tilde\pi\in\{0,e_t\}$, or $\pi_t=\tfrac12$ and the scalar part gives $|\vec\pi|^2=-\tfrac14$, with no real solution.

**Remark (the degeneracy in a division algebra).** A nontrivial idempotent is built, in a split algebra, from a pure root of $+e_t$ by $\tilde\pi=\tfrac12(e_t+\vec q_a)$, and the reason the construction fails here is that **the pure square is negative**: $\vec q_a\bullet\vec q_a=-|\vec q_a|^2e_t$, so a pure element can be a root of $-e_t$ but never a root of $+e_t$. Over a division algebra with a negative definite pure part the construction never closes, and the idempotent class collapses to the two trivial elements; the collapse is the algebraic form of the absence of the split.

**Corollary (the associated idempotents).** The only idempotents associated with the zero divisors are the trivial ones: a nonzero pure element $\vec q_a$ is a zero divisor but the element $\tfrac12(e_t+\vec q_a)$ has square $\tfrac14(1-|\vec q_a|^2)e_t+\tfrac12\vec q_a$, which is not an idempotent for any real $\vec q_a$.

## The Peirce Decomposition

**Theorem (the cubic identity).** The multiplication operator satisfies the cubic Peirce identity

$$
\boxed{\;2\,(L^{\bullet}_{\tilde\pi})^3-3\,(L^{\bullet}_{\tilde\pi})^2+L^{\bullet}_{\tilde\pi}=0\;}
$$

at every idempotent $\tilde\pi$, so the spectrum is contained in $\{0,\tfrac12,1\}$.

*Proof.* The identity holds in every Jordan algebra for an idempotent, by the Peirce theory of *Jordan Algebras*; in the block it is checked directly from $L^{\bullet}_{e_t}=\mathrm{id}$ and $L^{\bullet}_{0}=0$.

**Theorem (the Peirce decomposition).** For the two idempotents the decomposition is trivial:

$$
J_1(e_t)=\mathbb{H},\quad J_{1/2}(e_t)=J_0(e_t)=0;
\qquad
J_0(0)=\mathbb{H},\quad J_1(0)=J_{1/2}(0)=0,
$$

where $J_\lambda(\tilde\pi)=\{\tilde q : \tilde\pi\bullet\tilde q=\lambda\tilde q\}$.

*Proof.* $L^{\bullet}_{e_t}=\mathrm{id}$ has the single eigenvalue $1$ with multiplicity four; $L^{\bullet}_{0}=0$ has the single eigenvalue $0$ with multiplicity four.

**Remark (the would-be shape).** A nontrivial idempotent of a degree-two block of this kind would split the algebra into three Peirce spaces of dimensions $1,2,1$; since the block has only $0$ and $e_t$, **the middle space never opens and the Peirce calculus is degenerate.** This is the specific-theory reading of the degeneracy of the previous section, and it is the reason the block carries no projector calculus.

## The Jordan Inverse

**Theorem.** An element is invertible exactly when $\langle\tilde q\rangle_{\natural}\neq0$, that is, when $\tilde q\neq0$, and the inverse is

$$
\boxed{\;\tilde q^{-1}=\frac{T(\tilde q)e_t-\tilde q}{\langle\tilde q\rangle_{\natural}}=\frac{2q_te_t-\tilde q}{\langle\tilde q\rangle_{\natural}}=\frac{\tilde q^{\natural}}{\langle\tilde q\rangle_{\natural}}\;}.
$$

*Proof.* This is *Norm and Invertibility in the Symmetric Plain Algebra*; the inverse satisfies $\tilde q\bullet\tilde q^{-1}=e_t$ and $\tilde q^{\bullet2}\bullet\tilde q^{-1}=\tilde q$.

**Proposition (the two-sidedness and the failure of multiplicativity).** The inverse is two-sided and involutive, $(\tilde q^{-1})^{-1}=\tilde q$; but the inversion is not a homomorphism, and the invertible elements do not form a group, since $\vec e_x,\vec e_y$ are invertible and $\vec e_x\bullet \vec e_y=0$ has no inverse.

*Proof.* The two-sidedness is commutativity and the first defining equation; the failure of multiplicativity is the pair $\vec e_x,\vec e_y$.

## The Quadratic Representation

**Definition.** The **quadratic representation** of the block is

$$
U_{\tilde q_1}=2\,(L^{\bullet}_{\tilde q_1})^2-L^{\bullet}_{\tilde q_1^{\,\bullet2}},
\qquad
U_{\tilde q_1}(\tilde q_2)=2\,\tilde q_1\bullet(\tilde q_1\bullet\tilde q_2)-\tilde q_1^{\bullet2}\bullet\tilde q_2 .
$$

**Theorem.** The quadratic representation is the plain sandwich operator and it is multiplicative in the norm:

$$
\boxed{\;U_{\tilde q_1}(\tilde q_2)=\tilde q_1\,\tilde q_2\,\tilde q_1,\qquad
\langle U_{\tilde q_1}\tilde q_2\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}^2\langle\tilde q_2\rangle_{\natural}\;}.
$$

*Proof.* Expanding $U_{\tilde q_1}(\tilde q_2)$ in the symmetrised plain product, $U_{\tilde q_1}(\tilde q_2)=\tfrac12\bigl(\tilde q_1(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)+(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)\tilde q_1\bigr)-\tfrac12(\tilde q_1^2\tilde q_2+\tilde q_2\tilde q_1^2)=\tilde q_1\tilde q_2\tilde q_1$ by the associativity of the plain product. The norm identity is the multiplicativity of $\langle\cdot\rangle_{\natural}$ applied twice, $\langle\tilde q_1\tilde q_2\tilde q_1\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}^2\langle\tilde q_2\rangle_{\natural}$.

**Remark (the effect on the norm).** For a nonzero $\tilde q$ the operator $U_{\tilde q}$ is invertible with inverse $U_{\tilde q^{-1}}$, and $U_{\tilde q^{-1}}=U_{\tilde q}^{-1}$; the norm identity is the degree-two form of the composite, and it is the quadratic representation statement of the degree-two Common Theory of *The Two General Products of an Algebra with Involution* read on the block.

## Summary

The square map of the block is the plain square, $\mathfrak{Q}(\tilde q)=(q_t^2-|\vec q|^2)e_t+2q_t\vec q$, polarising to the product, with the scalar part $2q_t^2-\langle\tilde q\rangle_{\natural}$ and the quadratic identity $\tilde q^2-T(\tilde q)\tilde q+\langle\tilde q\rangle_{\natural}e_t=0$. The idempotents are exactly $0$ and $e_t$, because a nontrivial idempotent would need a pure root of $+e_t$ and the pure square is $-|\vec q_a|^2e_t$; the Peirce decomposition is trivial, $J_1(e_t)=\mathbb{H}$ and $J_0(0)=\mathbb{H}$ with the other spaces vanishing. The Jordan inverse is $\tilde q^{-1}=(T(\tilde q)e_t-\tilde q)/\langle\tilde q\rangle_{\natural}=\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$ for $\tilde q\neq0$, two-sided and involutive but not multiplicative, and the invertible elements do not form a group. The quadratic representation is $U_{\tilde q_1}=2(L^{\bullet}_{\tilde q_1})^2-L^{\bullet}_{\tilde q_1^{\,\bullet2}}$, equal to the sandwich $\tilde q_1\tilde q_2\tilde q_1$, and $\langle U_{\tilde q_1}\tilde q_2\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}^2\langle\tilde q_2\rangle_{\natural}$. Everything but the idempotents and the Peirce decomposition has the same shape over $\mathbb{C}$; there the idempotents are many and the Peirce calculus opens.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{Q}(\tilde q)=\tilde q\bullet\tilde q=\tilde q^2$ | the square map |
| $\vec q_a\bullet\vec q_a=-\lvert\vec q_a\rvert^2e_t$ | the square of a pure element |
| $\{0,e_t\}$ | the idempotents |
| $J_\lambda(\tilde\pi)$ | the Peirce spaces, trivial at $0$ and $e_t$ |
| $\tilde q^{-1}=\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$ | the Jordan inverse |
| $U_{\tilde q_1}=2(L^{\bullet}_{\tilde q_1})^2-L^{\bullet}_{\tilde q_1^{\,\bullet2}}$ | the quadratic representation, $=\tilde q_1\tilde q_2\tilde q_1$ |
| $\langle U_{\tilde q_1}\tilde q_2\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}^2\langle\tilde q_2\rangle_{\natural}$ | the norm identity |

## Further Reading

- [Introduction to the Symmetric Plain Algebra](introduction-to-the-symmetric-plain-algebra-of-quaternioid.html), for the product and the square.
- [Norm and Invertibility in the Symmetric Plain Algebra](norm-and-invertibility-in-the-symmetric-plain-algebra.html), for the norm, the trace and the inverse.
- [The Specificities of the Symmetric Plain Algebra](the-specificities-of-the-symmetric-plain-algebra-of-quaternioid.html), for the same objects read as the block's properties.
- [The Multiplication Operators of the Symmetric Plain Algebra](the-multiplication-operators-of-the-symmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the operator whose square and cube enter the representation.
- [Jordan Algebras](jordan-algebras.html), for the Peirce decomposition and the cubic identity.
- *The Two General Products of an Algebra with Involution*, for the degree-two Common Theory specialised here.
