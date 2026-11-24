# __States, Observables and the Born Weight__

## Introduction

This entry is the third of section I.12, and it reads the informational sector as a state space. The sector is the Hermitian half of the algebra, four real dimensions, and it carries both of the objects that a physical theory of probability needs: the thing that is measured and the thing that is prepared. The entry states what the algebra supplies to each of them, what it refuses, and which of the standard quantum statements are theorems rather than postulates.

$$
\mathbb{B}_{\Psi}=\{\tilde Q\in\mathbb{B}:\tilde Q^{*}=\tilde Q\},
\qquad
\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi,
\qquad
\tilde{Ϛ}_\Psi=\tfrac12\bigl(e_t+i\vec s_{\Psi}\bigr),
\qquad
h_t\in\mathbb{R},\ \ \vec h_\Psi,\vec s_{\Psi}\in\mathbb{R}^{3}.
$$

The first claim is that a state is an element and not a vector. The state is a positive element of the sector, normalised against the unit, and its four real numbers are the slice of a cone at unit weight. The unit ball that these numbers fill is the Bloch ball, its boundary is the pure states, and its centre is the maximally mixed state. The state vector of the standard formalism is a different object in the same algebra, and the map between them loses exactly one thing: a central phase.

The second claim is that the observable is an element of the same space. An observable is a Hermitian element $h_t e_t+i\vec h_\Psi$, and its two eigenvalues are $h_t\pm\lvert\vec h_\Psi\rvert$. State and observable are therefore two points of one real four-dimensional space, paired by one symmetric positive form. Nothing here is an operator on a Hilbert space, and the pairing is symmetric between its two slots.

The third claim is that the Born weight is that pairing, normalised. For a state and an observable the weight is

$$
p=\frac{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\tilde H_\Psi^{*}\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\bigr)}
=h_t+\vec s_{\Psi}\cdot\vec h_\Psi,
$$

and for a measurement along a unit axis $\vec u$ it is the analyser transmission law $p_\pm=\tfrac12(1\pm\vec u\cdot\vec s_{\Psi})$. Reality, positivity and normalisation follow from the algebra. That these numbers are observed frequencies does not.

The fourth claim is that the two forms of the sector divide the work. The Hermitian form, positive definite of inertia $(4,0)$, supplies the probabilities. The quaternionic norm, indefinite of inertia $(1,3)$, supplies the geometry and the mixedness. On the state slice the second is

$$
N(\tilde{Ϛ}_\Psi)=\tfrac14\bigl(1-\lvert\vec s_{\Psi}\rvert^{2}\bigr)=\tfrac12 S_{\mathrm{lin}}(\tilde{Ϛ}_\Psi),
$$

so the interval of a state is half its linear entropy, and the cone of the norm is the boundary of the ball.

The fifth claim is that no physical state is spacelike. The positivity condition $h_t\ge\lvert\vec h_\Psi\rvert$ is the condition that the state lie inside or on the future cone of the norm, and the pure states are exactly its null elements. The state space is therefore a causal region of the sector, and the statement that a state has a positive weight is the statement that it lies in the future cone. A state outside the cone would have a negative eigenvalue, and there are no such states.

The sixth claim is that the state space is a slice, and that the slice is not Lorentz-invariant. Positivity is preserved by every invertible congruence, normalisation only by the unitary group, and the state space is their intersection: it is preserved by $U(2)$ and by nothing larger. A boost maps the unit-scalar slice to a different hyperplane, and a mixed state that is carried by a boost and renormalised has a different Bloch radius. The pure states survive because they are rays; the mixed ones do not.

The seventh claim is that a particle of definite velocity has a state, and the velocity is its Bloch vector. For a particle of mass $m$ and velocity $\vec v$ the state element is $\tfrac12(e_t+i\vec s_{\Psi})$, with

$$
\vec s_{\Psi}=-\frac{\vec v}{c},
\qquad
N(\tilde{Ϛ}_\Psi)=\tfrac14\Bigl(\frac{mc^{2}}{E}\Bigr)^{2},
\qquad
S_{\mathrm{lin}}(\tilde{Ϛ}_\Psi)=\tfrac12\Bigl(\frac{mc^{2}}{E}\Bigr)^{2}.
$$

A timelike momentum gives a positive state, a null one gives a pure state, and a spacelike one gives nothing. Mass is what makes the state mixed, and the rest frame is the maximally mixed state.

The eighth claim is that the imaginary unit of the dynamics is forced. The unit $\tilde Z$ of the state-vector equation must be central if the flow is to preserve the norm for every Hermitian generator, and the centre contains exactly the two roots $\pm i$. Over the real quaternions the hypothesis fails, because the Hermitian elements there are too few to generate the algebra, and a non-central root does the job. The complex number field is not chosen; it is what a norm-preserving flow requires.

The strongest objection is that this is $M_2(\mathbb{C})$ with new letters. The algebra is isomorphic to the two-by-two complex matrices, and every formula above has a matrix reading. A dictionary is not a derivation. Three statements here are not translations. The first is that the positivity cone and the future cone of the norm have the same boundary, which is a statement about this norm and this slice. The second is that the split between states and observables is the split between the two signs of one conjugation, so the two kinds of object are two halves of one space and not two different constructions. The third is the centrality theorem: the unit of the flow is forced into the centre, and the centre is what makes the scalar field complex.

A second objection is that the Born rule is not derived here. It is not, and the entry says so in the section where it computes it. What is derived is the form of the assignment: given the pairing and the idempotents, realness, positivity, normalisation and the analyser law follow. The link from the numbers to frequencies is an empirical postulate here exactly as it is in the standard formalism. The framework's contribution is that the pairing and the idempotents are not chosen either.

A third objection is that the reading of mass as mixedness overreaches. It is a reading of a correspondence, and the entry states its scope. The map from a four-momentum to a state is algebraic and exact; the identification of that state with the spin state of a particle in a laboratory is an interpretation, and it is labelled as one. The theorem is the arithmetic of the map, and the arithmetic is checked.

The interpretation labels continue the category's sequence. The third and last entry of section I.12 begins after the twelve labels of the previous entry, so it carries I.12.m to I.12.y. §*The Interpretations* states each of the thirteen, and §*The Limits* states what the readings do not carry.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the sector, its basis, its blocks and its position among the six subspaces | [Subspaces and Decompositions of the Biquaternion Algebra](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html) |
| the norm, the invertibles, the zero-divisor cone and the inverse formula | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| the four forms, their Gram matrices and their inertia on the sector | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| the positive cone as an ordered set with its order unit | [Self-Adjoint Elements and the Positive Cone](../articles_maths/self-adjoint-elements-and-the-positive-cone.html) |
| the states as positive functionals and their normalisation | [States and Positive Functionals on an Involutive Algebra](../articles_maths/states-and-positive-functionals-on-an-involutive-algebra.html) |
| the effect interval, the orthomodular lattice and the projection lattice | [Effect Algebras and Orthomodular Lattices](../articles_maths/effect-algebras-and-orthomodular-lattices.html) |
| the extremal rays of a cone and the convex structure of a slice | [Cones, Extremal Rays and the Choquet Theory](../articles_maths/cones-extremal-rays-and-the-choquet-theory.html) |
| the eigenvalue decomposition, the idempotents and the degenerate case | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| the spectrum, the centraliser and the semisimple–nilpotent split | [The Spectrum](../articles_maths/the-spectrum-of-a-biquaternion.html) |
| the positive square root and the polar decomposition of an element | [Positive Operators and the Square Root](../articles_maths/positive-operators-and-the-square-root.html) |
| the completely positive maps, the Kraus form and the dilation | [Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint](../articles_maths/completely-positive-maps-of-a-hermitian-algebra-with-hermitian-adjoint.html) |
| the centraliser of a generic element and its dimension | [The Centraliser in the Biquaternion Algebra](../articles_maths/the-centraliser-in-the-biquaternion-algebra.html) |
| the rotor conjugation, the double covers and the Lorentz action | [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) |
| the bracket and the Jordan structure of the two halves | [Lie Algebras of Sesqualgebras](../articles_maths/lie-algebras-of-sesqualgebras.html) |
| the K norm and the coincidence of the two null sets on the material sector | [Kr-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/kr-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| the topology of the null set and its two components | [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html) |

Five physics companions are quoted and not rebuilt. The sector read as a state space with its observables and its probabilities is *The Informational Sector: States, Observables and Probability*. The derivation of the weight from the Hermitian form, with the comparison against the Hilbert-space statement, is *The Born Rule from the Hermitian Form*. The geometry of the slice is *The Bloch Ball as the Normalised Slice of the Future Light Cone* and *The Fubini–Study Geometry and the Biquaternion Norm*. The norm-preservation theorem and its flow form are *Unitarity from Centrality*. What this entry adds to those five is the position of the sector in the category: which properties are inherited from the algebra, which from the involution that defines the sector, and which are the sector's alone. It also states the correspondence with the material sector, which is the previous entry of this section.

## The Results in Brief

The sector is a real four-plane of two blocks. The scalar block $\mathbb{R}e_t$ is one-dimensional and carries the weight; the imaginary vector block is three-dimensional and carries the direction. The weight is what normalises, and the direction is what a measurement reads.

| operation | scalar block $\mathbb{R}e_t$ | imaginary vector block | whole sector |
| --- | --- | --- | --- |
| Hermitian form $H$ | $+h_t^{2}$ | $+\lvert\vec h_\Psi\rvert^{2}$ | positive definite, $(4,0)$ |
| quaternionic norm $N$ | $+h_t^{2}$ | $-\lvert\vec h_\Psi\rvert^{2}$ | indefinite, $(1,3)$ |
| plain norm $P$ | $+h_t^{2}$ | $+\lvert\vec h_\Psi\rvert^{2}$ | equal to $H$ on this sector |
| K norm $\mathrm{Kr}$ | $+h_t^{2}$ | $-\lvert\vec h_\Psi\rvert^{2}$ | equal to $N$ on this sector |
| bracket $[\cdot,\cdot]$ | $0$ | $-2\vec h_{\Psi,1}\times\vec h_{\Psi,2}$ | leaves the sector |
| anticommutator $\{\cdot,\cdot\}$ | — | — | stays in the sector |
| product | — | — | stays only for commuting factors |
| central imaginary $i\cdot$ | leaves the sector | leaves the sector | $\mathbb{B}_{\Psi}\to\mathbb{B}_{\Phi}$ |
| scalar part $\mathrm{Sc}$ | $h_t$ | $0$ | reads the weight, forgets the direction |

**Two of the four forms collapse on this sector and two do not.** The plain form equals the Hermitian form because the star is the identity here, and the K norm equals the quaternionic norm for the same reason. The sector therefore carries two distinct real quadratic forms, one positive definite and one indefinite, and the whole entry is an account of which question each of them answers.

The observable has two numbers per axis and one overall. Its eigenvalues are $\eta_{\pm}=h_t\pm\lvert\vec h_\Psi\rvert$, its mean is the scalar part, and its spread is the length of the vector part. No other data is needed, because the spectral theorem for this sector is the completeness of two idempotents.

The state has one radius and one direction. Its eigenvalues are $\tfrac12(1\pm\lvert\vec s_{\Psi}\rvert)$, so the direction is the axis of the spectral decomposition and the radius is the mixedness. A state with a given radius is determined up to a rotation of the axis, and the axis is what a measurement along that axis reads with certainty.

The weight is one bilinear expression. For the state and the observable of the two displays above it is $h_t+\vec s_{\Psi}\cdot\vec h_\Psi$, and the projection case is $p_\pm=\tfrac12(1\pm\vec u\cdot\vec s_{\Psi})$. The scalar part of the observable is the state-independent offset, and the vector part is what the state can predict.

The variance is the transverse component. For the same pair,

$$
\bigl\langle\tilde H_\Psi^{2}\bigr\rangle-\bigl\langle\tilde H_\Psi\bigr\rangle^{2}
=\lvert\vec h_\Psi\rvert^{2}\Bigl(1-\bigl(\vec s_{\Psi}\cdot\vec u_\Psi\bigr)^{2}\Bigr),
$$

which vanishes exactly when the state is pure and the two axes coincide. The noise of a measurement is the part of the observable that the state cannot predict, and it is not a property of either alone.

The geometry of the boundary is the algebra's own. The Fubini–Study line element of the pure states is a quarter of the round metric of the sphere, the complex structure is the commutator, and the symplectic area is finite. The factor of a quarter is the half-angle of the double cover, and the entry states it where it computes it.

Unitarity is a condition on the centre. The conjugation by $\tilde U$ preserves the scalar part exactly when $\tilde U^{*}\tilde U=e_t$, and the flow generated by a Hermitian element preserves the norm for every such element exactly when the unit of the flow is central. Both statements are two-line computations, and both are stated with their proofs.

The relation to the previous entry is exact and it is the entry's structural result. The future cone of the material sector and the state space are two slices of one cone, the causal classes of a four-vector and the purity classes of a state stand in the same order, and the interval of a state is its linear entropy. The two entries of this section are one statement about one cone.

## The Sector and Its Coordinates

The sector is the fixed space of the star. The Hermitian conjugation $\tilde Q\mapsto\tilde Q^{*}$ is a real-linear involution of the algebra, and its $+1$ eigenspace is the informational sector. Every element of the sector is its own star, so on this space the star is the identity map, and every formula that carries a star simplifies without changing.

$$
\mathbb{B}_{\Psi}=\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\},
\qquad
\tilde H_\Psi=h_t\,e_t+i h'_x\vec e_x+i h'_y\vec e_y+i h'_z\vec e_z .
$$

The coordinates are the parameters. There is no dictionary between a coordinate set and a parameter set. The four real numbers $h_t,h'_x,h'_y,h'_z$ are the coefficients themselves, the prime marks the slot that carries the $i$, and the sector's four dimensions are the four slots. The first slot is the weight and the other three are the direction, so the two blocks of the sector are

$$
\mathbb{B}_{\Psi}=\mathbb{R}e_t\oplus\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}
=\mathbb{R}e_t\oplus i\vec K,
$$

where $\vec K$ is the real vector subspace of the material sector. The second block is the imaginary image of the real three-space, so the sector's direction is a real vector multiplied by $i$, and the $i$ is part of the coordinate and not part of the direction.

**The sector is not a subalgebra.** The product of two Hermitian elements is

$$
\tilde H_{\Psi,1}\tilde H_{\Psi,2}
=\bigl(h_{1t}h_{2t}+\vec h_{\Psi,1}\cdot\vec h_{\Psi,2}\bigr)e_t
+i\bigl(h_{1t}\vec h_{\Psi,2}+h_{2t}\vec h_{\Psi,1}\bigr)
-\vec h_{\Psi,1}\times\vec h_{\Psi,2},
$$

and the last term is a real pure quaternion, which is anti-Hermitian. The product therefore falls out of the sector unless the cross product vanishes, that is, unless the two elements commute. The two brackets separate the two cases:

$$
\{\tilde H_{\Psi,1},\tilde H_{\Psi,2}\}\in\mathbb{B}_{\Psi},
\qquad
[\tilde H_{\Psi,1},\tilde H_{\Psi,2}]=-2\,\vec h_{\Psi,1}\times\vec h_{\Psi,2}\in\mathbb{B}_{\Phi}.
$$

The anticommutator closes and the commutator does not. Half the anticommutator is a product on the sector, commutative but not associative, and the sector is a **special Jordan algebra** under it. The commutator lands in the material sector, so the sector is not a Lie algebra either, and the two brackets of one pair of elements always land on opposite sides of the split. The square of an element is the case of two equal arguments, and it stays:

$$
\tilde H_\Psi^{2}=\bigl(h_t^{2}+\lvert\vec h_\Psi\rvert^{2}\bigr)e_t+2h_t\,i\vec h_\Psi .
$$

Every square is a sum of a non-negative weight and a direction. The display above shows it: the scalar part is $h_t^{2}+\lvert\vec h_\Psi\rvert^{2}\ge0$, and the direction is $2h_t\vec h_\Psi$. A square is therefore never negative, and the positive cone of the sector is generated by the squares. This is the algebraic origin of the positivity condition that the next sections use, and it is why the cone of the sector is the object that carries the states.

**The sector has a name.** The product above identifies it as $J_2(\mathbb C)$, the Hermitian $2\times2$ complex matrices under $\tfrac12(MN+NM)$, by

$$
h_te_t+i\vec h_\Psi\ \longmapsto\ \begin{pmatrix}h_t+h_z & h_x-ih_y\\ h_x+ih_y & h_t-h_z\end{pmatrix},
$$

and in the coordinate-free language it is the spin factor $S_3$. The identification fixes what the sector can carry: a Euclidean Jordan algebra has a positive cone, a spectral decomposition and a derivation algebra, and the objects of this article are the cone, the spectrum and the idempotents of that algebra. [The Operators of the Algebra](the-operators-of-the-algebra.html) computes its derivations, which span three dimensions and give $\mathfrak{su}(2)$.

Two of the four forms collapse on the sector. With the star the identity, the Hermitian form is the plain form,

$$
\langle\tilde H_{\Psi,1},\tilde H_{\Psi,2}\rangle_{*}=\mathrm{Sc}\bigl(\tilde H_{\Psi,1}\tilde H_{\Psi,2}^{*}\bigr)=\mathrm{Sc}\bigl(\tilde H_{\Psi,1}\tilde H_{\Psi,2}\bigr)=\langle\tilde H_{\Psi,1},\tilde H_{\Psi,2}\rangle
=h_{1t}h_{2t}+\vec h_{\Psi,1}\cdot\vec h_{\Psi,2},
$$

and the K norm is the quaternionic norm, for the same reason: the coefficient of the temporal slot is real and the three spatial coefficients are imaginary, so taking the modulus of each coefficient and attaching the sign of the slot gives the same numbers as the quaternionic form,

$$
\mathrm{Kr}(\tilde H_\Psi)=h_t^{2}-\lvert\vec h_\Psi\rvert^{2}=N(\tilde H_\Psi).
$$

The two survivors are different forms and they answer different questions. The Hermitian form is positive definite of inertia $(4,0)$, with Gram matrix the identity in the sector's basis. The quaternionic norm is indefinite of inertia $(1,3)$, with the signs $+,-,-,-$ in the same basis. The first is a Euclidean structure on the sector; the second is a Minkowski structure. The plain form and the K norm add nothing new here, and the sector is one of the subspaces where the four forms collapse pairwise.

| form | value on $\tilde H_\Psi=h_te_t+i\vec h_\Psi$ | Inertia | what it defines on the sector |
| --- | --- | --- | --- |
| Hermitian $\langle\cdot,\cdot\rangle_{*}$ | $h_{1t}h_{2t}+\vec h_{\Psi,1}\cdot\vec h_{\Psi,2}$ | $(4,0)$ | the probabilities |
| plain $\langle\cdot,\cdot\rangle$ | the same | $(4,0)$ | the same, without the star |
| quaternionic $\langle\cdot,\cdot\rangle_{\natural}$ | $h_{1t}h_{2t}-\vec h_{\Psi,1}\cdot\vec h_{\Psi,2}$ | $(1,3)$ | the interval and the mixedness |
| K $\mathrm{Kr}$ | the same as the quaternionic | $(1,3)$ | the same, coefficientwise |

The sector carries no area pairing. Multiplication by $i$ sends the sector to the material sector, $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$, so no element of the sector has an imaginary part that stays in the sector, and the imaginary parts of the four forms vanish identically on it. The sector is therefore a *real* four-space with no complex structure of its own: it is not a complex subspace, and its dimension over $\mathbb{C}$ is not defined. The complex structure that the algebra does carry, the left multiplication by the central $i$, is exactly the map that leaves the sector.

The scalar part reads the weight and forgets the direction. On the sector it is the coefficient $h_t$, because the vector part is a sum of three imaginary coefficients whose real parts vanish:

$$
\mathrm{Sc}(\tilde H_\Psi)=h_t .
$$

The scalar part is a positive functional on the positive cone of the sector, and it is the functional against which a state is normalised. It carries the first block and only the first block, which is the algebraic statement that normalisation is a condition on the weight and says nothing about the direction.

The sector's position in the split is one of the two signs. Nothing in the sector's definition refers to the material sector, and nothing in the material sector's definition refers to it. The two are the two eigenspaces of one involution, so the split is a decomposition and not a choice, and the names are labels on the two signs and not two constructions. The next two sections take each of the sector's two objects, the observable and the state, from this one space.

## The Observable

An observable is an element of the sector, and its spectrum is two real numbers. Write the element with a real weight and a real direction, and factor the direction into its length and its unit:

$$
\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi
=\bigl(h_t+\lvert\vec h_\Psi\rvert\bigr)\tilde\Pi_{\mathrm{id},1}(\vec u_\Psi)
+\bigl(h_t-\lvert\vec h_\Psi\rvert\bigr)\tilde\Pi_{\mathrm{id},2}(\vec u_\Psi),
\qquad
\vec u_\Psi=\frac{\vec h_\Psi}{\lvert\vec h_\Psi\rvert},
$$

with the two idempotents of the axis

$$
\tilde\Pi_{\mathrm{id},1,2}(\vec u)=\tfrac12\bigl(e_t\pm i\vec u\bigr),
\qquad
\tilde\Pi_{\mathrm{id},1+}\tilde\Pi_{\mathrm{id},2}=e_t,
\qquad
\tilde\Pi_{\mathrm{id},1}\tilde\Pi_{\mathrm{id},2}=0,
\qquad
\tilde\Pi_{\mathrm{id},1,2}^{2}=\tilde\Pi_{\mathrm{id},1,2}.
$$

The two eigenvalues are $\eta_{\pm}=h_t\pm\lvert\vec h_\Psi\rvert$. The display is not a construction: it is an identity, and it is the spectral theorem for this sector. The proof is one multiplication, and it uses the one algebraic accident of the sector,

$$
(i\vec u)^{2}=i^{2}\vec u^{2}=(-e_t)\bigl(-\lvert\vec u\rvert^{2}e_t\bigr)=+\lvert\vec u\rvert^{2}e_t=e_t ,
$$

so that $i\vec u$ is a root of $+e_t$ and the two halves of the axis are idempotents.

The idempotents are the measurement axes, and they are one family. The family $\{\tilde\Pi_{\mathrm{id},1}(\vec u)\}$ is a two-sphere: one idempotent for each unit direction, with $\tilde\Pi_{\mathrm{id},1}(-\vec u)=\tilde\Pi_{\mathrm{id},2}(\vec u)$. The axis is a parameter and not a datum of the algebra, so an observable is an axis together with two numbers, and the algebra supplies no axis of its own. A physical statement that names a direction is using the direction as a parameter; a physical statement that names no direction cannot be about a measurement.

The identity is the degenerate observable. At $\vec h_\Psi=0$ the element is $h_te_t$, central, and the two eigenvalues coincide at $h_t$. The spectral decomposition then fails to determine an axis: every idempotent family gives the same element. The degenerate case is not a defect of the formula but the statement that an observable proportional to the unit carries no direction, and a measurement of it produces the same number in every state. The vector part is what a measurement discriminates, and the scalar part is what it adds to every outcome.

The spectrum is real for every element of the sector. Both eigenvalues are real combinations of real coordinates, so the sector is the *self-adjoint* part of the algebra in the strong sense: every element of it has a real spectrum, and the spectral projectors lie in the sector itself. The property is not shared by the general element, whose eigenvalues can be complex, and it is the reason the sector and not the algebra is the home of the observables.

**Positivity is a condition on the two numbers, and it has four equivalent forms.** For $\tilde H_\Psi\in\mathbb{B}_{\Psi}$ the following are the same statement:

$$
\tilde H_\Psi\ge0
\iff
\eta_{+}\ge0\ \text{and}\ \eta_{-}\ge0
\iff
h_t\ge\lvert\vec h_\Psi\rvert
\iff
N(\tilde H_\Psi)\ge0\ \text{with}\ h_t\ge0 .
$$

The second form is the definition of the cone by its spectrum, the third is the same cone in the coordinates, and the fourth is the cone read through the quaternionic norm and the weight. The equivalence of the third and the fourth is the algebraic fact that makes the norm useful: the cone of the sector is a *half* of the cone of the norm, the half selected by the sign of the weight.

The order is the order of the cone. For two observables, $\tilde A\le\tilde B$ means $\tilde B-\tilde A\ge0$. The order is not total: two elements are incomparable exactly when their difference has $h_t<\lvert\vec h_\Psi\rvert$, which is the spacelike condition. The partial order on the sector is therefore the order of the cone read in the same coordinates as the interval, and the effect interval of a later section is the interval $[0,e_t]$ of this order.

The pair of idempotents is the resolution of the identity that the observable carries. Every observable determines one axis and two numbers, and the axis determines the two idempotents. So an observable carries a partition of the unit into two orthogonal parts, and the partition is unique unless the two eigenvalues coincide. The eigenvalue formula is the statement that the algebra's own multiplication supplies that partition.

Observables and states live in one cone, and the states are a slice of it. The positive cone is a single convex cone of the sector, and the observables are its elements without a normalisation. The states are the elements of the same cone at unit weight. The fact that the two objects are two parts of one cone is the reason the pairing between them is symmetric, and the next section takes the slice.

## The State and the Slice

A state is a positive element at unit weight. The state of the sector is

$$
\tilde{Ϛ}_\Psi=\tfrac12\bigl(e_t+i\vec s_{\Psi}\bigr),
\qquad
\langle\tilde{Ϛ}_\Psi,e_t\rangle_{*}=\tfrac12\langle e_t,e_t\rangle_{*}=\tfrac12,
\qquad
\mathrm{Sc}(\tilde{Ϛ}_\Psi)=\tfrac12,
\qquad
\lvert\vec s_{\Psi}\rvert\le1 .
$$

The normalisation is one real condition, the positivity is one inequality, and the parametrisation by $\vec s_{\Psi}$ is the solution of both. The four real numbers of a general sector element are reduced to three by the normalisation, and the inequality confines those three to a ball. The ball is the Bloch ball, and the state space of the sector is it.

The eigenvalues are the radius and the sign of the radius. The eigenvalue formula of the previous section, applied at $h_t=\tfrac12$ and $\lvert\vec h_\Psi\rvert=\tfrac12\lvert\vec s_{\Psi}\rvert$, gives

$$
\tilde{Ϛ}_\Psi=\frac{1+r}{2}\,\tilde\Pi_{\mathrm{id},1}(\vec u_s)+\frac{1-r}{2}\,\tilde\Pi_{\mathrm{id},2}(\vec u_s),
\qquad
r=\lvert\vec s_{\Psi}\rvert,
\qquad
\vec u_s=\frac{\vec s_{\Psi}}{r},
$$

so the spectrum of a state is $\tfrac12(1\pm r)$. Both eigenvalues are non-negative exactly when $r\le1$, and their sum is one. The state's two eigenvalues therefore carry one number between them, and that number is the radius.

The boundary is the pure states and it is a sphere. At $r=1$ one eigenvalue is one and the other is zero, the state is an idempotent, and the idempotents of the sector are exactly the elements $\tilde\Pi_{\mathrm{id},1}(\vec u)$ of the two-sphere. At $r=0$ the state is $\tfrac12 e_t$, both eigenvalues are $\tfrac12$, and no measurement prefers either outcome. Between them the state is mixed, and the direction $\vec u_s$ is the axis along which the state is most definite: the outcome along that axis has probability $\tfrac12(1+r)$, which decreases with the mixedness.

Purity is twice the Hermitian norm. The scalar part of the square of the state is the standard measure, and in the sector it is the Hermitian form twice,

$$
P(\tilde{Ϛ}_\Psi)=2\langle\tilde{Ϛ}_\Psi,\tilde{Ϛ}_\Psi\rangle_{*}=2\,\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi^{2}\bigr)=\tfrac12\bigl(1+r^{2}\bigr),
\qquad
r=\sqrt{2P-1},
$$

which runs from $\tfrac12$ at the centre to $1$ on the boundary. The radius is a monotone function of the purity, so the Euclidean geometry of the ball and the statistical notion of mixedness are one structure read twice.

The mixedness has a second expression, and it is the quaternionic norm. On the slice,

$$
N(\tilde{Ϛ}_\Psi)=\tilde{Ϛ}_\Psi\tilde{Ϛ}_\Psi^{\natural}
=\tfrac14\bigl(1-r^{2}\bigr)e_t ,
\qquad
S_{\mathrm{lin}}(\tilde{Ϛ}_\Psi)=2\,\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi-\tilde{Ϛ}_\Psi^{2}\bigr)=\tfrac12\bigl(1-r^{2}\bigr)=2N(\tilde{Ϛ}_\Psi).
$$

The identity is worth separating from its consequences. The form that defines the cone of the sector is the same form that measures how mixed a state is, up to the factor two. A pure state has $N=0$ and the maximally mixed state has $N=\tfrac14$, its largest value on the slice. **The two facts — that the cone cuts out the state space and that the form measures mixedness — are one fact**, because both are governed by the product of the two eigenvalues, $\eta_{+}\eta_{-}=\tfrac14(1-r^{2})$.

**The state is a zero divisor exactly when it is pure.** An element of the algebra has an inverse exactly when its norm is not zero, so the states with $N\ne0$ are invertible and the states with $N=0$ are the zero divisors. The pure states are therefore the null elements of the sector, and the boundary of the ball is the intersection of the sector with the zero-divisor cone of the algebra. A mixed state has an inverse in the algebra; a pure state does not.

The centre of the ball is the state with no direction. At $\vec s_{\Psi}=0$ the state is $\tfrac12e_t$, a central element, and its spectrum is degenerate. It is fixed by every rotor, no measurement distinguishes it, and it carries the maximal entropy $\log2$ of the ball. It is also the state of maximal $N$ on the slice, so the directionless state is the one furthest from the cone's boundary as the sector's own form measures distance.

The unit-scalar condition is a slice, and the slice is affine. The positive cone is a cone; the set $\{\mathrm{Sc}=\tfrac12\}$ is a hyperplane that does not pass through the apex; their intersection is a convex body, and for this sector the body is a ball. Nothing in the algebra selects the value $\tfrac12$: the condition could be $\mathrm{Sc}=\tau$ for any $\tau>0$, and the rescaled element $\tilde{Ϛ}_\Psi/(2\tau)$ is the same state. The value fixes the scale and is a convention, and the next section shows that the convention cancels from every probability.

The ball is the convex hull of its boundary. Every state is a convex combination of two orthogonal pure states, by the spectral decomposition, with weights $\tfrac12(1\pm r)$. The pure states are the extreme points of the convex set, and the decomposition of a given mixed state is unique up to the exchange of the two. The convex structure of the state space is therefore read from the algebra: the extreme points are the idempotents, and convexity is the assertion that a mixture of two preparations is again a preparation.

A state is a positive functional, and the element is its representative. The element defines the functional

$$
\omega_{\tilde{Ϛ}_\Psi}(\tilde A)=2\,\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\tilde A\bigr),
\qquad
\omega_{\tilde{Ϛ}_\Psi}(e_t)=1,
\qquad
\omega_{\tilde{Ϛ}_\Psi}(\tilde A^{2})\ge0
$$

on the sector. Every normalised positive functional on the sector arises this way, because the Hermitian form is an inner product and the algebra is finite-dimensional, so the element and the functional are the same information. The article writes the element, because the element has a spectrum, a radius and a direction, while the functional has only values.

The mixedness has a distance expression. The distance from a state to the centre of the ball, read in the scalar part of the absolute value, is half the radius,

$$
D\bigl(\tilde{Ϛ}_\Psi,\tfrac12e_t\bigr)=\mathrm{Sc}\bigl\lvert\tilde{Ϛ}_\Psi-\tfrac12e_t\bigr\rvert=\tfrac12 r,
$$

and the Hilbert–Schmidt distance between two states is half the Euclidean distance between their radius vectors,

$$
2\,\mathrm{Sc}\bigl((\tilde{Ϛ}_{\Psi,1}-\tilde{Ϛ}_{\Psi,2})^{2}\bigr)=\tfrac12\lvert\vec s_{\Psi,1}-\vec s_{\Psi,2}\rvert^{2}.
$$

The two distances are the two natural metrics of the ball, and both are functions of the radius vectors alone. The geometry is Euclidean in the coordinates and statistical in the radius, and the two readings agree on what the centre is.

The entropy is a function of the radius and of nothing else. The spectral logarithm of a state is the combination of the two idempotents weighted by the logarithms of the two eigenvalues, and the von Neumann entropy is

$$
S(\tilde{Ϛ}_\Psi)=-2\,\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\log\tilde{Ϛ}_\Psi\bigr)
=-\frac{1+r}{2}\log\frac{1+r}{2}-\frac{1-r}{2}\log\frac{1-r}{2}.
$$

The direction does not appear. Two states of equal radius have equal entropy, whatever their axes, so the entropy is a function on the radius and its level sets are the concentric spheres of the ball. This is the sector's statement that entropy counts mixedness and not orientation, and it is derived here rather than assumed.

## The Born Weight

The weight is the Hermitian pairing divided by the scalar part of the state. For a state $\tilde{Ϛ}_\Psi$ and an observable $\tilde H_\Psi$ the Born weight is

$$
\langle\tilde H_\Psi\rangle_{\tilde{Ϛ}_\Psi}
=\frac{\langle\tilde{Ϛ}_\Psi,\tilde H_\Psi\rangle_{*}}{\langle\tilde{Ϛ}_\Psi,e_t\rangle_{*}}
=\frac{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\tilde H_\Psi^{*}\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\bigr)}
=h_t+\vec s_{\Psi}\cdot\vec h_\Psi .
$$

The last equality is the whole content of the formula in the sector's coordinates: the weight is the scalar part of the observable plus the projection of its direction on the state's radius vector. The normalisation appears as a ratio, so the value of $\tau$ cancels, and the weight depends on the state only through $\vec s_{\Psi}$.

The derivation is three lines. With $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_{\Psi})$ and $\tilde H_\Psi=h_te_t+i\vec h_\Psi$,

$$
\tilde{Ϛ}_\Psi\tilde H_\Psi=\tfrac12\Bigl[\bigl(h_t-\vec s_{\Psi}\cdot\vec h_\Psi\bigr)e_t+i\bigl(h_t\vec s_{\Psi}+\vec h_\Psi\bigr)-\vec s_{\Psi}\times\vec h_\Psi\Bigr],
$$

whose scalar part is $\tfrac12(h_t-\vec s_{\Psi}\cdot\vec h_\Psi)$; and the star in the numerator is the identity on the sector, so the numerator is $\mathrm{Sc}(\tilde{Ϛ}_\Psi\tilde H_\Psi)$ and the denominator is $\mathrm{Sc}(\tilde{Ϛ}_\Psi)=\tfrac12$. The quotient is $h_t+\vec s_{\Psi}\cdot\vec h_\Psi$. The sign that appears in the product and disappears in the quotient is the sign of the cross-product term, and it cancels because the term is a real pure quaternion with no scalar part.

A measurement along an axis is the case of two idempotents. For the observable $\tilde\Pi_{\mathrm{id},1}(\vec u)=\tfrac12(e_t+i\vec u)$, whose eigenvalues are one and zero and whose axis is $\vec u$, the weight is

$$
p_+=\frac{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\tilde\Pi_{\mathrm{id},1}(\vec u)\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\bigr)}
=\tfrac12\bigl(1+\vec u\cdot\vec s_{\Psi}\bigr),
\qquad
p_-=\tfrac12\bigl(1-\vec u\cdot\vec s_{\Psi}\bigr),
\qquad
p_++p_-=1 .
$$

The two weights add to one because the two idempotents add to the unit, $\tilde\Pi_{\mathrm{id},1+}\tilde\Pi_{\mathrm{id},2}=e_t$, and the pairing is linear in its first slot. This is the analyser transmission law: the fraction of a beam transmitted by an analyser along $\vec u$ when the preparation is along $\vec s_{\Psi}$.

Written in the angle between the two axes it is the half-angle law. With $\vec u\cdot\vec s_{\Psi}=r\cos\theta$, where $\theta$ is the angle between the measurement axis and the state's axis,

$$
p_+=\tfrac12\bigl(1+r\cos\theta\bigr),
\qquad
p_+\big|_{\text{pure}}=\cos^{2}\frac{\theta}{2},
\qquad
p_+\big|_{r=0}=\tfrac12 .
$$

The pure case is the standard squared overlap of two rays, and the factor of a half in the angle is the double cover. The mixed case is the same expression weighted by the radius, and the maximally mixed case is the constant $\tfrac12$: a state with no direction gives no preference to any axis.

The three properties that make the pairing a probability are algebraic. Reality, positivity and normalisation are not assumptions of the Born rule; they are properties of the pairing on the positive cone.

- Reality. For two Hermitian elements the star is the identity twice, so the pairing is the symmetric bilinear form $h_{1t}h_{2t}+\vec h_{\Psi,1}\cdot\vec h_{\Psi,2}\,$, which is real. **The star is retained in the formula because it names the pairing that is positive definite on the whole algebra**, and because it cannot be dropped when one factor is not Hermitian.
- Positivity. If $\tilde{\mathcal E}\ge0$ and $\tilde{Ϛ}_\Psi\ge0$ then $2\,\mathrm{Sc}(\tilde{\mathcal E}\tilde{Ϛ}_\Psi)\ge0$. The product of two positive elements need not be Hermitian, but its scalar part is real and non-negative, and the reason is the spectral decomposition: writing both in the same idempotent family reduces the scalar part to a sum of products of non-negative numbers.
- Normalisation. The unit is the sum of the two idempotents of any axis, so a two-outcome measurement sums to one, and the general case sums to one because a resolution of the unit sums to $e_t$ and the pairing is linear.

The observable has two readings, and the algebra names both. Every Hermitian element is $\tilde H_\Psi=iA$ for a unique anti-Hermitian $A\in\mathbb{B}_{\Phi}$, because multiplication by the central $i$ exchanges the sectors. The weight can therefore be written against a material element,

$$
\langle iA\rangle_{\tilde{Ϛ}_\Psi}
=\frac{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi(iA)^{*}\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\bigr)}
=\frac{i\,\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi A\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\bigr)},
$$

and the numerator is purely imaginary, so the factor $i$ makes the weight real. The pairing of a state with an observable is thus the pairing of an informational element with a material one, and the factor $i$ is what converts the second into a reading. The two senses of the word *observable* — the element of the sector and the material element it mirrors — are separated by one multiplication.

The weight of the square gives the variance. For the square $\tilde H_\Psi^{2}=(h_t^{2}+\lvert\vec h_\Psi\rvert^{2})e_t+2h_t i\vec h_\Psi$, whose weight is $h_t^{2}+\lvert\vec h_\Psi\rvert^{2}+2h_t\vec s_{\Psi}\cdot\vec h_\Psi$,

$$
\bigl\langle\tilde H_\Psi^{2}\bigr\rangle_{\tilde{Ϛ}_\Psi}-\bigl\langle\tilde H_\Psi\bigr\rangle_{\tilde{Ϛ}_\Psi}^{2}
=\bigl(1-r^{2}\cos^{2}\theta\bigr)\lvert\vec h_\Psi\rvert^{2},
$$

which is non-negative and which vanishes exactly when $r=1$ and $\cos^{2}\theta=1$, that is, when the state is the pure state on the observable's own axis. The variance is the part of the observable that the state cannot predict, and the two factors in it are the two reasons for failing to predict: a direction that is not the observable's, and a radius below one. A mixed state therefore has a variance on every axis, including its own, where the residue is $(1-r^{2})\lvert\vec h_\Psi\rvert^{2}$. **Only a pure state can be an eigenstate of anything.**

Two checks on the arithmetic. The first is the pure case at $\vec s_{\Psi}=\vec u_\Psi$, where $p_+=1$ and the variance is zero. The second is the mixed case at $\vec s_{\Psi}=0$, where $p_+=\tfrac12$ and the variance is $\lvert\vec h_\Psi\rvert^{2}$, its largest value. A computation in the algebra confirms both formulas on random states and observables to machine precision, and the identity $\eta_{+}\eta_{-}=h_t^{2}-\lvert\vec h_\Psi\rvert^{2}$ ties the variance to the two eigenvalues.

The matrix trace is a reading, and it adds nothing. In the two-by-two image the matrix trace of the product is the pairing twice, and the normalised state has matrix trace one, so the weight becomes the familiar ratio of matrix traces. The factor two is the dimension of the image and cancels in the ratio; it is not a normalisation constant of the form. The symmetry of that trace, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ on the image, is the symmetry of the pairing on Hermitian arguments, and it is what allows the state to be written on either side.

What is derived and what is not is worth stating in one place. The algebra fixes the pairing, the idempotents and the cone. From these, the weight is real, non-negative and normalised, the two outcomes of a projective measurement add to one, and the variance is non-negative. Nothing else entered: no inner product was chosen, no Hilbert space was assumed, no frequency argument was used. What is not derived is that the weights are observed frequencies. That identification is the Born rule, and it is a postulate here as it is in the standard formalism. The framework's claim is narrower and it is exact: the *structure* of the assignment is forced by the algebra, and the empirical link is not.

The non-uniqueness is real and it is stated. A reading through the matrix trace could equally be written with the plain form, because the two coincide on the sector; the star is kept because it names the pairing that is positive definite on the whole algebra and because it survives the extension to maps. A reading could also be normalised by any positive functional, but only the scalar part is invariant under the unitary action, and that invariance is what makes the weight frame-independent within the compact group. The alternatives are therefore not equivalent: they differ in what they preserve.

## The Effects

An effect is an element between zero and the unit. The interval $[0,e_t]$ of the sector's order is the set of effects, and its elements are exactly the elements whose two eigenvalues lie in $[0,1]$. Writing an effect with its two numbers,

$$
\tilde{\mathcal E}_{\Psi}=a\,e_t+i\vec w,
\qquad
\tilde{\mathcal E}_{\Psi}\in[0,e_t]
\iff
a\ge\lvert\vec w\rvert\ \ \text{and}\ \ 1-a\ge\lvert\vec w\rvert
\iff
0\le a\le1\ \ \text{and}\ \ \lvert\vec w\rvert\le\min\bigl(a,1-a\bigr).
$$

The two inequalities are the two conditions $\tilde{\mathcal E}_{\Psi}\ge0$ and $e_t-\tilde{\mathcal E}_{\Psi}\ge0$, each of them the cone condition of the observable section applied to one of the two elements. The interval is a double cone with apexes at zero and at the unit, and its widest cross-section is at $a=\tfrac12$.

The projections are the extreme points. At $a=\tfrac12$ and $\lvert\vec w\rvert=\tfrac12$ the effect is $\tilde\Pi_{\mathrm{id},1}(\vec u)=\tfrac12(e_t+i\vec u)$, an idempotent, and no idempotent lies in the interior of the interval. The interval is therefore the convex hull of the projections plus the two endpoints, and the projections are the measurements with a definite outcome. The effect algebra of the sector is the interval of its own order, and the projection lattice is the two-sphere of axes together with zero and the unit.

A general resolution of the unit is a measurement. A finite family $\{\tilde{\mathcal E}_{\Psi,k}\}$ with $\tilde{\mathcal E}_{\Psi,k}\ge0$ and $\sum_{\imath}\tilde{\mathcal E}_{\Psi,k}=e_t$ is a POVM, and the weight of the $k$-th outcome is

$$
p_{\imath}=\frac{\mathrm{Sc}\bigl(\tilde{\mathcal E}_{\Psi,k}\tilde{Ϛ}_\Psi\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}_\Psi\bigr)}=a_{\imath}+\vec w_{\imath}\cdot\vec s_{\Psi},
\qquad
\sum_{\imath} a_{\imath}=1,
\qquad
\sum_{\imath}\vec w_{\imath}=0 .
$$

The two sums are the single condition $\sum_{\imath}\tilde{\mathcal E}_{\Psi,k}=e_t$ split into its two blocks. Normalisation of the weights follows, positivity follows from the interval, and the projective case is the one in which the effects are idempotents and pairwise orthogonal.

An effect is a measurement with a finite resolution, and the resolution is a number. The one-parameter family

$$
\tilde{\mathcal E}_{\Psi,\pm}=\tfrac12\bigl(e_t\pm\digamma_{\mathrm{blc}}\,i\vec u\bigr),
\qquad
0\le\digamma_{\mathrm{blc}}\le1,
\qquad
p_\pm=\tfrac12\bigl(1\pm\digamma_{\mathrm{blc}}\,\vec u\cdot\vec s_{\Psi}\bigr),
$$

is a POVM for every $\digamma_{\mathrm{blc}}$ in the range, because $a=\tfrac12$ and $\lvert\vec w\rvert=\digamma_{\mathrm{blc}}/2\le\tfrac12$. It is projective only at $\digamma_{\mathrm{blc}}=1$, since

$$
\tilde{\mathcal E}_{\Psi,+}^{2}-\tilde{\mathcal E}_{\Psi,+}=\tfrac14\bigl(\digamma_{\mathrm{blc}}^{2}-1\bigr)e_t ,
$$

which vanishes exactly at the endpoint. The number $\digamma_{\mathrm{blc}}$ is the sharpness of the measurement: at $\digamma_{\mathrm{blc}}=1$ the analyser passes one axis and blocks the other, and at $\digamma_{\mathrm{blc}}=0$ the two effects are both $\tfrac12e_t$ and the outcome carries no information about the state at all. **Every intermediate value is a measurement whose two outcomes overlap, and the overlap is what the interval's interior contains.**

Three outcomes show that the projection lattice is not the whole story. With three unit vectors $\vec u_0,\vec u_1,\vec u_2$ at $120^\circ$ apart, so that $\vec u_0+\vec u_1+\vec u_2=0$, the three effects

$$
\tilde{\mathcal E}_{\Psi,k}=\tfrac13\bigl(e_t+i\vec u_{\imath}\bigr)=\tfrac23\,\tilde\Pi_{\mathrm{id},1}(\vec u_{\imath}),
\qquad
k=0,1,2,
$$

are a POVM with weights $p_{\imath}=\tfrac13(1+\vec u_{\imath}\cdot\vec s_{\Psi})$. No two of them are orthogonal and none of them is a projection, so the measurement has three outcomes and no orthonormal basis. The projection lattice of a two-dimensional carrier cannot supply three orthogonal alternatives, and the interval supplies them without an enlargement.

**What the interval does not supply is the state after the measurement.** The weight is a statistic of the preparation and the effect alone. The update of the state requires a family of maps, $\tilde{Ϛ}_\Psi\mapsto\sum_{\imath}\tilde M_{\mathrm{kraus},k}\tilde{Ϛ}_\Psi\tilde M_{\mathrm{kraus},k}^{*}$ with $\sum_{\imath}\tilde M_{\mathrm{kraus},k}^{*}\tilde M_{\mathrm{kraus},k}=e_t$, and the Kraus operators are not determined by the effect they implement. Two instruments with the same POVM can update the state differently, so the interval answers "how often" and not "what then".

The dilation is the algebraic reason the interval is enough. Every POVM on this carrier has a projective realisation on a larger algebra, $\mathbb{B}\otimes_{\mathbb{C}}M_{\imath}(\mathbb{C})\cong M_{2k}(\mathbb{C})$, and the enlargement is by a factor that the tensor product supplies. The interval of the small algebra is therefore not an approximation to a projective measurement on the same algebra; it is the shadow of a projective measurement on a larger one, and the shadow is exact.

## The Geometry of the Slice

The boundary carries two metric structures, and both come from the algebra. The pure states are a two-sphere, and the two forms of the sector restrict to it as a metric and as a two-form. The Hermitian form gives the transition probability between two pure states, and the quaternionic norm gives the line element. The two are different functions of the same pair of axes, and the entry states both.

The transition probability is the Hermitian pairing of two idempotents. For two pure states on the axes $\vec u_1$ and $\vec u_2$,

$$
2\,\mathrm{Sc}\bigl(\tilde\Pi_{\mathrm{id},1}(\vec u_1)\tilde\Pi_{\mathrm{id},1}(\vec u_2)\bigr)=\tfrac12\bigl(1+\vec u_1\cdot\vec u_2\bigr)=\cos^{2}\frac{\theta}{2},
$$

with $\theta$ the angle between the axes. The pairing is symmetric in the two states and it is bounded between zero and one, so it is the squared overlap of the two rays, and the half-angle is the double cover again.

The line element is the quaternionic norm of a displacement, and that is why the factor is a quarter. The norm vanishes on a pure state, so it cannot be a metric there; what it measures is the second-order displacement of the state along the sphere. For a tangential displacement $\delta\tilde\Pi_{\mathrm{id}}=\tfrac12 i\,\delta\vec u$, orthogonal displacements adding in quadrature,

$$
ds^{2}=-\langle\delta\tilde\Pi_{\mathrm{id}}\rangle_{\natural}\Big|_{\text{tangential}}
=\tfrac14\lvert d\vec u\rvert^{2}
=\tfrac14\bigl(d\theta^{2}+\sin^{2}\theta\,d\theta_{\mathrm{azm}}^{2}\bigr),
$$

which is the Fubini–Study line element of the projective line, equal to a quarter of the round metric of the sphere. The quarter is the square of the half-angle: the sphere of axes is a double cover of the ray space, and a metric on the ray space pulls back with the square of the covering map's derivative.

The state space is Kähler, and the complex structure is the commutator. At an axis $\vec u$ the map on the tangent space

$$
J_{\vec u}(v)=\vec u\times v=\tfrac12\,[\vec u,v]
$$

satisfies $J^{2}=-1$ on the tangent plane, so it is an almost-complex structure, and it is integrable because the sphere is a projective line. It is the algebra's own antisymmetric product, restricted to the boundary. The metric is invariant under it and the associated two-form is

$$
\omega(\delta_1,\delta_2)=-\,i\,\mathrm{Sc}\bigl(\tilde\Pi_{\mathrm{id}}\,[\delta_1\tilde\Pi_{\mathrm{id}},\delta_2\tilde\Pi_{\mathrm{id}}]\bigr)
=\tfrac14\,\vec u\cdot(\delta_1\vec u\times\delta_2\vec u)
=\tfrac14\sin\theta\,d\theta\wedge d\theta_{\mathrm{azm}} .
$$

The area is finite, and the finiteness is the statement that the spin is bounded. The total symplectic area of the boundary is

$$
\int_{S^{2}}\omega=\tfrac14\int_0^{2\pi}\!\!\int_0^{\pi}\sin\theta\,d\theta\,d\theta_{\mathrm{azm}}=\pi ,
$$

the area of the sphere of radius $\tfrac12$. In units of $2\pi$ that is $\tfrac12$, which is the spin of the carrier: a spin-$s$ carrier would give $2\pi s$. The state space is compact, its symplectic volume is finite and fixed, and the number that fixes it is the one the algebra's normalisation has already set.

The distances are the same information as the probabilities. The geodesic distance of the metric is half the angle between the axes, and the trace distance of the two images is its sine,

$$
d_{\mathrm{FS}}=\arccos\bigl\lvert\cos\tfrac{\theta}{2}\bigr\rvert=\frac{\theta}{2},
\qquad
D\bigl(\tilde\Pi_{\mathrm{id},1}(\vec u_1),\tilde\Pi_{\mathrm{id},1}(\vec u_2)\bigr)=\sin d_{\mathrm{FS}} .
$$

Two pure states at a right angle on the sphere are therefore at a Fubini–Study distance of $\pi/4$ and at a trace distance of $1/\sqrt{2}$, and orthogonal states are at a distance of $\pi/2$ and trace distance one. **The geometry and the statistics are the same numbers in two parametrisations.**

**The interior metric is not the one the norm gives.** The flat form $-\tfrac14\lvert d\vec s_{\Psi}\rvert^{2}$ that the quaternionic norm supplies on the interior is not the Bures metric, whose boundary restriction is the Fubini–Study metric. The algebra's own form therefore gives the boundary exactly and the flat geometry everywhere, and it does not single out the metrically distinguished interior. That is a limit of what the norm does, and it is stated in the article on the Fubini–Study geometry rather than glossed here. The Bures metric is nevertheless a closed geometric object once it is granted: it is the round metric of a hemisphere of radius $\tfrac12$ whose pole is the maximally mixed state and whose equator is the pure-state sphere, so latitude is purity and the interior is not a flat ball. The flat form and that hemisphere agree on the angular part at every radius and differ in the radial coefficient alone.

The slice is the base of a cone, and the cone is defined by the product. The state set of this article is fixed by two conditions, the positivity of the matrix $\tilde\rho$ and the normalisation to unit weight. Read in the Hermitian sector they are one object. The positivity is membership in the cone of squares $C$ of the symmetrised plain product, which is $t\geq\lvert\vec s\rvert$ on $\tilde\rho=te_t+i\vec s$, and the normalisation cuts that cone with the affine hyperplane $2\,\mathrm{Sc}\tilde\rho=2t=1$. The state set is therefore the base of a symmetric cone. Its extreme points are its rank-one idempotents $\tfrac12(e_t+i\vec u)$ with $\lvert\vec u\rvert=1$, which is why the pure states fill the sphere and not the ball, and the Born weight is a positive functional normalised at the order unit $e_t$. The reading is *The Biquaternion Algebra as a JB-Algebra*, and what it supplies here is the reason why the three facts of this section — the slice, the sphere of pure states and the positivity of the weight — are one fact and not three.

## The Flow and the Centre

The state changes by conjugation, and the conjugation is by an invertible element of the algebra. The action of the algebra on its own sector is

$$
\Gamma_{\tilde U}\bigl(\tilde X\bigr)=\tilde U\tilde X\tilde U^{*},
\qquad
\tilde U\in\mathbb{B}^{\times},
$$

and it maps the sector to itself because the star is an anti-automorphism and the two signs cancel. On a state it is the transformation of a preparation, and the question of the section is which $\tilde U$ leave the state space intact.

Two different conditions preserve two different forms, and the difference is the whole content. The first theorem is about the Hermitian norm, which is the scalar part of the product on the sector.

- The scalar part is preserved exactly by the star-unitary elements. For all $\tilde X$,
$$
\mathrm{Sc}\bigl(\Gamma_{\tilde U}(\tilde X)^{*}\Gamma_{\tilde U}(\tilde X)\bigr)=\mathrm{Sc}\bigl(\tilde X^{*}\tilde X\bigr)
\iff
\tilde U^{*}\tilde U=e_t .
$$
The proof writes $\tilde Q_4=\tilde U^{*}\tilde U$, uses the cyclicity of the scalar part twice, and tests the identity on rank-one elements; positivity then forces $\tilde Q_4=e_t$. The group is $U(2)$.
- The quaternionic norm is preserved exactly by the unit-norm elements. For all $\tilde X$,
$$
\langle\Gamma_{\tilde U}(\tilde X)\rangle_{\natural}=\bigl\lvert\langle\tilde U\rangle_{\natural}\bigr\rvert^{2}\langle\tilde X\rangle_{\natural},
$$
so the norm is preserved exactly when $\lvert N(\tilde U)\rvert=1$. The group is $U(1)\cdot SL(2,\mathbb{C})$, which contains $U(2)$.

**The state space is preserved by $U(2)$ and by nothing else.** Positivity alone is preserved by every invertible congruence: if $\tilde X\ge0$ and $\tilde U$ is invertible then $\tilde U\tilde X\tilde U^{*}\ge0$, because the eigenvalues of a congruence by an invertible element keep their signs. The slice is the stronger condition. If $\Gamma_{\tilde U}$ maps the unit-scalar slice to itself, then $\mathrm{Sc}(\Gamma_{\tilde U}(\tilde{Ϛ}_\Psi))$ is constant over the slice, and a linear function constant on a hyperplane is a multiple of the functional that defines it, so $\tilde U^{*}\tilde U$ is a positive multiple of $e_t$. The multiple is a scale, and up to scale the condition is $\tilde U^{*}\tilde U=e_t$. The state space is the intersection of the cone with the slice, and it is preserved by the intersection of the two groups, which is $U(2)$.

A boost therefore moves a mixed state off the slice, and the change is not a normalisation. For a boost of rapidity $\theta$ along $\vec e_x$ and a state with radius $r$ on the same axis, the conjugated element is

$$
\Gamma_{\tilde U_{\mathrm b}}\bigl(\tilde{Ϛ}_\Psi\bigr)
=\tfrac12\Bigl[\bigl(\cosh\theta+r\sinh\theta\bigr)e_t+i\bigl(\sinh\theta+r\cosh\theta\bigr)\vec e_x\Bigr],
$$

whose scalar part is $\tfrac12(\cosh\theta+r\sinh\theta)$ and whose normalised radius is

$$
r'=\frac{r+\tanh\theta}{1+r\tanh\theta}.
$$

The scalar part is not $\tfrac12$, so the image is not a state; after renormalisation the radius has changed, and for a mixed state it has increased. The formula is the addition law of velocities, and the next section reads it as one. The unit-scalar slice is not invariant under the Lorentz group, and the statement that it is invariant is the statement that the boost is a rotation, which it is not.

The flow generated by a Hermitian element preserves the norm only for a central unit. In the state module the equation is

$$
i \frac{h}{2\pi} c\,\frac{\partial}{\partial r'_t}\tilde{Ξ}=\tilde Z\,\tilde H_\Psi\tilde{Ξ},
\qquad
\tilde Z^{2}=-e_t,
\qquad
\tilde H_\Psi\in\mathbb{B}_{\Psi},
$$

with the solution $\tilde{Ξ}(r'_t)=\exp(Gr'_t)\tilde{Ξ}(0)$ and $G=-\frac{2\pi \tilde Z\tilde H_\Psi}{h\,c}$. The norm $2\,\mathrm{Sc}(\tilde{Ξ}^{*}\tilde{Ξ})$ is preserved for every $\tilde H_\Psi$ exactly when $G$ is anti-Hermitian, and the condition becomes

$$
\tilde H_\Psi\tilde Z=\tilde Z\tilde H_\Psi
\qquad\text{for every Hermitian }\tilde H_\Psi .
$$

The Hermitian elements span the sector, so this is the statement that $\tilde Z$ commutes with the whole sector, hence with the algebra it generates together with $i$. The centre contains exactly the two roots $\pm i$, and the unit is forced to be one of them.

The forcing is what fixes the scalar field. Over the real quaternions the Hermitian elements are only the reals, too few to generate the algebra, and a non-central root such as $\vec e_x$ generates a norm-preserving flow for the Hamiltonians that algebra admits. Over the biquaternions the Hermitian elements are rich enough, the exceptional roots fail, and the unit lands in the centre. The complex numbers are therefore not a convenience of notation: they are the smallest coefficient field in which the norm-preserving unit is unique, and the uniqueness is what makes the equation a law rather than a family.

The conservation law is the commutator of the generator with the unit. The derivative of the norm vanishes identically because $G^{*}+G=0$, which is one line:

$$
\frac{d}{dr'_t}2\,\mathrm{Sc}\bigl(\tilde{Ξ}^{*}\tilde{Ξ}\bigr)
=2\,\mathrm{Sc}\bigl(\tilde{Ξ}^{*}\bigl(G^{*}+G\bigr)\tilde{Ξ}\bigr)=0 .
$$

The equation is not postulated with an anti-Hermitian generator; the generator is anti-Hermitian because the unit is central, and the conservation is a corollary of the centre.

The two theorems are the two halves of one statement about the sector's two forms. The quaternionic norm is preserved by the larger group and the Hermitian norm by the smaller one. The state space is defined by the smaller one's functional and by the larger one's cone, so it inherits the smaller group: a **preparation is Lorentz-covariant as a ray and not as a normalised state**. That asymmetry is the theme of the next section, where it becomes the difference between a four-vector and a velocity.

## The State of a Particle of Definite Velocity

A particle of definite velocity has a state, and the velocity fixes the state. For a particle of mass $m$ and velocity $\vec v$ the state element is

$$
\tilde{Ϛ}_\Psi=\tfrac12\Bigl(e_t+i\vec s_{\Psi}\Bigr),
\qquad
\vec s_{\Psi}=-\frac{\vec v}{c},
\qquad
N(\tilde{Ϛ}_\Psi)=\tfrac14\Bigl(\frac{mc^{2}}{E}\Bigr)^{2},
\qquad
S_{\mathrm{lin}}(\tilde{Ϛ}_\Psi)=\tfrac12\Bigl(\frac{mc^{2}}{E}\Bigr)^{2}.
$$

The state's radius is $\beta=\lvert\vec v\rvert/c$ and its axis is the direction of motion reversed. The sign is the sign of the phase in the wave function; the magnitude is not a convention.

**The positivity of the state and the causality of the momentum are one condition.** The state is positive exactly when $\lvert\vec s_{\Psi}\rvert\le1$, which is $\lvert\vec v\rvert\le c$, which is $E\ge\lvert\vec p\rvert c$, which is the statement that the four-momentum is future timelike or null. A spacelike momentum gives an element with $\lvert\vec s_{\Psi}\rvert>1$, which is not a state, and a past-pointing momentum gives a negative scalar part. **The state space is the future cone of the material sector**, and the ball's boundary is the light cone:

$$
\lvert\vec s_{\Psi}\rvert<1\ \leftrightarrow\ \text{timelike},
\qquad
\lvert\vec s_{\Psi}\rvert=1\ \leftrightarrow\ \text{null, a pure state},
\qquad
\lvert\vec s_{\Psi}\rvert>1\ \leftrightarrow\ \text{spacelike, no state} .
$$

The interval of the state is the inverse Lorentz factor. Applied to the state's radius,

$$
N(\tilde{Ϛ}_\Psi)=\tfrac14\bigl(1-\beta^{2}\bigr)=\tfrac14\gamma^{-2}=\tfrac14\Bigl(\frac{mc^{2}}{E}\Bigr)^{2},
\qquad
S_{\mathrm{lin}}(\tilde{Ϛ}_\Psi)=\tfrac12\gamma^{-2}.
$$

The linear entropy of the state of a particle is half the square of the inverse Lorentz factor. A massless particle has $\gamma=\infty$ and a pure state; a particle at rest has $\gamma=1$ and the maximally mixed state; and the mixedness falls as the particle is made relativistic. The quantity that measures how far a state is from a ray is the quantity that measures time dilation.

A boost acts on the ball as velocity addition, which is the statement that the ball is the velocity space. A boost of rapidity $\theta$ along the state's own axis carries the radius by the addition law of the previous section, $r'=(r+\tanh\theta)/(1+r\tanh\theta)$. Writing the radius as the hyperbolic tangent of a rapidity, $r=\tanh\rho$, the law is $\rho'=\rho+\theta$. The ball is therefore the Klein model of velocity space: its radius is the hyperbolic tangent of the rapidity, its centre is the rest frame, its boundary is the speed of light, and a boost is a hyperbolic translation. The Euclidean radius that measures mixedness and the hyperbolic distance that measures rapidity are the same coordinate in two readings.

The velocity is read off the state, and the two differ only by the factor $c$.

$$
\frac{\tilde V_\Phi}{c}=i\,e_t+\frac{\vec v}{c}=i\,e_t-\vec s_{\Psi},
\qquad
\tilde V_\Phi=ic\,e_t+\vec v .
$$

The state of a momentum is the four-velocity over $c$, up to the sign of its vector part, and the ball of states is therefore the set of all four-velocities: the affine slice of the sector's cone at unit weight is the hyperbolic ball of velocities.

The reverse direction takes every state to a velocity, and the two exceptional cases are the two ends. The centre of the ball is the rest frame, where $\vec v=0$ and $\gamma=1$; the boundary is the light cone, where $\lvert\vec v\rvert=c$ and the state is pure. A pure state is therefore the state of a massless particle, and the celestial sphere of the previous entry is its boundary. The state of a massive particle is never pure, and the heavier the particle at fixed energy, the more mixed its state.

The two entries of this section are one statement about one cone. Each of the following is a single fact read in the two sectors:

| the fact | in the material sector | in the informational sector |
| --- | --- | --- |
| the cone | the future cone of $N$, four-dimensional | the positive cone, a half of the same cone |
| the slice | the mass shell $N(\tilde P_\Phi)=-m^{2}c^{2}$ | the unit-scalar slice $2\,\mathrm{Sc}=1$ |
| the boundary | the light cone | the pure states |
| the classifier | timelike, null, spacelike | mixed, pure, not a state |
| the preserved group | $U(1)\cdot SL(2,\mathbb{C})$ for the form | $U(2)$ for the slice |
| the idempotents | none | a two-sphere of them |
| the form that vanishes on the boundary | $N$ | $N$, hence the linear entropy |
| what the boundary is | a null direction | a ray |

What the correspondence is not. It is not a derivation of quantum mechanics from relativity, and it is not a claim that a particle carries a thermal state. It is an algebraic statement about two slices of one cone, and it says that the two structures have the same shape because they are the same cone. The reading that a moving particle's state is mixed is an interpretation of the geometry of the ball: the radius is $\beta$, and it is not a statement about the reduced density matrix of a laboratory preparation.

A second check, in the other direction. Multiplication by $i$ carries a Hermitian element to an anti-Hermitian one and back, so the two sectors are exchanged and neither is embedded in the other. The classification of states by the cone does not depend on that exchange.

The correspondence explains the asymmetry of the two preserved groups. The material sector's element is classified by the quaternionic norm, which is preserved by $U(1)\cdot SL(2,\mathbb{C})$, so a four-momentum's causal class is a Lorentz invariant. The informational element's state space is a unit-scalar slice, which is preserved only by $U(2)$, so the purity of a state is not a Lorentz invariant. In the correspondence the two statements are the same statement: the radius of the ball is the velocity, and a boost changes the velocity. A boost cannot change whether a vector is timelike, and it can change how mixed a state is, because those are the two readings of one cone, and the boost acts on the cone and not on the slice.

## The Interpretations

### I.12.m — The State Is a Ray and Not a Vector

Read: the state $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_{\Psi})$, the idempotents $\tilde\Pi_{\mathrm{id},1}(\vec u)$, and the Bloch vector $\vec s_{\Psi}=-\vec v/c$.

The two objects that the standard formalism calls a state are different here, and only one of them is in this sector. A state vector is an element of the spinor module; the state of this entry is an element of the sector. The map between them is the rank-one construction, $\xi\mapsto\xi\xi^{*}$, and it is not injective: two spinors that differ by a central phase give the same idempotent. The phase is the one thing the map loses, and it is lost because it is central.

The algebra explains why the phase is unobservable and not merely unobserved. A weight is a ratio of scalar parts, and a central phase multiplies both factors of the product, so it cancels. The loss is not an imperfection of the description; it is the statement that the sector's objects are the ones a bilinear pairing can see. A state, in this framework, is what remains of a preparation when the pairing has been applied.

A superposition is therefore not a state in this sector either. The sum of two idempotents is not an idempotent, and the state that a superposition produces is the diagonal of the interference pattern, which is one point of the ball. The interference itself lives in the module and not in the sector, and the sector sees only its square.

Boundary. The entry does not construct the spinor module, does not state which spinor represents a given preparation, and does not derive the phase's disappearance from a dynamical argument. The rank-one map is quoted from the article on the spinor module, and the claim here is only that the sector's state is the image of it.

### I.12.n — A Pure State Is a Null Element

Read: $N(\tilde\Pi_{\mathrm{id},1,2})=0$, $2\,\mathrm{Sc}(\tilde\Pi_{\mathrm{id},1,2})=1$, and the zero-divisor cone.

The state of maximal information has zero weight in the sector's own form. The idempotents are null, $N=0$, so the pure states are exactly the elements of the sector that the quaternionic norm cannot see. The form that measures the interval of an event annihilates the state of a completely known system, and it does so at the same time as the scalar part takes its value $\tfrac12$. The two facts are compatible because the two forms are different.

**A pure state is a zero divisor and therefore has no inverse.** A mixed state is invertible in the algebra, and a pure state is not. The algebraic reading is that a maximal-information state cannot be undone by multiplication: there is no element whose product with it returns the unit. The statistical reading is that the pure state is the boundary of the cone, where the cone's interior structure degenerates.

The old vocabulary of a "ray" is the geometric name for nullness. A ray in the module is a null direction in the sector, and the projective line of rays is the two-sphere of null elements modulo the phase. Two descriptions of one set, and the sector's description is the one that gives the set its cone and its metric.

Boundary. Nullness here is nullness for the quaternionic norm of this algebra. It is not a statement that a pure state has zero energy, zero probability or zero norm for the Hermitian form, whose value on an idempotent is $\tfrac12$. Confusing the two forms produces the false statement that a pure state is "trivial".

### I.12.o — The Weight of a State Is Its Linear Entropy

Read: $S_{\mathrm{lin}}=2N$ on the slice, the spectral entropy $S(r)$, and the eigenvalue product $\eta_{+}\eta_{-}=\tfrac14(1-r^{2})$.

One quantity measures mixedness, and it is the form that also measures the interval. **The identity $S_{\mathrm{lin}}=2N$ is not a coincidence of two definitions**: both sides are functions of $\eta_{+}\eta_{-}$, and the product of the eigenvalues is the norm of the state. The consequence is that every statement about mixedness is a statement about the position of the state in the cone, and conversely.

The first reading is thermal. The Gibbs state of a Hamiltonian $\tilde H_\Psi=h_te_t+i\vec h_\Psi$ is the state whose radius vector is $\vec s_{\Psi}=-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$, with $\beta=1/(k_BT)$. The radius is the magnetisation, its saturation at low temperature is the approach to the boundary, and at high temperature the expansion of the hyperbolic tangent gives $\lvert\vec s_{\Psi}\rvert\approx\lvert\vec h_\Psi\rvert/(k_BT)$, which is Curie's law. The centre of the ball is the infinite-temperature state, and the boundary is unreachable at any finite temperature.

The second reading is entanglement. For a pure state of two carrier copies, the reduced state of one copy is a state of this sector, and its concurrence is $\mathcal{C}=2\sqrt{N(\tilde{Ϛ}_\Psi)}$. A maximally entangled pair has $N=\tfrac14$ and $\mathcal{C}=1$; a product state has $N=0$ and $\mathcal{C}=0$. The mixedness of a half and the entanglement of the whole are the same number, and the factor two is the one that appears throughout the sector.

The third reading is decoherence. A state that is entangled with an environment and then traced over is a state of this sector, and the partial trace is a map that moves it inward. The purity falls, the linear entropy $2N$ rises, and the entropy $S(r)$ rises with it. The boundary is where the environment has learned nothing; the interior is where it has.

Boundary. The concurrence formula uses the standard two-qubit expression for a pure pair and is quoted as a reading of $N$; the framework computes the reduced state's norm and does not by itself define an entanglement measure. The thermal reading requires the identification of $\beta$ with an inverse temperature, which is the standard Gibbs construction. Neither reading adds a dynamical law to the algebra.

### I.12.p — Normalisation Is a Slice and Not a Law

Read: the ratio form of the weight, the slice $\{\mathrm{Sc}=\tau\}$, and the group that preserves it.

The unit-scalar condition is a choice of scale, and the weight does not depend on it. The probability is a quotient of two pairings, so a rescaling of the state cancels. Any positive element is a positive multiple of a state, and any measurement is a weight on the cone, normalised by the scalar part of the element that is measured against. The value $\tfrac12$ is a convention of the same kind as the choice of a unit of mass.

The convention is not arbitrary within a frame, and the reason is the group. Among all positive functionals, the scalar part is the one invariant under the unitary action, and it is the order unit of the cone. A normalisation by another functional would define a different slice and would not be preserved by the same group. So the choice of *which* functional is canonical, and the choice of *value* is not.

The physical content is that a preparation has an intensity and a shape, and only the shape is a state. A beam of particles with twice the flux has twice the scalar part and the same state. The intensity is what the scalar part measures, and the shape is what the radius vector measures. The sector keeps both, and the ratio throws the first away.

Boundary. The statement concerns the sector's own normalisation. It does not say that normalisation is physically meaningless in a theory with a superselection rule on particle number, where the normalisation can be fixed by the superselection charge; the sector has no such charge.

### I.12.q — The Born Weight Is an Analyser Transmission

Read: $p_+=\tfrac12(1+\vec u\cdot\vec s_{\Psi})$, the half-angle form $\cos^{2}(\theta/2)$, and the two-projector decomposition.

The weight is the law of an analyser. A preparation along $\vec s_{\Psi}$ meets an analyser along $\vec u$, and the transmitted fraction is $\tfrac12(1+\vec u\cdot\vec s_{\Psi})$. The law interpolates between certainty at $\vec u=\vec s_{\Psi}$ and impossibility at $\vec u=-\vec s_{\Psi}$, with equal transmission at a right angle. Every two-outcome measurement of the sector is an instance of it, because every two-outcome projective measurement is a pair of idempotents on some axis.

The half in the angle is the double cover, and it is visible in the formula. The analyser is set by an axis of the three-space, and the state is set by an axis too, but the natural angle of the transmission law is half the angle between them. A rotation of the analyser by $\pi$ returns the same analyser and exchanges the two outcomes; a rotation of the state by $2\pi$ returns the same state. The two-to-one geometry of the sphere over the ray space is what the half-angle records.

The formula contains both a classical and a quantum term, and the split is the radius. Written as $p_+=\tfrac12+\tfrac12\vec s_{\Psi}\cdot\vec u$, the first term is the unbiased guess and the second is the correlation between the preparation and the analyser. For a state at the centre the second term vanishes and the analyser transmits half of everything; for a pure state the second term is the whole of the classical Malus correlation. Mixedness is the dilution of the correlation and nothing else.

Boundary. This is the algebraic analogue of the Malus law, not a derivation of the electromagnetic law of the same form. The electromagnetic statement concerns the intensity of a classical field through a polariser; the statement here concerns the frequency of an outcome for a state. They agree in form because both are quadratic in a projection, and the agreement is not evidence that the two objects are the same.

### I.12.r — The Observable and the State Are One Space

Read: both objects as elements of $\mathbb{B}_{\Psi}$, the symmetric pairing, and the identity $\tilde H_\Psi=iA$.

There is one space and two roles, and the roles are fixed by normalisation and by the cone. The pairing takes two elements of the sector and returns a number, and it does not care which is which. A state is an element of the cone at unit weight; an observable is an element of the sector with no normalisation. The symmetry of the pairing is therefore exact, and the asymmetry of the roles is the asymmetry of the conditions, not of the objects.

The pairing has a second reading in which one slot is material. Since every Hermitian element is $iA$ with $A$ anti-Hermitian, the weight pairs an informational element with a material one, and the factor $i$ converts the imaginary scalar part into a real reading. This is the algebraic form of the statement that an apparatus is a physical object: the thing measured is described by the other sector, and the description is one multiplication away.

The standard separation into two kinds of object is not available here. A state is not a vector and an observable is not an operator on vectors: both are elements, and the operator is the element's left multiplication, which is a different object again. The two kinds of the standard formalism are two uses of one space, and the framework's claim is that this is what the algebra supplies.

Boundary. The symmetry of the pairing does not make states and observables interchangeable in a physical statement. A state has unit weight and a fixed cone; an observable has any spectrum and no normalisation. Reading an observable as a state is a category error, and the algebra prevents it only by the two conditions, not by the shape of the object.

### I.12.s — The Noise Is the Component the State Cannot Predict

Read: the variance $\lvert\vec h_\Psi\rvert^{2}(1-r^{2}\cos^{2}\theta)$ and its residue $(1-r^{2})\lvert\vec h_\Psi\rvert^{2}$ on the aligned axis.

Two independent reasons prevent a definite outcome, and the formula multiplies them. A direction that is not the observable's own leaves a transverse part of the observable, and a radius below one leaves a residue even on the aligned axis. The first is the quantum reason and it is present for a pure state; the second is the mixedness reason and it is present for every mixed state. A state with $r<1$ has no eigenstate.

The aligned residue is a measurable prediction, and it is not small. For a state of radius $r$ and an observable whose vector part has length $\lvert\vec h_\Psi\rvert$, the variance on the aligned axis is $(1-r^{2})\lvert\vec h_\Psi\rvert^{2}$, and the standard deviation is $\sqrt{1-r^{2}}\,\lvert\vec h_\Psi\rvert$. A thermal state at high temperature therefore has a spread comparable to the observable's own scale, and no preparation short of a pure one removes it.

The variance of a projector is the weight times its complement. For an idempotent the two eigenvalues are one and zero, so the variance is $p_+(1-p_+)$, the Bernoulli variance. The general formula reduces to it at $\lvert\vec h_\Psi\rvert=\tfrac12$ and $h_t=\tfrac12$, which is a check that the algebraic variance and the statistical variance of a two-outcome experiment are the same object.

Boundary. The variance computed here is the algebraic second moment of one element in one state. It is not an experimental error budget, which would add the noise of the apparatus; and it is not the Robertson inequality, which requires two observables and the commutator, and which this entry does not derive.

### I.12.t — An Effect Is a Measurement of Finite Resolution

Read: the interval $[0,e_t]$, the conditions $\lvert\vec w\rvert\le\min(a,1-a)$, the sharpness $\digamma_{\mathrm{blc}}$, and the trine POVM.

The interval is the set of measurements, and its interior is the set of imperfect ones. The two endpoints are the never and the always; the boundary circle at $a=\tfrac12,\lvert\vec w\rvert=\tfrac12$ is the set of perfect analysers; and everything between is an analyser with finite contrast. The parameter $\digamma_{\mathrm{blc}}$ names the contrast, and the identity $\tilde{\mathcal E}_{\Psi,+}^{2}-\tilde{\mathcal E}_{\Psi,+}=\tfrac14(\digamma_{\mathrm{blc}}^{2}-1)e_t$ says that the effect is a projection exactly at unit contrast.

A finite-resolution measurement is not a defective perfect one. The two outcomes of an unsharp analyser overlap, and the overlap is a property of the apparatus and not of the state. The weight $p_\pm=\tfrac12(1\pm\digamma_{\mathrm{blc}}\vec u\cdot\vec s_{\Psi})$ shows the two roles separately: $\digamma_{\mathrm{blc}}$ belongs to the measurement and $\vec s_{\Psi}$ to the preparation, and the product is what the experiment reads. No improvement of the preparation can raise $\digamma_{\mathrm{blc}}$.

The three-outcome measurement is the case that no basis supplies. Three effects at $120^\circ$ sum to the unit and none is a projection, so the measurement has three exclusive alternatives and no orthonormal family of three exists in a two-dimensional carrier. The interval supplies the alternatives without enlarging the carrier, and the dilation supplies the projective realisation on a larger one.

Boundary. The interval gives the statistic and not the update. The post-measurement state needs Kraus operators, which the interval does not determine, and two instruments with the same effects can update differently. The entry states the statistic and refers the update to the channel article.

### I.12.u — The Metric Is a Quarter of the Sphere

Read: $ds^{2}=\tfrac14\lvert d\vec u\rvert^{2}$, the half-angle in $\cos^{2}(\theta/2)$, and the trace distance $\sin d_{\mathrm{FS}}$.

The geometry of the state space is fixed and not chosen. The two forms of the sector supply the transition probability and the line element, and the line element is the Fubini–Study one. There is no freedom in it: the normalisation of the identity fixes the scale, and the half-angle of the double cover fixes the factor of a quarter. A different coefficient would contradict the transition probability computed from the same forms.

The quarter is the square of the half-angle, and it is visible in one comparison. Two states at an angle $\theta$ on the sphere have a transition probability $\cos^{2}(\theta/2)$, which is the square of the cosine of half the angle. The metric is the same half-angle squared, so the metric and the probability are two derivatives of one function. A measurement that turns an analyser by $\theta$ changes the probability by the square of the half-angle and the distance by the half-angle itself.

The compactness of the state space is the statement that the spin is finite. The sphere of pure states has a finite area and no boundary of its own, and the ball is its convex hull. A carrier of higher spin would have a larger sphere with a different total area, and the number that distinguishes them is the one in the symplectic form. The state space's size is a quantum number and not a parameter.

Boundary. The metric statement is exact on the pure states. On the interior the distinguished metric is the Bures one, which the algebra's own forms do not supply, and the flat form that the norm gives is not it. The entry states the boundary result and declines the interior.

### I.12.v — The Commutator Is an Area

Read: $J_{\vec u}(v)=\tfrac12[\vec u,v]$, $\omega=-i\operatorname{Sc}(\tilde\Pi_{\mathrm{id}}[\delta_1\tilde\Pi_{\mathrm{id}},\delta_2\tilde\Pi_{\mathrm{id}}])$, and the total area $\pi$.

The antisymmetric product of the algebra is the complex structure of the state space. On the sphere of pure states, the commutator with the state's own axis is a rotation by a right angle in the tangent plane, and it squares to minus the identity. The algebra's bracket is therefore not only the measure of non-commutation; at a state it is the operation that turns a displacement into an orthogonal one.

The two-form is an area, and the area is finite. The symplectic form is the metric composed with the complex structure, and its integral over the sphere is $\pi$, which is $2\pi$ times the spin. The state space is a phase space with a finite and fixed volume, and the number that measures the volume is the spin of the carrier. In units where the symplectic form is measured in units of the action, the area per state is a fixed quantum, and that quantum is what the algebra's normalisation has set.

The bracket also supplies the uncertainty relation's left-hand side. For two observables, the commutator is twice the cross product of their vector parts, so the commutator's size is the area of the parallelogram they span. The uncertainty relation's bound is therefore an area in the same three-space where the state is a ball, and the two structures — the state's geometry and the observables' non-commutation — are two uses of one cross product.

Boundary. The identification of the area with a number of Planck cells requires the invertibles, and the entry does not make it. The claim is the finiteness of the area and its value $\pi$ in the normalisation $\operatorname{Sc}(e_t)=1$. A quantisation argument that fixes $\frac{h}{2\pi}$ is outside this entry.

### I.12.w — The Imaginary Unit Is Forced by the Centre

Read: the flow $G=-\frac{2\pi \tilde Z\tilde H_\Psi}{h\,c}$, the condition $\tilde H_\Psi\tilde Z=\tilde Z\tilde H_\Psi$, and the two central roots of $-e_t$.

The $i$ of the evolution equation is not a convention of notation. A root of $-e_t$ exists in abundance: every unit pure direction times $i$ is one. Each such root gives a flow, and each flow preserves the norm of the state only for the Hamiltonians with which it commutes. A dynamics that must preserve the norm for every admissible Hamiltonian forces the root into the centre, and the centre contains two roots and no more.

The forcing is a statement about the richness of the observable algebra. Over the real quaternions the Hermitian elements are the reals alone, and a non-central root generates a norm-preserving flow because there is nothing to fail to commute with. The biquaternion algebra's Hermitian sector is rich: it contains the three imaginary directions, which are exactly the elements that a non-central root fails to commute with. The complex coefficient is what makes the requirement bite.

The physical content is that the unit of the theory is a scalar and not a direction. A non-central root would make the evolution depend on a direction in space, and the norm would fail for some Hamiltonian. The scalar root is the only one that no Hamiltonian can detect, and the theory's invariance under the rotation group is what rules the others out.

Boundary. The theorem establishes necessity within this algebra's dynamics. It does not establish that nature uses this algebra, and it does not exclude a real formalism with a different notion of state, such as a real Hilbert space with a complex structure supplied by an operator. The claim is conditional on the carrier being $\mathbb{B}$.

### I.12.x — A Boost Is Not a Symmetry of the State Space

Read: the preservation of the cone by every invertible congruence, the preservation of the slice by $U(2)$, and the radius law $r'=(r+\tanh\theta)/(1+r\tanh\theta)$.

The two halves of the state space have different symmetry groups, and the intersection is the smaller one. Positivity is preserved by the general linear group; the unit-scalar condition only by the unitary group. The state space is the intersection of the cone and the slice, so its symmetry group is the intersection of the two, and a boost is in the first and not in the second.

A boost therefore changes the purity of a mixed state, and it leaves a pure state pure. A congruence by an invertible element preserves rank, so an idempotent stays an idempotent; the scalar part changes and the normalised state has a different radius only if it was mixed. The pure states are the fixed points of the effect, and the centre of the ball is the state that moves the most.

The physical reading is that spin is not a Lorentz-covariant notion in this sense. The normalised state of a system is defined with respect to a frame, and a change of frame changes the normalisation and the mixedness. What is covariant is the ray, which is the boundary, and that is why the celestial sphere of the previous entry is the Lorentz-covariant object while the ball is not. The Wigner rotation is the residue of the same fact: the little group acts on the state, and the boost moves it between slices.

Boundary. The statement is about the normalised state space, not about the algebra's Lorentz action, which is perfectly well defined on the whole sector. Any element transforms, and the transformed element is still in the sector; what fails is that the transformed element is again a state of unit weight.

### I.12.y — The Ball Is the Velocity Space

Read: $\tilde V_\Phi/c=i\,e_t+\vec v/c=i\,e_t-\vec s_{\Psi}$, and $N(\tilde{Ϛ}_\Psi)=\tfrac14\gamma^{-2}$.

The dictionary makes the ball the set of velocities. Inverting the preparation map turns a normalised state into a four-velocity over $c$, and the inverse is defined on the whole ball. The centre is the rest frame, the boundary is the speed of light, and the radius is the speed fraction. The positivity of the state and the causal bound on a velocity are the same inequality, and this is the entry's sharpest structural statement.

Velocity space is hyperbolic, and the ball is its Klein model. The composition of boosts along one axis is the addition law $r'=(r+\tanh\theta)/(1+r\tanh\theta)$, so the radius is the hyperbolic tangent of the rapidity. The Euclidean ball with the radius as coordinate is therefore the Klein model of hyperbolic three-space, and a boost is a hyperbolic translation. The pure states are the sphere at infinity.

The mixedness of the state of a particle is its time-dilation factor. The linear entropy is $\tfrac12\gamma^{-2}$, so the state is pure for a massless particle, maximally mixed at rest, and mixed in proportion to $mc^{2}/E$. Entropy, purity and rapidity are three names for one coordinate of the same ball, and the coordinate is the velocity.

Boundary. The correspondence is between two slices of two cones of one algebra, and the identification of the state with the spin state of a particle is a reading of it. The entry does not claim that a particle's laboratory state is thermal, and it does not derive a density matrix from a momentum. The arithmetic of the ball is exact and checked; the naming of its radius as the velocity is an interpretation.

## The Limits

**The entry derives the structure of the probability assignment and not its empirical validity.** Every weight computed here is a number the algebra assigns; that experiments produce those numbers as frequencies is not a theorem of the algebra and is not claimed as one. The framework's position is the standard one on this point, and the entry states it rather than leaving it to be inferred.

The entry has no dynamics. No Hamiltonian is derived, no time evolution beyond the conjugation flow is constructed, and no field equation appears. The flow of §*The Flow and the Centre* is the one-parameter group generated by a given Hermitian element, and the selection of which element is a dynamical input that the sector does not supply.

The carrier is two-dimensional, and the entry is about one carrier. The sector's idempotents are a two-sphere, the ball is three-dimensional, and the effect interval is the interval of this carrier. A composite system needs the tensor product, and the entanglement reading of the weight is quoted for the two-copy case only. Nothing here is a statement about a spin-$s$ carrier with $s>\tfrac12$, whose state space would be a larger ball with a different symplectic area.

The coincidence of the positivity cone and the causal cone is a property of this norm. The two cones have the same boundary because the sector's two blocks carry the signs $(1,3)$ and $(4,0)$ with one sign difference in the direction block. A different quadratic form on the same sector would give a different ball, and the correspondence with the material sector would fail. The result is exact for the quaternionic norm and is not a general fact about real four-spaces.

The interior metric is not supplied. The algebra gives the Fubini–Study metric on the boundary and a flat form on the interior, and the Bures metric is neither. The entry states this limit where the geometry is computed and does not repair it. A reader who needs the metrically distinguished interior must add a structure the algebra does not contain; that structure, once added, is the hemisphere of *The Fubini–Study Geometry and the Biquaternion Norm*, and its boundary is the metric the algebra does give.

The entanglement reading is a reading. The identity $\mathcal{C}=2\sqrt{N}$ is exact for a pure state of two carrier copies and uses the standard concurrence formula; the framework computes $N$ and does not define an entanglement measure. The thermal reading likewise requires the Gibbs construction, which is an assumption about the state and not a theorem about the sector.

There is no element that is both a position and a state. The state is $\tfrac12(e_t+i\vec s_{\Psi})$ with $\vec s_{\Psi}=-\vec v/c$, and the velocity is read from it as $\tilde V_\Phi/c=i\,e_t-\vec s_{\Psi}$. The four-position is a different element with different numbers, and no factor carries one into the other. The naming of that state as the state of a particle of that velocity is an interpretation, and its scope is stated in §*The State of a Particle of Definite Velocity*.

No claim is made about the measurement problem. The entry computes weights and states that the update of a state after a measurement requires Kraus operators that the interval does not fix. It says nothing about when a measurement occurs, about the reality of the state before it, or about the interpretation of the probability beyond its algebraic form.

## Summary

The sector is one real four-space with two quadratic forms. The Hermitian form is positive definite of inertia $(4,0)$ and supplies the probabilities; the quaternionic norm is indefinite of inertia $(1,3)$ and supplies the geometry, the cone and the mixedness. The other two forms of the algebra collapse onto these two on this sector.

An observable is an element, and its spectrum is two real numbers. Every Hermitian element factors through the two idempotents of its own axis, with eigenvalues $h_t\pm\lvert\vec h_\Psi\rvert$. Positivity is $h_t\ge\lvert\vec h_\Psi\rvert$, and the order is the order of the cone.

A state is an element of the same cone at unit weight. It is $\tfrac12(e_t+i\vec s_{\Psi})$ with $\lvert\vec s_{\Psi}\rvert\le1$, its eigenvalues are $\tfrac12(1\pm r)$, its purity is $\tfrac12(1+r^{2})$, and its mixedness is the norm: $S_{\mathrm{lin}}=2N$.

The pure states are the null elements and the boundary of the ball. They are the idempotents, the zero divisors of the sector, and the extreme points of the convex set. The centre is the maximally mixed state and the fixed point of every rotor.

The Born weight is the normalised Hermitian pairing. It is $h_t+\vec s_{\Psi}\cdot\vec h_\Psi$, and for a projector it is $\tfrac12(1+\vec u\cdot\vec s_{\Psi})$. Reality, positivity and normalisation follow from the algebra; that the numbers are frequencies does not.

The variance is the part of the observable the state cannot predict. It is $\lvert\vec h_\Psi\rvert^{2}(1-r^{2}\cos^{2}\theta)$, with a transverse term and a mixedness term, and only a pure state has an eigenstate.

The effects are the interval between zero and the unit. The projections are its extreme points, a general resolution of the unit is a POVM, and the sharpness $\digamma_{\mathrm{blc}}$ names the resolution of a two-outcome measurement. The interval gives statistics and not the post-measurement state.

The geometry is the algebra's own. The boundary is the projective line with the Fubini–Study metric, a quarter of the round sphere; the complex structure is the commutator; the symplectic area is $\pi$, which is $2\pi$ times the spin.

The state space is preserved by $U(2)$ and by nothing larger. Positivity survives every invertible congruence, the scalar part only the unitary group, and the state space is their intersection. A boost moves a mixed state off the slice and changes its radius by the velocity-addition law.

The imaginary unit of the flow is forced. The unit of the state-vector equation must be central for the norm to be preserved for every Hamiltonian, and the centre's only roots of $-e_t$ are $\pm i$. Over the real quaternions the requirement fails to bite, which is why the coefficient field is complex.

The two entries of this section are one statement about one cone. A particle of velocity $\vec v$ has the state of radius $\beta$, a null momentum gives a pure state, and a spacelike momentum gives nothing. The ball is the velocity space, its radius is the hyperbolic tangent of the rapidity, and the linear entropy of a particle's state is $\tfrac12\gamma^{-2}$.

## Summary of Notation

| object | notation | content |
| --- | --- | --- |
| the sector | $\mathbb{B}_{\Psi}$ | the Hermitian half, $\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ |
| the observable | $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ | real weight, real direction |
| the spectrum | $\eta_{\pm}$ | $h_t\pm\lvert\vec h_\Psi\rvert$ |
| the axis | $\vec u_\Psi$ | $\vec h_\Psi/\lvert\vec h_\Psi\rvert$ |
| the idempotent | $\tilde\Pi_{\mathrm{id},1,2}(\vec u)$ | $\tfrac12(e_t\pm i\vec u)$, pure state on the axis $\vec u$ |
| the state | $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_{\Psi})$ | positive, unit weight, $\lvert\vec s_{\Psi}\rvert\le1$ |
| the Bloch radius | $r$ | $\lvert\vec s_{\Psi}\rvert$, the mixedness, $\tanh\rho$ |
| the rapidity of the state | $\rho$ | $\mathrm{artanh}\,r$ |
| the purity | $P(\tilde{Ϛ}_\Psi)$ | $\tfrac12(1+r^{2})=2\,\mathrm{Sc}(\tilde{Ϛ}_\Psi^{2})$ |
| the linear entropy | $S_{\mathrm{lin}}$ | $\tfrac12(1-r^{2})=2N$ |
| the von Neumann entropy | $S(\tilde{Ϛ}_\Psi)$ | $-\sum_\pm\tfrac12(1\pm r)\log\tfrac12(1\pm r)$ |
| the Hermitian pairing | $\langle\cdot,\cdot\rangle_{*}$ | $\mathrm{Sc}$ of the product with the starred second factor |
| the scalar part | $\mathrm{Sc}\tilde Q=Q_t$ | the coefficient of $e_t$, the functional the weight is built on |
| the Born weight | $\langle\tilde H_\Psi\rangle_{\tilde{Ϛ}_\Psi}$ | $h_t+\vec s_{\Psi}\cdot\vec h_\Psi$ |
| the weight of a projector | $p_\pm$ | $\tfrac12(1\pm\vec u\cdot\vec s_{\Psi})$ |
| the variance | $\bigl\langle\tilde H_\Psi^{2}\bigr\rangle-\bigl\langle\tilde H_\Psi\bigr\rangle^{2}$ | $\lvert\vec h_\Psi\rvert^{2}(1-r^{2}\cos^{2}\theta)$ |
| the effect | $\tilde{\mathcal E}_{\Psi}=a\,e_t+i\vec w$ | $0\le a\le1$, $\lvert\vec w\rvert\le\min(a,1-a)$ |
| the sharpness | $\digamma_{\mathrm{blc}}$ | $\lvert\vec w\rvert/(\min(a,1-a))$ for the symmetric family |
| the POVM | $\{\tilde{\mathcal E}_{\Psi,k}\}$ | positive effects summing to $e_t$ |
| the conjugation action | $\Gamma_{\tilde U}$ | $\tilde U\tilde X\tilde U^{*}$ |
| the unit of the flow | $\tilde Z$ | a root of $-e_t$, forced central, $\pm i$ |
| the line element | $ds^{2}_{\mathrm{FS}}$ | $\tfrac14\lvert d\vec u\rvert^{2}$ |
| the symplectic form | $\omega$ | $\tfrac14\vec u\cdot(\delta_1\vec u\times\delta_2\vec u)$ |
| the complex structure | $J_{\vec u}$ | $\tfrac12[\vec u,\cdot]=\vec u\times$ |
| the Fubini–Study distance | $d_{\mathrm{FS}}$ | $\theta/2$ |
| the trace distance | $D$ | $\sin d_{\mathrm{FS}}$ |
| the state of a momentum | $\vec s_{\Psi}=-\vec v/c$ | radius $\beta$, axis reversed |
| the velocity of a state | $\tilde V_\Phi/c=i\,e_t-\vec s_{\Psi}$ | $i\,e_t+\vec v/c$, read off the Bloch vector |

## Further Reading

The geometry. [The Fubini–Study Geometry and the Biquaternion Norm](the-fubini-study-geometry-and-the-biquaternion-norm.html) treats the metric, the Kähler form and the distances; the ball, the purity, the entropy and the fidelity are stated here.

The flow. [The Group of Invertibles, the Cone and the Orders](the-group-of-invertibles-the-cone-and-the-orders.html) proves the two normalisation theorems and the centrality of the unit.
The cone of squares. [The Biquaternion Algebra as a JB-Algebra](../articles_maths/the-biquaternion-algebra-as-a-jb-algebra.html) supplies the object behind the two conditions of this article: the positivity of a state is membership in the cone of squares of the symmetrised plain product, the unit-scalar condition is a hyperplane section of it, the pure states are its rank-one idempotents, and the Born weight is a positive functional normalised at the order unit.

The previous entry of the section. [Four-Vectors and the Interval](four-vectors-and-the-interval.html) is the material sector read as spacetime, and its §*The Lorentz Action* is the action that the last section of this entry reads on the ball.

The relativistic qubit. [The Relativistic Qubit in Biquaternionic Form](the-relativistic-qubit-in-biquaternionic-form.html) treats the module, the rays, the celestial sphere and the little group, and it states the failure of the state space to be Lorentz-invariant.

The measurement. [The Polar Decomposition of a Kraus Operator: Effect, Backaction and the Measurement Boundary](the-polar-decomposition-of-a-kraus-operator-effect-backaction-and-the-measurement-boundary.html) is where the update that the interval does not supply is constructed.

The thermodynamics. [Quantum Thermodynamics in Biquaternionic Form](quantum-thermodynamics-in-biquaternionic-form.html) owns the Gibbs state and the Bloch vector $\vec s_{\Psi}=-\tanh(\beta\lvert\vec h_\Psi\rvert)\vec u_\Psi$ quoted in §*The Interpretations*.

The standard background. The density-operator formalism and the Born rule are treated in Nielsen and Chuang, *Quantum Computation and Quantum Information*, and in Peres, *Quantum Theory: Concepts and Methods*; the effect algebra and the POVM formalism in Busch, Grabowski and Lahti, *Operational Quantum Physics*; and the geometry of the state space in Bengtsson and Życzkowski, *Geometry of Quantum States*.

The mathematics. The Squares and the Positive Cone of the Biquaternion Sesqualgebra owns the cone, [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) owns the restrictions, and [Effect Algebras and Orthomodular Lattices](../articles_maths/effect-algebras-and-orthomodular-lattices.html) owns the interval.
