# __Remarkable Subspaces and the Two Algebraic Norms__

## Introduction

The two algebraic norms of *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, the plain norm $\langle\tilde p\rangle=p_0^2-\lvert\vec p\rvert^2$ and the quaternion norm $\langle\tilde p\rangle_{\natural}=p_0^2+\lvert\vec p\rvert^2$, are read here on the two **remarkable subspaces** of the quaternion space, the scalar line $\mathbb{R}_{\mathbb{H}}=\{p_0e_0\}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})=\{\vec p\}$, the fixed and the anti-fixed space of the quaternion conjugation. On the scalar line the two norms **coincide** and are nonnegative; on the vector subspace they **differ by sign**, the plain norm being nonpositive and the quaternion norm nonnegative. The two subspaces split the whole space for both associated forms, and the **signature table** of the forms the two norms define is $(1,3)$ for the plain norm and $(4,0)$ for the quaternion norm.

The norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, the article preceding this one; the subspaces are *Introduction to the Remarkable Subspaces of the Quaternions*, in the Linear Spaces group above; the forms on the same subspaces are *Remarkable Subspaces and the Two Forms*, the article preceding this one; and the comparison is *Remarkable Subspaces and the Four Algebraic Norms*.

**Conventions.** Throughout, $\tilde p=p_0e_0+\vec p$ names an element, the scalar line has basis $e_0$ and the vector subspace has basis $e_1,e_2,e_3$, and the two norms are $\langle\tilde p\rangle$ and $\langle\tilde p\rangle_{\natural}$. The associated forms of the two norms are $\langle\tilde p,\tilde q\rangle=\mathrm{Sc}(\tilde p\tilde q)$ and $\langle\tilde p,\tilde q\rangle_{\natural}=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$, of signatures $(1,3)$ and $(4,0)$.

## The Two Norms on the Two Subspaces

**Proposition (the restrictions of the two norms).** On a scalar element $\tilde p=p_0e_0$,

$$
\langle\tilde p\rangle=p_0^2=\langle\tilde p\rangle_{\natural} ,
$$

the two norms coinciding and being the square of the scalar, a nonnegative real number. On a vector element $\tilde p=\vec p$,

$$
\langle\tilde p\rangle=-\lvert\vec p\rvert^2 , \qquad \langle\tilde p\rangle_{\natural}=+\lvert\vec p\rvert^2 ,
$$

the plain norm being the negative of $(\vec p,\vec p)$ and the quaternion norm the positive one; and the two agree on the vector subspace exactly at the origin.

*Proof.* A scalar element has $\vec p=0$, so $\langle\tilde p\rangle=p_0^2-0=p_0^2$ and $\langle\tilde p\rangle_{\natural}=p_0^2+0=p_0^2$. A vector element has $p_0=0$, so $\langle\tilde p\rangle=0-\lvert\vec p\rvert^2=-\lvert\vec p\rvert^2$ and $\langle\tilde p\rangle_{\natural}=0+\lvert\vec p\rvert^2=+\lvert\vec p\rvert^2$.

So the two norms are **equal on the scalar line** and **opposite on the vector subspace**: the plain norm is the square of the scalar on the fixed space and the negative $(\vec p,\vec p)$ on the anti-fixed space, and the quaternion norm is the positive $(\vec p,\vec p)$ on both. The sign reversal of the plain norm is the sign reversal of the plain form on the two subspaces, and it is what makes the plain norm indefinite; the quaternion norm has no sign reversal, and it is what makes the quaternion norm positive definite.

## The Signature Table of the Forms the Norms Define

The form of a norm is the polarisation of its algebraic norm, and the two norms define the two forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*: the polarisation of the plain norm is the plain form, and the polarisation of the quaternion norm is the quaternion form. The signature table is therefore the table of the two forms on the two subspaces.

| subspace | the plain norm on an element | the quaternion norm on an element | $\langle\cdot,\cdot\rangle$-signature | $\langle\cdot,\cdot\rangle_{\natural}$-signature |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $p_0^2$, nonnegative | $p_0^2$, nonnegative | $(1,0)$ | $(1,0)$ |
| $\operatorname{Vect}(\mathbb{H})$ | $-\lvert\vec p\rvert^2$, nonpositive | $\lvert\vec p\rvert^2$, nonnegative | $(0,3)$ | $(3,0)$ |
| whole space | indefinite | positive definite | $(1,3)$ | $(4,0)$ |

The plain norm is **indefinite**, of the signature $(1,3)$ of its form: one positive direction, the scalar line, and three negative directions, the vector subspace. The quaternion norm is **positive definite**, of the signature $(4,0)$: four positive directions, the scalar line and the vector subspace together. The two norms give the two ends of the scale of the algebraic norm of a real symmetric bilinear form on the four coordinates, and the signature table here is the reading on the two subspaces of the signature rule of *Remarkable Subspaces and the Two Forms*, the article preceding this one.

## The Splitting of the Space

**Proposition (the splitting).** The two subspaces are orthogonal for both forms, so the space splits as the orthogonal sum

$$
\mathbb{H}=\mathbb{R}_{\mathbb{H}}\perp\operatorname{Vect}(\mathbb{H})
$$

for the polarised forms of both norms. For the plain norm the two summands carry opposite signs, the form being positive on the scalar line and negative on the vector subspace; for the quaternion norm the two summands carry the same sign, the form being positive on both, and **the whole space is definite**, every nonzero element having a positive value of the form.

*Proof.* The orthogonality of the two subspaces is *Remarkable Subspaces and the Two Forms*, the article preceding this one, for both forms; the signs are the restrictions computed in the table above; and the sum of two positive definite summands is positive definite, so the quaternion form has no isotropic direction on the whole space.

So the plain norm is the norm of a splitting of signature $(1,3)$, the scalar line positive and the vector subspace negative; the quaternion norm is the norm of a splitting of signature $(4,0)$, both summands positive. The whole space is orthogonal for the quaternion norm in the strong sense that no direction of the space is isotropic, and the splitting of the plain form is orthogonal with the sign reversal of the restricted forms.

## The Isotropic Cone of the Plain Norm

**Proposition (the vanishing of the plain norm).** The plain norm vanishes on the **isotropic cone** $p_0^2=\lvert\vec p\rvert^2$: a cone of **real dimension three**, consisting of the elements of $\mathbb{H}$ whose scalar coefficient has the same square as the vector part, with the elements $e_0\pm\hat u$, $(\hat u,\hat u)=1$, as its generators. Separately, the plain square $\tilde p\tilde p$, read as an element, vanishes only at the origin: $\tilde p\tilde p=0$ forces $\tilde p=0$, since $\mathbb{H}$ is a division algebra.

*Proof.* The scalar-valued statement is the vanishing of the plain form, computed in *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, the article preceding this one: a single homogeneous quadratic equation in four coordinates, hence a cone of real dimension three, generated by the elements with $p_0=\pm\lvert\vec p\rvert$ and $\vec p\neq0$. The element-valued statement is the division property: $\tilde p\tilde p=\langle\tilde p\rangle e_0+2p_0\vec p$ vanishes only when its two coefficients vanish, $\langle\tilde p\rangle=0$ and $p_0\vec p=0$, which together force $p_0^2=\lvert\vec p\rvert^2$ with $p_0\vec p=0$, hence $p_0=0$ or $\vec p=0$, hence $\tilde p=0$.

So the vanishing of the plain norm is the **isotropic cone** of real dimension three: the isotropic elements of the plain form, whose squares are the nonzero pure quaternions, and which are not zero divisors. The plain square $\tilde p\tilde p$ vanishes only at the origin.

## Summary

On the scalar line the two algebraic norms of the quaternion space coincide, both being the square of the scalar $p_0^2$; on the vector subspace they are opposite, the plain norm $-\lvert\vec p\rvert^2$ and the quaternion norm $+\lvert\vec p\rvert^2$. The forms the two norms define have the signatures $(1,3)$ for the plain norm, one positive direction on the scalar line and three negative on the vector subspace, and $(4,0)$ for the quaternion norm, four positive directions on the two subspaces together; the space splits as the orthogonal sum of the scalar line and the vector subspace for both forms, with a sign reversal for the plain norm and with the whole space definite for the quaternion norm.

The vanishing of the plain norm is the **isotropic cone** $p_0^2=\lvert\vec p\rvert^2$ of real dimension three, the cone of the elements whose square is pure; separately, the plain square $\tilde p\tilde p$ vanishes only at the origin, the plain algebra being a division algebra with no nonzero nilpotent. The quaternion norm vanishes only at the origin and has no isotropic direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle p_0e_0\rangle=\langle p_0e_0\rangle_{\natural}=p_0^2$ | the two norms coincide on the scalar line |
| $\langle\vec p\rangle=-\lvert\vec p\rvert^2$, $\langle\vec p\rangle_{\natural}=+\lvert\vec p\rvert^2$ | the two norms are opposite on the vector subspace |
| $(1,3)$; $(4,0)$ | the signatures of the two norms as forms |
| $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\perp\operatorname{Vect}(\mathbb{H})$ | the orthogonal splitting for both forms |
| $p_0^2=\lvert\vec p\rvert^2$ | the isotropic cone of the plain form, real dimension three |
| $\tilde p\tilde p=0\iff\tilde p=0$ | the vanishing of the plain square as an element |
| $\langle\tilde p\rangle_{\natural}=0\iff\tilde p=0$ | the anisotropy of the quaternion norm |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the norm forms of the quaternion algebra and their restrictions to the scalar and vector parts.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, 3rd ed. 2002), for the index and the signature of a real quadratic form and its isotropic cone.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the squares of the quaternion elements and the nonzero roots of $-1$.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the division property, the absence of nonzero nilpotents and the invertibility criterion.
