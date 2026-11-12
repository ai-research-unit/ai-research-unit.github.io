# __The Klein–Gordon Equation in Biquaternionic Polar Variables__

## Introduction

This article writes the biquaternionic Klein–Gordon equation in the polar variables of the $N$-regular element. On the central class the word collapses to a scale, an angle and a sign, and the equation separates into two exact real equations: a relativistic continuity equation for $\rho_{\mathrm{num}}=r^{2}$ and a relativistic quantum Hamilton–Jacobi equation with quantum potential $Q_{\mathrm{qnt}}=-\hbar^{2}\Box r/(2mr)$. The pair is the relativistic Madelung fluid, exact and not an approximation, away from the nodal set. The reading is explicit: the density is $\rho_{\mathrm{num}}=r^{2}$, the four-velocity is the phase gradient over the mass, $\tilde V_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi}/m$, the flow is irrotational off the nodes, and the quantum potential is the logarithmic curvature of that density, so it depends on the density and not on the phase. That fluid is Takabayasi's spin-$0$ quantum fluid, and it is the relativistic analogue of Madelung's pair. The general solution in free space is the Fourier superposition of plane-wave modes, and the word re-reads each mode.

The Klein–Gordon equation of this corpus is one element of $\mathbb{B}$ acted on by the algebra's own d'Alembertian. *The Klein–Gordon Equation in Biquaternionic Form* writes it as

$$
\left(\Box-k_m^{2}\right)\tilde\Xi=0,
\qquad
\tilde\Xi=\Xi_t e_t+\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z,
$$

and $\Box$ is central with real coefficients, so the one biquaternion equation is the four complex equations $\left(\Box-k_m^{2}\right)\Xi_\mu=0$, one per coefficient.

This article substitutes a parametrisation of that one element into that one equation and reads what comes out. The parametrisation is the polar word of *The Polar Decomposition of an N-Regular Biquaternion*, in the exponential form it takes in *Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion*:

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\Rho=r\,e^{i\theta_{\mathrm{pha}}},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr).
$$

The four factors are a positive real scale, a central angle, a Hermitian positive boost and a real rotor. The word has eight real parameters against the element's eight real components, and on its domain it is a bijection: it adds no object and drops no datum. $\Rho$ is the principal square root of the quaternionic norm $N(\tilde\Xi)=\langle\tilde\Xi\rangle_{\natural}$, and $\varepsilon=\Xi_t/\Rho=\pm1$, with $\Xi_t=\mathrm{Sc}\,\tilde\Xi$ the scalar coefficient, is its branch.

**The domain is $N$-regularity.** The word is a parametrisation of the group of units, so it exists iff $N(\tilde\Xi)\neq0$ (*The Meaning of N-Regularity and Degeneracy*), and it fails on every $N$-degenerate element. On the central class the cone and the nodal set coincide.

**The scalar case comes first.** The field is taken central, $\tilde\Xi=\Xi_t e_t\in\mathbb{B}_{C}$, so that the whole field is the one complex scalar $\Xi_t$. Nothing in the equation couples $\Xi_t$ to the other three coefficients, so the restriction loses no structure. It is a choice of subject, taken because it is the case in which one scale and one angle describe the whole field. The general field is §*General Fields*.

On the scalar the word collapses. The boost has no rapidity to carry and the rotor no axis, so

$$
\boxed{\;\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\varepsilon\,e_t\;}
\qquad
\tilde U_{\Psi,\mathrm b}=e_t,\quad
\tilde u_{\mathrm r}=\varepsilon e_t,\quad
r=\bigl(\langle\tilde\Xi\rangle_{*}\bigr)^{1/2},\quad
\varepsilon=\frac{\Xi_t}{\Rho}=\pm1,
$$

with $r$ the amplitude and $\rho_{\mathrm{num}}=r^{2}$ the proper density. The angle carries the action, $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$, defined modulo $2\pi\hbar$. The action carries the subscript of the field it belongs to, as in *Relativistic Mechanics from the Dirac Wave*, because the corpus's spin $\tilde S_{\Psi,\eta}$ stands on the bare letter.

Substituting this word into $\left(\Box-k_m^{2}\right)\Xi_t=0$ and separating real from imaginary parts replaces one complex equation by two real equations. That is the whole of the construction, and the two equations are exact: no term is dropped and no order is taken.

**The pair is known, and the article's work is to read it in the algebra's letters.** The two equations are Takabayasi's relativistic hydrodynamics of a spin-$0$ quantum fluid, and their non-relativistic limit is Madelung's pair as the WKB article writes it. Three statements about them are established below.

**The mass shell carries a quantum term.** The amplitude equation is the mass shell with the mass term shifted by the curvature of the amplitude, and the shift is the term that the companion's boxed dispersion relation leaves implicit.

**The companion's box is the constant-amplitude case.** $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ holds when $\Box r=0$, and a general wave adds one term to it.

**The two defects are one mechanism.** The current is $\tilde J_{\Phi}=(\rho_{\mathrm{num}}/m)\tilde P_{\Phi}$ with $\rho_{\mathrm{num}}>0$, so the sign of the charge is the sign of the energy and the amplitude carries neither.

The sections follow that order: the field and its word, the equation in polar variables, the momentum and the current, the non-relativistic limit, the general field, and what the word does and does not add.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $\mathbb{B}_{C}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ is the centre; $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ are the anti-Hermitian and Hermitian fixed subspaces. The gradient is $\tilde\nabla=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$, and $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$, with $\partial^{2}/\partial R_t^{2}=-\partial^{2}/\partial {r'_{t}}^{2}$ on the material sector, so that on that sector $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ in one length unit. The four-position is $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, the four-wavevector is $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$, and the mass wave number is $k_m=mc/\hbar$. The amplitude–phase decomposition and the quantum potential are those of *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form*, and the phase gradient as the four-momentum is that of *Relativistic Mechanics from the Dirac Wave*. Every symbol is defined where it first appears, and §*Summary of Notation* collects the letters with their domains.

## The Field and Its Word

### The collapse of the word

The word is the boxed form of the introduction. On a central field two of its four factors have no data to carry: the boost has neither rapidity nor axis, so it is $e_t$, and the rotor has neither angle nor axis, so it is the sign $\varepsilon e_t$ that the branch of the modulus deposits. The two factors that survive are the scale $r$ and the angle $\theta_{\mathrm{pha}}$, and both are central, so both commute with everything in the algebra. The symbol $\Xi_t$ stays available for the coefficient, and on the centre it is the product of the two, $\Xi_t=r e^{i\theta_{\mathrm{pha}}}$. The two real functions $(r,\theta_{\mathrm{pha}})$ and the one complex function $\Xi_t$ carry the same information.

The angle carries the action, $\theta_{\mathrm{pha}}=S_{\tilde\Xi}/\hbar$, so $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ is real and $\exp(i\theta_{\mathrm{pha}})$ has modulus one.

**The sign is data and not a redundancy.** $\Rho$ is the principal square root of $N=\Xi_t^{2}$ and $\varepsilon=\Xi_t/\Rho=\pm1$ is its branch, so the angle of the word runs over a half-turn and the rotor's sign carries the other half. The pair $(r,\theta_{\mathrm{pha}},\varepsilon)$ is a bijection onto the nonzero complex scalars, and the three letters are read from the scalar and never chosen.

**The action is defined modulo $2\pi\hbar$.** A shift of the angle by a full turn leaves the field unchanged and leaves every observable below unchanged, so the action is a coordinate of the field and not a property of it. The field carries three real parameters, the scale, the angle modulo the turn and the sign, and that is the count of the one nonzero complex coefficient it replaces.

### Where the Word Ends: the Nodal Set Is the Cone

The form needs $r>0$. On the centre the quaternionic norm of the element is the square of the coefficient, $\langle\tilde\Xi\rangle_{\natural}=\Xi_t^{2}$, so the two vanishing conditions coincide:

$$
r=0
\qquad\Longleftrightarrow\qquad
\langle\tilde\Xi\rangle_{\natural}=0 .
$$

The locus where the word fails is therefore the locus where the field meets the zero-divisor cone, and for a central field that locus is the nodal set of the wave.

The failure costs nothing observable. $S_{\tilde\Xi}$ is undefined at a node because the phase of zero is undefined, and the current $\tilde J_{\Phi}$ vanishes there. What is lost is the differentiability of $S_{\tilde\Xi}$, and that is why the transport equation below is written on the products $\rho_{\mathrm{num}}\partial S_{\tilde\Xi}/\partial r'_t$ and $\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}$, which stay differentiable where $S_{\tilde\Xi}$ does not.

**The equivalence is a property of the central field.** For a general field the condition on the element is $\langle\tilde\Xi\rangle_{\natural}\neq0$ and the condition on a coefficient is $\Xi_\mu\neq0$, and the second is the weaker. The element $e_t+i\vec e_x$ is on the cone although both of its coefficients are nonzero, as §*General Fields* shows. For a scalar the form ends exactly at the nodes; for a general field it ends on a larger set.

### The half turn, and the modulus

**The angle of the word and the angle of the coefficient.** The word keeps $\theta_{\mathrm{pha}}$ in $(-\pi/2,\pi/2]$ and deposits the excess in the sign of the rotor, so the angle of the coefficient, $\arg\Xi_t$, runs over $(-\pi,\pi]$ and the two agree up to $\varepsilon$: $\arg\Xi_t=\theta_{\mathrm{pha}}$ when $\varepsilon=+1$ and $\arg\Xi_t=\theta_{\mathrm{pha}}+\pi$ when $\varepsilon=-1$. The half turn is invisible to $r$, to $\partial S_{\tilde\Xi}/\partial r'_t$, to $\nabla S_{\tilde\Xi}$ and to every observable below. It is a statement about the range of the word's angle and not about the field.

**The amplitude is not the polar modulus.** The polar modulus is the principal square root of $\langle\tilde\Xi\rangle_{\natural}$, which is complex, and on the centre $\lvert\Rho\rvert=r$. The four norms and their collapse on the centre are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, and the distinction matters here only at the nodes, where both vanish.

## The Equation in Polar Variables

### The identity

The d'Alembertian of the word separates into a real and an imaginary part with no remainder, because the amplitude and the action are real and the exponential is central. With $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ on the material sector,

$$
\Box_\Phi\!\left(r e^{i\theta_{\mathrm{pha}}}\right)
=e^{i\theta_{\mathrm{pha}}}\left\{\Box_\Phi r+\frac{r}{\hbar^{2}}\left[\left(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}\right]+\frac{i}{\hbar}\left[\frac{1}{r}\nabla\cdot\!\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{1}{r}\frac{\partial}{\partial r'_t}\!\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)\right]\right\}.
$$

The first two terms are real and the third is purely imaginary. The verification is one differentiation of a product: each derivative of the field returns a real term, an imaginary term and a cross term carrying both functions once, and the temporal second derivative enters with the sign that $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ gives it.

Dividing by $r e^{i\theta_{\mathrm{pha}}}$ and using $\hbar k_m=mc$, the equation $\left(\Box-k_m^{2}\right)\Xi_t=0$ becomes the pair

$$
\boxed{\;\left(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r}\;}
\qquad
\boxed{\;\nabla\cdot\!\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{\partial}{\partial r'_t}\!\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)=0\;}
$$

The first is the amplitude equation and the second is the transport equation. Together they are equivalent to the Klein–Gordon equation for a field of this form, and the equivalence runs both ways: every solution of the pair gives a solution of the equation through the boxed form, and every solution of the equation that is nowhere zero gives a solution of the pair. At a node the pair still holds, with the action undefined and the products finite.

**One length unit, and no setting of $c=1$.** Both equations are written with the temporal derivative $\partial/\partial r'_t$, with no $c$ beside it and no factor $c^{-2}$ on the temporal term. That is the coordinate $r'_t=c\,t'$ doing the conversion once, in the definition of $\Box$, and it is not a choice of units made at the level of the equation.

### The amplitude equation

Read the phase gradient as the four-momentum. The corpus's momentum is $\tilde P_{\Phi}=i(E/c)e_t+\vec p$, with $\vec p=\nabla S_{\tilde\Xi}$ and

$$
E=-c\,\frac{\partial S_{\tilde\Xi}}{\partial r'_t},
$$

the factor $c$ being the algebra's own: the temporal slot of $\tilde\nabla_\Phi S_{\tilde\Xi}$ is $-i\partial S_{\tilde\Xi}/\partial r'_t$ and the temporal slot of $\tilde P_{\Phi}$ is $iE/c$. Substituting the two readings into the amplitude equation,

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box r}{r},
$$

which is the mass shell with the mass term shifted by the quantum potential. The shift is the only place the amplitude enters, and it enters as a curvature: $Q_{\mathrm{qnt}}$ is the d'Alembertian of the amplitude divided by the amplitude.

**The companion's dispersion relation, and its remainder.** Dividing by $\hbar^{2}$ and multiplying by $-1$ puts the same statement on the four-wavevector,

$$
\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}+\frac{\Box r}{r},
$$

which is the companion's $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ with one term added. The added term vanishes exactly when $\Box r=0$: a plane wave of constant amplitude satisfies that, and a wave packet, a bound state, or any field whose amplitude is not annihilated by $\Box$ does not.

**The quantum potential is the WKB one with the Laplacian promoted.** The WKB article writes $Q=-\frac{\hbar^{2}}{2\,m}\frac{\nabla^{2}A}{A}$ for the stationary state, with $A$ its real amplitude and $\nabla^{2}$ the Laplacian. Since $mc^{2}/(2k_m^{2})=\hbar^{2}/(2m)$, the coefficient is the same and $\Box$ replaces the Laplacian: $Q_{\mathrm{qnt}}$ is the static quantum potential with the second derivative taken in four coordinates instead of three. The term appears only because the operator is second order: a first-order operator applied to $r e^{i\theta_{\mathrm{pha}}}$ returns one derivative of the amplitude and no curvature, which is why the polar form of the Dirac wave stops at the eikonal and the four-momentum (*Relativistic Mechanics from the Dirac Wave*).

### The quantum potential depends on the density alone

The bracket $\Box r/r$ carries the amplitude and its second derivatives, so $Q_{\mathrm{qnt}}$ appears to need the amplitude rather than the density. It does not. With $u=\ln r$,

$$
\Box_\Phi e^{u}=e^{u}\left(\Box_\Phi u+(\partial u)^{2}\right),
\qquad
(\partial u)^{2}=\lvert\nabla u\rvert^{2}-\left(\frac{\partial u}{\partial r'_t}\right)^{2},
$$

so that $\Box r/r=\Box u+(\partial u)^{2}$, and with $u=\tfrac12\ln\rho_{\mathrm{num}}$,

$$
\boxed{\;Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\left[\frac{1}{2}\Box\ln\rho_{\mathrm{num}}+\frac{1}{4}\left(\partial\ln\rho_{\mathrm{num}}\right)^{2}\right]\;}
$$

The quantum potential is a functional of the density and of nothing else. The density is unchanged when the central phase is shifted, so $Q_{\mathrm{qnt}}$ is defined without reference to the phase. The bracket separates as well: its first term is the d'Alembertian of the logarithm of the density, and its second is the squared gradient of that logarithm, whose spatial part enters with $+$ and whose temporal part enters with $-$ because $\Box$ is a d'Alembertian and not a Laplacian.

The identity is not an accident of the logarithm. It states that $Q_{\mathrm{qnt}}$ is the curvature of the density on a logarithmic scale, so it is large where the density varies rapidly in proportion to itself, small where the density is nearly flat, and small for a wave packet whose envelope is broad compared with $\hbar/(mc)$. Everywhere else in the pair $\hbar$ is absorbed into the angle, into $\tilde K_{\Phi}$ and into $k_m$; in $Q_{\mathrm{qnt}}$ it stays, because $Q_{\mathrm{qnt}}$ compares a quantum curvature with a rest energy.

### The transport equation

The second equation is a conservation law in divergence form. Dividing by $m$ and reading the two derivatives as the density and the current of §*The Momentum and the Current*, it is $c\,\partial\rho_{\mathrm{chg}}/\partial r'_t+\nabla\cdot\vec j=0$, which is the continuity equation of the four-current in the companion's own form.

For a plane wave the equation is satisfied identically, since the amplitude is constant and the action is linear. For a general wave it constrains the pair, and it is the equation that fixes the amplitude once the action is given, or the action once the amplitude is given. The two equations are not independent: each contains both functions. The amplitude equation carries the second derivatives of the amplitude and the squared gradient of the action; the transport equation is first order in each and carries them only through the products $\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}$ and $\rho_{\mathrm{num}}\partial S_{\tilde\Xi}/\partial r'_t$.

**The divergence form is what the real amplitude buys.** With a complex amplitude the same separation leaves a source term in the transport equation, proportional to the imaginary part of the logarithm of the amplitude, and the conservation law reads as a production law. The gauge $r>0$ real is the choice that removes it.

## The Momentum and the Current

### The phase gradient is the four-momentum

The biquaternionic gradient of the action is the four-momentum. Since $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$ on the material sector,

$$
\tilde\nabla_\Phi S_{\tilde\Xi}
=e_t\,\frac{\partial S_{\tilde\Xi}}{\partial R_t}+\sum_\eta\vec e_\eta\,\frac{\partial S_{\tilde\Xi}}{\partial R_\eta}
=-i\frac{\partial S_{\tilde\Xi}}{\partial r'_t}e_t+\nabla S_{\tilde\Xi}
=i\frac{E}{c}e_t+\vec p
=\tilde P_{\Phi}.
$$

The two spellings match slot by slot, and that is where the factor $c$ in $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ comes from. Also $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=\tilde\nabla_\Phi S_{\tilde\Xi}/\hbar$, and the amplitude equation of the previous section is the quaternionic norm of that gradient with the quantum term added. This is the algebraic content of the statement that the phase is the action: the four-momentum is not read off the phase by a rule, it is the algebra's derivative of it.

### The current is the density times the four-velocity

The companion's current for a central field is $\tilde J_{\Phi}=ic\rho_{\mathrm{chg}}\,e_t+\vec j$ with

$$
\rho_{\mathrm{chg}}=\frac{i}{2k_m}\left(\Xi_t^{*}\frac{\partial\Xi_t}{\partial r'_t}-\Xi_t\,\frac{\partial\Xi_t^{*}}{\partial r'_t}\right),
\qquad
\vec j=-\frac{i\,\hbar}{2\,m}\left(\Xi_t^{*}\nabla\Xi_t-\Xi_t\,\nabla\Xi_t^{*}\right).
$$

Substituting the word, $\Xi_t^{*}\partial\Xi_t/\partial r'_t-\Xi_t\,\partial\Xi_t^{*}/\partial r'_t=2i\rho_{\mathrm{num}}\partial S_{\tilde\Xi}/(\hbar\partial r'_t)$ and $\Xi_t^{*}\nabla\Xi_t-\Xi_t\,\nabla\Xi_t^{*}=2i\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}/\hbar$, so the current becomes

$$
\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}E}{mc^{2}},
\qquad
\vec j=\frac{\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}}{m},
\qquad
\boxed{\;\tilde J_{\Phi}=\frac{\rho_{\mathrm{num}}}{m}\tilde P_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}\;}
$$

**The normalisation is one chain.** With $\rho_{\mathrm{num}}=r^{2}$ and $E=-c\,\partial_{r'_t}S_{\tilde\Xi}$,

$$
j_{r'_t}=2r^{2}\frac{\partial\theta_{\mathrm{pha}}}{\partial r'_t}
=\frac{2r^{2}}{\hbar}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}
=-\frac{2r^{2}E}{\hbar c}
=-2k_m\frac{r^{2}E}{mc^{2}}
=-2k_m\,\rho_{\mathrm{chg}},
$$

so the factor $2k_m$ converts a phase rate into a charge density, and the prefactor $i/(2k_m)$ of the companion's bilinear is the inverse of it. The sign is the sign of $E$ and of nothing else.

The current is the density times the four-velocity, and the coefficient $\rho_{\mathrm{num}}/m$ is a positive real scalar. The charge density and the proper density differ by the factor $\gamma$: with $v'_t=\gamma c$ the temporal slot gives $\rho_{\mathrm{chg}}=(v'_t/c)\rho_{\mathrm{num}}=\gamma\rho_{\mathrm{num}}$, which is the conventions' $\rho_{\mathrm{chg}}=ϙ\gamma\rho_{\mathrm{num}}$ at $ϙ=1$. The two minus signs of the two conversions, the one in $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ and the one in the temporal slot of $\tilde P_{\Phi}$, cancel, so the charge density is positive exactly when the energy is.

**The check on a plane wave.** With $\Xi_t=\tilde Q_{\mathrm{amp}}\exp(-i\theta_{\mathrm{pwp}})$ for a complex constant $\tilde Q_{\mathrm{amp}}$, the amplitude is $r=\lvert\tilde Q_{\mathrm{amp}}\rvert$ and the energy is $E=\hbar\omega$, so $\rho_{\mathrm{chg}}=r^{2}\omega/(ck_m)$, which is the companion's value. The general formula reproduces it with no separate computation.

The angle is $\theta_{\mathrm{pwp}}=p\cdot x/\hbar=\omega r'_t-\vec k_\Phi\cdot\vec r$: a real four-momentum paired with a real position over $\hbar$, so the angle is real.

### Conservation is the transport equation

The companion proves that the current is conserved, in the form $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi})=0$. With the current written as in the box, the scalar part works out as

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi}\right)
=\frac{1}{m}\left[\nabla\cdot\!\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{\partial}{\partial r'_t}\!\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)\right],
$$

and the bracket is the transport equation. The conservation law and the imaginary part of the Klein–Gordon equation are therefore the same equation, not two equations that agree. The companion describes conservation as the scalar projection of a stronger biquaternion equation; the polar form says which part of that stronger equation the wave equation contains. The imaginary part is one real equation, and it is the scalar slot of $(\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi}=0$. The three vector slots are not implied: they would be three more equations for the two functions $r$ and $S_{\tilde\Xi}$, and the wave equation does not impose them.

### The two defects, and one mechanism

The parent records that $\rho_{\mathrm{chg}}$ is not positive definite, that it has the sign of the energy, and that this is a defect of the equation. The word supplies the mechanism.

The current is a positive scalar times $\tilde P_{\Phi}$, so the sign of its temporal component is the sign of the temporal component of $\tilde P_{\Phi}$. The mass shell constrains the norm of $\tilde P_{\Phi}$ and not the sign of its time part: where the quantum term is small, the constraint is $\langle\tilde P_{\Phi}\rangle_{\natural}=-m^{2}c^{2}$, a two-sheeted hyperboloid, and the two sheets are the two branches.

| branch | $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ | $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$ | amplitude $r$ |
| --- | --- | --- | --- |
| positive frequency | $>0$ | $>0$ | $>0$ |
| negative frequency | $<0$ | $<0$ | $>0$ |

So the defect is one sign and one sign only. The density is positive on both sheets; what changes sign is the energy, and with it the charge density. The quantity $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$ is the standard Klein–Gordon charge density, the one the parent writes as $\frac{i}{2k_m}\bigl(\Xi_t^{*}\partial\Xi_t/\partial r'_t-\Xi_t\,\partial\Xi_t^{*}/\partial r'_t\bigr)$; what the polar form adds is not the object but the reason it is indefinite. An antiparticle is not a separate field in these variables. It is the same amplitude squared with the action running the other way.

The transport equation cannot see the difference: it is linear in $\partial S_{\tilde\Xi}/\partial r'_t$ and in $\nabla S_{\tilde\Xi}$, hence invariant under $S_{\tilde\Xi}\to-S_{\tilde\Xi}$, and both rows of the table satisfy it with the same amplitude. That is the polar reading of the companion's statement that the second-order structure does not organize itself by the particle–antiparticle pair: the equation for the amplitude is even, and only the energy factor in $\rho_{\mathrm{chg}}$ is odd.

**The two imaginary operations, read on the action.** The companion separates multiplication by the central $i$ from complex conjugation. In these variables the first multiplies the coefficient by a quarter turn and the second reflects the action,

$$
i\,\Xi_t = r\exp\!\left(\frac{i}{\hbar}\left(S_{\tilde\Xi}+\frac{\pi\hbar}{2}\right)\right),
\qquad
\Xi_t^{*}=r\exp\!\left(-\frac{iS_{\tilde\Xi}}{\hbar}\right).
$$

Since $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$, the translation preserves the sheet of the mass shell and the reflection exchanges the sheets. The material and informational parts are the two quadratures of the one angle, $r\cos\theta_{\mathrm{pha}}$ and $r\sin\theta_{\mathrm{pha}}$, which is why multiplication by $i$ exchanges them.

### The pair is Takabayasi's system

**The identification.** The two equations are the relativistic hydrodynamics of a spin-$0$ quantum fluid, which Takabayasi wrote in the same programme as his treatment of Dirac matter: the transport equation is his continuity equation and the amplitude equation is his relativistic Hamilton–Jacobi equation with the quantum potential. Nothing in the pair is added here.

**The same pair is the fluid of a light scalar field.** In cosmology the relativistic Madelung fluid is the non-relativistic reading of a light scalar field: the density is the field's energy density, the phase gradient is its bulk momentum, and the quantum potential is the pressure that suppresses structure below the de Broglie wavelength. That is the wave (fuzzy) dark matter picture, and it is the pair derived here with $m$ the mass of the light boson. Nothing in this article depends on that application; it is the same two equations under another name.

**One density, one four-velocity.** The fluid is described by the density of its markers and by their four-velocity,

$$
\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi},
\qquad
\tilde V_{\Phi}=\frac{\tilde P_{\Phi}}{m}=\frac{\tilde\nabla_\Phi S_{\tilde\Xi}}{m},
\qquad
\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}+\frac{\hbar^{2}}{m^{2}}\frac{\Box_\Phi r}{r}.
$$

The coefficient is the proper density of the markers, and it is not the charge density, which is the temporal component. The flow follows the phase gradient, and the transport equation is the continuity equation of that density with that velocity. The norm in the same display is the mass shell read as a statement about the fluid: it is $-c^{2}$ exactly when the quantum term vanishes, so the flow is a unit timelike vector for a plane wave and not for a general wave. The fluid reading carries the same defect as the charge density and from the same cause: what fails is the on-shell condition, not the continuity equation, which holds whatever the amplitude does.

**The flow is irrotational.** The velocity is a gradient, so its vorticity vanishes wherever the action is twice differentiable,

$$
\nabla\times\vec v_{\Phi}=\frac{1}{m}\nabla\times\nabla S_{\tilde\Xi}=0 ,
$$

and the vorticity tensor vanishes for the same reason. The exception is a nodal line, around which the action is multivalued: the curl vanishes off the node and the circulation around it need not, which is the topological charge treated in *The Nodal Set and Quantized Circulation*.

**The dynamics in the algebra's letters.** The two equations are the divergence and the norm of one gradient,

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi}\right)=0,
\qquad
\langle\tilde\nabla_\Phi S_{\tilde\Xi}\rangle_{\natural}=-m^{2}c^{2}+\hbar^{2}\frac{\Box_\Phi r}{r}.
$$

The second term is the whole of the quantum content. With it the fluid is not dust; without it the pair is relativistic irrotational dust, pressureless flow along the phase gradient.

## The Non-Relativistic Limit

### The action carries the rest energy

The companion divides out the rest-mass phase $f=\exp(-i\theta_{\mathrm{rst}})$ and expands what is left. In polar variables that step is a statement about the action: it is dominated by a term linear in the material time,

$$
S_{\tilde\Xi}=-mc\,r'_t+\sigma,
\qquad
E=-c\,\frac{\partial S_{\tilde\Xi}}{\partial r'_t}=mc^{2}+T_{\mathrm{kin}},
\qquad
T_{\mathrm{kin}}=-c\,\frac{\partial\sigma}{\partial r'_t},
$$

with $\sigma$ the action of the envelope and $T_{\mathrm{kin}}$ the kinetic energy. The coefficient of $r'_t$ is $mc$ and not $mc^{2}$, because $r'_t$ is a length and $mc^{2}t'=mc\,r'_t$. Dividing out $f$ and adding the rest term to the action are one operation: the companion's $f$ is the leading term of the action, and the companion's envelope $\chi$ is $r\exp(i\theta_{\mathrm{act}}/\hbar)e_t$ in these variables.

The angle is $\theta_{\mathrm{rst}}=k_m r'_t$: the mass wave number and the real interval give a real angle.

### The quantum potential becomes the WKB one

Substituting $E=mc^{2}+T_{\mathrm{kin}}$ into the amplitude equation,

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}
\qquad\Longrightarrow\qquad
2mT_{\mathrm{kin}}+\frac{T_{\mathrm{kin}}^{2}}{c^{2}}=\lvert\vec p\rvert^{2}+2mQ_{\mathrm{qnt}} .
$$

Dropping $T_{\mathrm{kin}}^{2}/c^{2}$ and dropping $\partial^{2}r/\partial {r'_{t}}^{2}$ against $\Delta r$ in $Q_{\mathrm{qnt}}$,

$$
T_{\mathrm{kin}}=\frac{\lvert\vec p\rvert^{2}}{2m}+Q_{\mathrm{qnt}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Delta r}{r},
$$

which is the WKB article's quantum Hamilton–Jacobi equation with $V=0$: the same kinetic energy, the same $\vec p=\nabla S_{\tilde\Xi}$, and the same quantum potential. The first dropped term is of relative order $T_{\mathrm{kin}}/(2mc^{2})$ and the second of order $v^{2}/c^{2}$.

### The transport becomes the continuity equation

In the same limit the temporal term of the transport equation keeps only the large part of $\partial S_{\tilde\Xi}/\partial r'_t$, which is $-mc$:

$$
\frac{\partial}{\partial r'_t}\!\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)
\simeq-mc\,\frac{\partial\rho_{\mathrm{num}}}{\partial r'_t},
$$

so the equation becomes

$$
c\,\frac{\partial\rho_{\mathrm{num}}}{\partial r'_t}+\nabla\cdot\!\left(\rho_{\mathrm{num}}\frac{\nabla\sigma}{m}\right)=0,
$$

which is $\partial\rho_{\mathrm{num}}/\partial t'+\nabla\cdot(\rho_{\mathrm{num}}\nabla\sigma/m)=0$ once the derivative in the length is converted into a derivative in the time. This is the continuity equation for the density $\rho_{\mathrm{num}}$ with the velocity $\vec p/m$; in the rate form it carries no $c$, because it is a rate against a rate. The non-relativistic pair of the WKB article is the leading order of this pair, and the two expansions are one expansion.

## General Fields

Everything above concerns the coefficient $\Xi_t$, with the other three set to zero. This section states what happens when they are switched on, and it separates what carries over from what does not.

### The four equations are independent

Because $\Box$ is central with real coefficients, $\Box\tilde\Xi=\sum_\mu(\Box\Xi_\mu)e_\mu$, and the four units are linearly independent, so $\left(\Box-k_m^{2}\right)\tilde\Xi=0$ holds if and only if

$$
\left(\Box-k_m^{2}\right)\Xi_\mu=0
\qquad\text{for each }\mu\in\{t,x,y,z\}.
$$

No equation relates $\Xi_t$ to $\Xi_x$. The solution space is a tensor product: writing $S$ for the set of complex scalar solutions, $\{\tilde\Xi:(\Box-k_m^{2})\tilde\Xi=0\}=\mathbb{C}^{4}\otimes_{\mathbb{C}}S$, because the equation is linear with scalar coefficients and the four units are a basis. Each coefficient carries its own amplitude $\lvert\Xi_\mu\rvert>0$ and its own action $S_\mu$, and the pair of §*The Equation in Polar Variables* returns for each of them with $r$ replaced by $\lvert\Xi_\mu\rvert$ and $S_{\tilde\Xi}$ by $S_\mu$. Four complex coefficients are eight real functions, and the four complex equations are eight real equations, one pair per coefficient: nothing is missing and nothing is overdetermined.

**The four pairs share no content.** The four actions are unrelated, so the four momenta $\tilde P_{\Phi,\mu}=\tilde\nabla_\Phi S_\mu$ are unrelated, and a superposition may carry four different wavevectors. Within a single plane wave the four coefficients share one $\vec k$, because there is one phase and a phase has one gradient at each event; the four-way freedom lives in superpositions and not in modes.

### One phase, a biquaternion amplitude

There is an intermediate case between the scalar and the fully general, and it is the one a plane wave realizes. Let $\tilde Q_{\mathrm{amp}}$ be a constant biquaternion and $g$ a complex scalar function, and set $\tilde\Xi=\tilde Q_{\mathrm{amp}}g$. Because $\Box$ has real scalar coefficients and $\tilde Q_{\mathrm{amp}}$ is constant, $\Box(\tilde Q_{\mathrm{amp}}g)=\tilde Q_{\mathrm{amp}}\Box g$, so

$$
\left(\Box-k_m^{2}\right)\left(\tilde Q_{\mathrm{amp}}g\right)=\tilde Q_{\mathrm{amp}}\left(\Box-k_m^{2}\right)g .
$$

The bracket is a central element, and each coefficient of $\tilde Q_{\mathrm{amp}}$ times a central element is $Q_{\mathrm{amp},\mu}h$; since at least one $Q_{\mathrm{amp},\mu}$ is nonzero, $\tilde Q_{\mathrm{amp}}h=0$ forces $h=0$. So for $\tilde Q_{\mathrm{amp}}\neq0$ the field solves the Klein–Gordon equation if and only if $g$ does. The four coefficients are then $\Xi_\mu=Q_{\mathrm{amp},\mu}g$: proportional, with one phase $S_{\tilde\Xi}=\hbar\arg g$, one nodal set, and four complex constants that the equation never touches.

Two consequences follow. The polarization is free and unconstrained, so $\tilde Q_{\mathrm{amp}}$ is a constant of the solution and not a dynamical variable, and its four complex entries cost nothing. And the charge density is the scalar one times the Hermitian norm of the polarization,

$$
\rho_{\mathrm{chg}}=\langle\tilde Q_{\mathrm{amp}}\rangle_{*}\lvert g\rvert^{2}\frac{E}{mc^{2}},
\qquad
\langle\tilde Q_{\mathrm{amp}}\rangle_{*}=\mathrm{Sc}\!\left(\tilde Q_{\mathrm{amp}}\tilde Q_{\mathrm{amp}}^{*}\right)=\sum_{\mu}\lvert Q_{\mathrm{amp},\mu}\rvert^{2},
$$

so a general polarization enters the density through one positive number and nothing else. The scalar case is the member $\tilde Q_{\mathrm{amp}}=Q_{\mathrm{amp},t}e_t$, and the pair of §*The Equation in Polar Variables* returns unchanged on $r=\langle\tilde Q_{\mathrm{amp}}\rangle_{*}^{1/2}\lvert g\rvert$.

**A varying frame is not available.** The algebra's polar word applies to any $N$-regular element, so $\tilde\Xi=r\exp(i\theta_{\mathrm{pha}})\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ exists for a general field; but the frame rotor and the rotor are then fields, their derivatives do not vanish, and substituting the word into the Klein–Gordon equation gives eight equations for the eight real parameters, with the derivatives of the frame entering to the same order as those of the amplitude. Two parameters are what a pair can describe, so the other six have to be constants. That is the condition $\tilde\Xi=\tilde Q_{\mathrm{amp}}g$, and it is why the one-phase case is the polarized case.

### The charge density adds up, and the spatial current has two readings

One sum is exact, and the answer is not the obvious one. With $\tilde\Xi^{*}=\Xi_t^{*}e_t-\Xi_x^{*}\vec e_x-\Xi_y^{*}\vec e_y-\Xi_z^{*}\vec e_z$ and $\vec e_\eta\vec e_\eta=-e_t$, the two sign changes cancel in the scalar part, and

$$
\mathrm{Sc}\!\left(\tilde\Xi^{*}\frac{\partial\tilde\Xi}{\partial r'_t}-\tilde\Xi\,\frac{\partial\tilde\Xi^{*}}{\partial r'_t}\right)
=\sum_{\mu}\left(\Xi_\mu^{*}\frac{\partial\Xi_\mu}{\partial r'_t}-\Xi_\mu\frac{\partial\Xi_\mu^{*}}{\partial r'_t}\right).
$$

So the companion's charge density, extended to a general field, is the sum of the four component densities with the same sign for all four: a vector coefficient contributes to $\rho_{\mathrm{chg}}$ exactly as a scalar one does. The natural guess is the opposite, that a spatial coefficient enters with a minus, and it is wrong. The reason is algebraic: the Hermitian conjugate flips the sign of the three vector coefficients, and $\vec e_\eta^{2}=-e_t$ flips it back.

The extension is a reading and not a quotation. The companion defines the current for $\tilde\Xi=\Xi_t e_t\in\mathbb{B}_{C}$ and for nothing else, so the display above is the same bilinear read on a larger domain. What it shows is that the additivity of the temporal slot belongs to the bilinear and not to the central restriction, and the mechanism of §*The two defects, and one mechanism* therefore survives without the centre: the sign of the charge is the sign of the energy for each coefficient separately. Two coefficients on opposite branches carry opposite charge, so a field with $\Xi_t$ on the positive branch and $\Xi_x$ on the negative one has a density that can vanish identically without either coefficient vanishing. The vanishing of the density is then not the vanishing of the field, and it is not even a nodal condition.

**The spatial current adds up the same way.** With $\vec e_\eta^{*}=-\vec e_\eta$ and $\vec e_\eta^{2}=-e_t$, every diagonal term $\Xi_\mu^{*}\partial_\eta\Xi_\mu\,\vec e_\mu^{*}\vec e_\mu$ lands in the scalar slot with a plus, whatever $\mu$ is, and every off-diagonal term $\vec e_\mu^{*}\vec e_\nu$ with $\mu\neq\nu$ is a spatial unit and contributes nothing there. Direction by direction, the companion's $\vec j$ is therefore additive as well,

$$
\vec j=\sum_{\mu}\frac{\rho_\mu}{m}\nabla S_\mu,
\qquad
\rho_\mu=\lvert\Xi_\mu\rvert^{2},
$$

with the plus sign for all four coefficients.

**The reading that puts the current in the vector slots gives another object.** An element of $\mathbb{B}_{\Phi}$ carries its current in the vector slots and its charge in the temporal slot, and there the same product is not the one just summed: it vanishes identically for a field with one active coefficient, temporal or spatial, because $\vec e_\mu^{*}\vec e_\mu=+e_t$ sends every diagonal term to the scalar slot. What survives in the vector slots is off-diagonal. The smallest case is $\tilde\Xi=\Xi_t e_t+\Xi_x\vec e_x$ with the direction $\eta=x$,

$$
\tilde\Xi^{*}\frac{\partial\tilde\Xi}{\partial r_x}
=\Bigl[\bar\Xi_t\frac{\partial\Xi_t}{\partial r_x}+\bar\Xi_x\frac{\partial\Xi_x}{\partial r_x}\Bigr]e_t
+\Bigl[\bar\Xi_t\frac{\partial\Xi_x}{\partial r_x}-\bar\Xi_x\frac{\partial\Xi_t}{\partial r_x}\Bigr]\vec e_x .
$$

The scalar slot is the additive piece. The $\vec e_x$ slot is $2i\,\mathrm{Im}(\bar\Xi_t\,\partial_{r_x}\Xi_x)$, an interference term between the two coefficients: it vanishes when they share a phase, and it contains no term of the form $\lvert\Xi_\mu\rvert^{2}\partial_\eta S_\mu$. The vector slot measures interference and not flow.

**Which reading is the current is not decided here.** The companion's $\vec j$ is the scalar-slot coefficient of the product taken one direction at a time, which is what "for a complex scalar field" licenses and what its plane-wave value requires. The additive reading is the one that extends, and the vector-slot reading is the one that the sector membership of $\tilde J_{\Phi}$ demands; on a central field the two coincide in the temporal slot and the vector slots are empty either way. The algebra does not pick between them and the wave equation does not either, since it constrains the coefficients separately and imposes no relation that would make one reading the conserved one. §*Open Questions* records the choice as open.

### The domain is larger than the nodal set

For the scalar the form fails exactly where $r=0$. For a general field the condition for the element's word is $\langle\tilde\Xi\rangle_{\natural}\neq0$, which is strictly stronger. Take

$$
\tilde\Xi=\Xi_t\left(e_t+i\vec e_x\right),
\qquad \Xi_t\neq0 .
$$

Both coefficients are nonzero, and $\langle\tilde\Xi\rangle_{\natural}=\Xi_t^{2}+(i\Xi_t)^{2}=0$, so the element is on the zero-divisor cone: $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$. A nowhere-zero field can therefore sit on the cone, exactly as a massless Dirac solution does in §*Where the Word Ends*. The four componentwise polar forms still exist there, because each coefficient is nonzero; it is the one-phase description of the element that has no value.

## What the Polar Word Does and Does Not Add

The objection is stated first. For a scalar field the word is a change of coordinates, two real functions for one complex one, and the two equations are Madelung's pair in its relativistic form, which is the spin-$0$ case of Takabayasi's hydrodynamics. No prediction is added and the equation is not new.

Three things are nevertheless not a relabelling.

**The dispersion relation is a plane-wave statement, and the remainder is visible.** $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ holds for a plane wave and misses a general wave by $\Box r/r$. In the complex form the box is read as a statement about one wave; in these variables the same equation says which part belongs to the action and which to the amplitude.

**The two defects become one mechanism.** The sign of the charge is the sign of the energy, and the reason is that the current is the density times the four-velocity. That is one line in these variables and a computation in the others. It also says what a repair would cost: the coefficient $\rho_{\mathrm{num}}/m$ cannot be made negative without ceasing to be positive, so the sign cannot be removed by rewriting the current; only the sign of the energy can change it, and the sign of the energy is the branch.

**The stress tensor is read off the same two functions.** The density and the four-velocity are the two ingredients of the energy–momentum tensor of the scalar field, so the polar variables give it without a separate computation: the tensor is built from $\rho_{\mathrm{num}}$, $\tilde V_{\Phi}$ and $Q_{\mathrm{qnt}}$, as *The Quantum Stress Tensor of the Biquaternion Scalar Field* writes it. The fluid reading and the tensor reading are one reading in these coordinates.

**The algebra's own structure becomes legible.** The four-momentum is the gradient of the action, the mass shell is the quaternionic norm of that gradient, the transport equation is the scalar part of a divergence, and the algebra's polar word is seen to carry nothing on a spin-$0$ wave that the amplitude and the action do not already carry.

The ledger is therefore: the equation, no; the coordinates, yes. What the coordinates add is that the algebra's structure and the fluid's structure are one structure written twice.

## Open Questions

1. **The locus where the effective mass vanishes.** The amplitude equation carries $m^{2}c^{2}-\hbar^{2}\Box r/r$. That combination can vanish and can change sign on a set of events even though $m\neq0$. Whether such a locus has a physical interpretation, or is an artefact of the variables, is not settled here. The natural guess is that it is where the de Broglie wavelength of the amplitude variation reaches the Compton length, and a guess is all it is.

2. **The nodal set.** At a node the phase is undefined, the current vanishes, and the transport equation stays meaningful while the action does not. Whether the winding of the action around a nodal line carries a topological charge, and whether that charge is an object of the algebra rather than of the phase, is taken up in *The Nodal Set and Quantized Circulation*.

3. **Minimal coupling.** The current is $\rho_{\mathrm{num}}\tilde P_{\Phi}/m$, and the minimal coupling of the corpus adds a coupling times the four-potential to the four-momentum inside the equation. Whether the same replacement acts on the current, and whether $Q_{\mathrm{qnt}}$ is untouched, is a question for the coupled treatment; nothing here decides it.

4. **The current of a general field.** The bilinear that serves as the current for a central field admits two readings once the field is general: the scalar-slot coefficient of each directional product, which is additive over the four coefficients, and the vector slots of the algebra, which hold no diagonal term at all. The two readings cannot both give the conserved current of a sector-valued element. Whether the correct current is one of them, another bilinear of the even algebra, or needs the odd element as [the Dirac companion](the-dirac-equation-in-biquaternionic-polar-variables.html) argues in its §*The Bilinear That Is Not the Current*, is open. It is the first question for the general field, and nothing in the scalar case answers it.

5. **Trajectories, and the speed of light.** The amplitude equation defines trajectories by $\vec p=\nabla S_{\tilde\Xi}$, and $Q_{\mathrm{qnt}}$ enters them as a potential. Whether the resulting flow respects $c$ as a limit, and whether the relativistic polar form admits a trajectory reading at all, is the standing difficulty of the de Broglie–Bohm programme in its relativistic form. The polar variables relocate it rather than remove it.

## Summary

The scalar case comes first: the field is central and is the one complex scalar $\Xi_t$. Its word is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\varepsilon e_t$ with $r>0$ real and $S_{\tilde\Xi}$ the action, so the angle $S_{\tilde\Xi}/\hbar$ is a pure number and the amplitude squared is the proper density $\rho_{\mathrm{num}}$. Substituting this form into $\left(\Box-k_m^{2}\right)\Xi_t=0$ gives two exact real equations,

$$
\left(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r},
\qquad
\nabla\cdot\!\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{\partial}{\partial r'_t}\!\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)=0,
$$

which together are equivalent to the one complex equation. The pair is Takabayasi's relativistic hydrodynamics of a spin-$0$ fluid, written in the one length unit of the material sector. In the momentum variables $\vec p=\nabla S_{\tilde\Xi}$ and $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ the first reads $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$, and the second is the exact relativistic analogue of the WKB transport equation. The pair reduces to the WKB pair when the action is dominated by its rest term $-mc\,r'_t$ and $\Box r$ is replaced by $\Delta r$. The quantum potential is the logarithmic curvature of the density, so it is a functional of $\rho_{\mathrm{num}}$ alone.

The phase gradient is the four-momentum, $\tilde P_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi}$, and in polar variables the quaternionic norm of a gradient reads $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}+\Box r/r$. The boxed dispersion relation of the companion is the case $\Box r=0$, which a plane wave satisfies and a general wave does not.

The current is $\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde P_{\Phi}/m$, with $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$ and $\vec j=\rho_{\mathrm{num}}\vec p/m$. Its conservation, $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi})=0$, is the transport equation and not merely consistent with it. The sign defect is the sign of the energy: the mass shell is a two-sheeted hyperboloid, the density is positive on both sheets, and the charge density changes sign because the energy does. Multiplication by the central $i$ translates the action by $\pi\hbar/2$ and preserves the sheet, while complex conjugation reflects the action and exchanges the sheets.

The algebra's polar word degenerates on a central field: the scale is the amplitude, the frame rotor is $e_t$, the rotor is $\pm e_t$, and six of the eight parameters are frozen. The form's domain is the complement of the nodal set, and for a central field the nodal set is exactly where the field meets the zero-divisor cone. That is the opposite of the Dirac case, where the cone is the massless shell and a nowhere-zero solution can lie on it.

The general field is not a harder version of this one; it is four copies of it. Because $\Box$ is central, the equation is the four equations for the coefficients, the solution space is $\mathbb{C}^{4}\otimes S$, and each coefficient carries its own pair, so eight real functions obey eight real equations with no constraint among them. A constant polarization is the intermediate case: $\tilde\Xi=\tilde Q_{\mathrm{amp}}g$ solves the equation exactly when $g$ does, the four coefficients are proportional, and the density is $\langle\tilde Q_{\mathrm{amp}}\rangle_{*}\lvert g\rvert^{2}E/(mc^{2})$, which is one scalar solution with a free biquaternion weight and is what a plane wave is. The charge density of a general field is exactly additive over the four coefficients with the same sign for all, and so is the current read one spatial direction at a time, $\vec j=\sum_\mu\rho_\mu\nabla S_\mu/m$. What fails is the reading that puts the current in the vector slots of the algebra: those slots hold no diagonal term, so that reading is empty on every field the article treats and off-diagonal on a general one. The companion's bilinear is a current for a central field, its extension rests on which reading is chosen, and that choice is open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\mathbb{B}_{C}$ | Centre, $\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$; the scalar's home |
| $\mathbb{B}_{\Phi},\ \mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\tilde\nabla=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ | Biquaternionic gradient |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ | d'Alembertian on the material sector |
| $r'_t=c\,t'$ | Material time, a length in the same unit as $r_\eta$ |
| $R_t=h_t+i r'_t$ | Complex time; $h_t$ informational, $r'_t$ material |
| $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position |
| $\tilde\Xi=\Xi_t e_t+\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z$ | The biquaternion Klein–Gordon field, four complex coefficients |
| $\Xi_\mu$ | The coefficient of $e_\mu$, a complex scalar; the scalar case is $\Xi_t$ alone |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\varepsilon e_t$ | The word of the scalar case, $r>0$ real, $\varepsilon=\pm1$, $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ real |
| $r$ | The amplitude and the word's scale, positive; the square root of the Hermitian norm, $r=\bigl(\langle\tilde\Xi\rangle_{*}\bigr)^{1/2}$ |
| $\rho_{\mathrm{num}}=r^{2}$ | Proper density; the amplitude squared, never a letter |
| $S_{\tilde\Xi}$ | The action, in $\mathrm{J\,s}$, defined modulo $2\pi\hbar$ |
| $\lvert\Xi_\mu\rvert,\ S_\mu$ | Amplitude and action of a general coefficient |
| $\theta_{\mathrm{pha}}=S_{\tilde\Xi}/\hbar$ | The phase angle, a pure number modulo $2\pi$ |
| $\vec p=\nabla S_{\tilde\Xi},\ E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ | Momentum and energy of the action |
| $\tilde P_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi}=i\frac{E}{c}e_t+\vec p$ | Four-momentum as the gradient of the action |
| $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=\tilde\nabla_\Phi S_{\tilde\Xi}/\hbar$ | Four-wavevector |
| $k_m=mc/\hbar$ | Mass wave number |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box r}{r}$ | Relativistic quantum potential; central and real |
| $u=\ln r$ | Logarithm of the amplitude; $Q_{\mathrm{qnt}}$ is read on $u$ |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; on $\tilde\Xi$ it is $\Xi_t^{2}$ |
| $\langle\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | Hermitian norm; on $\tilde\Xi$ it is $\rho_{\mathrm{num}}$ |
| $\Rho$ | Polar modulus, the principal square root of $\langle\tilde\Xi\rangle_{\natural}$; complex, with $\lvert\Rho\rvert=r$ on the centre |
| $\varepsilon=\Xi_t/\Rho=\pm1$ | Branch of the modulus; on a central field the rotor is $\varepsilon e_t$, with $\theta_{\mathrm{axr}}=0$ for $\varepsilon=+1$ and $2\pi$ for $\varepsilon=-1$ |
| $\tilde Q=r\exp(i\theta_{\mathrm{pha}})\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The algebra's polar word; on the scalar case $r$ is the amplitude, $\theta_{\mathrm{pha}}$ the angle, $\tilde U_{\Psi,\mathrm b}=e_t$ and $\tilde u_{\mathrm r}=\varepsilon e_t$ |
| $\tilde J_{\Phi}=ic\rho_{\mathrm{chg}}\,e_t+\vec j=\rho_{\mathrm{num}}\tilde V_{\Phi}$ | Conserved four-current |
| $\tilde V_{\Phi}=\tilde P_{\Phi}/m=\tilde\nabla_\Phi S_{\tilde\Xi}/m$ | Four-velocity; unit timelike for a plane wave only |
| $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2}),\ \vec j=\rho_{\mathrm{num}}\vec p/m$ | Charge density and current density; $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ on shell |
| $\rho_\mu=\lvert\Xi_\mu\rvert^{2}$ | Density of the coefficient $\Xi_\mu$; the current of a general field reads $\vec j=\sum_\mu\rho_\mu\nabla S_\mu/m$ |
| $\tilde Q_{\mathrm{amp}}$ | Constant biquaternion amplitude of a polarized wave; components $Q_{\mathrm{amp},\mu}$ |
| $g$ | The complex scalar of the polarized field $\tilde\Xi=\tilde Q_{\mathrm{amp}}g$ |
| $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi})=0$ | Conservation; identical to the transport equation |
| $\sigma,\ T_{\mathrm{kin}}=-c\,\partial\sigma/\partial r'_t$ | Envelope action and kinetic energy; $S_{\tilde\Xi}=-mc\,r'_t+\sigma$, $E=mc^{2}+T_{\mathrm{kin}}$ |
| $f=\exp(-i\theta_{\mathrm{rst}})$ | The rest-mass phase divided out by the companion |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the transformation of the Schrödinger equation into a continuity equation and a Hamilton–Jacobi equation, which is the non-relativistic case of the pair derived here.
- Louis de Broglie, *La mécanique ondulatoire* (Gauthier-Villars, 1930), and *Une tentative d'interprétation causale et non linéaire de la mécanique ondulatoire* (Gauthier-Villars, 1956), for the phase as the action and the trajectory reading of the phase gradient.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the trajectories it defines.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the hydrodynamical formulation in the non-relativistic case, which is Madelung's pair read as a fluid.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the relativistic polar variables. The spin-$\tfrac12$ field carries an eight-parameter word that is degenerate for a spin-$0$ wave, and the spin-$0$ case of the same programme is the pair derived here.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the relativistic quantum potential, its non-locality, and the difficulty with the speed of light recorded in §*Open Questions*.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Klein–Gordon equation, its current and its two defects.
- The companion articles: [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the complex form, its current, its two defects and the conjugate pair; [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), for the stress of the same polar variables; [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the phase around a node; [The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form](the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.html), for the non-relativistic pair; [Relativistic Mechanics from the Dirac Wave](relativistic-mechanics-from-the-dirac-wave.html), for the phase as the action and its subscript; [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html), for the cone as the nodal set; [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), for the case in which the frame does not degenerate and the algebra's bilinear is shown not to be the current; [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its domain; and [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the same word applied to the non-relativistic equation.
