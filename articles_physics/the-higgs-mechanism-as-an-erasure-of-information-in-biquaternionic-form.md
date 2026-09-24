# __The Higgs Mechanism as an Erasure of Information in Biquaternionic Form__

## Introduction

The Higgs mechanism is the statement that a gauge symmetry which is exact in the action can be hidden by the vacuum, and that the hiding is not free. The scalar acquires a vacuum expectation value $\langle|\varphi|\rangle = v/\sqrt{2}$; the would-be Goldstone mode of the scalar, which the vacuum makes massless, is absorbed into the gauge field as its longitudinal polarization; and the gauge field acquires the mass $M_A = qv/\hbar$. The two events are one event, and the degree-of-freedom count records it: the symmetric phase has $2$ real scalar degrees of freedom and $2$ transverse gauge polarizations, the broken phase has $1$ real scalar and $3$ gauge polarizations, and $2+2 = 1+3$.

This article reads that mechanism information-theoretically. The word the title uses is **erasure**, and the article's central claim is that the word is exact in one sense and misleading in another, with the distinction being the whole content.

- The phase of the scalar is **erased from the observable description**. Before the breaking the scalar has two real fields, the radial and the angular; after the breaking the angular field is not an independent physical field, and the observable scalar is a single real field. In this sense a continuous label — the phase on the circle of minima — is removed from the list of things an observable can read.
- The information in the phase is **not destroyed**. It reappears as the longitudinal polarization of the gauge field, the degree of freedom that a massless vector does not have and a massive vector does. The total count is conserved and the mass $M_A$ is a gauge-invariant record of what the vacuum did.

The reason the two statements do not contradict each other is the subject of the companion article on gauge redundancy. The phase of the scalar is a **pure gauge direction**: a rotation of the phase is a gauge transformation, so two vacua differing by a phase are two descriptions of one configuration. What the Higgs mechanism erases is therefore a redundant label, not a physical degree of freedom. The erasure is of the description; the physics is re-encoded, reversibly, and leaves a record. This is what distinguishes the Higgs mechanism from confinement, the subject of the other companion: confinement removes partonic labels from the asymptotic algebra and leaves no gauge choice that recovers them, whereas the Higgs mechanism removes a gauge coordinate and records its effect in a mass.

The article proceeds as follows. The symmetric phase is set up with its circle of degenerate vacua, and the informational status of the phase is fixed. The erasure is then shown to be the elimination of a gauge direction, with the invariant content of the vacuum isolated. The relocation of the information into the longitudinal mode and the mass is then derived, with the mass coefficient recomputed on a generic connection. The symmetry-breaking map is read as a channel — unitary on the full degrees of freedom and many-to-one only on the gauge-invariant ones — and compared with the loss of confinement and with the redundancy of the gauge orbit. The vacuum is then read as a stable record, in the structure of einselection, and the Landauer comparison is drawn. A ledger separates the framework's own construction from the imports.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$, and central scalar imaginary $i$; the material sector is $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$; the centre is $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$. The gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The connection is $\tilde{A} = \sum_\mu A_\mu e_\mu = i\phi/c\,e_0 + \mathbf{A}\in\mathbb{M}_-$; it transforms as $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$; the coupling is $\kappa = q/\hbar$ with $D = \tilde{\nabla} + i\kappa\tilde{A}$ and $D_\mu = \partial_\mu + i\kappa A_\mu$. The scalar is the **complex central field** $\tilde{\Phi} = \varphi\,e_0$, $\varphi\in\mathbb{C}$. The amplitude symbol $\varphi$ is kept distinct from the connection's scalar potential $\phi$. The scalar part is $\mathrm{Sc}$, the trace is $\mathrm{Tr} = 2\,\mathrm{Sc}$, and $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. The $ict$ coordinates are $x_\mu = (ict,x,y,z)$, so $\partial_0 = \partial_{ict} = -i\partial_t/c$, and the Lorentz-invariant contraction of two four-vectors is $g^{\mu\nu}U_\mu^*V_\nu$ with

$$
g = \mathrm{diag}(-1,+1,+1,+1)
$$

on these coordinates, the same convention in which the Maxwell density is $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$. <!-- CONVENTION — metric levels: the $g$ written here is the LEVEL-2 $ict$-coordinate metric used for index contractions, not the LEVEL-3 Clifford metric $g = \mathrm{diag}(+1,-1,-1,-1)$ that defines the $\gamma^\mu$. The two are different objects at different levels; the appearance of $\mathrm{diag}(-1,+1,+1,+1)$ here is not a discrepancy with the Clifford convention and must not be "reconciled" with it. --> Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. The states of the informational sector are $\tilde{\rho}\in\mathbb{M}_+$ with $\mathrm{Tr}\tilde{\rho} = 1$, parametrized by the Bloch vector, $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$, $|\mathbf{r}|\leq1$; the relative entropy is $S(\tilde{\rho}\|\tilde{\sigma})$.

## The Symmetric Phase and the Information in Its Vacuum

### Two Real Fields and a Circle of Minima

The framework's scalar is the complex central field $\tilde{\Phi} = \varphi\,e_0$, and its gauge-invariant content is the single real combination $\varphi^*\varphi = \mathrm{Sc}[\tilde{\Phi}^\dagger\tilde{\Phi}] = |\varphi|^2$. Take the potential

$$
V(\varphi^*\varphi) = \beta\left(\varphi^*\varphi - \frac{v^2}{2}\right)^2,
\qquad \beta > 0,
$$

whose minimum is the **circle**

$$
|\varphi| = \frac{v}{\sqrt{2}} .
$$

Every point of the circle minimizes $V$, and no point is preferred by the action, which is invariant under the central phase $\varphi\mapsto e^{i\alpha}\varphi$. The vacuum is therefore a member of a **degenerate family** parametrized by the phase. Writing

$$
\varphi(\tilde{X}) = \frac{1}{\sqrt{2}}\bigl(v + h(\tilde{X})\bigr)e^{\,i\theta(\tilde{X})/v},
$$

with $h$ and $\theta$ real, exhibits the two real fields: $h$ the radial fluctuation, with mass $m_h^2 = 2\beta v^2$ from the curvature of the potential, and $\theta$ the angular fluctuation, with no potential term at all.

### The Informational Status of the Phase

Considered as a classical label, the phase is a continuum: the vacuum family is a circle at every point of spacetime, and a description that resolved $\theta(\tilde{X})$ point by point would carry the classical information of a function space — a continuum rather than a finite string of bits. If the phase were a physical observable, the choice of one vacuum would **erase** all of it, and the erasure would be a loss of a continuum and not of a record: a field with values on a circle, one at each point of spacetime, reduced to a single number, with no way to recover it from the broken phase.

Two facts of the framework make the actual situation different, and they are the reason the title's word needs the qualification this section supplies.

**The phase is not an observable.** The action is invariant under $\varphi\mapsto e^{i\alpha}\varphi$, and the action of the central phase on a state of the informational sector is trivial. The framework's sharpest statement of this is the one made in the gauge-orbit companion: a central phase acts on $\tilde{\rho}\in\mathbb{M}_+$ by $\tilde{\rho}\mapsto\lambda\tilde{\rho}\lambda^\dagger = |\lambda|^2\tilde{\rho} = \tilde{\rho}$, so it is not merely that no measurement distinguishes the phases — no Hermitian observable is conjugate to the phase at all. The phase is a **non-variable** of the informational sector.

**The gauge-invariant content of the vacuum is a single number.** Because $\varphi$ is central, the product $\tilde{\Phi}\tilde{\Phi}^\dagger = |\varphi|^2 e_0$ is the entire gauge-invariant content of the vacuum, and it is independent of the phase. This was checked for the generic complex value $\varphi = 0.8 - 0.35i$ under phase rotations $e^{i\alpha}$ for $\alpha = 0.3, 1.7, -2.2$: $\tilde{\Phi}\tilde{\Phi}^\dagger$ was unchanged to within $3\times10^{-16}$ in every case. The circle of vacua collapses, for every observable, to the single number $|\varphi| = v/\sqrt{2}$.

The two facts together give the article's first accounting. The phase direction carries no physical information, so the erasure of the phase from the observable description erases nothing physical. What the vacuum does carry — the magnitude $v$ — is untouched. The word "erasure" is therefore correct about the description and incorrect about the physics, and the remainder of the article locates the physics that is relocated rather than erased.

## The Flat Directions of the Potential

The information-theoretic reading of the erasure is sharpened by the curvature of the potential, which separates the directions of the vacuum into those that are recorded and those that are erased.

### The Hessian at the Minimum

Write the scalar in the two real fields, $\varphi = \frac{1}{\sqrt{2}}(v+h)e^{i\theta/v}$, so that

$$
\varphi^*\varphi = \tfrac{1}{2}(v+h)^2,
\qquad
V = \beta\left(\tfrac{1}{2}(v+h)^2 - \tfrac{v^2}{2}\right)^2
= \frac{\beta}{4}h^2(2v+h)^2 .
$$

The potential is a function of $h$ alone; the phase $\theta$ does not appear in it. Expanding about the minimum,

$$
V(h) = \beta v^2h^2 + \beta v\,h^3 + \frac{\beta}{4}h^4 ,
$$

so the Hessian at the minimum, in the coordinates $(h,\theta)$, is

$$
H = \begin{pmatrix} \partial_h^2V & \partial_h\partial_\theta V \\[2pt] \partial_\theta\partial_h V & \partial_\theta^2V \end{pmatrix}_{h=\theta=0}
= \begin{pmatrix} 2\beta v^2 & 0 \\ 0 & 0 \end{pmatrix}.
$$

The Hessian has rank one. The **massive direction** is the radial one, with $m_h^2 = 2\beta v^2$; the **flat direction** is the phase, with zero curvature. This was recomputed by finite differences: at $\beta = 1$ and $v = 1.3$, the second derivative of $V$ along $h$ came out as $3.38000000$ against the prediction $2\beta v^2 = 3.38000000$, while the curvature along $\theta$ is identically zero for every value of $\theta$, because $V$ does not depend on it.

### The Count of Records and the Count of Erased Labels

The rank of the Hessian and the dimension of its kernel are the two numbers the informational reading needs.

- The **rank** is the number of directions with a restoring force, hence the number of massive fields: here $1$, the radial mode. These are the directions in which the vacuum **records** a value — the mass is the record, and it is the same for every point of the vacuum family.
- The **kernel** is the number of flat directions, hence the number of would-be Goldstone modes: here $1$, the phase. These are the directions **erased** from the observable description, because they are the coordinates along which the vacuum is degenerate.

For a general breaking of a group $G$ to a subgroup $H$, the count is the standard one of the Goldstone theorem. The number of flat directions, and hence of erased labels, equals the number of broken generators, $\dim(G/H)$; for the abelian model $G = U(1)$ and $H = 1$, so $\dim(G/H) = 1$. The same number counts the gauge fields that become massive, since each broken generator supplies one, so the gauge-boson masses stand in bijection with the erased labels. The count of massive *scalar* directions is a different number: it is the number of real scalar components less the number of Goldstone modes, so $2 - 1 = 1$ for the abelian model — the single radial mode. The abelian model displays a coincidence of the two counts, not a general rule: a complex doublet in the electroweak pattern, where three generators are broken, leaves $4 - 3 = 1$ massive scalar direction against three erased labels. What a general breaking leaves as its record is therefore not one number but the gauge-field mass matrix together with the masses of the surviving scalars, and the open question of the non-abelian case is exactly whether the ranks of those matrices carry the same information here as they do in standard field theory.

The important point for the erasure reading is that the flat direction is not merely unrecorded but **unrecordable**: a flat direction has no curvature, so no restoring force and no mass, and a gauge coordinate has no observable, so no measurement. The two properties coincide because the phase is both flat in the potential and a gauge direction, and it is their coincidence that makes the erasure costless.

## The Erasure as the Elimination of a Gauge Direction

### The Unitary-Gauge Transformation

The elimination of the phase is an explicit gauge transformation. With the parametrization above, choose

$$
\Gamma(\tilde{X}) = -\,\frac{\hbar}{qv}\,\theta(\tilde{X}),
$$

so that the covariant phase factor is $e^{iq\Gamma/\hbar} = e^{-i\theta/v}$ and

$$
\varphi \;\longmapsto\; e^{iq\Gamma/\hbar}\varphi = \tfrac{1}{\sqrt{2}}(v+h)e^{i\theta/v}e^{-i\theta/v} = \tfrac{1}{\sqrt{2}}(v+h),
$$

real. This is the **unitary gauge** of the abelian model. In it the scalar is a single real field $h$, and the angular field $\theta$ has been removed from the scalar. The removal is effected entirely by a gauge transformation, which is what makes the erased object a redundant label: it is the coordinate along the gauge orbit of the vacuum, and the orbit's information content was fixed in the companion article to be nil.

### What the Transformation Does to the Connection

The same gauge transformation shifts the connection,

$$
A_\mu' = A_\mu - \partial_\mu\Gamma = A_\mu + \frac{\hbar}{qv}\,\partial_\mu\theta ,
$$

so that the combination

$$
\mathcal{A}_\mu := A_\mu + \frac{\hbar}{qv}\,\partial_\mu\theta
$$

is gauge invariant, and the mass term of the next section depends on it rather than on $A_\mu$ alone. The two terms are not separately physical. What appears as the removal of one field and the shift of another is a single gauge transformation; the erasure of $\theta$ and the modification of $A_\mu$ are the same operation seen from the two ends.

This is the precise sense in which the Higgs mechanism **uses** the gauge redundancy rather than suffering it. In the companion article on the gauge orbit the redundancy was an inert overcompleteness: many descriptions, one configuration, no physical consequence. Here the redundancy is exploited: the phase is a coordinate along the orbit, the transformation that removes it shifts the connection by a gradient, and the shifted connection is the one whose kinetic term produces a mass. The erasure is the act of spending the redundancy.

## Where the Information Goes: The Longitudinal Mode and the Mass

### The Degree-of-Freedom Balance

The accounting is a count of real, on-shell degrees of freedom in four dimensions, and it was set out in full in the physics companion; it is recalled here in the informational reading.

| Phase | Scalar | Gauge field | Total |
|---|---|---|---|
| Symmetric, $\langle\tilde{\Phi}\rangle = 0$ | $2$ real, massless | $2$ transverse (massless) | $4$ |
| Broken, $\langle|\varphi|\rangle = v/\sqrt{2}$ | $1$ real (radial $h$), massive | $3$ ($2$ transverse $+1$ longitudinal) | $4$ |

The balance $2+2 = 1+3$ is the conservation statement. One scalar mode ceased to be an independent physical field, and one gauge polarization was gained, and the two events are the same event. Nothing was created and nothing destroyed: the Goldstone mode was **moved**, and it moved into the gauge field as the longitudinal polarization. In information-theoretic terms the balance is a conservation of the number of local physical degrees of freedom, and it is the reason the article says "relocation" rather than "loss".

### The Mass as the Gauge-Invariant Record

The physical content of the relocation is the mass, and its derivation is the derivation of a record. At the constant vacuum $\varphi = v/\sqrt{2}$ — that is, in the unitary gauge of the previous section, in which $\mathcal{A}_\mu = A_\mu$ — the ordinary derivative vanishes and the covariant derivative is proportional to the connection,

$$
D_\mu\varphi\Big|_{\mathrm{vac}} = \frac{iq}{\hbar}A_\mu\frac{v}{\sqrt{2}},
$$

so the gauge-invariant kinetic term becomes a quadratic form in the connection,

$$
-\,g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)\Big|_{\mathrm{vac}}
= -\,\frac{q^2v^2}{2\hbar^2}\,g^{\mu\nu}A_\mu^*A_\nu
= -\,\frac{q^2v^2}{2\hbar^2}\,\mathrm{Sc}\!\left(\bar{\tilde{A}}\tilde{A}\right),
$$

the last step using the material-sector reality condition $\tilde{A}\in\mathbb{M}_-$, which makes $g^{\mu\nu}A_\mu^*A_\nu = A_0^2+\mathbf{A}^2 = \mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ — the two sides differ for a connection with four unconstrained complex components, so the reality condition is what lets the covariant-derivative form and the biquaternion form be identified. Comparing with the Proca normalization $-\tfrac12 M_A^2\,\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ gives the mass

$$
M_A^2 = \frac{q^2v^2}{\hbar^2},
\qquad
M_A = \frac{qv}{\hbar}.
$$

This was recomputed by two independent routes on an explicit non-axis-aligned connection, $A_0 = 0.37i$, $A_1 = 0.82$, $A_2 = -0.51$, $A_3 = 0.29$ — with $A_0$ imaginary and $A_1,A_2,A_3$ real, as $\tilde{A}\in\mathbb{M}_-$ requires — at the generic parameter values $\kappa = q/\hbar = 0.7$ and $v = 1.3$. Directly from $-g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)$ at the vacuum the kinetic density was $-0.3642397850$; independently, the biquaternion prediction $-\tfrac12\kappa^2v^2\,\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ was $-0.3642397850$ as well. The two routes agree to all digits and confirm $M_A^2 = q^2v^2/\hbar^2$, with $qv/\hbar = 0.910000$. The mass is gauge invariant, because it is read from a gauge-invariant term; the phase is invisible in it, because it depends only on $v$.

The informational reading is that the mass is the **record** of the breaking. The vacuum family is a circle, but every member yields the same $v$, hence the same mass. The information that survives is a single gauge-invariant number; the phase information that the erasure removed was never physical, and the physical information that the breaking produced is $v$, recorded in $M_A$ and in $m_h$. This is a compression of the description, not a loss of physics.

## The Symmetry-Breaking Map as a Channel

### Unitary on the Full Degrees of Freedom

On the full degrees of freedom the passage from the symmetric to the broken description is reversible. The gauge transformation that eliminates $\theta$ is implemented by a unitary (the central phase $e^{iq\Gamma/\hbar}$), and on the state space of the combined scalar-and-gauge system it acts by conjugation. Relative entropy is invariant under such a map,

$$
S\bigl(U\tilde{\rho}\,U^\dagger \,\big\|\, U\tilde{\sigma}\,U^\dagger\bigr) = S(\tilde{\rho}\|\tilde{\sigma}),
$$

which was checked on explicit superpositions: with the Bloch vectors $\mathbf{r} = (0.41,-0.52,0.23)$ and $\mathbf{s} = (-0.33,0.61,0.47)$ and a rotation by $2.0$ radians about the axis $(0.55,0.31,-0.77)$ — a generic unitary of the informational sector; the central phase itself acts on $\mathbb{M}_+$ by $|\lambda|^2 = 1$, so for the re-encoding proper the invariance is immediate — the relative entropy took the same value $1.375407856007$ before and after the rotation, agreeing to machine precision. So no distinguishability between states is destroyed by the re-encoding in which the Goldstone mode is absorbed. The relocation is information-preserving on the full description.

### Many-to-One on the Observable Description

Restricted to the gauge-invariant observables, the map is not invertible. The phase is projected out — it is the coordinate along the orbit, and the orbit's observables cannot see it — so distinct full descriptions that differ by a phase give the same observable content. This is the same fibre structure the gauge-orbit companion analysed: the observable description is a quotient by the orbit, and the map from full descriptions to observable ones is many-to-one on that fibre.

The two statements are not in tension; they are the two sides of the quotient. The symmetry-breaking map is **unitary on the total space and many-to-one on the base**. Its information loss is exactly the information in the fibre, which is zero because the fibre is a gauge orbit. The apparent erasure is the quotient map, and its kernel carries no physical information — which is the article's answer to the title.

### Comparison with Loss and with Redundancy

The three cases of the subcategory can now be stated in one place.

- **Redundancy** (companion: gauge orbit). The fibre is a gauge orbit, non-trivial as a set but carrying no physical information; a representative recovers the configuration. Nothing is erased. This is the structure of the Higgs phase before the breaking, and it is what the mechanism exploits.
- **Loss** (companion: confinement). The fibre of the physical map is non-trivial and its elements are distinct partonic configurations that the asymptotic algebra cannot see; no gauge choice recovers them, and no record survives. This is genuine erasure with a non-trivial kernel.
- **Relocation** (this article). The fibre is a gauge orbit — hence carries no physical information — but the mechanism's action on it produces a physical record, the mass, and the count of degrees of freedom is conserved. Nothing physical is erased, and something physical is recorded.

The test that separates relocation from loss is whether the erasure leaves a gauge-invariant record. The Higgs mechanism does: the mass $M_A$ and the scalar mass $m_h$ are the record. Confinement does not: the colour of an individual parton leaves no asymptotic record at all. And the test that separates relocation from mere redundancy is whether the erasure has any physical consequence: the gauge orbit alone has none, while the Higgs mechanism's exploitation of it gives the gauge field a mass.

## The Vacuum as a Stable Record

### Einselection and the Pointer Variable

The broken vacuum is a **stable record**: a definite value of $|\varphi|$, a definite mass spectrum, and a definite set of gauge-invariant observables. The phase and the radial field together form the two real variables of the scalar; the vacuum makes one of them ($h$) massive and the other ($\theta$) a gauge coordinate. The massive variable is the one whose measurement is stable; the gauge coordinate is the one that no measurement distinguishes. This is the structure of **einselection**: a preferred, stable set of variables — the pointer variables — emerges, and the complementary variables lose their sharpness. The closest written model in the corpus is the article on decoherence as idempotent projection, and the analogy is worth stating carefully.

- In decoherence, the pointer basis is selected by the interaction with an environment, and the off-diagonal coherences decay because the environment records them.
- Here, the stable variables are selected by the gauge structure and the potential: the radial mode is stable because it is massive and gauge invariant, and the phase is not a variable at all because it is gauge. No environment is involved; the selection is by the vacuum.

The formal structure is shared — a preferred subalgebra, an idempotent-looking reduction of the description — but the mechanism is different. In one case an environment hides the information in correlations that exist; in the other there is no environment and the hidden variable is a gauge coordinate.

### The Landauer Comparison

The word erasure has a precise meaning in the thermodynamics of computation, and it is worth drawing the comparison explicitly. **Landauer's principle** states that the erasure of one bit of information in a system in contact with a heat bath at temperature $T$ dissipates at least $k_B T\ln2$ of heat: erasing a record has a thermodynamic cost, because the information must go somewhere.

The Higgs mechanism's erasure does not incur that cost, and the reason is the article's thesis. The object erased is a **gauge coordinate**, not a record. A gauge coordinate is not the kind of thing that must go somewhere; it was never a physical degree of freedom, and the "erasure" of a gauge coordinate is a change of description, not a physical process. What the mechanism does to the physical degrees of freedom is to **re-encode** them: the longitudinal mode is physical and exists in both descriptions, as the absorbed Goldstone mode before the gauge choice and as the third polarization after it. Re-encoding is reversible and costs no heat. The apparent paradox — a continuous label erased at no thermodynamic cost — dissolves once the label is identified as a coordinate along a gauge orbit rather than a bit of record.

One consequence is worth recording as a caution. If the phase were a *physical* (global) variable rather than a gauge coordinate, then the apparent erasure would be the **reset of a record** — a map taking the variable to a standard value whatever its prior value, which is exactly the operation Landauer's principle prices — and the mechanism would be genuinely dissipative. The framework's scalar is central and the phase is gauged, so this is not the case; the phase joins the gauge orbit, and the orbit is where physical information is not. The erasure is free because it erases nothing.

## What the Framework Supplies and Does Not Supply

**Supplied by the algebra, and recomputed here.** The complex central scalar $\tilde{\Phi} = \varphi e_0$ with its single gauge-invariant combination $\varphi^*\varphi$, checked to be invariant under phase rotations; the degenerate circle of vacua and the unitary-gauge elimination of the phase by a gauge transformation, which is the redundancy the mechanism spends; the identification of the phase as the coordinate along that orbit, so that the relocation of the Goldstone mode into the longitudinal polarization is a relocation of a gauge direction; the Proca mass with $M_A^2 = q^2v^2/\hbar^2$, recomputed on a generic connection and a generic parameter set; and the invariance of the relative entropy under the unitary re-encoding, checked on generic states. The informational reading — erasure of a gauge coordinate, conservation of the physical content, the mass as the record — is the article's interpretation, and it is the framework's own because the phase is central.

**Transcribed from standard physics.** The Higgs mechanism itself; the Goldstone theorem, the count of would-be Goldstone bosons, and the degree-of-freedom balance $2+2 = 1+3$; the unitary gauge; the Proca mass form; the identification of the longitudinal polarization; and Landauer's principle. The physics companion derives the mechanism; this article reads it.

**Not supplied.** A non-abelian or electroweak Higgs mechanism: the framework's scalar is a singlet of the $\mathfrak{su}(2)$ factor and a central scalar cannot break $SU(2)$; there is no electroweak doublet, no hypercharge assignment, and no constructed Yukawa coupling to the chiral fermions. The mass of the radial mode depends on the potential's coefficient $\beta$, which the framework does not fix. And there is no empirical consequence distinguishing the reading from standard scalar electrodynamics. These gaps are the physics companion's, and they are inherited here unchanged.

**Companion articles.** The construction rests on the following written articles of the series.

- Companion article *The Higgs Mechanism in Biquaternionic Form*, for the physics of the mechanism, the potential, the Proca mass, the Goldstone count, and the non-abelian gap.
- Companion article *The Gauge Principle in Biquaternionic Form*, for the central complex scalar, the local central phase, and the connection.
- Companion article *The Covariant Derivative and Gauge Connection in Biquaternionic Form*, for the covariant derivative at the vacuum and the covariant square.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the $\mathfrak{su}(2)$ factor, the adjoint law, and the reality-condition gap.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chirality selection rule and the unconstructed Yukawa coupling.
- Companion article *Decoherence as Idempotent Projection*, for the idempotent-projection model of a stable preferred description.
- Companion article *Relative Entropy and the Biquaternion Framework*, for the relative entropy and its invariance under unitary re-encoding.
- Companion article *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form*, for the redundancy that this article's mechanism exploits.
- Companion article *Confinement and the Loss of Partonic Information in Biquaternionic Form*, for the genuine loss that this article's relocation is contrasted against.

## Open Questions

1. **An information-theoretic mass formula.** The mass is the record of the erasure. Is there a framework-internal functional — an entropy, or a relative entropy between the symmetric and broken descriptions — whose extremization or whose value yields $M_A^2 = q^2v^2/\hbar^2$? No such functional is known.

2. **The count as a channel invariant.** The balance $2+2 = 1+3$ is a conservation of the count of local degrees of freedom. Is it the statement that, for a natural channel modelling the map, the input and the output carry the same information about the physical degrees of freedom, and if so, which channel? No such channel is identified here.

3. **The non-abelian relocation.** For a non-abelian breaking the number of absorbed Goldstone modes equals the number of broken generators, and the record is a mass matrix rather than a mass. Does the informational reading — erasure of a gauge orbit, conservation of the total, a gauge-invariant record — extend to the mass matrix, and can the framework supply the non-singlet scalar that would make the question concrete?

4. **Landauer and the gauge coordinate.** The article argues that erasing a gauge coordinate costs nothing because the coordinate is not physical. Is there a framework-internal statement of this — an "information" of a gauge orbit that is exactly zero, in the sense that the states of any two of its members are equal, so their relative entropy vanishes — and does it extend to the non-abelian orbit?

5. **The vacuum as a record and the arrow of time.** The Higgs vacuum is a stable record selected by the gauge structure rather than by an environment. Does the record structure have any dynamical content — a relaxation, a selection time — or is the vacuum selection in the framework purely kinematical, as it appears here?

6. **Empirical content.** As everywhere in the framework, no prediction distinguishing the reading from standard scalar electrodynamics is derived. The mechanism is standard; the reading is the framework's.

## Summary

The Higgs mechanism hides a gauge symmetry in the vacuum, gives the gauge field the mass $M_A = qv/\hbar$, and absorbs the would-be Goldstone mode as the longitudinal polarization. Read information-theoretically, it is an **erasure** of a redundant label and a **relocation** of physical content, not a loss.

The erased object is the phase of the scalar. It is a coordinate on the circle of degenerate vacua, $|\varphi| = v/\sqrt{2}$, but it is a **gauge** coordinate: the central phase acts trivially on the informational sector, so no Hermitian observable is conjugate to it, and the gauge-invariant content of the vacuum is the single number $|\varphi| = v/\sqrt{2}$, checked to be independent of the phase. A gauge transformation removes the phase from the scalar and shifts the connection by a gradient, and the combination $A_\mu + (\hbar/qv)\partial_\mu\theta$ is what the mass term depends on. The erasure of the phase and the shift of the connection are one operation, which is why the mechanism is best described as *using* the gauge redundancy rather than suffering it.

The relocated content is the longitudinal mode, and the record is the mass. The degree-of-freedom count balances, $2+2 = 1+3$: one scalar mode became the third gauge polarization, and nothing was created or destroyed. The mass $M_A^2 = q^2v^2/\hbar^2$ was recomputed on a generic connection and a generic parameter set, and the relative entropy was shown to be invariant under the unitary re-encoding. On the full degrees of freedom the symmetry-breaking map is unitary and information-preserving; on the gauge-invariant observables it is many-to-one, with the fibre being the gauge orbit — whose information content is zero. The erasure is the quotient map, and its kernel is a gauge orbit.

This distinguishes the mechanism from the two neighbours. Unlike confinement, which removes partonic labels from the asymptotic algebra with no record surviving, the Higgs mechanism leaves a gauge-invariant record, the mass, and conserves the total count. Unlike a bare gauge orbit, which has no physical consequence, the exploitation of the orbit generates the mass. The vacuum is then a stable record in the structure of einselection — the radial variable massive and observable, the phase a gauge coordinate — and the erasure costs no heat, in contrast with Landauer's principle, precisely because the object erased is a gauge coordinate rather than a bit of record. The mechanism's own construction is standard and is imported; the informational reading is the framework's, and it rests on the framework's central scalar.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material and informational sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$ | Centre; the complex scalar subspace |
| $\tilde{\Phi} = \varphi\,e_0 \in \mathbb{C}_{\mathbb{B}}$ | Complex central scalar |
| $\varphi^*\varphi = \mathrm{Sc}[\tilde{\Phi}^\dagger\tilde{\Phi}] = |\varphi|^2$ | Gauge-invariant content of the scalar |
| $V = \beta(\varphi^*\varphi - v^2/2)^2$ | Potential; minimum the circle $|\varphi| = v/\sqrt{2}$ |
| $v$ | Vacuum expectation value; the gauge-invariant record of the breaking |
| $h,\ \theta$ | Radial and angular (would-be Goldstone) fields |
| $m_h^2 = 2\beta v^2$ | Radial-mode mass |
| $\tilde{A}\in\mathbb{M}_-$, $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ | Connection and gauge law |
| $D_\mu = \partial_\mu + i\kappa A_\mu$, $\kappa = q/\hbar$ | Covariant derivative and coupling |
| $g = \mathrm{diag}(-1,+1,+1,+1)$ | Level-2 $ict$-coordinate metric for contractions |
| $\Gamma = -(\hbar/qv)\theta$ | Gauge function of the unitary gauge |
| $\mathcal{A}_\mu = A_\mu + (\hbar/qv)\partial_\mu\theta$ | Gauge-invariant combination carrying the mass |
| $M_A^2 = q^2v^2/\hbar^2$, $M_A = qv/\hbar$ | Gauge-field (Proca) mass; the record |
| $-\tfrac12 M_A^2\,\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ | Proca mass term |
| $2+2 = 1+3$ | Degree-of-freedom balance; conservation |
| $S(\tilde{\rho}\|\tilde{\sigma})$ | Relative entropy; invariant under the re-encoding |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$, $|\mathbf{r}|\leq1$ | State of the informational sector (Bloch ball) |
| $k_BT\ln2$ | Landauer cost of erasing a physical bit (not incurred here) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing; $\mathrm{Tr}(e_0) = 2$ |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- Peter W. Higgs, "Broken Symmetries and the Masses of Gauge Bosons," *Physical Review Letters* **13** (1964) 508–509, for the mechanism and the gauge-boson mass.
- F. Englert and R. Brout, "Broken Symmetry and the Mass of Gauge Vector Mesons," *Physical Review Letters* **13** (1964) 321–323, for the independent formulation.
- Jeffrey Goldstone, Abdus Salam, and Steven Weinberg, "Broken Symmetries," *Physical Review* **127** (1962) 965–970, for the Goldstone theorem and the massless mode.
- Steven Weinberg, "A Model of Leptons," *Physical Review Letters* **19** (1967) 1264–1266, for the electroweak realization and the doublet structure the framework lacks.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the abelian and non-abelian Higgs mechanism, the unitary gauge, and the degree-of-freedom count.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Proca mass, the absorbed Goldstone mode, and the counting of polarizations.
- T. Kugo and I. Ojima, "Local Covariant Operator Formalism of Non-Abelian Gauge Theories and Quark Confinement Problem," *Progress of Theoretical Physics Supplement* **66** (1979) 1–130, for the quartet mechanism and the statement that the Goldstone modes are unphysical in a covariant gauge.
- Rolf Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development* **5** (1961) 183–191, for the thermodynamic cost of erasing a bit.
- Charles H. Bennett, "The Thermodynamics of Computation — A Review," *International Journal of Theoretical Physics* **21** (1982) 905–940, for reversible computation, erasure, and the distinction between re-encoding and dissipation.
- Wojciech H. Zurek, "Decoherence, einselection, and the quantum origins of the classical," *Reviews of Modern Physics* **75** (2003) 715–775, for einselection and the emergence of a preferred, stable set of variables.
- Huzihiro Araki, "Relative entropy of states of von Neumann algebras," *Publications of the Research Institute for Mathematical Sciences* **11** (1976) 809–833, for relative entropy and its invariance under unitary conjugation.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the entropy-theoretic background used in the channel reading.
