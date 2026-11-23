# __Quantum Thermodynamics in Biquaternionic Form__

## Introduction

Quantum thermodynamics is the thermodynamics of systems whose state is a density operator: equilibrium is the Gibbs state, and the thermodynamic quantities — internal energy, entropy, free energy, heat capacity — are functionals of that state. This article asks what the biquaternion framework adds to that account, and it keeps the answer modest: the framework supplies an **interpretation** of the standard objects, not a new law.

The interpretation rests on one formula, inherited from the companion articles:

$$
\langle\tilde{H}_{\Psi,1},\tilde{H}_{\Psi,2}\rangle_{*}=\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*}).
$$

The scalar part is defined on the algebra itself, and no step below needs the $2\times2$ representation. The partition function and every thermal average are computed by taking the scalar part of a product; the factor $2$ appears once, in the partition function, where it counts the two levels of a single biquaternion.

Two structural facts follow and are developed below. First, the Gibbs state of a qubit is an element of the Hermitian subspace $\mathbb{B}_{\Psi}$ — a point in the Bloch ball — and its thermodynamic functionals are scalars extracted from $\mathbb{B}_{\Psi}$-valued objects. Second, the free energy is the additive real scalar carried by the **modular Hamiltonian** $H_{\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}$, which also lies in $\mathbb{B}_{\Psi}$; and the temperature $\beta$ that parametrises the state measures a displacement along the imaginary-time direction of the material sector $\mathbb{B}_{\Phi}$, as the companion articles on the KMS condition and on the partition function record.

The article proceeds as follows. The Gibbs state is defined and its existence condition — the convergence of $Z$ — is treated as part of the content rather than as a technicality. The thermodynamic quantities are then written as functionals of the state and computed through the Hermitian form, with the scalar part as the final reading. The Gibbs state is characterised variationally, as the minimiser of the free-energy functional, and the Legendre structure relating $\log Z$, the entropy, and the free energy is set out with its signs checked against the thermodynamic identities. The low- and high-temperature limits are computed, the third law is examined in its three formulations and the one the algebra decides is identified, the KMS condition is identified as the operator-algebraic characterisation of the same state, and the closing section separates what the framework adds from what it does not.

## The Gibbs State and the Convergence of $Z$

At inverse temperature $\beta$ a quantum system with Hamiltonian $\tilde H_\Psi$ is described by the **Gibbs state**

$$
\tilde{Ϛ}_{\Psi,\beta}=\frac{1}{Z}\,\exp(-\beta H),\qquad
Z(\beta)=2\,\mathrm{Sc}\big(\exp(-\beta H)\big),
$$

provided the partition sum converges. The convergence condition is part of the content, because when it fails the state does not exist.

For a **finite-level** system the partition sum is a finite sum of exponentials, so $Z$ is an entire function of $\beta$ and the Gibbs state exists for every real $\beta$. A single biquaternion is a two-level system, and $n$ of them span $M_{2^n}(\mathbb{C})$; this is the case in which the framework's exact computations live, and it is why no restriction appears on the closed formulas below.

For a system whose spectrum is unbounded above and bounded below — the generic many-body case — convergence depends on the real part of $\beta$. With eigenvalues $E_n\to+\infty$,

$$
|Z(\beta)|\le\sum_n \exp(-\mathrm{Re}(\beta)E_n),
$$

so the sum converges absolutely for $\mathrm{Re}\,\beta>0$ and diverges for $\mathrm{Re}\,\beta<0$. The physical domain is the half-plane $\mathrm{Re}\,\beta>0$, that is, positive temperature. The boundary $\beta\to0^+$ is the infinite-temperature limit, and whether the limit exists is a property of the spectrum. A harmonic oscillator of frequency $\omega$ has $Z=\exp(-\beta\omega/2)/(1-\exp(-\beta\omega))$, finite for $\beta>0$ and divergent as $\beta\to0^+$; a qubit has $Z\to2$, finite. The convergence condition therefore decides the behaviour at infinite temperature, not merely at zero.

The framework's Hamiltonian is Hermitian, $\tilde H_\Psi\in\mathbb{B}_{\Psi}$, so its eigenvalues are real; in the two-level case they are $h_t\pm|\vec h_\Psi|$. From the companion article on the partition function, the thermal operator is

$$
\exp(-\beta H)=\exp(-\beta h_t)\Big(\cosh(\beta|\vec h_\Psi|)\,e_t-i\sinh(\beta|\vec h_\Psi|)\,\vec u_\Psi\Big),
\qquad \vec u_\Psi=\frac{\vec h_\Psi}{|\vec h_\Psi|},
$$

an element of $\mathbb{B}_{\Psi}$. Applying the Hermitian form to $\tilde{H}_{\Psi,1}=e_t$ and $\tilde{H}_{\Psi,2}=\exp(-\beta H)$, and doubling, gives

$$
\boxed{\;Z=2\,\mathrm{Sc}\big(\exp(-\beta H)\big)=2\exp(-\beta h_t)\cosh(\beta|\vec h_\Psi|)\;},
$$

and division gives the state

$$
\tilde{Ϛ}_{\Psi,\beta}=\tfrac12\big(e_t+i\vec s_{\Psi}\big),\qquad
\vec s_{\Psi}=-\tanh(\beta|\vec h_\Psi|)\,\vec u_\Psi.
$$

Its scalar part is $\mathrm{Sc}(\tilde{Ϛ}_{\Psi,\beta})=\tfrac12$, so $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi,\beta})=1$: normalization is itself a statement about the scalar part. The state lies in the Bloch ball, with $|\vec s_{\Psi}|=\tanh(\beta|\vec h_\Psi|)\le1$. It is mixed for every finite $\beta$ and approaches the pure ground state $\tilde\Pi_{\mathrm{id}}(-\vec u_\Psi)=\tfrac12(e_t-i\vec u_\Psi)$ only as $\beta\to\infty$; as $\beta\to0$ it tends to the maximally mixed state $\tfrac12e_t$, the centre of the ball. The Gibbs state is thus a temperature-parametrised path in the Bloch ball from the centre toward the boundary, and thermodynamics is the study of the scalars along that path.

## Thermodynamic Quantities as Functionals of the State

Every thermodynamic quantity of the canonical ensemble is a functional of the Gibbs state, and in the framework each is a scalar extracted by the Hermitian form:

- internal energy: $E[\tilde{Ϛ}_{\Psi}]=\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi)/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=h_t+\vec s_{\Psi}\cdot\vec h_\Psi$; the star is inert on $\mathbb{B}_{\Psi}$, and the unstarred scalar part is real, and non-negative only when $\tilde H_\Psi\ge0$;
- entropy: $S[\tilde{Ϛ}_{\Psi}]=-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$;
- free energy: $F[\tilde{Ϛ}_{\Psi}]=E[\tilde{Ϛ}_{\Psi}]-\tfrac1\beta S[\tilde{Ϛ}_{\Psi}]$;
- heat capacity: $C=\partial E/\partial T$.

The entropy functional needs the logarithm, which exists on $\mathbb{B}$ but is multivalued. The companion exercise on entanglement entropy establishes that $S=-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$ is correct in the interior of the Bloch ball when the principal branch is used, and that the logarithm — hence the formula written this way — is undefined at the pure states, which are zero divisors; the value $S=0$ there is the continuous extension, not a value the logarithm takes. This edge is kept visible rather than smoothed over, and it returns in the variational section below.

For the qubit the Hermitian form evaluates each functional explicitly. With $r_x=\beta|\vec h_\Psi|$ and $\vec s_{\Psi}=-\tanh r_x\,\vec u_\Psi$, the product $\tilde{Ϛ}_{\Psi}\tilde H_\Psi$ has scalar part

$$
\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=\tfrac12\big(h_t+\vec s_{\Psi}\cdot\vec h_\Psi\big)=\tfrac12\big(h_t-|\vec h_\Psi|\tanh r_x\big),
$$

so

$$
\boxed{\;E=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=h_t-|\vec h_\Psi|\tanh r_x\;}.
$$

The eigenvalues of $\tilde{Ϛ}_{\Psi}$ are the level populations, $\eta_{\pm}=\tfrac12(1\pm\tanh x)$ with $\eta_{+}$ the ground-state population, and the entropy is the binary entropy of the pair:

$$
\boxed{\;S=-\eta_{+}\log\eta_{+}-\eta_{-}\log\eta_{-}=\log 2+\log\cosh x-x\tanh x\;}.
$$

The free energy is $F=E-S/\beta$, which also equals $-\beta^{-1}\log Z$:

$$
F=h_t-\frac{\log 2+\log\cosh x}{\beta}.
$$

The **heat capacity** is a fluctuation. Differentiating $E$ at fixed spectrum,

$$
C=\frac{\partial E}{\partial T}=k_B\,\beta^2\,\mathrm{Var}(\tilde H_\Psi),
\qquad
\mathrm{Var}(\tilde H_\Psi)=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}(\tilde{H}_\Psi^2)^{*})-\big(2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})\big)^2 .
$$

Since $\tilde{H}_\Psi^2=(h_t^2+|\vec h_\Psi|^2)e_t+2i h_t\vec h_\Psi$ lies in $\mathbb{B}_{\Psi}$, the variance is computed by the same Hermitian form:

$$
\mathrm{Var}(\tilde H_\Psi)=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{H}_\Psi^2)-\big(2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})\big)^2=|\vec h_\Psi|^2\,\mathrm{sech}^2x .
$$

Hence $C=x^2\mathrm{sech}^2x$ in units of $k_B$: the two-level **Schottky heat capacity**. It is non-negative because a variance is, and it vanishes at both ends of the temperature range, with a maximum $C_{\max}=0.439229$ at $x=1.199679$, the root of $x\tanh x=1$. The framework adds nothing to the value; it supplies the route, since both $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})$ and $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}(\tilde{H}_\Psi^2)^{*})$ are scalar extractions.

**Numerical check on an independently chosen case.** Take $h_t=0.4$, $\vec h_\Psi=(0.5,0.2,-0.6)$, $\beta=0.8$. Then $|\vec h_\Psi|=0.8062258$, $x=0.6449806$, and the eigenvalues are $h_t\pm|\vec h_\Psi|=1.2062258$ and $-0.4062258$. The Hermitian form gives,

$$
Z=2\,\mathrm{Sc}\big(\exp(-\beta H)\big)=2\exp(-0.32)\cosh(0.6449806)=1.7649944,
$$

while the direct sum over levels gives $\exp(-0.8(1.2062258))+\exp(-0.8(-0.4062258))=1.7649944$. The functionals are $E=-0.0581630$, $S=0.5216171$, $F=-0.7101844$, and $C=0.2816555$; they satisfy $F=E-S/\beta$ to machine precision. A four-level **product** Hamiltonian — two independent qubits with $(h_{t,1},\vec h_{\Psi,1})=(0.3,(0.2,0,-0.4))$ and $(h_{t,2},\vec h_{\Psi,2})=(-0.7,(0.1,0.5,0.2))$ at $\beta=1.1$ — gives $Z=8.2828313$, equal both to the product of the two single-qubit partition functions and to the direct sum of the four level weights; its functionals satisfy the same Legendre relations.

## The Variational Characterisation

The Gibbs state is not merely the state obtained by exponentiating the Hamiltonian; it is selected by a variational principle, and the principle can be stated entirely in the framework's terms.

Consider the free-energy functional on states,

$$
\mathcal F[\tilde{Ϛ}_{\Psi}]=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})-\frac{1}{\beta}S[\tilde{Ϛ}_{\Psi}]
=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})+\frac{2}{\beta}\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi}),
$$

with $S[\tilde{Ϛ}_{\Psi}]=-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$. Extremise $\mathcal F[\tilde{Ϛ}_{\Psi}]-\mu\,(2\,\mathrm{Sc}\,\tilde{Ϛ}_{\Psi}-1)$ over Hermitian elements of $\mathbb{B}_{\Psi}$. The variation gives

$$
\tilde H_\Psi+\frac{1}{\beta}\big(\log\tilde{Ϛ}_{\Psi}+e_t\big)-\mu\,e_t=0,
$$

hence $\log\tilde{Ϛ}_{\Psi}=-\beta\tilde H_\Psi+(\mu\beta-1)e_t$ and

$$
\tilde{Ϛ}_{\Psi}=\frac{\exp(-\beta H)}{Z},\qquad Z=2\,\mathrm{Sc}\,\exp(-\beta H).
$$

The stationary point is the Gibbs state, and it is a minimum: $\mathcal F$ is convex, because $-\tfrac1\beta S$ is convex ($S$ is concave) while $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})$ is linear. The minimum value is the free energy,

$$
\min_{\tilde{Ϛ}_{\Psi}}\mathcal F[\tilde{Ϛ}_{\Psi}]=\mathcal F[\tilde{Ϛ}_{\Psi,\beta}]=-\frac{1}{\beta}\log Z .
$$

The same statement can be read as the **maximum-entropy principle**: at fixed internal energy $\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=E$, the Gibbs state maximises $S[\tilde{Ϛ}_{\Psi}]$, and the two variational problems are Legendre transforms of one another. The derivation uses only the Hermitian form and the entropy functional, both of which are framework objects.

One caveat belongs here. The functional $\mathcal F$ is defined where $\log\tilde{Ϛ}_{\Psi}$ exists, that is, in the interior of the Bloch ball. The minimiser is interior for every finite $\beta$, since $|\vec s_{\Psi}|=\tanh(\beta|\vec h_\Psi|)<1$, but as $\beta\to\infty$ it approaches the boundary, where the functional is undefined. The variational characterisation therefore describes the finite-$\beta$ states exactly and the zero-temperature state only as a limit — the same boundary already noted for the entropy.

## Legendre Structure and Thermodynamic Identities

The thermodynamic potentials are not independent; they are Legendre transforms of one another, with $\log Z$ as the generating function. With $\beta=1/(k_BT)$ the inverse temperature,

$$
A(\beta):=\log Z,\qquad
E=-\frac{\partial A}{\partial\beta},\qquad
S=k_B\left(A+\beta E\right)=k_B\left(A-\beta\frac{\partial A}{\partial\beta}\right),\qquad
F=-\frac{A}{\beta}=E-TS.
$$

The first two say that $A$ and $S$ are Legendre conjugates in the variables $\beta$ and $E$: from $S=k_B(A+\beta E)$ and $E=-\partial A/\partial\beta$ one finds

$$
\frac{\partial S}{\partial E}=\beta,
$$

which is the thermodynamic identity $\mathrm{d}E=T\,\mathrm{d}S$ at fixed spectrum, and the involution returns $A=S-\beta E$. The relation $F=E-TS$ says that $F$ is the Legendre transform of the energy in the entropy, with $T=\partial E/\partial S$, and it satisfies

$$
\frac{\partial F}{\partial T}=-S .
$$

All four identities hold for the explicit qubit functions of the preceding section. On the case checked above they hold numerically: $S=A+\beta E$ and $F=E-S/\beta$ to $10^{-31}$, while finite differences reproduce $\partial S/\partial E=\beta=0.8$ and $\partial F/\partial T=-S$ to eight digits. The same relations hold for the four-level product Hamiltonian.

In the framework each of $A$, $E$, $S$, $F$ is a scalar obtained by the Hermitian form from an $\mathbb{B}_{\Psi}$-valued object: $E=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})$, $S=-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$, and $F=-\beta^{-1}A$ with $A=\log Z=\mathrm{Sc}(H_{\mathrm{modular}}-\beta\tilde H_\Psi)$, the scalar part of the modular Hamiltonian once the Hamiltonian's own scalar part is removed (next section). The Legendre structure itself is standard thermodynamics; the framework's contribution is that every member of the chain is a scalar extraction from $\mathbb{B}_{\Psi}$.

## Low- and High-Temperature Limits

The limits test the signs and the normalizations of the preceding sections, and they display where the convergence condition bites.

**Low temperature, $\beta\to\infty$ ($T\to0$).** Since $\tanh x\to1$ and $\log\cosh x-x\tanh x\to-\log2$,

$$
\vec s_{\Psi}\to-\vec u_\Psi,\qquad
\tilde{Ϛ}_{\Psi}\to\tilde\Pi_{\mathrm{id}}(-\vec u_\Psi)=\tfrac12\big(e_t-i\vec u_\Psi\big),
$$

the pure ground state, and

$$
E\to h_t-|\vec h_\Psi|,\qquad S\to0,\qquad F\to h_t-|\vec h_\Psi|,\qquad C\to0 .
$$

The internal energy tends to the lower eigenvalue $h_t-|\vec h_\Psi|$ and the free energy to the same value, as it must at zero temperature; the entropy vanishes, and the heat capacity vanishes because the system is frozen into a single level. The limit is finite throughout for the qubit.

**High temperature, $\beta\to0$ ($T\to\infty$).** Since $\tanh x\to0$ and $\log\cosh x\to0$,

$$
\vec s_{\Psi}\to0,\qquad \tilde{Ϛ}_{\Psi}\to\tfrac12 e_t,
$$

the maximally mixed state, and

$$
E\to h_t,\qquad S\to\log 2,\qquad C\to0,\qquad F=-\frac{\log Z}{\beta}\to-\infty .
$$

The internal energy tends to the arithmetic mean $h_t$ of the two levels, which are equally populated; the entropy tends to $\log2$, the maximum for a two-state system; and the heat capacity vanishes because the populations are already equal and further heating changes nothing. The free energy diverges as $-(\log2)/\beta$: when $Z$ tends to the finite degeneracy $2$, $-T\log Z$ diverges in $T$, not in the state.

| Quantity | $\beta\to\infty$ ($T\to0$) | $\beta\to0$ ($T\to\infty$) |
|---|---|---|
| $\tilde{Ϛ}_{\Psi}$ | $\tilde\Pi_{\mathrm{id}}(-\vec u_\Psi)$ (pure) | $\tfrac12 e_t$ (maximally mixed) |
| $E$ | $h_t-|\vec h_\Psi|$ | $h_t$ |
| $S$ | $0$ | $\log 2$ |
| $F$ | $h_t-|\vec h_\Psi|$ | $-\infty$ |
| $C$ | $0$ | $0$ |

The high-temperature limit is exactly where the convergence condition of the second section acts. The qubit's $Z\to2$ is finite, so the limit exists and gives $S\to\log2$. For the harmonic oscillator, $Z\to\infty$ as $\beta\to0^+$, so no state at $\beta=0$ exists and the entropy has no finite high-temperature limit. That difference is invisible in the finite-level formulas alone; it is a property of the spectrum, and it is why the convergence of $Z$ was treated above as content.

## The KMS Condition as the Characterisation of the Same State

The Gibbs state is one description of thermal equilibrium; the KMS condition is another, and the companion article on the KMS condition shows that they describe the same state, not two facts that happen to agree.

In the framework, with operators $\tilde Q_2,\tilde Q_1\in\mathbb{B}$ and thermal state $\omega_\beta$, the correlation function $F_{\tilde Q_2\tilde Q_1}(r'_t)=\omega_\beta(\tilde Q_2\,\alpha_{r'_{t}}(\tilde Q_1))$ extends analytically to the strip $0<\mathrm{Im}\,r'_t<\beta$ and satisfies the boundary relation

$$
F_{\tilde Q_2\tilde Q_1}(r'_t+i\beta)=F_{\tilde Q_1\tilde Q_2}(-r'_t).
$$

By the Haag–Hugenholtz–Winnink theorem this relation characterises the thermal state at inverse temperature $\beta$, and the Gibbs state satisfies it; the two are the same state. The framework's contribution is the location of the objects. The analytic continuation is a shift in the complexified time plane whose imaginary direction is the time coordinate $i r'_t$ of $\mathbb{B}_{\Phi}$ and whose real direction is the time coordinate of $\mathbb{B}_{\Psi}$, as the KMS article states, and the **modular Hamiltonian**

$$
H_{\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi,\beta}=\beta\tilde H_\Psi+(\log Z)\,e_t=\beta\big(\tilde H_\Psi-F e_t\big)
$$

lies in $\mathbb{B}_{\Psi}$ — it is Hermitian by construction. The last equality uses $\log Z=-\beta F$ and displays the role of the free energy: it is the real scalar by which the Hamiltonian must be shifted so that $H_{\mathrm{modular}}$ generates the modular flow of the Gibbs state. Equivalently, $\mathrm{Sc}(H_{\mathrm{modular}}-\beta\tilde H_\Psi)=\log Z$, so $\log Z$ — and with it the whole Legendre chain — is a scalar part of an $\mathbb{B}_{\Psi}$ element. Nothing here is additional to the KMS article's statement; it is recorded because the same state is the subject of both, and because the modular Hamiltonian is where the free energy sits in the framework.

## The Third Law in Three Formulations

Three statements travel under the name. The **Nernst heat theorem** says $S\to S_0$ with $S_0$ finite as $T\to0$. The **unattainability** formulation says $T=0$ cannot be reached in a finite sequence of operations. The **absolute-entropy** formulation says $S_0=0$, which holds exactly when the ground state is nondegenerate. The first is a theorem of the Gibbs formula, the second is not a theorem of any formula, and the third is false as stated. The framework's contribution is to say which is which, and to exhibit the counterexample to the third inside the algebra.

**The Nernst form is a substitution, and it is best written in $N$.** Write $N$ for the quaternionic norm of the state, $N=\tfrac14(1-|\vec s_\Psi|^{2})=\tfrac14\operatorname{sech}^{2}x$ with $x=\beta|\vec h_\Psi|$; it is the quantity that vanishes at the pure states and reaches $\tfrac14$ at the centre. Inverting gives $\cosh x=1/(2\sqrt N)$ and $\tanh x=\sqrt{1-4N}$, so the entropy of the preceding sections becomes a function of one variable,

$$
S=\log 2+\log\cosh x-x\tanh x
=\log 2-\tfrac12\log(4N)-\sqrt{1-4N}\;\operatorname{artanh}\sqrt{1-4N}.
$$

**The two infinities cancel, and the cancellation is the theorem.** As $N\to0$ the term $-\tfrac12\log(4N)$ diverges to $+\infty$ and $\operatorname{artanh}\sqrt{1-4N}$ diverges with it; their difference tends to $-\log2$, which cancels the $\log2$ and leaves zero. Verified from $N=\tfrac14$ down to $N=4.5\times10^{-5}$: the two expressions for $S$ agree to $1.3\times10^{-13}$.

**The approach is logarithmic in $N$, and that is the quantitative content of the law here.** Expanding the same expression at small $N$,

$$
S=-N\log N+N+O\bigl(N^{2}\log N\bigr),\qquad \frac{dS}{dN}=\log\frac1N+O(1),
$$

with the remainder confirmed to the stated order across seven decades of $N$. So the derivative diverges: **the entropy is infinitely sensitive to the last of the distance to the boundary, while the distance itself is exponentially small in $x$.** Since $N\propto e^{-2x}$, every halving of $N$ costs the same increment of $x$, tending to $\tfrac12\log 2=0.346573590$ — measured as $0.347814$ at $x=3$ and $0.346574$ at $x=8$. Reaching $N=0$ takes infinitely many halvings of a quantity that never reaches zero, which is Nernst's unattainability restated as a statement about one function.

**Unattainability itself is imported, and honestly so.** "In a finite number of operations" quantifies over operations, and no algebraic identity constrains how many are allowed or what they cost. What the algebra supplies is the geometric half. The boundary $N=0$ is a level set of $N$, every reversible motion preserves $N$, so no reversible process moves along the thermal curve at all — the result of *What the Biquaternion Algebra Cannot Do*, where the Gibbs path is shown to lie on no orbit of the reversible group. In this setting the unattainability formulation is therefore **equivalent to "the thermal path is not an orbit"**, and the resource bound that turns it into a law about engines is added from outside.

**The absolute-entropy form fails, and the algebra makes the failure exact.** Both statements above presumed $|\vec h_\Psi|>0$. Take instead a Hamiltonian with no vector part, $\tilde H_\Psi=h_t e_t$, a pure central element. Its levels coincide, the spectrum is doubly degenerate, and

$$
Z=2e^{-\beta h_t},\qquad
\tilde{Ϛ}_{\Psi,\beta}=\tfrac12 e_t,\qquad
\vec s_{\Psi}=0,\qquad r=0,\qquad N=\tfrac14,\qquad S=\log 2
$$

at **every** $\beta$: the curve has collapsed to a point, the centre of the ball. Verified for $h_t$ of both signs and $\beta$ from $0$ to $10^{6}$: $S=0.693147180560$, $N=0.250000000000$, unchanged, with $C=0$ throughout and $E=h_t$ independent of temperature.

**Residual entropy is therefore the centre of the ball, and the third law is the statement that the centre is not where the curve ends.** A residual entropy $\log g$ is $N=\tfrac14$ in this case; zero residual entropy is $N=0$. The two ideals the law conflates — no entropy at zero temperature, and a pure state at zero temperature — coincide in this language, and the degenerate Hamiltonian separates both of them from the Gibbs formula, which holds in every case.

**A near-degeneracy shows the scale, and it shows that the law is about the gap, not about the temperature.** With $|\vec h_\Psi|=10^{-3}$ the curve does reach the boundary, but only for $x\gtrsim1$, that is $\beta\gtrsim10^{3}$:

| $\beta$ | $10$ | $10^{2}$ | $10^{3}$ | $10^{4}$ |
| --- | --- | --- | --- | --- |
| $N$ | $0.2499750$ | $0.2475166$ | $0.1049936$ | $2.06\times10^{-9}$ |
| $S$ | $0.6930972$ | $0.6881721$ | $0.3653339$ | $4.33\times10^{-8}$ |

Cooling a system whose splitting is a milli-unit into the regime where $S$ has visibly fallen requires a thousand-fold inverse temperature. The law is exact at every $|\vec h_\Psi|>0$, its crossover is set by the gap, and the degenerate case is not the limit of this table but the separate exact case in which no value of $\beta$ moves the state at all.

**What the section establishes, and what it does not.** The Nernst form is reproduced, and reproduced as a statement about one variable: on the thermal curve both the entropy and the heat capacity depend on $N$ alone, $C=4N\operatorname{artanh}^{2}\sqrt{1-4N}$, verified to $10^{-12}$. Unattainability is not derived; its geometric half is, and its resource half is imported. The absolute-entropy form is refuted by an element of the algebra, exactly rather than approximately. None of this is new thermodynamics, and the closing section's claim stands unchanged; what the framework decides is the split between proved, imported and false.

## What the Framework Adds, and What It Does Not

The framework adds an **interpretation** with three components.

First, the computational spine is algebraic: the partition function, every thermal average, the entropy, and the heat capacity are obtained by extracting a scalar part from a product of $\mathbb{B}_{\Psi}$ elements, and the only factor that is not algebraic is the $2$ that counts the two levels. The variance form of the heat capacity, $C=k_B\beta^2[2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{H}_\Psi^2)-(2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*}))^2]$, shows the interpretation at work.

Second, the state is geometric: the Gibbs state is the point $\vec s_{\Psi}=-\tanh(\beta|\vec h_\Psi|)\vec u_\Psi$ in the Bloch ball, and temperature traverses the ball from its centre toward its boundary.

Third, the temperature is a direction: $\beta$ measures a displacement along the imaginary-time axis of the material sector $\mathbb{B}_{\Phi}$, while the modular Hamiltonian $H_{\mathrm{modular}}=\beta(\tilde H_\Psi-Fe_t)$, which carries the free energy, lies in $\mathbb{B}_{\Psi}$. The thermal structure is therefore a coupling of the two sectors of the kind the KMS article describes.

The framework does **not** produce a new thermodynamic law. The Gibbs state, the Legendre relations, the variational principle, the KMS characterisation, the Schottky heat capacity, both temperature limits, and the Nernst form of the third law are standard, and the framework reproduces them. What it changes is where they live: the potentials become scalar extractions from the informational sector, and the temperature becomes an imaginary-time displacement in the material sector. Whether that interpretation has consequences beyond the standard account is open, and no such consequence is claimed here.

## Summary

Quantum thermodynamics in biquaternionic form is the thermodynamics of the Gibbs state $\tilde{Ϛ}_{\Psi,\beta}=\exp(-\beta H)/Z$, read through the Hermitian form $\langle\tilde{H}_{\Psi,1},\tilde{H}_{\Psi,2}\rangle_{*}=\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})$, and the normalisation of a state is $\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=\tfrac12$. The partition function is $Z=2\,\mathrm{Sc}(\exp(-\beta H))=2\exp(-\beta h_t)\cosh(\beta|\vec h_\Psi|)$ for a qubit, and every thermal average is twice a scalar part.

The Gibbs state exists only when $Z$ converges: always for a finite-level system, and in the half-plane $\mathrm{Re}\,\beta>0$ for a spectrum unbounded above. The infinite-temperature boundary $\beta\to0$ is where the condition matters, and it separates the qubit ($Z\to2$) from the oscillator ($Z\to\infty$).

The thermodynamic functionals of the state are the internal energy $E=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})$, the entropy $S=-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$, the free energy $F=E-S/\beta$, and the heat capacity $C=\partial E/\partial T$. For a qubit they are $E=h_t-|\vec h_\Psi|\tanh r_x$, $S=\log2+\log\cosh x-x\tanh x$, $F=h_t-(\log2+\log\cosh x)/\beta$, and $C=x^2\mathrm{sech}^2x$ with $r_x=\beta|\vec h_\Psi|$, the Schottky form with maximum $0.439229$ at $x=1.199679$.

The Gibbs state is the minimiser of $\mathcal F[\tilde{Ϛ}_{\Psi}]=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})-\beta^{-1}S[\tilde{Ϛ}_{\Psi}]$, equivalently the maximiser of the entropy at fixed energy. The potentials are Legendre transforms: $S=\log Z+\beta E$ with $\partial S/\partial E=\beta$, and $F=E-TS$ with $\partial F/\partial T=-S$. The low-temperature limits are the pure ground state, $E=F=h_t-|\vec h_\Psi|$, $S=C=0$; the high-temperature limits are $\tilde{Ϛ}_{\Psi}=\tfrac12e_t$, $E=h_t$, $S=\log2$, $C=0$. The KMS condition $F_{\tilde Q_2\tilde Q_1}(r'_t+i\beta)=F_{\tilde Q_1\tilde Q_2}(-r'_t)$ is the operator-algebraic characterisation of the same state, and its modular Hamiltonian $H_{\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}=\beta(\tilde H_\Psi-Fe_t)$ lies in $\mathbb{B}_{\Psi}$. The third law is read in its three formulations: the Nernst form is a substitution, $S=\log2-\tfrac12\log(4N)-\sqrt{1-4N}\operatorname{artanh}\sqrt{1-4N}\to0$ as $N\to0$ with $S=-N\log N+N+O(N^{2}\log N)$; the unattainability form is not a theorem of the algebra but is equivalent in this setting to the Gibbs path being on no orbit of the reversible group; and the absolute-entropy form is false, since a Hamiltonian with $\vec h_\Psi=0$ gives $\tilde{Ϛ}_{\Psi,\beta}=\tfrac12e_t$, $N=\tfrac14$ and $S=\log2$ at every $\beta$.

The framework reproduces standard thermodynamics and claims no new law. Its addition is the interpretation: the potentials are scalar parts of $\mathbb{B}_{\Psi}$ elements, the state is a path in the Bloch ball, and the temperature is a displacement along the imaginary-time axis of $\mathbb{B}_{\Phi}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\imath^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{C}=\mathbb{C}e_t$ | Complex subspace (centre of $\mathbb{B}$) |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (informational sector): real scalar, imaginary vector |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ | Hermitian Hamiltonian (observable) |
| $\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})$ | Scalar part of a product (computational spine) |
| $Z=2\,\mathrm{Sc}(\exp(-\beta H))$ | Partition function |
| $\tilde{Ϛ}_{\Psi,\beta}=\exp(-\beta H)/Z=\tfrac12(e_t+i\vec s_{\Psi})$ | Gibbs state |
| $\vec s_{\Psi}=-\tanh(\beta|\vec h_\Psi|)\vec u_\Psi$ | Bloch vector of the Gibbs state |
| $r_x=\beta|\vec h_\Psi|$ | Thermal parameter |
| $N=\tfrac14(1-|\vec s_{\Psi}|^{2})=\tfrac14\operatorname{sech}^{2}x$ | Quaternionic norm of the state; $N=0$ at the pure states, $N=\tfrac14$ at the centre |
| $E=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=h_t-|\vec h_\Psi|\tanh r_x$ | Internal energy |
| $S=-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})=\log2+\log\cosh x-x\tanh x$ | Entropy (units of $k_B$) |
| $F=E-S/\beta=h_t-(\log2+\log\cosh x)/\beta$ | Free energy |
| $C=\partial E/\partial T=k_B\beta^2\mathrm{Var}(\tilde H_\Psi)=r_x^2\mathrm{sech}^2x$ | Heat capacity (Schottky form) |
| $A(\beta)=\log Z$, $S=A+\beta E$, $F=E-TS$ | Legendre structure |
| $H_{\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi,\beta}=\beta(\tilde H_\Psi-Fe_t)$ | Modular Hamiltonian (in $\mathbb{B}_{\Psi}$) |
| $F_{\tilde Q_2\tilde Q_1}(r'_t+i\beta)=F_{\tilde Q_1\tilde Q_2}(-r'_t)$ | KMS boundary relation |
| $\beta=1/(k_BT)$ | Inverse temperature |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1* (Pergamon, 1980), for the Gibbs state, the thermodynamic potentials, and the Legendre structure.
- H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics* (Wiley, 1985), for the Legendre transforms and the thermodynamic identities.
- R. H_{\mathrm{modular}}. Pathria and P. D. Beale, *Statistical Mechanics* (Butterworth–Heinemann, 2011), for the canonical ensemble and the Schottky heat capacity of a two-level system.
- H_{\mathrm{modular}}. Huang, *Statistical Mechanics* (Wiley, 1987), for the partition function and its relation to the spectrum.
- J. Gemmer, M. Michel, and G. Mahler, *Quantum Thermodynamics* (Springer, 2009), for the quantum-statistical formulation of equilibrium thermodynamics.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the imaginary-time formulation in which $\beta$ is the circumference of the thermal circle.
- R. Haag, N. M. Hugenholtz, and M. Winnink, "On the equilibrium states in quantum statistical mechanics," *Communications in Mathematical Physics* **5** (1967) 215–236, for the KMS characterisation of thermal equilibrium.
- M. Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications* (Springer, 1970), for the modular Hamiltonian $H_{\mathrm{modular}}=-\log\rho$.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the von Neumann entropy and its properties.
- Companion articles: [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html), for the thermal operator and $Z$; [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html), for the operator-algebraic characterisation and the modular Hamiltonian; [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the state space, the plain form, and the entropy; [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) and [Four-Vectors and the Interval](four-vectors-and-the-interval.html), for the two sectors; [Exercise: Entanglement Entropy and the Partial Trace](exercise-entanglement-entropy-and-the-partial-trace.html), for the entropy functional $-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$ and its domain, for the geometry of the state space; [The Hermitian Tomita–Takesaki Theory under the Biquaternion Framework](the-hermitian-tomita-takesaki-theory-under-the-biquaternion-framework.html), for the modular structure in the framework.
