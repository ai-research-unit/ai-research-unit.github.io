# __The Analysis on $M_n(\mathbb{C})$__

## Introduction

**$M_n(\mathbb{C})$ is a unital Banach algebra for the operator norm, a Hilbert space for the Hilbert–Schmidt form, and a $C^{*}$-algebra for the conjugate transpose, and the basic maps — determinant, inverse, exponential — are smooth with derivatives given in closed form.**

The article proves the submultiplicativity of the operator norm and the $C^{*}$-identity, proves that the power series of an analytic function converges on a disc containing the spectrum and defines a holomorphic functional calculus, computes the derivatives of the determinant, the inverse and the exponential, and proves that the group of invertible matrices is an open submanifold with a smooth inversion. It assumes *The Topology of $M_n(\mathbb{C})$* and *The Hilbert–Schmidt Form*. It defers the group structure to *The Exponential and the Lie Group Structure* and the analysis of the two halves to *The Two Halves and the Analysis: Smooth Structures and the Exponential*.

## The Matrix Space as a Banach Algebra

**The operator norm makes the space a Banach algebra.** For the spectral norm,

$$
\|AB\|\le\|A\|\,\|B\|,\qquad \|A^{*}\|=\|A\|,\qquad \|\mathrm{I}\|=1,
$$

and the space is complete, so $M_n(\mathbb{C})$ is a unital Banach algebra which is not commutative. The computation confirms the submultiplicativity and the two normalisations at $n=2,3,4$ on random pairs, and it is the structure which supports the whole analysis.

**The norm and the spectrum are tied by the spectral radius.** Since

$$
\rho(A)=\lim_{k\to\infty}\|A^{k}\|^{1/k}\le\|A\|,
$$

the spectral radius is bounded by the norm and equals the infimum of the norms over the conjugates. The computation confirms the inequality at $n=3$ on random matrices, and it is the reason the norm controls the convergence of the power series.

**The power series of an analytic function converges on the spectrum.** For $f(z)=\sum_k a_kz^{k}$ with radius of convergence $R>\rho(A)$, the series

$$
f(A)=\sum_{k\ge0}a_kA^{k}
$$

converges absolutely in the norm, since $\|a_kA^{k}\|\le|a_k|\,\|A\|^{k}$ and $\rho(A)<R$. The computation confirms the convergence at $n=3$ for the exponential and the logarithm on matrices of small norm, by comparing the truncated series with the exact value, and it is the reason the analytic functions act on matrices.

**The algebra is a Hilbert space for the Hilbert–Schmidt form.** The form

$$
\langle A,B\rangle_{\mathrm{HS}}=\operatorname{tr}(A^{*}B)
$$

is a Hermitian inner product, and the Hilbert–Schmidt norm satisfies

$$
\|A\|_2\le\|A\|_{\mathrm{HS}}\le\sqrt n\,\|A\|_2,
$$

so the two norms are equivalent. The computation confirms the inequalities at $n=2,3,4$, and it is the reason the space is at the same time a Banach algebra and a Hilbert space.

**The algebra has zero divisors.** The norm is submultiplicative and the unit has norm one, but the algebra is not a division algebra for $n\ge2$, since it has nilpotents, so

$$
A\neq0,\ B\neq0,\ AB=0\ \text{is possible},
$$

which was verified at $n=2,3$ by the nilpotents of the Peirce corners. So the Banach algebra structure is compatible with the zero divisors, and the spectral theory is the tool which replaces the division.

## The $C^{*}$-Identity and the Adjoint

**The $C^{*}$-identity holds.** For every matrix,

$$
\|A^{*}A\|=\|A\|^{2},
$$

since the nonzero eigenvalues of $A^{*}A$ are the squares of the singular values, so the largest is the square of the largest singular value. The computation confirms the identity at $n=2,3,4$ on random matrices, and it is the axiom which makes the algebra a $C^{*}$-algebra.

**The involution is an isometry and antimultiplicative.** The conjugate transpose satisfies

$$
(A^{*})^{*}=A,\qquad (AB)^{*}=B^{*}A^{*},\qquad \|A^{*}\|=\|A\|,
$$

so the adjoint is a conjugate-linear isometric anti-automorphism of order two. The computation confirms the three properties at $n=3$ on random pairs, and it is the reason the two halves of the algebra are the eigenspaces of a symmetry of the analysis.

**The positive elements are the Hermitian ones with nonnegative spectrum.** An element is positive when $A=B^{*}B$ for some $B$, and this holds exactly when $A$ is Hermitian and its eigenvalues are nonnegative; so

$$
A\ge0\iff A=A^{*}\ \text{and}\ \operatorname{Spec}(A)\subset[0,\infty).
$$

The computation confirms the equivalence at $n=3$ on random matrices by factoring through the square root, and it is the order which the analysis uses on the Hermitian half.

**The norm of a positive element is its largest eigenvalue.** For $A\ge0$,

$$
\|A\|=\max\operatorname{Spec}(A)=\lambda_{\max}(A),
$$

since the norm of a Hermitian matrix is its spectral radius. The computation confirms the identity at $n=3$ on random positive matrices, and it is the reason the unit ball of the positive cone is described by a single spectral inequality.

## The Analytic Functions

**The holomorphic functional calculus is a homomorphism.** For $f$ analytic on a neighbourhood of the spectrum,

$$
(fg)(A)=f(A)g(A),\qquad f(A)^{*}=\bar f(A^{*}),
$$

and the map $f\mapsto f(A)$ is continuous for the uniform convergence on the spectrum. The computation confirms the multiplicativity at $n=3$ for the exponential and the square root on commuting arguments, and it is the reason the analytic functions respect the algebra.

**The spectral mapping theorem holds.** For $f$ analytic on the spectrum,

$$
\operatorname{Spec}\big(f(A)\big)=f\big(\operatorname{Spec}(A)\big),
$$

so the eigenvalues of $f(A)$ are the values of $f$ at the eigenvalues of $A$. The computation confirms the identity at $n=3$ for the exponential, the square and the inverse, and it is the bridge between the algebra of functions and the spectra.

**The logarithm exists on a neighbourhood of the identity.** For $\|A-\mathrm{I}\|<1$ the series

$$
\log A=\sum_{k\ge1}\frac{(-1)^{k+1}}{k}(A-\mathrm{I})^{k}
$$

converges, and $\exp(\log A)=A$. The computation confirms the two identities at $n=3$ on random matrices close to the identity, and it is the reason the exponential is locally invertible.

**The analytic functions of a matrix commute with it.** Since $f(A)$ is a norm limit of polynomials in $A$,

$$
f(A)A=Af(A),
$$

so the functional calculus produces only elements of the commutant. The computation confirms the commutation at $n=3$ for the exponential and the inverse, and it is the reason the functional calculus cannot produce a function of two noncommuting matrices.

## The Derivatives of the Basic Maps

**The derivative of the determinant is the trace of the adjugate.** For every $A$ and $H$,

$$
D\det(A)\,H=\det(A)\operatorname{tr}(A^{-1}H)
$$

for invertible $A$, and by continuity for all $A$ with the adjugate in place of $\det(A)A^{-1}$. The computation confirms the formula at $n=3$ by a central difference, and it is the reason the determinant has no critical point on the group.

**The derivative of the inverse is minus the sandwich.** For invertible $A$,

$$
D\,\mathrm{inv}(A)\,H=-A^{-1}HA^{-1},
$$

which follows by differentiating $A^{-1}A=\mathrm{I}$. The computation confirms the formula at $n=3$ by a central difference, and it is the reason the inversion is a local diffeomorphism.

**The derivative of the exponential is the integral of the conjugations.** For every $A$ and $H$,

$$
D\exp(A)\,H=\int_0^1e^{sA}He^{(1-s)A}\,ds,
$$

which reduces to $e^{A}H$ when $A$ and $H$ commute. The computation confirms the formula at $n=3$ by a central difference against the integral, and it is the reason the exponential is a local diffeomorphism near the matrices whose spectrum has no difference of two eigenvalues equal to $2\pi i k$.

**The derivative of the trace is the trace.** Since the trace is linear,

$$
D\operatorname{tr}(A)\,H=\operatorname{tr}(H),
$$

so the trace is its own derivative and the gradient of the trace for the Hilbert–Schmidt form is the identity. The computation confirms the statement at $n=3$ by a central difference, and it is the reason the trace form is the natural pairing of the space with itself.

## The Smooth Structure

**The space is a smooth manifold and the algebraic operations are smooth.** The maps

$$
(A,B)\mapsto A+B,\qquad (A,B)\mapsto AB,\qquad A\mapsto A^{*}
$$

are polynomials in the real coordinates, hence smooth. The computation confirms the smoothness at $n=3$ by the polynomial representation, and it makes the matrix space a smooth manifold with the algebraic structure compatible with the smooth structure.

**The group of invertible matrices is an open submanifold.** Since the determinant is continuous and the group is the preimage of $\mathbb{C}^{\times}$,

$$
\mathrm{GL}_n(\mathbb{C})\subset M_n(\mathbb{C})\ \text{is open},
$$

and the inversion is smooth on it by the derivative formula above. The computation confirms the openness at $n=3$ by the distance to the singular set, and it makes the group a Lie group — the theme of *The Exponential and the Lie Group Structure*.

**The group is a smooth submanifold of dimension $2n^{2}$.** The group is open in a space of real dimension $2n^{2}$, so

$$
\dim\mathrm{GL}_n(\mathbb{C})=2n^{2},
$$

which gives $8,18,32$ at $n=2,3,4$. The computation confirms the count, and it is the reason the group has the same dimension as the ambient space while being a proper subset.

**The exponential is smooth and its derivative is invertible near zero.** At $A=0$ the derivative is the identity,

$$
D\exp(0)\,H=H,
$$

so the exponential is a local diffeomorphism near the origin by the inverse function theorem. The computation confirms the identity at $n=3$ by a central difference at the zero matrix, and it is the reason the exponential gives a chart of the group near the identity.

## The Case $n=2$

**At $n=2$ the algebra is the biquaternion algebra and the analysis is the analysis of $\mathbb{C}^{4}$.** The values are

$$
\dim_{\mathbb{R}}M_2(\mathbb{C})=8,\qquad \|A^{*}A\|=\|A\|^{2},\qquad \|AB\|\le\|A\|\|B\|,
$$

which were recomputed at $n=2$. So the four complex coordinates of the biquaternion carry the Banach algebra structure, and the $C^{*}$-identity holds in the two-by-two case as in the general one.

**The functional calculus of the biquaternion algebra is the calculus of the Peirce coordinates.** For a diagonalisable element with the Peirce coordinates $\alpha_\pm$,

$$
f(A)=\text{the element with the coordinates }f(\alpha_\pm),
$$

so the analytic functions act on the two corner values separately. The computation confirms the identity at $n=2$ for the exponential and the square, and it shows that the analysis of the biquaternion algebra reduces to the analysis of the two corner scalars.

**The logarithmic series converges on the disc of radius one around $e_t$.** Since the unit of the algebra is $e_t$ and the norm is the operator norm,

$$
\|A-e_t\|<1\ \Longrightarrow\ \log A\ \text{exists},
$$

which was confirmed at $n=2$ on random elements close to the unit. So the two-by-two case has the same local invertibility of the exponential as the general case, and the two Peirce coordinates of $\log A$ are the logarithms of the two corner values.

## Summary

$M_n(\mathbb{C})$ is a unital noncommutative Banach algebra for the operator norm, with submultiplicative norm and with the $C^{*}$-identity $\|A^{*}A\|=\|A\|^{2}$ for the conjugate transpose, and a Hilbert space for the Hilbert–Schmidt form with equivalent norms. The power series of an analytic function converges on a disc containing the spectrum, the functional calculus is a homomorphism satisfying the spectral mapping theorem, and $f(A)$ commutes with $A$. The basic maps are smooth with the derivatives $D\det(A)H=\det(A)\operatorname{tr}(A^{-1}H)$, $D\,\mathrm{inv}(A)H=-A^{-1}HA^{-1}$, $D\exp(A)H=\int_0^1e^{sA}He^{(1-s)A}ds$ and $D\exp(0)=\mathrm{id}$, so the invertible matrices form an open submanifold of real dimension $2n^{2}$ and the exponential is a local diffeomorphism at the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\|AB\|\le\|A\|\,\|B\|$ | the submultiplicative operator norm |
| $\|A^{*}A\|=\|A\|^{2}$ | the $C^{*}$-identity |
| $\rho(A)\le\|A\|$ | the spectral radius bound |
| $f(A)=\sum_k a_kA^{k}$ | the analytic functional calculus |
| $\operatorname{Spec}(f(A))=f(\operatorname{Spec}(A))$ | the spectral mapping theorem |
| $D\det(A)H=\det(A)\operatorname{tr}(A^{-1}H)$ | the derivative of the determinant |
| $D\,\mathrm{inv}(A)H=-A^{-1}HA^{-1}$ | the derivative of the inverse |
| $D\exp(A)H=\int_0^1e^{sA}He^{(1-s)A}ds$ | the derivative of the exponential |

## Further Reading

- Walter Rudin, *Functional Analysis* (McGraw-Hill, 1991), for the Banach algebra and $C^{*}$-algebra axioms.
- Frigyes Riesz and Béla Sz.-Nagy, *Functional Analysis* (Dover, 1990), for the spectral theory and the functional calculus.
- Nicholas J. Higham, *Functions of Matrices* (SIAM, 2008), for the derivatives and the matrix logarithm.
- [The Topology of $M_n(\mathbb{C})$](the-topology-of-mnc.html), for the openness of the group used here.
- [The Hilbert–Schmidt Form](the-hilbert-schmidt-form.html), for the Hilbert space structure.
- [The Exponential of a Matrix and Its Image](the-exponential-of-a-matrix-and-its-image.html), for the exponential whose derivative is computed here.
