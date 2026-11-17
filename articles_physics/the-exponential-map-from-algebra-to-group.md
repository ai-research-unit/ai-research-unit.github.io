# __The Exponential Map from Algebra to Group__

## Introduction

The exponential map carries the six-dimensional Lie algebra to the six-dimensional group. On a two-by-two traceless matrix it has a closed form, because Cayley–Hamilton reduces every power to a multiple of the first: for a traceless $\tilde X$,

$$
\exp(\tilde X)=\cos\Rho+\frac{\sin\Rho}{\Rho}\,\tilde X,
\qquad \Rho^{2}=\tfrac12\operatorname{tr}\bigl(\tilde X^{2}\bigr),
$$

with the limit $\Rho\to0$ understood as the identity plus $\tilde X$. One formula contains the rotation family and the boost family: when $\Rho$ is real the formula is a rotation, and when $\Rho$ is imaginary it is a boost.

The article then states something that is often asserted wrongly. The exponential of the traceless algebra is **not** onto the unit-norm group. It misses one conjugacy class, the class of $-e_t$ plus a nonzero nilpotent, and the missing class is exactly what produces the "$\pi$ rotation" of the double cover at the level of the algebra. The exponential of the **full eight-dimensional algebra** is onto the group of invertibles, by a different and classical theorem, and the difference between the two statements is the central direction.

The article assumes *The Group of Unit-Norm Biquaternions* for the group and its dimension, *The Six Generators and Their Commutators* for the algebra, and *The Two Casimirs of the Lorentz Algebra* for the labels. It feeds *A Frame Is a Boost Times a Rotation: The Cartan Word* and *The Principal Series and the Complementary Series*.

## The Exponential of a Biquaternion

### The Series

$$
\exp(\tilde X)=\sum_{n\ge0}\frac{\tilde X^{n}}{n!},
$$

convergent for every $\tilde X$ because the algebra is finite-dimensional and the norm is submultiplicative. Under the isomorphism $\mathsf{M}_2$ it is the matrix exponential, since $\mathsf{M}_2$ is an algebra isomorphism and preserves sums and products.

### The Determinant of the Exponential

In the $2\times2$ image the Jacobi identity is the trace of the image,

$$
\det\mathsf M_2(\exp\tilde X)=e^{2\,\mathrm{Sc}\tilde X}.
$$

For a scalar-free $\tilde X$ this reads $\langle\exp\tilde X\rangle_{\natural}=1$, so the exponential of the Lie algebra lands in the unit-norm group. That one line replaces every series computation of the norm, and it is the cleanest proof that $\exp\mathfrak{sl}\subset SL_2(\mathbb{C})$.

### Cayley–Hamilton in Two Dimensions

Every $2\times2$ matrix satisfies its characteristic polynomial. For scalar-free $\tilde X$,

$$
\tilde X^{2}=-\langle\tilde X\rangle_{\natural}\,e_t,
$$

so every power of $\tilde X$ is a multiple of $e_t$ or of $\tilde X$. Summing the series term by term,

$$
\exp(\tilde X)=\Bigl(\sum_{k\ge0}\frac{(-1)^{k}\langle\tilde X\rangle_{\natural}^{k}}{(2k)!}\Bigr)e_t
+\Bigl(\sum_{k\ge0}\frac{(-1)^{k}\langle\tilde X\rangle_{\natural}^{k}}{(2k+1)!}\Bigr)\tilde X
=\cos\Rho+\frac{\sin\Rho}{\Rho}\tilde X,
$$

with $\Rho^{2}=-\langle\tilde X\rangle_{\natural}$. The two series are the cosine and the cardinal sine of $\Rho$, and the identity $\Rho^{2}=-\langle\tilde X\rangle_{\natural}=\mathrm{Sc}(\tilde X^{2})$ follows from the same characteristic polynomial.

### The Verification

The closed form is checked against the series on random traceless complex matrices to machine precision, and it is checked to reduce to the rotation and the boost formulas below. The check is exact in the special cases $\Rho=i\pi k$, where the coefficient $\frac{\sin\Rho}{\Rho}$ vanishes and the exponential is the scalar $(-1)^{k}e_t$; this is the exceptional case of §*What Is True and What Is Not*.

## The Two Closed Forms

### The Compact Case

When $\Rho$ is real and nonzero, write $\tilde X=\Rho\hat X$ with $\hat X$ scalar-free and $\hat X^{2}=-e_t$. Then

$$
\exp(\tilde X)=\cos\Rho+\sin\Rho\,\hat{\tilde X},
\qquad \tilde X^{2}=-\Rho^{2},\quad \hat X^{2}=-e_t .
$$

This is the rotation family: $\hat X$ is a real unit vector $\vec u_{\mathrm r}$ and $\Rho=\tfrac12\theta_{\mathrm{axr}}$, so the formula is $\cos\tfrac{\theta_{\mathrm{axr}}}{2}+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$, the rotor of *The Lorentz Transformation as a Biquaternionic Rotation*.

### The Split Case

When $\Rho$ is imaginary, write $\Rho=i\vartheta$ with $\vartheta$ real and $\tilde X=\vartheta\hat X$ with $\hat X^{2}=+e_t$. Then

$$
\exp(\tilde X)=\cosh\vartheta+\sinh\vartheta\,\hat{\tilde X},
\qquad \tilde X^{2}=+\vartheta^{2},\quad \hat X^{2}=+e_t .
$$

This is the boost family: $\hat X=i\vec u_{\mathrm b}$ and $\vartheta=\tfrac12\theta_{\mathrm{rpd}}$, so the formula is $\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}+\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$.

The menu writes the split case with the letter $\Rho$ for what is $\vartheta$ here and the compact case with the same letter for the real $\Rho$. Both are the same complex modulus evaluated on two different ranges of the complex plane, and the one formula above covers both.

### One Formula, Two Ranges

The statements of the two subsections are the statement of the single formula, read on two ranges of $\Rho$:

| range of $\Rho$ | generator | exponential | group element |
|---|---|---|---|
| $\Rho$ real | $\Rho\vec u_{\mathrm r}$, $\vec u_{\mathrm r}^{2}=-e_t$ | $\cos\Rho+\sin\Rho\,\vec u_{\mathrm r}$ | rotation by $2\Rho$ |
| $\Rho=i\vartheta$ | $i\vartheta\vec u_{\mathrm b}$, $\vec u_{\mathrm b}^{2}=-e_t$ | $\cosh\vartheta+\sinh\vartheta\,\vec u_{\mathrm b}$ | boost by $2\vartheta$ |
| $\Rho=0$ | nilpotent | $e_t+\tilde X$ | a wall element |

The third row is the degenerate case: a nonzero scalar-free nilpotent is exactly the sort of element whose $\Rho$ vanishes, because $\langle\tilde X\rangle_{\natural}=0$.

### The Half-Angle Convention

The factor $\tfrac12$ in the generators of *The Six Generators and Their Commutators* is what makes the argument of the cosine one half of the physical angle. The block keeps it, because it makes the rotor a single exponential without a factor of two, and it reports the physical angle as $2\Rho$ wherever a laboratory number is needed.

## What the Closed Form Parametrises

### The Three Cases of a Scalar-Free Element

Every scalar-free $\tilde X$ is one of three kinds, and the value of $\Rho^{2}$ decides which.

- $\Rho^{2}\neq0$: the two eigenvalues are $\pm\Rho$ and are distinct, so $\tilde X$ is diagonalisable and the exponential is conjugate to $\operatorname{diag}(e^{\Rho},e^{-\Rho})$.
- $\Rho^{2}=0$ with $\tilde X\neq0$: $\tilde X$ is nilpotent, and the exponential is $e_t+\tilde X$, a unipotent element with a nonzero nilpotent part.
- $\Rho^{2}=0$ with $\tilde X=0$: the identity.

Those are the only three cases, because a two-by-two traceless matrix either has two distinct eigenvalues or both zero.

The third case is the one the closed form's limit produces, and it is the case that the surjectivity question turns on.

### What the Parameters Are

The traceless algebra has six real parameters. The closed form uses
$\Rho$ (two real parameters, since it is complex) and the direction of $\hat X$ (four real parameters, modulo the two real scalings already counted in $\Rho$). The count is consistent, and the parametrisation is the exponential chart of the next section.

## What Is True and What Is Not

### The Claim That Is Usually Made

It is often said that the exponential of the traceless algebra is onto the unit-norm group. The claim is false, and this article states the correct version because the block uses the exponential constantly and a reader deserves to know where it stops.

### The Counterexample

Let

$$
\tilde A=-e_t+\tilde N,\qquad \tilde N\neq0,\qquad \tilde N^{2}=0,
$$

the image of $\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$. Then $\tilde A$ has unit norm, since $\langle\tilde A\rangle_{\natural}=1$, so $\tilde A\in G$. Suppose $\exp(\tilde X)=\tilde A$ with $\mathrm{Sc}\tilde X=0$.

- If $\tilde X$ has distinct eigenvalues, $\exp(\tilde X)$ has distinct eigenvalues. But $\tilde A$'s eigenvalues are equal, both $-1$. Contradiction.
- So $\tilde X$ has equal eigenvalues; being scalar-free, both are zero; so $\tilde X^{2}=0$ and $\exp(\tilde X)=e_t+\tilde X$. But $\tilde A=-e_t+\tilde N$ has trace $-2$, while $e_t+\tilde X$ has trace $2$. Contradiction.

Both cases exhausted, $\tilde A$ is not an exponential. The argument uses only the trace and the eigenvalues, and it is exact.

### The Correct Statement

$$
\exp\bigl(\mathfrak{sl}(2,\mathbb{C})\bigr)=SL(2,\mathbb{C})\setminus\{-e_t+\tilde N:\tilde N^{2}=0,\ \tilde N\neq0\}.
$$

The image is the group minus a single conjugacy class. Everything else is an exponential:

- elements with distinct eigenvalues are exponentials, by choosing the two logarithms of the eigenvalues with sum zero;
- $\pm e_t$ are exponentials, of $0$ and of $\operatorname{diag}(i\pi,-i\pi)$;
- $e_t+\tilde N$ is the exponential of the nilpotent $\tilde N$;
- and the class $-e_t+\tilde N$ is precisely the class where the two bullets of the counterexample overlap, and it is the only exclusion.

### The Price and the Repair

The exclusion is not a disaster, for three reasons.

- **Every element is a product of two exponentials.** $\tilde A=(-e_t)\cdot(e_t-\tilde N)$, and $-e_t$ and $e_t-\tilde N$ are both exponentials. So the group is generated by the image, and the block's uses of the exponential are always of the form "a coordinate patch", never "the unique logarithm".
- **The excluded class is a set of measure zero in the group.** It is a single conjugacy class, so it cannot be met by a generic computation. A numerical logarithm will fail on it, and it will fail visibly, because the series is trying to converge to a matrix it cannot reach.
- **The classical statement is about the full algebra.** See the next subsection.

### The Full Algebra's Exponential Is Onto

$$
\exp:\ \mathbb{B}\longrightarrow\mathbb{B}^{\times}
$$

is **onto**. The reason is the classical theorem that every nonsingular complex matrix has a complex logarithm: a matrix over $\mathbb{C}$ is a logarithm's exponential if and only if it is nonsingular. Since $\mathbb{B}\cong M_2(\mathbb{C})$ as algebras and the exponential is transported by an algebra isomorphism, the statement holds for biquaternions.

So the menu's "formula $\tilde Q=\exp(\tilde W)$ for a general non-null biquaternion" is true, and the correct reading is that $\tilde W$ ranges over the **eight-dimensional** algebra and not over the six-dimensional Lie algebra. The two extra dimensions are the scalar part, and the scalar part is exactly what the excluded class needs: the trace of the logarithm is free, and the obstruction above was a trace obstruction.

| map | domain | image | statement |
|---|---|---|---|
| $\exp$ on $\mathbb{B}$ | real dimension $8$ | all of $\mathbb{B}^{\times}$ | onto |
| $\exp$ on $\mathfrak{sl}$ | real dimension $6$ | $G$ minus one class | not onto |
| $\exp$ on $\mathfrak{p}$ (boosts) | real dimension $3$ | the boosts | onto, injectively |
| $\exp$ on $\mathfrak{k}$ (rotations) | real dimension $3$ | $SU(2)$ | onto, $2\pi$-periodic |

## The Logarithm and Its Branches

### The Matrix Logarithm

A logarithm of $\tilde Q$ is any $\tilde W$ with $\exp(\tilde W)=\tilde Q$. Two logarithms differ by an element of the period lattice: if $\exp(\tilde W_1)=\exp(\tilde W_2)$ then $\tilde W_1-\tilde W_2$ commutes with $\tilde W_1$ and has eigenvalues in $2\pi i\mathbb{Z}$. The set of logarithms is therefore discrete and infinite, and a branch is a choice of one in each connected component.

### The Principal Branch

The principal branch is the one whose eigenvalues' imaginary parts lie in $(-\pi,\pi]$, computed by the Schur–Padé algorithm. It is holomorphic on the complement of the closed negative real axis in the eigenvalue plane, and it is the branch a numerical library returns. On the group of unit norm it is the branch that maps $G$ into the strip $\lvert\operatorname{Im}\Rho\rvert<\pi$, which is why a numerical logarithm of a boost of rapidity above $2\pi$ is not automatically the one a reader expects.

### The Trace and the Branch

The trace of the logarithm is fixed only modulo $2\pi i$:

$$
\operatorname{tr}\log\mathsf M_2(\tilde Q)=\log\langle\tilde Q\rangle_{\natural}+2\pi i k .
$$

That freedom is precisely what allows the full algebra's exponential to be onto while the scalar-free one is not: a logarithm with any trace can be shifted to trace zero only if the shift does not change the exponential, and the shift by $2\pi i\,\mathrm{diag}(1,0)$ changes it. The obstruction is at once a trace statement and a conjugation statement, and they are the same statement.

### The Reconstruction Check

For a rotation of $0.7$, a boost of rapidity $0.9$, a general element built as the product of the two, and a random element of the group away from the excluded class, computing the logarithm on the principal branch and exponentiating returns the element to $10^{-15}$. The excluded class fails, as it must.

## The Cut Locus

### The Criterion

The differential of the exponential at $\tilde X$ is

$$
d(\exp)_{\tilde X}=e^{\tilde X}\cdot\frac{e^{\operatorname{ad}_{\tilde X}}-1}{\operatorname{ad}_{\tilde X}},
$$

so it is singular exactly where $\operatorname{ad}_{\tilde X}$ has an eigenvalue in $2\pi i\mathbb{Z}\setminus\{0\}$. For scalar-free $\tilde X$ the eigenvalues of $\operatorname{ad}_{\tilde X}$ are $0,\pm2\Rho$, so the criterion becomes

$$
2\Rho\in2\pi i\mathbb{Z}\setminus\{0\},
\qquad\text{that is}\qquad \Rho=i\pi k,\ k\in\mathbb{Z}\setminus\{0\}.
$$

### The Shape

The singular set is a union of spheres in the algebra:

- $\Rho=i\pi(2k+1)$ is the sphere of generators whose exponential is $-e_t$; every point of it maps to the same element, so the chart collapses a two-sphere to a point;
- $\Rho=2\pi i k$ is the sphere whose exponential is $+e_t$;
- between them the chart is a local diffeomorphism.

This is the algebra-level picture of the fibre computed in *The Group of Unit-Norm Biquaternions*, and the numbers agree: a rotation by $2\pi$ in the physical angle is $\Rho=\pi$, i.e. the first singular sphere.

### The Consequence for Coordinates

A coordinate system built from the exponential is one-to-one only outside the cut locus and only after a choice of branch. The block's rule: exponential coordinates are used for *paths* and for *small* elements, and every global statement is made with the Cartan coordinates of the next section.

## Coordinate Systems and Their Ranges

### Exponential Coordinates

Six real numbers, the real and imaginary parts of the three complex components of $\tilde X$. Their range is the strip where the chart is injective, and their image is the group minus the excluded class and minus the identified spheres. This is the chart of a Lie algebra to its group in the usual sense, and it is the one used for infinitesimal arguments.

### Cartan Coordinates

$$
\tilde U=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

six numbers $(\theta_{\mathrm{rpd}},\vec u_{\mathrm b};\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ with the directions on spheres. The ranges are

| coordinate | range | what its endpoints mean |
|---|---|---|
| $\theta_{\mathrm{rpd}}$ | $[0,\infty)$ | $0$ is the identity, $\infty$ is the speed of light |
| $\vec u_{\mathrm b}$ | $S^{2}$ | the boost axis |
| $\theta_{\mathrm{axr}}$ | $[0,2\pi]$ | $2\pi$ returns $-e_t$ |

and the pair $(\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ covers $SU(2)$ once at $\theta_{\mathrm{axr}}\in[0,2\pi)$ except for the endpoint. Positivity of the Hermitian factor is what makes the pair unique, and *A Frame Is a Boost Times a Rotation: The Cartan Word* proves that it is.

### What the Coordinates Are Not

Cartan coordinates are not exponential coordinates: the product of two exponentials is not the exponential of the sum, because $[\mathfrak{k},\mathfrak{p}]\neq0$. They are a *global* product decomposition of the group, and that is a different theorem from the local invertibility of the exponential.

## Summary

The exponential of a scalar-free biquaternion has the closed form $\exp(\tilde X)=\cos\Rho+\frac{\sin\Rho}{\Rho}\tilde X$ with $\Rho^{2}=\mathrm{Sc}(\tilde X^{2})$, which is a rotation when $\Rho$ is real and a boost when $\Rho$ is imaginary; the two forms in the menu are its two ranges. Its determinant is $e^{2\,\mathrm{Sc}\tilde X}$, so it lands in the unit-norm group. It is **not** onto that group: it misses exactly the conjugacy class of $-e_t+\tilde N$ with $\tilde N$ a nonzero nilpotent, and the proof is the eigenvalue-and-trace argument above. Every element is nevertheless a product of two exponentials, and the exponential of the full eight-dimensional algebra *is* onto the group of invertibles, because every nonsingular complex matrix has a logarithm and the extra scalar direction supplies the trace. The chart's singular locus is the union of spheres $\Rho=i\pi k$, where it collapses to $\pm e_t$. The block uses exponential coordinates for paths and Cartan coordinates for global statements.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde X$ | a scalar-free element of the algebra |
| $\Rho^{2}=\mathrm{Sc}(\tilde X^{2})=-\langle\tilde X\rangle_{\natural}$ | the complex modulus of the generator |
| $\hat{\tilde X}$ | an invertible element generator, $\hat X^{2}=\pm e_t$ |
| $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{axr}}$ | rapidity and rotation angle, twice the arguments |
| $\mathfrak{k}$, $\mathfrak{p}$ | rotations and boosts |
| $\tilde N$ | a nilpotent, $\tilde N^{2}=0$, $\tilde N\neq0$ |
| $\operatorname{ad}_{\tilde X}$ | the adjoint map $[\tilde X,\cdot]$ |

## Further Reading

- R. A. Horn and C. R. Johnson, *Topics in Matrix Analysis*, Cambridge University Press, 1991 — the matrix exponential, the determinant formula, and the logarithm's existence for nonsingular matrices.
- W. J. Culver, "On the existence and uniqueness of the real logarithm of a matrix", *Proceedings of the American Mathematical Society* **17** (1966) 1146–1151 — the theorem that a complex matrix has a logarithm exactly when it is nonsingular.
- W. Rossmann, *Lie Groups: An Introduction through Linear Groups*, Oxford University Press, 2002 — the differential of the exponential, the cut locus and the divided-difference formula.
- *The Group of Unit-Norm Biquaternions* — the target group, its dimension and its exponential chart read as a chart.
- *A Frame Is a Boost Times a Rotation: The Cartan Word* — the global product decomposition that the coordinates of the last section describe.
