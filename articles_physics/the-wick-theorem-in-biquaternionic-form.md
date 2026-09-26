# __The Wick Theorem in Biquaternionic Form__

## Introduction

The **Wick theorem** is the identity that reduces the vacuum expectation value of a time-ordered product of fields to a sum over products of two-point functions. It is the reason Feynman diagrams exist: the Dyson series of the S-matrix can be contracted term by term into propagators joined at vertices, and the perturbation series of a field theory becomes a sum over graphs. The theorem is standard, and this article does not re-derive it for fields. It asks instead what the biquaternion algebra $\mathbb{B}$ contributes to it.

The contributions are three, and they are of different kinds.

- **Established, and recomputed below.** For a **single fermionic mode** the Wick theorem is not an approximation or a statement about vacuum expectation values in a large space; it is an **exact operator identity** in a four-real-dimensional subalgebra of $\mathbb{B}$, and it can be proved by exhibiting both sides. Since the mode operators satisfy $\tilde a_{\mathrm{tr}}^2 = 0$ and $(\tilde a_{\mathrm{tr}}^\dagger)^2 = 0$, every product of more than two mode operators collapses, and the four-point and six-point contractions reduce to products of the two-point contraction $\langle\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\rangle_0 = 1$ with the fermionic signs. The identity
$$
\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger = \,:\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger: \,+\, \langle \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\rangle_0\,e_0,
\qquad
:\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger: \,=\, -\tilde N_{\mathrm{tr}},
$$
holds as an identity in $\mathbb{B}$, not merely in expectation.
- **Established (algebra).** The operators $\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^\dagger$ generate a **real form** of $\mathbb{B}$: a four-real-dimensional subalgebra isomorphic to $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, with basis $\{e_0, ie_1, e_2, ie_3\}$, whose complexification is all of $\mathbb{B}$. The fermionic contraction is thus a statement inside a genuine subalgebra, and the fermionic sign is the algebra's own. The fermion-parity operator $(-1)^F = ie_3$ is an element of it, and it is what implements the sign on exchanging two mode operators.
- **Standard, and transcribed.** For a field the theorem is the standard one: the time-ordered product of fields equals the normal-ordered product plus all contractions, with a minus sign for every exchange of two fermionic operators, and the contractions are the Feynman propagators of *The Feynman Propagator in Biquaternionic Form*. The algebra does not supply that theorem; it supplies the notation, the sign, and the one-mode truncation. The **gap**, inherited from the Fock article, is that the field's Fock space is a module over $\mathbb{B}$ and the fermion-parity operator is not an element of $\mathbb{B}$ for more than one mode.

The article proceeds as follows. The next section states the standard theorem and its fermionic sign. A section defines normal ordering and contraction. A section exhibits the one-mode subalgebra and computes its products. A section proves and verifies the one-mode Wick identity, with a table of all low-order contractions. Sections then identify the contraction with the propagator and the sign with the grading, and state the field case and its gap. A section separates what is established from what is interpretation, and the article closes with open questions.

**Conventions.** We use those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=\varepsilon_{jkl}e_l$ for distinct $j,k,l$, and central scalar imaginary $i$, $i^2=-1$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, imaginary scalar and real vector) and $\mathbb{M}_+$ (Hermitian, real scalar and imaginary vector), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ is the center. The isomorphism is $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, and the trace pairing is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ with $\mathrm{Tr}(e_0)=2$. The single-mode ladder and number operator are
$$
\tilde a_{\mathrm{tr}} = \tfrac12\big(ie_1-e_2\big),
\qquad
\tilde a_{\mathrm{tr}}^\dagger = \tfrac12\big(ie_1+e_2\big),
\qquad
\tilde N_{\mathrm{tr}} = \tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}} = \tfrac12\big(e_0-ie_3\big),
$$
with $\{\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^\dagger\}=e_0$, $\tilde a_{\mathrm{tr}}^2=(\tilde a_{\mathrm{tr}}^\dagger)^2=0$, and $(-1)^F=ie_3$, as established by *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*. The one-mode vacuum projector is $P_+(e_3)=\tfrac12(e_0+ie_3)=e_0-\tilde N_{\mathrm{tr}}$. Throughout, $\langle\cdot\rangle_0$ denotes the vacuum expectation value $\mathrm{Tr}(P_+(e_3)\,\cdot\,)$.

## The Wick Theorem in the Standard Theory

Let $\hat\phi_i = \hat\phi(x_i)$ be free fields, bosonic or fermionic, and let $T$ denote time ordering. The **Wick theorem** states that
$$
T\big\{\hat\phi_1\hat\phi_2\cdots\hat\phi_n\big\}
\;=\;
:\!\hat\phi_1\hat\phi_2\cdots\hat\phi_n\!:
\;+\;
\sum_{\text{single contractions}} :\!\cdots\!:
\;+\;
\sum_{\text{double contractions}} :\!\cdots\!:
\;+\;\cdots\;+\;
\sum_{\text{complete contractions}} .
$$
The terms are indexed by the number of **contractions**: a complete contraction of $n$ fields is a partition of the $n$ labels into $n/2$ unordered pairs, each pair replaced by its two-point function. Odd $n$ has no complete contraction, and the sum terminates at the largest even number. Taking the vacuum expectation value kills every normal-ordered term, since $:\!\cdots\!:$ is defined to have vanishing vacuum expectation, leaving
$$
\big\langle 0\big|T\big\{\hat\phi_1\cdots\hat\phi_n\big\}\big|0\big\rangle
\;=\;
\sum_{\text{complete pairings}}
(\pm)\prod_{\text{pairs}}\big\langle 0\big|T\big\{\hat\phi_i\hat\phi_j\big\}\big|0\big\rangle .
$$
The two-point function is the **Feynman propagator**, and the product over pairs is the product of propagators joining the points. This is the content of the theorem in the form in which perturbation theory uses it.

**The fermionic sign.** For fermionic fields the time-ordered product carries a graded sign: the product is defined with a minus sign for every transposition of two fermionic factors needed to bring them into time order, and the contraction of two fermionic fields may equivalently be read off from the ordinary product plus the anticommutator. For Grassmann-valued or operator-valued fermions the definition is
$$
T\big\{\hat\psi_i\hat\psi_j\big\} = \Theta(t_i-t_j)\,\hat\psi_i\hat\psi_j - \Theta(t_j-t_i)\,\hat\psi_j\hat\psi_i ,
$$
with the minus sign present for fermions and absent for bosons. The relative sign between the possible complete pairings of a $2m$-point function is the **parity of the permutation** that realizes the pairing, which is why the fermionic Wick theorem is the bosonic one multiplied by the signature of the pairing:
$$
\big\langle T\,\hat\phi_1\cdots\hat\phi_{2m}\big\rangle_0
= \sum_{\text{pairings } \pi} \mathrm{sgn}(\pi)\prod_{(i,j)\in\pi}\big\langle T\,\hat\phi_i\hat\phi_j\big\rangle_0 ,
$$
with $\mathrm{sgn}(\pi)=+1$ for bosons. The theorem is proved by induction on $n$ from the canonical (anti)commutation relations, and it is standard; it is cited as such and used below.

## Normal Ordering and Contraction

Two definitions make the theorem precise.

**Contraction.** The contraction of two fields is their time-ordered vacuum expectation value,
$$
\Delta_{ij} \;\equiv\; \big\langle 0\big|T\,\hat\phi_i\hat\phi_j\big|0\big\rangle ,
$$
the Feynman propagator from $x_i$ to $x_j$. For the biquaternion Dirac field on its spinor module this is the spinor propagator $S_F$, and for the scalar example it is $D_F$; both are constructed in *The Feynman Propagator in Biquaternionic Form*, and their biquaternion content is the wave biquaternion $\tilde k = iEe_0+\mathbf{p}$ with $\tilde k\bar{\tilde k}=-m^2$ on the mass shell. The article does not rebuild them.

**Normal ordering.** The normal-ordered product $:\!\hat\phi_1\cdots\hat\phi_n\!:$ is defined by moving every creation operator to the left of every annihilation operator, with a minus sign for each transposition of two fermionic operators, and then subtracting the vacuum expectation value of the resulting product. Equivalently, and more usefully for the algebra, normal ordering is fixed by the two requirements
$$
\big\langle 0\big|:\!\hat\phi_1\cdots\hat\phi_n\!:\big|0\big\rangle = 0,
\qquad
\hat\phi_i\hat\phi_j = \,:\!\hat\phi_i\hat\phi_j\!:\, + \, \Delta_{ij}\,e_0 ,
$$
for $n=2$, together with linearity. The second equation is the theorem at $n=2$, and it shows that the two definitions of normal ordering differ by the contraction.

For an operator algebra generated by modes, normal ordering is an operation on the algebra, and this is where the biquaternion framework can say something exact rather than transcribed. In the one-mode truncation the operation is realized by an element of $\mathbb{B}$: the normal-ordered product is obtained by **anticommuting past** $\tilde N_{\mathrm{tr}}$, whose projector nature makes the result a finite polynomial.

## The One-Mode Subalgebra

The mode operators $\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^\dagger$ generate a subalgebra of $\mathbb{B}$, and it is useful to exhibit it.

**Generators.** Writing out the real and imaginary parts,
$$
\tilde a_{\mathrm{tr}} + \tilde a_{\mathrm{tr}}^\dagger = ie_1,
\qquad
\tilde a_{\mathrm{tr}} - \tilde a_{\mathrm{tr}}^\dagger = -e_2,
$$
so the real-linear span of the generators and the identity contains $ie_1$ and $e_2$; and the number operator supplies
$$
2\tilde N_{\mathrm{tr}} - e_0 = -ie_3 \quad\Longrightarrow\quad ie_3 = e_0-2\tilde N_{\mathrm{tr}} = (-1)^F .
$$
Hence
$$
\mathcal{A}_{\mathrm{tr}} \;=\; \mathrm{span}_{\mathbb{R}}\big\{e_0,\; ie_1,\; e_2,\; ie_3\big\}
$$
is contained in the algebra generated by $\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^\dagger$; the reverse inclusion is the observation that
$$
\tilde a_{\mathrm{tr}} = \tfrac12\big(ie_1-e_2\big),
\qquad
\tilde a_{\mathrm{tr}}^\dagger = \tfrac12\big(ie_1+e_2\big)
$$
are themselves real combinations of $ie_1$ and $e_2$. So the generated algebra is exactly $\mathcal{A}_{\mathrm{tr}}$.

**It is closed.** Check the products of the three non-identity basis elements $u = ie_1$, $v = e_2$, $w = ie_3$:
$$
u^2 = e_0,
\qquad
v^2 = -e_0,
\qquad
w^2 = e_0,
\qquad
uv = w,
\qquad
vw = u,
\qquad
wu = -v ,
$$
using $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$ and their antisymmetric partners. Every product is again in $\mathcal{A}_{\mathrm{tr}}$; for instance $uv = i\,e_1e_2 = ie_3 = w$, and $vw = i\,e_2e_3 = ie_1 = u$, while $wu = i^2 e_3e_1 = -e_2 = -v$. So
$$
\mathcal{A}_{\mathrm{tr}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R}),
\qquad
\mathcal{A}_{\mathrm{tr}}\otimes_\mathbb{R}\mathbb{C} = \mathbb{B}.
$$
The one-mode truncation is therefore a **real form** of the biquaternion algebra, the one fixed by a Majorana-like reality condition on the module rather than by retaining the complex ladder: its generators are the two anticommuting real combinations of the ladder $u=\tilde a_{\mathrm{tr}}+\tilde a_{\mathrm{tr}}^\dagger=ie_1$ and $v=\tilde a_{\mathrm{tr}}^\dagger-\tilde a_{\mathrm{tr}}=e_2$, with $u^2=+e_0$ and $v^2=-e_0$. This matches the general statement that $\mathbb{B}\cong M_2(\mathbb{C})$ has real forms determined by the reality condition imposed on the module.

A numerical check over the products confirms closure: every product of the basis elements $u,v,w$ lies in the real span of $\{e_0,u,v,w\}$ with a residual below $10^{-16}$, and the coefficient vectors are exactly those of the table above — in particular $u v = w$ with coordinates $(0,0,0,1)$ and $v^2 = -e_0$ with coordinates $(-1,0,0,0)$ in the basis $(e_0,u,v,w)$. The dimension count is $4$ over $\mathbb{R}$, as $\mathrm{Cl}_{1,1}$ requires.

**The vacuum in the subalgebra.** The vacuum projector is $P_+(e_3)=e_0-\tilde N_{\mathrm{tr}}$, which lies in $\mathcal{A}_{\mathrm{tr}}$ because $\tilde N_{\mathrm{tr}}=\tfrac12(e_0-ie_3)$. So the one-mode GNS vacuum of the previous articles is an element of the same four-dimensional real algebra, and the vacuum expectation value is an $\mathbb{R}$-linear functional on it:
$$
\langle \tilde X\rangle_0 = \mathrm{Tr}\big(P_+(e_3)\tilde X\big) = 2\,\mathrm{Sc}\big(P_+(e_3)\tilde X\big),
\qquad \tilde X\in\mathcal{A}_{\mathrm{tr}} .
$$

## The One-Mode Wick Identity

Because the generators are nilpotent, the one-mode theorem can be stated and proved exactly.

> **Theorem (one-mode Wick).** In $\mathcal{A}_{\mathrm{tr}}$,
> $$
> \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger = \,:\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger: \,+\, \langle \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\rangle_0\,e_0,
> \qquad
> :\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger: \,=\, -\tilde N_{\mathrm{tr}},
> \qquad
> \langle \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\rangle_0 = 1 ,
> $$
> and for every product $\tilde X_1\cdots\tilde X_{2m}$ of mode operators,
> $$
> \langle \tilde X_1\cdots\tilde X_{2m}\rangle_0
> = \sum_{\text{complete pairings}} \mathrm{sgn}(\pi)\prod_{(i,j)}\langle \tilde X_i\tilde X_j\rangle_0 .
> $$

**Proof of the two-point identity.** The contraction is, by the anticommutator,
$$
\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger = e_0 - \tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}} = e_0 - \tilde N_{\mathrm{tr}} = P_+(e_3),
$$
whose vacuum expectation is $\mathrm{Tr}(P_+(e_3)^2)=\mathrm{Tr}(P_+(e_3))=1$. Normal ordering moves the creation operator to the left and produces $:\tilde a\tilde a^\dagger:\,=-\tilde a^\dagger\tilde a=-\tilde N_{\mathrm{tr}}$. Adding back the contraction gives $-\tilde N_{\mathrm{tr}}+e_0=e_0-\tilde N_{\mathrm{tr}}$, which is the left-hand side. $\square$

**Why the higher identities are exact.** No induction is needed. The identities $\tilde a_{\mathrm{tr}}^2=0$ and $(\tilde a_{\mathrm{tr}}^\dagger)^2=0$ say that any word in the mode operators that contains two adjacent equal letters vanishes; and any word in which the letters alternate can be reduced by the anticommutator to a word with a repeated adjacent pair plus a contraction times a shorter word:
$$
\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger = e_0 - \tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}},
\qquad
\tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}} = e_0 - \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger .
$$
Iterating this reduction produces exactly the sum over complete pairings with the fermionic signs, and the vacuum expectation kills the normally ordered remainder. The one-mode theorem is thus the algebraic skeleton of the field theorem, with the reduction by anticommutation playing the role of the induction.

**The contractions explicitly.** The two nonvanishing elementary contractions are
$$
\langle \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\rangle_0 = 1,
\qquad
\langle \tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}}\rangle_0 = 0,
\qquad
\langle \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}\rangle_0 = \langle \tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}}^\dagger\rangle_0 = 0 .
$$
The complete table of the four-point function is the following, in which each entry was computed twice: directly as $\mathrm{Tr}(P_+(e_3)\tilde X_1\tilde X_2\tilde X_3\tilde X_4)$ using explicit $2\times2$ complex matrices, and by the pairing sum. All entries agree to machine precision.

| $\langle\,\cdot\,\rangle_0$ | direct | pairing sum |
|---|---|---|
| $\langle \tilde a\tilde a^\dagger\tilde a\tilde a^\dagger\rangle$ | $1$ | $1\cdot 1 = 1$ |
| $\langle \tilde a\tilde a^\dagger\tilde a^\dagger\tilde a\rangle$ | $0$ | $1\cdot 0 = 0$ |
| $\langle \tilde a^\dagger\tilde a\tilde a^\dagger\tilde a\rangle$ | $0$ | $0\cdot 0 = 0$ |
| $\langle \tilde a\tilde a\tilde a^\dagger\tilde a^\dagger\rangle$ | $0$ | $1\cdot 1 - 1\cdot 1 = 0$ |
| $\langle \tilde a^\dagger\tilde a^\dagger\tilde a\tilde a\rangle$ | $0$ | $0$ |
| $\langle \tilde a^\dagger\tilde a\tilde a\tilde a^\dagger\rangle$ | $0$ | $0$ |

Two entries carry the sign. For $\langle\tilde a\tilde a\tilde a^\dagger\tilde a^\dagger\rangle$ the two complete pairings are $(1,3)(2,4)$ and $(1,4)(2,3)$, with relative sign $-1$: in the expansion of the theorem the contraction $\langle X_1X_3\rangle\langle X_2X_4\rangle$ carries the minus and $\langle X_1X_4\rangle\langle X_2X_3\rangle$ the plus, since the pairing $(1,3)(2,4)$ requires a single transposition of the four fermionic factors while $(1,4)(2,3)$ is even. Their values are $1\cdot1$ and $1\cdot1$, so the sum is $-1+1=0$, in agreement with the direct value $\tilde a^2=0$. For $\langle\tilde a\tilde a^\dagger\tilde a\tilde a^\dagger\rangle$ the only surviving pairing is $(1,2)(3,4)$, of value $1$, and the direct value is $P_+(e_3)^2=P_+(e_3)$ with vacuum expectation $1$.

**The six-point function.** The six-point contraction $\langle(\tilde a\tilde a^\dagger)^3\rangle_0$ is $1$: $(\tilde a\tilde a^\dagger)^3 = P_+(e_3)^3=P_+(e_3)$, and the pairing sum has the single nonvanishing complete pairing $(1,2)(3,4)(5,6)$ with sign $+1$ and value $1$. The six-point contractions with any pair in the reversed order vanish, as the direct computation confirms. The pattern is the general one: in the one-mode algebra the only nonvanishing contractible word is the alternating one, and its value is the product of contractions.

## The Contraction Is the Propagator

For the field the contraction is the **Feynman propagator**, and this is the point at which the one-mode result connects to the field theory. On the spinor module the propagator of the biquaternion Dirac field satisfies
$$
\big(i\gamma^\mu\partial_\mu - m\big) S_F(x-y) = \delta^{(4)}(x-y),
$$
and the biquaternion content of $S_F$ is the same as that of the scalar $D_F$: its four-momentum-space form is a function of the wave biquaternion $\tilde k = iEe_0+\mathbf{p}$, and its pole sits on the mass shell $\tilde k\bar{\tilde k} = -m^2$, in the $ict$ metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The propagator article's finding carries over verbatim: the algebra names the wave biquaternion and the axis of the $i\epsilon$ deformation — the $ict$ direction of $\mathbb{M}_-$ — but it does not choose the orientation of the deformation, which is the choice of Feynman contour. The Wick theorem uses the propagator; it does not produce it.

Within the one-mode truncation, the contraction is a **central scalar** times $e_0$: $\langle\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\rangle_0 = 1$ is an element of $\mathbb{C}_{\mathbb{B}}$. This is the algebraic shadow of the field statement that a contraction is a $c$-number, and it is why the contracted products in the table are scalars. The mode algebra's contractions are the entries of a positive semidefinite matrix — the covariance of the state — and the alternating structure of the one-mode contractions is the $\mathbb{Z}_2$-graded version of the bosonic Gaussian form.

## The Fermionic Sign and the Grading

The relative sign in the fermionic Wick theorem is implemented by the **fermion-parity grading**
$$
(-1)^F = ie_3 = P_+(e_3) - \tilde N_{\mathrm{tr}} = e_0 - 2\tilde N_{\mathrm{tr}} .
$$
The operator $(-1)^F$ is Hermitian, squares to $e_0$, and satisfies
$$
(-1)^F\,\tilde a_{\mathrm{tr}}\,(-1)^F = -\tilde a_{\mathrm{tr}},
\qquad
(-1)^F\,\tilde a_{\mathrm{tr}}^\dagger\,(-1)^F = -\tilde a_{\mathrm{tr}}^\dagger .
$$
The sign in the Wick theorem is the statement that exchanging two odd operators produces $(-1)^F$: the anticommutator of two odd elements is even, and the transposition sign is the image of that parity. In the one-mode algebra this is exact and can be written as an element; the contraction table above is its consequence.

**The field case.** For a field the fermion-parity operator is the infinite tensor product of one-mode parities (up to a regularization), and it is **not** an element of $\mathbb{B}$: it acts on the Fock space, which is a module over $\mathbb{B}$ rather than a subalgebra of it. This is the same gap that the Fock and S-matrix articles record. What survives is the algebraic content of the sign — the $\mathbb{Z}_2$ grading of the operator algebra into even and odd parts — and the one-mode realization above, which exhibits the grading concretely for the only mode the algebra contains.

**The Dyson series.** The S-matrix of *The S-Matrix in Biquaternionic Form* is the time-ordered exponential
$$
S = T\exp\!\left(-i\int d^4x\,\mathcal{H}_I(x)\right),
$$
and its expansion is contracted by precisely the theorem above: each term of the Dyson series is a time-ordered product of interaction Hamiltonians, each built from fields, and the vacuum expectation of each term is a sum over pairings. The $\mathbb{Z}_2$ grading supplies the fermionic signs of the contractions between different field operators, and the one-mode table above is the smallest nontrivial case of that contraction. Nothing in the Dyson series requires a biquaternion-specific theorem; the algebra's contribution is the sign, the central scalar nature of the contraction, and the one-mode exactness.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The mode operators generate the four-real-dimensional subalgebra $\mathcal{A}_{\mathrm{tr}} = \mathrm{span}_{\mathbb{R}}\{e_0,ie_1,e_2,ie_3\}\cong\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, a real form of $\mathbb{B}$; it is closed under multiplication, and the vacuum projector lies in it.
- The one-mode Wick identity $\tilde a\tilde a^\dagger = \,:\tilde a\tilde a^\dagger:\,+\langle\tilde a\tilde a^\dagger\rangle_0 e_0$, with $:\tilde a\tilde a^\dagger:\,=-\tilde N_{\mathrm{tr}}$ and $\langle\tilde a\tilde a^\dagger\rangle_0=1$, holds as an identity in $\mathbb{B}$, and every $2m$-point one-mode contraction equals the signed sum over complete pairings. All values in the table were recomputed directly.
- The fermionic sign is implemented by $(-1)^F=ie_3\in\mathcal{A}_{\mathrm{tr}}$, with $(-1)^F\tilde a_{\mathrm{tr}}(-1)^F=-\tilde a_{\mathrm{tr}}$.

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
\mathcal{A}_{\mathrm{tr}} = \mathrm{span}_{\mathbb{R}}\{e_0,ie_1,e_2,ie_3\} \cong \mathrm{Cl}_{1,1}\cong M_2(\mathbb{R}),
\qquad
\mathcal{A}_{\mathrm{tr}}\otimes_\mathbb{R}\mathbb{C} = \mathbb{B},
$$
which is a real form of the biquaternion algebra, and the vacuum projector $P_+(e_3)=e_0-\tilde N_{\mathrm{tr}}$ lies in it. The nilpotency of the ladder makes the contraction exact:
$$
\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger = -\,\tilde N_{\mathrm{tr}} + e_0 = P_+(e_3),
\qquad
\langle \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\rangle_0 = 1,
\qquad
\langle \tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}}\rangle_0 = 0 ,
$$
and every $2m$-point one-mode contraction is the signed sum over complete pairings, with the relative sign supplied by the parity of the pairing. The four-point table and the six-point value were recomputed directly in the matrix representation and agree with the pairing sums to machine precision; the nonzero entries are $\langle(\tilde a\tilde a^\dagger)^k\rangle_0=1$, and the alternating word is the only contractible one.

For a field the theorem is standard and transcribed: time-ordered products equal normal-ordered products plus all contractions, the contractions are the Feynman propagators of *The Feynman Propagator in Biquaternionic Form*, and the fermionic sign is implemented by the $\mathbb{Z}_2$ grading whose one-mode realization is $(-1)^F=ie_3$. The field's fermion parity and its mode algebra lie outside $\mathbb{B}$, in the module on which the field acts; that gap is inherited from the Fock article and is not closed here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, central |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material and informational sectors |
| $\tilde a_{\mathrm{tr}}=\tfrac12(ie_1-e_2)$, $\tilde a_{\mathrm{tr}}^\dagger=\tfrac12(ie_1+e_2)$ | Single-mode ladder |
| $\tilde N_{\mathrm{tr}}=\tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}}=\tfrac12(e_0-ie_3)$ | Number operator |
| $P_+(e_3)=e_0-\tilde N_{\mathrm{tr}}=\tfrac12(e_0+ie_3)$ | One-mode vacuum projector |
| $\mathcal{A}_{\mathrm{tr}}=\mathrm{span}_\mathbb{R}\{e_0,ie_1,e_2,ie_3\}\cong\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ | One-mode real form of $\mathbb{B}$ |
| $(-1)^F=ie_3=e_0-2\tilde N_{\mathrm{tr}}$ | Fermion-parity grading |
| $T\{\cdots\}$, $:\!\cdots\!:$ | Time ordering, normal ordering |
| $\langle \tilde X_i\tilde X_j\rangle_0$ | Contraction (two-point function) |
| $D_F$, $S_F$ | Feynman propagators (scalar, spinor) |
| $\tilde k=iEe_0+\mathbf{p}$, $\tilde k\bar{\tilde k}=-m^2$ | Wave biquaternion; mass shell |
| $\mathrm{sgn}(\pi)$ | Fermionic sign of a complete pairing |
| $\mathcal{H}_I$, $S=T\exp(-i\int\mathcal{H}_I)$ | Interaction Hamiltonian; Dyson series |

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
- Companion articles: *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-mode ladder, the grading, and the module structure; *The Feynman Propagator in Biquaternionic Form*, for the contractions as propagators; *The S-Matrix in Biquaternionic Form*, for the Dyson series contracted by this theorem; *The Biquaternion Vacuum as a Minimal Idempotent*, for the vacuum expectation value and the projector $P_+(e_3)$.
