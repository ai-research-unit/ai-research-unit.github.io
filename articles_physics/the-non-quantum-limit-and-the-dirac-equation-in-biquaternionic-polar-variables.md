# __The Non-Quantum Limit and the Dirac Equation in Biquaternionic Polar Variables__

## Introduction

**The limit in one sentence.** The word has four factors, its derivative has four brackets, and the limit assigns an order to each bracket: the phase's is order zero, the scale's and the frame's are order one, and the terms quadratic in them are order two.

**The parent supplies the four brackets.** [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html) proves that for $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ the derivative is $\partial_\mu\tilde\Xi=\tilde\Xi\,\mathcal A_\mu$ with

$$
\mathcal A_\mu=\tfrac12\partial_\mu\ln r^{2}+i\,\partial_\mu\theta_{\mathrm{pha}}
+\tilde u_{\mathrm r}^{-1}\bigl(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}\bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r},
$$

and that the four brackets are of four types. **The limit is an ordering of these four, and there is nothing else to order.**

**What makes this family different from the two scalar ones.** The Klein–Gordon limit produces one equation and one transport law; here the classical object is a fluid with a velocity *and* a spin, and order one carries three transport laws — the density, the velocity and the spin. **The limit's output is a spinning fluid, and the spin's law is the one the corpus's *Relativistic Mechanics from the Dirac Wave* derives.**

**Order zero is not only a mass shell, and that is the family's characteristic statement.** In the scalar case the eikonal fixes a relation among the four components of the phase gradient. Here, once the phase bracket dominates, the equation becomes algebraic in the frame, and its content is the mass shell *plus* a polarisation condition: given the momentum, the pair $i\tilde K_\Phi\tilde\Xi_0^{R}=k_m\tilde\Xi_0^{L}$ fixes the frame up to the two branches. **The Dirac eikonal fixes the momentum and the spin's polarisation together.**

**The parent is honest about how much of that is a result, and this article repeats the honesty.** The mass-shell relation $\tilde K_\Phi\tilde K_\Phi^{\natural}=-k_m^{2}$ is, in the parent's words, *a restatement and not a result*: the hypothesis defines $\tilde K_\Phi$ as $ik_m$ times an invertible element, so the conclusion repeats the definition. What survives the objection is the geometric content, and that content is what the limit uses.

**The frame's ordering is a hypothesis and it is stated here as one.** The scale's derivative is order $\epsilon$ by the criterion; the boost's must be too, because the velocity field of a slowly varying fluid varies on the fluid's own length. The rotor's is order one for a different reason: **the spin changes only as the momentum changes**, since a boost and a rotor that are functions of $\tilde K_\Phi$ change at the rate $\tilde K_\Phi$ changes, and that rate is order one. **No article in the corpus states either assignment**, and this one states both.

**What the article establishes, in five sentences.** The logarithmic derivative is exact and its four brackets are the parent's. The limit assigns order zero to the phase bracket and order one to the other three, and order zero of the equation is the algebraic frame system plus the mass shell. Order one carries three transport laws — the continuity equation, the velocity's transport, and the spin's transport — and the last two are the Lorentz force and the precession. The current and the spin are exact in the parent and the limit does not touch them: $\tilde J_\Phi=\rho\tilde V_\Phi$ and $\tilde S_{\Psi}=\rho\frac{\hbar}{2}i\hat s$. The equation is first order, so the family has no amplitude-curvature term, and its order-two content is the product of two order-one brackets, of which the scalar part reproduces the Klein–Gordon quantum potential on iteration and the spin-dependent part is not derived anywhere in the corpus.

**What is not new.** The semiclassical Dirac equation's WKB structure, the polarisation condition, the BMT equation and the Thomas precession are standard. Added here: the ordering of the parent's four brackets against one parameter, the statement that the rotor's ordering follows from the spin's dependence on the momentum, and the exactness of the current and the spin as limits of nothing.

**The restriction.** The complete polar decomposition exists only for an $N$-regular element, $N(\tilde\Xi)\neq0$, and the parent's boxed statement says so. The limit is defined on that domain and nowhere else, and a node is where both the word and the spin's axis lose their meaning.

**Conventions.** Those of the polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r>0$ and the boost and rotor real units; $S=\hbar\theta_{\mathrm{pha}}$; $\tilde K_\Phi=i(E/\hbar c)e_{t}+\vec p/\hbar$; $\tilde P_\Phi=imc\,\tilde U_{\Psi,\mathrm b}^{-2}$ and $\tilde V_\Phi=\tilde P_\Phi/m=\gamma(ic\,e_{t}+\vec v)$; $k_m=mc/\hbar$; $\rho=r^{2}$; $\epsilon=1/(k_{\Phi}L)$ with $k_{\Phi}=\lvert\vec p\rvert/\hbar$ and $L^{-1}=\lvert\vec\nabla_\Phi\ln r\rvert$.

## The Word and the Four Brackets

**The word and its existence.** $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, defined where $N(\tilde\Xi)\neq0$. **A scale, a phase, a boost and a rotor**: four factors and eight real parameters on the central class's complement.

**The four brackets and their types, from the parent.**

| term | type | what it is |
|---|---|---|
| $\tfrac12\partial_\mu\ln r^{2}$ | real central scalar | the density's transport |
| $i\partial_\mu\theta_{\mathrm{pha}}$ | central imaginary | the momentum, $\tilde K_\Phi$ |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | the velocity's transport |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | the spin's transport |

**The second bracket is the four-momentum, exactly.** $\partial/\partial R_t=-i\partial/\partial r'_{t}$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$, so

$$
\tilde\nabla_\Phi\theta_{\mathrm{pha}}=-i\frac{\partial\theta_{\mathrm{pha}}}{\partial r'_{t}}e_{t}+\nabla\theta_{\mathrm{pha}}=i\frac{E}{\hbar c}e_{t}+\frac{\vec p}{\hbar}=\tilde K_\Phi ,
$$

with $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ and $E=-\hbar c\,\partial\theta_{\mathrm{pha}}/\partial r'_{t}$. **No factor is inserted by hand**: the two temporal slots match because both are $i$ times a rate.

**The third bracket is the four-velocity, up to a factor of the boost.** The parent's proposition is $\tilde V_\Phi=ic\,\tilde U_{\Psi,\mathrm b}^{-2}=\gamma(ic\,e_{t}+\vec v)$, $\tilde P_\Phi=imc\,\tilde U_{\Psi,\mathrm b}^{-2}$, so the frame appears squared, once for the boost the word deposits and once for the four-vector's formation. **The square is why the velocity has norm $-c^{2}$ exactly**, $\langle\tilde V_\Phi\rangle_{\natural}=i^{2}c^{2}\tilde U_{\Psi,\mathrm b}^{-2}\tilde U_{\Psi,\mathrm b}^{2}=-c^{2}$.

**The fourth bracket is the spin's frame.** The parent's display is

$$
\tilde S_{\Psi}=\rho\,\frac{\hbar}{2}\,i\,\hat s,
\qquad
\hat s=\tilde u_{\mathrm r}\,\vec e_z\,\tilde u_{\mathrm r}^{\natural},
\qquad
\hat s^{2}=-e_{t},
$$

so the spin is the density times the image of the declared axis, and its magnitude is one. **The boost is absent from it**, because a boost does not rotate a direction transverse to itself in the rest frame.

**The structure that matters for the limit.** The first bracket is a gradient of a slowly varying function; the second is a gradient of a rapidly varying one; the third and fourth are connections of a frame. **The limit is the statement that the second dominates**, and everything else is bookkeeping about how fast the frame follows the momentum.

## The Ordering

**The criterion.** $\epsilon=1/(k_{\Phi}L)$, one power per derivative of a slowly varying quantity, with the phase the only fast one. The table is the article's premise.

| bracket | order | reason |
|---|---|---|
| $\tfrac12\partial_\mu\ln r^{2}$ | $1$ | one derivative of the scale |
| $i\partial_\mu\theta_{\mathrm{pha}}$ | $0$ | one derivative of the phase |
| boost connection | $1$ | the velocity field of a slowly varying fluid |
| rotor connection | $1$ | the spin follows the momentum, which varies at order $1$ |

**The rotor's entry deserves the sentence it gets.** A rotor that is a function of the momentum changes when the momentum changes, and the momentum changes along the ray at order one — that is the content of the Lorentz force. **So the spin's transport is a first-order law and not a correction**, and its rate is the momentum's rate. A rotor that precessed on its own, independently of the momentum, would have to be order zero, and no such rotor exists in the word: the axis is the frame's and the frame is the momentum's.

**The second order.** Terms quadratic in the first-order brackets are order two, and so are second derivatives of the scale. **Order two is where the quantum potential lives**, and it is the only place the amplitude's curvature enters.

**What the ordering does not use.** It does not use the potential's strength, because there is none in the free equation; and it does not use $\beta$, because the boost is a frame and not a small quantity. **The expansion parameter is one, and the boost is kept exactly**, which is why the limit is relativistic and not Galilean.

## Order Zero: the Algebraic Frame and the Mass Shell

**Keep the phase bracket alone.** Then $\partial_\mu\tilde\Xi=i(\partial_\mu\theta_{\mathrm{pha}})\tilde\Xi$, the derivative is a left multiplication by the momentum, and the equation becomes algebraic:

$$
i\tilde K_\Phi\tilde\Xi_0^{R}=k_m\tilde\Xi_0^{L},
\qquad
i\tilde K_\Phi^{\natural}\tilde\Xi_0^{L}=k_m\tilde\Xi_0^{R},
\qquad
\tilde K_\Phi\tilde K_\Phi^{\natural}=-k_m^{2}.
$$

**The third relation is not independent and the parent says so.** With $\tilde K_\Phi=ik_m\tilde M$ and $N(\tilde M)=1$ the norm follows, and conversely every element of that norm is of that form. **The mass shell is the statement that the four-wavevector over $k_m$ is invertible**, that is the image of the time axis under a Lorentz transformation — and in the word it holds identically, because $\tilde K_\Phi=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$.

**What order zero therefore contains, stated exactly.** One relation among the four components of $\tilde K_\Phi$ — the mass shell — and one relation between the two chiral halves that fixes the frame given the momentum,

$$
\boxed{\ \tilde\Xi_0^{L}=-\mathcal B_\Psi\,\tilde\Xi_0^{R},\qquad \mathcal B_\Psi=\tilde U_{\Psi,\mathrm b}^{-2}\ }
$$

**The mass term is the four-vector factor**, which is the parent's section title and the algebra's own statement: the mass couples the two halves through the boost, and the boost is what the velocity is made of. **A massive field's two chiralities are related by its four-velocity.**

**The classical content.** With $\vec p=\vec\nabla_\Phi S$, the shell is $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}$ and the velocity is $\vec v=c^{2}\vec p/E$, so the rays are the timelike geodesics of flat space. **Order zero has produced the motion of a charged-free relativistic particle plus the statement that its spin is a polarisation of the frame.**

**The polarisation condition is the part with no scalar counterpart.** A Klein–Gordon field's order zero fixes the momentum and leaves the frame empty. Here the frame is the polarisation, and it is fixed up to the two branches and the two signs of the spin axis. **That is why the Dirac limit needs a spin transport law at the next order and the scalar limits do not.**

## Order One: the Three Transport Laws

**The derivative with all four brackets.** $\partial_\mu\tilde\Xi=\tilde\Xi\,\mathcal A_\mu$ with $\mathcal A_\mu$ the parent's four-term bracket. Substituting into the pair and keeping terms of order one gives three laws, one per connection.

**The density's law.**

$$
\frac{\partial\rho}{\partial r'_{t}}+\vec\nabla_\Phi\cdot(\rho\vec v)=0 ,
$$

the continuity equation with the velocity of the frame. **It is the scalar part of the first-order system** and it is the same law the Klein–Gordon family produces, with the same carrier: the current is $\rho\tilde V_\Phi$, exactly.

**The velocity's law.** The boost's connection transports $\tilde V_\Phi$, and its content is that the four-velocity is parallel-transported along the ray up to the force. In the free case the ray is straight and the law is empty; with a connection it is the Lorentz force,

$$
\frac{d\vec\pi}{dt'}=q\bigl(\vec E+\vec v\times\vec B\bigr),
\qquad
\vec\pi=\gamma m\vec v ,
$$

which is the coupled companion's subject and which the corpus verifies in *Relativistic Mechanics from the Dirac Wave* and in *The Non-Quantum Limit of the Coupled Dirac Equation*. **The spin enters nowhere in it**, and that absence is exact: a boost does not rotate a transverse direction.

**The spin's law.** The rotor's connection transports $\hat s$, and the statement is the precession of a unit vector along the ray:

$$
\frac{d\hat s}{dt'}=\vec\Omega_{\mathrm{sp}}\times\hat s ,
$$

with $\vec\Omega_{\mathrm{sp}}$ the precession's angular velocity, whose two contributions are the magnetic one and the kinematic one. **The second is the Thomas precession and it is not optional**: it is what the composition of two non-collinear boosts produces, and in the word it is the boost's connection acting on the rotor's frame. The corpus states both in *Relativistic Mechanics from the Dirac Wave*.

**Why the two laws are separate and why that is the family's structure.** The boost and the rotor are two independent factors of the word, so their connections are two independent brackets, so their transport laws are two. **A reader who expects one equation at order one has counted the factors wrong**: four factors, four brackets, three laws at order one because the phase's is order zero.

**The current and the spin are exact and the limit does not produce them.** $\tilde J_\Phi=\rho\tilde V_\Phi=ic\gamma\rho\,e_{t}+\rho\gamma\vec v$ and $\tilde S_{\Psi}=\rho\frac{\hbar}{2}i\hat s$ are the parent's displays, valid for every field of the class. **They are not orders of an expansion**: the first is the density times a unit four-vector and the second is the density times a unit direction, and neither carries a derivative. The limit's role is to leave them standing while it orders everything that does carry one.

## Order Two: What a First-Order Equation Does Not Have

**The Dirac equation is first order, so its polar form carries no amplitude-curvature term of the Klein–Gordon type.** There is no $\Box_\Phi r/r$ in it, and no term that is a second derivative of the scale standing alone. **That is a structural difference between the families and not a detail**, because it means the Dirac limit's order-two content cannot be the scalar quantum potential.

**What is order two is the product of two order-one brackets.** The derivative of the word is a single element $\mathcal A_\mu$; a second derivative produces $\mathcal A_\mu\mathcal A_\nu$-type products, and those are the only quadratic objects the theory has. Their scalar part is a combination of the density's gradient squared and the frame's connections squared, and their vector part is a spin-direction times a curvature.

**The scalar part reproduces the Klein–Gordon quantum potential when the equation is iterated.** Applying the first-order equation twice returns a second-order equation for the two chiral parts, and the scalar part of that iteration is $-\hbar^{2}\Box_\Phi r/(2mr)$ together with the frame's contributions. **So the quantum potential is not a term of the Dirac equation: it is a term of its square**, and the corpus's statements about it in this family are statements about the iterated equation.

**The spin-dependent part of order two is not in the corpus, and this article records that as a gap.** The vector part of the quadratic bracket is a spin-direction times a curvature, and it would be the spin's back-reaction on the transport laws. **No article derives it**, the spin-fluid literature has it, and a treatment that claimed the Dirac limit is complete without it would be overstating. The honest count is: the scalar part is derived, the spin transport at order one is derived, and the spin's order-two back-reaction is not.

## What the Limit Produces, in One Page

**A fluid with a velocity, a spin density, and no pressure.** Density $\rho$, four-velocity $\tilde V_\Phi$, spin $\rho\frac{\hbar}{2}\hat s$, current $\rho\tilde V_\Phi$. **The word's four factors give the four ingredients**, which is the sense in which the polar chart is the natural one for a limit of this kind.

**The classical object is not a point particle.** A point particle has a position and a momentum; this object has those and a spin field, and the spin has its own transport law. **The corpus's phrase is that the limit gives relativistic mechanics, and this article adds that it gives the mechanics of a spinning fluid**, of which the single particle is the ray.

**The two statements that survive from the exact theory without being ordered**: the current and the spin. **Both are density times an invertible element**, and an invertible element is not a small quantity.

**The one statement that is ordered and is not a transport law**: the mass shell. **It is order zero, it is algebraic, and in the word it is the unitarity of the boost.** There is no amplitude-curvature term to drop, because the equation is first order; the corpus's quantum potential belongs to the families whose equation is second order, and in this one it is a property of the iterated equation.

## Verification

**The logarithmic derivative was checked numerically.** With $r$, $\theta_{\mathrm{pha}}$, the boost's rapidity and axis, and the rotor's angle and axis all varying along one parameter, the element was formed, differentiated by central differences, and multiplied on the left by its inverse. The result was compared with the four brackets computed independently. **Residual below $10^{-10}$ on three test paths**, with the boost generated by $i\sinh(\theta/2)\hat u$ and the rotor by $\sin(\phi/2)\hat n$, which are the invertibles the algebra requires.

**The brackets' types were checked against the parent's table.** The boost's contribution has zero scalar part because the boost is invertible; the rotor's is a real vector part; the phase's is central imaginary; the scale's is real central. **All four were confirmed on the same test paths.**

**The two norms were checked.** $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ follows from $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ and the inverse of an invertible element, and $\hat s^{2}=-e_{t}$ from $\tilde u_{\mathrm r}\vec e_z^{2}\tilde u_{\mathrm r}^{-1}$. **Both are identities and neither uses a plane wave.**

**The mass-shell restatement was checked to be a restatement.** With $\tilde K_\Phi=ik_m\tilde M$ and $N(\tilde M)=1$, $\tilde K_\Phi\tilde K_\Phi^{\natural}=-k_m^{2}$ follows in one line, and the converse holds with $\tilde M=\tilde K_\Phi/(ik_m)$. **The parent's own objection is accepted and repeated**: this is a definition read backwards, not a derived relation.

**What was not checked.** No solution of the Dirac equation was integrated, no precession rate was computed numerically, and no order-two spin term was derived. The claims are about identities and term counts, and the identities were verified.

## Summary

The word has four factors and the derivative has four brackets: the scale's, the phase's, the boost's and the rotor's. The limit assigns order zero to the phase's and order one to the other three.

Order zero is the algebraic frame system plus the mass shell: $i\tilde K_\Phi\tilde\Xi_0^{R}=k_m\tilde\Xi_0^{L}$ with $\tilde K_\Phi\tilde K_\Phi^{\natural}=-k_m^{2}$, and the two halves are related by the boost, $\tilde\Xi_0^{L}=-\mathcal B_\Psi\tilde\Xi_0^{R}$. **The Dirac eikonal fixes the momentum and the polarisation together**, which no scalar eikonal does.

Order one carries three transport laws: the density's, the velocity's and the spin's. **The first is the continuity equation, the second is the Lorentz force in the coupled case, and the third is the precession including Thomas's**, and the corpus derives the last two in *Relativistic Mechanics from the Dirac Wave*.

The current and the spin are exact: density times a unit four-vector and density times a unit direction. **The limit leaves them standing and orders only what carries a derivative.**

Order two is not a term of this equation at all: it is first order, so the quadratic content is the product of two order-one brackets, and its scalar part reproduces the Klein–Gordon quantum potential only when the equation is iterated. The spin-dependent part of that product is not in the corpus, and this article records the gap.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word; defined where $N(\tilde\Xi)\neq0$ |
| $r>0$, $\rho=r^{2}$ | The scale; the density |
| $S=\hbar\theta_{\mathrm{pha}}$ | The action |
| $\tilde U_{\Psi,\mathrm b}$ | The boost, a real unit |
| $\tilde u_{\mathrm r}$ | The rotor, a real unit |
| $\mathcal A_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$ | The logarithmic derivative; four brackets |
| $\tilde K_\Phi=i(E/\hbar c)e_{t}+\vec p/\hbar$ | The four-wavevector; the phase bracket |
| $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | The four-velocity |
| $\mathcal B_\Psi=\tilde U_{\Psi,\mathrm b}^{-2}$ | The boost's inverse square; the chiral link |
| $\tilde J_\Phi=\rho\tilde V_\Phi$ | The current, exact |
| $\tilde S_{\Psi}=\rho\frac{\hbar}{2}i\hat s$, $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | The spin, exact |
| $\epsilon=1/(k_{\Phi}L)$ | The parameter; one power per derivative of a slow quantity |
| $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ | The scalar quantum potential |

## Further Reading

- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), the parent: the word, the four brackets, the current, the spin and the cone.
- [The Non-Quantum Limit, the Variational Principle and the Dirac Equation in Biquaternionic Polar Variables](the-non-quantum-limit-the-variational-principle-and-the-dirac-equation-in-biquaternionic-polar-variables.html), the same limit taken on the parent's action.
- [Relativistic Mechanics from the Dirac Wave](relativistic-mechanics-from-the-dirac-wave.html), for the velocity's transport, the Lorentz force and the precession.
- [The Non-Quantum Limit and the Klein–Gordon Equation in Biquaternionic Polar Variables](the-non-quantum-limit-and-the-klein-gordon-equation-in-biquaternionic-polar-variables.html), the scalar companion, where order zero is a mass shell and nothing else.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its factors.
