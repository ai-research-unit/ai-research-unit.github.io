# __The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form__

## Introduction

The two preceding articles of this subcategory treat systems whose configuration is a real vector — the free particle and the harmonic oscillator — and in both the energy, the frequency and the phase are scalars. The present article isolates the common structure and gives it a name. The **central-scalar limit** of classical mechanics is the restriction of the biquaternion framework in which

1. every scalar quantity of the system — the energy, the potential, the mass, the time, the orbital frequency — is a **central** scalar, that is, a real multiple of the identity $e_0$;
2. every configuration quantity — the position, the velocity, the momentum, the force, the angular momentum — is a **real vector**, an element of the real three-space $\operatorname{span}\{e_1, e_2, e_3\}$ inside the material sector $\mathbb{M}_-$; and
3. no vector direction of the informational sector $\mathbb{M}_+$ is occupied.

The name records the first two conditions; the third is what makes the limit the home of **structureless particles**. A nonzero element of the form $i\mathbf{s} \in \mathbb{M}_+$ is an internal vector degree of freedom, and the direction of such an element is a spin-like variable with its own precession. The central-scalar limit excludes it by construction, and that is exactly the spin-zero condition of the present subcategory: a point particle with no intrinsic angular momentum, no intrinsic magnetic moment, and no multipole structure.

The article is the frame around the two central-force articles that follow. It does three things. It fixes the kinematic setting — how the non-relativistic world is realized in the algebra and where each mechanical quantity sits. It develops the general central-force structure: the algebraic criterion for a force to be central, the identification of angular momentum with the commutator of position and momentum, the conservation law that follows, the reduction to a radial problem, and Binet's equation for the orbit. And it delimits the limit, recording what is excluded and what the informational sector contributes when it is reduced to a central scalar.

The treatment is classical and non-quantum throughout. The companion articles *The Harmonic Oscillator in Biquaternionic Form* and *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case* treat the operator versions of two of these systems; the states, the operators and the canonical commutator do not appear here, and the only bracket used is the classical Poisson bracket of the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \epsilon_{jkl}e_l$ for $j \neq k$; the scalar imaginary $i$ is central with $i^2 = -e_0$. The anti-Hermitian subspace $\mathbb{M}_-$ is the material sector and the Hermitian subspace $\mathbb{M}_+$ the informational sector, with $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ and $i\mathbb{M}_\pm = \mathbb{M}_\mp$. The real-quaternion subalgebra is $\mathbb{H}_{\mathbb{B}}$, its pure part is the real three-space $\operatorname{span}\{e_1, e_2, e_3\}$, and the centre is $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$. For a quaternion $\mathbf{a} = a_1e_1 + a_2e_2 + a_3e_3$ the norm form is $N(\mathbf{a}) = \mathbf{a}\overline{\mathbf{a}} = |\mathbf{a}|^2e_0$, so that $N$ restricts to the positive Euclidean square on the real three-space. The trace satisfies $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ for $\tilde{P}, \tilde{H} \in \mathbb{M}_+$.

## The Non-Relativistic Configuration

### Where the World Is Placed

The full worldline is the material-sector curve $\tilde{X}(t) = ic\,t\,e_0 + \mathbf{x}(t)$. In the non-relativistic limit the scalar direction $ie_0$ is inert — the Galilean shear of the first article leaves it fixed — so the configuration space of the non-relativistic particle is the direct sum

$$
ie_0\mathbb{R} \;\oplus\; \operatorname{span}\{e_1, e_2, e_3\} \;\subset\; \mathbb{M}_- ,
$$

that is, one scalar direction for time and three real vector directions for space. This is the algebra's realization of $\mathbb{R} \times \mathbb{R}^3$, and it is the setting of every classical problem in this subcategory.

The scalar direction is the imaginary $ie_0$, so the time coordinate appears as the imaginary scalar $ic\,t$; the spatial directions are the real $e_k$, so the position is a real pure quaternion. The velocity, acceleration, momentum and force are then all real pure quaternions,

$$
\mathbf{v} = \dot{\mathbf{x}}, \qquad \mathbf{a} = \ddot{\mathbf{x}}, \qquad \mathbf{p} = m\mathbf{v}, \qquad \mathbf{F} = m\mathbf{a} ,
$$

each obtained from the others by differentiation with respect to the scalar parameter $t$ or by multiplication by the central scalar $m$. The three directions are rotated among themselves by the unit real quaternions, and the rotation is the adjoint action $R(\cdot)R^{-1}$ of the companion article *The Reflection and the Rotation in Biquaternionic Form*.

### Scalars Are Central

Every quantity in the list above that is not a vector is a central scalar. The mass is $m e_0$; the kinetic energy is $\tfrac12m|\mathbf{v}|^2 e_0$; the potential of a central force will be $V(r)e_0$; the time is the parameter multiplying $ie_0$. In each case the algebra element is a multiple of the identity, hence commutes with everything, and hence transforms trivially under every rotation and every frame change. This triviality is a feature and not a defect: it is why the scalar quantities of non-relativistic mechanics are frame-independent numbers and why the rotation group acts on the vector quantities alone.

The placement of the scalars along $e_0$ also fixes their sector. A real scalar multiple of $e_0$ is Hermitian and lies in $\mathbb{M}_+$, so the energy and the potential are elements of the **informational** sector, while the configuration — position, momentum, force — lies in the vector part of the **material** sector. The central-scalar limit is therefore not a confinement to one sector: it uses the central direction of $\mathbb{M}_+$ for the scalar data and the vector directions of $\mathbb{M}_-$ for the configuration, and it leaves the vector directions of $\mathbb{M}_+$ untouched.

### A Digression on the Kinetic Sign

One point of the placement deserves emphasis because it is easy to get wrong. The kinetic energy of a pure vector is **minus** half the quaternion square, not half the square:

$$
\tfrac12m\mathbf{v}^2 = -\tfrac12m|\mathbf{v}|^2 e_0 ,
$$

since $\mathbf{v}^2 = -|\mathbf{v}|^2e_0$. The physically positive kinetic energy is therefore

$$
T = -\tfrac12 m\,\mathbf{v}^2 = \tfrac12 m\,N(\mathbf{v}) = \tfrac12 m|\mathbf{v}|^2 e_0 ,
$$

which is the norm form of the velocity, up to the mass. The sign is the same algebraic fact — $e_k^2 = -e_0$ — that gives the real three-space its Euclidean-square norm and the material sector its Lorentzian signature. In the central-scalar limit, where the velocities are small and the vectors are real, the norm form of a vector is its positive Euclidean square, and the kinetic energy is a positive central scalar.

## The Definition of the Central-Scalar Limit

The conditions of the introduction can be stated as a restriction on the algebra elements a problem is allowed to use. A classical central-force problem in the limit is specified by:

- a real vector $\mathbf{r}(t) \in \operatorname{span}\{e_1, e_2, e_3\} \subset \mathbb{M}_-$ for the position;
- a real vector $\mathbf{p}(t)$ for the momentum, equal to $m\dot{\mathbf{r}}$;
- a real vector $\mathbf{F} = \dot{\mathbf{p}}$ for the force;
- a **central scalar** potential $\tilde{V} = V(|\mathbf{r}|)e_0 \in \mathbb{M}_+$, depending on the position only through the rotation-invariant length $|\mathbf{r}| = \sqrt{N(\mathbf{r})}$;
- a central scalar energy $\tilde{E} = E e_0$.

No element of this list has a nonzero vector part in $\mathbb{M}_+$, and none has a noncentral scalar part. The vector part of the configuration is entirely in $\mathbb{M}_-$; the scalar data are entirely in the central part of $\mathbb{M}_+$.

The reason the potential may depend on the position only through $|\mathbf{r}|$ is that it is a central scalar and therefore rotation-invariant. Under a rotation rotor $R \in \mathbb{H}_{\mathbb{B}}$ with $R\overline{R} = e_0$, the position transforms as $\mathbf{r} \mapsto R\mathbf{r}R^{-1}$, and the norm form is invariant,

$$
N(R\mathbf{r}R^{-1}) = R\,N(\mathbf{r})\,R^{-1} = N(\mathbf{r}) ,
$$

because the norm form is a central scalar. Hence $V(|\mathbf{r}|)e_0$ is unchanged by every rotation: a central scalar potential is automatically spherically symmetric, and its symmetry is trivial in the sense of the preceding section.

## Two Limits, Distinguished

The name "central-scalar limit" combines two restrictions that are logically independent, and it is worth separating them because the rest of the corpus uses both.

**The non-relativistic limit** is a limit of the kinematics: the ratio $v/c$ is small, the boost rotor of the frame contractions degenerates into a shear, the scalar direction $ie_0$ becomes an inert parameter, and the configuration space reduces to $\mathbb{R}\times\mathbb{R}^3$. It is a statement about the **transformation law** and about which terms in an expansion are retained. A relativistic central-force problem — the relativistic Kepler problem, for instance — takes the limit in the other direction while remaining central and scalar.

**The central-scalar restriction** is a statement about which **directions of the algebra are occupied**. It says that the scalar data are central and the configuration is a real vector, and that no vector direction of $\mathbb{M}_+$ is excited. It does not by itself require small velocities. A rigid body with an intrinsic spin is excluded by this restriction even when its centre of mass moves non-relativistically, because its state carries an element of $\mathbb{M}_+$ with a nonzero vector part.

The articles of this subcategory take **both** restrictions at once: they are non-relativistic and spin-zero. That combination is what makes the framework's description of them so economical — the algebra contributes the real three-space, its rotations, and the central scalars, and nothing else — and it is also what defines the boundary with the sibling subcategories. A non-relativistic problem with intrinsic magnetism violates the central-scalar restriction while respecting the non-relativistic limit; a relativistic structureless problem violates the non-relativistic limit while respecting the central-scalar restriction.

## Central Forces and Angular Momentum

### The Algebraic Criterion for a Central Force

A force is **central** (about the origin) when it is everywhere directed along the position, $\mathbf{F} \parallel \mathbf{r}$. In the real-quaternion subalgebra this condition has three equivalent forms:

$$
\mathbf{F}\parallel\mathbf{r} \;\Longleftrightarrow\; \mathbf{r}\times\mathbf{F} = 0 \;\Longleftrightarrow\; [\mathbf{r}, \mathbf{F}] = 0 \;\Longleftrightarrow\; \mathbf{F}\,\mathbf{r} = -\mathbf{F}\cdot\mathbf{r}\,e_0 \ \text{is central} .
$$

The middle form uses the identity for two real pure quaternions,

$$
\mathbf{a}\mathbf{b} = -\mathbf{a}\cdot\mathbf{b}\,e_0 + \mathbf{a}\times\mathbf{b} ,
$$

so that the commutator isolates the cross product,

$$
[\mathbf{a}, \mathbf{b}] = \mathbf{a}\mathbf{b} - \mathbf{b}\mathbf{a} = 2\,\mathbf{a}\times\mathbf{b} .
$$

A central force is therefore exactly a force that **commutes with the position**. This is the algebraic statement of "$\mathbf{F}$ is along $\mathbf{r}$", and it is the criterion that the oscillator satisfies, since its force is $-m\omega^2\mathbf{r}$ and a real vector commutes with its own multiples.

### Angular Momentum as a Commutator

For a particle of momentum $\mathbf{p}$ the angular momentum is $\mathbf{L} = \mathbf{r}\times\mathbf{p}$. By the identity above,

$$
\mathbf{L} = \mathbf{r}\times\mathbf{p} = \tfrac12[\mathbf{r}, \mathbf{p}] .
$$

The three components $L_k$ are the three real coefficients of the commutator of the position and momentum quaternions. The product $\mathbf{r}\mathbf{p}$ contains both $\mathbf{L}$ and the scalar $-\mathbf{r}\cdot\mathbf{p}$,

$$
\mathbf{r}\mathbf{p} = -\mathbf{r}\cdot\mathbf{p}\,e_0 + \mathbf{L} ,
$$

so the angular momentum is the **vector part of the quaternion product** of position and momentum, and the scalar part is the negative of their inner product. This is the sense in which the real-quaternion product packages the two invariants of a pair of vectors: its scalar part is the dot product and its vector part is the cross product.

### Conservation

The conservation of angular momentum for a central force follows from the commutator form with no vector identity beyond the product rule. Indeed,

$$
\dot{\mathbf{L}} = \tfrac12\frac{d}{dt}[\mathbf{r}, \mathbf{p}] = \tfrac12\left([\dot{\mathbf{r}}, \mathbf{p}] + [\mathbf{r}, \dot{\mathbf{p}}]\right) = \tfrac12\left(m[\dot{\mathbf{r}}, \dot{\mathbf{r}}] + [\mathbf{r}, \mathbf{F}]\right) = \tfrac12[\mathbf{r}, \mathbf{F}] ,
$$

because $[\dot{\mathbf{r}}, \dot{\mathbf{r}}] = 0$ and $\dot{\mathbf{p}} = \mathbf{F}$. Hence

$$
\dot{\mathbf{L}} = 0 \;\Longleftrightarrow\; [\mathbf{r}, \mathbf{F}] = 0 ,
$$

which is precisely the criterion for a central force. **The conservation of angular momentum and the centrality of the force are the same algebraic condition**, and the derivation is a two-line computation in the algebra rather than a vector identity about torque. The torque $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$ is $\tfrac12[\mathbf{r}, \mathbf{F}]$, so the result is the standard $\dot{\mathbf{L}} = \boldsymbol{\tau}$ written as a commutator.

### Planar Motion and the Areal Law

Since $\mathbf{L}$ is a constant real vector, the motion lies in the plane through the origin perpendicular to $\mathbf{L}$: contracting the definition with $\mathbf{r}$ gives $\mathbf{r}\cdot\mathbf{L} = \mathbf{r}\cdot(\mathbf{r}\times\mathbf{p}) = 0$, so the position is always orthogonal to the fixed direction $\mathbf{L}$. The motion is therefore planar for every central force, and the two-dimensional problem is the general one.

In that plane, with polar coordinates $(r, \theta)$, the angular momentum is $L = mr^2\dot\theta$. The **areal velocity** is

$$
\frac{dA}{dt} = \frac{1}{2}r^2\dot\theta = \frac{L}{2m},
$$

a constant; this is the law Kepler stated for the planets, and the argument shows that it holds for every central force, not only the inverse-square one. Its algebraic content is that $L = \tfrac12[\mathbf{r},\mathbf{p}]$ is constant.

## The Reduction to One Dimension

### Polar Coordinates and the Effective Potential

With the motion planar and $L$ constant, the kinetic energy separates into radial and angular parts,

$$
T = \frac{1}{2}m\left(\dot r^2 + r^2\dot\theta^2\right) = \frac{1}{2}m\dot r^2 + \frac{L^2}{2mr^2},
$$

and the energy becomes a one-dimensional problem for the radius with the **effective potential**

$$
V_{\text{eff}}(r) = V(r) + \frac{L^2}{2mr^2} .
$$

The energy is conserved,

$$
E = \frac{1}{2}m\dot r^2 + V_{\text{eff}}(r) = \text{const},
$$

and the radial equation is

$$
m\ddot r = -V_{\text{eff}}'(r) = -V'(r) + \frac{L^2}{mr^3} .
$$

The reduction is the standard one; its role here is to display the scalar character of the central-scalar limit. After the reduction, the entire problem is a one-dimensional scalar problem in the central scalars $E$ and $L$ and the radial variable $r$. The vector directions have been exhausted by the conserved angular momentum, and the only surviving dynamical variable is a scalar.

### Binet's Equation

The orbit $r(\theta)$ is obtained from the radial equation by the substitution $u = 1/r$. With $h = L/m$ the areal law gives $\dot\theta = hu^2$, and differentiating $u$ with respect to $\theta$ rather than to $t$ converts the radial equation into **Binet's equation** for a general central force:

$$
\frac{d^2u}{d\theta^2} + u = -\frac{F(1/u)}{mh^2u^2},
$$

where $F(r)$ is the radial component of the force, positive outward. The derivation is the standard one: from $\dot r = -h\,u'$ and $\ddot r = -h^2u^2u''$ (with $u' = du/d\theta$), substituting into $m\ddot r = F(r) + L^2/(mr^3)$ and using $L^2/(mr^3) = mh^2u^3$ gives the equation above. The equation is scalar, it is second order, and its two integration constants are the eccentricity-like amplitude and the orientation of the orbit. Every central-force orbit in the limit is a solution of this one equation.

For the linear force $F(r) = -m\omega^2r$, Binet's equation becomes $u'' + u = \omega^2/(h^2u^3)$, which is nonlinear in $u$; its orbits are nevertheless closed ellipses, centred on the force centre rather than focused on it, and they are more cleanly seen in the phase plane of the second article than through Binet's equation. For the inverse-square force $F(r) = -\kappa/r^2$ the equation becomes linear,

$$
\frac{d^2u}{d\theta^2} + u = \frac{\kappa}{mh^2} = \frac{1}{p}, \qquad p = \frac{L^2}{m\kappa},
$$

with the general solution $u = 1/p + C\cos(\theta - \theta_0)$, hence $r = p/(1 + e\cos(\theta-\theta_0))$ with $e = Cp$. This is the conic section of the Kepler and Coulomb problems, and the two following articles are its development.

## The Rotation Group and the Bracket Algebra

### Rotations

The rotations of the real three-space are the adjoint actions of the unit real quaternions $R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$, acting by $\mathbf{a} \mapsto R\mathbf{a}R^{-1}$. The group is $SU(2)$, the double cover of $SO(3)$, and its Lie algebra is the three-dimensional real space $\operatorname{span}\{e_1, e_2, e_3\}$ closed under the commutator, since

$$
[e_j, e_k] = 2\epsilon_{jkl}e_l .
$$

The rotation generators are the real vector directions themselves, up to the factor of two, and this is the vector part of the material sector. The biquaternion algebra thus carries the rotation algebra in the same subspace that carries the position and momentum: the rotations and the rotated objects share the three real directions, and the rotations act on the objects by conjugation.

### The Bracket Algebra of Angular Momentum

The components of $\mathbf{L}$ satisfy the angular-momentum algebra under the Poisson bracket,

$$
\{L_i, L_j\} = \epsilon_{ijk}L_k ,
$$

which is the classical form of the commutation relations of the quantum angular momentum. The bracket is a bracket on functions of the phase-space variables $(x_k, p_k)$, with $\{x_i, p_j\} = \delta_{ij}$ and $\{x_i, x_j\} = \{p_i, p_j\} = 0$; its conventions are those of the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*.

It is important not to conflate two algebras that the notation makes look alike. The commutator $[\mathbf{a},\mathbf{b}]$ of the quaternion algebra is a product in a three-dimensional subspace and equals twice the cross product; the Poisson bracket $\{L_i, L_j\}$ is a derivative operation on the six-dimensional phase space. They produce the same three-dimensional algebra because the angular momentum is built from the cross product of the position and momentum, but they are different operations on different spaces. The algebra's commutator can be evaluated at a single instant and involves only the current vectors; the Poisson bracket relates the angular momentum to the Hamiltonian flow and requires the phase-space structure. The central-scalar limit uses both, and the companion article on the bracket treats their relation in detail.

### Numerical Checks

Several identities used above were verified by explicit computation with complex-coefficient quaternions and with numerical differentiation of phase-space functions. The quaternion product of two real vectors was confirmed to be $\mathbf{a}\mathbf{b} = -\mathbf{a}\cdot\mathbf{b}\,e_0 + \mathbf{a}\times\mathbf{b}$ and the commutator to be $[\mathbf{a},\mathbf{b}] = 2\,\mathbf{a}\times\mathbf{b}$; the vector part of $\mathbf{r}\mathbf{p}$ was confirmed to equal $\mathbf{r}\times\mathbf{p}$; the central-force criterion $[\mathbf{r},\mathbf{F}] = 0$ was confirmed to hold exactly when $\mathbf{r}\times\mathbf{F} = 0$; and the bracket $\{L_i, L_j\} = \epsilon_{ijk}L_k$ was confirmed by central-difference evaluation of the Poisson bracket at several representative phase-space points, with a maximum deviation of order $10^{-11}$. The rotation-rotor identity $R\mathbf{a}R^{-1}$ for $R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$ was confirmed to rotate a vector by the angle $\theta$ about $\hat{\mathbf{n}}$ while preserving the norm form.

## What the Limit Excludes

The central-scalar limit is a restriction, and it is worth recording exactly what is left out, because the omitted structures are the subjects of the sibling subcategories.

**Internal vectors are excluded.** An element $i\mathbf{s} \in \mathbb{M}_+$ with $\mathbf{s}$ a real vector is an internal vector degree of freedom. It would transform as a vector under rotations, it would precess under torques, and its coupling to the orbital motion would produce the spin-orbit and magnetic phenomena. The limit sets it to zero. This is the spin-zero restriction, and it is why the effects of this subcategory carry no intrinsic magnetism.

**Noncentral scalars are excluded.** A potential that is a scalar but not central, or a scalar that depends on direction, would break the rotation invariance and would not be a central scalar. Such terms belong to the generalities of the framework rather than to the central-force problems.

**Noncentral vector couplings are excluded.** A force with a component perpendicular to the position — a velocity-dependent force, a magnetic-type force $q\mathbf{v}\times\mathbf{B}$, or a torque that changes the direction of an internal vector — is not covered. The magnetic and multipole effects are exactly these couplings, and they belong to the sibling subcategories on intrinsic magnetism and higher multipoles.

**The general formulation is not repeated.** The Lagrangian and Hamiltonian formalisms, the action principle and the symplectic form belong to the subcategory of generalities; the central-scalar limit uses the equations of motion directly and cites the bracket article for the phase-space conventions. Nothing in the present article depends on the general formalism beyond the Poisson bracket $\{x_i,p_j\} = \delta_{ij}$.

## Summary

The central-scalar limit of classical mechanics is the restriction of the biquaternion framework in which the scalar quantities of a problem are central scalars — real multiples of $e_0$, hence Hermitian and in $\mathbb{M}_+$ — and the configuration quantities are real vectors in the three-space $\operatorname{span}\{e_1, e_2, e_3\} \subset \mathbb{M}_-$. The non-relativistic configuration space is the direct sum $ie_0\mathbb{R} \oplus \operatorname{span}\{e_1,e_2,e_3\}$, and no vector direction of $\mathbb{M}_+$ is occupied; this last condition is the spin-zero restriction.

A central force is defined by $\mathbf{F} \parallel \mathbf{r}$, equivalently $[\mathbf{r}, \mathbf{F}] = 0$, equivalently $\mathbf{F}\mathbf{r}$ central. The angular momentum is the commutator and the vector part of the product,

$$
\mathbf{L} = \mathbf{r}\times\mathbf{p} = \tfrac12[\mathbf{r},\mathbf{p}], \qquad \mathbf{r}\mathbf{p} = -\mathbf{r}\cdot\mathbf{p}\,e_0 + \mathbf{L} ,
$$

and the conservation law is a two-line computation,

$$
\dot{\mathbf{L}} = \tfrac12[\mathbf{r},\mathbf{F}] = 0 \;\Longleftrightarrow\; \mathbf{F}\text{ central}.
$$

The conservation of angular momentum is therefore identical with the centrality of the force, and both are statements that the position and the force commute as quaternions.

A central force gives planar motion, the areal law $\dot A = L/(2m)$, the reduction to the radial problem with effective potential $V_{\text{eff}} = V(r) + L^2/(2mr^2)$, and Binet's equation

$$
u'' + u = -\frac{F(1/u)}{mh^2u^2}, \qquad u = \frac{1}{r}, \quad h = \frac{L}{m},
$$

whose inverse-square solution is the conic section $r = p/(1 + e\cos(\theta-\theta_0))$ with $p = L^2/(m\kappa)$.

The rotations are the unit real quaternions acting by $\mathbf{a} \mapsto R\mathbf{a}R^{-1}$, with Lie algebra $[e_j,e_k] = 2\epsilon_{jkl}e_l$ in the real three-space; the components of $\mathbf{L}$ satisfy $\{L_i,L_j\} = \epsilon_{ijk}L_k$ under the Poisson bracket, which is a phase-space operation and is not the quaternion commutator. The limit excludes internal vectors (spin), noncentral scalars, and noncentral vector couplings; those structures are the subjects of the sibling subcategories.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -e_0$; $i\mathbb{M}_\pm = \mathbb{M}_\mp$ |
| $\mathbb{M}_-$ | Anti-Hermitian (material) sector |
| $\mathbb{M}_+$ | Hermitian (informational) sector |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subalgebra; unit elements are rotation rotors |
| $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$ | Centre |
| $ie_0\mathbb{R} \oplus \operatorname{span}\{e_1,e_2,e_3\}$ | Non-relativistic configuration space in $\mathbb{M}_-$ |
| $\mathbf{r}, \mathbf{p}, \mathbf{F}$ | Position, momentum, force: real vectors in $\operatorname{span}\{e_1,e_2,e_3\}$ |
| $m e_0$, $E e_0$, $V(r)e_0$ | Mass, energy, potential: central scalars in $\mathbb{M}_+$ |
| $\mathbf{a}\mathbf{b} = -\mathbf{a}\cdot\mathbf{b}\,e_0 + \mathbf{a}\times\mathbf{b}$ | Quaternion product of two real vectors |
| $[\mathbf{a},\mathbf{b}] = 2\,\mathbf{a}\times\mathbf{b}$ | Commutator of two real vectors |
| $\mathbf{L} = \mathbf{r}\times\mathbf{p} = \tfrac12[\mathbf{r},\mathbf{p}]$ | Angular momentum; vector part of $\mathbf{r}\mathbf{p}$ |
| $\dot{\mathbf{L}} = \tfrac12[\mathbf{r},\mathbf{F}]$ | Torque; vanishes iff the force is central |
| $r, \theta$; $h = L/m$ | Polar coordinates; areal constant |
| $V_{\text{eff}} = V(r) + L^2/(2mr^2)$ | Effective potential |
| $u = 1/r$ | Binet variable |
| $u'' + u = -F(1/u)/(mh^2u^2)$ | Binet's equation for a central force |
| $R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$ | Rotation rotor; $\mathbf{a}\mapsto R\mathbf{a}R^{-1}$ |
| $[e_j,e_k] = 2\epsilon_{jkl}e_l$ | Rotation algebra in the real three-space |
| $\{L_i,L_j\} = \epsilon_{ijk}L_k$ | Poisson-bracket angular-momentum algebra |
| $\{x_i,p_j\} = \delta_{ij}$ | Canonical Poisson brackets |

## Further Reading

- Isaac Newton, *Philosophiae Naturalis Principia Mathematica* (1687), for the inverse-square force and the areal law.
- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics* (Pearson, 2002), for central forces, effective potentials and Binet's equation.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the reduction of central-force motion and the areal law.
- E. T. Whittaker, *A Treatise on the Analytical Dynamics of Particles and Rigid Bodies* (Cambridge, 1937), for Binet's equation and the integration of central-force orbits.
- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for the Poisson bracket and the phase-space formulation of angular momentum.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the quaternion product of vectors and the geometric-algebra treatment of central motion.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the real subspaces of the biquaternion algebra and their commutator structure.
