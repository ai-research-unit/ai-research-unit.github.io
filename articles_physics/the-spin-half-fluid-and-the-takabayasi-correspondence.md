# __The Spin-Half Fluid and the Takabayasi Correspondence__

## Introduction

**The claim of this article is that the biquaternion polar word and Takabayasi's tensor formulation of 1957 are the same fluid described in two languages, and that the correspondence is exact on the domain where both are defined.** Takabayasi's *Relativistic Hydrodynamics of the Dirac Matter* replaces the spinor and the gamma matrices by a set of real tensor fields — a density, a velocity, a spin vector, a momentum and one internal angle. The polar word writes the same field as one element of $\mathbb{B}$ decomposed into four factors. Every variable of the tensor system is a factor of the complete polar decomposition or a component of one.

**The article is a comparison and not a derivation.** The word, its four brackets, its current and its spin are [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html). Takabayasi's system is his. What is new here is the mapping between them, the reason each row of the mapping holds, and the ledger of what the comparison buys.

**The comparison also yields two fluid properties that the block has named and not used, and they are computed here rather than asserted.** §*The Mass Density and the Heat Flow* shows that his density is the current's modulus and that the mass term couples to a different number, and it puts a value on the heat flow that his choice of velocity leaves in the fluid's own rest frame. The two are not decoration: the first gives the fluid its one thermodynamic function, and the second says what the frame choice costs. Each claim carries its check in place.

**The ledger is short and it is stated at the outset.**

- **No new prediction.** Nothing in the biquaternion reading predicts what the tensor formulation does not predict.
- **No new solution.** The general solution is the Fourier superposition of plane waves in both.
- **A cleaner origin.** The spin-half fluid, its non-closure, its current–spin separation and its domain all follow from the factorisation of one element, and in the tensor language they are imposed by hand.

**The correspondence is graded, and the grades matter.** Three of the five rows are read off the algebra as identities. One is a reading of the momentum as a gradient, which holds only where his curl vanishes, so it is a reading and not an identity. The last is forced by the count once the first four are granted, and is supported by two further arguments that are not computations. The table in §*The Variable Mapping* marks each row with its grade, and a reader who wants only the secure part can take the first three rows and leave the rest.

## The Tensor Formulation

**Takabayasi's starting point is the set of bilinear covariants of the Dirac field.** There are sixteen of them, and kinematical identities relate them, so that seven real quantities independent at each event remain. He writes them as a density, a unit timelike four-velocity and a unit spacelike four-vector orthogonal to it:

$$
\rho>0,
\qquad
\sum_\mu\varepsilon_\mu v_\mu v_\mu=-1,
\qquad
\sum_\mu\varepsilon_\mu w_\mu w_\mu=1,
\qquad
\sum_\mu\varepsilon_\mu v_\mu w_\mu=0 .
$$

The count is $1+3+2=6$, and the remaining quantity of the seven is an internal angle $\theta$, defined as the angle in the plane of the two pseudoscalar densities of the field, $\theta=\arctan(\Omega_{\mathrm{ps}}/\Omega)$ with $\Omega$ and $\Omega_{\mathrm{ps}}$ the scalar and pseudoscalar bilinears.

**To those he adds the momentum.** The particle momentum-energy four-vector $k_\mu$ is not among the bilinears, and it enters his equations as a separate variable. With it the system's variables are

$$
\{\,\rho,\ \theta,\ v_\mu,\ w_\mu,\ k_\mu\,\} .
$$

**The count of functions is the count of the field's real components, and this is the first thing the two formulations agree on.** The field has four complex coefficients, that is eight real functions at each event. The tensor system has six from the first three items ($\rho$, $v_\mu$, $w_\mu$: $1+3+2$), one for $\theta$, and one for $k_\mu$ once its curl is fixed, which his second subsidiary condition fixes. So the system carries eight.

**His equations of motion close the count but do not close the system.** The Dirac equation is equivalent to a set of real equations for the tensor variables: a continuity equation for $\rho v_\mu$, a balance equation for the spin density $\rho w_\mu$ with a source proportional to $\sin\theta$, and two transport laws in which $\theta$ and $k_\mu$ appear together with the gradients of $v$ and $w$. That is eight real equations for eight real unknowns, and they are equivalent to the Dirac equation.

**The momentum is not determined by them.** The equations contain $k_\mu$ and do not determine it. Takabayasi therefore adds a further condition, his second subsidiary, which fixes the curl of $k_\mu$ in terms of the velocity, the spin and the electromagnetic field strength. The condition is quasi-irrotational: the curl of the momentum is not zero, and it is not free either. He calls it the condition that makes the system self-contained, and it is the one place where his formulation adds an equation that the Dirac equation does not supply by itself.

## The Variable Mapping

**The mapping is a table, and every row is a comparison of what a bilinear reads.**

| Takabayasi | polar word | grade |
| --- | --- | --- |
| $\rho$, the rest density | $r^{2}$, the scale squared | identity |
| $v_\mu$, the unit four-velocity | $\tilde U_{\Psi,\mathrm b}$, the Hermitian boost | identity |
| $w_\mu$, the unit spin vector | $\tilde u_{\mathrm r}$, the real rotor | identity |
| $k_\mu$, the momentum | $\tilde K_{\mu}/k_m$, the phase gradient in units of the mass wave number | reading, with a qualifier |
| $\theta$, the internal angle | $\theta_{\mathrm{axr}}$, the rotor angle | forced by the count, given the first four rows |

**Two of the rows carry a unit as well as a comparison, and the momentum row is one of them.** Takabayasi defines $k_\mu=p_\mu/(mc)$, a momentum divided by a mass, so his $k_\mu$ is dimensionless. The word's momentum is the phase gradient, an inverse length. The ratio between them is the mass wave number $k_m=mc/\hbar$, so the row reads $k_\mu=\tilde K_\mu/k_m$ and a table that equates the two loses the $\hbar$. His units also set $c=1$, which is why his $v_\mu$ is $\tilde V_{\Phi}/c$ and his $\rho$ is the corpus's $\rho_{\mathrm{num}}$; with $c$ carried, the velocity's norm is $c^{2}$ in the word and $1$ in his display.

**The first three rows are identities and they are the corpus's own statements.** The density of the word is $\rho_{\mathrm{num}}=r^{2}$, read from the scale. The four-velocity is $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}=\gamma(ic\,e_t+\vec v)$, read from the boost, with $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$ for every field. The spin is $\tilde S_{\Psi}=\rho_{\mathrm{num}}\frac{\hbar}{2}i\vec s$ with $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, read from the rotor. These are not correspondences of formulas; they are the same three objects named twice.

### Why the count forces the fifth row

**The count argument is short and it is the strongest part of the comparison.** The count closes twice over. The word has $1+1+3+3=8$ parameters: the scale one, the phase one, the boost three, the rotor three. Takabayasi's list has $1+1+3+2+1=8$ effective functions: density one, momentum one, velocity three, spin two, angle one, the momentum counting once because his second subsidiary condition fixes its curl. Four buckets are matched by the first four rows — the scale against the density, the phase against the momentum, the boost's three against the velocity's three, and two of the rotor's three against the spin's two. **The only unmatched pair is the rotor's third parameter and Takabayasi's angle, and there is nothing else on either side.** The identification of $\theta$ with $\theta_{\mathrm{axr}}$ is therefore forced by the count and not chosen, once the first four rows are granted.

**Two further arguments support the identification, and neither is a computation.**

**The sign of the double cover.** Takabayasi writes the two densities as $\Omega=\rho\cos\theta$ and $\Omega_{\mathrm{ps}}=\rho\sin\theta$. A shift of $\theta$ by $2\pi$ leaves both and multiplies the field by $-1$, and a shift by $\pi$ flips both, which is no invariance and is the field multiplied by $-i\gamma_5$ rather than by a sign. The rotor's angle has exactly this structure: the spin direction $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ has period $2\pi$ and is reversed at $\pi$, while the rotor itself is $-e_t$ at $2\pi$ and multiplies the element by $-1$. So the two angles are the same kind of angle, and the similarity is exact rather than analogical.

**Neither is the phase.** The density is the modulus of the norm, so it has period $\pi$ in $\theta_{\mathrm{pha}}$ and the phase's own range is a half turn, the other half being the sign. The two angles of this section are the opposite case: their bilinears need the full turn. That is the difference between the angle the scalar fluid carries and the angle the spinor fluid carries, and it is why the two cases have different counts.

**The chiral operation.** A chiral rotation of the field is a right multiplication by the rotor $e^{\alpha\vec e_z}$ about the declared axis, and the word's rotor is the rightmost factor, so the rotation moves $\tilde u_{\mathrm r}$ alone: the scale and the phase are central and commute, and the boost stands to the left and is untouched. Takabayasi's $\theta$ is the angle that the same rotation shifts, because $\Omega$ and $\Omega_{\mathrm{ps}}$ rotate into one another under it. So the fifth row pairs the two objects that one operation acts on, and that is the whole of the argument. When the rotor's axis is not the declared one the rotation changes the axis as well as the angle, and the pairing of angles is then a statement about the factor and not about a single number.

**The mass term is not part of it.** $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$ depends on the boost and on nothing else, so the mass does not couple the rotor angle; what the mass does is make the chiral rotation a broken symmetry rather than an exact one, which is a statement about the equation and not about which factor carries the angle.

**What the identification is not.** It is not a theorem. Nothing in the corpus computes $\theta$ from $\theta_{\mathrm{axr}}$ in a given solution, and the two are defined in different ways: his as the argument of a bilinear ratio, the corpus's as a parameter of the polar decomposition. What the count and the two further arguments establish is that the identification is the only consistent assignment. A reader may hold that and still want the explicit computation, and it is not in this corpus.

### The qualifier on the fourth row

**The momentum row needs one sentence of care, and it is the row where the two formulations are not literally the same.** The word's momentum is the phase gradient, $\tilde K_{\Phi}=\tilde\nabla_\Phi\theta_{\mathrm{pha}}$, so it is a gradient by construction and its curl vanishes. Takabayasi's $k_\mu$ has a curl fixed by his second subsidiary condition and that curl is not zero in general. The two therefore agree on the fields where the curl vanishes, and differ elsewhere.

**The reading that reconciles them is that his curl is the freedom of the phase.** His condition fixes the curl of $k_\mu$ and leaves the gradient part free; the free part is one function, which the word names the phase and whose gradient it calls the momentum. On this reading his $k_\mu$ is a particular momentum and the word's $\tilde K_{\Phi}$ is the canonical one, and the difference is the term his condition supplies. The reading is stated here as a reading, because the alternative — that the two momenta are simply different objects — cannot be excluded from the comparison alone.

## The Four Brackets and the Non-Closure

**Differentiating the word separates the derivative into four terms of four different types.** For $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$,

$$
\frac{\partial\tilde\Xi}{\partial R_\mu}
=\tilde\Xi\left[\frac{1}{2}\frac{\partial\ln\rho_{\mathrm{num}}}{\partial R_\mu}
+i\frac{\partial\theta_{\mathrm{pha}}}{\partial R_\mu}
+\tilde u_{\mathrm r}^{-1}\Bigl(\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu}\Bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\frac{\partial\tilde u_{\mathrm r}}{\partial R_\mu}\right].
$$

**The four brackets are four different objects, and the equation cannot mix them.**

| bracket | type | fluid reading |
| --- | --- | --- |
| $\tfrac12\partial_\mu\ln\rho_{\mathrm{num}}$ | real central scalar | continuity of the density |
| $i\partial_\mu\theta_{\mathrm{pha}}$ | central imaginary | guidance: $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | transport of the velocity |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | transport of the spin direction |

**The equation constrains the four and does not determine them.** The Dirac equation is one equation for the element, so it is eight real equations for the eight parameters. It is not eight equations for the four brackets taken separately, because the brackets are not independent functions: the boost connection is determined by three parameters and the rotor connection by three, and the two are coupled through the order of the factors.

**This is exactly the situation Takabayasi's subsidiary condition answers.** His equations close the count and leave $k_\mu$ undetermined; he adds a condition on its curl. The algebraic statement is that the four brackets are of four types and no rule of the algebra fixes one from another, because a real scalar cannot be a Hermitian element and a central imaginary cannot be a real vector. **His condition is the tensor form of that non-closure, and the non-closure is a property of the factorisation and not a defect of either formulation.**

**The non-closure is also where the non-uniqueness enters.** A closing condition is a choice, and the literature contains many. Takabayasi's is one; the spin-transport laws of the classical-spin literature are others; Fabbri's enumeration of minimal spin-fluid systems records nineteen. The corpus does not choose among them and says so: the Dirac equation does not single out a spin-transport law, and any formulation that supplies one has added a choice.

## The Current and the Spin

**Both formulations separate the current from the spin, and both separate them the same way.**

| object | Takabayasi | polar word |
| --- | --- | --- |
| current | $\rho v_\mu$ | $\rho_{\mathrm{num}}\tilde V_{\Phi}$, reading $\rho_{\mathrm{num}}$, $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ |
| spin density | $\rho w_\mu$ | $\rho_{\mathrm{num}}\frac{\hbar}{2}i\vec s$, reading $\rho_{\mathrm{num}}$, $\theta_{\mathrm{axr}}$, $\vec u_{\mathrm r}$ |
| what neither reads | $\theta$ | $\theta_{\mathrm{pha}}$ |

**The separation is the same and the reason is not.** In the tensor formulation the current and the spin are different bilinears, and the separation is a fact about which bilinear is which. In the word the current reads the Hermitian factor and the spin reads the real-unitary factor, and the separation is a consequence of the four factors being of different types. **The word explains the separation and does not merely record it.**

**The thing that is not the current is worth one paragraph here, because Takabayasi's formulation does not have the problem.** The algebra's own bilinear $i\tilde\Xi\tilde\Xi^{*}$ is the current's mirror image: its temporal slot agrees with $\tilde J_{\Phi}$ up to the factor $c$ and its spatial part is reversed, because the star conjugation fixes the boost and cancels the rotor and the outer $i$ then reverses the spatial vector. Takabayasi defines his current as $\rho v_\mu$ directly and never meets this. The corpus meets it because it tries to read the current from a bilinear of the algebra, and [The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html) carries the analysis of the failure.

## The Domain

**Takabayasi assumes $\rho>0$ and derives. The word states its domain and the domain is smaller.**

**His assumption and the word's condition are different conditions.** The factorisation $\rho v_\mu$ with $v_\mu$ a unit vector needs $\rho\neq0$. The word needs $N(\tilde\Xi)\neq0$, which is the condition that the element be an invertible element of the algebra. For the scalar field the two agree. For the spinor field they do not.

**Two families of Dirac fields have $\rho\neq0$ everywhere and no word anywhere.**

- **Parts of definite value.** An element with $\tilde X\vec e_z=\pm i\tilde X$ is a zero divisor at every amplitude, because $\tilde X(\vec e_z\mp ie_t)=0$ and the bracket is not zero. Every field of definite chirality is of this kind.
- **One-sided plane waves.** A plane wave with $\tilde K_{\Phi}\tilde\Xi_{0}=0$ and $\tilde K_{\Phi}$ null has $N(\tilde\Xi_{0})=0$ everywhere. It is nowhere zero and its density never vanishes, and its word does not exist.

**The second family is the one that matters physically**, because a one-sided wave is what a massless helicity eigenstate is. His variables $\rho$, $v_\mu$ and $w_\mu$ are defined on it, since $\rho>0$. **Whether his formulation proceeds on it is a separate question.** Several of his quantities carry the factor $1/k_m=\hbar/(mc)$, so they diverge at $m=0$ and the massless field is a limit rather than a case, and whether that limit exists for a one-sided wave is not settled here. What the comparison establishes is a difference of domain conditions: the word needs the element to be an invertible element, which is strictly stronger than $\rho\neq0$, and the one-sided wave is the field that exhibits the difference.

**What survives on the cone is the two-factor decomposition.** Every element is $\tilde\Xi=\tilde\Xi_{H}\tilde\Xi_{0}$ with $\tilde\Xi_{H}$ Hermitian positive semidefinite and $\tilde\Xi_{0}$ a partial isometry, and that factorisation is defined on the whole algebra. It separates a scale from a direction but not a velocity from a spin, so it is not enough for a fluid. The four-factor word is the finer decomposition and it is the one that fails.

**This is a finding and not a criticism of Takabayasi.** His variables are defined for the fields he treats, and the cone is outside his scope. What the comparison adds is the identification of the boundary, and the boundary is the price of the word.

## The Mass Term and the Stress

**The mass term is a number in his formulation and a frame factor in the word.** In the standard reading the mass is a scalar coupling the two chiral parts, invariant in every frame. In the word the kinetic relation between the parts is $\tilde\Xi_{0}^{L}=-\mathcal B_{\Psi}\tilde\Xi_{0}^{R}$ with $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$, so the mass's sign is carried along by the boost and the momentum carries the same boost. At rest the factor is the identity and the relation is the plain sign. The two statements agree; what the word adds is where the scalar goes in a moving frame.

**His energy-momentum tensor separates into a particle part and a stress part.** Takabayasi writes $L_{\mu\nu}$ as a momentum transport term $\rho k_\mu v_\nu$ plus a remainder, and reads the remainder as the mechanical stress and heat flow inside the fluid. The remainder is not a pure spin term: it carries the gradient of the internal angle multiplied by the spin direction, and the spin density contracted with the curl of the velocity. The conservation law is the equation of motion for the particle momentum, and the remainder represents the quantum effects.

**The remainder is a mix, and the correspondence is not a computed equality.** The word splits the derivative into a boost connection and a rotor connection, and a split of the derivative is not a split of the stress. Takabayasi's remainder draws on both: the angle's gradient is a rotor quantity, the spin direction is a rotor quantity, and the curl of the velocity is a boost quantity. So the honest statement is that the remainder is not the rotor's contribution alone, and that no term-by-term identification of it with the word's boost and rotor pieces is computed in this corpus. The relativistic quantum stress is exhibited in [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) for the scalar case, and the spinor case's antisymmetric part is the subject of the articles that follow this one.

## The Mass Density and the Heat Flow

**Two fluid properties follow from the mapping and have not been used in this block.** The fluid carries two densities and not one, and its velocity is the particle frame's and not the energy frame's. The first is what the internal angle says when it is not read as a spin; the second is what the stress remainder calls heat flow. Both are computed here.

### The two densities

**His density is the modulus of the current, and his scalar bilinear is a different number.** His $\Omega$ and $\Omega_{\mathrm{ps}}$ are the scalar and the pseudoscalar bilinears, $\Omega=\bar\psi\psi$ and $\Omega_{\mathrm{ps}}=i\bar\psi\gamma_5\psi$, and his density is their quadrature:

$$
\rho^{2}=\Omega^{2}+\Omega_{\mathrm{ps}}^{2}=\sum_\mu\varepsilon_\mu j_\mu j_\mu,
$$

with $j$ the current. The identity is Fierz's; on twenty random spinors its largest deviation is $9\times10^{-14}$.

**Three statements follow.** The velocity $v_\mu=S_\mu/\rho$ is a unit vector because $\rho$ is the current's modulus, so the normalisation of the velocity is not a condition at all: nothing is imposed. His $\rho>0$ is a definition and not a restriction, the modulus being positive exactly where the current does not vanish. The third is this section's subject: his mass term carries the scalar bilinear and not the density, so the fluid's mass density is

$$
m\Omega=m\rho\cos\theta
$$

while its particle density is $\rho$, and the two differ by the factor $\cos\theta$.

**A plane wave is the case where they agree in magnitude.** $\Omega_{\mathrm{ps}}$ vanishes for a free plane wave, and the reason is exact rather than numerical: the two chiral halves of a plane-wave spinor differ by the Hermitian factor $\vec\sigma\cdot\vec p$, so the two terms of the pseudoscalar cancel. Checked on eight plane waves, four momenta and both spins, to $10^{-16}$. So $\theta$ is $0$ for a particle and a half turn for an antiparticle, and $\lvert\cos\theta\rvert=1$ either way. A free plane wave is a fluid element whose mass density and particle density are one number, up to the sign that carries its charge content.

**Away from it they differ, and the difference is a mass defect.** A two-mode superposition gives $\cos\theta=0.9986$, $0.9739$ and $0.8777$ at three events of one field, and a particle–antiparticle superposition gives $0.045$ and $0.037$ at two events of another. Each particle then contributes $mc^{2}\cos\theta$ to the mass term instead of $mc^{2}$, so the fluid carries a defect $mc^{2}(1-\cos\theta)$ per particle: between $0.0014$ and $0.12$ in the first field and about $0.95$ in the second. **Whether the defect is to be called an internal energy is a reading**; what is computed is $\cos\theta$. The reading is that the fluid has one thermodynamic function per particle, $mc^{2}(\cos\theta-1)$, which is the function the block's table records as "none". The table's *none* is right about the shape of the stress: [The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html) says in the same place that the fluid's data do not determine its stress. It is silent about the mass, and it is silent about the trace, which the last subsection of this section computes.

**The sign of the mass density is the particle content, and charge conjugation flips it while leaving the density alone.** An antiparticle-dominated field has $\Omega<0$ with $\rho>0$; two antiparticle modes give $\cos\theta=-0.9987$. Charge conjugation sends $\Omega\to-\Omega$ and leaves $\Omega_{\mathrm{ps}}$, so $\cos\theta\to-\cos\theta$ and $\sin\theta\to+\sin\theta$. That is $\theta\to\pi-\theta$ and not $\theta\to\theta+\pi$. Checked on both superpositions: the cosines are equal and opposite to the last digit, the sines agree to $10^{-17}$, and the alternative $\theta+\pi$ misses by $2.0$ and $0.09$. The energy reading of the paragraph above is therefore confined to the particle sector; on the antiparticle side the sign of $\Omega$ is a charge label and not an energy.

### The velocity and the heat flow

**His velocity is the current's direction, and the standard name for that choice is the Eckart frame.** Relativistic hydrodynamics fixes the fluid's velocity in one of two ways. The Eckart frame takes the particle flux, and that is his, by definition: $S_\mu=\rho v_\mu$. The Landau frame takes the energy flux, the timelike eigenvector of the stress. The two coincide exactly when the energy flux vanishes in the Eckart frame, and that flux is the heat flow,

$$
q_\mu=\sum_\lambda\varepsilon_\lambda T_{\mu\lambda}u_\lambda-\epsilon\,u_\mu,
\qquad
\epsilon=\sum_{\lambda,\rho}\varepsilon_\lambda\varepsilon_\rho T_{\lambda\rho}u_\lambda u_\rho,
$$

with $u$ the Eckart velocity, a unit timelike vector, and $\epsilon$ the energy density it sees.

**A plane wave has none, and a superposition has some.** Computed on the Belinfante stress — the symmetrised canonical tensor, whose divergence vanishes to $2\times10^{-16}$ on every case checked — a single plane wave has $\lVert q\rVert/\lvert\epsilon\rvert\le6\times10^{-16}$. The two-mode superposition has it at $0.31$ and $0.34$ of the energy density at two events, and the particle–antiparticle superposition at $18$ and $15$. The angle and the flux move together: $\lvert\cos\theta\rvert=1$ with $q=0$, and $\lvert\cos\theta\rvert<1$ with $q\neq0$.

**The check that separates the angle from the superposition is the pair with one momentum.** Two plane waves of the same momentum and opposite spins have $\cos\theta=1$ and $\lVert q\rVert/\lvert\epsilon\rvert\le5\times10^{-17}$. So it is not the interference of two waves that produces the heat flow; it is the disparity between the momentum and the velocity, which the interference happens to produce and the common momentum does not.

**This is where his reading of $\theta$ becomes a fluid statement.** He says that the angle measures the disparity between the velocity and the momentum, and his own stress says the same in the other vocabulary: the particle part of $L_{\mu\nu}$ is $mc^{2}\rho k_\mu v_\nu$, whose momentum density lies along $k$ and whose particle flux lies along $v$, so the two are parallel exactly when $k$ is. When they are parallel the transport term is a transport along the flow and there is nothing left to carry; when they are not, the momentum density and the particle flux point along different directions, and the difference has to appear as a flux in the fluid's own rest frame. **The identification of the disparity with $\theta$ is his and is quoted; what is computed here is that the two families separate the same way.**

### The trace and the pressure

**The stress has a fixed trace, and that trace is his mass term.** Computed on the symmetrised canonical tensor, the trace is the scalar bilinear,

$$
\sum_\mu\varepsilon_\mu T_{\mu\mu}=mc^{2}\Omega=mc^{2}\rho\cos\theta ,
$$

the improvement that symmetrises the tensor being a divergence whose own trace vanishes. The identity is asserted of the corpus's own tensor: his $L_{\mu\nu}$ is a different arrangement of the same bilinears, and this article does not recompute it. The arithmetic is in [The Spin-Half Energy-Momentum Tensor](the-spin-half-energy-momentum-tensor.html): twenty-one events, largest deviation $2.7\times10^{-15}$. The identity joins the two objects that his formulation keeps apart — the mass term of the Lagrangian and the trace part of the stress — and says they are one number.

**So the equation of state has one line, and it is not the pressure.** In the flow's frame the trace is $\epsilon-3p$, hence

$$
p=\tfrac13\bigl(\epsilon-mc^{2}\rho\cos\theta\bigr).
$$

The isotropic part is a function of the state, since $\epsilon$ and $\cos\theta$ are. The deviatoric part is not, and the next computation shows by how much it is not.

**At fixed density and fixed angle the rest of the stress is not fixed.** Two positive-energy modes, the first at momentum $(0.7,0.3,0)$ and the second at $(-\lambda,0.4,0.2)$, both of amplitude one, at one event, with $m=1$ and $\pi^{j}{}_{k}$ the traceless part of the spatial block:

| $\lambda$ | $\rho$ | $\cos\theta$ | $\epsilon/\rho$ | $p/\rho$ | $\lVert\pi\rVert/\rho$ |
| --- | --- | --- | --- | --- | --- |
| 0.2 | 4.1355 | 0.99823 | 1.20121 | 0.06766 | 0.16573 |
| 0.6 | 4.1292 | 0.99880 | 1.42017 | 0.14046 | 0.34405 |
| 1.0 | 4.1204 | 0.99948 | 1.70057 | 0.23370 | 0.57244 |
| 1.6 | 4.1087 | 0.99999 | 2.18642 | 0.39548 | 0.96872 |
| 2.4 | 4.0998 | 0.99948 | 2.89036 | 0.63029 | 1.54390 |

**The columns separate cleanly.** The density moves by under one percent and the cosine by two tenths of a percent, so the state is the same state in every row. The energy density per particle more than doubles, the pressure grows by a factor nine, and the shear by a factor nine. The trace is not a separate column: $\epsilon/\rho-3p/\rho$ equals $\cos\theta$ in every row, to the five digits shown.

**The missing datum is a derivative, not a value.** What separates the rows is the spread of the momentum about its mean, and the spread is the dispersion of the phase gradient, not the gradient. The word holds eight numbers at an event and the phase gradient contributes one four-vector among them; the dispersion contributes nothing. So no function of the fluid's variables can supply the pressure, and a transport equation is needed for the spread. That is the information-count form of the non-closure this article records in *The Four Brackets and the Non-Closure*: the algebra gives the mean of the connection and not its dispersion, which is why Takabayasi must impose (II) and why the choice of a closure is not unique.

**This is the answer to the block's *none*.** The block's table records the equation of state as *none*, and the reading is right about the tensor and wrong about its trace. The trace is one line; the deviation from isotropy is undetermined. A fluid with a known trace and an unknown shear is a fluid with a bulk equation of state and no shear prediction.

**What is established and what is read.** Established: that $\rho$ is the current's modulus and that $\Omega=\rho\cos\theta$; that $\lvert\cos\theta\rvert=1$ for a free plane wave and falls below it for superpositions, with the values quoted; that charge conjugation sends $\theta\to\pi-\theta$; that the Eckart energy flux vanishes for a plane wave and for two waves of one momentum, and does not for the superpositions; that the trace of the stress is $mc^{2}\rho\cos\theta$, so that $p=\tfrac13(\epsilon-mc^{2}\rho\cos\theta)$; that at fixed density and fixed angle the energy density runs over a factor $2.4$ and the shear over a factor $9$. Read: that the defect is an internal energy; that the disparity of momentum and velocity is the angle itself; that the missing datum for the pressure is the dispersion of the phase gradient.

## What the Correspondence Adds and What It Does Not

### What it adds

**The origin of the spin-half fluid.** Takabayasi constructs the fluid from the bilinears of the field. The word reads it from the factorisation of one element: the four factors are the fluid's variables and the four brackets are its equations. The construction becomes a reading.

**The explanation of the subsidiary condition.** Takabayasi imposes his condition to close the system. The word shows that the system's non-closure is the algebraic independence of four brackets of four types, and his condition is one way to close it.

**The reason for the current–spin separation.** In the tensor language the separation is a fact about bilinears; in the word it follows from the Hermitian factor carrying the boost and the real-unitary factor carrying the rotor.

**The reason the vorticity is not a dynamical variable.** A classical fluid's vorticity is derived and then transported, with Helmholtz's theorems and a conserved helicity. The word's vorticity is a function of the boost's gradient and of nothing else, so the transport law has nothing to act on and the invariant of a loop is the frame's holonomy rather than a circulation. [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) carries the classical side of that distinction.

**The precise domain.** His variables need $\rho\neq0$; the word needs the element to be an invertible element, and for the spinor field the second condition is strictly stronger. The one-sided waves are the fields that show the difference.

**The mass term's frame dependence.** The scalar coupling is a frame factor, and the factor is the same one the velocity carries.

**The equation of state, and its one line.** A general fluid needs a function of two variables; here the trace of the stress is the mass term, $\sum_\mu\varepsilon_\mu T_{\mu\mu}=mc^{2}\rho\cos\theta$, so the pressure is $\tfrac13(\epsilon-mc^{2}\rho\cos\theta)$ and the isotropic part follows from the state. What is not fixed is the shear, and the fixed-density table shows it running over a factor nine while the state stands still. The corpus's own statement of the identity is in [The Spin-Half Energy-Momentum Tensor](the-spin-half-energy-momentum-tensor.html), and it is proved there for the corpus's tensor and not for his.

**The fluid's two densities, and the frame its velocity belongs to.** His density is the current's modulus, so his subsidiary conditions are met by construction, and the mass term couples to the scalar rather than to that density: the fluid carries a particle density and a mass density, and their ratio is the angle. His velocity is the current's direction, which is the Eckart frame, and the energy flux that this choice leaves in the fluid's rest frame is what his reading of the stress remainder calls heat flow.

### What it does not add

**No prediction.** The two formulations make the same predictions, and there is no experiment that separates them.

**No solution.** A plane wave is a plane wave in both. The word reads each mode and does not solve the equation.

**No removal of the non-uniqueness.** The closing condition is still a choice. Takabayasi makes one, the spin-hydrodynamics literature makes others, and the corpus records the choice without making it.

**Where the spin-half fluid stands among the three.** The block now has a fluid per spin, and they are compared side by side in [The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html)'s §*The Three Fluids* and in [The Spin-One Fluid](the-spin-one-fluid.html)'s: the scalar field is a gradient flow with a Korteweg stress and no orientation, the Proca field is a charged flow with a London response and no orientation, and this one is a flow with an orientation — a Cosserat medium but not the constrained one. Takabayasi's own subsidiary condition is the constraint that would make it the constrained case, and that is the sharpest way to say what his tensor fluid is and what the word's is.

**The one-sentence ledger is: the equation, no; the coordinates, yes.** Takabayasi's tensor calculus is the equation in tensor form. The polar word is the coordinates in which the equation's structure is algebraic.

## What Is Established and What Is Interpretation

**Established.** That the first three rows of the mapping are identities of the corpus's own definitions. That the count of eight functions matches on both sides and that the fifth row is the only consistent assignment of the two leftovers. That the derivative of the word separates into four brackets of four distinct types, and that the Dirac equation constrains them without closing them. That the current reads the boost and the spin reads the rotor. That the word's domain is the set of invertibles and that the one-sided plane waves lie on the cone with a density that never vanishes. That the mass term is the frame factor and depends on the boost alone. That his density is the current's modulus, so that the normalisation of his velocity and his $\rho>0$ are definitions and not restrictions. That the mass density is $\Omega=\rho\cos\theta$ and is therefore not the particle density; that $\lvert\cos\theta\rvert=1$ on a free plane wave and falls below it on superpositions, with the values quoted; that $\theta\to\pi-\theta$ under charge conjugation; and that the Eckart-frame energy flux vanishes for a plane wave and for two waves of one momentum and not for the superpositions.

**Interpretation.** That Takabayasi's subsidiary condition is the tensor form of the algebraic non-closure. The structural correspondence is exact — both are statements that the momentum is fixed only up to one function — but the identification of the two conditions is an identification and not a derivation. That his internal angle is the rotor angle. The count forces the pairing once the first four rows are granted, and the sign of the double cover and the chiral operation support it; it is not computed. That his stress remainder is what the word's boost and rotor pieces together would give. That the momentum row's qualifier is resolved by reading his curl as the phase's freedom. That the mass defect is an internal energy per particle; what is computed is the ratio $\cos\theta$, and the energy is a reading of it. That the disparity between his momentum and his velocity is the angle itself, which is his statement quoted and not a derivation; the computed content is the correlation of the two families, $\theta=0$ with $q=0$ and $\theta\neq0$ with $q\neq0$.

**Not claimed.** It is not claimed that the two formulations are the same in the sense of a dictionary with no residue. Three rows are exact, one is forced, one is read. A reader who wants a single theorem will not find one; what is offered is a mapping with its grades named. It is not claimed that the heat flow and the angle are proportional: no number is computed that ties $\lVert q\rVert$ to $\theta$, and the two are checked only to vanish and to be non-zero together.

## Summary

Takabayasi's 1957 formulation of the Dirac field as a relativistic spin fluid and the biquaternion polar word describe the same object. His variables are a density, an invertible element four-velocity, an invertible element spin vector, a momentum and an internal angle. The word's variables are a scale, a phase, a boost and a rotor.

The mapping is graded. The density is the scale squared, the velocity is the boost and the spin is the rotor, and those three rows are identities. The internal angle is the rotor angle, and that row is forced by the count once the first three identities and the one reading are granted: eight parameters on each side, four buckets matched, and the rotor's third parameter and the internal angle are the only two leftovers. The momentum is the phase gradient, and that row holds where his momentum's curl vanishes.

His equations close the count and not the system. The derivative of the word separates into four brackets of four algebraic types — a real scalar, a central imaginary, a Hermitian element and a real vector — and the equation constrains them without determining them. His second subsidiary condition is the tensor form of that non-closure: it fixes the curl of the momentum and leaves one function free.

The current reads the density and the boost; the spin reads the density and the rotor. The separation is the same in both formulations, and the word supplies its reason.

The domain is where the word is smaller. His variables need a non-zero density; the word needs the element to be an invertible element. The one-sided plane waves are nowhere zero, have a positive density, and have no word. That is the difference the comparison finds, and it is a finding about the word.

The trace is the mass term, so the equation of state has one line: the pressure is a third of the energy density less the mass density, and the shear is left open, as the fixed-density table shows. The two densities are the by-product. His $\rho$ is the current's modulus, so the normalisation of his velocity is satisfied by construction, and the density that the mass term couples to is the scalar $\Omega=\rho\cos\theta$ and not $\rho$. A free plane wave has the two equal in magnitude; a superposition does not, and the defect $mc^{2}(1-\cos\theta)$ per particle is the one function of the particle's internal state that the fluid carries — an internal energy per particle, if it is read as one. Charge conjugation flips the sign of the mass density and leaves the particle density, which makes the sign a charge label. His velocity is the current's direction, which is the Eckart frame, and the energy flux it leaves in its own rest frame — the heat flow — vanishes on a plane wave and on two waves of one momentum, and not on a superposition. That flux and the angle vanish together.

No experiment separates the two formulations. What separates them is the origin of the structure: Takabayasi constructs the spin-half fluid and the word reads it. The equation, no; the coordinates, yes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The field, in its word |
| $r$, $\rho_{\mathrm{num}}=r^{2}$ | Scale; proper density |
| $\theta_{\mathrm{pha}}$ | Angle of the word; $S=\hbar\theta_{\mathrm{pha}}$ |
| $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ | Rapidity and unit axis of the boost |
| $\theta_{\mathrm{axr}}$, $\vec u_{\mathrm r}$ | Angle and unit axis of the rotor |
| $\tilde U_{\Psi,\mathrm b}$ | Hermitian positive boost factor |
| $\tilde u_{\mathrm r}$ | Real unit rotor factor |
| $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$ | The frame factor; the four-vector factor |
| $\tilde V_{\Phi}=ic\mathcal B_{\Psi}=\gamma(ic\,e_t+\vec v)$ | Four-velocity |
| $\tilde K_{\Phi}=\tilde\nabla_\Phi\theta_{\mathrm{pha}}$ | The phase gradient; the momentum in wave-number units |
| $\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}$ | The current |
| $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction |
| $\tilde S_{\Psi}=\rho_{\mathrm{num}}\frac{\hbar}{2}i\vec s$ | The spin element |
| $\rho$, $v_\mu$, $w_\mu$, $k_\mu$, $\theta$ | Takabayasi's density, velocity, spin, momentum and internal angle |
| $\Omega=\bar\psi\psi$, $\Omega_{\mathrm{ps}}=i\bar\psi\gamma_5\psi$ | His scalar and pseudoscalar bilinears; $\Omega=\rho\cos\theta$ and $\Omega_{\mathrm{ps}}=\rho\sin\theta$ |
| $j_\mu$ | The current, with $\rho^{2}=\sum_\mu\varepsilon_\mu j_\mu j_\mu=\Omega^{2}+\Omega_{\mathrm{ps}}^{2}$ |
| $k_m=mc/\hbar$ | Mass wave number; the unit that makes his $k_\mu$ dimensionless |
| $u_\mu$, $q_\mu$, $\epsilon$ | Eckart four-velocity, heat flow, and the energy density it sees |
| $\sum_\mu\varepsilon_\mu T_{\mu\mu}=mc^{2}\rho\cos\theta$ | Trace of the stress; the mass term |
| $p$, $\pi^{j}{}_{k}$ | Pressure and the traceless part of the spatial block |
| $N(\tilde\Xi)=\langle\tilde\Xi\rangle_{\natural}$ | Quaternionic norm |
| $c$ | Speed of light in the medium |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter, Part I. General theory," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, the formulation compared here.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the non-relativistic hydrodynamical formulation.
- David Hestenes, *Space–Time Algebra* (Gordon and Breach, 1966; second edition Birkhäuser, 2015), for the geometric reading of the Dirac field as a density, an angle and a rotor.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), §9, for the relativistic spin fluid and the spin-transport equation it must carry.
- Luca Fabbri, *Dirac Theory in Hydrodynamic Form* (2023), for the enumeration of minimal spin-fluid systems and the non-uniqueness of the closing condition.
- C. Eckart, "The thermodynamics of irreversible processes III: Relativistic theory of the simple fluid," *Physical Review* **58** (1940) 919–924, for the frame that follows the current and the first-order entropy production.
- L. D. Landau and E. M. Lifshitz, *Fluid Mechanics*, 2nd edition (Pergamon, 1987), §127, for the frame that follows the energy flux and for the heat flow that separates the two.
- The companion articles: [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), [The Spin-Zero Fluid](the-spin-zero-fluid.html), [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), [The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html).
