# __The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module__

## Introduction

A scalar field is, in standard relativistic physics, the simplest possible kind of field: a single component at each event, transforming in the **trivial representation** of the Lorentz group,

$$
\phi'(x') = \phi(x),
\qquad x'=\Lambda x,
$$

with no internal index, no axis, and no orientation. Every other field carries structure that a Lorentz transformation can act on: the four-vector carries its spacetime index, the Dirac field carries its spinor index, and the field strength carries two. The scalar carries none, and that is what "spin $0$" means.

The biquaternion framework describes quantum states in a specific algebraic object. In the companion article *The Schrödinger Equation in Biquaternionic Form* the state space is a **Peirce carrier** $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$, a minimal left ideal and here the **state module**; the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* shows that this same module carries the defining two-dimensional representation of the Lorentz group, and that its elements are the spinors. This is where spin-$\tfrac{1}{2}$ lives, and where the biquaternion Dirac field is built. The question this article asks is then immediate and unavoidable: **the framework's quantum states are spinor-like by construction, so where does a spin-$0$ field go, and why does it not go there?**

The answer worked out below is that a scalar field lives in the **centre** of the algebra, $\mathbb{C}_{\mathbb{B}}=\{Q_t e_t: Q_t\in\mathbb{C}\}$, and that it *escapes* the state module for three reasons that turn out to be the same reason seen three ways. The state module is the defining module of $M_2(\mathbb{C})$, and a simple matrix algebra has only one kind of module: every nonzero finite-dimensional $\mathbb{B}$-module is a direct sum of copies of $\mathbb{C}^2$. There is no one-dimensional module for the trivial representation to occupy. The centre, by contrast, is not a module at all: it is a subalgebra, and under the rotation subgroup of the Lorentz group it is exactly the rotationally invariant subspace of $\mathbb{B}$. Spin $0$ is the representation that the algebra carries in its centre, not in any module. The state module is the wrong *kind* of object to hold it.

The companion article *The Klein–Gordon Equation in Biquaternionic Form* reached a related conclusion from the equation rather than from the representation theory. It found that the second-order scalar equation decouples into four independent scalar equations because the d'Alembertian is central and scalar, that its right host is the centre $\mathbb{C}_{\mathbb{B}}$, and that the second-order structure does **not** organize itself by the material/informational split $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$. The present article supplies the algebraic reason behind that verdict. It shows *why* the centre is the scalar's home, why neither $\mathbb{M}_-$ nor $\mathbb{M}_+$ can host it as a representation space, and how the sector split should be read when the field is a scalar: not as particle and antiparticle, and not as state and operator, but as the real and imaginary parts of one complex number. The two scalar directions $e_t$ and $ie_t$ lie in the two sectors, and the complex scalar line is their direct sum.

The article is organized as follows. The state module and the representation it carries are recalled first, together with the fact that its elements are zero divisors. Then the centre is characterized, by the centralizer computation that fixes it as the rotationally invariant subspace. Then the three obstructions are stated and proved. Then the sector question is settled. Then the scalar field and its Klein–Gordon equation are written in the centre. A final section records the composite route, in which a scalar is built as a bilinear in the module rather than as an element of it, which is how scalar fields actually arise in the standard model.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_\mu^2=-e_t$ and $\vec e_\nu \vec e_\mu=-\delta_{\nu\mu}e_t+\varepsilon_{\nu\mu\lambda}\vec e_\lambda$, and $i$ is the central scalar imaginary with $i^2=-1$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector), and $\mathbb{H}_{\mathbb{B}}$ (real quaternions, the fixed points of complex conjugation); the centre is $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$. The conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*}=({}^{\natural})^{\,*}$ (Hermitian) and ${}^\flat=-{}^{*}$ (anti-Hermitian). The biquaternionic gradient is $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_\mu \vec e_\mu\,\partial/\partial Q_\mu$, with $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}=\partial^2/\partial Q_t^2+\Delta$, where $\Delta=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$ is the Laplacian in the three vector coordinates. The coordinates are $Q_t=ict'$ and $Q_x=x$, $Q_y=y$, $Q_z=z$, so that $\partial^2/\partial Q_t^2=-c^{-2}\,\partial^2/\partial {t'}^2$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value.

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation, its mass-term sign, and the sector analysis that this article explains.
- Companion article *The Schrödinger Equation in Biquaternionic Form*, for the state module and the central Hamiltonian.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the Peirce carrier (a minimal left ideal here), the two chiral halves, the Lorentz action, and the bilinear pairings.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the module-valued Dirac field and its scalar bilinears.
- Companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action*, for the material sector, the four-vectors, and the biquaternion norm.
- Companion article *The Informational Sector: States, Observables and Probability*, for the Hermitian sector, the idempotents, and the trace formula.

## The State Module and the Spin It Carries

### The Minimal Left Ideal

The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$ as a complex algebra, and the isomorphism sends the quaternion units to

$$
\mathsf{M}_2(e_t)=I_2,\qquad \mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu,\qquad \mathsf{M}_2(i)=iI_2,
$$

with $\sigma_\mu$ the Pauli matrices. A **primitive idempotent** is an element $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$ that cannot be written as a sum of two nonzero orthogonal idempotents. The idempotents of the form

$$
\tilde\Pi(\vec u)=\tfrac{1}{2}\left(e_t+i\vec u\right),
\qquad
\vec u=u_x\vec e_x+u_y\vec e_y+u_z\vec e_z,\quad u_x^2+u_y^2+u_z^2=1,\quad u_\mu\in\mathbb{R},
$$

are primitive, Hermitian, and of trace one. They lie in $\mathbb{M}_+$, and they are the pure states of the informational sector in the interpretation of the companion article *The Informational Sector: States, Observables and Probability*. The **minimal left ideal**

$$
\mathbb{B}\tilde\Pi(\vec u)=\{\tilde{Q}\tilde\Pi(\vec u) : \tilde{Q}\in\mathbb{B}\}\cong\mathbb{C}^2
$$

is the **state module** of the framework. Its elements are the spinors $\psi$, characterized by $\psi\tilde\Pi=\psi$.

Two features of this object are fixed by the definitions and used constantly. First, in the matrix picture it is the space of matrices whose only nonzero column is the first, that is, the column spinors $\mathbb{C}^2$; the idempotent $\tilde\Pi(\vec e_z)$ is the diagonal matrix unit $E_{11}=\mathrm{diag}(1,0)$ under the isomorphism above. Second, the algebra acts on it by **left multiplication**, $\psi\mapsto\tilde{Q}\psi$, and this action is complex-linear because the scalar imaginary $i$ is central. The state module is therefore a genuine two-dimensional complex module over $\mathbb{B}$, and

$$
\mathbb{B}\cong\mathbb{B}\tilde\Pi\oplus\mathbb{B}\tilde\Pi_{\mathrm{c}}=S\oplus S
$$

as a left module, where $\tilde\Pi_{\mathrm{c}}=e_t-\tilde\Pi$ is the complementary orthogonal idempotent.

### The Module Is the Defining Representation

The Lorentz group acts on the state module by left multiplication,

$$
\psi\;\longmapsto\;\tilde{U}\psi,
\qquad
\tilde{U}\in SL(2,\mathbb{C})=\{\tilde{U}\in\mathbb{B}:\tilde{U}\tilde{U}^{\natural}=e_t\},
$$

and the representation so obtained is the defining two-dimensional representation of $SL(2,\mathbb{C})$, the **spin-$\tfrac{1}{2}$** representation. The representation-theoretic content of the module is the content of $S=\mathbb{C}^2$ as a module over $M_2(\mathbb{C})$; its restriction to the rotation subgroup can be read off from the Lie algebra action.

The rotation subgroup is $SU(2)=SL(2,\mathbb{C})\cap \mathrm{U}(2)$, whose elements are the unit real quaternions, $\tilde r=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\,\vec n$ with $\vec n$ a unit pure real quaternion. Its Lie algebra is spanned by the generators

$$
\tilde S_\mu=\tfrac{i}{2}\vec e_\mu,
\qquad
[\tilde S_\nu,\tilde S_\mu]=i\varepsilon_{\nu\mu\lambda}\tilde S_\lambda .
$$

On the state module these act as left multiplication. The left multipliers, $L_a\psi=a\psi$, compose as $L_aL_b=L_{ab}$, so they inherit the quaternion relations,

$$
L_{\vec e_\nu}L_{\vec e_\mu}=-\delta_{\nu\mu}L_{e_t}+\varepsilon_{\nu\mu\lambda}L_{\vec e_\lambda},
$$

and in the matrix representation $L_{\vec e_\mu}$ is multiplication by $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$, so that

$$
\tilde S_\mu\;\longmapsto\;\tfrac{1}{2}\sigma_\mu .
$$

The quadratic Casimir is therefore

$$
\tilde S_1^2+\tilde S_2^2+\tilde S_3^2
\;\longmapsto\;
\tfrac{1}{4}\left(\sigma_1^2+\sigma_2^2+\sigma_3^2\right)
=\tfrac{1}{4}\cdot 3 I_2
=\tfrac{3}{4}I_2 ,
$$
and the matrix representation is faithful, so

$$
\boxed{\;\tilde S_1^2+\tilde S_2^2+\tilde S_3^2=\tfrac{3}{4}e_t\;}.
$$

Since $\tfrac{3}{4}=s(s+1)$ gives $s=\tfrac{1}{2}$, the state module carries **spin one-half**, as claimed. The value was confirmed by direct computation in the matrix representation: the Casimir evaluates to $\tfrac{3}{4}I_2$ exactly.

### The Module Is Not Rotationally Invariant

There is a second way to see the same content, and it is the one that makes the contrast with the scalar sharp. The idempotent $\tilde\Pi(\vec u)$ is built from a **direction** $\vec u$, and a rotation moves that direction. Conjugating by a unit real quaternion $\tilde r$,

$$
\tilde r\,\tilde\Pi(\vec u)\,\tilde r^{*}
=\tfrac{1}{2}\left(e_t+i\,\tilde r\vec u\tilde r^{*}\right)
=\tilde\Pi(\vec u_2),
$$

where $\vec u_2=\tilde r\vec u\tilde r^{*}$ is the rotated unit pure quaternion. Rotations about the axis $\vec u$ leave $\tilde\Pi$ fixed; rotations about other axes do not. The ideal moves with the axis, $\tilde r\,(\mathbb{B}\tilde\Pi)\,\tilde r^{-1}=\mathbb{B}\tilde\Pi(\vec u_2)$, and this is a different subspace of $\mathbb{B}$ whenever $\vec u_2\neq\vec u$; for the sample rotation used in the check below the angle between the two ideals is $25.9^{\circ}$. The abstract module is $\mathbb{C}^2$ for every axis, since the algebra has only one, but the copy of it inside $\mathbb{B}$ is tied to a direction. The orbit of the idempotent is therefore the two-sphere of unit pure quaternions, and its stabilizer is the $\mathrm{U}(1)$ subgroup of rotations about $\vec u$. This was verified numerically: a rotor of angle $1.1$ about the normalized axis $(0.3,-0.7,0.5)$ sends $\tilde\Pi(\vec e_z)=\tfrac{1}{2}(e_t+i\vec e_z)$ to $\tilde\Pi(\vec u_2)$ with $\vec u_2=(-0.586,-0.524,0.618)$, a unit vector, while a rotation about $\vec e_z$ fixes $\tilde\Pi(\vec e_z)$ identically. The state module is therefore invariant as an abstract module and not as a subspace of $\mathbb{B}$: its very definition singles out a direction.

A scalar field is exactly the opposite. It has no axis, and no rotation may move it. The remainder of the article makes that requirement precise inside the algebra and identifies the unique subspace that satisfies it.

## The Centre and Its Trivial Representation

### The Centralizer of the Rotations

Consider the element $\tilde{Q}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu\in\mathbb{B}$ and ask which elements are fixed by **every** rotation. Equivalently, ask for which $\tilde{Q}$ the infinitesimal condition

$$
[\vec e_\nu,\tilde{Q}]=\vec e_\nu\tilde{Q}-\tilde{Q}\vec e_\nu=0,
\qquad \nu\in\{x,y,z\},
$$

holds. Evaluating the first of these with $\vec e_x^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$, $\vec e_x\vec e_z=-\vec e_y$, one finds

$$
[\vec e_x,\tilde{Q}]=2Q_y\vec e_z-2Q_z\vec e_y,
$$

so $[\vec e_x,\tilde{Q}]=0$ forces $Q_y=Q_z=0$. The condition $[\vec e_y,\tilde{Q}]=0$ then forces $Q_x=Q_z=0$, and together with the first gives $Q_x=Q_y=Q_z=0$. Hence

$$
\boxed{\;
\{\tilde{Q}\in\mathbb{B} : [\vec e_\nu,\tilde{Q}]=0,\ \nu\in\{x,y,z\}\}
=\mathbb{C}_{\mathbb{B}}
=\{Q_te_t : Q_t\in\mathbb{C}\}\;},
$$

the **centre** of the algebra. The result was confirmed independently by solving the linear system $[\vec e_\nu,\tilde{Q}]=0$ over the eight real coordinates of $\tilde{Q}$: the coefficient matrix has rank six and nullity two, so the solution space is the real two-dimensional subspace $\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$, as stated.

The algebraic statement is therefore exact: **the elements of $\mathbb{B}$ that are invariant under the rotation subgroup are precisely the central elements.** The traceless part transforms instead as the adjoint representation, so under rotations the algebra splits as

$$
\boxed{\;
\mathbb{B}=\underbrace{\mathbb{C}_{\mathbb{B}}}_{\text{spin }0}\;\oplus\;\underbrace{\{\tilde{Q}:\mathrm{Sc}\,\tilde{Q}=0\}}_{\text{spin }1}\;},
$$

while the state module carries spin $\tfrac{1}{2}$. A spin-$0$ field has no alternative but the centre.

### The Centre Is a Subalgebra, Not an Ideal

It matters that the centre is a subalgebra and not a module, because that is what separates the scalar from the spinor structurally. The centre is closed under multiplication, because central elements commute and their product is again central,

$$
(Q_te_t)(R_te_t)=(Q_tR_t)e_t\in\mathbb{C}_{\mathbb{B}},
$$

so it is a field isomorphic to $\mathbb{C}$. It is fixed pointwise by quaternion conjugation, hence it is exactly the fixed space of $\natural$.

It is **not** a left ideal. For a central element $Q_te_t$ and a general $\tilde{Q}\in\mathbb{B}$,

$$
(Q_te_t)\tilde{Q}=Q_t\tilde{Q},
$$

which lies in the centre only if $\tilde{Q}$ does. Taking $\tilde{Q}$ with a nonzero vector part produces a nonzero vector part in the product, so the centre is not closed under left multiplication by the algebra. In particular the centre contains no nonzero $\mathbb{B}$-submodule: the only $\mathbb{B}$-module it could be is trivial, and $M_2(\mathbb{C})$ has no one-dimensional module with a nonzero action. The centre meets the state module trivially as well: a central element $\lambda e_t$ lies in $\mathbb{B}\tilde\Pi$ only if its second column vanishes, which forces $\lambda=0$. This was confirmed in the matrix representation.

The distinction has a second, more elementary face. Every nonzero element of the state module is a **zero divisor**. A spinor satisfies $\psi\tilde\Pi=\psi$, hence $\psi(e_t-\tilde\Pi)=0$ with $e_t-\tilde\Pi\neq0$; in the matrix picture its determinant vanishes. A central element $\lambda e_t$, by contrast, has determinant $\lambda^2$ and is invertible whenever $\lambda\neq0$. The nonzero elements of the scalar line are invertible; the module is the algebra's space of non-invertible spinors. They cannot be the same space, and they do not overlap except at zero.

## Three Obstructions, One Reason

The state module cannot host a spin-$0$ field for three reasons, one for each object involved: the module, the algebra, and the tensor square.

### No Trivial Submodule

The algebra $M_2(\mathbb{C})$ is **simple**: its only two-sided ideals are $0$ and itself. A finite-dimensional module of a simple algebra is completely reducible, and there is exactly one simple module up to isomorphism, the column space $S=\mathbb{C}^2$. Every nonzero finite-dimensional module is therefore a direct sum of copies of $S$. A one-dimensional module carrying the trivial representation does not exist, with any nonzero action. Since the trivial representation is precisely what a scalar field carries, no module of $\mathbb{B}$ can hold it.

The state module is not an exception within a richer family of modules; it is, up to multiplicity, the *only* module there is. A spin-$0$ field is not "the module with spin $0$" as opposed to "the module with spin $\tfrac{1}{2}$", because the algebra has just one kind of module and it is spin-$\tfrac{1}{2}$. The spin-$0$ carrier has to be found outside the module category altogether.

### The Invariant Subspace Is the Centre

If one insists on locating the scalar inside the algebra rather than inside a module, the centralizer computation settles where. Under the rotation subgroup the algebra decomposes as spin $0$ (the centre) plus spin $1$ (the traceless part); under the rotor-conjugation action $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$ there is no nonzero element invariant under the full Lorentz group, since that action on $\mathbb{B}$ is the irreducible complexified four-vector representation. The only rotationally invariant elements are central. A scalar field, being invariant under rotations, must therefore take its values in $\mathbb{C}_{\mathbb{B}}$, and there is nothing else it could take them in.

It is worth stating plainly how the scalar relates to the rotor-conjugation action that carries the material sector. The four-vectors of $\mathbb{M}_-$ transform as $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$, which is the four-vector representation; under rotations it splits into the time component (spin $0$) and the spatial vector (spin $1$). The scalar field does not transform by this rule at all. Its Lorentz transformation is the transformation of its argument, $\tilde{\Phi}'(x')=\tilde{\Phi}(x)$ with $x'=\Lambda x$, and no algebraic factor acts on the value. The absence of an algebraic action is the field-theoretic statement of spin $0$, and the centre is the value space in which that absence is natural.

### The Trivial Representation Lives in the Tensor Square

There is a third way to see why the scalar is not *in* the module, and it explains where scalars actually come from. If the state module carries the defining representation $(\tfrac{1}{2},0)$ of complex dimension two, then its complex conjugate $\bar{S}=(0,\tfrac{1}{2})$ is the other chiral half, and the tensor product decomposes as

$$
S\otimes\bar{S}=\left(\tfrac{1}{2},0\right)\otimes\left(0,\tfrac{1}{2}\right)
=\left(\tfrac{1}{2},\tfrac{1}{2}\right)
\;\cong\;\mathbb{C}\oplus\mathbb{C}^3
$$

under the rotation subgroup, where the trivial piece is the channel a scalar would occupy. The trivial representation appears here, in the **bilinear** combination of two spinors, not as a submodule of either factor. The decomposition, however, is a statement about the rotation subgroup only: under the full Lorentz group $S\otimes\bar{S}=(\tfrac{1}{2},\tfrac{1}{2})$ is irreducible, so the $SU(2)$-trivial piece is the time component of a four-vector rather than a Lorentz scalar. The Lorentz scalars come instead from two contractions: the antisymmetric square $\Lambda^2 S$, whose invariant is the symplectic form $\varepsilon$, and the mixed pairing $\mathfrak{b}$ of $S$ with the conjugate half, which carries the contragredient of the conjugate action. A scalar is therefore not an element of the state module but a scalar-valued pairing of two module elements. The four-vector channel is the Hermitian bilinear

$$
H=\tfrac{1}{2}\left(\psi\chi^{*}+\chi\psi^{*}\right)\in\mathbb{M}_+,
$$

which is Hermitian for every pair, unlike the single product $\psi\chi^{*}$; its diagonal case $\chi=\psi$ is the positive element $\psi\psi^{*}$, and normalised by its trace it is the density $\tilde{Ϛ}=\psi\psi^{*}/\mathrm{Tr}(\psi\psi^{*})$.

This is the algebraic content of the standard fact that a spin-$0$ object can be built from two spin-$\tfrac{1}{2}$ objects but is not itself one: the trivial representation of $SU(2)$ sits in the tensor square, not in the defining representation. The companion article *The Dirac Equation in Biquaternionic Form* uses the same bilinears when it forms the Dirac current and the Dirac scalar, and the companion article on the spinor module develops the Hermitian, symplectic and mixed pairings and their invariance properties explicitly.

## The Sector Question: Neither $\mathbb{M}_-$ nor $\mathbb{M}_+$

The framework's central algebraic fact is the decomposition $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ into the anti-Hermitian material sector and the Hermitian informational sector. The companion article *The Klein–Gordon Equation in Biquaternionic Form* asked whether the second-order scalar structure organizes itself by this split, and found that it does not: because the d'Alembertian is central and scalar, the split merely separates a complex solution into its real and imaginary parts, giving two $i$-related copies of one real solution space rather than a particle–antiparticle or state–operator pair. The representation theory above explains why, and it also says what the split *does* mean for a scalar.

The scalar field's value space is the centre, and the centre meets each sector in exactly one real direction:

$$
\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\},
\qquad
\operatorname{span}_{\mathbb{R}}\{e_t\}\subset\mathbb{M}_+,
\qquad
\operatorname{span}_{\mathbb{R}}\{ie_t\}\subset\mathbb{M}_- .
$$

The real scalar direction $e_t$ is the scalar part of the Hermitian sector; the imaginary scalar direction $ie_t$ is the scalar part of the material sector. A complex scalar $\tilde{\Phi}=\phi e_t$ with $\phi=\phi_1+i\phi_2$ and $\phi_1,\phi_2\in\mathbb{R}$ therefore splits as

$$
\tilde{\Phi}=\underbrace{\phi_1\,e_t}_{\in\,\mathbb{M}_+}+\underbrace{\phi_2\,ie_t}_{\in\,\mathbb{M}_-},
$$

and the sector decomposition of a scalar field is nothing other than the decomposition of a complex number into its real and imaginary parts. This is the precise sense in which the Klein–Gordon article's negative verdict is forced: the $\mathbb{M}_-/\mathbb{M}_+$ split cannot carry the particle–antiparticle doubling, because on the scalar line it is the real/imaginary-part split of a single complex number.

The operations that act on that complex number must be kept distinct, and the same distinction settles the sector question completely.

- **Multiplication by $i$** is central and exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, $i\mathbb{M}_-=\mathbb{M}_+$. On a scalar it maps $\phi_1e_t+\phi_2ie_t$ to $-\phi_2e_t+\phi_1ie_t$: it is a quarter-turn of the complex scalar line, exchanging its two real directions.
- **Complex conjugation $\bar{\cdot}$** acts on the coefficients and preserves each sector. On a scalar it maps $\phi_1e_t+\phi_2ie_t$ to $\phi_1e_t-\phi_2ie_t$: it is the reflection of the complex line, and it produces the second solution of the second-order equation, $\bar{\tilde{\Phi}}$.
- **Hermitian conjugation ${}^{*}$** is the involution whose eigenspaces define the sectors; it is neither of the other two, and on the centre it agrees with $\bar{\cdot}$.

These are three different maps, but only two distinct actions on the scalar line: the Hermitian star and complex conjugation coincide there, and multiplication by $i$ is the map that acts differently. The sector-exchanging map $i$ is not the conjugate-producing map $\bar{\cdot}$, and reading the Klein–Gordon conjugate pair $(\tilde{\Phi},\tilde{\Phi}^*)$ as the sector pair $(\mathbb{M}_-,\mathbb{M}_+)$ is precisely the conflation the companion article warns against. The centre makes the distinction visible: complex conjugation has real fixed points in the centre, the direction $e_t$; multiplication by $i$ has none.

## The Scalar Field in the Centre

With the value space fixed, the scalar field is written down at once. A spin-$0$ field of mass $m$ is a function into the centre,

$$
\tilde{\Phi}(x)=\phi(x)\,e_t,
\qquad
\phi(x)\in\mathbb{C},
$$

and it obeys the Klein–Gordon equation in the form of the companion article,

$$
\left(\Box-\frac{m^2c^2}{\hbar^2}\right)\tilde{\Phi}=0,
\qquad
\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial Q_t^2+\Delta .
$$

Because $\Box$ is central and scalar, it acts coefficient by coefficient, and on a central field the equation is the ordinary complex scalar Klein–Gordon equation

$$
\left(\Box-\frac{m^2c^2}{\hbar^2}\right)\phi=0 ,
$$

with the biquaternion writing carrying no additional content. This is the honest verdict of the companion article, and the representation theory of the present article says why it must be so: there is no axis in the field for any non-central algebraic structure to act on.

The plane-wave solutions exhibit the same point. Writing the four-wavevector and the four-position in the material sector,

$$
\tilde P/\hbar=i\frac{\omega}{c}e_t+\vec k\in\mathbb{M}_-,
\qquad
\tilde{R}=ict'\,e_t+\vec x\in\mathbb{M}_-,
\qquad
\vec k=k_x\vec e_x+k_y\vec e_y+k_z\vec e_z,\quad \vec x=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,
$$

the phase is the real scalar $\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar=\vec k\cdot\vec x-\omega t'$, and the positive-frequency solution is

$$
\tilde{\Phi}=\phi_0\,\exp\!\left(i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar\right)e_t
=\phi_0\,\exp\!\left(i(\vec k\cdot\vec x-\omega t')\right)e_t .
$$

The exponential is central. The mass-shell condition is the biquaternion norm of the four-wavevector,

$$
\langle\tilde P/\hbar\rangle_{\natural}=\frac{\tilde P\tilde P^{\natural}}{\hbar^{2}}
=-\frac{\omega^2}{c^2}+k_x^2+k_y^2+k_z^2 ,
$$
and setting it to the negative constant $-m^2c^2/\hbar^2$ gives the dispersion relation
$$
-\frac{\omega^2}{c^2}+k_x^2+k_y^2+k_z^2=-\frac{m^2c^2}{\hbar^2}
\quad\Longleftrightarrow\quad
\omega^2=c^2\left(k_x^2+k_y^2+k_z^2\right)+\frac{m^2c^4}{\hbar^2} ,
$$

which is the standard relativistic dispersion relation and is reproduced here only to record that the scalar field's entire algebraic content is the biquaternion norm of a four-vector, not a module structure. The conserved current $\tilde{J}=ic\rho\,e_t+\vec j$ lies in $\mathbb{M}_-$, its scalar component being the imaginary scalar direction, exactly as for the four-current of relativistic mechanics.

One structural remark belongs with the equation. The first-order operators of the framework, $\tilde{\nabla}$ and the left action of $\tilde{U}$, are module-theoretic or vectorial: they act on spinors or on four-vectors and change their representation content. The scalar field has neither. The only operator the scalar equation uses is the central scalar $\Box$, whose square-root structure — the spinor factorisation $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ — is a statement about the *operator*, not about the field it acts on. A scalar field is annihilated by a composite of spinor operators without ever being a spinor; it is the algebra's trivial representation appearing in the composition, not a state in the module.

## Scalars from the Module: The Composite Route

The three obstructions above say that a scalar is not an element of the state module. They do not say that the state module is irrelevant to scalar physics, and it is worth recording how scalars actually appear in the standard model, because the framework reproduces the mechanism.

A Lorentz-invariant scalar built from module elements is a **bilinear**, but not every bilinear is one. If $\psi,\chi$ are spinors in the state module, the product $\psi\chi^{*}$ is a rank-one element of $\mathbb{B}$; it is Hermitian only when $\chi=\lambda\psi$ with $\lambda\in\mathbb{R}$, so in general it is not a four-vector. The object that is Hermitian for every pair is the symmetrised product

$$
H=\tfrac{1}{2}\left(\psi\chi^{*}+\chi\psi^{*}\right)\in\mathbb{M}_+,
\qquad
\sigma=\mathrm{Sc}\,H=\tfrac{1}{2}\mathrm{Tr}\,H=\mathrm{Re}\,\mathrm{Sc}\!\left(\psi\chi^{*}\right),
$$

and its scalar part $\sigma$ is real. Under a Lorentz transformation the module transforms by left multiplication, $\psi\mapsto\tilde{U}\psi$ and $\chi\mapsto\tilde{U}\chi$, so

$$
H\;\longmapsto\;\tilde{U}\,H\,\tilde{U}^{*},
$$

which is the rotor-conjugation action on $\mathbb{M}_+$; the physical four-vector is $iH\in\mathbb{M}_-$. The scalar part $\sigma$ is invariant under the rotation subgroup, where $\tilde U^{*}=\tilde U^{-1}$, but **not** under boosts, where $\tilde U^{*}\tilde U\neq e_t$. The object $H$ is therefore the four-vector channel, and $\sigma$ is the coefficient of its time direction, not a Lorentz scalar; this is the algebraic form of the standard statement that $\psi^\dagger\psi$ is the time component of the four-current, not an invariant. A numerical check on a generic pair gives the expected behaviour: a rotation leaves $\sigma$ unchanged to machine precision, while a boost of rapidity $1.3$ multiplies it by $e^{1.3}=3.669$ for $\psi=(1,0)^{\mathsf T}$, $\chi=(1,1)^{\mathsf T}/\sqrt2$ and a boost along $\vec e_x$.

The Lorentz-invariant scalars are instead the two pairings developed in the companion article on the spinor module. The **symplectic pairing** of two spinors of the same chirality,

$$
\varepsilon(\psi,\chi)=\psi^{T}\epsilon\,\chi,
\qquad
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

is invariant because $\tilde{U}^{T}\epsilon\,\tilde{U}=\epsilon$, which holds since $\det\tilde{U}=1$. The **mixed pairing** of a spinor with one in the conjugate module,

$$
\mathfrak{b}(\psi,\chi)=2\,\mathrm{Sc}\!\left(\psi^{*}\chi\right),
\qquad
\psi\mapsto\tilde{U}\psi,
\qquad
\chi\mapsto\mathsf{M}_2\!\left((\tilde{U}^{*})^{\natural}\right)\chi,
$$

is invariant because $\tilde U^{*}(\tilde U^{*})^{\natural}=e_t$ for a unit-norm $\tilde U$; the factor on the right is the inverse conjugate transpose $(\mathsf{M}_2(\tilde U)^{\dagger})^{-1}$, not $\mathsf{M}_2(\tilde U^{*})$. These are the two scalar channels of the module: $\varepsilon$ is the antisymmetric contraction of two same-chirality spinors, and $\mathfrak b$ is the Dirac scalar, which pairs the two chiral halves. Both are invariant complex numbers, hence central multiples of $e_t$; the Hermitian channel, by contrast, gives the four-vector $H$ just described. This is the algebraic form of the standard statements that $\bar{\psi}\psi$ is a Lorentz scalar while $\psi^\dagger\psi$ is not, that a fermion condensate can break a symmetry, and that the Higgs field, being a scalar, couples to fermions through precisely such bilinears. The scalar does not live in the module; it is a *pairing of two module elements*, and the pairing takes its values in the centre.

The distinction between the two routes is the distinction the title names. A field that is *in* the state module is a spinor, and it carries spin $\tfrac{1}{2}$ whether or not it is a solution of any particular equation. A field that is *built from* the state module can be a scalar, and it lives in the centre. The Klein–Gordon field is of the second kind: it is the trivial sector of the module's tensor square promoted to an independent field, which is why its equation is second order, why it decouples from the module's first-order structure, and why the material/informational split applies to it only as the real/imaginary split of one complex number.

## Open Questions

1. **The uniqueness of the trivial carrier.** *Open for the author.* The centralizer computation shows that the rotationally invariant elements of $\mathbb{B}$ form the centre, and the irreducibility of $S$ shows that the state module contains no nonzero invariant vector, since such a vector would span a one-dimensional trivial submodule. Whether the framework should regard the centre as *the* scalar field's value space, or whether a scalar could be valued outside $\mathbb{B}$ altogether, is a convention the present article fixes in the first sense; the second would require a value space the series has not considered.

2. **The boost transformation of a scalar.** A scalar field transforms trivially under the whole Lorentz group. The framework's rotor-conjugation action is the four-vector action: it has no nonzero invariant under the full group, and a boost along a spatial axis fixes the two transverse directions while carrying the time direction into the boost axis, so no element of the centre survives it. Whether the scalar's transformation law should be regarded as an independent assignment — the argument transformation with no algebraic factor — or as the restriction of some algebraic action, is not resolved here. The present article takes the first interpretation, which is the standard one and is consistent with the centre being invariant under the rotation subgroup.

3. **The general idempotent and the state axis.** The idempotents $\tilde\Pi(\vec u)=\tfrac{1}{2}(e_t+i\vec u)$ with $\vec u$ a real unit pure quaternion are the Hermitian ones, and their axes fill the two-sphere. Idempotents built from non-Hermitian roots of $-e_t$ generate the remaining minimal left ideals. Those ideals are all isomorphic as modules, since primitive idempotents of $M_2(\mathbb{C})$ are conjugate, so the representation content — spin $\tfrac{1}{2}$ — is the same for every choice; what varies is the projector, and with it the identification of the spinor coordinates and the Hermitian structure through which probabilities are read. Whether the physical state space must be a Hermitian ideal, and how the axis $\vec u$ is to be interpreted, is not settled here; the companion article on the spinor module addresses the ideal model but not this classification.

4. **The relation to the informational interpretation.** The centre is contained in neither sector as a whole; it meets each sector in one real direction. This suggests that the material/informational dichotomy, at least for the scalar, is a real/complex pair rather than a state/operator pair. Whether the informational interpretation of $\mathbb{M}_+$ survives the scalar case intact, or must be restricted to the non-scalar sectors, is a question for the informational articles.

5. **Composite scalars and the trace formula.** The bilinear route uses the Hermitian product $H$ and its scalar part $\sigma=\mathrm{Sc}\,H$, read through the trace formula $\mathrm{Tr}(H)=2\,\mathrm{Sc}\,H$. At the bilinear level nothing is left open: $S\otimes S$ and $S\otimes\bar{S}$ each have a one-dimensional space of invariants under $SL(2,\mathbb{C})$, spanned by $\varepsilon$ and $\mathfrak{b}$, so every invariant bilinear is a multiple of one of them. Whether every scalar-valued functional of higher degree — a quartic condensate, a determinant, an effective action — reduces to products and sums of these is a different question, and it is not settled here.

6. **Why the algebra admits only spin $0$ and one-half.** The module carries spin $\tfrac{1}{2}$ and the algebra under rotations carries spin $0$ and $1$; there is no simple module of higher spin. The general question — which spins the biquaternion algebra admits as elementary representations — is the subject of a separate article in the series and is not answered here.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The body writes no $\gamma$: the letter appears only in this closing dictionary.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$. The central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$, where $\tilde\Xi_{\mathrm{ad}}$ is the central root of $-e_t$, is a different object: it is the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$, and it is represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

A scalar field carries the trivial representation of the Lorentz group, and the biquaternion framework must therefore be asked where a trivial-representation field can live. The framework's state module is the minimal left ideal $\mathbb{B}\tilde\Pi(\vec u)\cong\mathbb{C}^2$, and it carries the defining two-dimensional, spin-$\tfrac{1}{2}$ representation of $SL(2,\mathbb{C})$: the left action of the rotation generators $\tilde S_\mu=\tfrac{i}{2}\vec e_\mu$ on the module has Casimir $\tfrac{3}{4}e_t$. Its primitive idempotent is built from a spatial axis, and rotations move that axis around the two-sphere, so the module is not rotationally invariant.

The unique rotationally invariant subspace of $\mathbb{B}$ is the centre $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$, obtained as the centralizer of the quaternion units: $[\vec e_\nu,\tilde{Q}]=0$ for $\nu\in\{x,y,z\}$ forces $\tilde{Q}=Q_te_t$. The centre is a subalgebra isomorphic to $\mathbb{C}$ and is not a left ideal; it meets the state module only at zero. This gives three reasons why spin $0$ escapes the state module. The algebra $M_2(\mathbb{C})$ is simple and has only one simple module, $\mathbb{C}^2$, so there is no one-dimensional module for the trivial representation. The rotationally invariant elements are exactly the central ones, so the scalar's value space is forced to be the centre. And the trivial representation is not a submodule of either factor: under $SU(2)$ it appears in $S\otimes\bar{S}\cong\mathbb{C}\oplus\mathbb{C}^3$, where it is the time component of the Lorentz four-vector, while the Lorentz-scalar channels are the symplectic contraction of $S\otimes S$ and the mixed pairing, so a scalar is a bilinear in the module rather than an element of it.

For the sector split, the centre meets each sector in one real direction: the real scalar $e_t$ is the scalar part of $\mathbb{M}_+$, and the imaginary scalar $ie_t$ is the scalar part of $\mathbb{M}_-$. The $\mathbb{M}_-/\mathbb{M}_+$ decomposition of a complex scalar is therefore its decomposition into real and imaginary parts, which is the representation-theoretic reason behind the companion article's finding that the second-order Klein–Gordon structure does not organize itself by the sector split. Multiplication by $i$ exchanges the sectors and quarter-turns the scalar line; complex conjugation preserves each sector and reflects the scalar line, and is the operation that produces the conjugate solution. The scalar field itself is $\tilde{\Phi}=\phi e_t$ with $\phi$ complex, obeying $(\Box-m^2c^2/\hbar^2)\tilde{\Phi}=0$ with $\Box$ central and scalar; no non-central operator of the framework acts on it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, $\vec e_\nu \vec e_\mu=-\delta_{\nu\mu}e_t+\varepsilon_{\nu\mu\lambda}\vec e_\lambda$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| ${}^{\natural},\,\bar{\cdot},\,{}^{*}=({}^{\natural})^{\,*},\,{}^\flat=-{}^{*}$ | Quaternion, complex, Hermitian, anti-Hermitian conjugation |
| $\mathbb{M}_-,\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, fixed points of $\bar{\cdot}$ |
| $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ | Centre of $\mathbb{B}$; the scalar field's value space |
| $\tilde\Pi(\vec u)=\tfrac{1}{2}(e_t+i\vec u)$ | Primitive Hermitian idempotent, $\vec u$ a unit pure real quaternion |
| $L_a,\,R_b$ | Left and right multipliers, $L_a\psi=a\psi$ and $R_b\psi=\psi b$; the cells of *The Gamma Formulation* |
| $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$ | State module (minimal left ideal) |
| $\psi$ | Spinor, an element of the state module |
| $\tilde S_\mu=\tfrac{i}{2}\vec e_\mu$ | Rotation generators; $\tilde S_1^2+\tilde S_2^2+\tilde S_3^2=\tfrac{3}{4}e_t$ on the module |
| $SL(2,\mathbb{C})=\{\tilde{U}:\tilde{U}\tilde{U}^{\natural}=e_t\}$ | Unit-norm biquaternions; Lorentz group |
| $\tilde{R}=ict'\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Four-position biquaternion, $\in\mathbb{M}_-$ |
| $\tilde P/\hbar=i\omega/c\,e_t+\vec k$, $\vec k=k_x\vec e_x+k_y\vec e_y+k_z\vec e_z$ | Four-wavevector, $\in\mathbb{M}_-$ |
| $\langle\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\tilde\Xi_{\mathrm{ad}}$, $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ | Central root of $-e_t$ and the central grading of the gamma formulation |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_\mu \vec e_\mu\,\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial Q_t^2+\Delta$, $\Delta=\sum_k\partial^2/\partial Q_k^2$ | d'Alembertian, central and scalar; $\Delta$ is the spatial Laplacian |
| $\tilde{\Phi}=\phi e_t$ | Scalar (spin-$0$) field, valued in the centre |
| $H=\tfrac{1}{2}(\psi\chi^{*}+\chi\psi^{*})\in\mathbb{M}_+$ | Hermitian bilinear; the four-vector channel, whose physical four-vector is $iH\in\mathbb{M}_-$ |
| $\sigma=\mathrm{Sc}\,H=\tfrac{1}{2}\mathrm{Tr}\,H$ | Scalar part of $H$; the time-direction coefficient of $iH$, not a Lorentz scalar |
| $\varepsilon(\psi,\chi)=\psi^{T}\epsilon\chi$ | Symplectic pairing; Lorentz scalar of two same-chirality spinors |
| $\mathfrak{b}(\psi,\chi)=2\,\mathrm{Sc}(\psi^{*}\chi)$ | Mixed pairing; Dirac scalar of a left–right spinor pair |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace formula |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard treatment of the scalar field and the trivial representation of the Lorentz group.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the classification of the representations of the Lorentz group and the transformation laws of scalar, vector and spinor fields.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Klein–Gordon field and the role of the complex scalar.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra $M_2(\mathbb{C})$, its idempotents, minimal left ideals and simple modules.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the real structures and the representation theory of the Clifford algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of spinors, bilinears and the scalar and vector channels.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor calculus and the construction of scalars from spinor bilinears.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the operator-algebra interpretation of the two-state module.
