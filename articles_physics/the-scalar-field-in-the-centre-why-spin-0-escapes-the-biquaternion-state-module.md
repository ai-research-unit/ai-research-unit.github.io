# __The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module__

## Introduction

A scalar field is, in standard relativistic physics, the simplest kind of field: one component at each event, and no axis. A Lorentz transformation moves the event and leaves the value alone,

$$
\xi_{\mathrm{scl}}'(r'_{x})=\xi_{\mathrm{scl}}(x),
\qquad r'_{x}=\Lambda x .
$$

Every other field carries structure that the transformation can act on: the four-vector carries its spacetime index, the Dirac field carries its two labels, and the field strength carries two indices. The scalar carries none, and that is what spin $0$ means.

In the biquaternion framework a state is an element of the algebra $\mathbb{B}$. Its label takes two values, and the state is written $\tilde{Ξ}_{\mathrm{sp},L}$ or $\tilde{Ξ}_{\mathrm{sp},R}$ accordingly; a general element has an L part and an R part, and left multiplication keeps the label. The framework calls the carrier of states the state module; in this article the carrier is the algebra, and a state is an element. The question of this article follows at once: the carrier of states is an element of $\mathbb{B}$ and the left action on it carries spin $\tfrac12$, so where does a spin-$0$ value live, and why is it not a value of that action?

The answer worked out below is that a scalar field takes its value in the **centre** of the algebra, $\mathbb{B}_{C}$, and that it escapes the carrier of states for three reasons that turn out to be one reason seen three ways. The centre is the set of elements fixed by the conjugation action of every rotation. It is a subalgebra, and it is not stable under left multiplication: multiplying a central value by a general element carries it out of the centre. No one-dimensional subspace of $\mathbb{B}$ is carried into itself by every left multiplication, so the trivial action has no carrier. And the trivial action of the rotation subgroup appears in a product of two states, not in a single state. The scalar is a value in the centre, not a value of the state action.

The companion article *The Klein–Gordon Equation in Biquaternionic Form* reached a related conclusion from the equation rather than from the algebra. It found that the second-order scalar equation decouples into four independent scalar equations because the d'Alembertian is central and scalar, that its host is the centre $\mathbb{B}_{C}$, and that the second-order structure does **not** organize itself by the material/informational split of the algebra. The present article supplies the algebraic reason behind that verdict. It shows *why* the centre is the scalar's home, why neither $\mathbb{B}_{\Phi}$ nor $\mathbb{B}_{\Psi}$ can host it as a carrier, and how the sector split should be read when the field is a scalar: not as particle and antiparticle, and not as state and operator, but as the real and imaginary parts of one complex number.

The article is organized as follows. The carrier of states and the spin it carries are recalled first. Then the centre is characterized, by the centralizer computation that fixes it as the rotationally invariant subspace. Then the three obstructions are stated and proved. Then the sector question is settled. Then the scalar field and its equation are written in the centre. A final section records the composite route, in which a scalar is built as a product of two states rather than as an element of the carrier.

The conventions are those of the series: the algebra and the element glyphs of *Algebra and Element Conventions*, the pure states and the spin of *Special Element Conventions*, the operators and the d'Alembertian of *Operator and Calculus Conventions*, the coordinate and the frame of *Frame and Metric Conventions*, the forms and the norms of *Product and Form Conventions*, and the displays of *Matrix Representations Conventions*. They are cited here and not restated.

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation, its mass-term sign, and the sector analysis that this article explains.
- Companion article *The Schrödinger Equation in Biquaternionic Form*, for the state and the central Hamiltonian.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the carrier, the two halves, the Lorentz action, and the invariant forms.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the Dirac field and its scalar bilinears.
- Companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action*, for the material sector, the four-vectors, and the biquaternion norm.
- Companion article *The Informational Sector: States, Observables and Probability*, for the Hermitian sector, the pure states, and the trace formula.

## The Carrier of States and the Spin It Carries

### A State Is an Element

A state is an element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$. Its label takes two values; the element is written $\tilde{Ξ}_{\mathrm{sp},L}$ in the first and $\tilde{Ξ}_{\mathrm{sp},R}$ in the second, and a general element is $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$. Left multiplication keeps the label, and a product takes the label of its right factor. These two facts are the whole of the label's behaviour, and no formula is needed for them.

The L part is stable under left multiplication, so it is a carrier of the left action in its own right, and the left action on it is what this article asks about. The algebra acts on it by left multiplication, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Q}\tilde{Ξ}_{\mathrm{sp}}$, and the action is complex-linear because the scalar imaginary $i$ is central. The carrier is $\mathbb{B}$ itself: a state is an element, and no array enters the description.

Two features are used constantly. First, a state that carries a pure state is a zero divisor. Let $\tilde\Pi(\vec u)$ be a pure state of the informational sector, with $\vec u$ the unit direction the preparation supplies; a state that carries it satisfies $\tilde{Ξ}_{\mathrm{sp}}\tilde\Pi(\vec u)=\tilde{Ξ}_{\mathrm{sp}}$. Then, for nonzero $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp}}(e_t-\tilde\Pi(\vec u))=0$ with $e_t-\tilde\Pi(\vec u)\neq0$, so $\tilde{Ξ}_{\mathrm{sp}}$ is a zero divisor. Second, the pure state carries the direction $\vec u$ and nothing else: under the conjugation action of a rotation it goes to the pure state whose direction is the rotated unit, and a rotation about $\vec u$ fixes it.

### The Left Action Carries Spin One-Half

The rotation subgroup acts on a state by left multiplication, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde r\tilde{Ξ}_{\mathrm{sp}}$, with $\tilde r$ a unit real quaternion. Its generators are $\tilde S_{\Psi,k}$, and the sum of their squares in the algebra is

$$
\tilde S_{\Psi,1}^2+\tilde S_{\Psi,2}^2+\tilde S_{\Psi,3}^2=\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}\,e_t .
$$

The computation is one line from the squares of the generators, $\vec e_k^2=-e_t$; the value was checked by recomputation and is exact.

Left multiplication by a central element is the identity map of $\mathbb{B}$. The left action of the Casimir is therefore multiplication by $\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}$ on every element, and on every irreducible piece of the left action the spin convention gives $s(s+1)=\tfrac34$, hence $s=\tfrac12$. The L part is stable under left multiplication and carries the same Casimir, so its pieces carry $s=\tfrac12$. The carrier of states carries spin one-half.

### No State Is Rotationally Invariant

A state cannot be fixed by every rotation. If $\tilde r\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}$ for every unit real quaternion $\tilde r$, the choice $\tilde r=-e_t$ gives $-\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}$, hence $\tilde{Ξ}_{\mathrm{sp}}=0$. No nonzero state is rotation-invariant.

The pure state carries the direction $\vec u$ that the preparation supplies, and a rotation of the frame carries it to the pure state whose direction is the rotated unit, while a rotation about $\vec u$ fixes it. A rotor of angle $1.1$ about the normalized axis $(0.3,-0.7,0.5)$ sends the direction $\vec e_z$ to $(-0.586,-0.524,0.618)$, a unit vector. The direction is what the preparation supplies, and the rotation moves it.

A scalar field is the opposite. It has no axis, and no rotation may move it. The remainder of the article makes that requirement precise inside the algebra and identifies the unique subspace that satisfies it.

## The Centre and Its Trivial Representation

### The Centralizer of the Rotations

Consider a general element $\tilde{Q}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$ and ask which elements are fixed by the **conjugation action** $\tilde{Q}\mapsto\tilde r\tilde{Q}\tilde r^{*}$ of every rotation. Equivalently, ask for which $\tilde{Q}$ the infinitesimal condition

$$
[\vec e_\nu,\tilde{Q}]=\vec e_\nu\tilde{Q}-\tilde{Q}\vec e_\nu=0,
\qquad \nu\in\{x,y,z\},
$$

holds. Evaluating the first of these with $\vec e_x^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$ and $\vec e_x\vec e_z=-\vec e_y$, one finds

$$
[\vec e_x,\tilde{Q}]=2Q_y\vec e_z-2Q_z\vec e_y,
$$

so $[\vec e_x,\tilde{Q}]=0$ forces $Q_y=Q_z=0$. The condition $[\vec e_y,\tilde{Q}]=0$ then forces $Q_x=Q_z=0$, and together with the first gives $Q_x=Q_y=Q_z=0$. Hence

$$
\boxed{\;
\{\tilde{Q}\in\mathbb{B}:[\vec e_\nu,\tilde{Q}]=0,\ \nu\in\{x,y,z\}\}
=\mathbb{B}_{C}\;},
$$

the **centre** of the algebra. The result was confirmed independently by solving the condition over the eight real coordinates of $\tilde{Q}$: the system has rank six and nullity two, so the solution space is the real two-dimensional subspace spanned by $e_t$ and $ie_t$, as stated.

The algebraic statement is therefore exact: **the elements of $\mathbb{B}$ that are invariant under the conjugation action of the rotation subgroup are precisely the central elements.** The traceless part transforms instead as the adjoint action, so under rotations the algebra separates into the centre, which is spin $0$, and the traceless part, which is spin $1$, while the carrier of states carries spin $\tfrac{1}{2}$. A spin-$0$ field has no alternative but the centre.

### The Centre Is a Subalgebra, Not a Carrier

It matters that the centre is a subalgebra and not a carrier, because that is what separates the scalar from the state structurally. The centre is closed under multiplication, because central elements commute and their product is again central,

$$
(Q_te_t)(R_te_t)=(Q_tR_t)e_t\in\mathbb{B}_{C},
$$

so it is a field isomorphic to $\mathbb{C}$. It is fixed pointwise by quaternion conjugation, hence it is exactly the fixed space of ${}^{\natural}$.

It is **not** stable under left multiplication. For a central element $Q_te_t$ and a general $\tilde{Q}\in\mathbb{B}$,

$$
(Q_te_t)\tilde{Q}=Q_t\tilde{Q},
$$

which lies in the centre only if $\tilde{Q}$ does. Taking $\tilde{Q}$ with a nonzero vector part produces a nonzero vector part in the product, so multiplying a central value by a general element carries it out of the centre. The centre is therefore not a carrier of the left action. It contains no nonzero subspace that the left action preserves.

The centre meets the states only at zero. If a central element $\lambda e_t$ carried a pure state, $\lambda e_t\tilde\Pi(\vec u)=\lambda e_t$, then $\lambda(\tilde\Pi(\vec u)-e_t)=0$; the difference is nonzero and $e_t$ is invertible, so $\lambda=0$. The overlap is the zero element, and this was confirmed by recomputation.

The distinction has a second, more elementary face. A state that carries a pure state is a **zero divisor**, as shown above. A nonzero central element $\lambda e_t$, by contrast, is invertible, with inverse $\lambda^{-1}e_t$. The nonzero elements of the scalar line are invertible; the states are the algebra's zero divisors. They cannot be the same space, and they do not overlap except at zero.

## Three Obstructions, One Reason

The carrier of states cannot host a spin-$0$ field for three reasons, one for each object involved: the carrier, the algebra, and the product of two states.

### No One-Dimensional Carrier

Suppose a one-dimensional subspace is carried into itself by every left multiplication. Choose a nonzero $\tilde{Ξ}_{\mathrm{sp}}$ in it. Then $\tilde{Q}\tilde{Ξ}_{\mathrm{sp}}=\lambda(\tilde{Q})\tilde{Ξ}_{\mathrm{sp}}$ for every $\tilde{Q}$, with $\lambda(\tilde{Q})$ a complex number. The map $\lambda$ is multiplicative, $\lambda(\tilde{Q}_1\tilde{Q}_2)=\lambda(\tilde{Q}_1)\lambda(\tilde{Q}_2)$, and $\lambda(e_t)=1$. From $\vec e_k^2=-e_t$,

$$
\lambda(\vec e_k)^2=-1,
$$

so $\lambda(\vec e_k)=\pm i$ for each spatial direction. From $\vec e_x\vec e_y=\vec e_z$,

$$
\lambda(\vec e_x)\lambda(\vec e_y)=\lambda(\vec e_z).
$$

The product of two numbers each equal to $\pm i$ is $\pm1$, while $\lambda(\vec e_z)$ is $\pm i$. The equation has no solution, and no one-dimensional carrier exists. The check was repeated over all eight sign choices, with no nonzero solution.

The consequence is immediate. A scalar field carries the trivial action: the algebra does nothing to its value. If that value were a carrier of the left action, the carrier would be one-dimensional and invariant. No such subspace exists. The value of a scalar is therefore not a value of the state action. The carrier is not "the carrier with spin $0$" as against "the carrier with spin $\tfrac{1}{2}$": every carrier of the left action is at least two-dimensional and carries spin $\tfrac{1}{2}$. The spin-$0$ value has to be found outside the carrier.

### The Invariant Subspace Is the Centre

If one insists on locating the scalar inside the algebra rather than in a carrier, the centralizer computation settles where. Under the rotation subgroup the algebra separates into spin $0$ and spin $1$. Under the full Lorentz action $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$ there is no nonzero invariant, because each sector is carried into itself and carries the four-vector action; the centre, fixed by the rotations, is carried out of itself by a boost. The only rotationally invariant elements are central. A scalar field, being invariant under rotations, must therefore take its values in $\mathbb{B}_{C}$, and there is nothing else it could take them in.

It is worth stating plainly how the scalar relates to the action that carries the material sector. The four-vectors of $\mathbb{B}_{\Phi}$ transform as $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$; under rotations that action splits into the time component, spin $0$, and the spatial vector, spin $1$. The scalar field does not transform by this rule at all. Its Lorentz transformation is the transformation of its argument, $\tilde{Ξ}'(r'_{x})=\tilde{Ξ}(x)$ with $r'_{x}=\Lambda x$, and no algebraic factor acts on the value. The absence of an algebraic action is the field-theoretic statement of spin $0$, and the centre is the value space in which that absence is natural.

### The Trivial Representation Lives in a Product

There is a third way to see why the scalar is not a value of the state action, and it explains where scalars actually come from. The L part carries the two-dimensional action of one label, the R part the other, and the product of the two contains the trivial action once and the three-dimensional action once under the rotation subgroup. The trivial piece is the product channel; it is not a part of either factor. Under the full Lorentz group the product is the four-vector action, so the rotation-trivial piece is the time component of a four-vector rather than a Lorentz scalar.

The Lorentz scalars come from two pairings. The antisymmetric pairing of two states of one label is invariant, and the mixed pairing of two states of opposite labels,

$$
\mathfrak{b}(\tilde{Ξ}_{\mathrm{sp}},\tilde\xi)=2\,\mathrm{Sc}\!\left(\tilde{Ξ}_{\mathrm{sp}}^*\tilde\xi\right),
$$

is invariant when the second state carries the dual transformation $\tilde\xi\mapsto(\tilde{U}^{*})^{\natural}\tilde\xi$, because the two factors $\tilde{U}^{*}$ and $(\tilde{U}^{*})^{\natural}$ then cancel, $\tilde{U}^{*}(\tilde{U}^{*})^{\natural}=e_t$ for a unit-norm $\tilde{U}$. Both are complex numbers, hence central multiples of $e_t$. A scalar is therefore not an element of the carrier but a pairing of two elements, and the pairing takes its value in the centre.

The four-vector channel is the Hermitian product

$$
H=\tfrac12\left(\tilde{Ξ}_{\mathrm{sp}}\tilde\xi^{*}+\tilde\xi\tilde{Ξ}_{\mathrm{sp}}^*\right)\in\mathbb{B}_{\Psi},
$$

which is Hermitian for every pair, unlike the single product $\tilde{Ξ}_{\mathrm{sp}}\tilde\xi^{*}$. Its scalar part is $\sigma=\mathrm{Sc}\,H$; the physical four-vector is $iH\in\mathbb{B}_{\Phi}$, and $\sigma$ is the coefficient of its time direction. Under a rotation $\sigma$ is unchanged; under a boost it is not, and the next section records the check.

This is the algebraic content of the standard fact that a spin-$0$ object can be built from two spin-$\tfrac{1}{2}$ objects but is not itself one: the trivial action of the rotation subgroup sits in the product, not in either factor. The companion article *The Dirac Equation in Biquaternionic Form* uses the same products when it forms the Dirac current and the Dirac scalar, and the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* develops the pairings and their invariance properties explicitly.

## The Sector Question: Neither $\mathbb{B}_{\Phi}$ nor $\mathbb{B}_{\Psi}$

The framework's central algebraic fact is the split into the anti-Hermitian material sector $\mathbb{B}_{\Phi}$ and the Hermitian informational sector $\mathbb{B}_{\Psi}$. The companion article *The Klein–Gordon Equation in Biquaternionic Form* asked whether the second-order scalar structure organizes itself by this split, and found that it does not: because the d'Alembertian is central and scalar, the split merely separates a complex solution into its real and imaginary parts, giving two $i$-related copies of one real solution space rather than a particle–antiparticle or state–operator pair. The algebra above explains why, and it also says what the split *does* mean for a scalar.

The scalar field's value space is the centre, and the centre meets each sector in exactly one real direction: the real scalar direction $e_t$ lies in $\mathbb{B}_{\Psi}$, and the imaginary scalar direction $ie_t$ lies in $\mathbb{B}_{\Phi}$. A complex scalar $\tilde{Ξ}=\xi_{\mathrm{scl}} e_t$ with $\xi_{\mathrm{scl}}=\xi_{\mathrm{scl},1}+i\xi_{\mathrm{scl},2}$ and $\xi_{\mathrm{scl},1},\xi_{\mathrm{scl},2}\in\mathbb{R}$ therefore splits as

$$
\tilde{Ξ}=\underbrace{\xi_{\mathrm{scl},1}\,e_t}_{\in\,\mathbb{B}_{\Psi}}+\underbrace{\xi_{\mathrm{scl},2}\,ie_t}_{\in\,\mathbb{B}_{\Phi}},
$$

and the sector decomposition of a scalar field is nothing other than the decomposition of a complex number into its real and imaginary parts. This is the precise sense in which the negative verdict of the Klein–Gordon article is forced: the $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$ split cannot carry the particle–antiparticle doubling, because on the scalar line it is the real/imaginary-part split of a single complex number.

The operations that act on that complex number must be kept distinct, and the same distinction settles the sector question completely.

- **Multiplication by $i$** is central and exchanges the sectors, $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$, $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$. On a scalar it maps $\xi_{\mathrm{scl},1}e_t+\xi_{\mathrm{scl},2}ie_t$ to $-\xi_{\mathrm{scl},2}e_t+\xi_{\mathrm{scl},1}ie_t$: it is a quarter-turn of the complex scalar line, exchanging its two real directions.
- **Complex conjugation $\bar{\cdot}$** acts on the coefficients and preserves each sector. On a scalar it maps $\xi_{\mathrm{scl},1}e_t+\xi_{\mathrm{scl},2}ie_t$ to $\xi_{\mathrm{scl},1}e_t-\xi_{\mathrm{scl},2}ie_t$: it is the reflection of the complex line, and it produces the second solution of the second-order equation, $\bar{\tilde{Ξ}}$.
- **Hermitian conjugation ${}^{*}$** is the involution whose eigenspaces define the sectors; it is neither of the other two, and on the centre it agrees with $\bar{\cdot}$.

These are three different maps, but only two distinct actions on the scalar line: the Hermitian star and complex conjugation coincide there, and multiplication by $i$ is the map that acts differently. The sector-exchanging map $i$ is not the conjugate-producing map $\bar{\cdot}$, and reading the conjugate pair $(\tilde{Ξ},\tilde{Ξ}^{*})$ as the sector pair $(\mathbb{B}_{\Phi},\mathbb{B}_{\Psi})$ is precisely the conflation the companion article warns against. The centre makes the distinction visible: complex conjugation has real fixed points in the centre, the direction $e_t$; multiplication by $i$ has none.

## The Scalar Field in the Centre

With the value space fixed, the scalar field is written down at once. A spin-$0$ field of mass $m$ is a function into the centre,

$$
\tilde{Ξ}(r_x)=\xi_{\mathrm{scl}}(r_x)\,e_t,
\qquad
\xi_{\mathrm{scl}}(r_x)\in\mathbb{C},
$$

and it obeys the Klein–Gordon equation in the form of the companion article,

$$
\left(\Box-k_m^{2}\right)\tilde{Ξ}=0,
$$

with $\Box$ the d'Alembertian, central and scalar. Because $\Box$ is central and scalar, it acts coefficient by coefficient, and on a central field the equation is the ordinary complex scalar Klein–Gordon equation

$$
\left(\Box-k_m^{2}\right)\xi_{\mathrm{scl}}=0,
$$

with the biquaternion writing carrying no additional content. This is the honest verdict of the companion article, and the algebra of the present article says why it must be so: there is no axis in the field for any non-central algebraic structure to act on. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The plane-wave solutions exhibit the same point. With the four-position $\tilde R_\Phi$ and the four-wavevector $\tilde P_{\Phi}\,k_{\Phi}$ in the material sector, the phase is the real scalar $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural})/\hbar=\vec k\cdot\vec r-\omega r'_t/c$, and the positive-frequency solution is

$$
\tilde{Ξ}=\xi_{\mathrm{scl},0}\,\exp\!\left(i\,\mathrm{Sc}\frac{k_m\,\tilde{P}_{\Phi}\,\tilde{R}_{\Phi}^{\natural}}{m\,c}\right)e_t
=\xi_{\mathrm{scl},0}\,\exp\!\left(i(\vec k\cdot\vec r-\omega r'_t/c)\right)e_t .
$$

The exponential is central. The mass-shell condition is the biquaternion norm of the four-wavevector,

$$
\langle\tilde P_{\Phi}\,k_{\Phi}\rangle_{\natural}=-\frac{\omega^2}{c^2}+k_x^2+k_y^2+k_z^2 ,
$$

and setting it to the negative constant $-k_m^{2}$ gives the dispersion relation

$$
-\frac{\omega^2}{c^2}+k_x^2+k_y^2+k_z^2=-k_m^{2}
\quad\Longleftrightarrow\quad
\omega^2=c^2\left(k_x^2+k_y^2+k_z^2\right)+c^2k_m^{2},
$$

which is the standard relativistic dispersion relation. It is reproduced here only to record that the scalar field's entire algebraic content is the biquaternion norm of a four-vector, not the action of the algebra on a state. The conserved current $\tilde{J}_{\Phi}$ lies in $\mathbb{B}_{\Phi}$, its scalar component being the imaginary scalar direction, exactly as for the four-current of relativistic mechanics. Here $k_{\Phi}=\frac{k_m\,p}{m\,c}$ is the momentum length.

One structural remark belongs with the equation. The first-order operators of the framework act on states and change their content. The scalar field has no such action. The only operator the scalar equation uses is the central scalar $\Box$, whose square-root structure is a statement about the *operator*, not about the field it acts on. A scalar field is annihilated by a composite of state operators without ever being a state; it is the trivial channel appearing in the composition, not an element of the carrier.

## Scalars from Two States: The Composite Route

The three obstructions say that a scalar is not a value of the state action. They do not say that the states are irrelevant to scalar physics, and it is worth recording how scalars actually appear in the standard model, because the framework reproduces the mechanism.

A Lorentz-invariant scalar built from two states is a product, but not every product is one. If $\tilde{Ξ}_{\mathrm{sp}},\tilde\xi$ are states, the product $\tilde{Ξ}_{\mathrm{sp}}\tilde\xi^{*}$ is an element of $\mathbb{B}$; it is Hermitian only for special pairs, so in general it is not a four-vector. The object that is Hermitian for every pair is the symmetrised product

$$
H=\tfrac12\left(\tilde{Ξ}_{\mathrm{sp}}\tilde\xi^{*}+\tilde\xi\tilde{Ξ}_{\mathrm{sp}}^*\right)\in\mathbb{B}_{\Psi},
\qquad
\sigma=\mathrm{Sc}\,H=\mathrm{Re}\,\mathrm{Sc}\!\left(\tilde{Ξ}_{\mathrm{sp}}\tilde\xi^{*}\right),
$$

and its scalar part $\sigma$ is real. Under a Lorentz transformation the states transform by left multiplication, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{U}\tilde{Ξ}_{\mathrm{sp}}$ and $\tilde\xi\mapsto\tilde{U}\tilde\xi$, so

$$
H\;\longmapsto\;\tilde{U}\,H\,\tilde{U}^{*},
$$

which is the four-vector action on $\mathbb{B}_{\Psi}$; the physical four-vector is $iH\in\mathbb{B}_{\Phi}$. The scalar part $\sigma$ is invariant under the rotation subgroup, where $\tilde U^{*}=\tilde U^{-1}$, but **not** under boosts, where $\tilde U^{*}\tilde U\neq e_t$. The object $H$ is therefore the four-vector channel, and $\sigma$ is the coefficient of its time direction, not a Lorentz scalar; this is the algebraic form of the standard statement that the squared norm of a state is the time component of the four-current, not an invariant.

A check makes the behaviour explicit. Take $\tilde{Ξ}_{\mathrm{sp}}=\tilde\Pi(\vec e_z)$ and $\tilde\xi=\tilde\Pi(\vec e_z)+0.3\,\vec e_x$. A rotation of angle $1.1$ about the normalized axis $(0.3,-0.7,0.5)$ leaves $\sigma$ unchanged, with residual $0$. A boost of rapidity $1.3$ along $\vec e_x$ multiplies $\sigma$ by $\cosh 1.3=1.9709$.

The Lorentz-invariant scalars are instead the two pairings developed in the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. The antisymmetric pairing of two states of one label is invariant, and the mixed pairing of two states of opposite labels is invariant for the reason given above. Both are invariant complex numbers, hence central multiples of $e_t$; the Hermitian channel, by contrast, gives the four-vector $H$ just described. This is the algebraic form of the standard statements that one bilinear is a Lorentz scalar while the squared norm of a single state is not, that a fermion condensate can break a symmetry, and that the Higgs field, being a scalar, couples to fermions through precisely such products. The scalar does not live in the state; it is a *product of two states*, and the product takes its value in the centre.

The distinction between the two routes is the distinction the title names. A state is an element and carries spin $\tfrac{1}{2}$ whether or not it is a solution of any particular equation. A field built from two states can be a scalar, and it lives in the centre. The Klein–Gordon field is of the second kind: it is the invariant channel of a product promoted to an independent field, which is why its equation is second order, why it decouples from the first-order structure, and why the material/informational split applies to it only as the real/imaginary split of one complex number.

## Open Questions

1. **The uniqueness of the trivial carrier.** *Open for the author.* The centralizer computation shows that the rotationally invariant elements of $\mathbb{B}$ form the centre, and no one-dimensional carrier exists. Whether the framework should regard the centre as *the* scalar field's value space, or whether a scalar could be valued outside $\mathbb{B}$ altogether, is a convention the present article fixes in the first sense; the second would require a value space the series has not considered.

2. **The boost transformation of a scalar.** A scalar field transforms trivially under the whole Lorentz group. The four-vector action has no nonzero invariant, and a boost along a spatial axis fixes the two transverse directions while carrying the time direction into the boost axis, so no nonzero central element is fixed by it. Whether the scalar's transformation law should be regarded as an independent assignment — the argument transformation with no algebraic factor — or as the restriction of some algebraic action, is not resolved here. The present article takes the first interpretation, which is the standard one and is consistent with the centre being invariant under the rotation subgroup.

3. **The general pure state and its direction.** The pure states $\tilde\Pi(\vec u)$ with $\vec u$ a real unit direction are the Hermitian ones, and their directions fill the two-sphere. A preparation may also carry a complex direction; the label then names a different pair of parts. The spin content is the same for every choice, because the left action is the same; what varies is the identification of the two parts and the Hermitian structure through which probabilities are read. Whether the physical state space must be built from Hermitian pure states, and how the direction $\vec u$ is to be interpreted, is not settled here; the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* addresses the carrier but not this classification.

4. **The relation to the informational interpretation.** The centre is contained in neither sector as a whole; it meets each sector in one real direction. This suggests that the material/informational dichotomy, at least for the scalar, is a real/complex pair rather than a state/operator pair. Whether the informational interpretation of $\mathbb{B}_{\Psi}$ survives the scalar case intact, or must be restricted to the non-scalar sectors, is a question for the informational articles.

5. **Composite scalars and higher-degree functionals.** The composite route uses the Hermitian product $H$ and its scalar part $\sigma=\mathrm{Sc}\,H$. At the bilinear level nothing is left open: each of the two products has a one-dimensional space of invariants under the Lorentz group, spanned by the antisymmetric and the mixed pairing, so every invariant bilinear is a multiple of one of them. Whether every scalar-valued functional of higher degree — a quartic condensate, a determinant, an effective action — reduces to products and sums of these is a different question, and it is not settled here.

6. **Why the algebra admits only spin $0$, $\tfrac{1}{2}$ and $1$.** The left action carries spin $\tfrac{1}{2}$, and the conjugation action carries spin $0$ and spin $1$; no other spin occurs among the elementary carriers. The general question — which spins the biquaternion algebra admits as elementary actions — is the subject of a separate article in the series and is not answered here.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The body writes no $\gamma$: the letter appears only in this closing dictionary.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$. The central grading $\xi_{\mathrm{ad}}=i\tilde{Ζ}_{\mathrm{ad}}$, where $\tilde{Ζ}_{\mathrm{ad}}$ is the central root of $-e_t$, is a different object: it is the difference of the two central idempotents of the complexified algebra, so $\xi_{\mathrm{ad}}^2=e_t$, and it is represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

A scalar field carries the trivial action of the Lorentz group: the transformation moves the argument and leaves the value alone. The carrier of states in the biquaternion framework is an element of $\mathbb{B}$, split into an L part and an R part by a label that takes two values; left multiplication keeps the label, and the L part is a carrier of the left action. The left action of the rotation generators $\tilde S_{\Psi,k}$ has Casimir $\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}e_t$ on every element, so every irreducible piece of the left action carries spin $\tfrac{1}{2}$. No nonzero state is rotation-invariant: the rotation by $-e_t$ negates it.

The rotationally invariant subspace of largest dimension in $\mathbb{B}$ is the centre $\mathbb{B}_{C}$, obtained as the centralizer of the quaternion units: $[\vec e_\nu,\tilde{Q}]=0$ for $\nu\in\{x,y,z\}$ forces $\tilde{Q}=Q_te_t$. The centre is a subalgebra isomorphic to $\mathbb{C}$, it is not stable under left multiplication, and it meets the states only at zero. This gives three reasons why the spin-$0$ value escapes the carrier of states. No one-dimensional subspace is carried into itself by every left multiplication, so the trivial action has no carrier. The rotationally invariant elements are exactly the central ones, so the scalar's value space is forced to be the centre. And the trivial action is not a part of either label: under the rotation subgroup it appears in the product of the two labels, while the Lorentz-scalar channels are the antisymmetric pairing of two states of one label and the mixed pairing of two states of opposite labels. A scalar is a product of two states, not a value of the state action.

For the sector split, the centre meets each sector in one real direction: the real scalar direction $e_t$ lies in $\mathbb{B}_{\Psi}$, and the imaginary scalar direction $ie_t$ lies in $\mathbb{B}_{\Phi}$. The sector decomposition of a complex scalar is therefore its decomposition into real and imaginary parts, which is the algebraic reason behind the companion article's finding that the second-order scalar structure does not organize itself by the sector split. Multiplication by $i$ exchanges the sectors and quarter-turns the scalar line; complex conjugation preserves each sector and reflects the scalar line, and is the operation that produces the conjugate solution. The scalar field itself is $\tilde{Ξ}=\xi_{\mathrm{scl}} e_t$ with $\xi_{\mathrm{scl}}$ complex, obeying $(\Box-k_m^{2})\tilde{Ξ}=0$ with $\Box$ central and scalar; no non-central operator of the framework acts on it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra; the carrier of states (cited) |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The four units, with $e_t$ the unit of the algebra (cited) |
| $i$ | Central scalar imaginary (cited) |
| ${}^{\natural},\,\bar{\cdot},\,{}^{*}$ | Quaternion, complex and Hermitian conjugation (cited) |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) sectors (cited) |
| $\mathbb{B}_{C}$ | Centre of $\mathbb{B}$; the scalar field's value space |
| $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | A state and its two labelled parts |
| $\tilde\Pi(\vec u)$ | Pure state carrying the unit direction $\vec u$ |
| $\tilde S_{\Psi,k}$ | Rotation generator; the left action has Casimir $\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}e_t$ |
| $\tilde{Ξ}=\xi_{\mathrm{scl}} e_t$ | Scalar (spin-$0$) field, valued in the centre |
| $\xi_{\mathrm{scl}}=\xi_{\mathrm{scl},1}+i\xi_{\mathrm{scl},2}$ | Complex scalar coefficient |
| $H=\tfrac12(\tilde{Ξ}_{\mathrm{sp}}\tilde\xi^{*}+\tilde\xi\tilde{Ξ}_{\mathrm{sp}}^*)$ | Hermitian product of two states, in $\mathbb{B}_{\Psi}$ |
| $\sigma=\mathrm{Sc}\,H$ | Scalar part of $H$; the time coefficient of $iH$, not a Lorentz scalar |
| $\mathfrak{b}(\tilde{Ξ}_{\mathrm{sp}},\tilde\xi)=2\,\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde\xi)$ | Mixed pairing of two states of opposite labels |
| $\tilde R_\Phi$, $\tilde P_{\Phi}\,k_{\Phi}$ | Four-position and four-wavevector, in $\mathbb{B}_{\Phi}$ (cited) |
| $\langle\tilde{Q}\rangle_{\natural}$ | Biquaternion norm (cited) |
| $\Box$ | d'Alembertian, central and scalar (cited) |
| $c$, $\frac{m\,c}{k_m}$, $m$ | Speed of light in the medium, reduced Planck constant, mass |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard treatment of the scalar field and the trivial representation of the Lorentz group.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the classification of the representations of the Lorentz group and the transformation laws of scalar, vector and spinor fields.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Klein–Gordon field and the role of the complex scalar.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra $M_2(\mathbb{C})$, its idempotents, minimal left ideals and simple modules.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the real structures and the representation theory of the Clifford algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of spinors, bilinears and the scalar and vector channels.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor calculus and the construction of scalars from spinor bilinears.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the operator-algebra interpretation of the two-state module.
