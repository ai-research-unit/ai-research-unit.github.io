# __The Four General Products and Their Physical Readings__

## Introduction

The biquaternion space carries four general products and not one, and the physics menu gives each of the four a
subcategory of its own. This article is the map between them. It states the single mechanism that
generates the four, the two structural rules behind their properties, and the physical job that each of
the four is asked to do.

The mechanism is that the four general products are the four ways of inserting the involutions of the algebra
into the two slots of a multiplication. Written for a general product $\tilde P\star\tilde Q$, the first
factor is read either as it stands or through the natural conjugation ${}^{\natural}$, and the second
factor is read either as it stands or through the involution ${}^{*}$; nothing else varies. The four general
products are therefore indexed by a $2\times2$ grid, and the grid is the whole subject. The four rules
are written out on the coordinates in §*The Four General Products in Coordinates*, before the grid is used.

The structural result is that the two slots decide different things, and that each slot decides one of
the two properties a physical theory cares about most.

- The **second slot** decides whether the operation is a **composition** or a **pairing**. Read
  without a conjugation it is $\mathbb{C}$-bilinear and can be iterated; read with the star it is
  sesquilinear and can only be evaluated. It is the slot that separates the two **general algebras** from the
  two **general sesqualgebras**, and that is exactly the two-and-two division of the corpus's four general
  products.
- The **first slot** decides whether $e_0$ is a **right** identity, whether the induced form is
  **definite on each sector** or indefinite there, and it **toggles** the coefficient $\varepsilon$ of
  the scalar form. Since the second slot toggles $\varepsilon$ too, the coefficient survives exactly in
  the two settings whose slots agree. It is the slot that turns a definite form into an indefinite one,
  and so the slot that decides which of the four carries a metric.

**The framework's reading, and it is a reading and not a theorem, is that the four general products are the four
jobs a relativistic quantum theory needs.** The plain product is **composition**, the product of
operations and of the identity operation. The quaternionic product is **causality**, because its square
is the interval. The sesquilinear product is **probability**, because its form is positive definite and
is the Born pairing. The general quaternionic sesquilinear product is **gauge**, because its form is indefinite
and its ternary product is not a state space. Each of the four readings is labelled in §*The Four
Readings* and in §*The Ledger*, and none of them is proved here: what is proved is the grid, and the
reading is what the framework does with it.

**Precision: the two algebras and the two sesqualgebras of the title are the general ones.** The
biquaternion space carries **twelve** products, and with them twelve algebraic structures: each of the four
general products splits into a symmetric and an antisymmetric part, giving six $\mathbb{C}$-bilinear and six
sesquilinear operations, that is **six algebras over $\mathbb{C}$ and six sesqualgebras over
$(\mathbb{C},\bar{\cdot})$** (*The 12 Products of the Biquaternion Complex Space*, *The 12 Algebraic
Structures over the Biquaternion $\mathbb{C}$ Space*). This article, and the four blocks it maps, read the
**general** structures alone: the two **general** algebras and the two **general** sesqualgebras among the
six of each kind. The other eight structures are the symmetric and antisymmetric parts of the four general
products, and they enter here only through the reading of §*The Four Readings* that the twelve are the four
general products together with the two halves of each.

The mathematics of the four general products, of their scalar and vector parts, of their comparison and of their
scalar forms is *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *Relations Between the Four General Products*, *Comparison Between the Four General Products* and *The Four Pairings of the
Biquaternion Algebra*, and the slot construction itself, with the two theorems that the second slot
decides the composition and the first the form, is *The Four General Products and Their Two Slots: the Two
Algebras and the Two Sesqualgebras*. The signature table of the four scalar forms on the six subspaces,
which is where the effect of the first slot on the form is quantified, compares the four blocks with one
another and so belongs to this article rather than to any of them; it is in §*The Six Subspaces*. The
field of $B$ alone is *The Ordinary Product and the Material Sector*, the entry article of the block of
the algebra over $\mathbb{C}$, where the restriction of $B$ to the six subspaces is read.

**This article is also the place where the four are compared with one another.** Each block reads one
product and one form, compares its own product with its sibling, and does not re-tabulate the grid; the
comparisons that cross the grid are collected here, in §*The Four Forms Compared* and in §*The Four
Readings*. The four scalar forms turn out to be one bilinear form read through the two involutions, and
the two sectors collapse the four to two.

This article is the prose companion of *The Mathematical Study of Biquaternions*, which carries the
entries of the mathematics menu, and it is the map of the four physics blocks that follow.

**Conventions.** Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis
$e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, $e_k^{2}=-e_0$, central imaginary $i$, and
$\tilde Q=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The conjugations are
$\bar{\cdot}$, ${\natural}$, ${}^{*}=\bar{\cdot}\circ{\natural}$ and $\flat=-{}^{*}$; the scalar part is
$\mathrm{Sc}(\tilde Q)=Q_0$. The **informational sector** $\mathbb{M}_+$ is the Hermitian subspace, the
fixed space of ${}^{*}$ (real $Q_0$, imaginary $Q_k$), and the **material sector** $\mathbb{M}_-$ is the
anti-Hermitian subspace, the fixed space of $\flat$ (imaginary $Q_0$, real $Q_k$); each is a real
subspace of dimension four. A form is called **definite on a sector** when it is definite as a real form
on $\mathbb{M}_-$ and on $\mathbb{M}_+$; this is weaker than definiteness on the whole real space, and
the two readings are distinguished wherever they differ below.

## The Four General Products in Coordinates

The four general products are written out here on the coordinates, before the slot language of §*The Two Slots*
is used, because the four rules are met first as formulas and this article is the map of the four
physics blocks that follow. For two elements $\tilde P,\tilde Q$ of $\mathbb{B}$, with
$\tilde Q=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ and $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$, a conjugation either
leaves a coordinate as it stands or reverses its sign, conjugating the coefficient in the second case:

$$
\tilde Q^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3,\qquad \tilde Q^{*}=\overline{Q_0}e_0-\overline{Q_1}e_1-\overline{Q_2}e_2-\overline{Q_3}e_3 .
$$

With $\varepsilon=(1,-1,-1,-1)$ and the sums over $\mu,\nu=0,\dots,3$, the four general products multiply the
coordinates of the two factors on the basis of the units, the first factor read plain or through
${}^{\natural}$ and the second plain or through ${}^{*}$, the two choices independent:

$$
\tilde P\tilde Q=\sum_{\mu,\nu}P_\mu Q_\nu\,e_\mu e_\nu,\qquad \tilde P^{\natural}\tilde Q=\sum_{\mu,\nu}\varepsilon_\mu P_\mu Q_\nu\,e_\mu e_\nu,
$$
$$
\tilde P\tilde Q^{*}=\sum_{\mu,\nu}\varepsilon_\nu P_\mu\overline{Q_\nu}\,e_\mu e_\nu,\qquad \tilde P^{\natural}\tilde Q^{*}=\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu P_\mu\overline{Q_\nu}\,e_\mu e_\nu .
$$

Their scalar parts are the four forms the article reads throughout, and written out term by term they
are

$$
\begin{aligned}
B(\tilde P,\tilde Q)&=\mathrm{Sc}(\tilde P\tilde Q)=\textstyle\sum_\mu\varepsilon_\mu P_\mu Q_\mu=P_0Q_0-P_1Q_1-P_2Q_2-P_3Q_3,\\
N(\tilde P,\tilde Q)&=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\textstyle\sum_\mu P_\mu Q_\mu=P_0Q_0+P_1Q_1+P_2Q_2+P_3Q_3,\\
H(\tilde P,\tilde Q)&=\mathrm{Sc}(\tilde P\tilde Q^{*})=\textstyle\sum_\mu P_\mu\overline{Q_\mu}=P_0\overline{Q_0}+P_1\overline{Q_1}+P_2\overline{Q_2}+P_3\overline{Q_3},\\
K(\tilde P,\tilde Q)&=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\textstyle\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}=P_0\overline{Q_0}-P_1\overline{Q_1}-P_2\overline{Q_2}-P_3\overline{Q_3}.
\end{aligned}
$$

The four scalar forms carry the short names $B$, $N$, $H$ and $K$ of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*. The four general products are the four readings of §*The Four Readings* — composition, causality, probability
and gauge — and the four scalar forms above are what the two slots organise in §*What the Two Slots
Decide*; restricted to the two sectors they carry the signs recorded in §*The Two Marks in the Scalar
Form*.

## The Two Slots

Each of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* is obtained by reading each factor
through an involution, and the involutions used are only two of the four available ones:

$$
\tilde P\tilde Q,\qquad \tilde P^{\natural}\tilde Q,\qquad \tilde P\tilde Q^{*},\qquad
\tilde P^{\natural}\tilde Q^{*}.
$$

Every one of them is of the form

$$
\tilde P\star\tilde Q=K_1(\tilde P)\,K_2(\tilde Q),\qquad
K_1\in\{\mathrm{id},{}^{\natural}\},\quad K_2\in\{\mathrm{id},{}^{*}\},
$$

with the two slots read independently. The **first slot** takes only the identity or the natural
conjugation, and the **second slot** only the identity or the star. Neither ${}^{*}$ in the first slot
nor ${}^{\natural}$ in the second occurs among the four, and that restriction is what makes the family a
grid of four and not a table of sixteen. It also means the two slots are not interchangeable. The star
involves the complex conjugation, which is antilinear, while the natural conjugation is
$\mathbb{C}$-linear, and the list of four is consequently not symmetric in its two slots: there is no
product in it that reads its first factor through ${}^{*}$. The asymmetry is not accidental. It is the
source of every difference in the table of §*What the Two Slots Decide*.

The grid is:

| | $K_2=\mathrm{id}$ | $K_2={}^{*}$ |
|---|---|---|
| $K_1=\mathrm{id}$ | the plain product $\tilde P\tilde Q$ | the sesquilinear product $\tilde P\tilde Q^{*}$ |
| $K_1={}^{\natural}$ | the quaternionic product $\tilde P^{\natural}\tilde Q$ | the general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ |

**The two rows are not a second classification; they are the first slot.** The upper row has no
${}^{\natural}$ and the lower row has it, and by §*What the Two Slots Decide* that single difference is
what decides whether the scalar form of the product is definite on each sector or indefinite there. In
the same way the two columns are the second slot, and the right-hand column is what makes a product
sesquilinear rather than bilinear.

**Remark (the four used slot pairs are not a redundant set).** Sixteen slot pairs are available and four
are used, and it is tempting to read the unused twelve as transposes or conjugates of the four, hence as
redundant. They are not, and the point matters for the reason the grid is a grid of four. The transpose
does behave inside the two bilinear cells: the transpose of the plain product is a plain product, and the
transpose of the quaternionic product is its **natural conjugate**,
$\tilde Q^{\natural}\tilde P=(\tilde P^{\natural}\tilde Q)^{\natural}$, so it stays in the quaternionic
cell. But the transpose of a **sesquilinear** product is not a product of the family at all — it returns a
product of the opposite type — which is exactly why the exchange used for the sesquilinear families is the
**conjugate transpose** and not the bare interchange (§*The Method of the Decomposition* of *The 12
Products of the Biquaternion Complex Space*). And the twelve unused pairs are in the main **other
products**: a pair such as $(\bar{\cdot},\mathrm{id})$, reading the first factor through the
coefficientwise conjugation, gives the product $\bar{\tilde P}\tilde Q$, which is none of the four and not
a transpose or a conjugate of any of them. The restriction to the four is therefore a genuine restriction
of the algebra and not a redundancy of naming, and reading the unused twelve as a "mirror" of the four is
**not** supported. What the transpose does supply is the reason the four are closed in the bilinear row and
the reason the corpus conjugates in the sesquilinear one.

**The two and two by which the corpus names its four general objects is the column split.** When the second slot is
read without a conjugation the product is $\mathbb{C}$-bilinear and defines on $\mathbb{B}$ the
structure of an **algebra over $\mathbb{C}$**; when it carries the star the product is
$\mathbb{C}$-linear in the first factor and conjugate-linear in the second and defines the structure of
a **sesqualgebra over $\mathbb{C}$**. The two-and-two is the column split of the four **general** products
alone: since each of the four splits further into a symmetric and an antisymmetric part, the space carries
**six algebras and six sesqualgebras** in all (*The 12 Algebraic Structures over the Biquaternion
$\mathbb{C}$ Space*), of which the two columns of the grid are the two **general** members of each kind. This
is the split made in *Comparison Between the Four General Products*, and it is the reason the corpus has the four objects *Introduction to the General Plain Algebra of
Biquaternions*, *Introduction to the General Quaternionic Algebra of Biquaternions*, *Introduction to the
General Plain Sesqualgebra of Biquaternions* and *Introduction to the General Quaternionic Sesqualgebra of
Biquaternions* and not one object with four general products.

### The Two Marks in the Scalar Form

The effect of the two slots is visible at once in the four scalar forms, which differ from one another
in exactly two marks. With $\varepsilon=(1,-1,-1,-1)$ and $\mathrm{Sc}$ the scalar part,

| product | scalar form | written out |
|---|---|---|
| $\tilde P\tilde Q$ | $B(\tilde P,\tilde Q)$ | $\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ |
| $\tilde P^{\natural}\tilde Q$ | $N(\tilde P,\tilde Q)$ | $\sum_\mu P_\mu Q_\mu$ |
| $\tilde P\tilde Q^{*}$ | $H(\tilde P,\tilde Q)$ | $\sum_\mu P_\mu\overline{Q_\mu}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $K(\tilde P,\tilde Q)$ | $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ |

Read by column and row, the two marks separate cleanly:

- **The coefficient $\varepsilon_\mu$ survives if and only if the two slots agree.** It is present in
  $B$ and in $K$ — the settings $(\mathrm{id},\mathrm{id})$ and $({}^{\natural},{}^{*})$ — and absent in
  $N$ and in $H$, the settings $({}^{\natural},\mathrm{id})$ and $(\mathrm{id},{}^{*})$. Conjugating the
  first factor therefore *toggles* $\varepsilon$: it removes the coefficient from the bilinear product
  and supplies it to the sesquilinear one.
- **The bar is present if and only if the second slot carries ${}^{*}$.** It is absent in $B$ and in
  $N$ and present in $H$ and in $K$.

So the **conjugation** is inserted by the second slot alone, while the **coefficient** $\varepsilon$ is
carried by the two slots together. That is the mechanism in one line: a product is made Hermitian by
conjugating its second factor, and its scalar form carries the coefficient $\varepsilon$ exactly when
its two slots agree.

Reading the first factor through ${}^{\natural}$ is what turns a definite form into an indefinite one.
On the material sector $\mathbb{M}_-$ the four scalar forms read, in the signs of a diagonal basis,
$B=(-,-,-,-)$, $N=(-,+,+,+)$, $H=(+,+,+,+)$ and $K=(+,-,-,-)$; on the informational sector
$\mathbb{M}_+$ they read $B=(+,+,+,+)$, $N=(+,-,-,-)$, $H=(+,+,+,+)$ and $K=(+,-,-,-)$. So $B$ and $H$
are definite on each sector — $H$ positively on both, $B$ negatively on $\mathbb{M}_-$ and positively on
$\mathbb{M}_+$ — while $N$ and $K$ are indefinite on each sector; and only $N$ carries the signature of
spacetime, on $\mathbb{M}_-$ and with the opposite signs on $\mathbb{M}_+$. Read instead on the whole
real space, where the four are the forms of *The Four Pairings of the Biquaternion Algebra*, only $H$ is
definite, and $B$, $N$ and $K$ are indefinite, of signatures $(4,4)$, $(4,4)$ and $(2,6)$. The full
table on the six subspaces, with the Gram matrices and the isotropic structures, is in §*The Six
Subspaces*; the two sectors read above are its material and informational columns, and nothing else is
claimed here.

**The sector signs are checkable on one element.** Writing $\tilde Q=(ict,x,y,z)$ on $\mathbb{M}_-$ and
$\tilde Q=(ct,ix,iy,iz)$ on $\mathbb{M}_+$, with $t,x,y,z$ real, the four forms read on $\mathbb{M}_-$
$B=-c^2t^2-(x^2+y^2+z^2)$, $N=-c^2t^2+x^2+y^2+z^2$, $H=c^2t^2+x^2+y^2+z^2$, $K=c^2t^2-(x^2+y^2+z^2)$,
and on $\mathbb{M}_+$ the same four with $B$ and $N$ negated and $H$ and $K$ unchanged. That is the
table above, and it shows on $\mathbb{M}_-$ that $N$ is the Minkowski form.

## What the Two Slots Decide

The properties of the four general products do not have to be checked one by one. Each is decided by one slot,
by both, or by singling out one of the four general products. The following table is the complete list for the
properties the corpus tabulates, and the rule in the last column is the reason.

| property | decided by | the rule |
|---|---|---|
| $\mathbb{C}$-bilinear, or sesquilinear | second slot | bilinear if and only if $K_2=\mathrm{id}$ |
| $e_0$ is a **left** identity | second slot | yes if and only if $K_2=\mathrm{id}$ |
| the left multiplications form a monoid | second slot | yes if and only if $K_2=\mathrm{id}$ |
| $e_0$ is a **right** identity | first slot | yes if and only if $K_1=\mathrm{id}$ |
| the coefficient $\varepsilon$ survives in the scalar form | both slots | yes if and only if the two slots agree |
| the induced form is positive definite | exactly one product | only for $\tilde P\tilde Q^{*}$ |
| the induced form is definite on each sector | first slot | definite on $\mathbb{M}_-$ and on $\mathbb{M}_+$ if and only if $K_1=\mathrm{id}$ |
| $e_0$ is a **two-sided** identity | both slots | yes if and only if $K_1=K_2=\mathrm{id}$ |
| associative | both slots | yes if and only if $K_1=\mathrm{id}$ and $K_2=\mathrm{id}$ |
| the square $\tilde Q\star\tilde Q$ is scalar | exactly one product | only for $\tilde P^{\natural}\tilde Q$ |

The table gathers the rows of the property table of *Comparison Between the Four General Products*
— bilinearity, the two identities, the monoid of the left multiplications and associativity — read by
slot rather than by column, together with the two form rows of *The Four Pairings of the Biquaternion
Algebra* and the restriction table of §*The Six Subspaces*, and the row of the scalar square, which is
the property selected in *Introduction to the General Quaternionic Algebra of Biquaternions*. The table is the
article's central claim in tabular form, and it says that the two slots carry two independent
structures:

- **The second slot governs everything about the composition.** Whether the operation can be iterated
  at all, whether it has a left identity, and whether the left multiplications compose are one property
  of one slot. Whatever the first slot is set to, a product in the right-hand column stays a pairing and
  never becomes a composition.
- **The first slot governs the form as well.** Whether the operation induces a form definite on each
  sector, and whether it has a right identity, are read from the other slot; and it is the slot that
  toggles the coefficient $\varepsilon$, so that $\varepsilon$ survives exactly when the two slots
  agree.

**The one-sidedness of the identity is the sharpest consequence, and it is worth stating separately.**
$e_0$ is a left identity for exactly the two products whose second slot is trivial, and a right identity
for exactly the two whose first slot is trivial. So the plain product alone has a two-sided identity,
and it alone is associative; the quaternionic product has a left identity and no right one; the
sesquilinear product has a right identity and no left one; and the general quaternionic sesquilinear product has
neither. In the notation of the slots,

$$
e_0\star\tilde Q=\tilde Q \iff K_2=\mathrm{id},\qquad
\tilde Q\star e_0=\tilde Q \iff K_1=\mathrm{id}.
$$

The reason is immediate once the slots are named. $e_0^{\natural}=e_0^{*}=e_0$, so reading $e_0$ through
either involution returns $e_0$; what fails in the other slot is the involution applied to the *other*
factor. In the quaternionic product $e_0^{\natural}\tilde Q=\tilde Q$ but
$\tilde Q^{\natural}e_0=\tilde Q^{\natural}\neq\tilde Q$; in the sesquilinear product
$e_0\tilde Q^{*}=\tilde Q^{*}\neq\tilde Q$ but $\tilde Q e_0^{*}=\tilde Q$. The two failures are the two
conjugations of the algebra, ${}^{\natural}$ and ${}^{*}$, and each of the two is already an object of a
companion block.

### The Square of an Element

The last row of the table is the row the physics rests on, and it is the one that singles out a setting
rather than a slot.

$$
\tilde Q^{\natural}\tilde Q=N(\tilde Q)\,e_0,\qquad N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2}.
$$

The square of an element is scalar for the quaternionic product and for that product alone. It is not
scalar for the plain product, where $\tilde Q\tilde Q$ retains the vector part
$2Q_0\mathbf Q$; not for the sesquilinear product, where $\tilde Q\tilde Q^{*}$
is the rank-one pairing and not a scalar; and not for the general quaternionic sesquilinear product either.
**Only one of the four general products turns an element into a number, and it is the one whose first slot is
${}^{\natural}$ and whose second slot is trivial.**

That is the precise sense in which the quaternionic product is the product of the *interval*: it is the
unique product of the four under which the square of an element is a scalar, and the scalar it returns
is the biquaternion norm. The interval, the mass shell, the four-velocity and the inverse are owned by
*Biquaternion Norm and Invertibility* and are not restated here; what this article records is that the
interval is read off a product rather than attached to the space, and that the product is selected by
its slots.

## The Two General Algebras

The two products whose second slot is trivial are $\mathbb{C}$-bilinear, and they are the multiplication
of an **algebra over $\mathbb{C}$** in the sense the corpus uses — the two **general** algebras among the
six the space carries, the general plain and the general quaternionic algebra. Both have a left identity, and both
induce a bilinear form by squaring.

**The plain product $\tilde P\tilde Q$** is the only associative one and the only one with a two-sided
identity. Its form $B=\mathrm{Sc}(\tilde P\tilde Q)$ is $-\mathrm{I}_4$ on $\mathbb{M}_-$ and
$+\mathrm{I}_4$ on $\mathbb{M}_+$, so it is definite on each sector and carries the **sector sign**;
within each sector it has no null cone, so it carries no Lorentzian metric. The physical reading is that
this is the product of **composition**: it is associative, so it can be iterated without ambiguity, and
its identity $e_0$ is the identity operation. The algebra it defines is the algebra of material
operations, and the first physics block reads it: the ordinary product and the sector sign of its form,
the reference state and the absence of a material idempotent, the composition of material operations on
both sides, and the square roots of an element. The decomposition structure the algebra also carries —
the Peirce decomposition, the minimal left ideals and the bi-module — is mathematics, read in
*Biquaternion Ideals and Peirce Decomposition* and in *The Enveloping Algebra of the Biquaternion
Algebra and the Bi-module Structure*.

**The quaternionic product $\tilde P^{\natural}\tilde Q$** is not associative, has a left identity and
no right one, and is the only product of the four whose square is scalar. Its form
$N=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ is $(-,+,+,+)$ on $\mathbb{M}_-$ and $(+,-,-,-)$ on
$\mathbb{M}_+$, so it is indefinite on both sectors and carries the opposite signs on them, and it is
the material metric. The physical reading is that this is the product of **causality**: the scalar it
returns when an element is squared is the interval, so the light cone, the mass shell and the level sets
of the norm are read off it. The companion block is its subject, and the interval identity above is its
opening statement.

**What the two general algebras have in common is the second slot.** Both are bilinear, so both can be composed
with themselves; both have a left identity, so both admit a notion of an operation acting on the
algebra; and each satisfies exactly one law that the other does not — associativity for the first, the
scalar square for the second. They are the two ways a product can be a *rule for combining*, and the
framework uses them for the two things a rule for combining can describe: how operations compose, and
how an element is measured against the interval.

## The Two General Sesqualgebras

The two products whose second slot carries the star are conjugate-linear in the second factor, and they
are the multiplication of a **sesqualgebra over $\mathbb{C}$** — the two **general** sesqualgebras among the
six the space carries, the general plain and the general quaternionic sesqualgebra. Neither has a left identity, and both
induce a Hermitian form.

**The sesquilinear product $\tilde P\tilde Q^{*}$** has a right identity and no left one, and it is the
**derived operation** of the algebra $\mathbb{B}$ with its conjugate-linear involution ${}^{*}$. Its
form $H=\mathrm{Sc}(\tilde P\tilde Q^{*})$ is positive definite on every subspace, so it is the one form
of the four that is definite; it is the form of the state space and of the Born pairing, its Hermitian
idempotents are the pure states, and its positive cone is the state cone. The physical reading is that
this is the product of **probability**: it is the pairing that returns an amplitude between two elements
and a probability after squaring, and it is the only product of the four that carries positivity. Its
block owns the sesquilinear square, the positivity of the dagger and the reading mass equals rank.

**The general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$** has no identity on either
side. It is not the derived operation: it is the **isotope** of the derived operation by the natural
conjugation, $\tilde P\star\tilde Q={}^{\natural}(\tilde P)\tilde Q^{*}$, so it is obtained from the
sesquilinear product by acting on the first slot and not by deriving anything new from the algebra. Its
form $K=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$ is indefinite, of signature $(1,3)$ on each of the
four four-dimensional subspaces, so it is a Krein form. The physical reading is that this is the product
of **gauge**: it is the pairing of an indefinite-metric structure, in which positivity is replaced by a
sign, and it is the standard form of the fourth product in the theory of sesqualgebras.

**What the two general sesqualgebras have in common is the second slot**, exactly as before. Both are
sesquilinear, so both are pairings rather than compositions and neither can be iterated unambiguously —
the associativity of both fails, and it fails on explicit basis triples recorded in *Comparison Between
the Four General Products*. Neither has a left identity. They differ in the first slot, and the
difference is that one is positive definite and the other is indefinite.

## The Four Forms Compared

Each block of the menu reads one form. The comparisons between the four forms belong to no single block,
and they are collected here. The first thing the comparison shows is that the four forms are **not four
independent objects**: they are one bilinear form read through the two involutions. The scalar form of
the plain product is the reference,

$$
B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu ,
$$

and the other three are obtained from it by reading the first argument through ${}^{\natural}$, the
second through ${}^{*}$, or both:

$$
N(\tilde P,\tilde Q)=B(\tilde P^{\natural},\tilde Q),\qquad
H(\tilde P,\tilde Q)=B(\tilde P,\tilde Q^{*}),
$$
$$
K(\tilde P,\tilde Q)=N(\tilde P,\tilde Q^{*})=H(\tilde P^{\natural},\tilde Q)=B(\tilde P^{\natural},\tilde Q^{*}).
$$

Nothing beyond the definitions is used: $B(\tilde P,\cdot)$ is the scalar part of the plain product, so
substituting a conjugated argument into $B$ returns the scalar part of the product whose slot carries
that conjugation. The four forms are the four cells of the grid read at the level of numbers, and these
identities are the companion, at the level of forms, of *Relations Between the Four General Products*, which states the corresponding relations between the products themselves.

| | second slot $=\mathrm{id}$ | second slot $={}^{*}$ |
|---|---|---|
| **first slot $=\mathrm{id}$** | $B$, symmetric, **definite on each sector** | $H$, Hermitian, **positive definite everywhere** |
| **first slot $={}^{\natural}$** | $N$, symmetric, **indefinite** | $K$, Hermitian, **indefinite** |

### The Six Subspaces

The two-sector collapse below is the coarse reading. The fine reading places the four forms on the six
distinguished real subspaces at once, and it is the table from which each block takes its own row. A
restriction is read by choosing a real basis of the subspace and recording the signature of the
restricted form. On the four four-dimensional subspaces all four forms are real-valued, because those
subspaces contain both halves of each coefficient. On the centre and on the vector subspace, which are
complex lines in each coordinate, the pairing of a real basis direction with its imaginary companion is
purely imaginary, of value $\pm i$, and it is the **real part** of the form that is realified and
carries the signature.

| subspace | $\dim_{\mathbb{R}}$ | $B$ | $N$ | $H$ | $K$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $(1,1)$ | $(1,1)$ | $(2,0)$ | $(2,0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $(3,3)$ | $(3,3)$ | $(6,0)$ | $(0,6)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_+$ | $4$ | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_-$ | $4$ | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |

**Remark (verified).** The table is checked on the six real Gram matrices in the natural bases, and the
computed inertias agree with it on all six rows. The two rows the physics uses directly are the two
sectors, and their diagonals show the pattern in numbers. On the material basis $\{ie_0,e_1,e_2,e_3\}$
the diagonals of $B,N,H,K$ are $\mathrm{diag}(-1,-1,-1,-1)$, $\mathrm{diag}(-1,1,1,1)$,
$\mathrm{diag}(1,1,1,1)$ and $\mathrm{diag}(1,-1,-1,-1)$, reproducing $(0,4)$, $(3,1)$, $(4,0)$ and
$(1,3)$; on the informational basis $\{e_0,ie_1,ie_2,ie_3\}$ the two **bilinear** diagonals change sign,
to $\mathrm{diag}(1,1,1,1)$ and $\mathrm{diag}(1,-1,-1,-1)$, while the two **Hermitian** diagonals are
unchanged, reproducing $(4,0)$, $(1,3)$, $(4,0)$ and $(1,3)$. The Hermitian diagonal of $K$ is
$Q_0\overline{Q_0}-Q_1\overline{Q_1}-Q_2\overline{Q_2}-Q_3\overline{Q_3}$ in every basis, which is the
$\varepsilon$-sign the first slot supplies and the reason its signature is the same on all four
four-dimensional subspaces.

Three features are read off the table and used throughout the corpus. **$H$ is positive definite on
every subspace**, so it carries no signature and marks no subspace; it is the form of the state space
and the Born pairing. **Each indefinite bilinear form is definite on exactly one pair of the
four-dimensional subspaces**: $N$ on $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, the pair
exchanged by multiplication by $i$, and $B$ on $\mathbb{M}_+$ and $\mathbb{M}_-$, the pair exchanged by
the dagger; the first pair is the quaternionic split and the second the material–informational split.
**$K$ has the same signature $(1,3)$ on all four four-dimensional subspaces**, so it distinguishes the
four from the centre and the vector subspace but not from one another, which is why it is the natural
form of the Krein space rather than a marker of a particular subspace.

### The Two Sectors

On the two sectors the comparison sharpens, because the star is a sign there: $\tilde Q^{*}=\tilde Q$ on
the informational sector $\mathbb{M}_+$ and $\tilde Q^{*}=-\tilde Q$ on the material sector
$\mathbb{M}_-$. Substituting that into the two identities above, with both arguments taken in the same
sector, gives the relations between the two rows of the grid,

$$
H=B \ \text{ and } \ K=N \ \text{ on } \mathbb{M}_+,\qquad
H=-B \ \text{ and } \ K=-N \ \text{ on } \mathbb{M}_- .
$$

**The two sesquilinear forms are therefore the two bilinear forms read through the sector sign**, and on
a given sector only two of the four forms are independent. Written on the two sectors, the four
restrictions are

| form | on $\mathbb{M}_-$ | on $\mathbb{M}_+$ | the relation between the rows |
|---|---|---|---|
| $B$ | negative definite, $(0,4)$ | positive definite, $(4,0)$ | the sector sign |
| $N$ | indefinite, $(3,1)$ | indefinite, $(1,3)$ | the interval, and its sign on the sector |
| $H$ | positive definite, $(4,0)$ | positive definite, $(4,0)$ | $H=\pm B$ |
| $K$ | indefinite, $(1,3)$ | indefinite, $(1,3)$ | $K=\pm N$ |

**Remark (verified).** The four identities were checked on $100$ random pairs in each sector, together
with the diagonal signs of the table. The identities hold to machine precision, and the realified
diagonals of $B,N,H,K$ are $(-1,-1,-1,-1)$, $(-1,1,1,1)$, $(1,1,1,1)$, $(1,-1,-1,-1)$ on $\mathbb{M}_-$
and $(1,1,1,1)$, $(1,-1,-1,-1)$, $(1,1,1,1)$, $(1,-1,-1,-1)$ on $\mathbb{M}_+$, reproducing the inertias
$(0,4)$, $(3,1)$, $(4,0)$, $(1,3)$ on $\mathbb{M}_-$ and $(4,0)$, $(1,3)$, $(4,0)$, $(1,3)$ on
$\mathbb{M}_+$. These are the two sector rows of the table of §*The Six Subspaces*; what is added here
is the last column, which compares the rows with each other.

**The two rows under the sector exchange.** Multiplication by the central imaginary carries
$\mathbb{M}_-$ to $\mathbb{M}_+$ and back, and it acts on the two rows of the grid by their pair:
the two **bilinear** forms change sign,

$$
B(i\tilde P,i\tilde Q)=-B(\tilde P,\tilde Q),\qquad
N(i\tilde P,i\tilde Q)=-N(\tilde P,\tilde Q),
$$

while the two **sesquilinear** forms are unchanged,

$$
H(i\tilde P,i\tilde Q)=H(\tilde P,\tilde Q),\qquad
K(i\tilde P,i\tilde Q)=K(\tilde P,\tilde Q).
$$

Each identity is the centrality of $i$ and the definitions, and nothing else: $i$ pulls out of both
slots of the bilinear pair, and out of the first slot of the sesquilinear pair it leaves the sign that
the bar contributes in the second. The grid therefore splits $2+2$ under the exchange, and the split is
the row split: the bilinear row is the class the sector exchange flips, the sesquilinear row the class
it preserves. The two flips are the sign reversal of the interval and of the composition, and they are
the two signatures $(3,1)$ against $(1,3)$ and $(0,4)$ against $(4,0)$; the two invariants are the
probability and the indefinite gauge metric, which is why a probability carries no sign of the sector
while a metric carries it. The exchange is the framework's Wick rotation
(*The Four Other Remarkable Subspaces*), and this is its statement at the level of the forms.

**Remark (verified).** The four identities were checked on $100$ random pairs of general complex
elements, not only on the sectors, and hold identically; on a sector they reduce to the row relations
$H=\pm B$ and $K=\pm N$ above.

**The exchange-invariant square.** A quantity built from a **tensor square** of a bilinear form,
$N(\tilde{P}_1,\tilde{Q}_1)N(\tilde{P}_2,\tilde{Q}_2)$, is built from two factors that the exchange
reverses, so the exchange multiplies it by $(-1)(-1)=+1$: the tensor square of a bilinear form is
therefore **invariant** under the sector exchange and carries no sign of the sector, while a tensor
square of a sesquilinear form is invariant for the opposite reason, each factor being fixed. The
correlation structure of a two-qubit state is built from the bilinear row alone, so it sits **outside**
the four-row grid rather than in one of its cells, and the two-qubit articles are indexed by the tensor
square and not by a row. Recomputed on $100$ random pairs:
$N(i\tilde{P}_1,i\tilde{Q}_1)N(i\tilde{P}_2,i\tilde{Q}_2)=N(\tilde{P}_1,\tilde{Q}_1)N(\tilde{P}_2,\tilde{Q}_2)$
on $100$ of $100$. Boundary: the identity states which sign the exchange carries and says nothing about
the size of the correlation, which is computed in *Quantum Discord and Correlations Beyond Entanglement
in Biquaternionic Form* and *Two Spin-Half Particles in Biquaternionic Form*.

### The Reading

The comparison is what makes the four readings of §*The Four Readings* precise, and it adds three
statements that no single block can make.

**The sector sign is $B$, and it is $H$ that does not see the sectors.** $B$ is definite with opposite
signs on the two sectors, so it is the one symmetric form that tells them apart; $H$ is positive
definite on both, so it is blind to the difference. The two are the same numbers up to the sign of the
sector, and that is the precise sense of the corpus's rule that the material sector is *visible in the
bilinear layer and invisible in the sesquilinear one*: the visible form is $B$, the invisible one is
$-B$, which is $H$ there.

**The interval and the indefinite metric are the same numbers, one row apart.** $N$ and $K$ agree on
$\mathbb{M}_+$ and oppose on $\mathbb{M}_-$, and each is indefinite with one sign and three of the other
on each sector. Read physically, the bilinear row supplies the metric of spacetime, $N$ with its light
cone and its mass shell, while the sesquilinear row supplies the metric of an indefinite-metric quantum
theory, $K$; and on the informational sector the two metrics coincide, which is the algebraic reason the
two readings are easy to conflate.

**Every structure the corpus uses is one of the four cells.** $B$ for the sector sign, $N$ for the
interval, the light cone and the mass shell, $H$ for positivity, the Born pairing and the state space,
$K$ for the indefinite metric of the gauge side. The comparison says that the framework does not use
four unrelated forms but one form and two dials, and that the dial ${}^{\natural}$ is the one that
produces a metric: it turns $B$ into $N$ in the bilinear row and $H$ into $K$ in the sesquilinear one.

**The four forms are four measurements of one frame.** Because each cell is one pairing of one element
with another, each form answers one question about a pair: $B$ how the two **compose**, $N$ whether one
can **influence** the other, $H$ with what **probability** one reaches the other, $K$ how the two sit in
the **gauge** frame. The four corners are then not four structures but the four readings a single frame
invites, and a physical theory is a choice of which reading is the measured one. Read this way the grid
is a grid of questions, and the corpus's four blocks are the four answers.

**The signature is what an object is.** The signature of the form decides the kind of object it counts:
$H$ is definite of signature $(8,0)$ on the real algebra and counts **states**, while $K$ is indefinite of
signature $(2,6)$ and counts a **constraint**, a quantity with a sign and a direction that is not a state.
The distinction the framework draws between the state side and the gauge side is therefore carried by the
signature alone: a definite Hermitian form is a state structure, an indefinite one is a structure of
redundancy and constraint, and no further input separates them. This is the analytic content of the
corpus's rule that the fourth product is a gauge structure and not a state space.

**One principle separates the state side from the transformation side.** The two dials do two different
jobs and they compose into a single rule. The **second** slot's star makes the form Hermitian, and the
**first** slot's natural conjugation decides whether that Hermitian form is definite or indefinite. So the
plain slot is positive and carries the probability, the quaternionic slot is indefinite and carries the
causal and gauge metric, and one principle — read the first slot without or with ${}^{\natural}$ —
distinguishes the state side from the transformation side of the whole grid. The two metrics of a single
element (*Mass, Rank and the Positivity of the Dagger*) are the two outcomes of that one principle.

**Geometry and symmetry are complementary, and no single product carries both.** The comparison makes a
division visible that no block states: the **metric** lives in the symmetric, order-free layer and the
**symmetry obstruction** lives in the antisymmetric, order-carrying layer. The interval is the diagonal of
the symmetric part of the quaternionic product, and the Jacobi failure is the obstruction of its
antisymmetric part; the symmetric half is where the form is, the antisymmetric half is where the failure
is. So the grid does not place the metric and the group in one product: it separates them into the two
halves of a product and into two rows of the grid. This is the grid-level form of the corpus's rule that
the coupling carries the metric and the order carries the obstruction. The two are read in *The Quaternion
Form as a Product: the Scalar Coupling of Two Material Operations* and *Boosts, Mixed Terms and the
Missing Lie Structure*.

**The two sectors are coupled algebraically, once.** The grid is a grid of forms; the two sectors of the
framework are coupled by one map that the grid itself supplies, and it is not a form but the **square**:
the square of a material element is its interval, a real number, and the real scalar line is contained in
$\mathbb{M}_+$, so squaring carries $\mathbb{M}_-\to\mathbb{M}_+$. The map and its proof are *The Interval
as the Square and the Charge of the Material Composition*; it is recorded here because it is the one
cross-sector statement that sits at the level of this article, and because it is a partial answer to the
open question of the introduction about a coupling between the two sectors. It is a map and not a
dynamics, and the caution of that article carries over.

**Caution.** The identities are form-level and are read on the sectors, with both arguments taken there;
they do not say that the four general products agree. Off the sectors the four forms are four. In particular
$K=N$ on $\mathbb{M}_+$ does not make the general quaternionic sesquilinear product a bilinear one there, and
$H=-B$ on $\mathbb{M}_-$ does not make the ordinary product a pairing.

### Named Readings of the Grid

Three further readings of the grid are recorded here, each under a name of its own and each labelled a reading rather than a theorem; the counts they rest on are the body's.

- **Twelve-to-ten measure.** The fall of the twelve operations to ten on the real part is read as a **measure of the complex structure** the grid carries: two distinctions are lost when the coefficients are restricted to the reals, and the count $12$ against $10$ is the algebraic size of the complex structure of the framework. The reading is the grid-level counterpart of *classical blindness* in *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure*, and its boundary is that the count is a count of operations and not a measure of a physical complexification.
- **Involution grid.** The four general products are read as the **four cells the two slots admit**: the identity or the natural conjugation ${}^{\natural}$ in the first slot and the identity or the star ${}^{*}$ in the second, and never ${}^{*}$ in the first nor ${}^{\natural}$ in the second, which is the rule of §*The Two Slots*. The name makes the grid a single object with two dials and not a list of four constructions. Its boundary is the corpus's own: the twelve unused slot pairs are not transposes or conjugates of the four used ones, so the grid of four is a genuine restriction of the algebra and not a redundancy of naming, and the four cells are therefore **not** the orbit of one product under the two involutions.
- **Dial principle.** The rule that the first slot's natural conjugation decides between the definite form of the state side and the indefinite form of the transformation side is read as the **dial principle** of the framework: one dial separates the state side from the transformation side of the whole grid, and the two metrics of a single element are its two outcomes. The name is given here so that the principle can be cited as a single rule; the boundary is that the principle is a statement about the forms and not a derivation of the two jobs. The dial is a **reflection** — it negates the three vector coordinates and fixes the scalar direction, so it is a change of frame in the strict sense — and it is the algebraic sibling, and not the equal, of the framework's **Wick rotation**, which is multiplication by the central imaginary and a quarter-turn exchange of the two sectors (*The Four Other Remarkable Subspaces*, *The Wick Rotation in the Biquaternion Universe*). The dial is an involution and the Wick rotation has order four; the rotation is central and therefore commutes with the multiplication, while the dial is an anti-automorphism that reverses the order of a product and acts on one argument of it. Only the dial is a slot of a product, and it is that slot — and not the rotation — that the grid's metric is made of.

## The Four Readings

The table collects the four jobs. It is the framework's reading of the grid, and its last column is a
reading and not a theorem.

| product | slots | scalar form | the form on $\mathbb{M}_-$ | the physical job | status of the reading |
|---|---|---|---|---|---|
| $\tilde P\tilde Q$ | $(\mathrm{id},\mathrm{id})$ | $B$ | definite, $(-,-,-,-)$ | **composition** | the algebra of material operations |
| $\tilde P^{\natural}\tilde Q$ | $({}^{\natural},\mathrm{id})$ | $N$ | indefinite, $(-,+,+,+)$ | **causality** | the interval and the cone |
| $\tilde P\tilde Q^{*}$ | $(\mathrm{id},{}^{*})$ | $H$ | positive definite, $(+,+,+,+)$ | **probability** | the state space and the Born pairing |
| $\tilde P^{\natural}\tilde Q^{*}$ | $({}^{\natural},{}^{*})$ | $K$ | indefinite, $(+,-,-,-)$ | **gauge** | the indefinite metric |

What is proved is the left half of the table: the four general products are the four slot pairs, and the four
forms have the signs shown, by §*What the Two Slots Decide* and by §*The Four Forms Compared*, which
also states the relations among the four forms. What is read is the last two columns: that composition,
causality, probability and gauge are the four jobs a relativistic quantum theory needs, and that the
grid is a grid of jobs. **That the four jobs are these four is a claim about the framework and not a
consequence of the algebra**, and it is offered as such. What can be said in its favour is that the four
jobs are independent: a theory needs a rule for combining operations, a rule for saying which events can
influence which, a rule for assigning probabilities, and a rule for handling the redundancy of its
description, and the four forms supply exactly one candidate for each. What cannot be said is that no
other assignment of the four is possible.

**Reading (four jobs and two halves).** Each of the four general products splits into a symmetric and an
antisymmetric half, so the twelve products of the space are the four general products together with the
two halves of each: a **magnitude half** (the symmetric part, which carries the form, the interval and
the pairing) and an **order half** (the antisymmetric part, which carries the bracket and the
obstruction) attached to each job. The reading is thin, and is offered as one because the selection is
severe: only two of the twelve satisfy a classical identity, the antisymmetric plain bilinear product
being a Lie bracket and the symmetric plain bilinear product a Jordan product, and every other half is a
structure without a classical identity of its own. So the grid's twelve are not twelve equivalent structures but four jobs, each with a
metric half and an order half, of which only the two halves that close are classical. The claim that this
is a selection principle is the framework's and is not proved; the count and the two exceptional halves
are. The twelve themselves are *The 12 Products of the Biquaternion Complex Space* and the two that pass
are *The Unitary Lie Algebra* and *The Hermitian Jordan Algebra*.

## Further Readings of the Rows

The readings below are read one row at a time. Each is labelled a reading, each rests on a carrier the body
has proved, and none adds a theorem.

### The Composition Row

- **Composition is the plain product; the interval is not.** The scalar form $B$ of the plain product is the
  **sector sign** and the bilinear pairing of the composition, and the metric of the material sector is the
  *quaternionic* form $N$, which the first slot's dial produces (§*The Two Steps*). The two forms are the two
  jobs of the row and must not be exchanged: reading $B$ as the metric, or $N$ as the scalar of the
  composition, is the confusion the row invites.
- **The monoid of acting maps.** The elements are oriented and the plain product is associative, but the
  physical process is not the element; it is the **act** of multiplying. The left multiplications
  $L_{\tilde P}:\tilde R\mapsto\tilde P\tilde R$ form an associative **monoid** under composition, with the
  identity $L_{e_0}$; it is a monoid and not a group, since only the units are invertible. Two consequences
  are read from this. First, the **twisted** actions are not a monoid, because the twisted products are not
  associative; it is the plain action alone that composes. Second, a measurement is a projection, and the
  projections of the framework are the idempotents of the informational sector $\mathbb{M}_+$, not the
  invertible elements of the action monoid; the process side is the monoid of actions and the state side is
  the idempotents, and the two are not the same object. Reading: the physical process is the monoid of
  acting maps, not the elements.
- **The associator is a three-way interaction.** The plain product is associative, and it is the **twisted**
  products that are not: the associator of the quaternionic products is a nonzero trilinear form. Read
  physically, a non-vanishing associator is the algebraic image of an **irreducible term in three
  operations**, a genuine three-way interaction that cannot be assembled from two-body pieces. The reading
  pairs with the corpus's ternary-product articles (*Particle Types, Discrete Charge and Three-Particle
  Couplings*), and its boundary is that what fails to associate is the twist and not the elements.

### The Causality Row

- **The scale potential $\log|N|$.** $N$ is multiplicative, so $\log|N|$ is **additive** over the
  composition — a potential on the material sector. The reading is read on the **scale** and not on the
  rapidity: a boost rotor is Hermitian with $N=1$ at every rapidity, so $\log|N|$ vanishes on the boosts,
  while the rapidity is the **angle** of the polar form. Read physically, $\log|N|$ is a causal **dilation**
  potential and the rapidity is its angular companion.
- **The scalar coupling is the kinematic overlap.** On two material four-vectors the quaternionic pairing
  $N(\tilde P,\tilde Q)$ is the **Minkowski inner product** of the two, in the material signature: on the
  diagonal it is the squared interval, that is the mass shell, and off the diagonal the kinematic overlap of
  two momenta. The cone is the on-shell condition, and the non-degeneracy of $N$ on the off-cone material
  directions is the non-degeneracy of the kinematics. The reading must name the sector: it is the
  **quaternionic** pairing, on $\mathbb{M}_-$, that carries the Minkowski sign.
- **The Jacobi failure needs one leg in each real form.** The gauge bracket fails the Jacobi identity, and
  the failure is **not** confined to the boosts: recomputed, it vanishes on triples taken wholly in the
  rotation directions and vanishes on triples taken wholly in the boost directions, and it is generic only
  when a triple carries **one leg in each of the two real forms**. Read physically, the obstruction is
  neither the compact nor the non-compact part alone but their **mixing** — a consistency condition that
  neither the rotation nor the boost subgroup can see alone. The reading is labelled: it does not by itself
  select the internal group, whose ceiling has its own cause (*The Gauge Group Ceiling: Why the Biquaternion
  Algebra Reaches SU(2) but Not SU(3)*).

### The Probability Row

- **Probability is centrality.** The symmetric sesquilinear product is a **central** number, and a number
  selects no state; the states are the idempotents, not the values of the product. Reading: the row supplies
  a weight and no state.
- **The argument is the geometric phase of the cone.** The Born pairing has a real part, the probability
  $H$, and a vector part, the phase; the **argument** of the amplitude is the geometric (Pancharatnam) phase,
  and the vector part is the axis the phase is built on. Reading: the phase of the probability row is the
  geometric phase of the cone, which is the grid-level form of the corpus's phase articles.

### The Gauge Row

- **The axial value is a polarisation direction.** The gauge product's value is a vector in the axial
  directions, and its three components read as the **polarisation** or **spin** direction of the gauge
  object. Reading: the row carries a direction and not a state.
- **Discrete charge is compactness.** The charge lives on the compact part of an internal generator and the
  rapidity on the non-compact part, and the split is the compact/non-compact split of that generator. The
  reading is anchored to a generator of a **bracket that closes** — the gauge product's bracket does not
  close and carries no Killing form, so the split must not be read from it — and its boundary is that the
  number of discrete charges is the rank of the compact part, here the one of a single internal $U(1)$.

### Cross-Cutting

- **Two times on one complex axis.** The central imaginary exchanges the two sectors,
  $i\mathbb{M}_\pm=\mathbb{M}_\mp$; the framework's parameter time and coordinate time are two **real
  structures** of one complex time, and multiplication by the central $i$ is the quarter turn of that
  complex time, exchanging the two. Read physically, the problem of time becomes the question of **which
  real slice is physical**. The reading is a reading of the sector structure and not a resolution. **Caution
  on the word:** the corpus uses *Wick rotation* in two ways, and the generator is the first and not the
  second. Multiplication by $i$ is the exchange of the real and imaginary sectors and the quarter turn of
  the complex time, which *The Four Other Remarkable Subspaces* names the Wick rotation; the analytic
  continuation $t\mapsto-i\tau$ of *The Wick Rotation in the Biquaternion Universe* is a **relabeling** of
  the time coordinate that holds the space real, is real-linear, and is not the multiplication by $i$. The
  two share the temporal sign flip and the time axis and diverge off it; the whole reading is
  *Conventions in the Biquaternion Universe*, §*The Central Map and Its Six Restrictions*.
- **Phase and duality are one central $U(1)$.** The complex-time sector carries the global phase, the
  complex-space sector carries the field strength, and multiplication by the central $i$ is at once the phase
  rotation and the **duality rotation** of the field. Reading: one central $U(1)$ does both jobs.
- **The interval is a clock and the Euclidean square a ruler.** One biquaternion space yields two metrics: the
  indefinite $N$ has the causal structure of a **clock** (the cone, the interval), and the definite $H$ that
  of a **ruler** (the length, the probability). Reading: the two metrics of one element are the two
  instruments, and the grid is why one biquaternion space carries both. The uniqueness clause is not claimed; the two
  metrics are.
- **The $4\times3$ table as a mnemonic.** The four products and the three involutions read as twelve
  questions — composition, commutation, rotation, causality, coupling, obstruction, decision, weight, phase,
  gauge, measurement, polarisation. The reading is offered as a **mnemonic** and not as a completeness
  claim: the article's own caution is that no single product carries both halves, and the table does not
  assert that these twelve are the only questions.

## The Two Steps

The grid has an origin and two generators, and the two generators are physical operations. The two steps
are the products' version of the form identities of §*The Four Forms Compared*, and the second step is
the dial that the comparison identifies as the producer of the metric.

**Insert the star in the second slot, and read the second factor through ${}^{*}$.** The composition
becomes a pairing, the bilinear form becomes Hermitian, and a value becomes an amplitude. This is the
step from an algebra to its sesqualgebra, and **the reading proposed for it is quantisation**: a
classical composition of operations is replaced by a pairing that can be squared into a probability.

**Reading (the star is the Riesz duality of the pairing).** The second slot is where the conjugation enters, and it changes the linearity of the form. Read without a conjugation, the product is $\mathbb{C}$-bilinear and its form pairs two elements linearly; read with the star, the Hermitian form
$H$ (*The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*) is linear in the first argument and conjugate-linear in the second, so the map that sends an element to its pairing against a fixed other, $\tilde Q\mapsto H(\cdot,\tilde Q)$, is **anti-linear** and is exactly the **Riesz map** that identifies the algebra with its dual. The second slot is therefore the conjugate-linear slot, and the second factor is read as the **bra** of the first. Read this way the Born pairing is not an added structure but a **choice of slot** — the star chooses the anti-linear side — and an amplitude is a number read from the pairing of an element with a dual element. The reading is labelled: the star supplies the Hilbert structure and the identification of the dual, and no equation of motion and no measure.

**Insert the natural conjugation in the first slot, and read the first factor through the map
${}^{\natural}$.** The form becomes indefinite on each sector, so a metric appears, and the coefficient
$\varepsilon$ is toggled — cancelled in the bilinear row and supplied in the sesquilinear one. This is
the step from an algebra to a quaternionic algebra and from a sesqualgebra to a quaternionic
sesqualgebra, and **the reading proposed for it is the appearance of a metric**. It is the same step in
both rows: in the bilinear row it turns $B$ into $N$ and produces the interval, and in the sesquilinear
row it turns $H$ into $K$ and produces an indefinite metric.

**Reading (the quaternionic product is the plain product in a conjugated frame).** The identity
$N(\tilde P,\tilde Q)=B(\tilde P^{\natural},\tilde Q)$ says that the quaternionic form is the plain form
with its **first argument read in the naturally conjugated frame**; equivalently the quaternionic product
$\tilde P^{\natural}\tilde Q$ is the plain product of the conjugated first factor with the second. The
composition rule is untouched — it is the same multiplication of the same algebra — and what the frame
change does is move the metric: the plain form of the conjugated frame is the indefinite interval, the
plain form of the untouched frame is the definite Euclidean square. The reading is that the dial
${}^{\natural}$ is a **change of frame**, and that the appearance of the metric is the appearance of the
interval under that change; it is a re-reading of the two identities above and is labelled as a reading.
The same frame language covers the sesquilinear row, where the coefficient $K$ is $H$ of the conjugated
frame.

**The two steps commute**, because the two slots are read independently, and the fourth corner is the
result of taking both. That is the sense in which the four objects are not four independent structures
but one structure with two dials. The fourth corner is therefore the pairing with an indefinite metric,
which is the standard setting of an **indefinite-metric quantum theory**: the framework of
Gupta–Blokhintsev, of BRST quantisation, of PT-symmetric quantum mechanics, and the form of the
Klein–Gordon charge. The reading of the fourth corner is that the framework's own quantum theory is the
*first* column of the sesquilinear row, with a positive definite form, and that the fourth product is
what one gets by turning the metric dial while keeping the pairing.

### What Bounds the Fourth Corner

Three proved negative results limit what the fourth product can be asked to do, and all three are recorded
because they are what makes the reading in the table above a reading of *gauge* rather than of a second
state space.

- **No identity on either side.** Unlike the sesquilinear product, which has a right identity, the
  general quaternionic sesquilinear product has none, so it is not the derived operation of the algebra with any
  involution; it is the ${}^{\natural}$-isotope of the derived operation instead.
- **The ternary product is not a Jordan triple.** The ternary product built from it has the parity of
  an algebraic $J^{*}$-algebra and satisfies the symmetry and linearity axioms of a Jordan triple
  system, but it fails the Jordan triple identity on the explicit five-tuple $(e_0,e_1,e_0,e_2,e_0)$,
  where the two sides are $e_3$ and $-3e_3$. So the algebra with this product is **not** the state space
  of a quantum theory, and no state space is obtained from it.
- **No associativity either: the associator as the curvature of the pairing.** The fourth product does not
  compose. Its associator $(\tilde A\star\tilde B)\star\tilde C-\tilde A\star(\tilde B\star\tilde C)$ is
  nonzero on $256$ of the $512$ triples of the eight-element basis, at the clean witnesses $(e_0,e_0,e_1)$,
  where it is $-2e_1$, and $(e_0,e_1,e_1)$, where it is $2e_0$. The defect carries both a central and a
  vector part, so — unlike the Jacobi defect of the antisymmetric half, which is purely vector — it is not
  confined to one grade. Read as the failure of parallel transport to be path-independent, an associator is
  the **curvature** of the multiplication, and the pairing is therefore read as carrying a curvature whose
  values are the local holonomies of a multiplication that does not compose. The name is this article's;
  the failure, the count and the witnesses are the algebra.

The first is the reason the fourth product is not derived from the algebra; the second is the reason it
is not a state space; the third is the reason its multiplication carries a curvature rather than a
composition. Together they leave it a structure with a symmetry and a pairing but without a unit, a
composition or the positivity that counts states, and that is the precise sense in which it is the
**gauge side** of the frame rather than the state side. This reading is a reading of what remains after
the three negative results, and it is labelled as such.

**Where the failures come from.** The fourth product fails associativity *and* fails the Jacobi identity: the associator does not vanish and the cyclic sum of the antisymmetric half does not vanish. Neither failure is the work of the *first* slot alone, and the pairing must not be blamed for both. Inserting a nontrivial involution into *either* slot spoils composition and closure: the plain sesquilinear product, which conjugates the second slot only, already fails associativity on $256$ of the $512$ basis triples, and its antisymmetric part already fails the Jacobi identity on $252$. What the first-slot conjugation adds is different and sharper — the **metric** (the sign vector $\varepsilon$ and the indefinite signature), the loss of the unit, and the loss of the Jordan triple identity — the three the mathematics attributes to the first slot, and exactly the two no-go results (no unit, no Jordan triple) that the first slot contributes to the bounds of the corner. The non-associativity and the non-closure are shared with the sibling readings and are not the first slot's signature.

**Why the frame's fourth product is gauge and not a graded structure.** A gauge structure at the product
level carries a pairing and a bracket; a BRST or superalgebraic structure carries, in addition, a
$\mathbb{Z}_2$ grading and a graded bracket with a sign rule. The fourth product supplies the first and not
the second: its bracket is not graded, and no grading is read from the four general products. The
framework's own BRST complex and its odd extension are therefore **separate constructions**, built on the
algebra but not read off the fourth product — *BRST Symmetry in Biquaternionic Form* and *The Superalgebra
Reading and the Odd Extension with Signed Hermitian Adjoint in Biquaternionic Form* — and the word *gauge*
in the table above is the pairing-based sense, the metric of the transformation side, and not the graded
sense. The boundary keeps two uses of one word apart.

## The Four Blocks and the Division of Labour

The four subcategories of `## Biquaternion Mathematical Physics` that carry the four general products are the
four objects this article maps, and they are placed in the order of the corpus's own naming:

| block of the physics menu | the product | the form | the maths anchor |
|---|---|---|---|
| *Focus on the General Plain Algebra (GPA) of Biquaternions — Composition* | $\tilde P\tilde Q$ | $B$ | *Introduction to the General Plain Algebra of Biquaternions* |
| *Focus on the General Quaternionic Algebra (GQA) of Biquaternions — Causality* | $\tilde P^{\natural}\tilde Q$ | $N$ | *Introduction to the General Quaternionic Algebra of Biquaternions* |
| *Focus on the General Plain Sesqualgebra (GPS) of Biquaternions — Probability* | $\tilde P\tilde Q^{*}$ | $H$ | *Introduction to the General Plain Sesqualgebra of Biquaternions* |
| *Focus on the General Quaternionic Sesqualgebra (GQS) of Biquaternions — Gauge* | $\tilde P^{\natural}\tilde Q^{*}$ | $K$ | *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* |

The division of labour among the four is fixed, and the corpus keeps to it.

- **The block of the algebra over $\mathbb{C}$** carries the algebra of operations and its sector: the
  ordinary product, its associativity and its unit, the sector sign of its form, the reference state and
  the absence of a material idempotent, the composing multiplications, and the square roots of elements.
  The ideals, the Peirce decomposition and the enveloping algebra of the algebra are mathematics, and
  the block cites them instead of reproducing them.
- **The quaternionic algebra** carries the interval and the light cone: the form $N$, the norm, the
  zero-divisor cone, the mass shell and the isometry group of the interval.
- **The sesqualgebra** carries the state space: the sesquilinear product, the positivity of the
  dagger, the state cones and the Born pairing.
- **The quaternionic sesqualgebra**, the fourth corner, carries the indefinite structure: the
  general quaternionic sesquilinear product and the Krein form $K$, the indefinite-metric companion that is not
  a state space.

From this follow the two rules that make the four blocks readable as four. **A block reads its own
product and its own form**, and cites the others instead of reproducing them. **A comparison that
crosses the grid belongs to this article**, not to any of the four blocks: §*The Four Forms Compared* is
the worked case, since the mutual relations of the four forms are read here and each block uses them
without re-deriving them. This article is the map; the four blocks are the territory, and neither
replaces the other.

## The Ledger

**Proved.** The four general products are the four slot pairs $(K_1,K_2)$, with the first slot in
$\{\mathrm{id},{}^{\natural}\}$ and the second in $\{\mathrm{id},{}^{*}\}$; that is the indexing of the
four general products already defined in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and not a further statement
about them. The two slots decide the properties tabulated in §*What the Two Slots Decide*: bilinearity,
the left identity and the monoid of the left multiplications by the second slot; definiteness on each
sector and the right identity by the first slot; the coefficient $\varepsilon$ by the two slots
together; and associativity by both. $e_0$ is a left identity if and only if the second slot is trivial
and a right identity if and only if the first slot is trivial, so exactly one of the four is associative
and two-sidedly unital. The scalar forms are $B=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$,
$N=\sum_\mu P_\mu Q_\mu$, $H=\sum_\mu P_\mu\overline{Q_\mu}$ and
$K=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, so that $\varepsilon$ survives exactly when the two
slots agree and the bar appears with the second slot. The quaternionic product is the only one of the
four whose square is scalar, and $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0$. Only the sesquilinear
product is the derived operation of the algebra with ${}^{*}$, and the general quaternionic sesquilinear product
is its ${}^{\natural}$-isotope and has no identity on either side. The four scalar forms are one
bilinear form read through the two involutions, $N(\tilde P,\tilde Q)=B(\tilde P^{\natural},\tilde Q)$,
$H(\tilde P,\tilde Q)=B(\tilde P,\tilde Q^{*})$ and
$K(\tilde P,\tilde Q)=B(\tilde P^{\natural},\tilde Q^{*})$, and on the two sectors $H=\pm B$ and
$K=\pm N$ with the sign of the sector, so that on a sector only two of the four forms are independent;
the restrictions read negative definite, $(3,1)$, positive definite and $(1,3)$ on $\mathbb{M}_-$ and
positive definite, $(1,3)$, positive definite and $(1,3)$ on $\mathbb{M}_+$. The full restriction table
of §*The Six Subspaces* is the companion statement: $H$ is positive definite on all six subspaces, each
indefinite bilinear form is definite on exactly one pair of the four-dimensional subspaces, and $K$ has
the same signature $(1,3)$ on all four of them. The fourth product is non-associative: its associator is
nonzero on $256$ of the $512$ triples of the eight-element basis, at the clean witnesses $(e_0,e_0,e_1)$,
where it is $-2e_1$, and $(e_0,e_1,e_1)$, where it is $2e_0$, and the defect carries both a central and a
vector part.

**Readings.** That the four general products are composition, causality, probability and gauge; that inserting
the star reads as quantisation and inserting the natural conjugation reads as the appearance of a metric
— the same dial that turns $B$ into $N$ and $H$ into $K$; that the fourth corner is the gauge side
of the frame rather than a second state space; that the four forms are **four measurements of one
frame**, one question about a pair per cell; that the **signature is what an object is**, a definite
Hermitian form counting a state and an indefinite one a constraint; and that **one principle separates
the state side from the transformation side**, the second slot's star making the form Hermitian and the
first slot's natural conjugation deciding its definiteness. Each is the framework's naming of a proved
structure, and each is labelled as such. The assignment of jobs to products is offered as a reading and is not forced
by the algebra. Two further readings are added at the grid level: that **geometry and symmetry are
complementary**, the metric living in the symmetric layer and the obstruction in the antisymmetric one,
so no single product carries both; and that the two sectors are coupled algebraically once, by the square
$\mathbb{M}_-\to\mathbb{M}_+$, the one cross-sector map the grid supplies. Two more are added as
labelled readings: that the dial ${}^{\natural}$ is a **change of frame**, the quaternionic product being
the plain product in the conjugated frame, so the metric is what the frame change moves; and that the
twelve products are **the four general products together with the two halves of each**, a magnitude half
and an order half per job, of which only the two classical halves close. One point is added as a **remark
and not a reading**: the twelve unused slot pairs are *not* transposes or conjugates of the four used
ones, so the grid of four is a genuine restriction of the algebra and not a redundancy of naming. Three
further readings are added at the block level: that the associator of the fourth product reads as the **curvature** of the
pairing, its values the local holonomies of a multiplication that does not compose; that the metric, the
absence of a unit and the failure of the Jordan triple identity are the first slot's work, while the
non-associativity and the non-closure are shared with the sibling readings that conjugate a single slot;
and that the fourth
product's *gauge* is the pairing-based sense and not the graded sense, a $\mathbb{Z}_2$-graded or BRST
structure being a separate construction on the same algebra. Three further grid-level readings are named
in §*Named Readings of the Grid*: **twelve-to-ten measure**, **involution grid** and **dial
principle**.

**One caution.** That the four jobs are the four a relativistic quantum theory needs, and that the grid
is a grid of jobs, is a claim about the framework's organisation and not a theorem about biquaternions.
The algebra fixes the grid and the signs; it does not fix the names.

## Physical Readings

Three transversal readings can be added to the map. The sector exchange sorts the four products into two classes, the two bilinear products moving with the Wick exchange and the two sesquilinear products not, and a change of the local complex structure does the same, so the sorting itself is the framework's invariant criterion (*Conventions in the Biquaternion Universe*). And the exchange read as a clock adds a reading of the temporal product: the quarter turn of the complex time sector is the tick, whose reference and period are supplied and whose arrow and rate are not (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). A third reading is the exchange-invariant tensor square: because a tensor square of a bilinear form carries no sign of the sector, the framework's correlations are **between** the rows and not inside one of them, entanglement is not a fifth job, and the partial trace of a subsystem lives on the tensor square rather than on a row.

## Summary

The biquaternion space carries four general products, obtained by inserting the involutions of the algebra into
the two slots of a multiplication, and every property of the four is decided by one slot, by both, or by
singling out one of the four. The second slot decides everything about the composition: read without a
conjugation the operation is $\mathbb{C}$-bilinear, has a left identity and has left multiplications
forming a monoid; read with ${}^{*}$ it is sesquilinear and has none of these. The first slot decides
the right identity, the definiteness of the form on a sector, and the toggle of the coefficient
$\varepsilon$: read as it stands $e_0$ is a right identity and the form is definite on each sector, and
read through ${}^{\natural}$ the form becomes indefinite on each sector, so a metric appears, while
$\varepsilon$ is cancelled in the bilinear row and supplied in the sesquilinear one. Associativity
requires both slots trivial, and the square of an element is scalar for exactly one of the four, the
quaternionic product, whose square is the interval $N(\tilde Q)e_0$. The two-and-two division by the
second slot is therefore the division of the four general products into two **general algebras over
$\mathbb{C}$** and two **general sesqualgebras over $\mathbb{C}$** — the space itself carrying six algebras
and six sesqualgebras, of which these four are the general members (*The 12 Algebraic Structures over the
Biquaternion $\mathbb{C}$ Space*) — and the two blocks of each pair are the two values of the first
slot. Reading the grid physically, the four general products are the four jobs a relativistic quantum theory
needs — composition, causality, probability and gauge — with the plain product associative and
two-sidedly unital, the quaternionic product carrying the interval, the sesquilinear product carrying
the positive definite Born form and the state space, and the general quaternionic sesquilinear product carrying
an indefinite Krein form with no identity on either side and a ternary product that is not a Jordan
triple. The four scalar forms are one bilinear form read through the two involutions, and on a sector
the two sesquilinear forms are the two bilinear ones up to the sign of that sector, so that on a sector
the four reduce to two; the comparisons that cross the grid belong here, in §*The Four Forms Compared*
and §*The Six Subspaces*, which carries the full restriction table of the four forms on the six
subspaces, and each block reads only its own product and its own form. The four subcategories of the
physics menu are these four objects, and this article is their map.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=K_1(\tilde P)K_2(\tilde Q)$ | A general product, with the two slots read independently |
| $K_1\in\{\mathrm{id},{}^{\natural}\}$ | First slot: identity or natural conjugation; the right identity, sector definiteness and the toggle of $\varepsilon$ |
| $K_2\in\{\mathrm{id},{}^{*}\}$ | Second slot: identity or star; decides the composition |
| $\tilde P\tilde Q$ | Plain product; slots $(\mathrm{id},\mathrm{id})$; associative, two-sided identity |
| $\tilde P^{\natural}\tilde Q$ | Quaternionic product; slots $({}^{\natural},\mathrm{id})$; scalar square, the interval |
| $\tilde P\tilde Q^{*}$ | Sesquilinear product; slots $(\mathrm{id},{}^{*})$; the derived operation |
| $\tilde P^{\natural}\tilde Q^{*}$ | General quaternionic sesquilinear product; slots $({}^{\natural},{}^{*})$; no identity |
| $B,N,H,K$ | The four scalar forms; $\varepsilon$ survives when the two slots agree, the bar with the second |
| $\varepsilon=(1,-1,-1,-1)$ | The sign pattern of $\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ |
| $\mathbb{M}_-$ | Material sector, the anti-Hermitian real four-space; the four forms read $(-,-,-,-)$, $(-,+,+,+)$, $(+,+,+,+)$, $(+,-,-,-)$ |
| $\mathbb{M}_+$ | Informational sector, the Hermitian real four-space; the four forms read $(+,+,+,+)$, $(+,-,-,-)$, $(+,+,+,+)$, $(+,-,-,-)$ |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ | The biquaternion norm; scalar only for the quaternionic product |
| six algebras / six sesqualgebras | the twelve structures the space carries; the four general products are the two **general** algebras and the two **general** sesqualgebras among them |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the involutions of the
  quaternion algebra, the conjugation and the bar, and the two products they generate.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the
  product that carries the interval and the metric of signature $(-,+,+,+)$.
- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* 39 (2002), for the
  complexification of the quaternions and the four general products on it.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2015), for the
  conjugate-linear involution of a Hilbert algebra and the sesquilinear form it induces.
- M. Reed and B. Simon, *Methods of Modern Mathematical Physics* II (Academic Press, 1975), for the
  Born pairing, positivity and the state space carried by the Hermitian form.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for Krein spaces, the fundamental
  decomposition and the indefinite metric carried by the fourth product.
- Mathematics article *The Four General Products of the Biquaternion $\mathbb{C}$ Space*
  (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general products and their
  definitions.
- Mathematics article *Relations Between the Four General Products*
  (`articles_maths/relations-between-the-four-general-products.md`), for the scalar and vector
  parts the four induce.
- Mathematics article *Comparison Between the Four General Products*
  (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the
  units, the monoids and the derived operation.
- Mathematics article *The Four Pairings of the Biquaternion Algebra*
  (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms, their Gram
  matrices and their signatures.
- Mathematics article *The Four General Products and Their Two Slots: the Two Algebras and the Two
  Sesqualgebras*
  (`articles_maths/the-four-general-products-and-their-two-slots-the-two-algebras-and-the-two-sesqualgebras.md`),
  for the slot construction stated and proved in general, with the two theorems that the second slot
  decides the composition and the first the form, and the second instance on $M_2(\mathbb{C})$.
- Mathematics article *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*
  (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the
  sign of the square on the two sectors, $\tilde Q\star\tilde Q=\pm N(\tilde Q)e_0$.
- Companion article *The Ordinary Product and the Material Sector*, for the form $B$ alone on the six
  subspaces.
- Companion articles *The Interval as the Square and the Charge of the Material Composition*, *Mass, Rank and the Positivity of the Dagger* and *The Fourth Product and Its Indefinite Metric*, for $N$, $H$ and $K$ on the six subspaces, and for the interval identity and the physical
  reading of the quaternionic product.
- Companion article *The Mathematical Study of Biquaternions*, whose Algebra block this article
  accompanies and whose entries carry the mathematics menu.
