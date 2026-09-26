# __The Double-Slit Experiment in Biquaternionic Form__

## Introduction

The double-slit experiment is the minimal experiment in which a quantum amplitude is the **sum of two alternatives**. A particle reaches a screen point by either slit, the two routes contribute two amplitudes, and the intensity at the screen is the squared modulus of their sum. The cross term is the interference pattern; closing one slit removes it. Everything that is strange and everything that is ordinary about quantum amplitudes is visible in this one arrangement.

This article asks what the biquaternion framework $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ says about the double slit, and what it does not. The read list has already settled the three objects the question depends on. *The Path Integral in Biquaternionic Form* identifies the symbol $i$ of the phase $e^{iS/\hbar}$ with the **central scalar imaginary**, places the exponent $iS/\hbar$ in the material sector $\mathbb{M}_-$, and records that only *relative* phases of paths are observable. *The Schrödinger Equation in Biquaternionic Form* identifies the wave function not with an element of $\mathbb{M}_+$ but with a **spinor in a minimal left ideal** $\mathbb{B}\tilde{P} \cong \mathbb{C}^2$, and shows that the same central $i$ is the complex structure of that module. *Quantum Mechanics in Biquaternionic Form* supplies the states, observables, Born rule, and measurement rule for the corresponding qubit. Two further articles of the series carry the geometry the double slit turns out to use: *The Bloch Ball as the Trace-One Slice of the Future Light Cone* identifies the state space with a slice of the norm-form cone, and *Decoherence as Idempotent Projection* describes the destruction of coherence as an algebraic channel. This article assembles these into the canonical interference experiment.

The division between what is established and what is interpretation is stated here and kept explicit.

- **Established, and recomputed below.** Two route amplitudes add, $K = K_1 + K_2$, and the intensity is $I = a_1^2 + a_2^2 + 2a_1a_2\cos\delta$ with $\delta$ the relative phase; a common phase shift of both routes is unobservable. The which-path degree of freedom is a qubit whose state is an element $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ of $\mathbb{M}_+$. The fringe **visibility** is the length of the equatorial part of its Bloch vector, the **path predictability** is its polar part, and $V^2 + P^2 = |\mathbf{r}|^2 \le 1$, with equality if and only if $\tilde{\rho}$ is pure — that is, if and only if $\tilde{\rho}$ lies on the zero-divisor cone of $\mathbb{M}_+$. A which-path measurement, or full dephasing along the path axis, annihilates the equatorial part and with it the fringes. For spinor-valued routes, $I = I_1 + I_2 + 2\,\mathrm{Re}\,\mathrm{Tr}(\psi_1^\dagger\psi_2)$, and a spin overlap reduces the visibility.
- **Interpretation.** Reading the fringe pattern as the projection of a rotating equatorial Bloch vector, and reading the two-slit arrangement as the place where a material-sector action is converted through the central phase into an informational-sector state, are geometric and structural readings of the algebra. The algebra is consistent with them; it does not force them.
- **Gap, left visible.** The framework supplies the phase and the state geometry but not the **action**, the **measure**, or the space of paths; and it does not select which slit, or which screen point, a given detection realises. The first gap is inherited from the path-integral article, the second from the measurement-problem article; both are restated where they arise and collected in the open questions.

One further finding is reported as a **limit on what the double slit demonstrates**. For a beam whose two routes carry the same spin state, the *spin-summed* two-path intensity is unchanged when the central root $i$ of the phase is replaced by a fixed non-central root $\hat{\mu}$; the difference between the two choices appears only under spin analysis, or when the two routes carry different spin states. The spin-summed double-slit pattern therefore does not by itself witness the centrality of the phase; the framework's grounds for the central root lie in the state-vector equation and in the complex structure of the state module, not in this pattern. The computation is in the section on the phase root below, and it is stated against the pull to claim more for the experiment than it shows.

The article is organized as follows. The next section writes the two-route amplitude and its interference. The section after that treats the fringe pattern and its standard geometry. The following section identifies the which-path qubit and its Bloch ball. The next proves the visibility–predictability bound and reads it as the cone condition. A section treats which-path detection and dephasing. A section examines the choice of phase root. A section treats spinor-valued routes and spin-dependent fringes. The article closes with what the algebra supplies, what it does not, and the open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ and its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$. A Hermitian element is written $\tilde{H} = h_0 e_0 + i\mathbf{h}$, an idempotent is $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ with $\hat{\mu}$ a unit pure real quaternion, and a state is $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ with $|\mathbf{r}|\le 1$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged, as is the statement that multiplication by $i$ exchanges the sectors, $i\,\mathbb{M}_\pm = \mathbb{M}_\mp$.

## The Two-Path Amplitude

Let $\tilde{K}_j(P)$ be the amplitude for the particle to arrive at the screen point $P$ through slit $j$, $j = 1, 2$. Each is a sum over paths through that slit, and by the path-integral article the single-path phase is a **central** unitary element of $\mathbb{C}_{\mathbb{B}}$ whose exponent lies in $\mathbb{M}_-$:

$$
\tilde{K}_j(P) \;=\; \int_{\text{paths via slit }j}\!\mathcal{D}x\; e^{iS_j[x]/\hbar}, \qquad e^{iS_j/\hbar} \in \mathbb{C}_{\mathbb{B}}, \qquad \frac{iS_j}{\hbar} \in \mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_- .
$$

Because each phase factor is central and the sum of central elements is central, each $\tilde{K}_j$ is a complex scalar times $e_0$. Writing $a_j(P) = |\tilde{K}_j(P)| \ge 0$ and $\varphi_j(P) = S_j(P)/\hbar$ for its phase,

$$
\tilde{K}_j(P) = a_j(P)\, e^{i\varphi_j(P)}\, e_0 .
$$

The total amplitude is the **sum of the two alternatives**,

$$
\tilde{K}(P) = \tilde{K}_1(P) + \tilde{K}_2(P) = \bigl(a_1 e^{i\varphi_1} + a_2 e^{i\varphi_2}\bigr) e_0 ,
$$

which is again central. The additivity is the superposition principle; in the algebra it is the linearity of the complex one-dimensional space $\mathbb{C}_{\mathbb{B}}$ over $\mathbb{C}$ (equivalently, the additivity of the path integral, which the path-integral article takes as its starting point). The intensity is the scalar coefficient of the Hermitian norm of the amplitude:

$$
\tilde{K}(P)\tilde{K}(P)^\dagger = I(P)\,e_0, \qquad I(P) = a_1^2 + a_2^2 + 2 a_1 a_2 \cos\delta(P), \qquad \delta(P) := \varphi_1(P) - \varphi_2(P).
$$

**Only the relative phase is observable.** The substitution $\varphi_j \mapsto \varphi_j + c$ with $c$ constant multiplies both amplitudes by the same central element $e^{ic}$, which cancels in the Hermitian norm $\tilde{K}\tilde{K}^\dagger$; and it cancels in any state built from $\tilde{K}$ as well, since $\tilde{K}\tilde{K}^\dagger \mapsto e^{ic}\tilde{K}\tilde{K}^\dagger e^{-ic} = \tilde{K}\tilde{K}^\dagger$. This is the path-integral article's statement that the global phase of a path is unobservable and only differences of actions are observable, in its simplest instance. The double slit is the arrangement in which exactly one relative phase, $\delta$, is read off.

Two observations about where the objects live belong here, because later sections use them.

- **The relative phase is central.** $\delta = \varphi_1 - \varphi_2$ is a real number, and $i\,\delta \in \mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_-$ lies along the $ict$ direction, the same axis on which the path-integral article locates the phase exponent and the Feynman-propagator article locates $i\epsilon$. The argument of the complex number $e^{i\delta}$ is supplied by the central imaginary; a non-central root would supply a different kind of argument, and the section on the phase root examines what that changes.
- **The scalar amplitude carries no spin.** $\tilde{K}$ is a complex scalar times $e_0$; it is not an element of $\mathbb{M}_+$ and not a spinor. For a spin-independent beam this is the whole amplitude, and the pattern it produces is a statement about the center $\mathbb{C}_{\mathbb{B}}$. When the two routes can be distinguished by spin, the amplitude is a spinor and the cross term acquires a spin overlap; that is the subject of the later section on spinor-valued routes.

## The Fringe Pattern

The standard idealisation of the experiment is two narrow slits separated by a distance $d$ and a screen at distance $D$, with the point $P$ at transverse coordinate $x$ and the two routes equally illuminated. The path-length difference is $L_1 - L_2 \approx d\sin\theta \approx dx/D$, so the relative phase is

$$
\delta(x) = k\,(L_1 - L_2) \approx \frac{2\pi d}{\lambda D}\, x,
$$

with $k = 2\pi/\lambda$ the wavenumber. With equal amplitudes $a_1 = a_2 = a$, the intensity is

$$
I(x) = 4a^2\cos^2\!\Big(\frac{\delta(x)}{2}\Big) = 2a^2\bigl(1 + \cos\delta(x)\bigr).
$$

Maxima occur where $d\sin\theta = m\lambda$ and nodes where $d\sin\theta = (m + \tfrac12)\lambda$, with $m \in \mathbb{Z}$; the fringe spacing on the screen is $\lambda D/d$. For $\lambda = 600\,\mathrm{nm}$, $d = 0.1\,\mathrm{mm}$, $D = 1\,\mathrm{m}$, the spacing is $6\,\mathrm{mm}$ and the first node sits at $3\,\mathrm{mm}$.

Two remarks keep this section honest.

- **Finite slit width adds an envelope, which is standard.** A slit of finite width has its own diffraction pattern, and the observed intensity is the two-slit interference modulated by the single-slit envelope. Nothing about the biquaternion framework changes this; it is ordinary wave optics, and this article does not develop it.
- **The numbers are inputs, not outputs.** The wavelength, the separation $d$, the distance $D$, and the action $S_j$ itself are not supplied by the algebra. What the biquaternion reading supplies is the *identification* of the $i$ in $e^{iS_j/\hbar}$ with the central scalar imaginary, the *location* of the exponent $iS_j/\hbar$ in $\mathbb{M}_-$, and the *statement* that only $\delta$ is observable. It does not supply the action, the measure, or the geometry; that is the path-integral article's central gap, and it is inherited here without change.

## The Which-Path Qubit and the Bloch Ball

The two slits define a **which-path** degree of freedom with exactly two alternatives. In the framework it is a qubit, and its state is an element of $\mathbb{M}_+$. Choose a unit pure real quaternion $\hat{\mu}$ to name the path axis; the two alternatives are the idempotents

$$
\tilde{P}_\pm(\hat{\mu}) = \tfrac12\bigl(e_0 \pm i\hat{\mu}\bigr),
$$

with $\tilde{P}_+ + \tilde{P}_- = e_0$ and $\tilde{P}_+ \tilde{P}_- = 0$. The which-path state is

$$
\tilde{\rho} = \tfrac12\bigl(e_0 + i\mathbf{r}\bigr), \qquad |\mathbf{r}| \le 1,
$$

with **polar** part $r_\parallel = \hat{\mu}\cdot\mathbf{r}$ and **equatorial** part $\mathbf{r}_\perp = \mathbf{r} - (\hat{\mu}\cdot\mathbf{r})\,\hat{\mu}$. The polar part is the population bias between the two paths; the equatorial part is the coherence between them. The state is pure, $\tilde{\rho}^2 = \tilde{\rho}$ and $|\mathbf{r}| = 1$, exactly when it lies on the two-sphere; it is mixed, $|\mathbf{r}| < 1$, otherwise.

The connection with the two route amplitudes is explicit. For a spin-independent beam, write the two amplitudes at the screen point $P$ as $\tilde{K}_j = A_j e_0$ and form the spinor $\psi = \bigl(A_1, A_2\bigr)$ in the framework's state module $\cong \mathbb{C}^2$. The Schrödinger article's construction gives

$$
\tilde{\rho} = \frac{\psi\,\psi^\dagger}{\mathrm{Tr}(\psi^\dagger\psi)},
$$

and the entries are, with $\rho_{jk}$ the matrix elements in the path basis,

$$
\rho_{11} = \frac{|A_1|^2}{|A_1|^2 + |A_2|^2}, \qquad
\rho_{22} = \frac{|A_2|^2}{|A_1|^2 + |A_2|^2}, \qquad
\rho_{12} = \frac{A_1 A_2^{*}}{|A_1|^2 + |A_2|^2}.
$$

Three identifications follow, each of which is a translation rather than a new fact.

1. **The population bias is the polar component,** $r_\parallel = \rho_{11} - \rho_{22} = \dfrac{|A_1|^2 - |A_2|^2}{|A_1|^2 + |A_2|^2}$.
2. **The coherence is the equatorial component,** with length $|\mathbf{r}_\perp| = 2|\rho_{12}| = \dfrac{2|A_1 A_2|}{|A_1|^2 + |A_2|^2}$.
3. **The relative phase is the argument of the off-diagonal element,** $\arg \rho_{12} = \arg A_1 - \arg A_2 = \delta(P)$.

So the central phase does double duty. It is the *global* phase of each route, which cancels in the state, and it is the *complex structure* whose argument is the relative phase stored in the off-diagonal element. As the screen point sweeps and $\delta(x)$ varies, the equatorial vector $(r_1, r_2)$ rotates in the equatorial plane of the Bloch sphere. The normalised intensity is exactly the equatorial component along one axis,

$$
\frac{I(x)}{|A_1|^2 + |A_2|^2} = 1 + r_1(x),
$$

which was checked on random amplitudes independently of the derivation: the normalised intensity and $1 + r_1$ agreed to machine precision, and the reconstruction $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ from the Bloch components agreed with $\psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi)$ to machine precision.

**Interpretation.** Reading the fringe pattern as the projection of a rotating equatorial Bloch vector is a geometric reading. The algebra is consistent with it and makes it precise, but the algebra does not require the reading; the standard statement in terms of the two amplitudes is complete without it.

## Visibility, Predictability, and the Norm-Form Bound

Two numbers summarise the pattern and the path information. The **visibility** is the contrast of the fringes,

$$
V = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} = \frac{2|\rho_{12}|}{\rho_{11} + \rho_{22}} = |\mathbf{r}_\perp|,
$$

and the **path predictability** is the population bias,

$$
P = \frac{|\rho_{11} - \rho_{22}|}{\rho_{11} + \rho_{22}} = |r_\parallel| .
$$

Their squares add to the squared Bloch radius:

$$
V^2 + P^2 = |\mathbf{r}_\perp|^2 + r_\parallel^2 = |\mathbf{r}|^2 \le 1 .
$$

This was checked on random pure and mixed which-path states; the identity held to machine precision, and equality held exactly for the pure states and failed for the mixed ones. The bound has a clean biquaternion reading. The norm form of $\tilde{\rho}$ is

$$
N(\tilde{\rho}) = \tilde{\rho}\,\bar{\tilde{\rho}} = \tfrac14\bigl(1 - |\mathbf{r}|^2\bigr)e_0,
$$

so that $|\mathbf{r}|^2 = 1 - 4\,\mathrm{Sc}\bigl(N(\tilde{\rho})\bigr)$, and therefore

$$
V^2 + P^2 = 1 - 4\,\mathrm{Sc}\bigl(N(\tilde{\rho})\bigr).
$$

By *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, a trace-one element of $\mathbb{M}_+$ is a physical state exactly when it lies in the future light cone of the norm form, and it is pure exactly when it lies *on* the cone, where it is a zero divisor. Hence

> **maximal fringe contrast is the statement that the which-path state lies on the zero-divisor cone of $\mathbb{M}_+$; partial contrast is the statement that it lies in the interior.**

Half-filled fringes and a mixed which-path state are the same fact, and it is a fact about the norm form. This is the framework's translation of the standard two-path duality $V^2 + P^2 \le 1$; the algebra does not change the number, it identifies the bound with the cone condition that the framework already uses for purity.

## Which-Path Detection and the Loss of Interference

The framework describes the destruction of the fringes by the same algebraic operations it uses for any measurement.

**Selective detection.** A projective measurement of the path observable — the Hermitian element whose idempotents are $\tilde{P}_\pm(\hat{\mu})$ — has the Born probabilities $p_\pm = \mathrm{Tr}(\tilde{P}_\pm \tilde{\rho}) = \tfrac12(1 \pm r_\parallel)$ and post-measurement states $\tilde{\rho}' = \tilde{P}_\pm(\hat{\mu})$. The equatorial component is annihilated: $\mathbf{r}' = \pm\hat{\mu}$, so $V = 0$. Whether the particle was recorded at slit one or slit two, the interference is gone.

**Non-selective detection.** If the which-path record is not read, the operation is the dephasing channel along $\hat{\mu}$ of *Decoherence as Idempotent Projection*. At full strength ($p = 1$),

$$
\tilde{\rho} \;\longmapsto\; p_+\,\tilde{P}_+(\hat{\mu}) + p_-\,\tilde{P}_-(\hat{\mu}),
$$

which preserves the populations and destroys the coherence; again $\mathbf{r}_\perp = 0$ and $V = 0$. At partial strength $p \in (0,1)$ the equatorial component is scaled by $1-p$, so

$$
V = (1 - p)\,|\mathbf{r}_\perp^{(0)}|,
$$

a reduced contrast rather than a vanished one. The channel is a contractive, information-losing map, idempotent only at full strength, exactly as the decoherence article establishes.

Two structural points, both inherited and neither resolved here.

- **Which direction is measured is an input.** The path axis $\hat{\mu}$ is the pointer direction; the decoherence article records that the framework represents the *consequence* of a system–environment coupling — the channel and its fixed subalgebra — but contains no coupling dynamics from which $\hat{\mu}$ could be derived. The double slit does not change this: the algebra will kill the coherence along any axis one names, and it does not name the axis.
- **Which outcome is realised is not supplied.** Full dephasing yields the mixture $p_+\tilde{P}_+ + p_-\tilde{P}_-$; the *measurement-problem article* shows that the mixture and the single outcome are different objects, and that no change of notation makes the outcome a function of the state. The double slit exhibits both facts at once: the fringes disappear when the paths are distinguished, and the formalism says which record was *made* only probabilistically.

## The Phase Root: Central, or Not

It is natural to ask whether the double slit requires the phase's root to be the central imaginary $i$. The path-integral and Schrödinger articles argue for the central root on grounds of the complex structure of the state module and of norm preservation. The narrower question here is what the two-slit *intensity* can show, and the honest answer is: less than one might expect.

Take a **non-central** root $\hat{\mu}$ — a unit pure real quaternion, $\hat{\mu}^2 = -e_0$, lying in $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$. The phase factor is

$$
e^{\hat{\mu}\,S/\hbar} = \cos\!\Big(\frac{S}{\hbar}\Big)e_0 + \sin\!\Big(\frac{S}{\hbar}\Big)\hat{\mu},
$$

which is unitary, $(e^{\hat{\mu}S/\hbar})(e^{\hat{\mu}S/\hbar})^\dagger = e_0$, and whose exponent $\hat{\mu}S/\hbar$ also lies in $\mathbb{M}_-$. Under the isomorphism $e_k \mapsto -i\sigma_k$ with $\hat{\mu} = e_3$ it maps to

$$
e^{e_3 S/\hbar} \;\longmapsto\; \operatorname{diag}\!\bigl(e^{-iS/\hbar},\, e^{+iS/\hbar}\bigr),
$$

verified directly in the matrix representation. It is a **relative** phase between the two spin components — a spin rotation — not a global phase shared by both.

Now compute the two-path intensity with this root, for a beam whose two routes carry the same spinor $\hat{s}$ (normalised, $\mathrm{Tr}(\hat{s}^\dagger\hat{s}) = 1$). The total amplitude is $\tilde{W}\hat{s}$ with $\tilde{W} = a_1 e^{\hat{\mu}\varphi_1} + a_2 e^{\hat{\mu}\varphi_2}$, an element of the plane $\mathrm{span}\{e_0, \hat{\mu}\}$. Its Hermitian norm is

$$
\mathrm{Tr}\!\bigl((\tilde{W}\hat{s})^\dagger(\tilde{W}\hat{s})\bigr) = \mathrm{Tr}\bigl(\hat{s}^\dagger \bar{\tilde{W}}\tilde{W}\hat{s}\bigr) = N(\tilde{W})\,\mathrm{Tr}(\hat{s}^\dagger\hat{s}) = \bigl(a_1^2 + a_2^2 + 2a_1a_2\cos\delta\bigr),
$$

because $\bar{\tilde{W}}\tilde{W} = N(\tilde{W})e_0$ is central and $N(\tilde{W}) = \bigl(\sum_k a_k\cos\varphi_k\bigr)^2 + \bigl(\sum_k a_k\sin\varphi_k\bigr)^2 = |a_1 e^{i\varphi_1} + a_2 e^{i\varphi_2}|^2$. This is *exactly* the central-phase intensity. The identity was checked numerically on random amplitudes and random spinors: the central and non-central intensities agreed to about $4\times10^{-14}$, the level of floating-point round-off.

So the *spin-summed* two-slit intensity, for a common spin state, is **root-independent**; the double slit, read as an intensity pattern without spin analysis, does not by itself witness the centrality of the phase. What the non-central choice changes is not this number but the *type* of the amplitude and the *action* of the phase:

- the amplitude is a quaternion in a plane that must be chosen, rather than a complex scalar;
- the phase rotates the spin: a spin-resolved intensity *in a basis not aligned with* $\hat{\mu}$ distinguishes the roots, while the intensity resolved in the $\hat{\mu}$ eigenbasis does not (the transverse difference is generically of order unity — about $10.9$ on random cases — whereas the $\hat{\mu}$-resolved difference between the roots agrees with the spin-summed difference to about $4\times10^{-14}$);
- when the two routes carry **different** spin states the *total* intensity itself differs between the two choices, again generically by an order-unity amount (about $9.5$ on random cases);
- the choice of $\hat{\mu}$ is extra input that the algebra does not supply, whereas the central $i$ is fixed by $\mathbb{C} \subset \mathbb{B}$.

The framework's grounds for the central root therefore lie where the Schrödinger and path-integral articles put them — in the complex structure of the state module and in the unitarity of the state-vector equation, which fail for a non-central generator unless the Hamiltonian commutes with it — and not in the scalar two-slit pattern. This section is written against the temptation to overstate what the experiment shows.

## Spinor-Valued Routes and Spin-Dependent Fringes

When the two routes can be distinguished by an internal state, the amplitudes are spinors $\psi_1, \psi_2 \in \mathbb{B}\tilde{P}$ and the total amplitude is their sum, $\psi = \psi_1 + \psi_2$. The Schrödinger article's Hermitian norm gives

$$
I = \mathrm{Tr}(\psi^\dagger\psi) = \mathrm{Tr}(\psi_1^\dagger\psi_1) + \mathrm{Tr}(\psi_2^\dagger\psi_2) + 2\,\mathrm{Re}\,\mathrm{Tr}(\psi_1^\dagger\psi_2),
$$

which was checked on random spinor pairs to machine precision. Write $\psi_j = a_j e^{i\varphi_j}\hat{s}_j$ with $\hat{s}_j$ normalised spinors. Then $\mathrm{Tr}(\psi_j^\dagger\psi_j) = a_j^2$ and the cross term is

$$
2\,\mathrm{Re}\,\mathrm{Tr}(\psi_1^\dagger\psi_2) = 2a_1a_2\,\bigl|\langle \hat{s}_1, \hat{s}_2\rangle\bigr|\,\cos\!\bigl(\delta - \arg\langle \hat{s}_1,\hat{s}_2\rangle\bigr),
$$

where $\langle \hat{s}_1,\hat{s}_2\rangle := \mathrm{Tr}(\hat{s}_1^\dagger\hat{s}_2)$ is the module inner product, of modulus at most one. The visibility is therefore

$$
V = \frac{2a_1a_2\,|\langle \hat{s}_1,\hat{s}_2\rangle|}{a_1^2 + a_2^2},
$$

maximal when the two route spinors are parallel (the scalar case) and vanishing when they are orthogonal, whatever the relative phase. Here the route label $j$ is the index of the two terms, not a second factor of the module; describing a path and a spin together as two qubits would require the tensor-product extension that *Quantum Mechanics in Biquaternionic Form* leaves open. This is the **spin-dependent double slit** in the framework's language, and it makes two things visible at once.

- **The central phase cannot itself produce spin dependence,** because it multiplies both components of the spinor equally; a spin-dependent pattern requires the two routes to differ in their spin part (or a non-central phase, as the preceding section discusses).
- **Which-path and which-spin are complementary.** Any measurement that reveals which route was taken — including one performed on the spin, if the two routes carry orthogonal spin states — supplies the which-path information and removes the cross term. In the algebra this is the loss of the off-diagonal element of $\tilde{\rho}$, and it is the same operation as in the preceding two sections, applied to the spin label instead of the path label.

## What the Algebra Supplies and What It Merely Transcribes

**Standard quantum mechanics, transcribed.**

- The sum of two route amplitudes, the relative-phase interference formula, the nodes and maxima, the fringe geometry, and the diffraction envelope are all standard. None is new, and none depends on the biquaternion structure beyond the identification of the phase's imaginary unit.

**What the biquaternion notation provides.**

- A **canonical complex structure.** The $i$ of the phase and of the relative phase is the central scalar imaginary, fixed by the algebra rather than chosen; the amplitude is a complex scalar, and the relative phase is the argument of the off-diagonal element of $\tilde{\rho}$.
- A **home for the amplitude.** Each route amplitude is a central element of $\mathbb{C}_{\mathbb{B}}$, and the exponent $iS_j/\hbar$ lies in the material sector $\mathbb{M}_-$ along $ict$, as the path-integral article establishes.
- A **state geometry for the which-path degree of freedom.** The which-path state is an element $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ of $\mathbb{M}_+$; visibility and predictability are its equatorial and polar components; and the duality bound $V^2 + P^2 \le 1$ is exactly the trace-one-slice-of-the-cone condition of the Bloch-ball article, with equality on the zero-divisor cone.
- **Measurement and dephasing as algebraic operations.** The projective sandwich and the dephasing channel are the same operations the framework uses elsewhere; the double slit is an application, not a new mechanism.
- **The sector chain, restated.** A material-sector quantity (the action along a route in $\mathbb{M}_-$) is converted, through the central complex structure, into a central phase, and the state it produces, $\tilde{\rho} = \psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi)$, lies in the informational sector $\mathbb{M}_+$.

**What is interpretation.**

- The reading of the fringes as the projection of a rotating equatorial Bloch vector, and the reading of the arrangement as a conversion from the material to the informational sector, are structural and geometric readings. The algebra is consistent with them; it does not require them, and the standard amplitude language states the same results without them.

**What remains open.**

- **The action, the measure, and the space of paths.** The algebra supplies the phase and its imaginary unit; it does not supply $S$, $\mathcal{D}x$, or the (infinite-dimensional) domain of integration. This is the path-integral article's gap, unchanged.
- **The preferred direction and the selected outcome.** The framework represents the effect of a which-path coupling, not the coupling; and it yields the mixture, not the realised record. These are the decoherence article's and the measurement-problem article's gaps, unchanged.
- **Empirical content.** For a two-path system the framework reproduces the standard predictions exactly. It supplies no deviation here.

## Open Questions

1. **The measure and the action.** Can the algebra supply a distinguished measure or action for the paths, or is the double-slit pattern irreducibly an analytic construction laid on biquaternion-valued fibres? (Inherited from *The Path Integral in Biquaternionic Form*.)

2. **The which-path coupling.** The dephasing channel is the consequence of a system–environment coupling that the framework does not contain. Can a biquaternion field equation produce the coupling, and with it the pointer direction $\hat{\mu}$? (*Decoherence as Idempotent Projection* leaves this open.)

3. **Spin-dependent routes from first principles.** The spin-dependent fringe formula above is standard once the route spinors differ. Does the framework produce the spin-path coupling of its own accord — for instance through a non-central phase generated by a spinor field equation — or must the route spinors be put in by hand? (Compare *The Path Integral in Biquaternionic Form*, open question 2.)

4. **Does the cone reading add content?** The identity $V^2 + P^2 = 1 - 4\,\mathrm{Sc}(N(\tilde{\rho}))$ identifies the duality bound with the norm-form cone. Is that identification merely a restatement, or does the cone's Lorentzian geometry constrain interference in ways the standard inequality does not?

5. **More than two paths.** The which-path state of a two-slit experiment is a qubit, and its state space is the Bloch ball. A three-slit experiment is a three-state system, whose framework state space would require the tensor or module extension that *Quantum Mechanics in Biquaternionic Form* leaves open. Does the cone picture survive, and in what dimension?

6. **The local complex structure.** The series makes the complex structure local through $c = 1/\sqrt{\epsilon\mu}$, hence a medium-dependent wavelength $\lambda = c/\nu$; but the $i$ of the phase is a global central element. The relation between the local frame and the global phase is unresolved here, as in the Schrödinger and path-integral articles.

7. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard quantum mechanics. The double slit, on the evidence of this article, does not.

## Summary

The double-slit experiment in biquaternionic form is the statement that two route amplitudes, each a **central** complex phase $a_j e^{iS_j/\hbar}$, add, and that the intensity is their squared modulus:

$$
I = a_1^2 + a_2^2 + 2a_1a_2\cos\delta, \qquad \delta = \frac{S_1 - S_2}{\hbar}.
$$

A common phase shift is unobservable, so only the relative phase $\delta$ — a central element whose exponent lies in $\mathbb{M}_-$ along $ict$ — is read off. The standard geometry (nodes where $d\sin\theta = (m+\tfrac12)\lambda$, spacing $\lambda D/d$) is unchanged and is an input, not an output, of the algebra.

The which-path degree of freedom is a qubit with state $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r}) \in \mathbb{M}_+$. Its equatorial component is the coherence, and its length is the fringe **visibility** $V = |\mathbf{r}_\perp| = 2|\rho_{12}|$; its polar component is the path **predictability** $P = |r_\parallel| = |\rho_{11}-\rho_{22}|$. They satisfy

$$
V^2 + P^2 = |\mathbf{r}|^2 = 1 - 4\,\mathrm{Sc}\bigl(N(\tilde{\rho})\bigr) \le 1,
$$

with equality if and only if $\tilde{\rho}$ is pure — that is, if and only if the which-path state lies on the zero-divisor cone of $\mathbb{M}_+$. Partial fringe contrast and an interior (mixed) which-path state are the same fact. The normalised intensity is the equatorial component, $I/(|A_1|^2+|A_2|^2) = 1 + r_1$.

A which-path measurement, whether selective (projective) or non-selective (full dephasing along the path axis), annihilates the equatorial component and the fringes; partial dephasing scales the visibility by $1-p$. The preferred direction and the realised outcome are not supplied by the algebra.

The **spin-summed** two-slit intensity is **root-independent** for a beam with a common spin state: replacing the central $i$ by a fixed non-central root leaves it unchanged. Read without spin analysis, the double slit therefore does not witness the centrality of the phase; that centrality is required by the complex structure of the state module and by the unitarity of the state-vector equation, not by this pattern. The difference between the roots reappears under spin analysis in a basis not aligned with $\hat{\mu}$, and the total intensity differs when the two routes carry different spinors — when it acquires a spin overlap $\langle\hat{s}_1,\hat{s}_2\rangle$ that reduces the visibility (the spin-dependent double slit). The scalar case is the parallel-spinor case.

The algebra supplies the phase's imaginary unit, the sector of its exponent, a state geometry for the which-path qubit, and algebraic accounts of measurement and dephasing. It does not supply the action, the measure, the space of paths, the preferred direction, or the selection of an outcome; and it makes no prediction here that standard quantum mechanics does not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, central, $i^2 = -e_0$ |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center; home of the path phase |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde{K}_j = a_j e^{i\varphi_j} e_0$ | Route amplitude through slit $j$; central |
| $\varphi_j = S_j/\hbar$, $\delta = \varphi_1 - \varphi_2$ | Route phase; relative phase |
| $I = a_1^2 + a_2^2 + 2a_1a_2\cos\delta$ | Two-path intensity |
| $d, D, \lambda, k = 2\pi/\lambda$ | Slit separation, screen distance, wavelength, wavenumber |
| $\hat{\mu}$ | Unit pure real quaternion; path (pointer) axis |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ | Which-path idempotents |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ | Which-path state |
| $r_\parallel = \hat{\mu}\cdot\mathbf{r}$, $\mathbf{r}_\perp$ | Polar (predictability) and equatorial (coherence) parts |
| $V = |\mathbf{r}_\perp| = 2|\rho_{12}|$ | Fringe visibility |
| $P = |r_\parallel| = |\rho_{11}-\rho_{22}|$ | Path predictability |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form; $N(\tilde{\rho}) = \tfrac14(1-|\mathbf{r}|^2)e_0$ |
| $V^2 + P^2 = |\mathbf{r}|^2 \le 1$ | Visibility–predictability (duality) bound = cone condition |
| $\psi = \psi_1 + \psi_2 \in \mathbb{B}\tilde{P} \cong \mathbb{C}^2$ | Spinor-valued two-route amplitude |
| $\langle\hat{s}_1,\hat{s}_2\rangle = \mathrm{Tr}(\hat{s}_1^\dagger\hat{s}_2)$ | Module inner product; spin overlap |
| $e^{\hat{\mu}S/\hbar}$ | Non-central phase; a spin rotation |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $i\,\mathbb{M}_\pm = \mathbb{M}_\mp$ | The scalar imaginary exchanges the sectors |

## Further Reading

- *Introduction to the Biquaternion Universe* — the algebra, its two sectors, and the local complex structure.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the anti-Hermitian sector and the four-vectors.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian sector, its idempotents, and the trace formula.
- *Quantum Mechanics in Biquaternionic Form* — states, observables, the Born rule, and the measurement update.
- *The Schrödinger Equation in Biquaternionic Form* — the wave function as a spinor in a minimal left ideal, and the central imaginary as the complex structure.
- *The Path Integral in Biquaternionic Form* — the phase $e^{iS/\hbar}$ as a central unitary, its exponent in $\mathbb{M}_-$, and the measure/paths gap.
- *The Bloch Ball as the Trace-One Slice of the Future Light Cone* — the state space as a slice of the norm-form cone.
- *Decoherence as Idempotent Projection* — the dephasing channel and the destruction of coherence.
- *The Measurement Problem in Algebraic Form* — the mixture versus the realised outcome.
- *The Born Rule as a Trace Formula — Derivation and Comparison* — the trace formula and its comparison with the standard postulate.
- *Angular Momentum and Spin in Biquaternionic Form* — the spin degree of freedom used in the spinor-valued routes.
- *The Feynman Propagator in Biquaternionic Form* — the $i\epsilon$ direction shared with the phase exponent.
- *The Wick Rotation in the Biquaternion Universe* — the transfer $\mathbb{M}_- \to \mathbb{H}_{\mathbb{B}}$ that turns the phase into a decaying weight.
