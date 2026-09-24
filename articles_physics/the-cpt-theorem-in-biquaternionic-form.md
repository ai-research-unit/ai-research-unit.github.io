# __The CPT Theorem in Biquaternionic Form__

## Introduction

The **CPT theorem** is the statement that a relativistic quantum field theory on Minkowski space whose Lagrangian is local, Hermitian and Lorentz invariant is invariant under the composition of **charge conjugation** $C$, **parity** $P$ and **time reversal** $T$, taken in any order. Its force is that the composition survives when the factors do not: a theory may violate $C$, $P$ and $T$ separately, and even the product $CP$, while $CPT$ remains exact. The proof requires locality (fields commute or anticommute outside the light cone), the positivity of the inner product, and the spin–statistics connection, and it is one of the deepest general results of quantum field theory.

This article asks what the biquaternion framework supplies for the theorem. The framework carries **more involutions than the standard four**, and they are easy to conflate. Alongside $C$, $P$ and $T$ the algebra provides the **complex conjugate** ${}^{*}$ (conjugation of the four coefficients), the **quaternion conjugate** $\bar{\cdot}$, and the **Hermitian conjugate** ${}^{\dagger}=\bar{\cdot}^{\,*}$. Building $C$, $P$ and $T$ therefore requires more than writing three matrices: each must be separated from the algebra's own conjugations, with which it shares the operation of complex conjugation but not the operation's meaning. The known trap, recorded in the companion on the Klein–Gordon equation, is to read a conjugate pair through the two-sector split $\mathbb{M}_+/\mathbb{M}_-$ — the temptation to place a field and its conjugate one in each sector. It is a trap because *none* of the three conjugations exchanges the sectors; the sector swap is multiplication by the central scalar imaginary $i$, which is neither a conjugation nor anti-linear. That fact, and not the notation, is what forbids the identification.

The framework's Dirac field is treated here, as in the companion articles on canonical quantization and on spin–statistics, through its **spinor-module representative**. There the discrete operations are unambiguous. We build each of $C$, $P$ and $T$ explicitly, verify each one separately against the free Dirac equation, and then check the composition $CPT$ explicitly rather than inferring it from the three factors. The composition check is not redundant, for a reason that is easy to miss: $C$ and $T$ are **anti-linear**, so the internal matrix of the product is $\eta_C\eta_P^*\eta_T^*$, not $\eta_C\eta_P\eta_T$, and the two differ whenever the phases are not real.

The division between what is established and what is only transcribed is kept explicit throughout.

- **Established, and recomputed below.** The three operations on the spinor-module Dirac field,
  $$
  C[\psi]=\eta_C\,\psi^{*},\qquad
  P[\psi](t,\mathbf{x})=\gamma^0\,\psi(t,-\mathbf{x}),\qquad
  T[\psi](t,\mathbf{x})=\eta_T\,\psi^{*}(-t,\mathbf{x}),
  $$
  with $\eta_C=i\gamma^2$ and $\eta_T=\gamma^1\gamma^3$, each maps every solution of the free equation $(i\gamma^\mu\partial_\mu-m)\psi=0$ to a solution. Each was verified separately on the differential equation, on three on-shell momenta and on a superposition of both frequency branches. $T$ is anti-unitary, $T[i\psi]=-i\,T[\psi]$, so it conjugates the scalar imaginary. $C$ and $P$ anticommute with $\gamma_5$ and exchange the chiral halves; $T$ commutes with $\gamma_5$ and preserves them; hence $CPT$ preserves chirality. $C$ exchanges the two frequency branches, so at the operator level it exchanges the particle and antiparticle modes. Of the internal matrices, $T$'s factor $\gamma^1\gamma^3=-e_2$ is an even element of $\mathrm{Cl}_{1,3}^{+}\cong\mathbb{B}$ (a real quaternion), while $C$'s $i\gamma^2$ and $P$'s $\gamma^0$ are **odd** and have no representative in $\mathbb{B}$. The composition $\Theta=C\circ P\circ T$ acts as $\Theta[\psi](x)=\eta_{CPT}\,\psi(-x)$ with $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$; in the phase convention above, $\eta_{CPT}=\gamma_5=i\omega$. Here $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ is the volume element, the element the framework identifies with the biquaternion scalar imaginary, and on the Dirac module $i$ acts as $\mathrm{diag}(i,-i)=\omega$.
- **Transcribed, not derived.** The CPT theorem itself, together with the hypotheses that prove it: locality, Hermiticity of the Lagrangian, Lorentz invariance, positivity and spin–statistics. The computation below exhibits the composition as a symmetry of *one* free equation; it does not show that the composition survives interactions, which is the content of the theorem. Nothing here derives CPT from the biquaternion algebra.
- **Gap, left visible.** The framework does not fix a $\mathbb{B}$-intrinsic form of $C$ and $P$: their internal matrices are odd Clifford elements, outside $\mathbb{B}$, so they are operations of the Clifford algebra or of the module, not inner operations of the biquaternion algebra. Whether they admit a $\mathbb{B}$-intrinsic realization is unbuilt. Separately, the parent's mass term is the linear chiral pair of the Dirac article, whose spinor representative is the massive Dirac equation verified above to be $C$-invariant; the algebra's anti-linear object is the real structure $\flat=-\dagger$, a separate Majorana-type pairing, and whether $C$ is a symmetry of the single-field equation built on $\flat$ is the open reading developed in the neutrino companion.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_je_k=\epsilon_{jkl}e_l$ for $j\ne k$, and $i$ is the scalar imaginary with $i^2=-1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}=\mathbb{C}e_0$ is the center. The conjugations are $\bar{\cdot}$ (quaternion), ${}^{*}$ (complex, i.e. conjugation of the coefficients), and ${}^{\dagger}=\bar{\cdot}^{\,*}$ (Hermitian); the anti-Hermitian conjugate is $\tilde{Q}^{\flat}=-\tilde{Q}^{\dagger}$. The matrix realization is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, satisfying $\Phi(\tilde{Q}\tilde{R})=\Phi(\tilde{Q})\Phi(\tilde{R})$ and $\Phi(\tilde{Q}^{\dagger})=\Phi(\tilde{Q})^{\dagger}$. The spinor module is $S=\mathbb{C}^2$, the unique simple left $\mathbb{B}$-module, carrying the left-handed Weyl representation $(\tfrac12,0)$, and the Dirac module is $\Delta=S\oplus\bar{S}=(\tfrac12,0)\oplus(0,\tfrac12)$, $\dim_{\mathbb{C}}\Delta=4$. The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$, with $\bar{\tilde{\nabla}}=e_0\partial_{ict}-e_k\partial_k$ and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}$; the trace pairing is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, inherited unchanged. The biquaternion Dirac field is $\tilde{\Psi}:\mathbb{R}^{1,3}\to\mathbb{B}$, with massless equation $\tilde{\nabla}\tilde{\Psi}=0$ and massive equation the linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$, and its spinor-module representative $\psi$ satisfies $(i\gamma^\mu\partial_\mu-m)\psi=0$.

We use the **block representation** of the gamma matrices of the canonical-quantization and spin–statistics articles,
$$
\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad
\gamma^k=\begin{pmatrix}0&\sigma^k\\ -\sigma^k&0\end{pmatrix},\qquad
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\qquad g=\mathrm{diag}(+1,-1,-1,-1),
$$
which is unitarily equivalent to the Dirac representation used for the non-relativistic limit; the spacetime metric of the $ict$ gradient is $\eta=-g$. The chirality operator and the volume element are
$$
\gamma_5=i\,\omega=\begin{pmatrix}-I_2&0\\ 0&I_2\end{pmatrix},\qquad
\omega=\gamma^0\gamma^1\gamma^2\gamma^3=-i\gamma_5=\begin{pmatrix}iI_2&0\\ 0&-iI_2\end{pmatrix},
$$
and the framework identifies $\omega$ with the image of the scalar imaginary under $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$, so that $\gamma_5=i\omega$. A Dirac spinor is written in chiral blocks as $\psi=(\psi_L,\psi_R)^{T}$ with $\psi_L\in S$ and $\psi_R\in\bar{S}$. We work in natural units $\hbar=c=1$ except in the mass-shell relation, and borrow the plane-wave spinors $u^{(r)}(\mathbf{p}),v^{(r)}(\mathbf{p})$ and the spin sums of the solutions article unchanged.

## The Discrete Operations and the Algebra

Three different structures are in play, and the article's first task is to keep them apart.

**The Clifford algebra and its even part.** The gamma matrices generate $\mathrm{Cl}_{1,3}(\mathbb{R})$, of real dimension $16$. Its **even subalgebra** is spanned by the identity, the six bivectors $\gamma^\mu\gamma^\nu$, and the volume element $\omega$, and is isomorphic to $\mathbb{B}$; the biquaternion units correspond to spatial bivectors by
$$
e_1\mapsto\gamma^2\gamma^3,\qquad e_2\mapsto\gamma^3\gamma^1,\qquad e_3\mapsto\gamma^1\gamma^2,
$$
and the scalar imaginary to the volume element $\omega$ — the corpus's identification, which belongs to this isomorphism $\mathbb{B}\to\mathrm{Cl}_{1,3}^{+}$ and is not a statement about the matrix realization $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ used elsewhere in this article. (The ordering in the last entry is fixed by the metric $g=\mathrm{diag}(+1,-1,-1,-1)$ used here, under which $(\gamma^2\gamma^3)(\gamma^3\gamma^1)=\gamma^1\gamma^2$; the parent Dirac article's opposite metric reverses the sign of the third bivector. What matters below is only that the map is a homomorphism, and with this ordering it is one, with each image squaring to $-e_0$.) The **odd part** — the span of the individual generators $\gamma^\mu$ — is *not* contained in $\mathbb{B}$. This matters below: an even element acts on the Dirac module block-diagonally, preserving each chiral half, while an odd element acts off-diagonally and **exchanges the two chiral halves**. The chirality operator $\gamma_5$ anticommutes with every generator and hence commutes with every even element; it is a Lorentz-invariant label.

**The three conjugations of the algebra.** They are distinct maps, and they behave differently on the sectors and on the scalar imaginary:

| Map | Action on coefficients | Scalar imaginary | Effect on $S\oplus\bar S$ |
|---|---|---|---|
| Quaternion $\bar{\cdot}$ | $(Q_0,Q_k)\mapsto(Q_0,-Q_k)$ | $i\mapsto i$ | real-linear, anti-automorphism |
| Complex ${}^{*}$ | $Q_\mu\mapsto Q_\mu^{*}$ | $i\mapsto -i$ | the real structure relating $S$ to $\bar{S}$ |
| Hermitian ${}^{\dagger}=\bar{\cdot}^{\,*}$ | $(Q_0,Q_k)\mapsto(Q_0^{*},-Q_k^{*})$ | $i\mapsto -i$ | $+1$ on $\mathbb{M}_+$, $-1$ on $\mathbb{M}_-$ |

All three **preserve each sector** $\mathbb{M}_-$ and $\mathbb{M}_+$. The map that exchanges the sectors is not a conjugation at all: it is multiplication by the central scalar imaginary,
$$
i\,\mathbb{M}_-= \mathbb{M}_+,\qquad i\,\mathbb{M}_+= \mathbb{M}_-,
$$
and $i$ commutes with everything, so it is neither an anti-linear map nor an involution of the kind a discrete symmetry needs. This is the precise content of the trap: a conjugate pair of fields cannot be assigned one member to each sector, because conjugation preserves the sectors and the sector swap is a central phase rotation. It is worth recording separately that chirality is *also* not the sector split: the chiral decomposition lives on the four-dimensional Dirac module $\Delta=S\oplus\bar{S}$ and is a module decomposition, while the sector decomposition lives on the eight-dimensional algebra $\mathbb{B}$ and is an algebra decomposition; they share no projector.

**The discrete operations are module operations.** $C$, $P$ and $T$ act on the Dirac spinor, not on the algebra element. Their internal matrices are drawn from the Clifford algebra, and the three cases differ:

- $T$ has internal matrix $\gamma^1\gamma^3=-\gamma^3\gamma^1=-e_2$, an **even** element, i.e. a biquaternion (a real quaternion, in $\mathbb{H}_{\mathbb{B}}$). Its module action is left multiplication by an element of $\mathbb{B}$.
- $C$ and $P$ have internal matrices $i\gamma^2$ and $\gamma^0$, both **odd**: they are not elements of $\mathbb{B}$, and they exchange the chiral halves. Charge conjugation and parity are therefore not inner operations of the biquaternion algebra.

None of the three is a sector swap, and none of them needs the sector split to be stated.

## The Three Operations Built Explicitly

Let $\psi$ solve the free Dirac equation $(i\gamma^\mu\partial_\mu-m)\psi=0$. A discrete operation is a map $\psi\mapsto\psi'$ whose output also solves the equation. We take the operations in the standard form: $C$ is local and anti-linear, $P$ is a spatial reflection and linear, $T$ is a time reflection and anti-linear. Each is defined by an internal matrix $\eta$ fixed by the requirement that the transformed field satisfy the same equation, and the requirement determines $\eta$ up to a phase, which is a convention.

### Charge conjugation

Define
$$
C[\psi]=\eta_C\,\psi^{*},\qquad \eta_C=i\gamma^2 .
$$
Then
$$
(i\gamma^\mu\partial_\mu-m)\,C[\psi]
=\eta_C\Big(i\,\eta_C^{-1}\gamma^\mu\eta_C\,\partial_\mu-m\Big)\psi^{*},
$$
while the complex conjugate of the Dirac equation is $(-i\gamma^{\mu*}\partial_\mu-m)\psi^{*}=0$. The two agree, so that $C[\psi]$ solves the equation, precisely when
$$
\eta_C^{-1}\gamma^\mu\eta_C=-\gamma^{\mu*},\qquad\text{equivalently}\qquad \eta_C\gamma^{\mu*}\eta_C^{-1}=-\gamma^\mu .
$$
For the block gamma matrices, $\gamma^{0*}=\gamma^0$, $\gamma^{1*}=\gamma^1$, $\gamma^{2*}=-\gamma^2$, $\gamma^{3*}=\gamma^3$, and $\eta_C=i\gamma^2$ satisfies the identity (the central $i$ is inert in it). Since $\eta_C$ is odd, $C$ anticommutes with $\gamma_5$: charge conjugation flips chirality. And since $\psi^{*}$ enters, $C$ is anti-linear.

### Parity

Define
$$
P[\psi](t,\mathbf{x})=\eta_P\,\psi(t,-\mathbf{x}),\qquad \eta_P=\gamma^0 .
$$
Only the spatial derivatives change sign, and
$$
(i\gamma^\mu\partial_\mu-m)\,P[\psi]
=\eta_P\Big(i\,\eta_P^{-1}\gamma^0\eta_P\,\partial_0
-i\,\eta_P^{-1}\gamma^k\eta_P\,\partial_k-m\Big)\psi(t,-\mathbf{x}),
$$
so $P[\psi]$ solves the equation when
$$
\eta_P^{-1}\gamma^0\eta_P=\gamma^0,\qquad \eta_P^{-1}\gamma^k\eta_P=-\gamma^k ,
$$
i.e. when $\eta_P$ commutes with $\gamma^0$ and anticommutes with each $\gamma^k$. The choice $\eta_P=\gamma^0$ works. Parity is linear, and since $\eta_P$ is odd it anticommutes with $\gamma_5$: parity flips chirality.

### Time reversal

Define
$$
T[\psi](t,\mathbf{x})=\eta_T\,\psi^{*}(-t,\mathbf{x}),\qquad \eta_T=\gamma^1\gamma^3 .
$$
The time derivative changes sign, the spatial derivatives do not, and the field is conjugated:
$$
(i\gamma^\mu\partial_\mu-m)\,T[\psi]
=\eta_T\Big(-i\,\eta_T^{-1}\gamma^0\eta_T\,\partial_0
+i\,\eta_T^{-1}\gamma^k\eta_T\,\partial_k-m\Big)\psi^{*},
$$
evaluated at $(-t,\mathbf{x})$, to be matched against the conjugate equation at the same argument. This requires
$$
\eta_T^{-1}\gamma^0\eta_T=\gamma^{0*},\qquad
\eta_T^{-1}\gamma^k\eta_T=-\gamma^{k*} .
$$
With the reality of $\gamma^0,\gamma^1,\gamma^3$ and the pure imaginary character of $\gamma^2$, these say that $\eta_T$ commutes with $\gamma^0$ and $\gamma^2$ and anticommutes with $\gamma^1$ and $\gamma^3$; the choice $\eta_T=\gamma^1\gamma^3$ works. Since $\eta_T$ is even, $T$ commutes with $\gamma_5$: time reversal preserves chirality.

### $T$ is anti-unitary

The conjugation in $T$ is not a calculational convenience; it is the definition of anti-unitarity. With $i$ the scalar imaginary,
$$
T[i\psi]=\eta_T(i\psi)^{*}=\eta_T(-i)\psi^{*}=-i\,\eta_T\psi^{*}=-i\,T[\psi].
$$
An anti-linear map with this property conjugates the scalar imaginary, and this is the sense in which $T$ is anti-unitary and $C$, which is also anti-linear, is not: $C$ does not carry a time reflection, and in the standard classification the anti-unitary discrete symmetry is $T$. The framework's single scalar imaginary $i$ — the same $i$ that appears in the $ict$ gradient and in the volume element $\omega$ — is exactly what the conjugation negates. We record this because a time reversal written without the conjugation (as $T:\psi\mapsto\eta_T\psi(-t,\mathbf{x})$) is a different, linear map, and is *not* a symmetry of the Dirac equation.

The three operations are collected below. The last column records the chirality action that follows from the parity of the internal matrix.

| Operation | Action on $\psi$ | $\eta$ | Linear? | Chirality |
|---|---|---|---|---|
| $C$ | $\eta_C\,\psi^{*}(x)$ | $i\gamma^2$ (odd) | anti-linear | flips |
| $P$ | $\eta_P\,\psi(t,-\mathbf{x})$ | $\gamma^0$ (odd) | linear | flips |
| $T$ | $\eta_T\,\psi^{*}(-t,\mathbf{x})$ | $\gamma^1\gamma^3=-e_2$ (even) | anti-linear | preserves |

Two remarks on conventions. First, the phases of $\eta_C$ and $\eta_T$ are not fixed by the requirement that the equation be preserved; only the intertwining identities are, and they fix the internal matrix only up to an arbitrary nonzero complex multiple. The companion on the electron uses $C=i\gamma^2\gamma^0$ acting on $\bar{\psi}^{T}$, which corresponds to $\eta_C=i\gamma^2$ here, and we follow that alignment. Second, the individual phases are not observable; what is observable is the composition, and changing a phase changes the internal factor of the composition, which is why the composition must be checked independently (next section).

## Each Operation Preserves the Free Equation

The verification was carried out on the differential equation itself, not only on a momentum-space identity, and on cases other than the one that suggested the definitions. The working field was the general solution
$$
\psi=(\not p+m)\chi\,e^{-ip\cdot x}+(\not p-m)\chi'\,e^{+ip\cdot x},
\qquad p\cdot x=E_{\mathbf p}t-\mathbf{p}\cdot\mathbf{x},\quad E_{\mathbf p}^2=\mathbf{p}^2+m^2,
$$
with $\not p=\gamma^0E_{\mathbf p}-\boldsymbol{\gamma}\cdot\mathbf{p}$ and $\chi,\chi'$ arbitrary constant spinors; the first branch is positive-frequency and the second negative-frequency, and their sum is a general solution of the free equation by linearity. Substituting, conjugating and reflecting as the definitions require, the residual $(i\gamma^\mu\partial_\mu-m)$ acting on each transform was reduced symbolically and found to vanish. The checks were run for the three parameter sets
$$
(m,\mathbf{p})=(3,(1,2,2)),\qquad (5,(3,4,0)),\qquad (\tfrac{7}{2},(1,0,-2)),
$$
each with the corresponding $E_{\mathbf p}=+\sqrt{\mathbf p^2+m^2}$, and with both frequency branches present simultaneously. All three operations passed on all three cases.

The individual checks are worth a word each, because they test different parts of the structure.

- **$C$.** The identity $\eta_C\gamma^{\mu*}\eta_C^{-1}=-\gamma^\mu$ was verified as a $4\times4$ matrix identity for all four $\mu$, and the transformed field was confirmed to solve the equation. The same computation identifies *which* solution the transform produces: for a positive-frequency amplitude $u=(\not p+m)\chi$,
  $$
  \eta_C\,u^{*}=i\gamma^2(\not p^{*}+m)\chi^{*}=i(-\not p+m)\gamma^2\chi^{*}
  =-i\,(\not p-m)\,\gamma^2\chi^{*},
  $$
  a negative-frequency amplitude. So $C$ exchanges the two branches; in the mode expansion it exchanges the particle operator $\hat a$ with the antiparticle operator $\hat b$, which is the operator-level statement that the conserved charge reverses sign. This was checked on the same three cases.
- **$P$.** The commutator/anticommutator conditions on $\eta_P$ were verified for $\mu=0$ and $k=1,2,3$, and the reflected field was confirmed to solve the equation. The transform keeps the positive-frequency branch positive-frequency and reverses the momentum, $\mathbf{p}\mapsto-\mathbf{p}$.
- **$T$.** The two intertwining conditions were verified, and the conjugated-reflected field was confirmed to solve the equation. Because $T$ is anti-linear, the check on the superposition is the sharpest one: a linear map that ignored the conjugation would send the negative-frequency branch to the wrong sign.

Two negative results belong here, to prevent a future pass from claiming more than was checked.

- The verification is of the **free** equation. Nothing was checked for a field with a local interaction, and no claim is made there. The reason the free check cannot be promoted is stated at the end of this article: the CPT theorem is precisely the statement that the composition survives interactions when the factors do not, and a free-field identity contains no information about that.
- The operation $T$ was *not* defined as the linear map $\psi\mapsto\eta_T\psi(-t,\mathbf{x})$ that is sometimes written. That map does not preserve the equation; the check was performed with the conjugation present.

## The Algebra's Conjugations Are Not the Discrete Operations

The temptation that the trap names is to identify one of the operations $C$, $P$, $T$ with one of the algebra's conjugations, or to read the particle–antiparticle pair as the sector pair. Three independent facts close the identification.

**First, the conjugations preserve both sectors.** For a general element $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, membership in $\mathbb{M}_-$ means $Q_0$ purely imaginary and $Q_1,Q_2,Q_3$ real, and membership in $\mathbb{M}_+$ means $Q_0$ real and $Q_1,Q_2,Q_3$ purely imaginary. Each of $\bar{\cdot}$, ${}^{*}$ and ${}^{\dagger}$ maps either condition to itself: conjugation negates the scalar or the vector coefficients but does not interchange the two patterns. The Hermitian conjugate is the identity on $\mathbb{M}_+$ and minus the identity on $\mathbb{M}_-$, so it *defines* the sectors rather than exchanging them. The map that interchanges them is $i\,\mathbb{M}_\pm=\mathbb{M}_\mp$, and $i$ is central, hence not a conjugation and not anti-linear. A particle–antiparticle or chiral-conjugate pair therefore cannot be placed one member in each sector.

**Second, the sector split and the chirality split are different decompositions of different objects.** The chiral projectors $P_{L,R}=\tfrac12(I_4\mp\gamma_5)$ act on the Dirac module $\Delta=S\oplus\bar S$ of complex dimension four. The sector projectors act on the algebra $\mathbb{B}$ of real dimension eight. They share no projector, and the electron article reaches the same conclusion from the physical side. Recorded here only because a reader who has just seen $C$ and $P$ exchange the chiral halves might try to read that exchange as a sector exchange; it is not one.

**Third, the operations are module maps, and only $T$'s internal matrix belongs to the algebra.** $T$'s factor $\gamma^1\gamma^3=-e_2$ lies in $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$ and acts by left multiplication; $C$'s $i\gamma^2$ and $P$'s $\gamma^0$ are odd and act off-diagonally, exchanging $S$ and $\bar{S}$. The odd part of $\mathrm{Cl}_{1,3}$ is not contained in the even subalgebra, so $C$ and $P$ have no representative in $\mathbb{B}$. This is the sharp form of the framework's difficulty with the discrete operations: the algebra contains the operations that preserve chirality ($T$, and the even Lorentz action) and does not contain those that exchange it ($C$ and $P$). The electroweakly relevant fact that $C$ and $P$ are precisely the operations Nature violates separately, while their product with $T$ is the one that survives, is not explained by this structure; it is the theorem's content, and it is imported.

The anti-linear part of $C$ and of $T$ is exactly the algebra's complex conjugation ${}^{*}$. This is the same real-structure operation that relates $S$ to $\bar S$ and that distinguishes the two chiral halves inside the simple algebra, and it is what supplies the anti-linear part of the discrete operations. It is *not* the mass. The parent's mass term is the linear chiral pair of the Dirac article, and the algebra's anti-linear real structure $\flat=-\dagger$ is a separate, order-reversing conjugation whose pairing is a Majorana-type coupling. The discrete operations are symmetries of the kinetic equation; the real structure is a dynamical pairing.

## The Composition CPT, Checked as a Composition

Compose the three operations in the order $C$, then $P$, then $T$, and write $\Theta=C\circ P\circ T$. Because $C$ and $T$ are anti-linear, the composition must be evaluated as a composition, not by multiplying the three internal matrices. Applied to a field $\psi$,
$$
\psi\xrightarrow{\;T\;}\eta_T\,\psi^{*}(-t,\mathbf{x})
\xrightarrow{\;P\;}\eta_P\eta_T\,\psi^{*}(-t,-\mathbf{x})
\xrightarrow{\;C\;}\eta_C\big(\eta_P\eta_T\big)^{*}\psi(-t,-\mathbf{x}),
$$
so that
$$
\Theta[\psi](x)=\eta_{CPT}\,\psi(-x),\qquad
\eta_{CPT}=\eta_C\,\eta_P^{*}\,\eta_T^{*}.
$$
The internal factor is built from the **conjugates** of $\eta_P$ and $\eta_T$, which is the bookkeeping that a naive product $\eta_C\eta_P\eta_T$ would miss. In the convention of this article, $\eta_P=\gamma^0$ and $\eta_T=\gamma^1\gamma^3$ are real, so $\eta_P^{*}=\eta_P$ and $\eta_T^{*}=\eta_T$, and
$$
\eta_{CPT}=\eta_C\eta_P\eta_T=i\gamma^2\gamma^0\gamma^1\gamma^3=i\omega=\gamma_5 .
$$
The agreement with the naive product in *this* convention is an accident of real internal matrices and should not be taken as general. If, for example, the phase convention $\eta_T=i\gamma^1\gamma^3$ is used — equally admissible, since the equation-preservation condition leaves the phase of the internal matrix free — then the true composition has $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}=\omega$, while the naive product gives $i\omega=-\omega$. The two differ by a sign. The operation $T$ and the composition were re-verified in that convention as well, and both still map solutions to solutions; the point is that the internal factor is a convention-dependent phase and can only be read off from the composition itself. This is the concrete sense in which verifying $C$, $P$, $T$ individually and multiplying is not the same as verifying $CPT$.

The composition has the following verified properties.

- **It is a symmetry of the free equation.** $\Theta[\psi]$ solves $(i\gamma^\mu\partial_\mu-m)\psi=0$ whenever $\psi$ does. This was checked on all three parameter sets and with both frequency branches present.
- **It is complex-linear.** $\Theta[i\psi]=+i\,\Theta[\psi]$: the two anti-linear factors $C$ and $T$ combine into a linear map on the field, since $\Theta[\psi](x)=\eta_{CPT}\psi(-x)$ carries no conjugation. (The standard $CPT$ *operator* on the mode algebra is anti-unitary; that operator is not constructed here, and it is the field map that this article defines.)
- **It reverses both the spacetime argument and the charge.** The argument is $-x$, and because $C$ exchanges the frequency branches, a particle is mapped to an antiparticle.
- **It preserves chirality.** $C$ and $P$ each flip chirality and $T$ preserves it; the composition flips it twice. Equivalently, $\eta_{CPT}=i\omega$ commutes with $\gamma_5$, consistent with the fact that $\eta_{CPT}$ is an even element of the Clifford algebra.
- **Its internal factor is (a phase times) the volume element.** $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ is the element the framework identifies with the scalar imaginary $i$. On the defining module $S$ the central imaginary acts as $iI_2$; on the Dirac module $\Delta=S\oplus\bar S$, whose right-handed half carries the conjugate action, the same central element acts as $\mathrm{diag}(i,-i)=\omega$. So on the Dirac module the internal factor of $CPT$ *is* the scalar imaginary, up to the phase carried by the convention for $\eta_C$ and $\eta_T$. Equivalently, with the phase above, it is the chirality operator $\gamma_5=i\omega$. We state it in both forms because the equality $\eta_{CPT}=\pm\omega$ is a statement about the algebra while $\eta_{CPT}=\pm\gamma_5$ is a statement about the module, and the two are related by $i$.

**What this does and does not establish.** It establishes that the free biquaternion Dirac equation carries three discrete operations whose composition is a symmetry, that the composition's internal factor is the scalar imaginary up to a phase, and that the anti-linearity resides in the factors $C$ and $T$ alone, where it is the algebra's complex conjugation ${}^{*}$; the parent's mass term is linear, so the discrete antilinearity is not shared with it.

It does **not** establish the CPT theorem. A free equation is a special case in which $C$, $P$ and $T$ are separately symmetries, so the composition is a symmetry for the trivial reason. The theorem's content is that $CPT$ remains a symmetry when $C$, $P$ and $T$ do not, and that statement rests on locality, Hermiticity, Lorentz invariance and spin–statistics, none of which is derived here. The correct summary is that the framework *exhibits* CPT on the free field and *transcribes* the theorem.

## Relation to the Companion Articles

- **The S-matrix.** The companion raises as an open question the biquaternion realization of the anti-unitary discrete symmetries, and locates it in "the planned companions on CPT and on the discrete symmetries". This article answers part of that: it gives the anti-unitary $T$ and the composition $CPT$ on the free spinor-module field, with the anti-linearity identified with the algebra's ${}^{*}$. It does not give the action on the S-matrix.
- **Spin–statistics.** That article establishes that the spinor module is the carrier of the double-valued representation and that the fermionic bracket is imposed; the discrete operations here act on the same module and are insensitive to the bracket. The anti-unitarity of $T$ is the one place where the complex structure of the module enters the discrete symmetries directly.
- **Chiral fermions.** That article's real structure — the conjugation relating $S$ to $\bar S$ — is exactly the ${}^{*}$ that supplies the anti-linear part of $C$ and $T$; the framework's mass term, now the linear chiral pair, is not built on it. The present article adds that $C$ and $P$ flip chirality, $T$ preserves it, and $CPT$ preserves it: the discrete operations do not mix the chirality question with the sector question, and the two decompositions remain distinct.

- **Canonical quantization.** The mode expansion there gives the operator-level reading of $C$: because $\eta_Cu^{*}$ is a negative-frequency amplitude, $C$ exchanges $\hat a$ and $\hat b$ and reverses the normal-ordered charge. This is the operator form of the classical statement.
- **The electron.** That article's charge conjugation, generated by $C=i\gamma^2\gamma^0$ on $\bar\psi^{T}$, is the matrix convention aligned with $\eta_C=i\gamma^2$ here, and its observation that the energy-sign projector $\gamma^0$ is an odd Clifford element with no representative in $\mathbb{B}$ is the same odd/even distinction that governs the table above.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The three operations $C[\psi]=i\gamma^2\psi^{*}$, $P[\psi]=\gamma^0\psi(t,-\mathbf{x})$ and $T[\psi]=\gamma^1\gamma^3\psi^{*}(-t,\mathbf{x})$ each preserve the free Dirac equation, verified on the differential equation for three on-shell momenta and on a superposition of both frequency branches.
- $T$ is anti-unitary, $T[i\psi]=-i\,T[\psi]$; $C$ is anti-linear; $P$ is linear.
- $C$ and $P$ anticommute with $\gamma_5$ and exchange the chiral halves; $T$ commutes with $\gamma_5$; $CPT$ preserves chirality.
- $C$ exchanges the frequency branches, hence the particle and antiparticle modes.
- Of the internal matrices, $\gamma^1\gamma^3=-e_2$ is even and belongs to $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$, while $i\gamma^2$ and $\gamma^0$ are odd and do not belong to $\mathbb{B}$.
- The algebra's conjugations $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger}$ preserve both sectors; ${}^{\dagger}$ is $+1$ on $\mathbb{M}_+$ and $-1$ on $\mathbb{M}_-$; the sector swap is the central multiplication by $i$. No discrete operation is a sector swap.
- The composition $\Theta=C\circ P\circ T$ acts as $\eta_{CPT}\psi(-x)$ with $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$, verified as a composition; in the aligned convention $\eta_{CPT}=i\omega=\gamma_5$, with $\omega$ the volume element identified with the scalar imaginary. The naive product differs from the true composition once the phases are not real.

**Transcribed, not derived.**

- The CPT theorem itself, and the hypotheses (locality, Hermiticity, Lorentz invariance, positivity, spin–statistics) that prove it.
- The internal factors and phases of $C$ and $T$, which are the standard Clifford-algebra objects; the free-field computation is the standard one expressed in the framework's module and notation.
- The intertwiners, which are the standard relations $\eta_C\gamma^{\mu*}\eta_C^{-1}=-\gamma^\mu$ and their analogues.

**Gap, left visible.**

- No $\mathbb{B}$-intrinsic form of $C$ and $P$. Because their internal matrices are odd, they cannot be inner operations of $\mathbb{B}$; whether the framework can realize them on an enlarged structure, or only on the Clifford algebra or the module, is not built.
- No action on the S-matrix, and no treatment of $CP$ violation.
- No derivation of CPT from the algebra. Whether locality and positivity are expressible as properties of $\mathbb{B}$ in a way that yields the theorem is open.
- The massive case: the parent's mass term is the linear chiral pair, whose spinor representative is the massive Dirac equation that $C$, $P$ and $T$ were each verified to preserve; the open question is whether $C$ is a symmetry of the single-field equation built on the algebra's antilinear real structure $\flat$, the same Majorana-versus-Dirac reading as before.

## Open Questions

1. **Is there a $\mathbb{B}$-intrinsic $C$ and $P$?** Their internal matrices are odd and outside $\mathbb{B}$. Does an enlargement of the algebra (a Clifford or module extension) carry them as inner operations, or are charge conjugation and parity irreducibly external to the biquaternion structure? This is the structural counterpart of the electron article's observation that the energy-sign projector has no representative in $\mathbb{B}$.

2. **Is $C$ a symmetry of the real structure's pairing?** The algebra's real structure $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$ is anti-linear, while the parent's mass term is the linear chiral pair, and $C$ preserves the massive spinor equation. Whether the separate single-field equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ built on the real structure is $C$-invariant, and whether that pairing is Majorana-type or a real-form Dirac mass, decide whether the framework's fermion number is conserved. The companion on the neutrino and Majorana fermions is the natural place.

3. **Can CPT be derived rather than transcribed?** The theorem follows from locality, Hermiticity, Lorentz invariance and positivity. Are any of these native to $\mathbb{B}$, or does the framework only host the notation? A derivation would be the framework's first genuine theorem of this kind.

4. **The phase of the charge-conjugation matrix and the grading.** The phase of $\eta_C$ is conventional, but $C$ and the fermion-parity element $(-1)^F$ both act on the field with a sign, and the two signs are related in the single-mode algebra. Is the phase of $\eta_C$ fixed by the requirement that $C$ commute with the grading, or is it free?

5. **Where would $CP$ violation live?** The free equation is $CP$-invariant. If the framework has a place for a complex phase in the mass or coupling structure — the Majorana question above is one candidate — does it admit the standard $CP$-violating invariants, and is there a biquaternion statement of them?

6. **Empirical contact.** The construction reproduces standard field theory. Any deviation would have to appear where the framework is used beyond transcription, for instance in the relation between the discrete operations and the mass term; none is visible at the level developed here.

## Summary

The biquaternion framework carries the three discrete operations on its spinor-module Dirac field. Charge conjugation is $C[\psi]=i\gamma^2\psi^{*}$; parity is $P[\psi](t,\mathbf{x})=\gamma^0\psi(t,-\mathbf{x})$; time reversal is $T[\psi](t,\mathbf{x})=\gamma^1\gamma^3\psi^{*}(-t,\mathbf{x})$. Each was verified separately to preserve the free equation $(i\gamma^\mu\partial_\mu-m)\psi=0$, on the differential equation, for three on-shell momenta and on a superposition of both frequency branches. Time reversal is anti-unitary, $T[i\psi]=-i\,T[\psi]$, and so conjugates the framework's scalar imaginary. Charge conjugation and parity anticommute with $\gamma_5$ and exchange the chiral halves; time reversal commutes with $\gamma_5$; the composition preserves chirality.

The operations are kept distinct from the algebra's own conjugations. The quaternion, complex and Hermitian conjugates all preserve both sectors $\mathbb{M}_-$ and $\mathbb{M}_+$, and the Hermitian conjugate defines them; the sector swap is multiplication by the central scalar imaginary $i$, which is not a conjugation. The transition between the two sectors is therefore not the particle–antiparticle or chiral-conjugate transition; the temptation to read it so is the trap the companion articles record, and it is refuted by the fixed-point definitions. Of the internal matrices, only $\gamma^1\gamma^3=-e_2$ is even and belongs to the biquaternion algebra; $i\gamma^2$ and $\gamma^0$ are odd, so charge conjugation and parity are operations of the Clifford algebra and the module, not inner operations of $\mathbb{B}$.

The composition was checked as a composition. Because $C$ and $T$ are anti-linear, $\Theta=C\circ P\circ T$ has internal factor $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$, equal to $i\omega=\gamma_5$ in the convention used here, where $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ is the volume element the framework identifies with the scalar imaginary. The composition is complex-linear, maps particles to antiparticles, and preserves chirality. What the framework establishes is that the free Dirac equation carries these operations and their composition, with the anti-linearity supplied by the algebra's complex conjugation in $C$ and $T$; what it transcribes is the CPT theorem. A free-field check is not the theorem, whose content is the survival of the composition under interactions, and the $\mathbb{B}$-intrinsic forms of $C$ and $P$ remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ $(j\ne k)$ |
| $i$ | Scalar imaginary, $i^2=-1$; the matrix realization gives $iI_2$ on the module, and the Clifford isomorphism $\mathbb{B}\to\mathrm{Cl}_{1,3}^{+}$ (a different map from $\Phi$) sends it to $\omega$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | Real-quaternion subspace; center |
| $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger}=\bar{\cdot}^{\,*}$ | Quaternion, complex, and Hermitian conjugations |
| $\tilde{Q}^{\flat}=-\tilde{Q}^{\dagger}$ | Anti-Hermitian conjugate; the algebra's real structure, $\mathbb{C}$-antilinear and order-reversing |
| $\Phi(e_k)=-i\sigma_k,\ \Phi(i)=iI_2$ | Matrix realization, $\Phi(\tilde{Q}^{\dagger})=\Phi(\tilde{Q})^{\dagger}$ |
| $S=\mathbb{C}^2=(\tfrac12,0)$, $\bar{S}=(0,\tfrac12)$, $\Delta=S\oplus\bar{S}$ | Spinor module, conjugate, Dirac module |
| $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$, $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ | Biquaternionic gradient and d'Alembertian |
| $\tilde{\Psi}$, $\tilde{\Psi}^{\flat}$ | Biquaternion Dirac field and its anti-Hermitian conjugate |
| $\psi=(\psi_L,\psi_R)^{T}$ | Spinor-module representative; $(i\gamma^\mu\partial_\mu-m)\psi=0$ |
| $\gamma^\mu$, $g=\mathrm{diag}(+1,-1,-1,-1)$ | Block gamma matrices and Clifford metric; $\eta=-g$ |
| $\not p=\gamma^0E_{\mathbf p}-\boldsymbol{\gamma}\cdot\mathbf{p}$ | Feynman slash; $p\cdot x=E_{\mathbf p}t-\mathbf{p}\cdot\mathbf{x}$ |
| $\gamma_5=i\omega$, $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ | Chirality operator and volume element; $\eta_{CPT}=i\omega=\gamma_5$ |
| $P_{L,R}=\tfrac12(I_4\mp\gamma_5)$ | Chiral projectors |
| $u^{(r)}(\mathbf{p}),v^{(r)}(\mathbf{p})$ | Positive- and negative-frequency spinors (solutions article) |
| $C[\psi]=i\gamma^2\psi^{*}$ | Charge conjugation (anti-linear); $\eta_C\gamma^{\mu*}\eta_C^{-1}=-\gamma^\mu$ |
| $P[\psi]=\gamma^0\psi(t,-\mathbf{x})$ | Parity (linear); $\eta_P^{-1}\gamma^0\eta_P=\gamma^0$, $\eta_P^{-1}\gamma^k\eta_P=-\gamma^k$ |
| $T[\psi]=\gamma^1\gamma^3\psi^{*}(-t,\mathbf{x})$ | Time reversal (anti-unitary); $\gamma^1\gamma^3=-e_2$ |
| $\Theta=C\circ P\circ T$ | CPT composition; $\Theta[\psi](x)=\eta_{CPT}\psi(-x)$ |
| $\eta_{CPT}=\eta_C\eta_P^{*}\eta_T^{*}$ | Internal factor of the composition |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing of the informational sector |

## Further Reading

- G. Lüders and B. Zumino, "Connection between Spin and Statistics," *Physical Review* **110** (1958) 1450–1453, for the general proof of the CPT theorem in the axiomatic setting.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the Wightman-axiomatic treatment from which the theorem's hypotheses — locality, positivity, Lorentz invariance — are read.
- J. J. Sakurai, *Invariance Principles and Elementary Particles* (Princeton, 1964), for the classic operator treatment of the discrete symmetries and of CPT.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the CPT theorem in the Lagrangian setting and the role of the anti-unitary operations.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac-field implementations of $C$, $P$ and $T$ used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the plane-wave spinors, the charge-conjugation matrix and the mode exchange.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the even/odd structure of $\mathrm{Cl}_{1,3}$ and the volume element.
- Companion articles: *Canonical Quantization of the Biquaternion Dirac Field*; *The Spin–Statistics Theorem in Biquaternionic Form*; *The S-Matrix in Biquaternionic Form*; *Chiral Fermions in the Biquaternion Framework*; *The Electron in Biquaternionic Form*; *The Dirac Equation in Biquaternionic Form*; *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*; *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; *Exercise: Chirality and the Weyl Spinors*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *The Gauge Principle in Biquaternionic Form*; *The KMS Condition and the Biquaternion Framework*.
