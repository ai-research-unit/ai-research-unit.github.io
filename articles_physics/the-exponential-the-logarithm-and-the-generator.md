# __The Exponential, the Logarithm and the Generator__

## Introduction

The exponential of a biquaternion is never zero. Its image is exactly the group of units, and the zero-divisor cone is the boundary that it never reaches. The logarithm is the inverse, and it exists on the units and only there. A logarithm of a unit is a **generator**: the element whose one-parameter exponential is the process.

The three statements belong together. The image says which processes have a generator. The kernel says how many generators a process has. The cone says where the answer stops. This article reads the three, and closes with the question that the reading answers: **which processes have a generator?**

The article owns no theorem. The closed forms of the exponential and the logarithm, the kernel, the principal branch and the fibre are those of *Biquaternion Elementary Functions*. The boundary behaviour is that of *Exponential Polar Decomposition of Biquaternions*. The reversible/irreversible dichotomy is that of *Quantum Channels and the Reversible/Irreversible Dichotomy*. The article states the results, links to the proofs, and records the interpretation and its limits.

**Placement.** The article belongs to the Algebra block of the category, in the Element and Operator Representations group, after *The Exponential Word and Its Boundary* and before *The Krein Form and the Indefinite Structure*. It is the category article that reads the exponential and the logarithm; the mathematics stays in the Analysis group of the Mathematical menu.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, central imaginary $i$, and $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$. The vector part has the complex norm $B=\sqrt{(\vec Q,\vec Q)}$ and, for $B\neq0$, the axis $\vec U=\vec Q/B$ with $\vec U^2=-e_t$. The eigenvalues are $\lambda_\pm=Q_t\pm iB$. The biquaternion norm is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$, and $\tilde Q$ is a unit exactly when $\langle\tilde Q\rangle_{\natural}\neq0$.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The closed forms of the exponential, in the oscillatory and nilpotent regimes | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The kernel of the exponential and its parity-matched lattice | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The logarithm by regime, the principal branch and the fibre | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The domain, the principal domain and the cut walls | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The exponential word and the boundary of the polar decomposition | [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html) |
| The group of units and the complement of the cone | [The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone](../articles_maths/the-group-of-units-of-the-biquaternion-algebra-and-the-complement-of-the-zero-divisor-cone.html) |

## The Image

The exponential is entire and its values are units,

$$
\exp:\mathbb{B}\longrightarrow\mathbb{B}^{\times},
\qquad
\langle\exp\tilde Q\rangle_{\natural}=\exp(2Q_t)\neq0.
$$

It is surjective. Every unit has a logarithm, because $\mathbb{B}\cong\mathsf M_2(\mathbb{C})$ and every invertible complex matrix has a logarithm. The image is therefore exactly the group of units, and the zero-divisor cone is exactly the complement of the image.

The closed form separates the two regimes.

| Regime | Condition | $\exp\tilde Q$ |
| --- | --- | --- |
| Oscillatory | $B\neq0$ | $\exp(Q_t)\left(\cos B\,e_t+\sin B\,\vec U\right)$ |
| Nilpotent or scalar | $B=0$ | $\exp(Q_t)\left(e_t+\vec Q\right)$ |

The first row is a scale times a point of the unit sphere in the plane $\{e_t,\vec U\}$. The second row is a scale times a unipotent element. In both rows the value is a unit, and in both rows the value has a logarithm.

The image is open and the cone is its boundary. That is the precise sense in which the cone is the wall: not a set of values, but the set of limits that the values approach and never attain.

## The Kernel

The exponential is not injective. Its kernel is the set of exponents that exponentiate to the identity,

$$
\ker\exp=\left\{\tilde L:\exp\tilde L=e_t\right\}.
$$

The characterisation is exact: $\tilde L$ lies in the kernel exactly when it is diagonalisable over $\mathbb{C}$ and every eigenvalue lies in $2\pi i\mathbb{Z}$. In the algebra the condition reads as follows.

| Exponent | Exponential | Reason |
| --- | --- | --- |
| $2\pi i k\,e_t$, $k\in\mathbb{Z}$ | $e_t$ | the central period of the phase |
| $2\pi j\,\vec U$, $\vec U^2=-e_t$ | $e_t$ | the period of a pure root of $-1$ |
| $\pi i\,e_t+\pi\,\vec U$ | $e_t$ | the half-shifts, which must occur together |
| $2\pi i k\,e_t+2\pi j\,\vec U$ | $e_t$ | the sum of two commuting periods |

For $B\neq0$ the complete kernel on the diagonal part is the **parity-matched lattice**

$$
L=\left\{\pi i m\,e_t+\pi n\,\vec U:\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\right\}.
$$

The scalar and the vector shifts cannot be chosen independently. The rectangular lattice $2\pi i\mathbb{Z}e_t\oplus2\pi\mathbb{Z}\vec U$ is the sublattice of index two on which both integers are even, and the other coset is $\pi i e_t+\pi\vec U$. The matching is the statement that the two eigenvalue logarithms must be shifted in step.

The kernel is **not a subgroup**. It is not closed under addition, because the exponential is not a homomorphism. The sum of two kernel elements need not lie in the kernel: $2\pi\vec e_x$ and $2\pi\vec e_y$ both exponentiate to $e_t$, while $2\pi(\vec e_x+\vec e_y)$ does not. The kernel is a union of conjugacy classes, and it meets the cone: $\pi i e_t+\pi\vec e_z$ has norm zero and exponentiate to the identity.

## The Logarithm

A logarithm of a unit $\tilde Q$ is any $\tilde L$ with $\exp\tilde L=\tilde Q$. The principal logarithm is fixed by the eigenvalues, and the full fibre is the principal value plus the kernel, with a qualification for the scalar case.

| Regime | Principal logarithm | Ambiguity |
| --- | --- | --- |
| $B\neq0$ | $\dfrac{\operatorname{Log}\lambda_++\operatorname{Log}\lambda_-}{2}e_t+\dfrac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{2i}\vec U$ | $2\pi i\left(k_+\tilde\Pi_++k_-\tilde\Pi_-\right)$, $k_\pm\in\mathbb{Z}$ |
| $B=0$, $\vec Q\neq0$ | $\operatorname{Log}Q_t\,e_t+\dfrac{\vec Q}{Q_t}$ | $2\pi i k\,e_t$, $k\in\mathbb{Z}$ |
| $\vec Q=0$ | $\operatorname{Log}Q_t\,e_t$ | scalar logarithms and vector logarithms, not a coset |

The first two rows are lattice cosets. The third is not: a scalar unit has logarithms with a nonzero vector part, whose vector component runs over the complex quadric $(\vec Q_1,\vec Q_1)=(\pi n)^2$. The fibre over a scalar is therefore larger than a translate of the kernel by a lattice, and the coset language must not be used there.

The eigenvalue formula is the general one. The scalar part of the logarithm is fixed by the norm up to the imaginary part, and the vector part is the complex angle along the axis. The principal branch takes the arguments of $\lambda_\pm$ in $(-\pi,\pi]$; the other branches are the lattice shifts.

## The Generator Is a Gauge

A **generator** of a unit $\tilde U$ is an element $\tilde L$ with

$$
\exp\tilde L=\tilde U.
$$

The one-parameter group is $\tilde U(t)=\exp(t\tilde L)$, with $\tilde U(1)=\tilde U$. The generator is the logarithm, and the ambiguity of the logarithm is the ambiguity of the generator.

The ambiguity has three layers.

| Layer | Shift | What it changes |
| --- | --- | --- |
| central phase | $2\pi i k\,e_t$ | nothing observable; the sandwich is blind to it |
| full rotation | $2\pi j\,\vec U$ | nothing; a full turn is the identity |
| parity-matched pair | $\pi i\,e_t+\pi\,\vec U$ | nothing; the two half-shifts cancel |

The first layer is the global phase. The second is not central: $\vec U$ does not commute with the algebra, and a shift by $2\pi\vec U$ is a full rotation of the generator, not a global phase. The third couples the two. The kernel is therefore not merely the centre, and the gauge is not merely a $\mathrm{U}(1)$.

The layer structure is also the reason the quotient language fails. The full kernel is not a subgroup, so the set of generators is not a coset of it. For a non-scalar unit the fibre is a coset of the part of the kernel that lies in the commutative algebra $\mathbb{C}[\tilde Q]$, which is the lattice $L$ and is a subgroup. For a scalar unit the fibre is not a coset of any lattice at all.

The physical reading is that a generator is a **coordinate on the group**, not an element uniquely attached to the process. Two generators that differ by a kernel element produce the same one-parameter group at $t=1$, and the difference is unobservable in the process. The generator is a gauge choice in the precise sense that the algebra does not select one.

## The Cone as the Boundary

The logarithm is defined on the units and nowhere else. The cone is the boundary of the domain, and it is also the boundary of the image of the exponential.

| Point | In the image of $\exp$? | Logarithm? | How it is reached |
| --- | --- | --- | --- |
| interior, $\langle\tilde Q\rangle_{\natural}\neq0$ | yes | yes | a value |
| idempotent stratum, $Q_t\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | no | no | limit with $r\to0$, $\psi\to\infty$ |
| nilpotent stratum, $Q_t=0$, $\langle\tilde Q\rangle_{\natural}=0$ | no | no | rescaled limit of the unipotent line |

The idempotent stratum is reached by the polar word with the scale collapsing and the boost diverging at the same rate. The nilpotent stratum is reached by the rescaled unipotent line,

$$
\tilde Q=\lim_{t\to\infty}\frac{\exp(tN)-e_t}{t},
\qquad
N^2=0.
$$

Neither stratum is a value. The cone is the boundary in the strict sense: every point of it is a limit of units, and no point of it is a unit.

The cone is also the wall of reversibility. A unit is a process that can be run backwards; a zero divisor is not. The exponential sees the difference as the difference between a value and a limit, and the logarithm sees it as the difference between a finite generator and no generator.

## Which Processes Have a Generator?

The question has a sharp answer.

| Process | Element | In the image of $\exp$? | Generator |
| --- | --- | --- | --- |
| reversible, distinct spectrum | unit, $B\neq0$ | yes | $\tilde L$ up to the parity lattice |
| reversible, Jordan | unit, $Q_t(e_t+N)$ | yes | $\tilde L$ up to $2\pi i\mathbb{Z}e_t$ |
| reversible, scalar | unit, $Q_te_t$ | yes | $\tilde L$ plus the vector logarithms |
| zero divisor | $2Q_t\tilde\Pi$ or $N$ | no | none |
| irreversible channel | completely positive trace-preserving map | not a single element | no algebraic generator |

The first three rows are the reversible processes. Every unit is $\exp\tilde L$, so every reversible process lies on a one-parameter subgroup and is continuously connected to the identity. The generator exists, and it is unique only up to the kernel.

The fourth row is the zero divisor. It has no logarithm because it is not a unit, and it has no generator because it is not in the image of the exponential. The cone is the wall: a process on the cone cannot be continuously undone inside the algebra.

The fifth row is the irreversible channel. An irreversible completely positive trace-preserving map is a sum of conjugations, not a single conjugation, so it is not of the form $\tilde U(\cdot)\tilde U^{-1}$ and it has no single algebraic generator. When such a map has a generator, the generator is a Lindbladian superoperator acting on the state space, not an element of $\mathbb{B}$. That object belongs to *Quantum Channels and the Reversible/Irreversible Dichotomy*, and it is a different kind of generator: a generator of a semigroup of maps, not the logarithm of one element.

The algebra therefore answers the question in one direction only. It supplies the generators of the reversible processes, and it says that the irreversible ones have none of the same kind. It does not supply the Lindbladian, the dynamics, or the arrow of time.

## Physical Readings

- **The generator is the logarithm of the process.** A reversible evolution is a unit, and its generator is the element whose exponential it is. The reading is the Hamiltonian when the process is unitary and the boost or rotation exponent when it is a frame change.
- **The kernel is the gauge.** A global phase, a full rotation and a parity-matched half-shift produce the same process. The reading is that the generator is a coordinate, and the coordinate is not the process.
- **The cone is the wall of reversibility.** A zero divisor cannot be exponentiated back to the identity. The reading is that a process on the cone has no continuous inverse inside the algebra.
- **The parity lattice is the phase ambiguity, not a thermal spectrum.** The lattice $L$ is the kernel on the diagonal part, and it is not the Matsubara lattice. The reading is a gauge ambiguity, and the two must not be identified.
- **No arrow of time is supplied.** If $\tilde L$ is a generator, so is $-\tilde L$, and it generates the inverse process. The reading is that the algebra gives both directions and no selection between them.

## Limits

The logarithm is not unique, and the kernel is not a subgroup. The set of generators of a unit is a lattice coset only in the non-scalar case; for a scalar unit it is larger and is not a coset. Any statement that treats the fibre as a coset of a group must be restricted to the non-scalar case.

The logarithm is a coordinate, not a law. The article says which processes have a generator and how many; it does not say which generator a physical system uses, and it does not supply a dynamics.

The principal branch is a convention. The cut walls of the principal logarithm are a choice of branch, not a physical boundary; the physical boundary is the cone, which no branch crosses.

The parity lattice is not thermal. The Matsubara lattice is the character group of the compact thermal circle; $L$ is the kernel of the exponential on the diagonal part of one element. Identifying them would turn a gauge ambiguity into a spectrum, and the parity matching is what blocks the identification.

No arrow of time, no preferred generator and no thermal reading are supplied. The algebra gives the reversible side and the wall; the rest is a boundary condition.

## Summary

- The exponential is entire, its image is exactly the group of units, and the zero-divisor cone is the complement of the image.
- The closed forms are $\exp(Q_t)(\cos B\,e_t+\sin B\,\vec U)$ for $B\neq0$ and $\exp(Q_t)(e_t+\vec Q)$ for $B=0$.
- The kernel is the set of diagonalisable elements with all eigenvalues in $2\pi i\mathbb{Z}$; for $B\neq0$ it is the parity-matched lattice $\pi i m\,e_t+\pi n\,\vec U$ with $m\equiv n\pmod2$.
- The kernel is not a subgroup, and the sum of two kernel elements need not lie in the kernel.
- The logarithm exists on the units and nowhere else; its fibre is a lattice coset for a non-scalar unit and a larger set for a scalar unit.
- A generator of a unit $\tilde U$ is any $\tilde L$ with $\exp\tilde L=\tilde U$; it is defined up to the kernel.
- The gauge is not merely a global phase: the kernel contains the noncentral full rotations $2\pi\vec U$.
- The cone is the boundary of the domain and of the image; the idempotent and nilpotent strata are limits, not values.
- Exactly the reversible processes have an algebraic generator; a zero divisor has none, and an irreversible channel has a Lindbladian superoperator rather than an element.
- The algebra supplies no dynamics, no preferred generator and no arrow of time.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a general biquaternion, $Q_t\in\mathbb{C}$, $\vec Q\in\mathbb{C}^3$ |
| $B=\sqrt{(\vec Q,\vec Q)}$ | the complex norm of the vector part |
| $\vec U=\vec Q/B$ | the axis, a pure root of $-1$, defined for $B\neq0$ |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the eigenprojections, $\vec\Xi=-i\vec U$ |
| $\ker\exp$ | the exponents that exponentiate to $e_t$ |
| $L=\pi i m\,e_t+\pi n\,\vec U$, $m\equiv n\pmod2$ | the parity-matched lattice |
| $\operatorname{Log}\tilde Q$ | the principal logarithm |
| $\tilde L$ | a generator, an element with $\exp\tilde L=\tilde U$ |
| $\mathbb{B}^{\times}$ | the group of units, the complement of the cone |

## Further Reading

- [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the fibre.
- [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html), for the word, the defect and the boundary of the decomposition.
- [The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone](../articles_maths/the-group-of-units-of-the-biquaternion-algebra-and-the-complement-of-the-zero-divisor-cone.html), for the units and the cone.
- [Quantum Channels and the Reversible/Irreversible Dichotomy](quantum-channels-and-the-reversible-irreversible-dichotomy.html), for the Lindbladian side of the dichotomy.
- [The Unit Group, the Cone and the Orders](the-unit-group-the-cone-and-the-orders.html), for the topological reading of the unit group.
- [The Discrete Lattice and the Thermal Circle](the-discrete-lattice-and-the-thermal-circle.html), for the distinction between the parity lattice and the Matsubara lattice.
- [The Exponential Word and Its Boundary](the-exponential-word-and-its-boundary.html), for the polar word and the two strata of the cone.
