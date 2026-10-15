# __Annihilators in the Algebraic Structures of Biquaternions over $\mathbb{C}$__

## Introduction

The annihilator of an element in a product is the set of partners that the element kills. It is the kernel
of the operation "multiply by it", so it is the kernel of a process, and the physical reading of the
kernel is direct: a process is invertible exactly when its kernel is trivial, and the size of the kernel
measures how much the process forgets — it counts the independent inputs the operation merges into zero.
The twelve products of the biquaternion complex space define twelve annihilators for one element, and this
article reads them physically. It is the second physics companion of the mathematics comparison group, after
*Zero Divisors in the Algebraic Structures of Biquaternions over $\mathbb{C}$*, and the mathematics companion is *Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*
(`articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.md`).

The mathematics companion computes the annihilator of a general element in each of the twelve structures
and proves two theorems. The first: the two one-sided annihilators, the left one $\{\tilde X:\tilde P\star
\tilde X=0\}$ and the right one $\{\tilde X:\tilde X\star\tilde P=0\}$, are equal in ten of the twelve
structures and differ in exactly two, the plain product $\tilde P\tilde Q$ and the general quaternionic
sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$, and there only at an element of vanishing
biquaternion norm. The second: the four planes of a cone element in the four general products are one
plain plane read through the two conjugations. The physical thesis of this article is that these two
theorems are statements about operators: a symmetric or one-slot product has one kernel, the plain
composite and the gauge coupling have two, and the difference between the two sides is the chirality of an
operation against its adjoint.

Four physical objects of the annihilator table organise the article. The **invertible operation** is the
element whose annihilator is the origin alone. The **lightlike operation** is the cone element, whose
annihilator is a plane of other lightlike directions, so that a null direction can be killed only along
null directions. The **scalar-valued coupling** is the symmetrisation that returns a number; its
annihilator is a hyperplane, and the hyperplane is the set of partners with which the coupling gives zero,
the physical form of orthogonal amplitudes. The **bracket** is the antisymmetrisation; its annihilator is
the centraliser of the element, and at a central element, which is a global phase, the bracket kills the
whole algebra.

The article proceeds as follows. It first fixes the annihilator as the kernel of an operation and reads
invertibility as trivial kernel. It then reads the two-sided theorem as chirality, the four general planes
as the lightlike kernel, the hyperplane rows as zero overlap, and the bracket rows as the centraliser. It
then reads the kernel in the quantum corpus and again in the corpus's cohomology, its constraint equations,
its polarisation operator and its information channels. A table collects the twelve annihilators with one
physical clause each, and the closing sections are the
ledger, the interpretation, the summary, the notation table and the literature. The other articles of the
section own the objects that the table touches: *Zero Divisors in the Algebraic Structures of Biquaternions over $\mathbb{C}$* the
degeneracy itself, *Square Roots of Minus One, Zero and Plus One in the Algebraic Structures of Biquaternions over $\mathbb{C}$* and
*Square Roots of a General Element in the Algebraic Structures of Biquaternions over $\mathbb{C}$* the radicands, *Idempotents in the Algebraic Structures of Biquaternions over $\mathbb{C}$* the projectors, and *Nilpotents in the Algebraic Structures of Biquaternions over $\mathbb{C}$* the square-zero
elements.

**Conventions.** We use those of the companion articles unchanged. The algebra is
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$ and
$e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; $i$ is the central scalar imaginary. The conjugations are
${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The biquaternion norm is
$N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$, whose vanishing locus is the cone; the trace
is $\mathrm{Tr}=2\,\mathrm{Sc}$; the material coordinate is $\tilde Q=ict\,e_0+\vec x$. The twelve
structures are cited by their three-letter names, and the left and right annihilators are written
$A_\star(\tilde P)$ and $B_\star(\tilde P)$ as in the mathematics companion.

## The Annihilator as the Kernel of an Operation

**Definition and kernel.** For a product $\star$ and an element $\tilde P$, the left and right
annihilators are

$$
A_\star(\tilde P)=\{\tilde X:\tilde P\star\tilde X=0\},\qquad
B_\star(\tilde P)=\{\tilde X:\tilde X\star\tilde P=0\},
$$

which are the kernels of the left and right multiplications $L_{\tilde P}$ and $R_{\tilde P}$. Each is a
complex subspace, and its dimension is the number of free complex parameters left by one equation. Read as
an operation, an element is the map "multiply by it" (*The Monoid of Acting Maps: the Process Is the
Multiplication, the State Is the Idempotent*), and the annihilator is the kernel of that map.

**Invertibility is trivial kernel.** An element has a two-sided plain inverse exactly when
$N(\tilde P)\neq0$, the inverse being $\tilde P^{\natural}/N(\tilde P)$, and then multiplying by
$\tilde P$ is a bijection, so its annihilator is the origin alone. On the cone the multiplication drops
rank and the annihilator is a nonzero subspace. The physical statement is the usual one for maps: a
process is reversible if and only if it loses nothing, and the dimension of the annihilator is the number
of independent inputs the process sends to zero. The corpus's operator articles read the rank of the
multiplications directly, in *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the
Sandwich* and *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*.

**The annihilator lies in the zero-divisor set.** When $\tilde P\neq0$ kills $\tilde X\neq0$, the element
$\tilde X$ is itself a zero divisor of the same product with witness $\tilde P$. Every nonzero element of
an annihilator is therefore a zero divisor, and for the four general products, whose zero-divisor set is
the cone, the whole annihilator lies on the cone. The physics is the sharp statement that the killers of a
lightlike element are lightlike: a null direction annihilates only along null directions. In the derived
structures the zero-divisor set is larger and the annihilator can leave the cone, the unit $e_1$ being
annihilated in the symmetrised products while off the cone, as *Zero Divisors in the Algebraic Structures
of Biquaternions over $\mathbb{C}$* records.

## The Two Sides: Chirality of an Operation

The two annihilators are the kernels of the left and right multiplications, and "left" and "right" are the
two ways an operation can act. When the two coincide, the operation has a single kernel; when they differ,
the operation kills different things depending on the side.

The mathematics companion proves that they differ in exactly two structures, the plain product
$\tilde P\tilde Q$ and the general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$,
and only at a cone element. The physical reading is a chirality. The plain product is the composition of
two material operations, which is not commutative, and the gauge coupling is its conjugate; in both, the
element and its conjugate play different roles on the two sides, so the left multiplication and the right
one are different maps with different kernels. In the other ten structures the product is commutative, or
conjugate-commutative, or alternating, and the exchange of the two factors does not change whether the
product vanishes, so the two kernels coincide. The corpus has already named the operator face of this
chirality: the internal action is one-sided, only the right multiplication by a unitary being an isometry
of the fourth product's form, in *Observables, Gauge Generators and the Chirality of the Internal Action*.
The two-sided theorem is the annihilator face of the same chirality.

At the non-pure cone element $e_0+ie_1$ the two plain planes are

$$
A_{\text{plain}}(e_0+ie_1)=\mathbb{C}\{e_0-ie_1,\ e_3+ie_2\},\qquad
B_{\text{plain}}(e_0+ie_1)=\mathbb{C}\{e_0-ie_1,\ e_3-ie_2\}.
$$

The two planes share the line of the natural conjugate $\tilde P^{\natural}=e_0-ie_1$ and differ in their
second generator, so the two-sided annihilator is the line of the conjugate and the operation kills the
conjugate on both sides but only one more direction on each side. The shared line is the physical residue
of the symmetry: $\tilde P\tilde P^{\natural}=N(\tilde P)e_0=0$ on the cone, so a lightlike element always
kills its own conjugate, whichever side the multiplication is taken.

## The Four General Products: the Lightlike Kernel

Fix a nonzero cone element, $N(\tilde P)=0$. Each of the four general products gives it a plane, and the
mathematics companion proves that the four planes are the plain plane read through the two conjugations,

$$
A_{\natural}(\tilde P)=A_{\text{plain}}(\tilde P^{\natural}),\qquad
A_{*}(\tilde P)=A_{\text{plain}}(\tilde P)^{*},\qquad
A_{\natural*}(\tilde P)=A_{\text{plain}}(\tilde P^{\natural})^{*}.
$$

At $e_0+ie_1$ the four left planes are the plain plane
$\mathbb{C}\{e_0-ie_1,e_3+ie_2\}$, the plain
sesquilinear plane $\mathbb{C}\{e_1+ie_0,e_2+ie_3\}$, the natural plane $\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$ and the general quaternionic sesquilinear plane
$\mathbb{C}\{e_0+ie_1,e_2-ie_3\}$.

The physical reading has two parts. First, the four planes are not four independent objects: they are one
plane and its two conjugates, so the four bands differ by which conjugation is applied to the kernel, not
by the kernel itself. The plain plane contains the lightlike directions that the composition sends to
zero, and the other three are its images, so the composition band determines the kernel of the pairing and
of the gauge band. Second, the plane is made of cone elements: the killers of a null momentum are null.
This is the algebraic form of the statement that a lightlike signal can be annihilated only by another
lightlike signal, and it is the reason the cone is closed under the annihilator operation on the four
general rows. The rank of the multiplications and the collapse of the congruences on the cone are read in
*The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions* and in *The Cone and
the Massless Particles in the Algebraic Structures of Biquaternions over $\mathbb{C}$*.

At the pure cone element $e_1+ie_2$ the plain planes are

$$
A_{\text{plain}}(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_0+ie_3\},\qquad
B_{\text{plain}}(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_0-ie_3\},
$$

so a lightlike element lies in its own annihilator, as it must: $\tilde P^{2}=0$ for a pure cone element,
and the square is the product of the element with itself. The self-annihilation of a lightlike
displacement is the elementary physical case, and *Nilpotents in the Algebraic Structures of Biquaternions over $\mathbb{C}$* reads it as
the square-zero class.

## The Hyperplane of a Scalar-Valued Coupling

Two structures collapse their product to a form: the symmetric plain sesqualgebra $\tilde P\star\tilde Q=H(\tilde P,\tilde Q)e_0$ with
$H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$, and the symmetric quaternionic algebra
$\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ with $N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$.
For each, the annihilator of
any nonzero element is the hyperplane cut by the form,

$$
P_0\overline{X_0}+(\vec P,\overline{\vec X})=0\quad\text{(SPS)},\qquad
P_0X_0+(\vec P,\vec X)=0\quad\text{(SQA)} .
$$

The physical object is a coupling that returns a number. A number has no slot in which to act, so the
operation "couple with $\tilde P$" is not an invertible map; it is a scalar functional, and its kernel is
a hyperplane. The reading of the hyperplane is orthogonality: the partners the coupling sends to zero are
the partners orthogonal to $\tilde P$ in the corresponding form. For the symmetric plain sesqualgebra the
form $H$ is the Born pairing, so its hyperplane is the set of amplitudes whose overlap with $\tilde P$ is
zero, that is, the amplitudes with which $\tilde P$ has zero transition amplitude. Orthogonal states
interfere to nothing, and the hyperplane is the algebraic home of that fact. For the symmetric
quaternionic algebra the form is $N$, the interval form at the two equal arguments, and the hyperplane is
its polar: the partners at zero interval with $\tilde P$.

The kernel of a scalar coupling is a hyperplane for every nonzero element, so in these two rows every
element destroys exactly one complex dimension of information. This is the largest annihilator a nonzero
element can have without killing the whole space, and it is the algebraic reason these two structures are
couplings and not compositions. The physical caveat is that the coupling is not invertible in any case;
its kernel is nonzero because a number cannot act, not because the element is lightlike. The owner articles
of the two rows are the symmetric structures of the coupling band, and the form $H$ and its cone are read
in *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*.

## The Bracket and the Centre: the Centraliser

The four antisymmetric structures are the brackets of the algebra, and their annihilators are the sets of
partners with which the bracket vanishes, that is, the **centralisers** of the element in the three cases
where the bracket is a commutator and its analogue. The clean physical case is the plain commutator
$\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\vec P\times\vec Q$, whose annihilator is
$\mathbb{C}e_0\oplus\mathbb{C}\vec P$: the partners the bracket sends to zero are the centre and the
element's own direction. Two facts follow, and both are physical.

- **An element lies in its own annihilator.** The bracket of an element with itself is zero, because a
  commutator is alternating, so every element is in its own centraliser. The physical statement is that
  the bracket measures non-commutativity, and an element commutes with itself.
- **A central element kills everything.** At $\tilde P=qe_0$ the vector part is zero and the bracket
  vanishes for every partner, so the annihilator is the whole algebra. A central element is a global
  phase: it commutes with every operation, and the bracket, which measures the failure to commute, does
  nothing to it. The centre is the kernel of the adjoint action, and the two rows of the table where some
  nonzero element has the whole space as its annihilator are exactly the two antisymmetrisations
  $\mathrm{APA}$ and $\mathrm{AQS}$.

The conjugate-alternating rows
$\mathrm{APS}$ and $\mathrm{AQS}$ act on the conjugate direction, and the rows whose bracket is
conjugate-alternating annihilate their own conjugate rather than themselves in the generic case. The
general quaternionic antisymmetrisation separates the two cases of the cone by the size of the
annihilator: at an element of nonzero norm the annihilator is the line of the element itself, and at a
cone element it is a plane containing that line. The reading is the same as for the plain bracket, with
the norm deciding whether the centraliser grows from a line to a plane.

## The Twelve Annihilators and Their Physical Readings

An annihilator is the kernel of a multiplication: the set of operations a given operation sends to zero.
Each of the twelve structures carries its own kernel, and the twelve are read one by one below, each
naming its product, its annihilator and the physical interpretation, before the table collects the twelve
in one place.

### $\mathrm{GPA}$, the general plain algebra — composition

The product is $\tilde P\tilde Q$, and the annihilator is the kernel of the left or the right
multiplication by $\tilde P$. Off the cone both kernels are $\{0\}$, because the multiplication is
invertible. On the cone each kernel is a complex plane; the two planes share the line
$\mathbb{C}\tilde P^{\natural}$ and differ in their second generator, so left and right composition by a
lightlike element kill different directions. That is the chirality of the composition, the same one-sided
action the internal symmetry carries. *Annihilators of the General Plain Algebra* owns the planes, and
*The Operators of the General Plain Bilinear Product* the operator.

### $\mathrm{GPS}$, the general plain sesqualgebra — probability

The product is the pairing $\tilde P\tilde Q^{*}$, conjugate-commutative, so there is a single annihilator.
Off the cone it is $\{0\}$; on the cone it is the star-image of the plain plane, the set of the
$\tilde Z^{*}$ with $\tilde P\tilde Z=0$. The kernel of the pairing is the conjugate image of the kernel
of the composition, which is how the Born pairing reads a lightlike direction. The reading is *Mass, Rank
and the Positivity of the Dagger*.

### $\mathrm{GQA}$, the general quaternionic algebra — causality

The product is $\tilde P^{\natural}\tilde Q$, and its two multiplications have the same kernel. Off the
cone the annihilator is $\{0\}$; on the cone it is one plane containing the line $\mathbb{C}\tilde P$. The
natural product has a single kernel, and a lightlike element lies in its own kernel. The reading is *The
Interval as the Square and the Charge of the Material Composition*.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra — gauge

The product is the fourth product $\tilde P^{\natural}\tilde Q^{*}$. Off the cone each annihilator is
$\{0\}$; on the cone each is a complex plane, and the two planes are distinct, meeting exactly in the line
$\mathbb{C}\tilde P^{*}$. The gauge coupling is chiral like the plain composition, and the shared line is
the lightlike gauge direction the two sides cannot separate. The reading is *The Fourth Product and Its
Indefinite Metric*.

### $\mathrm{SPA}$, the symmetric plain algebra — commutativity

The product is the Jordan product $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, which is commutative, so
there is a single annihilator. Off the cone with $P_0\neq0$ it is $\{0\}$; on the cone with $P_0\neq0$ it
is the line $\mathbb{C}\tilde P^{\natural}$; and at a pure element it is the plane
$\{X_0=0,\ (\vec P,\vec X)=0\}$. A pure operation therefore kills the plane of operations
orthogonal to it. The reading is *The Symmetrised Material Composition and the Jordan Identity*.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra — positivity

The product is the scalar-valued symmetrisation, so the annihilator is the hyperplane
$H(\tilde P,\tilde X)=0$. It is the polar hyperplane of the positive definite Born form: the amplitudes of
zero overlap with $\tilde P$. The form is definite, so the kernel is never larger than a hyperplane. The
reading is *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra — coupling

The product is the scalar-valued symmetrisation $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$, so the
annihilator is the complex hyperplane $N(\tilde P,\tilde X)=0$. A scalar coupling kills exactly the
operations orthogonal to $\tilde P$, and a number cannot act: the kernel has the largest dimension a
nonzero element can have without killing everything. The reading is *The Quaternion Form as a Product: the
Scalar Coupling of Two Material Operations*.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra — metric

The product is the symmetrisation, conjugate-commutative, so there is a single annihilator: $\{0\}$ off
the cone with $P_0\neq0$, the line $\mathbb{C}\tilde P^{*}$ on the cone with $P_0\neq0$, and the plane
$\{X_0=0,\ K(\tilde P,\tilde X)=0\}$ at a pure element. The symmetric gauge coupling separates its two
families by the size of the kernel, a plane at a pure element against a line at a non-pure one. The
reading is *The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product*.

### $\mathrm{APA}$, the antisymmetric plain algebra — rotation

The product is the commutator $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\vec P\times\vec Q$. At
a non-central element the annihilator is the plane $\mathbb{C}e_0\oplus\mathbb{C}\vec P$, the centre
together with the element's own direction; at a central element it is the whole space. The bracket, which
measures non-commutativity, is blind to the centre, so a global phase is annihilated by everything. The
reading is *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra — phase

The product is the antisymmetrisation, the vector part of the pairing. Off the cone the annihilator is the
line $\mathbb{C}\overline{\tilde P}$; on the cone it is the star-image of the plain plane. The conjugate
bracket reads the conjugate direction, and that is the phase side of the Born pairing. The reading is *The
Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra — obstruction

The product is the antisymmetrisation. Its annihilator is the line $\mathbb{C}\tilde P$ when the norm is
nonzero and a complex plane containing that line when the norm vanishes; at a central element it is the
centre $\mathbb{C}e_0$. This is the centraliser of the quaternionic bracket, with the norm deciding line
against plane. The reading is *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator*.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra — polarisation

The product is the conjugate cross product $\vec P\times\overline{\vec X}$. At a non-central element
the annihilator is the plane $\mathbb{C}e_0\oplus\mathbb{C}\overline{\vec P}$; at a central element it
is all of $\mathbb{B}$. The centraliser of the conjugate bracket is the centre together with the conjugate
direction, and a global phase is annihilated by everything. The reading is *The Cross Product of a Vector
with Its Conjugate: the Antisymmetric Gauge Product*.

### The Twelve Annihilators in One Table

The table collects the twelve products, the annihilator of a general element in each, and the physical
interpretation.

| structure | product | annihilator of a general $\tilde P$ | physical reading |
|---|---|---|---|
| GPA | $\tilde P\tilde Q$ | $\{0\}$ off the cone; two distinct planes through $\mathbb{C}\tilde P^{\natural}$ on the cone | an invertible composition has trivial kernel; a lightlike one is chiral, killing different directions on the two sides |
| GPS | $\tilde P\tilde Q^{*}$ | $\{0\}$ off the cone; the star-image of the plain plane on the cone | the pairing's kernel is the conjugate image of the composition kernel |
| GQA | $\tilde P^{\natural}\tilde Q$ | $\{0\}$ off the cone; one plane containing $\mathbb{C}\tilde P$ on the cone | the natural product has one kernel, and a lightlike element lies in it |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | $\{0\}$ off the cone; two distinct planes through $\mathbb{C}\tilde P^{*}$ on the cone | the gauge coupling is chiral, like the plain composition |
| SPA | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $\{0\}$ off the cone with $P_0\neq0$; the line $\mathbb{C}\tilde P^{\natural}$ on the cone; the plane $\{X_0=0,(\vec P,\vec X)=0\}$ for $P_0=0$ | the symmetric composition has one kernel; a pure operation kills the plane orthogonal to it |
| SPS | $H(\tilde P,\tilde Q)e_0$ | the hyperplane $H(\tilde P,\tilde X)=0$ | the Born pairing kills the amplitudes orthogonal to $\tilde P$: zero overlap |
| SQA | $N(\tilde P,\tilde Q)e_0$ | the hyperplane $N(\tilde P,\tilde X)=0$ | a scalar coupling kills the orthogonal hyperplane; a number cannot act |
| SQS | the symmetrisation | $\{0\}$ off the cone with $P_0\neq0$; the line $\mathbb{C}\tilde P^{*}$ on the cone; the plane $\{X_0=0,K(\tilde P,\tilde X)=0\}$ for $P_0=0$ | the symmetric gauge coupling has one kernel, a plane at a pure element against a line at a non-pure one |
| APA | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | the plane $\mathbb{C}e_0\oplus\mathbb{C}\vec P$ for $\vec P\neq0$; the whole space for a central element | the bracket's centraliser is the centre and the element's own direction; a global phase is annihilated by everything |
| APS | the antisymmetrisation | $\{0\}$ off the cone; the line $\mathbb{C}\overline{\tilde P}$ at nonzero norm; the star-image of the plain plane on the cone | the conjugate bracket reads the conjugate direction |
| AQA | the antisymmetrisation | a line or a plane through $\mathbb{C}\tilde P$; the centre for a central element | the quaternionic bracket's centraliser, with the norm deciding line against plane |
| AQS | the antisymmetrisation | the plane $\mathbb{C}e_0\oplus\mathbb{C}\overline{\vec P}$ for $\vec P\neq0$; the whole space for a central element | the conjugate bracket's centraliser; a global phase is annihilated by everything |

Four facts of the table are physical statements, and the mathematics companion states all four.

- **The two sides differ in two rows, the plain composition and the gauge coupling.** Left multiplication
  and right multiplication by a lightlike element are different operations with different kernels. This is
  the chirality of the composition, the same chirality that makes the internal action one-sided.
- **In two rows some element kills the whole algebra, and the elements are the scalars.** The two rows are
  the plain and the conjugate plain brackets, and a central element is a global phase. The bracket, the
  measure of non-commutativity, is blind to the centre.
- **In two rows every nonzero element has a hyperplane as its annihilator.** The two rows are the
  scalar-valued symmetrisations; every coupling destroys one complex dimension, because a number cannot
  act.
- **In the six remaining rows the annihilator is small off the cone, but not always trivial, and it grows
  on the cone.** The four general products $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$ and
  $\mathrm{GQS}$ have the origin alone off the cone and a plane of lightlike partners on it. The two
  antisymmetric sesquilinear structures $\mathrm{APS}$ and $\mathrm{AQA}$ are already non-injective off
  the cone: their annihilator is the line $\mathbb{C}\tilde P$, or its conjugate, because a bracket kills
  its own direction, and it grows to a plane on the cone. The two symmetric structures $\mathrm{SPA}$ and
  $\mathrm{SQS}$ are locally non-injective as well: every pure element, the unit $e_1$ included, has a
  complex plane as its annihilator, on the cone or off it, because a symmetrised coupling of a pure
  element with an orthogonal partner vanishes whether or not either factor is lightlike. The physical
  content is twofold. For a composition or a pairing the cone is the only locus of lost information, and
  the dimension of the kernel is the rank drop read by *Mass, Rank and the Positivity of the Dagger*. For
  a bracket or a symmetric coupling information is lost off the cone too: the bracket forgets its own
  direction, and the symmetrisation forgets the plane orthogonal to a pure direction, which is the kernel
  face of the zero-divisor enlargement of $\mathrm{SPA}$ and $\mathrm{SQS}$.

## What the Annihilator Decides

| claim | source | status |
|---|---|---|
| the annihilator is the kernel of the left or right multiplication | mathematics companion; operator articles | cited |
| an element off the cone has trivial annihilator in the four general products | mathematics companion; recomputed (no non-null sample has an annihilator) | verified |
| the killers of a cone element in the four general products lie on the cone | *Zero Divisors in the Algebraic Structures of Biquaternions over $\mathbb{C}$*; mathematics companion | cited |
| the two sides differ exactly for GPA and GQS, and only on the cone | mathematics companion, theorem; recomputed planes at $e_0+ie_1$ | verified |
| the plain planes at $e_0+ie_1$ share $\mathbb{C}(e_0-ie_1)$ and differ in the second generator | mathematics companion, example; recomputed | verified |
| the four general planes are one plane read through the two conjugations | mathematics companion, theorem; recomputed at $e_0+ie_1$ | verified |
| SPS and SQA annihilators are hyperplanes; the APA and AQS annihilator is the whole space at a central element | mathematics companion; recomputed for SQA at $e_0$ and APA at $e_1$, AQS at $e_0$ | verified |
| the SQS annihilator is a plane at a pure element and a line at a non-pure cone element | mathematics companion; recomputed at $e_1+ie_2$ and $e_0+ie_1$ | verified |
| the physical readings (chirality, zero overlap, centraliser, lightlike kernel, zero-mode count, GNS null space, no-cloning) | this article; owners cited in the text | interpretation |
| the gauge orbit lies in the kernel of the field-strength map | *The Covariant Derivative and Gauge Connection in Biquaternionic Form* | cited |
| the index is a kernel dimension: the chiral zero-mode count equals the topological charge | *The Index Theorem and the Zero-Mode Count in Biquaternionic Form* | cited |

## The Kernel in the Quantum Corpus: Zero Modes, Null Spaces and No-Cloning

The annihilator is the kernel of a multiplication, and the quantum corpus already gives the kernel three
further jobs. Setting them beside the table makes the annihilator's physical content more than a
bookkeeping of rank drops.

**The zero-mode count.** The dimension of the annihilator is the number of independent inputs the operation
sends to zero, which is the elementary form of the count an index theorem performs. *The Index Theorem and
the Zero-Mode Count in Biquaternionic Form* counts the zero modes of a Dirac operator and equates their
chiral difference to a topological charge, the framework supplying the operator and the density and not the
counting. The annihilator of the multiplication by $\tilde P$ is the kernel whose dimension that theorem
counts in the field case: a nonzero kernel is a zero mode of the elementary operation, and the trivial
kernel of a unit is the absence of zero modes. The differential operator sits one level above the
multiplication, but the word "count" means the same dimension in both places.

**The GNS null space.** *The GNS Construction in the Biquaternion Framework* builds the Hilbert space of a
state as the quotient of the algebra by the state's null space,
$\mathcal N_\omega=\{\tilde A:\omega(\tilde A^{*}\tilde A)=0\}$, and finds that for the vacuum the null
space is the left ideal the annihilation operator lies in; the GNS space is then the minimal left ideal, of
complex dimension two, and the representation is irreducible. A state with a nontrivial null space is not
faithful, and its GNS space is smaller than the regular one. The annihilator of an element is the same
object for a single multiplication: a one-sided ideal the element kills, whose size measures how much of
the algebra the element overlooks. The vacuum's annihilator and the vacuum's GNS null space are two names
for one left ideal.

**The no-cloning obstruction.** *No-Cloning and the Algebraic Obstruction in Biquaternionic Form* locates
the obstruction in the trace pairing of two idempotents: a cloning map would have to preserve the pairing
and replace it by its square, and no linear map does both. The annihilator gives the obstruction in its
crudest form. An operation that kills a nonzero input is not invertible; an operation that is not
invertible has no inverse process; and the existence of a nonzero kernel is the failure of reversibility on
which every no-go theorem rests. The universal cloner of that article is a sum of conjugations and not a
unit, exactly as the irreversible channels of *Quantum Channels and the Reversible/Irreversible Dichotomy*
are sums rather than a single conjugation.

**Zero overlap and the centraliser.** The hyperplane and centraliser rows of the table are the two ways the
kernel becomes a physical relation. In the probability band the annihilator of $\tilde P$ is the set of
$\tilde X$ with $\langle\tilde P,\tilde X\rangle=0$, the set of amplitudes of zero overlap with
$\tilde P$; the annihilator of an amplitude is its orthogonal complement in the Born pairing, and
orthogonality of states is the standard physical instance of a nontrivial kernel. In the bracket rows the
annihilator is the centraliser, the set of partners that commute with the element; at a central element the
bracket kills the whole algebra, which is the operator form of the statement that the centre carries no
bracket and no gauge charge. *The Centre of the Biquaternion Algebra as the Classical Sector* reads the
centre as the gauge-blind part of the algebra, and the whole-space annihilator is that blindness written as
a kernel. *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form* reads the same
kernel as the redundancy of a gauge orbit: the directions a bracket annihilates are the directions that
carry no gauge-invariant information.

## The Kernel in Cohomology, Constraints, Polarisation and Channels

Four further jobs of the kernel are already written in the corpus, and each sharpens the annihilator
reading of the table by naming a different use of the same set.

**Cohomology: the kernel with the image removed.** *BRST Symmetry in Biquaternionic Form* constructs a
Grassmann-odd derivation $s$ with $s^{2}=0$ and identifies the physical states with its cohomology,
$\mathcal{H}_{\mathrm{phys}}=\ker s/\mathrm{im}\,s$. The annihilator of the nilpotent $s$ is the kernel
$\ker s$, and the cohomology is that kernel quotiented by the image. The reading is a sharpening of the
invertibility criterion: the kernel of an operation is the set it sends to zero, and when the operation is
a nilpotent differential the kernel contains the image as a subspace, so the physical content is the
kernel with the reachable part discarded. In the language of this article, the annihilator is the set of
states the differential does not reach, and the cohomology removes the states that are themselves reached
by it. The cohomology is the object the nilpotent article owns, read there as the odd nilpotent, and the
two companions meet at it.

**Constraints: the kernel of a divergence.** *The Schwinger–Dyson Equations and the Ward–Takahashi
Identities in Biquaternionic Form* derives, as the quantum Noether theorem, the statement that the Noether
current of the central phase is conserved inside correlation functions,
$\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J)=0$. A conserved current is a current in the kernel of the
divergence: the conservation equation says that the four-divergence of the current annihilates it, so the
physical currents are the annihilator of the divergence operator, and a current that fails conservation is
not in that kernel. The same article reads the abelian Ward identity as the vanishing of the longitudinal
part of the photon vacuum polarisation, $Z_1=Z_2$: the physical polarisations are the ones the transverse
projector leaves, so the longitudinal sector is what that projector kills. *Noether's Theorem in
Biquaternionic Form* locates the current in the material sector, so the constraint that defines the
physical current is a kernel in the same sector as the lightlike displacements of the zero-divisor
article. The kernel is the **classical** statement, and *Anomalies and Anomaly Cancellation in
Biquaternionic Form* records what quantisation does to it: the one-loop divergence of the current is not
zero, so the current is no longer in the kernel. For a global symmetry the failure is the physical axial
anomaly; for a gauge symmetry it is fatal unless the matter spectrum cancels it. The anomaly is therefore the
statement that the quantum current is **not** in the classical kernel of the divergence, and the cancellation
condition is the vanishing of the triangle coefficient — a condition on the matter spectrum that restores the
conservation.

**The kernel is observer-dependent.** A kernel belongs to an operator, and the operator a mode expansion
defines is not the same for every observer. *Bogoliubov Transformations in Biquaternionic Form* makes this
precise. A transformation with $v\neq0$ mixes $\tilde a$ with $\tilde a^{\dagger}$; the article records that
it is not implementable by a unitary on the Fock space of the original modes, that it maps the original
vacuum to a squeezed state, and that the two vacua are not unitarily equivalent as states of the same
algebra. The transformed annihilator therefore annihilates a different vacuum, and "the state of no
particles" is defined only relative to a choice of mode basis. The article adds the sharp caveat that the
biquaternion algebra holds exactly one mode: there the group is $O(2)=U(1)\rtimes\mathbb Z_2$, with no
continuous squeezing, so the continuous squeezing the thermal transformations need is a many-mode object
living in the module. *The Unruh Effect in Biquaternionic Form* and *Hawking Radiation in Biquaternionic
Form* are where that many-mode transformation is used: the inertial and the accelerated, or the in- and
out-, vacua are related by it, and the thermality of the radiation is the statement that the particle
notion, and with it the annihilator, has changed. The annihilator is thus not an observer-independent set;
it is the kernel that one's own mode expansion supplies.

**The kernel of the Dirac operator and the triple it belongs to.** *The Spectral Triple of the Biquaternion
Algebra* assembles the framework's own objects into Connes' triple $(\mathcal{A},\mathcal{H},D)$ — the
algebra, the spinor module, and the biquaternion Dirac operator $\mathcal{D}=\tilde\nabla+\tilde m$ — and is
scrupulous about what it does and does not establish. What it establishes is the candidate triple, the
spectral dimension four in the almost-commutative case, and a real-structure obstruction: the algebra's own
conjugation is an antilinear involution with $\flat^{2}=+1$, whereas four-dimensional spin geometry needs
$J^{2}=-1$, which here can only be supplied by the module's quaternionic structure, so the data are split
across algebra and module. What it explicitly does **not** claim is a distance: in the commutative case the
spectral triple recovers the distance from $D$ by a supremum over the algebra, while the framework's own
move derives a *signature* from the biquaternion norm, and the article says the two have the same shape but
are different theorems. The gauge fields, finally, appear as inner fluctuations of $D$,
$D\mapsto D+\sum_i a_i[D,b_i]$, which the article assigns to the standard neighbouring construction rather
than to a result of the series. The kernel table of this article and the triple are thus two readings of one
operator: the object that fails to vanish on the physical modes is also the object from which the geometry
and the gauge redundancy are read.

**Polarisation: the kernel of the skew operator.** *The Operators of the Antisymmetric Quaternionic
Sesquilinear Product and the Polarisation* computes the left multiplication of the row that this article
reads through the table, and finds

$$
\ker L^{\diamond}_{\tilde A}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\overline{\vec A},\qquad
\operatorname{im}L^{\diamond}_{\tilde A}=\{(\vec A,\cdot)=0\}.
$$

The kernel is the centre together with the conjugate direction of the parameter, and the image is the
plane perpendicular to it: the operator of that band maps the whole module into one direction and kills
the rest, which is why the article reads the band under the job word **polarisation**. The annihilator
rows of the two antisymmetric sesquilinear structures, which the table records as the identity lying in
its own kernel, are the algebraic statement of that image: an operator with a large kernel cannot be
inverted, and the physical content it keeps is the single direction it selects.

**Channels and the information the kernel destroys.** The dimension of the kernel is the information an
operation loses, and the corpus prices the loss. *The Holevo Bound and Accessible Information in
Biquaternionic Form* bounds the classical information recoverable from an ensemble by the Holevo
quantity. A measurement cannot separate two states exactly when every one of its positive operators
annihilates the difference of the two state elements under the trace pairing, so that both states give the
same outcome statistics and the distinction between them is inaccessible; the annihilator of the difference
is the kernel that holds the lost information. *Confinement and the Loss of Partonic Information in
Biquaternionic Form* supplies the sharpest case: the colour labels of an asymptotic state are not
redundant descriptions held in a kernel that a gauge choice could recover, they are absent from the
observable algebra, and the article distinguishes that loss from the gauge redundancy of *Gauge Redundancy
and the Information in the Gauge Orbit in Biquaternionic Form*, where the kernel is a redundancy. A kernel
therefore has two opposite readings, and the corpus keeps them apart: a gauge kernel hides a description, a
confinement kernel has destroyed one.

**The bracket's kernel is the classical sector.** The bracket's annihilator is the centraliser, and every
centraliser contains the centre. *The Centre of the Biquaternion Algebra as the Classical Sector* identifies
that centre $\mathbb{C}_{\mathbb{B}}=\{Q_0e_0\}\cong\mathbb{C}$ as the framework's canonical classical
sector: the largest commuting subalgebra, the set of observables fixed by every symmetry transformation, and
the home of the theory's **$c$-number parameters** — $\hbar$, $c$, a mass, a coupling, each of which enters
as a real multiple of $e_0$ and is central, so that the chirality-off-diagonal mass enters as the central
coefficient $me_0$. A bracket is the algebra's non-commutativity made into an operation, and its kernel is
therefore exactly the part of the algebra that does not contribute to it. The article also states the
boundary of the reading, and the annihilator inherits it: the algebra is central simple, so it has no
non-trivial central idempotents and no intrinsic superselection sectors, and the centre is a *minimal*
classical sector rather than a decomposition into classical branches.

**The kernel is forced by the product.** A conserved current is an element in the kernel of a divergence, and
*Gauge Curvature and the Bianchi Identity in Biquaternionic Form* exhibits a kernel the algebra supplies for
free. The field strength is not arbitrary: it satisfies the **Bianchi identity**
$D_\lambda F_{\mu\nu}+D_\mu F_{\nu\lambda}+D_\nu F_{\lambda\mu}=0$, and the article's own finding is that
this is not an analogy but a substitution — the covariant derivatives are operators in an associative
algebra, they satisfy the Jacobi identity identically, and the Bianchi identity is that Jacobi identity
rewritten through $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$. So the cyclic covariant derivative annihilates the
field strength on every connection, and the article proves the sharpness of the statement with a negative
control: replacing the two-sided derivative by a one-sided one destroys the identity, the cyclic sum becoming
nonzero of order unity. The annihilation is a consequence of associativity, the same property that makes the
BRST charge nilpotent; the kernel here is not a physical constraint imposed on the curvature but a
structural identity that any curvature built from a connection must satisfy.

**The annihilator need not be the complement.** *The Complementary Space of the Spinor Space and Its
Physical Meaning* separates two notions of "complement" that a naive reading would conflate, and the
separation is a warning the annihilator inherits. The spinor space $S=\mathbb{B}\tilde\Pi_1$ has a **module
complement** $\mathbb{B}\tilde\Pi_2$, the other Peirce summand, and it has a **Hilbert complement**, the
orthogonal complement for the algebra's sesquilinear form; the article proves that the two coincide, so the
annihilator of the native pairing is also the algebraic complement, and both are two-complex-dimensional. The
companion articles on the general plain algebra and the general plain sesqualgebra record the other case,
where the module split and the form's split **differ**. The kernel of a pairing is therefore band-dependent:
a subspace being annihilated need not make it the module complement, and the coincidence that holds for the
Born pairing is a property of that band rather than a general theorem.

**An identically conserved current is the topological case of the kernel.** *The Skyrme Model and the
Topological Baryon in Biquaternionic Form* gives the annihilator a second, stronger instance beside the
Bianchi one. The topological current of the chiral field,
$B^\mu=\frac{1}{24\pi^2}\varepsilon^{\mu\nu\rho\sigma}\mathrm{Tr}(j_\nu j_\rho j_\sigma)$ with
$j_\mu=\tilde U^{-1}\partial_\mu\tilde U$, is **conserved identically**: $\partial_\mu B^\mu=0$ holds without
any equation of motion, the divergence cancelling by antisymmetry of $\varepsilon$ and by the Maurer–Cartan
flatness of $j_\mu$. So the current lies in the kernel of the divergence as a matter of algebraic structure,
not as a consequence of dynamics. The contrast with Noether's theorem is what the companion should record:
Noether's current is conserved only **on shell**, so its divergence vanishes in the kernel of the divergence
*when the equations of motion hold*; the topological current's divergence vanishes *always*. The baryon
number is therefore not a Noether charge that a dynamics conserves but a **degree** of the map
$\tilde U:\mathbb{S}^3\to\mathbb{S}^3$, an integer fixed by the boundary data — the same shape of statement
the Bianchi identity makes, where associativity, not flatness, is what annihilates the derivative. The two
readings together sharpen the annihilator's meaning: the kernel is not only the obstruction a product cannot
escape, it is also the **identity** a density satisfies for structural reasons, and the corpus's topological
charges live in that second sense.

**The kernel generates the solution, and its dimension counts the moduli.** *Instantons and Solitons in
Biquaternionic Form* shows the annihilator doing field-theoretic work in two ways. First, the solutions of
the self-dual ansatz are **generated from the kernel** of a Fueter-type operator $\partial_t+D_3$, so that
solving the equation is finding what that operator annihilates: the kernel is not a loss of information but
the **source** of the configuration. Second, the instanton's collective coordinates are the **moduli** — the
eight-dimensional family of four translations, the dilatation $\rho$, and the three global $SU(2)$
orientations — the directions in which the configuration can be deformed at no cost in action, since the
article notes that the radius $\rho$ does not appear in the action and its constancy is the conformal
invariance of the Euclidean theory. The article's honest ledger belongs here too: the framework
supplies the **abelian** topological density but not the **non-abelian** one, because the latter needs a
bilinear carrying a second algebra index that the biquaternion norm does not have — a rank-two limitation
stated as a gap rather than smoothed over. The reading for this companion is that the kernel has a
constructive face beside its destructive one: it can be the space a solution is built from and the moduli it
is labelled by.

## Physical Interpretation

- The annihilator of an element is the kernel of the operation "multiply by it". A process is invertible
  exactly when its kernel is trivial, and the dimension of the kernel measures how much the process
  forgets: it counts the independent inputs the operation merges into zero.
- The killers of a lightlike element are lightlike. The annihilator of a cone element lies on the cone, and
  a null direction annihilates only along null directions.
- The two one-sided annihilators coincide in ten structures and differ in two, the plain composition and
  the gauge coupling. The difference is a chirality: an operation and its conjugate play different roles
  on the two sides, and at a lightlike element the left and right kernels are distinct planes.
- The four planes of a cone element in the four general products are one plain plane and its two conjugate
  images. The composition band determines the kernels of the pairing and of the gauge band.
- A scalar-valued coupling has a hyperplane as its annihilator. The hyperplane is the set of partners with
  which the coupling gives zero, which for the Born pairing is the set of amplitudes orthogonal to the
  element, that is, of zero overlap.
- A bracket has the centraliser as its annihilator. Every element lies in its own centraliser, and a
  central element, a global phase, is annihilated by every partner, so the bracket is blind to the centre.
  The centre is the framework's **classical sector** of *The Centre of the Biquaternion Algebra as the
  Classical Sector*: the home of the $c$-number parameters ($\hbar$, $c$, a mass, a coupling), so the
  bracket's kernel contains exactly the data that are classical rather than quantum; the classical sector is
  minimal, since the algebra is central simple and has no intrinsic superselection sectors.
- The kernel can also be **structural**, not a constraint. The Bianchi identity of *Gauge Curvature and the
  Bianchi Identity in Biquaternionic Form* says the cyclic covariant derivative annihilates every field
  strength, and it is the operator Jacobi identity rewritten: the annihilation follows from the associativity
  of the product, and it holds on every connection rather than being imposed on the curvature.
- The kernel is band-dependent. *The Complementary Space of the Spinor Space and Its Physical Meaning* proves
  that for the native pairing the module complement and the Hilbert complement coincide, while the general
  plain algebra and sesqualgebra articles record the case in which they differ: the annihilator's coincidence
  with the metric complement is a property of the band, not a general theorem.
- The annihilator is the zero-divisor condition with its witnesses displayed. It is the entry to the
  section's later articles: the square roots of zero are the elements that annihilate themselves, and the
  idempotents are the projectors whose kernel is a full half of the space.
- The kernel is also the zero-mode space of *The Index Theorem and the Zero-Mode Count in Biquaternionic
  Form*, the GNS null space of *The GNS Construction in the Biquaternion Framework*, and the algebraic
  obstruction behind *No-Cloning and the Algebraic Obstruction in Biquaternionic Form*: one object, and
  four physical names for it.
- The size of the kernel can be a **topological invariant**. In *The Index Theorem and the Zero-Mode Count
  in Biquaternionic Form* the index — the difference between the numbers of positive- and negative-chirality
  zero modes of the Dirac operator — equals the topological charge, so "the charge that classifies the field
  and the number of fermion zero modes that the field supports are one and the same number." The article is
  also explicit about the framework's ceiling: the abelian index density is the invariant $I_2=\vec E\cdot\vec B$,
  while the non-abelian density $\mathrm{Tr}(F\wedge F)$ needs a second slot that the rank-two biquaternion
  norm does not have.
- The kernel is also the closed-state space $\ker s$ of BRST — the physical cohomology is its quotient
  $\ker s/\mathrm{im}\,s$ — the kernel of the divergence that defines a conserved current, and the
  polarisation kernel $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\overline{\tilde A}$ of the antisymmetric
  sesquilinear operator.
- A kernel has two opposite readings. A gauge kernel hides a description that a gauge choice can recover;
  a confinement kernel has destroyed a description that the observable algebra does not contain.
- The kernel can shrink under quantisation and change under a change of observer. An anomaly is a current
  that is no longer in the kernel of the divergence at one loop, and its cancellation is a condition that
  keeps the kernel large enough; a Bogoliubov transformation with $v\neq0$ changes the annihilator itself,
  so the vacuum of one mode expansion is not annihilated by the operators of another (Unruh, Hawking).
- A current can lie in the kernel for a structural reason rather than a dynamical one. The topological baryon
  current of *The Skyrme Model and the Topological Baryon in Biquaternionic Form* is conserved identically,
  $\partial_\mu B^\mu=0$ with no equation of motion, by antisymmetry and Maurer–Cartan flatness: the kernel
  of a Noether-type divergence is made off-shell, and the charge is the degree of a map rather than the
  integral of a dynamics.
- The kernel can be constructive rather than destructive. The self-dual instantons of *Instantons and
  Solitons in Biquaternionic Form* are generated from the kernel of a Fueter-type operator, their collective
  coordinates are the moduli (the directions of zero action cost), and the framework supplies the
  abelian topological density while the non-abelian one lies outside the biquaternion-norm invariants.
- The kernel of the field-strength map is the **gauge orbit**. In *The Covariant Derivative and Gauge
  Connection in Biquaternionic Form* the connection has no gauge-invariant local value — it can be gauged to
  zero at any one point — and only its curvature obstructs doing so on a neighbourhood: two connections in
  one gauge orbit produce the same field strength, so the pure-gauge directions lie in the kernel of the map
  from connections to curvatures. This is the algebraic form of gauge redundancy, and it is the first of the
  annihilator's two information readings: what the kernel holds here is a description, recoverable by a gauge
  choice, not a quantity destroyed.

## Summary

The annihilator of an element in one of the twelve products is the kernel of the corresponding
multiplication, and the mathematics companion computes it for all twelve, with the case split and the
generators. Read physically, it is the set of inputs a process sends to zero, and it carries three
statements. First, a process is invertible exactly when its kernel is trivial; off the cone the four
general products have trivial kernel, and on the cone the kernel is a plane of other lightlike
directions, so lightlike elements are killed along lightlike directions. Second, the two one-sided kernels
coincide in ten structures and differ in the plain composition and the gauge coupling, which is the
chirality of an operation against its adjoint, and at a cone element the two kernels are distinct planes
sharing the line of the conjugate. Third, the shape of the kernel names the kind of structure: a
scalar-valued coupling has a hyperplane, the set of partners of zero overlap, and a bracket has the
centraliser, the whole algebra at a central element, because the central element is a global phase that
commutes with everything. The four planes of a cone element in the four general products are one plain
plane and its two conjugate images, so the composition band fixes the kernels of the other three. The
annihilator is thus the zero-divisor condition with its witnesses displayed, and it is the natural entry to
the roots of zero, the idempotents and the nilpotents of the rest of the section.

## Summary of Notation

- $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$.
- $A_\star(\tilde P)=\{\tilde X:\tilde P\star\tilde X=0\}$ the left annihilator, $B_\star(\tilde P)=\{\tilde X:\tilde X\star\tilde P=0\}$ the right one, the kernels of $L_{\tilde P}$ and $R_{\tilde P}$.
- $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ the biquaternion norm; the cone is $\{N=0\}$; $N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$ and $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ the two forms of the scalar-valued structures.
- ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; $\mathrm{Tr}=2\,\mathrm{Sc}$; $\mathbb{C}\{u,v\}$ a complex plane, $\mathbb{C}u$ a complex line.
- The twelve structures: GPA, GPS, GQA, GQS general; SPA, SPS, SQA, SQS symmetric; APA, APS, AQA, AQS antisymmetric.
- $\mathbb{M}_\pm$ the sectors; $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace; $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the centre.

## Further Reading

- The mathematics companion: *Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve computations, the two-sided theorem and the four general planes.
- The zero-divisor context: *Zero Divisors in the Algebraic Structures of Biquaternions over $\mathbb{C}$*; *The Light Cone as the Biquaternion Zero-Divisor Cone*.
- The operators and the kernels: *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*; *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; *Observables, Gauge Generators and the Chirality of the Internal Action*; *The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions*.
- The scalar-valued and bracket rows: *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*; *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations*; *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*; *The States the Indefinite Metric Cannot Normalise*.
- The kernel in the quantum corpus: *The Index Theorem and the Zero-Mode Count in Biquaternionic Form*; *The GNS Construction in the Biquaternion Framework*; *No-Cloning and the Algebraic Obstruction in Biquaternionic Form*; *The Born Rule as a Trace Formula — Derivation and Comparison*; *The Centre of the Biquaternion Algebra as the Classical Sector*; *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form*.
- The kernel as a structural identity: *Gauge Curvature and the Bianchi Identity in Biquaternionic Form*, for the Bianchi identity as the operator Jacobi identity and the annihilating role of associativity; *The Skyrme Model and the Topological Baryon in Biquaternionic Form*, for the topological current conserved identically by antisymmetry and Maurer–Cartan flatness, the off-shell kernel whose charge is a degree.
- The kernel that generates and labels: *Instantons and Solitons in Biquaternionic Form*, for the self-dual solutions generated from the kernel of a Fueter-type operator, the moduli as the flat directions of the action, and the abelian-versus-non-abelian topological-density gap.
- The complement and the band: *The Complementary Space of the Spinor Space and Its Physical Meaning*, for the coincidence of the module complement and the Hilbert complement in the native pairing and its failure in the general plain bands.
- The kernel in cohomology, constraints and channels: *BRST Symmetry in Biquaternionic Form*; *The Schwinger–Dyson Equations and the Ward–Takahashi Identities in Biquaternionic Form*; *Noether's Theorem in Biquaternionic Form*; *Anomalies and Anomaly Cancellation in Biquaternionic Form*; *The Operators of the Antisymmetric Quaternionic Sesquilinear Product and the Polarisation*; *The Holevo Bound and Accessible Information in Biquaternionic Form*; *Confinement and the Loss of Partonic Information in Biquaternionic Form*.
- The kernel as the gauge orbit: *The Covariant Derivative and Gauge Connection in Biquaternionic Form*, for the connection with no gauge-invariant local value and the curvature as the only obstruction, so that the pure-gauge directions lie in the kernel of the field-strength map.
- The kernel as a topological count: *The Index Theorem and the Zero-Mode Count in Biquaternionic Form*, for the index as the difference of the chiral zero-mode counts, equal to the topological charge, and the rank-two ceiling on the non-abelian index density.
- The observer-dependent kernel: *Bogoliubov Transformations in Biquaternionic Form*; *The Unruh Effect in Biquaternionic Form*; *Hawking Radiation in Biquaternionic Form*.
- The operator and the geometry: *The Spectral Triple of the Biquaternion Algebra*, for the zero-mode kernel, the distance and the gauge fields as inner fluctuations of the Dirac operator; *The Index Theorem and the Zero-Mode Count in Biquaternionic Form*.
- The general products and the cone: *Composition and Probability: the General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared*; *The Cone and the Massless Particles in the Algebraic Structures of Biquaternions over $\mathbb{C}$*; *Mass, Rank and the Positivity of the Dagger*.
- The grid: *The 12 Products of the Biquaternion Complex Space*; *The Twelve Structures Compared: Product, Law and Form*; *The Four General Products and Their Physical Readings*.
- The conventions of the series: *Conventions in the Biquaternion Universe*.
