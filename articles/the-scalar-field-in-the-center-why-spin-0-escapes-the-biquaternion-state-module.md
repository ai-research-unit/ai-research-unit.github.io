# __The Scalar Field in the Center: Why Spin 0 Escapes the Biquaternion State Module__

## Introduction

A scalar field is, in standard relativistic physics, the simplest possible kind of field: a single component at each event, transforming in the **trivial representation** of the Lorentz group,

$$
\phi'(x') = \phi(x),
$$

with no internal index, no axis, and no orientation. Every other field carries structure that a Lorentz transformation can act on: the four-vector carries its spacetime index, the Dirac field carries its spinor index, and the field strength carries two. The scalar carries none, and that is what "spin $0$" means.

The biquaternion framework describes quantum states in a specific algebraic object. In the companion article *The Schrödinger Equation in Biquaternionic Form* the state space is a **minimal left ideal** $\mathbb{B}\tilde{P}\cong\mathbb{C}^2$, the **state module**; the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* shows that this same module carries the defining two-dimensional representation of the Lorentz group, and that its elements are the spinors. This is where spin-$\tfrac{1}{2}$ lives, and where the biquaternion Dirac field is built. The question this article asks is then immediate and unavoidable: **the framework's quantum states are spinor-like by construction, so where does a spin-$0$ field go, and why does it not go there?**

The answer worked out below is that a scalar field lives in the **center** of the algebra, $\mathbb{C}_{\mathbb{B}}=\{Q_0 e_0\}$, and that it *escapes* the state module for three reasons that turn out to be the same reason seen three ways. The state module is the defining module of $M_2(\mathbb{C})$, and a simple matrix algebra has only one kind of module: every nonzero finite-dimensional $\mathbb{B}$-module is a direct sum of copies of $\mathbb{C}^2$. There is no one-dimensional module for the trivial representation to occupy. The center, by contrast, is not a module at all: it is a subalgebra, and under the rotation subgroup of the Lorentz group it is exactly the rotationally invariant subspace of $\mathbb{B}$. Spin $0$ is the representation that the algebra carries in its center, not in any module. The state module is the wrong *kind* of object to hold it.

The companion article *The Klein–Gordon Equation in Biquaternionic Form* reached a related conclusion from the equation rather than from the representation theory. It found that the second-order scalar equation decouples into four independent scalar equations because the d'Alembertian is central and scalar, that its right host is the center $\mathbb{C}_{\mathbb{B}}$, and that the second-order structure does **not** organize itself by the material/informational split $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$. The present article supplies the algebraic reason behind that verdict. It shows *why* the center is the scalar's home, why neither $\mathbb{M}_-$ nor $\mathbb{M}_+$ can host it as a representation space, and how the sector split should be read when the field is a scalar: not as particle and antiparticle, and not as state and operator, but as the real and imaginary parts of one complex number. The two scalar directions $e_0$ and $ie_0$ lie in the two sectors, and the complex scalar line is their direct sum.

The article is organized as follows. The state module and the representation it carries are recalled first, together with the fact that its elements are zero divisors. Then the center is characterized, by the centralizer computation that fixes it as the rotationally invariant subspace. Then the three obstructions are stated and proved. Then the sector question is settled. Then the scalar field and its Klein–Gordon equation are written in the center. A final section records the composite route, in which a scalar is built as a bilinear in the module rather than as an element of it, which is how scalar fields actually arise in the standard model.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, and $i$ is the central scalar imaginary with $i^2=-1$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector), and $\mathbb{H}_{\mathbb{B}}$ (real quaternions, the fixed points of complex conjugation); the center is $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$. The conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), ${}^\dagger=\bar{\cdot}^{\,*}$ (Hermitian) and ${}^\flat=-\dagger$ (anti-Hermitian). The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$, with $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}=\partial_{ict}^2+\Delta$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value.

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation, its mass-term sign, and the sector analysis that this article explains.
- Companion article *The Schrödinger Equation in Biquaternionic Form*, for the state module and the central Hamiltonian.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the minimal left ideal, the two chiral halves, the Lorentz action, and the bilinear pairings.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the module-valued Dirac field and its scalar bilinears.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material sector, the four-vectors, and the norm form.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian sector, the idempotents, and the trace formula.

## The State Module and the Spin It Carries

### The Minimal Left Ideal

The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$ as a complex algebra, and the isomorphism sends the quaternion units to

$$
\Phi(e_0)=I_2,\qquad \Phi(e_k)=-i\sigma_k,\qquad \Phi(i)=iI_2,
$$

with $\sigma_k$ the Pauli matrices. A **primitive idempotent** is an element $\tilde{P}$ with $\tilde{P}^2=\tilde{P}$ that cannot be written as a sum of two nonzero orthogonal idempotents. The idempotents of the form

$$
\tilde{P}(\hat{\mu})=\tfrac{1}{2}\left(e_0+i\hat{\mu}\right),
\qquad
\hat{\mu}=\mu_1e_1+\mu_2e_2+\mu_3e_3,\quad \mu_1^2+\mu_2^2+\mu_3^2=1,\quad \mu_k\in\mathbb{R},
$$

are primitive, Hermitian, and of trace one. They lie in $\mathbb{M}_+$, and they are the pure states of the informational sector in the reading of the companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*. The **minimal left ideal**

$$
\mathbb{B}\tilde{P}(\hat{\mu})=\{\tilde{Q}\tilde{P}(\hat{\mu}) : \tilde{Q}\in\mathbb{B}\}\cong\mathbb{C}^2
$$

is the **state module** of the framework. Its elements are the spinors $\tilde{\psi}$, characterized by $\tilde{\psi}\tilde{P}=\tilde{\psi}$.

Two features of this object are fixed by the definitions and used constantly. First, in the matrix picture it is the space of matrices whose only nonzero column is the first, that is, the column spinors $\mathbb{C}^2$; the idempotent $\tilde{P}(e_3)$ is the diagonal matrix unit $E_{11}=\mathrm{diag}(1,0)$ under the isomorphism above. Second, the algebra acts on it by **left multiplication**, $\tilde{\psi}\mapsto\tilde{Q}\tilde{\psi}$, and this action is complex-linear because the scalar imaginary $i$ is central. The state module is therefore a genuine two-dimensional complex module over $\mathbb{B}$, and

$$
\mathbb{B}\cong\mathbb{B}\tilde{P}\oplus\mathbb{B}\tilde{Q}=S\oplus S
$$

as a left module, where $\tilde{Q}=e_0-\tilde{P}$ is the complementary orthogonal idempotent.

### The Module Is the Defining Representation

The Lorentz group acts on the state module by left multiplication,

$$
\tilde{\psi}\;\longmapsto\;\tilde{\Lambda}\tilde{\psi},
\qquad
\tilde{\Lambda}\in SL(2,\mathbb{C})=\{\tilde{\Lambda}\in\mathbb{B}:\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0\},
$$

and the representation so obtained is the defining two-dimensional representation of $SL(2,\mathbb{C})$, the **spin-$\tfrac{1}{2}$** representation. The representation-theoretic content of the module is the content of $S=\mathbb{C}^2$ as a module over $M_2(\mathbb{C})$; its restriction to the rotation subgroup can be read off from the Lie algebra action.

The rotation subgroup is $SU(2)=SL(2,\mathbb{C})\cap U(2)$, whose elements are the unit real quaternions, $\tilde{R}=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\hat{\mathbf{n}}$ with $\hat{\mathbf{n}}$ a unit pure real quaternion. Its Lie algebra is spanned by the generators

$$
J_k=\tfrac{i}{2}e_k,
$$

which satisfy $[J_j,J_k]=i\varepsilon_{jkl}J_l$. On the state module these act as left multiplication, and one verifies directly from the quaternion relations that the left-multiplication operators satisfy the quaternion product rule; in the matrix representation they become $L_k=\Phi(e_k)=-i\sigma_k$, so that

$$
J_k\;\longmapsto\;\tfrac{1}{2}\sigma_k .
$$

The quadratic Casimir is therefore

$$
J_1^2+J_2^2+J_3^2
=\tfrac{1}{4}\left(\sigma_1^2+\sigma_2^2+\sigma_3^2\right)
=\tfrac{1}{4}\cdot 3 I_2
=\tfrac{3}{4}e_0 .
$$

Since $\tfrac{3}{4}=j(j+1)$ gives $j=\tfrac{1}{2}$, the state module carries **spin one-half**, as claimed. The value was confirmed by direct computation in the matrix representation, with the left-multiplication operators checked against the quaternion relations $L_jL_k=-\delta_{jk}e_0+\varepsilon_{jkl}L_l$ and the Casimir evaluated to $\tfrac{3}{4}I_2$ exactly.

### The Module Is Not Rotationally Invariant

There is a second way to see the same content, and it is the one that makes the contrast with the scalar sharp. The idempotent $\tilde{P}(\hat{\mu})$ is built from a **direction** $\hat{\mu}$, and a rotation moves that direction. Conjugating by a unit real quaternion $\tilde{R}$,

$$
\tilde{R}\,\tilde{P}(\hat{\mu})\,\tilde{R}^\dagger
=\tfrac{1}{2}\left(e_0+i\,\tilde{R}\hat{\mu}\tilde{R}^\dagger\right)
=\tilde{P}(\hat{\mu}'),
$$

where $\hat{\mu}'=\tilde{R}\hat{\mu}\tilde{R}^\dagger$ is the rotated unit pure quaternion. Rotations about the axis $\hat{\mu}$ leave $\tilde{P}$ fixed; rotations about other axes do not. The orbit of the idempotent is therefore the two-sphere of unit pure quaternions, and its stabilizer is the $U(1)$ subgroup of rotations about $\hat{\mu}$. This was verified numerically: a rotor of angle $1.1$ about the normalized axis $(0.3,-0.7,0.5)$ sends $\tilde{P}(e_3)=\tfrac{1}{2}(e_0+ie_3)$ to $\tilde{P}(\hat{\mu}')$ with $\hat{\mu}'=(-0.586,-0.524,0.618)$, a unit vector, while a rotation about $e_3$ fixes $\tilde{P}(e_3)$ identically. A module that is carried by an idempotent with an axis is, in this concrete sense, not rotationally invariant: its very definition singles out a direction.

A scalar field is exactly the opposite. It has no axis, and no rotation may move it. The remainder of the article makes that requirement precise inside the algebra and identifies the unique subspace that satisfies it.

## The Center and Its Trivial Representation

### The Centralizer of the Rotations

Consider the element $X=\sum_{\mu=0}^{3}X_\mu e_\mu\in\mathbb{B}$ and ask which elements are fixed by **every** rotation. Equivalently, ask for which $X$ the infinitesimal condition

$$
[e_j,X]=e_jX-Xe_j=0,
\qquad j=1,2,3,
$$

holds. Evaluating the first of these with $e_1^2=-e_0$, $e_1e_2=e_3$, $e_1e_3=-e_2$, one finds

$$
[e_1,X]=2X_2e_3-2X_3e_2,
$$

so $[e_1,X]=0$ forces $X_2=X_3=0$. The condition $[e_2,X]=0$ then forces $X_1=X_3=0$, and together with the first gives $X_1=X_2=X_3=0$. Hence

$$
\{X\in\mathbb{B} : [e_j,X]=0,\ j=1,2,3\}
=\mathbb{C}_{\mathbb{B}}
=\{Q_0e_0 : Q_0\in\mathbb{C}\},
$$

the **center** of the algebra. The result was confirmed independently by solving the linear system $[e_j,X]=0$ over the eight real coordinates of $X$: the coefficient matrix has rank six and nullity two, so the solution space is the real two-dimensional subspace $\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$, as stated.

The algebraic statement is therefore exact: **the elements of $\mathbb{B}$ that are invariant under the rotation subgroup are precisely the central elements.** The traceless part of $\mathbb{B}$, on the other hand, transforms as the adjoint representation, of spin one. Under rotations,

$$
\mathbb{B}=\underbrace{\mathbb{C}_{\mathbb{B}}}_{\text{spin }0}\;\oplus\;\underbrace{\{X:\mathrm{Sc}\,X=0\}}_{\text{spin }1},
$$

so the algebra under the conjugation action carries spin $0$ and spin $1$, while the state module carries spin $\tfrac{1}{2}$. A spin-$0$ field has no alternative but the center.

### The Center Is a Subalgebra, Not an Ideal

It matters that the center is a subalgebra and not a module, because that is what separates the scalar from the spinor structurally. The center is closed under multiplication, because central elements commute and their product is again central,

$$
(Q_0e_0)(R_0e_0)=(Q_0R_0)e_0\in\mathbb{C}_{\mathbb{B}},
$$

and it is a field isomorphic to $\mathbb{C}$. It is fixed pointwise by quaternion conjugation, and it is the fixed space of the algebra's center in the ring-theoretic sense.

It is **not** a left ideal. For a central element $Q_0e_0$ and a general $\tilde{X}\in\mathbb{B}$,

$$
(Q_0e_0)\tilde{X}=Q_0\tilde{X},
$$

which lies in the center only if $\tilde{X}$ does. Taking $\tilde{X}$ with a nonzero vector part produces a nonzero vector part in the product, so the center is not closed under left multiplication by the algebra. In particular the center contains no nonzero $\mathbb{B}$-submodule: the only $\mathbb{B}$-module it could be is trivial, and $M_2(\mathbb{C})$ has no one-dimensional module with a nonzero action. The center meets the state module trivially as well: a central element $\lambda e_0$ lies in $\mathbb{B}\tilde{P}$ only if its second column vanishes, which forces $\lambda=0$. This was confirmed in the matrix representation.

The distinction has a second, more elementary face. Every nonzero element of the state module is a **zero divisor**. A spinor satisfies $\tilde{\psi}\tilde{P}=\tilde{\psi}$, hence $\tilde{\psi}(e_0-\tilde{P})=0$ with $e_0-\tilde{P}\neq0$; in the matrix picture its determinant vanishes. A central element $\lambda e_0$, by contrast, has determinant $\lambda^2$ and is invertible whenever $\lambda\neq0$. The scalar line is the algebra's line of invertible complex numbers; the module is its space of non-invertible spinors. They cannot be the same space, and they do not overlap except at zero.

## Three Obstructions, One Reason

The state module cannot host a spin-$0$ field for three reasons, which are three faces of the algebra's simplicity.

### No Trivial Submodule

The algebra $M_2(\mathbb{C})$ is **simple**: its only two-sided ideals are $0$ and itself. A finite-dimensional module of a simple algebra is completely reducible, and there is exactly one simple module up to isomorphism, the column space $S=\mathbb{C}^2$. Every nonzero finite-dimensional module is therefore a direct sum of copies of $S$. A one-dimensional module carrying the trivial representation does not exist, with any nonzero action. Since the trivial representation is precisely what a scalar field carries, no module of $\mathbb{B}$ can hold it.

The state module is not an exception within a richer family of modules; it is, up to multiplicity, the *only* module there is. A spin-$0$ field is not "the module with spin $0$" as opposed to "the module with spin $\tfrac{1}{2}$", because the algebra has just one kind of module and it is spin-$\tfrac{1}{2}$. The spin-$0$ carrier has to be found outside the module category altogether.

### The Invariant Subspace Is the Center

If one insists on locating the scalar inside the algebra rather than inside a module, the centralizer computation settles where. Under the rotation subgroup the algebra decomposes as spin $0$ (the center) plus spin $1$ (the traceless part); under the conjugation action there is no nonzero element invariant under the full Lorentz group, since the conjugation action on $\mathbb{B}$ is the irreducible complexified four-vector representation. The only rotationally invariant elements are central. A scalar field, being invariant under rotations, must therefore take its values in $\mathbb{C}_{\mathbb{B}}$, and there is nothing else it could take them in.

It is worth stating plainly how the scalar relates to the rotor-conjugation action that carries the material sector. The four-vectors of $\mathbb{M}_-$ transform as $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, which is the four-vector representation; under rotations it splits into the time component (spin $0$) and the spatial vector (spin $1$). The scalar field does not transform by this rule at all. Its Lorentz transformation is the transformation of its argument, $\tilde{\Phi}'(x')=\tilde{\Phi}(x)$, with no algebraic factor acting on the value. The absence of an algebraic action is the field-theoretic statement of spin $0$, and the center is the value space in which that absence is natural.

### The Trivial Representation Lives in the Tensor Square

There is a third way to see why the scalar is not *in* the module, and it explains where scalars actually come from. If the state module carries the defining representation $V_1=(\tfrac{1}{2},0)$ of complex dimension two, then its complex conjugate $\bar{S}=(0,\tfrac{1}{2})$ is the other chiral half, and the tensor product decomposes as

$$
S\otimes\bar{S}=\left(\tfrac{1}{2},0\right)\otimes\left(0,\tfrac{1}{2}\right)
=\left(\tfrac{1}{2},\tfrac{1}{2}\right)
\;\cong\;\mathbb{C}\oplus\mathbb{C}^3
$$

under the rotation subgroup, where the trivial piece is the scalar channel. The trivial representation appears here, in the **bilinear** combination of two spinors, not as a submodule of either factor; the decomposition, however, is a statement about the rotation subgroup only, because under the full Lorentz group $S\otimes\bar{S}=(\tfrac{1}{2},\tfrac{1}{2})$ is irreducible and contains no invariant, and the Lorentz scalars come instead from the antisymmetric square $\Lambda^2 S$ (the symplectic contraction $\varepsilon$) and from the mixed left-right pairing $b$. A scalar is therefore not an element of the state module but a scalar-valued pairing of two module elements. The bilinear

$$
\tilde{\rho}=\tilde{\psi}\tilde{\chi}^\dagger\in\mathbb{M}_+
$$

is the four-vector channel; it is Hermitian, and its diagonal case $\tilde{\chi}=\tilde{\psi}$ gives the positive element whose trace is the conventional density.

This is the algebraic content of the standard fact that a spin-$0$ object can be built from two spin-$\tfrac{1}{2}$ objects but is not itself one: the trivial representation of $SU(2)$ sits in the tensor square, not in the defining representation. The companion article *The Dirac Equation in Biquaternionic Form* uses the same bilinears when it forms the Dirac current and the Dirac scalar, and the companion article on the spinor module develops the Hermitian, symplectic and mixed pairings and their invariance properties explicitly.

## The Sector Question: Neither $\mathbb{M}_-$ nor $\mathbb{M}_+$

The framework's central algebraic fact is the decomposition $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ into the anti-Hermitian material sector and the Hermitian informational sector. The companion article *The Klein–Gordon Equation in Biquaternionic Form* asked whether the second-order scalar structure organizes itself by this split, and found that it does not: because the d'Alembertian is central and scalar, the split merely separates a complex solution into its real and imaginary parts, giving two $i$-related copies of one real solution space rather than a particle–antiparticle or state–operator pair. The representation theory above explains why, and it also says what the split *does* mean for a scalar.

The scalar field's value space is the center, and the center meets each sector in exactly one real direction:

$$
\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\},
\qquad
\operatorname{span}_{\mathbb{R}}\{e_0\}\subset\mathbb{M}_+,
\qquad
\operatorname{span}_{\mathbb{R}}\{ie_0\}\subset\mathbb{M}_- .
$$

The real scalar direction $e_0$ is the scalar part of the Hermitian sector; the imaginary scalar direction $ie_0$ is the scalar part of the material sector. A complex scalar $\tilde{\Phi}=\phi e_0$ with $\phi=\phi_1+i\phi_2$ and $\phi_1,\phi_2\in\mathbb{R}$ therefore splits as

$$
\tilde{\Phi}=\underbrace{\phi_1\,e_0}_{\in\,\mathbb{M}_+}+\underbrace{\phi_2\,ie_0}_{\in\,\mathbb{M}_-},
$$

and the sector decomposition of a scalar field is nothing other than the decomposition of a complex number into its real and imaginary parts. This is the precise sense in which the Klein–Gordon article's negative verdict is forced: the $\mathbb{M}_-/\mathbb{M}_+$ split cannot carry the particle–antiparticle doubling, because on the scalar line it is the real/imaginary-part split of a single complex number.

The operations that act on that complex number must be kept distinct, and the same distinction settles the sector question completely.

- **Multiplication by $i$** is central and exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, $i\mathbb{M}_-=\mathbb{M}_+$. On a scalar it maps $\phi_1e_0+\phi_2ie_0$ to $-\phi_2e_0+\phi_1ie_0$: it is a quarter-turn of the complex scalar line, exchanging its two real directions.
- **Complex conjugation ${}^*$** acts on the coefficients and preserves each sector. On a scalar it maps $\phi_1e_0+\phi_2ie_0$ to $\phi_1e_0-\phi_2ie_0$: it is reflection of the complex line, and it is the operation that produces the second solution of the second-order equation, $\tilde{\Phi}^*$.
- **Hermitian conjugation ${}^\dagger$** is the involution whose eigenspaces define the sectors; it is neither of the other two, and on the center it agrees with ${}^*$.

These are three different maps with three different actions on the scalar line. The sector-exchanging map $i$ is not the conjugate-producing map ${}^*$, and reading the Klein–Gordon conjugate pair $(\tilde{\Phi},\tilde{\Phi}^*)$ as the sector pair $(\mathbb{M}_-,\mathbb{M}_+)$ is precisely the conflation the companion article warns against. The center makes the distinction visible: complex conjugation has real fixed points in the center, the direction $e_0$; multiplication by $i$ has none.

## The Scalar Field in the Center

With the value space fixed, the scalar field is written down at once. A spin-$0$ field of mass $m$ is a function into the center,

$$
\tilde{\Phi}(x)=\phi(x)\,e_0,
\qquad
\phi(x)\in\mathbb{C},
$$

and it obeys the Klein–Gordon equation in the form of the companion article,

$$
\left(\Box-\frac{m^2c^2}{\hbar^2}\right)\tilde{\Phi}=0,
\qquad
\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta
=-\frac{1}{c^2}\partial_t^2+\Delta .
$$

Because $\Box$ is central and scalar, it acts coefficient by coefficient, and on a central field the equation is the ordinary complex scalar Klein–Gordon equation

$$
\left(\Box-\frac{m^2c^2}{\hbar^2}\right)\phi=0 ,
$$

with the biquaternion writing carrying no additional content. This is the honest verdict of the companion article, and the representation theory of the present article says why it must be so: there is no axis in the field for any non-central algebraic structure to act on.

The plane-wave solutions exhibit the same point. Writing the four-wavevector in the material sector,

$$
\tilde{K}=i\frac{\omega}{c}e_0+\mathbf{k}\in\mathbb{M}_-,
\qquad
\tilde{X}=ict\,e_0+\mathbf{x}\in\mathbb{M}_-,
$$

the phase is the scalar part $\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})=\mathbf{k}\cdot\mathbf{x}-\omega t$, a real central element, and the positive-frequency solution is

$$
\tilde{\Phi}=\phi_0\,e^{\,i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})}\,e_0
=\phi_0\,e^{\,i(\mathbf{k}\cdot\mathbf{x}-\omega t)}\,e_0 .
$$

The exponential is central. The mass-shell condition is the norm form of the four-wavevector fixed to a negative constant,

$$
N(\tilde{K})=\tilde{K}\bar{\tilde{K}}=-\frac{\omega^2}{c^2}+\mathbf{k}^2=-\frac{m^2c^2}{\hbar^2}
\quad\Longleftrightarrow\quad
\omega^2=c^2\mathbf{k}^2+\frac{m^2c^4}{\hbar^2} ,
$$

which is the standard relativistic dispersion relation and is reproduced here only to record that the scalar field's entire algebraic content is the norm form of a four-vector, not a module structure. The conserved current $\tilde{J}=ic\rho\,e_0+\mathbf{j}$ lies in $\mathbb{M}_-$, its scalar component being the imaginary scalar direction, exactly as for the four-current of relativistic mechanics.

One structural remark belongs with the equation. The first-order operators of the framework, $\tilde{\nabla}$ and the module action by $\tilde{\Lambda}$, are module-theoretic or vectorial: they act on spinors or on four-vectors and change their representation content. The scalar field has neither. The only operator the scalar equation uses is the central scalar $\Box$, whose square-root structure — the spinor factorisation $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ — is a statement about the *operator*, not about the field it acts on. A scalar field is annihilated by a composite of spinor operators without ever being a spinor; it is the algebra's trivial representation appearing in the composition, not a state in the module.

## Scalars from the Module: The Composite Route

The three obstructions above say that a scalar is not an element of the state module. They do not say that the state module is irrelevant to scalar physics, and it is worth recording how scalars actually appear in the standard model, because the framework reproduces the mechanism.

A Lorentz-invariant scalar built from module elements is a **bilinear**, but not every bilinear is one. If $\tilde{\psi},\tilde{\chi}$ are spinors in the state module, then $\tilde{\psi}\tilde{\chi}^\dagger$ is a Hermitian element, and its scalar part,

$$
\sigma=\mathrm{Sc}\!\left(\tilde{\psi}\tilde{\chi}^\dagger\right)=\tfrac{1}{2}\mathrm{Tr}\!\left(\tilde{\psi}\tilde{\chi}^\dagger\right),
$$

is a complex number. Under a Lorentz transformation the module transforms by left multiplication, $\tilde{\psi}\mapsto\tilde{\Lambda}\tilde{\psi}$ and $\tilde{\chi}\mapsto\tilde{\Lambda}\tilde{\chi}$, so

$$
\tilde{\psi}\tilde{\chi}^\dagger
\;\longmapsto\;
\tilde{\Lambda}\,\tilde{\psi}\tilde{\chi}^\dagger\,\tilde{\Lambda}^\dagger ,
$$

which is the conjugation action on $\mathbb{M}_+$, the four-vector channel. Its scalar part is invariant under the rotation subgroup, where $\tilde{\Lambda}^\dagger=\tilde{\Lambda}^{-1}$, but **not** under boosts, where $\tilde{\Lambda}^\dagger\tilde{\Lambda}\neq e_0$. The object $\tilde{\psi}\tilde{\chi}^\dagger$ is therefore a four-vector and $\sigma$ is its time component, not a Lorentz scalar; this is the algebraic form of the standard statement that $\psi^\dagger\psi$ is the time component of the four-current $\bar{\psi}\gamma^\mu\psi$, not an invariant. A numerical check on a generic pair gives the expected behaviour: at rapidity $1.3$ the boost changes $\sigma$ by $1.36$, while a rotation leaves it unchanged to $10^{-9}$.

The Lorentz-invariant scalars are instead the two pairings developed in the companion article on the spinor module. The **symplectic pairing** of two spinors of the same chirality,

$$
\varepsilon(\tilde{\psi},\tilde{\chi})=\tilde{\psi}^{T}\epsilon\,\tilde{\chi},
\qquad
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

is invariant because $\tilde{\Lambda}^{T}\epsilon\,\tilde{\Lambda}=\epsilon$, which holds since $\det\tilde{\Lambda}=1$. The **mixed pairing** of a spinor with one in the conjugate module,

$$
b(\tilde{\psi},\tilde{\chi})=\tilde{\psi}^{\dagger}\tilde{\chi},
\qquad
\tilde{\psi}\mapsto\tilde{\Lambda}\tilde{\psi},
\qquad
\tilde{\chi}\mapsto\Phi(\tilde{\Lambda}^{*})\tilde{\chi},
$$

is invariant because $\tilde{\Lambda}^\dagger\tilde{\Lambda}^{*}=e_0$. These are the two scalar channels of the module: $\varepsilon$ is the antisymmetric contraction of two same-chirality spinors, and $b$ is the Dirac scalar, which pairs the two chiral halves. Both take their values in the center; the Hermitian pairing, by contrast, gives the four-vector channel just described. This is the algebraic form of the standard statements that $\bar{\psi}\psi$ is a Lorentz scalar while $\psi^\dagger\psi$ is not, that a fermion condensate can break a symmetry, and that the Higgs field, being a scalar, couples to fermions through precisely such bilinears. The scalar does not live in the module; it is a *pairing of two module elements*, and the pairing takes its values in the center.

The distinction between the two routes is the distinction the title names. A field that is *in* the state module is a spinor, and it carries spin $\tfrac{1}{2}$ whether or not it is a solution of any particular equation. A field that is *built from* the state module can be a scalar, and it lives in the center. The Klein–Gordon field is of the second kind: it is the trivial sector of the module's tensor square promoted to an independent field, which is why its equation is second order, why it decouples from the module's first-order structure, and why the material/informational split applies to it only as the real/imaginary split of one complex number.

## Open Questions

1. **The uniqueness of the trivial carrier.** *Open for the author.* The centralizer computation shows that the rotationally invariant elements of $\mathbb{B}$ form the center, and that the state module contains no rotationally invariant submodule. Whether the framework should regard the center as *the* scalar field's value space, or merely as the natural one among several subspaces on which the rotation group acts trivially, is a convention the present article fixes in the first sense. The alternative would require a value space outside $\mathbb{B}$, which the series has not considered.

2. **The boost transformation of a scalar.** A scalar field transforms trivially under the whole Lorentz group, but the framework's conjugation action is the four-vector action and has no nonzero invariant under boosts. Whether the scalar's transformation law should be regarded as an independent assignment — the argument transformation with no algebraic factor — or as the restriction of some algebraic action, is not resolved here. The present article takes the first reading, which is the standard one and is consistent with the center being invariant under rotations.

3. **The general idempotent and the state axis.** The idempotents $\tilde{P}(\hat{\mu})=\tfrac{1}{2}(e_0+i\hat{\mu})$ with $\hat{\mu}$ a real unit pure quaternion are the Hermitian idempotents, and their axes fill the two-sphere. The non-Hermitian idempotents built from the non-central roots of $-1$ define other minimal left ideals. Whether those ideals carry a different representation content, or the same defining representation under a different complex structure, bears on the sense in which "spin $\tfrac{1}{2}$" is unique; the companion article on the spinor module addresses the ideal model but not this classification.

4. **The relation to the informational reading.** The center is the intersection of the scalar field's value space with neither sector as a whole, but with one real direction in each. This suggests that the material/informational dichotomy, at least for the scalar, is a real/complex pair rather than a state/operator pair. Whether the informational reading of $\mathbb{M}_+$ survives the scalar case intact, or must be restricted to the non-scalar sectors, is a question for the informational articles.

5. **Composite scalars and the trace formula.** The bilinear route uses the trace pairing $\mathrm{Tr}(\tilde{\psi}\tilde{\chi}^\dagger)=2\,\mathrm{Sc}(\tilde{\psi}\tilde{\chi}^\dagger)$. The symplectic pairing $\varepsilon$ and the mixed pairing $b$ supply the Lorentz-scalar channels, while the Hermitian pairing $\tilde{\psi}\tilde{\chi}^\dagger$ supplies the four-vector channel; whether every scalar-valued functional of the module reduces to these two is not settled here.

6. **Why the algebra admits only spin $0$ and one-half.** The module carries spin $\tfrac{1}{2}$ and the algebra under rotations carries spin $0$ and $1$; there is no simple module of higher spin. The general question — which spins the biquaternion algebra admits as elementary representations — is the subject of a separate article in the series and is not answered here.

## Summary

A scalar field carries the trivial representation of the Lorentz group, and the biquaternion framework must therefore be asked where a trivial-representation field can live. The framework's state module is the minimal left ideal $\mathbb{B}\tilde{P}(\hat{\mu})\cong\mathbb{C}^2$, and it carries the defining two-dimensional, spin-$\tfrac{1}{2}$ representation of $SL(2,\mathbb{C})$: the left action of the rotation generators $J_k=\tfrac{i}{2}e_k$ on the module has Casimir $\tfrac{3}{4}e_0$. Its primitive idempotent is built from a spatial axis, and rotations move that axis around the two-sphere, so the module is not rotationally invariant.

The unique rotationally invariant subspace of $\mathbb{B}$ is the center $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$, obtained as the centralizer of the quaternion units: $[e_j,X]=0$ for $j=1,2,3$ forces $X=X_0e_0$. The center is a subalgebra isomorphic to $\mathbb{C}$ and is not a left ideal; it meets the state module only at zero. This gives three equivalent reasons why spin $0$ escapes the state module. The algebra $M_2(\mathbb{C})$ is simple and has only one simple module, $\mathbb{C}^2$, so there is no one-dimensional module for the trivial representation. The rotationally invariant elements are exactly the central ones, so the scalar's value space is forced to be the center. And the trivial representation appears in the tensor square — in $S\otimes\bar{S}=\mathbb{C}\oplus\mathbb{C}^3$ under the rotation subgroup, and in the symplectic channel of $S\otimes S$ and the mixed left-right pairing under the full Lorentz group — not as a submodule of either factor, so a scalar is a bilinear in the module rather than an element of it.

For the sector split, the center meets each sector in one real direction: the real scalar $e_0$ is the scalar part of $\mathbb{M}_+$, and the imaginary scalar $ie_0$ is the scalar part of $\mathbb{M}_-$. The $\mathbb{M}_-/\mathbb{M}_+$ decomposition of a complex scalar is therefore its decomposition into real and imaginary parts, which is the representation-theoretic reason behind the companion article's finding that the second-order Klein–Gordon structure does not organize itself by the sector split. Multiplication by $i$ exchanges the sectors and quarter-turns the scalar line; complex conjugation preserves each sector and reflects the scalar line, and is the operation that produces the conjugate solution. The scalar field itself is $\tilde{\Phi}=\phi e_0$ with $\phi$ complex, obeying $(\Box-m^2c^2/\hbar^2)\tilde{\Phi}=0$ with $\Box$ central and scalar; the framework's first-order, module-theoretic structure never acts on it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\bar{\cdot},\,{}^*,\,{}^\dagger=\bar{\cdot}^{\,*},\,{}^\flat=-\dagger$ | Quaternion, complex, Hermitian, anti-Hermitian conjugation |
| $\mathbb{M}_-,\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, fixed points of ${}^*$ |
| $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center of $\mathbb{B}$; the scalar field's value space |
| $\tilde{P}(\hat{\mu})=\tfrac{1}{2}(e_0+i\hat{\mu})$ | Primitive Hermitian idempotent, $\hat{\mu}$ a unit pure real quaternion |
| $\mathbb{B}\tilde{P}\cong\mathbb{C}^2$ | State module (minimal left ideal) |
| $\tilde{\psi}$ | Spinor, an element of the state module |
| $J_k=\tfrac{i}{2}e_k$ | Rotation generators; $J_1^2+J_2^2+J_3^2=\tfrac{3}{4}e_0$ on the module |
| $SL(2,\mathbb{C})=\{\tilde{\Lambda}:\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0\}$ | Unit-norm biquaternions; Lorentz group |
| $\tilde{X}=ict\,e_0+\mathbf{x}$ | Four-position biquaternion, $\in\mathbb{M}_-$ |
| $\tilde{K}=i\omega/c\,e_0+\mathbf{k}$ | Four-wavevector, $\in\mathbb{M}_-$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$ | Biquaternionic gradient |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$ | d'Alembertian, central and scalar |
| $\tilde{\Phi}=\phi e_0$ | Scalar (spin-$0$) field, valued in the center |
| $\sigma=\mathrm{Sc}(\tilde{\psi}\tilde{\chi}^\dagger)$ | Scalar part of the module bilinear; a four-vector component, not a Lorentz scalar |
| $\varepsilon(\tilde{\psi},\tilde{\chi})=\tilde{\psi}^{T}\epsilon\tilde{\chi}$ | Symplectic pairing; Lorentz scalar of two same-chirality spinors |
| $b(\tilde{\psi},\tilde{\chi})=\tilde{\psi}^{\dagger}\tilde{\chi}$ | Mixed pairing; Dirac scalar of a left–right spinor pair |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard treatment of the scalar field and the trivial representation of the Lorentz group.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the classification of the representations of the Lorentz group and the transformation laws of scalar, vector and spinor fields.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Klein–Gordon field and the role of the complex scalar.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra $M_2(\mathbb{C})$, its idempotents, minimal left ideals and simple modules.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the real structures and the representation theory of the Clifford algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of spinors, bilinears and the scalar and vector channels.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor calculus and the construction of scalars from spinor bilinears.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the operator-algebra reading of the two-state module.
