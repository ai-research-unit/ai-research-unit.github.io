# __Spin and the Three Elementary Carriers in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries exactly three kinds of subspace that a field can occupy and that its own multiplications preserve: the centre, the minimal left ideals, and the material sector. Their spins are $0$, $\tfrac12$ and $1$. That list is the article's subject, and it is also its definition: **the spin of a field is the spin of its carrier**, and the spin of a carrier is read from the dimension of the representation space the carrier holds.

**Why the definition is stated this way and not as a highest weight.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, so it has one isomorphism class of simple modules. A label attached to a module therefore cannot distinguish three spins: one module serves two of them, and the third is not a module at all. The algebra has three carriers and one module, so the label attaches to the carrier. The highest weight is then a *reading* of the carrier, and it is the reading this article develops in full once the carriers are in place.

**What the article does.** It names the three carriers and their spins (§*The Three Carriers*), states the definition and the arithmetic behind it (§*The Spin Is the Dimension of the Carrier*), and then treats each carrier in turn: the centre for spin $0$, the ideals for spin $\tfrac12$, the material sector for spin $1$. It also settles which of the two sectors is the carrier, since the two hold the same representation and only the material one is closed under the commutator (§*Why the Material Sector and Not the Informational One*). The generators, the Casimir, the ladder and the classification follow as the machinery that computes the spin once the carrier is named. The article closes with the addition of angular momenta, the tensor products and the five uses of the word spin.

**The two actions.** Only two multiplications of the algebra make a subspace a carrier. Left multiplication acts irreducibly on each minimal left ideal and reducibly on the rest. Conjugation by the unit real quaternions — the adjoint action — fixes the centre and acts on the traceless part as the vector representation, that is, as spin one. Every carrier of this article is a carrier for one of those two actions, and the pair of them is the whole of the algebra's spin content. The second action preserves both sectors and gives them the same representation, so the spin does not choose between them. The commutator does: the material sector is closed under it and the informational one is not.

**What no carrier carries.** No subspace of $\mathbb{B}$ carries spin $\tfrac32$ or spin $2$. The tensor square of the adjoint module does contain a spin-two summand, and the multiplication map kills it; the article proves that vanishing, since it is the reason the list stops where it does. A field of higher spin is a field with more than one index, built by tensoring the spin-$\tfrac12$ module and imposing a constraint, and it is not a subspace of the algebra.

**No scale enters.** Every operator below is $\tilde S_k=\tfrac12 i\vec e_k$, and every weight, every bracket and the Casimir are fixed by the multiplication of $\mathbb{B}$; the article carries no constant beside the elements. It is the pure-mathematical counterpart of *Spin and the Three Elementary Carriers* in the physics corpus, which names the same three carriers and reads them physically, and of *Angular Momentum and Spin in Biquaternionic Form*, which carries the units.

## The Algebra and Its Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and the multiplication

$$
\vec e_k^2=-e_t,\qquad \vec e_\mu\vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda\quad(\mu\neq\nu),
$$

so that $\vec e_x\vec e_y=\vec e_z$ and $\vec e_y\vec e_x=-\vec e_z$. The matrix model is fixed by

$$
\mathsf{M}_2(e_t)=I_2,\qquad \mathsf{M}_2(\vec e_k)=-i\sigma_k,\qquad \mathsf{M}_2(i)=iI_2,
$$

with $\sigma_k$ the Pauli matrices. It follows that $\mathsf{M}_2(i\vec e_k)=\sigma_k$. The conjugation is the anti-automorphism

$$
e_t^*=e_t,\qquad \vec e_k^*=-\vec e_k,\qquad i^*=-i,
$$

and $\mathsf{M}_2(X^*)=\mathsf{M}_2(X)^\dagger$. The two sectors are

$$
\mathbb{B}_{\Psi}=\operatorname{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\},\qquad
\mathbb{B}_{\Phi}=\operatorname{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\},
$$

the Hermitian and anti-Hermitian subspaces; $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ and $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$.

The trace form is

$$
\langle X,Y\rangle=\operatorname{tr}(X^*Y),
$$

with $\operatorname{tr}$ the matrix trace. It is positive definite and $\mathbb{C}$-linear in $Y$. The group of unit real quaternions is

$$
G=\{u\in\mathbb{B}_{H}:uu^*=e_t\},
$$

which is $SU(2)$; its Lie algebra is $\mathfrak{g}=\mathbb{B}_{H}\cap\mathbb{B}_{\Phi}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, with bracket $[\vec e_\mu,\vec e_\nu]=2\epsilon_{\mu\nu\lambda}\vec e_\lambda$. The complexification $\mathfrak{g}_{\mathbb{C}}=\operatorname{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$ is $\mathfrak{sl}_2(\mathbb{C})$, the traceless part under $\mathsf{M}_2$.

**Proposition.** $\mathsf{M}_2$ is an isomorphism of complex algebras, carries $*$ to the conjugate transpose, and carries the trace form to the Hilbert–Schmidt form.

*Proof.* The map is defined on the basis; on products of basis elements it is the standard Pauli multiplication, so it is an algebra homomorphism. The correspondence $*$ to the conjugate transpose is checked on the basis: $\mathsf{M}_2(\vec e_k^*)=\mathsf{M}_2(-\vec e_k)=i\sigma_k=(-i\sigma_k)^\dagger$. The trace form is then $\operatorname{tr}(\mathsf{M}_2(X)^\dagger\mathsf{M}_2(Y))$, the Hilbert–Schmidt form.

## The Three Carriers

**Definition (carrier and carrier type).** A **carrier** is a nonzero subspace $W\subseteq\mathbb{B}$ invariant under one of the algebra's own actions, left multiplication or conjugation by $G$. Its **representation space** is its irreducible part: $W$ itself when the action is irreducible on $W$, and the traceless part when the action fixes a line inside $W$. Its **type** is the isomorphism class of that representation space, and a carrier is **elementary** when that space is irreducible. A carrier of one type contained in a carrier of the same type is a **sub-carrier** of it, and two carriers of one type are **copies**. The action is part of the carrier, because the same subspace can be reducible for one and irreducible for the other.

The algebra has three elementary types, and no more. They are the whole of the spin content of $\mathbb{B}$. **It is the types that are three and not the spaces**: the third line below is the material sector, and the informational sector is a second carrier of the same type. §*Why the Material Sector and Not the Informational One* settles which of the two the article takes.

| carrier | type | set | $\dim_{\mathbb{R}}$ | $\dim_{\mathbb{C}}$ | action | representation space | spin |
|---|---|---|---|---|---|---|---|
| the centre $\mathbb{B}_{C}$ | $\mathcal{V}_0$ | $\mathbb{C}e_t$ | $2$ | $1$ | conjugation; fixed pointwise | $\mathbb{C}e_t$ | $0$ |
| the ideals $S_\pm$ | $\mathcal{V}_1$ | $\mathbb{B}\tilde\Pi_\pm$ | $4$ | $2$ | left multiplication | $S_\pm$ | $\tfrac12$ |
| the material sector $\mathbb{B}_{\Phi}$ | $\mathcal{V}_2$ | $\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ | $4$ | — | conjugation | $\mathfrak{k}$, the traceless part | $1$ |

Two of the three are irreducible as they stand. The third is one real dimension larger than its representation space, and the extra dimension is the fixed line $\mathbb{R}(ie_t)$, which carries the trivial representation beside the triplet. Nothing is lost by the enlargement and nothing is gained: the spin is the dimension of the representation space. The list gives one carrier for each type, so a sub-carrier of a listed carrier is not a further entry: the line and $\mathfrak{k}$ are the two pieces of the third, and the content is the triplet's.

**The centre.** $\mathbb{B}_{C}=\mathbb{C}e_t$ is the fixed space of the adjoint action: $ue_tu^*=e_t$ for every unit $u$. It is a carrier of the adjoint action in the degenerate sense that the action is trivial on it, and its representation space is one-dimensional.

**The ideals.** For a unit real axis $\vec u$ and $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$, the set $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$ is a minimal left ideal: left multiplication acts on it irreducibly and it has no invariant left subspace. The axis is a parameter of the family and not a datum of the algebra. It is four real dimensions, two complex. Both ideals occur, the algebra distinguishes neither, and $\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u)$. The two are module-isomorphic, and the isomorphism is inner: right multiplication by the mixed unit $\vec\Upsilon_{+-}(\vec u)$ carries $S_+(\vec u)$ onto $S_-(\vec u)$.

**The material sector.** $\mathbb{B}_{\Phi}$ is the anti-Hermitian subspace, four real dimensions, and it is not a complex subspace: multiplication by $i$ carries it to $\mathbb{B}_{\Psi}$. Under conjugation it splits as

$$
\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k},\qquad \mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},
$$

because $u(ie_t)u^*=ie_t$ and $u\vec vu^*$ is again a real pure quaternion. The first summand is one-dimensional and the second is three-dimensional; the three-dimensional summand carries the vector representation, and that is the spin-one space.

The split is a split of Lie algebras, not only of modules. The triple is closed under the commutator, $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, because $[\vec e_\mu,\vec e_\nu]=2\epsilon_{\mu\nu\lambda}\vec e_\lambda$ is real, and $ie_t$ is central in $\mathbb{B}$ and hence central in the sector. So $\mathbb{B}_{\Phi}$ is closed under the commutator as well, and as a real Lie algebra it is a direct sum, $\mathbb{B}_{\Phi}\cong\mathfrak{u}(1)\oplus\mathfrak{su}(2)$, with both summands ideals. The spin-one space is the derived algebra: $[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]=\mathfrak{k}$.

**Three and not four.** The classification is the classification of the left ideals of $M_2(\mathbb{C})$ together with the isotypic decomposition of the adjoint action, and both are complete: a left ideal is a sum of columns, the minimal ones are single columns, and the adjoint action on $\mathbb{B}$ has exactly the two isotypic components $Z$ and $V$. A fourth type would have to be a fourth isotypic component, and there is none. The two sub-carriers of the sector are not a fourth and a fifth: they are the two pieces of the third, and the type belongs to the triplet. §*The Spectrum and the Criterion* states the same fact as a dimension count.

**Two invariants, and the carrier fixes one.** The two elementary invariants of an element are

$$
N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

the quaternionic norm and the vector square. On the ideals $N=0$ identically, because $\tilde\Pi_\pm^{\natural}=\tilde\Pi_\mp$ and $\tilde\Pi_+\tilde\Pi_-=0$. On the centre $B^2=0$ identically. On the material sector both are free. So the carrier decides where in the partition by $(N,B^2)$ a field's values can fall, and that partition is the subject of *The Three Elementary Carriers and the Four Sectors of Regularity and Degeneracy* in the physics corpus. The chain runs one way: spin, carrier, invariants, region.

### Why the Material Sector and Not the Informational One

**The objection first.** Conjugation by $G$ preserves Hermiticity exactly as it preserves anti-Hermiticity, and $i$ is central and commutes with it, so the two sectors are exchanged by multiplication by $i$, $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$. The partner splits in the same way, $\mathbb{B}_{\Psi}=i\mathbb{B}_{\Phi}=\mathbb{R}e_t\oplus i\mathfrak{k}$, and it carries the same $1\oplus0$ under conjugation. Nothing in the action, in the weights or in the Casimir separates the two sectors, and a reader who swaps the letters keeps every spin of this article.

**What separates them is the commutator.** The material sector is closed under it and the informational sector is not. On $\mathbb{B}_{\Phi}$ the bracket stays inside the sector, $[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]=\mathfrak{k}$; on $\mathbb{B}_{\Psi}$ it does not, because $[\mathbb{B}_{\Psi},\mathbb{B}_{\Psi}]=\mathfrak{k}$ as well and $\mathfrak{k}$ lies outside $\mathbb{B}_{\Psi}$, the two sectors being complementary, $\mathbb{B}_{\Phi}\cap\mathbb{B}_{\Psi}=0$. No bracket of two Hermitian elements is Hermitian. So $\mathbb{B}_{\Phi}$ is the real Lie algebra $\mathfrak{u}(2)$, and $\mathbb{B}_{\Psi}$ is not a Lie algebra at all.

**The generators are in the material sector.** The anti-Hermitian normalisation of the rotation generators, $g_k=-\tfrac12\vec e_k$, is an element of $\mathbb{B}_{\Phi}$; the Hermitian one is $i$ times it, $\tilde S_k=-i g_k$, and lies in $\mathbb{B}_{\Psi}$. The sector that holds the Lie algebra of the group is the material one, and on the triplet the action is the adjoint action of that Lie algebra on itself; that is the sense in which the spin sits in $\mathbb{B}_{\Phi}$ and not in its partner. The informational sector holds $i$ times the algebra and is where the group acts, not where it lives.

**The letter follows the sector, and that part is a convention.** The two tokens are the corpus's, $\varphi$ material and $\psi$ informational (*Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces*), and the spin-one carrier takes the letter of the sector it is. The choice of $\Phi$ is a convention with a warrant and not a theorem: the warrant is the closure under the commutator, and the convention is the reading, in which the four-vectors and the momenta live in $\mathbb{B}_{\Phi}$. A page that reads its states in $\mathbb{B}_{\Psi}$ and calls that sector the carrier makes no algebraic error; it changes the reading and keeps the spin.

## The Spin Is the Dimension of the Carrier

**Definition (spin).** Let $W$ be a carrier, let $\rho$ be its action, and let $V_W\subseteq W$ be the representation space the action generates — for the adjoint action on the material sector, the traceless part; for the two other carriers, the carrier itself. The **spin** of $W$ is

$$
s=\frac{\dim_{\mathbb{C}}V_W-1}{2},
$$

so that $\dim_{\mathbb{C}}V_W=2s+1$. The spin is a scalar label, not a vector, and it takes the values $0,\tfrac12,1$ on the three carriers.

**The arithmetic, carrier by carrier.** The centre has $\dim_{\mathbb{C}}=1$ and $s=0$. An ideal has $\dim_{\mathbb{C}}=2$ and $s=\tfrac12$. The material sector is not a complex space, and its traceless part $\mathfrak{k}$ is three real dimensions; complexified, $V=\mathfrak{k}_{\mathbb{C}}$ has complex dimension $3$ and $s=1$.

**Why the third carrier needs the subtraction.** $\mathbb{B}_{\Phi}$ is four-dimensional and the spin-one space is three-dimensional, and the difference is one entry: the component along $ie_t$, that is, the scalar part. That component is not a defect of the counting. It is the scalar admixture that a vector field carries before its field equation removes it, and the removal is the Proca constraint in the physics corpus. The carrier holds four components and the spin uses three, and a reader who forgets the subtraction gets a carrier of dimension four and a spin $s=\tfrac32$ that no field has.

**Dimension alone does not give the spin.** Two of the three carriers are four real-dimensional, and their spins are $\tfrac12$ and $1$. What separates them is the action and the invariant line: left multiplication has no invariant line inside $S_\pm$, and the adjoint action on $\mathbb{B}_{\Phi}$ has one, the line of $ie_t$. So the definition is the dimension *of the representation space*, not the dimension of the carrier, and the difference between the two is exactly the trivial summand.

**The definition is not a label of an element.** An element has whatever carrier its field has. The same element can be read in two carriers when the two meet, and they meet on the line $\mathbb{R}(ie_t)=\mathbb{C}e_t\cap\mathbb{B}_{\Phi}$, shared by the centre and the material sector, and on the lines $\mathbb{R}\bigl(i\tilde\Pi_\pm(\vec u)\bigr)$, shared by the ideals and the material sector. The corpus uses both coincidences: $i\tilde\Pi_\pm(\vec u)$ is at once a lightlike four-vector and a spinor value, and $ie_t$ is at once the scalar and the timelike four-vector.

**The definition is not a label of a module either.** There is one simple module, and the carriers are three. A module statement can say $\tfrac12$; it can say $\tfrac12$ any number of times; it cannot say $0$ or $1$ except by leaving the module category, which is what the centre and the adjoint action do.

## The Rotation Generators

The Lie algebra has the anti-Hermitian basis

$$
g_k=-\tfrac12\vec e_k\in\mathfrak{g},\qquad [g_i,g_j]=-\epsilon_{ijk}g_k,\qquad g_k^*=-g_k,
$$

and the Hermitian basis

$$
\tilde S_k=\tfrac12 i\vec e_k\in\mathbb{B}_{\Psi},\qquad [\tilde S_i,\tilde S_j]=i\epsilon_{ijk}\tilde S_k,\qquad \tilde S_k^*=\tilde S_k.
$$

They are related by $\tilde S_k=-ig_k$. The bracket of the $\tilde S_k$ is the standard angular-momentum relation; the bracket of the $g_k$ is its anti-Hermitian form. The triple is read as one vector, $\vec S$ with components $\tilde S_k$, so that $\vec u\cdot\vec S=u_k\tilde S_k$ for a unit $\vec u$; the glyph is arrowed and carries no tilde, because each component is a pure element (*Algebra and Element Conventions*, §*The Centre and the Vector Subspace*).

**Proposition (the exponential).** For a unit $\vec u\in\mathfrak{g}$ and real $\theta$, the rotation through $\theta$ about $\vec u$ is

$$
\exp(-\theta\,\vec u\cdot\vec g)=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u\cdot\vec e
=\exp(-i\theta\,\vec u\cdot\vec S),
$$

a unit real quaternion, whose adjoint action turns a vector through $+\theta$ about $\vec u$.

*Proof.* The element $\vec u\cdot\vec e$ is a pure real quaternion with square $-e_t$, so the power series splits into the cosine and sine series. The two expressions agree because $\tilde S_k=-ig_k$. The sense of the turn is that of $\operatorname{Ad}_{\tilde q}$ for $\tilde q=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\vec u$ (*Quaternion Rotations and Reflections*, §*The Adjoint Action*), which is the same element.

The group generated is $G=SU(2)$, which is the double cover of $SO(3)$.

**The action on a carrier.** A carrier is a pair $(W,\rho)$ with $W$ a finite-dimensional complex space and $\rho$ either an algebra homomorphism $\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(W)$ or a Lie-algebra homomorphism $\mathfrak{g}\to\operatorname{End}_{\mathbb{C}}(W)$. In the first case the generator acts as $\rho(\tilde S_k)$ with $\tilde S_k\in\mathbb{B}$; in the second, $\rho$ extends $\mathbb{C}$-linearly to $\mathfrak{g}_{\mathbb{C}}$ and again $\rho(\tilde S_k)$ is defined. The two cases are kept apart: only the first is a module over the associative algebra. A carrier is **unitary** when $\rho(X^*)=\rho(X)^\dagger$ in the algebra case, equivalently $\rho(X)^\dagger=-\rho(X)$ for $X\in\mathfrak{g}$ in the Lie case. The carriers of this article are unitary for the trace form.

**Lemma (self-adjointness).** For $X\in\mathbb{B}$, the adjoint of $\operatorname{ad}_X$ with respect to the trace form is $\operatorname{ad}_{X^*}$.

*Proof.* Using $\operatorname{tr}((XY-YX)^*Z)=\operatorname{tr}((X^*Z-ZX^*)Y)$ by cyclicity and $(XY)^*=Y^*X^*$, one gets $\langle\operatorname{ad}_X Y,Z\rangle=\langle Y,\operatorname{ad}_{X^*}Z\rangle$.

Consequently $\operatorname{ad}_{\tilde S_k}$ is self-adjoint and $\operatorname{ad}_{g_k}$ is skew-adjoint; $L_{\tilde S_k}$ is self-adjoint on the defining module.

**The generator is the same object on all three carriers.** Fix a unit $\vec u$ and take $\tilde S(\vec u)=\vec u\cdot\vec S$; no axis is preferred by the algebra, and any unit will do. It acts on the centre as $0$, on each ideal with the eigenvalues $\pm\tfrac12$, and on the material sector with the eigenvalues $0,\pm1$. One element, one axis, three carriers, three spectra. That is the whole of the difference between the spins, and the sections that follow compute the three spectra.

## The Spin-Zero Carrier: the Centre

Let $Z=\mathbb{C}e_t=\mathbb{B}_{C}$.

**Proposition.** $Z$ is fixed by the adjoint action, its Casimir is $0$, and its spin is $0$.

*Proof.* For $u\in G$, $ue_tu^*=uu^*e_t=e_t$, since $e_t$ is central. The generator acts as $\operatorname{ad}_{\tilde S(\vec u)}e_t=0$ for every unit $\vec u$, so every weight is $0$ and the Casimir, $\sum_k\operatorname{ad}_{\tilde S_k}^2$, vanishes on $Z$. With $\dim_{\mathbb{C}}Z=1$ the definition gives $s=0$.

**What the spin-zero carrier is not.** It is not a module under left multiplication: $L_{\tilde Q}Z=\mathbb{C}\tilde Q$, which is $\mathbb{B}$ for a unit $\tilde Q$, not a line. The centre is a carrier of the adjoint action only. That asymmetry is why the corpus's physics states that a scalar field "escapes the state module", and the algebraic content is the one line above: the scalar is not in the module, it is in the centre.

**The invariant.** $B^2=0$ on $Z$ identically, while $N$ is free: $N(Q_te_t)=Q_t^2$. The centre is therefore the carrier whose values sit on the axis of the partition, and the point $e_t$ is the only member of $Z$ with $N\neq0$ up to scale.

## The Spin-Half Carrier: the Two Ideals

**No axis is chosen.** A minimal left ideal is $\mathbb{B}\tilde\Pi$ for an idempotent, and every idempotent of this algebra is built from a direction, $\tilde\Pi_+(\vec u)=\tfrac12(e_t+i\vec u)$. There is therefore no such thing as *the* minimal left ideal, only the sphere of them. A section that writes the one at $\vec e_z$ and calls it the carrier has replaced a family by a member of it. The family is the object, the member is a coordinate, and this section is written at a unit $\vec u$.

The rule is the one of *Why AXF Matrices instead of Pauli and Gamma Matrices*, §*Why the Third Matrix Is the Diagonal One*: the third of the three Pauli arrays is the diagonal one because $\vec e_z$ built the idempotents of the display, and the diagonal is the footprint of that choice and not a property of $\vec e_z$. The defect also appears in words. A sentence that reads "$w_+=\tilde\Pi_+$ and $w_-=\tfrac12(i\vec e_x+\vec e_y)$" looks like a statement about the algebra and is a statement about a frame.

**The operator and the module.** The generator is one element per direction, $\tilde S(\vec u)=\vec u\cdot\vec S=\sum_k u_k\tilde S_k$, with $\tilde S_k=\tfrac12 i\vec e_k$. The operator carries the tilde; the module and its ideals do not, and are written $S$ and $S_\pm(\vec u)$.

**The carrier.** For unit real $\vec u$,

$$
\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u),\qquad S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u).
$$

$\tilde\Pi_\pm(\vec u)$ is an idempotent of trace $1$ and rank one, the two are orthogonal, $\tilde\Pi_+(\vec u)\tilde\Pi_-(\vec u)=0$, and they sum to the identity, $\tilde\Pi_+(\vec u)+\tilde\Pi_-(\vec u)=e_t$. Hence

$$
\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u),
$$

with the two summands orthogonal for the trace form, isomorphic as $\mathbb{B}$-modules, and each a minimal left ideal, hence a simple module, of complex dimension $2$. They are two carriers of one spin, not two spins.

**A basis, and what it costs.** A basis of $S_+(\vec u)$ needs coordinates, and coordinates need a frame. Let $(\vec u,\vec v,\vec w)$ be a right-handed orthonormal frame of the rotation algebra, $\vec u\times\vec v=\vec w$. Then

$$
w_+(\vec u)=\tilde\Pi_+(\vec u),\qquad w_-(\vec u)=\vec\Upsilon_{-+}(\vec u)=\tfrac12(i\vec v+\vec w)
$$

is a basis of $S_+(\vec u)$, with $\vec\Upsilon_{-+}(\vec u)$ a nonzero element of the mixed line $\mathbb{B}_{-+}$. **The module depends on the axis $\vec u$ alone; the basis depends on the axis and on the frame $(\vec v,\vec w)$.** The axis is a parameter of a family that the algebra itself supplies, and the frame is a choice a page makes; only the second carries a direction that no statement needs.

**The generators on the basis.** Write $\tilde S_\pm(\vec u)=\vec v\cdot\vec S\pm i\,\vec w\cdot\vec S$. Then

$$
[\tilde S(\vec u),\tilde S_\pm(\vec u)]=\pm\tilde S_\pm(\vec u),\qquad [\tilde S_+(\vec u),\tilde S_-(\vec u)]=2\tilde S(\vec u),
$$

and on the basis

$$
\tilde S(\vec u)w_\pm(\vec u)=\pm\tfrac12 w_\pm(\vec u),\qquad
\tilde S_+(\vec u)w_+(\vec u)=0,\qquad
\tilde S_-(\vec u)w_+(\vec u)=w_-(\vec u),
$$

$$
\tilde S_+(\vec u)w_-(\vec u)=w_+(\vec u),\qquad
\tilde S_-(\vec u)w_-(\vec u)=0.
$$

**The weight is the axis's and the ladder is the frame's.** Rotate the pair $(\vec v,\vec w)$ inside the plane orthogonal to $\vec u$ through an angle $\theta$: the two weights and the two weight vectors are unchanged, while $\tilde S_\pm(\vec u)$ is multiplied by the phase $e^{\mp i\theta}$. So $\tilde S_+(\vec u)$ and $\tilde S_-(\vec u)$ are not structure of the module but a frame written as an operator, and a reader who takes them for intrinsic has fixed a frame without saying so — the same defect, one level down. What is intrinsic is the pair of weight vectors and the two weights.

**Proposition.** On $S_+(\vec u)$, for every unit $\vec u$, the Casimir is $C=\tfrac34 e_t$ and the spin is $s=\tfrac12$.

*Proof.* The weights are $\pm\tfrac12$ at every axis, so the representation space is two-dimensional and the definition gives $s=\tfrac12$ and $C=s(s+1)=\tfrac34$. Directly, each generator squares to a central element, $\tilde S_k^2=\tfrac14 e_t$, so

$$
(\tilde S_1^2+\tilde S_2^2+\tilde S_3^2)w_+(\vec u)=\tfrac34 w_+(\vec u)
$$

for every $\vec u$, because $e_t$ acts as the identity on the module. No axis enters the computation, which is why the number is one number and not one per axis.

**Proposition (the states in the two copies).** The idempotent $\tilde\Pi_+(\vec u)$ is the weight $+\tfrac12$ vector of $S_+(\vec u)$, and $\tilde\Pi_-(\vec u)$ is the weight $-\tfrac12$ vector of $S_-(\vec u)$. That is,

$$
(\vec u\cdot\vec S)\tilde\Pi_+(\vec u)=+\tfrac12\tilde\Pi_+(\vec u),\qquad
(\vec u\cdot\vec S)\tilde\Pi_-(\vec u)=-\tfrac12\tilde\Pi_-(\vec u).
$$

*Proof.* $(\vec u\cdot\vec S)\tilde\Pi_+(\vec u)=\tfrac12(i\vec u)\tfrac12(e_t+i\vec u)=\tfrac12\tilde\Pi_+(\vec u)$, because $(i\vec u)^2=+e_t$ and $i\vec u$ commutes with $\tilde\Pi_+(\vec u)$. The other sign is the same computation with $\vec u$ replaced by $-\vec u$.

**Each lies in its own copy.** The two vectors are not two vectors of one module: $\tilde\Pi_+(\vec u)$ lies in $S_+(\vec u)$ and $\tilde\Pi_-(\vec u)$ in $S_-(\vec u)$, and the two copies are distinct ideals. In $S_+(\vec u)$ the weight $-\tfrac12$ vector is $\vec\Upsilon_{-+}(\vec u)$, and it is nilpotent for every $\vec u$, because the two units of a right-handed frame anticommute and their cross terms therefore cancel:

$$
\vec\Upsilon_{-+}(\vec u)^2=\tfrac14\bigl(\vec v+i\vec w\bigr)^2=\tfrac14\bigl(\vec v^2+i(\vec v\vec w+\vec w\vec v)+(i\vec w)^2\bigr)=\tfrac14\bigl(-e_t+0+e_t\bigr)=0,
$$

Nilpotence is the axis-free statement; the axis appears only when the letter $\vec\Upsilon_{-+}$ is written out. That is the reason the two signs label two copies and not a doublet.

**Proposition (the sphere of minimal left ideals).** The map $\vec u\mapsto S_+(\vec u)$ is a bijection from the unit sphere of the rotation algebra onto the set of minimal left ideals of $\mathbb{B}$.

*Proof.* The minimal left ideals of $M_2(\mathbb{C})$ are the sets of matrices whose rows lie in a fixed line of $\mathbb{C}^2$, and the lines are parametrised by $\mathbb{CP}^1\cong S^2$. The idempotent $\tilde\Pi_+(\vec u)$ is the orthogonal projection onto the $+1$ eigenspace of the Hermitian generator in the direction $\vec u$, and $\vec u\mapsto$ that line is the standard identification.

**The invariant.** $N=0$ on both ideals identically: $\tilde\Pi_+(\vec u)^{\natural}=\tilde\Pi_-(\vec u)$, so $\tilde\Pi_+(\vec u)\tilde\Pi_+(\vec u)^{\natural}=\tilde\Pi_+(\vec u)\tilde\Pi_-(\vec u)=0$, and every member is $\tilde Q\tilde\Pi_+(\vec u)$ with $\tilde Q\tilde\Pi_+(\vec u)\tilde\Pi_-(\vec u)\tilde Q^{\natural}=0$. The ideals are the carrier of the degenerate values of $N$, and no ideal holds a member with $N\neq0$.

**The double cover.** On $S_+(\vec u)$, $\exp(-2\pi i\tilde S(\vec u))=-e_t$ for every $\vec u$. On the adjoint carrier of the next section, $\exp(-2\pi i\operatorname{ad}_{\tilde S(\vec u)})=\operatorname{id}$. The first is the spinor sign and the second is the vector sign; the algebra produces both, and the difference is the parity of the weights, not a property of the axis.

*Proof.* The eigenvalues of $\tilde S(\vec u)$ on $S_+(\vec u)$ are $\pm\tfrac12$, so the exponential is $e^{\pm\pi i}=-1$. The eigenvalues of $\operatorname{ad}_{\tilde S(\vec u)}$ on $\mathbb{B}$ are $0,\pm1$, so the exponential is $1$.

**The instance.** One axis, given once so that the letters of this article can be matched to the corpus's older pages, and flagged as one: at $\vec u=\vec e_z$ with $(\vec v,\vec w)=(\vec e_x,\vec e_y)$,

$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y),\qquad
\tilde S_3w_\pm=\pm\tfrac12 w_\pm,\qquad
\tilde S_+=\tfrac12\bigl(i\vec e_x-\vec e_y\bigr).
$$

Nothing in this section needs it, and no result changes if the axis is moved: $\vec e_z$ is the unit that builds this display and is otherwise one of three. The corpus's older pages write the weight $-\tfrac12$ vector of $S_+(\vec e_z)$ as $w_-=\tfrac12(i\vec e_x+\vec e_y)$; the same vector at another axis is $\vec\Upsilon_{-+}(\vec u)$, and the statement that it is nilpotent is the statement that survives the change.

## The Spin-One Carrier: the Material Sector

Conjugation, $X\mapsto uXu^{-1}$, makes $\mathbb{B}$ a module over $G$, and on the Lie algebra a module over $\mathfrak{g}$. The action of $a\in\mathfrak{g}_{\mathbb{C}}$ is $\operatorname{ad}_a$. On the material sector the action preserves

$$
\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k},\qquad \mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},
$$

so the sector is a carrier of the adjoint action with one invariant line and one irreducible three-dimensional complement. Over $\mathbb{C}$ the same decomposition is written

$$
\mathbb{B}=Z\oplus V,\qquad Z=\mathbb{C}e_t,\qquad V=\ker\operatorname{tr}=\operatorname{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\},
$$

with $Z\cong\mathcal{V}_0$ and $V\cong\mathcal{V}_2$. There is no preferred axis here either, so the weight basis is written at a unit $\vec u$ and a right-handed orthonormal frame $(\vec u,\vec v,\vec w)$:

$$
v_+(\vec u)=\vec v+i\vec w,\qquad v_-(\vec u)=\vec v-i\vec w,\qquad v_0(\vec u)=\vec u,
$$

with

$$
[\tilde S(\vec u),v_\pm(\vec u)]=\pm v_\pm(\vec u),\qquad [\tilde S(\vec u),v_0(\vec u)]=0,
$$
$$
[\tilde S_+(\vec u),v_+(\vec u)]=0,\qquad [\tilde S_-(\vec u),v_+(\vec u)]=-2v_0(\vec u),\qquad [\tilde S_-(\vec u),v_0(\vec u)]=v_-(\vec u).
$$

The three vectors are the frame's and the weights are the axis's; the module is the whole of $V$ and needs neither. At $\vec u=\vec e_z$ with $(\vec v,\vec w)=(\vec e_x,\vec e_y)$ this is the display $v_\pm=\vec e_x\pm i\vec e_y$, $v_0=\vec e_z$ of the corpus's older pages.

**Proposition.** On $Z$ the Casimir is $0$ and the spin is $0$; on $V$ the Casimir is $2$ and the spin is $1$, so the material sector has spin $1$ on its traceless part and $0$ on its trace.

*Proof.* The weights of $V$ are $\pm1,0$, so the representation space is three-dimensional and the definition gives $s=1$ and $C=s(s+1)=2$. Directly, $\sum_k\operatorname{ad}_{\tilde S_k}^2$ acts on $v_+(\vec u)$ as $2v_+(\vec u)$ and on $v_0(\vec u)$ as $2v_0(\vec u)$, for every frame. The line $\mathbb{R}(ie_t)$ is fixed by the same argument as the centre.

**The third carrier is real and the representation is complexified.** $\mathbb{B}_{\Phi}$ is not a complex subspace, so the weights $\pm1,0$ belong to the complexified picture. §*Real Forms and the Rotation Subgroup* separates the two: the real carrier is $\mathfrak{k}$, and the complex carrier $\mathcal{V}_2$ is one object over $\mathbb{C}$ and two copies of one object over $\mathbb{R}$.

**Remark (the highest-weight vector is nilpotent).** The vector $v_+(\vec u)=\vec v+i\vec w$ is a highest-weight vector of the adjoint for every frame, and $v_+(\vec u)^2=0$ in the algebra, by the anticommutation of the two units of the frame. The highest-weight vector of the adjoint is a nilpotent element; the same vector is not null for the trace form, which is positive definite. The two notions of length, the product and the form, must be kept apart.

**Remark (why the shortcut fails).** One cannot compute the adjoint Casimir as $\operatorname{ad}_{\tilde S_k^2}$, because $\operatorname{ad}$ is a representation of the Lie algebra and not of the associative algebra. For example,

$$
\operatorname{ad}_{\vec e_x}^2\vec e_y=[\vec e_x,[\vec e_x,\vec e_y]]=[\vec e_x,2\vec e_z]=-4\vec e_y,
\qquad
\operatorname{ad}_{\vec e_x^2}\vec e_y=\operatorname{ad}_{-e_t}\vec e_y=0.
$$

The two differ, and only the first enters the Casimir.

**The invariant.** On the material sector neither invariant is constrained: $N$ and $B^2$ are free, and $N=Q_t^2+B^2$ with $Q_t$ the trace and $B^2=\lvert\vec r\rvert^2$ the square of the vector part. The sector is the carrier that reaches every region of the partition, and the two other carriers are its two degenerate faces.

## The Generator Reading: the Casimir and the Ladder

The three carriers are in place. What follows computes their spins a second time, by the highest weight, and the computation is the reading that the classical theory of angular momentum supplies.

**Definition (spin, highest-weight form).** Let $(W,\rho)$ be an irreducible unitary carrier. For a unit $\vec u\in\mathfrak{g}$, the operator $\rho(\vec u\cdot\vec S)$ is self-adjoint. Its largest eigenvalue is the **highest weight** of $W$, and it equals the spin of §*The Spin Is the Dimension of the Carrier*.

**Proposition (independence of the axis).** The spectrum of $\rho(\vec u\cdot\vec S)$ does not depend on the unit vector $\vec u$.

*Proof.* For $u\in G$, $\rho(u)\rho(\vec u\cdot\vec S)\rho(u)^{-1}=\rho\bigl(\operatorname{Ad}_u(\vec u\cdot\vec S)\bigr)=\rho\bigl((R\vec u)\cdot\vec S\bigr)$, with $R$ the rotation. The map $G\to SO(3)$ is surjective, so all unit vectors are conjugate, and conjugate operators have the same spectrum.

**A frame, declared once.** This section uses a right-handed orthonormal frame $(\vec u,\vec v,\vec w)$, with $\tilde S(\vec u)=\vec u\cdot\vec S$ as in §*The Spin-Half Carrier*. It is a coordinate choice and nothing below depends on it. The Casimir is

$$
C=(\vec u\cdot\vec S)^2+(\vec v\cdot\vec S)^2+(\vec w\cdot\vec S)^2=\tilde S_1^2+\tilde S_2^2+\tilde S_3^2\in U(\mathfrak{g}),
$$

and the two expressions are equal for every frame, because the coefficient of $\tilde S_i\tilde S_j$ in the first is $\sum_a n_{a,i}n_{a,j}=\delta_{ij}$ and the first is therefore $\sum_i\tilde S_i^2$ with no ordering question. Every statement below is a statement about the algebra with the frame removed.

**Proposition (centrality).** $[C,\tilde S_l]=0$ for $l=1,2,3$.

*Proof.* $\sum_i[\tilde S_i^2,\tilde S_l]=\sum_i\bigl(\tilde S_i[\tilde S_i,\tilde S_l]+[\tilde S_i,\tilde S_l]\tilde S_i\bigr)=\sum_i\bigl(i\epsilon_{ilj}\tilde S_i\tilde S_j+i\epsilon_{ilj}\tilde S_j\tilde S_i\bigr)$, which is antisymmetric under $i\leftrightarrow j$ and vanishes.

**Theorem (the Casimir value and the dimension).** Let $W$ be an irreducible unitary carrier of spin $s$. Then

$$
\rho(C)=s(s+1)\operatorname{id}_W,\qquad \dim_{\mathbb{C}}W=2s+1,\qquad s\in\tfrac12\mathbb{Z}_{\ge0}.
$$

*Proof.* Choose an eigenvector $v$ of $\rho(\tilde S(\vec u))$ with the maximal eigenvalue $s$, the axis being any unit and the answer being independent of it. Then $\rho(\tilde S_+(\vec u))v=0$, since otherwise that operator would produce an eigenvector of weight $s+1$. Put $v_k=\rho(\tilde S_-(\vec u))^kv$. The span of the $v_k$ is invariant, so it is all of $W$. Since $\tilde S_+(\vec u)\tilde S_-(\vec u)=C-\tilde S(\vec u)^2+\tilde S(\vec u)$, one has $\rho(\tilde S_+(\vec u)\tilde S_-(\vec u))v_k=(2s-k)(k+1)v_k$. If the string terminates, so that $v_{k+1}=0$ with $v_k\neq0$, then $0=\rho(\tilde S_+(\vec u))v_{k+1}=(2s-k)(k+1)v_k$, so $k=2s$. Hence $v_0,\dots,v_{2s}$ are a basis and $\dim W=2s+1$. On $v_0$, $\rho(C)v_0=(s^2+s)v_0=s(s+1)v_0$, because $\rho(\tilde S_+(\vec u)\tilde S_-(\vec u))v_0=2s\,v_0$ and $\rho(C)=\rho(\tilde S_+(\vec u)\tilde S_-(\vec u))+\rho(\tilde S(\vec u))^2-\rho(\tilde S(\vec u))$.

The theorem is the converse of the definition: the definition reads the spin off the dimension, and the theorem recovers the dimension from the spin. Neither replaces the other, and the definition comes first because the dimension is what the algebra supplies.

**The ladder operators** are the frame's,

$$
\tilde S_\pm(\vec u)=\vec v\cdot\vec S\pm i\,\vec w\cdot\vec S,\qquad [\tilde S(\vec u),\tilde S_\pm(\vec u)]=\pm\tilde S_\pm(\vec u),\qquad [\tilde S_+(\vec u),\tilde S_-(\vec u)]=2\tilde S(\vec u),
$$

with $\vec u$ the axis and $(\vec v,\vec w)$ the frame inside the plane orthogonal to it. At $\vec u=\vec e_z$ they read $\tilde S_\pm=\tilde S_1\pm i\tilde S_2$, which is the corpus's older display and is one instance of the line above.

**Theorem (the irreducible modules).** For every integer $n\ge0$ there is, up to isomorphism, exactly one irreducible module $\mathcal{V}_n$ of dimension $n+1$. In a basis $v_0,\dots,v_n$,

$$
\tilde S(\vec u)v_k=\bigl(k-\tfrac{n}{2}\bigr)v_k,\qquad
\tilde S_+(\vec u)v_k=\sqrt{(n-k)(k+1)}\,v_{k+1},\qquad
\tilde S_-(\vec u)v_k=\sqrt{k(n-k+1)}\,v_{k-1},
$$

with $\tilde S_+(\vec u)v_n=0$ and $\tilde S_-(\vec u)v_0=0$. The spin is $s=n/2$ and the Casimir is $s(s+1)$, for every frame.

*Proof.* The preceding theorem gives existence and the dimension. The formulas are the standard ones, and they satisfy the brackets directly. Uniqueness follows because a highest-weight vector generates the module and its weight fixes $n$.

The notation $\mathcal{V}_n$ is that of *Representations of Lie Algebras*, where these modules are written $V_n$; the letter $V$ is reserved here for the traceless part of $\mathbb{B}$.

**Corollary (the Clebsch–Gordan rule).** For nonnegative integers $m,n$,

$$
\mathcal{V}_m\otimes\mathcal{V}_n\cong\bigoplus_{k=|m-n|}^{m+n}\mathcal{V}_k,
$$

the sum over $k$ of the same parity as $m+n$.

*Proof.* The tensor product is completely reducible, and its highest weight is $m+n$, with multiplicity one; removing the highest summand and repeating gives the rule.

**Remark.** The algebra sees $SU(2)$ and not $SO(3)$: $s$ ranges over the half-integers. The integer values are the ones on which the centre $\pm e_t$ of $G$ acts trivially, and they are the representations that descend to $SO(3)$. §*The Central Sign and the Integrality Class* returns to the point.

**The closed list is a list of carriers.** The theorem gives an irreducible module of every dimension, so spin $\tfrac32$ and spin $2$ are carriers in the sense of this section. No subspace of $\mathbb{B}$ carries them, and the reason is in §*The Spectrum and the Criterion*: the subcarriers of the regular module are three, of dimensions $1$, $2$ and $3$, and a fourth would need dimension $4$ or more.

## The Spectrum and the Criterion

The definition of spin presumes a carrier, and the Casimir theorem reads a dimension off the spin. The converse is what a reader with a subspace in hand needs: a test that decides whether the subspace is a carrier at all, and of which spin. The test is the weight string.

**Proposition (the weight string of an irreducible carrier).** Let $W$ be an irreducible unitary carrier of spin $s$, and let $\vec u$ be a unit real vector. The spectrum of $\rho(\vec u\cdot\vec S)$ is

$$
s,\ s-1,\ \dots,\ -s,
$$

each value once, so that $\dim_{\mathbb{C}}W=2s+1$.

*Proof.* The proof of the Casimir theorem in §*The Generator Reading* produces the vectors $v_0,\dots,v_{2s}$, of weights $s,s-1,\dots,-s$, and proves that they are a basis. Distinct weights therefore occur once each, and the length of the string is the dimension.

**Proposition (the criterion).** Let $W$ be a finite-dimensional carrier whose highest weight is $s$. Then $W$ is irreducible exactly when $\dim_{\mathbb{C}}W=2s+1$; equivalently, exactly when the weights of $\rho(\vec u\cdot\vec S)$ are $s,s-1,\dots,-s$, each occurring once.

*Proof.* If $W$ is irreducible, the two propositions agree. Conversely, the highest-weight vector generates the irreducible subcarrier $W_0$ of dimension $2s+1$, and $W_0\subseteq W$; if $\dim W=2s+1$ then $W_0=W$. The hypothesis is that $W$ contains a highest-weight vector of weight $s$, not that such a vector generates $W$: a carrier generated by a highest-weight vector is irreducible already, and the proposition would say nothing.

**Remark (a repeated weight is a symptom, not the criterion).** Distinct weights do not by themselves give irreducibility. The module $\mathcal{V}_0\oplus\mathcal{V}_1$ has the weights $-\tfrac12$, $0$, $+\tfrac12$, all distinct, and dimension $3$ against $2\cdot\tfrac12+1=2$; it is reducible. The dimension count decides, and a repeated weight is the visible trace of a reducible sum.

**The weight string is the spin.** The word spin is the length of the string, read on the carriers of this article. It is the same criterion that *Spinors as Peirce Coordinates* applies to the column of a matrix model, where the half-root has the weight $-\tfrac12$ with multiplicity $N-1$ and the string $+\tfrac12,-\tfrac12$ occurs exactly when $N=2$; the "each occurring once" of the spinor definition there is the criterion above.

**The spectra of the three carriers.** With any unit axis $\vec u$ and the generator $\tilde S(\vec u)$, the computations of the preceding sections give the following table. The spectra do not depend on the axis, so none is written.

| carrier | action | $\dim$ of the carrier | weights of $\tilde S(\vec u)$ | string | verdict |
|---|---|---|---|---|---|
| $\mathbb{B}_{C}$ | conjugation | $1$ complex | $0$ | complete | irreducible, $\mathcal{V}_0$ |
| $S_\pm(\vec u)$ | left multiplication | $2$ complex | $+\tfrac12,\ -\tfrac12$ | complete | irreducible, $\mathcal{V}_1$ |
| $\mathbb{B}_{\Phi}$ | conjugation | $4$ real | $+1,\ 0,\ 0,\ -1$ | doubled at $0$ | reducible, $\mathcal{V}_0\oplus\mathcal{V}_2$ |
| $\mathfrak{k}\subset\mathbb{B}_{\Phi}$ | conjugation | $3$ real | $+1,\ 0,\ -1$ | complete | irreducible, $\mathcal{V}_2$ |
| $\mathbb{B}$ | left multiplication | $4$ complex | $+\tfrac12,\ +\tfrac12,\ -\tfrac12,\ -\tfrac12$ | doubled | reducible, $2\mathcal{V}_1$ |
| $\mathbb{B}$ | conjugation | $4$ complex | $+1,\ 0,\ 0,\ -1$ | doubled at $0$ | reducible, $\mathcal{V}_0\oplus\mathcal{V}_2$ |
| four-vector | two-sided action | $4$ complex | $+1,\ 0,\ 0,\ -1$ | doubled at $0$ | reducible, $\mathcal{V}_2\oplus\mathcal{V}_0$ |

**Remark (the last four rows).** The adjoint action on all of $\mathbb{B}$, on one sector and on the four-vector of the two-sided action present the same multiset to the rotation subgroup, $+1,0,0,-1$. The repeated weight $0$ is the centre in the first case, the fixed line in the second and the singlet summand in the third. Three carriers, one spectrum. The representation space of the sector is the triplet inside it, and that is the row that reads as complete.

**The four-vector of the two-sided action.** The carriers above are the ones that multiplication on the algebra produces. The algebra also carries the four-vector of the two-sided action $a\mapsto gag^{*}$, which is the representation $(\tfrac12,\tfrac12)$ of the Lorentz group, of complex dimension four. On the rotation subgroup it restricts to

$$
(\tfrac12,\tfrac12)\big|_{\mathrm{SU}(2)}\cong\mathcal{V}_2\oplus\mathcal{V}_0 ,
$$

so its weights are $+1,0,0,-1$, and its dimension is $4$ against $2\cdot1+1=3$. By the criterion the carrier is reducible, and its constituents are the triplet and the singlet. The split into $\mathbf{1}\oplus\mathbf{3}$ is recorded in §*What the Algebra Does Not Determine*; the weights are computed here. The Lorentz labels are those of *Biquaternion Rotations and Lorentz Transformations*, and the two-sided operator is not a subcarrier of the regular module: it is a second action, and the closure theorem does not apply to it.

**The arithmetic obstruction.** Suppose one action on $\mathbb{B}$ contained all three carriers. They would be distinct irreducible submodules, since their dimensions differ, and distinct irreducibles intersect trivially; their representation spaces have dimensions $1$, $2$ and $3$, and they would add:

$$
1+2+3=6>4=\dim_{\mathbb{C}}\mathbb{B}.
$$

This is impossible. The three spins are the union of the constituents of two actions, not the constituents of one. The count is about representation spaces and not about carriers: the carriers are $1$, $2$ and $4$ real dimensions, and they were never required to fit inside one module — two of them are not modules at all.

**Remark (carriers and subcarriers).** The theorem classifies the subcarriers of the regular module, not the representations of $\mathfrak{g}$. The Lie algebra has an irreducible module of every dimension, so spin $\tfrac32$ and spin $2$ are carriers in the sense of §*The Generator Reading*; no subspace of $\mathbb{B}$ carries them. The word *subcarrier* is what the closure theorem needs, and the distinction is not a technicality: it is the difference between a representation and a representation realised inside the algebra.

**Theorem (the closure of the subcarriers).** The irreducible subcarriers of $\mathbb{B}$ are:

1. under left multiplication, the minimal left ideals $S_\pm(\vec u)$, $\vec u$ a unit real vector, all isomorphic to $S\cong\mathcal{V}_1$;
2. under conjugation, $Z\cong\mathcal{V}_0$ and $V\cong\mathcal{V}_2$, and therefore the real carrier $\mathfrak{k}$ of the material sector.

*Proof.* The left ideals of $M_2(\mathbb{C})$ are the sets of matrices whose rows lie in a fixed subspace, and the minimal ones are those whose rows lie in a line; these are the $S_\pm(\vec u)$ by the proposition above; $\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u)$ for every $\vec u$. For the adjoint action, let $W$ be invariant and irreducible. If $W\subseteq V$, then $W=V$, because the string $v_+,S_-v_+,S_-^2v_+$ spans $V$. If $W$ has a nonzero component in $Z$, then either $W=Z$ (when $W\cap V=0$) or $W$ contains $Z$ and a nonzero subspace of $V$, hence contains $V$, and then $W=\mathbb{B}$, which is reducible.

**Corollary.** The spins of the three carriers are $0$, $\tfrac12$ and $1$, and their representation spaces have dimensions $1$, $2$ and $3$.

**Corollary.** No carrier has a representation space of dimension $4$ or more. The only invariant subspace of complex dimension four is $\mathbb{B}$ itself, and it is reducible in both actions: $S_+\oplus S_-$ on the left, $Z\oplus V$ under conjugation. The two sectors are four real dimensions and are not complex subspaces; over $\mathbb{C}$ each of them spans $\mathbb{B}$.

## The Orbital Realisation

A third realisation of the rotation algebra exists, and no subspace of $\mathbb{B}$ carries it. Let $A$ be a commutative $\mathbb{C}$-algebra carrying an action of $\mathfrak{so}(3)$ by derivations: linear maps $D_k$ with the Leibniz rule $D_k(ab)=D_k(a)b+aD_k(b)$ and with the angular-momentum brackets among themselves. The classical example is the algebra of polynomials in three commuting letters, where the action is faithful and every spin occurs, in the summands $\mathcal{V}_0,\mathcal{V}_2,\mathcal{V}_4,\dots$ of the homogeneous parts.

**Proposition.** No derivation of a commutative algebra is inner.

*Proof.* An inner derivation is $\operatorname{ad}_a(b)=ab-ba$, which vanishes identically as soon as $ab=ba$ for all $a,b$.

**Theorem (the algebra carries no outer derivation).** Every $\mathbb{C}$-linear derivation of $\mathbb{B}$ is inner.

*Proof.* The algebra is central simple over $\mathbb{C}$, and for a central simple algebra every derivation is inner (*Biquaternion Automorphisms and Derivations*, §*Derivations over $\mathbb{C}$*).

**Corollary (what belongs to the algebra and what does not).** The spin part of an angular momentum is the inner derivation $\operatorname{ad}_{\tilde S_k}$ of $\mathbb{B}$. The orbital part is outer. It therefore cannot be an operator of $\mathbb{B}$ at all, and the question of which subspace carries it does not arise: it belongs to a commutative algebra of functions of position, which is a module for the orbital action and not a module of $\mathbb{B}$. The biquaternion algebra supplies the second and only the second.

## The Total Angular Momentum

For a carrier $U$ of spin $l$ and the spin-half carrier $S$, the tensor product $U\otimes S$ carries the total generator

$$
\tilde S_{\mathrm{tot},k}=L_k\otimes1+1\otimes \tilde S_k,
$$

where $L_k$ denotes the three generators of the action on $U$.

Since the two summands commute and each satisfies the angular-momentum brackets, so does the sum. The Casimir expands as

$$
C_{\mathrm{tot}}=C_L\otimes1+1\otimes C_S+2\sum_k L_k\otimes \tilde S_k.
$$

The last term is the spin–orbit operator,

$$
\vec L\cdot\vec S=\sum_k L_k\otimes \tilde S_k=\tfrac12\bigl(C_{\mathrm{tot}}-C_L\otimes1-1\otimes C_S\bigr).
$$

**Theorem (the addition of angular momenta).** For $l\ge1$,

$$
\mathcal{V}_{2l}\otimes\mathcal{V}_1\cong\mathcal{V}_{2l-1}\oplus\mathcal{V}_{2l+1},
$$

and for $l=0$ it is $\mathcal{V}_1$. The total spin is $s_{\mathrm{tot}}=l\pm\tfrac12$.

*Proof.* By the Clebsch–Gordan rule, $\mathcal{V}_{2l}\otimes\mathcal{V}_1=\mathcal{V}_{2l-1}\oplus\mathcal{V}_{2l+1}$ for $l\ge1$, and $\mathcal{V}_0\otimes\mathcal{V}_1=\mathcal{V}_1$.

**Corollary (the spin–orbit eigenvalues).** On the summand of total spin $s_{\mathrm{tot}}$,

$$
\vec L\cdot\vec S=\frac12\Bigl[s_{\mathrm{tot}}(s_{\mathrm{tot}}+1)-l(l+1)-\tfrac34\Bigr],
$$

that is, $+\tfrac{l}{2}$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $-\tfrac{l+1}{2}$ for $s_{\mathrm{tot}}=l-\tfrac12$.

*Proof.* Evaluate the Casimir expansion on the summand.

**Remark.** The total Casimir is central in $U(\mathfrak{g})$ acting on the tensor product, but it is not a central element of $\mathbb{B}$: it contains the cross term $\sum L_k\otimes \tilde S_k$. The pure-spin Casimir $\tfrac34e_t$ is a central element of the algebra itself. The two senses of *central* are different, and only the second is a statement about $\mathbb{B}$.

## Tensor Products and the Absence of a Spin-Two Carrier

The adjoint module is $\mathbb{B}\cong\mathcal{V}_0\oplus\mathcal{V}_2$.

**Proposition.** Its tensor square decomposes as

$$
\mathbb{B}\otimes\mathbb{B}
\cong 2\mathcal{V}_0\oplus3\mathcal{V}_2\oplus\mathcal{V}_4,
$$

of dimension $2+9+5=16$.

*Proof.* $(\mathcal{V}_0\oplus\mathcal{V}_2)^{\otimes2}=\mathcal{V}_0\oplus2\mathcal{V}_2\oplus(\mathcal{V}_2\otimes\mathcal{V}_2)$, and $\mathcal{V}_2\otimes\mathcal{V}_2=\mathcal{V}_0\oplus\mathcal{V}_2\oplus\mathcal{V}_4$.

**Theorem (multiplication kills spin two).** The multiplication map

$$
m:\mathbb{B}\otimes\mathbb{B}\longrightarrow\mathbb{B},\qquad a\otimes b\longmapsto ab
$$

is equivariant for conjugation, surjective, and its kernel is

$$
\ker m\cong\mathcal{V}_0\oplus2\mathcal{V}_2\oplus\mathcal{V}_4.
$$

In particular the unique spin-two summand $\mathcal{V}_4$ lies in the kernel.

*Proof.* For $u\in G$, $m(uau^{-1}\otimes ubu^{-1})=(uau^{-1})(ubu^{-1})=u(ab)u^{-1}$, so $m$ is equivariant. It is surjective because $m(a\otimes e_t)=a$. Since $G$ is compact, the exact sequence $0\to\ker m\to\mathbb{B}\otimes\mathbb{B}\to\mathbb{B}\to0$ splits, and the multiplicities of $\ker m$ are the differences of those of the tensor square and of $\mathbb{B}=\mathcal{V}_0\oplus\mathcal{V}_2$. The image has no $\mathcal{V}_4$, so the $\mathcal{V}_4$-isotypic component maps to zero.

**Corollary.** No product of two biquaternions has a spin-two component. There is therefore no fourth carrier inside the algebra, and the three of §*The Three Carriers* are the whole list.

*Proof.* The image is $\mathbb{B}=\mathcal{V}_0\oplus\mathcal{V}_2$.

**Example (the highest-weight check).** The highest-weight vector of $\mathcal{V}_4$ is $v_+(\vec u)\otimes v_+(\vec u)$, of weight $2$. Its product is

$$
v_+(\vec u)^2=(\vec v+i\vec w)^2=\vec v^2+i\bigl(\vec v\vec w+\vec w\vec v\bigr)+(i\vec w)^2=(-e_t)+0+(e_t)=0,
$$

and the four descendants obtained by applying $\operatorname{ad}_{\tilde S_-}\otimes1+1\otimes\operatorname{ad}_{\tilde S_-}$ also multiply to zero. This is the five-dimensional summand, and it vanishes under the product.

**Remark (why the left picture does not give the theorem).** Under left multiplication $\mathbb{B}\cong2\mathcal{V}_1$ and $\mathbb{B}\otimes\mathbb{B}\cong4(\mathcal{V}_0\oplus\mathcal{V}_2)$, but $m$ is not equivariant for that action, because $(ga)(gb)\neq g(ab)$. The argument must be run in the adjoint picture, where conjugation is an algebra automorphism.

## Real Forms and the Rotation Subgroup

The algebra $\mathbb{B}$ is complex; its underlying real algebra is $\mathbb{B}_{\mathbb{R}}$, and the real structure is what this section adds. Complexifying $\mathbb{B}_{\mathbb{R}}$ by an adjoined root of $-1$ gives $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}\cong\mathbb{B}\oplus\mathbb{B}$, and the two halves are the eigenspaces of the central sign $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, with $\tilde{Ζ}_{\mathrm{ad}}^2=-e_t$, $\chi^2=+e_t$ and $\chi\notin\mathbb{B}$; the chiral idempotents are $e_\pm=\tfrac12(e_t\pm\chi)$. The construction, its notation and the two halves are *The Unpolarized Module of the Biquaternion Algebra*; nothing below uses them.

The two actions of this article are two actions of the group: left multiplication on the whole algebra, giving $2\mathcal{V}_1$, and conjugation on the adjoint picture, giving $\mathcal{V}_0\oplus\mathcal{V}_2$. The Lorentz group acts by the two-sided operator $a\mapsto gag^*$, and the two sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the two four-vectors; the left spinor is the $(\tfrac12,0)$ and the conjugate module the $(0,\tfrac12)$. The details are in *Biquaternion Rotations and Lorentz Transformations* and in *The Unpolarized Module of the Biquaternion Algebra*; nothing in the present article depends on them.

**Proposition (the two real forms of the carrier).** Put $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and $\mathfrak{p}=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$. Then

$$
V=\mathfrak{k}\oplus\mathfrak{p},
$$

and $\mathrm{ad}_{\vec e_k}$ preserves each summand, acting by the same matrix on both.

*Proof.* The bracket $[\vec e_k,\vec e_j]=2\epsilon_{kjl}\vec e_l$ is real, so $\mathrm{ad}_{\vec e_k}\mathfrak{k}\subseteq\mathfrak{k}$. The bracket $[\vec e_k,i\vec e_j]=i[\vec e_k,\vec e_j]$ is $i$ times the same combination, so $\mathrm{ad}_{\vec e_k}\mathfrak{p}\subseteq\mathfrak{p}$, and the two matrices agree. Left multiplication by $i$ is central and carries $\mathfrak{k}$ onto $\mathfrak{p}$, so the complex span of either summand is $V$.

**Corollary.** Each summand is a real form of $V$ and carries the real three-dimensional irreducible representation of the rotation algebra. The complex carrier $\mathcal{V}_2$ is one object over $\mathbb{C}$ and two copies of one object over $\mathbb{R}$.

**The material sector is the real carrier.** $\mathfrak{k}$ is the spin-one carrier in the real algebra, and $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$ is that carrier together with its scalar line. This is why the corpus names the sector rather than the traceless part: the sector is the smallest real subspace that holds a four-vector and is closed under conjugation and under the commutator, and the spin sits in its traceless part.

**Remark (the Hermitian generators exchange the summands).** The element $\tilde S_k=\tfrac12 i\vec e_k$ is not in the real rotation algebra $\mathfrak{k}$; it is an element of $\mathfrak{p}$, that is, the complexified generator. Since $i\mathfrak{k}=\mathfrak{p}$, the derivation $\mathrm{ad}_{\tilde S_k}$ carries $\mathfrak{k}$ onto $\mathfrak{p}$ and $\mathfrak{p}$ onto $\mathfrak{k}$. A weight vector of $\mathrm{ad}_{\tilde S_3}$ therefore has one component in each, and the highest-weight vector is of that form: $v_+=\vec e_x+i\vec e_y$ with $\vec e_x\in\mathfrak{k}$ and $i\vec e_y\in\mathfrak{p}$. The integer weights belong to the complexified picture, and the real picture splits the one carrier into two copies.

## The Five Uses of the Word Spin

Five objects in this corpus are called a spin. One of them is the definition, two are readings of it, and two are signs that carry no weight at all.

| use | what it labels | the object | values |
|---|---|---|---|
| **the carrier** | the subspace, and the spin is the dimension of its representation space | $\mathbb{B}_{C}$, $S_\pm$, $\mathbb{B}_{\Phi}$ | $0,\ \tfrac12,\ 1$ |
| the highest weight | the same number, read as the largest eigenvalue | either action | $0,\ \tfrac12,\ 1$ |
| the Casimir | the same number, read as $s(s+1)$ | either action | $0,\ \tfrac34,\ 2$ |
| the Peirce index | the copy | right multiplication by $i\vec u$ | $+$ or $-$ |
| chirality | the Lorentz half | a central sign in $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$ | $+$ or $-$ |

**The first three rows are one number.** The carrier decides the dimension, the dimension is the highest weight plus one, and the Casimir is a function of the highest weight. The rows are three readings of one arithmetic, and the corpus's habit of stating them in three places, in three vocabularies, is what this article's order is meant to end: the carrier is named, and the other two are computed from it.

**The last two rows are not values of $s$.** The Peirce index separates two copies of one carrier. The chirality separates two Lorentz halves. Neither changes a spin.

### The Central Sign and the Integrality Class

The $2\pi$ signs of §*The Spin-Half Carrier* are the two integrality classes: $-e_t$ acts as $-\mathrm{id}$ on the minimal left ideals and as the identity on $Z$ and on $V$. Half-integer carriers carry the first sign, integer carriers the second.

Neither sign is an eigenvalue read off one operator on $\mathbb{B}$. In the left regular module $-e_t$ acts as $-\mathrm{id}$ on all of $\mathbb{B}$; in the adjoint action it acts trivially on all of $\mathbb{B}$. The two signs are read in the two actions, not as the two eigenspaces of one operator on the algebra. This is the same lesson as the definition: a property of a carrier is not a property of the algebra.

### The Peirce Sign Is Not the Central Sign

The central element $-e_t$ acts as $-\mathrm{id}$ on $S_+$ and on $S_-$ alike, so it cannot separate them. The Peirce sign is the right multiplication $P=R_{i\vec u}$ at a unit $\vec u$. Since $(i\vec u)^2=+e_t$, $P^2=\mathrm{id}$, and

$$
P\tilde\Pi_+(\vec u)=\tilde\Pi_+(\vec u),\qquad P\tilde\Pi_-(\vec u)=-\tilde\Pi_-(\vec u),
$$

so $P$ is $+1$ on $S_+(\vec u)$ and $-1$ on $S_-(\vec u)$. It is implemented by the element $i\vec u$, which is not central: at $\vec u=\vec e_z$, $i\vec e_z\vec e_x=+i\vec e_y$ while $\vec e_x i\vec e_z=-i\vec e_y$. The Peirce index is therefore an inner, non-central copy label, and it never changes a spin value.

At a fixed axis, right multiplication by the mixed unit $\vec\Upsilon_{+-}$ carries $S_+$ onto $S_-$ and is the module isomorphism: it sends $\tilde\Pi_+$ to $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ to $\tilde\Pi_-$. Right multiplication by $\vec\Upsilon_{-+}$ annihilates $S_+$, because $\tilde\Pi_+\vec\Upsilon_{-+}=0$ and $\vec\Upsilon_{-+}^2=0$. Neither is the grading: each mixed unit is nilpotent, $\vec\Upsilon_{\pm\mp}^2=0$, and a nilpotent cannot be an involution.

### Chirality Is Central but Not a Spin

In the double, the chirality has the central form $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, with $\chi^2=+e_t$, and its two eigenspaces are the chiral halves $e_\pm=\tfrac12(e_t\pm\chi)$ of §*Real Forms and the Rotation Subgroup*. Both halves carry the same rotation content: chirality separates the two Lorentz chiralities, not two values of $s$.

The three signs are therefore distinct. A central sign in $\mathbb{B}$ marks integer against half-integer; an inner non-central sign separates two copies of one half-integer carrier; a central sign in the double separates two Lorentz halves. Only the first tracks the integrality of a spin, and none of the three is a value of $s$.

### The Dimensions One, Two and Three as Tensor Degrees

Two descriptions of one arithmetic.

**Matrix.** A left ideal of $M_2(\mathbb{C})$ is a sum of columns, each of dimension $2$. The centre is the line of scalar matrices, and the traceless part is the complement, of dimension $4-1=3$.

**Tensor degree.** The first three tensor powers of the simple module are

$$
\mathbb{C}\ (\text{degree }0),\qquad S\ (\text{degree }1),\qquad S\otimes S\ (\text{degree }2),
$$

of dimensions $1$, $2$ and $4$. The module $S$ is self-dual, the invariant alternating form $\varepsilon$ identifying $S^{*}$ with $S$, so $S\otimes S\cong\operatorname{End}_{\mathbb{C}}(S)=\mathbb{B}$, and under $G$ it splits as

$$
S\otimes S=\Lambda^2S\oplus\operatorname{sym}^2S\cong\mathbf{1}\oplus\mathbf{3}.
$$

The trivial summand is $\Lambda^2S$, the line of $\varepsilon$, and the identification carries it to the line of the identity endomorphism; the traceless symmetric part is the adjoint $V$. The dimensions $1$, $2$, $3$ are those of the degree-$0$ object, the degree-$1$ object, and the traceless part of the degree-$2$ object.

The truncation is the same fact from the other side. The algebra is the endomorphism object of $S$, of dimension $4$, and it splits as $\mathbf{1}\oplus\mathbf{3}$; degree $3$ is $S^{\otimes3}$, of dimension $8$, and it is not a subspace of $\mathbb{B}$. A spin above one is a carrier but not a subcarrier, which is the remark that closes §*The Spectrum and the Criterion*.

### What the Algebra Does Not Determine

**Which carrier a given object uses.** The algebra carries three. It does not say which field occupies which; that assignment lies outside the algebra, and the physics corpus makes it.

**No dynamics.** The Casimir is a label of the carrier. No generator of evolution and no equation of motion follow from it.

**No statistics.** The algebraic split matches the two integrality classes. The spin–statistics theorem is not proved by the algebra.

**No full Lorentz label.** Under left multiplication by $SL(2,\mathbb{C})$ the algebra carries the chiral spinor $(\tfrac12,0)$ with multiplicity two; under the Lorentz two-sided operator $Q\mapsto\tilde U Q\tilde U^{*}$ it carries the four-vector $(\tfrac12,\tfrac12)$, and its split into $\mathbf{1}\oplus\mathbf{3}$ is the work of the compact subgroup $G$. The rotation spin is the little-group shadow of the Lorentz label, not the whole label.

## Summary

The biquaternion algebra carries three elementary carrier types and no fourth: the type $\mathcal{V}_0$ on the centre $\mathbb{B}_{C}=\mathbb{C}e_t$ with spin $0$ under conjugation, the type $\mathcal{V}_1$ on the minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$ with spin $\tfrac12$ under left multiplication, and the type $\mathcal{V}_2$ on the material sector $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$ with spin $1$ on its traceless part $\mathfrak{k}$ under conjugation. The informational sector is a second carrier of the third type, and the material one is the carrier the article takes because it is closed under the commutator: $[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]=\mathfrak{k}$ stays inside the sector, while $[\mathbb{B}_{\Psi},\mathbb{B}_{\Psi}]=\mathfrak{k}$ lands in the other one. The spin of a carrier is the dimension of its representation space, $2s+1$; for the third carrier that dimension is three against a carrier of four, and the fourth entry is the scalar line that a vector field's constraint removes.

| carrier | action | spin | dimension of the representation space | Casimir |
|---|---|---|---|---|
| $\mathbb{B}_{C}=\mathbb{C}e_t$ | conjugation; fixed | $0$ | $1$ | $0$ |
| $S_\pm(\vec u)\cong\mathcal{V}_1$ | left multiplication | $\tfrac12$ | $2$ | $\tfrac34$ |
| $\mathbb{B}_{\Phi}$, traceless part $\mathfrak{k}$ | conjugation | $1$ | $3$ | $2$ |

The rotation algebra inside $\mathbb{B}$ has two normalisations: the anti-Hermitian $g_k=-\tfrac12\vec e_k$ and the Hermitian $\tilde S_k=\tfrac12 i\vec e_k$, related by $\tilde S_k=-ig_k$. The Casimir is $C=\sum \tilde S_k^2$; on an irreducible unitary carrier it is $s(s+1)$, the dimension is $2s+1$, and $s$ is the maximal weight. Irreducibility is decided by the spectrum: the carrier is irreducible exactly when the weights $s,s-1,\dots,-s$ occur once each, so that the length of the string is the dimension. A repeated weight marks a reducible sum, and the three carriers that present the multiset $+1,0,0,-1$ in the table of §*The Spectrum and the Criterion* present it for the same reason, each containing the centre or the singlet beside the triplet.

The three types are exactly the types of the irreducible subcarriers of the regular module, and $1+2+3=6>4$ shows that no single action contains all three. The minimal left ideals are parametrised by the sphere, and each is a copy of the spin-half module. Two of the three carriers are four real-dimensional, and their spins differ because the adjoint action on the sector has an invariant line and the left action on an ideal has none. The orbital part is an outer derivation, and the algebra cannot carry it, since every derivation of $\mathbb{B}$ is inner; the spin part is the inner derivation $\operatorname{ad}_{\tilde S_k}$.

The tensor square of the adjoint module contains a spin-two summand, and the multiplication map kills it: the product of two biquaternions carries no spin two. That vanishing is why there is no fourth carrier; the dimension count is why no other route can produce one. A spin above one is a field with more than one index, not a subspace.

The word spin has five uses in this corpus. Three are one number: the carrier, which is the definition; the highest weight, which is the largest eigenvalue on it; and the Casimir, which is $s(s+1)$ on it. The other two are signs, the Peirce index an inner copy label and the chirality a central Lorentz label, and neither is a value of $s$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Its basis; $\vec e_k^2=-e_t$ |
| $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ | The Hermitian and anti-Hermitian sectors |
| carrier; type; sub-carrier | An invariant subspace; the isomorphism class of its representation space; a proper invariant subspace of a carrier |
| $\mathbb{B}_{C}=\mathbb{C}e_t$ | The centre; the spin-$0$ carrier |
| $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$ | The minimal left ideals at the axis $\vec u$; the spin-$\tfrac12$ carriers |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$ | The rank-one idempotents |
| $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | The compact triple, the traceless part of $\mathbb{B}_{\Phi}$; the spin-$1$ carrier |
| $\mathfrak{p}=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ | The hyperbolic triple, the other real form; $V=\mathfrak{k}\oplus\mathfrak{p}$ |
| $\mathbb{B}_{\Phi}\cong\mathfrak{u}(1)\oplus\mathfrak{su}(2)$ | The material sector as a real Lie algebra; $[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]=\mathfrak{k}$ |
| $Z=\mathbb{C}e_t$, $V=\ker\operatorname{tr}$ | The two isotypic components of the adjoint action; $Z\cong\mathcal{V}_0$, $V\cong\mathcal{V}_2$ |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | The quaternionic norm; $N=0$ identically on $S_\pm$ |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | The vector square; $B^2=0$ identically on $\mathbb{B}_{C}$ |
| $G=SU(2)$ | The unit real quaternions |
| $\mathfrak{g}=\mathfrak{su}(2)$ | The real pure quaternions |
| $g_k=-\tfrac12\vec e_k$ | The anti-Hermitian generators |
| $\tilde S_k=\tfrac12 i\vec e_k$ | The Hermitian generators |
| $C=\tilde S_1^2+\tilde S_2^2+\tilde S_3^2$ | The Casimir |
| $s$ | The spin, the dimension of the carrier's representation space read as $(2s+1-1)/2$ |
| $\mathcal{V}_n$ | The irreducible module of dimension $n+1$ |
| $R_{Q}$ | Right multiplication by $Q$ |
| $\vec\Upsilon_{+-}=\tfrac12(i\vec e_x-\vec e_y)$ | The nilpotent weight $+\tfrac12$ vector of $S_-$ |
| $\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y)$ | The nilpotent weight $-\tfrac12$ vector of $S_+$ |
| $v_+=\vec e_x+i\vec e_y$ | The highest-weight vector of $V$ |
| $(\tfrac12,\tfrac12)$ | The four-vector of the two-sided action; $\mathcal{V}_2\oplus\mathcal{V}_0$ under $G$, with weights $+1,0,0,-1$ |
| $L_k$ | The three generators of the orbital action; outer, hence not an operator of $\mathbb{B}$ |

## Further Reading

- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html), for the physics reading of the same three carriers, with the particle assignments and the units.
- [The Three Elementary Carriers and the Four Sectors of Regularity and Degeneracy](../articles_physics/the-three-elementary-carriers-and-the-four-sectors-of-regularity-and-degeneracy.html), for the partition by $N$ and $B^2$ that the three carriers cut, and the region each of them reaches.
- [The Category of Modules in the Biquaternion Algebra](the-category-of-modules.html), for the simple module and the classification of the modules, which is why a module cannot label three spins.
- [The Polarized Module of the Biquaternion Algebra](the-polarized-module-of-the-biquaternion-algebra.html), for the decomposition ${}_\mathbb{B}\mathbb{B}\cong S\oplus S$; the spinor spaces and the ladder.
- [Spinors as Peirce Coordinates](spinors-as-peirce-coordinates.html), for the weight condition on a Peirce carrier, the multiplicity of the half-root on a column, and the irreducibility criterion read as a weight string.
- [The Casimir Operator](the-casimir-operator.html), for the Casimir in the general theory.
- [Representations of Lie Algebras](representations-of-lie-algebras.html), for the highest-weight classification and the Clebsch–Gordan rule.
- [The Tensor Square of the Duo-Complex Numbers](the-tensor-square-of-c2.html), for the decomposition of the tensor square.
- [The Unpolarized Module of the Biquaternion Algebra](the-unpolarized-module-of-the-biquaternion-algebra.html), for the central sign and the conjugate module.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz action and its labels.
- [Angular Momentum and Spin in Biquaternionic Form](../articles_physics/angular-momentum-and-spin-in-biquaternionic-form.html), for the physics counterpart and the units.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the highest-weight theorem and the Casimir.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for $\mathfrak{sl}_2$ and the Clebsch–Gordan rule.
