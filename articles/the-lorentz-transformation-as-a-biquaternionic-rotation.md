
# __The Lorentz Transformation as a Biquaternionic Rotation__

## Introduction

The Lorentz transformation is usually presented as a change of coordinates between inertial frames, expressed by a $4 \times 4$ real matrix $\Lambda^\mu{}_\nu$ that preserves the Minkowski metric. In the biquaternion formulation, the same transformation appears as a **rotation** — specifically, a rotation in the complexified four-dimensional space whose coordinates are the components of the biquaternion.

This article develops the biquaternionic formulation of the Lorentz transformation. The central objects are:

1. The **boost biquaternion** $\tilde{\Lambda}$, which generates the transformation.
2. The **four-velocity biquaternion** $\tilde{U}$, which describes the state of motion.
3. The **rotor conjugation** $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, which implements the transformation on four-vectors.

The article is organized as follows. First the $ict$ convention and the Euclidean form of the metric are recalled, because this is what makes the Lorentz transformation a rotation. Then the boost biquaternion is defined and its properties established. The rotor conjugation is stated and verified against the standard component formulas. The relation between the boost biquaternion and the four-velocity is derived. Finally, the subtleties introduced by the complex nature of the rotation and by the local complex structure are discussed.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $\mathbf{u}$ (or $\mathbf{v}$) is reserved for particle and frame velocities.

## The $ict$ Convention and the Euclidean Metric

The foundation of the biquaternion formulation of the Lorentz transformation is the $ict$ convention. The Minkowski interval is written

$$
ds^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2.
$$

With the substitution $x^0 = ict$, the interval becomes

$$
ds^2 = (ic\,dt)^2 + dx^2 + dy^2 + dz^2 = (x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2.
$$

This is the **Euclidean** quadratic form in the four real variables $(x^0, x^1, x^2, x^3)$. The Lorentzian signature has been absorbed into the **complex structure** of the time coordinate.

The group that preserves this form on $\mathbb{R}^4$ is the rotation group $SO(4)$. When the coordinates are complex — as they are when $x^0 = ict$ with $t$ real — the group becomes $SO(4, \mathbb{C})$, the group of complex rotations preserving the **complex bilinear form**

$$
(x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2.
$$

The Lorentz group $SO(1,3)$ is the subgroup of $SO(4,\mathbb{C})$ that preserves the **real slice** $x^0 = ict$ (i.e., the slice on which $x^0$ is purely imaginary and $x^1, x^2, x^3$ are real). So:

**The Lorentz group is a real slice of the complex rotation group $SO(4, \mathbb{C})$.**

This is the precise sense in which the Lorentz transformation is a rotation: it is a rotation in the complexified four-dimensional space, restricted to the real slice on which the time coordinate is imaginary.

### The Subtlety of Working Over $\mathbb{C}$

The statement "the Lorentz transformation is a rotation" requires care, because we are working over the complex numbers. The key points:

**1. The rotation angle is imaginary.** A boost is a rotation by an **imaginary angle** in a plane that mixes the time direction with a spatial direction. To see this, consider the spatial rotation rotor in the plane $(x^0, x^1)$ by angle $\theta$: it is $\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{e}_{01}$, where $\hat{e}_{01}$ is the unit bivector for the $(x^0, x^1)$ plane. Substituting $\theta = i\psi$ (imaginary angle) gives $\cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{e}_{01}$, which is the **boost** rotor in the $(x^0, x^1)$ plane. The boost is therefore a rotation by an imaginary angle, and the parameter $\psi$ (the rapidity) is the "imaginary angle" of the rotation.

**2. The bilinear form is complex.** The quantity preserved by the rotation is the complex bilinear form $(x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2$, which is the biquaternion norm form $N(\tilde{X}) = \tilde{X}\bar{\tilde{X}}$. On the real slice, this form can be negative (timelike intervals), positive (spacelike intervals), or zero (null intervals).

**3. The Euclidean form is only apparent.** The Euclidean appearance of the metric $ds^2 = (x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2$ is a consequence of using the imaginary coordinate $x^0 = ict$. On the real slice, the metric is still Lorentzian, because the coordinate $x^0$ is constrained to be imaginary. The "Euclidean" character is a formal device that trades the Lorentzian signature for a complex structure.

The biquaternion algebra $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$ is the natural home of these complex rotations: it contains the rotor biquaternions that generate them, and its complex structure encodes the imaginary rotation angles.

## The Boost Biquaternion

The Lorentz boost is generated by the **boost biquaternion**

$$
\tilde{\Lambda} = \exp\!\left(\frac{\psi}{2}\,i\hat{\mathbf{u}}\right) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}},
$$

where:

- $\psi$ is the **rapidity** of the boost,
- $\hat{\mathbf{u}}$ is the unit vector in the direction of the boost,
- $i$ is the scalar imaginary,
- the exponential is taken in the biquaternion algebra.

The rapidity is related to the velocity $\mathbf{u} = u\,\hat{\mathbf{u}}$ of the boost by

$$
\cosh\psi = \gamma, \qquad \sinh\psi = \gamma\frac{u}{c}, \qquad \tanh\psi = \frac{u}{c},
$$

where

$$
\gamma = \frac{1}{\sqrt{1 - u^2/c^2}}
$$

is the Lorentz factor.

### Properties of the Boost Biquaternion

The boost biquaternion $\tilde{\Lambda}$ has the following properties.

**1. It lies in the Hermitian subspace $\mathbb{M}_+$.** The scalar part $\cosh(\psi/2)$ is **real**, and the vector part $i\sinh(\psi/2)\hat{\mathbf{u}}$ is **purely imaginary**. So $\tilde{\Lambda} \in \mathbb{M}_+$.

**2. It is Hermitian.** Since $\tilde{\Lambda} \in \mathbb{M}_+$, its Hermitian conjugate is

$$
\tilde{\Lambda}^\dagger = \bar{\tilde{\Lambda}}^* = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}} = \tilde{\Lambda}.
$$

**3. It has unit norm.** The norm form is

$$
\tilde{\Lambda}\bar{\tilde{\Lambda}} = \left(\cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}\right)\left(\cosh\frac{\psi}{2} - i\sinh\frac{\psi}{2}\hat{\mathbf{u}}\right) = \cosh^2\frac{\psi}{2} - \left(i\sinh\frac{\psi}{2}\right)^2\hat{\mathbf{u}}^2.
$$

Since $\hat{\mathbf{u}}^2 = -e_0$ and $(i\sinh\frac{\psi}{2})^2 = -\sinh^2\frac{\psi}{2}$, the second term is $-\left(-\sinh^2\frac{\psi}{2}\right)(-e_0) = -\sinh^2\frac{\psi}{2}e_0$. So

$$
\tilde{\Lambda}\bar{\tilde{\Lambda}} = \left(\cosh^2\frac{\psi}{2} - \sinh^2\frac{\psi}{2}\right)e_0 = e_0.
$$

**4. It is a rotor.** In geometric algebra, a **rotor** is an even element that generates a rotation by conjugation. The boost biquaternion $\tilde{\Lambda}$ is the biquaternion form of the Lorentz rotor, and its conjugation action $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ implements the Lorentz transformation on four-vectors.

### Why the Imaginary Unit Appears

The key feature of the boost biquaternion is that the vector part is **purely imaginary** — it is $i\sinh(\psi/2)\hat{\mathbf{u}}$, not $\sinh(\psi/2)\hat{\mathbf{u}}$. The imaginary unit $i$ is what makes the transformation a **boost** rather than a **spatial rotation**.

Compare:

- **Spatial rotation** about an axis $\hat{\mathbf{n}}$ by angle $\theta$: the rotor is $\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$, with a **real** vector part.
- **Boost** along a direction $\hat{\mathbf{u}}$ with rapidity $\psi$: the rotor is $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, with a **purely imaginary** vector part.

Both are rotors in the sense of geometric algebra, both satisfy the unit-norm condition, and both act by conjugation. The difference is the **sign** of the vector part squared:

- In the spatial case, $\hat{\mathbf{n}}^2 = -e_0$ (spacelike bivector).
- In the boost case, $(i\hat{\mathbf{u}})^2 = +e_0$ (timelike bivector).

This sign difference is the algebraic distinction between a rotation in a spacelike plane and a rotation in a timelike plane. In the biquaternion formulation, the imaginary unit $i$ is the marker that converts a spacelike rotation into a timelike one.

## The Rotor Conjugation

The Lorentz transformation acts on four-vectors by **rotor conjugation**:

$$
\tilde{X}' = \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger.
$$

For a pure boost, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$ (Hermitian rotor), so the conjugation reduces to $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}$. For a general Lorentz transformation (boost plus spatial rotation), $\tilde{\Lambda}$ is not Hermitian and the formula $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ must be used.

The same conjugation applies to any four-vector, i.e., to any element of the anti-Hermitian subspace $\mathbb{M}_-$:

$$
\tilde{A}' = \tilde{\Lambda}\,\tilde{A}\,\tilde{\Lambda}^\dagger, \qquad \tilde{U}' = \tilde{\Lambda}\,\tilde{U}\,\tilde{\Lambda}^\dagger, \qquad \tilde{P}' = \tilde{\Lambda}\,\tilde{P}\,\tilde{\Lambda}^\dagger, \qquad \tilde{J}' = \tilde{\Lambda}\,\tilde{J}\,\tilde{\Lambda}^\dagger.
$$

### Properties of the Conjugation

**1. It preserves the subspace $\mathbb{M}_-$.** If $\tilde{A} \in \mathbb{M}_-$ and $\tilde{\Lambda}$ is a unit-norm biquaternion, then $\tilde{\Lambda}\tilde{A}\tilde{\Lambda}^\dagger \in \mathbb{M}_-$.

**2. It preserves the norm form.** Since $\tilde{\Lambda}$ has unit norm, we have

$$
\tilde{A}'\bar{\tilde{A}'} = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^\dagger\,\overline{\tilde{\Lambda}\tilde{A}\tilde{\Lambda}^\dagger} = \tilde{A}\bar{\tilde{A}},
$$

so the norm form of the transformed four-vector is the same as the norm form of the original. This is the biquaternion expression of the Lorentz invariance of the Minkowski interval.

**3. It is a group action.** The composition of two rotor conjugations is another rotor conjugation: if $\tilde{\Lambda}_1$ and $\tilde{\Lambda}_2$ are two unit-norm biquaternions, then

$$
\tilde{\Lambda}_2(\tilde{\Lambda}_1\tilde{X}\tilde{\Lambda}_1^\dagger)\tilde{\Lambda}_2^\dagger = (\tilde{\Lambda}_2\tilde{\Lambda}_1)\tilde{X}(\tilde{\Lambda}_2\tilde{\Lambda}_1)^\dagger,
$$

so the product of two rotors generates the composition of the two Lorentz transformations.

### Verification Against Component Formulas

The rotor conjugation can be verified against the standard component formulas for a Lorentz boost. Take a four-potential $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$, and apply the rotor conjugation with $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$.

The scalar part of $\tilde{A}'$ is

$$
\mathrm{Sc}(\tilde{\Lambda}\tilde{A}\tilde{\Lambda}^\dagger) = i\gamma\left(\frac{\phi}{c} - \frac{\mathbf{u}\cdot\mathbf{A}}{c}\right) = i\frac{\phi'}{c},
$$

where the standard relations $\cosh\psi = \gamma$ and $\sinh\psi = \gamma u/c$ have been used. This gives

$$
\phi' = \gamma(\phi - \mathbf{u}\cdot\mathbf{A}),
$$

which is the standard Lorentz transformation of the scalar potential (in units where $\mathbf{A}$ is measured in the same units as $\phi$ divided by velocity, i.e., the SI convention).

The vector part gives

$$
\mathbf{A}' = \mathbf{A} + \frac{\gamma - 1}{u^2}(\mathbf{u}\cdot\mathbf{A})\mathbf{u} - \gamma\frac{\phi}{c^2}\mathbf{u},
$$

which is the standard Lorentz transformation of the vector potential, including the longitudinal projection term and the contribution from the scalar potential.

So the rotor conjugation $\tilde{A}' = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^\dagger$ reproduces the standard Lorentz transformation of the four-potential.

## Relating the Boost Biquaternion to the Four-Velocity

The two biquaternions $\tilde{U}$ (four-velocity) and $\tilde{\Lambda}$ (boost) are distinct but related. Given the four-velocity

$$
\tilde{U} = \gamma\left(ic\,e_0 + \mathbf{v}\right),
$$

the associated boost biquaternion is

$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\bar{\tilde{U}}},
$$

where the square root is the biquaternion square root (multivalued by sign) and $\bar{\tilde{U}} = \gamma(ic\,e_0 - \mathbf{v})$ is the quaternion conjugate.

### Derivation

The derivation is a direct computation. Define the unit four-velocity $\tilde{u} = \tilde{U}/c = \gamma(i\,e_0 + \mathbf{v}/c)$, so that $\bar{\tilde{u}} = \gamma(i\,e_0 - \mathbf{v}/c)$. Then

$$
-i\bar{\tilde{u}} = -i\gamma(i\,e_0 - \mathbf{v}/c) = \gamma\,e_0 + i\gamma\frac{\mathbf{v}}{c}.
$$

On the other hand, the square of the boost biquaternion is

$$
\tilde{\Lambda}^2 = \exp\!\left(\psi\,i\hat{\mathbf{u}}\right) = \cosh\psi + i\sinh\psi\,\hat{\mathbf{u}} = \gamma + i\gamma\frac{\mathbf{v}}{c},
$$

where the identification $\hat{\mathbf{u}} = \hat{\mathbf{v}}$ (boost direction aligned with particle velocity) and the relations $\cosh\psi = \gamma$, $\sinh\psi = \gamma v/c$ have been used.

Comparing the two expressions,

$$
\tilde{\Lambda}^2 = -i\bar{\tilde{u}} = -\frac{i}{c}\bar{\tilde{U}},
$$

and hence

$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\bar{\tilde{U}}}.
$$

### Interpretation

The formula $\tilde{\Lambda} = \sqrt{-i\bar{\tilde{U}}/c}$ says:

- The **four-velocity** $\tilde{U}$ describes the state of motion of a particle or frame.
- The **boost biquaternion** $\tilde{\Lambda}$ is the "square root" of the (quaternion conjugate of the) unit four-velocity, up to a factor of $-i/c$.

The square root is **multivalued by sign**: both $\tilde{\Lambda}$ and $-\tilde{\Lambda}$ square to the same biquaternion. The two branches implement the **same** Lorentz transformation, since $\tilde{\Lambda}$ and $-\tilde{\Lambda}$ differ by the kernel element $-1$ of the two-to-one map $SL(2,\mathbb{C}) \to SO^+(1,3)$; the boost by $-\psi$ is a different element, the quaternion conjugate $\bar{\tilde{\Lambda}}$. The conventional branch is selected by requiring the real scalar part of $\tilde{\Lambda}$ to be positive, i.e., $\cosh(\psi/2) > 0$.

## The Group Structure

The **unit-norm biquaternions** form a group under multiplication. The general element is

$$
\tilde{Q} \in \{\tilde{Q} \in \mathbb{B} : \tilde{Q}\bar{\tilde{Q}} = e_0\},
$$

which under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ is the group $SL(2, \mathbb{C})$, the group of $2 \times 2$ complex matrices with determinant $1$. The map from $SL(2, \mathbb{C})$ to the proper orthochronous Lorentz group $SO^+(1,3)$ is $2$-to-$1$, exactly as in the standard matrix formulation.

**Pure boosts** are the **Hermitian** elements of $SL(2,\mathbb{C})$: those satisfying $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$. They do **not** form a subgroup of $SL(2,\mathbb{C})$, because the product of two non-collinear boosts is generally a boost plus a spatial rotation (the Thomas–Wigner rotation), which is not Hermitian. So the set of pure boosts is a symmetric submanifold of $SL(2,\mathbb{C})$, but not a group.

**Pure spatial rotations** are the elements with **real vector part** (i.e., lying in $\mathbb{H}_{\mathbb{B}}$, the real quaternion subalgebra), satisfying $\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$ with $\hat{\mathbf{n}}^2 = -e_0$. These form the subgroup $SU(2) \subset SL(2,\mathbb{C})$.

The general Lorentz transformation is the product of a boost and a rotation, and corresponds to a general element of $SL(2,\mathbb{C})$.

## The Complex Nature of the Rotation

We are now in a position to discuss the subtleties of working over the complex numbers.

### Real vs. Complex Rotations

The Lorentz transformation is a **real** transformation of the real coordinates $(t, x, y, z)$. But in the $ict$ convention, the time coordinate is $ict$, which is **imaginary** in the real slice. So the transformation that acts on $(ict, x, y, z)$ is a **complex** rotation, even though the original transformation on $(t, x, y, z)$ is real.

The complex nature of the rotation appears in the following places:

1. **The rotation angle is imaginary.** A boost is a rotation by an imaginary angle $i\psi$ in the plane spanned by the time direction and the boost direction. In real Euclidean geometry, a rotation by an imaginary angle is not a rotation at all — it is a **hyperbolic rotation**. The Lorentz boost is precisely this: a hyperbolic rotation in the $(ict, x)$ plane.

2. **The rotor has an imaginary vector part.** The boost biquaternion $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ has a purely imaginary vector part. In contrast, a spatial rotation rotor has a real vector part.

3. **The bilinear form is complex.** The quantity preserved by the rotation is not the real Euclidean norm (which is positive-definite), but the **complex bilinear form** $(x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2$, which is the biquaternion norm form $N(\tilde{X}) = \tilde{X}\bar{\tilde{X}}$. On the real slice, this form can be negative, positive, or zero.

### The Euclidean Form Is Only Apparent

The Euclidean form $ds^2 = (x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2$ with $x^0 = ict$ appears to be a genuine Euclidean metric on $\mathbb{R}^4$. But it is not: the coordinate $x^0$ is constrained to be imaginary (since $t$ is real and $x^0 = ict$). So the "real slice" on which the Lorentz transformations act is not all of $\mathbb{R}^4$ but the subspace $\{(ict, x, y, z) : t, x, y, z \in \mathbb{R}\}$, which is a **complex subspace** of $\mathbb{C}^4$.

The Lorentz group $SO(1,3)$ acts on this slice as the subgroup of $SO(4, \mathbb{C})$ that preserves the slice. So the statement "the Lorentz transformation is a rotation in 4-dimensional Euclidean space" is correct, but the space in question is $\mathbb{C}^4$ with a complex bilinear form, not $\mathbb{R}^4$ with a real Euclidean form.

## The Local Complex Structure

The boost biquaternion $\tilde{\Lambda}$ uses the speed of light $c$ through the rapidity $\psi$: $\tanh\psi = u/c$. In a material medium with permittivity $\epsilon$ and permeability $\mu$, the local speed of light is $c = 1/\sqrt{\epsilon\mu}$, which may differ from the vacuum speed $c_0$.

This means that the rapidity and the boost biquaternion are **local** quantities: they depend on the local electromagnetic properties of the medium. In vacuum, $c = c_0$ and the rapidity is a fixed function of the velocity. In a medium, $c$ varies from point to point, and the boost biquaternion varies accordingly.

This is consistent with the program of the companion articles on the $ict$ convention and on complexified spacetime: the complex structure is **local**, determined by the local electromagnetic properties of the medium. The boost biquaternion inherits this locality, and it becomes a **field** in the same sense as the electromagnetic field.

## Summary

The Lorentz transformation in biquaternionic form is a **rotation** in the complexified four-dimensional space, implemented by the **rotor conjugation**

$$
\tilde{X}' = \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger,
$$

where $\tilde{\Lambda}$ is the **boost biquaternion**

$$
\tilde{\Lambda} = \exp\!\left(\frac{\psi}{2}\,i\hat{\mathbf{u}}\right) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}.
$$

For a pure boost, $\tilde{\Lambda} \in \mathbb{M}_+$ (Hermitian, unit norm). The rapidity $\psi$ is related to the velocity $\mathbf{u}$ by $\tanh\psi = u/c$.

The **four-velocity biquaternion** $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$, which lives in $\mathbb{M}_-$, is related to the boost biquaternion by

$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\bar{\tilde{U}}},
$$

the square root being multivalued by sign, with the physical branch selected by $\mathrm{Sc}(\tilde{\Lambda}) > 0$.

The rotation is **complex** in the sense that the rotation angle (the rapidity) is imaginary in the $ict$ convention. The Euclidean character of the metric is only apparent: the real slice on which the Lorentz transformations act is a complex subspace of $\mathbb{C}^4$, not a real Euclidean space. The Lorentz group $SO(1,3)$ is the subgroup of the complex rotation group $SO(4,\mathbb{C})$ that preserves this slice.

The **same rotor conjugation applies to all four-vectors** in the anti-Hermitian subspace $\mathbb{M}_-$: the four-position, four-velocity, four-momentum, four-force, four-potential, and four-current. The unit-norm biquaternions form the group $SL(2,\mathbb{C})$, which is the double cover of the proper orthochronous Lorentz group $SO^+(1,3)$.

## Open Questions

1. **Higher-rank tensors.** The rotor conjugation $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ applies to four-vectors. How does the biquaternion formulation extend to higher-rank tensors, such as the field-strength tensor $F^{\mu\nu}$ and the energy–momentum tensor $T^{\mu\nu}$?

2. **Spinor transformations.** A spinor transforms under the Lorentz group by a **one-sided** multiplication, not by a rotor conjugation. What is the precise biquaternion form of the spinor transformation, and how does it relate to the Dirac equation?

3. **The local structure.** In a medium with varying electromagnetic properties, the boost biquaternion is a **field**. What are the consequences of treating the boost biquaternion as a field, and how does it couple to the electromagnetic field?

4. **The relation to the twistor program.** Penrose's twistor theory uses the complexified spinor space $\mathbb{C}^4$, which is closely related to the biquaternion algebra. How does the biquaternion formulation of the Lorentz transformation relate to the twistor formulation?

5. **The general transformation.** The article has focused primarily on pure boosts. What is the biquaternion form of the general Lorentz transformation (boost plus spatial rotation), and how does the non-Hermiticity of $\tilde{\Lambda}$ manifest physically?

These questions are open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (real scalar, imaginary vector) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (imaginary scalar, real vector) |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace (home of the spatial rotation rotors) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity biquaternion |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost biquaternion (Hermitian for pure boosts) |
| $\psi$ | Rapidity, $\tanh\psi = u/c$ |
| $\hat{\mathbf{u}}$ | Unit vector in boost direction |
| $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation of special relativity.
- Albert Einstein, *The Meaning of Relativity* (Princeton, 1922), for the $ict$ formulation.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the spinor representation of the Lorentz group.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of the Lorentz transformation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment of Lorentz rotors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and the Lorentz group.
- V. V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a biquaternionic approach to the Lorentz group.

