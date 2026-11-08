# __The Hermitian Pair of Operators Acting on Two Sides__

## Introduction: The Real Cone

**The operator.** For $\tilde Q\in\mathbb{B}$, the **Hermitian pair of operators acting on two sides** is

$$
\mathrm{Hp}_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$

It is the two-sided operator $L_{\tilde Q}R_{\tilde Q^{*}}$: the second slot is tied to the first by the involution. The two-sided family is a complex cone of complex dimension seven; the Hermitian pair is the graph of the involution inside it, a **real** cone of real dimension seven. The phase of the parameter cancels, $\mathrm{Hp}_{\omega\tilde Q}=\mathrm{Hp}_{\tilde Q}$ for $|\omega|=1$, and the square of the modulus is the only scale. The image is not a complex subspace: the Hermitian pair is quadratic in $\tilde Q$, and a complex rescaling of $\tilde Q$ rescales the operator by the square of the modulus, a positive real number.

**The results.** The article states the following. The Hermitian pair is multiplicative up to the order of the factors, $\mathrm{Hp}_{\tilde Q}\mathrm{Hp}_{\tilde Q_2}=\mathrm{Hp}_{\tilde Q\tilde Q_2}$, and its defect from an algebra automorphism is the operator $e_t-\tilde Q^{*}\tilde Q$. It preserves the Hermitian and anti-Hermitian halves for every parameter, and it preserves the finer subspace structure exactly when the parameter is a central multiple of a real unit quaternion. It is characterised by the preservation of the halves: inside the two-sided family the sector-preserving operators are exactly the real multiples of the Hermitian pairs, so the sector condition forces the shape of the operator and the parameter of the operator is the element itself, up to the central phase. It scales the norm by $|\langle\tilde Q\rangle_{\natural}|^{2}$. Its parameter is defined modulo the central phase, which gives the real dimension seven. It meets each one-sided family in the closed ray of nonnegative multiples of the identity, and its spectrum is the four products of the eigenvalues of the $2\times2$ model with their conjugates. The family spans the whole sixteen-dimensional sector-preserving space: sixteen Hermitian pairs are a real basis, exactly as sixteen two-sided operators are a complex basis of the endomorphism algebra. On the unit-norm slice the parameter map is the twofold cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$; on the full unit group it has kernel $U(1)$ and image $CO^{+}(1,3)$.

**Verification.** The matrix verification of the spectrum and of the Lorentz action is in *The Polar Decomposition and Remarkable Subspaces*, §*The Anti-Hermitian Half as Four-Vectors* and §*The Two Halves Are One Action*. The present article states the operator results and sketches the proofs; no case study is cited as proof. The notation of the families is that of *Operator Family Conventions*: $\mathrm{Hp}_{\tilde Q}$ is the Hermitian pair, $L_{\tilde Q}R_{\tilde Q_2}$ the two-sided operator, $L(\mathbb{B})$ and $R(\mathbb{B})$ the two regular families, $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ the Hermitian and anti-Hermitian halves, $\langle\tilde Q\rangle_{\natural}$ the quaternionic norm, and $\operatorname{End}_{LR\ast}(\mathbb{B})$ the set of Hermitian pairs. The involution is the algebra's conjugation, the one whose matrix is the dagger in the matrix models.

**The real cone.** The set $\operatorname{End}_{LR\ast}(\mathbb{B})=\{\mathrm{Hp}_{\tilde Q}:\tilde Q\in\mathbb{B}\}$ is a cone: it is closed under multiplication by nonnegative real numbers, and it is not closed under addition. It is a real cone of real dimension seven, not a complex cone. The two-sided cone $\operatorname{End}_{LR}(\mathbb{B})$ is complex of complex dimension seven, and the Hermitian pair is a real slice of it, a proper subset, the slice on which the two parameters are conjugate.

**The other placement.** The pair $(L_{\tilde Q},R_{\tilde Q^{\ast}})$ is one placement of a Hermitian pair; the pair $(L_{\tilde Q},L_{\tilde Q^{\natural}})$, whose two members both multiply on the left, is the other. It is the subject of *The Hermitian Pair of Operators Acting on One Side*, where the transposition $R_{\tilde Q^{\ast}}=\ast^{-1}L_{\tilde Q}\ast$ replaces the right member here by a left member there, and where the composite of the pair is a scalar instead of this article's operator.

## The Operator $\mathrm{Hp}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$

### The Definition

**Definition.** For $\tilde Q\in\mathbb{B}$, $\mathrm{Hp}_{\tilde Q}$ is the map

$$
\mathrm{Hp}_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
\mathrm{Hp}_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$

It is the composite $L_{\tilde Q}R_{\tilde Q^{*}}$ of a left multiplication and a right multiplication. It is $\mathbb{C}$-linear in $\tilde X$, because $L_{\tilde Q}$ and $R_{\tilde Q^{*}}$ are $\mathbb{C}$-linear. It is invertible exactly when $\tilde Q$ is a unit, and then

$$
\mathrm{Hp}_{\tilde Q}^{-1}=\mathrm{Hp}_{\tilde Q^{-1}}.
$$

If $\tilde Q$ is not a unit, the map has a nonzero kernel: a nonzero $\tilde X$ with $\tilde Q\tilde X=0$ or $\tilde X\tilde Q^{*}=0$ is sent to zero.

**The zero and the identity.** $\mathrm{Hp}_0=0$, and $\mathrm{Hp}_{e_t}=\mathrm{id}$. The identity is the Hermitian pair of the unit, and the identity operator is also $\mathrm{Hp}_{\omega e_t}$ for every central phase $\omega$ of modulus one. The map $\tilde Q\mapsto\mathrm{Hp}_{\tilde Q}$ is not linear: it is quadratic, with the cross terms $\tilde Q\tilde X\tilde Q_2^{*}+\tilde Q_2\tilde X\tilde Q^{*}$ in $\mathrm{Hp}_{\tilde Q+\tilde Q_2}$.

**The scaling.** For $\lambda\in\mathbb{C}$,

$$
\mathrm{Hp}_{\lambda\tilde Q}=|\lambda|^{2}\,\mathrm{Hp}_{\tilde Q},
$$

because $(\lambda\tilde Q)^{*}=\bar\lambda\tilde Q^{*}$. The phase of $\lambda$ cancels and the modulus squared remains. In particular $\mathrm{Hp}_{\omega\tilde Q}=\mathrm{Hp}_{\tilde Q}$ for every $\omega$ with $|\omega|=1$.

### The Member $L_{\tilde Q}R_{\tilde Q^{*}}$

**The two-sided family.** The Hermitian pair is the member of the two-sided family whose parameters are tied:

$$
\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}.
$$

The two-sided family is the set of decomposable tensors $\tilde Q\otimes\tilde Q_{2,\mathrm{opp}}$, a complex cone of complex dimension seven in the complex sixteen-dimensional algebra. The Hermitian pair is the graph of the involution $\tilde Q_2=\tilde Q^{*}$ inside that cone.

**The graph is real, not complex.** For $\lambda\in\mathbb{C}^{\times}$ the pair $(\lambda\tilde Q,(\lambda\tilde Q)^{*})=(\lambda\tilde Q,\bar\lambda\tilde Q^{*})$ is not $\lambda(\tilde Q,\tilde Q^{*})$ unless $\lambda$ is real. The graph is therefore not a complex subcone: a complex rescaling of the pair leaves the graph, while the Hermitian pair itself rescales by $|\lambda|^{2}$. The image is a real cone of real dimension seven. Its complex span is the whole endomorphism algebra: the graph is a real form of $\mathbb{B}\times\mathbb{B}$, and the bilinear map $T$ is surjective by the generation theorem of *Operators Acting on Two Sides*; the complex cone generated by a single Hermitian pair is only a complex line, so the real cone is not the complex cone. Over $\mathbb{R}$ the Hermitian-pair cone is a proper subset of the ambient space: it is a real cone of real dimension seven, not a real vector space, and its complex span is the whole algebra.

**The member.** The set is named in *Operator Family Conventions*; this article proves the row: $\operatorname{End}_{LR\ast}(\mathbb{B})=\{\mathrm{Hp}_{\tilde Q}\}$ is a real cone of real dimension seven, contained in $\operatorname{End}_{LR}(\mathbb{B})$ and meeting each one-sided family in the closed ray of the identity. The sections below give the proofs.

## Multiplicativity

### $\mathrm{Hp}_{\tilde Q}\mathrm{Hp}_{\tilde Q_2}=\mathrm{Hp}_{\tilde Q\tilde Q_2}$

**Proposition (multiplicativity).** For all $\tilde Q,\tilde Q_2\in\mathbb{B}$,

$$
\mathrm{Hp}_{\tilde Q}\,\mathrm{Hp}_{\tilde Q_2}=\mathrm{Hp}_{\tilde Q\tilde Q_2}.
$$

*Proof.* For every $\tilde X$,

$$
\mathrm{Hp}_{\tilde Q}\bigl(\mathrm{Hp}_{\tilde Q_2}(\tilde X)\bigr)
=\tilde Q\,\tilde Q_2\,\tilde X\,\tilde Q_2^{*}\,\tilde Q^{*}
=(\tilde Q\tilde Q_2)\,\tilde X\,(\tilde Q\tilde Q_2)^{*},
$$

because $(\tilde Q\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q^{*}$. The right-hand side is $\mathrm{Hp}_{\tilde Q\tilde Q_2}(\tilde X)$.

**The order.** The composition is $\mathrm{Hp}_{\tilde Q}\mathrm{Hp}_{\tilde Q_2}=\mathrm{Hp}_{\tilde Q\tilde Q_2}$; the map $\tilde Q\mapsto\mathrm{Hp}_{\tilde Q}$ is therefore a homomorphism from the opposite algebra $\mathbb{B}_{\mathrm{opp}}$ to $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, not from $\mathbb{B}$. The reversal is the involution: the star reverses the order of the factors. In particular the image is a group anti-isomorphic to the unit group, and $\mathrm{Hp}_{\tilde Q}^{-1}=\mathrm{Hp}_{\tilde Q^{-1}}$ is the inverse in the image.

**The kernel of the parameter map.** If $\mathrm{Hp}_{\tilde Q}=\mathrm{id}$, then $\tilde Q\tilde X\tilde Q^{*}=\tilde X$ for all $\tilde X$. At $\tilde X=e_t$ this gives $\tilde Q\tilde Q^{*}=e_t$; the parameter is a unit of norm one. The identity Hermitian pair is $\mathrm{Hp}_{\omega e_t}$ for every central phase $\omega$ with $|\omega|=1$, and these are all: the kernel of the parameter map on the unit group is the central $U(1)$. The proof of the exact kernel is in §*The Parameter Modulo $\mathrm{U}(1)$*.

### The Defect of an Automorphism

**The defect.** The Hermitian pair is not an algebra automorphism in general. For all $\tilde X,\tilde Y$,

$$
\mathrm{Hp}_{\tilde Q}(\tilde X\tilde Y)-\mathrm{Hp}_{\tilde Q}(\tilde X)\,\mathrm{Hp}_{\tilde Q}(\tilde Y)
=\tilde Q\,\tilde X\,\bigl(e_t-\tilde Q^{*}\tilde Q\bigr)\,\tilde Y\,\tilde Q^{*}.
$$

The **defect** is the element $e_t-\tilde Q^{*}\tilde Q$, placed between the two arguments. The Hermitian pair is an algebra automorphism exactly when the defect vanishes, that is, when $\tilde Q^{*}\tilde Q=e_t$. For an invertible $\tilde Q$ this is the $*$-unitary group.

**The scaled case.** If $\tilde Q^{*}\tilde Q=\lambda e_t$ with $\lambda>0$, then

$$
\mathrm{Hp}_{\tilde Q}(\tilde X)\,\mathrm{Hp}_{\tilde Q}(\tilde Y)
=\lambda\,\mathrm{Hp}_{\tilde Q}(\tilde X\tilde Y),
$$

so the Hermitian pair is a scalar multiple of an algebra automorphism; it is an automorphism exactly when $\lambda=1$. The central multiples of real unit quaternions with a nontrivial scale preserve the subspace structure of §*The Two Halves* but are not algebra automorphisms. The defect $e_t-\tilde Q^{*}\tilde Q=(1-\lambda)e_t$ measures the scale.

**The two laws.** The composition law $\mathrm{Hp}_{\tilde Q}\mathrm{Hp}_{\tilde Q_2}=\mathrm{Hp}_{\tilde Q\tilde Q_2}$ holds for every pair, and it concerns the composition of two Hermitian pairs. The automorphism law $\mathrm{Hp}_{\tilde Q}(\tilde X\tilde Y)=\mathrm{Hp}_{\tilde Q}(\tilde X)\mathrm{Hp}_{\tilde Q}(\tilde Y)$ holds only under the defect criterion $\tilde Q^{*}\tilde Q=e_t$, not under the weaker subspace criterion. The two laws are different; the first is the multiplication of the parameter, the second is the preservation of the algebra's product.

## The Two Halves

### Preservation of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$

**The halves.** The Hermitian half and the anti-Hermitian half are

$$
\mathbb{B}_{\Psi}=\{\tilde X:\tilde X^{*}=\tilde X\},\qquad
\mathbb{B}_{\Phi}=\{\tilde X:\tilde X^{*}=-\tilde X\}.
$$

They are the real eigenspaces of the involution. Each is a real subspace of real dimension four; they are exchanged by multiplication by the central $i$, and their sum is the real algebra of real dimension eight. They are not complex subspaces: multiplication by $i$ moves one to the other.

**Preservation.** If $\tilde X^{*}=\pm\tilde X$, then

$$
\bigl(\tilde Q\tilde X\tilde Q^{*}\bigr)^{*}
=\tilde Q\tilde X^{*}\tilde Q^{*}
=\pm\tilde Q\tilde X\tilde Q^{*}.
$$

So $\mathrm{Hp}_{\tilde Q}$ preserves each half for every $\tilde Q$, without a unit or norm-one hypothesis. The two statements are consequences of the involution, not of the norm.

**The exchange.** Multiplication by the central $i$ exchanges the halves: $\tilde X\in\mathbb{B}_{\Psi}$ iff $i\tilde X\in\mathbb{B}_{\Phi}$. The Hermitian pair commutes with the exchange, because $i$ is central:
$$
\mathrm{Hp}_{\tilde Q}(i\tilde X)=i\,\mathrm{Hp}_{\tilde Q}(\tilde X).
$$
The two halves are one action read in two real forms; the Lorentz transformation on $\mathbb{B}_{\Phi}$ is the congruence on $\mathbb{B}_{\Psi}$ composed with the exchange.

### The Criterion on $\tilde Q$

**The two halves are always preserved.** The criterion is not for the halves; it is for the finer subspace structure. The centre, the vector subspace, the real quaternion subspace and the anti-quaternion subspace are preserved exactly when $\tilde Q$ is a central multiple of a real unit quaternion.

**Theorem (the criterion).** For a unit $\tilde Q$, the following are equivalent:

1. $\mathrm{Hp}_{\tilde Q}$ maps each of the six remarkable subspaces to itself;
2. $\tilde Q=\tilde A\,\tilde u$ with $\tilde A$ central and $\tilde u$ a real unit quaternion;
3. $\tilde Q\tilde Q^{*}$ is a positive real multiple of $e_t$;
4. $\tilde Q^{*}\tilde Q$ is a positive real multiple of $e_t$.

For a general element the same equivalences hold with $\tilde Q$ replaced by its unit part; the scale is central and preserves every subspace.

*Sketch.* $(2)\Rightarrow(3)$: a real unit quaternion satisfies $\tilde u\tilde u^{*}=e_t$, so $\tilde Q\tilde Q^{*}=|\tilde A|^{2}e_t$. $(3)\Rightarrow(2)$: if $\tilde Q\tilde Q^{*}=\lambda e_t$ with $\lambda>0$, the principal square root of $\lambda$ normalises $\tilde Q$ to a unit element with $\tilde U\tilde U^{*}=e_t$; a unit element with $\tilde U\tilde U^{*}=e_t$ is a central phase times a real unit quaternion, by the polar decomposition. $(2)\Rightarrow(1)$: the central factor is a dilation, the real unit quaternion is a rotation of the vector space, and both preserve the six subspaces. $(1)\Rightarrow(3)$: if the centre is preserved, $\tilde Q\tilde Q^{*}$ is central; it is Hermitian positive, and a central Hermitian positive element of the algebra is a positive real multiple of $e_t$. The full proof is *The Polar Decomposition and Remarkable Subspaces*, §*Which Subspaces the Hermitian Pair Preserves*.

**The group.** On the unit-norm slice the parameters are the real unit quaternions modulo sign, and they form $SO(3)$, of real dimension three. With the central dilations admitted they form $\mathbb{R}_{>0}\times SO(3)$, of real dimension four. The rotation group sits inside the six-dimensional operator group as the rotations sit inside the Lorentz group; the remaining three dimensions are the boosts, which move the centre and the vector subspace. The criterion is weaker than the vanishing of the defect: it allows a central scale, and the defect vanishes exactly on the $*$-unitary part of the set. The central multiples of real unit quaternions with a nontrivial scale are dilations composed with rotations; they preserve the subspaces but are not algebra automorphisms.

**The matrix check.** The matrix verification is in *The Polar Decomposition and Remarkable Subspaces*, §*The Hermitian Half as a Congruence*, and §*Which Subspaces the Hermitian Pair Preserves* of the same article.

## The Two Halves Characterise the Hermitian Pair

### The Condition Is Empty

The preservation of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ holds for every parameter, by §*Preservation of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$*. No hypothesis on $\tilde Q$ enters: the proof uses only that the star reverses the product and that $\tilde X^{*}=\pm\tilde X$. Preservation is a property of the star, not a constraint on the parameter.

**Proposition (the three equivalent forms).** For a $\mathbb{C}$-linear $T:\mathbb{B}\to\mathbb{B}$ the following are equivalent:

1. $T(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Phi}$;
2. $T(\mathbb{B}_{\Psi})\subseteq\mathbb{B}_{\Psi}$ and $T(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Phi}$;
3. $T(\tilde X^{*})=T(\tilde X)^{*}$ for every $\tilde X\in\mathbb{B}$.

*Proof.* $(3)\Rightarrow(1)$ and $(3)\Rightarrow(2)$: if $\tilde X^{*}=\pm\tilde X$, then $T(\tilde X)^{*}=T(\tilde X^{*})=\pm T(\tilde X)$. $(2)\Rightarrow(1)$ by truncation. $(1)\Rightarrow(2)$: the central $i$ exchanges the halves and $T$ is $\mathbb{C}$-linear, so $T(i\tilde X)=iT(\tilde X)$ carries $T(\mathbb{B}_{\Phi})$ onto $T(\mathbb{B}_{\Psi})$. $(1)\Rightarrow(3)$: write $\tilde X=\tilde X_{\Phi}+i\tilde Y$ with $\tilde X_{\Phi},\tilde Y\in\mathbb{B}_{\Phi}$; then $\tilde X^{*}=-\tilde X_{\Phi}+i\tilde Y$ and

$$
T(\tilde X)^{*}=T(\tilde X_{\Phi})^{*}+\bigl(i\,T(\tilde Y)\bigr)^{*}=-T(\tilde X_{\Phi})+i\,T(\tilde Y)=T(\tilde X^{*}).
$$

**The commutation form.** Write $J(\tilde X)=\tilde X^{*}$ for the real structure. Condition 3 is $TJ=JT$, and the Hermitian pair satisfies it at every parameter:

$$
J\,\mathrm{Hp}_{\tilde Q}\,J=\mathrm{Hp}_{\tilde Q}.
$$

The Hermitian pair is invariant under conjugation by the real structure. That is the operator form of §*Preservation of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$*: the star on the arguments and the star on the two slots cancel pairwise.

**Into, not onto.** The sector condition says "into", and it must not be read as "onto". On the null cone $\operatorname{rank}\mathrm{Hp}_{\tilde Q}=\operatorname{rank}(\tilde Q)^{2}=1$, so the image of $\mathbb{B}_{\Phi}$ is a real plane inside the four-dimensional $\mathbb{B}_{\Phi}$. Surjectivity on the halves is equivalent to the invertibility of the operator, that is, to $\tilde Q$ being a unit.

### The Rigidity

**Theorem (the sector condition forces the Hermitian pair).** Let $\tilde A,\tilde B\in\mathbb{B}$ be nonzero. Then $L_{\tilde A}R_{\tilde B}$ maps $\mathbb{B}_{\Phi}$ into itself if and only if

$$
\tilde B=\lambda\tilde A^{*}
$$

for some real $\lambda$.

*Proof.* For $\tilde X\in\mathbb{B}_{\Phi}$ the image has star

$$
\bigl(\tilde A\tilde X\tilde B\bigr)^{*}=\tilde B^{*}\tilde X^{*}\tilde A^{*}=-\tilde B^{*}\tilde X\tilde A^{*},
$$

so the condition is $\tilde B^{*}\tilde X\tilde A^{*}=\tilde A\tilde X\tilde B$ for every $\tilde X\in\mathbb{B}_{\Phi}$. Both sides are $\mathbb{C}$-linear in $\tilde X$, and $\mathbb{B}_{\Phi}$ spans $\mathbb{B}$ over $\mathbb{C}$ because $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$; the identity therefore holds for every $\tilde X$. It is the operator identity

$$
L_{\tilde B^{*}}R_{\tilde A^{*}}=L_{\tilde A}R_{\tilde B}.
$$

By *Operators Acting on Two Sides*, §*The Scaling Orbit*, the two parameter pairs lie on one orbit, so $(\tilde B^{*},\tilde A^{*})=(\mu\tilde A,\mu^{-1}\tilde B)$ for some $\mu\in\mathbb{C}^{\times}$, that is,

$$
\tilde B^{*}=\mu\tilde A,\qquad \tilde A^{*}=\mu^{-1}\tilde B.
$$

Daggering the second relation and substituting the first gives $\tilde A=\bar\mu^{-1}\tilde B^{*}=(\mu/\bar\mu)\tilde A$, so $\mu$ is real. Daggering the first relation then gives $\tilde B=\mu\tilde A^{*}$. Conversely, if $\tilde B=\lambda\tilde A^{*}$ with $\lambda$ real, then

$$
\bigl(\tilde A\tilde X\tilde B\bigr)^{*}=\lambda\tilde A\tilde X^{*}\tilde A^{*}=-\lambda\tilde A\tilde X\tilde A^{*}.
$$

The zero operator is the case $\tilde A=0$ or $\tilde B=0$, and it preserves the halves trivially.

**Corollary (the characterisation).** Inside the two-sided family the sector-preserving operators are exactly the real multiples of the Hermitian pairs:

$$
\{T\in\operatorname{End}_{LR}(\mathbb{B}):T(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Phi}\}=\mathbb{R}\cdot\operatorname{End}_{LR\ast}(\mathbb{B}).
$$

The Hermitian pair is not one choice among the two-sided operators. It is the only shape that preserves the sectors, up to a real scalar.

**The reading: the operator is the element.** The corollary determines the operator from the property, and §*The Parameter Modulo $\mathrm{U}(1)$* determines the parameter from the operator. The two directions are inverse, so the cone of Hermitian pairs is the biquaternion algebra read modulo the central phase,

$$
\operatorname{End}_{LR\ast}(\mathbb{B})\;\longleftrightarrow\;\mathbb{B}/\mathrm{U}(1),
$$

a bijection of sets and a homeomorphism, with the quadratic parametrisation $Q\mapsto\mathrm{Hp}_Q$; it is not linear, because $\mathrm{Hp}$ is quadratic in $Q$. The sector-preserving two-sided operators are that copy together with its negative. The family is $\mathbb{B}$ modulo the phase, not $\mathbb{B}$ itself: the phase is the only thing the correspondence forgets.

**The sign.** The real scalar $\lambda$ of the corollary may be negative, and a negative multiple is not a Hermitian pair. For a unit $\tilde A$ the value at the identity is $\mathrm{Hp}_{\tilde A}(e_t)=\tilde A\tilde A^{*}$, of norm $|\langle\tilde A\rangle_{\natural}|^{2}\ge0$, while $-\tilde A\tilde A^{*}$ has norm $-|\langle\tilde A\rangle_{\natural}|^{2}\le0$; the two agree only if both vanish. The Hermitian-pair cone is therefore one half of the sector-preserving set, and the sign is the part of the real scalar that the Hermitian pair cannot produce.

### Both Halves Give One Condition

**Theorem (one condition, two halves).** Let $\tilde A,\tilde B\in\mathbb{B}$ be nonzero. The following are equivalent:

1. $L_{\tilde A}R_{\tilde B}$ maps $\mathbb{B}_{\Phi}$ into itself;
2. $L_{\tilde A}R_{\tilde B}$ maps $\mathbb{B}_{\Psi}$ into itself;
3. $\tilde B=\lambda\tilde A^{*}$ for some real $\lambda$.

*Proof.* The equivalence of 1 and 3 is the theorem of §*The Rigidity*. For 2, let $\tilde X\in\mathbb{B}_{\Psi}$, so $\tilde X^{*}=\tilde X$. The image is Hermitian exactly when

$$
\bigl(\tilde A\tilde X\tilde B\bigr)^{*}=\tilde B^{*}\tilde X\tilde A^{*}=\tilde A\tilde X\tilde B .
$$

This is the operator identity $L_{\tilde B^{*}}R_{\tilde A^{*}}=L_{\tilde A}R_{\tilde B}$, the same identity as in the $\mathbb{B}_{\Phi}$ case, because the sign of the involution cancels on both sides. It involves no representative of $\mathbb{B}_{\Psi}$ in particular: it is an identity of operators, so the derivation that follows applies word for word and gives $\tilde B=\mu\tilde A^{*}$ with $\mu$ real. Conversely, $\tilde B=\lambda\tilde A^{*}$ with $\lambda$ real gives

$$
\bigl(\tilde A\tilde X\tilde B\bigr)^{*}=\lambda\tilde A\tilde X^{*}\tilde A^{*}=\pm\lambda\tilde A\tilde X\tilde A^{*},
$$

which is the image with the same sign as $\tilde X^{*}=\pm\tilde X$. So one real scalar serves both halves at once.

**Nothing is gained by asking for both.** The conditions 1 and 2 are the same condition, so the two sets coincide:

$$
\{T\in\operatorname{End}_{LR}(\mathbb{B}):T(\mathbb{B}_{\Psi})\subseteq\mathbb{B}_{\Psi}\}
=\{T\in\operatorname{End}_{LR}(\mathbb{B}):T(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Phi}\}
=\mathbb{R}\cdot\operatorname{End}_{LR\ast}(\mathbb{B}).
$$

The reason is that each half already spans the algebra over $\mathbb{C}$: $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$ and $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$. A two-sided operator that keeps one half inside itself therefore keeps the other inside itself too, and no operator tests the halves separately.

**The Hermitian pair is the case $\lambda=1$.** The theorem is a statement about the shape of the operator, not about the size of the parameter. The Hermitian pair is $\tilde B=\tilde A^{*}$, that is $\lambda=1$, the positive end of the ray. It preserves both halves with no hypothesis on $\tilde Q$ because $1$ is real. The hypothesis that does the work in §*The Condition Is Empty* is exactly this: the Hermitian pair sits at a real $\lambda$.

**The direction of $\lambda$.** Write $\lambda=\rho e^{i\theta}$ with $\rho>0$. Then

$$
L_{\tilde A}R_{\lambda\tilde A^{*}}=\lambda\,\mathrm{Hp}_{\tilde A},
$$

the Hermitian pair composed with the scalar $\lambda$. Multiplication by a scalar acts on the halves according to its argument:

| $\lambda$ | effect on $\mathbb{B}_{\Psi}$ | effect on $\mathbb{B}_{\Phi}$ |
|---|---|---|
| $\lambda$ real, $\lambda>0$ | into itself | into itself |
| $\lambda$ real, $\lambda<0$ | into itself | into itself |
| $\lambda$ purely imaginary | into $\mathbb{B}_{\Phi}$ | into $\mathbb{B}_{\Psi}$ |
| $\lambda$ complex, both parts nonzero | into neither | into neither |

A real $\lambda$, of either sign, keeps each half; the sign is invisible to the halves because it is real. A purely imaginary $\lambda$ swaps them, since $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$; that is the exchange of §*Preservation of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$*, read as a scalar. A $\lambda$ with both parts nonzero sends a Hermitian element to an element that is neither Hermitian nor anti-Hermitian, so neither half survives. The real line is therefore not a detail of the proof: it is the set of scalars that preserve the sector structure, and the Hermitian pair lies on it.

### The One-Sided Contrast

**Proposition (the one-sided case).** $L_{\tilde A}$ maps $\mathbb{B}_{\Phi}$ into itself exactly when $\tilde A$ is a real scalar, and the same holds for $R_{\tilde A}$.

*Proof.* For $\tilde X\in\mathbb{B}_{\Phi}$, $(\tilde A\tilde X)^{*}=\tilde X^{*}\tilde A^{*}=-\tilde X\tilde A^{*}$, so the condition is $\tilde X\tilde A^{*}=\tilde A\tilde X$ for every $\tilde X\in\mathbb{B}_{\Phi}$, hence for every $\tilde X$, that is $R_{\tilde A^{*}}=L_{\tilde A}$. The intersection $L(\mathbb{B})\cap R(\mathbb{B})$ is the line $\mathbb{C}\cdot\mathrm{I}$, so $\tilde A^{*}$ is central and $\tilde A=\lambda e_t$; the identity then reads $\bar\lambda=\lambda$, so $\lambda$ is real. The right case is the mirror, with the two slots exchanged.

**The reading.** The star is conjugate-linear, so a complex scalar $\lambda e_t$ sends $\tilde X$ to $\lambda\tilde X$, of star $\bar\lambda\tilde X^{*}$: the real part of $\lambda$ keeps the sector and the imaginary part turns it into the other sector. The Hermitian pair is the two-slot combination in which the conjugate-linearity occurs twice and cancels, and by §*The Rigidity* it is the only one, up to a real scalar. That is the structural reason the Hermitian pair, and not the one-sided multiplication, is the operator of the two halves.

### The Ambient Space

**The space.** The sector-preserving $\mathbb{C}$-linear maps form the real space $\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi})$, of real dimension sixteen. A $\mathbb{C}$-linear $T$ is determined by its restriction to $\mathbb{B}_{\Psi}$, and every real endomorphism of $\mathbb{B}_{\Psi}$ extends uniquely, because $T(i\tilde X)=iT(\tilde X)$ then fixes $T$ on $\mathbb{B}_{\Phi}$. Without $\mathbb{C}$-linearity the sector-preserving real-linear maps form a space of real dimension forty-eight inside the sixty-four-dimensional $\operatorname{End}_{\mathbb{R}}(\mathbb{B})$.

**The polarization.** The Hermitian-pair cone is quadratic in its parameter, and its polarization is

$$
\mathrm{Hp}_{\tilde A+\tilde B}-\mathrm{Hp}_{\tilde A}-\mathrm{Hp}_{\tilde B}=L_{\tilde A}R_{\tilde B^{*}}+L_{\tilde B}R_{\tilde A^{*}}.
$$

At $\tilde B=e_t$ the right side is $L_{\tilde A}+R_{\tilde A^{*}}$, the sum of a left multiplication and a mirrored right multiplication; at $\tilde A=i e_t$ it is $i(R_{\tilde B^{*}}-L_{\tilde B})$. Every such sum is sector-preserving, and the check is one line: for $\tilde X\in\mathbb{B}_{\Phi}$,

$$
\bigl(\tilde A\tilde X\tilde B^{*}+\tilde B\tilde X\tilde A^{*}\bigr)^{*}
=\tilde B\tilde X^{*}\tilde A^{*}+\tilde A\tilde X^{*}\tilde B^{*}
=-\tilde B\tilde X\tilde A^{*}-\tilde A\tilde X\tilde B^{*}.
$$

The two terms are exchanged by the star, so neither needs to be sector-preserving on its own. That is precisely what §*The Rigidity* forbids for a single two-sided operator: $L_{\tilde A}R_{\tilde B^{*}}$ preserves the halves only when $\tilde B=\lambda\tilde A$, and the sum of two such operators is not of the two-sided shape at all. The polarization is therefore the mechanism by which the sector-preserving set outgrows the cone: two Hermitian pairs combine into an operator of the ambient space that the cone does not contain.

**The dimensions.**

| space | real dimension |
|---|---|
| $\operatorname{End}_{\mathbb{R}}(\mathbb{B})$ | $64$ |
| sector-preserving real-linear maps | $48$ |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | $32$ |
| sector-preserving $\mathbb{C}$-linear maps, $\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi})$ | $16$ |
| Hermitian-pair cone $\operatorname{End}_{LR\ast}(\mathbb{B})$ | $7$ |

The rows are nested. The sector condition halves the complex endomorphisms, from thirty-two to sixteen, and the Hermitian-pair cone is a seven-dimensional cone inside that half. The corollary of §*The Rigidity* says that the cone is the part of the two-sided family that survives, and the table says how small that part is: seven dimensions of a sixteen-dimensional space, cut out of a complex seven-dimensional cone by a reality condition.

## The Span of the Hermitian-Pair Family

### The Hermitian Coefficient Matrix

**The expansion.** Write $\tilde Q=\sum_\mu a_\mu e_\mu$ in the units $e_t,\vec e_x,\vec e_y,\vec e_z$, with $a_\mu\in\mathbb{C}$, and put

$$
M_{\mu\nu}=L_{e_\mu}R_{e_\nu^{*}},\qquad \mu,\nu\in\{t,x,y,z\}.
$$

Expanding the two slots of the Hermitian pair gives

$$
\mathrm{Hp}_{\tilde Q}=\sum_{\mu,\nu}a_\mu\bar a_\nu\,M_{\mu\nu}.
$$

The coefficient matrix $c_{\mu\nu}=a_\mu\bar a_\nu$ is Hermitian of rank one: $c=aa^{\dagger}$ with $a$ the column of coordinates. A single Hermitian pair therefore carries a rank-one Hermitian coefficient matrix, exactly as a single two-sided operator carries a rank-one complex matrix in the expansion $L_{\tilde A}R_{\tilde B}=\sum a_\mu b_\nu M_{\mu\nu}$.

**The sixteen operators are independent.** The map $c\mapsto\sum c_{\mu\nu}M_{\mu\nu}$ is injective on Hermitian $c$. The check is a finite rank computation in the $2\times2$ model, where $M_{\mu\nu}$ acts by $\tilde X\mapsto\mathsf M_2(e_\mu)\tilde X\mathsf M_2(e_\nu)^{\dagger}$; the images of the eight basis elements $e_\mu$ and $ie_\mu$ give a $32\times16$ matrix of rank sixteen. Sixteen Hermitian parameters, sixteen independent operators.

**Proposition (the span).** The real span of the Hermitian-pair family is the whole sector-preserving space:

$$
\operatorname{span}_{\mathbb{R}}\{\mathrm{Hp}_{\tilde Q}:\tilde Q\in\mathbb{B}\}=\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi}).
$$

*Proof.* Each $\mathrm{Hp}_{\tilde Q}$ is sector-preserving, by §*Preservation of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$*, so the span is contained in the right side. Conversely, as $\tilde Q$ ranges over $\mathbb{B}$ the coefficient matrix $aa^{\dagger}$ ranges over the rank-one Hermitian matrices, and the real span of those is all of $\mathrm{Herm}_{4}(\mathbb{C})$, of real dimension sixteen. By the independence the image has real dimension sixteen, which is the dimension of $\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi})$; hence the inclusion is an equality.

**Corollary (sixteen Hermitian pairs are a basis).** Every sector-preserving $\mathbb{C}$-linear endomorphism of $\mathbb{B}$ is a real linear combination of the sixteen Hermitian pairs

$$
\mathrm{Hp}_{e_\mu},\qquad \mathrm{Hp}_{e_\mu+e_\nu},\qquad \mathrm{Hp}_{e_\mu+i e_\nu},\qquad \mu<\nu,
$$

and sixteen is the least number that works, because the target space has real dimension sixteen. The corresponding coefficient matrices are $E_{\mu\mu}$, $E_{\mu\mu}+E_{\mu\nu}+E_{\nu\mu}+E_{\nu\nu}$ and $E_{\mu\mu}+E_{\nu\nu}+i(E_{\nu\mu}-E_{\mu\nu})$, which are the four diagonal, the six real off-diagonal and the six imaginary off-diagonal Hermitian matrices: a basis of $\mathrm{Herm}_{4}(\mathbb{C})$.

**The sharpness with real parameters.** If the parameter is restricted to $\mathbb{B}_{\Psi}$ the span drops to ten, and no more is gained from the anti-Hermitian parameters, because $\mathrm{Hp}_{i\tilde Q}=\mathrm{Hp}_{\tilde Q}$ by the phase cancellation. The ten are the four $\mathrm{Hp}_{e_\mu}$ and the six $\mathrm{Hp}_{e_\mu+e_\nu}$, indexed by the symmetric square of the coordinate space. The six mixed Hermitian pairs $\mathrm{Hp}_{e_\mu+i e_\nu}$ are what the imaginary part of the parameter adds, and they are the reason the span reaches sixteen.

### The Parallel with the Two-Sided Basis

**The two bases.**

| family | indexed by | coefficients | space spanned | dimension |
|---|---|---|---|---|
| $L_{\tilde A}R_{\tilde B}$ | pairs $(\tilde A,\tilde B)\in\mathbb{B}\times\mathbb{B}$ | all $4\times4$ complex matrices | $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | $16$ complex, $32$ real |
| $\mathrm{Hp}_{\tilde Q}$ | pairs, tied by the star | Hermitian $4\times4$ matrices | $\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi})$ | $16$ real |

The two rows are the same computation read at two levels. A two-sided operator is a rank-one tensor, and the sixteen $U_{ij}[\,]U_{kl}$ of *Operators Acting on Two Sides* are the matrix units of the complex endomorphism space; a Hermitian pair is a rank-one tensor with the two slots conjugate to each other, and the sixteen Hermitian pairs are a real basis of the sector-preserving space. The number sixteen is the same in both rows because both families are indexed by pairs; the conjugation in the Hermitian pair imposes the Hermiticity of the coefficient matrix, and Hermiticity is what halves the thirty-two real dimensions of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ to the sixteen of $\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi})$.

**The length is a different question.** The spanning statement says nothing about how many terms a given operator needs. It gives an upper bound of sixteen with unrestricted real coefficients. The number of terms with coefficient one — that is, the length of an operator as a sum of Hermitian pairs — is a different invariant, and it is governed by positivity: by Choi's theorem the sums of Hermitian pairs are exactly the completely positive maps, the coefficient matrix is then positive semidefinite, and the shortest such sum has as many terms as the rank of the Choi matrix, at most four. The two statements are compatible and neither implies the other: the time reflection below needs four terms with a negative coefficient, and it is not a sum of Hermitian pairs at all.

### The Identity, the Reflection, and the General Case

**The identity.** $\mathrm{Hp}_{e_t}$ is the identity operator, so the identity is a single Hermitian pair; this is the case $\lambda=1$ of §*Both Halves Give One Condition*.

**The time reflection.** In the $2\times2$ model the map $\tilde X\mapsto(\operatorname{tr}\tilde X)\mathrm{I}_2-\tilde X$ fixes the centre and reverses the vector part; it is $\mathbb{C}$-linear and sector-preserving. The Pauli identity $\sum_\mu\sigma_\mu\tilde X\sigma_\mu^{\dagger}=2(\operatorname{tr}\tilde X)\mathrm{I}_2$ gives

$$
\tilde X\longmapsto(\operatorname{tr}\tilde X)\mathrm{I}_2-\tilde X
=-\tfrac12\mathrm{Hp}_{e_t}+\tfrac12\bigl(\mathrm{Hp}_{\vec e_x}+\mathrm{Hp}_{\vec e_y}+\mathrm{Hp}_{\vec e_z}\bigr),
$$

four Hermitian pairs, one coefficient negative. In the basis of the corollary above the coefficient vector is $(-\tfrac12,\tfrac12,\tfrac12,\tfrac12,0,\dots,0)$: the four diagonal Hermitian pairs, with the twelve mixed ones unused.

**It is not a sum of Hermitian pairs.** The Choi matrix of the reflection has the eigenvalues $(-1,1,1,1)$, so it is not positive semidefinite, and no sum of Hermitian pairs of any length equals it. The negative coefficient is therefore not an artefact of the chosen expansion: it is forced, and it is the visible sign of the operator's failure to be completely positive.

**The general case.** A generic sector-preserving map uses all sixteen basis Hermitian pairs, and several coefficients are negative. The identity uses one, the reflection four, and the count rises with the departure from the Hermitian-pair shape.

### The Cone and the Span

**The Hermitian pairs are the extreme rays.** The completely positive maps of $\mathbb{B}$ are the sums of Hermitian pairs, by *Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint*, §*Choi's Theorem and the Kraus Form*, and a sum of Hermitian pairs with coefficient one is a nonnegative real combination, because a nonnegative scalar is absorbed into the parameter, $\mu\,\mathrm{Hp}_{\tilde Q}=\mathrm{Hp}_{\sqrt{\mu}\tilde Q}$. The cone of completely positive maps is therefore exactly the cone generated by the Hermitian-pair family, and its extreme rays are the rank-one coefficient matrices, that is, the Hermitian pairs themselves.

**Two objects, one family.** The cone and the span are two readings of the same sixteen-parameter family. The cone is proper and has real dimension sixteen; the span is the linear space it generates, also of real dimension sixteen, and it contains operators outside the cone. A completely positive map is a sum of at most four Hermitian pairs with positive coefficients; a sector-preserving map is a real combination of at most sixteen. The two numbers answer different questions, and the second is not a bound on the first.

## The Norm

### $\langle\mathrm{Hp}_{\tilde Q}(\tilde X)\rangle_{\natural}=|\langle\tilde Q\rangle_{\natural}|^{2}\langle\tilde X\rangle_{\natural}$

**Proposition (the norm scaling).** For all $\tilde Q,\tilde X\in\mathbb{B}$,

$$
\langle\mathrm{Hp}_{\tilde Q}(\tilde X)\rangle_{\natural}
=|\langle\tilde Q\rangle_{\natural}|^{2}\,\langle\tilde X\rangle_{\natural}.
$$

*Proof.* The quaternionic norm is multiplicative, $\langle AB\rangle_{\natural}=\langle A\rangle_{\natural}\langle B\rangle_{\natural}$, and $\langle\tilde Q^{*}\rangle_{\natural}=\overline{\langle\tilde Q\rangle_{\natural}}$. Hence
$$
\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}
=\langle\tilde Q\rangle_{\natural}\langle\tilde X\rangle_{\natural}\overline{\langle\tilde Q\rangle_{\natural}}
=|\langle\tilde Q\rangle_{\natural}|^{2}\langle\tilde X\rangle_{\natural}.
$$

**The consequences.** The scaling factor is a nonnegative real number. The sign of the norm is preserved, so the positive and negative cones of the norm are each preserved; the null cone $\langle\tilde X\rangle_{\natural}=0$ is preserved, and the zero divisors map to zero divisors. The norm itself is preserved exactly when $|\langle\tilde Q\rangle_{\natural}|=1$, that is, on the unit-norm slice. The determinant in the $2\times2$ model is the norm and scales by $|\langle\tilde Q\rangle_{\natural}|^{2}$; in the $4\times4$ model the determinant is the square of the norm and scales by $|\langle\tilde Q\rangle_{\natural}|^{4}$, the eighth power of the modulus $r=|\langle\tilde Q\rangle_{\natural}|^{1/2}$.

### The Cancellation of the Phase

**The phase of the parameter.** For $\omega\in\mathrm{U}(1)$,

$$
\mathrm{Hp}_{\omega\tilde Q}=\mathrm{Hp}_{\tilde Q},\qquad
\langle\omega\tilde Q\rangle_{\natural}=\omega^{2}\langle\tilde Q\rangle_{\natural}.
$$

The phase of $\tilde Q$ cancels in the operator, and the phase of the norm cancels in the modulus: $|\langle\omega\tilde Q\rangle_{\natural}|=|\langle\tilde Q\rangle_{\natural}|$. The norm formula therefore depends only on the modulus of the norm, not on its argument.

**What the operator sees.** The Hermitian pair sees the orbit $\mathrm{U}(1)\cdot\tilde Q$ and the modulus $|\langle\tilde Q\rangle_{\natural}|$. It does not see the phase of $\tilde Q$ or the phase of the norm. The parameter of the Hermitian pair is a point of $\mathbb{B}/\mathrm{U}(1)$; the positive real scale is its modulus, and the phase is the kernel of the parameter map.

**The real form.** The norm is a complex quadratic form on the complex algebra; on the Hermitian half it is real, and on the anti-Hermitian half it is real with the opposite sign. The Hermitian pair scales it by the nonnegative factor $|\langle\tilde Q\rangle_{\natural}|^{2}$, so it preserves the common zero set and the sign of the norm on each half. The two halves are the two real readings of the same complex form.

## The Parameter Modulo $\mathrm{U}(1)$

### The Real Dimension Seven

**The action.** The group $\mathrm{U}(1)=\{\omega e_t:|\omega|=1\}$ acts on the parameter by $\tilde Q\mapsto\omega\tilde Q$. The Hermitian pair is invariant, by §*The Cancellation of the Phase*. The map $\tilde Q\mapsto\mathrm{Hp}_{\tilde Q}$ factors through the quotient $\mathbb{B}/\mathrm{U}(1)$.

**The fibre.** Suppose $\mathrm{Hp}_{\tilde Q}=\mathrm{Hp}_{\tilde Q_2}$ with $\tilde Q,\tilde Q_2\neq0$. Then $L_{\tilde Q}R_{\tilde Q^{*}}=L_{\tilde Q_2}R_{\tilde Q_2^{*}}$. By the fibre theorem of *Operators Acting on Two Sides*, §*The Scaling Orbit*, the two pairs are proportional:

$$
\tilde Q_2=\lambda\tilde Q,\qquad \tilde Q_2^{*}=\lambda^{-1}\tilde Q^{*}
$$

for some $\lambda\in\mathbb{C}^{\times}$. Conjugating the first equation gives $\tilde Q_2^{*}=\bar\lambda\tilde Q^{*}$; comparing with the second gives $\lambda^{-1}=\bar\lambda$, hence $|\lambda|=1$. Therefore $\tilde Q_2=\lambda\tilde Q$ with $|\lambda|=1$, and the fibre is exactly the $\mathrm{U}(1)$ orbit. The zero operator is the image of $\tilde Q=0$ alone.

**The dimension.** The parameter space $\mathbb{B}$ has complex dimension four, real dimension eight. The $\mathrm{U}(1)$ orbit is one real dimension, and it acts freely on $\mathbb{B}\setminus\{0\}$. The quotient has real dimension $8-1=7$, and the cone has real dimension seven. The dimension is real, not complex: the quotient $\mathbb{B}/\mathrm{U}(1)$ is the real cone over $\mathbb{CP}^{3}$, not a complex vector space, and the parameter map is quadratic. This is the row of the table: $\operatorname{End}_{LR\ast}(\mathbb{B})$ has real dimension seven, while $\operatorname{End}_{LR}(\mathbb{B})$ has complex dimension seven.

**The cone.** The image is a cone over the complex projective space $\mathbb{CP}^{3}$: the parameter modulo the positive real scale and the phase. The quotient of $\mathbb{B}\setminus\{0\}$ by $\mathrm{U}(1)$ and $\mathbb{R}_{>0}$ is $\mathbb{CP}^{3}$, of real dimension six, and the cone has real dimension seven. The image is the set of Hermitian pairs, a real cone of dimension seven. It is not a subspace: the sum of two Hermitian pairs is not a Hermitian pair in general, and the cone is not closed under multiplication by $i$ unless the parameter is scaled by a real number.

## The Intersections with $L(\mathbb{B})$ and $R(\mathbb{B})$

### The Closed Ray of the Identity

**The statement.** The Hermitian-pair cone meets each one-sided family in the same closed ray:

$$
\operatorname{End}_{LR\ast}(\mathbb{B})\cap L(\mathbb{B})
=\operatorname{End}_{LR\ast}(\mathbb{B})\cap R(\mathbb{B})
=\{t\,\mathrm{I}:t\ge0\}.
$$

The ray is the closed ray of nonnegative multiples of the identity; the identity is the point $t=1$, and the zero operator is the point $t=0$.

**The proof.** Write $\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$. If $\mathrm{Hp}_{\tilde Q}=L_{\tilde A}$, then $R_{\tilde Q^{*}}=L_{\tilde A}L_{\tilde Q}^{-1}$ when $\tilde Q$ is a unit, so $R_{\tilde Q^{*}}$ lies in $L(\mathbb{B})\cap R(\mathbb{B})$. The intersection of the two one-sided families is the scalars, by *Operators Acting on One Side*, so $R_{\tilde Q^{*}}$ is a scalar; hence $\tilde Q^{*}$ is central and $\tilde Q$ is central. If $\tilde Q$ is a zero divisor, it has $2\times2$ rank one, and then $\tilde Q\tilde X\tilde Q^{*}$ lies in the complex line through $\tilde Q\tilde Q^{*}$ for every $\tilde X$, so $\mathrm{Hp}_{\tilde Q}$ has complex rank at most one, while a nonzero $L_{\tilde A}$ has complex rank two or four. Hence $\tilde A=0$ and $\mathrm{Hp}_{\tilde Q}=0$; evaluating at $e_t$ gives $\tilde Q\tilde Q^{*}=0$, which forces $\tilde Q=0$. In every case $\tilde Q=\lambda e_t$, and $\mathrm{Hp}_{\tilde Q}=|\lambda|^{2}\mathrm{I}$ is a nonnegative multiple of the identity. The same argument with the roles exchanged gives the intersection with $R(\mathbb{B})$.

**The ray is not a subspace.** The ray is a half-line, not a line: the negative multiples of the identity are not in the cone, because they would require $|\lambda|^{2}<0$. The ray is a boundary face of the cone along the central direction; it is the only part of the Hermitian-pair cone that is one-sided. The two intersections are the same ray.

**The contrast.** The full product set of the two-sided family meets $L(\mathbb{B})$ in all of $L(\mathbb{B})$ and $R(\mathbb{B})$ in all of $R(\mathbb{B})$, because $L_{\tilde Q}R_{e_t}=L_{\tilde Q}$ and $L_{e_t}R_{\tilde Q_2}=R_{\tilde Q_2}$. The Hermitian pair is the graph $\tilde Q_2=\tilde Q^{*}$, and the graph meets the two axes only at the central ray. The two intersections of the product set are distinct; the two intersections of the Hermitian pair are the same ray.

## The Spectrum

### The Four Products $\lambda_i\bar\lambda_j$

**The statement.** Let $\lambda_1,\lambda_2$ be the eigenvalues of the $2\times2$ matrix $\mathsf M_2(\tilde Q)$. The eigenvalues of $\mathrm{Hp}_{\tilde Q}$ on $\mathbb{B}$ are the four products

$$
\lambda_i\bar\lambda_j,\qquad i,j\in\{1,2\}.
$$

The trace and the determinant follow:

$$
\operatorname{Tr}\mathrm{Hp}_{\tilde Q}=|\lambda_1+\lambda_2|^{2}=4|Q_t|^{2},\qquad
\det\mathrm{Hp}_{\tilde Q}=|\lambda_1\lambda_2|^{4}=|\langle\tilde Q\rangle_{\natural}|^{4}.
$$

**The reading.** The diagonal products $\lambda_i\bar\lambda_i=|\lambda_i|^{2}$ are nonnegative real; the two off-diagonal products are conjugate to each other. The spectrum is invariant under the phase of $\tilde Q$, and it depends only on the eigenvalues of the $2\times2$ model. If $\tilde Q$ is a unit, all four products are nonzero; if $\tilde Q$ is a null element, at least one eigenvalue is zero, and at least two products vanish. If $\tilde Q$ is central, $\lambda_1=\lambda_2=\lambda$, and all four products are $|\lambda|^{2}$; the Hermitian pair is the scalar $|\lambda|^{2}\mathrm{I}$.

**The verification.** The matrix verification is in *The Polar Decomposition and Remarkable Subspaces*, §*The Anti-Hermitian Half as Four-Vectors* and §*The Two Halves Are One Action*, both in that article. In the $2\times2$ model the Hermitian pair is the congruence $X\mapsto MXM^{\dagger}$; its eigenvalues are the products of an eigenvalue of $M$ with the conjugate of an eigenvalue of $M$, which is the display. The abstract statement is the same computation read in the $2\times2$ model of the algebra; the spectrum is a similarity invariant, so the choice of model does not change it.

**The trace.** The trace is $|\operatorname{Tr}\mathsf M_2(\tilde Q)|^{2}=4|Q_t|^{2}$, the squared modulus of the trace of the model matrix. The determinant is the fourth power of the modulus of the norm, $|\langle\tilde Q\rangle_{\natural}|^{4}$, which is also the determinant of the Hermitian pair as a linear operator on the complex four-dimensional algebra. The two invariants are real and nonnegative; the spectrum carries the phase information in its off-diagonal pair.

## The Image and the Kernel

### $\mathrm{U}(1)$ and $CO^{+}(1,3)$

**The parameter map on the unit group.** The map

$$
\mathrm{J}:\mathbb{B}^{\times}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\tilde Q\longmapsto\mathrm{Hp}_{\tilde Q}
$$

is a group anti-homomorphism. Its kernel is the central $\mathrm{U}(1)=\{\omega e_t:|\omega|=1\}$, by §*The Parameter Modulo $\mathrm{U}(1)$*. Its image, read on the anti-Hermitian half, is the conformal group

$$
CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3),
$$

of real dimension seven. The general element $\tilde Q=r\omega\tilde U$ with $r>0$, $|\omega|=1$ and $|\langle\tilde U\rangle_{\natural}|=1$ gives $\mathrm{Hp}_{\tilde Q}=r^{2}\mathrm{Hp}_{\tilde U}$: the phase cancels, the modulus squared is the dilation, and the unit part is the Lorentz transformation.

**The kernel of the linear map.** The kernel of the linear map $\mathrm{Hp}_{\tilde Q}$ for a fixed $\tilde Q$ is a different object. It is $\{0\}$ exactly when $\tilde Q$ is a unit; if $\tilde Q$ is a null element, the kernel is nonzero. The kernel of the parameter map is the $\mathrm{U}(1)$ orbit; the kernel of the linear map is $\{\tilde X:\tilde Q\tilde X\tilde Q^{*}=0\}$. The two kernels are stated separately, and neither is the other.

**The image of the linear map.** For a unit $\tilde Q$, $\mathrm{Hp}_{\tilde Q}$ is a linear isomorphism of $\mathbb{B}$; for a null element it has a nonzero kernel and a proper image. The image of the parameter map is the Hermitian-pair cone of the Introduction; the image of the linear map is the whole algebra or a proper subspace, according to the rank of $\tilde Q$. The rank of $\mathrm{Hp}_{\tilde Q}$ is the square of the rank of $\tilde Q$: the image is $\tilde Q\mathbb{B}\tilde Q^{*}$, of complex dimension $\operatorname{rank}(\tilde Q)^{2}$.

### $SL_2(\mathbb{C})\to SO^{+}(1,3)$ on the Norm-One Slice

**The slice.** On the norm-one slice $\mathbb{B}_1^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=1\}$, the group is $SL_2(\mathbb{C})$, of real dimension six. The parameter map restricts to

$$
SL_2(\mathbb{C})\longrightarrow SO^{+}(1,3),\qquad
\tilde Q\longmapsto\mathrm{Hp}_{\tilde Q},
$$

a twofold cover. The kernel is $\{\pm e_t\}$; the image is the identity component of the Lorentz group; both groups have real dimension six. The kernel and the image are stated per slice: on $\mathbb{B}^{\times}$ the kernel is $\mathrm{U}(1)$ and the image is $CO^{+}(1,3)$; on $\mathbb{B}_1^{\times}$ the kernel is $\{\pm e_t\}$ and the image is $SO^{+}(1,3)$.

**The Lorentz action.** The anti-Hermitian half is a real four-dimensional space with the Minkowski form of signature $(3,1)$. A unit-norm Hermitian pair preserves the form, because the norm scales by $|\langle\tilde Q\rangle_{\natural}|^{2}=1$. The map is continuous, $SL_2(\mathbb{C})$ is connected, and the kernel is $\{\pm e_t\}$; hence the image is the identity component $SO^{+}(1,3)$. The Hermitian half carries the same action composed with the exchange by $i$, with the opposite sign of the form. The matrix verification is in *The Polar Decomposition and Remarkable Subspaces*, §*The Anti-Hermitian Half as Four-Vectors* and §*The Two Halves Are One Action*.

**The conformal extension.** For a general unit $\tilde Q=r\omega\tilde U$, the Hermitian pair is $r^{2}\mathrm{Hp}_{\tilde U}$: a Lorentz transformation composed with the dilation of ratio $r^{2}$ on the algebra, $r^{4}$ on the norm and $r^{8}$ on the $4\times4$ determinant. The image is the conformal group $CO^{+}(1,3)$; the kernel remains the central $\mathrm{U}(1)$, and the scale is the positive real factor. The unit-norm slice is the subgroup on which the dilation is one; the general unit group adds the dilation and the phase, and the phase is the kernel.

## Summary

The Hermitian pair is $\mathrm{Hp}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$, the member $L_{\tilde Q}R_{\tilde Q^{*}}$ of the two-sided family. It is a real cone of real dimension seven, the graph of the involution inside the complex two-sided cone; the phase of the parameter cancels, and complex rescaling acts by the square of the modulus. It is multiplicative up to the order of the factors, $\mathrm{Hp}_{\tilde Q}\mathrm{Hp}_{\tilde Q_2}=\mathrm{Hp}_{\tilde Q\tilde Q_2}$, and its defect from an algebra automorphism is $e_t-\tilde Q^{*}\tilde Q$; the defect vanishes exactly on the central multiples of real unit quaternions. It preserves the Hermitian and anti-Hermitian halves for every parameter, and the finer subspace structure exactly on that same set. The preservation is not a constraint on the parameter but a property of the involution: the three conditions $T(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Phi}$, preservation of both halves, and $TJ=JT$ with $J(\tilde X)=\tilde X^{*}$ are equivalent, and $\mathrm{Hp}_{\tilde Q}$ satisfies all three for every $\tilde Q$. Conversely, inside the two-sided family the sector condition forces the shape: $L_{\tilde A}R_{\tilde B}$ preserves $\mathbb{B}_{\Phi}$ into itself exactly when $\tilde B=\lambda\tilde A^{*}$ with $\lambda$ real, and the same condition, with the same $\lambda$, is what preserves $\mathbb{B}_{\Psi}$ into itself; the two conditions are one condition, and the sector-preserving two-sided operators are the real multiples of the Hermitian pairs, with the cone itself corresponding one-to-one to $\mathbb{B}/\mathrm{U}(1)$ and the cone being one half of that set, the negative multiples being no Hermitian pairs. The argument of $\lambda$ decides the fate of the halves: real keeps both, purely imaginary swaps them, and a $\lambda$ with both parts nonzero destroys both. The Hermitian pair is the case $\lambda=1$, which is why it needs no hypothesis on its parameter. The one-sided multiplications preserve the halves only at a real scalar, because the star is conjugate-linear and the Hermitian pair is the combination in which the conjugate-linearity occurs twice. The sector-preserving $\mathbb{C}$-linear maps form a real space of dimension sixteen, $\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi})$, and forty-eight without $\mathbb{C}$-linearity; the cone is seven-dimensional inside the sixteen. The Hermitian pair family spans that sixteen-dimensional space: writing $\mathrm{Hp}_{\tilde Q}=\sum_{\mu\nu}a_\mu\bar a_\nu M_{\mu\nu}$ with $M_{\mu\nu}=L_{e_\mu}R_{e_\nu^{*}}$, the coefficient matrix $aa^{\dagger}$ is Hermitian of rank one, the sixteen Hermitian coefficients are independent, and the sixteen Hermitian pairs $\mathrm{Hp}_{e_\mu}$, $\mathrm{Hp}_{e_\mu+e_\nu}$ and $\mathrm{Hp}_{e_\mu+i e_\nu}$ are a real basis. Every sector-preserving map is therefore a real combination of sixteen Hermitian pairs, the identity being one Hermitian pair and the time reflection four with one negative coefficient, while the completely positive maps are the sums and have Kraus length at most four: the sixteen is a spanning number, the four a length, and the time reflection, whose Choi matrix has eigenvalue $-1$, shows that the two are different. It scales the norm by $|\langle\tilde Q\rangle_{\natural}|^{2}$, preserves the null cone and the sign of the norm, and sees only the modulus of the norm. The parameter is defined modulo the central $\mathrm{U}(1)$, which gives the real dimension seven. The Hermitian pair meets each one-sided family in the closed ray of nonnegative multiples of the identity. Its spectrum is the four products $\lambda_i\bar\lambda_j$ of the eigenvalues of the $2\times2$ model with their conjugates; the trace is $4|Q_t|^{2}$ and the determinant is $|\langle\tilde Q\rangle_{\natural}|^{4}$. On the unit group the parameter map has kernel $\mathrm{U}(1)$ and image $CO^{+}(1,3)$; on the norm-one slice it is the twofold cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$ with kernel $\{\pm e_t\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Hp}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the Hermitian pair |
| $L_{\tilde Q}R_{\tilde Q_2}$ | the two-sided operator; $\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ |
| $\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | the Hermitian and anti-Hermitian halves, real dimension four each |
| $\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm; $\langle\mathrm{Hp}_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}$ |
| $\mathrm{U}(1)$ | the central phase $\{\omega e_t:\lvert\omega\rvert=1\}$ |
| $\operatorname{End}_{LR\ast}(\mathbb{B})$ | the real cone of Hermitian pairs, real dimension seven |
| $J(\tilde X)=\tilde X^{*}$ | the real structure; the sector condition is $TJ=JT$ |
| $\operatorname{End}_{\mathbb{R}}(\mathbb{B}_{\Psi})$ | the sector-preserving $\mathbb{C}$-linear endomorphisms, real dimension sixteen |
| $M_{\mu\nu}=L_{e_\mu}R_{e_\nu^{*}}$ | the sixteen elementary operators; $\mathrm{Hp}_{\tilde Q}=\sum_{\mu\nu}a_\mu\bar a_\nu M_{\mu\nu}$ |
| $aa^{\dagger}$ | the Hermitian rank-one coefficient matrix of $\mathrm{Hp}_{\tilde Q}$, with $a$ the coordinates of $\tilde Q$ |
| $\lambda$ in $\tilde B=\lambda\tilde A^{*}$ | the real scalar of the sector-preserving two-sided operators |
| $L(\mathbb{B}),R(\mathbb{B})$ | the left and right regular families |
| $\lambda_1,\lambda_2$ | the eigenvalues of the $2\times2$ model $\mathsf M_2(\tilde Q)$ |
| $CO^{+}(1,3)$ | the conformal proper orthochronous Lorentz group |
| $SO^{+}(1,3)$ | the proper orthochronous Lorentz group |
| $SL_2(\mathbb{C})$ | the norm-one slice $\mathbb{B}_1^{\times}$ |

## Further Reading

- [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html), for the other placement of the same pair, the pair of equations it writes, and the transposition that rewrites the right member as a left one.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the two-sided family, the scaling orbit and the composition.
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the adjoints of the Hermitian pair.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the criterion on the parameter, the congruence in the $2\times2$ model, and the action on the six subspaces.
- [Operator Family Conventions](operator-family-conventions.html), for the names of the families and the sets.
- [Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint](completely-positive-maps-of-a-hermitian-algebra-with-hermitian-adjoint.html), for Choi's theorem, the Kraus form, and the sums of Hermitian pairs.
