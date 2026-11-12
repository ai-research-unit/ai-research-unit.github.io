# __The Proca Equation in Biquaternionic Polar Variables__

## Introduction

This article writes the Proca field in the polar variables of the material sector. It is the polar companion of *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, and it depends on three articles: that element form for the equation and the Lorenz condition, *The Dirac Equation in Biquaternionic Polar Variables* for the word and the logarithmic derivative, and *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector* for the carrier and its complex structure.

**The substitution is not the Schrödinger substitution.** The polar word of the scalar and spinor equations,

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

carries eight real parameters, and it is a bijection onto the N-regular set. The Proca potential is not a general element: it is an element of the material sector $\mathbb{B}_{\Phi}$, the anti-Hermitian sector, which has four real dimensions. Substituting the eight-parameter word into a four-dimensional carrier cannot be a bijection, and it is not. What survives is a two-branch word with four parameters on each branch, and the content of this article is that word, its two branches, and the equation read through it.

**Three things are established.**

*First, the word is piecewise.* The central angle $\theta_{\mathrm{pha}}$ is not a parameter of the material sector: a real four-vector has no phase to carry one. The word is the polar decomposition of a real four-vector, and its two branches are the two signs of the Minkowski form. On the timelike branch the frame is a boost and the sign of the scalar potential is a discrete label; on the spacelike branch the frame is a boost whose axis is locked to the direction of $\vec A$, and the direction replaces the rotor. The two branches are

$$
\tilde A_\Phi=\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}\quad(\langle\tilde A_\Phi\rangle_\natural<0),
\qquad
\tilde A_\Phi=r\,\tilde U_{\Psi,\mathrm b}\,\hat u\quad(\langle\tilde A_\Phi\rangle_\natural>0),
$$

with $r>0$ the modulus of the quaternionic norm, $\varepsilon=\pm1$ the sign of the scalar potential, $\tilde U_{\Psi,\mathrm b}$ the boost, and $\hat u$ a real unit vector. Each branch carries four parameters for four components, so the chart is exact and no condition is lost or added. The lightlike set $\langle\tilde A_\Phi\rangle_\natural=0$ is outside both branches: there the field is a zero divisor of $\mathbb{B}$ and has no polar reading at all.

*Second, the logarithmic derivative has two brackets and not four.* For a timelike field value

$$
\tilde A_\Phi^{-1}\frac{\partial\tilde A_\Phi}{\partial R_\mu}
=\frac{\partial\ln r}{\partial R_\mu}+\Gamma_\mu,
\qquad
\Gamma_\mu=\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu},
$$

and for a spacelike one the same expression with the frame conjugated by $\hat u$ and one term added. The central bracket of the Dirac word is absent identically in both branches, and the scalar bracket is exactly the gradient of $\ln r$. That absence is the polar form of the source article's central statement that the Proca field is real: a real four-vector has no phase to differentiate.

*Third, the equation separates into a scale equation and a transport equation.* Multiplying the Proca equation by $\tilde A_\Phi^{-1}$ and splitting into scalar and traceless parts gives

$$
\bigl(\Box_\Phi-k_m^2\bigr)r+r\sum_\mu\mathrm{Sc}\bigl(\Gamma_\mu^2\bigr)=0,
\qquad
\sum_\mu\Bigl(\frac{\partial\Gamma_\mu}{\partial R_\mu}+\Gamma_\mu^2-\mathrm{Sc}(\Gamma_\mu^2)\Bigr)+2\sum_\mu\frac{\partial\ln r}{\partial R_\mu}\Gamma_\mu=0,
$$

the second in the traceless part. The first is a Klein–Gordon equation for the scale with a source built from the frame's Maurer–Cartan form; the second is the transport of the frame. For a fixed boost axis they reduce to a pair with a conservation-law structure, $\partial_\mu(r^2\partial_\mu\theta_{\mathrm{rpd}})=0$.

**What is not available.** There is no Madelung pair, no guidance equation and no quantum potential, because there is no phase and therefore no phase gradient. The polar form of the material sector is a magnitude–direction decomposition of a real four-vector, and the Lorenz condition in these variables is one scalar equation, not the continuity equation of a fluid.

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_t=1$, $\vec e_\eta^2=-e_t$ and central scalar imaginary $i$; the sector split is $\mathbb{B}_{\Phi}=\mathrm{span}_\mathbb{R}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ (anti-Hermitian) and $\mathbb{B}_{\Psi}=\mathrm{span}_\mathbb{R}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ (Hermitian); the star conjugation is coefficient conjugation composed with the quaternion conjugation $\natural$, so that ${}^{*}$ is antilinear and $\natural$ is $\mathbb{C}$-linear; the quaternionic norm is $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$, a complex scalar that is real on $\mathbb{B}_{\Phi}$; and $\mathrm{Sc}$ is the coefficient of $e_t$. The potential is $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ with $a'_t$ and $\vec A$ real, so that

$$
\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^2+\vec A^2 ,
$$

the Minkowski square in the corpus's signature. The derivatives are $\partial/\partial R_t=-i\,\partial/\partial r'_t$ on the time slot and $\partial/\partial R_\eta=\partial/\partial r_\eta$ on the three space slots, so that $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$ as in the element form. The mass is the wave number $k_m=mc/\hbar$.

## Why the Four-Factor Word Does Not Apply

**A count first.** A general element of $\mathbb{B}$ has eight real components, and the four factors of the Schrödinger word supply exactly eight parameters: the scale, the central angle, the three of the boost (a rapidity and two angles) and the three of the rotor. That is why the Schrödinger word is a bijection. An element of $\mathbb{B}_{\Phi}$ has four real components, and the same eight parameters would be four redundant.

**The redundancy is four real conditions, and they are the easy half.** Anti-Hermiticity is the four conditions $\tilde A_\Phi^{*}=-\tilde A_\Phi$, and imposing them on the eight-parameter word leaves a four-parameter family. But on $\mathbb{B}_\Phi$ the conditions hold identically: every element $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ with real $a'_t$ and real $\vec A$ satisfies $\tilde A_\Phi^{*}=\overline{\tilde A_\Phi}^{\natural}=(-i\,a'_t+\vec A)^{\natural}=-i\,a'_t-\vec A=-\tilde A_\Phi$. So the type equation is not where the work is. The work is the **polar decomposition of a real four-vector**, and the branches of the word are the signs of its Minkowski form. Two plausible short arguments reach the branches the hard way and both are worth recording, because each fails for a reason that matters.

**First trap: the norm changes sign under multiplication by $i$.** The quaternion conjugation $\natural$ acts on the quaternion factor and leaves the central $i$ alone, $(i\tilde Q)^{\natural}=i\tilde Q^{\natural}$, so

$$
\langle i\tilde A_\Phi\rangle_\natural=i\tilde A_\Phi\,(i\tilde A_\Phi)^{\natural}=i\tilde A_\Phi\,i\tilde A_\Phi^{\natural}=i^{2}\langle\tilde A_\Phi\rangle_\natural=-\langle\tilde A_\Phi\rangle_\natural .
$$

The norm of $i\tilde A_\Phi$ is the negative of the norm of $\tilde A_\Phi$. On timelike field values, where $\langle\tilde A_\Phi\rangle_\natural=-r^{2}$, the element $i\tilde A_\Phi$ is Hermitian with norm $+r^{2}$; on spacelike ones it is Hermitian with norm $-r^{2}$. Writing $(i\tilde A_\Phi)^{\natural}=-i\tilde A_\Phi^{\natural}$ instead — the natural guess, and the wrong one — reverses the branches.

**Second trap: the rotor is unitary, not anti-Hermitian.** A real unit quaternion satisfies $\tilde u_{\mathrm r}^{*}=\overline{\tilde u_{\mathrm r}}^{\natural}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1}$, so it is unitary, neither Hermitian nor anti-Hermitian, and $\tilde u_{\mathrm r}^{*}=-\tilde u_{\mathrm r}$ only for $\tilde u_{\mathrm r}=\pm e_t$ and $\pm\hat u$. With this in hand the counting can be done honestly, and it is worse than awkward: for a generic boost and a generic rotor **no** central angle makes $e^{i\theta}\tilde U\tilde u_{\mathrm r}$ anti-Hermitian. On a sample with rapidity $0.9$ and rotor angle $0.6$ the least residual $\sup\lvert\tilde Q^{*}+\tilde Q\rvert$ over $\theta$ is $0.56$. The only rotor for which a phase works is $\pm e_t$, and then $\theta=\pm\pi/2$ exactly — the endpoints of the Schrödinger word's phase range, not interior points of it. The material sector's word is therefore a chart of its own: the timelike branch sits on the boundary of the Schrödinger phase range, and the spacelike branch is not in that range at all.

**The route that works: the Minkowski polar decomposition.** Write $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ and read it as the real four-vector $(a'_t,\vec A)$. The quaternionic norm is the Minkowski form,

$$
\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^{2}+\vec A^{2},
$$

real and indefinite, and it is the only invariant the field carries. The two branches of the word are the two signs of this form, and each branch is the polar decomposition of a real four-vector of that character.

**Timelike branch.** Let $\langle\tilde A_\Phi\rangle_\natural=-r^{2}$ with $r>0$. Then $i\tilde A_\Phi$ is Hermitian and, by the sign identity above, of norm $+r^{2}$. A Hermitian element $\tilde H=h_0+i\vec h$ has $\langle\tilde H\rangle_\natural=h_0^{2}-\vec h^{2}$, so a Hermitian element of positive norm has $\lvert h_0\rvert>\lvert\vec h\rvert$, and $\tilde H/\sqrt{\langle\tilde H\rangle_\natural}$ is Hermitian and unitary — a boost. Hence $i\tilde A_\Phi=\pm r\tilde U_{\Psi,\mathrm b}$, and

$$
\tilde A_\Phi=\mp\,i\,r\,\tilde U_{\Psi,\mathrm b}=\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b},
$$

the two signs being one pair written twice. The scalar potential is $a'_t=\varepsilon r\cosh\frac{\theta_{\mathrm{rpd}}}{2}$, so $\varepsilon=\mathrm{sign}\,a'_t$; the continuous parameters are $r$, the rapidity and the two angles of $\hat u_{\mathrm b}$, and $\varepsilon$ is a label.

**Spacelike branch.** Let $\langle\tilde A_\Phi\rangle_\natural=+r^{2}$. The first form is excluded by its norm, which is $-r^{2}$ whatever the boost, so the decomposition has to be built from the direction. Write $\tilde A_\Phi=r\tilde U\hat u$ with $\hat u$ a real unit vector. The boost of axis $\hat u$ is built from $e_t$ and $i\hat u$, both of which commute with $\hat u$, so $\tilde U\hat u=\hat u\tilde U$, and

$$
\tilde A_\Phi^{*}=\overline{\tilde A_\Phi}^{\natural}
=r\cosh\frac{\theta_{\mathrm{rpd}}}{2}\hat u^{\natural}+i\,r\sinh\frac{\theta_{\mathrm{rpd}}}{2}
=-r\cosh\frac{\theta_{\mathrm{rpd}}}{2}\hat u+i\,r\sinh\frac{\theta_{\mathrm{rpd}}}{2}
=-\tilde A_\Phi ,
$$

so the element is anti-Hermitian with no condition left over. In components,

$$
\tilde A_\Phi=r\Bigl(\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u\hat u\Bigr)
=-i\,r\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,e_t+r\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u ,
$$

so $a'_t=-r\sinh\frac{\theta_{\mathrm{rpd}}}{2}$ and $\vec A=r\cosh\frac{\theta_{\mathrm{rpd}}}{2}\hat u$. The norm is $r^{2}(\cosh^{2}-\sinh^{2})=r^{2}$, and the rapidity is signed on this branch, because $\vec A$ points along $+\hat u$ and the sign of $a'_t$ must be carried by the rapidity.

**The locking is a consequence, not an extra condition.** The axis appears in the boost as $i\hat u$ and in the field as $\hat u$; it is one vector, so the boost axis and the direction of $\vec A$ are one parameter pair and not two. That is the whole content of the locking, and it is why the spacelike branch has four parameters — $r$, one signed rapidity, two angles — and not five. Geometrically the branch is the hyperboloid $\vec A^{2}-(a'_t)^{2}=r^{2}$, which is $\mathbb{R}_{+}\times S^{2}\times\mathbb{R}$ with the coordinates $r$, $\hat u$ and the signed rapidity, and the reconstruction is everywhere smooth because a spacelike four-vector has $\vec A\neq0$.

**No third branch.** The two branches exhaust the non-null elements by the sign of the norm, and the lightlike set has no branch. A lightlike element is a zero divisor: its norm vanishes, $r=0$, and the scale degenerates. There is no limit of either branch that reaches a lightlike four-vector with a finite non-zero $r$, and the next section states this as the excluded set.

## The Word for the Material Sector

The result of the two decompositions is the word.

$$
\boxed{\;
\tilde A_\Phi=
\begin{cases}
\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}), & \langle\tilde A_\Phi\rangle_\natural=-r^2<0,\\[4pt]
r\,\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}},\hat u)\,, & \langle\tilde A_\Phi\rangle_\natural=+r^2>0,
\end{cases}
\qquad
\tilde U_{\Psi,\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u_{\mathrm b}
\;}
$$

with $r>0$, $\varepsilon=\pm1$, $\theta_{\mathrm{rpd}}\ge0$ and $\hat u_{\mathrm b}\in S^2$ on the timelike branch, and $\theta_{\mathrm{rpd}}\in\mathbb{R}$ with the axis $\hat u$ locked to the direction of $\vec A$ on the spacelike branch.

In components the two branches read

$$
\text{timelike:}\quad a'_t=\varepsilon\,r\cosh\frac{\theta_{\mathrm{rpd}}}{2},\quad \vec A=-\varepsilon\,r\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u_{\mathrm b};
$$

$$
\text{spacelike:}\quad a'_t=-r\sinh\frac{\theta_{\mathrm{rpd}}}{2},\quad \vec A=r\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u,\quad \hat u=\frac{\vec A}{\lvert\vec A\rvert}.
$$

**The count is four on each branch.** The timelike branch has $r$, the two angles of $\hat u_{\mathrm b}$, the rapidity, and the discrete $\varepsilon$: four continuous parameters and one sign, for four components with a fixed sign of the norm. The spacelike branch has $r$, the signed rapidity and the two angles of $\hat u$: four continuous parameters, no sign. The Minkowski square is $-r^2$ on the first and $+r^2$ on the second, so the two branches meet only on the light cone, which neither contains.

**Uniqueness.** On the timelike branch $r=\sqrt{-\langle\tilde A_\Phi\rangle_\natural}$ and $\varepsilon=\mathrm{sign}\,a'_t$; the boost is recovered from $\cosh\frac{\theta_{\mathrm{rpd}}}{2}=\lvert a'_t\rvert/r$ and $\sinh\frac{\theta_{\mathrm{rpd}}}{2}=\lvert\vec A\rvert/r$, and $\hat u_{\mathrm b}=-\varepsilon\vec A/\lvert\vec A\rvert$. The reconstruction fails only at $\vec A=0$, where the axis is undefined: that is the coordinate singularity of the branch, at the pure scalar-potential line, and it is a property of the chart and not of the field. On the spacelike branch $\hat u=\vec A/\lvert\vec A\rvert$ is determined by the field, and so is $r=\sqrt{\langle\tilde A_\Phi\rangle_\natural}$ and $\theta_{\mathrm{rpd}}=2\,\mathrm{arsinh}(-a'_t/r)$; the reconstruction is unique with no singularity, because a spacelike four-vector always has $\vec A\neq0$.

**Compared with the Schrödinger word, two of the four factors are gone.** A real four-vector has no phase to endow with a parameter, so the central factor has nothing to carry; and the rotor has collapsed, to a sign on the timelike branch and to the direction $\hat u$ on the spacelike one. The word has two brackets, not four, and the missing two are exactly the phase and the rotor angle. The next section proves that in the algebra, and it is the local statement of the difference.

## The Logarithmic Derivative and the Two Brackets

**The timelike branch.** Differentiate $\tilde A_\Phi=\varepsilon i r\tilde U$ and divide by $\tilde A_\Phi$. Since $\tilde A_\Phi^{-1}=(-\varepsilon i/r)\tilde U^{-1}$,

$$
\tilde A_\Phi^{-1}\frac{\partial\tilde A_\Phi}{\partial R_\mu}
=-\frac{\varepsilon i}{r}\tilde U^{-1}\,\varepsilon i\Bigl(\frac{\partial r}{\partial R_\mu}\tilde U+r\frac{\partial\tilde U}{\partial R_\mu}\Bigr)
=\frac{\partial\ln r}{\partial R_\mu}+\tilde U^{-1}\frac{\partial\tilde U}{\partial R_\mu}.
$$

Write $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$ for the frame bracket, with $\partial_\mu=\partial/\partial R_\mu$. Its decomposition is fixed by the two elementary derivatives of the boost,

$$
\Gamma_\mu=\tfrac12\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\,i\hat u_{\mathrm b}
+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,\frac{\partial\hat u_{\mathrm b}}{\partial R_\mu}
+\sinh^2\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u_{\mathrm b}\frac{\partial\hat u_{\mathrm b}}{\partial R_\mu},
$$

in which the first term is a Hermitian vector, the second is a Hermitian vector because $i$ times a real vector is Hermitian, and the third is a real vector because $\hat u_{\mathrm b}\partial_\mu\hat u_{\mathrm b}$ has no scalar part. So the frame bracket carries two types and no more, and its scalar part vanishes identically.

**The spacelike branch.** Differentiate $\tilde A_\Phi=r\tilde U\hat u$ and divide by it. Since $\tilde A_\Phi^{-1}=(1/r)\hat u^{-1}\tilde U^{-1}=-(1/r)\hat u\tilde U^{-1}$,

$$
\tilde A_\Phi^{-1}\frac{\partial\tilde A_\Phi}{\partial R_\mu}
=\frac{\partial\ln r}{\partial R_\mu}
-\hat u\,\Gamma_\mu\,\hat u-\hat u\frac{\partial\hat u}{\partial R_\mu},
$$

where the conjugation by $\hat u$ acts on the boost generator and returns a boost generator with its axis reflected, and the last term is a real vector because a unit vector field is orthogonal to its own derivative. The two identities are exact and are checked by finite differences on a smooth configuration at the level of $10^{-11}$.

**The bracket table.** The two brackets that the word carries are the scale and the frame; the two that the Dirac word carries in addition are the phase and the rotor angle. In the material sector they are as follows.

| bracket | type | timelike branch | spacelike branch |
| --- | --- | --- | --- |
| scale | real central scalar | $\partial_\mu\ln r$ | $\partial_\mu\ln r$ |
| phase | central imaginary | $0$ identically | $0$ identically |
| frame, rapidity part | Hermitian vector | $\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u_{\mathrm b}$ | $-\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u$ |
| frame, axis part | real vector | $\sinh^2\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}\partial_\mu\hat u_{\mathrm b}$ | $-\hat u\partial_\mu\hat u$ and the conjugated rapidity term |

**The absence of the central bracket is the whole difference.** In the spinor case the central bracket is the gradient of the angle and it is the guidance equation: $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$. In the material sector there is no central bracket at all, so there is no phase gradient, no guidance, and no Madelung pair. What replaces it is a direction $\hat u$ carried by the frame, and the transport of that direction is a real-vector bracket, which the spinor's rotor also has. The material sector keeps the scale, the boost and the rotor's rôle, and it loses the phase. That is the polar form of "the Proca field is real".

## The Proca Equation in Polar Variables

**The operator split.** The Proca equation of the element form is

$$
\tilde\nabla_\Phi\tilde F=k_m^2\tilde A_\Phi,
\qquad
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
$$

and on the Lorenz surface it is the componentwise Klein–Gordon equation $\Box_\Phi\tilde A_\Phi=k_m^2\tilde A_\Phi$. Substituting the timelike word and using the product rule,

$$
\Box_\Phi\tilde A_\Phi=\varepsilon i\Bigl[(\Box_\Phi r)\tilde U+2\sum_\mu\frac{\partial r}{\partial R_\mu}\frac{\partial\tilde U}{\partial R_\mu}+r\,\Box_\Phi\tilde U\Bigr],
$$

and multiplying on the left by $\tilde A_\Phi^{-1}$ gives the exact identity

$$
\tilde A_\Phi^{-1}\bigl(\Box_\Phi-k_m^2\bigr)\tilde A_\Phi
=\frac{\Box_\Phi r}{r}+2\sum_\mu\frac{\partial\ln r}{\partial R_\mu}\Gamma_\mu
+\tilde U^{-1}\Box_\Phi\tilde U-k_m^2 .
$$

The last term before the mass is a Maurer–Cartan identity, $\tilde U^{-1}\Box_\Phi\tilde U=\sum_\mu\bigl(\partial_\mu\Gamma_\mu+\Gamma_\mu^2\bigr)$, which is the statement that the frame's curvature is the derivative of its connection plus its square.

**The two equations.** Taking the scalar part, and using $\mathrm{Sc}\,\Gamma_\mu=0$ so that the cross term drops,

$$
\boxed{\;\bigl(\Box_\Phi-k_m^2\bigr)r+r\sum_\mu\mathrm{Sc}\bigl(\Gamma_\mu^2\bigr)=0\;}
$$

and taking the traceless part,

$$
\boxed{\;\sum_\mu\Bigl(\frac{\partial\Gamma_\mu}{\partial R_\mu}+\Gamma_\mu^2-\mathrm{Sc}\bigl(\Gamma_\mu^2\bigr)\Bigr)+2\sum_\mu\frac{\partial\ln r}{\partial R_\mu}\Gamma_\mu=0\;}
$$

where the second display is an equation in the traceless part of $\mathbb{B}$, that is, a Hermitian-vector equation with three real components, and the first is one real equation. Four real equations in all, for four parameters: the count is exact, and that is the sense in which the polar form of the material sector is a chart and not a reduction.

**Why the traceless equation subtracts a trace.** The Maurer–Cartan term $\sum_\mu(\partial_\mu\Gamma_\mu+\Gamma_\mu^2)$ is not traceless: its scalar part is $\sum_\mu\mathrm{Sc}(\Gamma_\mu^2)$, and that piece is already the source of the first equation. Splitting the identity into scalar and traceless parts therefore requires the subtraction, and the second display without it would carry a scalar component that duplicates the first. The cross term needs no correction, because $\mathrm{Sc}(\Gamma_\mu)=0$ identically. The two displays together are the identity, and neither alone is.

**The subtraction is empty on a fixed axis.** For $\Gamma_\mu=\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u_{\mathrm b}$ the square is $\Gamma_\mu^2=\tfrac14(\partial_\mu\theta_{\mathrm{rpd}})^{2}(i\hat u_{\mathrm b})^{2}=\tfrac14(\partial_\mu\theta_{\mathrm{rpd}})^{2}$, a central element, so $\mathrm{Sc}(\Gamma_\mu^2)=\Gamma_\mu^2$ and the subtraction removes nothing. That is why the fixed-axis reduction below is unaffected, and why a form derived only on a fixed axis cannot reveal the missing term.

**The first equation is a Klein–Gordon equation with a source.** The source is $\sum_\mu\mathrm{Sc}(\Gamma_\mu^2)$, the trace of the square of the frame's Maurer–Cartan form. It vanishes when the frame is constant, and it is positive for a pure rapidity gradient, because $\Gamma_\mu=\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u_{\mathrm b}$ gives $\Gamma_\mu^2=\tfrac14(\partial_\mu\theta_{\mathrm{rpd}})^2(i\hat u_{\mathrm b})^2=\tfrac14(\partial_\mu\theta_{\mathrm{rpd}})^2$ using $(i\hat u_{\mathrm b})^2=+e_t$. So

$$
\bigl(\Box_\Phi-k_m^2\bigr)r+\tfrac14\,r\sum_\mu\Bigl(\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\Bigr)^2=0
\qquad\text{(axis fixed)} .
$$

This is the closest analogue in this sector to the quantum potential of the scalar case: a term quadratic in the gradient of an angular parameter, added to the mass equation of the modulus. It is not the same object, because there is no phase and the term is built from the rapidity, not from the phase.

**The second equation is a transport law with a conservation form.** With the axis fixed, the frame bracket is $\Gamma_\mu=\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u_{\mathrm b}$ and $\Gamma_\mu^2$ is central, so the traceless part of the second display reduces to

$$
\tfrac12 i\hat u_{\mathrm b}\Bigl(\Box_\Phi\theta_{\mathrm{rpd}}+2\sum_\mu\frac{\partial\ln r}{\partial R_\mu}\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\Bigr)=0
\qquad\Longleftrightarrow\qquad
\sum_\mu\frac{\partial}{\partial R_\mu}\Bigl(r^2\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\Bigr)=0 .
$$

The rapidity flows with density $r^2$, and the conservation is exact. This is the polar form of the statement that the boost is the velocity: in the spinor case the velocity is the boost, $\tilde V_\Phi=ic\tilde U^{-2}$, and its transport is the third bracket; here the same object appears as a conserved flux with the modulus as its density. The identity is verified on a smooth configuration at the level of $10^{-9}$.

**The spacelike branch.** The same three steps apply with $\tilde A_\Phi=r\tilde U\hat u$, and they are longer because the direction $\hat u$ is differentiated as well as the frame. The result has the same shape: one real equation for $r$ with a source quadratic in the frame's connection, and one equation in the traceless part — three real equations — for the frame and the direction together. This article does not display the second in full; it states the structure and records the explicit form as an open item, because the branch is the one where the direction and the boost axis are locked and the two cannot be varied independently.

## The Lorenz Condition in Polar Variables

**The condition is one scalar equation.** On the timelike branch the scalar part of the conjugate gradient is

$$
S=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)=\frac{\partial a'_t}{\partial r'_t}+\nabla\cdot\vec A ,
$$

and substituting the word gives, with $c=\cosh\frac{\theta_{\mathrm{rpd}}}{2}$ and $s=\sinh\frac{\theta_{\mathrm{rpd}}}{2}$,

$$
S=\varepsilon\Bigl[c\,\frac{\partial r}{\partial r'_t}-s\,\hat u_{\mathrm b}\cdot\nabla r
+\tfrac12 rs\,\frac{\partial\theta_{\mathrm{rpd}}}{\partial r'_t}-\tfrac12 rc\,\hat u_{\mathrm b}\cdot\nabla\theta_{\mathrm{rpd}}-rs\,\nabla\cdot\hat u_{\mathrm b}\Bigr]=0 .
$$

The display is the divergence of the four-vector written in the word's variables, and nothing more: the first two terms are $\partial_{r'_t}(\varepsilon rc)$ and the last three are $-\nabla\cdot(\varepsilon rs\hat u_{\mathrm b})$. It is one equation on four parameters, and on shell it removes one of them, leaving the three polarizations of the source article's count.

**What it is not.** It is not a continuity equation and it is not a guidance equation. In the scalar Madelung case the phase equation is the continuity equation for $\rho=r^2$ and the modulus equation is the Hamilton–Jacobi equation with the quantum potential, and the pair closes because the field is one complex function. Here the field is a real four-vector: its modulus and its direction are not a complex function, the condition is a single divergence, and there is no second conserved density to pair it with. The polar form makes that explicit rather than assuming it.

**Why the condition is implied and not imposed.** The element form proves that the divergence of the Proca equation forces $S=0$, and the proof does not use the polar variables. The polar display is therefore a reading of an equation that is already there, and the count is consistent: four parameters, four field equations, one of which is the Lorenz condition and three of which are dynamical.

## Plane Waves and the Branch as a Region

**A plane wave is a constant frame.** Take $\tilde A_\Phi=\tilde A_0\cos\theta_{\mathrm{pwp}}$ with $\tilde A_0$ a constant timelike element and $\theta_{\mathrm{pwp}}=k'_t r'_t-\vec k_\Phi\cdot\vec r$. The word of the field is then

$$
r=\lvert\cos\theta_{\mathrm{pwp}}\rvert\,\sqrt{-\langle\tilde A_0\rangle_\natural},
\qquad
\tilde U_{\Psi,\mathrm b}\ \text{constant},
\qquad
\varepsilon=\mathrm{sign}\cos\theta_{\mathrm{pwp}} ,
$$

so the boost is fixed by the amplitude and the whole spacetime dependence sits in the scale. The frame bracket vanishes and the scale equation reduces to $(\Box_\Phi-k_m^2)r=0$, which the cosine satisfies on each side of a node with the dispersion relation $k'^2_t=\vec k_\Phi^2+k_m^2$. The sign $\varepsilon$ flips at every node, and it must: the four-vector reverses through zero, and the reversal is a change of branch label and not a change of direction.

**The branch is a property of the point.** For a solution, the sign of $\langle\tilde A_\Phi\rangle_\natural$ varies in spacetime, because the field's local value varies. A timelike plane wave crosses the light cone on its nodal surfaces; a field with a spacelike component crosses it on the surfaces where the local four-vector becomes null. The word is therefore piecewise in spacetime as well as in parameter space, and the two piecewiseness are the same fact read twice. The set where the chart fails is the set where the local four-vector is lightlike, and for a plane wave that set is the nodal surfaces.

**This is not the nodal set of the scalar case, and it is larger.** In the scalar case the chart fails where the complex number vanishes, $r=0$, and that is a codimension-two set in spacetime. Here the chart fails on the whole light cone of field values, which for a generic solution is a family of three-dimensional surfaces, and $r=0$ is only its corner. The material sector's polar chart is therefore more fragile than the spinor's, and the fragility is the reality of the field again: a real four-vector has a causal character, and the character can change.

## What the Polar Form Adds and What It Does Not

**Adds.**

- A word for the material sector with the exact count: four parameters for four components on each branch, so no condition, no multiplier and no constraint analysis.
- The two brackets that survive, and the proof that the central bracket is absent identically. The absence is the polar form of the reality of the field.
- The separation of the Proca equation into a scale equation with a source quadratic in the frame's connection and a transport equation for the frame, with the fixed-axis reduction to $\partial_\mu(r^2\partial_\mu\theta_{\mathrm{rpd}})=0$.
- The polar reading of the Lorenz condition as one divergence, and the reason there is no Madelung pair.
- The statement that the branch is a spacetime region for a solution, with the lightlike set of field values as the boundary of the chart.

**Does not add.**

- No new solution. The solutions are the element form's, and the plane-wave reading is a re-reading of the source's modes.
- No new prediction and no new degree of freedom. The count of three polarizations is the source's.
- No closure problem: unlike the constrained systems, the count here is exact.
- No simplification of the field equation. The Proca equation is second order in both branches, and the polar form replaces four linear equations by one real equation and one Hermitian-vector equation of three real components, both of them nonlinear in the word's parameters.

**The distinction that matters.** The spinor polar form is a chart on an eight-parameter group of units, and its four brackets are four transport laws. The material polar form is a chart on a four-parameter set, and its two brackets are one transport law and one scale. The difference in the number of brackets is the difference between a complex field and a real one, and it is not a convention.

## Open Questions

1. **The spacelike transport equation.** The explicit form of the traceless equation on the locked branch is not displayed here. It matters because the branch is the one where the field is a spacelike four-vector and the boost axis and the direction coincide; whether the transport preserves the locking, or whether the locking is compatible only with a subclass of solutions, is not settled.
2. **The crossing set.** The chart fails where the local four-vector is lightlike. What is the correct continuation across it, and does the continuation preserve the Lorentz condition? The analogous question for the scalar case is answered by the phase's winding; here there is no phase to wind.
3. **The operator setting.** This article treats the equation with a constant mass and uses the componentwise Klein–Gordon reduction, which is the operator statement. Whether the polar chart survives quantization, and how it composes with the polarization projector of the canonical quantization article, is not attempted.

## Summary

The Proca potential is an element of the material sector, and the material sector's polar word is piecewise. On timelike field values $\tilde A_\Phi=\varepsilon ir\tilde U_{\Psi,\mathrm b}$ with four parameters and a sign; on spacelike ones $\tilde A_\Phi=r\tilde U_{\Psi,\mathrm b}\hat u$ with four parameters, the boost axis locked to $\hat u$; on lightlike values there is no word. The branches are the two signs of the Minkowski form of the real four-vector, obtained by polar decomposition and not by restricting the eight-parameter Schrödinger word: no central angle makes that word anti-Hermitian except for the rotor $\pm e_t$, at the excluded endpoint of the phase range.

The logarithmic derivative is $\tilde A_\Phi^{-1}\partial_\mu\tilde A_\Phi=\partial_\mu\ln r+\Gamma_\mu$ with $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$, and the central bracket vanishes identically. The Proca equation separates into

$$
\bigl(\Box_\Phi-k_m^2\bigr)r+r\sum_\mu\mathrm{Sc}\bigl(\Gamma_\mu^2\bigr)=0,
\qquad
\sum_\mu\Bigl(\partial_\mu\Gamma_\mu+\Gamma_\mu^2-\mathrm{Sc}(\Gamma_\mu^2)\Bigr)+2\sum_\mu\partial_\mu\ln r\,\Gamma_\mu=0
$$

with the second in the traceless part; for a fixed axis they reduce to a massive scale equation with a rapidity-gradient source and to $\partial_\mu(r^2\partial_\mu\theta_{\mathrm{rpd}})=0$. The Lorenz condition is one divergence, and there is no Madelung pair because there is no phase. For a solution the branch is a spacetime region, bounded by the set where the local four-vector is lightlike.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| ${}^{*}$, ${}^{\natural}$, $\mathrm{Sc}$ | Hermitian conjugation, quaternion conjugation, scalar part |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; real on $\mathbb{B}_\Phi$ |
| $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ | Four-potential; $\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^2+\vec A^2$ |
| $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | Field-strength biquaternion |
| $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$ | d'Alembertian of the corpus |
| $\partial/\partial R_t=-i\,\partial/\partial r'_t$ | The time-slot derivative |
| $\tilde U_{\Psi,\mathrm b}$ | Boost, $\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}$ |
| $\theta_{\mathrm{rpd}}$, $\hat u_{\mathrm b}$ | Rapidity and boost axis |
| $\hat u$ | Real unit vector, the direction of $\vec A$ on the spacelike branch |
| $\varepsilon=\pm1$ | Sign of $a'_t$ on the timelike branch |
| $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$ | Frame bracket, the Maurer–Cartan form |
| $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | Lorenz scalar |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the equation, the implied Lorenz condition, and the three polarizations.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the carrier of the integer-spin representations and its complex structure.
- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), for the word, the four brackets and the logarithmic derivative.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the scalar case and the Madelung pair that this sector does not have.
- [Canonical Quantization of the Biquaternion Proca Field](canonical-quantization-of-the-biquaternion-proca-field.html), for the constraint structure and the polarization projector.
- [The Variational Principle and the Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-proca-equation-in-biquaternionic-polar-variables.html), for the action in these variables.
- [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html), for the third state and its place in the split.
- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* **7** (1936) 347–353, for the original massive vector equation.
- Erwin Madelung, "Quantentheorie in hydrodynamischer Form", *Zeitschrift für Physik* **40** (1927) 322–326, for the scalar pair that has no analogue here.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter", *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin fluid whose brackets the material sector truncates.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion realization of the even Clifford algebra and its conjugations.
