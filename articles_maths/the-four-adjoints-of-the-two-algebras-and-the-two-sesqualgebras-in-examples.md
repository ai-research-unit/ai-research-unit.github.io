
# __The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples__

## Introduction

The biquaternion algebra carries four pairings, and every pairing carries its own adjoint of a linear map. The corpus gives each of the four pairings an operator family, and it has named those families by their adjoints: *Association*, *Signed Inner Conjugation*, *Hermitian Adjoint* and *Signed Hermitian Adjoint*. Two of those names were also the titles of the operator articles until 2026-09-27; those two titles now name the algebra of their subcategory (*Two-Sided Operators on the General Plain Algebra of Biquaternions* and *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*), and the adjoint names are kept here for the adjoints themselves. The names look unrelated and the suffixes look arbitrary, so this article sets the four adjoints side by side and works them out on explicit maps and explicit matrices, in the coefficient basis $e_0,e_1,e_2,e_3$.

The result is a one-line rule, and the examples below are the evidence for it: **each of the four adjoint names is the adjoint of one of the four forms, and the adjective names the insertion of the sign.** *Association* is the transpose of the general plain bilinear form, the reversal of a product with no conjugation anywhere, and it is the name of that adjoint because the adjoint carries no conjugation to name. *Signed inner conjugation* is the name of the adjoint of the general quaternionic bilinear form: there the adjoint of $L_{\tilde A}$ is the left multiplication by $\tilde A^{\natural}$, the **signed left multiplication**, and the sandwich built from it is the inner conjugation up to the norm. *Hermitian adjoint* is the name of the adjoint of the general plain sesquilinear form, which is the conjugate linear $\ast$; and *signed Hermitian adjoint* is the **same** form with the sign inserted into the operator, which is why the Hermitian layer carries two families where the plain layer carries one. The word **signed** always has the same meaning in the corpus: the grade involution $\natural$, the conjugation that negates the vector part and fixes the centre, has been inserted.

The forms are *The Four Pairings of the Biquaternion Algebra*; the four conjugations are *The Group of Involutions*; the plain transpose is *Association and the Transpose on the Biquaternion Algebra*, and its operator family is *Two-Sided Operators on the General Plain Algebra of Biquaternions*; the two other families are *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* and *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*. The last section of examples turns the same two involutions on the *two-sided operators* themselves: the coefficient involution $\sigma$ and the sign character $\alpha$ are the two switches of the twisted right factor $c_{\sigma,\alpha}(\tilde A)=\sigma(\alpha(\tilde A))$, and the four settings of the two switches return the four forms read at the unit. The article is pure algebra; no argument uses a distance, a limit or a derivative.

## Conventions and the Four Forms

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$; the central scalar imaginary is $i$; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; $\mathrm{Sc}$ is the scalar part. The four conjugations on elements are the identity, the **natural conjugation** $\tilde Q^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$, the **coefficient conjugation** $\bar{\tilde Q}=\overline{Q_0}e_0+\overline{Q_1}e_1+\overline{Q_2}e_2+\overline{Q_3}e_3$, and the **Hermitian conjugation** ${}^{\ast}={}^{\natural}\bar{\cdot}=\bar{\cdot}\,{}^{\natural}$, so that $\tilde Q^{\ast}=\overline{Q_0}e_0-\overline{Q_1}e_1-\overline{Q_2}e_2-\overline{Q_3}e_3$. The natural conjugation is the sign of the algebra, equal to $+1$ on the centre and $-1$ on the vector subspace $V=\mathbb{C}\{e_1,e_2,e_3\}$; in the reading $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ it is the Clifford conjugation $\alpha(X^{r})$, the grade involution itself being the coefficient conjugation (*The Clifford Algebra Representation*). It is $\mathbb{C}$-linear and an anti-automorphism; the coefficient conjugation is conjugate linear and an automorphism; the Hermitian conjugation is conjugate linear and an anti-automorphism.

**Theorem (the four forms and their Gram matrices).** The four pairings of the algebra are

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q),
$$
$$
\langle\tilde P,\tilde Q\rangle_{\ast}=\mathrm{Sc}(\tilde P\tilde Q^{\ast}),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural\ast}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{\ast}),
$$

and in the basis $e_0,e_1,e_2,e_3$ their Gram matrices are $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$. The first two are bilinear and the last two are sesquilinear, conjugate linear in the second argument. All four are non-degenerate and no two of them agree.

*Proof.* Each pairing is the scalar part of one of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$; the natural and the Hermitian conjugations are diagonal in the basis, of diagonal entries $\varepsilon$ and $-\varepsilon$ respectively, which gives the four Gram matrices. The diagonal forms $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\sum_\mu Q_\mu^{2}$, $\sum_\mu|Q_\mu|^{2}$ and $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$ separate the four pairings on the units. $\square$

**Remark (the four forms are one family).** Any two of the four are recovered from the others by the two sign characters of the argument, $\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P^{\natural},\tilde Q\rangle$, $\langle\tilde P,\tilde Q\rangle_{\ast}=\langle\tilde P,\bar{\tilde Q}\rangle_{\natural}$, so the four forms differ only in which of the identity, $\natural$, $\bar{\cdot}$ and $\ast$ is inserted into which slot. The four adjoints below differ in exactly the same way, and that is the whole point of the article.

## The Four Adjoints

**Definition.** For each of the four pairings $\phi=\langle\cdot,\cdot\rangle,\langle\cdot,\cdot\rangle_{\natural},\langle\cdot,\cdot\rangle_{\ast},\langle\cdot,\cdot\rangle_{\natural\ast}$ and each $\mathbb{C}$-linear map $F$ of $\mathbb{B}$, the **adjoint of $F$ for $\phi$** is the unique $\mathbb{C}$-linear map $F^{\phi}$ with

$$
\phi\bigl(F\tilde X,\tilde Y\bigr)=\phi\bigl(\tilde X,F^{\phi}\tilde Y\bigr)\qquad\text{for all }\tilde X,\tilde Y\in\mathbb{B}.
$$

The form is non-degenerate, so the adjoint exists and is unique, and $F\mapsto F^{\phi}$ is conjugate linear in the sesquilinear cases and linear in the bilinear ones.

The corpus writes the first adjoint $F^{\approx}$ and calls it the **associate**; it writes the second $F^{N}$ and calls it the $N$-adjoint, the adjoint for the norm form; the third is the **Hermitian adjoint** $F^{\ast}$. This article writes $F^{\phi}$ with the form for the subscript, which is the notation of the notation table of *The Four Pairings of the Biquaternion Algebra*, and uses $\approx$ and $N$ as the two names of the corpus.

**Theorem (the adjoints of the one-sided and two-sided operators).** For the left multiplication $L_{\tilde A}(\tilde X)=\tilde A\tilde X$, the right multiplication $R_{\tilde B}(\tilde X)=\tilde X\tilde B$, and their product $L_{\tilde A}R_{\tilde B}$,

$$
(L_{\tilde A})^{\approx}=R_{\tilde A},\qquad (R_{\tilde B})^{\approx}=L_{\tilde B},\qquad (L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A};
$$
$$
(L_{\tilde A})^{N}=L_{\tilde A^{\natural}},\qquad (R_{\tilde B})^{N}=R_{\tilde B^{\natural}},\qquad (L_{\tilde A}R_{\tilde B})^{N}=L_{\tilde A^{\natural}}R_{\tilde B^{\natural}};
$$
$$
(L_{\tilde A})^{\ast}=L_{\tilde A^{\ast}},\qquad (R_{\tilde B})^{\ast}=R_{\tilde B^{\ast}},\qquad (L_{\tilde A}R_{\tilde B})^{\ast}=L_{\tilde A^{\ast}}R_{\tilde B^{\ast}};
$$
$$
(L_{\tilde A})^{\natural\ast}=R_{\bar{\tilde A}},\qquad (R_{\tilde B})^{\natural\ast}=L_{\bar{\tilde B}},\qquad (L_{\tilde A}R_{\tilde B})^{\natural\ast}=L_{\bar{\tilde B}}R_{\bar{\tilde A}}.
$$

*Proof.* For the first pair, $\mathrm{Sc}(\tilde A\tilde X\tilde Y)=\mathrm{Sc}(\tilde X\tilde Y\tilde A)$ by the cyclicity of $\mathrm{Sc}$, which is $\langle L_{\tilde A}\tilde X,\tilde Y\rangle=\langle\tilde X,R_{\tilde A}\tilde Y\rangle$, and the two-sided formula follows from the reversal of the adjoint of a composite, $(FG)^{\approx}=G^{\approx}F^{\approx}$. For the second, $\mathrm{Sc}((\tilde A\tilde X)^{\natural}\tilde Y)=\mathrm{Sc}(\tilde X^{\natural}\tilde A^{\natural}\tilde Y)=\langle\tilde X,L_{\tilde A^{\natural}}\tilde Y\rangle_{\natural}$, and the factors are **not** reversed because the adjoint of a left multiplication is again a left multiplication; the two-sided formula is $R_{\tilde B^{\natural}}L_{\tilde A^{\natural}}=L_{\tilde A^{\natural}}R_{\tilde B^{\natural}}$. The third is the same computation with the conjugate linear $\ast$ in place of $\natural$. For the fourth, $\mathrm{Sc}((\tilde A\tilde X)^{\natural}\tilde Y^{\ast})=\mathrm{Sc}(\tilde X^{\natural}\tilde A^{\natural}\tilde Y^{\ast})$ and $\mathrm{Sc}(\tilde X^{\natural}\tilde A^{\natural}\tilde Y^{\ast})=\mathrm{Sc}(\tilde X^{\natural}(\tilde Y\bar{\tilde A})^{\ast})$ by the cyclic property together with $(\tilde Y\bar{\tilde A})^{\ast}=\tilde A^{\natural}\tilde Y^{\ast}$, so the adjoint of $L_{\tilde A}$ is $R_{\bar{\tilde A}}$; the two-sided formula again reverses. Every identity was verified on the sixteen pairs of basis elements. $\square$

**Corollary (the plain adjoint swaps, the signed adjoint conjugates).** The first two lines above read

$$
(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A},
\qquad
(L_{\tilde A}R_{\tilde B})^{N}=L_{\tilde A^{\natural}}R_{\tilde B^{\natural}}.
$$

The associate **reverses the two parameters and leaves them alone**; the $N$-adjoint **keeps the parameters in place and replaces each by its image under the sign $\natural$**. So the word *association* names a transpose, and it is the suffix of a family exactly when the form of that family is the plain one; the word *signed inner conjugation* names the adjoint of the $\natural$-form, and no factor is reversed there. The third adjoint conjugates in place with the conjugate linear $\ast$, and the fourth swaps and conjugates.

**Remark (why this answers the naming question).** Each of the four names is the name of an adjoint of one form: $\approx$ is printed as "Association", $N$ as "Signed Inner Conjugation", $\ast$ as "Hermitian Adjoint". The form decides the adjoint, and the adjoint supplies the name. The fourth adjoint above, for the general quaternionic sesquilinear form, is computed for completeness; the biquaternion corpus names that form in the Krein articles and has no separate operator family for it, and the suffix "Signed Hermitian Adjoint" belongs to the Hermitian-algebra layer, where it names the operators with the sign inserted on the *same* form as the Hermitian family.

## One Operator, Four Adjoints

The example works one operator $F=L_{\tilde A}R_{\tilde B}$ with $\tilde A=e_0+2e_1$ and $\tilde B=e_0+ie_3$ through all four adjoints. The matrices are written in the basis $e_0,e_1,e_2,e_3$, the columns being the images of the four units.

$$
F=L_{\tilde A}R_{\tilde B}=
\begin{pmatrix}
1&-2&-2i&-i\\
2&1&i&-2i\\
-2i&-i&1&-2\\
i&-2i&2&1
\end{pmatrix},
\qquad
F^{\approx}=L_{\tilde B}R_{\tilde A}=
\begin{pmatrix}
1&-2&2i&-i\\
2&1&-i&-2i\\
2i&i&1&2\\
i&-2i&-2&1
\end{pmatrix},
$$
$$
F^{N}=L_{\tilde A^{\natural}}R_{\tilde B^{\natural}}=
\begin{pmatrix}
1&2&-2i&i\\
-2&1&-i&-2i\\
-2i&i&1&2\\
-i&-2i&-2&1
\end{pmatrix},
\qquad
F^{\ast}=L_{\tilde A^{\ast}}R_{\tilde B^{\ast}}=
\begin{pmatrix}
1&2&2i&-i\\
-2&1&i&2i\\
2i&-i&1&2\\
i&2i&-2&1
\end{pmatrix},
$$
$$
F^{\natural\ast}=L_{\bar{\tilde B}}R_{\bar{\tilde A}}=
\begin{pmatrix}
1&-2&-2i&i\\
2&1&i&2i\\
-2i&-i&1&2\\
-i&2i&-2&1
\end{pmatrix}.
$$

The five matrices are distinct. Reading the four adjoint matrices against $F$: the associate $F^{\approx}$ differs from $F$ by the reversal of the two factors, $2e_1$ and $ie_3$ changing places; the $N$-adjoint differs by the replacement $\tilde A\mapsto\tilde A^{\natural}=e_0-2e_1$ and $\tilde B\mapsto\tilde B^{\natural}=e_0-ie_3$; the Hermitian adjoint by $\tilde A\mapsto\tilde A^{\ast}=e_0-2e_1$ and $\tilde B\mapsto\tilde B^{\ast}=e_0-ie_3$ as well, the two differing only in the bar on the coefficients of $F$ itself; and the fourth adjoint by both operations, the swap of $L_{\bar{\tilde B}}R_{\bar{\tilde A}}$ and the two conjugations. None of the four adjoints equals $F$: the example is self-adjoint for no pairing, which is the generic case.

**Remark (the sign is a bar and a swap in the entries).** The four matrices above are the same matrix up to the conjugations and the transposition along the anti-diagonal of the parameter pair, which is what the corollary predicts; the reader who wants the transposition alone can compare $F$ with $F^{\approx}$, and the reader who wants the conjugation alone can compare $F$ with $F^{N}$.

## Signed, Unsigned and Associated

The second meaning of the word *signed* lives in the operators rather than in the adjoints. Two maps carry the same name in the corpus and differ by the sign $\natural$:

$$
\mathrm{Ad}_{\tilde A}(\tilde X)=\tilde A\tilde X\tilde A^{-1},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde A}(\tilde X)=\tilde A^{\natural}\tilde X\tilde A^{-1},
$$

the **unsigned inner conjugation** and the **signed inner conjugation**; the second is the first with the grade involution $\alpha=\natural$ inserted on the left factor, and it is the operator of the general theory of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, where $\mathrm{Ad}^{\alpha}_{U}(v)=\alpha(U)vU^{-1}$.

**Proposition (the difference is the vector part).** For an invertible $\tilde A$ with scalar part $a_0$ and vector part $\mathbf A$,

$$
\mathrm{Ad}^{\alpha}_{\tilde A}(\tilde X)-\mathrm{Ad}_{\tilde A}(\tilde X)=\bigl(\tilde A^{\natural}-\tilde A\bigr)\tilde X\tilde A^{-1}=-2\,\mathbf A\,\tilde X\tilde A^{-1},
$$

moreover $\mathrm{Ad}^{\alpha}_{\tilde A}=\mathrm{Ad}_{\tilde A}$ when $\tilde A$ is central, and $\mathrm{Ad}^{\alpha}_{\tilde A}=-\mathrm{Ad}_{\tilde A}$ when $\tilde A$ lies in the vector subspace $V$. The second case is the insertion of the sign at its sharpest: for $\tilde A\in V$ the whole operator is negated.

*Proof.* The first two displays are the definition, and $\tilde A^{\natural}-\tilde A=-2\mathbf A$ with $\mathbf A=\tilde A-a_0e_0$. If $\mathbf A=0$ the difference vanishes; if $a_0=0$ then $\tilde A^{\natural}=-\tilde A$. Verified on one hundred pairs. $\square$

**Worked example ($\tilde A=e_0+e_1$, mixed, neither central nor in $V$).** The two operators and their difference are

$$
\mathrm{Ad}_{\tilde A}=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde A}=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
$$
$$
\mathrm{Ad}^{\alpha}_{\tilde A}-\mathrm{Ad}_{\tilde A}=
\begin{pmatrix}
-1&1&0&0\\
-1&-1&0&0\\
0&0&1&1\\
0&0&-1&1
\end{pmatrix}.
$$

The unsigned operator is the identity on the plane $\mathbb{C}\{e_0,e_1\}$ and the quarter turn $e_2\mapsto e_3$, $e_3\mapsto-e_2$ on $\mathbb{C}\{e_2,e_3\}$; the signed operator interchanges the two roles, it is a quarter turn on $\mathbb{C}\{e_0,e_1\}$ and the identity on $\mathbb{C}\{e_2,e_3\}$. The difference is twice the vector part, $2\mathbf A=2e_1$, and it reads as the matrix above.

**Worked example (the two extreme cases).** For $\tilde A=ie_0$, central, both operators are the identity: $\mathrm{Ad}^{\alpha}_{ie_0}=\mathrm{Ad}_{ie_0}=\mathrm{id}$. For $\tilde A=e_1\in V$, of norm one, with $e_1^{-1}=-e_1$,

$$
\mathrm{Ad}_{e_1}=\operatorname{diag}(1,1,-1,-1),
\qquad
\mathrm{Ad}^{\alpha}_{e_1}=\operatorname{diag}(-1,-1,1,1)=-\mathrm{Ad}_{e_1}.
$$

The unsigned operator fixes $e_0$ and $e_1$ and negates the plane $\mathbb{C}\{e_2,e_3\}$; the signed operator does the opposite. Both are isometries of the plain form, both of determinant one on the four-dimensional space, because the space has even dimension.

**Corollary (the sign costs multiplicativity).** The unsigned inner conjugation is an algebra automorphism for every unit, $\mathrm{Ad}_{\tilde A}(\tilde X\tilde Y)=\mathrm{Ad}_{\tilde A}(\tilde X)\mathrm{Ad}_{\tilde A}(\tilde Y)$. The signed inner conjugation with a parameter in $V$ is **anti**-multiplicative, $\mathrm{Ad}^{\alpha}_{\tilde A}(\tilde X\tilde Y)=-\mathrm{Ad}^{\alpha}_{\tilde A}(\tilde X)\mathrm{Ad}^{\alpha}_{\tilde A}(\tilde Y)$; both statements were verified on one hundred pairs. This is the concrete cost of the insertion, and it is the reason the signed operators of the corpus are read for their own laws and not as automorphisms.

**Remark (two places for the sign, and the norm reads it).** The corpus inserts the sign on the left factor in $\mathrm{Ad}^{\alpha}$, and it writes the twisted two-sided operator $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$, with the sign on the right factor. The two are exchanged by the inverse and by the norm:

$$
\Theta_{\tilde A}=N(\tilde A)\,\mathrm{Ad}_{\tilde A},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde A}=N(\tilde A)\,L_{\tilde A^{-1}}R_{\tilde A^{-1}},
\qquad
N(\tilde A)=\tilde A\tilde A^{\natural},
$$

verified on one hundred invertible elements. On the shell $N(\tilde A)=\pm1$ the first line reads $\Theta_{\tilde A}=\pm\mathrm{Ad}_{\tilde A}$: the same operator is the inner automorphism or its negative according to the sign of the norm, which is the second reading of the word *signed*: the operator $\Theta_{\tilde A}$ is the inner automorphism or its negative according to the sign of the norm, and it is the operator of the family of *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*, whose old title carried that name before the title was changed to name the subcategory's algebra.

## The Two Switches $\sigma$ and $\alpha$

The four adjoints of the sections above are one reading of the two involutions that the general theory carries. The same two insert themselves into the two-sided operators as twists, and this section works them on one parameter. The first is the **coefficient involution** $\sigma$, the conjugation of the scalars of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, which on this algebra is the coefficient conjugation $\bar{\cdot}$ of *The Group of Involutions*; the second is the **sign character** $\alpha$, the identity on the centre $\mathbb{C}_{\mathbb{B}}$ and minus the identity on the vector subspace $V$, which on this algebra is the natural conjugation $\natural$ read as a twist, as in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, where the same operator carries $\alpha$ in place of $\natural$.

**Definition (the twisted right factor and its operator).** For a switch pair $(\sigma,\alpha)$ and a parameter $\tilde A$ put

$$
c_{\sigma,\alpha}(\tilde A)=\sigma\bigl(\alpha(\tilde A)\bigr),
\qquad
\Phi^{\sigma,\alpha}_{\tilde A}(\tilde Y)=\tilde A\,\tilde Y\,c_{\sigma,\alpha}(\tilde A).
$$

**The four settings.** Each switch is either the identity or its involution, so there are four right factors:

| $\sigma$ | $\alpha$ | $c_{\sigma,\alpha}(\tilde A)$ | the operator | value at $e_0$ |
|---|---|---|---|---|
| $\mathrm{id}$ | $\mathrm{id}$ | $\tilde A$ | $\tilde Y\mapsto\tilde A\tilde Y\tilde A$ | $\tilde A^{2}$ |
| $\mathrm{id}$ | $\alpha$ | $\tilde A^{\natural}$ | the conjugation sandwich, the operator of *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* | $N(\tilde A)=\tilde A\tilde A^{\natural}$, central |
| $\sigma$ | $\mathrm{id}$ | $\bar{\tilde A}$ | $\tilde Y\mapsto\tilde A\tilde Y\bar{\tilde A}$ | $\tilde A\bar{\tilde A}$, scalar part the split norm |
| $\sigma$ | $\alpha$ | $\tilde A^{\ast}$ | the Hermitian sandwich, the operator of *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* | $\tilde A\tilde A^{\ast}$, Hermitian |

The fifth conjugation of the algebra, the reversal $\flat=-\ast$ of *The Group of Involutions*, is the last row with the extra central sign: $\tilde A^{\flat}=-\tilde A^{\ast}$, so the reversal sandwich is minus the Hermitian sandwich.

**Proposition (which right factors close the family).** For a right factor $c$ one has $\Phi^{\sigma,\alpha}_{\tilde A}\circ\Phi^{\sigma,\alpha}_{\tilde B}=\Phi^{\sigma,\alpha}_{\tilde A\tilde B}$ for all $\tilde A,\tilde B$ exactly when $c(\tilde B)c(\tilde A)=c(\tilde A\tilde B)$, that is exactly when $c$ is an anti-automorphism. This holds for the two rows with $\alpha$, that is $c=\natural$ and $c=\ast$. For $c$ the identity or the coefficient conjugation the composite is $\tilde A\tilde B\,\tilde Y\,c(\tilde B\tilde A)$, the operator whose right factor is read on the product in the opposite order; the family is then closed only after replacing the parameter $\tilde A\tilde B$ by $\tilde B\tilde A$. The reversal satisfies $c(\tilde B)c(\tilde A)=-c(\tilde A\tilde B)$, so it closes the family up to the central sign $-1$.

*Proof.* Evaluating the composite on $\tilde Y$ and using that $\alpha$ is an automorphism and that $\sigma$ is multiplicative, $\Phi^{\sigma,\alpha}_{\tilde A}(\Phi^{\sigma,\alpha}_{\tilde B}(\tilde Y))=\tilde A\tilde B\,\tilde Y\,c(\tilde B)c(\tilde A)$, which is $\Phi^{\sigma,\alpha}_{\tilde A\tilde B}(\tilde Y)=\tilde A\tilde B\,\tilde Y\,c(\tilde A\tilde B)$ exactly when $c(\tilde B)c(\tilde A)=c(\tilde A\tilde B)$; a map with that property is an anti-automorphism, and $\natural$ and $\ast$ are anti-automorphisms while the identity and $\bar{\cdot}$ are automorphisms, giving $c(\tilde B)c(\tilde A)=c(\tilde B\tilde A)$ in those two cases. For the reversal $c(\tilde B)c(\tilde A)=(-\tilde B^{\ast})(-\tilde A^{\ast})=\tilde B^{\ast}\tilde A^{\ast}=(\tilde A\tilde B)^{\ast}=-c(\tilde A\tilde B)$. Verified on one hundred pairs. $\square$

**Worked example.** Take the unit $\tilde A=(1+i)e_0+e_1$, of norm $N(\tilde A)=(1+i)^{2}+1=1+2i$. The four right factors, the four values at $e_0$ and their scalar parts are

| $\sigma$ | $\alpha$ | $c_{\sigma,\alpha}(\tilde A)$ | $\tilde A\,c_{\sigma,\alpha}(\tilde A)$ | $\mathrm{Sc}$ |
|---|---|---|---|---|
| $\mathrm{id}$ | $\mathrm{id}$ | $(1+i)e_0+e_1$ | $(-1+2i)e_0+(2+2i)e_1$ | $-1+2i$ |
| $\mathrm{id}$ | $\alpha$ | $(1+i)e_0-e_1$ | $(1+2i)e_0$ | $1+2i$ |
| $\sigma$ | $\mathrm{id}$ | $(1-i)e_0+e_1$ | $e_0+2e_1$ | $1$ |
| $\sigma$ | $\alpha$ | $(1-i)e_0-e_1$ | $3e_0-2ie_1$ | $3$ |

Only the second value is central; the fourth is fixed by the dagger and is not central, $(3e_0-2ie_1)^{\ast}=3e_0-2ie_1$; the first and the third are fixed by neither map, and the reversal negates the fourth. The four values are pairwise distinct, and so are their scalar parts.

**Remark (the four scalar parts are the four forms).** On a general element $\tilde A=\sum_\mu\lambda_\mu e_\mu$ the scalar part of the value at $e_0$ is one of the four forms of the corpus read on that element:

| $\mathrm{Sc}\bigl(\tilde A\,c_{\sigma,\alpha}(\tilde A)\bigr)$ | $\alpha=\mathrm{id}$ | $\alpha=\natural$ |
|---|---|---|
| $\sigma=\mathrm{id}$ | $\sum_\mu\varepsilon_\mu\lambda_\mu^{2}=-1+2i$ | $\sum_\mu\lambda_\mu^{2}=1+2i$ |
| $\sigma=\bar{\cdot}$ | $\sum_\mu\varepsilon_\mu\lvert\lambda_\mu\rvert^{2}=1$ | $\sum_\mu\lvert\lambda_\mu\rvert^{2}=3$ |

so the coefficient involution $\sigma$ replaces the squares $\lambda_\mu^{2}$ by the moduli $\lvert\lambda_\mu\rvert^{2}$, while the sign character $\alpha$ replaces the signed sum $\sum\varepsilon_\mu\lambda_\mu^{2}$ by the unsigned one $\sum\lambda_\mu^{2}$. The two entries of the left column are complex bilinear sums and vanish on the norm cone and on the plain cone; the two of the right column are real sums of moduli and vanish only at the origin. The values $2i-1$ and $1+2i$ are the two bilinear readings of the example, and $1$ and $3$ the two sesquilinear ones.

**Remark (the same two switches on the left factor).** The left slot may also carry a twist, and there it must be an automorphism, so the two possibilities are the identity and $\sigma$. With the right factor $c$ the inverse, $\natural$ or $\ast$, and the left slot either the identity or $\sigma$, the six members are the ones the corpus uses: the inner conjugation $\mathrm{Ad}_{\tilde A}$, the conjugation sandwich $\tilde A\,\tilde Y\,\tilde A^{\natural}$ and the Hermitian sandwich $\tilde A\,\tilde Y\,\tilde A^{\ast}$ are the three with the identity on the left, while $\bar{\tilde A}\,\tilde Y\,\tilde A^{-1}$ is the $\sigma$-twisted one, the operator of the general theory of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, and $(\sigma,\natural)$, $(\sigma,\ast)$ are the two remaining. Every one of the six is multiplicative in the parameter, by the proposition above.

**Remark (which switch does what).** The four adjoints of the left multiplication separate by the switch that each one carries:

| form | adjoint of $L_{\tilde A}$ | the switch in the parameter |
|---|---|---|
| plain bilinear | $R_{\tilde A}$ | none, the side is swapped |
| quaternionic bilinear | $L_{\tilde A^{\natural}}$ | $\alpha$, the side is kept |
| plain sesquilinear | $L_{\tilde A^{\ast}}$ | $\alpha$ and $\sigma$, the side is kept |
| quaternionic sesquilinear | $R_{\bar{\tilde A}}$ | $\sigma$, the side is swapped |

The sign character $\alpha$ is the switch of the side: the adjoint is a left multiplication exactly for the two forms whose parameter carries the sign, and a right multiplication for the two whose parameter does not. The coefficient involution $\sigma$ is the switch of the pair of forms: it is present exactly in the two rows of the two sesquilinear forms, and it is the bar on the parameter there. Both readings are the two switches of the table above, read on the one-sided operators instead of on the sandwiches.

## Self-Adjointness under the Four Adjoints

The four adjoints separate on the two families of the previous section. The table gives, for the two-sided operator $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$ and for the inner automorphism $\mathrm{Ad}_{\tilde A}=L_{\tilde A}R_{\tilde A^{-1}}$, whether the operator equals its own adjoint, for the four forms and four positions of the parameter.

| parameter | $\Theta$: plain | $\Theta$: $\natural$ | $\Theta$: $\ast$ | $\Theta$: $\natural\ast$ | $\mathrm{Ad}$: plain | $\mathrm{Ad}$: $\natural$ | $\mathrm{Ad}$: $\ast$ | $\mathrm{Ad}$: $\natural\ast$ |
|---|---|---|---|---|---|---|---|---|
| $\tilde A=2+i$, central | yes | yes | no | no | yes | yes | yes | yes |
| $\tilde A\in V$ | yes | yes | yes | yes | yes | yes | yes | yes |
| $\tilde A$ mixed | no | no | no | no | no | no | no | no |
| $\tilde A=e_1$ | yes | yes | yes | yes | yes | yes | yes | yes |

**Corollary (the criteria).** The operator $\Theta_{\tilde A}$ is self-adjoint for the plain form and for the $\natural$-form exactly when $\tilde A^{\natural}$ is a multiple of $\tilde A$, that is exactly when $\tilde A$ is central or lies in the vector subspace; this is the criterion the corpus states for the $N$-adjoint. It is self-adjoint for the $\ast$-form exactly when $\tilde A^{\ast}/\tilde A=\tilde A^{\natural}/(\tilde A^{\natural})^{\ast}$, and for the $\natural\ast$-form exactly when $\tilde A^{\ast}/\tilde A=\tilde A^{\natural}/\bar{\tilde A}$. The inner automorphism $\mathrm{Ad}_{\tilde A}$ is self-adjoint for the plain form exactly when $\tilde A^{-1}$ is a multiple of $\tilde A$, for the $\natural$-form when $\tilde A^{\natural}$ is a multiple of $\tilde A$, for the $\ast$-form when $\tilde A^{\ast}$ is a multiple of $\tilde A$, and for the $\natural\ast$-form when $\overline{\tilde A^{-1}}$ is a multiple of $\tilde A$.

*Proof.* Self-adjointness is the equality of two decomposable tensors, and $L_{\tilde X}R_{\tilde Y}=L_{\tilde X'}R_{\tilde Y'}$ if and only if $\tilde X'=\lambda\tilde X$ and $\tilde Y'=\lambda^{-1}\tilde Y$ for one scalar $\lambda\in\mathbb{C}^{\times}$, the map $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ being faithful because $\mathbb{B}$ is central simple. Substituting the four adjoints of the theorem gives two equations on $\lambda$ for each pair; the two are the same equation in the bilinear cases and in the three cases of the second family, which leaves a single parallelism, and they are the two ratio equations in the sesquilinear cases of $\Theta_{\tilde A}$, where the two ratios must agree. The table above is the evaluation on the four parameters. $\square$

**Remark (the table is the naming rule in action).** The table is also a second piece of evidence for the rule of the introduction. The plain pair of the second family and the signed pair of the first are the two bilinear forms, and their criteria are the two parallelisms with $\natural$; the two conjugate linear forms give the two ratio equations, which the centre fails on the left and passes on the right, and the mixed parameter, which carries both a scalar and a vector part, satisfies none of the four conditions for $\Theta_{\tilde A}$. Nothing in the table uses a distance or a limit.

## Why the Families Are Named As They Are

The evidence is collected in one table, and it is a description of the corpus and not a new theorem. Each row is one form, the adjoint of the left multiplication that the form produces, the operator family built on it, and the adjoint name the corpus gives to that family. The first two of those names were the titles of the two bilinear operator families until 2026-09-27, when the titles were changed to name the algebra of the subcategory.

| form | Gram | adjoint of $L_{\tilde A}$ | the operator family | adjoint name of the family |
|---|---|---|---|---|
| plain bilinear $\mathrm{Sc}(\tilde P\tilde Q)$ | $\mathrm{E}$ | $R_{\tilde A}$, a swap, no conjugation | $\{L_{\tilde A}R_{\tilde B}\}$, two independent parameters; the article *Two-Sided Operators on the General Plain Algebra of Biquaternions* | **Association** |
| quaternionic bilinear $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | $\mathrm{I}_4$ | $L_{\tilde A^{\natural}}=\Lambda^{\alpha}_{\tilde A}$, the signed left multiplication | $\{\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}=\tilde A\,\tilde X\,\tilde A^{\natural}\}$; the article *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* | **Signed Inner Conjugation** |
| plain sesquilinear $\mathrm{Sc}(\tilde P\tilde Q^{\ast})$ | $\mathrm{I}_4$ | $L_{\tilde A^{\ast}}$ | the sandwich with the dagger, $\tilde X\mapsto\tilde A\tilde X\tilde A^{\ast}$, plain left factor; the article *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* | **with Hermitian Adjoint** |
| the same plain sesquilinear form | $\mathrm{I}_4$ | $L_{\tilde A^{\ast}}$ | the same sandwich with $\Lambda^{\alpha}_{\tilde A}$ in place of $L_{\tilde A}$ | **with Signed Hermitian Adjoint** |
| quaternionic sesquilinear $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{\ast})$ | $\mathrm{E}$ | $R_{\bar{\tilde A}}$, a swap with a bar | — the biquaternion corpus has no operator family for this form | — (the form of the Krein articles) |

**Remark (the two words, and what they select).** *Association* is the name of the transpose of the plain form: it reverses the factors and conjugates nothing, and it is the name of the adjoint whenever the form is the plain bilinear one, because there is no conjugation to put in the name. *Signed* is the name of the insertion of the grade involution $\natural$. For the general quaternionic bilinear form the adjoint **is** the signed left multiplication, $\Lambda^{\alpha}_{\tilde A}(\tilde X)=\tilde A^{\natural}\tilde X$, so the sign enters the name of the adjoint directly; the sandwich $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$ is then the inner conjugation up to the norm, which is the "inner conjugation" half of the name. For the general plain sesquilinear form the adjoint is the dagger and the sandwich needs no sign; the corpus writes that family as **Hermitian Adjoint**, and it writes the family of the *same* form with the sign inserted into the operator as **Signed Hermitian Adjoint**, so the Hermitian layer carries two rows where the plain layer carries one. Read together, the three names of the biquaternion layer — Association, Signed Inner Conjugation, Hermitian Adjoint — are the three possible answers to "which conjugation does the adjoint of the form carry?": none, the sign $\natural$, or the conjugate linear $\ast$.

**Remark (what the adjoint name does not say).** The name records the adjoint of the form; it does not assert that the operator of the family is an isometry, that it is self-adjoint, or that it is an automorphism, and the tables above show the three properties failing for the generic parameter. The name is a name for the adjoint, and the article of the family is to be read with the form in hand.

## Summary

The biquaternion algebra has four pairings, and each pairing has its own adjoint of a linear map. For the general plain bilinear form the adjoint is the exchange of the two factors with no conjugation, $\approx$, which the corpus calls **association**, the name of the adjoint that the plain family carries. For the general quaternionic bilinear form the adjoint of the left multiplication is the left multiplication by $\tilde A^{\natural}$, the **signed left multiplication**, and the sandwich built on it is the inner conjugation up to the norm, which the corpus calls the **signed inner conjugation**, the name of the adjoint that the quaternionic family carries. For the general plain sesquilinear form the adjoint is the **Hermitian adjoint** $\ast$; and *signed Hermitian adjoint* is the same form with the sign inserted into the operator. The word *signed* has one meaning throughout: the insertion of the grade involution $\natural$, which is the identity on the centre and minus the identity on the vector subspace. The examples give the four adjoint matrices of one two-sided operator, the two matrices of the signed and the unsigned inner conjugation of a mixed element and of the two extreme parameters, and the four self-adjointness criteria on the same parameters. No step of the article uses a topology, a distance or a limit.

The two switches of the last section are the same two involutions read on the operators: the coefficient involution $\sigma$ replaces the squares $\lambda_\mu^{2}$ by the moduli $|\lambda_\mu|^{2}$, and the sign character $\alpha$ turns the signed sum $\sum\varepsilon_\mu\lambda_\mu^{2}$ into the unsigned one $\sum\lambda_\mu^{2}$. The four scalar parts that the two switches produce on one element are the four forms of the article, and the same two switches separate the four adjoints of the left multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$, Gram $\mathrm{E}$ | the general plain bilinear form, the form of **association** |
| $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, Gram $\mathrm{I}_4$ | the general quaternionic bilinear form, the form of the **signed inner conjugation** |
| $\langle\tilde P,\tilde Q\rangle_{\ast}=\mathrm{Sc}(\tilde P\tilde Q^{\ast})$, Gram $\mathrm{I}_4$ | the general plain sesquilinear form, the form of the **Hermitian adjoint** |
| $\langle\tilde P,\tilde Q\rangle_{\natural\ast}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{\ast})$, Gram $\mathrm{E}$ | the general quaternionic sesquilinear form, the form of the **signed Hermitian adjoint** |
| $\natural$, $\bar{\cdot}$, $\ast=\natural\bar{\cdot}$ | the natural conjugation (the grade involution), the coefficient conjugation, the Hermitian conjugation |
| $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$ | the associate, the adjoint for the general plain bilinear form: the swap, no conjugation |
| $(L_{\tilde A}R_{\tilde B})^{N}=L_{\tilde A^{\natural}}R_{\tilde B^{\natural}}$ | the $N$-adjoint, the adjoint for the general quaternionic bilinear form: the sign in place |
| $(L_{\tilde A}R_{\tilde B})^{\ast}=L_{\tilde A^{\ast}}R_{\tilde B^{\ast}}$ | the Hermitian adjoint; $(L_{\tilde A}R_{\tilde B})^{\natural\ast}=L_{\bar{\tilde B}}R_{\bar{\tilde A}}$ the signed one |
| $\mathrm{Ad}_{\tilde A}=\tilde A\,\tilde X\,\tilde A^{-1}$, $\mathrm{Ad}^{\alpha}_{\tilde A}=\tilde A^{\natural}\tilde X\tilde A^{-1}$ | the unsigned and the signed inner conjugation; $\mathrm{Ad}^{\alpha}=\mathrm{Ad}$ on the centre, $-\mathrm{Ad}$ on $V$ |
| $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}=N(\tilde A)\mathrm{Ad}_{\tilde A}$ | the twisted two-sided operator; $N(\tilde A)=\tilde A\tilde A^{\natural}$ the norm |
| $c_{\sigma,\alpha}(\tilde A)=\sigma(\alpha(\tilde A))$ | the twisted right factor: $\tilde A$, $\tilde A^{\natural}$, $\bar{\tilde A}$ or $\tilde A^{\ast}$ according to the two switches |
| $\Phi^{\sigma,\alpha}_{\tilde A}=\tilde A\,\tilde Y\,c_{\sigma,\alpha}(\tilde A)$ | the two-sided operator of the switches; multiplicative in $\tilde A$ for $\alpha=\natural$ |

## Further Reading

- *The Four General Products and Operators* (`articles_maths/the-four-general-products-and-operators.md`), for the products-to-operators bridge that the adjoints above serve, and for the theorem that the plain product gives minus the reflection and the sign gives the reflection
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms the four adjoints belong to, their Gram matrices, their signatures and their notation table of the four adjoints
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations, their group and their linearity
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the associate $\approx$, the transposition rule and its Conway-basis form
- *Two-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), for the family of the first adjoint, its swap law and its criteria
- *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the twisted operator $\Theta_{\tilde A}$, its $N$-adjoint and its self-adjointness criterion
- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the same family read with the dagger
- *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* (`articles_maths/the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.md`), for $\mathrm{Ad}^{\alpha}_{U}(v)=\alpha(U)vU^{-1}$ and the general meaning of the sign
- *The General Plain Algebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-representation.md`), for the same operators read as matrices, where the swap and the sign become a transposition and a bar
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for the adjoint of a linear map with respect to a bilinear or a sesquilinear form
