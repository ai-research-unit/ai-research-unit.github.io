# __What the Bures Metric Cannot See__

## Introduction

The state space of the informational sector carries two metrics, and they disagree about which transformations are motions. The Cayley–Klein metric is preserved by every congruence, so its isometry group is the whole six-dimensional group of the sector. The Bures metric is preserved by the rotations alone, so its isometry group is three-dimensional. The gap between the two is not a matter of taste. It is the gap between frames and channels, and it has a one-line proof.

The proof is a statement about the trace. A congruence by an element $\tilde U$ carries the trace functional to itself only when $\tilde U$ is unitary, and the unitary elements of the group are exactly the real unit quaternions, which are the rotations. Every boost changes the trace, hence takes a state off the normalised slice, hence is not a trace-preserving map. The Bures metric is the metric that is monotone under trace-preserving maps. A metric of that kind cannot be invariant under a map that does not preserve the trace.

The article states the equivalence, proves it, and then draws four consequences the hemisphere picture makes visible. The pole of the hemisphere moves under a boost, so the latitude is measured from a state and not from a frame. The order of two states by purity is not invariant, and the article gives a pair whose order reverses. The distance to the pure boundary is finite, so the third law cannot be read off the Bures metric at all. And what does survive is the conformal class of the boundary, which is where the group still acts.

The findings are stated in advance.

1. **The polar split separates the two actions.** Every unit-norm element is $\tilde U=\tilde L\tilde R$ with $\tilde L$ a boost rotor and $\tilde R$ a rotation rotor, and the split is unique. Verified on a hundred random elements to $5.1\times10^{-15}$.
2. **A congruence preserves the trace only if it is a rotation.** The map $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ satisfies $2\,\mathrm{Sc}(\tilde U\tilde Q\tilde U^{*})=2\,\mathrm{Sc}\,\tilde Q$ for every $\tilde Q$ if and only if $\tilde U\tilde U^{*}=1$, and on the group that holds if and only if $\tilde L=1$.
3. **Hence the three-way equivalence.** A congruence is a Bures isometry, a congruence preserves the state slice, and a congruence is a rotation: the three conditions are one condition.
4. **The Bures metric sees the state and not the frame.** Latitude and entropy are visible to it; the boost that connects two observers is not.
5. **The group survives on the boundary as the conformal group.** A boost scales the round metric of the pure-state sphere by a point-dependent factor and preserves every angle, verified to $1.2\times10^{-6}$ on a finite-difference probe that is limited by the probe.

The notation is that of the foundational articles. The state is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$ with $\vec s_{\Psi}$ real and $r=\lvert\vec s_{\Psi}\rvert<1$; the congruence is $\mathrm{Cg}_{\tilde U}:\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$; the star is the anti-involution fixing $\mathbb{B}_{\Psi}$; the trace is $2\,\mathrm{Sc}$. The rapidity is $\theta_{\mathrm{rpd}}$, the boost rotor is $\tilde U_{\mathrm b}=\cosh(\theta_{\mathrm{rpd}}/2)e_t+i\sinh(\theta_{\mathrm{rpd}}/2)\vec u$ and the rotation rotor is $\tilde U_{\mathrm r}=\cos(\theta/2)e_t+\sin(\theta/2)\vec u$, both of unit norm. The Bures distance is the angle convention $d_{B}=\arccos F$, with $F$ the fidelity, so that two pure states at Bloch angle $\phi$ are at $d_{B}=\phi/2$.

The hemisphere is not re-derived here. *The Fubini–Study Geometry and the Biquaternion Norm* proves that the Bures ball is the northern hemisphere of a round three-sphere of radius $\tfrac12$, with the maximally mixed state at the pole, the pure states on the equator and the latitude equal to the purity. This article takes that picture as a coordinate system and asks what the group does inside it.

The companion articles supply the pieces:

- *The Fubini–Study Geometry and the Biquaternion Norm*, for the hemisphere, its isometry group $O(3)$ and the Bures line element.
- *The Group Is Shared, the Space Is Not*, for the congruence as a Lorentz transformation, the projective action and the two metrics.
- *States, Observables and the Born Weight*, for the state slice and the statement that it is preserved by the unitary group and by nothing larger.
- *Quantum Channels and the Reversible/Irreversible Dichotomy*, for the channel category and the unitary channels inside it.
- *Coarse-Graining and the Biquaternion Entropy Functional*, for the monotonicity of the entropy and the direction of the second law.
- *Fisher Information and the Biquaternion Norm*, for the Fisher form as four times the Bures form.

## The Polar Split

### The factorisation

**Every element of the group factors into a boost and a rotation, and the factors are unique.** Write $\tilde U=\tilde L\tilde R$ with $\tilde L$ Hermitian positive of unit norm and $\tilde R$ real of unit norm. In the defining representation this is the polar decomposition of a determinant-one matrix into a positive Hermitian factor and a unitary one, and the determinant condition fixes the scalar part of each factor to one. Verified on a hundred random products of one boost, one rotation and one boost: $\lvert\tilde U-\tilde L\tilde R\rvert\le4.5\times10^{-16}$, $\tilde L^{\dagger}=\tilde L$ and $N(\tilde L)=1$ to $5.1\times10^{-15}$, $\tilde R$ real and $N(\tilde R)=1$ to $5.0\times10^{-15}$.

**The split names two kinds of transformation the corpus already separates.** $\tilde L$ is a boost rotor: Hermitian, so $\tilde L^{*}=\tilde L$, and its congruence is the Lorentz transformation of the previous article. $\tilde R$ is a rotation rotor: real, so $\tilde R^{*}=\tilde R^{-1}$, and its congruence turns the vector $\vec s_{\Psi}$ about $\vec u$. The first is the non-compact half of the group and the second is the compact half, and the split exhibits the group as the product of the two, which is the Cartan decomposition.

### What each factor does

**The two factors act on the two metrics differently, and the table is the summary of the article.**

| | the boost $\tilde L$ | the rotation $\tilde R$ |
| --- | --- | --- |
| the trace of the image | $\cosh\theta_{\mathrm{rpd}}+s_{\parallel}\sinh\theta_{\mathrm{rpd}}$ | unchanged |
| the state slice | not preserved | preserved |
| the position on the hemisphere | latitude and longitude both move | longitude only |
| the Klein metric | preserved | preserved |
| the Bures metric | changed | preserved |
| the map on states | projective, non-affine | linear, affine |
| the channel category | outside | inside |

**Every row of the table is a computation, and the rows are the argument of the next three sections.** The trace row is the theorem. The metric rows are the statement that one metric belongs to the group and the other does not. The last row is the reason the metric rows hold, and it is the conceptual content of the article.

## The Dividing Line Is the Trace

### The theorem

**A congruence preserves the trace if and only if it is a rotation.** For any element $\tilde Q$ and any unit-norm $\tilde U$,
$$
2\,\mathrm{Sc}\bigl(\tilde U\tilde Q\tilde U^{*}\bigr)=2\,\mathrm{Sc}\bigl(\tilde Q\tilde U^{*}\tilde U\bigr)
$$
by the cyclicity of the trace in the defining representation. The right side equals $2\,\mathrm{Sc}\,\tilde Q$ for every $\tilde Q$ if and only if $\tilde U^{*}\tilde U=1$, which is the unitarity of $\tilde U$. On the group, $\tilde U=\tilde L\tilde R$ gives $\tilde U^{*}\tilde U=\tilde R^{*}\tilde L^{2}\tilde R$, so unitarity holds if and only if $\tilde L^{2}=1$, and $\tilde L$ positive gives $\tilde L=1$.

**The consequence is that the state space is exactly the set the rotations preserve.** A congruence carries states to states when it carries the normalised slice to itself, and the slice is the level set $2\,\mathrm{Sc}=1$. So the congruences that act on the state space are the rotations, and this is the statement the corpus records as claim six of *States, Observables and the Born Weight*. Verified: a rotation changes the trace of a random Hermitian element by $8.9\times10^{-16}$ and a boost changes it by up to $10.09$.

**The boost therefore acts on states only after a re-pinning.** The linear image has trace $\cosh\theta_{\mathrm{rpd}}+s_{\parallel}\sinh\theta_{\mathrm{rpd}}$, which is one only at $\theta_{\mathrm{rpd}}=0$; dividing by it produces a map that is defined on the state space and is not linear. So there are two maps, and neither is a channel: the linear one is not trace-preserving and the re-pinned one is not affine.

**The non-affinity is a number.** Take the two states of the order-reversal table below, $\vec s_{\Psi}=(0.3,0,0)$ and $\vec s_{\Psi}'=(-0.35,0,0)$, mix them with weight $\lambda=0.4$ and boost along $\vec e_x$ at rapidity $1$: the image of the mixture has coordinate $0.721015$ while the mixture of the images has $0.682370$, a difference of $0.038645$. The same comparison for a rotation of the same angle differs by $1.1\times10^{-16}$. A channel is affine on the state space by definition, so no boost is a channel.

### The channel interpretation

**The Bures metric is the metric of the channel category, and this is why it cannot see the boost.** The Bures metric is monotone under completely positive trace-preserving maps, which is Petz's theorem, and it is the smallest of the monotone metrics. A monotone metric is one for which every channel is a contraction, so its isometries must be realised by channels that are themselves reversible, and the reversible channels are the unitary ones. So the isometries of the Bures metric are the unitary channels, and in this algebra those are the rotations.

**The two maps of a boost fall outside the category for different reasons, and both reasons are fatal.** The linear congruence is completely positive and not trace-preserving, so it is not a channel but a subnormalised one. The re-pinned map is trace-preserving and not affine, so it is not a channel at all. The Bures metric is a metric of the first category, and a frame change belongs to neither.

**This is the whole content of the title.** The Bures metric cannot see the boost because the boost is not in the category whose metric the Bures metric is. It is not that the metric is insensitive by accident; it is that the metric was selected for a different purpose. Asking the Bures metric to compare two frames is like asking a ruler to weigh.

## What the Bures Metric Sees

### The latitude and the entropy

**The visible coordinates are the latitude and the relative angle, and both are functions the corpus already uses.** Write the lift of the state as
$$
\mathsf{w}(\vec s_{\Psi})=\bigl(\sqrt{1-r^{2}},\ \vec s_{\Psi}\bigr)\in\mathbb{R}^{4},
$$
a unit vector of the round three-sphere, with $r=\sin\alpha$ and $\alpha\in[0,\pi/2]$ the latitude. The Bures distance is half the angle between two lifts, $d_{B}=\tfrac12\arccos\langle\mathsf{w}_1,\mathsf{w}_2\rangle$, which is the hemisphere statement of the companion article; verified on a hundred random pairs to $9.7\times10^{-16}$.

**The linear entropy is the square of the height above the equatorial plane.** On the slice $S_{\mathrm{lin}}=\tfrac12(1-r^{2})=\tfrac12\cos^{2}\alpha$, and $\cos\alpha$ is the first coordinate of the lift. So the linear entropy is $\tfrac12\mathsf{w}_0^{2}$: a function of the latitude alone, and therefore a function the Bures metric sees exactly.

**The distance from the pole is the other half of the same pair of coordinates.** For a state of radius $r$,
$$
d_{B}\bigl(\vec 0,\vec s_{\Psi}\bigr)=\tfrac12\arcsin r ,
$$
which follows from the lift at once: the centre lifts to $(1,\vec 0)$ and the angle to $\mathsf{w}$ has cosine $\sqrt{1-r^{2}}$. Verified against the fidelity formula on a hundred states, worst deviation $6.5\times10^{-16}$.

### The relative angle

**The Bures distance depends on three numbers and on nothing else.** It depends on $r$, on $r'$ and on $\vec s_{\Psi}\cdot\vec s_{\Psi}'$; it does not depend on the direction of either state. That is the statement that the isometry group contains the rotations, and the companion article proves that it contains nothing else: the isometry group is $O(3)$, of dimension three, against the six of the group.

**So the metric sees the shape of a configuration and not its placement.** Two states at the same radii and the same mutual angle are at the same Bures distance wherever they sit in the ball. Everything the metric can say is said in the pair $(r,r')$ and the angle between them, and the direction of the pair is invisible.

## What It Cannot See

### The pole moves

**The latitude is measured from a state, and a boost moves that state.** The pole of the hemisphere is the maximally mixed state, $\vec s_{\Psi}=0$. A boost carries it to radius $\tanh\theta_{\mathrm{rpd}}$, hence to latitude $\alpha=\arcsin(\tanh\theta_{\mathrm{rpd}})$, and the numbers are the table.

| $\theta_{\mathrm{rpd}}$ | the radius of the image of the pole | its latitude $\alpha$ | its Bures distance from the pole |
| --- | --- | --- | --- |
| $0.5$ | $0.462117$ | $0.480381$ | $0.240191$ |
| $1.0$ | $0.761594$ | $0.865769$ | $0.432885$ |
| $2.0$ | $0.964028$ | $1.301760$ | $0.650880$ |
| $3.0$ | $0.995055$ | $1.471304$ | $0.735652$ |

**The interpretation is that the trivial state of one frame is not the trivial state of another.** The pole is the maximally mixed state, and a boost carries it off the pole. What the boost changes is the normalisation against which the state is counted, not the element that the framework counts. So "this state is more mixed than that one" is a comparison that requires a frame, and the latitude is a coordinate of the frame rather than a property of the state. The corpus records the same fact for the thermal state in a moving frame.

### The order by purity is not invariant

**Two states can exchange their order by purity under a boost, and the exchange is easy to exhibit.** Take the states $\vec s_{\Psi}=(0.3,0,0)$ and $\vec s_{\Psi}'=(-0.35,0,0)$ and boost along $\vec e_x$ with rapidity $1$. The first has the smaller radius before and the larger after, and both distances from the pole move with it.

| | the radius before | $d_{B}$ from the pole before | the radius after | $d_{B}$ from the pole after |
| --- | --- | --- | --- | --- |
| $\vec s_{\Psi}=(0.3,0,0)$ | $0.3000$ | $0.152346$ | $0.8642$ | $0.521733$ |
| $\vec s_{\Psi}'=(-0.35,0,0)$ | $0.3500$ | $0.178786$ | $0.5612$ | $0.297906$ |

**The order reverses and the distance between the two states changes.** Before the boost the pair is at $d_{B}=0.331132$; after it is at $d_{B}=0.223827$. So a statement of the form "this state is purer than that one" has no frame-independent truth value, and no Bures distance can supply one, because the distance itself is not preserved.

**This is not a paradox and it is worth saying why.** Purity is the distance from the maximally mixed state, and that state is frame-dependent by the previous subsection. Any ordering built on it inherits the dependence. The invariant object is the biquaternion norm of the element, which is another number entirely, and the previous article shows that it does not move.

### The third law

**The pure boundary is at finite Bures distance, so the metric cannot express the third law.** The distance from the centre to the boundary is $\pi/4=0.785398$, and the diameter of the ball is $\pi/2$, attained by two orthogonal pure states. Both are finite. In the Klein metric the same boundary is at infinite distance, and that is the metric in which "unreachable" is a statement about distance.

**The approach to the boundary is exponential in the rapidity, and this is the quantitative form of the difference.** A path that runs along an axis with increasing rapidity sits at radius $\tanh\theta_{\mathrm{rpd}}$, and its Bures distance to the boundary point in the same direction is
$$
d_{B}=\tfrac12\arccos\bigl(\tanh\theta_{\mathrm{rpd}}\bigr),
$$
which tends to $e^{-\theta_{\mathrm{rpd}}}$ for large rapidity. The table records the ratio, and it tends to one.

| $\theta_{\mathrm{rpd}}$ | the radius | $d_{B}$ to the boundary | $e^{-\theta_{\mathrm{rpd}}}$ | the ratio |
| --- | --- | --- | --- | --- |
| $1$ | $0.761594$ | $0.352513$ | $0.367879$ | $0.958$ |
| $2$ | $0.964028$ | $0.134518$ | $0.135335$ | $0.994$ |
| $3$ | $0.995055$ | $0.049746$ | $0.049787$ | $0.999$ |
| $4$ | $0.999329$ | $0.018314$ | $0.018316$ | $1.000$ |
| $5$ | $0.999909$ | $0.006738$ | $0.006738$ | $1.000$ |

**So the boundary is near in the Bures metric and unreachable in the group.** Every finite rapidity leaves a finite gap; the gap shrinks exponentially and never closes. A statement of the third law is therefore a statement about the unboundedness of the group parameter, and any argument that rests on "the boundary is infinitely far" is an argument in the Klein metric that has been written in the wrong metric. If the rapidity of the path is the temperature parameter, which is the identification the thermal companion proposes, then the gap is $e^{-\beta\lvert\vec h_{\Psi}\rvert}$ and the third law is the statement that it does not vanish at finite $\beta$.

## Where the Group Survives

### The conformal boundary

**The group survives on the boundary, where it acts conformally and not isometrically.** The boundary is the set of pure states, a sphere, and the congruence group acts on it by Möbius transformations. A Möbius map scales the round metric by a point-dependent factor and preserves every angle. The check is the isotropy of the scale factor: at a hundred random points and boosts, the two principal scale factors of the map agree to $1.2\times10^{-6}$, which is the accuracy of the finite-difference probe and not a defect of the map.

**The lengths change, and the change is large.** Two orthogonal pure states are at $1.570796$ rad on the sphere; after a boost of rapidity $1$ they are at $0.952036$ rad. So the boundary metric is not preserved and its conformal class is.

**This is the resolution of the apparent contradiction between the two pictures.** The Bures metric sees no boost inside the ball, and the group sees every boost on the boundary up to scale. The two statements are consistent because a conformal map is not an isometry: it preserves the angles and the circles, which is what the celestial-sphere article uses, and it does not preserve the distances, and distance is what the Bures metric measures.

### What the conformal class buys

**The invariant object on the boundary is the conformal class of the round metric, and the group acts on it faithfully.** A statement written in angles, in cross ratios or in circles is a statement the group can carry; a statement written in lengths is not. That is a usable criterion for the corpus: any sentence about the pure states that is to be frame-independent must be conformal, and any sentence that uses a length is tied to a frame.

**The criterion also explains the Kähler structure.** The companion article proves that the Fubini–Study metric on the boundary is one quarter of the round metric and that the complex structure is supplied by the commutator. A Möbius map preserves the conformal class and the circles, so it preserves the complex structure up to the same scale. The algebra's complex structure therefore survives the group on the boundary, and the flat metric of the interior, which is not the Bures metric, does not.

## The Strongest Objection

**The objection is that the Bures metric is the physical metric on states, so an article that measures a metric by its isometry group has chosen the wrong yardstick.** Distinguishability is what a measurement returns, and the Bures metric is the minimal monotone metric; a metric that no boost preserves is then a metric that correctly records that a boost changes what can be distinguished.

**The answer is that both metrics are physical and they answer different questions.** The Bures metric answers how far apart two states are for an observer who has already fixed a frame; the Klein metric answers how far apart two frames are. A boost changes the first because it changes the state, and preserves the second because it is a change of frame. Neither statement is more fundamental, and the one that is wrong is the one that is used outside its category.

**A second objection is that the article's equivalence is a tautology.** Trace preservation, slice preservation and unitarity are three descriptions of one condition, and the article proves nothing new.

**The answer is that the equivalence is not a tautology but a dictionary, and the dictionary has consequences.** The three descriptions come from three different vocabularies, and each one supplies a fact the others do not: unitarity supplies the isometry of two metrics, slice preservation supplies the boundary of the state space, and trace preservation supplies the channel category and with it the monotonicity of the Bures metric. The content is in the last one, and it is the reason the title is a statement about a category and not about a formula.

**A third objection is that the boost is a symmetry of the theory, so a metric that breaks it must be an artefact.** The answer is that the boost is a symmetry of the algebra and not of the state space: it acts on the cone and not on the section. A metric on the section has no reason to inherit a symmetry of the cone, and the Bures metric does not. The Klein metric does inherit it, and that is exactly why it is not monotone under channels.

## What the Article Does Not Claim

**It does not rank the two metrics.** Each is the metric of a category, and the article's point is that the categories are different. A reader who takes "cannot see" as a defect has the wrong picture: a ruler that cannot weigh is not a bad ruler.

**It does not say that entropy is subjective.** The entropy of a state is a function of its radius, and every observer agrees on it once the state is agreed. What runs under a boost is the radius of the re-pinned image, and the previous article establishes that.

**It does not give a dynamics.** The channel category is where dynamics lives, and the article says that the frame changes are outside it. That is a statement about what a frame change is not, and it leaves the question of what a thermalisation is exactly where the thermal-path article leaves it.

**It does not prove the isometry group is $O(3)$.** That is the companion article's result, cited and used. What is proved here is the equivalence of the three descriptions and the consequences that follow from the hemisphere picture.

## Summary

**The group splits into a boost and a rotation, and only the rotation preserves the trace.** The polar decomposition $\tilde U=\tilde L\tilde R$ is unique, the linear congruence by $\tilde U$ preserves $2\,\mathrm{Sc}$ for every element if and only if $\tilde U$ is unitary, and on the group that means $\tilde L=1$. So the congruences that carry states to states are the rotations, which is why the state space is preserved by $U(2)$ and by nothing larger.

**The Bures metric is the metric of the channel category, and a boost is not a channel.** The linear congruence of a boost is completely positive and not trace-preserving; the re-pinned map is trace-preserving and not affine, with a non-affinity of $0.0112$ against $1.1\times10^{-16}$ for a rotation. The Bures metric is monotone under channels and its isometries are the unitary channels, which are the rotations. So the metric is blind to the boost for a structural reason and not by accident.

**Four consequences follow, and each is a number.** The pole moves to latitude $\arcsin(\tanh\theta_{\mathrm{rpd}})$, so purity is a frame-dependent coordinate. Two states at radii $0.30$ and $0.35$ reverse their order under a boost of rapidity one, becoming $0.8642$ and $0.5612$. The pure boundary is at the finite Bures distance $\pi/4$, and the gap along such a path closes as $e^{-\theta_{\mathrm{rpd}}}$, so the third law is a statement about the group parameter and not about distance.

**What survives is the conformal class of the boundary.** A boost scales the round metric of the pure-state sphere by a point-dependent factor and by the same factor in every direction at a point — the two principal scale factors agree to $1.2\times10^{-6}$ — while the lengths change, from $1.570796$ to $0.952036$ rad on the sample pair. So the group acts on the boundary by conformal maps, and that is the only place where the full six-dimensional action is visible in the geometry of the state space.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde{Ϛ}_{\Psi}$ | the state $\tfrac12(e_t+i\vec s_{\Psi})$ |
| $r$ | the radius $\lvert\vec s_{\Psi}\rvert$ |
| $\alpha$ | the latitude, $r=\sin\alpha$ |
| $\mathsf{w}$ | the lift $(\sqrt{1-r^{2}},\vec s_{\Psi})$ to the unit three-sphere |
| $d_{B}$ | the Bures distance, $\arccos F$ |
| $d_{K}$ | the Cayley–Klein distance |
| $F$ | the fidelity, $\cos d_{B}$ |
| $\tilde L$ | the boost factor of the polar split, Hermitian of unit norm |
| $\tilde R$ | the rotation factor, real of unit norm |
| $\theta_{\mathrm{rpd}}$ | the rapidity of a boost |
| $2\,\mathrm{Sc}$ | the trace |
| $S_{\mathrm{lin}}$ | the linear entropy $\tfrac12(1-r^{2})$ |

## Further Reading

- D. Petz, "Monotone metrics on matrix spaces", *Linear Algebra and its Applications* 244 (1996) 81–96 — the monotone metrics, the Bures metric as the minimal one, and the role of complete positivity
- A. Uhlmann, "The 'transition probability' in the state space of a *-algebra", *Reports on Mathematical Physics* 9 (1976) 273–279 — the transition probability and the Bures distance
- I. Bengtsson and K. Życzkowski, *Geometry of Quantum States*, 2nd ed., Cambridge University Press, 2017 — the Bloch ball, the Bures metric, the hemisphere and the monotonicity
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2000 — the fidelity, the trace distance and the channel category
- A. A. Ungar, *Analytic Hyperbolic Geometry and Albert Einstein's Special Theory of Relativity*, World Scientific, 2008 — the Klein model and its isometry group
- *The Fubini–Study Geometry and the Biquaternion Norm* — the hemisphere of radius $\tfrac12$, its isometry group $O(3)$ and the Bures line element
- *The Group Is Shared, the Space Is Not* — the congruence as a Lorentz transformation, the projective action and the two metrics
- *States, Observables and the Born Weight* — the state slice and the unitary group as its stabiliser
- *Quantum Channels and the Reversible/Irreversible Dichotomy* — the channel category and the unitary channels inside it
- *Fisher Information and the Biquaternion Norm* — the Fisher form as four times the Bures form
