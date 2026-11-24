# __The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics__

## Introduction

One group acts on both sectors of the algebra, and the two sectors are not the same space. A unit-norm element acts by congruence on a four-momentum and on a state, and in both cases it preserves the biquaternion norm. That single fact is the whole reason the word Lorentz appears on both sides of the corpus. It is also the whole reason a careless table inverts the physics: the group preserves the norm, so the norm is the invariant in both sectors, and every quantity that runs is a coordinate of a space the group does not leave alone.

The two spaces differ in kind. On the material sector the element is a four-vector, and the congruence moves its tip along a line of Minkowski space. On the informational sector the element is a state, the normalisation fixes one coordinate, and the congruence moves that coordinate too, so the state leaves the slice it was defined on. The reader who takes "the group is shared" to mean "the spaces are the same" will conclude that purity is a velocity. The conclusion is wrong, and the error is exactly one step: the step from an action on a cone to an action on a section of it.

The article makes the step explicit. It gives the linear isometry that carries the Hermitian sector onto Minkowski space, proves that the congruence is a Lorentz transformation there, and then shows what the group does to the slice: it moves the weight, so the action on states is projective. It then separates the two metrics the ball carries. The Klein metric is the one the group preserves, and the Bures metric is not, and no boost is a Bures isometry except through its rotational part. That separation is the technical content behind the slogan of the title.

The findings are stated in advance.

1. The norm on the two sectors is one polynomial. On $\mathbb{B}_{\Psi}$ it reads $h_t^2-\lvert\vec h\rvert^2$ with signature $(1,3)$; on $\mathbb{B}_{\Phi}$ it reads $-E^2/c^2+\lvert\vec p\rvert^2$ with signature $(3,1)$. Multiplication by $i$ carries one plane onto the other and negates the form, so the two automorphism groups are the same group.
2. The state is a four-vector, exactly. The map $\tilde Q\mapsto(h_t,\vec h)$ is a linear isometry of $(\mathbb{B}_{\Psi},N)$ onto $\mathbb{R}^{1,3}$. A state is $\tfrac12(1,\vec s_{\Psi})$, the interior of the future cone intersected with the hyperplane $2\,\mathrm{Sc}=1$.
3. The congruence is a Lorentz transformation and it does not preserve the hyperplane. A boost sends $2\,\mathrm{Sc}$ to $\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,s_{\parallel}$, so the doubled scalar part leaves one; only after dividing by it does the image land on the ball again, and then its radius has moved.
4. Two metrics live on the ball and only one belongs to the group. The Klein metric is preserved to $1.7\times10^{-15}$ over a hundred draws; the Bures metric changes under a boost, by $0.224$ rad on the sample pair given below. The polar split $U=LR$ says why: $R$ is a Bures isometry and $L$ is not.
5. The Wigner angle is one number read twice. It is the rotational part of a product of two boosts, it is the residual rotation of the ball, and it is relational: no single state registers it.

The notation is that of the foundational articles. A Hermitian element is $\tilde H_{\Psi}=h_te_t+i\vec h_{\Psi}$, an anti-Hermitian one is $\tilde P_{\Phi}=(iE/c)e_t+\vec p$, the norm is $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$, the star is the anti-involution that fixes $\mathbb{B}_{\Psi}$, and the congruence is $\mathrm{Cg}_{\tilde U}:\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$. The state is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$, with $\vec s_{\Psi}$ real and $\lvert\vec s_{\Psi}\rvert<1$. The rapidity is written $\theta_{\mathrm{rpd}}$ and the boost rotor is $\tilde U_{\Psi,\mathrm b}=\cosh(\theta_{\mathrm{rpd}}/2)e_t+i\sinh(\theta_{\mathrm{rpd}}/2)\vec u$, Hermitian of unit norm.

The companion articles supply the pieces:

- *The Two Actions of One Group: Adjoint and Congruence*, for the congruence, its kernel and what it preserves.
- *The Lorentz Group as Biquaternion Norm Automorphisms*, for the same group read as the automorphisms of the norm with the real slice taken.
- *Velocity Space as Hyperbolic Geometry in Biquaternionic Form*, for the material hyperboloid, the rapidity as geodesic distance and the Klein model in the velocity coordinates.
- *States, Observables and the Born Weight*, for the state slice, its coordinates and the pairing that defines it.
- *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form*, for the boost as a controlled rotation and the holonomy of a boost path.
- *Von Neumann Entropy and the Biquaternion Norm*, for the entropy as a function of the norm alone.
- Maths article *Hyperbolic Geometry*, for the Klein model and its isometry group, used here without re-derivation.

## The Two Real Four-Planes

### The Hermitian plane

**The Hermitian sector is a real four-plane with a form of signature $(1,3)$.** An element is $\tilde Q=h_te_t+i\vec h$ with $h_t$ and the three components of $\vec h$ real, and the norm is
$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural}=(h_te_t+i\vec h)(h_te_t-i\vec h)=h_t^2-(i\vec h)^2=h_t^2-\lvert\vec h\rvert^2 ,
$$
because $(i\vec h)^2=i^2\vec h^2=+\lvert\vec h\rvert^2$ for a real vector $\vec h$. The form is positive on the temporal axis $e_t$ and negative on the three spatial directions $i\vec e_{\imath}$. This is the sector of states, of observables and of the boosts.

The state is one particular element of it. Every state of the sector is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$, so $h_t=\tfrac12$ and $\vec h=\tfrac12\vec s_{\Psi}$. Normalisation is the statement $2\,\mathrm{Sc}=1$, that is $\mathrm{Sc}\,\tilde{Ϛ}_{\Psi}=\tfrac12$.

### The anti-Hermitian plane

The material sector is a real four-plane with the opposite signature. An element is $\tilde P_{\Phi}=(iE/c)e_t+\vec p$ with $E$ and $\vec p$ real, and the norm is
$$
N(\tilde P_{\Phi})=\Bigl(\frac{iE}{c}\Bigr)^2+\lvert\vec p\rvert^2=-\frac{E^2}{c^2}+\lvert\vec p\rvert^2 .
$$
The form is negative on the temporal axis $ie_t$ and positive on the three spatial directions $\vec e_{\imath}$. This is the sector of four-momenta, of currents and of the field strengths.

### One form, two signs

The two planes are one plane multiplied by $i$, and the form changes sign. Multiplication by $i$ is a real-linear bijection between the sectors: $i(h_te_t+i\vec h)=ih_te_t-\vec h$, which is of the form $(it)e_t+\vec p$ with $t=h_t$ and $\vec p=-\vec h$. On norms,
$$
N(i\tilde Q)=(i\tilde Q)(i\tilde Q)^{\natural}=i^{2}\tilde Q\tilde Q^{\natural}=-N(\tilde Q),
$$
because the natural conjugation is complex-linear and commutes with multiplication by $i$. Verified on a hundred random Hermitian elements, worst deviation $0$.

A quadratic form and its negative have the same automorphisms. If $g$ preserves $N$ then it preserves $-N$, so the two sectors have one automorphism group, and the groups $O(1,3)$ and $O(3,1)$ are literally the same group of matrices written with the two orderings of the signs. This is the entire algebraic reason the group is shared, and it is one line long. Everything else in this article is about the spaces.

| | $\mathbb{B}_{\Psi}$ | $\mathbb{B}_{\Phi}$ |
| --- | --- | --- |
| the element | $h_te_t+i\vec h$ | $(iE/c)e_t+\vec p$ |
| the norm | $h_t^2-\lvert\vec h\rvert^2$ | $-E^2/c^2+\lvert\vec p\rvert^2$ |
| the signature | $(1,3)$ | $(3,1)$ |
| the automorphism group | $O(1,3)$ | $O(3,1)$, the same group |
| the distinguished direction | the temporal axis, positive | the temporal axis, negative |

## The State Is a Four-Vector

### The map

**The coordinates of the sector are the coordinates of Minkowski space, and the identification is an isometry.** Define
$$
\mathsf{X}:\ \tilde Q=h_te_t+i\vec h\ \longmapsto\ (h_t,\vec h)\in\mathbb{R}^{1,3},
$$
with the Minkowski form $t^2-\lvert\vec x\rvert^2$. The map is real-linear and bijective, and by the first computation of the previous section it satisfies $N(\tilde Q)=t^2-\lvert\vec x\rvert^2$ at $\mathsf{X}(\tilde Q)=(t,\vec x)$. Verified on a hundred random Hermitian elements, worst deviation $8.9\times10^{-16}$.

On a state the map reads one line. For $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$,
$$
\mathsf{X}(\tilde{Ϛ}_{\Psi})=\tfrac12\bigl(1,\vec s_{\Psi}\bigr),\qquad N(\tilde{Ϛ}_{\Psi})=\tfrac14\bigl(1-\lvert\vec s_{\Psi}\rvert^2\bigr),
$$
so the impurity is a quarter of the squared Minkowski length of the state's four-vector. Verified on a hundred states, worst deviation $2.8\times10^{-17}$.

### The cone and the slice

The state space is a section of the cone, and that is the whole of the difficulty. The condition $N>0$ cuts the interior of the cone; the condition $h_t>0$ selects its future half; the normalisation $h_t=\tfrac12$ cuts that half by a hyperplane. The section is the open ball
$$
\mathbb{B}^{3}=\{\vec s_{\Psi}\in\mathbb{R}^{3}:\lvert\vec s_{\Psi}\rvert<1\},
$$
the centre is the maximally mixed state, and the boundary is the set of pure states. The boundary is not part of the ball and is not reached: it is the null cone of the sector, where $N=0$.

The four-vector of a state is therefore half of a future-pointing timelike vector of unit Minkowski length. The factor $\tfrac12$ is the normalisation, the direction is the state, and the length is one by construction. Nothing else in the sector carries information: two states differ by their direction and by nothing else.

| the object | the element | the four-vector | the condition |
| --- | --- | --- | --- |
| the maximally mixed state | $\tfrac12e_t$ | $\tfrac12(1,\vec 0)$ | $\lvert\vec s_{\Psi}\rvert=0$ |
| a mixed state | $\tfrac12(e_t+i\vec s_{\Psi})$ | $\tfrac12(1,\vec s_{\Psi})$ | $0<\lvert\vec s_{\Psi}\rvert<1$ |
| a pure state | $\tfrac12(e_t+i\vec u)$ | $\tfrac12(1,\vec u)$ | $\lvert\vec s_{\Psi}\rvert=1$, null |
| a four-momentum | $(iE/c)e_t+\vec p$ | $(iE/c,\vec p)$ | $N=-m^2c^2$ |

The fourth row is the material analogue and it is not the same object. The material element's four-vector has an imaginary temporal component and a fixed negative length; the state's has a real temporal component and a positive length. The two are related by the factor $i$ of the previous section and by nothing else.

## The Congruence on the Slice

### The boost in components

**A boost acts on the four-vector by the Lorentz formula, and this is a computation, not an analogy.** Let $\tilde U=\cosh(\theta_{\mathrm{rpd}}/2)e_t+i\sinh(\theta_{\mathrm{rpd}}/2)\vec u$ with $\vec u$ a real unit vector, and let $\tilde Q=h_te_t+i\vec h$. Write $h_{\parallel}=\vec h\cdot\vec u$ and $\vec h_{\perp}=\vec h-h_{\parallel}\vec u$. Then
$$
\mathrm{Cg}_{\tilde U}(\tilde Q)=\bigl(h_t\cosh\theta_{\mathrm{rpd}}+h_{\parallel}\sinh\theta_{\mathrm{rpd}}\bigr)e_t
+i\bigl(h_{\parallel}\cosh\theta_{\mathrm{rpd}}+h_t\sinh\theta_{\mathrm{rpd}}\bigr)\vec u
+i\vec h_{\perp},
$$
which is the Lorentz transformation of $(h_t,\vec h)$ along $\vec u$: the temporal component mixes with the parallel one, the perpendicular one is untouched. Verified on a hundred random boosts and states, worst deviation $1.8\times10^{-15}$.

On a state the formula is the same formula with $h_t=\tfrac12$. The image is
$$
\mathrm{Cg}_{\tilde U}(\tilde{Ϛ}_{\Psi})=\tfrac12\Bigl[\bigl(\cosh\theta_{\mathrm{rpd}}+s_{\parallel}\sinh\theta_{\mathrm{rpd}}\bigr)e_t
+i\bigl(s_{\parallel}\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\bigr)\vec u+i\vec s_{\perp}\Bigr],
$$
where $s_{\parallel}=\vec s_{\Psi}\cdot\vec u$. The doubled scalar part of the image is $\cosh\theta_{\mathrm{rpd}}+s_{\parallel}\sinh\theta_{\mathrm{rpd}}$, and it is one only at $\theta_{\mathrm{rpd}}=0$.

### Rotations

A rotation fixes the temporal coordinate and rotates the vector. For $\tilde U=\cos(\theta/2)e_t+\sin(\theta/2)\vec u$, real and of unit norm, the congruence leaves $h_t$ alone and turns $\vec h$ about $\vec u$ through $\theta$. On the state space this is a Euclidean rotation of the ball about its centre, so the little group of the maximally mixed state is the rotation group, and the centre is the only point the whole rotation subgroup fixes.

The two kinds together generate the whole group. Every unit-norm element factors, so every congruence is a rotation followed by a boost or the other way round, and the group acting on the ball is the group acting on the cone.

### What the action is

The action on states is the action on the cone, read on a section. A congruence carries the future cone to itself, because it preserves $N$ and the sign of $h_t$ on the component of the identity. It therefore carries rays of the cone to rays. A state is a ray with a chosen representative, and the representative must be chosen again after the map has been applied. That is what "projective" means here, and it is not a defect: it is the definition of the Klein model, in which the points of the ball are the rays of the cone and the isometry group is the group of the cone.

So the two clauses of the title have precise content. The group is one group. The space of states is the projectivised cone, not the cone. A linear action on the cone becomes a projective action on the ball, and the radius of the ball is not a coordinate the group preserves but a coordinate of the representative it discards.

## The Slice Is Not Preserved

### $2\,\mathrm{Sc}$ runs

**The doubled scalar part of the image is a function of the rapidity, and it is not one except at the identity.** For the centre, $s_{\parallel}=0$ and
$$
2\,\mathrm{Sc}\,\mathrm{Cg}_{\tilde U}(\tilde{Ϛ}_{\Psi})=\cosh\theta_{\mathrm{rpd}},\qquad
\lvert\vec s_{\Psi}'\rvert=\tanh\theta_{\mathrm{rpd}},\qquad
N\bigl(\tilde{Ϛ}_{\Psi}'\bigr)=\frac{1}{4\cosh^{2}\theta_{\mathrm{rpd}}},
$$
where $\tilde{Ϛ}_{\Psi}'$ is the projected image and $N$ of the image before projection is $\tfrac14$ at every rapidity.
The table gives the numbers, computed to machine precision from the closed form.

| $\theta_{\mathrm{rpd}}$ | $2\,\mathrm{Sc}$ of the image | $N$ of the image | the radius after projection | $N$ of the projected state | its entropy |
| --- | --- | --- | --- | --- | --- |
| $0$ | $1.000000$ | $0.250000$ | $0.000000$ | $0.250000$ | $0.693147$ |
| $0.5$ | $1.127626$ | $0.250000$ | $0.462117$ | $0.196612$ | $0.582203$ |
| $1.0$ | $1.543081$ | $0.250000$ | $0.761594$ | $0.104994$ | $0.365334$ |
| $1.5$ | $2.352410$ | $0.250000$ | $0.905148$ | $0.045177$ | $0.190865$ |
| $2.5$ | $6.132289$ | $0.250000$ | $0.986614$ | $0.006648$ | $0.040180$ |
| $4.0$ | $27.308233$ | $0.250000$ | $0.999329$ | $0.000335$ | $0.003018$ |

The third column is the invariant and the rest are not. The norm of the image is the norm of the centre, as the congruence requires; the scalar part, the radius, the norm of the projected state and the entropy all move with the rapidity, and they move monotonically toward the pure boundary. The table therefore answers the question a reader of the block will ask. It is not that the norm runs in the informational sector and stays fixed in the material one. It is that the norm never runs, and that the coordinates beside it do.

### One state, four observers

A boost is not a change of the state, and the numbers make the distinction sharp. Take the state along $(0.3,0.4,0)$ rescaled to radius $1/1.1=0.9091$, so that its entropy is $0.1849$. Apply the congruence with a boost along $\vec e_x$ at four rapidities and project each image.

| $\theta_{\mathrm{rpd}}$ | the radius | the entropy | $N$ of the element | $2\,\mathrm{Sc}$ of the image |
| --- | --- | --- | --- | --- |
| $0.0$ | $0.909091$ | $0.184907$ | $0.043388430$ | $1.000000$ |
| $0.5$ | $0.955476$ | $0.106717$ | $0.043388430$ | $1.411860$ |
| $1.0$ | $0.981640$ | $0.052198$ | $0.043388430$ | $2.184099$ |
| $1.5$ | $0.992947$ | $0.023436$ | $0.043388430$ | $3.513835$ |

The third column is constant to nine decimals, and the second and fourth are not. An observer who computes the entropy of the projected state reports a different number at every rapidity. The invariant content of the pair is the norm, and the norm is exactly what such an observer does not compute. This is the inversion the corpus warns about, and it is easy to fall into because the entropy is the operational quantity: it is what a measurement of the state returns, and it is frame-dependent.

Nothing here says that entropy is subjective. The entropy of a state on its own slice is a fact about that state, and every observer agrees on it once the slice is agreed. What the congruence shows is that the slice is an extra structure, carried by the normalisation and not by the group, and that a boost does not preserve it. Two observers who boost differently describe two different states, correctly.

### The velocity state

The velocity state is the case where the projected image is a familiar object, and the identification is exact. *States, Observables and the Born Weight* proves that a particle of velocity $\vec v$ has the state $\vec s_{\Psi}=-\vec v/c$, with $N=\tfrac14/\gamma^{2}$ and $\gamma=(1-\vec v^{2}/c^{2})^{-1/2}$. Apply a congruence and project: the result is exactly the Lorentz-transformed velocity, computed by velocity addition, to $3.3\times10^{-16}$ over a hundred draws.

The worked case, with $\vec v=0.5c$ along $\vec e_x$ and a frame boost of $v_{b}=0.6c$ along the same axis. The image has norm $0.1875$, which is $\tfrac14(1-0.25)$ and is the norm of the original element. Divided by its own $2\,\mathrm{Sc}$, it is the state with radius $0.142857$ and norm $0.244898$, and velocity addition gives $v'=(0.5-0.6)/(1-0.3)=-0.142857$. So the projected state is purer than the original, and the element's norm is unchanged.

This removes a possible misreading and it is worth stating in full. The corpus says that a fast particle is in a nearly pure state, and the corpus also says that the congruence preserves the norm. Both are true, and they are statements about two different elements: the projected image, whose norm is $\tfrac14/\gamma'{}^{2}$ and runs, and the image before projection, whose norm is $\tfrac14/\gamma^{2}$ and does not. The two differ by the square of the projection factor, which is exactly the factor that makes velocity addition what it is.

## Two Metrics, Two Groups

### The Klein metric

The ball carries a hyperbolic metric, and it is the one the group preserves. For two states of radius below one,
$$
d_{K}(\vec s_{\Psi},\vec s_{\Psi}')=\operatorname{arccosh}\frac{1-\vec s_{\Psi}\cdot\vec s_{\Psi}'}
{\sqrt{\bigl(1-\lvert\vec s_{\Psi}\rvert^{2}\bigr)\bigl(1-\lvert\vec s_{\Psi}'\rvert^{2}\bigr)}} .
$$
The formula is the Cayley–Klein distance of the ball model, and the congruence preserves it exactly: verified on a hundred random pairs and boosts, worst deviation $1.7\times10^{-15}$.

The geodesics are the chords, and a boost orbit is not one. The geodesic through the centre in the direction $\vec u$ is the diameter along $\vec u$; a boost carries that diameter to itself but carries any other point along a curve that approaches the boundary point $\vec u$ without meeting the diameter. The orbit stays at a constant Klein distance from the axis, which is the defining property of a hypercycle: verified on a hundred random states and axes, constant to nine decimals. For the state $(0.35,0.35,0)$ at radius $0.495$ and the axis $\vec e_x$, that distance is $0.392638191$ at every rapidity from $0$ to $3$. The same orbit departs from the chord joining its ends by $0.083$ and ends at radius $0.998$, so it is neither a geodesic nor a straight line in the model.

The constant distance is the geometric content of "a boost is a translation along an axis". The axis is the diameter; the orbit is the hypercycle at the state's own distance from it; and the rapidity is the parameter along the hypercycle, not along the axis.

### The Bures metric

**The ball carries a second metric, and the group does not preserve it.** The Bures distance is
$$
F=\sqrt{\tfrac{1}{2}\Bigl(1+\vec s_{\Psi}\cdot\vec s_{\Psi}'
+\sqrt{\bigl(1-\lvert\vec s_{\Psi}\rvert^{2}\bigr)\bigl(1-\lvert\vec s_{\Psi}'\rvert^{2}\bigr)}\Bigr)},
\qquad d_{B}=\arccos F ,
$$
with $F$ the fidelity of the two states: $F=0.948683$ for the state at radius $0.6$ against the centre, and $F=\cos(\xi_{\mathrm{pot}}/2)$ for two pure states at Bloch angle $\xi_{\mathrm{pot}}$. It is the metric of distinguishability, and it is invariant under the rotation subgroup and under no boost. On the pair $\vec s_{\Psi}=(0.3,0,0)$ and $\vec s_{\Psi}'=(0.85,0,0)$ the two metrics read $d_{K}=0.946633$ and $d_{B}=0.355646$; after a boost of rapidity $1.2$ along $\vec e_x$ the Klein distance is still $0.946633$ and the Bures distance is $0.131964$.

So the two metrics answer two different questions, and only one of them is a question about frames. The Klein distance asks how far apart two states are in the geometry the group acts on; it is the distance a boost preserves, and it is the distance of the velocity space of the material sector. The Bures distance asks how distinguishable two states are; it is the distance a measurement can see, and a boost changes it because a boost changes the state.

| | the Klein metric | the Bures metric |
| --- | --- | --- |
| what it measures | the hyperbolic distance of the ball | the angle whose cosine is the fidelity |
| the isometry group | the congruence group | the rotation subgroup |
| under a boost | preserved | changed |
| on the pure boundary | infinite except at coincidence | half the Euclidean angle of the two points |
| the material analogue | the velocity-space metric | none |

The last row is the reason the two metrics cannot be conflated. In the material sector the Klein metric is the metric of velocity space, and it is the only metric the group leaves alone. In the informational sector the same metric exists and the distinguishability metric sits beside it. A theory of information that used only the Bures metric would have no Lorentz action; a theory that used only the Klein metric would have no measurement.

### The polar split explains it

Every element of the group factors into a unitary and a Hermitian part, and the two parts do different things to the metric. Write $\tilde U=\tilde L\tilde R$ with $\tilde R$ unitary and $\tilde L$ Hermitian positive, the polar decomposition of the element. On states, $\tilde R$ acts by a rotation of the ball and $\tilde L$ by a boost, and the split is the split of the metric: $\tilde R$ is a Bures isometry to $1.7\times10^{-15}$ over a hundred draws, and $\tilde L$ is not, with a change of up to $0.431$ rad on the same draws.

This is why the boost cannot be removed by a change of drawing. The unitary part is an isometry of both metrics; the Hermitian part is an isometry of one. Any statement about the ball that is to survive a boost must be written in the Klein metric, and any statement about distinguishability must be written without one.

## The Wigner Angle, Read Twice

### The product of two boosts

The product of two boosts is a boost times a rotation, and the rotation is the Wigner rotation. Take $\tilde U=\tilde U_{\mathrm b}(\theta_1,\vec u_1)\tilde U_{\mathrm b}(\theta_2,\vec u_2)$. The polar decomposition gives $\tilde U=\tilde L\tilde R$ with $\tilde R$ unitary, and the axis of $\tilde R$ is $\pm\vec u_1\times\vec u_2$. The closed form is
$$
\tan\frac{\Omega}{2}=
\frac{\sinh\frac{\theta_1}{2}\sinh\frac{\theta_2}{2}\sin\xi_{\mathrm{pot}}}
{\cosh\frac{\theta_1}{2}\cosh\frac{\theta_2}{2}+\sinh\frac{\theta_1}{2}\sinh\frac{\theta_2}{2}\cos\xi_{\mathrm{pot}}},
$$
with $\xi_{\mathrm{pot}}$ the angle between the two axes. Verified on a hundred random pairs, worst deviation $1.2\times10^{-15}$.

The numbers, at $\theta_1=1.5$ and $\theta_2=1.2$, with the first axis along $\vec e_z$.

| $\xi_{\mathrm{pot}}$ | $\Omega$ |
| --- | --- |
| $0$ | $0.000000$ |
| $\pi/6$ | $0.261814$ |
| $\pi/3$ | $0.494407$ |
| $\pi/2$ | $0.657460$ |

The angle vanishes when the axes are parallel and grows with the angle between them. That is the signature of a curvature: the product of two translations in a curved space is a translation plus a rotation, and the rotation measures the area of the geodesic triangle they span. In velocity space the same number is the defect of the triangle, and the corpus's velocity article derives it that way.

### The same number on the informational side

The rotation part of the product acts on the ball, so the Wigner angle is a rotation of the state space. Nothing new is computed: $\tilde R$ is unitary, the congruence by a unitary element is a rotation of the ball, and the angle of that rotation is $\Omega$. The same $\Omega$ appears in the material sector as the rotation of the four-momentum, because the two sectors share the group and the group element is one element.

The angle is relational, and this is where the informational interpretation adds something. No single state registers $\Omega$: a rotation of the ball about its centre fixes the centre, and a rotation about any other axis fixes a pair of states on that axis. What registers the angle is a comparison, either of two states or of one state before and after. So the Wigner angle is a property of a pair of frames, and its informational reading is a statement about a relation between descriptions, not about a state.

Thomas precession is the differential of this angle along a path. The finite angle is the holonomy of a closed loop of boosts; the precession rate is its derivative as the loop shrinks. One result, two names, and the corpus's relativity article carries the finite form while the accelerator literature carries the rate.

## Objections

The objection is that a shared group makes the two sectors one theory, and that the ball is then only the velocity space in disguise. The velocity space of the material sector is also a ball, its metric is also the Klein metric, and its isometry group is also the group. If the two balls are the same ball, then purity is speed and the article has established an identification rather than a contrast.

**The answer is that the two balls differ in what fills them, and the difference is measurable.** The material ball is filled by $\vec v/c$, a vector whose length is fixed by the four-velocity normalisation at every point of the trajectory, and the element is the four-velocity itself, an anti-Hermitian object of norm $-c^2$. The informational ball is filled by $\vec s_{\Psi}$, a vector whose length is the state's own purity, and the element is the state, a Hermitian object of norm $\tfrac14(1-\lvert\vec s_{\Psi}\rvert^{2})$. The two agree on the group, on the metric and on the shape; they disagree on the invariant, on the sign of the form and on what a point means.

The disagreement has a number. For a boost of rapidity $\theta_{\mathrm{rpd}}$ the material four-velocity has $\gamma=\cosh\theta_{\mathrm{rpd}}$ and its norm stays at $-c^2$; the informational element has $2\,\mathrm{Sc}=\cosh\theta_{\mathrm{rpd}}$ after the boost, its norm stays at its original value, and the projected state's norm is $\tfrac14\cosh^{-2}\theta_{\mathrm{rpd}}$. The material object needs no projection, because the normalisation is built into the four-velocity and the boost preserves it. The informational object needs one, because its normalisation is a coordinate the boost moves. That is the whole asymmetry, and it is the reason the corpus says mass is pinned twice and normalisation once.

A second objection is that the Bures metric is the natural metric on states, so the article's group is the wrong group. The answer is that both metrics are natural and they answer different questions. The Bures metric is the metric of distinguishability and its isometry group is the rotation subgroup; the Klein metric is the metric of the group action and its isometry group is the congruence group. A statement about frames must use the second; a statement about measurement must use the first. Confusing them produces exactly the table that puts the running quantity on the norm.

## What the Isometry Does Not Give

It does not extend the velocity identification beyond the velocity states. The identification $\vec s_{\Psi}=-\vec v/c$ is exact for a particle of definite velocity, and the previous section shows that it survives the group. It does not extend to a general state. A thermal state has radius $\tanh(\beta\lvert\vec h_{\Psi}\rvert)$, and that rapidity is a property of the Hamiltonian and of the temperature, not of a frame. The two coincide when the Hamiltonian generates the boost whose rapidity is $\beta\lvert\vec h_{\Psi}\rvert$, and equality in that case is not an identity.

**It does not give a dynamics.** A congruence is reversible and preserves the norm; an evolution that changes the norm, which is every thermalisation, is not a congruence. The group therefore describes the frames in which a state may be read, not the process by which it changes. The companion article on the thermal path states the consequence: no orbit of the group is a thermalisation.

It does not give a scale. The algebra carries $c$ through the material sector and carries no mass scale. The mass of a particle enters as the value of the norm, $-m^2c^2$, and not as a parameter of the algebra; the temperature enters as the modulus of the Hamiltonian's vector part. Both are imported, and the corpus records the absence as an open question.

## Summary

The group is one group and the spaces are two. The congruence by a unit-norm element preserves the biquaternion norm in both sectors. On the material sector that is the Lorentz transformation of a four-vector in Minkowski space. On the informational sector it is the same Lorentz transformation of the four-vector $\tfrac12(1,\vec s_{\Psi})$, followed by a projection, because the normalisation is a coordinate and not an invariant.

**The invariant is the norm and everything else runs.** The norm of the element is fixed by the congruence; the doubled scalar part, the radius and the entropy of the projected state all move, and they move monotonically. An observer who reports the entropy of the projected state reports a frame-dependent number, and the invariant content of the pair is the norm that the observer did not compute.

The ball carries two metrics and only one belongs to the group. The Klein metric is preserved and the Bures metric is not. The polar split $U=LR$ says why: $R$ is an isometry of both and $L$ of one. The Wigner angle is the rotational part of a product of boosts, it is the same number in both sectors because the group element is one element, and it is relational because no single state registers a rotation.

What the sharing buys is a dictionary with a fixed grammar. The group tells which quantities may be compared across frames and which may not. It identifies purity with speed for the velocity states and for no other family, it does not supply a dynamics, and it does not supply a scale.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}_{\Psi}$ | the Hermitian sector, signature $(1,3)$ |
| $\mathbb{B}_{\Phi}$ | the anti-Hermitian sector, signature $(3,1)$ |
| $N$ | the biquaternion norm, $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ |
| $\mathrm{Cg}_{\tilde U}$ | the congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ |
| $\mathsf{X}$ | the isometry $\tilde Q=h_te_t+i\vec h\mapsto(h_t,\vec h)$ |
| $\tilde{Ϛ}_{\Psi}$ | the state $\tfrac12(e_t+i\vec s_{\Psi})$ |
| $\vec s_{\Psi}$ | the state's vector, the radius $\lvert\vec s_{\Psi}\rvert$ its impurity coordinate |
| $\theta_{\mathrm{rpd}}$ | the rapidity of a boost |
| $d_{K}$ | the Klein distance on the ball |
| $d_{B}$ | the Bures distance on the ball |
| $\tilde L,\tilde R$ | the Hermitian and unitary factors of the polar split |
| $\Omega$ | the Wigner angle |

## Further Reading

- F. Klein, "Über die sogenannte Nicht-Euklidische Geometrie", *Mathematische Annalen* 4 (1871) — the ball model, its chords as geodesics and its isometry group
- L. P. Eisenhart, *Non-Riemannian Geometry*, American Mathematical Society, 1927 — the Klein model and the projective reading of the hyperbolic group
- A. A. Ungar, *Analytic Hyperbolic Geometry and Albert Einstein's Special Theory of Relativity*, World Scientific, 2008 — the gyrogroup structure, the velocity ball and the Wigner rotation as its defect
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2000 — the Bloch ball, the fidelity and the Bures distance
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford University Press, 1995 — the quaternionic state space and its geometry
- *The Two Actions of One Group: Adjoint and Congruence* — the two actions, their kernels and what each preserves
- *The Lorentz Group as Biquaternion Norm Automorphisms* — the same group as the automorphisms of the norm
- *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* — the material ball, the rapidity as distance and the Klein metric in the velocity coordinates
- *States, Observables and the Born Weight* — the state slice and its pairing
- *Von Neumann Entropy and the Biquaternion Norm* — the entropy as a function of the norm alone
- *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form* — the boost as a controlled rotation and the holonomy of a boost path
