# __Curved Spacetime and the Biquaternion Framework__

## Introduction

Every result in the read-list articles is a statement about one fixed algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, evaluated at one point. The norm form, the rotor group, the rotor conjugation, the light cone as the zero-divisor set, the decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ — all of them are pointwise and flat. The wave equations written with them presuppose a global coordinate system $(ict,\,x,\,y,\,z)$ carrying a distinguished imaginary time.

This article is about what happens when the spacetime in which those equations are written is curved. It is not a report of a finished construction. Its subject is a boundary: what the flat machinery extends to, what a curved metric can be made to do inside the algebra, and where the programme stops.

Three claims organise the discussion, and they are worth stating at the outset, because the prose of the framework elsewhere can suggest more than has been built.

**First, curvature cannot reside in the algebra.** The algebra is the same at every point and its norm form has constant coefficients. Curvature can therefore be carried only by the field that attaches the algebra to the manifold, not by the algebra itself. The question "what is curved spacetime in the biquaternion framework?" is a question about a field of frames, not about $\mathbb{B}$.

**Second, the framework's own local device does not reach general relativity.** That device is the local scale factor $c = 1/\sqrt{\epsilon\mu}$ of the imaginary time axis. Read as a map of points it produces no curvature at all, because the resulting line element is the flat form of $\mathbb{M}_-$ written in curvilinear coordinates; read as a derivative rule it produces a genuinely curved metric, but of a class so rigid that within it Ricci-flatness forces flatness. The two readings are inequivalent, and the framework's prose does not choose between them.

**Third, a general curved metric can be carried, but only by inserting a frame field (a tetrad).** The algebra then supplies the local Lorentz group at every point, and can even supply the connection and its curvature as elements of its own Lie subspace; it supplies nothing that determines them. Any four-dimensional real vector space with a form of signature $(3,1)$ would do the same work at each point, so nothing distinctive about $\mathbb{B}$ is put to the test along this route.

The article closes by separating what has been constructed from what remains an agenda. The separation is stark: the kinematical fibre of tetrad gravity is present, its dynamics is absent, and the informational sector $\mathbb{M}_+$ has no curved-space treatment at all.

The conventions are inherited from the read-list articles and none is redefined. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and scalar imaginary $i$ commuting with the quaternion units. The anti-Hermitian and Hermitian subspaces are $\mathbb{M}_-$ and $\mathbb{M}_+$, the real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, and the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$. The rotor group is $\{\tilde{\Lambda} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\} \cong SL(2,\mathbb{C})$, acting on $\mathbb{M}_-$ by rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, with covering homomorphism $\Pi$ onto $SO^+(1,3)$ and kernel $\{\pm e_0\}$. The trace formula of the informational sector is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum speed.

## What the Flat Machinery Assumes

The pointwise metric of the framework is the polar form of the norm form. For $\tilde{Q} = iq_0 + \mathbf{q}$ and $\tilde{P} = ip_0 + \mathbf{p}$ in $\mathbb{M}_-$,

$$
\tfrac{1}{2}\left(\tilde{Q}\bar{\tilde{P}} + \tilde{P}\bar{\tilde{Q}}\right)
= \mathrm{Sc}\left(\tilde{Q}\bar{\tilde{P}}\right)
= -q_0p_0 + \mathbf{q}\cdot\mathbf{p},
$$

a real scalar. Write $\langle \tilde{Q}, \tilde{P}\rangle$ for this form; in the basis $(ie_0, e_1, e_2, e_3)$ of $\mathbb{M}_-$ its Gram matrix is $\mathrm{diag}(-1,1,1,1)$, so it is the Minkowski inner product of $\mathbb{M}_- \cong \mathbb{R}^{1,3}$. It is preserved by rotor conjugation,

$$
\langle \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger,\ \tilde{\Lambda}\tilde{P}\tilde{\Lambda}^\dagger \rangle = \langle \tilde{Q}, \tilde{P}\rangle,
$$

because the norm form is invariant and the conjugation action is linear in $\tilde{Q}$. This is the entire metric content of the flat framework: one fixed form on one fixed real vector space.

Four assumptions are built into that statement, and each is a flat-space assumption.

**1. One algebra, at one point.** The framework has no notion of two points. The four-position $\tilde{X}$, the four-velocity $\tilde{U}$, and every other four-vector are elements of $\mathbb{M}_-$; separation between events enters only as a difference $\tilde{X}_1 - \tilde{X}_2$, never as a displacement along a path.

**2. A norm form with constant coefficients.** The form $\langle \cdot,\cdot \rangle$ is the same at every point, by construction. Nothing in the algebra can vary it.

**3. A global chart with a distinguished time axis.** The biquaternionic gradient

$$
\tilde{\nabla} = e_0\,\partial_{ict} + e_1\,\partial_x + e_2\,\partial_y + e_3\,\partial_z
$$

requires four global coordinates, and requires in addition that the time direction be the coefficient of $e_0$ — that is, a preferred split of the coordinates into a time function and three spatial functions. The Maxwell and Dirac equations of the companion articles are written with this operator and inherit the requirement.

**4. A global symmetry group.** The rotor group is the group of units of a fixed algebra. It is a global object. A curved manifold has no global group of that kind acting on it; what it has is a pointwise copy of the group at each point, if the frame is chosen.

The framework is not silent about these limitations. *Introduction to the Biquaternion Universe* lists the extension to curved spacetime as an open question; *Why Complexify Spacetime?* observes that the $ict$ convention "is tied to the existence of a global inertial frame"; and *Electromagnetism in Media — The Local Complex Structure at Work* states the position precisely: the algebra is "fixed while its embedding in physical spacetime is not." That last clause is the one this article takes seriously, because an embedding that varies from point to point is exactly where curvature would have to live.

## Curvature Cannot Be Carried by the Algebra

An algebra has no points, so it cannot have a curvature. The statement is worth making concrete rather than rhetorical. The norm form on $\mathbb{B}$ is a quadratic form with constant coefficients in a fixed basis; the only freedom in writing it is a change of basis, that is, a linear transformation, and a linear transformation maps a flat form to a flat form. There is no parameter in $\mathbb{B}$ that a field could modulate and no way to make the coefficient of the time direction a function of position. If one wants curvature in this framework, one must supply it in the map that attaches $\mathbb{B}$ to spacetime.

Two forms of that map are available, and they are the two routes examined below:

- a **scale** on the imaginary time axis, $ict \mapsto i\,c(x)\,t$, which is the framework's own local complex structure; and
- a **frame**, $dx^\mu \mapsto \tilde{E}_\mu(x)\,dx^\mu$, which is the tetrad of the standard spinor formulation of general relativity.

They are different devices, and it is a mistake to treat them as the same one. The first makes a piece of the embedding's scale local while leaving the frame rigid; the second makes the frame local while leaving every scale to the frame itself. The first is the framework's proposal and yields too little to be general relativity; the second yields everything kinematically and is no longer specifically biquaternionic.

A second structural point belongs here. General relativity's defining symmetry is diffeomorphism invariance: the theory is formulated on a manifold whose points carry no labels, and the group $\mathrm{Diff}(M)$ acts on those points. The algebra $\mathbb{B}$ has no representation of $\mathrm{Diff}(M)$ and nothing in it corresponds to a coordinate change on the base. Its algebraic symmetries are the pointwise $SL(2,\mathbb{C})$ — a redundancy in the description of a frame, not a symmetry of the manifold — together with the isometries of whatever background is chosen. This is a gap of a different kind from the absence of dynamics: a biquaternion formulation of gravitation in the strict sense would have to relate $\mathbb{B}$ to diffeomorphism invariance, and no such relation has been constructed.

Finally, a piece of representation-theoretic bookkeeping locates where the work would be. Under the Lorentz group the metric and the energy–momentum tensor are symmetric rank-2 objects, $\left(1,1\right)\oplus\left(0,0\right)$ in the $(m,n)$ labelling of the read list, of dimensions $9 + 1 = 10$. The kinematical fields the framework is built from are four-vectors, $\left(\tfrac12,\tfrac12\right)$, of dimension $4$, and they lie in $\mathbb{M}_-$. The companion article on the material space already records that the field-strength biquaternion and the energy–momentum biquaternion are not four-vectors and do not lie in $\mathbb{M}_-$. So the objects that would have to become dynamical fields in a theory of gravity are not the objects the framework is organised around. This is bookkeeping rather than impossibility, but it is where the missing formalism would have to be built.

## Route One: The Local Scale Factor

The framework's own route to a local structure is the local complex structure. Its content is stated in *Introduction to the Biquaternion Universe* and developed in *Electromagnetism in Media — The Local Complex Structure at Work*. In a medium with permittivity $\epsilon$ and permeability $\mu$, the speed of light is $c = 1/\sqrt{\epsilon\mu}$, a property of the medium at each point. The material time coordinate is $ict$, so the map from physical time to the imaginary scalar direction of $\mathbb{B}$ carries the factor $c$; the imaginary unit $i$ is fixed by the algebra and only the real scale attached to the imaginary axis is local. In the gradient, this means

$$
\partial_{ict} = -\frac{i}{c}\,\partial_t .
$$

The framework's phrasing is that the complex structure is local "in the same spirit as the metric in general relativity", and that the $ict$ convention of Minkowski space is the vacuum limit $c \to c_0$ of a more general local structure.

It is at this point that a genuine ambiguity appears, and it should be stated before anything is computed from it.

### The Two Readings

**Reading A, the point map.** Take the four-position as the framework writes it, $\tilde{X} = ict\,e_0 + \mathbf{x}$, with the local $c$. Then $c$ is a function of position and

$$
d(ict) = ic\,dt + i\,t\,dc,
$$

so the displacement biquaternion is $d\tilde{X} = i(c\,dt + t\,dc)e_0 + d\mathbf{x}$ — still an element of $\mathbb{M}_-$ — and the interval is $ds^2 = N(d\tilde{X})$,

$$
ds^2 = -c^2\,dt^2 - 2ct\,dt\,dc - t^2 (dc)^2 + d\mathbf{x}^2
= -c^2\,dt^2 - 2ct\,\partial_i c\,dt\,dx^i - t^2\,\partial_i c\,\partial_j c\,dx^i dx^j + d\mathbf{x}^2 .
$$

The metric so obtained is nondegenerate — $\det g = -c^2$ in the coordinates $(t,x,y,z)$ — but it is **flat**. The map $(t,\mathbf{x}) \mapsto i\,c(\mathbf{x})\,t\,e_0 + \mathbf{x}$ is a diffeomorphism of $\mathbb{R}^4$ onto $\mathbb{M}_-$ (its Jacobian determinant is $c > 0$), and it is pulling back the flat form of $\mathbb{M}_-$; a pullback of a flat form along a diffeomorphism is flat, and no curvature can be produced by reparametrising a flat space. Direct computation confirms it: for $c = 1 + \tfrac{1}{10}(x^2+y^2+z^2)$ and, on a second and independent case, for $c = 2 + \sin x\,\cos y$, every component of the Riemann tensor vanishes. The local scale factor, read as a map of points, changes the coordinate description of flat spacetime and nothing else.

**Reading B, the derivative rule.** Take instead the framework's actual usage, in which $c$ enters through the operator $\partial_{ict} = -(i/c)\partial_t$ and the four-position is written with a single complex coordinate $ict$ rather than with a position-dependent coefficient. Equivalently, hold $c$ fixed in the differential: $d(ict) = ic\,dt$. Then

$$
ds^2 = -c(\mathbf{x})^2\,dt^2 + d\mathbf{x}^2,
\qquad
g_{\mu\nu} = \mathrm{diag}\left(-c(\mathbf{x})^2,\ 1,\ 1,\ 1\right),
$$

and this metric is genuinely curved whenever $c$ is not affine in the spatial coordinates.

The two readings differ exactly by the terms containing $dc$, and they are not equivalent: one is flat and the other is not. Neither *Introduction to the Biquaternion Universe* nor *Electromagnetism in Media — The Local Complex Structure at Work* chooses between them, because the statements about the local $c$ are made at the level of the operator while the statements about the four-position are made at the level of the point. A reader can reasonably take either. This is left open here rather than resolved, because resolving it is a decision about what the framework means and not a computation.

### What the Restricted Class Cannot Do

Suppose Reading B is intended. Its curvature can be computed in closed form. Writing $u = c = 1/\sqrt{\epsilon\mu}$ and allowing $u$ to depend on time as well as position,

$$
R_{00} = -u\,\Delta u, \qquad R_{0i} = 0, \qquad R_{ij} = \frac{\partial_i\partial_j u}{u},
$$

where $\Delta$ is the three-dimensional Laplacian and the indices $i,j$ run over the spatial directions. Equivalently, with $f = c^2$, $R_{00} = \left(-2f\,\Delta f + |\nabla f|^2\right)/(4f)$ and $R_{ij} = \left(2f\,\partial_i\partial_j f - \partial_i f\,\partial_j f\right)/(4f^2)$. For example $c = 2 + \sin x$ gives scalar curvature

$$
R = -\frac{2\sin x}{2 + \sin x},
$$

which is $-\tfrac{2}{3}$ at $x = \pi/2$ and vanishes at $x = 0$ and $x = \pi$.

The class is narrow in a way that is easy to state: one free function of the spatial coordinates (or of time as well), no shift vector, and a flat three-metric on the spatial slices, $g_{ij} = \delta_{ij}$. It is the diagonal, spatially rigid sub-case of the frame route of the next section.

Its decisive limitation is the following. Within this class, **Ricci-flatness forces flatness.** The condition $R_{ij} = 0$ requires $\partial_i\partial_j u = 0$ for every pair of spatial indices, so $u = \mathbf{a}(t)\cdot\mathbf{x} + b(t)$ is affine in the spatial coordinates; then $R_{00} = -u\,\Delta u$ vanishes automatically, so this is the whole Ricci-flat family. And every member of that family is flat: for $u = \mathbf{a}(t)\cdot\mathbf{x} + b(t)$ with arbitrary functions $\mathbf{a}(t)$ and $b(t)$, the Riemann tensor vanishes identically, as direct symbolic computation of the general case confirms. The family is the algebra's way of writing a uniformly accelerated (Rindler-type) frame, and it is a reparametrisation of Minkowski space.

The consequence is worth stating plainly, in the restricted sense in which it holds. A metric that the local-scale route can write down at all cannot be a non-flat Ricci-flat spacetime. It therefore cannot carry a vacuum gravitational field with Weyl curvature, and with it no vacuum gravitational wave and no vacuum black-hole exterior. This is a statement about a metric class, not a theorem about the biquaternion programme — but it is enough to show that the local scale factor of the imaginary time axis is not the route by which general relativity will enter the framework.

There is a further conceptual gap along this route, independent of the calculation. The $c$ in $1/\sqrt{\epsilon\mu}$ is the speed of light in a material medium — a property of a dielectric, measurable with a capacitor and a magnet. The standard effective-geometry literature (Gordon's metric and its modern descendants in transformation optics) already attaches a metric to a dielectric medium, and that metric is a metric for *light*: it reproduces the ray trajectories of Maxwell's equations in the medium, not the free-fall trajectories of test masses. Identifying the medium's effective metric with the spacetime metric is a further step, and the framework's "in the same spirit as the metric in general relativity" is an analogy rather than that step. Nothing in the framework supplies it.

## Route Two: A Field of Frames

The general way to make the embedding of spacetime into the algebra local is to allow the coordinate differentials to be carried into $\mathbb{M}_-$ by a point-dependent frame:

$$
d\tilde{X} = \tilde{E}_\mu(x)\,dx^\mu, \qquad \tilde{E}_\mu(x) \in \mathbb{M}_- .
$$

The interval is $ds^2 = N(d\tilde{X})$, and since $N$ is the polar form evaluated on $d\tilde{X} = \tilde{E}_\mu dx^\mu$,

$$
g_{\mu\nu}(x) = \langle \tilde{E}_\mu(x), \tilde{E}_\nu(x)\rangle
= \mathrm{Sc}\left(\tilde{E}_\mu \bar{\tilde{E}}_\nu\right).
$$

Four $\mathbb{M}_-$-valued fields, so sixteen functions. Where they are linearly independent, the Gram matrix is nondegenerate, and by Sylvester's law it has signature $(3,1)$: the result is automatically a Lorentzian metric. Conversely, any Lorentzian metric can be written this way locally. Choose a $g$-orthonormal frame, map it into $\mathbb{M}_-$ by a linear isometry of quadratic spaces — which exists because both forms have signature $(3,1)$ — and read off the coordinate components. So there is no obstruction: **the framework can carry any curved metric.**

What makes the route more than a change of notation is the local symmetry. If $\tilde{\Lambda}(x)$ is a unit-norm biquaternion depending on position, then

$$
\tilde{E}_\mu \longmapsto \tilde{\Lambda}\tilde{E}_\mu\tilde{\Lambda}^\dagger
$$

leaves $g_{\mu\nu}$ unchanged at every point, because rotor conjugation preserves the bilinear form. So the local gauge group supplied by the algebra is exactly a copy of $SL(2,\mathbb{C})$ at each point, with the double cover, the Lie algebra, and the $\left(m,n\right)$ representation theory of the read list applying pointwise. This is the standard tetrad or vierbein structure of the spinor formulation of general relativity, written in the algebra's own notation; the interplay of the sixteen frame functions with the six local rotor parameters leaves $16 - 6 = 10$ independent components, which is the number of components of $g_{\mu\nu}$.

The corresponding flatness statement is exact and instructive. If the frame is *pure rotor gauge*, $\tilde{E}_\mu = \tilde{\Lambda}(x)\,\epsilon_\mu\,\tilde{\Lambda}(x)^\dagger$ for a fixed basis $\epsilon_\mu$ of $\mathbb{M}_-$, then $g_{\mu\nu}(x) = \langle \epsilon_\mu, \epsilon_\nu\rangle$ is a constant matrix, and the metric is flat. A point-dependent rotor field applied to a rigid basis produces no curvature whatever. Curvature in this route is exactly that part of the frame which is not of this pure-gauge form, and no amount of rotor-field machinery detects it.

Two honest qualifications keep this from sounding like more than it is.

First, *carrying is not deriving*. The frame field is inserted by hand, and it is subject to no condition from the algebra. Every Lorentzian metric, including every vacuum spacetime, is representable; the framework excludes nothing. That is not a success but an emptiness: the entire content of the construction is the sixteen functions, and the algebra contributes only a fixed four-dimensional real vector space with a form of signature $(3,1)$, which any such space would contribute equally. Nothing that distinguishes $\mathbb{B}$ — the quaternionic multiplication, the two-sector decomposition, the complex structure — is used in writing $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle$.

Second, *this route does not make the complex structure local*. The frame field is a real linear map at each point; the imaginary direction of $\mathbb{B}$ remains globally the coefficient of $e_0$ in a fixed basis. The framework's local complex structure and the tetrad's local frame are different devices, and neither contains the other: the frame route gives general relativity's kinematics and abandons the framework's own locality proposal, while the local-scale route keeps that proposal and cannot reach even a non-flat Ricci-flat vacuum. This tension is a finding of this article, not a problem it resolves.

## Route Three: The Connection, and the Two-Sided Derivative

A frame field is not by itself a geometry; a manifold also needs a way to compare frames at neighbouring points, that is, a connection. Here the biquaternion algebra makes a genuine and positive contribution, and the contribution has a trap in it that is worth recording.

The positive part is dimensional. The Lie algebra of the rotor group is the traceless part of $\mathbb{B}$,

$$
\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}
= \mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\} \oplus \mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}
= \left\{ G \in \mathbb{B} : G + \bar{G} = 0 \right\},
$$

six real dimensions, with the rotation generators $J_k = e_k$ and the boost generators $K_k = ie_k$ of the read list. Since this Lie algebra is a subspace of $\mathbb{B}$, a connection 1-form and its curvature 2-form can both be carried as $\mathbb{B}$-valued objects — specifically, as objects valued in that six-dimensional subspace. The spin connection of the tetrad formalism is therefore not foreign to the algebra; it sits inside it.

The trap concerns the covariant derivative. The group acts on the material sector by the two-sided formula $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, so the infinitesimal action of a generator $G$ is

$$
\tilde{X} \longmapsto \tilde{X} + \epsilon\left(G\tilde{X} + \tilde{X}G^\dagger\right) + O(\epsilon^2),
$$

which is **not** in general the commutator $[G,\tilde{X}]$. The two agree exactly when $G^\dagger = -G$, which is the case for the rotation generators $e_k$; for the boost generators $ie_k$, which are Hermitian, they do not agree. On $\tilde{X} = iq_0 + q_1e_1 + q_2e_2 + q_3e_3$, the boost generator $G = ie_1$ acts to first order as

$$
q_0 \longmapsto q_0 - 2\epsilon q_1, \qquad q_1 \longmapsto q_1 - 2\epsilon q_0,
$$

mixing the time and $e_1$ components as a boost must, whereas $[G,\tilde{X}]$ is $2\epsilon(-iq_3\,e_2 + iq_2\,e_3)$, a rotation in the $e_2e_3$ plane — a different transformation altogether. A biquaternionic covariant derivative must therefore be written in the two-sided form

$$
D_\mu \tilde{X} = \partial_\mu \tilde{X} + \tilde{\Gamma}_\mu \tilde{X} + \tilde{X}\tilde{\Gamma}_\mu^\dagger ,
$$

with $\tilde{\Gamma}_\mu$ in the Lie subspace; the natural abbreviation $D_\mu = \partial_\mu + [\tilde{\Gamma}_\mu, \cdot]$ would be wrong for exactly the boosts, which is where the Lorentzian content of the theory lives.

One object in this neighbourhood is automatic and one is not. The automatic one is the logarithmic derivative of a rotor field: if $\tilde{\Lambda}(x)$ is unit-norm, then both $\bar{\tilde{\Lambda}}\,\partial_\mu\tilde{\Lambda}$ and $\partial_\mu\tilde{\Lambda}\,\bar{\tilde{\Lambda}}$ are traceless, hence lie in the Lie algebra, because $\bar{\tilde{\Lambda}}\tilde{\Lambda} = e_0$ differentiates to zero. So a frame carried by a rotor field arrives with a natural $\mathfrak{sl}(2,\mathbb{C})$-valued connection. But it is pure gauge, and its curvature vanishes — which is the same statement as the flatness of the rotor-field metric in the previous section, arrived at from the other direction. Consistency, not new content.

What is not automatic is everything one would want. Metric compatibility and the vanishing of torsion are conditions, not consequences; nothing in the algebra selects the Levi-Civita lift. And the whole dynamics is absent: there is no action, no field equation for $\tilde{E}_\mu$ or $\tilde{\Gamma}_\mu$, and therefore no Einstein equation. The algebra can hold the objects of the spin-connection formalism in the same notation in which it holds the rotors and the four-vectors. It does not generate a single equation for them.

## The Informational Sector on a Curved Background

The second half of the framework — $\mathbb{M}_+$, its idempotents, its observables and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ — has no curved-space treatment, and it is worth saying why the absence is structural rather than a matter of effort.

When the spacetime is curved, the elements of $\mathbb{M}_+$ would have to become fields of operators, one copy of the algebra being attached at each point. That much is formal: the fibre is defined and the pointwise operator algebra goes through unchanged. What does not go through is the trace. The trace in the trace formula is the $2 \times 2$ matrix trace at a point; it has no volume element and no integration. Every trace in a field theory is an integral over the manifold, with a measure that itself depends on the metric, and the framework's trace cannot play that role. So even the Born rule, which is the most successful piece of the flat construction, has no constructed curved-space analogue here: the pointwise expectation value survives, the global one has nowhere to live.

The two-sector decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ is a pointwise decomposition and survives as such on any background. Beyond that, the curved setting is untouched. Any coupling between the sectors would have to be an equation of motion for fields belonging to both, and no such equation exists in the flat case either; a fortiori none exists here.

## What Is Constructed and What Is Agenda

The boundary can be drawn as a list, and drawing it is this article's main result.

**Constructed** (algebraic facts, each recomputed for this article). The pointwise metric of $\mathbb{M}_-$ as the polar form of the norm form, with signature $(3,1)$. Its invariance under rotor conjugation. The representation of an arbitrary Lorentzian metric by a frame field $\tilde{E}_\mu \in \mathbb{M}_-$ with $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle$, and the local $SL(2,\mathbb{C})$ gauge invariance of that representation. The identification of the rotor group's Lie algebra with the six-dimensional traceless subspace of $\mathbb{B}$. The two-sided infinitesimal action of a connection, and the tracelessness of a rotor field's logarithmic derivative. The induced metrics of the local-scale route in both readings, with the flatness of Reading A and the closed-form curvature of Reading B, and the result that within Reading B's metric class Ricci-flatness implies flatness.

**Agenda** (nothing constructed). An action principle or field equation for the frame or the connection, and hence any Einstein equation. Coupling to sources, with the bookkeeping problem that the gravitating objects are symmetric rank-2 tensors, $\left(1,1\right)\oplus\left(0,0\right)$, while the framework's own fields are four-vectors in $\mathbb{M}_-$. Curved-space forms of the biquaternion Maxwell and Dirac equations written in the framework's own notation, for which the background-dependence of $\tilde{\nabla}$ is precisely the obstacle. Global and topological structure of every kind: the algebra is a point, so causal structure, horizons, singularities, and topology are outside it, and even the existence of spinor fields on a manifold is a topological condition — the vanishing of the second Stiefel–Whitney class — that the algebra cannot see; the globalisation of the spinor module to a bundle over a curved background is recorded as a separate open item in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. The discrete symmetries, which are not in the connected rotor group. The informational sector, as above. And empirical contact, which remains the framework's central open question and is not advanced by anything here.

The honest summary of the boundary is this. The biquaternion framework contains the kinematical fibre of tetrad gravity: a pointwise Lorentzian vector space, its Lorentz group, the vector representation, and the Lie-algebra-valued connection. It contains nothing of tetrad gravity's dynamics, and nothing that selects a metric. It is therefore not correct to say that the framework contains general relativity, and it is not correct to say that it conflicts with it. What the framework contains is the algebra in which the local part of general relativity is normally written, plus a proposal — the local scale factor of the imaginary time axis — that is too rigid to carry the non-flat vacuum solutions.

## Summary

The read-list machinery is flat and pointwise: one fixed algebra, one fixed norm form with constant coefficients, a global chart with a distinguished imaginary time, and a global rotor group. Curvature cannot be made a property of the algebra, because the algebra has no points and no deformable coefficient; it can only be carried by the field that attaches the algebra to spacetime.

The framework's own local device is the local scale $c = 1/\sqrt{\epsilon\mu}$ of the imaginary time axis. It admits two inequivalent readings. As a map of points, $\tilde{X} = i\,c(\mathbf{x})\,t\,e_0 + \mathbf{x}$, it yields a nondegenerate metric with $\det g = -c^2$ that is identically flat — the pullback of the flat form of $\mathbb{M}_-$ along a diffeomorphism — as direct computation confirms. As a derivative rule, $\partial_{ict} = -(i/c)\partial_t$ with $c$ held fixed in the differential, it yields $g_{\mu\nu} = \mathrm{diag}(-c^2,1,1,1)$, genuinely curved, with $R_{00} = -u\Delta u$, $R_{0i} = 0$, $R_{ij} = \partial_i\partial_j u / u$ for $u = c$. The framework's prose does not choose between the readings, and the choice is left open here.

Within the second reading's class — one function, no shift, flat spatial slices — Ricci-flatness forces $u$ to be affine in the spatial coordinates, and every such metric is flat. The class therefore contains no non-flat vacuum geometry: no Weyl curvature, no gravitational waves, no black-hole exteriors. The local scale factor is not the route to general relativity. Nor is it the same object as the metric: $c$ is the Maxwell speed of a medium, and the standard effective metric of a dielectric is a metric for light, not for free fall.

A general curved metric can be carried, by a frame field $\tilde{E}_\mu(x) \in \mathbb{M}_-$ with $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle$, since any Lorentzian metric has a local orthonormal frame. The algebra then supplies the pointwise $SL(2,\mathbb{C})$, its vector representation, and its Lie algebra; the sixteen frame functions modulo six local rotor parameters reproduce the ten components of the metric; and a frame that is pure rotor gauge is flat, so curvature is exactly the non-gauge part of the frame. The algebra can even carry the connection and its curvature, since the Lie algebra is the six-dimensional traceless subspace of $\mathbb{B}$ — with the caveat that the infinitesimal action is the two-sided $G\tilde{X} + \tilde{X}G^\dagger$, not the commutator, the two differing precisely for the boosts.

What is missing is not a technical detail but the theory. Nothing determines the frame, the connection, or the metric; there is no action, no field equation, and no Einstein equation; the gravitating rank-2 tensors are not the framework's four-vectors; diffeomorphism invariance has no algebraic counterpart; global and topological structure is outside a pointwise algebra; and the informational sector's trace formula is a fibre trace with no measure and no integral, so its curved-space extension is not merely unwritten but unlocated. The framework contains the kinematical fibre of tetrad gravity and none of its dynamics; the title names a framework, and that is exactly what it is.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, home of the rotation rotors |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\langle \tilde{Q},\tilde{P}\rangle = \mathrm{Sc}(\tilde{Q}\bar{\tilde{P}})$ | Bilinear (polar) form on $\mathbb{M}_-$; the pointwise metric |
| $\tilde{\Lambda} \in SL(2,\mathbb{C})$ | Unit-norm biquaternion (Lorentz rotor) |
| $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation (four-vector action) |
| $\Pi : SL(2,\mathbb{C}) \to SO^+(1,3)$ | Two-to-one covering homomorphism, kernel $\{\pm e_0\}$ |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $ict$ | Local imaginary time coordinate, material sector |
| $\tilde{\nabla} = e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ | Biquaternionic gradient (needs a global chart) |
| $\tilde{E}_\mu(x) \in \mathbb{M}_-$ | Frame field (tetrad): $d\tilde{X} = \tilde{E}_\mu dx^\mu$ |
| $g_{\mu\nu} = \langle \tilde{E}_\mu,\tilde{E}_\nu\rangle$ | Metric carried by the frame field |
| $J_k = e_k$, $K_k = ie_k$ | Rotation and boost generators, spanning $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}} \subset \mathbb{B}$ |
| $\tilde{\Gamma}_\mu$ | Connection 1-form, valued in the Lie subspace |
| $D_\mu\tilde{X} = \partial_\mu\tilde{X} + \tilde{\Gamma}_\mu\tilde{X} + \tilde{X}\tilde{\Gamma}_\mu^\dagger$ | Covariant derivative on $\mathbb{M}_-$ (two-sided) |
| $u = c$, $f = c^2$ | Local scale factor and its square, in the local-scale route |
| $R_{00}=-u\Delta u$, $R_{0i}=0$, $R_{ij}=\partial_i\partial_j u/u$ | Ricci tensor of $g=\mathrm{diag}(-c^2,1,1,1)$ |
| $(m,n)$, $\left(\tfrac12,\tfrac12\right)$, $\left(1,1\right)\oplus\left(0,0\right)$ | Lorentz representations: four-vectors; symmetric rank-2 tensors |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule), pointwise only |

## Further Reading

- Charles W. Misner, Kip S. Thorne, and John A. Wheeler, *Gravitation* (Freeman, 1973), for the tetrad formalism and the distinction between coordinate and orthonormal frames in general relativity.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the metric, the curvature tensors, and the spinor formulation of curved spacetime.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984) and Vol. 2 (Cambridge, 1986), for the two-spinor calculus and the tetrad and spin-connection formalism in Lorentzian signature.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for spin structures on manifolds and the topological obstruction to spinor fields.
- W. Gordon, "Zur Lichtfortpflanzung nach der Relativitätstheorie," *Annalen der Physik* **72** (1923) 421–456, for the effective metric of a dielectric medium.
- Ulf Leonhardt and Thomas G. Philbin, "General relativity in electrical engineering," *New Journal of Physics* **8** (2006) 247, for the modern transformation-optics reading of a medium's effective geometry.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 18 and 33, for the complex structure of spacetime and for the spinorial formulation of curved geometry.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic treatment of gravity in the same rotor language used here.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a related biquaternionic approach to complexified geometry and its limits.
