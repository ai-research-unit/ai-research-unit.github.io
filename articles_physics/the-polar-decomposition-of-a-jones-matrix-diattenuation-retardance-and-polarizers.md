# __The Polar Decomposition of a Jones Matrix: Diattenuation, Retardance and Polarizers__

## Introduction

A Jones matrix is a $2\times2$ complex matrix that carries the transverse electric field of a monochromatic beam through a linear optical element. The corpus reads the same object as a biquaternion: the algebra is isomorphic to $M_2(\mathbb{C})$, the matrix acts on the two-component Jones vector, and composition of elements is composition of optical elements. This article reads the polar decomposition of that element and gives its optical names.

The decomposition is the **Cartan pairing**. A general Jones matrix is neither Hermitian nor unitary, so the quaternion and Hamilton pairings do not apply to it in general; the Cartan pairing does, and on the invertible elements it is unique. Its two factors are the two independent optical anisotropies: a Hermitian positive **diattenuator**, which transmits two orthogonal polarizations with different amplitudes, and a unitary **retarder**, which delays them by different phases.

The article states the correspondence, computes the standard optical parameters from the factors, and treats the boundary case. A polarizer is a rank-one Jones matrix. It lies on the zero-divisor cone, where the norm vanishes, the element is not invertible, and the classical Cartan pairing stops. The generalized Cartan pairing continues there with a positive semidefinite factor and a partial isometry, and the polarizer becomes the canonical example of that extension.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The element image $\mathsf{M}_2(\tilde J)$ and the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ | [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](../articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html) |
| The Cartan pairing $\tilde J=\tilde H\tilde U$, the positive factor and the unitary factor | [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html) |
| The generalized pairing on the cone, the partial isometry and its projections | [The General Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone](../articles_maths/the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html) |
| The eigenvalue decomposition, the eigenprojections and the rank-one case | [Eigenvalue Decomposition and Eigenbasis of a Biquaternion](../articles_maths/eigenvalue-decomposition-and-eigenbasis-of-a-biquaternion.html) |
| The norm, the invertibility criterion and the zero-divisor cone | [Norm Regularity and Degeneracy in the Biquaternion Algebra, §The Group of Units](../articles_maths/norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| The unitary group and its matrix model | [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html) |
| The square root of a positive element | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |

The physical sources are *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form* for the Jones vector, the Stokes parameters and the coherency biquaternion, *The Cartan Pairing, the Amplitude and the Operator-to-State Map* for the state that an operator defines, and *The Matrix Images: Mixedness, Rapidity and the Phase Fibre* for the singular values of the amplitude.

## The Jones Matrix as a Biquaternion

A monochromatic plane wave propagating along $\vec e_z$ has a transverse electric field

$$
\vec E=(E_x,E_y,0),\qquad E_x,E_y\in\mathbb{C}.
$$

Its polarization is the ray of the **Jones vector** $\vec J=(E_x,E_y)$; two vectors that differ by an overall complex phase describe the same polarization. A linear optical element acts by a $2\times2$ complex matrix,

$$
\vec J_{\mathrm{out}}=\mathsf{J}\,\vec J_{\mathrm{in}},
$$

and the matrix $\mathsf{J}$ is the **Jones matrix** of the element. Composition of elements is matrix multiplication, in the order in which the light meets them.

The matrix is an element of the algebra. Choose the element image of the algebra on the spinor module, $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$; it is an isomorphism, and every Jones matrix is the image of exactly one biquaternion $\tilde J$. The optical element, the biquaternion and the matrix are three names for one object. Hermitian conjugation of the element is the conjugate transpose of the matrix,

$$
\mathsf{M}_2(\tilde J^{*})=\mathsf{M}_2(\tilde J)^{\dagger},
$$

so the star is the operation that the optics uses.

The norm is the determinant. For an element $\tilde J$ the biquaternion norm is $\langle\tilde J\rangle_{\natural}=\det\mathsf{M}_2(\tilde J)$, a complex number in general. The three elementary optical elements are distinguished by it and by the conjugation:

| element | biquaternion condition | optical name |
| --- | --- | --- |
| Hermitian, positive | $\tilde J=\tilde J^{*}$, spectrum $\ge0$ | diattenuator |
| unitary | $\tilde J\tilde J^{*}=e_t$ | retarder |
| rank one | $\langle\tilde J\rangle_{\natural}=0$, $\tilde J\neq0$ | polarizer |

A general Jones matrix is none of the three. It is not Hermitian, because it has both amplitude and phase anisotropy, and it is not unitary, because it absorbs. Its norm is a general complex number: a pure retarder has $\lvert\langle\tilde J\rangle_{\natural}\rvert=1$, an ideal polarizer has $\langle\tilde J\rangle_{\natural}=0$, and a general element lies between them. The element is therefore outside the domains of the quaternion and Hamilton pairings, which need a real-quaternion factor and a non-null vector part respectively; the Cartan pairing is the one that applies.

## The Cartan Pair

For an invertible Jones matrix the Cartan pair is

$$
\boxed{\;\tilde J=\tilde H\tilde U,\qquad
\tilde H=\sqrt{\tilde J\tilde J^{*}},\qquad
\tilde U=\tilde H^{-1}\tilde J\;}.
$$

The factor $\tilde H$ is Hermitian positive and the factor $\tilde U$ is unitary. The pair is unique: the positive square root is unique, and the unitary factor is then fixed. In the matrix image this is the polar decomposition $\mathsf{J}=\mathsf{H}\mathsf{U}$, with $\mathsf{H}$ positive definite and $\mathsf{U}$ unitary.

**The optical order.** With the column-vector convention, $\tilde J=\tilde H\tilde U$ acts as $\tilde U$ first and $\tilde H$ second: a retarder followed by a diattenuator. The optics literature more often writes the reverse order, $\mathsf{J}=\mathsf{J}_{\mathrm R}\mathsf{J}_{\mathrm D}$, a diattenuator followed by a retarder. That is the right polar form, $\mathsf{J}=\mathsf{V}\mathsf{P}$ with $\mathsf{P}=\sqrt{\mathsf{J}^{\dagger}\mathsf{J}}$ and $\mathsf{V}$ unitary; it has the same unitary factor, $\mathsf{V}=\mathsf{U}$, and the positive factor $\mathsf{P}=\mathsf{U}^{\dagger}\mathsf{H}\mathsf{U}$, which is $\mathsf{H}$ in the frame of $\mathsf{U}$. The principal transmissions and the retardance are therefore independent of the order convention; only the axis of the diattenuator is rotated by the retarder. This article uses the corpus's left form and states the order when it matters.

**The parameter count.** A Jones matrix has eight real parameters. The pair has four in $\tilde H$ and four in $\tilde U$, and the decomposition is a bijection on the invertible elements. One of the four in $\tilde U$ is the central phase, which is invisible in the optical response, so the physical element has seven parameters: the transmission scale, the diattenuation and its axis, the retardance and its axis. The count is the optical content of the uniqueness statement.

**On the cone.** When $\langle\tilde J\rangle_{\natural}=0$ the element is not invertible and $\tilde H^{-1}$ does not exist. The generalized pair replaces the inverse by the Moore–Penrose inverse, the positive factor by a positive semidefinite one, and the unitary factor by a partial isometry:

$$
\boxed{\;\tilde J=\tilde H_{\mathrm{pos}}\tilde U_{\mathrm p},\qquad
\tilde H_{\mathrm{pos}}=\sqrt{\tilde J\tilde J^{*}},\qquad
\tilde U_{\mathrm p}=\tilde H_{\mathrm{pos}}^{+}\tilde J\;}.
$$

The pair is unique once the projections of $\tilde U_{\mathrm p}$ are fixed to be those of $\tilde J$. On the cone the positive factor becomes a scaled projection and the partial isometry carries one polarization direction to one output direction.

| element | pair | what the pair defines |
| --- | --- | --- |
| $\langle\tilde J\rangle_{\natural}\neq0$ | $\tilde H>0$, $\tilde U$ unitary | diattenuation and retardance |
| $\langle\tilde J\rangle_{\natural}=0$, $\tilde J\neq0$ | $\tilde H_{\mathrm{pos}}\ge0$, $\tilde U_{\mathrm p}$ partial isometry | diattenuation, no retardance |
| $\tilde J=0$ | $\tilde H_{\mathrm{pos}}=0$, $\tilde U_{\mathrm p}=0$ | neither |

## Diattenuation

The diattenuator is the factor that transmits the two eigenpolarizations with different amplitudes. Its spectral decomposition is

$$
\tilde H=T_1\tilde\Pi_+(\vec u_H)+T_2\tilde\Pi_-(\vec u_H),\qquad
\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u),\qquad T_1\ge T_2\ge0,
$$

with orthogonal eigenpolarizations $\vec u_H$ and $-\vec u_H$. The eigenvalues $T_1,T_2$ are the **principal amplitude transmissions**; their squares are the principal intensity transmissions. The mean intensity transmission is $\bar T=\tfrac12(T_1^{2}+T_2^{2})$, and the **diattenuation** is

$$
\boxed{\;D=\frac{T_1^{2}-T_2^{2}}{T_1^{2}+T_2^{2}}\in[0,1]\;}.
$$

A pure retarder has $T_1=T_2$, hence $D=0$; an ideal polarizer has $T_2=0$, hence $D=1$.

The positive Hermitian factor has a second reading in the algebra. Every positive Hermitian element is a scale times a boost,

$$
\tilde H=\tau\left(\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_H\right),\qquad
\tau=\sqrt{T_1T_2},\qquad \psi=\ln\frac{T_1}{T_2},
$$

with eigenvalues $\tau e^{\pm\psi/2}=T_1,T_2$. The diattenuation is the hyperbolic tangent of this rapidity,

$$
D=\tanh\psi .
$$

The half-angle is the boost-factor convention: the eigenvalues are the exponentials of $\pm\psi/2$, while the transmission ratio is $e^{\psi}$. The diattenuation axis $\vec u_H$ is the boost axis of the amplitude. This is a reading of the Cartan parameter, not a claim that the optical element moves at a velocity.

**The boundary.** The reading requires $\tilde H$ positive. A Hermitian Jones matrix with a negative eigenvalue is not a physical diattenuator, because it would multiply an intensity by a negative number; the polar decomposition never produces one, since $\tilde H$ is a positive square root.

## Retardance

The retarder is the unitary factor. Its spectral decomposition is

$$
\tilde U=\exp(i\phi_1)\tilde\Pi_+(\vec u_U)+\exp(i\phi_2)\tilde\Pi_-(\vec u_U),
$$

and the **retardance** is the phase difference

$$
\boxed{\;\delta=\phi_1-\phi_2 \pmod{2\pi}\;}.
$$

The eigenpolarizations $\vec u_U$ and $-\vec u_U$ are the **retarder axes**; one is fast and one is slow, and the sign convention for $\delta$ fixes which is which. The global phase $\tfrac12(\phi_1+\phi_2)$ is not a retardance. It is the central phase of the element and has no optical consequence.

The unitary factor splits into that phase and a real rotor,

$$
\tilde U=\exp(i\alpha)\tilde u_{\mathrm r},\qquad
\alpha=\tfrac12(\phi_1+\phi_2),\qquad
\tilde u_{\mathrm r}=\cos\frac{\delta}{2}+\sin\frac{\delta}{2}\,\vec u_U .
$$

The rotor is a real quaternion of unit norm, and its eigenvalues are $\exp(\pm i\delta/2)$. **The retardance is twice the exponent angle of the rotor**, and the rotor is the half-angle object that the double cover of the rotation group requires. A rotor with exponent angle $\pi/2$ is a retardance of $\pi$, not $\pi/2$.

**The boundary.** The retardance is defined modulo $2\pi$ and its sign depends on the labelling of the two axes. The unitary factor of a polarizer is a partial isometry, not a unitary element, so a polarizer has no retardance: one of its two eigenvalues is zero and the phase difference is not defined.

## Polarizers and the Cone

An ideal polarizer has a rank-one Jones matrix. In the algebra it is an idempotent, $\tilde J=\tilde\Pi(\vec u)$ up to a scale, and its norm vanishes:

$$
\tilde\Pi(\vec u)^{2}=\tilde\Pi(\vec u),\qquad
\tilde\Pi(\vec u)^{*}=\tilde\Pi(\vec u),\qquad
\langle\tilde\Pi(\vec u)\rangle_{\natural}=0 .
$$

It is a zero divisor: it kills the orthogonal polarization and cannot be inverted. With $\tilde\Pi(\vec u)=\tilde\Pi_+(\vec u)=\tfrac12(e_t+i\vec u)$, the scalar $\tfrac12$ normalisation makes it a pure state of the informational sector, and the same element is read as a polarizer here and as a pure state there.

The classical Cartan pair does not exist at the polarizer, because $\tilde H^{-1}$ does not. The generalized pair does:

$$
\tilde H_{\mathrm{pos}}=\tilde\Pi(\vec u),\qquad
\tilde U_{\mathrm p}=\tilde\Pi(\vec u),\qquad
\tilde J=\tilde\Pi(\vec u)\tilde\Pi(\vec u).
$$

The positive factor is the final projection and the partial isometry is the same projection; both are rank one. A rank-one element with different input and output rays is $\tilde J=\sigma\lvert f\rangle\langle i\rvert$ with $\sigma>0$ and normalised rays; it has $\tilde H_{\mathrm{pos}}=\sigma\tilde\Pi_f$ and $\tilde U_{\mathrm p}=\lvert f\rangle\langle i\rvert$, a partial isometry from the input ray to the output ray. It is a polarizer along $i$ followed by a unitary transformation that carries $i$ to $f$, with the amplitude $\sigma$, and the two projections are the two pure states that the element connects.

**Absorption is monotone.** The rank of a product cannot exceed the rank of a factor, so a polarizer anywhere in a sequence leaves the output rank one. The light that the polarizer absorbs is not recovered by anything downstream; the subsequent elements can rotate and attenuate the surviving polarization but cannot restore the killed component. This is the optical form of the statement that a zero divisor forgets a direction.

**The optical parameters at the wall.** A polarizer has $D=1$ and no retardance. It is the limit of a diattenuator as $T_2\to0$, and the limit is singular: inside the cone the pair of a Hermitian diattenuator is $(\tilde H,\tilde U)=(\tilde J,e_t)$, while at the wall it is $(T_1\tilde\Pi_1,\tilde\Pi_1)$. The unitary factor jumps from the identity to a projection. The discontinuity is the rank drop, and it is the same discontinuity that the generalized pairing records on the cone.

## Relation to the Mueller Matrix

The Jones matrix acts on the Jones vector, which describes a fully polarized beam. A partially polarized or depolarized beam is described by a coherency matrix, and a linear element acting on it by a $4\times4$ real Mueller matrix acting on the Stokes vector. The two descriptions are not independent.

For a non-depolarizing element the Mueller matrix is the real image of the same element acting by congruence on the coherency matrix, and it is determined by the Jones matrix up to the global phase. It carries no additional information: the diattenuation and the retardance are read from it, and the polar decomposition is the factorisation of the Jones matrix that makes them separate. The Mueller matrix of a depolarizing element is not the image of any single Jones matrix; it is a sum of conjugations, and the polar decomposition of one term does not describe the whole.

The operator-to-state map is the bridge between the two readings. For an input state $\tilde{Ϛ}_{\mathrm{in}}$, the output is

$$
\tilde{Ϛ}_{\mathrm{out}}=\frac{\tilde J\tilde{Ϛ}_{\mathrm{in}}\tilde J^{*}}{2\langle\tilde J\tilde{Ϛ}_{\mathrm{in}},\tilde J\rangle_{*}}.
$$

For unpolarized input, $\tilde{Ϛ}_{\mathrm{in}}=\tfrac12e_t$, the output is $\tilde J\tilde J^{*}/2\langle\tilde J,\tilde J\rangle_{*}$, which is exactly the state that the operator defines. Diattenuation is the anisotropy of that state; retardance cancels from it.

## Worked Example

Take the Jones matrix

$$
\mathsf{J}=\begin{pmatrix}1&0\\0&i/2\end{pmatrix},
$$

a quarter-wave retardance on the second axis followed by a diattenuator of transmissions $1$ and $\tfrac12$. Its Cartan factors are

$$
\mathsf{H}=\begin{pmatrix}1&0\\0&\tfrac12\end{pmatrix},\qquad
\mathsf{U}=\begin{pmatrix}1&0\\0&i\end{pmatrix},
$$

so $T_1=1$, $T_2=\tfrac12$, $\bar T=\tfrac58$, and

$$
D=\frac{1-\tfrac14}{1+\tfrac14}=0.6,\qquad
\tau=\sqrt{\tfrac12}=0.707106781,\qquad
\psi=\ln2=0.693147181 .
$$

The check $D=\tanh\psi=\tanh 0.693147181=0.6$ holds. The unitary factor has eigenvalues $1$ and $i$, so its retardance is $\delta=\pi/2$, its central phase is $\alpha=\pi/4$, and its rotor has exponent angle $\pi/4$. The norm is $\langle\tilde J\rangle_{\natural}=\det\mathsf{J}=i/2$, with modulus $\tfrac12$, which equals $\langle\tilde H\rangle_{\natural}=\det\mathsf{H}$.

For unpolarized input the output state is

$$
\tilde{Ϛ}_{\mathrm{out}}=\frac{\mathsf{J}\mathsf{J}^{\dagger}}{2\langle\tilde J,\tilde J\rangle_{*}}
=\begin{pmatrix}0.8&0\\0&0.2\end{pmatrix},
$$

with Bloch vector length $0.6$ and purity $\tfrac12(1+0.6^{2})=0.68$. The Bloch length equals the diattenuation, and the purity is fixed by it: the element prepares a state whose degree of polarization is its diattenuation.

A pure retarder contrasts with this. Take $\mathsf{J}=\operatorname{diag}(1,i)$: then $\mathsf{H}=\mathrm{I}_2$, $\mathsf{U}=\mathsf{J}$, $D=0$, $\delta=\pi/2$, and the output state for unpolarized input is $\tfrac12\mathrm{I}_2$, maximally mixed. A retarder changes the phase of each polarization but not the intensity of either, so it cannot polarize unpolarized light. Only the diattenuator can.

## Physical Interpretation

The polar decomposition separates the two things a linear element can do to polarization. It can **change the amplitudes** of two orthogonal directions, and it can **change their relative phase**. The first is diattenuation, the second retardance, and the Cartan factors are the two operations in a canonical order. Every other optical description — the Jones matrix, the Mueller matrix, the coherency matrix — is a rewriting of the same pair with some information discarded.

Three readings follow from the algebra.

- **Diattenuation is a purity.** For unpolarized input, the output state has Bloch length $D$ and purity $\tfrac12(1+D^{2})$. The diattenuator is the part of the element that prepares a state; a polarizer prepares a pure state, and a pure retarder prepares the maximally mixed state.
- **Retardance is a fibre.** It rotates the state along its phase orbit and leaves the degree of polarisation, and hence the purity, invariant. The operator-to-state map discards it: the output for unpolarised input does not see it. It is visible in the element and invisible in the state's spectrum.
- **The cone is the wall.** Polarizers are the zero divisors, the pure states and the non-invertible elements at once. The ideal polarizer is the point where the reversible description fails and the generalized description takes over.

**The boundary of the interpretation.** The decomposition is canonical, but it is not a claim that the physical device is built of two plates in that order. Any factorisation of a matrix into a positive and a unitary factor is unique only when the factors are restricted to those classes; a real device has one Jones matrix, and the split is a canonical rewriting of it. The order of the factors is a convention, and the physics is in the pair, not in the order. The article also treats a single frequency: a real element has a Jones matrix per frequency, and dispersion is outside the single-matrix description.

## What This Does Not Claim

- **No derivation of the Jones calculus.** The matrix action, the Jones vector and the Stokes parameters are standard classical optics, cited as such.
- **No depolarization.** A depolarizing element is not a single Jones matrix. The Mueller matrix and the coherency matrix are the objects there, and the polar decomposition of one Jones matrix does not apply.
- **No frequency dependence.** The element is a matrix at one frequency. Birefringence and dichroism as functions of frequency, and the Kramers–Kronig relations that tie them, are not read here.
- **No quantum interpretation.** The light is a classical Maxwell field. The algebra is shared with the quantum two-level system, and the state language is the same, but no photon, no measurement postulate and no quantisation is used.
- **No claim that every element splits into two physical plates.** The split is a canonical factorisation of the matrix, not a blueprint of the device.

## Summary

A Jones matrix is a biquaternion, and its Cartan pair is its optical decomposition:

$$
\tilde J=\tilde H\tilde U,\qquad
\tilde H=\sqrt{\tilde J\tilde J^{*}}\ge0,\qquad
\tilde U=\tilde H^{-1}\tilde J\ \text{unitary}.
$$

The Hermitian positive factor is the **diattenuator**. Its eigenvalues $T_1\ge T_2\ge0$ are the principal amplitude transmissions, its eigenpolarizations are the principal axes, its mean intensity transmission is $\tfrac12(T_1^{2}+T_2^{2})$, and its diattenuation is $D=(T_1^{2}-T_2^{2})/(T_1^{2}+T_2^{2})=\tanh\psi$, where $\psi$ is the rapidity of the amplitude read as a boost. The unitary factor is the **retarder**. Its eigenvalues are $\exp(i\phi_{1,2})$, its eigenpolarizations are the retarder axes, its retardance is $\delta=\phi_1-\phi_2$, and its central phase is the unobservable global phase; the retardance is twice the exponent angle of the real rotor $\tilde u_{\mathrm r}$ in $\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}$.

The polarizer is the boundary case. It is a rank-one element, hence a zero divisor with $\langle\tilde J\rangle_{\natural}=0$, hence non-invertible; the classical pair does not exist, and the generalized pair gives $\tilde H_{\mathrm{pos}}=\tilde\Pi_f$ and $\tilde U_{\mathrm p}=\lvert f\rangle\langle i\rvert$. Its diattenuation is one and its retardance is undefined. The operator-to-state map reads the same structure: for unpolarized input the output state is $\tilde J\tilde J^{*}/2\langle\tilde J,\tilde J\rangle_{*}$, its Bloch length is $D$, and its purity is $\tfrac12(1+D^{2})$. A retarder alone leaves that state maximally mixed.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde J$, $\mathsf{J}$ | the Jones matrix as a biquaternion and as its $2\times2$ image |
| $\vec J=(E_x,E_y)$ | the Jones vector of the beam |
| $\tilde H$, $\mathsf{H}$ | the diattenuator, the Hermitian positive factor |
| $\tilde U$, $\mathsf{U}$ | the retarder, the unitary factor |
| $T_1,T_2$ | the principal amplitude transmissions, $T_1\ge T_2\ge0$ |
| $\bar T$ | the mean intensity transmission, $\tfrac12(T_1^{2}+T_2^{2})$ |
| $D$ | the diattenuation, $(T_1^{2}-T_2^{2})/(T_1^{2}+T_2^{2})$ |
| $\psi$ | the rapidity of the amplitude, $\ln(T_1/T_2)$ |
| $\delta$ | the retardance, the phase difference of the unitary factor |
| $\alpha$ | the central phase of the unitary factor |
| $\tilde u_{\mathrm r}$ | the real rotor of the retarder, angle $\delta/2$ |
| $\tilde\Pi_\pm(\vec u)$ | the spectral projectors $\tfrac12(e_t\pm i\vec u)$; $\tilde\Pi_+$ is the ideal polarizer |
| $\langle\tilde J\rangle_{\natural}$ | the biquaternion norm, equal to $\det\mathsf{J}$ |

## Further Reading

- [Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html), for the Jones vector, the Stokes parameters and the coherency biquaternion.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the Cartan pairing in the corpus's notation and its comparison with the quaternion and Hamilton pairings.
- [The Cartan Pairing, the Amplitude and the Operator-to-State Map](the-cartan-pairing-amplitude-and-the-operator-to-state-map.html), for the state that an operator defines and its purity stratigraphy.
- [The Matrix Images: Mixedness, Rapidity and the Phase Fibre](the-matrix-images-mixedness-rapidity-and-the-phase-fibre.html), for the singular values of the amplitude and the determinant as a volume.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the theorem and its uniqueness.
- [The General Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone](../articles_maths/the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html), for the extension to the cone and the polarizer.
- [Eigenvalue Decomposition and Eigenbasis of a Biquaternion](../articles_maths/eigenvalue-decomposition-and-eigenbasis-of-a-biquaternion.html), for the spectral decomposition of the factors.
- [The Unit Group, the Cone and the Orders](the-unit-group-the-cone-and-the-orders.html), for the partition that the polarizer sits on.
- Max Born and Emil Wolf, *Principles of Optics* (Cambridge, 7th edn, 1999), for the Jones calculus, the Stokes parameters and the polar decomposition of optical elements.
