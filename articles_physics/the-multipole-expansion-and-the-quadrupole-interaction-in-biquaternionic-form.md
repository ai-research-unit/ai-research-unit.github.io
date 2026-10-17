# __The Multipole Expansion and the Quadrupole Interaction in Biquaternionic Form__

## Introduction

A bounded source — a charge distribution, a mass distribution, a deformed body — is described at distances large compared with its own size by an infinite series of **multipole moments**: the monopole, the dipole, the quadrupole, the octupole, and so on. The series is the standard way of organising the field of a localised source, and it is the classical expression of a simple fact: the field of a finite body, seen from far away, is classified by the angular momentum that its angular dependence carries. Each order $l$ is a definite irreducible representation $D^{(l)}$ of the rotation group, of dimension $2l+1$, and the series runs over every $l \geq 0$.

This article develops the multipole expansion in the biquaternion framework and treats the **quadrupole interaction** as the first order above the dipole. The treatment is **non-relativistic** and classical throughout: the sources are at rest or move slowly compared with the speed of light, the fields are computed in the static or quasi-static limit, and neither retardation nor the relativistic multipole structure enters. The relativistic quadrupole is a separate subject.

The biquaternion framework is set in the algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_k^2 = -e_t$, over complex coefficients, and central scalar imaginary $i$, $i^2 = -1$. The material sector is the anti-Hermitian subspace

$$
\mathbb{M}_- = \{\tilde{Q}\in\mathbb{B} : \tilde{Q}^\flat = \tilde{Q}\},
$$

with basis $ie_t, \vec e_x, \vec e_y, \vec e_z$, whose biquaternion norm has signature $(3,1)$; it carries the four-vectors of physics. The informational sector is the Hermitian subspace $\mathbb{M}_+$, with basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$. The two sectors satisfy $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$. The biquaternionic gradient is

$$
\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec e_x\,\partial/\partial Q_x + \vec e_y\,\partial/\partial Q_y + \vec e_z\,\partial/\partial Q_z,
\qquad
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta .
$$

Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ its vacuum value. The conventions are those of the companion articles:
- Companion article *Introduction to the Biquaternion Universe*, for the algebra and its two sectors.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the four-vectors of the material sector.
- Companion article *Conventions in the Biquaternion Universe*, for the trace, the metric (its three levels are ruled on in *The Four Forms, the Four Algebraic Norms and the Change of Scalars*), and the sector conventions.
- Companion article *Modules over the Biquaternion Algebra*, for the algebra as a complex algebra and its modules, whose $V$-modules are a different family from the rotation representations $D^{(l)}$ used here.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field-strength biquaternion and the fields $\vec E$ and $\vec H$.

The article's thesis can be stated at once. The biquaternion algebra, regarded as a representation space of the rotation group — the group acting by rotor conjugation — is the direct sum $D^{(0)}\oplus D^{(1)}$ of the trivial representation and the vector representation, and nothing more. Its **elements** can therefore carry the monopole (a central scalar) and the dipole (a vector), and its **product** never leaves that sum either, because $\vec q\vec v = -\vec q\cdot\vec v + \vec q\times\vec v$ keeps only the dot and the cross product. The **quadrupole** is the first moment that is not an algebra element: it is a symmetric traceless rank-two tensor, the representation $D^{(2)}$, and it lives in the symmetric traceless square of the vector part rather than in the algebra itself. The quadrupole **interaction energy**, by contrast, is a scalar, and therefore is always an element of the centre $\mathbb{C}_{\mathbb{B}}$. The distinction between the moment, which is a tensor, and its interaction, which is a scalar, organises the article and the two that follow it.

## The Multipole Expansion of a Localised Source

### From the Coulomb Integral to the Series

Let a charge distribution of density $\rho(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ be confined to a bounded region around the origin. Its electrostatic potential at a field point $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ is the Coulomb integral

$$
\Phi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon_0}\int \frac{\rho(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)}{|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)|}\,d^3x' .
$$

The kernel is expanded by the standard Legendre expansion. Writing $r = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|$, $r' = |x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z|$, $\vec u = (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/r$, $\vec u' = (x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)/r'$, and $\cos\gamma = \vec u\cdot\vec u'$, the expansion is

$$
\frac{1}{|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)|} = \sum_{l=0}^{\infty}\frac{r_<^{\,l}}{r_>^{\,l+1}}\,P_l(\cos\gamma),
$$

where $r_>$ is the larger and $r_<$ the smaller of $r$ and $r'$, and $P_l$ is the Legendre polynomial of degree $l$. For a field point outside the source, $r_> = r$ and $r_< = r'$, and the series converges absolutely. This is the standard result; it is the ancestor of every multipole expansion.

### The Spherical-Harmonic Form

Inserting the Legendre expansion and using the addition theorem for spherical harmonics gives the **spherical multipole expansion**

$$
\Phi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon_0}\sum_{l=0}^{\infty}\frac{4\pi}{2l+1}\,\frac{1}{r^{l+1}}\sum_{m=-l}^{l} \mathcal{Q}_{lm}\,Y_l^{m}(\theta,\phi),
$$

with the **spherical multipole moments**

$$
\mathcal{Q}_{lm} = \int \rho(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)\,r'^{\,l}\,Y_l^{m*}(\theta',\phi')\,d^3x' .
$$

The angular integration is over the source, and the moments $\mathcal{Q}_{lm}$ depend only on the source, not on the field point. Each order $l$ contributes $2l+1$ moments, transforming among themselves under a rotation of the coordinate frame as the representation $D^{(l)}$.

### The First Three Moments

The three lowest orders have their familiar names and their familiar Cartesian representatives.

**Monopole ($l = 0$).** The single moment is the total charge,

$$
ϙ = \int \rho(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)\,d^3x' ,
$$

and the monopole potential is $\Phi_{mon} = ϙ/(4\pi\epsilon_0 r)$.

**Dipole ($l = 1$).** The three moments are the components of the **dipole moment vector**

$$
\vec p = \int \rho(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)\,(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)\,d^3x',
$$

and the dipole potential is

$$
\Phi_{dip}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon_0}\,\frac{\vec p\cdot\vec u}{r^2}.
$$

**Quadrupole ($l = 2$).** The five independent moments are those of the **quadrupole tensor**

$$
\mathcal{Q}_{ij} = \int \rho(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)\left(3x_i'x_j' - r'^{\,2}\delta_{ij}\right)d^3x' ,
$$

which is symmetric, $\mathcal{Q}_{ij} = \mathcal{Q}_{ji}$, and traceless, $\mathcal{Q}_{ii} = 0$; those two conditions reduce the nine Cartesian entries to five. The quadrupole potential is

$$
\Phi_{quad}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon_0}\,\frac{1}{2r^3}\,\mathcal{Q}_{ij}\,\vec u_i\vec u_j .
$$

The tracelessness is not an extra assumption: the term proportional to $\delta_{ij}$ in $\mathcal{Q}_{ij}$ would contribute $\vec u_i\vec u_i = 1$ and hence a monopole-like $1/r$ tail, which is already accounted for by $ϙ$; removing the trace makes the quadrupole the pure $l = 2$ object. The relation of the Cartesian form to the spherical form is exact, and it has been checked directly: for a point charge, $\frac{1}{4\pi\epsilon_0}\frac{1}{2r^3}\mathcal{Q}_{ij}\vec u_i\vec u_j$ reproduces the $l = 2$ Legendre term $\frac{1}{4\pi\epsilon_0}\frac{r'^{\,2}}{r^3}P_2(\cos\gamma)$ term by term.

### The Tower and Its Ordering

The series is organized by increasing $l$. The potential falls off as $r^{-(l+1)}$, so at large distances each order is smaller than the one before by a factor of the source size over the distance, and the series is an expansion in that ratio. There is no largest $l$: the tower is **infinite**, and its infinity is a property of the angular structure of the fields, as the final article of this sequence examines.

## The Multipole Tower and the Rotation Group

### The Representations $D^{(l)}$

The rotation group $SO(3)$ has, up to equivalence, exactly one irreducible real representation of each odd dimension $2l+1$, $l = 0, 1, 2, \dots$; its double cover $SU(2)$ has exactly one irreducible complex representation of each dimension $2l+1$, written $D^{(l)}$ after Wigner's rotation matrices, so that $\dim_{\mathbb{C}}D^{(l)} = 2l+1$. The label $l$ is the angular momentum and $D^{(l)}$ is the standard rotation-group representation of that angular momentum; the representation-theory companion uses the letter $V$ for the polynomial modules of the complex algebra, a different family, and the present notation is the rotation-group one. In the biquaternion framework the rotation rotors are the real unit quaternions, a group isomorphic to $SU(2)$,

$$
\mathbb{H}_{\mathbb{B}}^1 = \{\tilde{U}\in\mathbb{H}_{\mathbb{B}} : \tilde{U}\tilde{U}^{\natural} = e_t\},
$$

acting on a vector by $\vec v\mapsto\tilde{U}\vec v\tilde{U}^{\natural}$. The multipole moment of order $l$ is a tensor in $D^{(l)}$: the monopole is $D^{(0)}$, the dipole is $D^{(1)}$, the quadrupole is $D^{(2)}$, and so on.

### Why the Order Is an Angular Momentum

The reason $l$ deserves to be called an angular momentum is that the moments are the coefficients of a function on the sphere, and the space of functions on the sphere carries the regular representation of the rotation group. Its decomposition is

$$
L^2(S^2) = \bigoplus_{l=0}^{\infty} D^{(l)} ,
$$

in which each $D^{(l)}$ occurs exactly once; the spherical harmonic $Y_l^m$ is its weight-$m$ basis vector, the eigenfunction of the rotation about the polar axis with eigenvalue $m$. The multipole expansion is therefore the decomposition of the field's angular dependence into irreducible rotation representations, and the order $l$ is the angular momentum carried by that angular dependence.

Two comments fix the interpretation. First, the tower is infinite because the space of functions on the sphere is **infinite-dimensional**: a function on $S^2$ has arbitrarily fine angular structure, and each finer scale is one more $D^{(l)}$. Second, the tower is a property of the **field**, which is a function of position; it is not a property of the algebra of values the field takes. That distinction becomes the whole content of the closing article, and it is already visible here.

## The Biquaternion Transcription of the Fields

### The Potential and the Field

In the $ict$ convention the four-potential is an element of the material sector,

$$
\tilde{A} = \frac{i\phi}{c}\,e_t + \vec A \in \mathbb{M}_- ,
\qquad \vec A = A_1\vec e_x + A_2\vec e_y + A_3\vec e_z ,
$$

whose scalar coefficient is imaginary and whose vector part is real. In the electrostatic limit $\vec A = 0$, and the four-potential reduces to the purely imaginary central element $(i\phi/c)\,e_t$, still an element of $\mathbb{M}_-$: the scalar part of a four-potential is imaginary, and it is that imaginary scalar coefficient that marks the sector. The constant factor $i/c$ plays no role in the statics, and it is convenient to work with the rescaled central element

$$
\tilde{\Phi} = \Phi\,e_t ,
$$

a real, Hermitian central element. It is not itself the four-potential — that is $(i\phi/c)\,e_t$ — but the scalar potential, and the gradients below are the same for either normalisation.

The spatial derivative operator is the vector part of the biquaternionic gradient,

$$
\vec\nabla = \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z ,
$$

so that $\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec\nabla$. Acting on a central element, $\vec\nabla$ produces a pure real vector,

$$
\vec\nabla(\Phi\,e_t) = (\partial/\partial Q_x\,\Phi)\vec e_x + (\partial/\partial Q_y\,\Phi)\vec e_y + (\partial/\partial Q_z\,\Phi)\vec e_z ,
$$

which is $-\vec E$ in biquaternion form: since $\vec E = -\vec\nabla\Phi$, the object computed is $\vec\nabla\Phi = -\vec E$, a pure real vector, an element of the vector part of $\mathbb{H}_{\mathbb{B}}$, and hence of $\mathbb{M}_-$.

**The spatial Laplacian.** A fact used twice below is that the second power of the vector gradient is minus the Laplacian,

$$
\vec\nabla\,\vec\nabla = \sum_{i,j}e_i e_j\,\partial^2/\partial Q_i\partial Q_j = -\sum_i \partial^2/\partial Q_i^2\,e_t = -\Delta\,e_t .
$$

The antisymmetric part of the quaternion product, $\sum_{i<j}(e_i e_j - e_j e_i)\partial^2/\partial Q_i\partial Q_j$, vanishes because the partial derivatives commute, so only the trace survives. This has been verified symbolically: for a quadratic potential $\Phi$ with Hessian $H$, the combination $\sum_{ij}e_i e_j\,H_{ij}$ equals $-\mathrm{tr}(H)e_t$ exactly, and the traceless symmetric part of the Hessian never appears.

### The Field-Strength Biquaternion

The field-strength biquaternion of the companion electromagnetic articles is

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H = \vec F,
\qquad \vec F = F_1\vec e_x + F_2\vec e_y + F_3\vec e_z ,
$$

a pure-vector biquaternion with vanishing scalar part, whose imaginary half carries the electric field and whose real half carries the magnetic field. In the electrostatic limit $\tilde{F} = i\sqrt{\epsilon}\,\vec E$. The conventions and the derivation are those of
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the definition of $\tilde{F}$ and the single field equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$.

For the multipole problem it is convenient to work with the real vector $\vec E$ itself, since the medium factors and the factor of $i$ play no role in the non-relativistic statics. The two objects are elements of the same kind: a real spatial vector is an element of the vector part, and the vector part is a faithful copy of $\mathbb{R}^3$ inside $\mathbb{H}_{\mathbb{B}}$.

## The Monopole and the Dipole as Algebra Elements

### The Monopole

The monopole moment is a scalar, and in the algebra it is the central element $ϙ\,e_t \in \mathbb{C}_{\mathbb{B}}$. Under a rotation the centre is pointwise fixed, which is the algebraic statement that the monopole is the $D^{(0)}$ representation. The monopole interaction energy $ϙ\Phi(0)$ is likewise a central scalar.

### The Dipole

The dipole moment is a vector,

$$
\tilde{p} = p_1\vec e_x + p_2\vec e_y + p_3\vec e_z ,
$$

a pure real quaternion with $\tilde{p}^{\natural} = -\tilde{p}$. Its representative lies in the vector part, which is exactly the $D^{(1)}$ representation, so the dipole is the first non-trivial multipole that is an **element of the algebra**. Two consequences follow.

**The dipole potential.** With the unit radial quaternion $\vec u = (x_1\vec e_x + x_2\vec e_y + x_3\vec e_z)/r$, satisfying $\vec u^2 = -e_t$, the dipole potential is

$$
\Phi_{dip} = -\frac{1}{4\pi\epsilon_0}\,\frac{\mathrm{Sc}\!\left(\tilde{p}\,\vec u\right)}{r^2},
$$

because $\mathrm{Sc}(\tilde{p}\vec u) = -\vec p\cdot\vec u$ for pure real vectors.

**The dipole interaction.** The energy of a dipole in an external electric field is $-\vec p\cdot\vec E$, and this is an algebraic pairing of two vector elements. For pure real vectors $\tilde{p}, \tilde E$ one has $\tilde{p}\tilde E = -\vec p\cdot\vec E + \vec p\times\vec E$, so

$$
-\vec p\cdot\vec E\,e_t = \mathrm{Sc}\!\left(\tilde{p}\tilde E\right)e_t = \tfrac12\left(\tilde{p}\tilde E + \tilde E\tilde{p}\right).
$$

The pairing is the **symmetrized product** of the two vectors, and its value is a central scalar. The dipole interaction is therefore fully internal to the algebra: both the moment and the field are elements, and their interaction is the scalar part of their product. The sign has been checked: $-\mathrm{Sc}(\tilde{p}\tilde E) = \vec p\cdot\vec E$ for real vectors, so $-\vec p\cdot\vec E = \mathrm{Sc}(\tilde{p}\tilde E)$.

The dipole is thus the first non-trivial multipole for which the moment is an algebra element and the moment–field coupling is an algebra product — the monopole is the trivial case, a scalar whose coupling $ϙ\Phi(0) = (qe_t)(\Phi e_t)$ is an algebra product too. The dipole is the model for what the algebra can do; the quadrupole is where that stops.

## The Quadrupole Tensor and Its Interaction

### The Moment as a Tensor

The quadrupole moment is not a vector but a symmetric traceless rank-two tensor,

$$
\mathcal{Q}_{ij} = \mathcal{Q}_{ji}, \qquad \mathcal{Q}_{ii} = 0, \qquad i,j = 1,2,3 ,
$$

with five independent components. It is the representation $D^{(2)}$ of the rotation group. Equivalently, it is a harmonic homogeneous polynomial of degree two in the direction cosines, $\mathcal{Q}(\vec u) = \mathcal{Q}_{ij}\vec u_i\vec u_j$, or a linear combination of the five spherical harmonics $Y_2^m$. The three descriptions are the same object in three notations.

### The Quadrupole Potential

The potential of a quadrupole is the $l = 2$ term of the expansion,

$$
\Phi_{quad}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon_0}\,\frac{1}{2r^3}\,\mathcal{Q}_{ij}\,\vec u_i\vec u_j ,
$$

and it agrees exactly with the $l = 2$ Legendre term of the Coulomb kernel, as noted above. The fall-off is $r^{-3}$, one power faster than the dipole and two faster than the monopole.

### The Interaction Energy

The interaction energy of a bounded charge distribution with an external potential $\Phi_{ext}$ is $W = \int\rho\,\Phi_{ext}\,d^3x'$. Expanding $\Phi_{ext}$ about the origin,

$$
\Phi_{ext}(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z) = \Phi(0) - x_i' E_i(0) - \tfrac12 x_i'x_j'\,\partial/\partial Q_i\,E_j(0) + \cdots ,
$$

where $\vec E = -\vec\nabla\Phi$ is the external field. The quadratic term separates into a trace part and a traceless part once the second moments are written in terms of the quadrupole tensor,

$$
\int\rho\,x_i'x_j'\,d^3x' = \tfrac13\,\mathcal{Q}_{ij} + \tfrac13\,\delta_{ij}\int\rho\,r'^{\,2}d^3x' ,
$$

and the trace part contributes $-\tfrac16(\nabla\cdot\vec E)(0)\int\rho\,r'^{\,2}d^3x'$. For an external field whose own sources lie outside the distribution, $\nabla\cdot\vec E$ vanishes wherever the distribution sits and that term drops, leaving the standard multipole expansion of the interaction energy,

$$
W = ϙ\,\Phi(0) - \vec p\cdot\vec E(0) - \tfrac16\,\mathcal{Q}_{ij}\,\partial/\partial Q_i\,E_j(0) + \cdots .
$$

Separating off the trace term is what leaves the quadrupole entering the expansion through the traceless tensor $\mathcal{Q}_{ij}$ alone, and it is the same split that the representation-theoretic contraction below uses.

The identity was verified numerically on three point charges: with a quadratic external potential carrying a traceless Hessian, so that $\nabla\cdot\vec E = 0$, the direct energy $\sum_a ϙ_a\Phi_{ext}(x_a\,\vec e_x+y_a\,\vec e_y+z_a\,\vec e_z)$ and the three-term expansion agree to machine precision at every source size $a$ (residual at the roundoff floor, a relative $10^{-16}$) — an exact test, since a quadratic potential terminates the expansion at the quadrupole. The coefficient $-\tfrac16$ was then checked against a genuinely higher-order case: adding a cubic term to $\Phi_{ext}$, the residual of the three-term expansion falls off as the cube of the source size, $4.3\times10^{-3}, 1.2\times10^{-4}, 4.3\times10^{-6}, 1.2\times10^{-7}, 4.3\times10^{-9}$ at source scales $1, 0.3, 0.1, 0.03, 0.01$ — a ratio of $27$ per factor of three, the signature of a first error at the octupole. A wrong coefficient in the quadrupole term would have left a residual falling only as the square. The trace term was verified on the same charges by varying the Hessian trace: the direct energy differs from the source-free expansion by exactly $-\tfrac16(\nabla\cdot\vec E)(0)\int\rho r'^{\,2}d^3x'$, to machine precision, at $\nabla\cdot\vec E = -0.3, +0.7, -1.5$, the difference changing sign with $\nabla\cdot\vec E$.

Two features of the quadrupole term deserve emphasis, because they are what the algebra will and will not see.

**Only the traceless part of the field gradient matters.** Since $\mathcal{Q}_{ii} = 0$ and $\partial/\partial Q_i\,E_j = -\partial^2/\partial Q_i\partial Q_j\,\Phi$ is symmetric in $i,j$, the contraction $\mathcal{Q}_{ij}\partial/\partial Q_i\,E_j$ receives contributions only from the traceless symmetric part of the field-gradient matrix. Writing

$$
\partial/\partial Q_i\,E_j = \tfrac13\delta_{ij}\,\nabla\cdot\vec E + T_{ij},
\qquad T_{ii} = 0, \quad T_{ij} = T_{ji},
$$

the trace term drops against $\mathcal{Q}_{ii} = 0$. With the external field source-free at the location of the distribution, as assumed for the expansion above, the quadrupole interaction is therefore the pure contraction of two $D^{(2)}$ objects,

$$
W_{quad} = -\tfrac16\,\mathcal{Q}_{ij}T_{ij} = \tfrac16\,\mathcal{Q}_{ij}\,\partial^2/\partial Q_i\partial Q_j\,\Phi(0).
$$

**It is a scalar.** Like every interaction energy, $W_{quad}$ is a single number, hence an element of the centre $\mathbb{C}_{\mathbb{B}}$. The algebra has no difficulty with the *value* of the quadrupole interaction. Its difficulty is with the *moment*, and that is the subject of the next section.

## Why the Quadrupole Is Not an Algebra Element

### The Product of Two Vectors Stops at $D^{(1)}$

The biquaternion product of two spatial vectors is fixed by the quaternion relations. For pure real vectors $\vec q, \vec v$,

$$
\vec q\vec v = -\vec q\cdot\vec v + \vec q\times\vec v,
$$

a central scalar plus a vector. Equivalently, symmetrizing,

$$
\tfrac12\left(\vec q\vec v + \vec v\vec q\right) = -(\vec q\cdot\vec v)\,e_t ,
\qquad
\tfrac12\left(\vec q\vec v - \vec v\vec q\right) = \vec q\times\vec v.
$$

The dot product is the $D^{(0)}$ channel and the cross product is the $D^{(1)}$ channel. The **symmetric traceless** part of the tensor product $\vec q\otimes\vec v$ — which is the $D^{(2)}$ channel — never appears: the symmetrized quaternion product collapses it to the trace. In the language of representations,

$$
D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)} ,
\qquad 3\times 3 = 1 + 3 + 5 ,
$$

and the quaternion product projects onto the first two summands, discarding the third. A quadrupole is precisely a symmetric traceless tensor, so it is precisely what the product discards.

### The Algebra Contains Only $D^{(0)}$ and $D^{(1)}$

The same conclusion follows from the structure of the algebra itself. Under the rotor-conjugation action of the rotation group, $\mathbb{B}$ decomposes into the centre, spanned by $e_t$, and the vector part, spanned by $\vec e_x, \vec e_y, \vec e_z$. The centre is invariant, so it is $D^{(0)}$; the vector part transforms as a vector, so it is $D^{(1)}$:

$$
\mathbb{B} = D^{(0)}\oplus D^{(1)} \quad\text{(as a complex representation of the rotations)},
\qquad 1 + 3 = 4 .
$$

The weight spectrum confirms that nothing else can be present. For a rotation about the axis $\vec e_z$, the centre is fixed, $\vec e_z$ is fixed, and the combinations $\vec e_x\pm i\vec e_y$ are eigenvectors with phases $\exp(\mp i\theta)$. The algebra therefore contains states only of weights $0$ and $\pm1$, and a $D^{(2)}$ representation would require a state of weight $\pm2$. There is none. The character of the conjugation action has been computed directly and equals $2 + 2\cos\theta = \chi_0(\theta) + \chi_1(\theta)$, the sum of the spin-$0$ and spin-$1$ characters, with no $D^{(2)}$ term $\chi_2 = 1 + 2\cos\theta + 2\cos2\theta$. Since $-\tilde{U}$ acts on a vector exactly as $\tilde{U}$ does, the conjugation action factors through $SO(3)$ and can carry only integral angular momentum. In the normalisation in which the vector part carries weights $\pm1$ — that is, with the generator $J_3 = -i\tfrac12\mathrm{ad}_{\vec e_z}$ — the generator has the eigenvalue spectrum $\{0, 0, +1, -1\}$ on $\mathbb{B}$: a doubly degenerate zero, together with a single $+1$ and a single $-1$. A quadrupole, which would carry weight $\pm2$, has no place to sit.

### Where the Quadrupole Does Live

The quadrupole is a symmetric traceless tensor over the vector part, and the natural algebraic home is the **symmetric traceless square** of $D^{(1)}$,

$$
\operatorname{Sym}^2_0(D^{(1)}) \cong D^{(2)} ,
\qquad \dim_{\mathbb{C}}\operatorname{Sym}^2_0(D^{(1)}) = 5 ,
$$

which is a subspace of the tensor square $D^{(1)}\otimes D^{(1)}$ — equivalently of $\mathbb{B}\otimes\mathbb{B}$ — and not a subspace of $\mathbb{B}$. In coordinate terms, a quadrupole is the traceless part of a symmetric bilinear form $\mathcal{Q}(\vec u,\vec v)$ on the vector part. This is the precise sense in which the quadrupole is *outside* the algebra: it is a tensor built from two vectors, not a single element.

The same conclusion can be read off the second derivative. From $\vec\nabla\vec\nabla = -\Delta\,e_t$, the iterated gradient of a scalar potential is a pure central element: the product of the two gradient operators annihilates the traceless symmetric part of $\partial^2/\partial Q_i\partial Q_j\,\Phi$. The quadrupole angular information is carried by the scalar field $\Phi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ — which has arbitrary angular dependence — and by the tensor of its second derivatives, but it is invisible to the *product* of two gradient operators.

### The Invariant Statement

It is worth stating the conclusion in the form the physics demands. A multipole moment is an *invariant of the source*: an integral over the source, a functional of the charge distribution. It is not an element of the value algebra of the field. The moments of order $l = 0$ and $l = 1$ happen to coincide with the two irreducible pieces of the algebra — the centre and the vector part — and so can be written as single biquaternions. The moments of order $l \geq 2$ cannot: they are tensors, functionals of the source, or, equivalently, coefficients in the angular expansion of a scalar field. The quadrupole is the first moment at which the finite dimension of the algebra becomes visible in the physics.

This is not a defect of the framework. It is the same finite-dimensionality that the companion article on the Poisson bracket identifies as the obstruction to the canonical Heisenberg algebra inside $\mathbb{B}$:
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the trace obstruction that blocks the canonical bracket inside the finite-dimensional algebra.

The algebra is a **value algebra** of finite dimension, and it carries exactly the spin-$0$ and spin-$1$ content of a scalar and a three-vector. The multipole tower is a property of the **field space**, which is infinite-dimensional. The two are different objects, and no finite algebra can play the role of the infinite-dimensional function space. The closing article of this sequence turns that observation into a general statement.

## Summary

The static field of a bounded source is expanded in multipole moments, one order for each irreducible representation $D^{(l)}$ of the rotation group, with $2l+1$ moments per order. In the biquaternion framework the fields are elements of the algebra: the four-potential is $\tilde{A} = i\phi/c\,e_t + \vec A\in\mathbb{M}_-$ with an imaginary scalar coefficient, the scalar potential is obtained from its scalar part, the spatial gradient is the vector operator $\vec\nabla$, and the electrostatic field is a real vector.

The moments fall into two classes. The monopole is a central scalar and the dipole is a vector, so both are **elements of the algebra**, and the dipole interaction $-\vec p\cdot\vec E = \mathrm{Sc}(\tilde{p}\tilde E)$ is an algebra product. The quadrupole is a symmetric traceless rank-two tensor, the representation $D^{(2)}$, and it is **not** an algebra element: the quaternion product of two vectors, $\vec q\vec v = -\vec q\cdot\vec v + \vec q\times\vec v$, projects $D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)}$ onto $D^{(0)}\oplus D^{(1)}$ and discards the symmetric traceless part. The algebra, as a rotation representation, is $\mathbb{B} = D^{(0)}\oplus D^{(1)}$ and contains no weight-$\pm2$ state. The quadrupole's home is the symmetric traceless square $\operatorname{Sym}^2_0(D^{(1)})\cong D^{(2)}$, a subspace of $\mathbb{B}\otimes\mathbb{B}$.

The quadrupole **interaction** is a scalar and therefore lies in the centre: with the external field source-free at the source, $W_{quad} = -\frac16 \mathcal{Q}_{ij}T_{ij} = \frac16 \mathcal{Q}_{ij}\partial^2/\partial Q_i\partial Q_j\,\Phi(0)$, the contraction of two $D^{(2)}$ objects. The interaction energy is an element of the algebra even though the moment is not.

The multipole tower is infinite because the angular structure of a field on the sphere is infinite-dimensional; the algebra is finite because it is the value algebra of a two-state, four-vector structure. The first order at which the difference shows is the quadrupole.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \{Q_te_t\}$ | Centre of $\mathbb{B}$ (the scalars) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde{U}\in\mathbb{H}_{\mathbb{B}}^1$, $\tilde{U}\tilde{U}^{\natural} = e_t$ | Rotation rotor, acting on a vector by $\vec v\mapsto\tilde{U}\vec v\tilde{U}^{\natural}$ |
| $\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec\nabla$ | Biquaternionic gradient |
| $\vec\nabla = \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$ | Spatial vector gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta$ | d'Alembertian (series convention) |
| $\tilde{A} = i\phi/c\,e_t + \vec A$ | Four-potential, an element of $\mathbb{M}_-$ |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion |
| $\vec u = (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/r$ | Unit radial quaternion, $\vec u^2 = -e_t$ |
| $\mathrm{Sc}(\cdot)$ | Scalar (central) part |
| $\Phi$, $\Phi_{ext}$ | Scalar potential of the source, and an external potential; $\Phi_{mon}, \Phi_{dip}, \Phi_{quad}$ its multipole parts |
| $\rho$ | Charge density, the corpus convention for the bare $\rho$ |
| $\mathcal{Q}_{lm}, ϙ, \vec p, \mathcal{Q}_{ij}$ | Spherical, monopole, dipole and quadrupole moments |
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
