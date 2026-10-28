# __The Hamilton Pairing: Mass as Modulus and the Complex Angle__

## Introduction

The Hamilton pairing writes an element as a complex scalar times the exponential of a complex angle:

$$
\boxed{\;\tilde Q=\Rho\,e^{\vec U\Theta}=\Rho\bigl(\cos\Theta+\vec U\sin\Theta\bigr),
\qquad
\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}},\qquad
\vec U=\frac{\vec Q}{B},\qquad
B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}\;}.
$$

It is the only one of the three pairings whose first factor is central, and the only one whose first factor is a scalar. That single fact is what makes it the natural home for an invariant: a central scalar is the one thing that a change of frame cannot touch.

The thesis is one sentence. **The Hamilton modulus $\Rho$ is the invariant of the element — the mass when the element is a four-momentum and the complex amplitude otherwise — and the second factor is the frame, a Lorentz transformation whose angle $\Theta$ is real for a rotation, imaginary for a boost and complex in general.** Two consequences follow and are the substance of the article. The mass is not the energy: the energy is a component of the four-momentum in a frame, and the modulus is the invariant left when the frame is divided out. And the angle is not a single number with a single convention: the spinor word stores $\psi/2$, the four-vector factor stores $\psi$, and the modulus may itself be imaginary, so the pair $(\Theta,\vec U)$ is the invariant object and $\Theta$ alone is not.

The article is a synthesis. The pairing, its theorem and its domain are owned by *The Hamilton Root Pairing of the Polar Decomposition of Biquaternions*; the eigenvalue decomposition and the mass shell by *The Biquaternion Eigenvalue Decomposition* and *The Spectral Reading of a Four-Vector*; the branch of the modulus by *The Polar Decomposition of a N-Regular Biquaternion*. What is added here is the physical reading of the first factor, the anatomy of the complex angle, and the boundaries of the mass identification.

The conventions are those of *Conventions in the Biquaternion Universe*, §*The Polar Word and the Three Pairings*, including its warning on the four objects called a boost. The norm is $\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, the Hermitian form is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, the trace is $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$, and the state glyph is $\tilde{Ϛ}$. The symbol $B$ here is the square root of the vector-part square, not the four-vector boost factor $\mathcal B$.

## The Results It Uses

| result | established in | used here for |
|---|---|---|
| the Hamilton pairing, its theorem and its domain | **The Hamilton Root Pairing of the Polar Decomposition of Biquaternions**, §*The Statement*, §*The Domain* | $\tilde Q=\Rho e^{\vec U\Theta}$, the axis and the angle |
| the eigenvalues $\lambda_\pm=Q_t\pm iB$ and the norm identity | [*The Biquaternion Eigenvalue Decomposition*](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), §*The Eigenvalues* | $\lambda_\pm=\Rho e^{\pm i\Theta}$ and $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}$ |
| the four factors and the branch of the modulus | [*The Polar Decomposition of a N-Regular Biquaternion*](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), §*The Four Factors* | $\Rho=r e^{i\alpha}$ with $\alpha\in(-\pi/2,\pi/2]$ |
| the four-momentum and the mass shell | [*The Spectral Reading of a Four-Vector*](the-spectral-reading-of-a-four-vector.html), §*The Frame Dependence* | $\Rho=i mc$, $\Theta=-i\psi$, $\vec U=\hat p$ |
| the four objects called a boost and the factor of two | [*Conventions in the Biquaternion Universe*](conventions-in-the-biquaternion-universe.html), §*The Four Objects Called a Boost* | the $\psi/2$ versus $\psi$ warning |
| multiplicativity of the norm | [*The Polar Decomposition of a N-Regular Biquaternion*](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), §*The Two Factors* | the modulus of a product |
| the generalized pairing on the null cone | [*The Polar Decomposition of a N-Degenerate Biquaternion*](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html), §*The Vanishing of the Modulus* | the massless limit |

## The Pairing

The pairing is the grouping of the scale and the phase against the boost and the rotor:

$$
\tilde Q=\Rho\,\exp(\vec U\Theta),
\qquad
\Rho=r\,e^{i\alpha},
\qquad
\exp(\vec U\Theta)=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}.
$$

The modulus is central and complex. The second factor is a unit-norm element, and the unit-norm subgroup of $\mathbb{B}$ is $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group $SO^{+}(1,3)$. The exponent is a complex multiple of a root of $-e_t$: the axis $\vec U$ is a unit pure element with $\vec U^{2}=-e_t$, and $\Theta$ is complex.

The two eigenvalues of the element are the polar form of the spectrum,

$$
\boxed{\;\lambda_\pm=Q_t\pm iB=\Rho\,e^{\pm i\Theta},
\qquad
\lambda_+\lambda_-=\Rho^{2}=\langle\tilde Q\rangle_{\natural}\;}.
$$

The product identity is the reason the modulus is an invariant: the two eigenvalues are the two light-cone combinations of the element, and their product is the norm. The sum, $2Q_t$, is the trace and is frame-dependent for a four-momentum; the product is not.

The representation is a statement about $\tilde Q$, not about $\exp\tilde Q$. The element and its exponential are different objects with different moduli and different angles, and the logarithm, not the exponential, recovers $(\Rho,\Theta)$ from the element. The corpus must keep the two apart, and the distinction is stated in the mathematical article.

## The Central Modulus

The modulus is

$$
\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}=r\,e^{i\alpha},\qquad \alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}] .
$$

It is central, so it commutes with every element and is unchanged by a change of frame implemented by conjugation. It is the only one of the three first factors with that property. The quaternion factor $r\tilde u_{\mathrm r}$ and the Cartan factor $r\tilde U_{\mathrm b}$ both carry frame data and both change under conjugation; $\Rho$ does not.

The phase of $\Rho$ carries the causal character when the norm is real.

| norm | modulus | phase | reading |
|---|---|---|---|
| $\langle\tilde Q\rangle_{\natural}>0$ | $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}>0$ | $0$ | spacelike element |
| $\langle\tilde Q\rangle_{\natural}<0$ | $\Rho=i\sqrt{\lvert\langle\tilde Q\rangle_{\natural}\rvert}$ | $\pi/2$ | timelike element |
| $\langle\tilde Q\rangle_{\natural}=0$ | $\Rho=0$ | undefined | null element |
| $\langle\tilde Q\rangle_{\natural}\in\mathbb{C}$ general | $\Rho=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{1/2}e^{i\arg\langle\tilde Q\rangle_{\natural}/2}$ | $\tfrac12\arg\langle\tilde Q\rangle_{\natural}$ | general element |

For a four-momentum the norm is $\langle\tilde P\rangle_{\natural}=-m^{2}c^{2}$ and the modulus is $\Rho=i mc$ on the principal branch. The two eigenvalues are

$$
\boxed{\;\lambda_\pm=i mc\,e^{\pm\psi}=i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right)\;},
$$

the two light-cone combinations, and their product is $-m^{2}c^{2}$. The mass shell is the level set of the modulus, not of the trace.

### Mass or Amplitude

The word "mass" is licensed by the object, not by the algebra.

- For a **four-momentum** $\tilde P=i(E/c)e_t+\vec p$, the modulus is $i mc$ and the invariant is the mass. This is the only case in which the reading is forced by the corpus's identification of $\tilde P$ with the four-momentum.
- For a **general element**, $\Rho$ is the invariant complex amplitude. Calling it a mass is an extra identification, and the article must say so. A field strength, a Jones matrix and a scattering element all have a Hamilton modulus; none of them has a mass unless a dynamics supplies one.

The distinction is not pedantic. The modulus is multiplicative under composition, while mass is not additive under the addition of four-momenta, and conflating the two produces false conservation statements. The next section makes the point exactly.

## The Complex Angle

The angle is defined by the two ratios

$$
\cos\Theta=\frac{Q_t}{\Rho},\qquad \sin\Theta=\frac{B}{\Rho},
\qquad B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}} .
$$

The pair $(\Theta,\vec U)$ is the invariant data of the second factor; $\Theta$ alone is not, because the sign of the axis flips the sign of the angle and leaves the element unchanged. The angle has three regimes.

| $\Theta$ | second factor | process | example |
|---|---|---|---|
| real | a rotation | compact rotation | $e^{\theta\vec u/2}$ |
| imaginary | a boost | non-compact boost | $e^{-i\psi\hat p}$ |
| complex | a rotation composed with a boost | general Lorentz element | aligned or skew word |

The classification is of the angle, not of $B$. The ratio $B/\Rho$ is what enters $\sin\Theta$, and a real $B$ with an imaginary $\Rho$ gives an imaginary angle. The four-momentum is the standard case: $B=\lvert\vec p\rvert$ is real, $\Rho=i mc$ is imaginary, and $\Theta=-i\psi$ is imaginary, which is the boost.

### The Factor of Two

The angle depends on which factor of the word the element carries, and the factor of two is the most common error in the corpus.

- The **spinor word** of a transformation carries the frame rotor $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$, whose exponent angle is $\psi/2$. On an aligned word with a rotation, $\Theta=\tfrac{\theta}{2}+\epsilon i\tfrac{\psi}{2}$.
- The **four-vector factor** is $\mathcal B=\tilde U_{\mathrm b}^{-2}=\exp(-i\psi\hat p)$, whose exponent angle is $-\psi$. A four-momentum carries this factor, and its Hamilton angle is $\Theta=-i\psi$, not $-i\psi/2$.
- The **word parameter** of a four-vector element is $\psi_w=2\psi$, because the word stores the boost twice.

Three statements follow, and each is a check. Do not write $\Theta=i\psi$ for a four-momentum; the sign is negative for the axis along the momentum. Do not write $\psi/2$ for the angle of a four-momentum; the four-vector factor carries the full rapidity. Do not identify the exponent angle of the spinor word with the exponent angle of the four-vector word; they differ by a factor of two and a sign.

### The Angle Is Not the Rapidity

The imaginary part of $\Theta$ has magnitude $\psi$, the kinematic rapidity, when the element is a four-momentum. For a general element the imaginary part is not a rapidity: it is the boost part of a complex angle whose real part is a rotation, and on skew axes the two parts do not align on a single axis. The statement "the imaginary part is the rapidity" is a statement about the four-momentum chart, not about the algebra.

The reality of the angle is also not the reality of the element. A rotation has a real angle and a real quaternion element; a boost has an imaginary angle and an imaginary vector part. The pair $(\Rho,\Theta)$ is the coordinate, and neither member alone classifies the element.

## The Frame Factor

The second factor is a unit-norm element, and it is the frame. Its action depends on the object it acts on, and the corpus separates the two laws.

- On a **spinor**, the unit factor acts by left multiplication, $\chi\mapsto\tilde U\chi$. This is the linear action and it carries the double cover and the sign of the spinor.
- On a **four-vector**, it acts by congruence, $X\mapsto\tilde U X\tilde U^{*}$. This is the bilinear action, and the four-vector element carries the inverse square of the spinor factor.

For a four-momentum the frame factor is $\mathcal B=e^{-i\psi\hat p}$ and the congruence by $\mathcal B$ is the boost of rapidity $\psi$ about $-\hat p$. The Hamilton axis $\vec U=\vec Q/B$ points along the momentum; the word's axis in $\mathcal B$ points opposite it. Both statements describe the same boost, and the sign is bookkeeping.

The rapidity is fixed by the ratio of the two invariants,

$$
\cosh 2\psi=\frac{\langle\tilde Q,\tilde Q\rangle_{*}}{\lvert\langle\tilde Q\rangle_{\natural}\rvert},
$$

for a four-momentum, where the numerator is the Hermitian square. The ratio is $\cosh\psi_w$, not $\cosh\psi$: the factor of two is already present in the Hermitian norm. This is the frame datum that the modulus does not carry. The modulus gives the mass; the ratio gives the rapidity; the phase of the four complex coordinates gives the two axis angles. The count is the same as in the hub: two invariants fix three numbers, and the directions need the phases.

## The Domain and the Witnesses

The Hamilton pairing needs $\langle\tilde Q\rangle_{\natural}\neq0$ and $B\neq0$. The second condition is not implied by the first, and the witness is

$$
\tilde Q=e_t+\vec e_x+i\vec e_y,\qquad \langle\tilde Q\rangle_{\natural}=1,\qquad B^{2}=1+i^{2}=0 .
$$

The element is invertible, the word exists, the quaternion factor exists, and the Hamilton factor does not: there is no axis and no angle. The failure has two physical faces.

- **The scalar case.** $\vec Q=0$ is the rest frame of a four-momentum. The axis is undefined because there is no boost to point it along; the angle is $0$ or $\pi$ and carries only the sign. The rest frame is the boundary of the chart, not a physical singularity: the element is regular and its mass is $\Rho$.
- **The nilpotent case.** $\vec Q\neq0$ with $\vec Q^{2}=0$ is a lightlike vector part. There is no frame in which the vector part is a pure scale, and the axis cannot be normalised. The element may still be invertible, as the witness shows.

The two cases are different. The scalar four-momentum is the $\psi\to0$ limit of a boost; the nilpotent case is a lightlike vector part, the boundary of the boost chart, and the two have different stabilisers. The algebra distinguishes them by $\vec Q=0$ and $\vec Q^{2}=0$ with $\vec Q\neq0$.

The third boundary is the null cone, $\langle\tilde Q\rangle_{\natural}=0$, where the modulus vanishes and the pairing does not exist. For a four-momentum this is the massless limit: the element is lightlike, the mass shell collapses to the cone, and the word has no rest frame. The generalized Cartan pairing covers the limit with a rank-one amplitude and a partial isometry, and the massless article owns the boundary value.

## Mass, Not Energy

The modulus is the invariant and the energy is not. For a four-momentum,

$$
E=mc^{2}\cosh\psi,\qquad \lvert\vec p\rvert=mc\sinh\psi,\qquad \langle\tilde P\rangle_{\natural}=-m^{2}c^{2}.
$$

The energy depends on the frame through $\psi$; the modulus does not. The trace $2Q_t=2iE/c$ is the frame-dependent sum of the eigenvalues; the norm is their frame-independent product. A change of frame moves $\psi$ and hence $E$, and leaves $\Rho$ fixed. This is the algebraic content of "mass is invariant, energy is a component".

The modulus is **multiplicative** under composition. For any two elements,

$$
\langle\tilde Q\tilde Q'\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde Q'\rangle_{\natural},
$$

so the modulus of a product is the product of the moduli up to the branch. This is a statement about multiplying operators, not about adding four-momenta. Four-momenta compose by addition, $\tilde P_{\mathrm{tot}}=\tilde P_1+\tilde P_2$, and the mass of a sum is not the sum or the product of the masses: it is the modulus of the sum, which depends on the angle between the momenta. The invariant mass of a two-particle system is

$$
\langle\tilde P_1+\tilde P_2\rangle_{\natural}=\langle\tilde P_1\rangle_{\natural}+\langle\tilde P_2\rangle_{\natural}+2\langle\tilde P_1,\tilde P_2\rangle_{\natural},
$$

and the cross term is what makes the mass of a system differ from the sum of its parts. The multiplicativity of the algebra and the additivity of the four-momentum are different operations. The mass shell is the level set of the norm, a property of one element, not of the sum.

This is the precise form of the caution. The Hamilton modulus is the invariant of one element. It is not a charge, it is not additive, and it does not compose by the rule that four-momenta compose. The algebra gives multiplicativity; physics gives the addition; the mass shell is the level set of the norm that both must respect.

## Physical Interpretation

The Hamilton pairing is the orbit picture in one line: **a particle is a rest value times a Lorentz transformation.** The rest value is the modulus, the transformation is the frame factor, and the product is the element. The reading is sharpest for a four-momentum and weakest for a general element, and the article has stated where each reading is licensed.

| question | Hamilton datum | reading |
|---|---|---|
| what is the invariant? | $\Rho$ | the mass of a four-momentum, the amplitude otherwise |
| what is the frame? | $\vec U$, $\Theta$ | the Lorentz transformation that carries the rest value to the element |
| what is the rapidity? | $\lvert\operatorname{Im}\Theta\rvert$ on the four-momentum chart | the boost parameter $\psi$ |
| what is the spin? | the rotation part of $\Theta$ | the compact angle of the frame |

The complex angle is the natural home for analytic continuation. A rotation continued to an imaginary angle is a boost; the single formula $\cos\Theta+\vec U\sin\Theta$ covers both, with the trigonometric and hyperbolic cases as the real and imaginary sections. This is not a new dynamics. It is the statement that the two kinds of Lorentz transformation are two sections of one complexified family, and that the algebra does not need two formulas.

The reading that changes the theory most is the identification of the modulus with the mass. It gives the mass shell an algebraic definition — the level set of the norm — and it makes the invariant mass a property of the element rather than of a frame. The reading that must be guarded most is the same one: for a general element the modulus is an amplitude, and the mass word is an identification that the algebra does not make.

## What This Does Not Claim

- It does not claim that $\Rho$ is a mass for every element. The mass reading is licensed for a four-momentum; for a general element $\Rho$ is a complex amplitude.
- It does not claim that mass is additive. The modulus is multiplicative under operator composition; four-momenta add; the mass of a sum is the modulus of the sum.
- It does not claim that the imaginary part of $\Theta$ is always the rapidity. That reading is specific to the four-momentum chart.
- It does not claim that the angle alone is invariant. The pair $(\Theta,\vec U)$ is the invariant data, and the sign of the axis flips the sign of the angle.
- It does not claim that the Hamilton pairing exists on the whole complement of the cone. It also needs $B\neq0$, and the witness $e_t+\vec e_x+i\vec e_y$ is invertible without a Hamilton factor.
- It does not claim that the rest frame is a singularity. It is the boundary of the chart, and the element is regular there.
- It does not claim that the exponential of the element is the element. The modulus and angle of $\tilde Q$ are not those of $\exp\tilde Q$.

## Summary

- The Hamilton pairing is $\tilde Q=\Rho\exp(\vec U\Theta)=\Rho(\cos\Theta+\vec U\sin\Theta)$.
- The modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}=r e^{i\alpha}$ is central and complex; it is the only scalar first factor of the three pairings.
- The eigenvalues are $\lambda_\pm=Q_t\pm iB=\Rho e^{\pm i\Theta}$, and their product is the norm.
- For a four-momentum, $\Rho=i mc$, $\Theta=-i\psi$, $\vec U=\hat p$, and the eigenvalues are $i mc\,e^{\pm\psi}$.
- The energy is $mc^{2}\cosh\psi$ and depends on the frame; the modulus is the invariant and does not.
- The angle is real for a rotation, imaginary for a boost and complex in general; the pair $(\Theta,\vec U)$ is the invariant data.
- The spinor word stores $\psi/2$, the four-vector factor stores $\psi$, and the four-momentum angle is $-i\psi$.
- The pairing needs $\langle\tilde Q\rangle_{\natural}\neq0$ and $B\neq0$; the scalar rest frame and the nilpotent lightlike case are different boundaries.
- The modulus is multiplicative under composition; mass is not additive under the addition of four-momenta; the mass of a sum carries a cross term.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the biquaternion norm |
| $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}=r e^{i\alpha}$ | the Hamilton modulus, central and complex |
| $r$, $\alpha$ | the scale and the central phase, $\alpha\in(-\pi/2,\pi/2]$ |
| $\vec U=\vec Q/B$ | the Hamilton axis, a unit pure element, $\vec U^{2}=-e_t$ |
| $B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}$ | the vector-part square root (not the boost factor $\mathcal B$) |
| $\Theta$ | the complex angle, $\cos\Theta=Q_t/\Rho$, $\sin\Theta=B/\Rho$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, $\lambda_\pm=\Rho e^{\pm i\Theta}$ |
| $\psi$ | the kinematic rapidity of a four-momentum |
| $\tilde U_{\mathrm b}(\psi)$ | the frame rotor, exponent angle $\psi/2$ |
| $\mathcal B=\tilde U_{\mathrm b}^{-2}$ | the four-vector boost factor, exponent angle $-\psi$ |
| $\tilde P=i(E/c)e_t+\vec p$ | the four-momentum, $\Rho=i mc$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hermitian form |
| $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$ | the trace |

## Further Reading

- *The Hamilton Root Pairing of the Polar Decomposition of Biquaternions*, for the theorem, the domain and the roots of one.
- [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), for the spectrum, the eigenprojections and the multiplicativity of the norm.
- [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four-factor word and the branch of the modulus.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the comparison with the quaternion and Cartan first factors.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the mass shell and the eigenvalues of a four-momentum.
- [The Roots of a General Element: Mass, Frames and the Mass Shell](the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html), for the mass as a modulus and the isospectral family.
- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), §*The Four Objects Called a Boost*, for the rapidity conventions and the factor of two.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the hub and the action of the factors.
- [The Null Four-Momentum: What the Cone Derives and What It Does Not](the-null-four-momentum-what-the-cone-derives-and-what-it-does-not.html), for the massless limit.
