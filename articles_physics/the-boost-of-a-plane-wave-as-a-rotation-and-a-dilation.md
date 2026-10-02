# __The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation__

## Introduction

A Lorentz boost acts on a plane wave in three apparently different ways: it shifts the frequency by the Doppler factor, it alters the propagation direction by aberration, and it rotates the polarisation. In the biquaternion algebra these are a single operation. The wave element and the field amplitude of a null wave are carried by a **spatial rotation composed with a dilation**, and the rotation and the dilation are the same for both.

The result is due to William E. Baylis (*Relativity in Introductory Physics*, Can. J. Phys. **82** (2004) 853–873, arXiv:physics/0406158), who derived it in the algebra of physical space and flagged it as the paper's new result on the boost of a wave. The present article states it in the conventions of this series and verifies it. Two objects enter: the **wave biquaternion** $\tilde{K}$, which is a null element of the material sector and whose coefficient of $i$ is the frequency, and the **field-strength biquaternion** $\tilde{F}$ of *The Field-Strength Biquaternion and Its Invariants*, which is a null pure vector. Written for a wave of direction $\hat{\mathbf k}$, wave speed $c$ and angular frequency $\omega$,

$$
\tilde{K} = \frac{\omega}{c}\left(i + \hat{\mathbf k}\right),
\qquad
N(\tilde{K}) = 0 ,
$$

which is the four-wavevector $\tilde{K} = \frac{i\omega}{c}e_0 + \mathbf k$ of the plane-wave exercise written with $\mathbf k = \frac{\omega}{c}\hat{\mathbf k}$. The claim is that for a boost with rotor $\tilde\Lambda = \cosh\frac{w}{2} + i\sinh\frac{w}{2}\hat{\mathbf u}$ (Hermitian, of unit norm, $w$ the rapidity and $\hat{\mathbf u}$ the boost direction) there is a **unit real quaternion** $\tilde{R}$ and a positive scalar $e^{d}$ for which

$$
\boxed{\;
\tilde{K}' \;=\; \tilde\Lambda\,\tilde{K}\,\tilde\Lambda^{*} \;=\; e^{d}\,\tilde{R}\,\tilde{K}\,\tilde{R}^{\natural},
\qquad
\tilde{F}' \;=\; \tilde\Lambda^{\natural}\,\tilde{F}\,\tilde\Lambda \;=\; e^{d}\,\tilde{R}\,\tilde{F}\,\tilde{R}^{\natural} .
\;}
$$

Since $\tilde{R}$ is a real quaternion, $\tilde{R}^{\natural} = \tilde{R}^{-1}$ and the action $\tilde{R}\,\cdot\,\tilde{R}^{\natural}$ is a **rotation of physical space**; the scalar $e^{d}$ is a dilation. A boost of a wave, then, is not a mixture of three effects but a similarity of Euclidean three-space, the same one acting on the wave element and on the field.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and the scalar imaginary $i$ central with $i^2 = -1$. A **real vector** is $\mathbf v = v_1e_1 + v_2e_2 + v_3e_3$ with the $v_k$ real; a hat denotes a unit vector, $\hat{\mathbf k}\hat{\mathbf k} = -e_0$. The scalar imaginary multiplies likewise, so $i\hat{\mathbf k}$ is imaginary-vector. The material sector $\mathbb{M}_-$ carries the four-vectors, the Hermitian sector $\mathbb{M}_+$ carries the boost rotors, and $i\mathbb{M}_+ = \mathbb{M}_-$. The field is taken in vacuum, $c = c_0$, where the source-free Maxwell system is Lorentz covariant and the field strength transforms in the bivector representation $\tilde{F}\mapsto\tilde\Lambda^{\natural}\tilde{F}\tilde\Lambda$ (*Exercise: Duality Rotation and the Riemann–Silberstein Vector*, Problem 5); the field-strength normalization cancels from the statement, which is homogeneous in $\tilde{F}$. Throughout, $\mathbf v$ is reserved for particle and frame velocities.

## The Null Wave Element and the Pacwoman Property

The one algebraic fact behind the result is a property of null elements that has come to be called the **pacwoman property**: a null element of the form $i+\hat{\mathbf k}$ "gobbles" factors of $\hat{\mathbf k}$.

**Lemma (pacwoman).** Let $\hat{\mathbf k}$ be a unit real vector. Then

$$
\hat{\mathbf k}\left(i + \hat{\mathbf k}\right) \;=\; \left(i + \hat{\mathbf k}\right)\hat{\mathbf k} \;=\; i\left(i + \hat{\mathbf k}\right).
$$

**Proof.** Expanding, $\hat{\mathbf k}(i + \hat{\mathbf k}) = i\hat{\mathbf k} + \hat{\mathbf k}\hat{\mathbf k} = i\hat{\mathbf k} - e_0$ using $\hat{\mathbf k}\hat{\mathbf k} = -e_0$ and the centrality of $i$; and $(i + \hat{\mathbf k})\hat{\mathbf k} = i\hat{\mathbf k} + \hat{\mathbf k}\hat{\mathbf k} = i\hat{\mathbf k} - e_0$. On the other hand $i(i + \hat{\mathbf k}) = i^2 + i\hat{\mathbf k} = i\hat{\mathbf k} - e_0$. The three expressions agree.

The lemma says that right-multiplication by $\hat{\mathbf k}$ acts on the null element $i+\hat{\mathbf k}$ exactly as multiplication by the scalar $i$ does. The name records the same statement in the form $k(1+k) = 1+k$ of the source, where $k$ is the null paravector $1+\hat{\mathbf k}$ of the algebra of physical space; in the series basis the null paravector is the Hermitian element $e_0 + i\hat{\mathbf k}$ and its gobbling factor is $i\hat{\mathbf k}$:

$$
\left(i\hat{\mathbf k}\right)\left(e_0 + i\hat{\mathbf k}\right) \;=\; \left(e_0 + i\hat{\mathbf k}\right)\left(i\hat{\mathbf k}\right) \;=\; e_0 + i\hat{\mathbf k}.
$$

**The nullity of the wave element.** The lemma is why $\tilde{K} = \frac{\omega}{c}(i+\hat{\mathbf k})$ has vanishing norm. Indeed $\tilde{K}^{\natural} = \frac{\omega}{c}(i-\hat{\mathbf k})$ and

$$
N(\tilde{K}) = \tilde{K}\tilde{K}^{\natural} = \frac{\omega^2}{c^2}\left(i+\hat{\mathbf k}\right)\left(i-\hat{\mathbf k}\right)
= \frac{\omega^2}{c^2}\left(i^2 - \hat{\mathbf k}\hat{\mathbf k}\right) = \frac{\omega^2}{c^2}\left(-1 + 1\right) = 0,
$$

because $\hat{\mathbf k}\hat{\mathbf k} = -e_0$. The null element is a zero divisor of $\mathbb{B}$ (*Biquaternion Zero Divisors*, *The Light Cone as the Biquaternion Zero-Divisor Cone*), and this is the algebraic form of the statement that light has no rest frame.

## The Null Flag and the Flagpole

The null element $e_0+i\hat{\mathbf k}$ has a geometric reading, due to Penrose, that the pacwoman lemma makes precise. A **null flag** in Minkowski space is a lightlike direction together with a plane containing it: the direction is the **flagpole**, and the plane is the **flag**. For the wave element the flagpole is the lightlike paravector $e_0+i\hat{\mathbf k}$ itself, and the flag is the two-plane transverse to $\hat{\mathbf k}$; the electric field of a plane wave lies in the flag, and the magnetic field is the flag swept along the flagpole as the wave propagates. Transversality of the electromagnetic field is the statement that the amplitude has no component along the flagpole; the pacwoman identity $i\hat{\mathbf k}(e_0+i\hat{\mathbf k}) = e_0+i\hat{\mathbf k}$ is the statement that the flagpole absorbs its own direction without leaving the null cone.

The flagpole is also a **pure state**. The element

$$
\tilde\Pi = \tfrac12\left(e_0 + i\hat{\mathbf k}\right)
$$

is idempotent, $\tilde\Pi^2 = \tilde\Pi$, and Hermitian, $\tilde\Pi^{*} = \tilde\Pi$, so it is a projector; and it is exactly the rank-one projector $\tilde\Pi_+(\hat{\mathbf k}) = \tfrac12(e_0+i\hat{\mathbf k})$ of the idempotent convention of *Conventions in the Biquaternion Universe*. The square of the un-normalised flagpole is $2\tilde\Pi$ rather than $\tilde\Pi$, which is the sense in which the flagpole is twice a state: the natural normalisation of the null direction carries the factor two that the projector removes. The set of null elements is the light cone, and the light cone is the zero-divisor cone (*The Light Cone as the Biquaternion Zero-Divisor Cone*); the flagpole is therefore a null direction that is simultaneously a projector of the informational sector, and the two readings — a lightlike vector and a pure state — are the two faces of the same eight parameters.

**Verification.** For a hundred random unit $\hat{\mathbf k}$: $N(e_0+i\hat{\mathbf k}) = 0$, the pacwoman identity holds in both orders, and $\tilde\Pi$ is idempotent and Hermitian, all to machine precision.

## The Boost of the Null Wave Element

Let $\tilde\Lambda = \cosh\frac{w}{2} + i\sinh\frac{w}{2}\hat{\mathbf u}$ be the boost rotor, so that $\tilde\Lambda$ is Hermitian ($\tilde\Lambda^{*} = \tilde\Lambda$), $\tilde\Lambda^{\natural} = \tilde\Lambda^{-1} = \cosh\frac{w}{2} - i\sinh\frac{w}{2}\hat{\mathbf u}$, and $N(\tilde\Lambda) = e_0$ (*The Lorentz Transformation as a Biquaternionic Rotation*). The pacwoman lemma turns the product of the rotor with the null element into a product of a *dilation–rotation factor* with the same null element.

**Proposition (the factorisation).** For every unit real $\hat{\mathbf u}$ and $\hat{\mathbf k}$,

$$
\tilde\Lambda\left(i + \hat{\mathbf k}\right) \;=\; \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\,\hat{\mathbf u}\hat{\mathbf k}\right)\left(i + \hat{\mathbf k}\right).
$$

**Proof.** Expand the left side,

$$
\tilde\Lambda\left(i + \hat{\mathbf k}\right)
= \cosh\frac{w}{2}\left(i + \hat{\mathbf k}\right) + i\sinh\frac{w}{2}\,\hat{\mathbf u}\left(i + \hat{\mathbf k}\right).
$$

In the second term the centrality of $i$ and the lemma in the form $i(i+\hat{\mathbf k}) = \hat{\mathbf k}(i+\hat{\mathbf k})$ give

$$
i\,\hat{\mathbf u}\left(i + \hat{\mathbf k}\right)
= \hat{\mathbf u}\, i\left(i + \hat{\mathbf k}\right)
= \hat{\mathbf u}\,\hat{\mathbf k}\left(i + \hat{\mathbf k}\right),
$$

so that the two terms carry a common factor $i+\hat{\mathbf k}$:

$$
\tilde\Lambda\left(i + \hat{\mathbf k}\right)
= \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\,\hat{\mathbf u}\hat{\mathbf k}\right)\left(i + \hat{\mathbf k}\right). 
$$

The point of the proposition is that the factor

$$
\tilde{D} \;=\; \cosh\frac{w}{2} + \sinh\frac{w}{2}\,\hat{\mathbf u}\hat{\mathbf k}
$$

contains the null element no longer: it is a real quaternion, that is an element of $\mathbb H_{\mathbb B}$, and it is the product of the dilation and the rotation. The product $\hat{\mathbf u}\hat{\mathbf k}$ of two unit real vectors is a unit real quaternion, and with the quaternion product rule $\mathbf u\mathbf k = -\mathbf u\cdot\mathbf k + \mathbf u\times\mathbf k$ it separates into its scalar and vector parts,

$$
\hat{\mathbf u}\hat{\mathbf k} \;=\; -\cos\alpha\,e_0 + \hat{\mathbf u}\times\hat{\mathbf k},
\qquad
\cos\alpha = \hat{\mathbf u}\cdot\hat{\mathbf k},
$$

so that $\tilde{D} = \left(\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha\right)e_0 + \sinh\frac{w}{2}\,\hat{\mathbf u}\times\hat{\mathbf k}$ is a scalar plus a real vector, with

$$
\tilde{D}\tilde{D}^{\natural} = \left(\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha\right)^2e_0 + \left|\sinh\frac{w}{2}\,\hat{\mathbf u}\times\hat{\mathbf k}\right|^2 e_0
= \left(\cosh w - \sinh w\cos\alpha\right)e_0 ,
$$

using $|\hat{\mathbf u}\times\hat{\mathbf k}|^2 = \sin^2\alpha$. Every real quaternion of positive norm is a positive scalar times a unit real quaternion, and $\tilde{D} = e^{d/2}\tilde{R}$ with

$$
\boxed{\; e^{d} \;=\; \cosh w - \cos\alpha\,\sinh w \;},
$$

the relativistic Doppler factor of a wave propagating at angle $\alpha$ to the boost, and $\tilde{R}$ a unit real quaternion — a rotation rotor of physical space (*Biquaternion Rotations and Lorentz Transformations*).

## The Rotation and the Dilation, Explicitly

Writing $\hat{\mathbf b}$ for the unit real vector along $\hat{\mathbf u}\times\hat{\mathbf k}$ (when the cross product does not vanish), the rotation rotor is a rotation about the axis perpendicular to the plane of $\hat{\mathbf u}$ and $\hat{\mathbf k}$,

$$
\tilde{R} \;=\; \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{\mathbf b},
\qquad
\tan\frac{\theta}{2} \;=\; \frac{\sinh\frac{w}{2}\,\sin\alpha}{\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha},
$$

with $\sin\alpha = |\hat{\mathbf u}\times\hat{\mathbf k}|$ and $\theta$ the rotation angle, taken with the sense of $\hat{\mathbf b}$. The formulas are read off from $\tilde{D} = e^{d/2}\tilde{R}$ by comparing the scalar parts and the magnitudes of the vector parts.

The rotation acts on the propagation direction by rotating it **in the plane of $\hat{\mathbf u}$ and $\hat{\mathbf k}$**, which is the algebraic form of aberration:

$$
\tilde{R}\,\hat{\mathbf k}\,\tilde{R}^{\natural} \;=\; \cos\theta\,\hat{\mathbf k} - \sin\theta\,\hat{\mathbf e},
\qquad
\hat{\mathbf e} \;=\; \frac{\hat{\mathbf u} - \cos\alpha\,\hat{\mathbf k}}{\sin\alpha},
$$

where $\hat{\mathbf e}$ is the unit vector in the plane of $\hat{\mathbf u}$ and $\hat{\mathbf k}$, perpendicular to $\hat{\mathbf k}$ and pointing from $\hat{\mathbf k}$ toward $\hat{\mathbf u}$ — the component of $\hat{\mathbf u}$ transverse to $\hat{\mathbf k}$, normalized; in particular $\hat{\mathbf u} = \cos\alpha\,\hat{\mathbf k} + \sin\alpha\,\hat{\mathbf e}$. In the transverse case $\hat{\mathbf u}\cdot\hat{\mathbf k} = 0$ this reduces to the source's $\tilde{R}\hat{\mathbf k}\tilde{R}^{\natural} = \hat{\mathbf k}\cos\theta - \hat{\mathbf u}\sin\theta$, and it is the general form above, not the transverse special case, that the rotation of a non-transverse ray requires.

The sign is the one fixed by the series' boost rotor; it records that the parameter $\hat{\mathbf u}$ of $\tilde\Lambda$ points opposite to the velocity, so that $\hat{\mathbf k}$ moves *away* from $\hat{\mathbf u}$ and hence *toward* the velocity as $\theta$ grows. Because $\tilde{R}$ commutes with $i$, it acts on the null element $\tilde{K}$ and on the field $\tilde{F}$ through the same sandwich, and since $\tilde{R}^{\natural} = \tilde{R}^{-1}$ the factor $e^{d}$ is the sole change of scale. The frequency and the field amplitude therefore scale by the same number $e^{d}$, so the intensity, quadratic in the field, scales by $e^{2d}$ — the classical content of the statement that a boost stretches the wave train while rescaling it.

**The transverse case.** When the wave propagates perpendicular to the boost, $\hat{\mathbf u}\cdot\hat{\mathbf k} = 0$, so $\cos\alpha = 0$ and the formulas simplify to the ones the source exhibits:

$$
e^{d} = \cosh w = \gamma,
\qquad
\tan\frac{\theta}{2} = \tanh\frac{w}{2},
\qquad
e^{d/2} = \frac{\cosh\frac{w}{2}}{\cos\frac{\theta}{2}} .
$$

The first is the **transverse Doppler** factor: a wave crossing the boost perpendicular to it is blueshifted by $\gamma$, with no first-order term. The second says the aberration drag of a transversely crossing ray by a boost of rapidity $w$ is the angle whose half-tangent is $\tanh\frac{w}{2}$, that is $\cos\theta = \operatorname{sech}w$, so the ray is dragged forward and its angle to the boost tends to $\pi/2$ as $w\to\infty$. In this case $\hat{\mathbf b} = \hat{\mathbf u}\times\hat{\mathbf k}$ is exactly the unit rotation axis and $\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf u}\hat{\mathbf k}$.

**Parallel propagation.** When $\hat{\mathbf u}\times\hat{\mathbf k} = 0$, the axis is undefined, $\theta = 0$ and the boost is a pure dilation: $e^{d} = \cosh w \mp \sinh w = e^{\mp w}$ for $\hat{\mathbf k} = \pm\hat{\mathbf u}$. There is no rotation, and the wave element and field are simply rescaled.

## The Field Transforms the Same Way

The field strength of a source-free plane wave is a null pure vector, and it is tied to the wave element by the annihilation condition $\tilde{K}\tilde{F} = 0$ of the plane-wave exercise. Under the boost it transforms in the bivector representation, $\tilde{F}\mapsto\tilde\Lambda^{\natural}\tilde{F}\tilde\Lambda$, not in the four-vector representation (*Exercise: Duality Rotation and the Riemann–Silberstein Vector*, Problem 5, where the four-vector candidate is shown to fail on a boost). The theorem of the section above applies to it with the same rotation and the same dilation.

**Proposition.** With $\tilde{R}$ and $e^{d}$ as above, the null field strength of the same wave satisfies

$$
\tilde\Lambda^{\natural}\,\tilde{F}\,\tilde\Lambda \;=\; e^{d}\,\tilde{R}\,\tilde{F}\,\tilde{R}^{\natural} .
$$

The verification is direct: writing the wave amplitude as $\tilde{F}_0 = i\sqrt{\epsilon_0}\,\mathbf E_0 - \sqrt{\mu_0}\,\mathbf H_0$ with $\mathbf E_0\perp\hat{\mathbf k}$ and $\mathbf H_0 = Z_0^{-1}\hat{\mathbf k}\times\mathbf E_0$, the identity holds for both polarisations of the wave and hence, the map being linear in $\tilde{F}$, for every null field of that wave. The same computation gives the field of the boosted wave in the frame in which the wave element is the one computed above.

Two consequences deserve recording. First, the electric and magnetic fields are rotated and rescaled by the same $\tilde{R}$ and $e^{d}$, so the polarisation direction, the propagation direction and the polarisation ellipse are carried by a single Euclidean similarity; this is why the boost of a plane wave can be drawn as a rotation of the wave's triad rather than as a mixing of field components. Second, because the field stays null, the boosted wave is still a radiation field and no Lorentz frame can make either field vanish — the null type of the invariant classification is preserved, as the field-strength article requires.

## Physical Reading

The identity turns the kinematics of a boosted wave into three readings of one formula:

- **Frequency.** The coefficient of $i$ in $\tilde{K}'$ is $e^{d}\omega = \left(\cosh w - \cos\alpha\sinh w\right)\omega$. This is the relativistic Doppler factor of *Exercise: The Relativistic Doppler Effect*, recovered here as the scalar factor of the dilation.
- **Direction.** The rotation $\tilde{R}$ carries $\hat{\mathbf k}$ to $\cos\theta\,\hat{\mathbf k} - \sin\theta\,\hat{\mathbf e}$ with $\hat{\mathbf e} = (\hat{\mathbf u}-\cos\alpha\,\hat{\mathbf k})/\sin\alpha$ the transverse direction of $\hat{\mathbf u}$, so that $\hat{\mathbf k}$ is dragged toward the velocity by the angle $\theta$; in the transverse case this is the elementary form $\hat{\mathbf k}\cos\theta - \hat{\mathbf u}\sin\theta$. This is aberration, recovered as the angle of the rotation.
- **Amplitude and polarisation.** The field is rotated by $\tilde{R}$ and scaled by $e^{d}$, so the Poynting vector and the energy density inherit the same similarity.

What the identity does **not** say is equally worth stating. The rotation $\tilde{R}$ is a rotation of physical space, not a Lorentz transformation of spacetime; the Lorentz character of the boost has been entirely absorbed into the dilation $e^{d}$ and the rotation $\tilde{R}$, and this is possible only because the wave is null. For a massive particle the same boost cannot be so reduced: the boost of a timelike four-velocity mixes the temporal and spatial components irreducibly, and there is no dilation and rotation of three-space that reproduces it. The reduction is thus a property of light, not of the Lorentz group.

A second caution is the medium. The identity is an identity of the vacuum algebra, where the source-free system is Lorentz covariant and the field strength transforms in the bivector representation. In a material medium the Lorentz action on the field needs the constitutive relations, and the plane-wave exercise records that the medium setting does not by itself establish the Lorentz covariance of the invariants; the wave element $\tilde{K}$ and the boost rotor are unaffected, since they are kinematic, but the field statement is a vacuum statement unless the medium is at rest in a frame in which the constitutive laws are prescribed.

## Summary

A boost of an electromagnetic plane wave is a rotation of physical space composed with a dilation, and the rotation and the dilation are the same for the wave element and for the field. The whole result rests on the **pacwoman property** of the null element, $\hat{\mathbf k}(i+\hat{\mathbf k}) = i(i+\hat{\mathbf k}) = (i+\hat{\mathbf k})\hat{\mathbf k}$, which factors the boost rotor against the null element,

$$
\tilde\Lambda\left(i+\hat{\mathbf k}\right) = \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf u}\hat{\mathbf k}\right)\left(i+\hat{\mathbf k}\right),
$$

leaving a real quaternion $\tilde{D} = \cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf u}\hat{\mathbf k}$, a scalar plus a real vector, which is $e^{d/2}\tilde{R}$ with

$$
e^{d} = \cosh w - \cos\alpha\,\sinh w,
\qquad
\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf b},
\qquad
\tan\frac{\theta}{2} = \frac{\sinh\frac{w}{2}\sin\alpha}{\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha},
$$

where $\alpha$ is the angle between $\hat{\mathbf u}$ and $\hat{\mathbf k}$ and $\hat{\mathbf b}$ the unit vector along $\hat{\mathbf u}\times\hat{\mathbf k}$. Then

$$
\tilde{K}' = \tilde\Lambda\tilde{K}\tilde\Lambda^{*} = e^{d}\tilde{R}\tilde{K}\tilde{R}^{\natural},
\qquad
\tilde{F}' = \tilde\Lambda^{\natural}\tilde{F}\tilde\Lambda = e^{d}\tilde{R}\tilde{F}\tilde{R}^{\natural} .
$$

Transversely the dilation is $\gamma$ — the transverse Doppler factor — and $\tan\frac{\theta}{2} = \tanh\frac{w}{2}$; parallel to the boost there is no rotation and the dilation is $e^{\mp w}$. The reduction is possible only because the wave is null, and the field statement is a vacuum statement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$, $e_0 = 1, e_k$ | Biquaternion algebra, quaternion basis with $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_\pm$ | Real-quaternion, Hermitian and anti-Hermitian subspaces |
| $\mathbf k = k\hat{\mathbf k} = \frac{\omega}{c}\hat{\mathbf k}$ | Wavevector, $k = \omega/c$, $\hat{\mathbf k}$ its unit direction |
| $\tilde{K} = \frac{\omega}{c}(i+\hat{\mathbf k})$ | Wave biquaternion (four-wavevector), null, $N(\tilde{K}) = 0$ |
| $\tilde{F}$ | Field-strength biquaternion, pure vector, null for a plane wave, $\tilde{K}\tilde{F}=0$ |
| $\tilde\Lambda = \cosh\frac{w}{2} + i\sinh\frac{w}{2}\hat{\mathbf u}$ | Boost rotor, Hermitian, unit norm; $w$ rapidity, $\hat{\mathbf u}$ boost direction |
| $\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf b}$ | Spatial rotation rotor, unit real quaternion |
| $\hat{\mathbf b}$ | Unit real vector along $\hat{\mathbf u}\times\hat{\mathbf k}$ |
| $e^{d}$ | Dilation factor, $= \cosh w - \cos\alpha\sinh w$ (Doppler factor) |
| $\alpha$ | Angle between $\hat{\mathbf u}$ and $\hat{\mathbf k}$, $\cos\alpha = \hat{\mathbf u}\cdot\hat{\mathbf k}$ |
| $\hat{\mathbf e} = (\hat{\mathbf u}-\cos\alpha\,\hat{\mathbf k})/\sin\alpha$ | Unit in-plane vector transverse to $\hat{\mathbf k}$, pointing toward $\hat{\mathbf u}$ |
| $\theta$ | Rotation angle, $\tan\frac{\theta}{2} = \frac{\sinh\frac{w}{2}\sin\alpha}{\cosh\frac{w}{2}-\sinh\frac{w}{2}\cos\alpha}$ |
| $c = c_0$ | Vacuum speed of light (the field statement is a vacuum statement) |

## Further Reading

- William E. Baylis, "Relativity in Introductory Physics", *Canadian Journal of Physics* **82** (2004) 853–873 (arXiv:physics/0406158), for the algebra of physical space, the pacwoman property, and the boost of a plane wave as a rotation and a dilation.
- William E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the paravector formalism in which the result is stated.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the null-element factorisation and the rotor treatment of the Lorentz group.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the complex-vector description of the free field.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Doppler effect, aberration and the transformation of the field of a plane wave.
