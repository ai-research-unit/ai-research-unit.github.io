# __The Quaternion Form as a Product on the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic block is the place where a form and a product are the same object: the product is $N$ read on the scalar line, and the coefficient $N$ is recovered from the product by taking its scalar part. This article reads the form in that role.

**Boundaries.** The product and its scalar law are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the two forms of the space, with their signatures and their reciprocal relation under the conjugation, are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*; the norm and the invertibility criterion of the plain product are *Norm and Invertibility in the General Plain Algebra*; the zero divisors and the isotropic elements are *Zero Divisors of the Symmetric Quaternionic Algebra* and *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*, above this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_kq_ke_k$. The **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\mathbf q$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is

$$
N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q=\mathrm{Sc}\bigl(\tilde p^{\natural}\tilde q\bigr),
$$

the **plain form** is $B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p\tilde q)$, and the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$.

## The Form Read as a Product

**Proposition (the product is the form on the scalar line).** For all $\tilde p,\tilde q$,

$$
\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0,\qquad
N(\tilde p,\tilde q)=\mathrm{Sc}\bigl(\tilde p\star\tilde q\bigr).
$$

*Proof.* The first display is the governing formula of *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the second is its scalar part, since $\mathrm{Sc}(ae_0)=a$.

**Corollary (the form is the product).** The bilinear form $N$ and the operation $\star$ determine each other: the product is the form with values in the scalar line, and the form is the scalar part of the product. The block is the only structure of the six for which this dictionary holds, because it is the only one with central values.

*Proof.* The two displays are inverse readings; the uniqueness is the isolation theorem of *The Specificities of the Symmetric Quaternionic Algebra*.

**Remark (the values of the form and the values of the product).** The form is scalar valued by definition; the product takes its values on the scalar line. The two are the same datum, and the article writes $N$ for the pairing of elements and $\star$ for the multiplication, without ever needing a third symbol.

## The Gram Matrix

**Theorem (the Gram matrix is the identity).** In the basis $e_0,e_1,e_2,e_3$ of $\mathbb{H}$,

$$
N(e_\mu,e_\nu)=\delta_{\mu\nu},\qquad
\mathrm{Gram}(N)=I_4 .
$$

*Proof.* In the coordinate basis the two elements $e_\mu,e_\nu$ have the standard coordinate vectors, and $N$ is the standard positive definite pairing of those coordinates, so $N(e_\mu,e_\nu)=\delta_{\mu\nu}$; the matrix is the identity.

**Corollary (rank, non-degeneracy and the identification of the coordinates).** The form has rank $4$, is non-degenerate, and reads $\tilde q=(q_0,q_1,q_2,q_3)$ as the coordinates of the element in the basis; the radical $\operatorname{rad}(N)$ is $\{0\}$.

*Proof.* An identity Gram matrix is invertible, so the form is non-degenerate and its rank is $4$; the radical of a non-degenerate form is $\{0\}$, which is the computation of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*.

This is why the radical is $\{0\}$ in both blocks and why the isotropic sets differ so sharply.

## The Polarisation and the Quadratic Form

**Theorem (the polarisation).** For all $\tilde p,\tilde q$,

$$
2N(\tilde p,\tilde q)=N(\tilde p+\tilde q)-N(\tilde p)-N(\tilde q),
\qquad
N(\tilde p,\tilde q)=\tfrac12\bigl(N(\tilde p+\tilde q)-N(\tilde p)-N(\tilde q)\bigr),
$$

where $N(\tilde x)=N(\tilde x,\tilde x)$ is the **quadratic form** of the block:

$$
N(\tilde x)=N(\tilde x,\tilde x)=x_0^{2}+x_1^{2}+x_2^{2}+x_3^{2}.
$$

*Proof.* The form is $\mathbb{R}$-bilinear and symmetric, so $N(\tilde p+\tilde q)=N(\tilde p)+2N(\tilde p,\tilde q)+N(\tilde q)$; the display is the rearrangement. The quadratic form is the form on the diagonal.

**Corollary (the quadratic form determines the form and the product).** The quadratic form $N(\tilde x)$ and the bilinear form $N(\tilde p,\tilde q)$ determine each other by the polarisation, and hence determine the product by $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$.

*Proof.* The polarisation recovers $N(\tilde p,\tilde q)$ from the values of $N$ on the diagonal, and the product is the bilinear form on the scalar line.

## The Positive Definiteness

**Theorem (definiteness, signature and inertia).** The form $N$ is positive definite; its signature is $(4,0)$, its inertia is $(4,0,0)$, and it is anisotropic. In coordinates it is the standard positive definite form of $\mathbb{R}^4$.

*Proof.* $N(\tilde x)=x_0^{2}+x_1^{2}+x_2^{2}+x_3^{2}$ is a sum of four squares, nonnegative and vanishing only at the origin; all four eigenvalues of the Gram matrix $I_4$ are $+1$.

**Corollary (the inequality and the equality case).** For all $\tilde p,\tilde q$,

$$
N(\tilde p,\tilde q)^{2}\leq N(\tilde p)\,N(\tilde q),
$$

with equality exactly when $\tilde p,\tilde q$ are proportional.

*Proof.* This is the standard inequality of a positive definite bilinear form, stated in *The 2 Forms over the Quaternion $\mathbb{R}$ Space* for this form and its companion.

**Remark (the definite coefficient against the indefinite companion).** The block's coefficient is definite and the plain form $B$ of the same space is indefinite of signature $(1,3)$; the two are exchanged by the conjugation, $N(\tilde p,\tilde q)=B(\tilde p,\tilde q^{\natural})$, as *Zero Divisors of the Symmetric Quaternionic Algebra* records. The definiteness of $N$ is the single property from which the block's empty isotropic set, its negative-free squares and its trivial radical all follow.

## The Reconstruction of the Form from the Product

**Theorem (the reconstruction, in three readings).** The form is recovered from the product by any of the three readings

$$
N(\tilde p,\tilde q)=\mathrm{Sc}\bigl(\tilde p\star\tilde q\bigr)
=\tfrac12\,\mathrm{Sc}\bigl((\tilde p+\tilde q)\star(\tilde p+\tilde q)-\tilde p\star\tilde p-\tilde q\star\tilde q\bigr)
=\tfrac14\,\mathrm{Sc}\bigl((\tilde p+\tilde q)\star(\tilde p+\tilde q)-(\tilde p-\tilde q)\star(\tilde p-\tilde q)\bigr),
$$

and the product is recovered from the form by $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$.

*Proof.* The first reading is the scalar part of the product; the second is the polarisation written through the square $\tilde x\star\tilde x=N(\tilde x)e_0$; the third is the difference of the squares of the sum and the difference, which by bilinearity is $4N(\tilde p,\tilde q)e_0$, and the scalar part gives the display. The converse reading is the governing formula.

**Corollary (the product is the polarisation on the diagonal and the form off it).** On the diagonal the product is the quadratic form, $\tilde x\star\tilde x=N(\tilde x)e_0$; off the diagonal it is the polarisation, $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. There is no information in the block beyond the four coordinates and the form.

*Proof.* The two clauses are the two readings of the theorem.

## Summary

The symmetric quaternionic block is the form $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$ read on the scalar line, $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$, and the form is the scalar part of the product. Its Gram matrix in the basis is the identity $I_4$, so it is non-degenerate of rank $4$ with radical $\{0\}$; its quadratic form is $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}$, positive definite of signature $(4,0)$ and inertia $(4,0,0)$, anisotropic, with the inequality $N(\tilde p,\tilde q)^{2}\leq N(\tilde p)N(\tilde q)$. The form determines the product and the product determines the form, through the scalar part and the polarisation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$ | the quaternion form, the coefficient of the product |
| $B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p\tilde q)$ | the plain form, indefinite of signature $(1,3)$ |
| $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}$ | the quadratic form, positive definite of signature $(4,0)$ |
| $I_4$ | the Gram matrix $N(e_\mu,e_\nu)=\delta_{\mu\nu}$ |
| $\operatorname{rad}(N)=\{0\}$ | the radical of the non-degenerate form |
| $2N(\tilde p,\tilde q)=N(\tilde p+\tilde q)-N(\tilde p)-N(\tilde q)$ | the polarisation |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the product
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the two forms, their signatures and their relation under the conjugation
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the radical and the isotropy of the coefficient
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the bridge $N(\tilde p,\tilde q)=B(\tilde p,\tilde q^{\natural})$ and the zero-divisor criterion
