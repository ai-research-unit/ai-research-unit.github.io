
# __The Adjoint of a Hermitian Operator__

## Introduction

Let $V$ be a complex vector space with a positive-definite Hermitian form $\langle\cdot,\cdot\rangle$ and let $H$ be an operator on $V$. The **adjoint** of $H$ with respect to the form is the unique operator $H^{*}$ with
$$
\langle Hx, y\rangle = \langle x, H^{*}y\rangle \qquad (x, y \in V),
$$
and $H$ is **Hermitian** (or self-adjoint) when $H^{*} = H$, that is when $\langle Hx,y\rangle = \langle x,Hy\rangle$ for all $x,y$. The adjoint is the operator that the Hermitian form of the category produces out of $H$, and its explicit form is transparent in a unitary frame: if $H$ has matrix $(H_{ij})$ there, then the matrix of $H^{*}$ is the conjugate transpose,
$$
(H^{*})_{ij} = \overline{H_{ji}},
$$
so that a Hermitian operator is exactly an operator whose matrix is a Hermitian matrix, and $H$ is **anti-Hermitian** when $H^{*} = -H$, equivalently when $iH$ is Hermitian. The self-adjoint operators are the ones that a Hermitian form detects: the assignment $H \mapsto \langle H\cdot,\cdot\rangle$ is a bijection between the Hermitian operators and the Hermitian forms on $V$, the quadratic form $x\mapsto\langle Hx,x\rangle$ is real for Hermitian $H$, and the spectral theorem makes the Hermitian operators exactly the orthogonally diagonalisable ones with real eigenvalues.

The article has three sections: the adjoint and its explicit form; the Hermitian operators and the correspondence with the Hermitian forms; and the spectral statements. The Hermitian forms and the unitary group are *Hermitian Geometry and the Unitary Group*, the preceding article of this category; the sesquilinear forms and the polarisation are *Sesquilinear Forms and the Lax–Milgram Theorem* and *Quadratic Forms and Polarisation*; the spectral theorem is *Self-Adjoint Operators and the Spectral Theorem*; the adjoint operation in the general operator layer is *Adjoints in a Banach Algebra* and *The L2 Adjoint of a Differential Operator*; the real structure that conjugates an operator is *The Involution on a Complex Vector Space*. None of that is re-derived.

Throughout, $V$ is a complex vector space of dimension $m$ with the positive-definite Hermitian form $\langle\cdot,\cdot\rangle$, $H$ is an operator on $V$, $H^{*}$ is its adjoint, and $q_H(x) = \langle Hx,x\rangle$ is its quadratic form.

## The Adjoint and Its Explicit Form

**Proposition (existence and uniqueness of the adjoint).** For every operator $H$ there is a unique operator $H^{*}$ with $\langle Hx,y\rangle = \langle x,H^{*}y\rangle$ for all $x,y$. In a unitary frame $e_1,\dots,e_m$ the matrix of $H^{*}$ is the conjugate transpose of the matrix of $H$, $(H^{*})_{ij} = \overline{H_{ji}}$, and the assignment $H\mapsto H^{*}$ is conjugate-linear, involutive and an anti-automorphism,
$$
(aH+bK)^{*} = \bar aH^{*}+\bar bK^{*}, \qquad (H^{*})^{*} = H, \qquad (HK)^{*} = K^{*}H^{*}.
$$

**Proof.** For fixed $y$ the map $x\mapsto\langle Hx,y\rangle$ is conjugate-linear, hence of the form $x\mapsto \langle x, z\rangle$ for a unique $z$, by the representation of conjugate-linear functionals through the positive-definite form; set $H^{*}y = z$. In a unitary frame the entries satisfy $\langle He_j,e_i\rangle = H_{ij}$ and $\langle e_j,H^{*}e_i\rangle = (H^{*})_{ij}$, so the defining identity gives $H_{ij} = \overline{(H^{*})_{ij}}$, that is $(H^{*})_{ij} = \overline{H_{ji}}$. The three properties are immediate from the definition and the antilinearity of the form in its second argument in the appropriate slot. Hermitian forms and the representation of functionals are *Hermitian Geometry and the Unitary Group* and *Hermitian Forms and Unitary Geometry*.

**Proposition (the Hermitian operator).** $H$ is Hermitian, $H^{*} = H$, if and only if its quadratic form is real, $\langle Hx,x\rangle \in \mathbb{R}$ for all $x$, if and only if its matrix in some unitary frame is a Hermitian matrix; $H$ is anti-Hermitian if and only if $iH$ is Hermitian, and every operator decomposes uniquely as
$$
H = \tfrac12(H+H^{*}) + \tfrac12(H-H^{*}),
$$
the sum of a Hermitian and an anti-Hermitian operator, the **real and imaginary parts** of $H$.

**Proof.** If $H^{*}=H$ then $\langle Hx,x\rangle = \overline{\langle x,Hx\rangle} = \overline{\langle Hx,x\rangle}$ is real; conversely if the quadratic form is real, the polarisation of $\langle Hx,y\rangle$ from $q_H$ shows $\langle Hx,y\rangle = \langle x,Hy\rangle$, so $H^{*}=H$. The matrix statement is the previous proposition; the decomposition is the projection onto the self-adjoint and skew-adjoint parts, using $(H+H^{*})^{*} = H+H^{*}$ and $(H-H^{*})^{*} = H^{*}-H$. This is *Quadratic Forms and Polarisation* and *Hermitian Geometry and the Unitary Group*.

## The Hermitian Operators and the Hermitian Forms

**Proposition (the correspondence).** The assignment
$$
H \longmapsto h_H, \qquad h_H(x,y) = \langle Hx, y\rangle ,
$$
is a bijection between the Hermitian operators on $V$ and the Hermitian forms on $V$; under it the definite operators correspond to the definite forms, $\langle Hx,x\rangle > 0$ for $x\neq0$, and the positive operators are exactly those of the form $H = K^{*}K$.

**Proof.** $h_H$ is sesquilinear and $h_H(y,x) = \overline{\langle Hy,x\rangle} = \overline{\langle y,H^{*}x\rangle} = \langle H^{*}x,y\rangle = h_{H^{*}}(x,y)$, so $h_H$ is Hermitian exactly when $H = H^{*}$; the converse is the representation of a sesquilinear form by an operator through the definite form. Finally $\langle K^{*}Kx,x\rangle = \langle Kx,Kx\rangle \ge 0$, and conversely a positive $H$ has a positive square root $K = \sqrt H$ with $H = K^2 = K^{*}K$. The positivity of operators and forms is *Hermitian Geometry and the Unitary Group*, and the square root is *Self-Adjoint Operators and the Spectral Theorem*.

**Corollary (self-adjointness of the structural operators).** The complex structure is anti-Hermitian, $J^{*} = -J$; a unitary operator $U$ satisfies $U^{*}U = UU^{*} = I$, so its adjoint is its inverse, $U^{*} = U^{-1}$. A conjugation $c$ compatible with the form, $h(cx,cy) = \overline{h(x,y)}$, is **antiunitary**: it is antilinear, so it has no ordinary adjoint, but the adjoint of an antilinear map defined by $h(cx,y) = \overline{h(x,c^{\dagger}y)}$ gives $c^{\dagger} = c$, so a compatible conjugation is self-adjoint in the antilinear sense.

**Proof.** $\langle Jx,y\rangle = -\langle x,Jy\rangle$ is the skew-adjointness of $J$ for a Hermitian form; $U^{*}U=I$ is the isometry condition, and the inverse of a unitary is its adjoint. For a compatible conjugation, $h(cx,y) = h(cx,c(cy)) = \overline{h(x,cy)}$ (using $c^2=\mathrm{id}$ and compatibility), which is exactly $c^{\dagger}=c$ under the antilinear adjoint convention. These are *The Involution on a Complex Vector Space* and *Hermitian Geometry and the Unitary Group*.

## The Spectral Statements and the Positivity

**Theorem (the spectral theorem, quoted).** A Hermitian operator on a finite-dimensional Hermitian space has an orthonormal basis of eigenvectors and real eigenvalues; it is **positive** when all its eigenvalues are $> 0$ and **positive semidefinite** when they are $\ge 0$, and the eigenvalues of $H$ are the critical values of the quadratic form $q_H$ restricted to the unit sphere.

**Proof.** The statement and its proof are *Self-Adjoint Operators and the Spectral Theorem*; the reality of the eigenvalues follows from the reality of $q_H$, the orthogonality of the eigenvectors of distinct eigenvalues from the self-adjointness, and the variational description is the Rayleigh quotient $\lambda = \min_{x\neq0} q_H(x)/\langle x,x\rangle$ on the appropriate subspace. This is quoted and not re-derived.

**Proposition (the operator norm and the numerical radius).** The **operator norm** $\|H\| = \sup\{ \|Hx\| : \|x\| = 1\}$ equals the largest modulus of an eigenvalue of $H$ for normal operators (and in particular for Hermitian and unitary operators), and the **numerical radius** $w(H) = \sup\{ |\langle Hx,x\rangle| : \|x\|=1\}$ equals $\|H\|$ for Hermitian $H$.

**Proof.** For a normal operator there is an orthonormal eigenbasis and $\|Hx\|^2 = \sum_k|\lambda_k|^2|x_k|^2 \le (\max|\lambda_k|)^2\|x\|^2$ with equality on an eigenvector of the largest modulus; for Hermitian $H$ the eigenvalues are real and $w(H) = \max|\lambda_k| = \|H\|$ by the variational description. The spectral theorem and the norm are *Self-Adjoint Operators and the Spectral Theorem* and *Normed and Banach Spaces*.

**Example (the projections and the Hermitian involutions).** An **orthogonal projection** is a Hermitian operator with $P^2 = P$, its eigenvalues $0$ and $1$, its quadratic form $q_P(x) = \|Px\|^2 \ge 0$; it is the adjoint-invariant form of a direct-sum decomposition $V = \operatorname{im}P\oplus\ker P$ with the summands orthogonal. A **Hermitian involution** is a Hermitian operator with $H^2 = I$, that is a unitary self-adjoint operator: the unitary reflections of *The Signed Adjoint of the Reflection on a Complex Vector Space* are the standard examples, and the orthogonal projection $P$ is the Hermitian idempotent. The compatible conjugation of *The Involution on a Complex Vector Space* is the antilinear companion of these, and the Bergman projection is the infinite-dimensional instance, *The Bergman Operator* and *Involutions of the Bergman Operator*.

## Summary

On a Hermitian space $(V,\langle\cdot,\cdot\rangle)$ the adjoint of an operator $H$ is the unique $H^{*}$ with $\langle Hx,y\rangle = \langle x,H^{*}y\rangle$; in a unitary frame it is the conjugate transpose, $(H^{*})_{ij} = \overline{H_{ji}}$, and the assignment is conjugate-linear, involutive and an anti-automorphism. $H$ is Hermitian exactly when its quadratic form is real, equivalently when its matrix is Hermitian; every operator splits into its Hermitian and anti-Hermitian parts; a Hermitian operator has real eigenvalues and an orthonormal eigenbasis by the spectral theorem, is positive exactly when $H = K^{*}K$, and its norm and numerical radius agree. The Hermitian operators are in bijection with the Hermitian forms by $h_H(x,y) = \langle Hx,y\rangle$, the definite forms corresponding to the positive operators; the structural operators satisfy $J^{*} = -J$ and $U^{*} = U^{-1}$, and a compatible conjugation is antiunitary, self-adjoint in the antilinear sense. The forms and the unitary group are *Hermitian Geometry and the Unitary Group*; the polarisation is *Quadratic Forms and Polarisation*; the spectral theorem is *Self-Adjoint Operators and the Spectral Theorem*; the linear conjugation is *The Involution on a Complex Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H^{*}$ | the adjoint, $\langle Hx,y\rangle=\langle x,H^{*}y\rangle$ |
| $(H^{*})_{ij}=\overline{H_{ji}}$ | the explicit form in a unitary frame |
| $H^{*}=H$ | Hermitian operator; real quadratic form |
| $H=\frac12(H+H^{*})+\frac12(H-H^{*})$ | Hermitian and anti-Hermitian parts |
| $h_H(x,y)=\langle Hx,y\rangle$ | the Hermitian form of a Hermitian operator |
| $H=K^{*}K$ | the positive operators |
| $J^{*}=-J$, $U^{*}=U^{-1}$ | the complex structure and the unitary operators |
| $c^{\dagger}=c$ | a compatible conjugation, antiunitary |

## Further Reading

- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the adjoint, the Hermitian operators and the spectral theorem.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2012), for the conjugate transpose, the Hermitian matrices and the positivity.
- Werner Greub, *Linear Algebra* (Springer, fourth edition, 1975), for the Hermitian forms, the adjoint and the correspondence with the operators.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the self-adjoint and unitary operators in the Hermitian geometry.
