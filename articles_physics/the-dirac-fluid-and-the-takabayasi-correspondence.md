# __The Dirac Fluid and the Takabayasi Correspondence__

## Introduction

**The claim of this article is that the biquaternion polar word and Takabayasi's tensor formulation of 1957 are the same fluid described in two languages, and that the correspondence is exact on the domain where both are defined.** Takabayasi's *Relativistic Hydrodynamics of the Dirac Matter* replaces the spinor and the gamma matrices by a set of real tensor fields — a density, a velocity, a spin vector, a momentum and one internal angle. The polar word writes the same field as one element of $\mathbb{B}$ decomposed into four factors. Every variable of the tensor system is a factor of the word or a component of one.

**The article is a comparison and not a derivation.** The word, its four brackets, its current and its spin are [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html). Takabayasi's system is his. What is new here is the mapping between them, the reason each row of the mapping holds, and the ledger of what the comparison buys.

**The ledger is short and it is stated at the outset.**

- **No new prediction.** Nothing in the biquaternion reading predicts what the tensor formulation does not predict.
- **No new solution.** The general solution is the Fourier superposition of plane waves in both.
- **A cleaner origin.** The spin fluid, its non-closure, its current–spin separation and its domain all follow from the factorisation of one element, and in the tensor language they are imposed by hand.

**The correspondence is graded, and the grades matter.** Three of the five rows are read off the algebra as identities. One is a reading of the momentum as a gradient, which holds only where his curl vanishes, so it is a reading and not an identity. The last is forced by the count once the first four are granted, and is supported by two further arguments that are not computations. The table in §*The Variable Mapping* marks each row with its grade, and a reader who wants only the secure part can take the first three rows and leave the rest.

## The Tensor Formulation

**Takabayasi's starting point is the set of bilinear covariants of the Dirac field.** There are sixteen of them, and kinematical identities relate them, so that seven real quantities independent at each event remain. He writes them as a density, a unit timelike four-velocity and a unit spacelike four-vector orthogonal to it:

$$
\rho>0,
\qquad
v_\mu v^{\mu}=-1,
\qquad
w_\mu w^{\mu}=1,
\qquad
v_\mu w^{\mu}=0 .
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
| $k_\mu$, the momentum | $\tilde K_{\Phi}=\tilde\nabla_\Phi\theta_{\mathrm{pha}}$, the phase gradient | reading, with a qualifier |
| $\theta$, the internal angle | $\theta_{\mathrm{axr}}$, the rotor angle | forced by the count, given the first four rows |

**The first three rows are identities and they are the corpus's own statements.** The density of the word is $\rho_{\mathrm{num}}=r^{2}$, read from the scale. The four-velocity is $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}=\gamma(ic\,e_t+\vec v)$, read from the boost, with $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$ for every field. The spin is $\tilde S_{\Psi,\mathrm{sp}}=\rho_{\mathrm{num}}\frac{\hbar}{2}i\vec s$ with $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, read from the rotor. These are not correspondences of formulas; they are the same three objects named twice.

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

**The thing that is not the current is worth one paragraph here, because Takabayasi's formulation does not have the problem.** The algebra's own bilinear $i\tilde\Xi\tilde\Xi^{*}$ is the current's mirror image: its temporal slot agrees with $\tilde J_{\Phi}$ up to the factor $c$ and its spatial part is reversed, because the star conjugation fixes the boost and cancels the rotor and the outer $i$ then reverses the spatial vector. Takabayasi defines his current as $\rho v_\mu$ directly and never meets this. The corpus meets it because it tries to read the current from a bilinear of the algebra, and [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) carries the analysis of the failure.

## The Domain

**Takabayasi assumes $\rho>0$ and derives. The word states its domain and the domain is smaller.**

**His assumption and the word's condition are different conditions.** The factorisation $\rho v_\mu$ with $v_\mu$ a unit vector needs $\rho\neq0$. The word needs $N(\tilde\Xi)\neq0$, which is the condition that the element be a unit of the algebra. For the scalar field the two agree. For the spinor field they do not.

**Two families of Dirac fields have $\rho\neq0$ everywhere and no word anywhere.**

- **Parts of definite value.** An element with $\tilde X\vec e_z=\pm i\tilde X$ is a zero divisor at every amplitude, because $\tilde X(\vec e_z\mp ie_t)=0$ and the bracket is not zero. Every field of definite chirality is of this kind.
- **One-sided plane waves.** A plane wave with $\tilde K_{\Phi}\tilde\Xi_{0}=0$ and $\tilde K_{\Phi}$ null has $N(\tilde\Xi_{0})=0$ everywhere. It is nowhere zero and its density never vanishes, and its word does not exist.

**The second family is the one that matters physically**, because a one-sided wave is what a massless helicity eigenstate is. His variables $\rho$, $v_\mu$ and $w_\mu$ are defined on it, since $\rho>0$. **Whether his formulation proceeds on it is a separate question.** Several of his quantities carry the factor $1/k_m=\hbar/(mc)$, so they diverge at $m=0$ and the massless field is a limit rather than a case, and whether that limit exists for a one-sided wave is not settled here. What the comparison establishes is a difference of domain conditions: the word needs the element to be a unit, which is strictly stronger than $\rho\neq0$, and the one-sided wave is the field that exhibits the difference.

**What survives on the cone is the two-factor decomposition.** Every element is $\tilde\Xi=\tilde\Xi_{H}\tilde\Xi_{0}$ with $\tilde\Xi_{H}$ Hermitian positive semidefinite and $\tilde\Xi_{0}$ a partial isometry, and that factorisation is defined on the whole algebra. It separates a scale from a direction but not a velocity from a spin, so it is not enough for a fluid. The four-factor word is the finer decomposition and it is the one that fails.

**This is a finding and not a criticism of Takabayasi.** His variables are defined for the fields he treats, and the cone is outside his scope. What the comparison adds is the identification of the boundary, and the boundary is the price of the word.

## The Mass Term and the Stress

**The mass term is a number in his formulation and a frame factor in the word.** In the standard reading the mass is a scalar coupling the two chiral parts, invariant in every frame. In the word the kinetic relation between the parts is $\tilde\Xi_{0}^{L}=-\mathcal B_{\Psi}\tilde\Xi_{0}^{R}$ with $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$, so the mass's sign is carried along by the boost and the momentum carries the same boost. At rest the factor is the identity and the relation is the plain sign. The two statements agree; what the word adds is where the scalar goes in a moving frame.

**His energy-momentum tensor separates into a particle part and a stress part.** Takabayasi writes $L_{\mu\nu}$ as a momentum transport term $\rho k_\mu v_\nu$ plus a remainder, and reads the remainder as the mechanical stress and heat flow inside the fluid. The remainder is not a pure spin term: it carries the gradient of the internal angle multiplied by the spin direction, and the spin density contracted with the curl of the velocity. The conservation law is the equation of motion for the particle momentum, and the remainder represents the quantum effects.

**The remainder is a mix, and the correspondence is not a computed equality.** The word splits the derivative into a boost connection and a rotor connection, and a split of the derivative is not a split of the stress. Takabayasi's remainder draws on both: the angle's gradient is a rotor quantity, the spin direction is a rotor quantity, and the curl of the velocity is a boost quantity. So the honest statement is that the remainder is not the rotor's contribution alone, and that no term-by-term identification of it with the word's boost and rotor pieces is computed in this corpus. The relativistic quantum stress is exhibited in [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) for the scalar case, and the spinor case's antisymmetric part is the subject of the articles that follow this one.

## What the Correspondence Adds and What It Does Not

### What it adds

**The origin of the spin fluid.** Takabayasi constructs the fluid from the bilinears of the field. The word reads it from the factorisation of one element: the four factors are the fluid's variables and the four brackets are its equations. The construction becomes a reading.

**The explanation of the subsidiary condition.** Takabayasi imposes his condition to close the system. The word shows that the system's non-closure is the algebraic independence of four brackets of four types, and his condition is one way to close it.

**The reason for the current–spin separation.** In the tensor language the separation is a fact about bilinears; in the word it follows from the Hermitian factor carrying the boost and the real-unitary factor carrying the rotor.

**The reason the vorticity is not a dynamical variable.** A classical fluid's vorticity is derived and then transported, with Helmholtz's theorems and a conserved helicity. The word's vorticity is a function of the boost's gradient and of nothing else, so the transport law has nothing to act on and the invariant of a loop is the frame's holonomy rather than a circulation. [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) carries the classical side of that distinction.

**The precise domain.** His variables need $\rho\neq0$; the word needs the element to be a unit, and for the spinor field the second condition is strictly stronger. The one-sided waves are the fields that show the difference.

**The mass term's frame dependence.** The scalar coupling is a frame factor, and the factor is the same one the velocity carries.

### What it does not add

**No prediction.** The two formulations make the same predictions, and there is no experiment that separates them.

**No solution.** A plane wave is a plane wave in both. The word reads each mode and does not solve the equation.

**No removal of the non-uniqueness.** The closing condition is still a choice. Takabayasi makes one, the spin-hydrodynamics literature makes others, and the corpus records the choice without making it.

**Where the Dirac fluid stands among the three.** The block now has a fluid per spin, and they are compared side by side in [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html)'s §*The Three Fluids* and in [The Proca Fluid](the-proca-fluid.html)'s: the scalar field is a gradient flow with a Korteweg stress and no orientation, the Proca field is a charged flow with a London response and no orientation, and this one is a flow with an orientation — a Cosserat medium but not the constrained one. Takabayasi's own subsidiary condition is the constraint that would make it the constrained case, and that is the sharpest way to say what his tensor fluid is and what the word's is.

**The one-sentence ledger is: the equation, no; the coordinates, yes.** Takabayasi's tensor calculus is the equation in tensor form. The polar word is the coordinates in which the equation's structure is algebraic.

## What Is Established and What Is Interpretation

**Established.** That the first three rows of the mapping are identities of the corpus's own definitions. That the count of eight functions matches on both sides and that the fifth row is the only consistent assignment of the two leftovers. That the derivative of the word separates into four brackets of four distinct types, and that the Dirac equation constrains them without closing them. That the current reads the boost and the spin reads the rotor. That the word's domain is the set of units and that the one-sided plane waves lie on the cone with a density that never vanishes. That the mass term is the frame factor and depends on the boost alone.

**Interpretation.** That Takabayasi's subsidiary condition is the tensor form of the algebraic non-closure. The structural correspondence is exact — both are statements that the momentum is fixed only up to one function — but the identification of the two conditions is an identification and not a derivation. That his internal angle is the rotor angle. The count forces the pairing once the first four rows are granted, and the sign of the double cover and the chiral operation support it; it is not computed. That his stress remainder is what the word's boost and rotor pieces together would give. That the momentum row's qualifier is resolved by reading his curl as the phase's freedom.

**Not claimed.** It is not claimed that the two formulations are the same in the sense of a dictionary with no residue. Three rows are exact, one is forced, one is read. A reader who wants a single theorem will not find one; what is offered is a mapping with its grades named.

## Summary

Takabayasi's 1957 formulation of the Dirac field as a relativistic spin fluid and the biquaternion polar word describe the same object. His variables are a density, a unit four-velocity, a unit spin vector, a momentum and an internal angle. The word's variables are a scale, a phase, a boost and a rotor.

The mapping is graded. The density is the scale squared, the velocity is the boost and the spin is the rotor, and those three rows are identities. The internal angle is the rotor angle, and that row is forced by the count once the first three identities and the one reading are granted: eight parameters on each side, four buckets matched, and the rotor's third parameter and the internal angle are the only two leftovers. The momentum is the phase gradient, and that row holds where his momentum's curl vanishes.

His equations close the count and not the system. The derivative of the word separates into four brackets of four algebraic types — a real scalar, a central imaginary, a Hermitian element and a real vector — and the equation constrains them without determining them. His second subsidiary condition is the tensor form of that non-closure: it fixes the curl of the momentum and leaves one function free.

The current reads the density and the boost; the spin reads the density and the rotor. The separation is the same in both formulations, and the word supplies its reason.

The domain is where the word is smaller. His variables need a non-zero density; the word needs the element to be a unit. The one-sided plane waves are nowhere zero, have a positive density, and have no word. That is the difference the comparison finds, and it is a finding about the word.

No experiment separates the two formulations. What separates them is the origin of the structure: Takabayasi constructs the spin fluid and the word reads it. The equation, no; the coordinates, yes.

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
| $\rho$, $v_\mu$, $w_\mu$, $k_\mu$, $\theta$ | Takabayasi's density, velocity, spin, momentum and internal angle |
| $N(\tilde\Xi)=\langle\tilde\Xi\rangle_{\natural}$ | Quaternionic norm, the determinant |
| $c$ | Speed of light in the medium |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter, Part I. General theory," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, the formulation compared here.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the non-relativistic hydrodynamical formulation.
- David Hestenes, *Space–Time Algebra* (Gordon and Breach, 1966; second edition Birkhäuser, 2015), for the geometric reading of the Dirac field as a density, an angle and a rotor.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), §9, for the relativistic spin fluid and the spin-transport equation it must carry.
- Luca Fabbri, *Dirac Theory in Hydrodynamic Form* (2023), for the enumeration of minimal spin-fluid systems and the non-uniqueness of the closing condition.
- The companion articles: [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html).
