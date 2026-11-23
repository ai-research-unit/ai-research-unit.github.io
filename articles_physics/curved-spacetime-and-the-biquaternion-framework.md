# __Curved Spacetime and the Biquaternion Framework__

## Introduction

Every result in the read-list articles is a statement about one fixed algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, evaluated at one point. The biquaternion norm, $SU(2)$, the rotor conjugation, the light cone as the zero-divisor set, the decomposition $\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi}$ — all of them are pointwise and flat. The wave equations written with them presuppose a global coordinate system $(i r'_t,\,r_x,\,r_y,\,r_z)$ carrying a distinguished imaginary time.

This article is about what happens when the spacetime in which those equations are written is curved. It is not a report of a finished construction. Its subject is a boundary: what the flat machinery extends to, what a curved metric can be made to do inside the algebra, and where the programme stops.

Three claims organise the discussion, and they are worth stating at the outset, because the prose of the framework elsewhere can suggest more than has been built.

**First, curvature cannot reside in the algebra.** The algebra is the same at every point and its biquaternion norm has constant coefficients. Curvature can therefore be carried only by the field that attaches the algebra to the manifold, not by the algebra itself. The question "what is curved spacetime in the biquaternion framework?" is a question about a field of frames, not about $\mathbb{B}$.

**Second, the framework's own local device does not reach general relativity.** That device is the local scale factor $c = 1/\sqrt{\epsilon\mu}$ of the imaginary time axis. Read as a map of points it produces no curvature at all, because the resulting line element is the flat form of $\mathbb{B}_{\Phi}$ written in curvilinear coordinates; read as a derivative rule it produces a genuinely curved metric, but of a class so rigid that within it Ricci-flatness forces flatness. The two interpretations are inequivalent, and the framework's prose does not choose between them.

**Third, a general curved metric can be carried, but only by inserting a frame field (a tetrad).** The algebra then supplies the local Lorentz group at every point, and can even supply the connection and its curvature as elements of its own Lie subspace; it supplies nothing that determines them. Any four-dimensional real vector space with a form of inertia $(3,1)$ would do the same work at each point, so nothing distinctive about $\mathbb{B}$ is put to the test along this route.

One family of frames deserves separate mention, because it is the one in which the algebra contributes more than a bilinear form. The Kerr–Schild metrics are the orbit of the flat form under a shear along a null direction, and the shear's generator is square-zero for the reason the corpus already owns: a null direction is a zero divisor. That single vanishing square is what makes the Kerr–Schild deformation affine in its scalar function, unimodular and invertible in closed form, what keeps its null direction fixed and therefore null, and why the class contains a vacuum plane-fronted wave while the local-scale class contains none. It supplies no dynamics either.

The article closes by separating what has been constructed from what remains unbuilt. The separation is stark: the kinematical fibre of tetrad gravity is present, its dynamics is absent, and the informational sector $\mathbb{B}_{\Psi}$ has no curved-space treatment at all.

The conventions are inherited from the read-list articles and none is redefined. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\imath^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$, and scalar imaginary $i$, with $i^2=-1$, commuting with the quaternion units. The anti-Hermitian and Hermitian subspaces are $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$, the real-quaternion subspace is $\mathbb{B}_{H}$, and the biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$. $SU(2)$ is $\{\tilde U : \tilde U\tilde U^{\natural} = e_t\} \cong SL(2,\mathbb{C})$, acting on $\mathbb{B}_{\Phi}$ by rotor conjugation $\tilde{Q} \mapsto \tilde U\tilde{Q}\tilde U^{*}$, with covering homomorphism $\mathrm{Ad}$ onto $SO^+(1,3)$ and kernel $\{\pm e_t\}$. For two observables of the informational sector the plain form is $\langle\tilde{H}_{\Psi,1},\tilde{H}_{\Psi,2}\rangle=\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2})$, read as the bilinear pairing $2\,\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum speed.

Two conventions govern the indices, and they are stated once. Every spacetime index is low. A repeated Greek label is a sum. The signs of the interval are written, not implied: the one minus of the material sector is the square of the $i$ in $Q_t=i q'_t$, made once on the time slot. Where the old pair was a contraction — one index up and one down — it is written as a plain sum over the four $Q_{\imath}$, whose only coefficient is the unit metric $\delta_{\imath\jmath}=(1,1,1,1)$; where the object was defined by lowering, the dynamical $g_{\imath\jmath}$ of the frame field stays inside it, as in the dual frame $\tilde F_{\imath} = g_{\imath\jmath}\tilde E_{\Phi,\jmath}$ and the inverse vierbein $e_{\imath a}$. The one exception is the external arena: $\epsilon_{\imath}$ with $\epsilon_0=1$, $\epsilon_\imath=-1$ is the C-space interval of the review, whose signs $(+,-,-,-)$ are that source's own and are stated where it is used. Where the old pair was a pairing and not a metric contraction — a coordinate differential against a derivative or a frame, as in $\tilde E_{\Phi,\imath} dx_{\imath}$, $\partial/\partial x_{\imath}$, and $F_{\mathrm{inf},\imath}\partial/\partial x_{\imath}$ — the sum is plain and no sign vector appears. Latin labels $a,b,c,d$ and $i,j,k$ are frame labels, not spacetime indices: they are never lowered by $g$, and, like every other component, they are written low; a frame slot is never raised. Where slots of different kinds meet the order is fixed: in $e_{\imath a}$ the world slot comes first and the frame slot second; in $\omega_{\imath ba}$ the world slot, then the frame row, then the frame column; in $S_{\alpha\beta\imath\jmath}$ the generator pair, then the row and the column. A dual basis is written with a different letter, never by raising: $\varsigma_{\imath}$ is dual to $s_{\imath}$, and $\tilde F_{\imath}$ is dual to $\tilde E_{\Phi,\imath}$.

## What the Flat Machinery Assumes

The pointwise metric of the framework is the polar form of the biquaternion norm. For $\tilde R_{\Phi,1} = i r'_{1t}\,e_t + \vec r_{\Phi,1}$ and $\tilde R_{\Phi,2} = i r'_{2t}\,e_t + \vec r_{\Phi,2}$ in $\mathbb{B}_{\Phi}$,

$$
\tfrac{1}{2}\left(\tilde{Q}_1\tilde{Q}_2^{\natural} + \tilde{Q}_2\tilde{Q}_1^{\natural}\right)
= \mathrm{Sc}\left(\tilde{Q}_1\tilde{Q}_2^{\natural}\right)
= -r'_{1t}r'_{2t} + \vec r_{\Phi,1}\cdot\vec r_{\Phi,2},
$$

a real scalar. Write $\langle \tilde{Q}_1, \tilde{Q}_2\rangle_{\natural}$ for this form; the units are $e_t, \vec e_x, \vec e_y, \vec e_z$ and the natural form on them is the unit metric $\delta_{\imath\jmath}=(1,1,1,1)$, so on the material sector, where $Q_t=i q'_t$, it is the Minkowski inner product of $\mathbb{B}_{\Phi} \cong \mathbb{R}^{1,3}$, its one minus the square of the $i$ in $Q_t$. It is preserved by rotor conjugation,

$$
\langle \tilde U\tilde{Q}_1\tilde U^{*},\ \tilde U\tilde{Q}_2\tilde U^{*} \rangle = \langle \tilde{Q}_1, \tilde{Q}_2\rangle_{\natural},
$$

because the biquaternion norm is invariant and the conjugation action is linear in each argument. This is the entire metric content of the flat framework: one fixed form on one fixed real vector space.

Four assumptions are built into that statement, and each is a flat-space assumption.

**1. One algebra, at one point.** The framework has no notion of two points. The four-position $\tilde R_\Phi$, the four-velocity $\tilde{V}_{\Phi}$, and every other four-vector are elements of $\mathbb{B}_{\Phi}$; separation between events enters only as a difference $\tilde{Q}_1 - \tilde{Q}_2$, never as a displacement along a path.

**2. A biquaternion norm with constant coefficients.** The form $\langle \cdot,\cdot \rangle_{\natural}$ is the same at every point, by construction. Nothing in the algebra can vary it.

**3. A global chart with a distinguished time axis.** The biquaternionic gradient

$$
\tilde\nabla_\Phi = e_t\,\partial/\partial R_t + \vec e_x\,\partial/\partial R_x + \vec e_y\,\partial/\partial R_y + \vec e_z\,\partial/\partial R_z
$$

requires four global coordinates, and requires in addition that the time direction be the coefficient of $e_t$ — that is, a preferred split of the coordinates into a time function and three spatial functions. The Maxwell and Dirac equations of the companion articles are written with this operator and inherit the requirement.

**4. A global symmetry group.** $SU(2)$ is the group of invertibles of a fixed algebra. It is a global object. A curved manifold has no global group of that kind acting on it; what it has is a pointwise copy of the group at each point, if the frame is chosen.

The framework is not silent about these limitations. *Introduction to the Biquaternion Universe* lists the extension to curved spacetime as an open question; *Why Complexify Spacetime?* observes that the $i r'_t$ convention "is tied to the existence of a global inertial frame"; and *Electromagnetism in Media — The Local Complex Structure at Work* states the position precisely: the algebra is "fixed while its embedding in physical spacetime is not." That last clause is the one this article takes seriously, because an embedding that varies from point to point is exactly where curvature would have to live.

## Curvature Cannot Be Carried by the Algebra

An algebra has no points, so it cannot have a curvature. The statement is worth making concrete rather than rhetorical. The biquaternion norm on $\mathbb{B}$ is a quadratic form with constant coefficients in a fixed basis; the only freedom in writing it is a change of basis, that is, a linear transformation, and a linear transformation maps a flat form to a flat form. There is no parameter in $\mathbb{B}$ that a field could modulate and no way to make the coefficient of the time direction a function of position. If one wants curvature in this framework, one must supply it in the map that attaches $\mathbb{B}$ to spacetime.

Two forms of that map are available, and they are the two routes examined below:

- a **scale** on the imaginary time axis, $i r'_t \mapsto i\,c(x)\,r'_t$, which is the framework's own local complex structure; and
- a **frame**, $dx_{\imath} \mapsto \tilde{E}_{\Phi,\imath}(x)\,dx_{\imath}$, which is the tetrad of the orthonormal-frame formulation of general relativity.

They are different devices, and it is a mistake to treat them as the same one. The first makes a piece of the embedding's scale local while leaving the frame rigid; the second makes the frame local while leaving every scale to the frame itself. The first is the framework's proposal and yields too little to be general relativity; the second yields everything kinematically and is no longer specifically biquaternionic.

A second structural point belongs here. General relativity's defining symmetry is diffeomorphism invariance: the theory is formulated on a manifold whose points carry no labels, and the group $\mathrm{Diff}(M)$ acts on those points. The algebra $\mathbb{B}$ has no representation of $\mathrm{Diff}(M)$ and nothing in it corresponds to a coordinate change on the base. Its algebraic symmetries are the pointwise $SL(2,\mathbb{C})$ — a redundancy in the description of a frame, not a symmetry of the manifold — together with the isometries of whatever background is chosen. This is a gap of a different kind from the absence of dynamics: a biquaternion formulation of gravitation in the strict sense would have to relate $\mathbb{B}$ to diffeomorphism invariance, and no such relation has been constructed.

Finally, a piece of representation-theoretic bookkeeping locates where the work would be. Under the Lorentz group the metric and the energy–momentum tensor are symmetric rank-2 objects, $\left(1,1\right)\oplus\left(0,0\right)$ in the $(m,n)$ labelling of the read list, of dimensions $9 + 1 = 10$. The kinematical fields the framework is built from are four-vectors, $\left(\tfrac12,\tfrac12\right)$, of dimension $4$, and they lie in $\mathbb{B}_{\Phi}$. The companion article on the material space already records that the field-strength biquaternion and the energy–momentum biquaternion are not four-vectors and do not lie in $\mathbb{B}_{\Phi}$. So the objects that would have to become dynamical fields in a theory of gravity are not the objects the framework is organised around. This is bookkeeping rather than impossibility, but it is where the missing formalism would have to be built.

## Route One: The Local Scale Factor

The framework's own route to a local structure is the local complex structure. Its content is stated in *Introduction to the Biquaternion Universe* and developed in *Electromagnetism in Media — The Local Complex Structure at Work*. In a medium with permittivity $\epsilon$ and permeability $\mu$, the speed of light is $c = 1/\sqrt{\epsilon\mu}$, a property of the medium at each point. The material time coordinate is $i r'_t$, so the map from physical time to the imaginary scalar direction of $\mathbb{B}$ carries the factor $c$; the imaginary unit $i$ is fixed by the algebra and only the real scale attached to the imaginary axis is local. In the gradient, this means

$$
\partial/\partial R_t = -i\,\partial/\partial r'_t .
$$

The framework's phrasing is that the complex structure is local "in the same spirit as the metric in general relativity", and that the $i r'_t$ convention of Minkowski space is the vacuum limit $c \to c_0$ of a more general local structure.

It is at this point that a genuine ambiguity appears, and it should be stated before anything is computed from it.

### The Two Readings

**Reading A, the point map.** Take the four-position as the framework writes it, $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, with $r'_t$ the temporal length and $r'_t=c(\vec r)\,t'$ its relation to the clock. Then $c$ is a function of position and

$$
d(i r'_t) = i\,c\,dt' + i\,t'\,dc,
$$

so the displacement biquaternion is $d\tilde R_\Phi = i(c\,dt' + t'\,dc)e_t + d(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ — still an element of $\mathbb{B}_{\Phi}$ — and the interval is $ds^2 = \langle d\tilde R_\Phi\rangle_{\natural}$, whose time sign comes from $i^2=-1$ and nothing else,

$$
ds^2 = -c^2\,d{t'}^2 - 2c\,t'\,dt'\,dc - {t'}^2 (dc)^2 + dr_x^2+dr_y^2+dr_z^2,
$$
$$
dc=\sum_i\frac{\partial c}{\partial x_i}\,dx_i,
\qquad
ds^2 = -c^2\,d{t'}^2 - 2c\,t'\,dt'\sum_i\frac{\partial c}{\partial x_i}\,dx_i
- {t'}^2\Bigl(\sum_i\frac{\partial c}{\partial x_i}\,dx_i\Bigr)^2
+ dr_x^2+dr_y^2+dr_z^2 ,
$$

with $i$ running over $x,y,z$ and with $c$ independent of $t'$; a time-dependent $c$ replaces $c$ by $c+t'\,\partial c/\partial t'$ in the $e_t$ coefficient and in $\det g$. The metric so obtained is nondegenerate — $\det g = -c^2$ in the coordinates $(t',r_x,r_y,r_z)$ — but it is **flat**, because it is nothing but the unit form of the algebra: the first three terms are $-d(c\,t')^2=-d{r'_{t}}^2$, so the display collapses to $-d{r'_{t}}^2+dr_x^2+dr_y^2+dr_z^2$, and $\langle d\tilde R_\Phi\rangle_{\natural}$ is exactly that. The map $(t', r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) \mapsto (r'_t,\vec r)=(c(\vec r)\,t',\vec r)$, followed by $\tilde R_\Phi=i r'_t\,e_t+\vec r$, is a diffeomorphism of $\mathbb{R}^4$ (its Jacobian determinant is $c > 0$), and it is pulling back the flat form of $\mathbb{B}_{\Phi}$; a pullback of a flat form along a diffeomorphism is flat, and no curvature can be produced by reparametrising a flat space. Direct computation confirms it: for $c = 1 + \tfrac{1}{10}(r_x^2+r_y^2+r_z^2)$ and, on a second and independent case, for $c = 2 + \sin x\,\cos y$, every component of the Riemann tensor vanishes. The local conversion, read as a map of points, changes the coordinate description of flat spacetime and nothing else.

**Reading B, the derivative rule.** Take instead the reading in which $c$ is a coefficient of the interval and not a definition of the coordinate. The operator is $\partial/\partial R_t = -i\,\partial/\partial r'_t = -(i/c)\,\partial/\partial t'$, and $c$ is held fixed in the differential, $d(i r'_t) = i\,c\,dt'$, the $dc$ term being dropped. Then

$$
ds^2 = -c(r_x,r_y,r_z)^2\,d{t'}^2 +dr_x^2+dr_y^2+dr_z^2,
$$

and this interval is genuinely curved whenever $c$ is not affine in the spatial coordinates. Its coefficient tuple in the coordinates $(t',r_x,r_y,r_z)$ is $(-c^2,1,1,1)$, and that tuple is the weight of one interval read in those coordinates, not a second metric: the metric of the series is the unit metric $\delta_{\imath\jmath}=(1,1,1,1)$ on the four $Q_{\imath}$, and the sign in front of $d{t'}^2$ is the square of the $i$ in $Q_t=i q'_t$, carried through the change of coordinate.

The two interpretations differ exactly by the terms containing $dc$, and they are not equivalent: one is flat and the other is not. Neither *Introduction to the Biquaternion Universe* nor *Electromagnetism in Media — The Local Complex Structure at Work* chooses between them, because the statements about the local $c$ are made at the level of the operator while the statements about the four-position are made at the level of the point. A reader can reasonably take either. This is left open here rather than resolved, because resolving it is a decision about what the framework means and not a computation.

### What the Restricted Class Cannot Do

Suppose Reading B is intended. Its curvature can be computed in closed form. The components below are quoted in the corpus's curvature convention — the convention of *Curvature and Geodesics*, in which $R(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$ and the unit two-sphere has positive scalar curvature, and the convention of the linearized-gravity, gravitational-wave and graviton-quantization articles. Writing $u = c = 1/\sqrt{\epsilon\mu}$ and allowing $u$ to depend on time as well as position,

$$
\mathrm{Ric}_{00} = u\,\Delta_\Phi u, \qquad \mathrm{Ric}_{0i} = 0, \qquad \mathrm{Ric}_{ij} = -\frac{\partial^2 u/\partial x_i\partial x_j}{u},
$$

where $\Delta_\Phi$ is the three-dimensional Laplacian and the indices $i,j$ run over the spatial directions. Equivalently, with $w = c^2$, $\mathrm{Ric}_{00} = \left(2w\,\Delta_\Phi w - |\vec\nabla_\Phi w|^2\right)/(4w)$ and $\mathrm{Ric}_{ij} = \left(-2w\,\partial^2 w/\partial x_i\partial x_j + (\partial w/\partial x_i)(\partial w/\partial x_j)\right)/(4w^2)$. For example $c = 2 + \sin x$ gives scalar curvature

$$
\mathrm{Ric} = \frac{2\sin x}{2 + \sin x},
$$

which is $+\tfrac{2}{3}$ at $x = \pi/2$ and vanishes at $x = 0$ and $x = \pi$.

The class is narrow in a way that is easy to state: one free function of the spatial coordinates (or of time as well), no shift vector, and a flat three-metric on the spatial slices, $g_{ij} = \delta_{ij}$. It is the diagonal, spatially rigid sub-case of the frame route of the next section.

Its decisive limitation is the following. Within this class, **Ricci-flatness forces flatness.** The condition $\mathrm{Ric}_{ij} = 0$ requires $\partial^2 u/\partial x_i\partial x_j = 0$ for every pair of spatial indices, so $u = \vec a(r'_t)\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) + b(r'_t)$ is affine in the spatial coordinates; then $\mathrm{Ric}_{00} = u\,\Delta_\Phi u$ vanishes automatically, so this is the whole Ricci-flat family. And every member of that family is flat: for $u = \vec a(r'_t)\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) + b(r'_t)$ with arbitrary functions $\vec a(r'_t)$ and $b(r'_t)$, the Riemann tensor vanishes identically, as direct symbolic computation of the general case confirms. The family is the algebra's way of writing a uniformly accelerated (Rindler-type) frame, and it is a reparametrisation of Minkowski space.

The consequence is worth stating plainly, in the restricted sense in which it holds. A metric that the local-scale route can write down at all cannot be a non-flat Ricci-flat spacetime. It therefore cannot carry a vacuum gravitational field with Weyl curvature, and so it cannot carry a vacuum gravitational wave or a vacuum black-hole exterior. This is a statement about a metric class, not a theorem about the biquaternion programme — but it is enough to show that the local scale factor of the imaginary time axis is not the route by which general relativity will enter the framework.

The wave and black-hole consequences of that boundary are the subject of two articles rather than of this one: [Gravitational Waves in Biquaternionic Form](gravitational-waves-in-biquaternionic-form.html) for what the framework does with a wave once a source is supplied, and [Black Hole Thermodynamics in Biquaternionic Form](black-hole-thermodynamics-in-biquaternionic-form.html) for the horizon thermodynamics the local-scale route cannot carry. Both work in the frame route, which is where the vacuum sector lives.

There is a further conceptual gap along this route, independent of the calculation. The $c$ in $1/\sqrt{\epsilon\mu}$ is the speed of light in a material medium — a property of a dielectric, measurable with a capacitor and a magnet. The standard effective-geometry literature (Gordon's metric and its modern descendants in transformation optics) already attaches a metric to a dielectric medium, and that metric is a metric for *light*: it reproduces the ray trajectories of Maxwell's equations in the medium, not the free-fall trajectories of test masses. Identifying the medium's effective metric with the spacetime metric is a further step, and the framework's "in the same spirit as the metric in general relativity" is an analogy rather than that step. Nothing in the framework supplies it.

**A wider class exists, and vacuum depends on the spatial leg.** The class above is what one free function writes by itself, but a frame field is not confined to it: allowing the radial leg of the frame to vary along with the time leg widens the class, and a spatially stretched $c$-metric is its natural member. An external programme takes exactly that step. A. Waser reads gravitation as the effect of a spatially varying speed of light and fixes the profile by its own force law: setting $F_g=-mc\,\vec\nabla_\Phi c=-m\nabla(c^2/2)$ equal to Newton's $-GMm/r^2$ gives the profile, and the model then works with the line element,

$$
c=c_0 f(r),\qquad f(r)=\exp(-r_s/(2r)),\qquad r_s=\frac{2GM}{c_0^2},
$$

$$
ds^2=-f(r)^2 c_0^2\,d{r'_{t}}^2+\frac{dr^2+r^2\,d\Omega^2}{f(r)^2}.
$$

The profile agrees with the local-scale route's $c^2=c_0^2(1-r_s/r)$ to first order in $r_s/r$, and the inverse squaring of the spatial part is a separate posit. At the profile the author actually derives, $f^2=\exp(-r_s/r)$, the computation returns a non-vanishing Ricci tensor, with

$$
\mathrm{Ric}_{00}=0,\qquad
\mathrm{Ric}_{11}=-\frac{r_s^2}{2r^4},\qquad
\mathrm{Ric}=-\frac{r_s^2\,e^{-r_s/r}}{2r^4},
$$

in the corpus's curvature convention, all three vanishing as $r\to\infty$. Truncated at first order, $f^2=1-r_s/r$, the line element is the isotropic weak-field form $ds^2=-(1-r_s/r)c_0^2d{r'_{t}}^2+(1+r_s/r)(dr^2+r^2d\Omega^2)$; that expansion **is** the Schwarzschild exterior to first order in $r_s/r$, and it is Ricci-flat to that order. The family's own line element with the truncated profile left unexpanded, $ds^2=-(1-r_s/r)c_0^2d{r'_{t}}^2+(dr^2+r^2d\Omega^2)/(1-r_s/r)$, is a different metric and is not Ricci-flat: it has $\mathrm{Ric}_{00}=-r_s^2/(2r^4)$ and $\mathrm{Ric}_{11}=-r_s^2/\bigl(r^2(r-r_s)^2\bigr)$. The classical tests the paper then computes are those of the first-order truncation.

The same computation settles what the instance can and cannot show. Within Waser's family, where the spatial part is forced to follow the time profile, the Ricci tensor has only two independent components,

$$
\mathrm{Ric}_{00}\propto rff''-r{f'}^2+2ff',\qquad
\mathrm{Ric}_{11}\propto rff''-3r{f'}^2+2ff',
$$

the other two follow from these, $\mathrm{Ric}_{22}=(r^2/f^4)\,\mathrm{Ric}_{00}$ and $\mathrm{Ric}_{33}=\sin^2\theta\,\mathrm{Ric}_{22}$, so $\mathrm{Ric}_{\imath\jmath}=0$ forces ${f'}^2=0$: the inverse-squared spatial part does not restore a non-flat vacuum member, it removes it. Free the radial leg instead, keeping the same profile $f^2=1-r_s/r$,

$$
ds^2=-f^2c_0^2\,d{r'_{t}}^2+\frac{dr^2}{f^2}+r^2\,d\Omega^2 ,
$$

and the line element is exactly the Schwarzschild exterior and exactly Ricci-flat. That contrast is the instance's real content. The metric class can hold a vacuum solution, but only as its two-function member, with the spatial leg chosen freely; the one-function member, in which the spatial leg follows the time leg, cannot. And in either case the profile is fixed by fitting Newton's law, not by the algebra. (The programme's one prediction not shared with general relativity is a screening of the static field, sized in *The Empirical Status of the Biquaternion Framework*.)

## Route Two: A Field of Frames

The general way to make the embedding of spacetime into the algebra local is to allow the coordinate differentials to be carried into $\mathbb{B}_{\Phi}$ by a point-dependent frame:

$$
d\tilde R_\Phi = \sum_{\imath} \tilde{E}_{\Phi,\imath}(x)\,dx_{\imath}, \qquad \tilde{E}_{\Phi,\imath}(x) \in \mathbb{B}_{\Phi} .
$$

The interval is $ds^2 = \langle d\tilde R_\Phi\rangle_{\natural}$, and since $\langle\cdot\rangle_{\natural}$ is the polar form evaluated on $d\tilde R_\Phi = \sum_{\imath}\tilde{E}_{\Phi,\imath} dx_{\imath}$,

$$
\boxed{\;g_{\imath\jmath}(x) = \langle \tilde{E}_{\Phi,\imath}(x), \tilde{E}_{\Phi,\jmath}(x)\rangle_{\natural}
= \mathrm{Sc}\left(\tilde{E}_{\Phi,\imath} \tilde{E}_{\Phi,\jmath}^{\natural}\right)\;}.
$$

Four $\mathbb{B}_{\Phi}$-valued fields, so sixteen functions. Where they are linearly independent, the Gram matrix is nondegenerate, and by Sylvester's law it has inertia $(3,1)$: the result is automatically a Lorentzian metric. Conversely, any Lorentzian metric can be written this way locally. Choose a $g$-orthonormal frame, map it into $\mathbb{B}_{\Phi}$ by a linear isometry of quadratic spaces — which exists because both forms have inertia $(3,1)$ — and read off the coordinate components. So there is no obstruction: **the framework can carry any curved metric.**

What makes the route more than a change of notation is the local symmetry. If $\tilde U(x)$ is a unit-norm biquaternion depending on position, then

$$
\tilde{E}_{\Phi,\imath} \longmapsto \tilde U\tilde{E}_{\Phi,\imath}\tilde U^{*}
$$

leaves $g_{\imath\jmath}$ unchanged at every point, because rotor conjugation preserves the bilinear form. So the local gauge group supplied by the algebra is exactly a copy of $SL(2,\mathbb{C})$ at each point, with the double cover, the Lie algebra, and the $\left(m,n\right)$ representation theory of the read list applying pointwise. This is the standard tetrad or vierbein structure of the orthonormal-frame formulation of general relativity, written in the algebra's own notation; the interplay of the sixteen frame functions with the six local rotor parameters leaves $16 - 6 = 10$ independent components, which is the number of components of $g_{\imath\jmath}$.

The corresponding flatness statement is exact and instructive. If the frame is *pure rotor gauge*, $\tilde{E}_{\Phi,\imath} = \tilde U(x)\,u_{\imath}\,\tilde U(x)^{*}$ for a fixed basis $u_{\imath}$ of $\mathbb{B}_{\Phi}$, then $g_{\imath\jmath}(x) = \langle u_{\imath}, u_{\jmath}\rangle_{\natural}$ is a constant matrix, and the metric is flat. A point-dependent rotor field applied to a rigid basis produces no curvature whatever. Curvature in this route is exactly that part of the frame which is not of this pure-gauge form, and no amount of rotor-field machinery detects it.

Two honest qualifications keep this from sounding like more than it is.

First, *carrying is not deriving*. The frame field is inserted by hand, and it is subject to no condition from the algebra. Every Lorentzian metric, including every vacuum spacetime, is representable; the framework excludes nothing. That is not a success but an emptiness: the entire content of the construction is the sixteen functions, and the algebra contributes only a fixed four-dimensional real vector space with a form of inertia $(3,1)$, which any such space would contribute equally. Beyond that one quadratic form, nothing that distinguishes $\mathbb{B}$ is used: writing $g_{\imath\jmath} = \langle \tilde{E}_{\Phi,\imath}, \tilde{E}_{\Phi,\jmath}\rangle_{\natural}$ calls on the biquaternion norm and on nothing else — not the quaternionic multiplication, not the two-sector decomposition, not the complex structure.

Second, *this route does not make the complex structure local*. The frame field is a real linear map at each point; the imaginary direction of $\mathbb{B}$ remains globally the coefficient of $e_t$ in a fixed basis. The framework's local complex structure and the tetrad's local frame are different devices, and neither contains the other: the frame route gives general relativity's kinematics and abandons the framework's own locality proposal, while the local-scale route keeps that proposal and cannot reach even a non-flat Ricci-flat vacuum. This tension is a finding of this article, not a problem it resolves. One thing the external record shows is that the frame **language**, rather than the algebra, is where the tension lives: a construction recorded below, under *An External Claim That the Bundle Basis Is Biquaternionic*, carries the same metric with no vierbein at all — the basis is four $\mathbb{B}_{\Phi}$-valued fields $s_{\imath}$ themselves — and derives its connection from a condition on the basis rather than inserting one.

## The Kerr–Schild Sub-class: the Frame Route's Reach

One family of frames deserves a paragraph here and a separate article, because it is the family in which the exact solutions the corpus's neighbouring articles work with are written, and because it is where the frame route reaches further than the local-scale route. It is the **Kerr–Schild form**,

$$
g_{\imath\jmath} = \delta_{\imath\jmath} + 2h\,\ell_{\imath} \ell_{\jmath},
\qquad
\sum_{\imath} \ell_{\imath}^2 = 0,
$$

with $\ell_{\imath}$ null and $h$ free. The family is the orbit of the flat form under a **shear along a null direction**, $T=\mathrm{id}+hN$ with $N(X)=\tilde{\mathcal L}_{\Phi,\mathrm{null}}\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural$; the shear's generator is square-zero because the null direction is a zero divisor, and the four properties usually listed one at a time for the class are that one vanishing read in four places. With a constant null direction and a varying profile the member is a plane-fronted vacuum wave, Ricci-flat exactly when the profile is harmonic in the two transverse coordinates.

That wave is the contrast with Route One in one object. Within the local-scale class Ricci-flatness forces flatness, so that route carries no vacuum gravitational wave; the frame route carries one, and this sub-class carries one in closed form. Nothing about the profile is derived, so the reach is a reach of carrying and not of content.

The construction, the four identities, the numerical checks and the complexified reading of the shear are the subject of [The Kerr–Schild Sub-class and the Vacuum Wave](the-kerr-schild-sub-class-and-the-vacuum-wave.html).

## Route Three: The Connection, and the Two-Sided Derivative

A frame field is not by itself a geometry; a manifold also needs a way to compare frames at neighbouring points, that is, a connection. Here the biquaternion algebra makes a genuine and positive contribution, and the contribution has a trap in it that is worth recording.

The positive part is dimensional. The Lie algebra of $SU(2)$ is the scalar-free part of $\mathbb{B}$,

$$
\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}
= \mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\} \oplus \mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}
= \left\{ G \in \mathbb{B} : G + G^{\natural} = 0 \right\},
$$

the elements with no scalar part, real or imaginary; six real dimensions, with the rotation generators $\vec e_\imath$ and the boost generators $B_{\mathrm{boost},k} = i\vec e_\imath$ of the read list. Since this Lie algebra is a subspace of $\mathbb{B}$, a connection 1-form and its curvature 2-form can both be carried as $\mathbb{B}$-valued objects — specifically, as objects valued in that six-dimensional subspace. The spin connection of the tetrad formalism is therefore not foreign to the algebra; it sits inside it.

**The compact half of that six-dimensional space is the corpus's non-abelian gauge factor, and this article accepts the identification.** The three rotation generators $\vec e_\imath$ span the compact part of the connection, and that span is the algebra $\mathfrak{su}(2)$ whose group is $\mathrm{Spin}(3)$ — the same factor that [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) calls the compact gauge algebra of the material sector, and whose adjoint is the vector part of $\mathbb{B}$. So the gauge field of that construction and the spatial part of the spin connection here are one object read twice: once as a Yang–Mills connection on a module and once as a connection on the frame bundle. [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) constructs it in the second reading, and [The $W$, $Z$ and $W_R$ Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html) shows that the self-couplings are the same vertices in both readings.

**What the identification costs, and what it does not buy.** It costs nothing, because the compact generators are already inside the six-dimensional subspace and the identification adds no structure. It does not buy an internal symmetry: the rotations do not commute with the boosts, so the factor is geometric and not internal, and the electroweak identification of the same algebra with weak isospin is a separate claim that this article does not make.

The trap concerns the covariant derivative. The group acts on the material sector by the two-sided formula $\tilde{Q} \mapsto \tilde U\tilde{Q}\tilde U^{*}$, so the infinitesimal action of a generator $G$ is

$$
\tilde{Q} \longmapsto \tilde{Q} + \epsilon\left(G\tilde{Q} + \tilde{Q}G^{*}\right) + O(\epsilon^2),
$$

which is **not** in general the commutator $[G,\tilde{Q}]$. The two agree exactly when $G^{*} = -G$, which is the case for the rotation generators $\vec e_\imath$; for the boost generators $i\vec e_\imath$, which are Hermitian, they do not agree. On $\tilde R_\Phi = i r'_t\,e_t + r_x\vec e_x + r_y\vec e_y + r_z\vec e_z$, the boost generator $G = i\vec e_x$ acts to first order as

$$
r'_t \longmapsto r'_t - 2\epsilon\,r_x, \qquad r_x \longmapsto r_x - 2\epsilon\,r'_t,
$$

mixing the time and $\vec e_x$ components as a boost must, whereas $[G,\tilde{Q}]$ is $2\epsilon(-i r_z\,\vec e_y + i r_y\,\vec e_z)$. Read on the basis, the commutator sends $\vec e_y\mapsto 2i\vec e_z$ and $\vec e_z\mapsto-2i\vec e_y$: the rotation of the $\vec e_y\vec e_z$ plane composed with multiplication by $i$, hence a boost-type element and not a rotation of the frame, and an element of $i\mathbb{B}_{\Phi}$ — so the abbreviated derivative does not even preserve the material sector. The two prescriptions differ by exactly the right action, $G\tilde{Q}+\tilde{Q}G^{*}=[G,\tilde{Q}]+2\tilde{Q}G$ when $G^{*}=G$, and they agree precisely when $G^{*}=-G$, which is the rotation case. A biquaternionic covariant derivative must therefore be written in the two-sided form

$$
\boxed{\;D_{\imath} \tilde{Q} = \partial/\partial x_{\imath} \tilde{Q} + \vec\Gamma_{\imath} \tilde{Q} + \tilde{Q}\vec\Gamma_{\imath}^{*}\;},
$$

with $\vec\Gamma_{\imath}$ in the Lie subspace; the natural abbreviation $D_{\imath} = \partial/\partial x_{\imath} + [\vec\Gamma_{\imath}, \cdot]$ would be wrong for exactly the boosts, which is where the Lorentzian content of the theory lives.

One object in this neighbourhood is automatic and one is not. The automatic one is the logarithmic derivative of a rotor field: if $\tilde U(x)$ is unit-norm, then both $\tilde U^{\natural}\,\partial/\partial x_{\imath}\,\tilde U$ and $\partial/\partial x_{\imath}\,\tilde U\,\tilde U^{\natural}$ are scalar-free, hence lie in the Lie algebra, because $\tilde U^{\natural}\tilde U = e_t$ differentiates to zero. So a frame carried by a rotor field arrives with a natural $\mathrm{SL}(2,\mathbb{C})$-valued connection. But it is pure gauge, and its curvature vanishes — which is the same statement as the flatness of the rotor-field metric in the previous section, arrived at from the other direction. Consistency, not new content.

What is not automatic is everything one would want. Metric compatibility and the vanishing of torsion are conditions, not consequences; nothing in the algebra selects the Levi-Civita lift. And the whole dynamics is absent: there is no action, no field equation for $\tilde{E}_{\Phi,\imath}$ or $\vec\Gamma_{\imath}$, and therefore no Einstein equation. The algebra can hold the objects of the spin-connection formalism in the same notation in which it holds the rotors and the four-vectors. It does not generate a single equation for them.

## The Arena Alternative: Algebra Valued Coordinates

The three routes above accept the article's premise and look for the map that attaches $\mathbb{B}$ to a manifold. There is a fourth position, and it is the only one that attacks the premise instead: **put the algebra in the coordinates**, so that the arena itself is not a manifold. It is worth naming here, because it is the sharpest existing answer to the sentence from which this article began — *the algebra has no points* — and because a reader who meets that sentence should know that the answer has been tried.

The construction is the review's *extended relativity in Clifford spaces* (Castro and Pavšič, 2004). The coordinates are themselves elements of an algebra; for a four-dimensional base one writes, in the reference-frame basis operators — with $L_a$ and $R_b$ the two multipliers, so that $L_aR_b$ is the basis operator $X\mapsto aXb$, and $\tfrac12[V_{\imath},V_{\jmath}]$ the bivector basis operator, where $V_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}$ and $V_\imath=iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}$ are the four frame basis operators —

$$
X = \sigma\,1 + \bigl(x_0\,iR_{\mathrm{axf},\vec e_x}-\sum_{\imath\in\{x,y,z\}} x_\imath\,iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}\bigr) + \tfrac12\sum_{\imath,\jmath} x_{\imath\jmath}[V_{\imath},V_{\jmath}] + \bigl(\check x_0\,iR_{\mathrm{axf},\vec e_x}-\sum_{\imath\in\{x,y,z\}} \check x_\imath\,iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}\bigr) + \check\sigma I ,
$$

with $I$ the pseudoscalar of the review's algebra, one coefficient for each grade — scalar, vector, bivector, pseudovector, pseudoscalar — so that a "point" carries a line, an area, a volume and a hyper-volume, and the arena is called a **C-space**. The invariant interval generalizes accordingly, $|dX|^2 = d\sigma^2 + \sum_{\imath}\epsilon_{\imath}\,dx_{\imath} dx_{\imath} + \tfrac12\sum_{\imath,\jmath}\epsilon_{\imath}\epsilon_{\jmath}\,dx_{\imath\jmath}dx_{\imath\jmath} - \sum_{\imath}\epsilon_{\imath}\,d\check x_{\imath} d\check x_{\imath} - d\check\sigma^2$, the signs of the last two terms being fixed by the square of the volume element, $I^2 = -1$ with the signs $(+,-,-,-)$; and the transformations that preserve it generalize the Lorentz transformations by mixing objects of different grade, so that a history of one dimension is reshuffled into a history of another.

The trade is exact, and it should be stated as a trade rather than as a solution. What the construction buys is the opposite of what this article has been recording: the extended objects — closed strings, membranes, $p$-branes — are not fields *on* the arena, they are among its coordinates, so a single action covers all $p$; and a fundamental length, the Planck scale, has a natural place to enter, as the parameter that bridges grades. What it costs is the manifold. The coordinates are **non-commuting** polyvectors, so there is no space of points, and distance, connection, dimension and even the sign of the interval have to be rebuilt — the review's own proposal is that the signs are relative to a chosen slice through C-space, which is a notion the corpus does not have and does not need (see the remark on the signs in *The Realification and the Effect of the Change of Scalars*). Two things must not be conflated: a C-space is an **algebra of coordinates**, while the corpus's $\mathbb{B}$ is an **algebra of fields and observables**; the corpus's algebra is the even part of $\mathrm{Cl}_{3,1}(\mathbb{C})$, and the review's arena is a manifold whose points are algebra elements.

The honest summary is that this is a different framework, not an extension of the one developed here, and that it does not fill this article's gap. The missing dynamics is missing in both: C-spaces supply a richer arena and a unified action for free extended objects, but the corpus's boundary — the biquaternion framework contains the kinematical fibre of tetrad gravity and none of its dynamics — is neither crossed nor refuted by moving the algebra into the coordinates. What the position does establish is that the sentence *the algebra has no points* is a statement about $\mathbb{B}$ as this framework uses it, not a theorem about algebras. The empirical status of the scale that C-spaces make natural is recorded in *The Empirical Status of the Biquaternion Framework*.

## The Biquaternion Dirac Equation on a Curved Background

The connection of the previous section was built for the material sector, where the field is a four-vector and the group acts by the two-sided rotor conjugation. The Dirac field is a different kind of object — an element $\tilde{Ξ}$ of $\mathbb{B}$, multiplied from the left by the group, not a four-vector acted on by rotor conjugation — and the difference in the kind of action is exactly what the curved Dirac equation turns on. This section writes that equation in the framework's own notation. It is the item the table below records as the curved-space form of the biquaternion Dirac equation.

**Frame note.** The operator below is built from the material frame $\tilde E_{\Phi,\imath}\in\mathbb{B}_{\Phi}$ of Route Two, indexed by the physical coordinates $x_{\imath}=(r'_t,r_x,r_y,r_z)$. The basis operator transcription uses the informational frame $F_{\mathrm{inf},\imath}$, built from $e_{\mathrm{inf},0}=e_t$ and $\vec e_{\mathrm{inf},k}=i\vec e_\imath$. The two frames are related but not interchangeable: the time leg of the material frame is $ie_t$, the time leg of the informational frame is $e_t$, and only the informational frame has legs that contract with the four frame basis operators weighted by $e_{\imath a}$. The relation is stated in the Lorentz-gauging section, and the two flat limits are computed below.

### The One-Sided Field Derivative

The Lorentz group acts on the field by **left multiplication**, $\tilde{Ξ} \mapsto \tilde U\tilde{Ξ}$, not by rotor conjugation; the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* establishes this, and it is the algebraic difference between a four-vector and the field. The covariant derivative compatible with that action is therefore **one-sided**,

$$
D_{\imath}\tilde{Ξ} = \partial/\partial x_{\imath}\,\tilde{Ξ} + \vec\Gamma_{\imath}\tilde{Ξ},
\qquad
\vec\Gamma_{\imath} \in \mathrm{SL}(2,\mathbb{C})_{\mathbb{R}} \subset \mathbb{B},
$$

which is not the two-sided prescription of the material sector, $D_{\imath}\tilde{Q} = \partial/\partial x_{\imath}\,\tilde{Q} + \vec\Gamma_{\imath}\tilde{Q} + \tilde{Q}\vec\Gamma_{\imath}^{*}$. The two must not be conflated. The vector carries the transformation twice, once on each side, $\tilde{Q} \mapsto \tilde U\tilde{Q}\tilde U^{*}$, and so receives two connection terms; the field carries it once, $\tilde{Ξ} \mapsto \tilde U\tilde{Ξ}$, and so receives one. Both connection terms live in the same six-dimensional Lie subspace, and each is the standard inhomogeneous connection of the object it acts on.

Covariance fixes the transformation law. If $\tilde{Ξ} \mapsto \tilde U\tilde{Ξ}$, then $D_{\imath}\tilde{Ξ} \mapsto \tilde U D_{\imath}\tilde{Ξ}$ precisely when the connection transforms as

$$
\vec\Gamma_{\imath} \longmapsto \tilde U\vec\Gamma_{\imath}\tilde U^{-1}
- \left(\partial/\partial x_{\imath}\,\tilde U\right)\tilde U^{-1},
$$

which is the inhomogeneous transformation expected of a connection on the field. A rotor field supplies an example at once: $\vec\Gamma_{\imath} = -\left(\partial/\partial x_{\imath}\,\tilde U\right)\tilde U^{-1}$ is pure gauge, and its curvature vanishes, exactly as the rotor-carried frame of the previous sections is pure gauge and flat.

### The Curved Dirac Operator and the Equation

The biquaternion gradient $\tilde\nabla_\Phi$ is the operator of *Operator and Calculus Conventions*, §*The Gradient*; read on the material sector in the physical coordinates $x_{\imath}=(r'_t,r_x,r_y,r_z)$, all four in metres, it is
$$
\tilde\nabla_\Phi = -i\,e_t\,\partial/\partial r'_t + \sum_{\imath\in\{x,y,z\}}\,\vec e_\imath\,\partial/\partial x_\imath,
$$
because $\partial/\partial r'_t=i\partial/\partial R_t$, and the two imaginary units multiply to a sign, $(-i)\cdot i=+1$. Its curved replacement substitutes the frame field for the **rigid material frame** and the one-sided derivative for the partial derivative. The rigid material frame is not the algebra basis $e_{\imath}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, which is not contained in $\mathbb{B}_{\Phi}$; it is
$$
\tilde E_{\Phi,0}=ie_t,\qquad \tilde E_{\Phi,k}=\vec e_\imath,
\qquad
\tilde F_0=-ie_t,\qquad \tilde F_\imath=\vec e_\imath,
$$
with $g_{\imath\jmath}$ the flat form, whose interval is $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$. The curved object is

$$
\tilde F_{\imath} D_{\imath},
\qquad
\tilde F_{\imath} = g_{\imath\jmath}\tilde E_{\Phi,\jmath},
\qquad
\langle \tilde F_{\imath}, \tilde E_{\Phi,\jmath}\rangle_{\natural} = \delta_{\imath\jmath},
$$

where $\tilde F_{\imath}$ is the **dual frame**, the inverse tetrad of the frame field $\tilde E_{\Phi,\imath}$ of Route Two. The operator is biquaternion-valued and first order, and it is the object the whole tetrad machinery was assembled to define.

**The massless member.** The massless equation is

$$
\tilde F_{\imath} D_{\imath}\tilde{Ξ} = 0,
$$

identical in form to the flat massless equation, the operator multiplying the field from the left like every other element of the algebra. Read as a basis operator — the operator acting on the algebra taken as a four-dimensional complex vector space — its representative is not the coefficient matrix of left multiplication by $\tilde F_{\imath}$: that matrix squares with a vector cross term left over. It is the sum $\sum_{\imath}\sum_a e_{\imath a}\,iL_{\mathrm{axf},e_a}R_{\mathrm{axf},\vec e_{\mathrm{spt}(a)}}\,D_{\imath}$ of the four frame basis operators of *Matrix Representations Conventions*, with $\mathrm{spt}(t)=x$ and $\mathrm{spt}(\eta)=y$, weighted by the inverse vierbein; the four basis operators close on the plain weight, $\{iL_{\mathrm{axf},e_a}R_{\mathrm{axf},\vec e_{\mathrm{spt}(a)}},iL_{\mathrm{axf},e_b}R_{\mathrm{axf},\vec e_{\mathrm{spt}(b)}}\}=2\varepsilon_a\delta_{ab}I_4$, and their square is the scalar operator below; in the rigid frame the sum is the flat operator built from the same four basis operators.

**The massive pair.** The massive equation is the chiral pair, for the two halves $\tilde{Ξ}_{R}$ and $\tilde{Ξ}_{L}$ of the Dirac field of the parent article. Its two lines are displayed separately because they are the two chiral halves of one field, not one equation written twice:

$$
\boxed{\;\tilde F_{\imath} D_{\imath}\tilde{Ξ}_{R} =2\pi\nu_m\tilde{Ξ}_{L}}
$$

$$
\boxed{\;(\tilde F_{\imath} D_{\imath})^{\natural}\tilde{Ξ}_{L} =2\pi\nu_m\tilde{Ξ}_{R}}
$$

where $(\tilde F_{\imath} D_{\imath})^{\natural}$ is the quaternion-conjugate operator: $\natural$ is an anti-automorphism, so it reverses the order of the factors, and the conjugate frame and the conjugate connection appear in the opposite order. It reduces to $(\tilde\nabla_\Phi)^{\natural}$ when the frame is rigid and the connection vanishes. The mass term is unchanged: it couples the two chiral parts and carries no field dependence, and the curvature enters only through the derivative. Here $\frac{1}{2\pi\nu_m}$ is the mass length.

**The one-sided pair and the two-sided equation.** The pair above is the corpus's **one-sided** formulation: the operator multiplies the field from the left, and the mass couples the two chiral parts $\tilde{Ξ}_{R}$ and $\tilde{Ξ}_{L}$, the two parts named by the subscript that *Special Element Conventions*, §*The Chirality Convention*, fixes. The **two-sided** equation is the Kravchenko form on $\mathbb{B}$, in which the derivative acts from the left and the mass term acts from the right through $\vec e_z$, the componentwise conjugation supplying the antilinear part; it is a change of representation, not a second law, and the parent article compares the two in *The One-Sided and the Two-Sided Equation*. The mass is **not** a right multiplication in the one-sided pair: a right multiplication acts within each chiral part, whereas the mass exchanges the two. The right multiplication appears in the two-sided dictionary, where it represents the same coupling. Only the one-sided pair is constructed here; the two-sided dictionary has not been extended to a curved background.

### Flat Limit and the Square

The **flat limit is exact.** With the rigid material frame $\tilde E_{\Phi,0}=ie_t$, $\tilde E_{\Phi,k}=\vec e_\imath$, the dual frame $\tilde F_0=-ie_t$, $\tilde F_\imath=\vec e_\imath$, the flat form $g_{\imath\jmath}$ and $\vec\Gamma_{\imath}=0$,

$$
\tilde F_{\imath}D_{\imath}=-i\,e_t\,\partial/\partial r'_t+\sum_{\imath\in\{x,y,z\}}\vec e_\imath\,\partial/\partial x_\imath=e_t\,\partial/\partial R_t+\sum_{\imath\in\{x,y,z\}}\vec e_\imath\,\partial/\partial R_\imath=\tilde\nabla_\Phi ,
$$

and the pair reduces to the flat pair. The rigid frame is **not** the algebra basis $e_{\imath}$: $e_t$ is not in $\mathbb{B}_\Phi$, and a term-by-term replacement of $\tilde E_{\Phi,\imath}$ by $e_{\imath}$ is invalid.

The **square** is the Lichnerowicz formula, and it is stated here for the basis operator — the operator acting on the algebra read as a four-dimensional complex vector space:

$$
\boxed{\;(\tilde F_{\imath}D_{\imath})^2=-\Box_{g,\Phi}+\tfrac14\mathrm{Ric}\;},
$$

with $\mathrm{Ric}$ the scalar curvature of the Gram metric and $\Box_{g,\Phi}=G_{\imath\jmath}\nabla_{\imath}\nabla_{\jmath}$ the Laplace–Beltrami operator on the field, so that $\vec\nabla_\Phi^{*}\vec\nabla_\Phi=-\Box_{g,\Phi}$ and the identity is the standard Lichnerowicz formula in Lorentzian signature. The algebra element itself does not square to a scalar; in the rigid frame $\tilde\nabla_\Phi^2$ carries the vector term $-2i\sum_{\imath\in\{x,y,z\}}\vec e_\imath\,\partial^2/\partial r'_t\partial x_\imath$. The sign is fixed by the flat limit, the coefficient by the Clifford contraction, and the derivation of both, together with the comparison against the derivation that never mentions the algebra, the Dirac–Kähler alternative and the informational sector's obstruction, is the subject of [The Curved Dirac Operator and Its Square](the-curved-dirac-operator-and-its-square.html).

### What This Does and Does Not Settle

It settles the ledger item that asked for the curved-space form of the biquaternion Dirac equation written in the framework's own notation. The operator $\tilde F_{\imath} D_{\imath}$, the one-sided derivative, the connection transformation, the massless equation and the massive chiral pair, the flat limit, and the Lichnerowicz square of the basis operator reading are now written, and every object in them — the frame, the dual frame, the connection, the one-sided derivative — is an object the algebra already carries. Two features separate the curved Dirac equation from the curved metric: the field's derivative is one-sided and its connection transformation inhomogeneous, while the frame's derivative is two-sided and its metric is bilinear in the frame; and the curvature couples to the field through $+\mathrm{Ric}/4$ even without a source, so the curved Dirac square is not the naive curved Klein–Gordon operator.

What it does not settle is everything the frame and the connection already failed to settle, and the Dirac equation is the most inviting place to overclaim, so the limits bear repeating. The equation contains the frame and the connection; it determines neither. Nothing in the algebra or in this equation fixes $\tilde E_{\Phi,\imath}$ or $\vec\Gamma_{\imath}$, selects the Levi-Civita lift rather than a torsionful one, or supplies an action for either; the Einstein equation is as absent here as it was in Route Three. The equation is the correct curved-space transcription of the matter equation **on a background** whose geometry is inserted by hand, and that is exactly what it is. On the matter side, the source of the equation — the conserved current — remains the object of the minimal-coupling and Gordon-decomposition articles, carrying the basis operator $iR_{\mathrm{axf},\vec e_x}$, which is an operator and not a product in $\mathbb{B}$; the closed sourced system, in which the Dirac current feeds the curved biquaternion Maxwell equation, is still unwritten. And the global question survives untouched: whether the field can exist on the manifold at all is the topological condition of Route Two's programme, and no local operator can answer it.

### Lorentz Gauging and the Euler–Lagrange Variation

The coupling written above is the standard one: the flat equation with the rigid material frame replaced by the frame and the partial derivative by the one-sided Lorentz-covariant derivative. An external source shows that this standard coupling carries an ambiguity the corpus has not recorded, and that the ambiguity sits exactly where the frame and the connection enter.

**Frame caveat.** The two Dirac equations below are quoted in the source's generator basis and in the source's index positions, with the frame index of $\mathsf G_a$ and of $\omega_{\imath b a}$ raised where the source raises it; $\mathsf G_a$ is the source's own letter for its four generator basis operators, drawn in its own display, and it corresponds to the four frame basis operators this article writes out. Elsewhere this article writes every label low. The source's basis is not the material frame of Route Two. The comparison map of *Matrix Representations Conventions*, §*The Clifford Structure*, is a dictionary, not an identity: it is the $\mathbb{R}$-algebra isomorphism onto the **even** part, with $e_t\mapsto I$, $\vec e_x\mapsto\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$, $\vec e_y\mapsto\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}$, $\vec e_z\mapsto\,iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}$, and $i\mapsto-iR_{\mathrm{axf},\vec e_x}\,iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$. Its image contains no vector. Vectors are reached only by multiplying by the fixed odd generator,
$$
e_{\mathrm{inf},a}\longmapsto\,iR_{\mathrm{axf},\vec e_x}\times(\text{the basis operator of }e_{\mathrm{inf},a}),
\qquad
e_{\mathrm{inf},a}=(e_t,i\vec e_x,i\vec e_y,i\vec e_z)\in\mathbb{B}_{\Psi} .
$$
Multiplication by the odd basis operator $iR_{\mathrm{axf},\vec e_x}$, not the reading itself, carries $\mathbb{B}_{\Psi}$ to the vector generators; on $\mathbb{B}_{\Phi}$ it gives trivectors. A material frame $\tilde F_{\imath}\in\mathbb{B}_{\Phi}$ therefore maps to a trivector, not to the basis operator of $e_{\mathrm{inf},a}$, and a term-by-term substitution of $\tilde F_{\imath}$ for the four generator basis operators weighted by $e_{\imath a}$ is invalid. The quoted kinetic factor translates through the informational dual frame — with $\mathsf G_a$ the four generator basis operators of the Gamma Formulation, $\mathsf G_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}$ and $\mathsf G_\imath=iL_{\mathrm{axf},e_k}R_{\mathrm{axf},\vec e_y}$ — and the two factors of $i$ in it are one minus sign:
$$
i\,e_{\imath a}\,\mathsf G_a\,\partial/\partial x_{\imath}
=-R_{\mathrm{axf},\vec e_x}\bigl(\text{image of }F_{\mathrm{inf},\imath}\,\partial/\partial x_{\imath}\bigr),
$$
because the map carries the fixed factor $iR_{\mathrm{axf},\vec e_x}$ and $i\cdot i=-1$. The fixed $iR_{\mathrm{axf},\vec e_x}$ is a generator, not part of the derivative; the derivative is the biquaternion-valued $F_{\mathrm{inf},\imath}\partial/\partial x_{\imath}$. The article's own operator $\tilde F_{\imath} D_{\imath}$ is built from the material frame, while the basis operator transcription in this section is built from the informational frame. The fixed generator and $\partial/\partial r'_t=i\partial/\partial R_t$ relate the two, so they are not term-by-term identical, and the substitution of $\tilde F_{\imath}$ for the frame vector $F_{\mathrm{inf},\imath}=e_{\imath a}e_{\mathrm{inf},a}$ is not a rename. In the chiral-pair form the fixed generator drops out, and the kinetic structure is $F_{\mathrm{inf},\imath} D_{\imath}\tilde{Ξ}_{R}=2\pi\nu_m\tilde{Ξ}_{L}$.

J. Fredsted, *Obtaining consistent Lorentz gauging for a gravitationally coupled fermion* (arXiv:1906.12200v3 [physics.gen-ph], 2019), proves that for a Dirac fermion coupled to gravity in the vierbein formulation the substitution $\partial/\partial x_{\imath} \to D_{\imath}$ and the Euler–Lagrange variation **do not commute**. Write $S_{cd}=\tfrac14[\mathsf G_c,\mathsf G_d]$ for the raised spin generator. Varying the gauged action gives the covariant Dirac operator
$$
E_{\mathrm{grav}} =
\bigl(i\,e_{\imath a}\,\mathsf G_a\,\partial/\partial x_{\imath}-m\bigr)\tilde{Ξ}
+\tfrac{i}{2}\bigl(\nabla_{\imath} e_{\imath a}\bigr)\mathsf G_a\tilde{Ξ}
+\tfrac{i}{4}e_{\imath a}\,\omega_{\imath cd}\{\mathsf G_a,S_{cd}\}\tilde{Ξ} ,
$$
while substituting the same replacement into the flat equation of motion gives
$$
\tilde E_{\Phi,\mathrm{grav}} =
\bigl(i\,e_{\imath a}\,\mathsf G_a\,\partial/\partial x_{\imath}-m\bigr)\tilde{Ξ}
+\tfrac{i}{2}e_{\imath a}\,\omega_{\imath cd}\mathsf G_aS_{cd}\tilde{Ξ} ,
$$
and the two do not differ by an anticommutator. Using $\{\mathsf G_a,S_{cd}\}=2\mathsf G_aS_{cd}-[\mathsf G_a,S_{cd}]$, the product form in the substituted equation is half the anticommutator plus half the commutator. The anticommutator coefficient therefore matches the variation's $\tfrac{i}{4}$, and the difference is the commutator term alone:
$$
E_{\mathrm{grav}}-\tilde E_{\Phi,\mathrm{grav}}
=\tfrac{i}{2}\bigl(\nabla_{\imath} e_{\imath a}\bigr)\mathsf G_a\tilde{Ξ}
-\tfrac{i}{4}e_{\imath a}\,\omega_{\imath cd}[\mathsf G_a,S_{cd}]\tilde{Ξ}
=\tfrac{i}{2}\bigl(\nabla_{\imath} e_{\imath a}\bigr)\mathsf G_a\tilde{Ξ}
-\tfrac{i}{2}e_{\imath b}\,\omega_{\imath b a}\mathsf G_a\tilde{Ξ}
=i\bigl(\nabla_{\imath} e_{\imath a}\bigr)\mathsf G_a\tilde{Ξ} ,
$$
where the middle equality uses $[\mathsf G_a,S_{cd}]=\delta_{ac}\mathsf G_d-\delta_{ad}\mathsf G_c$ and the antisymmetry of $\omega_{\imath cd}$, and the last uses the source's frame identity $\tfrac{i}{2}(\nabla_{\imath} e_{\imath a})\mathsf G_a=-\tfrac{i}{2}e_{\imath b}\omega_{\imath b a}\mathsf G_a$. Both surviving terms are grade one: the trivector parts of the two equations agree, and the mismatch is a vector connection term — the derivative of the frame — not a trivector. The source reads the mismatch as a violation of the equivalence principle, since the action-derived equation $E_{\mathrm{grav}}$ must take precedence over the substituted one $\tilde E_{\Phi,\mathrm{grav}}$. For an internal gauge force the two procedures agree, because the internal generators commute with the generator basis operator; gravity is exceptional, and the reason is that $[\mathsf G_c,S_{ab}]$ is a linear combination of the four generator basis operators with coefficients $(V^{ab})_c{}^d$ rather than zero.

The corpus's curved equation is the substitution form. The section above writes $\tilde F_{\imath} D_{\imath}\tilde{Ξ} = 0$ and the chiral pair $\tilde F_{\imath} D_{\imath}\tilde{Ξ}_{R} =2\pi\nu_m\tilde{Ξ}_{L}$, $(\tilde F_{\imath} D_{\imath})^{\natural}\tilde{Ξ}_{L} =2\pi\nu_m\tilde{Ξ}_{R}$ by replacing the rigid material frame and the partial derivative, and the article supplies no action for the coupled system whose variation could be compared with them. So this article does not take a side in the ambiguity. What the external source establishes is that the side matters: the corpus has been writing one of two inequivalent forms without saying which.

**The world-index repair.** The same source then constructs a formalism in which the two procedures commute again, and the construction differs from the corpus's in a way worth stating. The field carries a **world (coordinate) index** $\tilde{Ξ}_{\rho}$, and no local Lorentz label appears at all, neither on the field nor on the frame. The local Lorentz frame is carried by one timelike and three spacelike world vector fields $n_{\imath}$ and $n_{\imath i}$ obeying

$$
n\!\cdot\!n = 1, \qquad n\!\cdot\!n_i = 0, \qquad n_i\!\cdot\!n_j = -\delta_{ij},
$$

so a vierbein is hidden in them and never used, and the metric is $g_{\imath\jmath} = n_{\imath} n_{\jmath} - \delta_{ij}n_{i\imath}n_{j\jmath}$ — the source's signs, $(+,-,-,-)$, not this article's $(-,+,+,+)$. Two families of matrices replace the four generators: $M_{\imath\rho\sigma}$ built from $n_{\imath}$ and $N_{i\rho\sigma}$ built from $n_{\imath i}$,

$$
M_{\imath\rho\sigma} = \bigl(g_{\imath\rho}g_{\jmath\sigma} + g_{\imath\sigma}g_{\jmath\rho} - g_{\imath\jmath}g_{\rho\sigma} - i\varepsilon_{\imath\jmath\rho\sigma}\bigr)n_{\jmath},
$$

$$
N_{i\rho\sigma} = -\bigl(g_{\imath\rho}g_{\jmath\sigma} - g_{\imath\sigma}g_{\jmath\rho} - i\varepsilon_{\imath\jmath\rho\sigma}\bigr)n_{\imath} n_{\jmath i},
$$

and they obey the algebra

$$
M_{\imath} M_{\jmath}^* + M_{\jmath} M_{\imath}^* = 2g_{\imath\jmath}\mathbf{1}, \qquad
M_{\imath} N_i^* + N_i M_{\imath} = 0, \qquad
N_i N_j = \delta_{ij}\mathbf{1} + i\varepsilon_{\imath\jmath\ell}N_\imath,
$$

which is the role the Dirac algebra plays in the standard formalism; the free Lagrangian is Klein–Gordon compatible because of it. The sign of the $\varepsilon$ term is not fixed by the algebra: the source takes it $+$ for a right-handed triad $n_i$ and $-$ for a left-handed one, and the displayed plus is that choice. The covariant derivative is

$$
\partial/\partial x_{\imath}\,\tilde{Ξ}_{\rho} \;\longmapsto\;
D_{\imath}\tilde{Ξ}_{\rho} = \Bigl(\delta_{\rho\sigma}\nabla_{\imath} + \tfrac12\sum_{\alpha,\beta}\omega_{\imath\alpha\beta}S_{\alpha\beta\rho\sigma}\Bigr)\tilde{Ξ}_{\sigma} ,
$$

where $\omega_{\imath\alpha\beta}$ is the source's $\omega_{\alpha\beta\imath}$ in this article's index order, and the Levi-Civita $\nabla_{\imath}$ appears explicitly because the index is a world index, and $S_{\imath\jmath}$ is the spin generator, $4S_{\imath\jmath} = M_{\imath} M_{\jmath}^* - M_{\jmath} M_{\imath}^*$, related to the vector generator by $2S_{\imath\jmath} = V_{\imath\jmath} + i\varepsilon_{\imath\jmath}$, self-dual, and satisfying the source's Eq. (27), the same Lorentz algebra as the spin basis operator $S_{ab}$ of the frame. The Lorentz rotation acts on the field through $\delta\tilde{Ξ}_{\imath} = \tfrac12\sum_{\alpha,\beta}(d\theta_{\alpha\beta})S_{\alpha\beta\imath\jmath}\tilde{Ξ}_{\jmath}$. With these objects the varied equation is **identically** the substituted equation, so the gauging and the variation commute by construction and the ambiguity of the standard vierbein coupling is removed.

**The geometry the repair rests on: the connection is solved, not postulated.** The frame fields are not free parameters of the source's formalism; the connection is built out of them rather than assumed beside them. The metric is the polar form of the frame, $g_{\imath\jmath} = n_{\imath} n_{\jmath} - \delta_{ij}n_{i\imath}n_{j\jmath}$, so that the frame is orthonormal by construction; and the source's connection $\omega_{\imath\jmath\rho}$ is fixed by requiring the frame to be covariantly constant,

$$
D_\rho n_{\imath} = 0 , \qquad D_\rho n_{\imath i} = 0 .
$$

Metric compatibility then follows by the Leibniz rule instead of being imposed, $D_\rho g_{\imath\jmath} = 0$, because $g$ is built from the $n$'s. With the frame so fixed the source computes the curvature of $\omega$ and finds

$$
\Omega_{\imath\jmath\rho\sigma} = -\mathrm{Riem}_{\imath\jmath\rho\sigma} ,
$$

the Riemann tensor of the Levi-Civita symbols, the two sides differing by a sign and nothing else, because the commutator $[D_\rho,D_\sigma]$ annihilates each frame field and the frame is complete. The gravitational action is therefore still the Einstein–Hilbert one, as the source's abstract claims: $g_{\imath\rho}g_{\jmath\sigma}\Omega_{\imath\jmath\rho\sigma} = -\mathrm{Ric}$ is the Einstein–Hilbert Lagrangian up to a sign. The identity has a second face, and it is the one that matters for this article. Because $\omega$ has been solved for in terms of the metric, it is **not an independent field**, the formalism is not a local-Lorentz gauge theory in the sense of Route Three above, there is no field strength of $\omega$ to vary separately, and the compatibility failure of the standard vierbein coupling cannot arise because the object that produced it has been eliminated. What the construction therefore exhibits is a Lorentz-invariant formalism with no Lorentz index anywhere and with the Einstein–Hilbert action intact — at the cost of having no independent Lorentz connection to add dynamics to.

**The world index, and why the coordinate connection cannot be dropped.** The substitution takes the local form $\partial/\partial x_{\imath}\,\tilde{Ξ} \to \partial/\partial x_{\imath}\,\tilde{Ξ} + \tfrac12\sum_{\alpha,\beta}\omega_{\imath\alpha\beta}S_{\alpha\beta}\tilde{Ξ}$ of the standard theory to the world-index form displayed above, and the sentence the source attaches to it carries the whole point: the Levi-Civita covariant derivative appears explicitly **because the field now carries a world index**, where in the standard coupling it carries only a local one. In the standard coupling the field's label is a local Lorentz label, so the partial derivative is promoted by the spin connection alone and no coordinate connection ever appears; the vierbein is then what converts a world vector index into a Lorentz one, and that conversion, performed on the frame in the varied action, is precisely the origin of the anticommutator $\{\mathsf G_a,S_{cd}\}$ of a frame basis operator with the spin generator. Once the field's index is a world index there is nothing to convert, so nothing produces an anticommutator and the varied and substituted equations coincide by construction. The formalism's parsimony is thus not decorative: the absence of Lorentz indices is the same fact as the commutativity of the gauging, seen from the other side. The diacritics of the algebra are the metric transpose, $(V^{\mathsf{T}})_{\imath} = g_{\imath\jmath}V_{\jmath}$ and $(A^{\mathsf{T}})_{\imath\jmath} = g_{\imath\rho}g_{\jmath\sigma}A_{\sigma\rho}$, which reduce to the ordinary transpose when the metric is flat; the $M_{\imath}$ are metric-hermitian and the $N_i$ metric-antisymmetric (Eqs. (22)–(23) of the source), which is what makes the Lagrangian real.

**Status here.** This is an external construction, recorded and not adopted. It is worth recording in this article because it names a gap the boundary list below does not yet contain: the corpus's curved Dirac equation is the substituted form of a gauged flat equation, and the source shows that the substituted form and the varied form are different when the gauge group is the Lorentz group. Its structural relations were recomputed for this article on a constant Levi-Civita frame with the signs $(1,3)$ — the matrix algebra of the source's Eqs. (19)–(21), the hat-hermiticity and hat-antisymmetry (22)–(23), the self-duality of $S_{\imath\jmath}$ and $S_{\imath\jmath}+S_{\imath\jmath}^{\mathsf{T}}=0$, and the algebra of the field (27) — and all hold; the mixed-index position of the epsilon in the relation $2S_{\imath\jmath} = V_{\imath\jmath} + i\varepsilon_{\imath\jmath}$ is the one that makes it an identity. What the construction does not supply is the corpus's question: it is a formalism for a **background** metric handed in through $n_{\imath}$ and $n_{\imath i}$, with no action for those fields, no Einstein equation, and no selection of the metric, so it removes the coupling ambiguity without touching the dynamical void this article has recorded throughout.

## The Informational Sector on a Curved Background

The second half of the framework — $\mathbb{B}_{\Psi}$, its states, its observables and the plain form $\langle\tilde H_{\Psi,1},\tilde H_{\Psi,2}\rangle=\mathrm{Sc}(\tilde H_{\Psi,1}\tilde H_{\Psi,2})$ — has no curved-space treatment, and the absence is structural rather than a matter of effort. The fibre goes through unchanged and the two-sector decomposition survives pointwise; what does not go through is the **trace**, because the trace in the pairing is a pointwise matrix trace with no volume element and no integral, and every trace in a field theory is an integral with a measure that depends on the metric. The pointwise expectation value survives and the global one has nowhere to live. The reason, the four objects that would have to exist before a curved theory could be written, and the one thing that is not blocked are set out in the closing section of [The Curved Dirac Operator and Its Square](the-curved-dirac-operator-and-its-square.html).

## An External Claim of One Tensor Language, and What It Does Not Supply

The two kinds of relativistic tensor dynamics — the antisymmetric one of electrodynamics and the symmetric one of relativity — are usually written differently, and there is an external claim that one biquaternion calculus carries both. E. P. J. de Haas (*Biquaternion Formulation of Relativistic Tensor Dynamics*, arXiv:1401.4470v1, 2013) constructs a biquaternion tensor calculus whose stated goal is exactly that fusion, in a language he describes as "very akin to the standard relativistic space-time language", and reports that it carries no extra terms relative to it. The claim is recorded here because this article's boundary list is where its scope has to be stated.

What such a claim is: a **representational unification at the level of the kinematical fibre**. It shows that one notation can carry a symmetric rank-two tensor and an antisymmetric one at once — which is the vicinity of this article's own bookkeeping problem, since the framework's fields are four-vectors in $\mathbb{B}_{\Phi}$ while the gravitating source is a symmetric rank-two tensor, $(1,1)\oplus(0,0)$ in the vocabulary of the list below in *What Is Constructed and What Is Not*.

What it is **not**: a field equation. The paper supplies no action for the frame or for the connection, no selection of a metric, and no Einstein equation; by its author's own statement it presents known relativistic tensor dynamics in a new formalism, and it derives nothing. It is therefore not a partial answer to *The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap*, and it does not advance the central open question there. The one thing it claims **about the algebra** — that the formulation produces no extra terms beyond the standard relativistic language, the condition being the Lorenz gauge $F_0 = \partial/\partial x_{\jmath} A_{\jmath} = 0$ — is recorded, with its cautions, in *Relativistic Mechanics in Biquaternionic Form*.

The boundary of this article is unchanged by the claim, and the claim is unchanged by the boundary: one is about notation at a point, the other about dynamics for the field that attaches the notation to a curved manifold.

## An External Claim That the Bundle Basis Is Biquaternionic

A second external source reaches this article's own subject from the opposite direction, and it is worth separating from the first, because it claims more. D. J. Cirilo-Lombardo (*Algebraic structures, physics and geometry from a Unified Field Theoretical framework*, arXiv:1411.5493v3 [hep-th], 2015) works from a unified field theory unrelated to the corpus and asks what algebraic structure the **basis** of its principal fibre bundle $P(G,M)$ carries; his answer is the biquaternion algebra. The bundle is new here — no article of the series constructs a principal bundle over the manifold with the algebra in the basis — and the claim is *stronger* than anything this article has built, because a basis is exactly the thing the section *Curvature Cannot Be Carried by the Algebra* showed cannot carry curvature.

The dictionary is exact, and the companion article *The Biquaternion Basis of a Unified-Field Fibre Bundle* records the verification entry by entry. The source assembles its structural group from one $2\times2$ matrix, which is the image $\mathsf{M}_2(\tilde Q)$ of the biquaternion $\tilde Q = a_0 + \vec a\!\cdot\!\mathbf e$ under the isomorphism of *Matrix Representations Conventions*, §*The $2\times2$ Pauli Representation*, with the coefficients fixed by a four-momentum, $a_0 = p_0/m$ and $\vec a = i\vec p/m$. Its unit-norm condition and its relativistic relation are then one identity, $\langle\tilde Q\rangle_{\natural} = 1$, and its object is the Hermitian biquaternion of $\mathbb{B}_{\Psi}$ — the informational sector, not the material one this article's metric is read from. Its own "conjugate transpose" $G^+$ is the quaternionic conjugation of that matrix and not the matrix adjoint; that is the interpretation in which its $G^+G = I_4$ holds, and the distinction is invisible while the coefficients are real.

**Which naturality is meant.** The word *naturally* has to be split before the claim can be assessed, and the two interpretations are different statements. A **preferred-basis** claim would assert that the bundle's structure group reduces into the biquaternion group of invertibles; that is a statement about $G$, it is testable, and the source's own test is $G^+G = I_4$ in just the conjugation that holds. An **algebra-on-the-fibres** claim would assert that each fibre is a module over $\mathbb{B}$; that is what *The Hopf Fibration and the Biquaternion Gauge Bundle* already constructs from the framework's side, and it is a statement about the fibres rather than about the basis. The corpus reads the second as true and unremarkable and the first as the substantive claim.

**What it does not supply.** No reduction is exhibited and no curvature is computed from the bundle, so the claim does not move this article's boundary. A biquaternionic basis would still be a pointwise structure, and a field attaching it to the manifold would still be required; a fibre algebra is not a connection, an action or a metric. The source's concluding geometry — a G-structure on $T(M)$ whose reduced structure group changes the spacetime structure itself, and a metric sign and CP character induced by torsion — is recorded, and left as a claim, in *The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap*. One assertion of the source's is **not** reproduced: the Lorentzian metric it says is invariant under $G$ "due to its general form" is not invariant under it in any of the sign choices tried here; what does hold is the invariance of the quaternionic norm, and that only through $G^+$ and not through the ordinary transpose.

**A constructed instance, from the same algebra.** A third source does not merely claim that the basis can be biquaternionic; it builds the whole formalism around one, and the construction reproduces this article's frame route in the source's own notation. J. Fredsted (*Spinor fields without Lorentz frames in curved spacetime using complexified quaternions*, arXiv:0811.1357v4 [math-ph], 2009) discards the manifold frame outright — he writes "leaving the arena of Riemannian manifolds" — and takes as primitive a basis $s_{\imath} \in (\mathbb{C}\otimes\mathbb{H})_-$ inside the same biquaternion algebra, that is, exactly this article's material sector $\mathbb{B}_{\Phi}$. The metric is then **defined**, not inserted, by the polar form,

$$
g_{\imath\jmath} = \langle s_{\imath}, s_{\jmath}\rangle ,
$$

which is this article's own $g_{\imath\jmath} = \langle \tilde E_{\Phi,\imath}, \tilde E_{\Phi,\jmath}\rangle_{\natural}$; the nondegeneracy of the metric follows from the linear independence of the four basis elements, and the source notes that a basis in the opposite sector $(\mathbb{C}\otimes\mathbb{H})_+$ would give the opposite signs. Local Lorentz freedom is the rotor conjugation $s_{\imath} \mapsto \Lambda s_{\imath} \bar{\Lambda}$ with $\Lambda$ in $Sp(1,\mathbb{C}) \cong SL(2,\mathbb{C})$, so the metric is invariant for the reason the frame route's metric is invariant: the same verified statement, written with the source's conjugations — the bar in these displays is the source's quaternion conjugate, not the corpus's complex conjugation $\bar{\cdot}$.

What makes the construction worth recording here is its connection. A **single** algebra-valued $\omega_{\imath} \in \mathbb{C}\otimes\mathbb{H}$, subject only to the reality condition $\mathrm{Sc}(\omega_{\imath} + \bar{\omega}_{\imath}^*) = 0$, carries everything: its imaginary-scalar part $\mathrm{Sc}(\omega_{\imath}) \in i\mathbb{R}$ is a local $\mathrm{U}(1)$ freedom, which the source speculates may be electromagnetism, and its vector part $\mathrm{Vect}(\omega_{\imath}) \in \mathbb{C}\otimes\mathrm{Vec}(\mathbb{H})$ is the Lorentz connection. The fields transform one-sidedly, $\tilde{Ξ}_{L} \mapsto \Lambda\tilde{Ξ}_{L}$ and $\tilde{Ξ}_{R} \mapsto \tilde{Ξ}_{R}\bar{\Lambda}$, and their covariant derivatives are correspondingly one-sided, with the connection inserted on the left for $\tilde{Ξ}_{L}$ and on the right for $\tilde{Ξ}_{R}$. This is the two-connections situation of *The Covariant Derivative and Gauge Connection in Biquaternionic Form* seen from the other side: the corpus keeps its central $\mathrm{U}(1)$ connection $\tilde A_{\Phi,\imath}$ and its scalar-free Lorentz connection $\vec\Gamma_{\imath}$ apart and says no relation between them is asserted; the source has one algebra-valued connection whose two parts are the two objects. It also differs from the corpus's construction in that $\omega_{\imath}$ is a general biquaternion subject to one scalar condition, not restricted to the six-dimensional Lie subspace.

**The connection is derived, not inserted.** This is the part of the construction that goes beyond the frame route of this article. The source's covariant derivative of the basis is $D_\rho s_{\jmath} = \nabla_\rho s_{\jmath} + \omega_\rho s_{\jmath} + s_{\jmath}\bar{\omega}_\rho^*$ with $\nabla_\rho s_{\jmath} = \partial/\partial x_\rho s_{\jmath} - \Gamma_{\imath\jmath\rho}s_{\imath}$, and where $\varsigma_{\imath}$ is the dual basis, $\langle\varsigma_{\imath},s_{\jmath}\rangle=\delta_{\imath\jmath}$; the connection coefficients are then **determined**, not chosen, by the source's "minimality condition" $D_\rho s_{\jmath} \equiv 0$:

$$
\Gamma_{\imath\jmath\rho} = \left\langle \varsigma_{\imath},\ \partial/\partial x_\rho s_{\jmath} + \omega_\rho s_{\jmath} + s_{\jmath}\bar{\omega}_\rho^*\right\rangle .
$$

The bracketed element lies in $\mathbb{B}_{\Phi}$ — it is a sum of the $\mathbb{B}_{\Phi}$-valued derivative $\partial/\partial x_\rho s_{\jmath}$ and of terms $\omega_\rho s_{\jmath} + s_{\jmath}\bar{\omega}_\rho^*$, which combine into an $\mathbb{B}_{\Phi}$ element — and the bilinear form is real on $\mathbb{B}_{\Phi}$, so $\Gamma_{\imath\jmath\rho}$ is real-valued; this, together with the metric-compatibility computation below, was recomputed here. Two consequences deserve naming. First, **metric compatibility is a consequence, not a condition**: $\nabla_\rho g_{\imath\jmath} = 0$ follows from the minimality of $\Gamma$ together with the reality condition on $\omega_{\imath}$, whereas Route Three above records metric compatibility and the vanishing of torsion as conditions the framework must impose from outside. Second, $\Gamma_{\imath\jmath\rho}$ **need not be symmetric** under the exchange of its two last labels — the source states this, and the asymmetry is exactly what makes $\nabla_{\imath} A_{\jmath} - \nabla_{\jmath} A_{\imath}$ differ from $\partial/\partial x_{\imath} A_{\jmath} - \partial/\partial x_{\jmath} A_{\imath}$ for the connection's own $\mathrm{U}(1)$ part.

**The curvature, and the Lagrangian the source leaves unsettled.** The field strength of the single connection is $\Omega_{\rho\sigma} = \nabla_\rho\omega_\sigma - \nabla_\sigma\omega_\rho + [\omega_\rho,\omega_\sigma]$, and the minimality condition turns the double commutator of covariant derivatives into the identity

$$
[\nabla_\rho,\nabla_\sigma]s_{\imath} + \Omega_{\rho\sigma}s_{\imath} + s_{\imath}\bar\Omega_{\rho\sigma}^* = 0 ,
$$

whose last two terms are the same two-sided action — left action of $\Omega$, right action of its conjugate — that Route Three's derivative $\partial/\partial x_{\imath}\,\tilde Q + \vec\Gamma_{\imath}\tilde Q + \tilde Q\vec\Gamma_{\imath}^{*}$ exhibits. With the connection split as $\omega_{\imath} = \xi_{\imath} + igA_{\imath}$, where $\xi_{\imath} \in \mathbb{C}\otimes\mathrm{Vec}(\mathbb{H})$ and $A_{\imath} \in \mathbb{R}$, the field strength splits as $\Omega_{\imath\jmath} = \mathcal F_{\mathrm{med},\imath\jmath} + igF_{\imath\jmath}$ with $\mathcal F_{\mathrm{med},\imath\jmath} = \nabla_{\imath}\xi_{\jmath} - \nabla_{\jmath}\xi_{\imath} + [\xi_{\imath},\xi_{\jmath}]$ and $F_{\imath\jmath} = \nabla_{\imath} A_{\jmath} - \nabla_{\jmath} A_{\imath}$; both the split and the term-by-term decomposition were verified here. The scalar piece of the one connection therefore produces a Maxwell-type field strength and the vector piece a Yang–Mills-type curvature. The source then proposes an Einstein–Hilbert-like Lagrangian, $(1/\kappa)\mathrm{Lag} = \mathrm{Riem}_{\imath\jmath\imath\jmath}(\Gamma)$ with $\mathrm{Riem}_{\imath\jmath\rho\sigma}(\Gamma) = \langle \varsigma_{\imath},[\nabla_\rho,\nabla_\sigma]s_{\jmath}\rangle$, and an alternative $(1/\kappa)L = \mathrm{Re}\sum_{\imath,\jmath}\langle\Omega_{\imath\jmath},\Omega_{\imath\jmath}\rangle$, and judges both unsettled; both are recorded, with the reason for each verdict, in *The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap*.

**Weight of the instance.** A constructed instance is more than the bundle claim above, and it should be counted as what it is. It shows that the biquaternionic basis is not idle: four elements of $\mathbb{B}_{\Phi}$ determine a Lorentzian metric through the algebra's own bilinear form, and one algebra-valued connection suffices for the tensor field and the field alike. It does not show more. There is no settled action for $s_{\imath}$ or $\omega_{\imath}$ and no field equation; the Riemann tensor of the induced connection and its identity with the field strength are written, but nothing is varied and no dynamics is attached to them, so the metric is general while its dynamics are absent, which is the same void this article records for the frame route. Nor is it a construction of the principal bundle $P(G,M)$ of the first source above: the basis is a basis of the algebra over the manifold, not the basis of a principal bundle with a structural group. The instance therefore raises the bundle claim's floor — from proposal to construction — without raising its ceiling.

## What Is Constructed and What Is Not

The boundary can be drawn as a list, and drawing it is this article's main result.

**Constructed** (algebraic facts, each recomputed for this article). The pointwise metric of $\mathbb{B}_{\Phi}$ as the polar form of the biquaternion norm, with inertia $(3,1)$. Its invariance under rotor conjugation. The representation of an arbitrary Lorentzian metric by a frame field $\tilde{E}_{\Phi,\imath} \in \mathbb{B}_{\Phi}$ with $g_{\imath\jmath} = \langle \tilde{E}_{\Phi,\imath}, \tilde{E}_{\Phi,\jmath}\rangle_{\natural}$, and the local $SL(2,\mathbb{C})$ gauge invariance of that representation. The identification of $SU(2)$'s Lie algebra with the six-dimensional scalar-free subspace of $\mathbb{B}$. The two-sided infinitesimal action of a connection, and the vanishing of the array trace of a rotor field's logarithmic derivative. The curved biquaternion Dirac operator $\tilde F_{\imath} D_{\imath}$, built from the dual frame and the one-sided derivative $D_{\imath}\tilde{Ξ} = \partial/\partial x_{\imath}\,\tilde{Ξ} + \vec\Gamma_{\imath}\tilde{Ξ}$, with its covariant connection transformation, its exact flat limit, and the Lichnerowicz square $(\tilde F_{\imath} D_{\imath})^2 = -\Box_{g,\Phi} + \tfrac14 \mathrm{Ric}$ of its basis operator reading. The induced metrics of the local-scale route in both interpretations, with the flatness of Reading A and the closed-form curvature of Reading B, and the result that within Reading B's metric class Ricci-flatness implies flatness. The identification of the Kerr–Schild class as the orbit of the flat form under the unipotent null shear $\exp(hN_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}})$, with the affineness in $h$, the unimodularity $\det g=\det\delta$, the closed-form inverse and the direction being fixed and therefore still null, all read as the one vanishing square $N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}^2=0$, and the plane-fronted wave as its constant-direction member.

**Not constructed** (the boundary, and what each row needs). An action principle or field equation for the frame or the connection, and hence any Einstein equation. Coupling to sources, with the bookkeeping problem that the gravitating objects are symmetric rank-2 tensors, $\left(1,1\right)\oplus\left(0,0\right)$, while the framework's own fields are four-vectors in $\mathbb{B}_{\Phi}$. The curved-space form of the biquaternion **Maxwell** equation written in the framework's own notation, for which the background-dependence of $\tilde\nabla_\Phi$ is precisely the obstacle; the corresponding **Dirac** form is constructed in the section *The Biquaternion Dirac Equation on a Curved Background* above, on a background whose frame and connection are still inserted by hand and whose current source remains the object of the companion articles. The **coupling ambiguity** of the Lorentz gauge group: the Dirac form written here is the substituted form of a gauged flat equation, and the source recorded in *Lorentz Gauging and the Euler–Lagrange Variation* shows that the varied form differs, because the Lorentz generator does not commute with the generator basis operator; whether the corpus should adopt the varied form, or the world-index formalism that removes the difference, is open. Global and topological structure: the algebra is a point, so causal structure, singularity theorems, the *global* layer of a horizon and the topology of the manifold are outside it — though the pointwise and locus halves of horizon geometry are reachable, as [Horizons Without a Global Structure](horizons-without-a-global-structure.html) records — and even the existence of the field on a manifold is a topological condition — the vanishing of the second Stiefel–Whitney class — that the algebra cannot see; the globalisation of the field to a bundle over a curved background is recorded as a separate open item in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. The discrete symmetries, which are not in the connected $SU(2)$. The informational sector, as above. And empirical contact, which remains the framework's central open question and is not advanced by anything here.

The honest summary of the boundary is this. The biquaternion framework contains the kinematical fibre of tetrad gravity: a pointwise Lorentzian vector space, its Lorentz group, the vector representation, and the Lie-algebra-valued connection. It contains nothing of tetrad gravity's dynamics, and nothing that selects a metric. It is therefore not correct to say that the framework contains general relativity, and it is not correct to say that it conflicts with it. What the framework contains is the algebra in which the local part of general relativity is normally written, plus a proposal — the local scale factor of the imaginary time axis — that is too rigid to carry the non-flat vacuum solutions.

## The Local Complex Structure as an Emergent Metric

This article puts the biquaternion Dirac equation on an imported background $g$. The framework's own construction is more modest and, read one way, more suggestive: the complex structure is **local**, fixed point by point by the medium through $c=1/\sqrt{\epsilon\mu}$, and a change of the local structure moves the interval and the composition while leaving the probability form and the zero-divisor cone (*The Local Complex Structure and the Speed of Light*).

Read further, the local complex structure is an **emergent metric** in the sense of the analogue-gravity programme — the wave cone is a property of the medium and not of a fixed background — and the construction is a **bundle of algebras** whose typical fibre is the biquaternion algebra, whose local complex structure is a section of the frame bundle and whose medium is a connection on it. The interpretation is labelled and bounded: it is the shape the framework's algebra takes when the complex structure is allowed to vary, and it is offered against the imported $g$, not as a derivation of Einstein's equations. The owner of the local construction is *The Local Complex Structure and the Speed of Light*.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*. The generators carry no frame label: $\gamma_{\imath}$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_\imath^2=-I_4$. The frame belongs to the coordinate, not to the array.

The five gammas are the five frame basis operators of *Matrix Representations Conventions*, §*The Clifford Structure*, written as arrays. The section prints each of them in both displays: the $\mathrm{pau}$ display first, whose arrays are the ones the literature prints, and the axis-free display after it, labelled $\mathrm{axf}$, whose basis operators are the ones this article writes:

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

The four of them are, as basis operators, the frame basis operators the Dirac operator of this article is built from, and the fifth is $\mathsf{V}_{\mathrm{vol}}=-iR_{\vec e_z}$, a pure right multiplier that the display writes $\gamma_5$. The anticommutation $\{\gamma_a,\gamma_b\}=2\varepsilon_a\delta_{ab}I_4$ is the weight carried into the Lichnerowicz square of §*Flat Limit and the Square*, and the four compose to the fifth, $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$. The traces, the contraction sums and the algebra of the five are those of the conventions article, §*The Legacy Pauli Gamma Formulation*, and are not restated here. Nothing in the body of this article prints an array: the operators it uses are written there as basis operators or as elements.

## Summary

The read-list machinery is flat and pointwise: one fixed algebra, one fixed biquaternion norm with constant coefficients, a global chart with a distinguished imaginary time, and a global $SU(2)$. Curvature cannot be made a property of the algebra, because the algebra has no points and no deformable coefficient; it can only be carried by the field that attaches the algebra to spacetime.

The framework's own local device is the conversion $r'_t = c\,t'$ with $c = 1/\sqrt{\epsilon\mu}$ the local speed of light. It admits two inequivalent interpretations. As a definition of the temporal coordinate, the interval is $\langle d\tilde R_\Phi\rangle_{\natural}=-d{r'_{t}}^2+dr_x^2+dr_y^2+dr_z^2$; written in $(t',\vec r)$ it is a nondegenerate metric with $\det g = -c^2$ that is identically flat — the pullback of the flat form of $\mathbb{B}_{\Phi}$ along a diffeomorphism — as direct computation confirms. As a coefficient $c^2$ multiplying $d{t'}^2$ with $c$ held fixed in the differential, it yields $g_{\imath\jmath} = \mathrm{diag}(-c^2,1,1,1)$, genuinely curved, with $\mathrm{Ric}_{00} = u\Delta_\Phi u$, $\mathrm{Ric}_{0i} = 0$, $\mathrm{Ric}_{ij} = -(\partial^2 u/\partial x_i\partial x_j)/u$ for $u = c$. The framework's prose does not choose between the interpretations, and the choice is left open here.

Within the second interpretation's class — one function, no shift, flat spatial slices — Ricci-flatness forces $u$ to be affine in the spatial coordinates, and every such metric is flat. The class therefore contains no non-flat vacuum geometry: no Weyl curvature, no gravitational waves, no black-hole exteriors. The local scale factor is not the route to general relativity. Nor is it the same object as the metric: $c$ is the Maxwell speed of a medium, and the standard effective metric of a dielectric is a metric for light, not for free fall.

A general curved metric can be carried, by a frame field $\tilde{E}_{\Phi,\imath}(x) \in \mathbb{B}_{\Phi}$ with $g_{\imath\jmath} = \langle \tilde{E}_{\Phi,\imath}, \tilde{E}_{\Phi,\jmath}\rangle_{\natural}$, since any Lorentzian metric has a local orthonormal frame. The algebra then supplies the pointwise $SL(2,\mathbb{C})$, its vector representation, and its Lie algebra; the sixteen frame functions modulo six local rotor parameters reproduce the ten components of the metric; and a frame that is pure rotor gauge is flat, a condition that is sufficient and not necessary, so curvature can only come from the part of the frame that is neither a rotor gauge nor a change of chart. The algebra can even carry the connection and its curvature, since the Lie algebra is the six-dimensional scalar-free subspace of $\mathbb{B}$ — with the caveat that the infinitesimal action is the two-sided $G\tilde R_\Phi + \tilde R_\Phi G^{*}$, not the commutator, the two differing precisely for the boosts.

One sub-class of frames is worth separating because the algebra contributes more to it than a bilinear form, and it is the **Kerr–Schild class**, $g_{\imath\jmath} = \delta_{\imath\jmath} + 2h\,\ell_{\imath} \ell_{\jmath}$ with $\sum_{\imath} \ell_{\imath}^2 = 0$. The class is the orbit of the flat form under a shear along a null direction, the shear's generator is square-zero because a null direction is a zero divisor, and the affineness in $h$, the unimodularity $\det g = \det\delta$, the closed-form inverse and the direction's being fixed while still null are four faces of that one vanishing square. With a constant direction and a transverse harmonic $h$ the class contains a vacuum plane-fronted wave, so the frame route carries a vacuum gravitational wave that the local-scale route cannot. None of it is dynamics: the direction and $h$ are three free functions, and for Kerr–Newman they are fixed by the Kerr theorem and the Einstein–Maxwell equations, not by the algebra. The construction, the four identities and the numerical checks are the subject of [The Kerr–Schild Sub-class and the Vacuum Wave](the-kerr-schild-sub-class-and-the-vacuum-wave.html).

The field $\tilde{Ξ}$ is an element of $\mathbb{B}$ and carries a different action from the four-vector, so its curved equation has a different derivative. The field carries the **left** action $\tilde{Ξ} \mapsto \tilde U\tilde{Ξ}$, not the two-sided rotor conjugation, so its covariant derivative is the **one-sided** $D_{\imath}\tilde{Ξ} = \partial/\partial x_{\imath}\,\tilde{Ξ} + \vec\Gamma_{\imath}\tilde{Ξ}$, with $\vec\Gamma_{\imath}$ in the Lie subspace; covariance fixes the inhomogeneous transformation $\vec\Gamma_{\imath} \mapsto \tilde U\vec\Gamma_{\imath}\tilde U^{-1} - (\partial/\partial x_{\imath}\,\tilde U)\tilde U^{-1}$. With the dual frame $\tilde F_{\imath} = g_{\imath\jmath}\tilde E_{\Phi,\jmath}$ this gives the curved biquaternion Dirac operator $\tilde F_{\imath} D_{\imath}$, whose massless equation is $\tilde F_{\imath} D_{\imath}\tilde{Ξ} = 0$ and whose massive form is the same chiral pair as in the flat case, $\tilde F_{\imath} D_{\imath}\tilde{Ξ}_{R} =2\pi\nu_m\tilde{Ξ}_{L}$, $(\tilde F_{\imath} D_{\imath})^{\natural}\tilde{Ξ}_{L} =2\pi\nu_m\tilde{Ξ}_{R}$, the mass being untouched by the curvature. The operator reduces exactly to $\tilde\nabla_\Phi$ in the rigid material frame $\tilde E_{\Phi,0}=ie_t$, $\tilde E_{\Phi,k}=\vec e_\imath$ with vanishing connection, and its basis operator square is the Lichnerowicz formula $(\tilde F_{\imath} D_{\imath})^2 = -\Box_{g,\Phi} + \tfrac14 \mathrm{Ric}$, so the curvature couples to the field through the scalar curvature even without a source. That much of the curved matter equation is now constructed in the framework's own notation. What remains is unchanged and unyielding: the frame and the connection are inserted by hand and satisfy no equation, the metric is not selected, the current that would source the coupled system is the object of the field's own articles, carrying the basis operator $iR_{\mathrm{axf},\vec e_x}$ outside $\mathbb{B}$, and the global existence of the field is a topological condition no local operator can see.

What is missing is not a technical detail but the theory. Nothing determines the frame, the connection, or the metric; there is no action, no field equation, and no Einstein equation; the gravitating rank-2 tensors are not the framework's four-vectors; diffeomorphism invariance has no algebraic counterpart; global and topological structure is outside a pointwise algebra; and the informational sector's pairing formula is a fibre trace with no measure and no integral, so its curved-space extension is not merely unwritten but unlocated. The horizon case shows what that costs in detail: the local half of horizon physics is reachable and the global half is not, as [Horizons Without a Global Structure](horizons-without-a-global-structure.html) sets out, and the cosmological case shows the same boundary from the other side in [FLRW in the Frame Route](flrw-in-the-frame-route.html). The missing object that would close the dynamics — an action — is treated on its own in [The Action Problem](the-action-problem.html). The framework contains the kinematical fibre of tetrad gravity and none of its dynamics; the title names a framework, and that is exactly what it is.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\imath^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | Hermitian (informational) and anti-Hermitian (material) subspaces |
| $\delta_{\imath\jmath}=(1,1,1,1)$ | The unit metric on the four $Q_{\imath}$: diagonal, all four coefficients $+1$; in the material reading its interval is $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$ |
| $\mathbb{B}_{H}$ | Real-quaternion subspace, home of the rotation rotors |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{\natural})$ | The general quaternionic bilinear form, the polar form of the norm, on $\mathbb{B}_{\Phi}$; the interval |
| $\tilde U \in SL(2,\mathbb{C})$ | Unit-norm biquaternion (Lorentz rotor) |
| $\tilde{Q} \mapsto \tilde U\tilde{Q}\tilde U^{*}$ | Rotor conjugation (four-vector action) |
| $\mathrm{Ad} : SL(2,\mathbb{C}) \to SO^+(1,3)$ | Two-to-one covering homomorphism, kernel $\{\pm e_t\}$ |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $i r'_t$ | Local imaginary time coordinate, material sector |
| $\tilde\nabla_\Phi = e_t\partial/\partial R_t+\sum_{\imath\in\{x,y,z\}}\,\vec e_\imath\partial/\partial R_\imath$ | Biquaternionic gradient, $Q_t=i q'_t$; needs a global chart |
| $\tilde{E}_{\Phi,\imath}(x) \in \mathbb{B}_{\Phi}$ | Frame field (tetrad): $d\tilde R_\Phi = \sum_{\imath}\tilde{E}_{\Phi,\imath} dx_{\imath}$ |
| $g_{\imath\jmath} = \langle \tilde{E}_{\Phi,\imath},\tilde{E}_{\Phi,\jmath}\rangle_{\natural}$ | Metric carried by the frame field |
| $\ell_{\imath}$, $\tilde{\mathcal L}_{\Phi,\mathrm{null}} = \sum_{\imath} \ell_{\imath} e_{\imath}$ | Null covector and the null element it names: $\langle e_{\imath},\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = \ell_{\imath}$ and $\langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = \sum_{\imath} \ell_{\imath}^2 = 0$; the sign is the square of the $i$ in $Q_t$ |
| $N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}(X) = \tilde{\mathcal L}_{\Phi,\mathrm{null}}\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural$ | Rank-one real-linear map of $\mathbb{B}_{\Phi}$ built from a null element; $N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}^2 = 0$, $\mathrm{tr}\,N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}} = \langle\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = 0$ |
| $T = \exp(hN_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}) = \mathrm{id} + hN_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}$ | The null shear, a unipotent map of $\mathbb{B}_{\Phi}$; on the rigid frame $T\tilde E_{\Phi,\imath} = \tilde E_{\Phi,\imath} + h\ell_{\imath}\tilde{\mathcal L}_{\Phi,\mathrm{null}}$, the Kerr–Schild frame |
| $g_{\imath\jmath} = \delta_{\imath\jmath} + 2h\,\ell_{\imath} \ell_{\jmath}$ | Kerr–Schild form: the orbit of $\delta_{\imath\jmath}$ under the null shear; $\det g = \det\delta$, and the inverse array is $\delta_{\imath\jmath} - 2h\,\ell_{\imath} \ell_{\jmath}$ |
| $\tilde{\mathcal L}_{\Phi,\mathrm{null}}^{\perp}$ | Kernel of $N_{\tilde{\mathcal L}_{\Phi,\mathrm{null}}}$: the three-plane $\langle X,\tilde{\mathcal L}_{\Phi,\mathrm{null}}\rangle_\natural = 0$, fixed pointwise by $T$ |
| $\vec e_\imath$, $B_{\mathrm{boost},k} = i\vec e_\imath$ | Rotation and boost generators, spanning $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}} \subset \mathbb{B}$ |
| $\vec\Gamma_{\imath}$ | Connection 1-form, valued in the Lie subspace |
| $D_{\imath}\tilde{Q} = \partial/\partial x_{\imath}\,\tilde{Q} + \vec\Gamma_{\imath}\tilde{Q} + \tilde{Q}\vec\Gamma_{\imath}^{*}$ | Covariant derivative on $\mathbb{B}_{\Phi}$ (two-sided) |
| $\tilde F_{\imath} = g_{\imath\jmath}\tilde E_{\Phi,\jmath}$, $\langle \tilde F_{\imath}, \tilde E_{\Phi,\jmath}\rangle_{\natural} = \delta_{\imath\jmath}$ | Material dual frame (inverse tetrad) |
| $iL_{\mathrm{axf},e_a}R_{\mathrm{axf},\vec e_{\mathrm{spt}(a)}}$ | The four frame basis operators of the vector legs, with $\mathrm{spt}(t)=x$ and $\mathrm{spt}(\eta)=y$; the fifth basis operator of the frame is $\mathsf{V}_{\mathrm{vol}}=-iR_{\vec e_z}$, a pure right multiplier |
| $S_{ab}=\tfrac14[iL_{e_a}R_{\vec e_{\mathrm{spt}(a)}},iL_{e_b}R_{\vec e_{\mathrm{spt}(b)}}]$ | Spin basis operator, a quarter of the commutator of two frame basis operators; a derived form |
| $\varepsilon_a$, $\varepsilon=(1,-1,-1,-1)$ | The plain weight of a contraction, the basis operators' multiplication weight; a property of the multiplication, not of a frame; not the Levi-Civita $\varepsilon_{\imath\jmath\rho\sigma}$ and not the world metric $g_{\imath\jmath}$ |
| $e_{\mathrm{inf},a}=(e_t,i\vec e_x,i\vec e_y,i\vec e_z)$ | Informational basis; the basis operator of $e_{\mathrm{inf},a}$ is even, and multiplication by the odd basis operator $iR_{\mathrm{axf},\vec e_x}$ carries it to the vector generators |
| $F_{\mathrm{inf},\imath}=e_{\imath a}e_{\mathrm{inf},a}$ | Informational dual frame; the exact transcription of the source's Dirac operator uses it |
| $e_{\imath a}$ | Inverse vierbein components; world slot first, frame label second |
| $\epsilon_{\imath}$ | Sign vector, $\epsilon_0=1$, $\epsilon_\imath=-1$: the C-space interval, the signs $(+,-,-,-)$ (the permittivity is $\epsilon$, without an index) |
| $\omega_{\imath ba}$ | Spin connection; world slot, then frame row, then frame column, all low except in the quoted Lorentz displays, which keep the source's raised row |
| $\varsigma_{\imath}$ | Dual basis to $s_{\imath}$, $\langle\varsigma_{\imath},s_{\jmath}\rangle=\delta_{\imath\jmath}$ |
| $D_{\imath}\tilde{Ξ} = \partial/\partial x_{\imath}\,\tilde{Ξ} + \vec\Gamma_{\imath}\tilde{Ξ}$ | Covariant derivative on the field (one-sided, left action) |
| $\tilde F_{\imath} D_{\imath}$ | Curved biquaternion Dirac operator |
| $(\tilde F_{\imath} D_{\imath})^2 = -\Box_{g,\Phi} + \tfrac14 \mathrm{Ric}$ | Lichnerowicz square of the basis operator reading, $\vec\nabla_\Phi^{*}\vec\nabla_\Phi+\tfrac14\mathrm{Ric}$ with $\vec\nabla_\Phi^{*}\vec\nabla_\Phi=-\Box_{g,\Phi}$; $\Box_{g,\Phi}$ Laplace–Beltrami on the field, $\mathrm{Ric}$ Ricci scalar |
| $u = c$, $w = c^2$ | Local scale factor and its square, in the local-scale route |
| $\mathrm{Ric}_{00}=u\Delta_\Phi u$, $\mathrm{Ric}_{0i}=0$, $\mathrm{Ric}_{ij}=-(\partial^2 u/\partial x_i\partial x_j)/u$ | Ricci tensor of $g=\mathrm{diag}(-c^2,1,1,1)$, corpus convention |
| $(m,n)$, $\left(\tfrac12,\tfrac12\right)$, $\left(1,1\right)\oplus\left(0,0\right)$ | Lorentz representations: four-vectors; symmetric rank-2 tensors |

## Further Reading

Companion articles of this category, each a development of one of the sections above:

- [The Gram Matrix as the Only Metric](the-gram-matrix-as-the-only-metric.html), for the frame relation as a statement about quadratic spaces.
- [The Two-Sided Derivative and the Star Eigenvalue](the-two-sided-derivative-and-the-star-eigenvalue.html), for Route Three's connection in full.
- [The Curved Dirac Operator and Its Square](the-curved-dirac-operator-and-its-square.html), for the curved Dirac operator, the Lichnerowicz square and the informational sector's absence.
- [The Kerr–Schild Sub-class and the Vacuum Wave](the-kerr-schild-sub-class-and-the-vacuum-wave.html), for the exact class the frame route carries and the vacuum wave.
- [Linearized Gravity in Biquaternionic Form](linearized-gravity-in-biquaternionic-form.html), for the linearisation of the frame route and the collapse of the single-biquaternion packaging.
- [Gravitational Waves in Biquaternionic Form](gravitational-waves-in-biquaternionic-form.html), for the wave sector on a carried background.
- [The Newman–Penrose Formalism in Biquaternionic Form](the-newman-penrose-formalism-in-biquaternionic-form.html), for the null tetrad as the algebra's own Peirce basis, and for the Weyl scalars in $\mathrm{sym}^4S$.
- [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html), for the antisymmetric part of the connection that Route Three leaves as a condition.
- [The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap](the-einstein-field-equations-in-the-biquaternion-framework-the-linearised-dictionary-and-the-non-linear-gap.html), for what this boundary leaves unbuilt and what would close each item.
- [Black Hole Thermodynamics in Biquaternionic Form](black-hole-thermodynamics-in-biquaternionic-form.html), for the horizon thermodynamics the corpus hosts and transcribes.
- [Horizons Without a Global Structure](horizons-without-a-global-structure.html), for which horizon statements are pointwise and which are not.
- [FLRW in the Frame Route](flrw-in-the-frame-route.html), for the explicit cosmological frame.
- [The Action Problem](the-action-problem.html), for the single missing object and why the algebra cannot supply it.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Charles W. Misner, Kip S. Thorne, and John A. Wheeler, *Gravitation* (Freeman, 1973), for the tetrad formalism and the distinction between coordinate and orthonormal frames in general relativity.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the metric, the curvature tensors, and the spinor formulation of curved spacetime.
- A. Lichnerowicz, "Spineurs harmoniques," *Comptes Rendus de l'Académie des Sciences* **257** (1963) 7–9, for the square of the Dirac operator and the $\tfrac14 \mathrm{Ric}$ curvature term.
- G. C. Debney, R. P. Kerr and A. B. Schild, "Solutions of the Einstein and Einstein–Maxwell Equations," *Journal of Mathematical Physics* **10** (1969) 1842, for the Kerr–Schild family whose null congruence is generated by the Kerr theorem: the electrovacuum solutions written in the form of the section *The Kerr–Schild Form: a Null Shear of the Flat Form*, with the profile function fixed by the field equations rather than by the algebra.
- Alexander Burinskii, "Stringlike structures in the real and complex Kerr–Schild geometry," arXiv:1410.2462v1 (2014), for the same form as it is used in practice: $g_{\imath\jmath} = \delta_{\imath\jmath} + 2h\,e^3_{\imath} e^3_{\jmath}$ with the null congruence $e^3$ selected by the Kerr theorem, the property that the null planes of the congruence remain null for the curved metric, and the reading of Kerr's congruence as a stringlike structure. Only the metric form and the plane property are taken from it here; the string interpretation and the material-space speculation that follow are not used.
- H. Stephani, D. Kramer, M. MacCallum, C. Hoenselaers and E. Herlt, *Exact Solutions of Einstein's Field Equations*, 2nd ed. (Cambridge, 2003), for the Kerr–Schild class and for the plane-fronted waves with parallel rays, whose Ricci-flatness is the transverse harmonicity of the single profile function.
- J. Fredsted, "Obtaining consistent Lorentz gauging for a gravitationally coupled fermion," arXiv:1906.12200v3 [physics.gen-ph] (2019), for the external construction recorded in *Lorentz Gauging and the Euler–Lagrange Variation*: the non-commutativity of Lorentz gauging with the Euler–Lagrange variation in the standard vierbein coupling of a Dirac fermion to gravity; the world-index formalism — the frame fields $n_{\imath}$ and $n_{\imath i}$, the matrices $M_{\imath}$ and $N_i$ with their Dirac-like algebra, and the covariant derivative carrying the explicit Levi-Civita connection — in which the two procedures commute; and the geometry of that formalism, in which the frame is covariantly constant, the connection is thereby solved in terms of the metric, its curvature is minus the Riemann tensor, and the gravitational action remains the Einstein–Hilbert one. Cited as an external claim; the source's equations were recomputed here, and the formalism is not adopted.
- J. Fredsted, "Spinor fields without Lorentz frames in curved spacetime using complexified quaternions," arXiv:0811.1357v4 [math-ph] (2009), for the external construction recorded in *An External Claim That the Bundle Basis Is Biquaternionic*: a coordinate-covariant and locally Lorentz invariant formalism in which the basis $s_{\imath} \in (\mathbb{C}\otimes\mathbb{H})_-$ is biquaternionic, the metric is the polar form $g_{\imath\jmath} = \langle s_{\imath}, s_{\jmath}\rangle$, and a single algebra-valued connection $\omega_{\imath}$ carries both the local $\mathrm{U}(1)$ freedom and the Lorentz freedom. Cited as an external construction that reproduces the frame route of this article in the source's notation; the corpus does not adopt it.
- L. Parker and D. Toms, *Quantum Field Theory in Curved Spacetime: Quantized Fields and Gravity* (Cambridge, 2009), for the spinor covariant derivative, the Dirac equation on a curved background and its squared Klein–Gordon form.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984) and Vol. 2 (Cambridge, 1986), for the two-component calculus and the tetrad and spin-connection formalism in the Lorentzian case.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for spin structures on manifolds and the topological obstruction to spinor fields.
- W. Gordon, "Zur Lichtfortpflanzung nach der Relativitätstheorie," *Annalen der Physik* **72** (1923) 421–456, for the effective metric of a dielectric medium.
- Ulf Leonhardt and Thomas G. Philbin, "General relativity in electrical engineering," *New Journal of Physics* **8** (2006) 247, for the modern transformation-optics interpretation of a medium's effective geometry.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 18 and 33, for the complex structure of spacetime and for the two-component formulation of curved geometry.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic treatment of gravity in the same rotor language used here.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a related biquaternionic approach to complexified geometry and its limits.
- A. Waser, "Biquaternion Relativity — Gravitation as an Effect of Spatial Varying Speed of Light" (self-issued, issued 1 January 2011, 8 pp.), for the instance of a spatially stretched varying-$c$ metric recorded in *What the Restricted Class Cannot Do*: the profile fitted to Newton's law, the Schwarzschild line element obtained from its first-order truncation, and the programme's claims (the equation of motion with perihelion precession, the gravitational redshift, free transverse gravitation waves, and the screened field of a point charge). A self-issued preprint with no journal, DOI or arXiv identifier; cited for the construction and its own claims, with its curvature recomputed here so that the truncated profile and the profile the author derives are distinguished.
- C. Castro and M. Pavšič, "The Extended Relativity Theory in Clifford Spaces" (review, 8 July 2004), for the arena alternative of the section *The Arena Alternative: Algebra Valued Coordinates*: Clifford-valued coordinates, the generalized interval, the polyvector bosonic $p$-brane action, the relativity of the signs, and the maximal-acceleration programme.
- E. P. J. de Haas, "Biquaternion Formulation of Relativistic Tensor Dynamics," arXiv:1401.4470v1 [physics.gen-ph] (2013), for the external claim recorded in *An External Claim of One Tensor Language, and What It Does Not Supply*: one biquaternion tensor calculus carrying both the antisymmetric tensor dynamics of electrodynamics and the symmetric tensor dynamics of relativity. Cited as a representational result, with no field equation for the frame or the connection.
- D. J. Cirilo-Lombardo, "Algebraic structures, physics and geometry from a Unified Field Theoretical framework," arXiv:1411.5493v3 [hep-th] (2015), for the external claim recorded in *An External Claim That the Bundle Basis Is Biquaternionic*: the principal fibre bundle $P(G,M)$ whose basis is biquaternionic, its structural group and its three fundamental tensors, and the dictionary that carries its $2\times2$ matrix $Q$ to the corpus's biquaternion. Cited for the claim that the basis is biquaternionic and for its translation; the bundle's geometry — the G-structure, the reduced tangent bundle, the torsion-induced sign — is recorded as a claim in *The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap*, and the source's invariant-metric assertion is not reproduced.
