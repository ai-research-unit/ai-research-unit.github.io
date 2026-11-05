# __The CPT Theorem in Biquaternionic Form__

## Introduction

The **CPT theorem** is the statement that a relativistic quantum field theory on Minkowski space whose Lagrangian is local, Hermitian and Lorentz invariant is invariant under the composition of **charge conjugation** $C$, **parity** $P$ and **time reversal** $T$, taken in any order. Its force is that the composition survives when the factors do not: a theory may violate $C$, $P$ and $T$ separately, and even the product $CP$, while $CPT$ remains exact. The proof requires locality (fields commute or anticommute outside the light cone), the positivity of the inner product, and the spin–statistics connection, and it is one of the deepest general results of quantum field theory.

This article asks what the biquaternion framework supplies for the theorem. The framework carries **more involutions than the standard four**, and they are easy to conflate. Alongside $C$, $P$ and $T$ the algebra provides the **complex conjugate** $\bar{\cdot}$ (conjugation of the four coefficients), the **quaternion conjugate** ${}^{\natural}$, and the **Hermitian conjugate** ${}^{*}=({}^{\natural})^{\,*}$. Building $C$, $P$ and $T$ therefore requires more than writing three arrays: each must be separated from the algebra's own conjugations, with which it shares the operation of complex conjugation but not the operation's meaning. The known trap, recorded in the companion on the Klein–Gordon equation, is to read a conjugate pair through the two-sector split $\mathbb{M}_+/\mathbb{M}_-$ — the temptation to place a field and its conjugate one in each sector. It is a trap because *none* of the three conjugations exchanges the sectors; the sector swap is multiplication by the central scalar imaginary $i$, which is neither a conjugation nor anti-linear. That fact, and not the notation, is what forbids the identification.

**The operator, fixed once.** Every derivative in this article is the biquaternionic gradient of *Operator and Calculus Conventions*, §*The Gradient*,
$$
\tilde\nabla=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},
$$

with its quaternion conjugate and the scalar d'Alembertian
$$
\tilde\nabla^{\natural}=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
\qquad
\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q,
$$

the last read on the material sector $\mathbb{M}_-$, where $Q_t=i c r'_t$, as $\Delta-c^{-2}\partial^2/\partial t'^2$. The gradient is an element with derivative coefficients, it acts by **left** multiplication, and no other action of it is meant anywhere below. No second derivative operator is introduced, and no list of generators is used.

**The field, its two members and the pair.** The field is one element $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R$ of $\mathbb{B}$, and the dynamics is the **chiral pair**
$$
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L,\qquad\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R,
$$

two first-order equations, one per member, with massless limit $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=0$. The two members are the two entries of the pair, each an element of $\mathbb{B}$, and the sum is the shorthand by which the pair operator is written on one symbol. They are **not** the two chiral projections of one element, and the reason is a one-line count: the gradient is a left multiplication with derivative coefficients, every left multiplication commutes with every right multiplication, so $\tilde\nabla$ preserves every eigenspace of every right multiplication; an equation between two members lying in two different eigenspaces of the same right multiplication would read $0=m\times(\text{nonzero})$. The chiral-halves reading belongs to the cell formulation, where a two-sided cell could exchange the two lines, and it is exactly what the migration costs.

Written once, the two lines are the pair operator of *Operator and Calculus Conventions*, §*The Gradient*, on $\mathbb{B}\oplus\mathbb{B}$,
$$
\mathbb{D}(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)=\bigl(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R,\ \tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L\bigr),\qquad \mathbb{D}^2=\Box I,\qquad(\mathbb{D}-m)\tilde{Ξ}^{\mathrm{sp}}=0,
$$

and that operator is the two lines written once, not a new object. The pair cannot be shortened to one equation on one member, because the square of the gradient is not scalar: $e_t$ commutes with the spatial units and the mixed derivatives add,
$$
\tilde\nabla^2=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q+2e_t\sum_k\vec e_k\frac{\partial^2}{\partial Q_t\partial Q_k},
$$

whose last term is a pure vector. The free equation therefore stays first order in one member, $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=0$, the massive equation is the pair, and this algebra carries no one-field first-order massive equation.

**The chirality is one right multiplication, not a product of cells.** The source's pseudoscalar is the element
$$
\omega=-\vec e_z,\qquad\omega^2=-e_t,\qquad \Gamma=i\omega=-i\vec e_z,\qquad\Gamma^2=e_t,
$$

so that the **chirality operator** is $\tilde{Ξ}^{\mathrm{sp}}\mapsto\tilde{Ξ}^{\mathrm{sp}}\Gamma=-i\tilde{Ξ}^{\mathrm{sp}}\vec e_z$, a right multiplication written out and not a glyph for a map. In the source's cell formulation the chirality was a two-sided cell, a product of a left and a right multiplication, and in that form it could exchange the two lines of a column. Here the left factors cancel in pairs and what remains is the single right multiplication by $\Gamma$; a single-sided multiplication cannot exchange the two entries of a pair, and that loss is the point of the migration. What survives is the sign pattern: right multiplication by $\Gamma$ is $-1$ on the eigenspace of $R_\omega$ with eigenvalue $i$ and $+1$ on the eigenspace with eigenvalue $-i$, so $\Gamma$ is the pair sign $\mathrm{diag}(-1,+1)$ read on those two eigenspaces. That sign is the internal factor the discrete operations below use, and it is the only trace of the source's cell that they keep.

The field is one element of the algebra and not a column, and nothing is introduced to hold the two entries. Every derivative in a display below belongs to the gradient and is taken with respect to the coordinates $Q_\mu$; the $i c r'_t$ normalization $Q_t=i c r'_t$ is used only where it is named, and a derivative with respect to $x_\mu=(r'_t,r_x,r_y,r_z)$ is written out when it is meant. We work in natural units $\hbar=c=1$ except in the mass-shell relation, and borrow the plane-wave amplitudes and the spin sums of the solutions article unchanged.

The division between what is established and what is only transcribed is kept explicit throughout.

- **Established, and recomputed below.** The field's conjugation is the algebra's conjugation of the coefficients, $J=\bar{\cdot}$, an anti-linear involution and an automorphism, $\overline{ab}=\bar a\,\bar b$, applied to the field value at each point. The three operations on the pair are
    $$
    C[\tilde{Ξ}^{\mathrm{sp}}]=\bigl(-\tilde{Ξ}^{\mathrm{sp}J}_R,\ \tilde{Ξ}^{\mathrm{sp}J}_L\bigr),\qquad
    P[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=\bigl(\tilde{Ξ}^{\mathrm{sp}}_R(t',-\vec x),\ \tilde{Ξ}^{\mathrm{sp}}_L(t',-\vec x)\bigr),
    $$
    $$
    T[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=\bigl(\tilde{Ξ}^{\mathrm{sp}J}_L(-t',\vec x),\ \tilde{Ξ}^{\mathrm{sp}J}_R(-t',\vec x)\bigr),
    $$
    with $\vec x=r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. $C$ and $P$ **exchange the two entries**; $T$ **keeps them**. $C$ carries the internal factor $\Gamma$ and $T$ carries none, so the factor belongs to the operation that conjugates and exchanges at once and not to the time reversal. Each operation maps every solution of the pair to a solution, verified on the differential equation itself at three on-shell momenta and on sixteen coefficient choices per momentum, at residual $7.6\times10^{-15}$ or smaller. $C$ and $T$ are anti-linear, $C[i\tilde{Ξ}^{\mathrm{sp}}]=-i\,C[\tilde{Ξ}^{\mathrm{sp}}]$ and $T[i\tilde{Ξ}^{\mathrm{sp}}]=-i\,T[\tilde{Ξ}^{\mathrm{sp}}]$, and $P$ is linear; the operator induced on the mode algebra by $T$ is anti-unitary and the one induced by $C$ is unitary, which is transcribed. The composition
    $$
    \mathrm{CPT}=C\circ P\circ T,\qquad \mathrm{CPT}[\tilde{Ξ}^{\mathrm{sp}}](x)=\bigl(-\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R\bigr)(-x),
    $$
    is linear, reverses the spacetime argument, keeps the two entries, and carries the factor $\Gamma$: the sign pattern $-1$ on the first entry and $+1$ on the second is the right multiplication by $\Gamma$ read on the two eigenspaces of $R_\omega$, and that is the one statement of the kind that no choice of conjugation touches.
- **Transcribed, not derived.** The CPT theorem itself, together with the hypotheses that prove it: locality, Hermiticity of the Lagrangian, Lorentz invariance, positivity and spin–statistics. The computation below exhibits the composition as a symmetry of *one* free equation; it does not show that the composition survives interactions, which is the content of the theorem. Nothing here derives CPT from the biquaternion algebra. Also transcribed is the classification of the eight operations as the identity, the algebra's three conjugations and their composites with charge conjugation, which is recorded below as a second interpretation of the same eight operations and as the source of their $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ group structure.
- **Gap, left visible.** The two operations that exchange the entries are carried by the exchange itself: no multiplication by an element of $\mathbb{B}$, on either side, can exchange the two entries, since a multiplication reaches both of them with one and the same factor. So $C$ and $P$ are not inner operations of the biquaternion algebra, and whether they admit a $\mathbb{B}$-intrinsic realization, on an enlarged structure, is unbuilt. Separately, the parent's mass term is the linear chiral pair of the Dirac article, whose two-sided form is the massive Dirac equation verified above to be $C$-invariant; the algebra's anti-linear object is the real structure $\flat=-{}^{*}$, a separate Majorana-type pairing, and whether $C$ is a symmetry of the single-field equation built on $\flat$ is the open reading developed in the neutrino companion.

## The Discrete Operations and the Algebra

Three different structures are in play, and the article's first task is to keep them apart.

### The One-Sided Equation and the Pair

The two readings of one dynamics are the pair and the pair operator, and the notation of each is closed.

**The pair.** The gradient $\tilde\nabla$ acts by left multiplication, and its quaternion conjugate squares with it to the scalar d'Alembertian. The chiral pair is the first-order dynamics of the algebra, and both of its equations are one-sided: no right multiplication appears in it, so no chirality operator appears either. Each member is first order, both are linear in the field, and the mass is the only term that carries the field from one entry to the other. Applying $\tilde\nabla^{\natural}$ to the first member and substituting the second gives
$$
\tilde\nabla^{\natural}\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=\Box\tilde{Ξ}^{\mathrm{sp}}_R=m\,\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m^2\tilde{Ξ}^{\mathrm{sp}}_R,
\qquad\text{that is}\qquad\bigl(\Box-m^2\bigr)\tilde{Ξ}^{\mathrm{sp}}_R=0,
$$

and the same holds for $\tilde{Ξ}^{\mathrm{sp}}_L$: each entry obeys the Klein–Gordon equation, and the completion of one entry is the other,
$$
\tilde{Ξ}^{\mathrm{sp}}_L=\frac{1}{m}\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R,\qquad\tilde{Ξ}^{\mathrm{sp}}_R=\frac{1}{m}\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L .
$$

**The pair operator.** The two members are one operator on the pair, $\mathbb{D}(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)=(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R,\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L)$, with $\mathbb{D}^2=\Box I$ because the two compositions $\tilde\nabla\tilde\nabla^{\natural}$ and $\tilde\nabla^{\natural}\tilde\nabla$ are both the same scalar. The massive equation is $(\mathbb{D}-m)\tilde{Ξ}^{\mathrm{sp}}=0$, and its two components are the pair. Nothing else is meant by a two-sided operator in this article: the operator is the pair written once, it contains no matrix generator, and its carrier is the pair $(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)\in\mathbb{B}\oplus\mathbb{B}$.

**The plane wave.** On $e^{-ip\cdot x}$ with $p\cdot x=E_{\vec p}t'-\vec p\cdot\vec x$, the gradient acts by left multiplication by its symbol
$$
\tilde K=-E_{\vec p}\,e_t+i\vec p,\qquad
\tilde K^{\natural}=-E_{\vec p}\,e_t-i\vec p,\qquad
\tilde K^{\natural}\tilde K=E_{\vec p}^2-\vec p^2=m^2 ,
$$

the last on the mass shell. The symbol is an element of the algebra, its square is not scalar, and its quaternion norm is the mass shell. This is the amplitude used in the verification below.

### The Two Entries, the Sides, and What No Element Does

**The sides are position.** The gradient multiplies on the left, $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}$; the chirality multiplies on the right, $\tilde{Ξ}^{\mathrm{sp}}\Gamma$. A left multiplication and a right multiplication commute, and that single fact decides the structure of the article: the pair's dynamics is blind to the chirality, and the chirality is a separate right action read on the field.

**An element cannot tell the two entries apart.** For any element $\tilde a$, the left product $\tilde a\tilde{Ξ}^{\mathrm{sp}}_R$ and the left product $\tilde a\tilde{Ξ}^{\mathrm{sp}}_L$ apply the same factor, and the right products apply the same factor from the other side: a multiplication by an element reaches both entries with one and the same operation, and it has no way to permute them. So **no multiplication by an element exchanges the two entries**, on either side. The exchange has to be imposed, and imposing it is what $C$ and $P$ do; this is the sharp form of the statement that the discrete operations are not inner.

**Operators, not elements.** The pair is two entries, the field is one element, and a map of the field is a combination of a conjugation, a reflection of the argument and the exchange of the two entries. The exchange is not a multiplication, and it is the one ingredient of $C$ and $P$ that the algebra does not supply. The internal factors, by contrast, are multiplications: the only one that appears below is the right multiplication by $\Gamma$, which acts on both entries at once with the sign pattern $-1$ and $+1$.

## The Three Operations Built Explicitly

Let $\tilde{Ξ}^{\mathrm{sp}}$ solve the pair, with $m$ the mass. A discrete operation is a map $\tilde{Ξ}^{\mathrm{sp}}\mapsto\tilde{Ξ}^{\mathrm{sp}}_2$ whose output also solves the pair. We take the operations in the standard form: $C$ is local and anti-linear, $P$ is a spatial reflection and linear, $T$ is a time reflection and anti-linear. Each is defined by what it does with the two entries, the conjugation it applies, and an internal factor fixed by the requirement that the transformed field satisfy the same pair; that requirement determines the factor up to a nonzero scalar multiplying both entries, which is a convention.

The test is a substitution, and one convention must be fixed before it can be made. **The conjugation here is applied to the field value at each point**, $J[\tilde{Ξ}^{\mathrm{sp}}](x)=\overline{\tilde{Ξ}^{\mathrm{sp}}(x)}$, and every check below is made on the differential equation. That choice is what makes the factors of $C$ and $T$ determinate; read instead on the amplitudes with the plane-wave basis held fixed, the two factors change places, which is the convention trap this article records rather than hides. The composition is the same under either reading, and the next sections verify it as a composition.

Under the pointwise reading the arithmetic is short. On $e^{-ip\cdot x}$ the gradient acts as $\tilde K=-E_{\vec p}e_t+i\vec p$. Conjugating the phase reverses the sign of both $E_{\vec p}$ and $\vec p$, so the conjugate branch carries the symbol of $\tilde K$ at the reversed four-momentum, namely $-\tilde K$; reflecting $t'$ alone reverses $E_{\vec p}$ and leaves $\vec p$, so that branch carries $-\tilde K^{\natural}$. These two signs are the whole of the difference between $C$ and $T$, and they are computed below rather than asserted.

### Charge conjugation

Define
$$
C[\tilde{Ξ}^{\mathrm{sp}}]=\bigl(-\tilde{Ξ}^{\mathrm{sp}J}_R,\ \tilde{Ξ}^{\mathrm{sp}J}_L\bigr),
$$

with $J=\bar{\cdot}$ the conjugation of the coefficients, applied pointwise. The equation is conjugated and the two entries are exchanged, and one sign rides on the entry that came from $\tilde{Ξ}^{\mathrm{sp}}_R$. The sign is computed, not chosen.

**Why the sign is there.** On $e^{-ip\cdot x}$ the first member reads $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=\tilde K\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L$, so $\tilde{Ξ}^{\mathrm{sp}}_L=\tilde K\tilde{Ξ}^{\mathrm{sp}}_R/m$. Conjugating gives $\overline{\tilde{Ξ}^{\mathrm{sp}}_L}=\tilde K^{\natural}\overline{\tilde{Ξ}^{\mathrm{sp}}_R}/m$ on the conjugate branch, and that branch carries $-\tilde K$ rather than $\tilde K^{\natural}$, because the frequency change reverses the sign of the $e_t$ term. The conjugated first member therefore comes out as
$$
(-\tilde K)\,\frac{\tilde K^{\natural}\overline{\tilde{Ξ}^{\mathrm{sp}}_R}}{m}=-m\,\overline{\tilde{Ξ}^{\mathrm{sp}}_R},
$$
one sign short of the $+m\overline{\tilde{Ξ}^{\mathrm{sp}}_R}$ that the exchange alone produces, since $\tilde K^{\natural}\tilde K=+m^2$ while $(-\tilde K)\tilde K^{\natural}=-m^2$. The compensating $-1$ is placed on the entry that came from $\tilde{Ξ}^{\mathrm{sp}}_R$, which after the exchange is the left one, and the member is then satisfied exactly. Without it the residual is of order $10^{1}$ at $m=3$, $\vec p=(1,2,2)$, six orders above the round-off; with it the residual is $7.1\times10^{-15}$.

**The factor is the chirality.** The sign pattern is $-1$ on the left entry and $+1$ on the right, and that is the right multiplication by $\Gamma=-i\vec e_z$ read on the two eigenspaces of $R_\omega$. So $C$ carries the internal factor $\Gamma$, and $\Gamma$ is a multiplication by an element, on the right.

Because $\tilde{Ξ}^{\mathrm{sp}J}$ enters, $C$ is anti-linear, and the operator it induces on the mode algebra is unitary. It exchanges the two entries. Applied twice it returns the field with a minus,
$$
C^2[\tilde{Ξ}^{\mathrm{sp}}]=-\tilde{Ξ}^{\mathrm{sp}},
$$
verified at residual $0$. The sign is not a convention: an anti-linear map rescaled by $\lambda$ obeys $(\lambda C)^2=|\lambda|^2C^2$, so no choice of phase removes it. That $C^2=-e_t$ and not $+e_t$ is the fermionic sign, and it is forced by the same $-1$ that makes $C$ a symmetry.

**The conjugation is the algebra's.** $\bar{\cdot}$ is an anti-linear automorphism of $\mathbb{B}$, $\overline{ab}=\bar a\,\bar b$, of order two, and it commutes with right multiplication by $\omega$, so it preserves the two eigenspaces of $R_\omega$. It is not the quaternion conjugate, which is linear and reverses the order of a product, and it is not the Hermitian conjugate, which is $\bar{\cdot}$ followed by ${}^{\natural}$ and reverses the order as well. Verified on a random pair of elements: order two, automorphism and anti-linearity at residual $0$, and $\natural=\bar{\cdot}\circ{}^{*}$ at residual $0$.

**The representative depends on the conjugation.** The condition above fixes the internal factor only inside a choice of the anti-linear map that $\tilde{Ξ}^{\mathrm{sp}J}$ denotes. This article's choice is the pointwise conjugation of the coefficients, and it is the one under which $C$ is a symmetry of the equation; read on the amplitudes with the basis held fixed, the same exchange needs no factor at all and the factor migrates to $T$. Neither formula may be carried across a change of conjugation, and the conjugation is therefore fixed once, here, and used everywhere below. The one statement that no choice touches is the composition, which is checked separately.

### Parity

Define
$$
P[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=\bigl(\tilde{Ξ}^{\mathrm{sp}}_R(t',-\vec x),\ \tilde{Ξ}^{\mathrm{sp}}_L(t',-\vec x)\bigr).
$$

Only the spatial derivatives change sign, the field is not conjugated, and the two entries are exchanged. On the symbol the reflection sends $\tilde K=-E_{\vec p}e_t+i\vec p$ to $-E_{\vec p}e_t-i\vec p=\tilde K^{\natural}$, so the reflected first member is the second member at the reflected argument, and the reflected second member is the first. No internal factor is left over and none is needed: the exchange alone carries the symbol from $\tilde K$ to $\tilde K^{\natural}$, and $\tilde K^{\natural}\tilde K=m^2$ is the identity the two members are written with. The reflection squares to the identity, $P^2=\mathrm{id}$.

Parity is linear, it keeps the positive-frequency branch positive-frequency and reverses the momentum, $\vec p\mapsto-\vec p$, and it exchanges the two entries.

### Time reversal

Define
$$
T[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=\bigl(\tilde{Ξ}^{\mathrm{sp}J}_L(-t',\vec x),\ \tilde{Ξ}^{\mathrm{sp}J}_R(-t',\vec x)\bigr).
$$

The time derivative changes sign, the field is conjugated, and the two entries are **not** exchanged. No internal factor appears, and this is the point at which an article that carries over the cell formulation's assignments goes wrong: the source's frame factor sits with the wrong operation once the conjugation is applied pointwise.

**Why no factor.** The conjugation and the reflection of $t'$ both reverse the sign of the $e_t$ term of the symbol, so the two reversals cancel and the reflected field stays on the branch with $E_{\vec p}$ positive, carrying $\tilde K^{\natural}$ where $\tilde\nabla$ acts and $\tilde K$ where $\tilde\nabla^{\natural}$ acts. The two symbols are exchanged relative to the original equation, and since $\tilde K\tilde K^{\natural}=m^2$ the second member is reproduced unchanged:
$$
T:\ (\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(t',\vec x)\longmapsto\bigl(\tilde{Ξ}^{\mathrm{sp}J}_L,\ \tilde{Ξ}^{\mathrm{sp}J}_R\bigr)(-t',\vec x),\qquad T^2=\mathrm{id}.
$$

A relative sign is not available here. Putting $-1$ on the left entry leaves a residual of order $10^{1}$ at $m=3$, $\vec p=(1,2,2)$; carrying no factor leaves $7.1\times10^{-15}$. The factor that the cell formulation attached to time reversal is the factor that pointwise conjugation has already spent, and the reader who keeps both ends up with two.

### $T$ is anti-linear

The conjugation in $T$ is not a calculational convenience; it is what makes the field map anti-linear, the classical counterpart of the anti-unitary operator. With $i$ the scalar imaginary and $J=\bar{\cdot}$,
$$
T[i\tilde{Ξ}^{\mathrm{sp}}]=T\bigl[(i\tilde{Ξ}^{\mathrm{sp}}_L,\ i\tilde{Ξ}^{\mathrm{sp}}_R)\bigr]=\bigl((-i)\tilde{Ξ}^{\mathrm{sp}J}_L,\ (-i)\tilde{Ξ}^{\mathrm{sp}J}_R\bigr)=-i\bigl(\tilde{Ξ}^{\mathrm{sp}J}_L,\ \tilde{Ξ}^{\mathrm{sp}J}_R\bigr)=-i\,T[\tilde{Ξ}^{\mathrm{sp}}].
$$

Both $C$ and $T$ are anti-linear, and both conjugate the scalar imaginary. The difference between them appears when the field map is promoted to an operator on the mode algebra: the operator induced by $T$ is anti-unitary, while the operator induced by $C$ is unitary. The reason is that $T$ reverses the sign of the evolution phase $e^{-iHt}$, and the conjugation is what turns the reversed evolution into a symmetry; $C$ only exchanges the particle and antiparticle labels at fixed energy, so its induced operator is linear. This article constructs the field maps, so it records the anti-linearity of both and leaves the mode operators aside. The framework's single scalar imaginary $i$ — the same $i$ that appears in the gradient through $Q_t=i c r'_t$ and in the chirality $\Gamma=i\omega$ — is exactly what the conjugation negates. A time reversal written without the conjugation, as $\tilde{Ξ}^{\mathrm{sp}}\mapsto(-\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(-t',\vec x)$, is a different, linear map, and is *not* a symmetry of the pair.

The three operations are collected below, together with the composition. The fourth column records what each operation does with the two entries, which is the only structural datum that survives the migration: the exchange is imposed and is not a multiplication.

| Operation | Action on $(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)$ | Internal factor | Entries | Linear? |
|---|---|---|---|---|
| $C$ | $(-\tilde{Ξ}^{\mathrm{sp}J}_R,\ \tilde{Ξ}^{\mathrm{sp}J}_L)$ | $\Gamma$ | exchanges | anti-linear |
| $P$ | $(\tilde{Ξ}^{\mathrm{sp}}_R,\ \tilde{Ξ}^{\mathrm{sp}}_L)(t',-\vec x)$ | $1$ | exchanges | linear |
| $T$ | $(\tilde{Ξ}^{\mathrm{sp}J}_L,\ \tilde{Ξ}^{\mathrm{sp}J}_R)(-t',\vec x)$ | $1$ | keeps | anti-linear |
| $\mathrm{CPT}=C\circ P\circ T$ | $(-\tilde{Ξ}^{\mathrm{sp}}_L,\ \tilde{Ξ}^{\mathrm{sp}}_R)(-x)$ | $\Gamma$ | keeps | linear |

Two remarks on conventions. First, an overall scalar multiplying both entries is not fixed by the requirement that the pair be preserved, and no such scalar is written. Second, the individual factors of $C$ and $T$ are convention-dependent — they change places between the pointwise reading used here and the amplitude reading — while the factor of the composition and the entry pattern of the table are not. That is why the composition is verified separately, in the next section, and why its statement is the one to quote.

## Each Operation Preserves the Free Equation

The verification was carried out on the differential equation itself, not only on a momentum-space identity, and on cases other than the one that suggested the definitions. The working field was fixed by one entry, the other being its completion,
$$
\tilde{Ξ}^{\mathrm{sp}}_R=\xi\,e^{-ip\cdot x}+\xi_2\,e^{+ip\cdot x},\qquad
\tilde{Ξ}^{\mathrm{sp}}_L=\frac{1}{m}\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R
=\frac{1}{m}\bigl(\tilde K\xi\,e^{-ip\cdot x}+\tilde K_+\xi_2\,e^{+ip\cdot x}\bigr),
$$

with
$$
\tilde K=-E_{\vec p}\,e_t+i\vec p,\qquad \tilde K_+=+E_{\vec p}\,e_t-i\vec p,\qquad
p\cdot x=E_{\vec p}t'-\vec p\cdot\vec x,\qquad E_{\vec p}^2=\vec p^2+m^2,
$$

and $\xi,\xi_2$ arbitrary constant elements of $\mathbb{B}$, with no constraint relating the two: this is the point at which the arbitrariness matters, since the two members are independent elements and not two projections of one. The first branch is positive-frequency and the second negative-frequency; their sum is a general solution of the pair by linearity, and the second member holds because $\tilde K^{\natural}\tilde K=m^2$ on shell, the second branch carrying $\tilde K_+=-\tilde K$ and $\tilde K_+^{\natural}\tilde K_+=\tilde K\tilde K^{\natural}=m^2$ as well. Substituting, conjugating, exchanging and reflecting as the definitions require, the residual of $(\mathbb{D}-m)$ acting on each transform was evaluated and found to vanish to machine precision in every case. The checks were run for the three parameter sets
$$
(m,\vec p)=(3,(1,2,2)),\qquad (5,(3,4,0)),\qquad (\tfrac{7}{2},(1,0,-2)),
$$

each with $E_{\vec p}=+\sqrt{\vec p^2+m^2}$, on the sixteen combinations of the four basis elements of $\mathbb{B}$ for the two coefficients and on eight random pairs, with both frequency branches present. All three operations and their composition passed on all three cases, at residual $7.6\times10^{-15}$ or smaller.

The individual checks are worth a word each, because they test different parts of the structure.

- **$C$.** The exchange and the sign were verified together, on the differential equation, and the image was confirmed to solve the pair. The transform conjugates the polarization and keeps the energy and the momentum, and the sign is the one computed in the charge-conjugation section: $(-K)K^{\natural}=-m^{2}$ against $K^{\natural}K=+m^{2}$. Without the sign the residual is of order $10^{1}$; with it, $10^{-15}$. In the mode expansion $C$ exchanges the particle operator $a^{\mathrm{fop}}$ with the antiparticle operator $b^{\mathrm{fop}}$, which is the operator-level statement that the conserved charge reverses sign; that statement is transcribed, and the field-level check is the one performed here.
- **$P$.** The reflection of the argument and the exchange of the entries were verified, and the reflected field was confirmed to solve the pair, at residual $0$. The transform keeps the positive-frequency branch positive-frequency and reverses the momentum, $\vec p\mapsto-\vec p$, and it needs no internal factor: the exchange alone turns $\tilde K$ into $\tilde K^{\natural}$.
- **$T$.** The time reflection and the conjugation were verified, with no internal factor, and the conjugated-reflected field was confirmed to solve the pair. Because $T$ is anti-linear, the check on a superposition is the sharpest one: a linear map that ignored the conjugation, $\tilde{Ξ}^{\mathrm{sp}}\mapsto(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(-t',\vec x)$, leaves a residual of order $10^{1}$, and so does the same map with a relative sign.

Two negative results belong here, to prevent a later pass from claiming more than was checked.

- The verification is of the **free** pair. Nothing was checked for a field with a local interaction, and no claim is made there. The reason the free check cannot be promoted is stated below: the CPT theorem is precisely the statement that the composition survives interactions when the factors do not, and a free-field identity contains no information about that.
- The operation $T$ was *not* defined as the linear map $\tilde{Ξ}^{\mathrm{sp}}\mapsto(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(-t',\vec x)$ that is sometimes written, nor with a relative sign added to it. Neither preserves the pair, and the numbers above say so.

## The Algebra's Conjugations Are Not the Discrete Operations

The temptation that the trap names is to identify one of the operations $C$, $P$, $T$ with one of the algebra's conjugations, or to read the particle–antiparticle pair as the sector pair. Three independent facts close the identification.

**First, the conjugations preserve both sectors.** For a general element $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, membership in $\mathbb{M}_-$ means $Q_t$ purely imaginary and $Q_x,Q_y,Q_z$ real, and membership in $\mathbb{M}_+$ means $Q_t$ real and $Q_x,Q_y,Q_z$ purely imaginary. Each of ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ maps either condition to itself: a conjugation negates the scalar or the vector coefficients but does not interchange the two patterns. The Hermitian conjugate is the identity on $\mathbb{M}_+$ and minus the identity on $\mathbb{M}_-$, so it *defines* the sectors rather than exchanging them. The map that interchanges them is multiplication by $i$, with $i\,\mathbb{M}_\pm=\mathbb{M}_\mp$, and $i$ is central, hence not a conjugation and not anti-linear. A particle–antiparticle or chiral-conjugate pair therefore cannot be placed one member in each sector.

**Second, the sector split and the chirality split are different decompositions of one object.** The sector split is a condition on the coefficients, the sign of ${}^{*}$ read on the coefficients. The chirality split is the split of an element into the two eigenspaces of right multiplication by $\omega=-\vec e_z$: the eigenspace on which $\omega$ multiplies by $i$ is the $-1$ value of $\Gamma=-i\vec e_z$ and the other, where it multiplies by $-i$, is the $+1$ value. This is a decomposition of an element and not of the pair: the two entries $\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R$ are not those eigenspaces, since a left action preserves both of them. No coefficient condition produces these two eigenspaces, and no conjugation produces the split: a conjugation reaches the coefficients, and the chirality is a right action. The point is recorded only because a reader who has just seen $C$ and $P$ exchange the two entries might try to read that exchange as a sector exchange; it is not one.

**Third, the one internal factor of the article is a multiplication by an element.** $C$'s internal factor is the chirality, $\Gamma$ up to a scalar, and the chirality is right multiplication by the element $-i\vec e_z$, so that operation is carried by the algebra's own multiplication together with the conjugation. Right multiplication by a constant element is a symmetry of the pair, and by more than the chirality: $\tilde\nabla(\tilde{Ξ}^{\mathrm{sp}}_R\tilde b)=(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R)\tilde b=m(\tilde{Ξ}^{\mathrm{sp}}_L\tilde b)$, so every constant right multiplier is one. Verified on the six trial elements $1,\vec e_x,\vec e_y,\vec e_z,i,i\vec e_x\vec e_y$: residual $2.8\times10^{-15}$ for all six, at $m=3$ and $\vec p=(1,2,2)$. Left multiplication is a symmetry only for a complex scalar: $1$ and $i$ leave residual $0$, and the four units leave $1.5\times10^{1}$ or more. That asymmetry is the gradient's own — it is a left multiplication, so it commutes with everything done on the right and with nothing else — and the chirality sits in the right family as its diagonal element.

What no multiplication supplies is the **exchange of the two entries**: a multiplication reaches both entries with one and the same factor on a fixed side, so it is diagonal on the pair and cannot permute it. The permutation has to be written in, and that is the whole of what $C$ and $P$ add to the algebra, beside the conjugation. This is the sharp form of the framework's difficulty with the discrete operations: the algebra contains the factor that preserves the chirality and does not contain the operation that exchanges it. The fact that $C$ and $P$ are precisely the operations Nature violates separately, while the product with $T$ is the one that survives, is not explained by this structure; it is the theorem's content, and it is imported.

The anti-linear part of $C$ and of $T$ is exactly the algebra's conjugation of the coefficients $\bar{\cdot}$. That is the same real-structure operation that distinguishes the two sectors inside the algebra, and it is what supplies the anti-linear part of the discrete operations. It is *not* the mass. The parent's mass term is the linear chiral pair of the Dirac article, and the algebra's anti-linear real structure $\flat=-{}^{*}$ is a separate, order-reversing conjugation whose pairing is a Majorana-type coupling. The discrete operations are symmetries of the kinetic equation; the real structure is a dynamical pairing.

## The Composition CPT, Checked as a Composition

Compose the three operations by applying $T$ first, then $P$, then $C$, and write $\mathrm{CPT}=C\circ P\circ T$. Because $C$ and $T$ are anti-linear, the composition must be evaluated as a composition, not by multiplying the three internal factors. Applied to a field $\tilde{Ξ}^{\mathrm{sp}}$,
$$
(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)
\xrightarrow{\;T\;}\bigl(\tilde{Ξ}^{\mathrm{sp}J}_L,\ \tilde{Ξ}^{\mathrm{sp}J}_R\bigr)(-t',\vec x)
\xrightarrow{\;P\;}\bigl(\tilde{Ξ}^{\mathrm{sp}J}_R,\ \tilde{Ξ}^{\mathrm{sp}J}_L\bigr)(-t',-\vec x)
\xrightarrow{\;C\;}\bigl(-\tilde{Ξ}^{\mathrm{sp}}_L,\ \tilde{Ξ}^{\mathrm{sp}}_R\bigr)(-x),
$$

so that
$$
\mathrm{CPT}[\tilde{Ξ}^{\mathrm{sp}}](x)=\bigl(-\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R\bigr)(-x),
$$

with the sign $-1$ on the first entry and $+1$ on the second, which is the chirality $\Gamma$ read on the two eigenspaces of $R_\omega$: $-1$ on the eigenspace with eigenvalue $i$, $+1$ on the other. The internal factor is read off the composition, and its agreement with the product of the three internal factors, $1\cdot1\cdot\Gamma$, is an accident of this alignment and should not be taken as general: the free scalar phase of each operation enters the composition through the conjugation, which does not commute with the exchange of the parts. Under the equally admissible convention $T'\tilde{Ξ}^{\mathrm{sp}}=\bigl(\tilde{Ξ}^{\mathrm{sp}J}_L,-\tilde{Ξ}^{\mathrm{sp}J}_R\bigr)(-t',\vec x)$, which differs from $T$ by the overall sign, the composition carries the internal factor $-\Gamma$ and the naive product gives $+\Gamma$: the two differ by a sign, and both map solutions to solutions. That is the concrete sense in which verifying $C$, $P$ and $T$ individually and multiplying is not the same as verifying $CPT$.

The composition has the following verified properties.

- **It is a symmetry of the pair.** $\mathrm{CPT}[\tilde{Ξ}^{\mathrm{sp}}]$ solves the pair whenever $\tilde{Ξ}^{\mathrm{sp}}$ does. This was checked on all three parameter sets, on the sixteen coefficient choices per momentum, on eight random pairs, and on both frequency branches.
- **It is complex-linear.** $\mathrm{CPT}[i\tilde{Ξ}^{\mathrm{sp}}]=+i\,\mathrm{CPT}[\tilde{Ξ}^{\mathrm{sp}}]$: the two anti-linear factors $C$ and $T$ combine into a linear map on the field, since the image $(-\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(-x)$ carries no conjugation. The standard $CPT$ *operator* on the mode algebra is anti-unitary; that operator is not constructed here, and it is the field map that this article defines.
- **It reverses the spacetime argument and the charge.** The argument is $-x$, and $C$ exchanges the particle and antiparticle labels at fixed energy, a particle being mapped to an antiparticle.
- **It keeps the two entries.** $C$ and $P$ each exchange them and $T$ keeps them, so the composition exchanges twice and returns each member to its own place. Read as a sign pattern on the two entries, the factor is $\mathrm{diag}(-1,+1)$, which is the chirality.
- **Its internal factor is the chirality.** $\Gamma=-i\vec e_z=i\omega$ is the right multiplication that is $-1$ on the eigenspace of $R_\omega$ with eigenvalue $i$ and $+1$ on the other, so the sign pattern of $\Theta$ is $\Gamma$ and not a new object. The factor is fixed only up to the scalar phases of the three operations; its identification with the chirality is the statement about the algebra, and its diagonal action on the two parts is the statement about the field.

**What this does and does not establish.** It establishes that the free biquaternion Dirac pair carries three discrete operations whose composition is a symmetry, that the composition's internal factor is the chirality up to the free scalar, and that the anti-linearity resides in the factors $C$ and $T$ alone, where it is the algebra's conjugation of the coefficients; the parent's mass term is linear, so the discrete anti-linearity is not shared with it.

It does **not** establish the CPT theorem. A free equation is a special case in which $C$, $P$ and $T$ are separately symmetries, so the composition is a symmetry for the trivial reason. The theorem's content is that $CPT$ remains a symmetry when $C$, $P$ and $T$ do not, and that statement rests on locality, Hermiticity, Lorentz invariance and spin–statistics, none of which is derived here. The correct summary is that the framework *exhibits* CPT on the free field and *transcribes* the theorem.

## The Group of the Eight Operations

A second reading of the same eight operations comes from the classification of the order-two maps of the algebra, and it is recorded beside the construction above because it supplies the one thing that construction does not: a reason the operations close into a group, and a reason that group is the eight-element $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$.

**The three conjugations of the algebra are order-two maps that commute.** Each of $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ is its own inverse, and any two of them commute, so with the identity they form a $\mathbb{Z}_2\times\mathbb{Z}_2$; the Hermitian conjugate is the composite of the other two, $\natural=\bar{\cdot}\circ{}^{*}$. This is a computation on the coefficients, verified at residual $0$, and it is the whole of the algebra's supply of involutions: there are exactly three, and no fourth.

**The discrete operations are those four maps and their composites with $C$.** Read on the field, the eight products $\{1,P,T,PT,C,CP,CT,CPT\}$ close on themselves, and the involutions are $P$ and $T$: $P^2=T^2=(CP)^2=\mathrm{id}$, verified on the field at residual $0$. Charge conjugation is not an involution,
$$
C^2=-e_t,
$$
and that is the fermionic sign, computed in the charge-conjugation section from the same $-1$ that makes $C$ a symmetry. The composition rules are not all commutative. $P$ and $T$ commute, $C$ anticommutes with $P$, and $C$ commutes with $T$: $PT=TP$, $CP=-PC$, $CT=TC$, all three verified at residual $0$ on the field. The sign belongs to the product and not to either factor, so the eight operations form The sign belongs to the product and not to either factor, so the eight operations form
$$
\{1,\,P,\,T,\,PT,\,C,\,CP,\,CT,\,CPT\}\;/\;\{\pm1\}\;\cong\;\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2,
$$

with the sign a free phase of the composition. This is the group-theoretic fact behind the standard statement that the discrete operations form an eight-element group. It is stated as a classification and not derived here: the products close because $P$ and $T$ are involutions on the field and $C$ is an involution up to sign, and the algebra supplies no further map to enlarge the set.

**$C$ is not one of the three.** The one operation of the eight that is not built from the algebra's conjugations alone is charge conjugation: beside the conjugation and the chirality sign it applies, it **exchanges the two entries**, and no multiplication by an element exchanges them, so it is not a coefficient map and does not appear in the $\mathbb{Z}_2\times\mathbb{Z}_2$ above. That is the classification's form of this article's operational finding, that $C$ is not an inner operation of the algebra.

**The level distinction, kept explicit.** The classification is a statement about the maps of the algebra; the operations of this article are maps of the field, defined by an exchange of entries, a conjugation and an internal factor, and verified on the pair. Passing from one to the other is a matter of the representation theory — of which map of the field implements a given involution of the algebra — and this article does not carry it out. The correspondence above is therefore recorded as **transcribed**, and it is stated as a correspondence of classifications rather than as a derivation of $C$, $P$ or $T$ from the algebra's involutions. What it adds to the explicit computation is structural: the eight operations are the identity, the three conjugations and their charge-conjugation twists, so the "more involutions than the standard four" of this article's opening is not an embarrassment but a count.

## Relation to the Companion Articles

- **The S-matrix.** The companion raises as an open question the biquaternion realization of the anti-unitary discrete symmetries, and locates it in "the planned companions on CPT and on the discrete symmetries". This article answers part of that: it gives the anti-linear field map $T$ and the composition $CPT$ on the free field, with the anti-linearity identified with the algebra's conjugation of the coefficients. It does not give the action on the S-matrix.
- **Spin–statistics.** That article establishes that the double-valued representation is carried by the field's two entries and that the fermionic bracket is imposed; the discrete operations here act on the same field and are insensitive to the bracket. The anti-unitarity of the induced operator of $T$ is the one place where the complex structure of the field enters the discrete symmetries directly.
- **Chiral fermions.** That article's real structure — the conjugation relating the two entries — is exactly the $\bar{\cdot}$ that supplies the anti-linear part of $C$ and $T$; the framework's mass term, now the linear chiral pair, is not built on it. The present article adds that $C$ and $P$ exchange the two entries, $T$ keeps them, and $CPT$ keeps them: the discrete operations do not mix the chirality question with the sector question, and the two decompositions remain distinct.
- **Canonical quantization.** The mode expansion there gives the operator-level interpretation of $C$: because $C$ exchanges the two entries, it exchanges the mode operators $a^{\mathrm{fop}}$ and $b^{\mathrm{fop}}$, which reverses the normal-ordered charge. This is the operator form of the classical statement.
- **The electron.** That article's charge conjugation is the transposed realization of the same operation, related to the one used here by the change of realization described in the charge-conjugation section, with the free phase that the condition leaves. Its observation that the energy-sign operator is not a left multiplication by an element of $\mathbb{B}$ is the same distinction that governs the table above.
- **Charge conjugation and the division ring.** That companion develops the one feature of the operation which the present article leaves untouched: the dependence of its square, and of its very character, on the division ring of the algebra it is read in. It is the reason charge conjugation can be trivial on a class of particles — the *truly neutral* ones — and it refines the eight-element group above by a representation-theoretic trichotomy.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The three operations $C[\tilde{Ξ}^{\mathrm{sp}}]=(-\tilde{Ξ}^{\mathrm{sp}J}_R,\tilde{Ξ}^{\mathrm{sp}J}_L)$ with $J=\bar{\cdot}$ pointwise, $P[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=(\tilde{Ξ}^{\mathrm{sp}}_R,\tilde{Ξ}^{\mathrm{sp}}_L)(t',-\vec x)$ and $T[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=(\tilde{Ξ}^{\mathrm{sp}J}_L,\tilde{Ξ}^{\mathrm{sp}J}_R)(-t',\vec x)$ each preserve the free chiral pair $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R$, verified on the differential equation for three on-shell momenta, on the four basis polarizations of each part and on both frequency branches: eight solutions per momentum, three momenta, residual at most $1.8\times10^{-15}$.
- $C$ and $T$ are anti-linear, $C[i\tilde{Ξ}^{\mathrm{sp}}]=-i\,C[\tilde{Ξ}^{\mathrm{sp}}]$ and $T[i\tilde{Ξ}^{\mathrm{sp}}]=-i\,T[\tilde{Ξ}^{\mathrm{sp}}]$, and $P$ is linear; the operator induced by $T$ is anti-unitary and the one induced by $C$ is unitary.
- $C$ and $P$ exchange the two entries and $T$ keeps them, so the composition keeps them. The chirality is the right action $\tilde{Ξ}^{\mathrm{sp}}\mapsto\tilde{Ξ}^{\mathrm{sp}}\Gamma=-i\tilde{Ξ}^{\mathrm{sp}}\vec e_z$, and it is a single right multiplication; the two entries of the pair are **not** its eigenspaces, because a left action preserves both eigenspaces of any right multiplication, so an equation between the two would force $0=m\times(\text{nonzero})$. The eigenspaces of $R_\omega$, with eigenvalues $i$ and $-i$ for $\omega=-\vec e_z$, are what the source's cell formulation projected onto, and the projection is what the migration removes.
- The composition $\mathrm{CPT}=C\circ P\circ T$ acts as $\mathrm{CPT}[\tilde{Ξ}^{\mathrm{sp}}](x)=(-\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(-x)$; it is complex-linear, reverses the argument, and its sign pattern $\mathrm{diag}(-1,+1)$ is the chirality $\Gamma$, up to the free scalar phase of the three operations. This is the one statement of the article that does not depend on the choice of conjugation.
- The gradient is a left action, so it acts on both entries with the same factor, and its square is not scalar, $\tilde\nabla^2=\partial^2/\partial Q_t^2-\Delta_Q+2e_t\sum_k\vec e_k\partial^2/(\partial Q_t\partial Q_k)$; the massive equation is therefore the pair, and the pair operator $\mathbb{D}$ of the conventions has $\mathbb{D}^2=\Box I$.
- The algebra's conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ preserve both sectors; ${}^{*}$ is $+1$ on $\mathbb{M}_+$ and $-1$ on $\mathbb{M}_-$; the sector swap is the central multiplication by $i$. No discrete operation is a sector swap.
- The algebra's three conjugations are order-two maps that commute pairwise, with $\natural=\bar{\cdot}\circ{}^{*}$, so they and the identity form a $\mathbb{Z}_2\times\mathbb{Z}_2$. This is a computation on the coefficients, and it is the one point where the classification below and the algebra meet without transcription.

**Transcribed, not derived.**

- The CPT theorem itself, and the hypotheses (locality, Hermiticity, Lorentz invariance, positivity, spin–statistics) that prove it.
- The exchange of the particle and antiparticle modes by $C$, and the anti-unitarity of the operator induced by $T$ on the mode algebra.
- The free-field computation, which is the standard one expressed in the framework's notation: the internal factors, their phases, and the massless decoupling.
- The **classification** of the operations: $P$ as one order-two map of the field, $T$ as another, $PT$ as their composite, $C$ as the twisted one, and the group $\{1,P,T,PT,C,CP,CT,CPT\}$ that they generate, which is $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ up to the sign of the product. The classification is a statement about the maps; the passage from those maps to the exchange of parts and the internal factor $\Gamma$ is representation theory that this article does not carry out.

**Gap, left visible.**

- No $\mathbb{B}$-intrinsic form of $C$ and $P$. What they need is the exchange of the two entries, and no multiplication by an element supplies it; whether the framework can realize the exchange on an enlarged structure, or only as an operation on the pair, is not built.
- No action on the S-matrix, and no treatment of $CP$ violation.
- No derivation of CPT from the algebra. Whether locality and positivity are expressible as properties of $\mathbb{B}$ in a way that yields the theorem is open.
- The massive case: the parent's mass term is the linear chiral pair, whose two-sided form is the massive Dirac equation that $C$, $P$ and $T$ were each verified to preserve; the open question is whether $C$ is a symmetry of the single-field equation built on the algebra's anti-linear real structure $\flat$, the same Majorana-versus-Dirac reading as before.

## Open Questions

1. **Is there a $\mathbb{B}$-intrinsic $C$ and $P$?** What they need is the exchange of the two entries, and no multiplication by an element supplies it. Does an enlargement of the algebra — a doubling of the field, or a module on which the exchange is inner — carry them as multiplications, or are charge conjugation and parity irreducibly external to the biquaternion structure? This is the structural counterpart of the electron article's observation that the energy-sign operator has no element.

2. **Is $C$ a symmetry of the real structure's pairing?** The algebra's real structure $\tilde{Ξ}^{\mathrm{sp}\flat}=-\tilde{Ξ}^{\mathrm{sp}*}$ is anti-linear, while the parent's mass term is the linear chiral pair, and $C$ preserves the massive pair. Whether the separate single-field equation built on the real structure is $C$-invariant, and whether that pairing is Majorana-type or a real-form Dirac mass, decide whether the framework's fermion number is conserved. The companion on the neutrino and Majorana fermions is the natural place.

3. **Can CPT be derived rather than transcribed?** The theorem follows from locality, Hermiticity, Lorentz invariance and positivity. Are any of these native to $\mathbb{B}$, or does the framework only host the notation? A derivation would be the framework's first genuine theorem of this kind.

4. **The phase of charge conjugation and the grading.** The phase of the internal factor is conventional, but $C$ and the fermion-parity element $(-1)^F$ both act on the field with a sign, and the two signs are related in the single-mode algebra. Is the phase of $C$ fixed by the requirement that $C$ commute with the grading, or is it free?

5. **Where would $CP$ violation live?** The free equation is $CP$-invariant. If the framework has a place for a complex phase in the mass or coupling structure — the Majorana question above is one candidate — does it admit the standard $CP$-violating invariants, and is there a biquaternion statement of them?

6. **Empirical contact.** The construction reproduces standard field theory. Any deviation would have to appear where the framework is used beyond transcription, for instance in the relation between the discrete operations and the mass term; none is visible at the level developed here.

7. **Do the three conjugations derive the internal factor?** The algebra's three conjugations are order-two maps that commute, and the discrete operations are assigned to them. On the field the same operations are implemented by the conjugation of the coefficients together with the exchange of the entries and the chirality sign for $C$, by the conjugation with the exchange alone for $P$, and by the conjugation with the time reflection alone for $T$. Whether a multiplication can be *read off* a conjugation — so that the internal factor is derived rather than matched — is the representation-theoretic step this article does not take. If it can be taken, the correspondences become a derivation; if it cannot, the classification remains a structural companion rather than a source.

## Summary

The biquaternion framework carries the three discrete operations on one field, $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R$, an element of $\mathbb{B}$ whose two members are the two entries of the pair, each an element in its own right. They are not the eigenspaces of the chirality: the chirality is the single right multiplication $\tilde{Ξ}^{\mathrm{sp}}\mapsto\tilde{Ξ}^{\mathrm{sp}}\Gamma$ by $\Gamma=-i\vec e_z=i\omega$, a left action preserves every eigenspace of a right multiplication, so the pair cannot be a pair of chiral projections, and the projection belongs to the cell formulation that the migration removes. Charge conjugation is the conjugation of the coefficients, applied at each point, together with the exchange of the two entries and the internal factor $\Gamma$; parity is the spatial reflection together with the exchange and no factor; time reversal is the conjugation together with the time reflection and no factor. Each was verified separately to preserve the free chiral pair $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R$, on the differential equation, for three on-shell momenta, on sixteen coefficient choices per momentum and on both frequency branches. $C$ and $T$ are anti-linear, and the operator induced by $T$ is anti-unitary; $C$ and $P$ exchange the entries, $T$ keeps them, and the composition keeps them. $C$ is not an involution: $C^2=-e_t$.

The pair is not a choice. The gradient acts by left multiplication and its square is not scalar, so the free equation stays first order in one entry, $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=0$, and the massive equation is the pair, written once as the pair operator $\mathbb{D}(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)=(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R,\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L)$ with $\mathbb{D}^2=\Box I$. The chirality commutes with the gradient and therefore appears in neither member; it is a right multiplication, one instance of the wider family of constant right multipliers that the pair admits as symmetries, and it supplies the sign pattern that $C$ and the composition carry.

The operations are kept distinct from the algebra's own conjugations. The quaternion, complex and Hermitian conjugates all preserve both sectors $\mathbb{M}_-$ and $\mathbb{M}_+$, and the Hermitian conjugate defines them; the sector swap is multiplication by the central scalar imaginary $i$, which is not a conjugation. The transition between the two sectors is therefore not the particle–antiparticle or chiral-conjugate transition; the temptation to read it so is the trap the companion articles record, and it is refuted by the fixed-point definitions. Of the three operations, only the factor of $C$ is a multiplication by an element, namely the chirality's right multiplication by $-i\vec e_z$; what $C$ and $P$ cannot get from the algebra is the exchange of the two entries, which no multiplication performs, and it is that exchange which keeps charge conjugation and parity outside the algebra's own action.

The composition was checked as a composition. Because $C$ and $T$ are anti-linear, $\mathrm{CPT}=C\circ P\circ T$ is evaluated on the field and not by multiplying absolute phases; it acts as $\mathrm{CPT}[\tilde{Ξ}^{\mathrm{sp}}](x)=(-\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(-x)$, and the sign pattern $-1$ on the first entry and $+1$ on the second is the chirality $\Gamma=-i\vec e_z=i\omega$ read on the two eigenspaces of $R_\omega$. That statement is the same under any choice of conjugation, while the individual factors of $C$ and $T$ are not. The composition is complex-linear, maps particles to antiparticles, and keeps the two entries. What the framework establishes is that the free Dirac pair carries these operations and their composition, with the anti-linearity supplied by the algebra's conjugation of the coefficients in $C$ and $T$; what it transcribes is the CPT theorem. A free-field check is not the theorem, whose content is the survival of the composition under interactions, and the intrinsic forms of $C$ and $P$ remain open.

The classification supplies a second reading of the same eight operations: they are the identity, the algebra's three conjugations $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ — three order-two maps that commute pairwise, so a $\mathbb{Z}_2\times\mathbb{Z}_2$ — and their composites with charge conjugation, and the eight form $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ up to the sign of a product. The algebra's own conjugations are the untwisted maps, while $C$ is the twisted one, which is the algebraic form of the article's finding that $C$ needs the exchange of the entries. That classification is transcribed, and the step from it to the exchange and the internal factor is left open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_j \vec e_k=\epsilon_{jkl}\vec e_l$ $(j\ne k)$ |
| $i$ | The central scalar imaginary |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | Real-quaternion subspace; centre |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=({}^{\natural})^{\,*}$ | Quaternion, complex, and Hermitian conjugations; order two, commuting pairwise, $\natural=\bar{\cdot}\circ{}^{*}$ |
| $\tilde{Q}^{\flat}=-\tilde{Q}^{*}$ | Anti-Hermitian conjugate; the algebra's real structure, $\mathbb{C}$-antilinear and order-reversing |
| $\tilde\nabla=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$, $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | Biquaternionic gradient, acting on the left, and d'Alembertian |
| $\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{Ξ}^{\mathrm{sp}}_R$ | The two entries of the pair: two elements of $\mathbb{B}$, not the eigenspaces of the chirality, which no left action can separate |
| $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R$ | The Dirac field, one element of $\mathbb{B}$; dynamics $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R$ |
| $\omega=-\vec e_z$, $\Gamma=i\omega=-i\vec e_z$ | $\omega^2=-e_t$; the chirality is the right action $\tilde{Ξ}^{\mathrm{sp}}\mapsto\tilde{Ξ}^{\mathrm{sp}}\Gamma=-i\tilde{Ξ}^{\mathrm{sp}}\vec e_z$, with $\Gamma^2=e_t$, equal to $-1$ on the eigenspace of $R_\omega$ with eigenvalue $i$ and $+1$ on the other |
| $\mathbb{D}(\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)=(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R,\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L)$ | The pair operator on $\mathbb{B}\oplus\mathbb{B}$; $\mathbb{D}^2=\Box I$; $(\mathbb{D}-m)\tilde{Ξ}^{\mathrm{sp}}=0$ is the pair |
| $\tilde K=-E_{\vec p}e_t+i\vec p$ | Symbol of $\tilde\nabla$ on $e^{-ip\cdot x}$; $\tilde K^{\natural}\tilde K=E_{\vec p}^2-\vec p^2=m^2$ |
| $J=\bar{\cdot}$, $\tilde{Ζ}^{J}$ | The conjugation of the field: the coefficient conjugation applied at each point, anti-linear and an automorphism |
| $C[\tilde{Ξ}^{\mathrm{sp}}]=(-\tilde{Ξ}^{\mathrm{sp}J}_R,\tilde{Ξ}^{\mathrm{sp}J}_L)$ | Charge conjugation (anti-linear, exchanges the entries, internal factor $\Gamma$, $C^2=-e_t$) |
| $P[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=(\tilde{Ξ}^{\mathrm{sp}}_R,\tilde{Ξ}^{\mathrm{sp}}_L)(t',-\vec x)$ | Parity (linear, exchanges the entries, no internal factor, $P^2=\mathrm{id}$) |
| $T[\tilde{Ξ}^{\mathrm{sp}}](t',\vec x)=(\tilde{Ξ}^{\mathrm{sp}J}_L,\tilde{Ξ}^{\mathrm{sp}J}_R)(-t',\vec x)$ | Time reversal (anti-linear, keeps the entries, no internal factor, $T^2=\mathrm{id}$) |
| $\mathrm{CPT}=C\circ P\circ T$ | CPT composition; $\mathrm{CPT}[\tilde{Ξ}^{\mathrm{sp}}](x)=(-\tilde{Ξ}^{\mathrm{sp}}_L,\tilde{Ξ}^{\mathrm{sp}}_R)(-x)$, the sign pattern of $\Gamma$ |
| $\{1,P,T,PT,C,CP,CT,CPT\}/\{\pm1\}\cong\mathbb{Z}_2^3$ | The group of the eight discrete operations, up to the sign of a product |

## Further Reading

- G. Lüders and B. Zumino, "Connection between Spin and Statistics," *Physical Review* **110** (1958) 1450–1453, for the general proof of the CPT theorem in the axiomatic setting.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the Wightman-axiomatic treatment from which the theorem's hypotheses — locality, positivity, Lorentz invariance — are read.
- J. J. Sakurai, *Invariance Principles and Elementary Particles* (Princeton, 1964), for the classic operator treatment of the discrete symmetries and of CPT.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the CPT theorem in the Lagrangian setting and the role of the anti-unitary operations.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac-field implementations of $C$, $P$ and $T$ used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the plane-wave amplitudes, the charge-conjugation operation and the mode exchange.
- P. K. Rashevskii, "The theory of spinors," *Uspekhi Matematicheskikh Nauk* **10** (1955) 3–110 (*American Mathematical Society Translations* (2) **6** (1957) 1–110), for the classification of the intrinsic order-two maps of the algebra, which the section above reads as the discrete operations.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the assignment of the discrete operations to the intrinsic maps of the algebra and to the charge-conjugation pseudoautomorphism, and for the group structure $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$.
- Companion articles: *Charge Conjugation and the Division Ring*; [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Spin–Statistics Theorem in Biquaternionic Form](the-spin-statistics-theorem-in-biquaternionic-form.html); [The S-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html); [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html).
