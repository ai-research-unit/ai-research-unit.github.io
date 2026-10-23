# __Comparison Between the Four General Products__

## Introduction

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are four binary rules on the same space, and it is natural to ask which of them deserves the name of multiplication. In the strict sense, of an associative multiplication with a two-sided unit over the field of scalars, only the general plain bilinear product does: the general quaternionic bilinear product is $\mathbb{C}$-bilinear but not associative and carries a unit on one side only, and the two sesquilinear products are not $\mathbb{C}$-bilinear at all, being conjugate-linear in their second argument. In the sense of the two objects the corpus has — an algebra in the sense of *Algebras*, and a sesqualgebra over $\mathbb{C}$ with its conjugation in the sense of *Sesqualgebras* — the four split two and two, and within the pair of sesquilinear ones the complex product is the one this series takes, being the derived operation of the algebra with the conjugate-linear involution. It is the third article of the group *The Four General Products* and carries the property table.

This article tabulates the properties that separate the four general products — bilinearity, associativity, commutativity, the units, the alternative and the flexible identities, the degree-three identity, and the left multiplications — and gives the short computation that decides each entry where it is not immediate. It also records the one construction that produces the four, the plain product with a conjugation inserted in a slot, and with it the reason exactly one of them is a multiplication. §*The Group of the Operations* reads the four insertions of that construction as the four elements of a group, of which the four general products are the four readings of one rule; the same section reads the construction on a general algebra with its two anti-involutions, where each slot decides its own property, and collects the settings in the Table of the Slots. The scalar and vector parts the four induce are not compared here; they are *Relations Between the Four General Products*.

The article assumes the four general products and their scalar–vector forms from *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and it uses the identities of *Relations Between the Four General Products* for the unit and the monoid rows. Throughout, $1=e_t$ is the unit of the algebra and $\vec Q_1$ is the vector part of $\tilde Q_1=Q_{1,0}+\vec Q_1$.

## The Property Table

The last two rows are the **algebra rows**, and they are the reason the comparison is made. They ask which of the four general products is a multiplication of an algebra of each of the two kinds the corpus has, and each is read with the corpus's own definition of the object and with nothing added to it. **Multiplication of a bilinear $\mathbb{C}$-algebra** is the product of an algebra in the sense of *Algebras*: a $\mathbb{C}$-module with a product additive in each variable and $\mathbb{C}$-bilinear, with no associativity and no unit assumed, so $(\lambda\tilde Q_1)\tilde Q_2 = \lambda(\tilde Q_1\tilde Q_2)$ and $\tilde Q_1(\lambda\tilde Q_2) = \lambda(\tilde Q_1\tilde Q_2)$. **Multiplication of a sesqualgebra over $\mathbb{C}$** is the product of an algebra in the sense of *Sesqualgebras*: additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, so $(\lambda\tilde Q_1)\tilde Q_2 = \lambda(\tilde Q_1\tilde Q_2)$ and $\tilde Q_1(\lambda\tilde Q_2) = \bar\lambda(\tilde Q_1\tilde Q_2)$, the base involution being the conjugation $\varsigma(z)=\bar z$. The bilinear case is the trivial-involution collapse of the sesquilinear one, so the two kinds overlap in general; they do not overlap here. A product of full type carries only one involution (*Sesqualgebras*, §*The Collapse at the Identity*), and $\mathbb{B}$ is faithful, its products generate it and it has no nonzero left annihilator, so each of the four general products carries exactly one involution and lies in exactly one of the two rows.

| property | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
|---|---|---|---|---|
| $\mathbb{C}$-linear in the first argument | yes | yes | yes | yes |
| $\mathbb{C}$-linear in the second argument | yes | no | yes | no |
| associative | yes | no | no | no |
| commutative | no | no | no | no |
| $1$ is a left identity | yes | no | yes | no |
| $1$ is a right identity | yes | yes | no | no |
| alternative | yes | no | no | no |
| flexible | yes | no | no | no |
| degree-three identity | yes | no | no | no |
| left multiplications form a monoid | yes | no | yes | no |
| multiplication of an algebra over $\mathbb{C}$ | yes | no | yes | no |
| multiplication of a sesqualgebra over $\mathbb{C}$ | no | yes | no | yes |

The alternative row is satisfied automatically by the general plain bilinear product, which is associative, and it is the three other columns that the row decides. The degree-three row records the identity $\tilde Q_1(\tilde Q_1\tilde Q_1)=(\tilde Q_1\tilde Q_1)\tilde Q_1$ for the operation in question, which is how power associativity is tested for a product of this kind; in this and the two rows above it, juxtaposition stands for the operation of the row. The last two rows ask which of the four general products is a multiplication of an algebra of the two kinds the corpus has, with the definitions of the paragraph above the table and with nothing added to them. The test is the scalar rules alone, and it is decided by the second slot. When the second slot is read without a conjugation, as in $\tilde Q_1\tilde Q_2$ and in $\tilde Q_1^{\natural}\tilde Q_2$, the product is $\mathbb{C}$-bilinear and belongs to the bilinear row; when it carries the star, as in $\tilde Q_1\tilde Q_2^{*}$ and in $\tilde Q_1^{\natural}\tilde Q_2^{*}$, the product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second and belongs to the sesquilinear row. The witness for each exclusion is one scalar, $\lambda = i$, and one pair, $\tilde Q_1 = \tilde Q_2 = e_t$: for the two bilinear products $\tilde Q_1(i\tilde Q_2) = ie_t$ while $\bar\imath(\tilde Q_1\tilde Q_2) = -ie_t$, so they are not $\varsigma$-sesquilinear for the conjugation; and for the two star-products $\tilde Q_1(i\tilde Q_2) = -ie_t$ while $i(\tilde Q_1\tilde Q_2) = ie_t$, so they are not $\mathbb{C}$-bilinear. The four therefore split two and two by the involution each carries, the bilinear row reading yes, no, yes, no and the sesquilinear row no, yes, no, yes. Neither row separates the second column from the fourth, and none should: the two star-products differ only in the first slot, and ${}^{\natural}$ is $\mathbb{C}$-linear, so both are sesquilinear for the same conjugation. What separates them is the unit, and it is the row "$1$ is a right identity" above: the general plain sesquilinear product has $e_t$ on the right and the complex quaternionic one has not. Equivalently, only the general plain sesquilinear product is the **derived operation** $\tilde Q_1\star\tilde Q_2 = \tilde Q_1\tilde Q_2^{*}$ of $\mathbb{B}$ with its conjugate-linear involution, the standard example of *Sesqualgebras* and the structure of *Introduction to the General Plain Sesqualgebra*. The bilinear row is weakened in the same way by the absence of a qualifier: the sharper statement, that exactly one of the four general products is the multiplication of an **associative unital** $\mathbb{C}$-algebra, is §*Which of the Four Is a Multiplication* below, and it holds because the ${}^{\natural}$-product is neither associative nor two-sidedly unital.

## Bilinearity and Sesquilinearity

The first two rows are read off the definitions. Each of the four general products is $\mathbb{C}$-linear in the first argument: the first factor is either untouched or conjugated by the $\mathbb{C}$-linear map ${}^{\natural}$, and the rest of the computation is linear in it. In the second argument, the general plain bilinear product and the ${}^{\natural}$-product are $\mathbb{C}$-linear, while the two products carrying the star are conjugate-linear, since ${}^{*}$ conjugates the coefficients of the second factor before the multiplication.

The distinction is not a technicality of the definitions: it separates the two rows of the scalar and vector tables of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* that involve $\overline{\vec Q}$, and it is the reason the fourth column carries no unit and no monoid. It also settles what the four can be used for. A $\mathbb{C}$-bilinear operation on $\mathbb{B}$ defines on $\mathbb{B}$ the structure of an algebra over $\mathbb{C}$, associative or not; a conjugate-linear operation defines no such thing, and the two sesquilinear products are the multiplications of a sesqualgebra over $\mathbb{C}$ instead. The first of the two is nonetheless the multiplication of a sesqualgebra over $\mathbb{C}$ with its conjugation, being the derived operation of the algebra with the star, and that is a multiplication in the second sense the corpus admits (*Introduction to the General Plain Sesqualgebra*); the second is not, since it reads the first factor through the $\mathbb{C}$-linear ${}^{\natural}$ as well. The four remain binary operations of the same kind, with the same two-step rule for their computation.

**The two exchanges, and the class.** The four general products are split against an exchange of the two arguments, and there are two of them. The **exchange by a conjugation** $c$, $f^{c}(\tilde{Q}_1,\tilde{Q}_2)=c(f(\tilde{Q}_2,\tilde{Q}_1))$, composes the swap with $c$ and keeps the class of the two sesquilinear products, whose parts under it are sesquilinear again; the conjugation and the swap repair each other's parity, and this is the exchange the twelve names are read against. The **plain exchange** swaps the arguments and does not keep the class: a part of a sesquilinear product taken under it is only $\mathbb{R}$-bilinear, since the swap moves the conjugate-linear slot to the other side, and its two halves are the operations of *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*. For the plain sesquilinear product and $c=\overline{\cdot}$ the two parts are the scalar part and the vector part of the product, $Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ and $-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$; for the general quaternionic sesquilinear product they are the symmetrisation of $\tilde{Q}_1^{\natural}$ with $\tilde{Q}_2^{*}$ and half their commutator. The two exchanges and their two splits are read in *The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*, and in *The 12 Products of the Biquaternion Complex Space*, §*The Method of the Decomposition*.

## The Failure of Associativity

The general plain bilinear product is associative, being the complex-linear extension of the associative quaternion product. The other three products fail it, and each fails it on a triple of basis elements:

$$
(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}\tilde Q_3\neq\tilde Q_1^{\natural}(\tilde Q_2^{\natural}\tilde Q_3)
\quad\text{for}\quad \tilde Q_1=\tilde Q_2=-\vec e_y,\ \tilde Q_3=\vec e_y ,
$$

where the left-hand side is $\vec e_y$ and the right-hand side is $-\vec e_y$; and

$$
(\tilde Q_1\tilde Q_2^{*})\tilde Q_3^{*}\neq\tilde Q_1(\tilde Q_2\tilde Q_3^{*})^{*}
\quad\text{for}\quad \tilde Q_1=-\vec e_z,\ \tilde Q_2=\tilde Q_3=\vec e_y ,
$$

where the left-hand side is $\vec e_z$ and the right-hand side is $-\vec e_z$. For the fourth product,

$$
(\tilde Q_1^{\natural}\tilde Q_2^{*})^{\natural}\tilde Q_3^{*}\neq\tilde Q_1^{\natural}(\tilde Q_2^{\natural}\tilde Q_3^{*})^{*}
\quad\text{for}\quad \tilde Q_1=-\vec e_z,\ \tilde Q_2=\vec e_z,\ \tilde Q_3=e_t ,
$$

with left-hand side $e_t$ and right-hand side $-e_t$. In each case the two sides differ by the sign of a single basis element, and the reason is the same in all three: associativity of the general plain bilinear product lets the parentheses be dropped, and the operation then conjugates a factor and so transposes two of them. For the ${}^{\natural}$-product, for instance, $(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1$, so the two sides of the associative identity read $\tilde Q_2^{\natural}\tilde Q_1\tilde Q_3$ and $\tilde Q_1^{\natural}\tilde Q_2^{\natural}\tilde Q_3$, which differ by the transposition of $\tilde Q_1$ and $\tilde Q_2^{\natural}$ alone.

The failure is not repaired by the symmetry of the scalar parts, because that symmetry is a statement about the scalar parts alone. In the first two counterexamples the two sides have the same scalar part, namely zero, and differ in the vector part, and in the third the scalar part changes sign; associativity is a statement about elements, and it is decided on the vector parts.

## Identities and Units

The unit $1=e_t$ of the algebra is a unit for the general plain bilinear product on both sides. For the other three the two sides must be asked separately: ${}^{\natural}$ and ${}^{*}$ both fix the unit, $1^{\natural}=1^{*}=1$, but each of the three operations conjugates the other factor.

For the ${}^{\natural}$-product, $1^{\natural}\tilde Q_2=\tilde Q_2$, so $1$ is a left identity; and $\tilde Q_1^{\natural}1=\tilde Q_1^{\natural}$, which equals $\tilde Q_1$ only when $\tilde Q_1$ is fixed by ${}^{\natural}$, so $1$ is not a right identity, and there is no right identity, since a right identity $E$ would give $\tilde Q_1^{\natural}E=\tilde Q_1$ for all $\tilde Q_1$, hence $E=1$ on taking $\tilde Q_1=1$ and then $\tilde Q_1^{\natural}=\tilde Q_1$ for all $\tilde Q_1$, which is false.

For the ${}^{*}$-product the two sides exchange roles. Here $\tilde Q_1\tilde Q_2^{*}$ leaves the first factor untouched, so $\tilde Q_1 1^{*}=\tilde Q_1$ and $1$ is a right identity, while $1\tilde Q_2^{*}=\tilde Q_2^{*}$ is not $\tilde Q_2$ in general, so $1$ is not a left identity and there is no left identity. This is the one entry of the naive table that is easy to get wrong: because $\tilde Q_2^{*}=\overline{Q_{2t}}e_t-\overline{\vec Q_2}$, the unit is conjugated to itself, and the star product is unital on the right and not on the left.

For the fourth product neither $1^{\natural}\tilde Q_2^{*}=\tilde Q_2^{*}$ nor $\tilde Q_1^{\natural}1=\tilde Q_1^{\natural}$ returns its argument, and the same argument as above shows there is no identity on either side.

## Alternative, Flexible and Power Associative

The three remaining rows record weaker forms of associativity, and each is settled by a short computation on basis elements, recorded below.

The **left alternative** identity is $\tilde Q_1(\tilde Q_1\tilde Q_2)=(\tilde Q_1\tilde Q_1)\tilde Q_2$, and a single failure of either the left or the right law denies alternativity, so it settles the row; it fails for the ${}^{\natural}$-product at $\tilde Q_1=\vec e_z$, $\tilde Q_2=-\vec e_z$, where the left-hand side is $\vec e_z$ and the right-hand side is $-\vec e_z$, for the ${}^{*}$-product at $\tilde Q_1=-\vec e_z$, $\tilde Q_2=\vec e_z$, with the same two values, and for the fourth product at $\tilde Q_1=e_t$, $\tilde Q_2=ie_t$, where the two sides are $ie_t$ and $-ie_t$. The **flexible** identity is $(\tilde Q_1\tilde Q_2)\tilde Q_1=\tilde Q_1(\tilde Q_2\tilde Q_1)$; it fails for the ${}^{\natural}$-product at $\tilde Q_1=\vec e_z$, $\tilde Q_2=e_t$, the two sides being $-e_t$ and $e_t$, for the ${}^{*}$-product at $\tilde Q_1=-\vec e_y$, $\tilde Q_2=e_t$, the two sides being $e_t$ and $-e_t$, and for the fourth product at $\tilde Q_1=ie_t$, $\tilde Q_2=e_t$, with the same two values. The **degree-three** identity $\tilde Q_1(\tilde Q_1\tilde Q_1)=(\tilde Q_1\tilde Q_1)\tilde Q_1$ fails for all three products: for the ${}^{\natural}$-product and for the ${}^{*}$-product at $\tilde Q_1=\vec e_z$, where the two sides are $-\vec e_z$ and $\vec e_z$ in the first case and $\vec e_z$ and $-\vec e_z$ in the second, and for the fourth product at $\tilde Q_1=i\vec e_z$, where the two sides are $i\vec e_z$ and $-i\vec e_z$.

The general plain bilinear product satisfies all three, being associative, and it is the only one of the four that does. The pattern is the one the table shows: the four general products have the four displayed scalar parts and are told apart by their vector parts, and every one of these identities is an identity of elements, hence decided on the vector parts.

## The Left Multiplications

The left multiplication by $\tilde Q_1$ is the map sending $\tilde Q_2$ to the value of the operation on the pair $(\tilde Q_1,\tilde Q_2)$. For the general plain bilinear product the left multiplications compose by $L_{\tilde Q_1}\circ L_{\tilde Q_3}=L_{\tilde Q_1\tilde Q_3}$, which is associativity, and they form a monoid. For the ${}^{\natural}$-product the same composition law holds in reversed order, $L^{\natural}_{\tilde Q_1}\circ L^{\natural}_{\tilde Q_3}=L^{\natural}_{\tilde Q_3\tilde Q_1}$, so the left multiplications form a monoid again, isomorphic to the opposite of the multiplicative monoid of $\mathbb{B}$; this is why the row of the table on the left multiplications reads yes, no, yes, no, the two sesquilinear products being excluded by the computation of *Relations Between the Four General Products*, where the composition of two of their left multiplications is shown to be linear and hence not one of them.

The row is not implied by the associative row. The ${}^{\natural}$-product is not associative, and its left multiplications still form a monoid, because the composition law holds in reversed order, by the anti-automorphism property of ${}^{\natural}$; and the two sesquilinear products fail the row for the reason given above, namely that the composition of two of their left multiplications leaves the class, which has nothing to do with the associativity of the underlying product.

## Which of the Four Is a Multiplication

The four rules are not unrelated: each is the **general plain bilinear product with a conjugation inserted in one or both slots**:

$$
\tilde Q_1^{\natural}\tilde Q_2 = \natural(\tilde Q_1)\,\tilde Q_2 , \qquad
\tilde Q_1\tilde Q_2^{*} = \tilde Q_1\,\natural(\bar{\tilde Q}_2) , \qquad
\tilde Q_1^{\natural}\tilde Q_2^{*} = \natural(\tilde Q_1)\,\natural(\bar{\tilde Q}_2) ,
$$

the general plain bilinear product itself being read with no insertion. Here the complex conjugation $\bar{\cdot}$ conjugates the coefficients, ${}^{\natural}$ negates the vector units, the two commute, and $\tilde Q_2^{*} = \natural(\bar{\tilde Q}_2) = \bar{\tilde Q_2^{\natural}}$. The map ${}^{\natural}$ is a $\mathbb{C}$-linear anti-automorphism of $\mathbb{B}$, and $\bar{\cdot}$ is an automorphism of its underlying real algebra that is conjugate-linear over $\mathbb{C}$ (*The Group of Involutions*). Two rows of the table are read off from the insertion: the reversed order in which the left multiplications of the $\natural$-product compose follows from the anti-automorphism, $\natural(\tilde Q_1\tilde Q_2) = \natural(\tilde Q_2)\natural(\tilde Q_1)$, and the conjugate-linearity in the second argument of the two star-products follows from the conjugate-linearity of $\bar{\cdot}$.

Only the general plain bilinear product is a multiplication in the sense of algebra. It is $\mathbb{C}$-bilinear in both arguments, associative, commutative in its scalar part alone, and unital with a two-sided unit; it is the product that makes $\mathbb{B}$ an associative algebra with unit over $\mathbb{C}$, and it is the one whose associated structures — the remarkable subspaces, the Jordan and the Lie structures of *The 12 Products of the Biquaternion Complex Space*, the zero divisors and the idempotents — the rest of the category develops.

The ${}^{\natural}$-product is $\mathbb{C}$-bilinear, and that is all: it is not associative and it is unital on the left only. It defines on the underlying vector space a non-associative algebra structure in the weak sense, one that agrees with the general plain bilinear product on the centre and disagrees on the vector parts; it is the product whose scalar part is the signless sum $\sum_\mu Q_{1,\mu} Q_{2,\mu}$.

The two products carrying the star are not multiplications of a bilinear $\mathbb{C}$-algebra at all: being conjugate-linear in their second argument they cannot be. Both are multiplications of a sesqualgebra over the conjugation, and within the pair they are separated by the unit. The general plain sesquilinear product is the derived operation $\tilde Q_1\star\tilde Q_2 = \tilde Q_1\tilde Q_2^{*}$ of $\mathbb{B}$ with its conjugate-linear involution, that is the standard example of the category, and $e_t$ is a right unit of it; the general quaternionic sesquilinear product reads the first factor through the $\mathbb{C}$-linear ${}^{\natural}$ as well and has no right unit, so it is a sesquilinear multiplication that is not the derived one (*Introduction to the General Plain Sesqualgebra*). The classification of the four general products is therefore: one multiplication of an associative unital algebra, one bilinear product that fails associativity and two-sidedness, and two multiplications of a sesqualgebra, of which the complex one is the derived operation with the right unit and the complex quaternionic one is not the derived operation and has no right unit.

The order of the four general products matches the order of the objects. The general plain bilinear product is the multiplication of the associative unital algebra; the general plain sesquilinear product is the derived operation, the multiplication the sesqualgebra takes; the two $\natural$-products are the same two products read with the $\mathbb{C}$-linear conjugation ${}^{\natural}$ inserted in the first slot, and the insertion of a $\mathbb{C}$-linear map changes the product without changing its sesquilinearity type.

Each of the four general products is read as a multiplication in an article of its own: the general plain bilinear product in *Introduction to the Biquaternion Algebra*, the general plain sesquilinear product in *Introduction to the General Plain Sesqualgebra*, the general quaternionic bilinear product in *Introduction to the General Quaternionic Algebra*, and the general quaternionic sesquilinear product in *Introduction to the General Quaternionic Sesqualgebra*; the entries of the table above are the statements those four articles prove or quote.

## The Group of the Operations

The four general products are four rules on one and the same space, and §*Which of the Four Is a Multiplication* reads each of the three others as the general plain bilinear product with a conjugation inserted in a slot. **The four insertions that appear there are the four elements of a group.** One insertion reads the first argument through the natural conjugation and one reads the second through the Hermitian conjugation; each of the two is its own inverse, the two commute, and the four are these two insertions, their composite and the identity. The group is of order four and elementary abelian, and the four general products are its four elements read on one and the same rule. **Each of the two generators touches one slot**, and it is that reading which decides which property of the four general products belongs to which slot: the group is read on the rules in §*The Readings and Their Group*, the same operation is read on a general algebra with its two anti-involutions in §*The Operation on a General Algebra*, the settings are collected in §*The Table of the Slots*, and the one setting whose square is central is §*The Square at One Setting*.

### The Readings and Their Group

**Definition (the two insertions and the four readings).** Let $f$ be a rule of two arguments on $\mathbb{B}$. The **first insertion** and the **second insertion** carry $f$ to the rules

$$
(\tilde Q_1,\tilde Q_2)\longmapsto f(\tilde Q_1^{\natural},\tilde Q_2),
\qquad
(\tilde Q_1,\tilde Q_2)\longmapsto f(\tilde Q_1,\tilde Q_2^{*}).
$$

The **four readings** of $f$ are $f$ itself, its image under the first insertion, its image under the second insertion, and its image under the composite of the two. Following the convention of *The Four General Products and Operators*, the readings are written (none), (${}^{\natural}$), (${}^{*}$) and (both), the label naming the insertions made: none, the first insertion, the second insertion, or both.

**Remark (why four readings and not sixteen).** The involutions at hand are four — $\mathrm{id}$, ${}^{\natural}$, the coefficient conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}$ — so insertions built from all four would a priori give sixteen readings. The four general products use only $\mathrm{id}$ or ${}^{\natural}$ in the first slot and only $\mathrm{id}$ or ${}^{*}$ in the second, and two features of that choice matter in this part. The first slot is $\mathbb{C}$-linear and never conjugates the coefficients, while the second is conjugate-linear whenever it is not the identity; that asymmetry is why the two slots are not interchangeable, and it is the source of every entry of §*The Table of the Slots*. And the two conjugations chosen are the ones that produce the split of §*Which of the Four Is a Multiplication*, in which the second slot alone decides whether the product is the multiplication of an algebra over $\mathbb{C}$ or of a sesqualgebra over $\mathbb{C}$. **The part asserts nothing about the other twelve readings**, and every statement in it is about the four.

**Theorem (the four readings form a group).** The four readings of any rule are closed under composition, and they form a group isomorphic to $\mathbb{Z}_2\times\mathbb{Z}_2$, of which (none) is the identity and of which the first insertion and the second insertion are two generators.

*Proof.* The first insertion applied twice returns the rule, since $\tilde Q_1^{\natural\natural}=\tilde Q_1$ and ${}^{\natural}$ is an involution, and the second insertion applied twice returns it for the same reason, ${}^{*}$ being an involution. Each of the two insertions is therefore its own inverse, and so is each of the four readings. The first insertion touches the first argument alone and the second the second argument alone, so the two commute, and their composite is the reading (both). The four readings are closed, every element is its own inverse, and the group is abelian of order four with exponent two, that is $\mathbb{Z}_2\times\mathbb{Z}_2$. The product is the table, in which the row is the first factor and the column the second.

| $\circ$ | (none) | (${}^{\natural}$) | (${}^{*}$) | (both) |
|---|---|---|---|---|
| (none) | (none) | (${}^{\natural}$) | (${}^{*}$) | (both) |
| (${}^{\natural}$) | (${}^{\natural}$) | (none) | (both) | (${}^{*}$) |
| (${}^{*}$) | (${}^{*}$) | (both) | (none) | (${}^{\natural}$) |
| (both) | (both) | (${}^{*}$) | (${}^{\natural}$) | (none) |

**Theorem (the four general products are one rule and its three readings).** Read on the general plain bilinear product, the four readings give the four general products,

$$
\boxed{\;
\tilde Q_1\tilde Q_2,
\qquad
\tilde Q_1^{\natural}\tilde Q_2,
\qquad
\tilde Q_1\tilde Q_2^{*},
\qquad
\tilde Q_1^{\natural}\tilde Q_2^{*}
\;},
$$

in the order (none), (${}^{\natural}$), (${}^{*}$), (both). The four are pairwise distinct, so the group permutes them faithfully and the orbit of the general plain bilinear product is the four. **The four general products are therefore one rule and the three modifications of it, a modification being one insertion.**

*Proof.* The three non-identity readings applied to the general plain bilinear product are the three formulas of §*Which of the Four Is a Multiplication*: the first insertion gives $\natural(\tilde Q_1)\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$, the second gives $\tilde Q_1\,\natural(\bar{\tilde Q}_2)=\tilde Q_1\tilde Q_2^{*}$, and the composite gives $\natural(\tilde Q_1)\natural(\bar{\tilde Q}_2)=\tilde Q_1^{\natural}\tilde Q_2^{*}$. The four are pairwise distinct, by *Relations Between the Four General Products*, and each non-identity reading moves the general plain bilinear product, since it changes the first element, the second, or both; the orbit is therefore the four general products and the action is faithful.

**Corollary (the group is the two slots).** Each generator touches one slot alone, so a property that depends on one slot alone is carried by one generator, a property that depends on both requires the two, and a property that sees neither is carried by the whole group. **The two generators of the group are the two slots**, and the property table above reads row by row along them: §*The Table of the Slots* gives the rule that places each row.

**Corollary (the same group on the pairings and on the Gram matrices).** Read on the scalar part of a rule, the four readings give the four pairings, whose Gram matrices in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ are $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$ in the order (none), (${}^{\natural}$), (${}^{*}$), (both). The coefficient $\varepsilon=(1,-1,-1,-1)$ survives therefore for exactly the two readings in which the two insertions agree, (none), where neither is applied, and (both), where both are, and it is replaced by $1$ for the two in which they differ; that alternation is the sign matrix $\mathrm{E}$ against the identity $\mathrm{I}_4$ of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

**Remark (the group of the operations is not the group of the involutions).** The four readings are operations on rules, and the group they form is generated by the two insertions; the group of *The Group of Involutions*, generated by the natural conjugation ${}^{\natural}$ and the coefficient conjugation $\bar{\cdot}$, is a group of maps of the algebra. Both are elementary abelian of order four, and they are not the same group: the elements of the first are readings of a rule and the elements of the second are conjugations of an element. **A reading is not a conjugation of an element**, and the four general products are the four readings of one rule and not the four conjugations of one element.

**Remark (the identity element, and what the group does not produce).** The group has an identity element, the reading with no insertion, and read on the general plain bilinear product that reading is the general plain bilinear product itself. The four general products are nevertheless introduced independently, one by one on the coordinates, in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the group is read on the four afterwards; it is read in the same way on the four pairings, which are the scalar parts. What the group does not produce is an operator: its four elements act on rules, an operator acts on elements, and an operator needs an element of the algebra beside the reading (*The Four General Products and Operators*).

### The Operation on a General Algebra

An insertion is an operation on a rule of two arguments, and nothing in its definition uses the multiplication of $\mathbb{B}$: the operation is available on the multiplication of any algebra carrying the two conjugations. The four readings of that multiplication are then four products again, and they are the **slot family** of the algebra; the four general products are its instance $\mathbb{B}$, and the two generators of §*The Readings and Their Group* are the two slots of the family.

**Definition (the slot family).** Let $A$ be a unital associative $\mathbb{C}$-algebra, and let $\natural$ and $\varsigma$ be involutive anti-automorphisms of $A$ that commute, with $\natural$ $\mathbb{C}$-linear, $\varsigma$ conjugate-linear and $\natural(1)=\varsigma(1)=1$. For $K_1\in\{\mathrm{id},\natural\}$ and $K_2\in\{\mathrm{id},\varsigma\}$ put

$$
x\star_{K_1K_2}y=K_1(x)\,K_2(y).
$$

The **first slot** is $K_1$ and the **second slot** is $K_2$. In $\mathbb{B}$, with $A=\mathbb{B}$, $\natural$ the natural conjugation and $\varsigma$ the Hermitian conjugation, the four settings are the four general products in the order of the readings, $\star_{\mathrm{id}\,\mathrm{id}}$, $\star_{{}^{\natural}\mathrm{id}}$, $\star_{\mathrm{id}{}^{*}}$ and $\star_{{}^{\natural}{}^{*}}$.

**Theorem (the second slot rules the composition).** With $A$, $\natural$, $\varsigma$ as in the definition, let $K_1\in\{\mathrm{id},\natural\}$, $K_2\in\{\mathrm{id},\varsigma\}$ and $x\star y=x\star_{K_1K_2}y$. The following four statements are equivalent.

- $K_2=\mathrm{id}$.
- $\star$ is $\mathbb{C}$-bilinear in its second argument.
- $1$ is a left unit for $\star$: $1\star x=x$ for every $x$.
- The left multiplications $L_x:x'\mapsto x\star x'$ of $\star$ are closed under composition.

When they hold, $L_x\circ L_y=L_{xy}$ if $K_1=\mathrm{id}$ and $L_x\circ L_y=L_{yx}$ if $K_1={}^{\natural}$, so that the monoid of left multiplications is $A$ in the first case and the opposite monoid of $A$ in the second. When they fail, $L_x\circ L_y$ is $\mathbb{C}$-linear in its argument while every $L_z$ is conjugate-linear, so the composition is not a left multiplication at all.

*Proof.* ($K_2=\mathrm{id}$ implies bilinear and left unit.) $x\star(\lambda y)=K_1(x)\lambda y=\lambda(x\star y)$, and $1\star x=K_1(1)x=x$ since $\natural(1)=1$. ($K_2=\mathrm{id}$ implies closure.) $(L_x\circ L_y)(x')=K_1(x)K_1(y)x'$, which is $(xy)x'=L_{xy}(x')$ when $K_1=\mathrm{id}$ and $\natural(x)\natural(y)x'=\natural(yx)x'=L_{yx}(x')$ when $K_1={}^{\natural}$, the middle step because $\natural$ is an anti-automorphism.

(Bilinear implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$. Then $1\star(\lambda 1)=K_1(1)\varsigma(\lambda)1=\varsigma(\lambda)$, while $\lambda(1\star1)=\lambda$, and $\varsigma(\lambda)=\lambda$ fails at $\lambda=i$; so $\star$ is not $\mathbb{C}$-bilinear in its second argument, while it is $\mathbb{C}$-linear in the first, since $K_1$ is.

(Left unit implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$ and $1\star x=x$ for every $x$. Then $\varsigma(x)=1\star x=x$, so $\varsigma=\mathrm{id}$ against the hypothesis.

(Closure implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$. Then $1\star(1\star x)=\varsigma(\varsigma(x))=x$, so $L_1\circ L_1$ is the identity, while $L_z(\lambda x')=K_1(z)\varsigma(\lambda x')=\varsigma(\lambda)L_z(x')$ for every $z$, and $\varsigma\neq\mathrm{id}$; the identity is therefore not a left multiplication.

**Theorem (the first slot rules the right unit).** With the hypotheses and notation of the previous theorem, $1$ is a right unit for $\star$ if and only if $K_1=\mathrm{id}$.

*Proof.* $x\star 1=K_1(x)K_2(1)=K_1(x)$, since $\varsigma(1)=1$; this is $x$ for every $x$ if and only if $K_1=\mathrm{id}$.

**Corollary (the units, in the two slots).** $1$ is a left unit for the two settings whose second slot is trivial and a right unit for the two whose first slot is trivial, so exactly one of the four has a two-sided unit. These are the four unit entries of the property table above and of §*Identities and Units*, where a left unit is called a left identity, and the reason for them is the two slots.

**Theorem (associativity needs both slots trivial, in $\mathbb{B}$).** In $\mathbb{B}$ the product $\star_{K_1K_2}$ is associative if and only if $K_1=\mathrm{id}$ and $K_2=\mathrm{id}$.

*Proof.* The product $\star_{\mathrm{id}\,\mathrm{id}}$ is the multiplication of the associative algebra $\mathbb{B}$. For the converse, each of the other three settings is excluded by a triple of §*The Failure of Associativity*: $(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(-\vec e_y,-\vec e_y,\vec e_y)$ at the setting $({}^{\natural},\mathrm{id})$, $(-\vec e_z,\vec e_y,\vec e_y)$ at $(\mathrm{id},{}^{*})$, and $(-\vec e_z,\vec e_z,e_t)$ at $({}^{\natural},{}^{*})$, the two sides differing by the sign of a single basis element in each case.

**Remark (the first two theorems are theorems about the family, the third is not).** The two slot theorems hold in any $A$ of the definition, because their proofs use only that $\varsigma$ is conjugate-linear and not linear and that $\natural$ is an anti-automorphism. Associativity is not read on the slots: when both anti-involutions are the identity the four settings coincide, and with them associativity, so no rule stated in the two slots alone can hold for the whole family at once. Associativity is therefore decided in $\mathbb{B}$, by the triples above, and it remains the row of the property table that the slots do not read.

### The Table of the Slots

The two slot theorems, the pairings and the square collect into one table, one row for each property of the four general products, with the slot that carries the property and the rule it follows. The italic entries are the two that are not read on the slots of the general family.

| property of $\star_{K_1K_2}$ | decided by | the rule |
|---|---|---|
| $\mathbb{C}$-bilinear in the second argument | the second slot | yes if and only if $K_2=\mathrm{id}$ |
| $1$ is a left unit | the second slot | yes if and only if $K_2=\mathrm{id}$ |
| the left multiplications compose | the second slot | yes if and only if $K_2=\mathrm{id}$ |
| $1$ is a right unit | the first slot | yes if and only if $K_1=\mathrm{id}$ |
| the coefficient $\varepsilon$ survives in the scalar part | the two slots | yes if and only if the two slots agree |
| the Hermitian reading is positive definite | exactly one setting | only at $(\mathrm{id},{}^{*})$ |
| the form is definite on each sector | the first slot | yes if and only if $K_1=\mathrm{id}$ |
| $1$ is a two-sided unit | the two slots | yes if and only if $K_1=K_2=\mathrm{id}$ |
| *associative* | the two slots | yes if and only if $K_1=K_2=\mathrm{id}$, in $\mathbb{B}$ |
| *the square is scalar* | exactly one setting | only at $({}^{\natural},\mathrm{id})$ |

The first four rows are the slot reading of the property table of §*The Property Table*, whose columns are the four general products. The fifth is the coefficient $\varepsilon$ of the corollary on the pairings, and the sixth and the seventh are the two form rows, the Hermitian reading on the whole space and the form on the two sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ of dimension four; they are the rows of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, which owns the forms and their signatures. The eighth is the two unit rows together, and the last two are the two rows that the slots do not decide, associativity in §*The Operation on a General Algebra* and the scalar square in §*The Square at One Setting*.

The table says that the second slot governs the **composition**: iterating the operation, the unit acting on the left and the left multiplications forming a monoid are one property of one slot. The first slot governs the **form**: the unit acting on the right, the definiteness of the form on a sector and, jointly with the second slot, the survival of the coefficient $\varepsilon$. A product in the right-hand column is a pairing and not a composition, and no choice in the first slot repairs that.

### The Square at One Setting

**Theorem (the square is scalar at exactly one setting).** In $\mathbb{B}$, $\tilde Q\star_{K_1K_2}\tilde Q$ is a scalar, that is a multiple of $e_t$, if and only if $(K_1,K_2)=({}^{\natural},\mathrm{id})$; and then $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$ with $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$.

*Proof.* By §*The Squares, the Idempotents and the Roots* the ${}^{\natural}$-square is $\langle\tilde Q\rangle_{\natural}e_t$ for every element, the norm form of the quaternion algebra $\mathbb{B}$ taking its values in the centre $\mathbb{C}e_t$. Each of the other three settings is excluded by one element: at the reading (none) the element $e_t+\vec e_x$ has the square $2\vec e_x$, at the reading (${}^{*}$) the element $e_t+i\vec e_x$ has the square $2e_t+2i\vec e_x$, and at the reading (both) the element $e_t+\vec e_x$ has the square $-2\vec e_x$; none of the three is a scalar.

**Remark (this rule is not general).** The rule uses that $\natural$ is the standard involution of a quaternion algebra and that its norm form therefore lands in the centre, and it fails as soon as the algebra is changed and the involution kept. In the matrix algebra $M_2(\mathbb{C})$ with the transpose in the role of $\natural$, the element

$$
\begin{pmatrix}0&1\\0&0\end{pmatrix}
\quad\text{has the square}\quad
\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$

which is not a scalar multiple of $\mathrm{I}_2$. **The scalar square is a property of $\mathbb{B}$ and not of the slot family**, and it is the row of the table of §*The Table of the Slots* that assigns the ${}^{\natural}$-product its place among the four.

## The Squares, the Idempotents and the Roots

The four general products are told apart on a single element by the **square**, and the idempotent and the root problems follow from it. Writing $\tilde Q_1 = Q_{1,0}e_t + \vec Q_1$ and $(\vec Q_1,\vec Q_1) = Q_{1,1}^2 + Q_{1,2}^2 + Q_{1,3}^2$, the scalar part of the square is

$$
\boxed{\;
\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_1\bigr) = Q_{1,0}^2 - (\vec Q_1,\vec Q_1), \qquad
\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_1^{*}\bigr) = \sum_\mu\lvert Q_{1,\mu}\rvert^2
\;},
$$

$$
\boxed{\;
\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_1\bigr) = Q_{1,0}^2 + (\vec Q_1,\vec Q_1) = \langle\tilde Q_1\rangle_{\natural}, \qquad
\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_1^{*}\bigr) = \lvert Q_{1,0}\rvert^2 - \sum_k\lvert Q_{1,k}\rvert^2
\;}.
$$

These are the four algebraic norms of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, and the same four expressions are the scalar parts of the four general products of *Relations Between the Four General Products*. Two of them decide the two problems on the spot. The $\natural$-square lies in the centre for every element, being $\langle\tilde Q_1\rangle_{\natural}e_t$, so its roots of a central value are the single equation $\langle\tilde Q_1\rangle_{\natural} = \lambda$. The general plain sesquilinear square has the **non-negative** scalar part $\sum_\mu\lvert Q_{1,\mu}\rvert^2$, so that product has no root of a negative value at all. The remaining two squares are elements, and their scalar parts are the indefinite general plain bilinear and Krein values.

| problem | $\tilde Q_1\tilde Q_1 = \tilde Q_1$ | $\tilde Q_1\tilde Q_1^{*} = \tilde Q_1$ | $\tilde Q_1^{\natural}\tilde Q_1 = \tilde Q_1$ | $\tilde Q_1^{\natural}\tilde Q_1^{*} = \tilde Q_1$ |
|---|---|---|---|---|
| idempotents | $0$, $e_t$, and $\tfrac12(e_t + \tilde\Xi i)$ for a root $\tilde\Xi$ of $-e_t$ | $0$, $e_t$, and the Hermitian idempotents $\tfrac12(e_t + \tilde\Xi)$ with $\vec u$ a real unit vector | $0$ and $e_t$ alone | $0$, $e_t$, and $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ for a real $\vec u$ of the vector subspace with $(\vec u,\vec u)=1$ |

The four columns are four different sets. The first is infinite and is the one the rest of the category uses; the second is the family of the pure states of *Idempotents of the General Plain Algebra*; the third is the smallest possible, the two trivial idempotents; the fourth is a family of a different kind, lying in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$.

The square roots of a central value differ in the same way and by the same two structural facts.

| square roots | $\tilde Q_1\tilde Q_1 = \lambda e_t$ | $\tilde Q_1\tilde Q_1^{*} = \lambda e_t$ | $\tilde Q_1^{\natural}\tilde Q_1 = \lambda e_t$ | $\tilde Q_1^{\natural}\tilde Q_1^{*} = \lambda e_t$ |
|---|---|---|---|---|
| of $-e_t$ | $Q_{1,0} = 0$ with $(\vec Q_1,\vec Q_1) = 1$, and $Q_{1,0} = \pm i$ | none | the solutions of $\langle\tilde Q_1\rangle_{\natural} = -1$ | the solutions of $\tilde Q_1^{\natural}\tilde Q_1^{*} = -e_t$, among them every real pure $\vec Q_1$ with $(\vec Q_1,\vec Q_1) = 1$ |
| of $0$ | $Q_{1,0} = 0$ with $(\vec Q_1,\vec Q_1) = 0$, the nilpotents $\vec\Upsilon$ | $\tilde Q_1 = 0$ alone | the solutions of $\langle\tilde Q_1\rangle_{\natural} = 0$, the zero divisors together with $0$ | the solutions of $\tilde Q_1^{\natural}\tilde Q_1^{*} = 0$, among them $e_t + i\vec e_x$ |

The three families of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* are therefore the three parts of one column of this table, the column of the general plain bilinear product, and not a classification of the square of the algebra in general. The other three columns are the same three equations read in the other products, and each of the other three has its reading in the article of that product.

## Summary

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are compared in the table above. Each is $\mathbb{C}$-linear in the first argument; the general plain bilinear product and the ${}^{\natural}$-product are $\mathbb{C}$-linear in the second, the two products carrying the star are conjugate-linear there. The general plain bilinear product is associative, has the two-sided unit $1$, is alternative, flexible and satisfies the degree-three identity, and its left multiplications form a monoid; the ${}^{\natural}$-product is $\mathbb{C}$-bilinear and has the left unit $1$ alone, and it fails associativity, the alternative identities, flexibility and the degree-three identity, as do the two sesquilinear products, which have no identity at all and whose left multiplications do not even form a monoid. Counterexamples are given in each case on the basis elements $e_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$ and on $ie_t$ and $i\vec e_z$.

Both products without the star are multiplications of a bilinear $\mathbb{C}$-algebra, and exactly one of them is a multiplication of an associative unital one, the general plain bilinear product: the ${}^{\natural}$-product is $\mathbb{C}$-bilinear but neither associative nor two-sidedly unital. Both products carrying the star are multiplications of a sesqualgebra over $\mathbb{C}$ with the conjugation. Among the two, the general plain sesquilinear product is the derived operation of $\mathbb{B}$ with its conjugate-linear involution and has $e_t$ as a right unit, and the general quaternionic sesquilinear product is neither. Each of the four is the plain product with a conjugation inserted in one or both slots, and that single construction is the reason the table reads as it does. The construction is a group: the two insertions are commuting involutions, so the four readings of a rule — (none), the first insertion, the second insertion and both — are the four elements of a group isomorphic to $\mathbb{Z}_2\times\mathbb{Z}_2$, of which the general plain bilinear product is the identity element read on the algebra. The group is the two slots of the general construction, and read on a general algebra with its two anti-involutions it gives the slot family, in which the second slot carries the $\mathbb{C}$-bilinearity in the second argument, the left unit, the monoid and the two algebra rows, and the first slot carries the right unit; the two rows that the slots do not decide are associativity, which the counterexamples of §*The Failure of Associativity* settle in $\mathbb{B}$, and the scalar square, which holds at $({}^{\natural},\mathrm{id})$ alone. The same group read on the scalar parts gives the four pairings with the Gram matrices $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$, the coefficient $\varepsilon$ surviving exactly when the two insertions agree. The identities that link the four general products are *Relations Between the Four General Products*, and the split of the general plain bilinear product into a symmetric and an antisymmetric half, with the Jordan and the Lie structure the halves carry, is *The 12 Products of the Biquaternion Complex Space*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the four general products, defined in *The Four General Products of the Biquaternion $\mathbb{C}$ Space* |
| $1=e_t$ | the unit of the algebra, fixed by ${}^{\natural}$ and by ${}^{*}$ |
| $\vec e_x$, $\vec e_y$, $\vec e_z$ | the quaternion units, with $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ |
| $L_{\tilde Q_1}$, $L^{*}_{\tilde Q_1}$, $L^{\natural}_{\tilde Q_1}$, $L^{\natural*}_{\tilde Q_1}$ | the left multiplications of the four general products |
| $f(\tilde Q_1,\tilde Q_2)\mapsto f(\tilde Q_1^{\natural},\tilde Q_2)$ | the first insertion, the one that reads the first argument through the natural conjugation |
| $f(\tilde Q_1,\tilde Q_2)\mapsto f(\tilde Q_1,\tilde Q_2^{*})$ | the second insertion, the one that reads the second argument through the Hermitian conjugation |
| (none), (${}^{\natural}$), (${}^{*}$), (both) | the four readings of a rule; they are the four elements of a group $\mathbb{Z}_2\times\mathbb{Z}_2$ under composition |
| $\natural$, $\varsigma$ | the two commuting anti-involutions of a general algebra, $\natural$ linear and $\varsigma$ conjugate-linear, in the slot family |
| $\star_{K_1K_2}$ | the general product $x\star_{K_1K_2}y=K_1(x)K_2(y)$ of the slot family, with $K_1$ the first slot and $K_2$ the second |
| $\mathrm{E}$, $\mathrm{I}_4$ | the Gram matrices of the pairings of the readings in which the two insertions agree and differ |
| $\vec Q_1$ | the vector part of $\tilde Q_1=Q_{1,0}+\vec Q_1$ |

## Further Reading

- [The Four General Products of the Biquaternion $\mathbb{C}$ Space](the-four-general-products-of-the-biquaternion-c-space.html), for the four definitions and their scalar–vector forms.
- [Relations Between the Four General Products](relations-between-the-four-general-products.html), for the identities that link the four general products and for the left multiplications.
- [The Group of Involutions](the-group-of-involutions.html), for the natural and the complex conjugation as an anti-automorphism and an automorphism and for the group they generate, which is a group of maps of the algebra and not the group of the readings of a rule.
- [The Four General Products and Operators](the-four-general-products-and-operators.html), for the convention that writes the four insertions (none), (${}^{\natural}$), (${}^{*}$) and (both), for the four adjoints they decide and for the operator they do not.
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the four pairings of the readings, their Gram matrices $\mathrm{E}$ and $\mathrm{I}_4$ and their signatures.
- [The 12 Products of the Biquaternion Complex Space](the-12-products-of-the-biquaternion-complex-space.html), for the symmetric and the antisymmetric part of each of the four general products, and the Jordan and the Lie structure the two parts of the general plain bilinear product carry.
- [Remarkable Subspaces and the Four General Products](remarkable-subspaces-and-the-four-general-products.html), for the four general products on the remarkable subspaces, and for the Jordan and the Lie algebra each of the remarkable subspaces carries and with which product.
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the sesquilinear reading of the general plain sesquilinear product and the algebra it defines.
- [Sesqualgebras](sesqualgebras.html), for the two scalar rules, the collapse theorem and the standard example that the sesquilinear row of the table tests.
