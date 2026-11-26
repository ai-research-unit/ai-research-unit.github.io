# __The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors__

## Introduction

The Standard Model is the gauge theory of $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$: three group factor, matter in chiral representations — the left-handed quarks and leptons in $SU(2)_L$ doublets and their right-handed partners in singlets — a scalar doublet whose expectation value breaks the electroweak symmetry and supplies the fermion and weak-boson masses, and hypercharge assignments under which the anomalies cancel. This article's finding is that the framework's own action reaches the machinery of an abelian and a Yang–Mills theory on the largest compact algebra the algebra admits, together with an exact chiral structure on its field, and stops before the Standard Model, whose symmetry group, chiral action, hypercharge and scalar sector it does not derive.

The starting position is stated at the outset, because the finding depends on it and is easy to overstate.

- **The abelian factor.** The centre of the algebra is $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$; its $*$-unitary part is $\mathrm{U}(1)$; localizing a central phase forces a connection with the transformation law $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$, a covariant derivative, and a curvature. This is established in *The Gauge Principle in Biquaternionic Form* and is recalled in the next section.
- **The non-abelian factor.** The material sector decomposes as a Lie algebra, $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, and on the $\mathrm{SU}(2)$ factor the full non-abelian gauge construction — a connection transforming in the adjoint, a curvature containing the commutator term, the Bianchi identity, and an invariant Yang–Mills density — is built. This is established in *Non-Abelian Gauge Fields in Biquaternionic Form* and is recalled in the next section.
- **What is missing.** No source in the series derives a colour group or any three-valued internal structure. The $\mathrm{SU}(2)$ that is present acts vector-like on the field and is therefore not weak isospin. No source derives a hypercharge assignment. The scalar and symmetry-breaking sector is not built.

An article that quietly assumes its way to the Standard Model has fabricated its premise. Each Standard Model structure is therefore carried as an open item, never as a working assumption. Wherever a standard statement is written down — $SU(3)$, $SU(2)_L$, $\mathrm{U}(1)_Y$, the mixing angle, the Higgs doublet, a generation — it is marked as standard input and not as a framework result.

The article sorts every item into one of three categories, and the distinction carries the argument.

1. **Established.**
2. **Obstacle with a known route.** The object does not exist, but the route to it is identifiable, usually because standard field theory or a finite algebraic check supplies the computation and the framework must reproduce it on its own carrier.
3. **Obstacle with no route yet.** No mechanism has been proposed, and naming an object is not the same as having a route to it. Colour, weak isospin, hypercharge, and the scalar sector are in this class.

The spine of the article is the three group factor. Each is stated with its source and its status: $\mathrm{U}(1)$ from the abelian minimal coupling; $\mathrm{SU}(2)$ from the material-sector decomposition; $SU(3)$ from nothing. The pair of which the observed group is a broken phase is treated next, so that the comparison is stated once and not assumed elsewhere. The matter and scalar sectors follow: the chiral-fermion issue is open, hypercharge is underived, and the scalar and symmetry-breaking sector is unbuilt.

Three temptations are refused. (a) The isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, whose commutator algebra contains $\mathrm{SU}(2)$, is not a derivation of $SU(2)_L$: weak isospin is a chiral structure, and the chirality problem must be resolved first. (b) The factors are not assembled into a product group and called the Standard Model's symmetry group, because no hypercharge assignment is derived and one of the three factors is absent altogether. (c) Where the article counts what the framework supplies, it counts framework objects and not Standard Model parameters. Each refusal is argued where it arises.

The Standard Model is the low-energy phase of the four-factor group $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, which is what the transition at $M_C$ reaches: [the frame article](the-su4-model-four-colours-fifteen-generators-one-declaration.html) builds the carrier and the module, and [the group article](su2l-times-su2r-two-sides-six-generators-one-group.html) builds the weak pair at the element level. The ceiling below is a statement about what the algebra's own action carries, and the four factors do not remove it.

**The scope of the finding.** The group whose generators are elements of $\mathbb B$ is $\mathrm{U}(2)$, and none of the Standard Model's four structures is derived there. That is not the test the frame article applies. Its test asks two things: whether a generator lives in $\operatorname{End}_{\mathbb C}(\mathbb B)$, and which module its group acts on. The group passes both, acting on a formal copy of the carrier; the test is stated in the frame article, §*What Is Derived and What Is Declared*. Both statements therefore hold: the algebra's own action stops at $\mathrm{U}(2)$, and the frame admits the four factors, because the Standard Model is what they break to and the address belongs to them rather than to the broken group.

**What the larger test does not reach.** Two of the four unbuilt sectors survive it. $\mathrm{SU}(3)$ and hypercharge are admitted — the first by the split, the second by $T_{3R}+\tfrac12(B-L)$ — but $\mathrm{SU}(2)_L$ as a *chiral* group is not, because the test is about where the generators live and the chirality is about the module. The chiral sector is therefore the permanent obstacle, and the scalar sector is unbuilt on either reading.

## What the Framework Already Reaches

### The abelian gauge principle and the central $\mathrm{U}(1)$

The article *The Gauge Principle in Biquaternionic Form* derives the framework's abelian structure from the centre of the algebra. Its results are established and are recalled here unchanged.

The centre of $\mathbb{B}$ is the complex scalar line $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$, and its $*$-unitary part is

$$
\mathrm{U}(1) \;=\; \{\digamma_{\mathrm{gau}} = \exp(i\theta_{\mathrm{cen}}) : \theta_{\mathrm{cen}} \in \mathbb{R}\} \;\subset\; \mathbb{B}_{C} .
$$

Here $\theta_{\mathrm{cen}}$ is the central phase: it is the argument of a unit complex number, so it is real.

Because $\digamma_{\mathrm{gau}}$ is central and constant, it passes through the gradient, so the massless biquaternion equation $\tilde\nabla_\Phi\tilde{Ξ} = 0$ is invariant under the global phase $\tilde{Ξ}\mapsto \exp(i\theta_{\mathrm{cen}})\tilde{Ξ}$. Making the phase local, $\digamma_{\mathrm{gau}} = \exp(i\theta_{\mathrm{gau}}\tilde{Q})$, forces a connection with the transformation law

$$
\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma,
\qquad
D = \tilde\nabla_\Phi +\frac{2\pi i\,ϙ}{h}\tilde{A}_{\Phi},
\qquad
D_{\imath} = \partial/\partial R_{\imath} +\frac{2\pi i\,ϙ}{h}A_{\imath},
$$

Here $\theta_{\mathrm{gau}}:=ϙ\,\frac{2\pi \Gamma}{h}$ is the gauge angle: the charge $ϙ$ and the phase function $\Gamma$ are real, so the exponent is $i$ times a real number and the link is a phase of modulus one. Where the point $\tilde{Q}$ stands beside the angle, it is a real coordinate and the phase keeps modulus one.

under which $D\tilde{Ξ}$ transforms by the phase factor. The field strength is the vector part of $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}$ and satisfies the curvature identity $[D_{\imath},D_{\jmath}] =\frac{2\pi i\,ϙ}{h}F_{\imath\jmath}$. The abelian symmetry group is canonically attached to the algebra: the only phase that commutes with the whole algebra must lie in the centre, and the centre is one complex dimension, so no choice of representation is made in selecting it.

Two properties of this factor are as important for the article as the factor itself. First, the charge $ϙ$ is a parameter; the algebra does not fix it. Second, a central element acts as a scalar on the algebra: left multiplication by $\digamma_{\mathrm{gau}} = \exp(i\theta_{\mathrm{cen}})$ multiplies every element by the same factor. A symmetry group drawn from the centre therefore assigns every element the same charge — it is vector-like and cannot distinguish left from right. This is established in *Chiral Fermions in the Biquaternion Framework*, and it is the reason the abelian factor as it stands cannot be weak hypercharge, which is chiral.

### The compact algebra inside the material sector

The article *Non-Abelian Gauge Fields in Biquaternionic Form* builds the general non-abelian structure inside $\mathbb{B}$. Its results are established and are recalled here unchanged.

The vector part of the material sector, $\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, closes under the commutator and is $\mathrm{SU}(2)$ in a non-standard normalization,

$$
[e_a,e_b] = 2\,\varepsilon_{abc}\,e_c, \qquad a,b,c = 1,2,3,
\qquad T_a = \tfrac12 e_a,\quad [T_a,T_b] = \varepsilon_{abc}T_c,\quad 2\,\mathrm{Sc}(T_aT_b) = -\tfrac12\delta_{ab}.
$$

The scalar part of $\mathbb{B}_{\Phi}$ is the central line $\mathbb{R}(ie_t)$, so the material sector decomposes as a direct sum of Lie algebras,

$$
\boxed{\;\mathbb{B}_{\Phi} \;=\; \mathbb{R}(ie_t) \;\oplus\; \mathrm{SU}(2) \qquad \text{(direct sum of Lie algebras)}\;}
$$

which is $\mathrm{U}(1)\oplus\mathrm{SU}(2) = \mathrm{U}(2)$ of real dimension $4$. The symmetry group generated by the compact factor is the unit real quaternions, $SU(2) = \{\tilde U \in \mathbb{B}_{H} : \tilde U\bar{\tilde U} = e_t\}$, acting on a matter field by left multiplication. A local transformation $\tilde U(\tilde{Q})$ forces the connection

$$
\mathcal{A}_{2,\imath} = \tilde U\,\mathcal{A}_{\imath}\,\tilde U^{-1} + \frac{i}{\kappa}\,(\partial/\partial R_{\imath} \tilde U)\,\tilde U^{-1},
$$

which reduces to the abelian law $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$ when $\tilde U$ is central. The field strength

$$
F_{\imath\jmath} = \partial/\partial R_{\imath} \mathcal{A}_{\jmath} - \partial/\partial R_{\jmath} \mathcal{A}_{\imath} + i\kappa\,[\mathcal{A}_{\imath}, \mathcal{A}_{\jmath}],
\qquad
F = d\mathcal{A} + i\kappa\,\mathcal{A}\wedge\mathcal{A},
\qquad
[D_{\imath},D_{\jmath}] = i\kappa F_{\imath\jmath},
$$

is **not** invariant but transforms in the adjoint representation, $F_{2,\imath\jmath} = \tilde U F_{\imath\jmath} \tilde U^{-1}$; it satisfies the Bianchi identity $D_{\imath} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0$; and $-\tfrac12\mathrm{Tr}\bigl(\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath} F_{\imath\jmath}F_{\imath\jmath}\bigr)$ is an invariant density, with the matrix trace on the $\mathrm{SU}(2)$ factor and not the informational pairing formula. What this construction supplies is the general machinery of a Yang–Mills theory; what it does not supply is a chiral action of the factor on matter, because left multiplication acts vector-like on the field (the chiral structure is treated below).

One gap in the construction is carried here unchanged, because it bears on how a Standard Model factor could ever be identified. The reality class of the connection is not invariant in a single Hermitian-conjugation eigenspace: the $i r'_t$ derivative makes the Maurer–Cartan form $(\partial/\partial R_{\imath} \tilde U)\tilde U^{-1}$ anti-Hermitian in the spatial directions and Hermitian in the time direction, so a condition placing all four components $\mathcal{A}_{\imath}$ in one eigenspace cannot survive a local transformation. A consistent mixed assignment exists — $\mathcal{A}_0$ anti-Hermitian (in $\mathrm{SU}(2)\subset\mathbb{B}_{\Phi}$), $\mathcal{A}_{\imath}$ Hermitian (in $i\,\mathrm{SU}(2)\subset\mathbb{B}_{\Psi}$) — but whether it is the intended physical one is open. The obstruction is a property of the $i r'_t$ derivative, not of the algebra.

### The ceiling on the gauge algebra

The available algebra is determined by the algebra, not chosen, and it is bounded. The reasoning is inherited from *The Gauge Principle in Biquaternionic Form*, *Non-Abelian Gauge Fields in Biquaternionic Form* and *Modules over the Biquaternion Algebra*.

- **The compact subalgebra has dimension at most four.** The compact algebra present in $\mathbb{B}_{\Phi}$ is $\mathrm{U}(2)$, and $\mathbb{B}\cong M_2(\mathbb{C})$ has the Cartan decomposition
$$\boxed{\;\mathrm{GL}(2,\mathbb{C}) = \mathrm{U}(2)\oplus i\,\mathrm{U}(2), \qquad \dim_\mathbb{R} = 4+4 = 8\;},$$
with $[\mathrm{U}(2),\mathrm{U}(2)]\subseteq\mathrm{U}(2)$ and $[\mathrm{U}(2),i\mathrm{U}(2)]\subseteq i\mathrm{U}(2)$. Because every compact subalgebra of a real Lie algebra lies in a maximal compact subalgebra, and the maximal compact subalgebra of $\mathrm{GL}(2,\mathbb{C})$ is a conjugate of $\mathrm{U}(2)$, any compact algebra that is a subalgebra of $\mathbb{B}$ under the commutator has, on the present construction, real dimension at most $4$.
- **Every module has even complex dimension.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and Artinian, so every module is a direct sum of copies of its unique simple module, which is $\mathbb{C}^2$. Consequently every $\mathbb{B}$-module has complex dimension divisible by two, and a three-dimensional internal space for a quark is not a $\mathbb{B}$-module.

This is the precise ceiling of the present construction. The non-abelian machinery is real, and it is real for $\mathrm{U}(2)$; a colour theory needs a compact simple algebra of dimension $8$ and a three-dimensional module, and neither is available. The ceiling is the formal reason the framework stops where it does, and it is the reason colour is an obstacle with no route yet rather than a gap with a known route.

### Which claims are theorems and which are readings

**Three grades.** The ceiling admits three kinds of claim, and they are kept apart. A theorem survives a change of interpretation; a reading is revised when a better one appears.

- **Theorem.** The compact subalgebra of $\mathbb{B}$ has real dimension at most four. The Cartan decomposition of $\mathrm{GL}(2,\mathbb{C})$, the maximality of its compact part and the closure of every compact subalgebra in a maximal one are the whole proof.
- **Theorem.** Every $\mathbb{B}$-module has complex dimension divisible by two, because the algebra is simple and Artinian with unique simple module $\mathbb{C}^2$.
- **Interpretation.** That the first theorem *is* a no-go of the Coleman–Mandula type — that a compact internal symmetry commuting with the Lorentz action is what the theorem forbids, and that the theorem therefore explains the shape of the observed spectrum — is a reading. It is a good reading, because the compact part is the rotation group and a group commuting with the rotations is what gauge theory would need; it is not a corollary of the dimension count, and no dimension count alone excludes a large internal group in some other framework.
- **Forbidden inference.** That the ceiling makes the Standard Model impossible in principle. It bounds the algebras available inside $\mathbb{B}$ under the commutator. A construction that enlarged the algebra, or that reached the internal factors by a route other than a subalgebra of $\mathbb{B}$, is not touched by the count.

### The chiral structure: two values on one element

The article *Chiral Fermions in the Biquaternion Framework* establishes the framework's chirality kinematics, and this article inherits it without change.

**The field is one element.** The field of the framework is an element $\tilde{Ξ}$ of $\mathbb{B}$. Its chirality is the slot of an operator, and one basis operator supplies the sign: $\mathsf{V}_{\mathrm{vol}}=-iR_{\mathrm{axf},\vec e_z}$ is a pure right multiplier and therefore an example of the right slot (*Special Element Conventions*, §*The Chirality Convention*). The basis operator is named here once, because the subscript of the element is read from it, and the label it shows is the side.

**Two values, and no third.** The basis operator gives the subscript its two values: $L$ for the minus value and $R$ for the plus value. The field is the sum of its two parts,

$$
\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R},
$$

and only the zero element is both. That is the whole of the chirality. Everything below is read from it by two laws of the subscript — a product takes the letter of its right factor, and left multiplication keeps the letter (*Matrix Representations Conventions*, §*The Legacy Pauli Gamma Formulation*) — and by the one law of the units that the basis operator fixes: right multiplication by $\vec e_t$ or by $\vec e_z$ keeps the letter, and right multiplication by $\vec e_x$ or by $\vec e_y$ exchanges the two, because $\vec e_z$ commutes with the first pair and anticommutes with the second.

**Constants of the free equation.** The Lorentz action on the field multiplies on the left, and left multiplication keeps the letter; the chirality multiplies on the right, and right multiplications commute with left multiplications. The chirality basis operator therefore commutes with the gradient, and the two values are conserved by the free equation.

**The mass bilinear is mixed.** The Dirac mass bilinear is the scalar part of an element product built on the timelike unit,

$$
B=\mathrm{Sc}\bigl(\tilde{Ξ}^*i\,\tilde{Ξ}\,\vec e_x\bigr),
$$

where $\tilde{Ξ}^*i\,\cdot\,\vec e_x$ is the framework's adjoint pairing, written with the star of the algebra. Both of its properties follow from the letter law, and both are derived forms. Right multiplication by $\vec e_x$ exchanges the two letters, so $B$ pairs each part with the other and not a part with itself: it vanishes on an element of one letter. The chirality keeps the letter, and $\vec e_z$ anticommutes with $\vec e_x$, so the chirality reverses $B$. A bare mass term is available for a mixed element and not for a part of definite letter.

**The chiral abelian symmetry.** On the field, a chiral abelian local symmetry with independent charges is consistent. The charge is one right action, by the element

$$
b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z\in\mathbb{B}_{\Psi},
$$

so that $\tilde{Ξ}_{L}b=ϙ_L\tilde{Ξ}_{L}$ and $\tilde{Ξ}_{R}b=ϙ_R\tilde{Ξ}_{R}$, and its covariant derivative and the curvature it gives are these

$$
D_{\imath}\tilde{Ξ}=\frac{\partial}{\partial R_{\imath}}\tilde{Ξ}+\frac{2\pi i}{h}A_{\imath}\,(\tilde{Ξ} b),
\qquad
[D_{\imath},D_{\jmath}]\tilde{Ξ}=\frac{2\pi i}{h}F_{\imath\jmath}\,(\tilde{Ξ} b).
$$

The derivative is covariant for arbitrary $ϙ_L,ϙ_R$, and the mass bilinear is invariant if and only if $ϙ_L = ϙ_R$. This mass selection rule is the framework's form of the Standard Model's requirement that a chiral fermion acquire mass only through a compensating scalar. Both are the chiral article's, written with the charge element $b$.

**The centre gives one charge, not two.** The framework's own symmetry group, drawn from the centre, is vector-like: a central element multiplies every element by the same scalar, so the two parts receive the same charge, and it cannot be a chiral symmetry group. (The article records a qualification: under the alternative real-structure reading the central phase would act axially, with $\exp(i\theta_{\mathrm{cen}})$ on the $L$ part and $\exp(-i\theta_{\mathrm{cen}})$ on the $R$ part, and which reading is physical is not settled. Under neither reading does the centre supply independent left and right charges, so a derived chiral symmetry group remains out of reach either way.)

**The mass term is the linear pair.** The framework's mass term is the linear chiral pair

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R} = 2\pi\nu_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = 2\pi\nu_m\tilde{Ξ}_{R},
$$

through which the continuous central phase passes: the vector $\mathrm{U}(1)$ is conserved for the massive field, and what the mass breaks is the axial symmetry, whose current carries the chirality as a right factor of the field. The algebra's anti-linear object is the real structure $\tilde{Ξ}^{\flat} = -\tilde{Ξ}^*$, whose separate conjugate pairing — Majorana-type or the real form of an ordinary Dirac mass — is the open reading treated in *The Neutrino and Majorana Fermions in Biquaternionic Form*. Here $\nu_m=\frac{mc}{h}$ is the mass wave number, the inverse of the mass length.

## The Three Gauge Factors

### $\mathrm{U}(1)$: present, but not weak hypercharge

The source is *The Gauge Principle in Biquaternionic Form*. The minimal coupling is established; the identification with weak hypercharge is not made, and no route to it exists.

What is established is a single abelian group factor, canonical and vector-like: the $*$-unitary part of the centre, with connection law $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$ and curvature $[D_{\imath},D_{\jmath}] =\frac{2\pi i\,ϙ}{h}F_{\imath\jmath}$. What weak hypercharge requires is a factor that (i) carries a definite set of assignments — different eigenvalues on different Standard Model multiplets, the pattern that makes $Ϙ = T_3 + Y$ work and that cancels the anomalies — and (ii) acts chirally, with independent left and right charges on a single fermion, since the left- and right-handed components of the Standard Model fermions carry different hypercharge.

The framework's abelian factor supplies neither. Its action is a scalar multiplication, so it gives every element the same charge; under the alternative real-structure interpretation it would be axial, but still a single one-dimensional charge with no room for independent left and right assignments. And the coupling $ϙ$ is one parameter, not a table. There is no object in the series from which the numbers $1/6$, $-1/2$, $2/3$, and so on could be read off. An abelian group factor is established; weak hypercharge is not derived, and no computation in the series points toward it. This item is filed as no route yet.

### $SU(2)$: the algebra is present, weak isospin is not

The source is *Non-Abelian Gauge Fields in Biquaternionic Form*, on the decomposition $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$. The compact algebra, the connection and the full non-abelian gauge construction are established; the identification with $SU(2)_L$ is not, and is blocked on the chirality problem.

The $\mathrm{SU}(2)$ factor is genuinely there: $\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ closes under the commutator with $[e_a,e_b] = 2\varepsilon_{abc}e_c$, the connection transforms in the adjoint, and the Yang–Mills density is invariant. So the framework supplies a compact simple group factor of exactly the dimension and rank that $SU(2)$ has, with the general machinery attached. It is tempting to conclude that $SU(2)$ — and therefore, with the abelian factor, the electroweak symmetry group — has been derived. It has not. The reason is the trap this article exists to mark.

**The coincidence is not the derivation.** The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, whose commutator algebra $\mathrm{GL}(2,\mathbb{C})$ contains $\mathrm{SU}(2)$ — indeed many conjugates of it, and the unit-norm real quaternions generate one. That $\mathrm{SU}(2)$ is available is a fact about the algebra; it does not make the factor the Standard Model's weak isospin. The group factor of the non-abelian article acts on matter by left multiplication, and a left multiplication by $\tilde U$ keeps the letter of each part while multiplying both parts by the same $\tilde U$. The two values of the chirality therefore carry the same action: it is vector-like. $SU(2)_L$ is a chiral local symmetry — its left-handed doublets and right-handed singlets transform inequivalently — so the vector-like $\mathrm{SU}(2)$ of the algebra is not $SU(2)_L$, however compact and however correctly normalized. The chirality problem must be resolved first, and it is not resolved.

**The chirality problem is upstream and open.** What the framework has is exact chirality kinematics on the field (the two parts named by the subscript, the mass bilinear, the selection rule) and an abelian chiral charge carried by one right multiplication, $b$. What it does not have is a non-abelian chiral gauge group: a non-central action of a compact factor under which the two values of the chirality transform inequivalently. The chiral article states the obstruction plainly — a chiral gauge action has $ϙ_L\neq ϙ_R$ and cannot be central, so it is not supplied by the framework's $\mathbb{B}$-valued gauge principle — and the non-abelian article supplies the algebra but not the chiral action. *The Neutrino and Majorana Fermions in Biquaternionic Form* records the same conclusion for the weak interaction: the framework "does not derive the Standard Model's chiral $SU(2)_L$ structure; it transcribes a chiral gauge theory onto the module, with the chiral assignment put in by hand." Since the assignment is put in by hand, the item is classified **no route yet**.

The reality-class gap of the non-abelian article is a second, smaller obstacle on this factor: even the connection's Hermitian-conjugation class is not settled in a single eigenspace, and the mixed assignment that does close has not been tied to a physical principle. It is filed as a known route, because the computation that would settle it is finite and identifiable.

### $SU(3)$: nothing derives a three

No source derives it, and no route to it exists.

$SU(3)$ is not in the framework, on the present construction, for two independent reasons, both stated in the ceiling above: its algebra $\mathrm{SU}(3)$ has real dimension $8$, while every compact subalgebra of $\mathbb{B}$ under the commutator has dimension at most $4$; and its quark fundamental $\mathbf{3}$ would be a complex three-dimensional module, while every $\mathbb{B}$-module has complex dimension divisible by two. There is no colour group, no triplet, no octet, no colour coupling, and no confinement mechanism anywhere in the series. The article *Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated* carries this gap as its central open item and is the place where its consequences are developed; this article inherits the negative result and does not restate its argument.

The one candidate ever named in the series is an enlargement of the carrier — a module built by tensoring the algebra's own with an internal factor $X$, or an endomorphism algebra built from the algebra's own structures — in which a larger internal factor could act. It is named as a candidate only, because it either assumes the answer by choosing $X = \mathbb{C}^3$ or has no known outcome. Writing $SU(3)$ down and proceeding is the fabricated premise the article exists to prevent. **No route yet.**

The exceptional groups are that same candidate in its extreme form. Two instances of the enlargement dominate the literature, and both are recorded here for the same reason the smaller ones are: they are targets, not routes. The first is the $E_8$ programme, in which the connections and the fermions of a generation are placed in the adjoint $\mathbf{248}$, the smallest faithful representation of $E_8$; the second is the $E_8\times E_8$ of heterotic string compactification, of rank sixteen and dimension $496$, in which the Standard-Model group is a subgroup of the commutant of a broken factor. Set against the framework's ceiling these are the same enlargement of the carrier pushed to its largest known form: the compact subalgebra of $\mathbb{B}$ has dimension at most four, the intrinsic group is $\mathrm{U}(2)$ of rank two, the algebra's module has complex dimension two, and a carrier able to hold a $\mathbf{248}$ or a $\mathbf{496}$ is the candidate with the largest carrier anyone has written down. Naming $E_8$ therefore does not supply the missing three, and the table below is unchanged by the naming.

There is a second reason to treat the exceptional rungs differently from the others, and it is not a framework argument. Whether the observed chiral fermions can be placed in $E_8$ at all, with the Standard-Model symmetry group as the commutant, was examined exhaustively by Distler and Garibaldi; their conclusion is that the only embeddings compatible with the Standard-Model symmetry group require the fermions to fill a complete $\mathbf{248}$, that is three generations together with a conjugate set, and that the resulting spectrum is not chiral in the required sense without additional matter or a second $E_8$. The $E_8$ rung is thus closed on its own terms, before the framework's ceiling is consulted. This is a sharper version of the caution the article exists to enforce — that a large group is not an explanation — and it is why the exceptional candidates are recorded here with a negative result attached rather than as open candidates.

### The product group is not assembled

**Trap (b).** It is tempting to assemble the two available factors, add colour, and write the Standard Model's symmetry group. That would be naming the target and calling it the result.

What the framework's compact algebra actually is, as a Lie algebra, is $\mathrm{U}(2) = \mathrm{U}(1)\oplus\mathrm{SU}(2)$ — locally the same direct sum $\mathrm{SU}(2)\oplus\mathrm{U}(1)$ that the electroweak sector has, and at the level of the group not the same object: the framework's group is the quotient $(SU(2)\times\mathrm{U}(1))/\mathbb{Z}_2$ and the Standard Model's is the product, so the abelian charge of a framework multiplet is locked in parity to its spin. The framework's $\mathrm{U}(1)$ is the centre, acting as a scalar and giving equal charges to all components; the Standard Model's $\mathrm{U}(1)_Y$ is chiral, with independent left and right eigenvalues and a definite assignment pattern. The framework's $\mathrm{SU}(2)$ acts vector-like, not as $SU(2)_L$. No mixing angle exists, because a mixing angle is a relation between two independent couplings and the framework supplies no relation.

The electroweak part is developed on its own in *The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock*, which carries the group-level distinction, the parity lock read on representations, the check of the observed hypercharge table against it, and the pair's own table of items. This article keeps the one-line statement and does not restate the argument. The gap, in one line, is this: the framework reaches the Lie algebra of the electroweak pair as a direct sum of a vector-like abelian factor and a vector-like $\mathrm{SU}(2)$, and it does not reach the pair as a theory.

### Why the Standard Model Gauges One Side and Not Two

**The group is available, and the question is why only half of it is used.** The pair $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ sits in the endomorphisms of $\mathbb{B}$ at the element level and at no cost, as $L(\mathfrak{k})\oplus R(\mathfrak{k})=\mathfrak{so}(4)$; [The Group, the Two Sides, and Six Generators](su2l-times-su2r-two-sides-six-generators-one-group.html) builds it there and lists the four roles it plays in physics. **The statement this section makes is not a framework derivation**: the pair is itself framed on a formal copy of the carrier, so nothing here derives the observed group. What it does is locate the observed group inside the larger one, and state what the larger one costs.

**The first reason is the charged current.** Reinstating parity would require a right-handed charged current of the same size as the observed one, and it is not there. The measured parity violation is maximal and not partial, so the two factors cannot be even approximately symmetric at the electroweak scale. This is the reason that is quoted, and it is the weakest of the four, because it is a statement about the vacuum rather than about the group.

**The second is the right-handed neutrino.** For the right-handed electron to be a doublet it needs a partner, and the only candidate is a right-handed neutrino. That state is not required by the observed spectrum and has never been seen as a gauge state; it is allowed, and its mass is bounded from above only by cosmology. So the group costs a particle the low-energy content does not need.

**The third is structural, and it is the sharpest: the group forces the sixteen.** Electric charge in the frame is

$$
Q=T_{3L}+T_{3R}+\tfrac12(B-L),
$$

so $B-L$ must itself be a generator of the symmetry group, because $Q$ is a combination of them — a direction of the simple group above $M_C$, which the transition then breaks. And the abelian factor is anomaly-free exactly when the right-handed neutrino is included, since the two conditions

$$
\textstyle\sum(B-L)=0,\qquad \sum(B-L)^{3}=0
$$

hold on the sixteen and fail on the fifteen. The chain is then a sequence of implications rather than a choice:

$$
\text{gauge }\mathrm{SU}(2)_R\ \Longrightarrow\ \text{gauge }B-L\ \Longrightarrow\ \xi_{\mathrm{neu},R}\ \text{required}\ \Longrightarrow\ \text{matter is sixteen}.
$$

**A theory with half the group is free to be odd, and the observed one is odd.** The arithmetic is in [Anomalies and Anomaly Cancellation](anomalies-and-anomaly-cancellation.html), and the count is in the content section below.

**The fourth reason is that the factor is broken, not absent, and hypercharge is its remnant.** The neutral generator of the broken factor survives as a circle and mixes with $B-L$:

$$
Y=T_{3R}+\tfrac12(B-L).
$$

**The check is exact, and it is the reason hypercharge is not an independent invention in this frame:**

| field | $T_{3L}$ | $T_{3R}$ | $B-L$ | $Y=T_{3R}+\tfrac12(B-L)$ | $Q=T_{3L}+Y$ |
|---|---|---|---|---|---|
| $\xi_{\mathrm{neu},L}$ | $+\tfrac12$ | $0$ | $-1$ | $-\tfrac12$ | $0$ |
| $e_L$ | $-\tfrac12$ | $0$ | $-1$ | $-\tfrac12$ | $-1$ |
| $\xi_{\mathrm{neu},R}$ | $0$ | $+\tfrac12$ | $-1$ | $0$ | $0$ |
| $e_R$ | $0$ | $-\tfrac12$ | $-1$ | $-1$ | $-1$ |
| $u_L$ | $+\tfrac12$ | $0$ | $+\tfrac13$ | $+\tfrac16$ | $+\tfrac23$ |
| $d_L$ | $-\tfrac12$ | $0$ | $+\tfrac13$ | $+\tfrac16$ | $-\tfrac13$ |
| $u_R$ | $0$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ | $+\tfrac23$ |
| $d_R$ | $0$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ | $-\tfrac13$ |

**Two readings of that table, and the second is the one worth keeping.** The first is bookkeeping: the hypercharges come out right, so the relation is true. **The second is structural: the charge formula is parity-symmetric.** The two Cartans enter $Q$ on the same footing, and $Y$ is by definition the piece beyond $T_{3L}$, so substituting $T_{3R}$ for $T_{3L}$ throughout returns the same formula with the same charges. **The observed theory therefore does not violate parity by its charges; it violates it by its multiplet assignment** — a doublet here, a singlet there, and the right-handed neutrino omitted. **Parity is broken by the choice of module and not by the choice of numbers**, which is why the framework's hypercharge item is filed as underived rather than as contradicted: the assignment is the missing object, and the arithmetic above does not supply it.

**The chiral wall closes the argument, and this is where it differs from the reasons above.** From the group article: non-abelian chiral one-sided multiplication does not exist. The observed $SU(2)_L$ couples only to left-handed fields, so it is chiral non-abelian, so the algebra cannot supply it as a one-sided action. **That is the ceiling of this article restated at the pair**, and it is the reason the parity question cannot be settled by choosing a bigger group: the missing object is the tie between an operator side and a spinor letter, not a generator.

**The chain, in the form [The Matching at $M_C$](matching-at-m-c-the-four-quantities-that-cross-and-where-the-masses-come-from.html) owns.**

$$
\mathrm{SU}(4)\ \xrightarrow[\ M_C\ ]{\ \langleΞ\rangle\ }\
\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R
\ \xrightarrow[\ M_C\ ]{\ \langleΞ\rangle\ }\
\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_{Y}
\ \xrightarrow[\ v\ ]{\ \langle H\rangle\ }\
\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}} ,
$$

**The middle arrow is the same arrow read on the other factor, not a second event.**

**One transition at $M_C$ — breaking and decoupling in the same step — and one breaking at $v$.** The four-factor group is the group at $M_C$ and has no width: the same vacuum that makes it makes the right-handed bosons heavy. **So the Standard Model is not a theory that declined the pair; it is the description of a theory whose pair is heavy**, and hypercharge is the left-over of the right factor. **The scale of that breaking is bounded from below only**, so nothing forbids the pair and nothing requires it — which is why the fourth role of the group article is a hypothesis and not a fact, and why this article's ceiling survives the framing: a larger group does not build the objects the ceiling counts.

**What this section adds to the audit's checks.**

| claim | check | result |
|---|---|---|
| hypercharge | the eight rows against $Y=T_{3R}+\tfrac12(B-L)$ | all eight exact |
| the parity reading | substitute $T_{3R}$ for $T_{3L}$ in $Q$ | the same formula, the same charges |
| the sixteen | the two $B-L$ anomaly sums | $0$ and $0$ on sixteen, not on fifteen |

**What the section does not claim.** That the framework derives the pair, the breaking, or the hypercharge table. The pair is imported on a formal copy of the carrier; the breaking is a scalar sector this article files as unbuilt; and the assignment is put in by hand. **The section's content is the comparison between two imported frames, and its only framework statement is the negative one: the algebra supplies the group and does not supply the module.**

## The Matter Sector: Chirality, Hypercharge, Content

### The chiral-fermion issue

The Standard Model's matter is chiral: the left-handed quarks and leptons sit in $SU(2)_L$ doublets, their right-handed partners in singlets, and no invariant bare fermion mass exists. The framework reaches the kinematics of chirality and not its dynamics.

Established and inherited: the field as one element with its two values; the mixed, chirality-odd mass bilinear $B$; the chiral abelian charge as one right multiplication, by $b$, with the covariant derivative it gives; and the selection rule $ϙ_L = ϙ_R$ for an invariant bare mass. These are exact and are the framework's form of the statement that a chiral fermion is massless in the unbroken phase.

Not established: a chiral symmetry group. The framework's canonical symmetry group is the scalar centre, which assigns one charge to every element; the abelian chiral charge is one right multiplication, by $b\in\mathbb{B}_{\Psi}$, and a charge of that form coincides with a left multiplication by an element of $\mathbb{B}$ — the form the framework's connection takes — only when $b$ is central, that is when $ϙ_L=ϙ_R$; and a non-abelian chiral action requires non-commuting generators that are not supplied. The chiral article's summary is that without those conditions the framework has no chiral symmetry group at all. The neutrino article reaches the same place from the weak-interaction side and calls the chiral assignment an empirical input. The item is **no route yet**.

### Hypercharge is underived

The Standard Model's hypercharge is a specific $\mathrm{U}(1)$ with a specific assignment table and a chiral action, and it is the ingredient that makes the electric charge $Ϙ = T_3 + Y$ and cancels the gauge and gravitational anomalies. The framework has a $\mathrm{U}(1)$ — the $*$-unitary centre — but the assignment table is not derivable from it, and no source in the series supplies one. The only abelian charge the framework possesses is a single parameter $ϙ$, the same for every element; the gauge principle supplies no second abelian direction, no non-central abelian action is available to it, and there is no anomaly computation from which an assignment could be inferred. **No route yet.** The eight-row check of §*Why the Standard Model Gauges One Side and Not Two* does not change this: it is a consistency check inside an imported frame, and it begins from $B-L$ eigenvalues the frame assigns by hand.

### The content is not selected — and what the framework supplies, counted

**Trap (c).** A count of free parameters or of fields can be read as a statement about the Standard Model if it is not said exactly what is being counted. The count given here is a count of what the framework supplies, and of what it does not; it is not a count of Standard Model fields and not a count of Standard Model parameters.

The framework supplies:

- **One compact group factor of each kind.** One abelian factor — the $*$-unitary centre, real dimension $1$ — and one compact simple factor — $\mathrm{SU}(2)$, real dimension $3$ — joined in the material sector's Lie algebra $\mathrm{U}(2)$ of real dimension $4$.
- **One exact chiral structure on the field**, on the element $\tilde{Ξ}$ and its two values, with a chirality-odd mass bilinear and the selection rule.
- **The general connections, curvatures, Bianchi identities, and invariant densities** on the two factors, each carrying a coupling parameter whose value the algebra does not fix, and with no relation between the two couplings.

The framework does not supply, and nothing in the series derives: a colour group or colour representation; a chiral $SU(2)_L$; a hypercharge value or assignment; a mixing angle; a scalar field with the Standard Model's quantum numbers, its potential, or its vacuum expectation value; a Yukawa coupling; the number of fermion generations or the representation content of any generation; or a relation among the couplings of its factors. These are the absent objects. Writing a number here for the Standard Model — three colours, three generations, a stated hypercharge — would be importing the target; the article counts only the framework's own objects, and the count is short.

## The Scalar and Symmetry-Breaking Sector: Unbuilt

The Standard Model's masses come from one sector the sources this article builds on have not begun: a scalar field with the required $SU(2)_L$ quantum numbers, its potential, its vacuum expectation value, and its Yukawa couplings to the fermions. The companion *The Higgs Mechanism in Biquaternionic Form* works the abelian mechanism for the complex central scalar $\tilde{Ξ} = \xi_{\mathrm{scl}}\,e_t$; that scalar is a singlet of the material $\mathrm{SU}(2)$ and cannot break $SU(2)$, no Yukawa coupling is constructed, and the Standard Model's electroweak scalar sector is not built.

The framework does point at what the sector would have to do. The mass selection rule says that a fermion with $ϙ_L\neq ϙ_R$ has no invariant bare mass, so a mass can arise only through a compensating field carrying the opposite charge $ϙ_L-ϙ_R$; the chiral article reads off the quantum numbers such a scalar must carry. That is a statement of the requirement, not a construction of the object. There is no dynamics that would give the scalar an expectation value, no potential whose minimum could break the symmetry, and no coupling to the sector that would give the weak bosons a mass. The framework's own mass term is the linear chiral pair, which conserves fermion number and breaks the axial symmetry; the algebra's real structure $\flat$ carries a separate conjugate pairing whose interpretation — Majorana-type or real-form Dirac — is open, and it is the pairing of a single fermion, not a symmetry-breaking sector.

This is the largest single missing piece on the way from the gauge machinery to the Standard Model, and it is classified **no route yet**.

## The Items and Their Status

The table collects the article's items and sorts each into one of the three categories. "Established" means recomputed in the series and inherited here; "known route" means the object does not exist but the computation that would produce it is identifiable; "no route yet" means no mechanism has been proposed.

| Item | Status | Object or computation that would settle it |
|---|---|---|
| Abelian minimal coupling: centre $\mathbb{B}_{C}$, $*$-unitary $\mathrm{U}(1)$, connection $\tilde{A}_{\Phi,2}=\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$, covariant derivative, curvature identity | Established | — |
| Compact algebra in the material sector: $[e_a,e_b]=2\varepsilon_{abc}e_c$, $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)=\mathrm{U}(2)$ | Established | — |
| Non-abelian machinery: adjoint connection law, commutator curvature, Bianchi identity, invariant Yang–Mills density | Established | — |
| Ceiling: compact subalgebra of $\mathbb{B}$ has dimension $\le 4$; every $\mathbb{B}$-module has complex dimension $2k$ | Established | — |
| Chiral structure on the field: the fifth basis operator of the frame, the two parts named by the subscript, the chirality-odd bilinear $B$, the chiral abelian charge $b$, selection rule $ϙ_L=ϙ_R$ | Established | — |
| Vector-like character of the centre, read on the two values of the field | Established | — |
| Linear chiral mass with conserved vector $\mathrm{U}(1)$; real structure $\flat$ (antilinear) | Established; interpretation of $\flat$'s pairing (Majorana/Dirac) open | Decide the interpretation on the real structure |
| Reality class of the non-abelian connection | **Known route** | Recompute the transformation for the mixed assignment ($\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_{\imath}$ Hermitian) and find a principle fixing the placement of $i$; or a no-go |
| Non-abelian matter representation | **Known route** | Construct the action of the factor on the chosen matter field and verify $D_{2,\imath}(\tilde U\tilde{Ξ})=\tilde U D_{\imath}\tilde{Ξ}$ |
| Gauge and gravitational anomalies of a chiral spectrum | **Known route** in standard field theory; no framework realisation | A biquaternion computation of the axial-current divergence or the triangle diagram |
| Fixing the representative principle | **Known route** in standard field theory; no framework realisation | Reproduce the Faddeev–Popov or BV procedure in the algebra, or prove a no-go |
| Electroweak mixing angle | **Known route, blocked** | Fix $\mathrm{U}(1)_Y$ and $SU(2)_L$ and the scalar from the framework's own structure, then compute the relative coupling |
| $SU(2)_L$: chiral weak isospin | **No route yet** | A non-central compact action on the field under which the two values transform inequivalently; the chirality problem is upstream |
| $\mathrm{U}(1)_Y$ and the hypercharge assignments | **No route yet** | A derivation of a non-central abelian direction and its assignment table; none exists in the series |
| $SU(3)$ and the number of colours $N_c=3$ | **No route yet** | A positive internal construction with a principle selecting three, or a no-go covering all enlargements; positing is not a route |
| Exceptional carriers: $E_6$, $E_7$, $E_8$, $E_8\times E_8$ | **No route yet** (targets, not candidates) | A principle selecting a carrier of dimension $27$, $56$, $248$ or $496$; the $E_8$ case is closed on its own terms by Distler–Garibaldi |
| Scalar and symmetry-breaking sector | **No route yet** | A biquaternion scalar in the required non-abelian representation, with a symmetry-breaking potential, a vacuum expectation value, and Yukawa couplings |
| Fermion generations and representation content | **No route yet** | A principle selecting the matter content; none is proposed |
| Empirical contact | Open | A prediction distinguishing the framework from the Standard Model |

## The Object Each Row Needs

The obstacles are not independent, and the dependency chain is short.

The three **upstream** items are (1) the **chirality problem** — a non-central compact action on the field under which the two values transform inequivalently; (2) the **hypercharge problem** — a non-central abelian direction with a derivable assignment table; and (3) the **scalar sector** — a biquaternion scalar with a potential, an expectation value, and Yukawa couplings. Everything else hangs from them. Weak isospin needs (1); the electroweak pair needs (1) and (2) together; the mixing angle needs (1), (2), and (3); fermion masses need (3); and the anomaly conditions need a chiral spectrum first, which is (1).

Two further items are upstream in a different sense, because they are prerequisites for stating any of the above as a framework result rather than a transcription. The **reality class of the connection** must be settled, since a group factor whose connection cannot be assigned a definite conjugation behaviour cannot be cleanly identified with a Standard Model factor; and the **matter representation** must be constructed, since the non-abelian article's connection acts by left multiplication and the representation carried by the matter field has not been specified. Both are classified as known routes precisely because the computations are finite and identifiable: the first is a transformation check, the second is a covariance check, and both were performed in the parents for the cases they consider.

What is not on this list, and is the point of the article, is a derivation of the Standard Model. None of the three upstream items exists; colour does not exist for independent reasons; and no item on the list, if settled, would by itself produce the Standard Model. The three-way classification is not a schedule with three phases. It is a statement that some of the framework's gaps have a computation attached and some do not, and that the line between them is where the framework's relation to the Standard Model has to be described.

Finally, a standing caution applies here in its strongest form. *The Empirical Status of the Biquaternion Framework* records that on every domain developed, the framework is so far empirically equivalent to the standard theory it reformulates. A biquaternionic Standard Model, if one is ever constructed, would inherit that position unless it makes a prediction the Standard Model does not; and a theory whose symmetry group, matter content, hypercharge, and scalar sector are all imported has no prospect of doing so. That consequence is worth stating early, rather than producing a construction that appears to answer the Standard Model while assuming all of it.

## The Interpretive Default, and the Paper Route to the Scalar Sector

A short 2001 comment by Gsponer and Hurni on biquaternion formulations of the Dirac, Proca and Maxwell equations supplies the default reading of an extra component, a legitimacy test, and a prior-art warning; the corpus collects all three, with the Einstein–Mayer equation as their worked instance, in [Reading an Extra Component: The Gürsey Default, the Reversion Test, and the Prior-Art Warning](reading-an-extra-component-the-gursey-default-the-reversion-test-and-the-prior-art-warning.html). This article uses them and does not restate them.

What they settle here, in one line each. An extra component is read as a spin or isospin multiplicity rather than as new physics; a formulation is legitimate when every field is irreducible under the full Poincaré group including the discrete symmetries and the equation is covariant under reversion; and a biquaternion result is a re-description of standard physics until it supplies a prediction, which is the same caution [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html) records domain by domain.

**The one place they touch the table.** The scalar row above is marked no route yet, and the qualifier is the word *route*: a route exists on paper and does not become one here. Promoting the mass to an Einstein–Mayer element $E$ turns the Lanczos pair's second-order equations into eigenvalue equations for it, the degenerate case $EE^{\dagger}=m^2$ reads as an isospin doublet, the null case $EE=0$ as an electron–neutrino doublet with one mass vanishing, and the reading of $E$ as a Higgs-type field, $\Box_\Phi E=-\mu E+\digamma_{\mathrm{qtc}} EE^{\dagger}E$ invariant under $E\to G^{*}EH$, carries the manifest $SU(2)_L\times SU(2)_R$ symmetry of the sigma model. That is a literature route dating from 1932, and the source's own verdict on it is that its outputs are Standard Model re-descriptions and not derivations. The row stays **no route yet** because the framework supplies no such field with the required quantum numbers, and writing one down is not deriving it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*. The generators carry no frame label: $\gamma_{\imath}$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications of *Operator and Calculus Conventions*.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

A single basis operator is one term; a general element of the sixteen-dimensional algebra is a sum of at most four.

$\gamma_5$ is the reference-frame basis operator of the chirality operator; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, and $\gamma_5$ is its representative in the display.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every basis operator printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose form the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_{\imath}}=C_{\Pi}L_{\mathrm{pau},e_{\imath}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. A basis operator is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free form is the conjugate. The label names the display and not the operator.

## Summary

The finding of this article is that the framework's own action reaches the general machinery of an abelian and a Yang–Mills theory, on the largest compact algebra the algebra admits, together with an exact chiral structure on its field — and that it stops before the Standard Model, whose symmetry group, chiral action, hypercharge, and scalar sector it does not derive. The larger group of the frame admits colour and hypercharge, and the chiral action stays out of reach there.

What is established is recalled: the abelian minimal coupling on the centre, with $\mathrm{U}(1)$ canonically attached and the connection law $\tilde{A}_{\Phi,2}=\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$; the compact algebra inside the material sector, $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, with the full non-abelian construction — adjoint connection, commutator curvature, Bianchi identity, invariant Yang–Mills density; the ceiling, that a compact subalgebra of $\mathbb{B}$ on the present construction has real dimension at most $4$ and every $\mathbb{B}$-module has even complex dimension; and the chiral structure on the field, with the two parts named by the subscript, the chirality-odd mass bilinear, and the selection rule $ϙ_L=ϙ_R$.

What is not established is everything Standard-Model-specific.

- **$\mathrm{U}(1)$.** The abelian group factor exists and is canonical, but it is vector-like on the field and supplies one charge, not a hypercharge assignment table. **No route yet.**
- **$SU(2)$.** The compact algebra and its gauge machinery exist, but the factor acts vector-like, so it is not $SU(2)_L$; weak isospin is chiral and the chirality problem is unresolved. The isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, whose commutator algebra contains $\mathrm{SU}(2)$, is a coincidence of algebra, not a derivation of weak isospin. **No route yet.**
- **$SU(3)$.** Nothing derives a colour group or a three-valued internal structure; the dimension ceiling and the module-dimension parity forbid both on the present construction. **No route yet.**
- **The product.** The framework's compact algebra $\mathrm{U}(2)$ is locally the electroweak direct sum $\mathrm{SU}(2)\oplus\mathrm{U}(1)$, but the abelian factor is vector-like, no hypercharge assignment is derived, and the relative coupling and mixing angle are unconstrained. The factors are present as a direct sum; the electroweak theory is not. The group-level statement — the quotient against the product, the parity lock, and the check of the observed hypercharge table — is *The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock*.
- **The pair.** $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ is available at the element level and the observed group is its broken phase, with hypercharge as the survivor and the sixteen forced by the anomaly conditions. That chain is a comparison between two imported frames; it derives neither the group nor the assignment, and the charge formula being parity-symmetric is a statement about the numbers and not about the multiplets.
- **The matter sector.** The chirality kinematics are exact; the chiral symmetry group is absent, the hypercharge is underived, and the representation content and generation number are not selected. **No route yet.**
- **The scalar sector.** Unbuilt. The mass selection rule names what a compensating scalar would have to carry, and the framework supplies no scalar field with the required quantum numbers, and no corresponding potential, expectation value, or Yukawa coupling. **No route yet.**

The obstacles with a known route are the finite, identifiable ones: the reality class of the non-abelian connection, the non-abelian matter representation, the anomaly, the principle that fixes the representative, and — conditional on the no-route items above — the electroweak mixing. The upstream items are the chirality problem, the hypercharge problem, and the scalar sector. None of them exists, and settling any one of them would not by itself produce the Standard Model.

No section assumes a Standard Model structure. The three group factor are each stated with their source and status, and where standard numbers appear they are marked as imports. The boundary is the result.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_{\imath}^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors; $\mathbb{B}=\mathbb{B}_{\Phi}\oplus\mathbb{B}_{\Psi}$ |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; source of the abelian symmetry group |
| $\tilde\nabla_\Phi = e_t\partial/\partial R_t+\sum_{\imath}\,\vec e_{\imath}\partial/\partial R_{\imath}$ | Biquaternionic gradient |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ | d'Alembertian |
| $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A$ | Abelian connection (in $\mathbb{B}_{\Phi}$) |
| $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$ | Abelian local transformation |
| $D = \tilde\nabla_\Phi +\frac{2\pi i\,ϙ}{h}\tilde{A}_{\Phi}$ | Abelian covariant derivative |
| $[e_a,e_b]=2\varepsilon_{abc}e_c$, $T_a=\tfrac12 e_a$ | Commutator and normalized generators of $\mathrm{SU}(2)\subset\mathbb{B}_{\Phi}$ |
| $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)=\mathrm{U}(2)$ | Material-sector Lie-algebra decomposition (dimension $4$) |
| $\mathcal{A}_{\imath}\in\mathrm{SU}(2)$, $\kappa=\frac{2\pi ϙ}{h}$ | Non-abelian connection and coupling |
| $F_{\imath\jmath}=\partial/\partial R_{\imath}\,\mathcal{A}_{\jmath}-\partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}+i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$ | Non-abelian field strength |
| $F_{2,\imath\jmath}=\tilde UF_{\imath\jmath}\tilde U^{-1}$, $[D_{\imath},D_{\jmath}]=i\kappa F_{\imath\jmath}$ | Adjoint transformation law and curvature identity |
| $D_{\imath} F_{\imath\jmath}+\text{cyclic}=0$ | Bianchi identity |
| $-\tfrac12\mathrm{Tr}\bigl(\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath} F_{\imath\jmath}F_{\imath\jmath}\bigr)$ | Invariant Yang–Mills density |
| $\mathrm{GL}(2,\mathbb{C})=\mathrm{U}(2)\oplus i\,\mathrm{U}(2)$ | Cartan decomposition fixing the ceiling: maximal compact subalgebra $\mathrm{U}(2)$ |
| $\tilde{Ξ}$, $\tilde{Ξ}_{L}$, $\tilde{Ξ}_{R}$ | The field as one element and its two values: $L$ is the minus value, $R$ the plus value, and only the zero element is both |
| every $\mathbb{B}$-module | complex dimension $2k$; a three-dimensional internal space is not a module |
| $-iR_{\mathrm{axf},\vec e_z}$ | The fifth basis operator of the frame: a pure right multiplication, and the source of the two parts named by the subscript |
| $B=\mathrm{Sc}(\tilde{Ξ}^*i\,\tilde{Ξ}\,\vec e_x)$, $b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z$ | Chirality-odd mass bilinear; chiral charge as one right multiplication, $\tilde{Ξ}\mapsto\tilde{Ξ} b$; selection rule $ϙ_L=ϙ_R$ |
| $\tilde\nabla_\Phi\tilde{Ξ}_{R}=2\pi\nu_m\tilde{Ξ}_{L},\ (\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=2\pi\nu_m\tilde{Ξ}_{R}$; $\tilde{Ξ}^{\flat}=-\tilde{Ξ}^*$ | Linear chiral mass pair; algebra real structure $\flat$ (Majorana/Dirac reading of its pairing open) |
| $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Inherited plain trace reading |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| **Standard-model notation, not framework objects** | |
| $SU(3)_c$, $SU(2)_L$, $\mathrm{U}(1)_Y$ | Colour, weak-isospin and hypercharge groups — no route yet |
| $T_3$, $Y$, $Ϙ=T_3+Y$ | Weak isospin, hypercharge, electric charge — underived |
| $T_{3L}, T_{3R}$, $B-L$ | The two weak Cartans and the fourth-colour diagonal, written out where the pair's hypercharge relation is checked |
| $\theta_W$ | Electroweak mixing angle — no relation supplied |
| Higgs doublet, vacuum expectation value, Yukawa coupling | Scalar and symmetry-breaking sector — unbuilt |

## Further Reading

- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [The Group, the Two Sides, and Six Generators](su2l-times-su2r-two-sides-six-generators-one-group.html) — $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ built at the element level, its two modules, and the four roles it plays; §*Why the Standard Model Gauges One Side and Not Two* above is where this audit uses it.
- [The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html) — the electroweak part of this audit developed on its own: the algebra shared and the group not shared, the parity lock on the representations, the hypercharge table checked against it, and the pair's table of items.
- [The Minimal coupling in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) — the abelian minimal coupling, the centre and its $*$-unitary part, the connection, the covariant derivative, and the origin of the $\mathrm{U}(1)$ factor this article follows.
- [Non-Abelian Connections in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) — the immediate parent; the decomposition $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, the adjoint connection and curvature, the Bianchi identity, the invariant density, and the open reality-class gap.
- [The Covariant Derivative and Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) — the abelian connection whose non-abelian extension the parent builds.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the field's chirality structure, the vector-like centre, the mass selection rule, the linear mass and the real structure, and the statement that the framework has no chiral symmetry group.

- [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) — the Dirac/Weyl/Majorana distinction, the real-structure interpretation, and the explicit statement that the chiral $SU(2)_L$ assignment is empirical input.

- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html) — the colour gap, the ceiling on the algebra, and the three-way classification this article shares.
- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html) — the one-loop non-abelian beta function and the article's own statement that the group, matter, action, and regulator are inputs; the caution against reading a transcription as a derivation.
- [Modules over the Biquaternion Algebra](../articles_maths/the-category-of-modules-in-the-biquaternion-algebra.html) and [Lie Algebras: A General Introduction](../articles_maths/lie-algebras-a-general-introduction.html) — the module structure and the compact-subalgebra facts behind the ceiling.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) and [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the spinor module, the mass term, and the real-structure origin of chirality.

- [Peirce Decompositions of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) — the ideal decomposition, distinguished from the chiral and sector decompositions.
- [Helicity in Biquaternionic Form](helicity-in-biquaternionic-form.html) — the corpus's explicit statement that the framework "does not contain a colored gauge theory"; the transcription boundary this article makes systematic.
- [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html) — the standing empirical-equivalence result, the caution under which any biquaternionic Standard Model would labour.
- [Reading an Extra Component: The Gürsey Default, the Reversion Test, and the Prior-Art Warning](reading-an-extra-component-the-gursey-default-the-reversion-test-and-the-prior-art-warning.html), for the Lanczos doubling, the Gürsey isospin reading, the Poincaré-and-reversion legitimacy test, the Einstein–Mayer equation and the prior-art warning, with the primary sources listed there.
- Jacques Distler and Skip Garibaldi, "There is no $E_8$ gauge theory with three generations" (arXiv:0905.2658), for the exhaustive check that the Standard Model's chiral fermions do not fit in $E_8$ with the Standard-Model gauge group as the commutant; the basis of the row on the exceptional carriers.
- Garrett Lisi, "An exceptionally simple theory of everything" (arXiv:0711.0770), for the $E_8$ programme that places one generation of fermions and the gauge fields in the adjoint $\mathbf{248}$; recorded as the instance of the exceptional candidate, and as a target rather than a route.
- David J. Gross, Jeffrey A. Harvey, Emil Martinec and Ryan Rohm, "Heterotic string theory (I). The free heterotic string", *Nuclear Physics B* 256 (1985) 253–284, for the $E_8\times E_8$ gauge group recorded above as the top rung of the rank ladder.
- G. Petiau, *Il Nuovo Cimento* **40** (1965) 84–101, for the double-periodic waves of the derivatively coupled system.
- [The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap](the-einstein-field-equations-in-the-biquaternion-framework-the-linearised-dictionary-and-the-non-linear-gap.html) — the companion article whose three-way classification and settling-object discipline this article follows.
- [Four-Vectors and the Interval](four-vectors-and-the-interval.html) and [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) — the two sectors, the four-vectors, and the pairing formula on which the whole account rests.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html) — the algebra, the conjugations, and the research-program framing inherited throughout.
