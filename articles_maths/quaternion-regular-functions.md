
# __Quaternion Regular Functions__

## Introduction

Quaternion analysis, in the sense of one complex variable generalised to four real variables, is built on a first-order operator and the class of functions it annihilates. This article defines that operator and its conjugate, states the system of equations that regularity imposes, proves the harmonicity of regular functions through the factorization of the Laplacian, records the examples that generated the classical theory, and gives the Cauchy integral formula that holds on the quaternion algebra. It is the quaternion member of the family's regularity pair; its counterpart is the biquaternion case, where the algebra is no longer a division algebra and the null cone obstructs the complex analogy. Here the algebra is a division algebra, there is no null cone, and the analogy holds without restriction.

The article uses *Quaternion Algebra* and *Quaternion Norm and Invertibility* for the algebra, the quaternion norm and the inverse, *The Scalar and Vector Subspaces of $\mathbb{H}$* for the vector-calculus decomposition of the operator, *Quaternion Integration* for the Cauchy integral formula and its consequences, and *Quaternion Special Functions* for the exponential that generates the examples. It is adjacent to *Fueter Theory for Quaternions*, which owns the Fueter construction and the axial and slice approach; this article owns the operator and the system it defines. The classical one-variable model is compared throughout; no physical vocabulary is used, and the first-order operator is the **Cauchy–Riemann operator** of the menu (some older literature calls it the Dirac operator, a name not used in this corpus).

The corpus's default base is a commutative ring with identity; the analysis requires the real numbers, so the operator is defined over $\mathbb{R}$ and the results are stated for domains in $\mathbb{R}^4$.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; the variable is $x = x_0+x_1e_1+x_2e_2+x_3e_3$ with $x_\mu\in\mathbb{R}$; the conjugate is $\bar x = x_0-\mathbf{x}$ and the modulus is $|x| = \sqrt{N(x)}$. The partial derivatives are $\partial_\mu = \partial/\partial x_\mu$, and the Euclidean Laplacian is $\Delta = \sum_\mu \partial_\mu^2$. The vector operations on $\mathbf{f} = f_1e_1+f_2e_2+f_3e_3$ are $\mathrm{div}\,\mathbf{f} = \sum_k\partial_kf_k$, $\mathrm{grad}\,f_0 = \sum_k(\partial_kf_0)e_k$, and $\mathrm{rot}\,\mathbf{f} = \sum_{j,k,l}\epsilon_{jkl}(\partial_jf_k)e_l$.

## The Cauchy–Riemann Operator and Its Conjugate

**Definition.** The **Cauchy–Riemann operator** on $\mathbb{H}$ and its **quaternion conjugate** are

$$
D = \sum_{\mu=0}^{3}e_\mu\partial_\mu = \partial_0+e_1\partial_1+e_2\partial_2+e_3\partial_3, \qquad
\bar D = \sum_{\mu=0}^{3}\bar e_\mu\partial_\mu = \partial_0-e_1\partial_1-e_2\partial_2-e_3\partial_3,
$$

with $\bar e_0 = e_0$ and $\bar e_k = -e_k$; the bar conjugates the basis elements, not the derivatives.

**Proposition.** The units satisfy the Clifford relation $e_\mu\bar e_\nu+e_\nu\bar e_\mu = 2\delta_{\mu\nu}e_0$, and consequently

$$
D\bar D = \bar D D = \Delta,
$$

so the Cauchy–Riemann operator factors the Laplacian, exactly as $\partial_z\partial_{\bar z} = \tfrac14\Delta$ in one complex variable.

*Proof.* For $\mu = \nu$ one has $e_\mu\bar e_\mu = e_0$, since $e_0\bar e_0 = e_0$ and $e_k\bar e_k = -e_k^2 = e_0$; for $\mu\neq\nu$, $e_\mu\bar e_\nu = -e_\mu e_\nu = e_\nu e_\mu = -e_\nu\bar e_\mu$. Hence all mixed second derivatives cancel in the product, leaving $\sum_\mu\partial_\mu^2 = \Delta$.

**Remark.** The pair $(D,\bar D)$ plays the role of $(\partial_z,\partial_{\bar z})$, but the two operators are not merely the two first-order factors of the Laplacian: because the algebra is non-commutative, the products $D\bar D$ and $\bar D D$ agree as differential operators on the algebra but the operators themselves act on functions by left multiplication and are not interchangeable with right multiplication by a quaternion.

## Regular Functions

**Definition.** Let $\Omega\subseteq\mathbb{H}$ be a domain and $f : \Omega\to\mathbb{H}$ continuously differentiable. Then $f$ is **left-regular**, or **left-monogenic**, if

$$
Df = \sum_{\mu=0}^{3}e_\mu\partial_\mu f = 0
$$

on $\Omega$. It is **right-regular** if $fD := \sum_\mu\partial_\mu f\,e_\mu = 0$, and it is **anti-regular** if $\bar D f = 0$.

**Convention.** In this article and its companions, **regular** without qualification means **left-regular**, $Df = 0$. The opposite convention $\bar Df = 0$ also occurs in the literature and merely interchanges the regular and anti-regular classes.

**Proposition.** Quaternion conjugation exchanges the two regularity conventions: $f$ is left-regular if and only if $\bar f$ is right-regular with respect to the conjugate operator,

$$
Df = 0\iff\bar f\,\bar D = 0,
$$

and $f$ is right-regular if and only if $\bar f$ is anti-regular, $fD = 0\iff\bar D\bar f = 0$.

*Proof.* Conjugation is an anti-automorphism, so it reverses the order of the factors in each term: $\overline{Df} = \sum_\mu(\partial_\mu\bar f)\bar e_\mu = \bar f\bar D$ and $\overline{fD} = \sum_\mu\bar e_\mu\partial_\mu\bar f = \bar D\bar f$. A quaternion vanishes exactly when its conjugate does.

## The System of Regularity Equations

**Theorem.** Writing $f = f_0+\mathbf{f}$ with $\mathbf{f} = f_1e_1+f_2e_2+f_3e_3$, the operator decomposes as

$$
Df = \bigl(\partial_0f_0-\mathrm{div}\,\mathbf{f}\bigr) + \bigl(\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f}\bigr),
$$

so $f$ is left-regular if and only if it solves the **Cauchy–Riemann–Fueter system**

$$
\partial_0f_0 = \mathrm{div}\,\mathbf{f}, \qquad \partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f} = 0 .
$$

*Proof.* Multiply out $e_\mu\partial_\mu(f_0+\mathbf{f})$ term by term, using $\mathbf{a}\mathbf{b} = -\langle\mathbf{a},\mathbf{b}\rangle+\mathbf{a}\times\mathbf{b}$ for pure quaternions: the scalar part collects $\partial_0f_0-\mathrm{div}\,\mathbf{f}$, and the vector part collects $\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f}$. Both parts must vanish.

**Corollary.** The system is a first-order elliptic system of four equations for the four coefficients. Its principal symbol is $s(\xi) = \sum_\mu\xi_\mu e_\mu$, which satisfies $s(\xi)\bar s(\xi) = |\xi|^2e_0$ for every real covector $\xi\neq0$, so the system is elliptic and its solutions are real-analytic.

*Proof.* The principal symbol is invertible with inverse $\bar s(\xi)/|\xi|^2$, which is the ellipticity condition; elliptic systems with smooth coefficients have real-analytic solutions.

**Remark.** The ellipticity is exact, and it is the point at which the quaternion algebra differs from the biquaternion algebra: for the quaternion algebra the quaternion norm is definite, so $|\xi|^2$ never vanishes, and the operator has no characteristic set. There is therefore no analogue of the null cone of $\mathbb{B}$.

## Examples and Closure Properties

**Theorem.** Every constant function is regular; the coordinate function $x$ is not regular, since $Dx = \sum_\mu e_\mu e_\mu = -2e_0$; the Cauchy kernel

$$
G(x) = \frac{\bar x}{|x|^4}
$$

is regular on $\mathbb{H}\setminus\{0\}$; and every classical holomorphic function of the single complex variable $z = x_0+e_1x_1$, extended by constancy in $x_2,x_3$, is regular.

*Proof.* The constants have vanishing derivatives; the identity gives $Dx = e_0-3e_0 = -2e_0$; the kernel is checked by differentiation, the homogeneity of $G$ in four real variables being $1-4 = -3$, so that $G$ is the fundamental solution; and the single-plane statement follows because on functions independent of $x_2,x_3$ the operator reduces to $Df = 2\partial_{\bar z}f$ with $\partial_{\bar z} = \tfrac12(\partial_0+e_1\partial_1)$.

**Proposition (closure).** Regular functions are closed under addition, under right multiplication by constant quaternions, and under left multiplication by real scalars; they are **not** closed under left multiplication by a general quaternion constant. Hence they form a right $\mathbb{H}$-module but not a left one.

*Proof.* Additivity is clear; for a constant $c$, $D(fc) = (Df)c = 0$ while $D(cf) = \sum_\mu e_\mu c\,\partial_\mu f$ need not vanish, as $D(e_2z) = e_2+e_1e_2e_1 = 2e_2\neq0$ shows.

**Remark.** The failure of left multiplication exhibits the non-commutativity directly: the coordinate $z = x_0+e_1x_1$ is regular and $z^2$ is regular, but the reversed products are not, and the single-plane holomorphic functions are the largest class of regular functions obtained from one complex direction. The Cauchy kernel is regular but is not holomorphic in any single-plane variable, so the hypercomplex class is strictly larger than the single-plane class; the two coincide only in two real dimensions.

## Harmonicity and the Factorization of the Laplacian

**Theorem.** Every left-regular function is harmonic,

$$
Df = 0 \implies \Delta f = \bar D(Df) = 0,
$$

and every right-regular function is harmonic as well; the harmonic functions form a strictly larger class, since the coordinate $x_0$ is harmonic but $Dx_0 = e_0\neq0$.

*Proof.* By the factorization $\bar DD = \Delta$, a left-regular $f$ satisfies $\Delta f = \bar D(Df) = 0$; for right-regularity one uses $D\bar D = \Delta$ on the left factor. The coordinate $x_0$ is annihilated by the Laplacian and not by $D$.

**Corollary.** Each coefficient $f_\nu$ of a regular function solves the four-dimensional Laplace equation $\sum_\mu\partial_\mu^2f_\nu = 0$, so regular functions are real-analytic and satisfy the mean value property; the converse fails, so regularity is strictly stronger than harmonicity.

*Proof.* The Laplacian acts componentwise, and the factorization shows the coefficients are harmonic; strictness is the coordinate example. The mean value property and real-analyticity of harmonic functions are standard.

## The Cauchy Integral Formula

**Theorem (fundamental solution).** The Cauchy kernel $G(x) = \bar x/|x|^4$ satisfies $DG = 0$ for $x\neq0$ and, in the sense of distributions,

$$
DG = 2\pi^2\delta_0 e_0 .
$$

**Theorem (Cauchy integral formula).** Let $f$ be continuously differentiable on a bounded domain $\Omega\subseteq\mathbb{H}$ with piecewise smooth boundary $\partial\Omega$, and let $x_0$ be an interior point. Then

$$
f(x_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}G(x-x_0)\,n(x)f(x)\,dS - \frac{1}{2\pi^2}\int_{\Omega}G(x-x_0)\,(Df)(x)\,dV,
$$

where $n$ is the $\mathbb{H}$-valued outward unit normal. If $f$ is regular, the volume term vanishes and

$$
f(x_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}G(x-x_0)\,n(x)f(x)\,dS .
$$

*Proof.* These are the standard results of Clifford analysis in dimension four; the kernel and the constant are computed from the distributional identity $DG = 2\pi^2\delta_0e_0$, which is verified by integrating over a ball of radius $\varepsilon$ and using the homogeneity of $G$. The formula is derived by applying Stokes' theorem to the form $G(x-x_0)n(x)f(x)\,dS$ and subtracting the singular contribution at $x_0$, all products being quaternion products with $G$ on the left and $f$ on the right.

**Corollary.** On $\mathbb{H}$ the Cauchy integral formula holds on every domain, with no restriction to a subspace and no exceptional set; the mean value property, the maximum principle, Liouville's theorem, the identity theorem, and the residue theory for isolated singularities then follow as for holomorphic functions of one variable, since $\mathbb{H}$ has no zero divisors.

*Proof.* The kernel is defined and smooth off the origin throughout $\mathbb{H}$; the absence of zero divisors makes the inverse $x^{-1}$ defined for every $x\neq0$ and the singular set a single point. The consequences are standard in Clifford analysis.

## Comparison with the Biquaternion Case

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries the same operator with complex coefficients, so the Cauchy–Riemann operator on $\mathbb{H}$ is exactly the operator on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ of $\mathbb{B}$, where all coefficients are real.

| Feature | $\mathbb{H}$ | $\mathbb{B}$ |
|---|---|---|
| Coefficients of the variable | real | complex |
| Norm | definite | indefinite |
| Zero divisors | none | the null cone $\mathcal{N} = \{N = 0\}$ |
| Ellipticity of $D$ | everywhere, $s(\xi)\bar s(\xi) = \lvert\xi\rvert^2$ | on indefinite subspaces $s(\xi)\bar s(\xi)$ degenerates on $\mathcal{N}$ |
| Cauchy kernel | $G = \bar x/\lvert x\rvert^4$, regular off the origin | regular only where $N\neq0$; not a fundamental solution on indefinite subspaces |
| Cauchy integral formula | global on every domain | asserted only on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ |
| Maximum principle, Liouville, residue theory | available | available on $\mathbb{H}_{\mathbb{B}}$, fail on $\mathbb{M}_\pm$ |

The obstruction in the biquaternion case is entirely the null cone: because $N$ is indefinite, the principal symbol $s(\xi)$ is singular on the characteristic set, the Cauchy kernel ceases to be a fundamental solution off the quaternion subspace, and the identity $\bar x x = |x|^2$ used to compute $DG = 0$ fails once the coefficients are complex and null. On the quaternion algebra the quaternion norm is definite, so all of these properties hold globally and the four-variable Cauchy theory is complete. The biquaternion account is in *Biquaternion Regular Functions*.

## Summary

The Cauchy–Riemann operator $D = \sum_\mu e_\mu\partial_\mu$ and its conjugate $\bar D = \sum_\mu\bar e_\mu\partial_\mu$ factor the Euclidean Laplacian, $D\bar D = \bar DD = \Delta$, through the Clifford relation $e_\mu\bar e_\nu+e_\nu\bar e_\mu = 2\delta_{\mu\nu}e_0$. A function is left-regular if $Df = 0$; regularity is equivalent to the Cauchy–Riemann–Fueter system $\partial_0f_0 = \mathrm{div}\,\mathbf{f}$, $\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f} = 0$, a first-order elliptic system of four equations whose principal symbol is invertible everywhere because the quaternion norm is definite.

Regular functions are closed under addition, right multiplication by constants, and real scaling, but not under left multiplication by general quaternions, so they form a right module; constants and classical holomorphic functions of a single-plane variable are regular, the coordinate function is not, and the genuine radial regular function is the Cauchy kernel $G = \bar x/|x|^4$, of homogeneity $-3$ in four variables. Every regular function is harmonic, but not conversely. The Cauchy integral formula holds on every domain in $\mathbb{H}$, with the kernel $G$ and the constant $1/(2\pi^2)$, and it yields the mean value property, the maximum principle, Liouville's theorem and the residue theory without exception.

The comparison with the biquaternions isolates the role of the quaternion norm: on $\mathbb{H}$ the definiteness of $N$ makes the operator elliptic everywhere and the Cauchy theory global, while on $\mathbb{B}$ the indefinite form produces the null cone, on which the symbol degenerates and the Cauchy kernel ceases to be fundamental, so the analogy is available only on the quaternion subspace. The Fueter construction and the slice description of regular functions are in *Fueter Theory for Quaternions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, a division algebra |
| $x = x_0+\mathbf{x}$ | Variable quaternion, $x_\mu\in\mathbb{R}$, $\mathbf{x} = x_1e_1+x_2e_2+x_3e_3$ |
| $\partial_\mu, \Delta = \sum_\mu\partial_\mu^2$ | Partial derivatives and Euclidean Laplacian |
| $D = \sum_\mu e_\mu\partial_\mu$ | Cauchy–Riemann operator |
| $\bar D = \sum_\mu\bar e_\mu\partial_\mu$ | Conjugate operator, $\bar e_0 = e_0$, $\bar e_k = -e_k$ |
| $e_\mu\bar e_\nu+e_\nu\bar e_\mu = 2\delta_{\mu\nu}e_0$ | Clifford relation; gives $D\bar D = \bar DD = \Delta$ |
| $Df = 0$ | Left-regularity; regular means left-regular here |
| $fD = 0$, $\bar Df = 0$ | Right-regular and anti-regular functions |
| $\mathrm{div}, \mathrm{grad}, \mathrm{rot}$ | Vector-calculus operators in the decomposition of $Df$ |
| $\partial_0f_0 = \mathrm{div}\,\mathbf{f}$, $\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f} = 0$ | Cauchy–Riemann–Fueter system |
| $s(\xi) = \sum_\mu\xi_\mu e_\mu$ | Principal symbol, $s\bar s = \lvert\xi\rvert^2$ |
| $z = x_0+e_1x_1$ | Single-plane complex variable, $\partial_{\bar z} = \tfrac12(\partial_0+e_1\partial_1)$ |
| $G(x) = \bar x/\lvert x\rvert^4$ | Cauchy kernel; $DG = 2\pi^2\delta_0e_0$ |
| $\mathbb{B}, \mathbb{H}_{\mathbb{B}}$ | Biquaternion algebra and its quaternion subspace |

## Further Reading

- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934) 307–330, for the origin of the four-variable regularity theory.
- F. Brackx, Richard Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy–Riemann operator, monogenic functions and the Cauchy integral formula.
- Richard Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the function theory of the Cauchy–Riemann operator in several variables.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the analytic properties of the operator and its consequences.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the quaternion Cauchy formula and its applications.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the algebraic identities underlying the factorization of the Laplacian.
