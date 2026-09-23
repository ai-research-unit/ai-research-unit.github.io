# __Exercise: The Relativistic Kinematics of a Two-Body Decay__

## Introduction

This is one of the exercises in the relativity series. It is a set of worked problems in the relativistic kinematics of a two-body decay, using the framework and the notation of the companion article *The Relativistic Two-Body Problem in Biquaternionic Form*. That article is the parent of this exercise: it sets up the kinematics, and what follows applies it. Nothing new is introduced, and every result below is obtained from the tools already defined there.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, and the scalar imaginary $i$ with $i^2 = -1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part) and the Hermitian subspace $\mathbb{M}_+$. The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ and the invariant pairing $\langle \tilde{A}, \tilde{B}\rangle = \mathrm{Sc}(\tilde{A}\bar{\tilde{B}})$ on $\mathbb{M}_-$. The four-momentum $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$ with $N(\tilde{P}) = -m^2c^2$, the unit four-velocity $\tilde{u} = \tilde{U}/c$ with $N(\tilde{u}) = -1$, the rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$, the boost biquaternion $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ with $\tanh\psi = u/c$, and the relative rapidity $\psi_{\rm rel}$ with $\cosh\psi_{\rm rel} = -\langle \tilde{u}_1, \tilde{u}_2\rangle$. Throughout, $c$ is the speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ is the vacuum value.

**What is to be shown.** The problems are: (1) the daughter energies and momentum in the centre-of-momentum frame of a parent at rest; (2) the general case of a moving parent, through the boost biquaternion the parent constructs; (3) the invariant mass of each pair in a three-body decay; (4) the threshold and the opening-angle conditions; (5) a numerical instance, checked to several digits; (6) the non-relativistic limit. Each problem is stated and then solved in full; the value of an exercise article is in the solutions.

**Notation for the decay.** A parent of mass $M$ decays into two daughters of masses $m_1, m_2$,
$$
A \;\longrightarrow\; 1 + 2, \qquad \tilde{P}_A = \tilde{P}_1 + \tilde{P}_2 .
$$
In the rest frame of the parent the total four-momentum is $\tilde{P}_A = iMc\,e_0$, so the parent rest frame **is** the centre-of-momentum (COM) frame of the daughters. Starred quantities refer to that frame: $\mathbf{p}_1^* = -\mathbf{p}_2^* = \mathbf{p}^*$, $p^* = |\mathbf{p}^*|$, and $E_1^* + E_2^* = Mc^2$. Unstarred quantities refer to the laboratory frame. Because the two-body article already derived the kinematics, several intermediate steps below reproduce its equations; they are included so that the exercise is self-contained.

This exercise also serves to test the parent. The direction of the boost biquaternion that carries the COM frame to the laboratory — a point that repays care — is worked out explicitly in Problem 2.

## Problem 1: Daughter Energies and Momentum in the COM Frame

**Statement.** For $A \to 1+2$ with the parent at rest, derive the daughter energies $E_1^*, E_2^*$, the common momentum magnitude $p^*$, the speeds $v_a^*$, and the released energy $Q$. Show that the decay is allowed exactly when $M \ge m_1 + m_2$.

**Solution.** The conservation law is the single biquaternion equation $\tilde{P}_A = \tilde{P}_1 + \tilde{P}_2$. In the parent rest frame $\tilde{P}_A = iMc\,e_0$, and writing $\tilde{P}_a^* = iE_a^*/c\,e_0 + \mathbf{p}_a^*$, the conservation law splits, under the real-linear projections onto the scalar and vector parts of $\mathbb{M}_-$, into
$$
E_1^* + E_2^* = Mc^2, \qquad \mathbf{p}_1^* + \mathbf{p}_2^* = 0 .
$$
The second equation says the daughters are emitted back to back: $\mathbf{p}_1^* = -\mathbf{p}_2^* = \mathbf{p}^*$, so $p_1^{*2} = p_2^{*2} = p^{*2}$. The mass-shell relations are
$$
E_1^{*2} = m_1^2c^4 + p^{*2}c^2, \qquad E_2^{*2} = m_2^2c^4 + p^{*2}c^2 .
$$
Subtracting eliminates $p^{*2}$,
$$
E_1^{*2} - E_2^{*2} = (m_1^2 - m_2^2)c^4
\quad\Longrightarrow\quad
(E_1^* - E_2^*)(E_1^* + E_2^*) = (m_1^2 - m_2^2)c^4,
$$
and with $E_1^* + E_2^* = Mc^2$ this gives $E_1^* - E_2^* = (m_1^2 - m_2^2)c^2/M$. Combining the sum and the difference,
$$
E_1^* = \frac{\left(M^2 + m_1^2 - m_2^2\right)c^2}{2M},
\qquad
E_2^* = \frac{\left(M^2 + m_2^2 - m_1^2\right)c^2}{2M}.
$$
Substituting $E_1^*$ into the mass shell and factoring,
$$
p^{*2}c^2 = E_1^{*2} - m_1^2c^4
= \frac{c^4}{4M^2}\left[\left(M^2 + m_1^2 - m_2^2\right)^2 - 4M^2m_1^2\right].
$$
The bracket factors as a difference of squares, first as $\left[(M-m_1)^2 - m_2^2\right]\left[(M+m_1)^2 - m_2^2\right]$ and then as the product of two differences of squares, so that
$$
p^* = \frac{c}{2M}\sqrt{\left[M^2 - (m_1+m_2)^2\right]\left[M^2 - (m_1-m_2)^2\right]} .
$$
The speeds follow from $\mathbf{p}_a^* = \gamma_a^* m_a \mathbf{v}_a^*$ and $E_a^* = \gamma_a^* m_a c^2$, giving
$$
v_a^* = \frac{p^*c^2}{E_a^*},
\qquad
\tanh\psi_a^* = \frac{p^*c}{E_a^*} .
$$

**Threshold.** A physical parent always has $M > |m_1 - m_2|$, so the second factor under the square root is positive. The radicand is therefore non-negative exactly when $M \ge m_1 + m_2$. At $M = m_1 + m_2$ one has $p^* = 0$ and $E_a^* = m_ac^2$: the daughters emerge at rest, and the decay has no kinetic energy to distribute. Hence the decay is kinematically allowed if and only if $M \ge m_1 + m_2$, i.e. if and only if the released energy
$$
Q := (M - m_1 - m_2)c^2
$$
is non-negative.

**Released energy.** The kinetic energies $K_a := E_a^* - m_ac^2$ satisfy
$$
K_1 + K_2 = (E_1^* + E_2^*) - (m_1 + m_2)c^2 = Q ,
$$
so $Q$ is exactly the total kinetic energy of the daughters in the parent rest frame. An exact rearrangement used in Problem 6 is
$$
K_1 = \frac{Q\left(2m_2 + Q/c^2\right)}{2M},
\qquad
K_2 = \frac{Q\left(2m_1 + Q/c^2\right)}{2M},
$$
obtained from $K_1 = E_1^* - m_1c^2 = \left[(M-m_1)^2 - m_2^2\right]c^2/(2M)$ by writing $M - m_1 - m_2 = Q/c^2$ and $M - m_1 + m_2 = 2m_2 + Q/c^2$.

## Problem 2: The Moving Parent and the Boost Biquaternion

**Statement.** Let the parent have four-momentum
$$
\tilde{P}_A = i\frac{E}{c}\,e_0 + \mathbf{P},
\qquad
E = \Gamma Mc^2,
\qquad
\mathbf{P} = \Gamma M\mathbf{V},
\qquad
\Gamma = \frac{1}{\sqrt{1 - V^2/c^2}},
$$
in the laboratory, so that $\mathbf{V}$ is the parent's velocity in the lab. (a) Construct the boost biquaternion $\tilde{\Lambda}_{\rm CM}$ that carries the lab to the COM frame, and verify $\tilde{\Lambda}_{\rm CM}\tilde{P}_A\tilde{\Lambda}_{\rm CM}^\dagger = iMc\,e_0$. (b) Identify the rotor that carries the COM daughter four-momenta to the lab. (c) Obtain the lab energies and momenta and the range of a daughter's lab energy.

**Solution (a).** From $\bar{\tilde{P}}_A = iE/c\,e_0 - \mathbf{P}$,
$$
-\frac{i}{Mc}\bar{\tilde{P}}_A
= \frac{E}{Mc^2}e_0 + i\frac{\mathbf{P}}{Mc}
= \cosh\Psi\,e_0 + i\sinh\Psi\,\hat{\mathbf{V}},
$$
with $\cosh\Psi = E/(Mc^2) = \Gamma$, $\sinh\Psi = |\mathbf{P}|/(Mc) = \Gamma V/c$, hence $\tanh\Psi = V/c$. This is an element of $\mathbb{M}_+$ of unit norm form, since $\cosh^2\Psi - \sinh^2\Psi = 1$. Its principal square root, with $\mathrm{Sc} > 0$, is the boost biquaternion
$$
\tilde{\Lambda}_{\rm CM} = \sqrt{-\frac{i}{Mc}\bar{\tilde{P}}_A}
= \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\,\hat{\mathbf{V}},
\qquad
\tilde{\Lambda}_{\rm CM}\bar{\tilde{\Lambda}}_{\rm CM} = e_0 .
$$
To verify that it rotates $\tilde{P}_A$ to $iMc\,e_0$, use the component action of the rotor with parameter $\hat{\mathbf{V}}$, which is the boost to the frame moving with velocity $\mathbf{V}$. On a four-momentum $(E', \mathbf{P}')$ it acts as
$$
E'' = \Gamma\left(E' - \mathbf{V}\cdot\mathbf{P}'\right),
\qquad
\mathbf{P}'' = \mathbf{P}' + \frac{\Gamma-1}{V^2}\left(\mathbf{V}\cdot\mathbf{P}'\right)\mathbf{V} - \Gamma\frac{E'}{c^2}\mathbf{V}.
$$
Inserting $E' = E = \Gamma Mc^2$ and $\mathbf{P}' = \mathbf{P} = \Gamma M\mathbf{V}$ gives
$$
E'' = \Gamma\left(\Gamma Mc^2 - \Gamma MV^2\right) = \Gamma^2 Mc^2\left(1 - V^2/c^2\right) = Mc^2,
$$
and, using $\mathbf{V}\cdot\mathbf{P} = \Gamma MV^2$,
$$
\mathbf{P}'' = \Gamma M\mathbf{V} + (\Gamma-1)\Gamma M\mathbf{V} - \Gamma^2 M\mathbf{V} = 0 .
$$
Hence $\tilde{\Lambda}_{\rm CM}\tilde{P}_A\tilde{\Lambda}_{\rm CM}^\dagger = iMc\,e_0$, which is precisely the statement that $\tilde{\Lambda}_{\rm CM}$ is the boost to the COM frame.

**Solution (b).** The rotation generated by $\tilde{\Lambda}_{\rm CM}$ carries the lab to the COM frame. The inverse rotation is generated by the quaternion conjugate,
$$
\bar{\tilde{\Lambda}}_{\rm CM} = \cosh\frac{\Psi}{2} - i\sinh\frac{\Psi}{2}\,\hat{\mathbf{V}}
= \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\,(-\hat{\mathbf{V}}),
$$
which is the boost biquaternion of the same rapidity in the opposite direction. The COM daughter four-momenta are therefore carried to the laboratory by
$$
\tilde{P}_a = \bar{\tilde{\Lambda}}_{\rm CM}\,\tilde{P}_a^*\,\bar{\tilde{\Lambda}}_{\rm CM}^\dagger .
$$

> **Remark on the parent's boost convention.** The parent writes the star-to-lab rotation as $\tilde{P}_a = \tilde{\Lambda}\tilde{P}_a^*\tilde{\Lambda}^\dagger$ with $\tilde{\Lambda} = \cosh\frac{\Psi}{2} - i\sinh\frac{\Psi}{2}\hat{\mathbf{V}}$, the quaternion conjugate of the rotor that carries the laboratory frame to the parent rest frame - the sign of the vector part being opposite to that of the lab-to-rest rotor, as the parent states. That rotor produces $E_a = \gamma(E_a^* + \mathbf{V}\cdot\mathbf{p}_a^*)$, in agreement with the component formula quoted immediately below it in the parent; the biquaternion and component forms therefore agree. We work with the physical convention, in which a forward-emitted daughter ($\mathbf{V}\cdot\mathbf{p}_a^* > 0$) gains energy, and which corresponds to the inverse rotor above.

**Solution (c).** Applying the component form of the rotation with the inverse rotor — equivalently, the standard Lorentz transformation with velocity $\mathbf{V}$ — gives
$$
E_a = \gamma\left(E_a^* + \mathbf{V}\cdot\mathbf{p}_a^*\right),
\qquad
\mathbf{p}_a = \mathbf{p}_a^* + \frac{\gamma-1}{V^2}\left(\mathbf{V}\cdot\mathbf{p}_a^*\right)\mathbf{V} + \gamma\frac{E_a^*}{c^2}\mathbf{V},
$$
with $\gamma = \cosh\Psi = \Gamma$. Writing $\cos\theta_a^*$ for the angle between $\mathbf{V}$ and $\mathbf{p}_a^*$, and using $v_a^* = p^*c^2/E_a^*$,
$$
E_a = \gamma E_a^*\left(1 + \frac{Vv_a^*}{c^2}\cos\theta_a^*\right).
$$
Hence for a fixed daughter the lab energy lies in the range
$$
\gamma E_a^*\left(1 - \frac{Vv_a^*}{c^2}\right)
\;\le\; E_a \;\le\;
\gamma E_a^*\left(1 + \frac{Vv_a^*}{c^2}\right),
$$
the upper end being forward emission and the lower end backward emission. The two lab four-momenta still sum to $\tilde{P}_A$, because the rotation is linear:
$$
\bar{\tilde{\Lambda}}_{\rm CM}\left(\tilde{P}_1^* + \tilde{P}_2^*\right)\bar{\tilde{\Lambda}}_{\rm CM}^\dagger
= \bar{\tilde{\Lambda}}_{\rm CM}\left(iMc\,e_0\right)\bar{\tilde{\Lambda}}_{\rm CM}^\dagger
= \tilde{P}_A .
$$

## Problem 3: The Invariant Mass of Each Pair in a Three-Body Decay

**Statement.** Let $A \to 1 + 2 + 3$, with the parent at rest. For each pair define $M_{ij}$ by
$$
N\!\left(\tilde{P}_i + \tilde{P}_j\right) = -M_{ij}^2c^2, \qquad M_{ij} \ge 0 .
$$
(a) Express $M_{ij}$ through the invariant pairing. (b) Show that $M_{12}^2c^4 = (Mc^2 - E_3^*)^2 - p_3^{*2}c^2$. (c) Find the range of $M_{12}$. (d) Establish the sum rule $\sum_{i<j} M_{ij}^2 = M^2 + m_1^2 + m_2^2 + m_3^2$.

**Solution (a).** Because $N$ is a quadratic form with polarization $\langle \cdot, \cdot\rangle$,
$$
N\!\left(\tilde{P}_i + \tilde{P}_j\right) = N(\tilde{P}_i) + N(\tilde{P}_j) + 2\langle \tilde{P}_i, \tilde{P}_j\rangle,
$$
and with $N(\tilde{P}_i) = -m_i^2c^2$ this gives
$$
M_{ij}^2c^2 = m_i^2c^2 + m_j^2c^2 - 2\langle \tilde{P}_i, \tilde{P}_j\rangle .
$$
This is the parent's definition of the invariant mass of a pair, applied to a partial sum of three four-momenta. It requires only that $\mathbb{M}_-$ is a real vector space closed under addition and that $N$ be a quadratic form; no new primitive is needed. (The parent defines the pair mass for a two-body total; the same definition applied to a subset of a three-body system is the natural extension used in Dalitz-plot kinematics.)

**Solution (b).** In the parent rest frame the three momenta sum to zero, $\mathbf{p}_1^* + \mathbf{p}_2^* + \mathbf{p}_3^* = 0$, so with $\tilde{P}_{12} = \tilde{P}_1 + \tilde{P}_2$,
$$
N\!\left(\tilde{P}_{12}\right) = \left(i\frac{E_1^* + E_2^*}{c}\right)^2 + \left(\mathbf{p}_1^* + \mathbf{p}_2^*\right)^2
= -\frac{\left(Mc^2 - E_3^*\right)^2}{c^2} + p_3^{*2},
$$
where we used $\mathbf{p}_1^* + \mathbf{p}_2^* = -\mathbf{p}_3^*$ and $E_1^* + E_2^* = Mc^2 - E_3^*$. Hence
$$
M_{12}^2c^4 = \left(Mc^2 - E_3^*\right)^2 - p_3^{*2}c^2
= M^2c^4 + m_3^2c^4 - 2Mc^2E_3^*,
$$
the second equality using $E_3^{*2} = m_3^2c^4 + p_3^{*2}c^2$. The pair mass is thus fixed by the energy of the third particle.

**Solution (c).** Because $M_{12}$ is invariant, it may be evaluated in the parent rest frame, where it is a function of $E_3^*$ alone. The energy $E_3^*$ has a minimum $m_3c^2$, attained when $\mathbf{p}_3^* = 0$, and a maximum
$$
E_3^{*\max} = \frac{\left[M^2 + m_3^2 - (m_1+m_2)^2\right]c^2}{2M},
$$
attained when $\mathbf{p}_1^* = -\mathbf{p}_2^*$, that is, when the pair $(1,2)$ is at relative rest and the decay is effectively the two-body decay $A \to (12) + 3$ with the composite mass $m_1 + m_2$. Since $M_{12}^2c^4 = M^2c^4 + m_3^2c^4 - 2Mc^2E_3^*$ decreases with $E_3^*$, the endpoints are
$$
M_{12}^{\max} = M - m_3 \quad \left(\text{at } E_3^* = m_3c^2\right),
\qquad
M_{12}^{\min} = m_1 + m_2 \quad \left(\text{at } E_3^{*\max}\right),
$$
so that $(m_1+m_2) \le M_{12} \le M - m_3$, with the cyclic permutations for the other two pairs. These are the three boundary curves of the Dalitz plot.

**Solution (d).** Summing the squared pair masses and using part (a),
$$
\sum_{i<j} M_{ij}^2c^2 = 2\sum_i m_i^2c^2 - 2\sum_{i<j}\langle \tilde{P}_i, \tilde{P}_j\rangle .
$$
The bilinearity of the pairing gives
$$
\sum_{i<j}\langle \tilde{P}_i, \tilde{P}_j\rangle
= \tfrac12\left(\left\langle \sum_i \tilde{P}_i, \sum_j \tilde{P}_j\right\rangle - \sum_i \langle \tilde{P}_i, \tilde{P}_i\rangle\right)
= \tfrac12\left(N(\tilde{P}_A) - \sum_i N(\tilde{P}_i)\right)
= \tfrac12\left(-M^2c^2 + \sum_i m_i^2c^2\right),
$$
where $\sum_i \tilde{P}_i = \tilde{P}_A$ and the pairing is evaluated by polarization at the total four-momentum. Substituting,
$$
\sum_{i<j} M_{ij}^2c^2 = 2\sum_i m_i^2c^2 + M^2c^2 - \sum_i m_i^2c^2
= M^2c^2 + \sum_i m_i^2c^2,
$$
that is,
$$
\sum_{i<j} M_{ij}^2 = M^2 + m_1^2 + m_2^2 + m_3^2 .
$$
As a check, for $M = 100$, $(m_1,m_2,m_3) = (20,30,40)$ the right-hand side is $12900$; a direct evaluation of the three pair masses at a sample configuration (for instance the configuration with $\mathbf{p}_3^* = 0$, where $M_{12} = 60$) reproduces the same total.

## Problem 4: Threshold and the Opening Angle

**Statement.** (a) State the threshold condition and show that it follows from $p^{*2} \ge 0$. (b) Show that the opening angle between the daughters in the COM frame is $\pi$. (c) Derive the laboratory angle of a daughter. (d) For two massless daughters, derive the minimum opening angle $\Theta_{\min} = \arccos(1 - 2/\gamma^2)$ and its beamed limit.

**Solution (a).** Problem 1 gives
$$
p^{*2}c^2 = \frac{c^4}{4M^2}\left[M^2 - (m_1+m_2)^2\right]\left[M^2 - (m_1-m_2)^2\right].
$$
Since $M > |m_1 - m_2|$ for any physical parent, the second factor is positive, and the condition $p^{*2} \ge 0$ is equivalent to
$$
M \ge m_1 + m_2 \iff Q \ge 0 .
$$
At threshold $Q = 0$, $p^* = 0$, and the daughters emerge with no relative motion. Below threshold there is no solution of $\tilde{P}_A = \tilde{P}_1 + \tilde{P}_2$ with all four-momenta on the future mass shell and real momenta.

**Solution (b).** In the COM frame the momenta are back to back, $\mathbf{p}_1^* = -\mathbf{p}_2^*$, so the opening angle $\Theta^*$ between them satisfies
$$
\cos\Theta^* = \frac{\mathbf{p}_1^*\cdot\mathbf{p}_2^*}{p^{*2}} = -1,
\qquad \Theta^* = \pi .
$$
The daughters are collinear and oppositely directed.

**Solution (c).** Boost to the lab with the parent's velocity $\mathbf{V}$ along $\hat{\mathbf{z}}$, and let $\theta^*$ be the angle between $\mathbf{p}^*$ and $\mathbf{V}$ for daughter 1. From Problem 2 its lab momentum components perpendicular to and along $\mathbf{V}$ are
$$
p_{1\perp} = p^*\sin\theta^*,
\qquad
p_{1\parallel} = \gamma\left(p^*\cos\theta^* + \frac{VE_1^*}{c^2}\right),
$$
so the lab angle $\theta_1$ measured from $\mathbf{V}$ satisfies
$$
\tan\theta_1 = \frac{p^*\sin\theta^*}{\gamma\left(p^*\cos\theta^* + VE_1^*/c^2\right)}
= \frac{\sin\theta^*}{\gamma\left(\cos\theta^* + \beta/\beta_1^*\right)},
$$
where $\beta = V/c$ and $\beta_a^* = p^*c/E_a^* = v_a^*/c$ is the daughter's speed in the COM frame. For a massless daughter $\beta_a^* = 1$, and the angle is the classic result
$$
\tan\theta_a = \frac{\sin\theta^*}{\gamma\left(\cos\theta^* + \beta\right)} .
$$

**Solution (d).** For two massless daughters (for example $\pi^0 \to \gamma\gamma$) one has $E_1^* = E_2^* = Mc^2/2$ and $p^* = Mc/2$, so $\beta_a^* = 1$. Emit the two photons at COM angles $\theta^*$ and $\pi - \theta^*$ relative to $\mathbf{V}$; their lab angles $\theta_1, \theta_2$ measured from $\mathbf{V}$ obey the formula of part (c), and the opening angle is $\Theta = \theta_1 + \theta_2$. A direct calculation gives
$$
\cos\Theta = \frac{\gamma^2 - 2 - \gamma^2\beta^2\cos^2\theta^*}{\gamma^2\left(1 - \beta^2\cos^2\theta^*\right)} .
$$
As $\cos^2\theta^*$ runs from $0$ to $1$ this expression decreases monotonically, its derivative with respect to $\cos^2\theta^*$ being $-\,2\beta^2/\left[\gamma^2\left(1 - \beta^2\cos^2\theta^*\right)^2\right]$, which is negative for $\gamma > 1$. Hence $\cos\Theta$ is largest at $\cos\theta^* = 0$ (symmetric emission) and smallest at $\cos^2\theta^* = 1$ (collinear emission). The **minimum** opening angle is therefore
$$
\cos\Theta_{\min} = 1 - \frac{2}{\gamma^2},
\qquad
\Theta_{\min} = \arccos\!\left(1 - \frac{2}{\gamma^2}\right),
\qquad
\tan\frac{\Theta_{\min}}{2} = \frac{1}{\gamma\beta},
$$
and the **maximum** is $\Theta = \pi$. For $\gamma \gg 1$, $\Theta_{\min} \approx 2/\gamma$, the familiar collimation of the decay products into a cone of half-angle $1/\gamma$ about the parent's direction. Numerically $\Theta_{\min} = 60.00^\circ$ at $\gamma = 2$ and $23.07^\circ$ at $\gamma = 5$, the latter within $0.7\%$ of $2/\gamma$ radians. For massive daughters the single-daughter formula of part (c) still holds (with $\beta_a^* < 1$), but the opening angle is then a more complicated function of $\theta^*$.

## Problem 5: A Numerical Instance

**Statement.** Evaluate the two-body formulas for $K^+ \to \pi^+ \pi^0$, and for the limits $\pi^0 \to \gamma\gamma$ (two massless daughters) and $\pi^+ \to \mu^+ \nu_\mu$ (one massless daughter). Compare with the non-relativistic approximation.

**Solution.** We use the standard masses $m_{K^+} = 493.677$, $m_{\pi^+} = 139.57039$, $m_{\pi^0} = 134.9768$, $m_\mu = 105.6583755$ MeV$/c^2$, and set $c = 1$ so that energies are in MeV.

For $K^+ \to \pi^+\pi^0$, with $M = m_{K^+}$, $m_1 = m_{\pi^+}$, $m_2 = m_{\pi^0}$:
$$
Q = 219.1298\ \text{MeV},
$$
$$
E_1^* = E_{\pi^+}^* = 248.1158\ \text{MeV},
\qquad
E_2^* = E_{\pi^0}^* = 245.5612\ \text{MeV},
\qquad
E_1^* + E_2^* = 493.6770\ \text{MeV} = Mc^2,
$$
$$
p^*c = 205.1379\ \text{MeV},
\qquad
v_{\pi^+}^*/c = 0.826783,
\qquad
v_{\pi^0}^*/c = 0.835384 .
$$
The kinetic energies are $K_{\pi^+} = 108.5454$ MeV and $K_{\pi^0} = 110.5844$ MeV, whose sum is $219.1298$ MeV $= Q$, as required; the mass-shell residual $E_{\pi^+}^{*2} - m_{\pi^+}^2c^4 - p^{*2}c^2$ vanishes to round-off.

The non-relativistic approximation of Problem 6 gives, with $\mu = m_1m_2/(m_1+m_2) = 68.6176$ MeV,
$$
p^*_{\rm NR}c = \sqrt{2\mu Q} = 173.4137\ \text{MeV},
$$
which is low by $15.46\%$; and the partition $K_1/Q$ is $0.495348$ exactly, against the approximation $m_2/(m_1+m_2) = 0.491634$, an error of $0.75\%$. The momentum formula is poor here because $Q/(m_1+m_2) \approx 0.80$, far from the non-relativistic regime.

A decay with a smaller release, $\Lambda \to p\pi^-$ ($M = 1115.683$, $m_p = 938.2721$, $m_{\pi^-} = 139.5704$ MeV$/c^2$, so $Q = 37.8405$ MeV, only $3.51\%$ of the mass sum), illustrates the opposite regime:
$$
E_p^* = 943.6476\ \text{MeV},
\qquad
E_{\pi^-}^* = 172.0354\ \text{MeV},
\qquad
p^*c = 100.5797\ \text{MeV},
$$
$$
v_p^*/c = 0.106586,
\qquad
v_{\pi^-}^*/c = 0.584645,
\qquad
\frac{K_p}{Q}\Big|_{\rm exact} = 0.142057,
\qquad
\frac{m_{\pi^-}}{m_p+m_{\pi^-}} = 0.129491 .
$$
Here $\sqrt{2\mu Q} = 95.8908$ MeV, low by $4.66\%$, and the partition is in error by $8.9\%$.

The two limiting checks confirm the formula in the regime $\beta_a^* = 1$. For the massless decay $\pi^0 \to \gamma\gamma$ ($M = m_{\pi^0} = 134.9768$ MeV$/c^2$),
$$
E_\gamma^* = p^*c = \frac{Mc^2}{2} = 67.4884\ \text{MeV},
\qquad Q = Mc^2 .
$$
For $\pi^+ \to \mu^+\nu_\mu$ with a massless neutrino ($M = m_{\pi^+} = 139.57039$, $m_1 = m_\mu = 105.6583755$, $m_2 = 0$ MeV$/c^2$),
$$
E_\mu^* = 109.7782\ \text{MeV},
\qquad
E_\nu^* = 29.7921\ \text{MeV},
\qquad
p^*c = 29.7921\ \text{MeV},
\qquad
v_\mu^*/c = 0.271385,
$$
with $Q = 33.9120$ MeV and $K_\mu = 4.1199$ MeV. In this decay $\mu = 0$, so the non-relativistic momentum formula $\sqrt{2\mu Q}$ vanishes and fails completely: a massless, necessarily ultrarelativistic daughter lies outside the non-relativistic limit.

## Problem 6: The Non-Relativistic Limit

**Statement.** Expand the exact formulas of Problems 1 and 2 for $Q \ll (m_1+m_2)c^2$, recovering the Newtonian partition of the released energy, the momentum $p^* \approx \sqrt{2\mu Q}$, and Galilean velocity addition for the moving parent. Quantify the accuracy of the limit.

**Solution.** Write
$$
M = m_1 + m_2 + \frac{Q}{c^2},
\qquad
\mu = \frac{m_1m_2}{m_1+m_2} .
$$

**Energies.** From $K_1 = Q(2m_2 + Q/c^2)/(2M)$ and $2M = 2(m_1+m_2) + O(Q/c^2)$,
$$
K_1 = \frac{m_2}{m_1+m_2}\,Q + O\!\left(\frac{Q^2}{(m_1+m_2)c^2}\right),
\qquad
K_2 = \frac{m_1}{m_1+m_2}\,Q + O\!\left(\frac{Q^2}{(m_1+m_2)c^2}\right),
$$
so the light daughter carries the larger share of the released energy — the parent's non-relativistic decay result.

**Momentum.** The two factors under the square root are
$$
M^2 - (m_1+m_2)^2 = \frac{Q}{c^2}\left(2(m_1+m_2) + \frac{Q}{c^2}\right),
\qquad
M^2 - (m_1-m_2)^2 = \left(2m_1 + \frac{Q}{c^2}\right)\left(2m_2 + \frac{Q}{c^2}\right).
$$
Keeping the leading term in each,
$$
p^* \approx \frac{c}{2M}\sqrt{\frac{Q}{c^2}\,2(m_1+m_2)\cdot 4m_1m_2}
= \sqrt{\frac{2Qm_1m_2}{m_1+m_2}}
= \sqrt{2\mu Q}.
$$
Equivalently, since $v_a^* = p^*c^2/E_a^* \approx p^*/m_a$ and the daughters move oppositely, the relative speed is $v_{\rm rel} = v_1^* + v_2^* = p^*(1/m_1 + 1/m_2) = p^*/\mu$, so
$$
p^* \approx \mu\,v_{\rm rel},
$$
in agreement with the parent's non-relativistic COM momentum. The kinetic energies follow as $K_a \approx p^{*2}/(2m_a)$; using $p^{*2} = 2\mu Q$ reproduces the partition above, and $Q \approx \tfrac12 \mu v_{\rm rel}^2$ makes contact with the parent's relative-rapidity relation $Mc^2 = (m_1+m_2)c^2 + \tfrac12\mu v_{\rm rel}^2 + O(v_{\rm rel}^4/c^2)$.

**Moving parent.** Expanding the lab formulas of Problem 2 for $V, v_a^* \ll c$,
$$
E_a = \gamma\left(E_a^* + \mathbf{V}\cdot\mathbf{p}_a^*\right) \approx m_ac^2 + \tfrac12 m_a\left|\mathbf{V} + \mathbf{v}_a^*\right|^2,
\qquad
\mathbf{p}_a \approx m_a\left(\mathbf{V} + \mathbf{v}_a^*\right),
$$
so the daughter velocities add Galileanly, and the total lab momentum is
$$
\sum_a \mathbf{p}_a \approx (m_1+m_2)\mathbf{V} + m_1\mathbf{v}_1^* + m_2\mathbf{v}_2^* = (m_1+m_2)\mathbf{V},
$$
because $\mathbf{p}_1^* = -\mathbf{p}_2^*$ implies $m_1\mathbf{v}_1^* + m_2\mathbf{v}_2^* = 0$ at leading order. This is the Newtonian statement that the parent moves with velocity $\mathbf{V}$ while the daughters share the released energy in their relative motion.

**Accuracy.** The expansions carry relative errors of order $Q/((m_1+m_2)c^2)$ and $v_a^{*2}/c^2$. Problem 5 makes this concrete: for $\Lambda \to p\pi^-$ ($Q/(m_1+m_2) \approx 3.5\%$) the momentum approximation is good to $4.7\%$ and the energy partition to $8.9\%$; for $K^+ \to \pi^+\pi^0$ ($Q/(m_1+m_2) \approx 0.80$) the momentum approximation already fails at the $15\%$ level. The limit requires both daughters to be non-relativistic, so it fails outright when one daughter is massless.

## Summary

We have worked the relativistic kinematics of a two-body decay as an application of the two-body article.

1. **COM frame ($A$ at rest).** The daughters are back to back with $E_1^* + E_2^* = Mc^2$, individual energies $E_a^* = (M^2 + m_a^2 - m_b^2)c^2/(2M)$, common momentum $p^* = \frac{c}{2M}\sqrt{[M^2-(m_1+m_2)^2][M^2-(m_1-m_2)^2]}$, speeds $v_a^* = p^*c^2/E_a^*$, and released energy $Q = (M-m_1-m_2)c^2 = K_1 + K_2$. The decay is allowed iff $M \ge m_1 + m_2$.

2. **Moving parent.** The parent constructs $\tilde{\Lambda}_{\rm CM} = \sqrt{-i\bar{\tilde{P}}_A/(Mc)} = \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\hat{\mathbf{V}}$, which carries the lab to the COM frame; the inverse rotation, which carries the COM daughters to the lab, is generated by the quaternion conjugate $\bar{\tilde{\Lambda}}_{\rm CM}$. It gives $E_a = \gamma(E_a^* + \mathbf{V}\cdot\mathbf{p}_a^*)$ and the standard momentum formula, with the lab energy of each daughter confined to $\gamma E_a^*(1 \pm Vv_a^*/c^2)$.

3. **Three-body decay.** The pair mass is $M_{ij}^2c^2 = m_i^2c^2 + m_j^2c^2 - 2\langle\tilde{P}_i,\tilde{P}_j\rangle$; equivalently $M_{12}^2c^4 = (Mc^2 - E_3^*)^2 - p_3^{*2}c^2$, with $(m_1+m_2) \le M_{12} \le M - m_3$ and $\sum_{i<j}M_{ij}^2 = M^2 + m_1^2 + m_2^2 + m_3^2$.

4. **Threshold and opening angle.** The threshold is $M \ge m_1+m_2$; in the COM frame the opening angle is $\pi$, and for two massless daughters the lab opening angle has minimum $\Theta_{\min} = \arccos(1 - 2/\gamma^2) \approx 2/\gamma$ at symmetric emission.

5. **Numbers.** For $K^+ \to \pi^+\pi^0$ the exact values are $p^*c = 205.1379$ MeV and $K_{\pi^+} = 108.5454$ MeV, $K_{\pi^0} = 110.5844$ MeV; for $\Lambda \to p\pi^-$, $p^*c = 100.5797$ MeV. The massless limits $\pi^0 \to \gamma\gamma$ and $\pi^+ \to \mu^+\nu_\mu$ reproduce $E_\gamma^* = Mc^2/2$ and the standard pion-decay energies.

6. **Non-relativistic limit.** The exact formulas reduce to $K_a \approx (m_b/(m_1+m_2))Q$, $p^* \approx \sqrt{2\mu Q} = \mu v_{\rm rel}$, and Galilean velocity addition, with relative errors of order $Q/((m_1+m_2)c^2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $c$, $c_0$ | Speed of light in the medium, and in vacuum |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\langle\tilde{A},\tilde{B}\rangle = \mathrm{Sc}(\tilde{A}\bar{\tilde{B}})$ | Invariant pairing on $\mathbb{M}_-$ |
| $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$ | Four-momentum, $N(\tilde{P}) = -m^2c^2$ |
| $\tilde{u} = \tilde{U}/c$ | Unit four-velocity, $N(\tilde{u}) = -1$ |
| $\tilde{\Lambda}_{\rm CM} = \sqrt{-i\bar{\tilde{P}}_A/(Mc)}$ | Boost biquaternion, lab to COM frame |
| $\bar{\tilde{\Lambda}}_{\rm CM}$ | Quaternion conjugate, COM to lab |
| $\Psi$ | COM rapidity, $\tanh\Psi = V/c$ |
| $M$, $m_1$, $m_2$ | Parent and daughter masses |
| $Q = (M-m_1-m_2)c^2$ | Released energy |
| $E_a^*$, $\mathbf{p}_a^*$, $p^*$ | COM energies, momenta, common magnitude |
| $v_a^* = p^*c^2/E_a^*$ | COM daughter speeds |
| $\beta = V/c$, $\beta_a^* = v_a^*/c$ | Dimensionless speeds |
| $M_{ij}$ | Invariant mass of pair $(i,j)$ |
| $\Theta$, $\Theta_{\min}$ | Lab opening angle and its minimum |
| $\mu = m_1m_2/(m_1+m_2)$ | Non-relativistic reduced mass |
| $\gamma = \cosh\Psi$ | Lorentz factor of the parent in the lab |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard relativistic two-body kinematics and invariant masses.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Lorentz transformation of four-momenta and fixed-target kinematics.
- Particle Data Group, *Review of Particle Physics*, for the particle masses used in Problem 5.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra treatment of relativistic rotors and multiparticle kinematics.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original spacetime-algebra formulation of relativistic mechanics.
- The companion articles of this series: *Relativistic Mechanics in Biquaternionic Form*, *The Lorentz Transformation as a Biquaternionic Rotation*, and *The Relativistic Two-Body Problem in Biquaternionic Form*.
