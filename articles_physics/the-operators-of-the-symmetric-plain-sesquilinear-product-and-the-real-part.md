# __The Operators of the Symmetric Plain Sesquilinear Product and the Real Part__

## Introduction

This article is the operator article of the SPS band, the band of positivity. Its product is the symmetric part of the plain sesquilinear product of the biquaternion algebra, the sesquilinear product $\tilde P\tilde Q^{*}$ symmetrised under the natural conjugation ${}^{\natural}$:

$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P\tilde Q^{*}+(\tilde P\tilde Q^{*})^{\natural}\bigr).
$$

The product is **symmetric** — the symmetric part of the parent product $\tilde P\tilde Q^{*}$ under ${}^{\natural}$ — and **sesquilinear**, and its value is central and computed by a Hermitian form,

$$
\tilde P\star\tilde Q=H(\tilde P,\tilde Q)\,e_0,\qquad H(\tilde P,\tilde Q)=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

the identity in which the whole block is read (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the form is *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*). The operators of the block are the two maps that attach an element to an argument on the left and on the right:

$$
L^{\star}_{\tilde A}\tilde R=\tilde A\star\tilde R=H(\tilde A,\tilde R)\,e_0,\qquad R^{\star}_{\tilde A}\tilde R=\tilde R\star\tilde A=H(\tilde R,\tilde A)\,e_0 .
$$

Because the product is sesquilinear, the left family is **conjugate-linear** and the right family is **$\mathbb{C}$-linear**; because the value is central and the form's symmetry is the conjugate symmetry $H(\tilde R,\tilde A)=\overline{H(\tilde A,\tilde R)}$, the two families are the pointwise conjugates of one another. The operator theory of the family, its rank, image, kernel, traces and composition laws, is *The Multiplication Operators of the Symmetric Plain Sesqualgebra*, and the general adjoint rules are *The Sesquilinear Adjoint Operator*; this article reads them for the band and states the one thing the composition laws do not: **which form the operators are adjoint for, and what that adjoint does to the parameter**.

The answer is one sentence. The form is the Hermitian form $H$ of the band, whose symmetry is the **conjugate** symmetry $H(\tilde Q,\tilde P)=\overline{H(\tilde P,\tilde Q)}$; its adjoint is therefore an adjoint of **conjugation** type and it **keeps the side** of the family instead of exchanging the two sides as the transpose of the GPA band does. Every type criterion of the block is a consequence, and each is a criterion on the **single parameter** $\tilde A$: a left multiplication is self-adjoint exactly when its parameter is central, a right multiplication exactly when its parameter is a **real** central scalar. The one feature peculiar to the SPS row is that the family is **rank one**, and it sharpens the contrast with the GPA row to a negative answer: off the central parameters the adjoint of a one-sided operator is **not a multiplication of the block at all**. With the GPS band, this band owns the **physical** adjoint — the Hermitian adjoint whose fixed points are the observables — and not a transpose.

**What the band owns and what it cites.** The positivity of the product, the cone of the operation, the reality of the diagonal and the classical composition are the business of the two sibling articles, *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* and *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*; they are cited and not repeated. The positivity of the dagger and the Hermitian cone $\{\tilde Q\tilde Q^{*}\}$ are the mathematics of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* and *The Positive Cone of an Involutive Algebra*, and the physics of the positivity of the band is *Mass, Rank and the Positivity of the Dagger*, which owns that positivity. The rank-one family, the traces and the composition laws are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*; the parity, the twisted rule and the adjoint rules of the class are *The Sesquilinear Adjoint Operator* and *The Adjoint of the Sesquilinear Sandwich*; the contrast with the bilinear central sibling is *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*. The crossing of the twelve rows is *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve.

**The questions of the block.** The article follows the model of the operator article of the general plain product and answers its five questions in the band's own algebra: the **composition** of the two families; the **adjoint** — which form, and what the adjoint does to the parameter and to the side; the **types** — self-adjoint, skew-adjoint, form-preserving, multiplicative, and the adjoint of the sandwich; the **action** on the state space; and the **interpretation** under the job word of the band, positivity. Every algebraic statement is a theorem owned by one of the mathematics articles cited in the text and is followed by its interpretation.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with complex coefficients. The natural conjugation ${}^{\natural}$ fixes $i$ and negates $e_1,e_2,e_3$; the coefficientwise conjugation $\overline{\cdot}$ conjugates the four coefficients; the Hermitian conjugation is ${}^{*}=\overline{\cdot}\circ{}^{\natural}$, so that $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The form $H$ is linear in the first argument and conjugate-linear in the second, and it is positive definite: $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$, strictly positive off zero. The adjoint of a conjugate-linear operator $T$ is the map $T^{\dagger}$ with $H(T\tilde R,\tilde S)=\overline{H(\tilde R,T^{\dagger}\tilde S)}$ for all $\tilde R,\tilde S$, the twisted rule of the sesquilinear class; the adjoint of a $\mathbb{C}$-linear operator is the ordinary map with $H(T\tilde R,\tilde S)=H(\tilde R,T^{\dagger}\tilde S)$.

## The Two Multiplications and Their Composition

**Definition.** For $\tilde A\in\mathbb{B}$ the **left** and the **right multiplication** by $\tilde A$ are the maps

$$
L^{\star}_{\tilde A}\tilde R=H(\tilde A,\tilde R)e_0,\qquad R^{\star}_{\tilde A}\tilde R=H(\tilde R,\tilde A)e_0 .
$$

**Theorem (the parity and the conjugate relation).** The left family is conjugate-linear in its argument and the right family is $\mathbb{C}$-linear,

$$
L^{\star}_{\tilde A}(\lambda\tilde R)=\overline{\lambda}\,L^{\star}_{\tilde A}\tilde R,\qquad R^{\star}_{\tilde A}(\lambda\tilde R)=\lambda\,R^{\star}_{\tilde A}\tilde R ,
$$

and the two families are the pointwise conjugates of one another, $R^{\star}_{\tilde A}\tilde R=\overline{L^{\star}_{\tilde A}\tilde R}$, that is $R^{\star}_{\tilde A}=\overline{L^{\star}_{\tilde A}}$ with the bar on the value.

*Proof.* The linearity in a slot of the operator is the linearity of the form in the corresponding slot of the product, and the product is $\mathbb{C}$-linear in its first slot and conjugate-linear in its second. For the relation, $H(\tilde R,\tilde A)=\overline{H(\tilde A,\tilde R)}$ by the conjugate symmetry of $H$, and the value is central, so conjugating the value conjugates the operator. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Operators and Their Linearity*.)

**Read as a physical statement.** The two attachments of an operation to a state are **not of the same kind**: the left attachment is conjugate-linear and the right one is linear, because the product puts the conjugation on the side that the left multiplication uses. The symmetry of the product is what ties them: the right multiplication is the conjugate of the left one, so a single parametrised operation is read once on each side and the two interpretations are mirror images. This is the operator form of the conjugate-commutative law $\tilde Q\star\tilde P=\overline{\tilde P\star\tilde Q}$ of the band (*The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*).

**Theorem (rank one, image the centre, kernel a hyperplane).** For $\tilde A\neq0$ each of $L^{\star}_{\tilde A}$ and $R^{\star}_{\tilde A}$ has **rank one**, its image being the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$; the kernel of each is the hyperplane $\{\tilde R:H(\tilde A,\tilde R)=0\}$, of complex dimension three and real dimension six; neither is injective and each is surjective onto the centre.

*Proof.* Every value is a complex multiple of $e_0$, and $H(\tilde A,\cdot\,)$ is a nonzero conjugate-linear functional for $\tilde A\neq0$, so its image is $\mathbb{C}e_0$ and its kernel is a hyperplane. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*Rank, Image and Kernel*.)

**Read as a physical statement.** A multiplication of this band never produces a direction: it reads a number off the argument and places it in the centre. The block sees only the scalar part of a state, which is the operator content of the statement that the values of the product are probability values and lie in the centre (the sibling *Why Probability Values Are Central*). No operator of the block has an image containing a vector part, and the block therefore carries no internal rotation: the rotations of the state space are not multiplications of this product.

**Theorem (the composition laws).** For all $\tilde A,\tilde B\in\mathbb{B}$,

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}=A_0\,R^{\star}_{\tilde B},\qquad
R^{\star}_{\tilde A}R^{\star}_{\tilde B}=\overline{A_0}\,R^{\star}_{\tilde B},\qquad
L^{\star}_{\tilde A}R^{\star}_{\tilde B}=A_0\,L^{\star}_{\tilde B},\qquad
R^{\star}_{\tilde A}L^{\star}_{\tilde B}=\overline{A_0}\,L^{\star}_{\tilde B},
$$

where $A_0=H(\tilde A,e_0)$ is the scalar part of $\tilde A$. The family is closed under composition, and the assignment $\tilde A\mapsto L^{\star}_{\tilde A}$ is **not multiplicative**: $L^{\star}_{\tilde A}L^{\star}_{\tilde B}\neq L^{\star}_{\tilde A\star\tilde B}$ unless $A_0=0$.

*Proof.* $L^{\star}_{\tilde A}L^{\star}_{\tilde B}\tilde R=H(\tilde A,H(\tilde B,\tilde R)e_0)e_0=\overline{H(\tilde B,\tilde R)}\,H(\tilde A,e_0)e_0=A_0H(\tilde R,\tilde B)e_0$, and the other three are the same computation with the conjugation placed by the second slot; the failure of multiplicativity is the displayed identity against $L^{\star}_{A_0e_0}$, since $\tilde A\star\tilde B=H(\tilde A,\tilde B)e_0$. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Composition and the Failure of Multiplicativity*.)

**Read as a physical statement.** The composite of two operations of the band is a **scalar multiple of a one-sided operation**, the scalar being the form of the first parameter with the identity: composition reads the form. The family composes like the scalars it computes, which is the operator form of the centrality of the value; a scalar part vanishes and the composite vanishes with it, so the semigroup of the block collapses whenever the leading parameter has no central part. This is the sharpest difference from the associative unital GPA row, where the two families are genuine multiplications with $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ and the operators are invertible at invertible parameters: here there is no operator algebra, only a rank-one family closed under composition.

### The Traces

**Theorem (the traces).** In the basis $e_0,e_1,e_2,e_3$,

$$
\operatorname{Tr}\bigl(R^{\star}_{\tilde A}\bigr)=H(e_0,\tilde A)=\overline{A_0},\qquad \operatorname{Tr}\bigl(L^{\star}_{\tilde A}\bigr)=H(\tilde A,e_0)=A_0 ,
$$

the first the ordinary trace of the $\mathbb{C}$-linear operator, the second the trace of the conjugate-linear operator in the conjugate-linear convention; the real-linear trace of $L^{\star}_{\tilde A}$ is $0$.

*Proof.* The matrix of $R^{\star}_{\tilde A}$ has the single nonzero row $R^{\star}_{\tilde A}(e_j)=H(e_j,\tilde A)e_0$, whose diagonal entry is $H(e_0,\tilde A)=\overline{A_0}$; the conjugate-linear $L^{\star}_{\tilde A}$ has $L^{\star}_{\tilde A}(e_0)=A_0e_0$, read as its trace in the conjugate-linear convention, while as a real-linear map its matrix has real trace zero. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Traces*.)

**Read as a physical statement.** The trace of a right multiplication is conjugate-linear in the parameter and the trace of a left one is linear, the trace-level mark of the sesquilinear class; the bilinear quaternionic sibling has both traces linear, and the difference is the conjugation carried by the second slot of the product. The trace is the one scalar of the operator that is a value of the band's form on the parameter, and it vanishes whenever the parameter has no central part, so a purely vector parameter gives a traceless operator.

## The Adjoint of the Hermitian Form Conjugates the Parameter

**Theorem (the adjoint of the right multiplication).** For all $\tilde A,\tilde S\in\mathbb{B}$ the adjoint of the right multiplication with respect to $H$ is

$$
\bigl(R^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=S_0\,\tilde A ,
$$

the image of the argument's scalar part, and the map is $\mathbb{C}$-linear, as the adjoint of a linear operator must be.

*Proof.* The right multiplication is $\mathbb{C}$-linear, so the linear rule applies: $H(R^{\star}_{\tilde A}\tilde X,\tilde Y)=H(\tilde X,\tilde A)\overline{Y_0}$ and $H(\tilde X,Y_0\tilde A)=\overline{Y_0}\,H(\tilde X,\tilde A)$, the two scalars commuting; the form is non-degenerate, so the adjoint is the map displayed. (*The Sesquilinear Adjoint Operator*, §*The Adjoint of a Linear Operator*.)

**Theorem (the adjoint of the left multiplication).** For all $\tilde A,\tilde S\in\mathbb{B}$ the adjoint of the left multiplication is

$$
\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=\overline{S_0}\,\tilde A ,
$$

a **conjugate-linear** map, as the adjoint of a conjugate-linear operator must be; it is neither $L^{\star}_{\tilde A}$ nor $R^{\star}_{\tilde A}$, and it is not a multiplication of the block.

*Proof.* By the twisted rule, $H(L^{\star}_{\tilde A}\tilde R,\tilde S)=\overline{H(\tilde R,\overline{S_0}\tilde A)}$ for all $\tilde R,\tilde S$, by the conjugate symmetry of $H$ and the centrality of the value; the map $\tilde S\mapsto\overline{S_0}\tilde A$ is neither central-valued nor a multiplication of the block. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Adjoint of the Left Multiplication*.)

**Read as a physical statement.** The adjoint is taken for the Hermitian form of the band, whose symmetry is the **conjugate** symmetry; so its adjoint is an adjoint of conjugation type, and it **keeps the side** of the family: the adjoint of the linear right multiplication is again linear, the adjoint of the conjugate-linear left multiplication is again conjugate-linear, and the parity is preserved. This is the opposite of the GPA band, where the form is bilinear, the adjoint is a transpose, and the transpose of a left multiplication is a right one; there the sides swap and the type criteria are criteria on a pair. Here each side is stable under the adjoint operation, and the type criteria are criteria on the one parameter $\tilde A$ — the contrast between the conjugation adjoint and the transposition adjoint, read on a single block (*The Sesquilinear Adjoint Operator*, §*The Two Adjoints of a Conjugate-Linear Operator*).

**Theorem (the adjoint on the central parameters, and the negative answer off them).** On the central parameters the adjoint re-enters the family and reads as the coefficientwise conjugation of the parameter with the side kept,

$$
\bigl(R^{\star}_{ae_0}\bigr)^{\dagger}=R^{\star}_{\overline{a}\,e_0},\qquad a\in\mathbb{C},
$$

while off the central parameters the adjoint leaves the family altogether: although $R^{\star}_{\tilde A}$ is a multiplication of the block for every $\tilde A$, its adjoint $\tilde S\mapsto S_0\tilde A$ is a multiplication of the block exactly when $\tilde A$ is central, and only there does it re-enter the family as $R^{\star}_{\overline{a}e_0}$.

*Proof.* Self-adjointness of the adjoint formula: $H(R^{\star}_{ae_0}\tilde X,\tilde Y)=\overline{a}\,X_0\overline{Y_0}$ and $H(\tilde X,R^{\star}_{\overline{a}e_0}\tilde Y)=\overline{\overline{a}Y_0}\,X_0=aX_0\overline{Y_0}$ agree. Off the centre the map $\tilde S\mapsto S_0\tilde A$ has image the complex line $\mathbb{C}\tilde A$, which is not the centre, while every multiplication of the block is central-valued; hence the adjoint is not a multiplication. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Adjoint of the Left Multiplication*; *The Operators of the Twelve Structures*, §*The Adjoint*.)

**Read as a physical statement.** This is the price of the band's rank-one structure, and it is a **negative answer** stated as a fact. Where the parameter is a central scalar — the only place where the operation is a genuine multiplication of the block — the adjoint conjugates the scalar and keeps the side, so a real scalar gives a self-adjoint operator and an imaginary one gives a skew-adjoint operator. Where the parameter carries a vector part, the adjoint is still defined and still keeps the parity, but it is the rank-one map that multiplies the argument's scalar part by the parameter; it is no longer a multiplication of the block. The conjugate-linearity of the operator and the conjugate-linearity of the form cannot be matched by a multiplication of the row, and the failure is the operator expression of the sesquilinearity (*The Operators of the Twelve Structures*, §*The Adjoint*).

**Theorem (the adjoint of the sandwich).** For the parent sesquilinear product the two-sided operator is the **sandwich** $S_{\tilde A,\tilde B}(\tilde X)=\tilde A\tilde X^{*}\tilde B$, conjugate-linear in its argument, and its adjoint is the sandwich with the parameters exchanged,

$$
S^{\dagger}_{\tilde A,\tilde B}=S_{\tilde B,\tilde A},
$$

while the ordinary two-sided multiplication $T_{\tilde A,\tilde B}(\tilde X)=\tilde A\tilde X\tilde B$ is $\mathbb{C}$-linear and its adjoint conjugates each parameter and keeps the order, $T^{\dagger}_{\tilde A,\tilde B}=T_{\tilde A^{*},\tilde B^{*}}$.

*Proof.* By the twisted rule for the conjugate-linear sandwich and the linear rule for the two-sided multiplication, both against the pairing $H(\tilde X,\tilde Y)=\mathrm{Sc}(\tilde X\tilde Y^{*})$; the transposition of the pair for the sandwich is the trace of the involution that the sandwich already carries in its middle slot. (*The Adjoint of the Sesquilinear Sandwich*, §*The Adjoint of the Sandwich*; *The Sesquilinear Sandwich Operator*.)

**Read as a physical statement.** The two-sided operator of the parent product splits according to where the conjugation sits: the ordinary two-sided multiplication conjugates its two parameters and keeps their order, and the sandwich, which puts the involution in the middle slot, has nothing left to conjugate in the pair, so its adjoint trades the two slots. The band's own two-sided operator, $L^{\star}_{\tilde A}R^{\star}_{\tilde B}$, is a scalar multiple of a one-sided operator and its adjoint is read from the two cases above; it never is a sandwich of the parent product and never is a multiplication of the block.

### The Contrast with the Sibling Rows

The adjoint of this band is one of the adjoint operations of the twelve rows, and the comparison isolates it.

- **GPA, the plain bilinear row.** The form is $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$, the adjoint is the **transpose**, and the transpose of a left multiplication is a **right** one, $(L_{\tilde A})^{\approx}=R_{\tilde A}$: the sides **swap**, and the type criterion is a criterion on a pair of parameters.
- **GPS, the general plain sesquilinear row.** The left multiplication $L_{\tilde A}\tilde X=\tilde A\tilde X^{*}$ is conjugate-linear and its adjoint is the sandwich $S_{1,\tilde A}$, while the linear **right** multiplication obeys $R^{\dagger}_{\tilde B}=R_{\tilde B^{*}}$: on the linear family the adjoint **conjugates the parameter and keeps the side**. This is the class pattern, and it is the pattern the SPS block realizes only on its central parameters.
- **The quaternionic symmetric row, SQS.** The adjoint is $K(L^{\star}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y)}$, the natural conjugation ${\natural}$ of the parameter with the side kept, and the family is closed under the adjoint; the form is indefinite and the ranks are $0$, $4$, $6$ and $8$, not one.
- **SPS, this band.** The adjoint conjugates and keeps the side, and on the central parameters it is the coefficientwise conjugation of the parameter, $\bigl(R^{\star}_{ae_0}\bigr)^{\dagger}=R^{\star}_{\overline{a}e_0}$; off the centre it leaves the family, because the block's multiplications are rank one with central image.

**Read as a physical statement.** The class of the sesquilinear products is the class of the **conjugating, side-keeping** adjoint, and the four rows display it with four different fates. The plain bilinear row is the exception, the one whose adjoint is a transpose and swaps; the quaternionic symmetric row realizes the pattern and stays in the family; the general sesquilinear row realizes it on its linear half; and the symmetric plain sesquilinear row realizes it on the centre and loses it off the centre, the rank-one structure of the block being what prevents the multiplications from carrying the conjugating adjoint. The comparison of the twelve columns is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, and the table there records for this row exactly the words "not a multiplication".

## The Types of the Operators

**Theorem (the types of the left family).** For $\tilde A\in\mathbb{B}$,

$$
L^{\star}_{\tilde A}\ \text{self-adjoint}\iff\tilde A\in\mathbb{C}_{\mathbb{B}},\qquad L^{\star}_{\tilde A}\ \text{skew-adjoint}\iff\tilde A=0 .
$$

*Proof.* Self-adjointness is $H(\tilde A,\tilde X)\overline{Y_0}=\overline{X_0}\,H(\tilde A,\tilde Y)$ for all $\tilde X,\tilde Y$ by the twisted rule; at $\tilde Y=e_0$ this reads $H(\tilde A,\tilde X)=A_0\overline{X_0}$ for all $\tilde X$, so $\tilde A=A_0e_0$ is central, and then the identity holds for every complex $A_0$. Skew-adjointness gives $H(\tilde A,\tilde X)=-A_0\overline{X_0}$ for all $\tilde X$, so $\tilde A$ is central with $A_0=0$, that is $\tilde A=0$. (*The Sesquilinear Adjoint Operator*, §*The Twisted Rule*.)

**Theorem (the types of the right family).** For $\tilde A\in\mathbb{B}$,

$$
R^{\star}_{\tilde A}\ \text{self-adjoint}\iff\tilde A\in\mathbb{R}_{\mathbb{B}},\qquad R^{\star}_{\tilde A}\ \text{skew-adjoint}\iff\tilde A\in i\mathbb{R}_{\mathbb{B}},
$$

where $\mathbb{R}_{\mathbb{B}}=\mathbb{R}e_0$ and $i\mathbb{R}_{\mathbb{B}}=i\mathbb{R}e_0$.

*Proof.* Self-adjointness is $H(\tilde X,\tilde A)\overline{Y_0}=\overline{X_0}\,H(\tilde Y,\tilde A)$ for all $\tilde X,\tilde Y$ by the linear rule; at $\tilde Y=e_0$ this reads $\overline{A_0}\,X_0=A_0X_0$ for all $\tilde X$, so $\tilde A=A_0e_0$ is central with $A_0$ real, and then the identity holds. Skew-adjointness reads $\overline{A_0}X_0=-A_0X_0$ at $\tilde Y=e_0$, so $A_0=-\overline{A_0}$ is purely imaginary. (*The Sesquilinear Adjoint Operator*, §*The Adjoint of a Linear Operator*.)

| family | self-adjoint | skew-adjoint |
|---|---|---|
| $L^{\star}_{\tilde A}$ | $\tilde A\in\mathbb{C}_{\mathbb{B}}$ | $\tilde A=0$ |
| $R^{\star}_{\tilde A}$ | $\tilde A\in\mathbb{R}_{\mathbb{B}}$ | $\tilde A\in i\mathbb{R}_{\mathbb{B}}$ |

**Read as a physical statement.** The self-adjoint operators are the **observables**, and this band, with GPS, owns the physical adjoint: its adjoint is the Hermitian adjoint for the positive form of the band, whose fixed points are the observables and whose skew fixed points are the generators. Two features distinguish the band's observables from the GPS ones. First, the self-adjointness of a one-sided operator is a criterion on the parameter and not a consequence of the parameter lying in a sector: the criterion is **centrality**, not Hermiticity, so a Hermitian but non-central parameter such as $e_0+ie_1$ gives a right multiplication that is **not** self-adjoint, in contrast with the GPS row, where every Hermitian parameter gives a self-adjoint left multiplication. Second, the reality of the parameter is a **condition** and not an automatic consequence for the left family: a self-adjoint *right* operator has an automatically real central parameter, while a self-adjoint *left* operator may have any complex central parameter, because a conjugate-linear operator can be self-adjoint with a complex multiple of itself. The observables of the band are therefore the real multiples of the projection $\tilde X\mapsto X_0e_0$ onto the central scalar part — the operators that read the probability off a state — together with the complex multiples of its conjugate for the left family.

## The Symmetries of the Form and of the Product

The symmetries of the band are three questions and they are taken in turn: which operators preserve the **form**, which preserve the **product**, and which preserve the **cone** of the operation.

### The Form-Preserving Operators

**Theorem (the form-preserving operators).** The group $G_H$ of $\mathbb{C}$-linear bijections of $\mathbb{B}$ preserving $H$ has the matrix condition $T^{\mathsf H}T=I_4$ in the basis $e_0,e_1,e_2,e_3$; its Lie algebra is the space of the $\mathbb{C}$-linear endomorphisms $X$ with $X^{\mathsf H}+X=0$, the skew endomorphisms. **No** nonzero one-sided multiplication of the block preserves $H$.

*Proof.* Preservation is $H(T\tilde P,T\tilde Q)=H(\tilde P,\tilde Q)$ for all $\tilde P,\tilde Q$, which in the basis is $T^{\mathsf H}T=I_4$; the Lie algebra is read by the dual-number computation $S=I+\varepsilon X$. A one-sided multiplication is rank one, and a form-preserving map is invertible, so no nonzero one-sided multiplication preserves the definite form $H$. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Group of Linear Maps Preserving the Form*.)

### The Multiplicative Operators

**Theorem (the multiplicative operators).** A $\mathbb{C}$-linear bijection $T$ is an automorphism of the product, $T(\tilde P\star\tilde Q)=T\tilde P\star T\tilde Q$, if and only if it preserves $H$ and fixes the idempotent $e_0$:

$$
\operatorname{Aut}(\star)=\{\,T\in G_H:Te_0=e_0\,\}.
$$

No operator of the block is multiplicative: the two-sided operators $L^{\star}_{\tilde A}R^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$ and $R^{\star}_{\tilde A}L^{\star}_{\tilde B}=\overline{A_0}L^{\star}_{\tilde B}$ are rank one and therefore not invertible, while a multiplicative bijection is invertible by definition. The multiplicative operators are the external elements of $G_H$ fixing $e_0$, the unitary group of the complement of the central line.

*Proof.* If $T\in G_H$ with $Te_0=e_0$ then $T(\tilde P\star\tilde Q)=H(\tilde P,\tilde Q)e_0=T\tilde P\star T\tilde Q$, so $T$ is multiplicative; conversely a multiplicative $T$ has $Te_0=c_0e_0$ with $c_0=\lvert c_0\rvert^{2}$, so $c_0\in\{0,1\}$ and invertibility forces $c_0=1$, whence $T\in G_H$ and $Te_0=e_0$. A two-sided operator of the block is a scalar multiple of a rank-one one-sided operator, so it is not invertible and not multiplicative. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Group of Linear Maps Preserving the Form, and Its Lie Algebra*.)

### The Cone of the Operation

**Theorem (the cone of the operation and its preservers).** The cone of the operation, the set of the diagonal values $\tilde Q\star\tilde Q$ of the block, is the closed positive central ray $\mathbb{R}_{\ge0}e_0$, and a one-sided multiplication of the block maps that ray into itself if and only if the scalar part of its parameter is real and non-negative:

$$
L^{\star}_{\tilde A}(\mathbb{R}_{\ge0}e_0)\subseteq\mathbb{R}_{\ge0}e_0\iff A_0\in\mathbb{R}_{\ge0},\qquad R^{\star}_{\tilde A}\ \text{likewise}\iff A_0\in\mathbb{R}_{\ge0}.
$$

*Proof.* $L^{\star}_{\tilde A}(te_0)=tA_0e_0$ and $R^{\star}_{\tilde A}(te_0)=t\overline{A_0}e_0$ for $t\ge0$, so the image lies in the ray exactly when $A_0$ is real and non-negative. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*; the cone of the operation is the sibling *Why Probability Values Are Central*.)

**Read as a physical statement.** The symmetries of the band are two different things and neither is an operator of the block. The symmetry of the **form** is the unitary group $G_H$ of the coefficient space, the isometries of the positive form $H$; the symmetry of the **product** is the subgroup fixing the identity, the unitaries of the complement of the central line; and the two-sided operators of the block preserve neither, because they are rank one. The physical positivity of the band is carried by the **cone of the operation**, the positive central ray of probability values, and the operators of the block that keep the ray inside itself are exactly those whose parameter has a non-negative real scalar part — a condition on the parameter and not on the operator's rank. This is the operator-level form of the statement that the operation is probability read as a product: its values are non-negative real numbers, its preservers are the parameters with a non-negative real part, and the identity of the dagger and the Hermitian cone which give the positivity its involution belong to the sibling articles and to the mathematics of the positive cone (*The Positive Cone of an Involutive Algebra*; *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*).

## The Operators Acting on the State Space

The state space of the band is the **informational sector** $\mathbb{M}_+$, taken on its trace-one slice — the positive Hermitian elements $\tilde\varrho$ with $\mathrm{Tr}(\tilde\varrho)=1$, that is $\mathrm{Sc}(\tilde\varrho)=\tfrac12$, the Bloch ball — and the form $H$ is the band's Born pairing on it, one half of the trace pairing on that side (*The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; the two siblings own the state interpretation and the cone).

**Proposition (the action collapses to the centre).** For every parameter $\tilde A$ and every state $\tilde\varrho$,

$$
L^{\star}_{\tilde A}\tilde\varrho=H(\tilde A,\tilde\varrho)e_0,\qquad R^{\star}_{\tilde A}\tilde\varrho=H(\tilde\varrho,\tilde A)e_0 ,
$$

central values whose two interpretations are conjugate. The operators therefore do not move the state space: they evaluate the Born pairing and place its value in the centre. The self-adjoint right observables $\tilde A=ae_0$, $a\in\mathbb{R}$, act as $\tilde\varrho\mapsto a\,\varrho_0e_0$, reading the scalar part of the state.

*Proof.* The definitions give the values, and the centrality, conjugate relation and rank-one statements of the preceding sections give the rest; on the trace-one slice $\mathrm{Sc}(\tilde\varrho)=\tfrac12$ and the observable $R^{\star}_{ae_0}$ returns $\tfrac{a}{2}e_0$. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*; *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*.)

**Read as a physical statement.** The operators of the band are the **measurement functionals** of the state space, not its transformations. A multiplication reads the Born pairing of a parameter with a state and returns a probability value in the centre; it carries no direction, so it never maps a state to a state, and the composite of two such interpretations is a scalar multiple of an interpretation. The self-adjoint ones are exactly the real multiples of the trace functional, the observables that return a real number; the positivity of the diagonal $H(\tilde\varrho,\tilde\varrho)=\sum_\mu\lvert\varrho_\mu\rvert^{2}$ and the reality of the pairing $H(\tilde\varrho,\tilde\sigma)=\overline{H(\tilde\sigma,\tilde\varrho)}$ are the sibling statements that make the returned number a probability. With the GPS band the state side of the framework is owned here, and the operator content is that a multiplication of the band is a **question asked of a state**, whose answer is a central number, and never a motion of the state.

### The Born Pairing through the Operators

The pairing of two states is a value of the form and the multiplication reads it:

$$
H(\tilde\varrho,\tilde\sigma)=\tfrac12\operatorname{Tr}\bigl(\tilde\varrho\star\tilde\sigma\bigr),\qquad R^{\star}_{\tilde\varrho}\tilde\sigma=H(\tilde\varrho,\tilde\sigma)e_0 ,
$$

so multiplication by one state on another returns the Born pairing as a central value; on two pure states $\tilde\Pi_\mu=\tfrac12(e_0+i\boldsymbol\mu\!\cdot\!\mathbf e)$ and $\tilde\Pi_\nu$ this is $H(\tilde\Pi_\mu,\tilde\Pi_\nu)=\tfrac14(1+\boldsymbol\mu\!\cdot\!\boldsymbol\nu)$, the trace form of the two-by-two state.

**Read as a physical statement.** The probability of a measurement is the Born pairing written as a rank-one operator: the parameter is the tested state, the argument is the prepared state, and the answer is the central number. The conjugation in the second slot is why the pairing is conjugate-symmetric, so the answer given on the left and the answer given on the right are conjugates, and on the state side the two coincide and are real, which is what makes the returned number a probability. The form is positive definite, so no state has a vanishing self-pairing, and the operators of the band never return a negative probability.

**Proposition (the kernel on the state space).** For $\tilde A\neq0$ the kernel of $L^{\star}_{\tilde A}$ meets the state space in the states orthogonal to the parameter,

$$
\ker L^{\star}_{\tilde A}\cap\{\text{states}\}=\{\tilde\varrho:H(\tilde A,\tilde\varrho)=0\},
$$

the hyperplane section of the Bloch ball by the plane perpendicular to $\tilde A$; the operator returns the value zero exactly on that section.

*Proof.* Immediate from the kernel statement of the operator, and the state space is the trace-one slice of $\mathbb{M}_+$. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.)

**Read as a physical statement.** A vanishing probability is the orthogonality of the prepared state to the tested parameter, and the level sets of an interpretation are the planes of the Bloch ball perpendicular to the parameter. The rank-one family of the band therefore separates the state space by orthogonality: two parameters with the same ray give the same kernel, and the operator sees the ray of the parameter and its scalar, not the parameter itself.

## The Sandwich and the Inner Automorphism

The sandwich of the parent sesquilinear product is the two-sided operator $S_{\tilde A,\tilde B}(\tilde X)=\tilde A\tilde X^{*}\tilde B$, and the block's own two-sided operator is $L^{\star}_{\tilde A}R^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$, a scalar multiple of a one-sided one. The two are compared here because the model's sandwich against the inner automorphism has its analogue in the two-sided operators.

**Theorem (the block's two-sided operators are never automorphisms).** For all $\tilde A,\tilde B$,

$$
L^{\star}_{\tilde A}R^{\star}_{\tilde B}=A_0\,L^{\star}_{\tilde B},\qquad R^{\star}_{\tilde A}L^{\star}_{\tilde B}=\overline{A_0}\,L^{\star}_{\tilde B},\qquad L^{\star}_{\tilde A}R^{\star}_{\tilde A}=A_0\,L^{\star}_{\tilde A},
$$

so every two-sided operator of the block is rank one and no two-sided operator of the block is a multiplication of the block or an automorphism of its product.

*Proof.* Read the composition laws with the order of the two factors as displayed; the diagonal two-sided operator $L^{\star}_{\tilde Q}R^{\star}_{\tilde Q}=Q_0L^{\star}_{\tilde Q}$ is rank one. An automorphism is invertible, and a rank-one operator is not. (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, §*The Composition and the Failure of Multiplicativity*; the automorphisms are the elements of $G_H$ fixing $e_0$.)

**Read as a physical statement.** The GPA sandwich is the inner automorphism and coincides with it on the unitary parameters; the SPS block has no such object. Its sandwich degenerates to a scalar multiple of a one-sided operator, and the automorphisms of its product are **external** unitaries fixing the identity — not multiplications by elements of the block at all. The inversion is therefore a statement about the block: the associative row acts on itself by its own elements, and this central-valued row cannot, because its multiplications are rank one, and its symmetries have to be brought in from outside the block. This is the deepest difference between the composition band and the positivity band on the operator side.

### The Parent Sandwich on a State

On a state $\tilde\varrho$, which is Hermitian, the parent sandwich is $\tilde A\tilde\varrho^{*}\tilde B=\tilde A\tilde\varrho\tilde B$, and on the identity it gives $S_{\tilde A,\tilde B^{*}}(e_0)=\tilde A\tilde B^{*}$, whose scalar part is the band's value:

$$
S_{\tilde A,\tilde B^{*}}(e_0)=\tilde A\tilde B^{*},\qquad \mathrm{Sc}\bigl(\tilde A\tilde B^{*}\bigr)e_0=\tilde A\star\tilde B .
$$

*Proof.* $\tilde B^{**}=\tilde B$ and $e_0^{*}=e_0$, so $S_{\tilde A,\tilde B^{*}}(e_0)=\tilde A e_0^{*}\tilde B^{*}=\tilde A\tilde B^{*}$, and its scalar part is $H(\tilde A,\tilde B)$, the value of the product. (*The Sesquilinear Sandwich Operator*; *The Multiplication Operators of the Symmetric Plain Sesqualgebra*.)

**Read as a physical statement.** The band's product is the **central shadow** of the parent sandwich: where the parent two-sided operator returns an element, the band returns the scalar part of that element, because the band keeps only the probability and discards the rest. The adjoint of the parent sandwich transposes the two parameters, and the band's value — the scalar part of the sandwich on the identity — inherits the conjugate symmetry $H(\tilde B,\tilde A)=\overline{H(\tilde A,\tilde B)}$, so the band's operator theory is the parent theory projected onto the centre.

## A Worked Case

Take a material parameter and a state parameter, and read the four operator families on one element.

$$
\tilde A=ie_0+2e_1,\qquad H(\tilde A,\tilde A)=5,\qquad \tilde A\star\tilde A=5e_0,\qquad \tilde A^{2}=-5e_0+4ie_1 .
$$

On the identity the two one-sided operators give

$$
L^{\star}_{\tilde A}e_0=H(\tilde A,e_0)e_0=ie_0,\qquad R^{\star}_{\tilde A}e_0=H(e_0,\tilde A)e_0=-ie_0 ,
$$

the two conjugates, and their adjoints give

$$
\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}e_0=\overline{(e_0)_0}\,\tilde A=\tilde A,\qquad \bigl(R^{\star}_{\tilde A}\bigr)^{\dagger}e_0=(e_0)_0\,\tilde A=\tilde A ,
$$

the parameter itself, on the line $\mathbb{C}\tilde A$ and not in the centre: the parameter is not central, so neither operator is self-adjoint, and the adjoints are not multiplications of the block.

Take next a **Hermitian but non-central** parameter and a **real central** one:

$$
\tilde\Lambda=e_0+ie_1\in\mathbb{M}_+,\qquad \tilde A'=\tfrac12 e_0 .
$$

The right multiplication by $\tilde\Lambda$ is **not** self-adjoint, although $\tilde\Lambda$ lies in the Hermitian sector, while the right multiplication by the real central $\tilde A'$ **is** self-adjoint, with

$$
R^{\star}_{\tilde A'}\tilde\varrho=\tfrac12\varrho_0e_0
$$

on a state $\tilde\varrho$. This is the criterion on the parameter and not on the sector: centrality for the left family, real centrality for the right.

Take a second parameter $\tilde B=e_0+e_2$ and read a **composition** and the **parent sandwich** on the worked element:

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}=i\,R^{\star}_{\tilde B},\qquad A_0=i,\qquad S_{\tilde A,\tilde B^{*}}(e_0)=\tilde A\tilde B^{*}=ie_0+2e_1-ie_2-2e_3 ,
$$

whose scalar part $\mathrm{Sc}(\tilde A\tilde B^{*})=i$ is the band's value $H(\tilde A,\tilde B)=i$. The composite of the two readings is the reading by $\tilde B$ scaled by the modulus-one scalar $i$, and the parent sandwich returns an element whose scalar part is that value; the band keeps the scalar part and discards the vector part $2e_1-ie_2-2e_3$.

Take finally two **pure states** and read the Born pairing through the operators:

$$
\tilde\Pi_\mu=\tfrac12(e_0+i\boldsymbol\mu\!\cdot\!\mathbf e),\qquad
H(\tilde\Pi_\mu,\tilde\Pi_\nu)=\tfrac14(1+\boldsymbol\mu\!\cdot\!\boldsymbol\nu),\qquad
2\,H(\tilde\Pi_\mu,\tilde\Pi_\nu)=\cos^{2}\!\tfrac{\theta}{2},
$$

where $\theta$ is the Bloch angle between $\boldsymbol\mu$ and $\boldsymbol\nu$. The product $\tilde\Pi_\mu\star\tilde\Pi_\nu=H(\tilde\Pi_\mu,\tilde\Pi_\nu)e_0$ is the central real number, its real part is the transition probability, and the multiplication $R^{\star}_{\tilde\Pi_\mu}$ reads it off the state $\tilde\Pi_\nu$.

**A numerical check.** For random elements the identity $\tilde P\star\tilde Q=H(\tilde P,\tilde Q)e_0$ holds to machine precision on one hundred pairs (maximum error $0$). The conjugate relation $R^{\star}_{\tilde A}=\overline{L^{\star}_{\tilde A}}$ and the parity $L^{\star}_{\tilde A}(\lambda\tilde R)=\overline{\lambda}L^{\star}_{\tilde A}\tilde R$, $R^{\star}_{\tilde A}(\lambda\tilde R)=\lambda R^{\star}_{\tilde A}\tilde R$ hold to $8.0\times10^{-16}$ on one hundred random pairs; the four composition laws hold exactly (error $0$); the two adjoint formulas hold to $8.0\times10^{-16}$ and $5.0\times10^{-16}$; the sandwich adjoint $S^{\dagger}_{\tilde A,\tilde B}=S_{\tilde B,\tilde A}$ holds to $2.2\times10^{-15}$ while $T^{\dagger}_{\tilde A,\tilde B}=T_{\tilde A^{*},\tilde B^{*}}$ holds to $2.8\times10^{-15}$. The type criteria were checked on the parameters $e_0$, $e_1$, $e_3$, $ie_0$, $ie_1$, $\tfrac12e_0$, $2e_0$, $e_0+ie_1$, $e_1+ie_2$ and $ie_0+2e_1$: the left family is self-adjoint exactly for $e_0$, $ie_0$, $\tfrac12e_0$ and $2e_0$ (the central ones) and skew-adjoint for none of them except the zero parameter, and the right family is self-adjoint exactly for $e_0$, $\tfrac12e_0$, $2e_0$ (real central) and skew-adjoint exactly for $ie_0$ (imaginary central). The cone criterion $A_0\in\mathbb{R}_{\ge0}$ was checked on the scalar parameters: $e_0$, $2e_0$ and a zero-scalar vector parameter preserve the ray, while $ie_0$ and $-\tfrac12e_0$ do not. The right multiplication by the Hermitian non-central $e_0+ie_1$ fails self-adjointness on every probe tested, and the real rank of $L^{\star}_{e_1+e_2}$ is $2$, the rank recorded for the SPS row of the crossing article. The Born identity $2H(\tilde\Pi_\mu,\tilde\Pi_\nu)=\cos^{2}(\theta/2)$ was checked on four Bloch vectors and their six pairs.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must declare. Several of the statements are another article's, and they are cited rather than re-derived.

- **The positivity of the product and the cone.** The positivity of the diagonal, the interpretation of $H$ as the real part of the Born pairing, the reality of the pairing and the one-dimensional cone of the operation are *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* and *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*. This article states the operator-level preservers of the cone and not the cone itself.
- **The positivity of the dagger.** The involution and the Hermitian cone $\{\tilde Q\tilde Q^{*}\}$, the polar decomposition and the Cartan involution are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, *The Positive Cone of an Involutive Algebra* and *Positivity and the Positive Cone of a Hermitian Form*, and the physics of the positivity is *Mass, Rank and the Positivity of the Dagger*; the present band's job word names that positivity, which belongs to those articles and not here.
- **The rank, the traces and the composition laws.** They are *The Multiplication Operators of the Symmetric Plain Sesqualgebra* and are applied, not re-proved; the present article adds the adjoint of the right multiplication, the type criteria, the central-parameter conjugation law and the cone criterion.
- **The adjoint of the sandwich and the twisted rule.** They are *The Adjoint of the Sesquilinear Sandwich* and *The Sesquilinear Adjoint Operator*; the whole class is treated there against the pairing $H(x,y)=\mathrm{Sc}(xy^{*})$.
- **The bilinear contrast.** The symmetric quaternionic sibling *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* is invoked only for the difference of the parity and the traces; the two symmetric sesquilinear products are compared in the crossing article.
- **The twelve rows.** The comparison, block against block, is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this article declares only the SPS column.
- **The bracket and the generators.** The band has no bracket and no generator of its own: the antisymmetric plain sesquilinear row APS owns the bracket of the plain sesquilinear family, and the generators of the framework are the skew-adjoint operators for the positive form, read in *Observables, Gauge Generators and the Chirality of the Internal Action*, not here.
- **The exponential and the group.** The block carries no one-parameter group: the left family has no nonzero skew-adjoint element and the right family only the purely imaginary central ones, whose exponentials are central phases; the unitaries and the internal rotations are the external elements of $G_H$ and are cited, not generated here.
- **The order and the transition probability.** The order of the observables by their real parameter and the transition probability of two pure states are read here at the operator level; the physical transition probability, its comparison with the trace formula and its use in the update are the siblings and *The Born Rule as a Trace Formula — Derivation and Comparison*.

**What the framework does not claim.** The article does not derive the measurement rule, the state space or the Born pairing from the operator calculus; it reads the parametrisations the siblings already use. It does not claim that a self-adjoint operator of the block is a self-adjoint operator in the sense of the ordinary linear theory: the left family is conjugate-linear and its self-adjoint elements form a **complex** vector space, a feature of the twisted rule and not a physical statement about observables in general. It does not claim that the external unitaries fixing $e_0$ act on the state space; they are the automorphisms of the product, not multiplications by elements of the block. And it does not claim that the block generates anything: the rank-one family carries no generator and no one-parameter group, and the infinitesimal structure of the framework belongs to the antisymmetric band.

## The Ledger

**Proved.** The one-sided operators $L^{\star}_{\tilde A}\tilde R=H(\tilde A,\tilde R)e_0$ and $R^{\star}_{\tilde A}\tilde R=H(\tilde R,\tilde A)e_0$ are conjugate-linear and $\mathbb{C}$-linear respectively, they are pointwise conjugates, and each is rank one with image the centre and kernel the hyperplane $H(\tilde A,\cdot\,)=0$; the composition laws are $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=A_0R^{\star}_{\tilde B}$, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=\overline{A_0}R^{\star}_{\tilde B}$, $L^{\star}_{\tilde A}R^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$ and $R^{\star}_{\tilde A}L^{\star}_{\tilde B}=\overline{A_0}L^{\star}_{\tilde B}$, so the family is closed and the assignment is not multiplicative; the adjoint for the Hermitian form $H$ is $\bigl(R^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=S_0\tilde A$ on the right and $\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=\overline{S_0}\tilde A$ on the left, both of parity preserved and side kept, and on the central parameters it is the conjugation of the parameter, $\bigl(R^{\star}_{ae_0}\bigr)^{\dagger}=R^{\star}_{\overline{a}e_0}$; off the central parameters the adjoint leaves the family, which is the negative answer of the block; the type criteria are $\tilde A$ central for the self-adjoint left family and only the zero parameter for its skew sector, and $\tilde A$ real central for the self-adjoint right family and $\tilde A$ purely imaginary central for its skew sector, so the observables are the operators that read the central scalar part and the parameter type is a condition rather than a consequence; no nonzero one-sided operator preserves $H$, the form-preserving group is $G_H$ with $T^{\mathsf H}T=I_4$, the multiplicative operators are the elements of $G_H$ fixing $e_0$, and the two-sided operators of the block are rank one and never automorphisms; the cone of the operation is the positive central ray and a one-sided multiplication preserves it exactly for a parameter with a non-negative real scalar part; the sandwich of the parent product has adjoint $S^{\dagger}_{\tilde A,\tilde B}=S_{\tilde B,\tilde A}$ and the ordinary two-sided multiplication has adjoint $T^{\dagger}_{\tilde A,\tilde B}=T_{\tilde A^{*},\tilde B^{*}}$; and on the state space every multiplication evaluates the Born pairing and returns a central value.

**Interpretations.** That the adjoint of this band is the **physical** adjoint — the Hermitian adjoint for the positive form — and not a transpose, and that it keeps the side because the form's symmetry is conjugation; that its fixed points, the observables, are the real multiples of the projection onto the central scalar part, so an observable here reads a probability and does not transform a state; that the type criterion is a criterion on the single parameter — centrality for the left family, real centrality for the right — in contrast with the GPA row whose criterion is a criterion on the product of two parameters because its adjoint swaps the sides; that the block has no invertible operator, so it acts by questions and not by motions, and its symmetries are external unitaries; and that the cone of the operation, the positive central ray, is preserved exactly by the parameters with a non-negative real scalar part, the operator-level form of the positivity of the band. Each is the framework's naming of a proved algebraic fact and is labelled as such.

## Physical Readings

The operators of the symmetric plain sesquilinear product read as the **interpretations of probability**: the two ways of asking a parameter of a state, and the central number that answers. Under the band's job word, positivity, four interpretations follow from the adjoint, and a fifth from the rank of the family.

- **The real part of the Born pairing.** The product returns the Hermitian form $H$ of the pair, and the multiplication $R^{\star}_{\tilde A}$ returns it as a central value; on the state side that value is one half of the trace pairing, $\tfrac12\operatorname{Tr}(\tilde\varrho\tilde\sigma)$, and it is the central half of the parent amplitude $\tilde\varrho\tilde\sigma^{*}$, whose vector half is the phase of the companion band. The operator is therefore the **value** of the pairing, and the reading of the pairing as a probability is the operator's central value.
- **The positivity of the diagonal.** $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}\ge0$, with equality only at zero; the operator $L^{\star}_{\tilde Q}$ therefore returns a non-negative number on the state $\tilde Q$, and the band's positivity is the positivity of the diagonal of the form, the sibling result that makes the returned number a probability and not a mere scalar.
- **The order of the observables.** The self-adjoint operators are the real multiples of the central projection, and they are ordered by their real parameter: the greater the real multiple, the greater the value returned on every state, because the projection is positive. The order of the observables of the band is therefore the order of the real numbers, which is the sharpest form of the statement that the band reads probabilities and nothing else.
- **Why the symmetry of the product makes the pairing real.** On the state side both elements are Hermitian, and there the operation is the whole of the plain product, $\tilde P\star\tilde Q=\mathrm{Sc}(\tilde P\tilde Q)e_0=H(\tilde P,\tilde Q)e_0$ for $\tilde P,\tilde Q\in\mathbb{M}_+$, whose scalar part is commutative, $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=\mathrm{Sc}(\tilde Q\tilde P)=H(\tilde Q,\tilde P)$. Combined with the conjugate symmetry $H(\tilde Q,\tilde P)=\overline{H(\tilde P,\tilde Q)}$ this forces $H(\tilde P,\tilde Q)=\overline{H(\tilde P,\tilde Q)}$, a **real** number. The symmetry of the product on the state side is exactly what makes the pairing real there, and that is why the operators of the band return real observables: the symmetry of the product and the reality of the pairing on the state side are the same fact read on the values and on the operators.
- **The absence of a motion.** The rank-one operators never carry a state to a state, so the operator calculus of the band is a calculus of **questions** and not of motions: no observable and no generator of the band moves a state, and the transformation of a state in the framework is the sandwich of the parent block and not a multiplication of this band. This is the operator content of the separation between the positivity band and the composition band, and the reason the two bands own different halves of the one action form.

Read on the state space, the two families are the two interpretations of a single question, conjugate to one another; read on the parameter, the adjoint is the conjugation that returns the parameter and keeps its side; read on the cone, the operators that preserve the ray of probabilities are the parameters with a non-negative real part; and read on the rank, the block asks and never moves. The positivity of the band is the whole content of the block, and the block says it with rank-one operators and no motion.

## Summary

The operators of the symmetric plain sesquilinear product, $\tilde P\star\tilde Q=\tfrac12(\tilde P\tilde Q^{*}+(\tilde P\tilde Q^{*})^{\natural})=H(\tilde P,\tilde Q)e_0$, are $L^{\star}_{\tilde A}\tilde R=H(\tilde A,\tilde R)e_0$ and $R^{\star}_{\tilde A}\tilde R=H(\tilde R,\tilde A)e_0$. The **left** family is conjugate-linear and the **right** family is $\mathbb{C}$-linear, and they are pointwise conjugates; every nonzero operator has **rank one**, image the centre and kernel the hyperplane $H(\tilde A,\cdot\,)=0$. The **composition** laws are $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=A_0R^{\star}_{\tilde B}$, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=\overline{A_0}R^{\star}_{\tilde B}$, $L^{\star}_{\tilde A}R^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$ and $R^{\star}_{\tilde A}L^{\star}_{\tilde B}=\overline{A_0}L^{\star}_{\tilde B}$, so the family is closed and the assignment is **not multiplicative**.

The **adjoint** is taken for the Hermitian form $H$, and it is $\bigl(R^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=S_0\tilde A$ on the right and $\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=\overline{S_0}\tilde A$ on the left: it **conjugates** the parameter and **keeps the side**, preserving the parity, against the GPA band whose transpose swaps the two sides. On the central parameters it is the conjugation of the parameter, $\bigl(R^{\star}_{ae_0}\bigr)^{\dagger}=R^{\star}_{\overline{a}e_0}$; off them it leaves the family, which is the block's negative answer. The **type criteria** are criteria on the single parameter: $L^{\star}_{\tilde A}$ is self-adjoint exactly for central $\tilde A$ and skew-adjoint only at zero, and $R^{\star}_{\tilde A}$ is self-adjoint exactly for real central $\tilde A$ and skew-adjoint exactly for purely imaginary central $\tilde A$. The self-adjoint operators are the **observables**, and with the GPS band this band owns the physical adjoint; a self-adjoint right operator has an automatically real parameter, while a self-adjoint left operator may have a complex one, so the parameter type is a condition and not a consequence.

The **symmetries** are external: no nonzero one-sided operator preserves $H$, the form-preserving group is $G_H$ with $T^{\mathsf H}T=I_4$, and the multiplicative operators are the elements of $G_H$ fixing $e_0$; every two-sided operator of the block is rank one and never an automorphism. The **cone** of the operation is the positive central ray, preserved exactly by the parameters with a non-negative real scalar part. The **sandwich** of the parent product has adjoint $S^{\dagger}_{\tilde A,\tilde B}=S_{\tilde B,\tilde A}$ and the ordinary two-sided multiplication has adjoint $T^{\dagger}_{\tilde A,\tilde B}=T_{\tilde A^{*},\tilde B^{*}}$. On the **state space** every multiplication evaluates the Born pairing and returns a central value, so the operators are questions asked of a state and not motions of it. The band's **positivity** is the positivity of the diagonal of $H$, the reality of the pairing on the state side forced by the commutativity of the product there, and the order of the observables by their real parameters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=H(\tilde P,\tilde Q)e_0$ | the symmetric plain sesquilinear product |
| $H(\tilde P,\tilde Q)=\sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form of the band; positive definite |
| $L^{\star}_{\tilde A}\tilde R=H(\tilde A,\tilde R)e_0$ | the left multiplication; conjugate-linear |
| $R^{\star}_{\tilde A}\tilde R=H(\tilde R,\tilde A)e_0$ | the right multiplication; $\mathbb{C}$-linear |
| $R^{\star}_{\tilde A}=\overline{L^{\star}_{\tilde A}}$ | the two families are pointwise conjugate |
| $\mathbb{C}_{\mathbb{B}}$, $\{H(\tilde A,\cdot\,)=0\}$ | the image and the kernel of a nonzero operator; rank one |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=A_0R^{\star}_{\tilde B}$, etc. | the four composition laws |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B}\neq L^{\star}_{\tilde A\star\tilde B}$ | the failure of multiplicativity |
| $\bigl(R^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=S_0\tilde A$ | the adjoint of the right multiplication; linear |
| $\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S=\overline{S_0}\tilde A$ | the adjoint of the left multiplication; conjugate-linear |
| $\bigl(R^{\star}_{ae_0}\bigr)^{\dagger}=R^{\star}_{\overline{a}e_0}$ | the adjoint on the central parameters; conjugates, keeps the side |
| $L^{\star}_{\tilde A}$ self-adjoint $\iff$ $\tilde A\in\mathbb{C}_{\mathbb{B}}$ | the type criterion of the left family |
| $R^{\star}_{\tilde A}$ self-adjoint $\iff$ $\tilde A\in\mathbb{R}_{\mathbb{B}}$ | the type criterion of the right family; the observables |
| $G_H$, $T^{\mathsf H}T=I_4$ | the form-preserving group; no one-sided operator is in it |
| $\operatorname{Aut}(\star)=\{T\in G_H:Te_0=e_0\}$ | the multiplicative operators; external unitaries |
| $\mathbb{R}_{\ge0}e_0$ | the cone of the operation; preserved iff $A_0\in\mathbb{R}_{\ge0}$ |
| $S^{\dagger}_{\tilde A,\tilde B}=S_{\tilde B,\tilde A}$ | the adjoint of the sesquilinear sandwich; transposes the pair |
| $T^{\dagger}_{\tilde A,\tilde B}=T_{\tilde A^{*},\tilde B^{*}}$ | the adjoint of the two-sided multiplication; conjugates, keeps the order |

## Further Reading

- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the operators, the parity, the rank, the traces, the adjoint of the left multiplication, the composition laws and the group preserving the form.
- *The Sesquilinear Adjoint Operator* (`articles_maths/the-sesquilinear-adjoint-operator.md`), for the pairing, the two parities, the parity obstruction and the twisted rule.
- *The Adjoint of the Sesquilinear Sandwich* (`articles_maths/the-adjoint-of-the-sesquilinear-sandwich.md`), for the adjoint of the sandwich and its contrast with the linear family.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the bilinear central sibling and the difference of the traces.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`) and *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product and the form.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), *The Positive Cone of an Involutive Algebra* (`articles_maths/the-positive-cone-of-an-involutive-algebra.md`) and *Positivity and the Positive Cone of a Hermitian Form* (`articles_maths/positivity-and-the-positive-cone-of-a-hermitian-form.md`), for the positivity of the dagger and the cone; the physics of the positivity is *Mass, Rank and the Positivity of the Dagger* (`articles_physics/mass-rank-and-the-positivity-of-the-dagger.md`).
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`) and *The Bloch Ball as the Trace-One Slice of the Future Light Cone* (`articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.md`), for the state space and its trace-one slice.
- *The Born Rule as a Trace Formula — Derivation and Comparison* (`articles_physics/the-born-rule-as-a-trace-formula-derivation-and-comparison.md`), for the Born pairing that the operators read.
- The siblings of the band: *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* (`articles_physics/the-hermitian-form-as-a-product-positivity-and-the-real-part-of-the-born-pairing.md`) and *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone* (`articles_physics/why-probability-values-are-central-the-symmetric-sesquilinear-product-and-its-cone.md`).
- *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), for the comparison of the twelve rows, of which this article is the SPS column.
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the conjugations, the basis and the form.
