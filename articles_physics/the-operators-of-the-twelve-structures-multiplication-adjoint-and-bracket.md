# __The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket__

## Introduction

The twelve structures of the biquaternion complex space are twelve products on one vector space, and each of them is used physically through the maps it attaches to its own elements (*The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *The 12 Products of the Biquaternion Complex Space*). This article reads those maps for the twelve together. It is the crossing reader of the twelve bands of the menu: each product, each part, and the physical job of the band are owned by the band article, and nothing of the products themselves is re-derived here.

An element becomes an operator through its multiplication, and the multiplication of a product attaches two maps to one element,

$$
L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X,
\qquad
R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A ,
$$

the **left** and the **right multiplication** of the product $\star$. The pair is the operator data of the product, and the two-sided operator of a row is the composite of a left and a right multiplication; for the plain product the sandwich $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{*}}$ is the congruence $\tilde X\mapsto\tilde A\tilde X\tilde A^{*}$. This article treats the two families and the two structures they carry: the **adjoint** for the form of the row, which defines the self-adjoint, skew-adjoint and unitary operators, and the **bracket** or **derivation** of the antisymmetric row. The element read as an operator on the spinor module, the congruence $\mathrm{H}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$, and the polar word are *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*, *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions* and *The Twisted Spinor Operator Representation of Biquaternions*; the same operator written in the four coefficients is *The Four-Vector Operator Representation of Biquaternions* (mathematics). What is added here is the reading of the twelve multiplications side by side.

Three questions organise the article, and they are its three sections. The first is the **parity** of the operator: the bilinear rows give $\mathbb{C}$-linear operators on both sides, the sesquilinear rows give a conjugate-linear left family beside a $\mathbb{C}$-linear right family, and the parity is decided by which slot of the product carries the conjugation. The second is **composition**: the operators of a product compose exactly when the product is associative, so only the general plain row has an operator algebra with a unit, and each other row has a named replacement. The third is the **form**: the adjoint of an operator is taken with respect to the form the row carries, and the self-adjoint, the skew-adjoint and the unitary operators are the observables, the generators and the isometries of the frame.

**Boundaries.** The two operators of the general plain product and their commuting product are *One-Sided Operators on the General Plain Algebra of Biquaternions* and *Two-Sided Operators on the General Plain Algebra of Biquaternions* (mathematics), read physically in *Observables, Gauge Generators and the Chirality of the Internal Action*; the sandwich and its congruence form are *Biquaternion Rotations and Lorentz Transformations* (mathematics) and *The Sandwich Action in Subspaces*; the acting monoid and the dictionary of process and state are *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; the comparison of the four general products is *The Four General Products and Their Physical Readings*; the positive reading of the failures is *A Higher Structure for the Jacobi Failure*. The product of each band and its reading are the band articles listed in the sections below, and the operator theory of each row in the mathematics corpus is owned by the operator articles of the twelve blocks, cited in place. The general entry point, the ambient space of every operator and the ladder of its subspaces and groups, is the mathematics article *The Operators on an Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with complex coefficients $Q_\mu$ and $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation ${}^{\natural}$ fixes $i$ and negates $e_1,e_2,e_3$; the coefficientwise conjugation $\bar{\cdot}$ conjugates the four coefficients; the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, so that $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The scalar part is $\mathrm{Sc}(\tilde X)=X_0$ and the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the sectors $\mathbb{M}_{\pm}$, and the real-quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$. The twelve products are written with the marks of the corpus: the general plain bilinear $\tilde P\tilde Q$ (GPA), the symmetric plain $\tilde P\bullet\tilde Q$ (SPA), the antisymmetric plain $\tilde P\wedge\tilde Q$ (APA), the general quaternionic bilinear $\tilde P^{\natural}\tilde Q$ (GQA), the symmetric quaternionic $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ (SQA), the antisymmetric quaternionic $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ (AQA), the general plain sesquilinear $\tilde P\tilde Q^{*}$ (GPS), the symmetric plain sesquilinear $\tfrac12(\tilde P\tilde Q^{*}+(\tilde P\tilde Q^{*})^{\natural})$ (SPS), the antisymmetric plain sesquilinear $\tfrac12(\tilde P\tilde Q^{*}-(\tilde P\tilde Q^{*})^{\natural})$ (APS), the general quaternionic sesquilinear $\tilde P^{\natural}\tilde Q^{*}$ (GQS), the symmetric quaternionic sesquilinear $\tilde P\bullet\tilde Q$ of the gauge band (SQS), and the antisymmetric quaternionic sesquilinear $\tilde P\diamond\tilde Q$ (AQS). The bracket $\tilde P\wedge\tilde Q$ of the plain row is the cross product $\mathbf P\times\mathbf Q$, and the derivations of a product are the linear maps obeying the Leibniz rule for it. All conventions are those of *Conventions in the Biquaternion Universe*.

## The Operator of a Product and Its Parity

**Definition (the multiplication operators).** Let $\star$ be one of the twelve products. For a fixed element $\tilde A$ the **left multiplication** and the **right multiplication** of the block are the maps

$$
L^{\star}_{\tilde A}\colon \mathbb{B}\to\mathbb{B},\quad L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X ,
\qquad
R^{\star}_{\tilde A}\colon \mathbb{B}\to\mathbb{B},\quad R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A .
$$

Both assignments are additive in the parameter, and both are injective for a nonzero parameter **except on the centre of the two rows that kill the centre in the first slot**: the left multiplication of the plain bracket is $L^{\wedge}_{\lambda e_0}=0$, and that of the antisymmetric quaternionic sesquilinear row is $L^{\diamond}_{\lambda e_0}=0$. What the families are **not** is a single kind of map: the parity of each family is fixed by the slot of the product in which the parameter and the argument sit, and the sesquilinear rows put the conjugation in the second slot.

**Proposition (the parity of the two families).** For the six bilinear rows the product is $\mathbb{C}$-linear in both slots, so $L^{\star}_{\tilde A}$ and $R^{\star}_{\tilde A}$ are $\mathbb{C}$-linear. For the six sesquilinear rows the product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, so the **left** multiplication $L^{\star}_{\tilde A}$ is conjugate-linear and the **right** multiplication $R^{\star}_{\tilde A}$ is $\mathbb{C}$-linear: the argument occupies the second slot on the left and the first slot on the right. The parity of a family is read at a parameter on which it does not vanish; for the two rows that kill the centre in the first slot this means a non-central parameter.

| structure | product $\star$ | $L^{\star}_{\tilde A}$ | $R^{\star}_{\tilde A}$ | real rank of $L^{\star}_{e_1+e_2}$ |
|---|---|---|---|---|
| GPA | $\tilde P\tilde Q$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | $8$ |
| SPA | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | $4$ |
| APA | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | $4$ |
| GQA | $\tilde P^{\natural}\tilde Q$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | $8$ |
| SQA | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | $2$ |
| AQA | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | $6$ |
| GPS | $\tilde P\tilde Q^{*}$ | conjugate-linear | $\mathbb{C}$-linear | $8$ |
| SPS | $\tfrac12(\tilde P\tilde Q^{*}+(\tilde P\tilde Q^{*})^{\natural})$ | conjugate-linear | $\mathbb{C}$-linear | $2$ |
| APS | $\tfrac12(\tilde P\tilde Q^{*}-(\tilde P\tilde Q^{*})^{\natural})$ | conjugate-linear | $\mathbb{C}$-linear | $6$ |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | conjugate-linear | $\mathbb{C}$-linear | $8$ |
| SQS | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ | conjugate-linear | $\mathbb{C}$-linear | $4$ |
| AQS | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})$ | conjugate-linear | $\mathbb{C}$-linear | $4$ |

The rank column is the real rank of the real-linear operator on the eight-dimensional real space, at the element $e_1+e_2$ of biquaternion norm $2$; the rank at a general parameter, its dependence on the scalar part and the norm, and the kernels are the theorems of the operator articles of the blocks, cited below. Read down the column, the ranks are the shadow of the image of each product: the four general rows act at a unit by operators of full rank, the two central-valued symmetric rows collapse onto the centre, the two algebra-valued symmetric rows map onto a two-dimensional image, and the four antisymmetric rows act through the vector subspace.

Two readings follow. The first is that **the parity belongs to the slot and not to the element**: the same element acts by a $\mathbb{C}$-linear map on the right of a sesquilinear row and by a conjugate-linear map on the left, and this is the operator form of the statement that the two slots of a sesquilinear product are not interchangeable. The second is that the conjugate-linear left family is the reason the sesquilinear rows have no ordinary operator calculus: a conjugate-linear map is not an element of the complex endomorphism algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and the assignment $\tilde A\mapsto L^{\star}_{\tilde A}$ is conjugate-linear rather than linear (*The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, mathematics).

## Which Products Compose Their Operators

**Definition (multiplicativity and the operator algebra).** The left family of a row is **multiplicative** when

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}=L^{\star}_{\tilde A\star\tilde B}
\qquad\text{for all } \tilde A,\tilde B ,
$$

that is, when the assignment $\tilde A\mapsto L^{\star}_{\tilde A}$ is a representation of the product. The algebra generated by the two families inside the endomorphism algebra of the underlying vector space is the **multiplication algebra** of the block, and the **enveloping operator algebra** is the special case in which the two families together generate every linear operator. The associativity of the product is exactly the multiplicativity of its left regular representation, and this single fact divides the twelve.

### The Associative Row: the Operator Algebra of the General Plain Product

The general plain product is the only one of the twelve that is associative with a two-sided unit, and it is the only one whose two families together form an operator algebra in the full sense. For all $\tilde A,\tilde B$,

$$
L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B},
\qquad
R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A},
\qquad
L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A},
$$

the first two laws being associativity and the third being associativity with no commutativity. The left and the right multiplications are two commuting copies of the algebra and of its opposite inside one endomorphism algebra, and they are of the **same** algebraic type; the sandwiches span the whole algebra of $\mathbb{C}$-linear operators,

$$
\operatorname{span}_{\mathbb{C}}\{L_{\tilde A}R_{\tilde B}\}=\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

so that the biquaternion algebra is a **bi-module** over the pair and the multiplication algebra is the whole endomorphism algebra. The algebra in which the pair of actions lives is the **enveloping operator algebra** $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ with the sandwich action, and it is *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure* (mathematics). The law $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ is the operator form of the associativity of the material composition, and the reading is the one of *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*: the process is the map, and the maps compose.

The associativity of the product is a **luxury of this row alone**. The other eleven rows are non-associative, and they lose the multiplicativity with it; what each keeps is the subject of the rest of this section. The point is worth stating plainly, because the operator layer of the eleven is not a failed copy of the one of the general plain row: the operators exist, their adjoints exist, their derivations and their brackets exist, and only the algebra that glues the left family to the right family is absent.

### The Quaternionic Row: the Opposite Monoid

The quaternionic product $\tilde P^{\natural}\tilde Q$ is not associative, and its left multiplication is nevertheless multiplicative, with the order reversed:

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}=L^{\star}_{\tilde B\tilde A},
\qquad
L^{\star}_{e_0}=\mathrm{id} ,
$$

because the natural conjugation is a $\mathbb{C}$-linear anti-automorphism and the left multiplication reads its parameter through it. The left family is therefore a **monoid anti-isomorphic to the multiplicative monoid of the plain product**, and not a representation of the quaternionic product; the law is *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (mathematics). The product itself has a left unit and no right unit — $e_0^{\natural}\tilde Q=\tilde Q$ while $\tilde Q^{\natural}e_0=\tilde Q^{\natural}$ — so the row has no two-sided unit and no bi-module, and it is the operator monoid, and not the product, that composes. This is the reading of *Why the Material Composition Is Oriented and Cannot Measure*: the operations compose associatively although the product does not, and the physical evolution is that monoid while the product carries the orientation and the interval. The interval as the square of the composition is *The Interval as the Square and the Charge of the Material Composition*.

### The General Sesquilinear Row: the Sandwich as the Composite

For the general plain sesquilinear product the left multiplication is conjugate-linear and the composite of two left multiplications is $\mathbb{C}$-linear and is not a left multiplication:

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}(\tilde X)=\tilde A\tilde X\tilde B^{*},
$$

the two-sided operator of the row with two independent parameters. The right family, by contrast, is multiplicative with respect to the plain product, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=R^{\star}_{\tilde A\tilde B}$, because the right multiplication reads its parameter through the star and the star is an anti-automorphism. A family of one parity cannot multiply into a family of the same parity, so the row has **no single representation**: what it has instead is the sandwich, which is the composite of the two parities. The operator theory is *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (mathematics), and the physics of the row is the probability band, *Mass, Rank and the Positivity of the Dagger*, *Observables, Gauge Generators and the Chirality of the Internal Action* and *Particle Types, Discrete Charge and Three-Particle Couplings*.

### The Symmetric Rows: Central Values and Algebra Values

The four symmetric rows split into two pairs by the value they return, and the split is visible on the operators.

The **two central-valued rows** are the symmetric quaternionic row (SQA) and the symmetric plain sesquilinear row (SPS). Their values lie in the centre $\mathbb{C}_{\mathbb{B}}e_0$, and their multiplication operators are operators of **rank one** with the centre as their whole image. For the symmetric quaternionic product the composition law is

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B}=A_0\,L^{\star}_{\tilde B},
$$

the family having complex dimension four; for the symmetric plain sesquilinear product every nonzero operator has image the centre and kernel the hyperplane $H(\tilde A,\cdot\,)=0$. A rank-one family whose composition is a scalar multiple of one member is the operator form of the centrality of the value: the operators see the centre alone, they carry no direction, and the family composes like the scalars it computes. The laws are *The Multiplication Operators of the Symmetric Quaternionic Algebra* and *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (mathematics).

The **two algebra-valued rows** are the symmetric plain row (SPA), the symmetrised material composition, and the symmetric quaternionic sesquilinear row (SQS), the gauge pairing. Their values stay in the algebra or in no one of the remarkable subspaces, and their operators are **not** rank one: the symmetrised material operator has a two-dimensional complex image, and the gauge-pairing operator a two-dimensional one carrying a vector part. Neither family is multiplicative, and for the symmetrised row the failure is the operator form of the failure of associativity, the symmetrised product being a Jordan and not an associative algebra: $L^{\bullet}_{\tilde A}=\tfrac12(L_{\tilde A}+R_{\tilde A})$ and $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}\neq L^{\bullet}_{\tilde A\bullet\tilde B}$, while the Jordan identity survives on the operators (*The Multiplication Operators of the Symmetric Plain Algebra*, mathematics). The physical readings are the commutativity band *Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition* and *The Symmetrised Material Composition and the Jordan Identity*; the coupling band *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations* and *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*; the positivity band *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* and *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*; and the metric band *The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product* and *Values in No Subspace: Why the Symmetric Gauge Product Is Not a State*.

### The Antisymmetric Rows: the Operators Are a Bracket

The two antisymmetric bilinear rows are brackets, so their operators are the adjoint maps, and they are read as Lie data rather than as a representation. For the plain bracket the left multiplication is the adjoint up to the factor of two,

$$
L^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A},
\qquad
[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}]=L^{\wedge}_{\tilde A\wedge\tilde B}=\tfrac12\,L^{\wedge}_{[\tilde A,\tilde B]} ,
$$

so the operators close on the bracket and the adjoint representation is a representation in the strict sense; the two commutators of the corpus differ by the doubling of the bracket, $[\tilde A,\tilde B]=2(\tilde A\wedge\tilde B)$, and the operator law carries the same halving. The theory is *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (mathematics), and its physics is *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity* and *Angular Momentum and the Lie Algebra of the Material Sector*. For the quaternionic bracket the commutator of two operators deviates from the operator of the value by the **operator form of the Jacobi failure**,

$$
[L_{\tilde A},L_{\tilde B}]=L_{\tilde A\diamond\tilde B}+D(\tilde A,\tilde B),
$$

and the operators and their pairwise products span a proper subalgebra of the full endomorphism algebra rather than the whole of it; the theory is *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (mathematics), and its physics is the obstruction band, *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator* and *Boosts, Mixed Terms and the Missing Lie Structure*.

The two antisymmetric **sesquilinear** rows are the sharpest case of the parity. Their left multiplications are conjugate-linear, and neither family composes: the composite of two left multiplications is not an operator of the block, so the block has **no monoid of one-sided operators and no regular representation**. The plain one sends $\tilde X$ to the vector part of the product with its conjugate, $\operatorname{Vect}(\tilde A\tilde X^{*})$, of real rank six for a unit and four for a zero divisor; the quaternionic one is the cross product with the conjugate, $L^{\diamond}_{\tilde A}(\tilde X)=\mathbf A\times\overline{\mathbf X}$, of real rank four, killing the centre and with image in the vector subspace. The operator calculus is unavailable, and what is computed in its place is the rank, the kernel, the adjoint and the derivations; the theory is *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* and *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* (mathematics), and the physics is the phase band, *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product* and *Interference without a Lie Algebra: the Jacobi Failure in the State Space*, and the polarisation band, *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product* and *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure*.

## The Adjoint and the Form of the Row

**Definition (the adjoint and its three classes).** Each row of the table carries a form, fixed by its two conjugations, and the **adjoint** of a $\mathbb{C}$-linear operator $T$ with respect to a form $g$ is the operator $T^{\dagger}$ with $g(T\tilde X,\tilde Y)=g(\tilde X,T^{\dagger}\tilde Y)$; for a conjugate-linear operator the relation carries the conjugate, and the adjoint is conjugate-linear again. The adjoint defines three classes of operators, and they are the three physical kinds: the **self-adjoint** $T^{\dagger}=T$, the **skew-adjoint** $T^{\dagger}=-T$, and the **unitary** $T^{\dagger}T=\mathrm{id}$, read in the frame as the observable, the generator and the isometry.

The three classes are not equally populated by the twelve rows, and the reason is the definiteness of the form. The general plain row and the quaternionic row carry non-degenerate but indefinite forms; the plain sesquilinear row carries the **positive definite** form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ of the probability band; the quaternionic sesquilinear row carries the **indefinite Krein form** $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ of the gauge band. Positivity is what makes the adjoint classes a state structure, and the two indefinite rows keep the classes but lose the cone; the distinction between the two is the subject of *Why the Fourth Product Is a Gauge Structure and Not a State Space*, and the absent cone of the gauge metric is *The States the Indefinite Metric Cannot Normalise*.

The adjoint computed on the operators gives the physical dictionary of the corpus. On the plain row a left multiplication by a **Hermitian** element is self-adjoint and is read as an **observable**, a left multiplication by an **anti-Hermitian** element is skew-adjoint and is read as a **gauge generator**, and their exponentials are the internal unitaries; the sandwich $\Theta_{\tilde Q}$ is self-adjoint for Hermitian and for anti-Hermitian $\tilde Q$ and is **never** skew-adjoint, so the one-sided multiplication and not the sandwich is the operator algebra of the observables. The dictionary is *Observables, Gauge Generators and the Chirality of the Internal Action*, with the positivity of the dagger in *Mass, Rank and the Positivity of the Dagger* and the isometry group in *Biquaternion Rotations and Lorentz Transformations*. Two negative facts complete the picture, and both are the operator expression of a parity. For the symmetric plain sesquilinear row the adjoint of a left multiplication is **not a multiplication** of the block at all, because the conjugate-linearity of the operator and the conjugate-linearity of the form cannot be matched by a multiplication of the row (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*, mathematics). For the antisymmetric quaternionic sesquilinear row the adjoint of the left multiplication with respect to the Krein form is the **negative of the operator itself**, the class of a conjugate-linear operator whose adjoint is in its own span (*The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, mathematics). In both cases the adjoint exists, and the point is that it does not stay inside the operator family it came from.

## The Bracket and the Derivation

**Definition (derivation).** A linear map $\delta$ is a **derivation** of a product $\star$ when $\delta(\tilde P\star\tilde Q)=\delta\tilde P\star\tilde Q+\tilde P\star\delta\tilde Q$, and a derivation is **inner** when it is an adjoint of the bracket, $\delta=\operatorname{ad}^{\wedge}_{\tilde A}=\tilde A\wedge\cdot$. The derivations of a block are its infinitesimal automorphisms, and they are the Lie algebra of its structure group; the general theory is *The Operators on an Algebra* (mathematics).

The four antisymmetric rows distribute the derivations in four different ways, and the split is the sharpest single measurement of what each bracket is. The plain bracket closes, and its **inner** derivations are the maps $\operatorname{ad}^{\wedge}_{\tilde C}$ over the trace-zero elements, of complex dimension three, isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, with one **outer** derivation, the dilation of the centre, so that the derivation algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ of complex dimension four; the operator law $L^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A}$ identifies the inner ones with the operators of the row (*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, mathematics). The quaternionic bracket has **no nonzero inner derivation**, so all of its derivations are outer, and they are the three-dimensional algebra of skew maps of the vector subspace; its automorphism group is the group preserving the cross product and fixing the identity (*The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, mathematics). The antisymmetric plain sesquilinear bracket has derivations that are the products $D_{\mathbf a}(\tilde X)=[0,\mathbf a\times\tilde{\mathbf X}]$ with $\mathbf a$ real, a three-dimensional **real** Lie algebra isomorphic to $\mathbb{R}^{3}$ with the cross product, and its structure group contains the coefficient conjugation but not the natural one (*The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, mathematics). The antisymmetric quaternionic sesquilinear bracket has the largest derivation algebra, of real dimension seven, the direct sum of the $\mathbb{R}$-linear endomorphisms of the centre and of $\mathfrak{so}(3,\mathbb{R})$ (*The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, mathematics).

The physical reading of the four is the corpus's ledger of closure and obstruction. The plain bracket is the rotation algebra of the material sector, with the Killing form $\kappa(\tilde P,\tilde Q)=-2\,\mathbf P\cdot\mathbf Q$ and the angular momentum of *Angular Momentum and the Lie Algebra of the Material Sector*; the quaternionic bracket is the obstruction of *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator* and *Boosts, Mixed Terms and the Missing Lie Structure*, whose failure is the boost phenomenon and the non-invariance of the trace form; the state-space bracket is the interference of *Interference without a Lie Algebra: the Jacobi Failure in the State Space*; and the gauge bracket is the complex witness of *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure*. The positive reading that unites the three failures and the associativity failure as the first layers of one higher structure is *A Higher Structure for the Jacobi Failure*, and it closes the twelve bands.

## The Operator Content of the Twelve

The table collects the operator data of the twelve rows. Each entry is read down the columns as one sentence: what the product is, which parity its left multiplication has, whether the left family represents the product, what the adjoint and the bracket give, and which band of the menu owns the physics.

| structure | job | $L$ parity | $L^{\star}_{\tilde A}L^{\star}_{\tilde B}$ | operator content |
|---|---|---|---|---|
| GPA | composition | $\mathbb{C}$-linear | $L^{\star}_{\tilde A\star\tilde B}$ | operator algebra, bi-module, enveloping algebra |
| SPA | commutativity | $\mathbb{C}$-linear | not multiplicative | Jordan operators, inner derivations, $\mathfrak{sl}(2,\mathbb{C})$ |
| APA | rotation | $\mathbb{C}$-linear | not multiplicative | adjoint representation, bracket closes |
| GQA | causality | $\mathbb{C}$-linear | $L^{\star}_{\tilde B\tilde A}$ | opposite monoid, no two-sided unit |
| SQA | coupling | $\mathbb{C}$-linear | $A_0L^{\star}_{\tilde B}$ | rank one, image the centre |
| AQA | obstruction | $\mathbb{C}$-linear | not multiplicative | commutator deviation, outer derivations |
| GPS | probability | conjugate-linear | the sandwich | positive form, observable and generator |
| SPS | positivity | conjugate-linear | not a multiplication (rank one) | image the centre, adjoint not a multiplication |
| APS | phase | conjugate-linear | not an operator of the row | rank six, real structure group |
| GQS | gauge | conjugate-linear | the sandwich $\tilde A^{\natural}\tilde X\overline{\tilde B}$ | indefinite Krein form, isometry group $U(1,3)$ |
| SQS | metric | conjugate-linear | not multiplicative | values in no subspace, Krein form as scalar part |
| AQS | polarisation | conjugate-linear | no operator calculus | conjugate-alternating, derivations of dimension seven |

## The Reading

One statement organises the twelve, and it is the reason the article is written as a crossing and not as one more band. **The operators are defined for every product, and the operator algebra is the luxury of the associative unital one.** A product always attaches its two multiplications to its elements; the adjoint for the form of the row always defines the observables, the generators and the isometries; the antisymmetric row always defines a bracket and a derivation algebra. What only the general plain product supplies is the composition of the two families into one algebra with a unit, and with it the bi-module, the envelope and the universal property. The general quaternionic row keeps a monoid and loses the unit on one side; the general sesquilinear row keeps the sandwich and loses the single representation; the central-valued symmetric rows keep a rank-one family that composes like a scalar, and the algebra-valued symmetric rows keep only a family that is not multiplicative; the antisymmetric rows keep a bracket, closed for the plain row and obstructed for the other three.

Read physically, the twelve operators are the twelve ways one element of the frame can act on another, and the columns of the table above are the twelve physical jobs. The composition row is the process, and its operator algebra is what lets two processes be composed in a single algebra; the commutativity row is the symmetrised composition, whose operators are the Jordan operators of the classical observables; the rotation row is the angular momentum and the adjoint representation; the causality row is the interval and the oriented composition whose operators compose and whose product does not; the coupling row is the comparison that returns a number and no direction; the obstruction row is the bracket that fails to close; the probability row is the positive form on which the observables and the generators are read; the positivity row is the probability value as a rank-one product; the phase row is the interference term; the gauge row is the indefinite metric whose operators compose through the sandwich; the metric row is the gauge pairing; and the polarisation row is the self-helicity of one element. Each row's operators are read in its own band, and the crossing reading of this article is the single ladder that orders them.

## Summary

Every one of the twelve products of the biquaternion complex space attaches to an element $\tilde A$ the **left** multiplication $L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X$ and the **right** multiplication $R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A$. The **parity** of the two families is decided by the slot: the six bilinear rows give $\mathbb{C}$-linear operators on both sides, and the six sesquilinear rows give a **conjugate-linear** left family beside a $\mathbb{C}$-linear right family, because the product is conjugate-linear in the second slot and the left multiplication places the argument there. The **composition** of the operators is the associativity of the product read on the operators, and it divides the twelve: the general plain row alone is associative with a two-sided unit, and it alone has an operator algebra with a unit, the **enveloping operator algebra** $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, a faithful action that exhausts the linear operators and makes the algebra a **bi-module**; the general quaternionic row has the left family a **monoid anti-isomorphic** to the plain multiplicative monoid, $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=L^{\star}_{\tilde B\tilde A}$, with no two-sided unit; the general sesquilinear row has the composite of two conjugate-linear left multiplications equal to the **sandwich** and no single representation; the two central-valued symmetric rows have rank-one families that compose like scalars, $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$ for the quaternionic one, while the two algebra-valued symmetric rows have families that are not multiplicative; and the two antisymmetric bilinear rows have their operators equal to the adjoint maps, closing on the bracket for the plain row and deviating by the **Jacobi defect** for the quaternionic one, while the two antisymmetric sesquilinear rows are conjugate-linear with no operator calculus at all. The **adjoint** for the form of the row defines the self-adjoint, skew-adjoint and unitary operators, read as the observable, the generator and the isometry; the plain sesquilinear row is the positive one whose classes are the state structure, the quaternionic sesquilinear row is the indefinite Krein metric whose positivity is absent, and the adjoint of a multiplication can leave the family it came from, as it does for the symmetric plain sesquilinear row, or return the negative of the operator, as it does for the antisymmetric quaternionic sesquilinear one. The **derivations** of the antisymmetric rows have inner part of dimension three in $\mathfrak{sl}(2,\mathbb{C})$ for the plain row, with one outer derivation, the dilation of the centre, so that the derivation algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$; are all outer of dimension three for the quaternionic row; form a real three-dimensional cross-product algebra for the antisymmetric plain sesquilinear row; and are of real dimension seven, the centre's endomorphisms direct sum $\mathfrak{so}(3,\mathbb{R})$, for the antisymmetric quaternionic sesquilinear row. The single organising statement is that **the operators are defined for every product and the operator algebra is the luxury of the associative unital one**: the eleven non-associative rows keep their multiplications, their adjoints, their derivations and their brackets, and lose only the algebra that glues the left family to the right.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\star$ | one of the twelve products; its code names the row |
| $L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X$ | left multiplication of the row |
| $R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A$ | right multiplication of the row |
| $L^{\wedge}_{\tilde A}=\tilde A\wedge\cdot$, $L^{\diamond}_{\tilde A}$ | left multiplications of the two antisymmetric bilinear rows and of the antisymmetric quaternionic sesquilinear one |
| $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{*}}$ | the sandwich of the general plain row, the congruence $\tilde X\mapsto\tilde A\tilde X\tilde A^{*}$ |
| $\mathrm{H}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the sandwich read as an operator on the algebra |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B}=L^{\star}_{\tilde A\star\tilde B}$ | multiplicativity; holds for the general plain row alone |
| $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ | the enveloping operator algebra of the general plain row |
| $\operatorname{ad}^{\wedge}_{\tilde A}=\tilde A\wedge\cdot$ | the adjoint map of a bracket, the inner derivation of the plain row |
| $L^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A}$, $\operatorname{ad}_{\tilde A}=[\tilde A,\cdot\,]$ | the halving that separates the block's adjoint from the commutator adjoint |
| $T^{\dagger}$ | the adjoint of an operator for the form of the row |
| $H(\tilde P,\tilde Q)=\sum_\mu P_\mu\overline{Q_\mu}$ | the positive form of the probability row |
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the indefinite Krein form of the gauge row |
| GPA, SPA, APA, GQA, SQA, AQA | the six bilinear rows, of $\mathbb{C}$-linear operators |
| GPS, SPS, APS, GQS, SQS, AQS | the six sesquilinear rows, of conjugate-linear left operators |

## Further Reading

- *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*, *The Four-Vector Operator Representation of Biquaternions*, *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions* and *The Twisted Spinor Operator Representation of Biquaternions*, for the element as an operator through the sandwich and the acting monoid.
- *Observables, Gauge Generators and the Chirality of the Internal Action*, for the one-sided and two-sided operators read physically, and *Biquaternion Rotations and Lorentz Transformations* with *The Sandwich Action in Subspaces*, for the isometry and the sandwich restricted to the remarkable subspaces.
- The band articles of the twelve: *The Ordinary Product and the Material Sector*, *The Symmetrised Material Composition and the Jordan Identity*, *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*, *Angular Momentum and the Lie Algebra of the Material Sector*, *The Interval as the Square and the Charge of the Material Composition*, *Why the Material Composition Is Oriented and Cannot Measure*, *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations*, *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*, *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator*, *Boosts, Mixed Terms and the Missing Lie Structure*, *Mass, Rank and the Positivity of the Dagger*, *Particle Types, Discrete Charge and Three-Particle Couplings*, *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*, *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*, *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*, *Interference without a Lie Algebra: the Jacobi Failure in the State Space*, *The Fourth Product and Its Indefinite Metric*, *The States the Indefinite Metric Cannot Normalise*, *Why the Fourth Product Is a Gauge Structure and Not a State Space*, *The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product*, *Values in No Subspace: Why the Symmetric Gauge Product Is Not a State*, *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*, *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure* and *A Higher Structure for the Jacobi Failure*.
- *The Four General Products and Their Physical Readings*, for the transversal comparison of the four products that this article crosses with the operators.
- The mathematics: *The Operators on an Algebra*, *The 12 Products of the Biquaternion Complex Space*, *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, *One-Sided Operators on the General Plain Algebra of Biquaternions*, *Two-Sided Operators on the General Plain Algebra of Biquaternions*, *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, *The Multiplication Operators of the Symmetric Plain Algebra*, *The Multiplication Operators of the Symmetric Quaternionic Algebra*, *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, *The Multiplication Operators of the Symmetric Plain Sesqualgebra*, *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*, *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* and *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*.
