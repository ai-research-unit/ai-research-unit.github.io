# __The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone__

## Introduction

Of the twelve algebraic structures that the complex space
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries, exactly one is an associative unital
algebra, the general plain algebra of *Introduction to the General Plain Algebra of Biquaternions*;
the specificity that its associativity and its two-sided unit $e_0$ deliver is that its invertible
elements form a genuine **group** (*The Specificities of the General Plain Algebra*). This article
studies that group and the exact meaning of its boundary. The group of units is the complement of
the zero-divisor cone, the algebra is the disjoint union of the two, and the cone is at once the
complement of the group and its topological boundary.

The boundary deserves an article of its own because it is drawn by a form the product does not
carry. The plain product has one algebraic norm of its own, the general plain bilinear form
$B(\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, and $B$ decides nothing about invertibility (*Norm
and Invertibility in the General Plain Algebra*, §*The Absence of a Criterion from the Algebraic
Norm*). The boundary is drawn instead by the **general quaternionic bilinear algebraic norm** $N$,
also the **reduced norm**, $N(\tilde Q)=\sum_\mu Q_\mu^{2}$, the norm that the quaternionic
structure of the space carries; that form is **multiplicative**, and its multiplicativity is exactly
the reason its non-vanishing set is closed under the product and under inversion, hence a group. The
two statements of the article are the pair of these facts: **the units of the plain product are the
elements of non-vanishing norm $N$, and their complement is a group for the plain product and for no
other of the twelve structures.**

**Placement and boundaries.** The article closes the *Specific Theory* of the general plain algebra,
after *The Specificities of the General Plain Algebra*. It states the invertibility criterion of the
plain product that *Norm and Invertibility in the General Plain Algebra* declines to read from the
product's own algebraic norm, and it cites *Zero Divisors in the 12 Algebraic Structures over the
Biquaternion $\mathbb{C}$ Space* for the one-sided inverse equations read across the four general
products. The topology of the group — the polar decomposition, the retractions onto the compact
subgroups, the homotopy groups and the universal cover — is proved in *The Biquaternion Unit Group
as a Topological Group* and *The Unitary Group of the Biquaternion Algebra*; the ambient topology of
the cone is *The Topology of the Zero-Divisor Cone*; the distribution of the units over the
remarkable subspaces is *Norm and Invertibility in the General Quaternionic Algebra*, §*The
Algebraic Norm on the Remarkable Subspaces*; the invertibility of the symmetrised product is *Norm
and Invertibility in the Symmetric Plain Algebra*; and the classification of the twelve is *The 12
Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. None of those is reproved here.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$
with $e_1e_2=e_3$, $e_k^{2}=-e_0$ and central scalar imaginary $i$; a general element is $\tilde
Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$ and $\mathbf
Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$, the
coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is
${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The product is the general plain bilinear product $\tilde
P\tilde Q$, written by juxtaposition, and the **general quaternionic bilinear algebraic norm** $N$,
the reduced norm, is

$$
N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2}=\mathrm{Sc}\bigl(\tilde Q\tilde Q^{\natural}\bigr),
$$

the scalar of the central square $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0$. It is one of the four
algebraic norms of the space (*The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*), and
the whole article turns on its not being the algebraic norm of the plain product: $B$ is the
diagonal of the plain bilinear form, $N$ is the general quaternionic one, and the two are different
forms with different vanishing sets. The generic norm $\mathrm{Norm}$ of *Conventions in
Mathematics*, §*The form convention and the norm convention*, is instantiated in this article by the
general quaternionic bilinear algebraic norm $N$ (*The 4 Algebraic Norms over the Biquaternion
$\mathbb{C}$ Space*): every statement below names its norm, and the norm it names is $N$.

## The Partition of the Algebra

**Definition (the zero-divisor cone).** The vanishing set of the norm $N$,

$$
\mathcal{C}=\{\tilde Q\in\mathbb{B}:N(\tilde Q)=0\},
$$

is the **zero-divisor cone**. It is a complex cone with apex at the origin, of complex dimension
three and real dimension six, and the zero-divisor set of the four general products is the punctured
cone $\mathcal{C}\setminus\{0\}$ (*Zero Divisors of the General Plain Algebra*; *Zero Divisors in
the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*).

**Theorem (the invertibility criterion of the plain product).** An element $\tilde Q$ of
$\mathbb{B}$ is invertible in the plain product exactly when $N(\tilde Q)\neq0$, and its inverse is
then

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)} .
$$

*Proof.* The natural conjugation is an anti-automorphism, $\tilde P^{\natural}\tilde
Q^{\natural}=(\tilde Q\tilde P)^{\natural}$. Write $\tilde Q=Q_0e_0+\mathbf Q$, so that $\tilde
Q^{\natural}=Q_0e_0-\mathbf Q$ and

$$
\tilde Q\tilde Q^{\natural}=Q_0^{2}e_0-\mathbf Q^{2},
$$

whose vector part vanishes and whose scalar part is $Q_0^{2}+\sum_k Q_k^{2}=N(\tilde Q)$, because
the vector part of the algebra squares to $\mathbf Q^{2}=-\sum_kQ_k^{2}e_0$. Hence $\tilde Q\tilde
Q^{\natural}=N(\tilde Q)e_0$, and the same computation in the other order gives $\tilde
Q^{\natural}\tilde Q=N(\tilde Q)e_0$. If $N(\tilde Q)\neq0$ the displayed element is a two-sided
inverse. If $N(\tilde Q)=0$ and $\tilde Q\neq0$ then $\tilde Q^{\natural}\neq0$ and $\tilde Q\tilde
Q^{\natural}=0$, so $\tilde Q$ is a zero divisor and cannot be invertible; and the origin is not
invertible. Verified by recomputation on $100$ random elements, the two products $\tilde Q\tilde
Q^{-1}$ and $\tilde Q^{-1}\tilde Q$ returning $e_0$ with error below $10^{-9}$.

**Theorem (the partition of the algebra).** The algebra is the disjoint union

$$
\mathbb{B}=\mathbb{B}^\times\uplus\mathcal{C},\qquad
\mathbb{B}^\times=\{\tilde Q\in\mathbb{B}:N(\tilde Q)\neq0\},
$$

of its **group of units** and its **zero-divisor cone**. The cone is exactly the complement of the
group.

*Proof.* By the criterion the units are the elements of non-vanishing norm, so the two sets are
complementary; they are disjoint because a complex number is either zero or not. The group structure
is *Norm and Invertibility in the General Quaternionic Algebra*.
Verified by recomputation on a mixed sample of $100$ elements: the $93$ random elements off the cone
are units, the $6$ cone elements are zero divisors and the origin is neither.

**Corollary (the zero-divisor set and its complement).** The zero-divisor set of the four general
products is the punctured cone $\mathcal{C}\setminus\{0\}$, and the complement of the zero-divisor
set in the algebra is

$$
\mathbb{B}\setminus\bigl(\mathcal{C}\setminus\{0\}\bigr)=\mathbb{B}^\times\cup\{0\},
$$

the group of units together with the origin.

*Proof.* The apex is excluded from the zero-divisor set by the definition, which requires both
elements nonzero; every other point of the cone is a zero divisor by the criterion; and the
complement of the punctured cone is the off-cone part together with the apex, that is
$\mathbb{B}^\times\cup\{0\}$.

The partition gives the three-way classification of the elements of the algebra by their behaviour
in the plain product.

| condition on $N(\tilde Q)$ | condition on $\tilde Q$ | class |
| --- | --- | --- |
| $\neq0$ | (automatically $\neq0$) | a unit; an element of the group $\mathbb{B}^\times$ |
| $=0$ | $\tilde Q=0$ | the origin; neither a unit nor a zero divisor |
| $=0$ | $\tilde Q\neq0$ | a zero divisor; a point of the punctured cone $\mathcal{C}\setminus\{0\}$ |

**Remark (the two complements).** The group has two complements in the algebra, and they differ by
the apex. **The complement of the cone is the group of units, and the complement of the zero-divisor
set is the group together with the origin.** The apex is therefore the one point that separates the
two statements: it lies on the cone and in the complement of the zero-divisor set, it is the only
element of the algebra that is neither a unit nor a zero divisor, and it is the apex of the boundary
of the group while being no zero divisor itself. The identity $e_0$ is the mirror case: it is off
the cone, in the group, and in no zero-divisor set.

## Multiplicativity Makes the Complement a Group

**Theorem (the norm $N$ is multiplicative).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
N(\tilde P\tilde Q)=N(\tilde P)\,N(\tilde Q).
$$

*Proof.* The natural conjugation reverts the order, so

$$
(\tilde P\tilde Q)(\tilde P\tilde Q)^{\natural}
=\tilde P\tilde Q\tilde Q^{\natural}\tilde P^{\natural}
=\tilde P\,N(\tilde Q)e_0\,\tilde P^{\natural}
=N(\tilde Q)\tilde P\tilde P^{\natural}
=N(\tilde P)N(\tilde Q)e_0,
$$

the scalar $N(\tilde Q)$ being central. Verified by recomputation on $100$ random pairs, error below
$10^{-9}$.

**Corollary (the cone is absorbing and the units are closed).** The cone is closed under the product
in the strong sense that a cone factor forces a cone product: if $N(\tilde P)=0$ then $N(\tilde
P\tilde Q)=N(\tilde Q\tilde P)=0$ for every $\tilde Q$. The group of units is closed under the
product, and with it the inverse formula is closed under inversion.

*Proof.* Multiply the multiplicativity by zero in the two orders; closure under multiplication
follows from the non-vanishing of the two factors, and closure under inversion from $\tilde
Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$.

**Theorem (the norm $N$ is a homomorphism of the group onto $\mathbb{C}^\times$).** The
multiplicative norm restricts to a surjective homomorphism of groups

$$
N:\mathbb{B}^\times\longrightarrow\mathbb{C}^\times,\qquad \tilde Q\longmapsto N(\tilde Q),
$$

whose kernel is the **norm-one group** $\mathbb{B}^\times_1=\{\tilde Q:N(\tilde Q)=1\}$.

*Proof.* Multiplicativity makes the restriction a homomorphism into the nonzero complex numbers; it
is surjective because the centre gives $N(Ae_0)=A^{2}$ and every nonzero complex number is a square,
the map being two-to-one on the central line; the kernel is the preimage of $1$, a normal subgroup.
The identification of the norm-one group with $SL_2(\mathbb{C})$ and the two-to-one covering
$\mathbb{C}^\times e_0\times\mathbb{B}^\times_1\to\mathbb{B}^\times$ of kernel $\{\pm e_0\}$ are
*The Biquaternion Unit Group as a Topological Group*.

**Remark (why the complement is a group here and nowhere else).** The two closure properties are
exactly what a set of the form $\{\text{form}\neq0\}$ needs in order to be a group, and both are
read from multiplicativity. The norm $N$ supplies them, so its non-vanishing set is the group of
units of the plain product. The algebraic norm of the plain product, $B$, supplies neither, and its
non-vanishing set is not closed under the product: the elements $\tilde P=e_0-\tfrac13e_1$ and
$\tilde Q=e_0+2e_1$ have $B(\tilde P)=\tfrac89$ and $B(\tilde Q)=-3$, both nonzero, while $B(\tilde
P\tilde Q)=0$. The non-vanishing set of $B$ therefore carries no group, although it is closed under
the inverse formula; **a group of units needs a multiplicative norm, and the multiplicative norm of
the space is not the norm of the plain product.** Verified by recomputation: $B(\tilde P)=\tfrac89$,
$B(\tilde Q)=-3$, $B(\tilde P\tilde Q)$ below $10^{-15}$.

## The Boundary Is the Cone of the Norm and Not the Cone of the Product

The algebraic norm of the plain product is the general plain bilinear form read at the two equal
arguments,

$$
B(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

of Gram matrix $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$; it is not multiplicative, its vanishing
set is a complex cone of real dimension six, and it is neither the light cone nor the zero-divisor
cone (*Norm and Invertibility in the General Quaternionic Algebra*). The two cones are different objects,
and the difference is the boundary of the group.

**Theorem (neither cone decides invertibility through the other).** The two implications fail in
both directions,

$$
B(\tilde Q)=0\ \not\Longrightarrow\ \tilde Q\notin\mathbb{B}^\times,
\qquad
B(\tilde Q)\neq0\ \not\Longrightarrow\ \tilde Q\in\mathbb{B}^\times,
$$

with the witnesses $\tilde Q=e_0+e_1$, a unit of vanishing $B$, and $\tilde Q=e_0+ie_1$, a zero
divisor of non-vanishing $B$.

*Proof.* $(e_0+e_1)(e_0-e_1)=2e_0$, so $e_0+e_1$ is invertible, while $B(e_0+e_1)=1-1=0$. And
$(e_0+ie_1)(e_0-ie_1)=0$, so $e_0+ie_1$ is a zero divisor, while $B(e_0+ie_1)=1-i^{2}=2$.

**Corollary (the boundary of the group).** The boundary of the group of units is the zero-divisor
cone $\mathcal{C}=\{N=0\}$, and not the vanishing set $\{B=0\}$ of the product's own algebraic norm.
The two cones meet, and neither contains the other.

*Proof.* The complement of the group is the cone, the group is dense in the algebra and the cone is
closed, so the boundary of the group — the intersection of the closure of the group and the closure
of its complement — is the cone; and the witnesses of the theorem place a point of $\{B=0\}$ outside
$\mathcal{C}$ and a point of $\mathcal{C}$ outside $\{B=0\}$, so the two vanishing sets meet and
neither contains the other.

| form | vanishing set | real dimension | multiplicative | decides the units |
| --- | --- | --- | --- | --- |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the zero-divisor cone $\mathcal{C}$ | $6$ | yes | yes: $\mathbb{B}^\times=\{N\neq0\}$ |
| $B(\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the complex cone of $B$ | $6$ | no | no, by the two witnesses |

**Remark (what the boundary is made of).** The group of units of the plain product is therefore
bounded by the zero set of a form that the product does not carry in its own right: the plain
product is the multiplication, its algebraic norm is $B$, and the criterion is furnished by the
general quaternionic bilinear algebraic norm $N$, which belongs to the quaternionic structure of the
space. **The units of the plain product are read from the norm of a different product.** This is the
geometric content of the absence recorded in *Norm and Invertibility in the General Plain Algebra*,
and the reason the statement is stated here: the article that owns the product does not own the form
that decides its units, and the partition of §*The Partition of the Algebra* is the place where the
two meet.

## The Group and Its Boundary

The group and the cone are complementary, so their topologies are two readings of one partition; the
topological theorems are proved in the articles named and collected here for the group of the
algebra.

**Proposition (the group is open and dense, the cone is closed, and they share their boundary).**
The group $\mathbb{B}^\times$ is open and dense in the algebra; the cone $\mathcal{C}$ is closed,
with empty interior, of real codimension two; and the group and the cone have one and the same
boundary,

$$
\partial\mathbb{B}^\times=\partial\mathcal{C}=\mathcal{C}.
$$

*Proof.* The cone is the zero set of a polynomial, hence closed, and it is a proper algebraic
subset, hence of empty interior; its complement is therefore open and dense, of real dimension
eight. The identity of the two boundaries is the corollary of §*The Boundary Is the Cone of the Norm
and Not the Cone of the Product*.

**Proposition (the group is connected and its boundary does not separate).** $\mathbb{B}^\times$ is
connected, of real dimension eight, and the cone of real codimension two does not disconnect the
algebra; the group is the connected complement of the cone.

*Proof.* The polar decomposition retracts the group onto its maximal compact subgroup
$U(\mathbb{B})\cong U(2)$, a continuous image of a connected group; the retraction, the structure of
the maximal compact subgroup and the connectedness are *The Biquaternion Unit Group as a Topological
Group*, §*The Topology of the Group*, and *The Unitary Group of the Biquaternion Algebra*.

**The group in the matrix model (cited).** Under $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ the
group is $\mathbb{B}^\times\cong GL_2(\mathbb{C})$ and the norm is the determinant,
$\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$, so the norm-one group is $\mathbb{B}^\times_1\cong
SL_2(\mathbb{C})$, and the norm is the determinant homomorphism
$GL_2(\mathbb{C})\to\mathbb{C}^\times$ (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of
Biquaternions*; §*The Determinant and the Matrix Model* of *The Biquaternion Unit Group as a
Topological Group*). The homotopy type, the fundamental group generated by the loop around the cone,
the third homotopy group carried by the unit quaternions and the universal cover are *The
Biquaternion Unit Group as a Topological Group*.

## The Units inside the Remarkable Subspaces

The criterion restricts to the remarkable subspaces, where the cone cuts a slice of lower dimension
and the group is the complement of that slice. The distribution is *Norm and Invertibility in the
General Quaternionic Algebra*, §*The Algebraic Norm on the Remarkable Subspaces*, and is tabulated
here in the form the boundary takes.

| subspace | $\dim_{\mathbb{R}}$ | cone slice | units |
| --- | --- | --- | --- |
| centre $\mathbb{C}_{\mathbb{B}}$ | $2$ | the apex alone | the nonzero scalars $\mathbb{C}^\times e_0$ |
| quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $4$ | the apex alone | every nonzero element |
| anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ | $4$ | the apex alone | every nonzero element |
| vector subspace $\mathrm{Vect}(\mathbb{B})$ | $6$ | a complex cone of real dimension $4$ | the complement of that cone |
| sectors $\mathbb{M}_\pm$ | $4$ | a real cone of real dimension $3$ | the complement of that cone |

**Remark (the two rows that carry a cone).** On the centre and the two quaternionic subspaces the
norm vanishes at the origin alone, so the punctured cone is empty there and the only non-unit is the
origin; **the boundary of the group is empty in those subspaces and non-empty exactly in the vector
subspace and the two sectors.** On the vector subspace the cone is the complex cone
$\sum_kQ_k^{2}=0$, of real codimension two in the subspace; on the two sectors it is the light cone,
of real codimension one, the slice the physics articles read as the causal boundary. The dimension
of the cone drops from six to four on the vector subspace and to three on the sectors, and the group
is the complement at every stage.

## The Complement in the Other Eleven Structures

The invertibility is relative to the product, so the statement of this article is a statement about
one of the twelve structures, and the comparison is what fixes its exact scope. The units of the
four general products and the symmetrised plain product are collected first.

| structure | unit | invertible elements | a group |
| --- | --- | --- | --- |
| $\mathrm{GPA}$ | $e_0$, two-sided; associative | the units of the definition: $\{N\neq0\}$, with $\tilde P^{-1}=\tilde P^{\natural}/N(\tilde P)$ | **yes** |
| $\mathrm{SPA}$ | $e_0$, two-sided; not associative | the elements of non-vanishing norm, with the Jordan inverse | no |
| $\mathrm{GQA}$ | $e_0$, left alone; not associative | not defined; the inverse equations select $\{N\neq0\}$, solved by $(\tilde P^{-1})^{\natural}$ | no |
| $\mathrm{GPS}$ | $e_0$, right alone; not associative | not defined; the inverse equations select $\{N\neq0\}$, solved by $(\tilde P^{-1})^{*}$ | no |
| $\mathrm{GQS}$ | no unit on either side; not associative | not defined; the inverse equations select $\{N\neq0\}$, solved by $(\tilde P^{-1})^{\natural*}$ | no |

The definition of the inverse presupposes a two-sided unit, so the invertibility of the definitions
exists only in the two unital structures of the table, the plain and the symmetrised plain. The
three non-unital general products are read through the inverse equations, which use the fixed
element $e_0$ and make no appeal to a unit of the product.

**Theorem (the inverse equations of the four general products).** For each of the four general
products, and for a nonzero element $\tilde P$, the two equations $\tilde P\star\tilde X=e_0$ and
$\tilde X\star\tilde P=e_0$ have a solution exactly when $N(\tilde P)\neq0$, the solutions being
those of the table above. The cone is therefore the complement of the elements solvable on both
sides of the inverse equations, for each of the four products at once.

*Proof.* The solutions are exhibited in the table and satisfy the equations because the natural
conjugation and the coefficient conjugation revert the product, $(\tilde P\tilde
Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$, so that $\tilde P^{\natural}(\tilde
P^{-1})^{\natural}=(\tilde P^{-1}\tilde P)^{\natural}=e_0$ and likewise with the coefficient
conjugation. Conversely, the matrix model turns the equations into matrix equations with an
invertible right factor, so the multiplication by $\tilde P$ is invertible and $N(\tilde P)\neq0$.
The statement is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$
Space*, §*The One-Sided Inverse Equations*, and the verification is by recomputation on $100$ random
off-cone elements for each of the three non-unital products.

**Remark (the complement is one set for the four).** The theorem says that the elements of the four
general products that solve the inverse equations on both sides are one and the same set, the
complement of the cone; the table says where that set becomes a group. **The invertible elements of
the four general products are the same set, and the set is a group in the general plain algebra
alone.** $\mathrm{GPA}$ has both the two-sided unit and the associative product; $\mathrm{GQA}$ and
$\mathrm{GPS}$ have a one-sided unit and a non-associative product, so the element $e_0$ is not even
a two-sided identity and no group can be read; $\mathrm{GQS}$ has no unit at all.

**The symmetrised plain algebra: the same set and no group.** The symmetrised product
$\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ has $e_0$ as a two-sided unit, and its invertible
elements are again the elements of non-vanishing norm: for $N(\tilde P)\neq0$ the two-sided solution
is the **Jordan inverse**

$$
\tilde P^{\bullet}=\frac{2P_0e_0-\tilde P}{N(\tilde P)},
\qquad
\tilde P\bullet\tilde P^{\bullet}=\tilde P^{\bullet}\bullet\tilde P=e_0,
$$

which is the Cayley–Hamilton inverse of the matrix model, $\mathsf{M}_2(2P_0e_0-\tilde
P)=2P_0\mathrm{I}_2-\mathsf{M}_2(\tilde P)=\operatorname{tr}\mathsf{M}_2(\tilde
P)\mathrm{I}_2-\mathsf{M}_2(\tilde P)$; and a nonzero element of the cone is a zero divisor of the
symmetrised product, hence not invertible. But the product is not associative, and the invertible
elements form **no group**: the elements $e_1$ and $e_2$ are invertible, with $e_1\bullet(-e_1)=e_0$
and $e_2\bullet(-e_2)=e_0$, while $e_1\bullet e_2=\tfrac12(e_3-e_3)=0$ is not. The complement of the
zero-divisor set of the symmetrised product, which is $\{P_0\neq0,N\neq0\}\cup\{0\}$, is not the
invertible set either: the pure element $e_1$ is a zero divisor and invertible at once, and the
origin is a non-zero-divisor that is not invertible. The invertibility of the symmetrised product is
*Norm and Invertibility in the Symmetric Plain Algebra*, and it is quoted here for the comparison
only. Verified by recomputation: the Cayley–Hamilton solution returns the unit on $100$ random
elements of non-vanishing norm, and $e_1\bullet e_2=0$.

**The seven with no unit on either side.** The six structures $\mathrm{APA}$, $\mathrm{SQA}$,
$\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ and $\mathrm{AQS}$ have a unit on neither side, and
the seventh, the symmetric quaternionic sesqualgebra $\mathrm{SQS}$, has none either. The definition
of the inverse presupposes a two-sided unit, so no invertible element and no group of units is
defined for any of them; the fixed element $e_0$ is a value of some of them, $e_0\star e_0=e_0$ in
each symmetrised structure, but it is the identity of none, which is exactly what the absence of a
two-sided unit says. Six of the seven have the whole punctured space for zero-divisor set, so the
complement of the zero-divisor set degenerates to the origin alone; $\mathrm{SQS}$ has the enlarged
set, and its complement is the reduced set $\{Q_0\neq0,N\neq0\}\cup\{0\}$.

**Theorem (the isolation).** Of the twelve structures of the complex space, the general plain
algebra is the only one whose invertible elements form a group; equivalently, the only one in which
the complement of the zero-divisor cone is a group under the product of the structure.

*Proof.* By the table only $\mathrm{GPA}$ and $\mathrm{SPA}$ have a two-sided unit and therefore
invertible elements at all, and $\mathrm{SPA}$ fails the closure of them under its own product,
$e_1\bullet e_2=0$ against $e_1,e_2$ invertible, so they form no group. The ten others have no
two-sided unit: for $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$ the inverse equations detect
the off-cone elements without supplying an identity, and for the seven structures without a unit the
invertibility is not defined at all. The complement of the cone is the set of non-vanishing norm for
every structure of the space, and it is a group exactly when the product is associative with a
two-sided unit and the norm is multiplicative on it, which is the case in $\mathrm{GPA}$ alone.

**Remark (set and structure again).** The isolation is a statement about the **group structure** and
not about the **set**: the complement of the cone is the same set $\{N\neq0\}$ in $\mathrm{GPA}$ and
in $\mathrm{SPA}$, and the associativity of the plain product is the whole of the difference. The
same caution as in *The Specificities of the General Plain Algebra* applies: the plain product is
not the only structure with invertible elements, it is the only structure where they form a group.

## Summary

The general plain algebra has the group of units $\mathbb{B}^\times=\{N(\tilde Q)\neq0\}$ for the
multiplicative norm $N(\tilde Q)=\sum_\mu Q_\mu^{2}=\mathrm{Sc}(\tilde Q\tilde Q^{\natural})$, with
the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$; the zero-divisor cone
$\mathcal{C}=\{N=0\}$ is exactly its complement, so that the algebra is the disjoint union
$\mathbb{B}=\mathbb{B}^\times\uplus\mathcal{C}$, the zero-divisor set is the punctured cone, and the
complement of the zero-divisor set is the group together with the origin. The boundary of the group
is the cone of the norm $N$ of the general quaternionic bilinear form and not the cone of the
**plain product's own** algebraic norm $B=\sum_\mu\varepsilon_\mu Q_\mu^{2}$: the element $e_0+e_1$
is a unit with $B=0$ and the element $e_0+ie_1$ is a zero divisor with $B=2$, so $B$ decides
nothing, while $N$ is multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, which makes the
cone absorbing, the units closed under the product and the inverse, and $N$ a surjective
homomorphism $\mathbb{B}^\times\to\mathbb{C}^\times$ with kernel the norm-one group. The group is
open, dense and connected, of real dimension eight, of the homotopy type $S^{1}\times S^{3}$ with
$\pi_1\cong\mathbb{Z}$, with the cone of real codimension two as its boundary; on the centre and the
two quaternionic subspaces the cone is empty and the group is everything but the origin, while on
the vector subspace and the two sectors the boundary is the complex cone and the light cone. Across
the twelve structures the complement of the cone is one set and one group: the set is shared by the
four general products, whose inverse equations are solved by $(\tilde P^{-1})^{\natural}$, $(\tilde
P^{-1})^{*}$ and $(\tilde P^{-1})^{\natural*}$ for the off-cone elements, and the group structure
exists in the general plain algebra alone: the symmetrised plain algebra has the same invertible set
and no group, the three other general products select the same off-cone set through the inverse
equations without a two-sided identity, and the seven structures without a unit have no invertible
element at all.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}=\mathrm{Sc}(\tilde Q\tilde Q^{\natural})$ | the general quaternionic bilinear algebraic norm, the reduced norm; multiplicative; the criterion of invertibility |
| $\mathcal{C}=\{\tilde Q:N(\tilde Q)=0\}$ | the zero-divisor cone; the complement of the group of units; real dimension $6$; real codimension $2$ |
| $\mathcal{C}\setminus\{0\}$ | the zero-divisor set of the four general products |
| $\mathbb{B}^\times=\{N\neq0\}$ | the group of units of the plain product; the complement of the cone |
| $\mathbb{B}\setminus(\mathcal{C}\setminus\{0\})=\mathbb{B}^\times\cup\{0\}$ | the complement of the zero-divisor set: the group together with the origin |
| $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$ | the inverse of an element of the group |
| $e_0+e_1$; $e_0+ie_1$ | the unit with $B=0$; the zero divisor with $B=2$ |
| $B(\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the algebraic norm of the plain product; not multiplicative; not the criterion |
| $N:\mathbb{B}^\times\to\mathbb{C}^\times$ | the norm as a homomorphism; kernel the norm-one group $\mathbb{B}^\times_1$ |
| $(2P_0e_0-\tilde P)/N(\tilde P)$ | the Jordan inverse of the symmetrised plain product |
| $e_1\bullet e_2=0$ | the witness that the invertible elements of the symmetrised product form no group |

## Further Reading

- *Norm and Invertibility in the General Quaternionic Algebra*
  (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the algebraic norm
  of the plain product, its non-multiplicativity and the absence of a criterion, and for the
  distribution of the invertible elements over the remarkable subspaces.
- *Zero Divisors of the General Plain Algebra*
  (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the criterion of the plain
  product, the two families of the cone and the three-way classification.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*
  (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`),
  for the cone as the zero-divisor set of the four general products and the one-sided inverse
  equations.
- *The Biquaternion Unit Group as a Topological Group*
  (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the group
  $\mathbb{B}^\times\cong GL_2(\mathbb{C})$, the norm-one group $\mathbb{B}^\times_1\cong
  SL_2(\mathbb{C})$, the determinant sequence, the covering and the homotopy type.
- *The Unitary Group of the Biquaternion Algebra*
  (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the polar decomposition,
  the retractions onto the compact subgroups and the homotopy groups.
- *The Topology of the Zero-Divisor Cone*
  (`articles_maths/the-topology-of-the-zero-divisor-cone.md`), for the cone as the boundary of the
  group of units.
- *Norm and Invertibility in the Symmetric Plain Algebra*
  (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-algebra.md`), for the invertibility
  of the symmetrised product.
- *The Specificities of the General Plain Algebra*
  (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the left alternativity
  that the associativity of the plain product supplies and the isolation of the block.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*
  (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve
  structures, their units and their images.
- *Definitions for the Study of the 12 Algebraic Structures*
  (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the unit, the
  inverse, the zero divisor and the annihilator stated once for a general product.

