# __Time from the Algebra: Clock, Rate and Period__

## Introduction

The biquaternion algebra does not contain a time coordinate. It contains the structures from which a time coordinate can be read: the roots of $-1$, the one-parameter groups they generate, the Fourier kernel that ties a root to a frequency, and the two real slices on which the scalar coefficient becomes a clock. The article states those structures and reads them physically. It does not derive a direction of time, a rate, or a dynamics.

The central statement is that **a clock is a root of $-1$**. An element $\rho$ with $\rho^2=-e_t$ generates the rotation

$$
e^{\theta\rho}=\cos\theta\,e_t+\sin\theta\,\rho,
$$

which is periodic with period $2\pi$ in $\theta$. The root chooses the plane of the rotation; the parameter $\theta$ is the reading of the clock; the frequency is the rate at which the parameter advances. The algebra supplies the root and the group. It does not supply a preferred root, a preferred parameter, or a preferred origin.

The article develops five readings: the root as a clock, the Fourier kernel as the clock–frequency pair, the two sector times, the gauge ambiguity of the generator and the parameter, and the thermal clock of a state. It closes with the limits of the metaphor.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The roots of $-1$ and the exponential | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The three families of roots and the Fourier kernel | [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html) |
| The logarithm, the branch lattice and the generator | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html), §*The Logarithm* |
| The material and informational slices | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) |
| The local complex structure and the speed of light | [The Local Complex Structure and the Speed of Light](the-local-complex-structure-and-the-speed-of-light.html) |
| The generator as a gauge | [Generators, Periods and the Boundary of Evolution](the-exponential-the-logarithm-and-the-generator.html) |
| The no-clock theorem of the probability band | [The Probability Band: No Clock, Three Species and the Geometric Phase](the-probability-band-no-clock-three-species-and-the-geometric-phase.html) |
| The modular flow of a state | [Thermality from the Modular Pair](thermality-from-the-modular-pair-state-clock-and-the-definite-reading.html) |

## A Clock Is a Root of $-1$

### The Root

A root of $-1$ is an element $\rho\in\mathbb{B}$ with

$$
\rho^2=-e_t.
$$

The exponential is the rotation in the plane spanned by $e_t$ and $\rho$:

$$
e^{\theta\rho}=\cos\theta\,e_t+\sin\theta\,\rho,
\qquad
e^{(\theta+2\pi)\rho}=e^{\theta\rho}.
$$

The period is $2\pi$ in the parameter. The root is the clock: it fixes the plane, the orientation and the unit of the phase. The parameter is the clock reading, and the frequency is its rate.

The roots fall into three families:

| family | form | square | reading |
| --- | --- | --- | --- |
| central | $\rho=\pm i e_t$ | $-e_t$ | a global phase, no direction |
| spatial | $\rho=\pm\hat\mu$, $\hat\mu$ a real unit pure quaternion | $-e_t$ | a rotation about an axis |
| mixed | $\rho=b\hat\mu+d\hat\nu i$, $b^2-d^2=1$ | $-e_t$ | a rotation in a tilted plane |

The central root commutes with the algebra and acts as a scalar on every module. The spatial root is a pure real quaternion and generates a rotation of the material vector. The mixed root combines the two. The three families are not equivalent, and the choice among them is the first clock choice.

### The Period Is the Only Observable

The parameter is not observable; the period is. A clock is a map from the parameter to the group, and only the return matters:

$$
\theta\longmapsto e^{\theta\rho},
\qquad
e^{2\pi\rho}=e_t.
$$

A rescaling of the parameter, $\theta\mapsto c\theta$ with $c>0$, gives the same subgroup read at a different rate. The algebra does not distinguish the two readings. The clock is the subgroup together with a period; the numerical value of the period is a unit convention.

The reading is austere: the algebra gives a periodic group, not a ticking device. A clock measures the parameter by counting returns; the returns are in the algebra, the count is not.

## The Fourier Kernel: Clock and Frequency

### The Kernel

Fix a root $\rho$ and a frequency $\omega$. The Fourier kernel is

$$
W(t',\omega)=\exp(-2\pi\rho\,\omega t')
=\cos(2\pi\omega t')\,e_t-\sin(2\pi\omega t')\,\rho.
$$

It is a rotation in the plane of the root, with period $1/\omega$ in $t'$. The root is the clock; the frequency is the rate; the kernel is the pair. The inverse is the same expression with the sine reversed:

$$
W(t',\omega)^{-1}=\cos(2\pi\omega t')\,e_t+\sin(2\pi\omega t')\,\rho.
$$

The identity $WW^{-1}=e_t$ uses only $\rho^2=-e_t$. For a pure root the kernel is unitary, $W^{\natural}=W^{-1}$; for the central root it is the complex scalar $e^{\mp2\pi i\omega t'}$.

### The Reading

The kernel is the precise form of the clock–frequency relation. A frequency is not an independent object: it is the rate at which the root is traversed. The pair $(t',\omega)$ is a coordinate pair on the same plane, and the kernel is the bridge.

The choice of root changes the transform. The central root gives the complex Fourier transform; a spatial root gives a quaternionic transform with a non-commutative kernel; a mixed root gives a tilted transform. The transforms are different, and the difference is the clock choice. The algebra does not select one.

The vanishing-norm issue is the boundary. On the null cone the kernel can have zero norm, and the transform is not unitary; the clock is degenerate where the element is a zero divisor. The clock interpretation is licensed on the unit group, not on the cone.

## The Two Sector Times

### The Two Coefficients

The algebra has one complex scalar coefficient $Q_t$, and the two real slices read it in two ways:

$$
\mathbb{M}_-:\quad Q_t=i c\,t',
\qquad
\mathbb{M}_+:\quad Q_t=c\,t.
$$

On the material slice, the time coordinate is the imaginary part of $Q_t$; on the informational slice, it is the real part. The same complex number carries both: $Q_t=c(t+it')$. The two times are not two dimensions; they are the two real readings of one complex coefficient.

The norm reads the two:

$$
N=-c^2t'^2+\lvert\vec x\rvert^2
\quad\text{on }\mathbb{M}_-,
\qquad
N=c^2t^2-\lvert\vec x'\rvert^2
\quad\text{on }\mathbb{M}_+.
$$

The material time is the one that enters the interval with a minus sign; the informational time is the one that enters with a plus sign. The sign is the sector, not a convention.

### The Wick Rotation

The two slices are exchanged by

$$
t'\longleftrightarrow -i t,
\qquad
\vec x\longleftrightarrow i\vec x',
$$

which is a Wick rotation. The reading is that the material clock and the informational clock are the same complex coefficient read on two real slices. A Wick rotation is a change of which real part is called time; it is not a physical process in the algebra.

The local complex structure is the choice. The article *The Local Complex Structure and the Speed of Light* states that no global complex structure compatible with the Minkowski metric exists on spacetime, but a local one does, and that the speed of light is the single scale that converts the local structure into the Minkowski metric. The choice of slice is the choice of clock. The algebra has no preferred slice, and therefore no preferred time.

### The Central Root Is Not a Sector Time

The central root $\pm i$ generates the phase $e^{i\theta}$. It is a clock, but it is not a sector time: it commutes with the algebra, acts as a scalar, and cannot separate the material and informational coordinates. The sector times are the two real readings of the same coefficient, not two central phases. The central phase is the global gauge, and the sector time is the coordinate.

## No Canonical Clock

### The Generator Is a Coordinate

A generator of a unit $\tilde U$ is an element $\tilde L$ with $\exp\tilde L=\tilde U$. The one-parameter group is $\exp(t\tilde L)$, and the generator is the logarithm. The logarithm is multivalued, and the ambiguity is the clock ambiguity:

| layer | shift | what it changes |
| --- | --- | --- |
| central phase | $2\pi i k\,e_t$ | nothing observable |
| full rotation | $2\pi j\,\vec U$ | nothing; a full turn is the identity |
| parity-matched pair | $\pi i\,e_t+\pi\,\vec U$ | nothing; the two half-shifts cancel |

The first layer is the global phase; the second is a full rotation of the generator; the third couples the two. The kernel is not a subgroup, and the set of generators is not a coset of it. The generator is a coordinate on the group, not an element attached to the process.

### The Parameter Is a Gauge

The parameter is defined up to a positive rescaling: $\exp(t(c\tilde L))=\exp((ct)\tilde L)$. The subgroup is the same, and the clock is read at a different rate. The algebra gives the subgroup; the parameter is a gauge choice. This is the generator-is-a-gauge statement read on the parameter instead of on the element.

### The Reading

Time is a coordinate on a one-parameter subgroup. The subgroup is algebraic; the coordinate is not. The algebra supplies the ordering along the parameter and the sign of the generator, which distinguishes the two directions. It does not supply a canonical normalisation, a canonical origin, or a canonical choice among generators.

The reading is not that time is illusory. It is that time is a coordinate, and a coordinate needs a gauge. The physical content is the subgroup and its periods; the coordinate is the description.

## The Period Lattice and the Holonomy

The logarithm's branch lattice is the topology of the clock. A closed path in the parameter space returns to the same element with a phase; the phase is the holonomy, and the holonomy is the clock's memory. The geometric phase of the probability band is the same structure read on the state space: a closed path in the ray space returns with a phase that depends on the path, not on the rate.

The reading is that a clock has a period and a memory. The period is the return; the memory is the holonomy. The algebra supplies both, and neither is a time coordinate: the period is a property of the subgroup, and the holonomy is a property of the path.

## The Thermal Clock

A thermal state supplies a clock that the algebra alone does not. The modular flow of a state is a one-parameter group, and the KMS condition is periodicity in imaginary time with period $\beta$. The modular Hamiltonian is the generator, and the temperature is the inverse period.

The biquaternion algebra supplies a definite modular pair: the Tomita operator is the star, the modular operator is the identity, and the flow is trivial for the trace state. The trace state has no thermal clock. A non-tracial state would give a non-trivial modular operator, and the clock would be the state's, not the algebra's. The reading is developed in *Thermality from the Modular Pair*.

The thermal clock is therefore a second layer: the algebra gives the one-parameter groups, and the state selects one as the modular flow. The temperature is the period of that flow, not a property of the algebra.

## Physical Interpretations

- **A clock is a root of $-1$.** The root fixes the plane and the period; the parameter is the reading. The three families of roots give the global phase, the spatial rotation and the tilted rotation.
- **The Fourier kernel is the clock–frequency pair.** A frequency is the rate at which the root is traversed; the kernel is the bridge. The choice of root changes the transform.
- **The two sector times are two readings of one coefficient.** $Q_t=c(t+it')$: the material time is the imaginary part, the informational time the real part. The Wick rotation exchanges them.
- **The central root is a global phase, not a sector time.** It commutes with the algebra and cannot separate the sectors. The sector time is the coordinate; the central phase is the gauge.
- **There is no canonical clock.** The generator is defined up to the kernel, and the parameter up to a positive rescaling. Time is a coordinate on a one-parameter subgroup; the subgroup is algebraic, the coordinate is not.
- **The period is the observable.** Only the return is invariant; the numerical period is a unit convention. A clock measures by counting returns.
- **The period lattice is the topology of the clock.** The branch ambiguity of the logarithm is the clock's memory; the holonomy is the phase of a closed path.
- **The thermal clock is the state's.** The algebra's trace state has a trivial modular flow; a non-tracial state gives a non-trivial one. Temperature is the period of the modular flow, not a property of the algebra.

## Limits

The clock reading is licensed on the unit group. On the null cone the kernel can have zero norm and the clock is degenerate; the zero divisors have no logarithm and no generator.

The central root is a phase, not a time coordinate. The sector times are the two real readings of the complex coefficient, not two central phases.

The algebra does not supply a direction of time. It supplies the ordering along a parameter and the sign of the generator; the arrow is an extra choice.

The algebra does not supply a rate or a unit. The period is $2\pi$ in the parameter, and the numerical value is a convention.

The thermal clock is not derived. The trace state has a trivial flow; a non-trivial flow needs a non-tracial state and a modular pair, and the temperature is an input.

No dynamics is supplied. The article reads the clocks the algebra carries; it does not say which one a physical system uses.

## Summary

- A clock is a root of $-1$: $\rho^2=-e_t$ generates $e^{\theta\rho}$ with period $2\pi$. The root fixes the plane; the parameter is the reading.
- The roots fall into three families: central (global phase), spatial (rotation about an axis), mixed (tilted rotation). The choice is a gauge.
- The Fourier kernel $\exp(-2\pi\rho\omega t')$ ties the root to the frequency; the period is $1/\omega$.
- The two sector times are the real and imaginary readings of $Q_t$: $Q_t=c(t+it')$. The Wick rotation exchanges them; the sign of the norm is the sector.
- The central root is a global phase, not a sector time; it commutes with the algebra and cannot separate the sectors.
- The generator is defined up to the central phase, the full rotation and the parity-matched pair; the parameter is defined up to a positive rescaling. There is no canonical clock.
- The period is the observable; the period lattice is the topology of the clock; the holonomy is its memory.
- The thermal clock is the modular flow of a state; the trace state has a trivial flow, a non-tracial state a non-trivial one. Temperature is the period.
- The algebra supplies the groups and the periods; it supplies no direction, no rate, no unit and no dynamics.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\rho$ | a root of $-1$, $\rho^2=-e_t$ |
| $\theta$ | the clock parameter, period $2\pi$ |
| $W(t',\omega)=e^{-2\pi\rho\omega t'}$ | the Fourier kernel |
| $\omega$ | the frequency, the rate of the clock |
| $Q_t=c(t+it')$ | the complex scalar coefficient and the two sector times |
| $\tilde L$ | a generator, $\exp\tilde L=\tilde U$ |
| $\beta$ | the KMS period, the inverse temperature |
| $\sigma_t$ | the modular flow of a state |

## Further Reading

- [Generators, Periods and the Boundary of Evolution](the-exponential-the-logarithm-and-the-generator.html), for the logarithm, the branch lattice and the generator as a gauge.
- [The Probability Band: No Clock, Three Species and the Geometric Phase](the-probability-band-no-clock-three-species-and-the-geometric-phase.html), for the no-clock theorem and the holonomy.
- [The Local Complex Structure and the Speed of Light](the-local-complex-structure-and-the-speed-of-light.html), for the two slices and the Wick rotation.
- [Thermality from the Modular Pair](thermality-from-the-modular-pair-state-clock-and-the-definite-reading.html), for the thermal clock.
- [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html), for the Fourier kernel and its roots.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the material time.
