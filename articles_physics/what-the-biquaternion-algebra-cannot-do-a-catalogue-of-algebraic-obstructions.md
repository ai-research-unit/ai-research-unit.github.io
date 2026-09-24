# __What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ supplies the state space, the norm form, the trace pairing, the unitarity group and the centre that the preceding articles of this subcategory have put to work. It is equally important to record what it does **not** supply. This article is a catalogue of the algebraic obstructions: statements of the form "there is no element, subalgebra, or operation of $\mathbb{B}$ with such-and-such a property", each proved from the algebra's structure, each with its consequence for the framework and its minimal remedy.

The catalogue is not a list of defects of the framework. It is the map of the boundary at which the algebra's own resources end and something else must take over — an extended module, an imported statistical metric, an explicitly chosen basis, or a physical posit. A structural theory is only as honest as its account of its own limits, and the companion article *Fundamental and Derived Elements in the Biquaternion Framework* already distinguishes the algebra's fundamental content from what is derived. The present catalogue makes that distinction exhaustive for the structural questions.

**The obstructions, in summary.** They fall into six groups, and the grouping is itself informative.

*Commutativity and the centre.* The algebra is not commutative; its centre is the two-real-dimensional $\mathbb{C}e_0$; it has no non-trivial central idempotents; and its centre acts trivially on the pure states. The consequences are that the framework has no canonical classical bit, no intrinsic superselection structure, no observable global phase, and no internal determination of its own parameters.

*The two quadratic forms.* The Hermitian form is positive definite but trace-relative; the norm form is canonical but indefinite and vanishes on non-zero elements; neither alone can serve as the probability norm. The consequence is that the framework needs two forms, and that the statistically distinguished metric of mixed states cannot be read from either.

*Finite dimension and zero divisors.* The algebra is isomorphic to $M_2(\mathbb{C})$, so it has zero divisors, is not a division algebra, and describes a single qubit's worth of algebraic structure; tensor products and canonical commutation relations take one outside it, and a unit that preserves the norm for every Hermitian generator is forced into the centre. The consequences concern composite systems, field theory, and any genuinely infinite-dimensional structure.

*The sector structure.* The split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is a grading of the Lie algebra but not of the associative algebra; the Hermitian sector $\mathbb{M}_+$ is not a subalgebra and carries no intrinsic complex structure. The consequence is that material and informational sectors cannot be treated as independent algebras.

*The module action.* Every operation the algebra supplies is a multiplication, and a multiplication acts on the two chiral components of a Dirac module with the same matrix. The consequence is that the framework's apparatus is vector-like by construction, that the chiral gauge structure, the discrete operations and the energy-sign split have no multiplicative representative, and that the vector-like obstruction is a fact about the algebra rather than about any chosen gauge group.

*Dynamics and interpretation.* The algebra contains no time, no Hamiltonian, no preferred basis, and no value for its own central parameters. The consequences are that the dynamics is external input, that the measurement problem is untouched by the algebra, and that a norm-preserving quantum theory over $\mathbb{B}$ is a complex two-level theory in disguise.

Each item below is given in the form **statement — proof — consequence — remedy**, and each is verified either by explicit computation or by a standard theorem cited as standard.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$, and central $i$, $i^2=-1$. Conjugations are $\bar{\cdot}$ (quaternion), ${}^{*}$ (complex), $\dagger=\bar{\cdot}\circ{}^{*}$ (Hermitian), with $\flat=-\dagger$. The subspaces are $\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ and $\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$. The trace is $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$, $\mathrm{Tr}(e_0)=2$; the norm form is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$; the Hermitian form is $\langle\tilde{X},\tilde{Y}\rangle_\dagger=\mathrm{Tr}(\tilde{X}^\dagger\tilde{Y})$. The matrix model is the $\mathbb{C}$-linear representation $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, with $\Phi(\mathbb{B})=M_2(\mathbb{C})$ and $\det M(\tilde{Q})=N(\tilde{Q})$. States are $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ with $|\mathbf{r}|\leq1$; pure states are $\tilde{P}(\hat{\mu})=\tfrac12(e_0+i\hat{\mu})$; the state module is the minimal left ideal $\mathbb{B}p$ with $p=\tfrac12(e_0+ie_3)$.

## How an Obstruction Is Certified

An item enters this catalogue only if it satisfies three conditions, and the conditions are worth stating so that the reader can tell a genuine no-go statement from a limitation of effort.

**1. The statement is purely algebraic.** It says that no element, subspace, or operation of $\mathbb{B}$ has a stated property. Statements about what a human has not yet computed, or about what a particular representation does not exhibit, do not qualify; the obstruction must be a property of the algebra itself.

**2. The proof is from the algebra's defining relations.** The relations are $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$, and the centrality of $i$. Every proof below uses these, together with standard facts about finite-dimensional matrix algebras — transitivity of $U(2)$ on the rank-one projections, the tensor-dimension count, the innerness of the derivations of a central simple algebra, cyclicity of the trace, and the Bures/Fisher metric — each of which is identified as standard at the point where it is used.

**3. The consequence and the remedy are both stated.** An obstruction without a consequence is idle, and an obstruction without a remedy is a counsel of despair. Each item therefore names what must be adjoined, chosen, or imported for the framework to proceed: a maximal commutative subalgebra, an extension to modules and function algebras, a statistical metric, or a physical posit.

The catalogue is deliberately non-relativistic and structural. Obstructions that belong to the spin-specific articles — the absence of a spin-1 analogue of the quaternion triple, for instance — and obstructions that belong to the informational articles — no-cloning, the absence of a universal NOT — are not repeated here. Where an obstruction is a standard theorem about matrix algebras rather than a peculiarity of $\mathbb{B}$, it is cited as standard.

## I. Obstructions of Commutativity and the Center

### O1. There is no canonical maximal commutative subalgebra

**Statement.** There is no maximal commutative subalgebra $\mathbb{A}\subset\mathbb{B}$ that is invariant under the full symmetry group of the algebra. Equivalently, no classical bit is singled out by the algebra's own structure.

**Proof.** The maximal commutative subalgebras are the $\mathbb{A}_{\hat{n}}=\mathrm{span}_\mathbb{C}\{\tilde{P}(\hat{n}),e_0-\tilde{P}(\hat{n})\}$ for unit $\hat{n}\in\mathbb{R}^3$; the family is parametrized by $\mathbb{RP}^2$ and is permuted transitively by the adjoint action of $U(2)$. A subalgebra invariant under all of $U(2)$ would have to be fixed by a transitive group action on a space with more than one point, which is impossible. The only commutative subalgebra invariant under the whole adjoint action is the centre, which is not maximal. $\square$

**Consequence.** The framework has no preferred pointer basis and no canonical classical bit. Every classical reading of the algebra requires a choice of axis, and the choice is not derivable from the algebra.

**Remedy.** Choose a context, i.e. a Hermitian observable, and work in its centralizer. The companion articles *The Quantum–Classical Divide in the Biquaternion Framework* and *The Measurement Problem in Algebraic Form* take this route; the choice is a physical posit and remains external to the algebra.

### O2. There are no non-trivial central idempotents

**Statement.** The only idempotents in the centre $Z(\mathbb{B})=\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ are $0$ and $e_0$. Consequently $\mathbb{B}$ has no non-trivial two-sided ideals and no superselection sectors.

**Proof.** A central idempotent is $\tilde{C}=c\,e_0$ with $c\in\mathbb{C}$ and
$$
\tilde{C}^2=\tilde{C}\iff c^2=c\iff c\in\{0,1\},
$$
so the solutions are exactly $0$ and $e_0$. The corresponding two-sided ideals $\mathbb{B}\tilde{C}$ are $0$ and $\mathbb{B}$. The statement that a non-zero element generates the whole algebra, $\mathbb{B}\tilde{X}\mathbb{B}=\mathbb{B}$ for $\tilde{X}\neq0$, is the standard statement that $M_2(\mathbb{C})$ is simple, transported by the isomorphism $\Phi$. $\square$

**Consequence.** The framework cannot split itself into non-interfering branches labelled by central projections. Superposition across any two subspaces of the state module remains coherent unless coherence is destroyed by an external mechanism; the algebra provides no internal superselection rule.

**Remedy.** Adjoin a label algebra, or work on an enlarged algebra $\mathbb{B}\bar{\otimes}\mathbb{A}$ whose centre is larger; alternatively realise the labels on modules and states rather than in the algebra. An obstruction of this kind is a statement about $\mathbb{B}$ and not about the framework's ability to *describe* superselection once a label algebra is supplied.

### O3. The center acts trivially on the state space

**Statement.** The kernel of the action of the invertible group $\mathbb{B}^\times$ on the projective state space is the centre, $\mathbb{C}^\times e_0$. Hence no central data is observable at the level of states.

**Proof.** A central element acts on the module by scalar multiplication, $\tilde{C}\psi=\lambda\psi$, so it fixes every ray. Conversely, if $\tilde{U}$ fixes every ray then for each $\psi$ there is $\lambda(\psi)\in\mathbb{C}$ with $\tilde{U}\psi=\lambda(\psi)\psi$; linearity forces $\lambda$ to be constant and $\tilde{U}$ to be a scalar, hence central. $\square$

**Consequence.** The global phase and the overall scale of the state carry no information in this framework. The relevant symmetry group on states is the projective group $PGL(2,\mathbb{C})$, or $SO(3)$ on the Bloch sphere after restriction to unitaries, and the centre is not represented.

**Remedy.** None is needed, and none is possible: the unobservability of the global phase is a physical requirement, not a defect, and the companion article *The Bloch Ball as the Trace-One Slice of the Future Light Cone* uses exactly this fact when it identifies states with rays. The obstruction is recorded to make precise *why* the phase is unobservable: it is central.

### O4. The algebra cannot determine its own parameters

**Statement.** No operation of $\mathbb{B}$ fixes the numerical values of the parameters — $\hbar$, masses, couplings — that appear as central elements in the framework's equations. The centre is the store of these parameters, not their source.

**Proof.** The centre is $\mathbb{C}e_0$, and every central element commutes with every element of the algebra. A relation internal to the algebra can therefore only constrain central elements by algebraic equations such as $\tilde{C}^2=\tilde{C}$ (whose solutions are $0$ and $e_0$), never by a numerical condition selecting one real multiple over another. Any equation that determines a parameter must involve data external to the algebra. $\square$

**Consequence.** Dimensional analysis and renormalization aside, the framework cannot predict the spectrum of its own parameters from its structure; the mass coefficient $m e_0$, for example, is an input.

**Remedy.** Import the parameters as physical data, or embed the algebra in a larger structure whose relations fix them. The catalogue records the limit so that the framework is not credited with a derivation it does not perform.

## II. Obstructions of the Quadratic Forms

### O5. The norm form is not positive definite

**Statement.** Neither the norm form nor its negative is positive definite on the Hermitian subspace $\mathbb{M}_+$, and on the full algebra the form is complex-valued, so definiteness is not defined there at all. The norm form is therefore not a norm and cannot be used to define probabilities.

**Proof.** On $\mathbb{M}_+$ the norm form is $N(h_0e_0+i\mathbf{h})=(h_0^2-|\mathbf{h}|^2)e_0$, of signature $(1,3)$; on the algebra it is $N(\tilde{X})=(x_0^2+x_1^2+x_2^2+x_3^2)e_0$, which is complex-valued for complex coefficients. The form is already indefinite on the Hermitian subspace: the Hermitian element $\tilde{H}=e_0+ie_1$ has $N(\tilde{H})=(1-1)e_0=0$ while $\tilde{H}\neq0$, and $\tilde{H}=ie_1$ has $N(ie_1)=-e_0$, so neither sign is definite there. $\square$

**Consequence.** The norm form cannot certify that an element is non-zero, cannot define a topology, and cannot supply the positive quantity that Born probabilities require. Its physical role is the determinant — the Minkowski form on the Hermitian sector and the null cone of the pure states — not a metre.

**Remedy.** Use the Hermitian form $\mathrm{Tr}(\tilde{X}^\dagger\tilde{Y})$ for positivity, and the norm form for the cone and the metric; the two are not interchangeable, and the companion articles of this subcategory use them accordingly.

### O6. The norm form vanishes on non-zero elements

**Statement.** The radical of the norm form is non-trivial: there are non-zero $\tilde{X}$ with $N(\tilde{X})=0$, and every null element is orthogonal to itself in the associated bilinear form. In particular the whole pure-state boundary is null.

**Proof.** For the pure-state projector, $\bar{\tilde{P}}(\hat{\mu})=e_0-\tilde{P}(\hat{\mu})$ and hence
$$
N\bigl(\tilde{P}(\hat{\mu})\bigr)=\tilde{P}(\hat{\mu})\,\bar{\tilde{P}}(\hat{\mu})=\tilde{P}(\hat{\mu})\bigl(e_0-\tilde{P}(\hat{\mu})\bigr)=0
$$
for every $\hat{\mu}$ while $\tilde{P}(\hat{\mu})\neq0$; indeed the defining property $\tilde{P}^2=\tilde{P}$ together with $\tilde{P}\bar{\tilde{P}}=0$ characterises the boundary of the state space. Likewise $e_0\pm ie_k$ are null non-zero vectors, since $N(e_0\pm ie_k)=(1-1)e_0=0$. $\square$

**Consequence.** The state space is the boundary of the cone of a degenerate quadratic form. One cannot speak of the "length" of a state; the metric must be obtained as the second variation on the null boundary, and not from the form's value at a point.

**Remedy.** Read the metric from the second variation, not the value. The vanishing of a quadratic form on its cone is the standard mechanism of Lorentzian geometry, not a defect, but it must be accounted for rather than overlooked.

### O7. No single form is both canonical and positive

**Statement.** There is no quadratic form on $\mathbb{B}$ that is simultaneously positive definite and independent of an arbitrary normalization. The Hermitian form is positive definite but depends on the trace normalization; the norm form is canonical but indefinite.

**Proof.** The Hermitian form is determined by the trace, and the trace is normalised by $\mathrm{Tr}(e_0)=2$, a convention fixed by the degree of the matrix model; replacing $\mathrm{Tr}$ by $c\,\mathrm{Tr}$ for positive $c$ gives another positive definite form, so the positivity is canonical but the scale is not. The norm form is determined by the algebra's product alone, $N(\tilde{X})=\tilde{X}\bar{\tilde{X}}$, and is therefore canonical, but it is indefinite by O5. A form that were both would have to be intrinsic and positive simultaneously, and no such form exists on an algebra with a null cone. $\square$

**Consequence.** All probabilities, distances and normalizations in the framework are trace-relative. The trace normalization is a posit, and the numerical factors of the Fubini–Study metric are statements in the normalization $\mathrm{Tr}(e_0)=2$.

**Remedy.** State the normalization with every numerical claim, as the corpus does; the invariant content of any such claim is the statement that survives a rescaling of the trace.

### O8. The norm form gives a flat interior, not the Bures metric

**Statement.** The quadratic form of the algebra cannot generate the statistically distinguished metric of the mixed states. It supplies the flat Euclidean form $\tfrac14|d\mathbf{r}|^2$ on the whole ball, whereas the distinguished metric is the Bures metric.

**Proof.** For a state $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ and any displacement $\delta\tilde{\rho}=\tfrac12 i\,\delta\mathbf{r}$, the norm form is $-N(\delta\tilde{\rho})=\tfrac14|\delta\mathbf{r}|^2$, with no dependence on the radial direction; the quadratic form is the same at every point of the ball. The Bures metric is $\tfrac14\bigl(|d\mathbf{r}|^2+(\mathbf{r}\cdot d\mathbf{r})^2/(1-r^2)\bigr)$, which agrees with the flat form only at the centre $r=0$ and on tangential displacements at the boundary $r=1$. The two differ in the interior, and the difference is precisely the radial distinguishability term. $\square$

**Consequence.** The algebra's form fixes the geometry of the pure states and the geometry at the maximally mixed state, and nothing in between. Claims about the metrical structure of mixed states require an import from quantum information theory.

**Remedy.** Import the Bures metric, or the equivalent quantum Fisher information, as a standard statistical structure. This is a case where the framework should be credited with the boundary geometry and not with the interior.

### O9. There is no intrinsic algebraic norm

**Statement.** The algebra carries no norm determined by its algebraic structure alone. The two canonical forms are not norms, and a norm requires the choice of a faithful representation on a Hilbert space.

**Proof.** A norm must be positive definite, non-degenerate and satisfy the triangle inequality; the norm form fails positivity by O5 and non-degeneracy by O6, and the Hermitian form is a norm only up to a scale by O7. The operator norm, by contrast, is defined by a representation $\pi:\mathbb{B}\to B(\mathcal{H})$ and requires the Hilbert space $\mathcal{H}$ to be chosen; different faithful representations give the same finite-dimensional $C^{*}$-norm here, but the choice of representation is still an input, not a consequence of the algebra's relations. $\square$

**Consequence.** Statements of convergence, continuity and approximation in the framework are representation-relative unless the representation is fixed by the physics. The algebraic relations pin the structure but not the analytic size of its elements.

**Remedy.** Fix the representation once, at the start of a calculation, and record the choice; the companion articles fix the two-dimensional representation $\Phi$ throughout.

### O10. The invariance group of the norm form is not the symmetry group of the states

**Statement.** The group of invertible elements preserving the norm form under conjugation is $G_N=U(1)\cdot SL(2,\mathbb{C})$, strictly larger than the unitary group $U(2)$ that preserves the Hermitian form and acts on the state space. The algebra's quadratic form and its state-space geometry therefore have different symmetries.

**Proof.** From the multiplicativity of the determinant, $N(\tilde{U}\tilde{X}\tilde{U}^\dagger)=|N(\tilde{U})|^2N(\tilde{X})$, so the norm form is preserved exactly by the elements with $|N(\tilde{U})|=1$; the group is seven-real-dimensional and contains $U(2)$, which is four-real-dimensional. The element $\mathrm{diag}(\lambda,\lambda^{-1})$ with real $\lambda\neq1$ is in $G_N$ but not in $U(2)$. $\square$

**Consequence.** One cannot identify "the symmetry group" of the framework by asking which transformations preserve the norm form: the answer is larger than the group of physical symmetries and includes transformations that change the Hermitian norm of states.

**Remedy.** Distinguish the two preservation problems explicitly. Unitarity is the preservation of the Hermitian norm and its group is $U(2)$; invariance of the norm form — the determinant, in the matrix model — is the strictly different condition $|\det M(\tilde{U})|=1$, which defines a larger group and has no direct quantum-mechanical reading.

## III. Obstructions of Finite Dimension and Zero Divisors

### O11. The algebra is not a division algebra

**Statement.** There exist non-zero $\tilde{X},\tilde{Y}\in\mathbb{B}$ with $\tilde{X}\tilde{Y}=0$. Hence $\mathbb{B}$ has no multiplicative inverse operation defined on all its non-zero elements.

**Proof.** The complementary pure-state projectors satisfy
$$
\tilde{P}(\hat{\mu})\,\bigl(e_0-\tilde{P}(\hat{\mu})\bigr)=0
$$
for every unit $\hat{\mu}$, with both factors non-zero. In the matrix model this is the statement that rank-one matrices of orthogonal ranges multiply to zero; an element is invertible exactly when $\det M(\tilde{X})=N(\tilde{X})\neq0$, and the zero divisors are the elements of vanishing norm. $\square$

**Consequence.** The *pure* states are precisely the singular states: a pure state $\tilde{P}$ is idempotent with $N(\tilde{P})=0$, hence a zero divisor, while a mixed state $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ with $|\mathbf{r}|<1$ has $N(\tilde{\rho})=\tfrac14(1-r^2)e_0\neq0$ and is invertible. The multiplicative group of the algebra, $\mathbb{B}^\times=\{N\neq0\}$, therefore contains every mixed state and excludes every pure one, and statements requiring invertibility of a pure state are meaningless in this framework.

**Remedy.** None is needed; the structure is that of a matrix algebra, and the relevant group for transformations is $\mathbb{B}^\times$, acting on the module. The point of recording the obstruction is that "the quaternions are a division algebra" does not survive complexification, and the biquaternion algebra must not be used as if it did.

### O12. There are no canonical commutation relations inside the algebra

**Statement.** There are no elements $\tilde{X},\tilde{P}\in\mathbb{B}$ and no non-zero central scalar $\lambda$ with $[\tilde{X},\tilde{P}]=\lambda e_0$, and no finite-dimensional module of $\mathbb{B}$ carries such a pair either.

**Proof.** The trace of any commutator vanishes,
$$
\mathrm{Tr}\bigl([\tilde{X},\tilde{P}]\bigr)=\mathrm{Tr}\bigl(\tilde{X}\tilde{P}\bigr)-\mathrm{Tr}\bigl(\tilde{P}\tilde{X}\bigr)=0,
$$
by cyclicity, whereas $\mathrm{Tr}(\lambda e_0)=2\lambda\neq0$. The same argument applies in any finite-dimensional representation, since the trace there is also cyclic. $\square$

**Consequence.** The Heisenberg algebra, and with it position, momentum, and the creation and annihilation operators, cannot be internalised in $\mathbb{B}$. They require an infinite-dimensional extension.

**Remedy.** Work in the space of $\mathbb{B}$-valued functions of the appropriate configuration variables, on which the algebra acts pointwise; the commutator then involves a derivative and the trace argument does not apply. This is the standard route taken by the free-particle and mode-function articles of the corpus.

### O13. The algebra has no internal composite structure

**Statement.** The tensor product of two copies of the algebra is not the algebra: $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})\neq\mathbb{B}$. There is no tensor factorization of a single copy into two subsystems.

**Proof.** The two complex dimensions differ,
$$
\dim_\mathbb{C}\bigl(\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\bigr)=16\neq4=\dim_\mathbb{C}\mathbb{B},
$$
and under the matrix model $M_2(\mathbb{C})\otimes_\mathbb{C}M_2(\mathbb{C})\cong M_4(\mathbb{C})$. $\square$

**Consequence.** The two components of a state module element are not two subsystems; they are the two amplitudes of a single two-level system. A pair of qubits, and therefore entanglement as a resource, is not described by $\mathbb{B}$, and the Bloch ball is not closed under composition.

**Remedy.** Pass to tensor powers $\mathbb{B}^{\otimes n}$ or to the tensor powers of the module; the resulting state spaces are the higher-dimensional generalisations of the Bloch ball, not products of copies of it.

### O14. The norm-preserving unit is forced into the centre

**Statement.** There is no quantum dynamics over $\mathbb{B}$ that preserves the Hermitian norm for every Hermitian generator and whose unit is a non-central root of $-e_0$. A dynamics $i\hbar\,\partial_t\psi=J\tilde{H}\psi$ preserves the Hermitian norm for every Hermitian $\tilde{H}$ only if $J=\pm i$.

**Proof.** The generator is $G=-\hbar^{-1}J\tilde{H}$, so $G^\dagger=-\hbar^{-1}\tilde{H}J^\dagger$; anti-Hermiticity of $G$ for all Hermitian $\tilde{H}$ therefore reads $-\tilde{H}J^\dagger=J\tilde{H}$ for all Hermitian $\tilde{H}$, which at $\tilde{H}=e_0$ forces $J^\dagger=-J$ (so a general root of $-e_0$, which need not be anti-Hermitian, is excluded) and then requires $\tilde{H}J=J\tilde{H}$ for all Hermitian $\tilde{H}$, hence $J$ central. The central roots of $-e_0$ are $\pm i$. The non-central root $J=e_3$ with $\tilde{H}=ie_1$ gives $G=-\hbar^{-1}ie_2$, which is Hermitian and generates a non-unitary flow. $\square$

**Consequence.** The framework cannot realise a genuinely "biquaternionic" quantum mechanics whose evolution preserves the norm for the full class of Hermitian generators: that demand collapses the scalar field to the centre $\mathbb{C}$, and the algebra acts as a matrix algebra over that field. A non-central unit is not excluded outright, but its reach is exactly its commutant: $J=e_1$ gives $G=-\hbar^{-1}e_1\tilde{H}$, which is anti-Hermitian for precisely those Hermitian $\tilde{H}$ commuting with $e_1$, and Hermitian — hence norm-violating — for $\tilde{H}=ie_2$, say. The alternative units $e_1,e_2,e_3$, and more generally the unit pure real quaternions, are roots of $-e_0$ and are available as algebraic structures, but not as units of a norm-preserving dynamics; the elements $ie_k$ are not roots of $-e_0$ at all, since $(ie_k)^2=+e_0$.

**Remedy.** Either give up norm preservation — which departs from quantum mechanics — or restrict the class of generators to those commuting with the chosen $J$ — which singles out a subtheory. The framework's own choice is the third: accept that the scalar field is $\mathbb{C}$, and read $\mathbb{B}$ as an algebra of operators over it, which is what makes the state space, the trace pairing and the unitarity group work.

## IV. Obstructions of the Sector Structure

### O15. The two sectors do not form an algebra grading

**Statement.** The decomposition $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is not a grading of the associative algebra: $\mathbb{M}_+$ is not a subalgebra, and the product of two Hermitian elements need not be Hermitian. The decomposition is a grading of the commutator only.

**Proof.** For the Hermitian elements $ie_1,ie_2$,
$$
(ie_1)(ie_2)=i^2e_1e_2=-e_3\in\mathbb{M}_-,
$$
which is anti-Hermitian; so $\mathbb{M}_+\mathbb{M}_+\not\subseteq\mathbb{M}_+$. More precisely, products and commutators behave as
$$
\mathbb{M}_+\mathbb{M}_+\subseteq\mathbb{M}_++\mathbb{M}_-,
\qquad
[\mathbb{M}_+,\mathbb{M}_+]\subseteq\mathbb{M}_-,
\qquad
[\mathbb{M}_+,\mathbb{M}_-]\subseteq\mathbb{M}_+ ,
$$
the last two verified numerically on random elements of each sector. The commutator therefore grades the real Lie algebra $\mathbb{B}$ under $[\cdot,\cdot]$, while the product mixes the sectors. $\square$

**Consequence.** The material and informational subspaces cannot be treated as independent algebras. An observable's product with another observable is not an observable in general; only (anti-)commutators, or the trace, respect the split.

**Remedy.** Use the sector decomposition kinematically, to organise the components of a state and the two conjugate linear structures, and use the commutator or the Jordan product when a bilinear operation is needed.

### O16. The Hermitian sector carries no intrinsic complex structure

**Statement.** Multiplication by $i$ exchanges the two sectors, $i\mathbb{M}_+=\mathbb{M}_-$, so $\mathbb{M}_+$ is not a complex vector space. The Hermitian sector cannot be a complex Hilbert space in its own right.

**Proof.** For every basis element of $\mathbb{M}_+$, $i(ie_k)=-e_k$ and $i e_0=ie_0$, so
$$
i\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}=\mathbb{M}_- .
$$

Since the two subspaces intersect only at zero, no non-zero Hermitian element is $i$ times a Hermitian element. $\square$

**Consequence.** The framework's Hilbert space is the **module** $\mathbb{B}p\cong\mathbb{C}^2$, on which $i$ acts as the complex structure and the inner product is the Hermitian form; the observable space $\mathbb{M}_+$ is a real vector space and must be handled as such. Treating $\mathbb{M}_+$ as a complex Hilbert space is the characteristic error this catalogue is concerned to exclude.

**Remedy.** Put the complex structure on the module and keep the real structure on the observables; the two are related by the map $\psi\mapsto\psi\psi^\dagger$ that sends rays to Hermitian rank-one elements.

### O17. The state module is not canonical

**Statement.** There is no distinguished minimal left ideal of $\mathbb{B}$; the module $\mathbb{B}p$ depends on the idempotent $p$, and different choices give isomorphic but distinct submodules.

**Proof.** The minimal left ideals of $M_2(\mathbb{C})$ are the column spaces of rank-one projections; they are all isomorphic as modules, and the unitary group acts transitively on the rank-one projections, so no one of them is singled out by the algebra. Concretely, $p=\tfrac12(e_0+ie_3)$ and $p'=\tfrac12(e_0+ie_1)$ generate distinct ideals related by a unitary conjugation. $\square$

**Consequence.** The identification of the two components of a spinor, and hence the split into material and informational parts, requires a choice of basis; the state space is canonical only up to unitary equivalence. Physical predictions are invariant under the choice, but the bookkeeping is not.

**Remedy.** Fix the idempotent once and for all — the corpus fixes $p=\tfrac12(e_0+ie_3)$ — and verify that any statement of interest is invariant under unitary change of $p$. The isomorphism is not a canonical identification, and statements that depend on it must be shown to be basis-independent.

## V. Obstructions of Dynamics and Interpretation

### O18. The algebra contains no time and no Hamiltonian

**Statement.** There is no element or operation of $\mathbb{B}$ that represents the time derivative or selects a Hamiltonian. The dynamics must be supplied from outside.

**Proof.** The derivations of a finite-dimensional central simple algebra are inner: every derivation of $\mathbb{B}$ is of the form $\mathrm{ad}_{\tilde{X}}$ for some $\tilde{X}$. Every such derivation is frozen on the centre and generates a conjugation flow; none of them is a distinguished time translation, and there is no element of the algebra that can be picked out as the generator of physical time. The Schrödinger equation $i\hbar\partial_t\psi=J\tilde{H}\psi$ therefore introduces both $\partial_t$ and $\tilde{H}$ as external data. $\square$

**Consequence.** The framework derives no arrow of time and no equation of motion from its algebra; the dynamical law is a posit, and so is the identification of the central parameters that accompany it.

**Remedy.** Import the Hamiltonian and the time parameter, as every quantum theory does; the algebraic contribution is the form of the evolution (unitary, norm-preserving, generated by a commutator), not its generator.

### O19. The measurement problem is not addressed by the algebra

**Statement.** No element or operation of $\mathbb{B}$ selects a measurement outcome, a pointer basis, or a collapse. The algebraic structure is compatible with any of the standard interpretations and with none in particular.

**Proof.** By O1 there is no canonical maximal commutative subalgebra, so no preferred outcome basis is singled out; by O2 there are no non-trivial central projections, so there are no algebraic branch labels; and by O18 there is no extra dynamics to break the unitary evolution. The three ingredients that a solution needs — a preferred basis, branch labels, or modified dynamics — are all absent. $\square$

**Consequence.** The framework's reformulation of quantum mechanics in biquaternionic form is a reformulation of the kinematics and of the norm structure, not a resolution of the measurement problem.

**Remedy.** Address the problem with added structure: a collapse dynamics, a decoherence mechanism, or an interpretation. The companion article *The Measurement Problem in Algebraic Form* sets out the options in this framework's language.

### O20. No algebraic origin of scale

**Statement.** The algebra contains no scale: it is invariant under the simultaneous rescaling of all its elements, and it admits no relation that could fix a mass, a length, or an energy.

**Proof.** Every defining relation $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$, $i^2=-1$ is scale-free. A central element $\lambda e_0$ satisfies no equation with a numerical solution by O4; and the norm form is quadratic, so it rescales by the square of the element. No combination of the relations produces a number with the dimensions of a physical scale. $\square$

**Consequence.** The framework cannot explain the origin of mass or of any dimensionful parameter; masses enter through central coefficients such as $m e_0$.

**Remedy.** Import the scales as data, or obtain them from a structure external to the algebra — a dynamical mechanism, a boundary condition, or a symmetry-breaking sector. The catalogue records that they are not algebraic consequences of $\mathbb{B}$.

### O21. No stable classical sector under a generic dynamics

**Statement.** No maximal commutative subalgebra is invariant under a generic unitary evolution. Consequently no pointer basis is preserved by the dynamics.

**Proof.** Conjugation by a unitary element implements a rotation of the Bloch sphere; a generic rotation maps a given axis $\hat{n}$ to a different axis, and hence maps $\mathbb{A}_{\hat{n}}$ to $\mathbb{A}_{\hat{n}'}$ with $\mathbb{A}_{\hat{n}'}\neq\mathbb{A}_{\hat{n}}$ by O1. A subalgebra is invariant under a one-parameter unitary group only if its axis is fixed by the corresponding rotation, i.e. only if the axis is an eigenvector of the Hermitian generator, a non-generic condition. $\square$

**Consequence.** Classicality in this framework cannot be a permanent algebraic property of a subsystem; it must be emergent, contextual, or maintained by a mechanism external to the closed unitary evolution.

**Remedy.** Appeal to decoherence, coarse-graining, or a selected context, which are statistical or interpretive inputs. The companion articles on the quantum–classical divide and on the informational aspects treat these routes.

## VI. Obstructions of the Module Action

### O22. Multiplication is chirality-blind

**Statement.** Every operation that $\mathbb{B}$ supplies is a **multiplication** — left multiplication on the spinor module, the adjoint action on the algebra, the central phase — and a multiplication acts on the two chiral components of a Dirac module with the **same** matrix. The algebra therefore cannot supply, as a multiplication, any operation that gives the two chiralities inequivalent representations or exchanges them in a single step: the chiral gauge coupling that the electroweak theory requires, the internal matrices of charge conjugation and parity, the parity-reflecting frame element $\gamma^0$ and the energy-sign split built on it, and the odd form of a first-order operator (the Feynman slash). None of these has a representative in $\mathbb{B}$.

**Proof.** $\mathbb{B}\cong M_2(\mathbb{C})=\mathrm{End}(S)$, with $S$ the unique simple module, of complex dimension two. Every left $\mathbb{B}$-module is a direct sum of copies of $S$, and the left action of $\tilde B\in\mathbb{B}$ on such a sum is block diagonal, the same matrix $M(\tilde B)$ on every copy. That action commutes with the chirality grading of the module; an exchange of the two chiral components is off-diagonal and is not of that form. Both halves were checked in the explicit model $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$: with the grading $\mathrm{diag}(I_2,-I_2)$ a generic left action commutes with it, while $\gamma^0$ anticommutes with it and is not equal to any $\mathrm{diag}(M,M)$. The corpus records the consequence object by object: the central phase is vector-like so its cubic trace cancels (*Anomalies and Anomaly Cancellation*); the non-abelian action is left multiplication and cannot give the two chiralities inequivalent representations (*Custodial Symmetry and the Rho Parameter*); the chiral coupling is the layer the framework does not reach (*The W and Z Bosons*); the internal matrices of $C$ and $P$ are odd and have no representative in $\mathbb{B}$ (*The CPT Theorem*). These are one property, stated four times. $\square$

**Consequence.** The framework's entire apparatus — the gradient, the rotors, the gauge actions, the mass, the phase — is multiplicative and therefore vector-like. The discrete operations and the energy-sign split are not defects of a particular realization but consequences of the mechanism that carries them. The Feynman slash is the mildest instance: because $\mathbb{B}$ carries a first-order operator of its own, the even gradient $\tilde{\nabla}$, the slash's *role* is taken over inside the algebra, so it is a change of notation rather than a loss. The others have no such substitute.

**Remedy.** Separate the two mechanisms of the dictionary article: multiplication on the module and conjugation on the algebra are what the algebra supplies, and both are available; anything that must exchange the two chiralities is carried by the module together with one frame element, or not at all. The discrete operations remain module-level, as the CPT article records, and the chiral gauge structure is an import. The vector-like property is a fact about $\mathbb{B}$, not about any chosen gauge group, and no choice of group removes it.

## The Catalogue in One Table

| Obstruction | Algebraic locus | Remedy |
|---|---|---|
| O1 no canonical MASA | transitive $U(2)$ action on the axis | choose a context |
| O2 no central idempotents | $\mathbb{B}$ a factor | adjoin a label algebra |
| O3 centre acts trivially on states | $Z(\mathbb{B})\cong\mathbb{C}$ | none needed |
| O4 parameters not determined | centrality of the parameters | import the data |
| O5 norm form indefinite | signature $(1,3)$ on $\mathbb{M}_+$ | use the Hermitian form for positivity |
| O6 norm form vanishes on states | null cone of the boundary | read the metric from the second variation |
| O7 no form both canonical and positive | trace normalization | state the normalization |
| O8 no Bures metric | flat quadratic form | import the Fisher metric |
| O9 no intrinsic norm | representation required | fix the representation once |
| O10 $G_N\neq U(2)$ | determinant multiplicativity | separate the two preservation problems |
| O11 zero divisors | $\mathbb{B}\cong M_2(\mathbb{C})$ | none needed |
| O12 no commutator with a central value | cyclicity of the trace | pass to function modules |
| O13 no internal tensor factorization | dimension count | use $\mathbb{B}^{\otimes n}$ |
| O14 unit forced central | norm preservation for all $\tilde{H}$ | accept the complex scalar field |
| O15 sectors not an algebra grading | $\mathbb{M}_+\mathbb{M}_+\not\subseteq\mathbb{M}_+$ | use commutators or the trace |
| O16 no complex structure on $\mathbb{M}_+$ | $i\mathbb{M}_+=\mathbb{M}_-$ | put it on the module |
| O17 module not canonical | transitive action on idempotents | fix $p$ and check invariance |
| O18 no time or Hamiltonian | inner derivations only | import the dynamics |
| O19 measurement problem untouched | O1, O2, O18 together | add interpretive structure |
| O20 no algebraic scale | scale-free relations | import the scales |
| O21 no stable classical sector | generic rotations move axes | decoherence or coarse-graining |
| O22 multiplication chirality-blind | $\mathbb{B}=\mathrm{End}(S)$ acts identically on each copy of $S$ | carry chirality by the module and one frame |

## What the Catalogue Does Not Say

Two clarifications prevent the catalogue from being read as a refutation of the framework.

**It does not say that the algebra's positive results are withdrawn.** The state space as the trace-one slice of the future cone, the transition probability as a trace pairing, the Fubini–Study metric as the second variation of the norm form, the Kähler structure, the unitarity theorem and the identification of the centre as the classical sector all stand; they are the content of the preceding articles of the subcategory. The obstructions concern what those structures cannot additionally be asked to do, and every one of them is stated with its remedy.

**Most of the obstructions are shared with ordinary complex quantum mechanics, and only some are peculiar to the biquaternion setting.** The distinction matters for any assessment of the framework, and it is worth tabulating.

*Shared with complex quantum mechanics.* The absence of a canonical maximal commutative subalgebra and the absence of a preferred basis are generic facts about any non-commutative observable algebra. The measurement problem, the external status of the Hamiltonian and of the arrow of time, the absence of a derivation of dimensionful parameters, the need for a representation to define a norm, and the impossibility of canonical commutation relations inside a finite-dimensional algebra are equally generic; complex quantum mechanics meets all of them and answers them with an external Hilbert space, an external Hamiltonian, and an interpretation. An objection to the biquaternion framework on these grounds is an objection to quantum mechanics as such.

*Specific to the biquaternion framework.* What is distinctive is the coexistence of two quadratic forms with different invariance groups (O5–O10), the fact that the Hermitian sector is not a subalgebra and carries no complex structure (O15–O16), the forcing of the unit into the centre so that no genuinely biquaternionic norm-preserving quantum mechanics exists (O14), the non-canonicity of the module (O17), the use of a two-real-dimensional centre as the whole classical sector, with the resulting absence of superselection structure (O2), and the chirality-blindness of every operation the algebra supplies (O22), which is the algebraic form of the framework's vector-like obstruction. These are the obstructions that a reader must weigh, and they are the ones that the framework's own discipline — fundamental versus derived — is designed to keep in view.

**A closing balance.** An algebra that could be asked to do everything would determine its own parameters, select its own bases, fix its own scales and contain its own time; no algebra does, and the demand to do so is not a standard of adequacy in physics. What a structural framework owes its reader is an exact account of the division of labour between what its algebra supplies and what must be supplied from outside. The list above is that account for $\mathbb{B}$: the algebra supplies the state space, the two forms, the unitarity group and the centre, and it supplies them exactly; everything else is named, with its remedy, and left where it belongs.

## Summary

The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is the structural spine of the non-relativistic theory, and this article has catalogued its algebraic obstructions in six groups. In commutativity and the centre: there is no canonical maximal commutative subalgebra, no non-trivial central idempotent, no observable central data, and no internal determination of the theory's parameters, because the centre is the two-real-dimensional $\mathbb{C}e_0$ and it acts trivially on states. In the quadratic forms: the norm form is indefinite and vanishes on non-zero states, the Hermitian form is positive but trace-relative, no single form is both canonical and positive, and the statistically distinguished metric of mixed states is not the algebra's flat form; the invariance group of the norm form, $G_N=U(1)\cdot SL(2,\mathbb{C})$, is strictly larger than the unitary group. In finite dimension and zero divisors: the algebra is not a division algebra, it carries no canonical commutation relation, it admits no internal tensor factorization, and a unit that preserves the norm for every Hermitian generator is forced into the centre, so no genuinely biquaternionic quantum mechanics with a uniform norm-preserving evolution exists. In the sector structure: the split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ grades the commutator but not the product, the Hermitian sector carries no intrinsic complex structure, and the state module depends on a non-canonical choice of idempotent. In dynamics and interpretation: the algebra contains no time, no Hamiltonian, no preferred basis, no scale, and no stable classical sector under a generic evolution. In the module action: every operation the algebra supplies is a multiplication, and a multiplication acts identically on the two chiral components of a Dirac module, so the framework's apparatus is vector-like by construction and the chiral structure, the discrete operations and the energy-sign split are external.

Each obstruction is proved from the defining relations and is stated with its consequence and its remedy. The catalogue's purpose is not to fault the framework but to locate exactly where its algebra's resources end: at a chosen context, an extended module, an imported statistical metric, or a physical posit. Most of the obstructions are shared with ordinary complex quantum mechanics and are not peculiar to the biquaternion setting; the distinctive ones concern the coexistence of two forms, the non-algebraic nature of the sector split, the centralisation of the unit, the minimality of the classical sector, and the chirality-blindness of multiplication — and these are the items on which the framework should be judged.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\dagger=\bar{\cdot}\circ{}^{*}$ | Hermitian conjugation |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $Z(\mathbb{B})=\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | Centre of $\mathbb{B}$; the series symbol is $\mathbb{C}_{\mathbb{B}}$ |
| $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$ | Trace, $\mathrm{Tr}(e_0)=2$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form, $\mathbb{B}^{\times}=\{N\neq0\}$ |
| $\langle\tilde{X},\tilde{Y}\rangle_\dagger=\mathrm{Tr}(\tilde{X}^\dagger\tilde{Y})$ | Hermitian form |
| $\tilde{P}(\hat{\mu})=\tfrac12(e_0+i\hat{\mu})$ | Pure state, null under $N$ |
| $\mathbb{A}_{\hat{n}}$ | Maximal commutative subalgebra |
| $\mathbb{B}p$, $p=\tfrac12(e_0+ie_3)$, also written $S$ | State (spinor) module, $\cong\mathbb{C}^2$; $\mathbb{B}=\mathrm{End}(S)$ |
| $M_2(\mathbb{C})$ | Matrix model; $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$ |
| $U(2)$ | Norm-preserving (unitary) group |
| $G_N=U(1)\cdot SL(2,\mathbb{C})$ | Norm-form-preserving group, $\dim_\mathbb{R}=7$ |
| $\mathrm{ad}_{\tilde{X}}$ | Inner derivation $[\tilde{X},\cdot]$ |

## Further Reading

- N. Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for central simple algebras, their derivations, and their maximal commutative subalgebras.
- R. S. Pierce, *Associative Algebras* (Springer, 1982), for the structure of full matrix algebras, their simplicity, their ideals, and their idempotents.
- Y. A. Drozd and V. V. Kirichenko, *Finite Dimensional Algebras* (Springer, 1994), for zero divisors, the Wedderburn theorems, and the module theory of finite-dimensional algebras.
- B. Farb and R. K. Dennis, *Noncommutative Algebra* (Springer, 1993), for central simple algebras, the tensor product of matrix algebras, and the inner derivation property.
- G. Birkhoff and J. von Neumann, "The logic of quantum mechanics", *Annals of Mathematics* **37**, 823 (1936), for the algebraic setting of quantum propositions and the role of the scalar field.
- H. Weyl, *The Theory of Groups and Quantum Mechanics* (Dover, 1950), for the algebraic treatment of quantum kinematics and the origin of the complex field.
- G. G. Emch, *Algebraic Methods in Statistical Mechanics and Quantum Field Theory* (Wiley-Interscience, 1972), for superselection sectors, central projections, and the algebraic formulation of the measurement problem.
- N. P. Landsman, *Foundations of Quantum Theory: From Classical Concepts to Operator Algebras* (Springer, 2017), for the quantum–classical divide, Gelfand duality, and the limitations of algebraic reformulations.
- S. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford University Press, 1995), for the quaternionic scalar-field programme, its unitarity conditions, and the obstructions it meets.
- E. Artin, *Geometric Algebra* (Interscience, 1957), for the norm form, its multiplicativity, and the identification of the unit-norm group with the double cover of the Lorentz group.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000), for composite systems, the tensor product of qubits, and the Bloch-ball picture of a single qubit.
