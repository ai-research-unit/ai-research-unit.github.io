# __The Operators of the Symmetric Quaternionic Sesquilinear Product and the Gauge Metric__

## Introduction

This article is the operator article of the gauge-metric band, the band of *The Gauge Metric as a Product: the Symmetric Quaternionic
Sesquilinear Product* and *Values in No Subspace: Why the Symmetric Gauge Product Is Not a State*. Its product is the **symmetric
quaternionic sesquilinear product**

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)
=\bigl[P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})\bigr]-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P,
$$

and the operators the band attaches to an element are its two one-sided multiplications

$$
L^{\bullet}_{\tilde A}(\tilde X)=\tilde A\bullet\tilde X,\qquad R^{\bullet}_{\tilde A}(\tilde X)=\tilde X\bullet\tilde A .
$$

The answer is one sentence. The form of the band is the **indefinite** Krein form
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ of signature $(1,3)$; the
adjoint the operators carry is the **$J$-adjoint** for $K$ with the fundamental symmetry $J={}^{\natural}$ the natural conjugation; and that
adjoint **keeps the side and conjugates the parameter**: the adjoint of the left multiplication by $\tilde A$ is the left multiplication by
$\tilde A^{\natural}$. This is the operator face of the band's job word **metric**: the form the operators are adjoint for is the indefinite
pairing itself, its algebraic norm $K(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}-\sum_k\lvert Q_k\rvert^{2}$ is the metric, and the product that
carries it is a pairing of the gauge side and not a state.

Two facts organise the article, and the first corrects a phrase that belongs to another band. The symmetrisation gives the product its
**symmetry**, and the symmetry is **conjugate-commutativity**, not commutativity:
$\tilde P\bullet\tilde Q=\overline{\tilde Q\bullet\tilde P}$. The band therefore carries **two** multiplication families and not one, of
**opposite parity**, linked by the coefficientwise conjugation, $L^{\bullet}_{\tilde A}=\bar{\cdot}\circ R^{\bullet}_{\tilde A}$. The band in
which the two families genuinely coincide is the symmetric **plain** band, whose product $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ is
commutative; the gauge band is not that band. The second fact is that neither family closes under composition, so the band has **no operator
algebra**: the left defect is the associator, and the left family is conjugate-linear, so its composite is linear and can never be a left
multiplication off the zero operator.

The article is the quaternionic-sesquilinear sibling of *The Operators of the Ordinary Product: One-Sided, Two-Sided and the Sandwich*, of
*The Operators of the Plain Sesquilinear Product and the Born Pairing* and of *The Operators of the Symmetrised Plain Product: Jordan
Commutativity*, and it states the gauge row of the grid whose comparison is *The Operators of the Twelve Structures: Multiplication, Adjoint
and Bracket*, not one of the twelve. The product and its laws are *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*;
the operators, the parity, the rank, the traces and the automorphisms are *The Multiplication Operators of the Symmetric Quaternionic
Sesqualgebra*; the form $K$ read as a product is *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; the $J$-adjoint
and the $J$-unitary family are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*; and the
sandwich for the same indefinite form is *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*. All
are cited in place and none is re-proved here.

**Conventions.** The conventions are those of *Conventions in the Biquaternion Universe*:
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, the relations $e_k^{2}=-e_0$ and $e_1e_2=e_3$, and
central scalar imaginary $i$ with $i^{2}=-1$; an element is $\tilde Q=Q_0e_0+\mathbf Q$ with complex coefficients, of scalar part
$\mathrm{Sc}(\tilde Q)=Q_0$ and vector part $\mathbf Q=\sum_kQ_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0e_0-\mathbf Q$, the
coefficientwise conjugation is $\bar{\tilde Q}=\sum_\mu\overline{Q_\mu}e_\mu$, and the star is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$.
The invariant form is $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$
with sign vector $\varepsilon=(1,-1,-1,-1)$; the two one-sided actions of $e_0$ are the conjugations, $e_0\bullet\tilde Q=\tilde Q^{*}$ and
$\tilde Q\bullet e_0=\tilde Q^{\natural}$; and the norm is $N(\tilde Q)=\tilde Q^{\natural}\tilde Q=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$.

**A notation caution.** The mathematics block of the product writes it $\tilde P\star\tilde Q$ and its operators
$L^{\star}_{\tilde A},R^{\star}_{\tilde A}$, because in that block it is *the* product. The physics block reserves the mark $\star$ for the
fourth product $\tilde P^{\natural}\tilde Q^{*}$, writes the symmetric half $\bullet$ and the antisymmetric half $\diamond$, and this article
writes the operators $L^{\bullet}_{\tilde A},R^{\bullet}_{\tilde A}$ accordingly. The reader moving between the two blocks should carry the
names $\mathrm{SQS}$ and $\mathrm{AQS}$, not the marks.

## The One Symmetric Product and Its Two Operators

**Definition.** For $\tilde A\in\mathbb{B}$ the **left multiplication** and the **right multiplication** of the symmetric quaternionic
sesquilinear product are $L^{\bullet}_{\tilde A}(\tilde X)=\tilde A\bullet\tilde X$ and
$R^{\bullet}_{\tilde A}(\tilde X)=\tilde X\bullet\tilde A$. They are the biquaternion instance of the two multiplication operators of a
sesqualgebra, determined in *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*. Alongside them this article uses the
ordinary one-sided operators of the algebra, $L_{\tilde A}(\tilde X)=\tilde A\tilde X$ and $R_{\tilde A}(\tilde X)=\tilde X\tilde A$, to
which the two families are reducible by the involution.

**Theorem (the relation of the two families).** For every $\tilde A$ and every $\tilde X$,
$\tilde A\bullet\tilde X=\overline{\tilde X\bullet\tilde A}$, that is $L^{\bullet}_{\tilde A}=C\circ R^{\bullet}_{\tilde A}$ and
$R^{\bullet}_{\tilde A}=C\circ L^{\bullet}_{\tilde A}$, where $C=\bar{\cdot}$ is the coefficientwise conjugation.

*Proof.* The product is $\mathbb{C}$-linear in its first slot and conjugate-linear in its second, so the coefficientwise conjugation
interchanges the two orders; the exchange $\overline{\tilde P^{\natural}\tilde Q^{*}}=\tilde Q^{*}\tilde P^{\natural}$ fixes the half-sum,
which is *The Gauge Metric as a Product*. Reading the two orders at a fixed argument gives the operator identity, and $C$ is an involution.
This is the parity theorem of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

**Read as a physical statement.** The two attachments of the band are not the same act, nor are they independent: attaching a gauge element
on the left is attaching its coefficientwise conjugate on the right, and the conjugation is exactly the symmetry the symmetrisation bought.
The band carries **one** operator family read through the conjugation and **two** parities; the interpretation is that the ordering of the two slots
is immaterial while the conjugation between them is not.

**Corollary (the operators at the unit).** $L^{\bullet}_{e_0}={}^{*}$ is the star conjugation and $R^{\bullet}_{e_0}={}^{\natural}$ the
natural conjugation, with real matrices $\mathrm{diag}(1,-1,-1,-1,-1,1,1,1)$ and $\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$.

*Proof.* The two one-sided actions of the identity are $e_0\bullet\tilde X=\tilde X^{*}$ and $\tilde X\bullet e_0=\tilde X^{\natural}$, *The
Gauge Metric as a Product*; the diagonal matrices are the real matrices of the two conjugations, *The Multiplication Operators of the
Symmetric Quaternionic Sesqualgebra*.

**Read as a physical statement.** The neutral operation of the band is not the identity on either side: the left action of the unit is the
star, the right action is the natural conjugation. The interpretation is that the gauge pairing has no unit of a multiplication, and the two
conjugations are the residues of the unit it lacks.

**Caution (the word commutative).** The symmetrisation makes the product **conjugate-commutative** and it does **not** make it commutative;
the two operators do **not** coincide, they have opposite parity, and a reader who expects the collapse of the two families into one, as
happens for the commutative symmetric **plain** product of *The Operators of the Symmetrised Plain Product: Jordan Commutativity*, will not
find it here. The collapse requires commutativity, and conjugate-commutativity supplies only the link
$L^{\bullet}_{\tilde A}=C\circ R^{\bullet}_{\tilde A}$. The operator content of the metric word is the conjugation that links the two
parities, not a single family.

**Theorem (the parity of the two families).** For every $\lambda\in\mathbb{C}$ and every $\tilde X$ one has
$L^{\bullet}_{\tilde A}(\lambda\tilde X)=\overline{\lambda}\,L^{\bullet}_{\tilde A}(\tilde X)$ and
$L^{\bullet}_{\lambda\tilde A}=\lambda\,L^{\bullet}_{\tilde A}$, while
$R^{\bullet}_{\tilde A}(\lambda\tilde X)=\lambda\,R^{\bullet}_{\tilde A}(\tilde X)$ and
$R^{\bullet}_{\lambda\tilde A}=\overline{\lambda}\,R^{\bullet}_{\tilde A}$. The left multiplication is conjugate-linear in the variable and
complex-linear in the parameter; the right multiplication is complex-linear in the variable and conjugate-linear in the parameter. In
particular $L^{\bullet}_{\lambda e_0}=\lambda\,{}^{*}$ and $R^{\bullet}_{\lambda e_0}=\overline{\lambda}\,{}^{\natural}$.

*Proof.* The natural conjugation is $\mathbb{C}$-linear and the star is conjugate-linear, and the product is linear in its first slot and
conjugate-linear in its second; the four rules are read from the definition as in *The Operators of the Plain Sesquilinear Product and the
Born Pairing*, and the central case follows from the corollary at $e_0$. This is the parity theorem of *The Multiplication Operators of the
Symmetric Quaternionic Sesqualgebra*.

**Read as a physical statement.** The two slots of the gauge pairing have opposite polarity, and a conjugate-linear operator is not an
element of the complex endomorphism algebra. The interpretation is that no family of the band can be a representation of an algebra, so the band
carries its operators without an operator calculus.

**Definition (the value).** For all biquaternions the value of the product is
$\tilde A\bullet\tilde X=K(\tilde A,\tilde X)e_0-A_0\overline{\mathbf X}-\overline{X_0}\mathbf A$, with scalar part the Krein form
$K(\tilde A,\tilde X)$ and vector part the mixed term $-A_0\overline{\mathbf X}-\overline{X_0}\mathbf A$.

*Proof.* The value is the display of *The Gauge Metric as a Product*, §*The Value of the Symmetric Gauge Product*; the scalar part is $K$ and
the vector part the mixed term alone.

**Read as a physical statement.** The operator acts by returning the pairing as a scale and the mixed term as a direction, and the two
projections sit side by side in one value. The interpretation is that the multiplication is a **deformation** of an element and not a rotation or a
translation, its scalar part a conformal factor and its vector part a shear; the name is the sibling's and the algebra is the display.

**Theorem (the composition and the defect of multiplicativity).** The two families do not multiply,
$L^{\bullet}_{\tilde A}\circ L^{\bullet}_{\tilde B}\neq L^{\bullet}_{\tilde A\bullet\tilde B}$ and
$R^{\bullet}_{\tilde A}\circ R^{\bullet}_{\tilde B}\neq R^{\bullet}_{\tilde A\bullet\tilde B}$; the defect of the left composition is the
associator $\tilde A\bullet(\tilde B\bullet\tilde X)-(\tilde A\bullet\tilde B)\bullet\tilde X$. For the left family the inequality is forced
by parity, the composite of two conjugate-linear maps being $\mathbb{C}$-linear while a single left multiplication is conjugate-linear.

*Proof.* The defect of $L^{\bullet}$ at $\tilde X$ is the associator, nonzero on a general triple because the block is not associative; the
defect of $R^{\bullet}$ is the same computation with the factors in the other order. A map that is both $\mathbb{C}$-linear and
conjugate-linear is zero, which forbids a complex-linear representation. This is *The Multiplication Operators of the Symmetric Quaternionic
Sesqualgebra*, §*The Composition and the Defect of Multiplicativity*.

**Read as a physical statement.** Two gauge pairings do not compose to a gauge pairing, and the failure has two independent sources: the
associator, which is the ordinary defect of a non-associative operation, and the parity, which the left family carries alone. The interpretation is
that the metric band supplies a pairing to be transported and not a multiplication to be iterated, and that the transport is the adjoint.

## The Adjoint of the Krein Form

The band's operators are adjoint for the form their product carries as its scalar part, and the form is indefinite. This section states
exactly which form and which adjoint.

**Definition (the form and its fundamental symmetry).** The **Krein form** of the band is
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, with coefficient form
$K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}=P_0\overline{Q_0}-\sum_{k=1}^{3}P_k\overline{Q_k}$ and
$\varepsilon=(1,-1,-1,-1)$. It is Hermitian, non-degenerate, of signature $(1,3)$ over the complex coefficients and $(2,6)$ over the
real parameters, with fundamental decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_K\mathrm{Vect}(\mathbb{B})$ and fundamental symmetry
$J={}^{\natural}$ the natural conjugation, so that $K(\tilde P,\tilde Q)=(\tilde P^{\natural},\tilde Q)=(J\tilde P,\tilde Q)$ for the
definite star form $(\tilde P,\tilde W)=\mathrm{Sc}(\tilde P\tilde W^{*})=\langle\tilde P,\tilde W\rangle_{*}$, which is the positive form of
the probability row.

*Proof.* In the coefficient basis the form is the standard form of signature $(1,3)$, and the natural conjugation is the algebraic norm operator
$\mathrm{diag}(1,-1,-1,-1)$ inserted in the first slot, turning the definite form into the indefinite one; the details are *The Krein Gram
Matrix and the Restrictions of the Form* and *The Fourth Product and Its Indefinite Metric*, and the identity
$K(\tilde P,\tilde Q)=(\tilde P^{\natural},\tilde Q)$ is the fundamental-symmetry relation
$\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P^{\natural},\tilde Q\rangle_{*}$ of *Conventions in the Biquaternion
Universe*.

**Read as a physical statement.** The form of the band is not the positive form of the state row but the indefinite pairing of the gauge row,
and its modulus is a signature and not an error. The interpretation is that the band compares two internal frames without ranking them.

**Definition (the adjoint).** For a complex-linear operator $T$ the **$J$-adjoint**, or **indefinite adjoint**, is the operator $T^{\dagger}$
with $K(T\tilde P,\tilde Q)=K(\tilde P,T^{\dagger}\tilde Q)$ for all $\tilde P,\tilde Q$, that is $T^{\dagger}=JT^{*}J$ with
$J={}^{\natural}$ and $T^{*}$ the adjoint of $T$ for the definite star form, $(\tilde P,T^{*}\tilde Q)=(T\tilde P,\tilde Q)$. The form is
non-degenerate, so the adjoint exists and is unique. For a conjugate-linear operator $S$ the linear rule has
no solution, and the **twisted $J$-adjoint** is used instead, $K(S\tilde P,\tilde Q)=\overline{K(\tilde P,S^{\dagger}\tilde Q)}$, under which
the adjoint of a conjugate-linear operator is again conjugate-linear. Both rules are the indefinite adjoint of *The Indefinite Hermitian
Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*.

**Read as a physical statement.** The adjoint of the band is taken for the **indefinite** form, so it is a $J$-adjoint and not a definite
adjoint; the conjugation on the right of the twisted rule is the correction the conjugate-linearity of the left family forces. The interpretation is
that the transport across the gauge pairing is indefinite and that its fixed points will not be the observables of the positive form.

**Theorem (the adjoint of the left multiplication).** With respect to $K$, for every $\tilde A$ one has
$K(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\bullet}_{\tilde A^{\natural}}\tilde Y)}$, so the adjoint of the left
multiplication by $\tilde A$ is the left multiplication by $\tilde A^{\natural}$: the adjoint **keeps the side and conjugates the parameter
by the natural conjugation**.

*Proof.* This is the compatibility theorem of *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*:
$K(\tilde A\bullet\tilde X,\tilde Y)=\overline{K(\tilde X,\tilde A^{\natural}\bullet\tilde Y)}$, which is the display with the definition of
the left multiplication; the conjugate on the right is the parity correction of the conjugate-linear operator.

**Read as a physical statement.** Transporting a gauge operation across the pairing does not move it to the other side; it replaces the
parameter by its natural conjugation, the fundamental symmetry of the form. The interpretation is that the gauge adjoint is an **involution of the
parameter** and not a charge reversal of the positive row: it reflects the vector directions, and the reflection is the metric's own.

**Theorem (the adjoint of the right multiplication).** With respect to $K$, for every $\tilde A$ one has
$(R^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{\natural}}\circ C$, where $C=\bar{\cdot}$ is the coefficientwise conjugation; the
right multiplication is complex-linear, so this is the adjoint of the **linear** rule,
$K(R^{\bullet}_{\tilde A}\tilde X,\tilde Y)=K(\tilde X,(R^{\bullet}_{\tilde A})^{\dagger}\tilde Y)$. In the twisted sense $C$ is its own
adjoint, $K(C\tilde X,\tilde Y)=\overline{K(\tilde X,C\tilde Y)}$.

*Proof.* The right family is the left family through the coefficientwise conjugation, $R^{\bullet}_{\tilde A}=C\circ L^{\bullet}_{\tilde A}$,
and $C$ is an involution whose twisted adjoint is itself, $C^{\dagger}=C$ because
$K(\overline{\tilde X},\tilde Y)=\overline{K(\tilde X,\overline{\tilde Y})}$. The adjoint of a composite reverses the order whatever the
parities of the factors, $(C\circ L^{\bullet}_{\tilde A})^{\dagger}=(L^{\bullet}_{\tilde A})^{\dagger}\circ C^{\dagger}$; the composite
$R^{\bullet}_{\tilde A}$ is complex-linear, so its adjoint is taken in the linear sense, and substituting the left adjoint gives the display.

**Read as a physical statement.** The right attachment has an adjoint of a mixed kind: a left attachment composed with the coefficientwise
conjugation. The interpretation is the parity of the band at the level of the adjoint: the left family stays inside itself under the adjoint, the
right family does not, and the two statements are the two faces of the conjugate-commutativity.

**Remark (this adjoint against the plain adjoint).** The adjoint of the band keeps the side and conjugates the parameter by the natural
conjugation. The plain algebra's one-sided operators, adjoint for the same indefinite form, obey the other rule,
$(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, of *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of
Biquaternions*: there the adjoint **crosses to the other side** and conjugates by the coefficientwise conjugation. The two rules must not be
exchanged, and they are the operator difference between the plain multiplication and the symmetric sesquilinear multiplication of the same
form.

**Read as a physical statement.** The same indefinite form carries two adjoints, one for each product, and only the pair (form, product)
determines what the adjoint does to the parameter. The interpretation is that the adjoint is a property of an operation and not of a form alone, and
the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* is where the pairings are compared.

## The Types of the Operators

**Theorem (the types for $K$).** For $\tilde A\in\mathbb{B}$, $L^{\bullet}_{\tilde A}$ is self-adjoint for $K$ exactly when
$\tilde A^{\natural}=\tilde A$, that is exactly when $\tilde A\in\mathbb{C}e_0$, and it is skew-adjoint exactly when
$\tilde A^{\natural}=-\tilde A$, that is exactly when $\tilde A\in\mathrm{Vect}(\mathbb{B})$. A self-adjoint left multiplication has a
**central** parameter and a skew-adjoint one has a **pure vector** parameter; a mixed parameter $\tilde A=\lambda e_0+\mathbf A$ with both
parts nonzero is neither.

*Proof.* By the adjoint theorem the adjoint of $L^{\bullet}_{\tilde A}$ is $L^{\bullet}_{\tilde A^{\natural}}$, and
$\tilde A\mapsto L^{\bullet}_{\tilde A}$ is injective because $L^{\bullet}_{\tilde A}(e_0)=\tilde A^{\natural}$; so self-adjointness is
$\tilde A^{\natural}=\tilde A$ and skew-adjointness is $\tilde A^{\natural}=-\tilde A$. The natural conjugation fixes exactly the central
elements and anti-fixes exactly the pure vectors.

**Read as a physical statement.** A self-adjoint gauge multiplication is a multiplication by a central element and a skew-adjoint one a
multiplication by a pure vector. The interpretation is that the symmetric class of the band is the **centre**, the antisymmetric class the **vector
directions**, and that an element mixing a scale with a direction is neither: the two classes do not carve the algebra between them, and the
mixed elements carry both grades.

### The Reality Question

**Proposition (reality is not automatic).** A self-adjoint left multiplication of the band is **not** automatically real: its parameter is
central, $\tilde A=\lambda e_0$ with $\lambda\in\mathbb{C}$, and $\lambda=i$ gives the self-adjoint operator $L^{\bullet}_{ie_0}=i\,{}^{*}$
with a purely imaginary parameter. The condition of self-adjointness is a condition of **type** of the parameter and not of reality; the
self-adjoint operators of the band are the left multiplications by the parameters of the complex line $\mathbb{C}e_0$, and among them the
real ones are the real multiples of the identity.

*Proof.* Self-adjointness is $\tilde A^{\natural}=\tilde A$ by the type theorem, which is centrality and nothing more; a central parameter is
a complex multiple of $e_0$, real or not, and $L^{\bullet}_{ie_0}(\tilde X)=ie_0\bullet\tilde X=i\tilde X^{*}$ is self-adjoint because
$(ie_0)^{\natural}=ie_0$. This was checked numerically on the central parameters.

**Read as a physical statement.** The self-adjoint operators of the gauge band form a complex line of parameters, and a purely imaginary
scalar is a self-adjoint operator of the band. The interpretation is that the band's symmetry class is the **projective line of central
calibrations** and not the observables of the positive row; the reality that distinguishes observables belongs to the Hermitian form of the
probability band, *Observables, Gauge Generators and the Chirality of the Internal Action*.

## The Rank, the Determinant and the Traces

**Theorem (the rank, the determinant, the traces and the norm).** For an element $\tilde A$ the two families have the same rank,
$\operatorname{rank}L^{\bullet}_{\tilde A}=\operatorname{rank}R^{\bullet}_{\tilde A}$ equal to $0$ at $\tilde A=0$, to $4$ when $A_0=0$ with
$\tilde A\neq0$, to $8$ when $A_0\neq0$ with $N(\tilde A)\neq0$, and to $6$ when $A_0\neq0$ with $N(\tilde A)=0$; moreover
$\det L^{\bullet}_{\tilde A}=\det R^{\bullet}_{\tilde A}=\lvert N(\tilde A)\rvert^{2}\lvert A_0\rvert^{4}$,
$\operatorname{tr}L^{\bullet}_{\tilde A}=0$ and $\operatorname{tr}R^{\bullet}_{\tilde A}=-4\,\mathrm{Re}(A_0)$, the determinant and the
traces being those of the real-linear operators on the eight-real-dimensional space.

*Proof.* The rank table, the determinant and the traces are *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*,
§*Rank, Image and Trace*; the two families have the same rank because $L^{\bullet}_{\tilde A}=C\circ R^{\bullet}_{\tilde A}$ with $C$ of
determinant $+1$. The norm $N$ enters the determinant and the rank through the two conditions $A_0=0$ and $N(\tilde A)=0$, and *Norm and
Invertibility in the General Plain Algebra* owns the norm.

**Read as a physical statement.** The operator of a gauge element is invertible exactly when the element is not a zero divisor, and the norm
$N$ is the datum that decides it: an element of nonzero scalar part and nonzero norm acts at full rank, one of zero norm collapses a real
plane and a pure vector acts at half rank. The interpretation is that the gauge multiplication measures an element through its norm and its scale,
and that the collapse at $N=0$ is the algebraic trace of the null directions of the metric.

## The Symmetries of the Form and of the Product

**Theorem (the form-preserving operators).** No left multiplication preserves $K$. The right multiplication preserves $K$ exactly for a
**central parameter of modulus one**, that is $K(R^{\bullet}_{\tilde A}\tilde X,R^{\bullet}_{\tilde A}\tilde Y)=K(\tilde X,\tilde Y)$ for all
$\tilde X,\tilde Y$ exactly when $\tilde A=\lambda e_0$ with $\lvert\lambda\rvert=1$, and then
$R^{\bullet}_{\lambda e_0}=\overline{\lambda}\,{}^{\natural}$. The general group of complex-linear maps preserving $K$ is larger, of real
dimension sixteen, its matrices obeying $M^{\dagger}EM=E$ with $E=\mathrm{diag}(1,-1,-1,-1)$; the band's right multiplications meet it in the
circle $\{\overline{\lambda}\,{}^{\natural}:\lvert\lambda\rvert=1\}$.

*Proof.* The value $K(L^{\bullet}_{\tilde A}\tilde X,L^{\bullet}_{\tilde A}\tilde Y)$ is conjugate-linear in $\tilde X$ and linear in
$\tilde Y$, while $K(\tilde X,\tilde Y)$ is linear in $\tilde X$ and conjugate-linear in $\tilde Y$: the two parities differ, so no left
multiplication can preserve the form. For the right family, $R^{\bullet}_{\lambda e_0}=\overline{\lambda}\,{}^{\natural}$ gives
$K(\overline{\lambda}\tilde X^{\natural},\overline{\lambda}\tilde Y^{\natural})=\lvert\lambda\rvert^{2}K(\tilde X,\tilde Y)$ because
$K(\tilde X^{\natural},\tilde Y^{\natural})=K(\tilde X,\tilde Y)$. The group of linear maps preserving $K$ and its matrix condition are *The
Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*, §*The Groups*.

**Read as a physical statement.** The left family of the band is never an isometry of the metric, for a reason of parity and not of
parameter; the only isometries the band's own multiplications supply are the right multiplications by a central phase. The interpretation is that
the gauge pairing is preserved by a compact circle of central calibrations and by nothing one-sided else, and that the general isometry group
of the metric is larger than the band's operators.

**Theorem (the product-preserving operators).** The natural conjugation ${}^{\natural}$ is a $\mathbb{C}$-linear automorphism of the product,
the coefficientwise conjugation $\bar{\cdot}$ is a conjugate-linear automorphism, and the star ${}^{*}$ is their composite; the three
generate the **Klein group** $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$. The multiplicative one-sided operators of the band are only
the identity and the zero operator:
$L^{\bullet}_{\tilde A}(\tilde X\bullet\tilde Y)=(L^{\bullet}_{\tilde A}\tilde X)\bullet(L^{\bullet}_{\tilde A}\tilde Y)$ for all
$\tilde X,\tilde Y$ exactly when $\tilde A\in\{0,e_0\}$.

*Proof.* The three involutions satisfy $\varphi(\tilde P\bullet\tilde Q)=\varphi(\tilde P)\bullet\varphi(\tilde Q)$ by the definition of the
product and the two anti-automorphism properties of the conjugations, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$; this is *The Multiplication
Operators of the Symmetric Quaternionic Sesqualgebra*, §*The Groups*. For multiplicativity, $L^{\bullet}_{e_0}={}^{*}$ is multiplicative
because it is an automorphism of the product and $L^{\bullet}_{0}=0$ trivially, while every other parameter fails:
$L^{\bullet}_{\lambda e_0}=\lambda\,{}^{*}$ is multiplicative only for $\lambda$ with $\lambda^{2}=\lambda$, and a non-central parameter
fails already at $\tilde X=\tilde Y=e_0$. This was checked numerically on the central and non-central parameters.

**Read as a physical statement.** The symmetries of the **product** and the symmetries of the **form** fall on different operators: the form
is preserved by the right multiplications of the central phases and the product by the four involutions of the structure group, while the
band's one-sided multiplications are multiplicative only at the identity and at zero. The interpretation is that the gauge pairing has a finite
structure group and a compact circle of phase isometries, and that no genuine one-sided operation is a symmetry of either beyond those.

**Proposition (the structure group and the operators).** For every $\tilde A$ one has
$L^{\bullet}_{\tilde A^{\natural}}={}^{\natural}\circ L^{\bullet}_{\tilde A}\circ{}^{\natural}$ and
$L^{\bullet}_{\bar{\tilde A}}=\bar{\cdot}\circ L^{\bullet}_{\tilde A}\circ\bar{\cdot}$, so the structure group acts on the operator families
by conjugation of the parameter and of the space.

*Proof.* The two identities are the automorphism property of ${}^{\natural}$ and of $\bar{\cdot}$ read on the operator,
$L^{\bullet}_{\varphi\tilde A}=\varphi\circ L^{\bullet}_{\tilde A}\circ\varphi^{-1}$, and the involutions are their own inverses.

**Read as a physical statement.** The conjugations that generate the structure group relabel the space and the parameter at once, so the
band's operator is attached to the **class** of the parameter under the Klein group and not to the parameter alone. The interpretation is that the
gauge multiplication is invariant under the simultaneous relabelling of frame and calibration, which is the operator form of a gauge
redundancy of signs.

## The Operators Acting on the Krein Space

**The space of the band.** The band's space is the algebra $\mathbb{B}$ read as the **Krein space** of the form $K$, of signature $(1,3)$,
with fundamental decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_K\mathrm{Vect}(\mathbb{B})$ and fundamental symmetry
$J={}^{\natural}$. The operators $L^{\bullet}_{\tilde A}$ and $R^{\bullet}_{\tilde A}$ act on it, the first conjugate-linearly and the second
linearly, and the adjoint identity
$K(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\bullet}_{\tilde A^{\natural}}\tilde Y)}$ is the statement that the
adjoint of the left family stays inside the left family, and that the adjoint of the right family leaves it.

**Proposition (no module action).** The left multiplication of the band is conjugate-linear and is therefore not an element of
$\operatorname{End}_{\mathbb{C}}(\mathbb{B})$; it does not act on the simple left module $S=\mathbb{B}\tilde\Pi_1$ as a module map, and the
band supplies no action of the algebra on the state space. The action the framework uses on $S$ is the ordinary left multiplication
$L_{\tilde A}s=\tilde As$, of *The Spinor Space as a Module and as a Hilbert Space*.

*Proof.* A module action is $\mathbb{C}$-linear in the scalar, and the left multiplication of the band is conjugate-linear; the ordinary left
multiplication is the module action of the plain product.

**Read as a physical statement.** The band's operation cannot act on a state space, because a state space is a complex module and the band's
attachment of an element is conjugate-linear in the element it attaches. The interpretation is the operator form of the sibling's conclusion that
the symmetric gauge product **is not a state**: an operation that cannot be a module map cannot be a state update.

**Proposition (the algebraic norm is the metric and not a probability).** The scalar part of the product is the Krein form,
$\mathrm{Sc}(\tilde P\bullet\tilde Q)=K(\tilde P,\tilde Q)$, and at the two equal arguments
$\mathrm{Sc}(\tilde Q\bullet\tilde Q)=K(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}-\sum_{k=1}^{3}\lvert Q_k\rvert^{2}$, which is positive on the
centre, negative on the vector subspace and **not** positive definite. The form the band's operators are adjoint for is therefore the metric
itself, and it is not the positive definite form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ of the probability row.

*Proof.* The scalar part of the product is $K$ by the value theorem; the algebraic norm is the standard form of signature $(1,3)$ of the Krein
form, *The Fourth Product and Its Indefinite Metric*; $K(e_0,e_0)=+1$ and $K(e_1,e_1)=-1$ show that it is not positive definite, and the
positive form of the framework is *Mass, Rank and the Positivity of the Dagger*.

**Read as a physical statement.** The band's form is a metric of signature $(1,3)$, and its algebraic norm is the metric read on an element,
positive on a scale and negative on a direction. The interpretation, and it is the band's own: a symmetric gauge product is a **metric-like datum
and not a state**, its value lies, for a general pair, in no one of the remarkable subspaces, and the algebraic norm of the form is the metric the
band is named for (*Values in No Subspace: Why the Symmetric Gauge Product Is Not a State*).

**Proposition (the null directions).** The form has the null set $\{K=0\}$, a real cone of dimension seven, which contains $e_0+e_1$ and the
elements the metric cannot normalise; the operators of the band are not isometries of any sign-definite form, and their collapses on this
space are read from the rank table: the left multiplication by an element of zero norm and nonzero scalar part collapses a real plane, and
the left multiplication by a pure vector collapses the four-dimensional subspace $\mathrm{span}_{\mathbb{R}}\{e_2,e_3,ie_2,ie_3\}$ at
$\tilde A=e_1$.

*Proof.* The null set is the cone of the indefinite form, *The States the Indefinite Metric Cannot Normalise*; the kernel statements are read
from the rank table of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*, with $K(e_0+e_1,e_0+e_1)=0$ and
$N(e_0+e_1)=2\neq0$ for the invertible null element and $N(e_0+ie_1)=0$ with $A_0=1$ for the zero divisor of rank six.

**Read as a physical statement.** The band has null directions and the metric cannot normalise them, so the band's space is not a Hilbert
space and its operators are not isometries of a norm. The interpretation is that the gauge frame carries its own causal cone and that the states of
the framework live on the plain row and not here.

## The Sandwich and Its Adjoint

**Definition (the two-sided operator and the sandwich).** For a pair $\tilde P,\tilde Q$ the **two-sided operator** of the band is
$B^{\bullet}_{\tilde P,\tilde Q}(\tilde X)=\tilde P\bullet(\tilde X\bullet\tilde Q)$, and its **dielectric sandwich**, or algebraic norm, is the
case $\tilde Q=\tilde P^{\natural}$, that is
$\Theta^{\bullet}_{\tilde P}=B^{\bullet}_{\tilde P,\tilde P^{\natural}}=L^{\bullet}_{\tilde P}R^{\bullet}_{\tilde P^{\natural}}$, acting by
$\Theta^{\bullet}_{\tilde P}(\tilde X)=\tilde P\bullet(\tilde X\bullet\tilde P^{\natural})$. The sandwich is the biquaternion instance, for
the symmetric sesquilinear product, of the two-sided operator of the block; the sandwich of the plain product for the same indefinite form is
*The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*.

**Theorem (the adjoint of the two-sided operator).** For all $\tilde P,\tilde Q$ one has
$(B^{\bullet}_{\tilde P,\tilde Q})^{\dagger}=B^{\bullet}_{\tilde Q^{\natural},\tilde P^{\natural}}$ and
$(\Theta^{\bullet}_{\tilde P})^{\dagger}=\Theta^{\bullet}_{\tilde P}$, so a two-sided operator has as adjoint the same operator with the
parameters exchanged and each conjugated by ${}^{\natural}$, and every algebraic norm sandwich is **self-adjoint for $K$**.

*Proof.* The adjoint of a composite reverses the order and conjugates the parameters; with
$(R^{\bullet}_{\tilde Q})^{\dagger}=L^{\bullet}_{\tilde Q^{\natural}}C$ and
$(L^{\bullet}_{\tilde P})^{\dagger}=L^{\bullet}_{\tilde P^{\natural}}$,
$(L^{\bullet}_{\tilde P}R^{\bullet}_{\tilde Q})^{\dagger}=L^{\bullet}_{\tilde Q^{\natural}}C\,L^{\bullet}_{\tilde P^{\natural}}$.
Inserting $R^{\bullet}_{\tilde P^{\natural}}=C\circ L^{\bullet}_{\tilde P^{\natural}}$ and the involution of $C$ gives
$L^{\bullet}_{\tilde Q^{\natural}}R^{\bullet}_{\tilde P^{\natural}}$, which is the first display. For the algebraic norm, the two parameters of the
adjoint are $\tilde P^{\natural\natural}=\tilde P$ and $\tilde P^{\natural}$, which are the two parameters of the sandwich, so the operator
is its own adjoint.

**Read as a physical statement.** A two-sided gauge operation is self-adjoint for the metric whenever its two parameters are the two
conjugates of one element, and then the transport across the pairing returns the operation itself. The interpretation is the band's version of the
sandwich: the operation that pairs an element with its own natural conjugate is the symmetric two-sided datum of the gauge frame, and its
symmetry for $K$ is automatic and independent of the parameter, against the plain row where the sandwich is symmetric only on a slice.

**Remark (the sandwich of the plain product, cited).** For the plain product over the same indefinite form the sandwich is
$H_{Q}(T)=QTQ^{\dagger}$ with $Q^{\dagger}=JQ^{*}J$, and its laws are $H_{Q}(T)^{\dagger}=H_{Q}(T^{\dagger})$, $H_{Q}(H_{S}(T))=H_{QS}(T)$
and $H_{Q}(ST)=H_{Q}(S)H_{Q}(T)$ exactly when $Q^{\dagger}Q=\mathrm{id}$; the parameters coming from the algebra obey
$(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ and $(\Theta_{\tilde Q})^{\dagger}=\Theta_{{}^{\natural}\tilde Q}$, and on the $J$-unitary
slice $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{-1}}$. These are *The Indefinite Hermitian Sandwich on the General Quaternionic
Sesqualgebra of Biquaternions* and are cited, not re-proved.

**Read as a physical statement.** The plain sandwich of the same metric is an inner automorphism of the operator algebra on the $J$-unitary
slice, while the band's own algebraic norm sandwich is symmetric for every parameter. The interpretation is that the metric acts on the frame by a
conjugation of the **projective** parameter, and that the band's sandwich and the plain sandwich are two interpretations of the same indefinite
form.

## A Worked Case

Take the **minimal mixing element**, a sum of a scalar and a vector direction, $\tilde A=e_0+e_1$ with $A_0=1$, $\mathbf A=e_1$,
$N(\tilde A)=2$ and $K(\tilde A,\tilde A)=0$. Its operator is neither self-adjoint nor skew-adjoint, since
$\tilde A^{\natural}=e_0-e_1\neq\pm\tilde A$; its rank is eight and its determinant is $4$, so it is invertible. On the real basis
$(e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3)$ the left multiplication acts by

$$
e_0\mapsto e_0-e_1,\quad e_1\mapsto -e_0-e_1,\quad e_2\mapsto -e_2,\quad e_3\mapsto -e_3,
$$

$$
ie_0\mapsto -ie_0+ie_1,\quad ie_1\mapsto ie_0+ie_1,\quad ie_2\mapsto ie_2,\quad ie_3\mapsto ie_3,
$$

whose real matrix has $\det L^{\bullet}_{e_0+e_1}=\lvert N(\tilde A)\rvert^{2}\lvert A_0\rvert^{4}=4$, and the algebraic norm of the product leaves
the centre,

$$
\tilde A\bullet\tilde A=(e_0+e_1)\bullet(e_0+e_1)=-2e_1,
$$

because $K(\tilde A,\tilde A)=0$ and the mixed term $-A_0\overline{\mathbf A}-\overline{A_0}\mathbf A=-2e_1$ survives. The element is the
witness that the algebraic norm is not central, and its value is a vector and not a complex multiple of $e_0$.

Take next the **central parameter** $\tilde C=ie_0$ with $\tilde C^{\natural}=ie_0=\tilde C$ and $N(\tilde C)=-1$, which gives the
self-adjoint operator $L^{\bullet}_{ie_0}=i\,{}^{*}$ acting by $L^{\bullet}_{ie_0}(e_0)=ie_0$, $L^{\bullet}_{ie_0}(e_1)=-ie_1$ and
$L^{\bullet}_{ie_0}(ie_1)=-e_1$. The element is the witness that self-adjointness of the band is a condition of centrality and not of
reality, and its algebraic norm is central, $ie_0\bullet ie_0=e_0$.

Take next the **pure vector parameter** $\tilde S=e_1$ with $\tilde S^{\natural}=-e_1=-\tilde S$, $N(\tilde S)=1$ and
$K(\tilde S,\tilde S)=-1$, which gives the skew-adjoint operator $L^{\bullet}_{e_1}$ of real rank four, acting by
$L^{\bullet}_{e_1}(e_0)=-e_1$, $L^{\bullet}_{e_1}(e_1)=-e_0$, $L^{\bullet}_{e_1}(ie_0)=ie_1$ and $L^{\bullet}_{e_1}(ie_1)=ie_0$, with kernel
$\mathrm{span}_{\mathbb{R}}\{e_2,e_3,ie_2,ie_3\}$ and central algebraic norm $e_1\bullet e_1=-e_0$. The element is the witness of the skew class
and of the negative signature of the form.

Take finally the **zero divisor**, $\tilde D=e_0+ie_1$ with $A_0=1\neq0$ and $N(\tilde D)=1+i^{2}=0$, for which the rank drops to six and the
kernel is the real plane $\ker L^{\bullet}_{e_0+ie_1}=\mathrm{span}_{\mathbb{R}}\{e_0+ie_1,\ ie_0-e_1\}$, the element itself lying in its own
kernel. The four elements — a mixing element neither self- nor skew-adjoint, a central self-adjoint element with a non-real parameter, a pure
vector skew-adjoint element and a zero divisor of nonzero scalar part — display the type theory, the rank table and the indefiniteness of the
metric on four explicit parameters.

**A numerical check.** Recomputing with biquaternions in the coefficient model, to machine precision over random and structured elements and
never exceeding one hundred per claim: the product is conjugate-commutative and reduces to
$[P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})]-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P$;
$L^{\bullet}_{\tilde A}=C\circ R^{\bullet}_{\tilde A}$ with $C$ the coefficientwise conjugation, so the two families do **not** coincide;
$L^{\bullet}_{\lambda e_0}=\lambda\,{}^{*}$ and $R^{\bullet}_{\lambda e_0}=\overline{\lambda}\,{}^{\natural}$, the left family
conjugate-linear and the right linear, each with the opposite parity in the parameter; the adjoint identity
$K(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\bullet}_{\tilde A^{\natural}}\tilde Y)}$ and the right adjoint
$(R^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{\natural}}C$ hold; the type criteria hold exactly for the central and the pure
vector parameters, with $L^{\bullet}_{ie_0}$ self-adjoint though its parameter is not real and a mixed parameter neither self- nor
skew-adjoint; the rank table gives $0,4,8,6$ on the four cases, with $\det L^{\bullet}_{e_0+e_1}=4$ and
$\operatorname{tr}R^{\bullet}_{\tilde A}=-4\,\mathrm{Re}(A_0)$; no left multiplication preserves $K$, and the right multiplication preserves
it exactly for $\lambda e_0$ with $\lvert\lambda\rvert=1$; the multiplicative one-sided operators are exactly $0$ and $e_0$; the four
involutions $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ are automorphisms of the product; the two-sided adjoint gives
$(\Theta^{\bullet}_{\tilde A})^{\dagger}=\Theta^{\bullet}_{\tilde A}$ for every parameter; and the four worked elements were recomputed
coefficient by coefficient.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must declare.

- **The product and its laws are not re-proved here.** The value, the conjugate-commutativity, the absence of a unit, the failure of the
  Jordan identity and the fact that the value lies in no subspace are *The Gauge Metric as a Product* and *Values in No Subspace: Why the
  Symmetric Gauge Product Is Not a State*.

- **The metric is not re-derived here.** The signature, the inertia, the fundamental symmetry, the isometry group $U(1,3)$ and the null
  states are *The Fourth Product and Its Indefinite Metric* and *The States the Indefinite Metric Cannot Normalise*; this article reads the
  metric as the form the operators are adjoint for.

- **The positive adjoint is not this adjoint.** The observables and the gauge generators of the framework are the self-adjoint and the
  skew-adjoint operators of the **positive definite** Hermitian form of the probability row, and they are *Observables, Gauge Generators and
  the Chirality of the Internal Action*. This article's adjoint is the **$J$-adjoint** for the indefinite form $K$, its fixed points are the
  central multiplications, and they are not the observables.

- **The sandwich is not re-read here.** The general indefinite sandwich, its composition, its multiplicativity and its kernel and image are
  *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*; this article states the band's algebraic norm case
  and cites the rest.

- **The four adjoints are not compared here.** The comparison, block against block, is the crossing reader *The Operators of the Twelve
  Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this article declares only the gauge column.

**What the framework does not claim.** The interpretation does not reconstruct a state space from the gauge pairing; it states that no module action
and no positivity are available, which is the negative content of the band. It does not identify the band's self-adjoint operators with
observables; it states that the self-adjoint class is the centre and that the observables belong to the positive form. And it does not claim
that the operator calculus of the twelve rows is one calculus: the gauge row has two families and no operator algebra, and the collapse of
the two families into one, which the symmetric plain row enjoys, requires commutativity and is absent here.

## The Ledger

**Proved.** The symmetric quaternionic sesquilinear product has the two multiplication operators
$L^{\bullet}_{\tilde A}(\tilde X)=\tilde A\bullet\tilde X$, conjugate-linear, and $R^{\bullet}_{\tilde A}(\tilde X)=\tilde X\bullet\tilde A$,
complex-linear, linked by $L^{\bullet}_{\tilde A}=C\circ R^{\bullet}_{\tilde A}$ with the coefficientwise conjugation, so the band carries
**two** families of opposite parity and **not** a single family; $L^{\bullet}_{e_0}={}^{*}$ and $R^{\bullet}_{e_0}={}^{\natural}$; the value
is $K(\tilde A,\tilde X)e_0-A_0\overline{\mathbf X}-\overline{X_0}\mathbf A$ with scalar part the Krein form $K$ and vector part the mixed
term; the families do not multiply, the left defect is the associator, and the parity forbids a complex-linear representation, so the band
has no enveloping operator algebra. The form is the **indefinite** Krein form
$K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ of signature $(1,3)$ with fundamental symmetry $J={}^{\natural}$, and
the article is about the **$J$-adjoint** for $K$, not a definite adjoint:
$K(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\bullet}_{\tilde A^{\natural}}\tilde Y)}$ and
$(R^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{\natural}}C$. The types are self-adjoint exactly on the centre $\mathbb{C}e_0$ and
skew-adjoint exactly on the vector subspace $\mathrm{Vect}(\mathbb{B})$, and a self-adjoint operator of the band is **not** automatically
real, since $ie_0$ is a self-adjoint parameter. The rank is one of $0,4,8,6$ according to the scale $A_0$ and the norm $N(\tilde A)$, the
traces are $0$ and $-4\,\mathrm{Re}(A_0)$, and the determinant is $\lvert N(\tilde A)\rvert^{2}\lvert A_0\rvert^{4}$; no left multiplication
preserves $K$ and the right multiplication preserves it exactly for the central phases of modulus one; the multiplicative one-sided operators
are only $0$ and $e_0$; the structure group of the product is the Klein group $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$; and the
two-sided adjoint is $(B^{\bullet}_{\tilde P,\tilde Q})^{\dagger}=B^{\bullet}_{\tilde Q^{\natural},\tilde P^{\natural}}$ with every algebraic norm
sandwich $\Theta^{\bullet}_{\tilde P}=L^{\bullet}_{\tilde P}R^{\bullet}_{\tilde P^{\natural}}$ self-adjoint for $K$. The product and its
value are *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* and *The Gauge Metric as a Product*; the operators, the
parity, the rank, the traces and the groups are *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*; the adjoint
relation is *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; the $J$-adjoint and the $J$-unitary family are
*J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*; the sandwich is *The Indefinite Hermitian
Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*.

**Interpretations.** That the symmetrisation gives the product a **conjugate-commutativity** and that the two families are the two parities of one
pairing and do **not** coincide, the collapse into one family being the commutativity of the symmetric plain row; that the band's adjoint is
an **indefinite $J$-adjoint that keeps the side and conjugates the parameter by the natural conjugation**, the parameter conjugation
replacing the plain row's crossing of the sides; that self-adjointness is a condition of **type** (centrality) and not of reality, so a
purely imaginary central parameter gives a self-adjoint multiplication; that the band's symmetry class is the **centre** and its
antisymmetric class the **vector directions**; that the band supplies **no module action** and **no positivity**, so a symmetric gauge
product is a **metric-like datum and not a state**; that the algebraic norm of the form is the **metric** and that the value lies, for a general
pair, in no subspace; that the form-preserving operators of the band are a compact circle of central phases on the right and none on the
left, and that the product-preserving ones are the finite structure group; and that the algebraic norm sandwich is self-adjoint for $K$ for every
parameter. Each is the framework's naming of a proved algebraic fact and is labelled as such.

## Physical Readings

The operators of the symmetric gauge product read as the two ways of attaching a gauge calibration to an internal frame, and the calibration
enters the two ways with opposite polarity: the left attachment reads the argument through the star and the right through the natural
conjugation, and the two differ by the coefficientwise conjugation that the symmetrisation installed. The band's adjoint being the indefinite
$J$-adjoint, the pairing is read as an operation that **does not distinguish left from right** and that conjugates the calibration instead,
which is the operator content of the metric word: a gauge calibration is transported by reflecting the vector directions and not by reversing
a charge.

The band's form is an **indefinite metric of signature $(1,3)$**, and its algebraic norm is the metric read on an element: positive on a scale
direction and negative on a vector direction, with null directions the metric cannot normalise. The interpretation, and it is the band's own, is
that a symmetric gauge product is a **metric-like datum and not a state**: its value carries the scalar part $K$ and the mixed vector part
side by side and therefore lies, for a general pair, in no one of the remarkable subspaces, the self-pairing $\tilde Q\bullet\tilde Q$ is in
general not central, and the standard reconstruction of a state space — positivity, a unit, a Jordan structure, a module action — does not
reach it. The metric belongs to the transformation side of the frame, whose invariants are the pairings left unchanged, and not to the state
side, whose invariants are positive numbers.

Read on the type theory, the two classes of the band are the centre and the vector directions: a central calibration is a self-adjoint
multiplication and a pure vector calibration a skew-adjoint one, and a calibration that mixes a scale with a direction is neither. The
interpretation is that the symmetric class of the band is the complex line of central calibrations — not the observables of the positive row — and
that the antisymmetric class is the vector subspace, so that the band separates a scale from a direction and labels the mixing element as the
one that belongs to neither. Read on the rank, the band measures a calibration through its norm and its scale, and the collapse at $N=0$ is
the algebraic trace of the null directions of the metric. Read on the frame, the operators are a deformation: their scalar part a conformal
factor and their traceless vector part a shear, so the gauge pairing deforms an element rather than rotating it or translating it.

## Summary

The operators of the symmetric quaternionic sesquilinear product are the left multiplication
$L^{\bullet}_{\tilde A}(\tilde X)=\tilde A\bullet\tilde X$, conjugate-linear, and the right multiplication
$R^{\bullet}_{\tilde A}(\tilde X)=\tilde X\bullet\tilde A$, complex-linear, and they are **two** families and not one: the symmetrisation
makes the product **conjugate-commutative**, not commutative, and the two families are linked by
$L^{\bullet}_{\tilde A}=C\circ R^{\bullet}_{\tilde A}$ with the coefficientwise conjugation. The two operators of the unit are the two
conjugations, $L^{\bullet}_{e_0}={}^{*}$ and $R^{\bullet}_{e_0}={}^{\natural}$. The families do not multiply, the left defect being the
associator, and the parity forbids a complex-linear representation, so the band has no enveloping operator algebra. The form of the band is
the **indefinite** Krein form
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ of signature $(1,3)$, with
fundamental symmetry $J={}^{\natural}$, and the adjoint the operators carry is the **$J$-adjoint** for $K$: it **keeps the side and
conjugates the parameter by the natural conjugation**,
$K(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\bullet}_{\tilde A^{\natural}}\tilde Y)}$, against the plain row of the
same form, whose adjoint crosses the sides. The type criteria are on one parameter: self-adjoint exactly on the centre $\mathbb{C}e_0$,
skew-adjoint exactly on the vector subspace, and a self-adjoint operator is **not** automatically real, since $ie_0$ is a self-adjoint
parameter of the band. The rank is one of $0,4,8,6$ according to the scale and the norm $N(\tilde A)$, the determinant is
$\lvert N(\tilde A)\rvert^{2}\lvert A_0\rvert^{4}$ and the traces are $0$ and $-4\,\mathrm{Re}(A_0)$; no left multiplication preserves $K$
and the right multiplication preserves it exactly for the central phases of modulus one; the multiplicative one-sided operators are only $0$
and $e_0$; the structure group is the Klein group $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$; and the algebraic norm sandwich
$\Theta^{\bullet}_{\tilde P}=L^{\bullet}_{\tilde P}R^{\bullet}_{\tilde P^{\natural}}$ is self-adjoint for $K$ for every parameter. The band
supplies **no module action** and **no positivity**: the scalar part of the product is the metric itself, the algebraic norm of the form is the
metric, and a symmetric gauge product is a **metric-like datum and not a state**, its value lying, for a general pair, in no one of the
remarkable subspaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ | the product, $\mathrm{SQS}$ |
| $L^{\bullet}_{\tilde A}(\tilde X)=\tilde A\bullet\tilde X$ | the left multiplication, conjugate-linear |
| $R^{\bullet}_{\tilde A}(\tilde X)=\tilde X\bullet\tilde A$ | the right multiplication, complex-linear |
| $L^{\bullet}_{\tilde A}=C\circ R^{\bullet}_{\tilde A}$, $C=\bar{\cdot}$ | the conjugate-commutativity of the two families |
| $L^{\bullet}_{e_0}={}^{*}$, $R^{\bullet}_{e_0}={}^{\natural}$ | the two operators of the unit |
| $L^{\bullet}_{\lambda e_0}=\lambda\,{}^{*}$, $R^{\bullet}_{\lambda e_0}=\overline{\lambda}\,{}^{\natural}$ | the parity in the parameter |
| $\tilde A\bullet\tilde X=K(\tilde A,\tilde X)e_0-A_0\overline{\mathbf X}-\overline{X_0}\mathbf A$ | the value of the product |
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, $\varepsilon=(1,-1,-1,-1)$ | the Krein form, signature $(1,3)$ |
| $J={}^{\natural}$, $T^{\dagger}=JT^{*}J$ | the fundamental symmetry and the $J$-adjoint |
| $K(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\bullet}_{\tilde A^{\natural}}\tilde Y)}$ | the left-adjoint rule |
| $(R^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{\natural}}C$ | the adjoint of the right multiplication |
| self-adjoint $\iff\tilde A\in\mathbb{C}e_0$; skew-adjoint $\iff\tilde A\in\mathrm{Vect}(\mathbb{B})$ | the type criteria |
| $L^{\bullet}_{ie_0}=i\,{}^{*}$ self-adjoint, parameter non-real | reality is not automatic |
| $\operatorname{rank}\in\{0,4,8,6\}$, $\det=\lvert N\rvert^{2}\lvert A_0\rvert^{4}$ | the rank and the determinant; the norm enters |
| $\operatorname{tr}L^{\bullet}=0$, $\operatorname{tr}R^{\bullet}=-4\,\mathrm{Re}(A_0)$ | the traces |
| no left multiplication preserves $K$; $R^{\bullet}_{\lambda e_0}$ preserves $K\iff\lvert\lambda\rvert=1$ | the form-preserving operators |
| multiplicative $L^{\bullet}_{\tilde A}\iff\tilde A\in\{0,e_0\}$ | the multiplicative one-sided operators |
| $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ | the structure group of the product |
| $(B^{\bullet}_{\tilde P,\tilde Q})^{\dagger}=B^{\bullet}_{\tilde Q^{\natural},\tilde P^{\natural}}$ | the two-sided adjoint |
| $(\Theta^{\bullet}_{\tilde P})^{\dagger}=\Theta^{\bullet}_{\tilde P}$ | the self-adjoint algebraic norm sandwich |
| $\tilde D=e_0+ie_1$, $N=0$, rank $6$ | the zero divisor of zero norm |

## Further Reading

- Mathematics article *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*
  (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the two families, the parity, the
  matrices, the rank, the image, the traces, the kernel, the composition defect, the adjoint for $K$, the $J$-self-adjointness, the group
  preserving $K$ and the structure group.
- Mathematics article *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*
  (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form $K$ read as the multiplication
  of the block and for the adjoint relation in the form setting.
- Mathematics article *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*
  (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the
  $J$-adjoint, the conjugate transpose and the group preserving the form.
- Mathematics article *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*
  (`articles_maths/the-indefinite-hermitian-sandwich-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the indefinite
  sandwich, its composition and multiplicativity, its kernel and image and the parameters coming from the algebra.
- Mathematics article *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*
  (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its class and its
  scalar–vector form.
- Mathematics article *The Krein Gram Matrix and the Restrictions of the Form*
  (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form, its Gram data and its restrictions to the
  remarkable subspaces.
- Mathematics article *Norm and Invertibility in the General Plain Algebra*
  (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the norm $N$ entering the rank table and the determinant.
- Physics article *The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product*
  (`articles_physics/the-gauge-metric-as-a-product-the-symmetric-quaternionic-sesquilinear-product.md`), the framing article of the band, for
  the value, the conjugate-commutativity, the absence of a unit, the failure of the Jordan identity and the metric word.
- Physics article *Values in No Subspace: Why the Symmetric Gauge Product Is Not a State*
  (`articles_physics/values-in-no-subspace-why-the-symmetric-gauge-product-is-not-a-state.md`), for the value in no subspace, the non-central
  algebraic norm and the conclusion that the product is not a state.
- Physics article *The Fourth Product and Its Indefinite Metric* (`articles_physics/the-fourth-product-and-its-indefinite-metric.md`), for
  the signature, the inertia, the fundamental symmetry and the isometry group of the metric.
- Physics article *The States the Indefinite Metric Cannot Normalise*
  (`articles_physics/the-states-the-indefinite-metric-cannot-normalise.md`), for the null directions of the form.
- Physics article *Observables, Gauge Generators and the Chirality of the Internal Action*
  (`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`), for the positive adjoint, the observables
  and the generators, which are the self-adjoint and the skew-adjoint operators of the Hermitian form and not of the band's indefinite form.
- Physics article *The Spinor Space as a Module and as a Hilbert Space*
  (`articles_physics/the-spinor-space-as-a-module-and-as-a-hilbert-space.md`), for the state space on which the band supplies no action.
- Physics article *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*
  (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing reader of the twelve
  operator rows, which is not one of the twelve.

