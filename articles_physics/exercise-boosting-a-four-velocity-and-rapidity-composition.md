# __Exercise: Boosting a Four-Velocity and Rapidity Composition__

## Introduction

This is one of the exercises in the relativity series. It applies the apparatus of two companion articles: *The Lorentz Transformation as a Biquaternionic Rotation*, which defines the boost biquaternion, the rotor conjugation, and the square-root relation between the rotor and the four-velocity; and *Relativistic Mechanics in Biquaternionic Form*, which fixes the four-velocity and the four-momentum in $\mathbb{M}_-$. Those two articles are the parents of this exercise: every result below is obtained from the tools already defined there, and no new formalism is introduced. The sequence is: boost a general four-velocity (Problem 1); compose two collinear boosts and recover rapidity addition and velocity addition (Problem 2); compose two non-collinear boosts and extract the Thomas–Wigner rotation (Problem 3); and examine the parent's square-root relation between the four-velocity and the boost rotor, whose direction the parent does not state (Problem 4). A set of further problems is left to the reader.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$, and the scalar imaginary $i$ with $i^2 = -1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part), the Hermitian subspace $\mathbb{M}_+$ (real scalar part, imaginary vector part), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$, and the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ of the rotation rotors. The biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$, the quaternion conjugate $\tilde{Q}^{\natural}$, the Hermitian conjugate $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the rotor conjugation $\tilde{Q}\mapsto\tilde U\tilde{Q}\tilde U^{*}$ with $\tilde U\tilde U^{\natural} = e_t$. The trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ belongs to the shared notation; no object of the informational sector arises below, so it is recorded but not used. The four-velocity $\tilde{V} = \gamma(ic\,e_t + \vec v)$ with $\langle\tilde{V}\rangle_{\natural} = -c^2$ and $\gamma = (1-\vec v^2/c^2)^{-1/2}$, the four-momentum $\tilde{P} = m\tilde{V} = iE/c\,e_t + \vec p$, and the boost biquaternion
$$
\tilde U_{\vec v_b} = \cosh\frac{\psi_b}{2} + i\sinh\frac{\psi_b}{2}\vec u_x,
\qquad
\tanh\psi_b = \frac{v_b}{c},
$$
which is Hermitian ($\tilde U_{\vec v_b}^{*} = \tilde U_{\vec v_b}$), lies in $\mathbb{M}_+$, and has unit norm. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value; $\vec v$ is a particle velocity, and $\vec u_x, \vec u_y$ are unit frame or boost directions. The components of a biquaternion are taken in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**What is to be shown.** Problem 1 computes $\tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}^{*}$ for arbitrary $\vec v_b,\vec v$ and shows that it is again a four-velocity of $\mathbb{M}_-$ with the standard components. Problem 2 composes two collinear boost rotors and derives rapidity addition and the velocity-addition formula. Problem 3 composes two non-collinear boosts, shows that the product is no longer a pure boost, and extracts the boost part, the total rapidity, and the Thomas–Wigner angle. Problem 4 verifies the parent's relation $\tilde U = \sqrt{-\tfrac{i}{c}\tilde{V}^{\natural}}$, determines the direction of the transformation it generates, and identifies what the four-velocity does and does not determine. The problems are solved in full; the reader is asked in the final section to extend them.

## Problem 1: The Boost of a General Four-Velocity

**Statement.** Let $\tilde{V} = \gamma(ic\,e_t + \vec v)$ be the four-velocity of a particle, and let $\tilde U_{\vec v_b} = \cosh\frac{\psi_b}{2} + i\sinh\frac{\psi_b}{2}\vec u_x$, with $\tanh\psi_b = v_b/c$, be a boost biquaternion. Compute $\tilde{V}' = \tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}^{*}$ and show that:

**(a)** $\tilde{V}'$ lies in $\mathbb{M}_-$ and has $\langle\tilde{V}'\rangle_{\natural} = -c^2$;

**(b)** its scalar part is $ic\,\gamma'$ with $\gamma' = \gamma_b\gamma\left(1 - \vec v_b\cdot\vec v/c^2\right)$, where $\gamma_b = (1-v_b^2/c^2)^{-1/2}$;

**(c)** its vector part is $\gamma\left[\vec v + (\gamma_b-1)\dfrac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b - \gamma_b\vec v_b\right]$, so that the induced velocity is the standard parallel–perpendicular transformation;

**(d)** in the collinear case $\vec v\parallel\vec v_b$ the induced velocity is $v' = (v-v_b)/(1-v_b v/c^2)$, i.e. the rapidities subtract.

**Solution.** Because a pure-boost rotor is Hermitian, $\tilde U_{\vec v_b}^{*} = \tilde U_{\vec v_b}$, and the transformation is the two-sided product $\tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}$. Write $a = \cosh\frac{\psi_b}{2}$, $b = \sinh\frac{\psi_b}{2}$, and $J = \vec u_x$, a real unit pure quaternion with $J^2 = -e_t$. Split the velocity into parts parallel and perpendicular to $J$,
$$
\vec v = \vec v_\parallel + \vec v_\perp, \qquad \vec v_\parallel = v_\parallel J, \qquad J\,\vec v_\parallel = -v_\parallel, \qquad J\,\vec v_\perp = J\times\vec v_\perp, \qquad \vec v_\perp J = -J\times\vec v_\perp .
$$
The first product expands as
$$
\tilde U\tilde{V} = ic\gamma\,\tilde U + \gamma\,\tilde U\vec v
= ic\gamma a - c\gamma b\,J + \gamma\left(a\vec v_\parallel + a\vec v_\perp - i b v_\parallel + i b\,J\times\vec v_\perp\right).
$$
Multiplying once more on the right by $\tilde U = a + ibJ$ and collecting the scalar and vector parts gives
$$
\tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}^{*}
= ic\,\gamma_b\gamma\left(1 - \frac{\vec v_b\cdot\vec v}{c^2}\right)e_t
+ \gamma\left[\vec v + (\gamma_b-1)\frac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b - \gamma_b\vec v_b\right].
\tag{1}
$$
The identity $\sinh\psi_b = \gamma_b v_b/c$ and the expansion of the parallel component have been used. The result is the biquaternion form of the standard Lorentz transformation of a four-velocity from the lab to the frame moving with velocity $\vec v_b$.

**(a)** In (1) the scalar coefficient is purely imaginary and the vector coefficient is real, so $\tilde{V}'\in\mathbb{M}_-$. Its biquaternion norm is preserved because $\langle\cdot\rangle_{\natural}$ is multiplicative and $\langle\tilde U_{\vec v_b}\rangle_{\natural} = 1$:
$$
\langle\tilde{V}'\rangle_{\natural} = \langle\tilde U_{\vec v_b}\rangle_{\natural}\,\langle\tilde{V}\rangle_{\natural}\,\langle\tilde U_{\vec v_b}\rangle_{\natural}^{*} = 1\cdot(-c^2)\cdot 1 = -c^2 .
$$
The transformation therefore maps four-velocities to four-velocities; this is the algebraic content of Lorentz covariance in $\mathbb{M}_-$.

**(b)** Reading off the scalar coefficient of (1), $\gamma' = \gamma_b\gamma(1-\vec v_b\cdot\vec v/c^2)$. This is positive for $v_b,v<c$, since $\vec v_b\cdot\vec v\le v_b v < c^2$. It is the standard transformation of energy, $E'/c = \gamma_b(E/c - \vec v_b\cdot\vec p/c)$, written for the four-velocity.

**(c)** The induced velocity is the vector coefficient divided by $\gamma'$,
$$
\vec v' = \frac{\vec v + (\gamma_b-1)\dfrac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b - \gamma_b\vec v_b}{\gamma_b\left(1 - \vec v_b\cdot\vec v/c^2\right)}
= \frac{\vec v_\parallel - \vec v_b}{1 - \vec v_b\cdot\vec v/c^2} + \frac{\vec v_\perp}{\gamma_b\left(1 - \vec v_b\cdot\vec v/c^2\right)},
\tag{2}
$$
which is the standard transformation. The second equality uses $\vec v_\parallel = \frac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b$ and the rearrangement $\vec v + (\gamma_b-1)\vec v_\parallel - \gamma_b\vec v_b = \vec v_\perp + \gamma_b(\vec v_\parallel-\vec v_b)$.

**(d)** If $\vec v = v\vec u_x$ then $\vec v_\perp = 0$ and (2) reduces to
$$
v' = \frac{v-u}{1-v_b v/c^2},
$$
so that in rapidities $v' = c\tanh(\psi_v - \psi_b)$: **a boost subtracts its rapidity from the rapidity of the four-velocity it acts on.** This is the statement that the transformation (1) is the lab-to-moving-frame map, and it fixes the direction convention used throughout: the rotor $\tilde U_{\vec v_b}$ carries the lab to the frame moving with $+\vec v_b$, so the particle's speed is reduced by $v_b$.

**Numerical instance.** Take $\vec v = 0.6c\,\vec e_x$ and $\vec v_b = 0.5c\,\vec e_y$, orthogonal. Then $\gamma = 1.25$, $\gamma_b = 1.1547005$, $\vec v_b\cdot\vec v = 0$, and from (1)
$$
\gamma' = \gamma_b\gamma = 1.4433757, \qquad
\vec v' = \begin{pmatrix} 0.5196152 \\ -0.5 \\ 0\end{pmatrix}c, \qquad |\vec v'| = 0.7211103\,c .
$$
The norm is preserved: $\langle\tilde{V}'\rangle_{\natural} = -1$ in units $c=1$. The transverse component is contracted by $1/\gamma_b$ (from $0.6c$ to $0.5196c$) and the boost direction acquires the recoil $-v_b$; this is (2) term by term.

## Problem 2: Collinear Boosts and Rapidity Addition

**Statement.** Let $\tilde U_1 = \cosh\frac{\psi_1}{2} + i\sinh\frac{\psi_1}{2}\vec u_y$ and $\tilde U_2 = \cosh\frac{\psi_2}{2} + i\sinh\frac{\psi_2}{2}\vec u_y$ be two boost rotors along the same direction $\vec u_y$.

**(a)** Show that $\tilde U_2\tilde U_1$ is itself a pure boost along $\vec u_y$, of rapidity $\psi_1+\psi_2$.

**(b)** Deduce the velocity-addition formula $w = \dfrac{v_{b_1}+v_{b_2}}{1+v_{b_1}v_{b_2}/c^2}$.

**(c)** Reconcile the addition here with the subtraction found in Problem 1.

**Solution. (a)** Put $J = \vec u_y$, $c_i = \cosh\frac{\psi_i}{2}$, $s_i = \sinh\frac{\psi_i}{2}$. Since $J^2 = -e_t$, the product of the two scalar-imaginary vector parts is
$$
(iJ)(iJ) = i^2J^2 = (-1)(-1) = +e_t,
$$
so the two boosts in the same direction multiply hyperbolically:
$$
\tilde U_2\tilde U_1
= \left(c_1c_2 + s_1s_2\right) + i\left(c_1s_2 + s_1c_2\right)J
= \cosh\frac{\psi_1+\psi_2}{2} + i\sinh\frac{\psi_1+\psi_2}{2}\vec u_y
= \tilde U(\psi_1+\psi_2).
\tag{3}
$$
The cross terms combine by the addition formulas for $\cosh$ and $\sinh$. The product is Hermitian, lies in $\mathbb{M}_+$, and has unit norm, so it is a pure boost along $\vec u_y$: **boosts in a common direction form a one-parameter subgroup**, and their rapidities add.

**(b)** The product rotor has rapidity $\psi_1+\psi_2$, and the velocity it represents is $w = c\tanh(\psi_1+\psi_2)$. Using $\tanh\psi_i = v_{b_i}/c$,
$$
w = c\,\frac{\tanh\psi_1 + \tanh\psi_2}{1 + \tanh\psi_1\tanh\psi_2}
= \frac{v_{b_1}+v_{b_2}}{1 + v_{b_1}v_{b_2}/c^2}.
\tag{4}
$$
For $v_{b_1} = 0.5c$, $v_{b_2} = 0.6c$ this gives $w = 1.1c/1.3 = 0.8461538c$, which is $\tanh(\operatorname{atanh}0.5 + \operatorname{atanh}0.6)$ to machine precision.

**(c)** There is no contradiction with Problem 1. Equation (3) is the composition of two *coordinate changes*: the rotor $\tilde U_2\tilde U_1$ carries the lab to the frame moving with $w$. Equation (2) of Problem 1 is the action of a *single* coordinate change on a four-velocity: it subtracts the frame rapidity. The two statements are the multiplication and the action of the same group, and in the collinear case the action's rapidity shift is the group's rapidity sum with a sign, $v' = c\tanh(\psi_v-\psi_b)$.

## Problem 3: Non-Collinear Boosts and the Thomas–Wigner Rotation

**Statement.** Let $\tilde U_1$ have rapidity $\psi_1$ along $\vec u_y$ and $\tilde U_2$ rapidity $\psi_2$ along $\vec u_z$, with $\vec u_y\cdot\vec u_z = \cos\phi$ and $0<\phi<\pi$.

**(a)** Compute the product $P = \tilde U_2\tilde U_1$ and show that it is Hermitian if and only if $\phi\in\{0,\pi\}$; for $0<\phi<\pi$ it is not a pure boost.

**(b)** Show that $P$ admits the decomposition $P = \tilde{H}\tilde u$ with $\tilde{H}$ a pure boost of unit norm and $\tilde u$ a spatial rotation. Derive the total rapidity $\Psi$, the Wigner angle $\theta_W$, and the rotation axis.

**(c)** Verify the special case of equal orthogonal rapidities, and compute a numerical instance.

**Solution. (a)** With $c_i = \cosh\frac{\psi_i}{2}$, $s_i = \sinh\frac{\psi_i}{2}$, $J_i = \vec {u_y}_i$, and the quaternion product identity $J_2J_1 = -J_2\cdot J_1 + J_2\times J_1$ for unit pure quaternions,
$$
(iJ_2)(iJ_1) = -J_2J_1 = \cos\phi + J_1\times J_2 .
$$
Hence
$$
P = \tilde U_2\tilde U_1
= \underbrace{\left(c_1c_2 + s_1s_2\cos\phi\right)}_{a}
+ \underbrace{s_1s_2\,\vec u_y\times\vec u_z}_{\vec q}
+ i\underbrace{\left(c_2s_1\vec u_y + c_1s_2\vec u_z\right)}_{\vec w},
\tag{5}
$$
where $a$ is a real scalar, $\vec q$ is a real vector of magnitude $s_1s_2\sin\phi$, and $i\vec w$ is an imaginary vector. The real vector part $\vec q$ is orthogonal to $\vec w$, because $\vec v_{b_2}\times\vec v_{b_3}$ is orthogonal to both $\vec u_y$ and $\vec u_z$. The element $P$ is Hermitian exactly when its real vector part vanishes, i.e. when $s_1s_2\sin\phi = 0$. For nonzero rapidities this means $\sin\phi = 0$, so a product of two boosts is a pure boost only when the two directions are parallel or antiparallel. Otherwise it is a boost together with a rotation: the product has left $\mathbb{M}_+$.

**(b)** Write $P = a + \vec q + i\vec w$. Its biquaternion norm is, using $\vec q\cdot\vec w=0$,
$$
\langle P\rangle_{\natural} = a^2 + |\vec q|^2 - |\vec w|^2 = 1,
\tag{6}
$$
because $P$ is a product of two unit-norm elements. Then
$$
P^\dagger = \bar{P}^{*} = a - \vec q + i\vec w,
$$
and, since a real vector anticommutes with an orthogonal real vector,
$$
P P^\dagger = \left(a^2 + |\vec q|^2 + |\vec w|^2\right) + 2i\left(a\vec w + \vec q\times\vec w\right)
\equiv \Sigma + i\vec T.
\tag{7}
$$
The element $PP^\dagger$ is Hermitian and positive (it is $\tilde{H}^2$ for the required boost), so it has a unique positive Hermitian square root
$$
\tilde{H} = \sqrt{PP^\dagger} = \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\vec u_4,
\qquad
\cosh\Psi = \Sigma, \quad \sinh\Psi\,\vec u_4 = \vec T.
$$
Expanding $\Sigma = a^2 + |\vec q|^2 + |\vec w|^2$ with the definitions (5) and simplifying gives the standard total rapidity
$$
\cosh\Psi = \cosh\psi_1\cosh\psi_2 + \sinh\psi_1\sinh\psi_2\cos\phi .
\tag{8}
$$
The residual element
$$
\tilde u = \tilde{H}^{-1}P = \tilde{H}^{\natural}P
= \left(\cosh\frac{\Psi}{2} - i\sinh\frac{\Psi}{2}\vec u_4\right)\left(a + \vec q + i\vec w\right)
$$
is the unitary factor of the polar decomposition of $P$ (equivalently $\langle\tilde u\rangle_{\natural} = \langle\tilde{H}\rangle_{\natural}^{-1}\langle P\rangle_{\natural} = 1$ and $\tilde u\tilde u^{\natural} = e_t$ with $\tilde u$ a unit real quaternion). Its scalar part is
$$
\mathrm{Sc}(\tilde u) = a\cosh\frac{\Psi}{2} - \sinh\frac{\Psi}{2}\left(\vec u_4\cdot\vec w\right),
$$
where the minus sign comes from the $-\vec A\cdot\vec B$ term of the quaternion product, and the term involving $\vec q$ vanishes because $\vec u_4\perp\vec q$. Now $\vec u_4\cdot\vec w = \vec T\cdot\vec w/\sinh\Psi = 2a|\vec w|^2/\sinh\Psi$, so
$$
\mathrm{Sc}(\tilde u) = a\cosh\frac{\Psi}{2} - \frac{a|\vec w|^2}{\cosh\frac{\Psi}{2}}
= \frac{a\left(\cosh^2\frac{\Psi}{2} - |\vec w|^2\right)}{\cosh\frac{\Psi}{2}} .
$$
From (6) and $\Sigma$ one has $\cosh^2\frac{\Psi}{2} = \frac{1+\Sigma}{2} = a^2 + |\vec q|^2 = 1 + |\vec w|^2$, so $\cosh^2\frac{\Psi}{2} - |\vec w|^2 = 1$ and
$$
\mathrm{Sc}(\tilde u) = \frac{a}{\cosh\frac{\Psi}{2}}.
$$
Because $\tilde u$ is a unit real quaternion — a spatial rotation rotor — it has the form $\tilde u = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\vec u_{\mathrm r}$ with $\vec u_{\mathrm r}$ its axis. Comparing scalar parts identifies the **Thomas–Wigner angle** $\theta_W$:
$$
\cos\frac{\theta_W}{2} = \frac{a}{\cosh\frac{\Psi}{2}}
= \frac{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2} + \sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\phi}{\cosh\frac{\Psi}{2}},
\tag{9}
$$
and, since $|\vec q|^2 = \sinh^2\frac{\psi_1}{2}\sinh^2\frac{\psi_2}{2}\sin^2\phi$ and $\sin\frac{\theta_W}{2} = |\vec q|/\cosh\frac{\Psi}{2}$,
$$
\tan\frac{\theta_W}{2} = \frac{|\vec q|}{a}
= \frac{\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\sin\phi}{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2} + \sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\phi}.
\tag{10}
$$
The numerator is non-negative for $0<\phi<\pi$ and the denominator $a$ is positive for every $\phi$, since $a\ge\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2} - \sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2} = \cosh\frac{\psi_1-\psi_2}{2}>0$. Hence $0\le\theta_W<\pi$. The rotation axis is the normal to the plane of the two boost directions,
$$
\vec u_{\mathrm r} = \vec u_{\vec v_{b_2}\times\vec v_{b_3}},
\tag{11}
$$
which we verified numerically in several non-coplanar configurations; it is the direction of the antisymmetric, real-vector part $\vec q$ of $P$ in (5). With this, the decomposition is
$$
\tilde U_2\tilde U_1 = \tilde{H}\tilde u,
\qquad
\tilde{H} = \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\vec u_4,
\qquad
\tilde u = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\vec u_{\vec v_{b_2}\times\vec v_{b_3}}.
\tag{12}
$$
The rotation is intrinsic, but the split of $P$ into boost and rotation is only canonical in the right-polar sense (12). The alternative left-polar form $P = \tilde u\tilde{H}'$ with $\tilde{H}' = \tilde u^{-1}\tilde{H}\tilde u$ is an equally valid boost-times-rotation decomposition, with a boost of the same rapidity $\Psi$ but a different axis; only $\Psi$ and $\theta_W$ are convention-independent. This is the sense in which the parent's statement that a non-collinear product is "a boost plus a spatial rotation" is complete only after the ordering is fixed.

**(c)** For equal orthogonal rapidities, $\psi_1 = \psi_2 = \psi$ and $\phi = \pi/2$, so $\cosh\Psi = \cosh^2\psi$ and $a = \cosh^2\frac{\psi}{2}$. Then $\cos\frac{\theta_W}{2} = \cosh^2\frac{\psi}{2}\big/\cosh\frac{\Psi}{2}$, and (10) collapses to
$$
\tan\frac{\theta_W}{2} = \frac{\sinh^2\frac{\psi}{2}}{\cosh^2\frac{\psi}{2}} = \tanh^2\frac{\psi}{2}.
\tag{13}
$$
This is exact; it was checked numerically for $\psi = 0.5, 1, 1.5, 2, 3$ to $10^{-12}$.

**Numerical instance.** Take $\psi_1 = \psi_2 = \operatorname{atanh}0.6 = 0.6931472$ along $\vec u_y = \vec u_{e,1}$ and $\vec u_z = \vec u_{e,2}$, so that each boost has speed $0.6c$. Then (5) gives, in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,
$$
P = \tilde U_2\tilde U_1 = 1.125 + 0.375\,i\,\vec e_x + 0.375\,i\,\vec e_y + 0.125\,\vec e_z,
$$
which is not Hermitian: the real $\vec e_z$ term $s_1s_2 = 0.125$ is the antisymmetric part. From (8), $\Psi = 1.0163481$ and the composed frame has speed $c\tanh\Psi = 0.7683749c$; the velocity-addition formula (2) applied twice gives the same speed. The Wigner angle (9)–(10) is $\theta_W = 12.68038^{\circ} = 0.2213144$ rad, with
$$
\tilde u = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\vec u_{e,3} = 0.9938837 + 0.1104315\,\vec u_{e,3} .
$$
The frame reached by $P$ has, in the lab, the four-velocity $ic\,P^{-1}(P^{-1})^{*} = 1.5625i\,e_t + 0.9375\,\vec e_x + 0.75\,\vec e_y$, i.e. velocity $(0.6, 0.48, 0)c$: magnitude $0.7683749c$ and direction $38.66^{\circ}$ from $\vec u_{e,1}$. The boost part $\tilde{H}$ has axis $\vec u_4 = (0.6246950, 0.7808688, 0)$ at $51.34^{\circ}$, which is the velocity direction rotated by the Wigner angle, $\vec u_4 = \tilde u\vec u_5\tilde u^{-1}$. The two orderings do not agree: $\tilde U_1\tilde U_2$ is a different rotor, with the opposite sense of Wigner rotation, so the two boost directions do not merely "add".

## Problem 4: The Parent's Square-Root Relation and the Direction of the Boost

**Statement.** The companion article *The Lorentz Transformation as a Biquaternionic Rotation* states that the boost biquaternion associated with a four-velocity $\tilde{V} = \gamma(ic\,e_t+\vec v)$ is
$$
\tilde U = \sqrt{-\frac{i}{c}\tilde{V}^{\natural}},
\tag{14}
$$
with the square root branch selected by $\mathrm{Sc}(\tilde U)>0$.

**(a)** Verify (14) and the branch, and identify the rotor explicitly.

**(b)** Show that $\tilde U\tilde{V}\tilde U^{*} = ic\,e_t$: the rotor (14) carries the lab to the particle's rest frame.

**(c)** Show that the rotor that carries the rest four-velocity $ic\,e_t$ to $\tilde{V}$ is $\tilde U^{\natural}$, not $\tilde U$, and give the sign error that follows from using $\tilde U$ in that direction.

**(d)** State precisely what the four-velocity and the relation (14) determine.

**Solution. (a)** With $\tilde{V}^{\natural} = \gamma(ic\,e_t - \vec v)$,
$$
-\frac{i}{c}\tilde{V}^{\natural} = -\frac{i}{c}\gamma\left(ic\,e_t - \vec v\right)
= \gamma\,e_t + i\gamma\frac{\vec v}{c}.
$$
Writing $\gamma = \cosh\psi$, $\gamma v/c = \sinh\psi$, this is
$$
-\frac{i}{c}\tilde{V}^{\natural} = \cosh\psi + i\sinh\psi\,\vec u_6
= \exp\!\left(\psi\,i\vec u_6\right),
$$
where the exponential is hyperbolic because $(i\vec u_6)^2 = i^2\vec u_6^2 = (-1)(-1) = +e_t$. Its positive Hermitian square root is
$$
\tilde U = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u_6,
$$
which is precisely the boost biquaternion of *The Lorentz Transformation as a Biquaternionic Rotation* with $\vec u_x = \vec u_6$ and rapidity $\psi = \operatorname{atanh}(v/c)$. It is Hermitian and of unit norm. The element $-\tfrac{i}{c}\tilde{V}^{\natural}$ has eigenvalues $\exp(\pm\psi)>0$ in the matrix representation, so its two square roots are $\pm\tilde U$; the choice $\mathrm{Sc}>0$ selects $+\tilde U$. Note that the quaternion conjugate $\tilde U^{\natural}$, the boost of rapidity $-\psi$, is **not** a square root of $-\tfrac{i}{c}\tilde{V}^{\natural}$: it squares to $\cosh\psi - i\sinh\psi\vec u_6$. The two square roots differ by the kernel element $-1$ of $SL(2,\mathbb{C})\to SO^+(1,3)$ and generate the same Lorentz transformation; the conjugate is a different transformation.

**(b)** Since $\tilde U$ is Hermitian, $\tilde U^{*} = \tilde U$, and $P\,\tilde{V}\,P^\dagger$ for the pure boost reduces to a computation already made in Problem 1 with $\vec v_b = \vec v$ and $\psi_b = \psi_v$; by part (d) there, the rapidities subtract, $\psi_v-\psi_v = 0$, giving
$$
\tilde U\tilde{V}\tilde U^{*} = ic\,e_t .
$$
Equivalently, directly: $\tilde U\tilde{V}\tilde U^{*} = ic\gamma\tilde U^2 + \gamma v\,\tilde U\vec u_6\tilde U$, and since $\tilde U$ commutes with $\vec u_6$, $\tilde U\vec u_6\tilde U = \vec u_6\tilde U^2 = \cosh\psi\,\vec u_6 - i\sinh\psi$. Hence the vector part is $\gamma v\cosh\psi - c\gamma\sinh\psi = c\gamma\sinh\psi - c\gamma\sinh\psi = 0$ and the scalar part is $ic\gamma(\cosh\psi - \tanh\psi\sinh\psi) = ic$. So (14) is the rotor of the transformation *lab $\to$ rest*.

**(c)** Conjugating the rest four-velocity by $\tilde U$ instead gives
$$
\tilde U(ic\,e_t)\tilde U^{*} = ic\,\tilde U^2
= ic\left(\cosh\psi + i\sinh\psi\,\vec u_6\right)
= ic\cosh\psi\,e_t - c\sinh\psi\,\vec u_6,
$$
whose induced velocity is $-c\tanh\psi\,\vec u_6 = -\vec v$. Thus the rotor built from $\tilde{V}$ carries the lab to the rest frame and, applied in the opposite direction, produces the *negative* of the particle's velocity. The rotor that carries the rest frame to $\tilde{V}$ is the inverse, i.e. the quaternion conjugate:
$$
\tilde U^{\natural}\,(ic\,e_t)\,\overline{\tilde U} = ic\,(\tilde U^{\natural})^2 = ic\cosh\psi\,e_t + c\sinh\psi\,\vec u_6,
\qquad \text{velocity} = +\vec v.
$$
The sign is therefore fixed entirely by whether one uses $\tilde{V}^{\natural}$ (as the parent does) or $\tilde{V}$ in (14): the conjugate in the formula is what makes (14) the lab-to-rest rotor. The parent writes the formula but does not state the direction; a reader who reads "the boost biquaternion associated with $\tilde{V}$" as the rotor that *produces* $\tilde{V}$ will use $\tilde U$ where $\tilde U^{\natural}$ is required and obtain $-\vec v$ instead of $+\vec v$. This is a genuine gap in the parent's statement, although the formula itself is correct and its displayed verification (the four-potential transformation with $\vec v_b$ the boost velocity) is in the consistent direction.

**(d)** What relation (14) determines is the **Hermitian** (pure-boost) rotor. Given $\tilde{V}$, equation (14) has exactly the two solutions $\pm\tilde U$, and the branch $\mathrm{Sc}>0$ selects one; both generate the same Lorentz transformation. The quaternion conjugate $\tilde U^{\natural}$ is not a solution (it is the inverse transformation). More generally, if $P$ is any unit-norm rotor with $P\tilde{V}P^\dagger = ic\,e_t$, then $\tilde UP$ is another for every spatial rotation $\tilde u\in SU(2)$, since $\tilde u(ic\,e_t)\tilde u^{*} = ic\,\tilde u\tilde u^\dagger = ic\,e_t$. The four-velocity therefore determines the rotor only up to left multiplication by a rotation — equivalently, it determines the boost and leaves the orientation of the rest frame free. Among this family, (14) picks the unique Hermitian representative with positive scalar part (the other Hermitian member, $-\tilde U$, generates the same transformation). This is why the Thomas–Wigner rotation of Problem 3 is invisible in a single four-velocity but reappears in the composition of two of them: the four-velocity carries a boost, not a rotation.

## Problem 5: A Varying Rapidity, and the Boundary of Problem 2

**Statement.** Let the boost parameter vary along a scalar parameter $\tau$ instead of being fixed, and let the material coordinate of the moving frame's origin be
$$
\tilde{R}(\tau) = ic\,\tau\cosh\chi(\tau)\,e_t + c\,\tau\sinh\chi(\tau)\,\vec u_y,
\qquad \chi = \chi(\tau),
$$
so that $t = \tau\cosh\chi$ and the displacement along $\vec u_y$ is $x_1 = c\tau\sinh\chi$. Define the coordinate velocity by $\beta = (1/c)\,dx_1/dt$.

**(a)** Show that
$$
\beta(\tau) = \frac{\tanh\chi + \tau\chi'}{1 + \tau\chi'\tanh\chi},
\qquad \chi' = \frac{d\chi}{d\tau}.
$$

**(b)** Show that while $|\tau\chi'| < 1$ this is a rapidity addition, $\beta = \tanh(\chi+\psi)$ with $\tanh\psi = \tau\chi'$, and that for $|\tau\chi'| > 1$ no real $\psi$ exists, so $|\beta|$ need not stay below $1$.

**(c)** Show the interval identity
$$
c^2dt^2 - dx_1^2 = c^2d\tau_b^2\left(1 - (\tau\chi')^2\right),
$$
and read off when the worldline is timelike.

**(d)** For the linear profile $\chi(\tau) = \alpha\tau$, evaluate $\beta$ and find its maximum.

**Solution. (a)** Differentiate the two coordinate functions with respect to $\tau$:
$$
\frac{dx_1}{d\tau} = c\left(\sinh\chi + \tau\chi'\cosh\chi\right),
\qquad
\frac{dt}{d\tau} = \cosh\chi + \tau\chi'\sinh\chi .
$$
Both carry the same factor $\tau\chi'$ that a fixed rapidity would not have; their ratio is the stated expression. This is not the composition law (4), because the rotor here is a *different* rotor at every $\tau$: the second term is the rate at which the frame turns, not the rapidity of a second frame.

**(b)** Dividing numerator and denominator of (a) by $\cosh\chi$ gives
$$
\beta(\tau) = \frac{\tanh\chi + \tau\chi'}{1 + \tau\chi'\tanh\chi},
$$
which is the same rational form as the addition law of Problem 2(b), with $\tau\chi'$ in the place of $\tanh\psi_2$. Whenever $|\tau\chi'| < 1$ it is exactly $\tanh(\chi + \operatorname{atanh}(\tau\chi'))$, so the acceleration acts as an added rapidity and the bound $\beta < 1$ holds. For $|\tau\chi'| > 1$ no real rapidity has that tangent, and the bound is no longer forced: $\beta$ can pass through $1$.

**(c)** With $A = \cosh\chi$, $B = \sinh\chi$, $p = \tau\chi'$, the two derivatives are $c(B + pA)$ and $A + pB$, so
$$
\left(A+pB\right)^2 - \left(B+pA\right)^2 = \left(A^2-B^2\right)\left(1-p^2\right) = 1 - p^2 ,
$$
using $\cosh^2\chi - \sinh^2\chi = 1$. The worldline is timelike exactly while $|\tau\chi'| < 1$ and spacelike beyond, so the value $|\tau\chi'| = 1$ is precisely where it crosses the cone. The identity was checked on both sides for several profiles and values of $\tau$, agreeing to round-off.

**(d)** With $\chi = \alpha\tau$, so $\tau\chi' = \alpha\tau$,
$$
\beta = \frac{\tanh\alpha\tau + \alpha\tau}{1 + \alpha\tau\tanh\alpha\tau}.
$$
At $\alpha\tau = 1$ this is exactly $1$. For $\alpha\tau > 1$ it exceeds $1$, reaching its maximum $\beta = 1.02049$ at $\alpha\tau = \sqrt{2}$, and then decaying back towards $1$ from above as $\alpha\tau \to \infty$. The recomputed values $\beta(1.4) = 1.0204776$, $\beta(1.5) = 1.0201151$, $\beta(2) = 1.0122854$ reproduce the source's printed table to seven decimals; the table samples at $1.4$, while the exact maximum sits at $\sqrt{2}$.

**What this does and does not show.** It does not contradict Problem 2, and it does not open the light cone of *Causality and the Light Cone as an Information Barrier*. Problem 2 composes *fixed* rapidities, that is, inertial frames, and its bound is about that composition; the rotor here is a different rotor at every $\tau$, which is not a coordinate change to another inertial frame. What (c) identifies is that the worldline itself leaves the timelike region at $|\tau\chi'| = 1$, so past that point it is not the worldline of a material corpuscle. The construction and the profile are the source's, recorded and not adopted (I. Guzmán de Rojas, *Trajectories in space-time M4: Reinstating the Newtonian Time*, 2013); the four results above were recomputed from the source's printed formulas for this problem.

## Further Problems

The following are left to the reader; they extend the same tools and use the same notation.

1. **Boosting a four-momentum.** Starting from $\tilde{P} = m\tilde{V}$ and Problem 1, show that $\tilde U_{\vec v_b}\tilde{P}\tilde U_{\vec v_b}^{*} = iE'/c\,e_t + \vec p'$ with $E' = \gamma_b(E-\vec v_b\cdot\vec p)$ and $\vec p' = \vec p + (\gamma_b-1)\frac{\vec v_b\cdot\vec p}{v_b^2}\vec v_b - \gamma_b\frac{E}{c^2}\vec v_b$. Verify the mass shell $\tilde{P}'{\tilde{P}^{\natural}}' = -m^2c^2$ and recover the aberration of light by setting $m=0$.

2. **Antiparallel boosts.** For $\vec u_z = -\vec u_y$, show that $\tilde U_2\tilde U_1$ is a pure boost of rapidity $|\psi_1-\psi_2|$ (with the sign determined by which rapidity is larger) and that the Wigner angle (10) vanishes. Deduce the subtraction formula $w = |v_{b_1}-v_{b_2}|/(1-v_{b_1}v_{b_2}/c^2)$ and compare with Problem 1(d).

3. **The two orderings.** Show that $\tilde U_1\tilde U_2$ and $\tilde U_2\tilde U_1$ are related by conjugation with a unit quaternion, and determine the relative rotation. For equal projected rapidities show that the relative rotation is by $2\theta_W$ about $\vec u_{\vec v_{b_2}\times\vec v_{b_3}}$.

4. **The non-relativistic limit.** Expand (8) and (10) for $v_{b_i}/c\ll 1$. Show that the composed velocity tends to $\vec v_{b_1}+\vec v_{b_2}$ and that $\theta_W = O(v_{b_1}v_{b_2}/c^2)$, giving the leading correction to Galilean velocity addition. Identify which term in (5) is responsible for the Wigner rotation in this limit.

5. **Boost in a medium.** Redo Problems 1–3 with the local speed of light $c = 1/\sqrt{\epsilon\mu}$ in place of $c_0$, treating $c$ as a fixed local constant. Which of the results (1)–(12) change, and which are invariant? Discuss the sense in which the rotor becomes a field when $\epsilon$ and $\mu$ vary from point to point.

6. **A single four-velocity cannot see a rotation.** For a general unit-norm $P = \tilde{H}\tilde u$ show that the four-velocity of the frame reached from rest is $ic\,P^{-1}(P^{-1})^{*} = ic\,\tilde u^{-1}(\tilde{H}^{\natural})^2\tilde u$, and that $\tilde{H}$ alone (a boost) gives a different four-velocity unless $\tilde u$ commutes with $(\tilde{H}^{\natural})^2$. Reconcile this with Problem 4(d).

## Summary

We have applied the boost biquaternion and the rotor conjugation to four-velocities and to the composition of boosts.

1. **Boosting a four-velocity.** For $\tilde{V} = \gamma(ic\,e_t+\vec v)$ and $\tilde U_{\vec v_b} = \cosh\frac{\psi_b}{2}+i\sinh\frac{\psi_b}{2}\vec u_x$, the rotor conjugation gives (1): a four-velocity in $\mathbb{M}_-$ with $N = -c^2$, scalar part $ic\gamma_b\gamma(1-\vec v_b\cdot\vec v/c^2)$, and vector part $\gamma[\vec v+(\gamma_b-1)\frac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b-\gamma_b\vec v_b]$. The induced velocity is the standard parallel–perpendicular transformation (2); in the collinear case it is the rapidity subtraction $v' = (v-v_b)/(1-v_b v/c^2)$.

2. **Collinear composition.** Two boosts along one direction multiply to a pure boost of summed rapidity, (3), giving rapidity addition and the velocity-addition formula $w = (v_{b_1}+v_{b_2})/(1+v_{b_1}v_{b_2}/c^2)$.

3. **Non-collinear composition.** The product $P = \tilde U_2\tilde U_1$ is Hermitian only for parallel or antiparallel directions; otherwise it is a boost times a rotation, with total rapidity (8) and Thomas–Wigner angle (9)–(10), $\tan\frac{\theta_W}{2} = \frac{\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\sin\phi}{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2}+\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\phi}$, about the axis $\vec u_{\vec v_{b_2}\times\vec v_{b_3}}$ (11). For equal orthogonal rapidities $\tan\frac{\theta_W}{2} = \tanh^2\frac{\psi}{2}$ exactly. The numerical instance $\psi_1=\psi_2=\operatorname{atanh}0.6$, orthogonal, has composed speed $0.7683749c$ and Wigner angle $12.68038^{\circ}$.

4. **The parent's square-root relation.** $\tilde U = \sqrt{-\tfrac{i}{c}\tilde{V}^{\natural}} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_6$ is correct, with the branch $\mathrm{Sc}>0$; it is the **lab-to-rest** rotor, since $\tilde U\tilde{V}\tilde U^{*} = ic\,e_t$ and $\tilde U(ic\,e_t)\tilde U^{*}$ has velocity $-\vec v$. The rest-to-lab rotor is the conjugate $\tilde U^{\natural}$. The four-velocity determines the rotor only up to a rotation of the rest frame; (14) selects the Hermitian representative.

5. **A varying rapidity.** When the boost parameter is a function $\chi(\tau)$ of a scalar trajectory parameter, the coordinate velocity (Problem 5) is $\beta = (\tanh\chi + \tau\chi')/(1 + \tau\chi'\tanh\chi)$, the same rational form as the addition law with $\tau\chi'$ replacing a second rapidity, and the worldline is timelike exactly while $|\tau\chi'| < 1$. For $\chi = \alpha\tau$ the velocity reaches $1$ at $\alpha\tau = 1$ and peaks at $\beta = 1.02049$ at $\alpha\tau = \sqrt{2}$. This is not a counterexample to Problem 2: it composes a *varying* rotor, not two fixed rapidities, and past $|\tau\chi'| = 1$ the worldline is no longer timelike.

The exercise has also tested the parent. The parent's formula (14) is correct on every case computed here, including non-collinear directions; but the parent does not state the direction of the transformation it generates, and the conjugate $\tilde{V}^{\natural}$ inside the formula is what fixes that direction to lab-to-rest. (A companion exercise in this series, *The Relativistic Kinematics of a Two-Body Decay*, discusses the same direction convention in a different application.) Here the parent's own displayed application is consistent, and the gap is only in the statement; every equation of the parent used here was verified on cases chosen independently of the ones that motivated it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace (rotation rotors) |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $c$, $c_0$ | Speed of light in the medium, and in vacuum |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\tilde{Q}^{\natural}$, $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ | Quaternion conjugate, Hermitian conjugate |
| $\tilde{V} = \gamma(ic\,e_t+\vec v)$ | Four-velocity, $\langle\tilde{V}\rangle_{\natural}=-c^2$ |
| $\tilde{P} = m\tilde{V} = iE/c\,e_t+\vec p$ | Four-momentum |
| $\gamma = (1-\vec v^2/c^2)^{-1/2}$, $\gamma_b$ | Lorentz factors |
| $\tilde U_{\vec v_b} = \cosh\frac{\psi_b}{2}+i\sinh\frac{\psi_b}{2}\vec u_x$ | Boost biquaternion, $\tanh\psi_b = v_b/c$ |
| $\psi_v$, $\psi_1$, $\psi_2$ | Rapidities |
| $\vec v_b$, $\vec {u_y}_i$ | Boost velocity, boost directions |
| $\phi$ | Angle between $\vec u_y$ and $\vec u_z$ |
| $P = \tilde U_2\tilde U_1$ | Product of two boost rotors |
| $a$, $\vec q$, $\vec w$ | Real scalar, real vector, real vector in $P = a+\vec q+i\vec w$ |
| $\tilde{H}$, $\tilde u$ | Boost part and rotation part of $P = \tilde{H}\tilde u$ |
| $\Psi$ | Total rapidity, $\cosh\Psi = \cosh\psi_1\cosh\psi_2+\sinh\psi_1\sinh\psi_2\cos\phi$ |
| $\theta_W$ | Thomas–Wigner angle |
| $\vec u_4$ | Axis of the boost part $\tilde{H}$ |
| $\vec u_{\mathrm r} = \vec u_{\vec v_{b_2}\times\vec v_{b_3}}$ | Axis of the Wigner rotation |
| $\mathrm{Sc}$, $\mathrm{Tr}$ | Scalar part, trace; $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ |

## Further Reading

- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the original velocity-addition theorem.
- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard transformation of four-velocities and the velocity-addition formula.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the parallel–perpendicular decomposition and the four-potential transformation.
- E. P. Wigner, "On Unitary Representations of the Inhomogeneous Lorentz Group," *Annals of Mathematics* **40** (1939) 149–204, and the Thomas precession literature, for the rotation that accompanies the composition of non-collinear boosts.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of boosts and the composition of Lorentz transformations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the double cover $SL(2,\mathbb{C})\to SO^+(1,3)$ and the branch of the square root.
- The companion articles of this series: *Relativistic Mechanics in Biquaternionic Form*, *The Lorentz Transformation as a Biquaternionic Rotation*, and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*.
- I. Guzmán de Rojas, *Trajectories in space-time M4: Reinstating the Newtonian Time*, Communication to the National Academy of Sciences of Bolivia (2013), for the time-dependent rapidity of Problem 5: the coordinate velocity of an accelerated parametrisation, the interval identity that fixes where the worldline ceases to be timelike, and the maximum $\beta = 1.02049$ at $\alpha\tau = \sqrt{2}$. Cited as an external construction, not adopted; the source's printed table was recomputed here and reproduces to seven decimals.
