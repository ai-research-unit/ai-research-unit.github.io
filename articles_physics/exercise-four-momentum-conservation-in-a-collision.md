# __Exercise: Four-Momentum Conservation in a Collision__

## Introduction

This is one of the exercises in the relativity series. It is a set of worked problems in four-momentum conservation for a collision, using the framework and the notation of the companion article *Relativistic Mechanics in Biquaternionic Form*. That article is the parent of this exercise: it defines the four-velocity, the four-momentum, and the mass-shell relation, and what follows applies them. The frame transformations used below are those of *The Lorentz Transformation as a Biquaternionic Rotation*, and the frame-and-translation structure is that of *The Poincaré Group and the Biquaternion Frame*. Nothing new is introduced; every result below is obtained from the tools already defined in those articles.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and the scalar imaginary $i$ with $i^2 = -1$, commuting with every $e_k$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part, the material sector) and the Hermitian subspace $\mathbb{M}_+$ (real scalar part, imaginary vector part, the informational sector), with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$; the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$; and the complex scalar subspace $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$, the center of the algebra. The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, and the invariant pairing on $\mathbb{M}_-$,
$$
\langle \tilde{A}, \tilde{B}\rangle = \mathrm{Sc}\!\left(\tilde{A}\bar{\tilde{B}}\right),
$$
which is symmetric, real-valued on $\mathbb{M}_-$, and reproduces the norm form on the diagonal. The four-position $\tilde{X} = ict\,e_0 + \mathbf{x}$, the four-velocity $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ with $N(\tilde{U}) = -c^2$, and the four-momentum
$$
\tilde{P} = m\tilde{U} = i\frac{E}{c}\,e_0 + \mathbf{p},
\qquad N(\tilde{P}) = -m^2c^2,
\qquad E = \gamma mc^2,\quad \mathbf{p} = \gamma m\mathbf{v}.
$$
The boost biquaternion $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ with $\tanh\psi = u/c$ and $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$, and the rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$; the Poincaré pair $(\tilde{\Lambda},\tilde{a})$ acting by $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger+\tilde{a}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

**What is to be shown.** The problems are: (1) the conservation law as a single biquaternion equation, its equivalence to energy and three-momentum conservation, and its frame covariance; (2) the invariant mass and the Mandelstam invariants of a $2\to2$ collision; (3) the centre-of-momentum frame and the elastic point; (4) the production threshold, in fixed-target and collider form; (5) a numerical instance checked in two frames; (6) the non-relativistic limit. Each problem is stated and then solved in full; the value of an exercise article is in the solutions. The exercise also tests its parents: two gaps found in the course of the work are reported explicitly in the closing section rather than smoothed over.

**Notation for the collision.** Two initial bodies collide and produce $n-2$ final bodies,
$$
1 + 2 \;\longrightarrow\; 3 + 4 + \dots + n,
\qquad
\tilde{P}_1 + \tilde{P}_2 = \tilde{P}_3 + \tilde{P}_4 + \dots + \tilde{P}_n .
$$
Starred quantities refer to the centre-of-momentum (COM) frame, the inertial frame in which the total three-momentum vanishes. For a $2\to2$ collision we write $p^*$ for the common magnitude of the two initial COM momenta and $q^*$ for the common magnitude of the two final COM momenta, and $\theta^*$ for the COM scattering angle between $\mathbf{p}_1^*$ and $\mathbf{p}_3^*$. Unstarred quantities refer to the laboratory.

**A word on the parents.** The conservation law used below is not stated in the parent article, which treats a single particle; it is supplied here and applied. Its derivation from the translation invariance of the Poincaré frame is the subject of the planned companion *Noether's Theorem in Biquaternionic Form* and is not attempted here. What is checked here is that the law, once stated, does what a conservation law must do: it splits into the energy and momentum laws in any frame, it is preserved by every change of frame, and it yields the invariants and thresholds that the standard treatment yields.

## Problem 1: The Conservation Law as a Single Biquaternion Equation

**Statement.** (a) State the conservation law for an isolated collision as a single equation in $\mathbb{B}$ and show that it is equivalent to the separate conservation of total energy and total three-momentum. (b) Show that it is a *linear* equation, and that its consequence for the norm form is strictly weaker than the law itself. (c) Show that it is preserved by every Lorentz rotor and by every translation of the Poincaré frame. (d) Verify (a)–(c) on the two-body example of Problem 5, in the laboratory and in the COM frame.

**Solution (a).** The total four-momentum of the initial pair is
$$
\tilde{P}_{\rm in} = \tilde{P}_1 + \tilde{P}_2,
$$
and that of the final system is $\tilde{P}_{\rm out} = \sum_{f\ge3}\tilde{P}_f$. Each summand lies in $\mathbb{M}_-$, and $\mathbb{M}_-$ is a real vector space, so both sums lie in $\mathbb{M}_-$. The conservation law is the single equation
$$
\boxed{\ \tilde{P}_1 + \tilde{P}_2 = \tilde{P}_3 + \dots + \tilde{P}_n\ }
\qquad\Longleftrightarrow\qquad
\tilde{P}_{\rm in} - \tilde{P}_{\rm out} = 0 .
$$
Write the difference as $i\Delta_0\,e_0 + \boldsymbol{\Delta}$, with $\Delta_0$ real and $\boldsymbol{\Delta} = \sum_k\Delta_k e_k$ a real three-vector, by the membership condition of $\mathbb{M}_-$ (imaginary scalar, real vector). The scalar and vector parts of $\mathbb{M}_-$ are extracted by the real-linear projections $\mathrm{Sc}$ and $\mathrm{Vect}$, so the single biquaternion equation vanishes if and only if its scalar and vector parts vanish separately:
$$
\mathrm{Sc}\!\left(\tilde{P}_{\rm in}-\tilde{P}_{\rm out}\right) = 0
\iff \sum_a E_a = \sum_f E_f,
\qquad
\mathrm{Vect}\!\left(\tilde{P}_{\rm in}-\tilde{P}_{\rm out}\right) = 0
\iff \sum_a \mathbf{p}_a = \sum_f \mathbf{p}_f .
$$
These are the conservation of total energy and of total three-momentum. The biquaternion law is therefore not a new law: it is the pair of standard laws written as one $\mathbb{M}_-$-valued equation. The reason the compression is possible is structural — energy and three-momentum are the scalar and vector components of one element of the material sector, and the $ict$ convention is what puts them there.

**Remark on counting.** A reader may ask whether a single biquaternion equation can carry four real conditions. It can, because $\mathbb{B}$ is a four-dimensional *complex* algebra while the difference lies in the four-dimensional *real* subspace $\mathbb{M}_-$: the equation $\tilde{P}_{\rm in}-\tilde{P}_{\rm out}=0$ is one $\mathbb{M}_-$-valued equation, and since $\mathbb{M}_-$ has real dimension four ($\mathbb{B}$ itself has complex dimension four, i.e. real dimension eight), it is exactly four real equations. No information is lost, and none is smuggled in.

**Solution (b).** The law is linear in the four-momenta: it equates sums, not products or norms. The norm form is not additive, and it does not commute with the sum. Applying $N$ to the law gives only
$$
N(\tilde{P}_1+\tilde{P}_2) = N(\tilde{P}_3+\dots+\tilde{P}_n),
$$
which is the invariance of the total invariant mass (Problem 2). This consequence is strictly weaker than the law: equality of the total norms fixes one number, while four-momentum conservation fixes four. Two final configurations with the same total invariant mass but different total three-momentum can both satisfy the norm condition, and at most one of them conserves four-momentum. (For a $2\to2$ elastic collision at fixed $s$, all COM scattering angles share the same $s$ and the same $t+u$, but only the value of $\theta^*$ determines the split $t,u$; see Problem 2.) The conservation law is thus a linear constraint on $\mathbb{M}_-$-valued data, and it must be imposed as such.

**Solution (c).** *Lorentz rotor.* Apply the same rotor conjugation to every four-momentum, with a fixed unit-norm $\tilde{\Lambda}$. The conjugation is real-linear on $\mathbb{M}_-$ and distributive over addition, so
$$
\tilde{P}_{\rm in}' - \tilde{P}_{\rm out}'
= \sum_a \tilde{\Lambda}\tilde{P}_a\tilde{\Lambda}^\dagger - \sum_f \tilde{\Lambda}\tilde{P}_f\tilde{\Lambda}^\dagger
= \tilde{\Lambda}\left(\tilde{P}_{\rm in}-\tilde{P}_{\rm out}\right)\tilde{\Lambda}^\dagger .
$$
If the unprimed difference vanishes, the primed one vanishes: the law holds in every frame related by a Lorentz transformation. This is the frame covariance of the conservation statement, and it is why a conservation law checked only in the frame that suggested it is not checked. The invariant content is carried by the *element* $\tilde{P}_{\rm in}-\tilde{P}_{\rm out}\in\mathbb{M}_-$, which transforms as a whole.

*Translation.* A Poincaré translation $(\tilde{\Lambda},\tilde{a})$ acts on the four-position by $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger+\tilde{a}$. The four-momentum of a free body is built from its four-velocity, $d\tilde{X}/d\tau$, which is unchanged by a shift of the origin; the shift also drops out of the interval between any two events. Hence each $\tilde{P}_a$ is translation-invariant, and so is the conservation law. Equivalently, in the Poincaré frame the four-momenta are the generators $P_\mu$ of the translation subgroup, and a translation acts on a plane wave of four-wavevector $\tilde{K}$ by multiplication by a central scalar of unit modulus; this representation is checked in the closing section.

**Solution (d).** Take two equal masses $m_1 = m_2 = m$, units $c = 1$, and a projectile of total energy $E_1 = 3m$ striking the target at rest, with the collision elastic. The laboratory four-momenta are
$$
\tilde{P}_1 = i\,3m\,e_0 + \sqrt{8}\,m\,e_3,
\qquad
\tilde{P}_2 = i\,m\,e_0 ,
$$
so $\tilde{P}_{\rm in} = i\,4m\,e_0 + \sqrt{8}\,m\,e_3$ and $s := -N(\tilde{P}_{\rm in}) = (4m)^2 - 8m^2 = 8m^2$. Problem 3 gives the COM data: $W = \sqrt{s} = 2\sqrt{2}\,m$, $E^* = W/2 = \sqrt{2}\,m$, $p^* = m$, and the COM velocity $V = p^*/E^* = 1/\sqrt{2}$, $\gamma = \sqrt{2}$. For the COM scattering angle $\theta^* = 90^\circ$ the final COM momenta are $\mathbf{p}_3^* = m\,e_1$, $\mathbf{p}_4^* = -m\,e_1$, and boosting to the laboratory gives
$$
\tilde{P}_3 = i\,2m\,e_0 + m\,e_1 + \sqrt{2}\,m\,e_3,
\qquad
\tilde{P}_4 = i\,2m\,e_0 - m\,e_1 + \sqrt{2}\,m\,e_3 .
$$
Then, in the laboratory,
$$
\mathrm{Sc}\!\left(\tilde{P}_3+\tilde{P}_4\right) = i\,4m = \mathrm{Sc}\!\left(\tilde{P}_{\rm in}\right),
\qquad
\mathrm{Vect}\!\left(\tilde{P}_3+\tilde{P}_4\right) = \sqrt{8}\,m\,e_3 = \mathrm{Vect}\!\left(\tilde{P}_{\rm in}\right),
$$
so the single equation holds and, by Solution (a), so do the energy and momentum laws. The residual $\tilde{P}_{\rm in}-\tilde{P}_{\rm out}$ vanishes identically here; in Problem 5 the same collision is checked numerically, with the second frame (the COM frame) added explicitly, so that the law is confirmed on the case that did not suggest it.

**A trap in the parent's four-force.** The parent defines the four-force by the *proper*-time derivative, $\tilde{F} = d\tilde{P}/d\tau$. Since $d\tau_a = dt/\gamma_a$, the sum of two of the parent's four-forces is $\tilde{F}_1+\tilde{F}_2 = \gamma_1\,d\tilde{P}_1/dt + \gamma_2\,d\tilde{P}_2/dt$, which equals $d(\tilde{P}_1+\tilde{P}_2)/dt$ only when $\gamma_1 = \gamma_2$. The conservation law is the vanishing of the *coordinate*-time derivative of the *total* four-momentum, and the parent's symbol $\tilde{F}$ cannot be carried over to a multi-body system without the $\gamma$ factors. This is a real gap in the parent for the present purpose, and it is recorded as such in the closing section.

## Problem 2: The Invariant Mass and the Mandelstam Invariants

**Statement.** For a $2\to2$ collision $1+2\to3+4$, define
$$
s := -c^2\,N(\tilde{P}_1+\tilde{P}_2),
\qquad
t := -c^2\,N(\tilde{P}_1-\tilde{P}_3),
\qquad
u := -c^2\,N(\tilde{P}_1-\tilde{P}_4).
$$
(a) Express $s$ in components and identify it with the square of the COM energy. (b) Express $s,t,u$ through the invariant pairing. (c) Prove $s+t+u = (m_1^2+m_2^2+m_3^2+m_4^2)c^4$ using the conservation law. (d) Evaluate for elastic scattering and check the sum rule numerically. (e) Explain why $t$ and $u$ do not define real masses.

**Solution (a).** Since $\tilde{P}_1+\tilde{P}_2 = i(E_1+E_2)/c\,e_0 + (\mathbf{p}_1+\mathbf{p}_2)$,
$$
N(\tilde{P}_1+\tilde{P}_2)
= -\frac{(E_1+E_2)^2}{c^2} + (\mathbf{p}_1+\mathbf{p}_2)^2,
$$
so
$$
s = (E_1+E_2)^2 - (\mathbf{p}_1+\mathbf{p}_2)^2c^2 .
$$
This is the standard invariant $s$. In the COM frame $\mathbf{p}_1+\mathbf{p}_2 = 0$, so $s = W^2$ with $W := E_1^*+E_2^*$ the total COM energy; and $s$ is invariant, so $W = \sqrt{s}$ in every frame. The total invariant mass is $M_{\rm tot} = W/c^2 = \sqrt{s}/c^2$, and the parent's definition $N(\tilde{P}) = -M^2c^2$ is recovered with $M = M_{\rm tot}$ whenever $\tilde{P}$ is future-directed timelike, which the sum of two future-directed timelike four-momenta always is.

**Solution (b).** Expanding the norm of a difference,
$$
N(\tilde{A}-\tilde{B}) = N(\tilde{A}) + N(\tilde{B}) - 2\langle\tilde{A},\tilde{B}\rangle,
$$
and using $N(\tilde{P}_i) = -m_i^2c^2$,
$$
s = (m_1^2+m_2^2)c^4 - 2c^2\langle\tilde{P}_1,\tilde{P}_2\rangle,
\qquad
t = (m_1^2+m_3^2)c^4 + 2c^2\langle\tilde{P}_1,\tilde{P}_3\rangle,
\qquad
u = (m_1^2+m_4^2)c^4 + 2c^2\langle\tilde{P}_1,\tilde{P}_4\rangle .
$$
In components, using $\langle\tilde{P}_A,\tilde{P}_B\rangle = -E_AE_B/c^2 + \mathbf{p}_A\cdot\mathbf{p}_B$,
$$
s = (m_1^2+m_2^2)c^4 + 2E_1E_2 - 2c^2\,\mathbf{p}_1\cdot\mathbf{p}_2,
$$
and analogously for $t$ (with $2E_1E_3 - 2c^2\mathbf{p}_1\cdot\mathbf{p}_3$ added to $(m_1^2+m_3^2)c^4$) and for $u$.

**Solution (c).** Add the three invariants. The mass terms sum to $(3m_1^2+m_2^2+m_3^2+m_4^2)c^4$. The pairing terms, including the minus sign in $s$ and the plus signs in $t$ and $u$, are
$$
2c^2\left(-\langle\tilde{P}_1,\tilde{P}_2\rangle + \langle\tilde{P}_1,\tilde{P}_3\rangle + \langle\tilde{P}_1,\tilde{P}_4\rangle\right).
$$
The conservation law gives $\tilde{P}_2 = \tilde{P}_3+\tilde{P}_4-\tilde{P}_1$, hence by bilinearity
$$
\langle\tilde{P}_1,\tilde{P}_2\rangle
= \langle\tilde{P}_1,\tilde{P}_3\rangle + \langle\tilde{P}_1,\tilde{P}_4\rangle - \langle\tilde{P}_1,\tilde{P}_1\rangle
= \langle\tilde{P}_1,\tilde{P}_3\rangle + \langle\tilde{P}_1,\tilde{P}_4\rangle + m_1^2c^2,
$$
because $\langle\tilde{P}_1,\tilde{P}_1\rangle = N(\tilde{P}_1) = -m_1^2c^2$. The bracket in the pairing terms is therefore $-m_1^2c^2$, so the pairing contributes $-2m_1^2c^4$ and the total is
$$
\boxed{\ s + t + u = \left(m_1^2+m_2^2+m_3^2+m_4^2\right)c^4\ }
$$
The sum rule is exact and rests only on the mass-shell relation and the linearity of the conservation law. It fails if the conservation law is weakened to equality of norms.

**Solution (d).** For elastic scattering $1+2\to1+2$ one has $m_3 = m_1$, $m_4 = m_2$, hence $q^* = p^*$, $E_3^* = E_1^* =: E_1^*$, and the COM final momenta are back to back. Then
$$
t = m_1^2c^4 + m_1^2c^4 + 2c^2\left(-\frac{E_1^{*2}}{c^2} + p^{*2}\cos\theta^*\right)
= 2m_1^2c^4 - 2E_1^{*2} + 2c^2p^{*2}\cos\theta^* ,
$$
and with $E_1^{*2} = m_1^2c^4 + p^{*2}c^2$ this collapses to
$$
\boxed{\ t = -2c^2p^{*2}\left(1-\cos\theta^*\right)\ }
$$
for $m_1 = m_3$, irrespective of $m_2 = m_4$. If in addition $m_1 = m_2 = m$, then $E_1^* = E_2^* = \sqrt{s}/2$ and the crossed invariant is $u = -2c^2p^{*2}(1+\cos\theta^*)$; the sum rule becomes
$$
s + t + u = 4m^2c^4 = 4E^{*2} - 4c^2p^{*2},
$$
which is $E^{*2} - p^{*2}c^2 = m^2c^4$ rearranged. For the example of Problem 1(d), $s = 8m^2$, $p^* = m$, and $\theta^* = 90^\circ$ give $t = u = -2m^2$, so $s+t+u = 4m^2$, in agreement with the four equal masses $m$.

**Solution (e).** The definition $N(\tilde{P}) = -M^2c^2$ with real $M\ge0$ presupposes that $\tilde{P}$ is timelike (or null, for $M=0$). The total four-momentum of a physical initial state is future-directed timelike, so $s>0$ and $M_{\rm tot}$ is real. The crossed invariants $t$ and $u$, by contrast, are norms of *differences* of four-momenta and carry no such guarantee: for a $2\to2$ collision they can be negative, as they are in the example above ($t=u=-2m^2$). A negative $t$ or $u$ corresponds to a spacelike momentum transfer, and there is no real "mass" attached to it; the invariant is $t$ itself. The physically meaningful statements are $t\le0$ for elastic scattering with $m_1=m_3$ (from the boxed formula, since $1-\cos\theta^*\ge0$), and the sum rule of part (c). The parent's invariant-mass construction, stated for the total of a physical pair, does not extend to these crossed channels, and the exercise uses the norm form directly.

## Problem 3: The Centre-of-Momentum Frame of a Collision

**Statement.** (a) Construct the boost biquaternion that carries the laboratory to the COM frame and verify that it rotates the total four-momentum to a pure imaginary scalar. (b) Derive the COM energies and the initial and final momentum magnitudes for a general $2\to2$ collision. (c) Give the relation between the laboratory velocity of the COM frame and the total four-momentum. (d) Record the elastic case.

**Solution (a).** Let $\tilde{P} = \tilde{P}_1+\tilde{P}_2$ be the total four-momentum, with $\tilde{P}\bar{\tilde{P}} = -W^2/c^2$, where $W=\sqrt{s}>0$. The parent's relation between a four-velocity and its frame rotor, $\tilde{\Lambda} = \sqrt{-\frac{i}{c}\bar{\tilde{U}}}$, applied to the total treated as a single body of mass $M_{\rm tot} = W/c^2$, gives the rotor
$$
\boxed{\ \tilde{\Lambda}_{\rm CM} = \sqrt{-\frac{ic}{W}\,\bar{\tilde{P}}}\ }
= \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\,\hat{\mathbf{V}},
\qquad
\tilde{\Lambda}_{\rm CM}\bar{\tilde{\Lambda}}_{\rm CM} = e_0,
$$
where $\Psi$ is the rapidity of the COM frame in the laboratory, $\tanh\Psi = V/c$. This is the biquaternion form of the standard construction, and it is a Hermitian element of $\mathbb{M}_+$. A direct substitution shows that
$$
\tilde{\Lambda}_{\rm CM}\,\tilde{P}\,\tilde{\Lambda}_{\rm CM}^\dagger
= i\,M_{\rm tot}c\,e_0 = i\frac{W}{c}\,e_0 ,
$$
which is the statement that $\tilde{P}$ has been rotated until its vector part vanishes, i.e. that the frame is the COM frame. The rotor that carries the COM frame's data back to the laboratory is the quaternion conjugate,
$$
\tilde{P}_a = \bar{\tilde{\Lambda}}_{\rm CM}\,\tilde{P}_a^{*}\,\bar{\tilde{\Lambda}}_{\rm CM}^\dagger ,
$$
because $\bar{\tilde{\Lambda}}_{\rm CM}$ is the boost of the same rapidity in the opposite direction.

**Solution (b).** In the COM frame the vector part of $\tilde{P}$ vanishes, so $\mathbf{p}_1^* + \mathbf{p}_2^* = 0$ and $E_1^* + E_2^* = W$. The mass-shell relations $E_a^{*2} = m_a^2c^4 + p^{*2}c^2$ (both particles share the magnitude $p^*$ because their momenta are opposite) give, by the same elimination as for the two-body decay,
$$
E_1^* = \frac{s + m_1^2c^4 - m_2^2c^4}{2\sqrt{s}},
\qquad
E_2^* = \frac{s + m_2^2c^4 - m_1^2c^4}{2\sqrt{s}},
$$
and, factoring the difference of the squares of the masses,
$$
p^{*2}c^2 = \frac{\left[s-(m_1+m_2)^2c^4\right]\left[s-(m_1-m_2)^2c^4\right]}{4s}.
$$
The COM energy satisfies $W\ge (m_1+m_2)c^2$ with equality if and only if the two bodies are at relative rest, so the radicand is non-negative for every physical collision, and $p^*=0$ at the two-body threshold $W = (m_1+m_2)c^2$. For the final pair the identical formulas hold with $m_3,m_4$ and the magnitude $q^*$:
$$
E_3^* = \frac{s + m_3^2c^4 - m_4^2c^4}{2\sqrt{s}},
\qquad
q^{*2}c^2 = \frac{\left[s-(m_3+m_4)^2c^4\right]\left[s-(m_3-m_4)^2c^4\right]}{4s}.
$$
The final momenta are opposite, $\mathbf{p}_3^* = -\mathbf{p}_4^*$, of common magnitude $q^*$, and their common direction relative to $\mathbf{p}_1^*$ is the COM scattering angle $\theta^*$. There is no constraint on $\theta^*$ from four-momentum conservation alone: conservation fixes the magnitudes and the back-to-back configuration but leaves one angle free, which is why the scattering angle must be supplied by the dynamics (or measured).

**Solution (c).** The laboratory energy and momentum of the COM frame are the total ones, $E=E_1+E_2$ and $\mathbf{P}=\mathbf{p}_1+\mathbf{p}_2$, and the COM frame moves in the laboratory with velocity
$$
\mathbf{V} = \frac{\mathbf{P}c^2}{E},
\qquad
\gamma = \frac{1}{\sqrt{1-V^2/c^2}} = \frac{E}{W},
$$
the second equality because $E = \gamma(W + \mathbf{V}\cdot 0)$ when the total momentum vanishes in the COM frame. The laboratory energy of a body with COM energy $E_a^*$ and COM momentum $\mathbf{p}_a^*$ is therefore
$$
E_a = \gamma\left(E_a^* + \mathbf{V}\cdot\mathbf{p}_a^*\right),
$$
the standard transformation. The construction of $\tilde{\Lambda}_{\rm CM}$ is undefined when $\tilde{P}$ is null, $W=0$; that degenerate case (massless collinear momenta) is the collision analogue of the parent's open question on null totals and is not treated here.

**Solution (d).** In the elastic case $m_3=m_1$, $m_4=m_2$, the two formulas for the momentum magnitude agree, $q^*=p^*$, as they must, and $E_3^*=E_1^*$, $E_4^*=E_2^*$: four-momentum conservation in the COM frame is then the statement that the two bodies scatter, back to back, preserving each energy and the common momentum magnitude. The only free parameter is $\theta^*$, and the crossed invariant is the boxed formula of Problem 2(d).

## Problem 4: The Production Threshold

**Statement.** (a) Derive the general threshold condition for $1+2\to3+\dots+n$. (b) For a fixed target (body 2 at rest) derive $s$ and the threshold projectile energy, and evaluate it for $p+p\to p+p+\pi^0$. (c) Compare with the symmetric-collider threshold and explain the advantage quantitatively.

**Solution (a).** The final system has total invariant mass $M_{\rm out} = \sum_{f\ge3}m_f$ when it is produced at rest in its own COM frame, which is the configuration of least total energy. Since $W=\sqrt{s}$ is the total COM energy and is invariant, production is possible exactly when
$$
\sqrt{s} \;\ge\; \left(\sum_{f\ge3} m_f\right)c^2 .
$$
At equality the final particles emerge with no relative kinetic energy. This is the biquaternion form of the standard threshold: it is a statement about $N(\tilde{P}_1+\tilde{P}_2)$, computed from the initial data, against a rest-energy sum. Because $s$ is a Lorentz invariant, the condition is frame-independent, as a threshold must be.

**Solution (b).** Let body 2 be at rest in the laboratory, so $\tilde{P}_2 = i\,m_2c\,e_0$ and $\mathbf{p}_2=0$. Then
$$
s = (m_1^2+m_2^2)c^4 + 2E_1m_2c^2 ,
$$
which follows from $s = (m_1^2+m_2^2)c^4 - 2c^2\langle\tilde{P}_1,\tilde{P}_2\rangle$ with $\langle\tilde{P}_1,\tilde{P}_2\rangle = -E_1m_2$. Setting $s = \left(\sum_{f\ge3}m_f\right)^2c^4$ and solving for the projectile total energy,
$$
E_1^{\rm thr} = \frac{\left(\sum_{f\ge3}m_f\right)^2 - m_1^2 - m_2^2}{2m_2}\,c^2,
\qquad
K_1^{\rm thr} = E_1^{\rm thr} - m_1c^2 .
$$
For $p+p\to p+p+\pi^0$, with $m_p = 938.272$ MeV$/c^2$ and $m_\pi = 134.977$ MeV$/c^2$, the final mass sum is $2m_p+m_\pi = 2011.521$ MeV$/c^2$, so
$$
E_1^{\rm thr} = 1217.935\ \text{MeV},
\qquad
K_1^{\rm thr} = 279.663\ \text{MeV}.
$$
A projectile kinetic energy of $200$ MeV is below threshold ($\sqrt{s} = 1974.0$ MeV $< 2011.5$ MeV), and one of $300$ MeV is above it ($\sqrt{s} = 2021.0$ MeV); the threshold lies at the computed $279.66$ MeV, as a direct evaluation of $s(K_1)$ confirms.

**Solution (c).** In a symmetric collider the two initial bodies have equal and opposite momenta, so the laboratory *is* the COM frame and $s = (2E)^2 = 4E^2$, $E$ being the total energy of each beam. The threshold is therefore
$$
E_{\rm beam}^{\rm thr} = \tfrac{1}{2}\left(\sum_{f\ge3}m_f\right)c^2,
\qquad
K_{\rm beam}^{\rm thr} = \tfrac{1}{2}\left(\sum_{f\ge3}m_f\right)c^2 - m_1c^2 .
$$
For $p+p\to p+p+\pi^0$ this is $E_{\rm beam}^{\rm thr} = 1005.761$ MeV and $K_{\rm beam}^{\rm thr} = 67.489$ MeV. The collider threshold is lower by the factor
$$
\frac{K_1^{\rm thr}}{K_{\rm beam}^{\rm thr}} = \frac{279.663}{67.489} = 4.14 ,
$$
for this reaction. The origin of the factor is visible in the fixed-target expression: $s = (m_1^2+m_2^2)c^4 + 2E_1m_2c^2$ grows only linearly with $E_1$ when one body is at rest, whereas in a collider $s=4E^2$ grows quadratically. A fixed-target beam must supply most of its energy to the centre-of-mass motion, which the conservation law leaves kinematically present; only the invariant $s$ is available for production.

## Problem 5: A Numerical Instance

**Statement.** Take two equal masses $m_1=m_2=m$, units $c=1$, and an elastic collision with projectile total energy $E_1 = 3m$ on a stationary target. (a) Compute $s$, $W$, $E_1^*$, $p^*$, $V$, and $\gamma$. (b) For $\theta^*=90^\circ$ compute the two final laboratory four-momenta, energies, and angles. (c) Verify four-momentum conservation in both frames and the sum rule. (d) Compare the laboratory opening angle with the non-relativistic value.

**Solution (a).** With $c=1$ and $\mathbf{p}_1$ along $e_3$,
$$
\tilde{P}_1 = i\,3m\,e_0 + \sqrt{8}\,m\,e_3,
\qquad
\tilde{P}_2 = i\,m\,e_0,
\qquad
\tilde{P} = i\,4m\,e_0 + \sqrt{8}\,m\,e_3 .
$$
Hence
$$
s = 16m^2 - 8m^2 = 8m^2,
\qquad
W = \sqrt{s} = 2\sqrt{2}\,m = 2.828427\,m,
$$
$$
E_1^* = E_2^* = \frac{W}{2} = \sqrt{2}\,m = 1.414214\,m,
\qquad
p^* = \sqrt{E_1^{*2}-m^2} = m,
$$
$$
V = \frac{p^*}{E_1^*} = \frac{1}{\sqrt{2}} = 0.707107,
\qquad
\gamma = \frac{1}{\sqrt{1-V^2}} = \sqrt{2} = 1.414214 .
$$
The COM momentum is exactly $m$ in these units because $E_1^{*2} = 2m^2$ and $m_1^2 = m^2$; the numbers are chosen so that the arithmetic is exact.

**Solution (b).** Take the COM scattering in the $e_1$–$e_3$ plane with $\theta^*=90^\circ$, so
$$
\tilde{P}_3^* = i\sqrt{2}\,m\,e_0 + m\,e_1,
\qquad
\tilde{P}_4^* = i\sqrt{2}\,m\,e_0 - m\,e_1 .
$$
The COM→labor boost is the rotation generated by $\bar{\tilde{\Lambda}}_{\rm CM} = \cosh\frac{\Psi}{2} - i\sinh\frac{\Psi}{2}\hat{\mathbf{V}}$ with $\hat{\mathbf{V}} = e_3$, which acts by the component formula of Problem 3(c) with $E_1^* = E_2^* = \sqrt{2}m$, $p^* = m$, $V = 1/\sqrt{2}$, $\gamma = \sqrt{2}$. A particle whose COM momentum is transverse to $\mathbf{V}$ acquires the laboratory momentum $\gamma p^* = \sqrt{2}\,m$ along $\mathbf{V}$ and energy $\gamma E^* = 2m$; a particle with a longitudinal COM component gains or loses according to the sign. Thus
$$
\tilde{P}_3 = i\,2m\,e_0 + m\,e_1 + \sqrt{2}\,m\,e_3,
\qquad
\tilde{P}_4 = i\,2m\,e_0 - m\,e_1 + \sqrt{2}\,m\,e_3 .
$$
The laboratory energies are $E_3 = E_4 = 2m$, and the laboratory angles measured from $\mathbf{V}$ are
$$
\tan\theta_3 = \frac{p_{3\perp}}{p_{3\parallel}} = \frac{1}{\sqrt{2}},
\qquad
\tan\theta_4 = \frac{1}{\sqrt{2}},
\qquad
\theta_3 = \theta_4 = 35.2644^\circ,
$$
so the opening angle between the two final particles is $\Theta = 70.5288^\circ$.

**Solution (c).** Adding the two final four-momenta,
$$
\tilde{P}_3 + \tilde{P}_4 = i\,4m\,e_0 + \sqrt{8}\,m\,e_3 = \tilde{P}_1+\tilde{P}_2,
$$
so the conservation law holds exactly in the laboratory; the energy sum is $2m+2m = 4m$, and the three-momentum is $(\sqrt{2}+\sqrt{2})m\,e_3 = \sqrt{8}\,m\,e_3$. In the COM frame it holds by construction, $\tilde{P}_1^*+\tilde{P}_2^* = \tilde{P}_3^*+\tilde{P}_4^* = i\,2\sqrt{2}\,m\,e_0$; the second frame is the one that did not suggest the law, and the check there is the independent one. The invariants are
$$
s = 8m^2,
\qquad
t = -2p^{*2}(1-\cos 90^\circ) = -2m^2,
\qquad
u = -2p^{*2}(1+\cos 90^\circ) = -2m^2,
$$
so
$$
s + t + u = 8m^2 - 2m^2 - 2m^2 = 4m^2 = \left(m_1^2+m_2^2+m_3^2+m_4^2\right),
$$
as the sum rule requires.

**Solution (d).** In the non-relativistic limit $E_1\to m$ and $V\to0$, so $\gamma\to1$ and the two final particles emerge at $90^\circ$ to one another. Here $\gamma=\sqrt{2}=1.414$, appreciably above $1$, and the opening angle is $70.53^\circ$, well below $90^\circ$: the relativistic contraction of the opening angle is already large at a projectile kinetic energy of $K_1 = E_1 - m = 2m$, which is twice the rest energy. Problem 6 quantifies the limit.

## Problem 6: The Non-Relativistic Limit

**Statement.** Expand the results above for $\mathbf{v}\ll c$ and recover (a) the separate Galilean conservation laws, (b) the fixed-target threshold as a rest-energy balance, and (c) the $90^\circ$ opening angle for equal-mass elastic scattering. Quantify why the example of Problem 5 is far from the limit.

**Solution (a).** For $\mathbf{v}_a\ll c$, $\gamma_a = 1 + \frac{1}{2}v_a^2/c^2 + O(v^4/c^4)$, and the four-momentum is
$$
\tilde{P}_a = i\left(m_ac + \frac{1}{2}\frac{m_av_a^2}{c}\right)e_0 + m_a\mathbf{v}_a + O(v^3/c^3).
$$
The scalar part is $i/c$ times (rest energy + kinetic energy), and the vector part is the Newtonian momentum. Four-momentum conservation therefore splits into the separate conservation of total rest-plus-kinetic energy and of total Newtonian momentum. Because the rest masses are separately conserved in a non-relativistic collision, this is the Newtonian conservation of kinetic energy and momentum. The single biquaternion equation reproduces both, with the $ict$ convention packing them into one element of $\mathbb{M}_-$.

**Solution (b).** In the fixed-target expression $s = (m_1^2+m_2^2)c^4 + 2E_1m_2c^2$, writing $E_1 = m_1c^2+K_1$ gives $s = (m_1+m_2)^2c^4 + 2K_1m_2c^2$. At the production threshold $s = (M_{\rm out})^2c^4$, so
$$
K_1^{\rm thr} = \frac{M_{\rm out}^2 - (m_1+m_2)^2}{2m_2}\,c^2,
$$
which for $M_{\rm out} = m_1+m_2+\Delta m$ becomes $K_1^{\rm thr}\approx \frac{(m_1+m_2)\Delta m}{m_2}c^2$: the projectile must supply the mass excess, diluted by the recoil of the heavy target. For $p+p\to p+p+\pi^0$ this gives $K_1^{\rm thr}\approx\frac{2m_p\,m_\pi}{m_p}c^2 = 2m_\pi c^2 = 270.0$ MeV, within $3.5\%$ of the exact $279.66$ MeV, the correction being the target's recoil kinetic energy, which the approximation neglects by setting $M_{\rm out}\approx m_1+m_2$ before expanding.

**Solution (c).** For elastic equal-mass scattering, expand the laboratory angle relations of Problem 3(c). With $V\ll c$, $\gamma\to1$, and the COM relations $p^* = mV + O(V^3/c^2)$,
$$
\tan\theta_3 = \frac{\sin\theta^*}{\gamma(1+\cos\theta^*)} \to \tan\frac{\theta^*}{2},
\qquad
\tan\theta_4 = \frac{\sin\theta^*}{\gamma(1-\cos\theta^*)} \to \cot\frac{\theta^*}{2},
$$
so $\theta_3+\theta_4\to\theta^*/2+(\pi-\theta^*)/2 = \pi/2$. The two final particles emerge at right angles in the laboratory, the standard Newtonian result for equal masses; the relativistic opening angle is always less than $\pi/2$, the deficit growing with $\gamma$. Problem 5 makes this concrete: at $K_1 = 2mc^2$ the opening angle is $70.53^\circ$, $19.5^\circ$ below the Newtonian value, so the non-relativistic limit is nowhere near valid at twice the rest energy. For $K_1\ll mc^2$ the expansion is accurate, with relative corrections of order $V^2/c^2\sim K_1/(mc^2)$.

## Where the Parents Fall Short

Two gaps were found while applying the parents. They are reported here, with the evidence, rather than absorbed into the prose.

**Gap 1: the parent states no conservation law and no multi-body four-force.** *Relativistic Mechanics in Biquaternionic Form* defines the four-momentum and the mass-shell relation for a single particle, and it states the conservation of the four-*current*, $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})=0$. It does not state the conservation of the total four-momentum of a system, and it defines the four-force by the proper-time derivative $\tilde{F}=d\tilde{P}/d\tau$, which cannot be summed across bodies without the factors $\gamma_a$ (Problem 1). The conservation law is therefore supplied by this exercise, not inherited. No derivation from the translation invariance of the Poincaré frame is attempted here: that belongs to the planned companion *Noether's Theorem in Biquaternionic Form*, and its absence is a scope boundary, not an error.

**Gap 2: the parent's invariant-mass construction covers only the timelike total.** The parent (and the two-body companion) define the invariant mass by $N(\tilde{P}) = -M^2c^2$ with real $M\ge0$. Applied to the total four-momentum of a physical pair this is well founded, because the sum of future-directed timelike four-momenta is future-directed timelike. It does not extend to the crossed invariants $t$ and $u$ of a $2\to2$ collision, which are norms of differences and are spacelike (negative $t,u$ at $90^\circ$ in Problem 5). The exercise therefore uses the norm form directly and does not extract a real mass from $t$ or $u$; the parent's mass construction is silent on these.

**Inherited, and not re-reported.** The direction convention of the star-to-laboratory boost rotor in *The Lorentz Transformation as a Biquaternionic Rotation* (and in the two-body companion) is a known ambiguity: the rotor built with $+\hat{\mathbf{V}}$ carries the laboratory to the COM frame, so the COM-to-laboratory rotation is generated by the quaternion conjugate. This exercise adopts that physical convention and states it explicitly (Problem 3); it was already recorded by the exercise on the two-body decay and is not claimed here as a new finding.

## Summary

We have worked four-momentum conservation for a collision as an application of the parent article's four-momentum and mass-shell relation, with the frame tools of the Lorentz and Poincaré companions.

1. **The law.** An isolated collision satisfies the single $\mathbb{M}_-$-valued equation $\tilde{P}_1+\tilde{P}_2 = \sum_f\tilde{P}_f$, which is exactly the separate conservation of total energy and total three-momentum, because the scalar and vector parts are real-linear projections. The law is linear, is preserved by every Lorentz rotor, and is invariant under translations. Its norm consequence, the invariance of $s$, is strictly weaker than the law itself.

2. **Invariants.** With $s = -c^2N(\tilde{P}_1+\tilde{P}_2)$ and $t = -c^2N(\tilde{P}_1-\tilde{P}_3)$, $u = -c^2N(\tilde{P}_1-\tilde{P}_4)$, the sum rule $s+t+u = (m_1^2+m_2^2+m_3^2+m_4^2)c^4$ holds exactly; for elastic scattering with $m_1=m_3$ it gives $t = -2c^2p^{*2}(1-\cos\theta^*)$. The crossed invariants $t,u$ can be spacelike and define no real mass.

3. **COM frame.** The rotor $\tilde{\Lambda}_{\rm CM} = \sqrt{-\frac{ic}{W}\bar{\tilde{P}}}$ carries the laboratory to the centre-of-momentum frame, rotating $\tilde{P}$ to $iW/c\,e_0$; the conjugate rotor carries the data back. The COM energies and momentum magnitudes are $E_a^* = (s+m_a^2c^4-m_b^2c^4)/(2\sqrt{s})$ and $p^{*2}c^2 = [s-(m_1+m_2)^2c^4][s-(m_1-m_2)^2c^4]/(4s)$, and conservation leaves the COM scattering angle free.

4. **Threshold.** Production requires $\sqrt{s}\ge\left(\sum_f m_f\right)c^2$. For a fixed target $s = (m_1^2+m_2^2)c^4+2E_1m_2c^2$, giving $K_1^{\rm thr} = 279.663$ MeV for $p+p\to p+p+\pi^0$; a symmetric collider has $s=4E^2$ and needs only $67.489$ MeV per beam, the ratio $4.14$ reflecting the linear versus quadratic growth of $s$.

5. **Numbers.** For equal masses with $E_1=3mc^2$ and $\theta^*=90^\circ$: $s=8m^2$, $W=2\sqrt{2}m$, $E^*=\sqrt{2}m$, $p^*=m$, $V=1/\sqrt{2}$, $\gamma=\sqrt{2}$; the laboratory four-momenta are $i\,2m\,e_0 \pm m\,e_1 + \sqrt{2}\,m\,e_3$, the laboratory angles are $35.2644^\circ$ each, the opening angle is $70.5288^\circ$, and $s+t+u=4m^2$.

6. **Limits.** The non-relativistic limit recovers Galilean energy and momentum conservation, the right-angle emergence for equal-mass elastic scattering, and the mass-excess threshold formula $K_1^{\rm thr}\approx\frac{(m_1+m_2)\Delta m}{m_2}c^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): real scalar, imaginary vector |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Complex scalar subspace (center of the algebra) |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\langle\tilde{A},\tilde{B}\rangle = \mathrm{Sc}(\tilde{A}\bar{\tilde{B}})$ | Invariant pairing on $\mathbb{M}_-$ |
| $\tilde{P}_a = m_a\tilde{U}_a = iE_a/c\,e_0+\mathbf{p}_a$ | Four-momentum, $N(\tilde{P}_a)=-m_a^2c^2$ |
| $\tilde{U}_a = \gamma_a(ic\,e_0+\mathbf{v}_a)$ | Four-velocity, $N(\tilde{U}_a)=-c^2$ |
| $\tilde{P} = \tilde{P}_1+\tilde{P}_2$ | Total four-momentum |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost biquaternion, $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$ |
| $(\tilde{\Lambda},\tilde{a})$ | Poincaré transformation, $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger+\tilde{a}$ |
| $\tilde{\Lambda}_{\rm CM} = \sqrt{-\frac{ic}{W}\bar{\tilde{P}}}$ | Boost biquaternion, laboratory to COM frame |
| $\bar{\tilde{\Lambda}}_{\rm CM}$ | Quaternion conjugate, COM frame to laboratory |
| $s,t,u$ | Mandelstam invariants, $s=-c^2N(\tilde{P}_1+\tilde{P}_2)$, etc. |
| $W = \sqrt{s} = E_1^*+E_2^*$ | Total COM energy |
| $M_{\rm tot} = W/c^2$ | Total invariant mass of the initial pair |
| $p^*,q^*$ | Initial and final common COM momentum magnitudes |
| $E_a^*, \mathbf{p}_a^*$ | COM energies and momenta |
| $\theta^*$ | COM scattering angle |
| $\mathbf{V} = \mathbf{P}c^2/E$, $\gamma = E/W$ | Laboratory velocity and Lorentz factor of the COM frame |
| $\Theta$ | Laboratory opening angle |
| $K_1 = E_1 - m_1c^2$ | Projectile kinetic energy |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula of the informational sector |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard relativistic collision kinematics, thresholds, and Mandelstam invariants.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for fixed-target and collider kinematics and the transformation of four-momenta.
- Particle Data Group, *Review of Particle Physics*, for the particle masses and threshold energies used in Problem 4.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original spacetime-algebra formulation of relativistic conservation laws.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of rotors and relativistic kinematics.
- Companion articles of this series: *Relativistic Mechanics in Biquaternionic Form*; *The Lorentz Transformation as a Biquaternionic Rotation*; *The Poincaré Group and the Biquaternion Frame*; *The Relativistic Two-Body Problem in Biquaternionic Form*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *The Klein–Gordon Equation in Biquaternionic Form*.
