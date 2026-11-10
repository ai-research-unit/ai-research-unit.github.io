# __The Polar Form of the Klein–Gordon Equation in Biquaternionic Form__

## Introduction

The polar form of a field writes it in amplitude and phase. The Klein–Gordon field is biquaternion-valued,

$$
\left(\Box-k_m^{2}\right)\tilde\Xi=0,
\qquad
\tilde\Xi=\Xi_t e_t+\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z,
$$

and the operator $\Box$ is central and scalar, so it multiplies each coefficient and mixes no two of them: the one biquaternion equation is four independent complex equations, $\left(\Box-k_m^{2}\right)\Xi_\mu=0$ with $\mu\in\{t,x,y,z\}$, and each coefficient carries its own amplitude and its own phase.

**The scalar case is treated first, and it is a choice of subject.** In the first part of this article the field is central, $\Xi_x=\Xi_y=\Xi_z=0$, so that $\tilde\Xi=\Xi_t e_t$ and the field is the one complex scalar $\Xi_t$. Nothing in the equation forbids the other three coefficients and nothing couples them to $\Xi_t$; the general field is treated in §*General Fields*, where the algebra's frame is no longer frozen and each coefficient carries its own pair. What the restriction buys is that the equations below are two and not eight, and that one amplitude and one phase describe the whole field. What it costs is that the frame factor, which is the whole of the spin content of the polar word, is absent by construction.

On the scalar the polar form is

$$
\boxed{\;\tilde\Xi=\Xi_t e_t,\qquad \Xi_t=\lvert\Xi_t\rvert\,\exp\!\left(\frac{iS_t}{\hbar}\right)\;}
\qquad \lvert\Xi_t\rvert>0,\quad S_t\in\mathbb{R},
$$

with $\lvert\Xi_t\rvert=\bigl(\langle\tilde\Xi\rangle_{*}\bigr)^{1/2}>0$ the amplitude and $S_t$ the action, carried in $\mathrm{J\,s}$, so that $S_t/\hbar$ is a pure number. The variable is written $\Xi_t$ and not $\tilde\Xi$: without the tilde it is a complex scalar, and the tilde is kept for the algebra element $\tilde\Xi=\Xi_t e_t$ that carries it. The subscript names the direction of the unit, as in the companion, and the action takes the subscript of its coefficient, as in *Relativistic Mechanics from the Dirac Wave*, because the spin $\tilde S_{\Psi,\eta}$ stands on the same letter. That the field is central is what puts $e_t$ alone in the element and leaves $\mathbb{B}_{C}$ as its value space. Substituting the polar form into $\left(\Box-k_m^{2}\right)\Xi_t=0$ and separating real and imaginary parts replaces one complex equation by two exact real equations. That is the whole of the construction.

The representation is not unique. $S_t$ is defined modulo $2\pi\hbar$, and the amplitude is fixed by $\lvert\Xi_t\rvert>0$; once the angle is taken in one half-open interval of length $2\pi$ the form is unique, and nothing is approximated. For the Dirac field the phase factors out only up to a frame, which the equation then constrains; for a scalar the frame is the identity, and the algebra's polar word collapses onto the complex number's polar form.

The companion article *The Klein–Gordon Equation in Biquaternionic Form* treats the complex form of the equation, its current and its two defects. This article treats the same coefficient in the other coordinates. The two equations it reaches are not new: they are the relativistic hydrodynamics of a spin-$0$ quantum fluid as Takabayasi wrote it, and Madelung's pair in the non-relativistic limit. Five results follow, and they are what the change of coordinates and the algebra add to that system.

**The exact pair of real equations.** The amplitude obeys a mass-shell equation whose mass term is shifted by a second-derivative bracket of the amplitude, and the action obeys a transport equation. Both are exact and neither is an expansion.

**One term the companion's box leaves implicit.** The companion derives $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ on a plane wave of constant amplitude. The amplitude equation carries the remainder $\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert$, and a general wave does not drop it.

**One mechanism for the two defects.** The current is the squared amplitude times the four-velocity, so the sign of the charge is the sign of the energy, and the amplitude carries none of it.

**The algebraic word degenerates on this field.** Six of its eight parameters are frozen when the field is central, so the word reduces to the amplitude and the action, which are the two coordinates of this article.

**The general field needs four of these pairs.** With all four coefficients active the frame is free and varying, and the one pair becomes four.

The two senses of *polar form* are kept apart below. The polar form of the field is the amplitude–phase writing; the polar word of the algebra is the four-factor decomposition, and it appears only where the question is what that word does on a central field, so that a statement about the word is never read as a statement about the field. The sections follow the four results: the ansatz and its domain, the two real equations, the momentum and the current, the non-relativistic limit, what the change of coordinates adds, and the general field with its four pairs.

The conventions are those of the read list. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $\mathbb{B}_{C}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ is the centre; $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ are the anti-Hermitian and Hermitian fixed subspaces. The gradient is $\tilde\nabla=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$, and $\Box=\tilde\nabla\tilde\nabla^{\natural}=\partial^{2}/\partial R_t^{2}+\Delta$, with $\partial^{2}/\partial R_t^{2}=-\partial^{2}/\partial {r'_{t}}^{2}$ on the material sector, so that on that sector $\Box=\Delta-\partial^{2}/\partial {r'_{t}}^{2}$ in one length unit. The four-position is $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ and the four-wavevector is $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$. The mass wave number is $k_m=mc/\hbar$. The amplitude–phase decomposition and the non-relativistic quantum potential are those of *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form*; the phase gradient as the four-momentum is that of *Relativistic Mechanics from the Dirac Wave*; the polar word is that of *The Polar Decomposition of an N-Regular Biquaternion*.

## The Scalar Case: the Ansatz and Its Domain

### The field in amplitude and phase

Write the coefficient as $\Xi_t=\lvert\Xi_t\rvert\exp(iS_t/\hbar)$ with $\lvert\Xi_t\rvert>0$ real and $S_t$ real, that is, the element as $\tilde\Xi=\lvert\Xi_t\rvert\exp(iS_t/\hbar)e_t$. The exponential is central, so it commutes with everything, and the amplitude is central too. The symbol is the companion's own for the coefficient of $e_t$, so the polar form and the complex form of the article name the field by the same letter, and nothing has to be translated between them. What is left beyond the two is the angle,

$$
\theta_{\mathrm{phs}}=\frac{S_t}{\hbar},
$$

and the angle is the only quantity here carrying a choice: $\theta_{\mathrm{phs}}$ is defined modulo $2\pi$, equivalently $S_t$ modulo $2\pi\hbar$, and that shift is the one thing the field does not see. The role tag is not decoration. The conventions give the bare letter $\theta$ to the rotor's angle and $\theta_{\mathrm{rpd}}$ to the rapidity (*Norm and Pairing Conventions*, §*The Word and Its Factors*), so the action's angle takes its own tag here and no display has to be read twice.

This is the gauge of the WKB article, and it is a gauge rather than an assumption. A complex amplitude would also represent the field; the choice $\lvert\Xi_t\rvert>0$ real is what makes the transport equation below take its divergence form, and the reason is given there.

### The scope: one coefficient, and not the four

The ansatz presupposes that the phase can be factored out of the field as a whole. That is possible when the field lies in the centre, and it is the restriction that defines this part of the article. For a general $\mathbb{B}$-valued field the d'Alembertian acts on the four coefficients separately, so each coefficient carries its own amplitude and its own phase, and there is no single $S$ to write for the element as a whole.

The conclusion is not that the equation has no polar form, and the two statements are different. It is that the equation has one polar form per coefficient, four in all, and that no single pair $(r,S)$ describes the element. The choice made here is to read one of those coefficients, $\Xi_t$, and the scalar's home in the centre is the subject of *The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module*. What the restriction buys is that the two real equations below are two and not eight. What it costs is that the frame factor, which is the whole of the spin content of the polar form, is absent by construction. The four-pair case is taken up in §*General Fields*.

### Where the form ends: the nodal set is the cone

The form is defined where $\lvert\Xi_t\rvert\neq0$. Since $\langle\tilde\Xi\rangle_{\natural}=\Xi_t^{2}$ and $\langle\tilde\Xi\rangle_{*}=\lvert\Xi_t\rvert^{2}$ on the centre, the two conditions coincide:

$$
\lvert\Xi_t\rvert=0
\qquad\Longleftrightarrow\qquad
\langle\tilde\Xi\rangle_{\natural}=0 .
$$

So the locus where the polar form fails is the locus where the field meets the zero-divisor cone, and for a central field that locus is exactly the nodal set of the wave. This is the sharpest difference from the Dirac case. There the cone is not the zero field: a massless solution obeys $\tilde K_{\Phi}\tilde\xi=0$ with $\tilde K_{\Phi}$ of rank one, and such a $\tilde\xi$ is itself of rank one, hence on the cone identically. The polar word has no value on a solution that is nowhere zero. Here it has a value everywhere except at the nodes, and the nodes are where the density vanishes anyway.

The failure is not a defect of the method. $S_t$ is undefined at a node because the phase of zero is undefined, and the current $\tilde J_{\Phi}$ vanishes there, so no observable is lost. What is lost is differentiability of $S_t$, and the transport equation is written in terms of $\lvert\Xi_t\rvert^{2}\partial S_t/\partial r'_t$ and $\lvert\Xi_t\rvert^{2}\nabla S_t$ precisely because those products stay differentiable where $S_t$ does not.

The equivalence is a property of the central field, and it does not survive the general case. There the condition for the element is $\langle\tilde\Xi\rangle_{\natural}\neq0$, while the condition for a coefficient is $\Xi_\mu\neq0$, and the second is the weaker. The element $e_t+i\vec e_x$ is on the cone although both of its coefficients are nonzero, as §*General Fields* shows. For a scalar, then, the form ends exactly at the nodes; for a general field it ends on a larger set.

### The polar word degenerates on a central field

State the algebraic question exactly. The corpus's polar word is built from $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}$ and $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$, and reads

$$
\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad r>0,\quad \alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}],
$$

with $r$ the scale, $\exp(i\alpha)$ the central phase, $\tilde U_{\Psi,\mathrm b}$ the frame rotor, Hermitian positive with $N$-norm one, and $\tilde u_{\mathrm r}$ a rotor, a unit real quaternion. The spelling, the ranges and the order are those of *Norm and Pairing Conventions*, §*The Word and Its Factors*, and are not restated here. The word is defined on the complement of the cone. Applied to the field it gives the following.

*Proposition.* Let $\tilde\Xi=\lvert\Xi_t\rvert e^{i\theta_{\mathrm{phs}}}e_t$ with $\lvert\Xi_t\rvert>0$ and $\theta_{\mathrm{phs}}\in(-\pi,\pi]$. Then $\tilde Q_H=\lvert\Xi_t\rvert e_t$, and the word has $r=\lvert\Xi_t\rvert$ and $\tilde U_{\Psi,\mathrm b}=e_t$, with its last two factors fixed by the branch of $\theta_{\mathrm{phs}}$: $\alpha=\theta_{\mathrm{phs}}$ and $\tilde u_{\mathrm r}=e_t$ for $\theta_{\mathrm{phs}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, $\alpha=\theta_{\mathrm{phs}}-\pi$ and $\tilde u_{\mathrm r}=-e_t$ for $\theta_{\mathrm{phs}}\in(\tfrac{\pi}{2},\pi]$, and $\alpha=\theta_{\mathrm{phs}}+\pi$ and $\tilde u_{\mathrm r}=-e_t$ for $\theta_{\mathrm{phs}}\in(-\pi,-\tfrac{\pi}{2}]$.

*Proof.* The Hermitian norm of a central element is $\Xi_t\Xi_t^{*}=\lvert\Xi_t\rvert^{2}e_t$, whose positive square root is $\lvert\Xi_t\rvert e_t$; that is $\tilde Q_H$, positive definite because $\lvert\Xi_t\rvert>0$, with scale $r=\lvert\Xi_t\rvert$. Then $\tilde Q_0=(\lvert\Xi_t\rvert e_t)^{-1}\tilde\Xi=e^{i\theta_{\mathrm{phs}}}e_t$, a central element of modulus one, and the word's second factor is $\tilde Q_0$ divided by its rotor. A central unit element is $\exp(i\alpha)\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r}=\pm e_t$, since $\pm e_t$ are the only real unit quaternions in the centre. Since $\theta_{\mathrm{phs}}$ lies in $(-\pi,\pi]$ and $\alpha$ must lie in $(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, the sign is forced: the identity $\exp(i\theta_{\mathrm{phs}})e_t=\exp(i(\theta_{\mathrm{phs}}\mp\pi))(-e_t)$ holds on the two outer intervals, and only the branch written leaves $\alpha$ inside its range. The split is by the phase and not by the sign of the scalar part, because at $\theta_{\mathrm{phs}}=\pm\tfrac{\pi}{2}$ the real part vanishes while the angle is at the edge of its range. The frame rotor is $e_t$ in both cases, being the only Hermitian positive definite central element of $N$-norm one.

**The half-turn lives in the rotor, not in the angle.** The physics ansatz keeps $\lvert\Xi_t\rvert>0$ and lets $S_t/\hbar$ run over $(-\pi,\pi]$, so a field of negative scalar part is $\lvert\Xi_t\rvert e^{i\pi}e_t$ and carries $S_t/\hbar=\pi$. The word instead confines its own angle $\alpha$ to a half-turn and deposits the excess in $\tilde u_{\mathrm r}$, which is then $-e_t$. The two agree pointwise, $S_t/\hbar=\alpha$ when $\tilde u_{\mathrm r}=e_t$ and $S_t/\hbar=\alpha+\pi$ when $\tilde u_{\mathrm r}=-e_t$, so the identification is stated with its branch. The half-turn is invisible to every observable here, since $\lvert\Xi_t\rvert$ and $\partial S_t/\partial r'_t$ are unchanged, and it is visible in the word's factors. The word of a nonzero central field is therefore the polar form above with $\lvert\Xi_t\rvert=r$ and the algebra's central phase $e^{iS_t/\hbar}$, exact where it is defined, and the density is $\lvert\Xi_t\rvert^{2}=r^{2}$.

The count confirms the degeneracy. The field carries two real parameters. The word has $1+1+3+3=8$ slots, and six are frozen at the identity, leaving the scale and the phase. The word is therefore a bijection

$$
\mathbb{R}_{>0}\times(-\tfrac{\pi}{2},\tfrac{\pi}{2}]\times\{\pm e_t\}\longrightarrow\mathbb{C}\setminus\{0\},
\qquad (r,\alpha,\tilde u_{\mathrm r})\mapsto r\,e^{i\alpha}\tilde u_{\mathrm r},
$$

which is a polar coordinate chart. The six frozen parameters are not small; they are zero on every scalar field, at every event.

The amplitude is the topological norm, $\lvert\Xi_t\rvert=\bigl(\langle\tilde\Xi\rangle_{*}\bigr)^{1/2}$, and it is not the polar modulus $\Rho=\bigl(\langle\tilde\Xi\rangle_{\natural}\bigr)^{1/2}$, which is complex. On the centre $\lvert\Rho\rvert=\lvert\Xi_t\rvert=r$; the four norms and their collapse there are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## The Two Real Equations

### The identity

The derivatives of the ansatz separate into a real and an imaginary part with no remainder, because $\lvert\Xi_t\rvert$ and $S_t$ are real and the exponential is central. Since $\Box=\Delta-\partial^{2}/\partial {r'_{t}}^{2}$ on the material sector, and the second derivative of $\lvert\Xi_t\rvert\,e^{iS_t/\hbar}$ in $r'_t$ reads

$$
\frac{\partial^{2}}{\partial {r'_{t}}^{2}}\left(\lvert\Xi_t\rvert\,e^{iS_t/\hbar}\right)
=e^{iS_t/\hbar}\left\{\frac{\partial^{2}\lvert\Xi_t\rvert}{\partial {r'_{t}}^{2}}+\frac{2i}{\hbar}\frac{\partial S_t}{\partial r'_t}\frac{\partial \lvert\Xi_t\rvert}{\partial r'_t}
+\frac{i\lvert\Xi_t\rvert}{\hbar}\frac{\partial^{2}S_t}{\partial {r'_{t}}^{2}}
-\frac{\lvert\Xi_t\rvert}{\hbar^{2}}\left(\frac{\partial S_t}{\partial r'_t}\right)^{2}\right\},
$$

$\Delta$ acting on the same field gives the same display with $\nabla$ in place of $\partial/\partial r'_t$ in every term, and subtracting the second from the first, since $\Box=\Delta-\partial^{2}/\partial {r'_{t}}^{2}$, gives

$$
\Box\!\left(\lvert\Xi_t\rvert\,e^{iS_t/\hbar}\right)
= e^{iS_t/\hbar}\left\{\Box\lvert\Xi_t\rvert+\frac{\lvert\Xi_t\rvert}{\hbar^{2}}\left[\left(\frac{\partial S_t}{\partial r'_t}\right)^{2}-\lvert\nabla S_t\rvert^{2}\right]+\frac{i}{\hbar}\left[\frac{1}{\lvert\Xi_t\rvert}\nabla\cdot\!\left(\lvert\Xi_t\rvert^{2}\nabla S_t\right)-\frac{1}{\lvert\Xi_t\rvert}\frac{\partial}{\partial r'_t}\!\left(\lvert\Xi_t\rvert^{2}\frac{\partial S_t}{\partial r'_t}\right)\right]\right\}.
$$

The first two terms are real and the third is purely imaginary, so the equation $(\Box-k_m^{2})\Xi_t=0$ separates into two equations over the reals. Dividing by $\lvert\Xi_t\rvert\,e^{iS_t/\hbar}$ and using $\hbar k_m=mc$,

$$
\boxed{\;\left(\frac{\partial S_t}{\partial r'_t}\right)^{2}-\lvert\nabla S_t\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert}\;}
\qquad
\boxed{\;\nabla\cdot\!\left(\lvert\Xi_t\rvert^{2}\nabla S_t\right)-\frac{\partial}{\partial r'_t}\!\left(\lvert\Xi_t\rvert^{2}\frac{\partial S_t}{\partial r'_t}\right)=0\;}
$$

The first is the amplitude equation and the second is the transport equation. Together they are equivalent to the Klein–Gordon equation for a field of this form. Both are written with the one length unit of the material sector: the time derivative is $\partial/\partial r'_t$, no $c$ appears beside it, and no factor of $c^{-2}$ multiplies the temporal term. That is not a setting of $c=1$; it is the coordinate $r'_t=c\,t'$ doing the conversion once, in the definition of $\Box$.

### The amplitude equation

Read the phase gradient as the four-momentum. The corpus's momentum is $\tilde P_{\Phi}=i(E/c)e_t+\vec p$, and the gradient of an action is the momentum with $\vec p=\nabla S_t$ and

$$
E=-c\,\frac{\partial S_t}{\partial r'_t}.
$$

The factor $c$ is not decoration. $r'_t$ is a length and $E$ is a rate times an action, so a display that equated $E$ with $-\partial S_t/\partial r'_t$ would have set $c=1$ at that place; the corpus's rule for a rate against a length is that the factor goes on the derivative, and it does here. Substituting $(\partial S_t/\partial r'_t)^{2}=E^{2}/c^{2}$ and $\lvert\nabla S_t\rvert^{2}=\lvert\vec p\rvert^{2}$ into the amplitude equation,

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert},
$$

which is the mass shell with the mass term shifted by $Q_{\mathrm{qnt}}$. The shift is the only place the amplitude enters this equation, and it enters as a curvature: $Q_{\mathrm{qnt}}$ is the d'Alembertian of $\lvert\Xi_t\rvert$ divided by $\lvert\Xi_t\rvert$ itself.

**The plane-wave dispersion relation, and its remainder.** Dividing by $\hbar^{2}$ and multiplying by $-1$ gives the same statement on the wave biquaternion,

$$
\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}+\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert},
$$

which is the companion's $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ with one term added. The added term vanishes exactly when $\Box\lvert\Xi_t\rvert=0$: for a plane wave of constant amplitude it does, and for a wave packet, a bound state, or any state whose amplitude is not annihilated by $\Box$ it does not. The polar form shows what the amplitude must supply, and the remainder is the whole of the difference between the equation and the box.

**The quantum potential is the WKB one, with the Laplacian promoted.** The WKB article writes $Q_{\mathrm{qnt}}=-\frac{mc^{2}}{2k_m^{2}}\frac{\nabla^{2}\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert}$ for the stationary spin-$0$ state. Since $mc^{2}/(2k_m^{2})=\hbar^{2}/(2m)$, the coefficient here is the same and the operator is $\Box$ in place of the Laplacian in the three space coordinates. The relativistic $Q_{\mathrm{qnt}}$ is the static $Q_{\mathrm{qnt}}$ of the non-relativistic theory, with the second derivative taken in all four coordinates instead of three. The term appears only because the symbol is second order: a first-order operator applied to $\lvert\Xi_t\rvert e^{iS_t/\hbar}$ gives one derivative of the amplitude and no $\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert$, which is why the polar form of the Dirac wave stops at the eikonal and the four-momentum (*Relativistic Mechanics from the Dirac Wave*).

### The quantum potential depends on the density alone

The bracket $\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert$ carries the amplitude and its second derivatives, so $Q_{\mathrm{qnt}}$ looks as though it needs the amplitude and not the density. It does not. With $u=\ln \lvert\Xi_t\rvert$,

$$
\Box e^{u}=e^{u}\left(\Box u+(\partial u)^{2}\right),
\qquad
(\partial u)^{2}=\lvert\nabla u\rvert^{2}-\left(\frac{\partial u}{\partial r'_t}\right)^{2},
$$

so that $\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert=\Box u+(\partial u)^{2}$, and with $u=\tfrac12\ln \lvert\Xi_t\rvert^{2}$,

$$
\boxed{\;Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\left[\frac{1}{2}\Box\ln \lvert\Xi_t\rvert^{2}+\frac{1}{4}\left(\partial\ln \lvert\Xi_t\rvert^{2}\right)^{2}\right]\;}
$$

The quantum potential is a functional of the density $\lvert\Xi_t\rvert^{2}$ and of nothing else. Two consequences follow. The density is gauge invariant: it is unchanged when the central phase is shifted, and it is what a probability is built from, so $Q_{\mathrm{qnt}}$ is defined without reference to the phase. And the bracket separates: its first term is $\tfrac12\Box\ln \lvert\Xi_t\rvert^{2}$, and its second is $\tfrac14(\partial\ln \lvert\Xi_t\rvert^{2})^{2}$, whose spatial part is $\lvert\nabla\ln \lvert\Xi_t\rvert\rvert^{2}$, the squared logarithmic gradient of the amplitude, while its temporal part enters with the opposite sign because $\Box$ is the d'Alembertian and not the Laplacian.

The identity is not an accident of the logarithm. It is the statement that $Q_{\mathrm{qnt}}$ measures the curvature of the density on a logarithmic scale, which is why it is large where the density varies rapidly in proportion to itself and small where the density is flat, and why it is small for a wave packet whose envelope is broad compared with $\hbar/(mc)$. Everywhere else in the pair $\hbar$ is absorbed into the angle, into $\tilde K_{\Phi}$, and into $k_m$; in $Q_{\mathrm{qnt}}$ it cannot be, because $Q_{\mathrm{qnt}}$ compares a quantum curvature with a classical rest energy.

### The transport equation

The second equation is a conservation law in divergence form. Dividing by $m$ and using the two readings of the previous section it is $c\,\partial\rho_{\mathrm{chg}}/\partial r'_t+\nabla\cdot\vec j=0$ with the $\rho_{\mathrm{chg}}$ and $\vec j$ of the next section, so it is the continuity equation of the four-current in the companion's own form. The factor $c$ on the time term is the rule for a rate against a length: $r'_t$ is a length, so a time derivative is $c$ times the derivative in $r'_t$, the same conversion as in $E=-c\,\partial S_t/\partial r'_t$. The temporal term carries the sign it carries because $E=-c\,\partial S_t/\partial r'_t$, and that sign is what makes the temporal component $\lvert\Xi_t\rvert^{2}E/(mc^{2})$ rather than its negative.

For a plane wave the equation is satisfied identically, since $\lvert\Xi_t\rvert$ is constant and $S_t$ is linear. For a general wave it constrains the pair, and it is the equation that fixes the amplitude once the action is given, or the action once the amplitude is given. The two equations are not independent: each contains both $\lvert\Xi_t\rvert$ and $S_t$. The amplitude equation carries the second derivatives of $\lvert\Xi_t\rvert$ and the squared gradient of $S_t$; the transport equation is first order in each and carries them only through the products $\lvert\Xi_t\rvert^{2}\partial S_t/\partial r'_t$ and $\lvert\Xi_t\rvert^{2}\nabla S_t$.

## The Momentum and the Current

### The phase gradient is the four-momentum

The biquaternionic gradient of the action is the four-momentum itself. Since $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$ on the material sector,

$$
\tilde\nabla S_t
= e_t\,\frac{\partial S_t}{\partial R_t}+\sum_\eta\vec e_\eta\,\frac{\partial S_t}{\partial R_\eta}
= -i\frac{\partial S_t}{\partial r'_t}e_t+\nabla S_t
= i\frac{E}{c}e_t+\vec p
= \tilde P_{\Phi}.
$$

The two spellings match slot by slot, and that is where the factor $c$ comes from: the temporal slot of the gradient is $-i\partial S_t/\partial r'_t$ and the temporal slot of the momentum is $iE/c$, so $E=-c\,\partial S_t/\partial r'_t$ is the algebra's own statement and not an extra convention. Also $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=\tilde\nabla S_t/\hbar$, and the mass shell of the previous section is the quaternionic norm of a gradient. This is the algebraic content of "the phase is the action": the four-momentum is not read off the phase by a rule, it is the algebra's derivative of it.

### The current is the squared amplitude times the four-velocity

The companion's current is $\tilde J_{\Phi}=ic\rho_{\mathrm{chg}}\,e_t+\vec j$ with

$$
\rho_{\mathrm{chg}}=\frac{i}{2k_m}\left(\Xi_t^{*}\frac{\partial\Xi_t}{\partial r'_t}-\Xi_t\,\frac{\partial\Xi_t^{*}}{\partial r'_t}\right),
\qquad
\vec j=-\frac{ic}{2k_m}\left(\Xi_t^{*}\nabla\Xi_t-\Xi_t\,\nabla\Xi_t^{*}\right).
$$

Substituting the ansatz, $\Xi_t^{*}\frac{\partial\Xi_t}{\partial r'_t}-\Xi_t\,\frac{\partial\Xi_t^{*}}{\partial r'_t}=\frac{2i\lvert\Xi_t\rvert^{2}}{\hbar}\frac{\partial S_t}{\partial r'_t}$ and $\Xi_t^{*}\nabla\Xi_t-\Xi_t\,\nabla\Xi_t^{*}=\frac{2i\lvert\Xi_t\rvert^{2}}{\hbar}\nabla S_t$, so the current becomes

$$
\rho_{\mathrm{chg}}=\frac{\lvert\Xi_t\rvert^{2}E}{mc^{2}},
\qquad
\vec j=\frac{\lvert\Xi_t\rvert^{2}\nabla S_t}{m},
\qquad
\boxed{\;\tilde J_{\Phi}=\frac{\lvert\Xi_t\rvert^{2}}{m}\tilde P_{\Phi}=\frac{\hbar \lvert\Xi_t\rvert^{2}}{m}\tilde K_{\Phi}\;}
$$

The current is $\lvert\Xi_t\rvert^{2}$ times the four-velocity: it is the squared amplitude times the four-momentum over the mass, and the coefficient $\lvert\Xi_t\rvert^{2}/m$ is a positive real scalar. Writing the temporal slot as $ic\rho_{\mathrm{chg}}$ with $\rho_{\mathrm{chg}}=\lvert\Xi_t\rvert^{2}E/(mc^{2})$ is consistent with $E=-c\,\partial S_t/\partial r'_t$: the two minus signs of the two conversions cancel, and the charge density is positive exactly when the energy is.

Check the plane wave. With $\Xi_t=\Xi_{\mathrm{amp}}\exp(i\,\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^{\natural}))$ for a complex constant $\Xi_{\mathrm{amp}}$ the amplitude is $\lvert\Xi_t\rvert=\lvert\Xi_{\mathrm{amp}}\rvert$ and the energy is $E=\hbar\omega$, so $\rho_{\mathrm{chg}}=\lvert\Xi_t\rvert^{2}\hbar\omega/(mc^{2})=\omega\lvert\Xi_{\mathrm{amp}}\rvert^{2}/(ck_m)$, which is the companion's value. The general formula reproduces it.

### Conservation is the transport equation

The companion proves that the current is conserved, in the form $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J_{\Phi})=0$. With the current written as in the box, the scalar part works out as

$$
\mathrm{Sc}\!\left(\tilde\nabla^{\natural}\tilde J_{\Phi}\right)
=\frac{1}{m}\left[\nabla\cdot\!\left(\lvert\Xi_t\rvert^{2}\nabla S_t\right)-\frac{\partial}{\partial r'_t}\!\left(\lvert\Xi_t\rvert^{2}\frac{\partial S_t}{\partial r'_t}\right)\right],
$$

and the bracket is the transport equation. So the conservation law and the imaginary part of the Klein–Gordon equation are the same equation, not two equations that agree. The companion describes conservation as the scalar projection of a stronger biquaternion equation; the polar form says which part of that stronger equation the wave equation actually contains. The imaginary part is one real equation, and it is the scalar slot of $\tilde\nabla^{\natural}\tilde J_{\Phi}=0$. The three vector slots are not implied: they would be three more equations for the two functions $\lvert\Xi_t\rvert$ and $S_t$, and the wave equation does not impose them.

### The two defects, and one mechanism

The companion records that $\rho_{\mathrm{chg}}$ is not positive definite, that it has the sign of the energy, and that this is a defect of the equation. The polar form supplies the mechanism.

$\tilde J_{\Phi}$ is a positive scalar $\lvert\Xi_t\rvert^{2}/m$ times $\tilde P_{\Phi}$. The sign of its temporal component is therefore the sign of the temporal component of $\tilde P_{\Phi}$, and the mass shell constrains only the norm of $\tilde P_{\Phi}$, not the sign of its time part. The constraint $\langle\tilde P_{\Phi}\rangle_{\natural}=-m^{2}c^{2}+\hbar^{2}\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert$ fixes that norm. Where the amplitude term is small the fixed value is negative, the constraint is a two-sheeted hyperboloid, and the two sheets are the two branches.

| branch | $E=-c\,\partial S_t/\partial r'_t$ | $\rho_{\mathrm{chg}}=\lvert\Xi_t\rvert^{2}E/(mc^{2})$ | amplitude $\lvert\Xi_t\rvert$ |
| --- | --- | --- | --- |
| positive frequency | $>0$ | $>0$ | $>0$ |
| negative frequency | $<0$ | $<0$ | $>0$ |

So the defect is one sign and one sign only. The density is positive on both sheets; what changes sign is the energy, and with it the charge density. An antiparticle is not a separate field in these variables. It is the same amplitude squared with the action running the other way.

The transport equation cannot see the difference. It is linear in $\partial S_t/\partial r'_t$ and in $\nabla S_t$ and therefore invariant under $S_t\to-S_t$, so both rows of the table satisfy it with the same $\lvert\Xi_t\rvert$. This is the polar form of the companion's statement that the second-order structure does not organize itself by the particle–antiparticle pair: the equation for the amplitude is even, and only the energy factor in $\rho_{\mathrm{chg}}$ is odd.

### The two imaginary operations on the action

The companion separates multiplication by the central $i$ from complex conjugation. In polar variables each acts on the one real variable, and neither touches the amplitude:

$$
i\,\Xi_t = \lvert\Xi_t\rvert\exp\!\left(\frac{i}{\hbar}\left(S_t+\frac{\pi\hbar}{2}\right)\right),
\qquad
\Xi_t^{*}=\lvert\Xi_t\rvert\exp\!\left(-\frac{iS_t}{\hbar}\right),
\qquad
\text{equivalently}\quad
i\,\tilde\Xi=\lvert\Xi_t\rvert\exp\!\left(\frac{i}{\hbar}\left(S_t+\frac{\pi\hbar}{2}\right)\right)e_t,\quad
\tilde\Xi^{*}=\lvert\Xi_t\rvert\exp\!\left(-\frac{iS_t}{\hbar}\right)e_t .
$$

The first translates the action by a quarter turn and the second reflects it. Since $E=-c\,\partial S_t/\partial r'_t$, the translation preserves the sheet of the mass shell and the reflection exchanges the sheets. That is the whole of the companion's pair of adjectives in these variables. It also gives the sector split in one line: $\tilde\Xi_{\Psi}=\lvert\Xi_t\rvert\cos(S_t/\hbar)e_t$ and $\tilde\Xi_{\Phi}=i\lvert\Xi_t\rvert\sin(S_t/\hbar)e_t$, so the material and informational parts are the two quadratures of one angle, and multiplication by $i$ exchanges them because a quarter turn does.

### The pair is the Takabayasi system

**The identification.** The two exact equations are the relativistic hydrodynamics of a spin-$0$ quantum fluid, which Takabayasi wrote in the same programme as his treatment of Dirac matter: the transport equation is his continuity equation and the amplitude equation is his relativistic Hamilton–Jacobi equation with the quantum potential. Nothing in the pair is added here, and its non-relativistic limit is Madelung's.

**The state variables.** The fluid is described by one density and one four-velocity,

$$
\tilde J_{\Phi}=\lvert\Xi_t\rvert^{2}\tilde V_{\Phi},
\qquad
\tilde V_{\Phi}=\frac{\tilde P_{\Phi}}{m}=\frac{\tilde\nabla S_t}{m},
\qquad
\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}+\frac{\hbar^{2}}{m^{2}}\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert}.
$$

The coefficient is the proper density of the markers, $\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}$ with $\rho_{\mathrm{num}}=\lvert\Xi_t\rvert^{2}$, and it is not the charge density: $\rho_{\mathrm{chg}}$ is the temporal component, and with $v'_t=E/(mc)$ the two are related by $\rho_{\mathrm{chg}}=(v'_t/c)\rho_{\mathrm{num}}$, which is $\gamma\rho_{\mathrm{num}}$ on shell, the conventions' $\rho_{\mathrm{chg}}=ϙ\gamma\rho_{\mathrm{num}}$ at unit charge. The fluid flows along the phase gradient, and the transport equation is the continuity equation of that density with that velocity.

The norm in the same display is the mass shell read as a statement about the fluid. The conventions fix it on shell, $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$ for a marker whose four-velocity is $\tilde P_{\Phi}/m$; here $\tilde P_{\Phi}$ is the gradient of the action, so the norm is $-c^{2}$ exactly when the amplitude term vanishes, and the flow is a unit timelike vector for a plane wave and not for a general wave. The fluid reading then has the same defect as the charge density, and from the same cause: what fails is the on-shell condition, not the continuity equation, which holds whatever the amplitude does.

**The flow is irrotational potential flow.** The velocity is a gradient, $\vec v_{\Phi}=\nabla S_t/m$, so the vorticity vanishes wherever the action is twice differentiable,

$$
\nabla\times\vec v_{\Phi}=\frac{1}{m}\nabla\times\nabla S_t=0 .
$$

The vorticity tensor vanishes for the same reason, being built from derivatives of that one gradient, so the flow is potential flow in the relativistic sense and not only in its spatial part, and no circulation is generated where the action is smooth. The exception is a nodal line, around which $S_t$ is multivalued: the curl vanishes off the node and the circulation around it need not, which is the topological charge left open in the questions below.

**The dynamics.** The two equations are continuity and a relativistic Hamilton–Jacobi equation with a quantum potential, and in the algebra's letters they are the divergence and the norm of one gradient,

$$
\mathrm{Sc}\!\left(\tilde\nabla^{\natural}\tilde J_{\Phi}\right)=0,
\qquad
\langle\tilde\nabla S_t\rangle_{\natural}=-m^{2}c^{2}+\hbar^{2}\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert}.
$$

The second term is the whole of the quantum content: with it the fluid is not dust, and without it the pair is relativistic irrotational dust, pressureless flow along the phase gradient.

**What the degeneracy means physically.** For the Dirac field the word's frame rotor and rotor carry the spin, and they vary from event to event. For a scalar they freeze at $e_t$, and the fluid they describe is the spinless and irrotational one. The degeneracy of the polar word is therefore not an accident of the centre: it is the statement that a spin-$0$ fluid has no spin degree of freedom for the frame to carry.

**What the biquaternion form adds.** The pair is one element and two of its reductions, and the reductions are the two the algebra always supplies: the norm of an element and the scalar part of a divergence. The Takabayasi equations are the norm and the divergence of the biquaternionic gradient of the action, and that is the whole of what the algebra contributes to them. Nothing in the fluid reading needs a raised index or a metric, because the one metric of the corpus is the identity and the four-velocity is already an element of $\mathbb{B}_{\Phi}$.

## The Non-Relativistic Limit

### The action carries the rest energy

The companion divides out the rest-mass phase $f=\exp(-ik_m r'_t)=\exp(-imc^{2}t'/\hbar)$ and expands what is left. In polar variables that step is a statement about $S_t$: the action is dominated by a term linear in the material time,

$$
S_t=-mc\,r'_t+\sigma,
\qquad
E=-c\,\frac{\partial S_t}{\partial r'_t}=mc^{2}+T_{\mathrm{kin}},
\qquad
T_{\mathrm{kin}}=-c\,\frac{\partial\sigma}{\partial r'_t},
$$

with $\sigma$ the envelope's action and $T_{\mathrm{kin}}$ the kinetic energy. The coefficient of $r'_t$ is $mc$ and not $mc^{2}$, because $r'_t$ is a length and $mc^{2}t'=mc\,r'_t$; writing $mc^{2}$ there would be the $c=1$ defect in the other direction. Dividing out $f$ and adding the rest term to the action are the same operation: the companion's $f$ is the leading term of $S_t$, and the companion's envelope $\chi$ is $\lvert\Xi_t\rvert\exp(i\sigma/\hbar)e_t$ in these variables.

### The quantum potential becomes the WKB one

Substituting $E=mc^{2}+T_{\mathrm{kin}}$ into the amplitude equation,

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}
\qquad\Longrightarrow\qquad
2mT_{\mathrm{kin}}+\frac{T_{\mathrm{kin}}^{2}}{c^{2}}=\lvert\vec p\rvert^{2}+2mQ_{\mathrm{qnt}} .
$$

Dropping $T_{\mathrm{kin}}^{2}/c^{2}$ and dropping $\partial^{2}\lvert\Xi_t\rvert/\partial {r'_{t}}^{2}$ against $\Delta\lvert\Xi_t\rvert$ in $Q_{\mathrm{qnt}}$,

$$
T_{\mathrm{kin}}=\frac{\lvert\vec p\rvert^{2}}{2m}+Q_{\mathrm{qnt}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Delta\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert},
$$

which is the WKB article's quantum Hamilton–Jacobi equation with $V=0$: the same $T_{\mathrm{kin}}$, the same $\vec p=\nabla S_t$, and the same $Q_{\mathrm{qnt}}$. The first dropped term is of relative order $T_{\mathrm{kin}}/(2mc^{2})$ and the second of order $v^{2}/c^{2}$.

### The transport becomes the continuity equation

In the same limit the temporal term of the transport equation keeps only the large part of $\partial S_t/\partial r'_t$, which is $-mc$:

$$
\frac{\partial}{\partial r'_t}\!\left(\lvert\Xi_t\rvert^{2}\frac{\partial S_t}{\partial r'_t}\right)
\simeq-mc\,\frac{\partial \lvert\Xi_t\rvert^{2}}{\partial r'_t},
$$

so the equation becomes

$$
c\,\frac{\partial \lvert\Xi_t\rvert^{2}}{\partial r'_t}+\nabla\cdot\!\left(\lvert\Xi_t\rvert^{2}\frac{\nabla\sigma}{m}\right)=0,
$$

which is $\frac{\partial \lvert\Xi_t\rvert^{2}}{\partial t'}+\nabla\cdot\left(\lvert\Xi_t\rvert^{2}\frac{\nabla\sigma}{m}\right)=0$ once the derivative in the length is converted to a derivative in the time. This is the continuity equation for the density $\lvert\Xi_t\rvert^{2}$ with the velocity $\vec p/m$; in the rate form it carries no $c$, because it is a rate against a rate. The non-relativistic pair of the WKB article is the leading order of this pair, with the two expansions being the same expansion, and the quantum potential of that article is the one written here with $\Box$ replaced by the Laplacian.

## What the Polar Form Does and Does Not Add

The objection has to be stated before it is answered. For a scalar field the polar form is a change of variables, two real functions for one complex one, and the two real equations are the relativistic form of Madelung's pair, that is, the spin-$0$ case of Takabayasi's hydrodynamics. No prediction is added, and the equation is not new.

Four things are nevertheless not a relabelling.

**The dispersion relation is a plane-wave statement, and the remainder is visible.** $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ holds for a plane wave and misses a general wave by the term $\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert$. In the complex form the box is read as a statement about one wave; in the polar variables the same equation says which part belongs to the action and which to the amplitude.

**The two defects become one mechanism.** The sign of the charge is the sign of the energy, and the reason is that the current is $\lvert\Xi_t\rvert^{2}$ times the four-velocity. That is one line in these variables and a computation in the others. It also says what a repair would cost. The coefficient $\lvert\Xi_t\rvert^{2}/m$ cannot be made negative without ceasing to be positive, so the sign cannot be removed by rewriting the current; only the energy's sign can change it, and the energy's sign is the branch.

**The two imaginary operations become transformations of one variable.** The companion's distinction between the central $i$ and complex conjugation is a claim about frequency and about sectors, argued from the structure of the equation. Here it is two substitutions on $S_t$, and it is verified by inspecting $\partial S_t/\partial r'_t$.

**The algebraic word degenerates.** That is not a relabelling in either direction, because it is a fact about the algebra and not about the coordinates. It follows from $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}$ alone, and the polar form is where it becomes visible as the identification $\lvert\Xi_t\rvert=r$, the two being the topological norm and the scale whenever the field is central. The four-factor word is the right tool where the frame has content and the wrong tool here; for a spin-$0$ wave the frame is fixed once and for all, and a decomposition whose six frame parameters cannot vary is a decomposition of nothing. What it does describe is Takabayasi's spinless fluid, and the degeneracy is that fluid's absence of spin.

The honest ledger is: the equation, no; the coordinates, yes; and the coordinates are what make the algebra's own structure — the norm of a gradient, the degeneracy of the word, the positivity of the density factor — legible in the physics.

## General Fields

Everything above concerns the coefficient $\Xi_t$, with the other three set to zero. This section states what happens when they are switched on. There are three cases and they nest: the scalar case treated above, the case of one phase with a constant biquaternion polarization, and the fully general field in which amplitude and phase belong to each coefficient separately. The section takes them in that order and separates, in each, what carries over from what does not.

### The four equations are independent

Because $\Box$ is central with real coefficients,

$$
\Box\tilde\Xi=\sum_{\mu\in\{t,x,y,z\}}\left(\Box\Xi_\mu\right)e_\mu ,
$$

and the four units are linearly independent, so $\left(\Box-k_m^{2}\right)\tilde\Xi=0$ holds if and only if

$$
\left(\Box-k_m^{2}\right)\Xi_\mu=0
\qquad\text{for each }\mu\in\{t,x,y,z\}.
$$

No equation relates $\Xi_t$ to $\Xi_x$. The coefficient of $\vec e_x$ is as free as the coefficient of $e_t$, and a field with $\Xi_t=\Xi_y=\Xi_z=0$ and $\Xi_x\neq0$ is a solution of the same equation — it is simply a solution this article does not treat before this section.

The solution space is therefore a tensor product. Write $S$ for the set of complex scalar solutions of $(\Box-k_m^{2})f=0$. Then

$$
\left\{\tilde\Xi:\ (\Box-k_m^{2})\tilde\Xi=0\right\}=\mathbb{C}^{4}\otimes_{\mathbb{C}}S
=\left\{\sum_{\mu}e_\mu f_\mu:\ f_\mu\in S\right\},
$$

because the equation is linear with scalar coefficients and the four units are a basis. A general solution is four arbitrary scalar solutions placed in the four slots: nothing forces them to be equal, proportional, or related in any way. Each coefficient carries its own pair of spectral amplitudes, $a_\mu(\vec k)$ and $b_\mu(\vec k)$, eight complex functions in all, subject only to the one dispersion relation $\omega_k=c\sqrt{\lvert\vec k\rvert^{2}+k_m^{2}}$, which is the same for all four because it comes from $\Box$ and not from the slot.

### Four pairs, eight real equations

Give each coefficient its own amplitude and action,

$$
\Xi_\mu=\lvert\Xi_\mu\rvert\exp\!\left(\frac{iS_\mu}{\hbar}\right),
\qquad \lvert\Xi_\mu\rvert>0,\quad S_\mu\in\mathbb{R},
$$

and substitute into the equation for that coefficient. The pair of §*The Two Real Equations* comes back with $\Xi_t$ replaced by $\Xi_\mu$ and $S_t$ by $S_\mu$:

$$
\left(\frac{\partial S_\mu}{\partial r'_t}\right)^{2}-\lvert\nabla S_\mu\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box\lvert\Xi_\mu\rvert}{\lvert\Xi_\mu\rvert},
\qquad
\nabla\cdot\!\left(\lvert\Xi_\mu\rvert^{2}\nabla S_\mu\right)-\frac{\partial}{\partial r'_t}\!\left(\lvert\Xi_\mu\rvert^{2}\frac{\partial S_\mu}{\partial r'_t}\right)=0 .
$$

The count closes in both directions. Four complex coefficients are eight real functions, and the four complex equations are eight real equations, one pair per coefficient: nothing is missing and nothing is overdetermined. In particular the four equations are not a constraint system that a general field must satisfy, since each of them is a wave equation for its own function.

The four pairs have the same shape and no common content. The four actions $S_\mu$ are unrelated, so the four momenta $\tilde P_{\Phi,\mu}=\tilde\nabla S_\mu$ are unrelated, and a superposition may carry four different wave vectors. Within a single plane wave the four coefficients share one $\vec k$, because there is one phase and a phase has one gradient per event; the four-way freedom lives in superpositions and not in modes.

### One phase, a biquaternion amplitude

There is an intermediate case between the scalar and the fully general, and it is the one a plane wave actually realises. Let $\tilde A$ be a constant biquaternion and $f$ a complex scalar function, and set

$$
\tilde\Xi=\tilde A\,f,\qquad \tilde A\in\mathbb{B}\ \text{constant},\quad f\in\mathbb{C}.
$$

Because $\Box$ has real scalar coefficients and $\tilde A$ is constant, $\Box(\tilde A f)=\tilde A\,\Box f$, and the same holds for the mass term, so

$$
\left(\Box-k_m^{2}\right)\left(\tilde A f\right)=\tilde A\left(\Box-k_m^{2}\right)f .
$$

The bracket $\left(\Box-k_m^{2}\right)f$ is a complex scalar, that is, a central element, and each coefficient of $\tilde A$ times a central element is $A_\mu g$; since at least one $A_\mu$ is nonzero, $\tilde A g=0$ forces $g=0$. So for $\tilde A\neq0$ the field solves the Klein–Gordon equation if and only if $f$ does. The four coefficients are then $\Xi_\mu=A_\mu f$: proportional, with one phase $S=\hbar\arg f$, one set of nodes, and four complex constants that the equation never touches.

Three consequences follow, and they are what this case is for. First, the polarization is free and unconstrained: the equation constrains $f$ and never $\tilde A$, so $\tilde A$ is a constant of the solution rather than a dynamical variable, and its four complex entries cost nothing. Second, the charge density is the scalar one times the Hermitian norm of the polarization,

$$
\rho_{\mathrm{chg}}=\langle\tilde A\rangle_{*}\,\lvert f\rvert^{2}\frac{E}{mc^{2}},\qquad \langle\tilde A\rangle_{*}=\mathrm{Sc}\!\left(\tilde A\tilde A^{*}\right)=\sum_{\mu}\lvert A_\mu\rvert^{2},
$$

so a general polarization enters the density through one positive number and nothing else. Third, the word's frame is a constant and not the identity. Since $\tilde\Xi\tilde\Xi^{*}=\tilde A\tilde A^{*}\lvert f\rvert^{2}$ and $\lvert f\rvert^{2}$ is a positive central scalar, $\tilde Q_H=\tilde A_H\lvert f\rvert$, with $\tilde A_H$ the positive Hermitian square root of $\tilde A\tilde A^{*}$; writing $\tilde A=r_A\tilde U\tilde u_{\mathrm r}$ for the polarization, the word of the field has $r=r_A\lvert f\rvert$, frame $\tilde U$ and rotor $\tilde u_{\mathrm r}$, both constant. The pair of §*The Two Real Equations* therefore returns unchanged, read on $\lvert f\rvert=r/r_A$ and on the angle $\alpha$, with a frame that is not $e_t$. The degeneracy of §*The polar word degenerates on a central field* is a property of the central restriction and not of the equation, and a spin-$0$ field can carry a constant frame of its own without any of the machinery of the spin-$\tfrac12$ case.

The scalar case of this article is the case $\tilde A=A_t e_t$ with $A_t=1$ after rescaling $f$. So the article has treated one point of a four-complex-dimensional family of polarizations, and the family's other points are reached by multiplying, not by solving anything new.

### The charge density adds up over the four coefficients

One sum is exact and worth stating, because the answer is not the obvious one. With $\tilde\Xi^{*}=\Xi_t^{*}e_t-\Xi_x^{*}\vec e_x-\Xi_y^{*}\vec e_y-\Xi_z^{*}\vec e_z$ and $\vec e_\eta\vec e_\eta=-e_t$, the two sign changes cancel in the scalar part, and

$$
\mathrm{Sc}\!\left(\tilde\Xi^{*}\frac{\partial\tilde\Xi}{\partial r'_t}-\tilde\Xi\,\frac{\partial\tilde\Xi^{*}}{\partial r'_t}\right)
=\sum_{\mu}\left(\Xi_\mu^{*}\frac{\partial\Xi_\mu}{\partial r'_t}-\Xi_\mu\frac{\partial\Xi_\mu^{*}}{\partial r'_t}\right).
$$

So the companion's charge density, extended to a general field, is the sum of the four component densities with the same sign for all four: a vector coefficient contributes to $\rho_{\mathrm{chg}}$ exactly as a scalar one does. The natural guess is the opposite — that a spatial coefficient should enter with a minus — and it is wrong. The reason is algebraic: the Hermitian conjugate flips the sign of the three vector coefficients, and $\vec e_\eta^{2}=-e_t$ flips it back.

The extension has to be named as one. The companion defines the current for $\tilde\Xi=\Xi e_t\in\mathbb{B}_{C}$ and for nothing else, so the display above is not quoted from it; it is the same bilinear read on a larger domain. What it shows is that the additivity of the temporal slot belongs to the bilinear and not to the central restriction. The spatial slots behave differently, as the next subsection shows.

The mechanism of §*The two defects, and one mechanism* therefore survives without the centre. Computed on a field with $\Xi_x$ alone, the temporal slot of the bracket takes the same value, slot for slot, as on a central field with the same time dependence. The sign of the charge is the sign of the energy for each coefficient separately, and the reading needs no central field.

One consequence deserves a line, because it is the physical content of additivity. Two coefficients on opposite branches carry opposite charge, so a field with $\Xi_t$ on the positive branch and $\Xi_x$ on the negative one has $\rho_{\mathrm{chg}}=\lvert\Xi_t\rvert^{2}E_t/(mc^{2})-\lvert\Xi_x\rvert^{2}\lvert E_x\rvert/(mc^{2})$, which can vanish identically without either coefficient vanishing. The vanishing of the density is not the vanishing of the field, and for a general field it is not even a nodal condition.

### The spatial current does not add up

The other three slots do not behave this way, and the difference is not a small correction. Compute the bilinear on a field with one coefficient active, $\tilde\Xi=\Xi_\mu e_\mu$ with $\Xi_\mu=\lvert\Xi_\mu\rvert e^{i\phi_\mu}$, and its spatial slot $\eta$ is

$$
j_\eta^{(\mu)}=\sigma_{\eta\mu}\,\frac{\lvert\Xi_\mu\rvert^{2}}{m}\frac{\partial S_\mu}{\partial r_\eta},
\qquad
\sigma_{\eta\mu}=
\begin{cases}
+1, & \mu=t,\\[2pt]
+1, & \mu\neq t\ \text{and}\ \eta=\mu,\\[2pt]
-1, & \mu\neq t\ \text{and}\ \eta\neq\mu .
\end{cases}
$$

A scalar coefficient therefore reproduces $\vec j=\lvert\Xi_t\rvert^{2}\nabla S_t/m$ in all three slots, and $\mu=\eta$ reproduces it too: the current along a vector coefficient's own direction has the scalar sign. But the two transverse slots carry the opposite sign. The algebra is one line. The conjugation contributes a minus for a spatial coefficient; when $\eta=\mu$ the factor $\vec e_\mu\vec e_\mu=-e_t$ contributes a second minus and the two cancel; when $\eta\neq\mu$ the product $\vec e_\mu\vec e_\eta\vec e_\mu=+\vec e_\eta$ contributes none, and the conjugation's minus stands alone.

Two further facts, both verified rather than argued. The bilinear is not additive for the spatial slots: on a field with two or more coefficients active, the mixed terms are of the same order as the diagonal ones and do not cancel, so $\tilde J_{\Phi}$ of a general field is not the sum of its four projections. And the defect is not repaired by a common phase: even for the polarized field $\tilde A f$ of §*One phase, a biquaternion amplitude*, where all four coefficients share $S$, the spatial current is not $\langle\tilde A\rangle_{*}\lvert f\rvert^{2}\nabla S/m$.

The honest reading is that the companion's bilinear is a current for a central field, where it equals the density times the velocity, and it ceases to be one as soon as a vector coefficient is switched on. Whether the correct conserved current of a general biquaternion Klein–Gordon field is another bilinear of the same algebra, or needs the odd element as in *The Polar Form of the Dirac Equation in Biquaternionic Form*, §*The Bilinear That Is Not the Current*, is not settled here. What is settled is that this bilinear will not do, and that the obstruction is visible in three slots of four.

### The frame is a field

What the polarized case §*One phase, a biquaternion amplitude* fixes and the general case does not is the frame. In the general case the word still applies to any $N$-regular element, so $\tilde\Xi=r\exp(i\alpha)\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ exists; but the frame $\tilde U_{\Psi,\mathrm b}$ and the rotor $\tilde u_{\mathrm r}$ are fields, and their derivatives no longer vanish. Substituting the word into the Klein–Gordon equation therefore does not give two real equations: it gives eight, for the eight real parameters, and the derivatives of the frame enter them as terms of the same order as those of the amplitude.

So the two-equation form needs a constant frame and a constant rotor, and that is exactly the condition that the field be a complex scalar times a constant element, $\tilde\Xi=f\tilde A$, which is §*One phase, a biquaternion amplitude*. The scalar case is the member of that family with $\tilde A\propto e_t$, and the family has no other members: a varying frame with a single phase is possible, but then the equation must also determine the frame, and what looked like a pair becomes a larger system. Two parameters of the field are what a pair can describe, and the other six have to be constants.

### The domain is larger than the nodal set

For the scalar the form fails exactly where $\lvert\Xi_t\rvert=0$. For a general field the condition for the word is $\langle\tilde\Xi\rangle_{\natural}\neq0$, which is strictly stronger. Take

$$
\tilde\Xi=\Xi_t\left(e_t+i\vec e_x\right),
\qquad \Xi_t\neq0 .
$$

Both coefficients are nonzero, and $\langle\tilde\Xi\rangle_{\natural}=\Xi_t^{2}+(i\Xi_t)^{2}=0$, so the element is on the zero-divisor cone: $\left(e_t+i\vec e_x\right)\left(e_t-i\vec e_x\right)=0$. A nowhere-zero field can therefore sit on the cone, exactly as the massless Dirac solution does in §*Where the form ends*. The four componentwise polar forms still exist there, because each $\Xi_\mu$ is nonzero; it is the one-phase description of the element that has no value.

### What this section does and does not establish

Established, and checked directly rather than inherited: the four equations decouple and are independent; each coefficient admits the pair, with eight real equations for eight real functions; a constant polarization multiplies a scalar solution and enters the density only through its Hermitian norm; the charge density is exactly the sum of the four component densities, all with the same sign; a single vector coefficient contributes to the spatial current with the scalar sign in its own slot and the opposite sign in the other two; the bilinear is not additive over the coefficients in the spatial slots; and the domain of the element's word is the cone, not the nodal set of any one coefficient.

Not established: what the correct conserved current of a general field is. The bilinear fails three of its four slots, and *The Polar Form of the Dirac Equation in Biquaternionic Form*, §*The Bilinear That Is Not the Current*, is the precedent for the failure rather than the repair. Whether the mixed terms found above are a spin current in the sense of that article, and whether any current of the even algebra can be conserved without the odd element, are open.

The ledger of §*What the Polar Form Does and Does Not Add* stands unchanged, and this section does not move it. The four biquaternion equations are four scalar equations, the operator is central, and no prediction is added by writing them as one element. What the general case adds is a sharper reading of what the scalar case was: not a simplification of the equation, which none is available, but the choice of a polarization, of a frozen frame, and — for the current — of the only case in which the companion's bilinear is what it claims to be.

## Open Questions

1. **The locus where the effective mass vanishes.** The amplitude equation carries $m^{2}c^{2}-\hbar^{2}\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert$. That combination can vanish, and can change sign, on a set of events even though $m\neq0$. Whether such a locus has a physical interpretation, or is an artefact of the variables, is not settled here. The natural guess is that it is where the de Broglie wavelength of the amplitude variation reaches the Compton length, and a guess is all it is.

2. **The nodal set.** At $\lvert\Xi_t\rvert=0$ the phase is undefined, the current vanishes, and the transport equation remains meaningful while $S_t$ does not. Whether the winding of $S_t$ around a nodal line carries a topological charge, and whether that charge is an object of the algebra rather than of the phase, is open. The corpus's *Zero Divisors as a Physical Locus in Biquaternionic Form* is the natural place to ask it, since the nodal set is exactly where the field is on the cone.

3. **The quantum potential when $c$ varies.** $Q_{\mathrm{qnt}}$ is a central real scalar, it is a Lorentz scalar, and by the identity above it depends on the density alone, so every shift of the central phase leaves it unchanged. What is not settled is its behaviour under the local complex structure, where $c=1/\sqrt{\epsilon\mu}$ is a function of position. The identity still holds pointwise with $\Box$ read at each event, but whether the combination survives as an object of the algebra's own geometry, rather than as a scalar of the coordinate description, is inherited as open from the companion.

4. **Minimal coupling.** The current is $(\lvert\Xi_t\rvert^{2}/m)\tilde P_{\Phi}$, and the minimal coupling of the corpus adds a coupling times the four-potential to the four-momentum inside the equation. Whether the same replacement acts on the current, and whether $Q_{\mathrm{qnt}}$ is untouched, is a question for the coupled treatment; nothing here decides it.

5. **Trajectories, and the speed of light.** The amplitude equation defines trajectories by $\vec p=\nabla S_t$, and $Q_{\mathrm{qnt}}$ enters them as a potential. Whether the resulting flow respects $c$ as a limit, and whether the relativistic polar form admits a trajectory reading at all, is the standing difficulty of the de Broglie–Bohm programme in its relativistic form, and the polar variables relocate it rather than remove it.

6. **The current of a general field.** The bilinear that serves as the current for a central field is additive in its temporal slot and neither additive nor correctly signed in its spatial slots: a vector coefficient's transverse slots carry the opposite sign. Whether the correct conserved current is another bilinear of the even algebra, whether it needs the odd element as the Dirac companion argues, and whether the transverse terms are a spin current, are open. They are the natural first question for the general field, and nothing in the scalar case answers them.

## Summary

The first part of this article treats the scalar case, in which the field is central, $\tilde\Xi=\Xi_t e_t$, and the field is the one complex scalar $\Xi_t$. Its polar form is $\Xi_t=\lvert\Xi_t\rvert\exp(iS_t/\hbar)$ with $\lvert\Xi_t\rvert>0$ real and $S_t$ the action, so the angle $S_t/\hbar$ is a pure number and $S_t$ carries $\mathrm{J\,s}$. Substituting it into $(\Box-k_m^{2})\Xi_t=0$ gives two exact real equations,

$$
\left(\frac{\partial S_t}{\partial r'_t}\right)^{2}-\lvert\nabla S_t\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert},
\qquad
\nabla\cdot\!\left(\lvert\Xi_t\rvert^{2}\nabla S_t\right)-\frac{\partial}{\partial r'_t}\!\left(\lvert\Xi_t\rvert^{2}\frac{\partial S_t}{\partial r'_t}\right)=0,
$$

which together are equivalent to the one complex equation. The pair is Takabayasi's relativistic hydrodynamics of a spin-$0$ fluid. Both are written in the single length unit of the material sector, with no $c^{-2}$ on the temporal term and no $c$ beside the derivative. In the momentum variables $\vec p=\nabla S_t$ and $E=-c\,\partial S_t/\partial r'_t$ the first reads $\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$ with $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert}$; the second is the exact relativistic analogue of the WKB transport equation. The factor $c$ in $E=-c\,\partial S_t/\partial r'_t$ is the algebra's own statement, since the temporal slot of $\tilde\nabla S_t$ is $-i\partial S_t/\partial r'_t$ and the temporal slot of $\tilde P_{\Phi}$ is $iE/c$. The pair reduces to the WKB pair when the action is dominated by its rest term $-mc\,r'_t$ and $\Box\lvert\Xi_t\rvert$ is replaced by $\Delta\lvert\Xi_t\rvert$. The quantum potential is the logarithmic curvature of the density, $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\left[\frac{1}{2}\Box\ln \lvert\Xi_t\rvert^{2}+\frac{1}{4}\left(\partial\ln \lvert\Xi_t\rvert^{2}\right)^{2}\right]$, so it is a functional of the density alone.

The phase gradient is the four-momentum, $\tilde P_{\Phi}=\tilde\nabla S_t$, and in polar variables the quaternionic norm of a gradient reads $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}+\Box\lvert\Xi_t\rvert/\lvert\Xi_t\rvert$. The boxed dispersion relation of the companion is the case $\Box\lvert\Xi_t\rvert=0$, which a plane wave satisfies and a general wave does not.

The current is $\tilde J_{\Phi}=(\lvert\Xi_t\rvert^{2}/m)\tilde P_{\Phi}$, with $\rho_{\mathrm{chg}}=\lvert\Xi_t\rvert^{2}E/(mc^{2})$ and $\vec j=\lvert\Xi_t\rvert^{2}\vec p/m$. Its conservation, $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J_{\Phi})=0$, is the transport equation and not merely consistent with it. The sign defect is the sign of $E$: the mass shell is a two-sheeted hyperboloid, $\lvert\Xi_t\rvert^{2}$ is positive on both sheets, and the charge density changes sign because the energy does. In the same variables multiplication by the central $i$ translates the action by $\pi\hbar/2$ and preserves the sheet, while complex conjugation reflects the action and exchanges the sheets; the material and informational parts are the quadratures $\lvert\Xi_t\rvert\cos(S_t/\hbar)$ and $\lvert\Xi_t\rvert\sin(S_t/\hbar)$ of the one angle.

The polar word of the algebra is the polar form restricted to the centre. For a nonzero central field $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}=\lvert\Xi_t\rvert e_t$ and $\tilde Q_0=e^{i\theta_{\mathrm{phs}}}e_t$, so the frame rotor is $e_t$, the rotor is $\pm e_t$, and six of the eight word parameters are frozen; the word is the polar chart $(r,\alpha,\tilde u_{\mathrm r})\mapsto r\,e^{i\alpha}\tilde u_{\mathrm r}$ with $\lvert\Xi_t\rvert=r$. The domain is the complement of the nodal set, and the nodal set is exactly where the field meets the zero-divisor cone. This is the opposite of the Dirac case, where the cone is the massless shell and a nowhere-zero solution can lie on it.

The general field is not a harder version of this one; it is four copies of it. Because $\Box$ is central, $\left(\Box-k_m^{2}\right)\tilde\Xi=0$ is the four equations $\left(\Box-k_m^{2}\right)\Xi_\mu=0$, the solution space is $\mathbb{C}^{4}\otimes S$ with $S$ the scalar solutions, and each coefficient carries its own pair $(\lvert\Xi_\mu\rvert,S_\mu)$, so the eight real parameters are eight real equations with no constraint among them. A constant polarization is the intermediate case: $\tilde\Xi=\tilde A f$ solves the equation exactly when $f$ does, the four coefficients are proportional, and the density is $\langle\tilde A\rangle_{*}\lvert f\rvert^{2}E/(mc^{2})$ — one scalar solution with a free biquaternion weight, which is what a plane wave is. The charge density of a general field is exactly additive over the four coefficients with the same sign for all; the spatial current is not, since a vector coefficient's two transverse slots carry the opposite sign and the mixed terms between two coefficients do not cancel. The companion's bilinear is therefore a current for a central field and not beyond it, and that is the sharpest thing the general case says about the scalar one: the scalar case is the polarization for which the current formula is true.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\mathbb{B}_{C}$ | Centre, $\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$; the scalar's home |
| $\mathbb{B}_{\Phi},\ \mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\tilde\nabla=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ | Biquaternionic gradient |
| $\Box=\partial^{2}/\partial R_t^{2}+\Delta=\Delta-\partial^{2}/\partial {r'_{t}}^{2}$ | d'Alembertian on the material sector |
| $r'_t=c\,t'$ | Material time, a length in the same unit as $r_\eta$ |
| $R_t=r_t+i r'_t$ | Complex time; $r_t$ informational, $r'_t$ material |
| $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position |
| $\tilde\Xi=\Xi_t e_t+\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z$ | The biquaternion Klein–Gordon field, four complex coefficients |
| $\Xi_\mu$ | The coefficient of $e_\mu$, a complex scalar; the scalar case is $\Xi_t$ alone |
| $\tilde\Xi=\Xi_t e_t$ | The scalar case: the field central, vector coefficients zero |
| $\Xi_t=\lvert\Xi_t\rvert\exp(iS_t/\hbar)$ | The polar form of the scalar case; $\lvert\Xi_t\rvert>0$ real, $S_t$ real |
| $\lvert\Xi_t\rvert$ | The amplitude, positive; the topological norm $\lvert\Xi_t\rvert=\bigl(\langle\tilde\Xi\rangle_{*}\bigr)^{1/2}$; the word's scale $r$ |
| $S_t$ | The action of $\Xi_t$, in $\mathrm{J\,s}$; defined modulo $2\pi\hbar$ |
| $\lvert\Xi_\mu\rvert,\ S_\mu$ | Amplitude and action of a general coefficient, the general case of the two rows above |
| $\theta_{\mathrm{phs}}=S_t/\hbar=\frac{k_mS_t}{mc}$ | The phase angle, a pure number defined modulo $2\pi$; the word's $\alpha$ up to the half-turn carried by the rotor |
| $\vec p=\nabla S_t,\ E=-c\,\partial S_t/\partial r'_t$ | Momentum and energy of the action |
| $\tilde P_{\Phi}=\tilde\nabla S_t=i\frac{E}{c}e_t+\vec p$ | Four-momentum as the gradient of the action |
| $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=\tilde\nabla S_t/\hbar$ | Four-wavevector |
| $k_m=mc/\hbar$ | Mass wave number |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box\lvert\Xi_t\rvert}{\lvert\Xi_t\rvert}$ | Relativistic quantum potential; central and real |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; on $\tilde\Xi$ it is $\Xi_t^{2}$ |
| $\langle\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | Hermitian norm; on $\tilde\Xi$ it is $\lvert\Xi_t\rvert^{2}$ |
| $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}$, $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$ | The polar factors; here $\lvert\Xi_t\rvert e_t$ and $e^{iS_t/\hbar}e_t$ |
| $\tilde Q=r\exp(i\alpha)\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word; here $r=\lvert\Xi_t\rvert$, $\alpha=S_t/\hbar$ up to a half-turn, $\tilde U_{\Psi,\mathrm b}=e_t$ and $\tilde u_{\mathrm r}=\pm e_t$ |
| $\tilde J_{\Phi}=ic\rho_{\mathrm{chg}}\,e_t+\vec j=\frac{\lvert\Xi_t\rvert^{2}}{m}\tilde P_{\Phi}$ | Conserved four-current |
| $\tilde V_{\Phi}=\tilde P_{\Phi}/m=\tilde\nabla S_t/m$ | Four-velocity of the fluid; $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}+\hbar^{2}\Box\lvert\Xi_t\rvert/(m^{2}\lvert\Xi_t\rvert)$, so a unit timelike vector for a plane wave only |
| $\rho_{\mathrm{chg}}=\lvert\Xi_t\rvert^{2}E/(mc^{2}),\ \vec j=\lvert\Xi_t\rvert^{2}\vec p/m$ | Charge density and current density; $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ on shell, the companion's $\rho$ |
| $\rho_{\mathrm{num}}=\lvert\Xi_t\rvert^{2}$ | Proper density, the coefficient in $\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}$ |
| $\Xi_{\mathrm{amp}}$ | Complex constant amplitude of the plane wave $\Xi_t=\Xi_{\mathrm{amp}}\exp(i\,\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^{\natural}))$ |
| $\tilde A$ | Arbitrary constant biquaternion amplitude of a general plane wave, $\tilde\Xi=\tilde A\exp(i\,\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^{\natural}))$ |
| $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J_{\Phi})=0$ | Conservation; identical to the transport equation |
| $\sigma,\ T_{\mathrm{kin}}=-c\,\partial\sigma/\partial r'_t$ | Envelope action and kinetic energy; $S_t=-mc\,r'_t+\sigma$, $E=mc^{2}+T_{\mathrm{kin}}$ |
| $f=\exp(-ik_m r'_t)$ | The rest-mass phase divided out by the companion |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the transformation of the Schrödinger equation into a continuity equation and a Hamilton–Jacobi equation, which is the non-relativistic case of the pair derived here.
- Louis de Broglie, *La mécanique ondulatoire* (Gauthier-Villars, 1930), and *Une tentative d'interprétation causale et non linéaire de la mécanique ondulatoire* (Gauthier-Villars, 1956), for the phase as the action and the trajectory reading of the phase gradient.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the trajectories it defines.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the hydrodynamical formulation in the non-relativistic case, which is Madelung's pair read as a fluid.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the relativistic polar variables. The spin-$\tfrac12$ field carries there the eight-parameter word that this article finds degenerate, and the spin-$0$ case of the same programme is the pair derived here.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the relativistic quantum potential, its non-locality, and the difficulty with the speed of light recorded in §*Open Questions*.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Klein–Gordon equation, its current and its two defects.
- The companion articles: [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the complex form, its current, its two defects and the conjugate pair; [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), for the stress of the same polar variables; [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the phase around a node; [The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form](the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.html), for the non-relativistic pair; [Relativistic Mechanics from the Dirac Wave](relativistic-mechanics-from-the-dirac-wave.html), for the phase as the action and its subscript; [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html), for the cone as the nodal set; [The Polar Form of the Dirac Equation in Biquaternionic Form](the-polar-form-of-the-dirac-equation-in-biquaternionic-form.html), for the case in which the frame does not degenerate and the algebra's bilinear is shown not to be the current; and [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its domain.
