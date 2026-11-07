# __The Informational Sector: States, Observables and Probability__

## Introduction

The informational sector is the Hermitian subspace $\mathbb{B}_{\Psi}$. It is the fixed space of the Hermitian conjugation, the half of the algebra in which the scalar coefficient is real and the three vector coefficients are imaginary. Its mathematics is the mathematics of a two-state quantum system: the Hermitian elements are observables, the positive elements normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$ are states, the Hermitian idempotents are pure states, the Hermitian form is the Born pairing, and the sandwich by a matrix-unitary element is the evolution.

That mathematics is established algebra. What is not established is whether the sector is a distinct sector of the physical world in the sense in which the material sector is spacetime. The article states the hypothesis, develops the algebraic interpretation in full, and marks the boundary at the point where the algebra ends and the physics begins.

This article states each result in brief, links the mathematics article that owns it, and gives the physical interpretation with its boundary.

The results used are these.

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The subspace, its basis and its coordinate blocks | [Subspaces and Decompositions](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html) |
| The roots of $+1$ and the Hermitian idempotents | [Idempotents](../articles_maths/idempotents.html) |
| The norm, the spectrum and the positive cone | [The Squares and the Positive Cone of the Biquaternion Sesqualgebra](../articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.html) |
| The eigenvalue decomposition, the normality criterion and the non-normal pair | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| The four forms and their restrictions | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |
| The action on the material sector and the sandwich | [Two-Sided Operators on the General Plain Sesqualgebra](../articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra.html) |
| The $*$-unitary slice and the matrix-unitary condition | [Unitary Operators of a Sesqualgebra](../articles_maths/the-unitary-operators-of-a-sesqualgebra.html) |
| The Jordan algebra of the symmetrised product | [Jordan Algebras of Sesqualgebras](../articles_maths/jordan-algebras-of-sesqualgebras.html) |
| The matrix model and the Hilbert–Schmidt pairing | [$M_2(\mathbb{C})$ Representation : The General Plain Sesqualgebra of Biquaternions](../articles_maths/m2c-representation-the-general-plain-sesqualgebra-of-biquaternions.html) |

## The Results It Uses

### Definition and Basis

The informational sector is

$$
\mathbb{B}_{\Psi}=\{\tilde Q\in\mathbb{B}:\tilde Q^{*}=\tilde Q\},
$$

the fixed space of the Hermitian conjugation. In coordinates it is the set of elements with a real scalar coefficient and imaginary vector coefficients,

$$
\tilde R_\Psi=c r_t\,e_t+i r'_x\vec e_x+i r'_y\vec e_y+i r'_z\vec e_z,
$$

with $r_t,r'_x,r'_y,r'_z\in\mathbb{R}$. The parameters are the coordinates themselves, so the general element is

$$
\tilde R_\Psi=c r_t\,e_t+i\bigl(r'_x\vec e_x+r'_y\vec e_y+r'_z\vec e_z\bigr).
$$

The basis is $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, of real dimension four. The sector is the sum of two blocks, the real scalar block $A_1=\mathbb{R}e_t$ and the imaginary vector block $B_2=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$. Every element of the sector is its own Hermitian part, $\tilde Q=\tilde R_\Psi$. The temporal direction carries a real coordinate and the three spatial directions carry imaginary ones, the reverse of the material sector; the placement of the $i$ is a property of the sector, fixed by the conjugation that defines it.

The sector is not a subalgebra: the product of two Hermitian elements is Hermitian exactly when they commute, and the commutator of two of them lies in $\mathbb{B}_{\Phi}$. The sector is a **special Jordan algebra** under the symmetrised product $\tfrac12\{\tilde Q_1,\tilde Q_2\}$, and it is not a Lie algebra.

### The Idempotents and the Roots of $+1$

A real unit vector $\vec u$ gives a root of $+1$ in the sector,

$$
(i\vec u)^2=i^2\vec u^2=(-1)(-e_t)=+e_t,
$$

the two minus signs cancelling. The two idempotents along the axis are

$$
\boxed{\;\tilde\Pi_{1,2}(\vec u)=\tfrac12\bigl(e_t\pm i\vec u\bigr)\;}.
$$

They are Hermitian, idempotent, normalised by $\langle\tilde\Pi,e_t\rangle_{*}=\tfrac12\langle e_t\rangle$ (trace one in the $2\times2$ image), orthogonal and complete:

$$
\tilde\Pi_1+\tilde\Pi_2=e_t,\qquad \tilde\Pi_1\tilde\Pi_2=\tilde\Pi_2\tilde\Pi_1=0.
$$

They are the **pure states** of the sector, and they are the biquaternion analogues of the pure-state density matrices of a qubit. The material sector owns no non-trivial idempotent: if $\tilde\Pi^2=\tilde\Pi$ and $\tilde\Pi^{*}=-\tilde\Pi$, applying the star to the first relation gives $-\tilde\Pi=\tilde\Pi^2=\tilde\Pi$, hence $\tilde\Pi=0$. The sign that makes the idempotents possible is the sign of $(i\vec u)^2$, and it is the algebraic reason the states live in $\mathbb{B}_{\Psi}$ and not in $\mathbb{B}_{\Phi}$.

### The Biquaternion Norm, the Spectrum and the Positive Cone

The biquaternion norm on the sector is

$$
\langle\tilde R_\Psi\rangle_{\natural}=c^2r_t^2-\lvert\vec r_\Psi\rvert^2=c^2 r_t^2-{r'_{x}}^2-{r'_{y}}^2-{r'_{z}}^2,
$$

of signature $(1,3)$: one positive temporal direction and three negative spatial ones. It is indefinite, and it is not the positive form that a density matrix would suggest.

Every Hermitian element has a closed-form spectrum. Write $\tilde R_\Psi=c r_t e_t+i\vec r_\Psi$ with $c r_t$ and $\vec r_\Psi$ real, and let $\vec u_\Psi=\vec r_\Psi/\lvert\vec r_\Psi\rvert$ for $\vec r_\Psi\neq0$. Then

$$
\tilde R_\Psi=\bigl(c r_t+\lvert\vec r_\Psi\rvert\bigr)\tilde\Pi_1(\vec u_\Psi)+\bigl(c r_t-\lvert\vec r_\Psi\rvert\bigr)\tilde\Pi_2(\vec u_\Psi),
$$

with the eigenvalues

$$
\boxed{\;\lambda_\pm=c r_t\pm\lvert\vec r_\Psi\rvert\;}.
$$

The Hermitian form against the unit and the biquaternion norm read

$$
\langle\tilde R_\Psi,e_t\rangle_{*}=c r_t,\qquad 2\langle\tilde R_\Psi,e_t\rangle_{*}=2c r_t=\lambda_++\lambda_-,\qquad \langle\tilde R_\Psi\rangle_{\natural}=c^2 r_t^2-\lvert\vec r_\Psi\rvert^2=\lambda_+\lambda_-,
$$

whose middle entry is the trace in the $2\times2$ image, $\operatorname{Tr}(\tilde R_\Psi)=2c r_t$.

The element is **positive** exactly when $c r_t\geq\lvert\vec r_\Psi\rvert$, that is, exactly when both eigenvalues are non-negative. Positivity is a statement about the eigenvalues, not about the biquaternion norm: the norm is negative exactly when the two eigenvalues have opposite signs.

The **state slice**, which the $2\times2$ reading calls the trace-one slice, is the family

$$
\tilde{Ϛ}_{\Psi}=\tfrac12\bigl(e_t+i\vec r\bigr),\qquad \langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*},
$$

with $\vec r$ a real vector. Its spectral decomposition is

$$
\boxed{\;\tilde{Ϛ}_{\Psi}=\frac{1+r}{2}\tilde\Pi_1(\vec u)+\frac{1-r}{2}\tilde\Pi_2(\vec u),\qquad \vec r=r\vec u\;},
$$

so $\tilde{Ϛ}_{\Psi}$ is positive exactly when $\lvert\vec r\rvert\leq1$. The boundary $\lvert\vec r\rvert=1$ is the set of pure states, the interior $\lvert\vec r\rvert<1$ the mixed states, and the centre $\vec r=0$ the maximally mixed state $\tfrac12e_t$. The whole set is the **Bloch ball**, of real dimension three.

The biquaternion norm of the state is

$$
\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}=\tfrac14\bigl(1-\lvert\vec r\rvert^2\bigr),
$$

so every pure state is a **zero divisor**, while a mixed state is not. The Bloch ball is the state slice of the positive cone, and its boundary sphere is the intersection of that slice with the future light cone of the biquaternion norm. The positive cone of the sector and the causal cone of the interval therefore have one and the same boundary.

### The Action on the Material Sector

The sector acts on the material sector by **conjugation**,

$$
\tilde Q_-\longmapsto\tilde Q_+\tilde Q_-\tilde Q_+^{*},\qquad \tilde Q_+\in\mathbb{B}_{\Psi},\ \tilde Q_-\in\mathbb{B}_{\Phi}.
$$

The image is in $\mathbb{B}_{\Phi}$, because the star is an anti-automorphism and the two signs cancel. The action is linear in $\tilde Q_-$, it is a group action, and it preserves the biquaternion norm when the acting element has unit biquaternion norm, $\langle\tilde Q_+\rangle_{\natural}=1$. That condition is the condition of $SL(2,\mathbb{C})$; it is not the matrix-unitary condition $\tilde Q_+\tilde Q_+^{*}=e_t$, which defines $U(2)$ and preserves the trace of a state. A boost is Hermitian and has unit norm, but it is not matrix-unitary; a rotation is both.

The action is the algebraic form of **operators acting on states**: the material sector is the space of kinematic configurations, and the informational sector is the space of the things that act on them. The asymmetry is the content of the names, and it is what earns the sector the adjective *informational* or *operational*.

### The Four Forms and the Bracket Table

The four forms are real on $\mathbb{B}_{\Psi}$. With $\tilde Q_1=a_te_t+i\vec p$ and $\tilde Q_2=b_te_t+i\vec q$, they collapse in pairs. The two pairs are stated separately.

**The probability pair.** The Hermitian form and the plain form coincide on the sector,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle=a_tb_t+(\vec p,\vec q).
$$

This pair is positive definite of signature $(4,0)$. The Hermitian form is the probability pairing and is defined on the whole algebra; the plain form is its restriction to the sector and needs no matrix: $\mathrm{Sc}$ is the coefficient of $e_t$. Its diagonal is the plain norm, $\langle\tilde R_\Psi\rangle=\mathrm{Sc}(\tilde R_\Psi^2)=c^2r_t^2+\lvert\vec r_\Psi\rvert^2$, positive definite. The Born weight is always written with the star.

**The interval pair.** The quaternionic form and the Krein form coincide on the sector,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=a_tb_t-(\vec p,\vec q).
$$

This pair is indefinite of signature $(1,3)$: the interval. Its diagonal is the biquaternion norm $\langle\tilde R_\Psi\rangle_{\natural}=c^2r_t^2-\lvert\vec r_\Psi\rvert^2$. It is a different quadratic form from the diagonal of the plain form: the first is positive definite, the second indefinite, and neither normalises a state.

The reason for the collapse is the definition of the sector: the star is the identity on it, so the sesquilinear form equals the bilinear one in the second slot. The sector carries **no scalar area pairing**, because multiplication by $i$ carries $\mathbb{B}_{\Psi}$ out of itself, $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$; the imaginary parts of the four forms vanish identically.

The bracket table is uniform. On two elements of one sector the commutator lands in $\mathbb{B}_{\Phi}$ and the anticommutator in $\mathbb{B}_{\Psi}$; on two elements of different sectors the two are exchanged.

| Bracket | $\mathbb{B}_{\Psi},\mathbb{B}_{\Psi}$ | $\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | $\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}$ |
| --- | --- | --- | --- |
| commutator $[\tilde Q_1,\tilde Q_2]$ | $\mathbb{B}_{\Phi}$ | $\mathbb{B}_{\Psi}$ | $\mathbb{B}_{\Phi}$ |
| anticommutator $\{\tilde Q_1,\tilde Q_2\}$ | $\mathbb{B}_{\Psi}$ | $\mathbb{B}_{\Phi}$ | $\mathbb{B}_{\Psi}$ |

The commutator and the anticommutator therefore always land in opposite sectors. The anticommutator closes on $\mathbb{B}_{\Psi}$, which is a special Jordan algebra; the commutator does not close on it, and lands in the material sector. The square of an element of either sector lies in $\mathbb{B}_{\Psi}$, because $\{\tilde Q,\tilde Q\}=2\tilde Q^2$ and the two arguments then lie in one sector.

## Interpretations

### The Sector Is the Operator Space

The sector is the space of the operators of a two-state system, and its four families are carved out by conditions imposed on one element, not by four disjoint definitions.

| Family | Condition | Shape |
| --- | --- | --- |
| Observables | $\tilde R_\Psi\in\mathbb{B}_{\Psi}$ | the whole sector, real dimension four |
| Effects | $0\leq\tilde R_\Psi\leq e_t$, that is $\lvert c r_t-\tfrac12\rvert+\lvert\vec r_\Psi\rvert\leq\tfrac12$ | the operator interval |
| States | $\langle\tilde R_\Psi,e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$ and $\tilde R_\Psi\geq0$ | the Bloch ball, $\lvert\vec r_\Psi\rvert\leq\tfrac12$ |
| Pure states | $\langle\tilde R_\Psi,e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$ and $\langle\tilde R_\Psi\rangle_{\natural}=0$ | the Bloch sphere, $\lvert\vec r_\Psi\rvert=\tfrac12$ |

The nesting is strict: pure states are states, states are effects, and effects are observables. The roles are not exclusive, and the sector does not partition itself into states and observables. One and the same element can be read as a state, as an effect and as an observable, and the role is fixed by the conditions imposed on it.

Neither condition separates the families on its own. The normalisation alone does not: a Hermitian element with $\langle\tilde Q,e_t\rangle=\tfrac12$ whose spectrum straddles zero is not a state. The positivity alone does not: $2e_t$ is positive and is not a state. **Idempotency marks the boundary and nothing else**: among the Hermitian idempotents $0,e_t,\tilde\Pi_{1,2}(\vec u)$, exactly the last have $\langle\tilde\Pi,e_t\rangle_{*}=\tfrac12\langle e_t\rangle$, so the idempotency singles out the pure states within the state slice, and a general observable is not idempotent.

The separator the sector supplies is the quaternionic norm. On the state slice the positivity is $\lvert\vec r\rvert\leq1$, which is $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}\geq0$, so

$$
\text{states}=\{\tilde Q\in\mathbb{B}_{\Psi}:\langle\tilde Q,e_t\rangle=\tfrac12\langle e_t\rangle,\ \langle\tilde Q\rangle_{\natural}\geq0\},
$$

$$
\text{pure states}=\{\tilde Q\in\mathbb{B}_{\Psi}:\langle\tilde Q,e_t\rangle=\tfrac12\langle e_t\rangle,\ \langle\tilde Q\rangle_{\natural}=0\}.
$$

The state space and the causal cone therefore share their boundary in the state slice. The fact is the same one stated in the material article: the positive cone of the sector and the causal cone of the interval have one and the same boundary.

**The boundary.** The families are nested, not disjoint, and the words *state* and *observable* name roles, not types. The sector does not supply a measurement postulate; it supplies the algebraic shape that a measurement postulate takes.

### The State Space Is the Bloch Ball

The state slice of the sector is the family $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$ with $\vec r$ a real three-vector, normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$ (trace one in the $2\times2$ image). With $\vec r=r\vec u$ and $r=\lvert\vec r\rvert$, its spectral decomposition is a convex combination of two orthogonal pure states,

$$
\tilde{Ϛ}_{\Psi}=\frac{1+r}{2}\tilde\Pi_1(\vec u)+\frac{1-r}{2}\tilde\Pi_2(\vec u),
$$

with weights that sum to one. Positivity is exactly $\lvert\vec r\rvert\leq1$, so the state space is the unit ball of the vector part.

The geometry is the Bloch ball of a qubit. The boundary $\lvert\vec r\rvert=1$ is the two-sphere of pure states; the interior is the mixed states; the centre $\vec r=0$ is the maximally mixed state $\tfrac12e_t$. A state is pure exactly when it is idempotent, and the two notions coincide in the sector and nowhere else. The ball is three-dimensional, as the state space of a two-state system must be: the sector has real dimension four and the normalisation $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$ is one real equation.

Every pure state is a zero divisor, because $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}=\tfrac14(1-\lvert\vec r\rvert^2)$ vanishes on the sphere. A mixed state is not. The ball is the intersection of the affine hyperplane $\{\operatorname{Sc}=\tfrac12\}$ with the future light cone of the biquaternion norm, so its boundary is a slice of the causal cone. This is the structural link between probability and causality: the same quadratic form that gives the interval gives the positivity of the state.

**The boundary.** The ball is the state space of the frame, not a relativistic state space. A boost carries a state off the state slice, so the single-qubit ball is not invariant under the full Lorentz group. Making the state space itself relativistic is open work, not a result of this article.

### The Operator Defines the State

A state is not only an element given in advance; any nonzero operator produces one. The map is

$$
\tilde{Ϛ}_{\Psi,\tilde Q}=\frac{\tilde Q\tilde Q^{*}}{2\langle\tilde Q,\tilde Q\rangle_{*}},
\qquad
\langle\tilde Q,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})>0 ,
$$

and its image is Hermitian, positive and normalised by $\langle\tilde{Ϛ}_{\Psi,\tilde Q},e_t\rangle_{*}=\tfrac12$, hence a point of the Bloch ball. The Cartan amplitude $\tilde R_\Psi=\sqrt{\tilde Q\tilde Q^{*}}$ is the unnormalised square root of the image, and the eigenvalues of $\tilde R_\Psi$ are the singular values of $\tilde Q$.

Three properties fix the map. It is **right-invariant**, $(\tilde Q\tilde W)(\tilde Q\tilde W)^{*}=\tilde Q\tilde Q^{*}$ for $*$-unitary $\tilde W$, so the right $*$-unitary is a gauge fibre. It is **left-covariant**, $\tilde{Ϛ}_{\Psi,\tilde V\tilde Q}=\tilde V\tilde{Ϛ}_{\Psi,\tilde Q}\tilde V^{*}$, so a left $*$-unitary is a change of frame. And it is **stratified** by the rank of the operator:

| operator | singular values | image |
| --- | --- | --- |
| $*$-unitary up to scale | equal | maximally mixed |
| invertible, not $*$-unitary up to scale | distinct | mixed |
| rank one, a zero divisor | one vanishing | pure |

The direction is the one that is easy to get backwards: the reversible operators produce the least informative state, and the zero divisors produce the pure states. The reason is that the map keeps the ratios of the singular values and discards the $*$-unitary factor and the overall scale; a reversible operator has equal singular values, so its image carries no information beyond the normalisation.

**The boundary.** The map takes an operator to a state without an input. A measurement instrument takes an operator and an input state, $\tilde{Ϛ}_{\Psi}\mapsto\tilde M_{\mathrm{kraus}}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus}}^{*}/p$, and the two coincide only when the input is $\tfrac12e_t$. The operator-to-state map is therefore the input-free shadow of the instrument, not the instrument, and it neither selects an outcome nor supplies a dynamics. It is developed in *The General Polar Decomposition, the Amplitude and the Operator-to-State Map*.

### The Spectral Decomposition Is the Readout

Every Hermitian element is a real combination of two orthogonal idempotents,

$$
\tilde R_\Psi=\lambda_+\tilde\Pi_1(\vec u_\Psi)+\lambda_-\tilde\Pi_2(\vec u_\Psi),\qquad \lambda_\pm=c r_t\pm\lvert\vec r_\Psi\rvert,
$$

with $\tilde\Pi_1+\tilde\Pi_2=e_t$ and $\tilde\Pi_1\tilde\Pi_2=0$. The two coefficients are the eigenvalues, the two idempotents are the eigen-idempotents, and the pair is a resolution of the identity. The decomposition degenerates to $c r_t e_t$ exactly when $\vec r_\Psi=0$.

The scalar part and the biquaternion norm read

$$
2\,\mathrm{Sc}(\tilde R_\Psi)=\lambda_++\lambda_-,\qquad \langle\tilde R_\Psi\rangle_{\natural}=\lambda_+\lambda_-,
$$

the first of which is the trace in the $2\times2$ image. The trace is the sum of the eigenvalues and the biquaternion norm is their product, so that norm is indefinite: it is negative exactly when the two eigenvalues have opposite signs. This is the difference from the ordinary Hermitian matrix case, where the analogue of the norm is a sum of squares. **Positivity is a statement about the eigenvalues, not about the norm**, and the spectral decomposition is what makes the statement visible.

Read physically, the two eigenvalues are the two possible readings of the observable and the two idempotents are the two outcomes. The spectral decomposition is the algebraic form of a readout with two outcomes. The spectrum does not by itself give the frequencies of those outcomes; that is the role of the state and of the Born pairing.

**The boundary.** The spectrum is the set of possible readings, not the distribution of readings. The distribution requires a state, and the state is a separate element of the same sector.

**Normal is not automatic.** The readout above is the Hermitian case of the eigenvalue decomposition. For an element with distinct eigenvalues, the eigenprojections are Hermitian exactly when the element is normal, $\tilde R_\Psi\tilde R_\Psi^{*}=\tilde R_\Psi^{*}\tilde R_\Psi$. Otherwise the pair is still complete and $\tilde\Pi_+\tilde\Pi_-=0$, but the idempotents are not Hermitian, the left and right eigenbases differ, and the coefficients are read with a biorthogonal pairing rather than with the Born form. The probabilities of this article are therefore those of a normal observable, and the positivity statements do not extend to a general element without normality.

The two pairings are worth separating. The **orthogonal** pairing is the Born form $\langle\tilde\Pi_\pm,\tilde{Ϛ}_{\Psi}\rangle_{*}$: it uses the Hermitian eigenprojections of a normal element and the Hermitian state, and it is positive on the sector. The **biorthogonal** pairing uses the right and left eigenbases, $\ell_\pm^{\dagger}r_\pm=1$ and $\ell_+^{\dagger}r_-=0$, and the projectors $P_\pm=r_\pm\ell_\pm^{\dagger}$, which are not Hermitian in general; the weights are $\ell_\pm^{\dagger}\tilde{Ϛ}_{\Psi} r_\pm$, and they are not positive for every state. The two coincide exactly when the element is normal. The biorthogonal calculus, the Petermann factor and the exceptional-point limit are *Biorthogonal Quantum Mechanics and the Biquaternion Spectrum*.

### Evolution and Measurement Are One Sandwich

The action of an element $\tilde Q$ on the sector is the sandwich

$$
\Gamma_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

The same formula carries three physical regimes, distinguished only by the normalisation imposed on $\tilde Q$:

| Regime | Condition on $\tilde Q$ | Physical reading |
| --- | --- | --- |
| Lorentz rotor | $\langle\tilde Q\rangle_{\natural}=1$ | reversible change of frame on $\mathbb{B}_{\Phi}$ |
| Matrix-$*$-unitary | $\tilde Q\tilde Q^{*}=e_t$ | reversible evolution of states |
| Hermitian idempotent, $\tilde\Pi\neq0,e_t$ | $\tilde Q^2=\tilde Q$ and $\tilde Q^{*}=\tilde Q$ | irreversible measurement projection |

A unit-norm element is a Lorentz rotor: it preserves the interval and acts on the material sector. A matrix-unitary element preserves the trace and maps states to states; it is a rotation rotor up to a central phase, and its effective action on the Bloch ball is $SO(3)$. A proper Hermitian idempotent, neither $0$ nor $e_t$, does not preserve the norm, and its action is a projection: $\tilde{Ϛ}_{\Psi}\mapsto\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi$, with probability $2\operatorname{Sc}(\tilde\Pi\tilde{Ϛ}_{\Psi}^{*})$ and normalised post-measurement state $\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi/(2\operatorname{Sc}(\tilde\Pi\tilde{Ϛ}_{\Psi}^{*}))$.

The dichotomy between reversible and irreversible actions is therefore intrinsic to the sector: a norm-preserving rotor against a norm-destroying projection. On the material sector the rotor is a Lorentz transformation; on the state side the reversible class narrows to the matrix-unitary elements, and the pair is exactly the quantum-information dichotomy between $*$-unitary evolution and measurement.

**The boundary.** The sandwich is one operator; the three cases differ by the normalisation of the parameter, not by the operation. The projection is the algebraic form of a measurement, but the collapse is not derived from the algebra. The identification of the projection with a physical measurement is the interpretive step, and the probabilities it gives are the Born weights, not frequencies.

### The Born Rule Is the Normalised Hermitian Form

For a state $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec u)$ and an observable $\tilde R_\Psi=c r_t\,e_t+i\vec r_\Psi$, the state is normalised against the unit, $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, and the Born weight is

$$
\langle\tilde R_\Psi\rangle_{\tilde{Ϛ}_{\Psi},*}
=\frac{\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
=\frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}
=c r_t+\vec u\cdot\vec r_\Psi.
$$

The star is the Hermitian conjugation. It changes no number here, since $\tilde R_\Psi^{*}=\tilde R_\Psi$ and $\tilde{Ϛ}_{\Psi}^{*}=\tilde{Ϛ}_{\Psi}$ on $\mathbb{B}_{\Psi}$, but it is what makes the pairing positive definite on the whole algebra: $\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$, while the plain form is positive only on $\mathbb{B}_{\Psi}$ and negative on $\mathbb{B}_{\Phi}$. On the sector the two coincide, and the plain form is the restriction of the Hermitian form.

This is the standard spin-1/2 expectation value along the direction $\vec u$. For the two idempotents $\tilde\Pi_{1,2}(\vec u)$ and a general state $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$, the same pairing gives

$$
p_\pm=\frac{\langle\tilde\Pi_{1,2}(\vec u),\tilde{Ϛ}_{\Psi}\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
=\frac{\mathrm{Sc}(\tilde\Pi_{1,2}(\vec u)\tilde{Ϛ}_{\Psi}^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}
=\tfrac12\bigl(1\pm\vec u\cdot\vec r\bigr),
$$

the probability formula of the Born rule. For a general effect $0\le\tilde E_{\Psi}\le e_t$ the same reading gives $p=\mathrm{Sc}(\tilde E_{\Psi}\tilde{Ϛ}_{\Psi}^{*})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})\in[0,1]$, non-negative because the form is positive definite and the effect is positive.

The framework relocates the Born rule from a postulate to a property of the pairing: the probability is the normalised Hermitian form of a state and an effect. On $\mathbb{B}_{\Psi}$ the star is inert, so the same number is $\mathrm{Sc}(\tilde E_{\Psi}\tilde{Ϛ}_{\Psi})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})$, the plain scalar. Normalisation is the only place where the trace enters: in the $2\times2$ image $\operatorname{Tr}(e_t)=2$, so $\operatorname{Tr}(\tilde{Ϛ}_{\Psi})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=1$ and $p=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde E_{\Psi}^{*})/\operatorname{Tr}(\tilde{Ϛ}_{\Psi})=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde E_{\Psi})/\operatorname{Tr}(\tilde{Ϛ}_{\Psi})$, the star being inert on $\mathbb{B}_{\Psi}$ and the unstarred trace real and non-negative for a state and an effect, so $p\in[0,1]$. What the formula does not give is the identification of those numbers with physical frequencies. The interpretive step remains, and the article that derives the rule and compares it with the postulate states the separation.

**The boundary.** The formula gives probabilities, not frequencies. The identification of probability with long-run frequency is not a result of the algebra, and the Born rule is derived in the structural sense, not in the operational sense.

### The Sector Acts on the Material Sector

The sector is the space of the things that act, and the material sector is the space of the things acted upon. The action is the sandwich $\tilde Q_-\mapsto\tilde Q_+\tilde Q_-\tilde Q_+^{*}$, and it preserves the material sector and, for a unit-norm parameter, the interval. A boost is a Hermitian element of $\mathbb{B}_{\Psi}$: it acts on a four-vector and changes its frame. A rotation is a real quaternion, which lies in the real sector $\mathbb{B}_{H}$ rather than in $\mathbb{B}_{\Psi}$, and its action on $\mathbb{B}_{\Phi}$ is still a rotor conjugation. The general Lorentz rotor is a general unit-norm biquaternion, outside both sectors.

The asymmetry is the physical content of the names. The material element is a configuration; the informational element is an operator on configurations. The operator can be a change of frame, a rotation, or a measurement projection; the configuration cannot act on the operator in the same way. The action is established algebra; the interpretation of $\mathbb{B}_{\Psi}$ as a distinct physical sector is the hypothesis.

**The boundary.** The word *informational* names the role of the sector in the action, not a claim that the sector has been observed. The action is exact; the physical realisation is open.

### The Bracket Makes It a Jordan Algebra

The anticommutator of two Hermitian elements is Hermitian, so $\mathbb{B}_{\Psi}$ is closed under the symmetrised product $\tfrac12\{\tilde Q_1,\tilde Q_2\}$. It is a **special Jordan algebra**. The commutator does not close on the sector: it lands in $\mathbb{B}_{\Phi}$, and it is the Lie algebra of the material sector. The two sectors therefore carry two different algebraic structures: the material sector is a Lie algebra, and the informational sector is a Jordan algebra.

The asymmetry is structural and not interpretive. The material sector carries the compact rotation generators together with the central phase, and a Lie algebra is what a space of generators carries. The three boost generators lie in $\mathbb{B}_{\Psi}$, among the observables. The informational sector is the space of observables, and a Jordan algebra is what a space of observables carries: the symmetrised product is the algebraic form of the simultaneous measurement of two observables, and it is commutative but not associative. The square of an element lies in $\mathbb{B}_{\Psi}$ in both cases, because the square is the symmetrised product of an element with itself.

**The boundary.** The bracket is not the physical composition of observables. The Jordan product is the symmetrised part of the algebra product, and the Lie product is the antisymmetrised part; the two are the two halves of one multiplication, and they land in opposite sectors.

### The Correspondence with Quantum Information

The mathematics of the sector and its action on the material sector is structurally identical to the mathematics of a single qubit. The table records the dictionary.

| Quantum information | Biquaternion framework |
| --- | --- |
| State space $\mathbb{C}^2$ | spinor module $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_2\}$ |
| Density matrix $\rho$ (Hermitian, positive, trace one) | element $\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$ (Hermitian, positive, normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$; trace one in the image) |
| Pure state $\lvert\tilde{Ξ}_{\mathrm{sp}}\rangle_{*}\langle\tilde{Ξ}_{\mathrm{sp}}\rvert$ | idempotent $\tfrac12(e_t+i\vec u)$ |
| Observable (Hermitian operator) | Hermitian element $\tilde R_\Psi\in\mathbb{B}_{\Psi}$ |
| $*$-Unitary gate $U$ | matrix-unitary $\tilde Q$, $\tilde Q\tilde Q^{*}=e_t$: a rotation rotor up to a central phase, with effective action $SO(3)$ on the Bloch ball |
| Expectation value $\operatorname{Tr}(\rho H)$ | $\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$, read as $2\operatorname{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})$; the trace enters only at normalisation |
| Reversible evolution $U\rho U^{\dagger}$ | rotor conjugation $\tilde U\tilde{Ϛ}_{\Psi}\tilde U^{*}$ |
| Projective measurement $\rho\mapsto P\rho P$ | Hermitian idempotent projection $\tilde{Ϛ}_{\Psi}\mapsto\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi$ |

The basis of the module is one idempotent and one nilpotent: $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ and $\vec\Upsilon_2=\tfrac12(i\vec e_x+\vec e_y)$, with $\tilde\Pi_+^2=\tilde\Pi_+$, $\vec\Upsilon_2^2=0$ and Gram matrix $\tfrac12 I_2$. A general spinor is $s_1\tilde\Pi_++s_2\vec\Upsilon_2$ with complex coefficients; the two states are carried by the coefficients, not by the two basis elements. The module is a genuine Hilbert space, with $\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}_{\mathrm{sp}}\rangle_{*}=\tfrac12(\lvert s_1\rvert^2+\lvert s_2\rvert^2)$ positive definite.

**What the correspondence is.** A structural fact about the algebra. The Hermitian elements are operators on the spinor module, and the algebra they generate is the algebra of observables of a two-state system.

**What it is not.** A physical theory. It does not establish that $\mathbb{B}_{\Psi}$ is an informational sector of nature. It establishes that if the sector were given an informational interpretation, the mathematics would be available. Whether the interpretation is realised is the hypothesis.

**The boundary.** The correspondence is exact; the physical realisation is the hypothesis. The state space is the fixed Bloch ball, and a boost carries a state off the state slice.

### The Spin Analogy and Its Relativistic Extension

The sector carries the algebra of observables of a spin-1/2 system, and the biquaternion algebra widens the carrier without changing the state space. In non-relativistic spin-1/2 physics the state space is $\mathbb{C}^2$, the observables are the Hermitian $2\times2$ matrices, and the group that preserves the state space is the compact $U(2)$. In the biquaternion framework the state space is the spinor module of $\mathbb{B}$, the observables are the Hermitian elements of $\mathbb{B}_{\Psi}$, and the group that preserves the state slice is again $U(2)$.

The Lorentz group enters through the generators, and they are split between the sectors. The three rotation generators are the real vector units $\vec e_k\in\mathbb{B}_{\Phi}$, anti-Hermitian and compact. The three boost generators are the traceless Hermitian elements $i\vec r_\Psi\in\mathbb{B}_{\Psi}$, non-compact. The two triples generate $SL(2,\mathbb{C})$, which acts on the material sector and on the ambient algebra but not on the Bloch ball: a boost carries a state off the state slice. The central direction $i e_t$ generates the $\mathfrak{u}(1)$ phase and is not part of the Lorentz algebra. The compact/non-compact distinction is the distinction between rotations in a spacelike plane and boosts in a timelike plane.

The framework can therefore be read as a relativistic generalisation of the spin-1/2 formalism at the level of the algebra: the observables of $\mathbb{B}_{\Psi}$ include the boost generators alongside the central scalar, the rotation generators lie in the material sector, and the Lorentz group is generated by the rotations of $\mathbb{B}_{\Phi}$ and the boosts of $\mathbb{B}_{\Psi}$. The state space itself remains the non-relativistic Bloch ball.

**The boundary.** The single-qubit state space is a fixed Bloch ball, and a boost carries a state off the state slice. Making the state space itself relativistic is open work, not a result of the framework. The analogy is exact at the level of the algebra of one qubit; it is not a derivation of the relativistic state space.

### The Sector Is Phase-Free but Carries Coherence

The sector carries no scalar area pairing: the imaginary parts of the four forms vanish, because $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$ and no conjugate pair lies inside the sector. But the sector does carry phase information, and it sits in a different part of the same block. The **vector-valued** antisymmetric half of the sesquilinear product is not zero on the sector. At $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$,

$$
\operatorname{Vect}\bigl(\tilde{Ϛ}_{\Psi}\tilde{Ϛ}_{\Psi}^{*}\bigr)=\operatorname{Vect}\bigl(\tilde{Ϛ}_{\Psi}^2\bigr)=\tfrac12 i\vec r,
$$

the Bloch vector, up to the central factor. The vector part is the **coherence** and the interference term of the state.

The two statements are complementary, not opposed. On the informational sector the relative-phase content of a pairing sits in the vector part of the product, while the imaginary part of the scalar form is zero. The sector carries phase information and carries no area, and the two are carried by different parts of the same block.

**The boundary.** The scalar-valued alternating part of the form and the vector-valued antisymmetric half of the product are different objects. The first vanishes on the sector; the second does not. A sector without an area pairing is not a sector without an antisymmetric structure.

### The Sesqualgebra Behind the Reading

Eight statements of this article are not properties of the vector space $\mathbb{B}_{\Psi}$ alone. Each names a product, a form or an involution of the sesqualgebra structure on $\mathbb{B}$, and each has a mathematical owner.

| Statement | Algebraic address | Owner |
| --- | --- | --- |
| The Born pairing is the Hilbert–Schmidt pairing | $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_2)^{\dagger}\mathsf{M}_2(\tilde Q_1)\bigr)$ | [$M_2(\mathbb{C})$ Representation : The General Plain Sesqualgebra of Biquaternions](../articles_maths/m2c-representation-the-general-plain-sesqualgebra-of-biquaternions.html) |
| The form makes $\mathbb{B}$ a Hilbert space | $\operatorname{Sc}(\tilde Q_1^{*}\tilde Q_2)$ is positive definite of signature $(8,0)$ | [The Completion of a Sesqualgebra with a Form](../articles_maths/the-completion-of-a-sesqualgebra-with-a-form.html) |
| The level sets are the groups the physics uses | $\tilde U\tilde U^{*}=e_t$ gives $U(2)$; $\langle\tilde U\rangle_{\natural}=1$ gives $SL(2,\mathbb{C})$; the Euclidean sphere is not used | [Unitary Operators of a Sesqualgebra](../articles_maths/the-unitary-operators-of-a-sesqualgebra.html), [N-Regularity and N-Degeneracy in the Biquaternion Algebra, §The Group of Units](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| The operator dictionary is the adjointness dictionary | observables $\mathbb{B}_{\Psi}$, generators $\mathbb{B}_{\Phi}$, unitaries $U(2)$; $\tilde R_\Psi=iA$ for $A\in\mathbb{B}_{\Phi}$ | [$M_2(\mathbb{C})$ Representation : The General Plain Sesqualgebra of Biquaternions](../articles_maths/m2c-representation-the-general-plain-sesqualgebra-of-biquaternions.html) |
| One operator carries both evolutions | $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$, evaluated at a $*$-unitary or an idempotent parameter | [Two-Sided Operators on the General Plain Sesqualgebra](../articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra.html) |
| Projections come from one sector only | no non-zero idempotent lies in $\mathbb{B}_{\Phi}$ | [Idempotents](../articles_maths/idempotents.html), [Ideals and the Peirce Decomposition](../articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-sesqualgebra.html) |
| Two pairings, because one is not Hermitian | interval $\langle\cdot,\cdot\rangle_{\natural}$, probability $\langle\cdot,\cdot\rangle_{*}$; on $\mathbb{B}_{\Phi}$ they coincide on the space part and differ in the sign of the time part, on $\mathbb{B}_{\Psi}$ they coincide on the time part and differ in the sign of the space part | [Hermitian Forms over Algebras and Norms](../articles_maths/hermitian-forms-over-algebras-and-norms.html), [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| No alternating companion on the sector | the four forms are real on $\mathbb{B}_{\Psi}$, so their imaginary parts vanish | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |

The table is the algebraic address book of the interpretation. Each physical statement has a mathematical owner, and the interpretation adds no theorem to the list.

### The Hypothesis and Its Open Questions

The **hypothesis** is that the Hermitian subspace is physically realised as a distinct sector, the arena of operations and information, in the same sense in which the anti-Hermitian subspace is the arena of events and four-vectors.

**What it claims.** The mathematics of $\mathbb{B}_{\Psi}$ is structurally identical to the mathematics of a two-state quantum system. Its elements act as operators on the spinor module. The reversible/irreversible dichotomy is the $*$-unitary/measurement dichotomy. The Born pairing is the normalised Hermitian form; in the $2\times2$ image, the trace formula.

**What it does not claim.** That the sector has been observed. That it has a specified dynamics beyond the quantum formalism. That there is a specified coupling to the material sector beyond the Lorentz action. That it makes an empirical prediction distinguishing it from standard physics. That its imaginary directions are extra spatial dimensions.

**The honest position.** The mathematics is established; the physical interpretation is a research programme, not a theory. The material sector reproduces the four-vectors of relativistic physics, and the observables of $\mathbb{B}_{\Psi}$ generate the operator algebra of a qubit. Whether the sector is a distinct physical sector, or only a mathematical structure that describes a qubit, is open.

The open questions are concrete.

1. **Physical reality.** Is $\mathbb{B}_{\Psi}$ realised as a distinct sector, or is it only the kinematics of a qubit? A realisation would require a coupling with observable consequences.
2. **Dynamics.** Does the sector have its own dynamics, with $\mathbb{B}_{\Psi}$-valued fields and wave equations? The operators $\tilde\nabla$, $\tilde\nabla^{\natural}$ and $\Box$ are available, but which one governs the sector is not fixed.
3. **Coupling.** Beyond the Lorentz action, is there a new coupling between the two sectors?
4. **Entropy.** Does the framework admit an entropy functional on the states, for example $S(\tilde{Ϛ}_{\Psi})=-2\operatorname{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$? The logarithm is multivalued, and the proposal needs verification.
5. **Non-Hermitian idempotents.** The idempotents built on the roots of $-1$ lie outside $\mathbb{B}_{\Psi}$. Are they virtual states, or do they have a physical meaning?
6. **Quantum field theory.** How does the framework connect to QFT, entanglement and the continuum?
7. **Empirical contact.** What quantitative prediction distinguishes the hypothesis from standard physics? Without one, it remains a mathematical interpretation.
8. **Imaginary directions.** In what sense are the imaginary directions informational rather than spatial? The Fourier reading answers partially: an imaginary direction is a direction the pairing uses, along which the conjugate variable is paired, not a direction in which anything propagates.

## Examples

**The boost biquaternion.** $\tilde U_{\Psi,\mathrm b}=\cosh(\theta_{\mathrm{rpd}}/2)+i\sinh(\theta_{\mathrm{rpd}}/2)\vec u_{\mathrm b}$ is Hermitian, has unit norm, and lies in $\mathbb{B}_{\Psi}$. It acts on $\mathbb{B}_{\Phi}$ by rotor conjugation and implements a Lorentz boost. It is not matrix-unitary, and it does not preserve the normalisation $\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=\tfrac12$ (the trace of a state); it is an operator on four-vectors, not an evolution of states.

**A pure state.** $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ is Hermitian, idempotent, with $2\,\mathrm{Sc}(\tilde\Pi_+)=1$ (trace one), and a zero divisor. It is the pure state along $+z$, the Bloch vector $\vec r=\vec e_z$, and the north pole of the Bloch sphere. The orthogonal idempotent $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ is the south pole.

**A mixed state.** $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+\tfrac12 i\vec e_z)$ has $\lvert\vec r\rvert=\tfrac12$, so it is positive and mixed, with $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}=\tfrac{3}{16}>0$. It is not a zero divisor. At $\vec r=0$ the state is $\tfrac12e_t$, the maximally mixed state.

**An observable.** $\tilde R_\Psi=c r_t\,e_t+i\vec r_\Psi$ has eigenvalues $c r_t\pm\lvert\vec r_\Psi\rvert$ and spectral decomposition $\tilde R_\Psi=\lambda_+\tilde\Pi_1(\vec u_\Psi)+\lambda_-\tilde\Pi_2(\vec u_\Psi)$. For $c r_t=1$ and $\lvert\vec r_\Psi\rvert=\tfrac12$ the readings are $\tfrac32$ and $\tfrac12$; for $\lvert\vec r_\Psi\rvert=2$ they are $3$ and $-1$, and the element is not positive.

**The identity.** $e_t$ is Hermitian, idempotent, and has scalar part one, which the $2\times2$ reading calls trace two. It is the identity operator, not a state: its scalar part is one, and a state has scalar part $\tfrac12$ (trace one).

**The Hermitian form.** For any $\tilde Q\in\mathbb{B}$, the product $\tilde Q\tilde Q^{*}$ is Hermitian and lies in $\mathbb{B}_{\Psi}$. Its scalar part is the Euclidean norm squared $\sum_\mu\lvert Q_\mu\rvert^2$, which is non-negative; it is the natural weight of the element.

| Object | Structure | Role |
| --- | --- | --- |
| $e_t$ | real scalar, $\mathrm{Sc}(e_t)=1$ (trace two) | identity operator |
| $\tilde U_{\Psi,\mathrm b}$ | Hermitian, unit norm | Lorentz boost rotor |
| $\tilde\Pi_{1,2}(\vec u)$ | Hermitian, idempotent, $\mathrm{Sc}=\tfrac12$ (trace one) | pure state |
| $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$, $\lvert\vec r\rvert\leq1$ | Hermitian, positive, $\mathrm{Sc}=\tfrac12$ (trace one) | mixed state |
| $\tilde R_\Psi=c r_t\,e_t+i\vec r_\Psi$ | Hermitian, eigenvalues $c r_t\pm\lvert\vec r_\Psi\rvert$ | observable |
| $\tilde Q\tilde Q^{*}$ | Hermitian, positive scalar part | weight of an element |

## Limits

The article establishes the algebra of the sector and its interpretation as a two-state system. It does not establish that the sector is a distinct sector of the physical world, and it does not supply a dynamics, a coupling or an empirical prediction. The Born rule is derived as a property of the pairing, not as a frequency. The Bloch ball is the state space of the frame, not a relativistic state space. The identification of the projection with a physical measurement is the interpretive step, and the collapse is not derived. The sector's time is the real coordinate $c r_t$, not the material time $i c r'_t$.

## Summary

- The informational sector is the Hermitian subspace $\mathbb{B}_{\Psi}$, with a real time and an imaginary space, $\tilde R_\Psi=c r_t\,e_t+i(r'_{x}\vec e_x+r'_{y}\vec e_y+r'_{z}\vec e_z)$.
- Its biquaternion norm is indefinite of signature $(1,3)$; positivity is a condition on the eigenvalues, not on the biquaternion norm.
- The Hermitian idempotents $\tfrac12(e_t\pm i\vec u)$ are the pure states; they are the halvings of the roots of $+1$ and are zero divisors.
- The state slice (normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_*=\tfrac12$; trace one in the $2\times2$ image) is the Bloch ball $\lvert\vec r\rvert\leq1$; its boundary is the Bloch sphere, its centre the maximally mixed state.
- The Bloch ball is the state slice of the future light cone of the biquaternion norm; probability and causality share their boundary.
- The spectral decomposition writes every observable as two eigenvalues times two orthogonal idempotents.
- Evolution and measurement are one sandwich, with the parameter unit-norm, matrix-unitary or idempotent.
- The Born rule is the normalised Hermitian form $\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$, read in the $2\times2$ image as $\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)=2\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}=2\operatorname{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})$, with $p_\pm=\tfrac12(1\pm\vec u\cdot\vec r)$.
- The sector is a special Jordan algebra under the anticommutator, and not a Lie algebra; the material sector carries the compact Lie algebra $\mathfrak{u}(2)$, the spatial rotations together with the central phase.
- The sector is phase-free in the scalar sense, but its vector product carries the coherence.
- The physical realisation of the sector is a hypothesis, with eight open questions.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}_{\Psi}$ | the Hermitian subspace, the informational sector |
| $\tilde R_\Psi=c r_t e_t+i\vec r_\Psi$ | an informational element, the Hermitian part |
| $\tilde\Pi_{1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$ | the pure-state idempotents |
| $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$ | a state when $\lvert\vec r\rvert\leq1$, normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$; the Bloch vector $\vec r$ |
| $\tilde R_\Psi=c r_t\,e_t+i\vec r_\Psi$ | an observable, with eigenvalues $c r_t\pm\lvert\vec r_\Psi\rvert$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, $\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}$ | the Hermitian form and its norm, positive definite on $\mathbb{B}$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$ | the plain form and its norm, the restriction of the Hermitian form to $\mathbb{B}_{\Psi}$ |
| $\langle\tilde R_\Psi\rangle_{\natural}=c^2r_t^2-\lvert\vec r_\Psi\rvert^2$ | the quaternionic norm, of signature $(1,3)$ |
| $\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*})=2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*})$, $\operatorname{Tr}(\tilde Q)=2\operatorname{Sc}(\tilde Q)$ | the trace, the $2\times2$ reading of the Hermitian form |
| $\Gamma_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the sandwich |
| $\tilde Q\tilde Q^{*}=e_t$ | the matrix-unitary condition, $U(2)$ |
| $\langle\tilde U\rangle_{\natural}=1$ | the unit-norm condition, $SL(2,\mathbb{C})$ |
| $p_\pm=\langle\tilde\Pi_{1,2}(\vec u),\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12(1\pm\vec u\cdot\vec r)$ | the Born probability |

## Further Reading

- [Subspaces and Decompositions](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the definition and the basis of $\mathbb{B}_{\Psi}$.
- [Idempotents](../articles_maths/idempotents.html), for the idempotents and the roots of $+1$.
- [The Squares and the Positive Cone of the Biquaternion Sesqualgebra](../articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.html), for the positive cone and the spectral decomposition.
- [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition, the normality criterion and the non-normal pair.
- [Biorthogonal Quantum Mechanics and the Biquaternion Spectrum](biorthogonal-quantum-mechanics-and-the-biquaternion-spectrum.html), for the biorthogonal pairing and its difference from the Born form.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) and [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the forms and the absence of the area pairing.
- [Two-Sided Operators on the General Plain Sesqualgebra](../articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra.html), for the sandwich.
- [Unitary Operators of a Sesqualgebra](../articles_maths/the-unitary-operators-of-a-sesqualgebra.html), for the matrix-unitary slice.
- [Jordan Algebras of Sesqualgebras](../articles_maths/jordan-algebras-of-sesqualgebras.html), for the symmetrised product.
- [$M_2(\mathbb{C})$ Representation : The General Plain Sesqualgebra of Biquaternions](../articles_maths/m2c-representation-the-general-plain-sesqualgebra-of-biquaternions.html), for the Hilbert–Schmidt pairing and the matrix trace.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the partner sector and the action on it.
- [The Born Rule from the Hermitian Form — Derivation and Comparison](the-born-rule-from-the-hermitian-form-derivation-and-comparison.html), for the derivation of the probability formula and its comparison with the postulate.
- [The Bloch Ball as the Normalised Slice of the Future Light Cone](the-bloch-ball-as-the-normalised-slice-of-the-future-light-cone.html), for the geometry of the state space.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the full correspondence with quantum information.
- [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](the-general-polar-decomposition-the-amplitude-and-the-operator-to-state-map.html), for the operator-to-state map and its purity stratigraphy.
