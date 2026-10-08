# __The Zero Divisors and the Singular Julia Sets__

## Introduction

The biquaternion algebra is not a division algebra, and the failure is concentrated on a single cone: the set of non-zero elements of norm zero, equivalently the set of non-invertible elements, equivalently the rank-one matrices in the model. The cone is the critical set of the quadratic map, the set on which the square can collapse, the set on which no escape radius is uniform, the set on which the Green's function loses its normalization, and the set on which the Julia set is not a complex manifold. It is not a negligible exceptional set: for the parameter zero the whole surface of idempotents lies on the Julia set.

The zero divisors and their classification are *Biquaternion Zero Divisors*; the idempotents are *Biquaternion Idempotents and Projections*; the matrix model, the rank-one elements and the determinant are *Biquaternion 2×2 Matrix Element Representation*; the quadratic family and its critical set are *The Biquaternion Quadratic Map and Its Julia Sets*; the collapse of the square and the conditional radius are *The Biquaternion Mandelbrot Set and the Connectedness Locus*; the Green's function is *The Escape Radius and the Green's Function for the Biquaternions*.

The article owns the two kinds of zero divisor and the closed form of their square, the invariance of the cone under squaring, the affine dynamics it carries, the definition of the singular Julia set, and the theorem that the idempotent surface lies on the Julia set of the parameter zero. It does not re-derive the classification of the zero divisors, which is the zero-divisor article, and it does not treat the dimension of the singular set, which is *The Hausdorff Dimension of the Biquaternion Julia Sets*.

**Standing convention.** $\mathscr{Z}=\{\tilde Q\in\mathbb{B} : \tilde Q\neq0,\ N(\tilde Q)=0\}$ is the **zero-divisor cone**, $N$ the biquaternion norm, and $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ the quadratic family in the general plain bilinear product.

## The Two Kinds of Zero Divisor

**Proposition (the square of a zero divisor).** Every $\tilde Q\in\mathscr{Z}$ satisfies

$$
\tilde Q^2=2Q_0\,\tilde Q ,
$$

and consequently $\tilde Q^2$ is again a zero divisor, on the same complex line $\mathbb{C}\tilde Q$. In particular the cone is closed under squaring.

**Proof.** The Cayley–Hamilton identity of the matrix model reads $\tilde Q^2-2Q_0\tilde Q+N(\tilde Q)e_0=0$ (*Biquaternion 2×2 Matrix Element Representation*). On $\mathscr{Z}$ the last term vanishes and the identity is the displayed formula. Then $N(\tilde Q^2)=N(\tilde Q)^2=0$ by multiplicativity of the norm, so $\tilde Q^2$ is a zero divisor; and $\tilde Q^2\in\mathbb{C}\tilde Q$ because $2Q_0\in\mathbb{C}$.

**Theorem (the two kinds).** Every $\tilde Q\in\mathscr{Z}$ is exactly one of the following.

1. **Square-zero**: $\tilde Q^2=0$, equivalently $Q_0=0$. These are the pure vectors with $(\mathbf Q,\mathbf Q)=0$.
2. **Idempotent-like**: $\tilde Q=\tau\tilde\Pi$ with $\tau\in\mathbb{C}\setminus\{0\}$ and $\tilde\Pi$ a primitive idempotent; here $Q_0=\tau/2$, and $\tilde Q^2=\tau\tilde Q$.

**Proof.** The matrix $\Phi(\tilde Q)$ is rank one, so its spectrum is $\{0,\tau\}$ with $\tau=\operatorname{tr}\Phi(\tilde Q)=2Q_0$. If $\tau=0$ the matrix is nilpotent of trace and determinant zero, hence its square is zero, so $\tilde Q^2=0$; conversely $\tilde Q^2=0$ forces $N=0$ and $2Q_0\tilde Q=0$, so $Q_0=0$ because $\tilde Q\neq0$. If $\tau\neq0$ the matrix is diagonalisable with eigenvalues $\tau,0$, so $\Phi(\tilde Q)=\tau P$ with $P$ a rank-one idempotent, and transporting along the isomorphism $\Phi$ gives $\tilde Q=\tau\tilde\Pi$ for a rank-one idempotent $\tilde\Pi$ of the algebra; conversely such an element has norm $\tau^2N(\tilde\Pi)=0$ and is non-zero.

**Remark (the pure square-zero elements).** The square-zero elements form the cone $\{\mathbf Q : (\mathbf Q,\mathbf Q)=0\}\subset\mathrm{Vect}(\mathbb{B})$, the isotropic cone of the general plain bilinear form $\mathbf Q\cdot\mathbf Q$ on $\mathbb{C}^3$, and they are precisely the non-zero critical points at which $\Phi(\tilde Q)$ is nilpotent. The example $\tilde Q=e_1+ie_2$ of *The Biquaternion Quadratic Map and Its Julia Sets* is one of them.

## The Dynamics on the Cone

**Theorem (the affine dynamics of the cone and its lines).** Let $\tilde\Pi$ be a primitive idempotent and let $\tilde Q=\lambda\tilde\Pi$, $\lambda\in\mathbb{C}$. Then under $F_{\tilde C}$ with central parameter $\tilde C=Ce_0$,

$$
F_{\tilde C}(\lambda\tilde\Pi)=\lambda^2\tilde\Pi+C e_0 ,
$$

so the orbit leaves the line unless $C=0$; for $C=0$ the line $\mathbb{C}\tilde\Pi$ is invariant and the restriction is the complex map $\lambda\mapsto\lambda^2$ on the coordinate. For the pure square-zero elements and $C=0$, the orbit reaches $0$ in one step.

**Proof.** $\tilde\Pi^2=\tilde\Pi$ gives $(\lambda\tilde\Pi)^2=\lambda^2\tilde\Pi$; adding $Ce_0$ leaves the line $\mathbb{C}\tilde\Pi$ exactly when $C=0$. For a square-zero $\tilde Q$, $\tilde Q^2=0$ and $F_0(\tilde Q)=0$.

**Remark ($\tilde C=0$, the cone as a union of invariant lines).** For the parameter zero the cone is a union of complex lines through the origin, each mapped into itself with the square on the coordinate, and the induced map on the projective surface of lines is the identity. **The cone carries a foliation by invariant lines on which the dynamics is the scalar square**, and this is the only part of the biquaternion dynamics that is completely understood.

**Remark (the cone is not invariant for $\tilde C\neq0$).** Adding a non-zero central parameter moves the point off the line and off the cone, because $Ce_0$ has norm $C^2$ and the sum of a norm-zero element with a norm-nonzero central element has norm $C^2\neq0$. **The cone is invariant for exactly one parameter, and the interaction of the cone with the rest of the space is a genuinely two-way coupling** for every other parameter.

## The Singular Julia Set

**Definition.** Let $\Sigma(\mathbb{B})=\mathscr{Z}\cup\mathrm{Vect}(\mathbb{B})$ be the critical set of $F_{\tilde C}$, the union of the cone and the vector subspace (*The Biquaternion Quadratic Map and Its Julia Sets*). The **singular Julia set** of the parameter is

$$
\Sigma_{\tilde C}=J_{\tilde C}\cap\Sigma(\mathbb{B}),
$$

and its two parts are the **zero-divisor part** $J_{\tilde C}\cap\mathscr{Z}$ and the **pure part** $J_{\tilde C}\cap\mathrm{Vect}(\mathbb{B})$.

The name records that on $\Sigma(\mathbb{B})$ the derivative of $F_{\tilde C}$ is singular, so the local dynamics is not locally invertible and the Julia set there is not a complex manifold; every quantitative statement about the fractal — the escape radius, the Green's function, the dimension — needs a separate argument on the singular set.

**Theorem (the idempotent surface lies on the Julia set of the parameter zero).** For $\tilde C=0$, every idempotent $\tilde\Pi$ lies in $J_0$. The idempotents form the smooth complex surface $\{\tilde\Pi^2=\tilde\Pi\}$ inside the cone $\mathscr{Z}$, and hence

$$
\{\tilde\Pi : \tilde\Pi^2=\tilde\Pi\}\subset J_0\cap\mathscr{Z}=\Sigma_0\cap\mathscr{Z} .
$$

**Proof.** An idempotent is a fixed point, $F_0(\tilde\Pi)=\tilde\Pi$, and its matrix has spectrum $\{0,1\}$ with distinct eigenvalues, so $\rho(\Phi(\tilde\Pi))=1$ and $\Phi(\tilde\Pi)$ is diagonalisable; hence $\tilde\Pi\in\mathcal K_0$ by the corollary on the parameter zero of *The Biquaternion Quadratic Map and Its Julia Sets*. For $\lambda>1$ the element $\lambda\tilde\Pi$ has $\rho=\lambda>1$ and lies outside $\mathcal K_0$, while $\lambda\tilde\Pi\to\tilde\Pi$ as $\lambda\to1$. So every neighbourhood of $\tilde\Pi$ meets the complement of $\mathcal K_0$, and $\tilde\Pi\in\partial\mathcal K_0=J_0$. The variety of idempotents is the orbit of a single rank-one idempotent under the group of units, hence smooth of complex dimension two, and it is contained in the cone by $N(\tilde\Pi)=0$ for an idempotent.

**Corollary (the singular Julia set is not small).** $\Sigma_0$ contains a complex surface, so it is not a curve and not a countable set; in particular no statement that the singular part is negligible for the dimension can be true without qualification.

**Proof.** A complex surface has real dimension four, so the set is uncountable and of positive four-dimensional measure in the slice; the claim follows.

## The Obstructions Collected

The cone is the common obstruction of the four quantitative questions of the category, and the article collects them in one place.

| question | the classical answer | the obstruction on $\mathscr{Z}$ |
|---|---|---|
| escape radius | a single radius $1+\lvert C\rvert$ | $\tilde Q^2$ can vanish: no lower bound |
| Green's function | normalized at infinity | normalization fails, $G$ undefined on the cone |
| derivative and Fatou theory | locally invertible off critical points | $dF$ singular on the whole cone and on $\mathrm{Vect}$ |
| dimension | the Julia set is regular at a critical point of a polynomial | the surface of idempotents lies on $J_0$ |

**Remark (the zero divisors are the algebra, not a defect).** The zero-divisor cone is present for every element of the algebra and is not removed by a genericity assumption, because the algebra is fixed and not a family; the only escape is to restrict the dynamics to a division subalgebra, and the division subalgebras are the real quaternion subspace and its conjugates, which is why the quaternion slice is the computable one. **The singular Julia set is the price of doing dynamics in a complex algebra that is not a division algebra, and it is paid at every parameter.**

## Summary

Every zero divisor of the biquaternion algebra satisfies $\tilde Q^2=2Q_0\tilde Q$ and so squares to a zero divisor on the same complex line; the cone is closed under squaring and carries, for the parameter zero, a foliation by invariant complex lines on which the dynamics is the scalar square. The zero divisors are of exactly two kinds: the square-zero pure vectors, the isotropic cone of the general plain bilinear form on the vector part, and the non-zero complex multiples of primitive idempotents. The idempotents form a smooth complex surface inside the cone, and for the parameter zero that surface lies on the Julia set, so the singular Julia set contains a real four-dimensional set and is not negligible. The cone is the common obstruction of the escape radius, the Green's function, the invertibility of the derivative and the dimension theory; the pure vectors form the second component of the critical set; and the only escape from the obstruction is to restrict to a division subalgebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the biquaternion norm |
| $\mathscr{Z}=\{N(\tilde Q)=0,\ \tilde Q\neq0\}$ | the zero-divisor cone |
| $\mathrm{Vect}(\mathbb{B})=\{Q_0=0\}$ | the vector part, the pure subspace |
| $\Sigma(\mathbb{B})=\mathscr{Z}\cup\mathrm{Vect}(\mathbb{B})$ | the critical set of $F_{\tilde C}$ |
| $\Sigma_{\tilde C}=J_{\tilde C}\cap\Sigma(\mathbb{B})$ | the singular Julia set |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi^2=\tilde\Pi$ |
| $\tau=2Q_0$ | the non-zero eigenvalue of $\Phi(\tilde Q)$ on the cone |
| $\rho(\Phi(\tilde Q))$ | the spectral radius |

## Further Reading

- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the classification of the zero divisors and their rank-one form.
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the idempotents, the bijection with the roots of $-1$ and the standard idempotents.
- *The Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-biquaternion-quadratic-map-and-its-julia-sets.md`), for the critical set and the corollary on the parameter zero.
- *The Escape Radius and the Green's Function for the Biquaternions* (`articles_maths/the-escape-radius-and-the-greens-function-for-the-biquaternions.md`), for the failure of the escape radius and the conditional Green's function.
- *The Hausdorff Dimension of the Biquaternion Julia Sets* (`articles_maths/the-hausdorff-dimension-of-the-biquaternion-julia-sets.md`), for the dimension of the singular part.
