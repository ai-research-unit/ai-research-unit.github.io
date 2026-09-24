# __The Dirac Equation in Biquaternionic Form__

## Introduction

The Dirac equation is the relativistic wave equation for spin-$\frac{1}{2}$ particles. It was discovered by Paul Dirac in 1928 as an attempt to reconcile quantum mechanics with special relativity, and it predicted the existence of antimatter. It is one of the foundational equations of quantum field theory, and it is the equation that governs electrons, quarks, and all fermions.

The Dirac equation is usually written in terms of the **gamma matrices** $\gamma^\mu$, which satisfy the anticommutation relations

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2g^{\mu\nu} I,
$$

where $g^{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ is the Clifford metric of the generators and $I$ is the identity matrix. The gamma matrices generate the Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$, and the Dirac equation is the statement that the Dirac operator $\not\partial = \gamma^\mu \partial_\mu$ annihilates the spinor field.

This article develops the biquaternionic formulation of the Dirac equation. The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as a real algebra, to the **even subalgebra** of the Clifford algebra $\mathrm{Cl}_{1,3}$, and the biquaternionic gradient $\tilde{\nabla}$ plays the role of the Dirac operator. The Dirac equation in biquaternionic form is therefore a first-order equation on the biquaternion algebra.

The article is organized as follows. First the standard Dirac equation is reviewed, then the biquaternion algebra and its relation to $\mathrm{Cl}_{1,3}$ are recalled, then the biquaternionic Dirac operator is defined, and finally the biquaternionic Dirac equation is stated and solved. The article closes with the relativistic kinematics (four-velocity, four-momentum, mass-shell relation), the relation to the Maxwell equation, the plane-wave solutions, and the mass term.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0 \partial_{ict} + e_1 \partial_x + e_2 \partial_y + e_3 \partial_z$. The Minkowski metric has signature $(-,+,+,+)$, so that $\partial_{ict}^2 = -\partial_t^2/c^2$. Throughout this article, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $v$ is reserved for particle and frame velocities.

## The Standard Dirac Equation

### The Gamma Matrices

The **gamma matrices** $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ are $4\times 4$ complex matrices satisfying the anticommutation relations

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2g^{\mu\nu} I_4,
$$

where $g^{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ is the Clifford metric of the generators and $I_4$ is the $4\times 4$ identity. They generate the Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$, which has real dimension $16$; in standard counting $\mathrm{Cl}_{p,q}$ carries $p$ generators squaring to $+1$ and $q$ squaring to $-1$, so $(\gamma^0)^2 = +I_4$, $(\gamma^k)^2 = -I_4$, and $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$. The metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ of the $ict$ gradient is a separate object and is unchanged; the two differ by the sign of the generators' square.

In the **Dirac representation**, the gamma matrices are

$$
\gamma^0 = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & \sigma^k \\ -\sigma^k & 0 \end{pmatrix}, \quad k = 1, 2, 3,
$$

where $\sigma^k$ are the Pauli matrices. These are the usual **mostly-minus** Dirac representation, and they satisfy the metric declared above: $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$, so squaring reproduces $(\gamma^\mu)^2 = g^{\mu\mu} I_4$ and the anticommutation relation holds as stated.

### The Dirac Equation

The **Dirac equation** for a free fermion of mass $m$ is

$$
(i\not\partial - m)\psi = 0,
$$

where $\not\partial = \gamma^\mu \partial_\mu$ is the **Dirac operator**, $\psi$ is a four-component complex **Dirac spinor**, and $m$ is the mass. With the mostly-minus generators the factor of $i$ is explicit, as in the standard treatment; in natural units $\hbar = c = 1$ the equation is

$$
(i\gamma^\mu \partial_\mu - m)\psi = 0.
$$

For a massless fermion ($m = 0$), the equation reduces to

$$
i\not\partial\psi = 0.
$$

Squaring the Dirac operator gives the Klein–Gordon operator:

$$
(i\not\partial)^2 = -\not\partial^2 = -g^{\mu\nu}\partial_\mu\partial_\nu = \eta^{\mu\nu}\partial_\mu\partial_\nu = \Box,
$$

where $\Box = \eta^{\mu\nu} \partial_\mu \partial_\nu = -\partial_t^2/c^2 + \Delta$ is the d'Alembertian, with $\eta = -g$ the $ict$ metric of the material sector. So every solution of the massless Dirac equation is a solution of the wave equation.

### Spinors and the Lorentz Group

The Dirac spinor $\psi$ is not a vector under the Lorentz group; it transforms in the **spinor representation** of the Lorentz group. The spinor representation is a double cover of the vector representation: a rotation by $2\pi$ in the vector representation corresponds to a rotation by $2\pi$ in the spinor representation, but a rotation by $4\pi$ is the identity in the spinor representation, not $2\pi$.

The spinor representation is two-dimensional over $\mathbb{C}$ (for the **Weyl spinor**), and the Dirac spinor is a pair of Weyl spinors:

$$
\psi = \begin{pmatrix} \psi_L \\ \psi_R \end{pmatrix},
$$

where $\psi_L$ and $\psi_R$ are the left- and right-handed Weyl spinors. The Dirac equation couples $\psi_L$ and $\psi_R$ through the mass term.

## The Biquaternion Algebra and $\mathrm{Cl}_{1,3}$

### The Isomorphism

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as a **real algebra**, to the **even subalgebra** $\mathrm{Cl}_{1,3}^+$ of the real Clifford algebra $\mathrm{Cl}_{1,3}$. The even subalgebra consists of products of an even number of gamma matrices: the identity $I$, the six bivectors $\gamma^\mu\gamma^\nu$ with $\mu < \nu$, and the pseudoscalar $\gamma^0\gamma^1\gamma^2\gamma^3$. It has real dimension $8$, matching the real dimension of $\mathbb{B}$.

**A note on the convention.** It is important to keep two things distinct. The biquaternion algebra $\mathbb{B}$ is a **real algebra of dimension 8**, and it is the even part of the **real** Clifford algebra. It is **not** the even part of the **complexified** Clifford algebra $\mathbb{C}\otimes \mathrm{Cl}_{1,3}$, which has complex dimension 8 (real dimension 16) and is isomorphic to $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$.

**The isomorphism.** The bivectors of $\mathrm{Cl}_{1,3}^+$ span a 6-dimensional real space. Three of them are timelike-spacelike, $\gamma^0\gamma^k$, and have square $+I$. Three are spacelike-spacelike, $\gamma^j\gamma^k$ with $j,k \in \{1,2,3\}$, and have square $-I$. The three spacelike bivectors generate a copy of the quaternions $\mathbb{H}$ inside $\mathrm{Cl}_{1,3}^+$. The isomorphism is given by mapping the quaternion units to three mutually anticommuting spacelike bivectors, oriented so that $e_1 e_2 = e_3$. Concretely, one valid assignment is

$$
e_1 \mapsto \gamma^2\gamma^3, \qquad e_2 \mapsto \gamma^3\gamma^1, \qquad e_3 \mapsto \gamma^1\gamma^2.
$$

The choice of which bivector corresponds to which quaternion unit is a convention; different choices are related by rotations of the spatial frame. With the mostly-minus generators the three signs can be taken positive simultaneously, since $(\gamma^2\gamma^3)(\gamma^3\gamma^1) = \gamma^1\gamma^2$ and $e_1e_2 = e_3$; under the opposite sign of the metric that is impossible, and one of the three bivectors must be reversed.

The scalar imaginary $i$ of $\mathbb{B}$ corresponds to the pseudoscalar $\gamma^0\gamma^1\gamma^2\gamma^3$ of $\mathrm{Cl}_{1,3}$, up to a sign. This correspondence is what makes the complexification of the quaternions inside $\mathbb{B}$ match the complexification of the even Clifford algebra.

### The Gamma Matrices from the Biquaternion Units

The biquaternion units give an explicit set of gamma matrices. Write the biquaternion algebra as $M_2(\mathbb{C})$ by $e_0 \mapsto I_2$, $e_k \mapsto -i\sigma^k$, $i \mapsto iI_2$, so that $ie_k \leftrightarrow \sigma^k$, and arrange the units in $2 \times 2$ blocks:

$$
\gamma^0 = \begin{pmatrix} 0 & e_0 \\ e_0 & 0 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & i e_k \\ -i e_k & 0 \end{pmatrix}, \qquad k = 1,2,3 ,
$$

that is, $\gamma^0 = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix}$ and $\gamma^k = \begin{pmatrix} 0 & \sigma^k \\ -\sigma^k & 0 \end{pmatrix}$. The Clifford relations are then the quaternion relations in disguise. From the multiplication table and $i^2 = -1$, $e_k^2 = -e_0$,

$$
(\gamma^0)^2 = e_0^2 = +I_4, \qquad (\gamma^k)^2 = (ie_k)(-ie_k) = -i^2 e_k^2 = -I_4 .
$$

The mixed products are block diagonal: $\gamma^0\gamma^k = \mathrm{diag}(-ie_k,\, ie_k)$ and $\gamma^k\gamma^0 = -\gamma^0\gamma^k$, while $\gamma^j\gamma^k = \mathrm{diag}(e_je_k,\, e_je_k)$ and $\gamma^k\gamma^j = -\, \gamma^j\gamma^k$ because $e_je_k = -e_ke_j$. Hence

$$
\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu} I_4, \qquad g = \mathrm{diag}(+1,-1,-1,-1),
$$

and the verification uses nothing beyond the quaternion multiplication table and $i^2 = -1$. This is the declared metric of the introduction and of the section above. The overall sign of the metric is a convention: replacing every generator by $i\gamma^\mu$ flips the sign of $g$ and leaves the Clifford algebra unchanged, so the mostly-plus set is $i$ times the set displayed here.

### The Dirac Operator in Biquaternion Form

The biquaternionic gradient

$$
\tilde{\nabla} = e_0 \partial_{ict} + e_1 \partial_x + e_2 \partial_y + e_3 \partial_z
$$

is the biquaternion form of the Dirac operator. The correspondence with the gamma-matrix Dirac operator $\not\partial = \gamma^\mu \partial_\mu$ is through the isomorphism $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$: the biquaternion units $e_k$ correspond to spacelike bivectors, and the scalar unit $e_0$ corresponds to the identity $I$.

The biquaternionic gradient satisfies the factorization

$$
\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Box,
$$

which is the biquaternion form of the factorization $\not\partial^2 = \Box$. The two factorizations use the same algebraic relation between the basis elements and the metric.

### The Difference from the Matrix Form

The matrix Dirac operator $\not\partial$ acts on four-component complex spinors (the Dirac spinors), while the biquaternionic gradient $\tilde{\nabla}$ acts on biquaternions. The two formulations are related by the isomorphism

$$
\mathrm{Cl}_{1,3} \cong M_4(\mathbb{C}),
$$

under which the even subalgebra $\mathrm{Cl}_{1,3}^+$ corresponds to a subalgebra of $M_4(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$. The biquaternion algebra $\mathbb{B}$ is then isomorphic to $M_2(\mathbb{C})$ (article 5), and the action of $\tilde{\nabla}$ on the biquaternion algebra corresponds to the action of $\not\partial$ on a two-dimensional complex spinor module.

So the biquaternion formulation of the Dirac equation is expressed in terms of the biquaternion algebra, whose elements can be viewed as **pairs of two-component Weyl spinors**. The full four-component Dirac spinor is recovered by taking the direct sum of the two-component spinor module with its complex conjugate.

### Chirality and the Gamma-Five Operator

The volume element $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ of the Clifford algebra is minus the image of the biquaternion scalar imaginary, $\Phi(i) = -\omega$, and satisfies $\omega^2 = -1$. The chirality operator is

$$
\gamma_5 = i\,\omega = i\,\gamma^0\gamma^1\gamma^2\gamma^3, \qquad \gamma_5^2 = i^2 \omega^2 = (-1)(-1) = 1 .
$$

It anticommutes with every generator, $\gamma_5\gamma^\mu = -\gamma^\mu\gamma_5$, and therefore commutes with every even element, the biquaternion algebra among them. In the block representation of the preceding subsection it is diagonal,

$$
\gamma_5 = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2 \end{pmatrix},
$$

acting as $-1$ on the upper two-component block and $+1$ on the lower. Since $\gamma_5^2 = 1$, the Dirac spinor space splits into its eigenspaces,

$$
\mathbb{C}^4 = \Delta_+\oplus\Delta_-, \qquad \Delta_\pm = \{\psi : \gamma_5\psi = \pm\psi\}, \qquad P_\pm = \tfrac12(1\pm\gamma_5),
$$

each of complex dimension two; the elements of $\Delta_\pm$ are the Weyl spinors of the preceding section, left- and right-handed up to the labelling convention for the sign. Correspondingly the central idempotents $\tfrac12(1\pm i\omega)$ split the complexified even algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathrm{Cl}_{1,3}^+ \cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, which is the algebraic form of the same decomposition. The $i$ in $\gamma_5$ and in the projectors is the scalar imaginary of the complexified Clifford algebra; the biquaternion imaginary is the element whose image under $\Phi$ is $\omega$ itself.

## Relativistic Kinematics in Biquaternionic Form

Before developing the biquaternionic Dirac equation, it is useful to collect the basic relativistic kinematic quantities in biquaternion form. These are the objects that appear in the Dirac equation and its solutions, and they are established physics rewritten in biquaternion notation.

### The Four-Position

The **four-position biquaternion** is

$$
\tilde{X} = ic t\, e_0 + x\, e_1 + y\, e_2 + z\, e_3,
$$

with $x_0 = ict$. The scalar part is the complex time coordinate, and the vector part is the ordinary spatial position.

### The Invariant Interval

The invariant interval is the square of the biquaternion displacement:

$$
ds^2 = N(d\tilde{X}) = d\tilde{X} \circ \overline{d\tilde{X}} = (ic\,dt)^2 + dx^2 + dy^2 + dz^2 = -c^2 dt^2 + d\mathbf{x}^2.
$$

This is the biquaternion form of the Minkowski interval. The Lorentzian signature emerges algebraically from $i^2 = -1$, as discussed in the companion article on the $ict$ convention.

### The Four-Velocity

The **four-velocity biquaternion** is

$$
\tilde{U} = \gamma(ic\, e_0 + \mathbf{v}),
$$

where $\mathbf{v}$ is the ordinary three-velocity of the particle and

$$
\gamma = \frac{1}{\sqrt{1 - \mathbf{v}^2/c^2}}
$$

is the Lorentz factor. The four-velocity satisfies the **normalization condition**

$$
\tilde{U}\bar{\tilde{U}} = \gamma^2\big(-c^2 + \mathbf{v}^2\big) = -c^2.
$$

This is the biquaternion form of the standard relativistic normalization $u^\mu u_\mu = -c^2$.

### The Four-Momentum

The **four-momentum biquaternion** is

$$
\tilde{P} = m\tilde{U} = \gamma m(ic\, e_0 + \mathbf{v}) = i\,\frac{E}{c}\, e_0 + \mathbf{p},
$$

where $E = \gamma m c^2$ is the relativistic energy and $\mathbf{p} = \gamma m\mathbf{v}$ is the relativistic three-momentum. The scalar part of $\tilde{P}$ is $iE/c$, and the vector part is $\mathbf{p}$.

The four-momentum satisfies the **mass-shell relation**

$$
\tilde{P}\bar{\tilde{P}} = m^2 \tilde{U}\bar{\tilde{U}} = -m^2 c^2.
$$

This is the biquaternion form of the standard relativistic energy-momentum relation

$$
E^2 = \mathbf{p}^2 c^2 + m^2 c^4,
$$

which is obtained by expanding $-m^2 c^2 = -(E/c)^2 + \mathbf{p}^2$.

### The Four-Acceleration and Four-Force

The **four-acceleration biquaternion** is $\tilde{A} = d\tilde{U}/d\tau$, where $\tau$ is the proper time. The **four-force biquaternion** is $\tilde{F} = d\tilde{P}/d\tau = m\tilde{A}$. The four-acceleration satisfies $\tilde{A}\bar{\tilde{U}} + \tilde{U}\bar{\tilde{A}} = 0$, which is the biquaternion form of the orthogonality condition $a^\mu u_\mu = 0$.

### Summary of Relativistic Kinematics

| Quantity | Biquaternion | Constraint |
|---|---|---|
| Four-position | $\tilde{X} = ict\, e_0 + \mathbf{x}$ | — |
| Interval | $ds^2 = N(d\tilde{X}) = d\tilde{X}\circ\overline{d\tilde{X}}$ | $= -c^2 dt^2 + d\mathbf{x}^2$ |
| Four-velocity | $\tilde{U} = \gamma(ic\, e_0 + \mathbf{v})$ | $\tilde{U}\bar{\tilde{U}} = -c^2$ |
| Four-momentum | $\tilde{P} = m\tilde{U}$ | $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$ |
| Four-force | $\tilde{F} = d\tilde{P}/d\tau$ | — |

These kinematic relations are the biquaternion form of standard relativistic mechanics, and they are the natural setting for the biquaternionic Dirac equation.

## The Biquaternionic Dirac Equation

### Statement

Let $\tilde{\Psi}$ be a biquaternion-valued field, and let $\tilde{\nabla}$ be the biquaternionic gradient. The **biquaternionic Dirac equation** for a massless field is

$$
\tilde{\nabla}\tilde{\Psi} = 0.
$$

For a field of mass $m$ the equation is **linear** in $\tilde{\Psi}$ and **off-diagonal in chirality**. Writing the field as a pair of chiral components, $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$, the massive equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$
<!-- CONVENTION — the massive equation, canonical form. This linear, chirality-off-diagonal pair IS the biquaternionic Dirac equation for m ≠ 0; the derived articles state it in this orientation (∇̃ acting on Ψ_R, ∇̄̃ on Ψ_L), and this article is its definitional home. Two standing facts. (i) The mass term is LINEAR: the continuous central phase (fermion number) passes through it, so the vector U(1) is exact for the massive field, and what the mass breaks is the AXIAL symmetry, ∂_μ j_5^μ = 2im Ψ̄γ_5Ψ. (ii) It is NOT the antilinear single-field equation ∇̃Ψ = mΨ♭: that belongs to the algebra's real structure ♭ and is a different equation (see the remark on ♭ in The Massive Case). Do not restore mΨ♭ as the mass term. -->

Applying $\bar{\tilde{\nabla}}$ to the first equation and using the second, together with $\bar{\tilde{\nabla}}\tilde{\nabla} = \Box$, gives $\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R$, and likewise for $\tilde{\Psi}_L$; the pair therefore implies the Klein–Gordon equation for each chirality. On the spinor module the same statement is the matrix equation $(\not\partial - m)\psi = 0$ of the first section, with $\psi = (\psi_L, \psi_R)$ the pair of Weyl spinors.

The mass term is the term that breaks the exact correspondence between the biquaternionic Dirac equation and the biquaternionic Maxwell equation. It is linear in the field, the biquaternion transcription of the mass term $m\psi$ of the matrix Dirac equation.

### The Massless Case

The massless biquaternionic Dirac equation $\tilde{\nabla}\tilde{\Psi} = 0$ is identical in form to the **homogeneous biquaternion Maxwell equation** for the field-strength biquaternion $\tilde{F}$. The two equations have the same form:

$$
\tilde{\nabla}\tilde{\Psi} = 0 \quad \text{(massless Dirac)}, \qquad \tilde{\nabla}\tilde{F} = 0 \quad \text{(source-free Maxwell)}.
$$

The solutions are also the same in form: the kernel of the biquaternionic gradient consists of plane waves, spherical waves, and cylindrical waves (as in the companion article on Maxwell). The physical interpretation differs: $\tilde{\Psi}$ is a fermion field (spin-$\frac{1}{2}$), and $\tilde{F}$ is a boson field (spin-1).

The structural identity of the two equations is the algebraic content of the statement that the biquaternion algebra is the same for both. The difference is not in the operator but in the representation: the Maxwell field-strength biquaternion lives in the vector part of the algebra, and the Dirac biquaternion lives in the full algebra (with the two-component structure that corresponds to the pair of Weyl spinors).

### The Massive Case

The massive biquaternionic Dirac equation is the chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

The mass term is **linear** in the field and **off-diagonal** between the two chiralities: it is the biquaternion transcription of the mass term $m\psi$ of the matrix Dirac equation, and it is what couples the left- and right-handed Weyl spinors.

The coupling has to be off-diagonal. Left multiplication by an element of $\mathbb{B}$ *preserves* each chiral component — the minimal left ideals of $\mathbb{B} \cong M_2(\mathbb{C})$ are the two chiralities, and left multiplication maps each into itself — so no combination of the form $a\tilde{\Psi}_L + b\tilde{\Psi}_R$ relates them. A mass term that couples the chiralities therefore has to act as a *right* multiplication, which is what the pair above does; equivalently, on the strict spinor module (a single minimal left ideal) the mass is simply linear. This is the structural reason why the spinor module, and not the whole algebra, is the natural carrier of the Dirac field.

**A remark on the anti-Hermitian conjugation $\flat$.** The algebra carries, besides the quaternion conjugate and the Hermitian conjugation $\dagger$, a further antilinear involution:

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger = -\bar{\tilde{\Psi}}^{\,*},
$$

the **anti-Hermitian conjugate** $\flat = -\dagger$. It is a $\mathbb{C}$-**antilinear** involution, and it is order-reversing with a twist,

$$
\left(\tilde{A}\tilde{B}\right)^\flat = -\,\tilde{B}^\flat\tilde{A}^\flat ,
$$

the sign being the only difference from an ordinary anti-automorphism, and it acts by a sign on the two Hermitian sectors,

$$
\tilde{\Psi}^\flat = +\tilde{\Psi}\ \ (\tilde{\Psi}\in\mathbb{M}_-), \qquad \tilde{\Psi}^\flat = -\tilde{\Psi}\ \ (\tilde{\Psi}\in\mathbb{M}_+),
$$

so that the **fixed space of $\flat$ is the anti-Hermitian sector $\mathbb{M}_-$**.

The convention is worth a remark, because the more familiar one takes the *Hermitian* part as the real one, and here the *anti*-Hermitian part plays that role. The two differ only by the central factor $i$: anti-Hermitian elements are $i$ times Hermitian ones, and anti-Hermitian generators are the standard choice for the Lie algebra of a unitary group (in the companion quantum article the Lie algebra of the unitary group is $\mathbb{M}_-$). What is unusual here is not the sign convention as such, but that it is applied to the *field* rather than to the generators: it is $\mathbb{M}_-$ that is fixed, and that is what makes $\mathbb{M}_-$ the framework's "material" sector (the companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* takes $\mathbb{M}_-$ as the fixed space of $\flat$).

The map $\flat$ is the algebra's **real structure**, and its shape is that of a charge-conjugation (Majorana) pairing: it relates the field to its own conjugate. It is *not* the mass term. A coupling built on $\flat$ pairs $\tilde{\Psi}$ with $\tilde{\Psi}^\flat$ rather than relating two independent chiralities, and because $\flat$ is antilinear such a coupling is not invariant under the continuous central phase — precisely the two differences between a Majorana-type pairing and an ordinary Dirac mass. The single-field equation $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ is a real-linear equation of that type; it is a different equation from the one studied here, and its central-phase plane waves sit on the *spacelike* locus, not on the physical mass shell. The map $\flat$ is retained in the framework for what it is genuinely for — conjugation, the $\mathbb{M}_\pm$ split, the trace and bilinear pairings, and the real-form question of Dirac versus Majorana fermions, which the companion articles on chirality, the neutrino, and the CPT theorem develop. In the present article $\flat$ is used only for conjugation, never as the mass.
<!-- CONVENTION — verified, do not "fix". The claim that the antilinear companion ∇̃Ψ = mΨ♭ has its central-phase plane waves on the SPACELIKE locus is deliberate and was re-derived independently (pure real arithmetic, no libraries): the two-frequency system for a single-mode field has nullity 0 on the timelike shell k₀² = k² + m² and nullity 4 on the spacelike shell k² = k₀² + m². So the spacelike dispersion is a property of that equation, not a typo, and it is exactly why that equation is not the Dirac equation and was retired as the mass term. Do not relocate it to the physical mass shell. -->

**The associated Klein–Gordon equation.** Applying $\bar{\tilde{\nabla}}$ to the first of the pair and substituting the second gives

$$
\bar{\tilde{\nabla}}\tilde{\nabla}\tilde{\Psi}_R = \Box\tilde{\Psi}_R = m\,\bar{\tilde{\nabla}}\tilde{\Psi}_L = m^2\tilde{\Psi}_R ,
$$

and likewise for $\tilde{\Psi}_L$, so each chiral component satisfies the **Klein–Gordon equation**

$$
\left(\Box - m^2c^2/\hbar^2\right)\tilde{\Psi} = 0 ,
$$

in agreement with the companion article on the Klein–Gordon equation, whose operator is $\Box - m^2c^2/\hbar^2$. This is the biquaternion form of the standard statement that the square of the Dirac operator is the Klein–Gordon operator, $(\not\partial + m)(\not\partial - m) = \Box - m^2$.

## Plane-Wave Solutions

### The Massless Case

Plane-wave solutions of the massless biquaternionic Dirac equation are

$$
\tilde{\Psi}(\tilde{X}) = \tilde{\Psi}_0 \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{k}\bar{\tilde{X}}\right)\right)
= \tilde{\Psi}_0\,e^{\,i(\mathbf{k}\cdot\mathbf{x}-\omega t)},
$$

where $\tilde{\Psi}_0 \in \mathbb{B}$ is a constant biquaternion, $\tilde{k} = i k_0 e_0 + e_1 k_1 + e_2 k_2 + e_3 k_3$ (with $k_0 = \omega/c$) is the wave biquaternion, and $\tilde{X} = e_0 (ict) + e_1 x + e_2 y + e_3 z$ is the four-position biquaternion. The scalar part $\mathrm{Sc}(\tilde{k}\bar{\tilde{X}}) = \mathbf{k}\cdot\mathbf{x} - \omega t$ is real, so the exponent $i\,\mathrm{Sc}(\tilde{k}\bar{\tilde{X}})$ is a purely imaginary central element; the exponential therefore commutes with $\tilde{\Psi}_0$ and differentiates to left multiplication by $i\tilde{k}$,

$$
\tilde{\nabla}\tilde{\Psi} = i\,\tilde{k}\,\tilde{\Psi},
$$

so the equation $\tilde{\nabla}\tilde{\Psi} = 0$ becomes

$$
\tilde{k}\tilde{\Psi}_0 = 0,
$$

i.e., the polarization biquaternion $\tilde{\Psi}_0$ is annihilated by the wave biquaternion $\tilde{k}$. This is the biquaternion form of the **Weyl equation** $\not k\psi_0 = 0$.

Nonzero solutions of $\tilde{k}\tilde{\Psi}_0 = 0$ exist only when $\tilde{k}$ is a zero divisor in $\mathbb{B}$, that is, when $\tilde{k}$ is null: $\tilde{k}\bar{\tilde{k}} = 0$, equivalently $k_0^2 = \|\mathbf{k}\|^2$, the massless dispersion relation. In that case the kernel is a two-dimensional complex vector space, corresponding to the two spin states of a massless fermion; for non-null $\tilde{k}$ the kernel is trivial. This matches the two-component structure of the Weyl spinor.

### The Massive Case

For the massive equation a single central-phase plane wave,

$$
\tilde{\Psi}(\tilde{X}) = \tilde{\Psi}_0 \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{k}\bar{\tilde{X}}\right)\right) = \tilde{\Psi}_0\,e^{i\theta}, \qquad \theta = \mathbf{k}\cdot\mathbf{x} - \omega t,
$$

does solve the pair, with one polarization biquaternion per chirality, $\tilde{\Psi}_0 = \tilde{\Psi}_0^L + \tilde{\Psi}_0^R$. Differentiating as in the massless case, $\tilde{\nabla}$ acts on $e^{i\theta}$ as left multiplication by $i\tilde{k}$ and $\bar{\tilde{\nabla}}$ acts on it as left multiplication by $i\bar{\tilde{k}}$, so the chiral pair becomes the momentum-space system

$$
i\tilde{k}\tilde{\Psi}_0^R = m\tilde{\Psi}_0^L, \qquad i\bar{\tilde{k}}\tilde{\Psi}_0^L = m\tilde{\Psi}_0^R .
$$

Eliminating $\tilde{\Psi}_0^L$ gives

$$
\tilde{k}\bar{\tilde{k}}\,\tilde{\Psi}_0^R = -m^2\,\tilde{\Psi}_0^R ,
$$

so a nonzero solution requires the **mass-shell condition**

$$
\tilde{k}\bar{\tilde{k}} = -m^2 c^2/\hbar^2,
$$

i.e., $-k_0^2 + \|\mathbf{k}\|^2 = -m^2 c^2/\hbar^2$, which is the standard mass-shell relation $k_0^2 = \|\mathbf{k}\|^2 + m^2 c^2/\hbar^2$ (with $k_0 = E/\hbar c$). This is the biquaternion form of the standard relativistic energy-momentum relation $E^2 = \mathbf{p}^2 c^2 + m^2 c^4$ (with $\mathbf{p} = \hbar\mathbf{k}$), the same shell as the four-momentum kinematics of the preceding section. The two signs of $k_0$ are the two frequency branches — the particle and the antiparticle — and with the two spin states they give the four components of the Dirac spinor.

## Spherical and Cylindrical Solutions

### Spherical Solutions

Spherical solutions of the biquaternionic Dirac equation can be constructed by the methods of Clifford analysis, adapted to the biquaternion algebra. The standard technique is the **monogenic completion** of scalar harmonic functions: given a harmonic scalar function on the sphere, the monogenic completion produces a biquaternion-valued function that lies in the kernel of the Dirac operator.

The construction is more involved than the corresponding construction for the Maxwell equation, because $\tilde{\nabla}$ is not the operator whose square is the scalar wave operator. One has

$$
\tilde{\nabla}^2 = \partial_{ict}^2 - \Delta + 2\,\partial_{ict}\boldsymbol{\nabla},
\qquad \boldsymbol{\nabla} = e_1\partial_x + e_2\partial_y + e_3\partial_z,
$$

whose first-order cross term does not vanish, so $\tilde{\nabla}^2 \neq \Box = \partial_{ict}^2 + \Delta$. It is the **conjugate** gradient that squares to the d'Alembertian, $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$, so the completion operator is $\bar{\tilde{\nabla}}$: for every harmonic scalar function $\psi$ with $\Box\psi = 0$, the function $\bar{\tilde{\nabla}}\psi$ satisfies

$$
\tilde{\nabla}\left(\bar{\tilde{\nabla}}\psi\right) = \Box\psi = 0
$$

and is a solution of the massless Dirac equation. This is the biquaternion form of the monogenic completion of the scalar harmonic functions, and it is the reason the spherical solutions are indexed by the scalar spherical harmonics.

For the massless case, the spherical solutions of the biquaternionic Dirac equation are the **monogenic spherical harmonics**, and they form a basis of the solution space. For the massive case, the construction is more involved: the solution is a combination of the monogenic spherical harmonics and their anti-Hermitian conjugates, with coefficients determined by the mass-shell condition.

The spherical solutions describe the **angular momentum states** of a relativistic fermion. The quantum numbers $(n, \ell, m)$ correspond to the radial, orbital, and magnetic quantum numbers of the standard hydrogen-like Dirac equation.

### Cylindrical Solutions

Cylindrical solutions are similarly constructed from cylindrical harmonics by the same monogenic completion technique. They describe **waveguide modes** of a fermion field in a cylindrical geometry, with the transverse-electric and transverse-magnetic modes corresponding to the two spin states.

## Relation to the Maxwell Equation

### Structural Identity

The massless biquaternionic Dirac equation and the homogeneous biquaternion Maxwell equation have the same form:

$$
\tilde{\nabla}\tilde{\Psi} = 0.
$$

The difference is the interpretation of the field $\tilde{\Psi}$:

- In the Maxwell case, $\tilde{\Psi}$ is the field-strength biquaternion $\tilde{F}$, which lives in the vector part of the algebra and describes the electromagnetic field.
- In the Dirac case, $\tilde{\Psi}$ is the fermion field, which lives in the full algebra and describes the spin-$\frac{1}{2}$ particle.

The structural identity is the algebraic content of the statement that both the photon and the electron are described by the same Clifford algebra $\mathrm{Cl}_{1,3}$. The two fields differ in the **representation** of the algebra: the photon field lives in the vector representation (spin-1), and the electron field lives in the spinor representation (spin-$\frac{1}{2}$).

### The Mass Term

The **mass term** is the term that distinguishes the massive Dirac equation from the massless case, and it does not appear in the Maxwell equation. In the biquaternion formulation it is the linear, chirality-off-diagonal coupling of the pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ of the section *The Massive Case*; on the spinor module it is the term $m\psi$ of the matrix Dirac equation, which couples the left- and right-handed Weyl spinors. In the Standard Model the mass term arises from the **Higgs mechanism**: the fermion couples to the Higgs field, and the coupling generates an effective mass term.

The biquaternion framework does not derive the Higgs mechanism; it simply provides a compact notation for the mass term once the mechanism is assumed. The conjugation $\flat$ is a separate object — the algebra's real structure, discussed in the section *The Massive Case* — and is not the mass term.

## The Dirac Equation and the Biquaternion Algebra

### Why Biquaternions?

The Dirac equation is naturally expressed in terms of the Clifford algebra $\mathrm{Cl}_{1,3}$, which is the algebra generated by the gamma matrices. The biquaternion algebra $\mathbb{B}$ is isomorphic to the even subalgebra of $\mathrm{Cl}_{1,3}$, so the Dirac equation can be expressed in terms of $\mathbb{B}$ directly.

The advantage of the biquaternion formulation is that it is **more compact** than the matrix formulation: the biquaternion algebra has 8 real dimensions (or 4 complex dimensions), while the Clifford algebra $\mathrm{Cl}_{1,3}$ has 16 real dimensions. The biquaternion algebra is the minimal algebraic structure that contains the even part of the Clifford algebra, and it is sufficient for describing the spinor fields.

The disadvantage is that the biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ acts naturally on a two-dimensional complex module, while the Clifford algebra $\mathrm{Cl}_{1,3} \cong M_4(\mathbb{C})$ acts on a four-dimensional complex module. The biquaternion formulation therefore requires an additional step to recover the four-component Dirac spinor: the Dirac spinor is a pair of Weyl spinors (one left-handed, one right-handed), and the complex conjugate of the pair gives the antiparticle components.

### What the Biquaternion Formulation Adds

The biquaternion formulation adds three things:

**1. A unified algebraic framework for Maxwell and Dirac.** The two equations have the same form in different representations of the same algebra. This is the algebraic content of the statement that the photon and the electron are both described by the Clifford algebra $\mathrm{Cl}_{1,3}$.

**2. A compact notation for the spinor structure.** The two-component structure of the Weyl spinor is naturally encoded in the biquaternion algebra, without the need for explicit spinor indices. The left- and right-handed spinors are the two chiral components of the field — the two minimal left ideals of $\mathbb{B}$ — and the mass term is the linear coupling between them.

**3. A natural language for relativistic kinematics.** The four-velocity $\tilde{U}$, the four-momentum $\tilde{P}$, and the mass-shell relation $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$ are all natural objects in the biquaternion algebra. The Dirac equation is naturally stated in terms of these objects, and the plane-wave solutions are naturally written in terms of the wave biquaternion $\tilde{k}$ and the four-position $\tilde{X}$.

## Open Questions

1. **The real structure $\flat$ and the electroweak interaction.** The conjugation $\flat = -\dagger$, whose fixed space is the anti-Hermitian sector $\mathbb{M}_-$ and which is the algebra's real structure, has the shape of a Majorana-type pairing. Does that real structure have a natural interpretation in terms of the electroweak interaction — in particular, does it supply the real form in which the neutrino is distinguished from the charged fermions?

2. **The relation to the Standard Model.** The Standard Model describes fermions in the spinor representation of the Lorentz group. How does the biquaternion framework extend to the full Standard Model, including the gauge fields?

3. **The non-abelian generalization.** The biquaternionic Dirac equation is abelian (the field is a single biquaternion). How does the framework extend to non-abelian gauge theories, where the fermion field is a vector in a representation of the gauge group?

4. **The relation to the twistor program.** Twistor theory uses the complexified spinor space $\mathbb{C}^4$, which is related to the biquaternion algebra. How do the biquaternion Dirac equation and the twistor equation relate?

5. **The quantization.** The Dirac equation is the classical equation of motion for a fermion field. How does the biquaternion framework extend to the quantized theory (quantum field theory), and what is the role of the biquaternion structure in the quantized case?

6. **The relation to the biquaternion Maxwell equation.** The two equations have the same form. Is there a deeper sense in which the photon and the electron are the same biquaternion field in different representations, or is the identity purely formal?

7. **The minimal coupling to electromagnetism.** The standard Dirac equation couples to the electromagnetic field through the minimal coupling $\partial_\mu \to \partial_\mu - iqA_\mu/\hbar$. How this coupling reads in the biquaternion framework, given the biquaternion form of the four-potential $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$, is treated in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*.

These questions are open.

## Summary

The Dirac equation in biquaternionic form is the equation

$$
\tilde{\nabla}\tilde{\Psi} = 0
$$

in the massless case, and the chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R
$$

for mass $m$, where $\tilde{\nabla}$ is the biquaternionic gradient, $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$ is the spinor field with one component per chirality, and the mass term is linear. The massless equation has the same form as the source-free biquaternion Maxwell equation. The structural identity reflects the fact that both the photon and the electron are described by the same Clifford algebra $\mathrm{Cl}_{1,3}$, and the biquaternion algebra $\mathbb{B}$ is isomorphic to its even subalgebra. Each chiral component satisfies the Klein–Gordon equation $(\Box - m^2c^2/\hbar^2)\tilde{\Psi} = 0$.

The relativistic kinematic relations are naturally expressed in biquaternion form: the four-velocity $\tilde{U} = \gamma(ic\, e_0 + \mathbf{v})$ satisfies $\tilde{U}\bar{\tilde{U}} = -c^2$, the four-momentum $\tilde{P} = m\tilde{U}$ satisfies the mass-shell relation $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$, and the four-position $\tilde{X} = ict\, e_0 + \mathbf{x}$ gives the invariant interval $ds^2 = N(d\tilde{X}) = d\tilde{X}\circ\overline{d\tilde{X}}$.

The plane-wave solutions of the massless equation are $\tilde{\Psi} = \tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde{k}\bar{\tilde{X}})\right) = \tilde{\Psi}_0\,e^{\,i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ with $\tilde{k}\tilde{\Psi}_0 = 0$ (nonzero solutions only for null $\tilde{k}$), giving the two spin states of a massless fermion. The massive plane waves satisfy the mass-shell condition $\tilde{k}\bar{\tilde{k}} = -m^2 c^2/\hbar^2$; the two frequency branches are the particle and the antiparticle, and with the two spin states they give the four components of the Dirac spinor.

The spherical and cylindrical solutions are constructed by the methods of Clifford analysis, via the monogenic completion of harmonic functions. They describe the angular momentum states of the fermion field and the waveguide modes, respectively.

The biquaternion framework provides a compact and unified language for the Maxwell and Dirac equations, but it does not by itself derive the mass term or the electroweak structure. Those require additional physics beyond the algebraic framework.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\mathbf{v}$ | Particle three-velocity |
| $\gamma = 1/\sqrt{1 - \mathbf{v}^2/c^2}$ | Lorentz factor |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | Four-position biquaternion |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity biquaternion |
| $\tilde{P} = m\tilde{U}$ | Four-momentum biquaternion |
| $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$ | Spinor field, one component per chirality |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |

| $\tilde{k}$ | Wave biquaternion |
| $m$ | Fermion mass |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the foundational treatment of the Dirac equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard physics treatment.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and spinor fields.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra approach to the Dirac equation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in geometric algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation of the Dirac equation.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the monogenic functions and the Clifford-analytic technique.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of the Dirac equation.

