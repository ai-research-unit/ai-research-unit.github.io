# __The Pion and the Chiral Lagrangian in Biquaternionic Form__

## Introduction

The **pion** is the lightest hadron and the clearest realisation in nature of a Goldstone boson. In quantum chromodynamics with two light flavours the quark mass terms are nearly absent, and the theory possesses an approximate global chiral symmetry $SU(2)_L\times SU(2)_R$ that is spontaneously broken to the diagonal isospin $SU(2)_V$ by the quark condensate. The unbroken subgroup leaves the vacuum invariant; the broken directions would each carry a massless scalar, and the three of them appear as the pion triplet. The small quark masses break the symmetry explicitly and give the pions their small masses, and the low-energy dynamics of the three pions is captured by the **chiral Lagrangian**, an effective field theory whose field takes its values in the chiral group and whose couplings are derivatives. This is the framework's nonlinear sigma model, specialised to the coset of two-flavour chiral symmetry and to the pion quantum numbers.

This article constructs the pion and the chiral Lagrangian in the biquaternion framework $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The framework's available compact group is the group of unit quaternions, the elements $\tilde u$ with $\langle\tilde u\rangle_\natural = e_t$, isomorphic to $SU(2)$ and to $\mathbb{S}^3$, and the pion triplet is naturally carried by the adjoint of its Lie algebra, which lies in the material sector:

$$
\vec\pi = \sum_\eta\pi_\eta\vec e_\eta \in\mathfrak{su}(2)\subset\mathbb{B}_{\Phi} , \qquad \eta = 1, 2, 3 ,
$$

an isovector whose three components are simultaneously the three components of a material-sector vector. The chiral field is the unit element

$$
\tilde U = \exp\!\left(\frac{\vec\pi}{f_\pi}\right) , \qquad \langle\tilde U\rangle_\natural = \tilde U\tilde U^{\natural} = e_t ,
$$

and the chiral Lagrangian is the sum of the Hermitian norms of its four derivatives. The construction is therefore the framework's principal chiral model of the companion article, with the decay constant of two-flavour QCD.

The findings are the following.

- **Established, and recomputed below.** The pion triplet is the adjoint of the compact $\mathrm{SU}(2)$ inside the material sector, and the chiral field $\tilde U = \exp(\vec\pi/f_\pi)$ is a unit real quaternion, $\langle\tilde U\rangle_\natural = e_t$. The normalisation is read from the plain weight of the units, $\mathrm{Sc}(\vec e_j\vec e_\eta) = -\delta_{j\eta}$ and $\mathrm{Sc}(\vec e_j^{\natural}\vec e_\eta) = \delta_{j\eta}$; from them the generators $T_\eta = \tfrac{i}{2}\vec e_\eta$ satisfy $\mathrm{Sc}(T_jT_\eta) = \tfrac14\delta_{j\eta}$, equivalently $\mathrm{Tr}(T_jT_\eta) = \tfrac12\delta_{j\eta}$, and $[T_j,T_\eta] = i\sum_l\epsilon_{j\eta l}T_l$. Expanding the biquaternion chiral Lagrangian,
$$
\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{2}\sum_\mu\mathrm{Sc}\!\left(\frac{\partial\tilde U}{\partial R_\mu}\frac{\partial\tilde U^{\natural}}{\partial R_\mu}\right),
$$
gives the canonical pion kinetic term $\tfrac12\sum_\eta\big((\partial\pi_\eta/\partial r'_t)^2-(\nabla\pi_\eta)^2\big)$ with coefficient exactly one. The mass term $f_\pi^2B_0\,\mathrm{Sc}(M\tilde U + M^{*}\tilde U^{*})$ gives the standard Gell-Mann–Oakes–Renner relation $m_\pi^2 f_\pi^2 = -(m_u+m_d)\langle\bar qq\rangle$, equivalently $m_\pi^2 = B_0(m_u+m_d)$ with $B_0 = -\langle\bar qq\rangle/f_\pi^2$.
- **Interpretation.** Interpreting the pion's isospin triplet as the adjoint of the framework's material-sector $\mathrm{SU}(2)$, and the chiral field as a unit real quaternion, is the interpretive link between the framework's compact group and the pion's quantum numbers. The interpretation is exact at the level of the unbroken subgroup and is labelled where the chiral group is involved.
- **Gap, left visible.** The framework's centre is vector-like: the algebra supplies the diagonal isospin $SU(2)_V$ and its adjoint action on the pion triplet, but no axial generator of the centre acts on the triplet. The fifth basis operator of the frame is the right multiplication by $-i\vec e_z$, an operator of the frame and not an element of the centre, so it can carry the axial vertex but does not generate a chiral symmetry. The axial currents, the anomaly and the Wess–Zumino–Witten term therefore belong to the fermion and general-gauge sectors. The chiral Lagrangian is realised as a geometric construction on the framework's group manifold, with the axial-current algebra and the anomaly imported from the standard treatment.

- Companion article *Goldstone's Theorem in Biquaternionic Form*, for the Goldstone boson, the derivative couplings, the decay constant and the effective Lagrangian.
- Companion article *The Nonlinear Sigma Model in Biquaternionic Form*, for the group-valued field, its invariant metric and its flat connection, of which this article is the chiral specialisation.
- Companion article *The Higgs Mechanism in Biquaternionic Form*, for the symmetry-breaking potential and the vacuum expectation value.
- Companion article *The Effective Potential and the Coleman–Weinberg Mechanism in Biquaternionic Form*, for the loop-level treatment of that potential.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the non-abelian compact structure of the framework, the flavour assignment, and the programme to which the pion belongs.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral obstruction and the matter representation.
- Companion article *The Proton in Biquaternionic Form*, for the nucleon couplings that the Goldberger–Treiman relation relates to $f_\pi$.
- Companion article *The Neutron in Biquaternionic Form*, for the same couplings in the neutral channel.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the fermion context of the axial current.

## Chiral Symmetry and Its Breaking

The chiral symmetry of two-flavour QCD is a property of the fermion sector, and this article uses it without rebuilding it; the fermionic derivation belongs to the companion fermion articles. The statement is as follows.

In the limit of vanishing $u$- and $d$-quark masses the QCD Lagrangian is invariant under the independent rotations of the left- and right-handed quark doublets,

$$
q_{L,R}\;\longmapsto\; g_{L,R}\,q_{L,R} , \qquad g_{L,R}\in SU(2)_{L,R} ,
$$

so the global symmetry group is $G = SU(2)_L\times SU(2)_R$, with the two commuting factors acting on the two parts of the quark field. The quark condensate

$$
\langle\bar qq\rangle = \langle\bar uu\rangle + \langle\bar dd\rangle \neq 0
$$

is a Lorentz scalar and an isospin singlet, but it pairs the two parts of the quark field; it is therefore invariant under the diagonal subgroup $H = SU(2)_V$ — the simultaneous rotation of both parts, i.e. isospin — and not under the axial directions. The symmetry breaks spontaneously,

$$
SU(2)_L\times SU(2)_R \;\longrightarrow\; SU(2)_V ,
\qquad
\dim(G/H) = 6 - 3 = 3 ,
$$

and Goldstone's theorem gives three massless scalars, which are the three pions $\pi^\pm,\pi^0$. The nonzero quark masses break the symmetry explicitly, giving the pions a small mass and making them **pseudo-Goldstone** bosons; the explicit breaking is a perturbation, and the chiral Lagrangian organises its effects.

**The framework's part.** The biquaternion framework does not contain colour and does not contain the quark condensate; those belong to the fermion sector. What the framework contains is the group $SU(2)$, realised as the unit real quaternions, and its adjoint action on the material sector. The unbroken isospin $SU(2)_V$ is exactly such a group, and the pion triplet transforms in its adjoint, so the framework supplies the correct transformation law of the pion under the unbroken symmetry. The axial generators that complete $G$ are not supplied by the centre. A central element commutes with the triplet, so its adjoint action is trivial; the isospin in use is the two-sided action $\vec\pi\mapsto g_V\vec\pi g_V^{*}$ of the non-central rotors, and that action has no axial partner in the algebra. The fifth basis operator of the frame is an operator of the frame and not a central element, and this is the boundary of the framework's reach; it is stated precisely in the section on currents below and in the reading section at the end.

## The Pion as an Adjoint of the Material Sector

The pion's three charges under isospin are those of the adjoint representation, and the framework's material sector contains exactly such a triplet.

An element of the compact subalgebra is $\vec\pi = \sum_\eta\pi_\eta\vec e_\eta$, with $\pi_\eta$ real. The commutator

$$
\left[\vec e_j, \vec e_\eta\right] = 2\sum_l\epsilon_{j\eta l}\vec e_l
$$

shows that the span of the three units closes on itself, and the adjoint action of the rotor $\tilde u = \exp(\vec\alpha/2)$ rotates the triplet,

$$
\vec\pi \;\longmapsto\; \tilde u\,\vec\pi\,\tilde u^{*} ,
$$

which is the isospin rotation of an isovector. The bilinear invariant is the plain form,

$$
\mathrm{Sc}\!\left(\vec\pi^2\right) = -\,\sum_\eta\pi_\eta\pi_\eta ,
\qquad
\mathrm{Sc}\!\left(\vec\pi^{\natural}\vec\pi\right) = \sum_\eta\pi_\eta\pi_\eta ,
$$

so the triplet's invariant length is the quaternion norm, the same norm that the free-field articles use. The pions are therefore carried by the material sector $\mathbb{B}_{\Phi}$, exactly as the framework's four-current and its gauge fields are, and the assignment is

$$
\vec\pi\in\mathfrak{su}(2)\subset\mathbb{B}_{\Phi} ,
\qquad
\vec\pi^{*} = -\vec\pi ,
\qquad
\vec\pi^{\natural} = -\vec\pi .
$$

The last identity is the statement that the pion triplet has no central component: it is a pure element with real coefficients, which is what makes it an isovector rather than a mixture with the singlet. A would-be flavour-singlet scalar would instead be central, $\propto e_t$ or $\propto ie_t$; the pion is not, and this is the algebraic content of "the pion is an isovector".

**The normalisation.** The generators of the triplet are $T_\eta = \tfrac{i}{2}\vec e_\eta$, and their normalisation is the plain weight of the units:

$$
\mathrm{Sc}\!\left(T_jT_\eta\right) = \tfrac14\delta_{j\eta} ,
\qquad
\mathrm{Sc}\!\left(\vec e_j\vec e_\eta\right) = -\delta_{j\eta} ,
\qquad
\mathrm{Sc}\!\left(\vec e_j^{\natural}\vec e_\eta\right) = \delta_{j\eta} ,
\qquad
\mathrm{Sc}\!\left(T_j\{\!T_\eta,T_l\!\}\right) = 0 ,
$$

with the commutator

$$
\left[T_j,T_\eta\right] = i\sum_l\epsilon_{j\eta l}T_l .
$$

The last vanishing is the statement that the symmetric symbol of $SU(2)$ vanishes: the symmetrised product of two vector units is central, and the third unit has no scalar part to meet it. The algebra trace reads the same identities with the factor two of its own normalisation, $\mathrm{Tr}(T_jT_\eta) = \tfrac12\delta_{j\eta}$ and $\mathrm{Tr}(\vec e_j\vec e_\eta) = -2\delta_{j\eta}$. The factor $i$ in $T_\eta$ makes the generators Hermitian, and the units are anti-Hermitian, $\vec e_\eta^{*} = -\vec e_\eta$.

## The Chiral Lagrangian

The chiral Lagrangian is the most general Lagrangian for the field $\tilde U$ that is invariant under the global chiral group, organised by the number of derivatives. At two derivatives there is one term, and it is the Hermitian norm of the derivative.

**The chiral field.** Define

$$
\tilde U = \exp\!\left(\frac{\vec\pi}{f_\pi}\right) , \qquad \langle\tilde U\rangle_\natural = e_t ,
$$

which is $*$-unitary because $\vec\pi$ is anti-Hermitian, and which may be written in the closed form

$$
\tilde U = \cos\frac{|\pi|}{f_\pi}\,e_t + \frac{\sin(|\pi|/f_\pi)}{|\pi|}\,\vec\pi ,
\qquad
|\pi| = \sqrt{\sum_\eta\pi_\eta\pi_\eta} .
$$

Under the chiral group the field transforms by one left and one right factor,

$$
\tilde U\;\longmapsto\; g_L\,\tilde U\,g_R^{*} ,
\qquad \langle g_L\rangle_\natural = \langle g_R\rangle_\natural = e_t ,
$$

with $g_L,g_R$ constant unit quaternions. The diagonal $g_L=g_R=g_V$ is the adjoint action, conjugation by a single rotor, the unbroken isospin; the axial directions $g_L=g_R^{*}$ are the broken ones. The pion field is recovered by $\vec\pi=f_\pi\log\tilde U$ on the principal branch. On the unit real quaternions the star is the group inverse, so the chiral action is written without an operator inverse.

**The two-derivative Lagrangian.** It is

$$
\boxed{\;\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{2}\sum_\mu\mathrm{Sc}\!\left(\frac{\partial\tilde U}{\partial R_\mu}\frac{\partial\tilde U^{\natural}}{\partial R_\mu}\right)
= -\frac{f_\pi^2}{2}\sum_\mu\left\langle\frac{\partial\tilde U}{\partial R_\mu}\right\rangle_{*}\;},
$$

the second form reading the same term as the Hermitian norm of each derivative, the two conjugations agreeing on a real-coefficient element because $\tilde U^{*} = \tilde U^{\natural}$ for a unit real quaternion. The overall minus sign is the sign convention that makes the kinetic term positive; the standard literature writes the same term with a plus and a mostly-minus contraction. Expanding,

$$
\frac{\partial\tilde U}{\partial R_\mu} = \frac{1}{f_\pi}\frac{\partial\vec\pi}{\partial R_\mu} + O(\pi^2),
\qquad
\mathrm{Sc}\!\left(\frac{\partial\tilde U^{\natural}}{\partial R_\mu}\frac{\partial\tilde U}{\partial R_\mu}\right) = \frac{1}{f_\pi^2}\,\sum_\eta\frac{\partial\pi_\eta}{\partial R_\mu}\frac{\partial\pi_\eta}{\partial R_\mu} + O(\pi^4),
$$

using $\mathrm{Sc}(\vec e_j^{\natural}\vec e_\eta) = \delta_{j\eta}$, which follows from $\vec e_\eta^{\natural} = -\vec e_\eta$ and $\mathrm{Sc}(\vec e_j\vec e_\eta) = -\delta_{j\eta}$; the two minus signs cancel. Hence

$$
\mathcal{L}_\pi^{(2)} = -\frac12\sum_\mu\sum_\eta\frac{\partial\pi_\eta}{\partial R_\mu}\frac{\partial\pi_\eta}{\partial R_\mu} + O(\pi^4)
= \frac12\,\sum_\eta\left[\left(\frac{\partial\pi_\eta}{\partial r'_t}\right)^2-\sum_j\left(\frac{\partial\pi_\eta}{\partial R_j}\right)^2\right] + O(\pi^4) ,
$$

the canonical kinetic term of three real pion fields, with coefficient exactly one and no free parameter. The last step uses $\partial/\partial R_t = -i\,\partial/\partial r'_t$, so that the time term contributes $-(\partial\pi_\eta/\partial r'_t)^2$ before the overall minus, and no value of $c$ is needed. The higher terms are the interactions: every vertex carries derivatives, their coefficients are fixed by the algebra, and at four derivatives the terms include the Skyrme term of the companion article. This is the chiral Lagrangian at leading order, and it is the framework's principal chiral model with $f = f_\pi$.

**Why two factors.** The chiral action needs two independent rotations, and one factor cannot carry them. A single rotor has three real parameters, and $SU(2)_L\times SU(2)_R$ has six; with $g_L=g_R$ only the diagonal isospin survives. The second factor is the axial direction: without it there is no axial current, no Goldstone coset and no breaking pattern. On the unit quaternions the star is the inverse, so the pair $g_L\tilde U g_R^{*}$ is the usual left-right action, written by one product and with no operator inverse. Each factor acts alone on one of the two currents of the nonlinear sigma model: $\tilde U^{\natural}\,\partial_\mu\tilde U$ is carried by the right factor and $\partial_\mu\tilde U\,\tilde U^{\natural}$ by the left, and the target is $SU(2)_L\times SU(2)_R/SU(2)_V$. The diagonal leaves the isospin-singlet vacuum fixed and ties the $W$ and $Z$ masses, so that the custodial parameter is one at tree level with hypercharge off.

## Pion Mass and the Gell-Mann–Oakes–Renner Relation

The pions are massless only in the chiral limit. The quark masses break the symmetry explicitly, and their effect is a mass term in the chiral Lagrangian.

**The mass term.** The symmetry-breaking term is the one that transforms like the quark mass element: at lowest order in the derivative expansion and first order in $M$,

$$
\mathcal{L}_\pi^{\text{mass}} = f_\pi^2 B_0\,\mathrm{Sc}\!\left(M\tilde U + M^{*}\tilde U^{*}\right),
$$

with $B_0$ a constant with the dimensions of mass setting the scale of the condensate. Its normalisation is fixed so that the constant term $2f_\pi^2 B_0\,\mathrm{Sc}(M)$ is the vacuum energy shift of the quark masses, and the parameter $B_0$ is ${-}\langle\bar qq\rangle/f_\pi^2$. The quark mass element is Hermitian and lies in the informational sector,

$$
M = \frac{m_u+m_d}{2}\,e_t + i\,\frac{m_u-m_d}{2}\,\vec e_z ,
\qquad
M^{*} = M ,
\qquad
\mathrm{Sc}(M) = \frac{m_u+m_d}{2} ,
$$

with spectrum $m_u,m_d$; the factor $i$ on the vector part is what makes it Hermitian. Since $\tilde U+\tilde U^{*}$ is central,

$$
\tilde U+\tilde U^{*}=2\cos\frac{|\pi|}{f_\pi}\,e_t ,
$$

the vector part of $M$ does not enter the mass term at all, at any order in $|\pi|$: the leading-order Lagrangian is blind to $m_u-m_d$, and the isospin splitting is a next-order and electromagnetic effect. The mass term is therefore

$$
\mathcal{L}_\pi^{\text{mass}} = 2f_\pi^2 B_0\,\mathrm{Sc}(M)\cos\frac{|\pi|}{f_\pi}
= f_\pi^2 B_0\left(m_u+m_d\right) - \frac{B_0\left(m_u+m_d\right)}{2}\,\sum_\eta\pi_\eta\pi_\eta + \cdots ,
$$

and the three physical pion masses are exactly degenerate at this order, all three given by the one number

$$
m_{\pi^\pm}^2 = m_{\pi^0}^2 = B_0\left(m_u + m_d\right).
$$

The degeneracy is exact in the mass term, not merely as an isospin limit: the term depends only on $|\pi|$, so it cannot separate the neutral from the charged members even when $m_u\ne m_d$. The observed splitting $m_{\pi^\pm}-m_{\pi^0}\approx 4.6$ MeV is the electromagnetic-plus-next-order effect, which this Lagrangian does not capture.

**The Gell-Mann–Oakes–Renner relation.** Eliminating $B_0$ between the mass formula and its definition gives the GOR relation,

$$
\boxed{\;m_\pi^2 f_\pi^2 = -\left(m_u + m_d\right)\langle\bar qq\rangle ,
\qquad\Longleftrightarrow\qquad
m_\pi^2 = -\frac{m_u+m_d}{f_\pi^2}\,\langle\bar qq\rangle\;}
$$

the standard statement that the pion mass-squared is the product of the explicit breaking $m_u+m_d$ and the condensate scale $B_0$. It is the leading-order consequence of the chiral Lagrangian and is standard (Gell-Mann, Oakes, and Renner 1968); what the framework supplies is the field $\tilde U$ and the plain form that normalises the kinetic term, and hence the normalisation in which $f_\pi$ appears. The relation's content is that the pion mass vanishes with the quark masses while the condensate stays nonzero, which is the precise sense in which the pion is a pseudo-Goldstone boson.

**An illustrative numerical check.** Taking the inputs $m_\pi = 139.6$ MeV, $f_\pi = 92.1$ MeV and $m_u+m_d = 7.0$ MeV, the relation defines $B_0 = m_\pi^2/(m_u+m_d) = 2.784$ GeV and hence $-\langle\bar qq\rangle = B_0 f_\pi^2 = 2.362\times10^7\ \mathrm{MeV}^3$, whose cube root is $286.9$ MeV. The value is of the standard order $250$–$300$ MeV, which is the consistency the relation is meant to express. The quark masses are scheme- and scale-dependent and the numbers are illustrative; the identity, not the numbers, is the content.

## Currents, the Decay Constant and the Soft Limit

The chiral Lagrangian's currents are what couple the pions to the rest of the Standard Model, and they are the place where the framework's reach and its boundary are both visible.

**The vector current.** The unbroken isospin current is the Noether current of the diagonal $SU(2)_V$ acting as $\tilde U\mapsto g_V\tilde U g_V^{*}$. It is built from the Maurer–Cartan form of the companion article, and at lowest order it is

$$
j_{\mu \eta} = -\frac{f_\pi^2}{2}\,\mathrm{Sc}\!\left(\frac{\partial\tilde U^{\natural}}{\partial R_\mu}\left[\vec e_\eta,\tilde U\right]\right) + \cdots
= -\sum_{j,l}\epsilon_{\eta jl}\,\pi_j\,\frac{\partial\pi_l}{\partial R_\mu} + \cdots ,
$$

the standard isovector current of the pion triplet. The quaternion conjugation on the derivative is the one that fixes the sign: with $\partial\tilde U^{\natural}/\partial R_\mu=-\partial\tilde U/\partial R_\mu$ and $\mathrm{Sc}(\vec e_j\vec e_\eta)=-\delta_{j\eta}$, the two minus signs cancel and the prefactor $-\frac{f_\pi^2}{2}$ produces the displayed minus. It lies in the material sector, like every current of the framework, and it is the current whose charge rotates the pion triplet in the adjoint.

**The axial current and its divergence.** The axial current is not the Noether current of a symmetry of the algebra. It is the quark axial current of the underlying theory, which fixes its nature and its anomalous divergence; what the framework contributes is the product of elements that carries the vertex. The frame basis operator of the coordinate $x_\mu$ multiplies on the left by $e_\mu$ and on the right by $\vec e_{\nu(\mu)}$, with the phase $i$,

$$
C_\mu:\ \tilde Q\;\longmapsto\; i\,e_\mu\,\tilde Q\,\vec e_{\nu(\mu)} ,
\qquad \nu(t)=x,\quad \nu(k)=y ,
$$

so that the time slot collapses, $e_t\tilde Q=\tilde Q$, and the timelike basis operator is the single right multiplication $\tilde Q\mapsto i\tilde Q\vec e_x$, while the three spatial basis operators keep both factors. The fifth basis operator of the frame is the right multiplication by $-i\vec e_z$,

$$
\xi:\ \tilde Q\;\longmapsto\; -i\,\tilde Q\,\vec e_z ,
\qquad \xi\xi = e_t ,
$$

where $\xi\xi$ is the basis operator applied twice. The axial vertex is the product of the frame basis operator with the fifth basis operator, the fifth basis operator applied first, and the two central imaginaries multiply to one, $i\cdot(-i)=-i^2=1$, so the product is a single product of elements:

$$
C_\mu\xi:\ \tilde Q\;\longmapsto\; e_\mu\,\tilde Q\,\vec e_z\vec e_{\nu(\mu)} ,
\qquad \vec e_z\vec e_x=\vec e_y ,\quad \vec e_z\vec e_y=-\vec e_x .
$$

The axial vertex is therefore the frame basis operator with $\vec e_z\vec e_{\nu(\mu)}$ as its right multiplier, and no second imaginary unit survives. The vertex of the axial current in the direction $k$ is that product read on the quark field, with the isospin generator:

$$
j_{5\mu \eta} = \bar q\,C_\mu\xi\,T_\eta\,q .
$$

**The chiral pair behind the current.** The axial vertex is two-sided because the fermion has two parts. The two parts carry the two values of the label, $L$ for the minus one and $R$ for the plus one, and they obey the pair

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L} ,
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R} ,
$$

one equation per value, coupled only by the mass; at $m=0$ they decouple into the two Weyl equations. The axial current is the difference between the currents of the two parts, and the mass term is the coupling that makes its divergence nonzero. The single equation $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$ is only the $R$ part at $m=0$. This is the two-sided structure that the product of two elements displays. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

In the isospin limit the divergence is the mass bilinear,

$$
\langle\tilde\nabla,\tilde J_{\Phi,5k}\rangle_{\natural}
= \frac{m_u+m_d}{2}\,\bar q\,(i\xi)\,T_\eta\,q ,
$$

the basis operator $i\xi$ being the right multiplication by $\vec e_z$, the phase $i$ cancelling the $-i$ of the fifth basis operator, and at the level of the chiral Lagrangian it is proportional to the pion field itself,

$$
\langle\tilde\nabla,\tilde J_{\Phi,5k}\rangle_{\natural} = f_\pi m_\pi^2\,\pi_\eta + \cdots ,
\qquad
\langle 0|j_{5\mu \eta}(0)|\pi_l(p)\rangle = i f_\pi p_\mu\,\delta_{\eta l} ,
$$

which is the partially conserved axial current (PCAC) and the defining matrix element of the decay constant. The framework does not produce this current as the Noether current of a symmetry of its centre: the centre is vector-like, and no axial generator exists in $\mathbb{B}_{C}$. The fifth basis operator belongs to the frame and not to the centre; it can carry the axial vertex, but it does not generate a chiral symmetry of the algebra. The axial current, its anomaly and the Wess–Zumino–Witten term are therefore imported from the fermion and general-gauge sectors, and the framework's contribution is the geometric field and its normalisation.

**The soft limit.** Because every pion coupling is a derivative, the amplitude for a process with an additional pion of momentum $k$ is proportional to $k$ as $k\to0$, and the amplitude with an extra soft pion vanishes: the Adler zero. The statement follows from the form of $\mathcal{L}_\pi^{(2)}$ alone and is therefore inherited by the framework's chiral Lagrangian unchanged. It is the reason the pion is weakly coupled at low energy even though the underlying theory is strongly coupled.

**The Goldberger–Treiman relation.** The axial current also couples to the nucleon, and the relation

$$
g_A\,m_N = f_\pi\,g_{\pi NN}
$$

connects the nucleon axial charge, its mass and its pion coupling. The relation is a consequence of PCAC and the pion pole, and its ingredients — the nucleon mass, the axial charge and the pion–nucleon coupling — belong to the spin-$\tfrac12$ sector; it is quoted here only to record that the decay constant normalised by the chiral Lagrangian is the $f_\pi$ that appears in it, and it is developed in the companion articles on the proton and the neutron.

## The Biquaternion Reading

**The pion is a material-sector adjoint.** The framework's pion field is $\vec\pi = \sum_\eta\pi_\eta\vec e_\eta$, an element of the compact subalgebra $\mathfrak{su}(2)$ that lies in $\mathbb{B}_{\Phi}$. The isovector assignment is not imposed: it is the adjoint of the framework's compact group, and the invariant $\mathrm{Sc}(\vec\pi^{\natural}\vec\pi)=-\mathrm{Sc}(\vec\pi^2)=\sum_\eta\pi_\eta\pi_\eta$ is the quaternion norm. The pion shares the material sector with the conserved four-current and the gauge fields, and it is distinguished from the central scalar of the Higgs and Goldstone articles by being non-central: the pion rotates under isospin, the scalar does not.

**The chiral field is a rotor.** The unit real quaternion $\tilde U = \exp(\vec\pi/f_\pi)$ is the framework's rotation element, and the chiral transformation $\tilde U\mapsto g_L\tilde U g_R^{*}$ is one left multiplication and one right multiplication. The unbroken isospin is the diagonal, conjugation by a single rotor, and the pion field is the logarithm of the rotor. This is the same geometric identification that the nonlinear-sigma-model article makes, specialised to $SU(2)$ and to the pion triplet, and it is exact as a statement about the framework's group manifold.

**The plain form fixes the normalisation.** The kinetic term's coefficient is fixed by $\mathrm{Sc}(T_jT_\eta)=\tfrac14\delta_{j\eta}$, and the framework's plain form, read on the units, supplies it. The framework therefore contributes the normalisation in which $f_\pi$ appears, and hence the normalisation in which the GOR relation and the PCAC matrix element are written. This is the same role the plain form plays in every bilinear of the series.

**The chiral group's axial half is not supplied.** The framework's centre is vector-like, and the algebra contains no axial generator of the centre acting on the pion triplet. The isospin $SU(2)_V$ is realised as the diagonal of the two-sided action, conjugation by a single rotor; the axial $SU(2)_A$ is not. The fifth basis operator of the frame is the right multiplication by $-i\vec e_z$, an operator of the frame and not an element of the centre, so it can represent the axial vertex but does not generate a symmetry. The consequence is that the chiral Lagrangian is available to the framework as a geometric object and as a theory of the unbroken isospin current, while the axial current, the anomaly, the Wess–Zumino–Witten term and the flavour-singlet $\eta_{\mathrm s}$ mass are imported. This is the same boundary that the companion articles on chiral fermions and on the Standard Model agenda draw for the fermion sector, seen here from the pion side.

## Open Questions

1. **Does the framework constrain $f_\pi$?** The decay constant is the order parameter in units of the kinetic term, and the chiral Lagrangian normalises it but does not fix it. Whether the framework's plain form or biquaternion norm fixes a preferred relation between $f_\pi$ and the condensate scale $B_0$ is not shown.

2. **The isospin-breaking corrections.** The leading-order Lagrangian gives a degenerate triplet; the observed $\pi^\pm$–$\pi^0$ splitting and the $\eta$–$\pi$ mixing require the next order, whose coefficients (the Gasser–Leutwyler constants) are not computed here. Whether the framework constrains them is open.

3. **The axial current's origin.** Whether the framework's fermion sector, once its two parts are assigned, produces the axial current and the anomaly coefficient — and hence the Wess–Zumino–Witten level — is the question that would close the gap. It belongs to the fermion and anomaly articles.

4. **The flavour-singlet and the $\eta_{\mathrm s}$.** The ninth pseudo-Goldstone boson of three-flavour chiral symmetry acquires its mass from the anomaly; whether the framework can host the three-flavour extension, which would require an $SU(3)$ flavour group beyond the unit quaternions, is not settled.

5. **The nucleon sector.** The Goldberger–Treiman relation ties $f_\pi$ to the nucleon's axial charge and pion coupling; whether the framework's fermion articles reproduce that relation with the same normalisation is the cross-check that would test the pion assignment.

6. **Empirical contact.** As everywhere, the open question is whether the framework's chiral Lagrangian differs from the standard one with the same field content; the framework's contribution is geometric and normalisational, and no deviation has been exhibited.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four of them, at least $\operatorname{rank}c(M)$ in number.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

The four frame basis operators multiply to $\gamma_0\gamma_1\gamma_2\gamma_3=-i\xi$, so $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ spends one more $i$ and returns $\xi$: the two imaginary units give $i\cdot(-i)=1$, and the fifth basis operator is one of the body's own, not a sixth one.

Each of the four is one factor of $i$ times a bare basis operator of the body, $\gamma_\mu=i\beta_\mu$ with $\beta_\mu=L_{\mathrm{pau},e_\mu}R_{\mathrm{pau},\vec e_{\nu(\mu)}}$; the fifth is not of that form, being the fifth basis operator itself, $\gamma_5=\xi=-iR_{\mathrm{pau},\vec e_z}$. Nothing in the body needs the gammas: they are its own basis operators with the $i$ made explicit. The bare basis operators anticommute with the body's weight, $\{\beta_a,\beta_b\}=2(-\varepsilon_a\delta_{ab})I_4$: $\beta_t^2=-I_4$ while $\beta_k^2=+I_4$. The one $i$ per basis operator flips that square, $\gamma_t^2=-\beta_t^2=+I_4$, and leaves the three spatial signs alone, so the gammas anticommute with the negative metric, $\{\gamma_a,\gamma_b\}=2g_{ab}I_4$ with $g=-\eta$. The difference between the two signatures is therefore exactly one factor of $i$ per basis operator, spent as $i^2=-1$, and the signs that remain are the quaternion squares $\vec e_\eta^2=-e_t$. The central grading $\xi_{\mathrm{ad}}:=i\tilde{Ζ}_{\mathrm{ad}}$ — with $\tilde{Ζ}_{\mathrm{ad}}$ a central root of $-e_t$, so $\xi_{\mathrm{ad}}^2=i^2\tilde{Ζ}_{\mathrm{ad}}^2=(-1)(-e_t)=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the basis operators,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_\eta)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.
## Summary

The pion is the pseudo-Goldstone boson of the two-flavour chiral symmetry $SU(2)_L\times SU(2)_R$ spontaneously broken to isospin $SU(2)_V$, with three components transforming in the adjoint and a decay constant $f_\pi$. In the biquaternion framework the pion triplet is the adjoint of the compact $\mathrm{SU}(2)$ inside the material sector,

$$
\vec\pi = \sum_\eta\pi_\eta\vec e_\eta \in\mathfrak{su}(2)\subset\mathbb{B}_{\Phi} ,
\qquad
\left[\vec e_j,\vec e_\eta\right] = 2\sum_l\epsilon_{j\eta l}\vec e_l ,
\qquad
\mathrm{Sc}\!\left(\vec\pi^2\right) = -\sum_\eta\pi_\eta\pi_\eta ,
$$

the chiral field is the unit real quaternion

$$
\tilde U = \exp\!\left(\frac{\vec\pi}{f_\pi}\right),
\qquad
\langle\tilde U\rangle_\natural = \tilde U\tilde U^{\natural} = e_t ,
$$

and the leading chiral Lagrangian is the Hermitian norm of its derivative,

$$
\boxed{\;\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{2}\sum_\mu\mathrm{Sc}\!\left(\frac{\partial\tilde U}{\partial R_\mu}\frac{\partial\tilde U^{\natural}}{\partial R_\mu}\right)
= \frac12\left[\sum_\eta\left(\frac{\partial\pi_\eta}{\partial r'_t}\right)^2-\sum_\eta\sum_j\left(\frac{\partial\pi_\eta}{\partial R_j}\right)^2\right] + O(\pi^4)\;},
$$

with the coefficient exactly one, fixed by $\mathrm{Sc}(T_jT_\eta) = \tfrac14\delta_{j\eta}$ for $T_\eta = \tfrac{i}{2}\vec e_\eta$, equivalently $\mathrm{Tr}(T_jT_\eta) = \tfrac12\delta_{j\eta}$ with $\mathrm{Tr}(\vec e_j\vec e_\eta) = -2\delta_{j\eta}$ and $\mathrm{Sc}(\vec e_j^{\natural}\vec e_\eta) = \delta_{j\eta}$. These identities were checked on generic elements of the algebra, and the kinetic coefficient was verified numerically on the expansion, coming out exactly $1$.

The quark mass element adds the symmetry-breaking term $f_\pi^2B_0\,\mathrm{Sc}(M\tilde U + M^{*}\tilde U^{*})$ with $B_0 = -\langle\bar qq\rangle/f_\pi^2$, whose quadratic part gives the degenerate $m_{\pi^\pm}^2 = m_{\pi^0}^2 = B_0(m_u+m_d)$ and hence the Gell-Mann–Oakes–Renner relation $m_\pi^2 f_\pi^2 = -(m_u+m_d)\langle\bar qq\rangle$. For the inputs $m_\pi = 139.6$ MeV, $f_\pi = 92.1$ MeV, $m_u+m_d = 7.0$ MeV, the relation gives $B_0 = 2.784$ GeV and $|\langle\bar qq\rangle|^{1/3} = 286.9$ MeV, of the standard order.

The framework supplies the pion's adjoint isovector assignment, the geometric chiral field as a rotor, the decay-constant normalisation through its plain form, and the soft limit as a property of the derivative expansion. It does not supply the axial current, the anomaly, the Wess–Zumino–Witten term or the flavour-singlet mass, because its centre is vector-like; those are imported from the fermion and general-gauge sectors, and the flavour-singlet and three-flavour extensions remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Coefficient basis, $\vec e_\eta^2 = -e_t$, $\vec e_j\vec e_\eta = -\delta_{j\eta}e_t+\sum_l\epsilon_{j\eta l}\vec e_l$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathrm{Sc}$, ${}^{\natural}$, ${}^{*}$ | Scalar part, intrinsic conjugation, Hermitian conjugation; $\vec e_\eta^{\natural} = \vec e_\eta^{*} = -\vec e_\eta$, $\mathrm{Sc}(\vec e_j\vec e_\eta) = -\delta_{j\eta}$, $\mathrm{Sc}(\vec e_j^{\natural}\vec e_\eta) = \delta_{j\eta}$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}$ | Real quaternions; the unit elements are those with $\langle\tilde u\rangle_\natural = e_t$, $\cong SU(2)\cong\mathbb{S}^3$ |
| $\mathbb{B}_{C}$ | Centre; home of the condensate and of every scalar singlet |
| $\vec\pi = \sum_\eta\pi_\eta\vec e_\eta\in\mathfrak{su}(2)\subset\mathbb{B}_{\Phi}$ | Pion triplet; isovector adjoint |
| $[\vec e_j,\vec e_\eta] = 2\sum_l\epsilon_{j\eta l}\vec e_l$ | Compact algebra of the framework |
| $T_\eta = \tfrac{i}{2}\vec e_\eta$ | Hermitian generators of the triplet |
| $\mathrm{Sc}(T_jT_\eta) = \tfrac14\delta_{j\eta}$, $\mathrm{Tr}(T_jT_\eta) = \tfrac12\delta_{j\eta}$, $\mathrm{Sc}(\vec e_j^{\natural}\vec e_\eta) = \delta_{j\eta}$ | The identities fixing the normalisation |
| $\tilde U = \exp(\vec\pi/f_\pi)$, $\langle\tilde U\rangle_\natural = e_t$ | Chiral field (unit real quaternion) |
| $\tilde u = \exp(\vec\alpha/2)$ | Adjoint rotation element (isospin rotor) |
| $\tilde U\mapsto g_L\tilde U g_R^{*}$ | Chiral transformation; diagonal $SU(2)_V$ unbroken |
| $\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{2}\sum_\mu\mathrm{Sc}\!\left(\frac{\partial\tilde U}{\partial R_\mu}\frac{\partial\tilde U^{\natural}}{\partial R_\mu}\right)$ | Leading chiral Lagrangian |
| $f_\pi$ | Pion decay constant ($\approx 92.1$ MeV) |
| $\mathcal{L}_\pi^{\text{mass}} = f_\pi^2B_0\,\mathrm{Sc}(M\tilde U+M^{*}\tilde U^{*})$ | Explicit-breaking mass term |
| $M = \frac{m_u+m_d}{2}e_t+i\frac{m_u-m_d}{2}\vec e_z$ | Quark mass element, Hermitian, spectrum $m_u,m_d$, $\mathrm{Sc}(M)=\frac{m_u+m_d}{2}$ |
| $\bar q,q$ | Quark fields; the condensate and the axial current belong to the fermion sector |
| $B_0 = -\langle\bar qq\rangle/f_\pi^2$ | Condensate scale parameter |
| $m_\pi^2 = B_0(m_u+m_d)$, $m_\pi^2f_\pi^2 = -(m_u+m_d)\langle\bar qq\rangle$ | Pion mass and the Gell-Mann–Oakes–Renner relation |
| $j_{\mu \eta}$, $j_{5\mu \eta}$ | Isospin (vector) and axial currents |
| $C_\mu$, $\xi$ | Frame basis operator of the coordinate $x_\mu$, $\tilde Q\mapsto ie_\mu\tilde Q\vec e_{\nu(\mu)}$ with $\nu(t)=x$ and $\nu(k)=y$; and the fifth basis operator, the right multiplication by $-i\vec e_z$, written $-iR_{\vec e_z}$ where the operator is the subject |
| $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ | Chiral pair of the Dirac equation; the two parts are coupled only by the mass |
| $\langle0\vert j_{5\mu \eta}(0)\vert\pi_l(p)\rangle = if_\pi p_\mu\delta_{\eta l}$ | Defining matrix element of $f_\pi$ |
| $\langle\tilde\nabla,\tilde J_{\Phi,5k}\rangle_{\natural} = f_\pi m_\pi^2\pi_\eta$ | PCAC |
| $g_Am_N = f_\pi g_{\pi NN}$ | Goldberger–Treiman relation (spin-$\tfrac12$ companion) |
| $\delta_{\mu\nu}=(1,1,1,1)$ | The metric, used for index contractions; the $\gamma$ identities of *The Legacy Pauli Gamma Formulation* use the weight with the opposite sign, $-\varepsilon_\mu\delta_{\mu\nu}$ |
| $\mathrm{Tr}$ | The trace of the algebra, used in $\mathrm{Tr}(T_jT_\eta)=\tfrac12\delta_{j\eta}$ (§*Norm and Pairing Conventions*) |
| $j,k,l$ | Triplet indices, written low; every contraction over them is an explicit sum |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- M. Gell-Mann and M. Lévy, "The axial vector current in beta decay," *Il Nuovo Cimento* **16** (1960) 705–726, for the linear sigma model and the origin of PCAC.
- M. Gell-Mann, R. J. Oakes, and B. Renner, "Behavior of current divergences under $SU(3)\times SU(3)$," *Physical Review* **175** (1968) 2195–2199, for the relation between the pion mass, the decay constant and the quark condensate.
- S. L. Adler, "Consistency conditions on the strong interactions implied by a partially conserved axial-vector current," *Physical Review* **137** (1965) B1022–B1033, and W. I. Weisberger, "Unsubtracted dispersion relations and the renormalization of the weak axial-vector coupling constant," *Physical Review Letters* **14** (1965) 1047–1050, for the sum rules and the soft-pion theorems.
- S. Weinberg, "Dynamical approach to current algebra," *Physical Review Letters* **18** (1967) 188–191, "Nonlinear realizations of chiral symmetry," *Physical Review* **166** (1968) 1568–1577, and "Phenomenological Lagrangians," *Physica A* **96** (1979) 327–340, for the nonlinear realisation and the effective-Lagrangian power counting.
- J. Gasser and H. Leutwyler, "Chiral perturbation theory to one loop," *Annals of Physics* **158** (1984) 142–210, and "Chiral perturbation theory: expansions in the mass of the strange quark," *Nuclear Physics B* **250** (1985) 465–516, for the next-to-leading-order chiral Lagrangian and its low-energy constants.
- J. F. Donoghue, E. Golowich, and B. R. Holstein, *Dynamics of the Standard Model* (Cambridge, 1992), for the chiral Lagrangian, PCAC, and the Goldberger–Treiman relation.
- S. Scherer and M. R. Schindler, *A Primer for Chiral Perturbation Theory* (Springer, 2012), for the systematic construction of the chiral Lagrangian and its currents.
- S. L. Adler, "Axial-vector vertex in spinor electrodynamics," *Physical Review* **177** (1969) 2426–2438, and J. S. Bell and R. Jackiw, "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the sigma model," *Il Nuovo Cimento A* **60** (1969) 47–61, for the axial anomaly.
- J. Wess and B. Zumino, "Consequences of anomalous Ward identities," *Physics Letters B* **37** (1971) 95–97, and E. Witten, "Global aspects of current algebra," *Nuclear Physics B* **223** (1983) 422–432, for the Wess–Zumino–Witten term and the anomaly's topological content.
- G. 't Hooft, "Symmetry breaking through Bell–Jackiw anomalies," *Physical Review Letters* **37** (1976) 8–11, and "Computation of the quantum effects due to a four-dimensional pseudoparticle," *Physical Review D* **14** (1976) 3432–3450, for the anomaly's role in the flavour-singlet mass.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2: *Modern Applications* (Cambridge, 1996), for the chiral Lagrangian and the current algebra.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the PCAC relation and the Goldberger–Treiman relation.
