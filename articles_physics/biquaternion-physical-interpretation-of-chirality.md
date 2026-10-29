# __Biquaternion Physical Interpretation of Chirality__

## Introduction

The mathematics article *Chirality: The Conjugate Pair* proves that chirality is the central sign of the conjugate pair, not the sign of the Peirce decomposition. This article gives the physical interpretation of that result. It states the result in brief, gives six labelled interpretations, and records the limits. It proves nothing: the proofs are in the mathematics article, one click away.

The distinction is not a matter of notation. The Standard Model is chiral: its left- and right-handed fermions carry inequivalent representations. A sign that grades two copies of one module cannot supply that distinction, however it is drawn. The Peirce sign grades $S_+\cong S_-\cong S$; the chiral sign grades $S$ against its conjugate $S^{\mathrm{c}}$. The first is a copy index, the second is the chirality. The whole physical content of the article is in that difference.

The biquaternion algebra supplies the second sign only after one step: the central idempotents live in $\mathbb{B}[j]=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$, not in $\mathbb{B}$. A biquaternion is therefore never chiral by itself; the Dirac field is a pair, and the chirality is the grading of the pair.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The Peirce sign, the Peirce table and $S_+\cong S_-\cong S$ | [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-in-the-biquaternion-algebra.html) |
| The nilpotents as matrix units and the column ideals | [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](../articles_maths/the-column-ideals-of-a-matrix-ring.html) |
| The simple module, $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$ and $\mathbb{B}\cong S\oplus S$ | [The Category of Modules](../articles_maths/modules-over-the-biquaternion-algebra.html) |
| The conjugate module, its real isomorphism and its complex inequivalence | [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html) |
| The central idempotents $e_\pm=\tfrac12(1\pm ij)$, the chirality $\chi=ij$ and its action on $\Delta$ | [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html) |
| The invariant pairing $\beta$ and the mass operator $D_m$ | [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html) |

## The Result in Brief

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has one simple complex module $S$, and $\mathbb{B}\cong S\oplus S$ as a left module. The Peirce idempotents $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ give the two minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$, both isomorphic to $S$. The Peirce sign is the right multiplication

$$
P=R_{i\vec e_z},
\qquad
P(s)=s\ \text{on }S_+,
\qquad
P(s)=-s\ \text{on }S_- .
$$

It is implemented by the element $i\vec e_z\in\mathbb{B}$, it is $\mathbb{B}$-linear, and it grades two copies of one module. The centre of $\mathbb{B}$ is $\mathbb{C}e_t$, with no nontrivial idempotent; no element of $\mathbb{B}$ implements a grading into two non-isomorphic summands.

The conjugate module $S^{\mathrm{c}}$ is $S$ with the conjugate scalar action. It is isomorphic to $S$ as a real $\mathbb{B}_{\mathbb{R}}$-module and not isomorphic to $S$ as a complex $\mathbb{B}_{\mathbb{R}}$-module. The complexification $\mathbb{B}[j]=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$, with $j$ a new central imaginary unit, has the central idempotents

$$
e_+=\tfrac12(1+ij),\qquad e_-=\tfrac12(1-ij),
$$

and the chirality is

$$
\chi=ij=e_+-e_- .
$$

On the Dirac module

$$
\Delta=S\oplus S^{\mathrm{c}},
$$

the chirality acts as

$$
\chi=\operatorname{diag}(-I_2,I_2),
\qquad
P_L=\tfrac12(1-\chi),
\qquad
P_R=\tfrac12(1+\chi).
$$

The mass is the unique $SL_2(\mathbb{C})$-invariant sesquilinear pairing

$$
\beta:S\times S^{\mathrm{c}}\to\mathbb{C},
\qquad
\beta(s,t)=s^{\dagger}t,
$$

up to a scalar. The scalar is the mass. The pairing is off-diagonal and chirality-odd; it is not a $\mathbb{B}_{\mathbb{R}}$-linear operator, and it is not the Peirce nilpotent.

## The Chiral Multiplet

**The interpretation.** A left-handed Weyl field is a section of $S$; a right-handed Weyl field is a section of $S^{\mathrm{c}}$. The chirality operator is $\chi$, and a field of definite chirality is a section of one summand. The projectors $P_L$ and $P_R$ are the two chiral projections. A Dirac field is a pair

$$
\Psi=\begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix},
\qquad
\psi_L\in S,\quad \psi_R\in S^{\mathrm{c}}.
$$

**The boundary.** The naming of $S$ as left and $S^{\mathrm{c}}$ as right is a convention; exchanging the two names leaves the physics unchanged. The algebra supplies the pair and the grading. It does not supply the identification with the weak interaction, which is a separate physical input.

## The Peirce Index Is a Copy Label

**The interpretation.** The Peirce plane $S_+$ is a copy of $S$. A field in $S_+$ is a copy of a left-handed field, not a second chirality. The two Peirce planes are two copies of one Lorentz module; the left action does not distinguish them. A gauge action by left multiplication acts identically on $S_+$ and $S_-$, so it is vector-like on the copies. The weak chirality is the Lorentz chirality, not the Peirce index.

**The boundary.** The Peirce index is a legitimate label: it names the two copies, and the nilpotent $R_{\vec\Upsilon_x}$, with $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, flips it. It is not the label the weak interaction uses. Calling this copy index a chirality is a misnomer.

## The Mass Is a Pairing

**The interpretation.** The mass couples $S$ and $S^{\mathrm{c}}$ through the unique invariant sesquilinear pairing $\beta$. The mass term is

$$
m\,\beta(\psi_L,\psi_R)+\overline{m\,\beta(\psi_L,\psi_R)}.
$$

The algebra fixes the shape $\beta$; the number $m$ is the mass. The associated operator $D_m$ is off-diagonal,

$$
D_m=\begin{pmatrix}0&m\\ \bar m&0\end{pmatrix},
\qquad
\chi D_m\chi=-D_m,
$$

and it is not $\mathbb{B}_{\mathbb{R}}$-linear. The mass exists as a pairing between two inequivalent halves, not as an equivariant map between them.

**The boundary.** No mass value, no mass spectrum and no dynamics are supplied. The Peirce nilpotent $R_{\vec\Upsilon_x}:S_+\to S_-$ is a $\mathbb{B}$-linear copy flip; it is a different coupling, and calling it a mass is a model choice, not the Standard Model mass.

## A Biquaternion Is Not Chiral

**The interpretation.** A single element $\tilde\Psi\in\mathbb{B}$ is a section of the regular module $\mathbb{B}\cong S\oplus S$. Both summands are copies of $S$. The element therefore carries no chirality. The Dirac field is a pair in $S\oplus S^{\mathrm{c}}$, and the operation that relates the two halves is the conjugation (the real structure), not a biquaternion multiplication. This is the precise content of the sentence "a biquaternion is never chiral by itself."

**The boundary.** A Weyl fermion is one summand; a Majorana fermion is a real structure on one summand or on the pair, and it is outside this article. The statement is about the module, not about the existence of chiral fermions in nature.

## The Central Phase: Vector-Like or Axial

**The interpretation.** A central phase $\lambda\in U(1)$ acts on the regular module $S\oplus S$ as $\lambda$ on both copies: it is vector-like. The same phase acts on the Dirac module $S\oplus S^{\mathrm{c}}$ as $\lambda$ on $S$ and $\bar\lambda$ on $S^{\mathrm{c}}$: it is axial, with opposite charges. The mass bilinear transforms by $\bar\lambda^2$ under the axial phase and is not invariant; it is invariant under the vector phase. The algebra alone does not choose the representation. The gauge principle must say whether the fermions sit in $S\oplus S$ or in $\Delta$.

**The boundary.** This is a statement about the module, not a derivation of the Standard Model gauge group. The centre of $\mathbb{B}$ supplies an abelian phase; it does not supply the non-abelian weak group, and it does not decide between the vector-like and axial interpretations.

## The Grading of the Spectral Triple

**The interpretation.** A spectral triple with algebra $\mathbb{B}$ and finite Hilbert space $S$ cannot carry a nontrivial chirality. On $S$, every $\mathbb{B}$-linear operator is scalar, so the only grading commuting with the left action is trivial; a grading $\operatorname{diag}(1,-1)$ on a two-dimensional $S$ does not commute with a general left multiplication. The finite Hilbert space that carries the chiral grading is the Dirac module $\Delta$, with $\chi=\operatorname{diag}(-I_2,I_2)$. This is the module-level condition the finite part of the triple must meet.

**The boundary.** This is a consistency condition on the finite part of the triple, not a construction of the triple. The candidate in *The Spectral Triple of the Biquaternion Algebra* takes the finite space to be $\Delta=S\oplus S^{\mathrm{c}}$, with the chirality $\chi=\operatorname{diag}(-I_2,I_2)$; the single module $S$ carries no nontrivial grading. The analytic axioms, the Dirac operator and the spectral action are outside the article.

## Limits

- **No derivation of the gauge group.** The algebra supplies the Lorentz pair and the chirality grading. It does not supply the Standard Model gauge group, its representations or its breaking pattern.
- **No matter content and no generations.** The number of copies of $S$ and $S^{\mathrm{c}}$ is an input; the algebra does not fix it.
- **No mass value and no spectrum.** The pairing is fixed up to a scalar; the scalar is dynamical.
- **No dynamics.** Nothing here says how a field moves between the halves in time.
- **The left/right naming is a convention.** The physics is the pair and the grading, not the names.
- **The central phase's representation is an input.** Vector-like on $S\oplus S$, axial on $\Delta$; the algebra alone does not choose.
- **The Peirce copy flip is not the chiral mass.** The two couplings act on different pairs of spaces and have different invariance.
- **No claim that every fermion is a Dirac pair.** Weyl and Majorana fermions are separate cases.
- **No claim that chirality is an element of $\mathbb{B}$.** It is an endomorphism of $\Delta$ outside the algebra, equivalently the central element $ij$ of the complexification.

## Summary

Chirality is the central sign of the conjugate pair. The Peirce sign $P=R_{i\vec e_z}$ is implemented by the element $i\vec e_z\in\mathbb{B}$ and grades $S_+\cong S_-\cong S$; it is a copy index. The chiral sign $\chi=ij$ is the nontrivial central involution of $\mathbb{B}[j]\cong\mathbb{B}\oplus\mathbb{B}$ as real algebras, and grades $S$ against $S^{\mathrm{c}}$. On the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ it is $\operatorname{diag}(-I,I)$. The mass is the unique invariant sesquilinear pairing between the two halves, off-diagonal and chirality-odd; it is not a $\mathbb{B}_{\mathbb{R}}$-linear operator. A biquaternion is a section of $S\oplus S$ and carries no chirality; the Dirac field is the pair. The central phase is vector-like on $S\oplus S$ and axial on $\Delta$, and the algebra alone does not choose between the two interpretations.

$$
\boxed{\;
\chi=ij,\quad \chi=\operatorname{diag}(-I_2,I_2),\quad
P_L=\tfrac12(1-\chi),\quad P_R=\tfrac12(1+\chi),\quad
\Delta=S\oplus S^{\mathrm{c}},\quad
P=R_{i\vec e_z}\in\mathbb{B}.
\;}
$$

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $S$ | the simple left $\mathbb{B}$-module, the left-handed Weyl module |
| $S^{\mathrm{c}}$ | the conjugate module, the right-handed Weyl module |
| $\Delta=S\oplus S^{\mathrm{c}}$ | the Dirac module |
| $P=R_{i\vec e_z}$ | the Peirce sign, a copy index |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$ | the off-diagonal nilpotent; $R_{\vec\Upsilon_x}$ is the copy flip |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two Peirce planes, both $\cong S$ |
| $j$ | a new central imaginary unit, $j^2=-1$ |
| $\chi=ij$ | the chirality |
| $P_L=\tfrac12(1-\chi)$, $P_R=\tfrac12(1+\chi)$ | the chiral projectors |
| $\beta(s,t)=s^{\dagger}t$ | the invariant pairing $S\times S^{\mathrm{c}}\to\mathbb{C}$ |
| $D_m$ | the mass operator, off-diagonal |
| $m$ | the mass scale |

## Further Reading

- [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html), for the definitions, the two no-go theorems, the central idempotents and the pairing.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the carrier count, the module structure and the distinction between the Peirce index and the Lorentz chirality.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html), for the chiral projectors, the mass selection rule and the gauge discussion, stated there in the $\gamma_5$ language.
- [The Spectral Triple of the Biquaternion Algebra](the-spectral-triple-of-the-biquaternion-algebra.html), for the candidate triple with the finite space $\Delta$ and the central chirality.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the adjoint-action reading of integer spin, which is a representation label and not a chirality.
- [The Two Chiralities of $M_4(\mathbb{C})$](../articles_maths/the-two-chiralities-of-m4c.html), for the comparison with the matrix case.
