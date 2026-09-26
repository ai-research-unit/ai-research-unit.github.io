# __Exercise: Boosting a Four-Velocity and Rapidity Composition__

## Introduction

This is one of the exercises in the relativity series. It applies the apparatus of two companion articles: *The Lorentz Transformation as a Biquaternionic Rotation*, which defines the boost biquaternion, the rotor conjugation, and the square-root relation between the rotor and the four-velocity; and *Relativistic Mechanics in Biquaternionic Form*, which fixes the four-velocity and the four-momentum in $\mathbb{M}_-$. Those two articles are the parents of this exercise: every result below is obtained from the tools already defined there, and no new formalism is introduced. The sequence is: boost a general four-velocity (Problem 1); compose two collinear boosts and recover rapidity addition and velocity addition (Problem 2); compose two non-collinear boosts and extract the Thomas–Wigner rotation (Problem 3); and examine the parent's square-root relation between the four-velocity and the boost rotor, whose direction the parent does not state (Problem 4). A set of further problems is left to the reader.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, and the scalar imaginary $i$ with $i^2 = -1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part), the Hermitian subspace $\mathbb{M}_+$ (real scalar part, imaginary vector part), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$, and the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ of the rotation rotors. The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, the quaternion conjugate $\bar{\tilde{Q}}$, the Hermitian conjugate $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{*}$, and the rotor conjugation $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ belongs to the shared notation; no object of the informational sector arises below, so it is recorded but not used. The four-velocity $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ with $N(\tilde{U}) = -c^2$ and $\gamma = (1-\mathbf{v}^2/c^2)^{-1/2}$, the four-momentum $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$, and the boost biquaternion
$$
\tilde{\Lambda}_{\mathbf{u}} = \cosh\frac{\psi_u}{2} + i\sinh\frac{\psi_u}{2}\hat{\mathbf{u}},
\qquad
\tanh\psi_u = \frac{u}{c},
$$
which is Hermitian ($\tilde{\Lambda}_{\mathbf{u}}^\dagger = \tilde{\Lambda}_{\mathbf{u}}$), lies in $\mathbb{M}_+$, and has unit norm form. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value; $\mathbf{v}$ is a particle velocity, and $\hat{\mathbf{u}}, \hat{\mathbf{n}}$ are unit frame or boost directions. The components of a biquaternion are taken in the basis $(e_0,e_1,e_2,e_3)$.

**What is to be shown.** Problem 1 computes $\tilde{\Lambda}_{\mathbf{u}}\tilde{U}\tilde{\Lambda}_{\mathbf{u}}^\dagger$ for arbitrary $\mathbf{u},\mathbf{v}$ and shows that it is again a four-velocity of $\mathbb{M}_-$ with the standard components. Problem 2 composes two collinear boost rotors and derives rapidity addition and the velocity-addition formula. Problem 3 composes two non-collinear boosts, shows that the product is no longer a pure boost, and extracts the boost part, the total rapidity, and the Thomas–Wigner angle. Problem 4 verifies the parent's relation $\tilde{\Lambda} = \sqrt{-\tfrac{i}{c}\bar{\tilde{U}}}$, determines the direction of the transformation it generates, and identifies what the four-velocity does and does not determine. The problems are solved in full; the reader is asked in the final section to extend them.

## Problem 1: The Boost of a General Four-Velocity

**Statement.** Let $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ be the four-velocity of a particle, and let $\tilde{\Lambda}_{\mathbf{u}} = \cosh\frac{\psi_u}{2} + i\sinh\frac{\psi_u}{2}\hat{\mathbf{u}}$, with $\tanh\psi_u = u/c$, be a boost biquaternion. Compute $\tilde{U}' = \tilde{\Lambda}_{\mathbf{u}}\tilde{U}\tilde{\Lambda}_{\mathbf{u}}^\dagger$ and show that:

**(a)** $\tilde{U}'$ lies in $\mathbb{M}_-$ and has $N(\tilde{U}') = -c^2$;

**(b)** its scalar part is $ic\,\gamma'$ with $\gamma' = \gamma_u\gamma\left(1 - \mathbf{u}\cdot\mathbf{v}/c^2\right)$, where $\gamma_u = (1-u^2/c^2)^{-1/2}$;

**(c)** its vector part is $\gamma\left[\mathbf{v} + (\gamma_u-1)\dfrac{\mathbf{u}\cdot\mathbf{v}}{u^2}\mathbf{u} - \gamma_u\mathbf{u}\right]$, so that the induced velocity is the standard parallel–perpendicular transformation;

**(d)** in the collinear case $\mathbf{v}\parallel\mathbf{u}$ the induced velocity is $v' = (v-u)/(1-uv/c^2)$, i.e. the rapidities subtract.

**Solution.** Because a pure-boost rotor is Hermitian, $\tilde{\Lambda}_{\mathbf{u}}^\dagger = \tilde{\Lambda}_{\mathbf{u}}$, and the transformation is the two-sided product $\tilde{\Lambda}_{\mathbf{u}}\tilde{U}\tilde{\Lambda}_{\mathbf{u}}$. Write $a = \cosh\frac{\psi_u}{2}$, $b = \sinh\frac{\psi_u}{2}$, and $J = \hat{\mathbf{u}}$, a real unit pure quaternion with $J^2 = -e_0$. Split the velocity into parts parallel and perpendicular to $J$,
$$
\mathbf{v} = \mathbf{v}_\parallel + \mathbf{v}_\perp, \qquad \mathbf{v}_\parallel = v_\parallel J, \qquad J\,\mathbf{v}_\parallel = -v_\parallel, \qquad J\,\mathbf{v}_\perp = J\times\mathbf{v}_\perp, \qquad \mathbf{v}_\perp J = -J\times\mathbf{v}_\perp .
$$
The first product expands as
$$
\tilde{\Lambda}\tilde{U} = ic\gamma\,\tilde{\Lambda} + \gamma\,\tilde{\Lambda}\mathbf{v}
= ic\gamma a - c\gamma b\,J + \gamma\left(a\mathbf{v}_\parallel + a\mathbf{v}_\perp - i b v_\parallel + i b\,J\times\mathbf{v}_\perp\right).
$$
Multiplying once more on the right by $\tilde{\Lambda} = a + ibJ$ and collecting the scalar and vector parts gives
$$
\tilde{\Lambda}_{\mathbf{u}}\tilde{U}\tilde{\Lambda}_{\mathbf{u}}^\dagger
= ic\,\gamma_u\gamma\left(1 - \frac{\mathbf{u}\cdot\mathbf{v}}{c^2}\right)e_0
+ \gamma\left[\mathbf{v} + (\gamma_u-1)\frac{\mathbf{u}\cdot\mathbf{v}}{u^2}\mathbf{u} - \gamma_u\mathbf{u}\right].
\tag{1}
$$
The identity $\sinh\psi_u = \gamma_u u/c$ and the expansion of the parallel component have been used. The result is the biquaternion form of the standard Lorentz transformation of a four-velocity from the lab to the frame moving with velocity $\mathbf{u}$.

**(a)** In (1) the scalar coefficient is purely imaginary and the vector coefficient is real, so $\tilde{U}'\in\mathbb{M}_-$. Its norm form is preserved because $N$ is multiplicative and $N(\tilde{\Lambda}_{\mathbf{u}}) = 1$:
$$
N(\tilde{U}') = N(\tilde{\Lambda}_{\mathbf{u}})\,N(\tilde{U})\,N(\tilde{\Lambda}_{\mathbf{u}})^{*} = 1\cdot(-c^2)\cdot 1 = -c^2 .
$$
The transformation therefore maps four-velocities to four-velocities; this is the algebraic content of Lorentz covariance in $\mathbb{M}_-$.

**(b)** Reading off the scalar coefficient of (1), $\gamma' = \gamma_u\gamma(1-\mathbf{u}\cdot\mathbf{v}/c^2)$. This is positive for $u,v<c$, since $\mathbf{u}\cdot\mathbf{v}\le uv < c^2$. It is the standard transformation of energy, $E'/c = \gamma_u(E/c - \mathbf{u}\cdot\mathbf{p}/c)$, written for the four-velocity.

**(c)** The induced velocity is the vector coefficient divided by $\gamma'$,
$$
\mathbf{v}' = \frac{\mathbf{v} + (\gamma_u-1)\dfrac{\mathbf{u}\cdot\mathbf{v}}{u^2}\mathbf{u} - \gamma_u\mathbf{u}}{\gamma_u\left(1 - \mathbf{u}\cdot\mathbf{v}/c^2\right)}
= \frac{\mathbf{v}_\parallel - \mathbf{u}}{1 - \mathbf{u}\cdot\mathbf{v}/c^2} + \frac{\mathbf{v}_\perp}{\gamma_u\left(1 - \mathbf{u}\cdot\mathbf{v}/c^2\right)},
\tag{2}
$$
which is the standard transformation. The second equality uses $\mathbf{v}_\parallel = \frac{\mathbf{u}\cdot\mathbf{v}}{u^2}\mathbf{u}$ and the rearrangement $\mathbf{v} + (\gamma_u-1)\mathbf{v}_\parallel - \gamma_u\mathbf{u} = \mathbf{v}_\perp + \gamma_u(\mathbf{v}_\parallel-\mathbf{u})$.

**(d)** If $\mathbf{v} = v\hat{\mathbf{u}}$ then $\mathbf{v}_\perp = 0$ and (2) reduces to
$$
v' = \frac{v-u}{1-uv/c^2},
$$
so that in rapidities $v' = c\tanh(\psi_v - \psi_u)$: **a boost subtracts its rapidity from the rapidity of the four-velocity it acts on.** This is the statement that the transformation (1) is the lab-to-moving-frame map, and it fixes the direction convention used throughout: the rotor $\tilde{\Lambda}_{\mathbf{u}}$ carries the lab to the frame moving with $+\mathbf{u}$, so the particle's speed is reduced by $u$.

**Numerical instance.** Take $\mathbf{v} = 0.6c\,e_1$ and $\mathbf{u} = 0.5c\,e_2$, orthogonal. Then $\gamma = 1.25$, $\gamma_u = 1.1547005$, $\mathbf{u}\cdot\mathbf{v} = 0$, and from (1)
$$
\gamma' = \gamma_u\gamma = 1.4433757, \qquad
\mathbf{v}' = \begin{pmatrix} 0.5196152 \\ -0.5 \\ 0\end{pmatrix}c, \qquad |\mathbf{v}'| = 0.7211103\,c .
$$
The norm is preserved: $N(\tilde{U}') = -1$ in units $c=1$. The transverse component is contracted by $1/\gamma_u$ (from $0.6c$ to $0.5196c$) and the boost direction acquires the recoil $-u$; this is (2) term by term.

## Problem 2: Collinear Boosts and Rapidity Addition

**Statement.** Let $\tilde{\Lambda}_1 = \cosh\frac{\psi_1}{2} + i\sinh\frac{\psi_1}{2}\hat{\mathbf{n}}$ and $\tilde{\Lambda}_2 = \cosh\frac{\psi_2}{2} + i\sinh\frac{\psi_2}{2}\hat{\mathbf{n}}$ be two boost rotors along the same direction $\hat{\mathbf{n}}$.

**(a)** Show that $\tilde{\Lambda}_2\tilde{\Lambda}_1$ is itself a pure boost along $\hat{\mathbf{n}}$, of rapidity $\psi_1+\psi_2$.

**(b)** Deduce the velocity-addition formula $w = \dfrac{u_1+u_2}{1+u_1u_2/c^2}$.

**(c)** Reconcile the addition here with the subtraction found in Problem 1.

**Solution. (a)** Put $J = \hat{\mathbf{n}}$, $c_i = \cosh\frac{\psi_i}{2}$, $s_i = \sinh\frac{\psi_i}{2}$. Since $J^2 = -e_0$, the product of the two scalar-imaginary vector parts is
$$
(iJ)(iJ) = i^2J^2 = (-1)(-1) = +e_0,
$$
so the two boosts in the same direction multiply hyperbolically:
$$
\tilde{\Lambda}_2\tilde{\Lambda}_1
= \left(c_1c_2 + s_1s_2\right) + i\left(c_1s_2 + s_1c_2\right)J
= \cosh\frac{\psi_1+\psi_2}{2} + i\sinh\frac{\psi_1+\psi_2}{2}\hat{\mathbf{n}}
= \tilde{\Lambda}(\psi_1+\psi_2).
\tag{3}
$$
The cross terms combine by the addition formulas for $\cosh$ and $\sinh$. The product is Hermitian, lies in $\mathbb{M}_+$, and has unit norm, so it is a pure boost along $\hat{\mathbf{n}}$: **boosts in a common direction form a one-parameter subgroup**, and their rapidities add.

**(b)** The product rotor has rapidity $\psi_1+\psi_2$, and the velocity it represents is $w = c\tanh(\psi_1+\psi_2)$. Using $\tanh\psi_i = u_i/c$,
$$
w = c\,\frac{\tanh\psi_1 + \tanh\psi_2}{1 + \tanh\psi_1\tanh\psi_2}
= \frac{u_1+u_2}{1 + u_1u_2/c^2}.
\tag{4}
$$
For $u_1 = 0.5c$, $u_2 = 0.6c$ this gives $w = 1.1c/1.3 = 0.8461538c$, which is $\tanh(\operatorname{atanh}0.5 + \operatorname{atanh}0.6)$ to machine precision.

**(c)** There is no contradiction with Problem 1. Equation (3) is the composition of two *coordinate changes*: the rotor $\tilde{\Lambda}_2\tilde{\Lambda}_1$ carries the lab to the frame moving with $w$. Equation (2) of Problem 1 is the action of a *single* coordinate change on a four-velocity: it subtracts the frame rapidity. The two statements are the multiplication and the action of the same group, and in the collinear case the action's rapidity shift is the group's rapidity sum with a sign, $v' = c\tanh(\psi_v-\psi_u)$.

## Problem 3: Non-Collinear Boosts and the Thomas–Wigner Rotation

**Statement.** Let $\tilde{\Lambda}_1$ have rapidity $\psi_1$ along $\hat{\mathbf{n}}_1$ and $\tilde{\Lambda}_2$ rapidity $\psi_2$ along $\hat{\mathbf{n}}_2$, with $\hat{\mathbf{n}}_1\cdot\hat{\mathbf{n}}_2 = \cos\phi$ and $0<\phi<\pi$.

**(a)** Compute the product $P = \tilde{\Lambda}_2\tilde{\Lambda}_1$ and show that it is Hermitian if and only if $\phi\in\{0,\pi\}$; for $0<\phi<\pi$ it is not a pure boost.

**(b)** Show that $P$ admits the decomposition $P = \tilde{H}\tilde{R}$ with $\tilde{H}$ a pure boost of unit norm and $\tilde{R}$ a spatial rotation. Derive the total rapidity $\Psi$, the Wigner angle $\theta_W$, and the rotation axis.

**(c)** Verify the special case of equal orthogonal rapidities, and compute a numerical instance.

**Solution. (a)** With $c_i = \cosh\frac{\psi_i}{2}$, $s_i = \sinh\frac{\psi_i}{2}$, $J_i = \hat{\mathbf{n}}_i$, and the quaternion product identity $J_2J_1 = -J_2\cdot J_1 + J_2\times J_1$ for unit pure quaternions,
$$
(iJ_2)(iJ_1) = -J_2J_1 = \cos\phi + J_1\times J_2 .
$$
Hence
$$
P = \tilde{\Lambda}_2\tilde{\Lambda}_1
= \underbrace{\left(c_1c_2 + s_1s_2\cos\phi\right)}_{a}
+ \underbrace{s_1s_2\,\hat{\mathbf{n}}_1\times\hat{\mathbf{n}}_2}_{\mathbf{q}}
+ i\underbrace{\left(c_2s_1\hat{\mathbf{n}}_1 + c_1s_2\hat{\mathbf{n}}_2\right)}_{\mathbf{w}},
\tag{5}
$$
where $a$ is a real scalar, $\mathbf{q}$ is a real vector of magnitude $s_1s_2\sin\phi$, and $i\mathbf{w}$ is an imaginary vector. The real vector part $\mathbf{q}$ is orthogonal to $\mathbf{w}$, because $\mathbf{n}_1\times\mathbf{n}_2$ is orthogonal to both $\hat{\mathbf{n}}_1$ and $\hat{\mathbf{n}}_2$. The element $P$ is Hermitian exactly when its real vector part vanishes, i.e. when $s_1s_2\sin\phi = 0$. For nonzero rapidities this means $\sin\phi = 0$, so a product of two boosts is a pure boost only when the two directions are parallel or antiparallel. Otherwise it is a boost together with a rotation: the product has left $\mathbb{M}_+$.

**(b)** Write $P = a + \mathbf{q} + i\mathbf{w}$. Its norm form is, using $\mathbf{q}\cdot\mathbf{w}=0$,
$$
N(P) = a^2 + |\mathbf{q}|^2 - |\mathbf{w}|^2 = 1,
\tag{6}
$$
because $P$ is a product of two unit-norm elements. Then
$$
P^\dagger = \bar{P}^{*} = a - \mathbf{q} + i\mathbf{w},
$$
and, since a real vector anticommutes with an orthogonal real vector,
$$
P P^\dagger = \left(a^2 + |\mathbf{q}|^2 + |\mathbf{w}|^2\right) + 2i\left(a\mathbf{w} + \mathbf{q}\times\mathbf{w}\right)
\equiv \Sigma + i\mathbf{T}.
\tag{7}
$$
The element $PP^\dagger$ is Hermitian and positive (it is $\tilde{H}^2$ for the required boost), so it has a unique positive Hermitian square root
$$
\tilde{H} = \sqrt{PP^\dagger} = \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\hat{\mathbf{m}},
\qquad
\cosh\Psi = \Sigma, \quad \sinh\Psi\,\hat{\mathbf{m}} = \mathbf{T}.
$$
Expanding $\Sigma = a^2 + |\mathbf{q}|^2 + |\mathbf{w}|^2$ with the definitions (5) and simplifying gives the standard total rapidity
$$
\cosh\Psi = \cosh\psi_1\cosh\psi_2 + \sinh\psi_1\sinh\psi_2\cos\phi .
\tag{8}
$$
The residual element
$$
\tilde{R} = \tilde{H}^{-1}P = \bar{\tilde{H}}P
= \left(\cosh\frac{\Psi}{2} - i\sinh\frac{\Psi}{2}\hat{\mathbf{m}}\right)\left(a + \mathbf{q} + i\mathbf{w}\right)
$$
is the unitary factor of the polar decomposition of $P$ (equivalently $N(\tilde{R}) = N(\tilde{H})^{-1}N(P) = 1$ and $\tilde{R}\bar{\tilde{R}} = e_0$ with $\tilde{R}$ a unit real quaternion). Its scalar part is
$$
\mathrm{Sc}(\tilde{R}) = a\cosh\frac{\Psi}{2} - \sinh\frac{\Psi}{2}\left(\hat{\mathbf{m}}\cdot\mathbf{w}\right),
$$
where the minus sign comes from the $-\mathbf{A}\cdot\mathbf{B}$ term of the quaternion product, and the term involving $\mathbf{q}$ vanishes because $\hat{\mathbf{m}}\perp\mathbf{q}$. Now $\hat{\mathbf{m}}\cdot\mathbf{w} = \mathbf{T}\cdot\mathbf{w}/\sinh\Psi = 2a|\mathbf{w}|^2/\sinh\Psi$, so
$$
\mathrm{Sc}(\tilde{R}) = a\cosh\frac{\Psi}{2} - \frac{a|\mathbf{w}|^2}{\cosh\frac{\Psi}{2}}
= \frac{a\left(\cosh^2\frac{\Psi}{2} - |\mathbf{w}|^2\right)}{\cosh\frac{\Psi}{2}} .
$$
From (6) and $\Sigma$ one has $\cosh^2\frac{\Psi}{2} = \frac{1+\Sigma}{2} = a^2 + |\mathbf{q}|^2 = 1 + |\mathbf{w}|^2$, so $\cosh^2\frac{\Psi}{2} - |\mathbf{w}|^2 = 1$ and
$$
\mathrm{Sc}(\tilde{R}) = \frac{a}{\cosh\frac{\Psi}{2}}.
$$
Because $\tilde{R}$ is a unit real quaternion — a spatial rotation rotor — it has the form $\tilde{R} = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\hat{\mathbf{k}}$ with $\hat{\mathbf{k}}$ its axis. Comparing scalar parts identifies the **Thomas–Wigner angle** $\theta_W$:
$$
\cos\frac{\theta_W}{2} = \frac{a}{\cosh\frac{\Psi}{2}}
= \frac{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2} + \sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\phi}{\cosh\frac{\Psi}{2}},
\tag{9}
$$
and, since $|\mathbf{q}|^2 = \sinh^2\frac{\psi_1}{2}\sinh^2\frac{\psi_2}{2}\sin^2\phi$ and $\sin\frac{\theta_W}{2} = |\mathbf{q}|/\cosh\frac{\Psi}{2}$,
$$
\tan\frac{\theta_W}{2} = \frac{|\mathbf{q}|}{a}
= \frac{\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\sin\phi}{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2} + \sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\phi}.
\tag{10}
$$
The numerator is non-negative for $0<\phi<\pi$ and the denominator $a$ is positive for every $\phi$, since $a\ge\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2} - \sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2} = \cosh\frac{\psi_1-\psi_2}{2}>0$. Hence $0\le\theta_W<\pi$. The rotation axis is the normal to the plane of the two boost directions,
$$
\hat{\mathbf{k}} = \widehat{\mathbf{n}_1\times\mathbf{n}_2},
\tag{11}
$$
which we verified numerically in several non-coplanar configurations; it is the direction of the antisymmetric, real-vector part $\mathbf{q}$ of $P$ in (5). With this, the decomposition is
$$
\tilde{\Lambda}_2\tilde{\Lambda}_1 = \tilde{H}\tilde{R},
\qquad
\tilde{H} = \cosh\frac{\Psi}{2} + i\sinh\frac{\Psi}{2}\hat{\mathbf{m}},
\qquad
\tilde{R} = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\widehat{\mathbf{n}_1\times\mathbf{n}_2}.
\tag{12}
$$
The rotation is intrinsic, but the split of $P$ into boost and rotation is only canonical in the right-polar sense (12). The alternative left-polar form $P = \tilde{R}\tilde{H}'$ with $\tilde{H}' = \tilde{R}^{-1}\tilde{H}\tilde{R}$ is an equally valid boost-times-rotation decomposition, with a boost of the same rapidity $\Psi$ but a different axis; only $\Psi$ and $\theta_W$ are convention-independent. This is the sense in which the parent's statement that a non-collinear product is "a boost plus a spatial rotation" is complete only after the ordering is fixed.

**(c)** For equal orthogonal rapidities, $\psi_1 = \psi_2 = \psi$ and $\phi = \pi/2$, so $\cosh\Psi = \cosh^2\psi$ and $a = \cosh^2\frac{\psi}{2}$. Then $\cos\frac{\theta_W}{2} = \cosh^2\frac{\psi}{2}\big/\cosh\frac{\Psi}{2}$, and (10) collapses to
$$
\tan\frac{\theta_W}{2} = \frac{\sinh^2\frac{\psi}{2}}{\cosh^2\frac{\psi}{2}} = \tanh^2\frac{\psi}{2}.
\tag{13}
$$
This is exact; it was checked numerically for $\psi = 0.5, 1, 1.5, 2, 3$ to $10^{-12}$.

**Numerical instance.** Take $\psi_1 = \psi_2 = \operatorname{atanh}0.6 = 0.6931472$ along $\hat{\mathbf{n}}_1 = \hat{e}_1$ and $\hat{\mathbf{n}}_2 = \hat{e}_2$, so that each boost has speed $0.6c$. Then (5) gives, in the basis $(e_0,e_1,e_2,e_3)$,
$$
P = \tilde{\Lambda}_2\tilde{\Lambda}_1 = 1.125 + 0.375\,i\,e_1 + 0.375\,i\,e_2 + 0.125\,e_3,
$$
which is not Hermitian: the real $e_3$ term $s_1s_2 = 0.125$ is the antisymmetric part. From (8), $\Psi = 1.0163481$ and the composed frame has speed $c\tanh\Psi = 0.7683749c$; the velocity-addition formula (2) applied twice gives the same speed. The Wigner angle (9)–(10) is $\theta_W = 12.68038^{\circ} = 0.2213144$ rad, with
$$
\tilde{R} = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\hat{e}_3 = 0.9938837 + 0.1104315\,\hat{e}_3 .
$$
The frame reached by $P$ has, in the lab, the four-velocity $ic\,P^{-1}(P^{-1})^\dagger = 1.5625i\,e_0 + 0.9375\,e_1 + 0.75\,e_2$, i.e. velocity $(0.6, 0.48, 0)c$: magnitude $0.7683749c$ and direction $38.66^{\circ}$ from $\hat{e}_1$. The boost part $\tilde{H}$ has axis $\hat{\mathbf{m}} = (0.6246950, 0.7808688, 0)$ at $51.34^{\circ}$, which is the velocity direction rotated by the Wigner angle, $\hat{\mathbf{m}} = \tilde{R}\hat{\mathbf{V}}\tilde{R}^{-1}$. The two orderings do not agree: $\tilde{\Lambda}_1\tilde{\Lambda}_2$ is a different rotor, with the opposite sense of Wigner rotation, so the two boost directions do not merely "add".

## Problem 4: The Parent's Square-Root Relation and the Direction of the Boost

**Statement.** The companion article *The Lorentz Transformation as a Biquaternionic Rotation* states that the boost biquaternion associated with a four-velocity $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$ is
$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\bar{\tilde{U}}},
\tag{14}
$$
with the square root branch selected by $\mathrm{Sc}(\tilde{\Lambda})>0$.

**(a)** Verify (14) and the branch, and identify the rotor explicitly.

**(b)** Show that $\tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger = ic\,e_0$: the rotor (14) carries the lab to the particle's rest frame.

**(c)** Show that the rotor that carries the rest four-velocity $ic\,e_0$ to $\tilde{U}$ is $\bar{\tilde{\Lambda}}$, not $\tilde{\Lambda}$, and give the sign error that follows from using $\tilde{\Lambda}$ in that direction.

**(d)** State precisely what the four-velocity and the relation (14) determine.

**Solution. (a)** With $\bar{\tilde{U}} = \gamma(ic\,e_0 - \mathbf{v})$,
$$
-\frac{i}{c}\bar{\tilde{U}} = -\frac{i}{c}\gamma\left(ic\,e_0 - \mathbf{v}\right)
= \gamma\,e_0 + i\gamma\frac{\mathbf{v}}{c}.
$$
Writing $\gamma = \cosh\psi$, $\gamma v/c = \sinh\psi$, this is
$$
-\frac{i}{c}\bar{\tilde{U}} = \cosh\psi + i\sinh\psi\,\hat{\mathbf{v}}
= \exp\!\left(\psi\,i\hat{\mathbf{v}}\right),
$$
where the exponential is hyperbolic because $(i\hat{\mathbf{v}})^2 = i^2\hat{\mathbf{v}}^2 = (-1)(-1) = +e_0$. Its positive Hermitian square root is
$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{v}},
$$
which is precisely the boost biquaternion of *The Lorentz Transformation as a Biquaternionic Rotation* with $\hat{\mathbf{u}} = \hat{\mathbf{v}}$ and rapidity $\psi = \operatorname{atanh}(v/c)$. It is Hermitian and of unit norm. The element $-\tfrac{i}{c}\bar{\tilde{U}}$ has eigenvalues $e^{\pm\psi}>0$ in the matrix representation, so its two square roots are $\pm\tilde{\Lambda}$; the choice $\mathrm{Sc}>0$ selects $+\tilde{\Lambda}$. Note that the quaternion conjugate $\bar{\tilde{\Lambda}}$, the boost of rapidity $-\psi$, is **not** a square root of $-\tfrac{i}{c}\bar{\tilde{U}}$: it squares to $\cosh\psi - i\sinh\psi\hat{\mathbf{v}}$. The two square roots differ by the kernel element $-1$ of $SL(2,\mathbb{C})\to SO^+(1,3)$ and generate the same Lorentz transformation; the conjugate is a different transformation.

**(b)** Since $\tilde{\Lambda}$ is Hermitian, $\tilde{\Lambda}^{\dagger} = \tilde{\Lambda}$, and $P\,\tilde{U}\,P^\dagger$ for the pure boost reduces to a computation already made in Problem 1 with $\mathbf{u} = \mathbf{v}$ and $\psi_u = \psi_v$; by part (d) there, the rapidities subtract, $\psi_v-\psi_v = 0$, giving
$$
\tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger = ic\,e_0 .
$$
Equivalently, directly: $\tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger = ic\gamma\tilde{\Lambda}^2 + \gamma v\,\tilde{\Lambda}\hat{\mathbf{v}}\tilde{\Lambda}$, and since $\tilde{\Lambda}$ commutes with $\hat{\mathbf{v}}$, $\tilde{\Lambda}\hat{\mathbf{v}}\tilde{\Lambda} = \hat{\mathbf{v}}\tilde{\Lambda}^2 = \cosh\psi\,\hat{\mathbf{v}} - i\sinh\psi$. Hence the vector part is $\gamma v\cosh\psi - c\gamma\sinh\psi = c\gamma\sinh\psi - c\gamma\sinh\psi = 0$ and the scalar part is $ic\gamma(\cosh\psi - \tanh\psi\sinh\psi) = ic$. So (14) is the rotor of the transformation *lab $\to$ rest*.

**(c)** Conjugating the rest four-velocity by $\tilde{\Lambda}$ instead gives
$$
\tilde{\Lambda}(ic\,e_0)\tilde{\Lambda}^\dagger = ic\,\tilde{\Lambda}^2
= ic\left(\cosh\psi + i\sinh\psi\,\hat{\mathbf{v}}\right)
= ic\cosh\psi\,e_0 - c\sinh\psi\,\hat{\mathbf{v}},
$$
whose induced velocity is $-c\tanh\psi\,\hat{\mathbf{v}} = -\mathbf{v}$. Thus the rotor built from $\tilde{U}$ carries the lab to the rest frame and, applied in the opposite direction, produces the *negative* of the particle's velocity. The rotor that carries the rest frame to $\tilde{U}$ is the inverse, i.e. the quaternion conjugate:
$$
\bar{\tilde{\Lambda}}\,(ic\,e_0)\,\bar{\tilde{\Lambda}}^\dagger = ic\,\bar{\tilde{\Lambda}}^2 = ic\cosh\psi\,e_0 + c\sinh\psi\,\hat{\mathbf{v}},
\qquad \text{velocity} = +\mathbf{v}.
$$
The sign is therefore fixed entirely by whether one uses $\bar{\tilde{U}}$ (as the parent does) or $\tilde{U}$ in (14): the conjugate in the formula is what makes (14) the lab-to-rest rotor. The parent writes the formula but does not state the direction; a reader who reads "the boost biquaternion associated with $\tilde{U}$" as the rotor that *produces* $\tilde{U}$ will use $\tilde{\Lambda}$ where $\bar{\tilde{\Lambda}}$ is required and obtain $-\mathbf{v}$ instead of $+\mathbf{v}$. This is a genuine gap in the parent's statement, although the formula itself is correct and its displayed verification (the four-potential transformation with $\mathbf{u}$ the boost velocity) is in the consistent direction.

**(d)** What relation (14) determines is the **Hermitian** (pure-boost) rotor. Given $\tilde{U}$, equation (14) has exactly the two solutions $\pm\tilde{\Lambda}$, and the branch $\mathrm{Sc}>0$ selects one; both generate the same Lorentz transformation. The quaternion conjugate $\bar{\tilde{\Lambda}}$ is not a solution (it is the inverse transformation). More generally, if $P$ is any unit-norm rotor with $P\tilde{U}P^\dagger = ic\,e_0$, then $QP$ is another for every spatial rotation $Q\in SU(2)$, since $Q(ic\,e_0)Q^\dagger = ic\,QQ^\dagger = ic\,e_0$. The four-velocity therefore determines the rotor only up to left multiplication by a rotation — equivalently, it determines the boost and leaves the orientation of the rest frame free. Among this family, (14) picks the unique Hermitian representative with positive scalar part (the other Hermitian member, $-\tilde{\Lambda}$, generates the same transformation). This is why the Thomas–Wigner rotation of Problem 3 is invisible in a single four-velocity but reappears in the composition of two of them: the four-velocity carries a boost, not a rotation.

## Further Problems

The following are left to the reader; they extend the same tools and use the same notation.

1. **Boosting a four-momentum.** Starting from $\tilde{P} = m\tilde{U}$ and Problem 1, show that $\tilde{\Lambda}_{\mathbf{u}}\tilde{P}\tilde{\Lambda}_{\mathbf{u}}^\dagger = iE'/c\,e_0 + \mathbf{p}'$ with $E' = \gamma_u(E-\mathbf{u}\cdot\mathbf{p})$ and $\mathbf{p}' = \mathbf{p} + (\gamma_u-1)\frac{\mathbf{u}\cdot\mathbf{p}}{u^2}\mathbf{u} - \gamma_u\frac{E}{c^2}\mathbf{u}$. Verify the mass shell $\tilde{P}'\bar{\tilde{P}}' = -m^2c^2$ and recover the aberration of light by setting $m=0$.

2. **Antiparallel boosts.** For $\hat{\mathbf{n}}_2 = -\hat{\mathbf{n}}_1$, show that $\tilde{\Lambda}_2\tilde{\Lambda}_1$ is a pure boost of rapidity $|\psi_1-\psi_2|$ (with the sign determined by which rapidity is larger) and that the Wigner angle (10) vanishes. Deduce the subtraction formula $w = |u_1-u_2|/(1-u_1u_2/c^2)$ and compare with Problem 1(d).

3. **The two orderings.** Show that $\tilde{\Lambda}_1\tilde{\Lambda}_2$ and $\tilde{\Lambda}_2\tilde{\Lambda}_1$ are related by conjugation with a unit quaternion, and determine the relative rotation. For equal projected rapidities show that the relative rotation is by $2\theta_W$ about $\widehat{\mathbf{n}_1\times\mathbf{n}_2}$.

4. **The non-relativistic limit.** Expand (8) and (10) for $u_i/c\ll 1$. Show that the composed velocity tends to $\mathbf{u}_1+\mathbf{u}_2$ and that $\theta_W = O(u_1u_2/c^2)$, giving the leading correction to Galilean velocity addition. Identify which term in (5) is responsible for the Wigner rotation in this limit.

5. **Boost in a medium.** Redo Problems 1–3 with the local speed of light $c = 1/\sqrt{\epsilon\mu}$ in place of $c_0$, treating $c$ as a fixed local constant. Which of the results (1)–(12) change, and which are invariant? Discuss the sense in which the rotor becomes a field when $\epsilon$ and $\mu$ vary from point to point.

6. **A single four-velocity cannot see a rotation.** For a general unit-norm $P = \tilde{H}\tilde{R}$ show that the four-velocity of the frame reached from rest is $ic\,P^{-1}(P^{-1})^\dagger = ic\,\tilde{R}^{-1}\bar{\tilde{H}}^2\tilde{R}$, and that $\tilde{H}$ alone (a boost) gives a different four-velocity unless $\tilde{R}$ commutes with $\bar{\tilde{H}}^2$. Reconcile this with Problem 4(d).

## Summary

We have applied the boost biquaternion and the rotor conjugation to four-velocities and to the composition of boosts.

1. **Boosting a four-velocity.** For $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$ and $\tilde{\Lambda}_{\mathbf{u}} = \cosh\frac{\psi_u}{2}+i\sinh\frac{\psi_u}{2}\hat{\mathbf{u}}$, the rotor conjugation gives (1): a four-velocity in $\mathbb{M}_-$ with $N = -c^2$, scalar part $ic\gamma_u\gamma(1-\mathbf{u}\cdot\mathbf{v}/c^2)$, and vector part $\gamma[\mathbf{v}+(\gamma_u-1)\frac{\mathbf{u}\cdot\mathbf{v}}{u^2}\mathbf{u}-\gamma_u\mathbf{u}]$. The induced velocity is the standard parallel–perpendicular transformation (2); in the collinear case it is the rapidity subtraction $v' = (v-u)/(1-uv/c^2)$.

2. **Collinear composition.** Two boosts along one direction multiply to a pure boost of summed rapidity, (3), giving rapidity addition and the velocity-addition formula $w = (u_1+u_2)/(1+u_1u_2/c^2)$.

3. **Non-collinear composition.** The product $P = \tilde{\Lambda}_2\tilde{\Lambda}_1$ is Hermitian only for parallel or antiparallel directions; otherwise it is a boost times a rotation, with total rapidity (8) and Thomas–Wigner angle (9)–(10), $\tan\frac{\theta_W}{2} = \frac{\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\sin\phi}{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2}+\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\phi}$, about the axis $\widehat{\mathbf{n}_1\times\mathbf{n}_2}$ (11). For equal orthogonal rapidities $\tan\frac{\theta_W}{2} = \tanh^2\frac{\psi}{2}$ exactly. The numerical instance $\psi_1=\psi_2=\operatorname{atanh}0.6$, orthogonal, has composed speed $0.7683749c$ and Wigner angle $12.68038^{\circ}$.

4. **The parent's square-root relation.** $\tilde{\Lambda} = \sqrt{-\tfrac{i}{c}\bar{\tilde{U}}} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{v}}$ is correct, with the branch $\mathrm{Sc}>0$; it is the **lab-to-rest** rotor, since $\tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger = ic\,e_0$ and $\tilde{\Lambda}(ic\,e_0)\tilde{\Lambda}^\dagger$ has velocity $-\mathbf{v}$. The rest-to-lab rotor is the conjugate $\bar{\tilde{\Lambda}}$. The four-velocity determines the rotor only up to a rotation of the rest frame; (14) selects the Hermitian representative.

The exercise has also tested the parent. The parent's formula (14) is correct on every case computed here, including non-collinear directions; but the parent does not state the direction of the transformation it generates, and the conjugate $\bar{\tilde{U}}$ inside the formula is what fixes that direction to lab-to-rest. (A companion exercise in this series, *The Relativistic Kinematics of a Two-Body Decay*, discusses the same direction convention in a different application.) Here the parent's own displayed application is consistent, and the gap is only in the statement; every equation of the parent used here was verified on cases chosen independently of the ones that motivated it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace (rotation rotors) |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $c$, $c_0$ | Speed of light in the medium, and in vacuum |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\bar{\tilde{Q}}$, $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{*}$ | Quaternion conjugate, Hermitian conjugate |
| $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$ | Four-velocity, $N(\tilde{U})=-c^2$ |
| $\tilde{P} = m\tilde{U} = iE/c\,e_0+\mathbf{p}$ | Four-momentum |
| $\gamma = (1-\mathbf{v}^2/c^2)^{-1/2}$, $\gamma_u$ | Lorentz factors |
| $\tilde{\Lambda}_{\mathbf{u}} = \cosh\frac{\psi_u}{2}+i\sinh\frac{\psi_u}{2}\hat{\mathbf{u}}$ | Boost biquaternion, $\tanh\psi_u = u/c$ |
| $\psi_v$, $\psi_1$, $\psi_2$ | Rapidities |
| $\mathbf{u}$, $\hat{\mathbf{n}}_i$ | Boost velocity, boost directions |
| $\phi$ | Angle between $\hat{\mathbf{n}}_1$ and $\hat{\mathbf{n}}_2$ |
| $P = \tilde{\Lambda}_2\tilde{\Lambda}_1$ | Product of two boost rotors |
| $a$, $\mathbf{q}$, $\mathbf{w}$ | Real scalar, real vector, real vector in $P = a+\mathbf{q}+i\mathbf{w}$ |
| $\tilde{H}$, $\tilde{R}$ | Boost part and rotation part of $P = \tilde{H}\tilde{R}$ |
| $\Psi$ | Total rapidity, $\cosh\Psi = \cosh\psi_1\cosh\psi_2+\sinh\psi_1\sinh\psi_2\cos\phi$ |
| $\theta_W$ | Thomas–Wigner angle |
| $\hat{\mathbf{m}}$ | Axis of the boost part $\tilde{H}$ |
| $\hat{\mathbf{k}} = \widehat{\mathbf{n}_1\times\mathbf{n}_2}$ | Axis of the Wigner rotation |
| $\mathrm{Sc}$, $\mathrm{Tr}$ | Scalar part, trace; $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ |

## Further Reading

- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the original velocity-addition theorem.
- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard transformation of four-velocities and the velocity-addition formula.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the parallel–perpendicular decomposition and the four-potential transformation.
- E. P. Wigner, "On Unitary Representations of the Inhomogeneous Lorentz Group," *Annals of Mathematics* **40** (1939) 149–204, and the Thomas precession literature, for the rotation that accompanies the composition of non-collinear boosts.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of boosts and the composition of Lorentz transformations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the double cover $SL(2,\mathbb{C})\to SO^+(1,3)$ and the branch of the square root.
- The companion articles of this series: *Relativistic Mechanics in Biquaternionic Form*, *The Lorentz Transformation as a Biquaternionic Rotation*, and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*.
