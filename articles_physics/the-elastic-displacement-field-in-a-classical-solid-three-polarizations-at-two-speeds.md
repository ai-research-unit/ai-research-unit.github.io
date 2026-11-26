# __The Elastic Displacement Field in a Classical Solid: Three Polarizations at Two Speeds__

## Introduction

The other sections of this subcategory classify classical effects by the spin of the carrier that produces them. The spin-zero effects are those of a structureless point: a central energy, a vector position, no internal direction. The spin-$\tfrac12$ effects are those of intrinsic magnetism, where the orientation is a rotor and not a direction. The other-spin effects are those of a quadrupole, where the object needed is a symmetric traceless tensor. This article supplies the missing case. **The configuration of a classical solid is a material vector, and the material vector is the spin-one carrier.** Its plane waves come in three polarizations, at two speeds, and the two speeds are fixed by the two Lamé moduli.

The claim is not that a three-component field has three modes because it has three components. A three-component field can be constrained to two, as the Maxwell field is; it can be given a mass and keep three, as the Proca field does. What the article shows is that the elastic field takes the second route for a reason the algebra names: **the triad of polarization directions is a basis of the adjoint**, the three-dimensional representation that the algebra carries on its own vector part, and the split of that triad by the wavevector into one longitudinal and two transverse directions is the split of the adjoint by a unit vector.

The article also records an asymmetry that is easy to miss. The displacement is spin one, and yet the spin-one piece of its *gradient* is not a dynamical variable. The gradient of a vector splits into a dilatation, a local rotation and a shear, of dimension $1$, $3$ and $5$. The elastic energy of an isotropic solid contains the first and the third and not the second. **A rigid infinitesimal rotation costs no elastic energy, so the spin-one piece of the gradient is a gauge direction, while the spin-one field itself is the mode that propagates.** The two statements agree because the rotation that is gauged away is exactly the rotation that acts on the polarization triad.

The treatment is classical and non-quantum throughout, in the setting fixed by the companion article *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*: time is carried by the central imaginary direction $ie_t$, positions and displacements are real pure quaternions in the material sector $\mathbb{B}_{\Phi}$, and the only bracket used is the Poisson bracket. No quantum constant appears anywhere in the article.

- Companion article *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*, for the non-relativistic configuration space and the placement of the scalar and vector quantities.
- Companion article *Rigid-Body Dynamics and the Biquaternion Rotor*, for the rotor and the inertia tensor, which are the spin-$\tfrac12$ and spin-two objects this article does not use.
- Companion article *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*, for the identification of the adjoint action with the spin-one representation and for the passage to the quantum field.
- Companion article *The Proca Equation in the Non-Quantum Limit*, for the massive vector field, which is the relativistic counterpart of the field treated here.
- Companion article *The Spin-One Fluid*, for the same triad read as a velocity field rather than as a displacement.
- Companion article *The Multipole Expansion and the Quadrupole Interaction in Biquaternionic Form*, for the shear, which is the quadrupole of the neighbouring section.

## The Displacement as a Vector

### Where the Field Sits

A solid is described by a displacement at each point, $\vec u(\vec r,t)=\sum_{\imath\in\{x,y,z\}}u_{\imath}(\vec r,t)\,\vec e_{\imath}$. The coefficient $u_{\imath}$ is real and the element is a pure quaternion, so the displacement lies in the vector part of the material sector, the same three directions that carry the position of a particle in the preceding articles. The difference is one of bookkeeping and not of kind: the spin-zero articles have one vector per trajectory, and this article has one vector per point of the body.

The scalar data are central, as they are everywhere in this subcategory. The mass density $\rho e_t$, the Lamé moduli $\lambda e_t$ and $\mu e_t$, the energy density and the dilatation are real multiples of the identity. The configuration is the vector, and the central scalars are the prices attached to it. That division is the central-scalar limit of the companion article, applied to a continuum instead of a particle.

### Why the Vector Is Spin One

A rotation acts on the algebra by the adjoint action $R_Q(\tilde X)=Q\tilde XQ^{*}$. On the vector part it acts by conjugation, it maps the three-dimensional space to itself, and it returns to the identity after $2\pi$: a material vector is a weight-one object. **The vector part of $\mathbb{B}_{\Phi}$ is the adjoint representation of the rotation algebra, and its real dimension is three.** The three directions $\vec e_{x},\vec e_{y},\vec e_{z}$ are the three states of the carrier, and the dimension is not an accident of three-dimensional space but the dimension of the representation the algebra carries.

This is the same identification that the article on integer-spin quantization makes for the polarization index of a massive vector field. The present article uses it in the classical, non-quantum limit, where the three states are the three directions in which a point of the solid can be displaced.

### What the Field Is Not

Three comparisons keep the claim honest. First, the displacement is not a connection. It is a measurable field, a distance the material has moved, and it has no gauge freedom of its own; only its gradient will turn out to have one. Second, the solid has a rest frame, the medium itself. There is therefore no Lorentz symmetry to organize the three states into a longitudinal and two transverse ones at the level of the field; the split appears only when a wavevector is chosen. Third, the field is not the Proca field. It carries no mass parameter and no second time derivative with a mass term; the price of its third polarization will be a modulus, not a mass.

## The Gradient and Its Three Pieces

### The Decomposition

Write $\partial_{\imath}$ for the derivative along $\vec e_{\imath}$ and $\theta=\sum_{\imath}\partial_{\imath}u_{\imath}$ for the dilatation. The gradient of the displacement splits into three irreducible pieces under the rotation group,

$$
\partial_{\imath}u_{\jmath}=\tfrac13\theta\,\delta_{\imath\jmath}+\Omega_{\imath\jmath}+\Sigma_{\imath\jmath},
$$

with the local rotation $\Omega_{\imath\jmath}=\tfrac12(\partial_{\imath}u_{\jmath}-\partial_{\jmath}u_{\imath})$ and the shear $\Sigma_{\imath\jmath}=\tfrac12(\partial_{\imath}u_{\jmath}+\partial_{\jmath}u_{\imath})-\tfrac13\theta\,\delta_{\imath\jmath}$. The two symmetric pieces are the strain, $\varepsilon_{\imath\jmath}=\Sigma_{\imath\jmath}+\tfrac13\theta\delta_{\imath\jmath}$, and $\Omega$ is the antisymmetric part.

| Piece | Object | Dimension | Spin | Elastic role |
|---|---|---|---|---|
| Dilatation | $\theta$ | $1$ | $0$ | Volume change; priced by the bulk modulus |
| Local rotation | $\Omega_{\imath\jmath}$ | $3$ | $1$ | Rigid rotation; priced by nothing |
| Shear | $\Sigma_{\imath\jmath}$ | $5$ | $2$ | Shape change at fixed volume; priced by the shear modulus |

The count is the tensor-square decomposition $3\otimes3=1\oplus3\oplus5$: nine gradient components, one scalar, three rotation components, five shear components. Only six of the nine are dynamical, and the three that are not are exactly the spin-one ones.

### The Two Products of the Algebra

The decomposition is visible in the algebra's own product. With $D=\sum_{\imath}\vec e_{\imath}\partial_{\imath}$ the vector-valued derivative, the two products of $D$ with the displacement are

$$
D\vec u=-\theta+\nabla\times\vec u,
\qquad
\vec u\,D=-\theta-\nabla\times\vec u,
$$

so that

$$
D\vec u+\vec u\,D=-2\theta\,e_t,
\qquad
D\vec u-\vec u\,D=2\,\nabla\times\vec u .
$$

The sum is a central scalar and the difference is a vector. **The algebra reaches the dilatation through its symmetric product and the local rotation through its antisymmetric product, and it reaches nothing else.** The shear is a symmetric traceless tensor, and a tensor of that kind is not an element of the algebra; it enters the theory through the invariant $\Sigma_{\imath\jmath}\Sigma_{\imath\jmath}$, which is a central scalar, and this is the reason the quadrupole belongs to the neighbouring section on other spins rather than to this one.

The sector placement follows the same lines. The divergence lands on $e_t$ and is Hermitian, so the dilatation is informational; the curl lands on the vector directions and is anti-Hermitian, so the local rotation is material. A solid in motion therefore exchanges the two sectors through its gradient, in the manner of the harmonic oscillator of this subcategory.

### The Energy Sees Two of the Three

The elastic energy density of an isotropic solid is a function of the strain alone,

$$
\mathcal{E}=\tfrac12\lambda\theta^{2}+\mu\,\varepsilon_{\imath\jmath}\varepsilon_{\imath\jmath}
=\tfrac12K\theta^{2}+\mu\,\Sigma_{\imath\jmath}\Sigma_{\imath\jmath},
\qquad
K=\lambda+\tfrac23\mu,
$$

with $K$ the bulk modulus. The cross term between $\Sigma$ and the trace vanishes because $\Sigma$ is traceless, and the local rotation does not appear at all.

**The energy is the price of volume change plus the price of shape change at fixed volume.** The bulk modulus prices the spin-zero piece and the shear modulus prices the spin-two piece. The spin-one piece of the gradient is free: a body rotated as a whole stores no energy, and neither does an infinitesimal rotation added locally. That is the elastic statement of a gauge freedom, and it is why a continuum with nine gradient components per point has six dynamical ones.

The stress is the derivative of the energy with respect to the strain, $\sigma_{\imath\jmath}=K\theta\,\delta_{\imath\jmath}+2\mu\Sigma_{\imath\jmath}$, and it inherits the same absence: no term carries $\Omega$.

## The Equation of Motion and the Two Speeds

### The Equation

The balance of momentum for a body of density $\rho$ with no body force is $\rho\,\ddot u_{\imath}=\sum_{\jmath}\partial_{\jmath}\sigma_{\imath\jmath}$. Substituting the stress and using the decomposition,

$$
\rho\,\ddot{\vec u}=\bigl(K+\tfrac13\mu\bigr)\nabla\theta+\mu\,\nabla^{2}\vec u
=\bigl(\lambda+\mu\bigr)\nabla(\nabla\cdot\vec u)+\mu\,\nabla^{2}\vec u .
$$

The equation is second order in time, and its symbol carries two branches. The Helmholtz decomposition $\vec u=\nabla\phi+\nabla\times\vec A$ with $\nabla\cdot\vec A=0$ separates them: the scalar potential obeys $\rho\ddot\phi=(K+\tfrac43\mu)\nabla^{2}\phi$ and the vector potential obeys $\rho\ddot{\vec A}=\mu\nabla^{2}\vec A$. A single branch would need one modulus; the isotropic solid has two, and it has two branches.

### The Plane Wave

Take a plane wave with a central phase and a vector amplitude,

$$
\vec u=\hat\epsilon\,e^{i\theta_{\mathrm{pwp}}},
\qquad
\theta_{\mathrm{pwp}}=(\omega/c)\,r'_t-2\pi\,\vec\nu\cdot\vec r,
\qquad
\hat\epsilon=\sum_{\imath}\epsilon_{\imath}\vec e_{\imath},
$$

in the convention of the companion articles: $r'_t=c\,t'$ is the temporal length, $t'$ the clock written $t$ below, $\vec\nu$ the wave number vector and $\vec k=2\pi\vec\nu$ the angular wavevector, so that $\theta_{\mathrm{pwp}}=\vec k\cdot\vec r-\omega t$. **The phase is central and the amplitude is material**: the frequency and the wavevector are central data, and the polarization is the only material direction the wave carries. Substitution gives

$$
\rho\omega^{2}\hat\epsilon=\mu k^{2}\hat\epsilon+\bigl(K+\tfrac13\mu\bigr)\vec k\,(\vec k\cdot\hat\epsilon).
$$

The wavevector is itself a material vector, so the equation compares vectors in one three-dimensional space and asks for the directions in which $\hat\epsilon$ is an eigenvector. There are two cases.

| Case | Condition | Dispersion | Speed | Count |
|---|---|---|---|---|
| Transverse | $\hat\epsilon\cdot\vec k=0$ | $\rho\omega^{2}=\mu k^{2}$ | $c_{T}=\sqrt{\mu/\rho}$ | $2$ |
| Longitudinal | $\hat\epsilon\parallel\vec k$ | $\rho\omega^{2}=\bigl(K+\tfrac43\mu\bigr)k^{2}$ | $c_{L}=\sqrt{(K+\tfrac43\mu)/\rho}$ | $1$ |

The transverse branch is doubly degenerate and the longitudinal branch is single. Three polarizations in total, at two speeds.

### The Triad Is the Adjoint

The three directions $\{\hat k,\hat e_{1},\hat e_{2}\}$ form an orthonormal basis of the adjoint, with $\hat k$ the unit vector along the wavevector and $\hat e_{1},\hat e_{2}$ spanning the plane orthogonal to it. **The polarization triad of the elastic wave and the weight basis of the adjoint are the same triad.** The single direction along $\hat k$ is the direction picked out by the wavevector, and it is the direction named by the index $k$ in the construction of the weight basis.

The split $3=1+2$ is therefore the split of the adjoint by a unit vector, and it has a reading in terms of symmetry. The transverse pair is degenerate because the rotations about $\hat k$ leave the wavevector fixed: the two transverse states form a doublet of the stability group of $\hat k$, and the degeneracy of their speed is that symmetry and not a coincidence of the moduli. The longitudinal state is a singlet of the same group. This is exactly the pattern that the Proca triad shows, and the elastic solid reproduces it without a mass.

## The Ratio of the Two Speeds

### One Number Sets the Split

The two speeds are not independent. Their ratio is fixed by one dimensionless number, the Poisson ratio $\nu=\lambda/[2(\lambda+\mu)]$, through

$$
\frac{c_{L}^{2}}{c_{T}^{2}}=\frac{\lambda+2\mu}{\mu}=\frac{2(1-\nu)}{1-2\nu}.
$$

The ratio increases monotonically with $\nu$ over the stability range $-1<\nu\le\tfrac12$. At $\nu=\tfrac14$ it is $\sqrt3\approx1.73$, and $\nu=\tfrac14$ is the value a lattice of central forces gives, the value for which $\lambda=\mu$. At $\nu=0.3$, a typical metal, it is $1.87$. The measured ratio in steel is about $1.8$, and the order of magnitude is the prediction.

Two consequences follow. First, **the ratio is bounded below and unbounded above**: it runs from $\sqrt{4/3}\approx1.15$ in the auxetic limit $\nu\to-1$, where the bulk modulus vanishes, to infinity as $\nu\to\tfrac12$. The longitudinal branch is always the faster one and the two branches never cross. Second, a measurement of the two speeds measures one number and one scale,

$$
\nu=\frac{c_{L}^{2}-2c_{T}^{2}}{2\bigl(c_{L}^{2}-c_{T}^{2}\bigr)},
\qquad
\frac{\mu}{\rho}=c_{T}^{2},
$$

so that the moduli are recoverable from the speeds but are not separately visible in them. The algebra fixes the count and the degeneracy; it fixes no number here.

### The Removal of the Third Polarization

The limit $\nu\to\tfrac12$ is the incompressible limit. The bulk modulus diverges, the longitudinal speed diverges with it, and the dilatation is driven to zero: the constraint $\nabla\cdot\vec u=0$ replaces the longitudinal branch.

**This is the classical image of the mechanism that removes a polarization from a constrained field.** In the massless vector field the third polarization is removed by a constraint at every speed; here it is removed by being pushed beyond every speed the medium can carry. The two statements differ in the parameter that does the removing, a constraint or a modulus, and they agree in the structure: what remains is the pair transverse to the wavevector, and the adjoint is reduced to its two-dimensional quotient.

The honest qualification is that an incompressible solid does not lose a mode from its equations; it loses it from the acoustic window. At any finite frequency the third branch is present, with a wavelength short compared with the scales the incompressibility approximation resolves. The statement of the section is a statement about the limit, and the corpus records it as such.

## What the Algebra Supplies and What It Imports

The algebra supplies the whole representation theory of the problem. It supplies the identification of the displacement with the adjoint, hence the count of three polarizations. It supplies the decomposition of the gradient into $1\oplus3\oplus5$, which is what makes the statement that only two of the three pieces carry energy statable at all. It supplies the split $3=1+2$ by the wavevector, hence the existence of one longitudinal and two transverse branches. And it supplies the degeneracy of the transverse pair as the symmetry of the stability group. All of that is present before any modulus is named.

The algebra supplies no number. The two speeds are two material constants, the bulk and shear moduli divided by the density, and the ratio of the speeds is a third combination of them. Nothing in $\mathbb{B}$ selects $\nu=\tfrac14$ over $\nu=0.3$; the central-force value is a property of a particular lattice and not of the algebra. **The pattern is the algebra's, and the numbers are the material's.**

The same division appears in the spin assignments of the subcategory. The dilatation is the content of the spin-zero section: a volume change is a central scalar and nothing else. The shear is the content of the section on other spins: it is the quadrupole of the strain, the symmetric traceless tensor that the algebra cannot hold as an element. The local rotation is spin one and is not a mode. The displacement is spin one and is the mode. **One carrier, one field, three polarizations, two speeds, and no free number in the counting.**

## Summary

The displacement of a classical solid is a real pure quaternion at each point, so its configuration is the vector part of the material sector, which is the adjoint representation of the rotation algebra and therefore the spin-one carrier. Its plane waves carry three polarizations, the three directions of a basis of the adjoint adapted to the wavevector: one longitudinal along $\hat k$ and two transverse in the plane orthogonal to it.

The gradient of the displacement splits as $3\otimes3=1\oplus3\oplus5$ into a dilatation, a local rotation and a shear. The isotropic elastic energy contains the dilatation and the shear and not the local rotation,

$$
\mathcal{E}=\tfrac12K\theta^{2}+\mu\,\Sigma_{\imath\jmath}\Sigma_{\imath\jmath},
$$

so the spin-one piece of the gradient is a gauge direction — a rigid rotation costs no energy — while the spin-one field itself is what propagates. The symmetric product $D\vec u+\vec u D=-2\theta e_t$ and the antisymmetric product $D\vec u-\vec u D=2\nabla\times\vec u$ are the algebra's access to the two pieces it can hold; the shear is reached only through its scalar invariant.

The two branches disperse as $\rho\omega^{2}=\mu k^{2}$ and $\rho\omega^{2}=(K+\tfrac43\mu)k^{2}$, so that

$$
c_{T}=\sqrt{\frac{\mu}{\rho}},
\qquad
c_{L}=\sqrt{\frac{K+\tfrac43\mu}{\rho}},
\qquad
\frac{c_{L}^{2}}{c_{T}^{2}}=\frac{2(1-\nu)}{1-2\nu}.
$$

The transverse speed is set by the shear modulus and the longitudinal speed by the bulk modulus plus four thirds of the shear modulus. The ratio is bounded below by $\sqrt{4/3}$ in the auxetic limit and diverges in the incompressible limit, so the longitudinal branch is always faster and the two branches never cross. In the incompressible limit the third polarization is pushed beyond every speed the medium carries, which is the classical image of the constraint that removes a polarization from a massless vector field.

The algebra supplies the count, the decomposition and the degeneracy; the material supplies the two moduli. The dilatation belongs to the spin-zero section, the shear to the section on other spins, and the displacement to this one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec u=\sum_{\imath}u_{\imath}\vec e_{\imath}$ | Displacement; a real pure quaternion in $\mathbb{B}_{\Phi}$ |
| $\partial_{\imath}$ | Derivative along $\vec e_{\imath}$ |
| $D=\sum_{\imath}\vec e_{\imath}\partial_{\imath}$ | Vector-valued derivative |
| $\theta=\nabla\cdot\vec u$ | Dilatation; spin zero |
| $\Omega_{\imath\jmath}=\tfrac12(\partial_{\imath}u_{\jmath}-\partial_{\jmath}u_{\imath})$ | Local rotation; spin one |
| $\Sigma_{\imath\jmath}=\tfrac12(\partial_{\imath}u_{\jmath}+\partial_{\jmath}u_{\imath})-\tfrac13\theta\delta_{\imath\jmath}$ | Shear; spin two |
| $\varepsilon_{\imath\jmath}=\Sigma_{\imath\jmath}+\tfrac13\theta\delta_{\imath\jmath}$ | Strain |
| $\lambda$, $\mu$ | Lamé moduli |
| $K=\lambda+\tfrac23\mu$ | Bulk modulus |
| $\rho$ | Mass density |
| $\nu=\lambda/[2(\lambda+\mu)]$ | Poisson ratio |
| $\mathcal{E}=\tfrac12K\theta^{2}+\mu\Sigma_{\imath\jmath}\Sigma_{\imath\jmath}$ | Elastic energy density |
| $\sigma_{\imath\jmath}=K\theta\delta_{\imath\jmath}+2\mu\Sigma_{\imath\jmath}$ | Stress |
| $\vec\nu$, $\vec k=2\pi\vec\nu$ | Wave number vector; angular wavevector |
| $\theta_{\mathrm{pwp}}=(\omega/c)r'_t-2\pi\vec\nu\cdot\vec r$ | Plane-wave phase |
| $\hat\epsilon$ | Polarization amplitude of unit norm |
| $c_{T}=\sqrt{\mu/\rho}$ | Transverse speed; two polarizations |
| $c_{L}=\sqrt{(K+\tfrac43\mu)/\rho}$ | Longitudinal speed; one polarization |
| $c_{L}^{2}/c_{T}^{2}=2(1-\nu)/(1-2\nu)$ | Ratio of the two speeds |
| $\nu=(c_{L}^{2}-2c_{T}^{2})/[2(c_{L}^{2}-c_{T}^{2})]$ | Poisson ratio from the two speeds |

## Further Reading

- A.-L. Cauchy, "Sur les équations qui expriment les conditions d'équilibre ou les lois du mouvement intérieur d'un corps solide, élastique ou non élastique," *Exercices de mathématiques* **3** (1828) 160–187, for the strain and the symmetric stress tensor.
- G. Lamé, *Leçons sur la théorie mathématique de l'élasticité des corps solides* (Bachelier, 1852), for the two moduli and the equations of the isotropic solid.
- S. D. Poisson, "Mémoire sur les équations générales de l'équilibre et du mouvement des corps solides élastiques," *Journal de l'École Polytechnique* **20** (1831) 1–174, for the ratio that bears his name and the molecular derivation of the moduli.
- A. E. H. Love, *A Treatise on the Mathematical Theory of Elasticity* (Cambridge, 1927), for the decomposition of the displacement gradient and the classical treatment of the two branches.
- L. D. Landau and E. M. Lifshitz, *Theory of Elasticity* (Pergamon, 1986), for the elastic energy as a function of the two invariants of the strain and for the speeds $c_{T}$ and $c_{L}$.
- K. Aki and P. G. Richards, *Quantitative Seismology* (University Science Books, 2002), for the measurement of the two speeds and the inversion for the Poisson ratio.
- C. Truesdell and W. Noll, *The Non-Linear Field Theories of Mechanics* (Springer, 2004), for the role of the local rotation as a non-dynamical field in the linear theory.
- I. S. Sokolnikoff, *Mathematical Theory of Elasticity* (McGraw-Hill, 1956), for the displacement formulation and the derivation of the two branches from the single vector equation.
- H. Weyl, *The Classical Groups* (Princeton, 1939), for the decomposition $3\otimes3=1\oplus3\oplus5$ and the invariants of a symmetric traceless tensor.
- A. J. M. Spencer, *Continuum Mechanics* (Longman, 1980), for the isotropic representation of the elastic energy and the reduction of the constants from twenty-one to two.
- M. A. Biot, *Mechanics of Incremental Deformations* (Wiley, 1965), for the treatment of the rigid-rotation piece as a gauge direction in the linearized theory.
