# __The Massless Limit as a Boundary Value of the Polar Word__

## Introduction

The polar word is a parametrization of the group of units: every biquaternion off the zero-divisor cone is an ordered product of a scale, a central phase, a boost and a rotor. The massless shell is the cone. The massless limit is therefore not an interior limit of the word's parameters; it is the limit in which the element reaches the boundary of the group, where the word has no value.

This article owns that limit. It states the boundary value of the four-factor word along a path of infinite rapidity, identifies the two strata on which the limit can land, and records what the limit does and does not inherit from the massive element. The boundary theorem, the two strata and the exponential convergence are those of *Exponential Polar Decomposition of Biquaternions*. The stratum table and the element-level reading of the cone are those of *The Zero-Divisor Cone and the Massless Spectrum* and *The Exponential Word and Its Boundary*. What is added here is the massless question: which massive family has which boundary value, where the mass enters, and why the answer is a boundary value rather than a value.

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\mathrm b}=\exp\left(i\frac{\psi}{2}\vec u_{\mathrm b}\right),
\qquad
\tilde u_{\mathrm r}=\exp\left(\frac{\theta}{2}\vec u_{\mathrm r}\right),
$$

with $r>0$, $\alpha\in(-\pi/2,\pi/2]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ unit real pure quaternions. The norm is $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$, and the element is a unit exactly when $r\neq0$. The material four-momentum is

$$
\tilde P=i\frac{E}{c}e_t+\vec p,
\qquad
E=mc^2\cosh\psi,
\qquad
\lvert\vec p\rvert=mc\sinh\psi,
$$

with $\vec u_p=\vec p/\lvert\vec p\rvert$ and $\langle\tilde P\rangle_{\natural}=-m^2c^2$.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The four factors, their ranges and the uniqueness of the word | [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html) |
| The boundary theorem, the two strata and the rate | [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html) |
| The logarithm, the kernel and the exponential image | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The norm, its multiplicativity and the group of units | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| The minimal idempotents and the pure roots of $+1$ | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| The nilpotents, their index and their square-zero property | [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](../articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html) |
| The cone, its two strata and the mass shell | [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html) |

## The Word and the Mass Shell

The four factors carry the eight real parameters of the algebra.

| # | Factor | Name | Exponent | Range | Real dimension |
| --- | --- | --- | --- | --- | --- |
| 1 | $r$ | scale | — | $r>0$ | $1$ |
| 2 | $e^{i\alpha}$ | central phase | $i\alpha$ | $\alpha\in(-\pi/2,\pi/2]$ | $1$ |
| 3 | $\tilde U_{\mathrm b}$ | boost | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\psi\ge0$ | $3$ |
| 4 | $\tilde u_{\mathrm r}$ | rotor | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$ | $3$ |

The norm of the word is

$$
\langle\tilde Q\rangle_{\natural}=r^2e^{2i\alpha},
$$

so the cone is the locus $r=0$ and the mass shell is the level set $r^2e^{2i\alpha}=-m^2c^2$. The mass is a radial coordinate of the word, not one of its angles. The word is defined exactly on the complement of the cone, and the massless limit is the limit $r\to0$, which is not a point of the domain.

The boost grows with the rapidity,

$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}
=\frac{e^{\psi/2}}{2}\left(e_t+i\vec u_{\mathrm b}\right)
+\frac{e^{-\psi/2}}{2}\left(e_t-i\vec u_{\mathrm b}\right),
$$

so a collapsing scale and a diverging rapidity can compensate. That compensation is the whole content of the boundary value.

## The Limit at Infinite Rapidity

Take a unit complex number $\zeta$, a positive real $R$, and the family

$$
\tilde Q(\psi)=R\,e^{-\psi/2}\,\zeta\,\tilde U_{\mathrm b}(\vec u_{\mathrm b})\,\tilde u_{\mathrm r},
\qquad
\psi>0.
$$

Each member is a unit, because $R e^{-\psi/2}>0$, and the norm is

$$
\langle\tilde Q(\psi)\rangle_{\natural}=R^2e^{-\psi}\zeta^2.
$$

Insert the two-term form of the boost. The family splits into a constant term and a term of order $e^{-\psi}$:

$$
\tilde Q(\psi)
=\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r}
+\frac{R\zeta}{2}\,e^{-\psi}\left(e_t-i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r}.
$$

The limit therefore exists, and it is

$$
\boxed{\;L=\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r}\;}.
$$

The convergence is exponential in the rapidity, with the second term of order $e^{-\psi}$. The limit is nonzero, since $(e_t+i\vec u_{\mathrm b})\tilde u_{\mathrm r}\neq0$, and it lies on the cone, since

$$
\left(e_t+i\vec u_{\mathrm b}\right)^2=2\left(e_t+i\vec u_{\mathrm b}\right)
\quad\Longrightarrow\quad
\langle L\rangle_{\natural}=0.
$$

The limit is a rank-one null element. It is not a value of the word: $L$ is not a unit, and the word is defined only on the units.

**The finite part is the direction of the boost.** The diverging factor is the magnitude $e^{\psi/2}$; the direction $e_t+i\vec u_{\mathrm b}$ survives. The boundary value remembers the axis of the boost and the rotor, and forgets the rapidity. That is why the limit is a point of the cone and not a Lorentz transformation.

## The Two Strata

The rotor decides which stratum the limit reaches. Decompose it in the frame of the boost axis,

$$
\tilde u_{\mathrm r}=a\,e_t+b\,\vec u_{\mathrm b}+\tilde u_\perp,
\qquad
a,b\in\mathbb{R},
\qquad
\tilde u_\perp\ \text{orthogonal to}\ \vec u_{\mathrm b}.
$$

The scalar part of the limit is

$$
\operatorname{Sc}L=\frac{R\zeta}{2}\left(a-ib\right),
$$

and the square is

$$
\boxed{\;L^2=\tau L,
\qquad
\tau=2\operatorname{Sc}L=R\zeta\left(a-ib\right)\;}.
$$

The two cases follow from $\tau$.

| Rotor condition | Scalar part | Normal form | Stratum | Real dimension |
| --- | --- | --- | --- | --- |
| $a-ib\neq0$ | $\dfrac{R\zeta}{2}(a-ib)\neq0$ | $L=\tau P$, $P^2=P$, $\operatorname{Sc}P=\tfrac12$ | idempotent | $6$ |
| $a-ib=0$, that is $a=b=0$ | $0$ | $L^2=0$, $L\neq0$ | nilpotent | $4$ |

In the first row $L$ is a nonzero complex multiple of a minimal idempotent: $P=L/\tau$ satisfies $P^2=P$ and has scalar part $1/2$. In the second row $\tilde u_{\mathrm r}=\tilde u_\perp$ anticommutes with $\vec u_{\mathrm b}$ and has zero scalar part, and

$$
\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_\perp
$$

squares to zero, so $L$ is a nonzero nilpotent. The two rows are disjoint, and the scalar part distinguishes them pointwise. They are the two strata of the cone: the idempotent stratum is open and dense, and the nilpotent stratum is a closed subvariety of codimension two.

The classification was checked on sixty random samples of the data, with the predicted stratum and the computed trace agreeing in every case to machine precision, and on a targeted nilpotent sample with $\tilde u_\perp$ orthogonal to the boost axis, where $L^2=0$ and $\langle L\rangle_{\natural}=0$ held to $10^{-16}$.

**The rate is the same for both strata.** The splitting of the family is $O(e^{-\psi})$ in either row; what differs is the direction of the residual, not its rate. The stratum is selected by the orientation of the rotor relative to the boost, not by a slower or faster approach.

## The Massless Momentum

The physical family is the four-momentum written in the word. In this section $\psi$ is the rapidity of the momentum, not the word rapidity of the preceding section, and $\psi_w=2\psi$ is the word rapidity. Set

$$
r=mc,
\qquad
\zeta=i,
\qquad
\vec u_{\mathrm b}=-\vec u_p,
\qquad
\tilde u_{\mathrm r}=e_t,
\qquad
\psi_w=2\psi,
$$

where $\psi$ is the rapidity of the momentum and $\psi_w$ is the rapidity parameter of the word. The factor two is the difference between multiplying once and acting twice: the word multiplies the element once, while the Lorentz boost carries the rest momentum $\tilde P_0=imc\,e_t$ to $\tilde P$ through the half-angle rotor $\tilde U_{\mathrm b}(\psi)$, $\tilde P=\tilde U_{\mathrm b}(\psi)\tilde P_0\tilde U_{\mathrm b}(\psi)^{*}=\tilde U_{\mathrm b}(\psi)^{2}\tilde P_0$. The word's boost factor is that square, $\tilde U_{\mathrm b}(\psi_w)=\tilde U_{\mathrm b}(\psi)^{2}$, so $\psi_w=2\psi$. With these data,

$$
r\zeta\,\tilde U_{\mathrm b}(\psi_w)\tilde u_{\mathrm r}
=imc\left(\cosh\psi\,e_t-i\sinh\psi\,\vec u_p\right)
=i\frac{E}{c}e_t+\vec p
=\tilde P.
$$

The rate of the family is

$$
r\,e^{\psi_w/2}=mc\,e^{\psi}=2\frac{E}{c}-mc\,e^{-\psi},
$$

so $r e^{\psi_w/2}\to R$ with $R=2E/c$, and the relative defect is $e^{-2\psi}=O(m^2c^4/E^2)$ at fixed energy. The massless limit of the momentum therefore satisfies the finiteness condition automatically, and the coefficient is the energy.

The boundary value is the massless momentum:

$$
\boxed{\;L=\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)
=\frac{iE}{c}\left(e_t-i\vec u_p\right)
=i\frac{E}{c}e_t+\frac{E}{c}\vec u_p
=2i\frac{E}{c}\,\tilde\Pi(-\vec u_p)\;},
$$

with $\tilde\Pi(-\vec u_p)=\tfrac12(e_t-i\vec u_p)$ the Hermitian minimal idempotent along the direction opposite to the motion. The limit is an imaginary multiple of a Hermitian idempotent: a null four-momentum, not a nilpotent.

| Quantity | Massive | Massless limit |
| --- | --- | --- |
| element | $\tilde P$, a unit | $L$, a rank-one null element |
| norm | $-m^2c^2$ | $0$ |
| scale | $r=mc$ | $0$ |
| rapidity | $\psi<\infty$ | $+\infty$ |
| rest frame | exists at $\psi=0$ | does not exist |
| logarithm | exists | does not exist |

**The defect is of order $m^2$.** The approach to the boundary is $O(e^{-2\psi})=O(m^2c^4/E^2)$ at fixed energy. The massive momentum itself carries the same order in its algebraic defect, $\tilde P^2=2P_t\tilde P+m^2c^2e_t$, so the massless relation $\tilde P^2=2P_t\tilde P$ is the boundary identity and the mass term is the defect. The two statements are of the same order in the mass; they are not the same statement, one being a defect of the element and the other a defect of the path.

**The idempotent stratum is larger than the null momenta.** A general boundary value in the first row of the stratum table is a complex multiple of a minimal idempotent, not necessarily a Hermitian one. The physical null momenta are the anti-Hermitian slice of that stratum: for the Hermitian representative, $L^{*}=-L$ requires $\tau$ purely imaginary, which the data above satisfy. The identification of the stratum with the photon is therefore an identification of one slice, not of the whole stratum.

## The Path Dependence

The limit depends on the path, and the dependence is not a technicality. Two families with the same scale $R$ and the same phase $\zeta$ but different asymptotic rotors reach different points of the cone for generic rotors:

$$
L_1=\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r,1},
\qquad
L_2=\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r,2},
$$

and $L_1\neq L_2$ unless the rotors differ by the stabiliser of the idempotent. A path along which the boost axis turns reaches the point determined by its asymptotic axis, not by the axis at any finite parameter. The map from paths to points of the cone is therefore not injective, and the cone is not the graph of a function over the units.

Three consequences follow.

1. **The boundary value is a function of the germ of the path at infinity.** It is fixed by the limiting values of $\zeta$, $\vec u_{\mathrm b}$ and $\tilde u_{\mathrm r}$, and by the limiting product $r e^{\psi/2}$. It is not fixed by the element at any finite $\psi$.
2. **The word has no continuous extension to the cone.** A continuous extension would assign one set of word data to each point of the cone independently of the path. No such assignment exists: two paths with the same endpoint on the cone can have different asymptotic data, because the factorization of the limit into a scale, a phase, a boost axis and a rotor is not unique.
3. **The two strata can be reached from the same neighbourhood.** A rotor with $a-ib\neq0$ and a rotor with $a=b=0$ are both limits of unit rotors, so an arbitrarily small change of the path can move the boundary value from one stratum to the other. The stratum is stable under a small change of the path that keeps $a-ib$ away from zero; near the surface $a=b=0$ it is not.

The physical reading of the path dependence is that the massless limit is not a property of the massive element alone. It is a property of the massive element together with the direction in which the limit is taken, and the direction is the physical input: which axis the boost is taken along, and which polarization the rotor carries.

## What the Limit Inherits

The element has a limit and the generator does not. The formal exponent of the word is

$$
\tilde Q_{\log}(\psi)=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r},
$$

with $\ln r=\ln R-\psi/2\to-\infty$ and $\psi/2\to+\infty$. The true logarithm differs from it by the BCH correction, a boost of order $\psi$ that changes the coefficient of the divergence and not its presence (*The Exponential Word and Its Boundary*). The two divergent terms cancel in the element, because the boost's growth and the scale's collapse are the same exponential, but they do not cancel in the exponent. The generator of the boundary value does not exist.

| Object | Massive | Massless limit |
| --- | --- | --- |
| element | finite, a unit | finite, a null element |
| norm | nonzero | zero |
| logarithm | defined, finite | not defined |
| generator | finite | divergent |
| rest frame | defined | not defined |

**What the algebra supplies.** The finiteness condition $r e^{\psi/2}\to R$, the limit $L$, the exponential rate of convergence, and the criterion that separates the two strata. These are theorems about the word.

**What the model supplies.** The value of $R$, which is the energy; the identification of the idempotent slice with a particle momentum; the rotor, which is the polarization data; and the mass-energy relation $E=mc^2\cosh\psi$ that makes the rate automatic at fixed energy. None of these is an algebraic output.

**The generator is the place where the limit fails.** The element's limit is finite because the scale and the boost are inverse exponential coordinates. The generator's limit is infinite because it is the sum of the two, not their difference. A process can have a massless limit as an element and no massless limit as a generator, and the two statements are consistent.

## Physical Readings

- **The massless limit is a boundary value.** The massive element is a unit; the massless one is on the cone, which is the boundary of the group. The limit is taken along a path, and it lands on the cone without the word ever taking a value there.
- **The mass is the radial coordinate of the word.** The scale $r=mc$ is the distance from the cone, and the massless limit is $r\to0$ compensated by $\psi\to\infty$. The mass is not an angle and not a boost parameter; it is the coordinate that the boundary removes.
- **There is no rest frame at the boundary.** The rapidity diverges, so the frame in which the momentum is at rest does not survive the limit. The word's finite part is the boost direction, not the boost.
- **The photon lies on the idempotent stratum.** The null momentum is an imaginary multiple of a Hermitian idempotent, reached when the rotor has a component in the plane of $e_t$ and the boost axis. The nilpotent stratum is the other boundary behaviour and is not a four-momentum.
- **The rate is not predicted.** The algebra forces the leading exponential and leaves the coefficient and the corrections free. The coefficient is the energy, and the energy is supplied by the model.
- **The limit is path-dependent.** The massless limit of a process depends on the direction of approach, and the direction carries the polarization. A limit quoted without the path is incomplete.

## Limits

- **The boundary value is not a value.** The cone has no polar decomposition and no logarithm. The word is defined only on the units, and the limit is a statement about the closure of the domain.
- **The limit is path-dependent.** Different paths reach different points of the cone, and the same point can be reached with different parameter data. The article states the dependence and does not remove it.
- **The stratum is not the particle type.** The idempotent stratum contains the null momenta on its anti-Hermitian slice, but the stratum itself is larger. The algebra supplies no spin, no helicity and no gauge structure.
- **The algebra supplies no rate and no dynamics.** The finiteness condition is algebraic; the value of $R$, the mass-energy relation and the identification of the limit with a physical particle are inputs.
- **One algebra, one point.** Every statement is about one element at one point. In a field theory the massless limit is a limit of a field and a propagator, and the pointwise statement is only the algebraic kernel of it.
- **The generator diverges.** The element's limit does not imply a limit of the logarithm or of the generator. A process with a massless element limit can have no massless generator limit.

## Summary

The polar word parametrizes the units, and the massless shell is the cone, which is the boundary of the units. The massless limit is therefore a boundary value. Along a family with $r=R e^{-\psi/2}$ and asymptotic data $\zeta$, $\vec u_{\mathrm b}$ and $\tilde u_{\mathrm r}$, the word converges to

$$
L=\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r},
$$

a nonzero rank-one element of the cone, with a correction of order $e^{-\psi}$. Decomposing the rotor as $\tilde u_{\mathrm r}=a e_t+b\vec u_{\mathrm b}+\tilde u_\perp$, the trace of the limit is $\frac{R\zeta}{2}(a-ib)$ and $L^2=2\operatorname{Sc}L\,L$. When $a-ib\neq0$ the limit is a nonzero complex multiple of a minimal idempotent; when $a=b=0$ it is a nonzero nilpotent. The rotor selects the stratum, and the rate is the same for both.

For the material momentum the data are $r=mc$, $\zeta=i$, $\vec u_{\mathrm b}=-\vec u_p$, $\tilde u_{\mathrm r}=e_t$ and word rapidity $2\psi$, and the rate is $mc\,e^{\psi}=2E/c+O(e^{-\psi})$. The limit is $2i\frac{E}{c}\tilde\Pi(-\vec u_p)$, the massless momentum, reached with a relative defect of order $m^2$. The idempotent stratum contains this momentum on its anti-Hermitian slice; the stratum itself is larger. The element has a finite limit and the generator does not: the logarithm diverges as $\ln r$ and $\psi/2$ diverge separately. The limit is path-dependent, the cone is not a graph over the units, and the algebra supplies the normal form and the rate condition but not the energy, the polarization or the particle identification.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q=r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar word |
| $r>0$, $\zeta=e^{i\alpha}$ | the scale and the central phase |
| $\tilde U_{\mathrm b}=e^{i\psi\vec u_{\mathrm b}/2}$ | the boost factor at word rapidity $\psi$ and axis $\vec u_{\mathrm b}$ |
| $\tilde u_{\mathrm r}=e^{\theta\vec u_{\mathrm r}/2}$ | the rotor of angle $\theta$ |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the biquaternion norm |
| $L=\frac{R\zeta}{2}(e_t+i\vec u_{\mathrm b})\tilde u_{\mathrm r}$ | the boundary value |
| $\tilde u_{\mathrm r}=a e_t+b\vec u_{\mathrm b}+\tilde u_\perp$ | the rotor in the frame of the boost |
| $\tau=2\operatorname{Sc}L=R\zeta(a-ib)$ | the scale of the idempotent, $L^2=\tau L$ |
| $\tilde P=i\frac{E}{c}e_t+\vec p$ | the material four-momentum |
| $\tilde\Pi(-\vec u_p)=\tfrac12(e_t-i\vec u_p)$ | the Hermitian minimal idempotent opposite the motion |
| $\psi_w=2\psi$ | the word rapidity of the momentum against its Lorentz rapidity |

## Further Reading

- [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html), for the word, the boundary theorem and the two strata.
- [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four factors and their ranges.
- [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html), for the logarithm, its kernel and the image of the exponential.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone, the mass shell and the element-level reading of the two strata.
- [The Exponential Word and Its Boundary](the-exponential-word-and-its-boundary.html), for the boundary of the word and the two kinds of boundary point.
- [The Exponential, the Logarithm and the Generator](the-exponential-the-logarithm-and-the-generator.html), for the generator, its kernel and the processes that have one.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the eigenpair, the Doppler pair and the two null components of the momentum.
- [The Spinor-Helicity Formalism and Biquaternions](the-spinor-helicity-formalism-and-biquaternions.html), for the singular nature of the massless limit in the spinor variables.
- [Conformal Invariance and the Massless Limit in Biquaternionic Form](conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html), for the massless limit as the restoration of a symmetry.
