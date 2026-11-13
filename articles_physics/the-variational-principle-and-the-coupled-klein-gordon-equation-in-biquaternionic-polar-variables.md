# __The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables__

## Introduction

This article writes the action of the coupled Klein–Gordon theory in the coordinates of the polar word and varies it. It is the polar companion of *The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Form*, and it continues *The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables*, whose bracket form of the kinetic term, metric, Legendre analysis and Jacobian argument it takes over. Its subject is the one thing the coupling changes in that structure, and the one thing it leaves alone.

**The action.** With the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and the covariant bracket

$$
\mathcal A^{\mathrm{gco}}_\mu=\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi=\tilde\Xi^{-1}\partial_\mu\tilde\Xi+\frac{i\,ϙ}{\hbar}A_\mu ,
$$

the action is the free polar action with the bracket replaced:

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\Bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_\mu\bigl(\mathcal A^{\mathrm{gco}}_\mu\bigr)^{*}\Bigr]-\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\,k_m^{2}\Bigr\},
$$

summed over the four slots with the metric signs of the corpus's convention. The connection's term is additive and central, so it adds to the bracket and multiplies nothing; this is the same identity the polar companion of the element article displays, and here it is the whole of the substitution.

**Three results.**

*First, the coupling is a shift of two slots and it spares the frame.* A central scalar is either real or central imaginary in a given slot, so the connection adds to the scale bracket in the temporal slot and to the phase bracket in the three spatial ones, and it reaches neither the boost nor the rotor. For a central field the whole action becomes Madelung's with the mechanical four-momentum; for a general element the action keeps its metric and its frame, and the shift is the same shift read in the eight-parameter chart.

*Second, the Euler–Lagrange equations are the parent's with one substitution, and the rank of the kinetic matrix does not change.* The potential shifts velocities by functions and adds a term proportional to $\lvert A\rvert^{2}$ with no velocity, so the Legendre transform stays regular, no constraint appears, and no multiplier is needed — the free polar article's exact equivalence by the invertible Jacobian survives the coupling intact.

*Third, the interaction term's structure is visible in the chart and it is not the standard one-term coupling.* Expanding the kinetic term in powers of the connection gives a term linear in $A$ and a term quadratic in $A$; the quadratic term is what makes the action gauge invariant, and it is the term that a presentation writing the coupling as "current times potential" does not have. The chart exhibits the two terms separately, and §*The Action in the Chart* computes them.

**Scope and settings.** The connection is external and treated at the level of the action; the field is the scalar of the element companion. The central-field case is the Madelung variational principle with a potential, which is standard and closed. The general element is the eight-parameter chart, whose action is regular and whose equations are the Jacobian image of the element form's — also closed, because the free polar article's argument does not use the connection. What is *not* closed here is the same thing that is not closed in the free polar article: the explicit Jacobian in the general case. The article states what it computes and says so.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ central; $^{*}$ Hermitian conjugation, $^{\natural}$ quaternion conjugation; $\mathrm{Sc}$ the coefficient of $e_t$, $\mathrm{Tr}=2\,\mathrm{Sc}$; the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout. The word's parameters are $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\hat u_{\mathrm b}$, $\theta_{\mathrm{axr}}\in[0,2\pi)$, $\hat u_{\mathrm r}$, and $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ is the action. The connection is $\tilde A_\Phi=i a'_t e_t+\vec A$ with $a'_t$ and $\vec A$ real, the coupling is $ϙ$, the material time is $r'_t=c\,t'$, $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$, and $k_m=mc/\hbar$.

## The Action in the Chart

**The free bracket's four types.** The free polar article writes the kinetic term as $\mathrm{Sc}\big[\tilde\Xi^{*}\tilde\Xi\,\mathcal A_\mu\mathcal A_\mu^{*}\big]$ with $\mathcal A_\mu$ the sum of four objects: a real central scale rate, a central imaginary phase rate, a Hermitian vector conjugated by the rotor, and a real vector part. The frame density $\tilde\Xi^{*}\tilde\Xi=r^{2}\cosh\theta_{\mathrm{rpd}}$ weights the whole thing, and the resulting metric carries $\cosh\theta_{\mathrm{rpd}}$ on the four squares and $\sinh\theta_{\mathrm{rpd}}$ on the two cross terms.

**The connection's term and the slot-by-slot reading.** With $\mathcal A^{\mathrm{gco}}_\mu=\mathcal A_\mu+\frac{iϙ}{\hbar}A_\mu$ the kinetic term is the free one with

$$
\mathcal A_\mu\mathcal A_\mu^{*}\ \longmapsto\ \mathcal A_\mu\mathcal A_\mu^{*}
+\frac{i\,ϙ}{\hbar}\Bigl(A_\mu\mathcal A_\mu^{*}-\mathcal A_\mu A_\mu\Bigr)+\frac{ϙ^{2}}{\hbar^{2}}A_\mu^{2},
$$

where the cross term collects because $A_\mu$ is central and multiplies the bracket on either side. The difference $\mathcal A_\mu^{*}-\mathcal A_\mu$ is anti-Hermitian, because the conjugate of a difference is the difference of the conjugates with the sign reversed, so $i(\mathcal A_\mu^{*}-\mathcal A_\mu)$ is Hermitian and its scalar part is real; the linear term is therefore real, and it is weighted by the anti-Hermitian part of the free bracket. The quadratic term is real by inspection and carries no field derivative. So the shift is: a real linear term, weighted by the part of the bracket that changes sign under conjugation, and a real quadratic term, which is the potential squared.

**Which component of the bracket is shifted.** For a central field the anti-Hermitian part of the bracket is $2i\,\partial_\mu\theta_{\mathrm{pha}}$, the phase rate. So the linear term is $2\frac{ϙ}{\hbar}A_\mu\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\partial_\mu\theta_{\mathrm{pha}}$, the potential times the phase rate and the frame density, which is the current's slot; and in a general element the same expression holds with the phase rate replaced by the bracket's anti-Hermitian part, which also contains the boost's contribution once the rapidity is nonzero. The statement "the connection touches two of the four brackets" is a statement about the *additive* term in $\mathcal A^{\mathrm{gco}}_\mu$; the interaction is quadratic in the bracket and therefore reaches the frame through the anti-Hermitian combination, which mixes the phase rate with the rapidity. The article states both, because the distinction is the difference between $\tilde\Xi^{-1}D\tilde\Xi$ (one additive term, two types) and the Lagrangian (two terms, all types).

**Hence, slot by slot, for a central field.** Writing the central field's bracket, $\mathcal A_\mu=\partial_\mu\ln r+i\partial_\mu\theta_{\mathrm{pha}}$, the kinetic term is

$$
\mathrm{Sc}\Bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_\mu\bigl(\mathcal A^{\mathrm{gco}}_\mu\bigr)^{*}\Bigr]
=r^{2}\Bigl\lvert\partial_\mu\ln r+i\,\partial_\mu\theta_{\mathrm{pha}}+\frac{i\,ϙ}{\hbar}A_\mu\Bigr\rvert^{2},
$$

and the temporal and spatial slots read differently because $A_t=ia'_t$ is imaginary and $A_\eta$ is real:

$$
r^{2}\Bigl\lvert\partial_{r'_t}\ln r-\frac{ϙ}{\hbar}a'_t+i\,\partial_{r'_t}\theta_{\mathrm{pha}}\Bigr\rvert^{2}
\quad\text{and}\quad
r^{2}\Bigl\lvert\partial_\eta\ln r+i\Bigl(\partial_\eta\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\eta\Bigr)\Bigr\rvert^{2}.
$$

In the temporal slot the connection sits with the scale; in the spatial slots it sits with the phase. The two moduli are the same function of the *mechanical* four-momentum, and §*The Central Field* writes the action in that form.

**The action.** Collecting the four slots with their metric signs and the mass term,

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{r^{2}\Bigl[\bigl(\partial_{r'_t}\theta_{\mathrm{pha}}-\tfrac{ϙ}{\hbar}a'_t\bigr)^{2}-\bigl\lvert\nabla\theta_{\mathrm{pha}}+\tfrac{ϙ}{\hbar}\vec A\bigr\rvert^{2}\Bigr]
+\bigl(\partial_{r'_t}r\bigr)^{2}-\lvert\nabla r\rvert^{2}-k_m^{2}r^{2}\Bigr\},
$$

which is the free polar article's central action with $\partial_{r'_t}\theta_{\mathrm{pha}}\mapsto\partial_{r'_t}\theta_{\mathrm{pha}}-\frac{ϙ}{\hbar}a'_t$ and $\nabla\theta_{\mathrm{pha}}\mapsto\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$ and with the amplitude's two terms untouched. The signs of the two shifts are the metric's, and they are the same two signs the element companion records for the four-momentum shift.

**The two interaction terms, written out.** Expanding the phase's bracket,

$$
r^{2}\bigl(\partial_{r'_t}\theta_{\mathrm{pha}}\bigr)^{2}-r^{2}\bigl\lvert\nabla\theta_{\mathrm{pha}}\bigr\rvert^{2}
-\frac{2ϙ r^{2}}{\hbar}\Bigl(\partial_{r'_t}\theta_{\mathrm{pha}}\,a'_t+\nabla\theta_{\mathrm{pha}}\cdot\vec A\Bigr)
+\frac{ϙ^{2}r^{2}}{\hbar^{2}}\Bigl(\bigl(a'_t\bigr)^{2}-\lvert\vec A\rvert^{2}\Bigr),
$$

so the interaction is a term linear in the potential multiplying the free phase rate, plus a term quadratic in the potential with no phase. The first is the one a "current times potential" presentation writes; the second is the one it does not, and it is the term that makes the action invariant under $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+ϙ\Lambda/\hbar$, $A_\mu\mapsto A_\mu-\partial_\mu\Lambda$. The chart therefore shows the coupling's second order in the potential as a separate object, and the article records this as its third result.

## The Central Field

**The action.** With $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ and $\rho_{\mathrm{num}}=r^{2}$,

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{\bigl(\partial_{r'_t}r\bigr)^{2}-\lvert\nabla r\rvert^{2}
+\frac{\rho_{\mathrm{num}}}{\hbar^{2}}\Bigl[\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙ a'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\bigr\rvert^{2}\Bigr]-k_m^{2}\rho_{\mathrm{num}}\Bigr\},
$$

which is Madelung's action with the mechanical four-momentum. The free polar article cites Madelung (1927) and Takabayasi (1952) for the $\vec A=0$ case; the coupled case is the standard Madelung action of a charged scalar, and the article does not claim it as new. What the biquaternionic form supplies is the *derivation*: the action is not postulated as a hydrodynamic functional but obtained by substituting the word into the element action, so the two functions are the field's scale and the field's phase and not auxiliary variables.

**The equations.** Varying $\theta_{\mathrm{pha}}$ — equivalently $S_{\tilde\Xi}$ — gives

$$
\nabla\cdot\Bigl(\rho_{\mathrm{num}}\bigl(\nabla S_{\tilde\Xi}+ϙ\vec A\bigr)\Bigr)
-\frac{\partial}{\partial r'_t}\Bigl(\rho_{\mathrm{num}}\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙ a'_t\bigr)\Bigr)=0,
$$

which is the transport equation; varying $r$ gives

$$
\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\bigr\rvert^{2}
=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r},
$$

which is the amplitude equation. The two are the pair of the polar companion, and they are the polar companion's derivation read backwards: there they were obtained by separating the field equation's real and imaginary parts, here by varying two functions. The equivalence is exact and is the free polar article's central-field Jacobian, which is diagonal on the four parameters $(r,\theta_{\mathrm{pha}},\varepsilon)$ with $\varepsilon$ carrying no equation.

**What the sign of $\varepsilon$ does in the action.** Nothing. The central action contains $r$ and $\theta_{\mathrm{pha}}$ and no factor of $\varepsilon$, because $\varepsilon^{2}=1$ and the word's sign is absorbed by the density's square. So $\varepsilon$ is a branch label and not a dynamical variable, exactly as in the free article, and the variational principle has two equations for the two functions it can vary.

**Why the potential costs no regularity.** The kinetic matrix in $\partial_{r'_t}r$ and $\partial_{r'_t}S_{\tilde\Xi}$ is

$$
\begin{pmatrix}2&0\\[2pt]0&2\rho_{\mathrm{num}}/\hbar^{2}\end{pmatrix},
$$

up to the normalisation of the two terms, and it is invertible for $\rho_{\mathrm{num}}>0$: the connection contributes no $\partial_{r'_t}$-dependent term beyond the shift, so the rank is the free rank and the Legendre transform is the free one. This is the precise sense in which the coupling is not a constraint: it changes where the velocities are measured from, not which velocities the action contains.

## The Charge, Its Sign and Its Gauge Invariance

**The charge is the phase rate times the density.** The temporal component of the current in the chart is

$$
c\,\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}}{m}\bigl(E+ϙ c\,a'_t\bigr),
$$

with $E=-\hbar c\,\partial_{r'_t}\theta_{\mathrm{pha}}$, which is the free polar article's "charge is the phase rate times the density" with the mechanical phase rate. The article does not call $\rho_{\mathrm{num}}$ a momentum: in a second-order action the momentum conjugate to $\theta_{\mathrm{pha}}$ is proportional to $\partial_{r'_t}\theta_{\mathrm{pha}}$ and not to $r^{2}$, and the statement that the density *is* the momentum belongs to the first-order cases, where the action's kinetic term is $-\rho\dot\theta$.

**The sign.** On the negative-frequency branch $E$ is negative, the bracket can change sign where the potential is large, and the charge density follows. So the potential shifts the boundary between the two signs but does not remove the sign change; the free article's two defects are one defect, and the coupling does not address it. The positive definiteness of $\rho_{\mathrm{num}}$ is a statement about the number density and not about the charge.

**The gauge invariance.** Under $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+ϙ\Lambda/\hbar$ and $A_\mu\mapsto A_\mu-\partial_\mu\Lambda$, the bracket $\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t$ is invariant, the bracket $\nabla S_{\tilde\Xi}+ϙ\vec A$ is invariant, and the charge is invariant. The invariance is a two-line computation in the chart, and it is the same statement as the element companion's cancellation between the two terms of a bilinear. The chart's version is the sharper one for the charge, because the charge is one product and the cancellation is inside one bracket.

**What the pairing of the two branches gives.** Complex conjugation sends $\theta_{\mathrm{pha}}\to-\theta_{\mathrm{pha}}$ and leaves the connection alone; the charge changes sign and the action is unchanged, because the action is even in $\partial\theta$ except for the linear interaction term, and that term changes sign with the phase. So the conjugate branch is the antiparticle's chart, with the opposite charge and the same mass shell, and the potential's contribution to the charge reverses with it. The statement is the free article's, and the coupling's only addition is that the potential enters the charge.

## The Vorticity and the Flux

**The action's statement.** The chart's current is $\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}(\nabla S_{\tilde\Xi}+ϙ\vec A)$, and its vorticity is the curl of a gradient plus the curl of the potential. Varying the action in the phase gives the transport equation, and the transport equation is the statement that this current is divergenceless; so the action knows the current and not its curl. The curl is a consequence of the current's definition and not of the equation:

$$
\nabla\times\bigl(\nabla S_{\tilde\Xi}+ϙ\vec A\bigr)=ϙ\vec B .
$$

**The circulation.** Integrating along a closed loop,

$$
\oint\bigl(\nabla S_{\tilde\Xi}+ϙ\vec A\bigr)\cdot\mathrm{d}\vec l=2\pi\hbar\,n+ϙ\Phi_B ,
$$

with $n$ the winding of the phase and $\Phi_B$ the flux enclosed. So the mechanical circulation is quantized up to the flux, and the chart's exact statement of the Aharonov–Bohm structure is that the flux enters the phase's bookkeeping and not the field's.

**Why the action does not see it.** A circulation is a property of a closed loop and the action is a functional of functions; the loop's statement is a consequence of the phase's being single valued, which the action's variations do not test. The article states the consequence and records that it is not an equation of motion: it is a boundary condition on the phase's winding, and the free article's nodal-set structure is where it is analysed.

## The General Element

**The bracket's shift in the eight-parameter chart.** With $\mathcal A^{\mathrm{gco}}_\mu=\mathcal A_\mu+\frac{iϙ}{\hbar}A_\mu$ and $\mathcal A_\mu$ the free bracket, the action is the free polar article's

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_\mu(\mathcal A^{\mathrm{gco}}_\mu)^{*}\bigr]-k_m^{2}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\Bigr\}
$$

with the metric unchanged. The metric is unchanged because the metric is a property of the *free* bracket's coefficients in the parameter basis, and the connection's term is not a parameter derivative; it is an additive constant in the bracket, and its contribution to the action is the two terms of §*The Action in the Chart*. So the frame density, the $\cosh$ and $\sinh$ structure, the amplitude–rapidity block's unit determinant and the two cross terms are all the free article's.

**Which parameter equations are affected.** Varying the eight parameters gives eight equations: the scale's, the phase's, the rapidity's, the boost axis's two, the rotor's angle, and the rotor axis's two. The connection enters through the phase's temporal derivative and the scale's spatial derivatives, so the equations that contain those derivatives are shifted and the rest are shifted only through the potential term $-\frac{ϙ^{2}r^{2}}{\hbar^{2}}(a_{t}'^{2}-\lvert\vec A\rvert^{2})$, which is a function of the coordinates and of $r$ alone and therefore adds $\partial/\partial p$ of a known function to the right side of each.

**No constraint and no multiplier.** The free polar article's argument is that the eight parameters are coordinates on the units, that the word is a bijection with a smooth inverse, and that the Euler–Lagrange equations in the parameters are the Jacobian image of the element equation — hence exact, hence no constraint, hence no multiplier. The coupling does not touch the argument: the word is the same word, the bijection is the same bijection, and the Jacobian is the same Jacobian, because the connection enters the *action* and not the *parameterisation*. So the coupled polar variational principle is exactly as closed as the free one, and the closedness is a property of the chart and not of the dynamics.

**The Legendre transform.** The kinetic matrix in the eight velocities is the free one plus the connection's contribution, and the connection's contribution to the velocities' dependence is a shift: the $\partial_{r'_t}\theta_{\mathrm{pha}}$ terms become $\partial_{r'_t}\theta_{\mathrm{pha}}-\frac{ϙ}{\hbar}a'_t$ and the $\partial_\eta\theta_{\mathrm{pha}}$ terms $\partial_\eta\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\eta$. A shift of a velocity does not change the matrix of second derivatives, so the free article's invertibility and its "regular Legendre transform" statement survive verbatim. The only new second-derivative structure is the $\varrho^{2}A^{2}$ term, which has no velocity and contributes to the potential alone.

## What the Polar Principle Adds and What It Does Not

**Adds.**

- A derivation of the charged Madelung pair from the element action by one substitution, with the two functions identified as the field's scale and phase rather than postulated.
- The interaction's two-term structure, linear and quadratic in the potential, exhibited separately, with the quadratic term identified as the one that gauge invariance requires.
- The statement that the coupling preserves the chart's regularity: same kinetic rank, same Legendre transform, no constraint, no multiplier.
- The charge's gauge invariance as a cancellation inside one bracket, and the vorticity and circulation as consequences of the current's definition.
- The eight-parameter chart's closure carried over unchanged, with the connection shifting two slots and multiplying nothing.

**Does not add.**

- No new prediction. The equations are the element companion's, re-coordinated.
- No new solution. The pair is the standard charged Madelung pair.
- No repair of the charge's sign.
- No explicit Jacobian in the general case, which the free polar article also leaves open.
- No statement about the operator setting's renormalisation, which is the quantised scalar article's.

**The honest ledger.** For the central field the polar variational principle is Madelung's, and the coupling makes it Madelung's with a potential; that is standard and the article says so. For the general element the chart is exact and regular, the connection shifts two slots, and nothing about the closure changes — the closure was the chart's and it stays the chart's. The genuinely new content is small and precise: the two interaction terms' separation, and the observation that a velocity shift leaves the Legendre transform's rank alone, so the coupling cannot turn a regular system into a constrained one.

## Open Questions

**The explicit Jacobian with the connection.** The free polar article states the relation between the parameter equations and the four brackets and leaves the full Jacobian open. The coupling does not change the Jacobian, so the question is inherited rather than new; whether the connection's shift makes the correspondence triangular in a natural ordering — the phase's equation first, then the scale's, then the frame's — is not settled here.

**The $\varrho^{2}A^{2}$ term's role in the chart's reading.** The quadratic term is a potential and the chart's "potential" $V$ in the free article is a function of the frame; with the connection the potential acquires a term that depends on the frame only through $r^{2}$. Whether that term has a reading as an effective mass or as a refractive index in the hydrodynamic picture is not attempted.

**The operator setting.** The article treats the connection as an external field and the action as classical. In the operator setting the amplitude and the phase are fields, the quantum potential is a functional of the density, and the $\varrho^{2}A^{2}$ term's renormalisation is the quantised theory's question. Whether the chart's exactness survives there in the sense of a well-defined functional integral is the path-integral article's subject and not this one's.

## Summary

The coupled Klein–Gordon action in polar variables is the free polar action with the covariant bracket,

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_\mu(\mathcal A^{\mathrm{gco}}_\mu)^{*}\bigr]-k_m^{2}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\Bigr\},
\qquad
\mathcal A^{\mathrm{gco}}_\mu=\mathcal A_\mu+\frac{i\,ϙ}{\hbar}A_\mu .
$$

The connection's additive term is real in the temporal slot and central imaginary in the spatial ones, so it joins the scale bracket and the phase bracket and reaches neither the boost nor the rotor; the metric, the frame density and the amplitude–rapidity block are the free article's. For a central field the action is Madelung's with the mechanical four-momentum,

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{-(\partial_{r'_t}r)^{2}+\lvert\nabla r\rvert^{2}
+\frac{\rho_{\mathrm{num}}}{\hbar^{2}}\bigl[(\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t)^{2}-\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\rvert^{2}\bigr]-k_m^{2}\rho_{\mathrm{num}}\Bigr\},
$$

and its two equations are the transport equation and the amplitude equation of the polar companion. The interaction is a linear term in the potential times the free phase rate plus a quadratic term with no phase, and the quadratic term is what gauge invariance requires. The kinetic matrix's rank is unchanged, so no constraint appears and no multiplier is needed; the eight-parameter chart's exactness by the invertible Jacobian is the free article's and survives. The vorticity of the mechanical current is $ϙ\vec B$ and its circulation is $2\pi\hbar n+ϙ\Phi_B$.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word |
| $r>0$ | Scale; $\rho_{\mathrm{num}}=r^{2}$ |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Central phase; $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ |
| $\theta_{\mathrm{rpd}}\ge0$, $\hat u_{\mathrm b}$, $\theta_{\mathrm{axr}}\in[0,2\pi)$, $\hat u_{\mathrm r}$ | Frame parameters |
| $\mathcal A_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$ | The free bracket, four types |
| $\mathcal A^{\mathrm{gco}}_\mu=\mathcal A_\mu+\frac{iϙ}{\hbar}A_\mu$ | The covariant bracket |
| $r^{2}\cosh\theta_{\mathrm{rpd}}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | The frame density |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The connection; $a'_t,\vec A$ real |
| $ϙ$ | The coupling |
| $\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t$, $\nabla S_{\tilde\Xi}+ϙ\vec A$ | The mechanical four-momentum |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\Box_\Phi r/r$ | The quantum potential; unchanged |
| $\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}(\nabla S_{\tilde\Xi}+ϙ\vec A)$ | The mechanical current; $\nabla\times=\varrho\vec B$ |
| $2\pi\hbar n+ϙ\Phi_B$ | The mechanical circulation |
| $k_m=mc/\hbar$ | The mass wave number |

## Further Reading

- [The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-klein-gordon-equation-in-biquaternionic-form.html), the element form this article re-coordinatises.
- [The Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the pair, the vorticity and the flux.
- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), for the equation and the current.
- [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the free polar action, the metric and the Jacobian argument.
- [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Form](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-form.html), for the element action.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the covariant bracket and the curvature.
- [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), for the hydrodynamic reading.
- [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), for the free flow's irrotationality.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the winding and the circulation.
- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the vector case's chart.
- E. Madelung, "Quantentheorie in hydrodynamischer Form", *Zeitschrift für Physik* **40** (1927), for the pair and its variational principle.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures", *Progress of Theoretical Physics* **8** (1952), for the relativistic pair and the Lagrangian treatment.
