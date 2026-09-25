
# __Split-Quaternion Elementary Functions__

## Introduction

This article develops the elementary functions of a split-quaternion variable: the exponential, the trigonometric and hyperbolic functions, the logarithm, the power functions and the roots of unity. It records the domains, the periodicity, the identities that hold and the identities that fail, and it compares the situation with the quaternion and split-complex cases.

The split-quaternion algebra, its norm form, its conjugation, its idempotents and its split-complex subalgebras are assumed from *Split-Quaternion Algebra*; the units and the three-way classification from *Split-Quaternion Norm and Invertibility*; the roots of $\xi^2=-1$ from *Split-Quaternion Roots of Minus One*; the null cone and the nilpotents from *Split-Quaternion Zero Divisors*; the matrix model from *Split-Quaternion Matrix Representations*; and the convergence of power series from *Split-Quaternion Analysis*, §*Power Series and Analytic Functions*. The exponential map of a Lie group is that of *The Lie Algebra and the Exponential Map*; the elementary functions of the division-algebra case are those of *Quaternion Special Functions*, and of the two-dimensional hyperbolic case those of *Split-Complex Special Functions*. Nothing physical is invoked.

## The Exponential

**Definition.** The **exponential** is

$$
\exp x = \sum_{n \geq 0} \frac{x^n}{n!},
$$

a series with real coefficients convergent for every $x$ by *Split-Quaternion Analysis*, §*Power Series and Analytic Functions*.

**Theorem (The Exponential of a Vector).** For $v \in V$ the square $v^2 = -N(v)$ is a real scalar, and

$$
\exp v = c_0(\lambda) + c_1(\lambda)\, v, \qquad \lambda = N(v),
$$

where

$$
c_0(\lambda) = \begin{cases} \cos\sqrt{\lambda}, & \lambda > 0,\\ 1, & \lambda = 0,\\ \cosh\sqrt{-\lambda}, & \lambda < 0,\end{cases}
\qquad
c_1(\lambda) = \begin{cases} \dfrac{\sin\sqrt{\lambda}}{\sqrt{\lambda}}, & \lambda > 0,\\ 1, & \lambda = 0,\\ \dfrac{\sinh\sqrt{-\lambda}}{\sqrt{-\lambda}}, & \lambda < 0.\end{cases}
$$

In every case $N(\exp v) = 1$, so $\exp v$ lies in the norm-one group $U$.

**Proof.** For $v \in V$ one has $v^2 = -N(v)$ because the generators anticommute, as in the multiplication table of (*Split-Quaternion Algebra*, §*The Multiplication Table*). If $v^2 = -\lambda$ is a scalar then the even and odd parts of the series are the power series of the displayed functions, by the standard reduction of a power series of an element with scalar square. The norm: $N(\exp v) = c_0^2 + c_1^2 N(v)$ because $1$ and $v$ are orthogonal, and the identity $\cos^2 + \sin^2 = 1$ or $\cosh^2 - \sinh^2 = 1$ gives $1$ in all three cases; the nilpotent case gives $N(1+v) = 1$. $\square$

**Theorem (Factoring the Exponential).** For $x = a + v$ with $a$ real and $v \in V$,

$$
\exp x = e^{a} \exp v ,
$$

and hence

$$
N(\exp x) = e^{2a} > 0 .
$$

The exponential is therefore never zero and always invertible, its norm is $e^{2a}$, and it maps $\mathbb{H}_{\mathrm{s}}$ into the open set $\{N > 0\}$ of units.

**Proof.** The scalar $a$ is central and commutes with $v$, so the series splits, $\exp(a+v) = e^a\exp v$; the norm follows from multiplicativity and the theorem above. $\square$

**Theorem (The Image of the Exponential).** The image is

$$
\exp(\mathbb{H}_{\mathrm{s}}) = \big\{x : N(x) > 0,\ \operatorname{Sc}(x) > -\sqrt{N(x)}\big\} \cup \{x \in \mathbb{R} : x < 0\},
$$

the open set on which the norm is positive and the scalar part exceeds $-\sqrt{N}$, together with the negative scalar line. Equivalently, it is the set $\{N>0,\ \operatorname{Sc} \geq -\sqrt N\}$ with the elements $a + v$ removed for which $a < 0$ and $v \neq 0$ is nilpotent, these being exactly the non-scalar elements with $\operatorname{Sc} = -\sqrt N$.

In particular the exponential is not surjective onto the units: the elements of $\{N>0\}$ with $\operatorname{Sc}(x) < -\sqrt{N(x)}$ are not exponentials, the element $x = -3+2e_3$, with $N(x) = 9-4 = 5$ and $\operatorname{Sc}(x) = -3 < -\sqrt5$, being an example, and neither are the boundary elements: the element $x = -1+e_1+e_2$, with $N(x) = 1$ and $\operatorname{Sc}(x) = -1 = -\sqrt{N(x)}$, is one of them.

**Proof.** Under $\Phi$ the exponential is the exponential of $M_2(\mathbb{R})$, the norm is the determinant and twice the scalar part is the trace, so the question is the image of the real exponential of a $2\times2$ matrix. If $A = \exp X$ is real, then $\det A = e^{\operatorname{tr}X} > 0$, and each eigenvalue of $A$ is the exponential of an eigenvalue of $X$; a negative eigenvalue of $A$ therefore comes from an eigenvalue $\alpha \pm \mathrm{i}\pi$ of $X$ with an odd multiple of $\pi$, and the conjugate pair forces $X$, hence $A$, to be diagonalisable with both eigenvalues equal to $-e^\alpha$, so that $A = -e^\alpha I$. A non-scalar element of the image thus has no negative eigenvalue, which for a positive determinant is exactly $\operatorname{tr}A > -2\sqrt{\det A}$. Conversely, if $\det A > 0$ and $\operatorname{tr}A > -2\sqrt{\det A}$, then either the eigenvalues of $A$ are real and positive, when the logarithm exists by the series of the logarithms of the eigenvalues, or they are a non-real conjugate pair $\alpha \pm \mathrm{i}\beta$, when $X = sI + t(A - \alpha I)$ with $t\beta \in (0,\pi)$ determined by $\tan(t\beta) = \beta/\alpha$ and $e^s\cos(t\beta) = \alpha$ satisfies $\exp X = A$, the inequality being automatic in this case; and the negative scalars are attained, $-\mu I = \exp((\log\mu)I + \pi\xi)$ for every root $\xi$ of $-1$. Finally, a non-scalar matrix with $\det A > 0$ and $\operatorname{tr}A = -2\sqrt{\det A}$ has the negative eigenvalue $-\sqrt{\det A}$ repeated with a single Jordan block, so its commutant is $\{pI + qN\}$ with $N$ nilpotent and $\exp(pI+qN) = e^p(I+qN)$ has the positive eigenvalue $e^p$; such a matrix is therefore not an exponential. Translating back gives $N > 0$, $\operatorname{Sc} > -\sqrt N$, and the boundary described by $\operatorname{Sc} = -\sqrt N$, that is $N(\operatorname{Vec}x) = 0$ with $\operatorname{Sc}(x) < 0$. $\square$

**Theorem (The Kernel of the Exponential).** The solutions of $\exp y = 1$ are

$$
y = 0 \quad\text{or}\quad y = 2\pi k\,\xi \quad (k \in \mathbb{Z}\setminus\{0\}, \ \xi \in V, \ N(\xi) = 1).
$$

Hence the kernel of the exponential is the union of the scaled copies $2\pi k\,\Sigma$ of the sphere $\Sigma$ of the roots of $-1$, together with the origin; the exponential is not injective and is periodic along the whole root set of $-1$.

**Proof.** Write $y = a + v$. From $\exp y = e^a\exp v = 1$ and $N(\exp y) = e^{2a}$ one gets $a = 0$, and then $\exp v = 1$ with the three cases of the first theorem: for $\lambda = 0$ one needs $1 + v = 1$, so $v = 0$; for $\lambda > 0$ one needs $\cos\sqrt{\lambda} = 1$ and $\sin\sqrt{\lambda} = 0$, so $\sqrt{\lambda} = 2\pi k$ with $k \neq 0$; for $\lambda < 0$ one needs $\cosh\sqrt{-\lambda} = 1$, which forces $v = 0$. The elements with $\lambda = (2\pi k)^2$ and $N(v) > 0$ are exactly the multiples $2\pi k\xi$ of the roots of $-1$ by *Split-Quaternion Roots of Minus One*, §*The Equation and the Reduction to the Vector Subspace*. $\square$

**Corollary (The Two Real Periods).** Along a commutative subalgebra generated by an element of square $-1$ the exponential has period $2\pi$; along a split-complex subalgebra there is no real period, and the exponential of a split-complex element is injective on each branch of the positive cone. The two behaviours coexist in the algebra and must not be interchanged.

**Proof.** The first is the case $\xi^2=-1$ of the kernel; the second is the formula $\exp(a + c e_2) = e^a(\cosh c + e_2\sinh c)$, whose components $e^{a\pm c}$ are injective in the two null coordinates, with no periodicity. $\square$

## Trigonometric and Hyperbolic Functions

**Definition.** The **hyperbolic** and **trigonometric** functions are the series

$$
\cosh x = \sum_{n \geq 0} \frac{x^{2n}}{(2n)!}, \qquad \sinh x = \sum_{n \geq 0}\frac{x^{2n+1}}{(2n+1)!},
$$

$$
\cos x = \sum_{n \geq 0} (-1)^n \frac{x^{2n}}{(2n)!}, \qquad \sin x = \sum_{n \geq 0} (-1)^n \frac{x^{2n+1}}{(2n+1)!},
$$

all convergent for every $x$. The exponential splits by parity: $\exp x = \cosh x + \sinh x$.

**Theorem (The Values on a Vector).** For $v \in V$ with $\lambda = N(v)$,

$$
\cos v = \begin{cases} \cosh\sqrt{\lambda}, & \lambda > 0\\ 1, & \lambda = 0\\ \cos\sqrt{-\lambda}, & \lambda < 0\end{cases}, \qquad
\sin v = \begin{cases} \dfrac{\sinh\sqrt{\lambda}}{\sqrt{\lambda}}\, v, & \lambda > 0\\ v, & \lambda = 0\\ \dfrac{\sin\sqrt{-\lambda}}{\sqrt{-\lambda}}\, v, & \lambda < 0\end{cases},
$$

and the hyperbolic functions are obtained by the same reduction with the two cases interchanged:

$$
\cosh v = \begin{cases} \cos\sqrt{\lambda}, & \lambda > 0\\ 1, & \lambda = 0\\ \cosh\sqrt{-\lambda}, & \lambda < 0\end{cases}, \qquad
\sinh v = \begin{cases} \dfrac{\sin\sqrt{\lambda}}{\sqrt{\lambda}}\, v, & \lambda > 0\\ v, & \lambda = 0\\ \dfrac{\sinh\sqrt{-\lambda}}{\sqrt{-\lambda}}\, v, & \lambda < 0\end{cases}.
$$

The two families are therefore interchanged by a change of sign of the norm of the argument: for the elliptic direction, with $\lambda > 0$, the trigonometric series of $v$ gives the hyperbolic values and conversely, because $v^2 = -\lambda$ and the sign of the square is what the parity terms of the series see. A trigonometric identity read off one subalgebra does not transport to another.

**Proof.** The reduction of the even and odd series is the same as for the exponential, and the explicit cases are read from the sign of $\lambda$. $\square$

**Theorem (The Identities That Hold and the Identities That Fail).** The identities

$$
\exp x \exp(-x) = 1, \qquad \overline{\exp x} = \exp \bar{x}, \qquad \cos^2 v + \sin^2 v = 1, \qquad \cosh^2 v - \sinh^2 v = 1
$$

hold, the last two for every $v \in V$ with $N(v) \neq 0$, in both signs of the norm. The addition formulas

$$
\exp(x+y) = \exp x \exp y, \qquad \sin(x+y) = \sin x\cos y + \cos x\sin y
$$

hold when $xy = yx$ and fail in general; the failure is measured by the Baker–Campbell–Hausdorff series in the commutator.

**Proof.** The first identity is the series for $x$ and $-x$, which commute; the second holds because the coefficients are real and conjugation is an anti-automorphism; the Pythagorean identities are computed from the scalar square of $v$. The addition formulas hold for commuting elements by the binomial theorem, and fail when the binomial expansion does not collapse, as it does not for the anticommuting generators. $\square$

## The Logarithm

**Definition.** The **logarithm** is the inverse of the exponential on a domain on which the exponential is injective; on the dense open set where the power series of the matrix logarithm converges it is

$$
\log x = \log \sqrt{N(x)} + \log\big(x/\sqrt{N(x)}\big) ,
$$

the second term being an element of $V$ obtained from the matrix logarithm of the traceless part.

**Theorem (Existence and Branch).** The derivative of the exponential at $x$ is invertible if and only if no two eigenvalues of the matrix model $\Phi(x)$ differ by a nonzero multiple of $2\pi\mathrm{i}$. The eigenvalues of $\Phi(x)$ are $\operatorname{Sc}(x) \pm \sqrt{-N(\operatorname{Vec} x)}$, so they are complex conjugate when $N(\operatorname{Vec} x) > 0$ and real when $N(\operatorname{Vec} x) \leq 0$. The condition therefore reads

$$
N(\operatorname{Vec} x) \notin \{(\pi k)^2 : k = 1, 2, 3, \dots\},
$$

and on the open set where it holds the exponential is a local diffeomorphism with a smooth local inverse, mapping the open set $\{N>0,\ \operatorname{Sc} > -\sqrt N\}$ onto itself. The failure set is exactly

$$
\big\{x = a + v : N(v) = (\pi k)^2,\ k \geq 1\big\},
$$

on which $\Phi(x)$ has the eigenvalues $a \pm \pi k\,\mathrm{i}$ and the exponential folds: the simplest failure point is $x = \pi e_1$, where $\exp(\pi e_1) = -1$. On the norm-one group the logarithm takes values in $V$, $\log(1+v) = v$ for every nilpotent $v \in V$ of square zero, and the logarithm is multivalued exactly at the nonzero real scalars and at the elements with $N(\operatorname{Vec}x) > 0$, whose matrix model has a non-real pair of eigenvalues: at those points the infinitely many values differ by the kernel of the preceding section, while at the elements whose matrix model has real positive eigenvalues the value is unique, the logarithm being a polynomial in the element there.

**Proof.** The eigenvalues of $\Phi(x)$ have sum $2\operatorname{Sc}(x)$ and product $N(x)$, so they are $\operatorname{Sc}(x) \pm \sqrt{\operatorname{Sc}(x)^2 - N(x)}$ with $\operatorname{Sc}(x)^2 - N(x) = -N(\operatorname{Vec}x)$; the derivative of the exponential of a $2\times2$ matrix is singular exactly when the matrix has two eigenvalues differing by a nonzero multiple of $2\pi\mathrm{i}$, the divided difference of the exponential being zero in that case. In the real case the difference of the eigenvalues is $2\sqrt{-N(\operatorname{Vec}x)}$, real and nonzero unless $N(\operatorname{Vec}x) = 0$, where the eigenvalues coincide and the derivative is still invertible; in the complex case the difference is $2\mathrm{i}\sqrt{N(\operatorname{Vec}x)}$, which is a nonzero multiple of $2\pi\mathrm{i}$ exactly when $\sqrt{N(\operatorname{Vec} x)} = \pi k$. At $x = \pi e_1$ one has $\exp(\pi e_1) = \cos\pi + e_1\sin\pi = -1$, so the value is a negative scalar and two distinct points of the domain share it, which is the folding. The nilpotent case is the finite series $\log(1+v) = v - v^2/2 + \dots = v$, and the multivaluedness at the scalars and at the elements with timelike vector part is the ambiguity of the arguments of the eigenvalues of the matrix model, the various values differing by multiples of $2\pi$ times a complex structure that commutes with the logarithm. $\square$

**Corollary (The Logarithm on the Split-Complex Plane).** On the positive component of the split-complex plane, in the null coordinates $x = p\,n_+ + q\,n_-$ with $n_\pm = \tfrac12(1\pm e_2)$ and $p,q > 0$,

$$
\log x = (\log p)\, n_+ + (\log q)\, n_- ,
$$

which shows again the absence of a real period in the split directions and the presence of the two independent real logarithms.

**Proof.** Apply the exponential formula of the split-complex subalgebra in the null basis. $\square$

## Power Functions and Roots of Unity

**Definition.** For real $\alpha$ and $x$ in the domain of a branch of the logarithm, the **power** is $x^\alpha = \exp(\alpha\log x)$; the **$n$-th roots** are the solutions of $y^n = x$.

**Theorem (The Split Roots of Unity).** The elements $u_+ + \lambda u_-$ with $\lambda \in \{\pm 1\}$ satisfy

$$
(u_+ + \lambda u_-)^n = u_+ + \lambda^n u_-, \qquad (\lambda = \pm 1),
$$

so $1$ is a root of unity of every order, while $e_2 = u_+ - u_-$ has $e_2^2 = 1$ and is a root of unity of order two; the reflection $e_3$ is likewise of order two. The roots of unity in the elliptic plane are the elements $\cos\theta + \xi\sin\theta$ with $\xi^2 = -1$ and $\theta$ a rational multiple of $2\pi$, in accordance with the kernel of the exponential.

**Proof.** The first identity follows from $u_+u_- = 0$ and $u_\pm^2 = u_\pm$ by the binomial theorem, the cross terms vanishing. The order-two statements are $e_2^2 = e_3^2 = 1$, and the elliptic elements are the one-parameter subgroups of *Split-Quaternion Rotations and the Lorentz Group*, §*Elliptic and Hyperbolic One-Parameter Subgroups*. $\square$

**Corollary (Roots of Unity of Order Two and the Power Functions).** The solutions of $y^2 = 1$ are $y = \pm 1$ together with the elements $y = 2p - 1$ for $p$ a rank-one idempotent; equivalently they are the reflections, that is the matrices conjugate to $\operatorname{diag}(-1,1)$ in the matrix model, a two-dimensional family. The power functions inherit the ambiguity of the logarithm: $x^{1/n}$ is generally multiple-valued, and two values differ by a root of unity.

**Proof.** $y^2 = 1$ is $(y-1)(y+1) = 0$; in the matrix model the minimal polynomial of $\Phi(y)$ divides $(t-1)(t+1)$, so $\Phi(y)$ is diagonalisable with eigenvalues in $\{\pm1\}$; if $y \neq \pm1$ it has both eigenvalues and $p = (y+1)/2$ is a rank-one idempotent, whose family is two-dimensional as computed in *Split-Quaternion Zero Divisors*, §*The Two Families in the Algebra*. The multivaluedness of the power is the multivaluedness of the logarithm of the preceding section. $\square$

## Non-Commutativity and the One-Variable Case

**Theorem (One-Variable Case).** If $x$ lies in a commutative subalgebra of $\mathbb{H}_{\mathrm{s}}$, that is in one of the planes $\operatorname{span}\{1,\xi\}$ with $\xi^2 = \pm 1$, then all the elementary identities of the real and split-complex one-variable calculus hold for $x$, with the sine and cosine replaced by the hyperbolic functions when $\xi^2 = +1$.

**Proof.** In a commutative subalgebra the binomial theorem applies to the series, and the subalgebra is isomorphic to $\mathbb{C}$ or to $\mathbb{D}$ according to the sign of $\xi^2$. $\square$

**Theorem (The General Case).** For general $x,y$ the identities fail: $\exp(x+y) \neq \exp x\exp y$ unless $xy = yx$, and the failure is exactly the Baker–Campbell–Hausdorff correction. The conjugation however always behaves well: $\overline{\exp x} = \exp\bar{x}$, $N(\exp x) = e^{2\operatorname{Sc}(x)}$, and $\exp x$ is a unit for every $x$.

**Proof.** The failure of the addition formula is the non-commutativity of the series; the conjugation identity and the norm formula are the theorems above. $\square$

**Corollary (The Trap of the Split-Complex Case).** In the split-complex plane the exponential is $\exp(a + ce_2) = e^a(\cosh c + e_2\sinh c)$ and its image is one component of the positive cone, not the whole of it; the corresponding statement in the split-quaternion algebra is the theorem on the image of the exponential, and neither statement should be read off the other. In particular the sinusoidal and hyperbolic parts of $\exp v$ for $v \in V$ depend on the sign of $N(v)$, so an identity valid for one sign of the norm is generally false for the other.

**Proof.** The split-complex formula is *Split-Complex Special Functions*, and the general statement is the theorem on the exponential of a vector above. $\square$

## Summary of the Identities

| Object | Value or identity | Domain or hypothesis |
|---|---|---|
| $\exp(a+v)$ | $e^a\exp v$ | $a$ real, $v \in V$ |
| $\exp v$ | $c_0(N(v)) + c_1(N(v))v$ | all $v \in V$ |
| $\exp v$ | $1 + v$ | $N(v) = 0$ |
| $N(\exp x)$ | $e^{2\operatorname{Sc}(x)}$ | all $x$ |
| $\exp(\mathbb{H}_{\mathrm{s}})$ | $\{N>0,\ \operatorname{Sc} > -\sqrt{N}\} \cup \{x < 0\}$ | image of the exponential |
| kernel of $\exp$ | $\{0\} \cup 2\pi\mathbb{Z}\cdot\Sigma$ | $\Sigma$ the root set of $-1$ |
| $\cos^2v+\sin^2v$ | $1$ | $v \in V$, $N(v) \neq 0$ |
| $\cosh^2v-\sinh^2v$ | $1$ | $v \in V$, $N(v) \neq 0$ |
| $\overline{\exp x}$ | $\exp\bar{x}$ | all $x$ |
| $\exp(x+y)$ | $\exp x\exp y$ | if and only if $xy = yx$ |
| $\log(1+v)$ | $v$ | $v$ nilpotent |
| $(u_+ + \lambda u_-)^n$ | $u_+ + \lambda^nu_-$ | $\lambda = \pm1$ |

## Summary

The exponential converges everywhere and factors as $\exp(a+v) = e^a\exp v$, with $\exp v$ given in closed form by the functions $c_0$ and $c_1$ of the norm of $v$; it is never zero, its norm is $e^{2\operatorname{Sc}(x)}$, and its image is the set of elements of positive norm whose scalar part exceeds $-\sqrt{N}$ together with the negative scalars, so it is not surjective onto the units. Its kernel is the origin together with the scaled copies $2\pi k\Sigma$ of the sphere of the roots of $-1$; the exponential has a real period along every direction that squares to $-1$ and no real period in the split directions.

The trigonometric and hyperbolic functions are the parity parts of the exponential and reduce on the vector subspace to the classical functions of $\sqrt{|N(v)|}$, with sine and cosine interchanged with the hyperbolic functions when the sign of the norm changes; the Pythagorean identities hold, the addition formulas hold exactly for commuting arguments and fail otherwise, the failure being the Baker–Campbell–Hausdorff correction. The conjugation and the norm commute with the exponential in the expected way. The logarithm exists on the image of the exponential, that is where the scalar part exceeds $-\sqrt{N}$ or where the element is a negative scalar; it is $v$ on the nilpotents, it is a pair of real logarithms in the split-complex null coordinates, and it is multivalued exactly at the nonzero real scalars and at the elements with $N(\operatorname{Vec}x) > 0$, the several values differing by the kernel of the exponential. The roots of unity include the split elements $u_+ + \lambda u_-$ and the elliptic elements; the power functions inherit the ambiguity of the logarithm. The comparison with the quaternion and split-complex cases is by way of the sign pattern of the form only, and identities must not be transported from one system to another.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\exp$, $\log$ | the exponential and its inverse branch | this article |
| $c_0(\lambda)$, $c_1(\lambda)$ | the coefficient functions of $\exp v$ | this article |
| $\Sigma$ | the sphere of the roots of $-1$ | *Split-Quaternion Roots of Minus One* |
| $\cos$, $\sin$, $\cosh$, $\sinh$ | the trigonometric and hyperbolic series | this article |
| $n_\pm = \tfrac12(1\pm e_2)$ | the null basis of the split-complex plane | *Split-Quaternion Algebra* |
| $x^\alpha = \exp(\alpha\log x)$ | the power function | this article |
| $u_+ + \lambda u_-$ | the split roots of unity | this article |
| BCH | the Baker–Campbell–Hausdorff correction | this article |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map, its kernel and its image for the classical groups.
- Roger Carter, Graeme Segal and Ian Macdonald, *Lectures on Lie Groups and Lie Algebras* (Cambridge University Press, 1995), for the exponential of a matrix algebra and the trace condition for $\mathrm{SL}_2(\mathbb{R})$.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, 2008), for the matrix exponential, the logarithm and the power functions, and their branches.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the elementary functions of the low-dimensional Clifford algebras and the role of the sign pattern.
