# __The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product__

## Introduction

Every value of the plain sesquilinear product $\tilde P\tilde Q^{*}$ splits into two halves, and the companion band read the first of them. This article is the first of the two articles of the second band, and it reads the **antisymmetric half**:

$$
\tilde P\wedge_{*}\tilde Q=\tfrac12\Bigl(\tilde P\tilde Q^{*}-\bigl(\tilde P\tilde Q^{*}\bigr)^{\natural}\Bigr)=\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)=-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q}.
$$

The value is a **pure vector** and the scalar part of the parent value is exactly what the subtraction removes, so the two bands of the block carry the two halves of one number: the companion band carries the central half, which the corpus reads as a **probability**, and this band carries the vector half, which the corpus reads as a **phase** or an **interference term**. The split between the two bands of the block is exactly this split.

Three facts distinguish the operation from a bilinear antisymmetrisation, and they organise the article. Its **diagonal does not vanish**: $\tilde Q\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$ is the vector part of the sesquilinear square and is a genuine quadratic condition, not an identity. Its **trace form vanishes**, so it contributes nothing to the scalar part of the algebra, in exact contrast with the companion band, which is the whole scalar form. And its **symmetry law is conjugate-alternation**, $\tilde P\wedge_{*}\tilde Q=-\overline{\tilde Q\wedge_{*}\tilde P}$, which is the antisymmetric law of the class and not the alternation of the bilinear theory. On these three facts the reading of the value as a **phase** is built, and the bound at the end of the article is that a phase is *read from* a value and is not *measured by* the operation.

**Boundaries.** The operation is *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the diagonal, its vanishing criterion and the quadric it defines, and the Jacobi failure, are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; the general construction of the two parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. The physical phases are read elsewhere and are owned elsewhere: the phase of a path is *The Path Integral in Biquaternionic Form*, the interference experiment is *The Double-Slit Experiment in Biquaternionic Form*, the geometric phase of a spin is *Geometric Phases of Non-Relativistic Spin in Biquaternionic Form* and *The Berry Phase and Geometric Phases in Biquaternionic Form*, and the phase of a polarisation is *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*. The positivity and the states are *Mass, Rank and the Positivity of the Dagger*, *The Bloch Ball as the Trace-One Slice of the Future Light Cone* and *The Ontology of the Quantum State under the Biquaternion Framework*. The other half of the same value is *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*, and the centrality of probability there is *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*.

**Conventions.** As in the companion articles and in *Conventions in the Biquaternion Universe*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$; $\tilde Q=Q_0e_0+\mathbf Q$, $Q_\mu\in\mathbb{C}$; ${}^{\natural}$ the natural conjugation, $\overline{\cdot}$ the coefficientwise one, ${}^{*}=\overline{\cdot}\circ{}^{\natural}$; $\mathrm{Sc}$ the scalar part, $\mathrm{Vect}$ the vector part, $\mathrm{Tr}=2\,\mathrm{Sc}$. The bilinear dot and cross products of vector parts are written $(\mathbf P,\mathbf Q)$ and $\mathbf P\times\mathbf Q$. The Hermitian form is $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$, the operation of the companion band is $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0$, and the operation of this band is $\tilde P\wedge_{*}\tilde Q$. A state is $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ with $\mathbf r\in\mathbb{R}^{3}$ and $\lvert\mathbf r\rvert\le1$, and a projector is $\tilde\Pi_{\pm}(\hat{\boldsymbol{\mu}})=\tfrac12(e_0\pm i\hat{\boldsymbol{\mu}})$ with $\lvert\hat{\boldsymbol{\mu}}\rvert=1$. The sectors are $\mathbb{M}_{\pm}$ and the centre is $\mathbb{C}_{\mathbb{B}}=\{\lambda e_0\}$.

## The Operation and Its Value

### Definition

The exchange that keeps the class of the plain sesquilinear product is the interchange composed with the coefficientwise conjugation of the value, equivalently the natural conjugation of the parent value, $(\tilde P\tilde Q^{*})^{\natural}=\overline{\tilde Q\tilde P^{*}}$. Its antisymmetric half is the operation of this block,

$$
\tilde P\wedge_{*}\tilde Q=\tfrac12\Bigl(\tilde P\tilde Q^{*}-\bigl(\tilde P\tilde Q^{*}\bigr)^{\natural}\Bigr)=\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr).
$$

The two halves of the parent value therefore reconstruct it,

$$
\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q=H(\tilde P,\tilde Q)e_0+\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr),
$$

a central part and a vector part. Substituting the coordinate rule of the parent product gives the value in coordinates,

$$
\tilde P\wedge_{*}\tilde Q=-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q},
$$

each term of which is a vector part, so the value is **pure vector** and the operation has image in the vector subspace $\mathrm{Vect}(\mathbb{B})$ (*Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*).

**Remark (verified).** The half-difference is the vector part of $\tilde P\tilde Q^{*}$ on $100$ random pairs, and the reconstruction $\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q$ holds identically.

### The Law

Because the second slot conjugates, the symmetry that survives the antisymmetrisation is not the alternation of the bilinear theory but the **conjugate-alternation**

$$
\tilde P\wedge_{*}\tilde Q=-\overline{\tilde Q\wedge_{*}\tilde P},
$$

the bar acting coefficientwise on the vector value. A bilinear antisymmetrisation is alternating, vanishes on the diagonal, and satisfies $\tilde P\wedge\tilde Q=-\tilde Q\wedge\tilde P$; here the coefficientwise conjugation is part of the operation, and the exchange of the arguments alone does **not** reverse the sign. This is the general phenomenon of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* read on this block, and it is why the whole bilinear vocabulary — alternation, diagonal vanishing, a Jacobi identity of the usual form — is unavailable and must be replaced.

**Remark (verified).** $\tilde P\wedge_{*}\tilde Q+\overline{\tilde Q\wedge_{*}\tilde P}=0$ on $100$ random pairs, to $<10^{-13}$.

## The Diagonal Is Not Zero

### The Vector Part of the Square

Putting $\tilde P=\tilde Q$ in the definition, the parent value $X=\tilde Q\tilde Q^{*}$ is Hermitian, $X=x_0e_0+i\mathbf x$ with $x_0$ real and $\mathbf x$ a real vector, so $X^{\natural}=x_0e_0-i\mathbf x$ and the half-difference keeps the vector part alone; hence

$$
\tilde Q\wedge_{*}\tilde Q=\mathrm{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr),
$$

the **vector part of the sesquilinear square**. Writing the element in real coordinates, $Q_0=a+ib$ and $\mathbf Q=\mathbf u+i\mathbf v$ with $a,b\in\mathbb{R}$ and $\mathbf u,\mathbf v$ real vectors,

$$
\tilde Q\wedge_{*}\tilde Q=2i\bigl(a\,\mathbf v-b\,\mathbf u+\mathbf u\times\mathbf v\bigr),
$$

a **purely imaginary vector**, quadratic and homogeneous in the real coordinates (*The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*). The diagonal is therefore not an identity but a genuine quadratic map, and its vanishing is a condition and not a law.

**Remark (verified).** The real-coordinate form was recomputed on $100$ random elements to $<10^{-13}$; $e_1+ie_2$ gives $2ie_3$ and $e_0+ie_1$ gives $2ie_1$.

### The Witness and the Vanishing Set

The witness named by the menu is $\tilde Q=e_1+ie_2$, for which $\mathbf u=e_1$, $\mathbf v=e_2$, $a=b=0$ and the cross term alone survives:

$$
(e_1+ie_2)\wedge_{*}(e_1+ie_2)=2i\,e_1\times e_2=2ie_3\neq0 .
$$

So the antisymmetric part of the block is **not zero on the diagonal**, which is the exact opposite of the two algebra rows, where the antisymmetric part is alternating and vanishes on the diagonal. The vanishing set of the diagonal is a genuine condition: $\tilde Q\wedge_{*}\tilde Q=0$ exactly when the square $\tilde Q\tilde Q^{*}$ is central, and it is a quadric cone that contains the centre and the two quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ and misses the element $e_1+ie_2$ (*The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, which owns the criterion and the quadric).

**Remark (the image of the diagonal).** The image of the map $\tilde Q\mapsto\tilde Q\wedge_{*}\tilde Q$ is the whole real three-dimensional space $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ of the purely imaginary vectors, which is the vector part of the informational sector $\mathbb{M}_{+}$. The diagonal is a surjection onto the imaginary vectors and its zeros form the quadric it carries; the two are different objects, and the mathematics article holds their distinction.

## The Vector Part as the Phase

### The Two Halves of One Amplitude

The parent value is one amplitude, and its two halves are read on two sides of the same physical question. The central half,

$$
\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0,
$$

is the number that the corpus reads as a **probability**, the real part of the Born pairing on the state side. The vector half,

$$
\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr),
$$

is the part of the same value that the exchange reverses and conjugates, and the corpus reads it as a **phase** and as the **interference term** of the pairing. This article owns the second half and does not read the first.

**Remark (what is algebraic here, and what is reading).** The algebraic facts are that the parent value is the sum of the two operations, that the first is central and positive on the diagonal, and that the second is a **pure vector**, purely imaginary on the diagonal, which the exchange sends to minus its conjugate. The identification of the first with a probability and of the second with a phase is the corpus's physical reading of the pair, stated in the two menu comments of the bands and developed in the two articles. The reading is forced in the weak sense that the central part is the only part that can carry a probability (the companion band's argument) and the vector part is the only part that reverses under the exchange, which is what a relative phase does; it is not forced in the strong sense that the algebra names a phase.

### Where the Phase Lives

The value of the operation is a **pure vector**, $\mathrm{Vect}(\tilde P\tilde Q^{*})\in\mathrm{Vect}(\mathbb{B})$, with no scalar part; its complex coordinates are general, and the **diagonal** is where the value becomes purely imaginary — exactly the central imaginary $i$ times a real vector. Those purely imaginary vectors are exactly the vector part $i\mathbb{R}^{3}$ of the informational sector $\mathbb{M}_{+}=\mathbb{R}e_0\oplus i\mathbb{R}^{3}$, and they place the two halves of a diagonal amplitude in the two parts of the coordinate at once: the **probability** is the central, $e_0$ direction, and the **coherence** is the imaginary vector $i\mathbb{R}^{3}$. On the state side the statement is sharp. For $\tilde\rho=\tfrac12(e_0+i\mathbf r)$, $\tilde\rho^{*}=\tilde\rho$, so the operation is the vector part of the square, and

$$
\tilde\rho\wedge_{*}\tilde\rho=\mathrm{Vect}\bigl(\tilde\rho^{2}\bigr)=\tfrac12\,i\,\mathbf r .
$$

The antisymmetric square of a state is its **Bloch vector**, that is the direction and the magnitude of the state's coherence, while the symmetric square of the same state is its **purity**, $\tilde\rho\circledast\tilde\rho=\tfrac12\mathrm{Tr}(\tilde\rho^{2})e_0$ (the companion band). One value, one state: a central number and an imaginary vector, purity and coherence direction.

**The purely imaginary description belongs to the diagonal alone.** The imaginary character of the value is a statement about the **self-pairing**. On $\tilde P=\tilde Q$ the value is the real-coordinate vector $2i(a\mathbf v-b\mathbf u+\mathbf u\times\mathbf v)$, a real vector times the central $i$, and it is purely imaginary. For two **different** elements the value is a general vector part and is **not** purely imaginary: its coordinates are complex and are generically nonzero in real part as well, so the purely imaginary description characterises the diagonal and not the valued pairing. A reader who writes "the value of the antisymmetric product is imaginary" without qualification describes the diagonal and not the operation.

**Remark (verified).** $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\mathbf r$ on $100$ random states, to $<10^{-13}$.

**Remark (the phase is the central imaginary, and the corpus says so).** The corpus identifies the symbol $i$ of the phase $e^{iS/\hbar}$ with the **central scalar imaginary**, places the exponent in the material sector, and records that only *relative* phases of paths are observable (*The Path Integral in Biquaternionic Form*). The vector part of the pairing is written with that same central $i$, and this is the algebraic contact between the two statements: the phase-like half of a pairing is the half that is imaginary under the natural conjugation. The contact is a consistency and not a derivation, and it is stated as such.

**Reading (the axis of the relative phase).** The value is a vector, and a vector carries a **direction**. Read as a relative datum of two states, the direction of $\tilde P\wedge_{*}\tilde Q$ is the **axis** about which the two amplitudes differ: the central half $H$ supplies the alignment of the two states, the vector half supplies the axis that separates them, and an amplitude therefore carries an alignment, a magnitude of relative phase and an axis. This is the most that can be read structurally from the value; the operation names no angle, since an angle is extracted from the axis together with the alignment, and the corpus's phase articles own that extraction.

**Caution.** The vector is a direction and not a **generator**. The companion article of the band proves that this operation raises no Lie algebra — the Jacobi identity fails — so the axis of the relative phase must not be read as an infinitesimal transformation of the state, and the word "generator" is reserved for the material half $\mathbb{M}_{-}$ of the algebra, where the bracket does close.

**Reading (the relative phase carries no current).** The caution has a physical face. A conserved current is read from a **generator**: a one-parameter group of transformations carries one Noether charge, and the framework's *absolute*, central phase is exactly such a generator — the phase $e^{-i\theta}$ is generated by the central $ie_0$, and the charge is the generator of the phase (*The Harmonic Oscillator in Biquaternionic Form*, *The Scalar Fock Space in Biquaternionic Form*). The half read here is the **relative** half of a pairing, and it generates no one-parameter group: the Jacobi identity fails, so no current is read from it and no conservation law follows. Read physically, a relative phase is a **relational** datum and carries no current, while the absolute, central phase carries the charge; the two senses of the word *phase* are separated algebraically by whether the value is central or vector and by whether the operation closes. The boundary is the framework's usual one: the algebra supplies the failure of a current for the vector half and the centrality of the generator for the central half, and it supplies neither the value of the charge nor a dynamical law.

### Interference, and the Bound

The reading of the vector part as an interference term is the reading of the corpus's interference experiment. In *The Double-Slit Experiment in Biquaternionic Form* the two route amplitudes add and the cross term $2\,\mathrm{Re}\,\mathrm{Tr}(\psi_1^{\dagger}\psi_2)$ is the interference pattern; the cross term pairs two amplitudes, and the part of a pairing that carries the relative-phase information is the vector part $\mathrm{Vect}(\tilde P\tilde Q^{*})$. The operation of this article is that pairing half. It supplies the amplitude-like vector the interference is built from; it does not supply the two paths, the measure or the action, and it does not select an outcome.

**The caution, and it is the bound of the band.** A **phase is read from a value and is not measured by the operation**. The operation returns a vector in the informational directions; a *phase angle* is a relative quantity, extracted from two such vectors and only up to the central phase, and the corpus's phase articles — geometric phases, Berry phase, Pancharatnam's phase — own the physical phases and their measurement-like readings. This article reads the algebraic half of the pairing and does not trespass on those articles' subject; in particular it does not claim that $\tilde P\wedge_{*}\tilde Q$ is an observable, and it does not claim that a failed bracket (the companion article of this band) or a vanished trace form gives a phase a dynamical law.

## The Trace Form Vanishes

**The trace form of the block is zero.** For all biquaternions the scalar part of the value vanishes,

$$
\mathrm{Sc}\bigl(\tilde P\wedge_{*}\tilde Q\bigr)=0,
$$

because each of the three terms of the coordinate rule is a vector part. The block therefore contributes **nothing** to the scalar part of the algebra, in exact contrast with the companion band, whose operation *is* the scalar form, $\mathrm{Sc}(\tilde P\circledast\tilde Q)=H(\tilde P,\tilde Q)$ (*The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). The two bands are the two extreme cases of one split: the symmetric half carries the whole central form, and the antisymmetric half carries none of it. Read physically, the probability content of the pairing is entirely in the companion band; this band carries only the phase content, and it can carry nothing else, since its value has no scalar part to carry.

## The Operation Is Not Alternating

The vocabulary of this band has to be used exactly, because the bilinear words fail one by one.

| bilinear antisymmetrisation (for example $\mathrm{APA}$) | the plain sesquilinear antisymmetrisation, this block |
|---|---|
| alternating: $\tilde P\wedge\tilde P=0$ | conjugate-alternating: $\tilde P\wedge_{*}\tilde P=\mathrm{Vect}(\tilde P\tilde P^{*})\neq0$ in general |
| $\tilde P\wedge\tilde Q=-\tilde Q\wedge\tilde P$ | $\tilde P\wedge_{*}\tilde Q=-\overline{\tilde Q\wedge_{*}\tilde P}$ |
| values in the vector subspace $\mathrm{Vect}(\mathbb{B})$ | values in the vector subspace $\mathrm{Vect}(\mathbb{B})$, purely imaginary on the diagonal |
| trace form zero | trace form zero |

The two operations share the vector-valued image and the vanishing trace form, and they differ in the diagonal and in the law. The bilinear antisymmetrisation is the cross product and closes as a Lie algebra; this block fails the Jacobi identity, which is the subject of the companion article of the band, *Interference without a Lie Algebra: the Jacobi Failure in the State Space*. The comparison with $\mathrm{APA}$ is the comparison between a bracket that closes and a bracket that does not, and it is developed there.

## Ledger

**What the operation does.**
- Carries the vector half of the plain sesquilinear amplitude: $\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q$.
- Exposes the coherence of a state on its diagonal: $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\mathbf r$, the Bloch vector times $i/2$.
- Reads the **axis** of the relative phase of two amplitudes, the central half supplying the alignment; purely imaginary on the diagonal only.
- Has values in the vector subspace $\mathrm{Vect}(\mathbb{B})$, with the image of the diagonal the purely imaginary vectors $i\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$, the vector part of the informational sector $\mathbb{M}_{+}$.

**What the operation does not do.**
- It does not carry a probability: its trace form is zero and its scalar part vanishes.
- It does not measure a phase: the value is read, and a phase angle is a relative quantity extracted from two values.
- It is not alternating, and its diagonal is not zero: the bilinear vocabulary of a cross product does not apply.
- It is a pairing and not a measurement, and it supplies no state and no dynamics.
- Its value is **purely imaginary on the diagonal only**: for two different elements the value is a general vector part and need not be purely imaginary.
- It raises **no Lie algebra**: the Jacobi identity fails, so the axis it reads is a direction and not a generator.

## Physical Readings

The imaginary part reads as interference and, on the clock, as the carrier of the phase. Its values lie in the vector subspace, so it is the part of the pairing that carries a direction, and read against the exchange it is the part the central generator moves: the phase of an amplitude is where the clock of the framework enters a measurement (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). Read on the states, the antisymmetric part is why a pairing is not a metric and why interference cannot be read off the real part alone.

## Summary

The antisymmetric plain sesqualgebra carries the **vector half** of the plain sesquilinear amplitude, $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})=-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q}$, so that $\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q$ splits one value into its **probability** half and its **phase** half. The value is a **pure vector** (no scalar part), the trace form vanishes, and the law is the **conjugate-alternation** $\tilde P\wedge_{*}\tilde Q=-\overline{\tilde Q\wedge_{*}\tilde P}$. Its **diagonal is not zero**: $\tilde Q\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})=2i(a\mathbf v-b\mathbf u+\mathbf u\times\mathbf v)$ is a quadratic condition, and the witness $e_1+ie_2$ gives $2ie_3$, the exact opposite of the two algebra rows, where the antisymmetric part is alternating. The value is **purely imaginary on the diagonal only** — the self-pairing is a real vector times the central $i$, while the pairing of two different elements is a general vector part and need not be purely imaginary — so "the antisymmetric value is imaginary" is a statement about the diagonal and not about the operation. On the state side the diagonal is the **coherence direction**, $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\mathbf r$, while the diagonal of the companion band is the purity. The reading is that the vector half of a pairing is the phase, the interference term and the **axis** of the relative phase, in the algebraic sense that it is the half reversed and conjugated by the exchange, the central half supplying the alignment; the bound is that a phase is **read from** a value and is **not measured by** the operation, that the axis is a direction and not a generator since the Jacobi identity fails, and that the physical phases remain the property of the phase articles of the corpus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | the antisymmetric part (APS); the operation of the block |
| $\tilde P\wedge_{*}\tilde Q=-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q}$ | the coordinate rule |
| $\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q$ | one amplitude, a central half and a vector half |
| $\tilde P\wedge_{*}\tilde Q=-\overline{\tilde Q\wedge_{*}\tilde P}$ | conjugate-alternation |
| $\tilde Q\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})=2i(a\mathbf v-b\mathbf u+\mathbf u\times\mathbf v)$ | the diagonal; not zero in general |
| $(e_1+ie_2)\wedge_{*}(e_1+ie_2)=2ie_3$ | the witness of the non-vanishing diagonal |
| $\mathrm{Sc}(\tilde P\wedge_{*}\tilde Q)=0$ | the trace form vanishes |
| $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\mathbf r$ | the diagonal of a state is its Bloch vector times $i/2$ |
| purely imaginary on the diagonal only | the self-pairing is $i$ times a real vector; the pairing of two distinct elements also carries a real part |
| $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ | the purely imaginary vectors; the image of the diagonal |
| $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0$ | the symmetric half, read in the companion band |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, its class and its law.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the diagonal, its vanishing criterion and the quadric.
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the pairings of the values.
- *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* (`articles_physics/the-hermitian-form-as-a-product-positivity-and-the-real-part-of-the-born-pairing.md`), the companion band of the same value.
- *Interference without a Lie Algebra: the Jacobi Failure in the State Space* (`articles_physics/interference-without-a-lie-algebra-the-jacobi-failure-in-the-state-space.md`), the companion article of the band.
- *The Double-Slit Experiment in Biquaternionic Form* (`articles_physics/the-double-slit-experiment-in-biquaternionic-form.md`), which owns the interference experiment.
- *Geometric Phases of Non-Relativistic Spin in Biquaternionic Form* (`articles_physics/geometric-phases-of-non-relativistic-spin-in-biquaternionic-form.md`) and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form* (`articles_physics/pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.md`), which own the physical phases.
- *Mass, Rank and the Positivity of the Dagger* (`articles_physics/mass-rank-and-the-positivity-of-the-dagger.md`), which owns the positivity of the companion half.
