# __Derivatives, Fields and Transforms__

## Introduction

The analysis block of the category rests on two operators. The first is the **biquaternionic gradient** $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial Q_\mu$, an algebra-valued operator whose coefficients are derivatives. The second is the **d'Alembertian** $\Box=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$, the scalar norm of the gradient. Between them lie four general products, four forms and two second-order norms; beyond them lies the Fourier transform, whose kernel is the exponential of a root of $-1$.

The article states these results in brief and gives the physical interpretations. It proves nothing. The derivative conventions, the products, the forms, the norms, the transform and its properties are owned by the mathematics articles linked below; the interpretations are this category's. The organising distinction is between **differentiation as one-sided multiplication** and **the transform as a change of description**. The first acts on a field by multiplying it by the gradient on one side; the second re-expresses the field in the basis in which the constant-coefficient operators are diagonal. The first is a map from fields to fields; the second is an invertible map from one description to another.

The article is the analysis article of *Biquaternion Physical Interpretation of Mathematics*. It links the mathematics, not the physics companions. The interpretations it states are the ones the physics corpus has built, restated as interpretations of the mathematics, each with its boundary.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The derivative conventions, the gradient, its conjugate and the material-sector substitution | [Conventions in Mathematics](../articles_maths/conventions-in-mathematics.html), [Biquaternion Analysis](../articles_maths/biquaternion-analysis.html) |
| The four general products read on the gradient, with their symmetric and antisymmetric parts | [The Differential Operators, the Products, the Forms and the D'Alembertian](../articles_maths/the-differential-operators-the-products-the-forms-and-the-d-alembertian.html) |
| The four forms and the four algebraic norms | [The 4 Forms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternioid-c-space.html), [The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.html) |
| The d'Alembertian as the quaternionic and Hermitian norm of the gradient | [The Differential Operators, the Products, the Forms and the D'Alembertian](../articles_maths/the-differential-operators-the-products-the-forms-and-the-d-alembertian.html), [Biquaternion Analysis](../articles_maths/biquaternion-analysis.html) |
| The regular matrix, its determinant and its two blocks | [Introduction to the 4×4 Matrix Element Representation of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html) |
| The roots of $-1$ and their three families | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), [Square Roots of a General Element in the Biquaternion Algebra](../articles_maths/square-roots-of-a-general-element-in-the-biquaternion-algebra.html) |
| The Fourier kernel, the transform pair, inversion and Plancherel | [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html) |
| The factorization into complex transforms and the convolution theorem | [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html) |
| The symbol of the gradient and the d'Alembertian, and the support on the light cone | [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html) |
| The discrete transform, its inverse and the Z transform | [Biquaternion Discrete Harmonic Analysis](../articles_maths/biquaternion-discrete-harmonic-analysis.html) |
| The vanishing-norm issue | [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html), [Biquaternion Discrete Harmonic Analysis](../articles_maths/biquaternion-discrete-harmonic-analysis.html) |
| The transform of a measure and the positivity criterion | [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html), [The Bochner Theorem for the Biquaternioid Transform: the Hermitian Form and the Root](../articles_maths/the-bochner-theorem-for-the-biquaternioid-transform-the-hermitian-form-and-the-root.html) |

## The Gradient and the Four Products

### The Derivative Conventions

The corpus writes a subscript as a component or a label, never as a derivative; every partial derivative is written with $\partial$ and its variable named in full; and the prime is reserved for the imaginary coordinate of a complex coefficient. The coordinate derivative is $\partial/\partial Q_\mu$. On the material sector, where $Q_t=ict'$ and $Q_k=q_k$, the time derivative is the **imaginary-time derivative**,

$$
\frac{\partial}{\partial Q_t}=-\frac{i}{c}\frac{\partial}{\partial t'},
$$

while the three spatial derivatives are the physical ones. This is a convention about the coordinate, not a second derivative; the algebra has one derivative per coordinate.

The **gradient** and its quaternion conjugate are

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
$$

with $\varepsilon=(1,-1,-1,-1)$. The coefficients are invariant under the conjugations — the marks act on the units at fixed coordinate, not on the derivative symbol — so the coefficientwise conjugation leaves the gradient unchanged, and the Hermitian conjugation acts as the quaternion conjugation: $\tilde\nabla^{*}=\tilde\nabla^{\natural}$. The spatial part is written $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$, with divergence, gradient and curl.

### The Four Products

The four general products are the four settings of one rule: the plain product, the quaternionic bilinear product, the plain sesquilinear product and the quaternionic sesquilinear product. In the category they carry the names composition, causality, probability and gauge; on the gradient they are four ways of differentiating the element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$.

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f},
$$

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f},
$$

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}},
$$

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t}+\nabla\times\overline{\vec Q_{\mathrm f}}.
$$

The plain product holds the divergence, the gradient and the curl in one element. The quaternionic product flips the signs of the spatial terms of the plain product. The two sesquilinear products apply the same two products to the conjugated field.

### The Four Forms and the Two Norms

The scalar part of each product read in two arguments is a form:

| Form | Scalar part |
| --- | --- |
| plain bilinear | $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle=\dfrac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}$ |
| quaternionic bilinear | $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}=\dfrac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}$ |
| plain sesquilinear (Hermitian) | $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{*}=\dfrac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$ |
| quaternionic sesquilinear (Krein) | $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural*}=\dfrac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}$ |

At the two equal arguments the four forms give two operators:

| Norm | Operator | On the material sector |
| --- | --- | --- |
| quaternionic bilinear and Hermitian | $\Box=\dfrac{\partial^2}{\partial Q_t^2}+\Delta_Q$ | $\Delta-\dfrac{1}{c^2}\dfrac{\partial^2}{\partial {t'}^2}$ |
| plain bilinear and Krein | $\dfrac{\partial^2}{\partial Q_t^2}-\Delta_Q$ | $-\dfrac{1}{c^2}\dfrac{\partial^2}{\partial {t'}^2}-\Delta$ |

The d'Alembertian is the quaternionic bilinear and the Hermitian norm:

$$
\Box=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q.
$$

The other operator is the plain bilinear and the Krein norm. On the material sector the two read $\Delta-c^{-2}\partial^2/\partial {t'}^2$ and $-c^{-2}\partial^2/\partial {t'}^2-\Delta$. The corpus keeps one d'Alembertian and one sign.

### The Determinant of the First-Order Operator

The left regular matrix $\mathsf M_4^L(\tilde Q)$ has determinant $\langle\tilde Q\rangle_{\natural}^2$. Read on the gradient, with $\langle\tilde\nabla\rangle_{\natural}=\Box$, the same formula gives

$$
\det\mathsf M_4^L(\tilde\nabla)=\Box^2.
$$

The matrix is block diagonal in a basis adapted to the two minimal left ideals; write $A_+(\tilde\nabla)$ for the block on the first. The two blocks have the same determinant, and each carries one factor:

$$
\det A_+(\tilde\nabla)=\Box.
$$

The second-order wave operator is therefore the determinant of a first-order operator. The partial derivatives commute, so the substitution of the derivative for the coefficient is legitimate; the determinant formula and the block decomposition are the mathematics article's, and the computation read on the operator is a matrix computation, not a new theorem.

## The Fourier Transform

### The Kernel and the Root

Fix a root of $-1$, an element $\rho\in\mathbb{B}$ with $\rho^2=-e_t$. The **Fourier kernel** is

$$
W(t',\omega)=\exp(-2\pi\rho\,\omega t')=\cos(2\pi\omega t')e_t-\sin(2\pi\omega t')\rho.
$$

It is a rotation in the plane spanned by $e_t$ and $\rho$: the root generates the rotation and the frequency is the rate. Its inverse is the same expression with the sine reversed,

$$
W(t',\omega)^{-1}=\cos(2\pi\omega t')e_t+\sin(2\pi\omega t')\rho,
$$

and the identity $WW^{-1}=(\cos^2+\sin^2)e_t=e_t$ uses only $\rho^2=-e_t$. For a **pure** root, one with vanishing scalar part, the quaternion conjugate is the inverse, $W^{\natural}=W^{-1}$, and the kernel is unitary, $W^{\natural}W=e_t$; for the central root $\rho=\pm i$ the kernel is the central scalar $\exp(\mp2\pi i\omega t')e_t$, of unit complex modulus, and the inverse is the complex conjugate.

The roots of $-1$ fall into three families: the central imaginary $\rho=\pm i$; the unit pure real quaternions $\rho=\pm\hat\mu$; and the non-trivial roots $\rho=b\hat\mu+d\hat\nu i$ with $\hat\mu,\hat\nu$ perpendicular unit pure real quaternions and $b^2-d^2=1$. The last two families are pure; the first is not. The choice of family changes the transform, and it is the subject of the clock interpretation below.

### The Transform Pair

For a function $f:\mathbb{R}\to\mathbb{B}$, the **continuous transform** and its inverse are

$$
F(\omega)=\int_{-\infty}^{\infty}W(t',\omega)f(t')\,dt',\qquad
f(t')=\int_{-\infty}^{\infty}W(t',\omega)^{-1}F(\omega)\,d\omega,
$$

under the standard convergence hypotheses. The kernel may stand on the left or on the right; the placement is part of the convention. The kernel is invertible for every root. The Plancherel identity holds for square-integrable functions when the root is unitary, $\rho^{*}=-\rho$ — the central imaginary and the unit real roots — and it is that unitarity which the condition encodes,

$$
\int_{-\infty}^{\infty}\overline{f(t')}g(t')\,dt'=\int_{-\infty}^{\infty}\overline{F(\omega)}G(\omega)\,d\omega.
$$

Convolution in the coordinate becomes biquaternion multiplication in the frequency, and the non-commutativity of the algebra means that the order of the factors is part of the statement.

### The Factorization

In a basis adapted to the root, the transform splits into four ordinary complex Fourier transforms, one for each coefficient. For a non-trivial root and a signal that takes values in the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ or in its imaginary translate $i\mathbb{H}_{\mathbb{B}}$, two complex transforms suffice; for a general biquaternion signal, four are required. The factorization is the precise sense in which the biquaternion transform is ordinary complex analysis applied entrywise, dressed in the algebra; the genuinely biquaternionic content is the choice of root and the basis change it induces.

### The Symbol

The transform diagonalizes the constant-coefficient differential operators. The derivative becomes multiplication by the root times the frequency,

$$
\frac{\partial}{\partial Q_\mu}\longmapsto 2\pi\rho\,\omega_\mu,
$$

so the gradient becomes the biquaternion multiplier $2\pi\rho(\omega_te_t+\omega_x\vec e_x+\omega_y\vec e_y+\omega_z\vec e_z)$. The d'Alembertian becomes a scalar multiplier, its symbol. On the material sector, in the physical frequency $\omega$ and wavevector $\vec k$, the symbol is proportional to

$$
\frac{\omega^2}{c^2}-\lvert\vec k\rvert^2,
$$

with the constant and the sign fixed by the transform convention. It vanishes on the light cone $\omega^2=c^2\lvert\vec k\rvert^2$, so the transform of a solution of $\Box\tilde F=0$ is supported on the cone. Its level sets are the mass shells: the zero level is the massless shell, and the level $m^2c^2/\hbar^2$ is the shell of mass $m$.

### The Discrete Case

The discrete transform replaces the integral by a sum over $N$ samples, with kernel $W_N(n,\ell)=\exp(-2\pi\rho n\ell/N)$, and the inverse carries the factor $1/N$. The inversion, the factorization and the convolution theorem have the same shape. The sampling theorem and the periodization formula relate the discrete and continuous transforms; both are componentwise, because the kernel is the ordinary complex kernel in the direction $\rho$. The discrete article adds the $\mathrm Z$ transform, whose region of convergence is read coefficientwise.

### The Vanishing Norm and the Measure

Two features of the transform are genuinely biquaternionic. The first is the **vanishing norm**: a function may take zero-divisor values on a set of positive measure, and the transform is then not guaranteed to be invertible. The transform is invertible on functions whose values have non-vanishing norm; restricting to $\mathbb{H}_{\mathbb{B}}$ is sufficient, and on $\mathbb{M}_-$ the transform is invertible exactly for values off the cone, but the precise condition for a general function that takes zero-divisor values on a set of positive measure is open.

The second is the **positivity of the transform of a measure**. For a finite positive measure $\mu$, a pure root $\rho$ and central coefficients $A_k$, the transform $G(\omega)=\int\chi_\omega\,d\mu$, with $\chi_\omega$ the kernel at frequency $\omega$, satisfies the quadratic identity

$$
\sum_{k,l}A_kA_l\,G(\omega_k-\omega_l)=\int\langle Z\rangle_{\natural}\,d\mu,\qquad
Z=\sum_kA_k\chi_{\omega_k},
$$

with the biquaternion norm on the right. At $A_1=i$ the left-hand side is $i^2\mu(\mathbb{R}^n)e_t=-\mu(\mathbb{R}^n)e_t$, negative for every non-zero measure, because $\langle i\rangle_{\natural}=-1$: the norm pairing is not positive. With the Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, the quadratic form

$$
\sum_{k,l}A_k\,G(\omega_k-\omega_l)\,A_l^{*}=\int ZZ^{*}d\mu
$$

is positive definite exactly for the **degenerate** roots $\pm i$ and $\pm\hat\mu$, and fails for every genuinely complex root. The two failures are different: the norm failure is root-independent and belongs to the indefinite interval; the positivity failure is root-dependent and belongs to the character.

## Physical Interpretations

- **The derivative is the one-sided product.** Differentiation is multiplication of the field by the gradient on one side: $\tilde\nabla\tilde F$ holds the divergence, the gradient and the curl of $\tilde F$ in one biquaternion; the scalar part of the symmetric half is the plain form, and the antisymmetric half is the curl. For the field strength, $\tilde\nabla\tilde F=-g\tilde J$ is the Maxwell equation, with $g$ the coupling of the cited article. Boundary: the equation is a restatement of the cited Maxwell equation, not a derivation; the interpretation supplies no constitutive law, no dynamics and no prediction.

- **The Hermitian form on two gradients is the kinetic density.** For a scalar field $\tilde\Phi=\Phi e_t$,

    $$
    \mathrm{Sc}\left[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\right]=\sum_\mu\frac{\partial\Phi^{*}}{\partial Q_\mu}\frac{\partial\Phi}{\partial Q_\mu},
    $$

    and on the material sector, where the field is written $\phi$, this is $-c^{-2}\lvert\partial\phi/\partial t'\rvert^2+\lvert\nabla\phi\rvert^2$. The kinetic Lagrangian is its negative, so the sign of the kinetic term is the sign of the Hermitian form on the gradient. Boundary: the identification is the Klein–Gordon Lagrangian interpretation; the value of the Hermitian form on the gradient is not positive, because the time derivative is imaginary on the material sector; no dynamics is derived.

- **The d'Alembertian is the propagating operator.** $\Box=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$ is the second-order operator of the wave equations and of the Green's-function equation; on the material sector it is $\Delta-c^{-2}\partial^2/\partial {t'}^2$. Boundary: the corpus keeps one d'Alembertian and one sign; the partner $\partial^2/\partial Q_t^2-\Delta_Q$ is not a second propagating operator, and the Green's functions are owned by the physics article.

- **The wave operator is the determinant of the first-order operator.** The regular matrix of the gradient has determinant $\Box^2$, and its chiral block has determinant $\Box$. The second-order wave equation is therefore the determinant of a first-order matrix, and the square of a first-order equation. Boundary: this is the determinant of the regular matrix, a matrix computation; the doubling is the regular representation's two chiral copies, not a prediction of doubled particles, and the substitution of the derivative for the coefficient is the legitimate substitution of commuting partial derivatives.

- **The root is the clock.** The three root families give three transforms: the central root gives ordinary complex time–frequency analysis, a real pure-unit root gives the quaternion Fourier transform, and a non-trivial root gives the genuinely biquaternionic transform with its four complex factors. The root chooses which imaginary direction is the frequency axis, that is, which clock the analysis uses. Boundary: the algebra prefers no root; the central root is distinguished only by being central, and it is the framework's clock.

- **Frequency is the rate of the clock.** With the central root the kernel is the one-parameter group $\exp(-2\pi i\omega t')e_t$, and the angle is $2\pi\omega t'$ up to the sign of the exponent. The frequency is the rate of that group, and the spectrum is the group read parameter by parameter. Boundary: the interpretation supplies no $\hbar$ and no physical frequency until a time unit is chosen; it is a clock interpretation, not a measurement.

- **The conjugate axis is an imaginary direction.** The variable conjugate to a material coordinate enters the kernel through a root of $-1$ and not through a real number: the derivative is mapped to the root times a real frequency, so the momentum operator is a root of $-1$ times a real frequency. An imaginary direction is a conjugate direction, not a direction of propagation; on the informational hypothesis it is informational rather than spatial. Boundary: the imaginary directions are not extra spatial dimensions; the informational sector is not the Fourier dual of the material one.

- **The interval is the symbol, and the mass shell is its level set.** In the frequency variables the d'Alembertian acts as a multiplier, and the symbol is the interval read there. On the material sector it vanishes on the light cone, so the transform of a massless solution is supported on the cone; its level sets are the mass shells, and the mass labels the level. Boundary: the identification is the interval in the conjugate variables, up to the constant and the sign of the transform convention; it predicts no mass spectrum. On the whole algebra the symbol is a complex quadratic form, and the Minkowski cone appears only on the material sector.

- **The transform is a change of description, not a measurement.** The kernel is invertible, and the transform pair has an explicit inverse on the functions for which it holds, so the passage to the frequency description loses no information there. The sector exchange is the quarter turn inside the group the transform integrates, and the group is not the exchange. Boundary: the transform is not a state and not a measurement; it does not identify the informational sector as the Fourier dual of the material sector.

- **The positivity of the transform is the positivity of the Hermitian form, not of the norm.** With the biquaternion norm the value at the central coefficient $i$ is $\langle i\rangle_{\natural}=-1$, for every root, so the norm is indefinite and negative on the centre. With the Hermitian form the quadratic form of the transform is positive definite exactly for the degenerate roots, and it fails for every genuinely complex root. Boundary: the repair is a definite form and not the norm of the product; the criterion needs central coefficients and a single root; the norm failure and the root failure are different statements.

- **The vanishing norm is where the transform ceases to be invertible.** The transform is invertible on functions of non-vanishing norm; on functions that take zero-divisor values on a set of positive measure, invertibility is not guaranteed. The zero-divisor cone is therefore the locus where the Fourier description can lose information. Boundary: restricting to $\mathbb{H}_{\mathbb{B}}$ is sufficient, and on $\mathbb{M}_-$ the transform is invertible exactly for values off the cone; the precise condition for a general function that takes zero-divisor values on a set of positive measure is open, and the article does not claim the transform is non-invertible on every cone-valued function.

## Limits

- **No theorem is added.** The derivative conventions, the products, the forms, the norms, the transform and its properties are the mathematics articles'; the article states them in brief and interprets them.
- **No dynamics.** The Maxwell equation and the kinetic density are restatements of interpretations owned by the physics corpus; the article supplies no constitutive law, no equation of motion and no prediction.
- **One d'Alembertian, one sign.** The partner operator is not a second propagating operator; the Green's functions and the propagation are the physics article's.
- **The symbol is the interval only up to convention.** The constant and the sign depend on the transform convention; the mass shell is a level set, not a mass spectrum.
- **No preferred root.** The central root is distinguished only by being central; the non-central roots are rotated clocks, not errors.
- **The transform is not a measurement.** It is invertible where the transform pair holds, it loses no information there, and it does not make the informational sector the Fourier dual of the material one.
- **The imaginary directions are conjugate, not spatial.** The article does not add dimensions and does not identify an imaginary direction with a direction of propagation.
- **The positivity repair is a form, not the norm.** The Hermitian form is definite; the biquaternion norm is indefinite, and the two failures are distinct.
- **The vanishing-norm condition is open in general.** The article states the $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_-$ restrictions and does not claim a necessary and sufficient criterion for a general function that takes zero-divisor values on a set of positive measure.
- **The discrete case is cited, not developed.** The interpretations are the continuous ones; the discrete transform has the same shape, and the $\mathrm Z$ transform is left to its mathematics article.

## Summary

The analysis block has one first-order operator, the gradient $\tilde\nabla$, and one second-order operator, the d'Alembertian $\Box=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$. The four general products read on the gradient give the divergence, the gradient and the curl, four forms and two second-order norms; the d'Alembertian is the quaternionic and Hermitian norm, $\partial^2/\partial Q_t^2+\Delta_Q$, and on the material sector it is $\Delta-c^{-2}\partial^2/\partial {t'}^2$. The regular matrix of the gradient has determinant $\Box^2$, and its chiral block has determinant $\Box$: the second-order wave operator is the determinant of a first-order operator.

The Fourier transform is generated by a root of $-1$: the root is the clock, the frequency is its rate, the conjugate axis is an imaginary direction of the algebra, and the interval is the symbol of the d'Alembertian, with the mass shell as its level set. The transform is a change of description, not a measurement; it is invertible where the transform pair holds, and it does not make the informational sector the Fourier dual of the material one. The transform of a positive measure is not positive definite for the biquaternion norm, because the norm is indefinite and negative on the centre; with the Hermitian form, positivity holds exactly for the degenerate roots and fails for the genuinely complex ones. The vanishing norm marks the cone where the transform is not guaranteed to be invertible; the precise condition is open.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra; real dimension eight, complex dimension four |
| $e_t,\vec e_x,\vec e_y,\vec e_z$; $i$ | Quaternion units; the central imaginary |
| $\partial/\partial Q_\mu$ | Coordinate derivative; a subscript is never a derivative |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\partial/\partial Q_\mu$ | Quaternion conjugate of the gradient; also its Hermitian conjugate |
| $\nabla$, $\nabla\cdot\vec Q$, $\nabla\times\vec Q$ | Spatial gradient, divergence and curl |
| $\Delta_Q=\sum_k\partial^2/\partial Q_k^2$ | Laplacian in the three vector coordinates |
| $\Box=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$ | d'Alembertian, $\partial^2/\partial Q_t^2+\Delta_Q$ |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$ | Plain and quaternionic bilinear forms |
| $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | Hermitian and Krein forms |
| $\rho$, $\rho^2=-e_t$ | Root of $-1$; families $\pm i$, $\pm\hat\mu$, $b\hat\mu+d\hat\nu i$ |
| $W(t',\omega)=\exp(-2\pi\rho\omega t')$ | Fourier kernel; $\cos(2\pi\omega t')e_t-\sin(2\pi\omega t')\rho$ |
| $F(\omega)$, $f(t')$ | Transform and inverse transform |
| $\mathbb{M}_-$, $\tilde R=ict'\,e_t+\vec r$ | Material sector and material coordinate |
| $\omega_\mu$; $\omega$, $\vec k$ | Frequencies conjugate to $Q_\mu$; physical frequency and wavevector |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace and its imaginary translate |

## Further Reading

- [Conventions in Mathematics](../articles_maths/conventions-in-mathematics.html), for the derivative conventions and the gradient.
- [The Differential Operators, the Products, the Forms and the D'Alembertian](../articles_maths/the-differential-operators-the-products-the-forms-and-the-d-alembertian.html), for the four products, forms and norms on the gradient.
- [Biquaternion Analysis](../articles_maths/biquaternion-analysis.html), for the gradient, its conjugate and the d'Alembertian at length.
- [The 4 Forms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternioid-c-space.html) and [The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.html), for the forms and the norms.
- [Introduction to the 4×4 Matrix Element Representation of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the regular matrix, its determinant and its blocks.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) and [Square Roots of a General Element in the Biquaternion Algebra](../articles_maths/square-roots-of-a-general-element-in-the-biquaternion-algebra.html), for the roots of $-1$.
- [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html), for the transform, the factorization, the symbol, the vanishing norm and the measure.
- [Biquaternion Discrete Harmonic Analysis](../articles_maths/biquaternion-discrete-harmonic-analysis.html), for the discrete transform and the $\mathrm Z$ transform.
- [The Bochner Theorem for the Biquaternioid Transform: the Hermitian Form and the Root](../articles_maths/the-bochner-theorem-for-the-biquaternioid-transform-the-hermitian-form-and-the-root.html), for the positivity criterion.
