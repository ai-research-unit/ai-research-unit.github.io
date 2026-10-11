# __The Operators of the Ordinary Product: One-Sided, Two-Sided and the Sandwich__

## Introduction

This article is the operator article of the general plain algebra, the algebra of *The Ordinary Product and the
Material Sector*. Its product is the ordinary product $\tilde P\tilde Q$, and the operators of the block are the maps
that attach an element to an argument:

$$
L_{\tilde Q}(\tilde R)=\tilde Q\tilde R,\qquad
R_{\tilde P}(\tilde R)=\tilde R\tilde P,\qquad
\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}} .
$$

The left and the right multiplication are the two one-sided operators, their products $L_{\tilde A}R_{\tilde B}$ are
the two-sided ones, and the **sandwich** is the diagonal two-sided operator in which the right parameter is the
conjugate of the left one. The composition laws of the two families, and the reading of the multiplication as a
process, belong to *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; the
sandwich read as the operator $\mathrm{H}_{\tilde Q}=L_{\tilde Q}\circ R_{\tilde Q^{*}}$ belongs to *The 4×4 Matrix
Operator Representation $M_4(\mathbb{C})$ of Biquaternions*, and its action on the remarkable subspaces to *The
Sandwich Action in Subspaces*. This article states the one thing the composition laws do not: **which form the
operators are adjoint for, and what that adjoint does**.

The answer is one sentence. The bilinear form of the block is the scalar part $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$
of the product itself, its associate $F^{\approx}$ is the transpose, and the transpose of a left multiplication is a
**right** multiplication:

$$
\bigl(L_{\tilde A}\bigr)^{\approx}=R_{\tilde A},\qquad
\bigl(R_{\tilde B}\bigr)^{\approx}=L_{\tilde B},\qquad
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}R_{\tilde A}.
$$

Association therefore **swaps the two sides** instead of conjugating the parameter. The Hermitian dagger keeps the side,
$(L_{\tilde A})^{*}=L_{\tilde A^{*}}$, and the quaternionic adjoint keeps the side, so the swap belongs to the plain
form alone. Every type criterion of the block is the consequence: a one-sided operator is self-adjoint exactly when its
parameter is central, a two-sided operator exactly when its two parameters are proportional, and no generator appears
in either family. The criteria and their proofs are the mathematics of *One-Sided Operators on the General Plain Algebra
of Biquaternions*, *Two-Sided Operators on the General Plain Algebra of Biquaternions* and *Association and the
Transpose on the General Plain Algebra*; the article reads them.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$,
$e_k^{2}=-e_0$ and central imaginary $i$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$ with the vector part
$\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$. The adjoint for the plain form is written $F^{\approx}$ and called the **associate**.
The form is

$$
B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-\mathbf P\!\cdot\!\mathbf Q,\qquad
\mathrm{Gram}=\mathrm{diag}(1,-1,-1,-1),
$$

the **sector sign** of the block; the interval is $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, of
signature $(-,+,+,+)$ on the material sector $\mathbb{M}_-$, and it is cited, never re-proved (*Biquaternion Norm and
Invertibility*). The sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$, the conjugations are the
complex $\bar{\cdot}$, the natural ${\natural}$ and the Hermitian ${}^{*}=\bar{\cdot}\circ{\natural}$, and the sandwich
is the one action form of the framework: the Lorentz action for a unit-norm parameter, the unitary evolution for a
unitary one, the measurement update for a Hermitian idempotent.

## The Two Multiplications and the Sandwich

The block carries two one-sided operators and their products:

$$
L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B},\qquad
R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A},\qquad
L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A},\qquad
\bigl(L_{\tilde A}R_{\tilde B}\bigr)\circ\bigl(L_{\tilde C}R_{\tilde D}\bigr)=L_{\tilde A\tilde C}R_{\tilde D\tilde B}.
$$

The first two say that the left multiplications reproduce the algebra and the right multiplications reproduce the
opposite algebra; the third says that attaching an operation before an argument and attaching one after it are
independent; the fourth says that the two-sided family is closed under composition, with the second slot read in the
reverse order because the right multiplications form an anti-representation. The parallel is exact: the parameter
enters **once** in each slot, so the assignment $\tilde A\mapsto L_{\tilde A}$ is $\mathbb{C}$-linear and injective, and
$L_{\tilde A}(e_0)=\tilde A$ recovers the parameter from the operator. The composition laws and the monoid of acting
maps are *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*, and the
enveloping algebra they generate is *The Enveloping Operator Algebra of the General Plain Algebra and the
Bi-module Structure*.

**Proposition (the one-sided operators span the two-sided ones).** The sixteen operators
$e_n[\,]e_m=L_{e_n}R_{e_m}$, $n,m=0,\dots,3$, are linearly independent and span $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$,
of complex dimension sixteen; the two-sided operators are the images of the decomposable tensors of
$\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$, and a sum of two-sided operators need not be two-sided.

*Proof.* The independence of the sixteen basis operators is the independence of the matrix units in the two-sided
regular representation; the tensor statement is the isomorphism
$\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. That a sum of
decomposable tensors need not be decomposable is the example of *Two-Sided Operators on the General Plain Algebra of
Biquaternions*, §*Worked Examples*.

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

the diagonal pair $(\tilde A,\tilde B)=(\tilde Q,\tilde Q^{*})$ of the two-sided family, with the two boundary cases
$\Theta_{e_0}=\mathrm{id}$ and $R_{\tilde Q}=L_{e_0}R_{\tilde Q}$, $L_{\tilde Q}=L_{\tilde Q}R_{e_0}$.

The sandwich is one of the four objects the corpus calls an action, and it is the only one of them whose two slots are
tied; its own article is *The Sandwich Action in Subspaces*, and the operator form $\mathrm{H}_{\tilde Q}$ is *The 4×4
Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*.

## The Adjoint of the Plain Form Swaps the Sides

**Theorem (association swaps the two families).** For all $\tilde A,\tilde B,\tilde X,\tilde Y\in\mathbb{B}$,

$$
\bigl\langle L_{\tilde A}\tilde X,\tilde Y\bigr\rangle=\bigl\langle\tilde X,R_{\tilde A}\tilde Y\bigr\rangle,
\qquad\text{that is}\qquad
\bigl(L_{\tilde A}\bigr)^{\approx}=R_{\tilde A},\qquad
\bigl(R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}.
$$

*Proof.* The scalar part is invariant under cyclic permutation of the factors, so
$\mathrm{Sc}(\tilde A\tilde X\tilde Y)=\mathrm{Sc}(\tilde X\tilde Y\tilde A)$, which is the cross identity; the form is
non-degenerate, so the associate is the operator displayed.

**Theorem (the adjoint of a two-sided operator).** For all $\tilde A,\tilde B$,

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}R_{\tilde A},
$$

the two parameters exchanging their places.

*Proof.* The identity $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ for the transpose of a composite, applied to the
swap theorem of the one-sided operators.

**Read as a physical statement.** The pairing $B$ is the scalar part of the product, and the product reads a parameter
on the side on which it stands. Transporting an operation across the pairing therefore moves it to the other side and
reverses the order of a product of two; the plain form cannot tell a left attachment from a right one. This is what
"the transpose of the left regular representation is the right one" means physically. The three companion blocks do
**not** have this behaviour, because their adjoints carry a conjugation of the parameter and keep the side; the
comparison of the four adjoints is the business of *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in
Examples*, and the block-by-block table is the crossing reader *The Operators of the Twelve Structures: Multiplication,
Adjoint and Bracket*. The swap is also why no type criterion of this block is a criterion on one parameter alone, and
why association is an **anti**-homomorphism on the mixed family even though each family is multiplicative or
anti-multiplicative by itself.

**Corollary (the swap is an involution on the family).** Applying association twice returns the operator,
$(F^{\approx})^{\approx}=F$. In particular the fixed points of association inside the one-sided family are the
multiplications that are at once a left and a right multiplication, and they are exactly the central ones.

## The Types of the Operators

**Theorem (the one-sided types).** For $\tilde A\in\mathbb{B}$,

$$
L_{\tilde A}\ \text{self-adjoint}\iff \tilde A\ \text{central},\qquad
L_{\tilde A}\ \text{skew-adjoint}\iff \tilde A=0,
$$

and the same two criteria hold on the right with $\tilde B$ in place of $\tilde A$.

*Proof.* By the swap theorem, self-adjointness of $L_{\tilde A}$ is $R_{\tilde A}=L_{\tilde A}$, that is
$\tilde A\tilde Y=\tilde Y\tilde A$ for every $\tilde Y$, which is centrality; skew-adjointness is
$\tilde A\tilde Y=-\tilde Y\tilde A$ for every $\tilde Y$, and at $\tilde Y=e_0$ this reads $\tilde A=-\tilde A$, so
$\tilde A=0$.

**Theorem (the two-sided types).** For $\tilde A\neq0$,

$$
L_{\tilde A}R_{\tilde B}\ \text{self-adjoint}\iff \tilde B=\lambda\tilde A\ \text{for some }\lambda\in\mathbb{C},
\qquad
L_{\tilde A}R_{\tilde B}\ \text{skew-adjoint}\iff L_{\tilde A}R_{\tilde B}=0 .
$$

*Proof.* Self-adjointness is $L_{\tilde B}R_{\tilde A}=L_{\tilde A}R_{\tilde B}$ by the swap, that is
$\tilde B\tilde Y\tilde A=\tilde A\tilde Y\tilde B$ for all $\tilde Y$; at $\tilde Y=e_0$ the parameters commute, and
substituting $\tilde Y=\tilde A^{-1}\tilde C\tilde A^{-1}$ for a unit $\tilde A$ gives that $\tilde B\tilde A^{-1}$ is
central. Skew-adjointness gives $\mathrm{Sc}(\tilde Y\tilde A\tilde B)=0$ for all $\tilde Y$, hence $\tilde A\tilde B=0$
and symmetrically $\tilde B\tilde A=0$, and then the defining identity at $\tilde Y=e_0$ reads
$\tilde B\tilde A=-\tilde A\tilde B$, so both products vanish; the remaining cases were settled by elimination.

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
$|\lambda|=1$; splitting $\tilde Q=\tilde P+\tilde R$ with $\tilde P\in\mathbb{M}_+$ and $\tilde R\in\mathbb{M}_-$ then
gives $(1-\lambda)\tilde P=(1+\lambda)\tilde R$, which for $\lambda\neq\pm1$ forces both halves into one sector and
contradicts the value of $\lambda$. Hence $\lambda=\pm1$ and $\tilde Q$ is Hermitian or anti-Hermitian.

**Read as a physical statement.** Three readings follow, one for each kind of sandwich, and they separate the three
uses of the one action form.

- The **measurement update** has a Hermitian idempotent parameter, $\tilde\Pi^{2}=\tilde\Pi=\tilde\Pi^{*}$, so it lies in
$\mathbb{M}_+$ and its sandwich is self-adjoint for the plain form.
- The **material conjugation** has an anti-Hermitian parameter, $\tilde Q\in\mathbb{M}_-$, and by the criterion it is
self-adjoint too; the sector signs of the two cases are opposite, which is the $\lambda=\pm1$ of the proof.
- The **Lorentz action** has a unit-norm parameter $\tilde\Lambda\tilde\Lambda^{\natural}=e_0$ which is in general in
neither sector, and then the sandwich is **not** self-adjoint for the plain form: a boost is not symmetric for the
sector sign.

Two cautions belong here. First, self-adjointness for $B$ is **not** physical hermiticity: the plain form is indefinite,
and the observables of the framework are the self-adjoint operators for the Hermitian form of the sesquilinear block,
which is *Observables, Gauge Generators and the Chirality of the Internal Action* and not this article. What is proved
here is a statement about the transpose of the plain form. Second, the skew sector of the two-sided family is trivial,
so **the ordinary product supplies no generator at all**; the infinitesimal structure of the framework is the bracket
of the antisymmetric band, and its operators are read in the antisymmetric block.

## The Symmetries of the Form and of the Product

**Theorem (the one-sided automorphisms of the form).** The left multiplication $L_{\tilde A}$ preserves the plain form,

$$
B\bigl(L_{\tilde A}\tilde X,L_{\tilde A}\tilde Y\bigr)=B(\tilde X,\tilde Y)\qquad\text{for all }\tilde X,\tilde Y,
$$

if and only if $\tilde A=\pm e_0$, that is $L_{\tilde A}=\pm\mathrm{id}$; the same criterion holds on the right.

*Proof.* Using the swap and the symmetry of the form,

$$
B\bigl(L_{\tilde A}\tilde X,L_{\tilde A}\tilde Y\bigr)=\mathrm{Sc}\bigl(\tilde A\tilde X\tilde A\tilde Y\bigr)
=B\bigl(\tilde X,\tilde A\tilde Y\tilde A\bigr),
$$

so preservation is $\tilde A\tilde Y\tilde A=\tilde Y$ for all $\tilde Y$. At
$\tilde Y=e_0$ this gives $\tilde A^{2}=e_0$ and centrality, and a central element of square $e_0$ is $\pm e_0$.

**Theorem (the two-sided automorphisms of the form).** The two-sided operator $L_{\tilde A}R_{\tilde B}$ preserves the
plain form if and only if $\tilde B\tilde A=\pm e_0$, that is $\tilde B=\pm\tilde A^{-1}$; the operator is then
$\pm\mathrm{Ad}_{\tilde A}$, the inner automorphism of the unit $\tilde A$ up to sign, and $\mathrm{Ad}_{\tilde A}$
itself preserves the form.

**Theorem (the multiplicative operators).** The operator $L_{\tilde A}R_{\tilde B}$ is multiplicative if and only if
$\tilde A\tilde B=e_0$, that is $\tilde B=\tilde A^{-1}$:

$$
\bigl(L_{\tilde A}R_{\tilde B}\tilde X\bigr)\bigl(L_{\tilde A}R_{\tilde B}\tilde Y\bigr)
=\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde X\tilde Y)
\qquad\text{for all }\tilde X,\tilde Y,
$$

and the operator is then the inner automorphism $\mathrm{Ad}_{\tilde A}$.

**Corollary (the partial law of the central product).** If the product $\tilde B\tilde A$ is merely central, the
operator is still multiplicative up to that central scalar:

$$
\bigl(L_{\tilde A}R_{\tilde B}\tilde X\bigr)\bigl(L_{\tilde A}R_{\tilde B}\tilde Y\bigr)
=\tilde B\tilde A\,\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde X\tilde Y),
$$

and no norm enters the multiplier.

**Read as a physical statement.** The symmetries of the sector sign $B$ are the inner automorphisms of the algebra and
their negatives, and they are two-sided without exception: a genuine one-sided operation never preserves $B$, so
attaching an operation on one side alone changes the sector sign of a pairing. The operators that preserve the
**composition** are the inner automorphisms $\mathrm{Ad}_{\tilde A}$ themselves, and the two units $\tilde A$ and
$\tilde A'$ give the same operator exactly when they differ by a central scalar; conjugation is therefore the only
relabelling available to the block, and the centre is what it cannot see. The two roles — symmetry of the form and
symmetry of the product — differ by a sign and fall together on the inner automorphisms: the same operator preserves
both the composition and the pairing whenever it is multiplicative, which is the meaning of the corollary. Finally the
criteria are conditions on the **product of the two parameters**, in which no norm and no conjugation appears; the
quaternionic block carries the correspondingly stronger law,

$$
\Theta_{\tilde A}(\tilde X)\Theta_{\tilde A}(\tilde Y)=N(\tilde A)\,\Theta_{\tilde A}(\tilde X\tilde Y)
\qquad\text{for every parameter,}
$$

because there the twist absorbs a norm and here there is no twist to absorb one.

## The Operators Acting on the Spinor Space

The operators of the block act on the state space, and the action is the content of the two other articles of this
group. Let $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde\Upsilon_2\}$ be the minimal left ideal of *The
Spinor Space as a Module and as a Hilbert Space*, with $\tilde\Pi_2=e_0-\tilde\Pi_1$ and the complement
$\mathbb{B}\tilde\Pi_2=\mathbb{C}\{\tilde\Pi_2,\tilde\Upsilon_1\}$ of *The Complementary Space of the Spinor Space and
Its Physical Meaning*.

**Proposition (the left actions are the matrices of the module).** On the basis $(\tilde\Pi_1,\tilde\Upsilon_2)$ the
four left multiplications by the basis elements are the matrix units

$$
L_{\tilde\Pi_1}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
L_{\tilde\Pi_2}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
L_{\tilde\Upsilon_1}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
L_{\tilde\Upsilon_2}=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

so $L$ restricted to $S$ is the map $\tilde Q\mapsto\mathsf{M}_2(\tilde Q)$ of the algebra onto $M_2(\mathbb{C})$, and
every operator on the state space is a left multiplication: $\mathbb{B}\cong\mathrm{End}_{\mathbb{C}}(S)$.

*Proof.* The matrices are the ones displayed in *The Spinor Space as a Module and as a Hilbert Space*, §*The Structure
of the Module*, and the identification $\mathbb{B}\cong\mathrm{End}_{\mathbb{C}}(S)$ is the algebra acting on its
simple module.

**Proposition (the right actions move the state space to its complement).** A right multiplication commutes with every
left one, so it is a $\mathbb{B}$-linear map of $S$ into itself or into the complement; right multiplication by the
nilpotent $\tilde\Upsilon_1$ carries $S$ onto $\mathbb{B}\tilde\Pi_2$ and is an isomorphism of modules, and right
multiplication by $\tilde\Upsilon_2$ carries the complement onto $S$. A central element, by contrast, has equal left and
right actions and can move nothing.

*Proof.* The commutation is the third composition law, which makes every $R_{\tilde B}$ a module map; the two nilpotent
carriers are computed on the basis in *The Complementary Space of the Spinor Space and Its Physical Meaning*,
§*Right Multiplication by the Nilpotents*, and the actuality of the isomorphism follows from the two ideals being
simple of the same dimension. For a central $\tilde C$, $L_{\tilde C}=R_{\tilde C}$, so the right action preserves each
ideal.

**Theorem (the double centraliser).** An operator commutes with every left multiplication if and only if it is a right
multiplication, and an operator commuting with both families is a central scalar:

$$
\{S:SL_{\tilde A}=L_{\tilde A}S\ \forall\tilde A\}=R(\mathbb{B}),\qquad
\{S:SL_{\tilde A}=L_{\tilde A}S,\ SR_{\tilde B}=R_{\tilde B}S\ \forall\tilde A,\tilde B\}=\mathbb{C}\,\mathrm{id}.
$$

*Proof.* The commutant of the left regular representation is the right one, computed by evaluating at $e_0$; the
bicommutant is then the centre, by the same argument on the right.

**Read as a physical statement.** Three readings. The left actions are the **observables** acting on the state space,
and every operator on the state space is one of them, which is the algebraic form of the statement that the algebra of
the block is the full matrix algebra of the spinor space. The right actions are the **commuting** family, and the ones
among them that move a state are the nilpotent ones: attaching a nilpotent on the right carries a state to the
complement, which is the operator content of the corpus's reading of the mass term as a right multiplication. And the
bicommutant is the scalars, so the central phase is the only operation that is invisible from the state space — the
algebraic content of the invariance of the framework under a central phase. The three statements are proved in the two
sibling articles and in the double-centraliser theorem, and they are the reason the module of the block is complete:
the algebra is recovered from its action, and nothing else acts.

## The Sandwich and the Inner Automorphism

The sandwich and the inner automorphism are the same operator on the unitaries and different on the boosts, and that
difference is the block's own sharp statement about its two-sided operators.

**Proposition (the two parametrisations of one conjugation).** For every unit $\tilde A$,

$$
\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{*}},\qquad
\mathrm{Ad}_{\tilde A}=L_{\tilde A}R_{\tilde A^{-1}},
$$

so the sandwich conjugates by the **conjugate** of the parameter and the inner automorphism by its **inverse**. The
two operators agree exactly when $\tilde A^{*}=\tilde A^{-1}$, that is when $\tilde A\tilde A^{*}=e_0$: on the
**unitary** parameters, and there alone.

*Proof.* The first display is the definition of the sandwich, the second the definition of the inner automorphism, and
they coincide exactly when the two right parameters coincide; the kernel of the action $\tilde A\mapsto\mathrm{Ad}_{\tilde A}$
is the centre, so no ambiguity remains.

**Theorem (both preserve the interval, and they differ on a boost).** Let $\tilde\Lambda$ be of unit norm,
$\tilde\Lambda\tilde\Lambda^{\natural}=e_0$. Then $\Theta_{\tilde\Lambda}$ and $\mathrm{Ad}_{\tilde\Lambda}$ both
preserve the interval $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ and both preserve the sectors
$\mathbb{M}_\pm$; the inner automorphism preserves the plain form $B$ as well, and the sandwich preserves it exactly
when $\tilde\Lambda^{*}\tilde\Lambda=\pm e_0$, a condition the unit-norm boosts fail. A boost is therefore a parameter
for which the two operators differ **and** for which the sandwich loses the plain form.

*Proof.* For the interval, with $\tilde\Lambda^{\natural}=\tilde\Lambda^{-1}$ and
$\tilde\Lambda^{*}=\bar{\tilde\Lambda}^{\,\natural}$, and writing the two-sided operator of the sandwich as
$\Theta_{\tilde\Lambda}\tilde P=\tilde\Lambda\tilde P\tilde\Lambda^{*}$,

$$
N\bigl(\Theta_{\tilde\Lambda}\tilde P,\Theta_{\tilde\Lambda}\tilde Q\bigr)
=\mathrm{Sc}\bigl((\tilde\Lambda\tilde P\tilde\Lambda^{*})^{\natural}\,\tilde\Lambda\tilde Q\tilde\Lambda^{*}\bigr)
=\mathrm{Sc}\bigl(\tilde\Lambda^{*\natural}\tilde P^{\natural}\tilde\Lambda^{\natural}\tilde\Lambda\tilde Q\tilde\Lambda^{*}\bigr)
=\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde Q\,\tilde\Lambda^{*}\tilde\Lambda^{*\natural}\bigr)
=\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde Q\bigr),
$$

where the third step uses $\tilde\Lambda^{\natural}\tilde\Lambda=e_0$ and the cyclicity of the scalar part, and the
last uses

$$
\tilde\Lambda^{*}\tilde\Lambda^{*\natural}
=\bar{\tilde\Lambda}^{\,\natural}\bar{\tilde\Lambda}
=\overline{\tilde\Lambda^{\natural}\tilde\Lambda}=e_0 .
$$

The inner automorphism preserves the interval because it preserves the product and the natural conjugation; the sector statement is
$(\Theta_{\tilde\Lambda}\tilde P)^{*}=\tilde\Lambda\tilde P^{*}\tilde\Lambda^{*}$, which changes the sign of the sector
exactly when $\tilde P$ does; and the plain form is not preserved because the sandwich is not an algebra automorphism.

**Read as a physical statement.** The framework attaches a conjugation to an element in two ways, and the two agree
only on the compact part of the parameter group. The Lorentz action is the **conjugate** one,
$\tilde P\mapsto\tilde\Lambda\tilde P\tilde\Lambda^{*}$, and the algebra automorphism is the **inverse** one,
$\tilde P\mapsto\tilde\Lambda\tilde P\tilde\Lambda^{-1}$; on a boost the two differ, while on a rotation they coincide,
and the compact subgroup is exactly the place where "conjugation by the inverse" and "conjugation by the conjugate" are
the same statement. This is the operator form of the corpus's identification of the compact slice with the internal
charge and of the boost with the non-compact part: the difference of the two conjugations is a Lorentz-invariant
measure of the non-compactness of the parameter, and it vanishes identically on the unitary slice. The Lorentz action
itself, the double cover and the rotor are *Biquaternion Rotations and Lorentz Transformations*, and the two
conjugations of the block are read there.

## A Worked Case

Take one material element as a parameter,

$$
\tilde Q=ie_0+2e_1\in\mathbb{M}_-,\qquad
B(\tilde Q,\tilde Q)=-5,\qquad N(\tilde Q,\tilde Q)=+5,\qquad
\tilde Q^{2}=-5e_0+4ie_1 .
$$

Its conjugate is $-\tilde Q$, so the sandwich is $\Theta_{\tilde Q}=L_{\tilde Q}R_{-\tilde Q}$ and the criterion reads
$\lambda=-1$: the operator is self-adjoint for the plain form, as the corollary of the type criteria says, and the
sector $\mathbb{M}_-$ is why. On the unit,

$$
\Theta_{\tilde Q}(e_0)=\tilde Q\tilde Q^{*}=-\tilde Q^{2}=5e_0-4ie_1,
$$

a combination of the central and the $e_1$ directions, and the value is a material element up to the imaginary unit that
the transport across the pairing introduces. The same parameter gives the two different invariants of the block at once,
$B$ negative and $N$ positive, so the case displays the distinction the group is built on: the operator is symmetric
for the sector sign while the parameter is a material four-vector.

Take next a **boost** parameter,

$$
\tilde\Lambda=\cosh u\,e_0+\sinh u\,ie_1,\qquad
\tilde\Lambda\tilde\Lambda^{\natural}=e_0,\qquad
\tilde\Lambda\tilde\Lambda^{*}=\cosh 2u\,e_0+\sinh 2u\,ie_1\neq e_0 .
$$

The parameter has unit norm and is Hermitian, so it is in $\mathbb{M}_+$ and the sandwich is self-adjoint; but it is not
unitary, so it is not in the compact slice. On $e_1$ the two conjugations separate:

$$
\Theta_{\tilde\Lambda}(e_1)=\tilde\Lambda^{2}e_1=\cosh 2u\,e_1-\sinh 2u\,ie_0,
\qquad
\mathrm{Ad}_{\tilde\Lambda}(e_1)=e_1 .
$$

Both operators preserve the interval, the sandwich moves $e_1$ by a hyperbolic rotation, and the inner automorphism
leaves it fixed; the difference is the non-compact part of the parameter, displayed on one element. For $u\to0$ the two
operators merge, which is the unitary limit.

Take finally a **measurement** parameter,

$$
\tilde\Pi=\tfrac12(e_0+ie_1),\qquad
\tilde\Pi^{2}=\tilde\Pi=\tilde\Pi^{*}\in\mathbb{M}_+ ,\qquad
\Theta_{\tilde\Pi}=L_{\tilde\Pi}R_{\tilde\Pi},
$$

self-adjoint by the criterion with $\lambda=+1$, and a Hermitian idempotent, so the sandwich is the measurement update
of the one action form. The three parameters — an anti-Hermitian four-vector, a Hermitian boost, a Hermitian
idempotent — give the same symmetry verdict for the first and the third and a different Lorentz character for the
second, and the case separates the two questions the block asks about an operator: **which form it is symmetric for**
and **which motion it generates**.

**A numerical check.** For random elements the five identities $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$,
$R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$, $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$,
$\langle L_{\tilde A}\tilde X,\tilde Y\rangle=\langle\tilde X,R_{\tilde A}\tilde Y\rangle$ and
$(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$ hold to machine precision; the type criteria were
checked on random, central, pure, null and unit parameters; the sandwich criterion holds on the two sectors and fails
off them; the form-preserving criteria hold exactly at $\tilde A=\pm e_0$ and $\tilde B\tilde A=\pm e_0$; and the two
conjugations of the boost case were compared element by element.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must
declare.

- **The composition laws are not re-proved here.** They are *The Monoid of Acting Maps: the Process Is the
Multiplication, the State Is the Idempotent*, and the reading of the multiplication as a process belongs to that
article.
- **The sandwich is not re-read here.** Its action on the remarkable subspaces is *The Sandwich Action in Subspaces*,
and its operator form is *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*.
- **The physical adjoint is not this adjoint.** Self-adjointness for the plain form $B$ is not hermiticity; the
observables and the gauge generators are the self-adjoint and the skew-adjoint operators for the Hermitian form of the
sesquilinear block, and they are *Observables, Gauge Generators and the Chirality of the Internal Action*. This
article's adjoint is a **transpose**, and its fixed points are the central multiplications, not the observables.
- **The four adjoints are not compared here.** The comparison, block against block, is the crossing reader *The
Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this article
declares only the plain column.
- **The sector sign is not the metric.** $B$ carries the sector sign; the interval, the mass shell and the metric are
*Biquaternion Norm and Invertibility* and the companion block, and the worked case gives the two values on one element.

**What the framework does not claim.** The reading does not derive the Lorentz transformation, the unitary evolution or
the measurement update from the operator calculus; it reads the three parametrisations that the corpus already uses. It
does not identify a physical symmetry with the inner automorphisms; it states that the symmetries of the sector sign
inside this family are those. And it does not claim that the operator calculus of the twelve rows is one calculus: the
general plain row is the only row with an enveloping operator algebra, and the swap of the sides is its own.

## The Ledger

**Proved.** The one-sided operators $L_{\tilde A}(\tilde Y)=\tilde A\tilde Y$ and
$R_{\tilde B}(\tilde Y)=\tilde Y\tilde B$ are $\mathbb{C}$-linear and injective in the parameter, they commute, their
sixteen products span $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, and composition reverses the second slot; the associate
of the plain form, $F^{\approx}$, is the transpose, and it **swaps** the two families,
$(L_{\tilde A})^{\approx}=R_{\tilde A}$ and $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$; a
one-sided operator is self-adjoint exactly for a central parameter and skew-adjoint only for the zero parameter; a
two-sided operator is self-adjoint exactly when its parameters are proportional and skew-adjoint only when it vanishes;
the sandwich $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ is self-adjoint exactly when $\tilde Q$ lies in a sector,
so the measurement update and the material conjugation qualify and a generic Lorentz parameter does not; the one-sided
form-preserving operators are $\pm\mathrm{id}$ and the two-sided ones are the $\pm\mathrm{Ad}_{\tilde A}$ with
$\tilde B\tilde A=\pm e_0$; the multiplicative ones are the inner automorphisms, with the central-product partial law;
the commutant of the left regular representation is the right one and the bicommutant is the scalars; and the sandwich
and the inner automorphism agree exactly on the unitary parameters.

**Readings.** That the adjoint of the block is a **transport to the other side**, and that the plain form cannot tell a
left attachment from a right one; that **no generator appears** in either one-sided or two-sided family, so the
infinitesimal structure belongs to the antisymmetric band; that the symmetries of the sector sign are the inner
automorphisms and that a one-sided operation never is one; that the left actions are the observables on the state space
and the nilpotent right actions carry a state to the complement; and that the sandwich and the inner automorphism
separate on the boost and merge on the compact slice. Each is the framework's naming of a proved algebraic fact and is
labelled as such.

## Physical Readings

The operators of the ordinary product read as the two ways of attaching a material operation to an element and as the
composition on both sides that the framework calls the sandwich. Three further readings follow from the adjoint. The
adjoint being the swap, the pairing $B$ is read as a relation that does not distinguish left from right, which is the
operator content of its symmetry; the absence of generators in the block is read as the statement that the ordinary
product composes processes but does not infinitesimally generate them, the generation being the bracket of the
antisymmetric band; and the type criteria being criteria on the product of the two parameters is read as the statement
that the two-sided operations are **pairs**, not parameters, so only the relative data of the two slots is physical.
Read on the state space, the left actions are the matrices of the algebra and the right actions by the nilpotents are
the maps that exchange the two minimal ideals, which is the operator form of the corpus's coupling of the state space to
its complement. Read on the clock, the operators carry no phase of their own: the central scalars act as multiples of
the identity, and the central phase is the one operation the state space cannot see.

## Summary

The operators of the general plain algebra are the left and the right multiplications, $L_{\tilde A}(\tilde Y)=\tilde A\tilde Y$
and $R_{\tilde B}(\tilde Y)=\tilde Y\tilde B$, and their products $L_{\tilde A}R_{\tilde B}(\tilde Y)=\tilde A\tilde Y\tilde B$,
the one-sided and the two-sided families. The parameter enters once in each slot, the two families commute, and
composition reverses the second slot. The bilinear form of the block is the scalar part of the product itself,
$B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-\mathbf P\!\cdot\!\mathbf Q$ of Gram matrix
$\mathrm{diag}(1,-1,-1,-1)$, and the transpose for $B$ **swaps the two sides**:
$(L_{\tilde A})^{\approx}=R_{\tilde A}$ and $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$. Every
type criterion follows: a one-sided operator is self-adjoint exactly for a central parameter and skew-adjoint only for
zero, a two-sided one exactly when its two parameters are proportional, and the sandwich
$\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ exactly when the parameter lies in a sector — so the measurement
update and the material conjugation are symmetric for the sector sign and a generic Lorentz parameter is not. The
skew sector is trivial, so the ordinary product supplies **no generator**; the symmetries of the form are the inner
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
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^{2}=-e_0$, $e_1e_2=e_3$ |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ | General plain bilinear form; Gram $\mathrm{diag}(1,-1,-1,-1)$ |
| $F^{\approx}$ | The associate, or transpose, for $B$ |
| $L_{\tilde A}(\tilde Y)=\tilde A\tilde Y$ | Left multiplication; the left regular representation |
| $R_{\tilde B}(\tilde Y)=\tilde Y\tilde B$ | Right multiplication; anti-multiplicative in the parameter |
| $L_{\tilde A}R_{\tilde B}(\tilde Y)=\tilde A\tilde Y\tilde B$ | Two-sided operator; the decomposable tensors |
| $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=\mathrm{H}_{\tilde Q}$ | The sandwich; the one action form |
| $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$ | Composition laws |
| $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$ | The two families commute |
| $(L_{\tilde A})^{\approx}=R_{\tilde A}$ | Association swaps the sides; $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$ |
| Self-adjoint $L_{\tilde A}\iff\tilde A$ central | One-sided type criterion; skew sector $\{0\}$ |
| Self-adjoint $L_{\tilde A}R_{\tilde B}\iff\tilde B=\lambda\tilde A$ | Two-sided type criterion |
| $\Theta_{\tilde Q}$ self-adjoint $\iff\tilde Q\in\mathbb{M}_\pm$ | The sector criterion of the sandwich |
| $L_{\tilde A}$ preserves $B\iff\tilde A=\pm e_0$ | One-sided automorphisms of the form |
| $\tilde B\tilde A=\pm e_0\iff L_{\tilde A}R_{\tilde B}=\pm\mathrm{Ad}_{\tilde A}$ | Two-sided automorphisms of the form |
| $\tilde A\tilde B=e_0\iff L_{\tilde A}R_{\tilde B}=\mathrm{Ad}_{\tilde A}$ | The multiplicative operators |
| $\tilde B\tilde A$ central $\implies$ multiplicative up to $\tilde B\tilde A$ | The partial law; no norm enters |
| $\{S:SL_{\tilde A}=L_{\tilde A}S\}=R(\mathbb{B})$ | The commutant; the bicommutant is $\mathbb{C}\,\mathrm{id}$ |
| $\Theta_{\tilde\Lambda}=\mathrm{Ad}_{\tilde\Lambda}\iff\tilde\Lambda\tilde\Lambda^{*}=e_0$ | The two conjugations agree on the unitary slice |
| $S=\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The spinor space and its complement |

## Further Reading

- Mathematics article *One-Sided Operators on the General Plain Algebra of Biquaternions*
(`articles_maths/one-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), for $L_{\tilde A}$ and
$R_{\tilde B}$, the composition laws, the swap $(L_{\tilde A})^{\approx}=R_{\tilde A}$, the type criteria and the
one-sided form-preserving theorem.
- Mathematics article *Two-Sided Operators on the General Plain Algebra of Biquaternions*
(`articles_maths/two-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), the companion, for
$L_{\tilde A}R_{\tilde B}$, the swap adjoint, the self-adjointness criterion $\tilde B=\lambda\tilde A$, the trivial
skew sector, the form-preserving and multiplicative criteria and the partial law of the central product.
- Mathematics article *Association and the Transpose on the General Plain Algebra*
(`articles_maths/association-and-the-transpose-on-the-general-plain-algebra.md`), for the associate $F^{\approx}$, the
basis rule $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$ and the reversal $(FG)^{\approx}=G^{\approx}F^{\approx}$.
- Mathematics article *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*
(`articles_maths/the-enveloping-operator-algebra-of-the-general-plain-algebra-and-the-bi-module-structure.md`), for
$\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ and the two-sided
operators as the decomposable tensors.
- Mathematics article *Modules over the General Plain Algebra of Biquaternions*
(`articles_maths/modules-over-the-general-plain-algebra-of-biquaternions.md`), for the simple module, its
endomorphism ring and the decomposition of the left regular module.
- Physics article *The Ordinary Product and the Material Sector*
(`articles_physics/the-ordinary-product-and-the-material-sector.md`), the framing article of this group, for $B$, the
sector sign and the boundary of the block.
- Physics article *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*
(`articles_physics/the-monoid-of-acting-maps-the-process-is-the-multiplication-the-state-is-the-idempotent.md`), for
the composition laws, the regular representation and the monoid reading of the multiplications.
- Physics article *The Sandwich Action in Subspaces* (`articles_physics/the-sandwich-action-in-subspaces.md`), for the
sandwich restricted to the remarkable subspaces and the unit-norm slice.
- Physics article *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*
(`articles_physics/the-4x4-matrix-operator-representation-of-biquaternions.md`), for the operator form
$\mathrm{H}_{\tilde Q}=L_{\tilde Q}\circ R_{\tilde Q^{*}}$ and its physical arithmetic.
- Physics article *The Spinor Space as a Module and as a Hilbert Space*
(`articles_physics/the-spinor-space-as-a-module-and-as-a-hilbert-space.md`), for the ideal, the matrix units of the
left action and the module picture of the state space.
- Physics article *The Complementary Space of the Spinor Space and Its Physical Meaning*
(`articles_physics/the-complementary-space-of-the-spinor-space-and-its-physical-meaning.md`), for the right
multiplication by the nilpotents, the isomorphism to the complement and the mass reading.
- Physics article *Observables, Gauge Generators and the Chirality of the Internal Action*
(`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`), for the physical
adjoint, the observables and the generators of the framework, which are the self-adjoint and the skew-adjoint operators
for the Hermitian form and not for the plain one.
- Physics article *Biquaternion Rotations and Lorentz Transformations*
(`articles_physics/biquaternion-rotations-and-lorentz-transformations.md`), for the sandwich as the Lorentz action, the
double cover and the rotor.
- Physics article *Biquaternion Norm and Invertibility* (`articles_physics/biquaternion-norm-and-invertibility.md`), for
the interval, the mass shell and the metric, which are the quaternionic level data and not $B$.
- Physics article *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*
(`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing reader
of the twelve operator rows, for the comparison of the four adjoints and the division of the twelve rows.
