# __Annihilators in the 12 Structures Framework__

## Introduction

The annihilator of an element in a product is the set of partners that the element kills. It is the kernel
of the operation "multiply by it", so it is the kernel of a process, and the physical reading of the
kernel is direct: a process is invertible exactly when its kernel is trivial, and the size of the kernel is
the amount of information the process destroys. The twelve products of the biquaternion complex space
define twelve annihilators for one element, and this article reads them physically. It is the second
physics companion of the mathematics comparison group, after *Zero Divisors in the 12 Structures
Framework*, and the mathematics companion is *Annihilators* (`articles_maths/annihilators.md`).

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
section own the objects that the table touches: *Zero Divisors in the 12 Structures Framework* the
degeneracy itself, *Square Roots of Minus One, Zero and Plus One in the 12 Structures Framework* and
*Square Roots of a General Element in the 12 Structures Framework* the radicands, *Idempotents in the 12
Structures Framework* the projectors, and *Nilpotents in the 12 Structures Framework* the square-zero
elements.

**Conventions.** We use those of the companion articles unchanged. The algebra is
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$ and
$e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; $i$ is the central scalar imaginary. The conjugations are
${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The biquaternion norm is
$N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$, whose vanishing locus is the cone; the trace
is $\mathrm{Tr}=2\,\mathrm{Sc}$; the material coordinate is $\tilde Q=ict\,e_0+\mathbf x$. The twelve
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
multiplications directly, in *The Operators of the Ordinary Product: One-Sided, Two-Sided and the
Sandwich* and *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*.

**The annihilator lies in the zero-divisor set.** When $\tilde P\neq0$ kills $\tilde X\neq0$, the element
$\tilde X$ is itself a zero divisor of the same product with witness $\tilde P$. Every nonzero element of
an annihilator is therefore a zero divisor, and for the four general products, whose zero-divisor set is
the cone, the whole annihilator lies on the cone. The physics is the sharp statement that the killers of a
lightlike element are lightlike: a null direction annihilates only along null directions. In the derived
structures the zero-divisor set is larger and the annihilator can leave the cone, the unit $e_1$ being
annihilated in the symmetrised products while off the cone, as *Zero Divisors in the 12 Structures
Framework* records.

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
$\mathbb{C}\{e_0-ie_1,e_3+ie_2\}$, the natural plane $\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$, the plain
sesquilinear plane $\mathbb{C}\{e_1+ie_0,e_2+ie_3\}$ and the general quaternionic sesquilinear plane
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
the Massless Particles in the 12 Structures Framework*.

At the pure cone element $e_1+ie_2$ the plain planes are

$$
A_{\text{plain}}(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_0+ie_3\},\qquad
B_{\text{plain}}(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_0-ie_3\},
$$

so a lightlike element lies in its own annihilator, as it must: $\tilde P^{2}=0$ for a pure cone element,
and the square is the product of the element with itself. The self-annihilation of a lightlike
displacement is the elementary physical case, and *Nilpotents in the 12 Structures Framework* reads it as
the square-zero class.

## The Hyperplane of a Scalar-Valued Coupling

Two structures collapse their product to a form: the symmetric quaternionic algebra
$\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ with $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$,
and the symmetric plain sesqualgebra $\tilde P\star\tilde Q=H(\tilde P,\tilde Q)e_0$ with
$H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$. For each, the annihilator of
any nonzero element is the hyperplane cut by the form,

$$
P_0X_0+(\mathbf P,\mathbf X)=0\quad\text{(SQA)},\qquad
P_0\overline{X_0}+(\mathbf P,\overline{\mathbf X})=0\quad\text{(SPS)} .
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
$\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q$, whose annihilator is
$\mathbb{C}e_0\oplus\mathbb{C}\mathbf P$: the partners the bracket sends to zero are the centre and the
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

The general quaternionic antisymmetrisation separates the two cases of the cone by the size of the
annihilator: at an element of nonzero norm the annihilator is the line of the element itself, and at a
cone element it is a plane containing that line. The reading is the same as for the plain bracket, with
the norm deciding whether the centraliser grows from a line to a plane. The conjugate-alternating rows
$\mathrm{APS}$ and $\mathrm{AQS}$ act on the conjugate direction, and the rows whose bracket is
conjugate-alternating annihilate their own conjugate rather than themselves in the generic case.

## The Twelve Annihilators and Their Physical Readings

| structure | product | annihilator of a general $\tilde P$ | physical reading |
|---|---|---|---|
| GPA | $\tilde P\tilde Q$ | $\{0\}$ off the cone; two distinct planes through $\mathbb{C}\tilde P^{\natural}$ on the cone | an invertible composition has trivial kernel; a lightlike one is chiral, killing different directions on the two sides |
| SPA | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $\{0\}$ off the cone with $P_0\neq0$; the line $\mathbb{C}\tilde P^{\natural}$ on the cone; the plane $\{X_0=0,(\mathbf P,\mathbf X)=0\}$ for $P_0=0$ | the symmetric composition has one kernel; a pure operation kills the plane orthogonal to it |
| APA | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | the plane $\mathbb{C}e_0\oplus\mathbb{C}\mathbf P$ for $\mathbf P\neq0$; the whole space for a central element | the bracket's centraliser is the centre and the element's own direction; a global phase is annihilated by everything |
| GQA | $\tilde P^{\natural}\tilde Q$ | $\{0\}$ off the cone; one plane containing $\mathbb{C}\tilde P$ on the cone | the natural product has one kernel, and a lightlike element lies in it |
| SQA | $N(\tilde P,\tilde Q)e_0$ | the hyperplane $N(\tilde P,\tilde X)=0$ | a scalar coupling kills the orthogonal hyperplane; a number cannot act |
| AQA | the antisymmetrisation | a line or a plane through $\mathbb{C}\tilde P$; the centre for a central element | the quaternionic bracket's centraliser, with the norm deciding line against plane |
| GPS | $\tilde P\tilde Q^{*}$ | $\{0\}$ off the cone; the star-image of the plain plane on the cone | the pairing's kernel is the conjugate image of the composition kernel |
| SPS | $H(\tilde P,\tilde Q)e_0$ | the hyperplane $H(\tilde P,\tilde X)=0$ | the Born pairing kills the amplitudes orthogonal to $\tilde P$: zero overlap |
| APS | the antisymmetrisation | $\{0\}$ off the cone; the line $\mathbb{C}\overline{\tilde P}$ at nonzero norm; the star-image of the plain plane on the cone | the conjugate bracket reads the conjugate direction |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | $\{0\}$ off the cone; two distinct planes through $\mathbb{C}\tilde P^{*}$ on the cone | the gauge coupling is chiral, like the plain composition |
| SQS | the symmetrisation | $\{0\}$ off the cone with $P_0\neq0$; the line $\mathbb{C}\tilde P^{*}$ on the cone; the plane $\{X_0=0,K(\tilde P,\tilde X)=0\}$ for $P_0=0$ | the symmetric gauge coupling has one kernel, a plane at a pure element against a line at a non-pure one |
| AQS | the antisymmetrisation | the plane $\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf P}$ for $\mathbf P\neq0$; the whole space for a central element | the conjugate bracket's centraliser; a global phase is annihilated by everything |

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
- **In the six remaining rows the annihilator is the origin off the cone and a line or a plane on it.**
  The physical content is the cone itself: off the cone the operation is injective, on the cone it is not,
  and the dimension of the kernel is the rank drop read by *Mass, Rank and the Positivity of the Dagger*.

## What the Annihilator Decides

| claim | source | status |
|---|---|---|
| the annihilator is the kernel of the left or right multiplication | mathematics companion; operator articles | cited |
| an element off the cone has trivial annihilator in the four general products | mathematics companion; recomputed (no non-null sample has an annihilator) | verified |
| the killers of a cone element in the four general products lie on the cone | *Zero Divisors in the 12 Structures Framework*; mathematics companion | cited |
| the two sides differ exactly for GPA and GQS, and only on the cone | mathematics companion, theorem; recomputed planes at $e_0+ie_1$ | verified |
| the plain planes at $e_0+ie_1$ share $\mathbb{C}(e_0-ie_1)$ and differ in the second generator | mathematics companion, example; recomputed | verified |
| the four general planes are one plane read through the two conjugations | mathematics companion, theorem; recomputed at $e_0+ie_1$ | verified |
| SQA and SPS annihilators are hyperplanes; the APA and AQS annihilator is the whole space at a central element | mathematics companion; recomputed for SQA at $e_0$ and APA at $e_1$, AQS at $e_0$ | verified |
| the SQS annihilator is a plane at a pure element and a line at a non-pure cone element | mathematics companion; recomputed at $e_1+ie_2$ and $e_0+ie_1$ | verified |
| the physical readings (chirality, zero overlap, centraliser, lightlike kernel, zero-mode count, GNS null space, no-cloning) | this article; owners cited in the text | interpretation |

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
article.

**Polarisation: the kernel of the skew operator.** *The Operators of the Antisymmetric Quaternionic
Sesquilinear Product and the Polarisation* computes the left multiplication of the row that this article
reads through the table, and finds

$$
\ker L^{\diamond}_{\tilde A}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\overline{\mathbf A},\qquad
\operatorname{im}L^{\diamond}_{\tilde A}=\{(\mathbf A,\cdot)=0\}.
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

## Physical Interpretation

- The annihilator of an element is the kernel of the operation "multiply by it". A process is invertible
  exactly when its kernel is trivial, and the dimension of the kernel is the amount of information it
  destroys.
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
- The annihilator is the zero-divisor condition with its witnesses displayed. It is the entry to the
  section's later articles: the square roots of zero are the elements that annihilate themselves, and the
  idempotents are the projectors whose kernel is a full half of the space.
- The kernel is also the zero-mode space of *The Index Theorem and the Zero-Mode Count in Biquaternionic
  Form*, the GNS null space of *The GNS Construction in the Biquaternion Framework*, and the algebraic
  obstruction behind *No-Cloning and the Algebraic Obstruction in Biquaternionic Form*: one object, and
  four physical names for it.
- The same kernel is the BRST cohomology $\ker s/\mathrm{im}\,s$ of the physical state space, the kernel of
  the divergence that defines a conserved current, and the polarisation kernel
  $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\overline{\tilde A}$ of the antisymmetric sesquilinear operator.
- A kernel has two opposite readings. A gauge kernel hides a description that a gauge choice can recover;
  a confinement kernel has destroyed a description that the observable algebra does not contain.

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
- $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ the biquaternion norm; the cone is $\{N=0\}$; $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ and $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$ the two forms of the scalar-valued structures.
- ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; $\mathrm{Tr}=2\,\mathrm{Sc}$; $\mathbb{C}\{u,v\}$ a complex plane, $\mathbb{C}u$ a complex line.
- The twelve structures: GPA, GQA, GPS, GQS general; SPA, SQA, SPS, SQS symmetric; APA, AQA, APS, AQS antisymmetric.
- $\mathbb{M}_\pm$ the sectors; $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace; $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the centre.

## Further Reading

- The mathematics companion: *Annihilators* (`articles_maths/annihilators.md`), for the twelve computations, the two-sided theorem and the four general planes.
- The zero-divisor context: *Zero Divisors in the 12 Structures Framework*; *The Light Cone as the Biquaternion Zero-Divisor Cone*.
- The operators and the kernels: *The Operators of the Ordinary Product: One-Sided, Two-Sided and the Sandwich*; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*; *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; *Observables, Gauge Generators and the Chirality of the Internal Action*; *The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions*.
- The scalar-valued and bracket rows: *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*; *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations*; *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*; *The States the Indefinite Metric Cannot Normalise*.
- The kernel in the quantum corpus: *The Index Theorem and the Zero-Mode Count in Biquaternionic Form*; *The GNS Construction in the Biquaternion Framework*; *No-Cloning and the Algebraic Obstruction in Biquaternionic Form*; *The Born Rule as a Trace Formula — Derivation and Comparison*; *The Centre of the Biquaternion Algebra as the Classical Sector*; *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form*.
- The kernel in cohomology, constraints and channels: *BRST Symmetry in Biquaternionic Form*; *The Schwinger–Dyson Equations and the Ward–Takahashi Identities in Biquaternionic Form*; *Noether's Theorem in Biquaternionic Form*; *The Operators of the Antisymmetric Quaternionic Sesquilinear Product and the Polarisation*; *The Holevo Bound and Accessible Information in Biquaternionic Form*; *Confinement and the Loss of Partonic Information in Biquaternionic Form*.
- The general products and the cone: *Composition and Probability: the General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared*; *The Cone and the Massless Particles in the 12 Structures Framework*; *Mass, Rank and the Positivity of the Dagger*.
- The grid: *The 12 Products of the Biquaternion Complex Space*; *The Twelve Structures Compared: Product, Law and Form*; *The Four General Products and Their Physical Readings*.
- The conventions of the series: *Conventions in the Biquaternion Universe*.
