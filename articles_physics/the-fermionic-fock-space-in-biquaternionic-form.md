# __The Fermionic Fock Space in Biquaternionic Form__

## Introduction

The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* constructs the Fock space of the finite biquaternion algebra, exhibits the one fermionic mode inside $\mathbb{B}$, and shows that its ladder operators are the spin ladder operators. The companion article *The Spin–Statistics Theorem in Biquaternionic Form* fixes which bracket goes with which spin and shows that the spin-$\tfrac12$ field is quantized with anticommutators. Neither article constructs the Fock space of the *field*, and neither asks what the biquaternion structure says about the shape of that space. That is this article's subject.

The field of the article is the Dirac field, an element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$ whose two parts are the two values of the chirality. At one momentum, on the particle branch, a one-particle state is an L part, and the L parts form a complex two-dimensional space $S$. The result is that the fermionic Fock space of the field, on that branch at one momentum, is the **exterior algebra** over the one-particle space,

$$
\boxed{\;\mathcal{F}=\Lambda S=\bigoplus_{n=0}^{\dim S}\Lambda^n S,
\qquad
\Lambda(V\oplus W)=\Lambda V\mathbin{\hat\otimes}\Lambda W\;},
$$

and that this is not an extra assumption but the reflection in the state space of two facts already fixed by the parents: the one-particle space is a complex two-dimensional space, and the bracket is the anticommutator, which the spin–statistics companion fixes by the spin. The two together force the exterior algebra, occupation numbers $0$ and $1$, and the Lorentz decomposition $0\oplus\tfrac12\oplus 0$ over the two spin states of one momentum.

**Notation, by reference.** The algebra $\mathbb{B}$ and its units, the two conjugations ${}^{\natural}$ and ${}^{*}$, the scalar part $\mathrm{Sc}$ and the trace $\operatorname{Tr}$ are those of *Algebra and Element Conventions*, *Product and Form Conventions* and *Norm and Pairing Conventions*; the letters $L$ and $R$ on an element are the subscript of *Operator Chirality on the Biquaternion Algebra*, §*The Subscript on an Element*; the Fock mark $_{\mathrm{fop}}$ is that of *Unit, Index and Notation Conventions*. Nothing of this is redefined here. An action is written out, $Q\mapsto aQb$; no operator symbol is used in the body, and the cells return only in the closing legacy section.

The article develops five things.

- **The one-particle space and its two structures.** The space $S$ of L parts is complex two-dimensional; on it sit the positive-definite Hermitian form, which is the Hilbert-space form of the Fock construction, and the antisymmetric product, which is the algebra's own and which gives the invariant bilinears. The algebra's quaternionic norm degenerates on $S$ entirely. The two must not be interchanged.
- **The exterior algebra.** Occupation-number states, the wedge product, the Koszul sign, and the reason that sign appears in the state space rather than in the operators.
- **The Lorentz content.** $\Lambda S$ is the reducible representation $\Gamma(\rho)$; its decomposition into irreducibles is computed, and it is one doublet $\tfrac12$ plus two singlets, the vacuum and the antisymmetric pair. The $2\pi$ rotation acts as $(-1)^{N_{\mathrm{fop}}}$, tying the state-space grading to the parity of the number operator.
- **The functor $\Gamma$ and the grading.** $\Gamma(-I)=(-1)^{N_{\mathrm{fop}}}$ is derived and recomputed. The Fock space is $\mathbb{Z}/2$-graded, and the grading is the one the observable algebra commutes with.
- **The sector content.** Pure one-mode states are $\mathbb{B}_{\Psi}$ elements; the four-dimensional $\Lambda S$ is not an element of $\mathbb{B}$; the Born rule is the normalised Hermitian form, read through the trace; and the field's Fock space is the tensor product over modes, whose grading is the field's fermionic parity.

The division between transcribed standard material and the algebra's own statements is marked throughout.

## The One-Particle Space

The one-particle space of the biquaternion Dirac field, on the particle branch at one momentum, is the space $S$ of L parts of $\mathbb{B}$: the elements whose chirality takes the value $L$, read up to a complex multiple. It is complex two-dimensional, because each of the two values of the chirality is a complex two-dimensional part of $\mathbb{B}$ (*Special Element Conventions*, §*The Spinor Convention*), the two values themselves being those of §*The Chirality Convention*. The two values of the subscript are the only structure the space costs in this article.

Only the particle branch is used below. The antiparticle branch is a second copy $S^{\mathrm c}$, and the full Dirac one-particle space is $S\oplus S^{\mathrm c}$ per momentum. The exterior algebra over the doubled space is the full Dirac Fock space, sixteen-dimensional per momentum; the construction here is the four-dimensional one-branch factor, and the doubling is recorded where it changes a count.

Two structures live on $S$, and the distinction is one of the framework's standing conventions.

**The Hermitian form.** The restriction to $S$ of the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ of *Product and Form Conventions*, §*The Involutions and the Four Forms*, is a complex number for every pair of L parts, linear in the first argument and antilinear in the second. That form is positive definite on all of $\mathbb{B}$, so its restriction to $S$ is positive definite, and it is the Hilbert-space form of the Fock construction, the one that makes the fermionic Fock space a Hilbert space. It is *not* the algebra's quaternionic norm.

**The quaternionic norm degenerates on $S$.** The quaternionic norm $\langle\cdot\rangle_{\natural}$ is the algebra's own, and its central spelling is the element $\tilde Q\tilde Q^{\natural}$ (*Norm and Pairing Conventions*, §*The Four Algebraic Norms and the Unitary Convention*). For an L part $\zeta$ that element vanishes, and the reason is a derived form of the two rules of the letters. The natural conjugation reverses the order of a product, and an involution that reverses the order exchanges the two sides (*Operator and Calculus Conventions*, §*The Two Sides and the Renaming Theorem*); the value of an element is read on a right multiplication, so the conjugate of an L part is an R part. Then $\zeta\zeta^{\natural}$ takes the letter of its right factor, which is R, while $\zeta^{\natural}\zeta$ takes the letter of $\zeta$, which is L; but the two products are the same central element, and only the zero element carries both values. Hence $\zeta\zeta^{\natural}=0$, and the quaternionic norm vanishes on every L part. The one-particle space is therefore totally isotropic for the quaternionic norm, and the norm does not descend to a form on it.

A one-particle state is therefore an element of the algebra: an L part, whose *physical* content is the ray in $S$ and whose *algebraic* content is the element itself. The two are related by the Hermitian form for probabilities and by the antisymmetric product for the Lorentz-invariant bilinears. The classical plane-wave solution $w^{(r)}(\vec p)$ of the solutions article is a one-particle state in this sense; the positive-frequency half of the parent's mode expansion is exactly the statement that the one-particle space at momentum $\vec p$ is $S_{\vec p}\cong S$, spanned by the two solutions $w^{(r)}(\vec p)$.

### The Lorentz Action and the Covering Sign

The Lorentz action on $S$ is the spin-$\tfrac12$ representation, and a rotor $\tilde U$ of the algebra acts by $Q\mapsto\tilde UQ$. Two of its features are used below and are recorded here.

First, the action factors through the double cover: the rotor through $2\pi$ is $-e_t$ (*Norm and Pairing Conventions*, §*The Word and Its Factors*), and $-e_t$ multiplies every element by $-1$. This is the module-level statement of the covering and is computed in the spin–statistics companion.

Second, the action preserves the antisymmetric product up to the quaternionic norm of the rotor. For L parts $\zeta,\eta$,

$$
(\tilde U\zeta)\wedge(\tilde U\eta)=\langle\tilde U\rangle_{\natural}\;\zeta\wedge\eta ,
$$

which is a derived form: the factor is the quaternionic norm of the rotor, and a unit element has quaternionic norm one (*Norm and Pairing Conventions*, §*The Four Algebraic Norms and the Unitary Convention*). For every Lorentz rotor, therefore, the two-particle state is carried to itself, and it is this, and not a transpose identity of an array, that makes the *antisymmetric* power of $S$ a singlet and the two-particle state below Lorentz invariant. The Hermitian form, by contrast, is invariant only on the compact subgroup, as the one-particle article states; a boost does not preserve it, and the invariant bilinears of the space are the antisymmetric products.

## The Exterior Algebra

With $\dim_\mathbb{C}S=2$ the exterior algebra is short, and the fermionic Fock space is

$$
\boxed{\;\mathcal{F}=\Lambda S=\mathbb{C}\oplus S\oplus\Lambda^2S ,
\qquad
\dim_\mathbb{C}\mathcal{F}=1+2+1=4\;}.
$$

Its canonical basis is the occupation-number basis

$$
|0\rangle ,
\qquad
|\!\uparrow\rangle ,
\qquad
|\!\downarrow\rangle ,
\qquad
|\!\uparrow\downarrow\rangle=|\!\uparrow\rangle\wedge|\!\downarrow\rangle ,
$$

and this is the Fock space of the two spin states of one momentum — two modes in the parent's counting, whose one-particle space is two-dimensional. The vacuum is the unit of the exterior algebra; the one-particle states are $S$ itself; the two-particle state is the top power.

The top power is read inside the algebra, and the reading is a derived form. For L parts $\zeta,\eta$ the exterior product is the algebra's own antisymmetric product,

$$
\zeta\wedge\eta=\tfrac12\bigl(\zeta\eta-\eta\zeta\bigr),
$$

which is again an L part, because a product takes the letter of its right factor, and which is pure, because the scalar part of a product is symmetric. The antisymmetric products of L parts are therefore elements of $\mathbb{B}$, and they span one complex dimension: the space $S$ is two-dimensional and the pairing is antisymmetric, so all its values are multiples of one nonzero value. That line of pure L parts is the top power read inside the algebra, and the singlet of the next section is that line.

**The wedge and the Koszul sign.** The product is the wedge, and it is graded-commutative:

$$
q_1\wedge q_2=(-1)^{|q_1|\,|q_2|}\,q_2\wedge q_1 ,
$$

so that $q_1\wedge q_2=-q_2\wedge q_1$ for odd elements. The sign is the whole fermionic content of the state space, and it is the same sign that appears in the mode anticommutator. It has an operational consequence that carries the physics: $\theta\wedge\theta=0$ for any odd $\theta$, so wedging twice with the same element gives nothing, and the vacuum, being the unit of the algebra, is annihilated by the contraction:

$$
a_{\mathrm{fop}}|0\rangle=0 ,
\qquad
\bigl(a_{\mathrm{fop}}^{\dagger}\bigr)^2=0 ,
$$

and no state can be occupied twice. Pauli exclusion is not a dynamical accident of the Dirac field; it is the statement that the state space is the exterior algebra, which is what the anticommutator builds.

**The graded product and the number grading.** The degree operator $N_{\mathrm{fop}}$ assigns to a basis vector of $\Lambda^nS$ the eigenvalue $n$ and acts as degree multiplication. The wedge is compatible with it in the graded sense: $(\Lambda^m)\wedge(\Lambda^n)\subseteq\Lambda^{m+n}$. This is the $\mathbb{Z}$-grading, and by reduction modulo two the $\mathbb{Z}/2$-grading:

$$
\mathcal{F}=\mathcal{F}_{\mathrm{even}}\oplus\mathcal{F}_{\mathrm{odd}} ,
\qquad
\mathcal{F}_{\mathrm{even}}=\mathbb{C}\oplus\Lambda^2S ,
\qquad
\mathcal{F}_{\mathrm{odd}}=S .
$$

The even part is the state space of an even number of quanta; the odd part is the one-particle space. The field operators below are odd; the observables are even.

### Why the Antisymmetric Algebra Rather Than the Symmetric One

For a bosonic field the state space is the symmetric algebra $\mathrm{S}(V)$ over the one-particle space; for a fermionic field it is the exterior algebra. The choice is fixed by the bracket, and the bracket is fixed by the spin through the spin–statistics theorem, which the companion article states and tests. Two remarks make the connection to the algebra concrete.

The first is the one-mode coincidence of the parent Fock-space article: inside $\mathbb{B}$ a pair of elements can be chosen whose symmetric product is the unit and whose squares vanish, so the algebra hosts one *fermionic* mode and no bosonic one. The display is the parent's, and it is not restated here; the four-dimensional $\Lambda S$ above is the same construction applied to the two spin states of one momentum, which the parent counts as two modes. The second is the trace identity that blocks the bosonic alternative: a canonical commutator would have to be central, $[a,b]=c\,e_t$ with $c\in\mathbb{C}$, but the trace of a commutator vanishes and $\operatorname{Tr}(e_t)=2$, so $c=0$.

Neither remark *derives* the fermionic bracket for the field — that is the theorem's, and the companion is explicit that the algebra does not force it. What they establish is that the algebra's finite content is the fermionic one, so that the exterior algebra over the one-particle space is the state space the algebra itself supplies.

## The Lorentz Content of the Fock Space

The Lorentz group acts on $S$ through the spin-$\tfrac12$ representation $\rho$, a rotor acting by $Q\mapsto\tilde UQ$. On $\mathcal{F}$ it acts through the exterior (antisymmetric) power,

$$
\Gamma(\rho)=\bigoplus_{n=0}^{2}\Lambda^n\rho ,
$$

where $\Lambda^n\rho$ denotes the induced action on $\Lambda^nS$, and the reason this is the natural action is that the exterior algebra is a functor: it converts each one-particle representation into the sequence of its antisymmetric powers, preserving direct sums and duals. (It does not turn a tensor product into a tensor product; only the direct sum has the tensor-product rule.)

The decomposition is computed by symmetry. On $S$ the spin generators are the algebra elements $\tilde S_i=\tfrac{\hbar}{2}i\vec e_i$, whose action is $\zeta\mapsto\tilde S_i\zeta$, and the induced operator $\hat S_i=\Gamma(\tilde S_i)$ acts as $0$ on the vacuum, as that same action on $\Lambda^1S=S$, and as the induced scalar action on $\Lambda^2S$. The top power is annihilated by every $\hat S_i$: the rotor $\exp(\theta\,\vec u\cdot\tilde S)$ is a unit element at every $\theta$, so by the antisymmetric-product identity of §*The Lorentz Action and the Covering Sign* it carries $\zeta\wedge\eta$ to itself, and differentiating at $\theta=0$ gives $\hat S_i(\zeta\wedge\eta)=0$. The top power is therefore a Lorentz **singlet**, and the vacuum is the other. On $\Lambda^1S$ the quadratic Casimir is the one-particle Casimir, $s(s+1)=\tfrac34$ in units $\hbar=1$. The eigenvalues of $\hat S^2=\sum_i\hat S_i^2$ on $\mathcal{F}$, in the occupation basis, are

$$
\{0,\tfrac34,\tfrac34,0\},
$$

which is the decomposition

$$
\boxed{\;\Lambda S=\mathbb{C}\;\oplus\;S\;\oplus\;\mathbb{C}
\qquad\text{i.e.}\qquad
0\oplus\tfrac12\oplus 0\;}.
$$

They were recomputed on the four-dimensional space $\Lambda S$ by building the mode representation explicitly: diagonalising $\hat S^2$ returns the spectrum $\{0,\tfrac34,\tfrac34,0\}$, with $N_{\mathrm{fop}}$ eigenvalues $\{0,1,1,2\}$ and the projection of the spin along the declared direction with eigenvalues $\{0,\tfrac12,-\tfrac12,0\}$. The singlets are the vacuum and the antisymmetric pair; the doublet is the one-particle space. This is the same $\Lambda S$ of the previous section, now read as a representation.

The same decomposition follows without diagonalising, and the derivation shows why the top power must be a singlet. On $\Lambda^1S=S$ the induced action is the one-particle action, whose Casimir is $s(s+1)=\tfrac34$. On $\Lambda^2S$, which is one-dimensional, every generator vanishes by the antisymmetric-product identity, so the top power is a singlet; the vacuum is the other. The Casimir spectrum is therefore $\{0,\tfrac34,\tfrac34,0\}$ with no further computation, and the invariant two-particle state is the line of pure L parts, which is the reason the antisymmetric-product identity appears in the same role.

Three consequences are worth stating.

**The $2\pi$ sign and the grading agree.** The covering element $-e_t$ acts on $\Lambda^nS$ as $(-1)^n$ times the identity, so the nontrivial element of the double cover is precisely the degree parity on the Fock space. Because the one-particle space is odd, the action of $-e_t$ on it is $-\mathrm{id}$; on the vacuum and on the pair it is $+\mathrm{id}$. A $2\pi$ rotation therefore acts as the fermionic parity $(-1)^{N_{\mathrm{fop}}}$ on the state space: the one-particle states carry the sign $-1$, while the even subspace and every bilinear are returned to themselves, so the sign is invisible in observables and only the $4\pi$ rotation returns a one-particle state to itself. This is the state-space content of the spin–statistics pairing of the companion article.

**The field's Fock space is a tensor product.** For the field, the one-particle space on the particle branch is $\bigoplus_{\vec p}S_{\vec p}$, and the functor gives

$$
\mathcal{F}_{\mathrm{field}}=\Lambda\!\left(\bigoplus_{\vec p}S_{\vec p}\right)
=\bigotimes_{\vec p}\Lambda S_{\vec p},
$$

the graded tensor product, with the Koszul sign across momenta. Each factor is four-dimensional and the vacuum is the empty wedge. Occupation numbers are $0$ and $1$ mode by mode; the grading is the parity of the total occupation; and the Lorentz content is the tensor tower generated by the two singlet powers and the doublet power at each momentum. The antiparticle branch adds a second factor $\Lambda S^{\mathrm c}_{\vec p}$ at each momentum, so the full Dirac factor is $4\times4=16$-dimensional; the counting and the grading above are those of one branch, and the full parity is the product of the two branch parities.

**The mode algebra fills the matrix algebra of the Fock space.** Pair each annihilation operator with its creation operator into $2N$ Hermitian generators — the doubling of the $N$-mode one-particle space. They satisfy the canonical anticommutation relations, and the operators they generate fill the full matrix algebra of the Fock space,

$$
\mathcal{A}_N\;\cong\;M_{2^N}(\mathbb{C}) ,
$$

where $\mathcal{A}_N$ is the algebra generated by $N$ fermionic modes; it was checked by dimension, $4$ for $N=1$ and $16$ for $N=2$. The spin–statistics companion's realization of the Dirac algebra is the one-particle side of this identity: its generators are odd operators on the fermionic Fock space, and its even part is the algebra of the frame, $\mathbb{B}$ itself. The mode algebra $\mathcal{A}_N$ is a different algebra, that of the $2N$ mode operators; for $N=1$ it is $\mathbb{B}$, and for $N=2$ it is the full matrix algebra of the sixteen-dimensional space. The identity is recorded here as the algebraic fact that the state space carries; its physical exploitation belongs to the articles that map fermions onto other descriptions.

## The Functor $\Gamma$, the Grading and the Parity

The exterior-power construction is a functor from the one-particle category to the state-space category. Three of its properties are used in the framework.

**Preservation of the structure.** $\Gamma$ carries direct sums to graded tensor products and duals to duals; in symbols, $\Gamma(V\oplus W)=\Gamma(V)\mathbin{\hat\otimes}\Gamma(W)$ and $\Gamma(V^*)=\Gamma(V)^*$. It is a functor, so it preserves identities and composition. It does **not** carry a tensor product to a tensor product: $\Lambda(V\otimes W)$ is not $\Lambda V\otimes\Lambda W$ in general, and only the direct sum has the tensor-product rule. This is what makes the many-mode Fock space a tensor product of one-mode spaces, as used above.

**The parity of the negation.** The one-particle space carries the representation of the double cover; the scalar $-1$ acts on $S$ as $-\mathrm{id}$. On $\Lambda^nS$ it acts as $(-1)^n$, hence on the whole Fock space as the operator

$$
\boxed{\;\Gamma(-I)=(-1)^{N_{\mathrm{fop}}}=\prod_{\mathrm{modes}}\bigl(I-2N_{\mathrm{mode}}\bigr)\;}
$$

and, for one mode, the same operator on the module is the parent's one-mode parity, multiplication by the element $i\vec u$ at the direction $\vec u$ that the mode declares, so over the modes it is the tensor product of those one-mode actions, each at its own declared direction.

The one-mode identity $(-1)^{N_{\mathrm{mode}}}=i\vec u$ is the parents' statement, read on the one-particle space as multiplication by the element. The operator identity $\Gamma(-I)=(-1)^{N_{\mathrm{fop}}}$ was recomputed on the four-dimensional space $\Lambda S$: $\Gamma(-I)$ built from its action on degrees $0,1,2$ equals the product of the single-mode parities exactly, with eigenvalue list $\{+1,+1,-1,-1\}$ in both constructions.

**The parity and the field.** The field operator, being a sum of one-mode operators, is odd under $\Gamma(-I)$; a bilinear is even. The observable algebra of the field is therefore the even part of the Fock space's operator algebra, and the state space splits into an even and an odd sector that never mix under observables. This is the state-space statement of the field's $\mathbb{Z}/2$ grading.

**The sign convention.** With $N_{\mathrm{mode}}$ the number operator of a mode, $(-1)^{N_{\mathrm{mode}}}$ is the parent's one-mode parity, multiplication by $i\vec u$ at the direction the mode declares, which is $2(\vec u\cdot\tilde S)/\hbar$. The parity is thus both a state-space grading and an element of the algebra's informational sector, for one mode and at a declared direction; for the field, the tensor product over modes is not an element of $\mathbb{B}$, and the grading is external, the open item recorded by the companion article *The Spin–Statistics Theorem in Biquaternionic Form*.

## The Inner Product, States and the Trace Pairing

The Fock space is a Hilbert space under the Hermitian form induced from $S$: the one-particle form extends to $\Lambda S$ by the rule that distinct occupation numbers are orthogonal and the norm of a basis vector is one. The extensions of $a_{\mathrm{fop}}$ and $a_{\mathrm{fop}}^{\dagger}$ to $\Lambda S$ are adjoint with respect to this form, which is the sense in which the Fock construction is $*$-unitary.

The biquaternion content enters through the description of states, and it enters mode by mode. A pure state of the **one-mode** Fock space is a ray, and its state element is the Hermitian idempotent of trace one

$$
\tilde{Ϛ}^2=\tilde{Ϛ},
\qquad
\tilde{Ϛ}^{*}=\tilde{Ϛ},
\qquad
\operatorname{Tr}\tilde{Ϛ}=1 ,
$$

the Bloch element $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ at $\lvert\vec r\rvert=1$, where the direction $\vec r$ is the one the state itself supplies; it is an element of $\mathbb{B}_{\Psi}$. The four-dimensional $\Lambda S$ of the two spin states is not an element of $\mathbb{B}$ and has no state element of the algebra; only its one-mode restrictions do. For one mode, the Born rule is the normalised Hermitian form of the framework, read at normalisation through the trace (*Norm and Pairing Conventions*, §*The Trace and the Normalised State*),

$$
\langle H_{\mathrm{fop}}\rangle_{\tilde{Ϛ}}=\frac{\langle\tilde{Ϛ},H_{\mathrm{fop}}\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}} ,
$$

and the trace reading of the same ratio is the one the conventions fix, since the scalar part and the trace are one reading of the form; the number is a probability, by the positivity of the form. Two remarks fix the interpretation.

First, the state and the observable are both in $\mathbb{B}_{\Psi}$; the material sector $\mathbb{B}_{\Phi}$ carries the anti-Hermitian Lie-algebra generators, the $\vec e_k$ and their multiples, and it carries the *field*, not the states. This is the sector assignment the framework runs on, and the Fock construction respects it, mode by mode.

Second, the trace reading is the *algebraic* trace on $\mathbb{B}$, which for the one-mode Fock space is the Hilbert-space trace of the two-dimensional space. For the four-dimensional $\Lambda S$ the state is not an element of $\mathbb{B}$, and the biquaternion formula applies after restriction to a mode. For the field's Fock space the identification is formal — the Hilbert space is infinite-dimensional and the algebraic trace is not defined — and the framework's finite-algebra formulas are used mode by mode, where the algebra is finite-dimensional. The companion article *The KMS Condition and the Biquaternion Framework* discusses the thermal state on that passage, and the algebraic completion of a finite Fock space is the standard GNS construction; here the finite one-mode statement is what is used.

## What Is Standard and What Is the Algebra's Own

**Standard, transcribed.** The exterior-algebra construction of the fermionic Fock space; the occupation-number basis and Pauli exclusion; the functoriality of $\Lambda$; the Lorentz content $0\oplus\tfrac12\oplus0$ of the two spin states of one momentum; the $2\pi$ sign as the degree parity; the Hilbert-space inner product and the adjointness of $a_{\mathrm{fop}},a_{\mathrm{fop}}^{\dagger}$; the identity $\mathcal{A}_N\cong M_{2^N}(\mathbb{C})$ for the mode algebra. All of this is standard, and it is written in the parents' conventions.

**The algebra's own.**

- *The one-particle space as the space of L parts*, with the two structures on it: the Hermitian form for probabilities and the antisymmetric product for invariants, while the algebra's quaternionic norm degenerates on the whole space and does not descend to it. The distinction is a framework convention and is kept explicit.
- *The one-mode identification of the state space with the algebra's own spin structure*: the one-mode Fock space is two-dimensional and its grading is the degree parity, so for a single ladder the Fock space, the spin tower and the one-mode parity are all statements about $\mathbb{B}$. Over the two spin states of one momentum the state space is the four-dimensional $\Lambda S$, which is not an element of $\mathbb{B}$.
- *The sector assignment of states and observables*, both in $\mathbb{B}_{\Psi}$ for one mode, with the normalised Hermitian form, read through the trace, as the Born rule.

**Open.**

- **The infinite-mode grading.** For the field the grading is external to $\mathbb{B}$; whether an extension of the algebra carries it is the open question the spin–statistics companion records, and it is open here too.
- **The trace pairing off the finite algebra.** The Born rule as a scalar-part ratio is a finite-algebra statement; its extension to the field's Fock space is treated by the GNS and KMS companions and is not settled here.
- **The Lorentz content of the field's Fock space.** The tensor tower is written down mode by mode; its decomposition into irreducible massive representations of the full Poincaré group — the usual multi-particle classification — is standard and is not redone here.

## Companion Articles

- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder, the one-mode vacuum and the fermionic parity read inside the algebra.
- Companion article *The Spin–Statistics Theorem in Biquaternionic Form*, for the fermionic bracket and the external grading that force the antisymmetric state space.
- Companion article *The KMS Condition and the Biquaternion Framework*, for the thermal state and the passage of the finite-algebra form to the field's Fock space.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gamma symbols are used only in this section; every other section writes the same objects as cells. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$; on the regular module a left multiplication is the cell $L_aR_{\mathrm{pau},e_t}$, so the body's $L_{\tilde Q}$ are the cells whose right factor is the unit. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

Each generator is $i$ times a real cell, and multiplying by $i$ trades it back: $i\gamma_0=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}$ and $i\gamma_k=-L_{\mathrm{pau},\vec e_k}R_{\mathrm{pau},\vec e_y}$. Because $i^2=-1$, the square of a generator is minus the square of its cell, $(iL_aR_b)^2=-L_{a^2}R_{b^2}$, and with $e_t^2=e_t$ and $\vec e_k^2=-e_t$ that one line gives both signs of the frame,

$$
\gamma_0^2=-L_{\mathrm{pau},e_t^2}R_{\mathrm{pau},\vec e_x^2}=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},-e_t}=+I_4,
\qquad
\gamma_k^2=-L_{\mathrm{pau},\vec e_k^2}R_{\mathrm{pau},\vec e_y^2}=-L_{\mathrm{pau},-e_t}R_{\mathrm{pau},-e_t}=-I_4,
$$

In the axis-free display:

$$
\gamma_0^2=-L_{\mathrm{axf},e_t^2}R_{\mathrm{axf},\vec e_x^2}=-L_{\mathrm{axf},e_t}R_{\mathrm{axf},-e_t}=+I_4,
\qquad
\gamma_k^2=-L_{\mathrm{axf},\vec e_k^2}R_{\mathrm{axf},\vec e_y^2}=-L_{\mathrm{axf},-e_t}R_{\mathrm{axf},-e_t}=-I_4,
$$

and $\gamma_5^2=-L_{\mathrm{pau},e_t^2}R_{\mathrm{pau},\vec e_z^2}=+I_4$. They obey the anticommutation relations of the frame,

$$
\gamma_\mu\gamma_\nu+\gamma_\nu\gamma_\mu=2g_{\mu\nu}I_4,
\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

with $\varepsilon=(1,-1,-1,-1)$, and the chirality cell is their product,

$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3.
$$

The relations were checked exactly on the cells, where each product is a composition of left and right multiplications, so the check is one of algebra in $\mathbb{B}$ and not of a chosen matrix frame.

A single product is a pure tensor; the products form the seven-dimensional cone $\{M:\operatorname{rank}c(M)\le1\}$, and a general element is a sum of at most four, with its **length** $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality operator. The central grading $\xi_{\mathrm{ad}}=i\tilde{Ζ}_{\mathrm{ad}}$, with $\tilde{Ζ}_{\mathrm{ad}}$ the central root of $-e_t$ and $\xi_{\mathrm{ad}}$ the difference of the two central idempotents of the complexified algebra, so that $\xi_{\mathrm{ad}}^2=e_t$, is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, and the real cells $L_aR_b$, without the central $i$, span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The fermionic Fock space of the biquaternion spin-$\tfrac12$ field, on the particle branch at one momentum, is the exterior algebra over the one-particle space, $\mathcal{F}=\Lambda S$ with $\dim_\mathbb{C}\Lambda S=1+2+1=4$ over the two spin states. The antiparticle branch doubles the one-particle space, and the factor is then sixteen-dimensional. The antisymmetry is forced by the anticommutator, which the spin–statistics companion fixes by the spin. The one-particle space is the complex two-dimensional space of L parts, carrying the positive-definite Hermitian form for probabilities and the antisymmetric product for the Lorentz-invariant bilinears, while the algebra's quaternionic norm degenerates on it and does not descend to it.

The occupation-number basis $|0\rangle,|\!\uparrow\rangle,|\!\downarrow\rangle,|\!\uparrow\downarrow\rangle$ has the wedge product with the Koszul sign, which yields Pauli exclusion. The Lorentz content is

$$
\Lambda S=\mathbb{C}\oplus S\oplus\mathbb{C},
\qquad
0\oplus\tfrac12\oplus0,
$$

with $\hat S^2$ eigenvalues $\{0,\tfrac34,\tfrac34,0\}$ recomputed on the four-dimensional space; the antisymmetric pair is a singlet because a Lorentz rotor — every Lorentz transformation, not only the rotations — has quaternionic norm one, so it carries the two-particle state to itself, with the residual of the antisymmetric-product identity checked on random rotors. The covering element acts as the degree parity, $\Gamma(-e_t)=(-1)^{N_{\mathrm{fop}}}$, recomputed in both constructions. For one mode the parity is the parent's one-mode parity, multiplication by $i\vec u$ at the direction $\vec u$ the mode declares; for the field it is the tensor product over modes and external to $\mathbb{B}$.

The operators generated by the mode operators fill the matrix algebra of the Fock space, $\mathcal{A}_N\cong M_{2^N}(\mathbb{C})$, verified by dimension for $N=1$ (dimension $4$) and $N=2$ (dimension $16$). Pure one-mode states are Hermitian idempotents of $\mathbb{B}_{\Psi}$, the four-dimensional $\Lambda S$ is not an element of $\mathbb{B}$, the observables are even, and the Born rule is the normalised Hermitian form, read through the trace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$ | One-particle space: the L parts of $\mathbb{B}$, of complex dimension two |
| $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ | The Dirac field, an element of $\mathbb{B}$, and its two values |
| $\zeta\wedge\eta$ | The antisymmetric product of *Product and Form Conventions* read on $S$; its values are the pure L parts, one complex dimension |
| $\langle\cdot,\cdot\rangle_{*}$ | The Hermitian form, restricted to $S$; positive definite, and the Hilbert-space form of the construction |
| $\langle\tilde Q\rangle_{\natural}$ | The quaternionic norm on $\mathbb{B}$; it vanishes on every L part and does not descend to $S$ |
| $\mathcal{F}=\Lambda S$ | Fermionic Fock space |
| $\lvert 0\rangle,\lvert\!\uparrow\rangle,\lvert\!\downarrow\rangle,\lvert\!\uparrow\downarrow\rangle$ | Occupation-number basis; $\dim_\mathbb{C}\mathcal{F}=4$ |
| $q_1\wedge q_2=(-1)^{\lvert q_1\rvert\,\lvert q_2\rvert}q_2\wedge q_1$ | Graded-commutative wedge (Koszul sign) |
| $N_{\mathrm{fop}}$, $a_{\mathrm{fop}},a_{\mathrm{fop}}^{\dagger}$ | Number operator; one-mode ladder |
| $\Gamma(\rho)=\bigoplus_n\Lambda^n\rho$ | Exterior-power (Fock) functor |
| $\Lambda S=\mathbb{C}\oplus S\oplus\mathbb{C}$ | Lorentz content of the two spin states of one momentum: $0\oplus\tfrac12\oplus0$ |
| $\hat S_i=\Gamma(\tilde S_i)$ | Spin operators on $\Lambda S$, the images of $\tilde S_i=\tfrac{\hbar}{2}i\vec e_i$, in units $\hbar=1$ |
| $\Gamma(-I)=(-1)^{N_{\mathrm{fop}}}$ | Degree parity; $2\pi$ rotation on the Fock space |
| $(-1)^{N_{\mathrm{mode}}}=i\vec u$ (one mode) | Parity as the element $i\vec u$ at the declared direction, acting by $Q\mapsto i\vec uQ$ |
| $\mathcal{A}_N\cong M_{2^N}(\mathbb{C})$ | Mode algebra of $N$ fermionic modes |
| $\tilde{Ϛ}^2=\tilde{Ϛ}=\tilde{Ϛ}^{*}$, $\operatorname{Tr}\tilde{Ϛ}=1$ | One-mode pure state, the Bloch element $\tfrac12(e_t+i\vec r)$ at $\lvert\vec r\rvert=1$; the four-dimensional $\Lambda S$ has no state element of the algebra |
| $\langle H_{\mathrm{fop}}\rangle_{\tilde{Ϛ}}=\langle\tilde{Ϛ},H_{\mathrm{fop}}\rangle_{*}/\langle\tilde{Ϛ},e_t\rangle_{*}$ | Born rule for one mode: form first, trace at normalisation last |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, and "A theory of electrons and protons," *Proceedings of the Royal Society A* **126** (1930) 360–365, for the field and the hole picture whose state space this article constructs.
- P. Jordan and E. Wigner, "Über das Paulische Äquivalenzverbot," *Zeitschrift für Physik* **47** (1928) 631–651, for the antisymmetric occupation-number construction and its relation to spin systems.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Fock-space construction of the Dirac field and the anticommutation relations.
- F. A. Berezin, *The Method of Second Quantization* (Academic Press, 1966), for the exterior algebra, the Koszul sign, and the Grassmann coherent states used in the companion articles.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Lorentz decomposition of the one- and two-particle states.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the anticommutation relations and the Pauli exclusion principle in the convention used here.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic (GNS) construction of the state space as a completion of the finite Fock space.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for minimal left ideals, the exterior algebra over a one-particle space, and the identification of the algebra with the fermionic mode algebra.
- J.-P. Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the exterior-power functor and the exterior algebra as a representation.
