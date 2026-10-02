# __The Fundamental Solution Operator__

## Introduction

On the whole space there is no boundary to impose a condition on, and the inverse of a differential operator with constant coefficients is not an integral operator with a kernel vanishing at the boundary but a **convolution**: if $E$ is a fundamental solution of $L$, so that $LE=\delta$, then the operator $T_E$ defined by $T_Ef=E*f$ satisfies $LT_E=I$ on the distributions for which the convolution is defined. The operator $T_E$ is the object of this article, the third of the inverses of this group; it is the inverse of $L$ on the whole space, and unlike the Green operator of a boundary-value problem it is not unique, because any solution of the homogeneous equation may be convolved in as well.

This article reads the fundamental solution of *Distributions and Fundamental Solutions* as an operator. It fixes the convolution operator of a distribution, on which spaces it acts and in which sense it inverts $L$; proves that $T_E$ is a left inverse of $L$ on the compactly supported functions and a right inverse on the compactly supported distributions exactly when $LE=\delta$; describes the operator for a constant-coefficient operator as the Fourier multiplier by the reciprocal of the symbol and reads from that the smoothing it produces; records the nonuniqueness and its cause, the difference of two fundamental solutions being a solution of the homogeneous equation; and passes to the variable-coefficient case through the parametrix, where the inverse exists only modulo a smoothing operator and the Fredholm alternative governs the failure.

The distributions, the convolution of distributions, the fundamental solution and the parametrix are those of *Distributions and Fundamental Solutions*; the convolution operator, its profile and its Fourier multiplier are those of *Convolution Operators*, where the operator with profile $k$ is written $T_k$, the same mark used here with profile $E$; the Fourier transform on $\mathbb{R}^n$ and the tempered distributions are those of *Distributions and Fundamental Solutions* and *Fourier Analysis on Euclidean Spaces*; the elliptic regularity and the Rellich–Kondrachov theorem that turn the parametrix into a compact perturbation are those of *Sobolev Spaces and Weak Solutions*. The heat semigroup and the wave propagator of a differential operator are the applications of the convolution operator recorded in *Convolution Operators* and *Unbounded Operators and Spectral Measures*; the Green operator of a boundary-value problem and the correction of the fundamental solution by the boundary term are *The Green Operator*; and the resolvent, whose kernel is the fundamental solution at the shifted operator when the space is the whole space, is *The Resolvent Operator*.

## The Convolution Operator of a Fundamental Solution

**Definition.** Let $L$ be a linear differential operator with constant coefficients on $\mathbb{R}^n$ and let $E\in\mathcal{D}'(\mathbb{R}^n)$ be a **fundamental solution** of $L$, that is $LE=\delta$. The **fundamental solution operator** is the convolution operator

$$
T_E : f\mapsto E*f ,
$$

defined on the distributions $f$ for which the convolution with $E$ is defined: on $\mathcal{E}'(\mathbb{R}^n)$ by the convolution theorem of *Distributions and Fundamental Solutions*, on $\mathcal{S}'(\mathbb{R}^n)$ when $E$ is tempered, and on $C_c^\infty(\mathbb{R}^n)$ by the action on the second factor.

**Theorem (the inverse property).** Let $E$ be a fundamental solution of the constant-coefficient operator $L$. Then

$$
L\,T_E = I \ \text{on } \mathcal{E}'(\mathbb{R}^n), \qquad T_E\,L = I \ \text{on } C_c^\infty(\mathbb{R}^n) ,
$$

the second identity meaning that $E*(Lf)=f$ for every compactly supported smooth $f$; more generally $T_EL=I$ on every space on which the convolution with $E$ and with $Lf$ is defined and on which the fundamental solution is admissible.

*Proof.* For $f\in\mathcal{E}'$ the operator $L$ may be brought under the convolution, $L(E*f)=(LE)*f=\delta*f=f$, which is the first identity. For the second, the identity $\partial^\alpha(E*g)=(\partial^\alpha E)*g$ for the convolution of a distribution with a compactly supported smooth function gives $E*(Lf)=\sum_\alpha a_\alpha E*(\partial^\alpha f)=\sum_\alpha a_\alpha(\partial^\alpha E)*f=(LE)*f=\delta*f=f$. The identity for the wider spaces is the same computation with the convolution defined.

**Theorem (right inverse and homogeneous part).** Let $E$ be a fundamental solution of $L$ and let $h$ be a distribution with $Lh=0$ for which the convolutions are defined. Then $E+h$ is again a fundamental solution, and

$$
(E+h)*f = E*f + h*f
$$

for every admissible $f$. Conversely, if $E$ and $E'$ are two fundamental solutions, then $h=E-E'$ satisfies $Lh=0$; the fundamental solution operator is therefore determined only up to convolution with a solution of the homogeneous equation, and a **special fundamental solution** is one selected by an extra condition, such as decay at infinity, or being tempered, or being supported in a given cone.

*Proof.* The first assertion is linearity: $L(E+h)=LE+Lh=\delta$. For the converse, $L(E-E')=\delta-\delta=0$ by linearity, so the difference solves the homogeneous equation. The selection of a special fundamental solution is the extra condition that picks the decay, the growth or the support.

**Example (the Newtonian potential operator).** Let $L=-\Delta$ and let $\Phi$ be the Newtonian potential of *Distributions and Fundamental Solutions*, $-\Delta\Phi=\delta$. Then $T_\Phi f=\Phi*f$ solves $-\Delta u=f$ for compactly supported $f$, and when $n\ge3$ it is the solution that vanishes at infinity; the general solution is $T_\Phi f+h$ with $h$ harmonic, and in the tempered class the ambiguity is exactly the harmonic polynomials. The operator $T_\Phi$ gains two derivatives: it maps the compactly supported distributions into $C^\infty$ away from the support of $f$, and it maps $H^s(\mathbb{R}^n)$ into $H^{s+2}_{\mathrm{loc}}(\mathbb{R}^n)$, so it inverts the Laplacian and improves regularity at the same time.

**Example (the heat and wave operators).** Let $L=\partial_t-\Delta$ on $\mathbb{R}^n\times\mathbb{R}$ and let $E$ be the heat kernel of *Distributions and Fundamental Solutions*. Then $T_E$ is the **heat semigroup**: $(T_Ef)(x,t)=\int E(x-y,t)f(y)\,dy$ for $t>0$, $T_E$ is a strongly continuous semigroup of contractions on $L^p$, and it solves the Cauchy problem of the heat equation. For the wave operator $\Box=\partial_t^2-\Delta_x$ the fundamental solution supported in the forward cone defines the **wave propagator**, and its finite support is finite propagation speed. Both operators are convolution operators of *Convolution Operators*, and their semigroup and group properties are those of *Unbounded Operators and Spectral Measures*.

### Composition and the Inverse of a Product

**Theorem (the inverse of a product).** Let $E_1$ and $E_2$ be fundamental solutions of the constant-coefficient operators $L_1$ and $L_2$. Then $E_1*E_2$ is a fundamental solution of the product $L_1L_2$, and

$$
T_{E_1}T_{E_2} = T_{E_1*E_2} = T_{E_2}T_{E_1} ,
$$

the operators composing by the convolution of their profiles, as in the profile algebra of *Convolution Operators*.

*Proof.* By the profile algebra the composition of the two convolution operators is the convolution with the profile $E_1*E_2$. For the fundamental-solution property,

$$
L_1L_2\,(E_1*E_2) = L_1\bigl((L_2E_2)*E_1\bigr) = L_1(\delta*E_1) = L_1E_1 = \delta ,
$$

using the constant coefficients to move $L_2$ onto $E_2$ and the convolution with $\delta$. The commutativity is that of convolution.

**Example (the semigroup law).** For the heat kernel $E_t(x)=(4\pi t)^{-n/2}e^{-|x|^2/(4t)}$ the composition theorem reads $E_t*E_s=E_{t+s}$, which is the semigroup law in kernel form, and $T_{E_t}T_{E_s}=T_{E_{t+s}}$ is the semigroup in operator form; the identity $\partial_t-\Delta_x$ applied to $E_t$ gives the delta at $(0,0)$ by the convolution theorem.

## The Symbol and the Multiplier

**Theorem (the Fourier multiplier).** Let $L$ have constant coefficients with symbol $\sigma_L(\xi)$, and let $E$ be a tempered fundamental solution. On the Schwartz space,

$$
\widehat{T_E f}(\xi) = \frac{\hat f(\xi)}{\sigma_L(\xi)} ,
$$

in the sense that the distribution $1/\sigma_L(\xi)$ is the Fourier transform of $E$ and multiplication by it is the action of $T_E$; the operator $T_E$ is the **Fourier multiplier** by $1/\sigma_L$.

*Proof.* Taking the Fourier transform of $E*f$ gives the product $\hat E\hat f$ for tempered distributions, and taking the transform of $LE=\delta$ gives $\sigma_L(\xi)\hat E(\xi)=1$, so $\hat E=1/\sigma_L$ in the sense of distributions; substituting gives the display. The multiplier acts on $\mathcal{S}$ or on $L^2$ according to whether $1/\sigma_L$ is a bounded function, and otherwise as an operator between the Sobolev spaces.

**Example (the classical multipliers).** The following table records the operator and its multiplier.

| Operator $L$ | Fundamental solution $E$ | Multiplier $1/\sigma_L(\xi)$ | Inverse on |
|---|---|---|---|
| $-\Delta$ | Newtonian potential $\Phi$ | $1/|\xi|^2$ | $\mathcal{S}$, up to harmonic term |
| $\partial_t-\Delta$ | heat kernel | $1/(i\tau+|\xi|^2)$ | causal $f$, $t>0$ |
| $\Box$ | cone-supported solution | $1/(\tau^2-|\xi|^2)$ | causal $f$ |
| $\partial_x$ | Heaviside step | $1/(i\xi)$ | $\mathcal{S}$ modulo constants |
| $1-d^2/dx^2$ | $\tfrac12e^{-|x|}$ | $1/(1+\xi^2)$ | all of $L^2$ |

The first four multipliers are unbounded at the zeros of the symbol and the operators gain derivatives or lose support; the last is bounded, and $T_E$ is a bounded operator on $L^2$ with norm $1$, the multiplier $1/(1+\xi^2)$ having supremum $1$. The gain of two derivatives by the Newtonian potential operator and the boundedness of the resolvent kernel of $1-d^2/dx^2$ are the two extremes: whether the inverse gains regularity or is bounded is decided by the behaviour of $1/\sigma_L$ at infinity and near its singularities.

**Theorem (uniqueness in the tempered class).** Let $L$ have constant coefficients. If the only tempered solution of $Lu=0$ is $u=0$, then $L$ has exactly one tempered fundamental solution and the tempered inverse $T_E$ is unique; in general two tempered fundamental solutions differ by a tempered solution of the homogeneous equation, and the tempered inversion is unique modulo that kernel.

*Proof.* If $E$ and $E'$ are tempered fundamental solutions, then $E-E'$ is tempered and $L(E-E')=0$, so it vanishes under the hypothesis; conversely a tempered solution $h$ of $Lh=0$ may be added to any fundamental solution, and $E+h$ is a fundamental solution because $L$ is linear. The operator $T_E$ therefore differs from $T_{E'}$ by $T_h$ on the distributions for which both are defined.

**Example (the primitive and the Hilbert transform).** For $L=\partial_x$ on $\mathbb{R}$ the Heaviside function $H$ is a fundamental solution, and $T_Hf(x)=\int_{-\infty}^x f(y)\,dy$ is the primitive vanishing at $-\infty$; it is not bounded on $L^2$, and the bounded operator that inverts the derivative on the line is the **Hilbert transform**, whose multiplier is $-i\,\mathrm{sgn}(\xi)$ and whose relation to the two one-sided primitives is the subject of *Real Harmonic Analysis*. The example shows that the choice of fundamental solution is a choice of boundary behaviour at infinity, not merely of formula.

## The Adjoint Fundamental Solution

**Definition.** Let $L$ be a differential operator with smooth coefficients on $\mathbb{R}^n$ and let $E$ be a fundamental solution of $L$. The **reflected conjugate** of $E$ is the distribution

$$
E^{\dagger}(x) = \overline{E(-x)} ,
$$

and it is the fundamental solution of the formal adjoint.

**Theorem (the adjoint fundamental solution).** If $LE=\delta$ then $L^{\dagger}E^{\dagger}=\delta$, where $L^{\dagger}$ is the formal adjoint of *Differential Operators*. If in addition $E\in L^1(\mathbb{R}^n)$, so that $T_E$ is bounded on $L^2(\mathbb{R}^n)$, then the adjoint of $T_E$ is the integral operator with kernel $\overline{E(y-x)}=E^{\dagger}(x-y)$, that is

$$
(T_E)^{\dagger} = T_{E^{\dagger}} ,
$$

and the operator $T_{E^{\dagger}}$ is the inverse of $L^{\dagger}$ in the same sense as $T_E$ is the inverse of $L$.

*Proof.* The kernel of $T_E$ is $K(x,y)=E(x-y)$, so the kernel of its adjoint is $\overline{K(y,x)}=\overline{E(y-x)}=E^{\dagger}(x-y)$, which is the kernel of $T_{E^{\dagger}}$; hence $(T_E)^{\dagger}=T_{E^{\dagger}}$. Applying the adjoint to the identity $LT_E=I$ gives $T_E^{\dagger}L^{\dagger}=I$, that is $T_{E^{\dagger}}L^{\dagger}=I$, and the general equivalence between $T_GL^{\dagger}=I$ and $L^{\dagger}G=\delta$ of the first theorem yields $L^{\dagger}E^{\dagger}=\delta$.

**Corollary (the self-adjoint case).** If $L=L^{\dagger}$ and $E$ is real-valued, then $E$ is even, $E(-x)=E(x)$, and the fundamental solution operator is a self-adjoint convolution operator. The Newtonian potential for $-\Delta$ and the kernel $\tfrac12e^{-|x|}$ for $1-d^2/dx^2$ are the instances.

*Proof.* The identity $L^{\dagger}E^{\dagger}=\delta$ with $L=L^{\dagger}$ and $E$ real reads $LE^{\dagger}=\delta$, so $E^{\dagger}$ is a fundamental solution of $L$; the difference $E-E^{\dagger}$ solves the homogeneous equation, and in the cases listed it vanishes because the fundamental solutions there are the ones selected by decay. Then $E^{\dagger}=E$, which is $E(-x)=E(x)$.

## The Parametrix and Approximate Inversion

**Definition.** Let $L$ have smooth variable coefficients on $\Omega$. A **parametrix** of $L$ is a distribution $E$ with

$$
L\,E = \delta - S ,
$$

where $S$ is a **smoothing operator**: $S$ maps the compactly supported distributions into $C^\infty$. The convolution reading fails for variable coefficients, but the **parametrix operator** $T_E$, defined locally by the action of $E$, remains meaningful and is an approximate inverse.

**Theorem (approximate inversion).** Let $E$ be a properly supported parametrix of $L$. Then

$$
L\,T_E = I - S , \qquad T_E\,L = I - S' ,
$$

where $S$ and $S'$ are smoothing operators, and on every Sobolev space of finite order the operators $S$ and $S'$ are compact. Consequently $L$ is **Fredholm** on the Sobolev scale: it has finite-dimensional kernel and cokernel, and $Lu=f$ is solvable exactly when $f$ is orthogonal to the kernel of the formal adjoint.

*Proof.* The identity $LT_E=I-S$ is the defining equation of the parametrix applied to the operator; the second, on the other side, follows from the parametrix being two-sided modulo smoothing, which is the statement that the remainders $I-T_EL$ and $I-LT_E$ have smooth kernels. A smoothing operator on a bounded domain gains all derivatives, hence is compact on each Sobolev space by Rellich–Kondrachov; an operator that is the identity modulo a compact operator is Fredholm, and the Fredholm alternative gives the solvability condition.

**Theorem (from the parametrix to the Green operator).** Let $\Omega$ be bounded with smooth boundary and let $E$ be a properly supported parametrix of the elliptic operator $L$ on a neighbourhood of $\overline\Omega$. Let $\chi$ be a cutoff equal to $1$ near the diagonal, and let $G$ be the solution operator of the boundary-value problem with the modified parametrix $\chi E$ and the boundary correction. Then $G$ is the Green operator of *The Green Operator*, the boundary correction removes the failure of $\chi E$ to satisfy the boundary condition, and the identity $LG=I$ holds exactly, not merely modulo smoothing, precisely when the homogeneous problem is trivial.

*Proof.* The cut-off parametrix $\chi E$ inverts $L$ modulo a smoothing operator on the interior; the boundary correction is the solution of a boundary-value problem that removes the boundary values of the remainder, and it exists when the homogeneous problem is trivial, by the invertibility criterion of *The Green Operator*. The exact identity then follows from the approximate one by solving away the smoothing remainder, and the difference between the parametrix and the Green operator is a smoothing operator.

**Example (the method of images).** For the half-space $\Omega=\{x : x_n>0\}$ with the Dirichlet condition the Green function of $-\Delta$ is

$$
G(x,y) = \Phi(x-y) - \Phi(x-y^*) , \qquad y^* = (y_1,\dots,y_{n-1},-y_n) ,
$$

where $\Phi$ is the Newtonian potential; the second term is the boundary correction and is the **image** of the fundamental solution reflected in the plane $x_n=0$. It vanishes on the boundary because $|x-y|=|x-y^*|$ for $x_n=0$, and it is harmonic in $y$ on the half-space because the reflected singularity $y^*$ lies outside it. This is the explicit instance of the correction theorem: the fundamental solution of the whole space, reflected once, produces the exact inverse under the boundary condition.

## Summary

The fundamental solution operator of a constant-coefficient differential operator $L$ is the convolution $T_Ef=E*f$ with a fundamental solution $E$, and it inverts $L$: $LT_E=I$ on the compactly supported distributions and $T_EL=I$ on the compactly supported functions, exactly when $LE=\delta$. It is not unique, because two fundamental solutions differ by a solution of the homogeneous equation, and a special fundamental solution is selected by decay, growth or support. On the Fourier side it is the multiplier by the reciprocal of the symbol, $\widehat{T_Ef}=\hat f/\sigma_L$, so the inverse gains derivatives when $1/\sigma_L$ grows, as for the Newtonian potential operator, and is bounded when $1/\sigma_L$ is bounded, as for the resolvent kernel of $1-d^2/dx^2$. The heat kernel makes $T_E$ the heat semigroup and the cone-supported solution makes it the wave propagator.

For an operator with variable coefficients the convolution reading fails and is replaced by the parametrix $E$ with $LE=\delta-S$ and $S$ smoothing; then $LT_E=I-S$ and $T_EL=I-S'$, the remainders are compact on every Sobolev space, and $L$ is Fredholm with the Fredholm alternative governing solvability. The Green operator of a bounded domain is obtained from the parametrix by a cutoff and a boundary correction, and the difference between the two is smoothing. The reflected conjugate $E^{\dagger}(x)=\overline{E(-x)}$ is a fundamental solution of the formal adjoint, $(T_E)^{\dagger}=T_{E^{\dagger}}$ when $E$ is integrable, and the fundamental solution of a product is the convolution of the fundamental solutions; the heat kernel makes this the semigroup law $E_t*E_s=E_{t+s}$, and the method of images is the boundary correction for the half-space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$ | Constant- or variable-coefficient differential operator |
| $E$ | Fundamental solution, or parametrix, of $L$ |
| $T_E$ | Fundamental solution operator, $f\mapsto E*f$ |
| $\delta$ | Delta distribution |
| $S$, $S'$ | Smoothing remainders of the parametrix |
| $\sigma_L(\xi)$ | Symbol of $L$ |
| $\Phi$ | Newtonian potential, fundamental solution of $-\Delta$ |
| $\Box$ | Wave operator $\partial_t^2-\Delta_x$ |
| $1/\sigma_L$ | Fourier multiplier of $T_E$ |
| $E^{\dagger}(x)=\overline{E(-x)}$ | Reflected conjugate, fundamental solution of $L^{\dagger}$ |
| $T_{E^{\dagger}}$ | Adjoint of $T_E$, inverse of $L^{\dagger}$ |
| $y^*$ | Image point $(y_1,\dots,y_{n-1},-y_n)$ for the half-space |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the fundamental solution, the parametrix and the calculus of symbols.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (Springer, 1983), for the parametrix with variable coefficients and the Fredholm property.
- Leon Ehrenpreis, *Fourier Analysis in Several Complex Variables* (Wiley, 1970), for the Ehrenpreis–Malgrange theorem and the exponential-polynomial solutions.
- Bernard Malgrange, *Lectures on the Theory of Distributions* (Springer, 2016), for the convolution of distributions and the fundamental solution in the constant-coefficient case.
- Elias M. Stein, *Singular Integrals and Differentiability Properties of Functions* (Princeton University Press, 1970), for the Riesz potentials, the multiplier theorems and the Sobolev gain of the Newtonian potential operator.
- Avner Friedman, *Partial Differential Equations* (Dover, 1997), for the fundamental solution, the heat and wave kernels and the solution of the Cauchy problems.
