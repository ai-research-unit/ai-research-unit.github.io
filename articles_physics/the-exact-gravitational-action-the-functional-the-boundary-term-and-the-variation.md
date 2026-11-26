# __The Exact Gravitational Action: The Functional, the Boundary Term and the Variation__

## Introduction

**The question, in one line.** Which gravitational action can this framework write, and which can it not? The answer is a ledger, and the ledger is short enough to read at the door.

| sector | action written | where |
| --- | --- | --- |
| electromagnetic, free | one | the Maxwell articles of this corpus |
| electromagnetic, coupled | sixteen | *The Sector Hub* |
| electroweak | one, both phases | *The Sector Hub* |
| strong | none, and cannot be | *The Sector Hub* |
| gravitational, quadratic | yes | *The Lagrangian and Linearised Gravity* |
| gravitational, exact | not yet | this article |
| primordial block | yes, ghosts included | *The Machinery Under the Primordial Action* |

So the gravitational sector is not empty. It carries one action, exact at second order in the frame perturbation, varied to the linearised Einstein tensor with the calibrated coefficient, with the Bianchi identity falling out of the variation in one line. What it lacks is the *exact* functional — the one whose variation is the full equation, nonlinear terms included. That is the whole of the subject, and it is an engineering gap with a shape, not a defect of the algebra.

**What the gap is not, said first because it is usually said wrong.** It is not an absence of ingredients: a scalar, a volume element, a connection, a curvature two-form and a frame are all present in the corpus, and the sections below list them. It is not the absence of a candidate: Lovelock's theorem says that in four dimensions, among local functionals of the metric with second-order field equations, there is exactly one up to two constants, so the functional is not in doubt. It is not even an absence of variation: the second-order truncation is varied, in tensor letters, in the article cited above.

**The gap's shape, in three parts.** The *functional* must be written in the algebra's own variables rather than in the tensor dictionary. The *variation* must be performed with respect to the frame. The corpus's one exact verification of a frame variation is a pointwise check of the frame-to-metric dictionary, and that dictionary is exact; but it is quadratic in the frame, so its differential is linear in the perturbation, while the Hilbert Lagrangian is rational in the metric and its frame variation is not a finite expansion at all. The *boundary* must be handled, because the exact functional is not stationary under Dirichlet conditions without the Gibbons–Hawking–York term, and that term needs two objects — the induced Gram matrix of the boundary's legs and the extrinsic curvature of its normal — that the corpus has never built.

**One premise about method, because the earlier form of this article got it wrong.** No algebra counts derivatives. The Standard Model's gauge group does not count them; the tangent space of a manifold does not count them; derivative order in a field theory is fixed by power counting, by the demand for second-order equations, and by experiment. A framework whose algebra is derivative-free is therefore in the position of every other framework, and the biquaternions are not being asked to do something that groups cannot do. What they can do is *write every operator on the menu*, and the menu is finite. That is the difference between a gap and an impossibility, and it is worth the article.

## What an Action Needs, and What the Algebra Has

A local action in four dimensions needs four things.

**A scalar density.** Something whose integral is coordinate-independent. The algebra has a canonical scalar, the scalar part $\mathrm{Sc}$ of an element, and it has a canonical bilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$ which returns a scalar from two elements.

**A volume element.** $\sqrt{|g|}$ in the metric language. In the frame route $g_{\imath\jmath}=\langle\tilde E_{\Phi,\imath},\tilde E_{\Phi,\jmath}\rangle_{\natural}$, so $\sqrt{|g|}=\sqrt{|\det G|}$ with $G$ the Gram matrix of the four frame legs. That is an algebraic quantity: a determinant of an array of scalars the algebra produced.

**A connection.** The corpus constructs one: a $\mathbb{B}$-valued one-form $\vec\Gamma_{\imath}$ taking values in the six-real-dimensional scalar-free subspace, with a curvature two-form and a torsion. This is the object Route Three of the parent article builds, and it is the one place where the algebra makes a positive contribution rather than merely hosting.

**A space of fields to vary over, and a boundary term.** The frame, the connection, or both. The boundary term is required for a well-posed variational principle, and it is a technical demand the corpus has never addressed.

So the ingredients are all present. What the algebra does not supply is a reason to stop at two derivatives — and nothing else supplies one either, which is why the question has to be answered by a theorem and a measurement rather than by an algebraic identity.

## The Derivative Is Not an Algebra Operation, and No Algebra Counts Them

Here is the structural point, and it is short. Every operation the algebra owns is algebraic: products, the natural involution, the scalar part, the determinant of the matrix image. A derivative is not among them. Differentiation is an operation of the manifold, acting on the frame field $\tilde E_{\Phi,\imath}(x)$, and it appears in the theory only because the frame is a *field* — a function of position — not because it is a biquaternion.

That has a consequence which is easy to miss because it looks like a technicality. The algebra can constrain the *algebraic shape* of an integrand — it can say that the scalar must be built from $\mathrm{Sc}$, that the bilinear pairings must respect the two sectors, that a wedge product must be a $\mathbb{B}$-valued two-form — and it cannot constrain the *number of derivatives*. A functional with one derivative per field, with two, and with four are all equally algebraic in shape. The algebra is blind to the difference, and the difference is precisely what distinguishes Yang–Mills from general relativity from higher-derivative gravity.

So the selection problem is not "which algebraic combination" but "which derivative order".

**The counter, which has to be answered before this diagnosis is used for anything.** No algebra counts derivatives. $SU(3)\times SU(2)\times U(1)$ does not count them, the tangent space of a manifold does not count them, and the multiplication table of a Clifford algebra does not count them. Derivative order in a field theory is fixed by power counting, by the demand that the field equations be second order, and by experiment — never by the multiplication table of a symmetry group. The blindness described above is therefore a property of the method and not a defect of the biquaternions, and an article that presents it as the framework's special difficulty has mistaken a common condition for a private one.

**What the algebra can do instead, and it is the more important half.** It can write every operator on the menu. The menu is finite at any given dimension: with the frame dimensionless and $\partial$ of dimension one, the operators of dimension four built from the frame are a list that can be counted, and *Power Counting on a Frame* counts it. Nothing on that list needs an operation the algebra lacks — not the curvature scalars, not the field strength, not the fermion bilinear. So the algebra is not asked to choose two derivatives, because no algebra is; it is asked to write the finite list once the choice is made elsewhere, and it can.

That reframing is why the rest of this article is a list of constructions rather than a list of failures.

## Why the Natural Algebra Action Is Not Einstein's

The functional the algebra suggests most strongly is the quadratic one,

$$
S_{\mathrm{YM}}[\vec\Gamma]=\int d^{4}x\,\sqrt{|\det G|}\;\mathrm{Sc}\bigl(\tilde F_{\imath\jmath}\tilde F_{\imath\jmath}^{\natural}\bigr),
\qquad
\tilde F_{\imath\jmath}=\partial_{\imath}\vec\Gamma_{\jmath}-\partial_{\jmath}\vec\Gamma_{\imath}+[\vec\Gamma_{\imath},\vec\Gamma_{\jmath}],
$$

with $\tilde F$ the curvature two-form. It is the exact analogue of the Maxwell action the corpus already varies — the biquaternion Maxwell equation follows from it, with the caveat the corpus records that the Lorentz generator does not commute with the basis operator, so the varied form differs from the substituted form by a term. Its equations are second order in the connection, its principal symbol is the wave operator on each component, and its content is a connection, not a metric.

Einstein's action is a different functional of different variables,

$$
S_{\mathrm{EH}}[g]=\frac{1}{16\pi G}\int d^{4}x\,\sqrt{|g|}\,R[g],
$$

second order in the metric and linear in its second derivatives. Its variation gives second-order equations whose principal symbol is the wave operator on the trace-reversed perturbation — the operator the gravitational-waves article writes down — and not a Laplacian on a connection.

Two things are worth saying about the comparison, because both are commonly got wrong.

**The two cannot be separated by dimensions.** In four dimensions both integrands have mass dimension four, so no scaling argument distinguishes them. Any claim that "the algebra's natural action is the only marginal one" is false: gravity is marginal too.

**They cannot be separated by local invariance.** Both are invariant under their respective symmetry groups, and the frame route's local Lorentz freedom is exactly the redundancy the Einstein–Hilbert action has. Invariance therefore does not select between them.

What separates them is derivative order and variable: one derivative of a connection against two derivatives of a frame. The algebra sees neither.

## Lovelock's Theorem: What Selects Two Derivatives

The preceding section says that no algebra counts derivatives, so the question of which derivative order gravity takes cannot be answered inside any algebra. The sharpest external result on the question is worth setting beside that, because it changes what a solution would have to look like: the choice is made by a theorem plus a measurement, and the theorem names its own premises.

**The theorem.** In four dimensions the only symmetric rank-two tensor built from the metric and its first two derivatives, linear in the second derivative and divergence-free, is a combination of the Einstein tensor and the metric itself. Equivalently: the only local action of the form

$$
S=\int d^{4}x\,\sqrt{|\det G|}\,\mathcal L\bigl(g,\partial g,\partial^{2}g\bigr),
$$

invariant under diffeomorphisms and yielding field equations of second order, is

$$
S=\int d^{4}x\,\sqrt{|\det G|}\;\bigl(aR-2\Lambda\bigr)
$$

up to a total derivative, with $a$ and $\Lambda$ the only free numbers. In five or more dimensions the Gauss–Bonnet combination joins the list; in four it is itself a total derivative and contributes nothing, which is why four dimensions admit exactly one coefficient beyond the cosmological constant.

**What the theorem does to the argument, and it is not what it is usually taken to do.** It does not derive the derivative count from nothing. The premise that does the work is *second-order field equations*, not *two derivatives of the metric*; in the metric formulation the two are the same condition, and the theorem is a statement about their equivalence. So the freedom is relocated rather than removed: an author who declines to say why two derivatives may instead say why second order, and Lovelock guarantees that the second answer is as good as the first and no better.

**Three premises, and the corpus has none of them as a derived property.** The argument uses locality, diffeomorphism invariance and second order. Locality is not in doubt. Diffeomorphism invariance is the one *Conservation as a Consequence* records as absent: the corpus has no representation of $\mathrm{Diff}(M)$, and the conservation law that would follow from it is available only point by point, in Riemann normal coordinates. And second order is a condition on equations the corpus has not got, so it cannot be checked before the action is written. The theorem therefore does not close the action problem; it says precisely which three things a settling object must supply, and two of the three are already on the corpus's open list for other reasons.

**The two things it does settle, and both are useful.** The first is that the functional is unique once the premises hold, so the phrase "the Einstein–Hilbert action" is licensed and an author who writes it is not choosing among rivals. The second is that the cosmological constant costs nothing: $\Lambda$ enters as an additive constant, so a framework that can write $\int\sqrt{|\det G|}\,R$ can write $\int\sqrt{|\det G|}\,(R-2\Lambda)$ without introducing a new object. $\Lambda$ is therefore not part of the action problem. It is a number the action problem, once solved, would carry — the same status as $G$, which is calibrated rather than derived.

**What a no-go would now have to say.** The negative route sketched at the end of this article asks for a proof that no functional of the frame alone can produce a source with a traceless part. Lovelock sharpens the positive route in the same way: a candidate action does not have to be shown to be *algebraically natural*, only to satisfy the three premises, and the corpus's difficulty is that the second premise is a statement about the manifold's symmetry group rather than about the algebra's operations.

## Route One, as a Result: the Scalar Curvature as a Trace

There is one place in the corpus where a curvature scalar appears as an algebraic expression, and it is worth stating precisely, because it is the most promising route to an action written in the algebra's own terms.

The companion article proves the Lichnerowicz identity for the biquaternion Dirac operator on a curved background,

$$
(\tilde F_{\imath}D_{\imath})^{2}=-\Box_{g,\Phi}+\tfrac14 R ,
$$

where $\Box_{g,\Phi}$ is the connection Laplacian and $R$ the scalar curvature of the Gram metric. The identity holds of the basis operator, that is, of the left-regular representation of the algebra on itself as a four-dimensional complex vector space, and that qualification is the article's own headline caveat.

Read it backwards, and it gives the scalar curvature as a trace:

$$
R=\mathrm{tr}\bigl[(\tilde F_{\imath}D_{\imath})^{2}+\Box_{g,\Phi}\bigr],
$$

because the constant term contributes $\tfrac14R$ on each of the four basis elements and $4\cdot\tfrac14=1$. So the Einstein–Hilbert action can be written without ever naming the Riemann tensor:

$$
S=\frac{1}{16\pi G}\int d^{4}x\,\sqrt{|\det G|}\;\mathrm{tr}\bigl[(\tilde F D)^{2}+\Box\bigr].
$$

This is a genuine rewriting and it should not be oversold. It is not a derivation: the right-hand side needs $\Box$, which needs the connection, which is the same datum the left-hand side needs, so the identity expresses $R$ in terms of objects it presupposes. The gain is conceptual rather than computational — the curvature scalar becomes a spectral quantity, a trace of an operator built from the algebra's own Dirac operator, which is the shape a spectral action takes. Whether that shape buys anything depends on whether the trace can be regulated without a background metric, and the corpus has no measure and no regulator.

This is recorded as a construction, not as a candidate. Its virtue is that the Hilbert action becomes *algebra-writable* with no tensor named; its limit is that it does not make the choice of two derivatives algebraic, and no route can, for the reason the preceding section gives. The same trace could be taken of a fourth power of the Dirac operator, and the algebra would not object — but power counting would, and that is now the right place to look.

## Route Two, as a Result: the Source as the Gram Matrix of Its Own Frame

An action needs a matter part, and the matter part needs a source. The framework's difficulty here is independent of the gravitational one and is recorded in the cosmology article: the natural algebra packaging of a rank-two tensor collapses to its trace.

For a symmetric tensor $T_{\imath\jmath}$ the framework's natural object is the bilinear sum

$$
\tilde{\mathcal T}=\sum_{\imath,\jmath}T_{\imath\jmath}\,\tilde E_{\Phi,\imath}\tilde E_{\Phi,\jmath}^{\natural}\in\mathbb{B},
$$

and its scalar part is the trace, $\mathrm{Sc}\,\tilde{\mathcal T}=\sum_{\imath} T_{\imath\imath}$. For a perfect fluid in its rest frame $T=\mathrm{diag}(\rho,p,p,p)$ this gives $(-\rho+3p)e_t$: the two independent functions $\rho$ and $p$ are replaced by the single combination $-\rho+3p$, and the four-velocity and any anisotropic stress are discarded. A radiation fluid, for which $p=\rho/3$, is annihilated entirely.

That is the second half of the action problem. Even with a gravitational action in hand, the variation would need a source, and the source object the algebra naturally forms does not carry the two functions a source has. The trace-free part would have to be carried by a different map, and no map *into a single biquaternion* can exist: ten components do not fit in eight. A frame does carry it, and that is the qualification the next paragraph supplies.

There is a sharp way to put the two halves together: **the action problem is a pairing problem.** An action pairs a field with a source through an integral, and the framework's only integral is the scalar part, which is a trace, which annihilates the scalar-free part of anything. Gravity's source is precisely the part that a trace does not see.

**The carrier, however, is not the missing object, and it is worth being precise about that.** The collapse above is a statement about packaging a tensor into one element of $\mathbb{B}$, and no such packaging can be faithful: $\mathrm{Sym}^{2}$ of the four-dimensional material space has ten real components and $\mathbb{B}$ has eight, so no injective linear map exists whatever formula is chosen. A frame is a different object, and the same Gram construction that produces the metric produces a source. Over the complex numbers the form $\digamma_{\mathrm{met}}$ is congruent to the identity, so every nondegenerate symmetric $T$ is $E^{\mathsf T}\digamma_{\mathrm{met}} E$ for some frame $E$; the map is a parametrisation, not a derivation, but it exists.

The perfect fluid makes the point concretely, with no free parameters. Take the frame

$$
\mathfrak U_0=-\lambda_0\,e_t,\qquad \mathfrak U_{\imath}=\lambda\,\vec e_{\imath} ,
\qquad
\lambda_0^{2}=\rho,\qquad \lambda^{2}=p ,
$$

where the two leg scales are named through their squares: $\sqrt\rho$ and $\sqrt p$ are half powers of the base units and are not written. The time leg is **informational** — it is Hermitian, in $\mathbb{B}_{\Psi}$ — and the three spatial legs are material. The natural form reads

$$
\langle\mathfrak U_0,\mathfrak U_0\rangle_{\natural}=\rho,\qquad
\langle\mathfrak U_{\imath},\mathfrak U_{\imath}\rangle_{\natural}=p,\qquad
\langle\mathfrak U_0,\mathfrak U_{\imath}\rangle_{\natural}=0,
$$

so the Gram matrix is exactly $\mathrm{diag}(\rho,p,p,p)$: the two functions are the squared leg norms and are independent, and the traceless part lives in the *shape* of the frame rather than in a trace. The sector assignment is forced, not chosen: a material time leg $\lambda_0e_t$ has norm $-\rho$, which is negative energy, and the sign is restored only by the informational leg — the same factor of $i$ that carries a projector out of $\mathbb{B}_{\Psi}$ into a real null leg, run in reverse. Under a boost rotor the legs transform by congruence and the tensor goes to its standard form; at $\rho=1.7$, $p=0.4$ and rapidity $0.9$ the reconstructed $T$ agrees with $(\rho+p)u_{\imath} u_{\jmath}+p\,\delta_{\imath\jmath}$ to $9\times10^{-16}$.

What this does and does not settle. It settles the objection that the algebra cannot carry the traceless part: a frame carries it, exactly, and the count $10>8$ forbids only the single-element carrier, not the frame. It does not supply a source, because the frame is ten free functions — as much data as $T$ itself — and nothing in the algebra fixes them. The matter half of the action problem is therefore not a problem of *where to put* the two functions; it is the problem of a matter action whose variation produces that frame.

## The Boundary Term: the Gibbons–Hawking–York Functional

The third item of the list above — a boundary term that makes the variational principle well posed — is the one the corpus has never filled, and it is worth writing out because the failure is instructive rather than technical.

**The problem in one line.** Varying the Hilbert action gives a bulk term and a surface term, and the surface term contains the *normal derivative* of the metric variation:

$$
\delta S_{\mathrm{EH}}
=\frac{1}{16\pi G}\int_{\partial M}d^{3}x\,\sqrt{|\det h|}\;n_{\imath}\Bigl(\nabla_{\jmath}\,\delta g^{\imath\jmath}-g^{ab}\nabla^{\imath}\,\delta g_{ab}\Bigr)
+\text{(bulk)},
$$

with $n_{\imath}$ the unit normal and $h$ the induced Gram matrix of the three legs tangent to the boundary. Holding $\delta g_{\imath\jmath}=0$ on the boundary does not kill it, because the normal derivative is still free. So the Dirichlet condition — the single condition a second-order theory normally needs — is not enough, and the variational principle as written is not well posed.

**The repair.** Add the Gibbons–Hawking–York term,

$$
S_{\mathrm{GHY}}=\frac{c^{4}}{8\pi G}\int_{\partial M}d^{3}x\,\sqrt{|\det h|}\;K,
$$

with $K$ the trace of the extrinsic curvature of the boundary in the ambient metric. Its variation cancels the normal-derivative piece exactly, leaving a surface term that vanishes under $\delta g_{\imath\jmath}\big|_{\partial M}=0$ alone. The coefficient is twice the Hilbert one, $c^{4}/8\pi G$ against $c^{4}/16\pi G$, and the corpus sets $c=1$ with $G$, so the two read $1/8\pi G$ and $1/16\pi G$.

**The sign.** $K$ changes sign with the orientation of $n_{\imath}$, and the cancellation is exact only when the normal's convention matches the one used in the bulk variation. This is the one place in the construction where a bookkeeping choice fixes a sign, and it is the reason the term is frequently written with the opposite sign in the literature. The corpus's interval has the one minus on the time slot, so its spacelike normal is outward-pointing with $n_{\imath}n^{\imath}=+1$ on a boundary of constant time, and the sign above is the one that cancels.

**What it settles, and what it costs.** With the term the action is stationary under Dirichlet, so the third item can be met. The cost is that the term is built from the extrinsic curvature of the boundary, and that is a frame object the corpus has never constructed: on a frame route whose volume element is $\sqrt{|\det G|}$, the boundary term needs the induced Gram matrix of the three legs tangent to the boundary *and* the extrinsic curvature of the leg normal to it. The corpus has the Gram determinant and no boundary geometry at all. Requirement 4 is therefore not a technicality to be added later; it is a sixth object, of the same order of difficulty as the connection was.

**Where the corpus already leans on it.** The entropy $A/4G$ is obtained from the Euclidean action, and on a Euclidean section of a vacuum solution the bulk term vanishes on shell while the York term survives and supplies $A/4G$ in full. *Black Hole Thermodynamics in Biquaternionic Form* cites Gibbons and Hawking for exactly this and does not write the functional. The citation is correct; the dependency is worth naming, because it means one of the corpus's sharper results rests on a boundary term the corpus does not possess.

**What the corpus's other actions do, stated as a ledger.** A Klein–Gordon or Maxwell action carries no more than first derivatives of the field, so its surface term is $n^{\imath}\,\delta\phi\,\partial_{\imath}\phi$ and vanishes under $\delta\phi=0$ with no condition on the normal derivative. Those actions are well posed as written. The Hilbert action is not, and neither is any of its truncations. The corpus's Lagrangian articles are therefore correct to impose Dirichlet conditions without comment, and the gravity articles are not — a distinction no article currently draws.

## What Is Not the Problem

**The frame route is not weakened by the missing exact functional.** Carrying a metric does not require a dynamics, and every result in the neighbouring articles stands. A missing exact functional is a boundary of the programme's reach, not an error in its constructions.

**The gap is not an inconsistency.** Nothing in the corpus asserts an equation of motion it cannot derive, and the articles that transcribe say so. The articles that come closest — the gravitational-wave and black-hole-thermodynamics articles — both mark their equations as transcribed, and the audit that preceded this category found no place where a transcription had been promoted to a result.

**The problem is not that the algebra is too small.** It is not: the connection's home, the curvature two-form, the frame, the determinant and the scalar part are all present, and the operators that could sit in an action are on a finite list the algebra can write. What is missing is the exact functional's frame-letter form and its boundary term — two concrete objects, not a principle.

## What Is Owed, in the Order It Would Be Paid

Four items are owed. Each can be checked separately. Two of them have an article of their own, and neither article closes the item it addresses — which is the honest report of where the corpus stands.

1. **The exact functional in frame letters.** $S=\frac{1}{16\pi G}\int d^{4}x\,\sqrt{|\det G|}\,R$, with $R$ the scalar curvature of the Gram metric — written with no tensor named and no object the corpus does not already construct. *The Variation in Frame Letters* states exactly how far this is from being a formality.
2. **Its variation with respect to the frame**, reproducing the Einstein equation with the nonlinear terms intact, and its variation with respect to the connection, reproducing metric compatibility and vanishing torsion — the Palatini structure, for which the corpus is unusually well placed because it already holds both variables as $\mathbb{B}$-valued objects.
3. **The boundary term**, written out in the preceding section, with its two missing objects supplied: the induced Gram matrix of the boundary's legs and the extrinsic curvature of its normal. *Extrinsic Curvature on a Frame* builds the second.
4. **The matter part, producing a source that is not traceless.** The carrier for such a source is the frame; what the functional must still supply is the dynamics that fixes it.

**A third route, recorded and not taken.** The obstacle described above is that the algebra carries no derivative. The one external programme that attacks that obstacle directly is the calculus of Jordan differential forms. It keeps the five relations of the exterior algebra — linearity, the Leibniz rule, commutativity with the elements, and antisymmetry of the product of forms — and replaces the sixth, which is implicit in the commutative case and is associativity, by the Jordan relation. The construction is stated and its properties derived in the source cited here, and it has not been carried to a bosonic action; its authors defer the field theory. It therefore settles nothing, and it is recorded for one reason. It locates the missing derivative in the same place this article does, and it says the derivative can be had by changing the algebra of forms rather than the algebra of coordinates.

**What is not on the list, and why.** The coefficients. Lovelock leaves two constants at two derivatives and four at four, and this article calibrates none of them; the Newtonian limit fixes $\kappa^{2}=16\pi G/c^{4}$ uniquely, and the rest are measured or zero by fiat. A framework that leaves its couplings to measurement is in general relativity's position, and that is a weaker complaint than it sounds, but it is a real one and it belongs on a ledger rather than in a footnote.

## Summary

The question is which gravitational action this framework can write, and the answer has three parts rather than one verdict.

**The functional is not in doubt.** Lovelock's theorem leaves $R$ and $\Lambda$ as the only local, diffeomorphism-invariant, second-order choices in four dimensions, so an author who writes the Hilbert action is not choosing among rivals. The cosmological constant enters as an additive number and costs no new object. The corpus already writes the second-order truncation, varies it, recovers the linearised Einstein tensor with $\kappa^{2}=16\pi G/c^{4}$ calibrated by the Newtonian limit, and sees the Bianchi identity in one line of the variation.

**Three things are missing, and none of them is the functional.** The exact functional in frame letters; the boundary term that makes it stationary under Dirichlet conditions, which needs the induced Gram matrix of the boundary's legs and the extrinsic curvature of its normal; and three of the four coefficients Lovelock leaves free. The measure, which is a fourth item, is a matter for quantisation and is handed to the quantum-gravity article, where the conformal-factor problem shows that a measure is not enough even once an action exists.

**Two constructions are kept, and they are promoted rather than proposed.** The scalar curvature as a trace, $R=\mathrm{tr}[(\tilde FD)^{2}+\Box]$, makes the Hilbert action algebra-writable at the cost of presupposing the connection it uses. The source as the Gram matrix of its own frame carries the traceless part that no single element can. Neither substitutes for the exact variation; both are things the framework can do that the tensor language does not suggest.

The honest position is narrower than "there is no action", and it is checkable: the gravitational sector has one action, and what it needs is its exact form, its boundary term and its coefficients, in that order.

## Further Reading

- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the frame route and Route Three's connection.
- [The Curved Dirac Operator and Its Square](the-curved-dirac-operator-and-its-square.html), for the Lichnerowicz identity $(\tilde F D)^{2}=-\Box+\tfrac14R$ on which Route One rests, and for its basis-operator caveat.
- [The Gram Matrix as the Only Metric](the-gram-matrix-as-the-only-metric.html), for the volume element as a Gram determinant and for the congruence reading of the metric.
- [Cosmology in the Biquaternion Framework: The Carried Metric and the Missing Source](cosmology-in-the-biquaternion-framework-the-carried-metric-and-the-missing-source.html), for the rank-two carrier and the trace collapse of the perfect-fluid source.
- [Quantum Gravity in the Biquaternion Framework: The Two-Sided Obstruction and the Modular Temperature](quantum-gravity-in-the-biquaternion-framework-the-two-sided-obstruction-and-the-modular-temperature.html), for the ordering argument that puts the action before any quantisation.
- [Stress–Energy Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) and [The Non-Quantum Limit of the Action Principle and the Lagrangian](the-non-quantum-limit-of-the-action-principle-and-the-lagrangian.html), for the actions the corpus does have, which are the quadratic functionals this article contrasts with the Hilbert action.
- *Curvature and Geodesics*, for the curvature conventions.
- D. Lovelock, "The uniqueness of the Einstein field equations in a four-dimensional space," *Archive for Rational Mechanics and Analysis* **33** (1969) 54–70, and "The four-dimensionality of space and the Einstein tensor," *Journal of Mathematical Physics* **13** (1972) 874–876, for the uniqueness of the Einstein tensor and the status of the Gauss–Bonnet term in four dimensions.
- J. W. York, "Role of conformal three-geometry in the dynamics of gravitation," *Physical Review Letters* **28** (1972) 1082–1085, and G. W. Gibbons and S. W. Hawking, "Action integrals and partition functions in quantum gravity," *Physical Review D* **15** (1977) 2752–2756, for the boundary term that makes the Hilbert action stationary under Dirichlet conditions, and for the Euclidean action whose on-shell value supplies the entropy.
