# __Cosmology under the Biquaternion Framework — A Research Agenda__

## Introduction

This article is an agenda, not a result. It asks what it would take for the biquaternion framework to carry a cosmology, and it answers with a separation rather than a claim: which of the standard cosmological constructions — the FLRW line element with its scale factor and spatial curvature, the Friedmann equations and the equation of state that closes them, and the cosmological constant — the framework can reach, and what object or computation would close each gap. **No scale factor, no Hubble rate, and no equation of state is derived here; none exists in the framework.** The article says so at every point where a carried standard metric might be mistaken for a framework result.

The evidence base is the framework's established articles, in the order of the read list: the algebra and its two sectors, the material and informational spaces, *Curved Spacetime and the Biquaternion Framework* (the frame route and its boundary), *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* (the dynamics, to whose central question the Friedmann equations belong), and *The Partition Function in Biquaternionic Form* (the framework's thermodynamics). Two features of the evidence shape everything below. First, the framework's relation to gravity is kinematic: it carries any Lorentzian metric in a frame field and determines none, so it carries any FLRW metric and selects no scale factor. Second — the point this article adds to that picture — the framework's invariants are **rank-two**. The trace formula is a fibre trace over the two-dimensional qubit operator space; the cosmological source the Friedmann equations need is a symmetric rank-two tensor; and the framework's natural bilinear packaging of a rank-two tensor collapses to its trace. The first feature is why the FLRW metric can be written at all; the second is why the Friedmann equations cannot yet be sourced.

**The three-way classification.** Every item below is sorted into one of three kinds, following the gravitational agenda.

| Kind | Meaning |
|---|---|
| **Established** | Recomputed in the series and inherited here |
| **Obstacle with a known route** | The object does not exist, but the computation that would produce it is identifiable |
| **Obstacle with no route yet** | No mechanism has been proposed; naming an object is not a route to it |

**Conventions.** The notation of the read-list articles is inherited without change. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and scalar imaginary $i$ commuting with every $e_k$. The material and informational sectors are the anti-Hermitian and Hermitian subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the centre. The material basis is $\varepsilon_0 = ie_0$, $\varepsilon_k = e_k$, with $\eta_{\mu\nu} = \langle\varepsilon_\mu,\varepsilon_\nu\rangle = \mathrm{diag}(-1,1,1,1)$ and bilinear form $\langle\tilde{Q},\tilde{P}\rangle = \mathrm{Sc}(\tilde{Q}\bar{\tilde{P}})$. Real coordinates are $x^\mu = (ct,x,y,z)$; a four-vector of $\mathbb{M}_-$ is $\tilde{X} = X^\mu\varepsilon_\mu$; the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$. The trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. The frame field is $\tilde{E}_\mu \in \mathbb{M}_-$ with $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$. Standard cosmology's $a(t)$, $k$, $H$, $\rho$, $p$, $w$, and $\Lambda$ are **not** framework objects; they are written where the standard constructions are named as targets, and the framework supplies none of them. Nothing inherited is renamed or rederived.

## The Constructions Cosmology Would Require

Cosmology is a specific application of gravity, and it is worth stating the application precisely so that the gaps can be located. The standard constructions are three, and each is a target here rather than a framework result.

**The FLRW line element and its two functions.** A homogeneous and isotropic universe is described by the Friedmann–Lemaître–Robertson–Walker line element

$$
ds^2 = -c^2\,dt^2 + a(t)^2\left[\frac{dr^2}{1-kr^2} + r^2\,d\Omega^2\right],
$$

with two functions: the **scale factor** $a(t)$, which carries the expansion, and the **spatial-curvature parameter** $k \in \{-1,0,+1\}$, which selects the open, flat, or closed spatial geometry. This is standard cosmology, not framework content. It is the metric the framework's carrier would have to be able to write.

**The Friedmann equations, and what closes them.** Evaluating the Einstein equations on that metric gives

$$
H^2 \equiv \left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3c^2}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3},
\qquad
\frac{\ddot a}{a} = -\frac{4\pi G}{3c^2}\left(\rho + 3p\right) + \frac{\Lambda c^2}{3},
$$

where $\rho$ and $p$ are the energy density and pressure of the cosmic source. These are the Einstein equations on a homogeneous and isotropic ansatz; they inherit whatever status the Einstein equations have in the framework, no more and no less. Two of the three functions $a$, $\rho$, $p$ are fixed by them, and the system is **closed by an equation of state**, usually $p = w\rho$, together with the conservation law $\nabla_\mu T^{\mu\nu} = 0$. The source is the perfect-fluid stress–energy tensor

$$
T_{\mu\nu} = \left(\rho + p\right)\frac{u_\mu u_\nu}{c^2} + p\,g_{\mu\nu},
$$

a **symmetric rank-two tensor** of ten independent components. The framework's relation to this object is the second theme of the article.

**The cosmological constant.** $\Lambda$ enters the Friedmann equations as a term. The point that matters for an agenda is its logical status: in the standard theory $\Lambda$ may be read as a **parameter** of the field equation, fixed by observation, or as a **constant of integration**, arising from the trace-free (unimodular) part of the equations with its value undetermined by the local dynamics. Neither reading makes it a prediction of a theory. The framework has neither reading available, and the article records that as a gap rather than as a result.

## What the Framework Already Reaches

### The FLRW metric is carried by a frame, and nothing selects it

The frame route of *Curved Spacetime and the Biquaternion Framework* carries an arbitrary Lorentzian metric: four fields $\tilde{E}_\mu \in \mathbb{M}_-$ with

$$
g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle,
$$

and any Lorentzian metric is representable locally, because a $g$-orthonormal frame can be mapped into $\mathbb{M}_-$ by a pointwise linear isometry of quadratic spaces of the same signature. An FLRW metric is a Lorentzian metric, so it is representable. The representation is explicit for the flat-slice case. With a lapse $N(t)$ and scale $a(t)$,

$$
\tilde{E}_0 = i\,N(t)\,e_0, \qquad \tilde{E}_i = a(t)\,\sigma_i(x),
$$

where $\sigma_i$ spans $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ with $\langle\sigma_i,\sigma_j\rangle = \gamma_{ij}$, one has $g_{\mu\nu} = \mathrm{diag}(-N^2, a^2\gamma_{ij})$. For the flat spatial slice $\gamma_{ij} = \delta_{ij}$ and the choice $\tilde{E}_0 = ie_0$, $\tilde{E}_i = a\,e_i$, the Gram matrix is exactly

$$
\langle\tilde{E}_\mu,\tilde{E}_\nu\rangle = \mathrm{diag}\left(-1, a^2, a^2, a^2\right),
$$

recomputed here from the inherited bilinear form. This is the FLRW metric with $k=0$ and arbitrary scale factor, carried in the algebra's own operations.

Three qualifications belong to the statement, and they are the whole of its content.

- **Carrying is not deriving.** The scale factor $a(t)$ is a function the frame is *given*; the algebra produces no value for it, no equation for it, and no reason to prefer the FLRW form over any other metric. Every Lorentzian metric is representable, so the construction excludes nothing and selects nothing.
- **The scale factor is not computed.** The verified identity $\langle\tilde{E}_\mu,\tilde{E}_\nu\rangle = \mathrm{diag}(-1,a^2,a^2,a^2)$ is a consistency check on the carrier. It is a statement about the algebra's bilinear form, not a cosmological prediction.
- **The curved spatial slice is a separate step.** For $k \neq 0$ the spatial metric $a^2\gamma_{ij}$ is not flat, and the frame $\sigma_i$ with $\langle\sigma_i,\sigma_j\rangle = \gamma_{ij}$ must be built pointwise by a linear isometry from the constant-curvature tangent space into $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$. This is a finite-dimensional linear-algebra construction at each point, and it is the first item of the next section.

### Isotropy has a home in the algebra; homogeneity does not

The FLRW assumptions are imposed symmetries, and the two of them have different status in the framework.

**Isotropy is available.** The isotropy group about a point is $SO(3)$, and the algebra contains its double cover: the unit real quaternions in $\mathbb{H}_{\mathbb{B}} \subset \mathbb{B}$. A unit real quaternion $\tilde{\rho}$ acts on $\mathbb{M}_-$ by rotor conjugation $\tilde{X} \mapsto \tilde{\rho}\tilde{X}\tilde{\rho}^\dagger$ and preserves $\langle\cdot,\cdot\rangle$. The isotropy hypothesis therefore has an exact algebraic form: it is the statement that the spatial frame $\tilde{E}_i$ is equivariant under that action, so that the spatial metric it induces is the invariant $\gamma_{ij}$. This is a real, if modest, piece of framework content.

**Homogeneity is not available.** Homogeneity is a statement about the three-parameter translation group acting transitively on the spatial slices, and it is a statement about the manifold, not about the tangent space at a point. The algebra is pointwise — it has no notion of two distinct points, and separation enters only as a difference $\tilde{X}_1 - \tilde{X}_2$ — so it contains no translation group and, like $\mathrm{Diff}(M)$, no counterpart of homogeneity. The FLRW assumption therefore divides cleanly: isotropy can be expressed, homogeneity has no algebraic home. This asymmetry is a structural finding, not a technical gap.

### The framework's own local structure cannot write a scale factor

The framework's own proposal for locality is the local scale $c = 1/\sqrt{\epsilon\mu}$ of the imaginary time axis, not the frame. In its derivative-rule reading (Reading B of *Curved Spacetime and the Biquaternion Framework*) it produces

$$
g_{\mu\nu} = \mathrm{diag}\left(-u(\mathbf{x})^2, 1, 1, 1\right), \qquad u = c,
$$

a class with one free function, no shift, and **flat spatial slices** $g_{ij} = \delta_{ij}$. Two consequences were recomputed here.

- **A time-dependent local $c$ produces no expansion.** For $u = u(t)$, the metric $g = \mathrm{diag}(-u(t)^2,1,1,1)$ is **flat**: the substitution $d\tau = u(t)\,dt$ turns it into $-d\tau^2 + d\mathbf{x}^2$, and a direct computation for $u = 2 + \sin t$ gives an identically vanishing Riemann tensor. A "local scale on the imaginary time axis" is a reparametrisation of time; it cannot produce a scale factor or a Hubble rate, because the spatial metric is untouched.
- **A spatially varying local $c$ produces curvature, but not an FLRW metric.** For $u = u(\mathbf{x})$ the class is genuinely curved — recomputed here on the independent case $u = 2 + \cos y$, where the Riemann tensor is nonzero, a statement independent of the Riemann sign convention, and the parent's closed forms read $R_{00} = -u\,\Delta u$, $R_{ij} = \partial_i\partial_j u/u$, $R = 2\,\Delta u/u$ in the parent's sign convention — but the spatial slices remain flat, $g_{ij} = \delta_{ij}$, so no member is FLRW with a non-constant scale factor or non-zero spatial curvature. Within the class, Ricci-flatness forces $u$ to be affine in the spatial coordinates and the metric to be flat (the parent's result). An independent recomputation in the opposite Riemann sign convention reproduces the same magnitudes with every sign flipped; the convention choice is recorded in the companion.

The conclusion is a negative but an exact one: **the framework's own locality device cannot produce the FLRW line element.** If a cosmological metric enters the framework, it enters by the frame route, which abandons the local complex structure as the carrier of curvature.

### The two-sector decomposition survives pointwise

The decomposition $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ is a pointwise decomposition and survives on any background; the informational sector's elements become fields of Hermitian operators without difficulty. What does not survive is the trace: the trace in $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is a $2\times2$ fibre trace, with no volume element and no measure. This is the structural reason the informational sector has no curved-space field theory, and it is where the cosmological thermodynamics fails; it is stated in *Curved Spacetime and the Biquaternion Framework* and inherited here unchanged.

### The framework's thermodynamics is rank-two

*The Partition Function in Biquaternionic Form* reaches a definite and honest set of results, and its boundary is exactly where cosmology needs it to continue.

For a Hermitian Hamiltonian $\tilde{H} = h_0e_0 + i\mathbf{h} \in \mathbb{M}_+$, the thermal operator is a scalar Boltzmann weight times a boost biquaternion, and the trace formula gives

$$
Z = \mathrm{Tr}\left(e^{-\beta\tilde{H}}\right) = 2\,\mathrm{Sc}\left(e^{-\beta\tilde{H}}\right) = 2e^{-\beta h_0}\cosh\left(\beta|\mathbf{h}|\right),
$$

the ordinary partition function of a **two-level system** with energies $h_0 \pm |\mathbf{h}|$. Recomputed here: the closed form equals the sum of the two Boltzmann weights to machine precision, the observable has exactly two eigenvalues, and the entropy is $S = \log 2 + \log\cosh x - x\tanh x$ with $x = \beta|\mathbf{h}|$, which takes its **maximum value $\log 2$ at $x = 0$** and decreases thereafter. That maximum is the entropy of a two-state system. It is not the entropy of a field, and it cannot become one: the number of states is the rank of the $2\times2$ fibre, which is two.

This is the **rank-two limitation** in its first sense. The framework's thermal invariants are invariants of a finite, two-dimensional operator algebra: a state, an observable, a partition function, an entropy, and a heat capacity, all of a single qubit. They are not the thermodynamic quantities cosmology uses.

- There is no field-theoretic partition function. A cosmology needs the thermodynamics of a continuum — a radiation bath with a density of states growing with energy, an entropy density proportional to $T^3$, an energy density proportional to $T^4$ — and a finite two-level system has none of these. The framework's entropy saturates where a field's diverges.
- There is no thermodynamic limit and no volume. The trace has no integral and no metric measure, so no density, no pressure, and no extensive quantity can be formed from it.
- There is no equation of state. The two-level state supplies no relation $p = w\rho$; indeed it supplies no $p$ and no $\rho$ as separate quantities, only the eigenvalue splitting.

What the partition-function article establishes is therefore a genuine and carefully bounded result: the framework's thermodynamics is the thermodynamics of a qubit, and it reaches none of the thermodynamic quantities a homogeneous cosmology requires. The cosmological thermodynamic quantities are not "not yet computed"; at present they have no carrier.

## The Obstacles, and What Would Settle Them

Each obstacle is stated with what is known, what is open, and the computation that would close it.

### Obstacle with a known route: the spatial-curvature frame

*Known:* the frame carries the $k=0$ FLRW metric exactly, and the pointwise linear-algebra construction of a frame for a constant-curvature slice is standard. *Open:* an explicit $\mathbb{M}_-$-valued frame $\tilde{E}_i$ with $\langle\tilde{E}_i,\tilde{E}_j\rangle$ equal to a constant-curvature $a^2\gamma_{ij}$, and its consistency in the two steps the route needs. *Would settle it:* the object is a pointwise linear isometry from the tangent space of a constant-curvature three-manifold, with its form of signature $(3,0)$, into $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ with the restricted form $\mathrm{diag}(1,1,1)$; the computation is to build it and verify the Gram matrix for $k=\pm1$. This is a finite-dimensional construction at each point and should close promptly. A negative result — that the pointwise isometry exists but cannot be glued into a frame with the required differentiability — would itself be a finding about the carrier, not a failure of the arithmetic.

### Obstacle with a known route: transcribing the Friedmann equations

*Known:* the Einstein equations are the framework's central open question, treated in the companion agenda; the Friedmann equations are that question on a homogeneous and isotropic ansatz, and the algebraic steps from the ansatz to the equations are standard. *Open:* whether the framework reproduces them, which it cannot do more strongly than it reproduces the Einstein equations themselves. *Would settle it:* the object is the same action of the gravitational agenda, restricted to the FLRW ansatz; the computation is to evaluate its variation on that ansatz and check the two equations, including the conservation law $\nabla_\mu T^{\mu\nu} = 0$ that closes them. Until that action exists, the Friedmann equations in this framework can only be *transcribed* — written in the framework's notation on a carried FLRW metric — and a transcription is not a derivation. Stating them as derived would be exactly the promotion the gravitational agenda exists to prevent.

This obstacle inherits a hard ceiling: because the framework has not derived the Einstein equations, it has not derived the Friedmann equations, and no cosmological result can be reported as a framework result while that remains so. The agenda's contribution is to say where the cosmological case sits in that structure, not to break the ceiling.

### Obstacle with no route yet: the cosmological source in rank-two form

This is the obstacle specific to cosmology, and it is where the framework's invariant structure bites.

The Friedmann equations require the **perfect-fluid stress–energy tensor**, a symmetric rank-two tensor with two independent thermal functions $\rho$ and $p$ and a four-velocity. The framework's objects are different in kind. The natural packaging of a symmetric rank-two tensor into the algebra is the bilinear sum

$$
\tilde{T} = \sum_{\mu\nu} T_{\mu\nu}\,\varepsilon_\mu \bar{\varepsilon}_\nu ,
$$

and its behaviour is the framework's most important structural limitation for cosmology. Recomputed here on a general symmetric $T_{\mu\nu}$,

$$
\sum_{\mu\nu} T_{\mu\nu}\,\varepsilon_\mu\bar{\varepsilon}_\nu = \left(\eta^{\mu\nu}T_{\mu\nu}\right) e_0 ,
$$

so the packaging collapses to the **trace** and annihilates the vector part; and for a traceless symmetric object it vanishes identically. The consequences for the cosmological source are immediate and sharp.

- **A perfect fluid collapses to its trace.** In the fluid rest frame, $T_{\mu\nu} = \mathrm{diag}(\rho, p, p, p)$, so the packaging gives $(-\rho + 3p)\,e_0$. The separate functions $\rho$ and $p$ — which the Friedmann equations need as independent inputs — are replaced by the single combination $-\rho + 3p$, and the fluid's four-velocity and any anisotropic stress are discarded.
- **A radiation source vanishes.** For radiation, $p = \rho/3$, and $-\rho + 3p = 0$. The framework's natural packaging of a radiation-dominated cosmological source is **zero**, by the same collapse that annihilates the transverse-traceless amplitudes and the traceless quadrupole moment in the gravitational agenda. A radiation era is exactly what a hot early universe is made of.

*Open:* a carrier for the symmetric rank-two content that does not collapse to the trace — the same missing object the gravitational agenda names for the quadrupole moment and the transverse-traceless amplitudes. *Would settle it:* the object is an equivariant bilinear map from the fields the framework can carry into the representation $(1,1)\oplus(0,0)$ of the Lorentz group, with the trace part and the traceless part carried separately; the computation is to construct it and check that (i) it is equivariant under the local rotor action, (ii) its trace reduces to the packaging above, and (iii) its traceless part reproduces a supplied $\rho$ and $p$ rather than annihilating them. A no-go — a proof that no such map exists within the algebra's operations — would be an equally complete result, and would mean that a homogeneous cosmology cannot be sourced from within $\mathbb{B}$ at all.

### Obstacle with no route yet: the thermodynamic quantities cosmology needs

*Known:* the framework's thermodynamics is the qubit thermodynamics of *The Partition Function in Biquaternionic Form* — a two-level partition function, an entropy bounded by $\log 2$, a Bloch-ball state, and a temperature that measures imaginary-time displacement. *Open:* every quantity a homogeneous cosmology uses: an energy density and a pressure as functions of temperature, a density of states, an entropy density, and the equation of state $p = w\rho$ that closes the Friedmann system. *Would settle it:* the object is a thermodynamic limit — a trace over a growing algebra, or an $\mathbb{M}_+$-valued field with an action and a measure — that turns the rank-two invariants into continuum densities; the computation is to construct that limit and verify that the resulting energy density and entropy are extensive and that a $p(\rho)$ relation follows. The obstacle is the same structural one the gravitational agenda records for the informational trace on a curved background: the trace has no measure, and no measure means no density. Until it is built, the equation of state is an input the framework cannot supply, and the Friedmann system cannot be closed from within it.

The rank-two limitation is worth stating in its full generality, because it is the article's main new observation. The trace formula is a trace over the **two-dimensional fibre** $\mathbb{C}^2$. Every scalar invariant the framework produces — the Born expectation value, the partition function, the entropy, the heat capacity, and the collapse of a rank-two tensor — is built from that trace. A continuum cosmology needs an integral over a three-dimensional spatial slice, and a two-dimensional fibre trace cannot become a three-dimensional integral by any operation inside the algebra. The framework's invariants are therefore index-like (a state count) where cosmology's are density-like (a count per unit volume), and the mismatch is not one of effort.

## The Cosmological Constant: A Term With No Reading Here

Standard cosmology treats $\Lambda$ in two ways, and the distinction matters because an agenda that blurred them would be making a claim the evidence does not support.

- **As a parameter.** $\Lambda$ is a term in the field equation, $G_{\mu\nu} + \Lambda g_{\mu\nu} = \tfrac{8\pi G}{c^4}T_{\mu\nu}$, with a value fixed by observation. In this reading it is an input, not a prediction.
- **As a constant of integration.** In the trace-free (unimodular) formulation, the trace-free part of the field equations does not involve $\Lambda$ at all; $\Lambda$ is an integration constant of the remaining trace equation, and its value is not determined by the local dynamics. In this reading $g_{\mu\nu}$ and $\Lambda$ are unchanged by a shift of the source's trace, which is the standard route by which the "cosmological-constant problem" is reformulated as a problem of initial data rather than of vacuum energy.

The framework has **neither reading available**, and this is a statement about what is built, not a judgement about which reading is right.

- There is no field equation, so there is no term in which a parameter $\Lambda$ could sit; and there is no trace-free structure to take, because the framework has no diffeomorphism-invariant action and no representation of $\mathrm{Diff}(M)$.
- There is no framework quantity with the dimensions and transformation properties of $\Lambda$. The black-hole thermodynamics article records the relevant structural fact: $\Lambda$ has dimensions of inverse length squared and does not scale with the metric, so it breaks the scaling homogeneity that produces the Smarr relation, and it must be promoted to an independent thermodynamic variable with a conjugate volume. The same observation applies here in a milder form: $\Lambda$ is a dimensionful parameter the algebra does not contain.
- There is no route from the two-sector structure to a value of $\Lambda$. Even in the most favourable case the framework could supply a term of the right form; it has no mechanism that would fix its magnitude, and no mechanism that would make it a prediction rather than an input.

*Would settle it:* the object is an action with a $\Lambda$-term generated by the algebra's own operations — equivalently, a demonstration that a shift of the source's trace is a symmetry of that action, which would make $\Lambda$ an integration constant in the framework's own terms; or, on the other side, a derivation of the parameter from a framework quantity. The computation is to construct the action and check the trace-shift invariance, and then to check that the resulting $\Lambda$ either vanishes by the algebra's structure, is fixed by it, or remains free. A result that leaves it free is not a failure — it would place the framework with the standard reading in which $\Lambda$ is an input — but it must be reported as such and not as a prediction. **A framework that says nothing about the value of $\Lambda$ has not explained dark energy.**

## The Two-Sector Structure at Cosmological Scale: One Speculation, Labelled

The two-sector decomposition $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ invites a cosmological reading: the material sector $\mathbb{M}_-$ carries the geometry and the sources, the informational sector $\mathbb{M}_+$ carries operators and states, and at cosmological scale one might imagine the two exchanged — the geometry of $\mathbb{M}_-$ sourced by the information content of $\mathbb{M}_+$, or the expansion driven by the growth of some $\mathbb{M}_+$-valued quantity. The framework's own articles invite this by naming a coupling between the sectors as the place where new physics could reside.

It is important to state what this is: **a speculation with no derivation.** It is labelled here as speculation and not advanced as a result. Three things are true of it, and they are worth writing down precisely.

1. **The framework supplies no coupling.** *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and *Introduction to the Biquaternion Universe* both state that beyond the Lorentz coupling by rotor conjugation there is no specified coupling between the sectors, and no equation of motion for $\mathbb{M}_+$-valued fields. *Curved Spacetime and the Biquaternion Framework* adds that on a curved background even the pointwise trace has no integral analogue. A coupling that sources geometry would have to be an equation of motion for fields in both sectors; none exists.
2. **The only coupling that exists is kinematic and does no cosmological work.** The rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ is a Lorentz transformation of the material sector by a unit-norm biquaternion; it preserves the metric and moves no energy, so it cannot source an expansion. Using it as a "coupling" would be a category error: it is a symmetry, not a source.
3. **A one-sector-sources-the-other mechanism would be visible if it existed.** Any genuine coupling would contribute to an effective $T_{\mu\nu}$ and hence to the Friedmann equations. Its absence is the absence of that contribution.

**What would settle the speculation.** Not a reinterpretation of existing structure, but a construction. The object is an action coupling an $\mathbb{M}_-$-valued field to an $\mathbb{M}_+$-valued field through an algebra-built term — a term that is not the Lorentz action and does not reduce to it — together with the computation of the stress–energy tensor it produces when varied with respect to the frame. The check is whether that $T_{\mu\nu}$ is (i) non-zero, (ii) of perfect-fluid form on the cosmological ansatz, and (iii) such that the induced Friedmann equations differ from the standard ones. If the induced source is proportional to the trace of an already-present fluid, the speculation adds nothing; if it is independent, it is a genuine cosmological prediction and should be computed and confronted with observation. A no-go — a proof that no such coupling term can be built, or that any such term is a total derivative — would settle it in the negative and would be as valuable as a construction. Note that the obstacle of the rank-two source stands in the way of this speculation as it stands in the way of everything else: any energy–momentum produced would still have to be carried in a form the algebra can hold.

## What Would Not Settle It: Two Overclaims

Two tempting statements would be failures of this article if it made them, and they are named so that they are not made.

- **"The extra sector is dark energy" (or dark matter).** This is the framework's most tempting cosmological overclaim, and it has no derivation of any kind behind it. There is no coupling, no source term, no equation of state, and no value; there is not even a constructed stress–energy tensor for an $\mathbb{M}_+$-valued field. The framework's own articles state that the informational sector has no dynamics beyond the operator algebra and no specified coupling. Asserting an identification with dark energy or dark matter without a derivation would be precisely the "fabricated premise" the QCD agenda warns against, in its cosmological form. What is true, and all that is true, is that the framework has a second sector whose cosmological role is unspecified.
- **"The framework predicts a scale factor or a Hubble rate."** It does not. The carrier writes $\mathrm{diag}(-1,a^2,a^2,a^2)$ for an arbitrary supplied $a(t)$; that is an identity about the bilinear form, not a prediction. No equation for $a(t)$ exists, and no framework quantity fixes $H$ or any of its observable consequences. Everything the article writes about $a$, $k$, $\rho$, $p$, and $\Lambda$ is standard cosmology used as a target, marked as such.

The gravitational agenda's no-upgrade rule applies here in the cosmological form: a carried metric must not be read as a derived solution, and a transcribed Friedmann equation must not be read as a framework result.

## Progress Short of the Derivation

The obstacles are not equally hard, and some can be worked without the action. The following ordering is this agenda's judgement of what is reachable, with each step's status recorded so that a partial advance is recognisable for what it is.

1. **Build the constant-curvature frame.** The pointwise linear isometry from a $(3,0)$ tangent space into $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$, with the Gram matrix checked for $k=\pm1$. This is the only item on the list that is purely algebra and can be closed immediately; it extends the carried FLRW metric from flat to curved spatial slices without touching the dynamics.
2. **Construct the rank-two carrier.** The equivariant bilinear map into $(1,1)\oplus(0,0)$ that does not collapse to the trace. Like the gravitational agenda's traceless carrier, this is independent of the action, and it is the precondition for sourcing the Friedmann equations at all — including for any radiation era, whose packaging currently vanishes. It is the natural place to search for a no-go, since the collapse to the trace is a strong constraint.
3. **Give the thermodynamic quantities a continuum limit.** A trace with a measure, or an $\mathbb{M}_+$-valued field with an action, producing energy and entropy densities and a $p(\rho)$ relation. This is the item that would let the Friedmann system be closed from within the framework rather than supplied from outside, and it is the same missing measure the curved-spacetime article records.
4. **Fix the status of $\Lambda$.** With an action available, check whether an algebra-built term of the required form exists; if it does, determine whether it is forced, free, or forbidden. This item cannot precede the action, but it does not require the full non-linear identity: a $\Lambda$-term in a linearised action would already fix whether $\Lambda$ has a reading here.
5. **Attempt the two-sector coupling.** Only after items 2 and 4, since a coupling's contribution to geometry would have to be carried and would have to be distinguished from a cosmological-constant term. The speculation of the previous section is settled here or nowhere.
6. **Derive the Friedmann equations from the action.** The cosmological reduction of the gravitational agenda's central question. It is last because it is not independent: if the Einstein equations are not derived, the Friedmann equations are not derived either.

Two disciplines apply to every item. First, each candidate result must be recomputed on a case chosen independently of the one that suggested it — a second spatial-curvature sign, a second equation of state, a second frame — because a carrier that works for $k=0$ or for dust has not been shown to work in general. Second, a carried or transcribed cosmological statement must not be reported as a framework result. That distinction is the standing content of this agenda, and the easiest way to lose it is to write one sentence too many.

## Summary

This agenda asked what it would take for the biquaternion framework to carry a cosmology, and it has recorded what the framework reaches and what it does not.

**What is established.** The frame route carries the FLRW metric exactly: with $\tilde{E}_0 = ie_0$ and $\tilde{E}_i = a\,e_i$ the Gram matrix is $\mathrm{diag}(-1,a^2,a^2,a^2)$ for an arbitrary supplied scale factor, recomputed here from the inherited bilinear form. Isotropy has an exact algebraic home, as the invariance of the spatial metric under the unit real quaternions in $\mathbb{H}_{\mathbb{B}}$. The two-sector decomposition survives pointwise on any background. The framework's thermodynamics is the qubit thermodynamics of *The Partition Function in Biquaternionic Form*: $Z = 2e^{-\beta h_0}\cosh(\beta|\mathbf{h}|)$, an entropy bounded by $\log 2$, and a temperature that measures imaginary-time displacement.

**What is only carried, and is not a derived cosmology.** The scale factor, the spatial-curvature parameter, the Friedmann equations, the perfect-fluid source, and the cosmological constant are all **standard cosmology used as targets**. No scale factor, no Hubble rate, and no equation of state is derived here or in the framework. The framework's own locality device is not the route: a time-dependent local $c$ gives a flat metric and cannot produce an expansion, and a spatially varying local $c$ gives curvature but only on flat spatial slices.

**The obstacles, and the computation that would close each.**

| Obstacle | Status | What would settle it |
|---|---|---|
| Constant-curvature spatial frame ($k=\pm1$) | Known route | The pointwise linear isometry into $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$, with the Gram matrix verified |
| Friedmann equations | Known route, blocked on the Einstein equations | The gravitational agenda's action, restricted to the FLRW ansatz |
| Cosmological source in rank-two form | **No route yet** | An equivariant bilinear into $(1,1)\oplus(0,0)$ that does not collapse to the trace; the present packaging sends a perfect fluid to $(-\rho+3p)e_0$ and a radiation source to zero |
| Thermodynamic quantities (densities, equation of state) | **No route yet** | A trace with a measure, or an $\mathbb{M}_+$-valued field with an action, giving extensive densities and a $p(\rho)$ relation; the present invariants are rank-two and bounded by $\log 2$ |
| Cosmological constant | **No route yet** | An algebra-built $\Lambda$-term, with its trace-shift status fixed; the framework offers neither the parameter nor the integration-constant reading |
| Two-sector cosmological coupling | **No route yet, and a speculation** | An algebra-built coupling term whose induced $T_{\mu\nu}$ is independent of any existing fluid; or a no-go |

**The article's central finding** is that the framework's cosmological difficulty is not merely the missing dynamics. It is also a mismatch of invariant structure: the framework's scalars are traces over a two-dimensional fibre, while cosmology's are densities and integrals over a three-manifold; and its natural packaging of a rank-two source collapses to the trace, so the two functions $\rho$ and $p$ that close the Friedmann equations are not carried, and a radiation fluid is annihilated entirely. The framework's own thermodynamics reaches the quantities a homogeneous cosmology does not use, and stops at $\log 2$, which is the entropy of a two-state system.

The speculations are labelled as such. One sector sourcing the other at cosmological scale has no derivation and no coupling; dark energy and dark matter are **not** explained by the extra sector; and no scale factor or Hubble rate is predicted. Stating any of these without a derivation would be the article's failure, and the agenda's value lies in leaving them visible as gaps rather than closing them with prose.

## Summary of Notation

| Symbol | Meaning | Introduced or inherited |
|---|---|---|
| $\mathbb{B}$ | $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the biquaternion algebra | inherited |
| $e_0,e_1,e_2,e_3$ | quaternion basis, $e_k^2 = -e_0$ | inherited |
| $i$ | scalar imaginary, commuting with every $e_k$ | inherited |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | material and informational sectors, $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ | inherited |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | real-quaternion subspace; centre $\mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | inherited |
| $\varepsilon_\mu$ | material basis $\varepsilon_0 = ie_0$, $\varepsilon_k = e_k$ | inherited |
| $\langle\tilde{Q},\tilde{P}\rangle$ | bilinear form $\mathrm{Sc}(\tilde{Q}\bar{\tilde{P}})$, $\langle\varepsilon_\mu,\varepsilon_\nu\rangle = \eta_{\mu\nu} = \mathrm{diag}(-1,1,1,1)$ | inherited |
| $\tilde{\nabla}$, $\bar{\tilde{\nabla}}$, $\Box$ | biquaternionic gradient, its conjugate, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | inherited |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | trace formula, a **fibre** trace over $\mathbb{C}^2$ | inherited |
| $\tilde{E}_\mu \in \mathbb{M}_-$, $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$ | frame field and the metric it carries | inherited |
| $a(t)$, $k$ | scale factor and spatial-curvature parameter — **standard cosmology, carried not derived** | standard notation |
| $H = \dot a/a$, $\rho$, $p$, $w$, $\Lambda$ | Hubble rate, density, pressure, equation-of-state parameter, cosmological constant — **standard cosmology, no framework reading** | standard notation |
| $\tilde{T} = \sum_{\mu\nu}T_{\mu\nu}\varepsilon_\mu\bar{\varepsilon}_\nu$ | natural packaging of a rank-two tensor; equals $(\eta^{\mu\nu}T_{\mu\nu})e_0$ | recomputed here from an inherited identity |
| $Z = 2e^{-\beta h_0}\cosh(\beta|\mathbf{h}|)$ | qubit partition function; entropy bounded by $\log 2$ | inherited from the partition-function article |
| $u = c = 1/\sqrt{\epsilon\mu}$ | local scale of the imaginary time axis, Reading B of the local-scale route | inherited |

## Further Reading

- *Introduction to the Biquaternion Universe* — the algebra, the two sectors, the local complex structure, and the sector-coupling open question this agenda inherits.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the material sector, the four-vectors, the bilinear form, and the interval.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the informational sector, the trace formula, the no-dynamics and no-coupling statements, and the entropy open question.
- *Curved Spacetime and the Biquaternion Framework* — the frame route, the local-scale route and its metric class, the two-sided covariant derivative, and the informational trace's missing measure; the parent of this agenda.
- *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* — the dynamics, the central non-linear question, and the settling object; the Friedmann equations belong to this agenda's central item and are not duplicated here.
- *The Partition Function in Biquaternionic Form* — the framework's thermodynamics, the qubit partition function, and the boundary this agenda finds the cosmological case against.
- *Quantum Thermodynamics in Biquaternionic Form* and *The KMS Condition and the Biquaternion Framework* — the thermal functionals and the imaginary-time structure behind the rank-two limitation.
- *Black Hole Thermodynamics in Biquaternionic Form* — the horizon and extended ($\Lambda$/$P$–$V$) thermodynamics, the scaling argument, and the $\Lambda$ correction to the Smarr relation.
- *The Wick Rotation in the Biquaternion Universe* — the transfer between $\mathbb{M}_-$ and $\mathbb{H}_{\mathbb{B}}$ that underlies the imaginary-time reading.
- *The Local Complex Structure and the Speed of Light* and *Electromagnetism in Media — The Local Complex Structure at Work* — the local $c$ whose cosmological readings are examined here.
- *Exercise: The Electromagnetic Energy–Momentum Tensor* and *The Field-Strength Biquaternion and Its Invariants* — the framework's rank-two constructions, relevant to the source-carrier item.
- *Noether's Theorem in Biquaternionic Form* — the conservation-law machinery any cosmological source would need.
- *Biquaternion Representation Theory* and *The Lorentz Group in Biquaternionic Form — Structure and Representations* — the $(1,1)\oplus(0,0)$ and $(\tfrac12,\tfrac12)$ bookkeeping behind the rank-two limitation.
- *The Conformal Group in Biquaternionic Form* — the conformal structures relevant to a radiation-dominated universe.
- *The Empirical Status of the Biquaternion Framework* — the standing empirical-equivalence result, under which any biquaternionic cosmology would labour.
- *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda* — the companion agenda whose three-way classification and fabricated-premise discipline this article follows.
