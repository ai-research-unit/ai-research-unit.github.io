# __Frames, Rotations and the Lorentz Group__

## Introduction

A frame is a choice of axes, and a motion is a change of frame. The biquaternion algebra supplies both: the norm fixes the form, the unit-norm slice is the space of spin frames, and the sandwich by a unit is the change of frame. The Lorentz group is not a subset of the algebra; it is the quotient of the norm-one group by the central sign, and the algebra carries the double cover.

The article reads the group that carries the motions, the sandwich that acts, the rotations, the boosts, the orbits and the reflections. Its thesis is that a frame is a unit up to sign, that a change of frame is the dagger sandwich, that the interval is the invariant, that a rotation is an algebra automorphism and that a boost is a motion which is not one. It proves nothing; the theorems are in the mathematics articles of the source table.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The double covers, the rotor, the dagger sandwich, its kernel, its scaling and its action on the remarkable subspaces | [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) |
| The orbits, the rank invariant, the mass shell and the light cone | [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) |
| The reflection formula and the Cartan–Dieudonné theorem | [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) |
| The algebra automorphisms and the real automorphism group | [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html) |
| The group of units and the norm-one slice | [N-Regularity and N-Degeneracy in the Biquaternion Algebra, §The Group of Units](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| The topology of the unit group and its maximal compact subgroup | [The Biquaternion Unit Group as a Topological Group](../articles_maths/the-biquaternion-unit-group-as-a-topological-group.html) |
| The unitary group and the quotient $U(\mathbb{B})/U(1)\cong SO(3)$ | [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html) |

## The Group that Carries the Motions

### The Double Covers

The norm-one group is
$$
\mathbb{B}^{\times}_{1}=\{\tilde U:\langle\tilde U\rangle_{\natural}=1\}\cong SL_2(\mathbb{C}),
$$
of real dimension six. Its centre is $\{\pm e_t\}$, and the quotient is the proper orthochronous Lorentz group,
$$
\boxed{\;\mathbb{B}^{\times}_{1}/\{\pm e_t\}\cong SO^{+}(1,3)\;}.
$$
The group is simply connected, so it is the universal cover,
$$
\mathbb{B}^{\times}_{1}\cong \mathrm{Spin}(1,3).
$$
The compact part is the unit quaternions,
$$
Sp(1)=S^{3}\cong SU(2),
\qquad
Sp(1)/\{\pm e_t\}\cong SO(3),
$$
the double cover of the spatial rotations. The full unit group $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ has real dimension eight; the norm-one slice has dimension six; the quaternion layer $\mathbb{H}_{\mathbb{B}}$ has real dimension four.

**The Lorentz group is a quotient, not a subgroup.** A Lorentz transformation has six real parameters, and the quaternion layer has only four real dimensions; there is no smooth embedding of $SO^{+}(1,3)$ into $\mathbb{H}_{\mathbb{B}}$. The group manifold does not fit in the layer, while its action on the four-dimensional material sector does. The algebra contains the double cover $\mathbb{B}^{\times}_{1}$, and the Lorentz group is the quotient by the central sign. The group itself sits in the projective space, where the classes of the units form the complement of the null quadric and are $PGL_2(\mathbb{C})\cong SO^{+}(1,3)$.

**The algebra carries the spin frame.** A frame of the material sector is a norm-one unit up to sign, and the double cover is the spin frame. The sign is the spinor sign: a frame and its negative are the same frame, while a spinor and its negative are not the same spinor. Interpreted physically, the Lorentz group is the group of frames, and the norm-one group is its spin cover; the algebra carries the cover, not the quotient.

**The boundary of the interpretation.** The frame is an algebraic frame, not a laboratory. The identification uses the action on $\mathbb{M}_{-}$ and the norm; it does not fix a reference frame and it does not supply a metric beyond the norm. The projective description is a description of the group, not of a physical space of states.

### The Automorphism Group

The $\mathbb{C}$-linear automorphisms of the algebra are the inner ones,
$$
\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})\cong \mathbb{B}^{\times}/\mathbb{C}^{\times}\cong PGL_2(\mathbb{C})\cong SO(3,\mathbb{C}),
$$
of real dimension six; as a real group this is $SO^{+}(1,3)$. The full real automorphism group has two components,
$$
\mathrm{Aut}_{\mathbb{R}}(\mathbb{B})\cong \mathrm{Aut}_{\mathbb{C}}(\mathbb{B})\rtimes \mathbb{Z}/2,
$$
the second component consisting of the conjugate-linear automorphisms.

**The automorphism group is the same abstract group with a different action.** The Lorentz group appears twice: as the quotient of the norm-one group, acting on the material sector by the dagger sandwich, and as the automorphism group of the algebra, acting by inner automorphisms. The two actions agree on the unitary slice, where the inverse and the Hermitian conjugate coincide; they differ on a boost. Interpreted physically, the same group can be a change of frame and a symmetry of the algebraic structure, and the two interpretations are not the same map.

**The boundary of the interpretation.** The identification of $PGL_2(\mathbb{C})$ with $SO^{+}(1,3)$ is an isomorphism of real Lie groups, not of complex groups; the complex group is $SO(3,\mathbb{C})$. A physical Lorentz transformation is the action on $\mathbb{M}_{-}$, not the inner automorphism, and the article does not identify the two.

## The Sandwich and the Change of Frame

### The Action

For a unit $\tilde Q$, the **dagger sandwich** is
$$
\mathrm{H}_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
\mathrm{H}_{\tilde Q}(\tilde Q_3)=\tilde Q\,\tilde Q_3\,\tilde Q^{*}.
$$
It is a homomorphism of the unit group into $GL(\mathbb{B})$,
$$
\mathrm{H}_{\tilde Q\tilde Q_1}=\mathrm{H}_{\tilde Q}\circ\mathrm{H}_{\tilde Q_1},
\qquad
\mathrm{H}_{A\tilde Q}=\mathrm{H}_{A}\circ\mathrm{H}_{\tilde Q},
\qquad
\mathrm{H}_{A}=|A|^{2}\mathrm{id}\ \text{for central }A,
$$
it preserves the two sectors $\mathbb{M}_{\pm}$, and it scales the norm by
$$
\boxed{\;\langle\mathrm{H}_{\tilde Q}(\tilde Q_3)\rangle_{\natural}=|\langle\tilde Q\rangle_{\natural}|^{2}\langle\tilde Q_3\rangle_{\natural}\;}.
$$
On the whole algebra its kernel is the central circle $\mathrm{U}(1)e_t$; on the norm-one slice it is $\{\pm e_t\}$, which is the double cover. On the norm-one slice it is an isometry and its image is $SO^{+}(1,3)$; on the whole unit group the image is a seven-dimensional similarity group.

| operator | group | kernel | image |
| --- | --- | --- | --- |
| $\mathrm{H}_{\tilde Q}$, general unit | $\mathbb{B}^{\times}$ | $\mathrm{U}(1)e_t$ | similarities of real dimension seven |
| $\mathrm{H}_{\tilde U}$, norm-one unit | $\mathbb{B}^{\times}_{1}\cong SL_2(\mathbb{C})$ | $\{\pm e_t\}$ | $SO^{+}(1,3)$ |
| $\mathrm{H}_{\tilde u}$, rotation rotor | $Sp(1)\cong SU(2)$ | $\{\pm e_t\}$ | $SO(3)$ |

### The Interpretations

**A change of frame is the sandwich.** A four-vector is acted on by an element, not by a matrix, and the action is the sandwich. The acting element meets the element on both sides at once; a one-sided multiplication carries the element, while the sandwich carries the frame in which the element is described. Interpreted physically, a change of frame is a relabelling of the description, and the unit is the frame. The norm-one condition makes the action an isometry, and the central sign makes it a double cover.

**The interval is the frame-independent object.** On the norm-one slice the sandwich preserves $\langle\tilde Q\rangle_{\natural}$, and off the slice it multiplies $\langle\tilde Q\rangle_{\natural}$ by the positive factor $|\langle\tilde Q\rangle_{\natural}|^{2}$. The sign and the vanishing of the norm are therefore unchanged by every unit, and the causal class of a four-vector is frame-independent. Interpreted physically, the interval is objective and the scale is a similarity, not a change of causal type.

**The two sectors are preserved.** The sandwich preserves $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ for every unit, because the sectors are the eigenspaces of the dagger. Interpreted physically, a change of frame acts on the four-vectors and on the Hermitian forms in the same way; the state side and the material side are both covariant.

**The central phase is not a frame.** The kernel of the sandwich on the whole algebra is the central circle, so an overall phase acts trivially. Interpreted physically, a global phase is a redundancy of the action, not a change of frame; two units that differ by a phase give the same transformation of the algebra.

**The boundary of the interpretations.** The sandwich preserves $\mathbb{M}_{+}$, but a boost does not preserve its trace-one slice: the trace-one Bloch ball is not invariant under the full Lorentz group. The finite-dimensional Hermitian sector is the space of Hermitian forms, not the relativistic state space; making the state space itself relativistic is open work. The algebra supplies the covariant action on the forms, not a unitary representation of the Lorentz group on a finite-dimensional state space.

## Rotations

### The Rotor

A rotation about the unit real direction $\vec u$ through the angle $\theta$ is the rotor
$$
\tilde u=\exp\!\left(\frac{\theta}{2}\vec u\right)
=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\vec u,
$$
a real unit quaternion. Its sandwich is
$$
\mathrm{H}_{\tilde u}(\tilde Q_3)=\tilde u\,\tilde Q_3\,\tilde u^{*},
$$
an algebra automorphism. On the spatial part of a four-vector it is the rotation through $\theta$, and the angle in the element is half the angle of the rotation. A full turn of the rotor, $\tilde u\mapsto-\tilde u$, is the identity rotation, so
$$
Sp(1)\longrightarrow SO(3)
$$
is two-to-one.

**A rotation is an algebra automorphism.** The rotor is unitary, so the inverse and the Hermitian conjugate coincide, and the sandwich preserves the product as well as the interval. Interpreted physically, a rotation is a symmetry of the algebra and not only of the form: it can be applied to any element, and it preserves the centre, the vector subspace, the quaternion halves and the two sectors. The rotation is the only kind of frame change with this property.

**The half-angle is the spinor.** The rotation acts once through the left factor and once through the right, so the angle in the rotor is half the angle of the motion. Interpreted physically, the halved angle is the spinor: a rotation by $2\pi$ is $-e_t$ on the rotor, and the sign is the double cover. The sign is invisible on a four-vector and visible on a spinor.

**The two periods separate integer from half-integer spin.** The central sign $-e_t$ acts as $+e_t$ on the integer-spin representations and as $-e_t$ on the half-integer ones; a rotation by $2\pi$ is the identity on the former and minus the identity on the latter. Interpreted physically, the $2\pi/4\pi$ distinction is the spin parity: integer-spin states are single-valued under a full turn, and half-integer-spin states are double-valued.

**The boundary of the period interpretation.** The algebra supplies the sign and the two periods; it does not supply the spin-statistics theorem. The distinction is a property of the representations, not a derivation of the statistics of a particle.

**The rotation acts on the complexified vector space.** Because the central imaginary $i$ commutes with the rotor, the real vector part $\vec e_k$ and the imaginary vector part $i\vec e_k$ rotate by the same angle. Interpreted physically, the six-real-dimensional vector subspace carries one complex-linear rotation, not two independent ones; the imaginary half is not a separate spatial space.

**The boundary of the interpretations.** The algebra supplies the rotor and the double cover; it does not supply the quantisation of the angle or a dynamics. The identification of the sign with a physical spinor phase is an interpretation of the representation, not a derivation of the spin of a particle.

## Boosts

### The Boost Rotor

A boost along the unit real direction $\vec u$ of rapidity $\psi$ is the rotor
$$
\tilde U=\exp\!\left(\frac{\psi}{2}i\vec u\right)
=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u,
\qquad
\tanh\psi=\frac{v}{c}.
$$
It is Hermitian, $\tilde U^{*}=\tilde U$, of norm one, and it is not unitary: $\tilde U^{*}\tilde U=\tilde U^{2}\neq e_t$ unless $\psi=0$. Its sandwich is
$$
\mathrm{H}_{\tilde U}(\tilde Q_3)=\tilde U\,\tilde Q_3\,\tilde U,
$$
the element on both sides rather than an element and its inverse.

The boost moves the time axis. On the algebra unit,
$$
\mathrm{H}_{\tilde U}(e_t)=\tilde U^{2}=\cosh\psi\,e_t+i\sinh\psi\,\vec u,
$$
which is Hermitian and lies in $\mathbb{M}_{+}$; on the time axis,
$$
\mathrm{H}_{\tilde U}(ie_t)=i\tilde U^{2}=i\cosh\psi\,e_t-\sinh\psi\,\vec u,
$$
which is a four-vector with a spatial part. The centre is not preserved, the vector subspace is not preserved, and the product is not preserved:
$$
\mathrm{H}_{\tilde U}(\tilde Q_1\tilde Q_2)\neq
\mathrm{H}_{\tilde U}(\tilde Q_1)\mathrm{H}_{\tilde U}(\tilde Q_2)
$$
for $\psi\neq0$, because the missing factor is $\tilde U^{*}\tilde U=\tilde U^{2}$. The defect is first order in the rapidity, while the time dilation is second order.

**A boost is a change to a moving frame.** The rotor stores half the rapidity, and the sandwich carries the four-position of a world line to its rest frame; the rapidity is additive for collinear boosts. Interpreted physically, the boost is the change of inertial frame, and the rotor is the element that performs it.

**The boost spectrum is the Doppler pair.** As a $2\times2$ matrix the boost rotor is Hermitian of determinant one, and its eigenvalues are $e^{\pm\psi/2}$; their squares $e^{\pm\psi}$ are the red- and blue-shift factors of the frame change. The eigenvectors are the two spinors of the null directions along which the boost slides. Interpreted physically, the boost spectrum is the Doppler factor, and the doubling of the exponent is the two-way light travel.

**The boundary of the spectrum interpretation.** The eigenvalues are of the rotor, not of a four-vector, and the observed shift of a wave also depends on its direction. The algebra supplies the factor, not the emission or the observation.

**A boost is a motion, not an automorphism.** The boost preserves the interval and the two sectors, but it does not preserve the product, the centre or the vector subspace. Interpreted physically, a boost is a motion of the form which is not a symmetry of the algebraic structure; a rotation is both, and a boost is only the former. The time axis and the spatial axis are mixed, and the mixing is exactly the failure of multiplicativity.

**The time axis is frame-dependent.** The image of $ie_t$ is a four-vector with a spatial part $\sinh\psi$, and the image of $e_t$ leaves the centre for $\mathbb{M}_{+}$. Interpreted physically, the rest frame's time axis is not invariant; a boost carries it to the four-velocity of the moving frame, and the simultaneity plane tilts. The interval is what survives; the product of two events is not a frame-independent object.

**Two boosts are not a boost.** The product of two non-collinear boost rotors is a rotor whose polar decomposition has a rotation factor, the Wigner rotation. Interpreted physically, two successive non-collinear boosts are a boost followed by a rotation, and the rotation is the Thomas precession. The set of boosts is not a subgroup; the group is generated by the boosts and the rotations together.

**The boundary of the interpretations.** The boost is global and constant; the article does not read acceleration, gravity or a local frame field. The failure of multiplicativity is not a physical arrow of time, and the Wigner rotation is a property of the composition of the motions, not a derivation of a dynamical effect.

## The Orbits

### The Classification

The sandwich preserves the rank of the matrix image and, on the norm-one slice, the norm itself. On the material sector the sign and the vanishing of the norm give the causal classes:

| class | norm $\langle\tilde Q\rangle_{\natural}$ | interpretation |
| --- | --- | --- |
| timelike | $\langle\tilde Q\rangle_{\natural}<0$ | a world line of a massive particle |
| null | $\langle\tilde Q\rangle_{\natural}=0$, $\tilde Q\neq0$ | a point of the light cone; $N$-degenerate, a zero divisor of rank one |
| spacelike | $\langle\tilde Q\rangle_{\natural}>0$ | a separation outside the cone |
| zero | $\tilde Q=0$ | the origin, $N$-degenerate |

The rank is always preserved: rank two is $N$-regular, hence a unit, rank one is $N$-degenerate, a nonzero zero divisor, rank zero is the $N$-degenerate origin.

### The Interpretations

**The mass shell is an orbit.** The future timelike elements of a fixed norm form a single orbit of the proper orthochronous group, and the past elements form a second orbit. The orbit of the rest four-velocity $imc\,e_t$ is the future mass shell of mass $m$, with $\langle\tilde Q\rangle_{\natural}=-m^{2}c^{2}$. Interpreted physically, a particle of mass $m$ is a point on the orbit, and a change of frame moves it along the orbit; the mass is the invariant of the orbit, not a label attached to a representative.

**The light cone is an orbit, and a null vector has no rest frame.** The nonzero future null elements form a single orbit, and the past null elements a second. A null element is $N$-degenerate, a zero divisor of rank one, and no rotor carries it to the rest four-velocity, because the rest four-velocity is timelike. Interpreted physically, a massless particle has no rest frame; the future light cone is one orbit of directions, and the absence of a rest frame is the absence of a timelike representative.

**A frame is a point on the orbit.** The orbit is the physical object and the representative is a choice of frame. Interpreted physically, no frame is preferred; the interval, the mass and the causal class are the invariants, and the group acts transitively on the frames of a given orbit.

**The spacelike orbit is not a particle.** The spacelike elements of a fixed norm form one orbit, but no causal world line represents it. Interpreted physically, a spacelike separation is a relation between events, not a state of a particle.

**The boundary of the interpretations.** The algebra supplies the orbit and the invariant; it does not supply the mass spectrum, the coupling or the dynamics. The mass $m$ is an input, and the orbit is the set of frames of a particle of that mass. The future and past sheets are separate under the proper orthochronous group, and the article does not identify them.

## Reflections and the Two Chiralities

### The Reflection Formula

For $v$ with $\langle v\rangle_{\natural}=1$, so that $v\,v^{\natural}=e_t$, the **reflection** in the hyperplane $v^{\perp}$ is
$$
\boxed{\;\rho_v(\tilde Q_3)=-v\,\tilde Q_3\,v^{\natural}\;}.
$$
The right factor is the quaternion conjugate, which is the inverse of $v$ on the norm-one slice; the reflection is therefore written with the algebra's own conjugation and needs no operator inverse. The minus sign is what makes it a reflection: without it the map is an inner automorphism. On the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\}$ and on its real form $\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, the multiplication is Clifford and orthogonality coincides with anticommutation:
$$
v\tilde Q_3+\tilde Q_3v=-2\langle v,\tilde Q_3\rangle e_t.
$$
There $\rho_v$ fixes $v^{\perp}$ pointwise, negates $v$, and has determinant $-1$; it is an involution. On the quaternion and Hermitian subspaces a norm-one element acts by conjugation as a rotation rather than as a reflection, and on the whole algebra $\rho_v$ has determinant $+1$. The Cartan–Dieudonné theorem gives every isometry of the three-dimensional vector subspace as a product of at most three reflections $\rho_v$.

**A reflection is an odd isometry.** The reflection reverses one direction and fixes the hyperplane orthogonal to it; it is an isometry of the form and an orientation-reversing map of the vector subspace. Interpreted physically, it is a mirror: a parity in one direction, not a rotation.

**Parity is outside the connected group.** The unit group is connected, and a reflection is not a sandwich by a unit: the formula carries the minus sign. The reflections generate the orthogonal group of the vector subspace, which is the image of the Pin group; the versors themselves live in the Clifford algebra of that subspace, not in $\mathbb{B}^{\times}$. Interpreted physically, parity is a discrete symmetry not connected to the identity, and it is not a continuous motion. The Lorentz reflections are not of the shape $\rho_v$ and live in the Clifford layer, not in the algebra.

**Chirality is not an element of the algebra.** The two half-integral representations of the Lorentz group are conjugate, and the connected unit group does not exchange them; the exchange is an outer symmetry of the representation theory. Interpreted physically, chirality is a property of the representation, not an element of the algebra; the algebra's reflections act on the vector subspace, not on the spinor chirality.

**Every isometry of the vector space is a product of mirrors.** Cartan–Dieudonné writes every isometry of the three-dimensional vector subspace as at most three reflections. Interpreted physically, every orthogonal transformation of the spatial vector space is a product of mirrors; the statement is about the vector subspace, not about the full Lorentz group.

**The boundary of the interpretations.** The algebra's reflections are reflections of the vector subspace, not of spacetime; the spacetime parity and the chirality exchange are not elements of $\mathbb{B}$. The article does not supply a parity operator, a Dirac mass term or a chirality projection; it supplies the reflection formula and the representation statement on which those interpretations rest.

## Limits

The geometry of the algebra is the geometry of the norm and of its isometries. The unit group is eight-dimensional, the norm-one slice six-dimensional and the Lorentz group its six-dimensional quotient; the algebra carries the double cover, not the group. The sandwich is the action; the interval is the invariant; the product is preserved by a rotation and not by a boost. The orbits are the mass shells and the light cones; the reflections are odd and live outside the connected group.

The article does not derive the Lorentz group from the algebra: it reads the group that the norm already defines, and it reads the action that the dagger already supplies. It does not derive a dynamics, a field equation, a mass spectrum or a coupling. It does not supply a preferred frame; the frame is a choice, and the interval is what is left when the choice is made. It does not read acceleration, gravity or a local frame field. The finite-dimensional Hermitian sector is not the relativistic state space, and a boost carries the trace-one Bloch ball off its slice; that is a boundary of the interpretation, not a defect of the algebra.

## Summary

The norm-one group $\mathbb{B}^{\times}_{1}\cong SL_2(\mathbb{C})$ is the double cover of the proper orthochronous Lorentz group, and its compact part $Sp(1)\cong SU(2)$ is the double cover of the spatial rotations. The Lorentz group is the quotient by the central sign, not a subgroup of the quaternion layer; the algebra carries the spin frame. The dagger sandwich $\mathrm{H}_{\tilde Q}(\tilde Q_3)=\tilde Q\tilde Q_3\tilde Q^{*}$ is the change of frame: it preserves the two sectors, scales the norm by $|\langle\tilde Q\rangle_{\natural}|^{2}$, has kernel $\mathrm{U}(1)e_t$ on the algebra and $\{\pm e_t\}$ on the norm-one slice, and acts as $SO^{+}(1,3)$ there. The interval is the frame-independent object, and the central phase is not a frame.

A rotation is a unitary rotor, an algebra automorphism, with the angle halved in the element and the double cover $Sp(1)\to SO(3)$. A boost is a Hermitian norm-one rotor, not unitary, and not an automorphism: it preserves the interval and the sectors but not the product, the centre or the vector subspace. Two non-collinear boosts compose to a boost and a Wigner rotation. The orbits are the future and past mass shells and the future and past light cones; a null vector is a zero divisor and has no rest frame. The reflections $\rho_v$ are odd isometries of the vector subspace, the images of the Pin group and not sandwiches by the unit group; parity lies outside the connected Lorentz group, and chirality exchange is not an element of the group at all.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}^{\times}_{1}\cong SL_2(\mathbb{C})$ | norm-one group; double cover of $SO^{+}(1,3)$ |
| $Sp(1)=S^{3}\cong SU(2)$ | unit quaternions; double cover of $SO(3)$ |
| $\mathrm{H}_{\tilde Q}(\tilde Q_3)=\tilde Q\tilde Q_3\tilde Q^{*}$ | dagger sandwich; the change of frame |
| $\mathrm{U}(1)e_t$ | kernel of the sandwich on the algebra |
| $\langle\tilde Q\rangle_{\natural}$ | biquaternion norm; the interval on $\mathbb{M}_{-}$ |
| $\tilde u=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\vec u$ | rotation rotor |
| $\tilde U=\cosh\tfrac{\psi}{2}+i\sinh\tfrac{\psi}{2}\vec u$ | boost rotor; Hermitian and norm-one |
| $\rho_v(\tilde Q_3)=-v\tilde Q_3v^{\natural}$ | reflection in $v^{\perp}$ |
| $imc\,e_t$ | rest four-velocity; $\langle\tilde Q\rangle_{\natural}=-m^{2}c^{2}$ |
| $SO^{+}(1,3)$ | proper orthochronous Lorentz group; the frame group |

## Further Reading

- [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html), for the double covers, the sandwich, the orbits and the reflections.
- [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html), for the automorphism group and its real form.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra, §The Group of Units](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the unit group and the norm-one slice.
- [The Biquaternion Unit Group as a Topological Group](../articles_maths/the-biquaternion-unit-group-as-a-topological-group.html), for the topology of the group.
- [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html), for the compact real form and the quotient $U(\mathbb{B})/U(1)\cong SO(3)$.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the four-vector dictionary.
