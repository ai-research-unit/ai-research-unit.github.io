# __The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic product is the pairing $N$ placed on the scalar line. This article reads the block through the two notions that read a pairing on its kernel: the **radical**, the set of elements annihilated by every element, and the **isotropic elements**, those annihilated by themselves.

**Placement.** This is the Specific Theory entry of the block. Its companion is *The Specificities of the Symmetric Quaternionic Algebra*, above this article in this category; the Common Theory slots it cites rather than restates are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, *Zero Divisors of the Symmetric Quaternionic Algebra*, *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*, all above this article in this category; its Operators companion is *The Multiplication Operators of the Symmetric Quaternionic Algebra*, below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$; an element is $\tilde q=q_te_t+\vec q$. The **quaternion conjugation** is $\tilde q^{\natural}=q_te_t-\vec q$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_t+\vec p\cdot\vec q$ and $N(\tilde q)=q_t^{2}+|\vec q|^{2}$; the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_t$.

## The Pairing with Values in the Centre

The block is commutative, so its left and right radicals coincide, and the radical of the *product* is the radical of its *coefficient*.

**Definition.** The **radical** of the block is

$$
\operatorname{Rad}(\star)=\{\tilde r:\tilde r\star\tilde q=0\text{ for every }\tilde q\}=\{\tilde r:N(\tilde r,\tilde q)=0\text{ for every }\tilde q\}=\operatorname{rad}(N).
$$

An element $\tilde x$ is **isotropic** when $\tilde x\star\tilde x=0$, that is when $N(\tilde x)=0$. The definitions are those of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* read for a commutative operation.

**Theorem (the radical is zero, by definiteness).**

$$
\operatorname{Rad}(\star)=\{0\}.
$$

*Proof.* Let $\tilde r\in\operatorname{Rad}(\star)$ and suppose $\tilde r\neq0$. Some coordinate $r_\mu$ of $\tilde r$ is nonzero. Take $\tilde q=e_\mu$; then $N(\tilde r,e_\mu)=r_\mu\neq0$, contradicting the defining property. So $\tilde r=0$, and $0$ is in the radical because $0\star\tilde q=0$ for every $\tilde q$. The form is non-degenerate, its Gram matrix in the basis being the identity.

**Corollary (the block is non-degenerate and anisotropic).** The coefficient form is positive definite, of Gram matrix $I_4$, of rank $4$ and nullity $0$; the block has no isotropic direction.

*Proof.* The Gram matrix is $N(e_\mu,e_\nu)=\delta_{\mu\nu}$, the identity; its rank is $4$ over $\mathbb{R}$, so the radical is $\{0\}$ by the theorem; and the form is positive definite, so it is anisotropic.

## The Isotropic Elements

**Theorem (the isotropic set is the origin).**

$$
\{\tilde x:\tilde x\star\tilde x=0\}=\{0\}.
$$

*Proof.* The square is $N(\tilde x)e_t=(x_0^{2}+|\vec x|^{2})e_t$, a sum of squares; it vanishes exactly when every coordinate of $\tilde x$ vanishes.

**Remark (isotropy and zero divisors are pulled apart).** In many products the isotropic set and the zero-divisor set agree up to the origin; here they are opposite extremes. The isotropic set is the single point $\{0\}$, because the coefficient is definite; the zero-divisor set is the whole punctured space $\mathbb{H}\setminus\{0\}$, because the vanishing of a product involves a *pair* of elements and not a single one (*Zero Divisors of the Symmetric Quaternionic Algebra*). The block is therefore anisotropic and, at the same time, has no regular element except $0$. Neither statement contradicts the other, and the two together are the specific feature of the block.

## The Positivity

**Theorem (the cone of squares is a half-line).** For every $\tilde x$ the square is a nonnegative multiple of $e_t$,

$$
\tilde x\star\tilde x=N(\tilde x)e_t,\qquad N(\tilde x)=x_0^{2}+|\vec x|^{2}\geq0,
$$

and the set of values $\tilde x\star\tilde x$ as $\tilde x$ ranges over the block is the closed half-line $\mathbb{R}_{\geq0}e_t$.

*Proof.* The square formula is the governing formula on the diagonal. The set of the numbers $N(\tilde x)$ is the set of the values of a positive definite quadratic form, namely $[0,\infty)$, attained at $\tilde x=\sqrt{t}e_t$ for the value $t$; so the cone of squares is $\mathbb{R}_{\geq0}e_t$.

**Corollary (no element is negative, and the shadow is one).** No element squares to a negative multiple of $e_t$; in particular $\tilde x\star\tilde x=-e_t$ has no solution. The block has no negative direction, and the diagonal of the multiplication is the half-line.

*Proof.* Immediate from the theorem; the emptiness of the root set of $-e_t$ is *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*.

## The Square Root of a Positive Element

**Proposition (the positive central elements are exactly the squares).** Let $\lambda e_t$ be a central element.

- for $\lambda>0$ it is a square, and its square roots are the level set $\{\tilde x:N(\tilde x)=\lambda\}$, the orbit of $\sqrt{\lambda}e_t$ under $Sp(1)$, of real dimension $3$;
- for $\lambda=0$ it is the square of $0$ alone;
- for $\lambda<0$ it is not a square.

*Proof.* The equation $\tilde x\star\tilde x=\lambda e_t$ is $N(\tilde x)=\lambda$, and the three cases are the sign of $\lambda$ read on the sum of squares; the orbit description is *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*.

**Remark (the square root of an element and the square root of a value).** Every element $\tilde x$ is a square root of the *positive central element* $\tilde x\star\tilde x=N(\tilde x)e_t$. The square roots of a noncentral argument are not posed in this block: the block's root theory is the theory of the central values, and a noncentral right-hand side is not a value of the product except when it is scalar, by the scalar law.

## Summary

The symmetric quaternionic block is non-degenerate and anisotropic: its coefficient is the positive definite quaternion form, of Gram matrix $I_4$, rank $4$ and nullity $0$, so the radical is $\{0\}$ and the isotropic set is the single point $\{0\}$. The cone of squares is the closed half-line $\mathbb{R}_{\geq0}e_t$, so the negative central element $-e_t$ has no square root, while every positive central element $\lambda e_t$ is a square with the level set $\{N=\lambda\}$ as its roots.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\operatorname{Rad}(\star)=\operatorname{rad}(N)$ | the radical; $\{0\}$ by definiteness |
| $\{\tilde x:\tilde x\star\tilde x=0\}=\{0\}$ | the isotropic elements |
| $N(\tilde x)=x_0^{2}+|\vec x|^{2}$ | the definite coefficient, Gram matrix $I_4$ |
| $\mathbb{R}_{\geq0}e_t$ | the cone of squares |
| $\{\tilde x:N(\tilde x)=\lambda\}$, $\lambda>0$ | the square roots of a positive central element |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the product and its governing formula
- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the radical and the isotropic element
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the Gram data, the signature and the isotropy of the two forms
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the maximal zero-divisor set that contrasts with the trivial isotropic set
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`) and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the root sets of the central values
