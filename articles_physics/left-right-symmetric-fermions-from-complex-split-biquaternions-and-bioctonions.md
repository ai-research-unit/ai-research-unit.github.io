
# __Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions__

## Introduction

The Standard Model treats the two chiralities of the fermions unequally: the left-handed components sit in $\mathrm{SU}(2)_L$ doublets and the right-handed components in singlets, and no right-handed neutrino is required at all. The left-right symmetric models of Pati and Salam and of Mohapatra and Pati restore the symmetry by enlarging the electroweak factor to $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, so that every left-handed doublet has a right-handed partner and the right-handed neutrino becomes a member of an $\mathrm{SU}(2)_R$ doublet — a gauge singlet of the Standard Model, and therefore **sterile**, but a state of the larger theory. A construction of Vaibhav and Singh builds exactly this pairing out of a pair of division-algebra Clifford algebras: the complex **split biquaternion** algebra $\mathrm{Cl}(3)$ for the leptons and the complex **split bioctonion** algebra $\mathrm{Cl}(7)$ for the quarks, each splitting into two copies of a smaller algebra — $\mathrm{Cl}(2)$ and $\mathrm{Cl}(6)$ respectively — which carry the two chiralities and are interchanged by a parity automorphism. This article states the algebraic core of that construction and sorts its steps into what is established, what is read, and what is left open.

The algebraic core is proved for the lepton case in the companion mathematics article, and the quark case is the same statement one dimension up. The complex split biquaternions and the doubling
$$
\mathrm{Cl}(3) \cong \mathrm{Cl}(2)\oplus\mathrm{Cl}(2) \cong \mathbb{B}\oplus\mathbb{B}
$$
are the subject of *Complex Split Biquaternions and the Clifford Algebra Cl(3)*; the complex split bioctonions double in the same way,
$$
\mathrm{Cl}(7) \cong \mathrm{Cl}(6)\oplus\mathrm{Cl}(6),
$$
by the same computation of the volume-element square, which *The Two Algebraic Facts* below redoes for both cases; and the octonionic chain algebra $\mathrm{Cl}(6)\cong M_8(\mathbb{C})$, with its ladder operators, its intrinsic $\mathrm{su}(3)\oplus\mathrm{u}(1)$, its primitive idempotent and its charge spectrum $0,\tfrac13,\tfrac13,\tfrac13,\tfrac23,\tfrac23,\tfrac23,1$, is the complex octonionic chain algebra, whose physics interpretation is *The Particle Roster of the Complex Octonionic Chain Algebra*. The neutrino content against which the construction is compared is *The Neutrino and Majorana Fermions in Biquaternionic Form* and *The Seesaw Mechanism and Majorana Mass in Biquaternionic Form*; the anomaly conditions that decide whether a sterile state is allowed are *Anomalies and Anomaly Cancellation in Biquaternionic Form*; the framework's own ledger on the electroweak factor, on the generation count and on the ceiling it cannot pass is *The Standard Model under the Biquaternion Framework — A Research Agenda*, *The Number of Generations and the Biquaternion Algebra* and *Grand Unification and the Biquaternion Algebra Ceiling*; and the exceptional structures of the source's further programme are outside the framework's algebra.

As in *The Particle Roster of the Complex Octonionic Chain Algebra*, the construction is **outside the biquaternion algebra**: $\mathbb{B}\cong M_2(\mathbb{C})$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, the chain algebras here are $\mathrm{Cl}(6)$ and $\mathrm{Cl}(7)$, of complex dimensions $64$ and $128$, and no operation of $\mathbb{B}$ reaches them. The article is in the physics category as a record of the literature's most economical answer to the chirality and sterile-neutrino questions, not as a derivation inside the framework, and no result of it feeds back into the framework's ledger. Besides the doubling and its interpretation, the record covers the further pieces of the source: the explicit construction by which each of the two weak factors is made to act on one chirality only, with the part of it recomputed here marked; the interpretation of the volume element as the Higgs; the source's proposal that the two chiralities existed in a combined leptoquark state before symmetry breaking; the source's later programme, in which the right-handed weak factor becomes a chiral formulation of gravity in a ten-dimensional octonionic pre-spacetime and the second summand's charge becomes a square root of mass; and the $\mathrm{Cl}(5)$ statement that the right action of $\mathbb{C}\otimes\mathbb{H}$ on $\mathrm{Cl}(3)$ generates $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, recomputed in the companion mathematics article.

## The Two Algebraic Facts

Two structural facts are all that the construction's treatment of chirality uses, and both are recomputed below. They are statements about **cells**, so the article fixes that language first.

**Cells.** For $a$ and $b$ in the algebra, $L_a:x\mapsto ax$ and $R_b:x\mapsto xb$ are the left and the right multiplication, and the two-sided operator is the cell
$$
T_{a,b}:=L_aR_b,\qquad T_{a,b}\,x=axb,\qquad T_{a,b}T_{c,d}=T_{ac,db},
$$
the right factors multiplying in reverse order. Every sign below follows from that rule together with $i^2=-1$ and $\vec e_k^{\,2}=-e_t$. The gamma frame is written once, in *The Legacy Pauli Gamma Formulation* at the end; nothing before it uses one.

**The doubling.** Each of the two algebras has a central volume element which is an involution. The complex split biquaternions $\mathrm{Cl}(3)$ are generated by $E_\mu=j\vec e_\mu$, with $\vec e_\mu$ the quaternion units and $j$ the split unit, $j^2=1$; the volume element is $\omega=E_1E_2E_3$. The complex split bioctonions $\mathrm{Cl}(7)$ are generated by $e_1,\dots,e_7$, and the volume element is $J=e_1\cdots e_7$. All Clifford algebras here are complex: $\mathrm{Cl}(n)$ means $\mathrm{Cl}(n,\mathbb{C})$, and a real form is written out, as $\mathrm{Cl}_{1,3}(\mathbb{R})$. In both cases the idempotents $\Pi_{1,2}=\tfrac12(1\pm\omega)$ and $\tfrac12(1\pm J)$ are a complete family of orthogonal central idempotents, so that the algebra is the direct sum of two copies of the smaller one,
$$
\boxed{\;\mathrm{Cl}(3) \cong \mathrm{Cl}(2)\oplus\mathrm{Cl}(2), \qquad \mathrm{Cl}(7) \cong \mathrm{Cl}(6)\oplus\mathrm{Cl}(6)\;}.
$$
The two squares follow from one computation. For a product of $n$ anticommuting generators of common square $c$,
$$
(E_1\cdots E_n)^2=(-1)^{n(n-1)/2}\,c^{\,n},
$$
which gives $(-1)^{3}(-1)^{3}=+1$ at $n=3$ and $(-1)^{21}(-1)^{7}=+1$ at $n=7$: both volume elements are involutions. Each is central because a generator moves past the other $n-1$ factors at the cost of $n-1$ signs, an even number at $n=3$ and at $n=7$.

The parity automorphism $\sigma:e_i\mapsto-e_i$, fixing the even elements and negating the odd ones, sends $\omega\mapsto-\omega$ and $J\mapsto-J$ and thereby interchanges the two copies. The copies are the two **pinor representations**, inequivalent, distinguished by the eigenvalue $\pm1$ of the central volume element.

**$\omega$ is a sign, not an exchange.** What multiplication by $\omega$ does has to be stated on its own, because two decompositions are easily run together. Since $\Pi_{1,2}$ project on the two summands and $\omega\Pi_1=\Pi_1$, $\omega\Pi_2=-\Pi_2$, multiplication by $\omega$ **preserves** each summand and multiplies it by $\pm1$. The operator that **exchanges** the summands is $\sigma$, and $\sigma$ is outer: an inner automorphism fixes every central element, while $\sigma(\omega)=-\omega$. What multiplication by $\omega$ does exchange is another pair of subspaces, the diagonal and the anti-diagonal halves of the faithful representation of the real form, $\mathrm{Cl}(0,3)\cong\mathbb{H}\oplus\mathbb{H}$. The split unit is central with $j^2=1$, so it acts as a scalar in each component and $E_\mu=j\vec e_\mu$ is a quaternion unit up to that sign; with the signs and the quaternion basis chosen so that
$$
E_1\longmapsto(\vec e_x,\vec e_x),\qquad E_2\longmapsto(\vec e_y,\vec e_y),\qquad E_3\longmapsto(\vec e_z,-\vec e_z).
$$
The volume element is then the product of three quaternionic units in each component,
$$
\omega\longmapsto(\vec e_x\vec e_y\vec e_z,\,-\vec e_x\vec e_y\vec e_z)=(\vec e_z\vec e_z,\,-\vec e_z\vec e_z)=(-1,+1),
$$
so with $x$ quaternionic it acts on the diagonal half $\{(x,x)\}$ and the anti-diagonal half $\{(x,-x)\}$ by
$$
(x,x)\longmapsto(-x,x),\qquad (x,-x)\longmapsto(-x,-x),
$$
which carries each half to the other, with $\omega^2=1$, $\omega$ central and $\omega^{*}=\omega$ (residuals $0$). These two halves are the two sets in which the source writes its left- and right-handed states; they are not the two central summands, which $\omega$ preserves. The distinction is used twice below, in the interpretation of the two chiralities and in the Higgs interpretation.

**The two $\mathrm{SU}(2)$ factors from the left and the right.** On the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ there are two commuting actions of the quaternion units, the left multiplications $L_{x}:y\mapsto xy$ and the right multiplications $R_{x}:y\mapsto yx$. They compose in opposite orders,
$$
L_aL_b=L_{ab},\qquad R_bR_c=R_{cb},
$$
so the left action generates a copy of $\mathbb{H}$ and the right action the opposite algebra $\mathbb{H}^{\mathrm{opp}}$, which is isomorphic to $\mathbb{H}$ through conjugation but is a different copy. The imaginary part of each is a Lie algebra isomorphic to $\mathrm{su}(2)$; the real span of the six cells $L_{\vec e_k}^{\mathrm{axf}},R_{\vec e_k}^{\mathrm{axf}}$ is $\mathrm{so}(4)\cong\mathrm{su}(2)\oplus\mathrm{su}(2)$, and the two $\mathrm{su}(2)$'s commute. Together the two actions generate the full endomorphism algebra,
$$
\boxed{\;\operatorname{span}_{\mathbb{C}}\{\,T_{a,b}:a,b\in\mathbb{B}\,\} = \operatorname{End}_{\mathbb{C}}(\mathbb{B}) \cong M_4(\mathbb{C}) \cong \mathrm{Cl}(4)\;},
$$
the complexified Dirac algebra, of complex dimension $16$. These statements were checked on the four-dimensional model of $\mathbb{B}$: the left and right actions commute identically, $L_{\vec e_x}^{\mathrm{axf}}L_{\vec e_y}^{\mathrm{axf}}=L_{\vec e_z}^{\mathrm{axf}}$ while $R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=R_{\vec e_y}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=-R_{\vec e_z}^{\mathrm{axf}}$, each action spans a four-dimensional algebra, the six imaginary cells span a six-dimensional Lie algebra closed under the commutator, and the span of the sixteen cells $T_{a,b}$ is sixteen-dimensional, i.e. all of $M_4(\mathbb{C})$.

## The Left-Right Symmetric Interpretation

**The two copies as the two chiralities.** The doubling is the construction's answer to the chirality problem. Where the single chain algebra $\mathrm{Cl}(6)$ of *The Particle Roster of the Complex Octonionic Chain Algebra* carries one generation in one chirality, and reaching the second chirality there takes another ideal together with an enlarged supercharge sector; the doubled algebra carries the two chiralities as its two simple summands. The interpretation is that one summand is the left-handed sector and the other the right-handed sector. The parity automorphism $\sigma$, which interchanges them, is then the discrete left-right symmetry of the left-right symmetric model. The two summands carry the same intrinsic $\mathrm{su}(3)\oplus\mathrm{u}(1)$ and the same charge spectrum, because the ladder operators, the number operator and the $\mathrm{su}(3)$ generators all commute with the volume element $J$ — the centrality established above — so that the two sectors differ in chirality and in nothing else. The states of one summand are

$$
\boxed{\;1(0),\quad 3(\tfrac13),\quad 3(\tfrac23),\quad 1(1)\;}.
$$

That is the charge multiset of half a generation, and the summand's conjugate ideal supplies the antiparticles, exactly as in the undoubled construction of the particle-roster article.

**The chirality trap.** The chirality is carried by **which set** a state comes from and not by its expression: the source's own equations give the same element $\tfrac12(1+ie_1e_2)$ for the left-handed neutrino of the first set and the right-handed neutrino of the second, and the source says so explicitly. That element is idempotent for the usual reason, $(ie_1e_2)^2=i^2\,e_1e_2e_1e_2=(-1)(-1)=+1$, with $e_1,e_2$ the chain-algebra generators of the summand. A second object of the same shape appears below and must not be identified with it: the right-action factor carries $P=\tfrac12(1+i\vec e_x\vec e_y)$, built from the quaternion units of $\mathbb{C}\otimes\mathbb{H}$ and idempotent for the same reason, $\vec e_x\vec e_y$ squaring to $-1$. One is a projector of the chain algebra, the other of the right action. A reader who looks for two different algebraic expressions for the two chiralities will not find them; the element that gives the sets their relative sign is the volume element $\omega$, treated below, while the automorphism that exchanges the two summands is $\sigma$.

**The weak factors from the two actions.** The weak $\mathrm{SU}(2)$ factors come from a different place, and the two facts of the previous section have to be kept apart. The doubling supplies the two chiralities, and the two commuting quaternion actions of the biquaternion algebra supply two commuting $\mathrm{su}(2)$ algebras. The interpretation is that the left action is $\mathrm{SU}(2)_L$ and the right action is $\mathrm{SU}(2)_R$: the left multiplications act on the internal biquaternion index of the states, the right multiplications act on a separate one, and the two commute by the computation above, so that the states of the doubled construction can be organised into doublets of the left action and doublets of the right action without the two actions interfering. The isospin structure that the undoubled construction had to leave to an interpretation — the second non-abelian factor whose absence makes the minimal version non-chiral — is here supplied by the right action, and the electroweak factor of the enlarged theory is the $\mathrm{su}(2)\oplus\mathrm{su}(2)=\mathrm{so}(4)$ of the previous section. The source's mechanism is more specific: the right action of the quaternion units on the ideal is stated to annihilate the right-handed component while interchanging the two isospin states of the left-handed component, so that the two factors act on opposite chiralities, which is the defining statement of the left-right symmetric model. 
The corpus records the finite algebraic facts — the commutation of the two actions, the generation of $M_4(\mathbb{C})$, and the diagonalisation of the right action on the ideal — and marks the identification of the two actions with the two weak factors of the model as an interpretation, because the precise isospin alignment depends on the supercharge sector chosen and is not fixed by the algebra alone. The mechanism itself — which state the generators annihilate and which pair they interchange — is worked out below in *Why Each Factor Acts on One Chirality Only*, where its algebraic skeleton is recomputed and the part that remains an interpretation is named.

**The right-handed neutrino.** With the right-handed sector present, the state of the second summand of charge $0$ is available: a neutral, colourless, $\mathrm{SU}(2)_L$-singlet fermion, which is the right-handed neutrino $\nu_R$. In the Standard Model this state is not required — the fifteen states of a generation are the left-handed doublet, the right-handed singlets and their conjugates, and the right-handed neutrino can be dropped because it is a complete gauge singlet under $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$. It is exactly because it is sterile that the construction's presence of it is conspicuous: a sterile fermion is unconstrained by the anomaly conditions, which act only on the gauge-charged content, so the doubling costs nothing at the level of gauge consistency and adds a state that the Standard Model's own ledger must otherwise introduce by hand for neutrino mass. This is the construction's sharpest contact with the framework's ledger: the framework's own count of the electroweak factor is $\mathrm{U}(2)$ and never $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, and its $\nu_R$ status is exactly the question this construction answers by construction rather than by addition.

**The Pati–Salam interpretation.** The full gauge group of the left-right symmetric unification is the Pati–Salam group
$$
\mathrm{SU}(4)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R ,
$$
in which the colour $\mathrm{SU}(3)_c$ and the baryon-minus-lepton number $\mathrm{U}(1)_{B-L}$ sit inside $\mathrm{SU}(4)_c$, and the two $\mathrm{SU}(2)$'s act on the two chiralities. The construction supplies the two $\mathrm{SU}(2)$'s from the two quaternion actions, and the $\mathrm{SU}(3)$ from the maximal totally isotropic subspace of the octonionic chain algebra in each summand. The abelian direction that the chain algebra itself supplies is the number-operator charge $Ϙ=\tfrac13N$, with the spectrum $0,\tfrac13,\tfrac23,1$; the particle-roster article reads $Ϙ$ as the electric charge, and the $B-L$ of the Pati–Salam group is a different combination, with the values $(\tfrac13,\tfrac13,\tfrac13,-1)$ on each colour-lepton quartet. Which combination $Ϙ$ is — the hypercharge $Y$, the electric charge $T_3+Y$, or $B-L$ — is one of the three commutator tests that the roster article leaves open, and the present article does not decide it. The assignment of the states to the Pati–Salam multiplets, in the source's interpretation, places one generation of quarks and leptons, with both chiralities, in the doubled algebra; the corpus does not recompute the multiplet assignment, and records it as an interpretation, in the same sense as the particle-roster article's assignment of its sixteen states.

**The weak bosons as ladder operators.** The source identifies the composite ladder operator $\Omega_L=\alpha_1\alpha_2\alpha_3$ of each summand with the charged weak boson: $\Omega_L$ has charge $-1$ and $\Omega_L^{\dagger}$ charge $+1$ under the number-operator charge, right multiplication by $\Omega_L$ changes a particle's isospin from up to down and right multiplication by $\Omega_L^{\dagger}$ reverses that on the antiparticles, so that $\Omega_L,\Omega_L^{\dagger}$ "mimic" $W^-$ and $W^+$. In the doubled algebra the same statement is made for the second summand's $\Omega_R,\Omega_R^{\dagger}$ as the right-handed analogues. This is an interpretation of the ladder operators that the chain-algebra article already uses — the corpus records it and notes that a ladder operator has the charge and the isospin action of a $W$, but that the construction contains no gauge field, no kinetic term and no coupling, so "mimics the $W$" is a correspondence of quantum numbers, not a derivation of the weak interaction. The source later abandons this assignment for the right sector in favour of using $\mathrm{SU}(2)_R$ for gravity, as recorded under *the further programme* below; the corpus keeps both statements with that shift marked.

## The Two Dirac Equations in Cells

The construction is a finite algebra, and the source writes no equation of motion. The corpus's dictionary does supply one, and it is worth writing here because it separates two things that the construction runs together: the two-sidedness of the operator algebra and the two chiralities. The equation comes in two forms, and they must not be read as one.

**The one-sided pair.** The biquaternion Dirac field is a section of the Dirac module $\Delta=S\oplus\bar S$, with $S$ and $\bar S$ the two chiral halves of *Chiral Fermions in the Biquaternion Framework*, and the equation is the chirality-off-diagonal pair
$$
\begin{aligned}
L_{\tilde\nabla}\tilde\Psi_R&=m\,\tilde\Psi_L,\\
L_{\tilde\nabla^{\natural}}\tilde\Psi_L&=m\,\tilde\Psi_R,
\end{aligned}
$$
with $\tilde\nabla=e_t\,\partial/\partial Q_t+\vec e_x\,\partial/\partial Q_x+\vec e_y\,\partial/\partial Q_y+\vec e_z\,\partial/\partial Q_z$ and $\tilde\nabla^{\natural}$ its quaternion conjugate. The first is the right-handed equation and the second the left-handed one; the $\natural$ in the second is what makes the pair real-linear, and each line is a left multiplication of the field. At $m=0$ the two lines decouple into the two Weyl equations $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^{\natural}\tilde\Psi_L=0$; at $m\ne0$ the mass couples them, and eliminating one half leaves the Klein–Gordon equation. **Two equations, one per chirality** — that is the content of the word "pair".

**The two-sided single equation.** Read on the algebra rather than on the module, the same content is one equation whose two sides are the two multiplications,
$$
L_{\tilde\nabla^{\natural}}F=m\,T_{e_t,-i\vec e_z}\bar F=m\,\chi\,\bar F,
$$
where $F\in\mathbb{B}$, $\bar F$ is the coefficient conjugate, and
$$
\chi:=T_{e_t,-i\vec e_z}=L_{e_t}^{\mathrm{axf}}R_{-i\vec e_z}^{\mathrm{axf}}=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}
$$
is the chirality cell, with the $i$ extracted from the right multiplier since right multiplication is complex-linear, $R_{-i\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$, and with $L_{e_t}^{\mathrm{axf}}=I_4$ dropped in the last step. Its square is exact,
$$
\chi^2=(-i)^2R_{\vec e_z^{\,2}}^{\mathrm{axf}}=(-1)\cdot(-I_4)=I_4,
$$
using $i^2=-1$ and $\vec e_z^{\,2}=-e_t$; and $\chi$ anticommutes with each of the four frame cells of *The Legacy Pauli Gamma Formulation*, so it commutes with every even product of them. Those even products span eight dimensions of operators on $\mathbb{B}$, and because $\chi$ commutes with all of them $\chi$ is block diagonal for them; each of the two blocks is the full $M_2(\mathbb{C})$, so the even algebra is $\mathrm{Cl}(3)\cong\mathbb{B}\oplus\mathbb{B}$, its two summands acting on the two $\chi$-eigenspaces. That is the doubling of the first section, read inside the frame. The derivative acts on the left and the mass on the right: the two sides of the single equation are the two multiplications of the cell algebra.

**Why the two forms are worth keeping apart.** The one-sided pair is the definition and the two-sided equation is the form the corpus's operator calculus uses; the two are related by a real-linear dictionary, not by an identity of operators. The construction touches both. It supplies the two chirality spaces on which the one-sided pair acts — one per summand of $\mathrm{Cl}(3)\cong\mathbb{B}\oplus\mathbb{B}$ — and it reads the left and the right action as the two weak factors, so the two-sided equation's division of labour, derivative on the left and mass on the right, is the same division of labour as the article's $\mathrm{SU}(2)_L$ and $\mathrm{SU}(2)_R$. The mass cell $\chi$ is a right multiplication, hence an element of the right action. What the construction does not supply is the equation itself: the source has no derivative, no kinetic term and no mass, and the pair above is the corpus's equation written in the cells of the construction's algebra.

## Why Each Factor Acts on One Chirality Only

The interpretation above identifies the left action with $\mathrm{SU}(2)_L$ and the right action with $\mathrm{SU}(2)_R$ and leaves open the mechanism that makes each act on one chirality only.

**The construction.** Let $\alpha_1,\alpha_2,\alpha_3$ be the octonionic ladder operators and $\Omega_L=\alpha_1\alpha_2\alpha_3$ the composite one, in the complex octonionic chain algebra. The source acts on a tensor product of the ladder side of the chain algebra with the four-dimensional right-action space $\mathbb{C}\otimes\mathbb{H}$ with basis $(\vec e_t,\vec e_x,\vec e_y,\vec e_z)$; what the isospin statement below uses of the ladder side is only the two-dimensional module $\{\Pi_{\mathrm{ch}},\Omega_L^{\dagger}\Pi_{\mathrm{ch}}\}$ that its triple acts on, with $\Pi_{\mathrm{ch}}$ the primitive idempotent of the chain algebra. On that second factor the cells $T_{a,b}=L_aR_b$ with $a,b\in\mathbb{B}$ span $\mathrm{Cl}(4)\cong M_4(\mathbb{C})$, which is the source's "the right action of $\mathbb{C}\otimes\mathbb{H}$ on $\mathbb{C}\otimes\mathbb{H}$ gives $\mathrm{Cl}(4)$"; the symbols $\vec e_x,\vec e_y$ below are the quaternion units of that factor, not the generators of $\mathrm{Cl}(7)$.

The isospin triple is built from the ladder operator alone,
$$
\tau_1=\Omega_L+\Omega_L^{\dagger},\qquad
\tau_2=i\bigl(\Omega_L-\Omega_L^{\dagger}\bigr),\qquad
\tau_3=1-2N,\qquad N=\Omega_L^{\dagger}\Omega_L ,
$$
all three Hermitian, $\tau_3$ taking the values $\pm1$ on the two-dimensional module the triple acts on. The qualification matters, because $\Omega_L$ is a composite of three ladder operators and $\{\Omega_L,\Omega_L^{\dagger}\}=1$ is **not** an identity on the eight-dimensional ideal: there $\Omega_L\Omega_L^{\dagger}$ is the projector on the state of zero occupation of the three oscillators and $N$ the projector on the fully occupied state, each of rank $1$, and their sum is the projector $\Pi_\Omega$ on the two-dimensional module $\{\Pi_{\mathrm{ch}},\Omega_L^{\dagger}\Pi_{\mathrm{ch}}\}$ those two states span, not the identity. So $\tau_3^2=1$ on the whole ideal, while $\tau_1^2=\tau_2^2=\Pi_\Omega$, and $\tau_3$ agrees with $\Omega_L\Omega_L^{\dagger}-\Omega_L^{\dagger}\Omega_L$ only on the module, the two expressions differing elsewhere by the complementary projector. On the module, where the anticommutator does equal $1$, the triple closes on $\mathrm{su}(2)$ with the orientation reversed,
$$
[\tau_1,\tau_2]=-2i\tau_3,\qquad [\tau_2,\tau_3]=-2i\tau_1,\qquad [\tau_3,\tau_1]=-2i\tau_2,
$$
the reversed orientation being what the source's factor of $i$ in $\tau_2$ produces, and $\operatorname{tr}\tau_3=0$ there. Off the module only the first relation fails, and it fails by the complementary projector, $[\tau_1,\tau_2]+2i\tau_3=2i\,(1-\Pi_\Omega)$; the other two hold on the whole ideal. The states are built from the totally isotropic elements
$$
\beta_1=\tfrac12\bigl(-\vec e_x+i\,\vec e_y\,\tau_3\bigr),\qquad
\beta_2=\Omega_L^{\dagger}\,i\,\vec e_y ,
$$
where $\tau_3$ acts on the ladder factor and $\vec e_x,\vec e_y$ on the right-action factor, so the two commute. Isotropy is a cancellation of signs:
$$
\beta_1^2=\tfrac14\Bigl(\vec e_x^{\,2}+i^2\,\vec e_y^{\,2}\tau_3^2\Bigr)
=\tfrac14\bigl(-1+(-1)(-1)(+1)\bigr)=0,
$$
the cross terms cancelling because $\vec e_x\vec e_y=-\vec e_y\vec e_x$ and $[\tau_3,\vec e_x]=[\tau_3,\vec e_y]=0$; and
$$
\beta_2^2=i^2\,\vec e_y^{\,2}\,(\Omega_L^{\dagger})^2=0
$$
because $(\Omega_L^{\dagger})^2=0$, since $\Omega_L^2=0$. The idempotent and its excitations are
$$
V_R=\beta_1^{\dagger}\beta_2^{\dagger}\beta_2\beta_1,\qquad
V_L=V_R\beta_1^{\dagger},\qquad e^-_R=V_R\beta_2^{\dagger},\qquad e^-_L=V_R\beta_1^{\dagger}\beta_2^{\dagger}.
$$
The isospin generators of the doubled ideal are the products of the triple with the primitive idempotent of the right-action $\mathrm{Cl}(2)$,
$$
T_a=\tau_a\,P,\qquad P=\tfrac12\bigl(1+i\,\vec e_x\vec e_y\bigr).
$$

**$P$ is a left multiplication, not a mixed cell.** It acts on the right-action factor by left multiplication, $L_P=\tfrac12\bigl(L_{e_t}^{\mathrm{axf}}+i\,L_{\vec e_x}^{\mathrm{axf}}L_{\vec e_y}^{\mathrm{axf}}\bigr)$. Left multiplication is an algebra map, so $L_{\vec e_x\vec e_y}^{\mathrm{axf}}=L_{\vec e_x}^{\mathrm{axf}}L_{\vec e_y}^{\mathrm{axf}}$, and $\vec e_x\vec e_y$ squares to $-1$, so $(iL_{\vec e_x}^{\mathrm{axf}}L_{\vec e_y}^{\mathrm{axf}})^2=i^2L_{(\vec e_x\vec e_y)^2}^{\mathrm{axf}}=(-1)(-1)=+1$ and $P^2=P$. The mixed cell $T_{\vec e_x,\vec e_y}=L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ is **not** this operator and must not be substituted for it: $(iT_{\vec e_x,\vec e_y})^2=i^2L_{\vec e_x^{\,2}}^{\mathrm{axf}}R_{\vec e_y^{\,2}}^{\mathrm{axf}}=(-1)(-1)(-1)=-1$, so $\tfrac12(1+iT_{\vec e_x,\vec e_y})$ is not idempotent: it is not even Hermitian, its four eigenvalues being $\tfrac12(1\pm i)$, each twice, where a projector's would be $1$ and $0$.

**The source's statement.** The $T_a$ annihilate $V_R$ and $e^-_R$ while interchanging $e^-_L$ and $V_L$ as the two isospin states, so that $\mathrm{SU}(2)_L$ acts on the left-handed particles and their right-handed antiparticles; and the mirror construction — the right action on $\omega\,\mathbb{C}\otimes\mathbb{H}$ rather than on $\mathbb{C}\otimes\mathbb{H}$ — reproduces the same picture with the roles exchanged, so that $\mathrm{SU}(2)_R$ acts on the right-handed particles and their left-handed antiparticles.

**What is exact and what is read.** Three ingredients were recomputed. First, the closure above: the three relations hold on the module $\{\Pi_{\mathrm{ch}},\Omega_L^{\dagger}\Pi_{\mathrm{ch}}\}$, where $\{\Omega_L,\Omega_L^{\dagger}\}=1$ and $\tau_3=1-2N$ takes the values $\pm1$; off the module only $\tau_3$ remains an involution, and $\tau_1$ interchanges the two states of the module. Second, $P$ is self-adjoint and idempotent, $P^{\dagger}=P$ and $P^2=P$, of rank $1$ as a $2\times2$ matrix — of rank $2$ as the operator $x\mapsto Px$ on the four-dimensional $\mathbb{B}$, which is the same statement read on four components instead of two. Third, because the ladder and right-action factors commute,
$$
T_a(1-P)=\tau_a P(1-P)=0
$$
**identically**, and
$$
[T_a,T_b]=[\tau_a,\tau_b]\,P=-2i\varepsilon_{abc}\,\tau_cP=-2i\varepsilon_{abc}\,T_c ,
$$
so the generators annihilate one component of the algebra, act only on the component $P$ selects, and carry the same $\mathrm{su}(2)$. That identity is the algebraic content of "the generators annihilate $V_R$ and $e^-_R$ while interchanging $e^-_L$ and $V_L$" — which of the four named states lie in the selected component is the source's identification of states, but the selectivity itself is a property of the idempotent, not an interpretation. All residuals were $0$. The article therefore records the mechanism as **established in its algebraic skeleton and read in its particle assignment**: the commutation, the closure on $\mathrm{su}(2)$ and the annihilation of the complementary component are exact; the naming of $V_L,e^-_L$ as the isospin doublet and of $V_R,e^-_R$ as the annihilated states depends on the supercharge sector, which the algebra does not fix.

**A parity operator from the right action.** The source notes that the right action of $\mathbb{C}\otimes\mathbb{H}$ on $\mathrm{Cl}(3)$ is said to give $\mathrm{Cl}(5)$, whose Coxeter element — the product of its five generators — supplies the parity reversal that $\mathrm{Cl}(3)$ does not contain, so that for $\mathrm{Cl}(3)$ a parity reversal operator does not have to be introduced by hand; and that $\mathrm{Cl}(5)\cong\mathrm{Cl}(6)^+$ links this to Stoica's interpretation of the standard model from a pair of $\mathrm{Cl}(6)$'s, one carrying $\mathrm{SO}(4)$ and the other $\mathrm{SU}(3)\times\mathrm{U}(1)$. Two steps of it are in the corpus, both computed in *The Right Action and the Enveloping Algebra* of the companion mathematics article. The algebra generated by the left action of $\mathrm{Cl}(3)$ and the right action of $\mathbb{C}\otimes\mathbb{H}$ on the eight-dimensional $\mathrm{Cl}(3)$ is
$$
\mathrm{Cl}(3)\otimes_{\mathbb{C}}(\mathbb{C}\otimes\mathbb{H})^{\mathrm{opp}}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})\cong\mathrm{Cl}(5)\cong\mathrm{Cl}(6)^+ ,
$$
of complex dimension $32$ and with a two-dimensional centre. Read on one chirality — the sixteen cells $T_{a,b}$ with both factors in $\mathbb{B}$ — the same construction gives the smaller algebra $\mathrm{Cl}(4)\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, which is the source's "the right action on $\mathbb{C}\otimes\mathbb{H}$ gives $\mathrm{Cl}(4)$". What remains the source's, and is recorded as such, is the identification of the Coxeter element with a parity-reversal operator.

**Two rungs, two volume elements.** The Coxeter element the source writes is an object of the second rung, and the biquaternion dictionary does not name it. The algebra generated acts on the eight-dimensional $\mathrm{Cl}(3)$ and has dimension $32$; the cells $T_{a,b}$ with both factors in $\mathbb{B}$ span only the first rung,
$$
\mathbb{B}^{\mathrm{e}}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})\cong\mathrm{Cl}(4),
$$
of dimension $16$, acting on the four-dimensional $\mathbb{B}$.

The volume element of the first rung is the product of the four frame cells written in *The Legacy Pauli Gamma Formulation*,
$$
i\,(iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}})(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$
where the four factors carry $i^4=1$; the left factors multiply to $e_t\vec e_x\vec e_y\vec e_z=\vec e_z\vec e_z=-e_t$, the right factors, multiplying in reverse order, to $\vec e_y\vec e_y\vec e_y\vec e_x=-\vec e_y\vec e_x=+\vec e_z$, and the outer $i$ is what makes the result $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$. Without the outer $i$ the product is $-R_{\vec e_z}^{\mathrm{axf}}$, whose square is $R_{\vec e_z^{\,2}}^{\mathrm{axf}}=R_{-e_t}^{\mathrm{axf}}=-I_4$; the outer $i$ turns that into $+I_4$, since $i^2=-1$.

The Coxeter element of the $\mathrm{Cl}(5)$ rung is a different object. It is a single two-sided product of five generators of $\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ — three from the left and the two right generators $\vec e_x,\vec e_y$, the third imaginary unit $\vec e_z$ being their product rather than a third generator — so its left factor is an element of $\mathrm{Cl}(3)$ outside $\mathbb{B}$, and it acts on eight dimensions, not four. In one ordering,
$$
L_{E_1}L_{E_2}L_{E_3}R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{\omega}R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{\omega}R_{-\vec e_z}^{\mathrm{axf}},
$$
using $R_bR_c=R_{cb}$, so that $R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=R_{-\vec e_z}^{\mathrm{axf}}$; a different ordering of the five factors changes the sign, which is the $\pm$ recorded in the source. Its square is
$$
\bigl(L_\omega R_{-\vec e_z}^{\mathrm{axf}}\bigr)^2=L_{\omega^2}R_{(-\vec e_z)^2}^{\mathrm{axf}}=L_1R_{-e_t}^{\mathrm{axf}}=-I_8,
$$
with $\omega^2=1$ and $\vec e_z^{\,2}=-e_t$. That is why the Coxeter element is not the first rung's volume cell: it multiplies by the volume element on the left and by a bivector on the right, and it acts on the algebra rather than on $\mathbb{B}$. The corpus therefore states the dictionary at the rung where it is exact and records the $\mathrm{Cl}(5)$ Coxeter element as an object of the larger algebra, which is the algebra this article already declares outside the sixteen cells.

## The Volume Element as the Higgs Candidate

**The interpretation.** The source reads the volume element as the Higgs. The argument rests on the one place in the construction where a left-handed state passes to a right-handed one: multiplication by $\omega$ carries the left-handed electron of the first set to the right-handed electron of the second set, up to a sign. In the source's normalisation, $\omega\,e^-_L=-e^-_R$ and $\omega\,e^-_R=-e^-_L$, and $\omega^2=1$ makes the two steps compose to the identity, so the pair is a two-state system on which $\omega$ acts by the off-diagonal sign. The two symbols name the electron of the first set and the electron of the second, which is not the pair $e^-_L,e^-_R$ of the $\beta$-construction above, where both lie in a single set; the sets are what the equation relates, exactly as in the chirality trap of the section above. In the basis in which the source writes its states the two sets are the diagonal and the anti-diagonal halves, and there $\omega$ does exchange them, as recomputed above: $(x,x)\mapsto(-x,x)$ and $(x,-x)\mapsto(-x,-x)$. In the algebra's own decomposition of $\mathrm{Cl}(3)$ into two simple summands it does not exchange anything: it multiplies the two summands by $\pm1$, and the exchange is the outer automorphism $\sigma$. What the Higgs reading needs is the sign, and the sign is exact: $\omega$ is central, self-adjoint and involutive, it commutes with the whole algebra, and it separates the two chiralities by the eigenvalue $\pm1$. In the standard mechanism the Higgs is what supplies the hypercharge shift turning a right-handed fermion into a left-handed one; the source proposes the pseudoscalar $\omega$ of a Clifford algebra as the algebraic object in that role, for $\mathrm{Cl}(3)$ and, with the quarks added, for $\mathrm{Cl}(7)$, where it notes in passing that for the up quark $\omega$ "gets squared to one" and the assignment is therefore not uniform across a generation.

**Where the interpretation stops.** The corpus records this as an interpretation, and names the boundary. What is exact is $\omega$'s centrality, self-adjointness, square and its action as the relative sign of the two sets, all recomputed; what is not in the algebra is a **coupling**. The construction is a finite algebra with no field content, no hypercharge multiplet structure and no Yukawa operator, so "$\omega$ is the Higgs" names an element whose algebraic role resembles the Higgs's role in the standard mechanism, and is not a derivation of a Higgs field, of a Higgs potential, or of a coupling. It is recorded alongside the framework's own scalar-sector ledger rather than as a result of it.

**Two claims cited to the standard literature.** The source also states, as properties of the left-right symmetric model as such, that the model explains the strong CP problem and that the Higgs coupling vanishes before electroweak symmetry breaking, citing Hall and Harigaya. These are claims about the left-right model and not about the division algebras; the corpus records them as attributed statements of the source's introduction and conclusion, and takes no position on them.

## The Sterile Neutrino, Its Mass and the Seesaw

**Sterility.** The anomaly conditions on a gauge theory with a single $\mathrm{U}(1)$ are $\sum Y=0$, $\sum Y^3=0$ and $\sum YT_3^2=0$ over the fermions, and they constrain only the gauge-charged content. A right-handed neutrino that is a complete gauge singlet carries $Y=0$, $T_3=0$ and colour $0$, so it contributes nothing to any of the three sums; the corpus's anomaly article establishes the same conclusion in the biquaternion framework, that sterile fermions are anomaly-unconstrained. The doubling therefore adds a state that no consistency condition of the gauge sector forbids, and the construction's inclusion of it is not a claim about anomaly cancellation but a claim about the pattern of the fermions.

**Mass and the seesaw.** A sterile fermion is allowed a Majorana mass $M_R$ as a renormalisable term, unlike the gauge-charged fermions; through the type-I seesaw of *The Seesaw Mechanism and Majorana Mass in Biquaternionic Form*, a Dirac mass $m_D$ linking $\nu_L$ to $\nu_R$ and a large Majorana mass $M_R$ give a light neutrino of mass $m_\nu\simeq m_D^2/M_R$, so the construction's $\nu_R$ is exactly the state that the seesaw needs and the smallness of the observed neutrino masses follows from the largeness of $M_R$. The corpus's seesaw article works the mechanism in the framework's own conventions: the Dirac mass is the linear chirality-off-diagonal pair, the Majorana block is the self-conjugate pairing on the module real structure, and the renormalisable-level obstruction is the statement that a mass term for a chiral fermion requires a compensating scalar. The construction supplies the second chirality whose presence the seesaw's Dirac mass requires; the mechanism and the scale are the cited standard treatment and are not recomputed here.

**Dark matter.** A keV-scale sterile neutrino is a standard warm dark matter candidate, produced by oscillation from the active neutrinos in the early universe and detected only gravitationally. The source proposes the construction's right-handed neutrino as this candidate. The corpus records the proposal and its status: the mass scale and the production mechanism are the standard ones of the sterile-neutrino dark-matter literature, the construction's contribution is the presence of the state in the algebra, and the dark-matter identification is an interpretation in the same sense as the rest.

**The proposed probe, and the Majorana requirement.** The source names neutrinoless double beta decay as the experiment proposed to infer a right-handed sterile neutrino, and notes that both the seesaw and its own mass-ratio programme require the neutrino to be a Majorana particle. The corpus records both as the standard statements they are — the seesaw needs a Majorana mass for the singlet, and $0\nu\beta\beta$ is the standard lepton-number-violating probe of it — and records that the construction contributes the presence of the state and not the decay rate, the effective mass or any nuclear matrix element. *The Neutrino and Majorana Fermions in Biquaternionic Form* carries the corpus's treatment of the Majorana condition.

## What the Construction Establishes, Interprets, and Leaves Open

The construction is best summarised by sorting its steps, as the framework's agendas sort theirs.

| Step | Status |
|---|---|
| $\mathrm{Cl}(3)\cong\mathbb{B}\oplus\mathbb{B}$ and $\mathrm{Cl}(7)\cong\mathrm{Cl}(6)\oplus\mathrm{Cl}(6)$; central volume elements $\omega,J$ with $\omega^2=J^2=1$ | Established in the companion mathematics article for $\mathrm{Cl}(3)$; for $\mathrm{Cl}(7)$ by the same computation, redone here |
| Parity automorphism $\sigma:e_i\mapsto-e_i$; the two inequivalent pinor representations distinguished by the eigenvalue of the volume element | Established; $\sigma$ is outer, so it is not the multiplication by $\omega$ |
| The two summands carry the same $\mathrm{su}(3)\oplus\mathrm{u}(1)$ and the same charge spectrum; $[N,J]=0$ and $[\Lambda_a,J]=0$ for the colour generators $\Lambda_a$ | Established, and immediate from the centrality of $J$ |
| Left and right quaternion actions commute; combined they generate $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ with $\mathrm{so}(4)\cong\mathrm{su}(2)\oplus\mathrm{su}(2)$ | Established, recomputed on the four-dimensional model |
| $\omega=E_1E_2E_3$ is central and self-adjoint with $\omega^2=1$ and acts as $\pm1$ on the two summands, preserving each; in the source's basis, where the two sets are the diagonal and anti-diagonal halves, it exchanges them, $\omega\,e^-_L=-e^-_R$ | Established, recomputed in $\mathrm{Cl}(0,3)\cong\mathbb{H}\oplus\mathbb{H}$ |
| The triple $\tau_1,\tau_2,\tau_3$ built from the ladder operator $\Omega_L$ closes on $\mathrm{su}(2)$ on its two-dimensional module, with $\tau_3=1-2N$; $P=\tfrac12(1+i\,\vec e_x\vec e_y)$ is a self-adjoint idempotent; $T_a=\tau_aP$ closes the same way and annihilates $1-P$ identically | Established, recomputed |
| Ladder operators, primitive idempotent, the eight-dimensional minimal left ideal and the charge spectrum $0,\tfrac13,\tfrac13,\tfrac13,\tfrac23,\tfrac23,\tfrac23,1$ in each summand | Established in *The Particle Roster of the Complex Octonionic Chain Algebra* and inherited by each summand of $\mathrm{Cl}(7)$; recomputed |
| The right action of $\mathbb{C}\otimes\mathbb{H}$ on $\mathrm{Cl}(3)$ gives $\mathrm{Cl}(5)\cong\mathrm{Cl}(6)^+$; the generated algebra is $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, of dimension $32$ and centre $2$ | The $\mathrm{Cl}(4)\cong M_4(\mathbb{C})$ half was verified here; the $\mathrm{Cl}(5)\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ half is now recomputed in *Complex Split Biquaternions and the Clifford Algebra Cl(3)*; the Coxeter-element parity operator is the source's |
| The two summands are the two chiralities; the parity automorphism is the discrete left-right symmetry | Interpretation |
| The two weak factors act on opposite chiralities, $\mathrm{SU}(2)_L$ on the left-handed and $\mathrm{SU}(2)_R$ on the right-handed states | The selectivity ($T_a(1-P)=0$) is established; which states are in $P$ is an interpretation |
| The charge-$0$ state of the right-handed summand is the sterile right-handed neutrino | Interpretation; the state's gauge quantum numbers are exact, its identification is an interpretation |
| The volume element $\omega$ is the Higgs, supplying the hypercharge shift between the two chiralities | Interpretation; $\omega$'s role as the relative sign of the two sets is exact, the Higgs identification and any coupling are not in the algebra |
| $\Omega_L,\Omega_L^{\dagger}$ ("mimic $W^-$, $W^+$") and $\Omega_R,\Omega_R^{\dagger}$ as their right-handed analogues | Interpretation of the ladder operators; abandoned for $\mathrm{SU}(2)_R$ in the source's later programme, where $\mathrm{SU}(2)_R$ is used for chiral gravity |
| One generation of quarks and leptons, both chiralities, in the Pati–Salam multiplets of $\mathrm{SU}(4)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | Interpretation; the multiplet assignment is not recomputed |
| $\sqrt{m_e}:\sqrt{m_u}:\sqrt{m_d}=1:2:3$; $\sqrt{m}$ quantised in $(\tfrac13,\tfrac23,1)$ and identified with the second summand's $\mathrm{U}(1)$, read as $\mathrm{U}(1)_{\text{grav}}$ | Source's proposal; checked against PDG central values, $1:2.06:3.02$ |
| Three generations from the eigenvalues of $J_3(\mathbb{O})$ with fermionic entries, and from rotations of one generation's representation | Source's proposal, not recomputed |
| The left-right model explains the strong CP problem and the vanishing of the Higgs coupling before symmetry breaking | Standard-literature claim cited by the source (Hall–Harigaya); not a claim of the algebra |
| Sterile fermions are unconstrained by the anomaly conditions | Standard, and established in the corpus's anomaly article |
| Light neutrino mass from the type-I seesaw $m_\nu\simeq m_D^2/M_R$; $M_R$ a renormalisable Majorana mass for the singlet; $0\nu\beta\beta$ as the proposed probe | Standard, treated in the corpus's seesaw article |
| keV sterile neutrino as warm dark matter | Literature's proposal, recorded |
| Leptoquark combination of the two chiralities before symmetry breaking, on the doubled $\mathrm{Cl}(7)$, with a merged charge-root-mass | Source's programme, put as a question; the construction supplies no leptoquark field |
| Three spin-$1$ Lorentz bosons instead of a spin-$2$ graviton; $10$-dimensional octonionic pre-spacetime from $\mathrm{Sl}(2,\mathbb{O})$ on $J_2(\mathbb{O})$, $(1,9)$ signature, $8$-dimensional octonionic Kaluza–Klein | Source's programme, most speculative, recorded not endorsed |
| The three-colour content, the quantised charge and the observed charge multiplicities | Established in the particle-roster article's sense; the colour and charge successes are properties of a finite algebra |

Three statements deserve emphasis.

- **What the doubling genuinely supplies.** The second chirality, as the second simple summand, with the same internal quantum numbers and the same charge spectrum as the first — a property of a finite algebra, not a transcription. This is exactly the structure that the framework's own ledger records as missing: *Chiral Fermions in the Biquaternion Framework* establishes the projectors and the selection rule $ϙ_L=ϙ_R$ but not a non-central action under which the two chiral halves transform inequivalently, and the doubling supplies such an action by construction, at the price of leaving the biquaternion algebra.
- **What is an interpretation.** The identification of the two summands with the two chiralities; the identification of the two quaternion actions with the two weak factors; the multiplet assignment; and the identification of the neutral state with the right-handed neutrino. Each is a choice consistent with the exact algebra, not a consequence of it; and, as in the particle-roster article, the same charge multiset can be grouped in more than one way, so the charge table fixes multiplicities and not the grouping.
- **What remains open.** The decisive computations are the same three that the particle-roster article names — the centraliser of $\mathrm{su}(3)\oplus\mathrm{u}(1)$ inside the internal algebra, the projection of the abelian generator on the colour Cartan subalgebra, and its commutator with the Lorentz algebra — together with the choice of the supercharge sector that fixes the isospin alignment of the two quaternion actions. The doubling does not perform them; it supplies the second chirality that makes them meaningful.

## The Further Programme of the Source

The construction is presented by its authors as one step of a larger programme, and the corpus records the further steps in the same spirit, as the source's programme rather than as results.

**Mass as a square root and a second $\mathrm{U}(1)$.** The source proposes that the $\mathrm{U}(1)$ number operator of the *right*-chiral fermions — the second summand's charge operator, not the hypercharge — be identified with the **square root of mass**, $\pm\sqrt{m}$, which like electric charge comes with both signs, one sign for matter and the other for antimatter. On that identification the square root of mass is quantised in the ratio $(\tfrac13,\tfrac23,1)$, assigned respectively to the electron, the up quark and the down quark, so that relative to the electric-charge assignment of the first $\mathrm{Cl}(6)$ the positions of the electron and the down quark are interchanged in the second $\mathrm{Cl}(6)$ while the up quark keeps its place. This is what makes the second abelian factor a *mass* factor rather than a second electric charge, and the source calls it $\mathrm{U}(1)_{\text{grav}}$ and associates it with gravitation; in the pre-theory of the next paragraph the two invariants merge into a single "charge-root-mass", quantised in units $0,\tfrac13,\tfrac23,1$ with both signs. The shift from the earlier sections is worth marking: there the two summands carry the **same** $\mathrm{U}(1)$ charge, and the reassignment of the second copy's $\mathrm{U}(1)$ from electric charge to square-root mass is a step of the source's later programme, not a property of the doubling. The corpus records the whole chain as a proposal and notes that its own mass articles read mass differently: *The Petiau System and the Quantisation of Mass in Biquaternionic Form* reads mass from the eigenvalues of $\tilde E\tilde E^{*}$ and from the double-periodic Petiau modulus, and does not use a square root.

**Leptoquarks before the breaking.** The source puts one further speculation, as a question, at the end of its sixth section: whether before electroweak symmetry breaking the left-handed and the right-handed particles existed in a combined state of **leptoquarks**, carrying both the electric charge and the square-root-mass charge. In its account the leptoquarks are **bosons**, described by the doubled algebra $\mathrm{Cl}(7)$ — two copies of $\mathrm{Cl}(6)$ and the split bioctonions — which the source gives as its reason for the study of the split bioctonions. On the merged identification the two quantum numbers become one, the **charge-root-mass**, quantised in units $0,\tfrac13,\tfrac23,1$ with both signs, the negative sign for antiparticles. The corpus records the proposal as the source's programme and as a question rather than a result: the word leptoquark occurs nowhere else in the corpus, the construction exhibits no leptoquark field, no coupling to the states of the two summands and no decay, and the bosonic character that the source assigns to the combined states is a statement of its pre-theory, not a property of the two Clifford algebras.

**The square-root mass ratios and the exceptional Jordan algebra.** The $1:2:3$ statement of the source's fourth and sixth sections is about the **square roots of the masses** of the electron, the up quark and the down quark — one generation, leptons and quarks together, not the charged leptons alone — and is quoted as the motivation for the mass-ratio programme rather than derived in this paper. The separate three-generation statement is that the eigenvalues of the exceptional Jordan matrices $J_3(\mathbb{O})$ **with fermionic entries** give the mass ratios of the three Standard Model generations, summarised in the source's Figure 2 and worked out in its own reference on the fine-structure constant and mass ratios; the source proposes obtaining the three generations themselves as rotations of the fermionic representation of any one generation, a transformation of $J_3(\mathbb{O})$. The classical theory treats $J_3(\mathbb{O})$ as the carrier of the exceptional structures, and the corpus records both statements as the source's proposals: it does not recompute the eigenvalue fit, the fermionic-entry construction or the three-generation rotation. The $1:2:3$ pattern is not a charged-lepton ratio, and it is not the eigenvalue statement for $J_3(\mathbb{O})$; the source makes two different claims, and they are kept apart here.

**$\mathrm{E}_6$, $\mathrm{Spin}(10)$ and the exceptional subgroups.** $\mathrm{F}_4$ is the automorphism group of the Albert algebra $J_3(\mathbb{O})$ and sits inside $\mathrm{E}_6$ as a maximal subgroup, the quotient $\mathrm{E}_6/\mathrm{F}_4$ being a compact symmetric space of dimension $26$; the two are not related by complexification, their complex dimensions being $52$ and $78$. The source uses the two maximal subgroups of $\mathrm{F}_4$ — $H_1=[\mathrm{SU}(3)\times\mathrm{SU}(3)]/\mathbb{Z}_3$, of dimension $16$, and $H_2=\mathrm{Spin}(9)$, of dimension $36$ — which are not isomorphic, their dimensions differing — whose intersection $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$, of dimension $12$, is the Standard Model's gauge group; and their counterparts in $\mathrm{E}_6$: the subgroups $\tilde H_1=[\mathrm{SU}(3)]^3/\mathbb{Z}_3$ and $\tilde H_2=\mathrm{Spin}(10)$, whose intersection
$$
\mathrm{SU}(3)\times\mathrm{SU}(2)_R\times\mathrm{SU}(2)_L\times\mathrm{U}(1)
$$
is the left-right symmetric gauge group. These subgroup statements are standard Lie theory, cited by the source from the literature of Boyle and of Dubois-Violette and Todorov; the corpus records them as standard and not as results of the construction.

**$\mathrm{E}_8\times\mathrm{E}_8$, trace dynamics and pre-spacetime.** The source's further programme proposes an $\mathrm{E}_8\times\mathrm{E}_8$ structure, one factor for each chirality, as the carrier of a pre-gravitational interaction; a passage from that structure to quantum theory and gravity through Adler's trace dynamics, in which quantum physics emerges as the statistical mechanics of a deterministic matrix mechanics; and a pre-spacetime in which the algebra precedes and generates the spacetime manifold. Two consequences are stated sharply enough to record separately. The first is what happens to $\mathrm{SU}(2)_R$: rather than being the gauge factor of a right-handed weak interaction, it is used for a **chiral formulation of gravity**, and in place of a spin-$2$ graviton the programme proposes **three spin-$1$ Lorentz bosons**, on an equal footing with the other gauge bosons — a departure from the left-right model as usually written, which the corpus marks. The second is the arena: before symmetry breaking the spacetime is taken to be ten-dimensional and labelled by the octonions, its symmetry being the action of $\mathrm{Sl}(2,\mathbb{O})$ on the Hermitian $2\times2$ octonionic matrices $J_2(\mathbb{O})$, whose determinant gives a $(1,9)$ signature, so that the Lorentz–weak symmetry is unified with the electro-colour symmetry through an eight-dimensional **octonionic Kaluza–Klein** structure; the $J_3(\mathbb{O})\supset J_2(\mathbb{O})\supset J_2(\mathbb{C})$ stabiliser chain of the preceding paragraph is read as the chain in which the stabiliser of $4$-dimensional spacetime sits inside the stabiliser of the $10$-dimensional one, giving the Standard Model group at the bottom. These are the programme's most speculative steps. The corpus records them as such: they are not derived from the two Clifford algebras of this article, and the corpus's ledger already records that the framework's ceiling is the reason such structures have to be supplied outside the biquaternion algebra. The Coleman–Mandula theorem, which the source invokes, forbids the combination of spacetime and internal symmetries of the ordinary kind; the programme argues that in a pre-spacetime with no background manifold the distinction between internal and spacetime symmetries has not yet arisen, so the theorem does not apply, and the corpus records the argument without endorsing it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

Every section but this one is written in cells; here the same cells are written as gamma matrices, for readers who want the standard notation. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

The cells are those of the setup, $T_{a,b}=L_aR_b$ with $T_{a,b}\psi=a\psi b$ and $T_{a,b}T_{c,d}=T_{ac,db}$; $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products, and $\ell(M)=\operatorname{rank}c(M)$ its cell rank. The frame is
$$
\begin{aligned}
\gamma_0[\mathbb{M}_-]&=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}, & \gamma_1[\mathbb{M}_-]&=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}, & \gamma_2[\mathbb{M}_-]&=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\
\gamma_3[\mathbb{M}_-]&=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}, & \gamma_5[\mathbb{M}_-]&=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\chi .
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0[\mathbb{M}_-]&=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}, & \gamma_1[\mathbb{M}_-]&=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}, & \gamma_2[\mathbb{M}_-]&=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\\
\gamma_3[\mathbb{M}_-]&=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}, & \gamma_5[\mathbb{M}_-]&=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\chi .
\end{aligned}
$$

Every gamma is a single cell. The single cells are the pure tensors; they form the seven-dimensional cone $\ell(M)\le1$, and a general element of the algebra is a sum of at most four of them.

**The relations, and where the signs come from.** With $\varepsilon=(1,-1,-1,-1)$,
$$
\begin{aligned}
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}&=2\varepsilon_\mu\delta_{\mu\nu}I_4, & \gamma_0[\mathbb{M}_-]^2&=I_4, & \gamma_1[\mathbb{M}_-]^2=\gamma_2[\mathbb{M}_-]^2=\gamma_3[\mathbb{M}_-]^2&=-I_4,\\
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}&=0, & \gamma_5[\mathbb{M}_-]^2&=I_4.
\end{aligned},
\qquad \varepsilon=(1,-1,-1,-1),$$
Each entry is the cell rule with $i^2=-1$ and $\vec e_k^{\,2}=-e_t$. The first pair, for instance,
$$
\begin{aligned}
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]&=i^2\,L_{e_t}^{\mathrm{pau}}L_{\vec e_x}^{\mathrm{pau}}\,R_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-L_{\vec e_x}^{\mathrm{pau}}R_{-\vec e_z}^{\mathrm{pau}}=+L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},\\
\gamma_1[\mathbb{M}_-]\gamma_0[\mathbb{M}_-]&=i^2\,L_{\vec e_x}^{\mathrm{pau}}L_{e_t}^{\mathrm{pau}}\,R_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=-L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},
\end{aligned}
$$

In the axis-free display:

$$
\begin{aligned}
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]&=i^2\,L_{e_t}^{\mathrm{axf}}L_{\vec e_x}^{\mathrm{axf}}\,R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=-L_{\vec e_x}^{\mathrm{axf}}R_{-\vec e_z}^{\mathrm{axf}}=+L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},\\
\gamma_1[\mathbb{M}_-]\gamma_0[\mathbb{M}_-]&=i^2\,L_{\vec e_x}^{\mathrm{axf}}L_{e_t}^{\mathrm{axf}}\,R_{\vec e_y}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=-L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
\end{aligned}
$$

since $L_{e_t}^{\mathrm{pau}}=I_4$ and $R_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=R_{-\vec e_z}^{\mathrm{pau}}$ while $R_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=R_{\vec e_z}^{\mathrm{pau}}$, the two right multiplications themselves anticommuting; the signs come from $i^2=-1$ in each product.

**Chirality.** $\gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\chi$ is the chirality cell of the section *The Two Dirac Equations in Cells*, and the product of the four frame cells returns it,
$$
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-i\chi,\qquad\text{so}\qquad i\,\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=\chi=\gamma_5[\mathbb{M}_-] ,
$$
with the four factors carrying $i^4=1$ and the left and right products evaluated as in *Two rungs, two volume elements*. The corpus's abstract central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ is a different object, and the two must not be confused: $\chi_{\mathrm{ad}}$ is the difference $\Pi_1-\Pi_2$ of the two central idempotents, so $\chi_{\mathrm{ad}}=\omega$ and $\chi_{\mathrm{ad}}^2=e_t$, while $\tilde\Xi_{\mathrm{ad}}$ is the central root of $-e_t$ itself, $\tilde\Xi_{\mathrm{ad}}=-i\,\omega$, since $(-i\omega)^2=(-i)^2\omega^2=(-1)(+1)=-e_t$. So $\omega$, $\tilde\Xi_{\mathrm{ad}}$ and $\gamma_5[\mathbb{M}_-]$ are three different objects: a central element, its root, and the cell that carries it on the module. $\gamma_5[\mathbb{M}_-]$ represents $\chi_{\mathrm{ad}}$ on the Dirac module, as $\pm1$ on the two chiral halves, and the sign of the representation — hence which summand is called left — is the only freedom left.

**Traces.** With $\epsilon_{0123}=+1$,
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma}.
$$

**The dictionary.** It is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The left-right symmetric construction of Vaibhav and Singh rests on two exact algebraic facts and a set of interpretations.

The first fact is the doubling. The central volume element of each algebra is an involution, $\omega^2=J^2=1$, so $\mathrm{Cl}(3)\cong\mathrm{Cl}(2)\oplus\mathrm{Cl}(2)$ and $\mathrm{Cl}(7)\cong\mathrm{Cl}(6)\oplus\mathrm{Cl}(6)$: the idempotents $\tfrac12(1\pm\omega)$ and $\tfrac12(1\pm J)$ cut each algebra into two summands on which the volume element acts by $\pm1$, the two inequivalent pinor representations, and the parity automorphism $e_i\mapsto-e_i$ exchanges them. The second fact is the pair of commuting quaternion actions of the biquaternion algebra, whose combination generates $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ and whose imaginary parts span the $\mathrm{su}(2)\oplus\mathrm{su}(2)$ of $\mathrm{so}(4)$.

The interpretations are the identification of the two summands with the two chiralities and of the two quaternion actions with $\mathrm{SU}(2)_L$ and $\mathrm{SU}(2)_R$, the identification of the neutral state of the right-handed summand with the sterile right-handed neutrino, the assignment of the states to the Pati–Salam multiplets, and the interpretation of the volume element $\omega$ as the Higgs.

The equation side is written in the article's cells: the chirality-off-diagonal pair $L_{\tilde\nabla}\tilde\Psi_R=m\tilde\Psi_L$ and $L_{\tilde\nabla^{\natural}}\tilde\Psi_L=m\tilde\Psi_R$, one equation per chirality, together with the single two-sided equation $L_{\tilde\nabla^{\natural}}F=m\chi\bar F$, in which the mass is a right multiplication by the chirality cell $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, whose square is $I_4$.

The construction's contact with the framework's ledger is that the second chirality and the sterile state are supplied by the algebra rather than added by hand, and that a sterile fermion is unconstrained by the anomaly conditions. Its open end is the same as that of the undoubled construction: the three commutator computations that would decide whether the abelian charge is a physical gauge charge, together with the choice of the supercharge sector that fixes the isospin alignment.

Beyond the doubling, the article records the mechanism that makes each factor act on one chirality — the isospin generators built from the ladder operator, whose selectivity was recomputed here — and the source's further programme: the proposal of a combined leptoquark state before symmetry breaking; the later reassignment of $\mathrm{SU}(2)_R$ from a weak factor to a chiral formulation of gravity on a ten-dimensional octonionic pre-spacetime, with the second summand's $\mathrm{U}(1)$ read as a square root of mass; and the exceptional structures — $J_3(\mathbb{O})$, $\mathrm{F}_4\subset\mathrm{E}_6$, $\mathrm{E}_8\times\mathrm{E}_8$ — that the programme needs and the biquaternion algebra cannot supply.

The $\mathrm{Cl}(5)$ rung belongs to the mechanism rather than to the programme. There the left action of $\mathrm{Cl}(3)$ and the right action of $\mathbb{C}\otimes\mathbb{H}$ together generate
$$
\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})\cong\mathrm{Cl}(5),
$$
which is the algebra in which the source's Coxeter-element parity reversal lives.

The construction, like the particle-roster one, is outside the biquaternion algebra, and it is recorded here for the same reason: it is the literature's most economical answer to the chirality and sterile-neutrino questions, and its successes and its interpretations are best kept apart.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E_\mu=j\vec e_\mu$, $e_1,\dots,e_7$ | Clifford generators: quaternion units times the split unit $j$, $j^2=1$; and the seven octonionic units; all squares $-1$, all anticommuting |
| $\mathrm{Cl}(3)\cong\mathbb{B}\oplus\mathbb{B}$ | Complex split biquaternions; two biquaternion summands |
| $\mathrm{Cl}(7)\cong\mathrm{Cl}(6)\oplus\mathrm{Cl}(6)$ | Complex split bioctonions; two octonionic chain-algebra summands |
| $\omega=E_1E_2E_3$, $J=e_1\cdots e_7$ | Central volume elements, $\omega^2=J^2=1$; they act as $\pm1$ on the two summands |
| $\Pi_{1,2}=\tfrac12(1\pm\omega)$ and $\tfrac12(1\pm J)$ | Central idempotents projecting on the two summands |
| $\Pi_{\mathrm{ch}}$, $\Pi_\Omega$ | Primitive idempotent of the chain algebra; projector on the two-dimensional module $\{\Pi_{\mathrm{ch}},\Omega_L^{\dagger}\Pi_{\mathrm{ch}}\}$ |
| $\sigma:e_i\mapsto-e_i$ | Parity automorphism; the discrete left-right symmetry; the outer exchange of the two summands |
| $T_{a,b}=L_aR_b$ | Cell, $T_{a,b}\psi=a\psi b$, with $T_{a,b}T_{c,d}=T_{ac,db}$ |
| $L_x,R_x$ | Left and right quaternion multiplications; commuting $\mathrm{su}(2)$'s |
| $i\,(iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}})(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\chi$ | Four-factor volume cell of the first rung, $\mathrm{Cl}(4)$; it equals the chirality cell, and squares to $I_4$ |
| $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell; the mass term of the two-sided Dirac equation |
| $L_{\tilde\nabla}\tilde\Psi_R=m\tilde\Psi_L$, $L_{\tilde\nabla^{\natural}}\tilde\Psi_L=m\tilde\Psi_R$ | The chirality-off-diagonal pair of Dirac equations |
| $L_{\tilde\nabla^{\natural}}F=m\chi\bar F$ | The same content as one two-sided equation |
| $L_\omega R_{-\vec e_z}^{\mathrm{axf}}$ (one ordering) | Coxeter element of the second rung, $\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong\mathrm{Cl}(5)$; squares to $-I_8$ |
| $M_4(\mathbb{C})\cong\mathrm{Cl}(4)$ | First rung: the sixteen cells $T_{a,b}$ with both factors in $\mathbb{B}$, acting on the four-dimensional $\mathbb{B}$; contains $\mathrm{so}(4)\cong\mathrm{su}(2)\oplus\mathrm{su}(2)$ |
| $\mathrm{Cl}(3)\otimes_{\mathbb{C}}(\mathbb{C}\otimes\mathbb{H})^{\mathrm{opp}}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})\cong\mathrm{Cl}(5)\cong\mathrm{Cl}(6)^+$ | Algebra generated by left $\mathrm{Cl}(3)$ and right $\mathbb{C}\otimes\mathbb{H}$; dimension $32$, centre $2$ |
| $\Omega_L=\alpha_1\alpha_2\alpha_3$, $\Omega_R$ | Composite ladder operators of the two summands; read as $W^\pm$ |
| $\tau_1=\Omega_L+\Omega_L^{\dagger}$, $\tau_2=i(\Omega_L-\Omega_L^{\dagger})$, $\tau_3=1-2N$ | $\mathrm{su}(2)$ triple from the ladder operator; on its two-dimensional module $\tau_3=\Omega_L\Omega_L^{\dagger}-\Omega_L^{\dagger}\Omega_L$ |
| $T_a=\tau_aP$, $P=\tfrac12(1+i\,\vec e_x\vec e_y)$ | Isospin generators of the doubled ideal, $T_a(1-P)=0$; $P$ acts by left multiplication on the right-action factor, $L_P$, and is a self-adjoint idempotent of rank $2$ |
| $\beta_1=\tfrac12(-\vec e_x+i\,\vec e_y\tau_3)$, $\beta_2=\Omega_L^{\dagger}i\,\vec e_y$ | Totally isotropic elements of the right action; $\beta_1^2=\beta_2^2=0$ |
| $V_R,V_L,e^-_R,e^-_L$ | The four states of the right-action ideal |
| $\mathrm{SU}(2)_L,\mathrm{SU}(2)_R$ | Weak factors read from the left and right actions (interpretation) |
| $\mathrm{SU}(4)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | Pati–Salam gauge group of the interpretation |
| $\nu_R$ | Right-handed neutrino; $\mathrm{SU}(2)_L$ singlet, sterile (interpretation) |
| Leptoquark | Source's proposed pre-symmetry-breaking combined state of the two chiralities, on the doubled $\mathrm{Cl}(7)$ |
| $m_\nu\simeq m_D^2/M_R$ | Type-I seesaw mass; $M_R$ the singlet Majorana mass |
| $\sqrt{m}$ | Square root of mass; the second summand's $\mathrm{U}(1)$, quantised $(\tfrac13,\tfrac23,1)$ |
| $J_3(\mathbb{O})$ | Exceptional Jordan algebra; source's carrier of the three-generation mass ratios |
| $\mathrm{E}_6\supset\mathrm{F}_4$ | Exceptional group of the programme; $\mathrm{F}_4$ a maximal subgroup, of complex dimensions $78$ and $52$ |
| $\mathrm{U}(1)_{\text{grav}}$ | Proposed second abelian factor of the programme |
| $J_2(\mathbb{O})$, $\mathrm{Sl}(2,\mathbb{O})$ | Pre-spacetime arena of the programme; determinant of $(1,9)$ signature |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- V. Vaibhav and T. P. Singh, "Left-Right Symmetric Fermions and Sterile Neutrinos from Complex Split Biquaternions and Bioctonions," arXiv:2108.01858, for the construction, the interpretation and the further programme recorded here. The version recorded here is **v2** (19 April 2023), whose sixth section carries the three-generation, mass-ratio and pre-spacetime material; the fifth section carries the explicit construction of the isospin generators.
- G. Trayling and W. E. Baylis, "A geometric basis for the standard-model gauge group," *Journal of Physics A* **34** (2001) 3309, and G. Trayling, "A geometric approach to the Standard Model," arXiv:hep-th/9912231, for the predecessor interpretation of $\mathrm{Cl}(7)$ — four spacetime dimensions for rotations and boosts and four for the electroweak and colour sector — from which the source's construction departs.
- R. A. Wilson, "On the problem of choosing subgroups of Clifford algebras for applications in fundamental physics," *Advances in Applied Clifford Algebras* **31** (2021) 59, arXiv:2011.05171, for the alternative route to the Pati–Salam group as $\mathrm{Spin}(6)\times\mathrm{Spin}(4)$ from the real Clifford algebras $\mathrm{Cl}(0,6)$ and $\mathrm{Cl}(3,3)$, cited by the source as the contrast to its own complex split algebras.
- O. C. Stoica, "The standard model algebra," *Advances in Applied Clifford Algebras* **28** (2018) 52, arXiv:1702.04336, for the pair of $\mathrm{Cl}(6)$ algebras — one carrying $\mathrm{SO}(4)$, the other $\mathrm{SU}(3)\times\mathrm{U}(1)$ — to which the source's $\mathrm{Cl}(5)\cong\mathrm{Cl}(6)^+$ remark refers.
- A. B. Gillard and N. G. Gresnigt, "Three fermion generations with two unbroken gauge symmetries from the complex sedenions," *European Physical Journal C* **79** (2019) 446, arXiv:1904.03186, for a different division-algebra route to the three-generation problem, cited by the source alongside the $J_3(\mathbb{O})$ proposal.
- R. Abłamowicz, "Construction of spinors via Witt decomposition and primitive idempotents: a review," in *Clifford Algebras and their Applications in Mathematical Physics*, eds. R. Abłamowicz and B. Fauser (Birkhäuser, 2000), for the Witt-and-idempotent method by which the minimal left ideals of the two chain algebras — and hence the states the construction reads as particles — are built, the method the corpus states in *Peirce Carriers and Inner Conjugation*.
- G. M. Dixon, *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics* (Kluwer, 1994), for the division-algebra programme of which the construction is one entry.
- L. J. Hall and K. Harigaya, "Implications of Higgs discovery for the strong CP problem and unification," *JHEP* **10** (2018) 130, and "Higgs parity grand unification," *JHEP* **11** (2019) 033, for the claims about the strong CP problem and the vanishing of the Higgs coupling that the source cites as properties of the left-right symmetric model.
- R. N. Mohapatra and J. C. Pati, "Left-right gauge symmetry and an isoconjugate model of CP violation," *Physical Review D* **11** (1975) 566, and J. C. Pati and A. Salam, "Lepton number as the fourth color," *Physical Review D* **10** (1974) 275, for the left-right symmetric and Pati–Salam settings.
- G. Senjanović and R. N. Mohapatra, "Exact left-right symmetry and spontaneous violation of parity," *Physical Review D* **12** (1975) 1502, for the spontaneous breakdown of the left-right symmetry.
- S. Dodelson and L. M. Widrow, "Sterile neutrinos as dark matter," *Physical Review Letters* **72** (1994) 17, for the keV sterile-neutrino dark-matter mechanism.
- L. Boyle, "The standard model, the exceptional Jordan algebra, and triality," arXiv:2006.16265, and M. Dubois-Violette and I. Todorov, "Exceptional quantum geometry and particle physics," *Nuclear Physics B* **938** (2019) 751, for $\mathrm{F}_4$, $\mathrm{E}_6$ and their maximal subgroups, cited by the source.
- S. L. Adler, *Quantum Theory as an Emergent Phenomenon* (Cambridge, 2004), for trace dynamics, the programme's route from a matrix mechanics to quantum theory.
- Companion article [Complex Split Biquaternions and the Clifford Algebra Cl(3)](../articles_maths/complex-split-biquaternions-and-the-clifford-algebra-cl3.html), for the algebraic doubling of the lepton case.
- Companion article [The Particle Roster of the Complex Octonionic Chain Algebra](the-particle-roster-of-the-complex-octonionic-chain-algebra.html), for the undoubled construction, its charges and its three open tests.
- Companion article [The Seesaw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html), for the mass mechanism in the framework's own conventions.
