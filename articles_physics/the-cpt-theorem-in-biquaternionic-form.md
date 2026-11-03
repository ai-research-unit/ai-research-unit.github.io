# __The CPT Theorem in Biquaternionic Form__

## Introduction

The **CPT theorem** is the statement that a relativistic quantum field theory on Minkowski space whose Lagrangian is local, Hermitian and Lorentz invariant is invariant under the composition of **charge conjugation** $C$, **parity** $P$ and **time reversal** $T$, taken in any order. Its force is that the composition survives when the factors do not: a theory may violate $C$, $P$ and $T$ separately, and even the product $CP$, while $CPT$ remains exact. The proof requires locality (fields commute or anticommute outside the light cone), the positivity of the inner product, and the spin–statistics connection, and it is one of the deepest general results of quantum field theory.

This article asks what the biquaternion framework supplies for the theorem. The framework carries **more involutions than the standard four**, and they are easy to conflate. Alongside $C$, $P$ and $T$ the algebra provides the **complex conjugate** $\bar{\cdot}$ (conjugation of the four coefficients), the **quaternion conjugate** ${}^{\natural}$, and the **Hermitian conjugate** ${}^{*}=({}^{\natural})^{\,*}$. Building $C$, $P$ and $T$ therefore requires more than writing three matrices: each must be separated from the algebra's own conjugations, with which it shares the operation of complex conjugation but not the operation's meaning. The known trap, recorded in the companion on the Klein–Gordon equation, is to read a conjugate pair through the two-sector split $\mathbb{M}_+/\mathbb{M}_-$ — the temptation to place a field and its conjugate one in each sector. It is a trap because *none* of the three conjugations exchanges the sectors; the sector swap is multiplication by the central scalar imaginary $i$, which is neither a conjugation nor anti-linear. That fact, and not the notation, is what forbids the identification.

Two Dirac equations are in play, and the article keeps them apart from the first line.

- **The algebra equation.** The dynamics of the algebra is the chiral pair
  $$
  \tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\qquad
  \tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R,
  $$
  two first-order equations on the two chiral halves, with massless limit $\tilde{\nabla}\tilde{\Psi}_R=0$ and $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=0$. Each gradient acts by **left** multiplication, so the pair is a one-sided equation in the algebra. Chirality is invisible here: a right multiplication does not act on $\mathbb{B}$.
- **The module equation.** The framework's Dirac field is treated here, as in the companion articles on canonical quantization and on spin–statistics, through its **spinor-module representative** $\psi$, because the discrete operations act on the module. On the module the pair is the single four-component equation $(\mathbb{D}-m)\psi=0$, and the operator $\mathbb{D}$ is built from **two-sided** cells — a left multiplication for the gradient and a right multiplication for the chirality. This is the equation the three operations are defined on and checked against.

The passage between the two is what the two-sided operator theory supplies, and it is the reason the module equation can carry a chirality label while the algebra equation cannot. We build each of $C$, $P$ and $T$ explicitly, verify each one separately against the free module equation, and then check the composition $CPT$ explicitly rather than inferring it from the three factors. The composition check is not redundant, for a reason that is easy to miss: $C$ and $T$ are **anti-linear**, so the internal factor of the product is $\eta_C\eta_P^*\eta_T^*$, not $\eta_C\eta_P\eta_T$, and the two differ whenever the phases are not fixed by the conjugation.

We work in the **cell frame** of the canonical-quantization and spin–statistics articles. With $L_a\psi=a\psi$, $R_b\psi=\psi b$ and the two-sided cell $L_aR_b$, so that $L_aR_b\psi=a\psi b$, the four generator cells of the module are
$$
G_0=iR_{\vec e_x}^{\mathrm{pau}}=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
G_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
G_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
G_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}.
$$
Each carries one factor of $i$, and naming them $G_\mu$ is what keeps that factor from being written out again in every product. The factor is structural: it is what gives the four generators the metric $g$ rather than its negative, since without it the first would square to $-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and the other three to $+L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$.
$$
G_0^{2}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad G_1^{2}=G_2^{2}=G_3^{2}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad G_\mu G_\nu=-G_\nu G_\mu\quad(\mu\ne\nu),
$$
which are the Clifford relations of the metric $g=\operatorname{diag}(+1,-1,-1,-1)$. A product of two generators is where $i^{2}=-1$ is spent: the two factors of $i$ give $-1$, and that sign combines with $\vec e_k^{2}=-e_t$ and with $\vec e_j\vec e_k=\pm\vec e_l$ so that the product is again a single cell, this time with no $i$ in it. This is used repeatedly below: the generators themselves are not written out again, only $G_\mu$ and the plain cells $L_aR_b$ that the internal factors need. The section The Gamma Formulation is the only place this article writes gamma symbols, and it uses them for exactly these four cells.

The chirality cell and the volume element are
$$
\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},\qquad
\omega=-R_{\vec e_z}^{\mathrm{pau}},\qquad
\Gamma=i\omega,\qquad
\Gamma^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},
$$
and $\Gamma$ anticommutes with each $G_\mu$. The framework identifies $\omega$ with the image of the scalar imaginary under $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$. Neither cell is diagonal in the cell frame; in the chiral basis they are $\Gamma=\mathrm{diag}(-I_2,I_2)$ and $\omega=\mathrm{diag}(iI_2,-iI_2)$, and every diagonal form written below is in that basis. A Dirac spinor is written in chiral blocks as $\psi=(\psi_L,\psi_R)^{T}$ with $\psi_L\in S$ and $\psi_R\in\bar{S}$. Every derivative in a cell display below is with respect to $x_\mu=(t',x,y,z)$; the $ict'$ normalization $Q_t=ict'$ is used only where it is named. We work in natural units $\hbar=c=1$ except in the mass-shell relation, and borrow the plane-wave spinors $w^{(r)}(\vec p),v^{(r)}(\vec p)$ and the spin sums of the solutions article unchanged.

The division between what is established and what is only transcribed is kept explicit throughout.

- **Established, and recomputed below.** The three operations on the spinor-module Dirac field are
  $$
  C[\psi]=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\,\psi^{*},\qquad
  P[\psi]=G_0\,\psi(t',-\vec x),\qquad
  T[\psi]=-L_{\vec e_y}^{\mathrm{pau}}\,\psi^{*}(-t',\vec x),
  $$
  with $\vec x=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$. The three internal factors are
  $$
  \eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
  \eta_P=G_0=iR_{\vec e_x}^{\mathrm{pau}},\qquad
  \eta_T=-L_{\vec e_y}^{\mathrm{pau}},
  $$
  which square to $\eta_C^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $\eta_P^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and $\eta_T^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. Each operation maps every solution of the free equation $(\mathbb{D}-m)\psi=0$ to a solution, verified separately on the differential equation, on three on-shell momenta and on a superposition of both frequency branches. The field map $T$ is anti-linear, $T[i\psi]=-i\,T[\psi]$, so it conjugates the scalar imaginary; the operator it induces on the mode algebra is anti-unitary. $C$ and $P$ anticommute with $\Gamma$ and exchange the chiral halves; $T$ commutes with $\Gamma$ and preserves them; hence $CPT$ preserves chirality. $C$ exchanges the two frequency branches, so at the operator level it exchanges the particle and antiparticle modes. Of the internal factors, $\eta_T=-L_{\vec e_y}^{\mathrm{pau}}$ is a left multiplication and an **even** element, a real quaternion in $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$; $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and $\eta_P=iR_{\vec e_x}^{\mathrm{pau}}$ are **odd** and have no representative in $\mathbb{B}$. The composition $\Theta=C\circ P\circ T$ acts as $\Theta[\psi](x)=\eta_{CPT}\,\psi(-x)$ with $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$; in the phase convention above,
  $$
  \eta_{CPT}=\eta_C\eta_P\eta_T=\Gamma=i\omega .
  $$
  Here $\omega=-R_{\vec e_z}^{\mathrm{pau}}$ is the volume element, the element the framework identifies with the biquaternion scalar imaginary, and on the Dirac module it acts as $\mathrm{diag}(iI_2,-iI_2)$.
- **Transcribed, not derived.** The CPT theorem itself, together with the hypotheses that prove it: locality, Hermiticity of the Lagrangian, Lorentz invariance, positivity and spin–statistics. The computation below exhibits the composition as a symmetry of *one* free equation; it does not show that the composition survives interactions, which is the content of the theorem. Nothing here derives CPT from the biquaternion algebra. Also transcribed is the Clifford-algebra classification of the operations as the fundamental automorphisms of $\mathrm{Cl}_{n,m}$ together with the charge-conjugation pseudoautomorphism, which is recorded below as a second interpretation of the same eight operations and as the source of their $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ group structure.
- **Gap, left visible.** The framework does not fix a $\mathbb{B}$-intrinsic form of $C$ and $P$: their internal factors are odd Clifford cells, outside $\mathbb{B}$, so they are operations of the Clifford algebra or of the module, not inner operations of the biquaternion algebra. Whether they admit a $\mathbb{B}$-intrinsic realization is unbuilt. Separately, the parent's mass term is the linear chiral pair of the Dirac article, whose spinor representative is the massive Dirac equation verified above to be $C$-invariant; the algebra's anti-linear object is the real structure $\flat=-{}^{*}$, a separate Majorana-type pairing, and whether $C$ is a symmetry of the single-field equation built on $\flat$ is the open reading developed in the neutrino companion.

## The Discrete Operations and the Algebra

Three different structures are in play, and the article's first task is to keep them apart.

### The Algebra Equation and the Module Equation

The two equations are the two levels of one dynamics, and the notation of each is closed.

**The algebra equation.** The gradient $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$ acts by left multiplication, and its quaternion conjugate $\tilde{\nabla}^{\natural}$ squares with it to the scalar d'Alembertian, $\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}=\Box$. The chiral pair is the first-order dynamics of the algebra, and its two members are one-sided: no right multiplication appears in it, so no chirality operator appears either.

**The module equation.** The two members are one operator on $\mathbb{B}\oplus\mathbb{B}$. With $\Psi=(\Psi_L,\Psi_R)$ and
$$
\mathbb{D}\Psi=\bigl(\tilde{\nabla}\Psi_R,\ \tilde{\nabla}^{\natural}\Psi_L\bigr),
$$
the pair is $(\mathbb{D}-m)\Psi=0$, and $\mathbb{D}^2=\Box\,I$. On the four-component spinor-module representative $\psi$ the same operator acts through the cells, and in the cell frame it reads
$$
\mathbb{D}=-R_{\vec e_x}^{\mathrm{pau}}\,\partial/\partial t'-\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\,\partial/\partial x_k ,
$$
which is the two-sided form: the spatial terms are the two-sided cells, the time term is a pure right multiplication, and the frame is completed by the chirality, itself a pure right multiplication, $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}$. The four minus signs are the four factors of $i$ that the generators carry, since $-R_{\vec e_x}^{\mathrm{pau}}=iG_0$ and $-L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=iG_k$; in the generators the operator is the contraction
$$
\mathbb{D}=i\,G_\mu\,\partial_\mu=i\Bigl(G_0\,\partial_{t'}+\sum_kG_k\,\partial_{x_k}\Bigr),
$$
which has no metric sign anywhere because the metric is already in the generators, $G_0^{2}=1$ and $G_k^{2}=-1$. On a plane wave $e^{-ip\cdot x}$ with $p\cdot x=E_{\vec p}t'-\vec p\cdot\vec x$ the factors of $i$ cancel again:
$$
\mathbb{D}=G_0E_{\vec p}-\sum_k G_kp_k ,
$$
the operator that appears in the verification below.

The two-sided operator theory is what lets the two levels be written in one frame, and it is also what separates them. The cells $L_aR_b$ carry the left multiplication of the algebra equation and the right multiplication of the chirality: the four generator cells are of that form, the chirality $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}$ is a pure right multiplication, and the mass is the scalar $m$ times the identity. A one-sided equation has no room for a pure right multiplication, so chirality belongs to the module equation; a two-sided cell can carry both. **The discrete operations below are operations on the module equation, not on the algebra equation.**

**The Clifford algebra and its even part.** The sixteen products of the four generator cells span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, of real dimension $16$; the sixteen two-sided cells $L_{a}R_{b}$ are a different set of operators, spanning the opposite real form $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ of the same real dimension, and the two are not isomorphic. The **even subalgebra of $\mathrm{Cl}_{1,3}$** is spanned by the identity, the six bivectors, and the volume element $\omega$, and is isomorphic to $\mathbb{B}$; the biquaternion units correspond to spatial bivectors by
$$
\vec e_x\mapsto G_2G_3=L_{\vec e_x}^{\mathrm{pau}},\qquad \vec e_y\mapsto G_3G_1=L_{\vec e_y}^{\mathrm{pau}},\qquad \vec e_z\mapsto G_1G_2=L_{\vec e_z}^{\mathrm{pau}},
$$
and the scalar imaginary to the volume element $\omega=G_0G_1G_2G_3=-R_{\vec e_z}^{\mathrm{pau}}$ — the corpus's identification, which belongs to this isomorphism $\mathbb{B}\to\mathrm{Cl}_{1,3}^{+}$ and is not a statement about the matrix realization $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ used elsewhere in this article. The three entries are the whole point of the $i$ bookkeeping: $G_2G_3$ is $(i)(i)L_{\vec e_y\vec e_z}^{\mathrm{pau}}R_{\vec e_y\vec e_y}^{\mathrm{pau}}$, the $i^{2}$ gives $-1$, the factor $R_{\vec e_y\vec e_y}^{\mathrm{pau}}=R_{-e_t}^{\mathrm{pau}}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ gives a second $-1$, the two cancel, and the quaternion product $\vec e_y\vec e_z=\vec e_x$ leaves the single cell $L_{\vec e_x}^{\mathrm{pau}}$. Each image squares to $-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and the three multiply as the quaternion units do, $\vec e_x\vec e_y=\vec e_z$ included, so the assignment is a homomorphism on the generators; what matters below is only that it is one. The **odd part** — the span of the individual generators — is *not* contained in $\mathbb{B}$. This matters below: an even element acts on the Dirac module block-diagonally, preserving each chiral half, while an odd element acts off-diagonally and **exchanges the two chiral halves**. The chirality cell $\Gamma$ anticommutes with every generator and hence commutes with every even element; it is a Lorentz-invariant label.

**The three conjugations of the algebra.** They are distinct maps, and they behave differently on the sectors and on the scalar imaginary:

| Map | Action on coefficients | Scalar imaginary | Type and effect |
|---|---|---|---|
| Quaternion ${}^{\natural}$ | $(Q_t,Q_k)\mapsto(Q_t,-Q_k)$ | $i\mapsto i$ | real-linear anti-automorphism |
| Complex $\bar{\cdot}$ | $Q_\mu\mapsto Q_\mu^{*}$ | $i\mapsto -i$ | $\mathbb{C}$-antilinear involution; relates $S$ to $\bar{S}$ |
| Hermitian ${}^{*}=({}^{\natural})^{\,*}$ | $(Q_t,Q_k)\mapsto(Q_t^{*},-Q_k^{*})$ | $i\mapsto -i$ | $\mathbb{C}$-antilinear involution; $+1$ on $\mathbb{M}_+$, $-1$ on $\mathbb{M}_-$ |

All three **preserve each sector** $\mathbb{M}_-$ and $\mathbb{M}_+$. The map that exchanges the sectors is not a conjugation at all: it is multiplication by the central scalar imaginary,
$$
i\,\mathbb{M}_-= \mathbb{M}_+,\qquad i\,\mathbb{M}_+= \mathbb{M}_-,
$$
and $i$ commutes with everything, so it is neither an anti-linear map nor an involution of the kind a discrete symmetry needs. This is the precise content of the trap: a conjugate pair of fields cannot be assigned one member to each sector, because conjugation preserves the sectors and the sector swap is a central phase rotation. It is worth recording separately that chirality is *also* not the sector split: the chiral decomposition lives on the four-dimensional Dirac module $\Delta=S\oplus\bar{S}$ and is a module decomposition, while the sector decomposition lives on the eight-dimensional algebra $\mathbb{B}$ and is an algebra decomposition; they share no projector.

**The discrete operations are module operations.** $C$, $P$ and $T$ act on the Dirac spinor, not on the algebra element. Their internal factors are cells, and the three cases differ:

- $T$ has the internal factor $\eta_T=-L_{\vec e_y}^{\mathrm{pau}}$, a pure **left** multiplication by the real quaternion $-\vec e_y$, and therefore an **even** element of the Clifford algebra. Its module action is left multiplication by an element of $\mathbb{B}$.
- $C$ and $P$ have the internal factors $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and $\eta_P=G_0$, both **odd**: neither is a pure left multiplication, so neither is an element of $\mathbb{B}$, and both exchange the chiral halves. Charge conjugation and parity are therefore not inner operations of the biquaternion algebra.

None of the three is a sector swap, and none of them needs the sector split to be stated.

## The Three Operations Built Explicitly

Let $\psi$ solve the free Dirac equation $(\mathbb{D}-m)\psi=0$, with $\mathbb{D}$ the two-sided operator above acting on the module in the chiral basis. A discrete operation is a map $\psi\mapsto\psi_2$ whose output also solves the equation. We take the operations in the standard form: $C$ is local and anti-linear, $P$ is a spatial reflection and linear, $T$ is a time reflection and anti-linear. Each is defined by an internal cell $\eta$ fixed by the requirement that the transformed field satisfy the same equation, and the requirement determines $\eta$ up to a phase, which is a convention.

The three conditions are commutation conditions, because each internal cell is invertible. The generators are $G_\mu$, $\mu=0,1,2,3$, and $G_\mu^{*}$ is the module conjugate of $G_\mu$. For a field map of the form $\psi\mapsto\eta\,\psi^{*}(\Lambda x)$ the transformed field solves the equation precisely when
$$
\eta^{-1}G_\mu\,\eta=\pm\,G_\mu^{*}
$$
holds on each generator, the sign being fixed by the reflection of the argument and the conjugate present because $C$ and $T$ are anti-linear; for parity, which is linear, the same test reads $\eta^{-1}G_\mu\eta=\pm G_\mu$ with no conjugate. Since each $\eta$ squares to $\pm L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and is therefore its own inverse up to sign, the identity reduces on each generator to a commutation or an anticommutation, which is an algebraic fact about the cells and does not depend on the realization. The conjugate signs are the ones the module conjugation gives,
$$
G_0^{*}=G_0,\qquad G_1^{*}=G_1,\qquad G_3^{*}=G_3,\qquad G_2^{*}=-G_2,
$$
in the chiral-basis realization used here: three of the four generators are fixed and the second spatial one is negated.

### Charge conjugation

Define
$$
C[\psi]=\eta_C\,\psi^{*},\qquad \eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}.
$$
The equation is complex-conjugated, so the condition on the generator cells is $\eta_C^{-1}G_\mu\eta_C=-G_\mu^{*}$. It holds because $\eta_C$ **anticommutes** with the three generators the conjugation fixes and **commutes** with the one it negates:
$$
\eta_C^{-1}G_0\,\eta_C=-G_0,\qquad
\eta_C^{-1}G_1\,\eta_C=-G_1,\qquad
\eta_C^{-1}G_2\,\eta_C=+G_2,\qquad
\eta_C^{-1}G_3\,\eta_C=-G_3 .
$$
Because $\psi^{*}$ enters, $C$ is anti-linear. The internal factor $\eta_C$ is odd, so $C$ anticommutes with $\Gamma$: charge conjugation flips chirality.

**The representative depends on the realization.** The condition above fixes $\eta_C$ only inside a realization of the generators, meaning a choice of the conjugation that $\psi^{*}$ denotes. This article's realization is the cell frame, where $\psi^{*}$ is the module conjugation — the anti-linear map that carries the chiral half $S$ onto $\bar S$. The same cells read against the **coefficient conjugation** of the algebra give a different answer: every generator $iL_{a}R_{b}$ is purely imaginary, so that conjugation negates all four, the condition reduces to a commutation requirement, and *every* nonzero scalar satisfies it; the involution condition $\eta_C^{2}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ then narrows the scalar to $\pm1$. The transposed form $\psi_c=\eta\,\bar\psi^{T}$ carries the cell $\eta=R_{\vec e_x}^{\mathrm{pau}}$ in the cell frame, with $\eta^{2}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. Neither formula may be carried across the change of conjugation: $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ conjugates through $\psi^{*}$, and the transposed $\eta$ through the transpose, and the two conjugations do not agree on which cells they fix. Writing $-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ for $\eta_C$ is right; reading that cell against the coefficient conjugation instead of the module conjugation is the error this paragraph exists to prevent.

### Parity

Define
$$
P[\psi](t',\vec x)=\eta_P\,\psi(t',-\vec x),\qquad \eta_P=G_0=iR_{\vec e_x}^{\mathrm{pau}}.
$$
Only the spatial derivatives change sign, and the field is not conjugated, so the condition is $\eta_P^{-1}G_0\eta_P=G_0$ and $\eta_P^{-1}G_k\eta_P=-G_k$ for the three spatial generators. It holds because $\eta_P$ **commutes** with the time generator and **anticommutes** with each spatial one:
$$
\eta_P^{-1}G_0\,\eta_P=G_0,\qquad
\eta_P^{-1}G_k\,\eta_P=-G_k\quad(k=1,2,3).
$$
Parity is linear, and since $\eta_P$ is odd it anticommutes with $\Gamma$: parity flips chirality.

### Time reversal

Define
$$
T[\psi](t',\vec x)=\eta_T\,\psi^{*}(-t',\vec x),\qquad \eta_T=-L_{\vec e_y}^{\mathrm{pau}}=G_1G_3.
$$
The time derivative changes sign, the spatial derivatives do not, and the field is conjugated, so the condition is $\eta_T^{-1}G_0\eta_T=G_0^{*}$ and $\eta_T^{-1}G_k\eta_T=-G_k^{*}$. It holds because $\eta_T$ **commutes** with the time generator and with the second spatial one, and **anticommutes** with the first and third:
$$
\eta_T^{-1}G_0\,\eta_T=G_0,\qquad
\eta_T^{-1}G_2\,\eta_T=G_2,\qquad
\eta_T^{-1}G_1\,\eta_T=-G_1,\qquad
\eta_T^{-1}G_3\,\eta_T=-G_3 .
$$
Since $\eta_T$ is even, $T$ commutes with $\Gamma$: time reversal preserves chirality. Note that $\eta_T^{2}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, so the internal factor is a complex structure on the module; only the operation is of order two up to the free phase.

### $T$ is anti-linear

The conjugation in $T$ is not a calculational convenience; it is what makes the field map anti-linear, the classical counterpart of the anti-unitary operator. With $i$ the scalar imaginary,
$$
T[i\psi]=\eta_T(i\psi)^{*}=\eta_T(-i)\psi^{*}=-i\,\eta_T\psi^{*}=-i\,T[\psi].
$$
Both $C$ and $T$ are anti-linear, and both conjugate the scalar imaginary. The difference between them appears when the field map is promoted to an operator on the mode algebra: the operator induced by $T$ is anti-unitary, while the operator induced by $C$ is unitary. The reason is that $T$ reverses the sign of the evolution phase $e^{-iHt}$, and the conjugation is what turns the reversed evolution into a symmetry; $C$ only exchanges the particle and antiparticle labels at fixed energy, so its induced operator is linear. This article constructs the field maps, so it records the anti-linearity of both and leaves the mode operators aside. The framework's single scalar imaginary $i$ — the same $i$ that appears in the $ict'$ gradient and in the volume element $\omega$ — is exactly what the conjugation negates. A time reversal written without the conjugation (as $T:\psi\mapsto\eta_T\psi(-t',\vec x)$) is a different, linear map, and is *not* a symmetry of the Dirac equation.

The three operations are collected below. The last column records the chirality action that follows from the parity of the internal cell.

| Operation | Action on $\psi$ | Internal cell | Linear? | Chirality |
|---|---|---|---|---|
| $C$ | $-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\,\psi^{*}(x)$ | $-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ (odd) | anti-linear | flips |
| $P$ | $G_0\,\psi(t',-\vec x)$ | $G_0$ (odd) | linear | flips |
| $T$ | $-L_{\vec e_y}^{\mathrm{pau}}\,\psi^{*}(-t',\vec x)$ | $-L_{\vec e_y}^{\mathrm{pau}}$ (even) | anti-linear | preserves |

Two remarks on conventions. First, the phases of $\eta_C$ and $\eta_T$ are not fixed by the requirement that the equation be preserved; only the commutation conditions are, and they fix the internal factor only up to an arbitrary nonzero complex multiple. The companion on the electron writes charge conjugation in the transposed form $\eta\,\bar{\psi}^{T}$ with $\eta=R_{\vec e_x}^{\mathrm{pau}}$; that is the transposed realization of the same operation, not a different operation, and the free phase relates the two realizations. Second, the individual phases are not observable; what is observable is the composition, and changing a phase changes the internal factor of the composition, which is why the composition must be checked independently (next section).

## Each Operation Preserves the Free Equation

The verification was carried out on the differential equation itself, not only on a momentum-space identity, and on cases other than the one that suggested the definitions. The working field was the general solution
$$
\psi=\bigl(A(\vec p)+m\bigr)\chi\,e^{-ip\cdot x}+\bigl(A(\vec p)-m\bigr)\chi_2\,e^{+ip\cdot x},
$$
with
$$
A(\vec p)=G_0E_{\vec p}-\sum_k G_kp_k,\qquad
p\cdot x=E_{\vec p}t'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),\qquad E_{\vec p}^2=\vec p^2+m^2,
$$
and $\chi,\chi_2$ arbitrary constant spinors. The first branch is positive-frequency and the second negative-frequency, and their sum is a general solution of the free equation by linearity. Substituting, conjugating and reflecting as the definitions require, the residual $(\mathbb{D}-m)$ acting on each transform was reduced symbolically and found to vanish. The checks were run for the three parameter sets
$$
(m,\vec p)=(3,(1,2,2)),\qquad (5,(3,4,0)),\qquad (\tfrac{7}{2},(1,0,-2)),
$$
each with the corresponding $E_{\vec p}=+\sqrt{\vec p^2+m^2}$, and with both frequency branches present simultaneously. All three operations passed on all three cases.

The individual checks are worth a word each, because they test different parts of the structure.

- **$C$.** The commutation conditions above were verified as cell identities, and the transformed field was confirmed to solve the equation. The same computation identifies *which* solution the transform produces. On shell $A(\vec p)^2=E_{\vec p}^2-\vec p^2=m^2$, so the two factors in the decomposition satisfy $\bigl(A(\vec p)\mp m\bigr)\bigl(A(\vec p)\pm m\bigr)=0$. Conjugation by $\eta_C$ sends $A(\vec p)^{*}$ to $-A(\vec p)$, because it sends each generator to minus its conjugate; hence
  $$
  \eta_C\,w^{*}=\eta_C\bigl(A(\vec p)^{*}+m\bigr)\chi^{*}=\bigl(-A(\vec p)+m\bigr)\eta_C\chi^{*},
  $$
  which is annihilated by $A(\vec p)+m$: the transform is a **negative-frequency** amplitude. So $C$ exchanges the two branches; in the mode expansion it exchanges the particle operator $a^{\mathrm{fop}}$ with the antiparticle operator $b^{\mathrm{fop}}$, which is the operator-level statement that the conserved charge reverses sign. This was checked on the same three cases.
- **$P$.** The commutation with the time generator and the anticommutation with the three spatial ones were verified, and the reflected field was confirmed to solve the equation. The transform keeps the positive-frequency branch positive-frequency and reverses the momentum, $\vec p\mapsto-\vec p$.
- **$T$.** The four commutation conditions were verified, and the conjugated-reflected field was confirmed to solve the equation. Because $T$ is anti-linear, the check on the superposition is the sharpest one: a linear map that ignored the conjugation would send the negative-frequency branch to the wrong sign.

Two negative results belong here, to prevent a future pass from claiming more than was checked.

- The verification is of the **free** equation. Nothing was checked for a field with a local interaction, and no claim is made there. The reason the free check cannot be promoted is stated at the end of this article: the CPT theorem is precisely the statement that the composition survives interactions when the factors do not, and a free-field identity contains no information about that.
- The operation $T$ was *not* defined as the linear map $\psi\mapsto\eta_T\psi(-t',\vec x)$ that is sometimes written. That map does not preserve the equation; the check was performed with the conjugation present.

## The Algebra's Conjugations Are Not the Discrete Operations

The temptation that the trap names is to identify one of the operations $C$, $P$, $T$ with one of the algebra's conjugations, or to read the particle–antiparticle pair as the sector pair. Three independent facts close the identification.

**First, the conjugations preserve both sectors.** For a general element $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, membership in $\mathbb{M}_-$ means $Q_t$ purely imaginary and $Q_x,Q_y,Q_z$ real, and membership in $\mathbb{M}_+$ means $Q_t$ real and $Q_x,Q_y,Q_z$ purely imaginary. Each of ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ maps either condition to itself: conjugation negates the scalar or the vector coefficients but does not interchange the two patterns. The Hermitian conjugate is the identity on $\mathbb{M}_+$ and minus the identity on $\mathbb{M}_-$, so it *defines* the sectors rather than exchanging them. The map that interchanges them is $i\,\mathbb{M}_\pm=\mathbb{M}_\mp$, and $i$ is central, hence not a conjugation and not anti-linear. A particle–antiparticle or chiral-conjugate pair therefore cannot be placed one member in each sector.

**Second, the sector split and the chirality split are different decompositions of different objects.** The chiral projectors
$$
P_{L}=\tfrac12\bigl(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}-\Gamma\bigr),\qquad
P_{R}=\tfrac12\bigl(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}+\Gamma\bigr)
$$
act on the Dirac module $\Delta=S\oplus\bar S$ of complex dimension four. The sector projectors act on the algebra $\mathbb{B}$ of real dimension eight. They share no projector, and the electron article reaches the same conclusion from the physical side. Recorded here only because a reader who has just seen $C$ and $P$ exchange the chiral halves might try to read that exchange as a sector exchange; it is not one.

**Third, the operations are module maps, and only $T$'s internal factor belongs to the algebra.** $T$'s factor $\eta_T=-L_{\vec e_y}^{\mathrm{pau}}$ is a pure left multiplication by the real quaternion $-\vec e_y$, hence an even element of $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$; $C$'s $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and $P$'s $\eta_P=iR_{\vec e_x}^{\mathrm{pau}}$ are odd and act off-diagonally, exchanging $S$ and $\bar{S}$. The odd part of $\mathrm{Cl}_{1,3}$ is not contained in the even subalgebra, so $C$ and $P$ have no representative in $\mathbb{B}$. This is the sharp form of the framework's difficulty with the discrete operations: the algebra contains the operations that preserve chirality ($T$, and the even Lorentz action) and does not contain those that exchange it ($C$ and $P$). The electroweakly relevant fact that $C$ and $P$ are precisely the operations Nature violates separately, while their product with $T$ is the one that survives, is not explained by this structure; it is the theorem's content, and it is imported.

The anti-linear part of $C$ and of $T$ is exactly the algebra's complex conjugation $\bar{\cdot}$. This is the same real-structure operation that relates $S$ to $\bar S$ and that distinguishes the two chiral halves inside the simple algebra, and it is what supplies the anti-linear part of the discrete operations. It is *not* the mass. The parent's mass term is the linear chiral pair of the Dirac article, and the algebra's anti-linear real structure $\flat=-{}^{*}$ is a separate, order-reversing conjugation whose pairing is a Majorana-type coupling. The discrete operations are symmetries of the kinetic equation; the real structure is a dynamical pairing.

## The Composition CPT, Checked as a Composition

Compose the three operations by applying $T$ first, then $P$, then $C$, and write $\Theta=C\circ P\circ T$. Because $C$ and $T$ are anti-linear, the composition must be evaluated as a composition, not by multiplying the three internal factors. Applied to a field $\psi$,
$$
\psi
\xrightarrow{\;T\;}\eta_T\,\psi^{*}(-t',\vec x)
\xrightarrow{\;P\;}\eta_P\eta_T\,\psi^{*}(-t',-\vec x)
\xrightarrow{\;C\;}\eta_C(\eta_P\eta_T)^{*}\psi(-t',-\vec x),
$$
so that
$$
\boxed{\;\Theta[\psi](x)=\eta_{CPT}\,\psi(-x),\qquad
\eta_{CPT}=\eta_C\,\eta_P^{*}\,\eta_T^{*}\;}.
$$
The internal factor is built from the **conjugates** of $\eta_P$ and $\eta_T$, which is the bookkeeping that a naive product $\eta_C\eta_P\eta_T$ would miss. In the convention of this article, $\eta_P=G_0$ and $\eta_T=-L_{\vec e_y}^{\mathrm{pau}}$ are cells that the module conjugation fixes, so $\eta_P^{*}=\eta_P$ and $\eta_T^{*}=\eta_T$, and
$$
\boxed{\;\eta_{CPT}=\eta_C\eta_P\eta_T=(-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})\,G_0\,(-L_{\vec e_y}^{\mathrm{pau}})=\Gamma\;}.
$$
The agreement with the naive product in *this* convention is an accident of internal factors that the conjugation fixes, and should not be taken as general. If, for example, the phase convention $\eta_T'=i\eta_T$ is used — equally admissible, since the equation-preservation condition leaves the phase of the internal factor free — then the true composition has $\eta_{CPT}=\eta_C\eta_P^{*}(\eta_T')^{*}=-i\Gamma=\omega$, while the naive product gives $i\Gamma=-\omega$. The two differ by a sign. The operation $T$ and the composition were re-verified in that convention as well, and both still map solutions to solutions; the point is that the internal factor is a convention-dependent phase and can only be read off from the composition itself. This is the concrete sense in which verifying $C$, $P$, $T$ individually and multiplying is not the same as verifying $CPT$.

The composition has the following verified properties.

- **It is a symmetry of the free equation.** $\Theta[\psi]$ solves $(\mathbb{D}-m)\psi=0$ whenever $\psi$ does. This was checked on all three parameter sets and with both frequency branches present.
- **It is complex-linear.** $\Theta[i\psi]=+i\,\Theta[\psi]$: the two anti-linear factors $C$ and $T$ combine into a linear map on the field, since $\Theta[\psi](x)=\eta_{CPT}\psi(-x)$ carries no conjugation. (The standard $CPT$ *operator* on the mode algebra is anti-unitary; that operator is not constructed here, and it is the field map that this article defines.)
- **It reverses both the spacetime argument and the charge.** The argument is $-x$, and because $C$ exchanges the frequency branches, a particle is mapped to an antiparticle.
- **It preserves chirality.** $C$ and $P$ each anticommute with $\Gamma$ and $T$ commutes with it; the composition anticommutes twice. Equivalently, $\eta_{CPT}=\Gamma$ commutes with $\Gamma$, consistent with the fact that $\eta_{CPT}$ is an even element of the Clifford algebra.
- **Its internal factor is a phase times the volume element, and the chirality cell in this convention.** The volume element $\omega=-R_{\vec e_z}^{\mathrm{pau}}=-i\Gamma$ is the element the framework identifies with the scalar imaginary $i$: on the defining module $S$ the central imaginary acts as $iI_2$, and on the Dirac module $\Delta=S\oplus\bar S$, whose right-handed half carries the conjugate action, the same central element acts as $\mathrm{diag}(iI_2,-iI_2)=\omega$. In the convention above the internal factor is $\eta_{CPT}=\Gamma=i\omega$, the chirality cell itself. The factor is fixed only up to the free phases of $\eta_C$ and $\eta_T$; its identification with the volume element is the algebra statement, and its action as the chirality cell is the module statement.

**What this does and does not establish.** It establishes that the free biquaternion Dirac equation carries three discrete operations whose composition is a symmetry, that the composition's internal factor is a phase times the volume element (the chirality cell in the convention above), and that the anti-linearity resides in the factors $C$ and $T$ alone, where it is the algebra's complex conjugation $\bar{\cdot}$; the parent's mass term is linear, so the discrete anti-linearity is not shared with it.

It does **not** establish the CPT theorem. A free equation is a special case in which $C$, $P$ and $T$ are separately symmetries, so the composition is a symmetry for the trivial reason. The theorem's content is that $CPT$ remains a symmetry when $C$, $P$ and $T$ do not, and that statement rests on locality, Hermiticity, Lorentz invariance and spin–statistics, none of which is derived here. The correct summary is that the framework *exhibits* CPT on the free field and *transcribes* the theorem.

## The Discrete Operations in the Clifford Literature

A second interpretation of the same eight operations comes from the Clifford-algebra literature, where the discrete symmetries of a Dirac-type equation are classified by the intrinsic order-two maps of the real algebra $\mathrm{Cl}_{n,m}$. It is recorded beside the module construction above because it supplies the one thing that construction does not: the reason the operations close into a group, and why that group is the eight-element $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$.

**The fundamental automorphisms.** Every real Clifford algebra $\mathrm{Cl}_{n,m}$ carries three distinguished non-trivial order-two maps, and with the identity they form the group of **fundamental automorphisms**:

| map | name | action on a $k$-blade |
|---|---|---|
| $A\mapsto A$ | identity | $+1$ |
| $A\mapsto A^{\star}$ | involution (grade involution) | $(-1)^{k}$ |
| $A\mapsto A^{\sim}$ | reversion | $(-1)^{k(k-1)/2}$ |
| $A\mapsto A^{\mathrm{rev}}$ | conjugation | $(-1)^{k(k+1)/2}$ |

The conjugation is the composite of the involution and the reversion, so the non-trivial maps form $\{1,\star,\sim,\mathrm{rev}\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$. These are exactly the intrinsic maps that the corpus's *Clifford Algebra Representation* computes for $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, where the generators are the grade-one elements $i\vec e_k$: the grade involution is the algebra's complex conjugation $\bar{\cdot}$, reversion is the Hermitian conjugation ${}^{*}$, and their composite, the Clifford conjugation, is the quaternion conjugation ${}^{\natural}$. The classification is therefore not foreign to the algebra; it names maps the algebra already has.

**The correspondence with $P$ and $T$.** The literature attaches the discrete operations to these maps by the dictionary: space inversion $P$ is the involutive automorphism $A\to A^{\star}$; time reversal $T$ is the antiautomorphism $A\to A^{\sim}$; and the full reflection $PT$ is the antiautomorphism $A\to A^{\mathrm{rev}}$. The four operations obtained from these by composing with charge conjugation, $C$, $CP$, $CT$ and $CPT$, correspond to the correspondingly twisted maps. Every operation is then a product of the three generators $P$, $T$ and $C$, each of order two as a map of the algebra (the module implementation carries the free phase, so its cell may square to $-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$), and the eight products close on themselves:

$$
\boxed{\;\{1,\,P,\,T,\,PT,\,C,\,CP,\,CT,\,CPT\}\;\cong\;\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2\;}.
$$

This is the group-theoretic fact behind the standard statement that the discrete operations form an eight-element group. In the classification it is a statement about the intrinsic maps of $\mathrm{Cl}_{n,m}$ rather than an empirical input, and it is the reason the "more involutions than the standard four" of this article's opening is not an embarrassment: the eight operations are the four fundamental automorphisms *and* their composites with charge conjugation.

**Charge conjugation is the pseudoautomorphism.** $C$ is the one operation that is not a fundamental automorphism. In the classification it is the map
$$
A\;\mapsto\;A^{\mathrm{c}}=\Pi\,A^{*}\,\Pi^{-1},
$$
the **complex conjugation** of the algebra element followed by the inner automorphism by a matrix $\Pi$. (The symbol ${}^{\mathrm{c}}$ is local to this section; it is not the coefficient conjugation $\bar{\cdot}$ of the algebra.) Here $\Pi$ is a product of Clifford generators and is determined only up to a scalar; it is not a scalar, so the inner automorphism is not the identity on the generators. On the module the representative is the odd cell $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, and the generator relation is not uniform: $\eta_C^{-1}G_\mu\,\eta_C=-G_\mu^{*}$, which reads $-,-,+,-$ for $\mu=0,1,2,3$ because the module conjugation negates $G_2$. The conjugation together with this non-scalar inner automorphism is exactly why the map is a *pseudo*automorphism rather than an automorphism of $\mathrm{Cl}_{n,m}$. Theorem 1 of the source fixes the form of $\Pi$ by the division ring of the real subalgebra: for a real division ring $K\cong\mathbb{R}$ it is proportional to the unit matrix, and for a quaternionic one $K\cong\mathbb{H}$ it is a product of generators with $\Pi\bar{\Pi}=\pm I$. The matrix $\Pi$ is the charge-conjugation matrix, and it is at the algebra level the object that the module computation above fixes to $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ up to the free phase; the classification is also where that free phase comes from, since $\Pi$ is determined only up to a scalar. The twisted character of $C$ — that it is not one of the algebra's three untwisted involutions — is the classification's form of this article's operational finding that $C$'s internal factor is **odd** and outside $\mathbb{B}$.

**The level distinction, kept explicit.** The classification is a statement about $\mathrm{Cl}_{n,m}$ and its intrinsic maps; the operations of this article are maps of the Dirac **module**, defined by internal cells and verified on the free equation. Passing from one to the other is a matter of the representation theory — of which inner element of the Clifford algebra implements a given automorphism on the spinor module — and this article does not carry it out. The correspondence above is therefore recorded as **transcribed**, from the Clifford treatment of the discrete symmetries, and it is stated as a correspondence of classifications rather than as a derivation of $\eta_C$ or $\eta_T$ from the algebra's involutions. What it adds to the explicit computation is structural: the eight operations are the fundamental automorphisms and their charge-conjugation twists, and the algebra's three conjugations $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ are the three non-trivial fundamental maps.

## Relation to the Companion Articles

- **The S-matrix.** The companion raises as an open question the biquaternion realization of the anti-unitary discrete symmetries, and locates it in "the planned companions on CPT and on the discrete symmetries". This article answers part of that: it gives the anti-linear field map $T$ and the composition $CPT$ on the free spinor-module field, with the anti-linearity identified with the algebra's $\bar{\cdot}$ and the induced operator of $T$ anti-unitary. It does not give the action on the S-matrix.
- **Spin–statistics.** That article establishes that the spinor module is the carrier of the double-valued representation and that the fermionic bracket is imposed; the discrete operations here act on the same module and are insensitive to the bracket. The anti-unitarity of $T$ is the one place where the complex structure of the module enters the discrete symmetries directly.
- **Chiral fermions.** That article's real structure — the conjugation relating $S$ to $\bar S$ — is exactly the $\bar{\cdot}$ that supplies the anti-linear part of $C$ and $T$; the framework's mass term, now the linear chiral pair, is not built on it. The present article adds that $C$ and $P$ flip chirality, $T$ preserves it, and $CPT$ preserves it: the discrete operations do not mix the chirality question with the sector question, and the two decompositions remain distinct.
- **Canonical quantization.** The mode expansion there gives the operator-level interpretation of $C$: because $\eta_Cu^{*}$ is a negative-frequency amplitude, $C$ exchanges $a^{\mathrm{fop}}$ and $b^{\mathrm{fop}}$ and reverses the normal-ordered charge. This is the operator form of the classical statement.
- **The electron.** That article's charge conjugation, generated by the cell $R_{\vec e_x}^{\mathrm{pau}}$ on $\bar\psi^{T}$, is the transposed realization of the same operation; the untransposed realization used here carries $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, and the two are related by the change of realization described in the charge-conjugation section, with the free phase that the condition leaves. Its observation that the energy-sign projector is an odd Clifford element with no representative in $\mathbb{B}$ is the same odd/even distinction that governs the table above.
- **Charge conjugation and the division ring.** That companion develops the one feature of the pseudoautomorphism that the present article leaves untouched: the dependence of its square, and of its very character, on the division ring of the underlying real Clifford algebra. It is the reason charge conjugation can be trivial on a class of particles — the *truly neutral* ones — and it refines the eight-element group above by a representation-theoretic trichotomy.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The three operations $C[\psi]=\eta_C\psi^{*}$ with $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $P[\psi]=\eta_P\psi(t',-\vec x)$ with $\eta_P=G_0=iR_{\vec e_x}^{\mathrm{pau}}$, and $T[\psi]=\eta_T\psi^{*}(-t',\vec x)$ with $\eta_T=-L_{\vec e_y}^{\mathrm{pau}}$, each preserve the free Dirac equation, verified on the differential equation for three on-shell momenta and on a superposition of both frequency branches.
- The field map $T$ is anti-linear, $T[i\psi]=-i\,T[\psi]$, and the operator it induces is anti-unitary; $C$ is anti-linear with a unitary induced operator; $P$ is linear.
- $C$ and $P$ anticommute with $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}$ and exchange the chiral halves; $T$ commutes with $\Gamma$; $CPT$ preserves chirality.
- $C$ exchanges the frequency branches, hence the particle and antiparticle modes.
- Of the internal factors, $\eta_T=-L_{\vec e_y}^{\mathrm{pau}}$ is even and belongs to $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$, while $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and $\eta_P=G_0$ are odd and do not belong to $\mathbb{B}$.
- The algebra's conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ preserve both sectors; ${}^{*}$ is $+1$ on $\mathbb{M}_+$ and $-1$ on $\mathbb{M}_-$; the sector swap is the central multiplication by $i$. No discrete operation is a sector swap.
- The composition $\Theta=C\circ P\circ T$ acts as $\eta_{CPT}\psi(-x)$ with $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$, verified as a composition; in the aligned convention $\eta_{CPT}=\Gamma=i\omega$, with $\omega=-R_{\vec e_z}^{\mathrm{pau}}$ the volume element identified with the scalar imaginary. The naive product differs from the true composition once the phases are not fixed by the conjugation.
- The algebra's three conjugations are the three non-trivial fundamental automorphisms of its Clifford form: $\bar{\cdot}$ is the grade involution, ${}^{*}$ the reversion, and ${}^{\natural}$ their composite, the Clifford conjugation. This is the companion *Clifford Algebra Representation*'s computation, not a new claim, and it is the one point where the Clifford classification and the algebra meet without transcription.

**Transcribed, not derived.**

- The CPT theorem itself, and the hypotheses (locality, Hermiticity, Lorentz invariance, positivity, spin–statistics) that prove it.
- The internal factors and phases of $C$ and $T$, which are the standard Clifford-algebra objects; the free-field computation is the standard one expressed in the framework's module and notation.
- The intertwiners, which are the standard relations $\eta_C\,G_\mu^{*}\eta_C^{-1}=-G_\mu$ on the generator cells and their analogues.
- The **Clifford classification** of the operations: $P$ as the grade involution, $T$ as the reversion, $PT$ as the Clifford conjugation, $C$ as the charge-conjugation pseudoautomorphism, and the group $\{1,P,T,PT,C,CP,CT,CPT\}\cong\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ that they generate. The classification is a statement about the intrinsic maps of $\mathrm{Cl}_{n,m}$; the passage from those maps to the module intertwiners $\eta_P,\eta_T$ is representation theory that this article does not carry out.

**Gap, left visible.**

- No $\mathbb{B}$-intrinsic form of $C$ and $P$. Because their internal factors are odd, they cannot be inner operations of $\mathbb{B}$; whether the framework can realize them on an enlarged structure, or only on the Clifford algebra or the module, is not built.
- No action on the S-matrix, and no treatment of $CP$ violation.
- No derivation of CPT from the algebra. Whether locality and positivity are expressible as properties of $\mathbb{B}$ in a way that yields the theorem is open.
- The massive case: the parent's mass term is the linear chiral pair, whose spinor representative is the massive Dirac equation that $C$, $P$ and $T$ were each verified to preserve; the open question is whether $C$ is a symmetry of the single-field equation built on the algebra's antilinear real structure $\flat$, the same Majorana-versus-Dirac interpretation as before.

## Open Questions

1. **Is there a $\mathbb{B}$-intrinsic $C$ and $P$?** Their internal factors are odd and outside $\mathbb{B}$. Does an enlargement of the algebra (a Clifford or module extension) carry them as inner operations, or are charge conjugation and parity irreducibly external to the biquaternion structure? This is the structural counterpart of the electron article's observation that the energy-sign projector has no representative in $\mathbb{B}$.

2. **Is $C$ a symmetry of the real structure's pairing?** The algebra's real structure $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$ is anti-linear, while the parent's mass term is the linear chiral pair, and $C$ preserves the massive spinor equation. Whether the separate single-field equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ built on the real structure is $C$-invariant, and whether that pairing is Majorana-type or a real-form Dirac mass, decide whether the framework's fermion number is conserved. The companion on the neutrino and Majorana fermions is the natural place.

3. **Can CPT be derived rather than transcribed?** The theorem follows from locality, Hermiticity, Lorentz invariance and positivity. Are any of these native to $\mathbb{B}$, or does the framework only host the notation? A derivation would be the framework's first genuine theorem of this kind.

4. **The phase of the charge-conjugation matrix and the grading.** The phase of $\eta_C$ is conventional, but $C$ and the fermion-parity element $(-1)^F$ both act on the field with a sign, and the two signs are related in the single-mode algebra. Is the phase of $\eta_C$ fixed by the requirement that $C$ commute with the grading, or is it free?

5. **Where would $CP$ violation live?** The free equation is $CP$-invariant. If the framework has a place for a complex phase in the mass or coupling structure — the Majorana question above is one candidate — does it admit the standard $CP$-violating invariants, and is there a biquaternion statement of them?

6. **Empirical contact.** The construction reproduces standard field theory. Any deviation would have to appear where the framework is used beyond transcription, for instance in the relation between the discrete operations and the mass term; none is visible at the level developed here.

7. **Does the Clifford classification derive the module maps?** The three non-trivial fundamental automorphisms of $\mathrm{Cl}_{n,m}$ are the algebra's three conjugations, and the classification assigns $P$, $T$ and $PT$ to them. On the spinor module the same operations are implemented by the internal cells $\eta_P=G_0$ and $\eta_T=G_1G_3=-L_{\vec e_y}^{\mathrm{pau}}$, of which only the second is even. Whether the module maps can be *read off* the automorphism classification — so that $\eta_P$ and $\eta_T$ are derived rather than matched — is the representation-theoretic step this article does not take. If it can be taken, the correspondences $P\leftrightarrow\star$, $T\leftrightarrow\sim$ become a derivation; if it cannot, the classification remains a structural companion rather than a source.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. This is the only section of the article that uses them; the bodies above and below are written in the cells. In this frame the generators are the same four cells, with the $i$ written out rather than carried in the name:
$$
\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$
Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell written $\Gamma$ above; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The dictionary to the cells of this article.** The generators are the cells named $G_\mu$ above,
$$
\gamma_0=G_0,\qquad \gamma_1=G_1,\qquad \gamma_2=G_2,\qquad \gamma_3=G_3,\qquad \gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}=\Gamma,
$$
and the composite entries are where $i^{2}=-1$ is spent, twice over:
$$
\gamma_1\gamma_3=(i)(i)\,L_{\vec e_x\vec e_z}^{\mathrm{pau}}R_{\vec e_y\vec e_y}^{\mathrm{pau}}=-L_{\vec e_x\vec e_z}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=+L_{\vec e_x\vec e_z}^{\mathrm{pau}}=L_{-\vec e_y}^{\mathrm{pau}}=-L_{\vec e_y}^{\mathrm{pau}}=\eta_T,
$$
$$
\gamma_2\gamma_3=(i)(i)\,L_{\vec e_y\vec e_z}^{\mathrm{pau}}R_{\vec e_y\vec e_y}^{\mathrm{pau}}=-L_{\vec e_y\vec e_z}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=+L_{\vec e_y\vec e_z}^{\mathrm{pau}}=L_{\vec e_x}^{\mathrm{pau}},
$$
$$
i\gamma_2=i\,(iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=\eta_C,\qquad
\gamma_0\gamma_1\gamma_2\gamma_3=-R_{\vec e_z}^{\mathrm{pau}}=\omega=-i\Gamma .
$$
Each reduction is a single cell with no $i$ left, and the mechanism is the same in all four: the two factors of $i$ multiply to $-1$, the factor $R_{\vec e_y\vec e_y}^{\mathrm{pau}}=R_{-e_t}^{\mathrm{pau}}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ contributes a second $-1$, and the two cancel, leaving the quaternion product of the two arguments. That is the rule that decides the parity of a product: a product of an even number of generators is real, a product of an odd number is purely imaginary, so an odd product such as $\gamma_1$ or $i\gamma_2$ needs its explicit $i$ and an even product such as $\gamma_1\gamma_3$ never has one. The mechanical rules are $L_aR_bL_cR_d=L_{ac}R_{db}$, $\vec e_j\vec e_k=\epsilon_{jkl}\vec e_l$ for $j\ne k$ and $\vec e_k^{2}=-e_t$, together with $L_{e_t}^{\mathrm{pau}}=R_{e_t}^{\mathrm{pau}}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ for the identity.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
The four contraction sums are frame statements, because the square of a cell depends on the frame. In the Euclidean frame, where every cell squares to $+I_4$, they are $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\delta\gamma_\beta\gamma_\alpha$. In the $\mathbb{M}_-$ frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.

## Summary

The biquaternion framework carries the three discrete operations on its spinor-module Dirac field, and they are written in cells throughout. Charge conjugation is $C[\psi]=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\psi^{*}$; parity is $P[\psi](x)=G_0\psi(t',-\vec x)$; time reversal is $T[\psi](x)=-L_{\vec e_y}^{\mathrm{pau}}\psi^{*}(-t',\vec x)$. Each was verified separately to preserve the free equation $(\mathbb{D}-m)\psi=0$, on the differential equation, for three on-shell momenta and on a superposition of both frequency branches. The field map of time reversal is anti-linear, $T[i\psi]=-i\,T[\psi]$, and its induced operator is anti-unitary; it conjugates the framework's scalar imaginary. Charge conjugation and parity anticommute with the chirality cell $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}$ and exchange the chiral halves; time reversal commutes with $\Gamma$; the composition preserves chirality.

The two Dirac equations are kept apart. The algebra equation is the one-sided chiral pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$, in which every derivative acts by left multiplication and chirality has no room to appear. The module equation is $(\mathbb{D}-m)\psi=0$, with $\mathbb{D}$ built from two-sided cells; the chirality is the pure right multiplication $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}$, which is what the two-sided operator theory adds. The discrete operations act on the module equation.

The operations are kept distinct from the algebra's own conjugations. The quaternion, complex and Hermitian conjugates all preserve both sectors $\mathbb{M}_-$ and $\mathbb{M}_+$, and the Hermitian conjugate defines them; the sector swap is multiplication by the central scalar imaginary $i$, which is not a conjugation. The transition between the two sectors is therefore not the particle–antiparticle or chiral-conjugate transition; the temptation to read it so is the trap the companion articles record, and it is refuted by the fixed-point definitions. Of the internal factors, only $\eta_T=-L_{\vec e_y}^{\mathrm{pau}}$ is even and belongs to the biquaternion algebra; $\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and $\eta_P=G_0$ are odd, so charge conjugation and parity are operations of the Clifford algebra and the module, not inner operations of $\mathbb{B}$.

The composition was checked as a composition. Because $C$ and $T$ are anti-linear, $\Theta=C\circ P\circ T$ has internal factor $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$, equal to $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}=i\omega$ in the convention used here, where $\omega=-R_{\vec e_z}^{\mathrm{pau}}$ is the volume element the framework identifies with the scalar imaginary. The composition is complex-linear, maps particles to antiparticles, and preserves chirality. What the framework establishes is that the free Dirac equation carries these operations and their composition, with the anti-linearity supplied by the algebra's complex conjugation in $C$ and $T$; what it transcribes is the CPT theorem. A free-field check is not the theorem, whose content is the survival of the composition under interactions, and the $\mathbb{B}$-intrinsic forms of $C$ and $P$ remain open.

The Clifford-algebra literature supplies a second interpretation of the same eight operations: they are the three non-trivial fundamental automorphisms of $\mathrm{Cl}_{n,m}$ — the grade involution, the reversion and their composite, the Clifford conjugation — together with their composites with the charge-conjugation pseudoautomorphism $A\mapsto\Pi A^{*}\Pi^{-1}$, and they generate $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$. The algebra's own conjugations $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ are exactly the three untwisted maps, while $C$ is the twisted one, which is the algebraic form of the article's finding that $C$ is not an inner operation of $\mathbb{B}$. That classification is transcribed, and the step from it to the module intertwiners is left open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_j \vec e_k=\epsilon_{jkl}\vec e_l$ $(j\ne k)$ |
| $i$ | Scalar imaginary, $i^2=-1$; the matrix realization gives $iI_2$ on the module, and the Clifford isomorphism $\mathbb{B}\to\mathrm{Cl}_{1,3}^{+}$ (a different map from $\mathsf{M}_2$) sends it to $\omega$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | Real-quaternion subspace; centre |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=({}^{\natural})^{\,*}$ | Quaternion, complex, and Hermitian conjugations |
| $\tilde{Q}^{\flat}=-\tilde{Q}^{*}$ | Anti-Hermitian conjugate; the algebra's real structure, $\mathbb{C}$-antilinear and order-reversing |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k,\ \mathsf{M}_2(i)=iI_2$ | Matrix realization, $\mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger}$ |
| $S=\mathbb{C}^2=(\tfrac12,0)$, $\bar{S}=(0,\tfrac12)$, $\Delta=S\oplus\bar{S}$ | Spinor module, conjugate, Dirac module |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k\,\vec e_k\partial/\partial Q_k$, $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | Biquaternionic gradient and d'Alembertian |
| $\tilde{\Psi}$, $\tilde{\Psi}^{\flat}$ | Biquaternion Dirac field and its anti-Hermitian conjugate |
| $\psi=(\psi_L,\psi_R)^{T}$ | Spinor-module representative; $(\mathbb{D}-m)\psi=0$ |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi=a\psi b$ | Two-sided cells; identity $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, inverse $L_{a^{-1}}R_{b^{-1}}$, product $L_{a}R_{b}L_{c}R_{d}=L_{ac}R_{db}$ |
| $G_0=iR_{\vec e_x}^{\mathrm{pau}}=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, $G_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | The four generator cells (written as the gammas in the Gamma section); $G_0^{2}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $G_k^{2}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, distinct ones anticommute (metric $g=\mathrm{diag}(+1,-1,-1,-1)$); $\mathbb{D}=iG_\mu\partial_\mu$ |
| $\mathbb{D}=-R_{\vec e_x}^{\mathrm{pau}}\partial_{t'}-\sum_kL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\partial_k$ | The Dirac operator on the module, in cells |
| $G_0E_{\vec p}-\sum_k G_kp_k$ | Plane-wave value of $\mathbb{D}$; $p\cdot x=E_{\vec p}t'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ |
| $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, $\omega=-R_{\vec e_z}^{\mathrm{pau}}=-i\Gamma$ | Chirality cell and volume element; $\Gamma^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$; $\eta_{CPT}=\Gamma=i\omega$ |
| $P_{L,R}=\tfrac12(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}\mp\Gamma)$ | Chiral projectors |
| $w^{(r)}(\vec p),v^{(r)}(\vec p)$ | Positive- and negative-frequency spinors (solutions article) |
| $C[\psi]=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\psi^{*}$ | Charge conjugation (anti-linear, odd, $\eta_C^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$) |
| $P[\psi]=G_0\psi(t',-\vec x)$ | Parity (linear, odd, $\eta_P^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$) |
| $T[\psi]=-L_{\vec e_y}^{\mathrm{pau}}\psi^{*}(-t',\vec x)$ | Time reversal (anti-linear field map, even, $\eta_T^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$) |
| $\Theta=C\circ P\circ T$ | CPT composition; $\Theta[\psi](x)=\eta_{CPT}\psi(-x)$ |
| $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$ | Internal factor of the composition; $=\Gamma$ in the aligned convention |
| $A^{\star}$, $A^{\sim}$, $A^{\mathrm{rev}}$ | Fundamental automorphisms of $\mathrm{Cl}_{n,m}$: grade involution, reversion, Clifford conjugation; on $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ they are $\bar{\cdot}$, ${}^{*}$, ${}^{\natural}$ |
| $\Pi$, $A\mapsto A^{\mathrm{c}}=\Pi A^{*}\Pi^{-1}$ | Charge-conjugation pseudoautomorphism; $\Pi$ is a product of generators, fixed only up to a scalar; $\eta_C^{-1}G_\mu\eta_C=-G_\mu^{*}$ |
| $\{1,P,T,PT,C,CP,CT,CPT\}\cong\mathbb{Z}_2^3$ | The group of the eight discrete operations |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the plain form on the informational sector |
## Further Reading

- G. Lüders and B. Zumino, "Connection between Spin and Statistics," *Physical Review* **110** (1958) 1450–1453, for the general proof of the CPT theorem in the axiomatic setting.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the Wightman-axiomatic treatment from which the theorem's hypotheses — locality, positivity, Lorentz invariance — are read.
- J. J. Sakurai, *Invariance Principles and Elementary Particles* (Princeton, 1964), for the classic operator treatment of the discrete symmetries and of CPT.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the CPT theorem in the Lagrangian setting and the role of the anti-unitary operations.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac-field implementations of $C$, $P$ and $T$ used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the plane-wave spinors, the charge-conjugation matrix and the mode exchange.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the even/odd structure of $\mathrm{Cl}_{1,3}$ and the volume element.
- P. K. Rashevskii, "The theory of spinors," *Uspekhi Matematicheskikh Nauk* **10** (1955) 3–110 (*American Mathematical Society Translations* (2) **6** (1957) 1–110), for the classification of the intrinsic order-two maps of a Clifford algebra — the grade involution, the reversion and the Clifford conjugation — that the section above reads as the discrete operations.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the assignment of the discrete operations to the fundamental automorphisms and the charge-conjugation pseudoautomorphism, and for the group structure $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$.
- Companion articles: *Charge Conjugation and the Division Ring*; [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Spin–Statistics Theorem in Biquaternionic Form](the-spin-statistics-theorem-in-biquaternionic-form.html); [The S-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html); [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html); *Clifford Algebra Representation*.
