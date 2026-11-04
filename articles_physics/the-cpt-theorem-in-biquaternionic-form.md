# __The CPT Theorem in Biquaternionic Form__

## Introduction

The **CPT theorem** is the statement that a relativistic quantum field theory on Minkowski space whose Lagrangian is local, Hermitian and Lorentz invariant is invariant under the composition of **charge conjugation** $C$, **parity** $P$ and **time reversal** $T$, taken in any order. Its force is that the composition survives when the factors do not: a theory may violate $C$, $P$ and $T$ separately, and even the product $CP$, while $CPT$ remains exact. The proof requires locality (fields commute or anticommute outside the light cone), the positivity of the inner product, and the spin–statistics connection, and it is one of the deepest general results of quantum field theory.

This article asks what the biquaternion framework supplies for the theorem. The framework carries **more involutions than the standard four**, and they are easy to conflate. Alongside $C$, $P$ and $T$ the algebra provides the **complex conjugate** $\bar{\cdot}$ (conjugation of the four coefficients), the **quaternion conjugate** ${}^{\natural}$, and the **Hermitian conjugate** ${}^{*}=({}^{\natural})^{\,*}$. Building $C$, $P$ and $T$ therefore requires more than writing three arrays: each must be separated from the algebra's own conjugations, with which it shares the operation of complex conjugation but not the operation's meaning. The known trap, recorded in the companion on the Klein–Gordon equation, is to read a conjugate pair through the two-sector split $\mathbb{M}_+/\mathbb{M}_-$ — the temptation to place a field and its conjugate one in each sector. It is a trap because *none* of the three conjugations exchanges the sectors; the sector swap is multiplication by the central scalar imaginary $i$, which is neither a conjugation nor anti-linear. That fact, and not the notation, is what forbids the identification.

The field is one element of the algebra, $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$, where the $L$ part is the $-1$ value of the chirality and the $R$ part the $+1$ value. Two equations act on it, and the article keeps them apart from the first line.

- **The one-sided equation.** The dynamics of the algebra is the chiral pair
  $$
  \tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\qquad
  \tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R,
  $$
  two first-order equations on the two parts, with massless limit $\tilde{\nabla}\tilde{\Psi}_R=0$ and $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=0$. Each gradient acts by **left** multiplication, so the pair is a one-sided equation in the algebra. Chirality is not an operator of this one-sided form: both gradients multiply on the left, and the chirality is a right multiplication, so the pair has no place to write it.
- **The two-sided equation.** The same element carries the single equation $(\mathbb{D}-m)\tilde\Psi=0$, where $\mathbb{D}$ is built from **two-sided** cells — a left multiplication for the gradient and a right multiplication for the chirality. This is the equation the three operations are defined on and checked against.

The passage between the two is what the two-sided operator theory supplies, and it is the reason the two-sided equation can carry a chirality while the one-sided pair cannot. We build each of $C$, $P$ and $T$ explicitly, verify each one separately against the free equation, and then check the composition $CPT$ explicitly rather than inferring it from the three factors. The composition check is not redundant, for a reason that is easy to miss: $C$ and $T$ are **anti-linear**, so the internal factor of the product is $\eta_C\eta_P^*\eta_T^*$, not $\eta_C\eta_P\eta_T$, and the two differ whenever the phases are not fixed by the conjugation.

We work in the **cell frame** of the canonical-quantization and spin–statistics articles. With $L_a\tilde\Psi=a\tilde\Psi$, $R_b\tilde\Psi=\tilde\Psi b$ and the two-sided cell $L_aR_b$, so that $L_aR_b\tilde\Psi=a\tilde\Psi b$, the four generator cells of the field are
$$
G_0=iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
G_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
G_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
G_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$
Each carries one factor of $i$, and naming them $G_\mu$ is what keeps that factor from being written out again in every product. The factor is structural: it is what gives the four generators the metric $g$ rather than its negative, since without it the first would square to $-1$ and the other three to $+1$.
$$
G_0^{2}=1,\qquad G_1^{2}=G_2^{2}=G_3^{2}=-1,\qquad G_\mu G_\nu=-G_\nu G_\mu\quad(\mu\ne\nu),
$$
which are the cell relations of the sign vector $\varepsilon=(1,-1,-1,-1)$. A product of two generators is where $i^{2}=-1$ is spent: the two factors of $i$ give $-1$, and that sign combines with $\vec e_k^{2}=-e_t$ and with $\vec e_j\vec e_k=\pm\vec e_l$ so that the product is again a single cell, this time with no $i$ in it. The three such products are the three spatial units,
$$
G_2G_3=L_{\vec e_x}^{\mathrm{axf}},\qquad G_3G_1=L_{\vec e_y}^{\mathrm{axf}},\qquad G_1G_2=L_{\vec e_z}^{\mathrm{axf}},
$$
and the product of all four is the volume element, $G_0G_1G_2G_3=-R_{\vec e_z}^{\mathrm{axf}}$. This is used repeatedly below: the generators themselves are not written out again, only $G_\mu$ and the plain cells $L_aR_b$ that the internal factors need. The closing comparison section is the only place this article writes the other notation, and it uses it for exactly these four cells.

The chirality cell and the volume element are
$$
\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},\qquad
\omega=-R_{\vec e_z}^{\mathrm{axf}},\qquad
\Gamma=i\omega,\qquad
\Gamma^2=1.
$$
and $\Gamma$ anticommutes with each $G_\mu$. The framework identifies $\omega$ with the scalar imaginary: the identification is a reading of the conventions, and what it buys here is one line about the two parts. Since $\omega=-i\Gamma$, the volume element multiplies $\tilde\Psi_L$ by $i$ and $\tilde\Psi_R$ by $-i$, and the chirality cell takes the value $-1$ on the first part and $+1$ on the second. That is the whole of what the article needs about either cell. Every derivative in a cell display below is with respect to $x_\mu=(t',x,y,z)$; the $ict'$ normalization $Q_t=ict'$ is used only where it is named. We work in natural units $\hbar=c=1$ except in the mass-shell relation, and borrow the plane-wave amplitudes and the spin sums of the solutions article unchanged.

The division between what is established and what is only transcribed is kept explicit throughout.

- **Established, and recomputed below.** The three operations on the field are
  $$
  C[\tilde\Psi]=-\vec e_y\,\tilde\Psi^{J}\,\vec e_y,\qquad
  P[\tilde\Psi](t',\vec x)=i\,\tilde\Psi(t',-\vec x)\,\vec e_x,\qquad
  T[\tilde\Psi](t',\vec x)=-\vec e_y\,\tilde\Psi^{J}(-t',\vec x),
  $$
  with $\vec x=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$. The mark ${}^{J}$ denotes the **conjugation of the field**: $J$ is the anti-linear map this article's realization supplies, and $\tilde\Xi^{J}$ is $J$ applied to the element $\tilde\Xi$. It is fixed up to a scalar by its action on the four generator cells, where it keeps three of them and negates the second spatial one,
  $$
  G_0^{J}=G_0,\qquad G_1^{J}=G_1,\qquad G_2^{J}=-G_2,\qquad G_3^{J}=G_3 .
  $$
  $J$ is not one of the algebra's three conjugations, and no multiplication by an element realizes it; the paragraph on the realization in the section on charge conjugation returns to this. The three internal factors are
  $$
  \eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
  \eta_P=G_0=iR_{\vec e_x}^{\mathrm{axf}},\qquad
  \eta_T=-L_{\vec e_y}^{\mathrm{axf}},
  $$
  which square to $\eta_C^2=1$, $\eta_P^2=1$ and $\eta_T^2=-1$. Each operation maps every solution of the free equation $(\mathbb{D}-m)\tilde\Psi=0$ to a solution, verified separately on the differential equation, on three on-shell momenta and on a superposition of both frequency branches. The field map $T$ is anti-linear, $T[i\tilde\Psi]=-i\,T[\tilde\Psi]$, so it conjugates the scalar imaginary; the operator it induces on the mode algebra is anti-unitary. $C$ and $P$ anticommute with $\Gamma$ and exchange the two parts; $T$ commutes with $\Gamma$ and preserves them; hence $CPT$ preserves chirality. $C$ exchanges the two frequency branches, so at the operator level it exchanges the particle and antiparticle modes. Of the internal factors, $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$ is a left multiplication by the element $-\vec e_y\in\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$; $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ multiplies on both sides and $\eta_P=iR_{\vec e_x}^{\mathrm{axf}}$ on the right, so neither is a left multiplication by an element of $\mathbb{B}$. The composition $\Theta=C\circ P\circ T$ acts as $\Theta[\tilde\Psi](x)=\eta_{CPT}\,\tilde\Psi(-x)$ with $\eta_{CPT}=\eta_C\eta_P^{J}\eta_T^{J}$; in the phase convention above,
  $$
  \eta_{CPT}=\eta_C\eta_P\eta_T=\Gamma=i\omega .
  $$
- **Transcribed, not derived.** The CPT theorem itself, together with the hypotheses that prove it: locality, Hermiticity of the Lagrangian, Lorentz invariance, positivity and spin–statistics. The computation below exhibits the composition as a symmetry of *one* free equation; it does not show that the composition survives interactions, which is the content of the theorem. Nothing here derives CPT from the biquaternion algebra. Also transcribed is the classification of the eight operations as the identity, the algebra's three conjugations and their composites with charge conjugation, which is recorded below as a second interpretation of the same eight operations and as the source of their $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ group structure.
- **Gap, left visible.** The framework does not fix a $\mathbb{B}$-intrinsic form of $C$ and $P$: neither of their internal factors is a left multiplication by an element of $\mathbb{B}$, so they are operations of the cell algebra rather than inner operations of the biquaternion algebra. Whether they admit a $\mathbb{B}$-intrinsic realization is unbuilt. Separately, the parent's mass term is the linear chiral pair of the Dirac article, whose two-sided form is the massive Dirac equation verified above to be $C$-invariant; the algebra's anti-linear object is the real structure $\flat=-{}^{*}$, a separate Majorana-type pairing, and whether $C$ is a symmetry of the single-field equation built on $\flat$ is the open reading developed in the neutrino companion.

## The Discrete Operations and the Algebra

Three different structures are in play, and the article's first task is to keep them apart.

### The One-Sided Equation and the Two-Sided Equation

The two equations are the two levels of one dynamics, and the notation of each is closed.

**The one-sided equation.** The gradient $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$ acts by left multiplication, and its quaternion conjugate $\tilde{\nabla}^{\natural}$ squares with it to the scalar d'Alembertian, $\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}=\Box$. The chiral pair is the first-order dynamics of the algebra, and its two members are one-sided: no right multiplication appears in it, so no chirality operator appears either.

**The two-sided equation.** The two members of the pair are one operator on one element. In the cell frame the operator reads
$$
\mathbb{D}=-R_{\vec e_x}^{\mathrm{axf}}\,\partial/\partial t'-\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,\partial/\partial x_k ,
$$
and written as an action, for an element $\tilde\Psi$,
$$
\mathbb{D}\tilde\Psi=-\frac{\partial\tilde\Psi}{\partial t'}\,\vec e_x-\sum_k\vec e_k\,\frac{\partial\tilde\Psi}{\partial x_k}\,\vec e_y ,
$$
with $\mathbb{D}^{2}=-\Box$. The spatial terms multiply on both sides, the time term is a pure right multiplication, and the frame is completed by the chirality, itself a pure right multiplication, $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$. The four minus signs of the cell form are what the factors of $i$ inside the generators contribute, since $-R_{\vec e_x}^{\mathrm{axf}}=iG_0$ and $-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=iG_k$; written in the generators, the operator is the single contraction
$$
\mathbb{D}=i\,G_\mu\,\partial/\partial x_\mu=i\Bigl(G_0\,\partial/\partial t'+\sum_kG_k\,\partial/\partial x_k\Bigr),
$$
which has no metric sign anywhere because the metric is already in the generators, $G_0^{2}=1$ and $G_k^{2}=-1$. On the plane wave $e^{-ip\cdot x}$ with $p\cdot x=E_{\vec p}t'-\vec p\cdot\vec x$ the factors of $i$ cancel again, and the operator acts on the amplitude by
$$
A(\vec p)=G_0E_{\vec p}-\sum_k G_kp_k ,
$$
the amplitude that appears in the verification below.

The two-sided operator theory is what lets the two levels be written in one frame, and it is also what separates them. The cells $L_aR_b$ carry the left multiplication of the one-sided equation and the right multiplication of the chirality: the four generators are of that form, the chirality $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$ is a pure right multiplication, and the mass is the scalar $m$ times the identity. A one-sided equation has no room for a pure right multiplication, so chirality belongs to the two-sided equation; a two-sided cell can carry both. **The discrete operations below are operations on the two-sided equation, not on the one-sided pair.**

**Operators, not elements.** The sixteen products of the four generators span a real algebra of dimension sixteen, and the sixteen two-sided cells $L_{a}R_{b}$ span another of the same dimension. Both are sets of operators on the field, while the field is an element. The three spatial units appear among the cells as the pure left multiplications $L_{\vec e_k}$, and the volume element as $-R_{\vec e_z}$; the field's two parts appear in neither, because they are the two values of the chirality, which is a cell and not an entry of anything.

## The Three Operations Built Explicitly

Let $\tilde\Psi$ solve the free equation $(\mathbb{D}-m)\tilde\Psi=0$, with $\mathbb{D}$ the two-sided operator above. A discrete operation is a map $\tilde\Psi\mapsto\tilde\Psi_2$ whose output also solves the equation. We take the operations in the standard form: $C$ is local and anti-linear, $P$ is a spatial reflection and linear, $T$ is a time reflection and anti-linear. Each is defined by an internal cell $\eta$ fixed by the requirement that the transformed field satisfy the same equation, and the requirement determines $\eta$ up to a phase, which is a convention.

The three conditions are commutation conditions, because each internal cell is invertible. The generators are $G_\mu$, $\mu=0,1,2,3$, and $G_\mu^{J}$ is the conjugate of $G_\mu$ under the field's conjugation. For a field map of the form $\tilde\Psi\mapsto\eta\,\tilde\Psi^{J}(\Lambda x)$ the transformed field solves the equation precisely when
$$
\eta^{-1}G_\mu\,\eta=\pm\,G_\mu^{J}
$$
holds on each generator, the sign being fixed by the reflection of the argument and the conjugate present because $C$ and $T$ are anti-linear; for parity, which is linear, the same test reads $\eta^{-1}G_\mu\eta=\pm G_\mu$ with no conjugate. Since each $\eta$ squares to $\pm1$ and is therefore its own inverse up to sign, the identity reduces on each generator to a commutation or an anticommutation, which is an algebraic fact about the cells and does not depend on the realization. The conjugate signs are the ones the field's conjugation gives,
$$
G_0^{J}=G_0,\qquad G_1^{J}=G_1,\qquad G_3^{J}=G_3,\qquad G_2^{J}=-G_2,
$$
in the realization used here: three of the four generators are fixed and the second spatial one is negated.

### Charge conjugation

Define
$$
C[\tilde\Psi]=\eta_C\,\tilde\Psi^{J}=-\vec e_y\,\tilde\Psi^{J}\,\vec e_y,\qquad \eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$
The equation is complex-conjugated, so the condition on the generators is $\eta_C^{-1}G_\mu\eta_C=-G_\mu^{J}$. It holds because $\eta_C$ **anticommutes** with the three generators the conjugation fixes and **commutes** with the one it negates:
$$
\eta_C^{-1}G_0\,\eta_C=-G_0,\qquad
\eta_C^{-1}G_1\,\eta_C=-G_1,\qquad
\eta_C^{-1}G_2\,\eta_C=+G_2,\qquad
\eta_C^{-1}G_3\,\eta_C=-G_3 .
$$
Because $\tilde\Psi^{J}$ enters, $C$ is anti-linear. The internal factor carries a right multiplication by $\vec e_y$, which anticommutes with the right multiplication by $\vec e_z$ that $\Gamma$ carries: charge conjugation flips chirality.

**The representative depends on the realization.** The condition above fixes $\eta_C$ only inside a realization of the generators, meaning a choice of the conjugation that $\tilde\Psi^{J}$ denotes. This article's realization is the cell frame, where the conjugation is the anti-linear map that carries $\tilde\Psi_L$ onto the $R$ part. The same cells read against the **coefficient conjugation** of the algebra give a different answer: every generator $iL_{a}R_{b}$ is purely imaginary, so that conjugation negates all four, the condition reduces to a commutation requirement, and *every* nonzero scalar satisfies it; the involution condition $\eta_C^{2}=1$ then narrows the scalar to $\pm1$. Neither formula may be carried across the change of conjugation: $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ conjugates through $\tilde\Psi^{J}$, and the two conjugations do not agree on which cells they fix. Writing $-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for $\eta_C$ is right; reading that cell against the coefficient conjugation instead of the field's conjugation is the error this paragraph exists to prevent.

### Parity

Define
$$
P[\tilde\Psi](t',\vec x)=\eta_P\,\tilde\Psi(t',-\vec x)=i\,\tilde\Psi(t',-\vec x)\,\vec e_x,\qquad \eta_P=G_0=iR_{\vec e_x}^{\mathrm{axf}}.
$$
Only the spatial derivatives change sign, and the field is not conjugated, so the condition is $\eta_P^{-1}G_0\eta_P=G_0$ and $\eta_P^{-1}G_k\eta_P=-G_k$ for the three spatial generators. It holds because $\eta_P$ **commutes** with the time generator and **anticommutes** with each spatial one:
$$
\eta_P^{-1}G_0\,\eta_P=G_0,\qquad
\eta_P^{-1}G_k\,\eta_P=-G_k\quad(k=1,2,3).
$$
Parity is linear, and since $\eta_P$ is a right multiplication it anticommutes with $\Gamma$: parity flips chirality.

### Time reversal

Define
$$
T[\tilde\Psi](t',\vec x)=\eta_T\,\tilde\Psi^{J}(-t',\vec x)=-\vec e_y\,\tilde\Psi^{J}(-t',\vec x),\qquad \eta_T=-L_{\vec e_y}^{\mathrm{axf}}=G_1G_3.
$$
The time derivative changes sign, the spatial derivatives do not, and the field is conjugated, so the condition is $\eta_T^{-1}G_0\eta_T=G_0^{J}$ and $\eta_T^{-1}G_k\eta_T=-G_k^{J}$. It holds because $\eta_T$ **commutes** with the time generator and with the second spatial one, and **anticommutes** with the first and third:
$$
\eta_T^{-1}G_0\,\eta_T=G_0,\qquad
\eta_T^{-1}G_2\,\eta_T=G_2,\qquad
\eta_T^{-1}G_1\,\eta_T=-G_1,\qquad
\eta_T^{-1}G_3\,\eta_T=-G_3 .
$$
Since $\eta_T$ is a left multiplication, it commutes with $\Gamma$: time reversal preserves chirality. Note that $\eta_T^{2}=-1$, so the internal factor is a complex structure on the field; only the operation is of order two up to the free phase.

### $T$ is anti-linear

The conjugation in $T$ is not a calculational convenience; it is what makes the field map anti-linear, the classical counterpart of the anti-unitary operator. With $i$ the scalar imaginary,
$$
T[i\tilde\Psi]=\eta_T(i\tilde\Psi)^{J}=\eta_T(-i)\tilde\Psi^{J}=-i\,\eta_T\tilde\Psi^{J}=-i\,T[\tilde\Psi].
$$
Both $C$ and $T$ are anti-linear, and both conjugate the scalar imaginary. The difference between them appears when the field map is promoted to an operator on the mode algebra: the operator induced by $T$ is anti-unitary, while the operator induced by $C$ is unitary. The reason is that $T$ reverses the sign of the evolution phase $e^{-iHt}$, and the conjugation is what turns the reversed evolution into a symmetry; $C$ only exchanges the particle and antiparticle labels at fixed energy, so its induced operator is linear. This article constructs the field maps, so it records the anti-linearity of both and leaves the mode operators aside. The framework's single scalar imaginary $i$ — the same $i$ that appears in the $ict'$ gradient and in the volume element $\omega$ — is exactly what the conjugation negates. A time reversal written without the conjugation (as $T:\tilde\Psi\mapsto\eta_T\tilde\Psi(-t',\vec x)$) is a different, linear map, and is *not* a symmetry of the Dirac equation.

The three operations are collected below. The last entry of each row records the chirality action that follows from the internal cell.

| Operation | Action on $\tilde\Psi$ | Internal cell | Linear? | Chirality |
|---|---|---|---|---|
| $C$ | $-\vec e_y\,\tilde\Psi^{J}\,\vec e_y$ | $-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | anti-linear | flips |
| $P$ | $i\,\tilde\Psi(t',-\vec x)\,\vec e_x$ | $G_0$ | linear | flips |
| $T$ | $-\vec e_y\,\tilde\Psi^{J}(-t',\vec x)$ | $-L_{\vec e_y}^{\mathrm{axf}}$ | anti-linear | preserves |

Two remarks on conventions. First, the phases of $\eta_C$ and $\eta_T$ are not fixed by the requirement that the equation be preserved; only the commutation conditions are, and they fix the internal factor only up to an arbitrary nonzero complex multiple. Second, the individual phases are not observable; what is observable is the composition, and changing a phase changes the internal factor of the composition, which is why the composition must be checked independently (next section).

## Each Operation Preserves the Free Equation

The verification was carried out on the differential equation itself, not only on a momentum-space identity, and on cases other than the one that suggested the definitions. The working field was the general solution
$$
\tilde\Psi=\bigl(A(\vec p)+m\bigr)\chi\,e^{-ip\cdot x}+\bigl(A(\vec p)-m\bigr)\chi_2\,e^{+ip\cdot x},
$$
with
$$
A(\vec p)=G_0E_{\vec p}-\sum_k G_kp_k,\qquad
p\cdot x=E_{\vec p}t'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),\qquad E_{\vec p}^2=\vec p^2+m^2,
$$
and $\chi,\chi_2$ arbitrary constant elements of $\mathbb{B}$. The first branch is positive-frequency and the second negative-frequency, and their sum is a general solution of the free equation by linearity. Substituting, conjugating and reflecting as the definitions require, the residual $(\mathbb{D}-m)$ acting on each transform was evaluated and found to vanish to machine precision, in every case below. The checks were run for the three parameter sets
$$
(m,\vec p)=(3,(1,2,2)),\qquad (5,(3,4,0)),\qquad (\tfrac{7}{2},(1,0,-2)),
$$
each with the corresponding $E_{\vec p}=+\sqrt{\vec p^2+m^2}$, and with both frequency branches present simultaneously. All three operations passed on all three cases.

The individual checks are worth a word each, because they test different parts of the structure.

- **$C$.** The commutation conditions above were verified as cell identities, and the transformed field was confirmed to solve the equation. The same computation identifies *which* solution the transform produces. On shell $A(\vec p)^2=E_{\vec p}^2-\vec p^2=m^2$, so the two factors in the decomposition satisfy $\bigl(A(\vec p)\mp m\bigr)\bigl(A(\vec p)\pm m\bigr)=0$. Conjugation by $\eta_C$ sends $A(\vec p)^{J}$ to $-A(\vec p)$, because it sends each generator to minus its conjugate; hence
  $$
  \eta_C\,w^{J}=\eta_C\bigl(A(\vec p)^{J}+m\bigr)\chi^{J}=\bigl(-A(\vec p)+m\bigr)\eta_C\chi^{J},
  $$
  which is annihilated by $A(\vec p)+m$: the transform is an amplitude of the **other branch**. So $C$ exchanges the two branches; in the mode expansion it exchanges the particle operator $a^{\mathrm{fop}}$ with the antiparticle operator $b^{\mathrm{fop}}$, which is the operator-level statement that the conserved charge reverses sign. This was checked on the same three cases.
- **$P$.** The commutation with the time generator and the anticommutation with the three spatial ones were verified, and the reflected field was confirmed to solve the equation. The transform keeps the positive-frequency branch positive-frequency and reverses the momentum, $\vec p\mapsto-\vec p$.
- **$T$.** The four commutation conditions were verified, and the conjugated-reflected field was confirmed to solve the equation. Because $T$ is anti-linear, the check on the superposition is the sharpest one: a linear map that ignored the conjugation would send the negative-frequency branch to the wrong sign.

Two negative results belong here, to prevent a future pass from claiming more than was checked.

- The verification is of the **free** equation. Nothing was checked for a field with a local interaction, and no claim is made there. The reason the free check cannot be promoted is stated at the end of this article: the CPT theorem is precisely the statement that the composition survives interactions when the factors do not, and a free-field identity contains no information about that.
- The operation $T$ was *not* defined as the linear map $\tilde\Psi\mapsto\eta_T\tilde\Psi(-t',\vec x)$ that is sometimes written. That map does not preserve the equation; the check was performed with the conjugation present.

## The Algebra's Conjugations Are Not the Discrete Operations

The temptation that the trap names is to identify one of the operations $C$, $P$, $T$ with one of the algebra's conjugations, or to read the particle–antiparticle pair as the sector pair. Three independent facts close the identification.

**First, the conjugations preserve both sectors.** For a general element $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, membership in $\mathbb{M}_-$ means $Q_t$ purely imaginary and $Q_x,Q_y,Q_z$ real, and membership in $\mathbb{M}_+$ means $Q_t$ real and $Q_x,Q_y,Q_z$ purely imaginary. Each of ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ maps either condition to itself: conjugation negates the scalar or the vector coefficients but does not interchange the two patterns. The Hermitian conjugate is the identity on $\mathbb{M}_+$ and minus the identity on $\mathbb{M}_-$, so it *defines* the sectors rather than exchanging them. The map that interchanges them is $i\,\mathbb{M}_\pm=\mathbb{M}_\mp$, and $i$ is central, hence not a conjugation and not anti-linear. A particle–antiparticle or chiral-conjugate pair therefore cannot be placed one member in each sector.

**Second, the sector split and the chirality split are different decompositions of one object.** The sector split is a condition on the coefficients, the sign of ${}^{*}$ read on each slot. The chirality split is the two values of $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$: $\tilde\Psi_L$ is the $-1$ value and $\tilde\Psi_R$ the $+1$ value, and the cell that produces them multiplies on the right. No coefficient condition produces them, and no conjugation produces the split: a map of the algebra reaches the coefficients, and the chirality is a cell. Recorded here only because a reader who has just seen $C$ and $P$ exchange the two parts might try to read that exchange as a sector exchange; it is not one.

**Third, only $T$'s internal factor is a left multiplication by an element.** $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$ is left multiplication by $-\vec e_y$, an element of $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$, so the operation is carried by the algebra's own left action. $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ multiplies on both sides, and $\eta_P=iR_{\vec e_x}^{\mathrm{axf}}$ multiplies on the right; neither equals $L_a$ for any element $a$ of $\mathbb{B}$, so neither operation is a left multiplication, and the algebra's left action does not contain them. This is the sharp form of the framework's difficulty with the discrete operations: the algebra contains the operation that preserves chirality ($T$) and does not contain those that exchange it ($C$ and $P$). The electroweakly relevant fact that $C$ and $P$ are precisely the operations Nature violates separately, while their product with $T$ is the one that survives, is not explained by this structure; it is the theorem's content, and it is imported.

The anti-linear part of $C$ and of $T$ is exactly the algebra's complex conjugation $\bar{\cdot}$, read on the coefficients. That is the same real-structure operation that relates the two parts of the field and that distinguishes them inside the algebra, and it is what supplies the anti-linear part of the discrete operations. It is *not* the mass. The parent's mass term is the linear chiral pair of the Dirac article, and the algebra's anti-linear real structure $\flat=-{}^{*}$ is a separate, order-reversing conjugation whose pairing is a Majorana-type coupling. The discrete operations are symmetries of the kinetic equation; the real structure is a dynamical pairing.

## The Composition CPT, Checked as a Composition

Compose the three operations by applying $T$ first, then $P$, then $C$, and write $\Theta=C\circ P\circ T$. Because $C$ and $T$ are anti-linear, the composition must be evaluated as a composition, not by multiplying the three internal factors. Applied to a field $\tilde\Psi$,
$$
\tilde\Psi
\xrightarrow{\;T\;}\eta_T\,\tilde\Psi^{J}(-t',\vec x)
\xrightarrow{\;P\;}\eta_P\eta_T\,\tilde\Psi^{J}(-t',-\vec x)
\xrightarrow{\;C\;}\eta_C(\eta_P\eta_T)^{J}\tilde\Psi(-t',-\vec x),
$$
so that
$$
\boxed{\;\Theta[\tilde\Psi](x)=\eta_{CPT}\,\tilde\Psi(-x),\qquad
\eta_{CPT}=\eta_C\,\eta_P^{J}\,\eta_T^{J}\;}.
$$
The internal factor is built from the **conjugates** of $\eta_P$ and $\eta_T$, written $\eta^{J}=J\eta J^{-1}$ for a cell, which is the bookkeeping that a naive product $\eta_C\eta_P\eta_T$ would miss. In the convention of this article, $\eta_P=G_0$ and $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$ are cells that the field's conjugation fixes, so $\eta_P^{J}=\eta_P$ and $\eta_T^{J}=\eta_T$, and
$$
\boxed{\;\eta_{CPT}=\eta_C\eta_P\eta_T=(-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})\,G_0\,(-L_{\vec e_y}^{\mathrm{axf}})=\Gamma\;}.
$$
The agreement with the naive product in *this* convention is an accident of internal factors that the conjugation fixes, and should not be taken as general. If, for example, the phase convention $\eta_T'=i\eta_T$ is used — equally admissible, since the equation-preservation condition leaves the phase of the internal factor free — then the true composition has $\eta_{CPT}=\eta_C\eta_P^{J}(\eta_T')^{J}=-i\Gamma=\omega$, while the naive product gives $i\Gamma=-\omega$. The two differ by a sign. The operation $T$ and the composition were re-verified in that convention as well, and both still map solutions to solutions; the point is that the internal factor is a convention-dependent phase and can only be read off from the composition itself. This is the concrete sense in which verifying $C$, $P$, $T$ individually and multiplying is not the same as verifying $CPT$.

The composition has the following verified properties.

- **It is a symmetry of the free equation.** $\Theta[\tilde\Psi]$ solves $(\mathbb{D}-m)\tilde\Psi=0$ whenever $\tilde\Psi$ does. This was checked on all three parameter sets and with both frequency branches present.
- **It is complex-linear.** $\Theta[i\tilde\Psi]=+i\,\Theta[\tilde\Psi]$: the two anti-linear factors $C$ and $T$ combine into a linear map on the field, since $\Theta[\tilde\Psi](x)=\eta_{CPT}\tilde\Psi(-x)$ carries no conjugation. (The standard $CPT$ *operator* on the mode algebra is anti-unitary; that operator is not constructed here, and it is the field map that this article defines.)
- **It reverses both the spacetime argument and the charge.** The argument is $-x$, and because $C$ exchanges the frequency branches, a particle is mapped to an antiparticle.
- **It preserves chirality.** $C$ and $P$ each anticommute with $\Gamma$ and $T$ commutes with it; the composition anticommutes twice. Equivalently, $\eta_{CPT}=\Gamma$ commutes with $\Gamma$.
- **Its internal factor is a phase times the volume element, and the chirality cell in this convention.** The volume element $\omega=-R_{\vec e_z}^{\mathrm{axf}}=-i\Gamma$ is the element the framework identifies with the scalar imaginary $i$: it multiplies $\tilde\Psi_L$ by $i$ and $\tilde\Psi_R$ by $-i$, which is what the scalar imaginary does on the two parts. In the convention above the internal factor is $\eta_{CPT}=\Gamma=i\omega$, the chirality cell itself. The factor is fixed only up to the free phases of $\eta_C$ and $\eta_T$; its identification with the volume element is the algebra statement, and its action as the chirality cell is the statement about the two parts.

**What this does and does not establish.** It establishes that the free biquaternion Dirac equation carries three discrete operations whose composition is a symmetry, that the composition's internal factor is a phase times the volume element (the chirality cell in the convention above), and that the anti-linearity resides in the factors $C$ and $T$ alone, where it is the algebra's complex conjugation $\bar{\cdot}$; the parent's mass term is linear, so the discrete anti-linearity is not shared with it.

It does **not** establish the CPT theorem. A free equation is a special case in which $C$, $P$ and $T$ are separately symmetries, so the composition is a symmetry for the trivial reason. The theorem's content is that $CPT$ remains a symmetry when $C$, $P$ and $T$ do not, and that statement rests on locality, Hermiticity, Lorentz invariance and spin–statistics, none of which is derived here. The correct summary is that the framework *exhibits* CPT on the free field and *transcribes* the theorem.

## The Group of the Eight Operations

A second reading of the same eight operations comes from the classification of the order-two maps of the algebra, and it is recorded beside the construction above because it supplies the one thing that construction does not: a reason the operations close into a group, and a reason that group is the eight-element $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$.

**The three conjugations of the algebra are order-two maps that commute.** Each of $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ is its own inverse, and any two of them commute, so with the identity they form a $\mathbb{Z}_2\times\mathbb{Z}_2$; the Hermitian conjugate is the composite of the other two, $\natural=\bar{\cdot}\circ{}^{*}$. This is a computation on the coefficients, and it is the whole of the algebra's supply of involutions: there are exactly three, and no fourth.

**The discrete operations are those four maps and their composites with $C$.** Read on the field, the eight products $\{1,P,T,PT,C,CP,CT,CPT\}$ close on themselves, each factor is of order two up to the free phase that the internal cell carries, and the eight form
$$
\boxed{\;\{1,\,P,\,T,\,PT,\,C,\,CP,\,CT,\,CPT\}\;\cong\;\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2\;}.
$$
This is the group-theoretic fact behind the standard statement that the discrete operations form an eight-element group. It is stated as a classification and not derived here: the products close because each of the three operations is an involution on the field, and the algebra supplies no further involution to enlarge the set.

**$C$ is not one of the three.** The one operation of the eight that is not built from the algebra's conjugations alone is charge conjugation: its internal factor multiplies on both sides by units drawn from the frame, so it is a cell and not a coefficient map, and it therefore does not appear in the $\mathbb{Z}_2\times\mathbb{Z}_2$ above. That is the classification's form of this article's operational finding, that $\eta_C$ is not a left multiplication by an element and $C$ is not an inner operation of the algebra.

**The level distinction, kept explicit.** The classification is a statement about the maps of the algebra; the operations of this article are maps of the field, defined by internal cells and verified on the free equation. Passing from one to the other is a matter of the representation theory — of which cell implements a given map of the algebra on the field — and this article does not carry it out. The correspondence above is therefore recorded as **transcribed**, and it is stated as a correspondence of classifications rather than as a derivation of $\eta_C$ or $\eta_T$ from the algebra's involutions. What it adds to the explicit computation is structural: the eight operations are the identity, the three conjugations and their charge-conjugation twists, so the "more involutions than the standard four" of this article's opening is not an embarrassment but a count.

## Relation to the Companion Articles

- **The S-matrix.** The companion raises as an open question the biquaternion realization of the anti-unitary discrete symmetries, and locates it in "the planned companions on CPT and on the discrete symmetries". This article answers part of that: it gives the anti-linear field map $T$ and the composition $CPT$ on the free field, with the anti-linearity identified with the algebra's $\bar{\cdot}$ and the induced operator of $T$ anti-unitary. It does not give the action on the S-matrix.
- **Spin–statistics.** That article establishes that the double-valued representation is carried by the field's two parts and that the fermionic bracket is imposed; the discrete operations here act on the same field and are insensitive to the bracket. The anti-unitarity of $T$ is the one place where the complex structure of the field enters the discrete symmetries directly.
- **Chiral fermions.** That article's real structure — the conjugation relating the two parts — is exactly the $\bar{\cdot}$ that supplies the anti-linear part of $C$ and $T$; the framework's mass term, now the linear chiral pair, is not built on it. The present article adds that $C$ and $P$ flip chirality, $T$ preserves it, and $CPT$ preserves it: the discrete operations do not mix the chirality question with the sector question, and the two decompositions remain distinct.
- **Canonical quantization.** The mode expansion there gives the operator-level interpretation of $C$: because $\eta_C\chi^{J}$ is an amplitude of the other branch, $C$ exchanges $a^{\mathrm{fop}}$ and $b^{\mathrm{fop}}$ and reverses the normal-ordered charge. This is the operator form of the classical statement.
- **The electron.** That article's charge conjugation, generated by the cell $R_{\vec e_x}^{\mathrm{axf}}$, is the transposed realization of the same operation; the untransposed realization used here carries $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, and the two are related by the change of realization described in the charge-conjugation section, with the free phase that the condition leaves. Its observation that the energy-sign cell is not a left multiplication by an element of $\mathbb{B}$ is the same distinction that governs the table above.
- **Charge conjugation and the division ring.** That companion develops the one feature of the operation that the present article leaves untouched: the dependence of its square, and of its very character, on the division ring of the algebra it is read in. It is the reason charge conjugation can be trivial on a class of particles — the *truly neutral* ones — and it refines the eight-element group above by a representation-theoretic trichotomy.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The three operations $C[\tilde\Psi]=\eta_C\tilde\Psi^{J}=-\vec e_y\tilde\Psi^{J}\vec e_y$ with $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $P[\tilde\Psi]=\eta_P\tilde\Psi(t',-\vec x)=i\tilde\Psi(t',-\vec x)\vec e_x$ with $\eta_P=G_0$, and $T[\tilde\Psi]=\eta_T\tilde\Psi^{J}(-t',\vec x)=-\vec e_y\tilde\Psi^{J}(-t',\vec x)$ with $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$, each preserve the free Dirac equation, verified on the differential equation for three on-shell momenta and on a superposition of both frequency branches.
- The field map $T$ is anti-linear, $T[i\tilde\Psi]=-i\,T[\tilde\Psi]$, and the operator it induces is anti-unitary; $C$ is anti-linear with a unitary induced operator; $P$ is linear.
- $C$ and $P$ anticommute with $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$ and exchange the two parts of the field; $T$ commutes with $\Gamma$; $CPT$ preserves chirality.
- $C$ exchanges the frequency branches, hence the particle and antiparticle modes.
- Of the internal factors, $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$ is left multiplication by $-\vec e_y\in\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$, while $\eta_C$ multiplies on both sides and $\eta_P$ on the right; neither of the last two is a left multiplication by an element of $\mathbb{B}$.
- The algebra's conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ preserve both sectors; ${}^{*}$ is $+1$ on $\mathbb{M}_+$ and $-1$ on $\mathbb{M}_-$; the sector swap is the central multiplication by $i$. No discrete operation is a sector swap.
- The composition $\Theta=C\circ P\circ T$ acts as $\eta_{CPT}\tilde\Psi(-x)$ with $\eta_{CPT}=\eta_C\eta_P^{J}\eta_T^{J}$, verified as a composition; in the aligned convention $\eta_{CPT}=\Gamma=i\omega$, with $\omega=-R_{\vec e_z}^{\mathrm{axf}}$ the volume element identified with the scalar imaginary. The naive product differs from the true composition once the phases are not fixed by the conjugation.
- The algebra's three conjugations are order-two maps that commute pairwise, with $\natural=\bar{\cdot}\circ{}^{*}$, so they and the identity form a $\mathbb{Z}_2\times\mathbb{Z}_2$. This is a computation on the coefficients, and it is the one point where the classification below and the algebra meet without transcription.

**Transcribed, not derived.**

- The CPT theorem itself, and the hypotheses (locality, Hermiticity, Lorentz invariance, positivity, spin–statistics) that prove it.
- The internal factors and phases of $C$ and $T$, which are the standard objects of the discrete symmetries; the free-field computation is the standard one expressed in the framework's notation.
- The intertwiners, which are the standard relations $\eta_C\,G_\mu^{J}\eta_C^{-1}=-G_\mu$ on the generators and their analogues.
- The **classification** of the operations: $P$ as one order-two map of the algebra, $T$ as another, $PT$ as their composite, $C$ as the twisted one, and the group $\{1,P,T,PT,C,CP,CT,CPT\}\cong\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ that they generate. The classification is a statement about the maps of the algebra; the passage from those maps to the internal cells $\eta_P,\eta_T$ is representation theory that this article does not carry out.

**Gap, left visible.**

- No $\mathbb{B}$-intrinsic form of $C$ and $P$. Because neither of their internal factors is a left multiplication by an element, they cannot be operations of the algebra's left action; whether the framework can realize them on an enlarged structure, or only on the cell algebra, is not built.
- No action on the S-matrix, and no treatment of $CP$ violation.
- No derivation of CPT from the algebra. Whether locality and positivity are expressible as properties of $\mathbb{B}$ in a way that yields the theorem is open.
- The massive case: the parent's mass term is the linear chiral pair, whose two-sided form is the massive Dirac equation that $C$, $P$ and $T$ were each verified to preserve; the open question is whether $C$ is a symmetry of the single-field equation built on the algebra's antilinear real structure $\flat$, the same Majorana-versus-Dirac interpretation as before.

## Open Questions

1. **Is there a $\mathbb{B}$-intrinsic $C$ and $P$?** Neither internal factor is a left multiplication by an element of $\mathbb{B}$. Does an enlargement of the algebra (a larger cell algebra, or a doubling of the field) carry them as left multiplications, or are charge conjugation and parity irreducibly external to the biquaternion structure? This is the structural counterpart of the electron article's observation that the energy-sign cell has no element.

2. **Is $C$ a symmetry of the real structure's pairing?** The algebra's real structure $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$ is anti-linear, while the parent's mass term is the linear chiral pair, and $C$ preserves the massive equation written as a two-sided operator. Whether the separate single-field equation built on the real structure is $C$-invariant, and whether that pairing is Majorana-type or a real-form Dirac mass, decide whether the framework's fermion number is conserved. The companion on the neutrino and Majorana fermions is the natural place.

3. **Can CPT be derived rather than transcribed?** The theorem follows from locality, Hermiticity, Lorentz invariance and positivity. Are any of these native to $\mathbb{B}$, or does the framework only host the notation? A derivation would be the framework's first genuine theorem of this kind.

4. **The phase of charge conjugation and the grading.** The phase of $\eta_C$ is conventional, but $C$ and the fermion-parity element $(-1)^F$ both act on the field with a sign, and the two signs are related in the single-mode algebra. Is the phase of $\eta_C$ fixed by the requirement that $C$ commute with the grading, or is it free?

5. **Where would $CP$ violation live?** The free equation is $CP$-invariant. If the framework has a place for a complex phase in the mass or coupling structure — the Majorana question above is one candidate — does it admit the standard $CP$-violating invariants, and is there a biquaternion statement of them?

6. **Empirical contact.** The construction reproduces standard field theory. Any deviation would have to appear where the framework is used beyond transcription, for instance in the relation between the discrete operations and the mass term; none is visible at the level developed here.

7. **Do the three conjugations derive the internal cells?** The algebra's three conjugations are order-two maps that commute, and the discrete operations are assigned to them. On the field the same operations are implemented by the cells $\eta_P=G_0$ and $\eta_T=G_1G_3=-L_{\vec e_y}^{\mathrm{axf}}$, of which only the second is a left multiplication by an element. Whether a cell can be *read off* a conjugation — so that $\eta_P$ and $\eta_T$ are derived rather than matched — is the representation-theoretic step this article does not take. If it can be taken, the correspondences become a derivation; if it cannot, the classification remains a structural companion rather than a source.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. This is the only section of the article that uses them; the bodies above and below are written in the cells. In this frame the generators are the same four cells, with the $i$ written out rather than carried in the name:
$$
\gamma_0[\mathbb{M}_-]=iR_{\vec e_x}^{\mathrm{pau}}=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell written $\Gamma$ above; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The dictionary to the cells of this article.** The generators are the cells named $G_\mu$ above,
$$
\gamma_0[\mathbb{M}_-]=G_0,\qquad \gamma_1[\mathbb{M}_-]=G_1,\qquad \gamma_2[\mathbb{M}_-]=G_2,\qquad \gamma_3[\mathbb{M}_-]=G_3,\qquad \gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}=\Gamma,
$$

In the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=G_0,\qquad \gamma_1[\mathbb{M}_-]=G_1,\qquad \gamma_2[\mathbb{M}_-]=G_2,\qquad \gamma_3[\mathbb{M}_-]=G_3,\qquad \gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}=\Gamma,
$$

and the composite entries are where $i^{2}=-1$ is spent, twice over:
$$
\gamma_1[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=(i)(i)\,L_{\vec e_x\vec e_z}^{\mathrm{pau}}R_{\vec e_y\vec e_y}^{\mathrm{pau}}=-L_{\vec e_x\vec e_z}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=+L_{\vec e_x\vec e_z}^{\mathrm{pau}}=L_{-\vec e_y}^{\mathrm{pau}}=-L_{\vec e_y}^{\mathrm{pau}}=\eta_T,
$$

The same identities in the axis-free display:

$$
\gamma_1[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=(i)(i)\,L_{\vec e_x\vec e_z}^{\mathrm{axf}}R_{\vec e_y\vec e_y}^{\mathrm{axf}}=-L_{\vec e_x\vec e_z}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}=+L_{\vec e_x\vec e_z}^{\mathrm{axf}}=L_{-\vec e_y}^{\mathrm{axf}}=-L_{\vec e_y}^{\mathrm{axf}}=\eta_T,
$$

$$
\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=(i)(i)\,L_{\vec e_y\vec e_z}^{\mathrm{pau}}R_{\vec e_y\vec e_y}^{\mathrm{pau}}=-L_{\vec e_y\vec e_z}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=+L_{\vec e_y\vec e_z}^{\mathrm{pau}}=L_{\vec e_x}^{\mathrm{pau}},
$$

Read in the axis-free display:

$$
\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=(i)(i)\,L_{\vec e_y\vec e_z}^{\mathrm{axf}}R_{\vec e_y\vec e_y}^{\mathrm{axf}}=-L_{\vec e_y\vec e_z}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}=+L_{\vec e_y\vec e_z}^{\mathrm{axf}}=L_{\vec e_x}^{\mathrm{axf}},
$$

$$
i\gamma_2[\mathbb{M}_-]=i\,(iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=\eta_C,\qquad
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{pau}}=\omega=-i\Gamma .
$$

The same expressions, in the axis-free display:

$$
i\gamma_2[\mathbb{M}_-]=i\,(iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=\eta_C,\qquad
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{axf}}=\omega=-i\Gamma .
$$

Each reduction is a single cell with no $i$ left, and the mechanism is the same in all four: the two factors of $i$ multiply to $-1$, the factor $R_{\vec e_y\vec e_y}^{\mathrm{pau}}=R_{-e_t}^{\mathrm{pau}}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ contributes a second $-1$, and the two cancel, leaving the quaternion product of the two arguments. That is the rule that decides the parity of a product: a product of an even number of generators is real, a product of an odd number is purely imaginary, so an odd product such as $\gamma_1[\mathbb{M}_-]$ or $i\gamma_2[\mathbb{M}_-]$ needs its explicit $i$ and an even product such as $\gamma_1[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ never has one. The mechanical rules are $L_aR_bL_cR_d=L_{ac}R_{db}$, $\vec e_j\vec e_k=\epsilon_{jkl}\vec e_l$ for $j\ne k$ and $\vec e_k^{2}=-e_t$, together with $L_{e_t}^{\mathrm{pau}}=R_{e_t}^{\mathrm{pau}}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ for the identity.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.

## Summary

The biquaternion framework carries the three discrete operations on one field, $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$, an element of $\mathbb{B}$ whose two parts are the $-1$ and $+1$ values of the chirality. Charge conjugation is $C[\tilde\Psi]=-\vec e_y\tilde\Psi^{J}\vec e_y$; parity is $P[\tilde\Psi](x)=i\tilde\Psi(t',-\vec x)\vec e_x$; time reversal is $T[\tilde\Psi](x)=-\vec e_y\tilde\Psi^{J}(-t',\vec x)$. Each was verified separately to preserve the free equation $(\mathbb{D}-m)\tilde\Psi=0$, on the differential equation, for three on-shell momenta and on a superposition of both frequency branches. The field map of time reversal is anti-linear, $T[i\tilde\Psi]=-i\,T[\tilde\Psi]$, and its induced operator is anti-unitary; it conjugates the framework's scalar imaginary. Charge conjugation and parity anticommute with the chirality cell $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$ and exchange the two parts; time reversal commutes with $\Gamma$; the composition preserves chirality.

The two equations are kept apart. The one-sided equation is the chiral pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$, in which every derivative acts by left multiplication and chirality has no room to appear. The two-sided equation is $(\mathbb{D}-m)\tilde\Psi=0$, written out as $\mathbb{D}\tilde\Psi=-\partial_{t'}\tilde\Psi\,\vec e_x-\sum_k\vec e_k\partial_k\tilde\Psi\,\vec e_y$; the chirality is the pure right multiplication $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$, which is what the two-sided operator theory adds. The discrete operations act on the two-sided equation.

The operations are kept distinct from the algebra's own conjugations. The quaternion, complex and Hermitian conjugates all preserve both sectors $\mathbb{M}_-$ and $\mathbb{M}_+$, and the Hermitian conjugate defines them; the sector swap is multiplication by the central scalar imaginary $i$, which is not a conjugation. The transition between the two sectors is therefore not the particle–antiparticle or chiral-conjugate transition; the temptation to read it so is the trap the companion articles record, and it is refuted by the fixed-point definitions. Of the internal factors, only $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$ is left multiplication by an element of the algebra, namely $-\vec e_y$; $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ multiplies on both sides and $\eta_P=G_0$ on the right, so charge conjugation and parity are not operations of the algebra's left action.

The composition was checked as a composition. Because $C$ and $T$ are anti-linear, $\Theta=C\circ P\circ T$ has internal factor $\eta_{CPT}=\eta_C\eta_P^{J}\eta_T^{J}$, equal to $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}=i\omega$ in the convention used here, where $\omega=-R_{\vec e_z}^{\mathrm{axf}}$ is the volume element the framework identifies with the scalar imaginary; $\omega$ multiplies $\tilde\Psi_L$ by $i$ and $\tilde\Psi_R$ by $-i$. The composition is complex-linear, maps particles to antiparticles, and preserves chirality. What the framework establishes is that the free Dirac equation carries these operations and their composition, with the anti-linearity supplied by the algebra's complex conjugation in $C$ and $T$; what it transcribes is the CPT theorem. A free-field check is not the theorem, whose content is the survival of the composition under interactions, and the intrinsic forms of $C$ and $P$ remain open.

The classification supplies a second reading of the same eight operations: they are the identity, the algebra's three conjugations $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ — three order-two maps that commute pairwise, so a $\mathbb{Z}_2\times\mathbb{Z}_2$ — and their composites with charge conjugation, and the eight generate $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$. The algebra's own conjugations are the untwisted maps, while $C$ is the twisted one, which is the algebraic form of the article's finding that $C$ is not a left multiplication by an element. That classification is transcribed, and the step from it to the internal cells is left open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_j \vec e_k=\epsilon_{jkl}\vec e_l$ $(j\ne k)$ |
| $i$ | The scalar imaginary, identified here with the volume element $\omega$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | Real-quaternion subspace; centre |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=({}^{\natural})^{\,*}$ | Quaternion, complex, and Hermitian conjugations; order two, commuting pairwise, $\natural=\bar{\cdot}\circ{}^{*}$ |
| $\tilde{Q}^{\flat}=-\tilde{Q}^{*}$ | Anti-Hermitian conjugate; the algebra's real structure, $\mathbb{C}$-antilinear and order-reversing |
| $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$ | The Dirac field, an element of $\mathbb{B}$; $L$ is the $-1$ value of $\Gamma$ and $R$ the $+1$ value; $(\mathbb{D}-m)\tilde\Psi=0$ |
| $J$, $\tilde\Xi^{J}$ | The conjugation of the field: the anti-linear map of the realization, which keeps $G_0$, $G_1$, $G_3$ and negates $G_2$ |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k\,\vec e_k\partial/\partial Q_k$, $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | Biquaternionic gradient and d'Alembertian |
| $L_{a}$, $R_{b}$, $L_{a}R_{b}$ | Left multiplication, right multiplication, and the two-sided cell that applies both |
| $G_0=iR_{\vec e_x}^{\mathrm{axf}}$, $G_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | The four generator cells; $G_0^{2}=1$, $G_k^{2}=-1$, distinct ones anticommute; $G_2G_3=L_{\vec e_x}$, $G_3G_1=L_{\vec e_y}$, $G_1G_2=L_{\vec e_z}$ |
| $\mathbb{D}=-R_{\vec e_x}^{\mathrm{axf}}\partial_{t'}-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial_k=iG_\mu\partial/\partial x_\mu$ | The Dirac operator; $\mathbb{D}\tilde\Psi=-\partial_{t'}\tilde\Psi\,\vec e_x-\sum_k\vec e_k\partial_k\tilde\Psi\,\vec e_y$; $\mathbb{D}^{2}=-\Box$ |
| $A(\vec p)=G_0E_{\vec p}-\sum_k G_kp_k$ | Plane-wave amplitude, $E_{\vec p}^2=\vec p^2+m^2$; $p\cdot x=E_{\vec p}t'-\vec p\cdot\vec x$ |
| $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$, $\omega=-R_{\vec e_z}^{\mathrm{axf}}=-i\Gamma$ | Chirality cell and volume element; $\Gamma^2=1$; $\Gamma$ anticommutes with each $G_\mu$; $\omega\tilde\Psi_L=i\tilde\Psi_L$, $\omega\tilde\Psi_R=-i\tilde\Psi_R$; $\eta_{CPT}=\Gamma=i\omega$ |
| $C[\tilde\Psi]=-\vec e_y\tilde\Psi^{J}\vec e_y$ | Charge conjugation (anti-linear, $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $\eta_C^2=1$, flips chirality) |
| $P[\tilde\Psi]=i\tilde\Psi(t',-\vec x)\vec e_x$ | Parity (linear, $\eta_P=G_0$, $\eta_P^2=1$, flips chirality) |
| $T[\tilde\Psi]=-\vec e_y\tilde\Psi^{J}(-t',\vec x)$ | Time reversal (anti-linear field map, $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$, $\eta_T^2=-1$, preserves chirality) |
| $\Theta=C\circ P\circ T$ | CPT composition; $\Theta[\tilde\Psi](x)=\eta_{CPT}\tilde\Psi(-x)$ |
| $\eta_{CPT}=\eta_C\eta_P^{J}\eta_T^{J}$ | Internal factor of the composition; $=\Gamma$ in the aligned convention |
| $\{1,P,T,PT,C,CP,CT,CPT\}\cong\mathbb{Z}_2^3$ | The group of the eight discrete operations |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- G. Lüders and B. Zumino, "Connection between Spin and Statistics," *Physical Review* **110** (1958) 1450–1453, for the general proof of the CPT theorem in the axiomatic setting.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the Wightman-axiomatic treatment from which the theorem's hypotheses — locality, positivity, Lorentz invariance — are read.
- J. J. Sakurai, *Invariance Principles and Elementary Particles* (Princeton, 1964), for the classic operator treatment of the discrete symmetries and of CPT.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the CPT theorem in the Lagrangian setting and the role of the anti-unitary operations.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac-field implementations of $C$, $P$ and $T$ used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the plane-wave amplitudes, the charge-conjugation cell and the mode exchange.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the structure of $\mathrm{Cl}_{1,3}$ and the volume element.
- P. K. Rashevskii, "The theory of spinors," *Uspekhi Matematicheskikh Nauk* **10** (1955) 3–110 (*American Mathematical Society Translations* (2) **6** (1957) 1–110), for the classification of the intrinsic order-two maps of the algebra, which the section above reads as the discrete operations.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the assignment of the discrete operations to the intrinsic maps of the algebra and to the charge-conjugation pseudoautomorphism, and for the group structure $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$.
- Companion articles: *Charge Conjugation and the Division Ring*; [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Spin–Statistics Theorem in Biquaternionic Form](the-spin-statistics-theorem-in-biquaternionic-form.html); [The S-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html); [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html); *Clifford Algebra Representation*.
