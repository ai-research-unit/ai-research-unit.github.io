# __$M_2(\mathbb{R})$ Model : Rank-One Matrices and the Null Cone__

## Introduction

The determinant of the model is the split-quaternion norm, so the singular matrices are exactly the zero divisors, and the rank of the matrix measures how far an element is from being a unit. In a $2\times2$ matrix the rank takes only the values two, one and zero, and the two non-generic strata are the zero divisors and the origin.

This article reads the three strata in the model. It proves that the zero divisors are the rank-one matrices, parametrises them as outer products $u v^{\mathsf T}$, separates the nilpotents from the scalar multiples of the idempotents, and computes the link of the null cone: under an orthogonal change of coordinates the cone is $\{|z_1|=|z_2|\}$ and its link in the Euclidean sphere is the Clifford torus.

The zero divisors themselves are *Split-Quaternion Zero Divisors*; the norm is *Split-Quaternion Norm and Invertibility*; the projective geometry of the cone is *Split-Quaternion Null Quadric and Projective Geometry*; the idempotents are *$M_2(\mathbb{R})$ Model : The Idempotents and the Peirce Decomposition*.

## The Determinant as a Quadratic Form

**Proposition (the norm is a quadratic form of signature $(2,2)$).** In the split-quaternion coordinates

$$
\det\mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural} = q_t^2+q_x^2-q_y^2-q_z^2,
$$

and the associated symmetric bilinear form is

$$
B(\tilde p,\tilde q) = \tfrac12\bigl(\langle\tilde p+\tilde q\rangle_{\natural}-\langle\tilde p\rangle_{\natural}-\langle\tilde q\rangle_{\natural}\bigr) = p_tq_t+p_xq_x-p_yq_y-p_zq_z.
$$

In the basis $1,\vec e_x,\vec e_y,\vec e_z$ its matrix is $\operatorname{diag}(1,1,-1,-1)$.

**Proof.** The determinant is computed in *Split-Quaternion Matrix Element Representations*, §*The Determinant and the Trace*. The polar form of a diagonal quadratic form is the diagonal bilinear form with the same signs.

**Corollary (the diagonalisation).** With the complex coordinates

$$
z_1 = q_t-iq_x, \qquad z_2 = q_y+iq_z,
$$

the norm reads

$$
\langle\tilde q\rangle_{\natural} = \lvert z_1\rvert^2-\lvert z_2\rvert^2,
$$

and the squared Frobenius norm of the matrix is $2(\lvert z_1\rvert^2+\lvert z_2\rvert^2)$.

**Proof.** Expand $\lvert z_1\rvert^2-\lvert z_2\rvert^2 = q_t^2+q_x^2-q_y^2-q_z^2$, and $\lvert z_1\rvert^2+\lvert z_2\rvert^2 = q_t^2+q_x^2+q_y^2+q_z^2$. The dictionary gives $a^2+b^2+c^2+d^2=2(q_t^2+q_x^2+q_y^2+q_z^2)$, which is twice the latter sum.

The two complex coordinates exhibit the norm as the difference of two positive definite Hermitian forms in two variables each. This is the split signature $(2,2)$: two positive directions and two negative ones, with no isotropic direction in the coordinate planes.

## The Three Strata

**Theorem (the rank stratification).** For a matrix $X=\mathsf{M}_2(\tilde q)$ the following are equivalent:

- $\operatorname{rank}X=2$;
- $\det X\neq0$;
- $X$ is invertible;
- $\tilde q$ is a unit.

The remaining non-zero matrices have rank one, and they are exactly the zero divisors. The zero matrix has rank zero.

**Proof.** A square matrix is invertible exactly when its determinant is non-zero, and the determinant is the norm; the invertibility criterion of *Split-Quaternion Norm and Invertibility* says that an element is a unit exactly when its norm is non-zero. A non-zero matrix which is not invertible has rank one.

**Proposition (the strata are the orbits).** The group $GL_2(\mathbb{R})$ acts transitively on the matrices of each rank, and the three orbits are the units, the non-zero zero divisors and the origin.

**Proof.** Two matrices of the same rank are equivalent under left and right multiplication by invertible matrices: this is the rank normal form. For rank one, $X=uv^{\mathsf T}$ with $u,v\neq0$, and $P X Q = (Pu)(Q^{\mathsf T}v)^{\mathsf T}$ is again of rank one.

**Corollary (the cone is smooth off the apex).** The zero-divisor set is the cone $\mathcal N=\{\det X=0\}$, a real cone of dimension three with apex at the origin, and it is a smooth hypersurface away from the apex.

**Proof.** The gradient of $\det$ at $X$ is the adjugate transposed. At a non-zero singular matrix the adjugate is non-zero, since $\operatorname{adj}X=0$ would make every $1\times1$ minor vanish and force $X=0$. So the gradient does not vanish on $\mathcal N\setminus\{0\}$.

## The Rank-One Parametrisation

**Theorem (the outer-product form).** Every rank-one matrix is

$$
X = uv^{\mathsf T}, \qquad u,v\in\mathbb{R}^2\setminus\{0\},
$$

and the pair $(u,v)$ is determined up to the scaling $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$.

**Proof.** A rank-one matrix has a one-dimensional image, spanned by some $u\neq0$, and its kernel is a line; a linear functional $v^{\mathsf T}$ with that kernel satisfies $X=uv^{\mathsf T}$ after the choice of $u$. If $u_1v_1^{\mathsf T}=u_2v_2^{\mathsf T}\neq0$ then $u_1$ and $u_2$ span the same line, so $u_2=\lambda u_1$, and then $v_2=\lambda^{-1}v_1$.

**Proposition (the square of a rank-one matrix).** For $X=uv^{\mathsf T}$,

$$
X^2 = (v^{\mathsf T}u)\,X.
$$

Consequently $X$ is nilpotent exactly when $v^{\mathsf T}u=0$, and $X$ is a non-zero scalar multiple of an idempotent exactly when $v^{\mathsf T}u\neq0$, the idempotent being $X/(v^{\mathsf T}u)$.

**Proof.** $X^2=u(v^{\mathsf T}u)v^{\mathsf T}=(v^{\mathsf T}u)uv^{\mathsf T}$. The two criteria follow, and in the second case $X/(v^{\mathsf T}u)$ has square itself.

**Corollary (the two families of the cone).** The zero divisors split into the nilpotents, the rank-one matrices with $v^{\mathsf T}u=0$, and the multiples of the idempotents, the rank-one matrices with $v^{\mathsf T}u\neq0$. The first family is a cone of dimension two and the second is the complement, a dense open subset of the cone of dimension three.

**Proof.** The condition $v^{\mathsf T}u=0$ is one scalar equation, so the nilpotents are codimension one in the cone. The complementary condition is open and dense.

**Example.** The matrix $X=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is $uv^{\mathsf T}$ with $u=v=(1,1)$, and $v^{\mathsf T}u=2$, so $X/2$ is the idempotent $\mathsf{M}_2(\tilde\pi_+)$. The matrix $Y=\begin{pmatrix}1&-1\\1&-1\end{pmatrix}$ is $uv^{\mathsf T}$ with $u=(1,1)$ and $v=(1,-1)$, and $v^{\mathsf T}u=0$, so $Y$ is nilpotent; it is $4\mathsf{M}_2(\tilde\pi_+E_{11}\tilde\pi_-)$ of the Peirce article.

## The Nilpotents

**Proposition (the nilpotents are the pure null elements).** An element $\tilde q$ satisfies $\tilde q^2=0$ exactly when

$$
q_t=0, \qquad q_x^2=q_y^2+q_z^2.
$$

**Proof.** Write $\tilde q=t+\vec v$. Then $\tilde q^2=t^2+N(\vec v)+2t\vec v$. Both parts must vanish; over $\mathbb{R}$, $2t\vec v=0$ gives $t=0$ or $\vec v=0$, and $\vec v=0$ with $t^2=0$ gives $t=0$. So $t=0$ and $N(\vec v)=0$, which is the displayed equation.

**Corollary (two nappes).** The non-zero nilpotents form the cone $q_x^2=q_y^2+q_z^2$ in the vector subspace $V$, of signature $(2,1)$. It has two connected components, the nappes $q_x>0$ and $q_x<0$, each homeomorphic to $S^1\times\mathbb{R}_{>0}$.

**Proof.** The equation gives $q_x=\pm\sqrt{q_y^2+q_z^2}$, and the two signs are separated by $q_x=0$, where the equation forces $q_y=q_z=0$. Each nappe is parametrised by the sign of $q_x$, an angle in the plane $(q_y,q_z)$ and a positive radius.

So the nilpotent cone is a proper subcone of the zero-divisor cone: it is the part of the cone lying in the traceless subspace, of dimension two, while the zero-divisor cone has dimension three and is connected.

## The Link of the Null Cone

**Theorem (the link is a Clifford torus).** In the Euclidean sphere of matrices of Frobenius norm one, the zero-divisor cone cuts the torus

$$
\mathcal N\cap S^3 = \{X : \lvert z_1\rvert=\lvert z_2\rvert=\tfrac12\},
$$

with $z_1,z_2$ the complex coordinates of the previous section. This set is a flat torus $S^1\times S^1$.

**Proof.** The squared Frobenius norm is $2(\lvert z_1\rvert^2+\lvert z_2\rvert^2)$ and the determinant is $\lvert z_1\rvert^2-\lvert z_2\rvert^2$. On the unit sphere the two equations give $\lvert z_1\rvert^2=\lvert z_2\rvert^2=\tfrac14$, that is $\lvert z_1\rvert=\lvert z_2\rvert=\tfrac12$, which is the product of the two circles of radius $1/2$. The coordinates $z_1,z_2$ are related to the matrix entries by an orthogonal change of variables up to the factor $\sqrt2$, so this is the intersection with the round sphere.

**Corollary (the projectivised cone).** The projectivised zero-divisor cone is the doubly ruled quadric

$$
\mathcal N/\mathbb{R}^\times \cong \mathbb{R}P^1\times\mathbb{R}P^1,
$$

the two rulings being the image line $[u]$ and the kernel line $[v]$ of a rank-one matrix $uv^{\mathsf T}$.

**Proof.** The pair of lines $([u],[v])$ determines $X$ up to scale, and conversely $X$ determines its image and kernel. This is the Segre embedding of $\mathbb{R}P^1\times\mathbb{R}P^1$ as the quadric of rank-one matrices, developed in *Split-Quaternion Null Quadric and Projective Geometry*.

The link being a torus is the topological form of the double ruling: the torus is the product of the two circles of directions, and the two families of rulings are the two families of circles.

## Summary

The determinant of the model is the split-quaternion norm, a quadratic form of signature $(2,2)$, which in the complex coordinates $z_1=q_t-iq_x$ and $z_2=q_y+iq_z$ reads $\lvert z_1\rvert^2-\lvert z_2\rvert^2$. The invertible matrices are the units, the non-zero singular matrices are the zero divisors, and they have rank one; the origin is the only matrix of rank zero.

Every rank-one matrix is an outer product $uv^{\mathsf T}$, with $X^2=(v^{\mathsf T}u)X$. The nilpotents are the case $v^{\mathsf T}u=0$, equivalently $q_t=0$ and $q_x^2=q_y^2+q_z^2$, a two-dimensional cone with two nappes; the multiples of the idempotents are the complementary dense family. The projectivised cone is the doubly ruled quadric $\mathbb{R}P^1\times\mathbb{R}P^1$, and the link of the cone in the Euclidean sphere is the Clifford torus.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\langle\tilde q\rangle_{\natural}$ | the split-quaternion norm, the determinant | *Split-Quaternion Norm and Invertibility* |
| $B$ | the polar form of the determinant, signature $(2,2)$ | this article |
| $z_1,z_2$ | the complex coordinates $q_t-iq_x$ and $q_y+iq_z$ | this article |
| $\mathcal N$ | the null cone $\{\det=0\}$ | *Split-Quaternion Zero Divisors* |
| $u,v$ | the outer-product parameters of a rank-one matrix | this article |
| $\mathbb{R}P^1$ | the projective line of directions | *Split-Quaternion Null Quadric and Projective Geometry* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the rank stratification of a matrix algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the Segre embedding and the doubly ruled quadric.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the null cones of the low-dimensional Clifford algebras.
