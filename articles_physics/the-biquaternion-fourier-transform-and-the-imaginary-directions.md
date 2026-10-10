# __The Biquaternion Fourier Transform and the Imaginary Directions__

## Introduction

The mathematics corpus develops the biquaternion Fourier transform twice, in *Biquaternion Discrete Harmonic Analysis* and *Biquaternion Continuous Harmonic Analysis*. Both are written as pure mathematics: the kernel, the transform pair, the factorisation into complex transforms, the convolution theorem, the vanishing-norm issue and the relation to the differential operators, the discrete article adding the $\mathrm{Z}$ transform. This article proves nothing about the transform. It records the **physical reading** that the transform can carry in the framework, and it separates that reading from what the transform does not say.

Two facts organise the reading, and both are algebraic.

The first is the **generator**. The kernel of the transform is $\exp(-2\pi\rho\,\omega t)$ with $\rho^{2}=-e_0$, and the central choice $\rho=i$ makes it the central exponential $e^{-2\pi i\omega t}$. That is the one-parameter group $e^{i\theta}e_0$ of the centre, the angle being $\theta=2\pi\omega t$ up to the sign that the kernel's exponent carries. The companion article *Conventions in the Biquaternion Universe* reads that group as the global phase, as the duality rotation and as the Wick rotation, and the transform is the same generator read on a coordinate.

The second is the **conjugate variable**. The variable conjugate to a material coordinate enters the kernel through a root of $-1$ and not through a real number. The whole of the physical reading turns on two sentences, one algebraic and one interpretive: the conjugate axis of a material coordinate is an imaginary direction of the algebra, and on the informational hypothesis an imaginary direction is a conjugate direction and not a spatial one.

The article is organised as follows. The kernel and the root are recalled. The conjugate axis is read. The operators that the transform diagonalises are read, with the interval as their symbol. The choice of root is read as a choice of clock. The failure of positivity is recorded, and a closing section states what the reading does and does not claim.

## The Kernel and the Root

Fix a root of $-1$, an element $\rho\in\mathbb{B}$ with

$$
\rho^{2}=-e_0 .
$$

The **biquaternion Fourier kernel** is the biquaternion exponential

$$
W(t,\omega)=\exp(-2\pi\rho\,\omega t),
$$

and because $\rho^{2}=-e_0$ it closes on two terms,

$$
W(t,\omega)=\cos(2\pi\omega t)\,e_0-\sin(2\pi\omega t)\,\rho .
$$

The kernel is therefore a **rotation**: the two coefficients are the cosine and the sine of one real angle, and what the multiplication by $W$ does to a signal is a rotation in the plane spanned by $e_0$ and $\rho$. The root is the axis of that rotation and the frequency $\omega$ is its rate.

Its inverse is the same expression with the sine reversed,

$$
W(t,\omega)^{-1}=\cos(2\pi\omega t)\,e_0+\sin(2\pi\omega t)\,\rho ,
$$

and the identity $WW^{-1}=(\cos^{2}+\sin^{2})e_0=e_0$ uses only $\rho^{2}=-e_0$: it holds for every root. This is the reason the transform is a **change of description and not a measurement**. The kernel that performs the reading is invertible, so the passage to the conjugate variable loses nothing; the loss of information in the framework has other owners, and it is not this map.

### Unitarity and the Pure Root

The roots of $-1$ fall into three families — the central imaginary $\rho=\pm i$, the unit pure real quaternions $\rho=\pm\mu_{\mathbb{R}}$, and the non-trivial roots $\rho=b\mu+d\nu i$ with $\mu\perp\nu$ and $b^{2}-d^{2}=1$ — and two of the algebraic properties of the kernel depend on the family.

**For a pure root** the kernel is unitary, its quaternion conjugate being its inverse,

$$
W(t,\omega)^{\natural}=\cos(2\pi\omega t)\,e_0+\sin(2\pi\omega t)\,\rho=W(t,\omega)^{-1},
$$

because $\rho^{\natural}=-\rho$ for a pure element, and its biquaternion norm is the identity,

$$
N\big(W(t,\omega)\big)=\cos^{2}(2\pi\omega t)+\sin^{2}(2\pi\omega t)=e_0 .
$$

**The central root is the exception.** The element $i$ is not pure — its scalar part is $i$ — and the kernel is then the central scalar

$$
W(t,\omega)=e^{-2\pi i\omega t}e_0 ,
$$

of unit modulus in the complex sense, whose inverse is its complex conjugate. The pure-root statements above are stated for a pure root and are not extended to it.

## The Conjugate Axis Is the Imaginary Axis

The transform pairs a coordinate with its conjugate variable, and the pairing is made by the root: the exponent of the kernel is $\rho\,\omega t$, the product of the coordinate $t$, of the conjugate variable $\omega$ and of the root $\rho$. In the ordinary complex case the root is the imaginary unit, and the pairing is the familiar one of position and momentum. In the biquaternion case the root is an element of the algebra, and the framework can read it.

The differential statement makes the placement of the root explicit. The transform diagonalises the partial derivative, taking it to multiplication by the root times the frequency,

$$
\partial_\mu \;\longmapsto\; 2\pi\rho\,\omega_\mu ,
$$

so that the **momentum operator is a root of $-1$ times a real frequency**. In ordinary complex quantum mechanics this is written $p=-i\hbar\partial$, with the same central imaginary, and the framework's reading is that this $i$ is a **direction of the algebra**. The conjugate variable itself is real; what the root supplies is the axis along which the pairing is made, and that axis is an imaginary direction.

The material coordinate of the series is

$$
\tilde Q=ict\,e_0+\mathbf x ,
$$

an element of the material sector $\mathbb{M}_-$ whose scalar coefficient is imaginary and whose vector part is real: the material time is imaginary and the material space is real, and the placement of the $i$ is the sector's. The conjugate variable of that coordinate enters through the root and not through a real number. On the informational hypothesis of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* the reading sharpens, because the imaginary directions are not extra spatial directions: the sector's own coordinates show the placement, the informational time being real while the informational space is imaginary, and the transform adds the complementary fact that **the imaginary directions are the conjugate directions**. Read this way, an imaginary axis is a conjugate axis and not a direction of propagation: it is the axis the root selects, along which the frequency and the wavevector are paired, and not a further direction in which anything travels.

The generator $i$ also **exchanges the two sectors**, $\mathbb{M}_-\leftrightarrow\mathbb{M}_+$, and the kernel at the quarter turn $\theta=\pi/2$ is that exchange. The generator and the transform are nevertheless not the same statement. The kernel is a superposition of the rotations of every angle, and a transform taken with the central root is a superposition of central rotations, so the sector exchange is the quarter turn **inside** the group that the transform integrates and not the transform itself. In particular the transform does not identify the informational sector as the Fourier dual of the material sector; the exchange is one element of the group, and the group is not the exchange.

## The Interval as a Symbol

The structural content of the continuous transform is that it diagonalises the constant-coefficient differential operators of the framework. The gradient $\tilde{\nabla}$ becomes multiplication by the biquaternion $2\pi\rho(\omega_0e_0+\omega_1e_1+\omega_2e_2+\omega_3e_3)$, and the d'Alembertian $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ becomes multiplication by a scalar, its **symbol**,

$$
\Box \;\longmapsto\; -4\pi^{2}\left(\omega_0^{2}-\omega_1^{2}-\omega_2^{2}-\omega_3^{2}\right) .
$$

The symbol is the interval read in the conjugate variables. It vanishes on the light cone, so that the transform of a solution of $\Box\tilde F=0$ is supported on the cone. The level sets of the symbol and of the interval are the same sets — the two differ by a constant factor and by the overall sign the convention carries — so the mass-shell condition $N(\tilde P)=-m^{2}c^{2}$ is the statement that the symbol takes a fixed value, and the **mass labels the level set**: the zero set of the symbol is the massless shell and its level sets are the massive shells.

This is the spectral form of two readings the corpus already carries. *The Interval as the Square and the Charge of the Material Composition* reads the interval as the square of a material composition and its mass shell as the level set $\{N=-m^{2}c^{2}\}$, and *Square Roots: the Local Complex Structure, the Light Cone and the Mass Shell* reads the mass shell as the fibre of the natural square over the scalar $-m^{2}c^{2}$. The transform adds the conjugate-variable form of the same statement: in the frequency variables the interval acts as a **multiplier** and not as a form, the transform is the basis in which it is diagonal, and the mass is the value it reads there. The support of a massless field on the cone and the level set of a massive one are the two ends of the same sentence.

## The Choice of Root: Which Clock the Analysis Uses

The root is not neutral, and the three families give three transforms of different nature. The central root gives the ordinary complex exponential and the transform reduces to the ordinary complex transform of each component, that is, to ordinary time–frequency analysis. A unit pure real quaternion gives the real-quaternion exponential, a rotation rotor, and the quaternion Fourier transform. A non-trivial root gives the genuinely biquaternionic transform, with its factorisation into four complex transforms.

The reading is that **the root is the choice of which imaginary direction plays the frequency axis**, that is, which clock the analysis uses. The central root uses the central clock, the same $i$ that generates the global phase, the duality rotation and the Wick rotation; a non-central root uses a rotation about a spatial axis as its clock. The framework's own clock, in *Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*, is the central one, and the reading here is that the central root is the clock of the transform while the non-central roots are rotated clocks of it. The reading is a reading: the algebra prefers no root, and the central root is distinguished only by being central, that is, by commuting with the whole algebra.

## The Positivity Failure and the Conjugate Form

The transform of a finite positive measure is **not** a positive-definite function for $\mathbb{B}$, and the reason is the indefiniteness of the norm. The Bochner-type identity reads

$$
\sum_{k,l}\bar A_kA_l\,G(\omega_k-\omega_l)=\int N\big(Z(\tilde Q)\big)\,d\mu(\tilde Q),
$$

with the biquaternion norm on the right, and the norm is negative on the centre: at zero frequency with the central coefficient $A_1=i$ the left-hand side is $-\mu(\mathbb{R}^{n})e_0$, negative for every non-zero measure. The positivity that a Bochner-type hypothesis needs is therefore absent, and it is not restored by any restriction to ordinary data: it fails at the element that makes the algebra biquaternionic. The repair replaces the norm by a definite form, non-negative but not the norm of the product.

The reading is that the conjugate space is where the **indefinite norm of the framework shows up as a failure of positivity**, and that the definite form which repairs it is the positive form the informational sector already uses. The momentum-space positivity that ordinary quantum theory takes for granted is not supplied by the biquaternion norm; it is supplied by the Euclidean, Hermitian pairing $H$, the framework's probability form, which the companion articles on the sesquilinear products own. The absent positivity is the same indefiniteness that the vanishing-norm issue records, read at a value of the norm rather than at its zero.

## What the Reading Does and Does Not Claim

- It does **not** add a theorem. The transform, its kernel, its factorisation, its vanishing-norm issue and its positivity failure are the mathematics articles', and are read here.
- It does **not** claim that the imaginary directions are spatial, nor that they are "extra dimensions". The claim is narrower: the imaginary directions are the conjugate directions of the transform, and on the informational hypothesis they are informational and not spatial.
- It does **not** claim that the informational sector is the Fourier dual of the material sector. The transform is generated by the sector-exchange map, the exchange is the quarter turn inside the group, and the group is not the exchange.
- It does **not** claim that the kernel is a state or that the transform is a measurement. The kernel is invertible, and the transform is a change of description.
- It does **not** claim a new prediction, a new coupling or a new field. It reorganises readings the corpus already carries.
- It does **not** claim a preferred root. The central root is distinguished only by being central.

## Physical Readings

The transform reads as a change of description generated by one clock. The kernel is an invertible rotation, the conjugate axis is an imaginary direction of the algebra, the interval is the symbol of the d'Alembertian and the mass is its level set, and the choice of root is the choice of clock the analysis uses. The failure of positivity of the transform of a measure is the indefiniteness of the biquaternion norm read at a value of the norm rather than at its zero, and the form that repairs it is the positive Hermitian form of the informational sector.

Six named readings belong with the section, each labelled.

- **Frequency reading.** The transform is the central one-parameter group $e^{i\theta}e_0$ read as a frequency: the angle is $\theta=2\pi\omega t$ up to the sign the exponent carries, so the frequency is the rate of the central clock and the spectrum is the group read parameter by parameter. Boundary: the reading is the clock reading of *Conventions in the Biquaternion Universe* with the frequency as its carrier, and it supplies no new generator.
- **Conjugate-direction reading.** The variable conjugate to a material coordinate enters the kernel through a root of $-1$ and not through a real number, so an imaginary direction is a conjugate direction and not a direction of propagation. Boundary: the reading does not make the imaginary directions spatial, and it does not identify the informational sector as the Fourier dual of the material one.
- **Symbol reading.** The transform is the basis in which the constant-coefficient operators are diagonal: the interval is the scalar symbol of the d'Alembertian, the mass labels its level set, and the mass shell is that level set, so in the frequency variables the interval acts as a multiplier and not as a form. Boundary: the reading is the conjugate-variable form of the interval and mass-shell readings and adds no theorem.
- **Frame-change reading.** The kernel is a rotation with an explicit inverse, so the transform is a change of description and not a measurement; the sector exchange is the quarter turn inside the group the transform integrates, and the group is not the exchange. Boundary: no information is lost by the transform, and the framework's own information loss has other owners.
- **Clock-choice reading.** The root is the choice of which imaginary direction plays the frequency axis: the central root uses the central clock, and a non-central root uses a rotation about a spatial axis as its clock. Boundary: the algebra prefers no root, and the central root is distinguished only by being central.
- **Positivity reading.** The transform of a measure is not positive definite because the norm is indefinite and negative on the centre, so the missing momentum-space positivity is the indefiniteness of the norm read at a value and not at its zero; the definite form that repairs it is the Hermitian form $H$ of the informational sector. Boundary: the repair is a definite form and not the norm of the product.

## Summary

The biquaternion Fourier transform is generated by a root of $-1$ and read on a coordinate, and its physics is the physics of that generator and of that coordinate. With the central root the kernel is the one-parameter group of the centre, $e^{-2\pi i\omega t}e_0$, which is the same generator that *Conventions in the Biquaternion Universe* reads as the global phase, the duality rotation and the Wick rotation; the transform is the generator read as a **frequency**. The conjugate variable enters the kernel through the root and not through a real number, so the **conjugate axis of a material coordinate is an imaginary direction**; on the informational hypothesis this is the sharp form of the reading that the imaginary directions are informational and not spatial, and they are conjugate directions rather than wavevectors. The transform diagonalises the framework's constant-coefficient operators: the gradient becomes multiplication by $2\pi\rho(\omega_0e_0+\omega_1e_1+\omega_2e_2+\omega_3e_3)$, the d'Alembertian by its scalar symbol,

$$
\Box \;\longmapsto\; -4\pi^{2}\left(\omega_0^{2}-\omega_1^{2}-\omega_2^{2}-\omega_3^{2}\right),
$$

which vanishes on the light cone, so that the interval acts as a multiplier, the mass labels the level set of the symbol and the mass shell is that level set — the conjugate-variable form of the readings of the interval and of the mass shell. The kernel is a rotation whose inverse is explicit, so the transform is a change of description and not a measurement; it is unitary for a pure root and of unit complex modulus for the central one. The choice of root is the choice of the clock the analysis uses, the central root being the central clock, which is a reading and not a preference of the algebra. The transform of a measure is not positive-definite for $\mathbb{B}$, because the norm is indefinite and negative on the centre; the definite form that repairs it is the Hermitian form of the informational sector, and the absent momentum-space positivity is the vanishing-norm indefiniteness read at a value of the norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra; real dim $8$, complex dim $4$ |
| $e_0,e_1,e_2,e_3$; $i$ | Quaternion units; the central imaginary |
| $\rho$, $\rho^{2}=-e_0$ | A root of $-1$; the three families are $\pm i$, the unit pure real quaternions, and the non-trivial roots |
| $W(t,\omega)=\exp(-2\pi\rho\,\omega t)$ | The Fourier kernel; $=\cos(2\pi\omega t)e_0-\sin(2\pi\omega t)\rho$ |
| $W(t,\omega)^{-1}$ | The inverse; $=\cos(2\pi\omega t)e_0+\sin(2\pi\omega t)\rho$, for every root |
| $N(\tilde Q)$ | The biquaternion norm; $N(W)=e_0$ for a pure root |
| $\tilde Q=ict\,e_0+\mathbf x$ | The material coordinate in $\mathbb{M}_-$ |
| $\partial_\mu\mapsto 2\pi\rho\,\omega_\mu$ | The diagonalisation of the derivative; the momentum operator |
| $\tilde{\nabla}$, $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | The biquaternionic gradient and the d'Alembertian |
| $-4\pi^{2}(\omega_0^{2}-\omega_1^{2}-\omega_2^{2}-\omega_3^{2})$ | The symbol of $\Box$; the interval in the conjugate variables |
| $\mathbb{M}_\pm$ | Material and informational sectors; exchanged by the central $i$ |

## Further Reading

- *Biquaternion Discrete Harmonic Analysis* and *Biquaternion Continuous Harmonic Analysis* — the mathematics of the transform: the kernel, the transform pair, the factorisation into complex transforms, the convolution and the Z transform, the relation to the gradient and the d'Alembertian, the two-unit kernel, and the failure of positivity for the transform of a measure.
- *Conventions in the Biquaternion Universe* — the central imaginary as one generator on the remarkable subspaces; the phase, the duality rotation, the Wick rotation and the exchange of the two sectors as its restrictions.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the informational reading of the imaginary vector part and the positive form that repairs the positivity.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the material coordinate and the interval.
- *The Interval as the Square and the Charge of the Material Composition* and *Square Roots: the Local Complex Structure, the Light Cone and the Mass Shell* — the interval as a square, the mass shell as a level set and as a fibre of the natural square.
- *The Parabolic Dirac Operator and the Fourier Reformulation of Maxwell's Equations* — the use of the transform on the differential operators in the electromagnetism category, which owns the PDE applications.
- *Conventions in the Biquaternion Universe* — the conventions of the series.
