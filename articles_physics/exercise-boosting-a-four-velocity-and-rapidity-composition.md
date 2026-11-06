# __Exercise: Boosting a Four-Velocity and Rapidity Composition__

## Introduction

This is one of the exercises in the relativity series. It applies the apparatus of two companion articles: *The Lorentz Transformation as a Biquaternionic Rotation*, which defines the boost biquaternion, the rotor conjugation, and the square-root relation between the rotor and the four-velocity; and *Relativistic Mechanics in Biquaternionic Form*, which fixes the four-velocity and the four-momentum in $\mathbb{M}_-$. Those two articles are the parents of this exercise: every result below is obtained from the tools already defined there, and no new formalism is introduced. The sequence is: boost a general four-velocity (Problem 1); compose two collinear boosts and recover rapidity addition and velocity addition (Problem 2); compose two non-collinear boosts and extract the Thomas–Wigner rotation (Problem 3); and examine the parent's square-root relation between the four-velocity and the boost rotor, whose direction the parent does not state (Problem 4). A set of further problems is left to the reader.

**What is assumed.** The algebra, the sectors, the conjugations, the biquaternion norm and the rotor conjugation are those of *Algebra and Element Conventions*, *Norm and Pairing Conventions* and *Operator and Calculus Conventions*, and none is restated here. The pure boost is written $\tilde U_{\mathrm b}$ and the rotation factor $\tilde u_{\mathrm r}$, with $\tilde U^{\mathrm{lor}}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. No object of the informational sector arises below, so the trace formula of *Norm and Pairing Conventions* is recorded but not used. The four-velocity $\tilde{V} = \gamma(ic\,e_t + \vec v)$ with $\langle\tilde{V}\rangle_{\natural} = -c^2$ and $\gamma = (1-\vec v^2/c^2)^{-1/2}$, the four-momentum $\tilde{P} = m\tilde{V} = iE/c\,e_t + \vec p$, and the boost biquaternion
$$
\tilde U_{\vec v_b} = \cosh\frac{\theta^{\mathrm{rpd}}_b}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}_b}{2}\vec u_x,
\qquad
\tanh\theta^{\mathrm{rpd}}_b = \frac{v_b}{c},
$$
which is Hermitian ($\tilde U_{\vec v_b}^{*} = \tilde U_{\vec v_b}$), lies in $\mathbb{M}_+$, and has unit norm. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value; $\vec v$ is a particle velocity, and $\vec u_x, \vec u_y$ are unit frame or boost directions. The components of a biquaternion are taken in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**What is to be shown.** Problem 1 computes $\tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}^{*}$ for arbitrary $\vec v_b,\vec v$ and shows that it is again a four-velocity of $\mathbb{M}_-$ with the standard components. Problem 2 composes two collinear boost rotors and derives rapidity addition and the velocity-addition formula. Problem 3 composes two non-collinear boosts, shows that the product is no longer a pure boost, and extracts the boost part, the total rapidity, and the Thomas–Wigner angle. Problem 4 verifies the parent's relation $\tilde U_{\mathrm b} = \sqrt{-\tfrac{i}{c}\tilde{V}^{\natural}}$, determines the direction of the transformation it generates, and identifies what the four-velocity does and does not determine. The problems are solved in full; the reader is asked in the final section to extend them.

## Problem 1: The Boost of a General Four-Velocity

**Statement.** Let $\tilde{V} = \gamma(ic\,e_t + \vec v)$ be the four-velocity of a particle, and let $\tilde U_{\vec v_b} = \cosh\frac{\theta^{\mathrm{rpd}}_b}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}_b}{2}\vec u_x$, with $\tanh\theta^{\mathrm{rpd}}_b = v_b/c$, be a boost biquaternion. Compute $\tilde{V}_2 = \tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}^{*}$ and show that:

**(a)** $\tilde{V}_2$ lies in $\mathbb{M}_-$ and has $\langle\tilde{V}_2\rangle_{\natural} = -c^2$;

**(b)** its scalar part is $ic\,\gamma_2$ with $\gamma_2 = \gamma_b\gamma\left(1 - \vec v_b\cdot\vec v/c^2\right)$, where $\gamma_b = (1-v_b^2/c^2)^{-1/2}$;

**(c)** its vector part is $\gamma\left[\vec v + (\gamma_b-1)\dfrac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b - \gamma_b\vec v_b\right]$, so that the induced velocity is the standard parallel–perpendicular transformation;

**(d)** in the collinear case $\vec v\parallel\vec v_b$ the induced velocity is $v_2 = (v-v_b)/(1-v_b v/c^2)$, i.e. the rapidities subtract.

**Solution.** Because a pure-boost rotor is Hermitian, $\tilde U_{\vec v_b}^{*} = \tilde U_{\vec v_b}$, and the transformation is the two-sided product $\tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}$. Write $a = \cosh\frac{\theta^{\mathrm{rpd}}_b}{2}$, $b = \sinh\frac{\theta^{\mathrm{rpd}}_b}{2}$, and $\vec{Ζ} = \vec u_x$, a real unit pure quaternion with $\vec{Ζ}^2 = -e_t$. Split the velocity into parts parallel and perpendicular to $\vec{Ζ}$,
$$
\vec v = \vec v_\parallel + \vec v_\perp, \qquad \vec v_\parallel = v_\parallel \vec{Ζ}, \qquad \vec{Ζ}\,\vec v_\parallel = -v_\parallel, \qquad \vec{Ζ}\,\vec v_\perp = \vec{Ζ}\times\vec v_\perp, \qquad \vec v_\perp \vec{Ζ} = -\vec{Ζ}\times\vec v_\perp .
$$
The first product expands as
$$
\tilde U_{\mathrm b}\tilde{V} = ic\gamma\,\tilde U_{\mathrm b} + \gamma\,\tilde U_{\mathrm b}\vec v
= ic\gamma a - c\gamma b\,\vec{Ζ} + \gamma\left(a\vec v_\parallel + a\vec v_\perp - i b v_\parallel + i b\,\vec{Ζ}\times\vec v_\perp\right).
$$
Multiplying once more on the right by $\tilde U_{\mathrm b} = a + ib\vec{Ζ}$ and collecting the scalar and vector parts gives
$$
\boxed{\;\tilde U_{\vec v_b}\tilde{V}\tilde U_{\vec v_b}^{*}
= ic\,\gamma_b\gamma\left(1 - \frac{\vec v_b\cdot\vec v}{c^2}\right)e_t
+ \gamma\left[\vec v + (\gamma_b-1)\frac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b - \gamma_b\vec v_b\right]\;}
\tag{1}
$$
The identity $\sinh\theta^{\mathrm{rpd}}_b = \gamma_b v_b/c$ and the expansion of the parallel component have been used. The result is the biquaternion form of the standard Lorentz transformation of a four-velocity from the lab to the frame moving with velocity $\vec v_b$.

**(a)** In (1) the scalar coefficient is purely imaginary and the vector coefficient is real, so $\tilde{V}_2\in\mathbb{M}_-$. Its biquaternion norm is preserved because $\langle\cdot\rangle_{\natural}$ is multiplicative and $\langle\tilde U_{\vec v_b}\rangle_{\natural} = 1$:
$$
\langle\tilde{V}_2\rangle_{\natural} = \langle\tilde U_{\vec v_b}\rangle_{\natural}\,\langle\tilde{V}\rangle_{\natural}\,\langle\tilde U_{\vec v_b}\rangle_{\natural}^{*} = 1\cdot(-c^2)\cdot 1 = -c^2 .
$$
The transformation therefore maps four-velocities to four-velocities; this is the algebraic content of Lorentz covariance in $\mathbb{M}_-$.

**(b)** Reading off the scalar coefficient of (1), $\gamma_2 = \gamma_b\gamma(1-\vec v_b\cdot\vec v/c^2)$. This is positive for $v_b,v<c$, since $\vec v_b\cdot\vec v\le v_b v < c^2$. It is the standard transformation of energy, $E_2/c = \gamma_b(E/c - \vec v_b\cdot\vec p/c)$, written for the four-velocity.

**(c)** The induced velocity is the vector coefficient divided by $\gamma_2$,
$$
\vec v_2 = \frac{\vec v + (\gamma_b-1)\dfrac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b - \gamma_b\vec v_b}{\gamma_b\left(1 - \vec v_b\cdot\vec v/c^2\right)}
= \frac{\vec v_\parallel - \vec v_b}{1 - \vec v_b\cdot\vec v/c^2} + \frac{\vec v_\perp}{\gamma_b\left(1 - \vec v_b\cdot\vec v/c^2\right)},
\tag{2}
$$
which is the standard transformation. The second equality uses $\vec v_\parallel = \frac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b$ and the rearrangement $\vec v + (\gamma_b-1)\vec v_\parallel - \gamma_b\vec v_b = \vec v_\perp + \gamma_b(\vec v_\parallel-\vec v_b)$.

**(d)** If $\vec v = v\vec u_x$ then $\vec v_\perp = 0$ and (2) reduces to
$$
v_2 = \frac{v-v_b}{1-v_b v/c^2},
$$
so that in rapidities $v_2 = c\tanh(\theta^{\mathrm{rpd}}_v - \theta^{\mathrm{rpd}}_b)$: **a boost subtracts its rapidity from the rapidity of the four-velocity it acts on.** This is the statement that the transformation (1) is the lab-to-moving-frame map, and it fixes the direction convention used throughout: the rotor $\tilde U_{\vec v_b}$ carries the lab to the frame moving with $+\vec v_b$, so the particle's speed is reduced by $v_b$.

**Numerical instance.** Take $\vec v = 0.6c\,\vec e_x$ and $\vec v_b = 0.5c\,\vec e_y$, orthogonal. Then $\gamma = 1.25$, $\gamma_b = 1.1547005$, $\vec v_b\cdot\vec v = 0$, and from (1)
$$
\gamma_2 = \gamma_b\gamma = 1.4433757, \qquad
\vec v_2 = \begin{pmatrix} 0.5196152 \\ -0.5 \\ 0\end{pmatrix}c, \qquad |\vec v_2| = 0.7211103\,c .
$$
The norm is preserved: $\langle\tilde{V}_2\rangle_{\natural} = -1$ in units $c=1$. The transverse component is contracted by $1/\gamma_b$ (from $0.6c$ to $0.5196c$) and the boost direction acquires the recoil $-v_b$; this is (2) term by term.

## Problem 2: Collinear Boosts and Rapidity Addition

**Statement.** Let $\tilde U_{\mathrm b,1} = \cosh\frac{\theta^{\mathrm{rpd}}_1}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}_1}{2}\vec u_y$ and $\tilde U_{\mathrm b,2} = \cosh\frac{\theta^{\mathrm{rpd}}_2}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}_2}{2}\vec u_y$ be two boost rotors along the same direction $\vec u_y$.

**(a)** Show that $\tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}$ is itself a pure boost along $\vec u_y$, of rapidity $\theta^{\mathrm{rpd}}_1+\theta^{\mathrm{rpd}}_2$.

**(b)** Deduce the velocity-addition formula $w = \dfrac{v_{b_1}+v_{b_2}}{1+v_{b_1}v_{b_2}/c^2}$.

**(c)** Reconcile the addition here with the subtraction found in Problem 1.

**Solution. (a)** Put $\vec{Ζ} = \vec u_y$, $c_i = \cosh\frac{\theta^{\mathrm{rpd}}_i}{2}$, $s_i = \sinh\frac{\theta^{\mathrm{rpd}}_i}{2}$. Since $\vec{Ζ}^2 = -e_t$, the product of the two scalar-imaginary vector parts is
$$
(i\vec{Ζ})(i\vec{Ζ}) = i^2\vec{Ζ}^2 = (-1)(-1) = +e_t,
$$
so the two boosts in the same direction multiply hyperbolically:
$$
\tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}
= \left(c_1c_2 + s_1s_2\right) + i\left(c_1s_2 + s_1c_2\right)\vec{Ζ}
= \cosh\frac{\theta^{\mathrm{rpd}}_1+\theta^{\mathrm{rpd}}_2}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}_1+\theta^{\mathrm{rpd}}_2}{2}\vec u_y
= \tilde U_{\mathrm b}(\theta^{\mathrm{rpd}}_1+\theta^{\mathrm{rpd}}_2).
\tag{3}
$$
The cross terms combine by the addition formulas for $\cosh$ and $\sinh$. The product is Hermitian, lies in $\mathbb{M}_+$, and has unit norm, so it is a pure boost along $\vec u_y$: **boosts in a common direction form a one-parameter subgroup**, and their rapidities add.

**(b)** The product rotor has rapidity $\theta^{\mathrm{rpd}}_1+\theta^{\mathrm{rpd}}_2$, and the velocity it represents is $w = c\tanh(\theta^{\mathrm{rpd}}_1+\theta^{\mathrm{rpd}}_2)$. Using $\tanh\theta^{\mathrm{rpd}}_i = v_{b_i}/c$,
$$
\boxed{\;w = c\,\frac{\tanh\theta^{\mathrm{rpd}}_1 + \tanh\theta^{\mathrm{rpd}}_2}{1 + \tanh\theta^{\mathrm{rpd}}_1\tanh\theta^{\mathrm{rpd}}_2}
= \frac{v_{b_1}+v_{b_2}}{1 + v_{b_1}v_{b_2}/c^2}\;}
\tag{4}
$$
For $v_{b_1} = 0.5c$, $v_{b_2} = 0.6c$ this gives $w = 1.1c/1.3 = 0.8461538c$, which is $\tanh(\operatorname{atanh}0.5 + \operatorname{atanh}0.6)$ to machine precision.

**(c)** There is no contradiction with Problem 1. Equation (3) is the composition of two *coordinate changes*: the rotor $\tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}$ carries the lab to the frame moving with $w$. Equation (2) of Problem 1 is the action of a *single* coordinate change on a four-velocity: it subtracts the frame rapidity. The two statements are the multiplication and the action of the same group, and in the collinear case the action's rapidity shift is the group's rapidity sum with a sign, $v_2 = c\tanh(\theta^{\mathrm{rpd}}_v-\theta^{\mathrm{rpd}}_b)$.

## Problem 3: Non-Collinear Boosts and the Thomas–Wigner Rotation

**Statement.** Let $\tilde U_{\mathrm b,1}$ have rapidity $\theta^{\mathrm{rpd}}_1$ along $\vec u_y$ and $\tilde U_{\mathrm b,2}$ rapidity $\theta^{\mathrm{rpd}}_2$ along $\vec u_z$, with $\vec u_y\cdot\vec u_z = \cos\theta^{\mathrm{btw}}$ and $0<\theta^{\mathrm{btw}}<\pi$.

**(a)** Compute the product $P = \tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}$ and show that it is Hermitian if and only if $\theta^{\mathrm{btw}}\in\{0,\pi\}$; for $0<\theta^{\mathrm{btw}}<\pi$ it is not a pure boost.

**(b)** Show that $P$ admits the decomposition $P = \tilde R_\psi\tilde u_{\mathrm r}$ with $\tilde R_\psi$ a pure boost of unit norm and $\tilde u_{\mathrm r}$ a spatial rotation. Derive the total rapidity $\theta^{\mathrm{rpd}}$, the Wigner angle $\theta_W$, and the rotation axis.

**(c)** Verify the special case of equal orthogonal rapidities, and compute a numerical instance.

**Solution. (a)** With $c_i = \cosh\frac{\theta^{\mathrm{rpd}}_i}{2}$, $s_i = \sinh\frac{\theta^{\mathrm{rpd}}_i}{2}$, $\vec{Ζ}_i = \vec {u_y}_i$, and the quaternion product identity $\vec{Ζ}_2\vec{Ζ}_1 = -\vec{Ζ}_2\cdot \vec{Ζ}_1 + \vec{Ζ}_2\times \vec{Ζ}_1$ for unit pure quaternions,
$$
(i\vec{Ζ}_2)(i\vec{Ζ}_1) = -\vec{Ζ}_2\vec{Ζ}_1 = \cos\theta^{\mathrm{btw}} + \vec{Ζ}_1\times \vec{Ζ}_2 .
$$
Hence
$$
P = \tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}
= \underbrace{\left(c_1c_2 + s_1s_2\cos\theta^{\mathrm{btw}}\right)}_{a}
+ \underbrace{s_1s_2\,\vec u_y\times\vec u_z}_{\vec q}
+ i\underbrace{\left(c_2s_1\vec u_y + c_1s_2\vec u_z\right)}_{\vec w},
\tag{5}
$$
where $a$ is a real scalar, $\vec q$ is a real vector of magnitude $s_1s_2\sin\theta^{\mathrm{btw}}$, and $i\vec w$ is an imaginary vector. The real vector part $\vec q$ is orthogonal to $\vec w$, because $\vec v_{b_2}\times\vec v_{b_3}$ is orthogonal to both $\vec u_y$ and $\vec u_z$. The element $P$ is Hermitian exactly when its real vector part vanishes, i.e. when $s_1s_2\sin\theta^{\mathrm{btw}} = 0$. For nonzero rapidities this means $\sin\theta^{\mathrm{btw}} = 0$, so a product of two boosts is a pure boost only when the two directions are parallel or antiparallel. Otherwise it is a boost together with a rotation: the product has left $\mathbb{M}_+$.

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
The element $PP^\dagger$ is Hermitian and positive (it is $\tilde{R}_\psi^2$ for the required boost), so it has a unique positive Hermitian square root
$$
\tilde R_\psi = \sqrt{PP^\dagger} = \cosh\frac{\theta^{\mathrm{rpd}}}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}}{2}\vec u_4,
\qquad
\cosh\theta^{\mathrm{rpd}} = \Sigma, \quad \sinh\theta^{\mathrm{rpd}}\,\vec u_4 = \vec T.
$$
Expanding $\Sigma = a^2 + |\vec q|^2 + |\vec w|^2$ with the definitions (5) and simplifying gives the standard total rapidity
$$
\cosh\theta^{\mathrm{rpd}} = \cosh\theta^{\mathrm{rpd}}_1\cosh\theta^{\mathrm{rpd}}_2 + \sinh\theta^{\mathrm{rpd}}_1\sinh\theta^{\mathrm{rpd}}_2\cos\theta^{\mathrm{btw}} .
\tag{8}
$$
The residual element
$$
\tilde u_{\mathrm r} = \tilde R_\psi^{-1}P = \tilde R_\psi^{\natural}P
= \left(\cosh\frac{\theta^{\mathrm{rpd}}}{2} - i\sinh\frac{\theta^{\mathrm{rpd}}}{2}\vec u_4\right)\left(a + \vec q + i\vec w\right)
$$
is the $*$-unitary factor of the polar decomposition of $P$ (equivalently $\langle\tilde u_{\mathrm r}\rangle_{\natural} = \langle\tilde R_\psi\rangle_{\natural}^{-1}\langle P\rangle_{\natural} = 1$ and $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{\natural} = e_t$ with $\tilde u_{\mathrm r}$ a unit real quaternion). Its scalar part is
$$
\mathrm{Sc}(\tilde u_{\mathrm r}) = a\cosh\frac{\theta^{\mathrm{rpd}}}{2} - \sinh\frac{\theta^{\mathrm{rpd}}}{2}\left(\vec u_4\cdot\vec w\right),
$$
where the minus sign comes from the $-\vec A\cdot\vec B$ term of the quaternion product, and the term involving $\vec q$ vanishes because $\vec u_4\perp\vec q$. Now $\vec u_4\cdot\vec w = \vec T\cdot\vec w/\sinh\theta^{\mathrm{rpd}} = 2a|\vec w|^2/\sinh\theta^{\mathrm{rpd}}$, so
$$
\mathrm{Sc}(\tilde u_{\mathrm r}) = a\cosh\frac{\theta^{\mathrm{rpd}}}{2} - \frac{a|\vec w|^2}{\cosh\frac{\theta^{\mathrm{rpd}}}{2}}
= \frac{a\left(\cosh^2\frac{\theta^{\mathrm{rpd}}}{2} - |\vec w|^2\right)}{\cosh\frac{\theta^{\mathrm{rpd}}}{2}} .
$$
From (6) and $\Sigma$ one has $\cosh^2\frac{\theta^{\mathrm{rpd}}}{2} = \frac{1+\Sigma}{2} = a^2 + |\vec q|^2 = 1 + |\vec w|^2$, so $\cosh^2\frac{\theta^{\mathrm{rpd}}}{2} - |\vec w|^2 = 1$ and
$$
\mathrm{Sc}(\tilde u_{\mathrm r}) = \frac{a}{\cosh\frac{\theta^{\mathrm{rpd}}}{2}}.
$$
Because $\tilde u_{\mathrm r}$ is a unit real quaternion — a spatial rotation rotor — it has the form $\tilde u_{\mathrm r} = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\vec u_{\mathrm r}$ with $\vec u_{\mathrm r}$ its axis. Comparing scalar parts identifies the **Thomas–Wigner angle** $\theta_W$:
$$
\cos\frac{\theta_W}{2} = \frac{a}{\cosh\frac{\theta^{\mathrm{rpd}}}{2}}
= \frac{\cosh\frac{\theta^{\mathrm{rpd}}_1}{2}\cosh\frac{\theta^{\mathrm{rpd}}_2}{2} + \sinh\frac{\theta^{\mathrm{rpd}}_1}{2}\sinh\frac{\theta^{\mathrm{rpd}}_2}{2}\cos\theta^{\mathrm{btw}}}{\cosh\frac{\theta^{\mathrm{rpd}}}{2}},
\tag{9}
$$
and, since $|\vec q|^2 = \sinh^2\frac{\theta^{\mathrm{rpd}}_1}{2}\sinh^2\frac{\theta^{\mathrm{rpd}}_2}{2}\sin^2\theta^{\mathrm{btw}}$ and $\sin\frac{\theta_W}{2} = |\vec q|/\cosh\frac{\theta^{\mathrm{rpd}}}{2}$,
$$
\boxed{\;\tan\frac{\theta_W}{2} = \frac{|\vec q|}{a}
= \frac{\sinh\frac{\theta^{\mathrm{rpd}}_1}{2}\sinh\frac{\theta^{\mathrm{rpd}}_2}{2}\sin\theta^{\mathrm{btw}}}{\cosh\frac{\theta^{\mathrm{rpd}}_1}{2}\cosh\frac{\theta^{\mathrm{rpd}}_2}{2} + \sinh\frac{\theta^{\mathrm{rpd}}_1}{2}\sinh\frac{\theta^{\mathrm{rpd}}_2}{2}\cos\theta^{\mathrm{btw}}}\;}
\tag{10}
$$
The numerator is non-negative for $0<\theta^{\mathrm{btw}}<\pi$ and the denominator $a$ is positive for every $\theta^{\mathrm{btw}}$, since $a\ge\cosh\frac{\theta^{\mathrm{rpd}}_1}{2}\cosh\frac{\theta^{\mathrm{rpd}}_2}{2} - \sinh\frac{\theta^{\mathrm{rpd}}_1}{2}\sinh\frac{\theta^{\mathrm{rpd}}_2}{2} = \cosh\frac{\theta^{\mathrm{rpd}}_1-\theta^{\mathrm{rpd}}_2}{2}>0$. Hence $0\le\theta_W<\pi$. The rotation axis is the normal to the plane of the two boost directions,
$$
\vec u_{\mathrm r} = \vec u_{\vec v_{b_2}\times\vec v_{b_3}},
\tag{11}
$$
which we verified numerically in several non-coplanar configurations; it is the direction of the antisymmetric, real-vector part $\vec q$ of $P$ in (5). With this, the decomposition is
$$
\tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1} = \tilde R_\psi\tilde u_{\mathrm r},
\qquad
\tilde R_\psi = \cosh\frac{\theta^{\mathrm{rpd}}}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}}{2}\vec u_4,
\qquad
\tilde u_{\mathrm r} = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\vec u_{\vec v_{b_2}\times\vec v_{b_3}}.
\tag{12}
$$
The rotation is intrinsic, but the split of $P$ into boost and rotation is only canonical in the right-polar sense (12). The alternative left-polar form $P = \tilde u_{\mathrm r}\tilde{R}_{\psi,2}$ with $\tilde{R}_{\psi,2} = \tilde u_{\mathrm r}^{-1}\tilde R_\psi\tilde u_{\mathrm r}$ is an equally valid boost-times-rotation decomposition, with a boost of the same rapidity $\theta^{\mathrm{rpd}}$ but a different axis; only $\theta^{\mathrm{rpd}}$ and $\theta_W$ are convention-independent. This is the sense in which the parent's statement that a non-collinear product is "a boost plus a spatial rotation" is complete only after the ordering is fixed.

**(c)** For equal orthogonal rapidities, $\theta^{\mathrm{rpd}}_1 = \theta^{\mathrm{rpd}}_2 = \theta^{\mathrm{rpd}}$ and $\theta^{\mathrm{btw}} = \pi/2$, so $\cosh\theta^{\mathrm{rpd}} = \cosh^2\theta^{\mathrm{rpd}}$ and $a = \cosh^2\frac{\theta^{\mathrm{rpd}}}{2}$. Then $\cos\frac{\theta_W}{2} = \cosh^2\frac{\theta^{\mathrm{rpd}}}{2}\big/\cosh\frac{\theta^{\mathrm{rpd}}}{2}$, and (10) collapses to
$$
\tan\frac{\theta_W}{2} = \frac{\sinh^2\frac{\theta^{\mathrm{rpd}}}{2}}{\cosh^2\frac{\theta^{\mathrm{rpd}}}{2}} = \tanh^2\frac{\theta^{\mathrm{rpd}}}{2}.
\tag{13}
$$
This is exact; it was checked numerically for $\theta^{\mathrm{rpd}} = 0.5, 1, 1.5, 2, 3$ to $10^{-12}$.

**Numerical instance.** Take $\theta^{\mathrm{rpd}}_1 = \theta^{\mathrm{rpd}}_2 = \operatorname{atanh}0.6 = 0.6931472$ along $\vec u_y = \vec u_{e,1}$ and $\vec u_z = \vec u_{e,2}$, so that each boost has speed $0.6c$. Then (5) gives, in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,
$$
P = \tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1} = 1.125 + 0.375\,i\,\vec e_x + 0.375\,i\,\vec e_y + 0.125\,\vec e_z,
$$
which is not Hermitian: the real $\vec e_z$ term $s_1s_2 = 0.125$ is the antisymmetric part. From (8), $\theta^{\mathrm{rpd}} = 1.0163481$ and the composed frame has speed $c\tanh\theta^{\mathrm{rpd}} = 0.7683749c$; the velocity-addition formula (2) applied twice gives the same speed. The Wigner angle (9)–(10) is $\theta_W = 12.68038^{\circ} = 0.2213144$ rad, with
$$
\tilde u_{\mathrm r} = \cos\frac{\theta_W}{2} + \sin\frac{\theta_W}{2}\vec u_{e,3} = 0.9938837 + 0.1104315\,\vec u_{e,3} .
$$
The frame reached by $P$ has, in the lab, the four-velocity $ic\,P^{-1}(P^{-1})^{*} = 1.5625i\,e_t + 0.9375\,\vec e_x + 0.75\,\vec e_y$, i.e. velocity $(0.6, 0.48, 0)c$: magnitude $0.7683749c$ and direction $38.66^{\circ}$ from $\vec u_{e,1}$. The boost part $\tilde R_\psi$ has axis $\vec u_4 = (0.6246950, 0.7808688, 0)$ at $51.34^{\circ}$, which is the velocity direction rotated by the Wigner angle, $\vec u_4 = \tilde u_{\mathrm r}\vec u_5\tilde u_{\mathrm r}^{-1}$. The two orderings do not agree: $\tilde U_{\mathrm b,1}\tilde U_{\mathrm b,2}$ is a different rotor, with the opposite sense of Wigner rotation, so the two boost directions do not merely "add".

## Problem 4: The Parent's Square-Root Relation and the Direction of the Boost

**Statement.** The companion article *The Lorentz Transformation as a Biquaternionic Rotation* states that the boost biquaternion associated with a four-velocity $\tilde{V} = \gamma(ic\,e_t+\vec v)$ is
$$
\tilde U_{\mathrm b} = \sqrt{-\frac{i}{c}\tilde{V}^{\natural}},
\tag{14}
$$
with the square root branch selected by $\mathrm{Sc}(\tilde U_{\mathrm b})>0$.

**(a)** Verify (14) and the branch, and identify the rotor explicitly.

**(b)** Show that $\tilde U_{\mathrm b}\tilde{V}\tilde U_{\mathrm b}^{*} = ic\,e_t$: the rotor (14) carries the lab to the particle's rest frame.

**(c)** Show that the rotor that carries the rest four-velocity $ic\,e_t$ to $\tilde{V}$ is $\tilde U_{\mathrm b}^{\natural}$, not $\tilde U_{\mathrm b}$, and give the sign error that follows from using $\tilde U_{\mathrm b}$ in that direction.

**(d)** State precisely what the four-velocity and the relation (14) determine.

**Solution. (a)** With $\tilde{V}^{\natural} = \gamma(ic\,e_t - \vec v)$,
$$
-\frac{i}{c}\tilde{V}^{\natural} = -\frac{i}{c}\gamma\left(ic\,e_t - \vec v\right)
= \gamma\,e_t + i\gamma\frac{\vec v}{c}.
$$
Writing $\gamma = \cosh\theta^{\mathrm{rpd}}$, $\gamma v/c = \sinh\theta^{\mathrm{rpd}}$, this is
$$
-\frac{i}{c}\tilde{V}^{\natural} = \cosh\theta^{\mathrm{rpd}} + i\sinh\theta^{\mathrm{rpd}}\,\vec u_6
= \exp\!\left(\theta^{\mathrm{rpd}}\,i\vec u_6\right),
$$
where the exponential is hyperbolic because $(i\vec u_6)^2 = i^2\vec u_6^2 = (-1)(-1) = +e_t$. Its positive Hermitian square root is
$$
\tilde U_{\mathrm b} = \cosh\frac{\theta^{\mathrm{rpd}}}{2} + i\sinh\frac{\theta^{\mathrm{rpd}}}{2}\vec u_6,
$$
which is precisely the boost biquaternion of *The Lorentz Transformation as a Biquaternionic Rotation* with $\vec u_x = \vec u_6$ and rapidity $\theta^{\mathrm{rpd}} = \operatorname{atanh}(v/c)$. It is Hermitian and of unit norm. The element $-\tfrac{i}{c}\tilde{V}^{\natural}$ has eigenvalues $\exp(\pm\theta^{\mathrm{rpd}})>0$ in the matrix representation, so its two square roots are $\pm\tilde U_{\mathrm b}$; the choice $\mathrm{Sc}>0$ selects $+\tilde U_{\mathrm b}$. Note that the quaternion conjugate $\tilde U_{\mathrm b}^{\natural}$, the boost of rapidity $-\theta^{\mathrm{rpd}}$, is **not** a square root of $-\tfrac{i}{c}\tilde{V}^{\natural}$: it squares to $\cosh\theta^{\mathrm{rpd}} - i\sinh\theta^{\mathrm{rpd}}\vec u_6$. The two square roots differ by the kernel element $-1$ of $SL(2,\mathbb{C})\to SO^+(1,3)$ and generate the same Lorentz transformation; the conjugate is a different transformation.

**(b)** Since $\tilde U_{\mathrm b}$ is Hermitian, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$, and $P\,\tilde{V}\,P^\dagger$ for the pure boost reduces to a computation already made in Problem 1 with $\vec v_b = \vec v$ and $\theta^{\mathrm{rpd}}_b = \theta^{\mathrm{rpd}}_v$; by part (d) there, the rapidities subtract, $\theta^{\mathrm{rpd}}_v-\theta^{\mathrm{rpd}}_v = 0$, giving
$$
\boxed{\;\tilde U_{\mathrm b}\tilde{V}\tilde U_{\mathrm b}^{*} = ic\,e_t\;}
$$
Equivalently, directly: $\tilde U_{\mathrm b}\tilde{V}\tilde U_{\mathrm b}^{*} = ic\gamma\tilde U_{\mathrm b}^2 + \gamma v\,\tilde U_{\mathrm b}\vec u_6\tilde U_{\mathrm b}$, and since $\tilde U_{\mathrm b}$ commutes with $\vec u_6$, $\tilde U_{\mathrm b}\vec u_6\tilde U_{\mathrm b} = \vec u_6\tilde U_{\mathrm b}^2 = \cosh\theta^{\mathrm{rpd}}\,\vec u_6 - i\sinh\theta^{\mathrm{rpd}}$. Hence the vector part is $\gamma v\cosh\theta^{\mathrm{rpd}} - c\gamma\sinh\theta^{\mathrm{rpd}} = c\gamma\sinh\theta^{\mathrm{rpd}} - c\gamma\sinh\theta^{\mathrm{rpd}} = 0$ and the scalar part is $ic\gamma(\cosh\theta^{\mathrm{rpd}} - \tanh\theta^{\mathrm{rpd}}\sinh\theta^{\mathrm{rpd}}) = ic$. So (14) is the rotor of the transformation *lab $\to$ rest*.

**(c)** Conjugating the rest four-velocity by $\tilde U_{\mathrm b}$ instead gives
$$
\tilde U_{\mathrm b}(ic\,e_t)\tilde U_{\mathrm b}^{*} = ic\,\tilde U_{\mathrm b}^2
= ic\left(\cosh\theta^{\mathrm{rpd}} + i\sinh\theta^{\mathrm{rpd}}\,\vec u_6\right)
= ic\cosh\theta^{\mathrm{rpd}}\,e_t - c\sinh\theta^{\mathrm{rpd}}\,\vec u_6,
$$
whose induced velocity is $-c\tanh\theta^{\mathrm{rpd}}\,\vec u_6 = -\vec v$. Thus the rotor built from $\tilde{V}$ carries the lab to the rest frame and, applied in the opposite direction, produces the *negative* of the particle's velocity. The rotor that carries the rest frame to $\tilde{V}$ is the inverse, i.e. the quaternion conjugate:
$$
\tilde U_{\mathrm b}^{\natural}\,(ic\,e_t)\,\overline{\tilde U_{\mathrm b}} = ic\,(\tilde U_{\mathrm b}^{\natural})^2 = ic\cosh\theta^{\mathrm{rpd}}\,e_t + c\sinh\theta^{\mathrm{rpd}}\,\vec u_6,
\qquad \text{velocity} = +\vec v.
$$
The sign is therefore fixed entirely by whether one uses $\tilde{V}^{\natural}$ (as the parent does) or $\tilde{V}$ in (14): the conjugate in the formula is what makes (14) the lab-to-rest rotor. The parent writes the formula but does not state the direction; a reader who reads "the boost biquaternion associated with $\tilde{V}$" as the rotor that *produces* $\tilde{V}$ will use $\tilde U_{\mathrm b}$ where $\tilde U_{\mathrm b}^{\natural}$ is required and obtain $-\vec v$ instead of $+\vec v$. This is a genuine gap in the parent's statement, although the formula itself is correct and its displayed verification (the four-potential transformation with $\vec v_b$ the boost velocity) is in the consistent direction.

**(d)** What relation (14) determines is the **Hermitian** (pure-boost) rotor. Given $\tilde{V}$, equation (14) has exactly the two solutions $\pm\tilde U_{\mathrm b}$, and the branch $\mathrm{Sc}>0$ selects one; both generate the same Lorentz transformation. The quaternion conjugate $\tilde U_{\mathrm b}^{\natural}$ is not a solution (it is the inverse transformation). More generally, if $P$ is any unit-norm rotor with $P\tilde{V}P^\dagger = ic\,e_t$, then $\tilde U_{\mathrm b}P$ is another for every spatial rotation $\tilde u_{\mathrm r}\in SU(2)$, since $\tilde u_{\mathrm r}(ic\,e_t)\tilde u_{\mathrm r}^{*} = ic\,\tilde u_{\mathrm r}\tilde u_{\mathrm r}^\dagger = ic\,e_t$. The four-velocity therefore determines the rotor only up to left multiplication by a rotation — equivalently, it determines the boost and leaves the orientation of the rest frame free. Among this family, (14) picks the unique Hermitian representative with positive scalar part (the other Hermitian member, $-\tilde U_{\mathrm b}$, generates the same transformation). This is why the Thomas–Wigner rotation of Problem 3 is invisible in a single four-velocity but reappears in the composition of two of them: the four-velocity carries a boost, not a rotation.

## Problem 5: A Varying Rapidity, and the Boundary of Problem 2

**Statement.** Let the boost parameter vary along a scalar parameter $\tau$ instead of being fixed, and let the material coordinate of the moving frame's origin be
$$
\tilde R_\varphi(\tau) = ic\,\tau\cosh\xi(\tau)\,e_t + c\,\tau\sinh\xi(\tau)\,\vec u_y,
\qquad \xi = \xi(\tau),
$$
so that $r'_t = \tau\cosh\xi$ and the displacement along $\vec u_y$ is $x_1 = c\tau\sinh\xi$. Define the coordinate velocity by $\beta = (1/c)\,dx_1/dr'_t$.

**(a)** Show that
$$
\beta(\tau) = \frac{\tanh\xi + \tau\frac{d\xi}{d\tau}}{1 + \tau\frac{d\xi}{d\tau}\tanh\xi}.
$$

**(b)** Show that while $|\tau\frac{d\xi}{d\tau}| < 1$ this is a rapidity addition, $\beta = \tanh(\xi+\theta^{\mathrm{rpd}})$ with $\tanh\theta^{\mathrm{rpd}} = \tau\frac{d\xi}{d\tau}$, and that for $|\tau\frac{d\xi}{d\tau}| > 1$ no real $\theta^{\mathrm{rpd}}$ exists, so $|\beta|$ need not stay below $1$.

**(c)** Show the interval identity
$$
c^2d{r'_{t}}^2 - dx_1^2 = c^2d\tau_b^2\left(1 - (\tau\frac{d\xi}{d\tau})^2\right),
$$
and read off when the worldline is timelike.

**(d)** For the linear profile $\xi(\tau) = \alpha\tau$, evaluate $\beta$ and find its maximum.

**Solution. (a)** Differentiate the two coordinate functions with respect to $\tau$:
$$
\frac{dx_1}{d\tau} = c\left(\sinh\xi + \tau\frac{d\xi}{d\tau}\cosh\xi\right),
\qquad
\frac{dr'_t}{d\tau} = \cosh\xi + \tau\frac{d\xi}{d\tau}\sinh\xi .
$$
Both carry the same factor $\tau\frac{d\xi}{d\tau}$ that a fixed rapidity would not have; their ratio is the stated expression. This is not the composition law (4), because the rotor here is a *different* rotor at every $\tau$: the second term is the rate at which the frame turns, not the rapidity of a second frame.

**(b)** Dividing numerator and denominator of (a) by $\cosh\xi$ gives
$$
\beta(\tau) = \frac{\tanh\xi + \tau\frac{d\xi}{d\tau}}{1 + \tau\frac{d\xi}{d\tau}\tanh\xi},
$$
which is the same rational form as the addition law of Problem 2(b), with $\tau\frac{d\xi}{d\tau}$ in the place of $\tanh\theta^{\mathrm{rpd}}_2$. Whenever $|\tau\frac{d\xi}{d\tau}| < 1$ it is exactly $\tanh(\xi + \operatorname{atanh}(\tau\frac{d\xi}{d\tau}))$, so the acceleration acts as an added rapidity and the bound $\beta < 1$ holds. For $|\tau\frac{d\xi}{d\tau}| > 1$ no real rapidity has that tangent, and the bound is no longer forced: $\beta$ can pass through $1$.

**(c)** With $A = \cosh\xi$, $B = \sinh\xi$, $p = \tau\frac{d\xi}{d\tau}$, the two derivatives are $c(B + pA)$ and $A + pB$, so
$$
\left(A+pB\right)^2 - \left(B+pA\right)^2 = \left(A^2-B^2\right)\left(1-p^2\right) = 1 - p^2 ,
$$
using $\cosh^2\xi - \sinh^2\xi = 1$. The worldline is timelike exactly while $|\tau\frac{d\xi}{d\tau}| < 1$ and spacelike beyond, so the value $|\tau\frac{d\xi}{d\tau}| = 1$ is precisely where it crosses the cone. The identity was checked on both sides for several profiles and values of $\tau$, agreeing to round-off.

**(d)** With $\xi = \alpha\tau$, so $\tau\frac{d\xi}{d\tau} = \alpha\tau$,
$$
\boxed{\;\beta = \frac{\tanh\alpha\tau + \alpha\tau}{1 + \alpha\tau\tanh\alpha\tau}\;}
$$
At $\alpha\tau = 1$ this is exactly $1$. For $\alpha\tau > 1$ it exceeds $1$, reaching its maximum $\beta = 1.02049$ at $\alpha\tau = \sqrt{2}$, and then decaying back towards $1$ from above as $\alpha\tau \to \infty$. The recomputed values $\beta(1.4) = 1.0204776$, $\beta(1.5) = 1.0201151$, $\beta(2) = 1.0122854$ reproduce the source's printed table to seven decimals; the table samples at $1.4$, while the exact maximum sits at $\sqrt{2}$.

**What this does and does not show.** It does not contradict Problem 2, and it does not open the light cone of *Causality and the Light Cone as an Information Barrier*. Problem 2 composes *fixed* rapidities, that is, inertial frames, and its bound is about that composition; the rotor here is a different rotor at every $\tau$, which is not a coordinate change to another inertial frame. What (c) identifies is that the worldline itself leaves the timelike region at $|\tau\frac{d\xi}{d\tau}| = 1$, so past that point it is not the worldline of a material corpuscle. The construction and the profile are the source's, recorded and not adopted (I. Guzmán de Rojas, *Trajectories in space-time M4: Reinstating the Newtonian Time*, 2013); the four results above were recomputed from the source's printed formulas for this problem.

## Further Problems

The following are left to the reader; they extend the same tools and use the same notation.

1. **Boosting a four-momentum.** Starting from $\tilde{P} = m\tilde{V}$ and Problem 1, show that $\tilde U_{\vec v_b}\tilde{P}\tilde U_{\vec v_b}^{*} = iE_2/c\,e_t + \vec p_2$ with $E_2 = \gamma_b(E-\vec v_b\cdot\vec p)$ and $\vec p_2 = \vec p + (\gamma_b-1)\frac{\vec v_b\cdot\vec p}{v_b^2}\vec v_b - \gamma_b\frac{E}{c^2}\vec v_b$. Verify the mass shell $\tilde P_2{\tilde P_2^{\natural}} = -m^2c^2$ and recover the aberration of light by setting $m=0$.

2. **Antiparallel boosts.** For $\vec u_z = -\vec u_y$, show that $\tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}$ is a pure boost of rapidity $|\theta^{\mathrm{rpd}}_1-\theta^{\mathrm{rpd}}_2|$ (with the sign determined by which rapidity is larger) and that the Wigner angle (10) vanishes. Deduce the subtraction formula $w = |v_{b_1}-v_{b_2}|/(1-v_{b_1}v_{b_2}/c^2)$ and compare with Problem 1(d).

3. **The two orderings.** Show that $\tilde U_{\mathrm b,1}\tilde U_{\mathrm b,2}$ and $\tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}$ are related by conjugation with a unit quaternion, and determine the relative rotation. For equal projected rapidities show that the relative rotation is by $2\theta_W$ about $\vec u_{\vec v_{b_2}\times\vec v_{b_3}}$.

4. **The non-relativistic limit.** Expand (8) and (10) for $v_{b_i}/c\ll 1$. Show that the composed velocity tends to $\vec v_{b_1}+\vec v_{b_2}$ and that $\theta_W = O(v_{b_1}v_{b_2}/c^2)$, giving the leading correction to Galilean velocity addition. Identify which term in (5) is responsible for the Wigner rotation in this limit.

5. **Boost in a medium.** Redo Problems 1–3 with the local speed of light $c = 1/\sqrt{\epsilon\mu}$ in place of $c_0$, treating $c$ as a fixed local constant. Which of the results (1)–(12) change, and which are invariant? Discuss the sense in which the rotor becomes a field when $\epsilon$ and $\mu$ vary from point to point.

6. **A single four-velocity cannot see a rotation.** For a general unit-norm $P = \tilde R_\psi\tilde u_{\mathrm r}$ show that the four-velocity of the frame reached from rest is $ic\,P^{-1}(P^{-1})^{*} = ic\,\tilde u_{\mathrm r}^{-1}(\tilde R_\psi^{\natural})^2\tilde u_{\mathrm r}$, and that $\tilde R_\psi$ alone (a boost) gives a different four-velocity unless $\tilde u_{\mathrm r}$ commutes with $(\tilde R_\psi^{\natural})^2$. Reconcile this with Problem 4(d).

## Summary

We have applied the boost biquaternion and the rotor conjugation to four-velocities and to the composition of boosts.

1. **Boosting a four-velocity.** For $\tilde{V} = \gamma(ic\,e_t+\vec v)$ and $\tilde U_{\vec v_b} = \cosh\frac{\theta^{\mathrm{rpd}}_b}{2}+i\sinh\frac{\theta^{\mathrm{rpd}}_b}{2}\vec u_x$, the rotor conjugation gives (1): a four-velocity in $\mathbb{M}_-$ with $N = -c^2$, scalar part $ic\gamma_b\gamma(1-\vec v_b\cdot\vec v/c^2)$, and vector part $\gamma[\vec v+(\gamma_b-1)\frac{\vec v_b\cdot\vec v}{v_b^2}\vec v_b-\gamma_b\vec v_b]$. The induced velocity is the standard parallel–perpendicular transformation (2); in the collinear case it is the rapidity subtraction $v_2 = (v-v_b)/(1-v_b v/c^2)$.

2. **Collinear composition.** Two boosts along one direction multiply to a pure boost of summed rapidity, (3), giving rapidity addition and the velocity-addition formula $w = (v_{b_1}+v_{b_2})/(1+v_{b_1}v_{b_2}/c^2)$.

3. **Non-collinear composition.** The product $P = \tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}$ is Hermitian only for parallel or antiparallel directions; otherwise it is a boost times a rotation, with total rapidity (8) and Thomas–Wigner angle (9)–(10), $\tan\frac{\theta_W}{2} = \frac{\sinh\frac{\theta^{\mathrm{rpd}}_1}{2}\sinh\frac{\theta^{\mathrm{rpd}}_2}{2}\sin\theta^{\mathrm{btw}}}{\cosh\frac{\theta^{\mathrm{rpd}}_1}{2}\cosh\frac{\theta^{\mathrm{rpd}}_2}{2}+\sinh\frac{\theta^{\mathrm{rpd}}_1}{2}\sinh\frac{\theta^{\mathrm{rpd}}_2}{2}\cos\theta^{\mathrm{btw}}}$, about the axis $\vec u_{\vec v_{b_2}\times\vec v_{b_3}}$ (11). For equal orthogonal rapidities $\tan\frac{\theta_W}{2} = \tanh^2\frac{\theta^{\mathrm{rpd}}}{2}$ exactly. The numerical instance $\theta^{\mathrm{rpd}}_1=\theta^{\mathrm{rpd}}_2=\operatorname{atanh}0.6$, orthogonal, has composed speed $0.7683749c$ and Wigner angle $12.68038^{\circ}$.

4. **The parent's square-root relation.** $\tilde U_{\mathrm b} = \sqrt{-\tfrac{i}{c}\tilde{V}^{\natural}} = \cosh\frac{\theta^{\mathrm{rpd}}}{2}+i\sinh\frac{\theta^{\mathrm{rpd}}}{2}\vec u_6$ is correct, with the branch $\mathrm{Sc}>0$; it is the **lab-to-rest** rotor, since $\tilde U_{\mathrm b}\tilde{V}\tilde U_{\mathrm b}^{*} = ic\,e_t$ and $\tilde U_{\mathrm b}(ic\,e_t)\tilde U_{\mathrm b}^{*}$ has velocity $-\vec v$. The rest-to-lab rotor is the conjugate $\tilde U_{\mathrm b}^{\natural}$. The four-velocity determines the rotor only up to a rotation of the rest frame; (14) selects the Hermitian representative.

5. **A varying rapidity.** When the boost parameter is a function $\xi(\tau)$ of a scalar trajectory parameter, the coordinate velocity (Problem 5) is $\beta = (\tanh\xi + \tau\frac{d\xi}{d\tau})/(1 + \tau\frac{d\xi}{d\tau}\tanh\xi)$, the same rational form as the addition law with $\tau\frac{d\xi}{d\tau}$ replacing a second rapidity, and the worldline is timelike exactly while $|\tau\frac{d\xi}{d\tau}| < 1$. For $\xi = \alpha\tau$ the velocity reaches $1$ at $\alpha\tau = 1$ and peaks at $\beta = 1.02049$ at $\alpha\tau = \sqrt{2}$. This is not a counterexample to Problem 2: it composes a *varying* rotor, not two fixed rapidities, and past $|\tau\frac{d\xi}{d\tau}| = 1$ the worldline is no longer timelike.

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
| $\tilde U_{\vec v_b} = \cosh\frac{\theta^{\mathrm{rpd}}_b}{2}+i\sinh\frac{\theta^{\mathrm{rpd}}_b}{2}\vec u_x$ | Boost biquaternion, $\tanh\theta^{\mathrm{rpd}}_b = v_b/c$ |
| $\theta^{\mathrm{rpd}}_v$, $\theta^{\mathrm{rpd}}_1$, $\theta^{\mathrm{rpd}}_2$ | Rapidities |
| $\vec v_b$, $\vec {u_y}_i$ | Boost velocity, boost directions |
| $\theta^{\mathrm{btw}}$ | Angle between $\vec u_y$ and $\vec u_z$ |
| $P = \tilde U_{\mathrm b,2}\tilde U_{\mathrm b,1}$ | Product of two boost rotors |
| $a$, $\vec q$, $\vec w$ | Real scalar, real vector, real vector in $P = a+\vec q+i\vec w$ |
| $\tilde R_\psi$, $\tilde u_{\mathrm r}$ | Boost part and rotation part of $P = \tilde R_\psi\tilde u_{\mathrm r}$ |
| $\theta^{\mathrm{rpd}}$ | Total rapidity, $\cosh\theta^{\mathrm{rpd}} = \cosh\theta^{\mathrm{rpd}}_1\cosh\theta^{\mathrm{rpd}}_2+\sinh\theta^{\mathrm{rpd}}_1\sinh\theta^{\mathrm{rpd}}_2\cos\theta^{\mathrm{btw}}$ |
| $\theta_W$ | Thomas–Wigner angle |
| $\vec u_4$ | Axis of the boost part $\tilde R_\psi$ |
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
- The companion articles of this series: [Relativistic Mechanics in Biquaternionic Form](relativistic-mechanics-in-biquaternionic-form.html), [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html), and [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html).
- I. Guzmán de Rojas, *Trajectories in space-time M4: Reinstating the Newtonian Time*, Communication to the National Academy of Sciences of Bolivia (2013), for the time-dependent rapidity of Problem 5: the coordinate velocity of an accelerated parametrisation, the interval identity that fixes where the worldline ceases to be timelike, and the maximum $\beta = 1.02049$ at $\alpha\tau = \sqrt{2}$. Cited as an external construction, not adopted; the source's printed table was recomputed here and reproduces to seven decimals.
