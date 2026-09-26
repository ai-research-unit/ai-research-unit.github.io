# __The Gluon: An Octet Outside the Biquaternion Algebra__

## Introduction

The gluon is the gauge boson of the strong interaction: massless, electrically neutral, coloured, and eightfold degenerate, transforming in the adjoint representation of $SU(3)$. It is the object that closes this subcategory, because it is the gauge boson the framework cannot host. The companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* establishes the general theorem; this article works out the gluon case, states the three distinct ways in which the octet fails to fit, and records the one structure that would carry it and the price of reaching it.

The result is a boundary, and it is sharp. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is eight-dimensional over the reals, so the number eight is not by itself the obstruction; the obstruction is that the **compact** Lie structure inside the algebra is four-dimensional. The maximal compact subalgebra of $\mathbb{B}$ under the commutator is
$$
\mathfrak{u}(2)=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2),
\qquad
\dim_\mathbb{R}\mathfrak{u}(2)=4 ,
$$
whereas the compact algebra of the colour group is
$$
\mathfrak{su}(3),
\qquad
\dim_\mathbb{R}\mathfrak{su}(3)=8 ,
$$
and there is no eight-dimensional compact subalgebra to be found. The algebra therefore reaches $SU(2)\times U(1)$ and not $SU(3)$; the Standard Model's gauge group has the factors $SU(3)\times SU(2)\times U(1)$, and the framework reaches the last two and not the first. The gluon's **free kinematics**, by contrast, is reached completely: a single gluon, with its colour index fixed, is a massless spin-one field, and the framework's material vector carries it exactly as it carries the photon. What is outside the algebra is the **colour multiplet** — the triplet of colours and the octet of gluons — not the free propagation of one of them.

The article is organised as follows. A first section transcribes the gluon's standard field theory: the eight fields, the field strength, the self-couplings, the invariant tensors, asymptotic freedom and confinement. A second section states what the framework reaches, namely the free kinematics of a single constituent. A third section establishes the obstructions, one at a time: the dimension of the compact algebra, the dimension of the modules, the symmetric invariant tensor, and the failure of the octonion route through non-associativity. A fourth section records the enlarged carrier in which the octet can be embedded and identifies the price — the colour index becomes external data. A fifth section places the result as the ceiling of the category and points to the informational reading of confinement.

We use the conventions of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, and central $i$; the matrix realization is $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$. The sectors are $\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ (material, anti-Hermitian) and $\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ (informational, Hermitian), and the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$. The compact factor is $\mathfrak{u}(2)=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$ with $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, $[e_a,e_b]=2\varepsilon_{abc}e_c$, $T_a=\tfrac12 e_a$; the covariant derivative is $D_\mu=\partial_\mu+i\kappa\mathcal{A}_\mu$ with $\kappa=q/\hbar$; and the non-abelian curvature is $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, from the companion articles. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ with $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$, and the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$. Natural units $\hbar=c=1$ are used for the strong-interaction formulae, where $g_s$ denotes the standard QCD coupling and the standard symbols $f^{abc},d^{abc}$ the $\mathfrak{su}(3)$ invariant tensors; the framework's coupling is $\kappa$ where it appears in the algebra's expressions. Matrix traces on the gauge factors are written $\mathrm{Tr}$, distinct from the informational trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, for the general theorem of which this article is the gluon case.
- Companion article *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*, for the placement of the strong sector in the framework and the list of open problems.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the connection, the curvature and the structure constants of the compact factor.
- Companion article *The Yang–Mills Equation in Biquaternionic Form*, for the field equation and covariant conservation.
- Companion article *The Photon in Biquaternionic Form*, for the free kinematics of a massless spin-one field.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the abelian system the free gluon satisfies component by component.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field-strength biquaternion and the Lorentz invariants.
- Companion article *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the helicity decomposition of the material vector.
- Companion article *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*, for the spin-one representation and the charge eigenvalues.
- Companion article *Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin 0 and One-Half*, for the matter side of the spin ceiling.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the factor-by-factor comparison with the Standard Model gauge group.

## The Gluon in Standard Quantum Chromodynamics

### The Field and Its Action

Quantum chromodynamics is the gauge theory of the group $SU(3)$ with coupling $g_s$, whose gauge fields are eight massless vectors $G^a_\mu$, $a=1,\dots,8$, one for each generator $\lambda^a/2$ of $\mathfrak{su}(3)$. The action is
$$
S_{\mathrm{QCD}}=-\frac{1}{4}\int d^4x\,G^a_{\mu\nu}G^{a\mu\nu},
\qquad
G^a_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu ,
$$
with $f^{abc}$ the structure constants of $\mathfrak{su}(3)$, defined by
$$
[\lambda^a,\lambda^b]=2i f^{abc}\lambda^c ,
\qquad
\{\lambda^a,\lambda^b\}=\frac{4}{3}\delta^{ab}I+2 d^{abc}\lambda^c ,
$$
where $\lambda^a$ are the Gell-Mann matrices, normalized by $\mathrm{Tr}(\lambda^a\lambda^b)=2\delta^{ab}$. The first tensor is totally antisymmetric and the second totally symmetric; both are invariants of the group. The values of the nonzero independent components are
$$
f^{123}=1,
\qquad
f^{147}=f^{246}=f^{257}=f^{345}=\tfrac12,
\qquad
f^{156}=f^{367}=-\tfrac12,
\qquad
f^{458}=f^{678}=\tfrac{\sqrt3}{2},
$$
$$
d^{118}=d^{228}=d^{338}=\tfrac{1}{\sqrt3},
\qquad
d^{146}=d^{157}=d^{256}=d^{344}=d^{355}=\tfrac12,
\qquad
d^{247}=d^{366}=d^{377}=-\tfrac12,
$$
$$
d^{448}=d^{558}=d^{668}=d^{778}=-\tfrac{1}{2\sqrt3},
\qquad
d^{888}=-\tfrac{1}{\sqrt3},
$$
and these values were recomputed directly from the Gell-Mann matrices as a check: all the listed $f$ components were reproduced with the signs above, all the listed $d$ components with the values above, the imaginary parts of the extracted tensors were zero to machine precision, and the adjoint Casimir extracted from the structure constants was
$$
\sum_{c,e}f^{ace}f^{bce}=C_2(G)\,\delta^{ab},
\qquad
C_2(G)=3 ,
\qquad
C_2(\text{fundamental})=\frac{N^2-1}{2N}=\frac43,
\qquad
T(\text{fundamental})=\frac12 .
$$
The gluon is in the adjoint representation, whose dimension is the dimension of the group,
$$
\dim\mathfrak{su}(3)=N^2-1=8 ,
$$
which is the origin of the eight gluons. The action is invariant under the gauge transformation $G^a_\mu\mapsto G^a_\mu-\partial_\mu\Gamma^a-g_s f^{abc}G^b_\mu\Gamma^c$, and its expansion in powers of the fields contains the three-gluon and four-gluon self-couplings,
$$
\mathcal{L}_{3}\sim g_s f^{abc}\left(\partial_\mu G^a_\nu\right)G^{b\mu}G^{c\nu},
\qquad
\mathcal{L}_{4}\sim g_s^2 f^{abe}f^{cde}G^a_\mu G^b_\nu G^{c\mu}G^{d\nu},
$$
so that the gluon is charged under its own gauge group and interacts with itself.

### Asymptotic Freedom and Confinement

The one-loop beta function of the strong coupling is
$$
\beta_{g_s}=-\frac{g_s^3}{16\pi^2}b_0 ,
\qquad
b_0=\frac{11}{3}C_2(G)-\frac{2}{3}\sum_{\text{Weyl}}T(r)
=11-\frac{2}{3}N_f ,
$$
where the last form is for $N_f$ Dirac quark flavours; the coefficient is positive, $b_0=11$ in the pure theory and $b_0=7$ for six flavours, so the coupling decreases at short distances — **asymptotic freedom** — and grows at long distances. In the long-distance regime the theory confines: coloured states are absent from the spectrum and the potential between static colour sources grows linearly, which on the lattice is the area law of the Wilson loop with a string tension. The two facts, asymptotic freedom and confinement, are the physics of the gluon, and both are properties of the $SU(3)$ gauge structure.

### The Octet as the Adjoint of $SU(3)$

Three facts about the octet are the ones to hold against the algebra. Its dimension is eight, $\dim\mathfrak{su}(3)=8$. Its group is $SU(3)$, whose defining representation is the three-dimensional colour triplet of the quarks. Its invariant tensors include both the antisymmetric $f^{abc}$ and the symmetric $d^{abc}$, and the latter is a genuinely $SU(3)$ object: for $SU(2)$ the corresponding symmetric invariant vanishes identically. The octet therefore presupposes a three-dimensional module (the triplet) and an eight-dimensional compact algebra.

## What the Framework Reaches: The Free Constituent

The framework reaches the gluon as a free field. Fix a colour index $a$; the component $G^a_\mu$ is a massless, neutral, spin-one field whose free equation is the Maxwell equation of the companion articles, whose field-strength biquaternion
$$
\tilde{F}=\bar{\tilde{\nabla}}\tilde{G}-\mathrm{Sc}\left(\bar{\tilde{\nabla}}\tilde{G}\right)
\in\mathbb{M}_- ,
\qquad
\mathrm{Sc}(\tilde{F})=0 ,
$$
is a pure-vector material biquaternion, and whose propagating solutions are the self-dual and anti-self-dual combinations carrying the two helicities $\pm1$. The companion articles *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector* and *The Photon in Biquaternionic Form* develop exactly this structure for the massless vector, and it applies to a colour-fixed gluon without change, because a colour-fixed gluon satisfies the abelian Maxwell system component by component. The field-strength invariants $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$ of the companion article govern its Lorentz structure, and the helicity basis is the same.

Two qualifications keep the statement exact.

- **This is the free kinematics, not the colour multiplet.** What is carried is one massless vector field with a fixed external label; the label is not assigned by the algebra, and the eightfold multiplicity and the colour symmetry are not produced.
- **The spin-one carrier is a connection, not a matter module.** The higher-spin companion establishes that the algebra's matter modules do not exceed spin one-half; the spin-one objects of this subcategory are gauge connections, and the gluon, like the photon, is a connection. So the fact that the framework carries spin one does not help with the colour multiplet: the multiplet is a property of the gauge group, not of the free field.

## The Obstructions to the Octet

### The Dimension of the Compact Algebra

The decisive obstruction is the dimension of the compact part. The algebra is eight-dimensional over the reals, but its elements do not all generate compact one-parameter subgroups. The anti-Hermitian part of $\mathbb{B}$ is the material sector $\mathbb{M}_-$ of real dimension four,
$$
\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\},
\qquad
\dim_\mathbb{R}\mathbb{M}_-=4 ,
$$
and the maximal compact subalgebra of $\mathbb{B}$ under the commutator is
$$
\mathfrak{u}(2)=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2),
\qquad
\dim_\mathbb{R}\mathfrak{u}(2)=4 ,
$$
the compact form of the complexified algebra $\mathfrak{gl}(2,\mathbb{C})$, whose Cartan decomposition is $\mathfrak{gl}(2,\mathbb{C})=\mathfrak{u}(2)\oplus i\,\mathfrak{u}(2)$ with both factors of real dimension four. The colour algebra is compact of dimension eight,
$$
\dim_\mathbb{R}\mathfrak{su}(3)=8 ,
$$
and a compact Lie algebra of dimension eight cannot embed in a compact Lie algebra of dimension four. The same count is visible in the group: the compact group the algebra's gauge structure generates is $U(2)$, of real dimension four, and $SU(3)$ has real dimension eight. The number eight that suggests an embedding is the real dimension of $\mathbb{B}$, not the dimension of its compact part; the compact part is half the algebra, and the half is $\mathfrak{u}(2)$.

It is worth stating why the estimate "eight equals eight, so try to embed" fails even before the modules are examined. A gauge algebra is realized as a subalgebra of $\mathbb{B}$ under the commutator, so an eight-dimensional one would be all of $\mathbb{B}$; but $\mathbb{B}\cong\mathfrak{gl}(2,\mathbb{C})$ is not a compact algebra, its maximal compact subalgebra being the four-dimensional $\mathfrak{u}(2)$, and a gauge algebra must be compact, because a non-compact gauge direction generates negative-norm states. Every compact subalgebra lies in a maximal compact one, so the compact subalgebras of $\mathbb{B}$ have real dimension at most four, while $\dim_\mathbb{R}\mathfrak{su}(3)=8$. The coincidence of the two numbers eight is the real dimension of $\mathbb{B}$, which is not the size of its compact part. The algebra's gauge group is therefore $U(2)$, the electroweak factor and not the colour factor.

### The Dimension of the Modules

The second obstruction is on the matter side, and it is stated precisely because it is sometimes overextended. A module over $\mathbb{B}\cong M_2(\mathbb{C})$ is a complex vector space on which the algebra acts linearly, and the algebra's simple module is $\mathbb{C}^2$; every module is a direct sum of copies of it, so every $\mathbb{B}$-module has **even complex dimension**. The colour triplet of the quarks is three-dimensional over $\mathbb{C}$, so it cannot be an intrinsic $\mathbb{B}$-module: the quarks cannot be coloured by the algebra. This is the module-side statement of the ceiling.

The octet itself, however, has complex dimension eight, which is even, so the module obstruction does **not** exclude the adjoint representation by itself. This distinction matters: the gluon's failure is not that its representation has odd dimension but that the group whose adjoint it is cannot be realized. The module obstruction and the group obstruction are different, and only the first is a counting argument on the representation.

### The Symmetric Invariant

The third obstruction is the invariant tensor. The framework's products supply the antisymmetric structure constants and only those. The commutator of two generators is antisymmetric by construction, and its coefficients are the $f^{abc}$, read off in the compact factor as $f^{abc}=2\varepsilon^{abc}$ in the unnormalized basis $e_a$ in which the connection components are taken, equivalently $f^{abc}=\varepsilon^{abc}$ in the normalized basis $T_a=\tfrac12e_a$, and $[T^a,T^b]=2i\varepsilon^{abc}T^c$ for the Hermitian generators $T^a=ie_a\in\mathbb{M}_+$; there is no symmetric object in a commutator. The anticommutator can in principle carry a symmetric part, but for the algebra's compact factor it does not: with $T_a=\tfrac12 e_a$ one has
$$
\{T_a,T_b\}=\tfrac14\big(e_ae_b+e_be_a\big)=-\tfrac12\delta_{ab}\,e_0=\mathrm{Tr}(T_aT_b)\,e_0 ,
$$
which was verified in the defining representation. The anticommutator is therefore central, proportional to the trace rather than to a generator, and the traceless symmetric invariant of the compact factor — the analogue of the colour tensor — vanishes,
$$
d^{abc}=0 .
$$
$SU(3)$, by contrast, has a nonzero totally symmetric invariant, the tensor $d^{abc}$ whose independent components were listed above, and it is part of the group's invariant data. A framework whose invariant tensors are exhausted by the antisymmetric $\varepsilon$ supplies the three-gluon and four-gluon vertices in form — they are built from $f$ alone — but not the full invariant tensor algebra of the colour group. The symmetric tensor would have to be imported along with the group.

### The Octonion Route and the Price of Non-Associativity

There is one mathematical structure that is eight-dimensional, carries $SU(3)$, and lies next to the quaternions: the octonions. The octonion algebra $\mathbb{O}$ has real dimension eight, its automorphism group is the exceptional group $G_2$ of dimension fourteen,
$$
\mathrm{Aut}(\mathbb{O})=G_2,
\qquad
\dim G_2=14,
\qquad
G_2\supset SU(3),
\qquad
\dim SU(3)=8 ,
$$
and the imaginary octonions decompose under that $SU(3)$ as $\mathbb{R}\oplus\mathbb{C}^3$ over the reals, which is seven real dimensions, the complexification being the $\mathrm{SU}(3)$ decomposition $\mathbf{1}\oplus\mathbf{3}\oplus\bar{\mathbf{3}}$ — so that an $SU(3)$ structure carrying a triplet is present. Concretely, $SU(3)$ is the subgroup of $G_2$ that fixes one imaginary unit, and the remaining six span the $\mathbb{C}^3$; the multiplication of the seven units is encoded in the Fano plane. This is the standard relationship of the normed division algebras, and it is the reason the octet is tantalizingly close: the next division algebra after $\mathbb{H}$ does contain the colour group $SU(3)$.

The price is associativity. The octonions are **non-associative**,
$$
(xy)z\neq x(yz)
\qquad\text{in general},
$$
and the commutator is no longer a Lie bracket: the Jacobi identity fails,
$$
[[x,y],z]+[[y,z],x]+[[z,x],y]\neq0 \qquad\text{in general}.
$$
The two failures are one failure: on the octonions the Jacobiator is six times the associator,
$$
[[x,y],z]+[[y,z],x]+[[z,x],y]=6\big((xy)z-x(yz)\big),
$$
an identity verified in the standard realization of $\mathbb{O}$, so a nonvanishing associator and a failed Jacobi identity are the same defect of the product. The framework's entire gauge construction rests on that identity. The curvature is defined by the commutator of covariant derivatives, $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$; the Bianchi identity is the Jacobi identity of the covariant derivatives; the closure of the gauge algebra and the consistency of the Faddeev–Popov and BRST constructions use it; and the companion article *Gauge Curvature and the Bianchi Identity in Biquaternionic Form* takes it as the structural axiom. Without associativity there is no Lie bracket, no curvature from a commutator, no Bianchi identity and no gauge theory of the usual kind. Reaching the octet through the octonions would mean giving up associativity, and with it the algebra as the corpus uses it. This is the precise sense in which the octet is **outside the biquaternion algebra**: not merely not contained in it, but contained only in an algebra that does not have the property on which the framework's gauge structure depends.

## The Enlarged Carrier and the Price of Embedding

The octet can always be embedded if the carrier is enlarged. The algebra of $2\times2$ matrices over $\mathbb{B}$ is
$$
M_2(\mathbb{B})\cong M_2(M_2(\mathbb{C}))\cong M_4(\mathbb{C}),
$$
and the unitary group of $\mathbb{C}^4$ contains $U(3)$ and hence $SU(3)$ as a block-diagonal subgroup,
$$
SU(3)\subset U(3)\subset U(4),
\qquad
\dim_\mathbb{R}SU(4)=15 .
$$
So an $SU(3)$ gauge theory can be written on the enlarged carrier, with the colour triplet realized in a three-dimensional subspace of the four-dimensional defining space. The price is visible in the statement: the colour index is then an **external** index, adjoined to the algebra as the extra dimension of $\mathbb{C}^4$, and the gauge group is a subgroup of the *unit group of the enlarged matrix algebra*, not a structure of $\mathbb{B}$ itself. In the framework's own language, the triplet is not a module over $\mathbb{B}$; it is a module over $M_4(\mathbb{C})$ that happens to be three-dimensional, and the algebra's intrinsic simple module remains $\mathbb{C}^2$. The enlargement therefore does not bring the octet **into** the biquaternion algebra; it puts the octet beside the algebra and declares the extra structure as input. Whether such an enlarged carrier is a natural extension of the framework or an external construction is a question for the gauge-group-ceiling and Standard-Model companions; here the point is only that the embedding exists and costs an external colour index.

## The Boundary of the Category

The gluon is the boundary of this subcategory, and the boundary is algebraic. The framework's gauge sector is
$$
\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)
\qquad\text{and}\qquad
U(2)\cong\big(SU(2)\times U(1)\big)/\mathbb{Z}_2 ,
$$
which is the electroweak factor of the Standard Model's gauge group $SU(3)\times SU(2)\times U(1)$; the colour factor $SU(3)$ is not reached, and the octet is its marker. Three statements summarise the boundary and they should not be conflated.

- **The free gluon is reached.** A colour-fixed gluon is a massless spin-one material vector; its free equation, its helicity decomposition, its invariants and its quantization are the framework's, as for the photon.
- **The colour multiplet is not reached.** The octet presupposes the group $SU(3)$, whose compact algebra is eight-dimensional whereas the algebra's compact part is four-dimensional, and whose triplet is a three-dimensional irreducible representation whereas every $\mathbb{B}$-module is even-dimensional.
- **The self-couplings are reached in form, not in colour data.** The three-gluon and four-gluon vertices have the same Lie-algebraic structure as the framework's $SU(2)$ self-couplings, with $f^{abc}$ in place of $2\varepsilon^{abc}$; the framework supplies the form and would have to import the $SU(3)$ tensors $f^{abc}$ and $d^{abc}$.

The interpretation of the strong-sector results is not this article's. Confinement — the area law of the Wilson loop, the loss of partonic information at long distances, the informational reading of the deconfinement transition — belongs to the informational subcategory, and the lattice regularization in which the area law is established belongs to the massive-vector and lattice part of the present subcategory. What this article establishes is the algebraic ceiling: the algebra carries the electroweak factor exactly, carries a single gluon's free kinematics, and does not carry the octet.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The free kinematics of a colour-fixed gluon, as a massless material vector with the self-dual/anti-self-dual helicity split and the field-strength invariants of the companion articles. The form of the non-abelian self-couplings, as the expansion of the commutator with structure constants $f^{abc}=2\varepsilon^{abc}$ of the compact factor. The obstruction: the maximal compact subalgebra of $\mathbb{B}$ is $\mathfrak{u}(2)$ of real dimension four, computed from $\mathbb{B}=\mathfrak{u}(2)\oplus i\mathfrak{u}(2)$ and from $\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$, against $\dim_\mathbb{R}\mathfrak{su}(3)=8$; the module dimension, every $\mathbb{B}$-module being a sum of copies of $\mathbb{C}^2$ and hence even-dimensional over $\mathbb{C}$; the vanishing of the symmetric invariant, $\{T_a,T_b\}=-\tfrac12\delta_{ab}e_0$ and hence $d^{abc}=0$ for the compact factor; and the non-associativity of the octonions, which removes the Jacobi identity on which the curvature and the Bianchi identity depend.

**Imported, and left visible.** The group $SU(3)$ and its adjoint octet; the Gell-Mann matrices, the tensors $f^{abc}$ and $d^{abc}$ and their values; the colour triplet of the quarks; the QCD action, the self-couplings and the beta function; asymptotic freedom and confinement; and the enlarged-carrier embedding $SU(3)\subset U(3)\subset U(4)$ of $M_4(\mathbb{C})$. The algebra supplies the ceiling and the free kinematics; the colour data are standard and external.

**Not supplied.** The colour group, the octet, the triplet, the symmetric invariant, the colour factors, the running of the strong coupling and the confinement dynamics. The framework reaches the electroweak factor of the Standard Model gauge group and not the colour factor. As everywhere in the series, no empirical content is added.

## Summary

The gluon is the massless spin-one gauge boson of $SU(3)$, eightfold degenerate in the adjoint representation, with the action
$$
S_{\mathrm{QCD}}=-\frac14\int d^4x\,G^a_{\mu\nu}G^{a\mu\nu},
\qquad
G^a_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu,
$$
self-coupling through $f^{abc}$, asymptotically free with $b_0=11-\frac23N_f$, and confining at long distances. The framework reaches its **free kinematics**: a colour-fixed gluon is a massless material vector with the self-dual/anti-self-dual helicity decomposition and the field-strength invariants of the companion articles, indistinguishable at the level of the free field from the photon.

The framework does not reach the **octet**, and the failure has an algebraic root:
$$
\dim_\mathbb{R}\mathbb{B}=8,
\qquad
\dim_\mathbb{R}\mathfrak{u}(2)=4=\dim_\mathbb{R}\mathbb{M}_-,
\qquad
\dim_\mathbb{R}\mathfrak{su}(3)=8,
$$
so the compact part of the algebra is four-dimensional and cannot contain the eight-dimensional compact colour algebra. The module count reinforces the matter side: every $\mathbb{B}$-module is a sum of copies of $\mathbb{C}^2$ and has even complex dimension, whereas the colour triplet is three-dimensional; the octet's dimension eight is even, so this argument constrains the triplet and not the gluon. The invariant tensors are the third obstruction: the compact factor's symmetric invariant vanishes, $\{T_a,T_b\}=-\tfrac12\delta_{ab}e_0$ and $d^{abc}=0$, whereas $SU(3)$ has the nonzero symmetric tensor $d^{abc}$ with the components listed above, recomputed from the Gell-Mann matrices together with $f^{abc}$ and the Casimirs $C_2(\text{adj})=3$, $C_2(\text{fund})=\frac43$, $T(\text{fund})=\frac12$.

The one structure that carries the octet is the octonion algebra: $\dim_\mathbb{R}\mathbb{O}=8$, $\mathrm{Aut}(\mathbb{O})=G_2\supset SU(3)$, and $\mathbf{1}\oplus\mathbf{3}\oplus\bar{\mathbf{3}}$ under $SU(3)$. It is non-associative, so the commutator is not a Lie bracket, the Jacobi identity fails, and the curvature, Bianchi identity and BRST structure the framework uses all lapse. The octet is therefore not merely absent from the biquaternion algebra; it is present only in an algebra that lacks associativity, which is the property the framework's gauge construction cannot do without. The enlarged carrier $M_2(\mathbb{B})\cong M_4(\mathbb{C})\supset U(3)\supset SU(3)$ can host the group, at the price of making the colour index external. The gluon thus closes the subcategory as its ceiling: the framework's gauge sector is $U(1)\times SU(2)$, the electroweak factor, and the colour factor is outside.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$ | Biquaternion algebra; real dimension 8 |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ | Compact part of the algebra; real dimension 4 |
| $\mathfrak{u}(2)=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$ | Maximal compact subalgebra; real dimension 4 |
| $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, $[e_a,e_b]=2\varepsilon_{abc}e_c$ | Compact factor and its structure constants |
| $f^{abc}=2\varepsilon^{abc}$, $\{T_a,T_b\}=-\tfrac12\delta_{ab}e_0$ | Antisymmetric invariant of the compact factor, in the unnormalized basis $e_a$; vanishing symmetric invariant $d^{abc}=0$ |
| $\mathfrak{su}(3)$, $\dim_\mathbb{R}\mathfrak{su}(3)=8$ | Colour algebra; not reachable from the compact part |
| $G^a_\mu$ $(a=1,\dots,8)$ | Gluon fields; adjoint octet |
| $G^a_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu$ | Gluon field strength |
| $[\lambda^a,\lambda^b]=2if^{abc}\lambda^c$, $\{\lambda^a,\lambda^b\}=\tfrac43\delta^{ab}I+2d^{abc}\lambda^c$ | Gell-Mann tensors |
| $f^{123}=1$, $f^{147}=\tfrac12$, $f^{156}=-\tfrac12$, $f^{458}=\tfrac{\sqrt3}{2}$ | Sample nonzero $SU(3)$ components of the invariant $f^{abc}$ (verified) |
| $d^{118}=\tfrac1{\sqrt3}$, $d^{146}=\tfrac12$, $d^{448}=-\tfrac{1}{2\sqrt3}$, $d^{888}=-\tfrac1{\sqrt3}$ | Sample nonzero $SU(3)$ components of the invariant $d^{abc}$ (verified) |
| $C_2(\mathrm{adj})=3$, $C_2(\mathrm{fund})=\tfrac43$, $T(\mathrm{fund})=\tfrac12$ | $SU(3)$ Casimir data (verified) |
| $\beta_{g_s}=-\tfrac{g_s^3}{16\pi^2}b_0$, $b_0=11-\tfrac23N_f$ | One-loop QCD coefficient |
| $\tilde{F}=\bar{\tilde{\nabla}}\tilde{G}-\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{G})\in\mathbb{M}_-$ | Free field-strength biquaternion of one gluon |
| $\mathbb{B}\otimes\Lambda$ | Grassmann envelope adjacent to the algebra |
| $\mathbb{O}$, $\mathrm{Aut}(\mathbb{O})=G_2\supset SU(3)$ | Octonions; the non-associative carrier of $SU(3)$ |
| $M_2(\mathbb{B})\cong M_4(\mathbb{C})\supset U(4)\supset U(3)\supset SU(3)$ | Enlarged carrier; colour index external |
| $U(1)\times SU(2)$ | The framework's gauge sector; the electroweak factor |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$ metric (level 2) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Informational trace formula, distinct from the matrix trace |

## Further Reading

- M. Gell-Mann, "A schematic model of baryons and mesons," *Physics Letters* **8** (1964) 214–215, for the colour degree of freedom and the quark model.
- H. Fritzsch, M. Gell-Mann and H. Leutwyler, "Advantages of the color octet gluon picture," *Physics Letters B* **47** (1973) 365–368, for the colour octet of gauge fields and the non-abelian action.
- D. J. Gross and F. Wilczek, "Ultraviolet behavior of non-abelian gauge theories," *Physical Review Letters* **30** (1973) 1343–1346, for asymptotic freedom.
- H. D. Politzer, "Reliable perturbative results for strong interactions?," *Physical Review Letters* **30** (1973) 1346–1348, for the one-loop beta function and its sign.
- S. Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the non-abelian gauge theory, the structure constants and the Casimir data.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the QCD Lagrangian, the self-couplings and the beta function.
- W. G. McKay and J. Patera, *Tables of Dimensions, Indices, and Branching Rules for Representations of Simple Lie Algebras* (Dekker, 1981), for the $SU(3)$ invariant tensors and their normalization.
- J. F. Cornwell, *Group Theory in Physics, Vol. II* (Academic Press, 1984), for the symmetric and antisymmetric invariant tensors of $SU(3)$ and the absence of a symmetric invariant for $SU(2)$.
- M. Günaydin and F. Gürsey, "Quark structure and octonions," *Journal of Mathematical Physics* **14** (1973) 1651–1667, for the octonion realization of $SU(3)$ and the $G_2$ automorphism group.
- R. D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the failure of associativity and of the Jacobi identity in the octonions.
- J. C. Baez, "The octonions," *Bulletin of the American Mathematical Society* **39** (2002) 145–205, for the normed division algebras, $\mathrm{Aut}(\mathbb{O})=G_2$, and the $SU(3)$ structure of the imaginary octonions.
- K. G. Wilson, "Confinement of quarks," *Physical Review D* **10** (1974) 2445–2459, for the lattice formulation in which the confining area law is established.
- G. 't Hooft, "A planar diagram theory for strong interactions," *Nuclear Physics B* **72** (1974) 461–473, for the large-$N$ structure of the colour group.
