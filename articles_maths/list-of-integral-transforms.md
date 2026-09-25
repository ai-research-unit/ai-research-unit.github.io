
# __List of Integral Transforms__

## Introduction

This article lists the integral transforms the corpus constructs and inverts. An integral transform is an operation that carries a function to a new function by integrating it against a kernel, and a row below names one transform, records the kernel that defines it and the inversion theorem that recovers the function, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The transforms are grouped by the family that introduces them: the Fourier transforms, on the line, on the circle, on a finite abelian group and on a locally compact abelian group; the Laplace and Mellin transforms of a half-line and of a multiplicative group; the singular and geometric transforms — the Hilbert and Riesz transforms, the Radon, Hankel and wavelet transforms; and the transforms attached to a group representation, among them the Gelfand and spherical transforms. The rows that record the boundary of the theory — a transform that does not converge absolutely, an inversion that needs a summability method, a kernel that fails the admissibility condition — stand beside the transforms as non-examples.

## The Fourier Family

| Object | Its kernel and its inversion theorem | Introduced in |
|---|---|---|
| the Fourier transform on $\mathbb R^n$ | kernel $e^{-2\pi i\langle x,\xi\rangle}$; inversion $\hat f \mapsto f$ under $f \in L^1$ with $\hat f \in L^1$, and the $L^2$ form by Plancherel | *Fourier Analysis on Euclidean Spaces* |
| the Fourier series on the circle | kernel $e^{in\theta}$; inversion by the convergence of the partial sums, and by the Fejér and Cesàro means | *Real Harmonic Analysis*; *Fourier Analysis on Euclidean Spaces* |
| the Fourier transform on a finite abelian group | the characters as kernel; discrete inversion by the orthogonality relations | *Harmonic Analysis on Groups* |
| the Fourier transform on a locally compact abelian group | the characters of $\hat G$ as kernel; inversion and Plancherel for the Haar measure | *Harmonic Analysis on Groups* |
| the Fourier transform on a compact group | the matrix coefficients of the irreducible representations as kernel; inversion by the Peter–Weyl theorem | *Analysis on Compact Groups* |
| the Fourier transform on the adeles | the additive characters as kernel; inversion and the Poisson summation formula | *Adelic Analysis* |
| the Fourier transform on a hypercomplex system | the Fourier kernel of the system; inversion for the complex, quaternion, split-complex and dual-number planes | *Harmonic Analysis over Hypercomplex Systems* |

## The Laplace and Mellin Family

| Object | Its kernel and its inversion theorem | Introduced in |
|---|---|---|
| the Laplace transform | kernel $e^{-st}$; inversion by the Bromwich integral, and the resolvent form $R(\lambda,A) = \int_0^\infty e^{-\lambda t}T(t)\,dt$ | *Semigroups and Evolution Equations*; *Split-Complex Harmonic Analysis*; *Markov Chains and Processes* |
| the Fourier–Stieltjes transform $\hat\mu(\chi) = \int_G\overline{\chi(x)}\,d\mu(x)$ | the transform of a finite measure on a group, recovering the classical transform for $G = \mathbb R^n$; inversion by Bochner's theorem and the uniqueness of the transform | *Harmonic Analysis on Groups*; *Noncommutative Harmonic Analysis* |
| the Mellin transform | kernel $x^{s-1}$; inversion on a vertical line, and its identification with the Fourier transform in logarithmic coordinates | *Complex Harmonic Analysis* |
| the Mellin convolution and its inversion | the multiplicative convolution and its transform rule $\mathcal M(f \star g) = \mathcal M f\,\mathcal M g$ | *Complex Harmonic Analysis* |

## The Singular and Geometric Transforms

| Object | Its kernel and its inversion theorem | Introduced in |
|---|---|---|
| the Hilbert transform on the line | kernel $1/(\pi(x-y))$; inversion by $H^2 = -I$ and the boundedness on $L^p$, $1<p<\infty$ | *Fourier Analysis on Euclidean Spaces*; *Real Harmonic Analysis* |
| the Riesz transforms $R_j$ | symbols $-i\xi_j/\lvert\xi\rvert$; the model singular integrals of the Calderón–Zygmund theory, of which the Hilbert transform is the case $n=1$ | *Fourier Analysis on Euclidean Spaces*; *Real Harmonic Analysis* |
| the Radon transform | integration over hyperplanes; inversion by the Fourier slice theorem and filtered back-projection | *Complex Harmonic Analysis* |
| the Hankel transform | kernel $J_\nu(\rho r)r$; inversion by the Hankel inversion theorem, the radial part of the Fourier transform | *Octonion Harmonic Analysis* |
| the wavelet transform | kernel $\psi((t-b)/a)/a$; inversion by the admissibility condition $\int \lvert\hat\psi(\omega)\rvert^2/\lvert\omega\rvert\,d\omega < \infty$ | *Complex Harmonic Analysis* |
| the wavelet transform on a hypercomplex system | the same kernel with the system's scalings; inversion by the resolution of the identity | *Biquaternion Continuous Harmonic Analysis* |

## Transforms Attached to a Group or an Algebra

| Object | Its kernel and its inversion theorem | Introduced in |
|---|---|---|
| the Gelfand transform | the characters of a commutative Banach algebra as kernel; inversion by the Gelfand representation, an isomorphism for a commutative C*-algebra | *Harmonic Analysis on Groups*; *Holomorphic Functional Calculus* |
| the spherical transform on a symmetric space | the spherical functions as kernel; inversion by the Plancherel theorem for the spherical transform | *The Plancherel Theorem* |
| the Fourier transform of a representation | the matrix coefficients as kernel; the Plancherel decomposition of a unitary representation | *Noncommutative Harmonic Analysis* |
| the character of a representation | the trace of the representation, the degenerate kernel that inverts the decomposition | *Analysis on Compact Groups* |
| the Wigner transform of a state | the matrix-element kernel $W(x,\xi)$ on phase space; its semiclassical defect measure is positive, carried by the energy surface and invariant under the Hamiltonian flow; inversion is the Weyl quantisation $\operatorname{Op}^w_\hbar$ | *Semiclassical Analysis*; *Pseudodifferential Operators* |

## Transforms That Do Not Satisfy Their Inversion Theorem

| Object | The failure | Introduced in |
|---|---|---|
| the Fourier transform of a function outside $L^1 \cup L^2$ | the integral does not converge; only the tempered-distribution definition applies | *Fourier Analysis on Euclidean Spaces*; *Distributions and Fundamental Solutions* |
| the Fourier transform of a function with a singularity | the integral converges only as an improper integral or a principal value; otherwise the transform is defined as a tempered distribution | *Fourier Analysis on Euclidean Spaces*; *Distributions and Fundamental Solutions* |
| the Laplace transform with a divergent defining integral | the transform exists only in the half-plane $\operatorname{Re}\lambda > \omega_0$ of convergence of the defining integral, and the inversion is confined to it | *Semigroups and Evolution Equations* |
| a wavelet whose admissibility integral diverges | the transform has no inversion; the admissibility condition is the necessary hypothesis | *Complex Harmonic Analysis* |
| the Radon transform of a function that is not summable over the lines | the transform is not defined without a decay hypothesis on the measured set | *Complex Harmonic Analysis* |
| the Hilbert transform on $L^1$ | the strong-type bound fails at $p = 1$; only the weak-type $(1,1)$ bound holds | *Real Harmonic Analysis* |

## Summary

This list gathers the integral transforms of the corpus: the Fourier transforms of the line, the circle, the finite, locally compact and compact groups and the adeles; the Laplace, Fourier–Stieltjes and Mellin transforms of the half-line and the multiplicative group; the singular and geometric transforms of Hilbert, Riesz, Radon, Hankel and wavelet type; and the Gelfand, spherical, representation-theoretic and Wigner transforms attached to a group or an algebra. Each row records the kernel and the inversion theorem, and the closing table records the cases in which the defining integral or the inversion fails.

## Summary of Notation

The objects are named rather than denoted; the symbols in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $\hat f$, $\mathcal F f$ | the Fourier transform of $f$ |
| $\hat\mu$ | the Fourier–Stieltjes transform of a measure |
| $\varphi_X$, $\chi$ | a character, and a characteristic function in the probabilistic use |
| $R(\lambda,A)$ | the resolvent, the Laplace transform of a semigroup |
| $\mathcal M f$, $f \star g$ | the Mellin transform and the multiplicative convolution |
| $Hf$, $R_j$ | the Hilbert transform and the Riesz transforms |
| $Rf$ | the Radon transform |
| $W_\psi f$ | the wavelet transform |
| $J_\nu$ | the Bessel function of order $\nu$, the Hankel kernel |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton University Press, 1971), for the Fourier, Hilbert and Radon transforms with their inversion theorems.
- Sigurdur Helgason, *The Radon Transform* (Birkhäuser, 2nd ed. 1999), for the Radon transform and the spherical transform on symmetric spaces.
- Alexander D. Poularikas, ed., *The Transforms and Applications Handbook* (CRC Press, 3rd ed. 2010), for the catalogue of the classical integral transforms with their kernels and inversion formulas.
