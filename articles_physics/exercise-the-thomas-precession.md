# __Exercise: The Thomas Precession__

## Introduction

This is one of the worked exercises in the relativity series. It applies the boost biquaternion and the rotor conjugation of *The Lorentz Transformation as a Biquaternionic Rotation*, the four-velocity and the four-force of *Relativistic Mechanics in Biquaternionic Form*, the Thomas–Wigner angle of *The Lorentz Group in Biquaternionic Form — Structure and Representations*, and the discrete composition carried out in *Exercise: Boosting a Four-Velocity and Rapidity Composition*. No new formalism is introduced.

The discrete Thomas–Wigner rotation is already in the corpus: the product of two non-collinear boost rotors is a boost times a rotation, and its angle is known. This exercise takes only the distinct part of the subject — the **continuous limit**. A particle that is accelerated has a different instantaneous rest frame at every instant. Two rest frames a lab-time interval $dt$ apart are related by a Wigner rotation, and the limit $dt\to0$ defines an angular velocity, the **Thomas precession** $\boldsymbol{\omega}_T$. The exercise derives that rate, fixes its direction by a computation on a geometry that can actually see the direction, and connects it to the factor $\tfrac12$ in the spin–orbit coupling.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_1e_2=e_3$, and the scalar imaginary $i$ with $i^2=-1$, commuting with every $e_k$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part, the material sector), the Hermitian subspace $\mathbb{M}_+$ (real scalar part, imaginary vector part, the informational sector), with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ of the rotation rotors, and the complex scalar subspace $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$, the center of the algebra. The norm form $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$, the quaternion conjugate $\bar{\tilde{Q}}$, the Hermitian conjugate $\tilde{Q}^\dagger=\bar{\tilde{Q}}^{*}$, and the rotor conjugation $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged, but no object of the informational sector arises below, so it is recorded and not used. The four-velocity $\tilde{U}=\gamma(ic\,e_0+\mathbf{v})$ with $N(\tilde{U})=-c^2$ and $\gamma=(1-\mathbf{v}^2/c^2)^{-1/2}$, the four-momentum $\tilde{P}=m\tilde{U}=iE/c\,e_0+\mathbf{p}$, and the four-force $\tilde{F}=d\tilde{P}/d\tau \in \mathbb{M}_-$. The boost biquaternion
$$
\tilde{\Lambda}_{\mathbf{u}}=\cosh\frac{\psi_u}{2}+i\sinh\frac{\psi_u}{2}\hat{\mathbf{u}},
\qquad \tanh\psi_u=\frac{u}{c},
$$
which is Hermitian, lies in $\mathbb{M}_+$, and has unit norm form. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value; $\mathbf{v}$ is the particle velocity, $\mathbf{a}=d\mathbf{v}/dt$ its lab acceleration, and $\hat{\mathbf{u}}$ is a unit direction. Components are taken in the basis $(e_0,e_1,e_2,e_3)$.

**The boost-rotor direction, stated once.** In this series the rotor $\tilde{\Lambda}_{\mathbf{u}}$ is the **lab-to-frame** rotor: acting on a four-vector by $\tilde{X}\mapsto\tilde{\Lambda}_{\mathbf{u}}\tilde{X}\tilde{\Lambda}_{\mathbf{u}}^\dagger$, it carries the lab to the frame moving with $+\mathbf{u}$, and for the particle four-velocity $\tilde{U}$ it is the lab-to-rest rotor that satisfies $\tilde{\Lambda}_{\mathbf{v}}\tilde{U}\tilde{\Lambda}_{\mathbf{v}}^\dagger = ic\,e_0$. Its quaternion conjugate is the inverse, $\bar{\tilde{\Lambda}}_{\mathbf{u}}=\tilde{\Lambda}_{\mathbf{u}}^{-1}=\tilde{\Lambda}_{-\mathbf{u}}$. This direction is *not* stated in the parent article; it is the gap recorded in *Exercise: Boosting a Four-Velocity and Rapidity Composition*, Problem 4. Problem 3 below checks what that ambiguity does and does not do to the Thomas-precession sign.

**What is to be shown.** Problem 1 identifies the rotor that relates two neighbouring instantaneous rest frames. Problem 2 takes the continuous limit and derives the Thomas precession rate $\boldsymbol{\omega}_T$. Problem 3 checks the sign on a non-collinear geometry, where alone the sign is visible, and separates the manipulations that flip it from those that do not. Problem 4 treats uniform circular motion, recovers the retrograde rotation and the "Thomas half", and connects the result to the spin–orbit coupling. Problem 5 states what the parent articles do and do not supply.

## Problem 1: The Rotor Between Two Neighbouring Rest Frames

**Statement.** Let a particle have lab velocity $\mathbf{v}(t)$ and let $\tilde{\Lambda}_{\mathbf{v}}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{v}}$, with $\tanh\psi=v/c$, be its lab-to-rest boost rotor.

**(a)** Show that the rest frame at lab time $t+dt$ is related to the rest frame at time $t$ by the rotor
$$
\tilde{M}=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}\,\tilde{\Lambda}_{\mathbf{v}}^{-1}
=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}\,\bar{\tilde{\Lambda}}_{\mathbf{v}} .
\tag{1}
$$

**(b)** Show that $\tilde{M}$ is a unit-norm biquaternion and admits the polar decomposition
$$
\tilde{M}=\tilde{B}\tilde{R},\qquad \tilde{B}\in\mathbb{M}_+\ \text{a pure boost},\qquad \tilde{R}\in\mathbb{H}_{\mathbb{B}}\ \text{a rotation},
\tag{2}
$$
and identify $\tilde{R}$ as the Thomas–Wigner rotation of the interval $dt$.

**(c)** Express the angle and axis of $\tilde{R}$ through the parent's Wigner-angle formula.

**Solution. (a)** The rotor $\tilde{\Lambda}_{\mathbf{v}}$ carries the lab to the rest frame at time $t$: by the parent's relation $\tilde{\Lambda}_{\mathbf{v}}=\sqrt{-\tfrac{i}{c}\bar{\tilde{U}}}$, one has $\tilde{\Lambda}_{\mathbf{v}}\tilde{U}\tilde{\Lambda}_{\mathbf{v}}^\dagger=ic\,e_0$, and every four-vector $\tilde{X}$ has components
$$
\tilde{X}'=\tilde{\Lambda}_{\mathbf{v}}\tilde{X}\tilde{\Lambda}_{\mathbf{v}}^\dagger
\tag{3}
$$
in that rest frame. At $t+dt$ the same construction with $\mathbf{v}+d\mathbf{v}$ gives $\tilde{X}''=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}\tilde{X}\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}^\dagger$. Since $\tilde{\Lambda}_{\mathbf{v}}$ is Hermitian and of unit norm, $\tilde{\Lambda}_{\mathbf{v}}^\dagger=\tilde{\Lambda}_{\mathbf{v}}$ and $\tilde{\Lambda}_{\mathbf{v}}^\dagger\tilde{\Lambda}_{\mathbf{v}}=e_0$, so
$$
\tilde{X}''=\tilde{M}\,\tilde{X}'\,\tilde{M}^\dagger,
\qquad
\tilde{M}=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}\tilde{\Lambda}_{\mathbf{v}}^{-1},
$$
which is (1). The direction matters: $\tilde{\Lambda}_{\mathbf{v}}^{-1}=\bar{\tilde{\Lambda}}_{\mathbf{v}}=\tilde{\Lambda}_{-\mathbf{v}}$ is the inverse boost, not the same boost.

**(b)** The product of two unit-norm biquaternions is unit-norm, so $N(\tilde{M})=e_0$. The parent's polar decomposition theorem gives the unique Cartan form $\tilde{M}=\tilde{B}\tilde{R}$ with $\tilde{B}$ a boost of positive-definite matrix image and $\tilde{R}$ a unit real quaternion, i.e. a spatial rotation. The factor $\tilde{R}$ is the rotation of the rest frame at $t+dt$ relative to the rest frame at $t$; it is the **Thomas–Wigner rotation** of the interval. It is a rotation and not a boost because the transformation between two frames with the same four-velocity direction of motion but different orientation is a rotation of their spatial triads.

**(c)** Write (1) as a product in the order written, $\tilde{M}=\tilde{\Lambda}_1\tilde{\Lambda}_2$, with $\tilde{\Lambda}_1=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}$ the first factor and $\tilde{\Lambda}_2=\bar{\tilde{\Lambda}}_{\mathbf{v}}=\tilde{\Lambda}_{-\mathbf{v}}$ the second. Let $\hat{\mathbf{u}}_1=\widehat{\mathbf{v}+d\mathbf{v}}$ and $\hat{\mathbf{u}}_2=-\hat{\mathbf{v}}$ be their directions and $\psi_1,\psi_2$ their rapidities, $\tanh\psi_1=|\mathbf{v}+d\mathbf{v}|/c$, $\tanh\psi_2=v/c$. The parent's boxed result for the product $\tilde{\Lambda}_1\tilde{\Lambda}_2$ of two boost rotors then applies with the rotation angle $\theta_W$ of $\tilde{R}$ given by
$$
\tan\frac{\theta_W}{2}
=\frac{\sinh\frac{\psi_1}{2}\,\sinh\frac{\psi_2}{2}\,\sin\varphi}
{\cosh\frac{\psi_1}{2}\,\cosh\frac{\psi_2}{2}+\sinh\frac{\psi_1}{2}\,\sinh\frac{\psi_2}{2}\,\cos\varphi},
\tag{4}
$$
where $\varphi$ is the angle between $\hat{\mathbf{u}}_1$ and $\hat{\mathbf{u}}_2$, i.e. between $\widehat{\mathbf{v}+d\mathbf{v}}$ and $-\hat{\mathbf{v}}$. The axis is the parent's: for the product written in this order it is $-\widehat{\hat{\mathbf{u}}_1\times\hat{\mathbf{u}}_2}$. This form of the answer is exact for the finite step $dt$; the next problem takes the limit.

## Problem 2: The Thomas Precession Rate

**Statement.** Put $d\mathbf{v}=\mathbf{a}\,dt$. Expand (4) to first order in $dt$ and show that the rest frame precesses with angular velocity
$$
\boxed{\ \boldsymbol{\omega}_T=\frac{1}{c^2}\left(\frac{\gamma^2}{\gamma+1}\right)\,\mathbf{a}\times\mathbf{v}\ }
\tag{5}
$$
with axis along $\mathbf{a}\times\mathbf{v}$, and that in the non-relativistic limit $\boldsymbol{\omega}_T\approx \frac{1}{2c^2}\mathbf{a}\times\mathbf{v}$.

**Solution.** Decompose the acceleration into parts parallel and perpendicular to the velocity,
$$
\mathbf{a}_\parallel=(\mathbf{a}\cdot\hat{\mathbf{v}})\hat{\mathbf{v}},
\qquad
\mathbf{a}_\perp=\mathbf{a}-\mathbf{a}_\parallel,
\qquad
\mathbf{a}\times\mathbf{v}=\mathbf{a}_\perp\times\mathbf{v}.
\tag{6}
$$

*The angle $\varphi$.* The direction $\hat{\mathbf{u}}_2=-\hat{\mathbf{v}}$ is fixed; the direction $\hat{\mathbf{u}}_1=\widehat{\mathbf{v}+d\mathbf{v}}$ turns away from $\hat{\mathbf{v}}$ by the small angle $\delta$ with
$$
\delta=\frac{|\mathbf{a}_\perp|}{v}\,dt+O(dt^2).
\tag{7}
$$
Hence $\varphi=\pi-\delta$, so
$$
\sin\varphi=\sin\delta=\delta+O(dt^3),
\qquad
\cos\varphi=-\cos\delta=-1+O(dt^2).
\tag{8}
$$

*The rapidity $\psi_1$.* Since $\tanh\psi=v/c$, the change of rapidity under $v\mapsto v+(\mathbf{a}\cdot\hat{\mathbf{v}})dt$ is
$$
d\psi=\frac{d(v/c)}{1-v^2/c^2}=\frac{\gamma^2}{c}(\mathbf{a}\cdot\hat{\mathbf{v}})\,dt+O(dt^2),
\qquad\text{so}\qquad \psi_1=\psi+d\psi,\quad \psi_2=\psi .
\tag{9}
$$
The perpendicular part of the acceleration does not change the speed and hence does not change the rapidity.

*The numerator of (4).* To first order,
$$
\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\sin\varphi
=\left[\sinh\frac{\psi}{2}+\frac12\cosh\frac{\psi}{2}\,d\psi\right]\sinh\frac{\psi}{2}\,\delta
=\sinh^2\frac{\psi}{2}\,\delta+O(dt^2),
\tag{10}
$$
because the $d\psi$ term multiplies the already first-order $\delta$.

*The denominator of (4).* To zeroth order, $\cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2}=1$. The first-order $d\psi$ terms cancel between the two products,
$$
\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2}
=\cosh^2\frac{\psi}{2}+\frac12\cosh\frac{\psi}{2}\sinh\frac{\psi}{2}\,d\psi+O(dt^2),
$$
$$
\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}
=\sinh^2\frac{\psi}{2}+\frac12\sinh\frac{\psi}{2}\cosh\frac{\psi}{2}\,d\psi+O(dt^2),
$$
and multiplying the second by $\cos\varphi=-1+O(dt^2)$ gives
$$
\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2}+\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\varphi
=1+O(dt^2).
\tag{11}
$$
The two $d\psi$ terms cancel exactly; the residual $O(dt^2)$ comes from $\cos\varphi=-1+\tfrac12\delta^2+\cdots$, which is already second order.

*The angle.* Combining (10) and (11),
$$
\tan\frac{\theta_W}{2}=\sinh^2\frac{\psi}{2}\,\delta+O(dt^2)
\ \Longrightarrow\
\theta_W=2\sinh^2\frac{\psi}{2}\,\delta+O(dt^2)=(\cosh\psi-1)\,\delta+O(dt^2),
$$
where $2\sinh^2(\psi/2)=\cosh\psi-1$. With $\cosh\psi=\gamma$ and (7),
$$
\theta_W=(\gamma-1)\,\frac{|\mathbf{a}_\perp|}{v}\,dt+O(dt^2).
\tag{12}
$$
The Thomas precession angular velocity is therefore
$$
\omega_T=\frac{d\theta_W}{dt}=(\gamma-1)\frac{|\mathbf{a}_\perp|}{v}
=\frac{\gamma-1}{v^2}\,|\mathbf{a}\times\mathbf{v}| .
\tag{13}
$$
The coefficient can be written in the standard form by using
$$
\frac{\gamma-1}{v^2}=\frac{\gamma^2}{c^2(\gamma+1)},
\tag{14}
$$
which follows from $v^2/c^2=1-\gamma^{-2}$ and $\gamma^2-1=(\gamma-1)(\gamma+1)$. Substituting (14) into (13) gives the magnitude in (5).

*The direction.* In the notation of Problem 1(c), the parent's axis rule for the product $\tilde{M}=\tilde{\Lambda}_1\tilde{\Lambda}_2$ in the order written gives the axis $-\widehat{\hat{\mathbf{u}}_1\times\hat{\mathbf{u}}_2}$, where $\hat{\mathbf{u}}_1=\widehat{\mathbf{v}+d\mathbf{v}}$ and $\hat{\mathbf{u}}_2=-\hat{\mathbf{v}}$. Then
$$
-\hat{\mathbf{u}}_1\times\hat{\mathbf{u}}_2
=-\widehat{\mathbf{v}+d\mathbf{v}}\times(-\hat{\mathbf{v}})
=\widehat{\mathbf{v}+d\mathbf{v}}\times\hat{\mathbf{v}}
=\left(\hat{\mathbf{v}}+\frac{\mathbf{a}_\perp}{v}dt\right)\times\hat{\mathbf{v}}
=\frac{dt}{v}\,\mathbf{a}_\perp\times\hat{\mathbf{v}}
=\frac{dt}{v^2}\,\mathbf{a}\times\mathbf{v},
$$
where the last step uses $\mathbf{a}_\perp\times\hat{\mathbf{v}}=\frac{1}{v}(\mathbf{a}\times\mathbf{v})$. Its direction is $\widehat{\mathbf{a}\times\mathbf{v}}$, so the precession is along $\mathbf{a}\times\mathbf{v}$ and (5) holds as a vector equation.

*Non-relativistic limit.* As $v\to0$, $\gamma\to1$ and $\gamma^2/(\gamma+1)\to\tfrac12$, so
$$
\boldsymbol{\omega}_T\approx\frac{1}{2c^2}\,\mathbf{a}\times\mathbf{v}.
\tag{15}
$$
The factor $\tfrac12$ is the "Thomas half". It is not put in by hand: it is the value at $\gamma=1$ of $\gamma^2/(\gamma+1)$, and it comes in through the expansion of the denominator in (11) to the value $1$ rather than the larger $\cosh\psi$ that a first guess might produce.

*Only the transverse acceleration precesses the frame.* Since $\mathbf{a}\times\mathbf{v}=\mathbf{a}_\perp\times\mathbf{v}$, a purely longitudinal acceleration ($\mathbf{a}\parallel\mathbf{v}$) gives $\boldsymbol{\omega}_T=0$: it changes the rapidity but not the direction of the rest frame's rotation axis. This is the first sign that the collinear case cannot test the direction of (5).

## Problem 3: The Sign, Checked Where It Is Visible

**Statement.** The vector equation (5) has a sign, and the sign is the whole content of the statement that the rotation is about $\mathbf{a}\times\mathbf{v}$ rather than $\mathbf{v}\times\mathbf{a}$.

**(a)** Show that a collinear geometry ($\mathbf{a}\parallel\mathbf{v}$), and equally a single boost, gives $\boldsymbol{\omega}_T=0$ and therefore cannot distinguish the two signs.

**(b)** Compute $\boldsymbol{\omega}_T$ explicitly for $\mathbf{v}=v\,e_1$, $\mathbf{a}=a\,e_2$, an orthogonal non-collinear geometry, both from (5) and directly from the parent's formula (4).

**(c)** Show that the sign in (5) is carried by the order of the two factors in (1): the reverse-order rotor $\tilde{M}_{\mathrm{rev}}=\tilde{\Lambda}_{\mathbf{v}}^{-1}\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}$ has the opposite rotation factor $\tilde{R}^{-1}$ and flips $\boldsymbol{\omega}_T$. Then determine whether the unstated direction of the boost rotor — reading $\tilde{\Lambda}_{\mathbf{v}}$ as the rest-to-lab rotor — also flips it.

**(d)** Record the numerical verification.

**Solution. (a)** If $\mathbf{a}\parallel\mathbf{v}$ then $\mathbf{a}\times\mathbf{v}=0$, and (5) gives $\boldsymbol{\omega}_T=0$ with either sign convention. A single boost likewise produces no rotation — a lone boost rotor is Hermitian and lies in $\mathbb{M}_+$, and only the composition of two non-collinear boosts leaves a rotation — so a check performed on one boost, or on any collinear case, verifies nothing about the sign: a formula fitted to the case that suggested it is confirmed by that case and by no other.

**(b)** Take $\mathbf{v}=v\,e_1$ and $\mathbf{a}=a\,e_2$ with $v,a>0$, so $\mathbf{a}_\perp=\mathbf{a}$ and
$$
\mathbf{a}\times\mathbf{v}=a\,e_2\times v\,e_1=-av\,e_3 .
$$
Equation (5) gives
$$
\boldsymbol{\omega}_T=-\frac{\gamma^2}{\gamma+1}\frac{av}{c^2}\,e_3 .
\tag{16}
$$
Directly from the parent's formula: here $d\mathbf{v}=a\,dt\,e_2$, $\psi_1=\psi_2=\psi+O(dt^2)$ (the acceleration is perpendicular to $\mathbf{v}$, so $d\psi=0$ by (9)), $\delta=a\,dt/v$, and $\varphi=\pi-\delta$. Then (4) collapses to
$$
\tan\frac{\theta_W}{2}=\frac{\sinh^2\frac{\psi}{2}\sin\delta}{\cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2}\cos\delta}
=\sinh^2\frac{\psi}{2}\,\delta+O(dt^2),
$$
and the parent's axis rule places the rotation along $-(\hat{\mathbf{u}}_1\times\hat{\mathbf{u}}_2)$: in the basis used, $\hat{\mathbf{u}}_1=\widehat{\mathbf{v}+d\mathbf{v}}=e_1+\frac{a\,dt}{v}e_2$ is the direction of the first factor $\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}$, $\hat{\mathbf{u}}_2=-\hat{\mathbf{v}}=-e_1$ that of the second factor $\bar{\tilde{\Lambda}}_{\mathbf{v}}$, and
$$
-\hat{\mathbf{u}}_1\times\hat{\mathbf{u}}_2=-\left(e_1+\frac{a\,dt}{v}e_2\right)\times(-e_1)=\left(e_1+\frac{a\,dt}{v}e_2\right)\times e_1=\frac{a\,dt}{v}\,e_2\times e_1=-\frac{a\,dt}{v}\,e_3,
$$
which is the direction of $\mathbf{a}\times\mathbf{v}=a\,e_2\times v\,e_1=-av\,e_3$. The sign in (16) is therefore not a convention chosen at the end: it is what the parent's own formula produces, once the composition order is the one in (1).

For $v=0.6c$ and $a$ such that $av/c^2=|a\times v|/c^2=0.6$ per unit time (units $c=1$), $\gamma=1.25$, $\gamma^2/(\gamma+1)=0.694444$, and
$$
|\boldsymbol{\omega}_T|=0.694444\times0.6=0.4166667\ \text{rad per unit lab time},\qquad \text{direction }-e_3 .
$$
The parent's formula (4) evaluated on the same step gives $\theta_W/dt=0.41666667$ rad per unit time, to the printed digits.

**(c)** The reverse-order rotor is $\tilde{M}_{\mathrm{rev}}=\tilde{\Lambda}_{\mathbf{v}}^{-1}\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}$. To first order in $dt$ its rotation factor is $\tilde{R}^{-1}$: the same angle $\theta_W$ with the opposite axis. Equation (5) then reads $-\frac{\gamma^{2}}{\gamma+1}\frac{\mathbf{a}\times\mathbf{v}}{c^{2}}$, and the circular result of Problem 4 reverses its sense, becoming prograde instead of retrograde. The collinear check of (a) is blind to this; the non-collinear computation of (b) is not.

The rotor *direction* is a separate question, and it is settled by the same computation. If $\tilde{\Lambda}_{\mathbf{v}}$ is read as the rest-to-lab rotor, the lab-to-rest rotor is $\tilde{\Lambda}_{\mathbf{v}}^{-1}$, and the interval rotor built from it is $\tilde{M}'=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}^{-1}\tilde{\Lambda}_{\mathbf{v}}$, which inverts each factor of $\tilde{M}$ while keeping the order. To first order in $dt$ its rotation vector is the *same* as that of $\tilde{M}$, not the opposite one: inverting both factors together changes the boost part but not the first-order rotation. So the unstated direction of the parent's rotor, applied consistently, does not by itself flip the sign; the sign is fixed by the order of composition. That the sign is nevertheless delicate is why (5) is stated with its axis and not with its magnitude alone.

**(d)** *Numerical verification.* The biquaternion product (1) was formed directly, and $\tilde{R}$ extracted by polar decomposition $\tilde{M}=\tilde{B}\tilde{R}$, $\tilde{B}=\sqrt{\tilde{M}\tilde{M}^\dagger}$, $\tilde{R}=\tilde{B}^{-1}\tilde{M}$, with $\tilde{R}$ a unit real quaternion and $\theta_W$ read from $\mathrm{Sc}(\tilde{R})=\cos(\theta_W/2)$. On randomly generated non-collinear pairs $(\mathbf{v},\mathbf{a})$, restricted to $|\mathbf{v}|<c$, the computed rotation vector agreed with (5) to better than $10^{-10}$ in units $c=1$, in both magnitude and direction. The special case $\mathbf{v}=0.6c\,e_1$, $\mathbf{a}\perp\mathbf{v}$ reproduced $0.41666667$ as above. The reverse-order rotor $\tilde{M}_{\mathrm{rev}}$ reproduced the same magnitude with the opposite axis, while the consistently inverted reading $\tilde{M}'$ reproduced the same axis as (5), both to the same precision.

## Problem 4: Uniform Circular Motion, the Retrograde Rotation, and the Thomas Half

**Statement.** A particle moves on a circle of radius $R$ at constant speed $v$ in the lab, with angular velocity $\boldsymbol{\Omega}=\Omega\,e_3$, so that its acceleration is centripetal, $\mathbf{a}=-\Omega^2\mathbf{r}$, and $\mathbf{v}=\boldsymbol{\Omega}\times\mathbf{r}$, where $\mathbf{r}$ is the position on the circle, $|\mathbf{r}|=R$.

**(a)** Show that $\mathbf{a}\times\mathbf{v}=-\Omega v^2\,e_3$ and hence, from (5),
$$
\boldsymbol{\omega}_T=-(\gamma-1)\Omega\,e_3 .
\tag{17}
$$
**(b)** Show that over one orbit the frame precesses by $\Delta\theta=-2\pi(\gamma-1)$, i.e. *retrograde*, and that in the non-relativistic limit the ratio of the Thomas precession to the orbital angular velocity is $-\tfrac12 v^2/c^2$.

**(c)** Relate the rate to the factor $\tfrac12$ in the spin–orbit coupling.

**Solution. (a)** For uniform circular motion the acceleration is centripetal, $\mathbf{a}=-\Omega^2\mathbf{r}$, and $\mathbf{v}=\boldsymbol{\Omega}\times\mathbf{r}$, so with $\mathbf{r}\times(\boldsymbol{\Omega}\times\mathbf{r})=R^2\boldsymbol{\Omega}$ for $\boldsymbol{\Omega}\perp\mathbf{r}$,
$$
\mathbf{a}\times\mathbf{v}=(-\Omega^2\mathbf{r})\times(\boldsymbol{\Omega}\times\mathbf{r})
=-\Omega^2 R^2\,\boldsymbol{\Omega}
=-\Omega v^2\,e_3 .
$$
Equation (5) gives $\boldsymbol{\omega}_T=\frac{\gamma^2}{\gamma+1}(-\Omega v^2/c^2)e_3$. Using $v^2/c^2=1-\gamma^{-2}$,
$$
\frac{\gamma^2}{\gamma+1}\left(1-\frac{1}{\gamma^2}\right)
=\frac{\gamma^2-1}{\gamma+1}=\gamma-1,
$$
which is (17). The precession is **opposite to the orbital angular velocity**: it is retrograde.

**(b)** Over one orbit the lab time is $T=2\pi/\Omega$, so from (17)
$$
\Delta\theta=|\boldsymbol{\omega}_T|\,T=(\gamma-1)\,\Omega\,\frac{2\pi}{\Omega}=2\pi(\gamma-1)
\quad\text{with the sense opposite to }\boldsymbol{\Omega},
$$
i.e. $\Delta\theta=-2\pi(\gamma-1)$. In the non-relativistic limit $\gamma-1\approx v^2/2c^2$, so $\omega_T/\Omega\approx-\tfrac12 v^2/c^2$: the precession is half the orbital rate, to leading order, and opposite in sense. Formally the factor $\tfrac12$ is the value of $\gamma^2/(\gamma+1)$ at $\gamma=1$, first displayed in (15).

**(c)** The four-force of the parent article is $\tilde{F}=i\gamma\frac{q}{c}(\mathbf{E}\cdot\mathbf{v})e_0+\gamma q(\mathbf{E}+\mathbf{v}\times\mathbf{B})\in\mathbb{M}_-$, and under a magnetic field a spin is torqued at the Larmor rate. The kinematic precession (5) is a separate, purely kinematical contribution, present even with no torque: it is the rotation of the instantaneous rest frame relative to a non-rotating one. In the standard non-relativistic treatment of the spin–orbit coupling, the naive boost of the electron to its instantaneous rest frame gives a rest-frame magnetic field and hence a spin–orbit term twice as large as the observed one; the Thomas precession contributes $-\tfrac12$ of the naive Larmor precession, leaving the observed $\tfrac12$. *Exercise: The Non-Relativistic Limit and the Pauli Equation* records exactly this: the coefficient of the spin–orbit term carries the "Thomas factor of $\tfrac12$", and "a naive Lorentz transformation to the instantaneous rest frame of the electron would give twice this value." The present exercise supplies the kinematics behind that factor: (15) is the leading rate, half of $\mathbf{a}\times\mathbf{v}/c^2$, and (17) is its exact circular-orbit form.

## Problem 5: What the Parents Supply, and Where the Gap Is

**Statement.** Examine the parent articles for the Thomas precession and report exactly what they contain.

**Solution.** Three recorded facts and one gap.

*The discrete rotation is in the corpus, and it is correct.* The Lorentz-group article derives the exact Wigner angle (its boxed formula, reproduced as (4) above) and its axis, and records the leading approximation $\delta\approx\tfrac12|\mathbf{v}_1\times\mathbf{v}_2|/c^2$. The boosting exercise derives the same product in full, with a verified numerical instance. Both were re-checked here on independent cases: the axis rule, the angle formula, and the numerical instance $\psi_1=\psi_2=\operatorname{atanh}0.6$, orthogonal, with composed speed $0.7683749c$ and Wigner angle $12.68038^\circ$, all reproduce. No false statement was found in either parent on the cases tested.

*The rate is not in the corpus.* The parents give the Wigner angle of a **finite pair of given boosts**. The Thomas precession is an **angular velocity**; its input is the acceleration, which the two-boost formula does not contain. The bridge is the limit taken in Problem 2, $\theta_W/dt$ with $d\mathbf{v}=\mathbf{a}\,dt$, and it appears nowhere in the parents. A reader who needs $\boldsymbol{\omega}_T$ finds in the corpus only the discrete angle and its leading approximation, and the phrase in the Lorentz-group article that calls $\delta\approx\tfrac12|\mathbf{v}_1\times\mathbf{v}_2|/c^2$ "the familiar leading Thomas-precession angle". That phrase is accurate only in the infinitesimal limit in which the velocity change is $\mathbf{v}_2-\mathbf{v}_1=\mathbf{a}\,dt$; for two finite boosts the angle $\delta$ is not the *accumulated* precession angle along any particle's worldline, because there is no worldline, and the two quantities agree only to leading order. The rate is the missing object, and (5) is it.

*The direction of the boost rotor is unstated.* The parent Lorentz-transformation article writes $\tilde{\Lambda}=\sqrt{-\tfrac{i}{c}\bar{\tilde{U}}}$ without saying that it is the lab-to-rest rotor; the $\mathbb{M}_+$ article says only that the boost biquaternion "acts on $\mathbb{M}_-$ by rotor conjugation, implementing a Lorentz boost", again without a direction; the boosting exercise's Problem 4 records this as a genuine gap in the parent's statement. For the Thomas precession the gap is real but, as Problem 3(c) shows, benign when the ambiguity is applied consistently: inverting each boost rotor together leaves the first-order precession unchanged, and only the composition order in (1) reverses the sign. The gap does not by itself corrupt $\boldsymbol{\omega}_T$; what it does mean is that the sign cannot be checked from the parents' statements alone, and it is the non-collinear computation that supplies the missing information.

*Summary of the gap.* It is a gap of scope and of statement, not an error: the parents contain the discrete rotation and get it right, but they contain neither the precession rate nor the direction of the boost rotor. The rate is the object this exercise adds; the direction is a statement the parents leave implicit, and the sign it bears is only visible on a non-collinear geometry.

## Summary

We have taken the discrete Thomas–Wigner rotation of the parent articles to its continuous limit.

1. **The interval rotor.** The rest frame at lab time $t+dt$ is obtained from the rest frame at $t$ by the unit-norm rotor $\tilde{M}=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}\tilde{\Lambda}_{\mathbf{v}}^{-1}$, whose polar decomposition $\tilde{M}=\tilde{B}\tilde{R}$ separates a pure boost $\tilde{B}\in\mathbb{M}_+$ from the Thomas–Wigner rotation $\tilde{R}\in\mathbb{H}_{\mathbb{B}}$ of the interval.

2. **The rate.** Expanding the parent's Wigner-angle formula to first order in $dt$ gives the Thomas precession
$$
\boldsymbol{\omega}_T=\frac{1}{c^2}\left(\frac{\gamma^2}{\gamma+1}\right)\mathbf{a}\times\mathbf{v},
$$
along $\mathbf{a}\times\mathbf{v}$, and the non-relativistic limit $\boldsymbol{\omega}_T\approx\frac{1}{2c^2}\mathbf{a}\times\mathbf{v}$ — the Thomas half. Only the transverse part of the acceleration precesses the frame.

3. **The sign.** A collinear geometry gives zero and cannot test the sign; the orthogonal geometry $\mathbf{v}=v\,e_1$, $\mathbf{a}=a\,e_2$ gives $\boldsymbol{\omega}_T$ along $\mathbf{a}\times\mathbf{v}$, as the parent's own formula requires. Reversing the composition order (using the inverse interval rotor) flips the sign, while inverting each boost rotor together — the unstated-direction reading — leaves it unchanged. The sign was verified by polar decomposition of the exact biquaternion product on random non-collinear cases, to better than $10^{-10}$.

4. **Circular motion.** For uniform circular motion the frame precesses retrograde at $\omega_T=(\gamma-1)\Omega$, i.e. by $-2\pi(\gamma-1)$ per orbit, half the orbital rate to leading order; this is the kinematic origin of the factor $\tfrac12$ in the spin–orbit coupling recorded in the non-relativistic-limit exercise.

5. **The gap.** The parents supply the discrete Wigner angle, correctly, but neither the precession rate nor the direction of the boost rotor. The rate is supplied here; the sign it carries is only visible on a non-collinear geometry. The gap is reported rather than smoothed over.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; scalar (central) subspace |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $c$, $c_0$ | Speed of light in the medium, and in vacuum |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\bar{\tilde{Q}}$, $\tilde{Q}^\dagger=\bar{\tilde{Q}}^{*}$ | Quaternion conjugate, Hermitian conjugate |
| $\tilde{U}=\gamma(ic\,e_0+\mathbf{v})$ | Four-velocity, $N(\tilde{U})=-c^2$ |
| $\tilde{P}=m\tilde{U}=iE/c\,e_0+\mathbf{p}$ | Four-momentum |
| $\tilde{F}=d\tilde{P}/d\tau$ | Four-force, in $\mathbb{M}_-$ |
| $\gamma=(1-\mathbf{v}^2/c^2)^{-1/2}$ | Lorentz factor |
| $\psi$, $\tanh\psi=v/c$ | Rapidity; $v=|\mathbf{v}|$, $\hat{\mathbf{v}}=\mathbf{v}/v$ |
| $\tilde{\Lambda}_{\mathbf{v}}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{v}}$ | Lab-to-rest boost rotor, Hermitian, in $\mathbb{M}_+$ |
| $\mathbf{a}=d\mathbf{v}/dt$, $\mathbf{a}_\perp$ | Lab acceleration; its part perpendicular to $\mathbf{v}$ |
| $\tilde{M}=\tilde{\Lambda}_{\mathbf{v}+d\mathbf{v}}\tilde{\Lambda}_{\mathbf{v}}^{-1}$ | Rotor between neighbouring rest frames |
| $\tilde{B}$, $\tilde{R}$ | Boost and rotation factors of $\tilde{M}=\tilde{B}\tilde{R}$ |
| $\theta_W$ | Thomas–Wigner rotation angle of the interval |
| $\boldsymbol{\omega}_T$ | Thomas precession angular velocity |
| $\boldsymbol{\Omega}=\Omega\,e_3$ | Orbital angular velocity (circular motion) |
| $\mathrm{Sc}$, $\mathrm{Tr}$ | Scalar part, trace; $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ |

## Further Reading

- *Introduction to the Biquaternion Universe*, for the algebra and the two sectors.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the four-vectors and the rotor conjugation on $\mathbb{M}_-$.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the boost biquaternion as an element of $\mathbb{M}_+$.
- *Relativistic Mechanics in Biquaternionic Form*, for the four-velocity, four-momentum, and four-force.
- *The Lorentz Transformation as a Biquaternionic Rotation*, for the boost rotor, the square-root relation, and the polar decomposition.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations*, for the Wigner angle, its axis, and its leading approximation.
- *Exercise: Boosting a Four-Velocity and Rapidity Composition*, for the discrete composition and the recorded direction gap in the parent.
- *The Spinor Representation of the Lorentz Group in Biquaternionic Form*, for the one-sided action of the rotors that carries the spin.
- *Exercise: The Non-Relativistic Limit and the Pauli Equation*, for the spin–orbit coupling and the Thomas factor of $\tfrac12$.
