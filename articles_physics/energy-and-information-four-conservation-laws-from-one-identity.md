# __Energy and Information: Four Conservation Laws from One Identity__

## Introduction

The corpus splits the biquaternion algebra into two real four-dimensional subspaces. The anti-Hermitian subspace $\mathbb{B}_{\Phi}$ carries the four-vectors, the interval and the Lorentz action; the Hermitian subspace $\mathbb{B}_{\Psi}$ carries the states, the observables and the Born pairing. Multiplication by the central $i$ exchanges the two, and the framework's claim is that the first is the material sector and the second the informational one. Those names record a conjugation, not a dynamical role. The third section fixes the vocabulary: the anti-Hermitian sector is the sector of generators, and its flow is $*$-unitary.

The algebra attaches two numbers to an element, the trace and the quaternionic norm, and the two sectors read them in opposite roles. On $\mathbb{B}_{\Phi}$ the trace is energy and the norm is mass; on $\mathbb{B}_{\Psi}$ the trace is normalisation and the norm is information. Conjugation by a $*$-unitary element fixes both numbers of whatever it acts on, and that one algebraic fact is the warrant of every conservation law below: energy and mass on the material side, normalisation and information on the informational side. The split is a duality of two readings of two operations, not a sum of two contributions to one number.

It is not an exchange, because nothing passes from one sector to the other. It is not a decomposition either, because energy is not the sum of a mass term and an information term. Nor is it a dynamics: the article fixes what the two sectors conserve, and the one place where a probability falls is a reduced description, treated in its own section and attributed to no element of either sector.

The article takes the trace and the two norms from [Norm and Pairing Conventions](norm-and-pairing-conventions.html), the factorisation of the four-momentum from [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html), and the entropy from [Von Neumann Entropy and the Biquaternion Norm](von-neumann-entropy-and-the-biquaternion-norm.html). It follows [The Temporal Dimension: Why the Temporal Unit Is the Identity](the-temporal-dimension-why-the-temporal-unit-is-the-identity.html), whose two results it uses throughout. First, the trace is twice the temporal coefficient, so the conserved scalar of each sector is the coefficient of the scalar direction. Second, a boost is a unit element and not a $*$-unitary one, so a boost moves the trace and fixes the norm. The identities are algebra or corpus results, and they are checked below on a hundred random elements. The identification of the two sectors with a material and an informational sector of the world is the corpus's **hypothesis**, and the candidate constant $h_0$ is a **proposal** that the article examines and does not adopt.

The article runs in eight steps: the two operations, the identity and its four conservations, the dynamical vocabulary, the two sectors read in turn, the duality, the question of $h_0$, and the ledger of what is established. That last section also lists the five objections the thesis has to answer.

## The Two Operations on One Element

### The Element, the Trace and the Norm

Write a general element as a complex scalar times the identity plus a complex three-vector along the quaternion units,

$$
\tilde Q=Q_t\,e_t+Q_x\,\vec e_x+Q_y\,\vec e_y+Q_z\,\vec e_z,\qquad Q_\mu\in\mathbb{C},
$$

with $e_t=1$ and $\vec e_\eta^2=-e_t$. The algebra attaches two numbers to it. The **trace** is twice the scalar part, and the **quaternionic norm** is the product with the quaternion conjugate $\tilde Q^\natural=Q_t e_t-\vec Q$:

$$
\operatorname{Tr}\tilde Q=2\,\mathrm{Sc}\,\tilde Q=2Q_t,\qquad
\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural=Q_t^2+Q_x^2+Q_y^2+Q_z^2 .
$$

In the $2\times2$ image, under $e_t\mapsto I_2$ and $\vec e_\eta\mapsto -i\sigma_\eta$, the trace is the matrix trace and the quaternionic norm is the determinant:

$$
\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t,\qquad \det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_\natural .
$$

Write $B^2=\vec Q\cdot\vec Q$. The two eigenvalues of the element are

$$
\lambda_\pm=Q_t\pm iB,
$$

and the two numbers are their sum and their product:

$$
\lambda_++\lambda_-=\operatorname{Tr}\tilde Q,\qquad \lambda_+\lambda_-=\langle\tilde Q\rangle_\natural .
$$

The trace is therefore the **sum** of the spectrum and the norm is the **product**. That is all the algebra the split needs, and both identities hold on a hundred random elements to machine precision.

| property | trace | quaternionic norm |
| --- | --- | --- |
| operation on the spectrum | sum $\lambda_++\lambda_-$ | product $\lambda_+\lambda_-$ |
| linearity | $\mathbb{C}$-linear | quadratic |
| composition | additive for a sum | multiplicative for a product |
| behaviour under congruence | changes in general | preserved by every unit-norm rotor |
| behaviour under $*$-unitary conjugation | preserved | preserved |

The last two rows make the split, and each is proved in one line below.

### The Two Scalar Products

A scalar product is a form, and the algebra carries two that matter here. The **quaternionic form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_\natural=\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2\bigr)
=Q_{1t}Q_{2t}+Q_{1x}Q_{2x}+Q_{1y}Q_{2y}+Q_{1z}Q_{2z},
$$

which is $\mathbb{C}$-bilinear and indefinite. The **Hermitian form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_*=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)
=Q_{1t}\bar Q_{2t}+Q_{1x}\bar Q_{2x}+Q_{1y}\bar Q_{2y}+Q_{1z}\bar Q_{2z},
$$

which is sesquilinear and positive definite. The star is the Hermitian conjugation, $\tilde Q^*=\bar{\tilde Q}^{\natural}$.

The two forms read differently on the two sectors, and the difference is the signature. On $\mathbb{B}_{\Phi}$ the coefficients are $Q_t=iq'_t$ and $\vec Q=\vec q$ real, so

$$
\langle\tilde Q\rangle_\natural=-{q'_t}^2+\lvert\vec q\rvert^2,\qquad
\langle\tilde Q\rangle_*=+{q'_t}^2+\lvert\vec q\rvert^2 .
$$

On $\mathbb{B}_{\Psi}$ the coefficients are $Q_t=q_t$ real and $\vec Q=i\vec q'$, so

$$
\langle\tilde Q\rangle_\natural=+q_t^2-\lvert\vec q'\rvert^2,\qquad
\langle\tilde Q\rangle_*=+q_t^2+\lvert\vec q'\rvert^2 .
$$

The quaternionic form is indefinite on both sectors and changes signature from $(3,1)$ on $\mathbb{B}_{\Phi}$ to $(1,3)$ on $\mathbb{B}_{\Psi}$. The Hermitian form is positive definite on both. The material sector's indefinite form is the physical interval. On the informational sector the same form is the impurity, and the positivity of a state is a condition on its spectrum, not the sign of the norm.

| form | $\mathbb{B}_{\Phi}$ | $\mathbb{B}_{\Psi}$ | role |
| --- | --- | --- | --- |
| quaternionic, $\langle\cdot,\cdot\rangle_\natural$ | $-{q'_t}^2+\lvert\vec q\rvert^2$ | $q_t^2-\lvert\vec q'\rvert^2$ | the interval; the mass norm |
| Hermitian, $\langle\cdot,\cdot\rangle_*$ | ${q'_t}^2+\lvert\vec q\rvert^2$ | $q_t^2+\lvert\vec q'\rvert^2$ | the positive weight; the Born pairing |

### The Two Central Scalars

The centre of the algebra is $\mathbb{B}_{C}=\mathbb{C}e_t$, two real dimensions, and the sector split cuts it in two: the real scalar line $\mathbb{R}e_t$ belongs to $\mathbb{B}_{\Psi}$ and the imaginary line $i\mathbb{R}e_t$ to $\mathbb{B}_{\Phi}$. Each sector therefore owns one real central line, and that is where its central scalar sits.

On the material side the central scalar is the **mass**. For a timelike four-momentum the quaternionic norm is negative and its square root is imaginary. The Hamilton pairing writes

$$
\tilde P_{\Phi}=\Rho\,e^{\vec U\Theta},\qquad
\Rho=\sqrt{\langle\tilde P_{\Phi}\rangle_\natural}=imc,
$$

so the mass sits on the imaginary central line. Of the three factorisations of a four-vector — quaternion, Hamilton and Cartan — this is the only one whose first factor is central. That factor commutes with every element and is unchanged by every unit-norm congruence.

On the informational side the central scalar is the **normalisation**. A state is normalised by its pairing with the identity,

$$
\langle\tilde{Ϛ}_{\Psi},e_t\rangle_*=\mathrm{Sc}\,\tilde{Ϛ}_{\Psi}=\tfrac12,\qquad
\operatorname{Tr}\tilde{Ϛ}_{\Psi}=1,
$$

so the scalar part is $\tfrac12$ on the real central line, and the trace is one. The trace is the central projection of the state, and the Born rule is the ratio of two such projections.

| sector | central line | central scalar | value on the standard object |
| --- | --- | --- | --- |
| $\mathbb{B}_{\Phi}$ | $i\mathbb{R}e_t$ | mass $\Rho=imc$ | $\sqrt{\langle\tilde P_{\Phi}\rangle_\natural}$ |
| $\mathbb{B}_{\Psi}$ | $\mathbb{R}e_t$ | normalisation $\mathrm{Sc}\,\tilde{Ϛ}_{\Psi}$ | $\tfrac12$, trace one |

The placement depends on the regime, and the dependence is a single $i$. In the non-relativistic central-scalar limit the mass and the energy are real central scalars in $\mathbb{B}_{\Psi}$, and the material time is the parameter multiplying $ie_t$. Relativistically the four-momentum is in $\mathbb{B}_{\Phi}$ and its trace is imaginary. The two statements are the two ends of the same substitution $Q_t=ict'$: the non-relativistic limit drops the $i$, and with it the distinction between the real and the imaginary central lines. The limit is a contraction of the relativistic structure, not a second convention.

## One Identity, Four Conservations

### The Identity

Let $\tilde U$ be $*$-unitary, $\tilde U\tilde U^{*}=e_t$, and let $\tilde X$ be any element. Then

$$
\operatorname{Tr}\bigl(\tilde U\tilde X\tilde U^{*}\bigr)=\operatorname{Tr}\tilde X,
\qquad
\det\bigl(\tilde U\tilde X\tilde U^{*}\bigr)=\det\tilde X .
$$

The first identity is cyclicity of the trace, $\operatorname{Tr}(AB)=\operatorname{Tr}(BA)$ with $A=\tilde U$ and $B=\tilde X\tilde U^{*}$. The second is multiplicativity of the determinant, $\det(AB)=\det A\,\det B$, together with $\lvert\det\tilde U\rvert^{2}=1$, which follows from $\tilde U\tilde U^{*}=e_t$. Both were checked on a hundred random pairs to $2.7\times10^{-15}$ and $7.1\times10^{-15}$.

The statement is about a conjugation, so it applies to every element of the algebra and needs no sector, no physical object and no dynamics. Everything the article says about conservation is an instance of it.

### Why a Similarity Fixes Both Numbers

The two numbers the algebra attaches to an element are the two symmetric functions of its spectrum. Writing $\tilde Q=Q_t e_t+\vec Q$ and $B^{2}=\vec Q\cdot\vec Q$, the eigenvalues are $\lambda_\pm=Q_t\pm iB$, and

$$
\operatorname{Tr}\tilde Q=\lambda_++\lambda_-=2Q_t,
\qquad
\langle\tilde Q\rangle_\natural=\lambda_+\lambda_-=\det\mathsf M_2(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

checked on a hundred random elements to $4.4\times10^{-16}$ and $8.2\times10^{-15}$. A conjugation is a similarity, a similarity has the same spectrum, and the two symmetric functions are therefore fixed. The identity is not a coincidence of two formulas: it is the statement that $\tilde U\tilde X\tilde U^{*}$ and $\tilde X$ are the same operator in two bases.

That is why one identity carries four conservation laws. Conservation in this framework is never a separate postulate about a separate quantity; it is the invariance of a symmetric function of a spectrum under the group action that leaves the spectrum alone.

### The Four Conservations

The identity becomes four statements when the two numbers are named on the two sectors.

| sector | operation | value on the standard object | fixed by | conserved quantity |
| --- | --- | --- | --- | --- |
| $\mathbb{B}_{\Phi}$ | trace | $2iE/c$ | the $*$-unitary flow of the dynamics | energy |
| $\mathbb{B}_{\Phi}$ | quaternionic norm | $-m^{2}c^{2}$ | the flow, and every unit-norm congruence | mass |
| $\mathbb{B}_{\Psi}$ | trace | $1$ | the flow, and every trace-preserving map | normalisation |
| $\mathbb{B}_{\Psi}$ | quaternionic norm | $\tfrac14(1-\lvert\vec r\rvert^{2})$ | the reversible flow | information |

The four rows are the whole thesis. The material pair and the informational pair are the same two lines of algebra, with the sectors supplying the names: the trace is $2iE/c$ on one side and $1$ on the other, and the norm is $-m^{2}c^{2}$ on one side and the impurity on the other. One preservation, read twice, gives energy and mass conservation on the material side and normalisation and information conservation on the informational side.

### Conservation Is Not Invariance

The fourth column differs from row to row, and the difference separates conservation from invariance. **Conservation** means fixed by the dynamics, which is a $*$-unitary conjugation. **Invariance** means fixed by the change of frame, which is a unit-norm congruence. The two groups differ: *Norm and Pairing Conventions* keeps them apart, a boost being a unit element and not a $*$-unitary one.

A boost therefore fixes the determinant and moves the trace. Applied to a four-momentum at rest, it gives the numbers below.

| $\theta_{\mathrm{rpd}}$ | $E/(mc^{2})$ | $\det/(-m^{2}c^{2})$ | $\lvert BB^{*}-e_t\rvert$ |
| --- | --- | --- | --- |
| $0$ | $1.000000$ | $1.000000$ | $0$ |
| $0.5$ | $1.127626$ | $1.000000$ | $0.649$ |
| $1.0$ | $1.543081$ | $1.000000$ | $1.718$ |
| $2.0$ | $3.762196$ | $1.000000$ | $6.389$ |

The determinant residual is $0$ at every rapidity. Energy is conserved and frame-dependent; mass is conserved and frame-independent. The two words are not synonyms, and one identity gives one of each. The determinant is fixed by the larger group, so mass is invariant. The trace is fixed only by the smaller group, so energy is conserved without being invariant.

The same distinction settles the informational side. A coarse-graining is trace preserving and not reversible, so normalisation survives it and the norm does not. Information is conserved in the reversible regime and in no other, and the article states the conservation with that qualification rather than without it.

### The Temporal Reading

The identity is also the reason the conserved scalar of each sector is a temporal coefficient. The trace is twice the scalar part, and the scalar part is the coefficient of $e_t$, the temporal unit. Since $e_t$ is the identity, it is the only unit of the base that reaches the trace; the three vector units are traceless. That is the temporal article's result read from the other side.

So on $\mathbb{B}_{\Phi}$ the conserved trace is $2iE/c$, the temporal coefficient of the four-momentum, and on $\mathbb{B}_{\Psi}$ it is $1$, the normalisation, which is twice the scalar part $\tfrac12$ of the state. **Energy is the temporal coefficient of the four-momentum and normalisation is the temporal coefficient of the state; both are conserved because the temporal direction is the scalar direction, the one the flow leaves alone.**

The factor of $i$ then does the rest. It places the energy on the imaginary central line and the normalisation on the real one, so the same preservation reads as a phase on one side and as a probability on the other. That is the sense in which the split of the algebra is a split of what each sector conserves, and it is the sense in which the two sectors are two readings and not two substances.

### What the Identity Does Not Give

**It does not give an additive decomposition.** Energy is not the sum of a mass term and an information term. The trace is one number on each sector, and the two are of different kinds, one imaginary and one real.

**It does not give a sector charge.** The superselection article shows that the split is a grading of the operations and not a central decomposition of the state space, and that the algebra carries no additive label counting material against informational content. Nothing in the identity supplies one, and the article claims none.

**It does not give additivity of the conserved quantities.** The trace is additive for a sum and the norm is multiplicative for a product, so the norm of a sum carries a cross term. Mass is conserved as the norm of the total, not as a sum of masses; information is conserved as the norm of the whole, not as a share held by each part.

**It does not give a dynamics.** It says what a $*$-unitary flow leaves fixed, not what the flow is. The Hamiltonian is an input, and the identity is a constraint on any dynamics that has one.

## Anti-Hermitian, Decay and the Factor of $i$

Two things are easily confused: an element that is anti-Hermitian, and a probability that falls. They are not the same event. The material sector is anti-Hermitian and carries the energy, and the energy is conserved; a probability can also fall, and the fall is a fact about a reduced description, not about the sector. The section separates the two and names each by what it does.

**A falling probability is a measured fact.** Fix a slot of the module and let $P(r'_t)$ be the probability that the system is still found in the state it started in. $P$ can fall. The fall is measured, and over the life of a resonance it does not reverse. It is not a disappearance: the probability has moved into the part of the system that the description does not follow, by entanglement with it. *Quantum Channels and the Reversible–Irreversible Dichotomy* calls irreversibility exactly the regime in which the sector is open and its states are entangled with an environment. The fall belongs to the physics; the omission belongs to the description.

**The fall is real, and the exponential is only a window on it.** *The Unstable State and the Complex Energy Pole* states the exact short-time law,

$$
P(r'_t)=1-\frac{\Delta^{2}\,\tilde{H}_{\Psi}^{2}}{\hbar^{2}}{r'_{t}}^{2}+O({r'_{t}}^{4}),
$$

so the survival probability starts from one with zero slope, and no exponential can reproduce that: $\exp(-\gamma r'_t)$ starts with slope $-\gamma$. The fall has three regimes, and only the middle one is exponential.

| regime | law | where it holds |
| --- | --- | --- |
| early | $P=1-(\Delta\tilde H_\Psi)^{2}{r'_{t}}^{2}/\hbar^{2}+O({r'_{t}}^{4})$ | ${r'_t}\ll\frac{\hbar}{\Delta\,\tilde{H}_{\Psi}}$ |
| intermediate | $\exp(-\frac{\Gamma\,r'_{t}}{\hbar\,c})$, as a fit | long against the inverse spectral width of the continuum, short against the onset of the long-time deviation |
| late | a power law set by the density of states at the band edge, slower than exponential | beyond the window |

The exponential $\exp(-\frac{\Gamma\,r'_{t}}{\hbar\,c})$ is therefore a fit over an intermediate window, not the law. In the band model the quadratic coefficient is $(1-P)/{r'_{t}}^{2}=0.800$ against the predicted $g^{2}N=0.8$; at ${r'_t}=10^{-4}$ the exact deficit is $8.0\times10^{-9}$ against the exponential's $5.0\times10^{-5}$, a factor of $6287$. A band truncated to sixty levels shows partial revivals, from $0.032$ back to $0.65$ at the times set by the level spacing, which is why the continuum is a limit and not a large band. The decay has a shape. The exponential is the part of it that is quoted, and the word "monotonic" does not describe the shape either.

**An anti-Hermitian element does not make a probability fall.** Take $\tilde Q=-\tilde Q^{*}$. Its spectrum is purely imaginary, and for real $r'_t$

$$
\bigl(\exp(r'_t\tilde Q)\bigr)^{*}\exp(r'_t\tilde Q)
=\exp(-r'_t\tilde Q)\exp(r'_t\tilde Q)=e_t,
$$

so the exponential is $*$-unitary, $\tilde U\tilde U^{*}=e_t$, and conjugation by a $*$-unitary element preserves the trace and both norms. It is a $*$-unitary element and not a unit element: *Norm and Pairing Conventions* keeps the two apart, and the exponential of an anti-Hermitian element has $\lvert\det\tilde U\rvert=1$ with $\det\tilde U$ a general phase. The anti-Hermitian elements are the Lie algebra $\mathfrak{u}(2)$ of the unitary group; they generate the $*$-unitary transformations, and that is all they do. A sentence that calls them lossy has mistaken a rotation for a shrinkage.

*Relations between the Biquaternion Exponential and the Fourier Kernel* gives the general law, and it is the sharpest statement available. For $\tilde Q=Q_te_t+\vec Q$, $B^2=(\vec Q,\vec Q)$ and $\rho=\vec Q/B$,

$$
\bigl\langle e^{\theta\tilde Q}\bigr\rangle_*
=\bigl\lvert e^{\theta Q_t}\bigr\rvert^{2}
\left(\lvert\cos(B\theta)\rvert^{2}+\lvert\sin(B\theta)\rvert^{2}\lVert\rho\rVert^{2}\right),
\qquad
\lVert\rho\rVert^{2}\ge1,
$$

with equality exactly when $\tilde Q$ is normal. Only three numbers reach the norm, and they do different jobs: $\operatorname{Re}Q_t$ is a **rate**, $\operatorname{Im}B$ is an envelope rate, and $\lVert\rho\rVert^2$ is an **amplitude**, never a rate. That article puts it in one line: "a decay is a negative real part of $Q_t$ in the convention $e^{+\theta\tilde Q}$". The qualification is the whole point.

Neither sector puts anything in the rate slot. For anti-Hermitian $\tilde Q$, $Q_t$ is purely imaginary and $\vec Q$ is real, so $\operatorname{Re}Q_t=0$ and $\rho$ is a real unit vector: the norm is exactly $1$ for every $\theta$. For Hermitian $\tilde H_\Psi$, its scalar coefficient is real but the corpus's flow carries the factor $-i$, $\exp(-\frac{i\,\theta\,\tilde H_\Psi}{\hbar})$, and that factor moves the real scalar into the frequency slot: the norm is again exactly $1$. Checked on a hundred elements each, to $1.2\times10^{-14}$ and $5.6\times10^{-15}$. The factor of $i$ is therefore not decoration; it is what makes a real scalar a frequency rather than a rate, and removing it changes the physics from oscillation to dilation.

One case is worth stating, because it is the exception that fixes the rule: a single element can shrink the norm. Exponentiated without the $i$, a Hermitian element gives

$$
\bigl\langle e^{\theta\tilde H_\Psi}\bigr\rangle_*
=e^{2\theta h_t}\cosh\bigl(2\lvert\vec h_\Psi\rvert\theta\bigr),
$$

checked to $8.7\times10^{-16}$. The forward branch grows or decays at rate $2(R_t+\lvert\vec r\rvert)$, and it decays when $R_t<-\lvert\vec r\rvert$; the backward branch grows at rate $2(\lvert\vec r\rvert-R_t)$, which is positive for every Hermitian element. So such a flow falls in one direction of $\theta$ and diverges in the other: it has an arrow of time built into a single element, which is precisely why it cannot serve as a reversible law. No dynamics in the corpus uses it — the state-vector equation always carries the $-i$. A shrinking element and a falling probability are different events.

One level up, the question is about maps rather than elements. *The Exponential, the Logarithm and the Generator* records that an irreversible completely positive trace-preserving map is a sum of at least two conjugations, so it is not a single element and has no algebraic generator. When such a map has a generator, the generator is a superoperator on states, not an element of $\mathbb{B}$. A falling probability has no address in the algebra at all. The question "is $\mathbb{B}_{\Phi}$ lossy?" accordingly has no yes-or-no answer, because the predicate does not apply to elements.

The spectral vocabulary has a boundary of its own, drawn the same way: by asking what a statement is about. *Biorthogonal Quantum Mechanics and the Biquaternion Spectrum* treats a non-normal element by changing the pairing: left and right eigenvectors, and the Petermann factor $\kappa=\frac12(1+\lVert\rho\rVert^{2})$, which is the norm deficit again, $\kappa-1=\frac12(\lVert\rho\rVert^{2}-1)$, checked spectrally to $3.6\times10^{-15}$. *Exceptional Points and the Nilpotent Regime* treats the degeneracy on the isotropic cone. Both are statements about the spectrum of one element, and neither says that a probability falls. The cone itself is out of reach of both sectors. A real vector part gives $B^2=\sum_\eta Q_\eta^2\ge0$, vanishing only at $\vec Q=0$, and a Hermitian element gives $B^2=-\sum_\eta q_\eta^2\le0$, vanishing only at $\vec q=0$. The degeneracy available to either sector is therefore diabolic, and an exceptional point needs a vector part that is neither real nor purely imaginary. That is a third kind of element, and the corpus keeps it where it belongs, in the spectral articles.

**Where a falling $P$ comes from: a channel that was eliminated.** The mechanism is in *The Unstable State and the Complex Energy Pole*. Split the module into the slot under study and the rest, and integrate the rest out. The Green's function of the watched slot becomes

$$
G_{\mathrm{c}}(z)=\bigl(z-H_{\mathrm{c}}-\Sigma_{\mathrm{nc}}(z)\bigr)^{-1},
\qquad
\Sigma_{\mathrm{nc}}(z)=V\frac{1}{z-H_{\mathrm{nc}}}V^{*},
$$

and when the eliminated slot holds a continuum the self-energy is complex,

$$
\Sigma_{\mathrm{nc}}(E+i0^{+})=\Delta(E)-\tfrac{i}{2}\,\Gamma(E),
\qquad
\Gamma(E)=2\pi\lvert V_0(E)\rvert^{2}\rho(E)\ge0 .
$$

The real part displaces the level and the imaginary part gives the width. That article calls the two the **Hermitian and anti-Hermitian aspects of one complex scalar**, and the phrase is exact: they are the two parts of one complex number, not two operators. The decaying pole $z_\star=E_R-\frac{i}{2}\Gamma$ is a zero on the second sheet of the resolvent of a Hermitian Hamiltonian; it is not an eigenvalue of a non-Hermitian element on the physical sheet.

The arithmetic is easy to check directly. Couple one discrete level to a band of two thousand levels, with a Hamiltonian that is Hermitian by construction and no anti-Hermitian term anywhere. The survival probability of the discrete level is $1$, $0.841$, $0.625$, $0.495$, $0.376$, $0.226$, $0.135$ at $r'_t=0,\;0.5,\;1,\;1.5,\;2,\;3,\;4$, while the squared norm of the full state is $1.000000000$ at every one of those times. The missing probability sits in the band, to the last digit: the fitted fall rate over $0.3\le r'_t\le1.6$ is $0.531$, against the Golden-Rule value $0.503$ for that band. One slot loses probability while the whole is conserved, and nothing in the construction is anti-Hermitian.

**The shorthand, and what it stands for.** The eliminated channel is usually compressed into an effective Hamiltonian,

$$
i\,\partial_{r'_t}\tilde{Ξ}=\tilde H_{\Psi,\mathrm{eff}}\tilde{Ξ},
\qquad
\tilde H_{\Psi,\mathrm{eff}}=\tilde H_\Psi-\frac{i}{2}\tilde\Gamma,
$$

with $\tilde H_\Psi=\tilde H_\Psi^{*}$ and $\tilde\Gamma=\tilde\Gamma^{*}\ge0$, whose anti-Hermitian part is $-\frac{i}{2}\tilde\Gamma$. The squared Hermitian norm then obeys

$$
\frac{d}{dr'_t}\langle\tilde{Ξ}\rangle_*
=-\langle\tilde{Ξ},\tilde\Gamma\tilde{Ξ}\rangle_*\le0,
$$

which follows from $\frac{d}{dr'_t}\langle\tilde{Ξ}\rangle_*=\langle\tilde{Ξ},(G^{*}+G)\tilde{Ξ}\rangle_*$ with $G=-i\tilde H_{\Psi,\mathrm{eff}}$ and $G^{*}+G=-\tilde\Gamma$; checked on a hundred random pairs, the finite-difference residual staying below $10^{-9}$. An indefinite $\tilde\Gamma$ with negative eigenvalues gives growth, so the anti-Hermitian part records loss, gain, or both, and the sign of $\tilde\Gamma$ decides which. The coefficient is a convention: carrying the term as $-i\tilde\Gamma'$ with $\hbar$ restored gives $-\frac{2}{\hbar}\langle\tilde{Ξ},\tilde\Gamma'\tilde{Ξ}\rangle_*$, the same statement with the rate rescaled; the corpus measures the action in units of $\hbar$ and the coefficient $\frac12$, which is what puts the pole at $z_\star=E_R-\frac{i}{2}\Gamma$ and the amplitude decay at $\exp(-\Gamma r'_t/2)$.

The shorthand must not be read as a new element of the algebra. It is the reduced description of one slot, valid on the branch where the eliminated channel has been dropped, and its complex coefficient carries the width of that branch. The pole it produces is the second-sheet pole, not a physical-sheet eigenvalue.

**The rates are the poles.** A mode of eigenvalue $w$ evolves by $\exp(-iwr'_t)$, so its squared norm grows as $\exp(2\operatorname{Im}(w)\,r'_t)$: the mode falls when $\operatorname{Im}w<0$, at rate $-2\operatorname{Im}w$ on the squared norm and $-\operatorname{Im}w$ on the amplitude, which at $z_\star$ is $\frac{\Gamma}{2}$. Checked to $7.8\times10^{-16}$.

**A full open system, and where the probability goes.** If the environment is neither measured nor discarded but averaged over, the description is a map, and *Quantum Channels and the Reversible–Irreversible Dichotomy* writes it as

$$
\frac{d\tilde{Ϛ}_{\Psi}}{dr'_t}
=-\frac{i}{\hbar}\,[\tilde H_\Psi,\tilde{Ϛ}_{\Psi}]
+\sum_\eta\left(\tilde M_{\mathrm{kraus},k}\,\tilde{Ϛ}_{\Psi}\,\tilde M_{\mathrm{kraus},k}^{*}
-\tfrac12\{\tilde M_{\mathrm{kraus},k}^{*}\tilde M_{\mathrm{kraus},k},\tilde{Ϛ}_{\Psi}\}\right).
$$

The trace is preserved, $\frac{d}{dr'_t}\operatorname{Tr}\tilde{Ϛ}_{\Psi}=0$ by cyclicity, checked to $1.8\times10^{-15}$; the purity is not, and that fall is the whole effect. Nothing leaves the ensemble. The effective Hamiltonian with the anti-Hermitian part describes the branch on which no jump has occurred, whose unnormalised state obeys

$$
i\,\partial_{r'_t}\tilde{Ξ}_{\mathrm{nj}}
=\Bigl(\tilde H_\Psi-\frac{i}{2}\sum_\eta\tilde M_{\mathrm{kraus},k}^{*}\tilde M_{\mathrm{kraus},k}\Bigr)\tilde{Ξ}_{\mathrm{nj}},
\qquad
\frac{d}{dr'_t}\langle\tilde{Ξ}_{\mathrm{nj}}\rangle_*
=-\sum_\eta\langle\tilde{Ξ}_{\mathrm{nj}},\tilde M_{\mathrm{kraus},k}^{*}\tilde M_{\mathrm{kraus},k}\tilde{Ξ}_{\mathrm{nj}}\rangle_*\le0 .
$$

The lost norm is exactly the probability that a jump has occurred, checked to $1.0\times10^{-11}$ on a hundred random triples of jump operators. That is the precise content of the anti-Hermitian part of an effective Hamiltonian: it describes the branch where nothing has happened yet, and the rate it carries is the jump rate.

**The same warning on the state space.** With the Hilbert–Schmidt form $\langle\tilde Q_1,\tilde Q_2\rangle_{\mathrm{HS}}=\operatorname{Tr}(\tilde Q_1^{*}\tilde Q_2)$, the commutator $-i[\tilde H_\Psi,\cdot]$ is anti-Hermitian and preserves the Hilbert–Schmidt norm: it rotates the state and shrinks nothing, the adjoint being its negative with residual $0$. The jump part is generally neither Hermitian nor anti-Hermitian; over a hundred random single-jump terms the smallest distance to either form was $1.24$. So anti-Hermiticity marks the reversible generator here as elsewhere, and the fall of $P$ sits outside the Hermitian/anti-Hermitian alternative altogether.

The derivative form swaps the two labels. With $G=-i\tilde H_{\Psi,\mathrm{eff}}$,

$$
G=-\frac12\tilde\Gamma-i\tilde H_\Psi .
$$

The Hermitian part of $G$ is $-\frac12\tilde\Gamma$ and the anti-Hermitian part is $-i\tilde H_\Psi$. For the central pole, $G_\star=-iz_\star=-\frac{\Gamma}{2}e_t-iE_Re_t$, and the shrinkage is again the Hermitian part. A stable state has $\tilde\Gamma=0$, its generator is anti-Hermitian, and its evolution is unitary.

The norm used in this section is the Hermitian norm $\langle\cdot\rangle_*$, the Hilbert-space norm of the evolving element, not the quaternionic norm: on $\tilde{Ϛ}_{\Psi}$ the Hermitian norm measures purity, and the quaternionic norm is the impurity that the informational side reads as information.

| object | sector | property | dynamical role |
| --- | --- | --- | --- |
| Hamiltonian $\tilde H_\Psi$ | $\mathbb{B}_{\Psi}$ | Hermitian | the observable; reversible through $-i\tilde H_\Psi$ |
| generator $-i\tilde H_\Psi$ | $\mathbb{B}_{\Phi}$ | anti-Hermitian | unitary, norm-preserving flow |
| width $\Gamma$ | centre (a number) | $\Gamma\ge0$ | decay rate of the eliminated channel |
| pole $z_\star$ | centre (a number) | second sheet | fixes the decay law over its window |
| generator $G=-\frac12\tilde\Gamma-i\tilde H_\Psi$ | effective | Hermitian part $-\frac12\tilde\Gamma$ | Hermitian part shrinks, anti-Hermitian part oscillates |
| commutator $-i[\tilde H_\Psi,\cdot]$ | $\mathbb{B}_{\Phi}$ | anti-Hermitian in the Hilbert–Schmidt form | rotates the state, shrinks nothing |

The strongest objection is that the section splits one word into two and then picks a side. It does pick, and the choice follows the corpus. An anti-Hermitian element generates a reversible flow, and no element of either sector carries a rate, because a falling probability is not a property of an element. A decay is the survival probability of one slot falling while the whole is conserved; that is the content of the elimination in *The Unstable State and the Complex Energy Pole*, and it is the content of the trace-preservation in the channel article. "Hermitian is reversible" is exact for the Hamiltonian, "anti-Hermitian is lossy" is false as stated and true only of the coefficient of an eliminated channel in the reduced equation, and "the anti-Hermitian sector is lossy" is false, because the sector is a set of elements and no element falls.

The ledger is unaffected, and its vocabulary is now fixed. Energy is the trace of the four-momentum in $\mathbb{B}_{\Phi}$, conserved because the generator is anti-Hermitian. Mass is the norm, invariant for the same reason. Information is the norm of the state in $\mathbb{B}_{\Psi}$, conserved under the $*$-unitary flow and lost under coarse-graining. A falling probability names an event in a reduced description, and it names nothing in the algebra.

## The Material Side: Energy Is the Trace, Mass Is the Norm

### Energy Is the Trace

The four-momentum of a particle of mass $m$ is the material element

$$
\tilde P_{\Phi}=i\frac{E}{c}\,e_t+\vec p,\qquad \vec p=p_x\vec e_x+p_y\vec e_y+p_z\vec e_z .
$$

Its trace is

$$
\operatorname{Tr}\tilde P_{\Phi}=2i\frac{E}{c},
\qquad\text{hence}\qquad
E=\frac{c}{2i}\operatorname{Tr}\tilde P_{\Phi} .
$$

Energy is the trace of the four-momentum, up to the factor $c/(2i)$. The factor is bookkeeping: the trace is twice the scalar coefficient, and the scalar coefficient of a material element is imaginary. The statement is exact and was checked on a hundred random four-momenta. It is the algebraic content of "energy is the time component of the four-momentum": the time component is the scalar slot, and the trace is the scalar slot read twice.

The eigenvalues make the same statement without the factor. They are

$$
\lambda_\pm=i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right),
$$

the two light-cone combinations. Their sum is $2iE/c$ and their difference is $2i\lvert\vec p\rvert$. Energy is the sum of the two combinations and momentum is their difference, up to the same factor.

### Mass Is the Norm

The quaternionic norm of the same element is

$$
\langle\tilde P_{\Phi}\rangle_\natural=-\frac{E^2}{c^2}+\lvert\vec p\rvert^2=-m^2c^2 .
$$

Mass is the norm, and the mass shell is the level set of the norm. The eigenvalues are the two branches of the square root,

$$
\lambda_\pm=imc\,e^{\pm\theta_{\mathrm{rpd}}},\qquad
\cosh\theta_{\mathrm{rpd}}=\frac{E}{mc^{2}},\qquad
\sinh\theta_{\mathrm{rpd}}=\frac{\lvert\vec p\rvert}{mc},
$$

and their product is $-m^2c^2$. The product is frame-independent; the two factors are not, and their dependence is the Doppler rescaling. The ratio is the squared Doppler factor,

$$
\frac{\lambda_+}{\lambda_-}=e^{2\theta_{\mathrm{rpd}}}.
$$

This is the corpus's spectral reading of a four-vector, and the article only recalls it: mass is the product, energy the sum, momentum the difference, rapidity the ratio.

### The Split Is a Factorisation

The two readings combine in the Hamilton pairing,

$$
\tilde P_{\Phi}=\Rho\,e^{\vec U\Theta},\qquad
\Rho=imc,\qquad
\Theta=-i\theta_{\mathrm{rpd}},\qquad
\vec U=\vec u_p,
$$

where $\vec u_p$ is the unit along the momentum. Expanding the exponential gives

$$
\tilde P_{\Phi}=imc\bigl(\cosh\theta_{\mathrm{rpd}}-i\sinh\theta_{\mathrm{rpd}}\,\vec u_p\bigr)
=i\,mc\cosh\theta_{\mathrm{rpd}}\,e_t+mc\sinh\theta_{\mathrm{rpd}}\,\vec u_p,
$$

so that

$$
E=mc^2\cosh\theta_{\mathrm{rpd}},\qquad \lvert\vec p\rvert=mc\sinh\theta_{\mathrm{rpd}} .
$$

The energy is the **product** of the central scalar and a frame factor. It is not the sum of a mass term and an information term. The exact additive split is the mass shell,

$$
E^2=m^2c^4+\lvert\vec p\rvert^2c^2,
$$

and its additive form at fixed mass is

$$
E=mc^2+T,\qquad T=mc^2(\cosh\theta_{\mathrm{rpd}}-1),
$$

where $T$ is the kinetic energy. The first term is the rest energy and the second is the energy of motion. Neither term is an entropy.

The same factorisation governs the action. For a free particle the action is minus the mass times the proper time,

$$
S=-mc^2\tau,\qquad \tau=\int\frac{dt}{\gamma},\qquad \gamma=\cosh\theta_{\mathrm{rpd}} .
$$

The mass is the invariant coefficient and the frame factor is the conversion between coordinate time and proper time. The phase $e^{\frac{i\,S}{\hbar}}$ therefore carries the mass in its amplitude and the frame in its clock. This is the sharpest form of the split on the material side: **the action is the mass times the proper time, and the frame information is the rate at which proper time is spent.**

### Mass Conservation Is Norm Conservation of the Total

Mass is not conserved particle by particle, and the algebra says why. The norm is multiplicative under composition, the four-momenta add, and the two operations do not agree. For two four-momenta,

$$
\langle\tilde P_{\Phi,1}+\tilde P_{\Phi,2}\rangle_\natural
=\langle\tilde P_{\Phi,1}\rangle_\natural+\langle\tilde P_{\Phi,2}\rangle_\natural
+2\langle\tilde P_{\Phi,1},\tilde P_{\Phi,2}\rangle_\natural,
\qquad
\langle\tilde P_{\Phi,1},\tilde P_{\Phi,2}\rangle_\natural
=-\frac{E_1E_2}{c^2}+\vec p_1\cdot\vec p_2 .
$$

The cross term is what makes the mass of a system differ from the sum of the masses. At rest the sum gives $-(m_1+m_2)^2c^2$, the expected additivity. In general the norm of the total is the invariant mass of the pair, which exceeds $m_1+m_2$ when the particles move relative to one another. Mass is not additive, and a statement of mass conservation that adds masses is false.

What is conserved is the total four-momentum of an isolated system, and with it the norm of the total. The conservation of $\tilde P_{\Phi,\mathrm{tot}}$ is the Noether charge of translation invariance, and the conservation of the total invariant mass is a corollary: the norm of a conserved element is constant. This is the precise content of "mass conservation" in the framework. It is a statement about the total, not about the parts, and it follows from energy–momentum conservation rather than standing beside it.

The invariance is a separate statement from the conservation. The norm is preserved by every unit-norm rotor,

$$
\langle\tilde U\tilde P_{\Phi}\tilde U^*\rangle_\natural
=\det\tilde U\,\det\tilde P_{\Phi}\,\det\tilde U^*
=\langle\tilde P_{\Phi}\rangle_\natural
\qquad\text{when}\qquad
\langle\tilde U\rangle_\natural=1,
$$

because a unit-norm element has determinant one and its star has determinant one. The trace is not preserved by the same action: a boost changes $E$ and leaves $m$ fixed. The duality section below turns that remark into the two ledgers.

| statement | object | operation | result |
| --- | --- | --- | --- |
| energy conservation | $\tilde P_{\Phi,\mathrm{tot}}$ | addition of four-momenta | energy of the total is constant |
| mass conservation | $\tilde P_{\Phi,\mathrm{tot}}$ | norm of the total | invariant mass of the total is constant |
| mass invariance | one $\tilde P_{\Phi}$ | unit-norm congruence | norm unchanged |
| energy frame dependence | one $\tilde P_{\Phi}$ | unit-norm congruence | trace changes |

## The Informational Side: Normalisation Is the Trace, Information Is the Norm

### The Trace Is the Normalisation

A state of the informational sector is the Hermitian element

$$
\tilde{Ϛ}_{\Psi}=\tfrac12\bigl(e_t+i\vec r\bigr),\qquad
\vec r=r_1\vec e_x+r_2\vec e_y+r_3\vec e_z,\qquad
\lvert\vec r\rvert\le1 .
$$

Its trace is one,

$$
\operatorname{Tr}\tilde{Ϛ}_{\Psi}=2\,\mathrm{Sc}\,\tilde{Ϛ}_{\Psi}=1,
$$

and its scalar part is $\tfrac12$. The trace is the total probability, and the Born weight is the ratio of two traces,

$$
p=\frac{\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi)}{\operatorname{Tr}\tilde{Ϛ}_{\Psi}},
\qquad
\operatorname{Tr}\tilde{Ϛ}_{\Psi}=1 .
$$

The trace is fixed by the normalisation and says nothing about which state the system is in. Every state shares it, and the dynamics preserves it.

### The Norm Is the Information

The quaternionic norm of the state is

$$
\langle\tilde{Ϛ}_{\Psi}\rangle_\natural=\tfrac14\bigl(1-\lvert\vec r\rvert^2\bigr)e_t,
$$

a central element whose coefficient runs from $\tfrac14$ at the maximally mixed state to $0$ on the pure states. The Hermitian norm is a different number,

$$
\langle\tilde{Ϛ}_{\Psi}\rangle_*=\tfrac14\bigl(1+\lvert\vec r\rvert^2\bigr),
$$

and the two are related by the purity,

$$
P(\tilde{Ϛ}_{\Psi})=2\langle\tilde{Ϛ}_{\Psi},\tilde{Ϛ}_{\Psi}\rangle_*=\tfrac12\bigl(1+\lvert\vec r\rvert^2\bigr),
\qquad
P+2\langle\tilde{Ϛ}_{\Psi}\rangle_\natural=1 .
$$

The entropy is a function of the quaternionic norm and of nothing else:

$$
S(\tilde{Ϛ}_{\Psi})=-2\,\mathrm{Sc}\bigl(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi}\bigr)
=h\!\left(\frac{1+\lvert\vec r\rvert}{2}\right)
=H\!\left(\langle\tilde{Ϛ}_{\Psi}\rangle_\natural\right),
$$

with $h$ the binary entropy and $H(N)=h\bigl((1+\sqrt{1-4N})/2\bigr)$. The function is increasing on $[0,\tfrac14]$, vanishes on the pure states and reaches $\log 2$ at the maximally mixed state. This is the corpus's identification: the natural invariant of the algebra and the entropy of the state are one quantity in two readings. The norm is the information in that precise sense: it fixes the entropy, and the entropy is the information the state fails to hold.

| state | $\lvert\vec r\rvert$ | $\langle\tilde{Ϛ}_{\Psi}\rangle_\natural$ | $S$ |
| --- | --- | --- | --- |
| pure | $1$ | $0$ | $0$ |
| mixed | $0<\lvert\vec r\rvert<1$ | $0<\tfrac14(1-r^2)<\tfrac14$ | $0\lt S\lt\log2$ |
| maximally mixed | $0$ | $\tfrac14$ | $\log2$ |

There is a direction to the identification, and it is easy to get backwards. The **Hermitian** norm grows with $\lvert\vec r\rvert$ and measures purity; the **quaternionic** norm falls with $\lvert\vec r\rvert$ and measures impurity, which is the information the state fails to hold. The entropy belongs to the second, not the first. On the state slice the two are affinely related, so no number is lost, but the two names must not be exchanged.

### Information Conservation and Invariance

The reversible evolution of a state is a conjugation by a $*$-unitary element, $\tilde{Ϛ}_{\Psi}\mapsto\tilde U\tilde{Ϛ}_{\Psi}\tilde U^*$ with $\tilde U\tilde U^*=e_t$. Two identities hold:

$$
\operatorname{Tr}\bigl(\tilde U\tilde{Ϛ}_{\Psi}\tilde U^*\bigr)=\operatorname{Tr}\tilde{Ϛ}_{\Psi},
\qquad
\langle\tilde U\tilde{Ϛ}_{\Psi}\tilde U^*\rangle_\natural=\langle\tilde{Ϛ}_{\Psi}\rangle_\natural .
$$

The first follows from cyclicity of the trace and from $\tilde U^*\tilde U=e_t$. The second follows from multiplicativity of the determinant and from $\lvert\det\tilde U\rvert^{2}=1$. Both were checked on a hundred random $*$-unitary elements. Since the entropy is a function of the quaternionic norm, it is invariant:

$$
S\bigl(\tilde U\tilde{Ϛ}_{\Psi}\tilde U^*\bigr)=S(\tilde{Ϛ}_{\Psi}).
$$

This is the precise sense in which information is conserved. Conservation here is the invariance of the spectrum under a similarity, and the trace and the norm are the two symmetric functions of the spectrum that the algebra reads.

The conservation fails as soon as the dynamics is not reversible. A coarse-graining is a unital completely positive map that contracts the Bloch ball, $\lvert\vec r_Ξ\rvert\le\lvert\vec r\rvert$. The trace survives, because the map preserves it, and the quaternionic norm increases, because the radius falls:

$$
\operatorname{Tr}Ξ(\tilde{Ϛ}_{\Psi})=\operatorname{Tr}\tilde{Ϛ}_{\Psi},
\qquad
\langleΞ(\tilde{Ϛ}_{\Psi})\rangle_\natural\ge\langle\tilde{Ϛ}_{\Psi}\rangle_\natural,
\qquad
S\bigl(Ξ(\tilde{Ϛ}_{\Psi})\bigr)\ge S(\tilde{Ϛ}_{\Psi}).
$$

Coarse-graining never creates information. It can only fail to retain it. The fine-grained entropy is the conserved reference, and the increase appears when a reversible flow and a contraction are composed. The second law of the sector is a statement about the pair, not about the flow alone.

The frame action is a third case, and it separates the two kinds of invariance. At sharp momentum the physical Lorentz action on the state is the $*$-unitary Wigner rotation, and the entropy is invariant. At uncertain momentum the boost acts by a mixed $*$-unitary channel, and the entropy increases by an amount bounded by one bit per qubit and governed by the Wigner angle. The entropy is therefore invariant under the compact rotations and under the physical action at sharp momentum, and it is not invariant under a general congruence. The congruence moves a state off the trace-one slice; the physical channel does not. The distinction is operational, and it is the one the corpus draws between the two actions.

There is no conserved charge that counts the two sectors. The split is a grading of the operations, not a central decomposition of the state space, and the superselection article is explicit that the algebra has no additive label for material against informational content. "Information conservation" cannot therefore mean the conservation of a sector charge. It can only mean the invariance of the entropy under reversible dynamics, which is what the three identities above state.

## The Duality

### The Same Two Operations, Swapped

The two sectors use the same two operations in opposite roles. The table is the thesis of the article.

| | material side, $\mathbb{B}_{\Phi}$ | informational side, $\mathbb{B}_{\Psi}$ |
| --- | --- | --- |
| standard object | four-momentum $\tilde P_{\Phi}$ | state $\tilde{Ϛ}_{\Psi}$ |
| trace | energy, $2iE/c$ | normalisation, one |
| quaternionic norm | mass squared, $-m^2c^2$ | impurity, $\tfrac14(1-r^2)$ |
| scalar product | $\langle\cdot,\cdot\rangle_\natural$, indefinite | $\langle\cdot,\cdot\rangle_*$, positive definite |
| central scalar | mass $\Rho=imc$ | scalar part $\tfrac12$ |
| fixed by the physics | the norm (the particle's mass) | the trace (normalisation) |
| left free by the physics | the trace (the frame) | the norm (the state) |
| invariant under | unit-norm congruence | $*$-unitary conjugation |
| additive | trace | trace |
| multiplicative | norm | norm |

The swap is the content. On the material side the **norm** is fixed and the **trace** varies; the particle has a definite mass and a frame-dependent energy. On the informational side the **trace** is fixed and the **norm** varies; every state has unit total probability and the information varies from state to state. The same pair of operations, read with the roles exchanged, gives the two ledgers.

The rest of this section sets the two ledgers side by side. It gives each one a set of examples, then says what the word "fixed" means on each side, and then puts the numbers together. The examples are chosen so that one number is held while the other runs.

### The Material Ledger: The Trace Is a Frame Label

**One particle, two frames.** A muon has $mc^2=105.66$ MeV. At rest its energy is $105.66$ MeV and its rapidity is zero. At $E=10$ GeV its rapidity is $\theta_{\mathrm{rpd}}=5.24$, because $\cosh\theta_{\mathrm{rpd}}=94.6$, and its momentum is $10.0\ \mathrm{GeV}/c$. The trace grows by the factor $94.6$. The norm is the same number in both frames.

The eigenvalues show the mechanism. They are $imc\,e^{+\theta_{\mathrm{rpd}}}$ and $imc\,e^{-\theta_{\mathrm{rpd}}}$, and they move apart by the same factor in opposite directions. Their product is fixed by construction, and their sum is not. The trace is the sum and the norm is the product, so one number moves and the other cannot. This is the whole ledger in one line of algebra.

**Two particles, one energy.** An electron and a proton at $E=1$ GeV have the same trace, $2i(1\ \mathrm{GeV})/c$. Their norms are $-0.261\ \mathrm{MeV}^2$ and $-8.80\times10^{5}\ \mathrm{MeV}^2$, a ratio of $3.4\times10^{6}$. The trace does not tell the two particles apart. The norm does.

So the trace is not the material identity of the object. It records how much energy the frame assigns, and it is blind to which particle carries it. The mass is the number that survives the change of frame, and it is the number that names the particle.

**One particle, every energy.** A photon has zero norm at every energy. At $1$ eV and at $1$ TeV its traces differ by $10^{12}$, and its norm is zero in both cases. The invariant can sit on the boundary of the cone, where it separates nothing at all.

On the null cone the separation is total. The trace carries the whole description of the photon and the norm carries none of it. This is why a mass measurement cannot determine a momentum, and why the material ledger needs both numbers even though only one of them is invariant.

The fixed number is the one that two observers agree on. The free number is the one they exchange when they compare notes. A boost is exactly that exchange, and it acts on the trace alone.

### The Informational Ledger: The Norm Is a State Label

**One trace, four states.** Every state has trace one. Take the family $\tilde{Ϛ}_{\Psi}=\frac12(e_t+i\vec r)$ at $\lvert\vec r\rvert=1$, $0.8$, $0.5$ and $0$. The norms are $0$, $0.09$, $0.1875$ and $0.25$. The entropies are $0$, $0.47$, $0.81$ and $1$ bit.

The trace is the same four times. The norm separates the four states without error, and the entropy is a monotone function of it. So on this side the trace identifies nothing and the norm identifies everything.

**A part and a whole.** Take a Bell pair. The joint state is pure: trace one, norm zero, entropy zero. Either factor alone is maximally mixed: trace one, norm $0.25$, entropy one bit. The trace is one for the part and one for the whole, so it does not distinguish them.

The norm does distinguish them, and in the direction opposite to the material one. The whole is pure and the parts are not. The information of the pair sits in the correlation, which neither factor holds, and the norm of a factor is not a function of the norm of the whole.

This is the informational counterpart of the cross term in the mass of a pair. On the material side the mass of a sum is not the sum of the masses. On the informational side the information of a part is not a share of the information of the whole. In both cases the quantity that fails to add is the norm, and that is one more reason to read it as the invariant of the element rather than as a sum over parts.

**One state, one coarse-graining.** Send a pure state through a depolarising map that halves the radius, $\vec r\mapsto\frac12\vec r$. The trace stays one. The norm goes from $0$ to $0.1875$, and the entropy from $0$ to $0.811$ bit. No frame changed and no energy was exchanged. The norm moved because a distinction was lost.

So the free number on this side is a state label. It moves when the state is chosen, and it moves when the dynamics is not reversible. It never moves under a change of frame, because the frame is not part of the informational action at sharp momentum.

### The Two Meanings of "Fixed"

The two ledgers share a shape and differ in the reason for it.

On $\mathbb{B}_{\Phi}$ the group action moves one number and fixes the other. The unit-norm congruence is the Lorentz action. Its orbit through a timelike element is the mass hyperboloid, the norm names the orbit, and the trace names the point on it. The mass is the orbit label and the energy is the orbit coordinate. The algebra supplies both the invariant and the group that moves the other number.

On $\mathbb{B}_{\Psi}$ the group action fixes both numbers. The $*$-unitary conjugation preserves the trace and the norm, and its orbit through a state is the sphere of fixed $\lvert\vec r\rvert$ in the Bloch ball. Both numbers label the orbit, and neither is a coordinate on it: the coordinates are the direction of $\vec r$. So nothing in the reversible group moves the norm. Only a map that is not invertible moves it.

The asymmetry corrects a symmetric reading of the duality. "The trace varies" on $\mathbb{B}_{\Phi}$ means that the frame varies. "The norm varies" on $\mathbb{B}_{\Psi}$ means that the state varies, or that information was lost. The same word covers two different freedoms.

There is a second asymmetry, and it is a warning. A congruence is the material action, but it is not a state transformation. A congruence by an element of norm other than one can rescale the trace, and it therefore moves a state off the trace-one slice. The spin-entropy article states the consequence: a physical transformation of a state cannot rescale its trace, and the congruence can. The same algebraic operation has two physical interpretations, and only the $*$-unitary case is a symmetry of both numbers.

| action | on the trace | on the norm | reading |
| --- | --- | --- | --- |
| unit-norm congruence on $\mathbb{B}_{\Phi}$ | changes | fixed | change of frame |
| general congruence on $\mathbb{B}_{\Psi}$ | changes | multiplies | not a state change |
| $*$-unitary conjugation on $\mathbb{B}_{\Psi}$ | fixed | fixed | reversible evolution |
| coarse-graining on $\mathbb{B}_{\Psi}$ | fixed | increases | loss of distinction |
| addition of two four-momenta | adds | does not add | composition of a system |

The last row has no partner in the informational sector, because states do not add. They compose, and the norm of a composite is the product of the norms only when the parts are uncorrelated. That is why the informational column has no additive entry to match the material one.

### The Ledgers in Numbers

| object | $\operatorname{Tr}$ | $\langle\cdot\rangle_\natural$ | $S$ |
| --- | --- | --- | --- |
| muon at rest | $2i(105.66\ \mathrm{MeV})/c$ | $-1.116\times10^{4}\ \mathrm{MeV}^2$ | — |
| the same muon at $10$ GeV | $2i(10\ \mathrm{GeV})/c$, $94.6$ times larger | unchanged | — |
| photon at $1$ eV | $2i(1\ \mathrm{eV})/c$ | $0$ | — |
| photon at $1$ TeV | $2i(1\ \mathrm{TeV})/c$, $10^{12}$ times larger | $0$ | — |
| electron at $1$ GeV | $2i(1\ \mathrm{GeV})/c$ | $-0.261\ \mathrm{MeV}^2$ | — |
| proton at $1$ GeV | $2i(1\ \mathrm{GeV})/c$, the same | $-8.80\times10^{5}\ \mathrm{MeV}^2$ | — |
| pure qubit | $1$ | $0$ | $0$ |
| qubit at $\lvert\vec r\rvert=\tfrac12$ | $1$ | $0.1875$ | $0.811$ |
| maximally mixed qubit | $1$ | $0.25$ | $1$ |

Rows one and two hold the norm and vary the trace. Rows five and six hold the trace and vary the norm; rows seven to nine do the same over the whole range of the state. A number that can be held while another runs is the invariant of the pair, and each side names a different one.

### What "Energy Equals Mass plus Information" Can Mean

The phrase admits three readings, and only one of them is exact.

The **additive reading** is $E=mc^2+h_0 I$. It is exact only if $I$ is defined as the kinetic energy in units of the rest energy, $I=\cosh\theta_{\mathrm{rpd}}-1$, and then the coefficient is not a universal $h_0$ but the mass itself, $E=mc^2(1+I)$. The quantity $I$ is a frame factor, not an entropy, and the additive split is the rest energy plus the kinetic energy.

The **ledger reading** is that the material and informational accounts describe the same energy in two ways. Within one isolated system the identity $E=mc^2$ is exact, and the entropy is a function of the state. Across a partition the accounts exchange: the erasure of one bit in a memory lowers the memory's entropy by $\log2$ and delivers at least $k_BT\log2$ of heat to the environment. The exchange rate is the temperature, and it is a property of the partition, not a constant of nature.

The **duality reading** is the one the algebra supports without a new postulate: the trace is energy on the material side and normalisation on the informational side; the norm is mass on the material side and information on the informational side. This is a statement about two readings of two operations, not about a decomposition of one number. It is exact, and it needs no $h_0$.

The strongest objection to the phrase is that the additive reading double counts. A hot body's rest mass already contains its thermal energy, so adding a separate $T\,dS$ term to $c^2\,dm$ counts the same energy twice. The ledger reading avoids the double count by treating the two accounts as descriptions of one system or as a transfer between two systems; the duality reading avoids it by not adding at all. The phrase "energy equals mass plus information" is therefore a slogan for the duality, not a first law.

### The Two Discriminants

The two sides are separated by the sign of one algebraic number. The characteristic polynomial of a general element is

$$
\lambda^2-(\operatorname{Tr}\tilde Q)\,\lambda+\langle\tilde Q\rangle_\natural=0,
$$

and its discriminant is

$$
\Delta=(\operatorname{Tr}\tilde Q)^2-4\langle\tilde Q\rangle_\natural .
$$

On a four-momentum, with $\operatorname{Tr}\tilde P_{\Phi}=2iE/c$ and $\langle\tilde P_{\Phi}\rangle_\natural=-m^2c^2$,

$$
\Delta=-4\frac{E^2}{c^2}+4m^2c^2=-4\lvert\vec p\rvert^2\le0 .
$$

The eigenvalues are imaginary, and the mass shell is the statement $E\ge mc^2$ with equality at rest. On a state, with $\operatorname{Tr}\tilde{Ϛ}_{\Psi}=1$ and $\langle\tilde{Ϛ}_{\Psi}\rangle_\natural=\tfrac14(1-r^2)$,

$$
\Delta=1-(1-r^2)=r^2\ge0 .
$$

The eigenvalues are real and positive, and the entropy bound $0\le S\le\log2$ is the statement that they lie in $[0,1]$. The material element has a non-positive discriminant and the informational element a non-negative one. That is the spectral face of the sector split, and it is the reason the informational side carries a positive cone of states and a probability, while the material side carries the causal cone of the interval.

## The Candidate $h_0$

### What the Corpus Has

The corpus contains three constants and one unit, and none of them is an information quantum.

| object | value or origin | status |
| --- | --- | --- |
| $c$ | the unit conversion of the temporal slot; it sets the null cone at $\lvert\vec p\rvert=E/c$ | with the units |
| $\hbar$ | the phase $e^{\frac{i\,S}{\hbar}}$ and the spin generators | imported |
| $k_B$ | the thermodynamic entropy, $S_{\mathrm{th}}=k_BS$ | imported |
| the bit | $\log2$, the capacity of the two-dimensional carrier | algebraic, from $\dim S=2$ |

The bit is the only informational unit the algebra supplies. The carrier is the defining module of $\mathbb{B}\cong M_2(\mathbb{C})$, of complex dimension two, so at most two orthogonal states fit and the maximum entropy is $\log2$. That number is independent of $\hbar$. The Born rule contains no $\hbar$, and the state space contains no action. The material side carries $\hbar$ in its phase; the informational side does not.

### Four Candidate Readings of $h_0$

If one insists on an $h_0$, four readings are available, and they have different dimensions.

| candidate | formula | dimensions | status |
| --- | --- | --- | --- |
| action per nat | $h_0=\hbar$ | action | a convention, $1$ nat $=1$ radian |
| action per bit | $h_0=\hbar\log2$ | action | a convention joining two units |
| Landauer quantum | $h_0=k_BT\log2$ | energy | thermodynamic, temperature-dependent |
| phase-space basis operator | $h_0=h$ | action | semiclassical, one state per basis operator |

The first two are conventions: they join the phase unit to the information unit by a definition, and neither is forced by the algebra. The third is no constant of nature. It is the energy cost of erasure at a temperature, and it varies with the state of the bath. The fourth identifies a phase-space basis operator with a state, and it is imported from statistical mechanics.

### The Verdict

The corpus has no $h_0$. The algebra fixes $c$ and the bit, and it imports $\hbar$ and $k_B$. A universal constant converting energy into information would be a new postulate, and the article records it as a proposal rather than a result.

The slot that a naive $h_0$ would occupy is already occupied twice, by two different rates. In mechanics the rate is $c^2$, and it is exact: $E=mc^2$ for a system at rest, and $E=mc^2\cosh\theta_{\mathrm{rpd}}$ for a particle in motion. In thermodynamics the rate is $T$, and it is a state variable: $Q_{\min}=k_BT\log2$ per bit erased. The two rates are not independent, because the thermal energy of a body contributes to its rest mass, and that is the double-counting objection of the previous section. A single $h_0$ would have to replace both, and the corpus gives no equation in which it would sit without changing one of them.

What would fix $h_0$ is a derivation of $\hbar$ from the algebra. The corpus does not have one: $\hbar$ enters through the phase and the spin generators, and no algebraic condition selects its value. Absent that derivation, $h_0$ remains a name for a missing bridge, and the honest statement is the one the corpus already makes about its scales: the algebra supplies the arena and imports the dynamics.

## What Is Established and What Is Proposed

| statement | status | warrant |
| --- | --- | --- |
| the trace is the sum of the eigenvalues and the norm their product | established | the characteristic polynomial; checked on 100 elements |
| energy is the trace of the four-momentum | established | $\operatorname{Tr}\tilde P_{\Phi}=2iE/c$; checked |
| mass is the modulus, $\Rho=imc$ | established | $\langle\tilde P_{\Phi}\rangle_\natural=-m^2c^2$; checked |
| $E=mc^2\cosh\theta_{\mathrm{rpd}}$ | established | the Hamilton pairing; checked |
| the norm is preserved by unit-norm congruence | established | determinant multiplicativity; checked |
| the trace is preserved by $*$-unitary conjugation | established | cyclicity and $\tilde U^*\tilde U=e_t$; checked |
| the norm is preserved by $*$-unitary conjugation | established | $\lvert\det\tilde U\rvert^2=1$; checked |
| an anti-Hermitian element generates a $*$-unitary flow | established | $\exp(-r'_t\tilde Q)\exp(r'_t\tilde Q)=e_t$; checked |
| no element of either sector has a decay rate in the corpus convention, which carries the $-i$ | established | $\operatorname{Re}Q_t=0$ on $\mathbb{B}_{\Phi}$; the $-i$ moves $Q_t$ to the frequency slot on $\mathbb{B}_{\Psi}$; both norms identically $1$, checked to $10^{-14}$ |
| the norm of the exponential is fixed by three numbers | established | the law of *Relations between the Biquaternion Exponential and the Fourier Kernel*; checked to $1.4\times10^{-15}$ |
| the two sectors meet the discriminant locus only diabolically | corpus result | $B^2=\sum_\eta Q_\eta^2\ge0$ for a real vector part, $-\sum_\eta q_\eta^2\le0$ for a Hermitian element; 100 draws, $\operatorname{Im}B^2=0$ |
| a survival probability can fall while the total is conserved | established | band model, 2000 levels: $P_0$ falls $1\to0.135$, total norm $1.000000000$; checked |
| the survival probability leaves one quadratically | corpus result | $P=1-\frac{\Delta^{2}\,\tilde{H}_{\Psi}^{2}\,{r'_{t}}^{2}}{\hbar^{2}}+O(r'^4_t)$; band model $(1-P)/r_t^{\prime 2}=0.800$ vs $g^2N=0.8$ |
| the exponential is an intermediate-time fit, not the law | corpus result | quadratic start, power-law tail; deficit ratio $6287$ at $r'_t=10^{-4}$ |
| the width is the imaginary part of the central self-energy | corpus result | *The Unstable State and the Complex Energy Pole* |
| in the effective description the damping is the Hermitian part of $G$ | established | $G=-i\tilde H_{\Psi,\mathrm{eff}}=-\frac12\tilde\Gamma-i\tilde H_\Psi$; checked |
| the effective anti-Hermitian part decays the norm at rate $\tilde\Gamma$ | established | $\frac{d}{dr'_t}\langle\tilde{Ξ}\rangle_*=-\langle\tilde{Ξ},\tilde\Gamma\tilde{Ξ}\rangle_*$; checked on 100 elements |
| the decay rate of a mode is the imaginary part of its pole | established | $\lVert e^{-i(w/(\hbar c))r'_t}v\rVert^2=e^{2\operatorname{Im}(w)r'_t/(\hbar c)}$; checked to $7.8\times10^{-16}$ |
| the Lindblad flow preserves the trace | established | cyclicity; checked to $1.8\times10^{-15}$ |
| the norm lost on the no-jump branch is the total jump probability | established | $\frac{d}{dr'_t}\langle\tilde{Ξ}_{\mathrm{nj}}\rangle_*=-\sum_\eta\langle\tilde{Ξ}_{\mathrm{nj}},\tilde M_{\mathrm{kraus},k}^{*}\tilde M_{\mathrm{kraus},k}\tilde{Ξ}_{\mathrm{nj}}\rangle_*$; checked |
| the commutator $-i[\tilde H_\Psi,\cdot]$ is anti-Hermitian in the Hilbert–Schmidt form | established | the adjoint is its negative; residual $0$ |
| the entropy is a function of the quaternionic norm | corpus result | *Von Neumann Entropy and the Biquaternion Norm* |
| the entropy increases under coarse-graining | corpus result | *Coarse-Graining and the Biquaternion Entropy Functional* |
| the informational reading of the norm | hypothesis | the sector hypothesis of the corpus |
| $h_0$ | proposal | not in the corpus |

**The first objection is that the sectors are not conserved charges.** The superselection article shows that the split is a grading of the operations and not a central decomposition of the state space, and that there is no additive label counting material against informational content. The objection is correct and the article accepts it. The duality does not need such a charge: it is a statement about two readings of the trace and the norm, and both readings are available on every element. What the split does not give is a conserved quantum number, and the article does not claim one.

**The second objection is that mass is not additive.** The objection is correct, and it is the reason the article states mass conservation as norm conservation of the total. The norm is multiplicative under composition and the four-momenta add; the mass of a sum carries the cross term. A conservation law that adds masses is not the algebra's law.

**The third objection is that information is not conserved.** The objection is correct for the coarse-grained description, and the article states the conservation only for the reversible, fine-grained one. The trace is conserved by every trace-preserving map; the quaternionic norm is not, and the entropy increases. The word "conservation" applies to the first and not to the second.

**The fourth objection is that energy is not the sum of mass and information.** The objection is correct, and it is the main correction the article makes to the slogan. The exact additive split is rest energy plus kinetic energy, $E=mc^2+T$; the informational quantity is the norm of the state, not the kinetic energy. The exact statement is the duality of the trace and the norm, not a sum.

**The fifth objection is that the material sector is anti-Hermitian and therefore lossy.** The objection fails, but not for the reason one expects. No element of either sector carries a rate: an anti-Hermitian element generates a $*$-unitary flow, and an irreversible process has no algebraic generator at all, so the predicate does not apply to elements. A falling survival probability belongs to a description in which a channel has been dropped. The width is the imaginary part of the central self-energy $\Sigma_{\mathrm{nc}}=\Delta-\frac{i}{2}\Gamma$, the pole it produces sits on the second sheet of the resolvent of a Hermitian Hamiltonian, and the probability it removes from the watched slot is the probability that sits in the eliminated one. So $\mathbb{B}_{\Phi}$ carries the energy and the generators, and the fall of a probability names neither a sector nor an element. The vocabulary is fixed in the section on the factor of $i$, and the ledger uses it.

## Summary

- Conjugation by a $*$-unitary element fixes the trace and the determinant of every element it acts on. That is one identity, and it is the whole warrant of the four conservation laws: read on $\mathbb{B}_{\Phi}$ it says that energy is conserved and that mass is conserved, and read on $\mathbb{B}_{\Psi}$ it says that normalisation is conserved and that information is conserved. Each number lands in the sector where it is defined.
- The algebra attaches two numbers to an element: the trace, which is the sum of the two eigenvalues, and the quaternionic norm, which is their product and the determinant of the $2\times2$ image. A similarity fixes both because a similarity fixes the spectrum.
- On $\mathbb{B}_{\Phi}$ the trace is energy, $E=\frac{c}{2i}\operatorname{Tr}\tilde P_{\Phi}$, and the norm is mass, $\langle\tilde P_{\Phi}\rangle_\natural=-m^2c^2$; the mass is the central modulus $\Rho=imc$.
- The anti-Hermitian sector carries the generators, and no element of either sector carries a rate. For $\tilde Q=-\tilde Q^{*}$, $\exp(r'_t\tilde Q)$ is $*$-unitary, and the energy generator $-i\tilde H_\Psi$ is anti-Hermitian. A survival probability can fall: the width is the imaginary part of the central self-energy, the pole is a second-sheet zero of a Hermitian resolvent, and the probability removed from one slot is the probability in the eliminated one. The exponential is a fit over an intermediate window; the exact curve starts quadratically and ends as a power law.
- The material split is a factorisation, not a sum: $\tilde P_{\Phi}=\Rho e^{\vec U\Theta}$ with $\Rho=imc$, $\Theta=-i\theta_{\mathrm{rpd}}$, $\vec U=\vec u_p$, hence $E=mc^2\cosh\theta_{\mathrm{rpd}}$.
- Mass conservation is the norm conservation of the total four-momentum. Mass is not additive; the mass of a sum carries the cross term $2\langle\tilde P_{\Phi,1},\tilde P_{\Phi,2}\rangle_\natural$.
- On $\mathbb{B}_{\Psi}$ the trace is the normalisation, $\operatorname{Tr}\tilde{Ϛ}_{\Psi}=1$, and the quaternionic norm is the information, $\langle\tilde{Ϛ}_{\Psi}\rangle_\natural=\tfrac14(1-r^2)$; the entropy is a function of that norm alone.
- Information is conserved only in the reversible sense: $*$-unitary conjugation preserves the trace and the norm, and hence the entropy. Coarse-graining preserves the trace, increases the norm and increases the entropy.
- Conservation is not invariance. The trace is fixed by the $*$-unitary flow and moved by a boost, so energy is conserved and frame-dependent; the determinant is fixed by both, so mass is conserved and frame-independent.
- The duality is the thesis: the norm is fixed and the trace free on the material side, the trace fixed and the norm free on the informational side.
- The two freedoms are of different kinds. On $\mathbb{B}_{\Phi}$ the free number is a frame label, and the Lorentz group moves it. On $\mathbb{B}_{\Psi}$ the reversible group fixes both numbers, and the norm moves only under a loss of information.
- The trace identifies nothing on either side. An electron and a proton at $1$ GeV share it, and so do a pure and a maximally mixed state. The norm is the identifying number of both ledgers.
- The two sectors are separated by the sign of the discriminant: non-positive for the four-momentum, non-negative for the state.
- There is no $h_0$ in the corpus. The algebra supplies $c$ and the bit, and imports $\hbar$ and $k_B$. The two exchange rates the corpus does have are $c^2$ (mechanics) and $k_BT$ (thermodynamics).
- The slogan "energy equals mass plus information" is exact as a duality of readings, and false as an additive decomposition. The exact additive split is rest energy plus kinetic energy, $E=mc^2+T$.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | anti-Hermitian material sector, Hermitian informational sector |
| $\tilde{Ξ}$ | the biquaternion-valued field, the evolving element of the state-vector equation |
| $\operatorname{Tr}\tilde Q=2\,\mathrm{Sc}\tilde Q=2Q_t$ | the trace, twice the scalar part |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural$ | the quaternionic norm, the determinant, the interval |
| $\langle\tilde Q_1,\tilde Q_2\rangle_\natural=\mathrm{Sc}(\tilde Q_1^\natural\tilde Q_2)$ | the quaternionic form |
| $\langle\tilde Q_1,\tilde Q_2\rangle_*=\mathrm{Sc}(\tilde Q_1\tilde Q_2^*)$ | the Hermitian form |
| $\tilde P_{\Phi}=i(E/c)e_t+\vec p$ | the four-momentum |
| $\Rho=imc$ | the mass modulus, the central scalar of the material side |
| $\theta_{\mathrm{rpd}}$ | the rapidity, $\cosh\theta_{\mathrm{rpd}}=E/(mc^{2})$, $\sinh\theta_{\mathrm{rpd}}=\lvert\vec p\rvert/(mc)$ |
| $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$ | the state, $\lvert\vec r\rvert\le1$ |
| $S(\tilde{Ϛ}_{\Psi})=h((1+\lvert\vec r\rvert)/2)$ | the von Neumann entropy |
| $P=2\langle\tilde{Ϛ}_{\Psi},\tilde{Ϛ}_{\Psi}\rangle_*$ | the purity, $P+2\langle\tilde{Ϛ}_{\Psi}\rangle_\natural=1$ |
| $\tilde H_\Psi$ | the Hermitian Hamiltonian or observable, $\tilde H_\Psi=\tilde H_\Psi^{*}$ |
| $\tilde\Gamma$ | the Hermitian width element, $\tilde\Gamma=\tilde\Gamma^{*}\ge0$, of the eliminated channel |
| $\tilde H_{\Psi,\mathrm{eff}}=\tilde H_\Psi-\frac{i}{2}\tilde\Gamma$ | the effective Hamiltonian of the reduced slot, a shorthand, not an element of the algebra |
| $G=-i\tilde H_{\Psi,\mathrm{eff}}$ | the derivative-form generator, $G=-\frac12\tilde\Gamma-i\tilde H_\Psi$ |
| $c$, $\hbar$, $k_B$ | the cone scale, the imported action, the imported entropy unit |

## Further Reading

- [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html), for the factorisation, the modulus and the section *Mass, Not Energy*.
- [The Temporal Dimension: Why the Temporal Unit Is the Identity](the-temporal-dimension-why-the-temporal-unit-is-the-identity.html), for $e_t=1$, the trace as twice the temporal coefficient, and the boost as a unit element that is not $*$-unitary.
- [The N-Regular Spectrally Regular Sector: Mass in Motion](the-n-regular-spectrally-regular-sector-mass-in-motion.html), for mass as the product, energy as the sum, momentum as the difference and rapidity as the ratio.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the interval and the Lorentz congruence.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the trace, the Born pairing and the Bloch ball.
- [The Unstable State and the Complex Energy Pole in Biquaternionic Form](the-unstable-state-and-the-complex-energy-pole-in-biquaternionic-form.html), for the generator $G_\star=-iz_\star$ and the split into Hermitian damping and anti-Hermitian energy.
- [Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem](unitarity-from-centrality-the-biquaternion-norm-preservation-theorem.html), for the Hermitian norm and the anti-Hermitian generator of the state-vector equation.
- [Quantum Channels and the Reversible–Irreversible Dichotomy](quantum-channels-and-the-reversible-irreversible-dichotomy.html), for the Lindblad form, the trace-preserving flow and the split between the reversible derivation and the jump part.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](../articles_maths/relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the Hermitian norm of the flow, the three quantities that fix it, and the norm deficit $\lVert\rho\rVert^2\ge1$.
- [Biorthogonal Quantum Mechanics and the Biquaternion Spectrum](biorthogonal-quantum-mechanics-and-the-biquaternion-spectrum.html), for the left and right eigenbases and the Petermann factor as the norm deficit.
- [Exceptional Points and the Nilpotent Regime in the Biquaternion Spectrum](exceptional-points-and-the-nilpotent-regime-in-the-biquaternion-spectrum.html), for the isotropic cone and why the degeneracy available to either sector is diabolic.
- [The Exponential, the Logarithm and the Generator](the-exponential-the-logarithm-and-the-generator.html), for the generator as a logarithm and the boundary between reversible and irreversible processes.
- [Von Neumann Entropy and the Biquaternion Norm](von-neumann-entropy-and-the-biquaternion-norm.html), for the entropy as a function of the quaternionic norm.
- [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html), for the invariance under reversible flow and the increase under coarse-graining.
- [Spin Entropy and the Lorentz Group in Biquaternionic Form](spin-entropy-and-the-lorentz-group-in-biquaternionic-form.html), for the invariance at sharp momentum and the Wigner-rotation increase.
- [The Material–Informational Split as a Superselection Structure in Biquaternionic Form](the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html), for the absence of a conserved sector charge.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) and [Exercise: Four-Momentum Conservation in a Collision](exercise-four-momentum-conservation-in-a-collision.html), for the conservation of the total four-momentum and the invariant mass.
- [Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form](landauers-principle-and-the-material-informational-exchange-in-biquaternionic-form.html), for the exchange rate $k_BT\log2$.
- [Norm and Pairing Conventions](norm-and-pairing-conventions.html) and [Product and Form Conventions](product-and-form-conventions.html), for the trace, the two forms and the two norms.
- [The Central Scalar Limit of Classical Mechanics in Biquaternionic Form](the-central-scalar-limit-of-classical-mechanics-in-biquaternionic-form.html), for the non-relativistic placement of mass and energy in the centre of $\mathbb{B}_{\Psi}$.
