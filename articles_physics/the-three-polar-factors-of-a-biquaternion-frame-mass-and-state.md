# __The Three Polar Factors of a Biquaternion: Frame, Mass and State__

## Introduction

The corpus speaks of "the polar decomposition" and "the modulus" as if there were one of each. There are three. Every biquaternion off the null cone can be bracketed in three ways, and each bracketing has a first factor: the quaternion modulus $\tilde q=r\tilde u_{\mathrm r}$, the Hamilton modulus $\Rho=r e^{i\alpha}$, and the Cartan amplitude $\tilde H=r\tilde U_{\mathrm b}$. They answer three different questions — what frame, what invariant, what state — and they are not three versions of one number.

The thesis is one sentence. **The three first factors are three readings of one element, not three objects: they have different types, different domains and different physical questions, only $\Rho$ is a scalar, and the three together carry ten real numbers for an eight-dimensional element, the redundancy being the scale $r$ that all three contain.** The consequences are these. The quaternion factor is a real quaternion and is the spatial frame. The Hamilton factor is central and complex and is the invariant mass of a four-momentum, or the invariant amplitude of a general element. The Cartan factor is Hermitian positive and is the amplitude of the state that the element defines. No one of them is more fundamental than the others, and none of them is a field.

The article is a synthesis. It proves nothing new: the three factorisations are owned by the three mathematical articles, and the word they bracket is owned by *The Polar Decomposition of a N-Regular Biquaternion*. What is added here is the comparison — the types, the domains, the witnesses that separate the domains, and the count that shows the factors are not independent data.

The conventions are those of *Conventions in the Biquaternion Universe*, §*The Polar Word and the Three Pairings*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the norm is $N=\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$, the Hermitian form is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, and the trace is $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$. The state glyph is $\tilde{Ϛ}$. The word is $\tilde Q=r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $r>0$ and $\alpha\in(-\pi/2,\pi/2]$.

## The Results It Uses

| result | established in | used here for |
|---|---|---|
| the four-factor word and its uniqueness off the cone | [*The Polar Decomposition of a N-Regular Biquaternion*](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), §*The Four Factors*, §*Existence and Uniqueness* | the common reference that the three pairings bracket |
| the quaternion pairing, its construction and its domain | [*The Quaternion Pairing of the Polar Decomposition of Biquaternions*](../articles_maths/the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html), §*The Statement*, §*The Domain* | $\tilde q=r\tilde u_{\mathrm r}$ and the witness $\tilde q_r=0$ |
| the Hamilton pairing, the complex modulus and the axis | [*The Hamilton Root Pairing of the Polar Decomposition of Biquaternions*](../articles_maths/the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html), §*The Statement*, §*The Domain* | $\Rho=r e^{i\alpha}$ and the witness $B=0$ |
| the Cartan pairing and the Hermitian square root | [*The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), §*The Statement* | $\tilde H=r\tilde U_{\mathrm b}$ and the witness on the cone |
| the generalized pairing on the null cone | [*The Polar Decomposition of a N-Degenerate Biquaternion*](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html), §*The Two-Factor Decomposition* | the partial-isometry extension at the boundary |
| the domains of the three pairings and their witnesses | [*Conventions in the Biquaternion Universe*](conventions-in-the-biquaternion-universe.html), §*The Domains of the Three Pairings* | the domain table and the separation of factorisation from construction |
| the four-momentum as a Hamilton element | [*The Spectral Reading of a Four-Vector*](the-spectral-reading-of-a-four-vector.html), §*The Frame Dependence* | the mass reading of $\Rho$ |

## One Element, Three Bracketings

The four-factor word is the reference:

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\mathrm b}=\cosh\tfrac{\psi_w}{2}e_t+i\sinh\tfrac{\psi_w}{2}\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\vec u_{\mathrm r}.
$$

The three pairings are its three bracketings into two factors, and the first factor of each is the object of this article.

| pairing | first factor | type | real dimension | the question it answers |
|---|---|---|---|---|
| quaternion | $\tilde q=r\tilde u_{\mathrm r}$ | real quaternion, norm $r^{2}$ | $4$ | what is the spatial frame? |
| Hamilton | $\Rho=r e^{i\alpha}$ | central complex scalar | $2$ | what is the invariant? |
| Cartan | $\tilde H=r\tilde U_{\mathrm b}$ | Hermitian positive, $\det=r^{2}$ | $4$ | what is the state amplitude? |

The table is the whole thesis in one glance. The three factors have three different types. Two of them are not scalars. Only one of them is central. The real dimensions add to $10$, not to $8$, and the next section says why.

### The Count

The element has eight real coordinates. The quaternion factor $r\tilde u_{\mathrm r}$ has four: the scale, the rotation angle and the two angles of the axis. The Hamilton factor $\Rho$ has two: the scale and the phase. The Cartan factor $r\tilde U_{\mathrm b}$ has four: the scale, the rapidity and the two angles of the boost axis.

$$
4+2+4=10=8+2.
$$

The redundancy is exactly the scale $r$, which appears in all three factors. Each factor is a partial description that includes the scale and adds one structural datum: the rotor, the phase, or the boost. The three factors together do not give new information about the element; they give three summaries of the same information, each shaped for a different question. This is the precise sense in which the three pairings are readings and not decompositions.

### What Each Factor Is Blind To

| factor | determined by | blind to |
|---|---|---|
| $\tilde q=r\tilde u_{\mathrm r}$ | $r$, the rotation angle and axis | the phase $\alpha$, the rapidity $\psi_w$, the boost axis |
| $\Rho=r e^{i\alpha}$ | $r$, the phase | the rotation, the boost, both axes |
| $\tilde H=r\tilde U_{\mathrm b}$ | $r$, the rapidity, the boost axis | the phase, the rotation angle and axis |

The table is another way to see the count. Each factor sees the scale and one block of the word; each is blind to the other two blocks. The blocks are the central phase (one number), the compact rotor (three numbers) and the non-compact boost (three numbers).

## The Quaternion Factor: The Spatial Frame

The quaternion factor is

$$
\boxed{\;\tilde q=r\,\tilde u_{\mathrm r},\qquad \langle\tilde q\rangle_{\natural}=r^{2}>0\;}.
$$

It is an ordinary quaternion, and its decomposition is the ordinary quaternion polar decomposition: a positive scale times a unit rotor. It is the factor that carries the rotation. In the word it stands on the right, and its conjugation is the spatial rotation of the frame.

The physical reading is the **frame**. The rotor $\tilde u_{\mathrm r}$ is the rotation that carries the reference axes to the axes of the element, and $r$ is the scale at which the frame is taken. The factor contains no phase and no boost: it is what remains of the element after the central phase and the Hermitian boost have been divided out of the word, and it is computed as $\tilde q=\tilde Q(\tilde U_{\mathrm b}e^{i\alpha})^{-1}$.

The domain of the **factorisation** is the complement of the cone, $N\neq0$, like the word. The domain of the **construction** from the parts is smaller: the formula $\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i$ needs $\tilde q_r\neq0$. On the complement of the cone that condition is also sufficient, because the tangent equation fails only when $\tilde q_r^{-1}\tilde q_i$ is a unit pure quaternion, and that case forces $N=0$.

The witness that separates construction from factorisation is

$$
\tilde Q=i\vec e_x+i\vec e_y,\qquad N=-2,\qquad \tilde q_r=0 .
$$

The element is off the cone and its word exists; the construction from the parts does not start. The factor $\tilde q$ is not undefined as a factor of the word — it is $r\tilde u_{\mathrm r}$ with $r=\sqrt2$ — but the route to it through the real quaternion part is closed. This is a statement about a formula, not about the algebra.

## The Hamilton Factor: The Invariant

The Hamilton factor is

$$
\boxed{\;\Rho=\sqrt N=r\,e^{i\alpha},\qquad \alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]\;}.
$$

It is the only one of the three that is central, and the only one that is a scalar. It carries the scale and the phase and nothing else. Its modulus is $r$ and its argument is the phase of the norm; the branch fixes the sign.

The physical reading depends on the object, and the article must say which reading is in force.

- For a **four-momentum** $\tilde P=i(E/c)e_t+\vec p$, the Hamilton modulus is $\Rho=i mc$ and the invariant is the mass. The phase is $\pi/2$ on the timelike sheet, $0$ on the spacelike sheet, and the cone is the boundary. The eigenvalues are $\lambda_\pm=i mc\,e^{\pm\psi}$, the two light-cone combinations, and their product is $-m^{2}c^{2}$.
- For a **general element**, $\Rho$ is the invariant complex amplitude. Calling it a mass is an extra identification, and the identification is not made by the algebra. It is justified only when the element is a four-momentum, or when a dynamics supplies the identification.

The domain is the intersection of $N\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$. The second condition is not implied by the first. The witness is

$$
\tilde Q=e_t+\vec e_x+i\vec e_y,\qquad N=1,\qquad \langle\vec Q,\vec Q\rangle_{\natural}=1+i^{2}=0 .
$$

The element is invertible, the word exists, the quaternion factor exists, and the Hamilton factor does not: the vector part is null, so there is no axis $\vec U=\vec Q/B$ and no angle $\Theta$. The Hamilton pairing therefore has a domain of its own: it is not implied by the word, and it does not contain the quaternion domain.

The failure at $B=0$ has two physical faces. A **scalar** element is the rest frame: the axis is undefined because there is no boost, and the rest frame is the boundary of the chart, not a singularity. A **nilpotent** vector part is the lightlike direction: there is no frame in which the vector part is a pure scale. The two cases are different and the algebra distinguishes them by $\vec Q=0$ and $\vec Q^{2}=0$ with $\vec Q\neq0$.

## The Cartan Factor: The State Amplitude

The Cartan factor is the Hermitian positive factor

$$
\boxed{\;\tilde H=\sqrt{\tilde Q\tilde Q^{*}}=r\,\tilde U_{\mathrm b},\qquad \tilde H=\tilde H^{*},\qquad \tilde H>0\;}.
$$

It is the amplitude of the state that the element defines. The state itself is the normalized square,

$$
\tilde{Ϛ}_Q=\frac{\tilde Q\tilde Q^{*}}{2\langle\tilde Q,\tilde Q\rangle_{*}}=\frac{\tilde H^{2}}{2\langle\tilde Q,\tilde Q\rangle_{*}},
\qquad \langle\tilde{Ϛ}_Q,e_t\rangle_{*}=\tfrac12 .
$$

The factor $\tilde H$ is unnormalised; the state is $\tilde H^{2}$ up to the normalisation. The distinction matters: the amplitude carries the scale, the state does not.

The physical reading is the **state amplitude**. The positive factor is the part of the element that changes norms and not phases. In the informational sector it is the amplitude of the prepared or measured state; in the material sector it is the positive congruence that a boost applies. The same factor has both readings because the congruence is the same operation on the two sectors; the sectors differ in the sign of the cross terms, not in the factor.

The domain of the Cartan **factorisation** is the complement of the cone, like the word, and it is the widest of the three construction domains. The generalized decomposition extends it to the cone: every element, including a zero divisor, is $\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$ with $\tilde H_{\mathrm{pos}}\ge0$ and $\tilde U_{\mathrm{p}}$ a partial isometry. The witness that separates the Cartan pairing from the word is any element of the cone, for example

$$
\tilde Q=e_t+i\vec e_x,\qquad N=0,\qquad \tilde H_{\mathrm{pos}}=e_t+i\vec e_x .
$$

The word does not exist; the generalized Cartan form does, with a rank-one positive factor and a rank-one partial isometry. This is the boundary that the measurement and polarizer articles use.

## The Domains Are Not Nested

The three domains are different, and none contains another. The table collects the conditions and the witnesses.

| pairing | factorisation exists | construction exists | witness of the smaller domain |
|---|---|---|---|
| quaternion | $N\neq0$ | $N\neq0$ and $\tilde q_r\neq0$ | $i\vec e_x+i\vec e_y$: $N=-2$, $\tilde q_r=0$ |
| Hamilton | $N\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ | same | $e_t+\vec e_x+i\vec e_y$: $N=1$, $\langle\vec Q,\vec Q\rangle_{\natural}=0$ |
| Cartan | $N\neq0$; generalized: all $\tilde Q$ | same | $e_t+i\vec e_x$: on the cone |

The witnesses are chosen so that each element satisfies the other two conditions. $i\vec e_x+i\vec e_y$ is off the cone and has $B=i\sqrt2\neq0$, so Hamilton and Cartan both apply. $e_t+\vec e_x+i\vec e_y$ has $\tilde q_r=e_t+\vec e_x$ invertible and $N=1$, so quaternion and Cartan both apply. $e_t+i\vec e_x$ has $\tilde q_r=e_t$ and $B=i$, so the quaternion construction and the Hamilton pairing both apply, while the word and the Cartan pairing need the generalized form.

No domain contains another, so a statement proved in one pairing cannot be transported to another without checking the witness. The most common error is to assume that the Hamilton modulus exists whenever the word does. It does not.

## The Three Factors Are Not Additive

The factors are three **products**, not three terms:

$$
\boxed{\;\tilde Q=\tilde q\,e^{i\tilde\Psi}
=\Rho\,e^{\tilde U\Theta}
=\tilde H\,\tilde U\;}.
$$

There is no sense in which $\tilde Q=\tilde q+\Rho+\tilde H$, and no sense in which a physical quantity is the sum of the three. Each identity is the whole element, written three times. The consequences are:

- **No conservation law attaches to a factor.** A factor is not a charge, an energy or a particle number. The word is a coordinate statement, and a coordinate is not conserved.
- **No factor is a field.** The quaternion factor is not a triad field, the Hamilton modulus is not a scalar field, and the Cartan factor is not a density matrix field. Each is a function of one element at one point, and the element may itself be a field; the factor is a reading of the field's value, not a new field.
- **No factor evolves on its own.** The polar factors of $\tilde Q(t)$ depend on $t$ through $\tilde Q(t)$; the word does not supply a separate equation for $r$, $\alpha$, $\psi_w$ or $\theta$. The evolution articles own the dynamics, and they evolve the element.

The three factors are also not independent: the count of the previous section shows that they share the scale and that two of the ten numbers are redundant. A change of the element moves all three factors together, and a constraint on one factor is a constraint on the element, hence on the other two.

## Physical Interpretation

The three factors answer three questions that physics usually asks separately, and the synthesis is that one element answers all three at once.

| question | factor | reading | the object where the reading is sharpest |
|---|---|---|---|
| what frame? | $\tilde q=r\tilde u_{\mathrm r}$ | the spatial orientation and the scale of the frame | a rotation, a rigid body, a polarization frame |
| what invariant? | $\Rho=r e^{i\alpha}$ | the mass of a four-momentum, or the invariant amplitude | a particle, a scattering element |
| what state? | $\tilde H=r\tilde U_{\mathrm b}$ | the positive amplitude of the state $\tilde H^{2}$ | a Kraus operator, a Jones matrix, a state preparation |

The readings are compatible because they are readings of one element. A scattering element, for example, has a Cartan factor that gives the state it prepares, a Hamilton modulus that gives its invariant size, and a quaternion factor that gives the frame in which its spin is described. The three descriptions are not three measurements and do not compete; they are three projections of the same eight numbers.

The reading that changes the theory most is the Cartan one. It says that the state is not an independent object added to the algebra: every nonzero operator defines one by $\tilde Q\tilde Q^{*}$. The reading that changes it least is the quaternion one: the real quaternion factor is the ordinary polar decomposition of a real quaternion, and the corpus already used it as the spatial frame. The Hamilton reading sits between them: its first factor is the only scalar of the three, and its physical reading is the most direct.

## What This Does Not Claim

- It does not claim that the three factors are three fields, three particles or three independent degrees of freedom. They are three readings of one element, and the count $4+2+4=10$ for an eight-dimensional element shows the redundancy.
- It does not claim that the three factors are additive or that any of them is conserved.
- It does not claim that the domains coincide. The quaternion construction needs $\tilde q_r\neq0$; the Hamilton pairing needs a non-null vector part; the Cartan pairing is the widest and extends to the cone.
- It does not claim that $\Rho$ is a mass for every element. The mass reading is licensed for a four-momentum; for a general element $\Rho$ is an invariant amplitude.
- It does not claim that the word is unique without the branch. The phase branch $\alpha\in(-\pi/2,\pi/2]$ is the only convention, and the axes degenerate at $\psi_w=0$ and $\theta=0$.
- It does not derive any of the three factorisations. They are owned by the mathematical articles and are cited.

## Summary

- Every biquaternion off the null cone is $r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, and its three bracketings have three first factors: $\tilde q=r\tilde u_{\mathrm r}$, $\Rho=r e^{i\alpha}$ and $\tilde H=r\tilde U_{\mathrm b}$.
- The three factors have three types: a real quaternion, a central complex scalar, and a Hermitian positive element.
- Only $\Rho$ is a scalar and only $\Rho$ is central. The name "modulus" without a qualifier belongs to $\Rho$ alone.
- The three first factors carry $4+2+4=10$ real numbers for an eight-dimensional element; the redundancy is the scale $r$, which all three contain.
- The quaternion factor is the spatial frame; the Hamilton factor is the invariant mass or amplitude; the Cartan factor is the state amplitude.
- The domains are not nested: $i\vec e_x+i\vec e_y$ has no quaternion construction, $e_t+\vec e_x+i\vec e_y$ has no Hamilton pairing, and $e_t+i\vec e_x$ needs the generalized Cartan form.
- The factors are three products of the same element, not three terms; none is conserved, none is a field and none evolves on its own.
- The three readings are compatible because they read the same eight numbers.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N=\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | the biquaternion norm |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hermitian form |
| $r$ | the positive scale, $r=\lvert N\rvert^{1/2}$ |
| $\alpha$ | the central phase, $\alpha=\tfrac12\arg N\in(-\pi/2,\pi/2]$ |
| $\tilde U_{\mathrm b}$ | the Hermitian positive boost factor, $\det=1$ |
| $\tilde u_{\mathrm r}$ | the unit real quaternion rotor |
| $\psi_w$, $\theta$ | the word's rapidity and rotation angle |
| $\tilde q=r\tilde u_{\mathrm r}$ | the quaternion first factor, the spatial frame |
| $\Rho=r e^{i\alpha}$ | the Hamilton first factor, the invariant |
| $\tilde H=r\tilde U_{\mathrm b}$ | the Cartan first factor, the state amplitude |
| $\tilde{Ϛ}_Q=\tilde Q\tilde Q^{*}/2\langle\tilde Q,\tilde Q\rangle_{*}$ | the state defined by a nonzero operator |
| $\tilde H_{\mathrm{pos}}$, $\tilde U_{\mathrm{p}}$ | the generalized positive factor and partial isometry |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian sectors |
| $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$ | the trace |

## Further Reading

- [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four-factor word, its existence and its uniqueness.
- [The Quaternion Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html), for the real quaternion modulus and the construction from the parts.
- [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html), for the complex modulus, the axis and the complex angle.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive factor and the unitary quotient.
- [The Polar Decomposition of a N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the extension to the cone.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the hub that brackets the word and records the action of the factors.
- [The Cartan Pairing, the Amplitude and the Operator-to-State Map](the-cartan-pairing-amplitude-and-the-operator-to-state-map.html), for the state map in full.
- [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html), for the mass reading and the complex angle.
- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), §*The Polar Word and the Three Pairings*, for the frozen notation and the domain table.
