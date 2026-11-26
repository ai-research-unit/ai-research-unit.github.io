# __The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock__

## Introduction

The framework's compact symmetry group is $\mathrm{U}(2)$, and the electroweak group of the Standard Model is $SU(2)_L\times \mathrm{U}(1)_Y$. The two have the same Lie algebra and the same dimension count, and they are different groups: the framework's is a $\mathbb{Z}_2$ quotient, and the model's is a product. This article states that difference, computes what it forbids, and checks the observed hypercharge table against it.

The finding, first. The framework shares the **algebra** of the electroweak pair and not its **group**. The pair's algebra is $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, of real dimension $3+1=4$, and it is the anti-Hermitian sector of $\mathbb{B}$; that is the match, and it is exact. The framework's compact group is the $*$-unitary slice $U=\{\tilde Q:\tilde Q\tilde Q^{*}=e_t\}\cong\mathrm{U}(2)=(SU(2)\times\mathrm{U}(1))/\mathbb{Z}_2$, a central product; the Standard Model's is the product $SU(2)\times\mathrm{U}(1)$ itself, without the identification. The quotient is smaller, and the difference is a parity lock on the representation labels: a multiplet of spin $j$ carries an integer central charge $q$ with $q\equiv 2j\pmod 2$. The lock follows from the algebra's exponential, it is not a convention, and the observed hypercharge table satisfies it, with the least admissible step $q=6Y$. The quotient therefore does not exclude the observed multiplets. What remains outside is everything else: the chiral action, the assignment itself, the relation between the two couplings, and the scalar.

What this article is, in the family. It is the electroweak part of the Standard Model audit, given its own place. The audit as a whole — the three group factor, the matter content, the parameter count, the interpretive criteria, the ledger — is *The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors*, which sits in *The Standard Model as a Whole* because it is about the whole model. The sector's own boundary — the chiral wall, hypercharge, the scalar sector, fixing the representative — is *Electroweak Theory in the Biquaternion Framework: The U(2) Reach and the Chiral Wall*. Both are cited and neither is restated. The object of this article is narrower and it is one object: **the pair**, and the exact sense in which the framework has it.

Why the pair is worth an article. Because the error it guards against is the most natural one in the corpus. "The algebra is $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, the electroweak algebra is $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, therefore the framework contains the electroweak group" is a sentence that writes itself, and it is false at the group level: the framework's group is the quotient, the model's is the product, and the quotient quantises and locks the abelian charge in a way the product does not. The dimension count cannot see the difference. A parity check can.

## The Algebra Is the Pair's Algebra

The decomposition, in one display. The material sector is a direct sum of Lie algebras,

$$
\boxed{\;\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2),\qquad
[e_a,e_b]=2\,\varepsilon_{abc}e_c,\quad T_a=\tfrac12e_a,\quad [T_a,T_b]=\varepsilon_{abc}T_c\;}
$$

of real dimension $1+3=4$. That is $\mathfrak{u}(1)\oplus\mathfrak{su}(2)=\mathfrak{u}(2)$, which is the algebra of the electroweak pair and the algebra of $\mathrm{U}(2)$. *Non-Abelian Gauge Fields in Biquaternionic Form* builds the full machinery on the compact factor: the adjoint connection law, the curvature with its commutator term, the Bianchi identity, and the invariant Yang–Mills density.

The match is exact and it stops at the algebra. Both factors are ideals, so each carries its own coupling and its own kinetic term. That is what the pair needs: two coupling constants, $\kappa$ on the compact factor and $ϙ$ on the centre, each free and neither fixed by the algebra. A direct sum of ideals with two independent coefficients is a two-parameter gauge theory, and this is the framework's.

**The quotient, stated as a quotient of groups and not of algebras.** The algebra splits as a direct sum of ideals, but the **group** does not split as a product: the compact factor is $SU(2)$, $\mathrm{SU}(2)=S^3$, and the centre contributes $S^1$, and the two share the two points $\pm e_t$. The group of the construction is therefore $(\mathrm{SU}(2)\times S^1)/\{\pm e_t\}$, which is $\mathrm{U}(2)$. The **parity lock** then has a group-theoretic source rather than an assumed one: the label $q$ of a field is its character under the centre and the spin $j$ is its character under the rotor; identifying $-\tilde u$ with $+\tilde u$ is a half-turn on the rotor and a full turn on the centre, and the two labels therefore satisfy $q\equiv2j \pmod 2$. The kernel of the covering $\mathrm{Spin}(3)\to SO(3)$ is the whole content. The operator vocabulary is fixed in [Representation Is a Function of Spin](representation-is-a-function-of-spin.html).

What the algebra does not carry is the representation. The abelian factor acts by left multiplication by a central element, hence as a scalar on every element, hence with one charge for all components; the compact factor acts by left multiplication by a unit quaternion, hence identically on the two values of the chirality. Both are vector-like. *Representation Is a Function of Spin* states the general form of this: the symmetry group is the spin group, so the representation is read from the carrier and not chosen, and the carrier's three rows match the model in exactly one. *Chiral Fermions in the Biquaternion Framework* states the consequence for the two letters: a chiral action needs $ϙ_L\ne ϙ_R$ and a non-central charge, so it is not supplied by the algebra's own minimal coupling.

## The Group Is Not the Pair's Group

The group, not the algebra. The intrinsic group is the $*$-unitary slice,

$$
U=\{\tilde Q:\tilde Q\tilde Q^{*}=e_t\}\cong\mathrm{U}(2)=\frac{SU(2)\times\mathrm{U}(1)}{\mathbb{Z}_2},
\qquad
\mathbb{Z}_2=\{(\tilde e_t,1),\,(-\tilde e_t,-1)\},
$$

so the pair $(\tilde U,e^{i\theta})$ and its negative name the same group element. The Standard Model's symmetry group has no such identification: $SU(2)_L\times\mathrm{U}(1)_Y$ is the product, and $(-1,-1)$ is a distinct element there. The framework's group is a quotient of the pair's group, not the pair's group, and the electroweak theory of the Standard Model is a product theory. This is the statement the dimension count hides.

The lock the quotient imposes. The kernel of the exponential on the diagonal part is the parity-matched lattice

$$
L=\pi i m\,e_t+\pi n\,\vec U,\qquad m\equiv n\pmod 2,
$$

computed in *The Gauge Extension of the Central Phase: The Centre Bounds the Gauge Group*, where it is read as the statement that the two factors are not independent at the level of the exponent. Read on representations it is a selection rule. A multiplet of spin $j$ and central charge $q$ is a representation of $U$ only if it is trivial on $L$: on the half-turn $\pi\vec U$ it acts as $(-1)^{2j}$, on the half-phase $\pi i\,e_t$ as $(-1)^{q}$, so triviality on the odd-odd element requires

$$
\boxed{\;q\equiv 2j\pmod 2\;}
$$

and the even-even elements are automatically trivial. Integrality of $q$ alone says the phase is a circle; the parity is the quotient.

**What the product allows and the quotient forbids.** In the product the abelian charge of a multiplet is a free label: once the period of the circle is chosen, a doublet may carry any $Y$ on the resulting lattice, and the assignment is fixed by anomaly cancellation together with the observed electric charges. In the quotient the abelian charge of a doublet must be odd and that of a singlet even, in the lattice of the central phase. A framework multiplet cannot be given a charge independent of its spin.

The observed table passes the check. Take the central charge to be $q=6Y$, the least step on which every observed hypercharge is an integer; the table below is *The Electroweak Gauge Group and the Hypercharge Assignment: The Group and the Derived $Y$*'s, with the two added columns $q=6Y$ and $2j$.

| multiplet | $T_3$ | $Y$ | $Q=T_3+Y$ | $q=6Y$ | $2j$ | $q\equiv 2j$ |
|---|---|---|---|---|---|---|
| $u_L$ | $+\tfrac12$ | $+\tfrac16$ | $+\tfrac23$ | $+1$ | $1$ | yes |
| $d_L$ | $-\tfrac12$ | $+\tfrac16$ | $-\tfrac13$ | $+1$ | $1$ | yes |
| $u_R$ | $0$ | $+\tfrac23$ | $+\tfrac23$ | $+4$ | $0$ | yes |
| $d_R$ | $0$ | $-\tfrac13$ | $-\tfrac13$ | $-2$ | $0$ | yes |
| ${\jmath}_L$ | $+\tfrac12$ | $-\tfrac12$ | $0$ | $-3$ | $1$ | yes |
| $e_L$ | $-\tfrac12$ | $-\tfrac12$ | $-1$ | $-3$ | $1$ | yes |
| $e_R$ | $0$ | $-1$ | $-1$ | $-6$ | $0$ | yes |

Why the check had to pass, and what that means. On a doublet $6Y=6Q-6T_3=6Q\mp3$, odd exactly when $6Q$ is even; on a singlet $6Y=6Q$, even exactly when $6Q$ is even. Read on the table, the lock is therefore the statement that electric charge is quantised in thirds, $3Q\in\mathbb{Z}$, given the $T_3$ assignment. Every observed fermion satisfies it, and so does every fermion of any completion of the table that keeps charge in thirds. The lock does not exclude the observed content; it says something sharper: it is not a constraint on the model but a constraint the model meets, and a state of charge outside $\tfrac13\mathbb{Z}$ could not be a framework multiplet at all.

What the check does not do. It does not derive the values. The step six is chosen to make the table integral, and the seven rows are the model's; the lock fixes the parity of the abelian charge against the spin and says nothing about which charge a multiplet carries. The two statements must be kept apart, because this is the one place in the sector where a framework computation touches the table without importing it, and it would be easy to read more into it than it holds. *The Electroweak Gauge Group and the Hypercharge Assignment: The Group and the Derived $Y$* is where the values are computed as a solution of the anomaly conditions, and where the solution is shown to need the model's content as input.

## The Two Couplings and the Missing Angle

**Two parameters, no relation.** The algebra gives each factor its own coefficient: $\kappa$ on the compact factor, $ϙ$ on the centre. Both are free, neither is fixed by the algebra, and the algebra supplies no relation between them. A relation is what a mixing angle is. With $g$ and $g_{\mathrm Y}$ the two couplings,

$$
\tan\theta_W=\frac{g_{\mathrm Y}}{g},\qquad e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W,\qquad Q_{\mathrm{em}}=T_3+Y,
$$

and the angle is a derived quantity of a theory that supplies both couplings and their embedding. The framework supplies neither the values nor a principle relating them, so the angle it could at best compute is the ratio of two free parameters, which is not a prediction. The relation $Q_{\mathrm{em}}=T_3+Y$ is the same statement from the charge side: it needs the $T_3$ of a doublet and the $Y$ of the same doublet to come from one normalisation, and the framework has one normalisation only if the lock is used, which fixes parity and not scale.

What would settle it. A principle fixing the relative normalisation of the two factors on the framework's own carrier: a unification condition, an anomaly condition tying the two, or a derivation of the embedding of the centre in $\mathrm{U}(2)$ that the quotient already suggests. *Grand Unification in the Biquaternion Framework: Where the Embedding Fails* records that the standard route fails on the same ceiling, because a group large enough to fix the ratio is not available. The row is blocked, and it is blocked behind the same wall as hypercharge, not behind a new one.

One reading, stated and not adopted. That the parity lock be read as the framework's version of charge quantisation, with the two couplings the two halves of one normalisation, is a reading the algebra permits and does not require. It would make $\theta_W$ a framework number. Nothing in the corpus computes it, and this article does not supply the computation.

## The Pair's Ledger

| Item | Status | Object or computation that would settle it |
|---|---|---|
| The algebra $\mathfrak{u}(2)=\mathbb{R}(ie_t)\oplus\mathfrak{su}(2)$, dimension $3+1=4$ | Established | — |
| The two gauge constructions: abelian connection and curvature; adjoint connection, commutator curvature, Bianchi identity, invariant density | Established | — |
| The group $\mathrm{U}(2)=(SU(2)\times\mathrm{U}(1))/\mathbb{Z}_2$, a quotient and not a product | Established | — |
| The parity lock $q\equiv 2j\pmod 2$ on the representation labels | Established, read off the kernel lattice | — |
| The lock against the observed table with $q=6Y$; equivalence to $3Q\in\mathbb{Z}$ | Checked here | A state of charge outside $\tfrac13\mathbb{Z}$, or a framework multiplet that fails the lock |
| A chiral action of the compact factor, $SU(2)_L$ and not the vector-like $\mathrm{SU}(2)$ | No route yet | A non-central action under which the two letters transform inequivalently |
| The hypercharge values $Y$ of the multiplets | No route yet | A derivation of the table, or a no-go forcing it to be adjoined; the lock constrains parity only |
| The relative coupling and the mixing angle $\theta_W$ | Blocked | A principle fixing the ratio of the two couplings on the framework's carrier |
| The scalar of the pair, with its potential and its expectation value | Blocked | A gauge-charged scalar with a non-trivial invariant minimum |
| Empirical contact | Open | A prediction distinguishing the framework's group from the product |

**The dependency, in one line.** The chiral action is upstream of everything: without it the compact factor is not weak isospin, and without weak isospin the pair is a direct sum of a vector-like phase and a vector-like rotation, which is a gauge theory and not the electroweak theory. The lock is the one item independent of the chiral question, because it is a property of the group and not of the action.

## What the Article Refuses

**Three inferences, refused here and refused in the audit.** They are the reason the pair needs its own place.

- **"The algebra is the electroweak algebra, so the group is the electroweak group."** False at the group level: the framework's group is the $\mathbb{Z}_2$ quotient. The two agree on the tangent space and differ on the representations, and the representations are where the physics is.
- **"The parity lock derives hypercharge."** False: the lock fixes the parity of the abelian charge against the spin and leaves the scale free. The step six is chosen, and the values remain the model's.
- **"Two couplings from one algebra are one coupling."** False: the algebra is a direct sum of ideals, so the two coefficients are independent and no relation between them is available. The mixing angle is the missing relation, not a missing number.

## Summary

The framework shares the Lie algebra of the electroweak pair, $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$ of real dimension four, and not its group. Its compact group is the quotient $\mathrm{U}(2)=(SU(2)\times\mathrm{U}(1))/\mathbb{Z}_2$, whose kernel is the parity-matched lattice $L=\pi i m\,e_t+\pi n\,\vec U$ with $m\equiv n\pmod 2$; read on representations, the lattice is the lock $q\equiv 2j\pmod 2$ on the integer central charge, which the product group does not impose. The observed hypercharge table satisfies the lock with the least step $q=6Y$, and on that table the lock is the statement that electric charge is quantised in thirds — a consistency check the model meets, not a derivation of its values. The two couplings are free and unrelated, so the mixing angle is not a framework number; the chiral action, the assignment and the scalar remain outside; and the honest statement of the pair is that the framework has its algebra, its two gauge constructions and its group, and not its theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$ | material sector, a direct sum of Lie algebras, $\mathfrak{u}(2)$ of dimension $4$ |
| $\mathrm{U}(2)=(SU(2)\times\mathrm{U}(1))/\mathbb{Z}_2$ | the $*$-unitary slice: the framework's compact group, a quotient |
| $L=\pi i m\,e_t+\pi n\,\vec U$, $m\equiv n\pmod 2$ | kernel lattice of the exponential on the diagonal part |
| $q$ | integer central charge, the label of the abelian factor |
| $j$ | spin label of the $\mathrm{SU}(2)$ factor; $2j$ its parity |
| $q\equiv 2j\pmod 2$ | the parity lock on a $\mathrm{U}(2)$ multiplet |
| $\kappa$, $ϙ$ | the two gauge couplings, on the compact factor and on the centre |
| $T_3$, $Y$, $Q=T_3+Y$ | weak isospin, hypercharge, electric charge (standard notation) |
| $\tan\theta_W=g_{\mathrm Y}/g$ | the mixing angle, a ratio of the two couplings |

## Further Reading

- [$\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$: Two Sides, Six Generators, One Group](su2l-times-su2r-two-sides-six-generators-one-group.html). The doubled group rather than the pair: where the two factors sit in the algebra, the two modules they can act on, and the four roles, of which only one is gauged.
- [The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors](the-standard-model-as-the-low-energy-phase.html) — the audit of the whole model, of which this article is the electroweak part.
- [Electroweak Theory in the Biquaternion Framework: The U(2) Reach and the Chiral Wall](electroweak-theory-in-the-biquaternion-framework-the-u2-reach-and-the-chiral-wall.html) — the sector's own boundary: the chiral obstacle, hypercharge, the scalar sector, fixing the representative.
- [The Gauge Extension of the Central Phase: The Centre Bounds the Symmetry group](the-gauge-extension-of-the-central-phase-the-centre-bounds-the-gauge-group.html) — the quotient, the kernel lattice, and the no-go that caps the group.
- [The Electroweak Symmetry group and the Hypercharge Assignment: The Group and the Derived $Y$](the-electroweak-gauge-group-and-the-hypercharge-assignment.html) — the table used in the check, the anomaly conditions and the three rays.
- [Representation Is a Function of Spin](representation-is-a-function-of-spin.html) — why the representation is read from the carrier, and the one row in three that matches.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the two letters, the selection rule, and the absent chiral symmetry group.
- [Non-Abelian Connections in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) — the compact factor's full gauge construction.
- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) — the ceiling, for the factor that is not there.
- [Grand Unification in the Biquaternion Framework: Where the Embedding Fails](grand-unification-in-the-biquaternion-framework-where-the-embedding-fails.html) — why no larger group fixes the relative coupling.
