# __The Multipole Expansion and the Quadrupole Interaction in Biquaternionic Form__

## Introduction

A bounded source — a charge distribution, a mass distribution, a deformed body — is described at distances large compared with its own size by an infinite series of **multipole moments**: the monopole, the dipole, the quadrupole, the octupole, and so on. The series is the standard way of organising the field of a localised source, and it is the classical expression of a simple fact: the field of a finite body, seen from far away, is classified by the angular momentum that its angular dependence carries. Each order $l$ is a definite irreducible representation $D^{(l)}$ of the rotation group, of dimension $2l+1$, and the series runs over every $l \geq 0$.

This article develops the multipole expansion in the biquaternion framework and treats the **quadrupole interaction** as the first order above the dipole. The treatment is **non-relativistic** and classical throughout: the sources are at rest or move slowly compared with the speed of light, the fields are computed in the static or quasi-static limit, and neither retardation nor the relativistic multipole structure enters. The relativistic quadrupole is a separate subject.

The biquaternion framework is set in the algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, over complex coefficients, and central scalar imaginary $i$, $i^2 = -1$. The material sector is the anti-Hermitian subspace

$$
\mathbb{M}_- = \{\tilde{Q}\in\mathbb{B} : \tilde{Q}^\flat = \tilde{Q}\},
$$

with basis $ie_0, e_1, e_2, e_3$, whose norm form has signature $(3,1)$; it carries the four-vectors of physics. The informational sector is the Hermitian subspace $\mathbb{M}_+$, with basis $e_0, ie_1, ie_2, ie_3$. The two sectors satisfy $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$. The biquaternionic gradient is

$$
\tilde{\nabla} = e_0\,\partial_{ict} + e_1\,\partial_x + e_2\,\partial_y + e_3\,\partial_z,
\qquad
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta .
$$

Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ its vacuum value. The conventions are those of the companion articles:
- Companion article *Introduction to the Biquaternion Universe*, for the algebra and its two sectors.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the four-vectors of the material sector.
- Companion article *Conventions in the Biquaternion Universe*, for the trace, the metric at its three levels, and the sector conventions.
- Companion article *Biquaternion Representation Theory*, for the algebra as a complex algebra and its modules, whose $V$-modules are a different family from the rotation representations $D^{(l)}$ used here.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field-strength biquaternion and the fields $\mathbf{E}$ and $\mathbf{H}$.

The article's thesis can be stated at once. The biquaternion algebra, regarded as a representation space of the rotation group — the group acting by rotor conjugation — is the direct sum $D^{(0)}\oplus D^{(1)}$ of the trivial representation and the vector representation, and nothing more. Its **elements** can therefore carry the monopole (a central scalar) and the dipole (a vector), and its **product** never leaves that sum either, because $\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v}$ keeps only the dot and the cross product. The **quadrupole** is the first moment that is not an algebra element: it is a symmetric traceless rank-two tensor, the representation $D^{(2)}$, and it lives in the symmetric traceless square of the vector part rather than in the algebra itself. The quadrupole **interaction energy**, by contrast, is a scalar, and therefore is always an element of the center $\mathbb{C}_{\mathbb{B}}$. The distinction between the moment, which is a tensor, and its interaction, which is a scalar, organises the article and the two that follow it.

## The Multipole Expansion of a Localised Source

### From the Coulomb Integral to the Series

Let a charge distribution of density $\rho(\mathbf{x}')$ be confined to a bounded region around the origin. Its electrostatic potential at a field point $\mathbf{x}$ is the Coulomb integral

$$
\Phi(\mathbf{x}) = \frac{1}{4\pi\epsilon_0}\int \frac{\rho(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|}\,d^3x' .
$$

The kernel is expanded by the standard Legendre expansion. Writing $r = |\mathbf{x}|$, $r' = |\mathbf{x}'|$, $\hat{\mathbf{n}} = \mathbf{x}/r$, $\hat{\mathbf{n}}' = \mathbf{x}'/r'$, and $\cos\gamma = \hat{\mathbf{n}}\cdot\hat{\mathbf{n}}'$, the expansion is

$$
\frac{1}{|\mathbf{x} - \mathbf{x}'|} = \sum_{l=0}^{\infty}\frac{r_<^{\,l}}{r_>^{\,l+1}}\,P_l(\cos\gamma),
$$

where $r_>$ is the larger and $r_<$ the smaller of $r$ and $r'$, and $P_l$ is the Legendre polynomial of degree $l$. For a field point outside the source, $r_> = r$ and $r_< = r'$, and the series converges absolutely. This is the standard result; it is the ancestor of every multipole expansion.

### The Spherical-Harmonic Form

Inserting the Legendre expansion and using the addition theorem for spherical harmonics gives the **spherical multipole expansion**

$$
\Phi(\mathbf{x}) = \frac{1}{4\pi\epsilon_0}\sum_{l=0}^{\infty}\frac{4\pi}{2l+1}\,\frac{1}{r^{l+1}}\sum_{m=-l}^{l} q_{lm}\,Y_l^{m}(\theta,\phi),
$$

with the **spherical multipole moments**

$$
q_{lm} = \int \rho(\mathbf{x}')\,r'^{\,l}\,Y_l^{m*}(\theta',\phi')\,d^3x' .
$$

The angular integration is over the source, and the moments $q_{lm}$ depend only on the source, not on the field point. Each order $l$ contributes $2l+1$ moments, transforming among themselves under a rotation of the coordinate frame as the representation $D^{(l)}$.

### The First Three Moments

The three lowest orders have their familiar names and their familiar Cartesian representatives.

**Monopole ($l = 0$).** The single moment is the total charge,

$$
q = \int \rho(\mathbf{x}')\,d^3x' ,
$$

and the monopole potential is $\Phi_{mon} = q/(4\pi\epsilon_0 r)$.

**Dipole ($l = 1$).** The three moments are the components of the **dipole moment vector**

$$
\mathbf{p} = \int \rho(\mathbf{x}')\,\mathbf{x}'\,d^3x',
$$

and the dipole potential is

$$
\Phi_{dip}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0}\,\frac{\mathbf{p}\cdot\hat{\mathbf{n}}}{r^2}.
$$

**Quadrupole ($l = 2$).** The five independent moments are those of the **quadrupole tensor**

$$
Q_{ij} = \int \rho(\mathbf{x}')\left(3x_i'x_j' - r'^{\,2}\delta_{ij}\right)d^3x' ,
$$

which is symmetric, $Q_{ij} = Q_{ji}$, and traceless, $Q_{ii} = 0$; those two conditions reduce the nine Cartesian entries to five. The quadrupole potential is

$$
\Phi_{quad}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0}\,\frac{1}{2r^3}\,Q_{ij}\,\hat{n}_i\hat{n}_j .
$$

The tracelessness is not an extra assumption: the term proportional to $\delta_{ij}$ in $Q_{ij}$ would contribute $\hat{n}_i\hat{n}_i = 1$ and hence a monopole-like $1/r$ tail, which is already accounted for by $q$; removing the trace makes the quadrupole the pure $l = 2$ object. The relation of the Cartesian form to the spherical form is exact, and it has been checked directly: for a point charge, $\frac{1}{4\pi\epsilon_0}\frac{1}{2r^3}Q_{ij}\hat{n}_i\hat{n}_j$ reproduces the $l = 2$ Legendre term $\frac{1}{4\pi\epsilon_0}\frac{r'^{\,2}}{r^3}P_2(\cos\gamma)$ term by term.

### The Tower and Its Ordering

The series is organized by increasing $l$. The potential falls off as $r^{-(l+1)}$, so at large distances each order is smaller than the one before by a factor of the source size over the distance, and the series is an expansion in that ratio. There is no largest $l$: the tower is **infinite**, and its infinity is a property of the angular structure of the fields, as the final article of this sequence examines.

## The Multipole Tower and the Rotation Group

### The Representations $D^{(l)}$

The rotation group $SO(3)$ has, up to equivalence, exactly one irreducible real representation of each odd dimension $2l+1$, $l = 0, 1, 2, \dots$; its double cover $SU(2)$ has exactly one irreducible complex representation of each dimension $2l+1$, written $D^{(l)}$ after Wigner's rotation matrices, so that $\dim_{\mathbb{C}}D^{(l)} = 2l+1$. The label $l$ is the angular momentum and $D^{(l)}$ is the standard rotation-group representation of that angular momentum; the representation-theory companion uses the letter $V$ for the polynomial modules of the complex algebra, a different family, and the present notation is the rotation-group one. In the biquaternion framework the rotation rotors are the real unit quaternions, a group isomorphic to $SU(2)$,

$$
\mathbb{H}_{\mathbb{B}}^1 = \{\tilde{\Lambda}\in\mathbb{H}_{\mathbb{B}} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\},
$$

acting on a vector by $\mathbf{v}\mapsto\tilde{\Lambda}\mathbf{v}\bar{\tilde{\Lambda}}$. The multipole moment of order $l$ is a tensor in $D^{(l)}$: the monopole is $D^{(0)}$, the dipole is $D^{(1)}$, the quadrupole is $D^{(2)}$, and so on.

### Why the Order Is an Angular Momentum

The reason $l$ deserves to be called an angular momentum is that the moments are the coefficients of a function on the sphere, and the space of functions on the sphere carries the regular representation of the rotation group. Its decomposition is

$$
L^2(S^2) = \bigoplus_{l=0}^{\infty} D^{(l)} ,
$$

in which each $D^{(l)}$ occurs exactly once; the spherical harmonic $Y_l^m$ is its weight-$m$ basis vector, the eigenfunction of the rotation about the polar axis with eigenvalue $m$. The multipole expansion is therefore the decomposition of the field's angular dependence into irreducible rotation representations, and the order $l$ is the angular momentum carried by that angular dependence.

Two comments fix the reading. First, the tower is infinite because the space of functions on the sphere is **infinite-dimensional**: a function on $S^2$ has arbitrarily fine angular structure, and each finer scale is one more $D^{(l)}$. Second, the tower is a property of the **field**, which is a function of position; it is not a property of the algebra of values the field takes. That distinction becomes the whole content of the closing article, and it is already visible here.

## The Biquaternion Transcription of the Fields

### The Potential and the Field

In the $ict$ convention the four-potential is an element of the material sector,

$$
\tilde{A} = \frac{i\phi}{c}\,e_0 + \mathbf{A} \in \mathbb{M}_- ,
\qquad \mathbf{A} = A_1e_1 + A_2e_2 + A_3e_3 ,
$$

whose scalar coefficient is imaginary and whose vector part is real. In the electrostatic limit $\mathbf{A} = 0$, and the four-potential reduces to the purely imaginary central element $(i\phi/c)\,e_0$, still an element of $\mathbb{M}_-$: the scalar part of a four-potential is imaginary, and it is that imaginary scalar coefficient that marks the sector. The constant factor $i/c$ plays no role in the statics, and it is convenient to work with the rescaled central element

$$
\tilde{\Phi} = \Phi\,e_0 ,
$$

a real, Hermitian central element. It is not itself the four-potential — that is $(i\phi/c)\,e_0$ — but the scalar potential, and the gradients below are the same for either normalisation.

The spatial derivative operator is the vector part of the biquaternionic gradient,

$$
\boldsymbol{\nabla} = e_1\partial_x + e_2\partial_y + e_3\partial_z ,
$$

so that $\tilde{\nabla} = e_0\partial_{ict} + \boldsymbol{\nabla}$. Acting on a central element, $\boldsymbol{\nabla}$ produces a pure real vector,

$$
\boldsymbol{\nabla}(\Phi\,e_0) = (\partial_x\Phi)e_1 + (\partial_y\Phi)e_2 + (\partial_z\Phi)e_3 ,
$$

which is $-\mathbf{E}$ in biquaternion form: since $\mathbf{E} = -\boldsymbol{\nabla}\Phi$, the object computed is $\boldsymbol{\nabla}\Phi = -\mathbf{E}$, a pure real vector, an element of the vector part of $\mathbb{H}_{\mathbb{B}}$, and hence of $\mathbb{M}_-$.

**The spatial Laplacian.** A fact used twice below is that the second power of the vector gradient is minus the Laplacian,

$$
\boldsymbol{\nabla}\,\boldsymbol{\nabla} = \sum_{i,j}e_ie_j\,\partial_i\partial_j = -\sum_i \partial_i^2\,e_0 = -\Delta\,e_0 .
$$

The antisymmetric part of the quaternion product, $\sum_{i<j}(e_ie_j - e_je_i)\partial_i\partial_j$, vanishes because the partial derivatives commute, so only the trace survives. This has been verified symbolically: for a quadratic potential $\Phi$ with Hessian $H$, the combination $\sum_{ij}e_ie_j\,H_{ij}$ equals $-\mathrm{tr}(H)e_0$ exactly, and the traceless symmetric part of the Hessian never appears.

### The Field-Strength Biquaternion

The field-strength biquaternion of the companion electromagnetic articles is

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H} = \mathbf{F},
\qquad \mathbf{F} = F_1e_1 + F_2e_2 + F_3e_3 ,
$$

a pure-vector biquaternion with vanishing scalar part, whose imaginary half carries the electric field and whose real half carries the magnetic field. In the electrostatic limit $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E}$. The conventions and the derivation are those of
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the definition of $\tilde{F}$ and the single field equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$.

For the multipole problem it is convenient to work with the real vector $\mathbf{E}$ itself, since the medium factors and the factor of $i$ play no role in the non-relativistic statics. The two objects are elements of the same kind: a real spatial vector is an element of the vector part, and the vector part is a faithful copy of $\mathbb{R}^3$ inside $\mathbb{H}_{\mathbb{B}}$.

## The Monopole and the Dipole as Algebra Elements

### The Monopole

The monopole moment is a scalar, and in the algebra it is the central element $q\,e_0 \in \mathbb{C}_{\mathbb{B}}$. Under a rotation the center is pointwise fixed, which is the algebraic statement that the monopole is the $D^{(0)}$ representation. The monopole interaction energy $q\Phi(0)$ is likewise a central scalar.

### The Dipole

The dipole moment is a vector,

$$
\tilde{p} = p_1e_1 + p_2e_2 + p_3e_3 ,
$$

a pure real quaternion with $\bar{\tilde{p}} = -\tilde{p}$. Its representative lies in the vector part, which is exactly the $D^{(1)}$ representation, so the dipole is the first non-trivial multipole that is an **element of the algebra**. Two consequences follow.

**The dipole potential.** With the unit radial quaternion $\hat{\mathbf{n}} = (x_1e_1 + x_2e_2 + x_3e_3)/r$, satisfying $\hat{\mathbf{n}}^2 = -e_0$, the dipole potential is

$$
\Phi_{dip} = -\frac{1}{4\pi\epsilon_0}\,\frac{\mathrm{Sc}\!\left(\tilde{p}\,\hat{\mathbf{n}}\right)}{r^2},
$$

because $\mathrm{Sc}(\tilde{p}\hat{\mathbf{n}}) = -\mathbf{p}\cdot\hat{\mathbf{n}}$ for pure real vectors.

**The dipole interaction.** The energy of a dipole in an external electric field is $-\mathbf{p}\cdot\mathbf{E}$, and this is an algebraic pairing of two vector elements. For pure real vectors $\tilde{p}, \tilde{\mathbf{E}}$ one has $\tilde{p}\tilde{\mathbf{E}} = -\mathbf{p}\cdot\mathbf{E} + \mathbf{p}\times\mathbf{E}$, so

$$
-\mathbf{p}\cdot\mathbf{E}\,e_0 = \mathrm{Sc}\!\left(\tilde{p}\tilde{\mathbf{E}}\right)e_0 = \tfrac12\left(\tilde{p}\tilde{\mathbf{E}} + \tilde{\mathbf{E}}\tilde{p}\right).
$$

The pairing is the **symmetrized product** of the two vectors, and its value is a central scalar. The dipole interaction is therefore fully internal to the algebra: both the moment and the field are elements, and their interaction is the scalar part of their product. The sign has been checked: $-\mathrm{Sc}(\tilde{p}\tilde{\mathbf{E}}) = \mathbf{p}\cdot\mathbf{E}$ for real vectors, so $-\mathbf{p}\cdot\mathbf{E} = \mathrm{Sc}(\tilde{p}\tilde{\mathbf{E}})$.

The dipole is thus the first non-trivial multipole for which the moment is an algebra element and the moment–field coupling is an algebra product — the monopole is the trivial case, a scalar whose coupling $q\Phi(0) = (qe_0)(\Phi e_0)$ is an algebra product too. The dipole is the model for what the algebra can do; the quadrupole is where that stops.

## The Quadrupole Tensor and Its Interaction

### The Moment as a Tensor

The quadrupole moment is not a vector but a symmetric traceless rank-two tensor,

$$
Q_{ij} = Q_{ji}, \qquad Q_{ii} = 0, \qquad i,j = 1,2,3 ,
$$

with five independent components. It is the representation $D^{(2)}$ of the rotation group. Equivalently, it is a harmonic homogeneous polynomial of degree two in the direction cosines, $Q(\hat{\mathbf{n}}) = Q_{ij}\hat{n}_i\hat{n}_j$, or a linear combination of the five spherical harmonics $Y_2^m$. The three descriptions are the same object in three notations.

### The Quadrupole Potential

The potential of a quadrupole is the $l = 2$ term of the expansion,

$$
\Phi_{quad}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0}\,\frac{1}{2r^3}\,Q_{ij}\,\hat{n}_i\hat{n}_j ,
$$

and it agrees exactly with the $l = 2$ Legendre term of the Coulomb kernel, as noted above. The fall-off is $r^{-3}$, one power faster than the dipole and two faster than the monopole.

### The Interaction Energy

The interaction energy of a bounded charge distribution with an external potential $\Phi_{ext}$ is $W = \int\rho\,\Phi_{ext}\,d^3x'$. Expanding $\Phi_{ext}$ about the origin,

$$
\Phi_{ext}(\mathbf{x}') = \Phi(0) - x_i' E_i(0) - \tfrac12 x_i'x_j'\,\partial_iE_j(0) + \cdots ,
$$

where $\mathbf{E} = -\boldsymbol{\nabla}\Phi$ is the external field. The quadratic term separates into a trace part and a traceless part once the second moments are written in terms of the quadrupole tensor,

$$
\int\rho\,x_i'x_j'\,d^3x' = \tfrac13\,Q_{ij} + \tfrac13\,\delta_{ij}\int\rho\,r'^{\,2}d^3x' ,
$$

and the trace part contributes $-\tfrac16(\nabla\cdot\mathbf{E})(0)\int\rho\,r'^{\,2}d^3x'$. For an external field whose own sources lie outside the distribution, $\nabla\cdot\mathbf{E}$ vanishes wherever the distribution sits and that term drops, leaving the standard multipole expansion of the interaction energy,

$$
W = q\,\Phi(0) - \mathbf{p}\cdot\mathbf{E}(0) - \tfrac16\,Q_{ij}\,\partial_iE_j(0) + \cdots .
$$

Separating off the trace term is what leaves the quadrupole entering the expansion through the traceless tensor $Q_{ij}$ alone, and it is the same split that the representation-theoretic contraction below uses.

The identity was verified numerically on three point charges: with a quadratic external potential carrying a traceless Hessian, so that $\nabla\cdot\mathbf{E} = 0$, the direct energy $\sum_a q_a\Phi_{ext}(\mathbf{x}_a)$ and the three-term expansion agree to machine precision at every source size $a$ (residual at the roundoff floor, a relative $10^{-16}$) — an exact test, since a quadratic potential terminates the expansion at the quadrupole. The coefficient $-\tfrac16$ was then checked against a genuinely higher-order case: adding a cubic term to $\Phi_{ext}$, the residual of the three-term expansion falls off as the cube of the source size, $4.3\times10^{-3}, 1.2\times10^{-4}, 4.3\times10^{-6}, 1.2\times10^{-7}, 4.3\times10^{-9}$ at source scales $1, 0.3, 0.1, 0.03, 0.01$ — a ratio of $27$ per factor of three, the signature of a first error at the octupole. A wrong coefficient in the quadrupole term would have left a residual falling only as the square. The trace term was verified on the same charges by varying the Hessian trace: the direct energy differs from the source-free expansion by exactly $-\tfrac16(\nabla\cdot\mathbf{E})(0)\int\rho r'^{\,2}d^3x'$, to machine precision, at $\nabla\cdot\mathbf{E} = -0.3, +0.7, -1.5$, the difference changing sign with $\nabla\cdot\mathbf{E}$.

Two features of the quadrupole term deserve emphasis, because they are what the algebra will and will not see.

**Only the traceless part of the field gradient matters.** Since $Q_{ii} = 0$ and $\partial_iE_j = -\partial_i\partial_j\Phi$ is symmetric in $i,j$, the contraction $Q_{ij}\partial_iE_j$ receives contributions only from the traceless symmetric part of the field-gradient matrix. Writing

$$
\partial_iE_j = \tfrac13\delta_{ij}\,\nabla\cdot\mathbf{E} + T_{ij},
\qquad T_{ii} = 0, \quad T_{ij} = T_{ji},
$$

the trace term drops against $Q_{ii} = 0$. With the external field source-free at the location of the distribution, as assumed for the expansion above, the quadrupole interaction is therefore the pure contraction of two $D^{(2)}$ objects,

$$
W_{quad} = -\tfrac16\,Q_{ij}T_{ij} = \tfrac16\,Q_{ij}\,\partial_i\partial_j\Phi(0).
$$

**It is a scalar.** Like every interaction energy, $W_{quad}$ is a single number, hence an element of the center $\mathbb{C}_{\mathbb{B}}$. The algebra has no difficulty with the *value* of the quadrupole interaction. Its difficulty is with the *moment*, and that is the subject of the next section.

## Why the Quadrupole Is Not an Algebra Element

### The Product of Two Vectors Stops at $D^{(1)}$

The biquaternion product of two spatial vectors is fixed by the quaternion relations. For pure real vectors $\mathbf{u}, \mathbf{v}$,

$$
\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v},
$$

a central scalar plus a vector. The identity was verified on fifty random vector pairs. Equivalently, symmetrizing,

$$
\tfrac12\left(\mathbf{u}\mathbf{v} + \mathbf{v}\mathbf{u}\right) = -(\mathbf{u}\cdot\mathbf{v})\,e_0 ,
\qquad
\tfrac12\left(\mathbf{u}\mathbf{v} - \mathbf{v}\mathbf{u}\right) = \mathbf{u}\times\mathbf{v}.
$$

The dot product is the $D^{(0)}$ channel and the cross product is the $D^{(1)}$ channel. The **symmetric traceless** part of the tensor product $\mathbf{u}\otimes\mathbf{v}$ — which is the $D^{(2)}$ channel — never appears: the symmetrized quaternion product collapses it to the trace. In the language of representations,

$$
D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)} ,
\qquad 3\times 3 = 1 + 3 + 5 ,
$$

and the quaternion product projects onto the first two summands, discarding the third. A quadrupole is precisely a symmetric traceless tensor, so it is precisely what the product discards.

### The Algebra Contains Only $D^{(0)}$ and $D^{(1)}$

The same conclusion follows from the structure of the algebra itself. Under the rotor-conjugation action of the rotation group, $\mathbb{B}$ decomposes into the center, spanned by $e_0$, and the vector part, spanned by $e_1, e_2, e_3$. The center is invariant, so it is $D^{(0)}$; the vector part transforms as a vector, so it is $D^{(1)}$:

$$
\mathbb{B} = D^{(0)}\oplus D^{(1)} \quad\text{(as a complex representation of the rotations)},
\qquad 1 + 3 = 4 .
$$

The weight spectrum confirms that nothing else can be present. For a rotation about the axis $e_3$, the center is fixed, $e_3$ is fixed, and the combinations $e_1\pm ie_2$ are eigenvectors with phases $e^{\mp i\theta}$. The algebra therefore contains states only of weights $0$ and $\pm1$, and a $D^{(2)}$ representation would require a state of weight $\pm2$. There is none. The character of the conjugation action has been computed directly and equals $2 + 2\cos\theta = \chi_0(\theta) + \chi_1(\theta)$, the sum of the spin-$0$ and spin-$1$ characters, with no $D^{(2)}$ term $\chi_2 = 1 + 2\cos\theta + 2\cos2\theta$. Since $-\tilde{\Lambda}$ acts on a vector exactly as $\tilde{\Lambda}$ does, the conjugation action factors through $SO(3)$ and can carry only integral angular momentum. In the normalisation in which the vector part carries weights $\pm1$ — that is, with the generator $J_3 = -i\tfrac12\mathrm{ad}_{e_3}$ — the generator has the eigenvalue spectrum $\{0, 0, +1, -1\}$ on $\mathbb{B}$: a doubly degenerate zero, together with a single $+1$ and a single $-1$. A quadrupole, which would carry weight $\pm2$, has no place to sit.

### Where the Quadrupole Does Live

The quadrupole is a symmetric traceless tensor over the vector part, and the natural algebraic home is the **symmetric traceless square** of $D^{(1)}$,

$$
\operatorname{Sym}^2_0(D^{(1)}) \cong D^{(2)} ,
\qquad \dim_{\mathbb{C}}\operatorname{Sym}^2_0(D^{(1)}) = 5 ,
$$

which is a subspace of the tensor square $D^{(1)}\otimes D^{(1)}$ — equivalently of $\mathbb{B}\otimes\mathbb{B}$ — and not a subspace of $\mathbb{B}$. In coordinate terms, a quadrupole is the traceless part of a symmetric bilinear form $Q(\mathbf{u},\mathbf{v})$ on the vector part. This is the precise sense in which the quadrupole is *outside* the algebra: it is a tensor built from two vectors, not a single element.

The same conclusion can be read off the second derivative. From $\boldsymbol{\nabla}\boldsymbol{\nabla} = -\Delta\,e_0$, the iterated gradient of a scalar potential is a pure central element: the product of the two gradient operators annihilates the traceless symmetric part of $\partial_i\partial_j\Phi$. The quadrupole angular information is carried by the scalar field $\Phi(\mathbf{x})$ — which has arbitrary angular dependence — and by the tensor of its second derivatives, but it is invisible to the *product* of two gradient operators.

### The Invariant Statement

It is worth stating the conclusion in the form the physics demands. A multipole moment is an *invariant of the source*: an integral over the source, a functional of the charge distribution. It is not an element of the value algebra of the field. The moments of order $l = 0$ and $l = 1$ happen to coincide with the two irreducible pieces of the algebra — the center and the vector part — and so can be written as single biquaternions. The moments of order $l \geq 2$ cannot: they are tensors, functionals of the source, or, equivalently, coefficients in the angular expansion of a scalar field. The quadrupole is the first moment at which the finite dimension of the algebra becomes visible in the physics.

This is not a defect of the framework. It is the same finite-dimensionality that the companion article on the Poisson bracket identifies as the obstruction to the canonical Heisenberg algebra inside $\mathbb{B}$:
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the trace obstruction that blocks the canonical bracket inside the finite-dimensional algebra.

The algebra is a **value algebra** of finite dimension, and it carries exactly the spin-$0$ and spin-$1$ content of a scalar and a three-vector. The multipole tower is a property of the **field space**, which is infinite-dimensional. The two are different objects, and no finite algebra can play the role of the infinite-dimensional function space. The closing article of this sequence turns that observation into a general statement.

## Summary

The static field of a bounded source is expanded in multipole moments, one order for each irreducible representation $D^{(l)}$ of the rotation group, with $2l+1$ moments per order. In the biquaternion framework the fields are elements of the algebra: the four-potential is $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}\in\mathbb{M}_-$ with an imaginary scalar coefficient, the scalar potential is obtained from its scalar part, the spatial gradient is the vector operator $\boldsymbol{\nabla}$, and the electrostatic field is a real vector.

The moments fall into two classes. The monopole is a central scalar and the dipole is a vector, so both are **elements of the algebra**, and the dipole interaction $-\mathbf{p}\cdot\mathbf{E} = \mathrm{Sc}(\tilde{p}\tilde{\mathbf{E}})$ is an algebra product. The quadrupole is a symmetric traceless rank-two tensor, the representation $D^{(2)}$, and it is **not** an algebra element: the quaternion product of two vectors, $\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v}$, projects $D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)}$ onto $D^{(0)}\oplus D^{(1)}$ and discards the symmetric traceless part. The algebra, as a rotation representation, is $\mathbb{B} = D^{(0)}\oplus D^{(1)}$ and contains no weight-$\pm2$ state. The quadrupole's home is the symmetric traceless square $\operatorname{Sym}^2_0(D^{(1)})\cong D^{(2)}$, a subspace of $\mathbb{B}\otimes\mathbb{B}$.

The quadrupole **interaction** is a scalar and therefore lies in the center: with the external field source-free at the source, $W_{quad} = -\frac16 Q_{ij}T_{ij} = \frac16 Q_{ij}\partial_i\partial_j\Phi(0)$, the contraction of two $D^{(2)}$ objects. The interaction energy is an element of the algebra even though the moment is not.

The multipole tower is infinite because the angular structure of a field on the sphere is infinite-dimensional; the algebra is finite because it is the value algebra of a two-state, four-vector structure. The first order at which the difference shows is the quadrupole.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \{Q_0e_0\}$ | Center of $\mathbb{B}$ (the scalars) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde{\Lambda}\in\mathbb{H}_{\mathbb{B}}^1$, $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | Rotation rotor, acting on a vector by $\mathbf{v}\mapsto\tilde{\Lambda}\mathbf{v}\bar{\tilde{\Lambda}}$ |
| $\tilde{\nabla} = e_0\partial_{ict} + \boldsymbol{\nabla}$ | Biquaternionic gradient |
| $\boldsymbol{\nabla} = e_1\partial_x + e_2\partial_y + e_3\partial_z$ | Spatial vector gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$ | d'Alembertian (series convention) |
| $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | Four-potential, an element of $\mathbb{M}_-$ |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion |
| $\hat{\mathbf{n}} = \mathbf{x}/r$ | Unit radial quaternion, $\hat{\mathbf{n}}^2 = -e_0$ |
| $\mathrm{Sc}(\cdot)$ | Scalar (central) part |
| $\Phi$, $\Phi_{ext}$ | Scalar potential of the source, and an external potential; $\Phi_{mon}, \Phi_{dip}, \Phi_{quad}$ its multipole parts |
| $\rho$ | Charge density, the corpus convention for the bare $\rho$ |
| $q_{lm}, q, \mathbf{p}, Q_{ij}$ | Spherical, monopole, dipole and quadrupole moments |
| $D^{(l)}$ | Irreducible rotation representation of dimension $2l+1$ (Wigner's $D$) |
| $\operatorname{Sym}^2_0(D^{(1)})\cong D^{(2)}$ | Symmetric traceless square of the vector part |
| $Y_l^m, P_l$ | Spherical harmonics and Legendre polynomials |

## Further Reading

- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard multipole expansion and the quadrupole interaction energy.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for multipole moments and their transformation properties.
- M. E. Rose, *Elementary Theory of Angular Momentum* (Wiley, 1957), for the irreducible representations $D^{(l)}$ and the addition theorem.
- A. R. Edmonds, *Angular Momentum in Quantum Mechanics* (Princeton, 1957), for the Clebsch–Gordan decomposition of $D^{(1)}\otimes D^{(1)}$.
- G. B. Arfken and H. J. Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), for the Legendre expansion and the spherical harmonics.
- P. M. Morse and H. Feshbach, *Methods of Theoretical Physics* (McGraw-Hill, 1953), for solid harmonics and the multipole series.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quaternion product rule and the representation theory of the algebras used here.
