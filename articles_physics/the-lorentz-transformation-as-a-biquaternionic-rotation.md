# __The Lorentz Transformation as a Biquaternionic Rotation__

## Introduction

The Lorentz transformation is usually presented as a change of coordinates between inertial frames, expressed by a $4 \times 4$ real matrix $\Lambda^\mu{}_\nu$ that preserves the Minkowski metric. In the biquaternion formulation, the same transformation appears as a **rotation** — specifically, a rotation in the complexified four-dimensional space whose coordinates are the components of the biquaternion.

This article develops the biquaternionic formulation of the Lorentz transformation. The central objects are:

1. The **boost biquaternion** $\tilde{\Lambda}$, which generates the transformation.
2. The **four-velocity biquaternion** $\tilde{U}$, which describes the state of motion.
3. The **rotor conjugation** $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, which implements the transformation on four-vectors.

The article is organized as follows. First the $ict$ convention and the Euclidean form of the metric are recalled, because this is what makes the Lorentz transformation a rotation. Then the boost biquaternion is defined and its properties established. The rotor conjugation is stated and verified against the standard component formulas. The relation between the boost biquaternion and the four-velocity is derived. The group structure is identified, and the optical experiments that select this group rather than the Galilean one are recorded, with their ownership marked. Finally, the subtleties introduced by the complex nature of the rotation and by the local complex structure are discussed.

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

The group that preserves this form on $\mathbb{R}^4$ is the rotation group $SO(4)$. When the coordinates are complex — as they are when $x^0 = ict$ with $t$ real — the group becomes $SO(4, \mathbb{C})$, the group of complex rotations preserving the **general plain bilinear form**

$$
(x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2.
$$

The Lorentz group $SO(1,3)$ is the subgroup of $SO(4,\mathbb{C})$ that preserves the **real slice** $x^0 = ict$ (i.e., the slice on which $x^0$ is purely imaginary and $x^1, x^2, x^3$ are real). So:

**The Lorentz group is a real slice of the complex rotation group $SO(4, \mathbb{C})$.**

This is the precise sense in which the Lorentz transformation is a rotation: it is a rotation in the complexified four-dimensional space, restricted to the real slice on which the time coordinate is imaginary.

### The Subtlety of Working Over $\mathbb{C}$

The statement "the Lorentz transformation is a rotation" requires care, because we are working over the complex numbers. The key points:

**1. The rotation angle is imaginary.** A boost is a rotation by an **imaginary angle** in a plane that mixes the time direction with a spatial direction. To see this, consider the spatial rotation rotor in the plane $(x^0, x^1)$ by angle $\theta$: it is $\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{e}_{01}$, where $\hat{e}_{01}$ is the unit bivector for the $(x^0, x^1)$ plane. Substituting $\theta = i\psi$ (imaginary angle) gives $\cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{e}_{01}$, which is the **boost** rotor in the $(x^0, x^1)$ plane. The boost is therefore a rotation by an imaginary angle, and the parameter $\psi$ (the rapidity) is the "imaginary angle" of the rotation.

**2. The bilinear form is complex.** The quantity preserved by the rotation is the general plain bilinear form $(x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2$, which is the biquaternion norm $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$. On the real slice, this form can be negative (timelike intervals), positive (spacelike intervals), or zero (null intervals).

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
\tilde{\Lambda}^{*} = \overline{\tilde{\Lambda}^{\natural}} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}} = \tilde{\Lambda}.
$$

**3. It has unit norm.** The biquaternion norm is

$$
\tilde{\Lambda}\tilde{\Lambda}^{\natural} = \left(\cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}\right)\left(\cosh\frac{\psi}{2} - i\sinh\frac{\psi}{2}\hat{\mathbf{u}}\right) = \cosh^2\frac{\psi}{2} - \left(i\sinh\frac{\psi}{2}\right)^2\hat{\mathbf{u}}^2.
$$

Since $\hat{\mathbf{u}}^2 = -e_0$ and $(i\sinh\frac{\psi}{2})^2 = -\sinh^2\frac{\psi}{2}$, the second term is $-\left(-\sinh^2\frac{\psi}{2}\right)(-e_0) = -\sinh^2\frac{\psi}{2}e_0$. So

$$
\tilde{\Lambda}\tilde{\Lambda}^{\natural} = \left(\cosh^2\frac{\psi}{2} - \sinh^2\frac{\psi}{2}\right)e_0 = e_0.
$$

**4. It is a rotor.** In geometric algebra, a **rotor** is an even element that generates a rotation by conjugation. The boost biquaternion $\tilde{\Lambda}$ is the biquaternion form of the Lorentz rotor, and its conjugation action $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ implements the Lorentz transformation on four-vectors.

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
\tilde{Q}' = \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*}.
$$

For a pure boost, $\tilde{\Lambda}^{*} = \tilde{\Lambda}$ (Hermitian rotor), so the conjugation reduces to $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}$. For a general Lorentz transformation (boost plus spatial rotation), $\tilde{\Lambda}$ is not Hermitian and the formula $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ must be used.

The same conjugation applies to any four-vector, i.e., to any element of the anti-Hermitian subspace $\mathbb{M}_-$:

$$
\tilde{A}' = \tilde{\Lambda}\,\tilde{A}\,\tilde{\Lambda}^{*}, \qquad \tilde{U}' = \tilde{\Lambda}\,\tilde{U}\,\tilde{\Lambda}^{*}, \qquad \tilde{P}' = \tilde{\Lambda}\,\tilde{P}\,\tilde{\Lambda}^{*}, \qquad \tilde{J}' = \tilde{\Lambda}\,\tilde{J}\,\tilde{\Lambda}^{*}.
$$

### Properties of the Conjugation

**1. It preserves the subspace $\mathbb{M}_-$.** If $\tilde{A} \in \mathbb{M}_-$ and $\tilde{\Lambda}$ is a unit-norm biquaternion, then $\tilde{\Lambda}\tilde{A}\tilde{\Lambda}^{*} \in \mathbb{M}_-$.

**2. It preserves the biquaternion norm.** Since $\tilde{\Lambda}$ has unit norm, we have

$$
\tilde{A}'\tilde{A}'^{\natural} = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^{*}\,\overline{\tilde{\Lambda}\tilde{A}\tilde{\Lambda}^{*}} = \tilde{A}\tilde{A}^{\natural},
$$

so the biquaternion norm of the transformed four-vector is the same as the biquaternion norm of the original. This is the biquaternion expression of the Lorentz invariance of the Minkowski interval.

**3. It is a group action.** The composition of two rotor conjugations is another rotor conjugation: if $\tilde{\Lambda}_1$ and $\tilde{\Lambda}_2$ are two unit-norm biquaternions, then

$$
\tilde{\Lambda}_2(\tilde{\Lambda}_1\tilde{Q}\tilde{\Lambda}_1^{*})\tilde{\Lambda}_2^{*} = (\tilde{\Lambda}_2\tilde{\Lambda}_1)\tilde{Q}(\tilde{\Lambda}_2\tilde{\Lambda}_1)^{*},
$$

so the product of two rotors generates the composition of the two Lorentz transformations.

### The Action on Any Biquaternion

The rotor conjugation is written above for four-vectors, and it is worth stating that it is defined on **every** biquaternion, because that is what the field-theory articles need. Put

$$
\Phi_{\tilde{\Lambda}}(\tilde{B}) := \tilde{\Lambda}\,\tilde{B}\,\tilde{\Lambda}^{*}
\qquad\text{for any } \tilde{B} \in \mathbb{B}.
$$

Three properties follow from the fact that ${}^{*}$ is an involution and reverses products, and each was checked by direct expansion.

**It preserves both sectors.** If $\tilde{B}^{*} = \pm\tilde{B}$ then

$$
\bigl(\tilde{\Lambda}\tilde{B}\tilde{\Lambda}^{*}\bigr)^{\dagger}
= \tilde{\Lambda}\,\tilde{B}^{*}\,\tilde{\Lambda}^{*}
= \pm\,\tilde{\Lambda}\tilde{B}\tilde{\Lambda}^{*},
$$

so $\Phi_{\tilde{\Lambda}}$ maps $\mathbb{M}_-$ to itself, as the article already states for four-vectors, and equally maps $\mathbb{M}_+$ to itself. The A-field biquaternions of the electro-gravimagnetic programme therefore all transform by the same formula: the potential and the charge–current lie in $\mathbb{M}_-$, and the field strength and the power–force lie in $\mathbb{M}_+$, so each is carried to an element of its own sector by the conjugation whose component form that programme works out boost by boost. No second transformation law is needed, which is the reason the programme's transformation lemma agrees with the corpus's rotor action term for term.

**It is not an algebra automorphism.** For a product,

$$
\Phi_{\tilde{\Lambda}}(\tilde{B}\tilde{C}) = \tilde{\Lambda}\tilde{B}\tilde{C}\tilde{\Lambda}^{*},
\qquad
\Phi_{\tilde{\Lambda}}(\tilde{B})\,\Phi_{\tilde{\Lambda}}(\tilde{C}) = \tilde{\Lambda}\tilde{B}\,\tilde{\Lambda}^{*}\tilde{\Lambda}\,\tilde{C}\tilde{\Lambda}^{*},
$$

and these differ by the insertion of $\tilde{\Lambda}^{*}\tilde{\Lambda}$. They agree exactly when $\tilde{\Lambda}^{*} = \tilde{\Lambda}^{-1}$, that is, when $\tilde{\Lambda}$ is a **real** quaternion, which is the case of a pure spatial rotation. For a boost the rotor is Hermitian, $\tilde{\Lambda}^{*} = \tilde{\Lambda}$, so $\tilde{\Lambda}^{*}\tilde{\Lambda} = \tilde{\Lambda}^{2} \neq 1$ and the map is not multiplicative. The conjugation is a ${}^{*}$-conjugation, not the inner automorphism $\tilde{B}\mapsto\tilde{\Lambda}\tilde{B}\tilde{\Lambda}^{-1}$.

**It does not fix the center.** The same fact shows where the formula must not be used. On a central scalar, $\Phi_{\tilde{\Lambda}}(b\,e_0) = b\,\tilde{\Lambda}\tilde{\Lambda}^{*} = b\,\tilde{\Lambda}^2$, which is not central — for a boost it has a vector part proportional to $\hat{\mathbf{u}}$. Central elements are therefore not carried to central elements, and the conjugation is meaningful on the sectors, whose elements are the physical quantities that transform, rather than on the algebra as a whole. This is consistent with the four-vector reading: the invariant object of the conjugation is the biquaternion norm, and the norm is quadratic in a sector element, not linear in an arbitrary one.

### Verification Against Component Formulas

The rotor conjugation can be verified against the standard component formulas for a Lorentz boost. Take a four-potential $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$, and apply the rotor conjugation with $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$.

The scalar part of $\tilde{A}'$ is

$$
\mathrm{Sc}(\tilde{\Lambda}\tilde{A}\tilde{\Lambda}^{*}) = i\gamma\left(\frac{\phi}{c} - \frac{\mathbf{u}\cdot\mathbf{A}}{c}\right) = i\frac{\phi'}{c},
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

So the rotor conjugation $\tilde{A}' = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^{*}$ reproduces the standard Lorentz transformation of the four-potential.

## Relating the Boost Biquaternion to the Four-Velocity

The two biquaternions $\tilde{U}$ (four-velocity) and $\tilde{\Lambda}$ (boost) are distinct but related. Given the four-velocity

$$
\tilde{U} = \gamma\left(ic\,e_0 + \mathbf{v}\right),
$$

the associated boost biquaternion is

$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\tilde{U}^{\natural}},
$$

where the square root is the biquaternion square root (multivalued by sign) and $\tilde{U}^{\natural} = \gamma(ic\,e_0 - \mathbf{v})$ is the quaternion conjugate.

### Derivation

The derivation is a direct computation. Define the unit four-velocity $\tilde{u} = \tilde{U}/c = \gamma(i\,e_0 + \mathbf{v}/c)$, so that $\tilde{u}^{\natural} = \gamma(i\,e_0 - \mathbf{v}/c)$. Then

$$
-i\tilde{u}^{\natural} = -i\gamma(i\,e_0 - \mathbf{v}/c) = \gamma\,e_0 + i\gamma\frac{\mathbf{v}}{c}.
$$

On the other hand, the square of the boost biquaternion is

$$
\tilde{\Lambda}^2 = \exp\!\left(\psi\,i\hat{\mathbf{u}}\right) = \cosh\psi + i\sinh\psi\,\hat{\mathbf{u}} = \gamma + i\gamma\frac{\mathbf{v}}{c},
$$

where the identification $\hat{\mathbf{u}} = \hat{\mathbf{v}}$ (boost direction aligned with particle velocity) and the relations $\cosh\psi = \gamma$, $\sinh\psi = \gamma v/c$ have been used.

Comparing the two expressions,

$$
\tilde{\Lambda}^2 = -i\tilde{u}^{\natural} = -\frac{i}{c}\tilde{U}^{\natural},
$$

and hence

$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\tilde{U}^{\natural}}.
$$

### Interpretation

The formula $\tilde{\Lambda} = \sqrt{-i\tilde{U}^{\natural}/c}$ says:

- The **four-velocity** $\tilde{U}$ describes the state of motion of a particle or frame.
- The **boost biquaternion** $\tilde{\Lambda}$ is the "square root" of the (quaternion conjugate of the) unit four-velocity, up to a factor of $-i/c$.

The square root is **multivalued by sign**: both $\tilde{\Lambda}$ and $-\tilde{\Lambda}$ square to the same biquaternion. The two branches implement the **same** Lorentz transformation, since $\tilde{\Lambda}$ and $-\tilde{\Lambda}$ differ by the kernel element $-1$ of the two-to-one map $SL(2,\mathbb{C}) \to SO^+(1,3)$; the boost by $-\psi$ is a different element, the quaternion conjugate $\tilde{\Lambda}^{\natural}$. The conventional branch is selected by requiring the real scalar part of $\tilde{\Lambda}$ to be positive, i.e., $\cosh(\psi/2) > 0$.


### The Closed-Form Rotor and the Bisector Property

For a **simple** Lorentz rotation — a boost, or a rotation, or in general a transformation in a single non-null plane — the rotor can be recovered from the transformation of one vector in the plane, and the recovery has a clean closed form worth recording because it is used in the paravector computation of the boost of a wave (*Paravectors and the Geometry of Spacetime*, *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*).

Let $p$ be a non-null Hermitian element lying in the plane of the rotation, so that it commutes with the rotor, and let

$$
r \;=\; \tilde{\Lambda}\,p\,\tilde{\Lambda}^{*} \;=\; \tilde{\Lambda}^2\,p
$$

be its image, the second form using the commutation. Then

$$
\tilde{\Lambda} \;=\; \left(r\,p^{-1}\right)^{1/2},
$$

the square root being the biquaternion square root, multivalued by sign, and the two branches differing by the kernel element $-1$ of the double cover. Equivalently, since $\tilde{\Lambda}\,p$ lies along the **bisector** of $p$ and $r$,

$$
\tilde{\Lambda}\,p \;=\; \frac{p + r}{\sqrt{2\,\bigl\langle (p+r)\,p^{-1}\bigr\rangle_S}},
\qquad\text{so that}\qquad
\tilde{\Lambda} \;=\; \frac{(p+r)\,p^{-1}}{\sqrt{2\,\bigl\langle (p+r)\,p^{-1}\bigr\rangle_S}},
$$

where $\langle\,\cdot\,\rangle_S$ is the scalar part. The denominator is a positive real number because $p$ is non-null, and it normalizes the bisector to unit norm; the factor $p^{-1}$ on the right places the result in the plane.

The **bisector property** is the statement that the image $r=\tilde\Lambda^2p$ and the original $p$ are symmetrically placed about the direction of $\tilde\Lambda p$, which is the direction of $p+r$; it is why the rotor can be reconstructed from one element of the plane and its image. The closed form is the second printed form of the source (Baylis, §V.B), whose PDF extraction is ambiguous about the placement of the square-root exponent; the recomputation above selects the form displayed here, with no leading factor $p$ and the exponent $1/2$ on the whole denominator. The first form, $\tilde{\Lambda}=(rp^{-1})^{1/2}$, is unambiguous and agrees with it.


## The Group Structure

The **unit-norm biquaternions** form a group under multiplication. The general element is

$$
\tilde{Q} \in \{\tilde{Q} \in \mathbb{B} : \tilde{Q}\tilde{Q}^{\natural} = e_0\},
$$

which under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ is the group $SL(2, \mathbb{C})$, the group of $2 \times 2$ complex matrices with determinant $1$. The map from $SL(2, \mathbb{C})$ to the proper orthochronous Lorentz group $SO^+(1,3)$ is $2$-to-$1$, exactly as in the standard matrix formulation.

**Pure boosts** are the **Hermitian** elements of $SL(2,\mathbb{C})$: those satisfying $\tilde{\Lambda}^{*} = \tilde{\Lambda}$. They do **not** form a subgroup of $SL(2,\mathbb{C})$, because the product of two non-collinear boosts is generally a boost plus a spatial rotation (the Thomas–Wigner rotation), which is not Hermitian. So the set of pure boosts is a symmetric submanifold of $SL(2,\mathbb{C})$, but not a group.

**Pure spatial rotations** are the elements with **real vector part** (i.e., lying in $\mathbb{H}_{\mathbb{B}}$, the real quaternion subalgebra), satisfying $\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$ with $\hat{\mathbf{n}}^2 = -e_0$. These form the subgroup $SU(2) \subset SL(2,\mathbb{C})$.

The general Lorentz transformation is the product of a boost and a rotation, and corresponds to a general element of $SL(2,\mathbb{C})$.

## Active, Passive and Relative Transformations; the Reciprocal Basis

The word "transformation" hides three different operations, and the algebra states all three with the same rotor. It is worth fixing the three readings, because the source of the paravector literature distinguishes them and the distinction is not visible in the component formulas.

**Active.** The object is transformed and the frame is held fixed: a four-vector $\tilde{Q}$ is carried to $\tilde{Q}' = \tilde{L}\tilde{Q}\tilde{L}^{*}$, with $\tilde{L}$ the rotor of the operation. **Passive.** The frame is changed and the object is fixed: the components of the same object in the new frame are those of $\tilde{L}^{-1}\tilde{Q}\tilde{L}^{-{}^{*}}$, the inverse conjugation. **Relative.** Two frames are related by a rotor that is the ratio of their eigenspinors: if two worldlines carry eigenspinors $\tilde{\Lambda}_1$ and $\tilde{\Lambda}_2$ (in the sense of *The Eigenspinor: The Lorentz Rotor as a Function of Proper Time*), then the rotor

$$
\tilde{R}_{2\leftarrow1} = \tilde{\Lambda}_2\tilde{\Lambda}_1^{-1}
$$

carries the four-momentum of the first to the four-momentum of the second, $\tilde{P}_1\mapsto\tilde{P}_2$, and is the frame-to-frame transformation. The three readings differ by which factor of the rotor is inverted, and the physics of "which frame moves relative to which" is the choice among them. The series writes the abstract group element as $\tilde{L}$ without committing to a reading, and says which reading is meant only where a physical frame is named.

**The reciprocal basis.** The component transformation is most cleanly stated with a dual basis. On the four-dimensional space spanned by $\{e_0, e_1, e_2, e_3\}$, define the dual basis by the trace pairing $\mathrm{Sc}(\mathcal{E}^{\mu}\mathcal{E}_{\nu}) = \delta^{\mu}_{\ \nu}$. The basis and its dual are

$$
\mathcal{E}_0 = e_0,\quad \mathcal{E}_k = e_k,
\qquad
\mathcal{E}^{0} = e_0,\quad \mathcal{E}^{k} = -e_k,
$$

the minus signs coming from $e_k^2 = -e_0$: the metric is carried by the dual, not by any index-raising. Because the coefficient of $e_0$ is the imaginary $ict$, the pair $(q^0, q^k) = (ict, x_k)$ is the coordinate quadruple. Given a rotor $\tilde{L}$, the components transform as

$$
q'^{\mu} = \sum_{\nu} L^{\mu}{}_{\nu}\, q^{\nu},
\qquad
L^{\mu}{}_{\nu} = \mathrm{Sc}\!\left(\mathcal{E}^{\mu}\,\tilde{L}\,\mathcal{E}_{\nu}\,\tilde{L}^{*}\right),
$$

and the matrix $L^{\mu}{}_{\nu}$ is the ordinary Lorentz transformation matrix in the basis. The identity is algebraic and was checked numerically: for a hundred random boosts, $\mathrm{Sc}(\mathcal{E}^{\mu}\mathcal{E}_{\nu}) = \delta^{\mu}_{\ \nu}$ exactly and the component formula agrees with the direct computation of $\tilde{L}\tilde{Q}\tilde{L}^{*}$ to machine precision.

This is the sense in which the framework "raises and lowers no indices": the metric sits in the coefficients and in the dual basis, and the transformation law is a matrix multiplication without a metric tensor in sight. The reciprocal basis is the device that makes the component formula look ordinary while the geometry stays in the algebra.

## What Fixes the Transformation: The Experimental Route

Everything so far derives the transformation; nothing so far says what *selects* it. The algebra of $\mathbb{B}$ contains real and imaginary rotation angles alike, so it expresses a boost rotor with a real angle as readily as one with an imaginary angle, and the choice between them is not a choice the algebra makes. It was made by experiment. This section records the experiments and states their ownership, because a derivation that never says what fixes it invites the reader to mistake the derivation for the evidence.

**Boundary.** Nothing in this section is biquaternionic and nothing in it is a result of this corpus. The optical experiments, the contraction hypothesis and the two postulates are standard special relativity, recorded here from a single source, the *Relativité restreinte* chapter of J. Surdej, and recomputed arithmetically where a number appears. The biquaternionic formulation is a **reformulation** of the same group, so these experiments can neither confirm nor refute it: they select the group $SO^+(1,3)$, and every faithful representation of that group reproduces them. The bounds by which the reformulation could be told apart from the group belong to *The Empirical Status of the Biquaternion Framework*, not here.

### The Three Optical Experiments and Their Orders in $\beta$

Three nineteenth-century optical experiments bear on the kinematics, at different orders in the velocity ratio $\beta = v/c$.

| Experiment | Order in $\beta$ | What it measures | Result |
|---|---|---|---|
| Aberration of starlight, Bradley, 1725 | first | the apparent direction of a star as the Earth's velocity turns through the year | $20.50$ arcsec of annual shift, equal to the classical $\tan\alpha = \beta$ |
| Light drag in moving water, Fizeau, 1851 | first | the speed of light in water of velocity $u$ | the Fresnel fraction $1-1/n^2$ of $u$, which is $0.435$ at $n = 1.33$ |
| Ether drift, Michelson 1881, Michelson and Morley 1887 | second | the round-trip light time in two perpendicular arms | null, where about $0.37$ fringe was expected at $30$ km/s |

**Aberration settles nothing by itself.** The classical value $\tan\alpha = \beta$ follows from a ballistic picture of light as well as from a wave in a stationary ether. At the Earth's orbital speed $v = 29.79$ km/s one has $v/c = 9.94\times10^{-5}$, which is $20.50$ arcsec in angle, the observed annual shift; the experiment shows a relative velocity between the Earth and the incoming light, but not which kinematics governs it.

**Fizeau's drag is first order, and it is a partial drag.** An ether neither dragged nor displaced predicts no dependence on the water's motion, and a fully dragged ether predicts the whole $u$; what is measured is the fraction $1-1/n^2$ of Fresnel's formula, that is $0.435$ for $n = 1.33$. Historically this was accommodated by postulating a partial drag of the ether by the medium — an inserted property, of the same kind as the contraction below — so the experiment does not by itself refute the Galilean kinematics. Its place in the record is different: the relativistic velocity-addition formula reproduces Fresnel's fraction exactly at first order, so the experiment that motivated a drag hypothesis became a confirmation of the Lorentz kinematics.

**Michelson–Morley is second order, and it is the decisive one.** The ether wind enters as $(u/c)^2$, which is $1.0\times10^{-8}$ at $u = 30$ km/s; the expected fringe shift is this factor times the effective optical path divided by the wavelength, which for the standard effective arm of about $11$ m and $\lambda = 590$ nm is $0.37$ fringe, within the interferometer's reach. The measured shift was consistent with zero. The source's summary of the difficulty is that the result made the ether "immobile with respect to the Earth", which is geocentric and contradicts both aberration and Fizeau; what had to be abandoned was the classical interpretation itself.

### The Classical Rescue and Its Price

The first repair, proposed independently by G. FitzGerald and H. A. Lorentz in 1893, was a longitudinal contraction of moving bodies by the factor $1/\gamma$. The contraction is of order $\beta^2/2$, which at the orbital speed is $5.0\times10^{-9}$. It hides the ether wind, and its price is the corpus's recurring one: it is a **deformation inserted against the kinematics**, not derived from anything. That price is why the FitzGerald–Lorentz contraction is not the ancestor of the biquaternionic rotor.

Lorentz then arrived at the transformation that bears his name, and H. Poincaré — whom the source credits as the first to see it distinctly — stated that there is a deep antipathy between Maxwell's equations and the Galilean transformation. What was missing was Einstein's step of 1905, and it is worth recording how he described it himself, in the retrospective the source quotes:

> "The new feature of it was the realization of the fact that the bearing of the Lorentz-transformations transcended their connection with Maxwell's equations and was concerned with the nature of space and time in general. A further new result was that the 'Lorentz invariance' is a general condition for any physical theory."

That sentence is the one that matters for the corpus. The two postulates of 1905 — the speed of light in vacuum has the same value in every inertial frame whatever the motion of the source, and the laws of physics take the same form in every inertial frame — replace the inserted contraction by a kinematics, and they promote Lorentz invariance from a property of Maxwell's theory to a requirement on any theory. The biquaternionic rotor is a reformulation of the second postulate, not a competitor to it, and the corpus follows Einstein's retrospective when it treats Lorentz invariance as the general condition a candidate framework must meet.

### What the Derivation in This Article Does and Does Not Settle

The formal derivation above decides neither of the two things the experiments decide:

1. **The angle.** Nothing in the algebra forces the boost's rotation angle to be imaginary; that is what the constancy of $c$ forces, at second order, and the first-order experiments place the same constraint on the velocity-addition law.
2. **The parameterisation.** The rapidity $\psi$, with $\tanh\psi = u/c$ and the $\cosh(\psi/2)$ and $\sinh(\psi/2)$ of the boost biquaternion, is a reading of the experiments and not of the algebra.

Conversely, the experiments do not decide between the biquaternion formulation and the matrix one. They are experiments on the group, and a faithful representation cannot fail them; a reformulation must be judged by what it predicts beyond the group. That is the same point the empirical-status article makes from the other direction.

## The Complex Nature of the Rotation

We are now in a position to discuss the subtleties of working over the complex numbers.

### Real vs. Complex Rotations

The Lorentz transformation is a **real** transformation of the real coordinates $(t, x, y, z)$. But in the $ict$ convention, the time coordinate is $ict$, which is **imaginary** in the real slice. So the transformation that acts on $(ict, x, y, z)$ is a **complex** rotation, even though the original transformation on $(t, x, y, z)$ is real.

The complex nature of the rotation appears in the following places:

1. **The rotation angle is imaginary.** A boost is a rotation by an imaginary angle $i\psi$ in the plane spanned by the time direction and the boost direction. In real Euclidean geometry, a rotation by an imaginary angle is not a rotation at all — it is a **hyperbolic rotation**. The Lorentz boost is precisely this: a hyperbolic rotation in the $(ict, x)$ plane.

2. **The rotor has an imaginary vector part.** The boost biquaternion $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ has a purely imaginary vector part. In contrast, a spatial rotation rotor has a real vector part.

3. **The bilinear form is complex.** The quantity preserved by the rotation is not the real Euclidean norm (which is positive-definite), but the **general plain bilinear form** $(x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2$, which is the biquaternion norm $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$. On the real slice, this form can be negative, positive, or zero.

### The Euclidean Form Is Only Apparent

The Euclidean form $ds^2 = (x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2$ with $x^0 = ict$ appears to be a genuine Euclidean metric on $\mathbb{R}^4$. But it is not: the coordinate $x^0$ is constrained to be imaginary (since $t$ is real and $x^0 = ict$). So the "real slice" on which the Lorentz transformations act is not all of $\mathbb{R}^4$ but the subspace $\{(ict, x, y, z) : t, x, y, z \in \mathbb{R}\}$, which is a **complex subspace** of $\mathbb{C}^4$.

The Lorentz group $SO(1,3)$ acts on this slice as the subgroup of $SO(4, \mathbb{C})$ that preserves the slice. So the statement "the Lorentz transformation is a rotation in 4-dimensional Euclidean space" is correct, but the space in question is $\mathbb{C}^4$ with a general plain bilinear form, not $\mathbb{R}^4$ with a real Euclidean form.

## The Local Complex Structure

The boost biquaternion $\tilde{\Lambda}$ uses the speed of light $c$ through the rapidity $\psi$: $\tanh\psi = u/c$. In a material medium with permittivity $\epsilon$ and permeability $\mu$, the local speed of light is $c = 1/\sqrt{\epsilon\mu}$, which may differ from the vacuum speed $c_0$.

This means that the rapidity and the boost biquaternion are **local** quantities: they depend on the local electromagnetic properties of the medium. In vacuum, $c = c_0$ and the rapidity is a fixed function of the velocity. In a medium, $c$ varies from point to point, and the boost biquaternion varies accordingly.

This is consistent with the program of the companion articles on the $ict$ convention and on complexified spacetime: the complex structure is **local**, determined by the local electromagnetic properties of the medium. The boost biquaternion inherits this locality, and it becomes a **field** in the same sense as the electromagnetic field.

## Open Questions

1. **Higher-rank tensors.** The rotor conjugation $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ applies to four-vectors. How does the biquaternion formulation extend to higher-rank tensors, such as the field-strength tensor $F^{\mu\nu}$ and the energy–momentum tensor $T^{\mu\nu}$?

2. **Spinor transformations.** A spinor transforms under the Lorentz group by a **one-sided** multiplication, not by a rotor conjugation. What is the precise biquaternion form of the spinor transformation, and how does it relate to the Dirac equation?

3. **The local structure.** In a medium with varying electromagnetic properties, the boost biquaternion is a **field**. What are the consequences of treating the boost biquaternion as a field, and how does it couple to the electromagnetic field?

4. **The relation to the twistor program.** Penrose's twistor theory uses the complexified spinor space $\mathbb{C}^4$, which is closely related to the biquaternion algebra. How does the biquaternion formulation of the Lorentz transformation relate to the twistor formulation?

5. **The general transformation.** The article has focused primarily on pure boosts. What is the biquaternion form of the general Lorentz transformation (boost plus spatial rotation), and how does the non-Hermiticity of $\tilde{\Lambda}$ manifest physically?

These questions are open.

## Summary

The Lorentz transformation in biquaternionic form is a **rotation** in the complexified four-dimensional space, implemented by the **rotor conjugation**

$$
\tilde{Q}' = \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*},
$$

where $\tilde{\Lambda}$ is the **boost biquaternion**

$$
\tilde{\Lambda} = \exp\!\left(\frac{\psi}{2}\,i\hat{\mathbf{u}}\right) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}.
$$

For a pure boost, $\tilde{\Lambda} \in \mathbb{M}_+$ (Hermitian, unit norm). The rapidity $\psi$ is related to the velocity $\mathbf{u}$ by $\tanh\psi = u/c$.

The **four-velocity biquaternion** $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$, which lives in $\mathbb{M}_-$, is related to the boost biquaternion by

$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\tilde{U}^{\natural}},
$$

the square root being multivalued by sign, with the physical branch selected by $\mathrm{Sc}(\tilde{\Lambda}) > 0$.

The rotation is **complex** in the sense that the rotation angle (the rapidity) is imaginary in the $ict$ convention. The Euclidean character of the metric is only apparent: the real slice on which the Lorentz transformations act is a complex subspace of $\mathbb{C}^4$, not a real Euclidean space. The Lorentz group $SO(1,3)$ is the subgroup of the complex rotation group $SO(4,\mathbb{C})$ that preserves this slice.

The **same rotor conjugation applies to all four-vectors** in the anti-Hermitian subspace $\mathbb{M}_-$: the four-position, four-velocity, four-momentum, four-force, four-potential, and four-current. The unit-norm biquaternions form the group $SL(2,\mathbb{C})$, which is the double cover of the proper orthochronous Lorentz group $SO^+(1,3)$.

The transformation itself is fixed by experiment, not by the algebra: aberration, the Fizeau drag and the Michelson–Morley null result select the group $SO^+(1,3)$, and the biquaternion form is a faithful reformulation of that group, so it reproduces those experiments by construction rather than by prediction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (real scalar, imaginary vector) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (imaginary scalar, real vector) |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace (home of the spatial rotation rotors) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\beta = v/c$ | Velocity ratio of a frame or particle |
| $\gamma = 1/\sqrt{1-\beta^2}$ | Lorentz factor |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity biquaternion |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost biquaternion (Hermitian for pure boosts) |
| $\psi$ | Rapidity, $\tanh\psi = u/c$ |
| $\hat{\mathbf{u}}$ | Unit vector in boost direction |
| $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ | Rotor conjugation |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=N(\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation of special relativity.
- Albert Einstein, *The Meaning of Relativity* (Princeton, 1922), for the $ict$ formulation.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the spinor representation of the Lorentz group.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of the Lorentz transformation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment of Lorentz rotors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and the Lorentz group.
- V. V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a biquaternionic approach to the Lorentz group.
- L. A. Alexeyeva, "Lorentz Transformations for One Biquaternionic Model of the Electro-Gravimagnetic Field. Conservation Laws" (2009), for the induced action of the Lorentz transformation on the A-field biquaternions — potential, strength, charge–current and power–force — worked out component by component, and for the finding that the model's charge–mass conservation law is not invariant. The English text of the same work is arXiv:1104.1483v1; arXiv:0904.3446v1 is the Russian preprint.
- Jean Surdej, *La relativité restreinte*, chapter 3 of the lecture notes (2015–2016), for the experimental route recorded in *What Fixes the Transformation: The Experimental Route*: aberration of starlight, the Fizeau drag, the Michelson–Morley null result and the source's own reading of it, the FitzGerald–Lorentz contraction, Poincaré on the antipathy between Maxwell's equations and the Galilean transformation, the two postulates of 1905, and Einstein's 1955 retrospective on the bearing of the transformation.
- William E. Baylis, *Relativity in Introductory Physics*, *Canadian Journal of Physics* **82** (2004) 853–873 (arXiv:physics/0406158), §V.B, for the closed-form rotor and the bisector property recorded here, and for the paravector reading of the same transformation.

