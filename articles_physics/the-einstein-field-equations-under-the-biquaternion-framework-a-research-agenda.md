# __The Einstein Field Equations under the Biquaternion Framework — A Research Agenda__

## Introduction

This article is an agenda, not a result. It asks one question — does the biquaternion framework reproduce the Einstein field equations? — and its discipline is to answer with a separation rather than with a claim: what the framework's gravity articles have established, what they have not, and what object or computation would close each gap. An agenda that answered the central question without evidence would be worthless, so the central question is left open here, with the evidence that would decide it named explicitly.

The evidence base is the gravity series of companion articles. *Curved Spacetime and the Biquaternion Framework* established the kinematical route: the algebra can carry an arbitrary Lorentzian metric in a frame field $\tilde{E}_\mu \in \mathbb{M}_-$, and it supplies the pointwise $SL(2,\mathbb{C})$, its vector representation, and its Lie algebra — but no action, no field equation, and no representation of diffeomorphism invariance. *Linearized Gravity in Biquaternionic Form* linearised that route and established a definite dictionary: the metric perturbation $h_{\mu\nu}$ is carried by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$; the counting $16 = 10 + 6$ with a six-dimensional local-Lorentz kernel; the gauge transformation; the trace-reversal; and the reduction of the vacuum equation to $\Box\bar{h}_{\mu\nu} = 0$, hence to $\Box\bar{\delta\tilde{E}}_\mu = 0$ once the local Lorentz freedom is fixed. *Gravitational Waves in Biquaternionic Form* took the wave sector: the harmonic gauge and its residual freedom, the count $10 \to 6 \to 2$, the two transverse-traceless polarisations, and the quadrupole formula verified on the equal-mass circular binary. These two articles are the strongest evidence base in the series so far, and they are also the most easily misread. They are a linearised and wave-sector development, and nothing in them is a statement about the full non-linear equation.

The central question is therefore stated here in the form the evidence can support. Whether the framework reproduces the full non-linear Einstein equations, or only the linearised sector, is **open**; and the sharper finding recorded below is that even the linearised sector has been *carried* and *transcribed* rather than *derived*. The framework's independent content in the linearised and wave sectors is kinematic — the carrier, the counting, and the shape of the gauge structure. The dynamics was imported from general relativity. Consequently the non-linear question, which is a question about a dynamics, is not merely unanswered; it has not yet been reached.

The article is organised as follows. The next section fixes the three kinds of statement this agenda must keep apart, because the failure mode it exists to prevent is the upgrading of a transcribed result into a framework result. The two sections after it record, separately, what the curved-spacetime article and the linearised and wave articles actually established. The central section states what would settle the non-linear question, naming the object and the computation. The remaining open items follow, each with what would close it, and a short section orders those items by what could be achieved short of the full equation. The closing sections summarise.

**Conventions.** The notation of the read-list articles is inherited without change. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and scalar imaginary $i$ commuting with every $e_k$. The material and informational sectors are the anti-Hermitian and Hermitian subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ and $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace; $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the centre of the algebra. The material basis is $\varepsilon_0 = ie_0$, $\varepsilon_k = e_k$, with $\eta_{\mu\nu} = \langle\varepsilon_\mu,\varepsilon_\nu\rangle = \mathrm{diag}(-1,1,1,1)$ and bilinear form $\langle\tilde{Q},\tilde{P}\rangle = \mathrm{Sc}(\tilde{Q}\bar{\tilde{P}})$. Real coordinates are $x^\mu = (ct,x,y,z)$, so a four-vector of $\mathbb{M}_-$ is $\tilde{X} = X^\mu\varepsilon_\mu$ and $\partial_{ict} = -i\partial_0$; the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}}$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \eta^{\mu\nu}\partial_\mu\partial_\nu$. The trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. The frame field is $\tilde{E}_\mu \in \mathbb{M}_-$ with $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$, and the local-Lorentz generators are the rotations $J_k = e_k$ and the boosts $K_k = ie_k$, spanning the six-dimensional traceless subspace $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}} \subset \mathbb{B}$. Nothing inherited is renamed or rederived.

## How to Read the Evidence: Three Kinds of Statement

An agenda for this subject has to do one thing before anything else: keep apart the statements that look alike. Three kinds occur in the gravity articles, and they carry different weight.

| Kind | Examples | Status |
|---|---|---|
| **(i) Transcribed from general relativity** | the harmonic gauge $\partial^\lambda\bar{h}_{\lambda\nu} = 0$ and its residual freedom; the transverse-traceless plane wave and its two amplitudes; the wave equation $\Box\bar{h}_{\mu\nu} = -\tfrac{16\pi G}{c^4}T_{\mu\nu}$; the quadrupole amplitude and the power $P = \tfrac{G}{5c^5}\langle\dddot{Q}_{ij}\dddot{Q}_{ij}\rangle$ with its prefactor; the step $6 \to 2$ and the helicity count $\pm 2$ | Written in the framework's notation by the linearised and wave articles; not derived there |
| **(ii) Reproduced independently within the algebra** | the polar form $\langle\tilde{Q},\tilde{P}\rangle$ with Gram matrix $\mathrm{diag}(-1,1,1,1)$ and $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$; the carrier $h_{\mu\nu} = \langle\varepsilon_\mu,\delta\tilde{E}_\nu\rangle + \langle\delta\tilde{E}_\mu,\varepsilon_\nu\rangle$ and its surjectivity on symmetric perturbations; the splitting $16 = 10 + 6$ with the local-Lorentz kernel; the gauge image $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$; the trace-reversal frame shift; $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$ and the residual condition $\Box\tilde{\Xi} = 0$; the collapse $\sum_{\mu\nu} h_{\mu\nu}\,\varepsilon_\mu\bar{\varepsilon}_\nu = (\eta^{\mu\nu}h_{\mu\nu})e_0$; the bivector packaging of the curvature | Algebraic computations in the framework's own operations, recomputed in the gravity articles |
| **(iii) Framework-specific and still unverified** | the physical reality of $\mathbb{M}_+$ as an informational sector; the locality of the complex structure as a physical claim; that $\mathbb{B}$ is nature's algebra rather than a notation; any dynamics coupling the two sectors; that the frame route *is* general relativity | Hypotheses of the programme; no computation in the series establishes them |

The separation is the whole discipline of the article, because the failure mode it exists to prevent is the promotion of a row of (i) into a row of (ii). Two promotions are especially easy to make. The first is to read the verified count $10 \to 6 \to 2$ as an algebraic result of the framework: it is not. The wave article states plainly that the step $6 \to 2$ requires knowing which of the six harmonic-gauge components propagate, that this is the field equations and not the algebra, and that the framework has no natural handle on the count. The number two is inherited. The second is to read the quadrupole formula as a framework prediction: its prefactor is fixed by the transcribed coupling constant $8\pi G/c^4$ and by the transverse-traceless projection, neither of which the algebra supplies.

A promotion in the other direction matters too. A row of (ii) is a real computation and a real achievement — the dictionary is consistent, and a dictionary that got its signs, factors of two, and trace convention wrong would be wrong — but it is a fact about the algebra, not yet a fact about the world. The two statements "the algebra carries the metric perturbation in the frame perturbation" and "gravity is biquaternionic" are not the same statement, and the gap between them is what the rest of this agenda is about.

## What the Curved-Spacetime Article Established

The parent of the gravity series is a boundary article, and its boundary is the starting point of this agenda. Its findings, in the order in which the programme needs them, are these.

**Curvature cannot reside in the algebra.** The algebra $\mathbb{B}$ has no points, and its norm form has constant coefficients; nothing in it can be modulated by a field. Curvature can therefore be carried only by the map that attaches the algebra to spacetime. The article distinguishes two such maps and does not let them blur together: a **scale** on the imaginary time axis, which is the framework's own local complex structure, and a **frame** $d\tilde{X} = \tilde{E}_\mu dx^\mu$, which is the tetrad of the standard spinor formulation.

**The frame route carries any Lorentzian metric, and thereby tests nothing.** With $\tilde{E}_\mu \in \mathbb{M}_-$ and $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$, every Lorentzian metric is representable locally, because every Lorentzian metric has a local orthonormal frame and the bilinear form on $\mathbb{M}_-$ has the same signature. The local symmetry is a copy of $SL(2,\mathbb{C})$ at each point, acting by $\tilde{E}_\mu \mapsto \tilde{\Lambda}\tilde{E}_\mu\tilde{\Lambda}^\dagger$, and the sixteen frame functions modulo the six local rotor parameters reproduce the ten components of the metric. Two qualifications are part of the finding. First, *carrying is not deriving*: every metric, including every vacuum solution, is representable, so the framework excludes nothing and selects nothing. Second, this route uses from $\mathbb{B}$ only the underlying real four-dimensional space and its form of signature $(3,1)$, which any such space supplies equally; the quaternionic multiplication, the two-sector decomposition, and the complex structure do no work in writing $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$. A frame that is pure rotor gauge, $\tilde{E}_\mu = \tilde{\Lambda}(x)\,\epsilon_\mu\,\tilde{\Lambda}(x)^\dagger$ for a fixed basis, is flat; curvature is exactly the non-gauge part of the frame.

**The connection and its curvature fit inside the algebra, and the infinitesimal action is two-sided.** The Lie algebra of the rotor group is the six-dimensional traceless subspace $\mathrm{span}_{\mathbb{R}}\{e_k, ie_k\}$, so a connection one-form $\tilde{\Gamma}_\mu$ and its curvature can be carried as algebra-valued objects. The article records a trap: because the group acts by $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, the infinitesimal action is $G\tilde{X} + \tilde{X}G^\dagger$, which differs from the commutator $[G,\tilde{X}]$ exactly for the boost generators, where the Lorentzian content lives. The covariant derivative must therefore be written in the two-sided form $D_\mu\tilde{X} = \partial_\mu\tilde{X} + \tilde{\Gamma}_\mu\tilde{X} + \tilde{X}\tilde{\Gamma}_\mu^\dagger$. A rotor-carried frame arrives with a natural $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$-valued logarithmic derivative, but it is pure gauge and its curvature vanishes. Metric compatibility and vanishing torsion are conditions the algebra does not select.

**The framework's own local device does not reach general relativity.** The local scale factor $c = 1/\sqrt{\epsilon\mu}$ of the imaginary time axis admits two inequivalent readings. Read as a map of points, $\tilde{X} = i\,c(\mathbf{x})\,t\,e_0 + \mathbf{x}$, it produces a nondegenerate metric that is identically flat, because it is a reparametrisation of the flat form of $\mathbb{M}_-$. Read as a derivative rule, $\partial_{ict} = -(i/c)\partial_t$ with $c$ held fixed in the differential, it produces $g_{\mu\nu} = \mathrm{diag}(-c^2,1,1,1)$, genuinely curved but confined to a class of one free function, no shift, and flat spatial slices. Within that class the article proves that Ricci-flatness forces the free function to be affine in the spatial coordinates, and every such metric is flat. The class therefore contains no non-flat vacuum geometry: no Weyl curvature, no gravitational waves, no black-hole exterior. The framework's prose does not choose between the two readings, and the choice is left open; the class result is independent of the curvature sign convention in which the components are displayed.

**The informational sector has no curved-space treatment, for a structural reason.** The elements of $\mathbb{M}_+$ become pointwise operator fields without difficulty, but the trace in the formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is a fibre trace at a point. A field-theoretic trace is an integral over the manifold, with a measure that itself depends on the metric, and the framework's trace cannot play that role. The pointwise expectation value survives; the global one has nowhere to live.

**Nothing determines anything.** There is no action, no field equation for $\tilde{E}_\mu$ or $\tilde{\Gamma}_\mu$, no Einstein equation, no coupling to sources, and no representation of $\mathrm{Diff}(M)$. The bookkeeping makes the last gap vivid: the gravitating objects — the metric and the energy–momentum tensor — are symmetric rank-two objects in $(1,1)\oplus(0,0)$, of dimension ten, while the framework's kinematical fields are four-vectors in $(\tfrac12,\tfrac12)$, of dimension four.

The article's own summary of the boundary is the correct one to carry forward: the framework contains the **kinematical fibre** of tetrad gravity — a pointwise Lorentzian vector space, its Lorentz group, the vector representation, and a Lie-algebra-valued connection — and none of its dynamics.

## What the Linearised and Wave-Sector Articles Established

The linearised article and the wave article take the frame route of the parent and develop it as far as the linear theory reaches. Their results are precise, and it is worth stating them at the precision at which they were established.

### The Frame Perturbation, the Counting, and the Gauge Structure

The metric perturbation is carried by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$ through

$$
h_{\mu\nu} = \langle\varepsilon_\mu, \delta\tilde{E}_\nu\rangle + \langle\delta\tilde{E}_\mu, \varepsilon_\nu\rangle .
$$

The map is symmetric in $\mu\nu$ automatically and **surjective**: the choice $\delta\tilde{E}_\mu = \tfrac12 h_{\mu\lambda}\varepsilon^\lambda$ reproduces any symmetric $h_{\mu\nu}$, a statement the article checks on randomly generated perturbations rather than only on the construction that suggests it. The sixteen frame components split as $16 = 10 + 6$, the six-dimensional kernel being the infinitesimal local Lorentz transformations generated by the complex pure vectors $\tilde{G} \in \mathrm{span}_{\mathbb{R}}\{e_k, ie_k\}$, which leave $h_{\mu\nu}$ exactly invariant. The restriction to the unit-norm condition matters and was checked: a generator with a real scalar $e_0$ component produces a nonzero shift of $h$.

The linearised gauge transformation is written

$$
\delta\tilde{E}_\mu \;\longmapsto\; \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi},
\qquad \tilde{\Xi} \in \mathbb{M}_-,
$$

and it reproduces $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu$ with $\xi_\nu = \langle\tilde{\Xi},\varepsilon_\nu\rangle$. Its *shape* is the electromagnetic one — the exterior derivative of a gauge parameter — but its *origin* is a diffeomorphism, for which the algebra has no representation, and the article says so without qualification. The trace-reversal has a clean frame image,

$$
\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac14 h\,\varepsilon_\mu,
\qquad h = 2\langle\varepsilon^\nu,\delta\tilde{E}_\nu\rangle,
$$

which carries $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac12\eta_{\mu\nu}h$. In harmonic gauge the vacuum equation reduces to $\Box\bar{h}_{\mu\nu} = 0$, hence to $\Box\bar{\delta\tilde{E}}_\mu = 0$ once the local Lorentz freedom is fixed. The linearised Riemann tensor is gauge invariant, and it is carried index by index as a bivector-valued two-form whose values lie in the six-dimensional complex pure-vector subspace.

There is one sharp negative finding in this article, and it is central to the agenda. The graviton is **not** a material biquaternion. It is not an element of $\mathbb{M}_-$, it is not a single element of $\mathbb{B}$ at all — eight real dimensions cannot hold ten components — and the natural single-biquaternion packaging of a symmetric rank-two object,

$$
\tilde{H} = \sum_{\mu,\nu} h_{\mu\nu}\,\varepsilon_\mu\bar{\varepsilon}_\nu,
$$

collapses to the Lorentzian trace,

$$
\tilde{H} = (\eta^{\mu\nu}h_{\mu\nu})\,e_0 = h\,e_0 .
$$

The traceless part of $h_{\mu\nu}$ — nine of the ten components, and the whole of the transverse-traceless content that carries the two polarisations — maps to zero. The correct carrier is the $\mathbb{M}_-$-valued one-form $\delta\tilde{E}_\mu$, not an algebra element.

### The Wave Sector and the Quadrupole Formula

The wave article begins from the standard theory, recomputes it, and then asks what the framework contains.

The harmonic condition $\partial^\lambda\bar{h}_{\lambda\nu} = 0$ is four conditions on ten components, and it can always be imposed. It does **not** exhaust the gauge freedom: it is preserved by exactly those transformations with $\Box\xi_\nu = 0$, a statement the article verifies on a general smooth gauge parameter and not only on a plane wave. In the framework's variables the residual freedom is the kernel of $\Box$ acting on $\mathbb{M}_-$,

$$
\Box\tilde{\Xi} = 0 ,
$$

which is a genuine, if modest, piece of framework content: the residual gauge condition is built from the algebra's own operator and the material sector. The physical count is then $10 \to 6 \to 2$. Ten components of the symmetric perturbation; four harmonic conditions leaving six; and, inside those six, a four-dimensional image of the residual gauge freedom whose complement is the two-dimensional transverse-traceless subspace. The split was verified by a rank computation, and the final two were confirmed independently by the transverse-traceless tensor count and by the helicity count of a massless spin-two field.

The two polarisations were checked on an explicit plane-wave ansatz. For each of the plus amplitude $A_{11} = -A_{22}$ and the cross amplitude $A_{12} = A_{21}$, the wave is transverse, $k^\mu A_{\mu\nu} = 0$, and traceless, $\eta^{\mu\nu}A_{\mu\nu} = 0$; the Ricci tensor vanishes, $R_{\mu\nu} = 0$, and the Riemann tensor does not, so each carries physical curvature and neither is pure gauge. The gauge-invariant content is the Weyl part of the curvature.

The quadrupole formula was verified by matching it to an independent result. For the equal-mass circular binary, the traceless quadrupole moment's third derivatives give $\dddot{Q}_{ij}\dddot{Q}_{ij} = 128\,m^2R^4\omega^6$, and with Kepler's law and $R = d/2$ the power

$$
P = \frac{G}{5c^5}\left\langle \dddot{Q}_{ij}\,\dddot{Q}_{ij} \right\rangle
$$

equals $\tfrac{64}{5}\tfrac{G^4}{c^5}\tfrac{m^5}{d^5}$, in agreement with the standard equal-mass binary power $\tfrac{32}{5}\tfrac{G^4}{c^5}\tfrac{(m_1m_2)^2(m_1+m_2)}{d^5}$. The absence of monopole and dipole radiation was traced to the conservation of mass–energy and momentum.

### What Those Articles Did Not Establish

The negatives are as precise as the positives, and for this agenda they are more important.

- **The dynamics is transcribed, not derived.** The operator $\Box$ is the framework's own, but the equation $\Box\bar{h}_{\mu\nu} = 0$ and its sourced form are the standard linearised equations, written in the framework's notation. No action is supplied, and no principle selects the frame.
- **The step $6 \to 2$ is not a framework result.** It requires knowing which of the six harmonic-gauge components propagate; that is the field equations, not the algebra. The framework has no analogue of the little group of a null vector and no representation of helicity, so the number two is inherited.
- **The polarisation amplitudes and the quadrupole moment are exactly what the natural packaging annihilates.** Both are symmetric and traceless, and for a traceless symmetric object the packaging collapses to zero: $\sum_{ij} A_{ij}\varepsilon_i\bar{\varepsilon}_j = 0$ and $\sum_{ij} Q_{ij}\varepsilon_i\bar{\varepsilon}_j = 0$.
- **The coupling constant and the prefactor are not fixed.** The $8\pi G/c^4$ of the field equation and the $G/5c^5$ of the power are imported from the transcribed theory.

Two no-upgrade statements belong here, stated as plainly as the articles state them. First, the quadrupole formula is a weak-field, slow-motion, far-zone result, the leading term of a multipole expansion; it is not an exact statement, and it is not evidence about the non-linear equation. Second, the count $10 \to 6 \to 2$ is a statement about the linearised potential at a point; it carries no information about the non-linear constraint structure of general relativity. Neither result may be promoted.

## The Central Open Question: The Full Non-Linear Equation

The framework's gravity articles reach the linearised sector and no further. The question this agenda puts at the centre is therefore:

> **Does the biquaternion framework reproduce the full non-linear Einstein equations, or only the linearised sector?**

The honest answer, on the evidence of the three articles, is that the question is **open**, and that it is open in a stronger sense than "the proof has not been written". The framework has not derived the linearised equation either: it has transcribed that equation and established that its kinematics can be written in the algebra. A derivation of the non-linear equation cannot be missing when the derivation of the linear one is missing too. What the articles supply is a target — the correct linearisation of general relativity, in the framework's notation — and a set of kinematic identities that any candidate dynamics would have to reproduce.

### Why the Linearised Results Do Not Settle It

Three reasons, each of which is a statement about what linearisation discards.

1. **A linear equation does not determine a non-linear completion.** Infinitely many non-linear theories share a given linearisation; reproducing $\Box\bar{h}_{\mu\nu} = 0$ at first order constrains a candidate action but does not select one. The self-interaction terms of the Einstein–Hilbert action, the constraint structure, and the way the theory closes on itself are exactly what the first-order truncation removes.
2. **The carrier is linear by construction.** The dictionary $h_{\mu\nu} = \langle\varepsilon_\mu,\delta\tilde{E}_\nu\rangle + \langle\delta\tilde{E}_\mu,\varepsilon_\nu\rangle$ is the first-order expansion of $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$ about the flat basis. Its non-linear completion, $\langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$ for a general frame, is available and carries any metric; but carrying a metric is not solving its field equation, and the parent article is explicit that the frame is arbitrary and selected by nothing.
3. **The wave-sector count is a property of the linear potential.** The reduction $10 \to 6 \to 2$, the transverse-traceless amplitudes, and the quadrupole formula belong to the weak-field, slow-motion expansion. They are constancy checks on the linear dictionary and on the imported dynamics; they say nothing about the non-linear constraint structure, the initial-value problem, or the non-perturbative solutions.

To these a fourth, methodological reason should be added. The framework's independent results are kinematic: the carrier, the counting $16 = 10 + 6$, the gauge image, the trace-reversal, the residual condition $\Box\tilde{\Xi} = 0$. Kinematics is shared by every theory with the same field content; it cannot by itself distinguish the Einstein equations from any other second-order equation for the same fields. The distinguished content of general relativity is not its field content but its dynamics.

### What Would Settle It: A Biquaternion Action for the Frame and the Connection

The central question is settled by producing, or ruling out, a specific object. The object is a **biquaternion-valued action functional of the frame and the connection**,

$$
S[\tilde{E}_\mu, \tilde{\Gamma}_\mu] = \int \mathcal{L}\left(\tilde{E}_\mu, \tilde{\Gamma}_\mu, \partial_\mu\tilde{E}_\nu, \partial_\mu\tilde{\Gamma}_\nu\right) d^4x,
$$

in which $\tilde{E}_\mu \in \mathbb{M}_-$ is the frame field, $\tilde{\Gamma}_\mu$ is a connection valued in the six-dimensional Lie subspace $\mathrm{span}_{\mathbb{R}}\{e_k, ie_k\}$, and the Lagrangian density $\mathcal{L}$ is built from the algebra's own operations — the biquaternion product, the quaternion conjugate, the scalar part $\mathrm{Sc}$, and the biquaternion derivative $\tilde{\nabla}$ — together with the curvature two-form of $\tilde{\Gamma}_\mu$. The pair $(\tilde{E}_\mu, \tilde{\Gamma}_\mu)$ is the natural choice because it is exactly what the algebra can carry: the frame as an $\mathbb{M}_-$-valued one-form, the connection as a Lie-subspace-valued one-form, and their two-sided covariant derivative $D_\mu\tilde{X} = \partial_\mu\tilde{X} + \tilde{\Gamma}_\mu\tilde{X} + \tilde{X}\tilde{\Gamma}_\mu^\dagger$ as the derivative that respects the algebra's action. This is the Palatini structure written in the framework's notation, and the framework's own objects are already in place for it; what is missing is the density.

The computation that would settle the question is then the **variation**:

$$
\frac{\delta S}{\delta\tilde{E}_\mu} = 0, \qquad \frac{\delta S}{\delta\tilde{\Gamma}_\mu} = 0,
$$

followed by two checks and one decisive question.

- **Check (a), the linearisation.** Expand the field equations about the flat basis and verify that they reduce to the linearised Einstein equation in the form the wave articles established, $\Box\bar{\delta\tilde{E}}_\mu = 0$ in vacuum (with the local Lorentz freedom fixed) and $\Box\bar{h}_{\mu\nu} = -\tfrac{16\pi G}{c^4}T_{\mu\nu}$ with a source. This is the weakest of the checks and would already be progress.
- **Check (b), the non-linear identity.** Verify that the exact field equation coincides with the Einstein tensor, $G_{\mu\nu} = \tfrac{8\pi G}{c^4}T_{\mu\nu}$, when written on the frame — that is, that the variation reproduces not merely an equation of the right index structure and order but the specific tensor $R_{\mu\nu} - \tfrac12 g_{\mu\nu}R$.
- **The decisive question.** Does the variation produce the Einstein tensor off-shell, or only a symmetric, divergence-free rank-two tensor built from the frame and its first and second derivatives? There are many such tensors, and the constraint structure of general relativity lives in which one is selected. If the action can be chosen but not *forced* — if an arbitrary coefficient is available at second order — then the framework has not reproduced the Einstein equations but has parametrised a class of theories containing them.

Two further avenues belong to this item and would also settle it, in weaker senses.

**A no-go.** The central question would also be closed, in the negative, by a proof that no local functional of $\tilde{E}_\mu$ and $\tilde{\Gamma}_\mu$, built from the algebra's operations and invariant under the local rotor action, has the Einstein tensor as its Euler–Lagrange expression — or, more strongly, that no such functional is invariant under diffeomorphisms at all. A no-go of either kind would be a result about the framework as valuable as a derivation.

**A partial derivation.** An action whose *linearised* variation is the linearised Einstein equation would move the linearised sector from kind (i) to kind (ii) in the classification above. It is a necessary first step toward the non-linear question and is strictly weaker than it, but it is the smallest computation that would change the status of the framework's best-developed sector.

## The Remaining Open Items, and What Would Settle Them

Each item below is stated with what is known, what is open, and the object or computation that would close it. The items are ordered from the dynamics outward to the parts of the programme the algebra cannot currently see.

**An action for the frame.** *Known:* no action, no field equation, and no Einstein equation is constructed in the three articles that make up the gravity series; the frame is selected by nothing. *Open:* whether an algebra-built action exists, and whether the Einstein tensor or a larger class of tensors results. *Would settle it:* the object and computation of the previous section, with checks (a) and (b), or a no-go.

**A representation of diffeomorphism invariance.** *Known:* the algebra carries the *form* of the linearised diffeomorphism, $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$, but not its *origin*; $\mathbb{B}$ has no representation of $\mathrm{Diff}(M)$, and no element of it corresponds to a coordinate change on the base. *Open:* whether the soldering of the frame to the manifold can induce the diffeomorphism algebra from the local rotor gauge plus the frame's own one-form index, or whether diffeomorphism invariance must be posited alongside the action. *Would settle it:* a construction, in the algebra's operations, of a representation of $\mathrm{Diff}(M)$ on the space of frame fields — equivalently, a biquaternion version of the gauged-translation or Poincaré structure in which the soldering form closes the algebra — or a proof that none exists. The familiar remark that tetrad gravity's local translations are not gauge symmetries of the action but of the frame's soldering is the standard setting to test the algebra against.

**The coupling constant and the matter coupling.** *Known:* the source term carries $8\pi G/c^4$, and the quadrupole power carries $G/5c^5$; both are transcribed, and the gravitating source $T_{\mu\nu}$ is a symmetric rank-two object the framework does not carry as a single algebra element. *Open:* whether any normalisation intrinsic to the algebra — a preferred trace identity, a bilinear, or an inner product on the Lie subspace — fixes the coupling when the action is written, and whether the question is even well posed before an action exists. *Would settle it:* the object is the coefficient of the Einstein–Hilbert-like term in $\mathcal{L}$; the computation is to match the normalisation of the candidate action to the linearised source term, or to show that the algebra admits a one-parameter family of normalisations and therefore fixes nothing.

**A faithful carrier of the traceless rank-two content.** *Known:* no single biquaternion carries a symmetric rank-two object of ten components; the natural packaging collapses to the trace; the transverse-traceless amplitudes and the traceless quadrupole moment are annihilated (kind (ii) computations, recomputed for this agenda). *Open:* whether a bilinear construction — in the manner in which the electromagnetic energy–momentum tensor is carried not by one biquaternion but by a product of two — carries the traceless part faithfully, and with what transformation law under $SL(2,\mathbb{C})$. *Would settle it:* the object is an $SL(2,\mathbb{C})$-equivariant bilinear map into the symmetric traceless rank-two representation $(1,1)$, or a two-spinor construction $\phi_{ab}\bar{\phi}_{a'b'}$ whose symmetric traceless part is $Q_{ij}$; the computation is to exhibit the map and check its equivariance and its faithfulness on the traceless part. A positive answer would give the framework a place to stand in the generation problem; a negative answer would explain why the quadrupole formula resists transcription into an algebra element.

**The polarisation count and helicity $\pm 2$.** *Known:* the count $10 \to 6 \to 2$ was verified as a standard computation, and the framework has no natural handle on the step $6 \to 2$; the number is inherited. *Open:* whether the Lorentz-group structure the framework does contain — the stabiliser of a null wave vector $k^\mu$ in $SL(2,\mathbb{C})$, and the representations the algebra already carries — suffices to produce the two helicities algebraically. *Would settle it:* the object is the little group of a null vector $\tilde{K} \in \mathbb{M}_-$ and its representations; the computation is to decompose the six harmonic-gauge components, or the ten-component perturbation, under that stabiliser and check whether a two-dimensional helicity doublet appears or whether the algebra sees only their sum. If it appears, the count becomes a framework result rather than a transcription; if it does not, the failure should be stated as sharply as the absence.

**Weyl curvature, self-dual bivectors, and the Newman–Penrose scalars.** *Known:* the gauge-invariant content of a vacuum wave is its Weyl part; the linearised curvature is carried as a bivector-valued two-form whose values lie in the six-dimensional complex pure-vector subspace (kind (ii), recomputed here). *Open:* whether the decomposition into $\mathbb{M}_+$ and $\mathbb{M}_-$ organises the self-dual and anti-self-dual parts of the curvature bivectors, and whether the five Newman–Penrose scalars $\Psi_0,\dots,\Psi_4$ can be written as components of algebra elements. *Would settle it:* the object is the split of the complexified bivector space into self-dual and anti-self-dual three-dimensional pieces and its relation to the six real dimensions of the Lie subspace; the computation is to write the five scalars in the algebra's notation and check the algebraic identities they must satisfy. The biquaternion–twistor dictionary is the natural place to look.

**The local-scale route and its metric class.** *Known:* read as a map of points the local scale factor produces no curvature at all; read as a derivative rule it produces a one-function class in which Ricci-flatness forces flatness, so it carries no non-flat vacuum solution. *Open:* whether some other reading of the local complex structure produces a wider class — one in which the spatial geometry or the shift is also allowed to vary — and whether that class contains non-flat Ricci-flat members. *Would settle it:* the object is the most general metric expressible through the local complex structure; the computation is to exhibit it, search its Ricci-flat solutions, and either find a non-flat one or prove that every member built from a single scale function is flat.

**The informational sector on a curved background.** *Known:* the two-sector decomposition survives pointwise, but the trace formula is a fibre trace with no measure, so the pointwise expectation value has no global analogue and no curved Born rule has been constructed. *Open:* whether a covariant measure, or a density valued in the algebra, makes the trace integrable and diffeomorphism invariant. *Would settle it:* the object is a volume element, or a trace functional on $\mathbb{M}_+$-valued fields, built from the frame; the computation is to check its invariance under both the local rotor action and a coordinate change, and to recover the flat trace formula in the flat limit.

**Global and topological structure.** *Known:* the algebra is a point, so it cannot see causal structure, horizons, singularities, or topology; even the existence of spinor fields on a manifold is a topological condition — the vanishing of the second Stiefel–Whitney class — that the algebra cannot detect, and the globalisation of the spinor module to a bundle is recorded open elsewhere in the series. *Open:* everything on this list. *Would settle it:* the object is the frame bundle and its spin structure, with the associated spinor bundle; the computation is a bundle-theoretic construction of the biquaternion spinor module over a curved background, with its existence condition stated. Horizon and singularity questions would then require global data the algebra still does not carry, and the first honest step is to say which of them are even formulable in the framework.

**The source, back-reaction, and the Isaacson stress–energy tensor.** *Known:* the radiating source $T_{\mu\nu}$ and the quadrupole moment $Q_{ij}$ are symmetric rank-two objects; the framework annihilates the traceless part of the latter and collapses the former to its trace; the radiated power is quadratic in the wave amplitude. *Open:* whether the algebra supplies the Isaacson stress–energy tensor — the quadratic object whose flux gives the radiated power — as naturally as it supplies the electromagnetic energy–momentum tensor, or whether the transverse-traceless projection again obstructs the packaging. *Would settle it:* the object is the bilinear map from the transverse-traceless frame perturbation to a symmetric rank-two tensor; the computation is to check that its averaged flux reproduces $\tfrac{G}{5c^5}\langle\dddot{Q}_{ij}\dddot{Q}_{ij}\rangle$ with the correct sign and normalisation.

**Empirical content.** *Known:* nothing in the linearised or wave sector predicts a deviation from standard general relativity; the framework is, on every domain the series has developed, a faithful transcription and therefore empirically equivalent. *Open:* whether any derivation produces a framework-specific quantity. *Would settle it:* this item is treated in full in its own agenda article, *The Empirical Status of the Biquaternion Framework*, and is not duplicated here; the specifically gravitational part of it is the action of the first item, since a dynamics is the only thing that could make the framework's gravity distinct.

## Progress Short of the Full Equation

The central question is the last to be answered, not the first, and the items above admit an ordering by what is reachable now. The following sequence is this agenda's judgement of that order, with each step's status recorded so that a partial advance can be recognised for what it is.

1. **Derive the linearised equation from an action.** The smallest computation that would change the status of the framework's best-developed sector. It requires only an action whose first variation reproduces $\Box\bar{h}_{\mu\nu} = 0$ and its source; it does not require the non-linear identity. A positive result moves the linearised sector from transcribed to reproduced.
2. **Derive the polarisation count from the little group.** An algebraic computation using structure the framework already contains — the stabiliser of a null $\tilde{K} \in \mathbb{M}_-$ — and one that would turn the number two from an inherited fact into a framework result. It is independent of the action and can be attempted immediately.
3. **Construct a faithful carrier for the traceless rank-two content.** The bilinear map into the symmetric traceless representation, which would give the quadrupole moment and the transverse-traceless amplitudes a home in the algebra. Also independent of the action.
4. **Give the informational trace a covariant measure.** The step that would let the two-sector structure mean something on a curved background, and the precondition for any claim that $\mathbb{M}_+$ is more than a pointwise operator space.
5. **Produce an action with the Einstein tensor as its variation.** The central question, in the constructive sense, with checks (a) and (b).
6. **Or prove the no-go.** The central question, in the negative sense: no algebra-built functional of the frame and connection yields the Einstein equations, or none is diffeomorphism invariant.

Two general disciplines apply to every item. First, each candidate result should be recomputed on a case chosen independently of the one that suggested it — a random perturbation rather than a symmetric ansatz, a second metric rather than the metric that prompted the formula. Second, a result in the linearised or wave sector must not be reported as a statement about the full equation: the distinction between the two is the standing content of this agenda, and the easiest way to lose it is to write one sentence too many.

## Summary

This agenda asked whether the biquaternion framework reproduces the Einstein field equations, and it has recorded what the gravity articles did and did not establish.

The framework carries an arbitrary Lorentzian metric in a frame field, and it carries the local $SL(2,\mathbb{C})$, its vector representation, its six-dimensional Lie algebra, and a Lie-algebra-valued connection. That is the kinematical fibre of tetrad gravity, and it is all the framework's own local-scale device does not supply: read as a map of points the local complex structure gives a flat metric, and read as a derivative rule it gives a one-function class with no non-flat vacuum member.

In the linearised sector, the metric perturbation is carried surjectively by an $\mathbb{M}_-$-valued frame perturbation; the sixteen frame components split as $16 = 10 + 6$ with a six-dimensional local-Lorentz kernel; the gauge transformation, the trace-reversal, and the residual condition $\Box\tilde{\Xi} = 0$ are written in the algebra's operations; and the natural single-biquaternion packaging collapses to the trace and annihilates exactly the transverse-traceless content. In the wave sector, the count $10 \to 6 \to 2$ and the quadrupole formula were verified, and the articles state that the step $6 \to 2$, the polarisations, and the coupling prefactor are transcribed from general relativity rather than produced by the algebra.

The central question — does the framework reproduce the full non-linear Einstein equations, or only the linearised sector? — is **open**, and open more strongly than a missing proof: even the linearised equation has been transcribed rather than derived. The object that would settle it is a biquaternion-valued action functional of the frame and the connection, built from the algebra's own operations and the curvature two-form; the computation is its variation, checked at linear order against the linearised Einstein equation and at all orders against the Einstein tensor, with the decisive question being whether the Einstein tensor is forced or merely one choice in a family. A no-go would settle the question as completely in the negative. The remaining open items — diffeomorphism invariance, the coupling constant, the traceless carrier, the little-group count, the Weyl and Newman–Penrose encoding, the metric class, the informational measure, global structure, back-reaction, and empirical content — are each stated above with the object that would close them.

The honest position of the framework's gravity programme is therefore this. It contains the language of general relativity's kinematics and a faithful linearised dictionary, and it contains none of general relativity's dynamics. Whether the language can be made to carry the dynamics is the question, and it is a question that has not yet been asked in a form that could be answered.

## Summary of Notation

| Symbol | Meaning | Introduced or inherited |
|---|---|---|
| $\mathbb{B}$ | $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the biquaternion algebra | inherited |
| $e_0,e_1,e_2,e_3$ | quaternion basis, $e_k^2 = -e_0$, $e_je_k = -\delta_{jk}e_0 + \epsilon_{jkm}e_m$ | inherited |
| $i$ | scalar imaginary, commuting with every $e_k$ | inherited |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | material (anti-Hermitian) and informational (Hermitian) subspaces, $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ | inherited |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | real-quaternion subspace; centre $\mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | inherited |
| $\varepsilon_\mu$ | material basis $\varepsilon_0 = ie_0$, $\varepsilon_k = e_k$ | inherited |
| $\langle\tilde{Q},\tilde{P}\rangle$ | bilinear form $\mathrm{Sc}(\tilde{Q}\bar{\tilde{P}})$, $\langle\varepsilon_\mu,\varepsilon_\nu\rangle = \eta_{\mu\nu} = \mathrm{diag}(-1,1,1,1)$ | inherited |
| $\tilde{\nabla}$, $\bar{\tilde{\nabla}}$, $\Box$ | biquaternionic gradient, its conjugate, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \eta^{\mu\nu}\partial_\mu\partial_\nu$ | inherited |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | trace formula | inherited |
| $J_k = e_k$, $K_k = ie_k$ | local-Lorentz generators, spanning the six-dimensional Lie subspace | inherited |
| $\tilde{E}_\mu$, $\tilde{\Gamma}_\mu$ | frame field in $\mathbb{M}_-$; Lie-subspace-valued connection one-form | inherited from the curved-spacetime and linearised articles |
| $g_{\mu\nu} = \langle\tilde{E}_\mu,\tilde{E}_\nu\rangle$ | metric carried by the frame | inherited |
| $\delta\tilde{E}_\mu$, $\bar{\delta\tilde{E}}_\mu$ | frame perturbation and its trace-reversed form | inherited |
| $h_{\mu\nu}$, $h$, $\bar{h}_{\mu\nu}$ | metric perturbation, its Lorentzian trace, and its trace-reversal | inherited |
| $\tilde{\Xi}$, $\xi_\nu = \langle\tilde{\Xi},\varepsilon_\nu\rangle$ | gauge parameter in $\mathbb{M}_-$ and its four-vector image | inherited |
| $A_{ij}$, $Q_{ij}$, $I_{ij}$, $k^\mu$ | plane-wave amplitudes; quadrupole, moment, and null wave vector | inherited |
| $S[\tilde{E}_\mu,\tilde{\Gamma}_\mu]$, $\mathcal{L}$ | biquaternion-valued action and Lagrangian density | new in this article |
| $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ | the six-dimensional traceless real Lie subspace $\mathrm{span}_{\mathbb{R}}\{e_k, ie_k\}$ | naming of an inherited object |

## Further Reading

- *Introduction to the Biquaternion Universe* — the algebra, its conjugations, and the two-sector decomposition.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the material sector, the four-vectors, and the bilinear form.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the informational sector and the trace formula.
- *Curved Spacetime and the Biquaternion Framework* — the frame route, the local-scale route, the connection, and the boundary of the kinematics.
- *Linearized Gravity in Biquaternionic Form* — the carrier, the counting $16 = 10 + 6$, the gauge structure, and the collapse of the single-biquaternion packaging.
- *Gravitational Waves in Biquaternionic Form* — the harmonic gauge, the count $10 \to 6 \to 2$, the polarisations, and the quadrupole formula.
- *The Gauge Principle in Biquaternionic Form* and *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the abelian gauge pattern the linearised diffeomorphism imitates, and the connection formalism.
- *Exercise: The Electromagnetic Energy–Momentum Tensor* and *The Field-Strength Biquaternion and Its Invariants* — the bilinear construction of a rank-two tensor, relevant to the traceless-carrier item.
- *Biquaternion Representation Theory* — the representation theory behind the $(1,1)\oplus(0,0)$ and $(\tfrac12,\tfrac12)$ bookkeeping and the little-group item.
- *Why Complexify Spacetime?* and *Electromagnetism in Media — The Local Complex Structure at Work* — the local complex structure and its physical readings.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and *The Lorentz Group in Biquaternionic Form — Structure and Representations* — the spinor and Lorentz structures the agenda's carrier and helicity items rest on.
- *Twistor Theory and Biquaternions* — the bivector and self-duality dictionary relevant to the Weyl-curvature item.
- *The Empirical Status of the Biquaternion Framework* — the companion agenda on framework-specific predictions, not duplicated here.
