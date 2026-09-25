
# __Split-Quaternion Harmonic Analysis__

## Introduction

This article treats the harmonic analysis of the split-quaternion algebra. It identifies the additive group and its dual, develops the Fourier transform of the group, proves the convolution theorem, introduces the algebra-valued transform and the vanishing-determinant issue on the null cone, treats distributions and the transform of the fundamental solution, relates the whole to the matrix model, and compares the situation with the quaternion and split-complex transforms.

The split-quaternion algebra, its norm form, its units and its matrix model are assumed from *Split-Quaternion Algebra*, *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Matrix Representations*; the exponential and its invertibility from *Split-Quaternion Elementary Functions*; the operators, their characteristic variety and the failure of elliptic regularity from *Split-Quaternion Analysis*; the fundamental solution and its support on the cone from *Split-Quaternion Integration*; and the metric and the forms from *Split-Quaternion Geometry*. The harmonic analysis of Euclidean space is that of *Fourier Analysis on Euclidean Spaces*, the analysis of the abelian group and its dual that of *Harmonic Analysis on Groups*, the distributions that of *Distributions and Fundamental Solutions*, the division-algebra transform that of *Quaternion Harmonic Analysis*, and the two-dimensional hyperbolic transform that of *Split-Complex Harmonic Analysis*. Nothing physical is invoked.

## The Additive Group and Its Dual

**Theorem (The Group and Its Dual).** The additive group of the algebra, identified with $\mathbb{R}^4$ through the coordinates $x = a + be_1 + ce_2 + de_3$, is a locally compact abelian group, with the Lebesgue measure as its Haar measure. Its dual is again $\mathbb{R}^4$, identified with the frequency vectors $\xi = \alpha + \beta e_1 + \gamma e_2 + \delta e_3$, the pairing being the Euclidean scalar product of the coordinate vectors and the characters being the complex-valued functions

$$
\chi_\xi(x) = e^{2\pi \mathrm{i}\langle x,\xi\rangle}, \qquad \langle x,\xi\rangle = a\alpha + b\beta + c\gamma + d\delta ,
$$

Pontryagin duality holds, and the dual group is equipped with the dual Haar measure.

**Proof.** The additive group of a finite-dimensional real vector space with its Euclidean topology is locally compact and abelian, and the character group of $\mathbb{R}^n$ is $\mathbb{R}^n$ with the displayed characters; this is the standard duality of *Harmonic Analysis on Groups*, §*Characters and the Dual Group*. $\square$

**Remark (The Complex Unit Is Scalar).** The symbol $\mathrm{i}$ in the characters is the usual complex unit, a scalar; it is not an element of the algebra, and no element of the algebra is ever used as the imaginary unit of the transform. The algebra enters only through the values of the functions transformed and through the products of those values.

**Remark (The Corpus Convention).** The characters and the transform are taken with the sign convention of *Quaternion Harmonic Analysis*, §*The Quaternion Characters*, so that the pairing is the Euclidean one on $\mathbb{R}^4$ and the transform of a derivative carries the factor $-2\pi\mathrm{i}$. In the quaternion case the algebra-valued characters $e^{2\pi\omega\langle x,\xi\rangle}$ with $\omega^2 = -1$ lie on the unit sphere and are bounded; here the corresponding kernel $e^{-x\xi}$ is bounded only when $\operatorname{Sc}(x\xi) = 0$, and its norm is $e^{-2\operatorname{Sc}(x\xi)}$ in general, because the form is indefinite. The boundedness of the characters in the definite case and its failure in the split case is the same dichotomy as the definiteness of the form.

**Corollary (The Space of Functions).** The algebra-valued functions with square-integrable components form the Hilbert space

$$
L^2(\mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathrm{s}}) \cong \big(L^2(\mathbb{R}^4)\big)^4 ,
$$

with the inner product $\langle f,g\rangle = \int \operatorname{Sc}(f\bar g)$, and the algebra acts pointwise on it by left and right multiplication.

**Proof.** The identification is componentwise, and the scalar product is that of four real functions expressed in the basis. $\square$

## The Fourier Transform of the Group

**Definition.** For $f \in L^1(\mathbb{H}_{\mathrm{s}},\mathbb{H}_{\mathrm{s}})$ the **Fourier transform** is

$$
\hat f(\xi) = \int_{\mathbb{H}_{\mathrm{s}}} f(x)\, e^{2\pi \mathrm{i}\langle x,\xi\rangle}\,\mathrm{d}x \ \in \mathbb{H}_{\mathrm{s}} ,
$$

the transform of the four scalar components of $f$.

**Theorem (Inversion and Plancherel).** For $f$ in the Schwartz class of algebra-valued functions,

$$
f(x) = \int_{\mathbb{H}_{\mathrm{s}}} \hat f(\xi)\, e^{-2\pi \mathrm{i}\langle x,\xi\rangle}\,\mathrm{d}\xi ,
$$

the transform extends to a unitary operator on $L^2(\mathbb{H}_{\mathrm{s}},\mathbb{H}_{\mathrm{s}})$ up to the usual normalisation, and the Riemann–Lebesgue lemma holds. All of this is the classical Fourier analysis of $\mathbb{R}^4$ applied to each of the four components.

**Proof.** The scalar theory of *Fourier Analysis on Euclidean Spaces* applies componentwise; the unitarity is the Plancherel theorem in each component. $\square$

**Corollary (The Non-Commutativity Plays No Role Here).** The group transform sees only the abelian additive structure of the algebra: the non-commutativity of the product and the zero divisors do not enter the statements of inversion and Plancherel, because the characters are scalar and commute with everything. They enter as soon as a product of algebra-valued functions is taken, that is in the next two sections.

**Proof.** The characters are central; the transform is componentwise. $\square$

## Convolution and the Convolution Theorem

**Definition.** The **convolution** of two algebra-valued functions is

$$
(f * g)(x) = \int_{\mathbb{H}_{\mathrm{s}}} f(y)\,g(x-y)\,\mathrm{d}y ,
$$

with the product of the algebra inside the integral.

**Theorem (The Convolution Theorem).** For $f, g \in L^1(\mathbb{H}_{\mathrm{s}},\mathbb{H}_{\mathrm{s}})$ the convolution is well defined almost everywhere, and

$$
\widehat{f * g}(\xi) = \hat f(\xi)\,\hat g(\xi),
$$

the product being the product of the algebra.

**Proof.** Substituting $z = x-y$ in the transform of $f*g$ and using the multiplicativity of the characters, which are scalar, separates the double integral into the product of the two transforms; the algebra product factors out because the character is central. $\square$

**Corollary (The Transform Is an Algebra Homomorphism).** The Fourier transform carries convolution to the pointwise product of the algebra and the direct sum to the sum, both products taken in the same order; it is therefore an isomorphism of the convolution algebra onto the algebra of algebra-valued functions with the pointwise product. The convolution is associative, because the algebra product is, but it is **not** commutative: $\widehat{f*g} = \hat f\hat g$ while $\widehat{g*f} = \hat g\hat f$, and the two differ as soon as the values of the transforms fail to commute. The transform is an isomorphism onto the pointwise-product algebra, not onto a commutative algebra, and the non-commutativity of the algebra is exactly what is transported.

**Proof.** The theorem and the inversion formula give the isomorphism; for the failure of commutativity take $f = e_1k$ and $g = e_2k$ with a fixed integrable $k$ of positive square integral: then $(f*g)(0) = e_3\int k(y)k(-y)\,\mathrm{d}y$ and $(g*f)(0) = -e_3\int k(y)k(-y)\,\mathrm{d}y$, which differ. Associativity is $\widehat{(f*g)*h} = (\hat f\hat g)\hat h = \hat f(\hat g\hat h)$. $\square$

### Approximate Identities and Young's Inequality

**Definition.** An **approximate identity** is a family $(k_\varepsilon)_{\varepsilon>0}$ of integrable algebra-valued functions with $\int k_\varepsilon = 1$, with $\sup_\varepsilon \|k_\varepsilon\|_1$ finite and with the mass concentrating at the origin as $\varepsilon \to 0$; the standard choice is $k_\varepsilon(x) = \varepsilon^{-4}k(x/\varepsilon)$ for a fixed integrable $k$ with $\int k = 1$.

**Theorem (Young's Inequality and Convergence).** For $f \in L^p$ and $k \in L^1$,

$$
\|f * k\|_p \leq C\,\|f\|_p\,\|k\|_1 ,
$$

with the constant $C$ comparing the Euclidean norm with the submultiplicative norm of the matrix model as in *Split-Quaternion Analysis*, §*The Metric Structure*; and $f * k_\varepsilon \to f$ in $L^p$ as $\varepsilon \to 0$ for $1 \leq p < \infty$, so the $L^1$-convolution has bounded approximate identities.

**Proof.** Young's inequality is the classical one, the algebra-valued integrand being estimated by the submultiplicative norm; the convergence of the approximate identity uses the translation invariance of the Lebesgue measure and the continuity of translation in $L^p$, both componentwise. $\square$

## The Algebra-Valued Transform and the Vanishing Determinant

The transform that uses the algebra itself as the kernel is the analogue of the quaternionic and Clifford transforms; it is not the group transform, and its inversion is where the zero divisors appear.

**Definition.** For a suitable function $f$ the **algebra-kernel transform** is

$$
\mathcal{F}f(\xi) = \int_{\mathbb{H}_{\mathrm{s}}} e^{-x\xi}\, f(x)\,\mathrm{d}x , \qquad x\xi \text{ the algebra product},
$$

the exponential being that of *Split-Quaternion Elementary Functions*.

**Theorem (The Kernel Is Never Singular).** The kernel $e^{-x\xi}$ is invertible for all $x$ and all $\xi$, with

$$
N\big(e^{-x\xi}\big) = e^{-2\operatorname{Sc}(x\xi)} > 0 ,
$$

so the exponential kernel itself is never a zero divisor, and the transform is well defined and bounded on $L^1$ for every frequency.

**Proof.** *Split-Quaternion Elementary Functions*, §*The Exponential*, applied to the element $-x\xi$. $\square$

**Theorem (The Inversion Degenerates on the Null Cone).** The kernel $e^{-x\xi}$ is not a character of the group: it is algebra-valued and not multiplicative in $x$. The inversion of $\mathcal{F}$ requires, in its natural derivation by integration by parts in the frequency variable, the inverse of the difference variable $x-y$, and

$$
(x-y)^{-1} = \frac{\overline{x-y}}{N(x-y)}
$$

exists exactly when $N(x-y) \neq 0$, that is off the null cone. On the null cone the reciprocal does not exist, the derivation of the inversion formula fails, and the transform is not invertible by a kernel of the same shape.

**Proof.** The inverse of an element is $\bar{u}/N(u)$ by *Split-Quaternion Algebra*, §*The Norm Form*, and $N(u) = 0$ exactly on the zero divisors by *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*. The non-multiplicativity of the kernel is immediate from the non-commutativity: $e^{-(x+y)\xi} \neq e^{-x\xi}e^{-y\xi}$ unless $x$ and $\xi$ commute, by *Split-Quaternion Elementary Functions*, §*Non-Commutativity and the One-Variable Case*. $\square$

**Theorem (The Vanishing Determinant, Stated Precisely).** Let $D = e_1\partial_b + e_2\partial_c + e_3\partial_d$ be the vector operator and let the transform be the group transform of the preceding section, whose linearity allows differentiating under the integral. Then

$$
\widehat{Df}(\xi) = -2\pi \mathrm{i}\;\xi\, \hat f(\xi),
$$

so that the **symbol** of the operator is the frequency vector $\xi \in V$; the symbol is invertible exactly when $\xi$ is a unit, that is exactly when $N(\xi) \neq 0$, and it degenerates on the null cone, the zero divisor set. The singular set of the symbol is the characteristic variety of the operator, in agreement with *Split-Quaternion Analysis*, §*The Differential Operators*.

**Proof.** Integration by parts in each coordinate gives $\widehat{\partial_i f} = -2\pi\mathrm{i}\xi_i\hat f$, and the generators multiply the scalar-valued transform centrally; the identification of the invertible frequencies with $N \neq 0$ is the invertibility criterion of *Split-Quaternion Norm and Invertibility*. $\square$

**Corollary (The Transform of the Fundamental Solution Is Singular on the Cone).** Let $E_D$ be the fundamental solution of $D$ of *Split-Quaternion Integration*, §*The Fundamental Solution*. Then, with the principal value of the reciprocal,

$$
\hat E_D(\xi) = -\frac{1}{2\pi\mathrm{i}}\,\xi^{-1} = \frac{1}{2\pi\mathrm{i}}\,\frac{\xi}{N(\xi)} ,
$$

a distribution whose singular support is exactly the null cone. The vanishing determinant $N(\xi) = 0$ is therefore not a technical nuisance: it is the support of the transformed fundamental solution, and it is the reason the fundamental solution is singular on the cone rather than at a point.

**Proof.** From $\widehat{DE_D} = -2\pi\mathrm{i}\xi\hat E_D = \hat\delta = 1$ and $\xi^{-1} = -\xi/N(\xi)$ for $\xi \in V$; the support statement is then the standard computation of the principal value of $1/N$ on an indefinite quadratic form, as in *Distributions and Fundamental Solutions*. $\square$

## Distributions

**Theorem (Tempered Distributions).** The Fourier transform extends to an isomorphism of the space of tempered algebra-valued distributions onto itself, and it exchanges multiplication by the algebra-valued functions with convolution. The fundamental solution $E_D$ is tempered, being supported in a closed cone and of polynomial growth, so its transform exists and is the distribution displayed above.

**Proof.** The scalar theory of *Distributions and Fundamental Solutions* applies componentwise; the temperedness of the fundamental solution follows from its homogeneity of degree $-2$ and its support on the cone. $\square$

**Corollary (The Failure of Elliptic Inversion and Its Frequency Location).** The inversion of the transform of a solution of $Df = g$ is obstructed exactly on the null cone: the frequency equation $\hat f = -(2\pi\mathrm{i}\xi)^{-1}\hat g$ cannot be solved by a smooth symbol on the whole frequency space, and any solution must have its singularities concentrated on the characteristic variety. This is the frequency-space form of the failure of the elliptic theory and of the cone support of the fundamental solution.

**Proof.** The symbol is non-invertible on the null cone by the vanishing-determinant theorem, so the inverse symbol is not smooth there and the multiplication by it is not a pseudodifferential operation of the standard elliptic type. $\square$

## The Relation to the Matrix Model

**Theorem (The Matrix Model of the Transform).** Through the isomorphism $\Phi$ the transform of an algebra-valued function corresponds to the entrywise transform of the matrix-valued function $\Phi \circ f$, the convolution corresponds to the entrywise convolution, and the symbol $\xi$ corresponds to the traceless matrix $\Phi(\xi)$ with

$$
\det \Phi(\xi) = N(\xi) .
$$

The vanishing of the determinant of the symbol is therefore the vanishing of the determinant of the traceless matrix of the frequency, that is the condition that the frequency be a zero divisor, and the set of singular frequencies corresponds to the singular traceless matrices.

**Proof.** The transform is componentwise and $\Phi$ is a linear isomorphism; the determinant identity is *Split-Quaternion Matrix Representations*, §*The Determinant and the Trace*. $\square$

**Corollary (Two Readings of the Same Degeneracy).** The degeneracy of the harmonic analysis on the null cone can be read either in the algebra, as the non-invertibility of the frequency, or in the matrix model, as the singularity of the traceless matrix; the two readings are the same statement.

## Comparison with the Quaternion and Split-Complex Transforms

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}$ |
|---|---|---|---|
| additive group | locally compact abelian | locally compact abelian | locally compact abelian |
| group transform | four-dimensional Fourier transform | four-dimensional Fourier transform | two-dimensional Fourier transform |
| convolution theorem | holds | holds | holds |
| algebra-kernel transform | quaternionic Fourier transform, invertible symbol | algebra-kernel transform, symbol degenerate on the null cone | hyperbolic transform, degenerate on the isotropic lines |
| symbol $\xi$ | invertible for every $\xi \neq 0$ | invertible iff $N(\xi) \neq 0$ | invertible iff $N(\xi) \neq 0$ |
| transformed fundamental solution | singular at the origin | singular on the light cone | singular on the two isotropic lines |

The quaternion column is the content of *Quaternion Harmonic Analysis* and the split-complex column that of *Split-Complex Harmonic Analysis*. The decisive difference is that the quaternion norm vanishes only at the origin, so its symbol is invertible at every nonzero frequency and the quaternionic transform has no vanishing-determinant problem; in the split case the norm vanishes on a cone, of real dimension two in $V$, and the transformed fundamental solution is supported there. The eight-dimensional relative $\mathbb{H}_{\mathbb{D}}$ is a later system of Part V, treated under Split-Biquaternions, and nothing of it is used here.

## Summary

The additive group of the split-quaternion algebra is a locally compact abelian group, identified with $\mathbb{R}^4$, with dual $\mathbb{R}^4$ and scalar characters $\chi_\xi(x) = e^{2\pi\mathrm{i}\langle x,\xi\rangle}$. The Fourier transform of the group is the fourfold scalar transform applied to the components, with inversion and Plancherel; the convolution theorem holds with the algebra product, because the characters are scalar, so the transform is an isomorphism of the convolution algebra onto the pointwise product algebra; the convolution is associative because the algebra product is, and it is not commutative, because the algebra product is not.

The algebra-kernel transform uses the exponential of the algebra as kernel. The kernel is never a zero divisor, since $N(e^u) = e^{2\operatorname{Sc}u} > 0$, but it is not a character, and the inversion formula requires the reciprocal of the difference variable, which exists exactly off the null cone; the transform degenerates there. For the vector operator the symbol is the frequency vector $\xi$, invertible exactly when $N(\xi)\neq0$; the singular frequencies form the null cone, which is the characteristic variety of the operator and the zero divisor set. The transformed fundamental solution is $\hat E_D = -(2\pi\mathrm{i}\xi)^{-1} = \xi/(2\pi\mathrm{i}N(\xi))$, a distribution whose singular support is exactly the null cone, and the vanishing determinant is thus the frequency-space explanation of the cone-supported fundamental solution and of the failure of the elliptic theory. In the matrix model the symbol becomes the traceless matrix $\Phi(\xi)$ with $\det\Phi(\xi) = N(\xi)$, and the two readings of the degeneracy coincide.

The comparison with the quaternion case is sharp: there the norm vanishes only at the origin, the symbol is invertible at every nonzero frequency, and the transformed fundamental solution is singular at a point; in the split case the norm vanishes on a cone and every degeneracy is located there. The split-complex case is the two-dimensional model of the same phenomenon, with the two isotropic lines in place of the cone. The eight-dimensional relative is a later system of Part V, named only.

The two transforms of the article are therefore to be kept apart: the group transform is the harmonic analysis of the additive group, complete with inversion, Plancherel and the convolution theorem, and it is blind to the zero divisors; the algebra-kernel transform is the non-commutative transform of the system, and every one of its difficulties is located on the null cone, where the symbol ceases to be invertible. The same cone is the zero divisor set of the algebra, the characteristic variety of the vector operator and the support of the transformed fundamental solution, and it is the single object around which the analysis of this system is organised.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\chi_\xi(x) = e^{2\pi\mathrm{i}\langle x,\xi\rangle}$ | the scalar characters of the additive group | this article |
| $\hat f(\xi)$ | the group Fourier transform | this article |
| $f * g$ | the convolution with the algebra product | this article |
| $\widehat{f*g} = \hat f\hat g$ | the convolution theorem | this article |
| $\mathcal{F}f(\xi) = \int e^{-x\xi}f$ | the algebra-kernel transform | this article |
| $N(e^{-x\xi}) = e^{-2\operatorname{Sc}(x\xi)} > 0$ | the kernel is never a zero divisor | *Split-Quaternion Elementary Functions* |
| $\xi^{-1}$, $N(\xi)$ | the symbol and its determinant | *Split-Quaternion Norm and Invertibility* |
| $\hat E_D = -(2\pi\mathrm{i}\xi)^{-1} = \xi/(2\pi\mathrm{i}N(\xi))$ | the transformed fundamental solution, singular on the null cone | *Split-Quaternion Integration* |
| $\det\Phi(\xi) = N(\xi)$ | the symbol in the matrix model | *Split-Quaternion Matrix Representations* |
| null cone | the singular frequency set and the zero divisor set | *Split-Quaternion Zero Divisors* |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton University Press, 1971), for the group transform, the convolution theorem, inversion and Plancherel.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed. (CRC Press, 2015), for locally compact abelian groups, Pontryagin duality and the Fourier transform of distributions.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 1990), for the symbol of a differential operator, its characteristic variety and the failure of inversion there.
- Eckhard Hitzer and Stephen J. Sangwine, *Quaternion and Clifford Fourier Transforms and Wavelets* (Birkhäuser, 2013), for the non-commutative transforms that motivate the algebra-kernel transform and for the comparison with the quaternionic case.
