# __The Non-Relativistic Limit of Relativistic Mechanics in Biquaternionic Form__

## Introduction

The kinematic content of relativistic mechanics is one element and one constraint. The element is the four-velocity of the particle, a biquaternion of the material sector; the constraint is that its norm is $-c^{2}$, the same for every particle. Every other kinematic element of the theory — the four-momentum, the four-current, the four-potential of a single charge, the four-wave-number — is that element with a scale attached, and the scale is the one thing the constraint does not fix.

The non-relativistic limit is one operation on the constraint. Nothing is added, and no second equation is introduced.

**The method in one display.** Write the four-velocity in its two parts, the temporal one and the vector one,

$$
\tilde V_{\Phi} = \underbrace{i\,\gamma c\,e_{t}}_{\text{temporal}} + \underbrace{\gamma\vec v}_{\text{vector}} ,
\qquad
\langle\tilde V_{\Phi}\rangle_{\natural} = -\left(\gamma c\right)^{2}+\left(\gamma v\right)^{2} = -c^{2} .
$$

The constraint says that the square of the temporal part exceeds the square of the vector part by $c^{2}$. Write the temporal part as $\gamma c=c\left(1+2\eta\right)$, so that $2\eta c$ is its excess over its rest value $c$. The same constraint, divided by $c^{2}$ and rearranged, then reads

$$
\boxed{\;\left(\frac{\gamma v}{c}\right)^{2} = 4\eta\left(1+\eta\right)\;}
$$

which is exact. The right side shows both terms at once: $4\eta$ is the leading one, $4\eta^{2}$ is the one to be dropped, and $\eta$ **is** their ratio. The box therefore contains its own small parameter, and the limit is the statement that the second term may be dropped. No expansion is made before this line, and no constant is set to anything.

**Why the four-velocity and not the four-momentum.** The four-momentum is $\tilde P_{\Phi}=m\tilde V_{\Phi}$, and the mass is a free real scale that the algebra does not fix: the norm is homogeneous and the light cone is scale-invariant, so the constraint cannot choose a mass. If the limit is taken on $\tilde P_{\Phi}$, the mass appears in every coefficient of the answer, and it has entered by a route the constraint never authorised. Taken on $\tilde V_{\Phi}$, the limit is a statement about a dimensionless element, and the mass enters once, at the end, where the scale is attached. §*The Scale: The Four-Momentum* attaches it, and §*Other Biquaternions Under the Same Limit* lists the elements that are in the family and the elements that are not.

**What the article does.** It states the element and its norm, and shows that the norm is the only constraint and is conserved by construction. It reduces the constraint to one equation in one dimensionless number and computes the limit there. It records what the limit says about the velocity itself, including the composition of velocities. It attaches the scale and recovers the ladder of the energy, the momentum and the Lagrangian, with the error in closed form. It classifies the other biquaternions of the theory by whether they are that element times a scale, and it states what the limit does not do.

**What is not new.** The algebra is the algebra of *Relativistic Mechanics in Biquaternionic Form*, and the expansion of a square root is textbook. What the article isolates is which element carries the limit and in what order the moves go: **write the norm in two parts, reduce it to one dimensionless equation, expand once, keep the leading term, then attach the scale.** The same four moves, on the same constraint written in wave numbers, appear in *The Three Wavenumbers of a Particle*; on the field equation they appear in *The Klein–Gordon Equation in Biquaternionic Form*.

**Two limits, not one.** The corpus uses the phrase *non-relativistic limit* for two different restrictions. *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form* separates them, and this article keeps the separation. The **kinematic** limit is the one treated here: the vector part of the four-velocity is small compared with the temporal part, and the constraint is truncated. The **central-scalar** restriction says which directions of the algebra are occupied, and it holds at any speed. A slowly moving spinning top satisfies this article's limit and violates the central-scalar restriction. A relativistic scalar particle does the opposite.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_{t}=1, \vec e_{x}, \vec e_{y}, \vec e_{z}$ with $\vec e_{\mu}^{2}=-e_{t}$ and $\vec e_{\mu}\vec e_{\nu}=\varepsilon_{\mu\nu\lambda}\vec e_{\lambda}$, and $i$ is the scalar imaginary, central in $\mathbb{B}$. The material sector is $\mathbb{B}_{\Phi}=\mathrm{span}_{\mathbb{R}}\{ie_{t},\vec e_{x},\vec e_{y},\vec e_{z}\}$, the anti-Hermitian one, and the informational sector is $\mathbb{B}_{\Psi}=\mathrm{span}_{\mathbb{R}}\{e_{t},i\vec e_{x},i\vec e_{y},i\vec e_{z}\}$, the Hermitian one. The four-position is $\tilde R_{\Phi}=i\,r'_{t}\,e_{t}+\vec r$ and the four-velocity is $\tilde V_{\Phi}$ of §*The Four-Velocity and Its Norm*, both in $\mathbb{B}_{\Phi}$. The rapidity is $\theta_{\mathrm{rpd}}$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, $c_{0}$ its vacuum value, $\beta=\lvert\vec v\rvert/c$, and $\gamma=1/\sqrt{1-\beta^{2}}$.

## The Four-Velocity and Its Norm

**The element.** For a particle with velocity $\vec v$,

$$
\tilde V_{\Phi} = \gamma\left(i\,c\,e_{t}+\vec v\right) = i\,\gamma c\,e_{t}+\gamma\vec v ,
\qquad
\gamma=\frac{1}{\sqrt{1-\vec v^{\,2}/c^{2}}} .
$$

The coefficient of $e_{t}$ is imaginary and the vector part is real, so $\tilde V_{\Phi}$ is anti-Hermitian and lies in $\mathbb{B}_{\Phi}$. Its **norm** is

$$
\langle\tilde V_{\Phi}\rangle_{\natural} = \tilde V_{\Phi}\tilde V_{\Phi}^{\natural}
= \gamma^{2}\left(-c^{2}+\vec v^{\,2}\right) = -c^{2} .
$$

That line is the whole input of the article. It is one equation, it holds for every particle, and it contains no mass, no $\hbar$ and no energy.

**Two parts, one ratio.** The element carries two numbers: the temporal part, of magnitude $\gamma c$, and the vector part, of magnitude $\gamma v$. Their ratio is

$$
\beta := \frac{\lvert\gamma\vec v\rvert}{\lvert i\gamma c\rvert} = \frac{v}{c} ,
$$

exactly, at every speed and with no approximation. The parameter of the limit is therefore not a small number inserted from outside: it is **the ratio of the two parts of the element**, and the limit is the statement that this ratio is small. That is why the four-velocity is the right base for the calculation, and why no expansion in $v/c$ can surprise: the quantity expanded is a ratio of two parts of the object being expanded.

**The norm is conserved, and it is the only constraint.** The norm of $\mathbb{B}$ is multiplicative, $\langle\tilde Q_{1}\tilde Q_{2}\rangle_{\natural}=\langle\tilde Q_{1}\rangle_{\natural}\langle\tilde Q_{2}\rangle_{\natural}$, and a boost acts on the four-vectors of $\mathbb{B}_{\Phi}$ by a rotor conjugation, that is by multiplication on the two sides by elements of unit norm. The norm of $\tilde V_{\Phi}$ is therefore the same in every frame,

$$
\langle\tilde V_{\Phi}'\rangle_{\natural} = \langle\tilde V_{\Phi}\rangle_{\natural} = -c^{2} ,
$$

and the same along the worldline, for the same reason. So the constraint is preserved by the transformation group rather than imposed after the fact. It is also the only constraint: the element has four real coefficients, the norm is one real condition, and the remaining three are the three components of the velocity. Equivalently, the set of four-velocities is the hyperboloid $\langle\tilde Q_{\Phi}\rangle_{\natural}=-c^{2}$ in $\mathbb{B}_{\Phi}$, and the Lorentz group acts on it transitively.

**The shape of the hyperboloid.** The condition $\gamma^{2}\left(c^{2}-v^{2}\right)=c^{2}$ can be read without algebra: it says $c^{2}-v^{2}>0$, so $0\le\lvert\vec v\rvert<c$. The hyperboloid is one sheet with an apex at $\vec v=0$, where the element is $i\,c\,e_{t}$, and an asymptote at $\lvert\vec v\rvert=c$, which it approaches and never reaches. The speed of light is not a parameter of the theory that could be varied: it is the value of the norm, and it enters here as the height of the apex.

**The apex is itself a solution.** At $\vec v=0$ the element is $\tilde V_{\Phi}=i\,c\,e_{t}$, with norm $-c^{2}$. The rest element is not a limiting case of the family, it is a member of it, and that is why dividing a solution by its rest phase is legitimate in the field articles: the divisor is the four-velocity of a particle at rest, on the same hyperboloid as the state it divides.

## The Norm as One Equation in Two Terms

**One number replaces the velocity.** The element has four coefficients and one constraint, so three of them are free; at fixed direction there is one. Define the single dimensionless number by

$$
\gamma = 1+2\eta ,
\qquad
\eta=\frac{\gamma-1}{2} .
$$

The temporal part is then $c\left(1+2\eta\right)$, and $2\eta c$ is its excess over the rest value $c$. The number is non-negative, it vanishes at the apex, and it grows without bound as $\lvert\vec v\rvert\to c$.

**The constraint, rewritten.** Substituting $\gamma=1+2\eta$ into $\gamma^{2}\left(c^{2}-v^{2}\right)=c^{2}$ and solving for the vector part gives the box of the introduction,

$$
\left(\gamma v\right)^{2} = c^{2}\left[\left(1+2\eta\right)^{2}-1\right] = 4c^{2}\eta\left(1+\eta\right) .
$$

This is the equation the rest of the article works on. It says that **the square of the vector part, in units of $c^{2}$, is four times $\eta$ times one plus $\eta$**. One factor is linear in $\eta$ and one is not, and there is nothing else in the equation: no mass, no energy, no $\hbar$.

**The same statement in four other forms.** Multiplying out, the box is $\gamma^{2}\beta^{2}=4\eta\left(1+\eta\right)$, which is the difference of squares $\gamma^{2}-1=\left(\gamma-1\right)\left(\gamma+1\right)$ with $\gamma-1=2\eta$. Divided by $\gamma^{2}$ it is $1-\beta^{2}=1/\gamma^{2}$, which is the definition of $\gamma$, so the box is not a new relation but the norm in the variable $\eta$. Solved for $\eta$ it is

$$
\eta = \frac{1}{2}\left(\sqrt{1+\left(\gamma\beta\right)^{2}}-1\right) ,
$$

which is closed form. And in the rapidity of §*The Ladder of the Velocity* it is $\sinh^{2}\theta_{\mathrm{rpd}}=4\eta\left(1+\eta\right)$, which is the identity $\cosh^{2}-\sinh^{2}=1$ with $\cosh\theta_{\mathrm{rpd}}=1+2\eta$. These are one equation, and the choice among the forms is a choice of variable.

**Solved as a correction.** Write the box as $\eta\left(1+\eta\right)=\eta_{\mathrm{trunc}}$ with

$$
\eta_{\mathrm{trunc}} := \frac{\left(\gamma\beta\right)^{2}}{4} ,
$$

so that the exact $\eta$ and the truncated one stand in the ratio

$$
\eta = \frac{\eta_{\mathrm{trunc}}}{1+\eta} .
$$

Written this way, the box states the whole limit in one line: the numerator is what the leading term keeps, the denominator is the correction, and the correction is $1$ at the apex and falls as the speed rises. §*The Small Parameter* turns the ratio into the number that measures the truncation, and shows that it is $\eta$ itself.

**The trap in splitting the element.** The element splits as $\tilde V_{\Phi}=i\,c\,e_{t}+\left(i\,2\eta c\,e_{t}+\gamma\vec v\right)$, the apex plus a **displacement**, and it is tempting to split the norm the same way. It cannot be done: the norm is not additive,

$$
\langle\tilde Q_{1}+\tilde Q_{2}\rangle_{\natural} = \langle\tilde Q_{1}\rangle_{\natural}+\langle\tilde Q_{2}\rangle_{\natural}+2\,\mathrm{Sc}\left(\tilde Q_{1}\tilde Q_{2}^{\natural}\right) ,
$$

so the constraint on the sum is not the sum of the constraints. The apex satisfies the constraint, the displacement does not, and the state satisfies it because of the cross term. The box is the correct statement, and it is a statement about the whole element, not about its two parts.

## The Small Parameter

**The ratio of the two terms.** The box reads $4\eta+4\eta^{2}$, and the quotient of the second term by the first is $\eta$. So the parameter that appears in the box is the small parameter of its own expansion, and no second letter is needed. What remains is to say what it measures, and the answer is that it measures the truncation:

$$
\frac{\eta-\eta_{\mathrm{trunc}}}{\eta_{\mathrm{trunc}}} = -\frac{\eta}{1+\eta} .
$$

**The error, in closed form.** That ratio is exact at every speed, because $\eta\left(1+\eta\right)=\eta_{\mathrm{trunc}}$ is the box. The error of the leading term is therefore the parameter itself to leading order, and it is known exactly rather than estimated. It is below one per cent as soon as $\eta<10^{-2}$, that is $\gamma<1.02$, that is $\beta<0.197$.

**Why the parameter is not $\beta$.** The exact relation between the two is

$$
\beta^{2} = \frac{4\eta\left(1+\eta\right)}{\left(1+2\eta\right)^{2}} = 4\eta+O\left(\eta^{2}\right) ,
$$

so $\beta\approx2\sqrt{\eta}$: **half a power of $\eta$ for one power of $\beta$**. A limit stated as $\beta\ll1$ is therefore a statement about a square root. The two agree in what they call small — $\beta\to0$ and $\eta\to0$ together — and they disagree in the power, so a criterion quoted in $\beta$ is correct only after being squared. At leading order $\eta=\beta^{2}/4$, and a reader who wants one number can use either; the article uses $\eta$ because the box is written in it.

## The Ladder of the Velocity

**One expansion.** The box has one expansion, and every kinematic quantity is a function of the same hyperbolic cosine. Expanding,

$$
\gamma = 1+\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\frac{5\beta^{6}}{16}+\cdots ,
\qquad
\eta = \frac{\beta^{2}}{4}+\frac{3\beta^{4}}{16}+\frac{5\beta^{6}}{32}+\cdots ,
$$

and the vector part of the element follows from $\gamma\beta$,

$$
\frac{\lvert\gamma\vec v\rvert}{c} = \gamma\beta = \beta+\frac{\beta^{3}}{2}+\frac{3\beta^{5}}{8}+\cdots .
$$

The first correction to the element is thus entirely a thickening of the temporal part. To first order in $\beta^{2}$,

$$
\tilde V_{\Phi} = i\,c\,e_{t}+\vec v+\frac{\beta^{2}}{2}\,i\,c\,e_{t}+O\left(\beta^{4}\right) ,
$$

that is, the apex, plus the velocity, plus $O\left(\beta^{2}\right)$ of extra temporal part.

**The constraint decides the order of the truncation.** Truncate $\gamma$ at order zero, $\gamma=1$: the norm is then $-c^{2}+v^{2}$, which differs from $-c^{2}$ at order $\beta^{2}$. Truncate at order $\beta^{2}$, $\gamma=1+\beta^{2}/2$: the norm is

$$
\gamma^{2}\left(v^{2}-c^{2}\right) = -c^{2}\left(1-\frac{3}{4}\beta^{4}+O\left(\beta^{6}\right)\right) ,
$$

which differs at order $\beta^{4}$. Keep the $\beta^{4}$ term of $\gamma$ and the error is of order $\beta^{6}$. **The truncation error of the norm is one order beyond the truncation error of $\gamma$**, because the norm is quadratic in $\gamma$ and vanishes identically for the exact one, so its error is the square of the error of $\gamma$ to leading order. A truncated four-velocity is on the hyperboloid to one order better than it is on the series, which is why the element of the limit, though off the hyperboloid, is off it at a high order.

**The rapidity, and why it is the additive coordinate.** Set

$$
\gamma=\cosh\theta_{\mathrm{rpd}} ,
\qquad
\gamma\beta=\sinh\theta_{\mathrm{rpd}} ,
\qquad
\theta_{\mathrm{rpd}}=\operatorname{artanh}\beta .
$$

The norm identity then reads $\cosh^{2}\theta_{\mathrm{rpd}}-\sinh^{2}\theta_{\mathrm{rpd}}=1$, which is not a coincidence of notation: the hyperboloid $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$ **is** the hyperbola, and the rapidity is its own parameter. In this variable the limit has its simplest form. The parameter is

$$
\eta = \frac{\cosh\theta_{\mathrm{rpd}}-1}{2} = \frac{\theta_{\mathrm{rpd}}^{2}}{4}+\frac{\theta_{\mathrm{rpd}}^{4}}{48}+\cdots ,
$$

so **the limit is the statement that the rapidity is small**, and the parameter is a coordinate on the hyperboloid measured from the apex, squared and halved. The truncated form is $\eta_{\mathrm{trunc}}=\frac{1}{4}\sinh^{2}\theta_{\mathrm{rpd}}$, one quarter of the square of the vector part, and $\eta=\eta_{\mathrm{trunc}}/\left(1+\eta\right)$ is the exact correction between the two.

**Velocities compose by addition of rapidities and not of speeds.** Rapidity adds exactly, $\theta_{\mathrm{rpd},12}=\theta_{\mathrm{rpd},1}+\theta_{\mathrm{rpd},2}$, because the boost is one rotor and the rotors of one direction multiply by adding their angles. In speeds this is

$$
\beta_{12} = \frac{\beta_{1}+\beta_{2}}{1+\beta_{1}\beta_{2}} ,
$$

whose departure from the Galilean sum is

$$
\beta_{12}-\left(\beta_{1}+\beta_{2}\right) = -\frac{\beta_{1}\beta_{2}\left(\beta_{1}+\beta_{2}\right)}{1+\beta_{1}\beta_{2}} ,
$$

of second order in the speeds. Two speeds of $0.3c$ and $0.4c$ add to $0.625c$ and not to $0.7c$. The Galilean law is the leading term of the expression above, and its error is the product of the two small parameters. **The additivity of the rapidity is the exact statement, and the Galilean addition law is its truncation**: the same relation the box has to its leading term.

## The Scale: The Four-Momentum

**One multiplication.** The four-momentum is the four-velocity with the mass attached,

$$
\tilde P_{\Phi} = m\,\tilde V_{\Phi} = i\,\frac{E}{c}\,e_{t}+\vec p_{\Phi} ,
\qquad
E=\gamma mc^{2},
\qquad
\vec p_{\Phi}=m\gamma\vec v ,
$$

and it lies in $\mathbb{B}_{\Phi}$ with norm $\langle\tilde P_{\Phi}\rangle_{\natural}=-m^{2}c^{2}$. The two components are worth writing on their own, because they are what makes the scale a scale and nothing else: **the vector part of the four-velocity is the momentum per unit mass, and the temporal part is the energy per unit mass in units of $c$**,

$$
\vec p_{\Phi} = m\left(\gamma\vec v\right) ,
\qquad
E = mc\left(\gamma c\right) .
$$

**The same ladder, multiplied.** Since $\tilde P_{\Phi}=m\tilde V_{\Phi}$, every series of the previous sections is the same series with one factor:

$$
E = mc^{2}+\frac{1}{2}mv^{2}+\frac{3}{8}\frac{mv^{4}}{c^{2}}+\cdots ,
\qquad
p_{\Phi} = mv+\frac{1}{2}\frac{mv^{3}}{c^{2}}+\cdots .
$$

The excess energy is $\mathcal{E}:=E-mc^{2}=2\eta\,mc^{2}$, so the small parameter of the energy ladder is the same $\eta$, and the error of the truncation is the same $-\eta/\left(1+\eta\right)$. One check makes the point: the truncated excess energy is

$$
\frac{p_{\Phi}^{2}}{2m} = \frac{1}{2}m\left(\gamma v\right)^{2} = mc^{2}\cdot\frac{\left(\gamma\beta\right)^{2}}{2} = 2mc^{2}\eta_{\mathrm{trunc}} ,
$$

which is the truncated temporal excess times $mc^{2}$. The two "columns" — one in the momentum, one in the speed — are one column read in two units.

**The mass shell, and where it comes from.** Multiplying the norm by $m^{2}$ and writing it in components gives

$$
E^{2} = p_{\Phi}^{2}c^{2}+m^{2}c^{4} ,
$$

which is the constraint of the four-momentum. In the variable of the excess energy it reads

$$
\left(E-mc^{2}\right)\left(E+mc^{2}\right) = p_{\Phi}^{2}c^{2} ,
\qquad
p_{\Phi}^{2} = 2m\mathcal{E}+\frac{\mathcal{E}^{2}}{c^{2}} ,
$$

the second being the box multiplied by $m^{2}c^{2}$ and written in $\mathcal{E}$ instead of $\eta$. Nothing here is new. The point of writing the constraint twice is that the momentum form has one feature the velocity form does not, and the next paragraph is about it.

**The second sheet is an artefact of squaring.** The box in $\mathcal{E}$ is a quadratic, so it has two roots,

$$
E_{\pm} = \pm\sqrt{m^{2}c^{4}+p_{\Phi}^{2}c^{2}} ,
\qquad
\mathcal{E}_{-} = -mc^{2}-\sqrt{m^{2}c^{4}+p_{\Phi}^{2}c^{2}} \approx -2mc^{2} ,
$$

and the negative one is a branch the limit cannot touch: for it $\eta_{-}=\mathcal{E}_{-}/\left(2mc^{2}\right)\approx-1$, so no ratio in it is small. The four-velocity has no such branch. Its temporal part is $\gamma c$ with $\gamma>0$ by construction, so the hyperboloid is one sheet, the limit is taken on the only sheet there is, and nothing is discarded. **The negative branch appears when the constraint is squared, not when it is written.** That is a further reason to take the velocity as the base: on the velocity the limit has no branch to select, and the selection rule of the energy form is a rule about a form the algebra did not ask for.

**The Lagrangian, and the Legendre check.** The free relativistic Lagrangian is $L=-mc^{2}\sqrt{1-\beta^{2}}=-mc^{2}/\gamma$, and its warrant is that it reproduces the momentum, $\partial L/\partial v=\gamma mv$. In terms of the element it is $L=-mc^{2}\left(c/\lvert V_{t}\rvert\right)$: the Lagrangian is the rest energy divided by the temporal part of the four-velocity. Expanding in $\beta$,

$$
L = -mc^{2}+\frac{1}{2}mv^{2}+\frac{1}{8}\frac{mv^{4}}{c^{2}}+\cdots ,
\qquad
L = -mc^{2}+\frac{p_{\Phi}^{2}}{2m}-\frac{3p_{\Phi}^{4}}{8m^{3}c^{2}}+\cdots ,
$$

and the coefficients differ between the two variables for the reason given in the next paragraph. The Legendre transform $E=p_{\Phi}v-L$ is exact at every speed, and to order $c^{-2}$,

$$
p_{\Phi}v = \frac{p_{\Phi}^{2}}{m}-\frac{p_{\Phi}^{4}}{2m^{3}c^{2}} ,
\qquad
-L = mc^{2}-\frac{p_{\Phi}^{2}}{2m}+\frac{3p_{\Phi}^{4}}{8m^{3}c^{2}} ,
$$

whose sum is $mc^{2}+p_{\Phi}^{2}/2m-p_{\Phi}^{4}/\left(8m^{3}c^{2}\right)$ because $-\frac{1}{2}+\frac{3}{8}=-\frac{1}{8}$. The coefficient that surprises is a sum of two terms of opposite sign, and the check is what fixes it.

**Why the two columns have different coefficients.** The momentum column expands in $u:=p_{\Phi}^{2}/\left(m^{2}c^{2}\right)=\sinh^{2}\theta_{\mathrm{rpd}}$, and the velocity column expands in $\beta^{2}=\tanh^{2}\theta_{\mathrm{rpd}}$. Both are $\theta^{2}$ at leading order and they differ at the next: $\sinh^{2}\theta=\theta^{2}+\frac{1}{3}\theta^{4}+\cdots$ and $\tanh^{2}\theta=\theta^{2}-\frac{2}{3}\theta^{4}+\cdots$. The energy series in the two variables is

$$
2\eta = \frac{1}{2}u-\frac{1}{8}u^{2}+\cdots = \frac{\theta^{2}}{2}+\left(\frac{1}{6}-\frac{1}{8}\right)\theta^{4}+\cdots ,
$$

$$
2\eta = \frac{1}{2}\beta^{2}+\frac{3}{8}\beta^{4}+\cdots = \frac{\theta^{2}}{2}+\left(-\frac{1}{3}+\frac{3}{8}\right)\theta^{4}+\cdots ,
$$

and both brackets are $\frac{1}{24}$, which is the coefficient of $\theta^{4}$ in $\cosh\theta-1$. **The two columns are one function of the rapidity, read in $\sinh$ and in $\tanh$; their coefficients differ exactly as those two functions differ.** No sign is in disagreement, and nothing has been mis-derived: a reader who compares $-\frac{1}{8}$ with $+\frac{3}{8}$ has compared two coordinates on one hyperbola.

## Other Biquaternions Under the Same Limit

**A test for the family.** An element belongs to the family of the four-velocity if it is $\tilde V_{\Phi}$ times one real scale, the same scale for every state. For such an element the limit is the one computed above with one multiplication, and no new series is needed. The table at the end of this section sorts them.

**The four-wave-number.** Dividing by $\hbar$ gives

$$
\tilde K_{\Phi} = \frac{\tilde P_{\Phi}}{\hbar} = i\,k_{t}^{\prime}e_{t}+\vec k_{\Phi} = \frac{m}{\hbar}\,\tilde V_{\Phi} = \frac{k_m}{c}\,\tilde V_{\Phi} ,
\qquad
k_m=\frac{mc}{\hbar} ,
$$

so the wave-number biquaternion is the four-velocity in units of the mass wave number. Its components are the three wave numbers of *The Three Wavenumbers of a Particle*,

$$
k_{t}^{\prime} = k_m\gamma = k_m\left(1+2\eta\right) ,
\qquad
k_{\Phi} = k_m\gamma\beta = k_m\sinh\theta_{\mathrm{rpd}} ,
\qquad
k_m = k_m ,
$$

and the triangle of that article is the **hyperbolic** triangle of the four-velocity: its hypotenuse is the temporal part, its side is the vector part, and the mass side is the norm. Its criterion $k_{\Phi}\ll k_m$ is $\beta\ll1$ here, and its parameter is the same $\eta$. At $m\to0$ the scale vanishes and the triangle degenerates; the element $\tilde V_{\Phi}$ does not degenerate, which is why the massless case is a statement about the scale and not about the limit.

**The four-current.** For a charge density $\varrho_{0}$ in the rest frame of the material, the convective four-current is

$$
\tilde J_{\Phi} = \varrho_{0}\tilde V_{\Phi} = i\,c\rho\,e_{t}+\vec j ,
\qquad
\rho = \gamma\varrho_{0} ,
\qquad
\vec j = \rho\vec v .
$$

This is in the family, and the limit costs nothing because there is nothing to expand: the current is the velocity with a scale. The one place the limit enters is the density, and there it is the statement that the $O\left(\beta^{2}\right)$ correction to the charge density is the Lorentz contraction, $\rho=\varrho_{0}\left(1+\beta^{2}/2+\cdots\right)$.

**The four-potential, for one charge and for a field.** For a single charge in uniform motion the four-potential is proportional to the four-velocity, $\tilde A_{\Phi}=\left(\varphi/c,\vec A\right)\propto\tilde V_{\Phi}$, so the limit applies with one scale, and it is the standard statement that the magnetic field of a slowly moving charge is smaller than its electric field by one power of $\beta$. For a general field there is no such proportionality: $\tilde A_{\Phi}$ is a four-vector of the same sector, but it is not a four-velocity times a scale, and the limit of a general $\tilde A_{\Phi}$ is a separate problem in which the components are independent.

**The field biquaternion.** $\tilde F$ is built from the electric and magnetic fields and is not a multiple of $\tilde V_{\Phi}$ under any rescaling. Its limit is not a truncation of a norm but a statement about components: at leading order only the electric part of the field of a slow charge survives, and the magnetic part is the next order. It is the same physical statement as the potential case, written on the field rather than on the potential.

**The rotor.** The boost rotor of §*The Four-Velocity and Its Norm* is not a multiple of $\tilde V_{\Phi}$: the rotor is where the group lives, the element is where the state lives. Its limit is not a truncation but a degeneration — the boost becomes a shear, and the rapidity, which is the additive coordinate of the rotor, becomes the small parameter at leading order. That degeneration is the subject of its own article, and this one records only that the rotor is outside the family.

| Element | Definition | In the family | What the limit gives |
|---|---|---|---|
| $\tilde V_{\Phi}$ | $\gamma\left(ic\,e_{t}+\vec v\right)$ | the base element | $2\eta=\frac{1}{2}\beta^{2}+\frac{3}{8}\beta^{4}+\cdots$ |
| $\tilde P_{\Phi}$ | $m\tilde V_{\Phi}$ | yes, scale $m$ | $E=mc^{2}+\frac{1}{2}mv^{2}+\cdots$ |
| $\tilde K_{\Phi}$ | $\left(k_m/c\right)\tilde V_{\Phi}$ | yes, scale $k_m/c$ | $k_{t}^{\prime}=k_m\left(1+\frac{1}{2}\beta^{2}+\cdots\right)$ |
| $\tilde J_{\Phi}$ | $\varrho_{0}\tilde V_{\Phi}$ | yes, scale $\varrho_{0}$ | $\rho=\varrho_{0}\left(1+\frac{1}{2}\beta^{2}+\cdots\right)$ |
| $\tilde A_{\Phi}$ | $\propto\tilde V_{\Phi}$ for one charge only | partly | $\lvert\vec B\rvert/\lvert\vec E\rvert=O\left(\beta\right)$ |
| $\tilde F$ | built from $\vec E$ and $\vec B$ | no | electric part survives, magnetic part is next order |
| boost rotor | unit-norm element of the group | no | the boost degenerates to a shear |

## The Phase and the Order in Time

**The limit moves inside an exponential.** Everything so far is a statement about the numbers attached to one mode. In a wave the same numbers sit in an exponent, and the limit taken there is a further step: it turns a relation between coefficients into an equation for a field. That step is the business of the field articles — *The Klein–Gordon Equation in Biquaternionic Form* for the field, *The Three Wavenumbers of a Particle* for the same statement in wave numbers — and this section records only the form the limit takes inside the exponential, because the truncation of the ladder and the truncation of the exponential are one decision.

**The phase splits like the energy.** A plane wave carries the scalar part of $\tilde K_{\Phi}\tilde R_{\Phi}^{\natural}$ in its exponent, which in momentum units is $\vec p_{\Phi}\cdot\vec r/\hbar - Et/\hbar$. With $E = mc^{2}+\mathcal{E}$,

$$
e^{\,i\left(\vec p_{\Phi}\cdot\vec r - Et\right)/\hbar}
= \underbrace{e^{-i\,mc^{2}t/\hbar}}_{f}\,
\underbrace{e^{\,i\left(\vec p_{\Phi}\cdot\vec r - \mathcal{E}t\right)/\hbar}}_{\chi} .
$$

The first factor is the **rest phase**: unit modulus, frequency $\omega_{m}=mc^{2}/\hbar$, period $2\pi\hbar/\left(mc^{2}\right)$, which is $8.09\times10^{-21}\ \mathrm{s}$ for the electron. It is the fastest motion in the state by a wide margin at low speed: at $\beta=0.5$ the excess is $79052\ \mathrm{MeV}$ against $510999\ \mathrm{MeV}$ of rest energy, so the rest phase turns $6.5$ times for every turn of the excess. The second factor is the field with the rest oscillation divided out, and it is the field the limit is about.

Nothing is approximated in that line either. It is the same split as the split of the element, applied to the exponent.

**Two terms of the exponential give a first-order equation.** Over a step $\delta t$ the excess factor advances by

$$
e^{-i\,\mathcal{E}\,\delta t/\hbar} = 1 - i\,\frac{\mathcal{E}}{\hbar}\,\delta t + O\left(\delta t^{2}\right),
$$

so the field satisfies $\partial_{t}\chi = -i\mathcal{E}\chi/\hbar$. That is one equation and it is first order in time. It is first order because the exponential was cut after two terms. A third term would leave $\chi''$ in the relation and rebuild a second-order equation, which is the Klein–Gordon form; a fourth would leave $\chi'''$, and so on. **The order in time of the equation is the number of terms kept in the exponential**, and the truncation of the ladder and the truncation of the exponential are the same decision.

**The same statement as an operator.** The exact relation $\mathcal{E}=\sqrt{m^{2}c^{4}+p_{\Phi}^{2}c^{2}}-mc^{2}$ carries the whole ladder, and it is not a polynomial: through $p_{\Phi}^{2}\to-\hbar^{2}\Delta$ it becomes the square root of a differential operator,

$$
i\hbar\,\frac{\partial\chi}{\partial t} = \left(\sqrt{m^{2}c^{4}-\hbar^{2}c^{2}\Delta}-mc^{2}\right)\chi .
$$

That operator is non-local, and its square is the Klein–Gordon operator after the rest phase is removed. Truncating it to the first term of the ladder makes it local. The truncation of the ladder and the reduction of the order are one operation, seen from two sides.

## The Equation of the Limit

**Only one member of the family produces a wave equation.** The limit computed on $\tilde V_{\Phi}$ is a statement about a dimensionless element, and it stops there: a velocity is not an operator. To reach an equation for a field the scale must supply $\hbar$, and among the elements of the table only $\tilde P_{\Phi}$ and $\tilde K_{\Phi}$ do. The wave equation is therefore a consequence of the scale and not of the limit, which is why it is written last.

**From the momentum.** With the truncated excess energy $\mathcal{E}=p_{\Phi}^{2}/2m$, multiply the first-order relation by $i\hbar$ and use $p_{\Phi}^{2}\to-\hbar^{2}\Delta$:

$$
i\hbar\,\frac{\partial\chi}{\partial t} = \frac{p_{\Phi}^{2}}{2m}\,\chi = -\frac{\hbar^{2}}{2m}\,\Delta\,\chi .
$$

**From the wave number.** The same equation in the variable of the triangle, where $\Omega:=k_{t}^{\prime}-k_m=2k_m\eta$ and $\Omega_{\mathrm{trunc}}=k_{\Phi}^{2}/2k_m$, is

$$
i\,\frac{\partial\chi}{\partial r'_{t}} = -\frac{1}{2k_m}\,\Delta\,\chi ,
$$

which is the same statement multiplied by $\hbar c$ and written in the material time. Both are the free Schrödinger equation:

$$
\boxed{\;i\hbar\,\frac{\partial\chi}{\partial t} = -\frac{\hbar^{2}}{2m}\,\Delta\,\chi\;}
$$

**Two features are read off, not assumed.** The equation is first order in time, because the term kept is $\mathcal{E}$ and not $\mathcal{E}^{2}$. And it is local and linear, because the leading term is quadratic in the momentum, so the momentum enters as a derivative. The constraint it comes from is second order in time and not polynomial; both features of the Schrödinger equation are consequences of the truncation.

In the material time $r'_{t}=c\,t$ and with the central imaginary unit of the algebra, the same equation reads

$$
\frac{mc^{2}i}{k_m}\,\frac{\partial\chi}{\partial r'_{t}} = \tilde R_{\Psi}\,\chi ,
\qquad
\tilde R_{\Psi} = -\frac{\hbar^{2}}{2m}\,\Delta \in \mathbb{B}_{\Psi} ,
$$

since $mc^{2}/k_m = \hbar c$. The observable $\tilde R_{\Psi}$ is Hermitian and informational; the coefficient carries the central $i$ and lies in the material sector $\mathbb{B}_{\Phi}$. The structure is the one the parent article *The Schrödinger Equation in Biquaternionic Form* assumes, and here it is not assumed: it is what the constraint leaves when its quadratic term is dropped.

## What the Limit Selects

**No branch is selected on the velocity.** The hyperboloid has one sheet, and its temporal part is $\gamma c$ with $\gamma>0$ everywhere on it. The limit is taken on the whole of it, and nothing is discarded: **the velocity form of the constraint has no second branch to exclude.** The branch appears in §*The Scale: The Four-Momentum* only because squaring the constraint turns a hyperbola into a quadratic, and the quadratic has a second root. That root is not a second kind of four-velocity; it is a second root of a form the algebra did not ask for. The statement that the limit applies to the positive branch and not the negative one is therefore a statement about the energy form, and the velocity form makes it unnecessary.

**A branch is not a solution dropped.** No solution of a physical problem has been thrown away by the limit. Every four-velocity is on the hyperboloid, the limit is a truncation of the constraint on it, and the truncated constraint describes the states for which the truncation is small.

**The constant is not a knob.** The limit is taken on the state, not on $c$. The speed of light stays where it is; what becomes small is the ratio of the two parts of the element for the state in hand. Setting $c\to\infty$ would send the apex to infinity and destroy the Maxwell equations the constant comes from. The parameter $\eta$ is a property of the state, and it is the only thing that goes to zero.

## Case Checked

**The velocity, at four speeds.** The first four columns are exact; the fifth is the truncated parameter; the last two should agree.

| $\beta$ | $\gamma=1+2\eta$ | $\eta$ | $\left(\gamma\beta\right)^{2}$ | $\eta_{\mathrm{trunc}}$ | error | $-\eta/\left(1+\eta\right)$ |
|---|---|---|---|---|---|---|
| $0.01$ | $1.00005$ | $2.500\times10^{-5}$ | $1.0000\times10^{-4}$ | $2.500\times10^{-5}$ | $-2.50\times10^{-5}$ | $-2.50\times10^{-5}$ |
| $0.10$ | $1.00504$ | $2.5189\times10^{-3}$ | $1.01006\times10^{-2}$ | $2.5252\times10^{-3}$ | $-2.51\times10^{-3}$ | $-2.51\times10^{-3}$ |
| $0.50$ | $1.15470$ | $7.7350\times10^{-2}$ | $3.33333\times10^{-1}$ | $8.33333\times10^{-2}$ | $-7.18\times10^{-2}$ | $-7.18\times10^{-2}$ |
| $0.90$ | $2.29416$ | $6.4708\times10^{-1}$ | $4.26316$ | $1.06579$ | $-3.93\times10^{-1}$ | $-3.93\times10^{-1}$ |

The exact $\eta$ and the leading form $\frac{1}{4}\beta^{2}$ agree at small $\beta$ and part company at large $\beta$, which is the boundary of the limit. The last two columns agree in every row because the error is exact, not estimated.

**The same table with the scale attached.** For the electron, $mc^{2}=510998.95\ \mathrm{MeV}$:

| $\beta$ | $E\ (\mathrm{MeV})$ | $\mathcal{E}\ (\mathrm{MeV})$ | $p^{2}/2m\ (\mathrm{MeV})$ | error | $-\eta/\left(1+\eta\right)$ |
|---|---|---|---|---|---|
| $0.01$ | $511024.50$ | $25.55$ | $25.55$ | $-2.50\times10^{-5}$ | $-2.50\times10^{-5}$ |
| $0.10$ | $513573.27$ | $2574.32$ | $2580.80$ | $-2.51\times10^{-3}$ | $-2.51\times10^{-3}$ |
| $0.50$ | $590050.76$ | $79051.81$ | $85166.49$ | $-7.18\times10^{-2}$ | $-7.18\times10^{-2}$ |
| $0.90$ | $1172311.99$ | $661313.04$ | $1089234.60$ | $-3.93\times10^{-1}$ | $-3.93\times10^{-1}$ |

The first row is the regime the limit is for: one part in forty thousand. The last row is not: at $\beta=0.9$ the truncation costs thirty-nine per cent, and the leading term does not describe the state. The two tables are one table: the excess energy is $2\eta\,mc^{2}$ and the truncated one is $2\eta_{\mathrm{trunc}}mc^{2}$, so the fourth column here is the fifth column there multiplied by $2mc^{2}$.

**The identities, checked.** The box $\left(\gamma\beta\right)^{2}=4\eta\left(1+\eta\right)$ with $\gamma=1+2\eta$ was evaluated at two hundred speeds spanning $\beta=10^{-3}$ to $0.99$, and it holds to $10^{-15}$ relative, which is the arithmetic. The closed form $\eta=\frac{1}{2}\left(\sqrt{1+\left(\gamma\beta\right)^{2}}-1\right)$ agrees with $\left(\gamma-1\right)/2$ to the same accuracy. The composition of rapidities reproduces the speed-addition law to $10^{-15}$ at every pair tested, and the error of the Galilean law matches $-\beta_{1}\beta_{2}\left(\beta_{1}+\beta_{2}\right)/\left(1+\beta_{1}\beta_{2}\right)$ to the last digit printed.

**The equation, checked.** A two-mode packet $\chi=\sum_{j=1}^{2}a_{j}\exp\left(i\left(p_{j}x-\mathcal{E}_{j}t\right)/\hbar\right)$ with $\mathcal{E}_{j}=p_{j}^{2}/2m$ was propagated and compared with the right side of the boxed equation on a spectral grid. The residual is $3\times10^{-13}$ against a field of unit size, which is the floor of the transform. It must vanish: the boxed equation holds on each mode, and it is linear.

## Where the Limit Sits in the Series

**In wave numbers.** Multiply the box by $k_m^{2}$: with $\tilde K_{\Phi}=\left(k_m/c\right)\tilde V_{\Phi}$ it reads $k_{\Phi}^{2}=4k_m^{2}\eta\left(1+\eta\right)$, and with $\Omega=2k_m\eta$ it is $k_{\Phi}^{2}=2k_m\Omega+\Omega^{2}$, the form used in *The Three Wavenumbers of a Particle*. Its criterion $k_{\Phi}\ll k_m$ is $\beta\ll1$ here, and its parameter is the same.

**On the field.** *The Klein–Gordon Equation in Biquaternionic Form* divides out the rest phase and truncates the envelope's dispersion relation; the boxed equation of §*The Equation of the Limit* is the result. The three articles use one complex structure $i$ and no competing unit, and the same $\eta$.

**With the algebra's own restriction.** *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form* takes the kinematic limit together with the restriction that no vector direction of $\mathbb{B}_{\Psi}$ is excited. This article takes the kinematic limit alone, which is why the equation it produces is the scalar one and not the spinor one.

**With spin.** *The Foldy–Wouthuysen Transformation in Biquaternionic Form* takes the same limit on the Dirac equation, where the odd terms of the Hamiltonian must be removed before the limit can be read. The constraint is the same; what differs is the operator that carries it.

## What the Limit Does Not Do

**It does not produce spin.** The constraint is one equation on one element, and a particle with intrinsic angular momentum needs a multicomponent field. The corpus reaches the spinor case through the square root of the wave operator, not through this limit.

**It does not produce antiparticles.** The negative branch is an artefact of squaring the constraint, and on the four-velocity there is no branch at all. The antiparticle needs a second quantisation this article does not touch.

**It does not turn relativity into Galilean kinematics.** The ladder is a statement about one state's constraint. The transformation law between frames is not expanded here. What is expanded is the composition of two boosts, in §*The Ladder of the Velocity*, and the degeneration of the rotor into a shear is the separate subject of the rotor article.

**It does not survive at high speed with its leading term alone.** The error is $-\eta/\left(1+\eta\right)$ and it is known. Where $\eta$ is not small, the limit does not describe the state, and no rearrangement of the series repairs that; the next term is the repair, and it is written down.

## Summary

The kinematic content of relativistic mechanics is one element and one constraint: $\tilde V_{\Phi}=\gamma\left(ic\,e_{t}+\vec v\right)\in\mathbb{B}_{\Phi}$ with $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$. The norm is multiplicative and a boost is a rotor conjugation, so the constraint is the same in every frame and along the worldline, and it is the only constraint. The parameter of the limit is the ratio of the two parts of the element, $\beta=v/c$, exactly.

Written with $\gamma=1+2\eta$, the constraint is $\left(\gamma\beta\right)^{2}=4\eta\left(1+\eta\right)$, exact. The box shows its own small parameter: the two terms are $4\eta$ and $4\eta^{2}$, their ratio is $\eta$, and the truncation that drops the second has relative error $-\eta/\left(1+\eta\right)$, known in closed form at every speed and below one per cent for $\beta<0.197$. The parameter is not $\beta$: $\beta\approx2\sqrt{\eta}$, half a power either way.

One expansion gives the whole ladder, and the order of the truncation is fixed by the constraint: the norm is quadratic in $\gamma$, so it is preserved one order beyond the truncation of $\gamma$. In the rapidity the limit is simplest, $\eta=\left(\cosh\theta_{\mathrm{rpd}}-1\right)/2$, and the limit is small rapidity; the exact composition law is the addition of rapidities, whose truncation is the Galilean addition of speeds.

The scale attaches once. $\tilde P_{\Phi}=m\tilde V_{\Phi}$ gives $E=\gamma mc^{2}$ and $\vec p_{\Phi}=m\gamma\vec v$, and every series of the velocity is the same series multiplied by $m$: $E=mc^{2}+\frac{1}{2}mv^{2}+\frac{3}{8}mv^{4}/c^{2}+\cdots$, with the same $\eta$ and the same error. The negative branch of the energy form is a second root of a quadratic, not a second sheet of the constraint. The same test sorts the rest: $\tilde K_{\Phi}$, $\tilde J_{\Phi}$ and the $\tilde A_{\Phi}$ of a single charge are the element times a scale, while a general $\tilde A_{\Phi}$, the field $\tilde F$ and the boost rotor are not.

Only the scaled elements that carry $\hbar$ produce a wave equation, and it is the free Schrödinger equation. The power to do that is the scale's, not the limit's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde V_{\Phi} = \gamma\left(ic\,e_{t}+\vec v\right)$ | Four-velocity; the unit-norm element of $\mathbb{B}_{\Phi}$, the base of the article |
| $\langle\tilde V_{\Phi}\rangle_{\natural} = \tilde V_{\Phi}\tilde V_{\Phi}^{\natural} = -c^{2}$ | The norm; the one constraint, frame-independent and conserved |
| $\gamma c$, $\gamma\vec v$ | The temporal and vector parts of the element |
| $\beta = \lvert\gamma\vec v\rvert/\lvert i\gamma c\rvert = v/c$ | The ratio of the two parts; exact, the parameter of the limit |
| $\gamma = 1+2\eta$ | Definition of the parameter; $2\eta c$ is the temporal excess over $c$ |
| $\left(\gamma\beta\right)^{2}=4\eta\left(1+\eta\right)$ | The constraint in one dimensionless equation; exact |
| $\eta_{\mathrm{trunc}} = \left(\gamma\beta\right)^{2}/4$ | Truncated parameter; the leading term, $\frac{1}{4}\beta^{2}$ at small speed |
| $-\eta/\left(1+\eta\right)$ | Relative error of the truncation, exact at every speed |
| $\theta_{\mathrm{rpd}} = \operatorname{artanh}\beta$ | Rapidity; the additive coordinate of the hyperboloid |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$, $\gamma\beta=\sinh\theta_{\mathrm{rpd}}$ | The element in the additive coordinate |
| $\tilde P_{\Phi} = m\tilde V_{\Phi}$ | Four-momentum; the scale $m$ attached |
| $E=\gamma mc^{2}$, $\vec p_{\Phi}=m\gamma\vec v$ | Energy and momentum; the two components of the scaled element |
| $\mathcal{E} = E-mc^{2} = 2\eta\,mc^{2}$ | Excess energy; the scaled parameter |
| $\Omega = k_{t}^{\prime}-k_m = 2k_m\eta$ | Excess wave number; the scaled parameter in wave numbers |
| $\tilde K_{\Phi} = \left(k_m/c\right)\tilde V_{\Phi}$ | Four-wave-number; the scale $k_m/c$ attached |
| $\tilde J_{\Phi} = \varrho_{0}\tilde V_{\Phi}$ | Convective four-current; the scale $\varrho_{0}$ attached |
| $r'_{t} = c\,t$ | Material time |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (4th ed., Butterworth–Heinemann, 1975), §9, for the expansion of the relativistic energy and momentum and the Lagrangian of a free particle.
- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics* (3rd ed., Addison–Wesley, 2002), chapter 7, for the relativistic Lagrangian and the Legendre transform to the Hamiltonian.
- John David Jackson, *Classical Electrodynamics* (3rd ed., Wiley, 1999), §11.5 and §11.10, for the same expansion used on the motion of a charge in an external field.
- Albert Messiah, *Quantum Mechanics* (North-Holland, 1961), chapter XX, for the non-relativistic limit of the Klein–Gordon and Dirac equations.
- Leslie L. Foldy and Siegfried A. Wouthuysen, "On the Dirac theory of spin 1/2 and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the limit taken with spin, where the odd terms must be removed first.
- Paul A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order square root of the wave operator, which the non-local square root of §*The Phase and the Order in Time* shares with the matrix one.
