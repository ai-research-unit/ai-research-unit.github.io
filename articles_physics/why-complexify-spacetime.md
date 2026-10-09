# __Why Complexify Spacetime?__

## The Question

Why would anyone propose that the fundamental arena of physics is not real Minkowski space $\mathbb{R}^{3,1}$, but a complexified space whose coordinates are biquaternions?

The question is fair. Real spacetime works. General relativity describes gravity with extraordinary precision. Quantum field theory describes matter and forces with extraordinary precision. Neither requires complex coordinates. So why complexify?

This article lays out the motivations. They are not proofs. They are structural hints — reasons to suspect that the real slice is a projection of something larger, and that the complex structure is doing work that the real formalism hides.

Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. In a material medium, $c$ is the local speed of light, and it varies from point to point with the local electromagnetic properties. The symbol $v$ is reserved for particle and frame velocities.

## What Minkowski Knew

In most modern textbooks, the Minkowski interval is written with a metric of signature $(-,+,+,+)$:

$$
ds^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2.
$$

The minus sign sits explicitly in the metric, encoded in $\eta_{\mu\nu} = \mathrm{diag}(-1,+1,+1,+1)$. This is the standard convention. It is clean, it generalizes to curved spacetime, and it fits the tensor formalism.

But it was not always so. Minkowski himself, and most physicists before the 1960s, wrote the interval differently:

$$
ds^2 = (ic_0\,dt)^2 + dx^2 + dy^2 + dz^2.
$$

Here the imaginary unit $i$ multiplies the time coordinate and the vacuum speed of light. The metric is **Euclidean** — all plus signs. The Lorentzian structure is not in the metric; it is in the coordinate. This is the $ict$ convention.

Minkowski's original insight was that space and time are not separate entities but a single four-dimensional structure. In his 1908 lecture *Space and Time*, he wrote:

> "Henceforth space by itself, and time by itself, are doomed to fade away into mere shadows, and only a kind of union of the two will preserve an independent reality."

The $ict$ convention is a precise expression of this union. It says: space and time are unified not by a metric with mixed signs, but by a **complex structure**. The imaginary unit is not a computational trick; it is the algebraic expression of the fact that time is not simply another spatial dimension.

## What $ict$ Does

With the substitution $x^0 = ic_0\,t$, the Minkowski interval becomes

$$
ds^2 = (x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2,
$$

which is the ordinary Euclidean quadratic form in four real variables. Three consequences follow.

**1. Lorentz transformations look like rotations.** A boost becomes a rotation in a plane mixing time and space, but with an **imaginary angle**. The mathematics of rotations — simpler than the mathematics of boosts — carries over almost unchanged. The Lorentz group $SO(3,1)$ acts on the variables $(x^0, x^1, x^2, x^3)$ as the group of complex rotations that preserve the Euclidean form, i.e., $SO(4,\mathbb{C})$ restricted to the appropriate real slice.

**2. The wave equation becomes the Laplacian.** The d'Alembertian

$$
\Box = -\frac{1}{c_0^2}\frac{\partial^2}{\partial t^2} + \nabla^2
$$

becomes, with $x^0 = ic_0 t$,

$$
\Box = \frac{\partial^2}{\partial (x^0)^2} + \nabla^2,
$$

which is the ordinary Euclidean Laplacian in four dimensions. Maxwell's equations and the wave equation take their simplest possible form.

**3. The signature is algebraic, not postulated.** The minus sign in the time–time component arises from $i^2 = -1$. It is not an independent input; it is a consequence of the complex structure of the time coordinate. In the metric convention, the minus sign is put in by hand. In the $ict$ convention, it is derived.

## What Was Lost — and Why the Loss Is Technical

The switch away from $ict$ happened for good technical reasons, and it is worth being precise about them before asking whether the insight survives.

**1. Curved spacetime.** In general relativity, the metric $g_{\mu\nu}$ is a dynamical field. There is no global coordinate transformation that makes it Euclidean in the way $x^0 = ict$ does for flat spacetime. The $ict$ convention is tied to the existence of a global inertial frame.

**2. Quantum field theory.** The Wick rotation $t \to -i\tau$ connects Lorentzian QFT to Euclidean statistical mechanics. In the modern formulation, this is understood as a deformation of the metric, not a change of coordinates. Writing $ict$ makes the rotation look like a coordinate change, which obscures the fact that it is really a change in the causal structure.

**3. Spinors and the Dirac equation.** The Dirac equation is naturally written in terms of a Lorentzian metric. The $ict$ convention interacts awkwardly with the spinor formalism, because spinors transform under the Lorentz group in a way that depends on the signature.

**4. Vectors and one-forms.** In differential geometry, tangent vectors and cotangent vectors are genuinely different objects. The $ict$ convention lets you avoid distinguishing them, because the Euclidean-looking metric has no off-diagonal structure. This is a pedagogical simplification that becomes a liability in more advanced contexts.

These are real problems, and they explain why the $ict$ convention was abandoned. But they are **technical** problems, not **physical** ones. The physical content — that time is structurally different from space, and that this difference is encoded in a sign or an imaginary unit — is the same in both conventions. The question is whether the technical problems reflect a genuine deficiency of the $ict$ convention, or a deficiency of the frameworks that were built on the metric convention.

This blog takes the second view. The technical problems are real, but they are problems with the global $ict$ convention, not with the underlying insight. The insight — that the Lorentzian signature is a projection of a complex structure — survives, and it points toward a larger structure that the metric convention obscures.

## The Debate, and What Is Not New in It

The arguments above are not the invention of this blog. They were put and answered by others, and the exchange is worth recording, because it shows which parts of the case are contested and which are settled.

The defence of $ict$ rests on the observation that the substitution $x^0 = ict$ makes the Lorentz transformation an honest rotation. With an imaginary rotation angle $\chi$ the identities

$$
\cos i\chi = \cosh\chi, \qquad \sin i\chi = i\sinh\chi
$$

turn a rotation by $i\chi$ into a boost of rapidity $\chi$. The hyperbolic form of the boost, the velocity-addition theorem as the tangent addition formula, and the interpretation of the transformation as a rotation in a plane are all consequences. This reading goes back to Sommerfeld's 1909 treatment, which is the source Minkowski's own presentation is usually read through. One claim made in the $ict$ defence is sharper than the rest and is worth stating on its own: that $ict$ does not *hide* the non-compactness of the Lorentz group but **reveals** it, since $\cosh$ and $\sinh$ are precisely where the unboundedness enters. Every identity in this paragraph is exact.

The objections are the ones this article already treats as real. The first is that the device is tied to a global inertial frame and does not generalise to a curved metric — the objection that decided the question in gravitational physics. The second is subtler: if a rotation by an imaginary angle is taken at face value, it invites reading Minkowski space as a complexified $\mathbb{C}^4$, and the extra real directions that appear carry nothing observable. That objection is not about the algebra of the substitution, which is exact, but about what one is tempted to make of it.

The position of this blog is that the first objection is answered by making the complex structure local, which is the whole content of *The Complex Structure Should Be Local* above: the coefficient becomes $q'_0 = ct$ with $c$ the local speed of light, and the Euclidean form of the wave operator is preserved in any medium. The second objection is the more useful one, and it is the reason this article insists on the sector structure. A complexified coordinate carries eight real parameters, and if all eight were directions of space the theory would have unobservable dimensions. In the biquaternion framework they are not: the material sector keeps the real spatial parts and the imaginary time part, the informational sector keeps the complementary ones, and the signature of each is a projection of the complex structure rather than an extra dimension. The disciplines that make this precise are the ones stated in *Conventions in the Biquaternion Universe*.

What the exchange does not settle is whether the $ict$ convention should be used *in practice*, and this article does not claim that it should. It claims only that the substitution is not an inelegance to be discarded, and that the structure it exposes — a complex coordinate whose imaginary unit supplies the sign — is a fact about the geometry rather than a trick of notation. The source of the recorded exchange is the 2013 discussion by I. Guzmán de Rojas, "By dismissing Minkowski's notation $x_4 = ict$ are we not losing an essential aspect of space-time structure?"; it is an informal thread, cited as an instance of the debate and not as authority.

## What We Forgot

The $ict$ convention points toward something the metric convention hides: that **Minkowski space is a real slice of a complexified space**. The complex structure is not an accident of notation; it is a structural feature of the geometry.

This is the intuition that motivates the broader hypothesis this blog explores: that the fundamental arena of physics is a complexified space whose coordinates are biquaternions. A point in this space is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

with complex coefficients

$$
Q_\mu = q_\mu + i\,q'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The material sector is described by the real parts $q_\mu$ for $\mu = 1, 2, 3$ — the spatial parameters $x, y, z$ — together with the imaginary time part $q'_0$. The informational sector — the sector whose elements carry the operator algebra of quantum physics — is described by the imaginary parts $q'_j$ for $j = 1, 2, 3$ — the spatial parameters $x', y', z'$ — together with the real time part $q_0$. The time coefficient carries the $ict$ structure explicitly: $q'_0 = ct$, where $c = 1/\sqrt{\epsilon\mu}$ is the **local** speed of light in the medium. In vacuum, $c = c_0$ and the familiar $ic_0 t$ form is recovered.

In this framework, the Lorentzian signature of the real slice is not postulated; it emerges algebraically from the complex structure. The metric convention, for all its technical convenience, hides this emergence.

## The Complex Structure Should Be Local

The $ict$ convention, as usually written, uses the vacuum speed of light $c_0$. This makes the complex structure **global**: the same $c_0$ everywhere, the same imaginary unit everywhere.

But the electromagnetic properties of a medium suggest that the complex structure should be **local**, in the same spirit as the metric in general relativity. In a material medium with permittivity $\epsilon$ and permeability $\mu$, the speed of light is

$$
c = \frac{1}{\sqrt{\epsilon\mu}},
$$

which differs from $c_0$. If the complex structure is determined by the local electromagnetic properties, then the correct time coefficient is $q'_0 = ct$, not $c_0 t$. In vacuum, $c = c_0$ and the two coincide. In a medium, they differ.

This is the local version of the $ict$ convention. It makes the complex structure a **field**, varying from point to point, in the same way that the metric $g_{\mu\nu}(x)$ varies in general relativity. The $ict$ convention becomes the vacuum limit of a more general local structure, just as special relativity is the local limit of general relativity.

The d'Alembertian argument supports this reading. In a medium with speed of light $c$, the wave operator is

$$
\Box = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2,
$$

which becomes the ordinary Euclidean Laplacian in four dimensions when written in terms of the local complex coordinate $ict$. The Euclidean form is preserved in **any** medium, not just in vacuum. This is a structural argument in favor of the local complex structure: the Euclidean character of the wave operator is a medium-independent fact, and it is captured precisely by the local complex coordinate.

Note the structural parallel with the signature argument. In the metric convention, the signature is an input; in the $ict$ convention, it is derived. Likewise, in the global $ict$ convention, the complex structure is an input; in the local version, it is derived from the local electromagnetic properties of the medium. In both cases, what looks like a fundamental postulate in the real formalism becomes a derived quantity in the complexified formalism.

## Additional Motivations

Beyond the historical and structural arguments, several independent lines of thought support the complexification program.

**Wick rotation.** The analytic continuation $t \to -i\tau$ connects Lorentzian QFT to Euclidean statistical mechanics. The partition function of a quantum field theory at finite temperature is computed by continuing to imaginary time and imposing periodic boundary conditions, with the period being the inverse temperature. This is not merely a mathematical convenience: imaginary time is **thermodynamic time**. The imaginary direction is where temperature, entropy, and statistical weight live. If imaginary time already carries thermodynamic meaning, it is natural to ask whether the imaginary directions of a full complexified spacetime might also carry informational meaning. This is a question, not a claim.

**Holography.** In AdS/CFT and related frameworks, the bulk geometry is dual to boundary information. The radial direction in the bulk is not just a spatial direction; it is a renormalization scale, along which moving corresponds to integrating out degrees of freedom. Geometry and information are dual descriptions of the same structure. If extra dimensions can be informational in holography, it is natural to ask whether the imaginary directions of a complexified spacetime could play an analogous role — not "extra space" in the ordinary sense, but directions carrying informational content. This is a structural analogy, not a derivation.

**Twistor theory.** Penrose's twistor theory is built on complexified Minkowski space. Twistors are elements of $\mathbb{C}^4$, and Minkowski space is a real slice. The complex structure is not an add-on; it is the fundamental arena. Twistor theory has produced deep results — the nonlinear graviton construction, the Penrose transform, the twistor-string correspondence — even though it has not replaced standard physics. If twistor theory complexifies spinor space, and the $ict$ convention complexifies time, it is natural to ask whether the two complexifications are related. This blog explores whether they are: both could be projections of a single complexified spacetime.

**Other routes that also decline the postulate.** The program is not the only one to treat the Minkowski geometry as something to be explained rather than assumed. The survey by Kassandrov that is the source of this list — the companion of the paper behind the corpus's *The Algebrodynamical Programme* — separates the attempts by their first principle. One family keeps canonical Minkowski space and deforms it through an inserted parameter or an enlarged arena: a fundamental length and mass (Kadyshevsky), Euclidean time (Pestov), the Clifford space-time of Hestenes and Pavšič, a special six-dimensional geometry (Urusovskii). A second family sets out to **derive** the geometry from something more primitive: a theory of physical structures (Kulakov), binary geometrophysics (Vladimirov), a quaternionic theory of relativity (Yefremov), Finslerian anisotropic geometry (Bogoslovsky), the geometry of polynumbers (Pavlov), a metrical geometry built on a "World function" (Rylov) — and, in the same family, the algebrodynamics of Kassandrov himself. The complexification program of the present article belongs to the second family in its aim, since its signature is derived and not postulated. This is a map of the neighbourhood, not a fourth argument of the same kind as the three above: the distinction the source draws is between a structure inserted into Minkowski space and a geometry the algebra supplies, and the source's own caution is worth keeping — these approaches "differ essentially one from another in the character of the first principle", so the list is a family resemblance and not an agreement.

**Where the derivation claim reaches farthest.** One of the sources just listed states the aim in a stronger form than a motivation. In the algebrodynamical programme of Kassandrov the primary equation is nonlinear, and its non-trivial solutions take their values on the **null divisors** of the algebra — the complex light cone. The programme argues that such null fields can exist only on a manifold of **indefinite** signature, so the pseudo-Euclidean structure is not merely obtained from the algebra but is a **necessary condition for a non-trivial field to exist at all**, which is the sharpest form the "the signature is derived" family takes. The claim belongs to that programme, rests on its nonlinear primary equation, and is no derivation inside the corpus's linear framework; it is recorded in *The Algebrodynamical Programme* and is the counterpart, on the signature boundary, of that article's self-quantized charge.

## What This Program Does Not Claim

It is important to be clear about what this program does not claim:

1. **It does not claim that real spacetime is wrong.** The real slice reproduces ordinary Minkowski space. All the successes of standard physics are preserved.

2. **It does not claim that the imaginary directions are observable in the ordinary sense.** Their effects would be indirect.

3. **It does not claim to have a complete theory.** The dynamics of the coupling between the material and informational sectors is not yet specified. The empirical predictions are not yet worked out.

4. **It does not claim that complexification is the only way forward.** It is one direction among many. Its virtue is that it connects to existing structures — the $ict$ convention, the Wick rotation, holography, twistor theory — rather than standing alone.

## The Structural Intuition

The core intuition is this: **the real slice is a projection, and the complex structure is what is being projected.** The metric convention sees the projection and takes it for the whole. The complexified convention asks what is being projected and why.

The metric convention tells you **what** the geometry is. The $ict$ convention tells you **why**. And the "why" may be where the next physics lies.

This is not a proof. It is a research program. The motivations above are reasons to take it seriously, not reasons to believe it. The next articles lay out the mathematical structure in detail: first the two natural subspaces of the biquaternion algebra — the material sector $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$ — and then the objects that live in each.

## Physical Readings

Complexification can be read twice, and the two readings point in opposite directions. Read backwards it recovers Minkowski's $ict$ as a coordinate device and makes the Lorentzian signature an output of the complex structure rather than an axiom. Read forwards it makes the complex structure *local*: the algebra is one object, the speed $c$ is the scale of its embedding in physical spacetime, and a change of the embedding is a change of the local complex structure that moves the interval and the composition while the probability form and the cone stay (*Conventions in the Biquaternion Universe*, *Electromagnetism in Media — The Local Complex Structure at Work*). The article's additional motivation reads the other end of the same fact: the null-divisor fields exist only on manifolds of indefinite signature, so the Lorentzian signature is a necessary condition of a non-trivial dynamics.

## Summary

The corpus adopts the complexified convention: time is written $ict$ and the geometry is carried by the complexified algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, not by a real four-dimensional vector space with a metric. The article states why. The $ict$ convention is Minkowski's own, and the metric convention of signature $(-,+,+,+)$ is a later re-writing that suppresses the complex structure while preserving every result; what the re-writing lost is the reason the factors of $i$ were there. Reinstating them makes the real slice a **projection** and the complex structure the thing projected: the metric convention says *what* the geometry is, the complexified convention asks *why*.

Three independent motivations support the reading, and none of them is a derivation. The **Wick rotation** continues a Lorentzian theory to imaginary time and computes the finite-temperature partition function there, so imaginary time is already thermodynamic time. **Holography** makes a geometric direction an informational one, the radial direction of the bulk standing for a renormalization scale. **Twistor theory** is built on complexified Minkowski space, with Minkowski space only a real slice of it. Each is a structural analogy, stated as a reason to take the program seriously and not as a reason to believe it. The program is one of several that decline to take the Minkowski geometry as given; the neighbouring attempts are mapped in *Additional Motivations*, and the distinction this program keeps is that the signature is derived from the complex structure rather than inserted as a parameter.

The program claims neither that real spacetime is wrong, nor that the imaginary directions are observable in the ordinary sense, nor completeness. The coupling between the material and the informational sectors is not yet specified, and no quantitative prediction yet distinguishes the framework from standard physics. The local speed of light $c=1/\sqrt{\epsilon\mu}$ enters as the local scale factor of the complex structure, so the $ict$ convention is the vacuum approximation of a more general local complex structure, in the same way that special relativity is a local approximation of general relativity. The two subspaces the reading singles out, the material sector $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$, are developed in the articles that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum (global constant) |
| $x^0 = ict$ | Complex time coordinate (local) |
| $x^0 = ic_0 t$ | Complex time coordinate (vacuum) |
| $v$ | Particle or frame velocity |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- A. Sommerfeld, "Über die Zusammensetzung der Geschwindigkeiten in der Relativitätstheorie," *Physikalische Zeitschrift* **10** (1909) 826–829, for the reading of a Lorentz transformation as a rotation by an imaginary angle, recorded in *The Debate, and What Is Not New in It*.
- I. Guzmán de Rojas, "By dismissing Minkowski's notation $x_4 = ict$ are we not losing an essential aspect of space-time structure?", ResearchGate discussion (2013), for the exchange recorded in *The Debate, and What Is Not New in It*: the defence of $ict$ through the Sommerfeld rotation and the claim that it reveals rather than hides the non-compactness of the Lorentz group, and the objections that the device does not generalise to curved space and invites a complexified $\mathbb{C}^4$. An informal thread with no identifier; cited as an instance of the debate, not as authority.
- Charles W. Misner, Kip S. Thorne, John A. Wheeler, *Gravitation* (Freeman, 1973), §2.3 for the historical discussion of $ict$.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 18 and 33 for the complex structure of spacetime.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the complex structure of spacetime.
- Edward Witten, "Anti-de Sitter Space and Holography" (1998), for the geometric interpretation of information.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a modern biquaternionic approach.
- Vladimir V. Kassandrov, "Algebrodynamics over Complex Space and Phase Extension of the Minkowski Geometry", arXiv:0907.5425 [physics.gen-ph] (2009), for the survey of approaches that derive or deform the Minkowski geometry, from which the comparison in *Additional Motivations* is drawn.
- Vladimir V. Kassandrov, "Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time", *Gravitation & Cosmology* **1** (1995) 216, arXiv:gr-qc/0007027, for the sharpest form of the derivation claim recorded in *Where the derivation claim reaches farthest*: that non-trivial solutions of the algebrodynamical primary system take their values on the null divisors of the algebra, and that null fields exist only on manifolds of indefinite signature, so the Lorentzian signature is a necessary condition of non-trivial dynamics rather than a postulate. Recorded in *The Algebrodynamical Programme*, cited as that programme's claim and not adopted here.

