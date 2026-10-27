# __Thermality from the Modular Pair: State, Clock and the Definite Reading__

## Introduction

The biquaternion algebra has no temperature. Temperature is a property of a state, and a state is a functional on the algebra together with a modular pair. The modular pair supplies a one-parameter group, the modular flow, and the KMS condition turns that flow into a clock: a state is thermal when its modular flow is periodic in imaginary time with period $\beta$, and the temperature is $1/\beta$.

The biquaternion algebra supplies one modular pair, and it is definite. With the Hermitian star, the trace $\mathrm{Sc}$ and the cyclic separating unit $e_t$, the Tomita operator is the star itself, the modular operator is the identity, and the modular flow is trivial. The trace state has no thermal clock. A non-tracial state would give a non-trivial modular operator and a non-trivial clock; the algebra permits it, but the corpus computes only the trace case. The indefinite reading does not supply a modular pair at all: the Krein adjoint of a left multiplication is a right multiplication, the left regular image is not closed under it, and the envelope has no separating vector.

The article reads the modular structure physically: the modular flow as the clock of a state, the KMS condition as the period, the trace state as the no-temperature case, the modular conjugation as the exchange of the two sides, and the indefinite obstruction as the statement that thermality is a definite-form notion. It proves nothing; the Tomita operator and the obstruction are those of *The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra* and *The Biquaternion Algebra and the Krein–von Neumann Property*.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The Tomita operator, the polar decomposition and the modular flow | [The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra](../articles_maths/the-tomita-operator-and-the-j-modular-pair-for-the-biquaternion-algebra.html) |
| The obstruction in the indefinite reading | [The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra](../articles_maths/the-tomita-operator-and-the-j-modular-pair-for-the-biquaternion-algebra.html), §*The Indefinite Obstruction* |
| The Krein adjoint and the failure of the Krein–von Neumann property | [The Biquaternion Algebra and the Krein–von Neumann Property](../articles_maths/the-biquaternion-algebra-and-the-krein-von-neumann-property.html) |
| The modular reading of the Cartan amplitude | [The Cartan Pairing: Amplitude and the Operator-to-State Map](the-cartan-pairing-amplitude-and-the-operator-to-state-map.html) |
| The two sides and the commutant | [Operators and the Three Actions](the-element-and-operator-representations.html) |
| The indefinite form and its cones | [The Krein Form and the Indefinite Structure](the-krein-form-and-the-indefinite-structure.html) |
| The state space and the Born form | [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) |
| The modular clock | [Time from the Algebra: Clock, Rate and Period](time-from-the-algebra-clock-rate-and-period.html) |

## The Modular Pair

### The Data

A modular pair is a von Neumann algebra $\mathcal M$ with a cyclic and separating vector $\xi$. The Tomita operator is the antilinear map

$$
S(\Lambda\xi)=\Lambda^{*}\xi,
\qquad
\Lambda\in\mathcal M,
$$

and its polar decomposition is

$$
S=\jmath\,\Delta^{1/2}.
$$

The **modular operator** $\Delta$ is positive and self-adjoint; the **modular conjugation** $\jmath$ is antiunitary; the **modular flow** is

$$
\sigma_t(\Lambda)=\Delta^{it}\Lambda\Delta^{-it}.
$$

The flow is a one-parameter automorphism group of the algebra, and it is the clock of the state.

### The Definite Pair

For the biquaternion algebra with the Hermitian star, the trace $\mathrm{Sc}$ and $\xi=e_t$, the algebra is $\mathcal M=\{L_{\tilde Q}\}\cong M_2(\mathbb{C})$, the unit is cyclic and separating, and the Tomita operator is

$$
S(\tilde Q)=\tilde Q^{*}.
$$

It is antilinear, involutive and antiunitary, so the polar decomposition is

$$
\Delta=\mathrm{id},
\qquad
\jmath={}^{*},
\qquad
\sigma_t=\mathrm{id}.
$$

The modular flow is trivial. The reason is that the vector state of the unit is the trace:

$$
\omega(L_{\tilde Q})=\mathrm{Sc}(\tilde Q)=Q_t,
$$

and a tracial state has a trivial modular operator. The triviality is a property of the vector, not of the algebra: the algebra is a factor, and a cyclic and separating vector other than a scalar multiple of $e_t$ carries a non-tracial vector state and hence a non-trivial modular operator.

### The Reading

The modular flow is the **clock of the state**. The state selects a one-parameter group; the group is the state's own time. The algebra supplies the group structure; the state supplies the flow. The reading is the algebraic form of the statement that a thermal system has a time direction given by its state, not by the algebra.

The definite pair is the pair of the Born form. The trace is the state of maximal ignorance, and its clock is stopped. The physical reading is the infinite-temperature state: no modular Hamiltonian, no period, no temperature. The state is thermal at every $\beta$ in the KMS sense, and it fixes none.

## The KMS Condition

### The Period

A state $\omega$ is **KMS at inverse temperature $\beta$** with respect to a flow $\sigma_t$ if

$$
\omega(A\,\sigma_{i\beta}(B))=\omega(BA)
$$

for all $A,B$ in a suitable analytic domain. The condition is periodicity in imaginary time: the flow continued to $t+i\beta$ returns the state.

The modular flow of a faithful state is KMS at $\beta=1$ by construction, in modular units. The physical temperature is the normalization of the modular Hamiltonian:

$$
\tilde K_{\mathrm{mod}}=-\ln\Delta,
\qquad
\beta\,\tilde K_{\mathrm{mod}}
\quad\text{is the physical generator}.
$$

The overall scale of $\tilde K_{\mathrm{mod}}$ is a unit choice; the ratios of its eigenvalues are physical. The KMS condition fixes the relation between the flow and the state, not an absolute temperature.

### The Trace State

For the trace state, $\Delta=\mathrm{id}$ and $\tilde K_{\mathrm{mod}}=0$. The KMS condition holds for every $\beta$, because the flow is the identity and the state is tracial. The reading is the **no-temperature state**: the algebra's trace does not fix a period, and the state is compatible with every period. The infinite-temperature reading is the same statement: $\beta\to0$ is not a limit of the algebra, it is the absence of a scale.

### The Non-Tracial State

A non-tracial state has $\Delta\neq\mathrm{id}$ and a non-zero modular Hamiltonian. The flow is non-trivial, and the KMS period is the period of the flow in modular units. The state fixes a clock; the algebra does not.

The corpus states the existence of such states but does not compute their modular operators. The physical reading is therefore conditional: a non-tracial state on the biquaternion algebra would supply a thermal clock, and the temperature would be the normalization of its modular Hamiltonian. The algebra permits the reading; it does not supply the state.

## The Two Sides

### The Conjugation

The modular conjugation exchanges the left and the right multiplications:

$$
\jmath\,L_{\tilde Q}\,\jmath=R_{\tilde Q^{*}},
\qquad
\jmath\,\mathcal M\,\jmath=\mathcal M'.
$$

The commutant of the left regular image is the right regular image. The conjugation is the algebraic exchange of the two sides.

### The Reading

The pair $(\mathcal M,\mathcal M')$ is the algebraic form of a **bipartition**. A state on the algebra, with its modular conjugation, entangles the two sides: the modular flow acts on one side, and the conjugation maps it to the other. The reading is the Tomita–Takesaki form of entanglement, not a tensor-product decomposition.

The biquaternion algebra is a factor, and a factor has no tensor factorization into two independent subalgebras. The two sides here are the left and right regular images, which are commutants, not tensor factors. The entanglement reading is therefore the algebraic entanglement of a state with its commutant, not the bipartite entanglement of two subsystems. The distinction matters: the algebra supplies the exchange, not a partition into two laboratories.

The Cartan pairing supplies the same structure in the operator-to-state map: the amplitude is the square root of the state, and its logarithm is minus half the modular Hamiltonian. The modular conjugation is not the Cartan unitary factor; the two are different objects, and the notation must not identify them.

## The Indefinite Obstruction

The indefinite reading does not supply a modular pair. The Krein adjoint of a left multiplication is a right multiplication,

$$
(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}},
$$

which leaves the left regular image for non-central $\tilde Q$. The image is not a Krein–von Neumann algebra, and the Tomita operator is not definable. The envelope that replaces it, $\mathcal L(\mathbb{B})\cong M_4(\mathbb{C})$, has no separating vector: for every $\xi\neq0$ there is a non-zero $T$ with $T\xi=0$. The twisted fundamental symmetries $J'=R_c$ give a Krein–von Neumann algebra, but no commuting modular conjugation unless $c$ is central.

The physical reading is that **thermality is a definite-form notion**. The Krein form is a gauge calibration: it pairs two frames and returns a signed number. It is not a state, it is not positive, and it does not supply a trace. The thermal clock needs the definite Born form and a faithful state; the indefinite form supplies neither.

The reading is not that the indefinite structure is unphysical. It is that the indefinite structure is the geometry of the frame, not the statistics of the state. The two readings are different, and the modular pair belongs to the second.

## The Geometric Reading

The Krein isometry group contains the boosts $T_t$ with spectrum $\{e^t,e^{-t},1,1\}$. In the standard geometric reading, the modular flow of the vacuum restricted to a Rindler wedge is the boost, and the KMS period is $2\pi$ in modular units. The Unruh temperature is the period of that flow.

The algebra supplies the boost and its spectrum. It does not supply the wedge, the vacuum, the horizon or the observer. The geometric reading is therefore conditional: it requires a state, a region and a notion of restriction, none of which is an element of the algebra. The reading is a bridge, not a derivation.

The finite-dimensional algebra is type I. Its modular operator is inner, and it has no type III factor, no intrinsic thermality and no phase transition. A thermal ensemble in the algebraic sense needs a state and a thermodynamic limit; the finite algebra supplies the state space and the modular pair, not the limit.

## Physical Interpretations

- **The modular flow is the clock of a state.** The state selects a one-parameter group; the group is the state's time. The algebra supplies the group structure, the state supplies the flow.
- **The trace state has no temperature.** $\Delta=\mathrm{id}$, the modular Hamiltonian vanishes, and the KMS condition holds for every $\beta$. The trace is the infinite-temperature state, and it fixes no period.
- **A non-tracial state has a temperature.** $\Delta\neq\mathrm{id}$, the modular Hamiltonian is non-zero, and the KMS period is the state's clock. The temperature is the normalization of the generator.
- **The modular conjugation is the exchange of the two sides.** $\jmath L_{\tilde Q}\jmath=R_{\tilde Q^{*}}$; the commutant is the right regular image. The reading is algebraic entanglement, not a tensor-product bipartition.
- **The indefinite form has no modular pair.** The Krein adjoint leaves the algebra, and the envelope has no separating vector. Thermality is a definite-form notion; the Krein form is a gauge calibration, not a state.
- **The geometric reading is conditional.** The boost is in the algebra; the wedge, the vacuum and the horizon are not. The Unruh period is a bridge, not a derivation.
- **The finite algebra is type I.** The modular operator is inner; there is no type III factor and no intrinsic thermality. A thermal ensemble needs a state and a thermodynamic limit.
- **The Cartan amplitude is the modular square root.** The amplitude is the square root of the state, and its logarithm is minus half the modular Hamiltonian up to a central constant.

## Limits

The temperature is not in the algebra. It is a property of a state and a modular pair; the algebra supplies the pair, the state supplies the scale.

The trace state has no thermal clock. The KMS condition holds for every $\beta$, and the state fixes none.

The non-tracial reading is conditional. The corpus states that a non-tracial vector state gives a non-trivial modular operator; it does not compute the operator or its spectrum.

The modular conjugation is not the Cartan factor. The conjugation is antiunitary and state-dependent; the Cartan factor is the unitary quotient of the operator. They are different objects.

The indefinite reading is not a thermal reading. The Krein form is a gauge calibration; it is not positive, not traced and not a state. The failure of the modular pair is a statement about the form, not about the algebra's physics.

The geometric reading needs a state, a region and a horizon. The algebra supplies the boost, not the wedge.

No dynamics is supplied. The modular flow is a clock, not an equation of motion, and the KMS condition is a periodicity, not a derivation of the Hamiltonian.

## Summary

- Thermality needs a state and a modular pair; the algebra alone has no temperature.
- The definite biquaternion algebra with the trace state has $S={}^{*}$, $\Delta=\mathrm{id}$, $\jmath={}^{*}$ and a trivial modular flow.
- The trace state is KMS at every $\beta$; it fixes no temperature and is the infinite-temperature state.
- A non-tracial state has $\Delta\neq\mathrm{id}$ and a non-zero modular Hamiltonian; the KMS period is its clock. The corpus states the existence, not the spectrum.
- The modular conjugation exchanges the left and right multiplications, $\jmath L_{\tilde Q}\jmath=R_{\tilde Q^{*}}$; the commutant is the right regular image. The reading is algebraic entanglement, not a tensor-product bipartition.
- The indefinite reading has no modular pair: the Krein adjoint leaves the algebra, and the envelope has no separating vector. Thermality is a definite-form notion.
- The boosts $T_t$ supply a geometric reading; the wedge, the vacuum and the horizon are extra data.
- The finite algebra is type I; its modular operator is inner, and it has no intrinsic thermality.
- The Cartan amplitude is the modular square root; the conjugation is not the Cartan factor.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathcal M=\{L_{\tilde Q}\}$ | the left regular image |
| $\xi=e_t$ | the cyclic and separating unit |
| $S(\tilde Q)=\tilde Q^{*}$ | the Tomita operator |
| $S=\jmath\Delta^{1/2}$ | the polar decomposition |
| $\Delta=\mathrm{id}$ | the modular operator of the trace state |
| $\jmath={}^{*}$ | the modular conjugation |
| $\sigma_t(\Lambda)=\Delta^{it}\Lambda\Delta^{-it}$ | the modular flow |
| $\beta$ | the KMS period, the inverse temperature |
| $\tilde K_{\mathrm{mod}}=-\ln\Delta$ | the modular Hamiltonian |

## Further Reading

- [The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra](../articles_maths/the-tomita-operator-and-the-j-modular-pair-for-the-biquaternion-algebra.html), for the operator and the obstruction.
- [The Biquaternion Algebra and the Krein–von Neumann Property](../articles_maths/the-biquaternion-algebra-and-the-krein-von-neumann-property.html), for the indefinite adjoint and the envelope.
- [The Cartan Pairing: Amplitude and the Operator-to-State Map](the-cartan-pairing-amplitude-and-the-operator-to-state-map.html), for the modular reading of the amplitude.
- [The Krein Form and the Indefinite Structure](the-krein-form-and-the-indefinite-structure.html), for the gauge calibration and the cones.
- [Time from the Algebra: Clock, Rate and Period](time-from-the-algebra-clock-rate-and-period.html), for the clock reading.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the state space and the Born form.
