# __The Lagrangian and the Coupled Klein–Gordon Equation in Polar Variables__

## Introduction

This article writes the action of the coupled Klein–Gordon theory in the coordinates of the complete polar decomposition and varies it. It is the polar companion of *The Lagrangian and the Coupled Klein–Gordon Equation*, and it continues *The Lagrangian and the Klein–Gordon Equation in Polar Variables*, whose bracket form of the kinetic term, metric, Legendre analysis and Jacobian argument it takes over. Its subject is the one thing the coupling changes in that structure, and the one thing it leaves alone.

The action. With the word $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and the covariant bracket

$$
\mathcal A^{\mathrm{gco}}_{\imath}=\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde\Xi=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi+\frac{2\pi i\,ϙ}{h}A_{\imath} ,
$$

the action is the free polar action with the bracket replaced:

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\Bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_{\imath}\bigl(\mathcal A^{\mathrm{gco}}_{\imath}\bigr)^{*}\Bigr]-\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\,4\pi^{2}\nu_m^{2}\Bigr\},
$$

summed over the four slots with the metric signs of the corpus's convention. The connection's term is additive and central, so it adds to the bracket and multiplies nothing; this is the same identity the polar companion of the element article displays, and here it is the whole of the substitution.

Three results.

*First, the coupling is a shift of two slots and it spares the frame.* A central scalar is either real or central imaginary in a given slot, so the connection adds to the scale bracket in the temporal slot and to the phase bracket in the three spatial ones, and it reaches neither the boost nor the rotor. For a central field the whole action becomes Madelung's with the mechanical four-momentum; for a general element the action keeps its metric and its frame, and the shift is the same shift read in the eight-parameter chart.

*Second, the Euler–Lagrange equations are the parent's with one substitution, and the rank of the kinetic matrix does not change.* The potential shifts velocities by functions and adds a term proportional to $\lvert A\rvert^{2}$ with no velocity, so the Legendre transform stays regular, no constraint appears, and no multiplier is needed — the free polar article's exact equivalence by the invertible Jacobian survives the coupling intact.

*Third, the interaction term's structure is visible in the chart and it is not the standard one-term coupling.* Expanding the kinetic term in powers of the connection gives a term linear in $A$ and a term quadratic in $A$; the quadratic term is what makes the action gauge invariant, and it is the term that a presentation writing the coupling as "current times potential" does not have. The chart exhibits the two terms separately, and §*The Action in Polar Variables* computes them.

Scope and settings. The connection is external and treated at the level of the action; the field is the scalar of the element companion. The central-field case is the Madelung variational principle with a potential, which is standard and closed. The general element is the eight-parameter chart, whose action is regular and whose equations are the Jacobian image of the element form's — also closed, because the free polar article's argument does not use the connection. What is *not* closed here is the same thing that is not closed in the free polar article: the explicit Jacobian in the general case. The article states what it computes and says so.

The endpoint $2\pi$. At $\theta_{\mathrm{axr}}=2\pi$ the rotor is $-e_t$, so the angle's range is closed at that point. Without the endpoint the word misses every element whose rotor factor is $-e_t$, the negative real axis $-\varrho e_t$ among them.

## Conventions

The conventions are restated here so that every sign below is checkable from this page alone. $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $i$ central; $^{*}$ Hermitian conjugation, $^{\natural}$ quaternion conjugation; $\mathrm{Sc}$ the coefficient of $e_t$, ; the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout. The word's parameters are $\varrho>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\hat u_{\mathrm b}$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, $\hat u_{\mathrm r}$, and $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ is the action. The connection is $\tilde A_\Phi=i a'_t e_t+\vec A$ with $a'_t$ and $\vec A$ real, the coupling is $ϙ$, the material time is $r'_t=c\,t'$, $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$, and $\nu_m=\frac{mc}{h}$.

## The Action in Polar Variables

The free bracket's four types. The free polar article writes the kinetic term as $\mathrm{Sc}\big[\tilde\Xi^{*}\tilde\Xi\,\mathcal A_{\imath}\mathcal A_{\imath}^{*}\big]$ with $\mathcal A_{\imath}$ the sum of four objects: a real central scale rate, a central imaginary phase rate, a Hermitian vector conjugated by the rotor, and a real vector part. The frame density $\tilde\Xi^{*}\tilde\Xi=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ weights the whole thing, and the resulting metric carries $\cosh\theta_{\mathrm{rpd}}$ on the four squares and $\sinh\theta_{\mathrm{rpd}}$ on the two cross terms.

The connection's term and the slot-by-slot reading. With $\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ the kinetic term is the free one with

$$
\mathcal A_{\imath}\mathcal A_{\imath}^{*}\ \longmapsto\ \mathcal A_{\imath}\mathcal A_{\imath}^{*}
+\frac{2\pi i\,ϙ}{h}\Bigl(A_{\imath}\mathcal A_{\imath}^{*}-\mathcal A_{\imath} A_{\imath}\Bigr)+\frac{(2\pi)^{2} ϙ^{2}}{h^{2}}A_{\imath}^{2},
$$

where the cross term collects because $A_{\imath}$ is central and multiplies the bracket on either side. The difference $\mathcal A_{\imath}^{*}-\mathcal A_{\imath}$ is anti-Hermitian, because the conjugate of a difference is the difference of the conjugates with the sign reversed, so $i(\mathcal A_{\imath}^{*}-\mathcal A_{\imath})$ is Hermitian and its scalar part is real; the linear term is therefore real, and it is weighted by the anti-Hermitian part of the free bracket. The quadratic term is real by inspection and carries no field derivative. So the shift is: a real linear term, weighted by the part of the bracket that changes sign under conjugation, and a real quadratic term, which is the potential squared.

Which component of the bracket is shifted. For a central field the anti-Hermitian part of the bracket is $2i\,\partial_{\imath}\theta_{\mathrm{pha}}$, the phase rate. So the linear term is $2\frac{2\pi ϙ}{h}A_{\imath}\,\varrho^{2}\cosh\theta_{\mathrm{rpd}}\,\partial_{\imath}\theta_{\mathrm{pha}}$, the potential times the phase rate and the frame density, which is the current's slot; and in a general element the same expression holds with the phase rate replaced by the bracket's anti-Hermitian part, which also contains the boost's contribution once the rapidity is nonzero. The statement "the connection touches two of the four brackets" is a statement about the *additive* term in $\mathcal A^{\mathrm{gco}}_{\imath}$; the interaction is quadratic in the bracket and therefore reaches the frame through the anti-Hermitian combination, which mixes the phase rate with the rapidity. The article states both, because the distinction is the difference between $\tilde\Xi^{-1}D\tilde\Xi$ (one additive term, two types) and the Lagrangian (two terms, all types).

Hence, slot by slot, for a central field. Writing the central field's bracket, $\mathcal A_{\imath}=\partial_{\imath}\ln \varrho+i\partial_{\imath}\theta_{\mathrm{pha}}$, the kinetic term is

$$
\mathrm{Sc}\Bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_{\imath}\bigl(\mathcal A^{\mathrm{gco}}_{\imath}\bigr)^{*}\Bigr]
=\varrho^{2}\Bigl\lvert\partial_{\imath}\ln \varrho+i\,\partial_{\imath}\theta_{\mathrm{pha}}+\frac{2\pi i\,ϙ}{h}A_{\imath}\Bigr\rvert^{2},
$$

and the temporal and spatial slots read differently because $A_t=ia'_t$ is imaginary and $A_k$ is real:

$$
\varrho^{2}\Bigl\lvert\partial_{r'_t}\ln \varrho-\frac{2\pi ϙ}{h}a'_t+i\,\partial_{r'_t}\theta_{\mathrm{pha}}\Bigr\rvert^{2}
\quad\text{and}\quad
\varrho^{2}\Bigl\lvert\partial_k\ln \varrho+i\Bigl(\partial_k\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}A_k\Bigr)\Bigr\rvert^{2}.
$$

In the temporal slot the connection sits with the scale; in the spatial slots it sits with the phase. The two moduli are the same function of the *mechanical* four-momentum, and §*The Action in Polar Variables: The Central Field* writes the action in that form.

The action. Collecting the four slots with their metric signs and the mass term,

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\varrho^{2}\Bigl[\bigl(\partial_{r'_t}\theta_{\mathrm{pha}}-\frac{ϙ}{h}a'_t\bigr)^{2}-\bigl\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{h}\vec A\bigr\rvert^{2}\Bigr]
+\bigl(\partial_{r'_t}\varrho\bigr)^{2}-\lvert\nabla \varrho\rvert^{2}-4\pi^{2}\nu_m^{2}\varrho^{2}\Bigr\},
$$

which is the free polar article's central action with $\partial_{r'_t}\theta_{\mathrm{pha}}\mapsto\partial_{r'_t}\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}a'_t$ and $\vec\nabla_\Phi\theta_{\mathrm{pha}}\mapsto\nabla\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}\vec A$ and with the amplitude's two terms untouched. The signs of the two shifts are the metric's, and they are the same two signs the element companion records for the four-momentum shift.

The two interaction terms, written out. Expanding the phase's bracket,

$$
\varrho^{2}\bigl(\partial_{r'_t}\theta_{\mathrm{pha}}\bigr)^{2}-\varrho^{2}\bigl\lvert\nabla\theta_{\mathrm{pha}}\bigr\rvert^{2}
-\frac{2\pi 2ϙ \varrho^{2}}{h}\Bigl(\partial_{r'_t}\theta_{\mathrm{pha}}\,a'_t+\vec\nabla_\Phi\theta_{\mathrm{pha}}\cdot\vec A\Bigr)
+\frac{(2\pi)^{2} ϙ^{2}\varrho^{2}}{h^{2}}\Bigl(\bigl(a'_t\bigr)^{2}-\lvert\vec A\rvert^{2}\Bigr),
$$

so the interaction is a term linear in the potential multiplying the free phase rate, plus a term quadratic in the potential with no phase. The first is the one a "current times potential" presentation writes; the second is the one it does not, and it is the term that makes the action invariant under $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+\frac{2\pi ϙ\Lambda}{h}$, $A_{\imath}\mapsto A_{\imath}-\partial_{\imath}\Lambda$. The chart therefore shows the coupling's second order in the potential as a separate object, and the article records this as its third result.

### The General Element

The bracket's shift in the eight-parameter chart. With $\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ and $\mathcal A_{\imath}$ the free bracket, the action is the free polar article's

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_{\imath}(\mathcal A^{\mathrm{gco}}_{\imath})^{*}\bigr]-4\pi^{2}\nu_m^{2}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\Bigr\}
$$

with the metric unchanged. The metric is unchanged because the metric is a property of the *free* bracket's coefficients in the parameter basis, and the connection's term is not a parameter derivative; it is an additive constant in the bracket, and its contribution to the action is the two terms of §*The Action in Polar Variables*. So the frame density, the $\cosh$ and $\sinh$ structure, the amplitude–rapidity block's unit determinant and the two cross terms are all the free article's.

Which parameter equations are affected. Varying the eight parameters gives eight equations: the scale's, the phase's, the rapidity's, the boost axis's two, the rotor's angle, and the rotor axis's two. The connection enters through the phase's temporal derivative and the scale's spatial derivatives, so the equations that contain those derivatives are shifted and the rest are shifted only through the potential term $-\frac{(2\pi)^{2} ϙ^{2}\varrho^{2}}{h^{2}}(a_{t}'^{2}-\lvert\vec A\rvert^{2})$, which is a function of the coordinates and of $\varrho$ alone and therefore adds $\partial/\partial p$ of a known function to the right side of each.

No constraint and no multiplier. The free polar article's argument is that the eight parameters are coordinates on the invertibles, that the word is a bijection with a smooth inverse, and that the Euler–Lagrange equations in the parameters are the Jacobian image of the element equation — hence exact, hence no constraint, hence no multiplier. The coupling does not touch the argument: the word is the same word, the bijection is the same bijection, and the Jacobian is the same Jacobian, because the connection enters the *action* and not the *parameterisation*. So the coupled polar variational principle is exactly as closed as the free one, and the closedness is a property of the chart and not of the dynamics.

The Legendre transform. The kinetic matrix in the eight velocities is the free one plus the connection's contribution, and the connection's contribution to the velocities' dependence is a shift: the $\partial_{r'_t}\theta_{\mathrm{pha}}$ terms become $\partial_{r'_t}\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}a'_t$ and the $\partial_k\theta_{\mathrm{pha}}$ terms $\partial_k\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}A_k$. A shift of a velocity does not change the matrix of second derivatives, so the free article's invertibility and its "regular Legendre transform" statement survive verbatim. The only new second-derivative structure is the $\rho_{\mathrm{chg}}^{2}A^{2}$ term, which has no velocity and contributes to the potential alone.

The pairing. Inherited, and the connection is what the pairing now sees. The parent pairs with $\mathrm{Sc}(\cdot^{*}\cdot)$ and writes the matter kinetic term through the covariant derivative $\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde\Xi$. The chart rewrites $\tilde\Xi$ as a scale and a phase and the connection as its four components, and both are real variables. The density stays real, and the reason is the one the element article gives: the scalar part of a product of conjugates is real, and the covariant derivative is a sum of an ordinary derivative and a multiplication, each of which preserves that identity.

The type of the coefficient. The question moves from the mass to the connection. In the uncharged article the only coefficient is $\nu_m^{2}$ and it is real. Here the covariant derivative's bilinear must be real for *every* $\tilde\Xi$, and that is not a condition on one number: it is a condition on the four components of $\tilde\Gamma_{\imath}$, and the four brackets of *The Parameter Basis and the Four Brackets* are the list of what the condition permits.

The selection rule. Declared, and here the declaration is the interesting one. The coupled scalar has a connection and not a potential. A connection is not an object the action may exclude — it is the object the action couples to — so the selection rule has nothing to select. The rule's only worked case is the free scalar's, where the potential is a free element and the anti-Hermitian sector is excluded.

**What reality does not buy. Reality does not make the connection's equation consistent with the matter's.** Both variations come out real; neither comes out compatible. The compatibility is the article's structural consequence, and it is a statement about the two equations and not about the density's reality.

### The Central Field

The action. With $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ and $\rho_{\mathrm{num}}=\varrho^{2}$,

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{\bigl(\partial_{r'_t}\varrho\bigr)^{2}-\lvert\nabla \varrho\rvert^{2}
+\frac{(2\pi)^{2} \rho_{\mathrm{num}}}{h^{2}}\Bigl[\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙ a'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}-q\vec A\bigr\rvert^{2}\Bigr]-4\pi^{2}\nu_m^{2}\rho_{\mathrm{num}}\Bigr\},
$$

which is Madelung's action with the mechanical four-momentum. The free polar article cites Madelung (1927) and Takabayasi (1952) for the $\vec A=0$ case; the coupled case is the standard Madelung action of a charged scalar, and the article does not claim it as new. What the biquaternionic form supplies is the *derivation*: the action is not postulated as a hydrodynamic functional but obtained by substituting the word into the element action, so the two functions are the field's scale and the field's phase and not auxiliary variables.

The equations. Varying $\theta_{\mathrm{pha}}$ — equivalently $S_{\tilde\Xi}$ — gives

$$
\vec\nabla_\Phi\cdot\Bigl(\rho_{\mathrm{num}}\bigl(\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A\bigr)\Bigr)
-\frac{\partial}{\partial r'_t}\Bigl(\rho_{\mathrm{num}}\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙ a'_t\bigr)\Bigr)=0,
$$

which is the transport equation; varying $\varrho$ gives

$$
\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}-q\vec A\bigr\rvert^{2}
=m^{2}c^{2}-\frac{h^{2}}{4\pi^{2}}\frac{\Box_\Phi \varrho}{\varrho},
$$

which is the amplitude equation. The two are the pair of the polar companion, and they are the polar companion's derivation read backwards: there they were obtained by separating the field equation's real and imaginary parts, here by varying two functions. The equivalence is exact and is the free polar article's central-field Jacobian, which is diagonal on the four parameters $(\varrho,\theta_{\mathrm{pha}},\varepsilon)$ with $\varepsilon$ carrying no equation.

What the sign of $\varepsilon$ does in the action. Nothing. The central action contains $\varrho$ and $\theta_{\mathrm{pha}}$ and no factor of $\varepsilon$, because $\varepsilon^{2}=1$ and the word's sign is absorbed by the density's square. So $\varepsilon$ is a branch label and not a dynamical variable, exactly as in the free article, and the variational principle has two equations for the two functions it can vary.

Why the potential costs no regularity. The kinetic matrix in $\partial_{r'_t}\varrho$ and $\partial_{r'_t}S_{\tilde\Xi}$ is

$$
\begin{pmatrix}2&0\\[2pt]0&2\rho_{\mathrm{num}}/\frac{h^{2}}{4\pi^{2}}\end{pmatrix},
$$

up to the normalisation of the two terms, and it is invertible for $\rho_{\mathrm{num}}>0$: the connection contributes no $\partial_{r'_t}$-dependent term beyond the shift, so the rank is the free rank and the Legendre transform is the free one. This is the precise sense in which the coupling is not a constraint: it changes where the velocities are measured from, not which velocities the action contains.

## The Variation: The Euler–Lagrange Equations

Two variations of one functional. Varying the chart's action with respect to $\varrho$ and with respect to $\theta_{\mathrm{pha}}$ gives the two equations of the central field; varying the frame's angles gives the four equations of the general element; varying the connection gives the source equation. All of them are the element article's system read in the chart, because the word is a bijection on the invertibles and the Jacobian of the substitution is invertible wherever $\varrho>0$.

**The one computation that is not a transcription.** The mass term is a function of the frame and the scale, $\varrho^{2}$ times a frame factor, and its variation with respect to $\varrho$ produces the term that the free article calls the mass shell. In the coupled case that term carries the connection through the phase's rate, so the two central equations are the covariant ones and not the free ones with a renamed variable. That is the content of the section after this one, and the variation is what produces it.

The parameter basis and the four brackets. One derivative, four types. Differentiate the word and divide by it, $\tilde\Xi^{-1}\partial\tilde\Xi$, and the result is an element of the algebra like any other. Its decomposition into the four types the algebra carries is exhaustive, and each type is named for the parameter that generates it:

$$
\tilde\Xi^{-1}\partial\tilde\Xi
=\underbrace{\partial\ln\varrho}_{\text{real scalar}}
+\underbrace{i\,\partial\theta_{\mathrm{pha}}}_{\text{central imaginary}}
+\underbrace{\tfrac12\partial\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}}_{\text{Hermitian}}
+\underbrace{\tfrac12\bigl(\partial\theta_{\mathrm{axr}}\,\vec u_{\mathrm r}+\ldots\bigr)}_{\text{real vector}} .
$$

The four objects are the four brackets. They are not four new fields: each is a directional derivative of the one field, taken along one parameter and written in the type that parameter produces. The scale bracket is real, the phase bracket central imaginary, the boost bracket Hermitian with zero scalar part, and the rotor bracket a real vector; there is no fifth type and no bracket that is a mixture.

Why the pairing needs the types. The kinetic term is $\mathrm{Sc}\bigl[(\partial\tilde\Xi)^{*}\partial\tilde\Xi\bigr]$, and the scalar part of a product vanishes unless the two factors have conjugate types. Real scalar pairs with real scalar, central imaginary with central imaginary, Hermitian with Hermitian, real vector with real vector. A bracket therefore contributes to the action only through its own type, and the cross terms a naive expansion would write are zero by the algebra and not by a choice. That is the whole content of the polar action's block structure, and it is why this field's action has the metric $g_{ab}(p)$ that the summary displays.

The parameter basis is not the bracket basis. The eight parameters are coordinates; the four brackets are types. The map between them is the word's Jacobian, and it mixes: the derivative with respect to $\theta_{\mathrm{rpd}}$ carries a piece of the scale bracket as well as of the boost bracket, because $\cosh\theta_{\mathrm{rpd}}$ multiplies the phase term and $\sinh\theta_{\mathrm{rpd}}$ the cross term. The parameter equations are the same equations in a rotated basis, and calling them "the four brackets" would be an error.

What this article's field does with them. The coupled Klein–Gordon connection enters the logarithmic derivative as one additive term, $\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$, and its two slots have two different types: real in the temporal slot, central imaginary in the spatial ones. It therefore joins the scale bracket and the phase bracket and reaches neither the boost nor the rotor. That single type fact is the reason the coupling shifts the phase's gradient and nothing else, and why the frame density and the amplitude–rapidity block are the free article's, unchanged.

## The Constraints the Action Imposes: There Are None, and the Chart Adds None

The count. Two functions, the scale $\varrho$ and the phase $\theta_{\mathrm{pha}}$, two second-order equations, and momenta that are the velocities. The kinetic block is diagonal in the two rates, so the map from rates to momenta is multiplication by a frame factor and is invertible wherever $\varrho>0$. There is no primary constraint, no Dirac bracket and no constraint surface.

**The frozen frame is a restriction on the description, not on the data, and the distinction is the whole of this section.** Holding the six frame parameters fixed narrows which configurations the chart covers; a relation the variation cannot remove is a constraint. The one is imposed before the variation and the other by it, and the frame's freezing is the first kind. Reading it as a Gauss law counts one degree too few.

The connection enters as an additive shift and adds no condition. With $\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ the kinetic term keeps its bracket structure and changes its entries slot by slot, real in the temporal slot and central imaginary in the spatial ones. A shift of a rate is not a relation among variables, so the count survives the coupling unchanged.

What the chart costs, stated as a count. The general element's equations are not recovered from the central ones, and the central article says so in its own terms. That is a loss of variables and not the appearance of a constraint, and the count stays two and two at every rung of the chart.

## The Structural Consequence: Minimal Coupling Is a Shift of the Bracket

**The chart states minimal coupling as one substitution and nothing else.** In the eight-parameter chart the covariant derivative differs from the ordinary one by a central element, so it acts on the word as a shift of the phase's rate and of the frame's spatial gradient:

$$
\partial_{r'_t}\theta_{\mathrm{pha}}\ \longmapsto\ \partial_{r'_t}\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}A_t ,
\qquad
\vec\nabla_\Phi\theta_{\mathrm{pha}}\ \longmapsto\ \vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}\vec A .
$$

No other parameter moves. The claim is that this is the *whole* of minimal coupling in the chart, and it is checkable in one line: the covariant derivative is $\partial+\frac{2\pi iϙ}{h}A$ with $A$ central, and a central element commutes with the word, so it can only enter through the phase.

What it buys. The four-bracket expansion of the free article is unchanged: the brackets are the logarithmic derivative's decomposition and know nothing about the connection. The coupling enters the phase's bracket alone, and the mass term, being a function of $\varrho$ and the frame, is untouched. Hence the coupled chart's Lagrangian is the free chart's Lagrangian with one rate and one gradient shifted, and the two-number statement of the operator setting — $h_t\mapsto h_t-ϙ\omicron_{\mathrm{pot}}$, $\vec h_\Psi\mapsto\vec h_\Psi-ϙ\vec A$ — is the same statement read in the other chart.

What it forbids. A coupling that entered the frame's brackets would break the gauge invariance computed in the section on the charge, because the frame is what the gauge transformation rotates. The placement is therefore forced by the symmetry and not chosen for convenience.

### The Reconstruction and Its Limits

The reconstruction is the free one's, and that is a fact worth stating. The word does not contain the connection, so its inverse does not either: the two norms give $\varrho$ and $\theta_{\mathrm{rpd}}$, the direction gives $\theta_{\mathrm{pha}}$, and the residual rotor gives $\theta_{\mathrm{axr}}$ and $\vec u_{\mathrm r}$, by the same formulas as in the free polar article. The coupling is in the action and in the potential; it is not in the chart. A reader who expected the reconstructed variables to depend on $A_{\imath}$ has confused the field's parameterisation with its dynamics.

What the coupling does change is which frame is reconstructed. The potential depends on the frame variables and not on $\varrho$ or $\theta_{\mathrm{pha}}$, so the Euler–Lagrange equations for the six frame parameters are constraints rather than evolutions: the frame sits where the potential is extremal. The reconstruction recovers the frame, and then the constraint fixes it. Recovering and fixing are two steps, and the article keeps them apart because the first is a property of the bijection and the second a property of the coupling.

The scale's limit. $\varrho>0$ excludes the zero element and the cone's apex, so a field that reaches $\varrho=0$ leaves the chart. The coupled theory has no exception: the connection's term is finite at $\varrho=0$ and the chart still fails there, because the failure is in the parameterisation and not in the dynamics.

The angle's limits. The rotor's angle must be closed at $2\pi$ or the word misses the elements whose rotor factor is $-e_t$; the phase ranges over a half-open interval of length $\pi$. Both are inherited unchanged, and the coupling does not move either endpoint.

What the reconstruction does not give. The flow of the constrained system. The bijection makes the variation the same variation; it does not make the eight parameter equations' reduced flow the coupled pair's flow. This is the article's open question, stated once in the introduction and once here, because it is the one place where the polar reading of the coupled field is weaker than the element reading.

## The Noether Currents

### The Charge, Its Sign and Its Gauge Invariance

The charge is the phase rate times the density. The temporal component of the current in the chart is

$$
c\,\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}}{m}\bigl(E+ϙ c\,a'_t\bigr),
$$

with $E=-\frac{h}{2\pi} c\,\partial_{r'_t}\theta_{\mathrm{pha}}$, which is the free polar article's "charge is the phase rate times the density" with the mechanical phase rate. The article does not call $\rho_{\mathrm{num}}$ a momentum: in a second-order action the momentum conjugate to $\theta_{\mathrm{pha}}$ is proportional to $\partial_{r'_t}\theta_{\mathrm{pha}}$ and not to $\varrho^{2}$, and the statement that the density *is* the momentum belongs to the first-order cases, where the action's kinetic term is $-\rho\dot\theta$.

The sign. On the negative-frequency branch $E$ is negative, the bracket can change sign where the potential is large, and the charge density follows. So the potential shifts the boundary between the two signs but does not remove the sign change; the free article's two defects are one defect, and the coupling does not address it. The positive definiteness of $\rho_{\mathrm{num}}$ is a statement about the number density and not about the charge.

The gauge invariance. Under $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+\frac{2\pi ϙ\Lambda}{h}$ and $A_{\imath}\mapsto A_{\imath}-\partial_{\imath}\Lambda$, the bracket $\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t$ is invariant, the bracket $\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A$ is invariant, and **the charge is invariant**. The invariance is a two-line computation in the chart, and it is the same statement as the element companion's cancellation between the two terms of a bilinear. The chart's version is the sharper one for the charge, because the charge is one product and the cancellation is inside one bracket.

What the pairing of the two branches gives. Complex conjugation sends $\theta_{\mathrm{pha}}\to-\theta_{\mathrm{pha}}$ and leaves the connection alone; the charge changes sign and the action is unchanged, because the action is even in $\partial\theta$ except for the linear interaction term, and that term changes sign with the phase. So the conjugate branch is the antiparticle's chart, with the opposite charge and the same mass shell, and the potential's contribution to the charge reverses with it. The statement is the free article's, and the coupling's only addition is that the potential enters the charge.

### The Vorticity and the Flux

The action's statement. The chart's current is $\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}(\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A)$, and its vorticity is the curl of a gradient plus the curl of the potential. Varying the action in the phase gives the transport equation, and the transport equation is the statement that this current is divergenceless; so **the action knows the current and not its curl**. The curl is a consequence of the current's definition and not of the equation:

$$
\vec\nabla_\Phi\times\bigl(\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A\bigr)=ϙ\vec B .
$$

The circulation. Integrating along a closed loop,

$$
\oint\bigl(\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A\bigr)\cdot\mathrm{d}\vec l=h\,n+ϙ\Phi_B ,
$$

with $n$ the winding of the phase and $\Phi_B$ the flux enclosed. So the mechanical circulation is quantized up to the flux, and the chart's exact statement of the Aharonov–Bohm structure is that the flux enters the phase's bookkeeping and not the field's.

Why the action does not see it. A circulation is a property of a closed loop and the action is a functional of functions; the loop's statement is a consequence of the phase's being single valued, which the action's variations do not test. The article states the consequence and records that it is not an equation of motion: it is a boundary condition on the phase's winding, and the free article's nodal-set structure is where it is analysed.

## What the Principle Adds and What It Relabels: In the Polar Chart

Adds.

- A derivation of the charged Madelung pair from the element action by one substitution, with the two functions identified as the field's scale and phase rather than postulated.
- The interaction's two-term structure, linear and quadratic in the potential, exhibited separately, with the quadratic term identified as the one that gauge invariance requires.
- The statement that the coupling preserves the chart's regularity: same kinetic rank, same Legendre transform, no constraint, no multiplier.
- The charge's gauge invariance as a cancellation inside one bracket, and the vorticity and circulation as consequences of the current's definition.
- The eight-parameter chart's closure carried over unchanged, with the connection shifting two slots and multiplying nothing.

Does not add.

- No new prediction. The equations are the element companion's, re-coordinated.
- No new solution. The pair is the standard charged Madelung pair.
- No repair of the charge's sign.
- No explicit Jacobian in the general case, which the free polar article also leaves open.
- No statement about the operator setting's renormalisation, which is the quantised scalar article's.

The honest ledger. For the central field the polar variational principle is Madelung's, and the coupling makes it Madelung's with a potential; that is standard and the article says so. For the general element the chart is exact and regular, the connection shifts two slots, and nothing about the closure changes — the closure was the chart's and it stays the chart's. The genuinely new content is small and precise: the two interaction terms' separation, and the observation that a velocity shift leaves the Legendre transform's rank alone, so **the coupling cannot turn a regular system into a constrained one**.

## Open Questions

The $\rho_{\mathrm{chg}}^{2}A^{2}$ term's role in the chart's reading. The quadratic term is a potential and the chart's $V$ in the free article is a function of the frame; with the connection the potential acquires a term that depends on the frame only through $\varrho^{2}$. Whether that term has a reading as an effective mass or as a refractive index in the hydrodynamic picture is not attempted.

## Summary

The coupled Klein–Gordon action in polar variables is the free polar action with the covariant bracket,

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_{\imath}(\mathcal A^{\mathrm{gco}}_{\imath})^{*}\bigr]-4\pi^{2}\nu_m^{2}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\Bigr\},
\qquad
\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{i\,ϙ}{h}A_{\imath} .
$$

The connection's additive term is real in the temporal slot and central imaginary in the spatial ones, so it joins the scale bracket and the phase bracket and reaches neither the boost nor the rotor; the metric, the frame density and the amplitude–rapidity block are the free article's. For a central field the action is Madelung's with the mechanical four-momentum,

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{-(\partial_{r'_t}\varrho)^{2}+\lvert\nabla \varrho\rvert^{2}
+\frac{(2\pi)^{2} \rho_{\mathrm{num}}}{h^{2}}\bigl[(\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t)^{2}-\lvert\nabla S_{\tilde\Xi}-q\vec A\rvert^{2}\bigr]-4\pi^{2}\nu_m^{2}\rho_{\mathrm{num}}\Bigr\},
$$

and its two equations are the transport equation and the amplitude equation of the polar companion. The interaction is a linear term in the potential times the free phase rate plus a quadratic term with no phase, and the quadratic term is what gauge invariance requires. The kinetic matrix's rank is unchanged, so no constraint appears and no multiplier is needed; the eight-parameter chart's exactness by the invertible Jacobian is the free article's and survives. The vorticity of the mechanical current is $ϙ\vec B$ and its circulation is $h n+ϙ\Phi_B$.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=\varrho e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word |
| $\varrho>0$ | Scale; $\rho_{\mathrm{num}}=\varrho^{2}$ |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Central phase; $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ |
| $\theta_{\mathrm{rpd}}\ge0$, $\hat u_{\mathrm b}$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, $\hat u_{\mathrm r}$ | Frame parameters |
| $\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$ | The free bracket, four types |
| $\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ | The covariant bracket |
| $\varrho^{2}\cosh\theta_{\mathrm{rpd}}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | The frame density |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The connection; $a'_t,\vec A$ real |
| $ϙ$ | The coupling |
| $\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t$, $\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A$ | The mechanical four-momentum |
| $Q_{\mathrm{qnt}}=-\frac{hc}{8\pi^{2}\nu_m}\Box_\Phi \varrho/\varrho$ | The quantum potential; unchanged |
| $\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}(\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A)$ | The mechanical current; $\vec\nabla_\Phi\times=\rho_{\mathrm{chg}}\vec B$ |
| $h n+ϙ\Phi_B$ | The mechanical circulation |
| $\nu_m=\frac{mc}{h}$ | The mass wave number |

## Further Reading

- [The Lagrangian and the Coupled Klein–Gordon Equation](the-lagrangian-and-the-coupled-klein-gordon-equation.html), the element form this article re-coordinatises.
- [The Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the pair, the vorticity and the flux.
- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), for the equation and the current.
- [The Lagrangian and the Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-klein-gordon-equation-in-polar-variables.html), for the free polar action, the metric and the Jacobian argument.
- [The Lagrangian and the Klein–Gordon Equation](the-lagrangian-and-the-klein-gordon-equation.html), for the element action.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the covariant bracket and the curvature.
- [The Spin-Zero Fluid](the-spin-zero-fluid.html), for the hydrodynamic reading.
- [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), for the free flow's irrotationality.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the winding and the circulation.
- [The Lagrangian and the Coupled Proca Equation in Polar Variables](the-lagrangian-and-the-coupled-proca-equation-in-polar-variables.html), for the vector case's chart.
- E. Madelung, "Quantentheorie in hydrodynamischer Form", *Zeitschrift für Physik* 40 (1927), for the pair and its variational principle.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures", *Progress of Theoretical Physics* 8 (1952), for the relativistic pair and the Lagrangian treatment.
