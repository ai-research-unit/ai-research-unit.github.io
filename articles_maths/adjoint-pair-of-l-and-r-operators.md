# __Adjoint Pair of $L$ and $R$ Operators__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four forms, and each form carries an adjoint of every linear map. The four adjoints have four names, and the names are used throughout this article:

1. the **plain bilinear adjoint** $F^{\approx}$, the adjoint of the plain bilinear form;
2. the **quaternionic adjoint** $F^{\natural}$, the adjoint of the quaternionic bilinear form;
3. the **Hermitian adjoint** $F^{\ast}$, the adjoint of the plain sesquilinear form;
4. the **Krein adjoint** $F^{\natural\ast}$, the adjoint of the quaternionic sesquilinear form.

The four forms differ only in which sign is inserted into which slot, and the four adjoints differ in exactly the same way. That is the whole content of the article, and the tables below are the evidence.

**The four adjoints at a glance.** For a general $\mathbb{C}$-linear map $F$, the four adjoints are written with the four marks $\approx,\natural,\ast,\natural\ast$. On the two one-sided families they act as follows, and the first column is the name of the adjoint:

| name of the adjoint | mark | form | Gram matrix | adjoint of $L_{\tilde Q}$ | adjoint of $R_{\tilde Q}$ |
|---|---|---|---|---|---|
| the **plain bilinear adjoint** | $\approx$ | plain bilinear $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | $\mathrm{E}$ | $R_{\tilde Q}$ | $L_{\tilde Q}$ |
| the **quaternionic adjoint** | $\natural$ | quaternionic bilinear $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ | $\mathrm{I}_4$ | $L_{\tilde Q^{\natural}}$ | $R_{\tilde Q^{\natural}}$ |
| the **Hermitian adjoint** | $\ast$ | plain sesquilinear $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\ast})$ | $\mathrm{I}_4$ | $L_{\tilde Q^{\ast}}$ | $R_{\tilde Q^{\ast}}$ |
| the **Krein adjoint** | $\natural\ast$ | quaternionic sesquilinear $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{\ast})$ | $\mathrm{E}$ | $R_{\bar{\tilde Q}}$ | $L_{\bar{\tilde Q}}$ |

Two columns of that table decide the shape of the whole subject. The plain bilinear adjoint and the Krein adjoint **exchange the side**; the quaternionic adjoint and the Hermitian adjoint **keep it**. The plain bilinear adjoint and the quaternionic adjoint carry **no bar**; the Hermitian and the Krein adjoints carry one.

**The four families, and which adjoint each one records.** The operator families of the corpus are named after these adjoints, and the correspondence is one row per family:

| operator family | its operator | the adjoint it is named after |
|---|---|---|
| **Plain Bilinear Pair** | $L_{\tilde Q_1}R_{\tilde Q_2}$, two parameters free | the **plain bilinear adjoint** |
| **Quaternionic Pair** | $L_{\tilde Q}R_{\tilde Q^{\natural}}$ | the **quaternionic adjoint** |
| **Hermitian Pair** | $L_{\tilde Q}R_{\tilde Q^{\ast}}$ | the **Hermitian adjoint** |
| **Signed Hermitian Pair** | $L_{\tilde Q^{\natural}}R_{\tilde Q^{\ast}}$ | the **Hermitian adjoint**, with the sign put into the operator |
| **Krein Pair** | $L_{\tilde Q}R_{\bar{\tilde Q}}$ | the **Krein adjoint** |

Each family is named after the adjoint whose form it records, so a row here and a row of the table above carry the same word: plain bilinear, quaternionic, Hermitian, Krein. The fourth row is not a fifth adjoint, and the distinction matters. The form is the plain sesquilinear form, the same one as the row above it; only the operator carries the grade involution on its left factor. So there are **four adjoints and five families**, and the word *signed* names the same operation in every row where it appears: the insertion of $\natural$.

The article proves the theorem of §*The Four Adjoints*, works one operator through all four adjoints, gives the self-adjointness criteria of the four, and shows that only the Hermitian family preserves the two sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ of the algebra. The forms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the four involutions are *The Group of Involutions*; the general transpose of a bilinear form is *Bilinear Forms*, §*Isometries*. No step uses a topology, a distance or a limit.

## The Four Forms

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

*Proof.* Each pairing is the scalar part of one of the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra*, and $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$; both the quaternion conjugation and the Hermitian conjugation act on the $\mu$-th unit by the sign $\varepsilon_\mu$, the second conjugating the coefficients as well. The four diagonal forms $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\sum_\mu Q_\mu^{2}$, $\sum_\mu|Q_\mu|^{2}$ and $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$ separate the pairings on the units.

**Remark (the four forms are one family).** Any two of the four are reached from the others by the two sign characters of the argument,
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1^{\natural},\tilde Q_2\rangle,
\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\ast}=\langle\tilde Q_1,\bar{\tilde Q}_2\rangle_{\natural},
$$
so the forms differ only in which of the identity, $\natural$, $\bar{\cdot}$ and $\ast$ is inserted into which slot. The adjoints differ in exactly the same way.

## The Four Adjoints

**Definition (the adjoint of a form).** For one of the four forms $\phi$ and a $\mathbb{C}$-linear map $F$ of $\mathbb{B}$, the **adjoint of $F$ for $\phi$** is the unique map $F^{\phi}$ with

$$
\phi\bigl(F\tilde Q_1,\tilde Q_2\bigr)=\phi\bigl(\tilde Q_1,F^{\phi}\tilde Q_2\bigr)\qquad\text{for all }\tilde Q_1,\tilde Q_2\in\mathbb{B}.
$$

The form is non-degenerate, so the adjoint exists and is unique. It is $\mathbb{C}$-linear in all four cases, and $F\mapsto F^{\phi}$ is linear in the two bilinear cases and conjugate linear in the two sesquilinear ones.

**Theorem (the four adjoints, named).** For the left multiplication $L_{\tilde Q_6}$, the right multiplication $R_{\tilde Q_3}$ and their product,

| name of the adjoint | mark | on $L_{\tilde Q_6}$ | on $R_{\tilde Q_3}$ | on $L_{\tilde Q_6}R_{\tilde Q_3}$ |
|---|---|---|---|---|
| the **plain bilinear adjoint** | $\approx$ | $R_{\tilde Q_6}$ | $L_{\tilde Q_3}$ | $L_{\tilde Q_3}R_{\tilde Q_6}$ |
| the **quaternionic adjoint** | $\natural$ | $L_{\tilde Q_6^{\natural}}$ | $R_{\tilde Q_3^{\natural}}$ | $L_{\tilde Q_6^{\natural}}R_{\tilde Q_3^{\natural}}$ |
| the **Hermitian adjoint** | $\ast$ | $L_{\tilde Q_6^{\ast}}$ | $R_{\tilde Q_3^{\ast}}$ | $L_{\tilde Q_6^{\ast}}R_{\tilde Q_3^{\ast}}$ |
| the **Krein adjoint** | $\natural\ast$ | $R_{\bar{\tilde Q_6}}$ | $L_{\bar{\tilde Q_3}}$ | $L_{\bar{\tilde Q_3}}R_{\bar{\tilde Q_6}}$ |

*Proof.* Write $\mathrm{Sc}$ for the scalar part. **The plain bilinear adjoint.** $\mathrm{Sc}(\tilde Q_6\tilde Q_1\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2\tilde Q_6)$ by the cyclicity of $\mathrm{Sc}$, which is $\langle L_{\tilde Q_6}\tilde Q_1,\tilde Q_2\rangle=\langle\tilde Q_1,R_{\tilde Q_6}\tilde Q_2\rangle$; the two-sided row follows from $(FG)^{\approx}=G^{\approx}F^{\approx}$. **The quaternionic adjoint.** $\mathrm{Sc}((\tilde Q_6\tilde Q_1)^{\natural}\tilde Q_2)=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_6^{\natural}\tilde Q_2)$, so the adjoint is $L_{\tilde Q_6^{\natural}}$ and no factor is exchanged; on the product the two factors are again *not* exchanged, because $L$ and $R$ commute. **The Hermitian adjoint.** The same computation with the conjugate linear $\ast$ in place of $\natural$. **The Krein adjoint.** $\mathrm{Sc}((\tilde Q_6\tilde Q_1)^{\natural}\tilde Q_2^{\ast})=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_6^{\natural}\tilde Q_2^{\ast})$ and $\tilde Q_6^{\natural}\tilde Q_2^{\ast}=(\tilde Q_2\bar{\tilde Q_6})^{\ast}$, so the adjoint is $R_{\bar{\tilde Q_6}}$; on the product the factors are exchanged. All sixteen cases on the pairs of basis elements were checked one by one.

**Corollary (what each adjoint does to the two parameters).** The plain bilinear adjoint **exchanges the parameters and conjugates nothing**. The quaternionic adjoint **keeps the parameters in place** and replaces each by its image under $\natural$. The Hermitian adjoint **keeps the parameters in place** and conjugates each. The Krein adjoint **exchanges the parameters and conjugates each**.

So two rules decide the shape of the table, and both are read off the first two columns. The adjoint **exchanges the side exactly for the two forms of Gram matrix $\mathrm{E}$**, and it **conjugates the parameter exactly for the two sesquilinear forms**.

**Remark (why the mark $\natural$ appears on two different kinds of object).** The mark $\natural$ on an element is the quaternion conjugation, $\tilde Q\mapsto\tilde Q^{\natural}$, which negates the vector part. The mark $\natural$ on a map is the quaternionic adjoint, $F\mapsto F^{\natural}$. They are the same mark because they are the same operation seen once on elements and once on operators: the quaternionic adjoint of $L_{\tilde Q}$ is $L_{\tilde Q^{\natural}}$. No other reading of the mark is used in this article.

## The Associate

The plain bilinear adjoint is the one adjoint the corpus has studied on its own, and it carries a calculus. Write it $\approx$ for a general $\mathbb{C}$-linear map $F$, not only for a one-sided or a two-sided operator.

**Proposition (the plain bilinear adjoint is an involution that reverses composition).** For $\mathbb{C}$-linear maps $F,G$ of $\mathbb{B}$,

$$
(F^{\approx})^{\approx}=F,\qquad (F\circ G)^{\approx}=G^{\approx}\circ F^{\approx},
$$

and the defining property reads $\mathrm{Sc}(F(\tilde Q_1)\tilde Q_2)=\mathrm{Sc}(\tilde Q_1F^{\approx}(\tilde Q_2))$.

*Proof.* The involution and the exchange of the factors in a composite are the uniqueness of the adjoint applied twice; the display is the definition with $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ substituted.

**Proposition (the plain bilinear adjoint on the Conway basis).** On the Conway operator basis $e_n[\,]e_m$, the elementary operator being $(e_n[\,]e_m)(\tilde Q)=e_n\tilde Q e_m$,

$$
\bigl(e_n[\,]e_m\bigr)^{\approx}=e_m[\,]e_n,
\qquad\text{so}\qquad
\Bigl(\sum_{n,m}A_{nm}\,e_n[\,]e_m\Bigr)^{\approx}=\sum_{n,m}A_{nm}\,e_m[\,]e_n .
$$

The edge rows $L_a=\sum_n a_n\,e_n[\,]e_t$ and $R_b=\sum_m b_m\,e_t[\,]e_m$ give back $L_a^{\approx}=R_a$ and $R_b^{\approx}=L_b$, which is the first row of the theorem of §*The Four Adjoints*.

*Proof.* $\langle(a[\,]b)\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(a\tilde Q_1b\tilde Q_2)=\mathrm{Sc}(\tilde Q_1b\tilde Q_2a)=\langle\tilde Q_1,(b[\,]a)\tilde Q_2\rangle$, and the adjoint is unique. The Conway basis is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Conway Operator Basis*.

**Proposition (the matrix of the plain bilinear adjoint).** Let $F$ have matrix $M$ in the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$. Then the plain bilinear adjoint has matrix

$$
M^{\approx}=\mathrm{E}\,M^{\mathsf T}\mathrm{E},
$$

the sign matrix $\mathrm{E}$ conjugating the plain transpose.

*Proof.* On coordinate columns the form is $\langle\tilde Q_1,\tilde Q_2\rangle=Q_1^{\mathsf T}\mathrm{E}Q_2$, so $(MQ_1)^{\mathsf T}\mathrm{E}Q_2=Q_1^{\mathsf T}M^{\mathsf T}\mathrm{E}Q_2$ and $Q_1^{\mathsf T}\mathrm{E}M^{\approx}Q_2$ are equal for all $Q_1,Q_2$; hence $M^{\mathsf T}\mathrm{E}=\mathrm{E}M^{\approx}$ and $\mathrm{E}^{-1}=\mathrm{E}$.

**Remark (when the plain bilinear adjoint is the plain transpose).** The two agree exactly when $M^{\mathsf T}$ commutes with $\mathrm{E}$. An operator that fixes $e_t$ and preserves the vector subspace has a block form $\operatorname{diag}(1,M)$ with $M$ of size $3$, and the conjugation by $\mathrm{E}$ acts as $-1$ on the two off-diagonal blocks and as the identity on the two diagonal ones, so it is invisible there and $M^{\approx}=M^{\mathsf T}$. For a general map the two differ. The general statement is the transpose of a bilinear form, $M\mapsto G^{-1}M^{\mathsf T}G$ (*Bilinear Forms*, §*Isometries*; *Quadratic Forms and Polarisation*, §*Isometry of Forms*).

**Proposition (the plain bilinear adjoint against the Hermitian adjoint).** Let $\bar F$ be the map obtained from $F$ by conjugating every coefficient. Then

$$
\overline{F}^{\approx}=\mathrm{E}\,F^{\ast}\,\mathrm{E}.
$$

*Proof.* Conjugating the coefficients conjugates the entries, so $\overline{F}^{\approx}$ has matrix $\mathrm{E}\bar M^{\mathsf T}\mathrm{E}$; the Hermitian adjoint has matrix $M^{\dagger}=\overline{M^{\mathsf T}}$, and $\mathrm{E}F^{\ast}\mathrm{E}=\mathrm{E}\overline{M^{\mathsf T}}\mathrm{E}$ is the same matrix.

**Corollary (the collapse on the vector-preserving unitaries).** On the operators of block form $\operatorname{diag}(1,N)$ the conjugation by $\mathrm{E}$ is invisible, so the proposition reads $\overline{F}^{\approx}=F^{\ast}$, and for a $\ast$-unitary $F$ it reads $F^{\ast}=F^{-1}$. On those operators the plain transpose, the plain bilinear adjoint and the Hermitian adjoint are one involution, which is why the source literature writes the three interchangeably. For a general linear map they are three, and the corpus keeps them apart: the plain bilinear adjoint is the adjoint of the form of Gram matrix $\mathrm{E}$, the dagger the adjoint of the form of Gram matrix $\mathrm{I}_4$.

## The Four Pairs

Read as an operator, each adjoint pairs the parameter with a second element. The five pairs are the five rows of the second table of the introduction, and the second factor is what distinguishes them:

| name of the pair | operator | second factor | the adjoint behind it |
|---|---|---|---|
| **Plain Bilinear Pair** | $L_{\tilde Q_6}R_{\tilde Q_3}$, both parameters free | $\tilde Q_3$, independent | the plain bilinear adjoint |
| **Quaternionic Pair** | $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ | $\tilde Q_6^{\natural}$ | the quaternionic adjoint |
| **Hermitian Pair** | $L_{\tilde Q_6}R_{\tilde Q_6^{\ast}}$ | $\tilde Q_6^{\ast}$ | the Hermitian adjoint |
| **Signed Hermitian Pair** | $L_{\tilde Q_6^{\natural}}R_{\tilde Q_6^{\ast}}$ | $\tilde Q_6^{\ast}$, with the sign on the left factor | the Hermitian adjoint |
| **Krein Pair** | $L_{\tilde Q_6}R_{\bar{\tilde Q_6}}$ | $\bar{\tilde Q_6}$ | the Krein adjoint |

The first row is the only one with two free parameters; the other four are graphs of a conjugation inside the two-sided family. That is the reason the first row is named after the adjoint that exchanges the parameters and the other four after adjoints that tie them.

**The signed left multiplication.** The quaternionic adjoint of $L_{\tilde Q_6}$ is not merely a left multiplication; it is the left multiplication by the image of the parameter under the sign. On an element it reads

$$
L_{\tilde Q_6^{\natural}}(\tilde Q)=\tilde Q_6^{\natural}\tilde Q,
$$

the **signed left multiplication**, a left multiplication whose parameter has been put through $\alpha=\natural$. This is what the name *signed inner conjugation* records: the family $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ is the inner conjugation with the sign on one factor, and its adjoint is the signed left multiplication.

## One Operator through the Four Adjoints

The example works one operator $F=L_{\tilde Q_6}R_{\tilde Q_3}$ with $\tilde Q_6=e_t+2\vec e_x$ and $\tilde Q_3=e_t+i\vec e_z$ through all four adjoints, and names each result. The matrices are in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the columns being the images of the four units.

$$
F=\mathsf{M}_{4L}(\tilde Q_6)\mathsf{M}_{4R}(\tilde Q_3)=
\begin{pmatrix}
1&-2&-2i&-i\\
2&1&i&-2i\\
-2i&-i&1&-2\\
i&-2i&2&1
\end{pmatrix},
$$
$$
F^{\approx}=\mathsf{M}_{4L}(\tilde Q_3)\mathsf{M}_{4R}(\tilde Q_6)=
\begin{pmatrix}
1&-2&2i&-i\\
2&1&-i&-2i\\
2i&i&1&2\\
i&-2i&-2&1
\end{pmatrix},
\qquad
F^{\natural}=\mathsf{M}_{4L}(\tilde Q_6^{\natural})\mathsf{M}_{4R}(\tilde Q_3^{\natural})=
\begin{pmatrix}
1&2&-2i&i\\
-2&1&-i&-2i\\
-2i&i&1&2\\
-i&-2i&-2&1
\end{pmatrix},
$$
$$
F^{\ast}=\mathsf{M}_{4L}(\tilde Q_6^{\ast})\mathsf{M}_{4R}(\tilde Q_3^{\ast})=
\begin{pmatrix}
1&2&2i&-i\\
-2&1&i&2i\\
2i&-i&1&2\\
i&2i&-2&1
\end{pmatrix},
\qquad
F^{\natural\ast}=\mathsf{M}_{4L}(\bar{\tilde Q_3})\mathsf{M}_{4R}(\bar{\tilde Q_6})=
\begin{pmatrix}
1&-2&-2i&i\\
2&1&i&2i\\
-2i&-i&1&2\\
-i&2i&-2&1
\end{pmatrix}.
$$

The five matrices are distinct, and each of the four adjoints moves the matrix in its own way.

- **The plain bilinear adjoint** exchanges the two parameters: $2\vec e_x$ and $i\vec e_z$ change places.
- **The quaternionic adjoint** keeps them in place and replaces each by $\tilde Q_6^{\natural}=e_t-2\vec e_x$ and $\tilde Q_3^{\natural}=e_t-i\vec e_z$.
- **The Hermitian adjoint** keeps them in place and replaces each by $\tilde Q_6^{\ast}=e_t-2\vec e_x$ and $\tilde Q_3^{\ast}=\tilde Q_3=e_t+i\vec e_z$.
- **The Krein adjoint** exchanges them and conjugates: $L_{\bar{\tilde Q_3}}R_{\bar{\tilde Q_6}}$.

The signed and the Hermitian adjoints agree on the first parameter, which has real coefficients, and differ on the second: $\tilde Q_3$ is Hermitian, so the star fixes it while the sign turns $i\vec e_z$ into $-i\vec e_z$. That difference and the bar on the entries are what separate the matrices $F^{\natural}$, $F^{\ast}$ and $F^{\natural\ast}$. None of the four adjoints equals $F$: the example is self-adjoint for no pairing, which is the generic case.

## Self-Adjointness under the Four Adjoints

The four adjoints separate the parameters. The table gives, for the graded two-sided operator $L_{\tilde Q}R_{\tilde Q^{\natural}}$ of the second row of §*The Four Pairs*, whether the operator equals its own adjoint; the columns are the four names.

| parameter | **plain bilinear adjoint** | **quaternionic adjoint** | **Hermitian adjoint** | **Krein adjoint** |
|---|---|---|---|---|
| $2+i$, central | yes | yes | no | no |
| $\vec e_x$, real vector | yes | yes | yes | yes |
| $2\vec e_x+i\vec e_y$, vector, complex coefficients | yes | yes | no | no |
| $e_t+2i\vec e_x$, Hermitian | no | no | yes | yes |
| $1+2\vec e_x$, real, mixed | no | no | no | no |

**Corollary (the two criteria).** The operator $L_{\tilde Q}R_{\tilde Q^{\natural}}$ is self-adjoint for the **plain bilinear adjoint** and for the **quaternionic adjoint** exactly when $\tilde Q^{\natural}$ is parallel to $\tilde Q$, that is exactly when $\tilde Q$ is central or lies in the vector subspace $V$. It is self-adjoint for the **Hermitian adjoint** and for the **Krein adjoint** exactly when the two equations

$$
\tilde Q^{\ast}=\lambda\tilde Q,\qquad \bar{\tilde Q}=\lambda^{-1}\tilde Q^{\natural}
$$

hold for one scalar $\lambda\in\mathbb{C}^{\times}$.

*Proof.* Self-adjointness is an equality of two decomposable tensors, and $L_{\tilde Q_4}R_{\tilde Q_5}=L_{\tilde Q_4'}R_{\tilde Q_5'}$ if and only if $\tilde Q_4'=\lambda\tilde Q_4$ and $\tilde Q_5'=\lambda^{-1}\tilde Q_5$ for one $\lambda$, the map $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ being faithful because $\mathbb{B}$ is central simple. Substituting the four rows of the theorem of §*The Four Adjoints* gives one equation for the two bilinear adjoints, because there the two adjoints of the graded operator are the same operator, and two equations for the two sesquilinear ones, because there they differ. The table is the evaluation on the five parameters.

**Remark (why the fourth row of the table fails).** The parameter $1+2\vec e_x$ is real, and a real parameter is one's first guess for a self-adjoint operator. It fails. The plain bilinear adjoint sends $L_{\tilde Q}R_{\tilde Q^{\natural}}$ to $L_{\tilde Q^{\natural}}R_{\tilde Q}$, and the fibre theorem then asks for $\tilde Q^{\natural}\parallel\tilde Q$, which holds for a real *scalar* and for a real *vector* but not for a real mixture: $1-2\vec e_x$ is not a multiple of $1+2\vec e_x$. The two columns of the table that fail together are the two bilinear adjoints, and they fail on the same parameters.

## The Two Sectors

The five families are compared by what they do to the two sectors of the Hermitian conjugation. One of them keeps both sectors in place for every parameter, and the other four do not.

**The two sectors.** Put

$$
\mathbb{B}_{\Psi}=\{\tilde X:\tilde X^{\ast}=\tilde X\},\qquad
\mathbb{B}_{\Phi}=\{\tilde X:\tilde X^{\ast}=-\tilde X\}.
$$

Each is a real subspace of real dimension four, and they are the eigenspaces of the involution $\ast$ for the eigenvalues $+1$ and $-1$. The central $i$ exchanges them, $\mathbb{B}_{\Phi}=i\,\mathbb{B}_{\Psi}$, because $\ast$ is conjugate linear. Neither is a complex subspace. The four elements $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ are a complex basis of $\mathbb{B}$ inside $\mathbb{B}_{\Psi}$, and $ie_t,\vec e_x,\vec e_y,\vec e_z$ are a complex basis inside $\mathbb{B}_{\Phi}$.

**Theorem (the two-sided operators that preserve a sector).** Let $\tilde Q_6\ne0$. The operator $L_{\tilde Q_6}R_{\tilde Q_3}$ maps $\mathbb{B}_{\Psi}$ into itself if and only if $\tilde Q_3=\lambda\tilde Q_6^{\ast}$ with $\lambda$ real, and each such operator maps $\mathbb{B}_{\Phi}$ into itself as well.

*Proof.* Suppose $\tilde Q_3=\lambda\tilde Q_6^{\ast}$ with $\lambda$ real. By the antimultiplicativity of $\ast$,

$$
\bigl(\tilde Q_6\tilde X\lambda\tilde Q_6^{\ast}\bigr)^{\ast}
=(\lambda\tilde Q_6^{\ast})^{\ast}\,\tilde X^{\ast}\,\tilde Q_6^{\ast}
=\bar\lambda\,\tilde Q_6\tilde X^{\ast}\tilde Q_6^{\ast},
$$

so for $\tilde X^{\ast}=\pm\tilde X$ the image satisfies the same equation with the same sign. Conversely, suppose the operator maps $\mathbb{B}_{\Psi}$ into itself. For $\tilde X^{\ast}=\tilde X$ the antimultiplicativity gives $(\tilde Q_6\tilde X\tilde Q_3)^{\ast}=\tilde Q_3^{\ast}\tilde X\tilde Q_6^{\ast}$, so the preservation reads $L_{\tilde Q_3^{\ast}}R_{\tilde Q_6^{\ast}}\tilde X=L_{\tilde Q_6}R_{\tilde Q_3}\tilde X$ for every $\tilde X\in\mathbb{B}_{\Psi}$. Those four basis elements are a complex basis and both operators are $\mathbb{C}$-linear, so the two operators are equal. The fibre theorem then gives $\tilde Q_6=\mu\tilde Q_3^{\ast}$ and $\tilde Q_3=\mu^{-1}\tilde Q_6^{\ast}$ for one $\mu\in\mathbb{C}^{\times}$. Applying $\ast$ to the first gives $\tilde Q_6^{\ast}=\bar\mu\tilde Q_3$, and substituting into the second gives $\tilde Q_3=\mu^{-1}\bar\mu\tilde Q_3$, hence $\mu=\bar\mu$; so $\mu$ is real and so is $\lambda=\mu^{-1}$. The preservation of $\mathbb{B}_{\Phi}$ follows from the centrality of $i$: a $\mathbb{C}$-linear map sends $i\tilde X$ to $i$ times the image of $\tilde X$, so $i\,\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$ goes into itself.

**Corollary (only the Hermitian pair, of the five).** The second factors of the five pairs are $\tilde Q_3$ free for the Plain Bilinear Pair, $\tilde Q_6^{\natural}$ for the Quaternionic Pair, $\tilde Q_6^{\ast}$ for the Hermitian Pair, $\tilde Q_6^{\ast}$ again for the Signed Hermitian Pair, and $\bar{\tilde Q_6}$ for the Krein Pair. The criterion of the theorem is met by the **Hermitian pair** with $\lambda=1$, for every parameter. It is met by the other four only where the second factor is parallel to the star of the first: by the Quaternionic Pair where $\tilde Q_6^{\natural}\parallel\tilde Q_6^{\ast}$, by the Signed Hermitian Pair where $\tilde Q_6^{\ast}\parallel(\tilde Q_6^{\natural})^{\ast}$, by the Krein Pair where $\bar{\tilde Q_6}\parallel\tilde Q_6^{\ast}$, and by the Plain Bilinear Pair only where $\tilde Q_3$ is a real multiple of $\tilde Q_1^{\ast}$, a proper subvariety of the pair. Each of these conditions is proper, so only the Hermitian pair keeps the sectors for every parameter.

**Example (one parameter, three failures, one success).** Take $\tilde Q_6=e_t+2i\vec e_x$, of norm $\langle\tilde Q_6\rangle_{\natural}=-3$, and $\tilde X=i\vec e_y\in\mathbb{B}_{\Psi}$. The four pairs send it to

$$
\text{Plain Bilinear Pair: }-\tfrac13\bigl(5i\vec e_y-4\vec e_z\bigr),
\qquad
\text{Quaternionic Pair: }5i\vec e_y-4\vec e_z,
$$
$$
\text{Hermitian Pair: }-3i\vec e_y,
\qquad
\text{Krein Pair: }5i\vec e_y-4\vec e_z .
$$

The second and the fourth agree here because for this parameter $\tilde Q_6^{\natural}=e_t-2i\vec e_x=\bar{\tilde Q_6}$. The first, the second and the fourth images carry a real coefficient on $\vec e_z$ and lie in neither sector, since $Y^{\ast}\ne\pm Y$ for them. The third is a multiple of $i\vec e_y$ and is Hermitian, as the theorem says.

**Remark (a real parameter hides the difference).** For a real $\tilde Q_6$ the star and the inverse differ only by the norm. The star is then the quaternion conjugation, $\tilde Q_6^{\ast}=\tilde Q_6^{\natural}$, and the inverse is $\tilde Q_6^{-1}=\langle\tilde Q_6\rangle_{\natural}^{-1}\tilde Q_6^{\ast}$ with the norm real and nonzero, so the plain pair preserves the sectors too. On the real quaternion subspace the plain pair and the Hermitian pair behave alike on the sectors, and the two separate only for a complex parameter, where the inverse and the star are no longer parallel.

**Remark (one side is not enough).** A one-sided operator preserves a sector only trivially. If $L_{\tilde Q_6}$ maps $\mathbb{B}_{\Psi}$ into itself then $\tilde Q_6^{\ast}=\tilde Q_6$ by the value at $e_t$, and then $\tilde X\tilde Q_6^{\ast}=\tilde Q_6\tilde X$ for every $\tilde X\in\mathbb{B}_{\Psi}$, whose complex basis forces $\tilde Q_6$ central; and a central $\lambda e_t$ preserves $\mathbb{B}_{\Psi}$ exactly when $\lambda$ is real. The same holds for $R_{\tilde Q_6}$. The sector is therefore a property of a two-sided action, and in that action the second factor is forced to be the star of the first.

## The Signed and the Unsigned Inner Conjugation

The word *signed* carries a second meaning, in the operators rather than in the adjoints. Two maps share a name in the corpus and differ by the sign $\natural$:

$$
\mathrm{Ad}_{\tilde Q_6}(\tilde Q)=\tilde Q_6\tilde Q\tilde Q_6^{-1},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q)=\tilde Q_6^{\natural}\tilde Q\tilde Q_6^{-1},
$$

the **unsigned inner conjugation** and the **signed inner conjugation**. The second is the first with $\alpha=\natural$ inserted on the left factor, and it is the operator of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, where $\mathrm{Ad}^{\alpha}_{U}(v)=\alpha(U)vU^{-1}$. The family it generates is the Quaternionic Pair of the table above, and the earlier name of that family, Signed Inner Conjugation, is the one used in the Clifford articles.

**Proposition (the difference is twice the vector part).** For an invertible $\tilde Q_6$,

$$
\mathrm{Ad}^{\alpha}_{\tilde Q_6}-\mathrm{Ad}_{\tilde Q_6}
=\bigl(\tilde Q_6^{\natural}-\tilde Q_6\bigr)(\cdot)\tilde Q_6^{-1}
=-2\,\vec Q_6\,(\cdot)\,\tilde Q_6^{-1}.
$$

So $\mathrm{Ad}^{\alpha}_{\tilde Q_6}=\mathrm{Ad}_{\tilde Q_6}$ when $\tilde Q_6$ is central, and $\mathrm{Ad}^{\alpha}_{\tilde Q_6}=-\mathrm{Ad}_{\tilde Q_6}$ when $\tilde Q_6$ lies in $V$. The second case is the insertion of the sign at its sharpest: for $\tilde Q_6\in V$ the whole operator is negated.

*Proof.* $\tilde Q_6^{\natural}-\tilde Q_6=-2\vec Q_6$ with $\vec Q_6=\tilde Q_6-Q_{6t}e_t$. If $\vec Q_6=0$ the difference vanishes; if $Q_{6t}=0$ then $\tilde Q_6^{\natural}=-\tilde Q_6$.

**Worked example (the two extreme parameters).** For $\tilde Q_6=ie_t$, central, both operators are the identity. For $\tilde Q_6=\vec e_x\in V$, of norm one and with $\vec e_x^{-1}=-\vec e_x$,

$$
\mathrm{Ad}_{\vec e_x}=\operatorname{diag}(1,1,-1,-1),
\qquad
\mathrm{Ad}^{\alpha}_{\vec e_x}=\operatorname{diag}(-1,-1,1,1)=-\mathrm{Ad}_{\vec e_x}.
$$

The unsigned operator fixes $e_t$ and $\vec e_x$ and negates the plane $\mathbb{C}\{\vec e_y,\vec e_z\}$; the signed operator does the opposite. Both are isometries of the plain form, and both have determinant one on the complex four-dimensional space, which has even dimension.

**Worked example ($\tilde Q_6=e_t+\vec e_x$, mixed).** The two operators and their difference are

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
\qquad
\mathrm{Ad}^{\alpha}_{\tilde Q_6}-\mathrm{Ad}_{\tilde Q_6}=
\begin{pmatrix}
-1&1&0&0\\
-1&-1&0&0\\
0&0&1&1\\
0&0&-1&1
\end{pmatrix}.
$$

The unsigned operator is the identity on $\mathbb{C}\{e_t,\vec e_x\}$ and the quarter turn $\vec e_y\mapsto\vec e_z$, $\vec e_z\mapsto-\vec e_y$ on $\mathbb{C}\{\vec e_y,\vec e_z\}$; the signed operator interchanges the two roles. The difference is twice the vector part, $2\vec Q_6=2\vec e_x$.

**Corollary (the sign costs multiplicativity).** The unsigned inner conjugation is an algebra automorphism for every unit. The signed inner conjugation with a parameter in $V$ is **anti**-multiplicative, $\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q_1\tilde Q_2)=-\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q_1)\mathrm{Ad}^{\alpha}_{\tilde Q_6}(\tilde Q_2)$. Both statements were verified on one hundred pairs. This is the concrete cost of the insertion, and it is the reason the signed operators of the corpus are read for their own laws and not as automorphisms.

**Remark (two places for the sign, and the norm records it).** The corpus writes $\mathrm{Ad}^{\alpha}$ with the sign on the left factor, and it writes the graded two-sided operator $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ with the sign on the right. The two are exchanged by the inverse and by the norm:

$$
L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}=\langle\tilde Q_6\rangle_{\natural}\,\mathrm{Ad}_{\tilde Q_6},
\qquad
\mathrm{Ad}^{\alpha}_{\tilde Q_6}=\langle\tilde Q_6\rangle_{\natural}\,L_{\tilde Q_6^{-1}}R_{\tilde Q_6^{-1}},
\qquad
\langle\tilde Q_6\rangle_{\natural}=\tilde Q_6\tilde Q_6^{\natural},
$$

verified on one hundred invertible elements. On the shell $\langle\tilde Q_6\rangle_{\natural}=\pm1$ the first line reads $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}=\pm\mathrm{Ad}_{\tilde Q_6}$: the same operator is the inner automorphism or its negative according to the sign of the norm. That is the second reading of the word *signed*, and it is the reading under which the graded two-sided operator is the operator of *Two-Sided Operators on the General Quaternionic Algebra of the Biquaternions*.

## Summary

The biquaternion algebra has four forms and four adjoints, and the four adjoints have four names: the **plain bilinear adjoint** $\approx$, the **quaternionic adjoint** $\natural$, the **Hermitian adjoint** $\ast$ and the **Krein adjoint** $\natural\ast$, in the order of the plain bilinear, the quaternionic bilinear, the plain sesquilinear and the quaternionic sesquilinear form. The plain bilinear adjoint and the Krein adjoint exchange the two sides; the signed and the Hermitian adjoints keep them. The plain bilinear adjoint and the quaternionic adjoint carry no bar; the Hermitian and the Krein adjoints carry one.

Five operator families are named after these four adjoints and carry their names: the **Plain Bilinear Pair** after the plain bilinear adjoint, the **Quaternionic Pair** after the quaternionic adjoint, the **Hermitian Pair** and the **Signed Hermitian Pair** after the Hermitian adjoint, the second with the sign inserted into the operator, and the **Krein Pair** after the Krein adjoint. The word *signed* names one operation in all of them, the insertion of $\natural$.

The plain bilinear adjoint has a calculus of its own: it is an involution, it reverses composition, it reverses the factors of the Conway basis, its matrix is $\mathrm{E}M^{\mathsf T}\mathrm{E}$, and combined with the coefficient conjugation it relates to the Hermitian adjoint by $\overline{F}^{\approx}=\mathrm{E}F^{\ast}\mathrm{E}$, which collapses to $F^{\ast}=F^{-1}$ on the vector-preserving unitaries.

One operator $L_{\tilde Q_6}R_{\tilde Q_3}$ has four distinct adjoint matrices, and the four self-adjointness criteria separate the parameters: the two bilinear adjoints hold exactly when $\tilde Q^{\natural}\parallel\tilde Q$, the two sesquilinear ones exactly when one scalar $\lambda$ solves $\tilde Q^{\ast}=\lambda\tilde Q$ and $\bar{\tilde Q}=\lambda^{-1}\tilde Q^{\natural}$.

Of the five families only the **Hermitian pair** preserves the sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ for every parameter. The criterion is $\tilde Q_3=\lambda\tilde Q_6^{\ast}$ with $\lambda$ real, and the other four meet it only on proper subvarieties. A one-sided operator preserves a sector only for a real scalar, which is why the sectors belong to the two-sided action. No step of the article uses a topology, a distance or a limit.

## Summary of Notation

| Symbol | Name | Meaning |
|---|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, Gram $\mathrm{E}$ | plain bilinear form | the form of the **plain bilinear adjoint** |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, Gram $\mathrm{I}_4$ | quaternionic bilinear form | the form of the **quaternionic adjoint** |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\ast}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\ast})$, Gram $\mathrm{I}_4$ | plain sesquilinear form | the form of the **Hermitian adjoint** |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural\ast}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{\ast})$, Gram $\mathrm{E}$ | quaternionic sesquilinear form | the form of the **Krein adjoint** |
| $F^{\approx}$ | the **plain bilinear adjoint** | $(L_{\tilde Q_6}R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}R_{\tilde Q_6}$; $(FG)^{\approx}=G^{\approx}F^{\approx}$, $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$, $M^{\approx}=\mathrm{E}M^{\mathsf T}\mathrm{E}$ |
| $F^{\natural}$ | the **quaternionic adjoint** | $(L_{\tilde Q_6}R_{\tilde Q_3})^{\natural}=L_{\tilde Q_6^{\natural}}R_{\tilde Q_3^{\natural}}$; the adjoint of $L_{\tilde Q}$ is the signed left multiplication $L_{\tilde Q^{\natural}}$ |
| $F^{\ast}$ | the **Hermitian adjoint** | $(L_{\tilde Q_6}R_{\tilde Q_3})^{\ast}=L_{\tilde Q_6^{\ast}}R_{\tilde Q_3^{\ast}}$ |
| $F^{\natural\ast}$ | the **Krein adjoint** | $(L_{\tilde Q_6}R_{\tilde Q_3})^{\natural\ast}=L_{\bar{\tilde Q_3}}R_{\bar{\tilde Q_6}}$ |
| $\natural$, $\bar{\cdot}$, $\ast=\natural\bar{\cdot}$ | the three conjugations | quaternion conjugation (the grade involution), coefficient conjugation, Hermitian conjugation |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Phi}=i\mathbb{B}_{\Psi}$ | the two sectors | the real eigenspaces of $\ast$ |
| $\mathrm{Ad}_{\tilde Q_6}$, $\mathrm{Ad}^{\alpha}_{\tilde Q_6}$ | unsigned and signed inner conjugation | $\tilde Q_6\tilde Q\tilde Q_6^{-1}$ and $\tilde Q_6^{\natural}\tilde Q\tilde Q_6^{-1}$; equal on the centre, opposite on $V$ |
| $\langle\tilde Q_6\rangle_{\natural}=\tilde Q_6\tilde Q_6^{\natural}$ | the quaternionic norm | $L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}=\langle\tilde Q_6\rangle_{\natural}\mathrm{Ad}_{\tilde Q_6}$ |

## Further Reading

- [Introduction to the Operators of the Biquaternion Algebra](introduction-to-the-operators-of-the-biquaternion-algebra.html), for the products-to-operators bridge that the four adjoints serve, and for the two switches $\sigma$ and $\alpha$ read in the parameters
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms, their Gram matrices and their signatures
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations, their group and their linearity
- [The Transposition of the Two Sides](the-transposition-of-the-two-sides.html), for the plain bilinear adjoint read as the transpose of the plain form, $L_{\tilde Q}^{\mathsf T}=R_{\tilde Q}$, for the conjugation $\natural L_{\tilde Q}\natural=R_{\tilde Q^{\natural}}$, and for the three maps that surround them
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the Conway operator basis on which the plain bilinear adjoint reverses the factors
- [Bilinear Forms](bilinear-forms.html), §*Isometries*, and [Quadratic Forms and Polarisation](quadratic-forms-and-polarisation.html), §*Isometry of Forms*, for the general transpose $M\mapsto G^{-1}M^{\mathsf T}G$
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the family of the plain bilinear adjoint, its swap law and its self-adjoint pairs
- [Two-Sided Operators on the General Quaternionic Algebra of the Biquaternions](two-sided-operators-on-the-general-quaternionic-algebra-of-the-biquaternions.html), for the graded two-sided operator, its quaternionic adjoint and its self-adjointness criterion
- [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html), for the Hermitian pair, its multiplicativity defect and the sector argument proved on the pair itself
- [The Indefinite Hermitian Pair of Operators on the General Quaternionic Sesqualgebra](the-indefinite-hermitian-pair-of-operators-on-the-general-quaternionic-sesqualgebra.html), for the family of the Krein adjoint
- [The Clifford, Pin and Spin Groups with Signed Inner Conjugation](the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.html), for $\mathrm{Ad}^{\alpha}_{U}(v)=\alpha(U)vU^{-1}$ and the general meaning of the sign
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for the adjoint of a linear map with respect to a bilinear or a sesquilinear form
