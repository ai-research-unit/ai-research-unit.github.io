# __The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, and the one this article is about is the **plain sesquilinear** product $\tilde P\tilde Q^{*}$: the ordinary product with the second factor read through the Hermitian conjugation ${}^{*}$. It is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, and it is the product of the state row of the framework. This article is the first of the two articles of its band, and it reads the product's **symmetric half**.

The symmetric half is the central part of the value, and the single structural claim of the article is that this half is the **Hermitian form of the corpus read as a multiplication**:

$$
\tilde P\circledast\tilde Q=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)e_0=H(\tilde P,\tilde Q)e_0,\qquad H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q}).
$$

Three facts organise the band. The value is **central**, so the operation is a form and not a genuine multiplication; its diagonal is **real and strictly positive off the origin**, so this is the row the corpus reads as probability; and it is the row whose second slot conjugates, so its law is conjugate-commutative and its operation has no unit on either side. The companion article of the band, *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*, owns the centrality, the idempotents of the operation and the cone of its values; this article owns the operation itself, its positivity, the failure of the Jordan identity, and the reading of its value as the real part of the Born pairing.

**Boundaries.** The product that is split is *Introduction to the General Plain Sesqualgebra of Biquaternions*; the split itself and the general construction of the two parts are *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and both are cited and not restated. The positivity of $H$, its cone and its signature are *Mass, Rank and the Positivity of the Dagger* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, and the algebra of the operation is *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* and *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*. The Born rule as a trace formula and the state side are *The Born Rule as a Trace Formula — Derivation and Comparison*, *Quantum Physics in Biquaternionic Form* and *The Ontology of the Quantum State under the Biquaternion Framework*; the comparison of the four general products is *The Four General Products and Their Physical Readings*. The operation is a pairing; it is not a state and it is not a measurement, and neither is read from it.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity, $e_k^{2}=-e_0$ and $e_je_k=e_l$ for $(j,k,l)$ a cyclic permutation of $(1,2,3)$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$. The **natural conjugation** ${}^{\natural}$ fixes $e_0$, negates $e_1,e_2,e_3$ and is $\mathbb{C}$-linear; the **coefficientwise conjugation** $\overline{\cdot}$ conjugates the four coefficients; the **Hermitian conjugation** is ${}^{*}=\overline{\cdot}\circ{}^{\natural}$, so $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. $\mathrm{Sc}$ is the scalar part and the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, and the two sectors $\mathbb{M}_{\pm}$, with $\mathbb{B}=\mathbb{M}_{+}\oplus\mathbb{M}_{-}$ and $\mathbb{M}_{+}$ the Hermitian, informational side. The parent product is $\tilde P\tilde Q^{*}$, its symmetric half is written $\tilde P\circledast\tilde Q$ and its antisymmetric half $\tilde P\wedge_{*}\tilde Q$; all conventions are those of *Conventions in the Biquaternion Universe*.

## The Operation and Its Value

### Definition and the Central Value

The **general plain sesquilinear product** is the operation $\tilde P\tilde Q^{*}$, and the exchange that keeps its class is the interchange composed with the coefficientwise conjugation of the value (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). Its symmetric half is the operation of this block,

$$
\tilde P\circledast\tilde Q=\tfrac12\Bigl(\tilde P\tilde Q^{*}+\bigl(\tilde P\tilde Q^{*}\bigr)^{\natural}\Bigr)=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)e_0 .
$$

The two descriptions of the symmetrisation are the same element, $(\tilde P\tilde Q^{*})^{\natural}=\overline{\tilde Q\tilde P^{*}}$: the natural conjugation of the parent value is the interchange of the two factors followed by the coefficientwise conjugation of the value, and either is the exchange that keeps the class. The value is **central**: the natural conjugation fixes the scalar part and negates the vector part, so the vector part of $\tilde P\tilde Q^{*}$ is exactly cancelled and only the scalar part survives. Reading the scalar part through the Hermitian form,

$$
\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)\,e_0,\qquad H(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu}=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q}),
$$

which is the statement of the introduction: **the Hermitian form of the corpus is the operation**. The form $H$ and the product $\circledast$ carry the same information, and the image of the operation is the centre $\mathbb{C}_{\mathbb{B}}=\{\lambda e_0\}$; the block is the form read as a multiplication and nothing more (*The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*).

**Remark (one of the two central operations).** Because every value lies in the centre, the block is **one of the two central operations of the twelve**, the other being the symmetric quaternionic algebra $\mathrm{SQA}$; it is **not** a Jordan product — the symmetric plain algebra $\mathrm{SPA}$ alone among the twelve is one — and the failure of the Jordan identity in the section below is the statement of that (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*, *The 12 Products of the Biquaternion Complex Space*). The centrality is what makes the operation a form; the form's positivity is what makes its diagonal a probability; and the two are the same sentence.

**Remark (verified).** $\mathrm{Sc}(\tilde P\tilde Q^{*})=H(\tilde P,\tilde Q)$ and the half-sum is central, to $<10^{-13}$ over $100$ random pairs.

### The Class of the Operation

The operation is additive in each variable and

$$
(\lambda\tilde P)\circledast\tilde Q=\lambda\,(\tilde P\circledast\tilde Q),\qquad \tilde P\circledast(\lambda\tilde Q)=\overline{\lambda}\,(\tilde P\circledast\tilde Q),\qquad \lambda\in\mathbb{C},
$$

so it is $\mathbb{C}$-**linear in the first slot and conjugate-linear in the second**: it is a **sesquilinear** product, and that is what places the block in the sesqualgebra row and not in the algebra row. A scalar entering the first slot enters plain, and a scalar entering the second enters through its conjugate; a tabulation cannot be read by linearity in the second index. This is the first exact difference from the symmetric plain algebra $\mathrm{SPA}$ and the symmetric quaternionic algebra $\mathrm{SQA}$, whose products are $\mathbb{C}$-bilinear (*Introduction to the Symmetric Plain Algebra of Biquaternions*, *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*).

### The Multiplication Table of the Basis

**On the four basis elements the operation is the identity table.** Since $H(e_\mu,e_\nu)=\delta_{\mu\nu}$,

$$
e_\mu\circledast e_\nu=H(e_\mu,e_\nu)e_0=\delta_{\mu\nu}e_0 .
$$

| $\circledast$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $e_0$ | $0$ | $0$ |
| $e_2$ | $0$ | $0$ | $e_0$ | $0$ |
| $e_3$ | $0$ | $0$ | $0$ | $e_0$ |

The table is the Gram matrix of $H$ in the algebra basis times $e_0$: the operation records the form and nothing else. It is **rank one** over $\mathbb{C}$, its single value direction being $e_0$, and its kernel is the single scalar equation $H(\tilde P,\tilde Q)=0$ (*The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*).

**Remark (vanishing products of nonzero elements).** Off the diagonal the product vanishes, $e_\mu\circledast e_\nu=0$ for $\mu\neq\nu$, so the block **does** have vanishing products of nonzero elements; the vanishing pairs are exactly the $H$-orthogonal ones. The block has no isotropic vector and no nonzero element of square zero, and yet it has zero products: the two statements are one, and the second is the reason the first must be read as a statement about the *diagonal* of the form.

## The Diagonal and the Positivity

### The Diagonal Is Real and Strictly Positive

For every $\tilde Q$,

$$
\tilde Q\circledast\tilde Q=H(\tilde Q,\tilde Q)e_0=\Bigl(\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}\Bigr)e_0,
$$

a **central** element whose coefficient is a sum of squares of moduli; it is real, non-negative, and **strictly positive for $\tilde Q\neq0$**. The diagonal is the squared Euclidean length of the coefficient vector of the element, and it vanishes only at the origin.

**Consequences, and where they are owned.**
- **No isotropic vector, no square-zero element.** $H(\tilde Q,\tilde Q)=0$ forces $\tilde Q=0$, and $\tilde Q\circledast\tilde Q=0$ forces $\tilde Q=0$; the isotropic cone of the operation is $\{0\}$.
- **The absence of nulls is unitarity.** A form with no nonzero null vector is a form on which every nonzero state has strictly positive weight. The absence of an isotropic vector and the absence of a zero-weight state are one statement, and it is the statement that the form defines a genuine inner product: **unitarity written as an absence of nulls** rather than as a sign convention. On this form, and only on this form, a nonzero state is never annihilated.
- **The positivity is inherited, not built.** The diagonal is positive because $H$ is the definite form of the algebra, of signature $(8,0)$ on $\mathbb{B}\cong\mathbb{R}^{8}$; that positivity, its cone, its signature and its restriction to the remarkable subspaces are *Mass, Rank and the Positivity of the Dagger*, *Biquaternion Norm and Invertibility* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, and this article cites them and does not re-prove them.

**Remark (what the positivity is not).** The positivity is the positivity of the **diagonal of the form**, and the operation is conjugate-commutative and not commutative: it is not the positivity of a real-valued symmetric form, and it is not the positivity of the biquaternion norm $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$, which is indefinite and carries the interval. The statement $H\succ0$ is a statement about $H$ alone.

### The Reality on the State Side

The positivity acquires its physical reading on a subspace. On the Hermitian side $\mathbb{M}_{+}$ the Hermitian conjugation acts as the identity, $\tilde Q^{*}=\tilde Q$, so the second slot no longer conjugates anything new and the operation collapses onto the scalar part of the plain product,

$$
\tilde P\circledast\tilde Q=\mathrm{Sc}\bigl(\tilde P\tilde Q\bigr)e_0=\mathrm{Re}\,H(\tilde P,\tilde Q)\,e_0,\qquad \tilde P,\tilde Q\in\mathbb{M}_{+},
$$

and $H(\tilde P,\tilde Q)$ is **real**. The state side is the side on which the operation of this block is real-valued, and it is the side the corpus calls the informational sector; multiplication by the central $i$ exchanges it with the material side, $i\mathbb{M}_{-}=\mathbb{M}_{+}$.

**Remark (verified).** For $100$ random pairs of Hermitian elements, $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ identically, with vanishing imaginary part.

## The Hermitian Form as the Real Part of the Born Pairing

### The Two Halves of One Value

The parent value $X=\tilde P\tilde Q^{*}$ is an element of the algebra, and it decomposes into the two halves of the block,

$$
X=\tilde P\tilde Q^{*}=\underbrace{\mathrm{Sc}(X)e_0}_{\tilde P\circledast\tilde Q}+\underbrace{\mathrm{Vect}(X)}_{\tilde P\wedge_{*}\tilde Q},
$$

a central part and a vector part. The central part is the operation of this article; the vector part is the operation of the companion band, *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*. The two parts are the two halves of one number, and the split between them is the split between a **probability** and a **phase**; this article owns the first half and does not read the second.

### The Amplitude as Modulus and Argument

The same split reads as a split into a **modulus** and an **argument**. The central half is the modulus: on
the diagonal it is the positive number the operation measures, the squared length of the element. The
vector half is the argument: it is the direction the value carries, and it is the direction the central
operation discards, so an operation that keeps only the modulus cannot recover the argument and a
probability cannot be inverted to a phase. This is the modulus and the argument of an **amplitude**, and
the two bands of the block own one each. It is not the polar decomposition of an element — the corpus's
polar decomposition writes a unit as $\tilde Q=\lVert\tilde Q\rVert\tilde U$ and is owned by *Biquaternion
Norm and Invertibility* — but the polar reading of the two halves of one value, this band's contribution
to it.

### The Born Pairing

The corpus's Born rule is the trace formula

$$
\mathrm{Tr}\bigl(\tilde P\tilde H\bigr)=2\,\mathrm{Sc}\bigl(\tilde P\tilde H\bigr)=2\langle\tilde P,\tilde H\rangle,
$$

read on two Hermitian elements (*The Born Rule as a Trace Formula — Derivation and Comparison*, *Quantum Physics in Biquaternionic Form*). On the state side $\tilde H^{*}=\tilde H$, so $\mathrm{Sc}(\tilde P\tilde H^{*})=\mathrm{Sc}(\tilde P\tilde H)$, and the value of this block is one half of the Born pairing,

$$
\tilde P\circledast\tilde H=\tfrac12\,\mathrm{Tr}\bigl(\tilde P\tilde H\bigr)e_0=H(\tilde P,\tilde H)e_0,\qquad \tilde P,\tilde H\in\mathbb{M}_{+}.
$$

That identity is the reading the band's title records: **the operation is the Hermitian form as a product, and its central value is the real part of the Born pairing**. It is the real part in the exact sense of the decomposition above: $H(\tilde P,\tilde H)=\mathrm{Sc}(\tilde P\tilde H^{*})$ is the central half of the same amplitude whose vector half is the phase, and on the state side it is real and equals one half of the trace pairing.

**Remark (the caution, and it is the spine of the band).** A positive central value is a **pairing** and not a state. The operation compares two elements and returns a number; it selects none. The Born *probability* is that number once a state and an effect have been supplied from outside the operation, and the operation neither supplies them nor chooses among them. The state side is established in *Quantum Physics in Biquaternionic Form* and read ontologically in *The Ontology of the Quantum State under the Biquaternion Framework*; the operation contributes the pairing and not the state.

**Remark (where a scale enters).** The algebra carries no scale, and $\hbar$ enters with the physical reading of the phase amplitude and not here; the places of entry are those of the corpus, and none is invented in this article (*Action, Units, and the Constants of the Biquaternion Universe*).

## The Failure of the Jordan Identity

The symmetric plain algebra $\mathrm{SPA}$ satisfies the **Jordan identity**, and its reading as a Jordan algebra of observables is *Observables, Gauge Generators and the Chirality of the Internal Action*. It is therefore worth asking the same question of the symmetric sesquilinear block, and the answer is negative.

**The operation fails the Jordan identity.** For a commutative product the Jordan identity is the law

$$
(x^{2}\circledast y)\circledast x=x^{2}\circledast(y\circledast x),\qquad x^{2}=x\circledast x .
$$

Here the witness is $x=y=e_1$. Since $e_1\circledast e_1=e_0$ and $e_0\circledast\tilde Q=\overline{Q_0}\,e_0$, the two sides are

$$
(e_1^{2}\circledast e_1)\circledast e_1=(e_0\circledast e_1)\circledast e_1=0\circledast e_1=0,
$$

$$
e_1^{2}\circledast(e_1\circledast e_1)=e_0\circledast e_0=e_0 .
$$

The two sides are $0$ and $e_0$, distinct, so the identity fails (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*).

**Remark (why it fails, and what it means).** The reason is structural: the product is central-valued and conjugate-linear in its second slot, and the second slot of a central value cannot absorb the vector part that the identity would require it to absorb. A symmetrisation of a *sesquilinear* product is not a Jordan product; the algebraic fact is owned by the mathematics, and the reading is that the block is a genuine operation of the sesqualgebra row and of no classical kind, so **no Jordan-algebra structure may be read from it**, and the ordered cone of observables of the corpus belongs to the symmetric *plain* block and not to this one. The caution is exact: a failed identity is a failed identity of the algebra, and it says nothing about measurement.

## The Absence of a Unit and the Rank-One Image

**No unit, on either side.** For every $\tilde Q$,

$$
\tilde Q\circledast e_0=Q_0\,e_0,\qquad e_0\circledast\tilde Q=\overline{Q_0}\,e_0 .
$$

The element $e_0$ is neither a right unit nor a left unit: the first equation forces $\mathbf Q=0$, and the second forces $\mathbf Q=0$ and $Q_0$ real. The reason is the rank-one central image: a value of the block can carry only the scalar part of an element and never its vector part, so no element with a vector part is reproduced on either side. The block is therefore not a unital algebra, and there is no inverse theory attached to it.

**The idempotents are $0$ and $e_0$.** The idempotent equation $\tilde Q\circledast\tilde Q=\tilde Q$ forces $\tilde Q$ into the centre, where the operation is the field rule $(\lambda e_0)\circledast(\mu e_0)=\lambda\overline{\mu}\,e_0$ and the equation reduces to $\lvert\lambda\rvert^{2}=\lambda$, whose roots are $0$ and $1$. The element $e_0$ is an idempotent and not a unit; it is the certainty, not a state. The centrality of the image, the law and the idempotents are owned by *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* and read physically in *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*.

**The law.** The operation is **conjugate-commutative**,

$$
\tilde P\circledast\tilde Q=\overline{\tilde Q\circledast\tilde P},
$$

the bar acting on the central value; the law and the Hermitian symmetry of the form, $H(\tilde Q,\tilde P)=\overline{H(\tilde P,\tilde Q)}$, are one statement (*The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*).

## Remarkable Subspaces

The values of the block are central, so the product of two elements of any of the remarkable subspaces is a real or complex multiple of $e_0$, and the restricted form $H$ is positive definite on each of the remarkable subspaces, of rank the real dimension of the subspace. Only the **closure** of the product separates the remarkable subspaces, and the criterion is one line: a subspace is closed exactly when it contains $e_0$. The centre, the real-quaternion subspace and the Hermitian subspace are closed; the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace are not, the smallest witness in each being the square of a basis element, $e_1\circledast e_1=e_0$ in the vector and anti-Hermitian subspaces and $(ie_1)\circledast(ie_1)=e_0$ in the anti-quaternion subspace (*Remarkable Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions*).

| subspace | real dimension | $H$ restricted | closed under $\circledast$ | contains $e_0$ |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | positive definite, complex | yes | yes |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | positive definite, complex | no | no |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | positive definite, real-valued | yes | yes |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | positive definite, real-valued | no | no |
| $\mathbb{M}_{+}$ | $4$ | positive definite, real-valued | yes | yes |
| $\mathbb{M}_{-}$ | $4$ | positive definite, real-valued | no | no |

**Remark (the state side is the closed informational side).** The Hermitian subspace is closed because the positive real multiples of $e_0$ lie in it, and on it the restricted form is real-valued and positive definite of rank $4$: this is the frame of a two-state system, whose states and observables share the subspace, and on it the diagonal is the Born pairing. The block's home is therefore the **state side** $\mathbb{M}_{+}$, and not the material side of the two algebra rows. The contrast with the quaternionic sesquilinear row, whose form $K$ is indefinite and whose values lie in no subspace of the remarkable subspaces, is the companion article's subject and is stated there and not here.

## Ledger

**What the operation does.**
- Reads the central part of the plain sesquilinear amplitude as a multiplication: $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0$.
- Carries and exposes the **positivity** of the Hermitian form on its diagonal, $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}>0$ off the origin.
- Supplies, on the state side, one half of the Born trace pairing, $\tilde P\circledast\tilde H=\tfrac12\mathrm{Tr}(\tilde P\tilde H)e_0$.
- Supplies the **modulus** of an amplitude — the positive central half, the argument being the companion band's — and by the absence of nulls fixes a genuine inner product, the definiteness on which a unitary evolution rests.
- Records the Gram matrix of $H$ and the $H$-orthogonal (vanishing) pairs.

**What the operation does not do.**
- It is not a state: a positive central value pairs two elements and selects none.
- It is not a measurement: the operation produces no outcome and carries no probability rule of its own.
- It has no unit and no inverse, and it is not associative or Jordan: it is a rank-one central operation and of no classical kind.
- It carries no scale; the constants enter elsewhere in the corpus.

## Physical Readings

The real part of the Born pairing reads as the probability and, at the same time, as the framework's invariant. It is central-valued and positive on the informational sector, which is what makes a state normalisable, and it is one of the forms that a change of the local complex structure leaves alone, so the probability is data of the algebra while the interval is data of the embedding (*Conventions in the Biquaternion Universe*). Read on the clock, the pairing is silent about the phase: the phase of an amplitude is carried by the imaginary part of the pairing, and the article's separation of the real part is what makes the two readings distinct.

Read on the two slots, the form is the framework's **measurement pairing**: one slot is prepared and one is measured, the conjugation sitting in one slot and not in the other, so the asymmetry of the pairing is what distinguishes a state from an effect and is the algebraic mark of the quantum two-slot structure. Two established results are that shape. The no-cloning obstruction is the requirement that this pairing square under copying, which forces it to $0$ or $1$ (*No-Cloning and the Algebraic Obstruction in Biquaternionic Form*), and the in–out structure of the scattering matrix is the same two slots read asymptotically (*The S-Matrix in Biquaternionic Form*). Boundary: the article's pairing is the trace pairing of the algebra and the two named readings own their theorems; the reading records the shared shape and adds no obstruction of its own.

## Summary

The symmetric plain sesqualgebra is the **Hermitian form of the corpus read as a multiplication**, $\tilde P\circledast\tilde Q=\mathrm{Sc}(\tilde P\tilde Q^{*})e_0=H(\tilde P,\tilde Q)e_0$ with $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$. Its value is **central**, its class is sesquilinear with the conjugation in the second slot, and its basis table is the identity times $e_0$: the operation is the Gram matrix of $H$ and nothing else. Its **diagonal is real and strictly positive off the origin**, $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}>0$, so the operation has no isotropic vector and no nonzero element of square zero — the absence of a null vector is read as the definiteness of a genuine inner product, that is **unitarity written as an absence of nulls** — the positivity is that of the definite form of the algebra and is owned by the mass-and-positivity article. The parent value splits into the two halves of the block, $\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q$, and the two halves are the **modulus and the argument** of one amplitude: the central half is the **real part of the Born pairing** and on the state side it is one half of the trace pairing, $\tilde P\circledast\tilde H=\tfrac12\mathrm{Tr}(\tilde P\tilde H)e_0$ with $\tilde P,\tilde H\in\mathbb{M}_{+}$, while the argument is the companion band's. The operation **fails the Jordan identity**, with the witness $x=y=e_1$, where the two sides are $0$ and $e_0$; it has **no unit** on either side and its only idempotents are $0$ and $e_0$; it is **conjugate-commutative**. Among the remarkable subspaces only the closure separates the block, and it is closed on the centre, the real-quaternion subspace and the Hermitian subspace, which is the state side of the corpus. The reading is bounded twice: a positive central value is a pairing and not a state, and the operation belongs to the state row without being a state.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\tilde Q^{*}$ | the general plain sesquilinear product (GPS) |
| $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0$ | the symmetric part (SPS); the operation of the block |
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form; $H=\langle\cdot,\cdot\rangle_{*}$ |
| $H(e_\mu,e_\nu)=\delta_{\mu\nu}$, $e_\mu\circledast e_\nu=\delta_{\mu\nu}e_0$ | the identity table and the Gram matrix |
| $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}>0$ | the positive diagonal; no isotropic vector |
| $\tilde P\circledast\tilde Q=\overline{\tilde Q\circledast\tilde P}$ | conjugate-commutativity |
| $\tilde Q\circledast e_0=Q_0e_0$, $e_0\circledast\tilde Q=\overline{Q_0}e_0$ | no unit on either side |
| $(x^{2}\circledast y)\circledast x\neq x^{2}\circledast(y\circledast x)$ at $x=y=e_1$ | the Jordan failure; the sides $0$ and $e_0$ |
| $\{0,e_0\}$ | the idempotents of the operation |
| $\tilde P\circledast\tilde H=\tfrac12\mathrm{Tr}(\tilde P\tilde H)e_0$ on $\mathbb{M}_{+}$ | the Born pairing as the central value |
| central half = modulus, vector half = argument | the two polar components of one amplitude (not the polar decomposition of an element) |
| $\mathbb{M}_{+}$ | the state side; closed and real-valued |
| $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | the antisymmetric part, read in the companion band |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, its class, its table and the Jordan failure.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form read as the product, its rank-one image and its restrictions.
- *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the law, the idempotents and the vanishing annihilator.
- *Remarkable Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the closure of the remarkable subspaces.
- *Mass, Rank and the Positivity of the Dagger* (`articles_physics/mass-rank-and-the-positivity-of-the-dagger.md`), which owns the positivity of the Hermitian form.
- *The Born Rule as a Trace Formula — Derivation and Comparison* (`articles_physics/the-born-rule-as-a-trace-formula-derivation-and-comparison.md`), which owns the Born rule and the trace pairing.
- *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone* (`articles_physics/why-probability-values-are-central-the-symmetric-sesquilinear-product-and-its-cone.md`), the companion article of the band.
- *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product* (`articles_physics/the-imaginary-part-of-the-born-pairing-the-antisymmetric-sesquilinear-product.md`), the other half of the same value.
- *The Fourth Product and Its Indefinite Metric* (`articles_physics/the-fourth-product-and-its-indefinite-metric.md`), for the quaternionic sesquilinear row and its indefinite form.
