# __Why Biquaternions?__

## Introduction

An element of the biquaternion algebra holds eight real numbers. The claim of this article is that this one algebra writes three bodies of physics — relativity, wave mechanics, and the hydrodynamics of the Dirac field — with one product, and that the physical content of the corpus is that product applied at successive levels.

The claim is about pertinence, not about novelty. The framework predicts no number that the standard formalism does not predict, and [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html) records the parity domain by domain. What the algebra offers instead is economy of one specific kind. One element is the point, one element is the field, one element is the derivative, and the multiplication is the algebra's own. No matrix, no column, no minimal ideal, no projector and no basis enters the equations, and an array appears only as a display of an element.

The economy appears first in relativity, where the signature of spacetime is a fact about $i^{2}$ and the metric is read off the multiplication table. It appears next in wave mechanics, where the Schrödinger and Klein–Gordon equations are one equation read at two speeds. It pays best in the Dirac field, where the spin fluid that Takabayasi, Bohm and Hestenes each built by hand comes out as a factorisation of one element.

The article follows that order. It sets out the algebra, then relativity, then wave mechanics, then the Dirac field. It then compares the Dirac result with what the other traditions found, states what the algebra reaches and where it stops, and names the price. The strongest objection — that this is a reformulation and nothing more — is answered last, because it can only be answered after the account of what the reformulation does.

## The Algebra

### Eight real coordinates

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$. A point is an element

$$
\tilde Q=Q_t e_t+\vec Q=Q_t e_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
$$

with the four coefficients complex. Writing each as a real part plus $i$ times a real part gives eight real parameters, and the split of those eight is the framework's first structural statement. The four $q_\mu$ are the coefficients of $e_\mu$; the four $q'_\mu$ are the coefficients of $ie_\mu$. The prime marks the parameter that carries the $i$.

The basis multiplies as the quaternions do, with $e_t=1$ and

$$
\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t,
\qquad
\vec e_x\vec e_y=\vec e_z,
\qquad
\vec e_y\vec e_z=\vec e_x,
\qquad
\vec e_z\vec e_x=\vec e_y,
$$

and cyclically with the opposite sign in the reverse order. Every product in the corpus is this product. There is no second multiplication, and there is no object in the equations below that is not an element of this algebra or a number.

### One unit

The four coefficients are lengths, and they share one unit. That is the content of the temporal identification $e_t=1$: the temporal unit is the identity, so the temporal coefficient is written on the same footing as the three spatial ones and no constant stands between them. The corpus therefore writes $r'_t$ where the standard formalism writes $ct$, and the four-position is one element in one unit ([The Temporal Dimension: Why the Temporal Unit Is the Identity](the-temporal-dimension-why-the-temporal-unit-is-the-identity.html)).

This is a bookkeeping decision with a consequence. Because the temporal direction is $ie_t$ on the material sector, the temporal coefficient enters every square as $-{r'_t}^{2}$, and it does so without a sign placed by hand.

### Two sectors

Every element is the sum of an anti-Hermitian part and a Hermitian part,

$$
\mathbb{B}=\mathbb{B}_{\Phi}\oplus\mathbb{B}_{\Psi},
$$

and the two parts are the material sector and the informational sector ([The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html)). The division is exhaustive and unique: an element has one of each, and nothing is left over.

The sectors do the two jobs that physics needs done. The material sector carries the spacetime directions, the gradient, the four-velocity and the electric part of a field strength. The informational sector carries the observables, the magnetic part of the field strength, and the states, which are its positive elements of trace one and form the Bloch ball ([Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html)). An equation of motion is then one sector acting on the field by left multiplication, and the reading of the result is the other sector's business. That is the mechanism behind the two writings of the Schrödinger equation below.

## Relativity

### The interval is a norm

The interval between two nearby points is the quaternionic norm of the displacement:

$$
ds^{2}=\langle d\tilde R_{\Phi}\rangle_{\natural}
=d\tilde R_{\Phi}d\tilde R_{\Phi}^{\natural}
=(i\,dr'_t)^{2}+dr_x^{2}+dr_y^{2}+dr_z^{2}
=-d{r'_t}^{2}+dr_x^{2}+dr_y^{2}+dr_z^{2}.
$$

The Lorentzian minus is $i^{2}$. Nothing else supplies it. The norm is the algebra's own multiplicative form, the product of an element with its quaternion conjugate, so the interval is not an extra quadratic form imposed on the space; it is the form the multiplication already defines.

The series carries one metric on this account,

$$
\delta_{\mu\nu}=(1,1,1,1),
$$

diagonal with all four coefficients $+1$, the matrix of the sum of squares. It is the same in both frames, and it is read off the multiplication table rather than postulated ([The Unit Metric in the Biquaternion Universe](the-unit-metric-in-the-biquaternion-universe.html)). No index is raised, and the Lorentzian minus appears once, in the square of the temporal direction, instead of being carried by the metric and remembered at every contraction.

### The Lorentz group is the norm's group

A Lorentz transformation is a rotation in the complexified space, not a matrix acting on a column ([The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html)). A unit element $\tilde U$ acts on an element by $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{\natural}$, and the action preserves the norm. The norm is a central scalar, so it passes through the two factors: $\langle\tilde U\tilde Q\tilde U^{\natural}\rangle_{\natural}=\tilde U\tilde Q\tilde Q^{\natural}\tilde U^{\natural}=\langle\tilde Q\rangle_{\natural}$ when $\langle\tilde U\rangle_{\natural}=1$.

The converse is the more interesting direction. Ask which group the algebra forces when the norm is the structure to be preserved, and the answer is the Lorentz group, with the rotor description recovered as the coordinate form of the automorphisms ([The Lorentz Group as Biquaternion Norm Automorphisms](the-lorentz-group-as-biquaternion-norm-automorphisms.html)). The Lorentz group is therefore not an input whose invariance of the equations must be checked afterwards. It is the group of the one form the algebra has, and the invariance is a property of the multiplication.

The same mechanism gives the kinematics. The four-velocity is

$$
\tilde V_{\Phi}=\gamma(ic\,e_t+\vec v),
\qquad
\tilde V_{\Phi}\tilde V_{\Phi}^{\natural}=-c^{2},
$$

so the mass-shell condition, the four-acceleration constraints and the four-force are statements about one element and its norm, and the classical mechanics of a particle is a chapter of the same book ([Relativistic Mechanics in Biquaternionic Form](relativistic-mechanics-in-biquaternionic-form.html)).

### Maxwell in one equation

The potential is one element $\tilde A_{\Phi}$, the field strength is one element

$$
\tilde F=i\sqrt{\epsilon}\,(\vec E+ic\vec B),
$$

and the four Maxwell equations are one equation,

$$
\tilde\nabla_{\Phi}\tilde F=-\sqrt{\mu}\,\tilde J_{\Phi},
$$

with the source one element as well ([Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html)). Read on the coefficients, the one equation is four: the scalar part of the product carries the two divergence equations and the vector part the two curl equations. The reading is a decomposition of a product into its types, not a separation of the equation into four equations that must be solved together.

The wave operator comes free. The product of the gradient with its quaternion conjugate is central and scalar,

$$
\tilde\nabla_{\Phi}(\tilde\nabla_{\Phi})^{\natural}=\Box_{\Phi},
$$

so $\Box_{\Phi}$ multiplies each coefficient and mixes no two of them. Applying the conjugate gradient to the Maxwell equation gives the wave equation for $\tilde F$ and, at the same stroke, the compatibility condition on the source. The left side is a pure vector, so the scalar part of $(\tilde\nabla_{\Phi})^{\natural}\tilde J_{\Phi}$ has to vanish, and that condition is the continuity of the current. The constraint is the scalar part of the same product, not a separate axiom.

The pattern is worth naming, because it repeats at every level. One element on the left, one element on the right, one product between them, and the physics is the reading of the product's types.

## Wave Mechanics

### The Schrödinger equation in two writings

The Schrödinger equation is

$$
i\hbar c\,\frac{\partial}{\partial r'_t}\tilde\Xi=\tilde H_{\Psi}\tilde\Xi,
\qquad
\tilde H_{\Psi}=h_t e_t+i\vec h_{\Psi}\in\mathbb{B}_{\Psi},
\qquad
\tilde\Xi\in\mathbb{B},
$$

with the Hamiltonian an element of the informational sector and the state an element of the full algebra ([The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html)). The Hamiltonian is Hermitian, so the evolution operator $\exp(-i\theta_{\mathrm{evo}})$ is unitary in the algebra's own sense, and no Hilbert space is posited for it.

The angle is $\theta_{\mathrm{evo}}$, the scalar part of $\tilde H_\Psi$ times the interval over $\hbar\,c$: the generator is anti-Hermitian, so its scalar part is purely imaginary and the angle is real.

Dividing by the central unit $i\hbar c$ gives a second writing of the same equation,

$$
\frac{\partial}{\partial r'_t}\tilde\Xi=\frac{1}{\hbar c}\tilde H_{\Phi}\tilde\Xi,
\qquad
\tilde H_{\Phi}=-i\tilde H_{\Psi}\in\mathbb{B}_{\Phi}.
$$

The division is always possible because $i$ is central, and its effect is to move the generator from one sector to the other. The first writing names an observable, an energy in the informational sector. The second names a generator, an anti-Hermitian element of the material sector. They are one equation, and the pair of elements they exhibit is the mirror pair of the framework ([Mirror Biquaternions and the Phy–Psy Switch](mirror-biquaternions-and-the-phy-psy-switch.html)).

That is what the sector split buys at this level. The two things a quantum equation must carry — a self-adjoint observable and an anti-Hermitian generator — are the two sectors of one element, and the centrality of $i$ is what converts one into the other exactly.

### The Klein–Gordon equation

The relativistic scalar equation is the same product squared:

$$
\left(\tilde\nabla_{\Phi}(\tilde\nabla_{\Phi})^{\natural}-k_m^{2}\right)\tilde\Xi=0,
\qquad
\tilde\nabla_{\Phi}(\tilde\nabla_{\Phi})^{\natural}=\Box_{\Phi}=\Delta_{\Phi}-\frac{\partial^{2}}{\partial {r'_t}^{2}},
$$

with $k_m=mc/\hbar$ ([The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html)). Since $\Box_{\Phi}$ is central and scalar, the one equation is the same equation for each of the four coefficients, and no coefficient is mixed with another. The second order is a product of two first-order operators, not a postulate about the wave equation.

The two equations of this section are one equation in two regimes. The Schrödinger equation is first order in $r'_t$ and singles out one branch; the Klein–Gordon equation is second order and keeps both branches, which is why the negative-frequency sector exists at all and why the hole theory of §*Antimatter* has something to talk about.

### The polar word and the Madelung pair

Every element off the zero-divisor cone factors into four pieces,

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

a scale, a central phase, a boost and a spatial rotor ([The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html)). The derivative of the word separates into four brackets with no remainder, and in the scalar case the four collapse to two: a continuity equation for the density and a Hamilton–Jacobi equation with a quantum potential. That pair is Madelung's, and its relativistic form is the spin-zero case of Takabayasi's hydrodynamics ([The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html)).

The scalar pair closes because there is nothing else to close. A scalar field has no frame to vary: its word is a scale and an angle, so its derivative has two brackets and the equation relates them. The Dirac field has four factors, and the four brackets are the subject of the next section.

## The Dirac Field

### One element, one derivative

The Dirac field is one element $\tilde\Xi$ with four complex coefficients. That is the count the four-component column carries, and the difference is the object rather than the count: there the four numbers are entries of a column that a matrix multiplies, here they are the coefficients of an element that the algebra multiplies.

The equation is the chiral pair

$$
\tilde\nabla_{\Phi}\tilde\Xi_{R}=k_m\tilde\Xi_{L},
\qquad
(\tilde\nabla_{\Phi})^{\natural}\tilde\Xi_{L}=k_m\tilde\Xi_{R},
$$

as the corpus writes it ([The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html)). The derivative multiplies on the left, and a product takes the value — the side — of its right factor, so a left multiplier keeps the value of what it multiplies. The derivative therefore cannot carry one part of the field into the other, and read as two equations for two independent fields the pair forces both to vanish. The catalogue records the reason as obstruction O22: multiplication is chirality-blind ([What the Biquaternion Algebra Cannot Do](what-the-biquaternion-algebra-cannot-do-a-catalogue-of-algebraic-obstructions.html)).

The pair is a factorisation of one equation, and the Dirac article draws the consequence. In momentum space the second part is the first multiplied on the left, $\tilde\Xi_{L}=(i/k_m)\tilde K_{\Phi}\tilde\Xi_{R}$, and the product of the operator with its conjugate returns the wave operator. The two letters name the two factors of one equation.

Where the other side of the multiplication does appear is the mass, and only there. To exchange the two parts by a multiplication, one multiplies on the right by a unit $i\vec v$ with $\vec v$ perpendicular to the axis. The coefficient conjugation does the same job. Either way the exchange sits on the side of the mass and never on the side of the derivative. A derivative that carried the field out of its part would have to stop being a multiplication by an element.

### The word and its four brackets

With the field written in the polar word, the derivative takes the form

$$
\frac{\partial\tilde\Xi}{\partial R_\mu}
=\tilde\Xi\left[\frac{1}{2}\frac{\partial\ln\rho}{\partial R_\mu}
+i\frac{\partial\theta_{\mathrm{pha}}}{\partial R_\mu}
+\tilde u_{\mathrm r}^{-1}\Bigl(\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu}\Bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\frac{\partial\tilde u_{\mathrm r}}{\partial R_\mu}\right],
$$

and the four brackets are of four different types.

| Bracket | Type | Zero when |
|---|---|---|
| $\tfrac12\partial_\mu\ln\rho$ | real central scalar | the density is constant |
| $i\,\partial_\mu\theta_{\mathrm{pha}}$ | central imaginary | the angle is constant |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | the boost is constant |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | the rotor is constant |

The types are the four transport laws of the fluid. The first is the continuity equation for the density. The second is the guidance equation, since the gradient of the phase is the momentum element $\tilde K_{\Phi}=\tilde\nabla_{\Phi}\theta_{\mathrm{pha}}$. The third is the transport of the velocity, which is the logarithmic derivative of the boost, the element whose inverse square is the four-velocity. The fourth is the transport of the spin direction, $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$.

### The current and the spin

The current and the spin read different factors, and this is the most compact statement the algebra makes about the field.

$$
\tilde V_{\Phi}=ic\,\tilde U_{\Psi,\mathrm b}^{-2},
\qquad
\tilde J_{\Phi}=\rho\tilde V_{\Phi},
\qquad
\tilde S_{\Psi,\mathrm{sp}}=\rho\frac{\hbar}{2}i\,\hat s,
\qquad
\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}.
$$

The velocity is the inverse square of the boost. The spin direction is the rotor's image of the declared axis. The scale multiplies both. The phase appears in neither, and it is read only by the argument of the norm, which is $2\theta_{\mathrm{pha}}$.

So the three data of the fluid are three factors of one element, and the reading is the only step. There is no separate velocity field to be kept consistent with a separate spin field: a factor cannot disagree with its partner in a product. That is the structural gain of the algebra at this level, and it is the reason the Dirac level is where the framework earns its place.

### The Gordon split

The current of a solution splits into a convection part and a spin part,

$$
j_\mu=j^{\mathrm{conv}}_\mu+j^{\mathrm{spin}}_\mu,
$$

the first the orbital current of the momentum and the second the divergence of a spin density ([The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html)). The second term fixes the tree-level gyromagnetic factor at $g=2$, and its radiative correction is the anomalous moment.

The algebra writes the split without a spinor bilinear list. The current is the pairing of the field with the element the generator carries into it, $j_\mu=\bar{\tilde\Xi}\,i e_\mu\tilde\Xi\,\vec e_{\nu(\mu)}$, a scalar part of a product of elements. The algebra also says where the two terms sit. The convection term is the central direction, and the spin term is the bivector direction, with its magnetic part in the informational sector. The identity holds on solutions because the equation is used once for the field and once for its adjoint, and the mass divides both terms, which is why the covariant form needs $m\neq0$ and the massless case has its own reading.

### The vorticity and the nodal set

The velocity of the Dirac field is a unit element squared, not a gradient, so its one-form is not closed in general. The obstruction is the vorticity 2-form

$$
\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu},
$$

which is the antisymmetrised gradient of the frame element and vanishes exactly where the frame is constant ([The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html)). A spatially varying rapidity is enough to make it nonzero.

The frozen-frame sector is therefore the scalar sector: freeze the frame and the flow becomes a gradient flow, which is the Madelung flow of §*The polar word and the Madelung pair*. The Dirac field leaves that sector as soon as its rapidity or its axis varies, and the vorticity measures how far.

Where the field vanishes the story changes, and the algebra states the change exactly. On the nodal set the polar word fails, and around a nodal line the circulation is quantised:

$$
\oint\vec v\cdot d\vec l=\frac{h}{m}n,
$$

with $n$ the degree of the phase map, independent of the loop's shape ([The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html)). The charge is an object of the algebra because it is the winding of the field into the central unit circle, and the phase is only a coordinate on that circle.

## The Spin Fluid, and the Convergence

### Takabayasi

In 1952 and again in 1957 Takehiko Takabayasi showed that the Dirac field, with the spinor and the matrices suppressed, is exactly a relativistic hydrodynamics of a spinning fluid. The system has four equations: a continuity equation for a density, a guidance equation of Hamilton–Jacobi form with a spin-dependent quantum potential, a transport equation for the velocity field, and a transport equation for the internal angular momentum, which is the precession of the spin. Together with normalisation and single-valuedness, they determine a solution of the Dirac equation up to a global phase. That is the Takabayasi–Hestenes equivalence.

The four brackets of §*The word and its four brackets* are the four equations, one for one, in the numbering of his 1957 paper. The scale bracket is the continuity equation for the density, (1′). The phase bracket is the guidance equation, (3′), whose gradient is the momentum element. The boost connection is the velocity transport, (11′), the Euler-type equation for the velocity field. The rotor connection is the spin transport, (12′), the precession of the spin direction. The correspondence is the factorisation itself: the four laws are the four types of the four brackets.

### Bohm, Hestenes, and the others

The de Broglie–Bohm programme found the same structure by another route. Bohm's 1952 papers gave the non-relativistic guidance equation; the relativistic extension with spin is Bohm, Schiller and Tiomno in 1955; Holland's *The Quantum Theory of Motion* of 1993 records the polar variables, the spin transport and the difficulties in one place. The difficulties are the same three the algebra exhibits: the velocity is a bilinear and not a tangent to a trajectory, the spin orientation is underdetermined by the guidance equation, and a current read as a flow meets the speed-of-light problem.

Hestenes found the system a third time, in an algebra rather than in a spinor. The Dirac field is a density times an angle times a rotor, the Dirac equation becomes a condition on the rotor, and the velocity and spin are the rotor's images of a fixed time direction and a fixed spatial direction. That is the same factorisation as the polar word, with the operators written as real Clifford elements instead of biquaternions.

Around these three there is a second group, convergent on the object rather than on the fluid. Daviau writes the Dirac equation for an element with the mass carrying a conjugation. Clifford analysis treats the Dirac operator as one first-order operator on algebra-valued functions and builds a Cauchy kernel, a Teodorescu transform and a boundary-value theory on it. The algebraic-spinor tradition identifies the column with a minimal left ideal, so that the column, the projector and the ideal are three names for one construction.

### What the convergence is worth

Three languages, one structure. Takabayasi wrote a spinor with matrices suppressed, Bohm a wavefunction with a guidance law, Hestenes a real Clifford algebra with no matrix imaginary unit. The three do not share a notation, and they agree on the fluid, on its spin, on the transport laws and on the non-uniqueness. A convergence of notations is evidence about the structures; a convergence of authors would not be.

The independence must not be overstated. Takabayasi's two papers and Bohm's first paper are of 1952, the relativistic guidance equation is 1955, and Hestenes cites Takabayasi. The convergence lies inside a school that read one equation with one intention, and the agreement is therefore weaker than five unrelated discoveries would be. What remains, and what matters, is that the languages differ and the structure survives the change of language.

The second group converges on the object, and its convergence is stronger in one respect: it is about what the field is, not about what it does. Spacetime algebra, Clifford analysis, Daviau's formulation and the algebraic-spinor tradition all say that the field is one element of an eight-real-dimensional algebra and the derivative one operator of the same algebra. That is the sentence the corpus's Dirac equation is written in.

The two convergences meet here and nowhere else. The carrier is one element; the polar word of that element has four factors; the four brackets of the derivative are the four fluid equations. Takabayasi built the fluid from a spinor, Bohm from a wavefunction, Hestenes from a rotor. In the algebra the fluid is not built: it is read, and the reading is a decomposition of a product.

The non-uniqueness is where the algebra says something the others cannot. Fabbri's *Dirac hydrodynamics in 19 forms* (arXiv:2309.00617, 2023) exhibits nineteen minimal systems of hydrodynamic equations, each equivalent to the Dirac equation. The algebra explains why a family exists, though not why its first tabulation has nineteen members: the four brackets live in four subspaces of different types, and the equation relates them without a canonical rule. Different choices of the closure give different members — a different spin-transport equation, or a different local reparametrisation of the eight real components that keeps the system first order and local. Fabbri's nineteen forms are one tabulation of that family. The framework selects one member because in that member each fluid variable is one factor of the word.

## The Reach and the Ceiling

### Gauge fields

The vector units of the material sector span $\mathfrak{su}(2)$,

$$
\mathrm{SU}(2)=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}\subset\mathbb{B}_{\Phi},
$$

so a gauge field with values in $\mathfrak{su}(2)$ is a connection on the algebra itself, and instantons and solitons follow from the same product ([Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html), [Instantons and Solitons in Biquaternionic Form](instantons-and-solitons-in-biquaternionic-form.html)).

The ceiling is exact and it is stated as a result rather than a hope. The algebra reaches $\mathrm{SU}(2)$ and not $\mathrm{SU}(3)$, so colour with three values is outside the carrier ([The Gauge Group Ceiling](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html)). The weak isospin fits; the strong interaction does not, and no construction inside the algebra supplies the third colour.

### Antimatter

The negative-frequency branch of the Dirac equation is the branch the second-order form keeps, and the algebra resolves it the way quantum field theory does. If the modes commuted the energy would be unbounded below; the anticommutator makes the negative-frequency modes positive-energy antiparticles ([Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html)). The hole theory of 1930 is the historical form of the same statement, and the algebra carries its variables without a separate fermion sea being added ([The Dirac Sea, Hole Theory and Antimatter](the-dirac-sea-hole-theory-and-antimatter-in-biquaternionic-form.html)).

### Thermodynamics

Imaginary time is a coordinate here, not a trick. The material time is $ir'_t$, so the analytic continuation $r'_t\to r'_t+i\beta$ of the KMS condition is a translation along the algebra's own temporal direction, and the strip of the condition is a strip of the coordinate ([The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html)).

The informational sector supplies the states and the entropy. The states are the positive elements of trace one, and the functional $\mathcal{S}(\tilde\varsigma_{\Psi})=-2\,\mathrm{Sc}(\tilde\varsigma_{\Psi}\log\tilde\varsigma_{\Psi})$ vanishes exactly on the null cone, is maximal at the maximally mixed state, and measures the depth of the state inside the future cone ([Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html)). Entropy is then a function of one element, defined by the algebra's own operations.

### Gravity

The framework is flat so far, and the gravitational articles are a programme rather than a result. Linearised gravity and gravitational waves are written in the algebra, with the metric perturbation an element and the harmonic gauge a condition on its product ([Linearized Gravity in Biquaternionic Form](linearized-gravity-in-biquaternionic-form.html), [Gravitational Waves in Biquaternionic Form](gravitational-waves-in-biquaternionic-form.html)). The extension to curved spacetime, and the relation to the tetrad, remain open ([Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html)).

## The Price

### No new number

The framework reproduces and does not predict. The parity list is long and it is the corpus's own: the Bloch ball, the Born rule and the projective update; the interval, the mass shell and the four-force constraints; Maxwell and Dirac as transcriptions; the hydrogen spectrum, the Casimir force, the Unruh temperature and the Bell bounds ([The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html)).

So the objection is correct at the level of numbers, and the answer has to be at another level. What the framework changes is the number of objects a reader must hold at once. Before, the spin fluid is three constructions and a consistency condition; after, it is three factors and a product. Before, the Lorentz group is a group whose invariance is checked; after, it is the group of the one form the algebra has. Before, the Lorentzian minus is a convention declared in each article; after, it is $i^{2}$. None of that is a measurement, and the corpus says so.

### Chirality, and the declared direction

The algebra is blind to chirality. A left multiplication acts alike on both parts of the field, and obstruction O22 says so; no element of the algebra marks one part as left and the other as right. Obstruction O17 says the same about the two parts of any element: their split is not canonical, and the $*$-unitary elements act transitively on the directions a split could use.

A direction must therefore be declared. A frame is declared once, by a unit vector $\vec u$ of the algebra, real and of square $\vec u^{2}=-e_t$, and the declaration is the only datum the exercise adds ([Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html)). The chirality basis operator $-iR_{\vec u}$ returns the two parts, and a different $\vec u$ gives a different split.

This is not a defect of notation, and it is where the framework pays most visibly. The weak interaction distinguishes left from right, so the physics itself contains a direction. In a gamma display that direction sits inside the array, unnamed: the reader cannot tell from the page which axis was spent. Here it is one object, declared once, named on the page and rotatable. The price is that the algebra carries no invariant chirality of its own; the gain is that the declaration is visible and separate from the equation.

### The array and the direction

The Pauli and gamma matrices write a direction on the page, and they write it silently. Exactly one of the three Pauli matrices is real and diagonal, and that is the one that built the idempotents. A triplet with one diagonal member and two off-diagonal members cannot be written without deciding which member it is, so the decision is taken at the moment the arrays are written ([Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html)). The direction then travels: into the root $i\vec e_z$, into the Peirce frame, into the ideal, into the column, into the spinor and into the gamma set, and every later sentence about "the third component" or "the upper block" inherits it.

The coefficient array writes none. Its diagonal basis operators are the four squares, $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$ and $\vec e_z\vec e_z$, one per unit, and a permutation of the three spatial units permutes them without changing the shape of the array. No slot is privileged, because no slot was chosen.

This is also where the difference between $1+3$ and $2+2$ is settled. The biquaternion is scalar plus vector by its own structure: one coefficient on the time unit and three on three equal spatial units. The split of the algebra into two copies of $\mathbb{C}^2$ is a display the algebra does not carry, admitted only when the article that prints it declares the missing piece ([Conceptual Conventions](conceptual-conventions.html)). The bispinor's left and right are intrinsic to the bispinor, and the two structures are different rather than two packagings of one. The $2+2$ arises here only from a Peirce choice, an idempotent built from a root $i\vec u$, and that choice imports the direction $\vec u$. The $1+3$ is the structure the algebra has, and it is the one that matches a space with three equal directions.

The consequence for physics is the one drawn in §*Chirality, and the declared direction*. The weak interaction distinguishes left from right, so chirality is physics and not bookkeeping; but the algebra supplies none of its own, so a direction must be declared, once, and named. A display that writes the $2+2$ has already declared it, and has not said so.

### The cone, and where the reading stops

The polar word exists on the $N$-regular set, the elements with $\langle\tilde\Xi\rangle_{\natural}\neq0$. The excluded set is larger than the nodal set: a part of definite value lies on the cone at every amplitude, and a one-sided plane wave has vanishing norm everywhere while the field itself is nowhere zero.

What fails there is the reading and not the equation. The pair, the current and the spin are statements about the element and need no word, and the two-factor decomposition $\tilde\Xi=\tilde\Xi_{H}\tilde\Xi_{0}$ into a positive semidefinite part and a partial isometry is defined on every element ([The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html)). The equation does not stop on the cone; the description of the element in eight named coordinates stops.

One contrast must be stated, because it is easy to carry across from the scalar case. For the Schrödinger equation the flow is left multiplication by an element, the norm is multiplicative, so the cone is preserved and a field is a unit at every event or at none ([The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html)). The Dirac equation is not of that kind, and the reason is the one already given: the mass couples the two chiral pieces. A field with one piece alone does not keep one piece alone, and the two pieces are rank-one elements of independent profiles whose sum is generally of rank two.

A check fixes the statement. In the $2\times2$ image the modulus of the quaternionic norm is the modulus of the determinant, and with the two chiral pieces in the two columns the determinant is the product $\chi\varphi$. Take $\chi$ a Gaussian packet of width $2$ and $\varphi=0$ at $t=0$, on a periodic grid of $512$ points spanning $40$, with $k_m=1$ and step $5\times10^{-4}$, evolved by the $1+1$ chiral pair, $\partial_t\chi=ic\,\partial_x\chi-im\varphi$ and $\partial_t\varphi=-ic\,\partial_x\varphi-im\chi$. The modulus of the determinant is $0$ at $t=0$, $0.196$ at $t=0.2$ and $0.369$ at $t=0.4$. Halving the step moves the last two by less than $10^{-8}$, doubling the grid moves them by less than $2\times10^{-5}$, and $k_m=0$ leaves the value at $0$ for all time.

The rise is the mass, and that is obstruction O22 read dynamically. A term carried on the right is what moves a field between the pieces; the derivative is carried on the left and moves the field within one piece only. So the cone is not carried by the flow.

So the domain of the word is an algebraic condition, checked at each point. At each point either the norm is nonzero and the eight variables exist, or it is zero and the element is a zero divisor.

## Open Questions

1. **Empirical contact.** Which quantitative prediction distinguishes the framework from standard physics, and which structure produces the number? The corpus states this as the central question and does not answer it.

2. **The mass term and the side it acts on.** The exchange of the two parts of the field is carried on the right, by a unit or by the coefficient conjugation, and the mass is its only home. Whether that side has a dynamical meaning beyond the mass, and how it meets the weak interaction, is open.

3. **The conserved current of a general field.** The bilinear $i\tilde\Xi\tilde\Xi^{*}$ is the current with its spatial part reversed, because the star conjugation fixes the boost and inverts the rotor. Which object is conserved on solutions of the general field is open, and the polar article records it as the first question of the polar form.

4. **A closing condition for the four brackets.** Whether a second structure, a transport equation for the rotor of the kind the classical-spin literature carries, closes the system canonically is open. Fabbri's nineteen forms are the map of the possibilities, and no member of the map is canonical.

5. **Colour.** The algebra reaches $\mathrm{SU}(2)$ and not $\mathrm{SU}(3)$. Whether a larger carrier, or a tensor construction over the algebra, restores three colours without losing the economy of this one, is open.

6. **Curved spacetime.** The framework is flat. The tetrad form of the gradient, the coupling to curvature, and the relation to general relativity remain open.

7. **Quantisation of the factorisation.** The polar word is a classical factorisation of the field. Which part of it survives quantisation, and whether the four brackets become operators with a non-trivial commutator algebra, is open.

8. **Twistor theory.** Twistor theory works in $\mathbb{C}^{4}$, which is the coefficient space of $\mathbb{B}$, and the congruence twistors of the corpus join the incidence relation to the shear-free congruence ([Congruence Twistors and the Fields They Generate](congruence-twistors-and-the-fields-they-generate.html)). How the biquaternion Dirac equation and the twistor equation relate is open.

## Physical Interpretation

**The one-object interpretation.** The density, the velocity and the spin are factors of one element, and the four brackets of the derivative are the four transport laws. The boundary is that this is a reading of a factorisation and not a new equation: the Dirac equation is unchanged, and the non-uniqueness of the fluid form survives it (§*What the convergence is worth*).

**The carrier interpretation.** The eight-real-dimensional algebra, with the field and the derivative as its elements, is the carrier that the two convergences point to. The boundary is that a convergence of derivations cannot select a carrier: it is evidence that the carrier is natural, not that it is physical. The framework does not claim that nature uses biquaternions; it claims that this algebra is the natural home for the structures the traditions found (§*What the convergence is worth*).

**The sector interpretation.** The material sector carries the spacetime structure and the informational sector the states and observables, and an equation of motion is one sector acting on the field. The boundary is that the two writings of the Schrödinger equation are one equation and not two dynamics (§*The Schrödinger equation in two writings*).

**The algebraic-domain interpretation.** The domain of the polar word is the set where the quaternionic norm does not vanish, which is a determinant condition. The boundary is that the domain is not invariant under the flow (§*The cone, and where the reading stops*): what is claimed is the algebraic form of the condition, not its conservation.

## Summary

The biquaternion algebra writes relativity, wave mechanics and the Dirac fluid with one product, and that is its claim to pertinence.

Relativity is a chapter of the multiplication table. The interval is the quaternionic norm, the Lorentzian minus is $i^{2}$, the metric is the unit metric read off the table, the Lorentz group is the group of the norm, and Maxwell's four equations are one equation whose types are the four.

Wave mechanics uses the same product at both speeds. The Schrödinger equation is left multiplication by a Hermitian element of the informational sector, and its second writing multiplies by the anti-Hermitian mirror of that element; the Klein–Gordon equation is the product of the gradient with its conjugate, minus the mass term. The polar word turns the scalar case into the Madelung pair.

The Dirac field is where the algebra pays. One element, four complex coefficients, one derivative. The derivative multiplies on the left and cannot tell the two parts apart, so the exchange of the parts is carried on the right, and the mass is its only home. The polar word has four factors, its derivative has four brackets of four types, and those four brackets are Takabayasi's continuity, guidance, velocity transport and spin transport. The velocity is the inverse square of the boost, the spin direction is the rotor's image of an axis, and the phase is read by neither. The Gordon split, the vorticity as the frame's curl, and the quantised circulation around a nodal line all come out of the same element.

The convergence outside supports this without proving it. Takabayasi, the de Broglie–Bohm programme and Hestenes found the same fluid in three different languages, and spacetime algebra, Clifford analysis, Daviau and the algebraic-spinor tradition found the same object. The convergence is of notations and not of independent authors, which is the weaker and the honest form, and the algebra is the place where the object of the second group produces the structure of the first.

The reach is broad and the ceiling is real. Gauge fields with $\mathfrak{su}(2)$ values, antimatter through the anticommutator, KMS with imaginary time as a coordinate, entropy of the informational sector, and a gravitational programme. No three colours, no curved spacetime yet, and no new number.

The price is stated. The algebra is chirality-blind, so a direction must be declared, and the weak interaction is the physics that requires it. The array display is the other face of the same fact: the gamma set writes a direction and never names it, while the coefficient array writes none, and the $1+3$ the algebra carries is the structure that matches a space with three equal directions. The polar word fails on the zero-divisor cone, the equation continues there, and the flow does not preserve the cone.

The strongest objection is that this is a reformulation. It is, and the corpus accepts it. What the reformulation delivers is one object and one product at every level, a metric read off the table, a group forced by the norm, a sign that is a square, and a fluid that is a factorisation rather than a construction. Whether a prediction follows is the open question, and it is open in the corpus as it is open here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, eight real dimensions |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Basis, $e_t=1$, $\vec e_\eta^{2}=-e_t$, products cyclic |
| $i$ | Central scalar imaginary |
| $q_\mu$, $q'_\mu$ | Real and imaginary parts of the coefficient $Q_\mu$; the prime marks the parameter that carries the $i$ |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde Q^{\natural}$ | Quaternion conjugate |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm |
| $\mathrm{Sc}$ | Scalar part, the coefficient of $e_t$ |
| $\tilde\nabla_{\Phi}$ | The gradient, the Dirac operator of the material frame |
| $\tilde\nabla_{\Phi}(\tilde\nabla_{\Phi})^{\natural}=\Box_{\Phi}$ | The wave operator, central and scalar |
| $k_m=mc/\hbar$ | Mass wave number |
| $r'_t$ | Material time coordinate, with $e_t=1$ and temporal direction $ie_t$ |
| $R_\mu$ | The four coordinates of the material frame; indices stay low |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word: scale, phase, boost, rotor |
| $\rho$ | Scale of the word, the modulus of the norm; $\langle\tilde\Xi\rangle_{\natural}=\rho e^{2i\theta_{\mathrm{pha}}}$. Not the Hermitian density $\mathrm{Sc}(\tilde\Xi\tilde\Xi^{*})$, which stays positive on the cone |
| $\tilde U_{\Psi,\mathrm b}$ | Boost factor, Hermitian positive |
| $\tilde u_{\mathrm r}$ | Spatial rotor, real |
| $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | Four-velocity, $\tilde V_{\Phi}\tilde V_{\Phi}^{\natural}=-c^{2}$ |
| $\tilde J_{\Phi}=\rho\tilde V_{\Phi}$ | Current |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction |
| $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ | Spin element |
| $\tilde K_{\Phi}=\tilde\nabla_{\Phi}\theta_{\mathrm{pha}}$ | Momentum element: four-momentum divided by $\hbar$ |
| $\tilde F=i\sqrt{\epsilon}(\vec E+ic\vec B)$ | Field strength element |
| $\tilde\varsigma_{\Psi}$ | State of the informational sector, positive and of trace one |
| $\ast$ | Star conjugation |
| $c$ | Speed of light in the medium |

## Further Reading

The corpus articles, in the order in which this article uses them:

- [A Brief History of Biquaternions in Physics](a-brief-history-of-biquaternions-in-physics.html). The algebra before the framework, its displacement, and its return.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html). The core proposal, the two sectors, and the eight coordinates.
- [Algebra and Element Conventions](algebra-and-element-conventions.html). The basis, the coefficient split, and the two sectors.
- [The Unit Metric in the Biquaternion Universe](the-unit-metric-in-the-biquaternion-universe.html). The one metric, read off the multiplication table.
- [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html). The transformation as a rotation of the complexified space.
- [The Lorentz Group as Biquaternion Norm Automorphisms](the-lorentz-group-as-biquaternion-norm-automorphisms.html). The group forced by the norm.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html). The one equation and its four types.
- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html). The two writings and the mirror pair.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html). The wave operator as a product.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html). The chiral pair, the factorisation reading, and the constructions the equation does not need.
- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html). The word, the four brackets, the current, the spin, and the domain.
- [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html). The vorticity, the frozen-frame sector, and the fluid reading.
- [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html). The convection and spin parts, and $g=2$.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html). The cone, the phase winding, and the quantum of circulation.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html). The Madelung pair and its relativistic form.
- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html). The direction an array display writes, and the axis-free display.
- [The Gauge Group Ceiling](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). $\mathrm{SU}(2)$ from the vector units, and why colour is outside.
- [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html). Imaginary time as a coordinate.
- [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html). States, entropy, and the null cone.
- [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html). The anticommutator and the antiparticles.
- [What the Biquaternion Algebra Cannot Do](what-the-biquaternion-algebra-cannot-do-a-catalogue-of-algebraic-obstructions.html). O17 on the declared direction and O22 on the chirality-blindness of multiplication.
- [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html). The parity list, and what a signature would have to be.
- [Conceptual Conventions](conceptual-conventions.html). The status of the $2+2$ split and of the algebra's own structures.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html). The word, its domain and its four factors.
- [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html). The two-factor decomposition that survives on the cone.

The literature:

- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, and "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166 and 180; D. Bohm, R. Schiller and J. Tiomno, "A causal interpretation of the Pauli equation," *Nuovo Cimento Supplement* **1** (1955) 48.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993). The relativistic polar variables, the spin transport, and the underdetermination of velocity and spin.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966; reissued Springer, 2015), and "Local observables in the Dirac theory," *Journal of Mathematical Physics* **14** (1973) 893–905.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003).
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982). The Dirac operator as a first-order operator, and the analytic theory built on it.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Heldermann, 2003). The two-sided quaternionic form of the Dirac equation.
- Claude Daviau, "Équations de Dirac et de Maxwell en algèbre de Clifford," *Annales de la Fondation Louis de Broglie* **39** (2014).
- Luca Fabbri, "Dirac hydrodynamics in 19 forms," arXiv:2309.00617 (2023), and "Dirac theory in hydrodynamic form," arXiv:2303.17461 (2023).
