# __The Two Eigenvalues Are the Two Weyl Weights__

## Introduction

A Hermitian biquaternion of unit norm is a boost, and as a matrix it is Hermitian, so it acts on the two-component spinor module with two real eigenvalues. They are

$$
\lambda_\pm=e^{\pm\theta_{\mathrm{rpd}}/2},
$$

one greater than one, one less, with product one. Their logarithms, divided by the parameter, are the two weights $\pm\tfrac12$: the two Weyl weights of the fundamental representation of the Lorentz algebra.

This article derives that identification, states why a Hermitian generator is the one to diagonalise, shows how the eigenvalues and the weights are related to the roots, and computes the exceptional case in which the two eigenvalues coincide.

The article assumes *The Spinor Module in Biquaternionic Form and Its Lorentz Action* for the module, *The Six Generators and Their Commutators* for the Cartan elements, and *The Cartan Subalgebra, the Roots and the Three Real Forms* for the roots. It feeds *$P$, $T$ and the Representation Labels* and *The Principal Series and the Complementary Series*, where the same eigenvalues become the labels of the infinite-dimensional modules.

## The Left Action on the Spinor Module

### The Module

The spinor module is $\mathbb{C}^{2}$ under the left action of the algebra, $\xi\mapsto\mathsf{M}_2(\tilde Q)\xi$. Its two chiral halves are the eigenspaces of the chirality element, and the left action preserves the chirality only for elements in a definite summand of the complexified algebra. *The Spinor Module in Biquaternionic Form and Its Lorentz Action* develops all of that; this article needs only the two-dimensional carrier and the left multiplication.

### A Hermitian Element Acting

Let $\tilde H\in\mathbb{B}_\Psi$ with $\langle\tilde H\rangle_{\natural}=1$. Then $\mathsf{M}_2(\tilde H)$ is Hermitian of determinant one, so it is Hermitian and has real eigenvalues whose product is one. Its eigenvalues are

$$
\lambda_\pm=\frac{\operatorname{tr}\mathsf{M}_2(\tilde H)}{2}\pm\sqrt{\Bigl(\frac{\operatorname{tr}\mathsf{M}_2(\tilde H)}{2}\Bigr)^{2}-1},
$$

the standard formula for the eigenvalues of a two-by-two matrix of determinant one, and $\lambda_++\lambda_-=\operatorname{tr}$, $\lambda_+\lambda_-=1$.

### Why a Hermitian Generator

For an anti-Hermitian element the eigenvalues are imaginary times something and need not be real; for a general element they are unrestricted. The Hermitian elements are the ones whose eigenvalues are real and positive-or-negative, and those are the ones that can be read as exponentials of real weights. The $*$-unitary elements give eigenvalues on the unit circle, which are read as imaginary weights.

So the article treats two cases and their union is the whole group's diagonalisable part:

| element | matrix | eigenvalues | type of weight |
|---|---|---|---|
| boost, $\tilde H=\tilde H^{*}$ | Hermitian | real, $\lambda_+\lambda_-=1$ | real |
| rotation, $\tilde U^{*}\tilde U=e_t$ | unitary | on the unit circle | imaginary |

## The Eigenvalue Equation

### The Statement

$$
\mathsf{M}_2(\tilde H)\,\xi_\pm=\lambda_\pm\,\xi_\pm,
\qquad \xi_\pm\in\mathbb{C}^{2},\quad \xi_\pm\neq0 .
$$

### The Reduction

Write the boost in the word of *The Group of Unit-Norm Biquaternions*,

$$
\tilde H=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\hat u\Bigr)=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}+i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\hat u,
\qquad \hat u^{2}=-e_t,
$$

and use $\mathsf{M}_2(i\hat u)=\hat u\cdot\vec\sigma$, whose eigenvalues are $\pm1$ with eigenvectors the two spin states along $\hat u$. Then

$$
\mathsf{M}_2(\tilde H)=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}I+\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\,(\hat u\cdot\vec\sigma),
$$

whose eigenvalues are

$$
\lambda_\pm=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}\pm\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}=e^{\pm\theta_{\mathrm{rpd}}/2}.
$$

The two lines use only the identity $e^{\pm x}=\cosh x\pm\sinh x$.

### The Solutions

The eigenvectors are the two eigenspinors of $\hat u\cdot\vec\sigma$: the spin states along the boost axis, which the boost does not mix. So a boost scales the two spin states along its own axis by reciprocal factors, and mixes nothing. That statement is exact and is worth stating because the analogous statement for a rotation is the same with $\pm i$ in place of $\pm$.

### The Verification

For a boost of rapidity $0.9$ along $\vec e_z$, the numerically computed eigenvalues are $1.568312$ and $0.637628$, against $e^{0.45}=1.568312$ and $e^{-0.45}=0.637628$. For a rotation by $0.7$ about $\vec e_z$ the eigenvalues are $0.939373\mp0.342898i$, which is $e^{\mp0.35i}$. Both agree to machine precision, and the eigenvectors are the coordinate spin states for an axis along $\vec e_z$ and the diagonal ones for an axis along $\vec e_x$.

## The General Element

### The Two Eigenvalues in Closed Form

The boost case is the special case of a formula that holds for every element. Let $B$ be a chosen square root of $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$, so that $B^{2}$ is the corpus's squared vector part and $B$ its square root. Then the eigenvalues of the matrix image are

$$
\lambda_\pm=Q_t\pm iB .
$$

The proof is one line. The matrix image is $Q_tI-i\vec Q\cdot\vec\sigma$, and $(\vec Q\cdot\vec\sigma)^{2}=B^{2}I$, so the eigenvalues of $\vec Q\cdot\vec\sigma$ are $\pm B$ and the two eigenvalues of the image follow.

Two conventions are worth stating because they are easy to get wrong. The square root is a choice: replacing $B$ by $-B$ swaps the two eigenvalues, and no physical statement may depend on the choice. And $B$ is the square root while $B^{2}$ is the square, so a formula that writes $iB$ in one place and $iB^{2}$ in another has changed the object.

### The Idempotents From a Unit Vector

Set

$$
\vec Z=-\frac{i\vec Q}{B} .
$$

Then $\vec Z\cdot\vec Z=-1$ and, as an algebra product, $\vec Z^{2}=e_t$. The two elements

$$
P_\pm=\tfrac12\bigl(e_t\pm\vec Z\bigr)
$$

therefore satisfy

$$
P_\pm^{2}=P_\pm,\qquad P_++P_-=e_t,\qquad P_+P_-=0 ,
$$

and since $\vec Q=iB\vec Z$,

$$
\tilde Q=(Q_t+iB)P_+ +(Q_t-iB)P_- .
$$

So the two eigenvalues are read off a decomposition of the element into two projectors, and the projectors are the eigenprojectors of the matrix image. Each is rank one, each has trace one, and each has quaternionic norm zero: a rank-one projector of determinant zero is a zero divisor, and that is what an eigenprojector of a two-by-two matrix of trace one and determinant zero is.

The boost case is now the special case $\vec Z$ real: a Hermitian element has $\vec Q$ real, so $\vec Z$ is a real vector and $P_\pm$ are the two spin projectors along the boost axis.

### The Case $B=0$

At $B=0$ the vector $\vec Z$ does not exist, and there are two subcases. If $\vec Q=0$ the element is central and every projector is an eigenprojector. If $\vec Q\neq0$ but null, the element has a repeated eigenvalue and only one eigenline, so no pair of complementary projectors exists. The idempotent decomposition is thus exactly the statement that the element is semisimple, and the corpus's criterion $B^{2}\neq0$ is that same statement in the notation of the norm.

### The Check

On random complex elements the computed eigenvalues of $\mathsf{M}_2(\tilde Q)$ agree with $Q_t\pm iB$ to machine precision; the projectors satisfy $P_\pm^{2}=P_\pm$ to $10^{-16}$; their quaternionic norms vanish to $10^{-16}$; and the reconstruction $(Q_t+iB)P_++(Q_t-iB)P_-$ reproduces $\tilde Q$ to $9\times10^{-16}$.

## The Eigenvalues Are the Weights

### The Cartan Element

Take the boost axis to be $\vec e_z$. The generator of the family is the Cartan element

$$
K_z=\tfrac12 i\vec e_z,\qquad \mathsf{M}_2(K_z)=\tfrac12\sigma_z,
$$

and the boost of rapidity $\theta_{\mathrm{rpd}}$ is $\exp(\theta_{\mathrm{rpd}}K_z)$. The two eigenspinors of $\mathsf{M}_2(K_z)$ have eigenvalues $\pm\tfrac12$.

### The Weight Definition

A weight of a representation is a linear functional $w$ on the Cartan such that the representation's Cartan action on the weight vector is multiplication by $w(H)$. For the fundamental representation on $\mathbb{C}^{2}$ the two weights are

$$
w_\pm(K_z)=\pm\tfrac12 .
$$

Then the representation's action of the group element $\exp(\theta_{\mathrm{rpd}} K_z)$ on the weight vector is multiplication by

$$
e^{\theta_{\mathrm{rpd}}\,w_\pm(K_z)}=e^{\pm\theta_{\mathrm{rpd}}/2},
$$

which is exactly the eigenvalue computed above.

### The Dictionary

| object | value on the fundamental | where it appears |
|---|---|---|
| weight $w_+$ | $+\tfrac12$ | $\lambda_+=e^{+\theta_{\mathrm{rpd}}/2}$ |
| $B$, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square root of the squared vector part, and the square itself |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues of the general element |
| $\vec Z=-i\vec Q/B$, $P_\pm=\tfrac12(e_t\pm\vec Z)$ | the unit vector of the vector part and the two eigenprojectors |
| weight $w_-$ | $-\tfrac12$ | $\lambda_-=e^{-\theta_{\mathrm{rpd}}/2}$ |
| sum $w_++w_-$ | $0$ | $\det=1$ |
| root of the adjoint | $\pm1$ | eigenvalue ratio $e^{2\theta_{\mathrm{rpd}}}$ |

The last row is the statement that the adjoint's eigenvalues are $\pm\alpha$ with $\alpha$ the root, and the fundamental's are $\pm\tfrac12\alpha$: one factor of two, which is the same factor of two that makes the fundamental a spinor rather than a vector.

### Why the Statement Is Not a Tautology

It would be circular to say "the eigenvalues are the weights" if the weights were defined as the eigenvalues. They are not: the weights are defined as linear functionals on the Cartan subalgebra, computed from the structure of the representation and the root system, and they exist before any exponential is taken. The content of the identification is that exponentiating a weight functional evaluated on a generator reproduces the matrix eigenvalue. That is a theorem about the compatibility of the exponential with the weight decomposition, and it is what makes the weights the right labels.

## The Two Roots and the Two Weights

### The Roots

The adjoint representation has eigenvalues $\pm\alpha$ on the Cartan, with $\alpha(K_z)=1$ in the normalisation where the root length is one. In the corpus's anti-Hermitian convention the two Cartan generators $K_z$ and $J_z$ give different root values, real and imaginary respectively, as *The Cartan Subalgebra, the Roots and the Three Real Forms* states.

### The Weights

The fundamental representation has eigenvalues $\pm\tfrac12\alpha$ on the same Cartan. So the two Weyl weights are half the two roots, and the "half" is the spin.

### The Shift by $\rho$

The sum of the two weights is zero, and the Weyl vector is $\rho=\tfrac12\alpha$. Adding $\rho$ to each weight gives $\{0,1\}$, the two integers that label the two states of a two-level system. That shift is the reason the eigenvalues $e^{\pm\theta_{\mathrm{rpd}}/2}$ are conventionally rewritten as $e^{\theta_{\mathrm{rpd}}/2}$ and $e^{-\theta_{\mathrm{rpd}}/2}$ rather than as a symmetric pair around one, and it is the reason the second Casimir's eigenvalues are $m(m+1)$ rather than $m^{2}$.

### Why Two and Only Two

The fundamental representation is two-dimensional, so it has two weights. The number of weights equals the dimension, and the number of independent ones equals the rank, here one. For the Lorentz algebra the rank is two, so a representation's weights are labelled by two integers, which is the $(m,n)$ of the block.

## The Diagonalisation

### The Unitary Diagonalisation

Because $\mathsf{M}_2(\tilde H)$ is Hermitian, it is diagonalised by a unitary matrix:

$$
\mathsf{M}_2(\tilde H)=\mathsf{M}_2(\tilde u)\,D\,\mathsf{M}_2(\tilde u)^{*},
\qquad D=\operatorname{diag}(\lambda_+,\lambda_-),
$$

with $\tilde u$ a unit real quaternion, that is an element of $SU(2)$. The two-by-two biquaternion statement is

$$
\tilde H=\tilde u\,\bigl(e^{\theta_{\mathrm{rpd}}/2}\Pi_++e^{-\theta_{\mathrm{rpd}}/2}\Pi_-\bigr)\,\tilde u^{*},
$$

with $\Pi_\pm$ the two eigenprojectors, which are Hermitian idempotents of trace one. The eigenprojectors are the objects *The Rest Frame and the Exceptional Point* uses, and the equality above is the spectral theorem written in the algebra.

### The Angles

The diagonalising $\tilde u$ is a rotation, and its angle and axis are read from $\tilde H$'s vector part: the axis of $\tilde u$ is orthogonal to $\hat u$, and its angle is fixed by the relative phase of the two eigenvectors. The block uses the diagonalisation only through the eigenvalues, and the angle is material for *The Spectrum Does Not Determine the Frame*.

### The Physical Reading

The two eigenprojectors are the two spin states along the boost axis. A boost along $\hat u$ rescales the two of them reciprocally: one is stretched by $e^{+\theta_{\mathrm{rpd}}/2}$, the other squeezed by $e^{-\theta_{\mathrm{rpd}}/2}$. The product of the two scalings is one, which is the determinant condition, and the sum is $2\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}$, which is the trace.

## The Degenerate Case

### When the Eigenvalues Coincide

$\lambda_+=\lambda_-$ requires $\operatorname{tr}^{2}=4$, that is $H_t^{2}=1$. Since $\tilde H$ is Hermitian of unit norm, $H_t$ is real and

$$
1=\langle\tilde H\rangle_{\natural}=H_t^{2}+\sum_\eta H_\eta^{2}=H_t^{2}-\sum_\eta\lvert H_\eta\rvert^{2},
$$

so $H_t^{2}\ge1$ with equality **if and only if the vector part vanishes**. Hence

$$
\lambda_+=\lambda_-\iff\tilde H=\pm e_t .
$$

### What It Means

At $\tilde H=e_t$ both eigenvalues are $1$ and the eigenprojectors are undefined; at $\tilde H=-e_t$ both are $-1$, and the element is not Hermitian positive, so it is not an admissible boost factor. So the boost family's eigenvalues are distinct at every point except the identity, where the whole family collapses.

### The Reading at the Boundary

The rapidity $\theta_{\mathrm{rpd}}\to\infty$ is *not* a degenerate case: the eigenvalues run to $\infty$ and $0$ and stay distinct. The degenerate case is the opposite end, $\theta_{\mathrm{rpd}}=0$, the identity. This is worth saying because a reader who expects degeneracy at the speed of light will look in the wrong place: at the light speed the eigenvalues are infinite and zero, and the spinor transformation is singular in the limit but its two eigenvalues remain distinguishable for every finite rapidity.

### The Rotation's Degenerate Case

For a rotation the eigenvalues are $e^{\pm i\theta_{\mathrm{axr}}/2}$, which coincide exactly when $\theta_{\mathrm{axr}}\in\{0,2\pi\}$, that is at $\pm e_t$. The two families therefore degenerate at the same two elements, and the reason is the same: total scalar action.

## Summary

A Hermitian unit-norm biquaternion acts on the two-component spinor module with two real eigenvalues $\lambda_\pm=e^{\pm\theta_{\mathrm{rpd}}/2}$, whose product is one and whose sum is $2\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}$. Exponentiating the two weights $\pm\tfrac12$ of the fundamental representation of the Cartan generator $K_z$ reproduces those eigenvalues exactly, so the two eigenvalues *are* the two Weyl weights once the parameter is fixed. The weights are half the two roots of the adjoint, the shift by $\rho=\tfrac12\alpha$ turns them into $\{0,1\}$, and the factor of two between weights and roots is the spin. The diagonalisation is unitary, its eigenprojectors are the two spin states along the boost axis, and the eigenvalues coincide only at $\pm e_t$, never at the speed of light.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde H$ | a Hermitian element of unit norm, a boost |
| $\lambda_\pm$ | its two eigenvalues on the spinor module |
| $w_\pm=\pm\tfrac12$ | the two weights of the fundamental representation |
| $\alpha$ | the root of the adjoint |
| $\rho=\tfrac12\alpha$ | the Weyl vector |
| $\Pi_\pm$ | the eigenprojectors |
| $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{axr}}$ | rapidity, rotation angle |

## Further Reading

- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer, 1991 — weights, the Weyl vector, and $\mathfrak{sl}_2$'s fundamental representation worked from the definitions.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015 — weights and the exponential of a Cartan element; the theorem that exponentiating a weight gives the eigenvalue.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.4 — the boost eigenvalues $e^{\pm\theta_{\mathrm{rpd}}/2}$ and their identification with the spinor's weights.
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Cambridge University Press, 2001 — eigenprojectors of a Hermitian element in a Clifford algebra.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* — the left action used here.
- *The Rest Frame and the Exceptional Point* — the eigenprojectors read as states.
