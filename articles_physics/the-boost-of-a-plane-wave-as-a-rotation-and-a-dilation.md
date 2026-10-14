# __The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation__

## Introduction

A Lorentz boost acts on a plane wave in three apparently different ways: it shifts the frequency by the Doppler factor, it alters the propagation direction by aberration, and it rotates the polarisation. In the biquaternion algebra these are a single operation. The wave element and the field amplitude of a null wave are carried by a **spatial rotation composed with a dilation**, and the rotation and the dilation are the same for both.

The result is due to William E. Baylis (*Relativity in Introductory Physics*, Can. J. Phys. **82** (2004) 853–873, arXiv:physics/0406158), who derived it in the algebra of physical space and flagged it as the paper's new result on the boost of a wave. The present article states it in the conventions of this series and verifies it. Two objects enter: the **wave biquaternion** $\tilde{K}$, which is a null element of the material sector and whose coefficient of $i$ is the frequency, and the **field-strength biquaternion** $\tilde{F}$ of *The Field-Strength Biquaternion and Its Invariants*, which is a null pure vector. Written for a wave of direction $\hat k$, wave speed $c$ and angular frequency $\omega$,

$$
\tilde{K} = \frac{\omega}{c}\left(i + \hat k\right),
\qquad
N(\tilde{K}) = 0 ,
$$

which is the four-wavevector $\tilde{K} = \frac{i\omega}{c}e_0 + \vec k$ of the plane-wave exercise written with $\vec k = \frac{\omega}{c}\hat k$. The claim is that for a boost with rotor $\tilde U = \cosh\frac{w}{2} + i\sinh\frac{w}{2}\hat u$ (Hermitian, of unit norm, $w$ the rapidity and $\hat u$ the boost direction) there is a **unit real quaternion** $\tilde{u}$ and a positive scalar $e^{d}$ for which

$$
\boxed{\;
\tilde{K}' \;=\; \tilde U\,\tilde{K}\,\tilde U^{*} \;=\; e^{d}\,\tilde{u}\,\tilde{K}\,\tilde{u}^{\natural},
\qquad
\tilde{F}' \;=\; \tilde U^{\natural}\,\tilde{F}\,\tilde U \;=\; e^{d}\,\tilde{u}\,\tilde{F}\,\tilde{u}^{\natural} .
\;}
$$

Since $\tilde{u}$ is a real quaternion, $\tilde{u}^{\natural} = \tilde{u}^{-1}$ and the action $\tilde{u}\,\cdot\,\tilde{u}^{\natural}$ is a **rotation of physical space**; the scalar $e^{d}$ is a dilation. A boost of a wave, then, is not a mixture of three effects but a similarity of Euclidean three-space, the same one acting on the wave element and on the field.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and the scalar imaginary $i$ central with $i^2 = -1$. A **real vector** is $\vec v = v_1e_1 + v_2e_2 + v_3e_3$ with the $v_k$ real; a hat denotes a unit vector, $\hat k\hat k = -e_0$. The scalar imaginary multiplies likewise, so $i\hat k$ is imaginary-vector. The material sector $\mathbb{M}_-$ carries the four-vectors, the Hermitian sector $\mathbb{M}_+$ carries the boost rotors, and $i\mathbb{M}_+ = \mathbb{M}_-$. The field is taken in vacuum, $c = c_0$, where the source-free Maxwell system is Lorentz covariant and the field strength transforms in the bivector representation $\tilde{F}\mapsto\tilde U^{\natural}\tilde{F}\tilde U$ (*Exercise: Duality Rotation and the Riemann–Silberstein Vector*, Problem 5); the field-strength normalization cancels from the statement, which is homogeneous in $\tilde{F}$. Throughout, $\vec v$ is reserved for particle and frame velocities.

## The Null Wave Element and the Pacwoman Property

The one algebraic fact behind the result is a property of null elements that has come to be called the **pacwoman property**: a null element of the form $i+\hat k$ "gobbles" factors of $\hat k$.

**Lemma (pacwoman).** Let $\hat k$ be a unit real vector. Then

$$
\hat k\left(i + \hat k\right) \;=\; \left(i + \hat k\right)\hat k \;=\; i\left(i + \hat k\right).
$$

**Proof.** Expanding, $\hat k(i + \hat k) = i\hat k + \hat k\hat k = i\hat k - e_0$ using $\hat k\hat k = -e_0$ and the centrality of $i$; and $(i + \hat k)\hat k = i\hat k + \hat k\hat k = i\hat k - e_0$. On the other hand $i(i + \hat k) = i^2 + i\hat k = i\hat k - e_0$. The three expressions agree.

The lemma says that right-multiplication by $\hat k$ acts on the null element $i+\hat k$ exactly as multiplication by the scalar $i$ does. The name records the same statement in the form $k(1+k) = 1+k$ of the source, where $k$ is the null paravector $1+\hat k$ of the algebra of physical space; in the series basis the null paravector is the Hermitian element $e_0 + i\hat k$ and its gobbling factor is $i\hat k$:

$$
\left(i\hat k\right)\left(e_0 + i\hat k\right) \;=\; \left(e_0 + i\hat k\right)\left(i\hat k\right) \;=\; e_0 + i\hat k.
$$

**The nullity of the wave element.** The lemma is why $\tilde{K} = \frac{\omega}{c}(i+\hat k)$ has vanishing norm. Indeed $\tilde{K}^{\natural} = \frac{\omega}{c}(i-\hat k)$ and

$$
N(\tilde{K}) = \tilde{K}\tilde{K}^{\natural} = \frac{\omega^2}{c^2}\left(i+\hat k\right)\left(i-\hat k\right)
= \frac{\omega^2}{c^2}\left(i^2 - \hat k\hat k\right) = \frac{\omega^2}{c^2}\left(-1 + 1\right) = 0,
$$

because $\hat k\hat k = -e_0$. The null element is a zero divisor of $\mathbb{B}$ (*Zero Divisors of the General Plain Algebra*, *The Light Cone as the Biquaternion Zero-Divisor Cone*), and this is the algebraic form of the statement that light has no rest frame.

## The Null Flag and the Flagpole

The null element $e_0+i\hat k$ has a geometric interpretation, due to Penrose, that the pacwoman lemma makes precise. A **null flag** in Minkowski space is a lightlike direction together with a plane containing it: the direction is the **flagpole**, and the plane is the **flag**. For the wave element the flagpole is the lightlike paravector $e_0+i\hat k$ itself, and the flag is the two-plane transverse to $\hat k$; the electric field of a plane wave lies in the flag, and the magnetic field is the flag swept along the flagpole as the wave propagates. Transversality of the electromagnetic field is the statement that the amplitude has no component along the flagpole; the pacwoman identity $i\hat k(e_0+i\hat k) = e_0+i\hat k$ is the statement that the flagpole absorbs its own direction without leaving the null cone.

The flagpole is also a **pure state**. The element

$$
\tilde\Pi = \tfrac12\left(e_0 + i\hat k\right)
$$

is idempotent, $\tilde\Pi^2 = \tilde\Pi$, and Hermitian, $\tilde\Pi^{*} = \tilde\Pi$, so it is a projector; and it is exactly the rank-one projector $\tilde\Pi_1(\hat k) = \tfrac12(e_0+i\hat k)$ of the idempotent convention of *Conventions in the Biquaternion Universe*. The square of the un-normalised flagpole is $2\tilde\Pi$ rather than $\tilde\Pi$, which is the sense in which the flagpole is twice a state: the natural normalisation of the null direction carries the factor two that the projector removes. The set of null elements is the light cone, and the light cone is the zero-divisor cone (*The Light Cone as the Biquaternion Zero-Divisor Cone*); the flagpole is therefore a null direction that is simultaneously a projector of the informational sector, and the two readings — a lightlike vector and a pure state — are the two faces of the same eight parameters.


## The Boost of the Null Wave Element

Let $\tilde U = \cosh\frac{w}{2} + i\sinh\frac{w}{2}\hat u$ be the boost rotor, so that $\tilde U$ is Hermitian ($\tilde U^{*} = \tilde U$), $\tilde U^{\natural} = \tilde U^{-1} = \cosh\frac{w}{2} - i\sinh\frac{w}{2}\hat u$, and $N(\tilde U) = e_0$ (*The Lorentz Transformation as a Biquaternionic Rotation*). The pacwoman lemma turns the product of the rotor with the null element into a product of a *dilation–rotation factor* with the same null element.

**Proposition (the factorisation).** For every unit real $\hat u$ and $\hat k$,

$$
\tilde U\left(i + \hat k\right) \;=\; \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\,\hat u\hat k\right)\left(i + \hat k\right).
$$

**Proof.** Expand the left side,

$$
\tilde U\left(i + \hat k\right)
= \cosh\frac{w}{2}\left(i + \hat k\right) + i\sinh\frac{w}{2}\,\hat u\left(i + \hat k\right).
$$

In the second term the centrality of $i$ and the lemma in the form $i(i+\hat k) = \hat k(i+\hat k)$ give

$$
i\,\hat u\left(i + \hat k\right)
= \hat u\, i\left(i + \hat k\right)
= \hat u\,\hat k\left(i + \hat k\right),
$$

so that the two terms carry a common factor $i+\hat k$:

$$
\tilde U\left(i + \hat k\right)
= \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\,\hat u\hat k\right)\left(i + \hat k\right).
$$

The point of the proposition is that the factor

$$
\tilde{D} \;=\; \cosh\frac{w}{2} + \sinh\frac{w}{2}\,\hat u\hat k
$$

contains the null element no longer: it is a real quaternion, that is an element of $\mathbb H_{\mathbb B}$, and it is the product of the dilation and the rotation. The product $\hat u\hat k$ of two unit real vectors is a unit real quaternion, and with the quaternion product rule $\vec u\vec k = -\vec u\cdot\vec k + \vec u\times\vec k$ it separates into its scalar and vector parts,

$$
\hat u\hat k \;=\; -\cos\alpha\,e_0 + \hat u\times\hat k,
\qquad
\cos\alpha = \hat u\cdot\hat k,
$$

so that $\tilde{D} = \left(\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha\right)e_0 + \sinh\frac{w}{2}\,\hat u\times\hat k$ is a scalar plus a real vector, with

$$
\tilde{D}\tilde{D}^{\natural} = \left(\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha\right)^2e_0 + \left|\sinh\frac{w}{2}\,\hat u\times\hat k\right|^2 e_0
= \left(\cosh w - \sinh w\cos\alpha\right)e_0 ,
$$

using $|\hat u\times\hat k|^2 = \sin^2\alpha$. Every real quaternion of positive norm is a positive scalar times a unit real quaternion, and $\tilde{D} = e^{d/2}\tilde{u}$ with

$$
\boxed{\; e^{d} \;=\; \cosh w - \cos\alpha\,\sinh w \;},
$$

the relativistic Doppler factor of a wave propagating at angle $\alpha$ to the boost, and $\tilde{u}$ a unit real quaternion — a rotation rotor of physical space (*Biquaternion Rotations and Lorentz Transformations*).

## The Rotation and the Dilation, Explicitly

Writing $\hat b$ for the unit real vector along $\hat u\times\hat k$ (when the cross product does not vanish), the rotation rotor is a rotation about the axis perpendicular to the plane of $\hat u$ and $\hat k$,

$$
\tilde{u} \;=\; \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat b,
\qquad
\tan\frac{\theta}{2} \;=\; \frac{\sinh\frac{w}{2}\,\sin\alpha}{\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha},
$$

with $\sin\alpha = |\hat u\times\hat k|$ and $\theta$ the rotation angle, taken with the sense of $\hat b$. The formulas are read off from $\tilde{D} = e^{d/2}\tilde{u}$ by comparing the scalar parts and the magnitudes of the vector parts.

The rotation acts on the propagation direction by rotating it **in the plane of $\hat u$ and $\hat k$**, which is the algebraic form of aberration:

$$
\tilde{u}\,\hat k\,\tilde{u}^{\natural} \;=\; \cos\theta\,\hat k - \sin\theta\,\hat e,
\qquad
\hat e \;=\; \frac{\hat u - \cos\alpha\,\hat k}{\sin\alpha},
$$

where $\hat e$ is the unit vector in the plane of $\hat u$ and $\hat k$, perpendicular to $\hat k$ and pointing from $\hat k$ toward $\hat u$ — the component of $\hat u$ transverse to $\hat k$, normalized; in particular $\hat u = \cos\alpha\,\hat k + \sin\alpha\,\hat e$. In the transverse case $\hat u\cdot\hat k = 0$ this reduces to the source's $\tilde{u}\hat k\tilde{u}^{\natural} = \hat k\cos\theta - \hat u\sin\theta$, and it is the general form above, not the transverse special case, that the rotation of a non-transverse ray requires.

The sign is the one fixed by the series' boost rotor; it records that the parameter $\hat u$ of $\tilde U$ points opposite to the velocity, so that $\hat k$ moves *away* from $\hat u$ and hence *toward* the velocity as $\theta$ grows. Because $\tilde{u}$ commutes with $i$, it acts on the null element $\tilde{K}$ and on the field $\tilde{F}$ through the same sandwich, and since $\tilde{u}^{\natural} = \tilde{u}^{-1}$ the factor $e^{d}$ is the sole change of scale. The frequency and the field amplitude therefore scale by the same number $e^{d}$, so the intensity, quadratic in the field, scales by $e^{2d}$ — the classical content of the statement that a boost stretches the wave train while rescaling it.

**The transverse case.** When the wave propagates perpendicular to the boost, $\hat u\cdot\hat k = 0$, so $\cos\alpha = 0$ and the formulas simplify to the ones the source exhibits:

$$
e^{d} = \cosh w = \gamma,
\qquad
\tan\frac{\theta}{2} = \tanh\frac{w}{2},
\qquad
e^{d/2} = \frac{\cosh\frac{w}{2}}{\cos\frac{\theta}{2}} .
$$

The first is the **transverse Doppler** factor: a wave crossing the boost perpendicular to it is blueshifted by $\gamma$, with no first-order term. The second says the aberration drag of a transversely crossing ray by a boost of rapidity $w$ is the angle whose half-tangent is $\tanh\frac{w}{2}$, that is $\cos\theta = \operatorname{sech}w$, so the ray is dragged forward and its angle to the boost tends to $\pi/2$ as $w\to\infty$. In this case $\hat b = \hat u\times\hat k$ is exactly the unit rotation axis and $\tilde{u} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat u\hat k$.

**Parallel propagation.** When $\hat u\times\hat k = 0$, the axis is undefined, $\theta = 0$ and the boost is a pure dilation: $e^{d} = \cosh w \mp \sinh w = e^{\mp w}$ for $\hat k = \pm\hat u$. There is no rotation, and the wave element and field are simply rescaled.

## The Field Transforms the Same Way

The field strength of a source-free plane wave is a null pure vector, and it is tied to the wave element by the annihilation condition $\tilde{K}\tilde{F} = 0$ of the plane-wave exercise. Under the boost it transforms in the bivector representation, $\tilde{F}\mapsto\tilde U^{\natural}\tilde{F}\tilde U$, not in the four-vector representation (*Exercise: Duality Rotation and the Riemann–Silberstein Vector*, Problem 5, where the four-vector candidate is shown to fail on a boost). The theorem of the section above applies to it with the same rotation and the same dilation.

**Proposition.** With $\tilde{u}$ and $e^{d}$ as above, the null field strength of the same wave satisfies

$$
\tilde U^{\natural}\,\tilde{F}\,\tilde U \;=\; e^{d}\,\tilde{u}\,\tilde{F}\,\tilde{u}^{\natural} .
$$

The verification is direct: writing the wave amplitude as $\tilde{F}_0 = i\sqrt{\epsilon_0}\,\vec E_0 - \sqrt{\mu_0}\,\vec H_0$ with $\vec E_0\perp\hat k$ and $\vec H_0 = Z_0^{-1}\hat k\times\vec E_0$, the identity holds for both polarisations of the wave and hence, the map being linear in $\tilde{F}$, for every null field of that wave. The same computation gives the field of the boosted wave in the frame in which the wave element is the one computed above.

Two consequences deserve recording. First, the electric and magnetic fields are rotated and rescaled by the same $\tilde{u}$ and $e^{d}$, so the polarisation direction, the propagation direction and the polarisation ellipse are carried by a single Euclidean similarity; this is why the boost of a plane wave can be drawn as a rotation of the wave's triad rather than as a mixing of field components. Second, because the field stays null, the boosted wave is still a radiation field and no Lorentz frame can make either field vanish — the null type of the invariant classification is preserved, as the field-strength article requires.

## Physical Reading

The identity turns the kinematics of a boosted wave into three interpretations of one formula:

- **Frequency.** The coefficient of $i$ in $\tilde{K}'$ is $e^{d}\omega = \left(\cosh w - \cos\alpha\sinh w\right)\omega$. This is the relativistic Doppler factor of *Exercise: The Relativistic Doppler Effect*, recovered here as the scalar factor of the dilation.
- **Direction.** The rotation $\tilde{u}$ carries $\hat k$ to $\cos\theta\,\hat k - \sin\theta\,\hat e$ with $\hat e = (\hat u-\cos\alpha\,\hat k)/\sin\alpha$ the transverse direction of $\hat u$, so that $\hat k$ is dragged toward the velocity by the angle $\theta$; in the transverse case this is the elementary form $\hat k\cos\theta - \hat u\sin\theta$. This is aberration, recovered as the angle of the rotation.
- **Amplitude and polarisation.** The field is rotated by $\tilde{u}$ and scaled by $e^{d}$, so the Poynting vector and the energy density inherit the same similarity.

What the identity does **not** say is equally worth stating. The rotation $\tilde{u}$ is a rotation of physical space, not a Lorentz transformation of spacetime; the Lorentz character of the boost has been entirely absorbed into the dilation $e^{d}$ and the rotation $\tilde{u}$, and this is possible only because the wave is null. For a massive particle the same boost cannot be so reduced: the boost of a timelike four-velocity mixes the temporal and spatial components irreducibly, and there is no dilation and rotation of three-space that reproduces it. The reduction is thus a property of light, not of the Lorentz group.

A second caution is the medium. The identity is an identity of the vacuum algebra, where the source-free system is Lorentz covariant and the field strength transforms in the bivector representation. In a material medium the Lorentz action on the field needs the constitutive relations, and the plane-wave exercise records that the medium setting does not by itself establish the Lorentz covariance of the invariants; the wave element $\tilde{K}$ and the boost rotor are unaffected, since they are kinematic, but the field statement is a vacuum statement unless the medium is at rest in a frame in which the constitutive laws are prescribed.

## Summary

A boost of an electromagnetic plane wave is a rotation of physical space composed with a dilation, and the rotation and the dilation are the same for the wave element and for the field. The whole result rests on the **pacwoman property** of the null element, $\hat k(i+\hat k) = i(i+\hat k) = (i+\hat k)\hat k$, which factors the boost rotor against the null element,

$$
\tilde U\left(i+\hat k\right) = \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\hat u\hat k\right)\left(i+\hat k\right),
$$

leaving a real quaternion $\tilde{D} = \cosh\frac{w}{2} + \sinh\frac{w}{2}\hat u\hat k$, a scalar plus a real vector, which is $e^{d/2}\tilde{u}$ with

$$
e^{d} = \cosh w - \cos\alpha\,\sinh w,
\qquad
\tilde{u} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat b,
\qquad
\tan\frac{\theta}{2} = \frac{\sinh\frac{w}{2}\sin\alpha}{\cosh\frac{w}{2} - \sinh\frac{w}{2}\cos\alpha},
$$

where $\alpha$ is the angle between $\hat u$ and $\hat k$ and $\hat b$ the unit vector along $\hat u\times\hat k$. Then

$$
\tilde{K}' = \tilde U\tilde{K}\tilde U^{*} = e^{d}\tilde{u}\tilde{K}\tilde{u}^{\natural},
\qquad
\tilde{F}' = \tilde U^{\natural}\tilde{F}\tilde U = e^{d}\tilde{u}\tilde{F}\tilde{u}^{\natural} .
$$

Transversely the dilation is $\gamma$ — the transverse Doppler factor — and $\tan\frac{\theta}{2} = \tanh\frac{w}{2}$; parallel to the boost there is no rotation and the dilation is $e^{\mp w}$. The reduction is possible only because the wave is null, and the field statement is a vacuum statement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$, $e_0 = 1, e_k$ | Biquaternion algebra, quaternion basis with $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_\pm$ | Real-quaternion, Hermitian and anti-Hermitian subspaces |
| $\vec k = k\hat k = \frac{\omega}{c}\hat k$ | Wavevector, $k = \omega/c$, $\hat k$ its unit direction |
| $\tilde{K} = \frac{\omega}{c}(i+\hat k)$ | Wave biquaternion (four-wavevector), null, $N(\tilde{K}) = 0$ |
| $\tilde{F}$ | Field-strength biquaternion, pure vector, null for a plane wave, $\tilde{K}\tilde{F}=0$ |
| $\tilde U = \cosh\frac{w}{2} + i\sinh\frac{w}{2}\hat u$ | Boost rotor, Hermitian, unit norm; $w$ rapidity, $\hat u$ boost direction |
| $\tilde{u} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat b$ | Spatial rotation rotor, unit real quaternion |
| $\hat b$ | Unit real vector along $\hat u\times\hat k$ |
| $e^{d}$ | Dilation factor, $= \cosh w - \cos\alpha\sinh w$ (Doppler factor) |
| $\alpha$ | Angle between $\hat u$ and $\hat k$, $\cos\alpha = \hat u\cdot\hat k$ |
| $\hat e = (\hat u-\cos\alpha\,\hat k)/\sin\alpha$ | Unit in-plane vector transverse to $\hat k$, pointing toward $\hat u$ |
| $\theta$ | Rotation angle, $\tan\frac{\theta}{2} = \frac{\sinh\frac{w}{2}\sin\alpha}{\cosh\frac{w}{2}-\sinh\frac{w}{2}\cos\alpha}$ |
| $c = c_0$ | Vacuum speed of light (the field statement is a vacuum statement) |

## Further Reading

- William E. Baylis, "Relativity in Introductory Physics", *Canadian Journal of Physics* **82** (2004) 853–873 (arXiv:physics/0406158), for the algebra of physical space, the pacwoman property, and the boost of a plane wave as a rotation and a dilation.
- William E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the paravector formalism in which the result is stated.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the null-element factorisation and the rotor treatment of the Lorentz group.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the complex-vector description of the free field.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Doppler effect, aberration and the transformation of the field of a plane wave.
