# __The Pion and the Chiral Lagrangian in Biquaternionic Form__

## Introduction

The **pion** is the lightest hadron and the clearest realisation in nature of a Goldstone boson. In quantum chromodynamics with two light flavours the quark mass terms are nearly absent, and the theory possesses an approximate global chiral symmetry $SU(2)_L\times SU(2)_R$ that is spontaneously broken to the diagonal isospin $SU(2)_V$ by the quark condensate. The unbroken subgroup leaves the vacuum invariant; the broken directions would each carry a massless scalar, and the three of them appear as the pion triplet. The small quark masses break the symmetry explicitly and give the pions their small masses, and the low-energy dynamics of the three pions is captured by the **chiral Lagrangian**, an effective field theory whose field is a group-valued matrix and whose couplings are derivatives. This is the framework's nonlinear sigma model, specialised to the coset of two-flavour chiral symmetry and to the pion quantum numbers.

This article constructs the pion and the chiral Lagrangian in the biquaternion framework $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The framework's available compact group is the unit real quaternions $\mathbb{H}^1_{\mathbb{B}}\cong SU(2)\cong\mathbb{S}^3$, and the pion triplet is naturally carried by the adjoint of its Lie algebra, which lies in the material sector:

$$
\vec\pi = \sum_a\pi_a e_a \in\mathfrak{su}(2)\subset\mathbb{M}_- , \qquad a = 1,2,3 ,
$$

an isovector whose three components are simultaneously the three components of a material-sector vector. The chiral field is the group element

$$
\tilde U = \exp\!\left(\frac{\vec\pi}{f_\pi}\right) \in \mathbb{H}^1_{\mathbb{B}} , \qquad \tilde U\tilde U^{\natural} = e_t ,
$$

and the chiral Lagrangian is the biquaternion norm of its derivative. The construction is therefore the framework's principal chiral model of the companion article, with the decay constant of two-flavour QCD.

The findings are the following.

- **Established, and recomputed below.** The pion triplet is the adjoint of the compact $\mathrm{SU}(2)$ inside the material sector, and the chiral field $\tilde U = \exp(\vec\pi/f_\pi)$ is a unit real quaternion. The trace identities $\mathrm{Tr}(e_ae_b) = -2\delta_{ab}$ and, for the standard generators $T_a = \tfrac{i}{2}e_a$, $\mathrm{Tr}(T_aT_b) = \tfrac12\delta_{ab}$, together with $[T_a,T_b] = i\sum_c\varepsilon_{abc}T_c$, hold and were checked from the complex $2\times2$ representation $\mathsf{M}_2(e_a) = -i\sigma_a$. Expanding the biquaternion chiral Lagrangian,
$$
\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{4}\,\mathrm{Tr}\!\left(\partial/\partial Q_\mu\,\tilde U\,\partial/\partial Q_\mu\,\tilde U^{*}\right),
$$
gives the canonical pion kinetic term $\tfrac12[\sum_a\big((\partial/\partial t'\,\pi_a)^2-(\nabla\pi_a)^2\big)]$ with coefficient exactly one; verified numerically. The mass term $\propto\mathrm{Tr}(M\tilde U + M^\dagger\tilde U^{*})$ gives the standard Gell-Mann–Oakes–Renner relation $m_\pi^2 f_\pi^2 = -(m_u+m_d)\langle\bar qq\rangle$, equivalently $m_\pi^2 = B_0(m_u+m_d)$ with $B_0 = -\langle\bar qq\rangle/f_\pi^2$.
- **Interpretation.** Interpreting the pion's isospin triplet as the adjoint of the framework's material-sector $\mathrm{SU}(2)$, and the chiral field as a unit real quaternion, is the interpretive link between the framework's compact group and the pion's quantum numbers. The interpretation is exact at the level of the unbroken subgroup and is labelled where the chiral group is involved.
- **Gap, left visible.** The framework's centre is vector-like: the algebra supplies the diagonal isospin $SU(2)_V$ and its adjoint action on the pion triplet, but no axial generator of the centre acts on the triplet. The chirality cell $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$ is a two-sided frame operator, not a central generator, so it can represent the axial vertex but does not generate a chiral symmetry. The axial currents, the anomaly and the Wess–Zumino–Witten term therefore belong to the spinor and general-gauge sectors. The chiral Lagrangian is realised as a geometric construction on the framework's group manifold, with the axial-current algebra and the anomaly imported from the standard treatment.

- Companion article *Goldstone's Theorem in Biquaternionic Form*, for the Goldstone boson, the derivative couplings, the decay constant and the effective Lagrangian.
- Companion article *The Nonlinear Sigma Model in Biquaternionic Form*, for the group-valued field, its invariant metric and its flat connection, of which this article is the chiral specialisation.
- Companion article *The Higgs Mechanism in Biquaternionic Form*, for the symmetry-breaking potential and the vacuum expectation value.
- Companion article *The Effective Potential and the Coleman–Weinberg Mechanism in Biquaternionic Form*, for the loop-level treatment of that potential.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the non-abelian compact structure of the framework, the flavour assignment, and the programme to which the pion belongs.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral obstruction and the matter representation.
- Companion article *The Proton in Biquaternionic Form*, for the nucleon couplings that the Goldberger–Treiman relation relates to $f_\pi$.
- Companion article *The Neutron in Biquaternionic Form*, for the same couplings in the neutral channel.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the spinor context of the axial current.

## Chiral Symmetry and Its Breaking

The chiral symmetry of two-flavour QCD is a property of the fermion sector, and this article uses it without rebuilding it; the fermionic derivation belongs to the companion spinor articles. The statement is as follows.

In the limit of vanishing $u$- and $d$-quark masses the QCD Lagrangian is invariant under the independent rotations of the left- and right-handed quark doublets,

$$
q_{L,R}\;\longmapsto\; g_{L,R}\,q_{L,R} , \qquad g_{L,R}\in SU(2)_{L,R} ,
$$

so the global symmetry group is $G = SU(2)_L\times SU(2)_R$, with the two commuting factors acting on the two chiralities. The quark condensate

$$
\langle\bar qq\rangle = \langle\bar uu\rangle + \langle\bar dd\rangle \neq 0
$$

is a Lorentz scalar and an isospin singlet, but it pairs a left-handed quark with a right-handed antiquark; it is therefore invariant under the diagonal subgroup $H = SU(2)_V$ — the simultaneous rotation of both chiralities, i.e. isospin — and not under the axial directions. The symmetry breaks spontaneously,

$$
SU(2)_L\times SU(2)_R \;\longrightarrow\; SU(2)_V ,
\qquad
\dim(G/H) = 6 - 3 = 3 ,
$$

and Goldstone's theorem gives three massless scalars, which are the three pions $\pi^\pm,\pi^0$. The nonzero quark masses break the symmetry explicitly, giving the pions a small mass and making them **pseudo-Goldstone** bosons; the explicit breaking is a perturbation, and the chiral Lagrangian organises its effects.

**The framework's part.** The biquaternion framework does not contain colour and does not contain the quark condensate; those belong to the spinor sector. What the framework contains is the group $SU(2)$, realised as the unit real quaternions, and its adjoint action on the material sector. The unbroken isospin $SU(2)_V$ is exactly such a group, and the pion triplet transforms in its adjoint, so the framework supplies the correct transformation law of the pion under the unbroken symmetry. The axial generators that complete $G$ are not supplied by the centre. A central element commutes with the triplet, so its adjoint action is trivial; the isospin in use is the two-sided action $\tilde\pi\mapsto g_V\tilde\pi g_V^{*}$ of the non-central rotors, and that action has no axial partner in the algebra. The chirality cell is a two-sided operator, not a central generator, and this is the boundary of the framework's reach; it is stated precisely in the section on currents below and in the interpretation section at the end.

## The Pion as an Adjoint of the Material Sector

The pion's three charges under isospin are those of the adjoint representation, and the framework's material sector contains exactly such a triplet.

An element of the compact subalgebra is $\vec\pi = \sum_a\pi_a e_a$, with $\pi_a$ real. The commutator

$$
\left[e_a, e_b\right] = 2\sum_c\varepsilon_{abc}e_c
$$

shows that the span of the three $e_a$ closes on itself, and the adjoint action of the rotor $\tilde u = \exp(\vec\alpha/2)\in\mathbb{H}^1_{\mathbb{B}}$ rotates the triplet,

$$
\vec\pi \;\longmapsto\; \tilde u\,\vec\pi\,\tilde u^{*} ,
$$

which is the isospin rotation of an isovector. The bilinear invariant is the norm,

$$
\mathrm{Sc}\!\left(\vec\pi^2\right) = -\,\sum_a\pi_a\pi_a ,
$$

so the triplet's invariant length is the quaternion norm up to sign — the same biquaternion norm that the free-field articles use. The pions are therefore carried by the material sector $\mathbb{M}_-$, exactly as the framework's four-current and its gauge fields are, and the assignment is

$$
\vec\pi\in\mathfrak{su}(2)\subset\mathbb{M}_- ,
\qquad
\vec\pi^{*} = -\vec\pi ,
\qquad
\vec\pi=-\vec\pi^{\natural} .
$$

The last identity is the statement that the pion triplet has no central component — it is a pure imaginary quaternion (a vector) with real coefficients, $\vec\pi = \sum_a\pi_a e_a$ with $\pi_a$ real — which is what makes it an isovector rather than a mixture with the singlet. A would-be flavour-singlet scalar would instead be central, $\propto e_t$ or $\propto ie_t$; the pion is not, and this is the algebraic content of "the pion is an isovector".

**Trace identities.** The standard normalisation of the chiral generators is fixed by the trace

$$
\mathrm{Tr}\!\left(T_aT_b\right) = \frac12\delta_{ab} ,
\qquad
T_a = \frac{i}{2}e_a ,
$$

and its companions

$$
\mathrm{Tr}\!\left(e_ae_b\right) = -2\delta_{ab} ,
\qquad
\left[T_a,T_b\right] = i\sum_c\varepsilon_{abc}T_c ,
\qquad
\mathrm{Tr}\!\left(T_a\{\!T_b,T_c\!\}\right) = 0 ,
$$

the last because the symmetric $d$-symbol vanishes for $SU(2)$. These were checked from the complex $2\times2$ representation of the framework, $\mathsf{M}_2(e_a) = -i\sigma_a$, $\mathsf{M}_2(i) = iI_2$. Since $\mathsf{M}_2(e_ae_b)=(-i\sigma_a)(-i\sigma_b)=-\sigma_a\sigma_b$, the trace of the product is $-2\delta_{ab}$. Since $\mathsf{M}_2(T_a)=\frac{i}{2}(-i\sigma_a)=\frac12\sigma_a$, the normalisation follows at once, with $\mathrm{tr}$ the $2\times2$ matrix trace,

$$
\mathrm{Tr}\!\left(T_aT_b\right)=\frac14\,\mathrm{tr}\!\left(\sigma_a\sigma_b\right)=\frac12\delta_{ab},
$$

and equivalently, with $i^2=-1$,

$$
\mathrm{Tr}\!\left(T_aT_b\right)=\frac{i^2}{4}\,\mathrm{Tr}\!\left(e_ae_b\right)=\frac{(-1)(-2)}{4}\,\delta_{ab}=\frac12\delta_{ab}.
$$

The commutator reproduces the $\varepsilon$-tensor. The factor $i$ in $T_a$ is the standard one that makes the generators Hermitian while the framework's $e_a$ are anti-Hermitian; it does not change the algebra.

## The Chiral Lagrangian

The chiral Lagrangian is the most general Lagrangian for the field $\tilde U$ that is invariant under the global chiral group, organised by the number of derivatives. At two derivatives there is one term, and it is the biquaternion norm of the derivative.

**The chiral field.** Define

$$
\tilde U(\tilde{Q}) = \exp\!\left(\frac{\vec\pi(\tilde{Q})}{f_\pi}\right)\in\mathbb{H}^1_{\mathbb{B}} ,
$$

which is $*$-unitary because $\vec\pi$ is anti-Hermitian, and which may be written in the closed form

$$
\tilde U = \cos\frac{|\pi|}{f_\pi}\,e_t + \frac{\sin(|\pi|/f_\pi)}{|\pi|}\,\vec\pi ,
\qquad
|\pi| = \sqrt{\sum_a\pi_a\pi_a} .
$$

Under the chiral group the field transforms by the two-sided cell $L_{g_L}R_{g_R^{*}}$,

$$
\tilde U\;\longmapsto\; g_L\tilde U g_R^{*},
\qquad g_{L,R}\in\mathbb{H}^1_{\mathbb{B}},
$$

with $g_L,g_R$ constant unit quaternions. The diagonal $g_L=g_R=g_V$ is the cell $L_{g_V}R_{g_V^{*}}$, the adjoint action of the unbroken isospin; the axial directions $g_L=g_R^{*}$ are the broken ones. The pion field is recovered by $\vec\pi=f_\pi\log\tilde U$ on the principal branch. The right factor is the adjoint; on the unit real quaternions it is the group inverse, so the usual chiral action is written without an operator inverse.

**The two-derivative Lagrangian.** It is

$$
\boxed{\;\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{4}\,\mathrm{Tr}\!\left(\partial/\partial Q_\mu\,\tilde U\,\partial/\partial Q_\mu\,\tilde U^{*}\right)
= -\frac{f_\pi^2}{2}\,\mathrm{Sc}\!\left(\partial/\partial Q_\mu\,\tilde U\,\partial/\partial Q_\mu\,\tilde U^{\natural}\right)\;},
$$

the second form using $\mathrm{Tr} = 2\mathrm{Sc}$, $\tilde U^{*} = \tilde U^{\natural}$ for a unit real quaternion, and the cyclicity of $\mathrm{Sc}$. The overall minus sign is the sign convention that makes the kinetic term positive; the standard literature writes the same term with a plus and a mostly-minus contraction. Expanding,

$$
\partial/\partial Q_\mu\,\tilde U = \frac{1}{f_\pi}\partial/\partial Q_\mu\,\vec\pi + O(\pi^2),
\qquad
\mathrm{Sc}\!\left(\partial/\partial Q_\mu\,\tilde U^{\natural}\,\partial/\partial Q_\mu\,\tilde U\right) = \frac{1}{f_\pi^2}\,\sum_a\partial/\partial Q_\mu\,\pi_a\,\partial/\partial Q_\mu\,\pi_a + O(\pi^4),
$$

using $\mathrm{Sc}(e_a^{\natural}e_b) = \delta_{ab}$, which follows from $e_a^{\natural} = -e_a$ and $\mathrm{Sc}(e_ae_b) = -\delta_{ab}$; the two minus signs cancel. Hence

$$
\mathcal{L}_\pi^{(2)} = -\frac12\sum_\mu\sum_a\partial/\partial Q_\mu\,\pi_a\,\partial/\partial Q_\mu\,\pi_a + O(\pi^4)
= \frac12\left[\sum_a\big((\partial/\partial t'\,\pi_a)^2-(\nabla\pi_a)^2\big)\right] + O(\pi^4) ,
$$

the canonical kinetic term of three real pion fields, with coefficient exactly one and no free parameter. The last step uses $\partial/\partial Q_t = -(i/c)\,\partial/\partial t'$ and sets $c=1$. The higher terms are the interactions: every vertex carries derivatives, their coefficients are fixed by the algebra, and at four derivatives the terms include the Skyrme term of the companion article. This is the chiral Lagrangian at leading order, and it is the framework's principal chiral model with $f = f_\pi$.

```text
THE TWO-PARAMETER ADJOINT SANDWICH
==================================

    Theta[gL, gR](X) = gL X gR*

One parameter W gives Theta[W, W](X) = W X W*, the Hermitian sandwich.
The chiral action needs two independent parameters, gL and gR.

WHY IT IS NEEDED
----------------
* One parameter has three real dimensions; SU(2)L x SU(2)R has six.
  A single sandwich cannot carry two independent rotations, and
  gL = gR leaves only the diagonal SU(2)V.
* The second factor is the axial symmetry. Without it there is no axial
  current, no Goldstone coset and no breaking pattern.
* For star-unitary parameters, and in particular on the unit real
  quaternions, the adjoint is the group inverse. The map gL X gR* is
  therefore the usual left-right action, with both factors written by
  one operation and no operator inverse.

THE PHYSICS, IN THE THREE CASES
-------------------------------
* Custodial symmetry and rho. The vacuum <Q> = (v/sqrt2) e_t is fixed
  by gL = gR, so the diagonal SU(2)V is unbroken and ties the W and Z
  masses: rho = M_W^2/(M_Z^2 cos^2 theta_W) = 1 at tree level with
  hypercharge off. With one factor there is no breaking pattern.
* Nonlinear sigma model. U* dU transforms by gR alone, and dU U* by gL
  alone. The two currents are vector and axial, and the target is
  SU(2)L x SU(2)R / SU(2)V. With one factor only the adjoint O(3)
  model remains.
* Pion and chiral Lagrangian. The mass term couples gL and gR, and in
  the isospin limit it is invariant under the diagonal. The axial
  current gives f_pi, PCAC and the Gell-Mann-Oakes-Renner relation.
  With one factor the axial current is absent and the relation has no
  derivation.
```

## Pion Mass and the Gell-Mann–Oakes–Renner Relation

The pions are massless only in the chiral limit. The quark masses break the symmetry explicitly, and their effect is a mass term in the chiral Lagrangian.

**The mass term.** The symmetry-breaking term is the one that transforms like the quark mass matrix: at lowest order in the derivative expansion and first order in $M = \mathrm{diag}(m_u,m_d)$,

$$
\mathcal{L}_\pi^{\text{mass}} = \frac{f_\pi^2 B_0}{2}\,\mathrm{Tr}\!\left(M\tilde U + M^\dagger\tilde U^{*}\right),
$$

with $B_0$ a constant with the dimensions of mass setting the scale of the condensate. Its normalisation is fixed so that the constant term $f_\pi^2 B_0\,\mathrm{Tr}(M)$ is the vacuum energy shift of the quark masses, and the parameter $B_0$ is ${-}\langle\bar qq\rangle/f_\pi^2$. For real quark masses $M=M^\dagger$ and $\tilde U^\dagger=\tilde U^*$, this is the standard $\mathrm{Tr}(M\tilde U^\dagger+\tilde U M^\dagger)$; for the unit real quaternion $\tilde U^{*}=\tilde U^{\natural}=\tilde U^{-1}$,

$$
\tilde U+\tilde U^{*}=2\cos\frac{|\pi|}{f_\pi}\,e_t ,
$$

so the trace is

$$
\mathrm{Tr}\!\left(M\tilde U+M^\dagger\tilde U^{*}\right)
=2\cos\frac{|\pi|}{f_\pi}\,\mathrm{Tr}(M)
=2\,\mathrm{Tr}(M)-\frac{\mathrm{Tr}(M)}{f_\pi^2}\sum_a\pi_a\pi_a+O(\pi^4) ,
$$

with $\mathrm{Tr}(M)=m_u+m_d$. Read in the algebra through $\mathsf{M}_2(e_a)=-i\sigma_a$ and $\mathsf{M}_2(i)=iI_2$, the Hermitian matrix $\mathrm{diag}(m_u,m_d)$ is
$$
M=\frac{m_u+m_d}{2}\,e_t+i\,\frac{m_u-m_d}{2}\,\vec e_z ,
\qquad
\mathsf{M}_2(i\vec e_z)=\sigma_z ,
\qquad
\mathrm{Tr}(M)=m_u+m_d ,
$$
the factor $i$ on the vector part being what makes it Hermitian, and the trace killing that part. Since $\tilde U+\tilde U^{*}$ is central, the vector part does not enter the mass term at all, at any order in $|\pi|$: the leading-order Lagrangian is blind to $m_u-m_d$, and the isospin splitting is a next-order and electromagnetic effect. The quadratic term is therefore

$$
\mathcal{L}_\pi^{\text{mass}} = -\frac{B_0\left(m_u+m_d\right)}{2}\,\sum_a\pi_a\pi_a + \cdots ,
$$

and the three physical pion masses are therefore exactly degenerate at this order, all three given by the one number

$$
m_{\pi^\pm}^2 = m_{\pi^0}^2 = B_0\left(m_u + m_d\right),
$$

not merely degenerate in the isospin limit: the mass term depends only on $|\pi|$, so it cannot separate the neutral from the charged members even when $m_u\ne m_d$. The observed splitting $m_{\pi^\pm} - m_{\pi^0}\approx 4.6$ MeV is the electromagnetic-plus-next-order effect, which this Lagrangian does not capture.

**The Gell-Mann–Oakes–Renner relation.** Eliminating $B_0$ between the mass formula and its definition gives the GOR relation,

$$
\boxed{\;m_\pi^2 f_\pi^2 = -\left(m_u + m_d\right)\langle\bar qq\rangle ,
\qquad\Longleftrightarrow\qquad
m_\pi^2 = -\frac{m_u+m_d}{f_\pi^2}\,\langle\bar qq\rangle\;}
$$

the standard statement that the pion mass-squared is the product of the explicit breaking $m_u+m_d$ and the condensate scale $B_0$. It is the leading-order consequence of the chiral Lagrangian and is standard (Gell-Mann, Oakes, and Renner 1968); what the framework supplies is the field $\tilde U$ and the trace that normalises the kinetic term, and hence the normalisation in which $f_\pi$ appears. The relation's content is that the pion mass vanishes with the quark masses while the condensate stays nonzero, which is the precise sense in which the pion is a pseudo-Goldstone boson.

**An illustrative numerical check.** Taking the illustrative inputs $m_\pi = 139.6$ MeV, $f_\pi = 92.1$ MeV and $m_u+m_d = 7.0$ MeV, the relation defines $B_0 = m_\pi^2/(m_u+m_d) = 2.784$ GeV and hence $-\langle\bar qq\rangle = B_0 f_\pi^2 = 2.362\times10^7\ \mathrm{MeV}^3$, whose cube root is $286.9$ MeV. The value is of the standard order $250$–$300$ MeV, which is the consistency the relation is meant to express. The quark masses are scheme- and scale-dependent and the numbers are illustrative; the identity, not the numbers, is the content.

## Currents, the Decay Constant and the Soft Limit

The chiral Lagrangian's currents are what couple the pions to the rest of the Standard Model, and they are the place where the framework's reach and its boundary are both visible.

**The vector current.** The unbroken isospin current is the Noether current of the diagonal $SU(2)_V$ acting as $\tilde U\mapsto g_V\tilde U g_V^{*}$. It is built from the Maurer–Cartan form of the companion article, and at lowest order it is

$$
j_{\mu a} = -\frac{f_\pi^2}{2}\,\mathrm{Sc}\!\left(\partial/\partial Q_\mu\,\tilde U^{\natural}\left[e_a,\tilde U\right]\right) + \cdots
= -\sum_{b,c}\varepsilon_{abc}\pi_b\partial/\partial Q_\mu\,\pi_c + \cdots ,
$$

the standard isovector current of the pion triplet. The natural conjugation on the derivative is the one that fixes the sign: with $\partial \tilde U^{\natural}/\partial x_\mu=-\partial \tilde U/\partial x_\mu$ and $\mathrm{Sc}(e_ae_b)=-\delta_{ab}$, the two minus signs cancel and the prefactor $-\frac{f_\pi^2}{2}$ produces the displayed minus. It lies in the material sector, like every current of the framework, and it is the current whose charge rotates the pion triplet in the adjoint.

**The axial current and its divergence.** The axial current is not the Noether current of a symmetry of the algebra. It is the quark axial current of the underlying theory, which fixes its nature and its anomalous divergence; what the framework contributes is the cell that carries the vertex. The frame cells are

$$
C_\mu = iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}} ,
\qquad \nu(t)=x,\quad \nu(k)=y ,
$$

so that the timelike cell collapses to a single right multiplication, $C_t=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}$, while the three spatial ones keep both factors, $C_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$. The bare cell $\beta_\mu=L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ is the same product without the central $i$, so $C_\mu=i\beta_\mu$. The chirality cell is

$$
\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}},
\qquad
\chi^2=e_t ,
$$

where $L_X\psi=X\psi$ and $R_X\psi=\psi X$ for $X\in\mathbb{B}$. Two cells multiply by $L_aR_b\,L_cR_d=L_{ac}R_{db}$, the right factors in reverse order. The axial vertex is the product of the frame cell with the chirality cell, and the two central imaginaries multiply to one, $i\cdot(-i)=-i^2=1$, so the product is a single cell:

$$
j_{5\mu a} = \bar q\,C_\mu\,\chi\,\frac{\tau_a}{2}q
= \bar q\,L_{e_\mu}^{\mathrm{axf}}R_{\vec e_z\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,\frac{\tau_a}{2}q ,
$$

since $C_\mu\chi=i\beta_\mu\,(-iR_{\vec e_z}^{\mathrm{axf}})=\beta_\mu R_{\vec e_z}^{\mathrm{axf}}=L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ and the last two right multipliers compose as $\vec e_z\vec e_{\nu(\mu)}$, with $\vec e_z\vec e_x=\vec e_y$ and $\vec e_z\vec e_y=-\vec e_x$. The axial vertex is therefore the frame cell with $\vec e_z\vec e_{\nu(\mu)}$ as its right multiplier, and no second imaginary unit survives.

**The chiral pair behind the current.** The axial vertex is two-sided because the fermion has two chiral halves. On the spinor module the two chiral halves obey the pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L ,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R ,
$$

one equation per chirality, coupled only by the mass; at $m=0$ they decouple into the two Weyl equations. The two halves are the images of the projectors $P_{L,R}=\frac12(e_t\mp\chi)$. The axial current is the difference between the currents of the two chiral halves, and the mass term is the off-diagonal coupling that makes its divergence nonzero. The single equation $\tilde\nabla\tilde\Psi=0$ is only the right-handed massless member. This is the two-sided structure that the cell notation displays; the column notation of the Gamma Formulation writes the pair as one matrix equation.

In the isospin limit the divergence is the mass bilinear,

$$
\langle\tilde\nabla,\tilde J_{5a}\rangle_{\natural}
= \frac{m_u+m_d}{2}\,\bar q\,i\chi\,\tau_a q
= \frac{m_u+m_d}{2}\,\bar q\,R_{\vec e_z}^{\mathrm{axf}}\tau_a q ,
$$

and at the level of the chiral Lagrangian it is proportional to the pion field itself,

$$
\langle\tilde\nabla,\tilde J_{5a}\rangle_{\natural} = f_\pi m_\pi^2\,\pi_a + \cdots ,
\qquad
\langle 0|j_{5\mu a}(0)|\pi_b(p)\rangle = i f_\pi p_\mu\,\delta_{ab} ,
$$

which is the partially conserved axial current (PCAC) and the defining matrix element of the decay constant. The framework does not produce this current as the Noether current of a symmetry of its centre: the centre is vector-like, and no axial generator exists in $\mathbb{C}_{\mathbb{B}}$. The chirality cell $\chi$ is a two-sided frame operator, not a central generator; it can carry the axial vertex, but it does not generate a chiral symmetry of the algebra. The axial current, its anomaly and the Wess–Zumino–Witten term are therefore imported from the spinor and general-gauge sectors, and the framework's contribution is the geometric field and its normalisation.

**The soft limit.** Because every pion coupling is a derivative, the amplitude for a process with an additional pion of momentum $k$ is proportional to $k$ as $k\to0$, and the amplitude with an extra soft pion vanishes: the Adler zero. The statement follows from the form of $\mathcal{L}_\pi^{(2)}$ alone and is therefore inherited by the framework's chiral Lagrangian unchanged. It is the reason the pion is weakly coupled at low energy even though the underlying theory is strongly coupled.

**The Goldberger–Treiman relation.** The axial current also couples to the nucleon, and the relation

$$
g_A\,m_N = f_\pi\,g_{\pi NN}
$$

connects the nucleon axial charge, its mass and its pion coupling. The relation is a consequence of PCAC and the pion pole, and its ingredients — the nucleon mass, the axial charge and the pion–nucleon coupling — belong to the spin-$\tfrac12$ sector; it is quoted here only to record that the decay constant normalised by the chiral Lagrangian is the $f_\pi$ that appears in it, and it is developed in the companion articles on the proton and the neutron.

## The Biquaternion Reading

**The pion is a material-sector adjoint.** The framework's pion field is $\vec\pi = \sum_a\pi_a e_a$, an element of the compact subalgebra $\mathfrak{su}(2)$ that lies in $\mathbb{M}_-$. The isovector assignment is not imposed: it is the adjoint of the framework's compact group, and the invariant $\mathrm{Sc}(\vec\pi^{\natural}\vec\pi)=-\mathrm{Sc}(\vec\pi^2)=\sum_a\pi_a\pi_a$ is the biquaternion norm. The pion shares the material sector with the conserved four-current and the gauge fields, and it is distinguished from the central scalar of the Higgs and Goldstone articles by being non-central: the pion rotates under isospin, the scalar does not.

**The chiral field is a rotor.** The unit real quaternion $\tilde U = \exp(\vec\pi/f_\pi)$ is the framework's rotation element, and the chiral transformation $\tilde U\mapsto L_{g_L}R_{g_R^{*}}\tilde U=g_L\tilde U g_R^{*}$ is the composition of a left and a right rotation. The unbroken isospin is the diagonal, i.e. the conjugation by a single rotor, the cell $L_{g_V}R_{g_V^{*}}$, and the pion field is the logarithm of the rotor. This is the same geometric identification that the nonlinear-sigma-model article makes, specialised to $SU(2)$ and to the pion triplet, and it is exact as a statement about the framework's group manifold.

**The trace fixes the normalisation.** The kinetic term's coefficient is fixed by $\mathrm{Tr}(T_aT_b) = \tfrac12\delta_{ab}$, and the framework's plain form, read as the trace pairing, supplies it. The framework therefore contributes the normalisation in which $f_\pi$ appears, and hence the normalisation in which the GOR relation and the PCAC matrix element are written. This is the same role the trace plays in every bilinear of the series.

**The chiral group's axial half is not supplied.** The framework's centre is vector-like, and the algebra contains no axial generator of the centre acting on the pion triplet. The isospin $SU(2)_V$ is realised as the diagonal of the two-sided action, the adjoint cell $L_{g_V}R_{g_V^{*}}$; the axial $SU(2)_A$ is not. The chirality cell $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$ is a two-sided frame operator, not a central generator, so it can represent the axial vertex but does not generate a symmetry. The consequence is that the chiral Lagrangian is available to the framework as a geometric object and as a theory of the unbroken isospin current, while the axial current, the anomaly, the Wess–Zumino–Witten term and the flavour-singlet $\eta_{\mathrm s}$ mass are imported. This is the same boundary that the companion articles on chiral fermions and on the Standard Model agenda draw for the spinor sector, seen here from the pion side.

## Open Questions

1. **Does the framework constrain $f_\pi$?** The decay constant is the order parameter in units of the kinetic term, and the chiral Lagrangian normalises it but does not fix it. Whether the framework's trace or biquaternion norm fixes a preferred relation between $f_\pi$ and the condensate scale $B_0$ is not shown.

2. **The isospin-breaking corrections.** The leading-order Lagrangian gives a degenerate triplet; the observed $\pi^\pm$–$\pi^0$ splitting and the $\eta$–$\pi$ mixing require the next order, whose coefficients (the Gasser–Leutwyler constants) are not computed here. Whether the framework constrains them is open.

3. **The axial current's origin.** Whether the framework's spinor sector, once its chirality is fixed, produces the axial current and the anomaly coefficient — and hence the Wess–Zumino–Witten level — is the question that would close the gap. It belongs to the spinor and anomaly articles.

4. **The flavour-singlet and the $\eta_{\mathrm s}$.** The ninth pseudo-Goldstone boson of three-flavour chiral symmetry acquires its mass from the anomaly; whether the framework can host the three-flavour extension, which would require an $SU(3)$ flavour group beyond the unit quaternions, is not settled.

5. **The nucleon sector.** The Goldberger–Treiman relation ties $f_\pi$ to the nucleon's axial charge and pion coupling; whether the framework's spinor articles reproduce that relation with the same normalisation is the cross-check that would test the pion assignment.

6. **Empirical contact.** As everywhere, the open question is whether the framework's chiral Lagrangian differs from the standard one with the same field content; the framework's contribution is geometric and normalisational, and no deviation has been exhibited.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four of them, at least $\operatorname{rank}c(M)$ in number.

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

The four frame cells multiply to $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-i\chi$, so $\gamma_5[\mathbb{M}_-]=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ spends one more $i$ and returns $\chi$: the two imaginary units give $i\cdot(-i)=1$, and the fifth cell is the chirality cell of the body, not a sixth one.

Each of the four is one factor of $i$ times a bare cell of the body, $\gamma_\mu[\mathbb{M}_-]=i\beta_\mu$ with $\beta_\mu=L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$; the fifth is not of that form, being the chirality cell itself, $\gamma_5[\mathbb{M}_-]=\chi=-iR_{\vec e_z}^{\mathrm{pau}}$. Nothing in the body needs the gammas: they are its own cells with the $i$ made explicit. The bare cells anticommute with the body's metric, $\{\beta_a,\beta_b\}=2g_{ab}[\mathbb{M}_-]I_4$: $\beta_t^2=-I_4$ while $\beta_k^2=+I_4$. The one $i$ per cell flips that square, $\gamma_t[\mathbb{M}_-]^2=-\beta_t^2=+I_4$, and leaves the three spatial signs alone, so the gammas anticommute with the negative metric, $\{\gamma_a[\mathbb{M}_-],\gamma_b[\mathbb{M}_-]\}=2g_{ab}I_4$ with $g=-\eta$. The difference between the two signatures is therefore exactly one factor of $i$ per cell, spent as $i^2=-1$, and the signs that remain are the quaternion squares $\vec e_k^2=-e_t$. The central grading $\chi_{\mathrm{ad}}:=i\tilde\Xi_{\mathrm{ad}}$ — with $\tilde\Xi_{\mathrm{ad}}$ a central root of $-e_t$, so $\chi_{\mathrm{ad}}^2=i^2\tilde\Xi_{\mathrm{ad}}^2=(-1)(-e_t)=e_t$ — is a different object, represented by $\gamma_5[\mathbb{M}_-]$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5[\mathbb{M}_-]^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.
## Summary

The pion is the pseudo-Goldstone boson of the two-flavour chiral symmetry $SU(2)_L\times SU(2)_R$ spontaneously broken to isospin $SU(2)_V$, with three components transforming in the adjoint and a decay constant $f_\pi$. In the biquaternion framework the pion triplet is the adjoint of the compact $\mathrm{SU}(2)$ inside the material sector,

$$
\vec\pi = \sum_a\pi_a e_a \in\mathfrak{su}(2)\subset\mathbb{M}_- ,
\qquad
\left[e_a,e_b\right] = 2\sum_c\varepsilon_{abc}e_c ,
\qquad
\mathrm{Sc}\!\left(\vec\pi^2\right) = -\sum_a\pi_a\pi_a ,
$$

the chiral field is the unit real quaternion

$$
\tilde U = \exp\!\left(\frac{\vec\pi}{f_\pi}\right)\in\mathbb{H}^1_{\mathbb{B}},
\qquad
\tilde U\tilde U^{\natural} = e_t ,
$$

and the leading chiral Lagrangian is the biquaternion norm of its derivative,

$$
\boxed{\;\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{4}\,\mathrm{Tr}\!\left(\partial/\partial Q_\mu\,\tilde U\,\partial/\partial Q_\mu\,\tilde U^{*}\right)
= \frac12\left[\sum_a\big((\partial/\partial t'\,\pi_a)^2-(\nabla\pi_a)^2\big)\right] + O(\pi^4)\;},
$$

with the coefficient exactly one, fixed by the trace identity $\mathrm{Tr}(T_aT_b) = \tfrac12\delta_{ab}$ for $T_a = \tfrac{i}{2}e_a$ (equivalently $\mathrm{Tr}(e_ae_b) = -2\delta_{ab}$ and $\mathrm{Sc}(e_a^{\natural}e_b) = \delta_{ab}$). These identities were checked from the representation $\mathsf{M}_2(e_a) = -i\sigma_a$; with $i^2=-1$, the trace gives $\mathrm{Tr}(T_aT_b)=\frac{(-1)(-2)}{4}\delta_{ab}=\frac12\delta_{ab}$, and the kinetic coefficient was verified numerically on the expansion, coming out exactly $1$.

The quark mass matrix adds the symmetry-breaking term $\frac{f_\pi^2B_0}{2}\mathrm{Tr}(M\tilde U + M^\dagger\tilde U^{*})$ with $B_0 = -\langle\bar qq\rangle/f_\pi^2$, whose quadratic part gives the degenerate $m_{\pi^\pm}^2 = m_{\pi^0}^2 = B_0(m_u+m_d)$ and hence the Gell-Mann–Oakes–Renner relation $m_\pi^2 f_\pi^2 = -(m_u+m_d)\langle\bar qq\rangle$. For the illustrative inputs $m_\pi = 139.6$ MeV, $f_\pi = 92.1$ MeV, $m_u+m_d = 7.0$ MeV, the relation gives $B_0 = 2.784$ GeV and $|\langle\bar qq\rangle|^{1/3} = 286.9$ MeV, of the standard order.

The framework supplies the pion's adjoint isovector assignment, the geometric chiral field as a rotor, the decay-constant normalisation through its trace, and the soft limit as a property of the derivative expansion. It does not supply the axial current, the anomaly, the Wess–Zumino–Witten term or the flavour-singlet mass, because its centre is vector-like; those are imported from the spinor and general-gauge sectors, and the flavour-singlet and three-flavour extensions remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $e_ae_b = -\delta_{ab}e_t+\sum_c\varepsilon_{abc}e_c$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde Q^{\natural}$, $\mathrm{Sc}$ | Quaternionic conjugation, $e_a^{\natural}=-e_a$ and $i^{\natural}=i$, so $\mathrm{Sc}(e_a^{\natural}e_b)=\delta_{ab}$; scalar part |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{H}^1_{\mathbb{B}}$ | Real quaternions; unit real quaternions $\cong SU(2)\cong\mathbb{S}^3$ |
| $\mathbb{C}_{\mathbb{B}}$ | Centre; home of the condensate and of every scalar singlet |
| $\vec\pi = \sum_a\pi_a e_a\in\mathfrak{su}(2)\subset\mathbb{M}_-$ | Pion triplet; isovector adjoint |
| $[e_a,e_b] = 2\sum_c\varepsilon_{abc}e_c$ | Compact algebra of the framework |
| $T_a = \tfrac{i}{2}e_a$ | Standard Hermitian chiral generators |
| $\mathrm{Tr}(T_aT_b) = \tfrac12\delta_{ab}$, $\mathrm{Tr}(e_ae_b) = -2\delta_{ab}$, $\mathrm{Sc}(e_a^{\natural}e_b) = \delta_{ab}$ | Trace identities fixing the normalisation |
| $\tilde U = \exp(\vec\pi/f_\pi)\in\mathbb{H}^1_{\mathbb{B}}$ | Chiral field (unit real quaternion) |
| $\tilde u = \exp(\vec\alpha/2)\in\mathbb{H}^1_{\mathbb{B}}$ | Adjoint rotation element (isospin rotor) |
| $\tilde U\mapsto L_{g_L}R_{g_R^{*}}\tilde U=g_L\tilde U g_R^{*}$ | Chiral transformation; diagonal $SU(2)_V$ unbroken |
| $\mathcal{L}_\pi^{(2)} = -\frac{f_\pi^2}{4}\mathrm{Tr}(\partial/\partial Q_\mu\,\tilde U\partial/\partial Q_\mu\,\tilde U^{*})$ | Leading chiral Lagrangian |
| $f_\pi$ | Pion decay constant ($\approx 92.1$ MeV) |
| $\mathcal{L}_\pi^{\text{mass}} = \frac{f_\pi^2B_0}{2}\mathrm{Tr}(M\tilde U+M^\dagger\tilde U^{*})$ | Explicit-breaking mass term |
| $M = \mathrm{diag}(m_u,m_d) = \frac{m_u+m_d}{2}e_t+i\frac{m_u-m_d}{2}\vec e_z$ | Quark mass matrix, and the same element in the algebra, where it is Hermitian and $\mathrm{Tr}(M)=m_u+m_d$ |
| $\bar q,q$ | Quark fields; the condensate and the axial current belong to the spinor sector |
| $\tau_a$ | Pauli matrices in flavour space |
| $B_0 = -\langle\bar qq\rangle/f_\pi^2$ | Condensate scale parameter |
| $m_\pi^2 = B_0(m_u+m_d)$, $m_\pi^2f_\pi^2 = -(m_u+m_d)\langle\bar qq\rangle$ | Pion mass and the Gell-Mann–Oakes–Renner relation |
| $j_{\mu a}$, $j_{5\mu a}$ | Isospin (vector) and axial currents |
| $C_\mu=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, $\beta_\mu=L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$ | Frame cell of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$; its bare form, $C_\mu=i\beta_\mu$, with $\{\beta_a,\beta_b\}=2g_{ab}[\mathbb{M}_-]I_4$; and the chirality cell; $L_X\psi=X\psi$, $R_X\psi=\psi X$ for $X\in\mathbb{B}$; the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ is a different object |
| $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | Chiral pair of the Dirac equation; the two sides are coupled only by the mass |
| $\langle0\vert j_{5\mu a}(0)\vert\pi_b(p)\rangle = if_\pi p_\mu\delta_{ab}$ | Defining matrix element of $f_\pi$ |
| $\langle\tilde\nabla,\tilde J_{5a}\rangle_{\natural} = f_\pi m_\pi^2\pi_a$ | PCAC |
| $g_Am_N = f_\pi g_{\pi NN}$ | Goldberger–Treiman relation (spin-$\tfrac12$ companion) |
| $g_{\mu\nu}[\mathbb{M}_-]$ | $ict'$ metric for index contractions; the $\gamma$ identities of *The Legacy Pauli Gamma Formulation* use the same metric |
| $\mathrm{Tr} = 2\,\mathrm{Sc}$; $\mathrm{tr}$ | Algebra trace, and the matrix trace of the representation in use — $2\times2$ for $\mathbb{B}$, $4\times4$ on the spinor module in *The Legacy Pauli Gamma Formulation* |
| $a,b,c$ | Isospin indices, written low; every contraction over them is an explicit sum |

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
