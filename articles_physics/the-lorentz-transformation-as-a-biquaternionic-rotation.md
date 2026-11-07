# __The Lorentz Transformation as a Biquaternionic Rotation__

## Introduction

The Lorentz transformation is usually presented as a change of coordinates between inertial frames, expressed by a $4 \times 4$ real matrix $\Lambda_{\mu\nu}$, with $\mu$ the row and $\nu$ the column, that preserves the Minkowski metric. In the biquaternion formulation, the same transformation appears as a **rotation** — specifically, a rotation in the complexified four-dimensional space whose coordinates are the components of the biquaternion.

This article develops the biquaternionic formulation of the Lorentz transformation. The central objects are:

1. The **boost biquaternion** $\tilde U_{\Psi,\mathrm b}$, the Lorentz rotor that generates the transformation.
2. The **four-velocity biquaternion** $\tilde{V}_{\Phi}$, which describes the state of motion.
3. The **rotor conjugation** $\tilde{Q}_2 = \tilde U_{\Psi,\mathrm b}\tilde{Q}\tilde U_{\Psi,\mathrm b}^{*}$, which implements the transformation on four-vectors.

The article is organized as follows. First the $i r'_t$ convention and the Euclidean form of the metric are recalled, because this is what makes the Lorentz transformation a rotation. Then the boost biquaternion is defined and its properties established. The rotor conjugation is stated and verified against the standard component formulas. The relation between the boost biquaternion and the four-velocity is derived. The group structure is identified, and the optical experiments that select this group rather than the Galilean one are recorded, with their ownership marked. Finally, the subtleties introduced by the complex nature of the rotation and by the local complex structure are discussed.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial R_t + \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $\vec v_b$ (or $\vec v$) is reserved for particle and frame velocities. A pure boost is written $\tilde U_{\Psi,\mathrm b}$, the rotation factor $\tilde u_{\mathrm r}$, and the general rotor $\tilde U_{\mathrm{lor}}=\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$; the boost formulas below are the case $\tilde u_{\mathrm r}=e_t$, and a general transformation is recovered by multiplying the boost on the right by the rotation.

## The $i r'_t$ Convention and the Euclidean Metric

The foundation of the biquaternion formulation of the Lorentz transformation is the $i r'_t$ convention. The Minkowski interval is written

$$
ds^2 = -d{r'_{t}}^2 + dr_x^2+dr_y^2+dr_z^2.
$$

With the substitution $x_0= i r'_t$, the interval becomes

$$
ds^2 = (i\,dr'_t)^2 + dr_x^2+dr_y^2+dr_z^2 = (x_0)^2 + (x_1)^2 + (x_2)^2 + (x_3)^2.
$$

This is the **Euclidean** quadratic form in the four real variables $(x_0, x_1, x_2, x_3)$. The Lorentzian signature has been absorbed into the **complex structure** of the time coordinate.

The group that preserves this form on $\mathbb{R}^4$ is the rotation group $SO(4)$. When the coordinates are complex — as they are when $x_0= i r'_t$ with $r'_t$ real — the group becomes $SO(4, \mathbb{C})$, the group of complex rotations preserving the **general plain bilinear form**

$$
(x_0)^2 + (x_1)^2 + (x_2)^2 + (x_3)^2.
$$

The Lorentz group $SO(1,3)$ is the subgroup of $SO(4,\mathbb{C})$ that preserves the **real slice** $x_0= i r'_t$ (i.e., the slice on which $x_0$ is purely imaginary and $x_1, x_2, x_3$ are real). So:

**The Lorentz group is a real slice of the complex rotation group $SO(4, \mathbb{C})$.**

This is the precise sense in which the Lorentz transformation is a rotation: it is a rotation in the complexified four-dimensional space, restricted to the real slice on which the time coordinate is imaginary.

### The Subtlety of Working Over $\mathbb{C}$

The statement "the Lorentz transformation is a rotation" requires care, because we are working over the complex numbers. The key points:

**1. The rotation angle is imaginary.** A boost is a rotation by an **imaginary angle** in a plane that mixes the time direction with a spatial direction. To see this, consider the spatial rotation rotor in the plane $(x_0, x_1)$ by angle $\theta$: it is $\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\vec u_{01}$, where $\vec u_{01}$ is the unit bivector for the $(x_0, x_1)$ plane. Substituting $\theta = i\theta_{\mathrm{rpd}}$ (imaginary angle) gives $\cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{01}$, which is the **boost** rotor in the $(x_0, x_1)$ plane. The boost is therefore a rotation by an imaginary angle, and the parameter $\theta_{\mathrm{rpd}}$ (the rapidity) is the "imaginary angle" of the rotation.

**2. The bilinear form is complex.** The quantity preserved by the rotation is the general plain bilinear form $(x_0)^2 + (x_1)^2 + (x_2)^2 + (x_3)^2$, which is the biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$. On the real slice, this form can be negative (timelike intervals), positive (spacelike intervals), or zero (null intervals).

**3. The Euclidean form is only apparent.** The Euclidean appearance of the metric $ds^2 = (x_0)^2 + (x_1)^2 + (x_2)^2 + (x_3)^2$ is a consequence of using the imaginary coordinate $x_0= i r'_t$. On the real slice, the metric is still Lorentzian, because the coordinate $x_0$ is constrained to be imaginary. The "Euclidean" character is a formal device that trades the Lorentzian signature for a complex structure.

The biquaternion algebra $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$ is the natural home of these complex rotations: it contains the rotor biquaternions that generate them, and its complex structure encodes the imaginary rotation angles.

## The Boost Biquaternion

The Lorentz boost is generated by the **boost biquaternion**

$$
\boxed{\;\tilde U_{\Psi,\mathrm b} = \exp\!\left(\frac{\theta_{\mathrm{rpd}}}{2}\,i\vec u_{\mathrm b}\right) = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b}\;}
$$

where:

- $\theta_{\mathrm{rpd}}$ is the **rapidity** of the boost,
- $\vec u_{\mathrm b}$ is the unit vector in the direction of the boost,
- $i$ is the scalar imaginary,
- the exponential is taken in the biquaternion algebra.

The rapidity is related to the velocity $\vec v_b = v_b\,\vec u_{\mathrm b}$ of the boost by

$$
\cosh\theta_{\mathrm{rpd}} = \gamma, \qquad \sinh\theta_{\mathrm{rpd}} = \gamma\frac{v_b}{c}, \qquad \tanh\theta_{\mathrm{rpd}} = \frac{v_b}{c},
$$

where

$$
\gamma = \frac{1}{\sqrt{1 - v_b^2/c^2}}
$$

is the Lorentz factor.

### Properties of the Boost Biquaternion

The boost biquaternion $\tilde U_{\Psi,\mathrm b}$ has the following properties.

**1. It lies in the Hermitian subspace $\mathbb{B}_{\Psi}$.** The scalar part $\cosh(\theta_{\mathrm{rpd}}/2)$ is **real**, and the vector part $i\sinh(\theta_{\mathrm{rpd}}/2)\vec u_{\mathrm b}$ is **purely imaginary**. So $\tilde U_{\Psi,\mathrm b} \in \mathbb{B}_{\Psi}$.

**2. It is Hermitian.** Since $\tilde U_{\Psi,\mathrm b} \in \mathbb{B}_{\Psi}$, its Hermitian conjugate is

$$
\tilde U_{\Psi,\mathrm b}^{*} = \overline{\tilde U_{\Psi,\mathrm b}^{\natural}} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b} = \tilde U_{\Psi,\mathrm b}.
$$

**3. It has unit norm.** The biquaternion norm is

$$
\tilde U_{\Psi,\mathrm b}\tilde U_{\Psi,\mathrm b}^{\natural} = \left(\cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\right)\left(\cosh\frac{\theta_{\mathrm{rpd}}}{2} - i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\right) = \cosh^2\frac{\theta_{\mathrm{rpd}}}{2} - \left(i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\right)^2\vec u_{\mathrm b}^2.
$$

Since $\vec u_{\mathrm b}^2 = -e_t$ and $(i\sinh\frac{\theta_{\mathrm{rpd}}}{2})^2 = -\sinh^2\frac{\theta_{\mathrm{rpd}}}{2}$, the second term is $-\left(-\sinh^2\frac{\theta_{\mathrm{rpd}}}{2}\right)(-e_t) = -\sinh^2\frac{\theta_{\mathrm{rpd}}}{2}e_t$. So

$$
\tilde U_{\Psi,\mathrm b}\tilde U_{\Psi,\mathrm b}^{\natural} = \left(\cosh^2\frac{\theta_{\mathrm{rpd}}}{2} - \sinh^2\frac{\theta_{\mathrm{rpd}}}{2}\right)e_t = e_t.
$$

**4. It is a rotor.** In geometric algebra, a **rotor** is an even element that generates a rotation by conjugation. The boost biquaternion $\tilde U_{\Psi,\mathrm b}$ is the biquaternion form of the Lorentz rotor, and its conjugation action $\tilde{Q} \mapsto \tilde U_{\Psi,\mathrm b}\tilde{Q}\tilde U_{\Psi,\mathrm b}^{*}$ implements the Lorentz transformation on four-vectors.

### Why the Imaginary Unit Appears

The key feature of the boost biquaternion is that the vector part is **purely imaginary** — it is $i\sinh(\theta_{\mathrm{rpd}}/2)\vec u_{\mathrm b}$, not $\sinh(\theta_{\mathrm{rpd}}/2)\vec u_{\mathrm b}$. The imaginary unit $i$ is what makes the transformation a **boost** rather than a **spatial rotation**.

Compare:

- **Spatial rotation** about an axis $\vec u_{\mathrm r}$ by angle $\theta$: the rotor is $\tilde u_{\mathrm r} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\vec u_{\mathrm r}$, with a **real** vector part.
- **Boost** along a direction $\vec u_{\mathrm b}$ with rapidity $\theta_{\mathrm{rpd}}$: the rotor is $\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$, with a **purely imaginary** vector part.

Both are rotors in the sense of geometric algebra, both satisfy the unit-norm condition, and both act by conjugation. The difference is the **sign** of the vector part squared:

- In the spatial case, $\vec u_{\mathrm r}^2 = -e_t$ (spacelike bivector).
- In the boost case, $(i\vec u_{\mathrm b})^2 = +e_t$ (timelike bivector).

This sign difference is the algebraic distinction between a rotation in a spacelike plane and a rotation in a timelike plane. In the biquaternion formulation, the imaginary unit $i$ is the marker that converts a spacelike rotation into a timelike one.

## The Rotor Conjugation

The Lorentz transformation acts on four-vectors by **rotor conjugation**:

$$
\boxed{\;\tilde{Q}_2 = \tilde U_{\Psi,\mathrm b}\,\tilde{Q}\,\tilde U_{\Psi,\mathrm b}^{*}\;}
$$

For a pure boost, $\tilde U_{\Psi,\mathrm b}^{*} = \tilde U_{\Psi,\mathrm b}$ (Hermitian rotor), so the conjugation reduces to $\tilde{Q}_2 = \tilde U_{\Psi,\mathrm b}\tilde{Q}\tilde U_{\Psi,\mathrm b}$. For a general Lorentz transformation (boost plus spatial rotation), $\tilde U_{\mathrm{lor}}=\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ is not Hermitian and the formula $\tilde{Q}_2 = \tilde U_{\mathrm{lor}}\tilde{Q}\tilde U_{\mathrm{lor}}{}^{*}$ must be used.

The same conjugation applies to any four-vector, i.e., to any element of the anti-Hermitian subspace $\mathbb{B}_{\Phi}$:

$$
\tilde{A}_{\Phi,2} = \tilde U_{\Psi,\mathrm b}\,\tilde{A}_{\Phi}\,\tilde U_{\Psi,\mathrm b}^{*}, \qquad \tilde{V}_{\Phi,2} = \tilde U_{\Psi,\mathrm b}\,\tilde{V}_{\Phi}\,\tilde U_{\Psi,\mathrm b}^{*}, \qquad \tilde{P}_{\Phi,2} = \tilde U_{\Psi,\mathrm b}\,\tilde{P}_{\Phi}\,\tilde U_{\Psi,\mathrm b}^{*}, \qquad \tilde{J}_{\Phi,2} = \tilde U_{\Psi,\mathrm b}\,\tilde{J}_{\Phi}\,\tilde U_{\Psi,\mathrm b}^{*}.
$$

### Properties of the Conjugation

**1. It preserves the subspace $\mathbb{B}_{\Phi}$.** If $\tilde{A}_{\Phi} \in \mathbb{B}_{\Phi}$ and $\tilde U_{\Psi,\mathrm b}$ is a unit-norm biquaternion, then $\tilde U_{\Psi,\mathrm b}\tilde{A}_{\Phi}\tilde U_{\Psi,\mathrm b}^{*} \in \mathbb{B}_{\Phi}$.

**2. It preserves the biquaternion norm.** Since $\tilde U_{\Psi,\mathrm b}$ has unit norm, we have

$$
\tilde{A}_{\Phi,2}\tilde{A}_{\Phi,2}^{\natural} = \tilde U_{\Psi,\mathrm b}\tilde{A}_{\Phi}\tilde U_{\Psi,\mathrm b}^{*}\,\overline{\tilde U_{\Psi,\mathrm b}\tilde{A}_{\Phi}\tilde U_{\Psi,\mathrm b}^{*}} = \tilde{A}_{\Phi}\tilde{A}_{\Phi}^{\natural},
$$

so the biquaternion norm of the transformed four-vector is the same as the biquaternion norm of the original. This is the biquaternion expression of the Lorentz invariance of the Minkowski interval.

**3. It is a group action.** The composition of two rotor conjugations is another rotor conjugation: if $\tilde U_{\Psi,\mathrm b,1}$ and $\tilde U_{\Psi,\mathrm b,2}$ are two unit-norm biquaternions, then

$$
\tilde U_{\Psi,\mathrm b,2}(\tilde U_{\Psi,\mathrm b,1}\tilde{Q}\tilde U_{\Psi,\mathrm b,1}^{*})\tilde U_{\Psi,\mathrm b,2}^{*} = (\tilde U_{\Psi,\mathrm b,2}\tilde U_{\Psi,\mathrm b,1})\tilde{Q}(\tilde U_{\Psi,\mathrm b,2}\tilde U_{\Psi,\mathrm b,1})^{*},
$$

so the product of two rotors generates the composition of the two Lorentz transformations.

### The Action on Any Biquaternion

The rotor conjugation is written above for four-vectors, and it is worth stating that it is defined on **every** biquaternion, because that is what the field-theory articles need. Put

$$
Ξ_{\tilde U_{\mathrm{lor}}}(\tilde{Q}_1) := \tilde U_{\mathrm{lor}}\,\tilde{Q}_1\,\tilde U_{\mathrm{lor}}{}^{*}
\qquad\text{for any } \tilde{Q}_1 \in \mathbb{B}.
$$

Three properties follow from the fact that ${}^{*}$ is an involution and reverses products, and each was checked by direct expansion.

**It preserves both sectors.** If $\tilde{Q}_1^{*} = \pm\tilde{Q}_1$ then

$$
\bigl(\tilde U_{\mathrm{lor}}\tilde{Q}_1\tilde U_{\mathrm{lor}}{}^{*}\bigr)^{\dagger}
= \tilde U_{\mathrm{lor}}\,\tilde{Q}_1^{*}\,\tilde U_{\mathrm{lor}}{}^{*}
= \pm\,\tilde U_{\mathrm{lor}}\tilde{Q}_1\tilde U_{\mathrm{lor}}{}^{*},
$$

so $Ξ_{\tilde U_{\mathrm{lor}}}$ maps $\mathbb{B}_{\Phi}$ to itself, as the article already states for four-vectors, and equally maps $\mathbb{B}_{\Psi}$ to itself.

**It is not an algebra automorphism.** For a product,

$$
Ξ_{\tilde U_{\mathrm{lor}}}(\tilde{Q}_1\tilde{Q}_2) = \tilde U_{\mathrm{lor}}\tilde{Q}_1\tilde{Q}_2\tilde U_{\mathrm{lor}}{}^{*},
\qquad
Ξ_{\tilde U_{\mathrm{lor}}}(\tilde{Q}_1)\,Ξ_{\tilde U_{\mathrm{lor}}}(\tilde{Q}_2) = \tilde U_{\mathrm{lor}}\tilde{Q}_1\,\tilde U_{\mathrm{lor}}{}^{*}\tilde U_{\mathrm{lor}}\,\tilde{Q}_2\tilde U_{\mathrm{lor}}{}^{*},
$$

and these differ by the insertion of $\tilde U_{\mathrm{lor}}{}^{*}\tilde U_{\mathrm{lor}}$. They agree exactly when $\tilde U_{\mathrm{lor}}{}^{*} = \tilde U_{\mathrm{lor}}{}^{-1}$, that is, when $\tilde U_{\mathrm{lor}}$ is a **real** quaternion, which is the case of a pure spatial rotation. For a boost the rotor is Hermitian, $\tilde U_{\Psi,\mathrm b}^{*} = \tilde U_{\Psi,\mathrm b}$, so $\tilde U_{\Psi,\mathrm b}^{*}\tilde U_{\Psi,\mathrm b} = \tilde U_{\Psi,\mathrm b}^{2} \neq 1$ and the map is not multiplicative. The conjugation is a ${}^{*}$-conjugation, not the inner automorphism $\tilde{Q}_1\mapsto\tilde U_{\mathrm{lor}}\tilde{Q}_1\tilde U_{\mathrm{lor}}{}^{-1}$.

**It does not fix the centre.** The same fact shows where the formula must not be used. On a central scalar, $Ξ_{\tilde U_{\mathrm{lor}}}(b\,e_t) = b\,\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{*}$, which is not central in general; for a boost $\tilde U_{\Psi,\mathrm b}$ it equals $b\,\tilde U_{\Psi,\mathrm b}^2$ and has a vector part proportional to $\vec u_{\mathrm b}$. Central elements are therefore not carried to central elements, and the conjugation is meaningful on the sectors, whose elements are the physical quantities that transform, rather than on the algebra as a whole. This is consistent with the four-vector reading: the invariant object of the conjugation is the biquaternion norm, and the norm is quadratic in a sector element, not linear in an arbitrary one.

### Verification Against Component Formulas

The rotor conjugation can be verified against the standard component formulas for a Lorentz boost. Take a four-potential $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A$, and apply the rotor conjugation with $\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$.

The scalar part of $\tilde{A}_{\Phi,2}$ is

$$
\mathrm{Sc}(\tilde U_{\Psi,\mathrm b}\tilde{A}_{\Phi}\tilde U_{\Psi,\mathrm b}^{*}) = i\gamma\left(\frac{\xi}{c} - \frac{\vec v_b\cdot\vec A}{c}\right) = i\frac{\xi_2}{c},
$$

where the standard relations $\cosh\theta_{\mathrm{rpd}} = \gamma$ and $\sinh\theta_{\mathrm{rpd}} = \gamma v_b/c$ have been used. This gives

$$
\xi_2 = \gamma(\xi - \vec v_b\cdot\vec A),
$$

which is the standard Lorentz transformation of the scalar potential (in units where $\vec A$ is measured in the same units as $\xi$ divided by velocity, i.e., the SI convention).

The vector part gives

$$
\vec A_2 = \vec A + \frac{\gamma - 1}{u^2}(\vec v_b\cdot\vec A)\vec v_b - \gamma\frac{\xi}{c^2}\vec v_b,
$$

which is the standard Lorentz transformation of the vector potential, including the longitudinal projection term and the contribution from the scalar potential.

So the rotor conjugation $\tilde{A}_{\Phi,2} = \tilde U_{\Psi,\mathrm b}\tilde{A}_{\Phi}\tilde U_{\Psi,\mathrm b}^{*}$ reproduces the standard Lorentz transformation of the four-potential.

## Relating the Boost Biquaternion to the Four-Velocity

The two biquaternions $\tilde{V}_{\Phi}$ (four-velocity) and $\tilde U_{\Psi,\mathrm b}$ (boost) are distinct but related. Given the four-velocity

$$
\tilde{V}_{\Phi} = \gamma\left(ic\,e_t + \vec v\right),
$$

the associated boost biquaternion is

$$
\boxed{\;\tilde U_{\Psi,\mathrm b} = \sqrt{-\frac{i}{c}\tilde{V}_{\Phi}^{\natural}}\;}
$$

where the square root is the biquaternion square root (multivalued by sign) and $\tilde{V}_{\Phi}^{\natural} = \gamma(ic\,e_t - \vec v)$ is the quaternion conjugate.

### Derivation

The derivation is a direct computation. Define the unit four-velocity $\tilde{V}_{\Phi}/c = \gamma(i\,e_t + \vec v/c)$, so that $(\tilde{V}_{\Phi}/c)^{\natural} = \gamma(i\,e_t - \vec v/c)$. Then

$$
-i(\tilde{V}_{\Phi}/c)^{\natural} = -i\gamma(i\,e_t - \vec v/c) = \gamma\,e_t + i\gamma\frac{\vec v}{c}.
$$

On the other hand, the square of the boost biquaternion is

$$
\tilde U_{\Psi,\mathrm b}^2 = \exp\!\left(\theta_{\mathrm{rpd}}\,i\vec u_{\mathrm b}\right) = \cosh\theta_{\mathrm{rpd}} + i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b} = \gamma + i\gamma\frac{\vec v}{c},
$$

where the identification $\vec u_{\mathrm b} = \vec u_v$ (boost direction aligned with particle velocity) and the relations $\cosh\theta_{\mathrm{rpd}} = \gamma$, $\sinh\theta_{\mathrm{rpd}} = \gamma v/c$ have been used.

Comparing the two expressions,

$$
\tilde U_{\Psi,\mathrm b}^2 = -i(\tilde{V}_{\Phi}/c)^{\natural} = -\frac{i}{c}\tilde{V}_{\Phi}^{\natural},
$$

and hence

$$
\tilde U_{\Psi,\mathrm b} = \sqrt{-\frac{i}{c}\tilde{V}_{\Phi}^{\natural}}.
$$

### Interpretation

The formula $\tilde U_{\Psi,\mathrm b} = \sqrt{-i\tilde{V}_{\Phi}^{\natural}/c}$ says:

- The **four-velocity** $\tilde{V}_{\Phi}$ describes the state of motion of a particle or frame.
- The **boost biquaternion** $\tilde U_{\Psi,\mathrm b}$ is the "square root" of the (quaternion conjugate of the) unit four-velocity, up to a factor of $-i/c$.

The square root is **multivalued by sign**: both $\tilde U_{\Psi,\mathrm b}$ and $-\tilde U_{\Psi,\mathrm b}$ square to the same biquaternion. The two branches implement the **same** Lorentz transformation, since $\tilde U_{\Psi,\mathrm b}$ and $-\tilde U_{\Psi,\mathrm b}$ differ by the kernel element $-1$ of the two-to-one map $SL(2,\mathbb{C}) \to SO^+(1,3)$; the boost by $-\theta_{\mathrm{rpd}}$ is a different element, the quaternion conjugate $\tilde U_{\Psi,\mathrm b}^{\natural}$. The conventional branch is selected by requiring the real scalar part of $\tilde U_{\Psi,\mathrm b}$ to be positive, i.e., $\cosh(\theta_{\mathrm{rpd}}/2) > 0$.

### The Closed-Form Rotor and the Bisector Property

For a **simple** Lorentz rotation — a boost, or a rotation, or in general a transformation in a single non-null plane — the rotor can be recovered from the transformation of one vector in the plane, and the recovery has a clean closed form worth recording because it is used in the paravector computation of the boost of a wave (*Paravectors and the Geometry of Spacetime*, *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*).

Let $p$ be a non-null Hermitian element lying in the plane of the rotation, so that it commutes with the rotor, and let

$$
r \;=\; \tilde U_{\Psi,\mathrm b}\,p\,\tilde U_{\Psi,\mathrm b}^{*} \;=\; \tilde U_{\Psi,\mathrm b}^2\,p
$$

be its image, the second form using the commutation. Then

$$
\tilde U_{\Psi,\mathrm b} \;=\; \left(r\,p^{-1}\right)^{1/2},
$$

the square root being the biquaternion square root, multivalued by sign, and the two branches differing by the kernel element $-1$ of the double cover. Equivalently, since $\tilde U_{\Psi,\mathrm b}\,p$ lies along the **bisector** of $p$ and $r$,

$$
\tilde U_{\Psi,\mathrm b}\,p \;=\; \frac{p + r}{\sqrt{2\,\bigl\langle (p+r)\,p^{-1}\bigr\rangle_S}},
\qquad\text{so that}\qquad
\tilde U_{\Psi,\mathrm b} \;=\; \frac{(p+r)\,p^{-1}}{\sqrt{2\,\bigl\langle (p+r)\,p^{-1}\bigr\rangle_S}},
$$

where $\langle\,\cdot\,\rangle_S$ is the scalar part. The denominator is a positive real number because $p$ is non-null, and it normalizes the bisector to unit norm; the factor $p^{-1}$ on the right places the result in the plane.

The **bisector property** is the statement that the image $r=\tilde U_{\Psi,\mathrm b}^2p$ and the original $p$ are symmetrically placed about the direction of $\tilde U_{\Psi,\mathrm b} p$, which is the direction of $p+r$; it is why the rotor can be reconstructed from one element of the plane and its image. The closed form is the second printed form of the source (Baylis, §V.B), whose PDF extraction is ambiguous about the placement of the square-root exponent; the recomputation above selects the form displayed here, with no leading factor $p$ and the exponent $1/2$ on the whole denominator. The first form, $\tilde U_{\Psi,\mathrm b}=(rp^{-1})^{1/2}$, is unambiguous and agrees with it.

## The Group Structure

The **unit-norm biquaternions** form a group under multiplication. The general element is

$$
\tilde{Q} \in \{\tilde{Q} \in \mathbb{B} : \tilde{Q}\tilde{Q}^{\natural} = e_t\},
$$

which under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ is the group $SL(2, \mathbb{C})$, the group of $2 \times 2$ complex matrices with determinant $1$. The map from $SL(2, \mathbb{C})$ to the proper orthochronous Lorentz group $SO^+(1,3)$ is $2$-to-$1$, exactly as in the standard matrix formulation.

**Pure boosts** are the **Hermitian** elements of $SL(2,\mathbb{C})$: those satisfying $\tilde U_{\Psi,\mathrm b}^{*} = \tilde U_{\Psi,\mathrm b}$. They do **not** form a subgroup of $SL(2,\mathbb{C})$, because the product of two non-collinear boosts is generally a boost plus a spatial rotation (the Thomas–Wigner rotation), which is not Hermitian. So the set of pure boosts is a symmetric submanifold of $SL(2,\mathbb{C})$, but not a group.

**Pure spatial rotations** are the elements with **real vector part** (i.e., lying in $\mathbb{B}_{H}$, the real quaternion subalgebra), satisfying $\tilde u_{\mathrm r} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\vec u_{\mathrm r}$ with $\vec u_{\mathrm r}^2 = -e_t$. These form the subgroup $SU(2) \subset SL(2,\mathbb{C})$.

The general Lorentz transformation is the product of a boost and a rotation, and corresponds to a general element of $SL(2,\mathbb{C})$.

## Active, Passive and Relative Transformations; the Reciprocal Basis

The word "transformation" hides three different operations, and the algebra states all three with the same rotor. It is worth fixing the three interpretations, because the source of the paravector literature distinguishes them and the distinction is not visible in the component formulas.

**Active.** The object is transformed and the frame is held fixed: a four-vector $\tilde{Q}$ is carried to $\tilde{Q}_2 = \tilde U_{\mathrm{lor}}\tilde{Q}\tilde U_{\mathrm{lor}}{}^{*}$, with $\tilde U_{\mathrm{lor}}$ the rotor of the operation. **Passive.** The frame is changed and the object is fixed: the components of the same object in the new frame are those of $\tilde U_{\mathrm{lor}}{}^{-1}\tilde{Q}\tilde U_{\mathrm{lor}}{}^{-{}^{*}}$, the inverse conjugation. **Relative.** Two frames are related by a rotor that is the ratio of their eigenspinors: if two worldlines carry eigenspinors, the Lorentz rotors $\tilde U_{\mathrm{lor},1}$ and $\tilde U_{\mathrm{lor},2}$ (in the sense of *The Eigenspinor: The Lorentz Rotor as a Function of Proper Time*), then the rotor

$$
\tilde U_{\Psi,\mathrm b,2\leftarrow1} = \tilde U_{\Psi,\mathrm b,2}\tilde U_{\Psi,\mathrm b,1}^{-1}
$$

carries the four-momentum of the first to the four-momentum of the second, $\tilde{P}_{\Phi,1}\mapsto\tilde{P}_{\Phi,2}$, and is the frame-to-frame transformation. The three interpretations differ by which factor of the rotor is inverted, and the physics of "which frame moves relative to which" is the choice among them. The series writes the abstract group element as $\tilde U_{\mathrm{lor}}$ without committing to an interpretation, and says which interpretation is meant only where a physical frame is named.

**The reciprocal basis.** The component transformation is most cleanly stated with a dual basis. On the four-dimensional space spanned by $\{e_t, \vec e_x, \vec e_y, \vec e_z\}$, define the dual basis by the trace pairing $\mathrm{Sc}(\mathcal E_{\mathrm{du},\mu}\mathcal{E}_\nu) = \delta_{\mu\nu}$. The basis and its dual are

$$
\mathcal{E}_0 = e_t,\quad \mathcal{E}_k = \vec e_k,
\qquad
\mathcal E_{\mathrm{du},0} = e_t,\quad \mathcal E_{\mathrm{du},k} = -\vec e_k,
$$

the minus signs coming from $\vec e_k^2 = -e_t$: the metric is carried by the dual, not by any index-raising. Because the coefficient of $e_t$ is the imaginary $i r'_t$, the pair $(q_0, q_k) = (i r'_t, x_k)$ is the coordinate quadruple. Given a rotor $\tilde U_{\mathrm{lor}}$, the components transform as

$$
q_{2\mu} = \sum_{\nu} \Lambda_{\mu\nu}\, q_{\nu},
\qquad
\Lambda_{\mu\nu} = \mathrm{Sc}\!\left(\mathcal E_{\mathrm{du},\mu}\,\tilde U_{\mathrm{lor}}\,\mathcal{E}_{\nu}\,\tilde U_{\mathrm{lor}}{}^{*}\right),
$$

and the matrix $\Lambda_{\mu\nu}$ is the ordinary Lorentz transformation matrix in the basis, the same one the opening line calls $\Lambda_{\mu\nu}$.

This is the sense in which the framework "raises and lowers no indices": the metric sits in the coefficients and in the dual basis, and the transformation law is a matrix multiplication without a metric tensor in sight. The reciprocal basis is the device that makes the component formula look ordinary while the geometry stays in the algebra.

## What Fixes the Transformation: The Experimental Route

Everything so far derives the transformation; nothing so far says what *selects* it. The algebra of $\mathbb{B}$ contains real and imaginary rotation angles alike, so it expresses a boost rotor with a real angle as readily as one with an imaginary angle, and the choice between them is not a choice the algebra makes. It was made by experiment. This section records the experiments and states their ownership, because a derivation that never says what fixes it invites the reader to mistake the derivation for the evidence.

**Boundary.** Nothing in this section is biquaternionic and nothing in it is a result of this corpus. The optical experiments, the contraction hypothesis and the two postulates are standard special relativity, recorded here from a single source, the *Relativité restreinte* chapter of J. Surdej, and recomputed arithmetically where a number appears. The biquaternionic formulation is a **reformulation** of the same group, so these experiments can neither confirm nor refute it: they select the group $SO^+(1,3)$, and every faithful representation of that group reproduces them. The bounds by which the reformulation could be told apart from the group belong to *The Empirical Status of the Biquaternion Framework*, not here.

### The Three Optical Experiments and Their Orders in $\beta$

Three nineteenth-century optical experiments bear on the kinematics, at different orders in the velocity ratio $\beta = v/c$.

| Experiment | Order in $\beta$ | What it measures | Result |
|---|---|---|---|
| Aberration of starlight, Bradley, 1725 | first | the apparent direction of a star as the Earth's velocity turns through the year | $20.50$ arcsec of annual shift, equal to the classical $\tan\alpha = \beta$ |
| Light drag in moving water, Fizeau, 1851 | first | the speed of light in water of velocity $v$ | the Fresnel fraction $1-1/n^2$ of $v$, which is $0.435$ at $n = 1.33$ |
| Ether drift, Michelson 1881, Michelson and Morley 1887 | second | the round-trip light time in two perpendicular arms | null, where about $0.37$ fringe was expected at $30$ km/s |

**Aberration settles nothing by itself.** The classical value $\tan\alpha = \beta$ follows from a ballistic picture of light as well as from a wave in a stationary ether. At the Earth's orbital speed $v = 29.79$ km/s one has $v/c = 9.94\times10^{-5}$, which is $20.50$ arcsec in angle, the observed annual shift; the experiment shows a relative velocity between the Earth and the incoming light, but not which kinematics governs it.

**Fizeau's drag is first order, and it is a partial drag.** An ether neither dragged nor displaced predicts no dependence on the water's motion, and a fully dragged ether predicts the whole $v$; what is measured is the fraction $1-1/n^2$ of Fresnel's formula, that is $0.435$ for $n = 1.33$. Historically this was accommodated by postulating a partial drag of the ether by the medium — an inserted property, of the same kind as the contraction below — so the experiment does not by itself refute the Galilean kinematics. Its place in the record is different: the relativistic velocity-addition formula reproduces Fresnel's fraction exactly at first order, so the experiment that motivated a drag hypothesis became a confirmation of the Lorentz kinematics.

**Michelson–Morley is second order, and it is the decisive one.** The ether wind enters as $(v/c)^2$, which is $1.0\times10^{-8}$ at $v = 30$ km/s; the expected fringe shift is this factor times the effective optical path divided by the wavelength, which for the standard effective arm of about $11$ m and $\lambda = 590$ nm is $0.37$ fringe, within the interferometer's reach. The measured shift was consistent with zero. The source's summary of the difficulty is that the result made the ether "immobile with respect to the Earth", which is geocentric and contradicts both aberration and Fizeau; what had to be abandoned was the classical interpretation itself.

### The Classical Rescue and Its Price

The first repair, proposed independently by G. FitzGerald and H. A. Lorentz in 1893, was a longitudinal contraction of moving bodies by the factor $1/\gamma$. The contraction is of order $\beta^2/2$, which at the orbital speed is $5.0\times10^{-9}$. It hides the ether wind, and its price is the corpus's recurring one: it is a **deformation inserted against the kinematics**, not derived from anything. That price is why the FitzGerald–Lorentz contraction is not the ancestor of the biquaternionic rotor.

Lorentz then arrived at the transformation that bears his name, and H. Poincaré — whom the source credits as the first to see it distinctly — stated that there is a deep antipathy between Maxwell's equations and the Galilean transformation. What was missing was Einstein's step of 1905, and it is worth recording how he described it himself, in the retrospective the source quotes:

> "The new feature of it was the realization of the fact that the bearing of the Lorentz-transformations transcended their connection with Maxwell's equations and was concerned with the nature of space and time in general. A further new result was that the 'Lorentz invariance' is a general condition for any physical theory."

That sentence is the one that matters for the corpus. The two postulates of 1905 — the speed of light in vacuum has the same value in every inertial frame whatever the motion of the source, and the laws of physics take the same form in every inertial frame — replace the inserted contraction by a kinematics, and they promote Lorentz invariance from a property of Maxwell's theory to a requirement on any theory. The biquaternionic rotor is a reformulation of the second postulate, not a competitor to it, and the corpus follows Einstein's retrospective when it treats Lorentz invariance as the general condition a candidate framework must meet.

### What the Derivation in This Article Does and Does Not Settle

The formal derivation above decides neither of the two things the experiments decide:

1. **The angle.** Nothing in the algebra forces the boost's rotation angle to be imaginary; that is what the constancy of $c$ forces, at second order, and the first-order experiments place the same constraint on the velocity-addition law.
2. **The parameterisation.** The rapidity $\theta_{\mathrm{rpd}}$, with $\tanh\theta_{\mathrm{rpd}} = v_b/c$ and the $\cosh(\theta_{\mathrm{rpd}}/2)$ and $\sinh(\theta_{\mathrm{rpd}}/2)$ of the boost biquaternion, is an interpretation of the experiments and not of the algebra.

Conversely, the experiments do not decide between the biquaternion formulation and the matrix one. They are experiments on the group, and a faithful representation cannot fail them; a reformulation must be judged by what it predicts beyond the group. That is the same point the empirical-status article makes from the other direction.

## The Complex Nature of the Rotation

We are now in a position to discuss the subtleties of working over the complex numbers.

### Real vs. Complex Rotations

The Lorentz transformation is a **real** transformation of the real coordinates $(r'_t,r_x,r_y,r_z)$. But in the $i r'_t$ convention, the time coordinate is $i r'_t$, which is **imaginary** in the real slice. So the transformation that acts on $(i r'_t, r_x, r_y, r_z)$ is a **complex** rotation, even though the original transformation on $(r'_t,r_x,r_y,r_z)$ is real.

The complex nature of the rotation appears in the following places:

1. **The rotation angle is imaginary.** A boost is a rotation by an imaginary angle $i\theta_{\mathrm{rpd}}$ in the plane spanned by the time direction and the boost direction. In real Euclidean geometry, a rotation by an imaginary angle is not a rotation at all — it is a **hyperbolic rotation**. The Lorentz boost is precisely this: a hyperbolic rotation in the $(i r'_t, r_x)$ plane.

2. **The rotor has an imaginary vector part.** The boost biquaternion $\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ has a purely imaginary vector part. In contrast, a spatial rotation rotor has a real vector part.

3. **The bilinear form is complex.** The quantity preserved by the rotation is not the real Euclidean norm (which is positive-definite), but the **general plain bilinear form** $(x_0)^2 + (x_1)^2 + (x_2)^2 + (x_3)^2$, which is the biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$. On the real slice, this form can be negative, positive, or zero.

### The Euclidean Form Is Only Apparent

The Euclidean form $ds^2 = (x_0)^2 + (x_1)^2 + (x_2)^2 + (x_3)^2$ with $x_0= i r'_t$ appears to be a genuine Euclidean metric on $\mathbb{R}^4$. But it is not: the coordinate $x_0$ is constrained to be imaginary (since $r'_t$ is real and $x_0= i r'_t$). So the "real slice" on which the Lorentz transformations act is not all of $\mathbb{R}^4$ but the subspace $\{(i r'_t, r_x, r_y, r_z) : r'_t, r_x, r_y, r_z \in \mathbb{R}\}$, which is a **complex subspace** of $\mathbb{C}^4$.

The Lorentz group $SO(1,3)$ acts on this slice as the subgroup of $SO(4, \mathbb{C})$ that preserves the slice. So the statement "the Lorentz transformation is a rotation in 4-dimensional Euclidean space" is correct, but the space in question is $\mathbb{C}^4$ with a general plain bilinear form, not $\mathbb{R}^4$ with a real Euclidean form.

## The Local Complex Structure

The boost biquaternion $\tilde U_{\Psi,\mathrm b}$ uses the speed of light $c$ through the rapidity $\theta_{\mathrm{rpd}}$: $\tanh\theta_{\mathrm{rpd}} = v_b/c$. In a material medium with permittivity $\epsilon$ and permeability $\mu$, the local speed of light is $c = 1/\sqrt{\epsilon\mu}$, which may differ from the vacuum speed $c_0$.

This means that the rapidity and the boost biquaternion are **local** quantities: they depend on the local electromagnetic properties of the medium. In vacuum, $c = c_0$ and the rapidity is a fixed function of the velocity. In a medium, $c$ varies from point to point, and the boost biquaternion varies accordingly.

This is consistent with the program of the companion articles on the $i r'_t$ convention and on complexified spacetime: the complex structure is **local**, determined by the local electromagnetic properties of the medium. The boost biquaternion inherits this locality, and it becomes a **field** in the same sense as the electromagnetic field.

## Open Questions

1. **Higher-rank tensors.** The rotor conjugation $\tilde{Q}_2 = \tilde U_{\mathrm{lor}}\tilde{Q}\tilde U_{\mathrm{lor}}{}^{*}$ applies to four-vectors. How does the biquaternion formulation extend to higher-rank tensors, such as the field-strength tensor $F_{\mu\nu}$ and the energy–momentum tensor $T_{\mu\nu}$?

2. **Spinor transformations.** A spinor transforms under the Lorentz group by a **one-sided** multiplication, not by a rotor conjugation. What is the precise biquaternion form of the spinor transformation, and how does it relate to the Dirac equation?

3. **The local structure.** In a medium with varying electromagnetic properties, the boost biquaternion is a **field**. What are the consequences of treating the boost biquaternion as a field, and how does it couple to the electromagnetic field?

4. **The relation to the twistor program.** Penrose's twistor theory uses the complexified spinor space $\mathbb{C}^4$, which is closely related to the biquaternion algebra. How does the biquaternion formulation of the Lorentz transformation relate to the twistor formulation?

5. **The general transformation.** The article has focused primarily on pure boosts. What is the biquaternion form of the general Lorentz transformation (boost plus spatial rotation), and how does the non-Hermiticity of $\tilde U_{\mathrm{lor}}$ manifest physically?

These questions are open.

## Summary

The Lorentz transformation in biquaternionic form is a **rotation** in the complexified four-dimensional space, implemented by the **rotor conjugation**

$$
\tilde{Q}_2 = \tilde U_{\Psi,\mathrm b}\,\tilde{Q}\,\tilde U_{\Psi,\mathrm b}^{*},
$$

where $\tilde U_{\Psi,\mathrm b}$ is the **boost biquaternion**

$$
\tilde U_{\Psi,\mathrm b} = \exp\!\left(\frac{\theta_{\mathrm{rpd}}}{2}\,i\vec u_{\mathrm b}\right) = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b}.
$$

For a pure boost, $\tilde U_{\Psi,\mathrm b} \in \mathbb{B}_{\Psi}$ (Hermitian, unit norm). The rapidity $\theta_{\mathrm{rpd}}$ is related to the velocity $\vec v_b$ by $\tanh\theta_{\mathrm{rpd}} = v_b/c$.

The **four-velocity biquaternion** $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$, which lives in $\mathbb{B}_{\Phi}$, is related to the boost biquaternion by

$$
\tilde U_{\Psi,\mathrm b} = \sqrt{-\frac{i}{c}\tilde{V}_{\Phi}^{\natural}}
$$

the square root being multivalued by sign, with the physical branch selected by $\mathrm{Sc}(\tilde U_{\Psi,\mathrm b}) > 0$.

The rotation is **complex** in the sense that the rotation angle (the rapidity) is imaginary in the $i r'_t$ convention. The Euclidean character of the metric is only apparent: the real slice on which the Lorentz transformations act is a complex subspace of $\mathbb{C}^4$, not a real Euclidean space. The Lorentz group $SO(1,3)$ is the subgroup of the complex rotation group $SO(4,\mathbb{C})$ that preserves this slice.

The **same rotor conjugation applies to all four-vectors** in the anti-Hermitian subspace $\mathbb{B}_{\Phi}$: the four-position, four-velocity, four-momentum, four-force, four-potential, and four-current. The unit-norm biquaternions form the group $SL(2,\mathbb{C})$, which is the double cover of the proper orthochronous Lorentz group $SO^+(1,3)$.

The transformation itself is fixed by experiment, not by the algebra: aberration, the Fizeau drag and the Michelson–Morley null result select the group $SO^+(1,3)$, and the biquaternion form is a faithful reformulation of that group, so it reproduces those experiments by construction rather than by prediction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (real scalar, imaginary vector) |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (imaginary scalar, real vector) |
| $\mathbb{B}_{H}$ | Quaternion subspace (home of the spatial rotation rotors) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\beta = v/c$ | Velocity ratio of a frame or particle |
| $\gamma = 1/\sqrt{1-\beta^2}$ | Lorentz factor |
| $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | Four-velocity biquaternion |
| $\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | Boost biquaternion (Hermitian for pure boosts) |
| $\theta_{\mathrm{rpd}}$ | Rapidity, $\tanh\theta_{\mathrm{rpd}} = v_b/c$ |
| $\vec u_{\mathrm b}$ | Unit vector in boost direction |
| $\tilde{Q}_2 = \tilde U_{\Psi,\mathrm b}\tilde{Q}\tilde U_{\Psi,\mathrm b}^{*}$ | Rotor conjugation |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation of special relativity.
- Albert Einstein, *The Meaning of Relativity* (Princeton, 1922), for the $i r'_t$ formulation.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the spinor representation of the Lorentz group.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of the Lorentz transformation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment of Lorentz rotors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and the Lorentz group.
- V. V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a biquaternionic approach to the Lorentz group.
- L. A. Alexeyeva, "Lorentz Transformations for One Biquaternionic Model of the Electro-Gravimagnetic Field. Conservation Laws" (2009), for the induced action of the Lorentz transformation on the field biquaternions — potential, strength, charge–current and power–force — worked out component by component, and for the finding that the model's charge–mass conservation law is not invariant. The English text of the same work is arXiv:1104.1483v1; arXiv:0904.3446v1 is the Russian preprint.
- Jean Surdej, *La relativité restreinte*, chapter 3 of the lecture notes (2015–2016), for the experimental route recorded in *What Fixes the Transformation: The Experimental Route*: aberration of starlight, the Fizeau drag, the Michelson–Morley null result and the source's own interpretation of it, the FitzGerald–Lorentz contraction, Poincaré on the antipathy between Maxwell's equations and the Galilean transformation, the two postulates of 1905, and Einstein's 1955 retrospective on the bearing of the transformation.
- William E. Baylis, *Relativity in Introductory Physics*, *Canadian Journal of Physics* **82** (2004) 853–873 (arXiv:physics/0406158), §V.B, for the closed-form rotor and the bisector property recorded here, and for the paravector interpretation of the same transformation.

