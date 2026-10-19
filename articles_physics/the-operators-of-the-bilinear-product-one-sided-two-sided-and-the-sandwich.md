# __The Operators of the Bilinear Product: One-Sided, Two-Sided and the Sandwich__

## Introduction

This article is the operator article of the general plain algebra, the algebra of *The Products, Their Forms and Their Norms*. Its product is the general plain bilinear product $\tilde Q_3\tilde Q_4$, and the operators of the block are the maps
that attach an element to an argument:

$$
L_{\tilde Q}(\tilde Q_5)=\tilde Q\tilde Q_5,\qquad
R_{\tilde Q}(\tilde Q_5)=\tilde Q_5\tilde Q,\qquad
\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}} .
$$

The left and the right multiplication are the two one-sided operators, their products $L_{\tilde Q_7}R_{\tilde Q_1}$ are
the two-sided ones, and the **sandwich** is the algebraic norm two-sided operator in which the right parameter is the
conjugate of the left one. The composition laws of the two families, and the interpretation of the multiplication as a
process, belong to *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; the
sandwich read as the operator $\mathrm{H}_{\tilde Q}=L_{\tilde Q}\circ R_{\tilde Q^{*}}$ belongs to *The 4×4 Matrix
Operator Representation $M_4(\mathbb{C})$ of Biquaternions*, and its action on the remarkable subspaces to *The
Sandwich Action in Subspaces*. This article states the one thing the composition laws do not: **which form the
operators are adjoint for, and what that adjoint does**.

The answer is one sentence. The bilinear form of the block is the scalar part $\langle\tilde Q_3,\tilde Q_4\rangle=\mathrm{Sc}(\tilde Q_3\tilde Q_4)$
of the product itself, its associate $F^{\approx}$ is the transpose, and the transpose of a left multiplication is a
**right** multiplication:

$$
\bigl(L_{\tilde Q_7}\bigr)^{\approx}=R_{\tilde Q_7},\qquad
\bigl(R_{\tilde Q_1}\bigr)^{\approx}=L_{\tilde Q_1},\qquad
\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\bigr)^{\approx}=L_{\tilde Q_1}R_{\tilde Q_7}.
$$

Association therefore **swaps the two sides** without conjugating the parameter, and it is the only one of the four
adjoints of the corpus that reverses a side with the parameter untouched: the Hermitian dagger keeps the side,
$(L_{\tilde Q_7})^{*}=L_{\tilde Q_7^{*}}$, the quaternionic adjoint keeps the side, and the signed Hermitian adjoint
reverses the side but conjugates the parameter, $(L_{\tilde Q_7})^{\natural\ast}=R_{\bar{\tilde Q_7}}$. Every type criterion
of the block is the consequence: a one-sided operator is self-adjoint exactly when its
parameter is central, a two-sided operator exactly when its two parameters are proportional, and no generator appears
in either family. The criteria and their proofs are the mathematics of *One-Sided Operators on the Biquaternion Algebra*, *Two-Sided Operators on the Biquaternion Algebra* and *Association and the Transpose on the Quaternion Algebra*; the article reads them.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$,
$\vec e_k^{2}=-e_t$ and central imaginary $i$; a general element is $\tilde Q=Q_te_t+\vec Q$ with the vector part
$\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The adjoint for the plain form is written $F^{\approx}$ and called the **associate**.
The form is

$$
\langle\tilde Q_3,\tilde Q_4\rangle=\mathrm{Sc}(\tilde Q_3\tilde Q_4)=Q_{3t}Q_{4t}-\vec Q_3\!\cdot\!\vec Q_4,\qquad
\mathrm{Gram}=\mathrm{diag}(1,-1,-1,-1),
$$

the **sector sign** of the block; the interval is $\langle\tilde Q_3,\tilde Q_4\rangle_{\natural}=\mathrm{Sc}(\tilde Q_3^{\natural}\tilde Q_4)$, of
signature $(-,+,+,+)$ on the material sector $\mathbb{M}_-$, and it is cited, never re-proved (*Norm and Invertibility in the General Quaternionic Algebra*). The sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$, the conjugations are the
complex $\bar{\cdot}$, the natural ${\natural}$ and the Hermitian ${}^{*}=\bar{\cdot}\circ{\natural}$, and the sandwich
is the one action form of the framework: the Lorentz action for a unit-norm parameter, the unitary evolution for a
unitary one, the measurement update for a Hermitian idempotent.

## The Two Multiplications and the Sandwich

The block carries two one-sided operators and their products:

$$
L_{\tilde Q_7}L_{\tilde Q_1}=L_{\tilde Q_7\tilde Q_1},\qquad
R_{\tilde Q_7}R_{\tilde Q_1}=R_{\tilde Q_1\tilde Q_7},\qquad
L_{\tilde Q_7}R_{\tilde Q_1}=R_{\tilde Q_1}L_{\tilde Q_7},\qquad
\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\bigr)\circ\bigl(L_{\tilde Q_2}R_{\tilde D}\bigr)=L_{\tilde Q_7\tilde Q_2}R_{\tilde D\tilde Q_1}.
$$

The first two say that the left multiplications reproduce the algebra and the right multiplications reproduce the
opposite algebra; the third says that attaching an operation before an argument and attaching one after it are
independent; the fourth says that the two-sided family is closed under composition, with the second slot read in the
reverse order because the right multiplications form an anti-representation. The parallel is exact: the parameter
enters **once** in each slot, so the assignment $\tilde Q_7\mapsto L_{\tilde Q_7}$ is $\mathbb{C}$-linear and injective, and
$L_{\tilde Q_7}(e_t)=\tilde Q_7$ recovers the parameter from the operator. The composition laws and the monoid of acting
maps are *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*, and the
enveloping algebra they generate is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*.

**Proposition (the one-sided operators span the two-sided ones).** The sixteen operators
$e_n[\,]e_m=L_{e_n}R_{e_m}$, $n,m=0,\dots,3$, are linearly independent and span $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$,
of complex dimension sixteen; the two-sided operators are the images of the decomposable tensors of
$\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, and a sum of two-sided operators need not be two-sided.

*Proof.* The independence of the sixteen basis operators is the independence of the matrix units in the two-sided
regular representation; the tensor statement is the isomorphism
$\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. That a sum of
decomposable tensors need not be decomposable is the example of *Two-Sided Operators on the Biquaternion Algebra*, §*Worked Examples*.

**Read as a physical statement.** A composition of two operations is again an operation of the same shape, so the
family of two-sided operations is closed; it is however **not a vector space**, because the sum of two compositions is
not in general a composition. The exponentials of a two-sided operator are therefore outside the family already at the
first non-trivial order, and the operators that a physical process can realise are the family itself, not its span.
The contrast with a generator algebra is explicit and is the reason this block has no bracket: the bracket belongs to
the antisymmetric band, and it is read there.

**Proposition (the sandwich is a two-sided operator).** For every $\tilde Q$,

$$
\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=\mathrm{H}_{\tilde Q},
$$

the algebraic norm pair $(\tilde Q_7,\tilde Q_1)=(\tilde Q,\tilde Q^{*})$ of the two-sided family, with the two boundary cases
$\Theta_{e_t}=\mathrm{id}$ and $R_{\tilde Q}=L_{e_t}R_{\tilde Q}$, $L_{\tilde Q}=L_{\tilde Q}R_{e_t}$.

The sandwich is one of the four objects the corpus calls an action, and it is the only one of them whose two slots are
tied; its own article is *The Sandwich Action in Subspaces*, and the operator form $\mathrm{H}_{\tilde Q}$ is *The 4×4
Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*.

## The Adjoint of the Plain Form Swaps the Sides

**Theorem (association swaps the two families).** For all $\tilde Q_7,\tilde Q_1,\tilde Q_3,\tilde Q_4\in\mathbb{B}$,

$$
\bigl\langle L_{\tilde Q_7}\tilde Q_3,\tilde Q_4\bigr\rangle=\bigl\langle\tilde Q_3,R_{\tilde Q_7}\tilde Q_4\bigr\rangle,
\qquad\text{that is}\qquad
\bigl(L_{\tilde Q_7}\bigr)^{\approx}=R_{\tilde Q_7},\qquad
\bigl(R_{\tilde Q_1}\bigr)^{\approx}=L_{\tilde Q_1}.
$$

*Proof.* The scalar part is invariant under cyclic permutation of the factors, so
$\mathrm{Sc}(\tilde Q_7\tilde Q_3\tilde Q_4)=\mathrm{Sc}(\tilde Q_3\tilde Q_4\tilde Q_7)$, which is the cross identity; the form is
non-degenerate, so the associate is the operator displayed.

**Theorem (the adjoint of a two-sided operator).** For all $\tilde Q_7,\tilde Q_1$,

$$
\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\bigr)^{\approx}=L_{\tilde Q_1}R_{\tilde Q_7},
$$

the two parameters exchanging their places.

*Proof.* The identity $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ for the transpose of a composite, applied to the
swap theorem of the one-sided operators.

**Read as a physical statement.** The pairing $\langle\cdot,\cdot\rangle$ is the scalar part of the product, and the product reads a parameter
on the side on which it stands. Transporting an operation across the pairing therefore moves it to the other side and
reverses the order of a product of two; the plain form cannot tell a left attachment from a right one. This is what
"the transpose of the left regular representation is the right one" means physically. The three companion blocks do
**not** have this behaviour: their adjoints either keep the side and conjugate the parameter or reverse the side only
by conjugating it as well, so none of them reverses a side with the parameter untouched; the
comparison of the four adjoints is the business of *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in
Examples*, and the block-by-block table is the crossing reader *The Operators of the Twelve Structures: Multiplication,
Adjoint and Bracket*. The swap is also why no type criterion of this block is a criterion on one parameter alone, and
why association is an **anti**-homomorphism on the mixed family even though each family is multiplicative or
anti-multiplicative by itself.

**Corollary (the swap is an involution on the family).** Applying association twice returns the operator,
$(F^{\approx})^{\approx}=F$. In particular the fixed points of association inside the one-sided family are the
multiplications that are at once a left and a right multiplication, and they are exactly the central ones.

## The Types of the Operators

**Theorem (the one-sided types).** For $\tilde Q_7\in\mathbb{B}$,

$$
L_{\tilde Q_7}\ \text{self-adjoint}\iff \tilde Q_7\ \text{central},\qquad
L_{\tilde Q_7}\ \text{skew-adjoint}\iff \tilde Q_7=0,
$$

and the same two criteria hold on the right with $\tilde Q_1$ in place of $\tilde Q_7$.

*Proof.* By the swap theorem, self-adjointness of $L_{\tilde Q_7}$ is $R_{\tilde Q_7}=L_{\tilde Q_7}$, that is
$\tilde Q_7\tilde Q_4=\tilde Q_4\tilde Q_7$ for every $\tilde Q_4$, which is centrality; skew-adjointness is
$\tilde Q_7\tilde Q_4=-\tilde Q_4\tilde Q_7$ for every $\tilde Q_4$, and at $\tilde Q_4=e_t$ this reads $\tilde Q_7=-\tilde Q_7$, so
$\tilde Q_7=0$.

**Theorem (the two-sided types).** For $\tilde Q_7\neq0$,

$$
L_{\tilde Q_7}R_{\tilde Q_1}\ \text{self-adjoint}\iff \tilde Q_1=\lambda\tilde Q_7\ \text{for some }\lambda\in\mathbb{C},
\qquad
L_{\tilde Q_7}R_{\tilde Q_1}\ \text{skew-adjoint}\iff L_{\tilde Q_7}R_{\tilde Q_1}=0 .
$$

*Proof.* Self-adjointness is $L_{\tilde Q_1}R_{\tilde Q_7}=L_{\tilde Q_7}R_{\tilde Q_1}$ by the swap, that is
$\tilde Q_1\tilde Q_4\tilde Q_7=\tilde Q_7\tilde Q_4\tilde Q_1$ for all $\tilde Q_4$; at $\tilde Q_4=e_t$ the parameters commute, and
substituting $\tilde Q_4=\tilde Q_7^{-1}\tilde Q_2\tilde Q_7^{-1}$ for a unit $\tilde Q_7$ gives that $\tilde Q_1\tilde Q_7^{-1}$ is
central. Skew-adjointness gives $\mathrm{Sc}(\tilde Q_4\tilde Q_7\tilde Q_1)=0$ for all $\tilde Q_4$, hence $\tilde Q_7\tilde Q_1=0$
and symmetrically $\tilde Q_1\tilde Q_7=0$, and then the defining identity at $\tilde Q_4=e_t$ reads
$\tilde Q_1\tilde Q_7=-\tilde Q_7\tilde Q_1$, so both products vanish; the remaining cases were settled by elimination.

**Corollary (the types of the sandwich).** The sandwich $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ is
self-adjoint for the plain form **exactly when the parameter lies in one of the two sectors**:

$$
\Theta_{\tilde Q}^{\approx}=\Theta_{\tilde Q}
\iff \tilde Q^{*}=\lambda\tilde Q
\iff \tilde Q\in\mathbb{M}_+\ \text{or}\ \tilde Q\in\mathbb{M}_- .
$$

*Proof.* Apply the two-sided criterion to the pair $(\tilde Q,\tilde Q^{*})$: self-adjointness is
$\tilde Q^{*}=\lambda\tilde Q$. Applying the conjugate $^{*}$ to both sides gives
$\tilde Q=\bar{\lambda}\,\tilde Q^{*}$, and combining the two gives $\tilde Q=|\lambda|^{2}\tilde Q$, so
$|\lambda|=1$; splitting $\tilde Q=\tilde P+\tilde Q_6$ with $\tilde P\in\mathbb{M}_+$ and $\tilde Q_6\in\mathbb{M}_-$ then
gives $(1-\lambda)\tilde P=(1+\lambda)\tilde Q_6$: for $\lambda=+1$ it reads $\tilde Q_6=0$, for $\lambda=-1$ it reads
$\tilde P=0$, and for $\lambda\neq\pm1$ both coefficients are nonzero, so $\tilde P$ and $\tilde Q_6$ are proportional
while lying in opposite sectors, which forces $\tilde P=\tilde Q_6=0$ and $\tilde Q=0$, in both sectors. Hence
$\tilde Q$ is Hermitian or anti-Hermitian.

**Read as a physical statement.** Three interpretations follow, one for each kind of sandwich, and they separate the three
uses of the one action form.

- The **measurement update** has a Hermitian idempotent parameter, $\tilde\Pi^{2}=\tilde\Pi=\tilde\Pi^{*}$, so it lies in
$\mathbb{M}_+$ and its sandwich is self-adjoint for the plain form.
- The **material conjugation** has an anti-Hermitian parameter, $\tilde Q\in\mathbb{M}_-$, and by the criterion it is
self-adjoint too; the sector signs of the two cases are opposite, which is the $\lambda=\pm1$ of the proof.
- The **Lorentz action** has a unit-norm parameter $\tilde U_{\mathrm L}$, the Lorentz rotor, with $\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t$, which is in general in
neither sector, and then the sandwich is **not** self-adjoint for the plain form: a boost is not symmetric for the
sector sign.

Two cautions belong here. First, self-adjointness for $\langle\cdot,\cdot\rangle$ is **not** physical hermiticity: the plain form is indefinite,
and the observables of the framework are the self-adjoint operators for the Hermitian form of the sesquilinear block,
which is *Observables, Gauge Generators and the Chirality of the Internal Action* and not this article. What is proved
here is a statement about the transpose of the plain form. Second, the skew sector of the two-sided family is trivial,
so **the general plain bilinear product supplies no generator at all**; the infinitesimal structure of the framework is the bracket
of the antisymmetric band, and its operators are read in the antisymmetric block.

## The Symmetries of the Form and of the Product

**Theorem (the one-sided automorphisms of the form).** The left multiplication $L_{\tilde Q_7}$ preserves the plain form,

$$
\langle L_{\tilde Q_7}\tilde Q_3,L_{\tilde Q_7}\tilde Q_4\rangle=\langle\tilde Q_3,\tilde Q_4\rangle\qquad\text{for all }\tilde Q_3,\tilde Q_4,
$$

if and only if $\tilde Q_7=\pm e_t$, that is $L_{\tilde Q_7}=\pm\mathrm{id}$; the same criterion holds on the right.

*Proof.* Using the swap and the symmetry of the form,

$$
\langle L_{\tilde Q_7}\tilde Q_3,L_{\tilde Q_7}\tilde Q_4\rangle=\mathrm{Sc}\bigl(\tilde Q_7\tilde Q_3\tilde Q_7\tilde Q_4\bigr)
=\langle\tilde Q_3,\tilde Q_7\tilde Q_4\tilde Q_7\rangle,
$$

so preservation is $\tilde Q_7\tilde Q_4\tilde Q_7=\tilde Q_4$ for all $\tilde Q_4$. At
$\tilde Q_4=e_t$ this gives $\tilde Q_7^{2}=e_t$ and centrality, and a central element of square $e_t$ is $\pm e_t$.

**Theorem (the two-sided automorphisms of the form).** The two-sided operator $L_{\tilde Q_7}R_{\tilde Q_1}$ preserves the
plain form if and only if $\tilde Q_1\tilde Q_7=\pm e_t$, that is $\tilde Q_1=\pm\tilde Q_7^{-1}$; the operator is then
$\pm\mathrm{Ad}_{\tilde Q_7}$, the inner automorphism of the unit $\tilde Q_7$ up to sign, and $\mathrm{Ad}_{\tilde Q_7}$
itself preserves the form.

**Theorem (the multiplicative operators).** The operator $L_{\tilde Q_7}R_{\tilde Q_1}$ is multiplicative if and only if
$\tilde Q_7\tilde Q_1=e_t$, that is $\tilde Q_1=\tilde Q_7^{-1}$:

$$
\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\tilde Q_3\bigr)\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\tilde Q_4\bigr)
=\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\bigr)(\tilde Q_3\tilde Q_4)
\qquad\text{for all }\tilde Q_3,\tilde Q_4,
$$

and the operator is then the inner automorphism $\mathrm{Ad}_{\tilde Q_7}$.

**Corollary (the partial law of the central product).** If the product $\tilde Q_1\tilde Q_7$ is merely central, the
operator is still multiplicative up to that central scalar:

$$
\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\tilde Q_3\bigr)\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\tilde Q_4\bigr)
=\tilde Q_1\tilde Q_7\,\bigl(L_{\tilde Q_7}R_{\tilde Q_1}\bigr)(\tilde Q_3\tilde Q_4),
$$

and no norm enters the multiplier.

**Read as a physical statement.** The symmetries of the sector sign $\langle\cdot,\cdot\rangle$ are the inner automorphisms of the algebra and
their negatives, and they are two-sided without exception: a genuine one-sided operation never preserves $\langle\cdot,\cdot\rangle$, so
attaching an operation on one side alone changes the sector sign of a pairing. The operators that preserve the
**composition** are the inner automorphisms $\mathrm{Ad}_{\tilde Q_7}$ themselves, and the two units $\tilde Q_7$ and
$\tilde Q_7'$ give the same operator exactly when they differ by a central scalar; conjugation is therefore the only
relabelling available to the block, and the centre is what it cannot see. The two roles — symmetry of the form and
symmetry of the product — differ by a sign and fall together on the inner automorphisms: the same operator preserves
both the composition and the pairing whenever it is multiplicative, which is the meaning of the corollary. Finally the
criteria are conditions on the **product of the two parameters**, in which no norm and no conjugation appears; the
quaternionic block carries the correspondingly stronger law,

$$
\Theta_{\tilde Q_7}(\tilde Q_3)\Theta_{\tilde Q_7}(\tilde Q_4)=\langle\tilde Q_7\rangle_{\natural}\,\Theta_{\tilde Q_7}(\tilde Q_3\tilde Q_4)
\qquad\text{for every parameter,}
$$

because there the twist absorbs a norm and here there is no twist to absorb one.

## The Operators Acting on the Spinor Space

The operators of the block act on the state space, and the action is the content of the two other articles of this
group. Let $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ be the minimal left ideal of *The Spinor Space as a Module of the Biquaternion Algebra*, with $\tilde\Pi_-=e_t-\tilde\Pi_+$ and the complement
$\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$ of *The Complementary Space of the Spinor Space in the Biquaternion Algebra*.

**Proposition (the left actions are the matrices of the module).** On the basis $(\tilde\Pi_+,\vec\Upsilon_y)$ the
four left multiplications by the basis elements are the matrix units

$$
L_{\tilde\Pi_+}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
L_{\tilde\Pi_-}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
L_{\vec\Upsilon_x}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
L_{\vec\Upsilon_y}=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

so $L$ restricted to $S$ is the map $\tilde Q\mapsto\mathsf{M}_2(\tilde Q)$ of the algebra onto $M_2(\mathbb{C})$, and
every operator on the state space is a left multiplication: $\mathbb{B}\cong\mathrm{End}_{\mathbb{C}}(S)$.

*Proof.* The matrices are the ones displayed in *The Spinor Space as a Module of the Biquaternion Algebra*, §*The Left
Action*, and the identification $\mathbb{B}\cong\mathrm{End}_{\mathbb{C}}(S)$ is the algebra acting on its
simple module.

**Proposition (the right actions move the state space to its complement).** A right multiplication commutes with every
left one, so it is a $\mathbb{B}$-linear map of $S$ into itself or into the complement; right multiplication by the
nilpotent $\vec\Upsilon_x$ carries $S$ onto $\mathbb{B}\tilde\Pi_-$ and is an isomorphism of modules, and right
multiplication by $\vec\Upsilon_y$ carries the complement onto $S$. A central element, by contrast, has equal left and
right actions and can move nothing.

*Proof.* The commutation is the third composition law, which makes every $R_{\tilde Q_1}$ a module map; the two nilpotent
carriers are computed on the basis in *The Complementary Space of the Spinor Space in the Biquaternion Algebra*,
§*The Isomorphism Is Right Multiplication, Not a Relabelling*, and the actuality of the isomorphism follows from the two ideals being
simple of the same dimension. For a central $\tilde Q_2$, $L_{\tilde Q_2}=R_{\tilde Q_2}$, so the right action preserves each
ideal.

**Theorem (the double centraliser).** An operator commutes with every left multiplication if and only if it is a right
multiplication, and an operator commuting with both families is a central scalar:

$$
\{S:SL_{\tilde Q_7}=L_{\tilde Q_7}S\ \forall\tilde Q_7\}=R(\mathbb{B}),\qquad
\{S:SL_{\tilde Q_7}=L_{\tilde Q_7}S,\ SR_{\tilde Q_1}=R_{\tilde Q_1}S\ \forall\tilde Q_7,\tilde Q_1\}=\mathbb{C}\,\mathrm{id}.
$$

*Proof.* The commutant of the left regular representation is the right one, computed by evaluating at $e_t$; the
bicommutant is then the centre, by the same argument on the right.

**Read as a physical statement.** Three interpretations. The left actions are the **observables** acting on the state space,
and every operator on the state space is one of them, which is the algebraic form of the statement that the algebra of
the block is the full matrix algebra of the spinor space. The right actions are the **commuting** family, and the ones
among them that move a state are the nilpotent ones: attaching a nilpotent on the right carries a state to the
complement, which is the operator content of the corpus's interpretation of the mass term as a right multiplication. And the
bicommutant is the scalars, so the central phase is the only operation that is invisible from the state space — the
algebraic content of the invariance of the framework under a central phase. The three statements are proved in the two
sibling articles and in the double-centraliser theorem, and they are the reason the module of the block is complete:
the algebra is recovered from its action, and nothing else acts.

## The Sandwich and the Inner Automorphism

The sandwich and the inner automorphism are the same operator on the unitaries and different on the boosts, and that
difference is the block's own sharp statement about its two-sided operators.

**Proposition (the two parametrisations of one conjugation).** For every unit $\tilde Q_7$,

$$
\Theta_{\tilde Q_7}=L_{\tilde Q_7}R_{\tilde Q_7^{*}},\qquad
\mathrm{Ad}_{\tilde Q_7}=L_{\tilde Q_7}R_{\tilde Q_7^{-1}},
$$

so the sandwich conjugates by the **conjugate** of the parameter and the inner automorphism by its **inverse**. The
two operators agree exactly when $\tilde Q_7^{*}=\tilde Q_7^{-1}$, that is when $\tilde Q_7\tilde Q_7^{*}=e_t$: on the
**unitary** parameters, and there alone.

*Proof.* The first display is the definition of the sandwich, the second the definition of the inner automorphism, and
they coincide exactly when the two right parameters coincide; the kernel of the action $\tilde Q_7\mapsto\mathrm{Ad}_{\tilde Q_7}$
is the centre, so no ambiguity remains.

**Theorem (both preserve the interval, and they differ on a boost).** Let $\tilde U_{\mathrm L}$ be of unit norm,
$\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t$. Then $\Theta_{\tilde U_{\mathrm L}}$ and $\mathrm{Ad}_{\tilde U_{\mathrm L}}$ both
preserve the interval $\langle\tilde Q_3,\tilde Q_4\rangle_{\natural}=\mathrm{Sc}(\tilde Q_3^{\natural}\tilde Q_4)$ and both preserve the sectors
$\mathbb{M}_\pm$; the inner automorphism preserves the plain form $\langle\cdot,\cdot\rangle$ as well, and the sandwich preserves it exactly
when $\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}=\pm e_t$, a condition the unit-norm boosts fail. A boost is therefore a parameter
for which the two operators differ **and** for which the sandwich loses the plain form.

*Proof.* For the interval, with $\tilde U_{\mathrm L}^{\natural}=\tilde U_{\mathrm L}^{-1}$ and
$\tilde U_{\mathrm L}^{*}=\bar{\tilde U_{\mathrm L}}^{\,\natural}$, and writing the two-sided operator of the sandwich as
$\Theta_{\tilde U_{\mathrm L}}\tilde Q_3=\tilde U_{\mathrm L}\tilde Q_3\tilde U_{\mathrm L}^{*}$,

$$
N\bigl(\Theta_{\tilde U_{\mathrm L}}\tilde Q_3,\Theta_{\tilde U_{\mathrm L}}\tilde Q_4\bigr)
=\mathrm{Sc}\bigl((\tilde U_{\mathrm L}\tilde Q_3\tilde U_{\mathrm L}^{*})^{\natural}\,\tilde U_{\mathrm L}\tilde Q_4\tilde U_{\mathrm L}^{*}\bigr)
=\mathrm{Sc}\bigl(\tilde U_{\mathrm L}^{*\natural}\tilde Q_3^{\natural}\tilde U_{\mathrm L}^{\natural}\tilde U_{\mathrm L}\tilde Q_4\tilde U_{\mathrm L}^{*}\bigr)
=\mathrm{Sc}\bigl(\tilde Q_3^{\natural}\tilde Q_4\,\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}^{*\natural}\bigr)
=\mathrm{Sc}\bigl(\tilde Q_3^{\natural}\tilde Q_4\bigr),
$$

where the third step uses $\tilde U_{\mathrm L}^{\natural}\tilde U_{\mathrm L}=e_t$ and the cyclicity of the scalar part, and the
last uses

$$
\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}^{*\natural}
=\bar{\tilde U_{\mathrm L}}^{\,\natural}\bar{\tilde U_{\mathrm L}}
=\overline{\tilde U_{\mathrm L}^{\natural}\tilde U_{\mathrm L}}=e_t .
$$

The inner automorphism preserves the interval because it preserves the product and the natural conjugation; the sector statement is
$(\Theta_{\tilde U_{\mathrm L}}\tilde Q_3)^{*}=\tilde U_{\mathrm L}\tilde Q_3^{*}\tilde U_{\mathrm L}^{*}$, which changes the sign of the sector
exactly when $\tilde Q_3$ does; and the plain form is not preserved because the sandwich is not an algebra automorphism.

**Read as a physical statement.** The framework attaches a conjugation to an element in two ways, and the two agree
only on the compact part of the parameter group. The Lorentz action is the **conjugate** one,
$\tilde Q_3\mapsto\tilde U_{\mathrm L}\tilde Q_3\tilde U_{\mathrm L}^{*}$, and the algebra automorphism is the **inverse** one,
$\tilde Q_3\mapsto\tilde U_{\mathrm L}\tilde Q_3\tilde U_{\mathrm L}^{-1}$; on a boost the two differ, while on a rotation they coincide,
and the compact subgroup is exactly the place where "conjugation by the inverse" and "conjugation by the conjugate" are
the same statement. This is the operator form of the corpus's identification of the compact slice with the internal
charge and of the boost with the non-compact part: the difference of the two conjugations is a Lorentz-invariant
measure of the non-compactness of the parameter, and it vanishes identically on the unitary slice. The Lorentz action
itself, the double cover and the rotor are *Biquaternion Rotations and Lorentz Transformations*, and the two
conjugations of the block are read there.

## A Worked Case

Take one material element as a parameter,

$$
\tilde Q=ie_t+2\vec e_x\in\mathbb{M}_-,\qquad
\langle\tilde Q,\tilde Q\rangle=-5,\qquad \langle\tilde Q,\tilde Q\rangle_{\natural}=+3,\qquad
\tilde Q^{2}=-5e_t+4i\vec e_x .
$$

Its conjugate is $-\tilde Q$, so the sandwich is $\Theta_{\tilde Q}=L_{\tilde Q}R_{-\tilde Q}$ and the criterion reads
$\lambda=-1$: the operator is self-adjoint for the plain form, as the corollary of the type criteria says, and the
sector $\mathbb{M}_-$ is why. On the unit,

$$
\Theta_{\tilde Q}(e_t)=\tilde Q\tilde Q^{*}=-\tilde Q^{2}=5e_t-4i\vec e_x,
$$

a combination of the central and the $\vec e_x$ directions, and the value is a material element up to the imaginary unit that
the transport across the pairing introduces. The same parameter gives the two different invariants of the block at once,
$\langle\tilde Q,\tilde Q\rangle$ negative and $\langle\tilde Q,\tilde Q\rangle_{\natural}$ positive, so the case displays the distinction the group is built on: the operator is symmetric
for the sector sign while the parameter is a material four-vector.

Take next a **boost** parameter,

$$
\tilde U_{\mathrm L}=\cosh u\,e_t+\sinh u\,i\vec e_x,\qquad
\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t,\qquad
\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{*}=\cosh 2u\,e_t+\sinh 2u\,i\vec e_x\neq e_t .
$$

The parameter has unit norm and is Hermitian, so it is in $\mathbb{M}_+$ and the sandwich is self-adjoint; but it is not
unitary, so it is not in the compact slice. On $\vec e_x$ the two conjugations separate:

$$
\Theta_{\tilde U_{\mathrm L}}(\vec e_x)=\tilde U_{\mathrm L}^{2}\vec e_x=\cosh 2u\,\vec e_x-\sinh 2u\,ie_t,
\qquad
\mathrm{Ad}_{\tilde U_{\mathrm L}}(\vec e_x)=\vec e_x .
$$

Both operators preserve the interval, the sandwich moves $\vec e_x$ by a hyperbolic rotation, and the inner automorphism
leaves it fixed; the difference is the non-compact part of the parameter, displayed on one element. For $u\to0$ the two
operators merge, which is the unitary limit.

Take finally a **measurement** parameter,

$$
\tilde\Pi=\tfrac12(e_t+i\vec e_x),\qquad
\tilde\Pi^{2}=\tilde\Pi=\tilde\Pi^{*}\in\mathbb{M}_+ ,\qquad
\Theta_{\tilde\Pi}=L_{\tilde\Pi}R_{\tilde\Pi},
$$

self-adjoint by the criterion with $\lambda=+1$, and a Hermitian idempotent, so the sandwich is the measurement update
of the one action form. The three parameters — an anti-Hermitian four-vector, a Hermitian boost, a Hermitian
idempotent — give the same symmetry verdict for the first and the third and a different Lorentz character for the
second, and the case separates the two questions the block asks about an operator: **which form it is symmetric for**
and **which motion it generates**.

**A numerical check.** For random elements the five identities $L_{\tilde Q_7}L_{\tilde Q_1}=L_{\tilde Q_7\tilde Q_1}$,
$R_{\tilde Q_7}R_{\tilde Q_1}=R_{\tilde Q_1\tilde Q_7}$, $L_{\tilde Q_7}R_{\tilde Q_1}=R_{\tilde Q_1}L_{\tilde Q_7}$,
$\langle L_{\tilde Q_7}\tilde Q_3,\tilde Q_4\rangle=\langle\tilde Q_3,R_{\tilde Q_7}\tilde Q_4\rangle$ and
$(L_{\tilde Q_7}R_{\tilde Q_1})^{\approx}=L_{\tilde Q_1}R_{\tilde Q_7}$ hold to machine precision; the type criteria were
checked on random, central, pure, null and unit parameters; the sandwich criterion holds on the two sectors and fails
off them; the form-preserving criteria hold exactly at $\tilde Q_7=\pm e_t$ and $\tilde Q_1\tilde Q_7=\pm e_t$; and the two
conjugations of the boost case were compared element by element.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must
declare.

- **The composition laws are not re-proved here.** They are *The Monoid of Acting Maps: the Process Is the
Multiplication, the State Is the Idempotent*, and the reading of the multiplication as a process belongs to that
article.
- **The sandwich is not re-read here.** Its action on the remarkable subspaces is *The Sandwich Action in Subspaces*,
and its operator form is *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*.
- **The physical adjoint is not this adjoint.** Self-adjointness for the plain form $\langle\cdot,\cdot\rangle$ is not hermiticity; the
observables and the gauge generators are the self-adjoint and the skew-adjoint operators for the Hermitian form of the
sesquilinear block, and they are *Observables, Gauge Generators and the Chirality of the Internal Action*. This
article's adjoint is a **transpose**, and its fixed points are the central multiplications, not the observables.
- **The four adjoints are not compared here.** The comparison, block against block, is the crossing reader *The
Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this article
declares only the plain column.
- **The sector sign is not the metric.** $\langle\cdot,\cdot\rangle$ carries the sector sign; the interval, the mass shell and the metric are
*The Four Forms, the Four Algebraic Norms and the Change of Scalars* and the companion block, and the worked case gives the two values on one element.

**What the framework does not claim.** The interpretation does not derive the Lorentz transformation, the unitary evolution or
the measurement update from the operator calculus; it reads the three parametrisations that the corpus already uses. It
does not identify a physical symmetry with the inner automorphisms; it states that the symmetries of the sector sign
inside this family are those. And it does not claim that the operator calculus of the twelve rows is one calculus: the
general plain row is the only row with an enveloping operator algebra, and the swap of the sides is its own.

## The Ledger

**Proved.** The one-sided operators $L_{\tilde Q_7}(\tilde Q_4)=\tilde Q_7\tilde Q_4$ and
$R_{\tilde Q_1}(\tilde Q_4)=\tilde Q_4\tilde Q_1$ are $\mathbb{C}$-linear and injective in the parameter, they commute, their
sixteen products span $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, and composition reverses the second slot; the associate
of the plain form, $F^{\approx}$, is the transpose, and it **swaps** the two families,
$(L_{\tilde Q_7})^{\approx}=R_{\tilde Q_7}$ and $(L_{\tilde Q_7}R_{\tilde Q_1})^{\approx}=L_{\tilde Q_1}R_{\tilde Q_7}$; a
one-sided operator is self-adjoint exactly for a central parameter and skew-adjoint only for the zero parameter; a
two-sided operator is self-adjoint exactly when its parameters are proportional and skew-adjoint only when it vanishes;
the sandwich $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ is self-adjoint exactly when $\tilde Q$ lies in a sector,
so the measurement update and the material conjugation qualify and a generic Lorentz parameter does not; the one-sided
form-preserving operators are $\pm\mathrm{id}$ and the two-sided ones are the $\pm\mathrm{Ad}_{\tilde Q_7}$ with
$\tilde Q_1\tilde Q_7=\pm e_t$; the multiplicative ones are the inner automorphisms, with the central-product partial law;
the commutant of the left regular representation is the right one and the bicommutant is the scalars; and the sandwich
and the inner automorphism agree exactly on the unitary parameters.

**Interpretations.** That the adjoint of the block is a **transport to the other side**, and that the plain form cannot tell a
left attachment from a right one; that **no generator appears** in either one-sided or two-sided family, so the
infinitesimal structure belongs to the antisymmetric band; that the symmetries of the sector sign are the inner
automorphisms and that a one-sided operation never is one; that the left actions are the observables on the state space
and the nilpotent right actions carry a state to the complement; and that the sandwich and the inner automorphism
separate on the boost and merge on the compact slice. Each is the framework's naming of a proved algebraic fact and is
labelled as such.

## Physical Readings

The operators of the general plain bilinear product read as the two ways of attaching a material operation to an element and as the
composition on both sides that the framework calls the sandwich. Three further readings follow from the adjoint. The
adjoint being the swap, the pairing $\langle\cdot,\cdot\rangle$ is read as a relation that does not distinguish left from right, which is the
operator content of its symmetry; the absence of generators in the block is read as the statement that the general plain bilinear product composes processes but does not infinitesimally generate them, the generation being the bracket of the
antisymmetric band; and the type criteria being criteria on the product of the two parameters is read as the statement
that the two-sided operations are **pairs**, not parameters, so only the relative data of the two slots is physical.
Read on the state space, the left actions are the matrices of the algebra and the right actions by the nilpotents are
the maps that exchange the two minimal ideals, which is the operator form of the corpus's coupling of the state space to
its complement. Read on the clock, the operators carry no phase of their own: the central scalars act as multiples of
the identity, and the central phase is the one operation the state space cannot see.

## Summary

The operators of the general plain algebra are the left and the right multiplications, $L_{\tilde Q_7}(\tilde Q_4)=\tilde Q_7\tilde Q_4$
and $R_{\tilde Q_1}(\tilde Q_4)=\tilde Q_4\tilde Q_1$, and their products $L_{\tilde Q_7}R_{\tilde Q_1}(\tilde Q_4)=\tilde Q_7\tilde Q_4\tilde Q_1$,
the one-sided and the two-sided families. The parameter enters once in each slot, the two families commute, and
composition reverses the second slot. The bilinear form of the block is the scalar part of the product itself,
$\langle\tilde Q_3,\tilde Q_4\rangle=\mathrm{Sc}(\tilde Q_3\tilde Q_4)=Q_{3t}Q_{4t}-\vec Q_3\!\cdot\!\vec Q_4$ of Gram matrix
$\mathrm{diag}(1,-1,-1,-1)$, and the transpose for $\langle\cdot,\cdot\rangle$ **swaps the two sides**:
$(L_{\tilde Q_7})^{\approx}=R_{\tilde Q_7}$ and $(L_{\tilde Q_7}R_{\tilde Q_1})^{\approx}=L_{\tilde Q_1}R_{\tilde Q_7}$. Every
type criterion follows: a one-sided operator is self-adjoint exactly for a central parameter and skew-adjoint only for
zero, a two-sided one exactly when its two parameters are proportional, and the sandwich
$\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ exactly when the parameter lies in a sector — so the measurement
update and the material conjugation are symmetric for the sector sign and a generic Lorentz parameter is not. The
skew sector is trivial, so the general plain bilinear product supplies **no generator**; the symmetries of the form are the inner
automorphisms and their negatives, never a genuine one-sided operation; the operators preserving composition are the
inner automorphisms, with the central-product partial law and no norm anywhere. On the spinor space the left
multiplications are the matrix units, so the algebra is the full algebra of the state space, the right multiplications
are the commutant, the nilpotent ones carry a state to the complementary ideal, and the bicommutant is the scalars.
The sandwich and the inner automorphism, the two conjugations of one parameter, agree exactly on the unitary parameters
and separate on a boost. The distinctions are labelled throughout: what is proved is the algebra, what is proposed is
the naming.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $\langle\tilde Q_3,\tilde Q_4\rangle=\mathrm{Sc}(\tilde Q_3\tilde Q_4)$ | General plain bilinear form; Gram $\mathrm{diag}(1,-1,-1,-1)$ |
| $F^{\approx}$ | The associate, or transpose, for $\langle\cdot,\cdot\rangle$ |
| $L_{\tilde Q_7}(\tilde Q_4)=\tilde Q_7\tilde Q_4$ | Left multiplication; the left regular representation |
| $R_{\tilde Q_1}(\tilde Q_4)=\tilde Q_4\tilde Q_1$ | Right multiplication; anti-multiplicative in the parameter |
| $L_{\tilde Q_7}R_{\tilde Q_1}(\tilde Q_4)=\tilde Q_7\tilde Q_4\tilde Q_1$ | Two-sided operator; the decomposable tensors |
| $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=\mathrm{H}_{\tilde Q}$ | The sandwich; the one action form |
| $L_{\tilde Q_7}L_{\tilde Q_1}=L_{\tilde Q_7\tilde Q_1}$, $R_{\tilde Q_7}R_{\tilde Q_1}=R_{\tilde Q_1\tilde Q_7}$ | Composition laws |
| $L_{\tilde Q_7}R_{\tilde Q_1}=R_{\tilde Q_1}L_{\tilde Q_7}$ | The two families commute |
| $(L_{\tilde Q_7})^{\approx}=R_{\tilde Q_7}$ | Association swaps the sides; $(L_{\tilde Q_7}R_{\tilde Q_1})^{\approx}=L_{\tilde Q_1}R_{\tilde Q_7}$ |
| Self-adjoint $L_{\tilde Q_7}\iff\tilde Q_7$ central | One-sided type criterion; skew sector $\{0\}$ |
| Self-adjoint $L_{\tilde Q_7}R_{\tilde Q_1}\iff\tilde Q_1=\lambda\tilde Q_7$ | Two-sided type criterion |
| $\Theta_{\tilde Q}$ self-adjoint $\iff\tilde Q\in\mathbb{M}_\pm$ | The sector criterion of the sandwich |
| $L_{\tilde Q_7}$ preserves $\langle\cdot,\cdot\rangle\iff\tilde Q_7=\pm e_t$ | One-sided automorphisms of the form |
| $\tilde Q_1\tilde Q_7=\pm e_t\iff L_{\tilde Q_7}R_{\tilde Q_1}=\pm\mathrm{Ad}_{\tilde Q_7}$ | Two-sided automorphisms of the form |
| $\tilde Q_7\tilde Q_1=e_t\iff L_{\tilde Q_7}R_{\tilde Q_1}=\mathrm{Ad}_{\tilde Q_7}$ | The multiplicative operators |
| $\tilde Q_1\tilde Q_7$ central $\implies$ multiplicative up to $\tilde Q_1\tilde Q_7$ | The partial law; no norm enters |
| $\{S:SL_{\tilde Q_7}=L_{\tilde Q_7}S\}=R(\mathbb{B})$ | The commutant; the bicommutant is $\mathbb{C}\,\mathrm{id}$ |
| $\Theta_{\tilde U_{\mathrm L}}=\mathrm{Ad}_{\tilde U_{\mathrm L}}\iff\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{*}=e_t$ | The two conjugations agree on the unitary slice |
| $S=\mathbb{B}\tilde\Pi_+$, $\mathbb{B}\tilde\Pi_-$ | The spinor space and its complement |

## Further Reading

- Mathematics article *One-Sided Operators on the Biquaternion Algebra*
(`articles_maths/one-sided-operators-on-the-biquaternion-algebra.md`), for $L_{\tilde Q_7}$ and
$R_{\tilde Q_1}$, the composition laws, the swap $(L_{\tilde Q_7})^{\approx}=R_{\tilde Q_7}$, the type criteria and the
one-sided form-preserving theorem.
- Mathematics article *Two-Sided Operators on the Biquaternion Algebra*
(`articles_maths/two-sided-operators-on-the-biquaternion-algebra.md`), the companion, for
$L_{\tilde Q_7}R_{\tilde Q_1}$, the swap adjoint, the self-adjointness criterion $\tilde Q_1=\lambda\tilde Q_7$, the trivial
skew sector, the form-preserving and multiplicative criteria and the partial law of the central product.
- Mathematics article *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*
(`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the associate $F^{\approx}$, the
basis rule $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$ and the reversal $(FG)^{\approx}=G^{\approx}F^{\approx}$.
- Mathematics article *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*
(`articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for
$\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ and the two-sided
operators as the decomposable tensors.
- Mathematics article *Modules over the Biquaternion Algebra*
(`articles_maths/modules-over-the-biquaternion-algebra.md`), for the simple module, its
endomorphism ring and the decomposition of the left regular module.
- Physics article *The Products, Their Forms and Their Norms*
(`articles_physics/the-products-their-forms-and-their-norms.md`), the framing article of this group, for $\langle\cdot,\cdot\rangle$, the
sector sign and the boundary of the block.
- Physics article *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*
(`articles_physics/the-monoid-of-acting-maps-the-process-is-the-multiplication-the-state-is-the-idempotent.md`), for
the composition laws, the regular representation and the monoid interpretation of the multiplications.
- Physics article *The Sandwich Action in Subspaces* (`articles_physics/the-sandwich-action-in-subspaces.md`), for the
sandwich restricted to the remarkable subspaces and the unit-norm slice.
- Physics article *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*
(`articles_physics/the-4x4-matrix-operator-representation-of-biquaternions.md`), for the operator form
$\mathrm{H}_{\tilde Q}=L_{\tilde Q}\circ R_{\tilde Q^{*}}$ and its physical arithmetic.
- Physics article *The Spinor Space as a Module of the Biquaternion Algebra*
(`articles_physics/the-spinor-space-as-a-module-of-the-biquaternion-algebra.md`), for the ideal, the matrix units of
the left action and the module picture of the state space.
- Physics article *The Complementary Space of the Spinor Space in the Biquaternion Algebra*
(`articles_physics/the-complementary-space-of-the-spinor-space-in-the-biquaternion-algebra.md`), for the right
multiplication by the nilpotents, the isomorphism to the complement and the mass interpretation.
- Physics article *Observables, Gauge Generators and the Chirality of the Internal Action*
(`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`), for the physical
adjoint, the observables and the generators of the framework, which are the self-adjoint and the skew-adjoint operators
for the Hermitian form and not for the plain one.
- Physics article *Biquaternion Rotations and Lorentz Transformations*
(`articles_physics/biquaternion-rotations-and-lorentz-transformations.md`), for the sandwich as the Lorentz action, the
double cover and the rotor.
- Physics article *The Four Forms, the Four Algebraic Norms and the Change of Scalars* (`articles_physics/the-four-forms-the-four-algebraic-norms-and-the-change-of-scalars.md`), for
the interval, the mass shell and the metric, which are the quaternionic level data and not $\langle\cdot,\cdot\rangle$.
- Physics article *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*
(`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing reader
of the twelve operator rows, for the comparison of the four adjoints and the division of the twelve rows.
