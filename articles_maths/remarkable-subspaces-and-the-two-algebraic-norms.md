# __Remarkable Subspaces and the Two Algebraic Norms__

## Introduction

The two algebraic norms of *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*, the plain norm $N_P(\tilde p)=\tilde p^2$ and the quaternion norm $N_Q(\tilde p)=\tilde p^{\natural}\tilde p=|\tilde p|^2e_0$, are read here on the two **remarkable subspaces** of the quaternion space, the scalar line $\mathbb{R}_{\mathbb{H}}=\{p_0e_0\}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})=\{\mathbf p\}$, the fixed and the anti-fixed space of the quaternion conjugation. On the scalar line the two norms **coincide** and are nonnegative; on the vector subspace they **differ by sign**, the plain norm being nonpositive and the quaternion norm nonnegative. The two subspaces split the whole space for both associated forms, and the **signature table** of the forms the two norms define is $(1,3)$ for the plain norm and $(4,0)$ for the quaternion norm.

The norms are *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*, the article preceding this one; the subspaces are *Introduction to the Remarkable Subspaces of the Quaternions*, in the Linear Spaces group above; the forms on the same subspaces are *Remarkable Subspaces and the Two Forms*, the article preceding this one; and the comparison is *Remarkable Subspaces and the Four Algebraic Norms*.

**Conventions.** Throughout, $\tilde p=p_0e_0+\mathbf p$ names an element, the scalar line has basis $e_0$ and the vector subspace has basis $e_1,e_2,e_3$, and the two norms are $N_P(\tilde p)=\tilde p^2$ and $N_Q(\tilde p)=\tilde p^{\natural}\tilde p$. The associated forms of the two norms are $B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ and $N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$, of signatures $(1,3)$ and $(4,0)$.

## The Two Norms on the Two Subspaces

**Proposition (the restrictions of the two norms).** On a scalar element $\tilde p=p_0e_0$,

$$
N_P(p_0e_0)=p_0^2e_0=N_Q(p_0e_0) ,
$$

the two norms coinciding and being the square of the scalar, a nonnegative real multiple of $e_0$. On a vector element $\tilde p=\mathbf p$,

$$
N_P(\mathbf p)=-\lvert\mathbf p\rvert^2e_0 , \qquad N_Q(\mathbf p)=+\lvert\mathbf p\rvert^2e_0 ,
$$

the plain norm being the negative of $(\mathbf p,\mathbf p)e_0$ and the quaternion norm the positive one; and the two agree on the vector subspace exactly at the origin.

*Proof.* A scalar element has $\mathbf p=0$, so $N_P(\tilde p)=(p_0^2-0)e_0+0=p_0^2e_0$ and $N_Q(\tilde p)=(p_0^2+0)e_0=p_0^2e_0$. A vector element has $p_0=0$, so $N_P(\tilde p)=(0-\lvert\mathbf p\rvert^2)e_0+0=-\lvert\mathbf p\rvert^2e_0$ and $N_Q(\tilde p)=(0+\lvert\mathbf p\rvert^2)e_0=+\lvert\mathbf p\rvert^2e_0$.

So the two norms are **equal on the scalar line** and **opposite on the vector subspace**: the plain norm is the square of the scalar on the fixed space and the negative $(\mathbf p,\mathbf p)e_0$ on the anti-fixed space, and the quaternion norm is the positive $(\mathbf p,\mathbf p)e_0$ on both. The sign reversal of the plain norm is the sign reversal of the plain form on the two subspaces, and it is what makes the plain norm indefinite; the quaternion norm has no sign reversal, and it is what makes the quaternion norm positive definite.

## The Signature Table of the Forms the Norms Define

The form of a norm is the polarisation of its algebraic norm, and the two norms define the two forms $B$ and $N$ of *The 2 Forms over the Quaternion $\mathbb{R}$ Space*: the polarisation of the plain norm is the plain form, and the polarisation of the quaternion norm is the quaternion form. The signature table is therefore the table of the two forms on the two subspaces.

| subspace | $N_P$ on an element | $N_Q$ on an element | $B$-signature | $N$-signature |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $p_0^2e_0$, nonnegative | $p_0^2e_0$, nonnegative | $(1,0)$ | $(1,0)$ |
| $\operatorname{Vect}(\mathbb{H})$ | $-\lvert\mathbf p\rvert^2e_0$, nonpositive | $\lvert\mathbf p\rvert^2e_0$, nonnegative | $(0,3)$ | $(3,0)$ |
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

**Proposition (the vanishing of the plain norm).** Read as the element $N_P(\tilde p)=\tilde p^2$, the plain norm vanishes only at the origin: $\tilde p^2=0$ forces $\tilde p=0$, since $\mathbb{H}$ is a division algebra, so the vanishing set of the plain norm is the origin of real dimension zero. Read as the scalar coefficient $\mathrm{Sc}(\tilde p^2)=B(\tilde p,\tilde p)$, the plain norm vanishes on the **isotropic cone** $p_0^2=\lvert\mathbf p\rvert^2$: a cone of **real dimension three**, consisting of the elements of $\mathbb{H}$ whose scalar coefficient has the same square as the vector part, with the elements $e_0\pm\hat{\mathbf u}$, $(\hat{\mathbf u},\hat{\mathbf u})=1$, as its generators.

*Proof.* The element-valued statement is the division property: $\tilde p^2=B(\tilde p)e_0+2p_0\mathbf p$ vanishes only when its two coefficients vanish, $B(\tilde p)=0$ and $p_0\mathbf p=0$, which together force $p_0^2=\lvert\mathbf p\rvert^2$ with $p_0\mathbf p=0$, hence $p_0=0$ or $\mathbf p=0$, hence $\tilde p=0$. The scalar-valued statement is the vanishing of the plain form, computed in *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, the article preceding this one: a single homogeneous quadratic equation in four coordinates, hence a cone of real dimension three, generated by the elements with $p_0=\pm\lvert\mathbf p\rvert$ and $\mathbf p\neq0$.

So the vanishing of the plain norm has two readings over $\mathbb{R}$. The **scalar-valued reading** gives the light cone of real dimension three: the isotropic elements of the plain form, whose squares are the nonzero pure quaternions, and which are not zero divisors.

## Summary

On the scalar line the two algebraic norms of the quaternion space coincide, both being the square of the scalar $p_0^2e_0$; on the vector subspace they are opposite, the plain norm $-\lvert\mathbf p\rvert^2e_0$ and the quaternion norm $+\lvert\mathbf p\rvert^2e_0$. The forms the two norms define have the signatures $(1,3)$ for the plain norm, one positive direction on the scalar line and three negative on the vector subspace, and $(4,0)$ for the quaternion norm, four positive directions on the two subspaces together; the space splits as the orthogonal sum of the scalar line and the vector subspace for both forms, with a sign reversal for the plain norm and with the whole space definite for the quaternion norm.

The vanishing of the plain norm has two readings: the element-valued reading gives the origin alone, the plain algebra being a division algebra with no nonzero nilpotent, and the scalar-valued reading gives the isotropic cone $p_0^2=\lvert\mathbf p\rvert^2$ of real dimension three, the cone of the elements whose square is pure. The quaternion norm vanishes only at the origin and has no isotropic direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N_P(p_0e_0)=N_Q(p_0e_0)=p_0^2e_0$ | the two norms coincide on the scalar line |
| $N_P(\mathbf p)=-\lvert\mathbf p\rvert^2e_0$, $N_Q(\mathbf p)=+\lvert\mathbf p\rvert^2e_0$ | the two norms are opposite on the vector subspace |
| $(1,3)$; $(4,0)$ | the signatures of the two norms as forms |
| $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\perp\operatorname{Vect}(\mathbb{H})$ | the orthogonal splitting for both forms |
| $p_0^2=\lvert\mathbf p\rvert^2$ | the isotropic cone of the plain form, real dimension three |
| $\tilde p^2=0\iff\tilde p=0$ | the vanishing of the plain norm as an element |
| $N_Q(\tilde p)=0\iff\tilde p=0$ | the anisotropy of the quaternion norm |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the norm forms of the quaternion algebra and their restrictions to the scalar and vector parts.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, 3rd ed. 2002), for the index and the signature of a real quadratic form and its isotropic cone.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the squares of the quaternion elements and the nonzero roots of $-1$.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the division property, the absence of nonzero nilpotents and the invertibility criterion.
