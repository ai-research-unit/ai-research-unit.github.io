# __The Operators of the Plain Sesquilinear Product and the Born Pairing__

## Introduction

The GPS band reads the plain sesquilinear product as the probability structure of the framework. The product is
$\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, the ordinary product with its second slot read through the Hermitian
conjugation, and its scalar part is $\sum_{\mu}P_{\mu}\overline{Q_{\mu}}$, positive definite. This article carries
the operator layer of the band: the multiplication operators of this product, the form they are adjoint for, and
the consequences of that adjoint. It answers the question the twelve bands ask, and for this band the answer is the
mirror image of the composition band: the adjoint is taken for the **positive definite** Hermitian form, and it
**conjugates the parameter and keeps the side**, where the adjoint of the composition band swaps the sides.

The article is the sibling of *The Operators of the Ordinary Product: One-Sided, Two-Sided and the Sandwich*, the
operator article of the GPA band, and it carries a layer that article explicitly defers to this band. The composition
band reads its own indefinite plain form and states that self-adjointness for that form is not physical hermiticity;
the observables and the gauge generators of the framework are the self-adjoint and the skew-adjoint operators of the
Hermitian form of this sesquilinear block, and the full interpretation of them is *Observables, Gauge Generators and the
Chirality of the Internal Action*. The rank and the mass are *Mass, Rank and the Positivity of the Dagger*; the
particle types are *Particle Types, Discrete Charge and Three-Particle Couplings*; the state space and its
complement are *The Spinor Space as a Hilbert Space of the General Plain Sesqualgebra* and *The Complementary Space
of the Spinor Space in the General Plain Sesqualgebra*, with the fused reading of the module and the form in *The
Spinor Space as a Module and as a Hilbert Space*. None of these is re-proved here.

The new feature of the band is a **parity asymmetry** with no analogue in the bilinear rows. The left multiplication
of the product is conjugate-linear and the right multiplication is complex-linear, and the two families have
opposite parity in the variable and opposite parity in the parameter at once. Every difference from the composition
band descends from this: the left family does not close under composition, so the band has no operator algebra of
the associative kind, and the left multiplication has no adjoint of the same kind as the right one.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, the relations
$e_k^{2}=-e_0$ and $e_1e_2=e_3$, and central $i$ with $i^{2}=-1$; an element is $\tilde Q=Q_0e_0+\mathbf Q$ with
complex coefficients. The Hermitian conjugation is ${}^{*}$ with $Q^{*}_{\nu}=\varepsilon_{\nu}\overline{Q_{\nu}}$
and $\varepsilon=(1,-1,-1,-1)$; the natural conjugation is ${}^{\natural}$. The sectors are
$\mathbb{M}_+=\{\tilde Q^{*}=\tilde Q\}$ (informational) and $\mathbb{M}_-=\{\tilde Q^{*}=-\tilde Q\}$ (material),
and the unitary slice is $U=\{\tilde U:\tilde U\tilde U^{*}=e_0\}$. The scalar part is $\mathrm{Sc}$, the trace is
$\mathrm{Tr}=2\,\mathrm{Sc}$, and the matrix model $\mathsf{M}_2$ has $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$ for the biquaternion
norm $N(\tilde Q)=\sum_{\mu}Q_{\mu}^{2}$.

## The Two Multiplication Operators and Their Parity

The product carries one multiplication operator for each slot, and the two are not of the same kind.

**Definition.** For $\tilde A\in\mathbb{B}$ the **left multiplication** and the **right multiplication** of the
plain sesquilinear product are

$$
L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X=\tilde A\tilde X^{*},\qquad
R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A=\tilde X\tilde A^{*}.
$$

They are the biquaternion instance of the two multiplication operators of a sesqualgebra, *The Left and Right
Multiplication Operators of a Sesqualgebra*, and their biquaternion determination is *The Left and Right
Multiplications of the Biquaternion Sesqualgebra*. Alongside them this article uses the **ordinary one-sided
operators of the algebra**, $L_{\tilde A}(\tilde X)=\tilde A\tilde X$ and $R_{\tilde A}(\tilde X)=\tilde X\tilde A$,
which are the operators of *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*. The two pairs
are related by the involution, $L^{\star}_{\tilde A}=L_{\tilde A}\circ{}^{*}$ and $R^{\star}_{\tilde A}=R_{\tilde A^{*}}$.

**Theorem (the opposite parities).** For every $\lambda\in\mathbb{C}$ and every $\tilde X\in\mathbb{B}$,

$$
L^{\star}_{\tilde A}(\lambda\tilde X)=\overline{\lambda}\,L^{\star}_{\tilde A}(\tilde X),\qquad
L^{\star}_{\lambda\tilde A}=\lambda\,L^{\star}_{\tilde A},\qquad
R^{\star}_{\tilde A}(\lambda\tilde X)=\lambda\,R^{\star}_{\tilde A}(\tilde X),\qquad
R^{\star}_{\lambda\tilde A}=\overline{\lambda}\,R^{\star}_{\tilde A}.
$$

The left multiplication is conjugate-linear in the variable and complex-linear in the parameter; the right
multiplication is complex-linear in the variable and conjugate-linear in the parameter.

*Proof.* The involution is conjugate-linear and $\mathbb{C}$ is central, so
$L^{\star}_{\tilde A}(\lambda\tilde X)=\tilde A(\lambda\tilde X)^{*} =\tilde A\overline{\lambda}\tilde X^{*}=\overline{\lambda}L^{\star}_{\tilde A}(\tilde X)$, and the variable is read
plainly on the right, so $R^{\star}_{\tilde A}(\lambda\tilde X)=\lambda R^{\star}_{\tilde A}(\tilde X)$. For the
parameters, $L^{\star}_{\lambda\tilde A}=\lambda L^{\star}_{\tilde A}$ and
$R^{\star}_{\lambda\tilde A}(\tilde X)=\tilde X(\lambda\tilde A)^{*} =\overline{\lambda}\,\tilde X\tilde A^{*}=\overline{\lambda}R^{\star}_{\tilde A}(\tilde X)$.

**Read as a physical statement.** The two slots of the Born pairing have opposite polarity: the first slot is read
linearly and the second through the conjugation, and the multiplication operators inherit that polarity. Attaching
on the left conjugates the variable; attaching on the right conjugates the parameter. A bilinear product reads both
slots the same way, so no bilinear row has this behaviour. This is an interpretation: it names the algebraic fact that the
product is $\mathbb{C}$-linear in one argument and conjugate-linear in the other, and it calls that polarity the
bra-and-ket asymmetry of a probability amplitude.

**Proposition (the operators at the unit).** $L^{\star}_{e_0}={}^{*}$, the involution, and
$R^{\star}_{e_0}=\mathrm{id}$, the identity.

*Proof.* $L^{\star}_{e_0}(\tilde X)=e_0\tilde X^{*}=\tilde X^{*}$ and
$R^{\star}_{e_0}(\tilde X)=\tilde Xe_0^{*}=\tilde X$.

**Read as a physical statement.** The two extreme actions of the product are the conjugation and the identity, one
on each side, and the neutral operation is a right multiplication. The product has a one-sided unit, and the
operator form of that one-sidedness is this display. This is an interpretation of the asymmetry of the product's unit.

## The Composition of the Operators

The product is not associative, and the composition of its operators records exactly where associativity fails.

**Theorem (the composition laws).** For all $\tilde A,\tilde B\in\mathbb{B}$,

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A,\tilde B^{*}},\qquad
R^{\star}_{\tilde A}R^{\star}_{\tilde B}=R^{\star}_{\tilde A\tilde B},
$$
$$
L^{\star}_{\tilde A}R^{\star}_{\tilde B}=L^{\star}_{\tilde A\tilde B},\qquad
R^{\star}_{\tilde A}L^{\star}_{\tilde B}=S_{\tilde B,\tilde A},
$$

where $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ is the ordinary two-sided multiplication (the sandwich of the crossing reader) and
$S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ is the sesquilinear sandwich of *The Sesquilinear
Sandwich on the Biquaternions*.

*Proof.* Each is a direct computation with $(uv)^{*}=v^{*}u^{*}$. The first is
$L^{\star}_{\tilde A}L^{\star}_{\tilde B}(\tilde X)=\tilde A(\tilde B\tilde X^{*})^{*} =\tilde A\tilde X\tilde B^{*}=T_{\tilde A,\tilde B^{*}}(\tilde X)$; the second is
$R^{\star}_{\tilde A}R^{\star}_{\tilde B}(\tilde X)=(\tilde X\tilde B^{*})\tilde A^{*} =\tilde X(\tilde A\tilde B)^{*}=R^{\star}_{\tilde A\tilde B}(\tilde X)$; the third is
$L^{\star}_{\tilde A}R^{\star}_{\tilde B}(\tilde X)=\tilde A\tilde B\tilde X^{*} =L^{\star}_{\tilde A\tilde B}(\tilde X)$; the fourth is
$R^{\star}_{\tilde A}L^{\star}_{\tilde B}(\tilde X)=\tilde B\tilde X^{*}\tilde A^{*} =S_{\tilde B,\tilde A}(\tilde X)$.

**Corollary (the right family closes, the left one does not).** The right multiplications are closed under
composition, contain the identity $R^{\star}_{e_0}$, and form a monoid isomorphic to the multiplicative monoid
$(\mathbb{B},\cdot)$ under $\tilde A\mapsto R^{\star}_{\tilde A}$. The left multiplications are not closed: the
composite of two of them is the complex-linear two-sided multiplication $T_{\tilde A,\tilde B^{*}}$, which is a left
multiplication only when it vanishes, and the left family contains no identity. The four families
$\{L^{\star}\}$, $\{R^{\star}\}$, $\{S\}$, $\{T\}$ generate the monoid of the product, with identity
$R^{\star}_{e_0}=T_{e_0,e_0}=\mathrm{id}$.

**Read as a physical statement.** The product composes on the right exactly as the algebra does, and it does not
compose on the left, because the left slot carries the conjugation. This is an interpretation: it says that the probability
structure retains the composability of the algebra on one side only, and that the two-sided multiplication $T$ is
the residue of the failure on the other side.

**Corollary (no single representation).** Let $\tilde A\neq0$. No complex-linear representation of the algebra
contains $L^{\star}_{\tilde A}$: a complex-linear operator cannot equal a nonzero conjugate-linear one. Consequently
the band has no enveloping operator algebra of the associative kind, and what it has instead is the four-family
monoid of the previous corollary.

*Proof.* The parity theorem gives the obstruction, and the argument is the one of *The Left and Right Multiplication
Operators of a Sesqualgebra*, §*The Failure of a Single Linear Representation*, whose biquaternion instance is *The
Left and Right Multiplications of the Biquaternion Sesqualgebra*.

**Read as a physical statement.** The composition band recovers its algebra from the action,
$\mathbb{B}^{\mathrm{e}}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ with two commuting families. This band does not:
the parity mismatch forbids a single linear representation, and the action recovers the sesqualgebra only through
two families and a two-sided residue. This is an interpretation, and it is the operator form of the statement that the
sesquilinear product is not associative.

## The Form and the Adjoint: the Side Is Kept and the Parameter Conjugated

The product has a positive definite form, its scalar part, and the adjoint is taken for it.

**The form.** The **Born pairing** is

$$
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}\bigl(\tilde P\star\tilde Q\bigr)
=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)=\sum_{\mu=0}^{3}P_{\mu}\overline{Q_{\mu}},
$$

$\mathbb{C}$-linear in the first argument and conjugate-linear in the second, of Gram matrix the identity in the
basis $e_0,e_1,e_2,e_3$, and **positive definite**. It is the canonical Hermitian form of the regular module, *The
Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*, and it is the same form as
$(\tilde T,\tilde V)=\mathrm{Sc}(\tilde T^{*}\tilde V)$ of the one-sided article read with the arguments exchanged,
$\langle\tilde P,\tilde Q\rangle_{*}=\overline{(\tilde P,\tilde Q)}$.

**Definition (the adjoint).** For a complex-linear operator $T$ the **adjoint** is defined by

$$
\langle T\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,T^{\dagger}\tilde Q\rangle_{*}
\qquad\text{for all }\tilde P,\tilde Q .
$$

The form is positive definite, hence non-degenerate, so the adjoint exists and is unique. For a conjugate-linear
operator $S$ the linear rule has no solution, and the **twisted adjoint** is used instead,
$\langle S\tilde P,\tilde Q\rangle_{*}=\overline{\langle\tilde P,S^{\dagger}\tilde Q\rangle_{*}}$, under which the
adjoint of a conjugate-linear operator is again conjugate-linear. Both rules are *The Sesquilinear Adjoint
Operator*, whose individual biquaternion instances are *The Adjoint of the Conjugate Left Multiplication* and *The
Adjoint of the Sesquilinear Sandwich on the Biquaternions*.

**Theorem (the adjoint of the linear one-sided operators).** For every $\tilde A\in\mathbb{B}$,

$$
(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}},\qquad (R_{\tilde A})^{\dagger}=R_{\tilde A^{*}},\qquad
(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}} .
$$

The adjoint **keeps the side and conjugates the parameter**.

*Proof.* For the left multiplication, and for $\tilde P,\tilde Q\in\mathbb{B}$, the anti-involution property of the
dagger and the cyclicity of the scalar part give
$\langle L_{\tilde A}\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde A\tilde P\tilde Q^{*}) =\mathrm{Sc}(\tilde P\tilde Q^{*}\tilde A)=\langle\tilde P,L_{\tilde A^{*}}\tilde Q\rangle_{*}$. The right family
is the same computation with $(\tilde P\tilde A)^{*}=\tilde A^{*}\tilde P^{*}$, and the third identity follows from
the second and $R^{\star}_{\tilde A}=R_{\tilde A^{*}}$.

**Read as a physical statement.** Transporting an operation across the Born pairing conjugates its parameter and
does not move it to the other side; a left attachment stays a left attachment. This is an interpretation of a proof, and it
is the physical hermiticity the composition band defers to this one: the parameter is read as a charge or a phase,
and the adjoint reverses it. The type of the operator is decided by the type of one parameter, which is what the
next section uses.

**Theorem (the adjoint of the conjugate-linear left multiplication).** For every $\tilde A\in\mathbb{B}$,

$$
(L^{\star}_{\tilde A})^{\dagger}=S_{e_0,\tilde A^{*}},\qquad S_{e_0,\tilde A^{*}}(\tilde X)=\tilde X^{*}\tilde A .
$$

The left family is not stable under the adjoint: it leaves the family, and its image is the conjugate-linear family
of sandwiches. In particular $L^{\star}_{\tilde A}$ is twisted-self-adjoint exactly for a central $\tilde A$, and
twisted-skew-adjoint only for $\tilde A=0$.

*Proof.* For $\tilde P,\tilde Q$,
$\langle L^{\star}_{\tilde A}\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde A\tilde P^{*}\tilde Q^{*})$, while
$\overline{\langle\tilde P,\tilde Q^{*}\tilde A\rangle_{*}}=\mathrm{Sc}(\tilde P^{*}\tilde Q^{*}\tilde A)$, and the
two agree by the cyclicity $\mathrm{Sc}(\tilde A\tilde P^{*}\tilde Q^{*}) =\mathrm{Sc}(\tilde P^{*}\tilde Q^{*}\tilde A)$. Twisted-self-adjointness is then
$\tilde X^{*}\tilde A=\tilde A\tilde X^{*}$ for every $\tilde X$, which is centrality of $\tilde A$, and
twisted-skew-adjointness at $\tilde X=e_0$ reads $\tilde A=-\tilde A$.

**Read as a physical statement.** The two slots of the form do not receive adjoints of the same kind, because the
two multiplication operators are not of the same kind. The right attachment has a right attachment as its adjoint;
the left attachment has not, and its adjoint is a two-sided operation. This is an interpretation of the parity asymmetry of
the product at the level of the adjoint.

**Corollary (the contrast with the composition band).** The adjoint of this band is a **Hermitian adjoint** for a
positive definite form: it conjugates the parameter and keeps the side. The adjoint of the composition band is a
**transpose** for the indefinite plain bilinear form: it keeps the parameter and swaps the sides,
$(L_{\tilde A})^{\approx}=R_{\tilde A}$, of *The Operators of the Ordinary Product*. The type criteria are on
**one parameter** here and on the **product of two parameters** there, and the block-by-block comparison is the
crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of
the twelve.

**Theorem (the adjoint of the two-sided and sandwich operators).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
(T_{\tilde P,\tilde Q})^{\dagger}=T_{\tilde P^{*},\tilde Q^{*}},\qquad
(S_{\tilde P,\tilde Q})^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}},\qquad
(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{*}},
$$

where $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ is the Hermitian sandwich.

*Proof.* For $T$ the defining identity is the cyclic computation applied to both slots. For $S$, the composite
$S_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$ has a conjugate-linear adjoint, and the twisted rule
gives $(S_{\tilde P,\tilde Q})^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$, the two parameters exchanging as well as
conjugating; it is *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*. For $\Theta$ this is the case
$\tilde P=\tilde Q$ together with $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$, of *Two-Sided Operators on the
General Plain Sesqualgebra of Biquaternions*.

**Read as a physical statement.** A two-sided operation keeps its two sides under the adjoint and conjugates both
parameters; a sandwich exchanges them, so the adjoint reads the sandwich and its mirror image as a pair. This is a
interpretation of the anti-automorphism property $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$ of the twisted adjoint.

## The Types of the Operators: Observables and Generators

The type criteria are criteria on one parameter.

**Theorem (the linear types).** For $\tilde A\in\mathbb{B}$, and equally with $R_{\tilde A}$ or
$R^{\star}_{\tilde A}$ in place of $L_{\tilde A}$,

$$
L_{\tilde A}\ \text{self-adjoint}\iff\tilde A\in\mathbb{M}_+,\qquad
L_{\tilde A}\ \text{skew-adjoint}\iff\tilde A\in\mathbb{M}_-,\qquad
L_{\tilde A}\ \text{unitary}\iff\tilde A\in U .
$$

*Proof.* By the adjoint theorem $L_{\tilde A}^{\dagger}=L_{\tilde A^{*}}$, and $\tilde A\mapsto L_{\tilde A}$ is
injective, so $L_{\tilde A}^{\dagger}=L_{\tilde A}$ is $\tilde A^{*}=\tilde A$ and
$L_{\tilde A}^{\dagger}=-L_{\tilde A}$ is $\tilde A^{*}=-\tilde A$. Unitarity is
$L_{\tilde A}^{\dagger}L_{\tilde A}=L_{\tilde A^{*}\tilde A}=\mathrm{id}$, that is $\tilde A^{*}\tilde A=e_0$,
equivalent to $\tilde A\in U$ for invertible $\tilde A$. The right-hand computations are identical.

**Corollary (the observables and the generators).** The Hermitian and the anti-Hermitian parameters give the
self-adjoint and the skew-adjoint operators, $L_{\mathbb{M}_+}=\text{self-adjoint operators}$ and
$L_{\mathbb{M}_-}=\text{skew-adjoint operators}$, alongside the unitary operators $L_U$; and the slice exponentiates
inside the family, $e^{L_{\tilde S}}=L_{e^{\tilde S}}$ for $\tilde S\in\mathbb{M}_-$, whose exponential lies in $U$.

*Proof.* The type display gives the first statement; for the second, the exponential series and the linearity of
$\tilde B\mapsto L_{\tilde B}$ commute, and the exponential of an anti-Hermitian element is unitary.

**Read as a physical statement.** The **observables** of the framework are the self-adjoint operators of this form
and the **gauge generators** are the skew-adjoint ones, one for each parameter of the corresponding sector: the
Hermitian elements act by observables and the anti-Hermitian elements by generators. This is an interpretation, and it is
why this article is the owner of the physical adjoint that the composition band cites: the plain bilinear form of
that band is indefinite, and hermiticity is a property of this positive form. The gauge group, its compactness and
the chirality of the one-sided action are *Observables, Gauge Generators and the Chirality of the Internal Action*
and are not repeated here.

**Remark (the conjugate-linear types).** The conjugate-linear left multiplication is not a source of observables or
generators: its twisted-self-adjoint parameters are the central elements and its twisted-skew family is trivial, so
the two type classes are carried by the linear one-sided operators alone.

**Theorem (the two-sided and sandwich types).** Let $\tilde Q\in\mathbb{B}$ be nonzero. Then

$$
\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q}\iff
\tilde Q^{*}=\omega\tilde Q\ \text{for some }\omega\in\mathbb{C}\ \text{with}\ \lvert\omega\rvert=1 ,
$$

$\Theta_{\tilde Q}$ is never skew-adjoint, and both sectors give the same operator,
$\Theta_{\mathbb{M}_+}=\Theta_{\mathbb{M}_-}$.

*Proof.* By the adjoint theorem $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q^{*}}$, and by the kernel theorem of
*Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* the assignment is injective up to a
central phase; the criterion is the theorem there. The sectors give the same operator because
$\tilde Q\in\mathbb{M}_-$ gives $\tilde Q^{*}=-\tilde Q$ and $\Theta_{-\tilde Q}=\Theta_{\tilde Q}$ by the
central-phase invariance.

**Read as a physical statement.** The two-sided operator of the band is symmetric for the Born pairing exactly when
its parameter is Hermitian up to a phase, so the measurement update, whose parameter is a Hermitian idempotent, and
the material conjugation, whose parameter is anti-Hermitian, both qualify, and they give the same operator. This
differs from the composition band, where the sandwich criterion is membership in one sector; here the parameter
enters twice, the sign that separates the sectors is squared away, and the criterion becomes Hermitian-up-to-phase.
This is an interpretation.

## The Symmetries of the Form and of the Product

**Theorem (the form-preserving one-sided operators).** The left multiplication preserves the Born pairing,
$\langle L_{\tilde A}\tilde P,L_{\tilde A}\tilde Q\rangle_{*}=\langle\tilde P,\tilde Q\rangle_{*}$ for all
$\tilde P,\tilde Q$, if and only if $\tilde A\in U$; the same criterion holds on the right and for the product's
right multiplication. The preserving operators are then the unitary operators of the slice.

*Proof.* By the adjoint theorem,
$\langle L_{\tilde A}\tilde P,L_{\tilde A}\tilde Q\rangle_{*} =\langle\tilde P,L_{\tilde A^{*}\tilde A}\tilde Q\rangle_{*}$, which equals $\langle\tilde P,\tilde Q\rangle_{*}$ for
all $\tilde P,\tilde Q$ exactly when $\tilde A^{*}\tilde A=e_0$, that is $\tilde A\in U$.

**Theorem (the multiplicative operators and the product).** The ordinary one-sided operator $L_{\tilde A}$ is
multiplicative for the algebra product if and only if $\tilde A$ is central. The two-sided operator $\Theta_{\tilde Q}$ is an algebra automorphism if and only if $\tilde Q\in U$, and then $\Theta_{\tilde Q}=\mathrm{Ad}_{\tilde Q}$,
the inner automorphism. For a unitary $\tilde U$ the inner automorphism preserves the sesquilinear product as well
as the form, $\mathrm{Ad}_{\tilde U}(\tilde P\star\tilde Q) =\mathrm{Ad}_{\tilde U}(\tilde P)\star\mathrm{Ad}_{\tilde U}(\tilde Q)$.

*Proof.* Multiplicativity of $L_{\tilde A}$ reads $\tilde A\tilde P\tilde Q=(\tilde A\tilde P)(\tilde A\tilde Q)$
for all $\tilde P,\tilde Q$, that is $\tilde A\tilde P=\tilde P\tilde A$ for all $\tilde P$, which is centrality;
the automorphism statement is *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, §*The
Automorphisms*. For the sesquilinear product,
$\Theta_{\tilde U}(\tilde P\star\tilde Q)=\tilde U\tilde P\tilde Q^{*}\tilde U^{*} =(\tilde U\tilde P\tilde U^{-1})(\tilde U\tilde Q\tilde U^{-1})^{*}$, the second factor because
$\tilde U^{*}=\tilde U^{-1}$ on the slice.

**Read as a physical statement.** The isometries of the Born pairing are the unitary slice, on both sides, and the
same slice consists of the algebra automorphisms. A one-sided operation is an isometry exactly for a unitary
parameter and is a symmetry of the product only for a central one. This is an interpretation of the two criteria; it says
that the physical symmetry of the probability metric is one-sided and compact, and that the full algebra symmetry is
the two-sided inner action.

## The Operators Acting on the State Space: the Born Pairing

The operators act on the simple module, and there the pairing is the norm.

**The state space.** The **spinor module** is the minimal left ideal
$S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde\Upsilon_2\}$, the unique simple left $\mathbb{B}$-module, of
complex dimension two, of *The Spinor Space as a Hilbert Space of the General Plain Sesqualgebra* and *The
Complementary Space of the Spinor Space in the General Plain Sesqualgebra* (its second basis element is written
$\tilde W$ in the companion maths article *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions*).
The algebra acts on it by the left multiplication $L_{\tilde A}s=\tilde A s$, the action is onto the endomorphisms,
and the module form is $\langle t,s\rangle_{*}=\mathrm{Sc}(t s^{*})$, positive definite with Gram matrix
$\tfrac12 I_2$ in the basis $(\tilde\Pi_1,\tilde\Upsilon_2)$ of *Hermitian Modules over the Biquaternion Algebra with
Hermitian Adjoint*.

**Proposition (the Born pairing is the scalar part of the product).** For all $\tilde P,\tilde Q$,

$$
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}\bigl(\tilde P\star\tilde Q\bigr),\qquad
\langle\tilde Q,\tilde Q\rangle_{*}=\sum_{\mu}\lvert Q_{\mu}\rvert^{2}>0\quad(\tilde Q\neq0).
$$

On a state $s\in S$ the same form is the module norm, $\langle s,s\rangle_{*}=\mathrm{Sc}(s^{\dagger}s)>0$.

*Proof.* The first display is the definition of the Born pairing as the scalar part of the product; the second is
its diagonal, the Euclidean square of the coefficient vector; the module statement is the restriction of the form to
the ideal.

**Read as a physical statement.** The probability of the framework is a **product**: the amplitude of a state in
another is the scalar part of the band's product, and the probability is its squared modulus over the two norms.
The norm is positive definite, so no state of the module has negative probability, and the absence of ghosts and
tachyons is the positivity of this form (*Mass, Rank and the Positivity of the Dagger*). This is an interpretation: the
framework reads the scalar part of the product as a probability, it does not derive quantum probability from the
algebra.

**Proposition (the product pairs the carrier and does not act on it).** The product's left multiplication keeps the
carrier on its first basis element, $L^{\star}_{\tilde Q}(\tilde\Pi_1)=\tilde Q\tilde\Pi_1\in S$ for every
$\tilde Q$, and carries the second out of it for generic $\tilde Q$,
$L^{\star}_{\tilde Q}(\tilde\Upsilon_2)=\tilde Q\tilde\Upsilon_1\notin S$, since
$\tilde\Upsilon_2^{*}=\tilde\Upsilon_1$ lies in the complementary ideal $\mathbb{B}\tilde\Pi_2$. The product
therefore **pairs** the state space, taking two states to a scalar, and does not act on it; the acting structure is
the ordinary left multiplication of the paragraph above.

*Proof.* $\tilde\Pi_1^{*}=\tilde\Pi_1$, so the first image is $\tilde Q\tilde\Pi_1$, which lies in the left ideal
$S$; $\tilde\Upsilon_2^{*}=\tilde\Upsilon_1\in\mathbb{B}\tilde\Pi_2$, so the second image has components along
$\tilde\Upsilon_1$ and $\tilde\Pi_2$ for generic $\tilde Q$ and lies outside $S$. The two computations are the
state-space siblings' (*The Spinor Space as a Hilbert Space of the General Plain Sesqualgebra* and *The
Complementary Space of the Spinor Space in the General Plain Sesqualgebra*).

**Read as a physical statement.** The probability structure takes two states to a number and moves no state; the
motion of a state is the ordinary action, and the pairing is not an action. This is an interpretation of the parity
asymmetry at the level of the carrier, and it is the operator form of the fact that the band's product is a pairing
and not a representation.

**Corollary (the polarity is the quantisation datum).** The Born pairing is linear in its first slot and
conjugate-linear in its second, and no other polarity is admitted by the product. A decay therefore has a definite
handedness: the state is the conjugate-linear slot and the observable is the linear one.

**Read as a physical statement.** The two slots of the product are the two slots of a measurement, and their
opposite polarity is the datum that distinguishes a state from an observable. This is an interpretation; it is the operator
form of the fact that the product is sesquilinear and not bilinear, and it is the quantisation datum of the band.

**Proposition (the image of the identity and the cone).** The image of the identity under the two-sided operator is
the sesquilinear square, $\Theta_{\tilde Q}(e_0)=\tilde Q\tilde Q^{*}$, and the set
$\{\tilde Q\tilde Q^{*}:\tilde Q\in\mathbb{B}\}$ is the cone of the positive semidefinite Hermitian elements, with
interior the positive definite ones. The sandwich preserves the cone for every parameter and the unitary slice
permutes it. On the state space the left multiplications are the matrix units of $\mathrm{End}_{\mathbb{C}}(S)$;
the right multiplications commute with them and the nilpotent ones carry the module to the complementary ideal
$\mathbb{B}\tilde\Pi_2$.

*Proof.* The image is the definition; the cone is the positivity of the Gram matrix, *The Canonical Hermitian Form
on the Regular Module of the Biquaternion Algebra*; the cone preservation is
$\Theta_{\tilde Q}(\tilde R\tilde R^{*})=(\tilde Q\tilde R)(\tilde Q\tilde R)^{*}$; the matrix-unit statement is the
completeness of the action (*Bilinear Operators on the General Plain Sesqualgebra of Biquaternions*), and the
nilpotent carriers are computed in *The Complementary Space of the Spinor Space in the General Plain Sesqualgebra*
and *The Spinor Space as a Hilbert Space of the General Plain Sesqualgebra*.

**Read as a physical statement.** The states the algebra produces as squares are the elements of the positive cone
and nothing outside it, so the probability structure and the causal cone of the band are one cone read twice; the
left action is the algebra of the state space and the right action is the family that commutes with it. This is a
interpretation of the positivity, and the cone, the rank and the mass are *Mass, Rank and the Positivity of the Dagger*.

## The Sandwich and the Inner Automorphism

The framework attaches a conjugation to an element in two ways, and the two agree on the compact part.

**Proposition (two parametrisations of one conjugation).** For every unit $\tilde Q$,

$$
\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}},\qquad \mathrm{Ad}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{-1}} .
$$

The sandwich conjugates by the **conjugate** of the parameter and the inner automorphism by its **inverse**; they
agree exactly when $\tilde Q^{*}=\tilde Q^{-1}$, that is on the unitary slice and there alone.

*Proof.* The first display is the definition, the second the inner automorphism; they coincide exactly when the two
right parameters coincide, and the coincidence condition $\tilde Q^{*}=\tilde Q^{-1}$ is the defining equation of
the slice.

**Theorem (both preserve the interval and differ on a boost).** Let $\tilde\Lambda$ be Hermitian of unit natural
norm. Then $\Theta_{\tilde\Lambda}$ is self-adjoint, the inner automorphism $\mathrm{Ad}_{\tilde\Lambda}$ is defined,
and the two operators differ on the vector directions: the sandwich rotates them hyperbolically and the inner
automorphism fixes them. A generic such parameter is not unitary.

*Proof.* Hermiticity gives $\tilde\Lambda^{*}=\tilde\Lambda$, so $\Theta_{\tilde\Lambda}$ is self-adjoint by the
sandwich criterion with $\omega=1$. The unit natural norm makes $\mathrm{Ad}_{\tilde\Lambda}$ well defined, and the
difference is the worked case.

**Read as a physical statement.** The framework attaches a conjugation to an element in two ways, and the two agree
only on the compact part of the parameter group. The Lorentz action is the **conjugate** one,
$\tilde P\mapsto\tilde\Lambda\tilde P\tilde\Lambda^{*}$, and the algebra automorphism is the **inverse** one,
$\tilde P\mapsto\tilde\Lambda\tilde P\tilde\Lambda^{-1}$; on a boost the two differ and on a rotation they coincide,
and the compact subgroup is exactly where "conjugation by the inverse" and "conjugation by the conjugate" are the
same statement. This is an interpretation of the corpus's split between the compact slice and the boost.

## A Worked Case

Take one material parameter,

$$
\tilde Q=ie_0+2e_1\in\mathbb{M}_-,\qquad \langle\tilde Q,\tilde Q\rangle_{*}=5,\qquad N(\tilde Q)=3,\qquad
\tilde Q^{2}=-5e_0+4ie_1 .
$$

Its conjugate is $-\tilde Q$, so the sandwich criterion reads $\omega=-1$ and $\Theta_{\tilde Q}$ is self-adjoint for
the Born pairing, as the type theorem says; equivalently $\Theta_{\tilde Q}=L^{\star}_{\tilde Q}L^{\star}_{\tilde Q}$ is the composite of two left multiplications and it is complex-linear. On the unit,
$\Theta_{\tilde Q}(e_0)=\tilde Q\tilde Q^{*}=-\tilde Q^{2}=5e_0-4ie_1$, a Hermitian element of positive trace, and
the same element is the image of the identity under the operator. The two forms of the block separate on this
parameter: the Born pairing gives the positive value $5$, while the natural square carries $N(\tilde Q)=3$ and the
ordinary square carries $\mathrm{Sc}(\tilde Q^{2})=-5$, the sector sign.

Take next a **boost** parameter,

$$
\tilde\Lambda=\cosh u\,e_0+\sinh u\,ie_1,\qquad \tilde\Lambda=\tilde\Lambda^{*},\qquad
\tilde\Lambda\tilde\Lambda^{\natural}=e_0,\qquad \tilde\Lambda\tilde\Lambda^{*}
=\cosh 2u\,e_0+\sinh 2u\,ie_1 .
$$

The parameter is Hermitian and of unit natural norm but not unitary, so the sandwich is self-adjoint and the inner
automorphism is defined while the parameter is not in the compact slice. On $e_1$ the two conjugations separate,

$$
\Theta_{\tilde\Lambda}(e_1)=\tilde\Lambda e_1\tilde\Lambda^{*}=\tilde\Lambda^{2}e_1
=\cosh 2u\,e_1-i\sinh 2u\,e_0,\qquad \mathrm{Ad}_{\tilde\Lambda}(e_1)=e_1 .
$$

The sandwich moves $e_1$ by a hyperbolic rotation and the inner automorphism leaves it fixed; the difference is the
non-compact part of the parameter, displayed on one element, and it vanishes as $u\to0$.

The same verdict holds for a **measurement** parameter, $\tilde\Pi=\tfrac12(e_0+ie_1)$, a Hermitian idempotent,
$\tilde\Pi^{2}=\tilde\Pi=\tilde\Pi^{*}\in\mathbb{M}_+$, self-adjoint by the criterion with $\omega=+1$. The three
parameters separate the two questions the band asks of an operator: **which form it is symmetric for** and **which
motion it generates**.

**A numerical check.** Recomputing with biquaternions in the $2\times2$ matrix model, to machine precision over
random elements: the pairing equals $\sum_{\mu}P_{\mu}\overline{Q_{\mu}}$ with Gram matrix the identity; $L^{\star}$
is conjugate-linear and $R^{\star}$ complex-linear; the four composition laws hold, the right family closes and the
left family leaves the family onto $T$; the adjoints satisfy $(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$,
$(R_{\tilde A})^{\dagger}=R_{\tilde A^{*}}$, $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$,
$(T_{\tilde P,\tilde Q})^{\dagger}=T_{\tilde P^{*},\tilde Q^{*}}$,
$(S_{\tilde P,\tilde Q})^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$ and
$(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{*}}$; the twisted adjoint of $L^{\star}_{\tilde A}$ is
$\tilde X\mapsto\tilde X^{*}\tilde A$; the type criteria hold on random, Hermitian, anti-Hermitian and unitary
parameters; the sandwich criterion holds exactly for the parameters Hermitian up to a phase; the form-preserving
criterion holds exactly at $\tilde A\in U$; the multiplicativity criteria hold exactly at central parameters and at
the slice; the product's left multiplication keeps $\tilde\Pi_1$ in the carrier and carries $\tilde\Upsilon_2$ out of
it; and the worked case was checked coefficient by coefficient.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must
declare.

- **The composition laws are not re-proved here.** They are *The Left and Right Multiplications of the Biquaternion
  Sesqualgebra*, the biquaternion instance of *The Left and Right Multiplication Operators of a Sesqualgebra*, whose
  general theory is *Sesqualgebras*.
- **The adjoint is not re-proved here.** The general twisted rule is *The Sesquilinear Adjoint Operator*; the
  individual operators are *The Adjoint of the Conjugate Left Multiplication* and *The Adjoint of the Sesquilinear
  Sandwich on the Biquaternions*.
- **The positivity, the rank and the cone are not re-proved here.** They are *Mass, Rank and the Positivity of the
  Dagger*, with the canonical form of *The Canonical Hermitian Form on the Regular Module of the Biquaternion
  Algebra* and the norm of *Norm and Invertibility in the General Plain Sesqualgebra*.
- **The observables, the generators and the chirality are not re-read here.** They are *Observables, Gauge
  Generators and the Chirality of the Internal Action*, and the particle content is *Particle Types, Discrete Charge
  and Three-Particle Couplings*. This article is the owner of the physical adjoint that the composition band cites,
  and it declares that ownership; it does not re-read the chirality.
- **The comparison of the twelve rows is not this article.** It is the crossing reader *The Operators of the Twelve
  Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve.

**What the framework does not claim.** The interpretation does not derive the Born rule, the measurement postulate or
quantum probability from the algebra; it reads the scalar part of the product as a probability amplitude and names
the two slots. It does not claim that the positive form of this band is the only positivity of the corpus, the
indefinite companion being the business of the Krein articles. And it does not claim that the operator theory of the
twelve rows is one theory: the general plain bilinear row alone carries an enveloping operator algebra, and the
parity asymmetry of this row is its own.

## The Ledger

**Proved.** The plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ has two multiplication
operators, $L^{\star}_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ and
$R^{\star}_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$, conjugate-linear and complex-linear respectively, with
opposite parity in the variable and in the parameter; the unit gives $L^{\star}_{e_0}={}^{*}$ and
$R^{\star}_{e_0}=\mathrm{id}$; the composition laws $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A,\tilde B^{*}}$, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=R^{\star}_{\tilde A\tilde B}$,
$L^{\star}_{\tilde A}R^{\star}_{\tilde B}=L^{\star}_{\tilde A\tilde B}$ and
$R^{\star}_{\tilde A}L^{\star}_{\tilde B}=S_{\tilde B,\tilde A}$ hold, the right family closes and the left family
does not, and no nonzero left multiplication lies in a complex-linear representation, so the band has no enveloping
operator algebra of the associative kind; the Born pairing
$\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ is positive definite of Gram matrix the
identity; the adjoint for it exists and is unique, conjugates the parameter and keeps the side,
$(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$, $(R_{\tilde A})^{\dagger}=R_{\tilde A^{*}}$ and
$(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$, while the conjugate-linear left multiplication is not
stable and has the sandwich $S_{e_0,\tilde A^{*}}$ as its twisted adjoint; a linear one-sided operator is
self-adjoint exactly for a Hermitian parameter, skew-adjoint exactly for an anti-Hermitian one and unitary exactly
for a parameter of the slice, so the observables and the generators are the Hermitian and the anti-Hermitian
parameters; a two-sided operator keeps its two sides and conjugates both parameters, and a sandwich exchanges them,
the sandwich criterion being $\tilde Q$ Hermitian up to a phase for self-adjointness and $\tilde Q=0$ for
skew-adjointness; the form-preserving one-sided operators are exactly the unitary slice, the multiplicative ones
exactly the central parameters, and the two-sided automorphisms exactly the slice, where the sandwich and the inner
automorphism agree; the image of the identity is the sesquilinear square and the cone of the positive semidefinite
Hermitian elements; and the left actions on the state space are the matrix units while the right actions commute
with them. The worked case gives $\tilde Q=ie_0+2e_1$ with $\langle\tilde Q,\tilde Q\rangle_{*}=5$, $N(\tilde Q)=3$
and $\Theta_{\tilde Q}(e_0)=5e_0-4ie_1$, and the boost $\tilde\Lambda=\cosh u\,e_0+\sinh u\,ie_1$ with
$\Theta_{\tilde\Lambda}(e_1)=\cosh 2u\,e_1-i\sinh 2u\,e_0$ against $\mathrm{Ad}_{\tilde\Lambda}(e_1)=e_1$.

**Interpretations.** That the two slots of the product have opposite polarity, so the left family is conjugate-linear and
the right one complex-linear; that a probability amplitude has one linear and one anti-linear slot, a bra and a ket;
that the adjoint conjugates the charge and keeps the side, so the observables and the generators are the Hermitian
and the anti-Hermitian parameters; that the left family has no identity and no single representation, so the
probability structure composes on one side only; that the symmetries of the Born pairing are the unitary slice and
that the compact slice is where the sandwich and the inner automorphism coincide; and that the probability metric
and the causal cone are one positive cone read twice. Each is the framework's naming of a proved algebraic fact and
is labelled as such.

## Physical Readings

The plain sesquilinear product is the framework's probability structure, and its operators read as the two ways of
attaching an operation to a state with opposite polarity. The left attachment conjugates the variable and the right
attachment conjugates the parameter, and the asymmetry is the bra-and-ket asymmetry of a probability amplitude: the
first slot of the product is the linear one and the second the conjugate-linear one, and the two slots are the state
and the observable. The adjoint of the band is the Hermitian adjoint of the positive form, and it conjugates the
charge of the parameter without moving the operation to the other side; the self-adjoint operators are the
observables and the skew-adjoint ones the generators, which is why the physical hermiticity of the framework lives
in this band and not in the indefinite plain form of the composition band. The right family composes and the left
does not, and the band's interpretation of that is that a probability structure is one-sided in its composition while it is
two-sided in its action: the two-sided operations are the sandwich and its mirror, and the identity of the
composition is a right multiplication alone. On the state space the Born pairing is the norm, the left actions are
the matrices of the algebra, the nilpotent right actions carry a state to the complement, and the image of the
identity is the cone of positive elements, so the states the algebra produces lie in the forward cone and nowhere
else. Read on the clock, the dagger is the operation that conjugates the phase, and the unitary slice is the
compact part of the parameter group, where the reversible action lives; the boost is the non-compact part, where the
sandwich and the inner automorphism separate. The particle content of the same operator layer, the compactness of
the internal group and the discreteness of its charges are *Particle Types, Discrete Charge and Three-Particle
Couplings*.

## Summary

The operators of the plain sesquilinear product are the left and the right multiplications
$L^{\star}_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ and
$R^{\star}_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$. The left one is conjugate-linear and the right one
complex-linear, and the two families have opposite parity in the variable and in the parameter at once; this
asymmetry is the defining feature of the band and has no analogue in the bilinear rows. The right family closes
under composition, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=R^{\star}_{\tilde A\tilde B}$, and contains the
identity; the left family does not, $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A,\tilde B^{*}}$, and the
composite of two left multiplications is the two-sided multiplication $T$, so there is no single representation and
no enveloping operator algebra of the associative kind, against the composition band where
$L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ and
$\mathbb{B}^{\mathrm{e}}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. The form of the band is the Born pairing
$\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_{\mu}P_{\mu}\overline{Q_{\mu}}$, positive
definite of Gram matrix the identity, and the adjoint for it **conjugates the parameter and keeps the side**,
$(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$, $(R_{\tilde A})^{\dagger}=R_{\tilde A^{*}}$ and
$(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$; the conjugate-linear left multiplication is the single
exception, and its twisted adjoint is the sandwich $S_{e_0,\tilde A^{*}}$. So the type criteria are criteria on one
parameter: the self-adjoint operators are the Hermitian parameters, the observables, and the skew-adjoint ones the
anti-Hermitian parameters, the generators; the unitary parameters give the isometries of the form and the inner
automorphisms of the product, and the compact slice is where the sandwich and the inner automorphism agree. The
two-sided operator is self-adjoint exactly when its parameter is Hermitian up to a phase, both sectors giving the
same operator, and it is never skew. On the state space the Born pairing is the norm, the left actions are the
matrix units of the algebra, and the cone of the positive elements is the image of the identity. The contrast with
the composition band is the point of the pair: there the adjoint is a transpose that swaps the sides, here it is a
Hermitian adjoint that keeps them. What is proved is the algebra; what is proposed is the naming.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | The plain sesquilinear product |
| $L^{\star}_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ | Left multiplication; conjugate-linear in the variable |
| $R^{\star}_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$ | Right multiplication; complex-linear in the variable |
| $L_{\tilde A}$, $R_{\tilde A}$ | The ordinary one-sided operators of the algebra |
| $L^{\star}_{\tilde A}=L_{\tilde A}\circ{}^{*}$, $R^{\star}_{\tilde A}=R_{\tilde A^{*}}$ | The two families related |
| $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ | The two-sided multiplication |
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ | The sesquilinear sandwich |
| $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The Hermitian sandwich |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=T_{\tilde A,\tilde B^{*}}$ | The left family does not close |
| $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=R^{\star}_{\tilde A\tilde B}$ | The right family closes |
| $L^{\star}_{\tilde A}R^{\star}_{\tilde B}=L^{\star}_{\tilde A\tilde B}$, $R^{\star}_{\tilde A}L^{\star}_{\tilde B}=S_{\tilde B,\tilde A}$ | The mixed composites |
| $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | The Born pairing; positive definite, Gram identity |
| $T^{\dagger}$ | The adjoint for the Born pairing, $\langle T\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,T^{\dagger}\tilde Q\rangle_{*}$ |
| $(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$, $(R_{\tilde A})^{\dagger}=R_{\tilde A^{*}}$ | The adjoint keeps the side and conjugates the parameter |
| $(L^{\star}_{\tilde A})^{\dagger}=S_{e_0,\tilde A^{*}}$ | The twisted adjoint of the conjugate-linear left multiplication |
| $(T_{\tilde P,\tilde Q})^{\dagger}=T_{\tilde P^{*},\tilde Q^{*}}$, $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{*}}$ | The two-sided and sandwich adjoints |
| Self-adjoint $\iff\tilde A\in\mathbb{M}_+$; skew $\iff\tilde A\in\mathbb{M}_-$; unitary $\iff\tilde A\in U$ | The type criteria on one parameter |
| $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q}\iff\tilde Q^{*}=\omega\tilde Q$, $\lvert\omega\rvert=1$ | The sandwich criterion; both sectors give the same operator |
| $L_{\tilde A}$ preserves $\langle\cdot,\cdot\rangle_{*}\iff\tilde A\in U$ | The form-preserving operators |
| $\Theta_{\tilde Q}=\mathrm{Ad}_{\tilde Q}\iff\tilde Q\in U$ | The sandwich and the inner automorphism agree on the slice |
| $\mathbb{M}_\pm$, $U$, $\mathsf{M}_2$, $N$ | The sectors, the unitary slice, the matrix model, the biquaternion norm |
| $S=\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The spinor space and its complement |

## Further Reading

- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*
  (`articles_maths/one-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the ordinary
  one-sided operators, the adjoint $(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$, the type criteria and the
  form-preserving theorem.
- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*
  (`articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the Hermitian
  sandwich, its adjoint, the self-adjointness criterion up to central phase, the trivial skew sector, the unitarity
  and the automorphism theorem.
- *The Left and Right Multiplications of the Biquaternion Sesqualgebra*
  (`articles_maths/the-left-and-right-multiplications-of-the-biquaternion-sesqualgebra.md`), for the multiplication
  operators of the product, the two parities, the composition laws and the obstruction to a single representation.
- *The Sesquilinear Sandwich on the Biquaternions*
  (`articles_maths/the-sesquilinear-sandwich-on-the-biquaternions.md`), for $S_{\tilde P,\tilde Q}$, its composition
  table, its rank and its kernel.
- *The Sesquilinear Adjoint Operator* (`articles_maths/the-sesquilinear-adjoint-operator.md`), for the sesquilinear
  pairing, the twisted adjoint of a conjugate-linear operator, and the adjoints
  $R_{b}^{\dagger}=R_{b^{*}}$, $L_{a}^{\dagger}=S_{1,a}$, $S_{a,b}^{\dagger}=S_{b,a}$ and
  $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$.
- *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions*
  (`articles_maths/bilinear-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the spinor
  module, the module form with Gram matrix $\tfrac12 I_2$, and the completeness of the action.
- *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*
  (`articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternion-algebra.md`), for the
  positive form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and its structures.
- *The Operators of the Ordinary Product: One-Sided, Two-Sided and the Sandwich*
  (`articles_physics/the-operators-of-the-ordinary-product-one-sided-two-sided-and-the-sandwich.md`), the
  composition band sibling, for the adjoint that swaps the sides and the deferral of the physical adjoint to this
  band.
- *The Spinor Space as a Hilbert Space of the General Plain Sesqualgebra* and *The Complementary Space of the Spinor
  Space in the General Plain Sesqualgebra* (`articles_physics/`), the two state-space siblings of the band, for the
  form, the norm, the Born rule and the complement of the carrier; with the fused interpretation *The Spinor Space as a
  Module and as a Hilbert Space*.
- *Mass, Rank and the Positivity of the Dagger*, *Observables, Gauge Generators and the Chirality of the Internal
  Action* and *Particle Types, Discrete Charge and Three-Particle Couplings*
  (`articles_physics/`), the other members of the band.
- *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*
  (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing
  reader, for the comparison of the twelve rows.

