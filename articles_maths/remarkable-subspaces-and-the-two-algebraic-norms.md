# __Remarkable Subspaces and the Two Algebraic Norms__

## Introduction

The two algebraic norms of *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, the plain norm $\langle\tilde q\rangle=q_t^2-\lvert\vec q\rvert^2$ and the quaternion norm $\langle\tilde q\rangle_{\natural}=q_t^2+\lvert\vec q\rvert^2$, are read here on the two **remarkable subspaces** of the quaternion space, the scalar line $\mathbb{R}_{\mathbb{H}}=\{q_te_t\}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})=\{\vec q\}$, the fixed and the anti-fixed space of the quaternion conjugation. On the scalar line the two norms **coincide** and are nonnegative; on the vector subspace they **differ by sign**, the plain norm being nonpositive and the quaternion norm nonnegative. The two subspaces split the whole space for both associated forms, and the **signature table** of the forms the two norms define is $(1,3)$ for the plain norm and $(4,0)$ for the quaternion norm.

The norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, the article preceding this one; the subspaces are *Introduction to the Remarkable Subspaces of the Quaternions*, in the Linear Spaces group above; the forms on the same subspaces are *Remarkable Subspaces and the Two Forms*, the article preceding this one; and the comparison is *Remarkable Subspaces and the Four Algebraic Norms*.

**Conventions.** Throughout, $\tilde q=q_te_t+\vec q$ names an element, the scalar line has basis $e_t$ and the vector subspace has basis $\vec e_x,\vec e_y,\vec e_z$, and the two norms are $\langle\tilde q\rangle$ and $\langle\tilde q\rangle_{\natural}$. The associated forms of the two norms are $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ and $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)$, of signatures $(1,3)$ and $(4,0)$.

## The Two Norms on the Two Subspaces

**Proposition (the restrictions of the two norms).** On a scalar element $\tilde q=q_te_t$,

$$
\langle\tilde q\rangle=q_t^2=\langle\tilde q\rangle_{\natural} ,
$$

the two norms coinciding and being the square of the scalar, a nonnegative real number. On a vector element $\tilde q=\vec q$,

$$
\langle\tilde q\rangle=-\lvert\vec q\rvert^2 , \qquad \langle\tilde q\rangle_{\natural}=+\lvert\vec q\rvert^2 ,
$$

the plain norm being the negative of $(\vec q,\vec q)$ and the quaternion norm the positive one; and the two agree on the vector subspace exactly at the origin.

*Proof.* A scalar element has $\vec q=0$, so $\langle\tilde q\rangle=q_t^2-0=q_t^2$ and $\langle\tilde q\rangle_{\natural}=q_t^2+0=q_t^2$. A vector element has $q_t=0$, so $\langle\tilde q\rangle=0-\lvert\vec q\rvert^2=-\lvert\vec q\rvert^2$ and $\langle\tilde q\rangle_{\natural}=0+\lvert\vec q\rvert^2=+\lvert\vec q\rvert^2$.

So the two norms are **equal on the scalar line** and **opposite on the vector subspace**: the plain norm is the square of the scalar on the fixed space and the negative $(\vec q,\vec q)$ on the anti-fixed space, and the quaternion norm is the positive $(\vec q,\vec q)$ on both. The sign reversal of the plain norm is the sign reversal of the plain form on the two subspaces, and it is what makes the plain norm indefinite; the quaternion norm has no sign reversal, and it is what makes the quaternion norm positive definite.

## The Signature Table of the Forms the Norms Define

The form of a norm is the polarisation of its algebraic norm, and the two norms define the two forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*: the polarisation of the plain norm is the plain form, and the polarisation of the quaternion norm is the quaternion form. The signature table is therefore the table of the two forms on the two subspaces.

| subspace | the plain norm on an element | the quaternion norm on an element | $\langle\cdot,\cdot\rangle$-signature | $\langle\cdot,\cdot\rangle_{\natural}$-signature |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $q_t^2$, nonnegative | $q_t^2$, nonnegative | $(1,0)$ | $(1,0)$ |
| $\operatorname{Vect}(\mathbb{H})$ | $-\lvert\vec q\rvert^2$, nonpositive | $\lvert\vec q\rvert^2$, nonnegative | $(0,3)$ | $(3,0)$ |
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

**Proposition (the vanishing of the plain norm).** The plain norm vanishes on the **isotropic cone** $q_t^2=\lvert\vec q\rvert^2$: a cone of **real dimension three**, consisting of the elements of $\mathbb{H}$ whose scalar coefficient has the same square as the vector part, with the elements $e_t\pm\hat u$, $(\hat u,\hat u)=1$, as its generators. Separately, the plain square $\tilde q\tilde q$, read as an element, vanishes only at the origin: $\tilde q\tilde q=0$ forces $\tilde q=0$, since $\mathbb{H}$ is a division algebra.

*Proof.* The scalar-valued statement is the vanishing of the plain form, computed in *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, the article preceding this one: a single homogeneous quadratic equation in four coordinates, hence a cone of real dimension three, generated by the elements with $q_t=\pm\lvert\vec q\rvert$ and $\vec q\neq0$. The element-valued statement is the division property: $\tilde q\tilde q=\langle\tilde q\rangle e_t+2q_t\vec q$ vanishes only when its two coefficients vanish, $\langle\tilde q\rangle=0$ and $q_t\vec q=0$, which together force $q_t^2=\lvert\vec q\rvert^2$ with $q_t\vec q=0$, hence $q_t=0$ or $\vec q=0$, hence $\tilde q=0$.

So the vanishing of the plain norm is the **isotropic cone** of real dimension three: the isotropic elements of the plain form, whose squares are the nonzero pure quaternions, and which are not zero divisors. The plain square $\tilde q\tilde q$ vanishes only at the origin.

## Summary

On the scalar line the two algebraic norms of the quaternion space coincide, both being the square of the scalar $q_t^2$; on the vector subspace they are opposite, the plain norm $-\lvert\vec q\rvert^2$ and the quaternion norm $+\lvert\vec q\rvert^2$. The forms the two norms define have the signatures $(1,3)$ for the plain norm, one positive direction on the scalar line and three negative on the vector subspace, and $(4,0)$ for the quaternion norm, four positive directions on the two subspaces together; the space splits as the orthogonal sum of the scalar line and the vector subspace for both forms, with a sign reversal for the plain norm and with the whole space definite for the quaternion norm.

The vanishing of the plain norm is the **isotropic cone** $q_t^2=\lvert\vec q\rvert^2$ of real dimension three, the cone of the elements whose square is pure; separately, the plain square $\tilde q\tilde q$ vanishes only at the origin, the plain algebra being a division algebra with no nonzero nilpotent. The quaternion norm vanishes only at the origin and has no isotropic direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle q_te_t\rangle=\langle q_te_t\rangle_{\natural}=q_t^2$ | the two norms coincide on the scalar line |
| $\langle\vec q\rangle=-\lvert\vec q\rvert^2$, $\langle\vec q\rangle_{\natural}=+\lvert\vec q\rvert^2$ | the two norms are opposite on the vector subspace |
| $(1,3)$; $(4,0)$ | the signatures of the two norms as forms |
| $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\perp\operatorname{Vect}(\mathbb{H})$ | the orthogonal splitting for both forms |
| $q_t^2=\lvert\vec q\rvert^2$ | the isotropic cone of the plain form, real dimension three |
| $\tilde q\tilde q=0\iff\tilde q=0$ | the vanishing of the plain square as an element |
| $\langle\tilde q\rangle_{\natural}=0\iff\tilde q=0$ | the anisotropy of the quaternion norm |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the norm forms of the quaternion algebra and their restrictions to the scalar and vector parts.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, 3rd ed. 2002), for the index and the signature of a real quadratic form and its isotropic cone.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the squares of the quaternion elements and the nonzero roots of $-1$.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the division property, the absence of nonzero nilpotents and the invertibility criterion.
