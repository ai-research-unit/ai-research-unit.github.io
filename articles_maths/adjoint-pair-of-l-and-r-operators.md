# __Adjoint Pair of $L$ and $R$ Operators__

## Introduction

The biquaternion algebra carries four pairings, and every pairing carries its own adjoint of a linear map. Three of the pairings carry a named operator family of the corpus, and those families are named by their adjoints: *Association*, *Signed Inner Conjugation* and *Hermitian Adjoint*, the last with a signed version. The fourth pairing, the general quaternionic sesquilinear form, carries the indefinite Hermitian pair acting on two sides instead, named by its Krein adjoint; it is the form of the Krein articles, and its family is not one of the four names. The names look unrelated and the suffixes look arbitrary, so this article sets the four adjoints side by side and works them out on explicit maps and explicit matrices, in the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$.

The result is a one-line rule, and the examples below are the evidence for it: **each of the four operator names records an adjoint, and the adjective names the insertion of the sign.** *Association* is the transpose of the general plain bilinear form, the reversal of a product with no conjugation anywhere, and it is the name of that adjoint because the adjoint carries no conjugation to name. *Signed inner conjugation* is the name of the adjoint of the general quaternionic bilinear form: there the adjoint of $L_{\tilde Q_6}$ is the left multiplication by $\tilde Q_6^{\natural}$, the **signed left multiplication**, and the graded two-sided operator built from it is the inner conjugation up to the norm. *Hermitian adjoint* is the name of the adjoint of the general plain sesquilinear form, which is the conjugate linear $\ast$; and *signed Hermitian adjoint* is the **same** adjoint read on the operators that carry the sign, which is why the Hermitian layer carries two families where the plain layer carries one. The word **signed** always has the same meaning in the corpus: the grade involution $\natural$, the conjugation that negates the vector part and fixes the centre, has been inserted.

**The four pairs.** Read as an operator, each adjoint pairs the parameter with a second element: the plain form pairs $\tilde Q_6$ with $\tilde Q_6^{-1}$, the quaternionic form with $\tilde Q_6^{\natural}$, the plain sesquilinear form with $\tilde Q_6^{\ast}$, the quaternionic sesquilinear form with $\bar{\tilde Q_6}$. The article reads the four pairs twice. The first reading is the one above: the pair is the operator family that its form names, and the four names are the four adjoints. The second reading is at the end: the four pairs are compared by what each does to the two sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$, and only the Hermitian pair keeps both sectors in place for every parameter. That is the reason the Hermitian pair, and not another, is the pair the physical reading of the algebra uses.

The forms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the four conjugations are *The Group of Involutions*; the plain transpose is the general transpose of a bilinear form of *Bilinear Forms*, §*Isometries*, and its operator family is *Operators Acting 2 Side*; the family of the second form is *Two-Sided Operators on the General Quaternionic Algebra*. The table of §*Which Switch Does What* reads the two involutions on the four adjoints: the sign character $\alpha$ exchanges the side, and the coefficient involution $\sigma=\bar{\cdot}$ acts on the parameter. The switches themselves, with the twisted right factor and the four forms read at the unit, belong to the operator layer, in *Introduction to the Operators of the Biquaternion Algebra*, §*The Two Switches and the Twisted Right Factor*. The article is pure algebra; no argument uses a topology, a distance or a limit.

## Conventions and the Four Forms

**Theorem (the four forms and their Gram matrices).** The four pairings of the algebra are

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),
\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2),
$$
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\ast}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\ast}),
\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural\ast}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{\ast}),
$$

and in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ their Gram matrices are $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$. The first two are bilinear and the last two are sesquilinear, conjugate linear in the second argument. All four are non-degenerate and no two of them agree.

*Proof.* Each pairing is the scalar part of one of the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra*, and $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$; the natural and the Hermitian conjugations are diagonal in the basis, of diagonal entries $\varepsilon$ and $-\varepsilon$ respectively, which gives the four Gram matrices. The diagonal forms $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\sum_\mu Q_\mu^{2}$, $\sum_\mu|Q_\mu|^{2}$ and $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$ separate the four pairings on the units.

**Remark (the four forms are one family).** Any two of the four are recovered from the others by the two sign characters of the argument, $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1^{\natural},\tilde Q_2\rangle$, $\langle\tilde Q_1,\tilde Q_2\rangle_{\ast}=\langle\tilde Q_1,\bar{\tilde Q}_2\rangle_{\natural}$, so the four forms differ only in which of the identity, $\natural$, $\bar{\cdot}$ and $\ast$ is inserted into which slot. The four adjoints below differ in exactly the same way, and that is the whole point of the article.

## The Four Adjoints

**Definition.** For each of the four pairings $\phi=\langle\cdot,\cdot\rangle,\langle\cdot,\cdot\rangle_{\natural},\langle\cdot,\cdot\rangle_{\ast},\langle\cdot,\cdot\rangle_{\natural\ast}$ and each $\mathbb{C}$-linear map $F$ of $\mathbb{B}$, the **adjoint of $F$ for $\phi$** is the unique $\mathbb{C}$-linear map $F^{\phi}$ with

$$
\phi\bigl(F\tilde Q_1,\tilde Q_2\bigr)=\phi\bigl(\tilde Q_1,F^{\phi}\tilde Q_2\bigr)\qquad\text{for all }\tilde Q_1,\tilde Q_2\in\mathbb{B}.
$$

The form is non-degenerate, so the adjoint exists and is unique, and $F\mapsto F^{\phi}$ is conjugate linear in the sesquilinear cases and linear in the bilinear ones.

The corpus writes the first adjoint $F^{\approx}$ and calls it the **associate**; it writes the second $F^{\natural}$ and calls it the adjoint of the quaternionic form; the third is the **Hermitian adjoint** $F^{\ast}$. This article writes $F^{\phi}$ with the form for the subscript, and uses $\approx$ for the adjoint of the plain form and $\natural$ for the adjoint of the quaternionic form.

**Theorem (the adjoints of the one-sided and two-sided operators).** For the left multiplication $L_{\tilde Q_6}(\tilde Q)=\tilde Q_6\tilde Q$, the right multiplication $R_{\tilde Q_3}(\tilde Q)=\tilde Q\tilde Q_3$, and their product $L_{\tilde Q_6}R_{\tilde Q_3}$,

$$
(L_{\tilde Q_6})^{\approx}=R_{\tilde Q_6},\qquad (R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3},\qquad (L_{\tilde Q_6}R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}R_{\tilde Q_6};
$$
$$
(L_{\tilde Q_6})^{N}=L_{\tilde Q_6^{\natural}},\qquad (R_{\tilde Q_3})^{N}=R_{\tilde Q_3^{\natural}},\qquad (L_{\tilde Q_6}R_{\tilde Q_3})^{\natural}=L_{\tilde Q_6^{\natural}}R_{\tilde Q_3^{\natural}};
$$
$$
(L_{\tilde Q_6})^{\ast}=L_{\tilde Q_6^{\ast}},\qquad (R_{\tilde Q_3})^{\ast}=R_{\tilde Q_3^{\ast}},\qquad (L_{\tilde Q_6}R_{\tilde Q_3})^{\ast}=L_{\tilde Q_6^{\ast}}R_{\tilde Q_3^{\ast}};
$$
$$
(L_{\tilde Q_6})^{\natural\ast}=R_{\bar{\tilde Q_6}},\qquad (R_{\tilde Q_3})^{\natural\ast}=L_{\bar{\tilde Q_3}},\qquad (L_{\tilde Q_6}R_{\tilde Q_3})^{\natural\ast}=L_{\bar{\tilde Q_3}}R_{\bar{\tilde Q_6}}.
$$

*Proof.* For the first pair, $\mathrm{Sc}(\tilde Q_6\tilde Q_1\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2\tilde Q_6)$ by the cyclicity of $\mathrm{Sc}$, which is $\langle L_{\tilde Q_6}\tilde Q_1,\tilde Q_2\rangle=\langle\tilde Q_1,R_{\tilde Q_6}\tilde Q_2\rangle$, and the two-sided formula follows from the reversal of the adjoint of a composite, $(FG)^{\approx}=G^{\approx}F^{\approx}$. For the second, $\mathrm{Sc}((\tilde Q_6\tilde Q_1)^{\natural}\tilde Q_2)=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_6^{\natural}\tilde Q_2)=\langle\tilde Q_1,L_{\tilde Q_6^{\natural}}\tilde Q_2\rangle_{\natural}$, and the factors are **not** reversed because the adjoint of a left multiplication is again a left multiplication; the two-sided formula is $R_{\tilde Q_3^{\natural}}L_{\tilde Q_6^{\natural}}=L_{\tilde Q_6^{\natural}}R_{\tilde Q_3^{\natural}}$. The third is the same computation with the conjugate linear $\ast$ in place of $\natural$. For the fourth, $\mathrm{Sc}((\tilde Q_6\tilde Q_1)^{\natural}\tilde Q_2^{\ast})=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_6^{\natural}\tilde Q_2^{\ast})$ and $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_6^{\natural}\tilde Q_2^{\ast})=\mathrm{Sc}(\tilde Q_1^{\natural}(\tilde Q_2\bar{\tilde Q_6})^{\ast})$ by the cyclic property together with $(\tilde Q_2\bar{\tilde Q_6})^{\ast}=\tilde Q_6^{\natural}\tilde Q_2^{\ast}$, so the adjoint of $L_{\tilde Q_6}$ is $R_{\bar{\tilde Q_6}}$; the two-sided formula again reverses. Every identity was verified on the sixteen pairs of basis elements.

**Corollary (the plain adjoint swaps, the signed adjoint conjugates).** The first two lines above read

$$
\boxed{\; (L_{\tilde Q_6}R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}R_{\tilde Q_6},
\qquad
(L_{\tilde Q_6}R_{\tilde Q_3})^{\natural}=L_{\tilde Q_6^{\natural}}R_{\tilde Q_3^{\natural}} \;}.
$$

The associate **reverses the two parameters and leaves them alone**; the $\natural$-adjoint **keeps the parameters in place and replaces each by its image under the sign $\natural$**. So the word *association* names a transpose, and it is the suffix of a family exactly when the form of that family is the plain one; the word *signed inner conjugation* names the adjoint of the $\natural$-form, and no factor is reversed there. The third adjoint conjugates in place with the conjugate linear $\ast$, and the fourth swaps and conjugates.

**Remark (why this answers the naming question).** Each of the first three names is the name of an adjoint of one form: $\approx$ is printed as "Association", $\langle\cdot,\cdot\rangle_{\natural}$ as "Signed Inner Conjugation", $\ast$ as "Hermitian Adjoint". The form decides the adjoint, and the adjoint supplies the name. The last adjoint above, for the general quaternionic sesquilinear form, is the Krein adjoint of the indefinite theory; its family is the indefinite Hermitian pair acting on two sides, and it is named after the Krein structure rather than after one of the four operator names. The suffix "Signed Hermitian Adjoint" belongs to the Hermitian-algebra layer, where it names the operators with the sign inserted on the *same* form as the Hermitian family.

## Association as a Transpose

The first of the four adjoints is the one the corpus has named, and it carries a calculus of its own. Write it $\approx$ for a general $\mathbb{C}$-linear map $F$, not only for a one-sided or a two-sided operator.

**Proposition (the associate is an involution that reverses composition).** For $\mathbb{C}$-linear maps $F,G$ of $\mathbb{B}$,

$$
(F^{\approx})^{\approx}=F,\qquad (F\circ G)^{\approx}=G^{\approx}\circ F^{\approx},
$$

and on a pair of elements the defining property reads

$$
\mathrm{Sc}\bigl(F(\tilde Q_1)\,\tilde Q_2\bigr)=\mathrm{Sc}\bigl(\tilde Q_1\,F^{\approx}(\tilde Q_2)\bigr)\qquad\text{for all }\tilde Q_1,\tilde Q_2\in\mathbb{B}.
$$

*Proof.* The involution and the reversal are the uniqueness of the adjoint applied twice, as in the two-sided line of the theorem above; the second display is the definition with $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ substituted.

**Proposition (association reverses the factors of the Conway basis).** On the Conway operator basis $e_n[\,]e_m$, the elementary operator being $(e_n[\,]e_m)(\tilde Q)=e_n\tilde Q e_m$,

$$
\bigl(e_n[\,]e_m\bigr)^{\approx}=e_m[\,]e_n,
\qquad\text{so}\qquad
\Bigl(\sum_{n,m}A_{nm}\,e_n[\,]e_m\Bigr)^{\approx}=\sum_{n,m}A_{nm}\,e_m[\,]e_n .
$$

The edge rows $L_a=\sum_n a_n\,e_n[\,]e_t$ and $R_b=\sum_m b_m\,e_t[\,]e_m$ give back $L_a^{\approx}=R_a$ and $R_b^{\approx}=L_b$.

*Proof.* $\langle(a[\,]b)\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(a\tilde Q_1b\tilde Q_2)$ and the scalar part is invariant under the cyclic permutation of its three factors, $\mathrm{Sc}(a\tilde Q_1b\tilde Q_2)=\mathrm{Sc}(\tilde Q_1b\tilde Q_2a)=\langle\tilde Q_1,(b[\,]a)\tilde Q_2\rangle$; the identity is satisfied by $b[\,]a$ and it is unique by non-degeneracy. The edge rows are the special cases $b=e_t$ and $a=e_t$. The Conway basis is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Conway Operator Basis*.

**Proposition (the matrix of the associate).** Let $F$ have matrix $M$ in the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$. Then the matrix of the associate is

$$
\boxed{\; M^{\approx}=\mathrm{E}\,M^{\mathsf T}\mathrm{E} \;},
$$

the sign matrix $\mathrm{E}$ conjugating the plain transpose.

*Proof.* Write the form as $\langle\tilde Q_1,\tilde Q_2\rangle=Q_1^{\mathsf T}\mathrm{E}Q_2$ on the coordinate columns. Then $\langle F\tilde Q_1,\tilde Q_2\rangle=(MQ_1)^{\mathsf T}\mathrm{E}Q_2=Q_1^{\mathsf T}M^{\mathsf T}\mathrm{E}Q_2$ and $\langle\tilde Q_1,F^{\approx}\tilde Q_2\rangle=Q_1^{\mathsf T}\mathrm{E}M^{\approx}Q_2$ for all $Q_1,Q_2$, so $M^{\mathsf T}\mathrm{E}=\mathrm{E}M^{\approx}$, that is $M^{\approx}=\mathrm{E}M^{\mathsf T}\mathrm{E}$ because $\mathrm{E}^{-1}=\mathrm{E}$.

**Remark (when the associate is the plain transpose).** The two agree exactly when $M^{\mathsf T}$ commutes with $\mathrm{E}$. An operator that fixes the scalar unit $e_t$ and preserves the vector subspace has the block form $\operatorname{diag}(1,M)$ with $M$ a $3\times3$ matrix, and the conjugation by $\mathrm{E}$ acts as the sign $-1$ on the two off-diagonal blocks and as the identity on the two diagonal ones, so it is invisible there and $M^{\approx}=M^{\mathsf T}$. For a general map the two differ. The formula is the coordinate form of the general statement that the transpose of a bilinear form is taken with the Gram matrix conjugating both sides, $M\mapsto G^{-1}M^{\mathsf T}G$ (*Bilinear Forms*, §*Isometries*, and *Quadratic Forms and Polarisation*, §*Isometry of Forms*).

**Proposition (association against the Hermitian adjoint).** Let $\bar F$ be the map obtained from $F$ by conjugating every coefficient. Then

$$
\bar F^{\approx}=\mathrm{E}\,F^{\ast}\,\mathrm{E},
$$

$F^{\ast}$ being the adjoint for the positive definite Hermitian form $\langle\cdot,\cdot\rangle_{\ast}$ of the theorem above.

*Proof.* Conjugating the coefficients conjugates the entries of the matrix, taking $M$ to $\bar M$, so $\bar F^{\approx}$ has matrix $\mathrm{E}\bar M^{\mathsf T}\mathrm{E}$. The Hermitian adjoint has matrix $M^{\dagger}=\overline{M^{\mathsf T}}$, the conjugate transpose, so $\mathrm{E}F^{\ast}\mathrm{E}=\mathrm{E}\overline{M^{\mathsf T}}\mathrm{E}$, the same matrix.

**Corollary (the collapse on the vector-preserving unitaries).** On the operators of the block form $\operatorname{diag}(1,N)$ the conjugation by $\mathrm{E}$ is invisible, so the proposition reads $\bar F^{\approx}=F^{\ast}$, and for a $*$-unitary $F$ it reads $F^{\ast}=F^{-1}$. On those operators the plain transpose, the associate and the Hermitian adjoint are one involution, which is why the source literature writes the three interchangeably; for a general linear map they are three, and the corpus keeps the association, the transpose for the indefinite form of Gram matrix $\mathrm{E}$, apart from the dagger, the adjoint for the positive definite form of Gram matrix $\mathrm{I}_4$.

## One Operator, Four Adjoints

The example works one operator $F=L_{\tilde Q_6}R_{\tilde Q_3}$ with $\tilde Q_6=e_t+2\vec e_x$ and $\tilde Q_3=e_t+i\vec e_z$ through all four adjoints. The matrices are written in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the columns being the images of the four units.

$$
F=\mathsf{M}_{4L}(\tilde Q_6)\mathsf{M}_{4R}(\tilde Q_3)=
\begin{pmatrix}
1&-2&-2i&-i\\
2&1&i&-2i\\
-2i&-i&1&-2\\
i&-2i&2&1
\end{pmatrix},
\qquad
F^{\approx}=\mathsf{M}_{4L}(\tilde Q_3)\mathsf{M}_{4R}(\tilde Q_6)=
\begin{pmatrix}
1&-2&2i&-i\\
2&1&-i&-2i\\
2i&i&1&2\\
i&-2i&-2&1
\end{pmatrix},
$$
$$
F^{\natural}=\mathsf{M}_{4L}(\tilde Q_6^{\natural})\mathsf{M}_{4R}(\tilde Q_3^{\natural})=
\begin{pmatrix}
1&2&-2i&i\\
-2&1&-i&-2i\\
-2i&i&1&2\\
-i&-2i&-2&1
\end{pmatrix},
\qquad
F^{\ast}=\mathsf{M}_{4L}(\tilde Q_6^{\ast})\mathsf{M}_{4R}(\tilde Q_3^{\ast})=
\begin{pmatrix}
1&2&2i&-i\\
-2&1&i&2i\\
2i&-i&1&2\\
i&2i&-2&1
\end{pmatrix},
$$
$$
F^{\natural\ast}=\mathsf{M}_{4L}(\bar{\tilde Q_3})\mathsf{M}_{4R}(\bar{\tilde Q_6})=
\begin{pmatrix}
1&-2&-2i&i\\
2&1&i&2i\\
-2i&-i&1&2\\
-i&2i&-2&1
\end{pmatrix}.
$$

The five matrices are distinct. Reading the four adjoint matrices against $F$: the associate $F^{\approx}$ differs from $F$ by the reversal of the two factors, $2\vec e_x$ and $i\vec e_z$ changing places; the $\natural$-adjoint differs by the replacement $\tilde Q_6\mapsto\tilde Q_6^{\natural}=e_t-2\vec e_x$ and $\tilde Q_3\mapsto\tilde Q_3^{\natural}=e_t-i\vec e_z$; the Hermitian adjoint by $\tilde Q_6\mapsto\tilde Q_6^{\ast}=e_t-2\vec e_x$ and $\tilde Q_3\mapsto\tilde Q_3^{\ast}=e_t-i\vec e_z$ as well, the two differing only in the bar on the coefficients of $F$ itself; and the fourth adjoint by both operations, the swap of $L_{\bar{\tilde Q_3}}R_{\bar{\tilde Q_6}}$ and the two conjugations. None of the four adjoints equals $F$: the example is self-adjoint for no pairing, which is the generic case.

**Remark (the sign is a bar and a swap in the entries).** The four matrices above are the same matrix up to the conjugations and the transposition along the anti-diagonal of the parameter pair, which is what the corollary predicts; the reader who wants the transposition alone can compare $F$ with $F^{\approx}$, and the reader who wants the conjugation alone can compare $F$ with $F^{\natural}$.

## Signed, Unsigned and Associated

The second meaning of the word *signed* lives in the operators rather than in the adjoints. Two maps carry the same name in the corpus and differ by the sign $\natural$:

$$
\mathrm{Ad}_{\tilde Q_6}(\tilde Q)=\tilde Q_6\tilde Q\tilde Q_6^{-1},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q)=\tilde Q_6^{\natural}\tilde Q\tilde Q_6^{-1},
$$

the **unsigned inner conjugation** and the **signed inner conjugation**; the second is the first with the grade involution $\alpha=\natural$ inserted on the left factor, and it is the operator of the general theory of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, where $\mathrm{Ad}^{\alpha}_{U}(v)=\alpha(U)vU^{-1}$.

**Proposition (the difference is the vector part).** For an invertible $\tilde Q_6$ with scalar part $Q_{6t}$ and vector part $\vec Q_6$,

$$
\boxed{\; \mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q)-\mathrm{Ad}_{\tilde Q_6}(\tilde Q)=\bigl(\tilde Q_6^{\natural}-\tilde Q_6\bigr)\tilde Q\tilde Q_6^{-1}=-2\,\vec Q_6\,\tilde Q\tilde Q_6^{-1} \;},
$$

moreover $\mathrm{Ad}^{\alpha}_{\tilde Q_6}=\mathrm{Ad}_{\tilde Q_6}$ when $\tilde Q_6$ is central, and $\mathrm{Ad}^{\alpha}_{\tilde Q_6}=-\mathrm{Ad}_{\tilde Q_6}$ when $\tilde Q_6$ lies in the vector subspace $V$. The second case is the insertion of the sign at its sharpest: for $\tilde Q_6\in V$ the whole operator is negated.

*Proof.* The first two displays are the definition, and $\tilde Q_6^{\natural}-\tilde Q_6=-2\vec Q_6$ with $\vec Q_6=\tilde Q_6-Q_{6t}e_t$. If $\vec Q_6=0$ the difference vanishes; if $Q_{6t}=0$ then $\tilde Q_6^{\natural}=-\tilde Q_6$.

**Worked example ($\tilde Q_6=e_t+\vec e_x$, mixed, neither central nor in $V$).** The two operators and their difference are

$$
\mathrm{Ad}_{\tilde Q_6}=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde Q_6}=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
$$
$$
\mathrm{Ad}^{\alpha}_{\tilde Q_6}-\mathrm{Ad}_{\tilde Q_6}=
\begin{pmatrix}
-1&1&0&0\\
-1&-1&0&0\\
0&0&1&1\\
0&0&-1&1
\end{pmatrix}.
$$

The unsigned operator is the identity on the plane $\mathbb{C}\{e_t,\vec e_x\}$ and the quarter turn $\vec e_y\mapsto \vec e_z$, $\vec e_z\mapsto-\vec e_y$ on $\mathbb{C}\{\vec e_y,\vec e_z\}$; the signed operator interchanges the two roles, it is a quarter turn on $\mathbb{C}\{e_t,\vec e_x\}$ and the identity on $\mathbb{C}\{\vec e_y,\vec e_z\}$. The difference is twice the vector part, $2\vec Q_6=2\vec e_x$, and it reads as the matrix above.

**Worked example (the two extreme cases).** For $\tilde Q_6=ie_t$, central, both operators are the identity: $\mathrm{Ad}^{\alpha}_{ie_t}=\mathrm{Ad}_{ie_t}=\mathrm{id}$. For $\tilde Q_6=\vec e_x\in V$, of norm one, with $\vec e_x^{-1}=-\vec e_x$,

$$
\mathrm{Ad}_{\vec e_x}=\operatorname{diag}(1,1,-1,-1),
\qquad
\mathrm{Ad}^{\alpha}_{\vec e_x}=\operatorname{diag}(-1,-1,1,1)=-\mathrm{Ad}_{\vec e_x}.
$$

The unsigned operator fixes $e_t$ and $\vec e_x$ and negates the plane $\mathbb{C}\{\vec e_y,\vec e_z\}$; the signed operator does the opposite. Both are isometries of the plain form, both of determinant one on the complex four-dimensional space, because the space has even dimension.

**Corollary (the sign costs multiplicativity).** The unsigned inner conjugation is an algebra automorphism for every unit, $\mathrm{Ad}_{\tilde Q_6}(\tilde Q_1\tilde Q_2)=\mathrm{Ad}_{\tilde Q_6}(\tilde Q_1)\mathrm{Ad}_{\tilde Q_6}(\tilde Q_2)$. The signed inner conjugation with a parameter in $V$ is **anti**-multiplicative, $\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q_1\tilde Q_2)=-\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q_1)\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q_2)$; both statements were verified on one hundred pairs. This is the concrete cost of the insertion, and it is the reason the signed operators of the corpus are read for their own laws and not as automorphisms.

**Remark (two places for the sign, and the norm reads it).** The corpus inserts the sign on the left factor in $\mathrm{Ad}^{\alpha}$, and it writes the graded two-sided operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$, with the sign on the right factor. The two are exchanged by the inverse and by the norm:

$$
\boxed{\; L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}=\langle\tilde Q_6\rangle_{\natural}\,\mathrm{Ad}_{\tilde Q_6},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde Q_6}=\langle\tilde Q_6\rangle_{\natural}\,L_{\tilde Q_6^{-1}}R_{\tilde Q_6^{-1}},
\qquad
\langle\tilde Q_6\rangle_{\natural}=\tilde Q_6\tilde Q_6^{\natural} \;},
$$

verified on one hundred invertible elements. On the shell $\langle\tilde Q_6\rangle_{\natural}=\pm1$ the first line reads $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}=\pm\mathrm{Ad}_{\tilde Q_6}$: the same operator is the inner automorphism or its negative according to the sign of the norm, which is the second reading of the word *signed*: the operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ is the inner automorphism or its negative according to the sign of the norm, and it is the operator of the family of *Two-Sided Operators on the General Quaternionic Algebra*, whose old title carried that name before the title was changed to name the subcategory's algebra.



## Which Switch Does What

| form | adjoint of $L_{\tilde Q_6}$ | the switch in the parameter |
|---|---|---|
| plain bilinear | $R_{\tilde Q_6}$ | none, the side is swapped |
| quaternionic bilinear | $L_{\tilde Q_6^{\natural}}$ | $\alpha$, the side is kept |
| plain sesquilinear | $L_{\tilde Q_6^{\ast}}$ | $\alpha$ and $\sigma$, the side is kept |
| quaternionic sesquilinear | $R_{\bar{\tilde Q_6}}$ | $\sigma$, the side is swapped |

The sign character $\alpha$ is the switch of the side: the adjoint is a left multiplication exactly for the two forms whose parameter carries the sign, and a right multiplication for the two whose parameter does not. The coefficient involution $\sigma$ is the switch of the pair of forms: it is present exactly in the two rows of the two sesquilinear forms, and it is the bar on the parameter there. Both readings are the two switches of the table above, read on the one-sided operators instead of on the two-sided ones.

**The two isometries.** The inner automorphism $\mathrm{Ad}_{\tilde Q_6}=L_{\tilde Q_6}R_{\tilde Q_6^{-1}}$ is an isometry of the plain form for every unit $\tilde Q_6$, because

$$
\mathrm{Sc}\bigl(\tilde Q_6\tilde Q_1\tilde Q_6^{-1}\,\tilde Q_6\tilde Q_2\tilde Q_6^{-1}\bigr)=\mathrm{Sc}(\tilde Q_1\tilde Q_2).
$$

The signed inner conjugation $\mathrm{Ad}^{\alpha}_{\tilde Q_6}=L_{\tilde Q_6^{\natural}}R_{\tilde Q_6^{-1}}$ is an isometry on the two extreme parameters of §*Signed, Unsigned and Associated*, $\tilde Q_6=ie_t$ and $\tilde Q_6=\vec e_x$, where the sign is a reflection; the two operators of that example are isometries. The switch $\alpha$ keeps the side and changes the inner automorphism into the signed one; the switch $\sigma$ conjugates the parameter and is the bar of the sesquilinear forms.

## Self-Adjointness under the Four Adjoints

The four adjoints separate on the two families of §*Signed, Unsigned and Associated*. The table gives, for the graded two-sided operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ and for the inner automorphism $\mathrm{Ad}_{\tilde Q_6}=L_{\tilde Q_6}R_{\tilde Q_6^{-1}}$, whether the operator equals its own adjoint, for the four forms and four positions of the parameter.

| parameter | graded: plain | graded: $\natural$ | graded: $\ast$ | graded: $\natural\ast$ | $\mathrm{Ad}$: plain | $\mathrm{Ad}$: $\natural$ | $\mathrm{Ad}$: $\ast$ | $\mathrm{Ad}$: $\natural\ast$ |
|---|---|---|---|---|---|---|---|---|
| $\tilde Q_6=2+i$, central | yes | yes | no | no | yes | yes | yes | yes |
| $\tilde Q_6\in V$ | yes | yes | yes | yes | yes | yes | yes | yes |
| $\tilde Q_6$ mixed | no | no | no | no | no | no | no | no |
| $\tilde Q_6=\vec e_x$ | yes | yes | yes | yes | yes | yes | yes | yes |

**Corollary (the criteria).** The operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ is self-adjoint for the plain form and for the $\natural$-form exactly when $\tilde Q_6^{\natural}$ is a multiple of $\tilde Q_6$, that is exactly when $\tilde Q_6$ is central or lies in the vector subspace; this is the criterion the corpus states for the $\langle\cdot,\cdot\rangle_{\natural}$-adjoint. It is self-adjoint for the $\ast$-form exactly when $\tilde Q_6^{\ast}/\tilde Q_6=\tilde Q_6^{\natural}/(\tilde Q_6^{\natural})^{\ast}$, and for the $\natural\ast$-form exactly when $\tilde Q_6^{\ast}/\tilde Q_6=\tilde Q_6^{\natural}/\bar{\tilde Q_6}$. The inner automorphism $\mathrm{Ad}_{\tilde Q_6}$ is self-adjoint for the plain form exactly when $\tilde Q_6^{-1}$ is a multiple of $\tilde Q_6$, for the $\natural$-form when $\tilde Q_6^{\natural}$ is a multiple of $\tilde Q_6$, for the $\ast$-form when $\tilde Q_6^{\ast}$ is a multiple of $\tilde Q_6$, and for the $\natural\ast$-form when $\overline{\tilde Q_6^{-1}}$ is a multiple of $\tilde Q_6$.

*Proof.* Self-adjointness is the equality of two decomposable tensors, and $L_{\tilde Q_4}R_{\tilde Q_5}=L_{\tilde Q_4'}R_{\tilde Q_5'}$ if and only if $\tilde Q_4'=\lambda\tilde Q_4$ and $\tilde Q_5'=\lambda^{-1}\tilde Q_5$ for one scalar $\lambda\in\mathbb{C}^{\times}$, the map $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ being faithful because $\mathbb{B}$ is central simple. Substituting the four adjoints of the theorem gives two equations on $\lambda$ for each pair; the two are the same equation in the bilinear cases and in the three cases of the second family, which leaves a single parallelism, and they are the two ratio equations in the sesquilinear cases of $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$, where the two ratios must agree. The table above is the evaluation on the four parameters.

**The plain type.** The table is for the graded two-sided operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ and the inner automorphism $\mathrm{Ad}_{\tilde Q_6}$. The general two-sided operator $L_{\tilde Q_4}R_{\tilde Q_5}$ is the **plain type**. Its plain adjoint is $L_{\tilde Q_5}R_{\tilde Q_4}$. The skew part $L_{\tilde Q_4}R_{\tilde Q_5}-L_{\tilde Q_5}R_{\tilde Q_4}$ vanishes exactly when $L_{\tilde Q_4}R_{\tilde Q_5}=L_{\tilde Q_5}R_{\tilde Q_4}$, which by the fibre theorem means $\tilde Q_5=\lambda\tilde Q_4$ and $\tilde Q_4=\lambda^{-1}\tilde Q_5$, hence $\lambda^{2}=1$ and $\tilde Q_5=\pm\tilde Q_4$. In that case the operator is self-adjoint; the two signs are the two self-adjoint positions. For the Hermitian pair $\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$, the skew part is $L_{\tilde Q}R_{\tilde Q^{*}}-L_{\tilde Q^{*}}R_{\tilde Q}$, and it vanishes exactly when $\tilde Q^{*}=\pm\tilde Q$, that is, when $\tilde Q$ is Hermitian or anti-Hermitian. The plain type therefore has a vanishing skew sector exactly on the two real subspaces of the parameter, the Hermitian and the anti-Hermitian, not on a general mixed element.

**Remark (the table is the naming rule in action).** The table is also a second piece of evidence for the rule of the introduction. The plain pair of the second family and the signed pair of the first are the two bilinear forms, and their criteria are the two parallelisms with $\natural$; the two conjugate linear forms give the two ratio equations, which the centre fails on the left and passes on the right, and the mixed parameter, which carries both a scalar and a vector part, satisfies none of the four conditions for $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$. Nothing in the table uses a distance or a limit.

## Why the Families Are Named As They Are

Each row is one form, the adjoint of the left multiplication that the form produces, the operator family built on it, and the adjoint name the corpus gives to that family. The first two of those names were the titles of the two bilinear operator families until 2026-09-27, when the titles were changed to name the algebra of the subcategory.

| form | Gram | adjoint of $L_{\tilde Q_6}$ | the operator family | adjoint name of the family |
|---|---|---|---|---|
| plain bilinear $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | $\mathrm{E}$ | $R_{\tilde Q_6}$, a swap, no conjugation | $\{L_{\tilde Q_6}R_{\tilde Q_3}\}$, two independent parameters; the article *Operators Acting 2 Side* | **Association** |
| quaternionic bilinear $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ | $\mathrm{I}_4$ | $L_{\tilde Q_6^{\natural}}=\Lambda^{\alpha}_{\tilde Q_6}$, the signed left multiplication | $\{L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}=\tilde Q_6\,\tilde Q\,\tilde Q_6^{\natural}\}$; the article *Two-Sided Operators on the General Quaternionic Algebra* | **Signed Inner Conjugation** |
| plain sesquilinear $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\ast})$ | $\mathrm{I}_4$ | $L_{\tilde Q_6^{\ast}}$ | the Hermitian pair with the dagger, $\tilde Q\mapsto\tilde Q_6\tilde Q\tilde Q_6^{\ast}$, plain left factor | **with Hermitian Adjoint** |
| the same plain sesquilinear form | $\mathrm{I}_4$ | $L_{\tilde Q_6^{\ast}}$ | the same pair acting on two sides, with $\Lambda^{\alpha}_{\tilde Q_6}$ in place of $L_{\tilde Q_6}$ | **with Signed Hermitian Adjoint** |
| quaternionic sesquilinear $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{\ast})$ | $\mathrm{E}$ | $R_{\bar{\tilde Q_6}}$, a swap with a bar | $\{L_{\tilde Q_6}R_{\bar{\tilde Q_6}}\}=\{\tilde Q_6\,\tilde Q\,\bar{\tilde Q_6}\}$, the indefinite Hermitian pair acting on two sides, of *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra* | **the Krein adjoint** (the form of the Krein articles) |

**Remark (the two words, and what they select).** *Association* is the name of the transpose of the plain form: it reverses the factors and conjugates nothing, and it is the name of the adjoint whenever the form is the plain bilinear one, because there is no conjugation to put in the name. *Signed* is the name of the insertion of the grade involution $\natural$. For the general quaternionic bilinear form the adjoint **is** the signed left multiplication, $\Lambda^{\alpha}_{\tilde Q_6}(\tilde Q)=\tilde Q_6^{\natural}\tilde Q$, so the sign enters the name of the adjoint directly; the graded two-sided operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ is then the inner conjugation up to the norm, which is the "inner conjugation" half of the name. For the general plain sesquilinear form the adjoint is the dagger and the two-sided operator needs no sign; the corpus writes that family as **Hermitian Adjoint**, and it writes the family of the *same* form with the sign inserted into the operator as **Signed Hermitian Adjoint**, so the Hermitian layer carries two rows where the plain layer carries one. Read together, the three names of the biquaternion layer — Association, Signed Inner Conjugation, Hermitian Adjoint — are the three possible answers to "which conjugation does the adjoint of the form carry?": none, the sign $\natural$, or the conjugate linear $\ast$.

## The Hermitian Pair and the Two Sectors

The four pairs of the table of §*Why the Families Are Named As They Are* are four operators per parameter. Read on the two sectors of the algebra, they separate: one of the four keeps both sectors in place for every parameter, and the other three do not.

**The two sectors.** Put

$$
\mathbb{B}_{\Psi}=\{\tilde X:\tilde X^{\ast}=\tilde X\},\qquad
\mathbb{B}_{\Phi}=\{\tilde X:\tilde X^{\ast}=-\tilde X\}.
$$

Each is a real subspace of real dimension four, and they are the eigenspaces of the involution $\ast$ for the eigenvalues $+1$ and $-1$. The central $i$ exchanges them, $\mathbb{B}_{\Phi}=i\,\mathbb{B}_{\Psi}$, because $\ast$ is conjugate linear. Neither is a complex subspace: multiplication by $i$ moves one into the other. The four elements $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ are a complex basis of $\mathbb{B}$ contained in $\mathbb{B}_{\Psi}$, and $ie_t,\vec e_x,\vec e_y,\vec e_z$ are a complex basis contained in $\mathbb{B}_{\Phi}$.

**Theorem (the two-sided operators that preserve a sector).** Let $\tilde Q_6\ne0$. The operator $L_{\tilde Q_6}R_{\tilde Q_3}$ maps $\mathbb{B}_{\Psi}$ into itself if and only if $\tilde Q_3=\lambda\tilde Q_6^{\ast}$ with $\lambda$ real; and each such operator maps $\mathbb{B}_{\Phi}$ into itself as well.

*Proof.* Suppose $\tilde Q_3=\lambda\tilde Q_6^{\ast}$. By the antimultiplicativity of $\ast$,

$$
\bigl(\tilde Q_6\tilde X\lambda\tilde Q_6^{\ast}\bigr)^{\ast}
=(\lambda\tilde Q_6^{\ast})^{\ast}\,\tilde X^{\ast}\,\tilde Q_6^{\ast}
=\bar\lambda\,\tilde Q_6\tilde X^{\ast}\tilde Q_6^{\ast},
$$

so for $\tilde X^{\ast}=\pm\tilde X$ and $\lambda$ real the image satisfies the same equation with the same sign.

Conversely, suppose the operator maps $\mathbb{B}_{\Psi}$ into itself. For $\tilde X^{\ast}=\tilde X$ the antimultiplicativity gives $(\tilde Q_6\tilde X\tilde Q_3)^{\ast}=\tilde Q_3^{\ast}\tilde X\tilde Q_6^{\ast}$, so the preservation reads

$$
L_{\tilde Q_3^{\ast}}R_{\tilde Q_6^{\ast}}\tilde X=L_{\tilde Q_6}R_{\tilde Q_3}\tilde X
\qquad\text{for every }\tilde X\in\mathbb{B}_{\Psi}.
$$

The four elements $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ lie in $\mathbb{B}_{\Psi}$ and are a complex basis, and both operators are $\mathbb{C}$-linear, so the two are equal. The fibre theorem of §*Self-Adjointness under the Four Adjoints* then gives $\tilde Q_6=\mu\tilde Q_3^{\ast}$ and $\tilde Q_3=\mu^{-1}\tilde Q_6^{\ast}$ for one $\mu\in\mathbb{C}^{\times}$. Applying $\ast$ to the first gives $\tilde Q_6^{\ast}=\bar\mu\tilde Q_3$, and substituting into the second gives $\tilde Q_3=\mu^{-1}\bar\mu\tilde Q_3$, hence $\mu=\bar\mu$; so $\mu$ is real and so is $\lambda=\mu^{-1}$. The fact that $\mathbb{B}_{\Phi}$ is preserved with $\mathbb{B}_{\Psi}$ is the centrality of $i$: a $\mathbb{C}$-linear map sends $i\tilde X$ to $i$ times the image of $\tilde X$, so $i\,\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$ goes into itself.

**Corollary (only the Hermitian pair, among the four).** The second factors of the four pairs are $\tilde Q_6^{-1}$ for the plain form, $\tilde Q_6^{\natural}$ for the quaternionic bilinear form, $\tilde Q_6^{\ast}$ for the plain sesquilinear form and $\bar{\tilde Q_6}$ for the quaternionic sesquilinear form. The third is the star itself, so $\lambda=1$ and the Hermitian pair preserves both sectors for every parameter. The other three preserve them only on the parameters where the second factor happens to be parallel to the star: $\tilde Q_6^{-1}\parallel\tilde Q_6^{\ast}$, $\tilde Q_6^{\natural}\parallel\tilde Q_6^{\ast}$, $\bar{\tilde Q_6}\parallel\tilde Q_6^{\ast}$. Each of the three conditions is a proper subvariety of the parameter space.

**Example (one parameter, three failures, one success).** Take $\tilde Q_6=e_t+2i\vec e_x$, of norm $N=-3$, and $\tilde X=i\vec e_y\in\mathbb{B}_{\Psi}$. The plain pair sends $\tilde X$ to $-\tfrac13(5i\vec e_y-4\vec e_z)$, the quaternionic pair and the Krein pair both send it to $5i\vec e_y-4\vec e_z$, and the Hermitian pair sends it to $4e_t+5i\vec e_y$. The first three images carry a real coefficient on $\vec e_z$ and are therefore in neither sector, since $Y^{\ast}\ne\pm Y$ for them; the fourth is Hermitian, as the theorem says.

**Remark (a real parameter hides the difference).** For a real $\tilde Q_6$ the star and the inverse differ only by the norm. The star is then the natural conjugation, $\tilde Q_6^{\ast}=\tilde Q_6^{\natural}$, and the inverse is $\tilde Q_6^{\natural}/\langle\tilde Q_6\rangle_{\natural}$ with the norm $\langle\tilde Q_6\rangle_{\natural}=\tilde Q_6\tilde Q_6^{\natural}$ real and nonzero, so $\tilde Q_6^{-1}=\langle\tilde Q_6\rangle_{\natural}^{-1}\tilde Q_6^{\ast}$ and the plain pair preserves the sectors too. On the real quaternion subspace, therefore, the plain pair and the Hermitian pair behave alike on the sectors, and the two separate only for a complex parameter, where the inverse and the star are no longer parallel.

**Remark (one side is not enough).** A one-sided operator preserves a sector only trivially. If $L_{\tilde Q_6}$ maps $\mathbb{B}_{\Psi}$ into itself, then $\tilde Q_6^{\ast}=\tilde Q_6$ by the value at $e_t$, and $\tilde X\tilde Q_6^{\ast}=\tilde Q_6\tilde X$ for every $\tilde X$, so $\tilde Q_6$ is central; and a central $\lambda e_t$ preserves $\mathbb{B}_{\Psi}$ exactly when $\lambda$ is real. The same holds for $R_{\tilde Q_6}$. The sector is therefore a property of a two-sided action, and in that action the second factor is forced to be the star of the first.

## Summary

The biquaternion algebra has four pairings, and each pairing has its own adjoint of a linear map. For the general plain bilinear form the adjoint is the exchange of the two factors with no conjugation, $\approx$, which the corpus calls **association**, the name of the adjoint that the plain family carries. The associate has a calculus of its own: it is an involution, it reverses composition, $(FG)^{\approx}=G^{\approx}F^{\approx}$, it reverses the factors of the Conway basis, $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$, its matrix in the coefficient basis is $M^{\approx}=\mathrm{E}M^{\mathsf T}\mathrm{E}$, and combined with the coefficient conjugation it relates to the Hermitian adjoint by $\bar F^{\approx}=\mathrm{E}F^{\ast}\mathrm{E}$, which collapses to $F^{\ast}=F^{-1}$ on the vector-preserving unitaries. For the general quaternionic bilinear form the adjoint of the left multiplication is the left multiplication by $\tilde Q_6^{\natural}$, the **signed left multiplication**, and the graded two-sided operator built on it is the inner conjugation up to the norm, which the corpus calls the **signed inner conjugation**, the name of the adjoint that the quaternionic family carries. For the general plain sesquilinear form the adjoint is the **Hermitian adjoint** $\ast$; and *signed Hermitian adjoint* is the same form with the sign inserted into the operator. For the general quaternionic sesquilinear form the adjoint is the right multiplication by $\bar{\tilde Q_6}$, the Krein adjoint of the indefinite Hermitian pair acting on two sides. The word *signed* has one meaning throughout: the insertion of the grade involution $\natural$, which is the identity on the centre and minus the identity on the vector subspace. The examples give the four adjoint matrices of one two-sided operator, the two matrices of the signed and the unsigned inner conjugation of a mixed element and of the two extreme parameters, and the four self-adjointness criteria on the same parameters. No step of the article uses a topology, a distance or a limit.

The four pairs are then compared on the two sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ of the Hermitian conjugation. A two-sided operator $L_{	ilde Q_6}R_{	ilde Q_3}$ keeps a sector in place exactly when $	ilde Q_3$ is a real multiple of $	ilde Q_6^{st}$, and then it keeps both sectors in place, because the central $i$ exchanges them. Among the four pairs only the Hermitian pair has that second factor for every parameter, so only the Hermitian pair acts on the algebra while leaving its two sectors apart; the plain, the quaternionic and the Krein pairs each mix the sectors for a generic complex parameter, and the three of them coincide in this failure on the single parameter $e_t+2i\vec e_x$. A one-sided operator preserves a sector only when its parameter is a real scalar, which is the precise sense in which the sectors belong to the two-sided action.

The two switches of the twisted right factor, and the four forms that they return at the unit, are *Introduction to the Operators of the Biquaternion Algebra*, §*The Two Switches and the Twisted Right Factor*; the table of §*Which Switch Does What* gives the adjoint-side reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, Gram $\mathrm{E}$ | the general plain bilinear form, the form of **association** |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, Gram $\mathrm{I}_4$ | the general quaternionic bilinear form, the form of the **signed inner conjugation** |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\ast}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\ast})$, Gram $\mathrm{I}_4$ | the general plain sesquilinear form, the form of the **Hermitian adjoint** |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural\ast}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{\ast})$, Gram $\mathrm{E}$ | the general quaternionic sesquilinear form, the form of the **Krein adjoint** and of the indefinite Hermitian pair acting on two sides |
| $\natural$, $\bar{\cdot}$, $\ast=\natural\bar{\cdot}$ | the natural conjugation (the grade involution), the coefficient conjugation, the Hermitian conjugation |
| $(L_{\tilde Q_6}R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}R_{\tilde Q_6}$ | the associate, the adjoint for the general plain bilinear form: the swap, no conjugation |
| $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$ | association on the Conway operator basis; $(FG)^{\approx}=G^{\approx}F^{\approx}$, and $L_a^{\approx}=R_a$, $R_b^{\approx}=L_b$ |
| $M^{\approx}=\mathrm{E}M^{\mathsf T}\mathrm{E}$, $\bar F^{\approx}=\mathrm{E}F^{\ast}\mathrm{E}$ | the associate in the coefficient basis, and against the Hermitian adjoint; the collapse $\bar F^{\approx}=F^{\ast}=F^{-1}$ on the vector-preserving unitaries |
| $(L_{\tilde Q_6}R_{\tilde Q_3})^{\natural}=L_{\tilde Q_6^{\natural}}R_{\tilde Q_3^{\natural}}$ | the $\natural$-adjoint, the adjoint for the general quaternionic bilinear form: the sign in place |
| $(L_{\tilde Q_6}R_{\tilde Q_3})^{\ast}=L_{\tilde Q_6^{\ast}}R_{\tilde Q_3^{\ast}}$ | the Hermitian adjoint; $(L_{\tilde Q_6}R_{\tilde Q_3})^{\natural\ast}=L_{\bar{\tilde Q_3}}R_{\bar{\tilde Q_6}}$ the signed one |
| $\mathbb{B}_{\Psi}=\{\tilde X:\tilde X^{\ast}=\tilde X\}$, $\mathbb{B}_{\Phi}=\{\tilde X:\tilde X^{\ast}=-\tilde X\}$, $\mathbb{B}_{\Phi}=i\,\mathbb{B}_{\Psi}$ | the two sectors, the real eigenspaces of the Hermitian conjugation |
| $L_{\tilde Q_6}R_{\lambda\tilde Q_6^{\ast}}$ preserves both sectors exactly when $\lambda$ is real | the sector criterion; the Hermitian pair is the case $\lambda=1$, the other three pairs fail it for a generic parameter |
| $\mathrm{Ad}_{\tilde Q_6}=\tilde Q_6\,\tilde Q\,\tilde Q_6^{-1}$, $\mathrm{Ad}^{\alpha}_{\tilde Q_6}=\tilde Q_6^{\natural}\tilde Q\tilde Q_6^{-1}$ | the unsigned and the signed inner conjugation; $\mathrm{Ad}^{\alpha}=\mathrm{Ad}$ on the centre, $-\mathrm{Ad}$ on $V$ |
| $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}=\langle\tilde Q_6\rangle_{\natural}\mathrm{Ad}_{\tilde Q_6}$ | the graded two-sided operator; $\langle\tilde Q_6\rangle_{\natural}=\tilde Q_6\tilde Q_6^{\natural}$ the norm |

## Further Reading

- [Introduction to the Operators of the Biquaternion Algebra](introduction-to-the-operators-of-the-biquaternion-algebra.html), for the products-to-operators bridge that the adjoints above serve, for the theorem that the plain product gives minus the reflection and the sign gives the reflection, and for the two switches $\sigma$ and $\alpha$ that the last table of this article names
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms the four adjoints belong to, their Gram matrices, their signatures and their notation table of the four adjoints
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations, their group and their linearity
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the Conway operator basis on which the associate reverses the factors, and the regular representations $L_a$ and $R_b$ that transpose into one another
- [Bilinear Forms](bilinear-forms.html), §*Isometries*, and [Quadratic Forms and Polarisation](quadratic-forms-and-polarisation.html), §*Isometry of Forms*, for the general transpose $M\mapsto G^{-1}M^{\mathsf T}G$ of a bilinear form, of which the associate is the biquaternion instance
- [Operators Acting 2 Side](operators-acting-2-side.html), for the family of the first adjoint, its swap law and its criteria
- [Two-Sided Operators on the General Quaternionic Algebra of the Biquaternions](two-sided-operators-on-the-general-quaternionic-algebra-of-the-biquaternions.html), for the graded two-sided operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$, its $\natural$-adjoint and its self-adjointness criterion
- [The Clifford, Pin and Spin Groups with Signed Inner Conjugation](the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.html), for $\mathrm{Ad}^{\alpha}_{U}(v)=\alpha(U)vU^{-1}$ and the general meaning of the sign
- [Hermitian pair of operators acting as 2 side](hermitian-pair-of-operators-acting-as-2-side.html), for the preservation of the two sectors by the Hermitian pair, proved on the pair itself, and for the multiplicativity the pair does not have
- [Hermitian pair of operators acting as 1 side](hermitian-pair-of-operators-acting-as-1-side.html), for the same construction with both members on one side, where the adjoint of the quaternionic form keeps the side and the composite of the pair is a scalar
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for the adjoint of a linear map with respect to a bilinear or a sesquilinear form
