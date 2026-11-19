# __Inverse Temperature as a Rapidity: Translation, Addition and the Common Bound__

## Introduction

A boost of rapidity $\theta$ along the axis of a Gibbs state sends the inverse temperature to $\beta-\theta/\lvert\vec h_\Psi\rvert$. The statement is exact, and it says that the quantity that a boost translates is not the temperature but the product of the temperature's reciprocal with the Hamiltonian magnitude. That product is dimensionless, it is additive under composition of boosts, and it is the distance from the maximally mixed state in the Klein metric of the ball. It is a rapidity.

The claim is therefore an identification of parameters and not of units. $\Theta=\beta\lvert\vec h_\Psi\rvert$ plays, in the thermal family, the role that the rapidity plays in velocity space: it labels the family, it adds under composition, and it puts the unreachable end at infinity. The temperature is recovered as $T=\lvert\vec h_\Psi\rvert/\Theta$, so the two limits a physicist is told are absolute — $T=0$ and $c$ — turn out to be the same limit of the same parameter.

The findings are stated in advance.

1. **The thermal parameter is a rapidity, and a boost translates it.** $\Theta'=\Theta-\theta$ exactly, verified to $8.0\times10^{-16}$ on thirty pairs including $\beta=0$.
2. **The family is one orbit of the centre.** From the maximally mixed state, a boost of rapidity $\Theta$ along the axis produces the Gibbs state with $\beta=\Theta/\lvert\vec h_\Psi\rvert$ and $r=\tanh\Theta$; at $\Theta=1.7$ the radius is $0.935409070603$ and $\beta$ is $1.000000000000$.
3. **The rapidity is the distance from the centre.** $\operatorname{artanh}r=\Theta$ in the Klein metric, to every digit at $0.5$, $1.7$ and $3.0$.
4. **Rapidities add.** $\mathrm{Rp}_{\theta_2}\mathrm{Rp}_{\theta_1}=\mathrm{Rp}_{\theta_1+\theta_2}$ to $7.0\times10^{-15}$ on two hundred compositions.
5. **Radii compose by the law of velocity addition and inverse temperatures add harmonically.** $\tanh 0.9$ and $\tanh 0.8$ compose to $0.935409070603=\tanh 1.7$; two contacts at $T=3$ and $T=5$ give $T=1.875=15/8$.
6. **One bound carries two names.** $r<1$ for every finite $\Theta$, so $T\to0$ and $v\to c$ are the same limit, approached as $1-r\simeq2e^{-2\Theta}$; double precision cannot distinguish $\Theta=19$ from infinity.
7. **The thermodynamics is a function of the rapidity alone.** $S$ and $C=\Theta^{2}\operatorname{sech}^{2}\Theta$ depend on $\beta$ and $\vec h_\Psi$ only through $\Theta$, and the Schottky peak sits at the universal $\Theta^{*}=1.199678640$ with $C_{\max}=0.439228840$.

The notation is that of the companions. The state is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$; the Gibbs state of the Hamiltonian $\vec h_\Psi$ is $\vec s_{\Psi}=-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$; the signed coordinate along the axis is $z=-\tanh\Theta$, with $r=\lvert z\rvert=\tanh\lvert\Theta\rvert$; the congruence is $\mathrm{Cg}_{\tilde U}:\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ and the projected map is $\mathrm{Rp}_{\tilde U}$, the congruence followed by normalisation by $2\,\mathrm{Sc}$. The thermal rapidity is $\Theta=\beta\lvert\vec h_\Psi\rvert$, signed; a boost rapidity is $\theta$. The sample value of the Hamiltonian magnitude is $\lvert\vec h_\Psi\rvert=1.7$ wherever a table needs one, and every formula is homogeneous in it.

One convention fixes the signs. With the Gibbs state at $-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$, **a boost of rapidity $\theta$ along $+\vec u_\Psi$ subtracts**: $\Theta'=\Theta-\theta$. A positive boost therefore heats the state and passes it through infinite temperature into negative temperature. The article writes the law in that form and does not re-sign it later.

## The Parameter

### Three ways to label one family

**The family has one degree of freedom and three natural labels.** The inverse temperature $\beta$ is dimensionful and ranges over the whole line; the radius $r=\tanh(\beta\lvert\vec h_\Psi\rvert)$ is dimensionless and ranges over $[0,1)$; the product $\Theta=\beta\lvert\vec h_\Psi\rvert$ is dimensionless and ranges over the whole line. The first is a reciprocal temperature, the second is a length in the ball, the third is an angle.

**The three are related by one monotone map and its inverse.** $\Theta=\beta\lvert\vec h_\Psi\rvert$, $r=\tanh\lvert\Theta\rvert$, and $\beta=\Theta/\lvert\vec h_\Psi\rvert$. Nothing else in the state varies, so the choice among them is a choice of coordinate and not of physics; what distinguishes them is how they behave under composition, and there only one of them behaves well.

**The numbers, for $\lvert\vec h_\Psi\rvert=1.7$.**

| $\Theta$ | $\beta$ | $T=1/\beta$ | $r$ | $1-r$ | $S$ (bits) | $C$ |
| --- | --- | --- | --- | --- | --- | --- |
| $0.200000$ | $0.117647059$ | $8.50000$ | $0.197375320225$ | $8.026\times10^{-1}$ | $0.971713090$ | $0.038441719$ |
| $0.500000$ | $0.294117647$ | $3.40000$ | $0.462117157260$ | $5.379\times10^{-1}$ | $0.839941538$ | $0.196611933$ |
| $1.000000$ | $0.588235294$ | $1.70000$ | $0.761594155956$ | $2.384\times10^{-1}$ | $0.527065341$ | $0.419974342$ |
| $1.199679$ | $0.705693318$ | $1.41705$ | $0.833556559522$ | $1.664\times10^{-1}$ | $0.413430615$ | $0.439228840$ |
| $1.700000$ | $1.000000000$ | $1.00000$ | $0.935409070603$ | $6.459\times10^{-2}$ | $0.205775994$ | $0.361278526$ |
| $3.000000$ | $1.764705882$ | $0.56667$ | $0.995054753687$ | $4.945\times10^{-3}$ | $0.024975106$ | $0.088794334$ |
| $5.000000$ | $2.941176471$ | $0.34000$ | $0.999909204263$ | $9.080\times10^{-5}$ | $0.000720450$ | $0.004539581$ |

**Two rows are worth reading twice.** At $\Theta=1$ the temperature is the Hamiltonian magnitude itself, $T=\lvert\vec h_\Psi\rvert$, which is the thermal analogue of the unit of rapidity: one radian of thermal displacement per unit of Hamiltonian magnitude. At $\Theta=1.199679$ the heat capacity is at its maximum while the radius is still $0.834$; the peak of the anomaly is not near the boundary.

**The row $\Theta=1.7$ is the worked example of the rest of the article.** With $\lvert\vec h_\Psi\rvert=1.7$ it is $\beta=1$ exactly, the radius is $\tanh 1.7=0.935409070603$, and the state is the one a thermal contact at unit inverse temperature produces. Every composition below is checked against this row.

### Why the rapidity is the one that composes

**A composition of boosts is a boost, and the question is which coordinate adds.** If the temperature were the additive coordinate, two thermal contacts would give the sum of the temperatures. They do not: the composition of two thermal displacements is a translation of $\beta$, and translations of $\beta$ add.

**The additive coordinate is $\Theta$.** The sections that follow verify the three consequences: it translates under a boost, it adds under composition, and the bound sits at infinity in it. Those are the three properties that define a rapidity in kinematics, and no other of the three labels has them.

## The Orbit of the Centre

### From the centre

**The maximally mixed state is the origin of the family and a boost moves it out.** A boost of rapidity $\Theta$ along $\vec u_\Psi$, applied to $\tfrac12e_t$ and projected, gives the Gibbs state at $\beta=\Theta/\lvert\vec h_\Psi\rvert$. The numbers at $\Theta=0.3$, $0.9$, $1.7$ and $3.0$ reproduce $r=\tanh\Theta$ to twelve decimals, and the recovered $\beta$ is $\Theta/\lvert\vec h_\Psi\rvert$ to twelve decimals.

**So the orbit of the centre is the family, and the family is the orbit.** The one-parameter group generated by the boost along $\vec u_\Psi$ has a one-dimensional orbit through the centre; the orbit is the diameter, both halves of it, and the parameter on it is $\Theta$. The full group has one orbit, the ball itself, because its action is transitive — that is the companion's result and the reason a transitive action cannot single out a curve. The thermal family is the orbit of the *subgroup*, it is a diameter, and its dimension is one.

**For $\Theta\ge0$ the state has non-negative temperature and the radius stands at $z=-\tanh\Theta$; for $\Theta<0$ the same formula puts the state on the other side of the centre.** There is no separate rule for negative temperature: $\Theta$ is signed, $z$ is monotone in it, and the whole line is one orbit traversed once.

### The translation law

**A boost applied to a state already off the centre simply adds to $\Theta$.** For any $\Theta$ and any $\theta$,
$$
\Theta'=\Theta-\theta ,
$$
verified to $8.0\times10^{-16}$ on thirty pairs that include $\beta=0$, $\theta=0$ and both signs of both. In the radius coordinate the same law is
$$
r'=\tanh\bigl(\Theta-\theta\bigr),
$$
and in the temperature coordinate it is $1/T'=1/T-\theta/\lvert\vec h_\Psi\rvert$.

**The law is a translation and not a scaling.** The companion on the moving frame computes the temperature an observer in relative motion reads, and the factor there is a $\gamma$: $\beta_{\mathrm{obs}}=\gamma\beta$, $T_{\mathrm{obs}}=T/\gamma$. That is a multiplication of the period by the time-dilation factor. The law here is a subtraction of the boost rapidity from the thermal rapidity. The two are different functions of $\theta$, and the article does not identify them; what it claims is the second, which is the one that composes.

### The rapidity is the distance

**The parameter that translates is the parameter that measures.** The Klein distance from the centre to the state at radius $r$ is $\operatorname{artanh}r$, and $\operatorname{artanh}(\tanh\Theta)=\Theta$. The check at $\Theta=0.5$, $1.7$ and $3.0$ returns the same three numbers to twelve decimals.

**So the thermal rapidity is the arc length travelled from the maximally mixed state.** A thermal contact of any duration moves the state along the diameter by an arc length equal to the rapidity it supplies. The temperature is then the reciprocal of that distance in units of the Hamiltonian magnitude, which is a strange way to define a temperature and the correct one for a quantity that has to compose.

## Rapidities Add, Radii Compose

### The homomorphism

**Composing two boosts composes their rapidities by addition, and the projected map respects it.** For two hundred random compositions,
$$
\bigl\lVert\mathrm{Rp}_{\theta_2}\mathrm{Rp}_{\theta_1}(\vec s)-\mathrm{Rp}_{\theta_1+\theta_2}(\vec s)\bigr\rVert=7.0\times10^{-15}.
$$
The map $\theta\mapsto\mathrm{Rp}_{\theta}$ is therefore a homomorphism from the additive line into the isometries of the ball, and on the thermal family it is injective. The family is a one-parameter subgroup orbit in the strict sense, with the group law carried by the rapidity.

**The addition is of the thermal parameter, so a sequence of contacts adds its rapidities.** Ten contacts of rapidity $1$ put the state at $\Theta=10$, that is, $\beta=5.882353$ for $\lvert\vec h_\Psi\rvert=1.7$ and $r=0.999999995878$. The bookkeeping needs no composition law for temperatures; it needs a sum.

### The velocity-addition law for radii

**The radius of the composed state obeys the law of Einstein addition.** Writing $r=\tanh\Theta$ and using the addition theorem for the hyperbolic tangent,
$$
r_{1+2}=\frac{r_1+r_2}{1+r_1r_2}.
$$
The numbers: $\tanh0.9=0.716297870$ and $\tanh0.8=0.664036770$ compose to $0.935409070603$, which is $\tanh1.7$; $\tanh1.5=0.905148254$ and $\tanh0.2=0.197375320$ compose to the same value, because $1.5+0.2=1.7$; and $\tanh0.7$ with $\tanh(-0.5)$ composes to $0.197375320$, which is $\tanh0.2$.

**So the Bloch radius is a velocity.** It is a dimensionless number in $[0,1)$, it composes by the relativistic law, and the value one plays the part of $c$. The identification is not metaphorical: the two laws are the same formula, because both are the addition theorem of $\tanh$ read on the group of boosts.

### The harmonic law for temperatures

**In the temperature variable the same law is the harmonic one.** Since $\beta=\Theta/\lvert\vec h_\Psi\rvert$ and rapidities add,
$$
\frac{1}{T}=\frac{1}{T_1}+\frac{1}{T_2},\qquad T=\frac{T_1T_2}{T_1+T_2}.
$$
Two contacts at $T=3$ and $T=5$ give $T=1.875=15/8$; the radii at those temperatures, $0.512907058$ and $0.327477395$, compose to $0.719528511$, which is $\tanh(1.7/1.875)=\tanh0.906667$.

**This is the parallel-resistor law, and it is not a curiosity.** It is what a quantity means whose reciprocal is additive: conductances add, resistances compose harmonically, and so do temperatures, when the rapidity is the additive parameter. A temperature is the reciprocal of a rapidity, and reciprocals of additive quantities always compose this way.

### Why the collinear case has no gyration

**The composition law holds because both boosts point along the same axis.** For non-collinear boosts the composition carries a Wigner rotation, and the companion computes it: the angle is $2\arctan(1/9)$ at right angles with equal moduli, and the reassociation is a gyration. Here there is no rotation, because there is one axis, and the group of boosts along a line is abelian.

**The test of the qualifier is a tilt.** Boost along the axis and the additive law holds to $3.1\times10^{-16}$; tilt the boost by $15^\circ$ and the radius departs from the prediction by $0.117$; by $45^\circ$, $0.448$; by $90^\circ$, $0.662$, at which point the state is not on the family at all and its axis has moved. **The law is a statement about the axis, and the words "along $\vec u_\Psi$" are the hypothesis, not a convenience.**

## The Bound at $T=0$ and at $v=c$

### The bound is one point of the boundary

**No finite rapidity gives $\lvert z\rvert=1$, so no finite temperature is zero.** $z=-\tanh\Theta$ is strictly inside $(-1,1)$ for every real $\Theta$, and the boundary is approached only as $\lvert\Theta\rvert\to\infty$. In the state coordinate that boundary is the pure state $\tilde\Pi(-\vec u_\Psi)$; in the temperature coordinate it is $T=0$; in the radius coordinate it is $r=1$.

**The kinematic statement is the same sentence with other words.** A velocity is $v=\tanh\theta$, it is strictly below one for every finite $\theta$, and the light-like value is approached only as $\theta\to\infty$. Since $r=\tanh\Theta$ and $v=\tanh\theta$ are the same function of their respective rapidities, the two bounds are one bound: **the boundary of the ball is the light cone of the thermal family**, and the third law and the speed limit are one statement about the range of a rapidity.

**Negative temperature is inside.** A state past the centre has $\Theta<0$ and $\lvert z\rvert<1$ still; it is on the diameter on the other side, not beyond the boundary. The bound is crossed by no path, and no sign of $\Theta$ crosses it.

### The rate

**The approach is exponential in the rapidity, with a constant that has no free parameter.** Since $1-\tanh\Theta=2e^{-2\Theta}/(1+e^{-2\Theta})$,
$$
1-r\simeq 2e^{-2\Theta}\qquad(\Theta\gg1).
$$
At $\Theta=5$ the ratio of the two sides is $0.999954602$; at $3$ it is $0.997527377$; at $7$ it is $0.999999168$. In temperature language, $T=\lvert\vec h_\Psi\rvert/\Theta$ falls like $1/\Theta$ while the distance to the boundary falls like $e^{-2\Theta}$; **the boundary is not approached in the temperature at all, it is approached in the rapidity, and the temperature is a bystander that happens to vanish.**

**The numerical floor is a diagnostic and not physics.** Double precision resolves $1-r$ down to about $10^{-16}$, which the asymptotic form reaches at $\Theta=18.767254$; beyond that $r$ is stored as exactly one. A computation that reports the pure state reached at a finite temperature has hit the floor of the arithmetic, not the boundary of the ball.

### No finite sequence

**A sequence of boosts adds its rapidities, so it reaches the bound only in the limit.** With $n$ contacts of rapidity $1$, $\Theta=n$, $r=\tanh n$ and $T=\lvert\vec h_\Psi\rvert/n$: at $n=1$ the radius is $0.761594$, at $n=5$ it is $0.999909$, at $n=10$ it is $0.999999996$. The temperature falls as $1/n$ and the distance to the boundary as $2e^{-2n}$; neither reaches its limit at any finite $n$, and both reach it at the same one.

**That is the third law in the form the rapidity gives it.** Not "zero temperature is unattainable", but "the rapidity is a sum of finite terms and the bound is at an infinite sum". The unattainability is arithmetic, and it is the same arithmetic that makes $c$ unreachable by composing velocities.

### The dictionary

| thermal | kinematic |
| --- | --- |
| $\Theta=\beta\lvert\vec h_\Psi\rvert$ | rapidity $\theta$ |
| $r=\tanh\Theta$ | $v=\tanh\theta$ |
| $T=\lvert\vec h_\Psi\rvert/\Theta$ | the reciprocal of the rapidity; no kinematic image |
| the maximally mixed state | the rest frame |
| the pure state | the light-like value |
| $T=0$ | $v=c$ |
| a thermal contact | a boost |
| $\dfrac{1}{T}=\dfrac{1}{T_1}+\dfrac{1}{T_2}$ | $v=\dfrac{v_1+v_2}{1+v_1v_2}$ |
| $S$, $C$ are functions of $\Theta$ alone | $\gamma=\cosh\theta$ is a function of $\theta$ alone |
| $\Theta\to\infty$ | $\theta\to\infty$ |

**The dictionary is a correspondence of parameters, and it stops where the analogy stops.** The thermal family has no second spatial direction, so there is no Wigner angle; the kinematic group has three, and the companion's gyration has no thermal counterpart in this article. The entries that are exact are exact; the entries that are analogies — the rest frame, the light-like value — name the two ends of one segment and are not identities of objects.

## The Thermodynamics Is a Function of the Rapidity

### Entropy and heat capacity in $\Theta$

**Every thermodynamic quantity of the two-level system is a function of $\Theta$ alone.** The partition function is $Z=2\cosh\Theta$ up to the shift $e^{\beta h_t}$, the entropy is
$$
S=\log2+\log\cosh\Theta-\Theta\tanh\Theta ,
$$
and the heat capacity is
$$
C=\Theta^{2}\operatorname{sech}^{2}\Theta .
$$
The dependence on $\beta$ and on $\lvert\vec h_\Psi\rvert$ has collapsed into the one product, so two systems with different Hamiltonians at temperatures chosen so that $\beta_1\lvert\vec h_{\Psi,1}\rvert=\beta_2\lvert\vec h_{\Psi,2}\rvert$ have identical thermodynamics. **The rapidity is the only thing the equilibrium state knows.**

**The check is a substitution.** At $\beta=1$ and $\lvert\vec h_\Psi\rvert=1.7$ the two-level formula $(\beta\Delta)^{2}e^{\beta\Delta}/(1+e^{\beta\Delta})^{2}$ with $\Delta=2\lvert\vec h_\Psi\rvert$ returns $0.361278526$, and $\Theta^{2}\operatorname{sech}^{2}\Theta$ returns $0.361278526$; the entropy in bits is $0.205775994$, and the linear entropy is $\tfrac14\operatorname{sech}^{2}1.7=0.031252468$.

**The limits are the ends of the segment.** As $\Theta\to0$, $S\to\log2$ and $C\to0$; as $\Theta\to\infty$, $S\to0$ and $C\to0$. The entropy is monotone in $\lvert\Theta\rvert$ and the heat capacity is not.

### The universal Schottky peak

**The heat capacity peaks at a rapidity that no parameter can move.** Differentiating $C=\Theta^{2}\operatorname{sech}^{2}\Theta$ gives the condition $\tanh\Theta=1/\Theta$, whose root is
$$
\Theta^{*}=1.199678640,\qquad C_{\max}=0.439228840 .
$$
The values at $\Theta=1$ and $\Theta=2$ are $0.419974342$ and $0.282603299$, so the peak is sharp on the high side and shallow on the low side. The temperature at the peak is $T=\lvert\vec h_\Psi\rvert/1.199679$, which is $1.41705$ for $\lvert\vec h_\Psi\rvert=1.7$.

**The number is universal and the temperature is not.** The peak sits at the same rapidity for every two-level system, whatever its gap and whatever its units; the temperature at which that happens scales with the gap, and a table of peak temperatures across systems that omits the gap is a table of unit conversions. **The statement that is invariant is the statement in $\Theta$**, and that is the practical content of the identification.

**The peak also marks where the ball is still far from its boundary.** At $\Theta^{*}$ the radius is $0.833557$, a sixth of the way from one; the anomaly is a property of the interior and not of the approach to the pure state. Reading the Schottky peak as a boundary effect is the error the rapidity coordinate prevents.

## Objections

**The objection is that a temperature is not a rapidity, because a rapidity is a boost and a temperature is not.** The objection is right about the objects and wrong about the claim. The claim is that $\Theta=\beta\lvert\vec h_\Psi\rvert$ is the parameter of the family, that a boost translates it, that it adds, and that its bound is at infinity; those four properties are what the word rapidity names, and the article verifies them and does not assert anything more.

**A second objection is that the corpus already has a temperature transformation, $T/\gamma$, and the two disagree.** They do disagree as functions of $\theta$: the period of the thermal element multiplies by $\gamma$, while the thermal rapidity is translated. The answer is that they are transformations of different objects. $T/\gamma$ is what a moving observer reads from the temporal component of the thermal element, $\beta_{\Phi,t}=i\beta\gamma$; the translation is what the state does when it is carried by the projected congruence. The discriminating test is composition: $\gamma_1\gamma_2\neq\gamma_{12}$, so $\beta\gamma$ is not a group coordinate, while $\Theta-\theta$ is. **Only the additive one deserves to be called the parameter of the family**, and the article claims that one.

**A third objection is that the identification is empty because any monotone coordinate can be declared additive by declaring its logarithm.** The answer is that $\Theta$ is additive under the *group action that exists*, not under a reparametrisation chosen to make it so. The boost is given, its rapidity is given, and the law $\Theta'=\Theta-\theta$ is a fact about that boost, verified to $8.0\times10^{-16}$. A coordinate that is additive under a given action is a strong statement; any coordinate is additive under some relabelling.

## What Is Not Claimed

**It does not identify temperature with rapidity as quantities.** $T$ has the dimensions of $\lvert\vec h_\Psi\rvert$ and is the reciprocal of $\Theta$; what is a rapidity is the product $\beta\lvert\vec h_\Psi\rvert$, which is dimensionless. The title names the parameter, not the quantity.

**It does not claim that the thermal family is a geodesic submanifold of the ball in the Riemannian sense beyond the diameter.** It is a diameter: one dimension, straight, and a geodesic of both metrics, as the companion proves. No higher-dimensional thermal family is treated.

**It does not settle the moving-frame temperature.** The companion computes $T/\gamma$ from the period; this article computes the translation of $\Theta$ from the state. The relation between the two is a question about which object an observer's thermometer couples to, and it is left open here on purpose.

**It does not extend the composition law off the axis.** The law requires both boosts along $\vec u_\Psi$; the tilt test shows the failure and the Wigner companion supplies the correction.

## Summary

**$\Theta=\beta\lvert\vec h_\Psi\rvert$ is the rapidity of the thermal family.** A boost along the axis translates it, $\Theta'=\Theta-\theta$, to $8.0\times10^{-16}$; from the centre a boost of rapidity $\Theta$ produces the Gibbs state at $\beta=\Theta/\lvert\vec h_\Psi\rvert$ exactly; and the parameter is the Klein distance from the maximally mixed state, $\operatorname{artanh}r=\Theta$.

**The family is the orbit of the centre under the one-parameter group of boosts along the axis.** It is one-dimensional inside a ball on which the full group acts transitively; the subgroup orbit is the diameter, and the parameter on it is the rapidity.

**Rapidities add and radii compose.** $\mathrm{Rp}_{\theta_2}\mathrm{Rp}_{\theta_1}=\mathrm{Rp}_{\theta_1+\theta_2}$ to $7.0\times10^{-15}$; the radii obey $r_{1+2}=(r_1+r_2)/(1+r_1r_2)$, and the temperatures obey $1/T=1/T_1+1/T_2$, so two contacts at $3$ and $5$ give $1.875$. The law needs the axis: at $45^\circ$ the prediction is off by $0.448$.

**The bound is one point with two names.** $r<1$ for every finite $\Theta$, with $1-r\simeq2e^{-2\Theta}$, so $T=0$ and $v=c$ are the same limit, reached by no finite sum of rapidities; double precision flattens the difference at $\Theta=18.767254$.

**The thermodynamics is a function of $\Theta$ alone**, including the heat capacity $\Theta^{2}\operatorname{sech}^{2}\Theta$ and its universal peak at $\Theta^{*}=1.199678640$, $C_{\max}=0.439228840$. The temperature at which a system peaks is a unit conversion; the rapidity at which it peaks is not.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\beta$ | the inverse temperature |
| $\lvert\vec h_\Psi\rvert$ | the magnitude of the Hamiltonian; $1.7$ in the tables |
| $\Theta=\beta\lvert\vec h_\Psi\rvert$ | the thermal rapidity, signed |
| $\theta$ | the rapidity of a boost |
| $z=-\tanh\Theta$ | the signed coordinate of the state along the axis |
| $r=\lvert z\rvert$ | the radius, the modulus of the state vector |
| $T=1/\beta=\lvert\vec h_\Psi\rvert/\Theta$ | the temperature |
| $\mathrm{Rp}_{\tilde U}$ | the congruence followed by normalisation |
| $\Theta^{*}$ | the rapidity of the heat-capacity maximum, $1.199678640$ |
| $C=\Theta^{2}\operatorname{sech}^{2}\Theta$ | the heat capacity of the two-level system |

## Further Reading

- A. Sommerfeld, "Über die Zusammensetzung der Geschwindigkeiten in der Relativtheorie", *Physikalische Zeitschrift* **10** (1909) 826–829 — the composition of velocities and the parameter that linearises it
- A. A. Ungar, *Analytic Hyperbolic Geometry and Albert Einstein's Special Theory of Relativity*, World Scientific, 2008 — the velocity ball, rapidity additivity and the gyrogroup
- J. A. Rhodes and M. D. Semon, "Relativistic velocity space, Wigner rotation, and Thomas precession", *American Journal of Physics* **72** (2004) 943–960 — the metric of velocity space and the non-collinear correction
- W. Rindler, *Relativity: Special, General and Cosmological*, 2nd ed., Oxford University Press, 2006 — rapidity, its additivity and the velocity-addition law
- N. F. Ramsey, "Thermodynamics and statistical mechanics at negative absolute temperatures", *Physical Review* **103** (1956) 20–28 — negative temperature as a point of the same family and not beyond the bound
- C. Kittel and H. Kroemer, *Thermal Physics*, 2nd ed., W. H. Freeman, 1980 — the two-level system, its entropy and its Schottky anomaly
- R. K. Pathria and P. D. Beale, *Statistical Mechanics*, 3rd ed., Elsevier, 2011 — the same, with the maximum of $C$ at $\beta\Delta/2=1.1997$
- H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, 2nd ed., Wiley, 1985 — reciprocals of intensive parameters and how they compose
- *The Gibbs Path Is Not a Group Orbit* — the family as a diameter, the two metrics and the affinity test
- *The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics* — the ball as the Klein model and $2\,\mathrm{Sc}$ as the running quantity
- *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* — the Klein metric, its geodesics and the boundary at infinity
- *Quantum Thermodynamics in Biquaternionic Form* — the Gibbs state, the potentials and the low- and high-temperature limits
- *The Wigner Angle of Two Boosts* — the Wigner rotation that the collinear case does not have
