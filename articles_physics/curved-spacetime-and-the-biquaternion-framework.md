# __Curved Spacetime and the Biquaternion Framework__

## Introduction

Every result in the read-list articles is a statement about one fixed algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, evaluated at one point. The biquaternion norm, the rotor group, the rotor conjugation, the light cone as the zero-divisor set, the decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ — all of them are pointwise and flat. The wave equations written with them presuppose a global coordinate system $(ict,\,x,\,y,\,z)$ carrying a distinguished imaginary time.

This article is about what happens when the spacetime in which those equations are written is curved. It is not a report of a finished construction. Its subject is a boundary: what the flat machinery extends to, what a curved metric can be made to do inside the algebra, and where the programme stops.

Three claims organise the discussion, and they are worth stating at the outset, because the prose of the framework elsewhere can suggest more than has been built.

**First, curvature cannot reside in the algebra.** The algebra is the same at every point and its biquaternion norm has constant coefficients. Curvature can therefore be carried only by the field that attaches the algebra to the manifold, not by the algebra itself. The question "what is curved spacetime in the biquaternion framework?" is a question about a field of frames, not about $\mathbb{B}$.

**Second, the framework's own local device does not reach general relativity.** That device is the local scale factor $c = 1/\sqrt{\epsilon\mu}$ of the imaginary time axis. Read as a map of points it produces no curvature at all, because the resulting line element is the flat form of $\mathbb{M}_-$ written in curvilinear coordinates; read as a derivative rule it produces a genuinely curved metric, but of a class so rigid that within it Ricci-flatness forces flatness. The two readings are inequivalent, and the framework's prose does not choose between them.

**Third, a general curved metric can be carried, but only by inserting a frame field (a tetrad).** The algebra then supplies the local Lorentz group at every point, and can even supply the connection and its curvature as elements of its own Lie subspace; it supplies nothing that determines them. Any four-dimensional real vector space with a form of signature $(3,1)$ would do the same work at each point, so nothing distinctive about $\mathbb{B}$ is put to the test along this route.

The article closes by separating what has been constructed from what remains an agenda. The separation is stark: the kinematical fibre of tetrad gravity is present, its dynamics is absent, and the informational sector $\mathbb{M}_+$ has no curved-space treatment at all.

The conventions are inherited from the read-list articles and none is redefined. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and scalar imaginary $i$ commuting with the quaternion units. The anti-Hermitian and Hermitian subspaces are $\mathbb{M}_-$ and $\mathbb{M}_+$, the real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, and the biquaternion norm is $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$. The rotor group is $\{\tilde{\Lambda} : \tilde{\Lambda}\tilde{\Lambda}^{\natural} = e_0\} \cong SL(2,\mathbb{C})$, acting on $\mathbb{M}_-$ by rotor conjugation $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, with covering homomorphism $\mathrm{Ad}$ onto $SO^+(1,3)$ and kernel $\{\pm e_0\}$. The trace formula of the informational sector is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum speed.

## What the Flat Machinery Assumes

The pointwise metric of the framework is the polar form of the biquaternion norm. For $\tilde{Q} = iq_0 + \mathbf{q}$ and $\tilde{P} = ip_0 + \mathbf{p}$ in $\mathbb{M}_-$,

$$
\tfrac{1}{2}\left(\tilde{Q}\tilde{P}^{\natural} + \tilde{P}\tilde{Q}^{\natural}\right)
= \mathrm{Sc}\left(\tilde{Q}\tilde{P}^{\natural}\right)
= -q_0p_0 + \mathbf{q}\cdot\mathbf{p},
$$

a real scalar. Write $\langle \tilde{Q}, \tilde{P}\rangle$ for this form; in the basis $(ie_0, e_1, e_2, e_3)$ of $\mathbb{M}_-$ its Gram matrix is $\mathrm{diag}(-1,1,1,1)$, so it is the Minkowski inner product of $\mathbb{M}_- \cong \mathbb{R}^{1,3}$. It is preserved by rotor conjugation,

$$
\langle \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*},\ \tilde{\Lambda}\tilde{P}\tilde{\Lambda}^{*} \rangle = \langle \tilde{Q}, \tilde{P}\rangle,
$$

because the biquaternion norm is invariant and the conjugation action is linear in $\tilde{Q}$. This is the entire metric content of the flat framework: one fixed form on one fixed real vector space.

Four assumptions are built into that statement, and each is a flat-space assumption.

**1. One algebra, at one point.** The framework has no notion of two points. The four-position $\tilde{Q}$, the four-velocity $\tilde{U}$, and every other four-vector are elements of $\mathbb{M}_-$; separation between events enters only as a difference $\tilde{Q}_1 - \tilde{Q}_2$, never as a displacement along a path.

**2. A biquaternion norm with constant coefficients.** The form $\langle \cdot,\cdot \rangle$ is the same at every point, by construction. Nothing in the algebra can vary it.

**3. A global chart with a distinguished time axis.** The biquaternionic gradient

$$
\tilde{\nabla} = e_0\,\partial_{ict} + e_1\,\partial_x + e_2\,\partial_y + e_3\,\partial_z
$$

requires four global coordinates, and requires in addition that the time direction be the coefficient of $e_0$ — that is, a preferred split of the coordinates into a time function and three spatial functions. The Maxwell and Dirac equations of the companion articles are written with this operator and inherit the requirement.

**4. A global symmetry group.** The rotor group is the group of units of a fixed algebra. It is a global object. A curved manifold has no global group of that kind acting on it; what it has is a pointwise copy of the group at each point, if the frame is chosen.

The framework is not silent about these limitations. *Introduction to the Biquaternion Universe* lists the extension to curved spacetime as an open question; *Why Complexify Spacetime?* observes that the $ict$ convention "is tied to the existence of a global inertial frame"; and *Electromagnetism in Media — The Local Complex Structure at Work* states the position precisely: the algebra is "fixed while its embedding in physical spacetime is not." That last clause is the one this article takes seriously, because an embedding that varies from point to point is exactly where curvature would have to live.

## Curvature Cannot Be Carried by the Algebra

An algebra has no points, so it cannot have a curvature. The statement is worth making concrete rather than rhetorical. The biquaternion norm on $\mathbb{B}$ is a quadratic form with constant coefficients in a fixed basis; the only freedom in writing it is a change of basis, that is, a linear transformation, and a linear transformation maps a flat form to a flat form. There is no parameter in $\mathbb{B}$ that a field could modulate and no way to make the coefficient of the time direction a function of position. If one wants curvature in this framework, one must supply it in the map that attaches $\mathbb{B}$ to spacetime.

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

**Reading A, the point map.** Take the four-position as the framework writes it, $\tilde{Q} = ict\,e_0 + \mathbf{x}$, with the local $c$. Then $c$ is a function of position and

$$
d(ict) = ic\,dt + i\,t\,dc,
$$

so the displacement biquaternion is $d\tilde{Q} = i(c\,dt + t\,dc)e_0 + d\mathbf{x}$ — still an element of $\mathbb{M}_-$ — and the interval is $ds^2 = N(d\tilde{Q})$,

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

Suppose Reading B is intended. Its curvature can be computed in closed form. The components below are quoted in the corpus's curvature convention — the convention of *Curvature and Geodesics*, in which $R(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$ and the unit two-sphere has positive scalar curvature, and the convention of the linearized-gravity, gravitational-wave and graviton-quantization articles. Writing $u = c = 1/\sqrt{\epsilon\mu}$ and allowing $u$ to depend on time as well as position,

$$
R_{00} = u\,\Delta u, \qquad R_{0i} = 0, \qquad R_{ij} = -\frac{\partial_i\partial_j u}{u},
$$

where $\Delta$ is the three-dimensional Laplacian and the indices $i,j$ run over the spatial directions. Equivalently, with $f = c^2$, $R_{00} = \left(2f\,\Delta f - |\nabla f|^2\right)/(4f)$ and $R_{ij} = \left(-2f\,\partial_i\partial_j f + \partial_i f\,\partial_j f\right)/(4f^2)$. For example $c = 2 + \sin x$ gives scalar curvature

$$
R = \frac{2\sin x}{2 + \sin x},
$$

which is $+\tfrac{2}{3}$ at $x = \pi/2$ and vanishes at $x = 0$ and $x = \pi$.

The class is narrow in a way that is easy to state: one free function of the spatial coordinates (or of time as well), no shift vector, and a flat three-metric on the spatial slices, $g_{ij} = \delta_{ij}$. It is the diagonal, spatially rigid sub-case of the frame route of the next section.

Its decisive limitation is the following. Within this class, **Ricci-flatness forces flatness.** The condition $R_{ij} = 0$ requires $\partial_i\partial_j u = 0$ for every pair of spatial indices, so $u = \mathbf{a}(t)\cdot\mathbf{x} + b(t)$ is affine in the spatial coordinates; then $R_{00} = u\,\Delta u$ vanishes automatically, so this is the whole Ricci-flat family. And every member of that family is flat: for $u = \mathbf{a}(t)\cdot\mathbf{x} + b(t)$ with arbitrary functions $\mathbf{a}(t)$ and $b(t)$, the Riemann tensor vanishes identically, as direct symbolic computation of the general case confirms. The family is the algebra's way of writing a uniformly accelerated (Rindler-type) frame, and it is a reparametrisation of Minkowski space.

The consequence is worth stating plainly, in the restricted sense in which it holds. A metric that the local-scale route can write down at all cannot be a non-flat Ricci-flat spacetime. It therefore cannot carry a vacuum gravitational field with Weyl curvature, and with it no vacuum gravitational wave and no vacuum black-hole exterior. This is a statement about a metric class, not a theorem about the biquaternion programme — but it is enough to show that the local scale factor of the imaginary time axis is not the route by which general relativity will enter the framework.

There is a further conceptual gap along this route, independent of the calculation. The $c$ in $1/\sqrt{\epsilon\mu}$ is the speed of light in a material medium — a property of a dielectric, measurable with a capacitor and a magnet. The standard effective-geometry literature (Gordon's metric and its modern descendants in transformation optics) already attaches a metric to a dielectric medium, and that metric is a metric for *light*: it reproduces the ray trajectories of Maxwell's equations in the medium, not the free-fall trajectories of test masses. Identifying the medium's effective metric with the spacetime metric is a further step, and the framework's "in the same spirit as the metric in general relativity" is an analogy rather than that step. Nothing in the framework supplies it.

**A wider class exists, and an instance of it is Ricci-flat.** The class above is what one free function writes by itself, but a frame field is not confined to it: allowing the radial leg of the frame to vary along with the time leg widens the class, and a spatially stretched $c$-metric is its natural member. An external programme takes exactly that step. A. Waser reads gravitation as the effect of a spatially varying speed of light and fixes the profile by its own force law: setting $F_g=-mc\,\nabla c=-m\nabla(c^2/2)$ equal to Newton's $-GMm/r^2$ gives the profile, and the model then works with the line element,

$$
c=c_0 f(r),\qquad f(r)=e^{-r_s/(2r)},\qquad r_s=\frac{2GM}{c_0^2},
$$

$$
ds^2=-f(r)^2 c_0^2\,dt^2+\frac{dr^2+r^2\,d\Omega^2}{f(r)^2}.
$$

The profile agrees with the local-scale route's $c^2=c_0^2(1-r_s/r)$ to first order in $r_s/r$; the inverse squaring of the spatial part is a separate posit, and it is what removes the no-go above. Truncated at first order, $f^2=1-r_s/r$, this metric **is** the Schwarzschild exterior and is exactly Ricci-flat — direct computation gives $R_{\mu\nu}=0$ — and the classical tests the paper then computes are those of that truncated metric. At the profile the author actually derives, $f^2=e^{-r_s/r}$, the same computation returns a non-vanishing Ricci tensor, with $R_{11}=-r_s^2/(2r^4)$ in the corpus's curvature convention and a Ricci scalar of order $r_s^3/r^5$, both vanishing as $r\to\infty$. The metric the model itself supplies is therefore **not** a vacuum solution of Einstein's equations, and the Schwarzschild metric is its first-order truncation, differing from it at order $(r_s/r)^2$. The instance matters twice over. It shows that the wider class does contain non-flat Ricci-flat members, which answers the question the class raises; and it shows that the member is selected by the frame field and by the fitted profile, both inserted to match Newton's law, not by the algebra. (The programme's one prediction not shared with general relativity is a screening of the static field, sized in *The Empirical Status of the Biquaternion Framework*.)

## Route Two: A Field of Frames

The general way to make the embedding of spacetime into the algebra local is to allow the coordinate differentials to be carried into $\mathbb{M}_-$ by a point-dependent frame:

$$
d\tilde{Q} = \tilde{E}_\mu(x)\,dx^\mu, \qquad \tilde{E}_\mu(x) \in \mathbb{M}_- .
$$

The interval is $ds^2 = N(d\tilde{Q})$, and since $N$ is the polar form evaluated on $d\tilde{Q} = \tilde{E}_\mu dx^\mu$,

$$
g_{\mu\nu}(x) = \langle \tilde{E}_\mu(x), \tilde{E}_\nu(x)\rangle
= \mathrm{Sc}\left(\tilde{E}_\mu \tilde{E}^{\natural}_\nu\right).
$$

Four $\mathbb{M}_-$-valued fields, so sixteen functions. Where they are linearly independent, the Gram matrix is nondegenerate, and by Sylvester's law it has signature $(3,1)$: the result is automatically a Lorentzian metric. Conversely, any Lorentzian metric can be written this way locally. Choose a $g$-orthonormal frame, map it into $\mathbb{M}_-$ by a linear isometry of quadratic spaces — which exists because both forms have signature $(3,1)$ — and read off the coordinate components. So there is no obstruction: **the framework can carry any curved metric.**

What makes the route more than a change of notation is the local symmetry. If $\tilde{\Lambda}(x)$ is a unit-norm biquaternion depending on position, then

$$
\tilde{E}_\mu \longmapsto \tilde{\Lambda}\tilde{E}_\mu\tilde{\Lambda}^{*}
$$

leaves $g_{\mu\nu}$ unchanged at every point, because rotor conjugation preserves the bilinear form. So the local gauge group supplied by the algebra is exactly a copy of $SL(2,\mathbb{C})$ at each point, with the double cover, the Lie algebra, and the $\left(m,n\right)$ representation theory of the read list applying pointwise. This is the standard tetrad or vierbein structure of the spinor formulation of general relativity, written in the algebra's own notation; the interplay of the sixteen frame functions with the six local rotor parameters leaves $16 - 6 = 10$ independent components, which is the number of components of $g_{\mu\nu}$.

The corresponding flatness statement is exact and instructive. If the frame is *pure rotor gauge*, $\tilde{E}_\mu = \tilde{\Lambda}(x)\,\epsilon_\mu\,\tilde{\Lambda}(x)^{*}$ for a fixed basis $\epsilon_\mu$ of $\mathbb{M}_-$, then $g_{\mu\nu}(x) = \langle \epsilon_\mu, \epsilon_\nu\rangle$ is a constant matrix, and the metric is flat. A point-dependent rotor field applied to a rigid basis produces no curvature whatever. Curvature in this route is exactly that part of the frame which is not of this pure-gauge form, and no amount of rotor-field machinery detects it.

Two honest qualifications keep this from sounding like more than it is.

First, *carrying is not deriving*. The frame field is inserted by hand, and it is subject to no condition from the algebra. Every Lorentzian metric, including every vacuum spacetime, is representable; the framework excludes nothing. That is not a success but an emptiness: the entire content of the construction is the sixteen functions, and the algebra contributes only a fixed four-dimensional real vector space with a form of signature $(3,1)$, which any such space would contribute equally. Nothing that distinguishes $\mathbb{B}$ — the quaternionic multiplication, the two-sector decomposition, the complex structure — is used in writing $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle$.

Second, *this route does not make the complex structure local*. The frame field is a real linear map at each point; the imaginary direction of $\mathbb{B}$ remains globally the coefficient of $e_0$ in a fixed basis. The framework's local complex structure and the tetrad's local frame are different devices, and neither contains the other: the frame route gives general relativity's kinematics and abandons the framework's own locality proposal, while the local-scale route keeps that proposal and cannot reach even a non-flat Ricci-flat vacuum. This tension is a finding of this article, not a problem it resolves. One thing the external record shows is that the frame **language**, rather than the algebra, is where the tension lives: a construction recorded below, under *An External Claim That the Bundle Basis Is Biquaternionic*, carries the same metric with no vierbein at all — the basis is four $\mathbb{M}_-$-valued fields $s_\mu$ themselves — and derives its connection from a condition on the basis rather than inserting one.

## Route Three: The Connection, and the Two-Sided Derivative

A frame field is not by itself a geometry; a manifold also needs a way to compare frames at neighbouring points, that is, a connection. Here the biquaternion algebra makes a genuine and positive contribution, and the contribution has a trap in it that is worth recording.

The positive part is dimensional. The Lie algebra of the rotor group is the traceless part of $\mathbb{B}$,

$$
\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}
= \mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\} \oplus \mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}
= \left\{ G \in \mathbb{B} : G + \bar{G} = 0 \right\},
$$

six real dimensions, with the rotation generators $J_k = e_k$ and the boost generators $K_k = ie_k$ of the read list. Since this Lie algebra is a subspace of $\mathbb{B}$, a connection 1-form and its curvature 2-form can both be carried as $\mathbb{B}$-valued objects — specifically, as objects valued in that six-dimensional subspace. The spin connection of the tetrad formalism is therefore not foreign to the algebra; it sits inside it.

The trap concerns the covariant derivative. The group acts on the material sector by the two-sided formula $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, so the infinitesimal action of a generator $G$ is

$$
\tilde{Q} \longmapsto \tilde{Q} + \epsilon\left(G\tilde{Q} + \tilde{Q}G^{*}\right) + O(\epsilon^2),
$$

which is **not** in general the commutator $[G,\tilde{Q}]$. The two agree exactly when $G^{*} = -G$, which is the case for the rotation generators $e_k$; for the boost generators $ie_k$, which are Hermitian, they do not agree. On $\tilde{Q} = iq_0 + q_1e_1 + q_2e_2 + q_3e_3$, the boost generator $G = ie_1$ acts to first order as

$$
q_0 \longmapsto q_0 - 2\epsilon q_1, \qquad q_1 \longmapsto q_1 - 2\epsilon q_0,
$$

mixing the time and $e_1$ components as a boost must, whereas $[G,\tilde{Q}]$ is $2\epsilon(-iq_3\,e_2 + iq_2\,e_3)$, a rotation in the $e_2e_3$ plane — a different transformation altogether. A biquaternionic covariant derivative must therefore be written in the two-sided form

$$
D_\mu \tilde{Q} = \partial_\mu \tilde{Q} + \tilde{\Gamma}_\mu \tilde{Q} + \tilde{Q}\tilde{\Gamma}_\mu^{*} ,
$$

with $\tilde{\Gamma}_\mu$ in the Lie subspace; the natural abbreviation $D_\mu = \partial_\mu + [\tilde{\Gamma}_\mu, \cdot]$ would be wrong for exactly the boosts, which is where the Lorentzian content of the theory lives.

One object in this neighbourhood is automatic and one is not. The automatic one is the logarithmic derivative of a rotor field: if $\tilde{\Lambda}(x)$ is unit-norm, then both $\tilde{\Lambda}^{\natural}\,\partial_\mu\tilde{\Lambda}$ and $\partial_\mu\tilde{\Lambda}\,\tilde{\Lambda}^{\natural}$ are traceless, hence lie in the Lie algebra, because $\tilde{\Lambda}^{\natural}\tilde{\Lambda} = e_0$ differentiates to zero. So a frame carried by a rotor field arrives with a natural $\mathrm{SL}(2,\mathbb{C})$-valued connection. But it is pure gauge, and its curvature vanishes — which is the same statement as the flatness of the rotor-field metric in the previous section, arrived at from the other direction. Consistency, not new content.

What is not automatic is everything one would want. Metric compatibility and the vanishing of torsion are conditions, not consequences; nothing in the algebra selects the Levi-Civita lift. And the whole dynamics is absent: there is no action, no field equation for $\tilde{E}_\mu$ or $\tilde{\Gamma}_\mu$, and therefore no Einstein equation. The algebra can hold the objects of the spin-connection formalism in the same notation in which it holds the rotors and the four-vectors. It does not generate a single equation for them.

## The Arena Alternative: Algebra Valued Coordinates

The three routes above accept the article's premise and look for the map that attaches $\mathbb{B}$ to a manifold. There is a fourth position, and it is the only one that attacks the premise instead: **put the algebra in the coordinates**, so that the arena itself is not a manifold. It is worth naming here, because it is the sharpest existing answer to the sentence this article began from — *the algebra has no points* — and because a reader who meets that sentence should know that the answer has been tried.

The construction is *extended relativity in Clifford spaces*, whose principal review is by Castro and Pavšič (2004). The coordinates are themselves Clifford valued; for a four-dimensional base one writes

$$
X = \sigma\,1 + x^\mu\gamma_\mu + \tfrac12 x^{\mu\nu}\gamma_\mu\wedge\gamma_\nu + \tilde{x}^\mu I\gamma_\mu + \tilde{\sigma} I ,
$$

one coefficient for each grade — scalar, vector, bivector, pseudovector, pseudoscalar — so that a "point" carries a line, an area, a volume and a hyper-volume, and the arena is called a **Clifford space** (C-space). The invariant interval generalizes accordingly, $|dX|^2 = d\sigma^2 + dx_\mu dx^\mu + \tfrac12 dx_{\mu\nu}dx^{\mu\nu} - d\tilde{x}_\mu d\tilde{x}^\mu - d\tilde{\sigma}^2$, the signs of the last two terms being fixed by the square of the volume element, $I^2 = -1$ in signature $(+,-,-,-)$; and the transformations that preserve it generalize the Lorentz transformations by mixing objects of different grade, so that a history of one dimension is reshuffled into a history of another.

The trade is exact, and it should be stated as a trade rather than as a solution. What the construction buys is the opposite of what this article has been recording: the extended objects — closed strings, membranes, $p$-branes — are not fields *on* the arena, they are among its coordinates, so a single action covers all $p$; and a fundamental length, the Planck scale, has a natural place to enter, as the parameter that bridges grades. What it costs is the manifold. The coordinates are **non-commuting** polyvectors, so there is no space of points, and distance, connection, dimension and even signature have to be rebuilt — the review's own proposal is that the signature is relative to a chosen slice through C-space, which is a notion the corpus does not have and does not need (see the remark on signature in *The Clifford Structure of the Biquaternion Algebra*). Two things must not be conflated: a C-space is an **algebra of coordinates**, while the corpus's $\mathbb{B}$ is an **algebra of fields and observables**; the corpus's algebra is the even part of a four-dimensional Clifford algebra, and the review's arena is a manifold of Clifford numbers.

The honest summary is that this is a different framework, not an extension of the one developed here, and that it does not fill this article's gap. The missing dynamics is missing in both: C-spaces supply a richer arena and a unified action for free extended objects, but the corpus's boundary — the biquaternion framework contains the kinematical fibre of tetrad gravity and none of its dynamics — is neither crossed nor refuted by moving the algebra into the coordinates. What the position does establish is that the sentence *the algebra has no points* is a statement about $\mathbb{B}$ as this framework uses it, not a theorem about algebras. The empirical status of the scale that C-spaces make natural is recorded in *The Empirical Status of the Biquaternion Framework*.

## The Biquaternion Dirac Equation on a Curved Background

The connection of the previous section was built for the material sector, where the field is a four-vector and the group acts by the two-sided rotor conjugation. The Dirac field is a different kind of object — a section of the spinor module, a minimal left ideal $\mathbb{B}\tilde\Pi$ — and the difference in the kind of field, together with the difference in the kind of action, is exactly what the curved Dirac equation turns on. This section writes that equation in the framework's own notation. It is the item the agenda below records as the curved-space form of the biquaternion Dirac equation.

### The one-sided spinor derivative

The Lorentz group acts on the spinor module by **left multiplication**, $\psi \mapsto \tilde\Lambda\psi$, not by rotor conjugation; the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* establishes this, and it is the algebraic difference between a four-vector and a spinor. The covariant derivative compatible with that action is therefore **one-sided**,

$$
D_\mu\psi = \partial_\mu\psi + \tilde\Gamma_\mu\psi,
\qquad
\tilde\Gamma_\mu \in \mathrm{SL}(2,\mathbb{C})_{\mathbb{R}} \subset \mathbb{B},
$$

which is not the two-sided prescription of the material sector, $D_\mu\tilde{Q} = \partial_\mu\tilde{Q} + \tilde\Gamma_\mu\tilde{Q} + \tilde{Q}\tilde\Gamma_\mu^{*}$. The two must not be conflated. The vector carries the transformation twice, once on each side, $\tilde{Q} \mapsto \tilde\Lambda\tilde{Q}\tilde\Lambda^{*}$, and so receives two connection terms; the spinor carries it once, $\psi \mapsto \tilde\Lambda\psi$, and so receives one. Both connection terms live in the same six-dimensional Lie subspace, and each is the standard inhomogeneous connection of the module it belongs to.

Covariance fixes the transformation law. If $\psi \mapsto \tilde\Lambda\psi$, then $D_\mu\psi \mapsto \tilde\Lambda D_\mu\psi$ precisely when the connection transforms as

$$
\tilde\Gamma_\mu \longmapsto \tilde\Lambda\tilde\Gamma_\mu\tilde\Lambda^{-1}
- \left(\partial_\mu\tilde\Lambda\right)\tilde\Lambda^{-1},
$$

which is the inhomogeneous transformation expected of a connection on a module. A rotor field supplies an example at once: $\tilde\Gamma_\mu = -\left(\partial_\mu\tilde\Lambda\right)\tilde\Lambda^{-1}$ is pure gauge, and its curvature vanishes, exactly as the rotor-carried frame of the previous sections is pure gauge and flat.

### The curved Dirac operator and the equation

The biquaternion gradient of the flat articles is $\tilde\nabla = e_\mu\partial_\mu$ with the rigid basis $e_\mu = (e_0, e_1, e_2, e_3)$ and $\partial_\mu = (\partial_{ict}, \partial_x, \partial_y, \partial_z)$. Its curved replacement substitutes the frame field for the rigid basis and the one-sided derivative for the partial derivative:

$$
\tilde{\not D} = \tilde E^\mu D_\mu,
\qquad
\tilde E^\mu = g^{\mu\nu}\tilde E_\nu,
\qquad
\langle \tilde E^\mu, \tilde E_\nu\rangle = \delta^\mu{}_\nu,
$$

where $\tilde E^\mu$ is the **dual frame**, the inverse tetrad of the frame field $\tilde E_\mu$ of Route Two. The operator is biquaternion-valued and first order, and it is the object the whole tetrad machinery was assembled to define. The **massless** equation is

$$
\tilde{\not D}\psi = 0,
$$

identical in form to the flat massless equation. The **massive** equation is the chiral pair

$$
\tilde{\not D}\tilde\Psi_R = m\tilde\Psi_L,
\qquad
\tilde{\not D}^{\natural}\tilde\Psi_L = m\tilde\Psi_R,
$$

where $\tilde{\not D}^{\natural}$ is the quaternion-conjugate operator, built from the conjugate frame and the conjugate connection and reducing to $\tilde\nabla^{\natural}$ when the frame is rigid and the connection vanishes. The mass term is unchanged: it is the field-independent, chirality-off-diagonal pairing of the parent, and the curvature enters only through the derivative. That is the structural point of the pair, and it is worth stating in the framework's language: the mass is a constant right multiplication acting between the two minimal left ideals, and no amount of frame or connection is needed to write it.

### Flat limit and the square

Two consistency statements locate the construction.

The **flat limit** is exact. If the frame is the rigid basis, $\tilde E_\mu = e_\mu$, so that $\tilde E^\mu = e^\mu$ and $g_{\mu\nu} = \eta_{\mu\nu}$, and if the connection vanishes, $\tilde\Gamma_\mu = 0$, then $\tilde{\not D} = \tilde\nabla$ and the pair reduces to the flat pair of the parent article. The curved operator is a strict generalisation: nothing is added at flatness, and nothing of the flat structure is lost.

The **square** is the Lichnerowicz formula. Squaring the Dirac operator gives

$$
\tilde{\not D}^2 = \Box_g - \tfrac14 R,
$$

where $\Box_g = \frac{1}{\sqrt{-\det g}}\,D_\mu\!\left(\sqrt{-\det g}\,g^{\mu\nu}D_\nu\right)$ is the Laplace–Beltrami operator acting on spinors and $R$ is the Ricci scalar (the statement is the standard one, in the sign convention of the cited literature). The curvature term is not optional: a Dirac field on a curved background obeys a Klein–Gordon-type equation with the $-R/4$ coupling even in the absence of any source, which is the curved-space face of the statement that the square of a first-order operator is second order. With minimal coupling to an electromagnetic potential of the companion articles, the square acquires in addition a field-strength–spin term of the form $F_{\mu\nu}\Sigma^{\mu\nu}$, the curved-space relative of the Pauli term of the Gordon decomposition; its coefficient is stated in the curved-Dirac literature and is not rederived here. For comparison, the alternative first-order equation whose square is exactly the Laplacian, without the $-R/4$ term, is the **Dirac–Kähler equation**; the companion maths article records the price of that alternative, which is the loss of the Lorentz-covariant fourfold split in curved spacetime.

### What this does and does not settle

It settles the agenda item that asked for the curved-space form of the biquaternion Dirac equation written in the framework's own notation. The operator $\tilde{\not D} = \tilde E^\mu D_\mu$, the one-sided derivative, the connection transformation, the massless equation and the massive chiral pair, the flat limit, and the Lichnerowicz square are now written, and every object in them — the frame, the dual frame, the connection, the one-sided derivative — is an object the algebra already carries. Two features separate the curved Dirac equation from the curved metric: the field's derivative is one-sided and its connection transformation inhomogeneous, while the frame's derivative is two-sided and its metric is bilinear in the frame; and the curvature couples to the field through $-R/4$ even without a source, so the curved Dirac square is not the naive curved Klein–Gordon operator.

What it does not settle is everything the frame and the connection already failed to settle, and the Dirac equation is the most inviting place to overclaim, so the limits bear repeating. The equation contains the frame and the connection; it determines neither. Nothing in the algebra or in this equation fixes $\tilde E_\mu$ or $\tilde\Gamma_\mu$, selects the Levi-Civita lift rather than a torsionful one, or supplies an action for either; the Einstein equation is as absent here as it was in Route Three. The equation is the correct curved-space transcription of the matter equation **on a background** whose geometry is inserted by hand, and that is exactly what it is. On the matter side, the source of the equation — the conserved current — remains the spinor-module object of the minimal-coupling and Gordon-decomposition articles, carrying the Clifford-odd $\gamma^0$ that a product in $\mathbb{B}$ cannot supply; the closed sourced system, in which the Dirac current feeds the curved biquaternion Maxwell equation, is still unwritten. And the global question survives untouched: whether spinor fields exist on the manifold at all is the topological condition of Route Two's agenda, and no local operator can answer it.

### Lorentz Gauging and the Euler–Lagrange Variation

The coupling written above is the standard one: the flat equation with the rigid basis replaced by the frame and the partial derivative by the one-sided Lorentz-covariant derivative. An external source shows that this standard coupling carries an ambiguity the corpus has not recorded, and that the ambiguity sits exactly where the frame and the connection enter.

J. Fredsted, *Obtaining consistent Lorentz gauging for a gravitationally coupled fermion* (arXiv:1906.12200v3 [physics.gen-ph], 2019), proves that for a Dirac fermion coupled to gravity in the vierbein formulation the substitution $\partial_\mu \to D_\mu$ and the Euler–Lagrange variation **do not commute**. Varying the gauged action gives

$$
E_{\mathrm{grav}} = (ie^\mu{}_a\gamma^a\partial_\mu - m)\psi
- \tfrac{i}{2}e^{\mu}{}_{b}\,\omega_{\mu}{}^{b}{}_{a}\gamma^a\psi
+ \tfrac{i}{4}e^\mu{}_a\,\omega_{\mu cd}\{\gamma^a,S^{cd}\}\psi ,
$$

while substituting the same replacement into the flat equation of motion gives

$$
\tilde E_{\mathrm{grav}} = (ie^\mu{}_a\gamma^a\partial_\mu - m)\psi
+ \tfrac{i}{2}e^\mu{}_a\,\omega_{\mu cd}\gamma^a S^{cd}\psi ,
$$

and the two differ by the anticommutator $\{\gamma^a,S^{cd}\}$ that the variation produces and the substitution does not. The source reads the mismatch as a violation of the equivalence principle, since the action-derived equation $E_{\mathrm{grav}}$ must take precedence over the substituted one $\tilde E_{\mathrm{grav}}$. For an internal gauge force the two procedures agree, because the internal generators commute with $\gamma^a$; gravity is exceptional, and the reason is that the Lorentz generator satisfies $[\gamma^c,S^{ab}] = V^{ab}{}_d\gamma^d$ rather than commuting.

The corpus's curved equation is the substitution form. The section above writes $\tilde{\not D}\psi = 0$ and the chiral pair $\tilde{\not D}\tilde\Psi_R = m\tilde\Psi_L$, $\tilde{\not D}^{\natural}\tilde\Psi_L = m\tilde\Psi_R$ by replacing the rigid basis and the partial derivative, and the article supplies no action for the coupled system whose variation could be compared with them. So this article does not take a side in the ambiguity. What the external source establishes is that the side matters: the corpus has been writing one of two inequivalent forms without saying which.

**The world-index repair.** The same source then constructs a formalism in which the two procedures commute again, and the construction differs from the corpus's in a way worth stating. The spinor field carries a **world (coordinate) index** $\psi^\rho$, not a Lorentz spinor index, and no Lorentz indices appear at all, neither vector nor spinor. The local Lorentz frame is carried by one timelike and three spacelike world vector fields $n^\mu$ and $n^\mu{}_i$ obeying

$$
n\!\cdot\!n = 1, \qquad n\!\cdot\!n_i = 0, \qquad n_i\!\cdot\!n_j = -\delta_{ij},
$$

so a vierbein is hidden in them and never used, and the metric is $g_{\mu\nu} = n_\mu n_\nu - \delta^{ij}n_{i\mu}n_{j\nu}$. Two families of matrices replace the gamma matrices: $M^\mu{}_{\rho\sigma}$ built from $n^\mu$ and $N_i{}^\rho{}_\sigma$ built from $n^\mu{}_i$,

$$
M^{\mu\rho\sigma} = \bigl(g^{\mu\rho}g^{\nu\sigma} + g^{\mu\sigma}g^{\nu\rho} - g^{\mu\nu}g^{\rho\sigma} - i\varepsilon^{\mu\nu\rho\sigma}\bigr)n_\nu,
$$

$$
N_i{}^{\rho\sigma} = -\bigl(g^{\mu\rho}g^{\nu\sigma} - g^{\mu\sigma}g^{\nu\rho} - i\varepsilon^{\mu\nu\rho\sigma}\bigr)n_\mu n_{\nu i},
$$

and they obey the algebra

$$
M_\mu M_\nu^* + M_\nu M_\mu^* = 2g_{\mu\nu}\mathbf{1}, \qquad
M^\mu N_i^* + N_i M^\mu = 0, \qquad
N_i N_j = \delta_{ij}\mathbf{1} + i\varepsilon_{ijk}N_k,
$$

which is the role the Dirac algebra plays in the standard formalism; the free Lagrangian is Klein–Gordon compatible because of it. The covariant derivative is

$$
\partial_\mu\psi^\rho \;\longmapsto\;
D_\mu\psi^\rho = \Bigl(\delta^\rho{}_\sigma\nabla_\mu + \tfrac12\omega_{\alpha\beta\mu}S^{\alpha\beta\,\rho}{}_\sigma\Bigr)\psi^\sigma ,
$$

where the Levi-Civita $\nabla_\mu$ appears explicitly because the index is a world index, and $S_{\mu\nu}$ is the spinor generator, $4S_{\mu\nu} = M_\mu M_\nu^* - M_\nu M_\mu^*$, related to the vector generator by $2S_{\mu\nu} = V_{\mu\nu} + i\varepsilon_{\mu\nu}$, self-dual, and satisfying the source's Eq. (27), the same algebra as $\tfrac14[\gamma^a,\gamma^b]$. The Lorentz rotation acts on the field through $\delta\psi^\mu = \tfrac12(d\theta^{\alpha\beta})S_{\alpha\beta}{}^\mu{}_\nu\psi^\nu$. With these objects the varied equation is **identically** the substituted equation, so the gauging and the variation commute by construction and the ambiguity of the standard vierbein coupling is removed.

**The geometry the repair rests on: the connection is solved, not postulated.** The frame fields are not free parameters of the source's formalism; the connection is built out of them rather than assumed beside them. The metric is the polar form of the frame, $g_{\mu\nu} = n_\mu n_\nu - n_{i\mu}n_{i\nu}$ with $i$ summed, so that the orthonormality conditions of the frame are the statement that the frame is orthonormal; and the source's connection $\omega^\mu{}_{\nu\rho}$ is fixed by requiring the frame to be covariantly constant,

$$
D_\rho n^\mu = 0 , \qquad D_\rho n^\mu{}_i = 0 .
$$

Metric compatibility then follows by the Leibniz rule instead of being imposed, $D_\rho g_{\mu\nu} = 0$, because $g$ is built from the $n$'s. With the frame so fixed the source computes the curvature of $\omega$ and finds

$$
\Omega^\mu{}_{\nu\rho\sigma} = -R^\mu{}_{\nu\rho\sigma} ,
$$

the Riemann tensor of the Levi-Civita symbols, the two sides differing by a sign and nothing else, because the commutator $[D_\rho,D_\sigma]$ annihilates each frame field and the frame is complete. The gravitational action is therefore still the Einstein–Hilbert one, as the source's abstract claims: $g^{\mu\rho}g^{\nu\sigma}\Omega_{\mu\nu\rho\sigma} = -R$ is the Einstein–Hilbert Lagrangian up to a sign. The identity has a second face, and it is the one that matters for this article. Because $\omega$ has been solved for in terms of the metric, it is **not an independent field**, the formalism is not a local-Lorentz gauge theory in the sense of Route Three above, there is no field strength of $\omega$ to vary separately, and the compatibility failure of the standard vierbein coupling cannot arise because the object that produced it has been eliminated. What the construction therefore exhibits is a Lorentz-invariant formalism with no Lorentz index anywhere and with the Einstein–Hilbert action intact — at the cost of having no independent Lorentz connection to add dynamics to.

**The world index, and why the coordinate connection cannot be dropped.** The substitution takes the spinor-index form $\partial_\mu\psi \to \partial_\mu\psi + \tfrac12\omega_{\alpha\beta\mu}S^{\alpha\beta}\psi$ of the standard theory to

$$
\partial_\mu\psi^\rho \;\longmapsto\; D_\mu\psi^\rho
= \Bigl(\delta^\rho{}_\sigma\nabla_\mu + \tfrac12\omega_{\alpha\beta\mu}\,(S^{\alpha\beta})^\rho{}_\sigma\Bigr)\psi^\sigma ,
$$

and the sentence the source attaches to it carries the whole point: the Levi-Civita covariant derivative appears explicitly **because the spinor now carries a world index**, "in contrast to Eq. (1), where $\psi$ carries only a spinor index". In the standard coupling the spinor index is a Lorentz spinor index, so the partial derivative is promoted by the spin connection alone and no coordinate connection ever appears; the vierbein is then what converts a world vector index into a Lorentz one, and that conversion, performed on the frame in the varied action, is precisely the origin of the anticommutator $\{\gamma^a,S^{cd}\}$. Once the spinor's index is a world index there is nothing to convert, so nothing produces an anticommutator and the varied and substituted equations coincide by construction. The formalism's parsimony is thus not decorative: the absence of Lorentz indices is the same fact as the commutativity of the gauging, seen from the other side. The diacritics of the algebra are the metric transpose, $(V^{\hat T})_\mu = g_{\mu\nu}V^\nu$ and $(A^{\hat T})^\mu{}_\nu = g^{\mu\rho}g_{\nu\sigma}A^\sigma{}_\rho$, which reduce to the ordinary transpose when the metric is flat; the $M_\mu$ are hat-hermitian and the $N_i$ hat-antisymmetric (Eqs. (22)–(23) of the source), which is what makes the Lagrangian real.

**Status here.** This is an external construction, recorded and not adopted. It is worth recording in this article because it names a gap the boundary list below does not yet contain: the corpus's curved Dirac equation is the substituted form of a gauged flat equation, and the source shows that the substituted form and the varied form are different when the gauge group is the Lorentz group. Its structural relations were recomputed for this article on a constant Levi-Civita frame in signature $(1,3)$ — the matrix algebra of the source's Eqs. (19)–(21), the hat-hermiticity and hat-antisymmetry (22)–(23), the self-duality of $S_{\mu\nu}$ and $S_{\mu\nu}+S_{\mu\nu}^{\hat T}=0$, and the spinor algebra (27) — and all hold; the mixed-index position of the epsilon in the relation $2S_{\mu\nu} = V_{\mu\nu} + i\varepsilon_{\mu\nu}$ is the one that makes it an identity. What the construction does not supply is the corpus's question: it is a formalism for a **background** metric handed in through $n^\mu$ and $n^\mu{}_i$, with no action for those fields, no Einstein equation, and no selection of the metric, so it removes the coupling ambiguity without touching the dynamical void this article has recorded throughout.

## The Informational Sector on a Curved Background

The second half of the framework — $\mathbb{M}_+$, its idempotents, its observables and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ — has no curved-space treatment, and it is worth saying why the absence is structural rather than a matter of effort.

When the spacetime is curved, the elements of $\mathbb{M}_+$ would have to become fields of operators, one copy of the algebra being attached at each point. That much is formal: the fibre is defined and the pointwise operator algebra goes through unchanged. What does not go through is the trace. The trace in the trace formula is the $2 \times 2$ matrix trace at a point; it has no volume element and no integration. Every trace in a field theory is an integral over the manifold, with a measure that itself depends on the metric, and the framework's trace cannot play that role. So even the Born rule, which is the most successful piece of the flat construction, has no constructed curved-space analogue here: the pointwise expectation value survives, the global one has nowhere to live.

The two-sector decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ is a pointwise decomposition and survives as such on any background. Beyond that, the curved setting is untouched. Any coupling between the sectors would have to be an equation of motion for fields belonging to both, and no such equation exists in the flat case either; a fortiori none exists here.

## An External Claim of One Tensor Language, and What It Does Not Supply

The two kinds of relativistic tensor dynamics — the antisymmetric one of electrodynamics and the symmetric one of relativity — are usually written differently, and there is an external claim that one biquaternion calculus carries both. E. P. J. de Haas (*Biquaternion Formulation of Relativistic Tensor Dynamics*, arXiv:1401.4470v1, 2013) constructs a biquaternion tensor calculus whose stated goal is exactly that fusion, in a language he describes as "very akin to the standard relativistic space-time language", and reports that it carries no extra terms relative to it. The claim is recorded here because this article's boundary list is where its scope has to be stated.

What such a claim is: a **representational unification at the level of the kinematical fibre**. It shows that one notation can carry a symmetric rank-two tensor and an antisymmetric one at once — which is the vicinity of this article's own bookkeeping problem, since the framework's fields are four-vectors in $\mathbb{M}_-$ while the gravitating source is a symmetric rank-two tensor, $(1,1)\oplus(0,0)$ in the vocabulary of the list below in *What Is Constructed and What Is Agenda*.

What it is **not**: a field equation. The paper supplies no action for the frame or for the connection, no selection of a metric, and no Einstein equation; by its author's own statement it presents known relativistic tensor dynamics in a new formalism, and it derives nothing. It is therefore not a partial answer to *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda*, and it does not advance the central open question there. The one thing it claims **about the algebra** — that the formulation produces no extra terms beyond the standard relativistic language, the condition being the Lorenz gauge $F_0 = \tilde\partial_\nu A^\nu = 0$ — is recorded, with its cautions, in *Relativistic Mechanics in Biquaternionic Form*.

The boundary of this article is unchanged by the claim, and the claim is unchanged by the boundary: one is about notation at a point, the other about dynamics for the field that attaches the notation to a curved manifold.

## An External Claim That the Bundle Basis Is Biquaternionic

A second external source reaches this article's own subject from the opposite direction, and it is worth separating from the first, because it claims more. D. J. Cirilo-Lombardo (*Algebraic structures, physics and geometry from a Unified Field Theoretical framework*, arXiv:1411.5493v3 [hep-th], 2015) works from a unified field theory unrelated to the corpus and asks what algebraic structure the **basis** of its principal fibre bundle $P(G,M)$ carries; his answer is the biquaternion algebra. The bundle is new here — no article of the series constructs a principal bundle over the manifold with the algebra in the basis — and the claim is *stronger* than anything this article has built, because a basis is exactly the thing the section *Curvature Cannot Be Carried by the Algebra* showed cannot carry curvature.

The dictionary is exact, and the companion article *The Biquaternion Basis of a Unified-Field Fibre Bundle* records the verification entry by entry. The source assembles its structural group blockwise from one $2\times2$ matrix $Q = a_0\sigma_0 - i\boldsymbol\sigma\!\cdot\!\mathbf a$, which is the matrix image $\Phi(\tilde Q)$ of the biquaternion $\tilde Q = a_0 + \mathbf a\!\cdot\!\mathbf e$ under the corpus's representation $\Phi(e_k) = -i\sigma_k$, with the coefficients fixed by a four-momentum, $a_0 = p_0/m$ and $\mathbf a = i\mathbf p/m$. Its unit-norm condition and its relativistic relation are then one identity, $N(\tilde Q) = 1$, and its object is the Hermitian biquaternion of $\mathbb{M}_+$ — the informational sector, not the material one this article's metric is read from. Its own "conjugate transpose" $G^+$ is the quaternionic conjugation of the block and not the matrix adjoint; that is the reading in which its $G^+G = I_4$ holds, and the distinction is invisible while the coefficients are real.

**Which naturality is meant.** The word *naturally* has to be split before the claim can be assessed, and the two readings are different statements. A **preferred-basis** claim would assert that the bundle's structure group reduces into the biquaternion unit group; that is a statement about $G$, it is testable, and the source's own test is $G^+G = I_4$ in just the conjugation that holds. An **algebra-on-the-fibres** claim would assert that each fibre is a module over $\mathbb{B}$; that is what *The Hopf Fibration and the Biquaternion Gauge Bundle* already constructs from the framework's side, and it is a statement about the fibres rather than about the basis. The corpus reads the second as true and unremarkable and the first as the substantive claim.

**What it does not supply.** No reduction is exhibited and no curvature is computed from the bundle, so the claim does not move this article's boundary. A biquaternionic basis would still be a pointwise structure, and a field attaching it to the manifold would still be required; a fibre algebra is not a connection, an action or a metric. The source's concluding geometry — a G-structure on $T(M)$ whose reduced structure group changes the spacetime structure itself, and a signature and CP character induced by torsion — is recorded, and left as a claim, in *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda*. One assertion of the source's is **not** reproduced: the Lorentzian metric it says is invariant under $G$ "due to its general form" is not invariant under it in any signature tried here; what does hold is the invariance of the quaternionic norm, and that only through $G^+$ and not through the ordinary transpose.

**A constructed instance, from the same algebra.** A third source does not merely claim that the basis can be biquaternionic; it builds the whole formalism around one, and the construction reproduces this article's frame route in the source's own notation. J. Fredsted (*Spinor fields without Lorentz frames in curved spacetime using complexified quaternions*, arXiv:0811.1357v4 [math-ph], 2009) discards the manifold frame outright — he writes "leaving the arena of Riemannian manifolds" — and takes as primitive a basis $s_\mu \in (\mathbb{C}\otimes\mathbb{H})_-$ inside the same biquaternion algebra, that is, exactly this article's material sector $\mathbb{M}_-$. The metric is then **defined**, not inserted, by the polar form,

$$
g_{\mu\nu} = \langle s_\mu, s_\nu\rangle ,
$$

which is this article's own $g_{\mu\nu} = \langle \tilde E_\mu, \tilde E_\nu\rangle$; the nondegeneracy of the metric follows from the linear independence of the four basis elements, and the source notes that a basis in the opposite sector $(\mathbb{C}\otimes\mathbb{H})_+$ would give the opposite signature. Local Lorentz freedom is the rotor conjugation $s_\mu \mapsto \Lambda s_\mu \bar{\Lambda}$ with $\Lambda$ in $Sp(1,\mathbb{C}) \cong SL(2,\mathbb{C})$, so the metric is invariant for the reason the frame route's metric is invariant: the same verified statement, written with the source's conjugations.

What makes the construction worth recording here is its connection. A **single** algebra-valued $\omega_\mu \in \mathbb{C}\otimes\mathbb{H}$, subject only to the reality condition $\mathrm{Sc}(\omega_\mu + \bar{\omega}_\mu^*) = 0$, carries everything: its imaginary-scalar part $\omega_\mu \in i\mathbb{R}$ is a local $U(1)$ freedom, which the source speculates may be electromagnetism, and its vector part $\omega_\mu \in \mathbb{C}\otimes\mathrm{Vec}(\mathbb{H})$ is the Lorentz connection. The spinor fields transform one-sidedly, $\psi_L \mapsto \Lambda\psi_L$ and $\psi_R \mapsto \psi_R\bar{\Lambda}$, and their covariant derivatives are correspondingly one-sided, with the connection inserted on the left for $\psi_L$ and on the right for $\psi_R$. This is the two-connections situation of *The Covariant Derivative and Gauge Connection in Biquaternionic Form* seen from the other side: the corpus keeps its central $U(1)$ connection $\tilde A_\mu$ and its traceless Lorentz connection $\tilde\Gamma_\mu$ apart and says no relation between them is asserted; the source has one algebra-valued connection whose two parts are the two objects. It also differs from the corpus's construction in that $\omega_\mu$ is a general biquaternion subject to one scalar condition, not restricted to the six-dimensional Lie subspace.

**The connection is derived, not inserted.** This is the part of the construction that goes beyond the frame route of this article. The source's covariant derivative of the basis is $D_\rho s_\nu = \nabla_\rho s_\nu + \omega_\rho s_\nu + s_\nu\bar{\omega}_\rho^*$ with $\nabla_\rho s_\nu = \partial_\rho s_\nu - \Gamma^\mu{}_{\nu\rho}s_\mu$, and the connection coefficients are then **determined**, not chosen, by the source's "minimality condition" $D_\rho s_\nu \equiv 0$:

$$
\Gamma^\mu{}_{\nu\rho} = \left\langle s^\mu,\ \partial_\rho s_\nu + \omega_\rho s_\nu + s_\nu\bar{\omega}_\rho^*\right\rangle .
$$

The bracketed element lies in $\mathbb{M}_-$ — it is a sum of the $\mathbb{M}_-$-valued derivative $\partial_\rho s_\nu$ and of terms $\omega_\rho s_\nu + s_\nu\bar{\omega}_\rho^*$, which combine into an $\mathbb{M}_-$ element — and the bilinear form is real on $\mathbb{M}_-$, so $\Gamma^\mu{}_{\nu\rho}$ is real-valued; this, together with the metric-compatibility computation below, was recomputed here. Two consequences deserve naming. First, **metric compatibility is a consequence, not a condition**: $\nabla_\rho g_{\mu\nu} = 0$ follows from the minimality of $\Gamma$ together with the reality condition on $\omega_\mu$, whereas Route Three above records metric compatibility and the vanishing of torsion as conditions the framework must impose from outside. Second, $\Gamma^\mu{}_{\nu\rho}$ **need not be symmetric** in its lower indices — the source states this, and the asymmetry is exactly what makes $\nabla_\mu A_\nu - \nabla_\nu A_\mu$ differ from $\partial_\mu A_\nu - \partial_\nu A_\mu$ for the connection's own $U(1)$ part.

**The curvature, and the Lagrangian the source leaves unsettled.** The field strength of the single connection is $\Omega_{\rho\sigma} = \nabla_\rho\omega_\sigma - \nabla_\sigma\omega_\rho + [\omega_\rho,\omega_\sigma]$, and the minimality condition turns the double commutator of covariant derivatives into the identity

$$
[\nabla_\rho,\nabla_\sigma]s_\mu + \Omega_{\rho\sigma}s_\mu + s_\mu\bar\Omega_{\rho\sigma}^* = 0 ,
$$

whose last two terms are the same two-sided sandwiching — left action of $\Omega$, right action of its conjugate — that Route Three's derivative $\partial_\mu\tilde Q + \tilde\Gamma_\mu\tilde Q + \tilde Q\tilde\Gamma_\mu^{*}$ exhibits. With the connection split as $\omega_\mu = \chi_\mu + igA_\mu$, where $\chi_\mu \in \mathbb{C}\otimes\mathrm{Vec}(\mathbb{H})$ and $A_\mu \in \mathbb{R}$, the field strength splits as $\Omega_{\mu\nu} = K_{\mu\nu} + igF_{\mu\nu}$ with $K_{\mu\nu} = \nabla_\mu\chi_\nu - \nabla_\nu\chi_\mu + [\chi_\mu,\chi_\nu]$ and $F_{\mu\nu} = \nabla_\mu A_\nu - \nabla_\nu A_\mu$; both the split and the term-by-term decomposition were verified here. The scalar piece of the one connection therefore produces a Maxwell-type field strength and the vector piece a Yang–Mills-type curvature. The source then proposes an Einstein–Hilbert-like Lagrangian, $(1/\kappa)L = R^{\mu\nu}{}_{\mu\nu}(\Gamma)$ with $R^\mu{}_{\nu\rho\sigma}(\Gamma) = \langle s^\mu,[\nabla_\rho,\nabla_\sigma]s_\nu\rangle$, and an alternative $(1/\kappa)L = \mathrm{Re}\langle\Omega^{\mu\nu},\Omega_{\mu\nu}\rangle$, and judges both unsettled; both are recorded, with the reason for each verdict, in *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda*.

**Weight of the instance.** A constructed instance is more than the bundle claim above, and it should be counted as what it is. It shows that the biquaternionic basis is not idle: four elements of $\mathbb{M}_-$ determine a Lorentzian metric through the algebra's own bilinear form, and one algebra-valued connection suffices for the tensor and spinor fields alike. It does not show more. There is no settled action for $s_\mu$ or $\omega_\mu$ and no field equation; the Riemann tensor of the induced connection and its identity with the field strength are written, but nothing is varied and no dynamics is attached to them, so the metric is general while its dynamics are absent, which is the same void this article records for the frame route. Nor is it a construction of the principal bundle $P(G,M)$ of the first source above: the basis is a basis of the algebra over the manifold, not the basis of a principal bundle with a structural group. The instance therefore raises the bundle claim's floor — from proposal to construction — without raising its ceiling.

## What Is Constructed and What Is Agenda

The boundary can be drawn as a list, and drawing it is this article's main result.

**Constructed** (algebraic facts, each recomputed for this article). The pointwise metric of $\mathbb{M}_-$ as the polar form of the biquaternion norm, with signature $(3,1)$. Its invariance under rotor conjugation. The representation of an arbitrary Lorentzian metric by a frame field $\tilde{E}_\mu \in \mathbb{M}_-$ with $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle$, and the local $SL(2,\mathbb{C})$ gauge invariance of that representation. The identification of the rotor group's Lie algebra with the six-dimensional traceless subspace of $\mathbb{B}$. The two-sided infinitesimal action of a connection, and the tracelessness of a rotor field's logarithmic derivative. The curved biquaternion Dirac operator $\tilde{\not D} = \tilde E^\mu D_\mu$, built from the dual frame and the one-sided spinor derivative $D_\mu\psi = \partial_\mu\psi + \tilde\Gamma_\mu\psi$, with its covariant connection transformation, its exact flat limit, and its Lichnerowicz square $\tilde{\not D}^2 = \Box_g - \tfrac14 R$. The induced metrics of the local-scale route in both readings, with the flatness of Reading A and the closed-form curvature of Reading B, and the result that within Reading B's metric class Ricci-flatness implies flatness.

**Agenda** (nothing constructed). An action principle or field equation for the frame or the connection, and hence any Einstein equation. Coupling to sources, with the bookkeeping problem that the gravitating objects are symmetric rank-2 tensors, $\left(1,1\right)\oplus\left(0,0\right)$, while the framework's own fields are four-vectors in $\mathbb{M}_-$. The curved-space form of the biquaternion **Maxwell** equation written in the framework's own notation, for which the background-dependence of $\tilde{\nabla}$ is precisely the obstacle; the corresponding **Dirac** form is constructed in the section *The Biquaternion Dirac Equation on a Curved Background* above, on a background whose frame and connection are still inserted by hand and whose current source remains the spinor-module object of the companion articles. The **coupling ambiguity** of the Lorentz gauge group: the Dirac form written here is the substituted form of a gauged flat equation, and the source recorded in *Lorentz Gauging and the Euler–Lagrange Variation* shows that the varied form differs, because the Lorentz generator does not commute with $\gamma^a$; whether the corpus should adopt the varied form, or the world-index formalism that removes the difference, is open. Global and topological structure of every kind: the algebra is a point, so causal structure, horizons, singularities, and topology are outside it, and even the existence of spinor fields on a manifold is a topological condition — the vanishing of the second Stiefel–Whitney class — that the algebra cannot see; the globalisation of the spinor module to a bundle over a curved background is recorded as a separate open item in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. The discrete symmetries, which are not in the connected rotor group. The informational sector, as above. And empirical contact, which remains the framework's central open question and is not advanced by anything here.

The honest summary of the boundary is this. The biquaternion framework contains the kinematical fibre of tetrad gravity: a pointwise Lorentzian vector space, its Lorentz group, the vector representation, and the Lie-algebra-valued connection. It contains nothing of tetrad gravity's dynamics, and nothing that selects a metric. It is therefore not correct to say that the framework contains general relativity, and it is not correct to say that it conflicts with it. What the framework contains is the algebra in which the local part of general relativity is normally written, plus a proposal — the local scale factor of the imaginary time axis — that is too rigid to carry the non-flat vacuum solutions.

## Summary

The read-list machinery is flat and pointwise: one fixed algebra, one fixed biquaternion norm with constant coefficients, a global chart with a distinguished imaginary time, and a global rotor group. Curvature cannot be made a property of the algebra, because the algebra has no points and no deformable coefficient; it can only be carried by the field that attaches the algebra to spacetime.

The framework's own local device is the local scale $c = 1/\sqrt{\epsilon\mu}$ of the imaginary time axis. It admits two inequivalent readings. As a map of points, $\tilde{Q} = i\,c(\mathbf{x})\,t\,e_0 + \mathbf{x}$, it yields a nondegenerate metric with $\det g = -c^2$ that is identically flat — the pullback of the flat form of $\mathbb{M}_-$ along a diffeomorphism — as direct computation confirms. As a derivative rule, $\partial_{ict} = -(i/c)\partial_t$ with $c$ held fixed in the differential, it yields $g_{\mu\nu} = \mathrm{diag}(-c^2,1,1,1)$, genuinely curved, with $R_{00} = u\Delta u$, $R_{0i} = 0$, $R_{ij} = -\partial_i\partial_j u / u$ for $u = c$. The framework's prose does not choose between the readings, and the choice is left open here.

Within the second reading's class — one function, no shift, flat spatial slices — Ricci-flatness forces $u$ to be affine in the spatial coordinates, and every such metric is flat. The class therefore contains no non-flat vacuum geometry: no Weyl curvature, no gravitational waves, no black-hole exteriors. The local scale factor is not the route to general relativity. Nor is it the same object as the metric: $c$ is the Maxwell speed of a medium, and the standard effective metric of a dielectric is a metric for light, not for free fall.

A general curved metric can be carried, by a frame field $\tilde{E}_\mu(x) \in \mathbb{M}_-$ with $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle$, since any Lorentzian metric has a local orthonormal frame. The algebra then supplies the pointwise $SL(2,\mathbb{C})$, its vector representation, and its Lie algebra; the sixteen frame functions modulo six local rotor parameters reproduce the ten components of the metric; and a frame that is pure rotor gauge is flat, so curvature is exactly the non-gauge part of the frame. The algebra can even carry the connection and its curvature, since the Lie algebra is the six-dimensional traceless subspace of $\mathbb{B}$ — with the caveat that the infinitesimal action is the two-sided $G\tilde{Q} + \tilde{Q}G^{*}$, not the commutator, the two differing precisely for the boosts.

The Dirac field lives on a different module from the four-vector, and its curved equation has a different derivative. The spinor module carries the **left** action $\psi \mapsto \tilde\Lambda\psi$, not the two-sided rotor conjugation, so its covariant derivative is the **one-sided** $D_\mu\psi = \partial_\mu\psi + \tilde\Gamma_\mu\psi$, with $\tilde\Gamma_\mu$ in the Lie subspace; covariance fixes the inhomogeneous transformation $\tilde\Gamma_\mu \mapsto \tilde\Lambda\tilde\Gamma_\mu\tilde\Lambda^{-1} - (\partial_\mu\tilde\Lambda)\tilde\Lambda^{-1}$. With the dual frame $\tilde E^\mu = g^{\mu\nu}\tilde E_\nu$ this gives the curved biquaternion Dirac operator $\tilde{\not D} = \tilde E^\mu D_\mu$, whose massless equation is $\tilde{\not D}\psi = 0$ and whose massive form is the same chiral pair as in the flat case, $\tilde{\not D}\tilde\Psi_R = m\tilde\Psi_L$, $\tilde{\not D}^{\natural}\tilde\Psi_L = m\tilde\Psi_R$, the mass being untouched by the curvature. The operator reduces exactly to $\tilde\nabla$ in a rigid frame with vanishing connection, and its square is the Lichnerowicz formula $\tilde{\not D}^2 = \Box_g - \tfrac14 R$, so the curvature couples to the field through the Ricci scalar even without a source. That much of the curved matter equation is now constructed in the framework's own notation. What remains is unchanged and unyielding: the frame and the connection are inserted by hand and satisfy no equation, the metric is not selected, the current that would source the coupled system is the spinor-module object carrying $\gamma^0$ outside $\mathbb{B}$, and the global existence of spinor fields is a topological condition no local operator can see.

What is missing is not a technical detail but the theory. Nothing determines the frame, the connection, or the metric; there is no action, no field equation, and no Einstein equation; the gravitating rank-2 tensors are not the framework's four-vectors; diffeomorphism invariance has no algebraic counterpart; global and topological structure is outside a pointwise algebra; and the informational sector's trace formula is a fibre trace with no measure and no integral, so its curved-space extension is not merely unwritten but unlocated. The framework contains the kinematical fibre of tetrad gravity and none of its dynamics; the title names a framework, and that is exactly what it is.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian (informational) and anti-Hermitian (material) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, home of the rotation rotors |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\langle \tilde{Q},\tilde{P}\rangle = \mathrm{Sc}(\tilde{Q}\tilde{P}^{\natural})$ | Bilinear (polar) form on $\mathbb{M}_-$; the pointwise metric |
| $\tilde{\Lambda} \in SL(2,\mathbb{C})$ | Unit-norm biquaternion (Lorentz rotor) |
| $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ | Rotor conjugation (four-vector action) |
| $\mathrm{Ad} : SL(2,\mathbb{C}) \to SO^+(1,3)$ | Two-to-one covering homomorphism, kernel $\{\pm e_0\}$ |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $ict$ | Local imaginary time coordinate, material sector |
| $\tilde{\nabla} = e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ | Biquaternionic gradient (needs a global chart) |
| $\tilde{E}_\mu(x) \in \mathbb{M}_-$ | Frame field (tetrad): $d\tilde{Q} = \tilde{E}_\mu dx^\mu$ |
| $g_{\mu\nu} = \langle \tilde{E}_\mu,\tilde{E}_\nu\rangle$ | Metric carried by the frame field |
| $J_k = e_k$, $K_k = ie_k$ | Rotation and boost generators, spanning $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}} \subset \mathbb{B}$ |
| $\tilde{\Gamma}_\mu$ | Connection 1-form, valued in the Lie subspace |
| $D_\mu\tilde{Q} = \partial_\mu\tilde{Q} + \tilde{\Gamma}_\mu\tilde{Q} + \tilde{Q}\tilde{\Gamma}_\mu^{*}$ | Covariant derivative on $\mathbb{M}_-$ (two-sided) |
| $\tilde E^\mu = g^{\mu\nu}\tilde E_\nu$, $\langle \tilde E^\mu, \tilde E_\nu\rangle = \delta^\mu{}_\nu$ | Dual frame (inverse tetrad) |
| $D_\mu\psi = \partial_\mu\psi + \tilde\Gamma_\mu\psi$ | Covariant derivative on the spinor module (one-sided, left action) |
| $\tilde{\not D} = \tilde E^\mu D_\mu$ | Curved biquaternion Dirac operator |
| $\tilde{\not D}^2 = \Box_g - \tfrac14 R$ | Lichnerowicz square; $\Box_g$ Laplace–Beltrami on spinors, $R$ Ricci scalar |
| $u = c$, $f = c^2$ | Local scale factor and its square, in the local-scale route |
| $R_{00}=u\Delta u$, $R_{0i}=0$, $R_{ij}=-\partial_i\partial_j u/u$ | Ricci tensor of $g=\mathrm{diag}(-c^2,1,1,1)$, corpus convention |
| $(m,n)$, $\left(\tfrac12,\tfrac12\right)$, $\left(1,1\right)\oplus\left(0,0\right)$ | Lorentz representations: four-vectors; symmetric rank-2 tensors |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule), pointwise only |

## Further Reading

- Charles W. Misner, Kip S. Thorne, and John A. Wheeler, *Gravitation* (Freeman, 1973), for the tetrad formalism and the distinction between coordinate and orthonormal frames in general relativity.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the metric, the curvature tensors, and the spinor formulation of curved spacetime.
- A. Lichnerowicz, "Spineurs harmoniques," *Comptes Rendus de l'Académie des Sciences* **257** (1963) 7–9, for the square of the Dirac operator and the $\tfrac14 R$ curvature term.
- J. Fredsted, "Obtaining consistent Lorentz gauging for a gravitationally coupled fermion," arXiv:1906.12200v3 [physics.gen-ph] (2019), for the external construction recorded in *Lorentz Gauging and the Euler–Lagrange Variation*: the non-commutativity of Lorentz gauging with the Euler–Lagrange variation in the standard vierbein coupling of a Dirac fermion to gravity; the world-index formalism — the frame fields $n^\mu$ and $n^\mu{}_i$, the matrices $M_\mu$ and $N_i$ with their Dirac-like algebra, and the covariant derivative carrying the explicit Levi-Civita connection — in which the two procedures commute; and the geometry of that formalism, in which the frame is covariantly constant, the connection is thereby solved in terms of the metric, its curvature is minus the Riemann tensor, and the gravitational action remains the Einstein–Hilbert one. Cited as an external claim; the source's equations were recomputed here, and the formalism is not adopted.
- J. Fredsted, "Spinor fields without Lorentz frames in curved spacetime using complexified quaternions," arXiv:0811.1357v4 [math-ph] (2009), for the external construction recorded in *An External Claim That the Bundle Basis Is Biquaternionic*: a coordinate-covariant and locally Lorentz invariant formalism in which the basis $s_\mu \in (\mathbb{C}\otimes\mathbb{H})_-$ is biquaternionic, the metric is the polar form $g_{\mu\nu} = \langle s_\mu, s_\nu\rangle$, and a single algebra-valued connection $\omega_\mu$ carries both the local $U(1)$ freedom and the Lorentz freedom. Cited as an external construction that reproduces the frame route of this article in the source's notation; the corpus does not adopt it.
- L. Parker and D. Toms, *Quantum Field Theory in Curved Spacetime: Quantized Fields and Gravity* (Cambridge, 2009), for the spinor covariant derivative, the Dirac equation on a curved background and its squared Klein–Gordon form.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984) and Vol. 2 (Cambridge, 1986), for the two-spinor calculus and the tetrad and spin-connection formalism in Lorentzian signature.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for spin structures on manifolds and the topological obstruction to spinor fields.
- W. Gordon, "Zur Lichtfortpflanzung nach der Relativitätstheorie," *Annalen der Physik* **72** (1923) 421–456, for the effective metric of a dielectric medium.
- Ulf Leonhardt and Thomas G. Philbin, "General relativity in electrical engineering," *New Journal of Physics* **8** (2006) 247, for the modern transformation-optics reading of a medium's effective geometry.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 18 and 33, for the complex structure of spacetime and for the spinorial formulation of curved geometry.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic treatment of gravity in the same rotor language used here.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a related biquaternionic approach to complexified geometry and its limits.
- A. Waser, "Biquaternion Relativity — Gravitation as an Effect of Spatial Varying Speed of Light" (self-issued, issued 1 January 2011, 8 pp.), for the instance of a spatially stretched varying-$c$ metric recorded in *What the Restricted Class Cannot Do*: the profile fitted to Newton's law, the Schwarzschild line element obtained from its first-order truncation, and the programme's claims (the equation of motion with perihelion precession, the gravitational redshift, free transverse gravitation waves, and the screened field of a point charge). A self-issued preprint with no journal, DOI or arXiv identifier; cited for the construction and its own claims, with its curvature recomputed here so that the truncated profile and the profile the author derives are distinguished.
- C. Castro and M. Pavšič, "The Extended Relativity Theory in Clifford Spaces" (review, 8 July 2004), for the arena alternative of the section *The Arena Alternative: Algebra Valued Coordinates*: Clifford-valued coordinates, the generalized interval, the polyvector bosonic $p$-brane action, the relativity of signature, and the maximal-acceleration programme.
- E. P. J. de Haas, "Biquaternion Formulation of Relativistic Tensor Dynamics," arXiv:1401.4470v1 [physics.gen-ph] (2013), for the external claim recorded in *An External Claim of One Tensor Language, and What It Does Not Supply*: one biquaternion tensor calculus carrying both the antisymmetric tensor dynamics of electrodynamics and the symmetric tensor dynamics of relativity. Cited as a representational result, with no field equation for the frame or the connection.
- D. J. Cirilo-Lombardo, "Algebraic structures, physics and geometry from a Unified Field Theoretical framework," arXiv:1411.5493v3 [hep-th] (2015), for the external claim recorded in *An External Claim That the Bundle Basis Is Biquaternionic*: the principal fibre bundle $P(G,M)$ whose basis is biquaternionic, its structural group and its three fundamental tensors, and the dictionary that carries its $2\times2$ matrix $Q$ to the corpus's biquaternion. Cited for the claim that the basis is biquaternionic and for its translation; the bundle's geometry — the G-structure, the reduced tangent bundle, the torsion-induced signature — is recorded as a claim in *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda*, and the source's invariant-metric assertion is not reproduced.
