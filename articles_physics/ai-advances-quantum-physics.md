# __AI Advances Quantum Physics__

## Introduction

This article is the entry point to the quantum half of the biquaternion programme. One algebra of eight real dimensions is cut in two by the Hermitian conjugation; the anti-Hermitian half carries relativity, and the **Hermitian half** carries quantum physics. This article states what that second half contains, and why the arrangement is a reduction of the standard formalism rather than a redescription of it.

The claim is narrow enough to be checked. The states, the observables, the probabilities, the dynamics and the update rule are not five structures that happen to fit together. They are one subspace of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ read in five ways. The Born rule is a **ratio of two scalar parts**. Collapse is **idempotence**. Purity is the **vanishing of a norm**. The qubit is the **defining module** of the algebra. Nothing is added to the algebra; what is added is the reading.

## The Standard Formalism, in Six Lines

**The skeleton.** A quantum theory needs six things: a state space, observables, a Born rule, a dynamics, a measurement rule, and a composition rule. In the standard formulation they are a Hilbert space $\mathcal{H}$ with density operators $\rho$ as states; Hermitian operators $A$ as observables; probabilities $\operatorname{Tr}(\rho P)$ for the spectral projection $P$; unitary evolution $\rho\mapsto U\rho U^{\dagger}$; the Lüders update $\rho\mapsto P\rho P/\operatorname{Tr}(P\rho)$; and the tensor product with the partial trace.

**Beyond the skeleton.** A theory also needs a symmetry group, a relativistic extension, a classical limit, and an interpretation. Those are the ten items of the checklist that *Quantum Physics: Foundations and Structure* sets out, and against which the reformulation is measured here.

**What is separate and what is assumed.** In the standard formulation the six are postulates. Each is stated on its own, and the consistency between them — that the Born rule is preserved by the dynamics, that the update agrees with the rule — is a theorem to be checked. The reformulation is interesting only if that separation weakens, and it does.

## The Same Formalism in the Biquaternion Algebra

**The sector.** Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, where $e_t$ is the identity and $\vec e_k^2=-e_t$. Let ${}^{\natural}$ fix the scalars and negate the vectors, and let ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ be its composition with complex conjugation. The **Hermitian subspace** is the fixed-point set of the star,

$$
\mathbb{B}_{\Psi}=\{\tilde H\in\mathbb{B} : \tilde H^{*}=\tilde H\}
=\bigl\{h_t\,e_t+i(h'_x\vec e_x+h'_y\vec e_y+h'_z\vec e_z) : h_t,h'_\mu\in\mathbb{R}\bigr\},
$$

a real vector space of dimension four. Its elements are written $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ with $\vec h_\Psi\in\mathbb{R}^3$. This one space is the state space and the observable space at once.

**The two forms.** The algebra carries four forms, the scalar parts of the four general products. On $\mathbb{B}_{\Psi}$ they pair off and two remain:

$$
\langle\tilde H_{\Psi,1},\tilde H_{\Psi,2}\rangle_{*}=\mathrm{Sc}\bigl(\tilde H_{\Psi,1}\tilde H_{\Psi,2}^{*}\bigr)=h_{t,1}h_{t,2}+\vec h_{\Psi,1}\cdot\vec h_{\Psi,2},
\qquad
\langle\tilde H_\Psi\rangle_{\natural}=\tilde H_\Psi\tilde H_\Psi^{\natural}=h_t^2-\lvert\vec h_\Psi\rvert^2 .
$$

The first is **positive definite**, of inertia $(4,0)$: the Hilbert–Schmidt inner product, and the form the Born rule and the dynamics use. The second is **Lorentzian**, of inertia $(1,3)$: the form whose cone decides which elements are states. Two forms, two jobs, one element.

**The state.** A state of a qubit is the element

$$
\tilde{Ϛ}_{\Psi}=\tfrac12\bigl(e_t+i\vec s_{\Psi}\bigr),\qquad \vec s_{\Psi}=(s_x,s_y,s_z)\in\mathbb{R}^3,\qquad \lvert\vec s_{\Psi}\rvert\leq1,
$$

normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$. The weight $\tfrac12$ is not a convention: $\tilde\Pi=\alpha(e_t+i\vec u)$ satisfies $\tilde\Pi^2=\tilde\Pi$ only for $\alpha=\tfrac12$, and idempotency is what a rank-one projection has to satisfy.

**Three readings of one condition.** The positivity $\lvert\vec s_{\Psi}\rvert\leq1$ is one statement in three languages: the eigenvalues $\lambda_\pm=(1\pm\lvert\vec s_{\Psi}\rvert)/2$ are non-negative; the biquaternion norm is non-negative,

$$
\boxed{\ \langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}=\tfrac14\bigl(1-\lvert\vec s_{\Psi}\rvert^{2}\bigr)e_t\ },
$$

and the element lies in the future light cone of that norm. The **Bloch ball is the slice of the cone** at $\mathrm{Sc}=\tfrac12$. The boundary is $\lvert\vec s_{\Psi}\rvert=1$, where the norm vanishes: the **pure states are the zero divisors** of $\mathbb{B}_{\Psi}$ at that normalisation, and equivalently the idempotents, $\tilde\Pi_{1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$ with $\lvert\vec u\rvert=1$. Pure, idempotent, zero divisor, on the cone: four names, one condition.

**The observable.** An observable is a general Hermitian element $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$. Its eigenvalues are $\lambda_\pm=h_t\pm\lvert\vec h_\Psi\rvert$ and its eigenprojectors are the two idempotents along $\vec h_\Psi$: the spectral theorem of a Hermitian matrix, read on the element itself. The state and the observable live in the same four-dimensional space, told apart by one scalar, the weight, and by one inequality.

## The Born Rule Is a Ratio

**The expectation value.** For a state $\tilde{Ϛ}_{\Psi}$ and an observable $\tilde H_\Psi$, the expectation is the normalised Hermitian form,

$$
\langle\tilde H_\Psi\rangle_{\tilde{Ϛ}_{\Psi},*}
=\frac{\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
=\frac{\mathrm{Sc}\bigl(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*}\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}_{\Psi}\bigr)}
=h_t+\vec s_{\Psi}\cdot\vec h_\Psi .
$$

Only the scalar part of $(i\vec s_{\Psi})(i\vec h_\Psi)$ survives, and it is the dot product; the cross product is the vector part and drops out. **No postulate enters**: the value is the form, the normalisation is the form against the unit, and the ratio is what a probability with weight $\tfrac12$ must be.

**The probabilities.** For a projective measurement along $\vec u_\Psi=\vec h_\Psi/\lvert\vec h_\Psi\rvert$,

$$
\boxed{\ p_\pm=\tfrac12\bigl(1\pm\vec u_\Psi\cdot\vec s_{\Psi}\bigr)\ }
$$

which is the cosine rule on the Bloch ball and nothing more. At $\vec s_{\Psi}=\vec u_\Psi$ the outcome $+$ is certain; at $\vec s_{\Psi}\cdot\vec u_\Psi=0$ the two outcomes are equally likely.

**The mixed case is the same formula.** Nothing above assumes that $\tilde{Ϛ}_{\Psi}$ is idempotent, so the ratio covers the mixed states, the maximally mixed $\tfrac12 e_t$ giving one half for every outcome. The Born rule is one formula, not a pure case plus an averaging.

**The update.** After the outcome $+$ the state is

$$
\tilde{Ϛ}_{\Psi,\mathrm{out}}=\frac{\tilde\Pi_1(\vec u_\Psi)\,\tilde{Ϛ}_{\Psi}\,\tilde\Pi_1(\vec u_\Psi)}{2\,\mathrm{Sc}\bigl(\tilde\Pi_1(\vec u_\Psi)\tilde{Ϛ}_{\Psi}^{*}\bigr)}=\tilde\Pi_1(\vec u_\Psi),
$$

because a rank-one projection absorbs what it multiplies: $P\tilde{Ϛ}_{\Psi}P=(\operatorname{Tr}P\tilde{Ϛ}_{\Psi})P$ in the $2\times2$ image, and $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$ reads the multiple back as the probability. **Collapse is the statement that the idempotent is idempotent.**

## The Dynamics Is a Conjugation

**The rotor.** Time evolution is conjugation by a one-parameter group of $*$-unitary elements, $\tilde Q\tilde Q^{*}=e_t$,

$$
\tilde{Ϛ}_{\Psi}(r'_t)=\tilde Q(r'_t)\,\tilde{Ϛ}_{\Psi}(0)\,\tilde Q(r'_t)^{*},
\qquad
i\hbar c\,\frac{d}{dr'_t}\tilde Q(r'_t)=\tilde H_\Psi\,\tilde Q(r'_t),\quad \tilde Q(0)=e_t,
$$

with $r'_t=ct'$ the coordinate time carried as a length. The solution closes because the scalar and vector parts of $\tilde H_\Psi$ commute,

$$
\tilde Q(r'_t)=\exp(-i\theta_{\mathrm{evo}})\Bigl(\cos\theta\,e_t+\sin\theta\,\vec u_\Psi\Bigr),
\qquad
\theta_{\mathrm{evo}}=\frac{h_t\,r'_t}{\hbar c},\quad \theta=\frac{\lvert\vec h_\Psi\rvert\,r'_t}{\hbar c},
$$

and $\vec u_\Psi^2=-e_t$ turns the exponential of the vector part into a cosine and a sine.

**What cancels.** The factor $\exp(-i\theta_{\mathrm{evo}})$ is a central complex scalar and cancels in the two-sided product: only the **vector part** of the Hamiltonian moves the state, while the scalar part produces a global, unobservable phase. The cancellation is visible rather than asserted, because the phase is central in the algebra.

**The generator.** In differential form the state obeys $i\hbar c\,d\tilde{Ϛ}_{\Psi}/dr'_t=[\tilde H_\Psi,\tilde{Ϛ}_{\Psi}]$, the von Neumann equation with the biquaternion commutator. The Schrödinger and Heisenberg pictures are the same conjugation read on the rotor and on the observable.

**Why the group is $\mathrm{U}(2)$.** The condition $\tilde Q\tilde Q^{*}=e_t$ is one equation on four complex coordinates and leaves the four-dimensional group $\mathrm{U}(2)$. Its $SU(2)$ part produces the spin rotations, and those act on the Bloch sphere through $\mathrm{SO}(3)$. The relativity section's group is the other normalisation in the same algebra, $\tilde U\tilde U^{\natural}=e_t$, which is $\mathrm{SL}(2,\mathbb{C})$: the same conjugation, a different condition, and the subject of *AI describes the Lorentz Group*.

## What Comes Out of the Algebra Rather Than Into It

Five things that the standard formulation postulates, or derives case by case, are consequences of one object here.

**The Born rule.** A ratio of scalar parts, as above. It is not added, and the factor $2$ of the $2\times2$ image cancels in the ratio, so the rule reads the same in the algebra as in the matrix model.

**Collapse.** An idempotent times a state times the idempotent is the idempotent, up to a scalar that the normalisation removes. The projection postulate becomes a computation.

**Purity, entropy, fidelity.** Purity is $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}^2)=\tfrac12(1+\lvert\vec s_{\Psi}\rvert^2)$, and the deviation of the element from idempotence is the same number read the other way, $\tilde{Ϛ}_{\Psi}^2-\tilde{Ϛ}_{\Psi}=\tfrac14(\lvert\vec s_{\Psi}\rvert^2-1)e_t$. The von Neumann entropy in bits, $S=-\lambda_+\log_2\lambda_+-\lambda_-\log_2\lambda_-$, is a function of the biquaternion norm alone, and the fidelity of two pure states is $2\,\mathrm{Sc}(\tilde\Pi_{\mathrm p}\tilde\Pi_{\mathrm q}^{*})=\tfrac12(1+\vec u_{\mathrm p}\cdot\vec u_{\mathrm q})$, which is $\cos^2(\theta/2)$ in biquaternion letters.

**The three spins.** The regular module of the algebra contains exactly three irreducible subcarriers, of dimensions $1$, $2$ and $3$: the scalar $Z=\mathbb{C}e_t$ with spin $0$, the spinor $S_\pm$ with spin $\tfrac12$ and Casimir $\tfrac34\hbar^2$, and the vector with spin $1$. There is no fourth: the irreducible dimensions are $1,2,3$, the only four-dimensional invariant subspace is the algebra itself, and $1+2+3=6>4$ says the three can never be the constituents of one carrier. **Spin is the Casimir label of a carrier, not a direction**; the direction labels a state.

**The qubit.** An algebra isomorphic to $M_2(\mathbb{C})$ has exactly one simple left module, the column space $S=\mathbb{C}^2$, and the rank-one projections on $S$ are exactly the unit-weight idempotents of $\mathbb{B}_{\Psi}$. The qubit is not postulated: it is the module the algebra has.

## Three Extensions in the Informational Sector

**The relativistic qubit.** The module $S$ with the left action of the unit-norm group $\mathrm{SL}(2,\mathbb{C})$ is the relativistic qubit. Its state space is not invariant under the whole group: a boost scales the spinor norm, so only the compact $SU(2)$ acts $*$-unitarily, and at fixed four-velocity the physical spin transforms by the **Wigner rotation**, an element of $SU(2)$ assembled from two boosts. The pure states, the rays of $S$, are the **celestial sphere**, and each ray determines a future null direction through $\tilde{\mathcal L}_{\Phi}(u)=\tfrac{i}{2}e_t-\tfrac12\vec s_{\Psi}$, an element of vanishing biquaternion norm. The Bloch sphere of the non-relativistic theory and the celestial sphere of the relativistic one are one sphere seen from the two sectors.

**Frame-dependent entropy.** The entropy is a function of the biquaternion norm, and the norm is invariant under $*$-unitary conjugation, so the entropy is constant on the $SU(2)$ orbits and is a **complete invariant** of them. A boost is not $*$-unitary and does change the entropy: at uncertain momentum it acts as the channel $\tilde{Ϛ}_{\Psi}\mapsto\sum_i w_i\tilde U_{\mathrm{Wig},i}\tilde{Ϛ}_{\Psi}\tilde U_{\mathrm{Wig},i}^{*}$, which dephases a transverse spin and leaves the maximally mixed state fixed. Spin entropy is therefore frame-dependent in a controlled way, and *Spin Entropy and the Lorentz Group* computes the two regimes.

**The split as a superselection structure.** The decomposition $\mathbb{B}=\mathbb{B}_{\Phi}\oplus\mathbb{B}_{\Psi}$ is the eigenspace decomposition of the real structure $\flat=-{}^{*}$, and it satisfies the operational conditions: no operation of the framework maps one summand into the other, and the relative phase between them is unobservable. It does not satisfy the algebraic one: the centre is $\mathbb{C}e_t$, the algebra is central simple, and the defining module is irreducible. What the split gives sharply is a **grading of the Lie algebra**, the Cartan decomposition $\mathrm{SL}(2,\mathbb{C})=\mathbb{B}_{\Psi}^{0}\oplus\mathbb{B}_{\Phi}^{0}$ with $\flat$ the Cartan involution; and from $[\text{boost},\text{boost}]=\text{rotation}$ comes the Wigner rotation, as the algebraic origin of a kinematic effect.

**The measurement problem, restated.** The framework offers one operation form, $\tilde Q\mapsto\tilde Q_3\tilde Q\tilde Q_3^{*}$, with the acting element either $*$-unitary or an idempotent: two dynamics, one form. Decoherence is the trace-preserving conditional expectation onto the pointer subalgebra, and what remains is the gap between a **mixture** and an **outcome**, a segment and an endpoint. The restatement is exact and it does not close that gap; *The Measurement Problem in Algebraic Form* says where it lies.

## One Scale in Three Wavenumbers

**The three.** A free particle carries one wave number in three guises: the **mass** wave number $k_m=mc/\hbar$, the **momentum** wave number $k_{\Phi}=p/\hbar$, and the **energy** wave number $k'_t=E/(\hbar c)$. They are one biquaternion $\tilde K_{\Phi}$, and the mass shell is its norm,

$$
\boxed{\ \tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_t'^{2}+\vec k_{\Phi}^{\,2}=-k_m^{2}\ }
\qquad\Longleftrightarrow\qquad
k_t'^{2}=k_{\Phi}^{2}+k_m^{2}.
$$

The energy wave number is the hypotenuse and the other two are the legs: a right triangle whose right angle is at the mass side.

**The criterion.** Non-relativistic quantum mechanics applies when $k_{\Phi}\ll k_m$, equivalently when $\gamma\simeq1$. The hydrogen atom satisfies it with the room of $a_0k_{m_e}=1/\alpha=137.036$, so the small parameter of the non-relativistic limit **is** the fine-structure constant, and the size of the atom is its statement.

**The ladder.** One conversion, $\hbar c=197.32698\ \mathrm{MeV}\cdot\mathrm{fm}$, gives a wave number for every energy and, with $k_BT$ in place of $E$, for every temperature. The electron's mass wave number is $2.5896\times10^{12}\ \mathrm{m^{-1}}$, an inverse length of $386.159\ \mathrm{fm}$; room temperature is $1.310\times10^{5}\ \mathrm{m^{-1}}$.

## What the Framework Does Not Say

**It does not solve the measurement problem.** It restates it in one algebraic form and locates the gap; it does not close it, and nothing here says otherwise.

**It does not fix an interpretation.** The natural reading is algebraic, the states and observables being elements of $\mathbb{B}_{\Psi}$ from which the quantum structure follows, and it is compatible with the Copenhagen, relational and informational readings without choosing among them. What the algebra decides and what it leaves open is the subject of *The Ontology of the Quantum State*.

**It does not predict the particle content.** The three spins are the three irreducible subcarriers, and the observed elementary particles carry exactly those spins, but the match is a match of labels. The framework says which spins are available, not which particles exist.

**It does not change a number.** The single-qubit predictions are the standard ones: the Born rule, the Bloch sphere and the projective update are reproduced, not corrected. What changes is the number of independent postulates and the place where each statement lives.

**It does not reach the interacting relativistic theory from here.** This article is the qubit sector. The relativistic extension is the celestial-sphere action above; the field theory, the gauge structure and the thermodynamics of the framework are separate categories of the menu, and each states its own status.

## Summary

**One object.** The Hermitian subspace $\mathbb{B}_{\Psi}$ of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is a real four-dimensional space carrying two forms, the positive definite Hermitian form and the Lorentzian biquaternion norm.

**The state.** A state is a positive unit-weight element, $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$ with $\lvert\vec s_{\Psi}\rvert\leq1$: the Bloch ball, which is the slice of the future light cone of the norm. Pure states are the idempotents, equivalently the zero divisors, equivalently the points of the cone.

**The rule.** The Born rule is the normalised Hermitian form, $p_\pm=\tfrac12(1\pm\vec u_\Psi\cdot\vec s_{\Psi})$, a ratio of scalar parts rather than a postulate.

**The dynamics.** Evolution is conjugation by a $*$-unitary rotor obeying the Schrödinger equation; only the vector part of the Hamiltonian acts on the state, the scalar part being a central phase.

**The update.** Collapse is multiplication by the outcome idempotent; the idempotent absorbs the state, and the normalisation returns the probability.

**The additions.** Purity is idempotence, entropy is a function of the biquaternion norm, the qubit is the defining module, the three spins are the three irreducible subcarriers, and the split of the algebra is a Cartan grading whose bracket is the origin of the Wigner rotation.

**The limits.** The measurement problem is restated and not closed, the interpretation is left open, the particle content is not predicted, and no prediction of the standard theory is altered.

## Further Reading

- [Quantum Physics: Foundations and Structure](quantum-physics-foundations-and-structure.html), for the standard formalism and the ten-point checklist applied here.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the full derivation of every result summarised in this article.
- [The Ontology of the Quantum State under the Biquaternion Framework](the-ontology-of-the-quantum-state-under-the-biquaternion-framework.html), for what the state element is, and what it is not.
- [The Measurement Problem in Algebraic Form](the-measurement-problem-in-algebraic-form.html), for the single operation form and the mixture-versus-outcome gap.
- [The Determination of the Possible Spins in Biquaternionic Form](the-determination-of-the-possible-spins-in-biquaternionic-form.html), for the three irreducible subcarriers and the absence of a fourth.
- [The Relativistic Qubit in Biquaternionic Form](the-relativistic-qubit-in-biquaternionic-form.html), for the module $S$, the celestial sphere and the Wigner rotation.
- [Spin Entropy and the Lorentz Group in Biquaternionic Form](spin-entropy-and-the-lorentz-group-in-biquaternionic-form.html), for the frame dependence of the entropy and the two regimes.
- [The Material–Informational Split as a Superselection Structure](the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html), for what the split gives and what it does not.
- [The Three Wavenumbers of a Particle](the-three-wavenumbers-of-a-particle.html), for the triangle of $k_m$, $k_{\Phi}$ and $k'_t$ and the non-relativistic criterion.
- [AI describes the Lorentz Group](ai-describes-the-lorentz-group.html), for the other half of the same algebra.
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic formulation and its scalar-product obstruction.
