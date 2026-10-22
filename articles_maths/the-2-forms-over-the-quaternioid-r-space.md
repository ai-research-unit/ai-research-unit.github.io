# __The 2 Forms over the Quaternioid $\mathbb{R}$ Space__

## Introduction

The quaternion space carries two **bilinear forms**, read off the two general products of *The Two General Products of the Quaternioid $\mathbb{R}$ Space* by the scalar part:

$$
\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr) , \qquad \langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde q_1^{\natural}\tilde q_2\bigr) .
$$

The **plain form** $\langle\cdot,\cdot\rangle$ and the **quaternion form** $\langle\cdot,\cdot\rangle_{\natural}$ are the scalar parts of the plain product and of the quaternionic product, and on the coordinates they are $\langle\tilde q_1,\tilde q_2\rangle=q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ and $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=q_{1t}q_{2t}+(\vec q_1,\vec q_2)$. The two forms are symmetric and $\mathbb{R}$-bilinear, both are nondegenerate, and they differ in **signature**: $\langle\cdot,\cdot\rangle$ has signature $(1,3)$, the form of the quaternion coordinates, and $\langle\cdot,\cdot\rangle_{\natural}$ is positive definite with the identity Gram matrix.

**Conventions.** Throughout, $\tilde q_1=q_{1t}e_t+\vec q_1$ and $\tilde q_2=q_{2t}e_t+\vec q_2$ name elements, $(\vec q_1,\vec q_2)=\sum_kq_{1k}q_{2k}$ is the dot product of the vector parts, $\mathrm{Sc}$ is the scalar part, $\tilde q^{\natural}=q_te_t-\vec q$ is the quaternion conjugation, and $\langle\tilde q\rangle_{\natural}=\lvert\tilde q\rvert^2=\tilde q^{\natural}\tilde q$ is the quaternion norm of the element. The unit basis is $e_t,\vec e_x,\vec e_y,\vec e_z$.

## The Two Forms

**Definition.** The **plain form** and the **quaternion form** are the scalar parts

$$
\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr) , \qquad \langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde q_1^{\natural}\tilde q_2\bigr) ,
$$

and on the coordinates

$$
\langle\tilde q_1,\tilde q_2\rangle=q_{1t}q_{2t}-(\vec q_1,\vec q_2) , \qquad \langle\tilde q_1,\tilde q_2\rangle_{\natural}=q_{1t}q_{2t}+(\vec q_1,\vec q_2) .
$$

Both are symmetric and $\mathbb{R}$-bilinear. They differ by twice the dot product of the vector parts,

$$
\langle\tilde q_1,\tilde q_2\rangle_{\natural}-\langle\tilde q_1,\tilde q_2\rangle=2(\vec q_1,\vec q_2) , \qquad \langle\tilde q_1,\tilde q_2\rangle_{\natural}+\langle\tilde q_1,\tilde q_2\rangle=2q_{1t}q_{2t} ,
$$

so the sum of the two forms separates the scalar parts of the two elements and their difference the vector parts. The two are the two **scalar products of the two products**: $\langle\cdot,\cdot\rangle$ is the scalar part of the plain product, read in *Comparison Between the Two General Products*, and $\langle\cdot,\cdot\rangle_{\natural}$ is the scalar part of the quaternionic product, read in *Relations Between the Two General Products*; the two forms are therefore the two scalar parts of the two products, and no third scalar part is available over $\mathbb{R}$.

## The Gram Matrices

**Proposition (the Gram matrices).** In the unit basis $e_t,\vec e_x,\vec e_y,\vec e_z$,

$$
\operatorname{Gram}(B)=\operatorname{diag}(1,-1,-1,-1) , \qquad \operatorname{Gram}(N)=I_4 .
$$

The plain form has signature $(1,3)$, one positive and three negative squares; the quaternion form has signature $(4,0)$, being positive definite, and its Gram matrix is the identity.

*Proof.* On the units, $\langle e_t,e_t\rangle=1$ and $\langle \vec e_k,\vec e_k\rangle=-1$ for $k=1,2,3$, by the value $q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ on a basis pair; the off-diagonal entries vanish, the units being mutually perpendicular. Similarly $\langle \vec e_k,\vec e_k\rangle_{\natural}=1$ for every $k$ and the off-diagonal entries vanish.

So the two forms are the two standard forms on the coordinates: $\langle\cdot,\cdot\rangle$ is the form of signature $(1,3)$ and $\langle\cdot,\cdot\rangle_{\natural}$ the positive definite form of signature $(4,0)$. They are the two ends of the scale of the **index** of a symmetric bilinear form on a real four-dimensional space, $\langle\cdot,\cdot\rangle$ of maximal index three and $\langle\cdot,\cdot\rangle_{\natural}$ of minimal index zero, the forms of the two intermediate signatures $(3,1)$ and $(2,2)$ lying strictly between.

## The Polarisation and the Quadratic Forms

**Definition.** The **associated quadratic forms** of the two forms are the values at the two equal arguments

$$
Q_B(\tilde q)=\langle\tilde q,\tilde q\rangle=\mathrm{Sc}\bigl(\tilde q^2\bigr)=q_t^2-\lvert\vec q\rvert^2 , \qquad Q_\langle\tilde q\rangle_{\natural}=\langle\tilde q,\tilde q\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde q^{\natural}\tilde q\bigr)=\lvert\tilde q\rvert^2 .
$$

The two quadratic forms are the algebraic norm of the plain form and the quaternion norm of the element, written $\langle\tilde q\rangle$ and $\langle\tilde q\rangle_{\natural}$ for short; $Q_B$ is indefinite and $Q_N$ is the square of the quaternion norm.

**Proposition (the polarisation).** The two forms are recovered from their quadratic forms by the polarisation identity

$$
f(\tilde q_1,\tilde q_2)=\tfrac12\bigl(Q_f(\tilde q_1+\tilde q_2)-Q_f(\tilde q_1)-Q_f(\tilde q_2)\bigr) ,
$$

and the values of the quadratic forms on the units are $Q_B(e_t)=1$, $Q_B(\vec e_k)=-1$ for $k\neq0$, and $Q_N(\vec e_k)=1$ for every $k$.

*Proof.* The polarisation identity holds for any symmetric bilinear form over a field of characteristic not two; expanding $Q_B(\tilde q_1+\tilde q_2)$ with the bilinearity gives $2\langle\tilde q_1,\tilde q_2\rangle$. The values on the units are those of the diagonal of the Gram matrices.

So each form is the polarised quadratic of its algebraic norm, and the quadratic forms are read on the units as the diagonal of the Gram matrices: $Q_B$ takes the value $1$ on the unit and $-1$ on each of the three imaginary units, while $Q_N$ takes the value $1$ on all four. The two quadratic forms are the *two algebraic norms* of the chapter, their level sets, their multiplicativity and the invertibility criteria they give being *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

## The Radical

**Proposition (both forms are nondegenerate).** The radical of each form, the set of elements orthogonal to the whole space, is $\{0\}$, so both forms are nondegenerate.

*Proof.* The radical of a form with Gram matrix $G$ in a basis is the kernel of $G$ acting on the coordinate column. The two Gram matrices are diagonal with nonzero diagonal entries $1,-1,-1,-1$ and $1,1,1,1$, so each has zero kernel and the radical is $\{0\}$.

So neither form has a nonzero annihilator, and the two are nondegenerate in the sense of the radical; the statement is the form-level version of the nondegeneracy of the two products, the radical of a product being $\{0\}$ in *Comparison Between the Two General Products*. A nondegenerate symmetric bilinear form over $\mathbb{R}$ identifies the space with its dual, and both forms do so, the plain form with the reversed sign on the vector part and the quaternion form directly.

## The Isotropic Elements

**Definition.** An element $\tilde q\neq0$ is **isotropic** for the form $f$ when $f(\tilde q,\tilde q)=0$; the set of isotropic elements is the **isotropic set** or **null set**, and the set of isotropic directions the isotropic cone.

**Proposition (the two null sets).** The quaternion form has no isotropic element, $Q_\langle\tilde q\rangle_{\natural}=\lvert\tilde q\rvert^2>0$ for $\tilde q\neq0$. The plain form has the isotropic elements $Q_B(\tilde q)=0$, that is $q_t^2=\lvert\vec q\rvert^2$: the cone of real dimension three consisting of the elements whose scalar coefficient has the same square as their vector part, with the two sheets $q_t=\pm\lvert\vec q\rvert$ meeting at the origin.

*Proof.* $Q_N$ is the sum of four squares, so it vanishes only at the origin. $Q_B(\tilde q)=q_t^2-\lvert\vec q\rvert^2$ vanishes exactly when $q_t^2=\lvert\vec q\rvert^2$, a single homogeneous quadratic equation in the four coordinates, hence a cone of real dimension three; it contains the elements $e_t\pm \vec e_x$, whose scalar coefficient has the same square as the vector part, and it is not a subspace, a sum of two isotropic elements being isotropic only when they are proportional.

So the plain form is indefinite and its null set is the cone of the quaternion coordinates, of real dimension three; the quaternion form is definite and its null set is the origin alone. An isotropic element $\tilde q$ has $\langle\tilde q,\tilde q\rangle=0$, so its square $\tilde q^2=\langle\tilde q\rangle e_t+2q_t\vec q=2q_t\vec q$ is pure; the isotropic elements are the elements whose square is pure, and they are **not** square-zero and **not** zero divisors, since $\mathbb{H}$ is a division algebra in which $\tilde q^2=0$ forces $\tilde q=0$.

## Summary

The quaternion space carries two bilinear forms, the plain form $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)=q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ and the quaternion form $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=q_{1t}q_{2t}+(\vec q_1,\vec q_2)$, both symmetric and nondegenerate, differing by twice the dot product of the vector parts. Their Gram matrices in the unit basis are $\operatorname{diag}(1,-1,-1,-1)$, of signature $(1,3)$, and $I_4$, of signature $(4,0)$; their associated quadratic forms are $Q_B(\tilde q)=q_t^2-\lvert\vec q\rvert^2$, indefinite, and $Q_\langle\tilde q\rangle_{\natural}=\lvert\vec q\rvert^2$, positive definite; and each form is recovered from its quadratic form by polarisation.

The plain form has the isotropic cone $q_t^2=\lvert\vec q\rvert^2$, of real dimension three, and the quaternion form has no isotropic element. Both radicals are $\{0\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)=q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ | the plain form, signature $(1,3)$ |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ | the quaternion form, signature $(4,0)$ |
| $\operatorname{Gram}(B)=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of the plain form |
| $\operatorname{Gram}(N)=I_4$ | the Gram matrix of the quaternion form |
| $Q_B(\tilde q)=q_t^2-\lvert\vec q\rvert^2$, $Q_\langle\tilde q\rangle_{\natural}=\lvert\vec q\rvert^2$ | the two quadratic forms |
| $f(\tilde q_1,\tilde q_2)=\tfrac12(Q_f(\tilde q_1+\tilde q_2)-Q_f(\tilde q_1)-Q_f(\tilde q_2))$ | the polarisation identity |
| $Q_B(\tilde q)=0$: $q_t^2=\lvert\vec q\rvert^2$ | the isotropic cone of the plain form |
| $Q_\langle\tilde q\rangle_{\natural}>0$ for $\tilde q\neq0$ | the anisotropy of the quaternion form |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the two scalar products of the quaternion algebra and their signatures.
- Theodore Shifrin, *Abstract Algebra: A Geometric Approach* (Prentice Hall, 1996), for bilinear forms, their Gram matrices, their signatures and their polarisation.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, 3rd ed. 2002), for symmetric bilinear forms, nondegeneracy, the radical and the isotropic cone.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the trace form and the norm form of the quaternion algebra.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the trace of an element and its polarisation.
