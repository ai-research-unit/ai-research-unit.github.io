# __The Polar Representation and Its Three Pairings__

## Introduction

Every biquaternion off the null cone is the ordered product of four factors: a positive scale, a central phase, a Hermitian boost and a real quaternion rotor,

$$
\tilde Q=r\,\exp(i\alpha)\,\tilde B\,\tilde u_{\mathrm r}
=r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr).
$$

The four factors carry $1+1+3+3=8$ real parameters, the real dimension of the algebra. The word is a change of coordinates on the complement of the zero-divisor cone, not a dynamical decomposition: it says what an element is at one instant and not how it evolves.

The article reads the word and its three two-factor regroupings. The **quaternion pairing** puts the scale and the rotor on one side and the phase and the boost on the other; the **Hamilton root pairing** puts the scale and the phase on one side and the boost and the rotor on the other; the **Cartan Hermitian pairing** puts the scale and the boost on one side and the phase and the rotor on the other. The three are the three ways of splitting four ordered factors into two groups, and each has a physical reading: a real-quaternion modulus, a complex axis-angle, and an amplitude times a unitary.

The mathematics is owned by *The Polar Element Representation of Biquaternions*, *The Polar Representation and Its Three Pairings*, *The Quaternion Pairing*, *The Hamilton Root Pairing*, *The Cartan Hermitian Pairing* and *The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces*. The physics is the reading given below, with its boundaries stated at the end.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The four factors, their ranges, their dimensions and their stable subspaces | [The Polar Element Representation of Biquaternions](../articles_maths/the-polar-element-representation-of-biquaternions.html) |
| The theorem, the uniqueness and the domain off the null cone | [The Polar Element Representation of Biquaternions](../articles_maths/the-polar-element-representation-of-biquaternions.html) |
| The five-step procedure, the two invariants and the worked examples | [The Polar Element Representation of Biquaternions](../articles_maths/the-polar-element-representation-of-biquaternions.html) |
| The quaternion pairing and its domain | [The Quaternion Pairing of the Polar Element Representation of Biquaternions](../articles_maths/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.html) |
| The Hamilton root pairing and its domain | [The Hamilton Root Pairing of the Polar Element Representation of Biquaternions](../articles_maths/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.html) |
| The Cartan Hermitian pairing and the matrix polar decomposition | [The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.html) |
| The action of the four factors on the two sectors | [The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces](../articles_maths/the-action-of-the-polar-element-representation-on-the-hermitian-and-anti-hermitian-subspaces.html) |
| The six remarkable subspaces and the factor that preserves each | [The Polar Element Representation and Remarkable Subspaces](../articles_maths/the-polar-element-representation-and-remarkable-subspaces.html) |
| The two one-sided operators under the polar word | [One-Sided Operator Under the Polar Representation](../articles_maths/one-sided-operator-under-the-polar-representation.html) |
| The two-sided operator and its kernel | [Two-Sided Operator Under the Polar Representation](../articles_maths/two-sided-operator-under-the-polar-representation.html) |

## The Four Factors

| # | Factor | Name | Exponent | Root | Range | Real dimension | Action on the algebra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | $r$ | scale | — | — | $r>0$ | $1$ | dilation by $r^2$ |
| 2 | $\exp(i\alpha)$ | central phase | $i\alpha$ | $i$ | $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | $1$ | multiplication by the scalar |
| 3 | $\tilde B=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | boost | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $i\vec u_{\mathrm b}$ | $\psi\ge0$, $\vec u_{\mathrm b}\in\mathcal{A}$ | $3$ | congruence $X\mapsto \tilde BX\tilde B^{*}$ |
| 4 | $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | rotor | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\vec u_{\mathrm r}\in\mathcal{A}$ | $3$ | conjugation $X\mapsto \tilde u_{\mathrm r}X\tilde u_{\mathrm r}^{-1}$ |

The axis sphere $\mathcal{A}$ is the set of unit real pure quaternions, the roots of $-e_t$. The phase is the only factor whose sandwich is the identity; its action on the algebra is the scalar multiplication recorded in the table, and that is the one row that departs from the sandwich convention.

The scale and the phase are central, the boost is Hermitian positive and non-compact, and the rotor is compact and real. The order of the factors is forced by the construction: the scale and the phase commute with everything, the boost stands on the left of the rotor, and the rotor is what remains after the Hermitian part is divided out. The word is unique once the branch of the square root is fixed.

## Reading the Eight Numbers

The word returns the physical description of an element in eight real numbers:

- the **scale** $r$, the modulus of the biquaternion norm;
- the **phase** $\alpha$, half the argument of the norm, in the interval $(-\pi/2,\pi/2]$;
- the **rapidity** $\psi$ and the two angles of the **boost axis** $\vec u_{\mathrm b}$;
- the **rotation angle** $\theta$ and the two angles of the **rotor axis** $\vec u_{\mathrm r}$.

The first two are the central data, the next three the non-compact data, the last three the compact data. The scale and the phase are fixed by the norm $N$: $r=|N|^{1/2}$ and $\alpha=\tfrac12\arg N$. The rapidity is fixed by the ratio of the two invariants,

$$
\cosh\psi=\frac{E^2}{|N|}, \qquad E^2=\sum_\mu|Q_\mu|^2,
$$

and the two axes are fixed by the phases of the four complex coordinates. The pair $(N,E^2)$ fixes the scale, the phase and the rapidity and cannot fix the two directions: a real rotation of the vector part leaves both invariants unchanged and turns the axes.

The count is the same statement. Four complex coordinates carry eight real numbers. The scale, the phase and the rapidity account for three; the two boost-axis angles, the two rotor-axis angles and the rotation angle account for the remaining five. The word is a coordinate system on the eight-dimensional algebra, not a constraint on it.

## The Domain

The word exists if and only if $N\neq0$, that is, if and only if the element is outside the zero-divisor cone. On the cone the product of the four factors has norm of modulus $r^2>0$, so no factorisation exists. The condition is one complex equation, hence two real equations, and the cone has real codimension two: the domain is the complement of a six-real-dimensional cone in the eight-real-dimensional algebra.

The failure is physical. A lightlike four-vector has no rest frame, so the scale degenerates and there is no boost split: there is no frame in which its spatial part vanishes and no rapidity that carries it to that frame. The algorithm stops on the cone for the same reason a boost parametrisation stops at the speed of light.

The branch $\alpha\in(-\pi/2,\pi/2]$ is the only convention of the word. The other square root $-\Rho$ has angle $\alpha\pm\pi$, outside the interval. Every other step is forced: the normalised element, the Hermitian square root and the rotor are determined by the element and the branch.

## The Three Pairings

The four-factor word is the reference. The three pairings are its three bracketings into two factors, and the table records which pair of factors each one groups together.

| Pairing | First factor | Second factor | What it separates |
| --- | --- | --- | --- |
| Four-factor word | — | — | the unpaired reference |
| Quaternion | $\tilde q=r\tilde u_{\mathrm r}$ | $\exp(i\tilde\Psi)$ | scale and rotor / phase and boost |
| Hamilton root | $\Rho=r\exp(i\alpha)$ | $\exp(\vec\Xi\Theta)$ | scale and phase / boost and rotor |
| Cartan Hermitian | $\tilde H=r\tilde B$ | $\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}$ | scale and boost / phase and rotor |

### The Quaternion Pairing

The quaternion pairing writes the element as a **real quaternion modulus** times the exponential of a **real quaternion angle**:

$$
\tilde Q=\tilde q\,\exp(i\tilde\Psi), \qquad
\tilde q=r\,\tilde u_{\mathrm r}, \qquad
\exp(i\tilde\Psi)=\exp(i\alpha)\,\tilde u_{\mathrm r}^{-1}\tilde B\tilde u_{\mathrm r}.
$$

The exponent is a real quaternion with scalar part $\alpha$ and pure part $\tfrac{\psi}{2}\vec u_{\mathrm b,2}$, where $\vec u_{\mathrm b,2}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ is the boost axis rotated by the rotor. The modulus is an ordinary quaternion in its polar form: a positive scale and a unit rotor.

In the electromagnetic reading, $\tilde Q=\tilde E+i\tilde B_{\mathrm m}$ with $\tilde E,\tilde B_{\mathrm m}$ real quaternions. The ratio $\tilde P=\tilde E^{-1}\tilde B_{\mathrm m}$ is the duality quotient, the quaternion that carries the electric part to the magnetic part; the angle $\tilde\Psi$ is the quaternion angle of the field, with scalar part the duality phase and pure part half the boost. The modulus $\tilde q=\tilde E(\cos\tilde\Psi)^{-1}$ is the normalised electric part. The construction needs $\tilde E\neq0$: a purely magnetic field has no electric part to normalise. The factorisation of the word still exists on a purely imaginary element, but the construction from the parts does not.

### The Hamilton Root Pairing

The Hamilton pairing writes the element as a modulus times a complex cosine plus a complex unit axis times the complex sine:

$$
\tilde Q=\Rho\bigl(\cos\Theta+\vec\Xi\sin\Theta\bigr), \qquad
\Rho=\sqrt N, \qquad
\vec\Xi=\frac{\vec Q}{B}, \qquad
B=\sqrt{(\vec Q,\vec Q)}, \qquad
\cos\Theta=\frac{Q_t}{\Rho}, \qquad
\sin\Theta=\frac{B}{\Rho}.
$$

The modulus carries the scale and the phase; the axis and the angle carry the boost and the rotor. The complex axis $\vec\Xi$ is the direction of the transformation, and the complex angle $\Theta$ is its magnitude: on aligned axes the real part of the angle is half the rotation and the imaginary part is half the boost, while in general the two parts do not separate. A general Lorentz element is a point of the complexified rotation group, and the Hamilton form is its axis-angle coordinate.

The domain is smaller than the polar domain: it requires $N\neq0$ and $(\vec Q,\vec Q)\neq0$. The second condition is not implied by the first. The element $e_t+\vec e_x+i\vec e_y$ has $N=1$ and $(\vec Q,\vec Q)=1+i^2=0$, so it is invertible and has no Hamilton representation. The axis is normalised by the vector part, and a null vector part gives no axis.

### The Cartan Hermitian Pairing

The Cartan pairing writes the element as a **Hermitian positive factor** times a **unitary factor**:

$$
\tilde Q=\tilde H\tilde U, \qquad
\tilde H=\sqrt{\tilde Q\tilde Q^{*}}=r\tilde B, \qquad
\tilde U=\tilde H^{-1}\tilde Q=\exp(i\alpha)\tilde u_{\mathrm r}.
$$

The first factor is Hermitian positive; the second is unitary. The pairing is the matrix polar decomposition of $\mathrm{GL}(2,\mathbb{C})$ read in the algebra: the Hermitian factor is the amplitude, the part that changes norms and not phases; the unitary factor is the phase, the part that preserves the inner product. The determinant is the product,

$$
\det\tilde H=r^2, \qquad \det\tilde U=\exp(2i\alpha), \qquad \det\tilde Q=r^2\exp(2i\alpha),
$$

so the scale is the modulus of the determinant, the phase is half its argument, and the boost and rotor are the anisotropy and the turn of the two factors.

The factorisation solves one equation, $\tilde Q\tilde Q^{*}=\tilde H^2$, and the second factor follows by division. It needs no construction external to the algebra, and its domain is the whole complement of the cone.

### The Three Pairings Compared

The three pairings are not three decompositions; they are three readings of the same ordered word. The quaternion pairing isolates the real quaternion structure, the Hamilton pairing isolates the complex axis-angle, and the Cartan pairing isolates the amplitude–phase split. Each has a physical reading and a domain of its own.

| Question | Pairing | The factor that answers it |
| --- | --- | --- |
| What is the real quaternion modulus and its angle? | quaternion | $\tilde q=r\tilde u_{\mathrm r}$, $\tilde\Psi=\alpha+\tfrac{\psi}{2}\vec u_{\mathrm b,2}$ |
| What is the axis and the complex angle? | Hamilton | $\vec\Xi$, $\Theta$ |
| What is the amplitude and the phase? | Cartan | $\tilde H=r\tilde B$, $\tilde U=e^{i\alpha}\tilde u_{\mathrm r}$ |

The Cartan pairing has the widest construction domain, the whole complement of the cone, and the cleanest matrix interpretation; the quaternion pairing has the most direct electromagnetic reading; the Hamilton pairing has the most direct Lorentz-group reading. None is more fundamental than the others, and none adds information to the four-factor word.

## The Action on the Sectors and the Subspaces

The four factors act by four different operations, and the table records which subspace each one preserves.

| Factor | Operation | Stable subspaces |
| --- | --- | --- |
| scale $r$ | dilation by $r^2$ | all six |
| phase $\exp(i\alpha)$ | multiplication by the scalar | centre, vector space |
| boost $\tilde B$ | congruence | centre, $\mathbb{M}_+$, $\mathbb{M}_-$ |
| rotor $\tilde u_{\mathrm r}$ | conjugation | all six |

The six subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector space $\mathrm{Vect}(\mathbb{B})$, the real quaternion space $\mathbb{H}_{\mathbb{B}}$, the imaginary quaternion space $i\mathbb{H}_{\mathbb{B}}$, and the two sectors $\mathbb{M}_\pm$. The scale and the rotor preserve all six; the phase preserves only the centre and the vector space; the boost preserves the centre and the two sectors. Apart from the centre, no subspace is preserved by all four factors, and that is why no single subspace characterises the word.

On the material sector the boost reads

$$
a_2=a\cosh\psi-b_\parallel\sinh\psi, \qquad
b_{\parallel,2}=b_\parallel\cosh\psi-a\sinh\psi,
$$

with $\psi$ the rapidity of the factor in view, $a$ the scalar coordinate and $b_\parallel$ the component of the vector part along the boost axis; on the informational sector the two cross terms carry the opposite sign. The difference is the sector sign. The same congruence reads as the Lorentz action on matter and as a positive congruence on the state space.

The phase at $\alpha=\pi/2$ is multiplication by $i$, which exchanges the two sectors and reverses the norm. It is the Wick rotation, the passage from real to imaginary time, and it is not a symmetry of the material sector. The rotor at $\theta=2\pi$ is $-e_t$, the sign that a spinor picks up after a rotation by $2\pi$; the phase branch does not reach $\pi$.

## The Boost Factor Is Not the Acting Rotor

The word's boost factor is $\tilde B=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$. Its congruence is the Lorentz boost of rapidity $\psi$; the axis $\vec u_{\mathrm b}$ is the axis of the word's boost, and for a pure-boost word ($\tilde u_{\mathrm r}=e_t$) the four-velocity is along $-\vec u_{\mathrm b}$. The factor that the corpus uses as the physical frame rotor is the inverse square root,

$$
\tilde U_{\mathrm b}=\tilde B^{-1/2},
$$

whose congruence is the boost of half the rapidity. The word stores the boost twice: the factor's exponent carries $\psi/2$, and the congruence deposits $\psi$. Taking $\tilde B$ for the acting rotor doubles the rapidity.

The same doubling appears in the velocity. For a four-velocity of speed $v$ and $\beta=v/c$, the word gives

$$
\cosh\psi=\frac{1+\beta^2}{1-\beta^2}=\cosh(2\eta), \qquad \beta=\tanh\eta,
$$

so the word's rapidity is twice the rapidity $\eta$ of the frame. The physical rotor has rapidity $\eta$; the word has $2\eta$. This is the most common factor-of-two error in the corpus, and it is a bookkeeping error, not a physical one: both numbers describe the same boost, one stored and one acted.

The factor-of-two has a second face. A one-sided multiplication by a real scale $r$ dilates by $r$, while the sandwich dilates by $r^2$. The one-sided action is half the dilation of a frame change. The same one-slot versus two-slot bookkeeping is at work in the boost.

## A Four-Vector Is Bilinear, a Spinor Is Linear

The polar element acts on a four-vector and on a spinor by two different laws. A four-vector transforms by the congruence

$$
X\longmapsto \tilde U X\tilde U^{*},
$$

which is bilinear in the spinor when $X=\psi\psi^{*}$; a null four-vector is of that form. A spinor is a module element and transforms by the left multiplication

$$
\psi\longmapsto \tilde U\psi.
$$

The first law is quadratic in the spinor, the second linear. The sandwich is the four-vector column of the representation theory and the left multiplication is the spinor column. The polar action on the two sectors is the four-vector action; the action on the spinor module is the left multiplication, and it is the one that carries the double cover and the sign of the spinor.

The distinction is the reason the same rotor acts differently on the two objects. A rotation through $2\pi$ gives $-\tilde U$ on the spinor and $+\mathrm{id}$ on the four-vector, because the congruence by $-\tilde U$ is the congruence by $\tilde U$. The sign is visible only in the linear action.

## Physical Readings

The word is the physical description of an element, and each factor has a reading.

- The **scale** is the invariant length: the modulus of the four-position, $c$ for the four-velocity, $mc$ for the on-shell four-momentum. It is the only factor that survives the sandwich as a scalar, and it survives squared.
- The **phase** is the timelike/spacelike label and the gauge phase. It is $\pi/2$ on the timelike cone and $0$ on the spacelike sheet; it is the central $\mathrm{U}(1)$ that the sandwich does not see.
- The **boost** is the velocity: the axis and the rapidity that carry the element to its rest frame. The word stores the rapidity as $\psi=2\eta$, and the acting rotor uses $\eta=\psi/2$.
- The **rotor** is the spin orientation: the rotation angle and axis of the spatial frame.

The pairings read the same data under different headings. The quaternion pairing reads the electromagnetic field as a real quaternion modulus and a quaternion angle; the Hamilton pairing reads the Lorentz element as a complex axis-angle; the Cartan pairing reads the element as an amplitude times a unitary. The readings are dictionaries, not derivations: the algebra supplies the factors, and the physics supplies the names.

The word is a coordinate statement, not a dynamics. It says that every element off the cone is a scale times a phase times a boost times a rotor; it does not say that a physical system moves through those factors, nor that the factors are conserved, nor that the decomposition is stable under evolution. The evolution articles own the dynamics; this article owns the description.

## Limits

The decomposition is defined off the null cone and nowhere on it. The failure is the absence of a rest frame, not a singularity of the algebra.

The branch of the square root is the only convention. The interval $(-\pi/2,\pi/2]$ for the phase fixes the sign of the modulus; every other step is forced.

The boost factor is not the acting rotor. The word stores the boost twice, and reading the factor as the rotor doubles the rapidity. The velocity formula $\cosh\psi=(1+\beta^2)/(1-\beta^2)$ is the check.

The Hamilton pairing has a smaller domain than the polar word; the quaternion construction needs a non-vanishing real quaternion part; the Cartan pairing and the four-factor word have the widest domain. A statement proved in one pairing need not hold in another without checking the domain.

The three pairings are regroupings, not new decompositions. They add no information to the four-factor word and no physics to the factors. Their value is that each makes one physical question easy to ask.

## Summary

- Every biquaternion off the null cone is $r\exp(i\alpha)\tilde B\tilde u_{\mathrm r}$, with $1+1+3+3=8$ real parameters.
- The scale is the modulus of the norm, the phase is half its argument, the boost is the Hermitian positive factor and the rotor is the real quaternion factor.
- The word exists exactly off the zero-divisor cone; on the cone a lightlike four-vector has no rest frame and no boost split.
- The branch $\alpha\in(-\pi/2,\pi/2]$ is the only convention of the decomposition.
- The quaternion pairing is $\tilde Q=\tilde q\exp(i\tilde\Psi)$ with $\tilde q=r\tilde u_{\mathrm r}$ and $\tilde\Psi=\alpha+\tfrac{\psi}{2}\vec u_{\mathrm b,2}$; it groups scale and rotor against phase and boost.
- The Hamilton root pairing is $\tilde Q=\Rho(\cos\Theta+\vec\Xi\sin\Theta)$; it groups scale and phase against boost and rotor, and its domain also excludes a null vector part.
- The Cartan pairing is $\tilde Q=\tilde H\tilde U$ with $\tilde H=r\tilde B$ and $\tilde U=e^{i\alpha}\tilde u_{\mathrm r}$; it groups scale and boost against phase and rotor.
- The three pairings are the three bracketings of the four-factor word; none adds information to it.
- The scale and the rotor preserve all six remarkable subspaces, the phase preserves the centre and the vector space, and the boost preserves the centre and the two sectors.
- On the material sector the boost reads with one sign of the cross terms; on the informational sector the sign is opposite.
- The word's boost factor has rapidity $\psi=2\eta$, where $\eta$ is the rapidity of the physical frame; the acting rotor is the inverse square root of the factor.
- A four-vector transforms by the congruence and a spinor by the left multiplication; the first is bilinear in the spinor, the second linear.
- The decomposition is a coordinate statement off the cone and not a dynamics.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $r$ | the positive scale, $r=\lvert N\rvert^{1/2}$ |
| $\alpha$ | the central phase, $\alpha=\tfrac12\arg N\in(-\pi/2,\pi/2]$ |
| $\tilde B=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | the Hermitian positive boost factor, the word's boost |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ | the boost and rotor axes, unit real pure quaternions |
| $\psi$, $\theta$ | the rapidity stored in the word and the rotation angle |
| $\eta$ | the rapidity of the physical frame, $\psi=2\eta$ |
| $\tilde U_{\mathrm b}=\tilde B^{-1/2}$ | the physical frame rotor |
| $N=\langle\tilde Q\rangle_{\natural}$ | the biquaternion norm |
| $E^2=\sum_\mu\lvert Q_\mu\rvert^2$ | the Euclidean square, the Born form at equal arguments |
| $\tilde q=r\tilde u_{\mathrm r}$ | the real quaternion modulus of the quaternion pairing |
| $\tilde\Psi=\alpha+\tfrac{\psi}{2}\vec u_{\mathrm b,2}$ | the real quaternion angle of the quaternion pairing |
| $\Rho=\sqrt N$, $\vec\Xi$, $\Theta$ | the modulus, axis and complex angle of the Hamilton pairing |
| $\tilde H=r\tilde B$, $\tilde U=e^{i\alpha}\tilde u_{\mathrm r}$ | the Hermitian and unitary factors of the Cartan pairing |
| $\mathbb{M}_\pm$ | the material and informational sectors |

## Further Reading

- [The Polar Element Representation of Biquaternions](../articles_maths/the-polar-element-representation-of-biquaternions.html), for the four factors, the theorem and the uniqueness.
- [The Quaternion Pairing of the Polar Element Representation of Biquaternions](../articles_maths/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.html), for the real quaternion modulus and the angle.
- [The Hamilton Root Pairing of the Polar Element Representation of Biquaternions](../articles_maths/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.html), for the complex axis-angle.
- [The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.html), for the amplitude–phase split and the matrix polar decomposition.
- [The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces](../articles_maths/the-action-of-the-polar-element-representation-on-the-hermitian-and-anti-hermitian-subspaces.html), for the sector action and the cross-term signs.
- [The Polar Element Representation and Remarkable Subspaces](../articles_maths/the-polar-element-representation-and-remarkable-subspaces.html), for the preservation table.
- *The Element and Operator Representations*, for the pictures in which the polar factors act.
- *The Operators: One-Sided, Two-Sided, Sandwich*, for the one-sided and two-sided operators of the word.
