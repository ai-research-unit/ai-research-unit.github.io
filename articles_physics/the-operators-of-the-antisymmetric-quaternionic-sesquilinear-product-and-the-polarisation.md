# __The Operators of the Antisymmetric Quaternionic Sesquilinear Product and the Polarisation__

## Introduction

This article is the operator article of the fourth band's antisymmetric half, the operation
$\mathrm{AQS}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Its product is the
antisymmetric quaternionic sesquilinear product

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}},
$$

and its operators attach an element to an argument:

$$
L^{\diamond}_{\tilde A}(\tilde X)=\tilde A\diamond\tilde X=\mathbf{A}\times\overline{\mathbf{X}},\qquad
R^{\diamond}_{\tilde A}(\tilde X)=\tilde X\diamond\tilde A=\mathbf{X}\times\overline{\mathbf{A}} .
$$

The left family is **conjugate-linear** in its argument, the right family is $\mathbb{C}$-**linear**, and the
band's conjugate-alternation links the two, $L^{\diamond}_{\tilde A}=-C\circ R^{\diamond}_{\tilde A}$ with
$C$ the coefficientwise conjugation. The composite of two left multiplications is again $\mathbb{C}$-linear
and is **not** a left multiplication, so the family is not closed and carries **no Lie algebra**; the closure
that exists is the closure of the underlying cross product, and it is invisible on the real quaternion forms.

The answer in one sentence is this. The operators of the band are adjoint for the **indefinite Krein form**
$K$ of the fourth product, and the adjoint of the left multiplication is its **negative**,
$L^{\diamond\dagger}_{\tilde A}=-L^{\diamond}_{\tilde A}$: it **reverses the parameter** and **keeps the
side**, a third behaviour on the one algebra beside the composition band's side-swapping transpose and the
probability band's parameter-conjugating Hermitian adjoint. The band's sandwich is consequently self-adjoint
for $K$ for **every** parameter, and the type criteria, the symmetries and the reading follow from that sign.

The operation is *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*; the operator
content is *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, which owns the left
multiplication, its invariants, its adjoint and its structure group; the form is *The Krein Gram Matrix and
the Restrictions of the Form*; the indefinite adjoint and its type criteria are *J-Self-Adjoint and J-Unitary
Operators on the General Quaternionic Sesqualgebra of Biquaternions*; and the diagonal, the Jacobi failure
and the higher structure are *The Cross Product of a Vector with Its Conjugate*, *A Bracket Invisible on the
Real Forms* and *A Higher Structure for the Jacobi Failure*, cited and not repeated.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis
$e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, central $i$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with
vector part $\mathbf{Q}$, natural conjugation $\tilde Q^{\natural}=Q_0e_0-\mathbf{Q}$ and star
$\tilde Q^{*}=\overline{\tilde Q^{\natural}}$; $(\cdot,\cdot)$ and $\times$ are the bilinear dot and cross
products; the form is $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$
with $\varepsilon=(1,-1,-1,-1)$ and fundamental symmetry $J={}^{\natural}$. The symbol $\diamond$ is the
mathematics articles' name for the operation; the physics menu comment renders it $\wedge$, which the
mathematics avoids because $\wedge$ names the plain cross product.

## The Two Multiplication Operators and Their Composition Law

The band attaches one operator to each slot, and the two are not of the same kind: the first slot is the linear one, the second the conjugate-linear one.

**Definition (the multiplications of the product).** For $\tilde A\in\mathbb{B}$ the **left multiplication**
and the **right multiplication** of the product $\diamond$ are

$$
L^{\diamond}_{\tilde A}(\tilde X)=\tilde A\diamond\tilde X=\mathbf{A}\times\overline{\mathbf{X}},\qquad
R^{\diamond}_{\tilde A}(\tilde X)=\tilde X\diamond\tilde A=\mathbf{X}\times\overline{\mathbf{A}} .
$$

Their determination is *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, which owns the left family, its matrix, its rank and its adjoint.

### The Parities and the Link Between the Families

**Proposition (the parities).** For every $\lambda\in\mathbb{C}$ and every $\tilde X\in\mathbb{B}$,

$$
L^{\diamond}_{\tilde A}(\lambda\tilde X)=\overline{\lambda}\,L^{\diamond}_{\tilde A}(\tilde X),\qquad
R^{\diamond}_{\tilde A}(\lambda\tilde X)=\lambda\,R^{\diamond}_{\tilde A}(\tilde X),
$$

and in the parameter $L^{\diamond}_{\lambda\tilde A}=\lambda L^{\diamond}_{\tilde A}$,
$R^{\diamond}_{\lambda\tilde A}=\overline{\lambda}R^{\diamond}_{\tilde A}$. The left multiplication depends
on $\tilde A$ through $\mathbf{A}$ and is $\mathbb{C}$-linear in the parameter; the right multiplication
depends on $\tilde A$ through $\overline{\mathbf{A}}$ and is conjugate-linear in the parameter.

*Proof.* The cross product is conjugate-linear in its second factor and linear in its first; the parameter
laws are scalar multiplication of the vector part. Verified on sixty random pairs for the variable laws and
sixty for the parameter laws. The sibling mathematics article states the opposite of the parameter parity of
$L$ ("conjugate-linear in $\tilde A$"); it is corrected there, since the first slot is the linear one and
$L^{\diamond}_{\lambda\tilde A}=\lambda L^{\diamond}_{\tilde A}$.

**Read as a physical statement.** The two slots have opposite polarity and the attachments inherit it:
attaching on the left conjugates the variable, attaching on the right does not, and the parameter follows its
slot. This is a reading that names the parity of a sesquilinear product and calls it the two signs of a gauge
pairing.

**Proposition (the antisymmetry links the two families).** The conjugate-alternation reads on the operators as

$$
L^{\diamond}_{\tilde A}=-C\circ R^{\diamond}_{\tilde A},\qquad
R^{\diamond}_{\tilde A}=-C\circ L^{\diamond}_{\tilde A},
$$

that is $L^{\diamond}_{\tilde A}\tilde X=-\overline{R^{\diamond}_{\tilde A}\tilde X}$ for every $\tilde X$,
where the bar is the coefficientwise conjugation of the value.

*Proof.* The product's conjugate-alternation is $\tilde X\diamond\tilde A=-\overline{\tilde A\diamond\tilde X}$;
the identity is that equality read for a fixed $\tilde A$. Verified on fifty random pairs.

**Read as a physical statement.** The band has one operator family, not two independent ones: the right
multiplication is the conjugate of the left, and the conjugation of the second slot is the tie, which is why
the band never carries a full matrix algebra of one kind. This is a reading.

### The Composition Law

**Theorem (the composition laws).** For all $\tilde A,\tilde B,\tilde X\in\mathbb{B}$,

$$
L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}\tilde X=\mathbf{A}\times\bigl(\overline{\mathbf{B}}\times\mathbf{X}\bigr)
=\overline{\mathbf{B}}\,(\mathbf{A},\mathbf{X})-(\mathbf{A},\overline{\mathbf{B}})\,\mathbf{X},
$$

$$
R^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}\tilde X=\bigl(\mathbf{X}\times\overline{\mathbf{B}}\bigr)\times\overline{\mathbf{A}},\qquad
L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}\tilde X=\mathbf{A}\times\bigl(\overline{\mathbf{X}}\times\mathbf{B}\bigr),\qquad
R^{\diamond}_{\tilde B}L^{\diamond}_{\tilde A}\tilde X=\bigl(\mathbf{A}\times\overline{\mathbf{X}}\bigr)\times\overline{\mathbf{B}} .
$$

The first law is the **composition law adopted by this article**; the second form is the vector
triple-product identity
$\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=\mathbf{B}(\mathbf{A},\mathbf{C})-\mathbf{C}(\mathbf{A},\mathbf{B})$.

*Proof.* Each law substitutes one definition into the other and cancels the two conjugations in the inner
slot. The four laws were verified on sixty random triples each to machine precision. The left composition is
*The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, §*The Composition and the Conjugate
Invariants*.

**Corollary (the square).** Setting $\tilde B=\tilde A$, the square is
$\bigl(L^{\diamond}_{\tilde A}\bigr)^{2}\tilde X=\overline{\mathbf A}(\mathbf A,\mathbf X)-(\mathbf A,\overline{\mathbf A})\mathbf X$,
a $\mathbb{C}$-linear map of the vector part, in general nonzero and vanishing on the centre. Verified on
fifty random pairs.

**Read as a physical statement.** Two attachments on the left compose into a **linear** operation of the
ordinary kind, with a rank-one part and a scalar part proportional to $(\mathbf A,\overline{\mathbf A})$: the
band composes its operations into objects that are not operations of the band. This is a reading.

### The Failure of Closure

**Theorem (no Lie algebra of the left multiplications).** The commutator of two left multiplications is

$$
\bigl[L^{\diamond}_{\tilde A},L^{\diamond}_{\tilde B}\bigr]\tilde X
=\overline{\mathbf{B}}\,(\mathbf{A},\mathbf{X})-\overline{\mathbf{A}}\,(\mathbf{B},\mathbf{X})
-2i\,\mathrm{Im}\bigl(\mathbf{A},\overline{\mathbf{B}}\bigr)\,\mathbf{X},
$$

a $\mathbb{C}$-linear operator. On the **real quaternion subspace** the last term vanishes and

$$
\bigl[L^{\diamond}_{\mathbf a},L^{\diamond}_{\mathbf b}\bigr]\tilde X=(\mathbf a\times\mathbf b)\times\mathbf X
=R^{\diamond}_{-(\mathbf a\times\mathbf b)}\tilde X,
$$

while on the **real subspace of the arguments** it is the left multiplication of the cross product,
$[L^{\diamond}_{\mathbf a},L^{\diamond}_{\mathbf b}]=L^{\diamond}_{\mathbf a\times\mathbf b}$. Off the real
forms the last term is a nonzero multiple of the identity whenever
$\mathrm{Im}(\mathbf A,\overline{\mathbf B})\neq0$, and no multiplication of the band has such a term: the
commutator is then **not a multiplication of the band**, and the family is not closed.

*Proof.* The commutator is the difference of the two composites of the composition law, and the
triple-product identity gives the displayed form. For real parameters the last term vanishes because
$(\mathbf A,\overline{\mathbf B})$ is real, and the first two give $(\mathbf A\times\mathbf B)\times\mathbf X$;
a multiplication of the band has no term proportional to $\mathbf X$, so the last term cannot be absorbed.
Verified on sixty complex triples for the general formula, sixty real pairs for the real-form law, and sixty
further triples for the failure count.

**A complex witness.** At $(\tilde A,\tilde B,\tilde X)=(e_1,\,ie_1,\,e_2)$,

$$
\bigl[L^{\diamond}_{e_1},L^{\diamond}_{ie_1}\bigr]e_2=2i\,e_2,
\qquad\text{while}\qquad
L^{\diamond}_{e_1\diamond ie_1}e_2=L^{\diamond}_{0}e_2=0,
$$

because $e_1\diamond ie_1=e_1\times\overline{ie_1}=e_1\times(-ie_1)=0$. The witness uses $ie_1$, an element
off the real basis; the failure count is sixty of sixty complex triples against zero of sixty real ones.

**Read as a physical statement.** A family of operators that is to be a Lie algebra must close under the
commutator; here the commutator is an operator of a kind that no multiplication of the band supplies, so the
family closes into nothing. The obstruction is the coefficient conjugation: on the real quaternion forms the
conjugation is the identity, the cross product is a Lie bracket, and a real-form check finds no failure; the
failure appears when a complex coefficient enters. This is the operator form of *A Bracket Invisible on the
Real Forms: the Complex Witness of the Jacobi Failure*, and the positive reading is *A Higher Structure for
the Jacobi Failure*. This is a reading.

## The Adjoint: the Indefinite Form and What It Does to the Parameter

The form decides the adjoint, and the form of the band is the indefinite Krein form of the fourth product.

**Definition (the form and the adjoint).** The form of the band is
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$,
of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, with fundamental symmetry
$J={}^{\natural}$. The **adjoint** of a conjugate-linear operator $T$ is the conjugate-linear operator
$T^{\dagger}$ with $K(T\tilde R,\tilde S)=\overline{K(\tilde R,T^{\dagger}\tilde S)}$, and the adjoint of a
$\mathbb{C}$-linear operator $U$ is the $\mathbb{C}$-linear operator with
$K(U\tilde R,\tilde S)=K(\tilde R,U^{\dagger}\tilde S)$; the twisted rule is *The Adjoint of the Sesquilinear
Sandwich on the Biquaternions*, §*The Twisted Adjoint Rule*, and the linear class's $\mathbb{C}$-linear
adjoint is the $J$-adjoint $U^{\dagger}=JU^{*}J$ of *J-Self-Adjoint and J-Unitary Operators on the General
Quaternionic Sesqualgebra of Biquaternions*.

**Theorem (the adjoint of the multiplications).** For all $\tilde A,\tilde B\in\mathbb{B}$,

$$
\bigl(L^{\diamond}_{\tilde A}\bigr)^{\dagger}=-L^{\diamond}_{\tilde A},\qquad
\bigl(R^{\diamond}_{\tilde A}\bigr)^{\dagger}=-R^{\diamond}_{\overline{\tilde A}},\qquad
\bigl(L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}\bigr)^{\dagger}=R^{\diamond}_{\overline{\tilde B}}\,L^{\diamond}_{\tilde A}.
$$

The adjoint of the left multiplication is its **negative**: it reverses the parameter, $\mathbf A\mapsto-\mathbf A$,
and **keeps the side**. The adjoint of the right multiplication negates and conjugates the parameter and keeps
the side.

*Proof.* For the first, the left side is
$K(L^{\diamond}_{\tilde A}\tilde R,\tilde S)=-(\mathbf A\times\overline{\mathbf R},\overline{\mathbf S})=-\det[\mathbf A,\overline{\mathbf R},\overline{\mathbf S}]$
and the right side is
$-\overline{K(\tilde R,L^{\diamond}_{\tilde A}\tilde S)}=\det[\overline{\mathbf R},\mathbf A,\overline{\mathbf S}]$,
the two sign readings of one triple product; this
is the theorem of *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*. The second is the
same triple product on the other slot, and the third is antimultiplicativity,
$(L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B})^{\dagger}=(R^{\diamond}_{\tilde B})^{\dagger}(L^{\diamond}_{\tilde A})^{\dagger}$.
Verified on sixty random parameters each.

**Read as a physical statement.** The adjoint transports across the indefinite pairing without transporting
the side: it reverses the **parameter** and leaves the attachment. The three sesquilinear and bilinear rows
therefore do three different things on one algebra — the transpose swaps the sides, the Hermitian adjoint
conjugates and keeps the side, the indefinite adjoint negates and keeps the side. The band's operands are the
**value** of an alternating product, and the pairing of a value with a test element differs between the two
orders by the sign and the conjugate; the adjoint reads that sign. This is a reading.

**Corollary (the sandwich is self-adjoint for every parameter).** The diagonal two-sided operator

$$
\Theta^{\diamond}_{\tilde A}=L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde A}
$$

satisfies $\bigl(\Theta^{\diamond}_{\tilde A}\bigr)^{\dagger}=\Theta^{\diamond}_{\tilde A}$ for **every**
$\tilde A$, explicitly $R^{\diamond}_{\overline{\tilde A}}L^{\diamond}_{\tilde A}=L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde A}$.

*Proof.* $(\Theta^{\diamond}_{\tilde A})^{\dagger}=R^{\diamond}_{\overline{\tilde A}}L^{\diamond}_{\tilde A}$
by the third identity, and this equals $L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde A}$ by the triple-product
identity in the form
$\mathbf A\times(\overline{\mathbf X}\times\mathbf A)=(\mathbf A\times\overline{\mathbf X})\times\mathbf A$.
Verified on sixty random parameters.

**Read as a physical statement.** Where the composition band's sandwich is self-adjoint exactly on the two
sectors of its parameter, the band's sandwich is self-adjoint **unconditionally**: the negative of the left
multiplication is already the operator the pairing produces, so no sector condition can break the symmetry. A
sandwich of this band is a symmetric operation of the polarisation for every direction. This is a reading.

## The Types of the Operators

The type criteria are criteria on one parameter, as in every family whose adjoint keeps a side.

**Theorem (the types of the one-sided operators).** For every $\tilde A\in\mathbb{B}$,

$$
L^{\diamond}_{\tilde A}\ \text{self-adjoint}\iff\tilde A\in\mathbb{C}_{\mathbb{B}},
\qquad
L^{\diamond}_{\tilde A}\ \text{skew-adjoint for every }\tilde A,
$$

$$
R^{\diamond}_{\tilde A}\ \text{self-adjoint}\iff\mathbf A\in i\mathbb{R}^{3},
\qquad
R^{\diamond}_{\tilde A}\ \text{skew-adjoint}\iff\mathbf A\in\mathbb{R}^{3}.
$$

A self-adjoint left multiplication is therefore the **zero** operator, and the generic left multiplication is
skew-adjoint; the right multiplication separates on the reality of its vector part.

*Proof.* Self-adjointness of $L^{\diamond}_{\tilde A}$ is $-L^{\diamond}_{\tilde A}=L^{\diamond}_{\tilde A}$,
hence $\mathbf A=0$, and the skew case holds for every parameter. The right multiplication is parametrised
injectively in $\overline{\mathbf A}$, so self-adjointness is $-\overline{\mathbf A}=\mathbf A$ and
skew-adjointness is $-\overline{\mathbf A}=-\mathbf A$. Verified on sixty random parameters for each
criterion; the operator of the block is *The Adjoint Operators of the Antisymmetric Quaternionic
Sesqualgebra*, §*The Adjoint with respect to the Form*.

**Read as a physical statement.** The band supplies **no self-adjoint generator**: its left multiplications
are all skew-adjoint and the only self-adjoint one is zero. This is the operator statement that the
antisymmetric half is a structure of **directions** and not of observables; the observables and the gauge
generators are read with the **definite** Hermitian adjoint of *Observables, Gauge Generators and the
Chirality of the Internal Action*. This is a reading.

**Corollary (no J-unitary operator of the band).** No nonzero multiplication operator of the band, and no
nonzero sandwich of the band, preserves the Krein form: each annihilates the centre $\mathbb{C}_{\mathbb{B}}$,
hence is not invertible, and an operator preserving a non-degenerate form is invertible. The **J-unitary**
operators form the indefinite unitary group $U_{J}(\mathbb{B})\cong U(1,3)$ of real dimension sixteen; the
norm $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ enters their criteria for the **plain** families of the parent, where
$L_{\tilde Q}$ is $J$-unitary exactly for $\tilde Q\in S^{1}e_0$ and the plain sandwich $\Theta_{\tilde Q}$
exactly for $\lvert N(\tilde Q)\rvert=1$, as *J-Self-Adjoint and J-Unitary Operators on the General
Quaternionic Sesqualgebra of Biquaternions* states; the band's own criteria carry no norm, because the band's
operators are never invertible.

*Proof.* $L^{\diamond}_{\tilde A}$, $R^{\diamond}_{\tilde A}$ and $\Theta^{\diamond}_{\tilde A}$ all vanish at
$\tilde X=e_0$, so the centre lies in the kernel of all three and none is invertible. The group and its
dimension are *The Krein Isometry Group and Its J-Contractions*, and the norm criteria are the corollary of
*J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*. Verified
on sixty random parameters that no multiplication of the band preserves $K$.

**Read as a physical statement.** The isometries of the band's metric are not supplied by the band: they are
the indefinite unitaries of the parent, far larger than the multiplications, and the norm $N$ enters the gauge
story through the parent's plain sandwich, not through the antisymmetric half. This is a reading.

## The Symmetries of the Form and of the Product

**Theorem (the derivations and the structure group).** The derivations of the band form the real vector space

$$
\mathrm{Der}(\diamond)=\mathrm{End}_{\mathbb{R}}\bigl(\mathbb{C}_{\mathbb{B}}\bigr)\oplus\mathfrak{so}(3,\mathbb{R})
$$

of real dimension seven, the scalar maps of the centre together with the real skew maps of the vector part;
the group of invertible real-linear maps preserving the product contains

$$
\bigl\{\tilde Q\mapsto\lambda(Q_0)e_0+g\mathbf{Q}:\lambda\in GL_{\mathbb{R}}(\mathbb{C}),\ g\in SO(3,\mathbb{R})\bigr\}
\cong GL(2,\mathbb{R})\times SO(3,\mathbb{R}),
$$

of real dimension seven, whose Lie algebra is $\mathrm{Der}(\diamond)$.

*Proof.* The derivations and the structure group are *The Adjoint Operators of the Antisymmetric
Quaternionic Sesqualgebra*, §*The Derivations and the Structure Group*; the Leibniz rule on the vector part is
the classical derivation condition of the cross product, whose solutions are the skew maps of
$\mathbb{R}^{3}$.

**Proposition (the coefficient conjugation is an automorphism).** The coefficientwise conjugation preserves
the product, $\overline{\tilde P\diamond\tilde Q}=\overline{\tilde P}\diamond\overline{\tilde Q}$, it is
conjugate-linear, and it is an antiunitary map of the form,
$K(\bar{\tilde P},\bar{\tilde Q})=\overline{K(\tilde P,\tilde Q)}$.

*Proof.* $\overline{\tilde P\diamond\tilde Q}=\overline{\mathbf P\times\overline{\mathbf Q}}=\overline{\mathbf P}\times\mathbf Q=\overline{\tilde P}\diamond\overline{\tilde Q}$,
using that the coefficient conjugation is an involution; the form statement is the same computation on the scalar pairing.
Verified on fifty random pairs for the product law and thirty for the form law.

**Read as a physical statement.** The symmetries of the product are an arbitrary real-linear relabelling of
the scalar coordinate and a rotation of the vector part, while the form $K$ is preserved by the larger group
$U(1,3)$. The metric and the product therefore have different symmetries: the product is a direction
structure, the form a gauge structure. This is a reading.

## The Sandwich of the Band and Its Adjoint

The band has no unit and no associativity, so its sandwich is not built from an inverse, and its comparison with the parent's inner automorphism compares two different objects.

**Theorem (the sandwich, its value and its adjoint).** The diagonal two-sided operator of the band is

$$
\Theta^{\diamond}_{\tilde A}=L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde A},\qquad
\Theta^{\diamond}_{\tilde A}\tilde X=\mathbf A\times\bigl(\overline{\mathbf X}\times\mathbf A\bigr)
=(\mathbf A,\mathbf A)\,\overline{\mathbf X}-\mathbf A\,(\mathbf A,\overline{\mathbf X}),
$$

conjugate-linear, annihilating the centre, with
$\bigl(\Theta^{\diamond}_{\tilde A}\bigr)^{\dagger}=\Theta^{\diamond}_{\tilde A}$; and the general
two-sided operator has the adjoint
$\bigl(L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}\bigr)^{\dagger}=R^{\diamond}_{\overline{\tilde B}}L^{\diamond}_{\tilde A}$.

*Proof.* The value is the composite of the two definitions with the inner conjugation cancelled and the last
form is the triple-product identity; the adjoints are the identities of the preceding section. Verified on
sixty random parameters for the value law, sixty for the self-adjointness and sixty for the general adjoint.

**Theorem (the sandwich against the inner automorphism).** The band has no unit, so the parent's inner
automorphism $L_{\tilde A}R_{\tilde A^{-1}}$ of the ordinary product does not exist inside the band and is an
operator of the **composition** band. The band's sandwich uses the **same** parameter in both slots, is never
invertible, and is therefore never an automorphism; it is **equivariant** under the rotation part of the
structure group,

$$
\Theta^{\diamond}_{g\tilde A}\,g=g\,\Theta^{\diamond}_{\tilde A}
\qquad\text{for every }g\in SO(3,\mathbb{R}),
$$

so it transforms as an axial direction under the symmetries of the product.

*Proof.* The sandwich depends on $\mathbf A$, and $g$ acts on the vector part by a real orthogonal matrix of
determinant one, commuting with the coefficient conjugation, so
$g(\mathbf A\times(\overline{\mathbf X}\times\mathbf A))=g\mathbf A\times(\overline{g\mathbf X}\times g\mathbf A)$;
non-invertibility is the annihilation of the centre. Verified on thirty random parameters and rotations.

**Read as a physical statement.** In the composition band the sandwich and the inner automorphism agree
exactly on the unitary slice; here there is no slice, because there is no inner automorphism at all. The
band's sandwich reads an element through the product twice, and its symmetry is the rotation-equivariance of
an axial direction, not the conjugation of a group. The comparison with the model's sandwich is the crossing
reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*. This is a reading.

## The Operators Acting on the Gauge Space

The band's operators act on the algebra $\mathbb{B}$ itself, and that space carries the indefinite pairing: it is the gauge space and **not** the state space.

**Proposition (the space and the image of a multiplication).** The Krein form splits the algebra as an
orthogonal direct sum $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$, positive definite
on the centre and negative definite on the vector subspace, of realified signature $(2,6)$. For
$\tilde A\neq0$ the left multiplication is a conjugate-linear map of real rank four with

$$
\ker L^{\diamond}_{\tilde A}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\,\overline{\mathbf A},\qquad
\operatorname{im}L^{\diamond}_{\tilde A}=\bigl\{\mathbf V\in\mathbb{V}_{\mathbb{B}}:(\mathbf A,\mathbf V)=0\bigr\},
$$

and zero trace; the right multiplication has the same real invariants, being the conjugate of the left.

*Proof.* The decomposition and the inertia are *The Krein Gram Matrix and the Restrictions of the Form*; the
kernel, the image, the rank and the trace are *The Adjoint Operators of the Antisymmetric Quaternionic
Sesqualgebra*, §*The Matrix, the Rank and the Kernel*, confirmed here on the real basis and on sixty random
arguments.

**Proposition (the operator-pairing).** The trace of the composite of two left multiplications is the
conjugate-pairing of their parameters,

$$
\operatorname{Tr}_{\mathbb{C}}\bigl(L^{\diamond}_{\tilde P}L^{\diamond}_{\tilde Q}\bigr)
=-2\,(\mathbf P,\overline{\mathbf Q}),
$$

so the operator family reproduces the sesquilinear pairing of the vector parts of *The Sesquilinear Pairing
of the Antisymmetric Quaternionic Sesqualgebra*.

*Proof.* The composite is $\overline{\mathbf Q}(\mathbf P,\mathbf X)-(\mathbf P,\overline{\mathbf Q})\mathbf X$;
the rank-one part $X\mapsto\overline{\mathbf Q}(\mathbf P,\mathbf X)$ contributes
$+(\mathbf P,\overline{\mathbf Q})$ and the second term contributes $-3(\mathbf P,\overline{\mathbf Q})$ as
the trace of the negative of the projection onto the vector subspace, for the total
$-2(\mathbf P,\overline{\mathbf Q})$. Verified on forty random pairs.

**Read as a physical statement.** The states of the framework are not the gauge space: they are the elements
the indefinite metric cannot normalise, while the band's values are pure vectors. The left multiplication
sends **every** element into the plane perpendicular to its parameter and kills the centre and the conjugate
of its parameter's line; the centre is the scalar, potential-like direction and the image is the direction of
the polarisation, so the operator maps the whole frame to a direction. The trace pairing is the
operator-level form of the same statement: the family carries the pairing of the vector parts and no norm.
The state side is *The States the Indefinite Metric Cannot Normalise* and *Why the Fourth Product Is a Gauge
Structure and Not a State Space*. This is a reading.

## A Worked Case

**An isotropic vector parameter.** Take

$$
\tilde A=e_1+ie_2,\qquad \mathbf A=(1,i,0),\qquad
(\mathbf A,\mathbf A)=0,\qquad (\mathbf A,\overline{\mathbf A})=2,\qquad K(\tilde A,\tilde A)=-2 .
$$

The vector part is isotropic for the bilinear dot, the case the diagonal of the product reads:
$\tilde A\diamond\tilde A=\mathbf A\times\overline{\mathbf A}=-2i\,e_3$. The left multiplication is

$$
L^{\diamond}_{\tilde A}e_1=-i\,e_3,\qquad L^{\diamond}_{\tilde A}e_2=e_3,\qquad
L^{\diamond}_{\tilde A}e_3=i\,e_1-e_2,\qquad L^{\diamond}_{\tilde A}(ie_3)=e_1+ie_2=\tilde A,
$$

with kernel $\mathbb{C}e_0\oplus\mathbb{C}(e_1-ie_2)$, since $L^{\diamond}_{\tilde A}(e_1-ie_2)=0$, and image
the plane $\{(V_1,V_2,V_3):V_1+iV_2=0\}$, of real rank four. The sandwich, using $(\mathbf A,\mathbf A)=0$,
reduces to a rank-two map onto the complex line $\mathbb{C}\tilde A$,

$$
\Theta^{\diamond}_{\tilde A}\tilde X=-\mathbf A\,(\mathbf A,\overline{\mathbf X}),\qquad
\Theta^{\diamond}_{\tilde A}e_1=-\tilde A,\qquad \Theta^{\diamond}_{\tilde A}e_2=e_2-ie_1,\qquad
\Theta^{\diamond}_{\tilde A}e_3=0,
$$

and it is self-adjoint with $K(\Theta^{\diamond}_{\tilde A}e_1,e_1)=+1$ and
$K(\Theta^{\diamond}_{\tilde A}e_1,\Theta^{\diamond}_{\tilde A}e_1)=-2$.

**A real parameter for contrast.** Take $\tilde A=e_1$, with $(\mathbf A,\mathbf A)=1$,
$L^{\diamond}_{e_1}e_2=e_3$, $L^{\diamond}_{e_1}e_3=-e_2$, $L^{\diamond}_{e_1}(ie_2)=-ie_3$,
$L^{\diamond}_{e_1}(ie_3)=ie_2$. The sandwich is the projection onto the plane perpendicular to $e_1$ followed
by the coefficient conjugation of the vector part,
$\Theta^{\diamond}_{e_1}\tilde X=\overline{\mathbf X}-e_1(\overline{\mathbf X},e_1)$, so
$\Theta^{\diamond}_{e_1}e_2=e_2$, $\Theta^{\diamond}_{e_1}e_3=e_3$, $\Theta^{\diamond}_{e_1}(ie_2)=-ie_2$,
$\Theta^{\diamond}_{e_1}(ie_3)=-ie_3$, $\Theta^{\diamond}_{e_1}e_1=0$; it is self-adjoint, and the real
parameter is the case in which the sandwich is a conjugation on the plane.

**The closure witness.** At $(\tilde A,\tilde B,\tilde X)=(e_1,ie_1,e_2)$ the commutator of two left multiplications is

$$
\bigl[L^{\diamond}_{e_1},L^{\diamond}_{ie_1}\bigr]e_2=2i\,e_2,
\qquad\text{while}\qquad
L^{\diamond}_{e_1\diamond ie_1}e_2=L^{\diamond}_{0}e_2=0,
$$

so the commutator is not a multiplication; the term $2i\mathbf X$ is the multiple of the identity that the
conjugation produces.

**A numerical check.** Verified to machine precision: the four composition laws on sixty random triples
each; the square law on fifty; the two variable and the two parameter parities on sixty each; the
antisymmetry link on fifty; the three adjoint identities on sixty each; the commutator formula, the real-form
law and the closure count on sixty triples each (sixty failures on complex triples, none on real ones); the
type criteria and the non-$J$-unitarity on sixty parameters each; the automorphism property of the
coefficient conjugation, the kernel, image and rank, the trace pairing and the sandwich value, self-adjointness
and equivariance laws on thirty to sixty elements each; and the worked-case values on the exact elements
displayed.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must declare.

- **The composition laws are applied, not re-proved.** The left family, its rank, its kernel, its adjoint and its derivations are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*; the article verifies the formulas and reads them.
- **The product and its laws are the band's first article.** The rule, the conjugate-alternation, the non-vanishing diagonal and the axial reading are *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*, cited and not repeated.
- **The Jacobi failure, its witness and the higher structure are the band's other two articles.** *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure* owns the failure and the invisibility on the real forms; *A Higher Structure for the Jacobi Failure* owns the positive reading; this article states only the closure failure of the **operators**, a statement about the commutator and not about the cyclic sum.
- **The indefinite adjoint and its type criteria are applied, not derived.** The $J$-adjoint, the type criteria and the $J$-unitary group are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*; the indefinite sandwich is *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions*.
- **The form, the metric and the state side are not re-read here.** *The Fourth Product and Its Indefinite Metric*, *The States the Indefinite Metric Cannot Normalise* and *Why the Fourth Product Is a Gauge Structure and Not a State Space* own the metric, the null states and the no-go statement.
- **The physical adjoint is not this adjoint.** The observables and the gauge generators are read with the **definite** Hermitian adjoint of the probability band, in *Observables, Gauge Generators and the Chirality of the Internal Action*; this article's adjoint is the **indefinite** one.
- **The four adjoints are not compared here.** The comparison, block against block, is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this article declares only the $\mathrm{AQS}$ column.

**What the framework does not claim.** The reading does not derive the polarisation, the spin or the self-helicity from the operator calculus; it reads structures the corpus already uses. It does not identify the skew-adjoint multiplications with gauge generators, and it does not claim that the band is a Lie algebra, a monoid or a group. It does not claim that the twelve rows are one calculus; the antisymmetric quaternionic sesquilinear row is the row in which the adjoint is a negation, and that is its own.

## The Ledger

**Proved.** The band's multiplications are $L^{\diamond}_{\tilde A}(\tilde X)=\mathbf A\times\overline{\mathbf X}$,
conjugate-linear in the argument and $\mathbb{C}$-linear in the parameter, and
$R^{\diamond}_{\tilde A}(\tilde X)=\mathbf X\times\overline{\mathbf A}$, $\mathbb{C}$-linear in the argument
and conjugate-linear in the parameter, with $L^{\diamond}_{\tilde A}=-C\circ R^{\diamond}_{\tilde A}$. The
composition laws are $L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}\tilde X=\mathbf A\times(\overline{\mathbf B}\times\mathbf X)$,
$R^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}\tilde X=(\mathbf X\times\overline{\mathbf B})\times\overline{\mathbf A}$,
$L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}\tilde X=\mathbf A\times(\overline{\mathbf X}\times\mathbf B)$
and $R^{\diamond}_{\tilde B}L^{\diamond}_{\tilde A}\tilde X=(\mathbf A\times\overline{\mathbf X})\times\overline{\mathbf B}$;
the composite of two left multiplications is $\mathbb{C}$-linear and not a multiplication, and the trace
pairing is $\operatorname{Tr}_{\mathbb{C}}(L^{\diamond}_{\tilde P}L^{\diamond}_{\tilde Q})=-2(\mathbf P,\overline{\mathbf Q})$.
The commutator is
$[L^{\diamond}_{\tilde A},L^{\diamond}_{\tilde B}]\tilde X=\overline{\mathbf B}(\mathbf A,\mathbf X)-\overline{\mathbf A}(\mathbf B,\mathbf X)-2i\operatorname{Im}(\mathbf A,\overline{\mathbf B})\mathbf X$;
it is the multiplication $R^{\diamond}_{-(\mathbf a\times\mathbf b)}$ and equals $L^{\diamond}_{\mathbf a\times\mathbf b}$
on the real forms, and off them it is not a multiplication, the witness $(e_1,ie_1,e_2)$ giving $2ie_2$
against $0$; the left family is not closed and carries no Lie algebra. The form of the band is the indefinite
Krein form of signature $(1,3)$, and the adjoint it defines is the twisted adjoint of the conjugate-linear
class with $(L^{\diamond}_{\tilde A})^{\dagger}=-L^{\diamond}_{\tilde A}$,
$(R^{\diamond}_{\tilde A})^{\dagger}=-R^{\diamond}_{\overline{\tilde A}}$ and
$(L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B})^{\dagger}=R^{\diamond}_{\overline{\tilde B}}L^{\diamond}_{\tilde A}$:
the adjoint reverses the parameter and keeps the side. The types are $L^{\diamond}_{\tilde A}$ self-adjoint
exactly for a central parameter and skew-adjoint for every parameter, and $R^{\diamond}_{\tilde A}$
self-adjoint exactly for $\mathbf A\in i\mathbb{R}^{3}$ and skew-adjoint exactly for $\mathbf A\in\mathbb{R}^{3}$;
no nonzero operator of the band is $J$-unitary, the $J$-unitaries form $U(1,3)$, and the norm criterion
$\lvert N\rvert=1$ belongs to the parent's plain sandwich. The derivations are
$\mathrm{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})\oplus\mathfrak{so}(3,\mathbb{R})$, of real dimension
seven, with structure group $GL(2,\mathbb{R})\times SO(3,\mathbb{R})$, and the coefficient conjugation is an
automorphism of the product and an antiunitary of the form. The sandwich is
$\Theta^{\diamond}_{\tilde A}\tilde X=(\mathbf A,\mathbf A)\overline{\mathbf X}-\mathbf A(\mathbf A,\overline{\mathbf X})$,
self-adjoint for $K$ for every parameter, non-invertible and $SO(3,\mathbb{R})$-equivariant; the parent's
inner automorphism is not an operator of the band. On the gauge space, of canonical decomposition
$\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$ and realified signature $(2,6)$, the left
multiplication has rank four, kernel $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\overline{\mathbf A}$, image the
plane $(\mathbf A,\cdot)=0$ and zero trace.

**Readings.** That the adjoint of the band is taken for the **indefinite** form and is a **negation of the
parameter** that keeps the side, where the composition band's transpose swaps the sides and the probability
band's Hermitian adjoint conjugates the parameter; that the band supplies **no self-adjoint generator**, all
its multiplications being skew-adjoint, so the antisymmetric half is a structure of directions and not of
observables; that the operators **do not close** to a Lie algebra, the failure being invisible on the real
quaternion forms and carried by a complex witness, while the closure that exists is the cross-product closure
of the real forms; that the sandwich is **self-adjoint for every parameter** and there is **no inner
automorphism** in the band to compare it with; that the operators act on the **gauge space**, send the whole
frame into the plane perpendicular to the parameter and kill the centre, so the polarisation direction is the
image and the centre is not a state; and that the band's criteria carry **no norm**. Each is the framework's
naming of a proved algebraic fact and is labelled as such.

## Physical Readings

Read under the job word **polarisation**, the article is the operator layer of the antisymmetric gauge
product, which pairs a vector with the conjugate of another and returns an axial direction (*The Cross
Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*). The first reading is that the
operators **carry a direction and not a state**: the left multiplication sends every element into the plane
perpendicular to its parameter, the image is a direction space, and no value of the band is an element the
indefinite metric can normalise. The second reading is that the adjoint is a **reversal of the parameter**:
transporting a direction across the pairing reverses its sense, the operator form of the axial character of
the cross product. The third reading is negative: the operators do not close to a Lie algebra, so the band
does not supply the internal symmetry algebra of the frame, and the closure that exists is the cross-product
closure of the real quaternion forms, invisible to a computation with real coefficients. Read against the
composition and probability bands, the three rows are three adjoints on one algebra: the transpose that swaps
the sides, the Hermitian adjoint that conjugates and keeps the side, and the indefinite adjoint that negates
the parameter and keeps the side. Read on the clock, the band's operators carry no central phase of their own,
because the centre is annihilated, so the band belongs entirely to the vector part. The placement in the
twelve is the final reading: the antisymmetric quaternionic sesquilinear row is the row where the bracket
fails, the adjoint negates, and the metric remains a gauge metric and not a state space.

## Summary

The antisymmetric quaternionic sesquilinear product is $\tilde P\diamond\tilde Q=\mathbf P\times\overline{\mathbf Q}$,
and its multiplication operators are the conjugate-linear left multiplication
$L^{\diamond}_{\tilde A}(\tilde X)=\mathbf A\times\overline{\mathbf X}$ and the $\mathbb{C}$-linear right
multiplication $R^{\diamond}_{\tilde A}(\tilde X)=\mathbf X\times\overline{\mathbf A}$, tied by the
conjugate-alternation $L^{\diamond}_{\tilde A}=-C\circ R^{\diamond}_{\tilde A}$. The composition law adopted
is $L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}\tilde X=\mathbf A\times(\overline{\mathbf B}\times\mathbf X)$;
the four laws are displayed and were verified on sixty random triples each. The composite of two left
multiplications is $\mathbb{C}$-linear and is not a multiplication, so the family is not closed; the
commutator
$\overline{\mathbf B}(\mathbf A,\mathbf X)-\overline{\mathbf A}(\mathbf B,\mathbf X)-2i\operatorname{Im}(\mathbf A,\overline{\mathbf B})\mathbf X$
is a multiplication on the real forms and a non-multiplication off them, with the complex witness
$(e_1,ie_1,e_2)$ giving $2ie_2$ against $0$. The band carries **no Lie algebra**, the failure is invisible on
the real quaternion forms, and the positive reading of the same failure as a higher structure is the band's
own article. The form of the band is the indefinite Krein form of signature $(1,3)$, and its adjoint
**reverses the parameter and keeps the side**:
$(L^{\diamond}_{\tilde A})^{\dagger}=-L^{\diamond}_{\tilde A}$,
$(R^{\diamond}_{\tilde A})^{\dagger}=-R^{\diamond}_{\overline{\tilde A}}$ and
$(L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B})^{\dagger}=R^{\diamond}_{\overline{\tilde B}}L^{\diamond}_{\tilde A}$.
Every left multiplication is skew-adjoint and the only self-adjoint one is zero; the right multiplication is
self-adjoint exactly for a purely imaginary vector part; no nonzero operator of the band is $J$-unitary, the
$J$-unitary group being the parent's $U(1,3)$, and the norm criterion $\lvert N\rvert=1$ belongs to the
parent's plain sandwich. The derivations are
$\mathrm{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})\oplus\mathfrak{so}(3,\mathbb{R})$ of dimension seven, the
structure group is $GL(2,\mathbb{R})\times SO(3,\mathbb{R})$, the coefficient conjugation is an automorphism
of the product and an antiunitary of the form, and the metric and the product have different symmetries. The
sandwich $\Theta^{\diamond}_{\tilde A}=L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde A}$ is self-adjoint for $K$
for **every** parameter, non-invertible and $SO(3,\mathbb{R})$-equivariant; the inner automorphism of the
parent is not an operator of the band, so the comparison degenerates and the degeneration is the reading. On
the gauge space the left multiplication has rank four, kernel
$\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\overline{\mathbf A}$, image the plane $(\mathbf A,\cdot)=0$ and zero
trace, and the trace pairing of two left multiplications is $-2(\mathbf P,\overline{\mathbf Q})$, the
sesquilinear pairing of the vector parts. The worked case gives the isotropic parameter $e_1+ie_2$ with
$(\mathbf A,\mathbf A)=0$, $(\mathbf A,\overline{\mathbf A})=2$, $\tilde A\diamond\tilde A=-2ie_3$, the
sandwich image the line $\mathbb{C}\tilde A$, and the closure witness
$[L^{\diamond}_{e_1},L^{\diamond}_{ie_1}]e_2=2ie_2$. Read under polarisation, the operators carry a direction
and not a state, the adjoint reverses the parameter's sense, the front of the frame is the plane perpendicular
to the parameter, and the band does not close to an algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf P\times\overline{\mathbf Q}$ | The antisymmetric quaternionic sesquilinear product, $\mathrm{AQS}$ |
| $L^{\diamond}_{\tilde A}(\tilde X)=\mathbf A\times\overline{\mathbf X}$ | Left multiplication; conjugate-linear in the argument, $\mathbb{C}$-linear in the parameter |
| $R^{\diamond}_{\tilde A}(\tilde X)=\mathbf X\times\overline{\mathbf A}$ | Right multiplication; $\mathbb{C}$-linear in the argument, conjugate-linear in the parameter |
| $L^{\diamond}_{\tilde A}=-C\circ R^{\diamond}_{\tilde A}$ | The antisymmetry link between the two families |
| $L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}\tilde X=\mathbf A\times(\overline{\mathbf B}\times\mathbf X)$ | The composition law adopted |
| $[L^{\diamond}_{\tilde A},L^{\diamond}_{\tilde B}]\tilde X=\overline{\mathbf B}(\mathbf A,\mathbf X)-\overline{\mathbf A}(\mathbf B,\mathbf X)-2i\operatorname{Im}(\mathbf A,\overline{\mathbf B})\mathbf X$ | The commutator; not a multiplication off the real forms |
| $(e_1,ie_1,e_2)$, $2ie_2$ | The complex closure witness and its value |
| $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | The indefinite Krein form, $\varepsilon=(1,-1,-1,-1)$ |
| $(L^{\diamond}_{\tilde A})^{\dagger}=-L^{\diamond}_{\tilde A}$, $(R^{\diamond}_{\tilde A})^{\dagger}=-R^{\diamond}_{\overline{\tilde A}}$ | The adjoint reverses the parameter and keeps the side |
| $L^{\diamond}_{\tilde A}$ self-adjoint $\iff\mathbf A=0$; skew-adjoint always | The left types |
| $R^{\diamond}_{\tilde A}$ self-adjoint $\iff\mathbf A\in i\mathbb{R}^{3}$; skew-adjoint $\iff\mathbf A\in\mathbb{R}^{3}$ | The right types |
| $U_{J}(\mathbb{B})\cong U(1,3)$, $\lvert N(\tilde Q)\rvert=1$ | The $J$-unitary group and the norm criterion of the parent's plain sandwich |
| $\mathrm{Der}(\diamond)=\mathrm{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})\oplus\mathfrak{so}(3,\mathbb{R})$ | The derivations, real dimension seven |
| $GL(2,\mathbb{R})\times SO(3,\mathbb{R})$ | The structure group of the product |
| $\Theta^{\diamond}_{\tilde A}\tilde X=(\mathbf A,\mathbf A)\overline{\mathbf X}-\mathbf A(\mathbf A,\overline{\mathbf X})$ | The band's sandwich; self-adjoint for every parameter |
| $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$ | The gauge space; centre and vector subspace |
| $\ker L^{\diamond}_{\tilde A}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\overline{\mathbf A}$, $\operatorname{im}L^{\diamond}_{\tilde A}=\{(\mathbf A,\cdot)=0\}$ | The kernel and image; rank four, nullity four |
| $\operatorname{Tr}_{\mathbb{C}}(L^{\diamond}_{\tilde P}L^{\diamond}_{\tilde Q})=-2(\mathbf P,\overline{\mathbf Q})$ | The trace pairing of the left family |

## Further Reading

- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the left multiplication, its matrix, rank, kernel and image, the adjoint, the derivations, the structure group and the composition.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, the slot parities and the conjugate-alternation.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the diagonal, the Jacobi failure and the failure off the real forms.
- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the pairing of a value with a third element and the trace form.
- *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the indefinite adjoint, the dictionary with the definite case, the type criteria, the group $U(1,3)$ and the norm criterion.
- *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-indefinite-hermitian-sandwich-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the sandwich by the indefinite adjoint, its laws, the form-preservation and the transport.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the inertia of $K$ and its restrictions, and *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for $J$.
- *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product* (`articles_physics/the-cross-product-of-a-vector-with-its-conjugate-the-antisymmetric-gauge-product.md`), the framing article of the band.
- *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure* (`articles_physics/a-bracket-invisible-on-the-real-forms-the-complex-witness-of-the-jacobi-failure.md`) and *A Higher Structure for the Jacobi Failure* (`articles_physics/a-higher-structure-for-the-jacobi-failure.md`), for the Jacobi failure, its witness and the higher structure.
- *The Operators of the Quaternionic Sesquilinear Product and the Indefinite Gauge Metric* (`articles_physics/the-operators-of-the-quaternionic-sesquilinear-product-and-the-indefinite-gauge-metric.md`), the indefinite sibling row, whose adjoint swaps the sides where this one negates the parameter, and *The Operators of the Ordinary Product: One-Sided, Two-Sided and the Sandwich* (`articles_physics/the-operators-of-the-ordinary-product-one-sided-two-sided-and-the-sandwich.md`), the composition-band model.
- *The Fourth Product and Its Indefinite Metric* (`articles_physics/the-fourth-product-and-its-indefinite-metric.md`), *The States the Indefinite Metric Cannot Normalise* (`articles_physics/the-states-the-indefinite-metric-cannot-normalise.md`) and *Why the Fourth Product Is a Gauge Structure and Not a State Space* (`articles_physics/why-the-fourth-product-is-a-gauge-structure-and-not-a-state-space.md`), for the metric and the state side.
- *Observables, Gauge Generators and the Chirality of the Internal Action* (`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`), for the definite Hermitian adjoint of the observables, and *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing reader of the twelve.
