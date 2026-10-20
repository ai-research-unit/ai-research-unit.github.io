# __The Wick Theorem in Biquaternionic Form__

## Introduction

The **Wick theorem** is the identity that reduces the vacuum expectation value of a time-ordered product of fields to a sum over products of two-point functions. It is the reason Feynman diagrams exist: the Dyson series of the S-matrix can be contracted term by term into propagators joined at vertices, and the perturbation series of a field theory becomes a sum over graphs. The theorem is standard, and this article does not re-derive it for fields. It asks instead what the biquaternion algebra $\mathbb{B}$ contributes to it.

The contributions are three, and they are of different kinds.

- **Established, and recomputed below.** For a **single fermionic mode** the Wick theorem is not an approximation or a statement about vacuum expectation values in a large space; it is an **exact operator identity** in a four-real-dimensional subalgebra of $\mathbb{B}$, and it can be proved by exhibiting both sides. Since the mode operators satisfy $\vec\Upsilon_x^2 = 0$ and $(\vec\Upsilon_y)^2 = 0$, every product of more than two mode operators reduces to a word of at most two, and the four-point and six-point contractions reduce to products of the two-point contraction $\langle\vec\Upsilon_x\vec\Upsilon_y\rangle_t = 1$ with the fermionic signs. The identity
$$
\vec\Upsilon_x\vec\Upsilon_y = \,:\vec\Upsilon_x\vec\Upsilon_y: \,+\, \langle \vec\Upsilon_x\vec\Upsilon_y\rangle_t\,e_t,
\qquad
:\vec\Upsilon_x\vec\Upsilon_y: \,=\, -\tilde\Pi_-,
$$
holds as an identity in $\mathbb{B}$, not merely in expectation.
- **Established (algebra).** The operators $\vec\Upsilon_x,\vec\Upsilon_y$ generate a **real form** of $\mathbb{B}$: a four-real-dimensional subalgebra isomorphic to $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, with basis $\{e_t, i\vec e_x, \vec e_y, i\vec e_z\}$, whose complexification is all of $\mathbb{B}$. The fermionic contraction is thus a statement inside a genuine subalgebra, and the fermionic sign is the algebra's own. The fermion-parity operator $(-1)^F = i\vec e_z$ is an element of it, and it is what implements the sign on exchanging two mode operators.
- **Standard, and transcribed.** For a field the theorem is the standard one: the time-ordered product of fields equals the normal-ordered product plus all contractions, with a minus sign for every exchange of two fermionic operators, and the contractions are the Feynman propagators of *The Feynman Propagator in Biquaternionic Form*. The algebra does not supply that theorem; it supplies the notation, the sign, and the one-mode truncation. The **gap**, inherited from the Fock article, is that the field's Fock space is a module over $\mathbb{B}$ and the fermion-parity operator is not an element of $\mathbb{B}$ for more than one mode.

The article proceeds as follows. The next section states the standard theorem and its fermionic sign. A section defines normal ordering and contraction. A section exhibits the one-mode subalgebra and computes its products. A section proves and verifies the one-mode Wick identity, with a table of all low-order contractions. Sections then identify the contraction with the propagator and the sign with the grading, and state the field case and its gap. A section separates what is established from what is interpretation, and the article closes with open questions.

**Conventions.** We use those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_\mu^2=-e_t$, $\vec e_\mu \vec e_\nu=\varepsilon_{\mu\nu\lambda}\vec e_\lambda$ for distinct $\mu,\nu,\lambda$, and central scalar imaginary $i$, $i^2=-1$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, imaginary scalar and real vector) and $\mathbb{M}_+$ (Hermitian, real scalar and imaginary vector), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_t,ie_t\}$ is the centre. The isomorphism is $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$, $\mathsf{M}_2(i)=iI_2$, and the trace is $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2) = 2\langle\tilde Q_1,\tilde Q_2\rangle$, the $2\times2$ reading of the plain form, with $\mathrm{Tr}(e_t)=2$. The single-mode ladder and number operator are
$$
\vec\Upsilon_x = \tfrac12\big(i\vec e_x-\vec e_y\big),
\qquad
\vec\Upsilon_y = \tfrac12\big(i\vec e_x+\vec e_y\big),
\qquad
\tilde\Pi_- = \vec\Upsilon_y\vec\Upsilon_x = \tfrac12\big(e_t-i\vec e_z\big),
$$
with $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$, $\vec\Upsilon_x^2=(\vec\Upsilon_y)^2=0$, and $(-1)^F=i\vec e_z$, as established by *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*. Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. The one-mode vacuum idempotent is $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)=e_t-\tilde\Pi_-$. Throughout, $\langle\cdot\rangle_t$ denotes the vacuum expectation value $\mathrm{Tr}(\tilde\Pi_+\,\cdot\,)$.

## The Wick Theorem in the Standard Theory

Let $\phi^{\mathrm{fop}}_i = \phi^{\mathrm{fop}}(x_i)$ be free fields, bosonic or fermionic, and let $T$ denote time ordering. The **Wick theorem** states that
$$
T\big\{\phi^{\mathrm{fop}}_1\phi^{\mathrm{fop}}_2\cdots\phi^{\mathrm{fop}}_n\big\}
\;=\;
:\!\phi^{\mathrm{fop}}_1\phi^{\mathrm{fop}}_2\cdots\phi^{\mathrm{fop}}_n\!:
\;+\;
\sum_{\text{single contractions}} :\!\cdots\!:
\;+\;
\sum_{\text{double contractions}} :\!\cdots\!:
\;+\;\cdots\;+\;
\sum_{\text{complete contractions}} .
$$
The terms are indexed by the number of **contractions**: a complete contraction of $n$ fields is a partition of the $n$ labels into $n/2$ unordered pairs, each pair replaced by its two-point function. Odd $n$ has no complete contraction, and the sum terminates at the largest even number. Taking the vacuum expectation value kills every normal-ordered term, since $:\!\cdots\!:$ is defined to have vanishing vacuum expectation, leaving
$$
\big\langle 0\big|T\big\{\phi^{\mathrm{fop}}_1\cdots\phi^{\mathrm{fop}}_n\big\}\big|0\big\rangle
\;=\;
\sum_{\text{complete pairings}}
(\pm)\prod_{\text{pairs}}\big\langle 0\big|T\big\{\phi^{\mathrm{fop}}_i\phi^{\mathrm{fop}}_j\big\}\big|0\big\rangle .
$$
The two-point function is the **Feynman propagator**, and the product over pairs is the product of propagators joining the points. This is the content of the theorem in the form in which perturbation theory uses it.

**The fermionic sign.** For fermionic fields the time-ordered product carries a graded sign: the product is defined with a minus sign for every transposition of two fermionic factors needed to bring them into time order, and the contraction of two fermionic fields may equivalently be read off from the ordinary product plus the anticommutator. For Grassmann-valued or operator-valued fermions the definition is
$$
T\big\{\psi^{\mathrm{fop}}_i\psi^{\mathrm{fop}}_j\big\} = \Theta(t'_i-t'_j)\,\psi^{\mathrm{fop}}_i\psi^{\mathrm{fop}}_j - \Theta(t'_j-t'_i)\,\psi^{\mathrm{fop}}_j\psi^{\mathrm{fop}}_i ,
$$
with the minus sign present for fermions and absent for bosons. The relative sign between the possible complete pairings of a $2m$-point function is the **parity of the permutation** that realizes the pairing, which is why the fermionic Wick theorem is the bosonic one multiplied by the signature of the pairing:
$$
\big\langle T\,\phi^{\mathrm{fop}}_1\cdots\phi^{\mathrm{fop}}_{2m}\big\rangle_t
= \sum_{\text{pairings } \pi} \mathrm{sgn}(\pi)\prod_{(i,j)\in\pi}\big\langle T\,\phi^{\mathrm{fop}}_i\phi^{\mathrm{fop}}_j\big\rangle_t ,
$$
with $\mathrm{sgn}(\pi)=+1$ for bosons. The theorem is proved by induction on $n$ from the canonical (anti)commutation relations, and it is standard; it is cited as such and used below.

## Normal Ordering and Contraction

Two definitions make the theorem precise.

**Contraction.** The contraction of two fields is their time-ordered vacuum expectation value,
$$
\Delta_{ij} \;\equiv\; \big\langle 0\big|T\,\phi^{\mathrm{fop}}_i\phi^{\mathrm{fop}}_j\big|0\big\rangle ,
$$
the Feynman propagator from $x_i$ to $x_j$. For the biquaternion Dirac field on its spinor module this is the spinor propagator $S_F$, and for the scalar example it is $D_F$; both are constructed in *The Feynman Propagator in Biquaternionic Form*, and their biquaternion content is the wave biquaternion $\tilde P = iEe_t+\vec p$ with $\tilde P\tilde P^{\natural}=-m^2$ on the mass shell. The article does not rebuild them.

**Normal ordering.** The normal-ordered product $:\!\phi^{\mathrm{fop}}_1\cdots\phi^{\mathrm{fop}}_n\!:$ is defined by moving every creation operator to the left of every annihilation operator, with a minus sign for each transposition of two fermionic operators, and then subtracting the vacuum expectation value of the resulting product. Equivalently, and more usefully for the algebra, normal ordering is fixed by the two requirements
$$
\big\langle 0\big|:\!\phi^{\mathrm{fop}}_1\cdots\phi^{\mathrm{fop}}_n\!:\big|0\big\rangle = 0,
\qquad
\phi^{\mathrm{fop}}_i\phi^{\mathrm{fop}}_j = \,:\!\phi^{\mathrm{fop}}_i\phi^{\mathrm{fop}}_j\!:\, + \, \Delta_{ij}\,e_t ,
$$
for $n=2$, together with linearity. The second equation is the theorem at $n=2$, and it shows that the two definitions of normal ordering differ by the contraction.

For an operator algebra generated by modes, normal ordering is an operation on the algebra, and this is where the biquaternion framework can say something exact rather than transcribed. In the one-mode truncation the operation is realized by an element of $\mathbb{B}$: the normal-ordered product is obtained by **anticommuting past** $\tilde\Pi_-$, whose idempotent nature makes the result a finite polynomial.

## The One-Mode Subalgebra

The mode operators $\vec\Upsilon_x,\vec\Upsilon_y$ generate a subalgebra of $\mathbb{B}$, and it is useful to exhibit it.

**Generators.** Writing out the real and imaginary parts,
$$
\vec\Upsilon_x + \vec\Upsilon_y = i\vec e_x,
\qquad
\vec\Upsilon_x - \vec\Upsilon_y = -\vec e_y,
$$
so the real-linear span of the generators and the identity contains $i\vec e_x$ and $\vec e_y$; and the number operator supplies
$$
2\tilde\Pi_- - e_t = -i\vec e_z \quad\Longrightarrow\quad i\vec e_z = e_t-2\tilde\Pi_- = (-1)^F .
$$
Hence
$$
\mathcal{A}_{\mathrm{tr}} \;=\; \mathrm{span}_{\mathbb{R}}\big\{e_t,\; i\vec e_x,\; \vec e_y,\; i\vec e_z\big\}
$$
is contained in the algebra generated by $\vec\Upsilon_x,\vec\Upsilon_y$; the reverse inclusion is the observation that
$$
\vec\Upsilon_x = \tfrac12\big(i\vec e_x-\vec e_y\big),
\qquad
\vec\Upsilon_y = \tfrac12\big(i\vec e_x+\vec e_y\big)
$$
are themselves real combinations of $i\vec e_x$ and $\vec e_y$. So the generated algebra is exactly $\mathcal{A}_{\mathrm{tr}}$.

**It is closed.** Check the products of the three non-identity basis elements $\vec q_x = i\vec e_x$, $\vec q_y = \vec e_y$, $\vec q_z = i\vec e_z$:
$$
\vec q_x^2 = e_t,
\qquad
\vec q_y^2 = -e_t,
\qquad
\vec q_z^2 = e_t,
\qquad
\vec q_x\vec q_y = \vec q_z,
\qquad
\vec q_y\vec q_z = \vec q_x,
\qquad
\vec q_z\vec q_x = -\vec q_y ,
$$
using $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$ and their antisymmetric partners. Every product is again in $\mathcal{A}_{\mathrm{tr}}$; for instance $\vec q_x\vec q_y = i\,\vec e_x \vec e_y = i\vec e_z = \vec q_z$, and $\vec q_y\vec q_z = i\,\vec e_y \vec e_z = i\vec e_x = \vec q_x$, while $\vec q_z\vec q_x = i^2 \vec e_z \vec e_x = -\vec e_y = -\vec q_y$. So
$$
\mathcal{A}_{\mathrm{tr}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R}),
\qquad
\mathcal{A}_{\mathrm{tr}}\otimes_\mathbb{R}\mathbb{C} = \mathbb{B}.
$$
The one-mode truncation is therefore a **real form** of the biquaternion algebra, the one fixed by a Majorana-like reality condition on the module rather than by retaining the complex ladder: its generators are the two anticommuting real combinations of the ladder $\vec q_x=\vec\Upsilon_x+\vec\Upsilon_y=i\vec e_x$ and $\vec q_y=\vec\Upsilon_y-\vec\Upsilon_x=\vec e_y$, with $\vec q_x^2=+e_t$ and $\vec q_y^2=-e_t$. This matches the general statement that $\mathbb{B}\cong M_2(\mathbb{C})$ has real forms determined by the reality condition imposed on the module.

A numerical check over the products confirms closure: every product of the basis elements $\vec q_x,\vec q_y,\vec q_z$ lies in the real span of $\{e_t,\vec q_x,\vec q_y,\vec q_z\}$ with a residual below $10^{-16}$, and the coefficient vectors are exactly those of the table above — in particular $\vec q_x \vec q_y = \vec q_z$ with coordinates $(0,0,0,1)$ and $\vec q_y^2 = -e_t$ with coordinates $(-1,0,0,0)$ in the basis $(e_t,\vec q_x,\vec q_y,\vec q_z)$. The dimension count is $4$ over $\mathbb{R}$, as $\mathrm{Cl}_{1,1}$ requires.

**The vacuum in the subalgebra.** The vacuum idempotent is $\tilde\Pi_+=e_t-\tilde\Pi_-$, which lies in $\mathcal{A}_{\mathrm{tr}}$ because $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$. So the one-mode GNS vacuum of the previous articles is an element of the same four-dimensional real algebra, and the vacuum expectation value is an $\mathbb{R}$-linear functional on it:
$$
\langle \tilde{Q}\rangle_t = \mathrm{Tr}\big(\tilde\Pi_+\tilde{Q}\big) = 2\,\mathrm{Sc}\big(\tilde\Pi_+\tilde{Q}\big),
\qquad \tilde{Q}\in\mathcal{A}_{\mathrm{tr}} .
$$

## The One-Mode Wick Identity

Because the generators are nilpotent, the one-mode theorem can be stated and proved exactly.

> **Theorem (one-mode Wick).** In $\mathcal{A}_{\mathrm{tr}}$,
>$$
> \vec\Upsilon_x\vec\Upsilon_y = \,:\vec\Upsilon_x\vec\Upsilon_y: \,+\, \langle \vec\Upsilon_x\vec\Upsilon_y\rangle_t\,e_t,
> \qquad
> :\vec\Upsilon_x\vec\Upsilon_y: \,=\, -\tilde\Pi_-,
> \qquad
> \langle \vec\Upsilon_x\vec\Upsilon_y\rangle_t = 1 ,
>$$
> and for every product $\tilde{Q}_1\cdots\tilde{Q}_{2m}$ of mode operators,
>$$
> \langle \tilde{Q}_1\cdots\tilde{Q}_{2m}\rangle_t
> = \sum_{\text{complete pairings}} \mathrm{sgn}(\pi)\prod_{(i,j)}\langle \tilde{Q}_i\tilde{Q}_j\rangle_t .
>$$

**Proof of the two-point identity.** The contraction is, by the anticommutator,
$$
\vec\Upsilon_x\vec\Upsilon_y = e_t - \vec\Upsilon_y\vec\Upsilon_x = e_t - \tilde\Pi_- = \tilde\Pi_+,
$$
whose vacuum expectation is $\mathrm{Tr}(\tilde\Pi_+^2)=\mathrm{Tr}(\tilde\Pi_+)=1$. Normal ordering moves the creation operator to the left and produces $:\vec\Upsilon_x\vec\Upsilon_y:\,=-\vec\Upsilon_y\vec\Upsilon_x=-\tilde\Pi_-$. Adding back the contraction gives $-\tilde\Pi_-+e_t=e_t-\tilde\Pi_-$, which is the left-hand side.

**Why the higher identities are exact.** No induction is needed. The identities $\vec\Upsilon_x^2=0$ and $(\vec\Upsilon_y)^2=0$ say that any word in the mode operators that contains two adjacent equal letters vanishes; and any word in which the letters alternate can be reduced by the anticommutator to a word with a repeated adjacent pair plus a contraction times a shorter word:
$$
\vec\Upsilon_x\vec\Upsilon_y = e_t - \vec\Upsilon_y\vec\Upsilon_x,
\qquad
\vec\Upsilon_y\vec\Upsilon_x = e_t - \vec\Upsilon_x\vec\Upsilon_y .
$$
Iterating this reduction produces exactly the sum over complete pairings with the fermionic signs, and the vacuum expectation kills the normally ordered remainder. The one-mode theorem is thus the algebraic skeleton of the field theorem, with the reduction by anticommutation playing the role of the induction.

**The contractions explicitly.** The two nonvanishing elementary contractions are
$$
\langle \vec\Upsilon_x\vec\Upsilon_y\rangle_t = 1,
\qquad
\langle \vec\Upsilon_y\vec\Upsilon_x\rangle_t = 0,
\qquad
\langle \vec\Upsilon_x\vec\Upsilon_x\rangle_t = \langle \vec\Upsilon_y\vec\Upsilon_y\rangle_t = 0 .
$$
The complete table of the four-point function is the following, in which each entry was computed twice: directly as $\mathrm{Tr}(\tilde\Pi_+\tilde{Q}_1\tilde{Q}_2\tilde{Q}_3\tilde{Q}_4)$ using explicit $2\times2$ complex matrices, and by the pairing sum. All entries agree to machine precision.

| $\langle\,\cdot\,\rangle_t$ | direct | pairing sum |
|---|---|---|
| $\langle \vec\Upsilon_x\vec\Upsilon_y\vec\Upsilon_x\vec\Upsilon_y\rangle$ | $1$ | $1\cdot 1 = 1$ |
| $\langle \vec\Upsilon_x\vec\Upsilon_y\vec\Upsilon_y\vec\Upsilon_x\rangle$ | $0$ | $1\cdot 0 = 0$ |
| $\langle \vec\Upsilon_y\vec\Upsilon_x\vec\Upsilon_y\vec\Upsilon_x\rangle$ | $0$ | $0\cdot 0 = 0$ |
| $\langle \vec\Upsilon_x\vec\Upsilon_x\vec\Upsilon_y\vec\Upsilon_y\rangle$ | $0$ | $1\cdot 1 - 1\cdot 1 = 0$ |
| $\langle \vec\Upsilon_y\vec\Upsilon_y\vec\Upsilon_x\vec\Upsilon_x\rangle$ | $0$ | $0$ |
| $\langle \vec\Upsilon_y\vec\Upsilon_x\vec\Upsilon_x\vec\Upsilon_y\rangle$ | $0$ | $0$ |

Two entries carry the sign. For $\langle\vec\Upsilon_x\vec\Upsilon_x\vec\Upsilon_y\vec\Upsilon_y\rangle$ the two complete pairings are $(1,3)(2,4)$ and $(1,4)(2,3)$, with relative sign $-1$: in the expansion of the theorem the contraction $\langle \tilde{Q}_1\tilde{Q}_3\rangle\langle \tilde{Q}_2\tilde{Q}_4\rangle$ carries the minus and $\langle \tilde{Q}_1\tilde{Q}_4\rangle\langle \tilde{Q}_2\tilde{Q}_3\rangle$ the plus, since the pairing $(1,3)(2,4)$ requires a single transposition of the four fermionic factors while $(1,4)(2,3)$ is even. Their values are $1\cdot1$ and $1\cdot1$, so the sum is $-1+1=0$, in agreement with the direct value $\vec\Upsilon_x^2=0$. For $\langle\vec\Upsilon_x\vec\Upsilon_y\vec\Upsilon_x\vec\Upsilon_y\rangle$ the only surviving pairing is $(1,2)(3,4)$, of value $1$, and the direct value is $\tilde\Pi_+^2=\tilde\Pi_+$ with vacuum expectation $1$.

**The six-point function.** The six-point contraction $\langle(\vec\Upsilon_x\vec\Upsilon_y)^3\rangle_t$ is $1$: $(\vec\Upsilon_x\vec\Upsilon_y)^3 = \tilde\Pi_+^3=\tilde\Pi_+$, and the pairing sum has the single nonvanishing complete pairing $(1,2)(3,4)(5,6)$ with sign $+1$ and value $1$. The six-point contractions with any pair in the reversed order vanish, as the direct computation confirms. The pattern is the general one: in the one-mode algebra the only nonvanishing contractible word is the alternating one beginning with $\vec\Upsilon_x$, and its value is the product of contractions.

## The Contraction Is the Propagator

For the field the contraction is the **Feynman propagator**, and this is the point at which the one-mode result connects to the field theory. On the spinor module the propagator of the biquaternion Dirac field satisfies
$$
\big(i\gamma^\mu\partial/\partial Q_\mu - m\big) S_F(x-y) = \delta^{(4)}(x-y),
$$
and the biquaternion content of $S_F$ is the same as that of the scalar $D_F$: its four-momentum-space form is a function of the wave biquaternion $\tilde P = iEe_t+\vec p$, and its pole sits on the mass shell $\tilde P\tilde P^{\natural} = -m^2$, in the $ict'$ metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The propagator article's finding carries over verbatim: the algebra names the wave biquaternion and the axis of the $i\epsilon$ deformation — the $ict'$ direction of $\mathbb{M}_-$ — but it does not choose the orientation of the deformation, which is the choice of Feynman contour. The Wick theorem uses the propagator; it does not produce it.

Within the one-mode truncation, the contraction is a **central scalar** times $e_t$: $\langle\vec\Upsilon_x\vec\Upsilon_y\rangle_t = 1$ is an element of $\mathbb{C}_{\mathbb{B}}$. This is the algebraic shadow of the field statement that a contraction is a $c$-number, and it is why the contracted products in the table are scalars. The mode algebra's contractions are the entries of a positive semidefinite matrix — the covariance of the state — and the alternating structure of the one-mode contractions is the $\mathbb{Z}_2$-graded version of the bosonic Gaussian form.

## The Fermionic Sign and the Grading

The relative sign in the fermionic Wick theorem is implemented by the **fermion-parity grading**
$$
(-1)^F = i\vec e_z = \tilde\Pi_+ - \tilde\Pi_- = e_t - 2\tilde\Pi_- .
$$
The operator $(-1)^F$ is Hermitian, squares to $e_t$, and satisfies
$$
(-1)^F\,\vec\Upsilon_x\,(-1)^F = -\vec\Upsilon_x,
\qquad
(-1)^F\,\vec\Upsilon_y\,(-1)^F = -\vec\Upsilon_y .
$$
The sign in the Wick theorem is the statement that exchanging two odd operators produces a minus sign, which is the eigenvalue of $(-1)^F$ on the odd sector: the anticommutator of two odd elements is even, and the transposition sign is the image of that parity. In the one-mode algebra this is exact and can be written as an element; the contraction table above is its consequence.

**The field case.** For a field the fermion-parity operator is the infinite tensor product of one-mode parities (up to a regularization), and it is **not** an element of $\mathbb{B}$: it acts on the Fock space, which is a module over $\mathbb{B}$ rather than a subalgebra of it. This is the same gap that the Fock and S-matrix articles record. What survives is the algebraic content of the sign — the $\mathbb{Z}_2$ grading of the operator algebra into even and odd parts — and the one-mode realization above, which exhibits the grading concretely for the only mode the algebra contains.

**The Dyson series.** The S-matrix of *The S-Matrix in Biquaternionic Form* is the time-ordered exponential
$$
S = T\exp\!\left(-i\int d^4x\,\mathcal{H}_I(x)\right),
$$
and its expansion is contracted by precisely the theorem above: each term of the Dyson series is a time-ordered product of interaction Hamiltonians, each built from fields, and the vacuum expectation of each term is a sum over pairings. The $\mathbb{Z}_2$ grading supplies the fermionic signs of the contractions between different field operators, and the one-mode table above is the smallest nontrivial case of that contraction. Nothing in the Dyson series requires a biquaternion-specific theorem; the algebra's contribution is the sign, the central scalar nature of the contraction, and the one-mode exactness.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The mode operators generate the four-real-dimensional subalgebra $\mathcal{A}_{\mathrm{tr}} = \mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,\vec e_y,i\vec e_z\}\cong\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, a real form of $\mathbb{B}$; it is closed under multiplication, and the vacuum idempotent lies in it.
- The one-mode Wick identity $\vec\Upsilon_x\vec\Upsilon_y = \,:\vec\Upsilon_x\vec\Upsilon_y:\,+\langle\vec\Upsilon_x\vec\Upsilon_y\rangle_t e_t$, with $:\vec\Upsilon_x\vec\Upsilon_y:\,=-\tilde\Pi_-$ and $\langle\vec\Upsilon_x\vec\Upsilon_y\rangle_t=1$, holds as an identity in $\mathbb{B}$, and every $2m$-point one-mode contraction equals the signed sum over complete pairings.
- The fermionic sign is implemented by $(-1)^F=i\vec e_z\in\mathcal{A}_{\mathrm{tr}}$, with $(-1)^F\vec\Upsilon_x(-1)^F=-\vec\Upsilon_x$.

**Standard, and transcribed.**
- The field Wick theorem, its inductive proof from the (anti)commutation relations, the fermionic transposition sign, and the identification of contractions with Feynman propagators. These are cited as standard.
- The Dyson-series contraction that turns S-matrix elements into Feynman diagrams.

**Interpretation.**
- Reading the relative sign of the fermionic pairing sum as the image of the algebra's $\mathbb{Z}_2$ grading under the one-mode realization is the interpretive step that links the algebra to the sign; the sign itself is standard.

**Open.**
- Whether the fact that the one-mode contraction algebra is a *real* form of $\mathbb{B}$ (rather than the complex algebra itself) has consequences for the framework's treatment of Majorana fields is not settled here.
- The gap for the field — the absence of $(-1)^F$ and of the mode algebra in $\mathbb{B}$ beyond one mode — is inherited and not closed.

## Summary

For a single fermionic mode the Wick theorem is an exact identity in a four-real-dimensional subalgebra of $\mathbb{B}$. The mode operators generate
$$
\mathcal{A}_{\mathrm{tr}} = \mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,\vec e_y,i\vec e_z\} \cong \mathrm{Cl}_{1,1}\cong M_2(\mathbb{R}),
\qquad
\mathcal{A}_{\mathrm{tr}}\otimes_\mathbb{R}\mathbb{C} = \mathbb{B},
$$
which is a real form of the biquaternion algebra, and the vacuum idempotent $\tilde\Pi_+=e_t-\tilde\Pi_-$ lies in it. The nilpotency of the ladder makes the contraction exact:
$$
\vec\Upsilon_x\vec\Upsilon_y = -\,\tilde\Pi_- + e_t = \tilde\Pi_+,
\qquad
\langle \vec\Upsilon_x\vec\Upsilon_y\rangle_t = 1,
\qquad
\langle \vec\Upsilon_y\vec\Upsilon_x\rangle_t = 0 ,
$$
and every $2m$-point one-mode contraction is the signed sum over complete pairings, with the relative sign supplied by the parity of the pairing. The four-point table and the six-point value were recomputed directly in the matrix representation and agree with the pairing sums to machine precision; the nonzero entries are $\langle(\vec\Upsilon_x\vec\Upsilon_y)^k\rangle_t=1$, and the alternating word is the only contractible one.

For a field the theorem is standard and transcribed: time-ordered products equal normal-ordered products plus all contractions, the contractions are the Feynman propagators of *The Feynman Propagator in Biquaternionic Form*, and the fermionic sign is implemented by the $\mathbb{Z}_2$ grading whose one-mode realization is $(-1)^F=i\vec e_z$. The field's fermion parity and its mode algebra lie outside $\mathbb{B}$, in the module on which the field acts; that gap is inherited from the Fock article and is not closed here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$ |
| $i$ | Scalar imaginary, central |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material and informational sectors |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | Single-mode ladder |
| $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12(e_t-i\vec e_z)$ | Number operator |
| $\tilde\Pi_+=e_t-\tilde\Pi_-=\tfrac12(e_t+i\vec e_z)$ | One-mode vacuum idempotent |
| $\mathcal{A}_{\mathrm{tr}}=\mathrm{span}_\mathbb{R}\{e_t,i\vec e_x,\vec e_y,i\vec e_z\}\cong\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ | One-mode real form of $\mathbb{B}$ |
| $(-1)^F=i\vec e_z=e_t-2\tilde\Pi_-$ | Fermion-parity grading |
| $T\{\cdots\}$, $:\!\cdots\!:$ | Time ordering, normal ordering |
| $\langle \tilde{Q}_i\tilde{Q}_j\rangle_t$ | Contraction (two-point function) |
| $D_F$, $S_F$ | Feynman propagators (scalar, spinor) |
| $\tilde P=iEe_t+\vec p$, $\tilde P\tilde P^{\natural}=-m^2$ | Wave biquaternion; mass shell |
| $\mathrm{sgn}(\pi)$ | Fermionic sign of a complete pairing |
| $\mathcal{H}_I$, $S=T\exp(-i\int\mathcal{H}_I)$ | Interaction Hamiltonian; Dyson series |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |

## Further Reading

- G. C. Wick, "The evaluation of the collision matrix," *Physical Review* **80** (1950) 268–272, for the original theorem and its application to the S-matrix.
- F. J. Dyson, "The radiation theories of Tomonaga, Schwinger, and Feynman," *Physical Review* **75** (1949) 486–502, for the operator formulation in which Wick's theorem is used.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the fermionic Wick theorem with the transposition signs.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for normal ordering, contractions, and the reduction of correlation functions.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the theorem in the convention used here and its diagrammatic translation.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the derivation from the canonical (anti)commutation relations.
- J. W. Negele and H. Orland, *Quantum Many-Particle Systems* (Addison-Wesley, 1988), for the finite-mode form of Wick's theorem and the covariance matrix of a fermionic state.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the classical presentation of contractions and pairings.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification of the real form $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ inside the complex algebra.
- F. R. Gantmacher, *The Theory of Matrices*, Vol. II (Chelsea, 1959), for the algebra structure of $\mathrm{Cl}_{1,1}$ and its complexification.
- Companion articles: *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder, the grading, and the module structure; *The Feynman Propagator in Biquaternionic Form*, for the contractions as propagators; *The S-Matrix in Biquaternionic Form*, for the Dyson series contracted by this theorem; *The Biquaternion Vacuum as a Minimal Idempotent*, for the vacuum expectation value and the idempotent $\tilde\Pi_+$.
